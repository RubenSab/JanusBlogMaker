import shutil
from pathlib import Path
from typing import Dict

import markdown

from src.Documents.MDDocument import MDDocument


def mirrored_abspath(abspath: Path, input_dir_abspath: Path, output_dir_abspath: Path) -> Path:
    relpath = abspath.relative_to(input_dir_abspath)
    new_path = output_dir_abspath / relpath
    if new_path.suffix.lower() == '.md':
        new_path = new_path.with_suffix('.html')
    return new_path


def convert_aliased_md_to_html(md: str, aliases: Dict[str, str], invoked_obj) -> str:
    return replace_aliases_in_html(markdown.markdown(md), aliases, invoked_obj)


def replace_aliases_in_html(source_text: str, aliases: Dict[str, str], invoked_obj: MDDocument) -> str:
    return "test" # stub


def remove_recursive(path: Path) -> None:
    if path.is_dir():
        shutil.rmtree(path)

def remove_old_recursive_and_copy_recursive(src: Path, dest: Path) -> None:
    remove_recursive(dest)
    shutil.copytree(src, dest)

def remove_old_recursive_and_mkdir(dest: Path) -> None:
    remove_recursive(dest)
    dest.mkdir()