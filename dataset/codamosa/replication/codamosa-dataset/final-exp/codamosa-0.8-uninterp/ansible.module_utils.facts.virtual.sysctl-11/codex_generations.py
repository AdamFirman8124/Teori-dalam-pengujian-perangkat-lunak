

# Generated at 2022-06-13 04:20:43.657398
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    class FakeModule:
        def get_bin_path(self, name):
            return '/usr/bin/{}'.format(name)

        def run_command(self, command):
            if 'sysctl' not in command:
                return 0, '', ''

            if 'security.jail.jailed' in command:
                return 0, '1', ''

            return 0, 'KVM', ''

    class FakeSysctlDetectionMixin:
        def __init__(self):
            self.module = FakeModule()

        def detect_sysctl(self):
            pass

    detection_mixin = FakeSysctlDetectionMixin()


# Generated at 2022-06-13 04:20:52.835967
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    from ansible.module_utils.facts.system.bsd import VirtualSysctlDetectionMixin
    import sys

    class FakeModule(object):
        def __init__(self):
            self.run_command_line = ''
            self.run_command_rc = 0
            self.run_command_stdout = 'QEMU Virtual CPU version 1.0.2'
            self.run_command_stderr = ''

        def get_bin_path(self, binary):
            return '/usr/local/bin/' + binary

        def run_command(self, args):
            self.run_command_line = args
            if self.run_command_rc == 0:
                return self.run_command_rc, self.run_command_stdout, self.run_command_stderr

# Generated at 2022-06-13 04:20:58.496782
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    test_object = VirtualSysctlDetectionMixin()
    test_object.module = MockModule()

    test_object.module.run_command = Mock()
    test_object.module.run_command.return_value = (0, '', '')

    test_object.sysctl_path = '/usr/sbin/sysctl'

    expected_return = {'virtualization_role': 'guest',
                       'virtualization_type': 'kvm',
                       'virtualization_tech_host': set(),
                       'virtualization_tech_guest': set(['kvm'])}
    assert test_object.detect_virt_product('') == expected_return



# Generated at 2022-06-13 04:21:10.615790
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    mock = VirtualSysctlDetectionMixin()
    mock.detect_sysctl = lambda: None
    mock.module = MagicMock()
    mock.module.get_bin_path = lambda x: None
    mock.module.run_command = MagicMock(return_value=(0, '', ''))
    out = mock.detect_virt_product('machdep.dmi.system-product')
    assert out['virtualization_type'] == 'unknown'
    assert out['virtualization_role'] == 'unknown'
    assert len(out['virtualization_tech_guest']) == 0
    assert len(out['virtualization_tech_host']) == 0

    out = mock.detect_virt_product('machdep.dmi.system-product')
    assert out['virtualization_type'] == 'unknown'

# Generated at 2022-06-13 04:21:19.950088
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    class FakeVendorModule(object):
        class FakeVendor(object):
            def __init__(self):
                self.sysctl_path = 'sysctl'
            def detect_sysctl(self):
                return True

            def detect_virt_vendor(self, key):
                return self.FakeVendorModule().detect_virt_vendor(key)

        def detect_virt_vendor(self, key):
            fact_dict = {}
            rc, out, err = self.run_command("%s -n %s" % (self.sysctl_path, key))
            if rc == 0:
                if out.rstrip() == 'QEMU':
                    fact_dict['virtualization_type'] = 'kvm'
                    fact_dict['virtualization_role'] = 'guest'

# Generated at 2022-06-13 04:21:29.820005
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    # Testing for virtualization_type detection for jails
    VirtualSysctlDetectionMixin_jails = VirtualSysctlDetectionMixin()
    VirtualSysctlDetectionMixin_jails.module = MockModule()
    VirtualSysctlDetectionMixin_jails.module.run_command = Mock(return_value=(0, '1', None))
    VirtualSysctlDetectionMixin_jails.sysctl_path = '/usr/sbin/sysctl'
    VirtualSysctlDetectionMixin_jails.detect_sysctl = Mock()
    VirtualSysctlDetectionMixin_jails.detect_sysctl.return_value = '/usr/sbin/sysctl'
    key = 'security.jail.jailed'


