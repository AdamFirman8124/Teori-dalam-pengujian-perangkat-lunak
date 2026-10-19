

# Generated at 2022-06-13 02:09:17.250761
# Unit test for function get_sysctl
def test_get_sysctl():
    module = ansible_module_get_sysctl()
    prefixes = ['net.ipv4.tcp_rmem']
    get_sysctl(module, prefixes)

    out = module.resp.stdout
    assert 'net.ipv4.tcp_rmem = 4096 16384 4194304' in out



# Generated at 2022-06-13 02:09:20.963548
# Unit test for function get_sysctl
def test_get_sysctl():
    assert get_sysctl('', ['fs.file-max']) == {'fs.file-max': '1024960'}

# Generated at 2022-06-13 02:09:26.006464
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec=dict(prefixes='all'))
    sysctl_result = get_sysctl(module, ['kern.hostname'])
    # We don't check the exact result as it depends on the underlying system
    assert 'kern.hostname' in sysctl_result

# Generated at 2022-06-13 02:09:35.513091
# Unit test for function get_sysctl
def test_get_sysctl():
    import tempfile

    class ModuleMock():
        def __init__(self):
            self.params = {
                'prefix': ['net']
            }
            self.fail_json = None
            self.run_command = None

        def get_bin_path(self, var):
            return '/sbin/sysctl'

        def exit_json(self, *args, **kwargs):
            pass

    class RunCommandMock():
        def __init__(self):
            self.command = []
            self.stdout = ''
            self.stderr = ''

        def __call__(self, command, *args, **kwargs):
            self.command = command
            if command[1] == 'vm':
                with open(tempfile.mkstemp()[1], 'w') as f:
                    f

# Generated at 2022-06-13 02:09:42.609187
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule
    # Setup module
    module = AnsibleModule(argument_spec={})
    module.get_bin_path = lambda *args: '/proc/sys/kernel/hostname'
    module.run_command = lambda *args: (0, 'hostname.hostname', '')
    # Test function
    assert get_sysctl(module, []) == { 'hostname.hostname': 'hostname' }

# Generated at 2022-06-13 02:09:47.980173
# Unit test for function get_sysctl
def test_get_sysctl():
    module = MockAnsibleModule()
    assert get_sysctl(module, ['fs.file-nr'])['fs.file-nr'] == '10240   0   10240'
    assert get_sysctl(module, ['fs.file-nr','fs.file-max'])['fs.file-max'] == '2621440'
    assert get_sysctl(module, ['kernel.randomize_va_space'])['kernel.randomize_va_space'] == '2'


# Generated at 2022-06-13 02:09:52.351962
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(argument_spec=dict())

    assert get_sysctl(module, ['kern']) == {
        'kern.ostype': 'Darwin',
        'kern.osrelease': '17.7.0'
    }


# Generated at 2022-06-13 02:09:59.839208
# Unit test for function get_sysctl
def test_get_sysctl():
    def myrun_command(cmd):
        return (0, 'kernel.printk = 3\nkernel.hostname = oups\nnet.ipv4.ip_forward = 1\n', '')
    def mywarn(msg):
        print(msg)
    class MyModule:
        def __init__(self):
            self.verbose = 1
        def get_bin_path(self, prog):
            return prog
        def run_command(self, cmd):
            return myrun_command(cmd)
        def warn(self, msg):
            mywarn(msg)

    mymodule = MyModule()
    myprefixes=['kernel.printk']
    res = get_sysctl(mymodule, myprefixes)
    assert(res == {'kernel.printk': '3'})

# Generated at 2022-06-13 02:10:01.580413
# Unit test for function get_sysctl
def test_get_sysctl():
    assert get_sysctl('', ['']) == {}



# Generated at 2022-06-13 02:10:04.425914
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(supports_check_mode=True)
    result = get_sysctl(module, ['debug.exception-trace'])
    assert result['debug.exception-trace'] == '0'

# Generated at 2022-06-13 02:10:14.432776
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils import basic

    data = {
      'rc': 0,
      'stdout': """\
net.ipv4.ip_forward = 1
net.ipv4.conf.default.forwarding = 1
net.ipv4.conf.default.proxy_arp = 0
net.ipv4.conf.all.send_redirects = 1
net.ipv4.conf.default.send_redirects = 1
net.ipv4.conf.all.accept_source_route = 0
""",
    }

    module = basic.AnsibleModule(argument_spec=dict())
    module.run_command = lambda *args: data

    assert module.get_bin_path('sysctl') == 'sysctl'


