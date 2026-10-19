

# Generated at 2022-06-13 02:09:19.545276
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(argument_spec={
        'prefixes': {'type': 'list', 'required': True},
    })
    assert get_sysctl(module, ['net.ipv4.ip_forward']) == {'net.ipv4.ip_forward': '1'}
    assert get_sysctl(module, ['net.ipv4.ip_forward', 'net.ipv4.conf.all.forwarding']) == {'net.ipv4.ip_forward': '1',
                                                                                            'net.ipv4.conf.all.forwarding': '1'}

# Generated at 2022-06-13 02:09:26.495039
# Unit test for function get_sysctl
def test_get_sysctl():

    from ansible.module_utils import basic
    from ansible.module_utils.raw import exec_command

    class exec_mock:

        def __init__(self, out, rc=0, err=''):
            self.out = out
            self.err = err
            self.rc = rc

        def __call__(self, *args, **kwargs):
            return self.rc,self.out,self.err
    basic._ANSIBLE_ARGS = None
    module = basic.AnsibleModule(argument_spec={}, supports_check_mode=False)
    module.run_command = exec_command

# Generated at 2022-06-13 02:09:34.174649
# Unit test for function get_sysctl
def test_get_sysctl():
    import contextlib
    import tempfile

    @contextlib.contextmanager
    def fake_sysctl_file(sysctl_key, sysctl_value):
        (fd, path) = tempfile.mkstemp()
        with os.fdopen(fd, 'w') as f:
            f.write('%s\n' % sysctl_key)
            if sysctl_value:
                f.write('%s\n' % sysctl_value)
        yield path
        os.remove(path)

    from ansible.module_utils import basic
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.basic import missing_required_lib
    from ansible.module_utils.parsing.convert_bool import true_false_rep


# Generated at 2022-06-13 02:09:39.981264
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule
    testmodule = AnsibleModule({})
    prefixes = ['net.ipv4.tcp_max_syn_backlog']

    result = get_sysctl(testmodule, prefixes)
    assert len(result) == 1
    assert result['net.ipv4.tcp_max_syn_backlog'] == '1024'



# Generated at 2022-06-13 02:09:48.609730
# Unit test for function get_sysctl
def test_get_sysctl():
    # Test module mock
    class TestModule():
        def __init__(self, run_command_rc, run_command_out):
            self.run_command_rc = run_command_rc
            self.run_command_out = run_command_out
            self.params = {}

        def get_bin_path(self, name):
            return name

        def run_command(self, cmd):
            return self.run_command_rc, self.run_command_out, ''

    # Test cases

# Generated at 2022-06-13 02:09:55.486387
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec=dict())

    rc, out, err = module.run_command(['sysctl', 'net.ipv4.conf.all.rp_filter'])
    assert rc == 0

    sysctl = get_sysctl(module, ['net.ipv4.conf.all.rp_filter'])
    assert sysctl['net.ipv4.conf.all.rp_filter'] == out.strip()

# Generated at 2022-06-13 02:09:59.919826
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils import basic
    import ansible.module_utils.common.sysctl as m_s

    assert m_s.get_sysctl(basic.AnsibleModule(argument_spec={}), ['kernel.hostname']) == { 'kernel.hostname': 'localhost' }

# Generated at 2022-06-13 02:10:04.719946
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec=dict())

    assert get_sysctl(module, ['net.ipv4.ip_forward']) == {'net.ipv4.ip_forward': '0'}
    assert get_sysctl(module, ['does.not.exist']) == dict()

# Generated at 2022-06-13 02:10:11.749475
# Unit test for function get_sysctl

# Generated at 2022-06-13 02:10:22.117495
# Unit test for function get_sysctl
def test_get_sysctl():
    """Functional test for get_sysctl."""
    import os
    import tempfile
    import shutil
    import subprocess

    class FakeModule(object):
        def __init__(self, out=None, warn=None, run_cmd=None):
            self.out = out
            self.run_cmd = run_cmd
            self.warn = warn
            self.debug = lambda g: None

        def get_bin_path(self, name):
            return name

        def run_command(self, cmd):
            return self.run_cmd(cmd)

    out_file = tempfile.NamedTemporaryFile(delete=False)


