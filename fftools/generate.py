from typing import NoReturn, Optional, List

import fontforge

from fftools.option import InvalidFontError, Fonts, GlyphsOption
from fftools.font import FontOption
from fftools import file, font, sfd, plan, table, select
from fftools import SFDOption, LegibleFonts


FONT_NAMES = [Fonts.IOSEVKA_EXTENDED, Fonts.BIZ_UDGOTHIC, Fonts.NERD_FONTS, Fonts.NOTO_EMOJI]


def _open_font(font_name: Fonts) -> fontforge.font:
    """Returns the fontforge.font class."""
    if font_name not in plan.FONTS_PATH:
        raise InvalidFontError("Not found the font file.")
    return file.open_font(plan.FONTS_PATH[Fonts.FONTS_DIR] + plan.FONTS_PATH[font_name])


def _get_options(font_name: Fonts) -> Optional[List[GlyphsOption]]:
    """Returns the font options."""
    if font_name in plan.FONTS_OPTION:
        return plan.FONTS_OPTION[font_name]
    return None


def _get_sfd_path(font_name: Fonts) -> str:
    """Return the SFD path."""
    if font_name not in plan.SFD_PATH:
        raise InvalidFontError("Invaild the font.")
    return plan.SFD_PATH[Fonts.FONTS_DIR] + plan.SFD_PATH[font_name]


def _generate_sfd_file(font_name: Fonts, opt: FontOption) -> NoReturn:
    """Generates the SFD file."""
    _font = _open_font(font_name)
    font.set_option(_font, opt)
    sfd.generate_sfd(_font, _get_options(font_name), _get_sfd_path(font_name))


def generate_sfd_files() -> NoReturn:
    """Generates the SFD files."""
    opt = SFDOption()
    for font_name in FONT_NAMES:
        _generate_sfd_file(font_name, opt)


def merge_sfd_files() -> NoReturn:
    """Merges the SFD files."""
    _font = fontforge.font()
    font.set_option(_font, LegibleFonts())

    for font_name in FONT_NAMES:
        file.merge_font(_font, _get_sfd_path(font_name))

    table.delete_all_lookups(_font)
    select.select_invalid_glyphs(_font)
    _font.clear()

    file.generate_font(_font, "./dist/legible-fonts.ttf")
