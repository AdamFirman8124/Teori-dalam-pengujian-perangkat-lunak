

# Generated at 2022-06-13 04:20:44.951143
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    from ansible.module_utils.basic import AnsibleModule
    import collections

    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    # Create a mock object
    class SysctlDetectionMixin(VirtualSysctlDetectionMixin):
        class module:
            @staticmethod
            def run_command(cmd):
                return (0, 'QEMU', '')

    sysctl = SysctlDetectionMixin()
    sysctl.detect_sysctl = None
    sysctl.sysctl_path = 'sysctl'
    vendor_facts = sysctl.detect_virt_vendor('machdep.fake.key')
    assert 'virtualization_type' in vendor_facts

# Generated at 2022-06-13 04:20:53.892589
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    from ansible.module_utils.facts.virtual.freebsd import VirtualSysctlDetectionMixin
    from ansible.module_utils.facts.virtual.tests.fake_finder import FakeFinder
    from ansible.module_utils.facts.virtual.tests.fake_module import FakeModule
    from ansible.module_utils.facts.virtual.tests.fake_command import FakeCommand

    # Create our mixin
    mixin = VirtualSysctlDetectionMixin()

    # Create our finder
    finder = FakeFinder()

    # Create our dummy module
    module = FakeModule()

    # Create our command
    command = FakeCommand()

    # Set our finders
    module.set_finders([finder])

    # Set our command and it's return values
    module.set_command(command)

    # Set our sys

# Generated at 2022-06-13 04:21:00.053493
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    class TestModule(object):
        def get_bin_path(self, *args, **kwargs):
            return "/path/to/sysctl"

        def run_command(self, *args, **kwargs):
            rc = 0
            out = ""
            err = ""
            if args[0] == "/path/to/sysctl -n kern.vm_guest":
                out = "FreeBSD"
            elif args[0] == "/path/to/sysctl -n security.jail.jailed":
                out = "1"
            return rc, out, err

    class TestVirtualSysctlDetectionMixin(object):
        def __init__(self):
            self.module = TestModule()

    test_detect_virt_product = TestVirtualSysctlDetectionMixin()

# Generated at 2022-06-13 04:21:11.405063
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    from sys import version_info
    if version_info[0] < 3:
        import __builtin__ as builtins
    else:
        import builtins

    import os
    import sys
    import tempfile
    import types

    class ModuleStub(object):
        def __init__(self):
            self.args = types.SimpleNamespace()
            self.params = {
                'gather_subset': [],
                'gather_network_resources': [],
            }
            self.exit_json = lambda *args, **kwargs: sys.exit(0)
            self.fail_json = lambda *args, **kwargs: sys.exit(1)

        def get_bin_path(self, _):
            fd, self.sysctl_path = tempfile.mkstemp()
            os.close

# Generated at 2022-06-13 04:21:17.920449
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    from units.mock.sysctl import MockSysctlModule
    module = MockSysctlModule()
    sysctl_detect = VirtualSysctlDetectionMixin()
    (result, err) = sysctl_detect.detect_virt_vendor('hw.model')
    expected = dict(virtualization_role='guest', virtualization_type='kvm',
                    virtualization_tech_host=set(), virtualization_tech_guest=set(['kvm']))
    assert result == expected

# Generated at 2022-06-13 04:21:28.790773
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    import mock
    import copy

    p = mock.patch("ansible.module_utils.basic.AnsibleModule")
    mock_module = p.start()
    mock_module.params = {
        'gather_subset': ['virtual']
    }

    mock_module.run_command.return_value = (0, 'QEMU', None)
    mock_module.get_bin_path.return_value = '/sbin/sysctl'

    fact_mock = mock.MagicMock()

    p1 = mock.patch("ansible.module_utils.facts.virt.freebsd.VirtualSysctlDetectionMixin.detect_sysctl")
    p2 = mock.patch("ansible.module_utils.facts.virt.freebsd.VirtualSysctlDetectionMixin.get_sysctl")


