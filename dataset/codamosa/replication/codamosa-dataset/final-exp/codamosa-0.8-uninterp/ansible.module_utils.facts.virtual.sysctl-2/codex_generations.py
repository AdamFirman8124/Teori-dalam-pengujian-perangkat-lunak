

# Generated at 2022-06-13 04:20:44.878017
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    from ansible.module_utils import basic
    from ansible.module_utils.facts.collector.freebsd import VirtualSysctlDetectionMixin

    class Options:
        def __init__(self):
            self.virtual = None
            self.fetch_subset = None
            self.config = None

    class VirtualSysctlDetectionMixinLynx(VirtualSysctlDetectionMixin):
        def __init__(self):
            self.sysctl_path = None
            self.module = basic.AnsibleModule({}, {}, [], [])
            self.module.params = Options()
            self.facts = {}

    test = VirtualSysctlDetectionMixinLynx()
    test.facts[test.detect_virt_product("hw.model")] = 'KVM'

# Generated at 2022-06-13 04:20:52.908774
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    FakeSysctlModule = type('FakeSysctlModule', (object,), {'run_command': lambda self, command: (0, """KVM (0): QEMU Virtual CPU version 2.1.2
""", ''), 'get_bin_path': lambda self, name: '/bin/sysctl'})
    results = {}
    results['virtualization_type'] = 'kvm'
    results['virtualization_role'] = 'guest'
    results['virtualization_tech_guest'] = set(['kvm'])
    results['virtualization_tech_host'] = set()
    assert VirtualSysctlDetectionMixin().detect_virt_product('hw.model') == results


# Generated at 2022-06-13 04:20:58.932724
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    module_mock = AnsibleModuleMock()
    module_mock.get_bin_path.return_value = "/usr/sbin/sysctl"
    module_mock.run_command.return_value = (0, "QEMU", "")
    module_mock.run_command.return_value = (0, "KVM", "")
    module_mock.run_command.return_value = (0, "XenPV", "")
    module_mock.run_command.return_value = (0, "VirtualBox", "")
    module_mock.run_command.return_value = (0, "VMware", "")
    module_mock.run_command.return_value = (0, "Hyper-V", "")
    module_mock.run_command.return_

# Generated at 2022-06-13 04:21:10.647829
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    import platform
    if platform.system() != 'FreeBSD':
        print("Test only works on FreeBSD")
        return
    import os, sys
    from ansible.module_utils.facts.virtual.freebsd import VirtualSysctlDetectionMixin
    from ansible.module_utils.facts.system.freebsd import FreeBSDHardware
    sys.modules['sys'] = os
    sys.modules['ansible.module_utils.facts.system.freebsd'] = os 
    sys.modules['ansible.module_utils.facts.virtual.freebsd'] = os 
    class myModule:
        class sys(os):
            platform = 'FreeBSD'
            def get_bin_path(self, exe):
                if exe == 'sysctl': 
                    return 'sysctl'
                return ''

# Generated at 2022-06-13 04:21:19.951926
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    # Create a VirtualSysctlDetectionMixin object
    virtual_sysctl_detection_mixin = VirtualSysctlDetectionMixin()

    # Create a virtual_vendor_facts dictionary
    virtual_vendor_facts = \
    {
        'virtualization_type': 'kvm',
        'virtualization_role': 'guest'
    }

    # Set the module_executor property of the object
    virtual_sysctl_detection_mixin.module_executor = \
    {
        'run_command': \
        lambda *args: (0, 'QEMU', '')
    }

    # Check that deteect_virt_vendor method return a dictionary containing
    # the right values

# Generated at 2022-06-13 04:21:29.824408
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    class FakeModule(object):
        def run_command(self, _):
            return (0, 'OpenBSD', '')
    class FakeSuperClass(object):
        def __init__(self):
            self.module = FakeModule()
    class TestClass(VirtualSysctlDetectionMixin, FakeSuperClass):
        def __init__(self):
            self.sysctl_path = 'sysctl'
            FakeSuperClass.__init__(self)
    _ = TestClass()
    expected = {
        'virtualization_type': 'vmm',
        'virtualization_role': 'guest',
        'virtualization_tech_guest': set(['vmm']),
        'virtualization_tech_host': set()
    }

    result = _.detect_virt_vendor('hw.model')

