# VM Setup — Network MCP Server

## 1. Configure git identity (one-time)

```bash
git config --global user.name "TheFireSays"
git config --global user.email "TheFireSays@users.noreply.github.com"
```

## 2. Get the code

```bash
git clone https://github.com/TheFireSays/network_mcp.git
cd network_mcp
```

## 3. Create a virtual environment and install dependencies

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 4. Create the `.env` file

```bash
cat > .env << 'EOF'
NETWORK_USERNAME=admin
NETWORK_PASSWORD=admin
EOF
```

## 5. Configure Claude Desktop

Config file location:
- **Linux:** `~/.config/Claude/claude_desktop_config.json`
- **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "network-automation": {
      "command": "/absolute/path/to/network_mcp/.venv/bin/python",
      "args": ["-m", "network_mcp.server"],
      "cwd": "/absolute/path/to/network_mcp"
    }
  }
}
```

## 6. Restart Claude Desktop

Fully restart Claude Desktop (not just reload). A hammer icon in the chat interface confirms the MCP tools are active.
