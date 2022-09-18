from typing import NoReturn
from enum import Enum
from dataclasses import dataclass

import fontforge


class Width(Enum):
    """
    ULTRA_CONDENSED (1) 50%
    EXTRA_CONDENSED (2) 62.5%
    CONDENSED       (3) 75%
    SEMI_CONDENSED  (4) 87.5%
    NORMAL          (5) 100%
    SEMI_EXPANDED   (6) 112.5%
    EXPANDED        (7) 125%
    EXTRA_EXPANDED  (8) 150%
    ULTRA_EXPANDED  (9) 200%
    """

    ULTRA_CONDENSED = 1
    EXTRA_CONDENSED = 2
    CONDENSED = 3
    SEMI_CONDENSED = 4
    NORMAL = 5
    SEMI_EXPANDED = 6
    EXPANDED = 7
    EXTRA_EXPANDED = 8
    ULTRA_EXPANDED = 9


class Weight(Enum):
    """
    THIN
    EXTRALIGHT (2) 200
    LIGHT      (3) 300
    NORMAL     (4) 400
    MEDIUM     (5) 500
    SEMIBOLD   (6) 600
    BOLD       (7) 700
    EXTRABOLD  (8) 800
    BLACK      (9) 900
    """

    THIN = 1
    EXTRALIGHT = 2
    LIGHT = 3
    NORMAL = 4
    MEDIUM = 5
    SEMIBOLD = 6
    BOLD = 7
    EXTRABOLD = 8
    BLACK = 9


class FsType(Enum):
    NONE = 0

    INSTALLABLE_EMBEDDING = 1
    RESTRICTED_LICENSE_EMBEDDING = 2
    PREWVIEW_AND_PRINT_EMBEDDING = 4
    EDITABLE_EMBEDDING = 8


def create_fstype(embedding: FsType, no_subsetting: bool = False, bitmap_embedding_only: bool = False) -> int:
    """Returns a fstype from arguments."""
    embedding: int = embedding.value
    if no_subsetting:
        embedding += 256  # 8bit
    if bitmap_embedding_only:
        embedding += 512  # 9bit
    return embedding


@dataclass
class OS2MetricsTable:
    vendor: str
    fstype: int
    weight: Weight
    width: Width


def set_os2_metrics_table(font: fontforge.font, table: OS2MetricsTable) -> NoReturn:
    """Sets option about OS/2 Metrics Table."""

    font.os2_vendor = table.vendor
    font.os2_fstype = table.fstype
    font.os2_weight = table.weight.value
    font.os2_width = table.width.value