# Generated at 2022-06-13 02:10:31.636922
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(argument_spec={
        'prefixes': {'type': 'list', 'required': True}
    })

    try:
        sysctl = get_sysctl(module, ["kernel.hostname", "kern.cards.slot_names"])
    except Exception as e:
        module.fail_json(msg=to_text(e))

    module.exit_json(msg=sysctl)



from ansible.module_utils.basic import AnsibleModule
if __name__ == '__main__':
    main()

# Generated at 2022-06-13 02:10:41.824305
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict(),
    )

    module.get_bin_path = lambda x: '/bin/sysctl'

    module.run_command = lambda x: (0, 'vm.swappiness: 60\nvm.overcommit_memory: 0\nvm.panic_on_oom: 0\nvm.overcommit_ratio: 50\nvm.dirty_background_ratio: 3\nvm.dirty_ratio: 40\nvm.dirty_expire_centisecs: 6000\nvm.dirty_writeback_centisecs: 500', '')


# Generated at 2022-06-13 02:10:45.009356
# Unit test for function get_sysctl
def test_get_sysctl():
    assert get_sysctl('test', ['kernel.printk']) == {'kernel.printk': '5 4 1 7'}

# Generated at 2022-06-13 02:10:50.205794
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(argument_spec=dict(
        prefixes = dict(type='list', required=True)
    ), supports_check_mode=True)
    inp = {'prefixes': ['vm.swappiness']}
    mod = get_sysctl(module, inp['prefixes'])
    assert mod == {u'vm.swappiness': u'60'}


# Generated at 2022-06-13 02:11:01.199129
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils import basic

    sysctl_cmd = '/bin/sysctl'
    module = basic.AnsibleModule(argument_spec={})
    module.get_bin_path = lambda x: sysctl_cmd

# Generated at 2022-06-13 02:11:11.621203
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec={})


# Generated at 2022-06-13 02:11:14.931678
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec={},
    )

    sysctl = get_sysctl(module, ["vm.swappiness"])
    assert sysctl['vm.swappiness'] == "0"

# Generated at 2022-06-13 02:11:25.359076
# Unit test for function get_sysctl
def test_get_sysctl():
    test_prefixes = ['/proc/sys', '/not/a/real/path']

# Generated at 2022-06-13 02:11:31.605587
# Unit test for function get_sysctl
def test_get_sysctl():
    class MockAnsibleModule():
        @staticmethod
        def get_bin_path(binary):
            return '/sbin/sysctl'

        @staticmethod
        def run_command(cmd):
            return 0, 'kernel.domainname = example.com\nkernel.ostype = Linux', ''

    result = get_sysctl(MockAnsibleModule(), [])

    assert result['kernel.domainname'] == 'example.com'
    assert result['kernel.ostype'] == 'Linux'

# Generated at 2022-06-13 02:11:37.323566
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils import basic
    module = basic.AnsibleModule(argument_spec=dict())

    os_facts = dict(os_family='RedHat')
    module.deprecate('os_facts is deprecated, use ansible_facts instead', '2.13')
    module.exit_json(changed=False, ansible_facts=dict(os_facts=os_facts))

    #assert sysctl['kernel.domainname'] == 'example.com'


if __name__ == '__main__':
    test_get_sysctl()

# Generated at 2022-06-13 02:11:54.812559
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.shell import Shell, HAS_PARAMIKO

    module = AnsibleModule(argument_spec=dict())
    module.get_bin_path = lambda x: x if x in ('sysctl', 'ping', '/bin/true') else None

    # check for missing sysctl command
    module.run_command = lambda x: (255, '', '')
    result = get_sysctl(module, [])
    assert len(result) == 0

    # check successful return
    if HAS_PARAMIKO:
        module.run_command = lambda x: (0, 'foo.bar.baz: 1', '')

# Generated at 2022-06-13 02:12:00.775863
# Unit test for function get_sysctl
def test_get_sysctl():
    module = FakeModule()
    assert(get_sysctl(module, ['fs.file-max'])=={'fs.file-max': '1048576'})
    assert(get_sysctl(module, ['net.ipv4.ip_forward'])=={'net.ipv4.ip_forward': '0'})


# Generated at 2022-06-13 02:12:09.048714
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule
    sysctl_values = dict()
    sysctl_values['fs.aio-max-nr'] = '65536'
    sysctl_values['kernel.sysrq'] = '1'
    module = AnsibleModule(argument_spec=dict())
    module.run_command = lambda *args, **kwargs: (0, "", "")
    module.run_command = lambda *args, **kwargs: (0, ('%s\n' % ('\n'.join(sysctl_values.keys()))), "")
    module.run_command = lambda *args, **kwargs: (0, "%s" % ('\n'.join(sysctl_values.values())), "")

