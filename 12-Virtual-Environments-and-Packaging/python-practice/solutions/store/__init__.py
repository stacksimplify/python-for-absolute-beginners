# __init__.py is the store package's front door. Python runs it when store is imported.
# It brings the functions out, so other files can do: from store import line_total, apply_discount
from store.pricing import line_total, apply_discount

# __all__ lists what "from store import *" hands out. Named imports are not affected.
__all__ = ["line_total", "apply_discount"]
