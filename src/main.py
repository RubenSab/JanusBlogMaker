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
    janus = BlogBuilder(input, output)
    janus.translate_blog()

def cli():
    """
    CLI entry point
    """
    plac.call(main)

if __name__ == '__main__':
    cli()
