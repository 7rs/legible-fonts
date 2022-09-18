from typing import Optional, Tuple
from enum import Enum
from dataclasses import dataclass

from configurator.glyphs.ranges import UnicodeRange, UnicodeRanges
from configurator.glyphs.trans import TransformOption
from configurator.glyphs.name import NewName

MovingPlan = Tuple[Tuple[UnicodeRange], Tuple[UnicodeRange]]


class InvalidFontError(Exception):
    pass


class Fonts(Enum):
    """Font Family ID."""

    FONTS_DIR = 0
    IOSEVKA = 1
    IOSEVKA_EXTENDED = 2
    BIZ_UDGOTHIC = 3
    NERD_FONTS = 4
    NOTO_EMOJI = 5
    FIRACODE = 6


@dataclass
class GlyphsOption:
    """Glyphs option to change glyphs."""

    ranges: UnicodeRanges
    transform: Optional[TransformOption] = None
    moving_plan: Optional[MovingPlan] = None
    new_names: Optional[NewName] = None