# Generated at 2022-06-13 04:21:37.934638
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    virtual_sysctl_detection_mixin = VirtualSysctlDetectionMixin()
    virtual_sysctl_detection_mixin.detect_sysctl = Mock(return_value=True)
    virtual_sysctl_detection_mixin.module = Mock()
    virtual_sysctl_detection_mixin.module.run_command = Mock(return_value=(0, 'KVM', None))
    result = virtual_sysctl_detection_mixin.detect_virt_product('machdep.hypervisor')
    assert result == {'virtualization_role': 'guest', 'virtualization_type': 'kvm', 'virtualization_tech_guest': {'kvm'}, 'virtualization_tech_host': set()}


# Generated at 2022-06-13 04:21:49.795973
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    class Result():
        def __init__(self):
            self.result = {
                'virtualization_tech_guest': set(),
                'virtualization_tech_host': set(),
            }

    class FakeModule():
        def __init__(self):
            self.result = Result()
            self.run_command = run_command_mock

    class FakeObject():
        def __init__(self):
            self.module = FakeModule()

    def run_command_mock(*args, **kwargs):
        return 0, "OpenBSD", ""

    x = FakeObject()
    x.detect_sysctl()
    x.detect_virt_vendor('security.hostuuid')

    assert x.module.result.result['virtualization_tech_guest'] == set(['vmm'])
   

# Generated at 2022-06-13 04:21:55.808282
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    class Object(VirtualSysctlDetectionMixin):
        pass
    o = Object()
    o.module = create_module_mock('', rc=0, out='KVM', command_string="%s -n %s" % (o.sysctl_path, 'hw.product'))
    virtual_product_facts = o.detect_virt_product('hw.product')
    assert virtual_product_facts == dict(
        virtualization_role='guest',
        virtualization_type='kvm',
        virtualization_tech_guest={'kvm'},
        virtualization_tech_host={},
    )


# Generated at 2022-06-13 04:22:03.610412
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    class ModuleExec(object):
        def run_command(self, command):
            return 1, 'OpenBSD\n', ''

        def get_bin_path(self, command):
            return '/bin/sysctl'

    class Obj(VirtualSysctlDetectionMixin):
        def __init__(self, module):
            self.module = module

    obj = Obj(ModuleExec())
    results = obj.detect_virt_vendor('machdep.vmm.vendor')
    assert {'virtualization_role': 'guest', 'virtualization_type': 'vmm', 'virtualization_tech_host': set(), 'virtualization_tech_guest': {'vmm'}} == results



# Generated at 2022-06-13 04:22:28.665693
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    from ansible.module_utils.facts.virtual.freebsd import VirtualSysctlDetectionMixin
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts.virtual import Virtual, virtual_collector

    class VirtualSysctlDetectionMixinTest(VirtualSysctlDetectionMixin):
        def __init__(self, module):
            self.module = module

    # Class to combine the mixin with Virtual and virtual_collector so we can
    # get a virtual_collector.collect() call
    class TestVirtualSysctlDetectionMixin(Virtual, VirtualSysctlDetectionMixinTest):
        def __init__(self, module):
            self.module = module

    # Make a fake module object
    module = AnsibleModule({})

    result = {}

# Generated at 2022-06-13 04:22:32.793205
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    from ansible.modules.system import darwin
    from ansible.module_utils.facts.virtual.base import VirtualCollector

    class VirtualCollectorSub(VirtualSysctlDetectionMixin, VirtualCollector):
        pass

    class DarwinSub(darwin.Darwin, VirtualCollectorSub):
        pass

    assert DarwinSub().detect_virt_vendor("machdep.cpu.brand_string") == {
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set(),
        'virtualization_type': 'vmm',
        'virtualization_role': 'guest'
    }

# Generated at 2022-06-13 04:22:43.491636
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    mod = VirtualSysctlDetectionMixin()
    mod.module = DummyAnsibleModule()
    mod.sysctl_path = '/sbin/sysctl'
    mod.module.run_command = MagicMock(return_value=(0, 'Bochs, XenPVHVM', ''))

