from typing import NoReturn

import fontforge

from fftools.ranges import UnicodeRange, UnicodeRanges
from fftools import ranges


def _select_range(font: fontforge.font, _range: UnicodeRange, unicode: bool = True) -> NoReturn:
    """Selects the glyph within a range."""
    if unicode:
        ranges.correct_range(_range[0], _range[-1])
        font.selection.select(("more", "ranges", "unicode"), _range[0], _range[-1])
    else:
        font.selection.select(("more", "ranges"), _range[0], _range[-1])


def select_ranges(font: fontforge.font, ranges: UnicodeRanges, unicode: bool = True) -> NoReturn:
    """Selects the glyphs within ranges."""
    font.selection.none()
    for _range in ranges:
        _select_range(font, _range, unicode)


def select_invalid_glyphs(font: fontforge.font) -> NoReturn:
    """Selects the invalid glyphs in the Unicode blocks."""
    font.selection.none()
    for glyph in font.glyphs():
        if not ranges.correct_point(glyph):
            font.selection.select(("more", "encoding"), glyph)