# Generated at 2022-06-13 04:21:37.171623
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    import ansible.module_utils.facts.virtual.virt_detect as virt_detect
    # Need to test class, because virt_detect doesn't contain any functions
    class FakeModule:
        def __init__(self):
            self.module = None
            self.params = []

    class FakeFactCollector:
        def __init__(self, module):
            self.module = module
            self.objs = []

        def add(self, obj):
            self.objs.append(obj)

    class FakeObj:
        def __init__(self, module):
            self.module = module
            self.fact_subsets = {}

        def populate_facts(self, collected_facts):
            pass

        def populate_fact_subsets(self, collected_facts):
            pass


# Generated at 2022-06-13 04:21:49.676383
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    from ansible.module_utils.facts.virtual.freebsd import VirtualSysctlDetectionMixin

    key = 'hw.model'
    out = 'OpenBSD'
    rc = 0

    class test_class:
        def run_command(self, arg):
            return rc, out, None

        def get_bin_path(self, arg):
            return '/sbin/sysctl'

        module = test_class()

    fact = VirtualSysctlDetectionMixin()
    fact.sysctl_path = '/sbin/sysctl'
    fact.module = test_class()
    result = fact.detect_virt_vendor(key)
    assert result['virtualization_type'] == 'vmm'
    assert result['virtualization_role'] == 'guest'


# Generated at 2022-06-13 04:21:53.210343
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    detection = VirtualSysctlDetectionMixin()
    detection.module = MockModule()
    detection.detect_sysctl = Mock(return_value=None)
    detection.detect_virt_product('security.jail.jailed')
    assert detection.sysctl_path == '/usr/bin/sysctl'


# Generated at 2022-06-13 04:21:59.456285
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    class Mixin_Mock(VirtualSysctlDetectionMixin):
        def detect_sysctl(self):
            pass

    class Module_Mock:
        def __init__(self):
            self.params = dict()

        def get_bin_path(self, *args, **kwargs):
            return '/bin/test'

        def run_command(self, *args, **kwargs):
            return 0, 'OpenBSD', ''

    m = Mixin_Mock()
    m.module = Module_Mock()
    # init
    host_tech = set()
    guest_tech = set()
    virtual_vendor_facts = {
      'virtualization_tech_host': host_tech,
      'virtualization_tech_guest': guest_tech
    }
    assert virtual_vendor_facts == m

# Generated at 2022-06-13 04:22:19.163713
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    class TestClass(VirtualSysctlDetectionMixin):
        def __init__(self, module):
            self.module = module

    import sys
    import ansible.module_utils
    module = ansible.module_utils.basic.AnsibleModule(argument_spec={})
    module.exit_json = sys.exit
    module.fail_json = sys.exit

    test_object = TestClass(module)
    result = test_object.detect_virt_vendor('hw.product')
    assert result == {'virtualization_type': 'kvm', 'virtualization_role': 'guest', 'virtualization_tech_guest': set(['kvm']), 'virtualization_tech_host': set([])}


# Generated at 2022-06-13 04:22:23.767261
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    # create an instance of class VirtualSysctlDetectionMixin
    m = VirtualSysctlDetectionMixin()
    # We don't have sysctl on Linux, so the returned dict is empty
    empty_dict = m.detect_virt_vendor('hw.model')
    assert not empty_dict
    assert empty_dict == {}



# Generated at 2022-06-13 04:22:34.584229
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    """ Unit test for method VirtualSysctlDetectionMixin.detect_virt_product. """
    class MockModule(object):
        """ Mock class for AnsibleModule. """
        def __init__(self):
            pass

        def fail_json(self, *args, **kwargs):
            """ fail_json. """
            raise Exception("fail_json was called")

        def get_bin_path(self, *args, **kwargs):
            """ Get bin path. """
            return '/sbin/sysctl'

        def run_command(self, *args, **kwargs):
            """ Run command. """
            return (0, 'Unknown', '')

    class MockOSAPIMixin(object):
        """ Mock class for OSAPIMixin. """
        def __init__(self):
            pass


