# Handoff: Windows to macOS

This project is a Model Context Protocol (MCP) server for Spotify built using `FastMCP` and `spotipy`.

## Project State
- All core files created: `server.py`, `spotify/*.py`.
- Tools return structured dictionaries.
- Verified running on Windows.

## macOS Environment Setup

Since you are transitioning from Windows to macOS, follow these steps to set up the environment:

### 1. Initialize Virtual Environment
On macOS, Python is typically invoked as `python3` and venv activation uses `bin/activate`.

```bash
# Create a new venv for Mac
python3 -m venv .venv

# Activate the venv
source .venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
pip install "mcp[cli]"
```

### 3. Environment Configuration
Ensure your `.env` file is present in the root directory:
```env
SPOTIPY_CLIENT_ID=your_client_id_here
SPOTIPY_CLIENT_SECRET=your_client_secret_here
SPOTIPY_REDIRECT_URI=http://127.0.0.1:8080
```
*Note: Do not use `localhost` in the Redirect URI per Spotify's updated security policy.*

### 4. Run Initial Authentication
This will cache your Spotify token in `.spotify_cache`.
```bash
python -c "from spotify.client import get_client; get_client()"
```

### 5. Development & Installation

**Run Inspector:**
```bash
mcp dev server.py
```

**Install to Claude Desktop:**
```bash
mcp install server.py --name "spotify-mcp"
```
