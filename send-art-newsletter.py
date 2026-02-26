#!/usr/bin/env python3
"""
Levison Gallery Art Newsletter Sender
Send new paintings updates to art customers twice weekly
Usage: Configure images in Google Drive, then run this script
"""

import os
import json
import urllib.request
import urllib.parse

# Load buyers
with open('/home/charlesclaw/.openclaw/workspace/art-buyers.json') as f:
    data = json.load(f)
    buyers = [c['email'] for c in data['art_customers']]

MATON_API_KEY = os.environ.get('MATON_API_KEY')

# Email template - customize this
SUBJECT = "New Painting Available at Wildlife Center in Lilongwe"
BODY = """Dear Art Lover,

A stunning new piece is now available at Wildlife Center in Lilongwe!

🎨 This Week's Featured Work:
See the attached image for details.

Each piece is original and ready for your collection.

Best regards,
Charles Levison
Levison Gallery

---
You received this because you're a valued collector.
To unsubscribe, reply with "unsubscribe"
"""

IMAGE_PATH = "/home/charlesclaw/.openclaw/media/inbound/file_4---19f5ce4d-404a-4f04-8d65-8f31f1c8120e.jpg"

def send_email_with_image(to_emails, subject, body, image_path, bcc_emails=None):
    """Send email with image attachment via Gmail API through Maton Gateway"""
    
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email.mime.image import MIMEImage
    from email.mime.base import MIMEBase
    import base64
    
    msg = MIMEMultipart()
    msg['From'] = 'charleslevison@gmail.com'
    msg['To'] = ', '.join(to_emails[:1])
    msg['Subject'] = subject
    if bcc_emails:
        msg['Bcc'] = ', '.join(bcc_emails)
    
    msg.attach(MIMEText(body, 'plain'))
    
    # Attach image if exists
    if image_path and os.path.exists(image_path):
        with open(image_path, 'rb') as img_file:
            img_data = img_file.read()
            img_name = os.path.basename(image_path)
            
            image = MIMEImage(img_data, name=img_name)
            image.add_header('Content-Disposition', 'attachment', filename=img_name)
            msg.attach(image)
        print(f"✅ Attached image: {img_name}")
    else:
        print(f"⚠️ Image not found at: {image_path}")
    
    raw = base64.urlsafe_b64encode(msg.as_bytes()).decode()
    
    data = json.dumps({'raw': raw}).encode()
    req = urllib.request.Request(
        'https://gateway.maton.ai/google-mail/gmail/v1/users/me/messages/send',
        data=data, method='POST'
    )
    req.add_header('Authorization', f'Bearer {MATON_API_KEY}')
    req.add_header('Content-Type', 'application/json')
    
    try:
        res = urllib.request.urlopen(req)
        result = json.load(res)
        print(f"✅ Email sent to {len(to_emails)} recipients")
        print(f"   Message ID: {result.get('id')}")
        return True
    except Exception as e:
        print(f"❌ Failed: {e}")
        return False

if __name__ == '__main__':
    print("Levison Gallery Newsletter")
    print(f"Recipients: {len(buyers)} art customers")
    
    # Send to all buyers with image attachment
    if buyers:
        send_email_with_image([buyers[0]], SUBJECT, BODY, IMAGE_PATH, bcc_emails=buyers[1:] if len(buyers) > 1 else [])
    else:
        print("No buyers in list!")
