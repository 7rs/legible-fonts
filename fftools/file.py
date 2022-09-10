from typing import NoReturn
import os.path

import fontforge


class InvalidPathError(Exception):
    pass


def _check_path(path: str) -> NoReturn:
    """Checks a path."""
    if not os.path.exists(path):
        raise InvalidPathError(f"A file does not exist: {path}")


def _close_font(font: fontforge.font) -> NoReturn:
    """Closes a font."""
    font.selection.none()
    font.close()


def exists_path(path: str) -> bool:
    return os.path.exists(path)


def open_font(path: str) -> fontforge.font:
    """Opens a font."""
    _check_path(path)
    return fontforge.open(path)


def merge_font(font: fontforge.font, path: str) -> NoReturn:
    """Merges a font."""
    _check_path(path)
    font.mergeFonts(path)


def save_font(font: fontforge.font, path: str) -> NoReturn:
    """Saves a font and closes one."""
    font.save(path)
    _close_font(font)


def generate_font(font: fontforge.font, path) -> NoReturn:
    font.generate(path)
    _close_font(font)