# Generated at 2022-06-13 02:10:22.822116
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )
    sysctl = get_sysctl(module, [])
    assert isinstance(sysctl, dict)
    assert sysctl
    assert 'kernel.hostname' in sysctl
    assert 'kernel.domainname' not in sysctl
    sysctl = get_sysctl(module, ['kernel.domainname'])
    assert isinstance(sysctl, dict)
    assert sysctl
    assert 'kernel.hostname' not in sysctl
    assert 'kernel.domainname' in sysctl

# Generated at 2022-06-13 02:10:24.510808
# Unit test for function get_sysctl
def test_get_sysctl():
    print(get_sysctl(sysctlPrefixes=['vfs.generic.nfs']))

# Generated at 2022-06-13 02:10:31.176939
# Unit test for function get_sysctl
def test_get_sysctl():
    prefixes = ['-n', 'kernel.msgmax']
    sysctl = get_sysctl('', prefixes)
    assert sysctl['kernel.msgmax'] == '65536'

    prefixes = ['-n', 'kernel.msgmax', '-n', 'kernel.msgmnb']
    sysctl = get_sysctl('', prefixes)
    assert sysctl['kernel.msgmax'] == '65536'
    assert sysctl['kernel.msgmnb'] == '65536'

    prefixes = ['-n', 'kernel.shmall']
    sysctl = get_sysctl('', prefixes)
    assert sysctl['kernel.shmall'] == '34359738368'

# Generated at 2022-06-13 02:10:37.058740
# Unit test for function get_sysctl
def test_get_sysctl():
    module = ansible.module_utils.basic.AnsibleModule(
        argument_spec = dict()
    )
    prefixes = ['kernel']
    sysctl = get_sysctl(module, prefixes)
    assert(isinstance(sysctl, dict))
    assert('kernel.sched_yeild_sleep_millisecs' in sysctl)
    assert(sysctl['kernel.sched_yeild_sleep_millisecs'] == '0')

# Generated at 2022-06-13 02:10:43.487170
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule
    # Create a simple module for our script to use
    module = AnsibleModule(argument_spec={})

    sysctl = get_sysctl(module, ['-a'])
    assert 'kernel.usermodehelper.bset' in sysctl
    sysctl = get_sysctl(module, ['dummy.dummy.dummy'])
    assert len(sysctl) == 0

# Generated at 2022-06-13 02:10:52.571361
# Unit test for function get_sysctl
def test_get_sysctl():
    # test for a special value
    module = 'kernel.version: 3.10.0-123.el7.x86_64'
    assert get_sysctl(module, 'kernel.version') == {'kernel.version': '3.10.0-123.el7.x86_64'}
    # test for a full output

# Generated at 2022-06-13 02:11:03.097085
# Unit test for function get_sysctl
def test_get_sysctl():

    import sys
    import os
    import tempfile

    test_prefix = 'net.core.foo'
    test_values = [
        '{0} = 42'.format(test_prefix),
        '{0}.bar = bar'.format(test_prefix),
        '{0}.baz = baz'.format(test_prefix),
        '{0}.froz = froz'.format(test_prefix),
        '{0}.frob = frob',
        '{0}.frobozz = frobozz'.format(test_prefix),
    ]

    test_output = '\n'.join(test_values)

    # Assuming we are in a binding directory when running tests
    bindir = os.path.dirname(os.path.abspath(__file__))
    libdir = os.path.join

# Generated at 2022-06-13 02:11:12.547809
# Unit test for function get_sysctl
def test_get_sysctl():
    for sysctl_line in [
        'key = value',
        'key = value\n',
        'key: value',
        'key: value\n',
        'key=value',
        'key=value\n',
        'key=value\n\n',
        'key: value\n\n'
        ]:
        sysctl_dict = {}

        def run_command(module, cmd):
            cmd_str = ' '.join(cmd)
            if cmd_str == 'sysctl key':
                out = sysctl_line
                rc = 0
            else:
                rc = 1
            return (rc, out, '')

        def get_bin_path(module, name):
            return name

        def warn(module, msg):
            raise Exception(msg)


