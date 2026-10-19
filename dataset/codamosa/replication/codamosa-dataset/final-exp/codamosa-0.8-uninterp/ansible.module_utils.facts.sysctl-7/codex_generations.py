

# Generated at 2022-06-13 02:09:21.137028
# Unit test for function get_sysctl

# Generated at 2022-06-13 02:09:24.732744
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(argument_spec=dict(
        prefixes=dict(type='list', default=None),
    ))
    result = get_sysctl(module, [])
    assert(isinstance(result, dict))


# Generated at 2022-06-13 02:09:34.107305
# Unit test for function get_sysctl

# Generated at 2022-06-13 02:09:39.819729
# Unit test for function get_sysctl
def test_get_sysctl():
    module = type('', (object,), {'warn': lambda *args, **kwargs: None, 'run_command': lambda *args: (0, '', ''), 'get_bin_path': lambda *args: ''})()
    prefixes = ['security.bsd']
    res = get_sysctl(module, prefixes)
    assert res.has_key('security.bsd.see_other_uids')

# Generated at 2022-06-13 02:09:40.094522
# Unit test for function get_sysctl
def test_get_sysctl():
    pass

# Generated at 2022-06-13 02:09:49.087000
# Unit test for function get_sysctl
def test_get_sysctl():
    in_values = {
        'net.ipv4.icmp_echo_ignore_broadcasts': 0,
        'net.ipv6.conf.all.accept_ra': 1,
        'kernel.ostype': 'Linux',
        'kernel.sem': '250  32000 32  128',
        'kernel.shmmni': 4096,
        'kernel.panic': 10,
        'net.core.wmem_max': 16777216,
        'net.core.rmem_default': 8388608,
        'net.core.netdev_budget': 300,
        'net.core.netdev_budget_usecs': 5000,
    }

# Generated at 2022-06-13 02:09:56.445095
# Unit test for function get_sysctl
def test_get_sysctl():
    class FakeModule(object):
        @staticmethod
        def run_command(cmd):
            return 0, 'key1 = key1\nkey2 = key2', ''

        @staticmethod
        def first_available_binary(*args):
            return 'sysctl'

        @staticmethod
        def warn(msg):
            return ''

    fake_module = FakeModule()
    expected = {u'key1': u'key1\nkey2', u'key2': u'key2'}
    assert get_sysctl(fake_module, ['key1', 'key2']) == expected

# Generated at 2022-06-13 02:10:06.483621
# Unit test for function get_sysctl
def test_get_sysctl():
    module = Mock()
    prefixes = []

# Generated at 2022-06-13 02:10:11.461628
# Unit test for function get_sysctl
def test_get_sysctl():
    import sys

    # cannot import module until we are Python 2.6
    module = sys.modules.get(__name__)

    sysctl_map = {'net.ipv4.ip_forward': '1',
            'net.ipv4.conf.default.rp_filter': '1',
            'net.ipv4.conf.default.accept_source_route': '0',
            'net.ipv4.conf.default.accept_redirects': '0',
            'net.ipv4.conf.all.accept_redirects': '0'}


# Generated at 2022-06-13 02:10:16.097079
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict()
    )

    sysctl = get_sysctl(module, ['kern.boottime', 'kern.hostname'])
    assert sysctl['kern.boottime']
    assert sysctl['kern.hostname']

# Generated at 2022-06-13 02:10:21.120057
# Unit test for function get_sysctl
def test_get_sysctl():
    pass

# Generated at 2022-06-13 02:10:29.747920
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(
        argument_spec = dict(),
    )

    module.run_command = MagicMock(return_value=(0, "vm.swappiness: 60\nvm.overcommit_ratio: 50\nvm.overcommit_memory: 2\nvm.dirty_ratio: 20\nvm.dirty_background_ratio: 10\nvm.dirty_expire_centisecs: 3000000\n", ""))
    assert get_sysctl(module, ['vm.swappiness', 'vm.overcommit_ratio', 'vm.overcommit_memory']) == {'vm.overcommit_ratio': '50', 'vm.overcommit_memory': '2', 'vm.swappiness': '60'}

    module.run_command = MagicMock(return_value=(1, "", "Error"))


# Generated at 2022-06-13 02:10:36.652390
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(argument_spec={'prefixes': {'required': True}})
    sysctl = get_sysctl(module, ['net.ipv4.ip_forward', 'net.ipv4.conf.all.proxy_arp'])

    assert sysctl['net.ipv4.ip_forward'] == '1'
    assert sysctl['net.ipv4.conf.all.proxy_arp'] == '0'



