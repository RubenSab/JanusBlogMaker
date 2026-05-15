import shutil
from pathlib import Path
from typing import Dict

from src.Documents.MDDocument import MDDocument


def mirrored_abspath(abspath: Path, input_dir_abspath: Path, output_dir_abspath: Path) -> Path:
    relpath = abspath.relative_to(input_dir_abspath)
    new_path = output_dir_abspath / relpath
    if new_path.suffix.lower() == '.md':
        new_path = new_path.with_suffix('.html')
    return new_path


def convert_aliased_md_to_html(md: str, aliases_dict: Dict[str, str]) -> str:
    return md # stub


def replace_aliases(source_text: str, aliases: Dict[str, str], invoked_obj: MDDocument) -> str:
    pass


def remove_recursive(path: Path) -> None:
    if path.is_dir():
        shutil.rmtree(path)

def remove_and_copy_recursive(src: Path, dest: Path) -> Path:
    remove_recursive(dest)
    shutil.copytree(src, dest)
    return dest

def remove_and_copy(src: Path, dest: Path) -> Path:
    remove_recursive(dest)
    shutil.copy(src, dest)
    return dest