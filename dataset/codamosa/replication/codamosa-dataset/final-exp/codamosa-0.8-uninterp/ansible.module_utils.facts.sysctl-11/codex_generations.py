

# Generated at 2022-06-13 02:09:23.997899
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(argument_spec=dict())


# Generated at 2022-06-13 02:09:31.727517
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule
    from ansible_collections.ansible.community.plugins.module_utils.system import sysctl
    from ansible_collections.ansible.community.plugins.module_utils.basic import AnsibleModule

    sysctl_utils = sysctl.Sysctl()
    module = sysctl_utils.module

    sysctl = sysctl_utils.get_sysctl(['vm.dirty_ratio'])
    assert sysctl == {'vm.dirty_ratio': '20'}, sysctl

    sysctl = sysctl_utils.get_sysctl(['vm.dirty_ratio', 'vm.dirty_background_ratio'])
    assert sysctl.keys() == {'vm.dirty_ratio', 'vm.dirty_background_ratio'}, sysctl.keys()

# Generated at 2022-06-13 02:09:39.275207
# Unit test for function get_sysctl
def test_get_sysctl():
    module_name = 'get_sysctl'
    module_path = 'ansible/modules/system/%s.py' % module_name
    module_args = "prefixes='net.bridge.bridge-nf-call-iptables'"

    from ansible.module_utils.basic import AnsibleModule
    m = AnsibleModule(
        argument_spec={
            'prefixes': {'required': True, 'type': 'list', 'default': []}
        }
    )

    sysctl = get_sysctl(m, m.params['prefixes'])
    assert 'net.bridge.bridge-nf-call-iptables' in sysctl
    assert sysctl['net.bridge.bridge-nf-call-iptables'] == '1'

if __name__ == '__main__':
    test_get_

# Generated at 2022-06-13 02:09:47.036802
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec={})

    sysctl = get_sysctl(module, ['kernel.hostname'])
    assert 'kernel.hostname' in sysctl

    sysctl = get_sysctl(module, ['kernel'])
    assert 'kernel.hostname' in sysctl

    sysctl = get_sysctl(module, ['kern'])
    assert 'kernel.hostname' in sysctl

    sysctl = get_sysctl(module, ['kernel.hostname', 'kern'])
    assert 'kernel.hostname' in sysctl
    assert 'kernel' in sysctl

# Generated at 2022-06-13 02:09:55.573096
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule

    m = AnsibleModule()
    # Set some mocks
    m._ansible_sys_executable = '/usr/bin/python2.7'
    m.run_command = lambda x: (0, 'debug.exception-trace = 0\nhw.ncpu = 2\nhw.pagesize = 4096', '')

    res = get_sysctl(m, [])

    assert res
    assert res['hw.ncpu'] == '2'
    assert res['hw.pagesize'] == '4096'
    assert res['debug.exception-trace'] == '0'

# Generated at 2022-06-13 02:10:05.737046
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes, to_text


# Generated at 2022-06-13 02:10:11.440641
# Unit test for function get_sysctl
def test_get_sysctl():

    from ansible.module_utils.basic import AnsibleModule

    testmodule = AnsibleModule({}, supports_check_mode=False)

    assert testmodule.get_bin_path('sysctl')
    assert testmodule.run_command(testmodule.get_bin_path('sysctl'))

    sysctl = get_sysctl(testmodule, ['-a'])
    assert sysctl
    assert sysctl['net.ipv4.ip_forward'] == '0'
    assert sysctl['kernel.version']


if __name__ == '__main__':
    test_get_sysctl()

# Generated at 2022-06-13 02:10:20.548759
# Unit test for function get_sysctl
def test_get_sysctl():

    fake_module = FakeModule()

    # Fake of input argument
    prefixes = ['net.ipv4.tcp_timestamps']

    # Fake of output returned by command
    rc = 0
    out = 'net.ipv4.tcp_timestamps = 0\n'
    err = ''

    # Init the object with fake results
    fake_module.run_command = FakeRunCommand(rc, out, err)

    # call the function to test
    sysctl = get_sysctl(fake_module, prefixes)

    # we expect a dict with one element
    assert sysctl == {'net.ipv4.tcp_timestamps': '0'}


