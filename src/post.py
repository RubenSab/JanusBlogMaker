from pathlib import Path

import markdown
from context import Context


class Post:
    def __init__(self, md_text: str, dir_name: str|Path, post_name: str|Path, context: Context):
        self.context = context
        self.md_text = md_text
        self.md_body = None
        self.dir_name = dir_name
        self.post_name = str(post_name).split('.', 1)[0] # TODO check
        self.properties = { # inputted properties
            'title': None,
            'created': None,
            'modified': None,
            'thumbnail': None,
            'css': ['implicit'],
            'boards': [],
        }

    def extract_properties(self):
        for i, line in enumerate(self.md_text.splitlines()):
            if line.strip() == '---':
                self.md_body = '\n'.join(self.md_text.splitlines()[i + 1:])
                break
            if not line or ':' not in line:
                continue
            prop, value = line.split(':', 1)
            prop = prop.strip()
            value = value.strip()
            if prop == 'css':
                self.properties['css'].extend([v.strip() for v in value.split(',')])
            elif prop == 'boards':
                self.properties['boards'].extend([v.strip() for v in value.split(',')])
            else:
                self.properties[prop] = value

    def get_board_names(self):
        return self.properties['boards']

    def get_html(self, template_name = 'post', called_from_board = False):
        full_html = self.context.templates[template_name]
        # convert MD content to HTML
        aliased_md_body = self.convert(self.md_body)
        for alias in self.context.aliases_dict:
            aliased_md_body = aliased_md_body.replace(alias, self.context.aliases_dict[alias])
        full_html = full_html.replace('{BODY}', aliased_md_body)
        for alias in self.context.aliases_dict:
            full_html = full_html.replace(alias, self.context.aliases_dict[alias])
        full_html = full_html.replace("\\n<", "\n<")  # necessary, see line 74
        # translate every {self.property} found to its value
        if self.properties['boards']:
            full_html = full_html.replace('{FIRST_BOARD}', self.properties['boards'][0])
        else:
            full_html = '\n'.join([
                line for line in full_html.split('\n')
                if '{FIRST_BOARD}' not in line
            ])
        full_html = full_html.replace(
            '{POST PATH}',
            '../' + str(Path('posts') / self.dir_name / self.post_name) + '.html'
        ) # TODO clean
        if self.properties['thumbnail'] is not None and called_from_board:
            full_html = full_html.replace(
                '{THUMBNAIL}',
                str(Path('..') / 'posts' / self.dir_name / self.properties['thumbnail'])
            )  # TODO clean
        for prop, value in self.properties.items():
            if value is not None and prop != 'css' \
                    and (isinstance(value, str) or isinstance(value, Path)):
                full_html = full_html.replace(f'{{{prop.upper()}}}', str(value))
            elif value is None:  # if the value of {self.property} is None, the whole line gets deleted
                lines = full_html.split('\n')
                lines = [line for line in lines if f'{{{prop.upper()}}}' not in line]
                full_html = '\n'.join(lines)
        if '{CSS}' in full_html:
            full_html = full_html.replace(
                '{CSS}',
                '\n'.join([
                    f'<link rel="stylesheet" href="{self.context.map_stylename_to_css_path(css, self.dir_name)}" type="text/css">'
                    for css in self.properties['css']
                ])
            )
        full_html = full_html.replace('\\"', '"') # TODO clean
        full_html = full_html.replace("\\n<", "\n<") # to convert \n in newline
        full_html = full_html.replace("\\t<", "\t<") # to convert \n in newline
        return full_html

    def convert(self, md: str):
        return markdown.markdown(md, extensions=['attr_list', 'fenced_code'])