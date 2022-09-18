from typing import NoReturn

try:
    import fontforge
except ImportError:
    raise Exception("Fontforge is required: https://fontforge.org")

from configurator.fonts.option import FontOption
from configurator.fonts import file, table, option
from configurator.glyphs.option import Fonts
from configurator.glyphs import select
from configurator import sfd
from generator.glyphs import path, name
from generator.glyphs import option as config
from generator.fonts.option import SFDOption, LegibleFonts


FONT_NAMES = [Fonts.IOSEVKA_EXTENDED, Fonts.BIZ_UDGOTHIC, Fonts.NERD_FONTS, Fonts.NOTO_EMOJI]


def _generate_sfd_file(font_name: Fonts, opt: FontOption) -> NoReturn:
    """Generates the SFD file from the font name and option for the font."""
    font = path.open_font(font_name)
    option.set_option(font, opt)
    sfd.generate_sfd(font, config.get_options(font_name), path.get_sfd_path(font_name))


def generate_sfd_files() -> NoReturn:
    """Generates the SFD files."""
    opt = SFDOption()
    for font_name in FONT_NAMES:
        _generate_sfd_file(font_name, opt)


def _fix_names(font: fontforge.font) -> NoReturn:
    """Fixes the name for glyphs."""
    name.change_glyph_names(font, name.NerdFonts.ALL, new_name=None, add_name=name.NerdFonts.NAME)
    name.change_glyph_names(font, name.NotoEmoji.ALL, new_name=None, add_name=name.NotoEmoji.NAME)


def merge_sfd_files() -> NoReturn:
    """Merges the SFD files into a single font file."""
    font = fontforge.font()
    option.set_option(font, LegibleFonts())

    for font_name in FONT_NAMES:
        file.merge_font(font, path.get_sfd_path(font_name))

    table.delete_all_lookups(font)
    select.select_invalid_glyphs(font)
    font.clear()

    file.generate_font(font, "./dist/legible-fonts.ttf")
