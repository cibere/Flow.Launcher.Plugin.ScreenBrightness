import sys
import zipfile
from pathlib import Path


def main(archive_name: str):
    prod_file = Path("DELETE-ME-FOR-DEBUG-LOGS.flogin.prod")
    if not prod_file.exists():
        prod_file.write_text("")

    files = [
        Path(fp)
        for fp in (
            "plugin.json",
            "main.py",
            "assets/app.png",
            "assets/error.png",
            prod_file.name,
        )
    ]

    plugin_dir = Path("plugin")
    files.extend(plugin_dir.rglob("*.py"))

    lib_dir = Path("lib")
    files.extend(lib_dir.rglob("*"))

    with zipfile.ZipFile(archive_name, "w") as f:
        for file in files:
            f.write(file)
            print(f"Added {file}")
    print(f"\nDone. Archive saved to {archive_name}")


if __name__ == "__main__":
    if (archive_name := sys.argv[-1].strip()) == "build_plugin.py":
        raise RuntimeError("Give a filename")

    main(archive_name)
