

# Generated at 2022-06-13 02:09:21.515105
# Unit test for function get_sysctl
def test_get_sysctl():
    """
    Get sysctl value and return it as dict
    """
    test_out = "net.netfilter.nf_conntrack_tcp_be_liberal = 0\nnet.netfilter.nf_conntrack_max = 65536"
    test_prefixes = ["-a"]
    test_sysctl_cmd = "sysctl"
    test_rc = 0
    test_err = ""
    test_module = MockModule()

    result = get_sysctl(test_module, test_prefixes)
    assert result["net.netfilter.nf_conntrack_tcp_be_liberal"] == "0"
    assert result["net.netfilter.nf_conntrack_max"] == "65536"


# Generated at 2022-06-13 02:09:31.464339
# Unit test for function get_sysctl
def test_get_sysctl():
    """Unit tests for get_sysctl"""
    import sysctl
    import __builtin__ as builtins
    import tempfile
    import os
    import textwrap
    import mock

    args = {}

# Generated at 2022-06-13 02:09:34.423604
# Unit test for function get_sysctl
def test_get_sysctl():
    module = MockModule()
    sysctl = get_sysctl(module, ['kernel'])
    assert sysctl['kernel.domainname'] == 'localdomain'

# ==============================================================================
# Mocking for unit tests
# ==============================================================================

# Generated at 2022-06-13 02:09:39.875286
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.common.process import get_bin_path

    sysctl_cmd = get_bin_path('sysctl')
    if sysctl_cmd is None:
        return False, sysctl_cmd

    with open('/proc/sys/kernel/hostname', 'r') as f:
        hostname = f.read()

    sysctl = get_sysctl(module=None, prefixes=['kernel.hostname'])

    assert sysctl_cmd == '/sbin/sysctl' and sysctl['kernel.hostname'] == hostname
    return True, sysctl

# vim: ai et ts=4 sw=4 sts=4

# Generated at 2022-06-13 02:09:41.364144
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(argument_spec=dict())
    sysctl = get_sysctl(module, ['vm.swappiness'])
    assert sysctl['vm.swappiness'] == '60'

# Generated at 2022-06-13 02:09:52.089955
# Unit test for function get_sysctl
def test_get_sysctl():
    import sys
    import os
    # if python version < 2.7 use unittest2
    if sys.version_info < (2, 7):
        import unittest2 as unittest
    else:
        import unittest

    import contextlib
    try:
        from StringIO import StringIO
    except ImportError:
        from io import StringIO


# Generated at 2022-06-13 02:09:59.727683
# Unit test for function get_sysctl
def test_get_sysctl():
    import sys
    import os
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule({})

# Generated at 2022-06-13 02:10:08.572237
# Unit test for function get_sysctl
def test_get_sysctl():
    test_module = FakeAnsibleModule()
    fake_out = '''net.ipv4.ip_forward: 1
net.ipv4.conf.all.forwarding:  0
    This is a multiline value
net.ipv6.conf.all.forwarding: 0
'''

    fake_results = dict()
    fake_results['rc'] = 0
    fake_results['stdout'] = fake_out
    fake_results['stderr'] = ''
    test_module.run_command = FakeCommand(**fake_results)
    sysctl = get_sysctl(test_module, [])

    assert sysctl.get('net.ipv4.ip_forward') == '1'

    test_module = FakeAnsibleModule()

# Generated at 2022-06-13 02:10:14.352905
# Unit test for function get_sysctl
def test_get_sysctl():
    ac = dict(os.environ)
    ac['PATH'] = '/bin'
    command = dict(ansible_shell_executable='/bin/sh',
                   ansible_python_interpreter='/usr/bin/python',
                   ansible_env=ac)
    module = MockModule(command_def=command)

    sysctl = get_sysctl(module, ['kern.geom.label', 'kern.proc.all'])

    assert sysctl['kern.geom.label'] == '/dev/gptid/d9e38e85-94ec-11e6-b968-0cc47a1c8beb'

