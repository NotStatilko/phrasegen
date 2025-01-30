from pathlib import Path
try:
    from sys import _MEIPASS
except ImportError:
    _MEIPASS = None


ABSPATH: Path = Path(_MEIPASS) if _MEIPASS is not None \
    else Path(__file__).parent
WORDLISTPATH = ABSPATH / 'wordlist'

# By default, PyInstaller will not grab files
# from 'wordlist' folder. To resolve this error
# you will need to manually add it to .spec file.
PYINSTALLER_DATA: dict = {
    str(Path('wordlist', i.name)): str(i)
    for i in WORDLISTPATH.glob('*')
}
