from typing import NoReturn, Optional, List

import fontforge

from generator.configurator.fonts import FontOption
from generator.configurator.option import InvalidFontError, Fonts, GlyphsOption
from generator.configurator import file, fonts, table, select, sfd
from generator import SFDOption, LegibleFonts
from generator import config


FONT_NAMES = [Fonts.IOSEVKA_EXTENDED, Fonts.BIZ_UDGOTHIC, Fonts.NERD_FONTS, Fonts.NOTO_EMOJI]


def _open_font(font_name: Fonts) -> fontforge.font:
    """Returns the font object from the font name."""
    if font_name not in config.FONTS_PATH:
        raise InvalidFontError("Not found the font file.")
    return file.open_font(config.FONTS_PATH[Fonts.FONTS_DIR] + config.FONTS_PATH[font_name])


def _get_options(font_name: Fonts) -> Optional[List[GlyphsOption]]:
    """Returns the options for the glyphs from the font names."""
    if font_name in config.FONTS_OPTION:
        return config.FONTS_OPTION[font_name]
    return None


def _get_sfd_path(font_name: Fonts) -> str:
    """Returns the SFD path from the font name."""
    if font_name not in config.SFD_PATH:
        raise InvalidFontError("Invaild the font.")
    return config.SFD_PATH[Fonts.FONTS_DIR] + config.SFD_PATH[font_name]


def _generate_sfd_file(font_name: Fonts, opt: FontOption) -> NoReturn:
    """Generates the SFD file from the font name and option for the font."""
    font = _open_font(font_name)
    fonts.set_option(font, opt)
    sfd.generate_sfd(font, _get_options(font_name), _get_sfd_path(font_name))


def generate_sfd_files() -> NoReturn:
    """Generates the SFD files."""
    opt = SFDOption()
    for font_name in FONT_NAMES:
        _generate_sfd_file(font_name, opt)


def merge_sfd_files() -> NoReturn:
    """Merges the SFD files into a single font file."""
    font = fontforge.font()
    fonts.set_option(font, LegibleFonts())

    for font_name in FONT_NAMES:
        file.merge_font(font, _get_sfd_path(font_name))

    table.delete_all_lookups(font)
    select.select_invalid_glyphs(font)
    font.clear()

    file.generate_font(font, "./dist/legible-fonts.ttf")
