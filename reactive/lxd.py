import os
from subprocess import check_call

from charmhelpers.core.hookenv import status_set
from charmhelpers.core.hookenv import config

from charms.reactive import set_state, when, when_not


@when_not('lxd.installed')
def install_lxd():
    '''Installs the LXD software from the archive.'''
    packages = ['lxd']
    apt_install(packages, fatal=True)
    set_state('lxd.installed')

@when('lxd.installed'))
def configure_lxd():
    '''Configure the LXD software if necessary.'''
    # Perform confguration here.
    set_state('lxd.configured')
