

# Generated at 2022-06-13 04:20:36.520881
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    virtual_product_facts = {}
    class MockModule(object):
        def get_bin_path(self, executable):
            return '/usr/bin/sysctl'
        def run_command(self, cmd):
            return 0, 'bogus\nKVM', 'bogus'
    class VirtualSysctlDetectionMixinObj(VirtualSysctlDetectionMixin):
        def __init__(self):
            self.module = MockModule()
    sdmx = VirtualSysctlDetectionMixinObj()
    virtual_product_facts = sdmx.detect_virt_product('security.jail.jailed')
    assert virtual_product_facts['virtualization_type'] == 'kvm'
    assert virtual_product_facts['virtualization_role'] == 'guest'

# Generated at 2022-06-13 04:20:38.369223
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    # The tests for this method are in the linux/bsd file for the class.
    pass


# Generated at 2022-06-13 04:20:47.074618
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    from ansible.module_utils import basic
    from ansible.module_utils.facts import virtual

    class MockModule(object):
        def __init__(self, run_command_fn):
            self.run_command = run_command_fn

        def get_bin_path(self, _):
            return self.sysctl_path

    class MockRunCommand(object):
        def __init__(self, rc, out, err):
            self.rc = rc
            self.out = out
            self.err = err

        def __call__(self, *_):
            return self.rc, self.out, self.err

    module = MockModule(MockRunCommand(0, 'Parallels', ''))
    module.sysctl_path = '/sbin/sysctl'
    vsdmix = virtual.VirtualSys

# Generated at 2022-06-13 04:20:55.335181
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    # Create class instance
    virtual_sysctl_detection_mixin = VirtualSysctlDetectionMixin()

    # Create mock method
    virtual_sysctl_detection_mixin.detect_sysctl = mock_detect_sysctl_true

    virtual_product_facts = virtual_sysctl_detection_mixin.detect_virt_product('hw.product')
    assert virtual_product_facts['virtualization_type'] == 'kvm'
    assert virtual_product_facts['virtualization_role'] == 'guest'
    assert virtual_product_facts['virtualization_tech_guest'] == {'kvm'}
    assert virtual_product_facts['virtualization_tech_host'] == set()


# Generated at 2022-06-13 04:21:07.875055
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    class ModuleUtil(object):
        def run_command(self, cmd):
            return (0, 'VMware', '')
    module_util = ModuleUtil()
    class SysctlDetection(VirtualSysctlDetectionMixin):
        def __init__(self):
            self.module = module_util
            self.sysctl_path = 'sysctl'
            self.detect_sysctl()
    sysctl = SysctlDetection()
    guest_tech = set()
    guest_tech.add('VMware')
    virtual_product_facts = {}
    virtual_product_facts['virtualization_type'] = 'VMware'
    virtual_product_facts['virtualization_role'] = 'guest'

# Generated at 2022-06-13 04:21:17.655472
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    from ansible.module_utils.facts.system.virtual import VirtualSysctlDetectionMixin
    class MySUT(VirtualSysctlDetectionMixin):
        pass

    sut = MySUT()
    sut.sysctl_path = '/usr/bin/sysctl'
    sut.module = MockModule()

    sut.module._return_values = [
        0,
        'QEMU\n',
        None,
    ]
    virtual_vendor_facts = sut.detect_virt_vendor('hw.model')
    assert(virtual_vendor_facts['virtualization_type'] == 'kvm')
    assert(virtual_vendor_facts['virtualization_role'] == 'guest')
    assert('kvm' in virtual_vendor_facts['virtualization_tech_guest'])

# Generated at 2022-06-13 04:21:28.541120
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    class MockedModule(object):
        def get_bin_path(self, arg):
            return os.path.realpath(os.path.join(os.getcwd(), '__mocked_bin_path__'))

        @staticmethod
        def run_command(cmd):
            return 1, '', ''

    from ansible.module_utils.facts.virtual.freebsd import VirtualSysctlDetectionMixin

    class MockedOs(object):
        path = os.path

    # python 2.6 doesn't support mock_open()
    if sys.version_info[:2] == (2, 6):
        with open('/var/run/dmesg.boot') as dmesg_boot:
            dmesg_boot_str = dmesg_boot.read()
        MockedModule.run_command

