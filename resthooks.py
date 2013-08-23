from flask import Flask, Markup, Response
from flask import request, send_from_directory, render_template
from flask_flatpages import pygments_style_defs
app = Flask(__name__)
app.config.from_pyfile('config.py')

from flask_flatpages import FlatPages
pages = FlatPages(app)

import misaka
import operator
import random
import simplejson
import os
import re
import uuid
import fileinput
import requests
import sys
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
    return posts(page=1)

@app.route('/<int:page>/')
def page(page):
    return posts(page)

def posts(page=1, render=True):
    """
    Return a rendered template for a bunch of posts given a page offset
    """
    # live posts are pages with a draft=false or draft not set, always needs a date
    posts = (p for p in pages if ('date' in p.meta and ('draft' in p.meta and p.meta['draft'] == False) or ('draft' not in p.meta)))

    # show the 6 most recent articles, most recent first.
    latest = sorted(posts, reverse=True,
                    key=lambda p: p.meta['date'])

    # grab only the posts we want
    paginate = POSTS_PER_PAGE
    start = ((page-1)*paginate)
    end = start+paginate
    posts = latest[start:end]

    # set more and less page numbers where applicable
    prev = next = None

    if start > 0:
        next = page-1

    if len(latest) > end:
        prev = page+1

    # build captions
    for post in posts:
        post.caption = smart_truncate(render_markdown(post.body).striptags(), 120, '')

    if render:
        return render_template('index.html', posts=posts, prev=prev, next=next, **GLOBAL_CONTEXT)
    else:
        return {
            'posts': posts,
            'prev': prev,
            'next': next
        }

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
        md = render_markdown(p.body)
        post = {
            'content': md,
            'meta': p.meta,
            'path': p.path,
            'caption': smart_truncate(md.striptags(), 120, '...'),
        }
    else:
        post = None
    return render_template('index.html', post=post, **GLOBAL_CONTEXT)

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