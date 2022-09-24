from typing import List
from types import ModuleType

from docs import attr


def get_all_module(package: ModuleType) -> List[ModuleType]:
    """Returns modules includes a package."""
    return [
        mod
        for mod in attr.get_attributes(package)
        if (type(mod) == ModuleType) and (mod.__name__.startswith(package.__name__))
    ]


def analyze_package(package: ModuleType) -> List[ModuleType]:
    """Analyzes a package and Returns module list."""
    mods = get_all_module(package)
    if mods:
        for mod in mods:
            mods += analyze_package(mod)

    return mods
