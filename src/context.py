import os
from pathlib import Path

class Context:
    def __init__(self, input_root: Path, output_root: Path):
        self.input_root = input_root
        self.output_root = output_root
        self.aliases_dict = {}
        self.templates = {}

    def map_stylename_to_css_path(self, stylename: str, dir_name: str):
        css = self.input_root / 'context' / 'stylesheets' / (stylename + '.css')
        return os.path.relpath(css, self.input_root / 'posts' / dir_name) # TODO use pathlib

    def init_aliases_dict(self):
        with open(self.input_root / 'context' / 'aliases.txt') as file:
            lines = file.readlines()
            for line in lines:
                if not line.strip():
                    continue
                alias, translation = line.strip().split(':', 1)
                self.aliases_dict[alias.strip()] = translation.strip()

    def init_templates(self):
        templates_dir = self.input_root / 'context' / 'templates'
        for template_name in ['post', 'board', 'overview']:
            with open(templates_dir / f'{template_name}.html', 'r') as f:
                self.templates[template_name] = f.read()