from pathlib import Path
from typing import Dict


class MDDocument:
    def __init__(self, md_text: str, path: Path):
        self.md_text: str = md_text
        self.path: Path = path


    def write(self, template: str, aliases: Dict[str, str]) -> str:
        pass