# Generated at 2022-06-13 02:10:24.731402
# Unit test for function get_sysctl
def test_get_sysctl():
    # test_module accepts a function with one argument which is a module_runner.
    # This function must return True to pass the test, or False to fail it.
    from ansible.modules.system import sysctl
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils import basic

    # Create a fake AnsibleModule instance
    am = AnsibleModule(
        argument_spec=sysctl.argument_spec,
    )

    def run_command(*args, **kwargs):
        raise IOError('Unable to run sysctl: %s' % str(args[1]))

    # Set our fake module.run_command
    am.run_command = run_command

    # Run the function under test
    assert sysctl.get_sysctl(am) is None

# Generated at 2022-06-13 02:10:34.667784
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(
        argument_spec = dict()
    )

    sysctl = get_sysctl(module, ["net.core.somaxconn"])
    assert sysctl["net.core.somaxconn"] == "128"


# Generated at 2022-06-13 02:10:45.631534
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import Connection
    from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import module_for_test

    # Create a fake module with a set of fake argument spec
    module = module_for_test({})

    module.get_bin_path = Connection.get_bin_path
    module.run_command = Connection.run_command

    # Get a dict containing the current sysctl values
    sysctl_values = get_sysctl(module, ['net'])

    # test that we have a value
    assert sysctl_values['net.ipv4.tcp_fin_timeout']

    # test that we have a value that contains a newline

# Generated at 2022-06-13 02:10:53.613148
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils import basic
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import PY3

    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    class FakeModule(object):
        def __init__(self, d, p=None):
            self.d = d
            self.p = p

        def run_command(self, cmd):
            assert cmd[0] == 'sysctl'
            assert cmd[1:] == self.p
            return (0, self.d, '')

    # Test a basic sysctl
    module.basic = basic
    module.basic.AnsibleModule = AnsibleModule


# Generated at 2022-06-13 02:10:57.803312
# Unit test for function get_sysctl
def test_get_sysctl():

    from ansible.module_utils.basic import AnsibleModule

    class MockModule():

        def __init__(self, params):
            self.params = params

        def get_bin_path(self, arg, *args, **kwargs):
            return 'sysctl'


# Generated at 2022-06-13 02:11:03.024485
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils import basic
    module = basic.AnsibleModule(
        argument_spec = dict()
    )
    assert module.get_bin_path('sysctl') is not None

    sysctl = get_sysctl(module, [])
    assert 'kernel.ostype' in sysctl
    assert sysctl['kernel.ostype'] is not None
    assert len(sysctl['kernel.ostype']) > 0

# Generated at 2022-06-13 02:11:07.317039
# Unit test for function get_sysctl
def test_get_sysctl():
    module = type('', (), dict(run_command=lambda self, x, **kw: (0, 'a.b: 1\nc.d: 2\n', '')))
    assert get_sysctl(module, []) == dict(a_b='1', c_d='2')

# Generated at 2022-06-13 02:11:15.843893
# Unit test for function get_sysctl
def test_get_sysctl():
    sysctl = {b'net.ipv4.conf.all.rp_filter': 1, b'net.ipv4.conf.default.rp_filter': 1}
    assert(get_sysctl({'run_command': (0, b'net.ipv4.conf.all.rp_filter = 1\nnet.ipv4.conf.default.rp_filter = 1', b'')}, []) == sysctl)
    assert(get_sysctl({'run_command': (0, b'net.ipv4.conf.all.rp_filter = 1\nnet.ipv4.conf.default.rp_filter = 1', b'')}, ['net.ipv4.conf*']) == sysctl)

# Generated at 2022-06-13 02:11:21.714582
# Unit test for function get_sysctl
def test_get_sysctl():
    ''' Function get_sysctl returns a dictionary of prefixes '''
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule({'ANSIBLE_MODULE_ARGS': '', 'ANSIBLE_ARGS': ''})
    sysctl = get_sysctl(module, ['kernel.', 'hw.'])
    assert sysctl
    assert sysctl['hw.physmem']
    assert sysctl['kernel.ostype']

# Generated at 2022-06-13 02:11:29.918607
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.six import PY2
    from ansible.module_utils import basic
    import os

    class TestModule(object):
        def __init__(self, params):
            self.params = params

        def warn(self, warning):
            raise Warning(warning)

        def run_command(self, args):
            path = os.path.join(os.path.dirname(__file__), 'test', 'unit', 'module_utils', 'system', 'test.sysctl')
            with open(path, 'r') as f:
                return 0, f.read(), None

        def get_bin_path(self, name):
            return name

    test_module = TestModule({})
    actual = get_sysctl(test_module, ['vm'])