# Generated at 2022-06-13 04:21:34.279547
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    from ansible.module_utils.facts.system.bsd import VirtualSysctlDetectionMixin
    import pytest
    class MockSystem(object):
        def __init__(self):
            self.sysctl_path = '/sbin/sysctl'

    class MockModule(object):
        def __init__(self):
            self.system = MockSystem()
            self.run_command = MockSystem.run_command

        def get_bin_path(self, arg1):
            if arg1 == 'sysctl':
                return '/sbin/sysctl'
            else:
                return None

        @staticmethod
        def run_command(command):
            if command == '/sbin/sysctl -n hw.product':
                return 0, 'OpenBSD', ''
            return 0, '', ''

    BSD_V

# Generated at 2022-06-13 04:21:40.734369
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    module = FakeAnsibleModule()

    # Test detection of kvm
    sdc = VirtualSysctlDetectionMixin()
    facts = sdc.detect_virt_product('machdep.cpu.features')
    assert 'kvm' in facts['virtualization_tech_guest']
    assert 'kvm' == facts['virtualization_type']

    # Test detection of VMware
    sdc = VirtualSysctlDetectionMixin()
    facts = sdc.detect_virt_product('machdep.cpu.features')
    assert 'VMware' in facts['virtualization_tech_guest']
    assert 'VMware' == facts['virtualization_type']

    # Test detection of VirtualBox
    sdc = VirtualSysctlDetectionMixin()

# Generated at 2022-06-13 04:21:52.167994
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    from ansible.utils.virtualization import VirtualizationCollector
    from ansible.module.utils.facts.collector import get_file_content
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.facts import VirtualizationFactCollector

    class TestVM(object):
        def __init__(self):
            self.module = FakeAnsibleModule()
            self.sysctl_path = "echo"

        def detect_sysctl(self):
            pass

    class FakeAnsibleModule(object):
        def __init__(self):
            self.params = {}
            self.args = {}

        def get_bin_path(self, arg):
            return "echo"


# Generated at 2022-06-13 04:22:11.958195
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    req_1 = {'virtualization_type': 'kvm', 'virtualization_role': 'guest'}
    req_2 = {'virtualization_type': 'VMware', 'virtualization_role': 'guest'}
    req_3 = {'virtualization_type': 'virtualbox', 'virtualization_role': 'guest'}
    req_4 = {'virtualization_type': 'xen', 'virtualization_role': 'guest'}
    req_5 = {'virtualization_type': 'Hyper-V', 'virtualization_role': 'guest'}
    req_6 = {'virtualization_type': 'parallels', 'virtualization_role': 'guest'}
    req_7 = {'virtualization_type': 'RHEV', 'virtualization_role': 'guest'}
   

# Generated at 2022-06-13 04:22:23.156078
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    result = {
        'virtualization_type': 'kvm',
        'virtualization_role': 'guest',
        'virtualization_tech_host': set(),
        'virtualization_tech_guest': set()
    }
    class Module(object):
        def run_command(self, cmd):
            return 0, 'kvm', ''

        def get_bin_path(self, cmd):
            return '/usr/bin/sysctl'

    class VirtualSysctlDetectionMixin(object):
        def __init__(self, module):
            self.module = module
            self.sysctl_path = ''

    testclass = VirtualSysctlDetectionMixin(Module())
    assert testclass.detect_virt_product('machdep.cpu.features') == result
    assert testclass.detect_virt_product

# Generated at 2022-06-13 04:22:30.440505
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    fact_subclass = VirtualSysctlDetectionMixin()


# Generated at 2022-06-13 04:22:41.432735
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    class FakeModule():
        def get_bin_path(self, executable):
            return '/usr/bin/sysctl'
        def run_command(self, command):
            return 0, 'VirtualBox', ''

    class FakeSystem():
        def __init__(self, module):
            self.detect_sysctl = VirtualSysctlDetectionMixin.detect_sysctl
            self.detect_virt_product = VirtualSysctlDetectionMixin.detect_virt_product
            self.sysctl_path = None
            self.module = module

    fake_system = FakeSystem(FakeModule())

    # Test if sysctl returns what we expect an if the right class is returned
    # The return value should be a dictionary with the following keys:
    # virtualization_tech_guest, virtualization_tech_host,
    # virtual

