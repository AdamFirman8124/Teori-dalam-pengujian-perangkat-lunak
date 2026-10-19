

# Generated at 2022-06-13 02:09:17.094928
# Unit test for function get_sysctl
def test_get_sysctl():
    assert get_sysctl('') == {}

# Generated at 2022-06-13 02:09:28.421434
# Unit test for function get_sysctl
def test_get_sysctl():
    sysctl = dict()
    sysctl['kern.ipc.semmni'] = '32'
    sysctl['kern.ipc.semmns'] = '256'
    sysctl['kern.ipc.semmnu'] = '32'
    sysctl['kern.ipc.semmsl'] = '32'
    sysctl['kern.ipc.semopm'] = '100'
    sysctl['kern.ipc.shmall'] = '2048'

    prefixes = ['kern.ipc.semmni', 'kern.ipc.semmns', 'kern.ipc.semmnu',
                'kern.ipc.semmsl', 'kern.ipc.semopm', 'kern.ipc.shmall']


# Generated at 2022-06-13 02:09:32.532243
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec=dict())
    sysctl = get_sysctl(module, ['kern.ostype'])
    assert dict(kern_ostype='Darwin') == sysctl

# Generated at 2022-06-13 02:09:37.805124
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule

    prefixes = ['kernel.hostname', 'kernel.osrelease', 'kernel.version']

    # Minimal AnsibleModule
    module = AnsibleModule(argument_spec={}, supports_check_mode=False)

    # Get sysctl values
    sysctl = get_sysctl(module, prefixes)

    # Check hostname
    if sysctl['kernel.hostname'] != 'vagrant-ubuntu-trusty-64':
        raise AssertionError('sysctl missing hostname')

    # Check osrelease
    if sysctl['kernel.osrelease'] != '3.13.0-36-generic':
        raise AssertionError('sysctl missing osrelease')

# Generated at 2022-06-13 02:09:47.641979
# Unit test for function get_sysctl

# Generated at 2022-06-13 02:09:57.584057
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat.mock import MagicMock as mock
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat.mock import patch

    mock_module = mock()

    with patch('ansible_collections.notstdlib.moveitallout.plugins.module_utils.basic.get_platform') as mock_platform:
        mock_platform.return_value = 'FreeBSD'
        get_sysctl(mock_module, ['hw.physmem'])
        mock_module.run_command.assert_called_with(['/sbin/sysctl', 'hw.physmem'])


# Generated at 2022-06-13 02:10:07.244742
# Unit test for function get_sysctl

# Generated at 2022-06-13 02:10:08.999935
# Unit test for function get_sysctl
def test_get_sysctl():
    module = DummyAnsibleModule()
    result = get_sysctl(module, ['net.ipv4.conf.all.forwarding'])
    assert result['net.ipv4.conf.all.forwarding'] == '0'


# Generated at 2022-06-13 02:10:11.839574
# Unit test for function get_sysctl
def test_get_sysctl():
    module = type('Module', (object,), {})
    sysctl = get_sysctl(module, ['kern.sched.preempt_thresh'])
    assert len(sysctl.keys()) == 1
    assert sysctl['kern.sched.preempt_thresh'] == '160'

# Generated at 2022-06-13 02:10:22.223312
# Unit test for function get_sysctl
def test_get_sysctl():
    class FakeModule():
        def __init__(self):
            self.run_command_count = 0

        def get_bin_path(self, arg):
            return 'sysctl'

        def run_command(self, arg):
            assert arg[0] == 'sysctl'
            res = self.run_command_results[self.run_command_count]
            self.run_command_count += 1
            return res

        def warn(self, arg):
            pass

    fm = FakeModule()

