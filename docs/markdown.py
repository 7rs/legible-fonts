from types import ModuleType
from typing import List

from docs import attr, modules
from docs.attr import Function


def get_function_header(function: Function) -> str:
    header = " " * 2 + f"- ### `{function.__name__}`  " + "\n"

    if not function.__annotations__:
        return header

    if "return" in function.__annotations__:
        _return = function.__annotations__.pop("return")
    else:
        _return = "NoReturn"

    args: List[str] = []
    for arg in function.__annotations__:
        if type(function.__annotations__[arg]) == str:
            args.append(arg + "\t" + f"`{function.__annotations__[arg]}`")
        else:
            args.append(arg + "\t" + f"`{function.__annotations__[arg].__name__}`")

    if function.__doc__:
        header += " " * 4 + f"{function.__doc__}  " + "\n" * 2

    header += " " * 4 + "- Arguments  " + "\n"
    for arg in args:
        header += " " * 6 + f"- {arg}  " + "\n"

    header += " " * 4 + "- Returns  " + "\n"
    header += " " * 6 + f"- {_return}  " + "\n"
    return header


def get_module_docs(module: ModuleType) -> str:
    md = "\n" + f"## {module.__name__}  " + "\n" * 2

    functions = attr.get_functions(attr.get_attributes(module))
    if not functions:
        return ""

    for function in functions:
        md += get_function_header(function)
    return md


def get_package_docs(package: ModuleType) -> str:
    md = f"# {package.__name__}" + "\n" * 2

    mods = modules.analyze_package(package)
    for mod in mods:
        md += get_module_docs(mod)

    return md
