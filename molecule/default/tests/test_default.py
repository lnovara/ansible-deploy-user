import os
import pytest
import re
import testinfra.utils.ansible_runner
import yaml

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.fixture()
def ansible_defaults():
    with open('playbook-vars.yml', 'r') as stream:
        return yaml.load(stream)


@pytest.mark.parametrize('group', ansible_defaults()['user_groups'])
def test_groups_exists(host, group):
    g = host.group(group)

    assert g.exists


def test_user_exists(host, ansible_defaults):
    u = host.user(ansible_defaults['user_name'])

    assert u.exists


@pytest.mark.parametrize('group', ansible_defaults()['user_groups'])
def test_user_in_group(host, group, ansible_defaults):
    u = host.user(ansible_defaults['user_name'])

    assert group in u.groups


def test_user_shell(host, ansible_defaults):
    u = host.user(ansible_defaults['user_name'])

    assert u.shell == ansible_defaults['user_shell']


def test_authorized_keys(host, ansible_defaults):
    u = host.user(ansible_defaults['user_name'])
    f = host.file(os.path.join(u.home, '.ssh/authorized_keys'))

    assert (len(f.content_string.split('\n')) >=
            len(ansible_defaults['public_keys']))


def test_sudo_installed(host):
    assert host.package('sudo').is_installed


def test_sudoers_content(host, ansible_defaults):
    u = ansible_defaults['user_name']
    f1 = host.file('/etc/sudoers')
    f2 = host.file(os.path.join('/etc/sudoers.d/', u))

    p1 = '^\#includedir /etc/sudoers.d$'
    p2 = '^%s ALL=\(ALL\) NOPASSWD:ALL$' % u

    assert re.search(p1, f1.content_string, re.MULTILINE)
    assert re.search(p2, f2.content_string, re.MULTILINE)


#  def test_hosts_file(host):
#      f = host.file('/etc/hosts')

#      assert f.exists
#      assert f.user == 'root'
#      assert f.group == 'root'