# Generated at 2022-06-13 02:10:38.237258
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule

    class MockModule(object):
        def __init__(self):
            self.run_command_args = []
            self.run_command_rcs = []
            self.run_command_exceptions = []

        def get_bin_path(self, path, opt_dirs=[]):
            return path

        def run_command(self, args, check_rc=True, close_fds=True, executable=None, data=None, binary_data=False, path_prefix=None, cwd=None, use_unsafe_shell=False, prompt_regex=None):
            self.run_command_args.append(args)

# Generated at 2022-06-13 02:10:48.237196
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )

    prefix = 'kernel.hostname'
    sysctl = get_sysctl(module, [prefix])

    assert len(sysctl.keys()) == 1
    assert prefix in sysctl
    assert sysctl[prefix] == 'localhost.localdomain'

    # Test prefix with a wildcard
    sysctl = get_sysctl(module, [prefix[:-9] + '*'])
    assert len(sysctl.keys()) == 1
    assert sysctl[prefix] == 'localhost.localdomain'


# Generated at 2022-06-13 02:10:51.561247
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(argument_spec=dict(prefixes=dict(required=True)))
    sysctl = get_sysctl(module, prefixes=['net.ipv4.ip_forward'])
    assert sysctl == {'net.ipv4.ip_forward': '1'}

# Generated at 2022-06-13 02:11:02.226711
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(argument_spec=dict(prefixes=dict(required=False, type='list'),
                                              sysctl_path=dict(required=False, type='str'),
                                              fail_on_missing=dict(required=False, type='bool', default=False)),
                           supports_check_mode=True)
    sysctl_cmd = module.get_bin_path('sysctl')
    module.params['sysctl_path'] = sysctl_cmd
    sysctl = {
        'fs.file-max': '18446744073709551615',
    }
    module.run_command = MagicMock(return_value=(0, "fs.file-max = 18446744073709551615\n", ''))

# Generated at 2022-06-13 02:11:05.880167
# Unit test for function get_sysctl
def test_get_sysctl():
    import ansible.module_utils.basic
    base_module = ansible.module_utils.basic.AnsibleModule(argument_spec={})
    assert get_sysctl(base_module, ['vm.swappiness']) == {'vm.swappiness' : '10'}

# Generated at 2022-06-13 02:11:09.960090
# Unit test for function get_sysctl
def test_get_sysctl():

    assert get_sysctl({'run_command': (0, 'foo = bar\nbaz = boo', None)}, ['foo', 'baz']) == {'foo': 'bar', 'baz': 'boo'}

    assert get_sysctl({'run_command': (1, None, None)}, ['foo', 'baz']) == {}

    assert get_sysctl({'run_command': (1, None, None)}, []) == {}

    assert get_sysctl({'run_command': (0, 'foo = bar', None)}, []) == {}

# Generated at 2022-06-13 02:11:18.996978
# Unit test for function get_sysctl
def test_get_sysctl():
    # import module snippets
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict()
    )

    # set up test cases, only using functionality that is exercised in the function being
    # tested so we can keep this test case small and fast

# Generated at 2022-06-13 02:11:21.913576
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(argument_spec=dict())
    result = get_sysctl(module, ['kernel.ostype'])
    assert 'kernel.ostype' in result

# Generated at 2022-06-13 02:11:27.387080
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule

    test_module = AnsibleModule(argument_spec={})
    test_module.run_command = lambda x: (0, 'foo = bar\nhello = world\n', '')

    test_dict = get_sysctl(test_module, ['foo', 'hello'])
    assert test_dict['foo'] == 'bar'
    assert test_dict['hello'] == 'world'

# Generated at 2022-06-13 02:11:33.113600
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    prefixes = ['test_ansible',]
    ret = get_sysctl(module, prefixes)
    assert(ret['test_ansible.string'] == 'some_value')
    assert(ret['test_ansible.int'] == '42')
    assert(ret['test_ansible.bool'] == '1')

# Generated at 2022-06-13 02:11:50.241892
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(
        argument_spec=dict()
    )
    p1 = 'net.ipv4'
    p2 = 'net.ipv6'