# Generated at 2022-06-13 04:22:52.097654
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    obj = VirtualSysctlDetectionMixin()
    obj.detect_virt_product('hw.model')
    obj.detect_virt_product('compat.linux.osrelease')
    obj.detect_virt_product('compat.linux.osrelease')
    obj.detect_virt_product('compat.linux.osrelease')
    obj.detect_virt_product('compat.linux.osrelease')
    obj.detect_virt_product('compat.linux.osrelease')
    obj.detect_virt_product('compat.linux.osrelease')
    obj.detect_virt_product('hw.model')
    obj.detect_virt_product('hw.model')
    obj.detect_virt_product('hw.model')

# Generated at 2022-06-13 04:23:01.675165
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    from ansible.module_utils.facts.virtual.freebsd.virtual import VirtualSysctlDetectionMixin
    from ansible.module_utils.six import with_metaclass

    class Input():
        class AnsibleModule():
            def run_command(self, cmd):
                if cmd == '/sbin/sysctl -n hw.model':
                    return 0, 'QEMU Virtual CPU version 2.5+', ''
                elif cmd == '/sbin/sysctl -n security.jail.jailed':
                    return 0, '1', ''
                else:
                    return 0, '', ''
            def get_bin_path(self, binary):
                return '/sbin/{0}'.format(binary)
        module = AnsibleModule()


# Generated at 2022-06-13 04:23:10.523061
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    from ansible.module_utils.facts import VirtualSysctlDetectionMixin
    from ansible.module_utils.facts import Facts
    from ansible.module_utils.facts.sysctl import SysctlFacts
    from ansible.module_utils._text import to_bytes

    class ModuleStub(object):
        def __init__(self):
            self.fail_json = lambda x: False

        def run_command(self, *args, **kwargs):
            return (0,to_bytes('OpenBSD'),'')

        def get_bin_path(self, *args, **kwargs):
            return '/sbin/sysctl'

    class FactsStub(object):
        def get_hypervisor_type(self):
            return None

    module_stub = ModuleStub()
    facts_stub = Facts

# Generated at 2022-06-13 04:23:15.435998
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    from ansible.module_utils._text import to_bytes
    import platform
    import os
    import tempfile
    import json

    test_platform = platform.system()
    current_os = platform.dist()[0]
    current_version = platform.dist()[1]

    module = AnsibleModule(
        argument_spec=dict(
            key=dict(type='str')
        )
    )
    module.detect_virt_vendor = VirtualSysctlDetectionMixin.detect_virt_vendor

    if current_os in ('FreeBSD', 'OpenBSD'):
        if test_platform == 'OpenBSD':
            rc, out, err = module.run_command("echo 'OpenBSD\n' | %s -n %s" % (module.sysctl_path, module.params['key']))


# Generated at 2022-06-13 04:23:22.051383
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    from ansible.module_utils.facts.system.base import VirtualSysctlDetectionMixin

    class VirtualSysctlDetectionMixinDummyClass(VirtualSysctlDetectionMixin):
        def __init__(self):
            self.sysctl_path = ''
            self.module = VirtualSysctlDetectionMixinDummyModule()

        def detect_sysctl(self):
            self.sysctl_path = 'sysctl'

    class VirtualSysctlDetectionMixinDummyModule():
        def __init__(self):
            pass

        def get_bin_path(self, name):
            return 'sysctl'

        def run_command(self, cmd):
            return 0, 'QEMU', ''

    vdm = VirtualSysctlDetectionMixinDummyClass()

# Generated at 2022-06-13 04:23:33.524327
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    import os
    from distutils.version import LooseVersion

    from ansible.module_utils.facts.virtual.openbsd import OpenBSDCustomSysctlDetectionPlugin
    from ansible.module_utils.facts.virtual.base import BaseVirtual
    from ansible.module_utils.facts.virtual.openbsd import OpenBSDVirtual

    module = FakeModule(paths={
        'sysctl_path': '/usr/sbin/sysctl'
        })
    if LooseVersion(OpenBSDVirtual.distribution) >= LooseVersion('5.5'):
        # Default OpenBSD version of custom sysctl detection plugin
        sysctl_detection_plugin = OpenBSDCustomSysctlDetectionPlugin(module)
    else:
        # Custom version of OpenBSD sysctl detection plugin
        sysctl_detection_plugin = VirtualSysctlDet

