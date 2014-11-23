# (c) 2013 www.turkr.com

import json, datetime
from flask.ext.admin import expose
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.security import current_user
from Gthnk import Models, security
from flask.ext.diamond.administration import AuthModelView, AuthView, AdminIndexView
from Gthnk.Models.Day import latest

import flask

class ListExplorer(AuthView):
    def is_accessible(self):
        return current_user.is_authenticated()

    def is_visible(self):
        return False

    @expose('/')
    def index_view(self):
        return flask.redirect(flask.url_for('admin.index'))

    @expose("/items")
    def items_view(self):
        name_str = flask.request.args['name']
        if name_str is None:
            return flask.redirect(flask.url_for('admin.index'))

        item_list = Models.ItemList.find(name=name_str)
        if item_list:
            return self.render('itemlist_explorer/itemlist_view.html', item_list=item_list)
        else:
            return flask.redirect(flask.url_for('admin.index'))