# Generated at 2022-06-13 02:10:41.947269
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(
        argument_spec = dict()
    )

    prefixes = ['kern.hostname', 'kern.version']
    result = get_sysctl(module, prefixes)
    assert(result['kern.hostname'] == 'foohost.mydomain.com')
    assert(result['kern.version'].startswith('Darwin Kernel Version'))


# Generated at 2022-06-13 02:10:48.005769
# Unit test for function get_sysctl
def test_get_sysctl():
    module = FakeModule()
    sysctl = get_sysctl(module, ['net.ipv4.ip_forward'])
    assert sysctl == dict(net_ipv4_ip_forward='1',)

    sysctl = get_sysctl(module, ['net'])
    assert sysctl == dict(net_core_somaxconn='128',)



# Generated at 2022-06-13 02:10:54.657345
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils import basic
    from ansible.module_utils.basic import AnsibleModule

    sysctl = dict()

    module = AnsibleModule(argument_spec=dict())

# Generated at 2022-06-13 02:11:00.002923
# Unit test for function get_sysctl
def test_get_sysctl():
    expected = {'net.ipv4.ip_forward': '1',
            'net.ipv6.conf.all.forwarding': '1',
            'vm.swappiness': '60'}
    sysctl = get_sysctl('net.ipv4.ip_forward net.ipv6.conf.all.forwarding vm.swappiness')
    assert sysctl == expected

# Generated at 2022-06-13 02:11:11.101598
# Unit test for function get_sysctl
def test_get_sysctl():
    import os
    import tempfile
    import pytest
    from ansible.module_utils import basic

    class FakeModule:
        def __init__(self):
            self.params = {}
            self.run_command_count = 0
            self.run_command_args = []
            self.run_command_rcs = []
            self.run_command_exc = []

        def get_bin_path(self, arg, **kwargs):
            return arg

        def run_command(self, args, **kwargs):
            self.run_command_count += 1
            self.run_command_args.append(args)
            if self.run_command_exc and self.run_command_exc[0]:
                exc = self.run_command_exc[0]

# Generated at 2022-06-13 02:11:15.623237
# Unit test for function get_sysctl
def test_get_sysctl():
    module = None
    prefixes = ['net.ipv4.conf.all.forwarding', 'net.ipv4.conf.all.proxy_arp']
    assert get_sysctl(module, prefixes) == {u'net.ipv4.conf.all.forwarding': u'0',
                                            u'net.ipv4.conf.all.proxy_arp': u'1'}

# Generated at 2022-06-13 02:11:26.119191
# Unit test for function get_sysctl
def test_get_sysctl():
    # Get a dict of all sysctl key/value pairs that start with "kern." and "vm."
    original_sysctl = get_sysctl(module=None, prefixes=['-a', 'kern.', 'vm.'])

    # Make a new dict with the kern. and vm. prefixes removed from the keys
    sysctl = dict()
    for key in original_sysctl.keys():
        sysctl[key.replace("kern.", "").replace("vm.", "")] = original_sysctl[key]

    # Test that the new dict includes a variety of expected key/value pairs
    assert sysctl['hostname'] == socket.gethostname()
    assert sysctl['domainname'] == ''
    assert sysctl['nisdomainname'] == ''
    assert type(sysctl['ostype']) == str

# Generated at 2022-06-13 02:11:42.131978
# Unit test for function get_sysctl
def test_get_sysctl():

    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule({})

    assert module.get_bin_path('true')
    assert module.get_bin_path('/bin/true')

    assert module.run_command(['true']) == (0, '', '')

    result = get_sysctl(module, ['fs.file-max'])

    assert 'fs.file-max' in result
    assert result['fs.file-max']
    assert result['fs.file-max'].isdigit()

# Test for function get_sysctl with invalid key

# Generated at 2022-06-13 02:11:45.313989
# Unit test for function get_sysctl
def test_get_sysctl():
    sysctl = get_sysctl(['vm.swappiness'])
    assert(sysctl['vm.swappiness'] == '60')

test_get_sysctl()

# Generated at 2022-06-13 02:11:51.576383
# Unit test for function get_sysctl
def test_get_sysctl():
    # Create a module object
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={})

    # Get sysctl(8) output as a Python dictionary
    sysctls = get_sysctl(module, ['vm.mmap_min_addr', 'vm.mmap_min_addr'])

    # Assert that the expected sysctls were found
    assert 'vm.mmap_min_addr' in sysctls
    assert 'vm.mmap_min_addr' in sysctls

