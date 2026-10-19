

# Generated at 2022-06-13 04:20:41.898190
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    # We need to be able to instantiate the module and the class to
    # check if detection works
    import ansible.module_utils.facts.virtual.freebsd as virt
    import ansible.module_utils.facts.system.freebsd as sys

    obj = sys.SystemFreeBSD()
    obj.detect_platform_subclass = lambda: 'freebsd'
    obj.get_platform_subclass = lambda: 'freebsd'
    obj.distribution = 'freebsd'

    # Is jid the name of the jail?
    # Is jailed the name of the jail?


# Generated at 2022-06-13 04:20:48.867938
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    from . import detect_virt_vendor
    detection_mixin = VirtualSysctlDetectionMixin()
    detection_mixin.sysctl_path = '/usr/bin/sysctl'
    detection_mixin.module = detect_virt_vendor.AnsibleModule(
        argument_spec={},
        supports_check_mode=True)
    expected_virtual_vendor_facts = {
        'virtualization_tech_guest': set(['kvm', 'vmm']),
        'virtualization_tech_host': set(),
        'virtualization_type': 'vmm',
        'virtualization_role': 'guest'
    }

    virtual_vendor_facts = detection_mixin.detect_virt_vendor('machdep.vmm')

    assert virtual_vendor_facts == expected_virtual_

# Generated at 2022-06-13 04:20:53.729298
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    str_output = 'VirtualBox'
    obj = VirtualSysctlDetectionMixin()
    obj.module = AnsibleModule(argument_spec={})
    obj.detect_sysctl = MagicMock(return_value=True)
    obj.module.run_command = MagicMock(return_value=(0, str_output, ''))
    virtual_product_facts = obj.detect_virt_product('hw.model')
    assert virtual_product_facts['virtualization_type'] == 'virtualbox'
    assert virtual_product_facts['virtualization_role'] == 'guest'
    assert 'virtualization_tech_guest' in virtual_product_facts
    assert 'virtualization_tech_host' in virtual_product_facts


# Generated at 2022-06-13 04:20:59.929482
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    class TestVirtualSysctlDetectionMixin:
        def __init__(self):
            pass
        def get_bin_path(self):
            return ''
        def run_command(self):
            return [0, 'QEMU', '']
    virtual_sysctl_detection_mixin_inst = VirtualSysctlDetectionMixin()
    virtual_sysctl_detection_mixin_inst.module = TestVirtualSysctlDetectionMixin()
    virtual_sysctl_detection_mixin_inst.detect_sysctl()

# Generated at 2022-06-13 04:21:11.326629
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    class MockModule(object):
        def __init__(self):
            self.run_command_fails = False
            self.module_return_code = 0

        def get_bin_path(self, name):
            return '/usr/bin/sysctl'

        def run_command(self, command, check_rc=False):
            if self.run_command_fails is True:
                raise Exception("run_command failed!")
            return self.module_return_code, 'OpenBSD', ''

    class MockSysctlDetectionMixin():
        def __init__(self):
            self.module = MockModule()

    mixin = MockSysctlDetectionMixin()
    mixin.detect_virt_vendor('machdep.dmi.system-vendor')
    assert mixin.module.module_return

# Generated at 2022-06-13 04:21:20.156929
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    class FreeBSD(object):
        def __init__(self, module, sysctl_path):
            self.module = module
            self.sysctl_path = sysctl_path

        def get_bin_path(self, program):
            return self.sysctl_path

    class TestVirtualSysctlDetectionMixin(VirtualSysctlDetectionMixin):
        def __init__(self):
            self.module = FreeBSD(None, '/usr/bin/sysctl')

    # Test output from sysctl -n hw.vendor, which is "QEMU"
    obj = TestVirtualSysctlDetectionMixin()
    v = obj.detect_virt_vendor("hw.vendor")
    assert v['virtualization_tech_guest'] == set(['kvm'])

    # Test output from sysctl -n security.

