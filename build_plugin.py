import sys
import zipfile
from pathlib import Path


def main(archive_name: str):
    files = [
        Path(fp)
        for fp in (
            "plugin.json",
            "main.py",
            "assets/app.png",
            "assets/error.png",
        )
    ]

    plugin_dir = Path("plugin")
    files.extend(plugin_dir.rglob(f"*.py"))

    lib_dir = Path("lib")
    files.extend(lib_dir.rglob("*"))

    with zipfile.ZipFile(archive_name, "w") as f:
        for file in files:
            f.write(file)
            print(f"Added {file}")
    print(f"\nDone. Archive saved to {archive_name}")


if __name__ == "__main__":
    main(sys.argv[-1])
