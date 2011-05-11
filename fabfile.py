from fabric.api import local, env

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

def epio(commandstring):
    local("epio {0} -a {1}".format(
        commandstring,
        env['epioapp']))