# Generated at 2022-06-13 02:10:26.397550
# Unit test for function get_sysctl
def test_get_sysctl():
    module = object()
    module.warn = lambda msg: None
    module.run_command = lambda cmd: (0, '', '')

    # This test will fail if not run on Linux.
    # It will also fail if sysctl isn't installed.
    sysctl = get_sysctl(module, [])
    assert 'kernel.domainname' in sysctl
    assert 'kernel.domainname' in sysctl
    assert sysctl['kernel.domainname'] != ''

# Generated at 2022-06-13 02:10:33.127279
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.pycompat24 import get_exception
    from ansible.module_utils.six import StringIO

    class FakeModule(object):
        def __init__(self, *args, **kwargs):
            self.fail_json = kwargs.get('fail_json', lambda x: x)
            self.warn = kwargs.get('warn', lambda x: x)

        def get_bin_path(self, *args, **kwargs):
            return 'sysctl'

        def run_command(self, *args, **kwargs):
            return 0, StringIO(u"net.ipv4.ip_forward = 1"), ''

    fm = FakeModule()

# Generated at 2022-06-13 02:10:45.997736
# Unit test for function get_sysctl
def test_get_sysctl():
    ''' test to see if the sysctl function returns the correct values '''

    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict()
    )

    # Ensure sysctl returns the correct values
    sysctl = get_sysctl(module, ['kern'])
    assert 'kern.ostype' in sysctl
    assert 'kern.osrelease' in sysctl
    assert 'kern.osrevision' in sysctl
    assert 'kern.version' in sysctl

# Generated at 2022-06-13 02:10:49.069527
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(argument_spec=dict())
    sysctl = get_sysctl(module, ("vm.swappiness", "kernel.ostype"))
    assert ("kernel.ostype" in sysctl)


# Generated at 2022-06-13 02:11:00.877031
# Unit test for function get_sysctl
def test_get_sysctl():
    import ansible.module_utils.basic as module_utils
    import sys

# Generated at 2022-06-13 02:11:03.044095
# Unit test for function get_sysctl
def test_get_sysctl():
    assert get_sysctl('/proc/sys') == {}

# Generated at 2022-06-13 02:11:09.130165
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils import basic
    import json
    module = basic.AnsibleModule(
        argument_spec = dict()
    )

    results = get_sysctl(module, ['/proc/sys/kernel'])
    assert results['kernel.ostype'] == 'Linux'

    results = get_sysctl(module, ['/proc/sys', 'net'])
    assert results['net.ipv4.conf.all.rp_filter'] == '1'

# Generated at 2022-06-13 02:11:17.024129
# Unit test for function get_sysctl
def test_get_sysctl():
    # test this function with the following input params
    module = AnsibleModuleFake({'shell': dict(executable='/bin/sh')})
    rc, out, err = module.run_command('echo "dev.cdrom.autoclose = 1"')
    rc, out, err = module.run_command('echo "dev.cdrom.autoeject = 0"')
    rc, out, err = module.run_command('echo "dev.cdrom.info = \"CDROM information\""')
    rc, out, err = module.run_command('echo "dev.cdrom.check_media = 0"')

    rc, out, err = module.run_command('echo "kern.ipc.nmbclusters: 10000"')

# Generated at 2022-06-13 02:11:27.214855
# Unit test for function get_sysctl
def test_get_sysctl():
    # Setup module mock
    class TestModule:
        def __init__(self):
            self.run_command_called = False
            self.rc = 0

        def get_bin_path(self, app):
            return app

        def run_command(self, cmd):
            self.run_command_called = True
            if self.rc == 0:
                stdout = """\
    foo.bar: 1
    foo.baz: 2
    foo.qux: 3
    foo.quux: 4
            """
                return 0, stdout, ''
            else:
                return 1, '', 'Cannot find application'

    # Create test module
    module = TestModule()

    # Test that everything works as originally expected
    sysctl = get_sysctl(module, ['foo.bar'])

# Generated at 2022-06-13 02:11:29.583963
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(argument_spec={})
    sysctl = get_sysctl(module, ["vm.swappiness"])
    assert sysctl["vm.swappiness"] == "60"