# Generated at 2022-06-13 04:21:29.111679
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    mod = AnsibleModule(argument_spec=dict())
    mixin = VirtualSysctlDetectionMixin()
    facts = {}
    key = "kern.vm_guest"
    facts = mixin.detect_virt_vendor(key)
    ansible_test_assert_equal(facts['virtualization_tech_guest'], set(['kvm']))
    key = "kern.vm_guest"
    facts = mixin.detect_virt_vendor(key)
    ansible_test_assert_equal(facts['virtualization_type'], 'kvm')
    ansible_test_assert_equal(facts['virtualization_role'], 'guest')


# Generated at 2022-06-13 04:21:37.480908
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():

    from ansible.module_utils.basic import AnsibleModule
    from ansible_collections.ansible.misc.plugins.detectors.detect_virtualization_openbsd import VirtualizationDetector

    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    virtual_detector = VirtualizationDetector(module)
    virtual_detector.detect_sysctl = MagicMock()
    virtual_detector.detect_sysctl.return_value = None
    virtual_product_facts = virtual_detector.detect_virt_product('hw.model')
    assert virtual_product_facts == {}
    virtual_detector.detect_sysctl = MagicMock()
    virtual_detector.detect_sysctl.return_value = 'KVM'
   

# Generated at 2022-06-13 04:21:47.912648
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    module = FakeModule()

    v_type = 'kvm'
    module.run_command = lambda *args: v_type in args[1] and (0, v_type, '') or (1, '', '')
    virtual_product_facts = VirtualSysctlDetectionMixin().detect_virt_product('machdep.hypervisor')

    assert virtual_product_facts['virtualization_tech_guest'] == set(['kvm'])
    assert virtual_product_facts['virtualization_tech_host'] == set()
    assert virtual_product_facts['virtualization_type'] == 'kvm'
    assert virtual_product_facts['virtualization_role'] == 'guest'


# Generated at 2022-06-13 04:21:52.149646
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    class FakeModule(object):
        class FakeCM(object):

            def __init__(self):
                self.rc = 0
                self.out = ''
                self.err = ''
                self.rc2 = 0
                self.out2 = ''
                self.err2 = ''

            def run_command(self, cmd):
                if cmd.endswith('security.jail.jailed'):
                    return self.rc, self.out, self.err
                elif cmd.endswith('security.jail.enforce_statfs'):
                    return self.rc2, self.out2, self.err2

        def __init__(self):
            self.mod_cm = self.FakeCM()

        def get_bin_path(self, cmd):
            return '/usr/bin/sysctl'

   

# Generated at 2022-06-13 04:22:12.127504
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    class TestModule(object):
        def __init__(self):
            self.run_command_results = [
                (0, 'KVM', ''),
                (0, 'VMware', ''),
                (0, 'VirtualBox', ''),
                (0, 'HVM domU', ''),
                (0, 'Hyper-V', ''),
                (0, 'Parallels', ''),
                (0, 'RHEV Hypervisor', ''),
                (0, '1', ''),
                (0, 'QEMU', ''),
                (0, 'OpenBSD', '')
            ]
            self.run_command_index = 0

        def run_command(self, cmd):
            result = self.run_command_results[self.run_command_index]

# Generated at 2022-06-13 04:22:21.872874
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    # Create necessary structure to test
    module = {"run_command": lambda cmd, input: (0, "OpenBSD", None)}
    syctl_path = "/usr/sbin/sysctl"

    # Create instance of class VirtualSysctlDetectionMixin
    virtual_sysctl_detection_mixin = VirtualSysctlDetectionMixin()

    # Test detect_virt_vendor method
    result = virtual_sysctl_detection_mixin.detect_virt_vendor(sysctl_path, "hw.model", module)
    assert result["virtualization_type"] == "vmm"
    assert result["virtualization_role"] == "guest"


