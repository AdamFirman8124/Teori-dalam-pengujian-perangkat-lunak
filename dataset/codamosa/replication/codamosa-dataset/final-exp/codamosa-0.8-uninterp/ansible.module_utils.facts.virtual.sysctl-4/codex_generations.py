

# Generated at 2022-06-13 04:20:43.535337
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    sysctl_path = 'sysctl'
    module_args = dict(ansible_facts={})
    module_mock = AnsibleModule(argument_spec=dict(), supports_check_mode=True)
    openbsd = VirtualSysctlDetectionMixin()
    openbsd.module = module_mock
    openbsd.sysctl_path = sysctl_path
    virtualization_facts = openbsd.detect_virt_product('kern.bootfile')
    assert 'virtualization_type' in virtualization_facts
    assert 'virtualization_role' in virtualization_facts
    assert 'virtualization_tech_host' in virtualization_facts
    assert 'virtualization_tech_guest' in virtualization_facts


# Generated at 2022-06-13 04:20:52.763851
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():

    class Dummy:
        pass

    d = Dummy()
    d.module = Dummy()
    d.module.run_command = lambda x: ('', '', '')
    d.module.get_bin_path = lambda x: '/sbin/sysctl'

    sysctl_detect = VirtualSysctlDetectionMixin()
    sysctl_detect.detect_sysctl = lambda: None

    assert sysctl_detect.detect_virt_product(key='debug.virtual_guest') == {
        'virtualization_tech_guest': {},
        'virtualization_tech_host': {}
    }

# Generated at 2022-06-13 04:20:59.079289
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    class MockModule(object):
        def run_command(cmd):
            if cmd == '/bin/sysctl -n hw.model':
                out = 'QEMU Virtual CPU version 0.12.5'
            elif cmd == '/bin/sysctl -n hw.machine':
                out = 'amd64'
            return (0, out, '')
        def get_bin_path(self, arg, required=False):
            if arg == 'sysctl':
                return '/bin/sysctl'

    mixin = VirtualSysctlDetectionMixin()
    mixin.module = MockModule()
    facts = mixin.detect_virt_vendor('hw.model')
    assert facts['virtualization_type'] == 'kvm'



# Generated at 2022-06-13 04:21:10.646189
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    def sysctl_faker(self, command):
        if command == "sysctl -n kern.vm_guest":
            out = 'kvm'
        if command == "sysctl -n security.jail.jailed":
            out = '1'
        rc = 0
        return rc, out, ''
    VirtualSysctlDetectionMixin.detect_sysctl = sysctl_faker
    virtual = VirtualSysctlDetectionMixin()
    virtual_facts = virtual.detect_virt_product('kern.vm_guest')
    assert virtual_facts.get('virtualization_tech_guest') == set(['kvm'])
    virtual_facts = virtual.detect_virt_product('security.jail.jailed')
    assert virtual_facts.get('virtualization_tech_guest') == set

# Generated at 2022-06-13 04:21:19.949156
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    class BSDVirtualSysctlDetectionMixin(VirtualSysctlDetectionMixin):
        def __init__(self):
            self.sysctl_path = '/sbin/sysctl'

    vs = BSDVirtualSysctlDetectionMixin()
    facts = vs.detect_virt_product('hw.product')
    assert facts['virtualization_type'] == 'Hyper-V'
    assert facts['virtualization_role'] == 'guest'
    assert 'virtualization_tech_guest' in facts
    assert facts['virtualization_tech_guest'] == set(['Hyper-V'])
    assert 'virtualization_tech_host' in facts
    assert facts['virtualization_tech_host'] == set()

    facts = vs.detect_virt_product('security.jail.jailed')

# Generated at 2022-06-13 04:21:28.577955
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.facts.virtual.freebsd import VirtualSysctlDetectionMixin
    v = VirtualSysctlDetectionMixin()
    v.sysctl_path = 'fakepath/sysctl'
    product_facts = v.detect_virt_product('hw.model')
    assert product_facts['virtualization_type'] == 'virtualbox'
    assert product_facts['virtualization_role'] == 'guest'
    assert product_facts['virtualization_tech_host'] == set()
    assert product_facts['virtualization_tech_guest'] == {'virtualbox'}


