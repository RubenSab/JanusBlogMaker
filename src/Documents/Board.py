from typing import Dict, List
from pathlib import Path

from src.Documents.MDDocument import MDDocument
from src.Documents.Post import Post


class Board(MDDocument):
    def __init__(self, md_text: str, path: Path):
        super().__init__(md_text, path)
        self.posts: List[Post] = []


    def write(self, template: str, aliases: Dict[str, str]) -> str:
        pass