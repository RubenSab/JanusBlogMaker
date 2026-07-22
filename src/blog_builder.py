import shutil
from pathlib import Path

from board import Board
from context import Context
from post import Post


class BlogBuilder:
    def __init__(self, input_root: Path, output_root: Path):
        self.input_root = Path(input_root).absolute()
        self.output_root = Path(output_root).absolute()

    def translate_blog(self):
        # init Context
        context = Context(self.input_root, self.output_root)
        context.init_aliases_dict()
        context.init_templates()
        # get board names from their filenames
        boards = {
            board_path.stem : Board(board_path.stem)
            for board_path in (self.input_root / 'boards').iterdir()
        }
        # build the output/ tree
        Path(self.output_root).mkdir(parents=True, exist_ok=True)
        if (Path(self.input_root) / 'index.html').is_file():
            shutil.copy(self.input_root / 'index.html', self.output_root / 'index.html')
        else:
            with open(self.input_root / 'index.md', 'r', encoding='utf-8') as f:
                index = Post(f.read(), self.input_root, 'index', context)
                index.extract_properties()
                html = index.get_html()
            with open(self.output_root / 'index.html', 'w', encoding='utf-8') as f:
                f.write(html)

        shutil.copytree(
            self.input_root / 'context' / 'stylesheets',
            self.output_root / 'context' / 'stylesheets',
            dirs_exist_ok=True
        )
        shutil.copytree(
            self.input_root / 'not_translated',
            self.output_root / 'not_translated',
            dirs_exist_ok=True
        )
        (self.output_root / 'boards').mkdir(parents=True, exist_ok=True)
        (self.output_root / 'posts').mkdir(parents=True, exist_ok=True)
        # for each post directory, translate .md files and copy non .md files
        for post_dir in (self.input_root / 'posts').iterdir():
            if post_dir.is_dir():
                (self.output_root / 'posts' / post_dir.name).mkdir(parents=True, exist_ok=True)
                for post_file in post_dir.iterdir():
                    if post_file.suffix == '.md':
                        with open(self.input_root / 'posts' / post_dir.name / post_file.name, 'r', encoding='utf-8') as f:
                            post = Post(f.read(), post_dir.name, post_file.name, context)
                            post.extract_properties()
                            if post.get_board_names():
                                for board_name in post.get_board_names():
                                    boards[board_name].add_post(post)
                        with open(self.output_root / 'posts' / post_dir.name / (post_file.stem + '.html'), 'w', encoding='utf-8') as f:
                            f.write(post.get_html())
                    else:
                        src = post_dir / post_file
                        dst = self.output_root / 'posts' / post_dir.name / post_file.name

                        if src.is_dir():
                            shutil.copytree(src, dst, dirs_exist_ok=True)
                        elif src.is_file():
                            shutil.copy(src, dst)
                        else:
                            dst.parent.mkdir(parents=True, exist_ok=True)
                            shutil.copy2(src, dst)
            else:
                shutil.copy(post_dir, self.output_root / post_dir.name)
        # for each board file, translate it
        for file in (self.input_root / 'boards').iterdir():
            if file.suffix == '.md':
                board = boards[file.stem]
                with open(self.input_root / 'boards' / file, 'r', encoding='utf-8') as f:
                    post = Post(f.read(), self.input_root / 'boards', file, context)
                    board.init_board_post(post)
                    html = board.get_html()
                with open(self.output_root / 'boards' / (file.stem + '.html'), 'w', encoding='utf-8') as f:
                    f.write(html)
            elif file.is_dir():
                shutil.copytree(file, self.output_root / 'boards' / file.name, dirs_exist_ok=True)
            else:
                shutil.copy(file, self.output_root / 'boards' / file.name)