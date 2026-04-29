# Spotify MCP Server

A Model Context Protocol (MCP) server for Spotify, built with `FastMCP` and `spotipy`.

## Features

- **Playback Control**: Play, pause, skip, set volume, list devices.
- **Library Management**: Access saved tracks, playlists, and followed artists.
- **Analytics & Recommendations**: Get audio features, top tracks, and recommendations.
- **Search**: Search for tracks, artists, albums, and playlists.

## Setup

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Spotify Developer Setup**:
   - Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard).
   - Create an App (choose **Web API**).
   - In App Settings, add the following **Redirect URI**:
     `http://127.0.0.1:8080`
   - Copy your **Client ID** and **Client Secret**.
3. **Configure Environment**:
   - Edit the `.env` file with your keys:
     ```env
     SPOTIPY_CLIENT_ID=your_client_id_here
     SPOTIPY_CLIENT_SECRET=your_client_secret_here
     SPOTIPY_REDIRECT_URI=http://127.0.0.1:8080
     ```

## Usage

Run the server using FastMCP:

```bash
fastmcp run server.py
```

*Note: On the first run, a browser window will open asking you to log in to Spotify and authorize the app. A `.spotify_cache` file will be created to store your token.*
