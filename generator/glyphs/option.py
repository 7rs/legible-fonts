from typing import Optional, List, Dict

from configurator.glyphs.option import Fonts, GlyphsOption
from generator.glyphs import ranges, trans, name


FONTS_OPTION: Dict[Fonts, List[GlyphsOption]] = {}

FONTS_OPTION[Fonts.IOSEVKA_EXTENDED] = [
    GlyphsOption(
        ranges.IosevkaExtended.ALL,
        trans.IosevkaExtended.ALL,
    )
]

FONTS_OPTION[Fonts.BIZ_UDGOTHIC] = [
    GlyphsOption(ranges.BIZUDGothic.HALF_WIDTH_KATAKANA, trans.BIZUDGothic.HALF_WIDTH_KATAKANA),
    GlyphsOption(ranges.BIZUDGothic.FULL_WIDTH_HIRAGANA, trans.BIZUDGothic.FULL_WIDTH_HIRAGANA),
    GlyphsOption(ranges.BIZUDGothic.FULL_WIDTH_LATIN, trans.BIZUDGothic.FULL_WIDTH_LATIN),
    GlyphsOption(ranges.BIZUDGothic.FULL_SIZE_GLYPHS, trans.BIZUDGothic.FULL_SIZE_GLYPHS),
]

FONTS_OPTION[Fonts.NERD_FONTS] = [
    GlyphsOption(
        ranges.NerdFonts.ALL,
        moving_plan=((0xF900, 0xFD46), (0xE800, 0xEC46)),
        new_names=name.NerdFonts.ALL,
    )
]

FONTS_OPTION[Fonts.NOTO_EMOJI] = [
    GlyphsOption(
        ranges.NotoEmoji.ALL,
        trans.NotoEmoji.ALL,
        new_names=name.NotoEmoji.ALL,
    )
]


def get_options(font_name: Fonts) -> Optional[List[GlyphsOption]]:
    """Returns options to change glyphs from a font name."""
    if font_name in FONTS_OPTION:
        return FONTS_OPTION[font_name]
    return None