# Generated at 2022-06-13 02:12:03.027393
# Unit test for function get_sysctl
def test_get_sysctl():
    p = MockedModule(name='sysctl_test')
    p.mock_module.run_command.return_value = (0, 'net.ipv4.ip_forward: 0\nnet.ipv6.conf.all.forwarding: 1', '')
    result = get_sysctl(p.mock_module, [])
    assert result['net.ipv4.ip_forward'] == '0'
    assert result['net.ipv6.conf.all.forwarding'] == '1'
    result = get_sysctl(p.mock_module, ['net.ipv4.ip_forward'])
    assert result['net.ipv4.ip_forward'] == '0'
    assert 'net.ipv6.conf.all.forwarding' not in result



# Generated at 2022-06-13 02:12:13.806816
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils import basic
    import os

    module = basic.AnsibleModule(
        argument_spec=dict(),
    )

    module.run_command = lambda *args, **kwargs: (0, 'net.ipv4.ip_forward = 1\nnet.ipv4.ip_forward_use_pmtu = 0', '')

    # Test with one prefix
    prefixes = ['net.ipv4']
    sysctl = get_sysctl(module, prefixes)

    assert len(sysctl) == 2
    assert sysctl['net.ipv4.ip_forward'] == '1'
    assert sysctl['net.ipv4.ip_forward_use_pmtu'] == '0'

    # Test with multiple prefixes

# Generated at 2022-06-13 02:12:22.590112
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(argument_spec={})
    module.run_command = MagicMock()
    module.run_command.return_value = (0,
"""net.ipv4.tcp_syncookies: 1
net.ipv4.tcp_syncookies: 1
net.ipv4.tcp_syncookies: 1
net.ipv4.tcp_syncookies: 1
""", '')
    # this is a fake sysctl that allows us to test parsing
    assert len(get_sysctl(module, ['fake.sysctl.value'])) == 0


# Generated at 2022-06-13 02:12:28.344366
# Unit test for function get_sysctl
def test_get_sysctl():
    class FakeModule:
        def __init__(self, run_command_exception=False):
            self.run_command_exception = run_command_exception
            self.choices = None

        def get_bin_path(self, app):
            return app

        def run_command(self, cmd):
            if self.run_command_exception:
                raise Exception("Command exception")

            if cmd[0] == "sysctl":
                if cmd[1] == "-a":
                    return (0, "kernel.printk_ratelimit = 9\nvm.overcommit_memory = 1\n", "")
                elif cmd[1] == "kernel.printk_ratelimit":
                    return (0, "kernel.printk_ratelimit = 9\n", "")

# Generated at 2022-06-13 02:12:34.948221
# Unit test for function get_sysctl
def test_get_sysctl():

    module = lambda: None
    module.warn = lambda msg: sys.stdout.write('Warning: %s' % msg)
    module.run_command = lambda cmd: (0, 'k1 = v1', '')
    module.get_bin_path = lambda cmd: cmd

    result = get_sysctl(module, ['k1'])

    assert result == {'k1': 'v1'}


# Generated at 2022-06-13 02:12:45.654606
# Unit test for function get_sysctl

# Generated at 2022-06-13 02:12:55.718921
# Unit test for function get_sysctl
def test_get_sysctl():

    import sys
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.pycompat24 import get_exception

    class SysctlImplementation(object):

        def __init__(self, module):
            self.module = module
            self.sysctl = dict()
            self.bin_path = '/bin/sysctl'
            self.rc = 0
            self.out = ''
            self.err = ''
            self.exception = None


        def run_command(self, cmd):
            if self.exception:
                try:
                    raise self.exception
                except:
                    self.exception = get_exception()
                    raise self.exception

            return (self.rc, self.out, self.err)

# Generated at 2022-06-13 02:13:23.828568
# Unit test for function get_sysctl
def test_get_sysctl():
    import sys
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat import unittest
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat.mock import patch
    from ansible.module_utils import basic

    if sys.version_info < (2, 7):
        import unittest2 as unittest