# Generated at 2022-06-13 02:11:18.873131
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec={})
    params = {
        'kernel.msgmax': '65536',
        'kernel.msgmnb': '65536',
        'kernel.msgmni': '2878',
    }

    def _run_command(args, *args_rest):
        if args[0] == 'sysctl':
            if args_rest[0] == []:
                return (0, '\n'.join([key + ': ' + str(value) for key, value in params.items()]), None)
            else:
                return (0, '\n'.join([key + ': ' + str(value) for key, value in params.items() if key.startswith(args_rest[0][0])]), None)

# Generated at 2022-06-13 02:11:31.647719
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec={}, supports_check_mode=True)

    data = get_sysctl(module, ['fw.*'])
    assert data['fw.verbose_limit'] == '0'
    assert data['fw.enable'] == '0'



# Generated at 2022-06-13 02:11:38.798113
# Unit test for function get_sysctl
def test_get_sysctl():

    # Basic test with a single keyword
    mock_module = MockModule()
    mock_module.run_command.return_value = (0, "kern.random.foo = bar\n", "")
    sysctl = get_sysctl(mock_module, ["kern.random.foo"])
    mock_module.run_command.assert_called_with(["/bin/sysctl", "kern.random.foo"])
    assert sysctl == {u"kern.random.foo": u"bar"}

    # Test with multiple keywords that are not found in sysctl
    mock_module = MockModule()
    mock_module.run_command.return_value = (0, "", "")

# Generated at 2022-06-13 02:11:49.023802
# Unit test for function get_sysctl
def test_get_sysctl():

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.basic import _get_bin_path

    class MockModule(AnsibleModule):
        def __init__(self):
            self.module = AnsibleModule(
                    argument_spec=dict(),
                    supports_check_mode=True)

        def run_command(self, cmd):
            if 'sysctl' in cmd:
                return 0, 'vm.swappiness: 60\nvm.dirty_background_ratio: 10', ''
            else:
                return 1, '', ''

        def get_bin_path(self, exe):
            return _get_bin_path(exe)

        def warn(self, msg):
            return msg

    m = MockModule()

# Generated at 2022-06-13 02:11:56.564156
# Unit test for function get_sysctl
def test_get_sysctl():
    import sysctl

    # A known good sysctl prefix (in the majority of distros)
    sysctls = sysctl.get_sysctl(sysctl, [ 'net.ipv4.route' ])

    # We expect to get at least one key:value back
    assert sysctls is not None
    assert len(sysctls) > 0

    # We expect to get a key that starts with net.ipv4.route.
    assert any(k.startswith('net.ipv4.route') for k in sysctls.keys())

    # We expect to get a value that is not empty string
    assert all(v != '' for v in sysctls.values())

    # Test that passing a bad sysctl prefix returns an empty dict

# Generated at 2022-06-13 02:12:02.520345
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(argument_spec={})
    sysctl = get_sysctl(module, prefixes=["kernel.hostname"])
    assert sysctl.get('kernel.hostname', u'') != ""

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 02:12:11.049663
# Unit test for function get_sysctl
def test_get_sysctl():

    import ansible.module_utils.basic

    class TestModule(ansible.module_utils.basic.AnsibleModule):

        def __init__(self, *args, **kwargs):
            super(TestModule, self).__init__(*args, **kwargs)

        def exit_json(self, *args, **kwargs):
            pass

        def fail_json(self, *args, **kwargs):
            pass

    module = TestModule()
    sysctl = get_sysctl(module, ['vm.overcommit_memory'])
    assert sysctl['vm.overcommit_memory'] == '0'

# Generated at 2022-06-13 02:12:16.234521
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(
        argument_spec=dict(
            prefixes=dict(default='kernel.hostname',type='list')
        )
    )

    # returns dict of sysctl
    module.exit_json(**get_sysctl(module,module.params['prefixes']))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 02:12:18.829405
# Unit test for function get_sysctl
def test_get_sysctl():
    """Test that get_sysctl is working as expected"""
    assert get_sysctl({'get_bin_path': lambda x: x}, ['kernel.hostname']) == {u'kernel.hostname': u'localhost'}