# Generated at 2022-06-13 04:22:38.922190
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    """ Unit test for method detect_virt_vendor of class
    VirtualSysctlDetectionMixin.
    """
    facter = VirtualSysctlDetectionMixin()
    facter._system_virtualization = "None"
    facter.sysctl_path = None
    facter.sysctl_path = "/usr/bin/sysctl"
    out = facter.detect_virt_vendor('kern.vm_guest')
    assert "virtualization_type" in out
    assert "virtualization_role" in out
    assert out["virtualization_role"] == 'guest'
    assert "virtualization_tech_guest" in out
    assert out["virtualization_tech_guest"] == set(['kvm'])
    assert "virtualization_tech_host" in out

# Generated at 2022-06-13 04:22:49.324115
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    class MockModule(object):
        class MockRunCommand(object):
            foo = 0
            bar = 1
            stdout = None

            @classmethod
            def set_rc(cls, rc):
                cls.foo = rc

            @classmethod
            def set_stdout(cls, stdout):
                cls.stdout = stdout

        def run_command(self, cmd, check_rc=True):
            return self.MockRunCommand.foo, self.MockRunCommand.stdout, None

        def get_bin_path(self, cmd, opt_dirs=[]):
            return "/usr/sbin/sysctl"

    module = MockModule()

    # valid sysctl output and path
    module.MockRunCommand.set_rc(0)
    module.MockRunCommand.set

# Generated at 2022-06-13 04:23:00.117382
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    m = VirtualSysctlDetectionMixin()
    m.module = Mock()
    m.module.run_command.return_value = (0, 'QEMU', '')
    assert m.detect_virt_vendor('machdep.hypervisor') == {'virtualization_tech_host': set(), 'virtualization_tech_guest': {'kvm'}, 'virtualization_type': 'kvm', 'virtualization_role': 'guest'}
    assert m.module.run_command.called
    m.module.run_command.return_value = (0, 'OpenBSD', '')

# Generated at 2022-06-13 04:23:06.623676
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    class Module(object):
        """Class to represent AnsibleModule object in unit tests"""
        def __init__(self, *args, **kwargs):
            """Create Module object"""
            args = ()
            self.params = kwargs
            self.params['_ansible_verbosity'] = 0

        def get_bin_path(self, *args, **kwargs):
            """Stub for get_bin_path"""
            return '/sbin/sysctl'

        def run_command(self, *args, **kwargs):
            """Stub for run_command"""
            return (0, 'QEMU', '')

    class OpenBSDVirtualSysctlDetectionMixin(object):
        """Mock class to test detect_virt_vendor method"""
        def __init__(self):
            self.module = Module()

# Generated at 2022-06-13 04:23:17.041108
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    class MockModule(object):
        def __init__(self):
            self.params = {}

        class MockRunCommand(object):
            def __init__(self, module):
                self.module = module

            def run_command(self, cmd):
                rc = 0
                out = 'QEMU'
                err = ''
                return rc, out, err

        def run_command(self, cmd):
            return self.MockRunCommand(self).run_command(cmd)

    class MockSysctlDetectionMixin(object):
        def __init__(self):
            self.sysctl_path = None
            self.module = MockModule()

    mixin = MockSysctlDetectionMixin()
    mixin.detect_sysctl = VirtualSysctlDetectionMixin.detect_sysctl
    mixin

# Generated at 2022-06-13 04:23:28.224498
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():

    subj = VirtualSysctlDetectionMixin()


# Generated at 2022-06-13 04:23:38.565546
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    class MockModule(object):
        def get_bin_path(self, path):
            return '/sbin/sysctl'
        def run_command(self, command):
            out = 'OpenBSD'
            return 0, out, ''

    class Mock(VirtualSysctlDetectionMixin):
        def __init__(self):
            self.module = MockModule()

    roles = {'guest': set(('vmm',)), 'host': set()}
    virtual_vendor_facts = {'virtualization_type': 'vmm',
                            'virtualization_role': 'guest',
                            'virtualization_tech': roles}
    key = 'kern.vm_guest'
    virtual_facts = Mock()
    vendor_facts = virtual_facts.detect_virt_vendor(key)
    assert vendor