# Generated at 2022-06-13 02:13:33.668130
# Unit test for function get_sysctl
def test_get_sysctl():
    # sysctl() function test cases
    module = AnsibleModule(argument_spec=dict())

    # Test no sysctl output
    cmd = dict(rc=0, stdout='')
    module.run_command = MagicMock(return_value=cmd)
    sysctl = get_sysctl(module, [''])
    assert sysctl == dict()

    # Test a single line of sysctl output
    cmd = dict(rc=0, stdout='foo = bar\n')
    module.run_command = MagicMock(return_value=cmd)
    sysctl = get_sysctl(module, [''])
    assert sysctl == dict(foo='bar')

    # Test a single line of sysctl output with whitespace
    cmd = dict(rc=0, stdout='  foo  =  bar \n')
   

# Generated at 2022-06-13 02:13:41.336316
# Unit test for function get_sysctl
def test_get_sysctl():
    module = type('module', (object,), {})

# Generated at 2022-06-13 02:13:49.098571
# Unit test for function get_sysctl
def test_get_sysctl():
    import ansible.module_utils.basic
    import ansible.module_utils.local
    import os
    import sys
    import yaml

    sys.modules['ansible'] = ansible.module_utils.local
    sys.modules['ansible.module_utils'] = ansible.module_utils.basic

    fixture_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'sysctl.txt')

    with open(fixture_path, 'r') as f:
        fixture = f.read()

    with open(fixture_path + '.yml', 'r') as f:
        expected = yaml.safe_load(f)

    test_module = ansible.module_utils.local.AnsibleModule(argument_spec={})

# Generated at 2022-06-13 02:13:54.472817
# Unit test for function get_sysctl
def test_get_sysctl():
    module = get_bin_path.AnsibleModule(argument_spec=dict())

    sysctl = {}
    assert get_sysctl(module, sysctl) == sysctl

    sysctl = {'net.ipv4.conf.all.forwarding': '0'}
    assert get_sysctl(module, sysctl) == sysctl

    # This test is only valid if net.ipv4.ip_forward is 1
    sysctl['net.ipv4.conf.all.forwarding'] = '1'
    assert get_sysctl(module, sysctl) != sysctl

# Generated at 2022-06-13 02:13:58.886559
# Unit test for function get_sysctl
def test_get_sysctl():
    assert get_sysctl({'run_command': lambda *a, **kw: (0, 'net.ipv4.ip_forward = 1', ''), 'get_bin_path': lambda *a: '/sbin/sysctl'}, ['net.ipv4.ip_forward']) == {'net.ipv4.ip_forward': '1'}

# Generated at 2022-06-13 02:14:02.107688
# Unit test for function get_sysctl
def test_get_sysctl():
    module = FakeModule()
    prefixes = ['kernel.domainname', 'vm.swappiness']
    expected_sysctl = {
        'kernel.domainname': 'example.com',
        'vm.swappiness': '0'
    }
    sysctl = get_sysctl(module, prefixes)
    assert sysctl == expected_sysctl



# Generated at 2022-06-13 02:14:10.921773
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule

    test_module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode=True
    )

    test_module.run_command = lambda x: (0, 'net.ipv4.ip_forward: 1\nnet.ipv4.conf.default.rp_filter: 1', '')

    sysctl = get_sysctl(test_module, ['net.ipv4.ip_forward', 'net.ipv4.conf.default.rp_filter'])
    assert list(sysctl) == ['net.ipv4.ip_forward', 'net.ipv4.conf.default.rp_filter']
    assert sysctl['net.ipv4.ip_forward'] == '1'

# Generated at 2022-06-13 02:14:14.650661
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={})
    sysctl = get_sysctl(module, ['-a'])
    assert 'kernel.ostype' in sysctl
    assert sysctl['kernel.ostype'] == 'Linux'
    assert 'kernel.hostname' in sysctl



# Generated at 2022-06-13 02:14:21.257659
# Unit test for function get_sysctl
def test_get_sysctl():
    with open('/proc/sys/kernel/osrelease', 'r') as f:
        osrelease = f.read()
    sysctl = get_sysctl(osrelease, ['kernel.osrelease'])
    assert len(sysctl) == 1
    assert sysctl['kernel.osrelease'] == osrelease
    sysctl = get_sysctl(osrelease, ['kernel.unknown'])
    assert len(sysctl) == 0
    assert sysctl == {}

# Generated at 2022-06-13 02:15:15.922552
# Unit test for function get_sysctl
def test_get_sysctl():
#    sysctl_cmd = module.get_bin_path('sysctl')
#    cmd = [sysctl_cmd]
#    cmd.extend(prefixes)

