# coding: utf-8
from astroid import ImportFrom
from astroid import Module


def get_module_from_importfrom(node: ImportFrom) -> Module:
    parent = node.parent
    while not isinstance(parent, Module):
        parent = parent.parent
    return parent


def levels_to_toplevel(node: ImportFrom):
    module = get_module_from_importfrom(node)
    return module.name.count('.')


def is_relative(node: ImportFrom):
    return node.level is not None and node.level > 0
