![logo banner](white_logo.png)

# Janus Blog Maker

A Python utility that generates a full HTML + CSS blog with multiple boards of posts from a simpler structure based on MD files.

# Installation

```commandline
git clone https://github.com/RubenSab/JanusBlogMaker
cd JanusBlogMaker
pip install -e .
```

# Usage

```commandline
usage: janus [-h] [-i INPUT] [-o OUTPUT] [-v]

Janus Blog Maker
:param input: input root directory
:param output: output root directory
:param verbose: verbose mode

options:
  -h, --help           show this help message and exit
  -i, --input INPUT    input root directory
  -o, --output OUTPUT  output root directory
  -v, --verbose        verbose mode
```

Example

```commandline
janusBM -i blog_example/input -o blog_example/output
```

# Structure of the input file tree

```
index.md (or index.html) (mandatory)

boards/
    board_name_1.md (optional)
    board_name_2.md (optional)
    ...
    board_name_n.md (optional)

context/
    aliases.txt (mandatory)
    stylesheets/
        implicit.css (mandatory, it's the common stylesheet that doesn't need to be specified in post properties)
        style_name_1.css (optional)
        style_name_2.css (optional)
        ...
        style_name_n.css (optional)
    templates/
        board.html (mandatory, defines the structure of boards)
        overview.html (mandatory, defines the structure of post overviews in boards)
        post.html (mandatory, defines the structure of posts)

not_translated/
    md_name_1.md (optional)
    md_name_2.md (optional)
    ...
    md_name_n.md (optional)

posts/
    irrelevant_name_1/
        thumbnail_name.jpg (or any other image format) (optional)
        post_name.md (mandatory)
    irrelevant_name_2/
        thumbnail_name.jpg (optional)
        post_name.md (mandatory)
    ...
    irrelevant_name_n/
        thumbnail_name.jpg (optional)
        post_name.md (mandatory)
```

# Structure of the output file tree

```
index.html

boards/
    board_name_1.html
    board_name_2.html
    ...
    board_name_n.html

context/
    stylesheets/
        implicit.css
        style_name_1.css
        style_name_2.css
        ...
        style_name_n.css

not_translated/
    md_name_1.md
    md_name_2.md
    ...
    md_name_n.md

posts/
    irrelevant_name_1/
        thumbnail_name.jpg
        post_name.html
    irrelevant_name_2/
        thumbnail_name.jpg
        post_name.html
    ...
    irrelevant_name_n/
        thumbnail_name.jpg
        post_name.html
```

# File specifications

## Posts

## Boards

## aliases.txt

## Templates