#    sysctl = dict()

#    try:
#        rc, out, err = module.run_command(cmd)
#    except (IOError, OSError) as e:
#        module.warn('Unable to read sysctl: %s' % to_text(e))
#        rc = 1

    expected = {"kernel.sem": "250 32000 32 4096",
                "kernel.sysrq": "1",
                "vm.swappiness": "60",
                "vm.drop_caches": "0"}


# Generated at 2022-06-13 02:15:24.702373
# Unit test for function get_sysctl
def test_get_sysctl():
    import tempfile
    import pytest

    from ansible.module_utils.basic import AnsibleModule


# Generated at 2022-06-13 02:15:34.592121
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(
        argument_spec = dict(
            prefixes=dict(type='list')
        )
    )
    fake_bin_path = 'ansible/module_utils/basic.py'
    sysctl_content = '''
    kernel.sysrq = 0
    kernel.msgmax = 2097152
    kernel.msgmnb = 2097152
    kernel.msgmni = 2852
    '''
    sysctl_dict = dict(
        kernel=dict(
            msgmnb='2097152',
            msgmni='2852',
            msgmax='2097152',
            sysrq='0'
        )
    )

    class AnsibleExitJson(Exception):
        """Exception class to be raised by module.exit_json and caught by the test case"""

# Generated at 2022-06-13 02:15:42.097003
# Unit test for function get_sysctl
def test_get_sysctl():

    from ansible.module_utils.basic import AnsibleModule

    class TestAnsibleModule(AnsibleModule):
        def __init__(self, *args, **kwargs):
            super(TestAnsibleModule, self).__init__(*args, **kwargs)
            self._ansible_sysctl = ['-a']

        @property
        def ansible_sysctl(self):
            return self._ansible_sysctl

        @ansible_sysctl.setter
        def ansible_sysctl(self, value):
            self._ansible_sysctl = value

        def get_bin_path(self, arg, *args, **kwargs):
            return arg

    test_module = TestAnsibleModule(argument_spec={})

# Generated at 2022-06-13 02:15:48.258157
# Unit test for function get_sysctl
def test_get_sysctl():
    def mock_module(run_command=None, warn=None, get_bin_path=None):
        class MockModule(object):
            def __init__(self):
                self.run_command_results = dict()
                self.run_command_results['sysctl -a'] = (0, """
net.core.wmem_max: 262144
net.core.rmem_max: 4194304
net.ipv4.tcp_rmem: 4096    87380   4194304
net.ipv4.tcp_wmem: 4096    16384   262144
net.ipv4.udp_rmem_min: 4096
net.ipv4.udp_wmem_min: 4096
""", '')


# Generated at 2022-06-13 02:15:58.457121
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule
    import sys

    if sys.version_info.major < 3:
        from mock import patch
    else:
        from unittest.mock import patch

    module = AnsibleModule(
        argument_spec=dict(
            prefixes=dict(required=True, type='list')
        )
    )


# Generated at 2022-06-13 02:16:05.917797
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule
    import os

    sysctl_cmd = AnsibleModule(
        argument_spec=dict(),
    ).get_bin_path('sysctl')

    if sysctl_cmd is None:
        raise AssertionError('sysctl command not found, skipping test')

    prefixes = ['kernel.osrelease', 'vm.swappiness']
    sysctl = get_sysctl(AnsibleModule(argument_spec=dict()), prefixes)

    # make os.system() behave like normal run_command()
    os.environ['ANSIBLE_KEEP_REMOTE_FILES'] = '1'
    os.environ['ANSIBLE_REMOTE_TEMP'] = '/tmp'

    cmd = [sysctl_cmd]
    cmd.extend(prefixes)
    rc

# Generated at 2022-06-13 02:16:09.322165
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = False
    )
    res = get_sysctl(module, ['vm.swappiness'])
    assert 'vm.swappiness' in res


# Generated at 2022-06-13 02:16:12.402789
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(argument_spec=dict(
        prefixes=dict(required=True, type='list')
    ))

    module.run_command.return_value = (
        0,
        """foo.bar = 1
        foo.zoo = 2""",
        None)
    sysctl = get_sysctl(module, ['foo'])
    assert sysctl['foo.bar'] == '1'
    assert sysctl['foo.zoo'] == '2'

# Generated at 2022-06-13 02:16:14.766093
# Unit test for function get_sysctl
def test_get_sysctl():
    assert get_sysctl(['-w'], None) == {}