# Generated at 2022-06-13 02:11:57.294426
# Unit test for function get_sysctl
def test_get_sysctl():
    module = mock.MagicMock()
    prefixes = ["net.ipv4.tcp_keepalive_time"]

    distro = mock.MagicMock()
    distro.name = 'FreeBSD'

# Generated at 2022-06-13 02:12:07.866200
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule
    def mocked_run_command(cmd, **kwargs):
        out = b'kern.ipc.shmall: 4194304\n' \
              b'kern.usermount: 1\n' \
              b'kern.ipc.shmmax: 536870912\n' \
              b'kern.ipc.shmseg: 1024\n'
        rc = 0
        err = b''
        return rc, out, err

    def mocked_get_bin_path(name):
        return name

    module = AnsibleModule(argument_spec=dict(prefixes=dict(type='list', default=[])))
    module.run_command = mocked_run_command
    module.get_bin_path = mocked_get_bin

# Generated at 2022-06-13 02:12:12.905097
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(argument_spec={'prefixes': dict(type='list'), 'path': dict(type='path')})

    sysctl_values = get_sysctl(module, (sysctl_path,))

    assert sysctl_values['kernel.hostname'] == 'test'
    assert sysctl_values['kernel.domainname'] == 'example.com'

# Generated at 2022-06-13 02:12:20.565815
# Unit test for function get_sysctl
def test_get_sysctl():
    module = type('module', (object,), {
        'run_command': lambda self, cmd: (0, 'Setting\tkernel.hostname = localhost\nSetting\tkernel.sysrq = 1\nSetting\tkernel.core_pattern = core', ''),
        'get_bin_path': lambda self, bin: 'sysctl'
    })()

    assert get_sysctl(module, ['kernel.hostname']) == {'kernel.hostname': 'localhost'}
    assert get_sysctl(module, ['kernel.sysrq']) == {'kernel.sysrq': '1'}
    assert get_sysctl(module, ['kernel.core_pattern']) == {'kernel.core_pattern': 'core'}

# Generated at 2022-06-13 02:12:26.948060
# Unit test for function get_sysctl
def test_get_sysctl():
    module = type('', (), {})()
    module.get_bin_path = lambda *args: 'sysctl'

# Generated at 2022-06-13 02:12:31.306307
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec=dict())
    sysctl = get_sysctl(module, ['vm.swappiness'])
    assert sysctl == {u'vm.swappiness': u'30'}


# Generated at 2022-06-13 02:12:39.123860
# Unit test for function get_sysctl
def test_get_sysctl():
    # test_module is required for unit testing
    #
    # https://github.com/ansible/ansible/blob/devel/lib/ansible/module_utils/basic.py#L1674
    from ansible.module_utils.basic import AnsibleModule
    import os

    module = AnsibleModule(
        argument_spec = dict()
    )


# Generated at 2022-06-13 02:12:40.599978
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)

    sysctl = get_sysctl(module, ['kernel.hostname'])
    assert 'kernel.hostname' in sysctl

# Generated at 2022-06-13 02:12:49.733546
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.six.moves import StringIO

    # Gather input arguments
    sysctl_cmd = "sysctl"

# Generated at 2022-06-13 02:13:05.607794
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec=dict())
    assert len(get_sysctl(module, ['kernel.version'])) > 0

# Generated at 2022-06-13 02:13:10.426892
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec=dict())


# Generated at 2022-06-13 02:13:21.306054
# Unit test for function get_sysctl
def test_get_sysctl():
    sysctl = {
        "net.ipv4.ip_forward": "1",
        "net.ipv4.conf.all.accept_redirects": "0",
        "net.ipv4.conf.default.accept_redirects": "0",
        "net.ipv4.conf.all.secure_redirects": "1",
        "net.ipv4.conf.default.secure_redirects": "1",
        "net.ipv4.conf.all.send_redirects": "1",
        "net.ipv4.conf.default.send_redirects": "1"
    }


