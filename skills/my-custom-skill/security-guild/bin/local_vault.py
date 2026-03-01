#!/usr/bin/env python3
"""
Local Encrypted Vault for OpenClaw
Simple secret management without external services
"""

import os
import json
import base64
import hashlib
import getpass
from cryptography.fernet import Fernet
from pathlib import Path

# Configuration
VAULT_DIR = Path.home() / ".openclaw" / "vault"
VAULT_FILE = VAULT_DIR / "secrets.enc"
CONFIG_FILE = VAULT_DIR / "config.json"

class LocalVault:
    def __init__(self, master_password=None):
        VAULT_DIR.mkdir(parents=True, exist_ok=True)
        
        if master_password:
            self.key = self.derive_key(master_password)
            self.cipher = Fernet(self.key)
        else:
            self.key = None
            self.cipher = None
            self.load_config()
    
    def derive_key(self, password):
        """Derive encryption key from password"""
        key = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode(),
            b'openvault_salt_2024',
            100000
        )
        return base64.urlsafe_b64encode(key)
    
    def load_config(self):
        """Load vault configuration"""
        if CONFIG_FILE.exists():
            with open(CONFIG_FILE) as f:
                config = json.load(f)
                if config.get("key_hash"):
                    self.key_hash = config["key_hash"]
                else:
                    self.key_hash = None
    
    def save_config(self):
        """Save vault configuration"""
        config = {
            "key_hash": self.derive_key(getpass.getpass("Enter master password: ")).decode() if not self.key else self.key.decode()
        }
        with open(CONFIG_FILE, 'w') as f:
            json.dump(config, f)
    
    def unlock(self, master_password):
        """Unlock vault with master password"""
        self.key = self.derive_key(master_password)
        self.cipher = Fernet(self.key)
        return True
    
    def lock(self):
        """Lock vault"""
        self.key = None
        self.cipher = None
    
    def set(self, key, value):
        """Store a secret"""
        if not self.cipher:
            raise Exception("Vault is locked")
        
        secrets = self.load_all()
        secrets[key] = value
        self.save_all(secrets)
    
    def get(self, key, default=None):
        """Retrieve a secret"""
        if not self.cipher:
            raise Exception("Vault is locked")
        
        secrets = self.load_all()
        return secrets.get(key, default)
    
    def delete(self, key):
        """Delete a secret"""
        secrets = self.load_all()
        if key in secrets:
            del secrets[key]
            self.save_all(secrets)
            return True
        return False
    
    def load_all(self):
        """Load all secrets"""
        if not VAULT_FILE.exists():
            return {}
        
        try:
            with open(VAULT_FILE, 'rb') as f:
                encrypted = f.read()
            if encrypted:
                decrypted = self.cipher.decrypt(encrypted)
                return json.loads(decrypted)
        except:
            pass
        return {}
    
    def save_all(self, secrets):
        """Save all secrets"""
        if not self.cipher:
            raise Exception("Vault is locked")
        
        encrypted = self.cipher.encrypt(json.dumps(secrets).encode())
        with open(VAULT_FILE, 'wb') as f:
            f.write(encrypted)
    
    def list_keys(self):
        """List all secret keys"""
        secrets = self.load_all()
        return list(secrets.keys())

# CLI Interface
def main():
    import sys
    
    vault = LocalVault()
    
    if len(sys.argv) < 2:
        print("""
🔐 Local Vault CLI
=================
Usage:
  vault.py unlock          - Unlock vault
  vault.py lock            - Lock vault  
  vault.py set <key> <val> - Store secret
  vault.py get <key>       - Retrieve secret
  vault.py delete <key>    - Delete secret
  vault.py list            - List all secrets
  vault.py init            - Initialize new vault
        """)
        return
    
    command = sys.argv[1]
    
    try:
        if command == "init":
            password = getpass.getpass("Create master password: ")
            confirm = getpass.getpass("Confirm password: ")
            if password != confirm:
                print("❌ Passwords don't match")
                return
            vault = LocalVault(password)
            vault.set("_init", "true")
            print("✅ Vault initialized")
        
        elif command == "unlock":
            password = getpass.getpass("Master password: ")
            vault.unlock(password)
            print("✅ Vault unlocked")
        
        elif command == "lock":
            vault.lock()
            print("🔒 Vault locked")
        
        elif command == "set":
            if len(sys.argv) < 4:
                print("Usage: vault.py set <key> <value>")
                return
            key, value = sys.argv[2], sys.argv[3]
            vault.set(key, value)
            print(f"✅ Stored: {key}")
        
        elif command == "get":
            if len(sys.argv) < 3:
                print("Usage: vault.py get <key>")
                return
            key = sys.argv[2]
            value = vault.get(key)
            if value:
                print(f"{key}: {value}")
            else:
                print(f"❌ Key not found: {key}")
        
        elif command == "delete":
            if len(sys.argv) < 3:
                print("Usage: vault.py delete <key>")
                return
            key = sys.argv[2]
            if vault.delete(key):
                print(f"✅ Deleted: {key}")
            else:
                print(f"❌ Key not found: {key}")
        
        elif command == "list":
            keys = vault.list_keys()
            if keys:
                print("🔑 Stored secrets:")
                for k in keys:
                    print(f"  - {k}")
            else:
                print("No secrets stored")
        
        else:
            print(f"Unknown command: {command}")
    
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