# Generated at 2022-06-13 04:23:42.970469
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    from ansible.module_utils.facts import VirtualSysctlDetectionMixin
    from ansible.module_utils.facts import Facts
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.pycompat24 import get_exception
    from ansible.module_utils._text import to_bytes

    class MyFacts(Facts):
        def __init__(self):
            self._module = AnsibleModule(
                argument_spec={},
            )
            super(MyFacts, self).__init__()

        def populate(self):
            pass

    facts = MyFacts()

    class FakeVirtVendor(VirtualSysctlDetectionMixin):
        def __init__(self, facts):
            self.facts = facts
            self.sysctl_path = None
            self

# Generated at 2022-06-13 04:24:33.251369
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    module = BaseMockedModule()
    class_instance = VirtualSysctlDetectionMixin()
    class_instance.module = module
    module.sysctl_path = "/sbin/sysctl"
    module.client = BaseMockedClient()

# Generated at 2022-06-13 04:24:43.738118
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    module = MockAnsibleModule('bsd')
    module.params = {
        'key': 'hw.product'
    }
    module._command_strings = {
        'sysctl': 'sysctl'
    }
    module.run_command = MockAnsibleRunCommand(module)
    # Set the return values
    module.run_command().returncode = 0
    module.run_command().stdout = 'QEMU'
    virtual_sysctl_detection = VirtualSysctlDetectionMixin()
    virtual_sysctl_detection.module = module

# Generated at 2022-06-13 04:24:53.401945
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    class ModuleMock(object):
        def __init__(self, bin_paths, run_command_result):
            self.run_command_result = run_command_result
            self.bin_paths = bin_paths

        def get_bin_path(self, name):
            return self.bin_paths[name]

        def run_command(self, command):
            return self.run_command_result[command]

    class VirtualSysctlDetectionMixinMock(VirtualSysctlDetectionMixin):
        def detect_sysctl(self):
            self.sysctl_path = self.module.get_bin_path('sysctl')

    class CheckParameterMock(object):
        def __init__(self, module):
            self.module = module

    # Test with KVM sysctl
    sysctl

# Generated at 2022-06-13 04:25:02.634616
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    class MockBSDVirtualSysctl(VirtualSysctlDetectionMixin):
        def __init__(self):
            self.module = MagicMock()

    bsd = MockBSDVirtualSysctl()
    bsd.module.run_command.return_value = [0, 'XenPVHVM', '']
    facts = bsd.detect_virt_vendor('kern.vm_guest')
    assert facts['virtualization_type'] == 'xen'
    assert facts['virtualization_role'] == 'guest'
    bsd.module.run_command.return_value = [0, 'KVM', '']
    facts = bsd.detect_virt_vendor('kern.vm_guest')
    assert facts['virtualization_type'] == 'kvm'
    assert facts['virtualization_role']

# Generated at 2022-06-13 04:25:13.725651
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    from ansible.module_utils.facts.virt.bsd.sysctl import VirtualSysctlDetectionMixin
    # Dictionary below is a template of results when calling detect_virt_vendor of VirtualSysctlDetectionMixin
    virtual_vendor_facts = {
        'virtualization_type': 'vmm',
        'virtualization_role': 'guest',
        'virtualization_tech_guest': set('vmm'),
        'virtualization_tech_host': set(),
    }
    # Dictionary below is a template of mock_run_command when key is machdep.vmm.vendor
    mock_run_command = {
        'rc': 0,
        'out': 'OpenBSD\n',
        'err': '',
    }
    v = VirtualSysctlDetectionMixin()