# Generated at 2022-06-13 02:11:38.320990
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict()
    )

    sysctl_output_example = '''net.ipv4.ip_forward: 1
net.ipv6.conf.default.forwarding: 1
net.ipv6.conf.all.forwarding: 1
net.ipv6.conf.ens160.accept_ra: 0
net.ipv6.conf.lo.accept_ra: 0
'''


# Generated at 2022-06-13 02:11:55.373936
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule

    test_path = '/tmp/ansible_test_bin'

    class SysctlTest(object):
        def __init__(self, binfile, returns=None):
            self.binfile = binfile
            self.binpath = test_path
            self.returns = returns or (0, '', '')

        def get_bin_path(self, path, opt_dirs=[]):
            return self.binpath + '/' + path

        def run_command(self, cmd):
            assert self.binpath + '/' + cmd[0] == self.binfile

            if cmd[1:] == ['vm.swappiness']:
                return self.returns

            assert cmd[1:] == ['vm.swappiness', 'kernel.hostname']
            return

# Generated at 2022-06-13 02:12:06.331244
# Unit test for function get_sysctl
def test_get_sysctl():
    import ansible.module_utils.basic

    # This is a test helper method.  It will not normally be used in a module.
    class TestException(Exception):
        pass

    # This is a test helper method.  It will not normally be used in a module.
    class TestModule:
        def __init__(self, param):
            self._param = param

        def fail_json(self, **kwargs):
            raise TestException(kwargs)

        def exit_json(self, **kwargs):
            raise TestException(kwargs)

        def get_bin_path(self, name, **kwargs):
            if name == 'sysctl':
                return 'dummy-sysctl'
            else:
                return None


# Generated at 2022-06-13 02:12:15.523016
# Unit test for function get_sysctl
def test_get_sysctl():
    module = DummyAnsibleModule()

    sysctl = get_sysctl(module, ['net.ipv4.ip_forward'])
    assert sysctl == {'net.ipv4.ip_forward': '1'}

    sysctl = get_sysctl(module, ['kernel.mq_mqs_not_set'])
    assert not sysctl

    sysctl = get_sysctl(module, ['kernel.shmmax'])
    assert sysctl == {'kernel.shmmax': '34359738368'}

    sysctl = get_sysctl(module, ['kernel.shmmax'])
    assert sysctl == {'kernel.shmmax': '34359738368'}



# Generated at 2022-06-13 02:12:23.489424
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.basic import AnsibleModule

    sysctl_cmd = ''
    module = AnsibleModule(argument_spec=dict())
    rc = 0
    out = b''
    err = b''
    try:
        rc, out, err = module.run_command
    except (IOError, OSError):
        pass

    def _run_command_mock(cmd):
        return rc, out, err

    module.run_command = _run_command_mock
    module.get_bin_path = lambda _: sysctl_cmd

    # test with empty command output
    out = ''
    err = ''
    result = get_sysctl(module, ['vm.swappiness'])

# Generated at 2022-06-13 02:12:28.962929
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict()
    )

    sysctl = get_sysctl(module, ['security.jail'])
    assert(sysctl['security.jail.jailed'] == '0')

    sysctl = get_sysctl(module, ['hw.memsize', 'hw.ncpu'])
    assert(sysctl['hw.memsize'] == '1073741824')
    assert(sysctl['hw.ncpu'] == '16')
    assert('security.jail.jailed' not in sysctl)

    sysctl = get_sysctl(module, ['machdep.hyperthreading_allowed'])
    assert(sysctl['machdep.hyperthreading_allowed'] == '1')

    # Test