# Generated at 2022-06-13 02:12:25.531613
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(
        argument_spec=dict(),
    )

    assert module.get_bin_path.return_value == '/bin/sysctl'
    assert module.run_command.return_value == (0, 'kernel.sched_compat_yield: 0\nnet.core.bpf_jit_enable: 1\nkernel.sched_autogroup_enabled: 1\nkernel.sched_window_stats_policy: 1\nvm.block_dump: 0\nnet.core.busy_poll: 0\nfs.protected_fifos: 0\n', '')

    result = get_sysctl(module, prefixes=['kernel', 'net.core'])

# Generated at 2022-06-13 02:12:31.164795
# Unit test for function get_sysctl
def test_get_sysctl():
    import platform

    testvals = {}
    if platform.system() == 'Darwin':
        testvals['kern.hostname'] = 'macmini.local'
    elif platform.system() == 'Linux':
        testvals['kernel.hostname'] = 'localhost'

    assert get_sysctl(testvals.keys()) == testvals



# Generated at 2022-06-13 02:12:50.747276
# Unit test for function get_sysctl
def test_get_sysctl():
    import sysctl

    sysctl.main()
    assert sysctl.get_sysctl(sysctl, ['net.ipv4.ip_forward']) == {'net.ipv4.ip_forward': '1'}

# Generated at 2022-06-13 02:12:58.047487
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule
    import sys

    module = AnsibleModule(
        argument_spec = dict(),
    )

    module.bin_path = dict(sysctl='/bin/sysctl')

    # Make sure that empty prefixes return an empty dict
    sysctl = get_sysctl(module, [])
    assert len(sysctl) == 0

    # This command returns a number of sysctl variables.  One of them is:
    # kernel.pid_max = 4194303
    sysctl = get_sysctl(module, ['kernel'])
    assert len(sysctl) > 0
    assert sysctl['kernel.pid_max'] == '4194303'



# Generated at 2022-06-13 02:12:59.946711
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(argument_spec=dict())
    sysctl = get_sysctl(module, ('kernel', 'osrelease'))
    assert len(sysctl) > 0

# Generated at 2022-06-13 02:13:06.348740
# Unit test for function get_sysctl
def test_get_sysctl():
    test_dict = {'net.ipv4.ip_forward': '0', 'net.ipv4.conf.all.forwarding': '0', 'net.ipv4.conf.default.forwarding': '0', 'net.ipv4.conf.lo.forwarding': '0', 'net.ipv4.conf.eth0.forwarding': '0'}

    test_cmd = ['sysctl', 'net.ipv4.ip_forward', 'net.ipv4.conf.all.forwarding', 'net.ipv4.conf.default.forwarding', 'net.ipv4.conf.lo.forwarding', 'net.ipv4.conf.eth0.forwarding']

    result_dict = dict()


# Generated at 2022-06-13 02:13:12.818060
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(
        argument_spec=dict()
    )

    command = 'sysctl -a'

    # Test get_sysctl with IPv4 address
    lines = (
        'net.ipv4.ip_forward = 0',
        'net.ipv4.conf.all.accept_redirects = 0',
        'net.ipv4.conf.all.send_redirects = 0'
    )

    out = run_command(module, command)

    assert(get_sysctl(module, lines) == out)

# Generated at 2022-06-13 02:13:23.204042
# Unit test for function get_sysctl
def test_get_sysctl():
    class AnsibleModule:
        def get_bin_path(self, bin):
            return 'sysctl'


# Generated at 2022-06-13 02:13:32.992948
# Unit test for function get_sysctl
def test_get_sysctl():
    module = type('module', (object,), {
        'run_command': lambda self, cmd: (0, 'vm.swappiness = 60\nvm.vfs_cache_pressure = 100', ''),
        'get_bin_path': lambda self, name: name,
    })
    assert get_sysctl(module, ['vm.swappiness']) == {'vm.swappiness': '60'}
    assert get_sysctl(module, ['vm.vfs_cache_pressure', 'vm.swappiness']) == {'vm.vfs_cache_pressure': '100', 'vm.swappiness': '60'}

# Generated at 2022-06-13 02:13:40.932238
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.six.moves import StringIO
    from ansible.module_utils import basic
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils.facts import gather_facts
    ah = basic.AnsibleModule(
        argument_spec=dict(
            prefixes=[dict(type='list', required=True)],
        )
    )