# Generated at 2022-06-13 04:22:51.036084
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    import sys
    sys.path.append("..")

    class FakeModule(object):
        def __init__(self):
            self.run_command_line_rc = 0
            self.run_command_line_output = 'OpenBSD'

        def get_bin_path(self, arg):
            return 'fake_path'

        def run_command(self, cmd):
            return (self.run_command_line_rc, self.run_command_line_output, None)

    class OpenBSD(VirtualSysctlDetectionMixin):
        def __init__(self, module):
            self.module = module

    # Setup an example object
    fake_module = FakeModule()
    obj = OpenBSD(fake_module)
    obj.detect_virt_vendor('')
    assert obj.virtualization_type

# Generated at 2022-06-13 04:23:00.977799
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    module = MockModule('test_VirtualSysctlDetectionMixin_detect_virt_product')
    mod = VirtualSysctlDetectionMixin()

    # sysctl("security.jail.jailed") returns 1
    mod.sysctl_path = 'sysctl'
    rc, out, err = module.run_command("%s -n security.jail.jailed" % mod.sysctl_path)
    module.assertEqual(rc, 0)
    module.assertEqual(out, "1\n")

    # Virtualization tech should be jails, virtualization type should be jails, virtualization role should be guest
    virtual_product_facts = mod.detect_virt_product('security.jail.jailed')

# Generated at 2022-06-13 04:23:07.652213
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    module = VirtualSysctlDetectionMixin()
    virtual_facts = {}
    virtual_facts['virtualization_type'] = 'hyperv'
    virtual_facts['virtualization_role'] = 'guest'
    virtual_facts['virtualization_tech'] = set(['hyperv'])
    virtual_facts['virtualization_tech_guest'] = set(['hyperv'])

    assert virtual_facts == module.detect_virt_product('machdep.hyperv.features')


# Generated at 2022-06-13 04:23:17.398333
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    class MockModule:
        def __init__(self):
            self.params = {}
        def get_bin_path(self, arg):
            return '/sbin/sysctl'
        def run_command(self, arg):
            return 0, "KVM", ""

    mock = MockModule()
    facts = VirtualSysctlDetectionMixin()
    facts.module = mock
    virtual_product_facts = facts.detect_virt_product('hw.model')

    assert virtual_product_facts['virtualization_type'] == 'kvm'
    assert virtual_product_facts['virtualization_role'] == 'guest'
    assert 'vt-d' not in virtual_product_facts['virtualization_tech_host']
    assert 'nested' not in virtual_product_facts['virtualization_tech_host']

# Generated at 2022-06-13 04:23:28.396945
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    """Test sysctl-based detection of vendor."""

    class TestVirtModule:
        def get_bin_path(self, *args, **kwargs):
            return '/sbin/sysctl'

        def run_command(self, *args, **kwargs):
            output = {
                'security.jail.get_host_hostuuid': 1,
                'security.jail.jailed': 0,
                'vm.vmtotal': 1
            }.get(args[1], 'foo')

            return 0, output, ''

    class TestFactModule(VirtualSysctlDetectionMixin):
        def __init__(self, module):
            self.module = module

    test_module = TestVirtModule()
    test_fact_module = TestFactModule(test_module)

# Generated at 2022-06-13 04:23:38.695711
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    mixin = VirtualSysctlDetectionMixin()
    mixin.module = MockAnsibleModule()
    mixin.module.run_command = MockRunCommand() 
    mixin.module.run_command.setRc(0)

    # Case1: test kvm
    mixin.module.run_command.setOut('KVM')
    result = mixin.detect_virt_product('hw.model')
    assert result['virtualization_type'] == 'kvm'
    assert result['virtualization_role'] == 'guest'
    assert result['virtualization_tech_guest'] == set(['kvm'])
    assert result['virtualization_tech_host'] == set()
    # Case2: test vmware
    mixin.module.run_command.setOut('VMware')
    result = mix

