import logging
from flask_appbuilder.basemanager import BaseManager
from .views import DocumentsView
from .autodoc import Autodoc

log = logging.getLogger(__name__)

"""
   Create your plugin manager, extend from BaseManager.
   This will let you create your models and register your views

"""


class AutoDocManager(BaseManager):

    document_view = DocumentsView

    def __init__(self, appbuilder):
        """
             Use the constructor to setup any config keys specific for your app.
        """
        super(AutoDocManager, self).__init__(appbuilder)
        self.appbuilder.get_app.config.setdefault('AUTODOC_KEY', 'autodoc')

    def register_views(self):
        """
            This method is called by AppBuilder when initializing, use it to add you views
        """
        self.appbuilder.add_view(self.document_view, "AutoDocumentsView", label="Documents", icon="fa-file")


    def pre_process(self):
        pass

    def post_process(self):
        pass

