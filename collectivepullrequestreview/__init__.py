from pyramid.config import Configurator
from collectivepullrequestreview.resources import Root

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(root_factory=Root, settings=settings)
    config.add_view('collectivepullrequestreview.views.my_view',
                    context='collectivepullrequestreview:resources.Root',
                    renderer='collectivepullrequestreview:templates/mytemplate.pt')
    config.add_static_view('static', 'collectivepullrequestreview:static')
    return config.make_wsgi_app()