# Generated at 2022-06-13 04:24:12.050203
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    # Create Instance of VirtualSysctlDetectionMixin
    class_object = VirtualSysctlDetectionMixin()

    # Create Fake Module
    class_object.module = FakeModule()

    # Test VirtualSysctlDetectionMixin.detect_virt_product for VirtualBox
    class_object.detect_virt_product('hw.product')
    assert class_object.sysctl_path == '/sbin/sysctl'
    assert class_object.module.run_command.call_count == 1
    assert class_object.module.run_command.call_args == call('/sbin/sysctl -n hw.product')
    assert class_object.module.run_command.return_value == (0, 'VirtualBox', 'stdout')

# Generated at 2022-06-13 04:24:20.840915
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    class test_VirtualSysctlDetectionMixin(VirtualSysctlDetectionMixin):
        def detect_sysctl(self):
            pass

    class mock_module:
        def run_command(self, cmd):
            return 0, 'QEMU', ''

    class mock_ansible_module:
        def __init__(self):
            self.params = {}

        @staticmethod
        def get_bin_path(tool, required=False):
            return

    # Test with QEMU
    test_instance = test_VirtualSysctlDetectionMixin()
    test_instance.module = mock_ansible_module()

# Generated at 2022-06-13 04:24:32.870883
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    class TestModule(object):
        def get_bin_path(self, name):
            return '/sbin/sysctl'
        def run_command(self, cmd):
            if cmd == '/sbin/sysctl -n hw.product':
                return 0, 'OpenBSD', None
            elif cmd == '/sbin/sysctl -n hw.vendor':
                return 0, 'QEMU', None
            elif cmd == '/sbin/sysctl -n security.jail.jailed':
                return 0, '1', None
            else:
                return 1, None, None
    tm = TestModule()

    class TestClass(object):
        def __init__(self):
            self.module = tm
    tc = TestClass()

    v = VirtualSysctlDetectionMixin()

# Generated at 2022-06-13 04:24:43.459298
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
  class ModuleMock(object):
    def __init__(self):
      self.params = dict()
      self.binary_module = False
    def get_bin_path(self, name):
      return "/path/to/bin/" + name

    def run_command(self, cmd):
      return 0, "running command %s" % cmd , ""

  class SysctlDetectionMixinMock(VirtualSysctlDetectionMixin):
    def __init__(self):
      self.module = ModuleMock()

  detection_mixin_mock = SysctlDetectionMixinMock()

  # Test if method detect_virt_product of class VirtualSysctlDetectionMixin detects virtualization product

# Generated at 2022-06-13 04:24:53.214026
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    class VirtualSysctlDetectionMixinTest(object):
        sysctl_path = None
        module = None
    obj = VirtualSysctlDetectionMixinTest()
    obj.detect_virt_vendor = VirtualSysctlDetectionMixin.detect_virt_vendor

    obj.detect_sysctl = test_VirtualSysctlDetectionMixin_detect_sysctl

    obj.module = test_VirtualSysctlDetectionMixin_Module()

    obj.module.run_command = test_VirtualSysctlDetectionMixin_run_command

    virtual_vendor_facts = obj.detect_virt_vendor("hw.product")

# Generated at 2022-06-13 04:24:57.519957
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    test_object = VirtualSysctlDetectionMixin()
    results = test_object.detect_virt_product('hw.model')
    assert results['virtualization_tech_guest'] == set([])
    assert results['virtualization_tech_host'] == set([])


# Generated at 2022-06-13 04:25:08.585962
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    virtual_facts = {}
    tmp_VirtualSysctlDetectionMixin = VirtualSysctlDetectionMixin()
    tmp_VirtualSysctlDetectionMixin.sysctl_path = "/usr/sbin/sysctl"
    tmp_VirtualSysctlDetectionMixin.module = MockModule()

    mock_run_command = [0, 'QEMU', '']
    tmp_VirtualSysctlDetectionMixin.module.run_command = Mock(return_value=mock_run_command)
    virtual_facts = tmp_VirtualSysctlDetectionMixin.detect_virt_vendor('machdep.cpu.brand_string')

    assert virtual_facts['virtualization_type'] == 'kvm'
    assert virtual_facts['virtualization_role'] == 'guest'