# Generated at 2022-06-13 02:12:38.439872
# Unit test for function get_sysctl
def test_get_sysctl():
    import ansible.module_utils.basic

    # We are going to mock out the run_command function here, so that it
    # can be easily tested.
    def _run_command(self, cmd):
        stdout = 'kernel.hostname = myhost'
        stdout += '\nkernel.domainname = mydomain.com'
        stdout += '\nkernel.osrelease = 4.1.12-60.66.amzn1.x86_64\n'
        stdout += '\nkernel.osrelease_description = Amazon Linux AMI release 2016.03\n'
        stdout += '\nkernel.ostype = Linux\n'
        stdout += '\nkernel.pid_max = 402653184\n'
        stdout += '\nkernel.printk = 4 4 1 7\n'

# Generated at 2022-06-13 02:12:42.016286
# Unit test for function get_sysctl
def test_get_sysctl():
    ''' Test get_sysctl function '''
    # Requires sudo access
    assert type(get_sysctl('', ['kernel'])) is dict



# Generated at 2022-06-13 02:12:50.792182
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.six import PY3

    # If sysctl is not in the path, this function will fail
    if PY3:
        import unittest.mock as mock
        mock = mock.patch('ansible.module_utils.basic.get_bin_path')
    else:
        import mock
        mock = mock.patch('ansible.module_utils.basic.get_bin_path')
    mock.return_value = "sysctl"

    # No indenting

# Generated at 2022-06-13 02:12:58.717149
# Unit test for function get_sysctl
def test_get_sysctl():
    module = type('', (), {})()
    module.get_bin_path = lambda s: 'sysctl'
    module.run_command = lambda s: (0, 'net.ipv4.ip_forward = 1\nnet.ipv4.conf.all.accept_redirects = 0\nnet.ipv4.conf.all.accept_source_route = 0\nnet.ipv4.conf.default.accept_redirects = 0\nnet.ipv4.conf.default.accept_source_route = 0\nnet.ipv4.conf.lo.accept_redirects = 0\nnet.ipv4.conf.lo.accept_source_route = 0', None)

    result = get_sysctl(module, ['net.ipv4.ip_forward'])

# Generated at 2022-06-13 02:13:03.843813
# Unit test for function get_sysctl
def test_get_sysctl():
    result = get_sysctl({'run_command':lambda x: (0, 'net.ipv4.tcp_fin_timeout = 60\nnet.ipv4.tcp_keepalive_time = 7200', '')}, ['net.ipv4.tcp_fin_timeout', 'net.ipv4.tcp_keepalive_time'])
    assert result == {'net.ipv4.tcp_fin_timeout': '60', 'net.ipv4.tcp_keepalive_time': '7200'}


# Generated at 2022-06-13 02:13:27.650654
# Unit test for function get_sysctl
def test_get_sysctl():
    import sysctl
    sysctl_cmd = sysctl.get_sysctl(['net.ipv4.tcp_max_syn_backlog'])
    assert sysctl_cmd['net.ipv4.tcp_max_syn_backlog'] == os.environ['ANSIBLE_NET_IPV4_TCP_MAX_SYN_BACKLOG']

# Generated at 2022-06-13 02:13:34.229102
# Unit test for function get_sysctl
def test_get_sysctl():
    module = ansible.utils.module_runner.AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True)
    module.run_command = mock.MagicMock(return_value=(0, "kern.sched.preempt_thresh: 0", ""))
    sysctl = get_sysctl(module, ["kern.sched.preempt_thresh"])
    assert sysctl == {"kern.sched.preempt_thresh": "0" }

# Generated at 2022-06-13 02:13:39.241835
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={})
    module.run_command = lambda x: (0, 'kernel.sem = 250\t32000\t32\t128', '')
    module.get_bin_path = lambda x: x

    sysctl = get_sysctl(module, ['kernel.sem'])
    assert sysctl['kernel.sem'] == '250\t32000\t32\t128'

# Generated at 2022-06-13 02:13:47.484954
# Unit test for function get_sysctl
def test_get_sysctl():
    module = MagicMock()
    prefixes = ['-a']
    sysctl_out = '''net.ipv4.ip_forward = 0
net.ipv4.tcp_max_syn_backlog = 524288
net.ipv4.conf.all.arp_ignore = 1
'''
    module.run_command.return_value = (0, sysctl_out, '')
    sysctl = get_sysctl(module, prefixes)
    assert(sysctl['net.ipv4.ip_forward'] == '0')
    assert(sysctl['net.ipv4.tcp_max_syn_backlog'] == '524288')
    assert(sysctl['net.ipv4.conf.all.arp_ignore'] == '1')


