# Gumroad Integration Skill

Manage your Gumroad store, products, and orders using the Gumroad API and automation.

## Overview

This skill provides integration with Gumroad for:
- Product management (create, update, delete)
- Order tracking
- Subscriber management
- Link generation

## Requirements

- Gumroad account credentials
- Optional: Gumroad API key (for advanced features)

## Setup

### Option 1: API Key (Advanced)
1. Go to https://gumroad.com/settings/advanced
2. Generate API key
3. Configure in skill settings

### Option 2: Browser Automation (Recommended)
The skill uses browser automation to:
- Login to Gumroad
- Create products
- Upload images
- Manage orders

## Commands

### List Products
```bash
gumroad list-products
```

### Create Product
```bash
gumroad create-product --name "Painting Title" --price 200 --type physical
```

### Upload Image
```bash
gumroad upload-image --path /path/to/image.jpg
```

### Check Orders
```bash
gumroad orders
```

## Product Types

| Type | Description |
|------|-------------|
| physical | Original paintings, prints to ship |
| digital | Downloads, prints |
| membership | Subscriptions |

## Supported Actions

### Products
- Create new product
- Update existing product
- Delete product
- Add/remove variants
- Upload cover image

### Orders
- List recent orders
- Get order details
- Track fulfillment

### Links
- Generate share links
- Create discount codes
- Set subscription terms

## Configuration

Create `~/.openclaw/gumroad.yaml`:
```yaml
email: your@email.com
# API key (optional)
api_key: your_api_key
```

## Examples

### Create Original Painting Listing
```bash
gumroad create-product \
  --name "Lake Malawi Landscape" \
  --price 200 \
  --type physical \
  --description "Original oil painting" \
  --tags "malawi,art,painting"
```

### Create Digital Print
```bash
gumroad create-product \
  --name "Jacaranda Market Print" \
  --price 35 \
  --type digital \
  --description "High-resolution digital print"
```

## Troubleshooting

### Login Issues
- Ensure credentials are correct
- Check 2FA if enabled
- Try browser automation option

### Product Not Appearing
- Ensure product is published
- Check price and currency
- Verify images uploaded

## Notes

- Gumroad takes a 10% commission on sales
- Payments processed in USD
- Physical items require shipping setup