# Generated at 2022-06-13 04:21:39.306625
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():

    class MockModule:
        def __init__(self, *args, **kwargs):
            self.facts = dict()

        def get_bin_path(self, *args, **kwargs):
            return '/sbin/sysctl -n'

        def run_command(self, *args, **kwargs):
            if 'kern.vm_guest' in args:
                return (0, 'KVM', '')
            elif 'hw.model' in args:
                return (0, '', '')

    class MockClass:
        def __init__(self, *args, **kwargs):
            self.module = MockModule()
            self.sysctl_path = MockModule.get_bin_path(self.module)

    mock_class = MockClass()
    # We don't set virtualization_role or virtual

# Generated at 2022-06-13 04:21:43.792502
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    from ansible.module_utils.facts.virtual.freebsd import VirtualSysctlDetectionMixin
    class FakeModule():
        pass
    factory = VirtualSysctlDetectionMixin()
    expected = {'virtualization_role': 'guest', 'virtualization_type': 'kvm', 'virtualization_tech_guest': set(['kvm']), 'virtualization_tech_host': set([])}
    fake_module = FakeModule()
    fake_module.run_command = lambda x: (0, 'KVM', '')
    fake_module.get_bin_path = lambda x: '/usr/sbin/sysctl'
    factory.module = fake_module
    virtual_product_facts = factory.detect_virt_product("hw.product")
    assert expected == virtual_product_facts


# Generated at 2022-06-13 04:21:53.663997
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    class FakeModule:
        def get_bin_path(self, arg):
            return 'sysctl'

        def run_command(self, arg):
            return (0, "HVM", "")

    class FakeMixin(VirtualSysctlDetectionMixin):
        def __init__(self):
            self.sysctl_path = None
            self.module = FakeModule()

    sample_output = {'virtualization_type': 'xen', 'virtualization_role': 'guest'}
    fake_mixin = FakeMixin()
    assert fake_mixin.detect_virt_product('product') == sample_output

    fake_mixin.module.run_command = lambda arg: (0, "XenPV", "")

# Generated at 2022-06-13 04:22:03.222376
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    from ansible.module_utils.facts.bsd.virtual import VirtualSysctlDetectionMixin
    from ansible.module_utils.facts.bsd.virtual import VirtualSysctlDetectionMixin_impl
    # Create an object of class VirtualSysctlDetectionMixin_impl
    virtual = VirtualSysctlDetectionMixin_impl()
    # Assign 'qemu' as the value of the parameter `key`
    key = 'qemu'
    # Call the function being tested.
    virtual_vendor = virtual.detect_virt_vendor(key)
    # Assert that the virtualization_type is 'kvm' and the virtualization_role is 'guest'
    assert virtual_vendor['virtualization_type'] == 'kvm'
    assert virtual_vendor['virtualization_role'] == 'guest'

# Generated at 2022-06-13 04:22:24.506195
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    class TestClass():
        def __init__(self, *args, **kwargs):
            self.module = AnsibleModule(argument_spec={})

        def set_fs_facts(self, facts):
            self.FS_FACTS_CACHE = facts

        def run_command(self, cmd):
            if cmd == '/sbin/sysctl -n hw.product':
                return (0, 'QEMU_VM', '')
            if cmd == '/sbin/sysctl -n hw.product':
                return (0, 'OpenBSD', '')
            return (1, '', '')

        def get_bin_path(self, bin_path):
            if bin_path == 'sysctl':
                return '/sbin/sysctl'
            return bin_path


# Generated at 2022-06-13 04:22:36.451956
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    from ansible.module_utils.facts.virtual.freebsd import VirtualSysctlDetectionMixin

    class FreeBSDMock(object):
        def __init__(self):
            self.module = self

        def get_bin_path(self, path):
            self.path = path
            if path == 'sysctl':
                return '/sbin/sysctl'
            else:
                return path

        def run_command(self, command):
            self.command = command
            if command == '/sbin/sysctl -n hw.vendor':
                return 0, 'QEMU', ''
            else:
                return 255, '', ''

    obj = FreeBSDMock()
    obj.detect_virt_vendor('hw.vendor')
    assert obj.path == 'sysctl'