# Generated at 2022-06-13 02:13:22.784716
# Unit test for function get_sysctl
def test_get_sysctl():
    assert get_sysctl('a.debug') == '0'

# Generated at 2022-06-13 02:13:32.525131
# Unit test for function get_sysctl
def test_get_sysctl():
    import ansible.module_utils.basic
    m = ansible.module_utils.basic.AnsibleModule(
        argument_spec = dict(
            prefixes = dict(type='list', required=True),
        ),
    )
    m.get_bin_path = lambda x: x

    result = get_sysctl(m, ['prefix'])
    assert result == dict(kernel='prefix')

    result = get_sysctl(m, ['prefix.key'])
    assert result == dict(kernel_prefix='key')

    result = get_sysctl(m, ['prefix', 'prefix.key'])
    assert result == dict(kernel='prefix', kernel_prefix='key')

    result = get_sysctl(m, ['prefix.key', 'prefix'])

# Generated at 2022-06-13 02:13:36.538888
# Unit test for function get_sysctl
def test_get_sysctl():
    import module_utils.systemd

    module = module_utils.systemd.SystemdDummyModule()
    res = get_sysctl(module, ["vm.swappiness", "vm.dirty_background_ratio"])
    assert res["vm.swappiness"] == '60'
    assert res["vm.dirty_background_ratio"] == '10'

# Generated at 2022-06-13 02:13:44.036895
# Unit test for function get_sysctl
def test_get_sysctl():
    import sys
    import tempfile

# Generated at 2022-06-13 02:13:49.031737
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule

    result = get_sysctl(AnsibleModule(dict()), ['kern.boottime'])

    assert(result['kern.boottime'])

    result = get_sysctl(AnsibleModule(dict()), ['vm.swappiness'])

    assert(result['vm.swappiness'])

# vim: ai et ts=4 sts=4 sw=4

# Generated at 2022-06-13 02:13:55.209963
# Unit test for function get_sysctl
def test_get_sysctl():

    module = MockModule()
    sysctl_cmd = module.get_bin_path('sysctl')

    rc = 0
    out = '''
kern.ipc.maxsockbuf: 8388608
kern.ipc.somaxconn: 128
kern.maxclusters: 8192
kern.maxproc: 2706
kern.maxprocperuid: 2502
kern.maxusers: 2048
kern.maxvnodes: 353332
kern.random.fortuna.pool.size: 32
kern.random.fortuna.reseed.interval: 0
kern.random.fortuna.reseed.threshold: 256
'''


# Generated at 2022-06-13 02:14:02.468860
# Unit test for function get_sysctl
def test_get_sysctl():
    # Import ansible and module_utils
    import ansible.module_utils
    import ansible.module_utils.basic
    import ansible.module_utils.common.sysctl

    # Import mock and other required stuff
    import mock
    import types

    # Create mock object
    module = mock.MagicMock()

    # Create mock object to replace module.run_command
    rc = 0

# Generated at 2022-06-13 02:14:40.430132
# Unit test for function get_sysctl
def test_get_sysctl():
    # This function is not directly testable but
    # test_get_sysctlv should test by calling get_sysctl
    # function and asserting with expected values
    pass


# Generated at 2022-06-13 02:14:47.686400
# Unit test for function get_sysctl
def test_get_sysctl():

    # get module_utils
    import ansible.module_utils
    import ansible.module_utils.basic

    class SysctlTestException(Exception):
        pass

    # Mock run_commands

# Generated at 2022-06-13 02:14:53.421406
# Unit test for function get_sysctl
def test_get_sysctl():
    """
    Test function to validate if get_sysctl function is returning
    expected result.
    """
    sysctl_cmd = "{{ ansible_sysctl.bin_path }}"
    cmd = [sysctl_cmd]
    cmd.extend(['net.ipv4.tcp_keepalive_time'])
    result = {u'net.ipv4.tcp_keepalive_time': u'7200'}
    assert result == get_sysctl(module, cmd)
    return result