# Generated at 2022-06-13 02:12:18.554700
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={}, supports_check_mode=False)

    result = get_sysctl(module, ['kernel.hostname'])
    assert result == { "kernel.hostname": "ansible-test-host" }

    result = get_sysctl(module, ['kernel.hostname', 'kernel.randomize_va_space'])
    assert result == { "kernel.hostname": "ansible-test-host", "kernel.randomize_va_space": "2" }

    # Test that multiline sysctl values are handled properly
    result = get_sysctl(module, ['kernel.sched_domain.cpu0'])

# Generated at 2022-06-13 02:12:21.250632
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(argument_spec={})
    sysctl = get_sysctl(module, [])
    assert sysctl['kern.ostype'] == 'Darwin'
    assert sysctl['hw.ncpu'] == '4'

# Generated at 2022-06-13 02:12:27.516599
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils import basic
    import sys

    module = basic.AnsibleModule(
        argument_spec=dict()
    )

    sysctl = get_sysctl(module, ['kern', 'ostype'])

    assert 'kern.somaxconn' in sysctl
    assert sysctl['kern.somaxconn'] == '128'
    assert 'kern.ostype' in sysctl
    assert sysctl['kern.ostype'] == 'FreeBSD'

    if sys.platform.startswith('freebsd'):
        # FreeBSD and DragonFlyBSD have this key
        assert 'kern.secmodel.bsd' in sysctl
        assert sysctl['kern.secmodel.bsd'] == '1'

# Generated at 2022-06-13 02:12:28.962765
# Unit test for function get_sysctl
def test_get_sysctl():
    module = MockModule()
    sysctl = get_sysctl(module, ['net.ipv4.ip_forward'])
    assert sysctl['net.ipv4.ip_forward'] == '0'



# Generated at 2022-06-13 02:12:38.439535
# Unit test for function get_sysctl
def test_get_sysctl():
    import requests.exceptions

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.urls import open_url

    def _open_url_success(*args, **kwargs):
        class _Response(object):
            def read(self):
                return ''
        return _Response()

    def _open_url_fail(*args, **kwargs):
        raise requests.exceptions.RequestException

    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True,
    )
    module.open_url = _open_url_success
    assert 'ntp.drift_hz' not in get_sysctl(module, ['net.ipv4.ip_local_port_range'])
    module.open_url = _open_url_fail


# Generated at 2022-06-13 02:12:49.155480
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule
    m = AnsibleModule(argument_spec=dict())
    m.get_bin_path = lambda x: x

    m.run_command = lambda x: (0, '''net.ipv4.ip_forward: 0\nvm.swappiness: 20\nvm.swappiness: 0\nvm.swappiness: 1\nvm.swappiness: 2\nvm.swappiness: 3\nvm.swappiness: 4\nvm.swappiness: 5\nvm.swappiness: 6\nvm.swappiness: 7\nvm.swappiness: 8\nvm.swappiness: 9''', '')
    x = get_sysctl(m, ['vm.swappiness'])
    assert x == {'vm.swappiness': '9'}


# Generated at 2022-06-13 02:12:58.019601
# Unit test for function get_sysctl
def test_get_sysctl():
    sysctl_output_1 = """
        net.core.somaxconn = 511
        net.core.netdev_max_backlog = 511
        net.core.rmem_default = 8388608
        net.core.rmem_max = 16777216
    """

# Generated at 2022-06-13 02:13:25.336745
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils import basic

    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    test_sysctl = get_sysctl(module, prefixes=["net"])
    assert isinstance(test_sysctl, dict)
    keys = test_sysctl.keys()
    assert "net.ipv4.ip_forward" in keys
    assert test_sysctl["net.ipv4.ip_forward"] == "0"
    assert "net.ipv6.conf.default.forwarding" in keys
    assert "net.ipv6.conf.all.forwarding" in keys

