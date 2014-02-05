#!/usr/bin/env python
# -*- coding: utf-8 -


from flask import Flask
from flask import render_template
from flask.ext.assets import Environment, Bundle
from flask import redirect


app = Flask(__name__)


# app.config.from_pyfile(flask-config.cfg) -- import Config
assets = Environment(app)
css = Bundle('cardui.css', ' normalize.css',
             'semantic.min.css', 'pace.css', 'style.css')
js = Bundle(
    'semantic.min.js', 'jquery.min.js', 'pace.min.js')

assets.register('css', css)
assets.register('js', js)


@app.errorhandler(404)
def page_not_found(e):
        # return render_template('modal.html'), 404
        return "This developer is too lazy to write a 404 :D", 404


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=80, debug=True, host='0.0.0.0')
    # This can be omitted if using gevent wrapped around gunicorn
