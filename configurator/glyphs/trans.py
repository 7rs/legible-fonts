from typing import NoReturn, Optional, Tuple
from dataclasses import dataclass

import fontforge
import psMat

Matrix = Tuple[float, float, float, float, float, float]


@dataclass
class TransformOption:
    """The option to transform glyphs."""

    scaling: Optional[float] = None
    x_movement: Optional[int] = None
    y_movement: Optional[int] = None

    before_width: Optional[int] = None
    after_width: Optional[int] = None


def _get_matrix(
    scaling: float,
    x_translate: Optional[int] = None,
    y_translate: Optional[int] = None,
) -> Matrix:
    """
    Returns the matrix object.
    (The matrix object is an object to transform glyphs.)
    """
    if (x_translate is None) and (y_translate is None):
        # x_translate=None, y_translate=None
        return psMat.scale(scaling)
    elif (x_translate is not None) and (y_translate is None):
        # y_translate=None
        return psMat.compose(psMat.scale(scaling), psMat.translate(x_translate, 0))
    elif (x_translate is None) and (y_translate is not None):
        # x_translate=None
        return psMat.compose(psMat.scale(scaling), psMat.translate(0, y_translate))
    else:
        return psMat.compose(psMat.scale(scaling), psMat.translate(x_translate, y_translate))


def _update_widths(font: fontforge.font, before: int, after: int) -> NoReturn:
    """Updates selected glyphs width."""
    for glyph in font.selection.byGlyphs:
        if glyph.width >= before:
            glyph.width = after


def transform(font: fontforge.font, option: TransformOption) -> NoReturn:
    """Transforms glyphs from the transform option."""
    font.transform(_get_matrix(option.scaling, option.x_movement, option.y_movement))
    _update_widths(font, option.before_width, option.after_width)