# Generated at 2022-06-13 04:25:20.128282
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    from ansible.module_utils.facts.virtual.freebsd import VirtualSysctlDetectionMixin
    v = VirtualSysctlDetectionMixin()
    v.sysctl_path = "/bin/echo"
    v.module = FakeModule()
    assert v.detect_virt_product("hw.model") == {"virtualization_tech_guest": set(), "virtualization_tech_host": set()}



# Generated at 2022-06-13 04:25:31.073186
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    class VirtualSysctlDetectionMixinTest(VirtualSysctlDetectionMixin):
        module = FakeModule()


# Generated at 2022-06-13 04:25:39.266169
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    # Mock module
    class MockModule:
        def get_bin_path(self, key):
            return True
        def run_command(self, command):
            return (0, 'QEMU', '')
    mixin = VirtualSysctlDetectionMixin()
    mixin.module = MockModule()
    # call detect_virt_vendor
    res = mixin.detect_virt_vendor('kern.vm_guest')
    assert res['virtualization_type'] == 'kvm'
    assert res['virtualization_role'] == 'guest'
    # call detect_virt_vendor
    res = mixin.detect_virt_vendor('kern.vm_guest')
    assert res['virtualization_type'] == 'kvm'

# Generated at 2022-06-13 04:25:49.971885
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    class TestModule(object):
        def get_bin_path(self, name):
            return '/bin/sysctl'

        def run_command(self, name):

            if name == 'sysctl -n kern.vm_guest':
                return 0, "OpenBSD", "stderr"
            if name == 'sysctl -n security.jail.jailed':
                return 0, "1", "stderr"
            if name == 'sysctl -n machdep.cpu.brand_string':
                return 0, "Intel(R) Xeon(R) CPU E5-2699 v4 @ 2.20GHz", "stderr"

# Generated at 2022-06-13 04:25:57.618577
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    mixed = VirtualSysctlDetectionMixin()
    mixed.module = AnsibleModule(argument_spec={})

    mixed.module.run_command = MagicMock(return_value=(0, "KVM", None))
    prod_facts = mixed.detect_virt_product("hw.product")
    assert prod_facts['virtualization_type'] == 'kvm'
    assert prod_facts['virtualization_role'] == 'guest'
    assert prod_facts['virtualization_tech_guest'] == set(['kvm'])
    assert prod_facts['virtualization_tech_host'] == set()

    mixed.module.run_command = MagicMock(return_value=(0, "VMware", None))
    prod_facts = mixed.detect_virt_product("hw.product")

# Generated at 2022-06-13 04:26:47.796787
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    class _module(object):
        def get_bin_path(self, path):
            return 'sysctl'

        def run_command(self, cmd):
            rc = 0
            out = ''
            err = ''

            if cmd == 'sysctl -n kern.vm_guest':
                out = 'OpenBSD'
            else:
                rc = 1
            return rc, out, err

    class _facts(object):
        pass

    m = _module()
    f = _facts()
    d = VirtualSysctlDetectionMixin()
    d.module = m
    d.facts = f

    v = d.detect_virt_vendor('kern.vm_guest')
    assert v['virtualization_type'] == 'vmm'
    assert v['virtualization_role'] == 'guest'

# Generated at 2022-06-13 04:26:57.728455
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    from units.mock.sysctl import Sysctl
    from units.compat import mock

    def mock_run_command(module, command):
        if not command.startswith('sysctl --system'):
            return (0, 'QEMU', '')
        return (127, '', '')

    vm = VirtualSysctlDetectionMixin()
    vm.module = mock.MagicMock()
    vm.module.get_bin_path.return_value = '/sbin/sysctl'
    vm.module.run_command = mock_run_command
    vm.sysctl_path = '/sbin/sysctl'

    expected = dict(virtualization_tech_guest='kvm',
                    virtualization_tech_host='',
                    virtualization_type='kvm',
                    virtualization_role='guest')

# Generated at 2022-06-13 04:27:06.542648
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    import mock
    import module_utils

    x = module_utils.VirtualSysctlDetectionMixin()
    x.module = mock.Mock()
    x.module.run_command.return_value = (0, 'KVM', '')

    x.module.get_bin_path.return_value = '/bin/sysctl'

    result = x.detect_virt_product('hw.model')
    assert result['virtualization_role'] == 'guest'
    assert result['virtualization_type'] == 'kvm'