# Generated at 2022-06-13 04:22:29.703542
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    from ansible.module_utils import basic
    from ansible.module_utils.facts.collector import Collector

    class VirtualSysctlDetectionMixinTest(VirtualSysctlDetectionMixin, object):
        def __init__(self):
            self.module = basic.AnsibleModule(
                argument_spec={},
                supports_check_mode=True
            )
            self.facts = Collector()

    detect_virt_product_test = VirtualSysctlDetectionMixinTest()
    detect_virt_product_test.detect_sysctl = lambda: True
    detect_virt_product_test.module.run_command = lambda x: (0, 'VirtualBox', '')

    # Key: {key, product, role}
    # Value: sysctl-output

# Generated at 2022-06-13 04:22:41.028760
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    class _module(object):

        def __init__(self):
            self.params = {'virt_what_path': '/usr/bin/virt-what'}

        def get_bin_path(self, arg, **kwargs):
            if arg == "sysctl":
                return "/usr/bin/sysctl"
            return None

        def run_command(self, cmd):
            if cmd == "/usr/bin/sysctl -n kern.vm_guest":
                return 0, "OpenBSD", None
            if cmd == "/usr/bin/sysctl -n machdep.hypervisor_vendor":
                return 0, "QEMU", None

# Generated at 2022-06-13 04:22:50.762892
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    mixin = VirtualSysctlDetectionMixin()
    mixin.sysctl_path = True

    # test_detect_virt_vendor_fails
    setattr(mixin, "module", MockModule("", "EACCES"))
    assert mixin.detect_virt_vendor("") == {}

    # test_detect_virt_vendor_kvm
    setattr(mixin, "module", MockModule("QEMU", ""))
    assert mixin.detect_virt_vendor("") == {
        'virtualization_type': 'kvm',
        'virtualization_role': 'guest',
        'virtualization_tech_guest': {'kvm'},
        'virtualization_tech_host': {}
    }

    # test_detect_virt_vendor_vmm
   

# Generated at 2022-06-13 04:23:00.747780
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    import sys
    sys.path.append('/usr/local/lib/python2.7/site-packages/')
    import ansible
    from ansible.module_utils.facts.virtual.freebsd import VirtualSysctlDetectionMixin
    from ansible.modules.system import sysctl

    sysctl_fixture = sysctl.AnsibleModule(
        argument_spec = dict(
            name = dict(required=True)
        )
    )

    for sysctl_key in ['security.jail.jailed', 'hw.model']:
        sysctl_fixture.params['name'] = sysctl_key
        d = VirtualSysctlDetectionMixin()
        d.module = sysctl_fixture
        virtual_facts = d.detect_virt_product(sysctl_key)
        assert virtual_facts

# Generated at 2022-06-13 04:23:07.008381
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    class FakeModule(object):
        def __init__(self):
            self.run_command_results = [[0, "KVM", ""]]
            self.run_command_calls = []
            self.get_bin_path_results = ["/usr/bin/sysctl"]
            self.get_bin_path_calls = []
        def get_bin_path(self, name, opt_dirs=[]):
            self.get_bin_path_calls.append(name)
            return self.get_bin_path_results.pop(0)
        def run_command(self, cmd):
            self.run_command_calls.append(cmd)
            return self.run_command_results.pop(0)
    v = VirtualSysctlDetectionMixin()
    v.module = FakeModule()

# Generated at 2022-06-13 04:23:16.078096
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    class TestClass(object):
        class TestModule(object):
            def __init__(self):
                self.bin_path = '/usr/bin'
            def get_bin_path(self, name):
                return os.path.join(self.bin_path, name)
            def run_command(self, cmd):
                return (0, 'OpenBSD', '')
    test = TestClass()
    test.module = TestClass.TestModule()
    mixin = VirtualSysctlDetectionMixin()
    result = mixin.detect_virt_vendor('hw.model')
    assert result['virtualization_type'] == 'vmm'
    assert result['virtualization_role'] == 'guest'

