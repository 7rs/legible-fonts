from typing import NoReturn
import os.path

import fontforge


class InvalidPathError(Exception):
    pass


def _check_path(path: str) -> NoReturn:
    """Checks for the existence of the received path."""
    if not os.path.exists(path):
        raise InvalidPathError(f"A file doesn't exist: {path}")


def _close_font(font: fontforge.font) -> NoReturn:
    """Closes the received font object in fontforge."""
    font.selection.none()
    font.close()


def exists_path(path: str) -> bool:
    """When the received path exists, returns true."""
    return os.path.exists(path)


def open_font(path: str) -> fontforge.font:
    """Opens the font object from the received path in fontforge."""
    _check_path(path)
    return fontforge.open(path)


def merge_font(font: fontforge.font, path: str) -> NoReturn:
    """
    Opens the font object in fontforge from the received path
    and merges it into the received font object.
    """
    _check_path(path)
    font.mergeFonts(path)


def save_font(font: fontforge.font, path: str) -> NoReturn:
    """
    Saves the font object as the SFD file
    and closes it in fontforge.
    """
    font.save(path)
    _close_font(font)


def generate_font(font: fontforge.font, path) -> NoReturn:
    """
    Generates the TTF file from the received font object
    and closes it in fontforge.
    """
    font.generate(path)
    _close_font(font)
