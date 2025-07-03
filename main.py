from flogin.utils import setup_logging
from flogin import Pip

setup_logging()

with Pip() as pip:
    pip.ensure_installed("pywin32", module="pywintypes")

from screen_brightness.plugin import ScreenBrightnessPlugin

if __name__ == "__main__":
    ScreenBrightnessPlugin().run()