# Generated at 2022-06-13 04:25:20.249720
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    from ansible.module_utils.facts.system.virtual import VirtualSysctlDetectionMixin
    from ansible.module_utils.facts.system import virtual

    class FreeBSDVirtual(VirtualSysctlDetectionMixin, object):
        pass

    freebsd = FreeBSDVirtual()
    freebsd_p_facts = freebsd.detect_virt_product('hw.model')
    assert freebsd_p_facts['virtualization_type'] == 'virtualbox'
    assert freebsd_p_facts['virtualization_role'] == 'guest'

    freebsd_p_facts = freebsd.detect_virt_product('security.jail.jailed')
    assert freebsd_p_facts['virtualization_type'] == 'jails'

# Generated at 2022-06-13 04:25:31.164802
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    class VirtualSysctlDetectionMixinImpl(VirtualSysctlDetectionMixin):
        def __init__(self):
            self.module = sysctl_result_mock

    global sysctl_result_mock

    # Test 1: Expetect kvm as virtualization_type
    sysctl_result_mock = sysctl_result_mock_factory('kvm')
    virtual_sysctl_detection_mixin = VirtualSysctlDetectionMixinImpl()
    assert virtual_sysctl_detection_mixin.detect_virt_product('machdep.hypervisor') == {'virtualization_type': 'kvm', 'virtualization_role': 'guest'}

    # Test 2: Expetect VMware as virtualization_type
    sysctl_result_mock = sysctl_result_mock_factory

# Generated at 2022-06-13 04:25:39.334961
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.openbsd.virtual import VirtualSysctlDetectionMixin
    from ansible.module_utils.six import PY3
    from ansible.module_utils.six.moves import StringIO

    class VirtualSysctlDetectionMixinTester(basic.AnsibleModule, VirtualSysctlDetectionMixin):
        """
        Constructor for testing the detect_virt_product method of the class
        VirtualSysctlDetectionMixin
        """
        def __init__(self, *args, **kwargs):
            super(self.__class__, self).__init__(*args, **kwargs)


# Generated at 2022-06-13 04:26:36.544946
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():

    class Obj(object):
        pass

    obj = Obj()
    obj.module = Obj()

    detect_virt_product_key = 'machdep.cpu.brand_string'

    def detect_sysctl_mock(self):
        self.sysctl_path = '/usr/sbin/sysctl'

    obj.detect_sysctl = detect_sysctl_mock

    def run_command_mock(self, cmd):
        return (0, 'Intel(R) Core(TM) i5-4258U CPU @ 2.40GHz', '')

    obj.module.run_command = run_command_mock

    virtual_product_facts = obj.detect_virt_product(detect_virt_product_key)

    assert 'virtualization_role' in virtual_product_facts

# Generated at 2022-06-13 04:26:45.565792
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    class Module(object):
        class run_command(object):
            rc = 0
            err = ''
            def __call__(self, cmd):
                if cmd == '/sbin/sysctl -n hw.model':
                    return self.rc, 'KVM', self.err
                if cmd == '/sbin/sysctl -n security.jail.jailed':
                    return self.rc, '1', self.err
                return 1, '', self.err

        class get_bin_path(object):
            def __call__(self, binary):
                return '/sbin/sysctl'

    class VirtualSysctlDetectionMixinTests(VirtualSysctlDetectionMixin):
        def __init__(self):
            self.module = Module

    v = VirtualSysctlDetectionMixinTests()

# Generated at 2022-06-13 04:26:50.747436
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    import sys
    import os
    import imp

    file, pathname, description = imp.find_module('ansible')
    ansible = imp.load_module('ansible', file, pathname, description)
    imp.load_module('ansible.module_utils.facts', file, pathname, description)
    file, pathname, description = imp.find_module('ansible.module_utils.facts.virtual', os.path.dirname(pathname))
    virtual = imp.load_module('ansible.module_utils.facts.virtual', file, pathname, description)

    class FakeModule(object):
        def __init__(self):
            self.sysctl_path = 'sysctl'
            self._ansible_version = '2.7.0'