# Generated at 2022-06-13 02:11:38.121834
# Unit test for function get_sysctl
def test_get_sysctl():

    data, comments, rc, out, err = (
        "{'dev.cdrom.info': 'CDROM information',\n" +
        "'dev.cdrom.info.count': 'Number of CDROM drives'}\n"
    ), '', 0, '', ''

    # fake module object
    class MockModule():
        def __init__(self, data, comments, rc, out, err):
            self.data = data
            self.comments = comments
            self.rc = rc
            self.out = out
            self.err = err

        def get_bin_path(self, _):
            return 'sysctl'

        def run_command(self, _):
            return (self.rc, self.out, self.err)

        def warn(self, msg):
            self.comments += '%s\n'

# Generated at 2022-06-13 02:11:48.701916
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule
    from io import StringIO

    m = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=False,
        add_file_common_args=False
    )


# Generated at 2022-06-13 02:12:03.023275
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(argument_spec=dict(
        prefixes=dict(type='list', default=['kernel'])
    ))
    sysctl = get_sysctl(module, module.params['prefixes'])
    assert sysctl

# Generated at 2022-06-13 02:12:13.806195
# Unit test for function get_sysctl
def test_get_sysctl():
    import os
    import sys
    import pytest
    import tempfile
    import shutil
    import mock

    (fd, sysctl_output) = tempfile.mkstemp()


# Generated at 2022-06-13 02:12:20.400900
# Unit test for function get_sysctl
def test_get_sysctl():
    module = type('module', (object,), {'get_bin_path': lambda self, x: '/sbin/sysctl', 'run_command': lambda self, x: (0, 'foo = bar\nnet.ipv4.ip_forward = 1\n', '')})()
    assert get_sysctl(module, 'foo net.ipv4.ip_forward'.split(' ')) == {'foo': 'bar', 'net.ipv4.ip_forward': '1'}
    assert get_sysctl(module, '') == {}
    assert get_sysctl(module, 'foo') == {'foo': 'bar'}

# Generated at 2022-06-13 02:12:24.460568
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils import basic

    module = basic.AnsibleModule(argument_spec=dict())
    module.run_command = lambda x: ('', 'net.ipv6.conf.all.disable_ipv6 = 1\n', '')
    assert get_sysctl(module, ['net.ipv6.conf.all.disable_ipv6']) == {'net.ipv6.conf.all.disable_ipv6': '1'}

# Generated at 2022-06-13 02:12:28.849237
# Unit test for function get_sysctl
def test_get_sysctl():
    sysctl = get_sysctl(None, ['fs.file-max', 'vm.swappiness'])
    assert len(sysctl) == 2
    assert sysctl['fs.file-max'] == '20480'
    assert sysctl['vm.swappiness'] == '60'



# Generated at 2022-06-13 02:12:37.086642
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict(
            sysctl=dict(type='list', required=True),
        ),
    )

    module.run_command = lambda x, check_rc=None: (0, 'vm.swappiness = 1\nvm.dirty_ratio = 60\n'.encode('utf-8'), '')

    ret_dict = get_sysctl(module, ['vm.swappiness'])

    assert len(ret_dict) == 1
    assert ret_dict['vm.swappiness'] == '1'



# Generated at 2022-06-13 02:12:47.831639
# Unit test for function get_sysctl

# Generated at 2022-06-13 02:12:51.568026
# Unit test for function get_sysctl
def test_get_sysctl():
    assert get_sysctl('net', 'net.ipv4.tcp_wmem') == { 'net.ipv4.tcp_wmem': '4096 87380 8388608' }



# Generated at 2022-06-13 02:12:58.852126
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils import basic
    import json
    import sys

    if sys.version_info[:2] < (2, 7):
        import unittest2 as unittest
    else:
        import unittest

    class TestGetSysctl(unittest.TestCase):
        module = basic.AnsibleModule(
            argument_spec=dict(prefixes=dict(required=True, type='list'))
        )
        module.warn = lambda *args, **kwargs: None


# Generated at 2022-06-13 02:13:00.718590
# Unit test for function get_sysctl
def test_get_sysctl():
    import ansible.utils.module_docs_fragments
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec={
        'prefixes': dict(type='list', required=True),
    })
    res = get_sysctl(module, ['-a'])

    assert(res)