# Generated at 2022-06-13 04:21:36.002223
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    class mock_module(object):
        def get_bin_path(self, program_path, required=True, opt_dirs=None):
            return "/sbin/sysctl"

        def run_command(self, cmd):
            return 0, "OpenBSD", ""

    v = VirtualSysctlDetectionMixin()
    v.module = mock_module()
    v.detect_virt_vendor("hw.product")


# Generated at 2022-06-13 04:21:47.799073
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    class MockModule:
        def __init__(self):
            self.bin_path_cache = {}
            self.params = {}

        def get_bin_path(self, name, required=False):
            if name in ['sysctl']:
                return 'mock_sysctl_path'
            raise Exception('non-existent binary in get_bin_path: %s' % name)

        def run_command(self, cmd):
            if cmd == 'mock_sysctl_path -n hw.simd.ext':
                return 0, 'SSE2', ''
            elif cmd == 'mock_sysctl_path -n security.jail.jailed':
                return 0, '1', ''

# Generated at 2022-06-13 04:21:55.659322
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    # We create a object class with a fake command
    # return code of sysctl command is 0 fake_out and fake_err is the output of the command
    class TestObject(VirtualSysctlDetectionMixin):
        def __init__(self):
            self.sysctl_path = None

        def detect_sysctl(self):
            self.sysctl_path = '/dummy/sysctl'

        def run_command(self, command):
            fake_out = '''
hw.product: BHYVE
hw.machine: amd64
'''
            return 0, fake_out, ''

    test_obj = TestObject()
    # when we call detect_virt_product method
    # the output of the method must be:
    #        {
    #            'virtualization_type': 'bhyve',
    #            'virtual

# Generated at 2022-06-13 04:22:04.085962
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    import ansible.module_utils.basic

    class TestModule(object):
        def __init__(self):
            self.params = {}
            self.run_command_calls = []
            self.run_command_results = []
            self.exit_json_calls = []
            self.exit_json_results = []

        def get_bin_path(self, executable):
            return executable

        def run_command(self, command):
            self.run_command_calls.append(command)
            return self.run_command_results.pop(0)

        def exit_json(self, results):
            self.exit_json_calls.append(results)

    # Fake freebsd.freenas.FreeNasModule is used to mock the actual module

# Generated at 2022-06-13 04:22:24.635637
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    class TestModule:
        def __init__(self):
            self.run_command_lines = []

        def get_bin_path(self, path):
            if path != 'sysctl':
                return None
            return '/sbin/sysctl'

        def run_command(self, cmd):
            self.run_command_lines.append(cmd)
            if cmd == '/sbin/sysctl -n kern.smp.cpus':
                return 0, '2', ''
            if cmd == '/sbin/sysctl -n kern.smp.active':
                return 0, '1', ''
            if cmd == '/sbin/sysctl -n hw.model':
                return 0, 'VirtualBox', ''
            if cmd == '/sbin/sysctl -n security.jail.jailed':
                return

# Generated at 2022-06-13 04:22:36.831900
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    class FakeModule(object):
        def get_bin_path(self, modname):
            return "path_to_sysctl"
        def run_command(self, cmd):
            if cmd == "path_to_sysctl -n hw.model":
                return 0, "KVM/CPU", ""
            if cmd == "path_to_sysctl -n hw.machine_arch":
                return 0, "amd64", ""
            if cmd == "path_to_sysctl -n security.jail.jailed":
                return 0, "1", ""
    fake_module = FakeModule()
    virtual_sysctl_detection_mixin = VirtualSysctlDetectionMixin()
    fake_mixin = virtual_sysctl_detection_mixin
    fake_mixin.module = fake_module
    virtual_

# Generated at 2022-06-13 04:22:47.849271
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    # Test when sysctl is not accessible
    module = AnsibleModule(argument_spec={
        'virtual_vendor': {'required': True},
    })
    module.exit_json = mock.Mock()
    module.run_command = mock.Mock()
    module.run_command.return_value = (127, "", "")
    module.get_bin_path = mock.Mock()
    module.get_bin_path.return_value = "/usr/bin/sysctl"
    virtual_sysctl_detection_mixin = VirtualSysctlDetectionMixin()
    virtual_sysctl_detection_mixin.module = module
    virtual_sysctl_detection_mixin.detect_virt_vendor("security.jail.jailed")
    assert False == module.exit_json.called



