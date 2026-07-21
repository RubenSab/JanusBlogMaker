![logo banner](white_logo.png)

# Janus Blog Maker

A Python utility that generates a full HTML + CSS blog with multiple boards of posts from a simpler structure based on MD files.

# Installation

```commandline
git clone https://github.com/RubenSab/JanusBlogMaker
cd JanusBlogMaker
pip install -e .
janus -i /home/ruben/JanusBlogMaker/blog/input -o /home/ruben/JanusBlogMaker/blog/output
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
janus -i /home/ruben/JanusBlogMaker/blog/input -o /home/ruben/JanusBlogMaker/blog/output
```