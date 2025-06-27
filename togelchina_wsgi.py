import sys
import os

# Tambahkan path ke project directory
path = '/home/removevj/togelchina_project'
if path not in sys.path:
    sys.path.append(path)

# Set environment (jika perlu)
os.environ['FLASK_ENV'] = 'production'

# Import objek Flask
from web import application