# Generated at 2022-06-13 04:23:27.523088
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    '''
    Test method detect_virt_product of class VirtualSysctlDetectionMixin
    '''
    module = sys.modules[__name__]
    try:
        module.run_command
    except AttributeError:
        from ansible.module_utils.basic import AnsibleModule
        module = AnsibleModule(argument_spec={})
        module.run_command = lambda cmd: (0, 'KVM', '')

    module.get_bin_path = lambda cmd: '/usr/bin/sysctl'
    module.sysctl_path = None

    module.detect_sysctl = VirtualSysctlDetectionMixin.detect_sysctl
    module.detect_virt_product = VirtualSysctlDetectionMixin.detect_virt_product
    module.detect_virt_vendor = VirtualSysctlDetection

# Generated at 2022-06-13 04:23:37.923740
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    class d():
        module = d()
        sysctl_path = '/sbin/sysctl'

    class m():
        def get_bin_path(self, cmd):
            return '/sbin/sysctl'

        def run_command(self, cmd):
            cmd = cmd.split(' ')
            rc = 0
            err = None
            if cmd[-1] == "hw.vendor":
                out = "QEMU"
            elif cmd[-1] == "hw.product":
                out = "Standard PC (i440FX + PIIX, 1996)"
            elif cmd[-1] == "hw.machine_arch":
                out = "amd64"
            elif cmd[-1] == "security.jail.jailed":
                out = "0"

# Generated at 2022-06-13 04:24:10.454185
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    sysctl_result = "QEMU"
    module_mock = MockOpenBSDModule()
    mixin = VirtualSysctlDetectionMixin()
    mixin.detect_sysctl = Mock()
    mixin.detect_sysctl.return_value = True
    mixin.module = module_mock
    mixin.module.run_command.return_value = 0, sysctl_result, ''

    virtual_vendor_facts = mixin.detect_virt_vendor('machdep.hypervisor_vendor')
    assert virtual_vendor_facts['virtualization_tech_guest'] == set(['kvm'])
    assert virtual_vendor_facts['virtualization_tech_host'] == set()
    assert virtual_vendor_facts['virtualization_role'] == 'guest'
    assert virtual

# Generated at 2022-06-13 04:24:18.126132
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    fact_subclass = VirtualSysctlDetectionMixin()
    fact_subclass.module = FakeModule()
    fact_subclass.module.run_command = FakeCommand()
    fact_subclass.module.run_command.side_effect = [
        # first call to run_command
        (0, 'OpenBSD', ''),
        ]
    fact_subclass.sysctl_path = 'valid/path'

    result = fact_subclass.detect_virt_vendor('vm.vmm_name')

    assert result['virtualization_role'] == 'guest'
    assert result['virtualization_type'] == 'vmm'


# Generated at 2022-06-13 04:24:25.668149
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    class TestModule(object):
        def get_bin_path(self, argument):
            return None

        def run_command(self, argument):
            return (0, 'OpenBSD', '')

    class TestObject(object):
        def __init__(self):
            self.module = TestModule()
            self.sysctl_path = None
            self.fact_id = "vm.guest.product_name"

    instance = TestObject()
    instance = VirtualSysctlDetectionMixin()
    result = instance.detect_virt_vendor(instance.fact_id)

# Generated at 2022-06-13 04:24:38.101124
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    mixin_obj = VirtualSysctlDetectionMixin()
    mixin_obj.detect_sysctl = lambda: True
    mixin_obj.sysctl_path = "sysctl"
    mixin_obj.module = MockModule()
    mixin_obj.module.run_command = lambda command: (0, "1", None)
    virt_product_facts = {
        'virtualization_type': 'jails',
        'virtualization_role': 'guest',
        'virtualization_tech_guest': set(['jails']),
        'virtualization_tech_host': set([])}
    assert mixin_obj.detect_virt_product(key="security.jail.jailed") == virt_product_facts


