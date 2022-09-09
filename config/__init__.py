import os

MODE = os.environ.get("DEBUG")
if MODE:
    from .dev_settings import *
else:
    from .prod_settings import *


# MODE = os.environ['DJANGO_SETTINGS_MODULE']
# print("Env Mode..........", MODE)
# delete these - experimenting as not working otherwise
# from .development import *

# if environ['DJANGO_SETTINGS_MODULE'] == 'staturmon.settings':
# from .development import *
# from .production import *