# Generated at 2022-06-13 04:22:47.512430
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    class VirtualSysctlDetectionMixin_detect_virt_product_inline(VirtualSysctlDetectionMixin):
        def __init__(self):
            self.module = self
            self.sysctl_path = None
            self.sysctl_path = 'sysctl'
        def run_command(self, cmd):
            if cmd == 'sysctl -n kern.vm_guest':
                return (0, 'KVM', '')
            return (255, '', 'error')
    vsdm = VirtualSysctlDetectionMixin_detect_virt_product_inline()
    f = vsdm.detect_virt_product('kern.vm_guest')
    assert f['virtualization_type'] == 'kvm'
    assert f['virtualization_role'] == 'guest'


# Generated at 2022-06-13 04:22:53.927630
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    x = VirtualSysctlDetectionMixin()
    x.module = MockModule()
    assert x.detect_virt_product('hw.model') == \
        {'virtualization_type': 'kvm', 'virtualization_role': 'guest', 'virtualization_tech_guest': set(['kvm']), 'virtualization_tech_host': set()}


# Generated at 2022-06-13 04:23:02.900900
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    class VirtualSysctlDetectionMixinTest(VirtualSysctlDetectionMixin):
        def __init__(self):
            self.sysctl_path = None
            self.module = None
    obj = VirtualSysctlDetectionMixinTest()
    obj.detect_sysctl = lambda: None
    obj.sysctl_path = 'test_sysctl_path'
    class TestModule:
        def run_command(self, cmd):
            assert cmd == obj.sysctl_path + ' --hardware.system_product'
            results = { 'rc': 0 }
            results['stdout'] = 'KVM'
            return results['rc'], results['stdout'], results['stderr']
    obj.module = TestModule()

# Generated at 2022-06-13 04:23:08.359008
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():

    class ModuleStub(object):
        def get_bin_path(self, path):
            if path == 'sysctl':
                return '/sbin/sysctl'
            else:
                return None

        def run_command(self, path):
            if path == '/sbin/sysctl -n kern.vm_guest':
                return 0, 'QEMU', None
            elif path == '/sbin/sysctl -n kern.hostuuid':
                return 0, '0F0F0F0F-0000-0000-0000-000000000000', None
            else:
                return 1, None, None

    class VirtualSysctlDetectionMixinStub(VirtualSysctlDetectionMixin):
        module = ModuleStub()

    facts = VirtualSysctlDetectionMixinStub()

# Generated at 2022-06-13 04:23:17.928686
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():

    class TestVirtualSysctlDetectionMixin(VirtualSysctlDetectionMixin):
        def __init__(self):
            self.module = None
            self.sysctl_path = '/sbin/sysctl'

        def detect_sysctl(self):
            return

    def run_command(command):
        if command == '%s -n hw.model' % virtual_sysctl_detection_mixin.sysctl_path:
            return 0, 'Intel(R) Core(TM) i7-5557U CPU @ 3.10GHz', ''
        elif command == '%s -n hw.product' % virtual_sysctl_detection_mixin.sysctl_path:
            return 0, 'MacBookAir7,2', ''

# Generated at 2022-06-13 04:23:21.616830
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    vobj = VirtualSysctlDetectionMixin()
    vobj.module = object()
    vobj.module.get_bin_path = lambda a: 'bin/%s' % a
    vobj.module.run_command = lambda b: (0, 'QEMU', '')

    vobj.detect_virt_vendor('machdep.hypervisor_vendor')
    vobj.detect_virt_vendor('machdep.bios.vendor')

# Generated at 2022-06-13 04:23:27.899275
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    result = VirtualSysctlDetectionMixin.detect_virt_product('blah')
    assert result['virtualization_type'] == ''
    assert result['virtualization_role'] == ''
    result = VirtualSysctlDetectionMixin.detect_virt_product('security.jail.jailed')
    assert result['virtualization_type'] == 'jails'
    assert result['virtualization_role'] == 'guest'


