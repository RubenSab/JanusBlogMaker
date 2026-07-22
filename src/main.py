import sys
from pathlib import Path

from blog_builder import BlogBuilder

import plac

@plac.opt('input', help="input root directory", type=str, abbrev='i')
@plac.opt('output', help="output root directory", type=str, abbrev='o')
@plac.flg('verbose', help="verbose mode", abbrev='v')
def main(input: str, output: str, verbose=False):
    """
    Janus Blog Maker
    :param input: input root directory
    :param output: output root directory
    :param verbose: verbose mode
    """
    if not input:
        print("Error: input root directory is required (-i/--input)", file=sys.stderr)
        print(main.__doc__ if main.__doc__ else "Usage: ...")
        sys.exit(1)
    if not output:
        print("Error: output root is required (-o/--output)", file=sys.stderr)
        print(main.__doc__ if main.__doc__ else "Usage: ...")
        sys.exit(1)
    if not Path.is_dir(input):
        print(f"Error: Input directory '{input}' does not exist", file=sys.stderr)
        sys.exit(1)
    janus = BlogBuilder(input, output)
    janus.translate_blog()

def cli():
    """
    CLI entry point
    """
    plac.call(main)

if __name__ == '__main__':
    cli()
