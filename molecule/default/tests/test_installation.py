"""
Role tests
"""

import os
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_package(host):
    """
    Ensure package installed
    """

    assert host.package('xvfb').is_installed


def test_service(host):
    """
    Ensure service running
    """

    xvfb_service = host.service('xvfb')

    assert xvfb_service.is_enabled
    assert xvfb_service.is_running


def test_process(host):
    """
    Ensure process running
    """

    xvfb_process = host.process.get(user='root', comm='Xvfb')

    assert ':99 -screen 0 1x1x24 -ac +extension GLX +render -noreset' in \
        xvfb_process.args
    assert len(host.process.filter(comm='Xvfb')) == 1
