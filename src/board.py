from post import Post


class Board:
    def __init__(self, name):
        self.name = name
        self.board_post = None
        self.posts = []

    def add_post(self, post: Post):
        self.posts.append(post)

    def init_board_post(self, post: Post):
        post.extract_properties()
        self.board_post = post

    def get_html(self):
        static_html = self.board_post.get_html('board')
        overview_htmls = [
            post.get_html('overview', True)
            for post in self.posts
        ]
        return static_html.replace('{OVERVIEWS}', '\n'.join(overview_htmls))