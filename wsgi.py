import sys
path = '/home/removevj/togelchina_project'  # Ganti dengan username Anda
if path not in sys.path:
    sys.path.append(path)

from bot import app as application
