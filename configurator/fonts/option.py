from typing import NoReturn, Optional
from dataclasses import dataclass

import fontforge

from configurator.fonts.name import Name
from configurator.fonts.size import Size
from configurator.fonts.os2 import OS2MetricsTable
from configurator.fonts import name, size, os2


@dataclass
class Underline:
    """Underline options (Position, Height)"""

    position: int
    height: int


def _set_underline(font: fontforge.font, underline: Underline) -> NoReturn:
    """Sets the option about the underline."""
    font.upos = underline.position
    font.uwidth = underline.height


class FontOption:
    """The options for font."""

    name: Optional[Name] = None
    size: Optional[Size] = None
    underline: Optional[Underline] = None
    italic_angle: Optional[float] = None
    encoding: Optional[str] = None
    os2_metrics: Optional[OS2MetricsTable] = None


def set_option(font: fontforge.font, option: FontOption) -> NoReturn:
    """Sets the options for font.
    - Name (Family name, Font name, Full font name, Fond name) with copyright
    - Size (Ascent, Descent, Linegap)
    - Underline options (Position, Height)
    - Italic angle
    - Encoding
    """
    if option.name:
        name.set_name(font, option.name)
    if option.size:
        size.set_size(font, option.size)
    if option.underline:
        _set_underline(font, option.underline)
    if option.italic_angle:
        font.italicangle = option.italic_angle
    if option.encoding:
        font.encoding = option.encoding
    if option.os2_metrics:
        os2.set_os2_metrics_table(font, option.os2_metrics)
