from pathlib import Path
from typing import Dict

from src.Documents.MDDocument import MDDocument


class Post(MDDocument):
    def __init__(self, md_text: str, path: Path):
        super().__init__(md_text, path)
        self.properties: Dict[str, str|None] = {
            'title': None,
            'thumbnail': None,
            'created': None,
            'modified': None,
            'css': None,
            'summary': None
        }


    def write(self, template: str, aliases: Dict[str, str]) -> str:
        return template # stub


    def writePostlet(self, template: str) -> str:
        pass


    def _addToBoard(self, board_name: str):
        pass