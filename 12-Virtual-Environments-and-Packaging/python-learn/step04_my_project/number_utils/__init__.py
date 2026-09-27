# __init__.py is the package's front door. Python runs it when number_utils is imported.
# It brings the functions out, so other files can do: from number_utils import double, percentage
from number_utils.calculations import double, percentage

# __all__ lists what "from number_utils import *" hands out. Named imports are not affected.
__all__ = ["double", "percentage"]