# Generated at 2022-06-13 04:23:38.253709
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    def get_bin_path(binary, required=True):
        if binary == 'sysctl':
            return binary

    class FreeBSDVirtualSysctlDetectionMixin(VirtualSysctlDetectionMixin):
        def __init__(self, module):
            self.module = module

        def detect_sysctl(self):
            self.sysctl_path = get_bin_path('sysctl')

    f = FreeBSDVirtualSysctlDetectionMixin(module)

    class MyModule:
        def __init__(self):
            self.run_command_value = ''
            self.run_command_rc_value = 0


# Generated at 2022-06-13 04:23:58.469520
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )

    sysctl_path = module.get_bin_path('sysctl')
    if sysctl_path is None:
        raise ValueError('sysctl_path is not set.')

    detection = VirtualSysctlDetectionMixin()
    detection.module = module
    detection.sysctl_path = sysctl_path

    virtual_product_facts = detection.detect_virt_product('hw.product')
    assert 'virtualization_tech_guest' in virtual_product_facts
    assert 'virtualization_tech_host' in virtual_product_facts
    assert 'virtualization_type' in virtual_product_facts
    assert 'virtualization_role' in virtual_product_facts


# Generated at 2022-06-13 04:24:07.397704
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    try:
        reload(sysctl)
    except NameError:
        from units.compat import unittest
        import ansible.modules.system.sysctl as sysctl
    from units.compat.mock import patch
    from units.modules.utils import set_module_args, AnsibleExitJson, AnsibleFailJson, ModuleTestCase

    class TestVirtualSysctlDetectionMixin(ModuleTestCase):
        def setUp(self):
            super(TestVirtualSysctlDetectionMixin, self).setUp()
            self.version_detect_mock = patch('ansible.modules.system.sysctl.version_detect')
            self.version_detect_mock.start()

        def tearDown(self):
            self.version_detect_mock.stop()

# Generated at 2022-06-13 04:24:17.893200
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    mixin = VirtualSysctlDetectionMixin()
    mixin.sysctl_path = '/sbin/sysctl'
    mixin.module = type('FakeModule', (object,), dict(get_bin_path=lambda self, key: key,
                                                      run_command=lambda self, key: (0, 'virtualbox', '')))()
    out = mixin.detect_virt_product('hw.model')
    assert out['virtualization_type'] == 'virtualbox'
    assert out['virtualization_role'] == 'guest'
    assert out['virtualization_tech_guest'] == set(['virtualbox'])
    assert out['virtualization_tech_host'] == set()
    assert not out['virtualization_product_name']
    assert not out['virtualization_product_version']


# Generated at 2022-06-13 04:24:23.717365
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    product = VirtualSysctlDetectionMixin()
    product.detect_sysctl = lambda: '/sbin/sysctl'
    rc1 = product.detect_virt_product('hw.model')
    rc2 = product.detect_virt_product('security.jail.jailed')
    assert rc1['virtualization_role'] == 'guest'
    assert rc1['virtualization_type'] == 'virtualbox'
    assert rc2['virtualization_role'] == 'guest'
    assert rc2['virtualization_type'] == 'jails'


# Generated at 2022-06-13 04:24:36.661032
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    from ansible.utils.virtualsysctl_detection_mixin import VirtualSysctlDetectionMixin

    class MockSysctlModule(object):
        def __init__(self):
            self.virt_product_facts = {}
            self.virt_product_facts['virtualization_tech_guest'] = set()
            self.virt_product_facts['virtualization_tech_host'] = set()

        def get_bin_path(self, binary):
            return binary

        def run_command(self, command):
            if 'kern.vm_guest' in command:
                if re.match('(KVM|kvm|Bochs|SmartDC).*', command):
                    self.virt_product_facts['virtualization_tech_guest'].add('kvm')

