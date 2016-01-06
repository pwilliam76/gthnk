#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, '.')

import flask
import gthnk
from gthnk.librarian import Librarian


def main():
    app = flask.Flask(__name__)
    app.config.from_envvar('SETTINGS')
    gthnk.db.init_app(app)
    with app.app_context():
        librarian = Librarian(app)
        librarian.export_journal()

if __name__ == "__main__":
    main()