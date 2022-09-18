from dataclasses import dataclass

from configurator.fonts.option import FontOption, Underline
from configurator.fonts.size import Size
from configurator.fonts.name import Name
from configurator.fonts.os2 import OS2MetricsTable, FsType, Weight, Width
from configurator.fonts import os2

from generator.fonts import config


@dataclass
class SFDOption(FontOption):
    size: Size = config.SIZE_OPTION
    underline: Underline = config.UNDERLINE_OPTION
    italic_angle: float = config.ITALIC_ANGLE_OPTION
    encoding: str = config.ENCODING_OPTION


@dataclass
class LegibleFonts(FontOption):
    name: Name = Name(
        family="Legible", fond="Regular", font="Legible-Fonts", font_full="Legible-Fonts", copyright=config.COPYRIGHTS
    )
    size: Size = config.SIZE_OPTION
    underline: Underline = config.UNDERLINE_OPTION
    italic_angle: float = config.ITALIC_ANGLE_OPTION
    encoding: str = config.ENCODING_OPTION
    os2_metrics: OS2MetricsTable = OS2MetricsTable(
        vendor="7rs",
        fstype=os2.create_fstype(FsType.INSTALLABLE_EMBEDDING),
        weight=Weight.NORMAL,
        width=Width.NORMAL,
    )