# Generated at 2022-06-13 04:24:46.665457
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    class FakeModule(object):
        def __init__(self):
            self.sysctl_path = None
            self.run_command_result = (0, 'QEMU', None)

        def get_bin_path(self, path):
            return self.sysctl_path

        def run_command(self, cmd):
            return self.run_command_result

    test_class = VirtualSysctlDetectionMixin()
    test_class.module = FakeModule()
    test_class.sysctl_path = '/sbin/sysctl'
    test_class.detect_virt_vendor('hw.model')
    result = test_class.detect_virt_vendor('hw.model')
    assert result['virtualization_role'] == 'guest'

# Generated at 2022-06-13 04:24:56.989263
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    class FakeModule(object):
        class RunCommandResult(object):
            def __init__(self):
                self.rc = 0
                self.out = "KVM"
                self.err = ""

        def __init__(self):
            self.run_command_result = self.RunCommandResult()

        def get_bin_path(self, component):
            return 'fake_bin'

        def run_command(self, command):
            return self.run_command_result.rc, self.run_command_result.out, self.run_command_result.err

    class FakeMixin(VirtualSysctlDetectionMixin):
        def __init__(self):
            self.module = FakeModule()

        def detect_sysctl(self):
            pass

    sysctl_mixin = FakeMixin()
    res

# Generated at 2022-06-13 04:25:04.386972
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    from ansible.module_utils.facts.collector.virtual import VirtualSysctlDetectionMixin

    virtual_vendor_facts = dict(virtualization_type=None,
                                virtualization_role=None,
                                virtualization_tech_host=set(),
                                virtualization_tech_guest=set())
    mocked_class_obj = VirtualSysctlDetectionMixin()
    mocked_class_obj.module = MagicMock()
    mocked_class_obj.module.run_command.return_value = (0, 'QEMU', '')
    mocked_class_obj.module.get_bin_path.return_value = True
    result = mocked_class_obj.detect_virt_vendor('machdep.hypervisor_vendor')
    assert result == virtual_vendor_facts

# Generated at 2022-06-13 04:25:15.489110
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():

    class FakeModule:
        def __init__(self):
            self.run_command_results = []

        def run_command(self, command):
            results = self.run_command_results.pop(0)
            return [results['rc'], results['out'], results['err']]

    class FakeSys():
        def __init__(self):
            self.sysctl_path = '/sbin/sysctl'

    module = FakeModule()
    sys = FakeSys()

    mixin = VirtualSysctlDetectionMixin()
    mixin.sysctl_path = sys.sysctl_path
    mixin.module = module

    # Test 1
    # Setup the FakeModule
    module.run_command_results.append({'rc': 0, 'out': "QEMU", 'err': ''})

# Generated at 2022-06-13 04:25:20.122862
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    class FakeModule:
        class FakeClass(VirtualSysctlDetectionMixin):
            def __init__(self):
                self.module = FakeModule()
                self.sysctl_path = '/sbin/sysctl'
                self.module.get_bin_path = lambda x: self.sysctl_path
                self.module.run_command = lambda x: (0, 'VirtualBox', '')

        cls = FakeClass()
        cls.detect_virt_product("machdep.virtual_guest")
        assert cls.virtualization_type == 'virtualbox'
        assert cls.virtualization_role == 'guest'
        assert 'xen' not in cls.virtualization_tech_guest
        assert 'xen' not in cls.virtualization_tech_host
        assert 'virtualbox'

# Generated at 2022-06-13 04:25:51.349488
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    class FakeModule(object):

        def __init__(self):

            self.run_command_results = [
                [0, "QEMU", ""],
                [0, "OpenBSD", ""],
                [0, "Something Else", ""]
            ]
            self.run_command_calls = []

        def get_bin_path(self, executable):
            return executable

        def run_command(self, cmd):
            self.run_command_calls.append(cmd)
            return self.run_command_results.pop(0)

    module = FakeModule()
    sysctl = VirtualSysctlDetectionMixin()
    sysctl.module = module

    # First call to sysctl
    virtual_vendor_facts = sysctl.detect_virt_vendor('hw.vendor')

    # Second