# Generated at 2022-06-13 04:26:58.903126
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():

    from ansible.module_utils.facts.system.bsd import VirtualSysctlDetectionMixin

    # mocks
    class FakeVirtModule:
        def get_bin_path(self, command):
            return "/usr/bin/sysctl"

        def run_command(self, command):
            rc = 0
            out = 'QEMU'
            err = ''
            return rc, out, err

    class FakeVirtModuleOBSD(FakeVirtModule):
        def run_command(self, command):
            rc = 0
            out = 'OpenBSD'
            err = ''
            return rc, out, err

    # test virtualization_type=kvm
    fake_module = FakeVirtModule()
    fake_virt = VirtualSysctlDetectionMixin()
    fake_virt.module = fake_module
   

# Generated at 2022-06-13 04:27:09.787548
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    module = Mock()
    obj = VirtualSysctlDetectionMixin(module)

    key = 'machdep.hypervisor.product'
    module.get_bin_path.return_value = '/sbin/sysctl'
    out = 'VMWare ESXi 6.0.0 build-3707948 x86_64'
    module.run_command.return_value = (0, out, '')

    virtual_facts = obj.detect_virt_product(key)
    assert virtual_facts['virtualization_type'] == 'VMware'
    assert virtual_facts['virtualization_role'] == 'guest'
    assert virtual_facts['virtualization_tech_guest'] == set(['VMware'])
    assert virtual_facts['virtualization_tech_host'] == set()


# Generated at 2022-06-13 04:27:17.275065
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    module = get_module_mock()
    virtual_sysctl_detection_mixin = VirtualSysctlDetectionMixin()
    virtual_sysctl_detection_mixin.module = module
    assert virtual_sysctl_detection_mixin.detect_virt_product('kern.vm_guest') \
        == {'virtualization_role': 'guest',
            'virtualization_tech_guest': set(['kvm']),
            'virtualization_tech_host': set([]),
            'virtualization_type': 'kvm'}


# Generated at 2022-06-13 04:27:26.389002
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    from ansible.module_utils.basic import AnsibleModule

    class FakeModule(object):
        def __init__(self, **kwargs):
            self.params = kwargs

        def fail_json(self, *args, **kwargs):
            self.exit_args = args
            self.exit_kwargs = kwargs
            raise Exception('FAIL')

        def exit_json(self, *args, **kwargs):
            self.exit_args = args
            self.exit_kwargs = kwargs

    class FakeSysctlDetectionMixin(VirtualSysctlDetectionMixin):
        def __init__(self, module):
            self.sysctl_path = '/sbin/sysctl'
            self.module = module

        def detect_virt_product(self, key):
            guest_tech = set

# Generated at 2022-06-13 04:27:34.581127
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    class FakeModule(object):
        def get_bin_path(self, _):
            return '/sbin/sysctl'

        def run_command(self, cmd):
            assert cmd == '/sbin/sysctl -n kern.vendor'
            return 0, 'QEMU', ''
    class FakeVirtualSysctlDetectionMixin(VirtualSysctlDetectionMixin):
        module = FakeModule()
    virtual_facts = FakeVirtualSysctlDetectionMixin()
    assert virtual_facts.detect_virt_product('kern.vendor') == {
        'virtualization_type': 'kvm', 'virtualization_role': 'guest',
        'virtualization_tech_guest': {'kvm'}, 'virtualization_tech_host': set()}


# Generated at 2022-06-13 04:27:43.968098
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    class TestModule(object):
        def __init__(self):
            self.get_bin_path = lambda x: 'sysctl'
            self.run_command = lambda x: ['0', 'VirtualBox', '']

    class TestVirtualSysctlDetectionMixin(VirtualSysctlDetectionMixin):
        def __init__(self):
            self.module = TestModule()

    test_object = TestVirtualSysctlDetectionMixin()
    expected_virtual_product_facts = {
        'virtualization_role': 'guest',
        'virtualization_type': 'virtualbox',
        'virtualization_tech_guest': set(['virtualbox']),
        'virtualization_tech_host': set(),
    }
    result = test_object.detect_virt_product('machdep.hypervisor')