# Generated at 2022-06-13 02:13:48.773089
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict()
    )

    expected = {'kern.ostype': 'FreeBSD',
                'kern.osrelease': '11.1-STABLE',
                'kern.osrevision': '1',
                'kern.boottime': 'Sun Dec 31 16:21:45 2017',
                'kern.hostname': 'testhost.example.com',
                'kern.version': '#0: Thu Dec 21 06:02:32 UTC 2017     root@amd64-builder.daemonology.net:/usr/obj/usr/src/sys/GENERIC'}


# Generated at 2022-06-13 02:13:56.007230
# Unit test for function get_sysctl
def test_get_sysctl():
    class FakeModule(object):
        def __init__(self, result=None):
            self.rc = 0
            self.result = result
            self.cmd = ''
            self.warnings = []

        def run_command(self, cmd):
            self.cmd = ' '.join(cmd)
            if self.rc == 0:
                return self.rc, self.result, ''
            else:
                raise OSError('Command failed!')

        def get_bin_path(self, name, opts=None, required=False):
            if name == 'sysctl':
                return name

        def warn(self, warning):
            self.warnings.append(warning)

    # test returning a valid result

# Generated at 2022-06-13 02:14:45.691891
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils import basic
    import sys

    # output from sysctl taken on a FreeBSD machine
    if sys.version_info < (3, 0):
        from StringIO import StringIO
    else:
        from io import StringIO

# Generated at 2022-06-13 02:14:54.439735
# Unit test for function get_sysctl
def test_get_sysctl():
    module = type('test_get_sysctl', (object,), {})()

# Generated at 2022-06-13 02:14:56.907325
# Unit test for function get_sysctl
def test_get_sysctl():
    module = FakeAnsibleModule()
    sysctl = get_sysctl(module, ['net.core.somaxconn'])
    assert sysctl == {'net.core.somaxconn': '128'}


# Generated at 2022-06-13 02:15:03.014715
# Unit test for function get_sysctl
def test_get_sysctl():
    # Build the test module.
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec=dict())

    # Get the test variables.

# Generated at 2022-06-13 02:15:12.633766
# Unit test for function get_sysctl
def test_get_sysctl():
    """Basic sanity test and validation of the get_sysctl() function."""
    import subprocess
    from ansible.module_utils.pycompat24 import get_exception

    cmd_binary = 'sysctl'
    cmd_prefixes = ['-a']

    # Test a good system call
    cmd = [cmd_binary] + cmd_prefixes
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()

    sysctl = get_sysctl({'run_command': run_command}, cmd_prefixes)
    assert sysctl
    assert len(sysctl) > 1

    # Test a failure by altering the command prefix

# Generated at 2022-06-13 02:15:21.646487
# Unit test for function get_sysctl

# Generated at 2022-06-13 02:15:28.104374
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule


# Generated at 2022-06-13 02:15:34.746678
# Unit test for function get_sysctl
def test_get_sysctl():
    assert get_sysctl(dict(), ['key', 'value']) == dict()
    assert get_sysctl(dict(), ['nokey']) == dict()
    assert get_sysctl(dict(run_command=lambda *a, **kw: (0, 'key = value', '')), ['key']) == dict(key='value')
    assert get_sysctl(dict(run_command=lambda *a, **kw: (0, 'key = value1\nkey = value2', '')), ['key']) == dict(key='value1\nkey = value2')

# Generated at 2022-06-13 02:15:40.306890
# Unit test for function get_sysctl
def test_get_sysctl():
    module = type('module', (), {})
    module.get_bin_path = lambda self, x: '/sbin/sysctl'
    module.run_command = lambda self, x: (0, 'net.ipv4.ip_forward = 1\nnet.ipv4.neigh.default.gc_thresh1 = 128', None)
    module.warn = lambda self, x: None

    sysctl = get_sysctl(module, [])
    assert sysctl['net.ipv4.ip_forward'] == '1'


# Generated at 2022-06-13 02:15:46.932594
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.basic import get_exception


# Generated at 2022-06-13 02:17:25.679721
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(argument_spec=dict(prefixes=dict(required=True, type='list')))

    class AnsibleModuleTest:
        def __init__(self, argument_spec):
            self.params = argument_spec

        def get_bin_path(self, name, opts=None):
            return name

        def run_command(self, cmd):
            return None, "test_key1: test_value1\ntest_key2: test_value2", None

    get_sysctl(AnsibleModuleTest(dict(prefixes=['test_prefix1', 'test_prefix2'])), )

    expected_dict = {'test_key1': 'test_value1', 'test_key2': 'test_value2'}
    assert expected_dict == sysctl

    return sysctl