# Generated at 2022-06-13 04:26:00.438845
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    module = openbsd_virtual_vendor()
    module.sysctl_path = '/sbin/sysctl'

    module.run_command = MagicMock(return_value=(0, 'QEMU', ''))
    virtual_vendor_facts = module.detect_virt_vendor('vm.vm_guest')
    assert virtual_vendor_facts['virtualization_type'] == 'kvm'
    assert virtual_vendor_facts['virtualization_role'] == 'guest'

    module.run_command = MagicMock(return_value=(0, 'OpenBSD', ''))
    virtual_vendor_facts = module.detect_virt_vendor('vm.vm_guest')
    assert virtual_vendor_facts['virtualization_type'] == 'vmm'

# Generated at 2022-06-13 04:26:07.016892
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    import sysctl
    sysctl_obj = sysctl.Sysctl()
    sysctl_obj.sysctl_path = '/my/sysctl/path'
    sysctl_obj.module = MockModule()
    expected_facts = {
        'virtualization_type': 'kvm',
        'virtualization_role': 'guest',
        'virtualization_tech_host': set(),
        'virtualization_tech_guest': {'kvm'}
    }
    virt_product_facts = sysctl_obj.detect_virt_product('hw.model')
    assert virt_product_facts == expected_facts


# Generated at 2022-06-13 04:26:11.985056
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    virtual_sysctl_mixin = VirtualSysctlDetectionMixin()
    virtual_sysctl_mixin.module = FakeAnsibleModule()
    virtual_sysctl_mixin.detect_sysctl = lambda: None
    virtual_sysctl_mixin.sysctl_path = '/usr/bin/sysctl'
    virtual_sysctl_mixin.run_command = lambda command: (0, 'QEMU', '')
    virtual_vendor_facts = virtual_sysctl_mixin.detect_virt_vendor('machdep.hypervisor_vendor')
    assert virtual_vendor_facts['virtualization_type'] == 'kvm'
    assert virtual_vendor_facts['virtualization_role'] == 'guest'


# Generated at 2022-06-13 04:26:19.142081
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    class Module(object):
        def get_bin_path(self, path, default=None):
            if path == 'sysctl':
                return '/sbin/sysctl'
            else:
                return default

        def run_command(self, command):
            if command == '/sbin/sysctl -n hw.product':
                return 0, 'OpenBSD', None
            elif command == '/sbin/sysctl -n hw.vendor':
                return 0, 'QEMU', None
            elif command == '/sbin/sysctl -n security.jail.jailed':
                return 0, '1', None
            elif command == '/sbin/sysctl -n security.jail.hostname':
                return 0, 'hostname.jail.org', None

# Generated at 2022-06-13 04:26:25.784529
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    class VirtualSysctlDetectionMixinImpl(VirtualSysctlDetectionMixin):
        def __init__(self, sysctl_path, sysctl_key, sysctl_val):
            self.sysctl_path = sysctl_path
            self.sysctl_key = sysctl_key
            self.sysctl_val = sysctl_val
        def detect_sysctl(self):
            pass
        def module_run_command(self, cmd):
            return 0, self.sysctl_val, ''


# Generated at 2022-06-13 04:26:36.246700
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    import os
    from ansible.module_utils.facts import MythicFactsModule, VirtualSysctlDetectionMixin

    class VirtualSysctlDetectionMixin_System(MythicFactsModule, VirtualSysctlDetectionMixin):
        def __init__(self, *args, **kwargs):
            super(VirtualSysctlDetectionMixin_System, self).__init__(*args, **kwargs)

    # Construct class for testing
    MOCK_VARS = {}
    test_obj = VirtualSysctlDetectionMixin_System(MOCK_VARS)
    test_obj.detect_sysctl = lambda: setattr(test_obj, 'sysctl_path', '/usr/sbin')

