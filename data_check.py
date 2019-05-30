import os
if os.path.exists('data'):
    pass
else:
    raise Exception('no data file found')