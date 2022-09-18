from typing import NoReturn
from dataclasses import dataclass

import fontforge


@dataclass
class Size:
    """Size (Ascent, Descent, Linegap)"""

    ascent: int
    descent: int
    ascent_add: int = 0
    descent_add: int = 0
    linegap: int = 0


def _set_ascent(font: fontforge.font, ascent: int, add: int) -> NoReturn:
    """Sets the option about a ascent."""
    font.ascent = ascent
    font.os2_winascent = ascent
    font.hhea_ascent = ascent
    font.os2_typoascent = ascent

    font.os2_winascent_add = add
    font.hhea_ascent_add = add
    font.os2_typoascent_add = add


def _set_descent(font: fontforge.font, descent: int, add: int) -> NoReturn:
    """Sets the option about a descent."""
    font.descent = descent
    font.os2_windescent = descent
    font.hhea_descent = -descent
    font.os2_typodescent = -descent

    font.os2_windescent_add = add
    font.hhea_descent_add = add
    font.os2_typodescent_add = add


def _set_linegap(font: fontforge.font, linegap: int) -> NoReturn:
    """Sets the option about a linegap."""
    font.vhea_linegap = linegap
    font.hhea_linegap = linegap
    font.os2_typolinegap = linegap


def set_size(font: fontforge.font, size: Size) -> NoReturn:
    """Sets the option about the size. (Ascent, Descent, Linegap)"""
    _set_ascent(font, size.ascent, size.ascent_add)
    _set_descent(font, size.descent, size.descent_add)
    _set_linegap(font, size.linegap)
    font.em = size.ascent + size.descent
