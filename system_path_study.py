import os
import sys

_path = os.getcwd()

filename = '/mytools'
_path = _path + filename

# sys.path.append(_path)
# sys.path.remove(_path)

print(sys.path)
