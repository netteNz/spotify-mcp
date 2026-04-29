# Spotify MCP Server Setup — Session Handoff

**Date:** April 29, 2026  
**Session Status:** ✅ Complete & Tested  
**Last Action:** Verified Spotify MCP server connection and tested with listening history query

---

##  What Was Accomplished

- ✅ Created a **local stdio MCP server** in Python for Spotify integration
- ✅ Configured Claude Desktop to connect to the Spotify MCP server
- ✅ Tested connection: Successfully listed top 20 tracks from this month
- ✅ Server tools available: `play`, `search_and_play`, `pause`, `get_currently_playing`, etc.

---

##  Key Files & Locations

### Repository
- **Path:** `D:\code\mcp-servers\spotify-mcp` (or `/d/code/mcp-servers/spotify-mcp` in Git Bash)
- **Status:** Virtual environment active at `.venv/Scripts/python.exe`

### Configuration File
- **Location:** `%APPDATA%\Claude\claude_desktop_config.json`
- **Current Config (Windows):**
```json
{
  "preferences": {
    "menuBarEnabled": false,
    "coworkScheduledTasksEnabled": false,
    "ccdScheduledTasksEnabled": true,
    "sidebarMode": "epitaxy",
    "coworkWebSearchEnabled": true
  },
  "mcpServers": {
    "spotify-mcp": {
      "command": "D:\\code\\mcp-servers\\spotify-mcp\\.venv\\Scripts\\python.exe",
      "args": ["D:\\code\\mcp-servers\\spotify-mcp\\server.py"]
    }
  }
}
```

### Core Server Files
- `server.py` — Main MCP server entry point
- `requirements.txt` — Python dependencies (spotipy, mcp SDK, etc.)
- `.venv/` — Python virtual environment

---

## 🔧 How to Resume Next Session

### Step 1: Verify Environment
```bash
cd /d/code/mcp-servers/spotify-mcp
# Check venv is active and server.py exists
ls .venv/Scripts/python.exe
ls server.py
```

### Step 2: Relaunch Claude Desktop
- **Full quit** (right-click taskbar icon → Quit, or `Ctrl+Q`)
- **Relaunch** Claude Desktop
- Look for **hammer icon (🔨)** in chat input area

### Step 3: Test Connection
In a new chat, ask Claude to:
```
List my top 5 most played tracks this month
```
Or try playing a song:
```
Play "your song name" on Spotify
```

### Step 4: Check Logs (if needed)
In Claude Desktop → **Settings → Developer** — should show green indicator with no errors

---

## 🎵 Available Spotify Tools

Once connected, these commands are available to Claude:

| Tool | Purpose | Example |
|------|---------|---------|
| `play` | Play a track by URI | Play a specific track |
| `search_and_play` | Search Spotify & play top result | "Play Blinding Lights" |
| `pause` | Pause playback | Stop music |
| `skip_next` | Skip to next track | Go to next song |
| `skip_previous` | Go to previous track | Go back one track |
| `set_volume` | Set volume (0-100) | Set volume to 50 |
| `get_currently_playing` | Show what's playing | What song is playing now? |
| `get_top_tracks` | Get top tracks (time range) | List my top 20 songs |
| `get_playlists` | List your playlists | Show my playlists |
| `search_spotify` | General search | Search Spotify |
| `get_recommendations` | Get recommendations | Suggest songs like... |
| `save_track` | Save track to library | Add to liked songs |

---

##  Next Steps & Ideas

### Immediate (Low Effort)
- [ ] Try different Spotify queries (genre-specific recommendations, playlist exploration)
- [ ] Test the `play` command with different tracks
- [ ] Experiment with `set_volume` and playback controls

### Medium (Integration)
- [ ] Add **OS MCP server** (Windows file system, process control)
- [ ] Add **WhatsApp MCP server** (if available/buildable)
- [ ] Create a **multi-server config** with 3+ services running simultaneously

### Advanced (Custom Features)
- [ ] Build a custom tool that uses multiple Spotify APIs (e.g., "analyze my music taste")
- [ ] Create a playlist generator that takes natural language description
- [ ] Build automation (e.g., "create a weekly top songs playlist")

---

## 🛑 Shutdown / Cleanup

### To Stop the Server
- **Easiest:** Just close Claude Desktop (server closes automatically)
- **Manual:** Kill the Python process running `server.py`

### To Disable (Keep Config)
- Edit `claude_desktop_config.json` and comment out or remove the `spotify-mcp` entry
- Relaunch Claude Desktop

### To Re-enable
- Restore the `spotify-mcp` entry in the config
- Relaunch Claude Desktop
- (No reinstall needed — venv and files remain)

---

## ✅ Testing Checklist for Next Session

- [ ] Claude Desktop fully restarted
- [ ] Hammer icon visible in chat input
- [ ] No errors in Settings → Developer
- [ ] Test: Ask Claude for top 5 tracks
- [ ] Test: Try playing a song
- [ ] Verify: MCP server connection shows as active

---

## Troubleshooting Quick Reference

| Issue | Check |
|-------|-------|
| Hammer icon missing | Restart Claude Desktop (full quit) |
| "Server not found" error | Verify venv path in config matches actual location |
| Python not found | Check `.venv\Scripts\python.exe` exists |
| Permission denied | Re-verify Spotify API credentials in `.env` or config |
| Tools not showing | Look at Settings → Developer for error messages |

---

**Last Verified:** April 29, 2026 at 07:56 UTC  
**Setup Quality:** ✅ Production-Ready (locally)
