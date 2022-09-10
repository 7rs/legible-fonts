from typing import Optional, List
from enum import Enum
from dataclasses import dataclass

from fftools.ranges import UnicodeRange, UnicodeRanges
from fftools.glyph import TransformOption

MovingPlans = List[UnicodeRange]


class InvalidFontError(Exception):
    pass


class Fonts(Enum):
    """The fonts."""

    FONTS_DIR = 0
    IOSEVKA = 1
    IOSEVKA_EXTENDED = 2
    BIZ_UDGOTHIC = 3
    NERD_FONTS = 4
    NOTO_EMOJI = 5
    FIRACODE = 6


@dataclass
class GlyphsOption:
    """Glyphs option."""

    ranges: UnicodeRanges
    transform: Optional[TransformOption] = None
    moving_plans: Optional[MovingPlans] = None
