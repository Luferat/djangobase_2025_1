# cadastro/context_processors.py

from core import settings


def global_context(request):
    return {
        'dono': 'Joca da Silva',
        'sitename': settings.APP_NAME,
    }