# Generated at 2022-06-13 02:13:34.985622
# Unit test for function get_sysctl
def test_get_sysctl():
    import os
    import re
    import sys

    # Find the expected value for sysctl hw.memsize based on the number of available bytes in /dev/kmem
    (kmem_size, kmem_name) = os.stat("/dev/kmem").st_size, "/dev/kmem"
    # Find the expected value for sysctl hw.physmem based on the number of available bytes in /dev/mem
    (mem_size, mem_name) = os.stat("/dev/mem").st_size, "/dev/mem"

    # Determine the expected results
    if os.path.exists("/dev/kmem"):
        # On FreeBSD, sysctl hw.memsize is reported based on the number of bytes available in /dev/kmem
        expected_hw_memsize = kmem_size

# Generated at 2022-06-13 02:13:43.405705
# Unit test for function get_sysctl
def test_get_sysctl():

    import contextlib

    class FakeModule(object):
        class module_utils(object):
            class _text(object):
                @staticmethod
                def to_text(v):
                    return v

        def __init__(self):
            self.run_command_called = False
            self.run_command_rc = 0
            self.run_command_out = "net.ipv4.ip_forward = 0\nvm.swappiness = 60\n"
            self.run_command_err = ""
            self.run_command_called_with = None
            self.warn_called = False
            self.warn_called_with = None

        def get_bin_path(self, command):
            return command

        def run_command(self, args):
            self.run_command_called = True
            self.run

# Generated at 2022-06-13 02:13:47.798342
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={})
    module.run_command = lambda x: (1, "one\ntwo\nthree = foo\n four: bar", "exception")

    sysctl = get_sysctl(module, {'foo', 'bar'})

    assert sorted(sysctl.items()) == [('three', 'foo'), ('four', 'bar')]


# Generated at 2022-06-13 02:13:52.424346
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec=dict())

    # setup mocks for AnsibleModule to work
    module.params = {}
    module.check_mode = False
    module.run_command = lambda *args: ('', 'foo=bar\nfiz: buzz', '')

    sysctl = get_sysctl(module, ['foo'])
    assert sysctl == {'foo': 'bar\nfiz: buzz'}


# Generated at 2022-06-13 02:13:58.907168
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.six import PY3
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts.common import get_sysctl
    from ansible.module_utils.facts.system.sysctl import get_sysctl as py3_sysctl

    module = AnsibleModule()

    if PY3:
        get_sysctl = py3_sysctl

    module.run_command = Mock(return_value=(0, 'net.core.somaxconn = 1024', ''))
    assert get_sysctl(module, []) == {'net.core.somaxconn': '1024'}

    module.run_command = Mock(return_value=(0, 'net.ipv4.conf.all.forwarding = 1', ''))
    assert get_sys

# Generated at 2022-06-13 02:14:07.371605
# Unit test for function get_sysctl
def test_get_sysctl():
    """
    Test module's functionality
    """

    sysctl_output = """
net.ipv6.conf.all.disable_ipv6 = 0
net.ipv6.conf.default.disable_ipv6 = 0
net.ipv6.conf.lo.disable_ipv6 = 0

fs.inotify.max_user_watches = 524288
net.ipv6.conf.all.autoconf = 0
net.ipv6.conf.default.autoconf = 0
net.ipv6.conf.lo.autoconf = 0

kernel.sysrq = 1
"""

    module_mock = MockModule('ansible.modules.system.sysctl')
    module_mock.params = {}

    sysctl = dict()

# Generated at 2022-06-13 02:14:12.317202
# Unit test for function get_sysctl
def test_get_sysctl():
    module = type('AnsibleModule', (object,), {
        'get_bin_path': lambda *args: 'sysctl',
        'run_command': lambda *args: (0, 'net.ipv4.tcp_max_syn_backlog = 511\n', None)
    })
    sysctl = get_sysctl(module, ['net.ipv4.tcp_max_syn_backlog'])
    assert sysctl == {'net.ipv4.tcp_max_syn_backlog': '511'}

# Generated at 2022-06-13 02:14:16.704290
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec=dict())
    assert module.get_bin_path('sysctl') is not None
    assert get_sysctl(module, ['fs.file-max']) == {'fs.file-max': '100000'}
    assert get_sysctl(module, ['fs.file-max', 'fs.file-nr']) == {'fs.file-max': '100000', 'fs.file-nr': '0       0       0'}
    assert get_sysctl(module, ['fs.file-max', 'fs.file-nr', 'fs.file-nr']) == {'fs.file-max': '100000', 'fs.file-nr': '0       0       0'}