# Generated at 2022-06-13 02:13:29.998121
# Unit test for function get_sysctl
def test_get_sysctl():
    # Test passing of argument module
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={'key': dict(type='str')})
    # Test passing of argument prefixes
    prefixes = ['net.ipv4.conf.default.rp_filter', 'net.ipv4.conf.all.rp_filter']
    sysctl = get_sysctl(module, prefixes)
    assert sysctl['net.ipv4.conf.default.rp_filter'] == sysctl['net.ipv4.conf.all.rp_filter']
    assert sysctl['net.ipv4.conf.default.rp_filter'] == '1'


# Generated at 2022-06-13 02:13:39.280435
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    _mod = basic.AnsibleModule(
        argument_spec=dict(),
    )

    _mod.run_command = lambda x: (0, to_bytes('\n'.join([
        'kernel.ostype = Linux',
        'kernel.osrelease = 4.15.0-1043-aws',
        'kernel.version = #46-Ubuntu SMP Mon Jun 24 10:55:24 UTC 2019\n',
        'kernel.domainname = (none)\n',
        'kernel.hostname = ip-10-0-0-1\n',
        'kernel.arch = x86_64',
    ])), '')

    r = get_sysctl(_mod, ['kernel'])

# Generated at 2022-06-13 02:13:44.880424
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(
        argument_spec=dict(),
    )

    # Generate output from sysctl command
    module.run_command = mock.MagicMock(return_value=(0, sysctl_command(prefixes=[key1], value=value1, multi_value=True), None))

    # get_sysctl will call module.run_command
    result = get_sysctl(module, prefixes=[key1])

    assert result == {key1: value1}


# Generated at 2022-06-13 02:13:51.690885
# Unit test for function get_sysctl
def test_get_sysctl():
    out = '''
    net.ipv4.ip_forward = 0
    net.ipv4.conf.default.rp_filter = 1
    '''
    rc = 0
    err = ''
    class FakeModule():
        def run_command(self, cmd):
            return rc, out, err
        def warn(self, msg):
            pass
        def get_bin_path(self, cmd):
            return cmd

    module = FakeModule()
    sysctl = get_sysctl(module, ['net.ipv4.ip_forward'])
    assert sysctl['net.ipv4.ip_forward'] == '0'

# Generated at 2022-06-13 02:13:57.317955
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict(
            prefixes=dict(type='list', elements='str'),
        )
    )

    sysctl = get_sysctl(module, ['kernel', 'net'])
    assert isinstance(sysctl, dict), 'Returned data is not a dictionary'
    assert sysctl['kernel.version'].startswith('4.4.0-'), 'Unexpected kernel version'
    assert sysctl['net.ipv4.ip_forward'].strip() == '0', 'Unexpected IPv4 ip_forward value'

# Generated at 2022-06-13 02:14:02.445498
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.basic import EnvironmentDict
    module = AnsibleModule(argument_spec={'params': {'type': 'list', 'elements': 'str'}})
    env = EnvironmentDict({"PATH": "/usr/sbin:/sbin:/bin:/usr/bin", "PYTHONPATH": ""},
                          loader=None, shared_loader=None, search_paths=None)
    module.run_command = lambda x, check_rc=True: (0, "key1: value1\nkey2 = value2\nkey3: value3", "")
    res = get_sysctl(module, ['key1', 'key2', 'key3'])
    assert isinstance(res, dict)

# Generated at 2022-06-13 02:14:09.349285
# Unit test for function get_sysctl
def test_get_sysctl():
    module = type('FakeModule', (object, ), {
        'run_command' : lambda self, cmd, check_rc=False: (0, '{0}: 1'.format(cmd[-1]), ''),
        'warn' : lambda self, msg: None
    })()
    assert get_sysctl(module, ('kernel.ostype',)) == {'kernel.ostype': '1'}
    assert get_sysctl(module, ('kernel.osrelease', 'kernel.ostype')) == {'kernel.osrelease': '1', 'kernel.ostype': '1'}