# Generated at 2022-06-13 02:14:55.350795
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(argument_spec=dict())

    sysctls = get_sysctl(module, [])
    assert sysctls['kern.ostype'] == 'Darwin'

# Generated at 2022-06-13 02:14:57.014775
# Unit test for function get_sysctl
def test_get_sysctl():
    sysctl_output = 'net.ipv4.conf.default.rp_filter = 1'

    sysctl_dict = dict(sysctl_output.split('='))

    assert(sysctl_dict[sysctl_output.split('=')[0]] == sysctl_output.split('=')[1].strip())

# Generated at 2022-06-13 02:14:59.671122
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(argument_spec=dict())

    sysctl = get_sysctl(module, [])
    assert sysctl

    sysctl = get_sysctl(module, ["kernel.hostname"])
    assert sysctl["kernel.hostname"]

# Generated at 2022-06-13 02:15:00.835841
# Unit test for function get_sysctl
def test_get_sysctl():
    module = None
    assert get_sysctl(module, ['kern.boottime']).get('kern.boottime')



# Generated at 2022-06-13 02:15:09.837009
# Unit test for function get_sysctl
def test_get_sysctl():
    class MockAnsibleModule(object):
        def __init__(self, out, err):
            self.out = out
            self.err = err

        def run_command(self, cmd):
            return 0, self.out, self.err

        def get_bin_path(self, cmd):
            return '/sbin/%s' % cmd

        def warn(self, msg):
            pass


# Generated at 2022-06-13 02:15:15.580983
# Unit test for function get_sysctl
def test_get_sysctl():
    class MockModule(object):
        def __init__(self):
            self.rc = 0
            self.out = """
net.ipv4.conf.all.rp_filter = 1
net.ipv4.tcp_timestamps = 0
net.ipv6.conf.default.use_tempaddr = 2
net.ipv6.conf.default.accept_ra = 2
net.ipv4.conf.default.accept_redirects = 0

net.bridge.bridge-nf-call-iptables = 1
net.bridge.bridge-nf-call-ip6tables = 1
"""
            self.err = ''

        def get_bin_path(self, cmd):
            return '/bin/%s' % cmd

        def run_command(self, cmd):
            return self.rc,

# Generated at 2022-06-13 02:15:19.789075
# Unit test for function get_sysctl
def test_get_sysctl():
    module = FakeModule()
    sysctl = get_sysctl(module, ['vm.swappiness', 'net.ipv4.tcp_tw_recycle'])
    assert sysctl['vm.swappiness'] == '0'
    assert sysctl['net.ipv4.tcp_tw_recycle'] == '1'


# Generated at 2022-06-13 02:16:29.535594
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={'prefixes': {'type': 'list'}})
    module.params = {'prefixes':['kern','net.link']}
    assert get_sysctl(module, module.params['prefixes'])['kern.version'] == 'OpenBSD 5.9 (GENERIC) #474: Wed Sep 21 19:38:52 MDT 2016     deraadt@amd64.openbsd.org:/usr/src/sys/arch/amd64/compile/GENERIC'

# Generated at 2022-06-13 02:16:38.026042
# Unit test for function get_sysctl
def test_get_sysctl():
    prefixes = ['net.ipv4.ip_forward', 'vm.max_map_count']

    sysctl_cmd = '/sbin/sysctl'
    cmd = [sysctl_cmd]
    cmd.extend(prefixes)

    rc = 0
    out = 'net.ipv4.ip_forward = 1\nvm.max_map_count = 262144'
    err = ''
    sysctl = dict()

    if rc == 0:
        key = ''
        value = ''
        for line in out.splitlines():
            if not line.strip():
                continue


