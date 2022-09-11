from typing import NoReturn, Optional, List
from dataclasses import dataclass

import fontforge


@dataclass
class Copyright:
    """Copyright (Font/Tool name, Author, Year, Contact)"""

    font_name: str
    author: str
    year: str
    contact: Optional[str] = None


@dataclass
class Name:
    """Name (Family name, Font name, Full font name, Fond name) with copyright"""

    family: str
    fond: str
    font: str
    font_full: str
    copyright: str


@dataclass
class Size:
    """Size (Ascent, Descent, Linegap)"""

    ascent: int
    descent: int
    ascent_add: int = 0
    descent_add: int = 0
    linegap: int = 0


@dataclass
class Underline:
    """Underline options (Position, Height)"""

    position: int
    height: int


class FontOption:
    """The options for font."""

    name: Optional[Name] = None
    size: Optional[Size] = None
    underline: Optional[Underline] = None
    italic_angle: Optional[float] = None
    encoding: Optional[str] = None


def _get_copyright(c: Copyright) -> str:
    """Returns the copyright text from the received copyright object."""
    if c.contact:
        return f"[{c.font_name}]\n" + f"Copyright {c.year}, {c.author} ({c.contact})"
    return f"[{c.font_name}]\n" + f"Copyright {c.year}, {c.author}"


def _set_name(font: fontforge.font, name: Name) -> NoReturn:
    """
    Sets the option about name from the received name object,
    along with the copyright.
    """
    font.familyname = name.family
    font.fondname = name.fond
    font.fontname = name.font
    font.fullname = name.font_full
    font.copyright = name.copyright


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


def _set_size(font: fontforge.font, size: Size) -> NoReturn:
    """Sets the option about the size. (Ascent, Descent, Linegap)"""
    _set_ascent(font, size.ascent, size.ascent_add)
    _set_descent(font, size.descent, size.descent_add)
    _set_linegap(font, size.linegap)
    font.em = size.ascent + size.descent


def _set_underline(font: fontforge.font, underline: Underline) -> NoReturn:
    """Sets the option about the underline."""
    font.upos = underline.position
    font.uwidth = underline.height


def get_copyrights(cs: List[Copyright]) -> str:
    """Returns the copyright text from many copyrights object."""
    return "\n\n".join([_get_copyright(c) for c in cs])


def set_option(font: fontforge.font, option: FontOption) -> NoReturn:
    """Sets the options for font.
    - Name (Family name, Font name, Full font name, Fond name) with copyright
    - Size (Ascent, Descent, Linegap)
    - Underline options (Position, Height)
    - Italic angle
    - Encoding
    """
    if option.name:
        _set_name(font, option.name)
    if option.size:
        _set_size(font, option.size)
    if option.underline:
        _set_underline(font, option.underline)
    if option.italic_angle:
        font.italicangle = option.italic_angle
    if option.encoding:
        font.encoding = option.encoding
