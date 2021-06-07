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
