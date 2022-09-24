from typing import NoReturn, Tuple, List

import fontforge

NewName = Tuple[int, str]


def change_glyph_name(glyph: fontforge.glyph, name: str) -> NoReturn:
    """Changes a name for a glyph."""
    glyph.glyphname = name


def change_glyphs_name(font: fontforge.font, names: List[NewName]) -> NoReturn:
    """Changes a name for glyphs."""
    points = [name[0] for name in names]
    for glyph in font.glyphs():
        if glyph.encoding not in points:
            continue
        glyph.glyphname = names[points.index(glyph.encoding)][1]
