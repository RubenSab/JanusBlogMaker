import json
import shutil
import tomllib
from pathlib import Path
from typing import Set

from src import utils
from src.Documents.Board import Board
from src.Documents.Post import Post, Dict


def recursive_visit(path: Path, MD_not_to_convert: Set[Path], template: str, aliases: Dict[str, str]) -> None:
    # if the file is a directory create a mirrored directory in the output file tree
    if path.is_dir():
        utils.remove_old_recursive_and_mkdir(
            utils.mirrored_abspath(path, input_root_abspath, output_root_abspath)
        )
        for child in path.iterdir():
            recursive_visit(child, MD_not_to_convert, template, aliases)

    # if the file is a MD post not to ignore, convert its content and mirror it
    elif path.is_file() and path.suffix.lower() == '.md' and path not in MD_not_to_convert:
        current_post = Post(path.read_text(), path)
        utils.mirrored_abspath(path, input_root_abspath, output_root_abspath).write_text(
            current_post.write(template, aliases)
        )

    # else mirror the file in the output tree
    else:
        shutil.copy(path, utils.mirrored_abspath(path, input_root_abspath, output_root_abspath))


if "__main__" == __name__:
    # load input root directory abspath and output root directory abspath
    with open(Path.cwd() / "input_output_paths.toml", "rb") as f:
        paths = tomllib.load(f)
    input_root_abspath = Path(paths["md_input_root"])
    output_root_abspath = Path(paths["html_output_root"])
    if not output_root_abspath.is_dir():
        output_root_abspath.mkdir()

    # load aliases
    with open(input_root_abspath / "aliases.json", "r") as f:
        aliases_dict = json.loads(f.read())

    # load MD files not to be converted
    with open(input_root_abspath / "md_no_convert.txt", "r") as f:
        MD_not_to_convert = set([Path(line.strip()) for line in f.read().splitlines()])

    # load HTML templates
    board_template = Path(input_root_abspath / "templates" / "board.html").read_text()
    post_template = Path(input_root_abspath / "templates" / "post.html").read_text()
    postlet_template = Path(input_root_abspath / "templates" / "postlet.html").read_text()

    # create empty Board objects
    boards = []
    for board_path in Path(input_root_abspath / "boards").iterdir():
        boards.append(Board(board_path.read_text(), board_path))

    # convert index.md into index.html, or mirror it if it's already .html
    index_md_abspath = input_root_abspath / "index.md"
    index_html_abspath = input_root_abspath / "index.html"
    if Path(index_md_abspath).is_file():
        utils.mirrored_abspath(
            index_md_abspath, input_root_abspath, output_root_abspath
        ).write_text(
            utils.convert_aliased_md_to_html(
                index_md_abspath.read_text(),
                aliases_dict,
                Post(index_md_abspath.read_text(), index_md_abspath)
            )
        )
    elif Path(index_html_abspath).is_file():
        output_path = utils.mirrored_abspath(
            index_html_abspath,
            input_root_abspath,
            output_root_abspath
        )
        utils.remove_old_recursive_and_copy(index_html_abspath, output_path)

    # mirror stylesheets
    utils.remove_old_recursive_and_copy_recursive(
        input_root_abspath / "stylesheets",
        output_root_abspath / "stylesheets"
    )

    # visit content recursively
    recursive_visit(Path(input_root_abspath / "content"), MD_not_to_convert, post_template, aliases_dict)

    # for each Board compute its content and mirror it
    utils.remove_recursive(Path(output_root_abspath / "boards"))
    Path(output_root_abspath / "boards").mkdir()
    for board in boards:
        output_path = utils.mirrored_abspath(
            board.path, input_root_abspath, output_root_abspath
        )
        output_path.write_text(board.write(board_template, aliases_dict))