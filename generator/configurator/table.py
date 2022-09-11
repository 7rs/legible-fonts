from typing import NoReturn, Optional, List
from enum import Enum

import fontforge


Lookups = List[str]
Subtables = List[str]


class LookupType(Enum):
    NONE = 0
    GLYPH_SUBTABLE = 1
    GLYPH_POSITION = 2
    BOTH = 3


def _get_lookups(font: fontforge.font, _type: LookupType) -> Optional[Lookups]:
    """Returns the lookups. (GSUB/GPOS)"""
    if _type == LookupType.GLYPH_SUBTABLE:
        lookups = list(font.gsub_lookups)
    elif _type == LookupType.GLYPH_POSITION:
        lookups = list(font.gpos_lookups)
    elif _type == LookupType.BOTH:
        lookups = list(font.gsub_lookups) + list(font.gpos_lookups)
    else:
        lookups = []

    if not lookups:
        return None
    return lookups


def _get_subtables(font: fontforge.font, lookups: Lookups) -> Optional[Subtables]:
    """Returns the subtables."""
    sub = [subtable for lookup in lookups for subtable in font.getLookupSubtables(lookup)]
    if not sub:
        return None
    return sub


def _delete_lookups(font: fontforge.font, lookups: Lookups) -> NoReturn:
    """Deletes the lookups."""
    for lookup in lookups:
        font.removeLookup(lookup)


def _delete_subtables(font: fontforge.font, subtables: Subtables) -> NoReturn:
    """Deletes the subtables."""
    for subtable in subtables:
        font.removeLookupSubtable(subtable)


def delete_all_lookups(font: fontforge.font) -> NoReturn:
    """Deletes the all lookups, including the subtables."""
    lookups = _get_lookups(font, LookupType.BOTH)
    if lookups is None:
        return

    subtables = _get_subtables(font, lookups)
    if subtables is not None:
        _delete_subtables(font, subtables)

    _delete_lookups(font, lookups)
