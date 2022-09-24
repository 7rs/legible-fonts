from typing import List
import glob


def get_all_modules(module_path: str) -> List[str]:
    """Returns module names."""
    paths = [path.split("/")[-1] for path in glob.glob(f"{module_path}/*")]
    paths = [path for path in paths if not path.startswith("__")]
    for i in range(len(paths)):
        if paths[i].endswith(".py"):
            paths[i] = paths[i][:-3]

    return paths
