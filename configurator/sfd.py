from typing import NoReturn, Optional, List

import fontforge

from configurator.glyphs.ranges import UnicodeRanges
from configurator.glyphs.trans import TransformOption
from configurator.glyphs.option import GlyphsOption, MovingPlan
from configurator.glyphs import ranges, select, trans, name
from configurator.fonts import file


def _merged_ranges(opts: List[GlyphsOption]) -> UnicodeRanges:
    """Returns merged ranges."""
    if len(opts) <= 1:
        return opts[0].ranges

    _ranges = []
    for opt in opts:
        _ranges += opt.ranges

    return _ranges


def _delete_unused_ranges(font: fontforge.font, opts: List[GlyphsOption]) -> NoReturn:
    """Deletes unused ranges."""
    _ranges = ranges.sort_ranges(_merged_ranges(opts))
    unused_ranges = ranges.get_unused_ranges(_ranges)
    if unused_ranges is not None:
        select.select_ranges(font, unused_ranges)
        font.clear()


def _transform_glyphs(font: fontforge.font, _ranges: UnicodeRanges, opt: TransformOption) -> NoReturn:
    """Transforms glyphs in ranges."""
    select.select_ranges(font, _ranges)
    trans.transform(font, opt)


def _move_glyphs(font: fontforge.font, plan: MovingPlan) -> NoReturn:
    """Moves glyphs."""
    select.select_ranges(font, [plan[0]])
    font.cut()
    select.select_ranges(font, [plan[-1]])
    font.paste()
    select.select_ranges(font, [plan[0]])
    font.clear()


def _change_glyphs(font: fontforge.font, opts: List[GlyphsOption]) -> NoReturn:
    """Changes glyphs."""
    for opt in opts:
        if opt.transform is not None:
            _transform_glyphs(font, opt.ranges, opt.transform)
        if opt.moving_plan is not None:
            _move_glyphs(font, opt.moving_plan)
        if opt.new_names:
            name.change_glyphs_name(font, opt.new_names)


def generate_sfd(font: fontforge.font, opts: Optional[List[GlyphsOption]], path: str) -> NoReturn:
    """Generates the SFD file."""
    if opts is not None:
        _delete_unused_ranges(font, opts)
        _change_glyphs(font, opts)

    file.save_font(font, path)
