from typing import NoReturn, Optional, Tuple, List

import fontforge


UnicodeRange = Tuple[int, int]
UnicodeRanges = List[UnicodeRange]


class InvalidRangeError(Exception):
    pass


def _get_min_index(ranges: UnicodeRanges) -> int:
    """Returns the minimum index value of ranges."""
    min_index = 0

    _min = 0x110000
    for i in range(len(ranges)):
        if ranges[i][0] >= _min:
            continue
        _min = ranges[i][0]
        min_index = i

    return min_index


def correct_range(start: int, end: int) -> NoReturn:
    """Checks if the start and the end of range in Unicode is correct."""
    if start < 0x0000:
        raise InvalidRangeError("Invalid range. Unicode starts at U+0000")
    elif end > 0x10FFFF:
        raise InvalidRangeError("Invaild range. Unicode is up to U+10FFFF")


def correct_point(glyph: fontforge.glyph) -> bool:
    """Checks if the point in Unicode is correct."""
    if glyph.encoding > 0x10FFFF:
        return False
    elif glyph.unicode == -1:
        return False
    else:
        return True


def sort_ranges(ranges: UnicodeRanges) -> UnicodeRanges:
    """Returns the sorted ranges."""
    for i in range(len(ranges) - 1):
        min_index = _get_min_index(ranges[i:]) + i

        old_min = ranges[i]
        ranges[i] = ranges[min_index]
        ranges[min_index] = old_min

    return ranges


def get_unused_ranges(ranges: UnicodeRanges) -> Optional[UnicodeRanges]:
    """Returns the unused ranges."""
    unused: UnicodeRanges = []

    first_range = ranges[0]
    if first_range[0] != 0x0000:
        unused.append((0x0000, first_range[0] - 1))

    end = first_range[-1] + 1
    for _range in ranges[1:-2]:
        unused.append((end, _range[0] - 1))
        end = _range[-1] + 1

    last_range = ranges[-1]
    if last_range[-1] < 0x10FFFF:
        unused.append((last_range[-1] + 1, 0x10FFFF))

    if not unused:
        return None
    return unused