# Generated at 2022-06-13 04:22:59.252981
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    sysctl_path = '%{system_path}/sysctl'

    # Guest on QEMU
    module = FakeModule([sysctl_path], 'openbsd')

    virtual_vendor_facts = VirtualSysctlDetectionMixin().detect_virt_vendor('machdep.cpu_vendor')
    assert virtual_vendor_facts['virtualization_type'] == 'kvm'
    assert virtual_vendor_facts['virtualization_tech_host'] == set()
    assert virtual_vendor_facts['virtualization_tech_guest'] == set(['kvm'])
    assert virtual_vendor_facts['virtualization_role'] == 'guest'

    # Guest on OpenBSD
    module = FakeModule([sysctl_path], 'openbsd')

    virtual_vendor_facts = VirtualSysctlDet

# Generated at 2022-06-13 04:23:06.110035
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():

    class MockModule(object):
        class MockRunCommand(object):
            pass

        def __init__(self):
            self.run_command = MockRunCommand()
            self.run_command.return_value = (0, 'kvm', '')

        def get_bin_path(self, name):
            return '/sbin/sysctl'

    class MockClass(VirtualSysctlDetectionMixin):
        def __init__(self):
            self.module = MockModule()

    obj = MockClass()
    actual = obj.detect_virt_product('hw.model')

# Generated at 2022-06-13 04:23:16.449983
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    class VirtualSysctlDetectionMixinTest:
        def __init__(self):
            self.sysctl_path = '/usr/bin/sysctl'
            self.run_command_side_effect = {
                "/usr/bin/sysctl -n hw.model": (0, "amd64 QEMU", ''),
                "/usr/bin/sysctl -n hw.machine": (0, "OpenBSD", ''),
                "/usr/bin/sysctl -n hw.machine_arch": (0, "amd64", ''),
            }
            self.sysctl_path = '/usr/bin/sysctl'

        def run_command(self, cmd):
            return self.run_command_side_effect[cmd]

    a = VirtualSysctlDetectionMixinTest()
    b = VirtualSysctlDetectionMix

# Generated at 2022-06-13 04:23:21.068184
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    vmf = VirtualSysctlDetectionMixin()
    vmf.module = FakeModule()
    vmf.sysctl_path = 'foo/sysctl'
    vmf.module.run_command = fake_run_command

    # No product detected
    rc, out, err = vmf.module.run_command("%s -n %s" % (vmf.sysctl_path, 'hw.product'))
    dvp_facts = vmf.detect_virt_product('hw.product')

    assert dvp_facts['virtualization_type'] is None
    assert dvp_facts['virtualization_role'] is None
    assert dvp_facts['virtualization_tech_guest'] == set()
    assert dvp_facts['virtualization_tech_host'] == set()


# Generated at 2022-06-13 04:23:32.601155
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    class MyClass:
        def run_command(self, command):
            return (0, 'QEMU', '')

    class MyClass1:
        def run_command(self, command):
            return (0, 'OpenBSD', '')

    class MyClass2:
        def run_command(self, command):
            return (0, '', '')

    class MyClass3:
        def run_command(self, command):
            return (1, '', '')

    module = MyClass()
    module1 = MyClass1()
    module2 = MyClass2()
    module3 = MyClass3()
    sysctl_key = 'hw.vmm.vm_guest'
    mixin = VirtualSysctlDetectionMixin()
    mixin.module = module
    assert mixin.detect_virt_

# Generated at 2022-06-13 04:23:41.877148
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    import ansible.module_utils.facts.system.openbsd as openbsd
    import sys
    import unittest

    class MockModule(object):
        params = dict()
        def __init__(self, **kwargs):
            self.params = dict(**kwargs)

        def get_bin_path(self, path, *args, **kwargs):
            return '/sbin/sysctl'

        def run_command(self, path):
            # If a test needs to closely simulate the output of sysctl,
            # it can set params['mock_sysctl_output'] with the output to use.
            # Otherwise, a return code of 0 will be used.
            rc = 1
            if 'mock_sysctl_output' in self.params:
                rc = 0

# Generated at 2022-06-13 04:23:49.531661
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    from ansible.module_utils.facts.os import VirtualSysctlDetectionMixin
    from ansible.module_utils.facts.os.freebsd import VirtualSysctlDetectionMixin
    from ansible.module_utils.facts.os.openbsd import VirtualSysctlDetectionMixin
    from ansible.module_utils.facts.os.netbsd import VirtualSysctlDetectionMixin
    m = type('module', (), {})()
    c = VirtualSysctlDetectionMixin()
    c.module = m
    # m.run_command returns a tuple with three values, like a function would
    m.run_command = lambda x: (0, 'KVM', '')
    assert 'kvm' in c.detect_virt_product('hw.model')['virtualization_tech_guest']

