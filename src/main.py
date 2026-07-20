# Copia ricorsivamente context e not_translated nell'output
# Crea le directory content, content/posts e content/boards nell'output
# Per ogni directory in posts, traduci il post da md a html, passando al nuovo Post la directory in cui è contenuto.
# Per ogni directory in boards, traduci la board da md a html, passando alla nuova Board la directory in cui è contenuto.
from src.blog_builder import BlogBuilder

janus = BlogBuilder('/home/ruben/JanusBlogMaker/blog/input', '/home/ruben/JanusBlogMaker/blog/output')
janus.translate_blog()