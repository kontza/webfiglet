import collections
import os

import pyfiglet
from flask import Flask, render_template


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route("/")
    @app.route("/<text_to_render>")
    def hello(text_to_render=None):
        empty_font = pyfiglet.Figlet()
        fonts = collections.OrderedDict()
        for font in sorted(empty_font.getFonts()):
            f = pyfiglet.Figlet(font=font, width=200)
            if text_to_render:
                payload = f.renderText(text_to_render)
            else:
                payload = f.renderText(font)
            rows = payload.splitlines()
            cols = 0
            for row in rows:
                if len(row) > cols:
                    cols = len(row)
            fonts[font] = {"lines": 1 + len(rows), "cols": cols, "payload": payload}
        return render_template("fonts.html", fonts=fonts)

    return app