# Generated at 2022-06-13 04:24:14.200102
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    # pylint: disable=line-too-long,no-self-use
    class _VirtualSysctlDetectionMixinTest(VirtualSysctlDetectionMixin):
        def __init__(self):
            self.module = AnsibleModule(
                argument_spec={
                },
                supports_check_mode=True
            )

    # run test
    test_vm = _VirtualSysctlDetectionMixinTest()
    test_vm.sysctl_path = "/usr/bin/sysctl"
    test_vm.module.run_command = MagicMock(return_value=(0, 'Hyper-V', ''))
    result = test_vm.detect_virt_product("machdep.hypervisor_type")

# Generated at 2022-06-13 04:24:22.232404
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    # Imports are local to this function to speed up pytest
    from ansible.module_utils import basic

    # collect output from sysctl -n key1
    out1 = 'XenPVHVM'
    # collect output from sysctl -n key2
    out2 = 'kvm'
    # collect output from sysctl -n key3
    out3 = '0'
    # collect output from sysctl -n key4
    out4 = 'VMware'
    # collect output from sysctl -n key5
    out5 = 'RHEV Hypervisor'
    # collect output from sysctl -n key6
    out6 = 'VirtualBox'
    # collect output from sysctl -n key7
    out7 = 'Parallels'
    # collect output from sysctl -n key8

# Generated at 2022-06-13 04:24:26.962023
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    module = VirtualSysctlDetectionMixin()

    for key in module._SYSCTL_VIRT_PRODUCTS:
        module.detect_virt_product(key)


# Generated at 2022-06-13 04:24:39.313639
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():

    from ansible.module_utils.facts.system.bsd import VirtualSysctlDetectionMixin
    from ansible.module_utils.facts.system.bsd import OpenBSDBSD
    from collections import namedtuple

    FakeModule = namedtuple('FakeModule', ('run_command'))

    FakeRunCommand = namedtuple('FakeRunCommand', ('rc', 'out', 'err'))

    openbsd = OpenBSDBSD(FakeModule(run_command=lambda cmd, path=None: FakeRunCommand(rc=0, out="QEMU", err="")))
    openbsd.detect_virt_vendor()

    assert openbsd.virtual_vendor_facts['virtualization_type'] == 'kvm'
    assert openbsd.virtual_vendor_facts['virtualization_role'] == 'guest'

# Generated at 2022-06-13 04:24:48.419983
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    class MockSysModule():
        def get_bin_path(self, arg):
            return "/usr/bin/sysctl"

        def run_command(self, arg):
            if arg == '/usr/bin/sysctl -n hw.product':
                return (0, 'OpenBSD\n', '')
            elif arg == '/usr/bin/sysctl -n security.jail.jailed':
                return (0, '0\n', '')
            else:
                return (0, 'some_other_test_value\n', '')

    class FakeModule:
        def __init__(self):
            self.module = MockSysModule()

        def fail_json(self, msg):
            self.msg = msg

    sysctl = VirtualSysctlDetectionMixin()
    sysctl.module = FakeModule()

# Generated at 2022-06-13 04:24:54.004526
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    from ansible.module_utils.facts.virtual.os import OS
    target = OS()

    def detect_sysctl(self):
        self.sysctl_path = 'not_existing_binary'

    target.detect_sysctl = detect_sysctl.__get__(target, OS)
    target.sysctl_path = '/sbin/sysctl'

    result = target.detect_virt_product("hw.product")
    assert len(result) == 2
    assert len(result['virtualization_tech_guest']) == 1
    assert 'virtualbox' in result['virtualization_tech_guest']

    result = target.detect_virt_product("hw.product_version")
    assert len(result['virtualization_tech_guest']) == 1

# Generated at 2022-06-13 04:25:02.830635
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    # VirtualSysctlDetectionMixin instance
    virtual_sysctl_detection_mixin = VirtualSysctlDetectionMixin()

    # VirtualSysctlDetectionMixin.detect_sysctl mock
    mock_detect_sysctl = 'mock_detect_sysctl'
    virtual_sysctl_detection_mixin.detect_sysctl = mock_detect_sysctl

    # VirtualSysctlDetectionMixin.sysctl_path mock
    mock_sysctl_path = 'sysctl_path'
    virtual_sysctl_detection_mixin.sysctl_path = mock_sysctl_path

    # VirtualSysctlDetectionMixin.module mock