# Generated at 2022-06-13 02:14:13.688226
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(
        argument_spec=dict(
            prefixes=dict(required=True, type='list'),
        ),
    )
    prefixes = ['kern']

    actual = get_sysctl(module, prefixes)

    # The output of sysctl is largely dependent on the system so we just test
    # for a few specific keys.
    assert actual['kern.hostname'] == 'apple.local'
    assert actual['kern.osrelease'] == '16.0.0'
    assert actual['kern.ostype'] == 'Darwin'

# Generated at 2022-06-13 02:14:18.839257
# Unit test for function get_sysctl
def test_get_sysctl():
    """
    The function get_sysctl is tested by testing its direct effect on the
    dictionary it is given as a parameter.
    """
    sysctl = {}
    prefixes = ["net.ipv4.ip_forward"]
    get_sysctl(sysctl, prefixes)
    assert sysctl[prefixes[0]] == "1"

# Generated at 2022-06-13 02:14:25.170131
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule
    def test():

        module = AnsibleModule(
            argument_spec = dict(),
        )

        res = get_sysctl(module, ['kernel.shmmax'])

        module.exit_json(changed=False, kernel_shmmax=res['kernel.shmmax'])
    res = test()
    assert 'kernel.shmmax' in res
    assert res['kernel.shmmax']

# Generated at 2022-06-13 02:15:22.880892
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    full_sysctl = get_sysctl(module, ['net'])
    assert 'net.ipv4.ip_forward' in full_sysctl
    assert 'net.ipv6.ip_forward' in full_sysctl
    assert 'net.ipv4.ip_forward' in full_sysctl
    assert 'net.ipv4.ip_forward' in full_sysctl
    assert 'net.ipv4.ip_forward' in full_sysctl
    assert 'net.ipv4.ip_forward' in full_sysctl
    assert 'net.ipv4.ip_forward' in full_sysctl

# Generated at 2022-06-13 02:15:28.520667
# Unit test for function get_sysctl
def test_get_sysctl():
    module = MockAnsibleModule()
    module.run_command = Mock(return_value=(0, '', ''))

# Generated at 2022-06-13 02:15:34.177914
# Unit test for function get_sysctl
def test_get_sysctl():
    """ Test function get_sysctl """
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )

    # Test with a prefix that will have no results
    assert get_sysctl(module, ['kern.nonsense']) == {}

    # Test with a prefix that will have results
    assert 'net.inet.tcp.mssdflt' in get_sysctl(module, ['net.inet.tcp'])


# Generated at 2022-06-13 02:15:41.821358
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(argument_spec={})
    # Test prefixes without wildcards
    assert get_sysctl(module, ['net']) == get_sysctl(module, ['net.'])
    # Test prefixes with wildcards
    assert get_sysctl(module, ['net.*']) == get_sysctl(module, ['net.ipv4', 'net.ipv4.conf',
                                                                'net.ipv6'])
    # Test prefixes with wildcard at end
    assert get_sysctl(module, ['net.ipv4.*']) == get_sysctl(module, ['net.ipv4.conf'])
    # Test prefixes with wildcard and dot at end

# Generated at 2022-06-13 02:15:48.100038
# Unit test for function get_sysctl

# Generated at 2022-06-13 02:15:56.902872
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.basic import get_exception

    module = AnsibleModule(
        argument_spec=dict(),
    )

    try:
        import __main__
        sysctl = get_sysctl(module, ['fs.file-max'])
        __main__.sysctl = sysctl
    except Exception as e:
        module.fail_json(msg='Unable to read sysctl: %s' % str(e), exception=get_exception())

    if sysctl:
        module.exit_json(changed=False, ansible_facts=dict(sysctl=sysctl))
    else:
        module.fail_json(msg='Unable to read sysctl')

# Generated at 2022-06-13 02:16:05.245741
# Unit test for function get_sysctl
def test_get_sysctl():
    import os
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six.moves import StringIO

    prefixes = ['-a']
    if 'linux' in sys.platform:
        sysctl_out = '''
        net.ipv4.conf.default.forwarding = 1
        net.ipv4.conf.all.forwarding = 1
        net.ipv4.ip_forward = 1
        '''
    elif 'bsd' in sys.platform:
        sysctl_out = '''
        net.inet.ip.portrange.first: 49152
        net.inet.ip.portrange.last: 65535
        '''

