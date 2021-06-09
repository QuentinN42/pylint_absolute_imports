"""Pylint import checking module."""

from pylint_absolute_imports.checker import AbsoluteImportChecker


def register(linter):
    """Add the current checker to pylint."""
    linter.register_checker(AbsoluteImportChecker(linter))