# Generated at 2022-06-13 04:24:47.249109
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    class MockModule(object):
        def __init__(self, rc, out, err, command):
            self.rc = rc
            self.out = out
            self.err = err
            self.command = command
        def run_command(self, cmd):
            self.command = cmd
            return (self.rc, self.out, self.err)

    class MockSysctlDetectionMixin(VirtualSysctlDetectionMixin):
        def __init__(self, module):
            self.module = module

    module = MockModule(0, '', '', '')
    sysctl_path = '/usr/sbin/sysctl'
    module.get_bin_path = Mock(return_value=sysctl_path)
    sysctl_detection_mixin = MockSysctlDetectionMixin(module)
    facts

# Generated at 2022-06-13 04:24:57.519671
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    class FakeModule(object):
        def __init__(self):
            self.run_command_rcs = {
                'sysctl -n hw.model': 0,
                'sysctl -n hw.machine': 0,
                'sysctl -n hw.version': 0,
                'sysctl -n kern.hostuuid': 0,
                'sysctl -n security.jail.jailed': 0
            }

# Generated at 2022-06-13 04:25:08.585918
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    class FakeBSDModule():
        def __init__(self):
            self.params = {'name': 'OpenBSD'}

        def get_bin_path(self, path):
            return '/sbin/sysctl'

        def run_command(self, cmd):
            return 0, 'OpenBSD', ''

    b = VirtualSysctlDetectionMixin()
    b.module = FakeBSDModule()
    b.sysctl_path = b.module.get_bin_path('sysctl')
    assert b.detect_virt_vendor('security.jail.jailed') == \
        {'virtualization_tech_guest': set(['vmm']),
         'virtualization_tech_host': set(),
         'virtualization_type': 'vmm',
         'virtualization_role': 'guest'}

# Generated at 2022-06-13 04:25:19.484703
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    virtual_product_facts = VirtualSysctlDetectionMixin()
    virtual_product_facts.sysctl_path = '/sbin/sysctl'
    virtual_product_facts.module = MagicMock()
    virtual_product_facts.module.run_command = MagicMock()
    virtual_product_facts.module.run_command.return_value = (0, 'KVM', '')
    ret = virtual_product_facts.detect_virt_product('kern.vm_guest')
    expected = {'virtualization_role': 'guest', 'virtualization_type': 'kvm',
                'virtualization_tech_host': set(), 'virtualization_tech_guest': {'kvm'}}
    assert ret == expected


# Generated at 2022-06-13 04:25:30.614138
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    # Creating a Mock class for VirtualSysctlDetectionMixin
    class _VirtualSysctlDetectionMixin(VirtualSysctlDetectionMixin):
        def __init__(self):
            self.module = AnsibleModuleMock()
            self.module.run_command = run_command
            self.sysctl_path = None

    # Creating a Mock class for AnsibleModule
    class AnsibleModuleMock:
        def get_bin_path(self, app):
            return app

    # Creating a Mock function for AnsibleModule's run_command
    def run_command(self, cmd):
        error_msg = ''
        stdout = ''
        rc = 0
        if cmd == 'sysctl -n hw.model':
            stdout = 'VirtualBox'

# Generated at 2022-06-13 04:25:38.985501
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    from ansible.module_utils.facts.virtual.freebsd import VirtualSysctlDetectionMixin
    class VirtualSysctlDetectionMixinClass(VirtualSysctlDetectionMixin):
        def __init__(self):
            self.module = AnsibleModuleMock()
            self.sysctl_path = None

    class AnsibleModuleMock():
        def __init__(self):
            self.run_command_answers = {}

        def get_bin_path(self, program):
            return '/sbin/sysctl'

        def run_command(self, command, check_rc=False, close_fds=False, executable=None, data=None):
            if command in self.run_command_answers:
                return self.run_command_answers[command]

# Generated at 2022-06-13 04:26:23.922177
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    mixin = VirtualSysctlDetectionMixin()
    mixin.detect_sysctl = lambda: True
    mixin.module = MockModule()
    mixin.module.run_command = lambda x: (0, 'QEMU', '')

    assert mixin.detect_virt_vendor('kern.vm_guest') == {'virtualization_tech_guest': set(['kvm']), 'virtualization_tech_host': set([]), 'virtualization_type': 'kvm', 'virtualization_role': 'guest'}