# Generated at 2022-06-13 04:27:54.713754
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    class FakeModule:
        class FakeRunCommand:
            def __init__(self,rc,out,err):
                self.rc = rc
                self.out = out
                self.err = err

        def __init__(self):
            self.rc = 0
            self.out = ''
            self.err = ''
            self.sysctl_path = '/test/sysctl'
            self.run_command_list = []

        def get_bin_path(self,cmd):
            return self.sysctl_path

        def run_command(self,cmd):
            if self.rc < len(self.run_command_list):
                return self.run_command_list[self.rc]
            else:
                FakeRunCommand = self.FakeRunCommand
                self.rc = self.rc + 1

# Generated at 2022-06-13 04:29:39.094514
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    # Setup a fake class that we insert our detected values into
    class FakeModule(object):
        def __init__(self):
            self.sysctl_path = '/sbin/sysctl'
            self.facts = dict()

        def get_bin_path(self, value, opt_dirs=[]):
            # osx doesn't have a bin_path
            return self.sysctl_path

        def run_command(self, cmd, check_rc=True):
            # The first is our current vendor with kvm
            if cmd == '/sbin/sysctl -n kern.vm_guest hvm':
                return 0, 'QEMU', ''
            # The second is our current vendor without kvm

# Generated at 2022-06-13 04:29:49.346489
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    def sysctl_run_command(self, cmd, check_rc=True, close_fds=True, executable=None, data=None, binary=False):
        return (0, '', '')

    class VirtualSysctlDetectionMixinTest(VirtualSysctlDetectionMixin):
        def detect_sysctl(self):
            self.sysctl_path = '/usr/bin/sysctl'

        def detect_pv_product(self):
            # Override this method so we don't call pkgutil.
            return {'virtualization_role': 'guest'}

    virtual_sysctl_detection_mixin = VirtualSysctlDetectionMixinTest()

    # check that if sysctl is not available
    # it returns empty result
    virtual_sysctl_detection_mixin.sysctl_path = None
   

# Generated at 2022-06-13 04:29:58.918259
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    class TestModule(object):
        def __init__(self):
            self.run_command_results = [
                [0, 'KVM GUEST', ''],
                [0, 'VMware', ''],
                [0, 'VirtualBox', ''],
                [0, 'HVM domU', ''],
                [0, 'Hyper-V', ''],
                [0, 'Parallels', ''],
                [0, 'RHEV Hypervisor', '']
            ]
            self.run_command_calls = [0]

        def get_bin_path(self, exe):
            return '/sbin/sysctl'

        def run_command(self, args):
            call = self.run_command_calls[0]
            self.run_command_calls[0] += 1
            return self

# Generated at 2022-06-13 04:30:10.743303
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    class FakeModule(object):
        def get_bin_path(self, name):
            if name == 'sysctl':
                return name
        def run_command(self, name):
            if name == 'sysctl -n hw.product':
                return 0, 'KVM', ''
            if name == 'sysctl -n security.jail.jailed':
                return 0, '1', ''
            return 1, '', ''
    keys = ['hw.product', 'security.jail.jailed']
    vm = VirtualSysctlDetectionMixin()
    vm.module = FakeModule()
    vm.detect_sysctl()

    product_results = [vm.detect_virt_product(keys[0]), vm.detect_virt_product(keys[1])]

# Generated at 2022-06-13 04:30:16.834127
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    # Test with sysctl and sysctl_path defined
    class Module(object):
        def __init__(self):
            self.sysctl_path = '/usr/bin/sysctl'
        def run_command(self, cmd):
            return 0, 'Hyper-V', None
        def get_bin_path(self, cmd):
            return self.sysctl_path
    obj = VirtualSysctlDetectionMixin()
    obj.module = Module()
    result = obj.detect_virt_product('machdep.hypervisor_name')
    expected = {'virtualization_type': 'Hyper-V', 'virtualization_role': 'guest'}
    assert result['virtualization_type'] == expected['virtualization_type'], \
        "Virtual Sysctl Detection Mixin detect_virt_product test 1 failed"
   