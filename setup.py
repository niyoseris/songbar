from setuptools import setup

APP = ['songbar.py']
DATA_FILES = [('.env', ['.env'])]
OPTIONS = {
    'argv_emulation': False,
    'iconfile': None,
    'plist': {
        'LSUIElement': True,
        'CFBundleName': 'SongBar',
        'CFBundleDisplayName': 'SongBar',
        'CFBundleIdentifier': 'com.songbar.app',
        'CFBundleVersion': "1.0.0",
        'CFBundleShortVersionString': "1.0.0",
    },
    'packages': ['rumps', 'spotipy', 'dotenv'],
    'includes': ['dotenv'],
    'excludes': ['matplotlib', 'numpy', 'pandas', 'scipy', 'sympy', 'IPython']
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