# Generated at 2022-06-13 02:16:43.033085
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.common.collections import ImmutableDict
    sysctl = get_sysctl(ImmutableDict(
        module_args = dict(),
        get_bin_path = lambda path: '/sbin/sysctl',
        params = dict()),
        prefixes = ['net.ipv4.ip_forward', 'net.ipv4.route.flush'])

    assert 'net.ipv4.ip_forward' in sysctl
    assert 'net.ipv4.route.flush' in sysctl
    assert sysctl['net.ipv4.ip_forward'] == '0'
    assert sysctl['net.ipv4.route.flush'] == '1'
    return

# Generated at 2022-06-13 02:16:44.253825
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(argument_spec={})
    prefixes = ['fs.file-max']
    assert get_sysctl(module, prefixes) == {'fs.file-max': '25927457'}

# Generated at 2022-06-13 02:16:48.421388
# Unit test for function get_sysctl
def test_get_sysctl():
    # No error handling necessary, it is handled within the tested function
    sysctl_cmd = 'sysctl'
    cmd = [sysctl_cmd]
    cmd.extend('-a')

    sysctl = dict()

    key = ''
    value = ''
    for line in test_output.splitlines():
        if not line.strip():
            continue

        if line.startswith(' '):
            # handle multiline values, they will not have a starting key
            # Add the newline back in so people can split on it to parse
            # lines if they need to.
            value += '\n' + line
            continue

        if key:
            sysctl[key] = value.strip()


# Generated at 2022-06-13 02:16:51.854714
# Unit test for function get_sysctl
def test_get_sysctl():
    assert get_sysctl({'wrong': '', 'get_bin_path': lambda x: '/bin/sysctl', 'run_command': lambda x: (0, '', '')}, []) == {}

# Generated at 2022-06-13 02:16:59.825013
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={})

    sysctl = get_sysctl(module, prefixes=['vm', 'swap'])

    assert sysctl['vm.swappiness'] == '30'
    assert sysctl['vm.swappiness'] == module.run_command(['sysctl', '-n', 'vm.swappiness'])[1].strip()
    assert sysctl['vm.swapusage'] == 'total = 3072.00M  used = 0.00M  free = 3072.00M'
    assert sysctl['vm.swapusage'] == module.run_command(['sysctl', '-n', 'vm.swapusage'])[1].strip()

# Generated at 2022-06-13 02:17:05.912951
# Unit test for function get_sysctl
def test_get_sysctl():
    import warnings
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        import ansible.module_utils.basic
        import ansible.module_utils.system

        class TestModule(object):
            def __init__(self):
                self.fail_json = ansible.module_utils.basic.AnsibleModule.fail_json
                self.run_command = ansible.module_utils.system.run_command

            def get_bin_path(self, arg):
                return 'tests/modules'

        class TestParser(object):
            def __init__(self, output):
                self.output = output

            def splitlines(self):
                return self.output

        module = TestModule()

# Generated at 2022-06-13 02:17:15.174713
# Unit test for function get_sysctl
def test_get_sysctl():

    class FakeModule():
        def get_bin_path(self, name):
            return name

        def run_command(self, cmd):
            class Result():
                def __init__(self, stdout, stderr, rc):
                    self.stdout = stdout
                    self.stderr = stderr
                    self.rc = rc
                def __getattr__(self, key):
                    return self.__dict__[key]

            if cmd == ['sysctl', '-n']:
                return Result('key1 = foo\nkey2 = bar\n', '', 0)
            if cmd == ['sysctl', '-p']:
                return Result('key1 = foo\nkey2 = bar\n', '', 0)

# Generated at 2022-06-13 02:17:19.381323
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(argument_spec={})
    prefixes = ['vm.overcommit_memory', 'vm.overcommit_ratio', 'vm.swappiness']
    sysctl = get_sysctl(module, prefixes)
    assert(sysctl)
    for prefix in prefixes:
        assert(prefix in sysctl.keys())
    assert(sysctl['vm.overcommit_memory'] == '0')
    assert(sysctl['vm.overcommit_ratio'] == '50')
    assert(sysctl['vm.swappiness'] == '60')
