# Spotify Menu Bar

A simple macOS menu bar application that displays the currently playing Spotify track.

## Features

- Shows current song and artist name in the menu bar
- Updates automatically every second
- Runs in the background
- Minimal and lightweight

## Requirements

- macOS
- Python 3.11+
- Spotify account
- Spotify Developer API credentials

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/spotify-menu-bar
cd spotify-menu-bar
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Register your application at [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
   - Create a new application
   - Set the redirect URI to: `http://localhost:8888/callback`
   - Note down your Client ID and Client Secret

4. Create a `.env` file in the project root and add your Spotify API credentials:
```
SPOTIFY_CLIENT_ID=your_client_id_here
SPOTIFY_CLIENT_SECRET=your_client_secret_here
```

5. Build the application:
```bash
python3 setup.py py2app
```

6. The application will be created in the `dist` folder as `SpotifyMenuBar.app`

## Usage

1. Double click `SpotifyMenuBar.app` to run
2. On first run, authenticate with your Spotify account
3. The current playing track will appear in your menu bar

To make the app start automatically when you log in:
1. Go to System Settings > Users & Groups
2. Click on your user
3. Click Login Items
4. Click + and add SpotifyMenuBar.app

## Development

This app was built using:
- `rumps`: For creating the menu bar app
- `spotipy`: For Spotify API integration
- `py2app`: For packaging the Python script as a macOS app

## License

MIT License

## Credits

Created with [Windsurf](https://twitter.com/windsurfai)
By [@niyoseris](https://twitter.com/niyoseris)
