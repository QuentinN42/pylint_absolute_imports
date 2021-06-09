"""Strict check of the import."""
from astroid import ImportFrom  # type: ignore
from pylint.interfaces import IAstroidChecker  # type: ignore
from pylint.checkers import BaseChecker  # type: ignore


def is_relative(node: ImportFrom) -> bool:
    """Returns True, if import is relative, False otherwise. """
    return node.level is not None and node.level > 0


class AbsoluteImportChecker(BaseChecker):

    """Pylint checker for imports."""

    __implements__ = IAstroidChecker

    name = 'relative-import'
    priority = -1
    msgs = {
        'C0001': (
            'Unacceptable relative import',
            name,
            'Consider using absolute import',
        ),
    }

    def visit_importfrom(self, node: ImportFrom):
        """Look for relative imports."""
        if is_relative(node):
            self.add_message(
                'C0001',
                line=node.lineno,
                node=node,
                col_offset=node.col_offset,
            )
