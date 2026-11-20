#!/usr/bin/env bash
# VS Code in the browser + public HTTPS URL (Cloudflare quick tunnel). Works on Colab / Ubuntu VPS.
set -e
curl -fsSL https://code-server.dev/install.sh | sh
curl -fsSL -o /tmp/cloudflared https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64
chmod +x /tmp/cloudflared
PASSWORD="${CS_PASSWORD:-$(head -c12 /dev/urandom | base64 | tr -d "=+/")}"
echo "Password: $PASSWORD"
PASSWORD="$PASSWORD" nohup code-server --bind-addr 127.0.0.1:8080 --auth password "${1:-.}" >/tmp/cs.log 2>&1 &
sleep 5
nohup /tmp/cloudflared tunnel --url http://127.0.0.1:8080 >/tmp/cf.log 2>&1 &
sleep 8
grep -o "https://[a-z0-9-]*\.trycloudflare\.com" /tmp/cf.log | head -1