# Generated at 2022-06-13 04:27:16.159534
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    # mock class for FreeBSD FactCollector
    class BSD(object):
        def __init__(self):
            self.sysfs_path = '/sys'
            self.dmesg_path = False
            self.sysctl_path = 'sysctl'

        def get_file_content(self, path):
            # mock get_file_content method
            data = [
                'QEMU',
                'OpenBSD'
            ]
            for line in data:
                if line:
                    return line

    # mock module for AnsibleModule class
    class AnsibleModule(object):
        def __init__(self):
            self.run_command = self.run_command
            self.get_bin_path = self.get_bin_path


# Generated at 2022-06-13 04:27:22.163552
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    from ansible.module_utils.facts.virtual.freebsd import VirtualSysctlDetectionMixin
    class FakeModule:
        def run_command(self, arg, check_rc=True, data=None, binary_data=False):
            return 0, 'KVM', ''

        def get_bin_path(self, arg):
            return '/bin/' + arg

    class FakeClass(VirtualSysctlDetectionMixin):
        def __init__(self):
            self.module = FakeModule()
        def detect_sysctl(self):
            self.sysctl_path = self.module.get_bin_path('sysctl')

    c = FakeClass()
    c.detect_sysctl()
    virtual_product_facts = c.detect_virt_product('hw.model')
    assert virtual_product_facts

# Generated at 2022-06-13 04:27:32.191238
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    # Create test class for use in testing
    class TestVirtualSysctlDetectionMixin(VirtualSysctlDetectionMixin):
        def __init__(self, module):
            self.module = module
            self.sysctl_path = None

    # Create mock module and mock result names
    class TestModule(object):
        def __init__(self):
            self.run_command_data = {}
            self.run_command_data['security.jail.jailed'] = (0, '0', '')
            self.run_command_data['hw.model'] = (0, 'VirtualBox', '')
            self.run_command_data['hw.machine_arch'] = (0, 'amd64', '')
            self.run_command_data['hw.vendor'] = (0, 'i386', '')
           

# Generated at 2022-06-13 04:27:43.142256
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    from ansible.module_utils.facts.virtual.freebsd import VirtualSysctlDetectionMixin

    class FakeModule(object):
        def __init__(self):
            self.exit_json = None
            self.fail_json = None
            self.params = None
            self.run_command = None
            self.get_bin_path = None

    def get_bin_path_mock(name):
        if name == "sysctl":
            return "/usr/bin/sysctl"
        else:
            return None

    fake_module = FakeModule()
    fake_module.exit_json = FakeExitJson()
    fake_module.fail_json = FakeFailJson()
    fake_module.run_command = FakeRunCommand()
    fake_module.get_bin_path = get_bin_path_

# Generated at 2022-06-13 04:27:49.163790
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    class MyVMModule(VirtualSysctlDetectionMixin):
        def __init__(self, bin_path):
            self.bin_paths = {'sysctl': bin_path}
            self.sysctl_path = bin_path
            self.rc = 0
            self.output = ''

        def get_bin_path(self, name):
            if name in self.bin_paths:
                return self.bin_paths[name]
            else:
                return None

        def run_command(self, cmd, check_rc=True):
            return self.rc, self.output, ''

    # Test no output
    myvm = MyVMModule(bin_path='/usr/bin/sysctl')
    myvm.output = ''

# Generated at 2022-06-13 04:27:58.620298
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    mixin = VirtualSysctlDetectionMixin()

    mixin.detect_sysctl = lambda: None
    mixin.module = MagicMock()
    mixin.module.split_args = lambda x: []

    rc = 0
    out = 'KVM'
    err = ''
    mixin.module.run_command.return_value = (rc, out, err)

    key = 'hw.model'
    result = mixin.detect_virt_product(key)
    assert result
    assert 'virtualization_type' in result
    assert result['virtualization_type'] == 'kvm'
    assert 'virtualization_role' in result
    assert result['virtualization_role'] == 'guest'
    assert 'virtualization_tech_guest' in result

