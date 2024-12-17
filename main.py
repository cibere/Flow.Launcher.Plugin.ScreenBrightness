import os
import sys

parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, "lib"))
sys.path.append(os.path.join(parent_folder_path, "venv", "lib", "site-packages"))
sys.path.append(
    os.path.join(parent_folder_path, "venv", "lib", "site-packages", "win32", "lib")
)
sys.path.append(
    os.path.join(parent_folder_path, "venv", "lib", "site-packages", "win32")
)
sys.path.append(os.path.join(parent_folder_path, "lib", "win32", "lib"))
sys.path.append(os.path.join(parent_folder_path, "lib", "win32"))

from plugin.plugin import ScreenBrightnessPlugin

if __name__ == "__main__":
    ScreenBrightnessPlugin().run()