# Generated at 2022-06-13 04:24:20.008268
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    result = {}
    # Test case 1: sysctl_path is None
    test_case1 = VirtualSysctlDetectionMixin()
    test_case1.module = MockLinux()
    test_case1.module.run_command.return_value = (0, 'QEMU', '')
    test_case1.detect_sysctl = Mock(return_value = None)
    result = test_case1.detect_virt_vendor("")
    assert result['virtualization_role'] == 'guest'
    assert result['virtualization_type'] == 'kvm'
    assert result['virtualization_tech_host'] == set()
    assert result['virtualization_tech_guest'] == set(['kvm'])
    # Test case 2: rc(run_command()) != 0
    test_case2 = Virtual

# Generated at 2022-06-13 04:24:27.072678
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    class Module():
        def run_command(self, command):
            if command == 'sysctl -n hw.model':
                return 0, 'VirtualBox', ''
            if command == 'sysctl -n hw.product':
                return 0, 'VirtualBox', ''
            if command == 'sysctl -n security.jail.jailed':
                return 0, '1', ''
            return -1, '', "Command failed"

        def get_bin_path(self, bin_name):
            if bin_name == 'sysctl':
                return 'sysctl'

    class MockSysctlDetectionMixin(VirtualSysctlDetectionMixin):
        def __init__(self, module):
            self.module = module

    module = Module()
    sysctl = MockSysctlDetectionMixin(module)
    sysctl

# Generated at 2022-06-13 04:24:39.357713
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():

    test_class = VirtualSysctlDetectionMixin()

    """
        Case1: Detect vendor using sysctl command.
    """
    test_class.sysctl_path = '/usr/sbin/sysctl'

    test_class.module = MockAnsibleModule()
    test_class.module.run_command = MockRunCommand(True, 0, "OpenBSD")
    result = test_class.detect_virt_vendor('kern.vm_guest')
    assert result.get('virtualization_type') == 'vmm'
    assert result.get('virtualization_role') == 'guest'
    assert result.get('virtualization_tech_host') == set()
    assert result.get('virtualization_tech_guest') == set(['vmm'])


# Generated at 2022-06-13 04:24:48.450679
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    class TestVirtualSysctlDetectionMixin():
        def __init__(self):
            self.module = TestModule()

    import os

    class TestModule():
        def __init__(self):
            self.run_command_lines = []

        def get_bin_path(self, arg, opt_dirs=[]):
            return '/bin/%s' % arg

        def run_command(self, cmd):
            self.run_command_lines.append(cmd)

            if cmd.startswith('/bin/sysctl'):
                if cmd == '/bin/sysctl -n security.jail.jailed':
                    return 0, '1', ''
                else:
                    return 0, '', ''

    module = TestModule()
    vsdm = VirtualSysctlDetectionMixin()

# Generated at 2022-06-13 04:24:58.810332
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():

    from ansible.module_utils.facts.system.virtual import VirtualSysctlDetectionMixin
    from ansible.module_utils import basic
    import ansible.module_utils.facts.system.virtual

    class MockModule(object):
        def __init__(self):
            self.params = {}
            self.params['gather_subset'] = ['!all', 'virtual']
            self.params['gather_timeout'] = 5

        def get_bin_path(self, arg):
            return '/sbin/sysctl'

        def run_command(self, arg):
            if arg == 'sysctl -n hw.model':
                return 0, 'VirtualBox', ''
            if arg == 'sysctl -n security.jail.jailed':
                return 0, '1', ''

# Generated at 2022-06-13 04:25:09.683080
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    testobj = VirtualSysctlDetectionMixin()
    testobj.module = AnsibleModule(argument_spec=dict())
    testobj.sysctl_path = '/usr/sbin/sysctl'
    testobj.module.run_command = MagicMock(return_value=(1, '', ''))

    # Test with non-root user
    facts = testobj.detect_virt_product('security.jail.jailed')
    assert not facts['virtualization_role']

    testobj.module.run_command = MagicMock(return_value=(0, 'KVM-84.70', ''))

    # Test kvm
    facts = testobj.detect_virt_product('hw.model')
    assert facts['virtualization_tech_host'] == set()