# Generated at 2022-06-13 04:28:05.288829
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    # mock module
    class Arg(object):
        def __init__(self):
            self.module = self
        def get_bin_path(self, path):
            return '/sbin/sysctl'

    class RunCommand(object):
        def run_command(self, command):
            code = 0
            out = ''
            err = ''

            if command.startswith('/sbin/sysctl -n kern.vm_guest'):
                out = 'KVM'
            elif command.startswith('/sbin/sysctl -n hw.model'):
                out = 'OpenBSD'
            elif command.startswith('/sbin/sysctl -n hw.product'):
                out = 'VirtualBox'

# Generated at 2022-06-13 04:29:56.410228
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    from ansible.module_utils.facts.virtual import VirtualSysctlDetectionMixin
    class obj(VirtualSysctlDetectionMixin):
        def detect_sysctl(self):
            self.sysctl_path = '/usr/bin/sysctl'
            self.module = obj
            self.module.run_command = run_command

    obj = obj()
    def run_command(command, *args, **kwargs):
        if command == '/usr/bin/sysctl -n security.jail.jailed':
            return 0, '1', ''
        elif command == '/usr/bin/sysctl -n kern.vm_guest':
            return 0, 'HVM', ''
        else:
            return 0, '', ''

    # Test with security.jail.jailed sysctl
    virtual_product_facts

# Generated at 2022-06-13 04:30:02.786510
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    from ansible.module_utils.facts.system.bsd import VirtualSysctlDetectionMixin

    fakedetect = VirtualSysctlDetectionMixin()

    # Successful run when using bhyve
    fakedetect.run_command = lambda *args, **kwargs: (0, 'bhyve', '')
    facts = fakedetect.detect_virt_product('machdep.hypervisor')
    assert facts['virtualization_type'] == 'bhyve'
    assert facts['virtualization_role'] == 'guest'
    assert facts['virtualization_tech_guest'] == set(['bhyve'])
    assert facts['virtualization_tech_host'] == set()

    # Failed run when using jail, should return nothing
    fakedetect.sysctl_path = None
    facts = fakedetect.det

# Generated at 2022-06-13 04:30:12.495782
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    # Note: Not instantiated directly
    class FakeModule:
        def get_bin_path(self, name):
            return '/bin/sysctl'

        def run_command(self, cmd):
            if cmd == '/bin/sysctl -n kern.vm_guest':
                return 0, 'FreeBSD', None
            elif cmd == '/bin/sysctl -n security.jail.jailed':
                return 0, '1', None
            else:
                return 1, '',''
    class FakeClass(VirtualSysctlDetectionMixin): pass
    fake_instance = FakeClass()
    fake_instance.module = FakeModule()

    result = fake_instance.detect_virt_product('kern.vm_guest')
    assert result['virtualization_type'] == 'jails'

# Generated at 2022-06-13 04:30:17.977469
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    mixin = VirtualSysctlDetectionMixin()
    mixin.sysctl_path = "/usr/local/bin/sysctl"
    mixin.module = AnsibleModule(argument_spec=dict())
    virtual_vendor_facts = mixin.detect_virt_vendor("hw.model")
    assert 'virtualization_type' not in virtual_vendor_facts
    assert 'virtualization_role' not in virtual_vendor_facts
    assert 'virtualization_tech_guest' in virtual_vendor_facts
    assert 'virtualization_tech_host' in virtual_vendor_facts


# Generated at 2022-06-13 04:30:27.019926
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    class Args:
        virtual = False
    args = Args()
    mixin = VirtualSysctlDetectionMixin()

    mixin.module = SimpleModule()
    mixin.module.run_command = run_command({'hw.model': 'Some CPU'})

    assert mixin.detect_virt_vendor('hw.model') == {}

    mixin.module.run_command = run_command({'hw.model': 'QEMU Virtual CPU'})
    assert mixin.detect_virt_vendor('hw.model') == {
        'virtualization_type': 'kvm',
        'virtualization_role': 'guest',
        'virtualization_tech_guest': {'kvm'},
        'virtualization_tech_host': set()
    }

    mixin.module.run_command