# Generated at 2022-06-13 04:26:34.505487
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    from ansible.module_utils.facts.system.bsd import BsdFactCollector
    from ansible.module_utils.facts.virtual.bsd import BsdVirtual
    from ansible.module_utils.facts.virtual.bsd import VirtualSysctlDetectionMixin

    mixin = VirtualSysctlDetectionMixin()

    # Test host detection
    collector = BsdFactCollector()
    collector.get_bsd_virtual = lambda: BsdVirtual()
    collector.collect()
    virtual = collector.get_bsd_virtual()

    if not virtual.virtualization_type:
        virtual.virtualization_type = 'openbsd'
    virtual.virtualization_role = 'host'

    mixin.module = None
    mixin.sysctl_path = '/sbin/sysctl'
    mixin.detect

# Generated at 2022-06-13 04:26:39.763297
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    tmp = VirtualSysctlDetectionMixin()
    tmp.detect_sysctl = lambda: 0
    tmp.module = {}
    tmp.module.run_command = lambda x: [0, "vmm guest", ""]
    virtual_facts = tmp.detect_virt_product("hw.model")
    assert virtual_facts['virtualization_type'] == 'vmm'
    assert virtual_facts['virtualization_role'] == 'guest'
    assert list(virtual_facts['virtualization_tech_guest']) == ['vmm']
    assert list(virtual_facts['virtualization_tech_host']) == []


# Generated at 2022-06-13 04:26:43.999309
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    command_result = {
        'rc': 0,
        'stdout': 'QEMU',
        'stderr':''
    }

    module_args = {
    }

    my_obj = VirtualSysctlDetectionMixin()
    my_obj.module = MagicMock()
    my_obj.detect_sysctl = MagicMock()
    my_obj.module.run_command.return_value = command_result

    expected_vendor_facts = {
        'virtualization_type': 'kvm',
        'virtualization_role': 'guest',
        'virtualization_tech_guest': set(['kvm']),
        'virtualization_tech_host': set([])
    }

    assert my_obj.detect_virt_vendor('hw.vmm.version') == expected_

# Generated at 2022-06-13 04:26:49.919454
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    from ansible.module_utils.facts.virtual import VirtualSysctlDetectionMixin
    from ansible.module_utils.facts.virtual import VirtualSysctlDetectionMixin
    from ansible.module_utils.facts.virtual import VirtualSysctlDetectionMixin
    virtual_vendor_facts = {}
    host_tech = set()
    guest_tech = set()
    module_class = VirtualSysctlDetectionMixin
    virtual_vendor_facts['virtualization_tech_guest'] = guest_tech
    virtual_vendor_facts['virtualization_tech_host'] = host_tech
    module_class.detect_sysctl(module_class)
    module_class.detect_virt_vendor('key',module_class)

# Generated at 2022-06-13 04:26:58.497918
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    virtual_vendor_facts = dict()
    try:
        from ansible.module_utils.facts.virtual.openbsd import OpenBSDVirtualSysctlDetectionMixin
        current_virtual_openbsd = OpenBSDVirtualSysctlDetectionMixin()
    except:
        pass
    current_virtual_openbsd.module = MockModule()
    current_virtual_openbsd.sysctl_path = "/sbin/sysctl"
    current_virtual_openbsd.module.run_command = Mock(return_value=(0, 'QEMU', ''))
    virtual_vendor_facts = current_virtual_openbsd.detect_virt_vendor("kern.suse.product")
    assert virtual_vendor_facts.get('virtualization_type') == 'kvm'
    assert virtual_vendor_