# Generated at 2022-06-13 02:13:54.207022
# Unit test for function get_sysctl
def test_get_sysctl():
    """The test uses `modprobe` to test reading the sysctl"""
    from ansible.module_utils.basic import AnsibleModule

    class AnsibleModuleFake(AnsibleModule):
        def __init__(self):
            super(AnsibleModuleFake, self).__init__(
                argument_spec={
                    'params': dict(type='list', default=['kernel.hostname']),
                },
                supports_check_mode=True
            )

        def run_command(self, *args, **kwargs):
            (cmd, ) = args
            if cmd[0] != 'modprobe':
                self.fail_json('Expected `modprobe` to be called')
            return (0, 'kernel.hostname = {0}\n'.format(socket.gethostname()), '')


# Generated at 2022-06-13 02:13:55.484826
# Unit test for function get_sysctl
def test_get_sysctl():
    assert get_sysctl(['kernel.msgmax']) == {'kernel.msgmax': '65536'}

# Generated at 2022-06-13 02:14:01.083488
# Unit test for function get_sysctl
def test_get_sysctl():

    # We're not actually running any commands here, just checking that the
    # regexp works as expected.

    from ansible.module_utils.basic import AnsibleModule

    # Setup mock module
    module = AnsibleModule(
        argument_spec = dict()
    )

    cmd_out = u"key1 = value1\nkey2: value2\nkey3 = value3a\n value3b\n key3c\nkey4=value\n key5=value5a\n value5b\nkey6:\n value6a\n value6b\n\nkey7: value7a\n value7b\n value7c\n"
    result = get_sysctl(module, cmd_out.splitlines())

    assert result['key1'] == "value1"

# Generated at 2022-06-13 02:14:08.244886
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils._text import to_bytes
    from ansible.modules.extras.system.sysctl import get_sysctl

    out = to_bytes('''
kernel.domainname = test
kernel.kptr_restrict = 2
''')

    sysctl = get_sysctl(object(), ['kernel.domainname', 'kernel.kptr_restrict'])
    assert sysctl == {
        'kernel.domainname': 'test',
        'kernel.kptr_restrict': '2'
    }

# Generated at 2022-06-13 02:14:11.156407
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils import basic
    module = basic.AnsibleModule(argument_spec=dict())
    sysctl = get_sysctl(module, ['kernel.ostype'])
    assert 'kernel.ostype' in sysctl
    assert sysctl['kernel.ostype'] is not None

# Generated at 2022-06-13 02:14:19.527776
# Unit test for function get_sysctl
def test_get_sysctl():
    module = Mock()
    sysctl = dict({'net.ipv4.tcp_max_syn_backlog': '123', 'net.ipv6.conf.all.disable_ipv6': '1'})

    def run_command_mock(cmd):
        return 0, "", ""

    module.run_command = run_command_mock
    module.get_bin_path = Mock(return_value="/bin/sysctl")

    assert sysctl == get_sysctl(module, ["net.ipv4.tcp_max_syn_backlog", "net.ipv6.conf.all.disable_ipv6"])


# Generated at 2022-06-13 02:15:17.303059
# Unit test for function get_sysctl
def test_get_sysctl():
    module = MockModule()
    module.run_command.return_value = 0, """
    net.ipv4.ip_forward = 1
    kernel.ostype = Linux
    kernel.osrelease = 3.10.0-327.el7.x86_64
    kernel.osrelease_banner = CentOS Linux release 7.2.1511 (Core)
    kernel.version = #1 SMP Thu Nov 19 22:10:57 UTC 2015
    kernel.hostname = localhost.localdomain
    kernel.domainname = (none)
    kernel.modprobe = /usr/sbin/modprobe
    fs.inotify.max_user_instances = 128
    fs.inotify.max_user_watches = 8192
    vm.max_map_count = 262144
    """.strip(), ""

# Generated at 2022-06-13 02:15:22.614391
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(argument_spec={'prefixes': dict(required=True, type='list')})
    assert get_sysctl(module, ['vm.overcommit_memory']) == {'vm.overcommit_memory': '0'}