# Generated at 2022-06-13 02:14:25.466199
# Unit test for function get_sysctl
def test_get_sysctl():
    """ This is a basic unit test for the get_sysctl() function """
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common._collections_compat import Mapping

    import sys

    module = AnsibleModule(argument_spec=dict())
    if sys.version_info.major >= 3:
        prefixes = ['vm.overcommit_memory']
    else:
        prefixes = ['vm.swappiness']
    result = get_sysctl(module=module, prefixes=prefixes)
    assert isinstance(result, Mapping)


# vim: ai et ts=4 sts=4 sw=4 ft=python

# Generated at 2022-06-13 02:15:21.234503
# Unit test for function get_sysctl
def test_get_sysctl():
    ''' testing get_sysctl '''

# Generated at 2022-06-13 02:15:27.910852
# Unit test for function get_sysctl
def test_get_sysctl():

    import os
    import tempfile
    from ansible.module_utils import basic

    sysctl_file = tempfile.NamedTemporaryFile(delete=False)
    sysctl_file.write(to_text('kernel.exec-shield =   1'))
    sysctl_file.close()

    os.environ['PATH'] = to_text(os.path.dirname(sysctl_file.name)) + os.pathsep + os.environ['PATH']

    module = basic.AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True,
    )

    assert dict(get_sysctl(module, ['kernel.exec-shield']).items()) == dict([('kernel.exec-shield', '1')]).items()

# Generated at 2022-06-13 02:15:35.991369
# Unit test for function get_sysctl
def test_get_sysctl():

    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule({})

    assert get_sysctl(module, ['net.inet.ip.portrange.first', 'net.inet.ip.portrange.last',
                               'net.inet.ip.portrange.randomized', 'net.inet.ip.portrange.hifirst']) == {
        'net.inet.ip.portrange.first': '49152',
        'net.inet.ip.portrange.last': '65535',
        'net.inet.ip.portrange.randomized': '1',
        'net.inet.ip.portrange.hifirst': '49152'
    }

# Generated at 2022-06-13 02:15:40.042663
# Unit test for function get_sysctl
def test_get_sysctl():
    module = type('ModuleUtilsFake', (object,), dict(fail_json=lambda *_, **__: None, check_mode=False))
    sysctl = get_sysctl(module, ['net.ipv4.ip_local_port_range'])
    assert sysctl == {'net.ipv4.ip_local_port_range': '35000 61000'}

# Generated at 2022-06-13 02:15:42.417851
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(argument_spec=dict())
    sysctl_values = get_sysctl(module, ['-a'])
    assert sysctl_values
    assert 'user.home' in sysctl_values


# Generated at 2022-06-13 02:15:48.427537
# Unit test for function get_sysctl
def test_get_sysctl():
    # Test module import
    from ansible.module_utils.basic import AnsibleModule

    # Create test module
    module = AnsibleModule(argument_spec=dict())

    # Create dummy sysctl command output.
    sysctl_out = '''kernel.domainname = (none)
kernel.hostname = (none)
kernel.osrelease = 3.10.0-327.36.3.el7.x86_64
kernel.osrelease_name = CentOS Linux
kernel.ostype = Linux
kernel.panic_on_oops = 1
kernel.sysrq = 0
kernel.tainted = 2
'''

    # Create dummy sysctl command error output.
    sysctl_err = ''

    # Create dummy sysctl command exit status.
    sysctl_rc = 0

    # Create expected sysctl output.
    expected_sysctl

# Generated at 2022-06-13 02:15:50.325159
# Unit test for function get_sysctl
def test_get_sysctl():
    assert get_sysctl(None, ['kern.maxproc']) == {'kern.maxproc': '4096'}

# Generated at 2022-06-13 02:16:00.395531
# Unit test for function get_sysctl
def test_get_sysctl():
    import os
    import sys

    sys.modules['__builtin__'] = __builtin__
    # pylint: disable=no-name-in-module
    from ansible.module_utils import basic
    from ansible.module_utils.basic import AnsibleModule

    mod = AnsibleModule(argument_spec={
        'prefixes': dict(type='list', required=True),
    })

    if (os.path.exists('/etc/sysctl.conf') and
            not os.access('/etc/sysctl.conf', os.R_OK)):
        mod.fail_json(msg='/etc/sysctl.conf exists but is not readable')

    result = get_sysctl(mod, mod.params['prefixes'])
    mod.exit_json(ansible_facts={'sysctl': result})