# Generated at 2022-06-13 02:17:28.025947
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec={'prefixes': dict(type='list', default=['kern.ostype'])})
    results = get_sysctl(module, module.params['prefixes'])
    for k in ['kern.ostype']:
        assert k in results


# Generated at 2022-06-13 02:17:29.106571
# Unit test for function get_sysctl
def test_get_sysctl():
    sysctl = get_sysctl('', [''])
    assert len(sysctl) > 0

# vim:tw=76:ts=4:et:

# Generated at 2022-06-13 02:17:33.674866
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={'prefixes': {'type': 'list', 'required': True}})
    module.params['prefixes'] = [
        'fs.file-max',
        'net.core.wmem_max',
    ]
    module.run_command = lambda *args, **kwargs: (0, 'fs.file-max = 2097152\nnet.core.wmem_max = 16777216', '')
    assert get_sysctl(module, module.params['prefixes']) == {
        'fs.file-max': '2097152',
        'net.core.wmem_max': '16777216'
    }



# Generated at 2022-06-13 02:17:40.362308
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(argument_spec=dict(
        prefixes=dict(type='list', default=['kern.ipc']),
    ))

    sysctl = get_sysctl(module, module.params['prefixes'])

    assert 'kern.ipc.maxsockbuf' in sysctl
    assert sysctl['kern.ipc.maxsockbuf'] == '16777216'

if __name__ == '__main__':
    sysctl = get_sysctl()

    print(sysctl)

# Generated at 2022-06-13 02:17:44.596534
# Unit test for function get_sysctl
def test_get_sysctl():
    import module_utils.basic
    # We need to create a module_utils.basic.AnsibleModule object,
    # and make sure it's params are set to something so our test
    # get_sysctl function will run without error.
    setattr(module_utils.basic.AnsibleModule, 'params', {})
    # The imported module_utils.basic.AnsibleModule object is actually
    # a class, which when invoked returns a new AnsibleModule object.
    module = module_utils.basic.AnsibleModule()
    # Now we can invoke our get_sysctl function on the module_utils.basic.AnsibleModule object
    # we just created.
    out = get_sysctl(module, ['kern.boottime'])
    # The out dictionary should have one element
    assert len(out) == 1


# Generated at 2022-06-13 02:17:51.627626
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec={})

    assert get_sysctl(module, ['kernel.hostname']) == {'kernel.hostname': 'localhost.localdomain'}
    assert get_sysctl(module, ['kernel.domainname', 'kernel.hostname']) == {'kernel.domainname': '(none)', 'kernel.hostname': 'localhost.localdomain'}
    assert get_sysctl(module, []) == {}
    assert get_sysctl(module, ['nothing.here']) == {}
    assert get_sysctl(module, ['nothing.here', 'kernel.hostname']) == {'kernel.hostname': 'localhost.localdomain'}

# Generated at 2022-06-13 02:17:56.336080
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule
    module_args = dict()
    module = AnsibleModule(argument_spec=module_args)
    assert get_sysctl(module, ['net.ipv4.tcp_timestamps']) == {'net.ipv4.tcp_timestamps': '0'}

if __name__ == '__main__':
    test_get_sysctl()

# Generated at 2022-06-13 02:18:04.724544
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec={})
    fake_data = """
    net.ipv4.ip_forward = 1
    net.ipv6.conf.all.forwarding = 0
    """

    def run_command(self, cmd):
        return (0, fake_data, '')

    m = module.AnsibleModule(argument_spec={})
    m.run_command = run_command

    sysctl = get_sysctl(m, ['net.ipv4.ip_forward', 'net.ipv6.conf.all.forwarding'])

    assert sysctl == {'net.ipv4.ip_forward': '1', 'net.ipv6.conf.all.forwarding': '0'}


# Generated at 2022-06-13 02:18:08.993855
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(argument_spec={})
    sysctl = get_sysctl(module, ["kernel.hostname"])
    module.exit_json(changed=False, sysctl=sysctl)

from ansible.module_utils.basic import *
from ansible.module_utils.six import string_types
from ansible.module_utils.parsing.convert_bool import BOOLEANS_TRUE, BOOLEANS_FALSE

try:
    from __main__ import display
except ImportError:
    from ansible.utils.display import Display
    display = Display()

