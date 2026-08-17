![logo banner](white_logo.png)

# Janus Blog Maker

A Python utility that generates a full HTML + CSS blog with multiple boards of posts from a simpler structure based on MD files.

> **DISCLAIMER:** Janus has only been successfully tested on Linux, but it could also work on macOS.

# Prerequisites for using Janus

- A Python >3.10 interpreter
- A text editor
- Being able to run commands in a terminal shell
- Knowing Markdown syntax
- Knowing HTML (fully optional, only needed to edit the templates)
- Knowing CSS (fully optional, the example already provides default stylesheets)

# Installation

```commandline
git clone https://github.com/RubenSab/JanusBlogMaker
cd JanusBlogMaker
pip install -e .
```

# Usage

```commandline
usage: janusBM [-h] [-i INPUT] [-o OUTPUT] [-v]

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

# How Janus works

The HTML blog is built through a "conversion" of a simpler version of it written in Markdown.

Regardless of the input directory structure, blogs made with Janus have an index page that links to boards.
Boards are user defined collections of posts covering the same topic.

After writing a post and choosing its board(s), the program handles the linking of each board cited to the post's preview automatically.

Each post can be put in different boards, this is because boards are not directories; instead each post specifies the boards it belongs to  in its properties.

MD files alone cannot be converted into a blog, so a context/ folder with stylesheets, templates and aliases is needed to make the conversion more customizable.

> **NOTE:** to update the output directory with changes made in the input one, run the aforementioned command `janusBM -i input_dir -o output_dir`

> **NOTE:** the docs below are useful, but I suggest to read the example directory first if you want to gain an intuition of the blog's format. It's simpler than it looks.

# Blog structure

## Structure of the input file tree

```
index.md (or index.html) (mandatory, if there's an index.html it gets copied in the output tree)

boards/ (see the specifications below)
    board_name_1.md (optional)
    board_name_2.md (optional)
    ...
    board_name_n.md (optional)

context/
    aliases.txt (mandatory, see the specifications below)
    stylesheets/
        implicit.css (mandatory, it's the common stylesheet that doesn't need to be specified in post properties)
        style_name_1.css (optional)
        style_name_2.css (optional)
        ...
        style_name_n.css (optional)
    templates/ (see the specifications below)
        board.html (mandatory, it defines the structure of boards)
        overview.html (mandatory, it defines the structure of post previews in boards)
        post.html (mandatory, it defines the structure of posts)

not_translated/
    md_name_1.md (optional)
    md_name_2.md (optional)
    ...
    md_name_n.md (optional)

posts/ (see the specifications below)
    irrelevant_name_that_wont_appear_anywhere_1/
        thumbnail_name.jpg (or any other image format) (optional)
        post_name.md (mandatory)
    irrelevant_name_that_wont_appear_anywhere_2/
        thumbnail_name.jpg (optional)
        post_name.md (mandatory)
    ...
    irrelevant_name_that_wont_appear_anywhere_n/
        thumbnail_name.jpg (optional)
        post_name.md (mandatory)
```

## Structure of the output file tree

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
    irrelevant_name_that_wont_appear_anywhere_1/
        thumbnail_name.jpg
        post_name.html
    irrelevant_name_that_wont_appear_anywhere_2/
        thumbnail_name.jpg
        post_name.html
    ...
    irrelevant_name_that_wont_appear_anywhere_n/
        thumbnail_name.jpg
        post_name.html
```

## File specifications

### Posts

Posts are structured as follows:

- post properties (all are optional)
- a newline
- a --- divider
- another newline
- post content in Markdown syntax

```md
title: (title here)
thumbnail: (thumbnail filename, relative to this post's file)
created: (date here, DD-MM-YYYY format)
boards: (board names here, separated by comma)
css: (stylesheet names here, separated by comma)

---

(content here)
```

> **NOTE**: posts can use the aliases in aliases.txt. For more context read the post examples.

### Boards

Boards are structured like posts, but with fewer properties.

```md
title: (title here)
css: (stylesheet names here, separated by comma)

---

(content here)
```

> **NOTE**: boards can use aliases too.

### aliases.txt

aliases.txt is a file in context/ dir, where each line has a keyword to replace, a colon and the HTML string that will replace the keyword. 
To write multiline aliases, separate each line in the HTML string with a \n.

Examples:

```
[GALLERY]: <div class=\"gallery\">
[END DIV]: </div>
```

> **NOTE**: HTML strings can include dynamically resolved post properties between curly brackets. More documentation on the subject will come.

```
[BACK TO BOARD]: <a href="../../boards/{FIRST_BOARD}.html" class="back-link">Back to {FIRST_BOARD}</a>
```

### Templates

Templates are three HTML files inside context/templates:

- board.html defines the structure of boards,
- overview.html defines the structure of post previews in boards,
- post.html defines the structure of posts.

They are written in standard HTML syntax with the addition of aliases and post/board properties to resolve.