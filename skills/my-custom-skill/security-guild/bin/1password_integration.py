#!/usr/bin/env python3
"""
1Password Vault Integration for OpenClaw
Manages secrets securely using 1Password
"""

import os
import json
import subprocess
import urllib.request
import urllib.parse

# Configuration
OP_TOKEN = os.environ.get("OP_TOKEN", "")
VAULT_NAME = os.environ.get("OP_VAULT", "OpenClaw")

def run_op(args):
    """Run 1Password CLI command"""
    if not OP_TOKEN:
        return {"error": "OP_TOKEN not set"}
    
    cmd = ["op"] + args
    env = os.environ.copy()
    env["OP_TOKEN"] = OP_TOKEN
    
    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, env=env, timeout=30
        )
        if result.returncode == 0:
            return {"success": True, "output": result.stdout}
        else:
            return {"success": False, "error": result.stderr}
    except Exception as e:
        return {"success": False, "error": str(e)}

def list_vaults():
    """List all vaults"""
    return run_op(["vault", "list", "--format=json"])

def list_items(vault=None):
    """List items in vault"""
    args = ["item", "list", "--format=json"]
    if vault:
        args.extend(["--vault", vault])
    return run_op(args)

def get_item(item_id, vault=None):
    """Get item details"""
    args = ["item", "get", item_id, "--format=json"]
    if vault:
        args.extend(["--vault", vault])
    return run_op(args)

def get_password(item_id, vault=None):
    """Get password for item"""
    args = ["item", "get", item_id, "--fields=password", "--format=json"]
    if vault:
        args.extend(["--vault", vault])
    return run_op(args)

def create_item(vault, title, username, password, url="", notes=""):
    """Create new item"""
    return run_op([
        "item", "create",
        "--vault", vault,
        "--title", title,
        "--username", username,
        "--password", password,
        "--url", url,
        "--notes", notes,
        "--format=json"
    ])

def delete_item(item_id, vault=None):
    """Delete item"""
    args = ["item", "delete", item_id]
    if vault:
        args.extend(["--vault", vault])
    return run_op(args)

# Web server for fetching secrets
def start_server():
    """Start HTTP server to fetch secrets"""
    from http.server import HTTPServer, BaseHTTPRequestHandler
    import socketserver
    
    class SecretHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            # Parse path
            path = urllib.parse.urlparse(self.path).path
            parts = path.strip("/").split("/")
            
            if len(parts) >= 2 and parts[0] == "secret":
                item_name = urllib.parse.unquote(parts[1])
                # Find item
                items_result = list_items(VAULT_NAME)
                if items_result.get("success"):
                    items = json.loads(items_result.get("output", "[]"))
                    for item in items:
                        if item.get("title") == item_name:
                            # Get password
                            pw_result = get_password(item.get("id"), VAULT_NAME)
                            if pw_result.get("success"):
                                self.send_response(200)
                                self.send_header("Content-Type", "text/plain")
                                self.end_headers()
                                self.wfile.write(pw_result["output"].encode())
                                return
                
                self.send_response(404)
                self.send_header("Content-Type", "text/plain")
                self.end_headers()
                self.wfile.write(b"Not found")
            else:
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({
                    "endpoints": {
                        "/secret/{item_name}": "Get password for item",
                        "/vaults": "List vaults",
                        "/items": "List items"
                    }
                }).encode())
        
        def log_message(self, format, *args):
            pass  # Suppress logging
    
    print("🚀 1Password Secret Server starting...")
    print(f"Vault: {VAULT_NAME}")
    print("Endpoints:")
    print("  GET /secret/{item_name} - Get password")
    print("  GET /vaults - List vaults")
    print("  GET /items - List items")
    
    server = HTTPServer(("127.0.0.1", 3456), SecretHandler)
    print("Server running on http://127.0.0.1:3456")
    server.serve_forever()

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "server":
            start_server()
        elif sys.argv[1] == "list":
            print(list_items(VAULT_NAME))
        elif sys.argv[1] == "vaults":
            print(list_vaults())
        else:
            print("Usage: python3 1password_integration.py [server|list|vaults]")
    else:
        print("1Password Integration Ready")
        print("Set OP_TOKEN environment variable to use")
        print("Usage: python3 1password_integration.py [server|list|vaults]")