# Generated at 2022-06-13 04:25:13.937832
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    from ansible.module_utils.facts.system.openbsd import VirtualSysctlDetectionMixin
    virtual_sysctl_mixin = VirtualSysctlDetectionMixin()
    class Module(object):
        def get_bin_path(self, arg):
            return '/sbin/sysctl'
        def run_command(self, command):
            if command == '/sbin/sysctl -n hw.product':
                return 0, 'QEMU', ''
            elif command == '/sbin/sysctl -n machdep.virtual_avail':
                return 0, '1', ''
        class AnsibleModule(object):
            def __init__(self, arg):
                self.arg = arg
        class AVM(object):
            def __init__(self, arg):
                self.arg = arg

# Generated at 2022-06-13 04:25:21.452308
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    obj = VirtualSysctlDetectionMixin()
    obj.sysctl_path = '/usr/bin/sysctl'
    obj.module = FakeAnsibleModule()
    obj.module.run_command = my_run_command
    assert obj.detect_virt_vendor('hw.product') == {'virtualization_type': 'vmm', 'virtualization_role': 'guest', 'virtualization_tech_host': set(), 'virtualization_tech_guest': set(['vmm'])}



# Generated at 2022-06-13 04:25:32.472458
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    from ansible.module_utils.facts.system.bsd import VirtualSysctlDetectionMixin
    from ansible.module_utils.facts.system.bsd import VirtualSysctlModule

    # Create a testing class that has a run_command method
    class TestVirtualSysctlModule(VirtualSysctlDetectionMixin, VirtualSysctlModule):
        def __init__(self):
            self.module = AnsibleModuleMock()
            self.sysctl_path = 'sysctl'
        def run_command(self, cmd):
            rc = 0
            out = ''
            err = ''
            # Read the output of the command and return the results
            if cmd == 'sysctl -n security.jail.jailed':
                rc = 0
                out = 'FreeBSD'
                err = ''

# Generated at 2022-06-13 04:26:25.417597
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    ovsdm_module_args = dict(
        ansible_facts={},
        ansible_sysctl='/bin/sysctl',
        ansible_system='OpenBSD',
        ansible_product_name='OpenBSD vmm'
    )
    ovsdm_obj = VirtualSysctlDetectionMixin()
    ovsdm_obj.module = FakeAnsibleModule(ovsdm_module_args)
    ovsdm_obj.detect_sysctl()
    virtual_vendor_facts = ovsdm_obj.detect_virt_vendor('security.jail.jailed')
    assert (virtual_vendor_facts['virtualization_type'] == 'vmm')
    assert (virtual_vendor_facts['virtualization_role'] == 'guest')


# Generated at 2022-06-13 04:26:36.057745
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    #Use the VirtualSysctlDetectionMixin class to create a Test class so that we can unit test the detect_virt_vendor method

    class Test(VirtualSysctlDetectionMixin):

        def __init__(self, module):
            self.module = module

    import ansible.module_utils.basic
    module = ansible.module_utils.basic.AnsibleModule(
        argument_spec={
            "key": dict(type="str", required=True),
            "sysctl_path": dict(type="str", required=True),
            "out": dict(type="str", required=True),
        }
    )

    instance = Test(module)
    instance.sysctl_path = module.params['sysctl_path']

    actual = instance.detect_virt_vendor(module.params['key'])



# Generated at 2022-06-13 04:26:45.466781
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    from ansible.module_utils.facts import VirtualSysctlDetectionMixin

    # Create a class that can perform the sysctl call
    class FakeModule:
        def get_bin_path(self, cmd, required=False):
            return '/sbin/sysctl'

        def run_command(self, cmd):
            return 0, 'QEMU', ''

    class FakeFacts:
        def __init__(self):
            self.module = FakeModule()

    # Instantiate a class that has the class to be tested mixed in.
    # Since the mixin is only supposed to be used in classes with a module,
    # this should really only be unit tests of the mixin
    class NewFacts(VirtualSysctlDetectionMixin, FakeFacts):
        pass

    # Actual test
    new_facts = NewFacts()