# Generated at 2022-06-13 02:16:14.848718
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule
    import os

    module = AnsibleModule(argument_spec=dict())

# Generated at 2022-06-13 02:16:20.960475
# Unit test for function get_sysctl
def test_get_sysctl():
    module = DummyAnsibleModule()
    result = get_sysctl(module, ['hw.acpi.system.uuid'])
    assert 'hw.acpi.system.uuid' in result
    assert result['hw.acpi.system.uuid'] == 'Not Supported'

    result = get_sysctl(module, ['hw'])
    assert 'hw.acpi.system.uuid' in result
    assert result['hw.acpi.system.uuid'] == 'Not Supported'


# Generated at 2022-06-13 02:16:27.135418
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule

    data = dict(
        failed=False,
        changed=False,
        rc=0,
        stderr='',
        stdout='',
        stdout_lines=[]
    )

    my_args = dict(
        state='present',
    )
    module = AnsibleModule(argument_spec=my_args, supports_check_mode=True)

    test_sysctl = dict()
    test_sysctl['net.ipv4.ip_forward'] = '1'
    test_sysctl['net.bridge.bridge-nf-call-ip6tables'] = '0'

    sysctl_cmd = module.get_bin_path('sysctl')
    cmd = [sysctl_cmd, '-a']


# Generated at 2022-06-13 02:18:32.309739
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec = dict())
    assert {'dev.random.boot_randomize': '1'} == get_sysctl(module, ['dev.random.boot_randomize'])

# Generated at 2022-06-13 02:18:41.502811
# Unit test for function get_sysctl
def test_get_sysctl():
    '''Check our get_sysctl function against some known output.'''
    class Options:
        def __init__(self):
            self.become = True
            self.become_user = 'root'

    class ReturnCodes:
        def __init__(self, in_data):
            self.STD_OUT_RC = 0
            self.STDOUT = in_data

    class RunCommand:
        def __init__(self):
            self.rc = None
            self.stdout = None
            self.stderr = None

    class TestAnsibleModule:
        def __init__(self):
            self.params = Options()
            self.run_command_supports_check_rc = False
            self.check_mode = False
            self.run_command_environ_update = dict()

# Generated at 2022-06-13 02:18:46.040928
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(
        argument_spec=dict(
            prefixes=dict(required=True, type='list')
        )
    )
    result = get_sysctl(module, ['net.ipv4.ip_forward'])
    assert result['net.ipv4.ip_forward'] == '1'

# Generated at 2022-06-13 02:18:49.580053
# Unit test for function get_sysctl
def test_get_sysctl():
    rc, out, err = get_sysctl(['net.ipv4.conf.all.rp_filter'])

    assert rc == 0
    assert net.ipv4.conf.all.rp_filter in out


# Generated at 2022-06-13 02:18:55.387048
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={}, supports_check_mode=False)
    # Running with a prefix that does not exist should not cause a crash in the module
    try:
        assert get_sysctl(module, ['this.does.not.exist']) == {}
    except AssertionError:
        raise AssertionError('The command should not have crashed')


# Generated at 2022-06-13 02:19:02.281762
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule({})

    sysctl = get_sysctl(module, ['-n', 'kern.boottime'])
    assert sysctl['kern.boottime']

    sysctl = get_sysctl(module, ['kern.boottime'])
    assert sysctl['kern.boottime']

    sysctl = get_sysctl(module, ['kern.boottime=57'])
    assert sysctl['kern.boottime']

    sysctl = get_sysctl(module, ['kern.boottime: 57'])
    assert sysctl['kern.boottime']

# Generated at 2022-06-13 02:19:07.077959
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )

    result = get_sysctl(module, ['net.ipv4.conf.all.forwarding'])
    assert result.get('net.ipv4.conf.all.forwarding') == '0'

# Generated at 2022-06-13 02:19:10.274603
# Unit test for function get_sysctl
def test_get_sysctl():
    assert get_sysctl('/usr/sbin', ['vm.overcommit_memory=']) == {'vm.overcommit_memory': '0'}