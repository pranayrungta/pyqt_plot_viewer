"""Install GUI integration on XDG platforms (primarily Linux)"""
import os
from pathlib import Path
from subprocess import run
import sys

wd = Path(__file__).resolve().parent

if not os.environ.get('XDG_DATA_HOME'):
    os.environ['XDG_DATA_HOME'] = os.path.expanduser('~/.local/share')
print("Installing data files to:", os.environ['XDG_DATA_HOME'])

#export XDG_UTILS_DEBUG_LEVEL=1  #DEBUG

print('Installing mimetype data...')
file = wd/'application-x-plt.xml'
print(file, ':' ,file.is_file())
run(['xdg-mime', 'install', str(file)], check=True)


print('Installing desktop file...')
apps_dir = os.path.join(os.environ['XDG_DATA_HOME'], "applications/")
with (wd/'plotter.desktop').open('r', encoding='utf-8') as f:
    desktop_contents = f.read().format(PYTHON=sys.executable)
with Path(apps_dir, 'plotter.desktop').open('w', encoding='utf-8') as f:
    f.write(desktop_contents)
run(['update-desktop-database', apps_dir], check=True)

