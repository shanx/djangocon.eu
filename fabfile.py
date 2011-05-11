import tempfile
from fabric.api import local, env

APPS_TO_SYNC = ('accommodation', 'blog', 'schedule', 'speakers', 'talks', 'waitlist')

def production():
    env['epioapp'] = 'djangocon-eu-2011'

def staging():
    env['epioapp'] = 'djangocon-eu-2011-staging'

def deploy():
    local("./manage.py collectstatic")
    epio('upload')
    epio('django syncdb')
    epio('django migrate')
    epio('django flush_cache')

def sync_data():
    with tempfile.NamedTemporaryFile(suffix='.json') as dumpfile:
        epio('django dumpdata {0} > {1}'.format(
            ' '.join(APPS_TO_SYNC),
            dumpfile.name))
        local('./manage.py loaddata {0}'.format(dumpfile.name))

def epio(commandstring):
    local("epio {0} -a {1}".format(
        commandstring,
        env['epioapp']))