# Generated at 2022-06-13 04:26:57.042774
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    class Test:
        def __init__(self):
            self.module = True

        def get_bin_path(self, name, required=False):
            return 'sysctl'

        def run_command(self, cmd):
            return (0, 'KVM', '')

    t = Test()
    mixin = VirtualSysctlDetectionMixin()
    mixin.detect_sysctl = lambda: None
    mixin.module = t
    assert mixin.detect_virt_product(
        'hw.model') == {
            'virtualization_type': 'kvm',
            'virtualization_role': 'guest',
            'virtualization_tech_guest': set(['kvm']),
            'virtualization_tech_host': set(),
        }


# Generated at 2022-06-13 04:27:08.705189
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    class BSD():
        def __init__(self):
            self.name = "BSD"
            self.sysctl_path = "/usr/sbin/sysctl"

    class VM():
        def __init__(self):
            self.name = "VM"
            self.sysctl_path = "/usr/sbin/sysctl"

    class Dummy:
        def __init__(self):
            self.name = "Dummy"
            self.sysctl_path = None

    class TestModule:
        def __init__(self):
            self.facts = dict()
            self.facts['ansible_architecture'] = 'amd64'
            self.run_command = self.run_command_impl


# Generated at 2022-06-13 04:27:18.400247
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    class TestModule:
        def get_bin_path(self, module, *args, **kwargs):
            return '/sbin/sysctl'
        def run_command(self, module, *args, **kwargs):
            return (0, 'QEMU\n', None)

    class Test_VirtualSysctlDetectionMixin(VirtualSysctlDetectionMixin):
        def __init__(self):
            self.module = TestModule()

    my_test_object = Test_VirtualSysctlDetectionMixin()

    results = my_test_object.detect_virt_vendor('hw.product')
    assert results['virtualization_type'] == 'kvm',\
        "QEMU vendor string not converted to kvm virtualization_type"


# Generated at 2022-06-13 04:27:27.099542
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    mock_module = MockModule({'sysctl': '/usr/sbin/sysctl'})
    mock_module.command_complete = True
    mock_module.command_rc = 0
    mock_module.command_stdout = 'OpenBSD'
    task_obj = VirtualSysctlDetectionMixin()
    task_obj.module = mock_module
    expected = {
        'virtualization_tech_guest': {'vmm'},
        'virtualization_tech_host': set(),
        'virtualization_type': 'vmm',
        'virtualization_role': 'guest',
    }
    result = task_obj.detect_virt_vendor("machdep.vm_guest")
    assert result == expected


# Generated at 2022-06-13 04:27:35.296681
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    class FakeModule(object):
        def __init__(self):
            self.params = {}
            self.exit_json = lambda **kwargs: kwargs
            self.run_command = FakeModule.run_command

        def run_command(self, cmd):
            return 1, '', ''

    FakeModule.run_command = lambda self, cmd: (0, 'KVM', '')
    assert VirtualSysctlDetectionMixin().detect_virt_product('hw.model') == {'virtualization_type': 'kvm', 'virtualization_role': 'guest'}

    FakeModule.run_command = lambda self, cmd: (0, 'VMware', '')

# Generated at 2022-06-13 04:27:44.559754
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    from ansible.module_utils.facts.collector import FactsCollector

    data = {}
    data[key] = 'VirtualBox'
    data[key2] = 'HVM'


    class MyModule():
        def __init__(self, data):
            self.data = data
            self.run_command = mock_run_command


        def get_bin_path(self, key):
            if key == 'sysctl':
                return '/sbin/sysctl'

    class MyFactsCollector(VirtualSysctlDetectionMixin, FactsCollector):
        pass

    class MyFactsCollector1(VirtualSysctlDetectionMixin, FactsCollector):
        def __init__(self, data):
            self.data = data
            self.run_command = mock_run_command_real


