import ckan.plugins as p
from ckan.plugins import toolkit as tk

class ExceptionPlugin(p.SingletonPlugin):

    p.implements(p.IRoutes, inherit=True)

    def before_map(self, map):
        map.connect('exception', '/exception',
                controller='ckanext.exception.plugin:AwesomeException',
            action='get')
        return map

class AwesomeException(tk.BaseController):

    def get(self):
        return 1/0