# Generated at 2022-06-13 04:25:21.412456
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    # Create a mock class with modules.command module
    class MockModule(object):
        def __init__(self):
            self.command_calls = []

        def get_bin_path(self, path):
            return "/bin/sysctl"

        def run_command(self, command):
            self.command_calls.append(command)
            return 0, 'OpenBSD', ''

    # Create a mock class with the necessary functions from a platform class
    class MockFactClass(object):
        def __init__(self):
            self.module = MockModule()

    # Create a instance of the mixin
    mixin = VirtualSysctlDetectionMixin()

    # Create an instance of the platform class
    mock_fact_class = MockFactClass()

    # Make sure we return None when the command fails
    mock_fact_

# Generated at 2022-06-13 04:25:32.449080
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    class Obj(VirtualSysctlDetectionMixin):
        def __init__(self):
            self.sysctl_path = None
            self.module = None
    o = Obj()

    o.sysctl_path = 'foo'
    o.module = class_mock()
    o.module.run_command.return_value = (0, 'foo', '')
    virtual_key = 'machdep.cpu.brand_string'
    assert o.detect_virt_product(virtual_key) == {}

    o.module.run_command.return_value = (0, 'KVM', 'bar')
    assert o.detect_virt_product(virtual_key) == {'virtualization_type': 'kvm', 'virtualization_role': 'guest'}

    o.module.run_command.return_

# Generated at 2022-06-13 04:25:36.693604
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    virtual_product_facts = dict(detect_virt_product(key='kern.vm_guest'))
    assert 'virtualization_type' in virtual_product_facts
    assert 'virtualization_role' in virtual_product_facts 
    assert 'virtualization_tech_guest' in virtual_product_facts
    assert 'virtualization_tech_host' in virtual_product_facts


# Generated at 2022-06-13 04:25:48.312759
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    mockOpenBSDModule = AnsibleModule(argument_spec=dict(
        name = dict(required=True)
    ))
    mockOpenBSDModule.run_command = run_command_mock_for_class_VirtualSysctlDetectionMixin(
        [0, '', ''],
        [0, 'QEMU', ''],
        [0, 'OpenBSD', ''],
        [1, '', 'Error: Unknown key'],
        [0, '', '']
    )

    virtual_guest_facts = VirtualSysctlDetectionMixin()
    # Run method detect_virt_vendor with mock object of AnsibleModule
    virtual_guest_facts.module = mockOpenBSDModule
    virtual_guest_facts.get_file_content = get_file_content_mock_for_class_VirtualSysctlDet

# Generated at 2022-06-13 04:26:39.418765
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    test_module = FakeModule()
    test_vmm = VirtualSysctlDetectionMixin()

    # test if detect_virt_product properly detects product list
    test_vmm.sysctl_path = "/usr/sbin/sysctl"
    test_vmm.module = test_module
    test_module.run_command.return_value = (0, 'KVM', '')
    vmm_facts = test_vmm.detect_virt_product('hw.model')
    assert 'kvm' in vmm_facts['virtualization_tech_guest']
    assert vmm_facts['virtualization_role'] == 'guest'

    # test if detect_virt_product properly detects product list
    test_vmm.sysctl_path = "/usr/sbin/sysctl"

# Generated at 2022-06-13 04:26:45.761293
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    mock_module = MagicMock()
    mock_module.run_command.return_value = (0,"QEMU",None)
    virtual_sysctl = VirtualSysctlDetectionMixin()
    virtual_sysctl.module = mock_module
    virtual_vendor_facts = virtual_sysctl.detect_virt_vendor("machdep.hypervisor_vendor")
    assert virtual_vendor_facts['virtualization_type'] == 'kvm'
    assert virtual_vendor_facts['virtualization_role'] == 'guest'


# Generated at 2022-06-13 04:26:50.418811
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    class FakeModule(object):
        def get_bin_path(self, _):
            return '/sbin/sysctl'

        def run_command(self, _):
            return (0, 'QEMU', '')

    class FakeFacts(object):
        def __init__(self):
            self.module = FakeModule()

    fake_facts = FakeFacts()
    virtual_vendor_facts = VirtualSysctlDetectionMixin()
    virtual_vendor_facts.detect_virt_vendor('machdep.cpu.vendor')

    assert 'kvm' in virtual_vendor_facts.virtualization_type
    assert 'guest' in virtual_vendor_facts.virtualization_role

