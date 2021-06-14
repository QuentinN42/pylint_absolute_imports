# coding: utf-8
from astroid import ImportFrom
from astroid import Module


def levels_to_toplevel(node: ImportFrom) -> int:
    """Returns the number of packages up to toplevel of project. """
    module: Module = node.root()
    dots_count = module.name.count('.')
    if module.file.endswith('__init__.py'):
        return dots_count + 1
    return dots_count


def is_relative(node: ImportFrom) -> bool:
    """Returns True, if import is relative, False otherwise. """
    return node.level is not None and node.level > 0
