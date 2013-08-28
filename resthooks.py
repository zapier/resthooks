from flask import Flask, Markup
from flask import request, send_from_directory, render_template, render_template_string
app = Flask(__name__)
app.config.from_pyfile('config.py')

from flask_flatpages import FlatPages
pages = FlatPages(app)

import misaka
import operator
import os
import houdini
import datetime

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

ROOT = os.path.dirname(os.path.realpath(__file__))
STATIC_URL = app.config['STATIC_URL']
POSTS_PER_PAGE = app.config['POSTS_PER_PAGE']
FLATPAGES_EXTENSION = app.config['FLATPAGES_EXTENSION']
DEBUG = app.config['DEBUG']

GLOBAL_CONTEXT = {
    'STATIC_URL': STATIC_URL,
    'now': datetime.datetime.now()
}

@app.route('/')
def index():
    return render_template('index.html', **GLOBAL_CONTEXT)

@app.route('/static/<path:filename>')
def static(filename):
    return send_from_directory(ROOT + app.config['STATIC_URL'], filename)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(ROOT + app.config['STATIC_URL'], 'favicon.ico')

@app.route('/<slug>/')
def post(slug):
    """
    Render a single post to the screen by slug `post` or 404
    """
    p = pages.get(slug)
    if p:
        md = render_markdown(render_template_string(p.body, **GLOBAL_CONTEXT))
        post = {
            'content': md,
            'meta': p.meta,
            'path': p.path,
            'caption': smart_truncate(md.striptags(), 120, '...'),
        }
        return render_template('post.html', post=post, **GLOBAL_CONTEXT)
    else:
        return render_template('404.html', **GLOBAL_CONTEXT)

@app.route('/static/css/pygments.css')
def pygments_css():
    style = HtmlFormatter(style='monokai').get_style_defs('div.highlight')
    if DEBUG:
        with open('static/css/pygments.css', 'w') as f:
            f.write(style)
    return style, 200, {'Content-Type': 'text/css'}

def smart_truncate(content, length=100, suffix='...'):
    if len(content) <= length:
        return content
    else:
        return ' '.join(content[:length+1].split(' ')[0:-1]) + suffix

def render_markdown(md):
    class CustomRenderer(misaka.HtmlRenderer, misaka.SmartyPants):
        def block_code(self, text, lang):
            if not lang:
                return '\n<pre><code>%s</code></pre>\n' % \
                    houdini.escape_html(text.strip())
            lexer = get_lexer_by_name(lang, stripall=True)
            formatter = HtmlFormatter()
            return highlight(text, lexer, formatter)

    markdown = misaka.Markdown(
        renderer=CustomRenderer(),
        extensions=reduce(operator.or_, [misaka.EXT_FENCED_CODE,
                                         misaka.EXT_STRIKETHROUGH,
                                         misaka.EXT_NO_INTRA_EMPHASIS,
                                         misaka.EXT_TABLES,
                                         misaka.EXT_AUTOLINK,
                                         misaka.EXT_SPACE_HEADERS]))
    return Markup(markdown.render(md))

if __name__ == "__main__":
    app.run(threaded=True)