# Generated at 2022-06-13 04:26:58.401974
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    sysctl_path = '/sbin/sysctl'
    response = [0, 'QEMU', None]
    mod = MockOSModule()
    mod.run_command = MagicMock(return_value=response)
    v = VirtualSysctlDetectionMixin()
    v.detect_sysctl = MagicMock()
    virtual_vendor_facts = v.detect_virt_vendor('machdep.hypervisor_vendor')
    assert virtual_vendor_facts == {'virtualization_type': 'kvm',
                                    'virtualization_role': 'guest',
                                    'virtualization_tech_guest': {'kvm'},
                                    'virtualization_tech_host': set()}


# Generated at 2022-06-13 04:27:07.365545
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    # Setup
    vm_class = sysctl_detection.VirtualSysctlDetectionMixin()
    vm_class.module = MagicMock()
    vm_class.module.get_bin_path.return_value = 'sysctl'
    vm_class.module.run_command.return_value = (0, 'QEMU', '')

    # Execute
    result = vm_class.detect_virt_vendor('kern.vm_guest')

    # Test assertions
    assert result['virtualization_type'] == 'kvm'
    assert result['virtualization_role'] == 'guest'

# Generated at 2022-06-13 04:27:17.314300
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    class FakeModule(object):
        def __init__(self):
            self.params={}
            self.params['path'] = {'sysctl': '/sbin/sysctl'}

        def get_bin_path(self, key):
            return self.params['path'][key]

        def run_command(self, cmd):
            if cmd == '/sbin/sysctl -n kern.vm_guest':
                return 0, 'QEMU', ''
            if cmd == '/sbin/sysctl -n kern.vm_guest':
                return 0, 'OpenBSD', ''
            return -1, '', ''

    module = FakeModule()
    obj = VirtualSysctlDetectionMixin()
    obj.module = module

# Generated at 2022-06-13 04:27:26.427574
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    from ansible.module_utils.facts import virtual

    # We create a new class, because we don't want to mess with the original class
    # The test functions should be non-destructive
    class VirtualSysctlDetectionMixinTester():
        def detect_sysctl(self):
            self.sysctl_path = '/usr/sbin/sysctl'

        def run_command(self, command):
            if 'hw.product' in command:
                return 0, 'QEMU', ''
            elif 'virt.vendor' in command:
                return 0, 'OpenBSD', ''
            else:
                return -1, '', ''

        def get_bin_path(self, command):
            return self.sysctl_path

    class VirtualModule():
        def __init__(self):
            self.detector = Virtual

# Generated at 2022-06-13 04:27:30.428480
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    assert(VirtualSysctlDetectionMixin().detect_virt_vendor('security.jail.osreldate') == {'virtualization_tech_guest': {'jails'}, 'virtualization_tech_host': set(), 'virtualization_type': 'jails', 'virtualization_role': 'guest'})

# Generated at 2022-06-13 04:27:35.239074
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    sysctl_result = {
        "virtualization_tech_guest": set(["vmm"]),
        "virtualization_tech_host": set([]),
    }
    class_instance = VirtualSysctlDetectionMixin()
    class_instance.module = MockModule(**{
        "run_command.return_value": (0, "OpenBSD", None)
    })
    assert class_instance.detect_virt_vendor("security.jail.osrelease") == sysctl_result



# Generated at 2022-06-13 04:27:44.528051
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    from ansible.module_utils.facts.virtual.freebsd import VirtualSysctlDetectionMixin

    tmp = VirtualSysctlDetectionMixin()
    tmp.detect_sysctl = lambda: None
    tmp.module = lambda: None
    tmp.run_command = lambda: (0, 'qemu\n', '')
    virtual_vendor_facts = tmp.detect_virt_vendor(key='kern.vm_guest')
    assert virtual_vendor_facts['virtualization_type'] == 'kvm'
    assert virtual_vendor_facts['virtualization_role'] == 'guest'
    assert 'kvm' in virtual_vendor_facts['virtualization_tech_guest']
    assert len(virtual_vendor_facts['virtualization_tech_host']) == 0