# Import module snippets.
from ansible.module_utils.basic import *
#from ansible.module_utils.six import iteritems

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 02:15:25.649147
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec=dict())

    sysctl = get_sysctl(module, ['vm'])
    assert sysctl
    assert sysctl['vm.nr_hugepages'] == '0'
    assert sysctl['vm.swappiness'] == '60'

# Generated at 2022-06-13 02:15:31.284213
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule

    test = AnsibleModule(
        argument_spec=dict()
    )

    sysctl = get_sysctl(test, ['kern', 'maxproc'])

    assert sysctl == {
        'kern.maxproc': '10485760'
    }

# vim: expandtab tabstop=4 shiftwidth=4

# Generated at 2022-06-13 02:15:39.733377
# Unit test for function get_sysctl
def test_get_sysctl():
    module = type('ModuleTest', (), dict(run_command=_run_command))

    def test_get_sysctl(prefixes, rc, out):
        # function with same name.
        sysctl = get_sysctl(module, prefixes)

        # assert that run_command is called with correct parameters and
        # data structure returned is correct.
        assert module.run_command.called
        assert module.run_command.call_args == (_run_command_args(prefixes), )

        if rc != 0:
            assert sysctl == {}
        else:
            for key, value in out.items():
                assert sysctl[key] == value

    global _rc, _out, _err, _run_command_calls
    _run_command_calls = 0
    _rc = 0
    _out = {}


# Generated at 2022-06-13 02:15:46.428739
# Unit test for function get_sysctl
def test_get_sysctl():
    def get_fake_ansible_module(rc, data=''):
        class FakeAnsibleModule:
            def __init__(self, rc, data):
                self._rc = rc
                self._data = data
                self._warnings = []

            def get_bin_path(self, name):
                return name

            def run_command(self, cmd):
                return self._rc, self._data, ''

            def warn(self, msg):
                self._warnings.append(msg)

        return FakeAnsibleModule(rc, data)

    module = get_fake_ansible_module(0, 'kernel.msgmnb = 65536\nkernel.msgmax = 65536\n')
    prefixes = ['kernel.msgmnb', 'kernel.msgmax']


# Generated at 2022-06-13 02:15:51.378770
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(argument_spec=dict())
    result = get_sysctl(module, ['kernel.hostname'])

# Generated at 2022-06-13 02:16:01.418183
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModuleMock()
    test_sysctl = {'fs.file-max': '3903',
                   'kernel.randomize_va_space': '2',
                   'net.ipv4.ip_forward': '0',
                   'net.ipv4.ip_local_port_range': '32768    61000',
                   'net.ipv4.tcp_window_scaling': '1',
                   'net.ipv4.tcp_fin_timeout': '15',
                   'net.ipv4.tcp_keepalive_time': '1800',
                   'net.core.somaxconn': '1024'}

    result = get_sysctl(module, ['fs', 'kernel', 'net.ipv4', 'net.core'])

# Generated at 2022-06-13 02:16:04.974978
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(argument_spec=dict())
    sysctl = get_sysctl(module, [
        'kernel', 'fs', 'vm', 'net', 'net.ipv4', 'net.ipv4.ip_forward'])
    assert 'kernel.ostype' in sysctl
    assert 'net.ipv4.ip_forward' in sysctl



# Generated at 2022-06-13 02:16:08.034308
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(
        argument_spec=dict(),
    )
    module.get_bin_path = lambda x: '/sbin/sysctl'
    module.run_command = lambda x: (0, 'foo = bar\nbar = foo', '')
    results = get_sysctl(module, [])
    assert results['foo'] == 'bar'
    assert results['bar'] == 'foo'


# Generated at 2022-06-13 02:18:13.870116
# Unit test for function get_sysctl
def test_get_sysctl():
    import os
    import sys

    sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.realpath(__file__))))

    from units.compat.mock import patch
    from ansible.module_utils.basic import AnsibleModule


