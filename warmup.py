import pathlib
import shutil
import zipfile


def extract_txt(zip_filename, dst_dir):
    """Extract all txt files from a zip."""
    with zipfile.ZipFile(zip_filename) as zip_src:
        names = [
            name for name in zip_src.namelist()
            if pathlib.Path(name).suffix == ".txt"
        ]
        for member in names:
            dst_path = pathlib.Path(dst_dir) / pathlib.Path(member).name
            with zip_src.open(member) as src, open(dst_path, "wb") as dst:
                shutil.copyfileobj(src, dst)