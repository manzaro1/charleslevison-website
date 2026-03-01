#!/bin/bash
# 1Password CLI Installation for Security Guild

echo "=== 1Password CLI Installation ==="

# Detect OS
OS="$(uname -s)"
ARCH="$(uname -m)"

case "$OS" in
    Linux*)
        case "$ARCH" in
            x86_64)
                curl -s -o /tmp/op https://cache.agilebits.com/dist/1P/op2/pkg/v2.1.0-beta.1/op_linux_amd64_v2.1.0-beta.1.zip
                ;;
            aarch64|arm64)
                curl -s -o /tmp/op https://cache.agilebits.com/dist/1P/op2/pkg/v2.1.0-beta.1/op_linux_arm64_v2.1.0-beta.1.zip
                ;;
            *)
                echo "Unsupported architecture: $ARCH"
                exit 1
                ;;
        esac
        unzip -o /tmp/op -d /tmp
        sudo mv /tmp/op /usr/local/bin/op
        sudo chmod +x /usr/local/bin/op
        ;;
    Darwin*)
        brew install 1password-cli
        ;;
    MINGW*|CYGWIN*|MSYS*)
        curl -s -o /tmp/op.exe https://cache.agilebits.com/dist/1P/op2/pkg/v2.1.0-beta.1/op_windows_amd64_v2.1.0-beta.1.zip
        unzip -o /tmp/op.exe -d /tmp
        mv /tmp/op.exe /usr/local/bin/op.exe
        ;;
esac

# Verify installation
if command -v op &> /dev/null; then
    echo "✅ 1Password CLI installed successfully"
    echo ""
    echo "=== Next Steps ==="
    echo "1. Sign in: op signin"
    echo "2. Create service account: https://developer.1password.com/docs/service-accounts"
    echo "3. Set OP_TOKEN: export OP_TOKEN='your_token_here'"
    echo "4. Test: op vault list"
else
    echo "❌ Installation failed"
fi