# Generated at 2022-06-13 04:26:45.499160
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    from ansible.module_utils.facts.system.darwin import VirtualSysctlDetectionMixin
    class TestClass:
        def __init__(self):
            self.sysctl_path = '/usr/sbin/sysctl'
            self.module = self
            self.run_command_called = False
            self.command_rc = 0
            self.command_out = 'KVM'
            self.command_err = ''
            self.run_command_calls = []

        def run_command(self, cmd):
            self.run_command_called = True
            self.run_command_calls.append(cmd)
            return (self.command_rc, self.command_out, self.command_err)

        def get_bin_path(self, name):
            return self.sysctl_path

       

# Generated at 2022-06-13 04:26:57.077725
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    # We will pretend to provide the output of the sysctl command
    class MyModule:
        def __init__(self, *args, **kwargs):
            self.params = kwargs.get('params', {})
        def get_bin_path(self, *args, **kwargs):
            return '/usr/bin/sysctl'
        def run_command(self, cmd):
            return (0, 'QEMU Virtual CPU', '')
    class MyVirtDetect:
        def __init__(self, *args, **kwargs):
            self.module = MyModule(params=kwargs.get('params'))
        def detect_sysctl(self):
            return None
        def detect_virt_product(self, *args, **kwargs):
            return None
    my_virt = MyVirtDetect()
   

# Generated at 2022-06-13 04:27:08.786914
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    class VirtualSysctlDetectionMixin_test_case:
        sysctl_path = None
        def get_bin_path(self, name):
            return name
        def run_command(self, cmd):
            if cmd == 'sysctl -n kern.hostuuid':
                return 0, '0b8430c5-ac0c-4c67-9276-3a3baa1d42e4', ''
            elif cmd == 'sysctl -n security.jail.jailed':
                return 0, '0', ''
            elif cmd == 'sysctl -n hw.product':
                return 0, 'VMware7,1', ''
            elif cmd == 'sysctl -n hw.machine_arch':
                return 0, 'amd64', ''

    detect = VirtualSysctlDetectionMixin

# Generated at 2022-06-13 04:27:52.455200
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    test_obj = VirtualSysctlDetectionMixin()
    test_obj.module = FakeAnsibleModule()
    test_obj.detect_sysctl = FakeDetectSysctl()
    test_obj.module.run_command = FakeRunCommand(('OpenBSD', '', ''))
    results = test_obj.detect_virt_vendor('security.jail.jailed')
    assert results == {'virtualization_tech_guest': set(['vmm']),
                       'virtualization_role': 'guest', 'virtualization_type': 'vmm',
                       'virtualization_tech_host': set([])}

# Helper functions

# Generated at 2022-06-13 04:27:56.129233
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():

    result = VirtualSysctlDetectionMixin().detect_virt_vendor(key='hw.model')

    assert result['virtualization_tech_guest'] == set(['kvm', 'vmm'])
    assert result['virtualization_tech_host'] == set()

# Generated at 2022-06-13 04:28:03.780865
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    class ModuleMock(object):
        def get_bin_path(self, name):
            if name == "sysctl":
                return "/bin/sysctl"
            return None
        def run_command(self, cmd):
            out = ""
            if cmd == "/bin/sysctl -n hw.product":
                out = "OpenBSD"
            if cmd == "/bin/sysctl -n hw.machine":
                out = "OpenBSD"
            if cmd == "/bin/sysctl -n hw.vendor":
                out = "OpenBSD"
            return 0, out, ""
    class BSDFamily(VirtualSysctlDetectionMixin):
        def __init__(self):
            self.module = ModuleMock()
    bsdFamily = BSDFamily()
    assert bsdFamily.detect_virt_

# Generated at 2022-06-13 04:28:14.696409
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    class obj(object):
        def __init__(self, rc, out, err):
            self.rc = rc
            self.out = out
            self.err = err
        def run_command(self, cmd):
            return self.rc, self.out, self.err

    class TestClass(VirtualSysctlDetectionMixin):
        def __init__(self):
            self.sysctl_path = None

        def detect_sysctl(self):
            self.sysctl_path = '/sbin/sysctl'

    # No virtualization
    testobj = TestClass()
    testobj.module = obj(0, 'Generic', None)
    result = testobj.detect_virt_product('hw.product')

