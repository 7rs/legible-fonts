from dataclasses import dataclass

from fftools.font import FontOption, Copyright, Name, Size, Underline
from fftools import font


@dataclass
class SFDOption(FontOption):
    size: Size = Size(ascent=800, descent=200)
    underline: Underline = Underline(position=-100, height=50)
    italic_angle: float = 0.2
    encoding: str = "UnicodeFull"


@dataclass
class LegibleFonts(FontOption):
    name: Name = Name(
        family="Legible",
        fond="Regular",
        font="Legible-Fonts",
        font_full="Legible-Fonts",
        copyright=font.get_copyrights(
            [
                Copyright("Legible Fonts", "Cbrnex", "2022", "github.com/7rs"),
                Copyright("Iosevka", "Renzhi", "2015-2021", "aka. Belleve Invis, belleve@typeof.net"),
                Copyright(
                    "BIZ UDGothic",
                    "The BIZ UDGothic Project Authors",
                    "2022",
                    "https://github.com/googlefonts/morisawa-biz-ud-gothic",
                ),
                Copyright("Nerd Fonts", "Ryan McIntyre", "2016"),
                Copyright("Noto Emoji", "Google Inc.", "2013, 2021"),
                Copyright(
                    "FiraCode",
                    "The Fira Code Project Authors",
                    "2014-2021",
                    "https://github.com/tonsky/FiraCode",
                ),
                Copyright("FontForge", "George Williams", "2000-2012", "https://github.com/fontforge/fontforge"),
            ]
        ),
    )
    size: Size = Size(ascent=800, descent=200)
    underline: Underline = Underline(position=-100, height=50)
    italic_angle: float = 0.2
    encoding: str = "UnicodeFull"