# Generated at 2022-06-13 04:27:55.283878
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    class MockModule:
        def __init__(self, rc, out, err):
            self.rc = rc
            self.out = out
            self.err = err

        def get_bin_path(self, executable):
            return '/bin/sysctl'

        def run_command(self, cmd):
            return self.rc, self.out, self.err

    mixin_object = VirtualSysctlDetectionMixin()
    module_case1 = MockModule(0, 'KVM', '')
    module_case2 = MockModule(0, 'VMware', '')
    module_case3 = MockModule(0, 'VirtualBox', '')
    module_case4 = MockModule(0, 'HVM domU', '')
    module_case5 = MockModule(0, 'XenPVH', '')


# Generated at 2022-06-13 04:29:46.362045
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector.virtual.sysctl import VirtualSysctlDetectionMixin

    class MockModule(object):
        def __init__(self):
            self.params = {}
            self.params['gather_subset'] = ['all']
            self.run_command = run_command
            self.get_bin_path = get_bin_path

    class MockCollector(VirtualSysctlDetectionMixin, BaseFactCollector):
        def __init__(self, module):
            BaseFactCollector.__init__(self, module)
            self.collect_methods = ['detect_virt_product']


# Generated at 2022-06-13 04:29:55.287191
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    virtual_product_facts = {}
    key = 'hw.product'
    out = 'VirtualBox'
    rc = 0
    guest_tech = set()
    found_virt = False
    host_tech = set()
    virtual_product_facts['virtualization_type'] = 'virtualbox'
    virtual_product_facts['virtualization_role'] = 'guest'
    guest_tech.add('virtualbox')
    virtual_product_facts['virtualization_tech_guest'] = guest_tech
    virtual_product_facts['virtualization_tech_host'] = host_tech
    assert VirtualSysctlDetectionMixin.detect_virt_product(VirtualSysctlDetectionMixin(), key, out, rc, found_virt) == virtual_product_facts

# Generated at 2022-06-13 04:29:59.666086
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    from ansible.module_utils import basic
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_text

    module_class = basic.AnsibleModule
    module_class._ansible_module = AnsibleModule
    module_class._ansible_module.run_command = lambda *a, **kw: (0, 'KVM', '')
    module_class._ansible_module.get_bin_path = lambda *a, **kw: '/usr/bin/sysctl'
    module_class._ansible_module.params = {'key': 'hw.model', }

    d = VirtualSysctlDetectionMixin()
    res = d.detect_virt_product('hw.model')
    assert res['virtualization_role'] == 'guest'

# Generated at 2022-06-13 04:30:10.920317
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    class BSDModule(object):
        def __init__(self):
            self.params = dict()
            self.params['failed'] = 0
            self.params['changed'] = 0

        def fail_json(self, *args, **kwargs):
            self.params['failed'] = 1

        def exit_json(self, *args, **kwargs):
            pass

        def get_bin_path(self, name, opt_dirs=None, required=False):
            return '/sbin/sysctl'

        def run_command(self, cmd):
            return (0, "KVM", "")

    class TestFacts(VirtualSysctlDetectionMixin):
        def __init__(self):
            self.module = BSDModule()

    test_instance = TestFacts()

# Generated at 2022-06-13 04:30:16.882617
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    from ansible.modules.system.setup import setup_bsd

    sysctl_mixin = VirtualSysctlDetectionMixin()
    sysctl_mixin.module = object()
    sysctl_mixin.module.get_bin_path = lambda x: 'sysctl'
    sysctl_mixin.module.run_command = lambda cmd: (0, 'OpenBSD', None)

    expected = {'virtualization_tech_guest': set(['vmm']),
                'virtualization_tech_host': set([]),
                'virtualization_type': 'vmm',
                'virtualization_role': 'guest'
               }
    facts = setup_bsd.get_all_facts(sysctl_mixin)
    assert facts['virtualization_vendor'] == expected


# Generated at 2022-06-13 04:30:20.215968
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():

    class FakeModule(object):
        def get_bin_path(self, path):
            return '/sbin/sysctl'

        def run_command(cmd):
            rc = 0
            out = 'QEMU'
            err = ''
            return rc, out, err

        def __init__(self):
            self.run_command = self
            self.get_bin_path = self

    module = FakeModule()
    VirtualSysctlDetectionMixin.detect_virt_vendor(module)