import sys
from pathlib import Path

root = Path(__file__).parent
sys.path.extend(
    [
        path.as_posix()
        for path in (
            root,
            root / "plugin",
            root / "lib",
            root / "lib" / "win32",
            root / "lib" / "win32" / "lib",
        )
    ]
)

from flogin.utils import setup_logging
from flogin import Pip

setup_logging()

with Pip() as pip:
    pip.ensure_installed("pywin32", module="pywintypes")

from plugin.plugin import ScreenBrightnessPlugin

if __name__ == "__main__":
    ScreenBrightnessPlugin().run()
