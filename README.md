# Pylint relative imports plugin

## What for?

This is a simple Pylint plugin for checking relative import from the root of
the project. For example, in Django projects it's ofter not recommended to
import from another app. This plugin checks such imports and adds errors.

```python
# project/
# |---- shop/
#       |---- __init__.py
#       |---- models.py
#       |---- views.py
# |---- employee/
#       |---- __init__.py
#       |---- models.py
#       |---- views.py

# in project/shop/views.py
from ..employee.models import Employee  # <- BAD
from project.employee.models import Employee  # <- Good
```

## Installation

```bash
pip install pylint-relative-imports
```

## Usage

In `pylint.rc`:

```toml
[MASTER]
load-plugins=pylint_relative_imports.relative_imports_checker
```

Or, in terminal:

```bash
pylint --load-plugins pylint_relative_imports.relative_imports_checker foo.py
```

## Strict mode

If you want that any relative imports raise an error, you use `strict_relative_imports_checker` instead of `relative_imports_checker`.
So even `from .utils import is_relative` will be catch.

In `pylint.rc`:

```toml
[MASTER]
load-plugins=pylint_relative_imports.strict_relative_imports_checker
```

Or, in terminal:

```bash
pylint --load-plugins pylint_relative_imports.strict_relative_imports_checker foo.py
```