# Generated at 2022-06-13 02:18:20.578174
# Unit test for function get_sysctl
def test_get_sysctl():
    module = MagicMock()
    get_bin_path = MagicMock(return_value='/usr/sbin/sysctl')
    setattr(module, 'get_bin_path', get_bin_path)
    run_command = MagicMock(return_value=(0, 'value = myvalue', ''))
    setattr(module, 'run_command', run_command)
    module.warn = MagicMock()

    result = get_sysctl(module, ['value'])

    get_bin_path.assert_called_with('sysctl')
    run_command.assert_called_with(['/usr/sbin/sysctl', 'value'])
    assert result == {'value': 'myvalue'}

# Generated at 2022-06-13 02:18:27.453179
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.compat.tests import unittest

    class TestGetSysctl(unittest.TestCase):

        def setUp(self):
            self.sysctl = '/sbin/sysctl'
            self.module = AnsibleModule(
                argument_spec=dict(),
                supports_check_mode=True
            )
            self.module.run_command = mock_run_command
            self.module.get_bin_path = lambda s: s

        def test_get_sysctl(self):
            prefix = 'net.ipv6'
            sysctl = get_sysctl(self.module, prefix)
            self.assertIn(prefix + '.autoconf', sysctl)

# Generated at 2022-06-13 02:18:28.883071
# Unit test for function get_sysctl
def test_get_sysctl():
    pass

# Generated at 2022-06-13 02:18:32.346400
# Unit test for function get_sysctl
def test_get_sysctl():

    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode=True
    )

    sysctl = get_sysctl(module, 'vm.watermark_scale_factor')
    assert sysctl == {'vm.watermark_scale_factor': '1024'}

# Generated at 2022-06-13 02:18:41.605633
# Unit test for function get_sysctl
def test_get_sysctl():
    import shlex
    from ansible.module_utils.basic import AnsibleModule


# Generated at 2022-06-13 02:18:50.196714
# Unit test for function get_sysctl
def test_get_sysctl():
    assert get_sysctl(sysctl_cmd='/bin/sysctl', prefixes=['-n', 'vm.swappiness']) == {'vm.swappiness': '60'}
    assert get_sysctl(sysctl_cmd='/bin/sysctl', prefixes=['-n', 'vm.swappiness', '-n', 'vm.overcommit_memory']) == {'vm.swappiness': '60', 'vm.overcommit_memory': '0'}
    assert get_sysctl(sysctl_cmd='/bin/sysctl', prefixes=['-e', '-n', 'vm.swappiness']) == {'vm.swappiness': '60'}

# Generated at 2022-06-13 02:19:00.032423
# Unit test for function get_sysctl
def test_get_sysctl():
    import ansible.module_utils.basic

    module = ansible.module_utils.basic.AnsibleModule(
        argument_spec=dict()
    )
    module.get_bin_path = lambda x: 'systemctl'

    class TestRunCommand():
        def __init__(self, rc, output):
            self.rc = rc
            self.output = output

        def run_command(self, cmd, check_rc=True):
            return self.rc, self.output, ''

    import platform
    if platform.system() == 'FreeBSD':
        output = 'dev.apic.ipi.enable: 0\n' \
                 'dev.apic.ipi.early_eoi: 1'
        test_run_command = TestRunCommand(0, output)

# Generated at 2022-06-13 02:19:03.678274
# Unit test for function get_sysctl
def test_get_sysctl():
    cmd = 'sysctl -A'
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    stdout = stdout.decode('utf-8')
    stderr = stderr.decode('utf-8')
    rc = p.returncode
    print(rc, stdout, stderr)

# Generated at 2022-06-13 02:19:13.510510
# Unit test for function get_sysctl
def test_get_sysctl():
    import sys
    import mock

    m = mock.Mock()

    class MockModule(object):
        def run_command(self, cmd):
            cmd = m.run_command(cmd)
            return cmd
        def get_bin_path(self, cmd):
            cmd = m.get_bin_path(cmd)
            return cmd
        def warn(self, msg):
            pass

    m.get_bin_path.return_value = '/usr/sbin/sysctl'
    m.run_command.return_value = 0, 'net.inet.ip.forwarding: 1\net.inet.ip.redirect: 0', ''

    module = MockModule()
    results = get_sysctl(module, ['net.inet.ip'])
    assert results['net.inet.ip.forwarding'] == '1'