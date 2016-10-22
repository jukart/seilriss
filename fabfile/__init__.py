from fabric.api import run, local, env, task
from fabric.operations import put, get

import fabtools.python
import fabtools.require

env.user = 'pi'

VENV_DIR = 'env/seilriss'
DIRS = [
    'packages',
    'bin',
    'etc',
    'var',
    'var/log',
    'var/log/supervisor',
]


@task
def deploy():
    """Deploy for current sources
    """
    fabtools.require.files.directories(DIRS)
    local('rm -rf dist')
    local('python setup.py sdist')
    put('dist/*', 'packages/')
    put('fabfile/requirements.txt', '')
    put('fabfile/etc/supervisord.conf', 'etc')
    with fabtools.python.virtualenv(VENV_DIR):
        fabtools.require.python.requirements('requirements.txt')
    put('fabfile/bin/*', 'bin', mode=0755)


@task
def setup():
    """Setup the remote environment

    - install pip
    - install pygame
    - create a virtual python
    """
    if not fabtools.python.is_pip_installed():
        fabtools.python.install_pip()
    if not fabtools.deb.is_installed('python-pygame'):
        fabtools.deb.install('python-pygame')
    if not fabtools.python.virtualenv_exists(VENV_DIR):
        fabtools.require.python.virtualenv(
            VENV_DIR,
            system_site_packages=True
            )
