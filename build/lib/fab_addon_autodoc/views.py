from flask import render_template, request
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView
from .models import *
from flask_appbuilder.baseviews import BaseView, expose
from flask.globals import _app_ctx_stack, current_app
from jinja2.exceptions import TemplateNotFound
import logging
from jinja2._compat import string_types
from flask.blueprints import Blueprint


"""
    Create your Views (but don't register them here, do it on the manager::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


"""


log = logging.getLogger(__name__)

class DocumentsView(BaseView):

    route_base = '/addon/autodoc'
    template_folder = 'templates'
    static_folder = 'static/addon/autodoc'

    @expose('/list')
    @expose('/list/<group>')
    def list(self, group=None):
        if not group:
            group = 'all'
        return self.render_template('addon/autodoc/fab_autodoc_list.html', group=group, autodoc=self.appbuilder.get_app.extensions['autodoc'].generate(groups=str(group)))

