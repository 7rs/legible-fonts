from typing import NoReturn, Optional, List

import fontforge

from fftools.select import UnicodeRange, UnicodeRanges
from fftools.glyph import TransformOption
from fftools.option import GlyphsOption
from fftools import file, ranges, select, glyph


def _merged_ranges(opts: List[GlyphsOption]) -> UnicodeRanges:
    """Returns the merged ranges."""
    if len(opts) <= 1:
        return opts[0].ranges

    _ranges = []
    for opt in opts:
        _ranges += opt.ranges

    return _ranges


def _delete_unused_ranges(font: fontforge.font, opts: List[GlyphsOption]) -> NoReturn:
    """Deletes the unused ranges."""
    _ranges = ranges.sort_ranges(_merged_ranges(opts))
    unused_ranges = ranges.get_unused_ranges(_ranges)
    if unused_ranges is not None:
        select.select_ranges(font, unused_ranges)
        font.clear()


def _transform_glyphs(font: fontforge.font, _ranges: UnicodeRanges, trans: TransformOption) -> NoReturn:
    """Transforms the glyphs in ranges."""
    select.select_ranges(font, _ranges)
    glyph.transform(font, trans)


def _move_glyphs(font: fontforge.font, before: UnicodeRange, afrer: UnicodeRange) -> NoReturn:
    """Moves the glyphs."""
    select.select_ranges(font, before)
    font.cut()
    select.select_ranges(font, afrer)
    font.paste()
    select.select_ranges(font, before)
    font.clear()


def _change_glyphs(font: fontforge.font, opts: List[GlyphsOption]) -> NoReturn:
    """Changes glyphs."""
    for opt in opts:
        if opt.transform is not None:
            _transform_glyphs(font, opt.ranges, opt.transform)
        if opt.moving_plans is not None:
            _move_glyphs(font, opt.moving_plans[0], opt.moving_plans[-1])


def generate_sfd(font: fontforge.font, opts: Optional[List[GlyphsOption]], path: str) -> NoReturn:
    """Generates the SFD file."""
    if opts is not None:
        _delete_unused_ranges(font, opts)
        _change_glyphs(font, opts)

    file.save_font(font, path)
