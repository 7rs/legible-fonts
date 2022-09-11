from typing import List, Dict

from generator.configurator.glyph import TransformOption
from generator.configurator.option import Fonts, GlyphsOption


# The font file paths
FONTS_PATH: Dict[Fonts, str] = {
    Fonts.FONTS_DIR: "./source/fonts/regular/",
    Fonts.IOSEVKA: "iosevka-custom-regular.ttf",
    Fonts.IOSEVKA_EXTENDED: "iosevka-custom-extended.ttf",
    Fonts.BIZ_UDGOTHIC: "BIZUDGothic-Regular.ttf",
    Fonts.NERD_FONTS: "Symbols-1000-em Nerd Font Complete Mono.ttf",
    Fonts.NOTO_EMOJI: "NotoEmoji-Regular.ttf",
    Fonts.FIRACODE: "FiraCode-Regular.ttf",
}

# The SFD file paths
SFD_PATH: Dict[Fonts, str] = {
    Fonts.FONTS_DIR: "./source/sfd/regular/",
    Fonts.IOSEVKA: "iosevka.sfd",
    Fonts.IOSEVKA_EXTENDED: "iosevka-extended.sfd",
    Fonts.BIZ_UDGOTHIC: "biz_udgothic.sfd",
    Fonts.NERD_FONTS: "nerd-fonts.sfd",
    Fonts.NOTO_EMOJI: "noto-emoji.sfd",
    Fonts.FIRACODE: "firacode.sfd",
}

# The options for fonts
FONTS_OPTION: Dict[Fonts, List[GlyphsOption]] = {}

# Iosevka
FONTS_OPTION[Fonts.IOSEVKA_EXTENDED] = [
    GlyphsOption(
        [
            # Basic Multilingual Plane; BMP
            (0x0000, 0x052F),
            (0x0E00, 0x0E7F),
            (0x1AB0, 0x1AFF),
            (0x1D00, 0x243F),
            (0x2460, 0x2BFF),
            (0x2C60, 0x2C7F),
            (0x2DE0, 0x2E7F),
            (0xA640, 0xA69F),
            (0xA700, 0xA7FF),
            (0xAB30, 0xAB6F),
            (0xFB00, 0xFB4F),
            (0xFFF0, 0xFFFF),
            # Supplementary Multilingual Plane; SMP
            (0x1D400, 0x1D7FF),
            (0x1F100, 0x1F1FF),
            (0x1F300, 0x1F5FF),
            (0x1F780, 0x1F8FF),
            (0x1FB00, 0x1FBFF),
        ],
        TransformOption(scaling=0.83, x_movement=1, before_width=498, after_width=500),
        # 500  ÷ 600       = 0.833... -> 0.83
        # 600  × 0.83      = 498
        # (500 − 498) ÷ 2 = 1
    )
]

# BIZ UDGothic
FONTS_OPTION[Fonts.BIZ_UDGOTHIC] = [
    # Half width
    GlyphsOption(
        [
            # Basic Multilingual Plane; BMP
            (0xFF61, 0xFFDF)
        ],
        TransformOption(scaling=0.44, x_movement=25, before_width=451, after_width=500),
        # 800  ÷ 1802      = 0.443... -> 0.44
        # 1024 × 0.44      = 450.56   -> 451
        # (500 − 451) ÷ 2 = 24.5     -> 25
    ),
    # Full width
    GlyphsOption(
        [
            # Basic Multilingual Plane; BMP
            (0x3000, 0x30FF),
            (0xFF00, 0xFF60),
            (0xFFE0, 0xFFEF),
        ],
        TransformOption(scaling=0.44, x_movement=50, before_width=901, after_width=1000),
        # 800   ÷ 1802      = 0.443... -> 0.44
        # 2048  × 0.44      = 901.2    -> 901
        # (1000 − 901) ÷ 2 = 49.5     -> 50
    ),
    # Full size
    GlyphsOption(
        [
            # Basic Multilingual Plane; BMP
            (0x31F0, 0x4DBF),
            (0x4E00, 0x9FFF),
            (0xF900, 0xFAFF),
            (0xFE30, 0xFE4F),
            # Supplementary Multilingual Plane; SMP
            (0x20000, 0x2A6DF),
            (0x2F800, 0x2FA1F),
        ],
        TransformOption(scaling=0.39, x_movement=101, before_width=799, after_width=1000),
        # 800   ÷ 2048      = 0.390... -> 0.39
        # 2048  × 0.39      = 798.72   -> 799
        # (1000 − 799) ÷ 2 = 100.5    -> 101
    ),
]

# Nerd Fonts
FONTS_OPTION[Fonts.NERD_FONTS] = [
    GlyphsOption(
        [
            # Basic Multilingual Plane; BMP
            (0xE000, 0xFD46)
        ],
        moving_plans=[((0xF900, 0xFD46), (0xE800, 0xEC46))],
    )
]

# Noto Emoji
FONTS_OPTION[Fonts.NOTO_EMOJI] = [
    GlyphsOption(
        [
            # Supplementary Multilingual Plane; SMP
            (0x1F300, 0x1F64F),
            (0x1F680, 0x1F6FF),
            (0x1F780, 0x1F7FF),
            (0x1F900, 0x1F9FF),
            (0x1FA70, 0x1FAFF),
        ],
        TransformOption(scaling=0.47, x_movement=24, before_width=963, after_width=1000),
    )
]
