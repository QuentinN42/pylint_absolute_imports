# Pylint force absolute imports plugin

## What for?

Following [PEP8 recommendation about imports](https://peps.python.org/pep-0008/#imports), `import` statements should be absolute :

> Standard library code should avoid complex package layouts and always use absolute imports.

```python
# project/
# |---- __init__.py
# |---- employee.py

from .employee import Employee  # <- BAD
from project.employee import Employee  # <- Good
```

## Installation

```bash
pip install pylint_absolute_imports
```

## Usage

In `pylint.rc`:

```toml
[MASTER]
load-plugins=pylint_absolute_imports
```

Or, in terminal:

```bash
pylint --load-plugins pylint_absolute_imports foo.py
```
