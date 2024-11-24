# SpotifyTouchBar

A minimal macOS menu bar application that displays your currently playing Spotify track.

## Features

- Shows current playing track and artist in menu bar
- Automatic track updates
- Minimal memory footprint
- Runs in background
- Secure Spotify API integration

## Requirements

- macOS
- Python 3.11+
- Spotify Premium account

## Installation

### From Source

1. Clone the repository:
```bash
git clone https://github.com/yourusername/SpotifyTouchBar.git
cd SpotifyTouchBar
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file with your Spotify API credentials:
```
SPOTIFY_CLIENT_ID=your_client_id
SPOTIFY_CLIENT_SECRET=your_client_secret
```

4. Run the application:
```bash
python spotify_touchbar.py
```

### From Release

1. Download the latest release
2. Move SpotifyTouchBar.app to your Applications folder
3. Launch the application

## Building

To build the application:

```bash
python setup.py py2app
```

The built application will be in the `dist` folder.

## Technologies Used

- [Python](https://python.org)
- [rumps](https://github.com/jaredks/rumps) - Ridiculously Uncomplicated macOS Python Statusbar apps
- [spotipy](https://spotipy.readthedocs.io/) - Python client for the Spotify Web API
- [py2app](https://py2app.readthedocs.io/) - Python to macOS application bundler

## License

MIT License

## Author

Your Name