# Generated at 2022-06-13 04:28:25.265129
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    import sys

    if sys.version_info[0] < 3:
        import __builtin__ as builtins
    else:
        import builtins

    class Module(object):
        def __init__(self, params):
            self.params = params
            self.version_info = sys.version_info

        def set_module_args(self, args):
            self.params = args

        def run_command(self, cmd):
            class RC(object):
                def __init__(self, rc, stdout, stderr):
                    self.rc = rc
                    self.stdout = stdout
                    self.stderr = stderr
            return RC(0, 'KVM', None)

        def get_bin_path(self, arg):
            return '/sbin/sysctl'


# Generated at 2022-06-13 04:28:29.507933
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():

    # Set up mock objects
    module_mock = MagicMock()
    module_mock.get_bin_path.return_value = '/sbin/sysctl'
    module_mock.run_command.return_value = (0, 'OpenBSD', None)

    # Set up class instance
    mixin = VirtualSysctlDetectionMixin()
    mixin.module = module_mock

    # Assert that detect_virt_vendor returns expected data
    assert mixin.detect_virt_vendor('vm.product') == {
        'virtualization_role': 'guest',
        'virtualization_type': 'vmm',
        'virtualization_tech_host': set(),
        'virtualization_tech_guest': {'vmm'},
    }

# Generated at 2022-06-13 04:28:37.551927
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    import sys
    sys.modules['ansible.module_utils.facts'] = sys.modules['ansible.module_utils.facts.freebsd.virtual']

    from ansible.module_utils.facts.virtual import VirtualSysctlDetectionMixin
    from ansible.module_utils.facts.freebsd.virtual import VirtualFacts
    from ansible.module_utils.facts.freebsd.virtual import test_module
    new_VirtualFacts = type('new_VirtualFacts', (VirtualSysctlDetectionMixin, VirtualFacts), dict())
    new_module = test_module()
    new_virtual_facts = new_VirtualFacts(module=new_module)

    # Test kvm

# Generated at 2022-06-13 04:28:45.528767
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    class ModuleMock(object):
        def __init__(self):
            self.name = 'FreeBSD'
            self.name = 'OpenBSD'
            self.name = 'Solaris'
            self.name = 'Linux'
    
    class RunCommandMock(object):
        def __init__(self):
            self.rc = 0
            self.out = 'Linux'
            self.err = ''

        def run_command(self, cmd):
            return self.rc, self.out, self.err
    
    class VirtualSysctlDetectionMixinMock(VirtualSysctlDetectionMixin):
        def __init__(self):
            self.module = ModuleMock()
            self.sysctl_path = '/usr/sbin/sysctl'
            self.run_command = RunCommandMock().run

# Generated at 2022-06-13 04:28:56.022335
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    from ansible.modules.system.freebsd import virtual_sysctl_detection_mixin
    v_d = virtual_sysctl_detection_mixin.VirtualSysctlDetectionMixin()
    v_d.module = FakeModule()
    v_d.sysctl_path = '/sbin/sysctl'
    # vmm
    v_d.module.run_command.side_effect=[(0,'OpenBSD','')]
    d_v_v = v_d.detect_virt_vendor('hw.model')
    assert d_v_v['virtualization_type'] == 'vmm'
    assert d_v_v['virtualization_role'] == 'guest'
    # kvm
    v_d.module.run_command.side_effect=[(0,'QEMU','')]


# Generated at 2022-06-13 04:29:05.796744
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    #The class VirtualSysctlDetectionMixin is a mixin class, this is a hack to support unittesting
    class DummyVirtualSysctlDetectionMixin(VirtualSysctlDetectionMixin):
        def __init__(self):
            self.sysctl_path= '/usr/sbin/sysctl'
            self.module = DummyAnsibleModule()

    import sys
    if sys.version_info < (2, 7):
        import unittest2 as unittest
    else:
        import unittest

    class DummyAnsibleModule(object):
        def run_command(self, cmd):
            return (0, 'QEMU', '')

    class TestFacts(unittest.TestCase):
        def setUp(self):
            self.mixin = DummyVirtualSysctlDetectionMix