# Unit test

# Generated at 2022-06-13 04:29:31.535399
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    mock_module = type('AnsibleModule', (object,), {'get_bin_path': lambda x, y: '/usr/bin/sysctl'})()
    mock_module.run_command = lambda x: (0, 'KVM', '')
    mixin = VirtualSysctlDetectionMixin()
    mixin.module = mock_module

    # Call method to test
    facts = mixin.detect_virt_product('hw.model')
    assert facts['virtualization_type'] == 'kvm'
    assert facts['virtualization_role'] == 'guest'
    assert 'kvm' in facts['virtualization_tech_guest']


# Generated at 2022-06-13 04:29:38.885479
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    class TestObj(VirtualSysctlDetectionMixin):
        pass
    t = TestObj()
    t.module = AnsibleModule({'sysctl_path': 'sysctl'})
    t.sysctl_path = t.module.get_bin_path('sysctl')
    # check for kvm
    t.module.run_command = MagicMock(return_value=(0, 'QEMU', ''))
    result_kvm = t.detect_virt_vendor('machdep.hypervisor')
    assert(result_kvm['virtualization_type'] == 'kvm')
    assert('kvm' in result_kvm['virtualization_tech_guest'])
    assert('kvm' not in result_kvm['virtualization_tech_host'])

# Generated at 2022-06-13 04:29:49.335521
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    class FakeModule(object):
        _binary_path = {'sysctl': 'sysctl'}

        def get_bin_path(self, binary, required=False):
            return self._binary_path[binary]

        def run_command(self, binary):
            if binary == 'sysctl -n kern.vm_guest':
                return 0, 'Linux', ''
            elif binary == 'sysctl -n security.jail.jailed':
                return 0, 'True', ''
            return 0, '', ''

    p = VirtualSysctlDetectionMixin()
    p.module = FakeModule()
    facts = p.detect_virt_vendor('kern.vm_guest')
    assert facts['virtualization_type'] == 'kvm'


# Generated at 2022-06-13 04:29:58.906501
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    class temp:
        def __init__(self):
            self.virtualization_tech_guest = set()
            self.virtualization_type = ''
            self.virtualization_role = ''

    class temp2:
        def __init__(self):
            self.virtualization_tech_host = set()

    class temp3:
        def get_bin_path(self):
            return True

        def run_command(self):
            return True

    class TestClass(VirtualSysctlDetectionMixin, temp, temp2, temp3):
        pass

    # Try when host is not virtualized
    test_class = TestClass()
    product = test_class.detect_virt_product('machdep.hypervisor_name')
    assert product['virtualization_tech_guest'] == set([])

# Generated at 2022-06-13 04:30:10.744574
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    # create a mock class and assign the detect_virt_product method to a new
    # method called run so we can test it
    class Obj:
        pass

    obj = Obj()
    obj.detect_virt_product = VirtualSysctlDetectionMixin.detect_virt_product

    obj.module = Obj()
    obj.module.run_command = run_command
    obj.module.get_bin_path = get_bin_path
    obj.detect_sysctl = detect_sysctl


# Generated at 2022-06-13 04:30:18.193856
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    vscp = VirtualSysctlDetectionMixin()

    # Test the various formats of output from sysctl of a virtual machine
    class TestModule(object):
        def get_bin_path(self, arg):
            return '/sbin/sysctl'
        def run_command(self, arg):
            if arg == '/sbin/sysctl -n hw.model':
                return 0, '10.0.0.1', ''
            elif arg == '/sbin/sysctl -n kern.smp.hlt_cpus':
                return 0, 'foo', ''
            elif arg == '/sbin/sysctl -n security.jail.jailed':
                return 0, '1', ''

# Generated at 2022-06-13 04:30:27.053886
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    # Monkey patched
    class FakeModule(object):
        def __init__(self):
            self.run_command_values = {
                'hw.model': (0, 'OpenBSD SunOS', ''),
                'hw.machine': (0, 'amd64', '')
            }

        def run_command(self, command):
            if command.startswith('sysctl -n'):
                return self.run_command_values.get(command.split('-n')[1].strip(), (255, '', ''))
            else:
                return (255, '', '')

    class FakeSelf(object):
        def __init__(self):
            self.sysctl_path = None
            self.module = FakeModule()

    # Testing result when running 'sysctl -n hw.model' command