# Generated at 2022-06-13 04:27:09.476981
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    from ansible.module_utils.facts.system.base import VirtualSysctlDetectionMixin
    from ansible.module_utils.facts.system.base import Sysctl
    from ansible.module_utils.facts.system.base import BaseSysinfo

    class DummyModule(object):
        def __init__(self):
            self.params = None

        def run_command(self, args):
            if 'virtualization.vendor' in args:
                return 0, 'OpenBSD', ''
            elif 'virtualization.product' in args:
                return 1, 'OpenBSD', ''

        def get_bin_path(self, name, opts=None):
            if name in ('sysctl',):
                return self.run_command


# Generated at 2022-06-13 04:27:19.058795
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    class VirtualSysctlDetectionMixinMock(VirtualSysctlDetectionMixin):
        def __init__(self):
            self.hostname = 'hostname'
            self.sysctl_path = '/sbin/sysctl'
            self.module = AnsibleModuleMock()

    class AnsibleModuleMock():
        def __init__(self):
            self.params = {}
            self.run_command_values = {}

        def get_bin_path(self, arg):
            pass

        def run_command(self, arg, arg2):
            return self.run_command_values.get(arg, (0, None, None))

    class DetectMock():
        def __init__(self):
            self.facts = {}


# Generated at 2022-06-13 04:27:28.285375
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts import virtual

    # v0 has empty strings, v1 has populated strings
    virtual_test_values = [
        ["", "", "1", "", "", "", "", "", "", "", "", ""],
        ["KVM", "VMware", "VirtualBox", "HVM domU", "XenPVH", "XenPV", "XenPVHVM", "Hyper-V", "Parallels", "RHEV Hypervisor", "", "1"],
    ]

    # v0 has empty strings, v1 has populated strings
    virtual_test_keys = [
        "hw.model",
        "security.jail.jailed",
    ]


# Generated at 2022-06-13 04:27:37.064609
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    class args:
        module = None
        sysctl_path = ""
        sysctl_key = ""

    class module:
        run_command = Mock(return_value=(0, "QEMU", None))

    virtual_vendor = VirtualSysctlDetectionMixin()
    virtual_vendor.args = args
    virtual_vendor.module = module

    out = virtual_vendor.detect_virt_vendor("machine.model")
    assert out == { 'virtualization_tech_guest': set(['kvm']), 'virtualization_tech_host': set(),
                    'virtualization_type': 'kvm', 'virtualization_role': 'guest' }


# Generated at 2022-06-13 04:29:19.665789
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    # Testing virtualization_role and virtualization_type facts in OpenBSD
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.facts.os import VirtualSysctlDetectionMixin
    import tempfile
    import textwrap
    import os
    import shutil
    tmp_dir = tempfile.mkdtemp()
    tmp_file = "%s/sysctl" % tmp_dir

# Generated at 2022-06-13 04:29:29.503065
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    import sys
    import mock

    sys.modules["freebsd_version"] = mock.Mock()
    sys.modules["freebsd_version"].version = "12.0"

    mod = mock.MagicMock()
    mod.run_command.return_value = (0, "XenPVHVM", "")
    mod.get_bin_path.return_value = "/usr/sbin/sysctl"

    mixin = VirtualSysctlDetectionMixin()
    mixin.module = mod
    ret = mixin.detect_virt_product("hw.model")

    mod.run_command.assert_called_with("/usr/sbin/sysctl -n hw.model")
    assert ret["virtualization_type"] == "xen", "virtualization_type is not xen"
    assert ret

# Generated at 2022-06-13 04:29:38.179680
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    class test_for_mixin(object):
        def __init__(self):
            self.sysctl_path = '/usr/bin/sysctl'

        def get_bin_path(self, *args, **kwargs):
            return self.sysctl_path

        def run_command(self, *args, **kwargs):
            if args[0] == '/usr/bin/sysctl -n machdep.cpu.brand_string':
                out = 'Intel(R) Xeon(R) CPU E5-2650 v3 @ 2.30GHz'

