import fs from 'node:fs/promises';
import path from 'node:path';
import process from 'node:process';
import fetch from 'node-fetch';
import dotenv from 'dotenv';

dotenv.config({ path: path.resolve(process.cwd(), 'skills/facebook-page-autopost/.env') });

function requireEnv(name) {
  const v = process.env[name];
  if (!v) {
    console.error(`Missing required env var: ${name}`);
    process.exit(2);
  }
  return v;
}

function todayStr() {
  const d = new Date();
  const yyyy = d.getFullYear();
  const mm = String(d.getMonth() + 1).padStart(2, '0');
  const dd = String(d.getDate()).padStart(2, '0');
  return `${yyyy}-${mm}-${dd}`;
}

async function fileExists(p) {
  try {
    await fs.stat(p);
    return true;
  } catch {
    return false;
  }
}

async function findImage(baseNoExt) {
  for (const ext of ['.jpg', '.jpeg', '.png', '.webp']) {
    const p = baseNoExt + ext;
    if (await fileExists(p)) return p;
  }
  return null;
}

async function graphUploadPhoto({ apiVersion, pageId, accessToken, imagePath, caption }) {
  const url = `https://graph.facebook.com/${apiVersion}/${pageId}/photos`;

  const blob = await fs.readFile(imagePath);
  const form = new FormData();
  form.append('caption', caption);
  form.append('access_token', accessToken);
  form.append('source', new Blob([blob]));

  const res = await fetch(url, { method: 'POST', body: form });
  const json = await res.json();

  if (!res.ok) {
    const msg = JSON.stringify(json, null, 2);
    throw new Error(`Facebook API error (${res.status}): ${msg}`);
  }

  return json;
}

async function main() {
  const FB_PAGE_ID = requireEnv('FB_PAGE_ID');
  const FB_PAGE_ACCESS_TOKEN = requireEnv('FB_PAGE_ACCESS_TOKEN');
  const FB_API_VERSION = process.env.FB_API_VERSION || 'v19.0';

  const postsDir = path.resolve(process.cwd(), 'skills/facebook-page-autopost/posts');
  const stamp = todayStr();

  const captionPath = path.join(postsDir, `${stamp}.txt`);
  const imageBase = path.join(postsDir, `${stamp}`);
  const imagePath = await findImage(imageBase);

  if (!(await fileExists(captionPath))) {
    console.error(`No caption file found for today: ${captionPath}`);
    process.exit(3);
  }
  if (!imagePath) {
    console.error(`No image file found for today. Expected one of: ${imageBase}.jpg/.png/.webp`);
    process.exit(3);
  }

  const caption = (await fs.readFile(captionPath, 'utf8')).trim();
  if (!caption) {
    console.error(`Caption file is empty: ${captionPath}`);
    process.exit(3);
  }

  console.log(`Posting to Facebook Page ${FB_PAGE_ID} with image ${path.basename(imagePath)} ...`);
  const out = await graphUploadPhoto({
    apiVersion: FB_API_VERSION,
    pageId: FB_PAGE_ID,
    accessToken: FB_PAGE_ACCESS_TOKEN,
    imagePath,
    caption,
  });

  console.log('Success:', out);

  // Mark as sent
  const sentCaption = captionPath + '.sent';
  const sentImage = imagePath + '.sent';
  await fs.rename(captionPath, sentCaption);
  await fs.rename(imagePath, sentImage);

  console.log(`Marked as sent:\n- ${path.basename(sentCaption)}\n- ${path.basename(sentImage)}`);
}

main().catch((err) => {
  console.error(err?.stack || String(err));
  process.exit(1);
});
