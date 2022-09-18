from typing import NoReturn
import os.path

import fontforge


class InvalidPathError(Exception):
    pass


def exists_path(path: str) -> bool:
    """When a path exists, returns true."""
    return os.path.exists(path)


def check_path(path: str) -> NoReturn:
    """Checks for the existence of a path."""
    if not exists_path(path):
        raise InvalidPathError(f"A file doesn't exist: {path}")


def open_font(path: str) -> fontforge.font:
    """Opens the font object from a path in fontforge."""
    check_path(path)
    return fontforge.open(path, ("alltables",))


def merge_font(font: fontforge.font, path: str) -> NoReturn:
    """
    Opens the font object in fontforge from a path
    and merges it into the font object.
    """
    check_path(path)
    font.mergeFonts(path)


def close_font(font: fontforge.font) -> NoReturn:
    """Closes the font object in fontforge."""
    font.selection.none()
    font.close()


def save_font(font: fontforge.font, path: str) -> NoReturn:
    """
    Saves the font object as the SFD file
    and closes it in fontforge.
    """
    font.save(path)
    close_font(font)


def generate_font(font: fontforge.font, path) -> NoReturn:
    """
    Generates the TTF file from the font object
    and closes it in fontforge.
    """
    font.generate(path)
    close_font(font)