# Generated at 2022-06-13 04:29:43.867061
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    class VirtualSysctlDetectionMixinTest(VirtualSysctlDetectionMixin):
        def __init__(self, module):
            self.module = module

    class AnsibleModuleTest:
        def __init__(self):
            self.params = {}

        def get_bin_path(self, name):
            return '/sbin/sysctl'

        def run_command(self, cmd):
            if cmd == "/sbin/sysctl -n hw.model":
                out = "OpenBSD"
                return 0, out, ""
            elif cmd == "/sbin/sysctl -n hw.model":
                out = "QEMU"
                return 0, out, ""
            elif cmd == "/sbin/sysctl -n hw.vendor_id":
                out = "QLogic"
                return

# Generated at 2022-06-13 04:29:54.436943
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    import sys

    class FakeModule(object):
        def __init__(self):
            self.run_command_result = (0, 'KVM', '')
            self.get_bin_path_result = '/usr/bin/sysctl'

        def run_command(self, command):
            return self.run_command_result

        def get_bin_path(self, command):
            return self.get_bin_path_result

    class FakeAnsibleModule(object):
        def __init__(self):
            self.module = FakeModule()

    results = {}
    obj = VirtualSysctlDetectionMixin()
    obj = obj.__class__()
    obj.module = FakeAnsibleModule().module
    results = obj.detect_virt_product('hw.product')


# Generated at 2022-06-13 04:30:00.768411
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    class TestVirtualSysctlDetectionMixin(VirtualSysctlDetectionMixin):
        def __init__(self):
            self.module = None

    test_object = TestVirtualSysctlDetectionMixin()
    test_facts = test_object.detect_virt_product('hw.model')
    assert test_facts['virtualization_type'] == 'kvm'
    assert test_facts['virtualization_role'] == 'guest'
    assert test_facts['virtualization_tech_host'] == set()
    assert test_facts['virtualization_tech_guest'] == set(['kvm'])


# Generated at 2022-06-13 04:30:11.245061
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    # create a test class.
    class MyVirtualSysctlDetectionMixin(VirtualSysctlDetectionMixin):
        def __init__(self, module):
            # set these attributes so that detect_sysctl
            # can use them
            self.sysctl_path = "/sbin/sysctl"
            self.module = module

        def detect_sysctl(self):
            pass

    # create a mock module
    import sys
    import types
    import ansible
    mock_module = types.ModuleType("ansible.module_utils.basic")
    mock_module.run_command = ansible.module_utils.basic.run_command
    mock_module.get_bin_path = lambda x: "/sbin/sysctl"
    mock_module.exit_json = lambda x: sys.exit(0)
    mock_

# Generated at 2022-06-13 04:30:17.029439
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    test_instance = VirtualSysctlDetectionMixin()
    test_output_dict = {}
    test_output_dict = test_instance.detect_virt_product('machdep.hypervisor_name')
    test_output_dict = test_instance.detect_virt_product('machdep.emulated_guest_type')
    test_output_dict = test_instance.detect_virt_product('machdep.emulated_guest_os')
    test_output_dict = test_instance.detect_virt_product('machdep.cpu.features')
    test_output_dict = test_instance.detect_virt_product('security.jail.jailed')
    test_output_dict = test_instance.detect_virt_product('machdep.bios.vendor')
    test_

# Generated at 2022-06-13 04:30:21.549599
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    from ansible.module_utils.facts.virtual.freebsd import OpenBSD_VirtualSysctlDetectionMixin
    import os
    import sys

    # Cannot use virtual_product_detection_sysctl because it requires the
    # sysctl module and all tests are done on the python code directly.
    class OpenBSD_VirtualSysctlDetection(OpenBSD_VirtualSysctlDetectionMixin):
        def detect_sysctl(self):
            self.sysctl_path = "/sbin/sysctl"

    class TestAnsibleModule(object):
        arguments = {'base_dir': os.path.dirname(sys.argv[0])}
        params = {}

        class TestModule(object):
            def __init__(self, *arg):
                self.params = TestAnsibleModule.params
