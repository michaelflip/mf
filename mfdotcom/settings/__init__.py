from .base import *

try:
    from .local import *
    live = False
    print 'Using local settings'

except:
    live = True
    print 'Using prod settings'

if live:
    from .production import *
