from typing import Dict

import fontforge

from configurator.glyphs.option import Fonts, InvalidFontError
from configurator.fonts import file


class Regular:
    FONTS_PATH: Dict[Fonts, str] = {
        Fonts.FONTS_DIR: "./source/fonts/regular/",
        Fonts.IOSEVKA: "iosevka-custom-regular.ttf",
        Fonts.IOSEVKA_EXTENDED: "iosevka-custom-extended.ttf",
        Fonts.BIZ_UDGOTHIC: "BIZUDGothic-Regular.ttf",
        Fonts.NERD_FONTS: "Symbols-1000-em Nerd Font Complete Mono.ttf",
        Fonts.NOTO_EMOJI: "NotoEmoji-Regular.ttf",
        Fonts.FIRACODE: "FiraCode-Regular.ttf",
    }

    SFD_PATH: Dict[Fonts, str] = {
        Fonts.FONTS_DIR: "./source/sfd/regular/",
        Fonts.IOSEVKA: "iosevka.sfd",
        Fonts.IOSEVKA_EXTENDED: "iosevka-extended.sfd",
        Fonts.BIZ_UDGOTHIC: "biz_udgothic.sfd",
        Fonts.NERD_FONTS: "nerd-fonts.sfd",
        Fonts.NOTO_EMOJI: "noto-emoji.sfd",
        Fonts.FIRACODE: "firacode.sfd",
    }


def open_font(font_name: Fonts) -> fontforge.font:
    """Returns the font object from a font name."""
    if font_name not in Regular.FONTS_PATH:
        raise InvalidFontError("Not found the font file.")
    return file.open_font(Regular.FONTS_PATH[Fonts.FONTS_DIR] + Regular.FONTS_PATH[font_name])


def get_sfd_path(font_name: Fonts) -> str:
    """Returns the SFD path from a font name."""
    if font_name not in Regular.SFD_PATH:
        raise InvalidFontError("Invaild the font.")
    return Regular.SFD_PATH[Fonts.FONTS_DIR] + Regular.SFD_PATH[font_name]
