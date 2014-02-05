#!/usr/bin/env python
# -*- coding: utf-8 -

# remove UI segemnts
# fix grids
# layouts
# files

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
	return make_response(jsonify({"Error 404":
                                  "Bad request Lazy devloper"}), 404)


@app.errorhandler(400)
def bad_request(e):
    return make_response(jsonify({"Error 400":
                                  "Bad request"}), 400)


@app.errorhandler(500)
def internal_error(e):
    return make_response(jsonify({"Error 500":
                                  "Internal Server Error"}), 500)


@app.errorhandler(405)
def invalidMethod(e):
    return make_response(jsonify({"Error 405":
                                  "Invalid Request Method"}), 405)


@app.errorhandler(410)
def gone(e):
    return make_response(jsonify({"Error 410":
                                  "Resource is Gone"}), 410)



@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')
    # This can be omitted if using gevent wrapped around gunicorn