# Generated at 2022-06-13 02:16:05.677760
# Unit test for function get_sysctl
def test_get_sysctl():
    test_module = type('', (), dict(run_command=lambda cmd: (0, '', '')))
    assert dict(get_sysctl(test_module, ['vfs.nfs.nfsv4_recoveryacl',
                                         'vfs.nfs.nfsv4_recoverydomain'])) == {
        'vfs.nfs.nfsv4_recoveryacl': '0',
        'vfs.nfs.nfsv4_recoverydomain': '0',
    }

# vim:ts=4:sw=4:expandtab

# Generated at 2022-06-13 02:16:15.352192
# Unit test for function get_sysctl
def test_get_sysctl():
    test_module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    # empty string is not a valid sysctl
    assert get_sysctl(test_module, ['']) == dict()

    # FreeBSD
    prefixes = ['/compat']


# Generated at 2022-06-13 02:18:08.916429
# Unit test for function get_sysctl
def test_get_sysctl():
    assert get_sysctl(None, ['kernel.domainname']) == {'kernel.domainname': 'cvn.local'}



# Generated at 2022-06-13 02:18:13.385775
# Unit test for function get_sysctl
def test_get_sysctl():
    import sysctl
    module = sysctl
    setattr(module, '_sysctl_bin', './unit_tests/sysctl')
    sysctl = get_sysctl(module, ['vm', 'debug'])
    assert sysctl['vm.debug.exception_trace'] == '0'
    assert sysctl['vm.debug.kstack_depth'] == '64'
    assert sysctl['vm.debug.cow'] == '0'


# Generated at 2022-06-13 02:18:20.967987
# Unit test for function get_sysctl

# Generated at 2022-06-13 02:18:24.219292
# Unit test for function get_sysctl
def test_get_sysctl():
    assert get_sysctl(None, ['vm.swappiness']) == {'vm.swappiness': '0'}
    assert get_sysctl(None, ['vm.swappiness', 'fs.file-max']) == {'vm.swappiness': '0', 'fs.file-max': '524288'}


# Generated at 2022-06-13 02:18:26.652324
# Unit test for function get_sysctl
def test_get_sysctl():
    module = None
    prefixes = ["kern.securelevel", "kern.hostname"]
    sys = get_sysctl(module, prefixes)
    assert sys == {"kern.securelevel": "0", "kern.hostname": "hostname"}


# Generated at 2022-06-13 02:18:30.954371
# Unit test for function get_sysctl
def test_get_sysctl():

    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    sysctl = get_sysctl(module, ['vm.overcommit_memory'])
    assert sysctl['vm.overcommit_memory'] == '0'

# Generated at 2022-06-13 02:18:40.173842
# Unit test for function get_sysctl
def test_get_sysctl():
    import os
    import ansible.utils.module_docs as module_docs
    from ansible.module_utils.basic import AnsibleModule


# Generated at 2022-06-13 02:18:44.932712
# Unit test for function get_sysctl
def test_get_sysctl():
    """Function to test get_sysctl() function returns sysctl key value pair """
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(
        argument_spec=dict(
            prefixes=dict(type='list', default=['kern.'], required=True),  # osx/freebsd only
        ),
    )
    sysctl = dict()
    return_values = get_sysctl(module, module.params.get('prefixes'))
    sysctl = return_values
    assert sysctl is not None
    assert sysctl['kern.version'] is not None

# Generated at 2022-06-13 02:18:49.091882
# Unit test for function get_sysctl
def test_get_sysctl():
    test_sysctls = dict(
        aaa='AAA',
        bbb='BBB',
    )
    class TestModule:
        def run_command(self, cmd):
            if cmd[0] == 'sysctl':
                return 0, 'aaa = AAA\nbbb = BBB', ''
            else:
                raise Exception('unexpected command %s' % repr(cmd))

        def get_bin_path(self, cmd):
            if cmd == 'sysctl':
                return 'sysctl'
            else:
                raise Exception('unexpected get_bin_path(%s)' % repr(cmd))

        def warn(self, msg):
            pass

    test_module = TestModule()
    result = get_sysctl(test_module, ['aaa', 'bbb'])
    assert result == test_sysct

# Generated at 2022-06-13 02:18:58.891024
# Unit test for function get_sysctl