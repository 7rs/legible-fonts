from typing import List, Callable, Any
from types import ModuleType

Function = Callable[[Any], Any]


def get_attributes(mod: ModuleType) -> List[object]:
    """Returns attributes."""
    return [mod.__getattribute__(attr) for attr in dir(mod) if not attr.startswith("_")]


def get_functions(attrs: List[object]) -> List[Function]:
    """Returns functions."""
    return [attr for attr in attrs if type(attr).__name__ == "function"]


def get_function_datail(function: Function):
    if "__annotations__" not in dir(function):
        return
    print(function.__annotations__)
