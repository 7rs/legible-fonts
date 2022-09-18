from configurator.fonts.option import Underline
from configurator.fonts.name import Copyright
from configurator.fonts.size import Size
from configurator.fonts import name

SIZE_OPTION = Size(ascent=800, descent=200)
UNDERLINE_OPTION = Underline(position=-100, height=50)
ITALIC_ANGLE_OPTION = 0.2
ENCODING_OPTION = "UnicodeFull"

COPYRIGHTS = name.get_copyrights(
    [
        Copyright("Legible Fonts", "Cbrnex", "2022", "https://github.com/7rs"),
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
)
