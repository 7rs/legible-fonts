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


def get_copyright(copyright: Copyright) -> str:
    """Returns copyright text from the copyright object."""
    if copyright.contact:
        return f"[{copyright.font_name}]\n" + f"Copyright {copyright.year}, {copyright.author} ({copyright.contact})"
    return f"[{copyright.font_name}]\n" + f"Copyright {copyright.year}, {copyright.author}"


def get_copyrights(copyrights: List[Copyright]) -> str:
    """Returns copyright text from many copyright objects."""
    return "\n\n".join([get_copyright(copyright) for copyright in copyrights])


@dataclass
class Name:
    """Name (Family name, Font name, Full font name, Fond name) with copyright"""

    family: str
    fond: str
    font: str
    font_full: str
    copyright: str


def set_name(font: fontforge.font, name: Name) -> NoReturn:
    """
    Sets options about name from the name object,
    along with copyright.
    """
    font.familyname = name.family
    font.fondname = name.fond
    font.fontname = name.font
    font.fullname = name.font_full
    font.copyright = name.copyright
