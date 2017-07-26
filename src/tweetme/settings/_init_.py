from .base import *
# Whe in production 
from .production import *
 
 # the one we are currently using.
try:
	from .local import *
except:
	pass