# Generated at 2022-06-13 02:18:11.569050
# Unit test for function get_sysctl
def test_get_sysctl():
    # Example output from sysctl
    sysctl_out = """
    debug.bootverbose = 1
    user.john.uid = 501
    user.john.gid = 20
    user.john.home = /home/john
    user.john.shell = /bin/tcsh
    """

    sysctl_dict = dict()

    key = ''
    value = ''
    for line in sysctl_out.splitlines():
        if not line.strip():
            continue

        if line.startswith(' '):
            # handle multiline values, they will not have a starting key
            # Add the newline back in so people can split on it to parse
            # lines if they need to.
            value += '\n' + line
            continue

        if key:
            sysctl_dict[key] = value.strip()

# Generated at 2022-06-13 02:18:14.106474
# Unit test for function get_sysctl
def test_get_sysctl():
    module = type('FakeModule', (), {'run_command': lambda *args, **kwargs: (0, '', ''), 'warn': lambda *args, **kwargs: None})

    result = get_sysctl(module, [])
    assert result == {}

    result = get_sysctl(module, ['foo', 'bar'])
    assert result == {}



# Generated at 2022-06-13 02:18:18.093647
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    sysctl = get_sysctl(module, ['-a'])

    assert sysctl['kernel.hostname'] == 'localhost.localdomain'
    assert 'kernel.random.read_wakeup_threshold' in sysctl

# Generated at 2022-06-13 02:18:25.653523
# Unit test for function get_sysctl
def test_get_sysctl():
    module = None

# Generated at 2022-06-13 02:18:30.853031
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule
    m = AnsibleModule(argument_spec={
        'prefixes': {'type': 'list', 'required': True},
    })
    if m:
        sysctl = get_sysctl(m, m.params['prefixes'])
        assert isinstance(sysctl, dict)
        assert len(sysctl.keys()) > 0

# Generated at 2022-06-13 02:18:40.069599
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(argument_spec=dict())

    # get_sysctl will not be run if the module arguments are passed.
    module.params = dict()

    mock_run_command = MagicMock()

    sysctl_results = """
    net.ipv4.icmp_echo_ignore_broadcasts = 1
    net.ipv4.tcp_syncookies = 1
    net.ipv4.tcp_max_orphans = 262144
    net.ipv4.conf.all.accept_source_route = 0
    net.ipv4.conf.default.accept_source_route = 0
    net.ipv4.conf.all.accept_redirects = 0
    net.ipv4.conf.default.accept_redirects = 0
    """

# Generated at 2022-06-13 02:18:44.064034
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils import basic
    module = basic.AnsibleModule(argument_spec=dict())

    assert get_sysctl(module, []) == dict()
    assert get_sysctl(module, ['foo.bar']) == dict()
    # Some systems don't expose 'kern.version'
    assert get_sysctl(module, ['kern.version']) == dict() or get_sysctl(module, ['kern.version']) != dict()

# Generated at 2022-06-13 02:18:48.847328
# Unit test for function get_sysctl
def test_get_sysctl():
    module = None

    # Return an empty dict if sysctl is not available
    assert get_sysctl(module, '') == dict()

    # Return a dict of sysctl values parsed out of sysctl -a output
    results = get_sysctl(module, '')
    assert 'kern.ostype' in results
    assert 'net.inet.tcp.pcblist' in results

# Generated at 2022-06-13 02:18:51.912282
# Unit test for function get_sysctl
def test_get_sysctl():
    assert get_sysctl({'run_command': _run_command}, ['fs.file-max', 'kernel.shmmax']) == {
        'fs.file-max': '999888',
        'kernel.shmmax': '999777',
    }


# Unit test helper

# Generated at 2022-06-13 02:19:01.605988
# Unit test for function get_sysctl
def test_get_sysctl():

    MOCK_STDOUT = '''
dev.mac_hid.mouse_button_emulation: 0 -> 1
dev.cpu.0.freq: 1197 -> 1197
dev.cpu.0.freq_levels: 100 1197 1400 1600 1900 2200 2600 3000
hw.acpi.cpu.px_dom0.hotplug: 1
hw.acpi.cpu.px_dom0.hotplug_enable: 0 -> 1
hw.acpi.cpu.px_dom1.hotplug: 1
hw.acpi.cpu.px_dom1.hotplug_enable: 0 -> 1'''
