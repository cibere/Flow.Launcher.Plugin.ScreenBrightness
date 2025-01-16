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

from flogin.utils import print, setup_logging

setup_logging()

# Detect 'ImportError: DLL load failed while importing win32event: The specified module could not be found. '
# and automatically reinstall if found

try:
    import pywintypes
except ImportError:
    import subprocess

    libs = (
        os.path.join("venv", "lib", "site-packages")
        if os.path.exists("venv")
        else "lib"
    )

    subprocess.run(
        [
            sys.executable,
            "-m",
            "pip",
            "install",
            "--force-reinstall",
            "-U",
            "pywin32",
            "-t",
            libs,
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    print(f"Installed pywin32 at {libs!r}")


from plugin.plugin import ScreenBrightnessPlugin

if __name__ == "__main__":
    ScreenBrightnessPlugin().run()
