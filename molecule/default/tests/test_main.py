import pytest
import os
import testinfra.utils.ansible_runner
testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("name, version", [
    ("httpd", ""),
    ("httpd-devel", ""),
    ("mod_ssl", ""),
])
def test_apache_packages(host, name, version):
    pkg = host.package(name)
    assert pkg.is_installed
    assert pkg.version.startswith(version)


def test_apache_service(host):
    service = host.service("httpd")
    with host.sudo():
        assert service.is_running
        assert service.is_enabled


def test_apache_port(host):
    assert host.socket('tcp://80').is_listening
    assert host.socket('tcp://443').is_listening


@pytest.mark.parametrize("command", [
    ("curl localhost"),
    ("curl -6 localhost"),
    ("curl -k localhost"),
    ("curl -6 -k localhost"),
])
def test_apache_curl(host, command):
    command = host.run(command)
    assert command.rc == 0
