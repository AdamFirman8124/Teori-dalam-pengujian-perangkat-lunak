

# Generated at 2022-06-13 04:20:36.688357
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    import sys
    import ansible.module_utils.facts.system.freebsd_virtual as fv
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils import basic

    class FakeModule(object):
        def __init__(self, facts):
            self.params = {}
            self.facts = facts

        def get_bin_path(self, executable, required=False, opt_dirs=[]):
            if executable == 'sysctl':
                return '/sbin/sysctl'
            return None

        def run_command(self, command):
            if '-n security.jail.jailed' in command:
                return 0, '1', ''

# Generated at 2022-06-13 04:20:46.095723
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    virtual_vendor_facts = {}

    class FakeModule(object):
        def get_bin_path(self, exe):
            if exe == 'sysctl':
                return '/usr/sbin/sysctl'
            else:
                return None
        def run_command(self, cmd):
            if cmd == '/usr/sbin/sysctl -n hw.model':
                return (0, 'QEMU', '')
            else:
                return (1, None, None)

    class FakeVirtualSysctlDetectionMixin(object):
        def __init__(self):
            self.module = FakeModule()

    v = FakeVirtualSysctlDetectionMixin()
    v.__class__ = VirtualSysctlDetectionMixin

# Generated at 2022-06-13 04:20:54.661677
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    class KGSRule:
        def __init__(self):
            self.sysctl_path = '/sbin/sysctl'
            self.module = self

        def get_bin_path(self, bin_path):
            return self.sysctl_path

        def run_command(self, cmd):
            return (0, 'kvm', None)

    class KVM5Rule:
        def __init__(self):
            self.sysctl_path = '/sbin/sysctl'
            self.module = self

        def get_bin_path(self, bin_path):
            return self.sysctl_path

        def run_command(self, cmd):
            return (0, 'KVM', None)


# Generated at 2022-06-13 04:21:06.702965
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    from ansible.module_utils.facts import VirtualSysctlDetectionMixin
    class AnsibleModule(object):
        def __init__(self, *args, **kwargs):
            self.run_command_environ_update = kwargs['run_command_environ_update']
        def get_bin_path(self, *args, **kwargs):
            return self.run_command_environ_update.get('PATH')
        def run_command(self, *args, **kwargs):
            return(0, 'QEMU', '')
    class VFacts(VirtualSysctlDetectionMixin):
        def __init__(self, module):
            self.module = module
    vf = VFacts(AnsibleModule(run_command_environ_update={}))
    # This is what we

# Generated at 2022-06-13 04:21:16.765516
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    class Module(object):
        def __init__(self):
            self.params = dict()
            self.tmpdir = None

        def get_bin_path(self, filename):
            return filename

        def run_command(self, cmd, check_rc=True, close_fds=True, executable=None,
                        data=None, binary_data=False, path_prefix=None, cwd=None,
                        use_unsafe_shell=False, prompt_regex=None):
            if cmd == 'sysctl -n hw.model':
                return 0, 'OpenBSD', ''
            if cmd == 'sysctl -n security.jail.jailed':
                return 0, '1', ''
            return 0, '', ''

# Generated at 2022-06-13 04:21:27.665894
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    class Module(object):
        class Runs(object):
            class Command(object):
                def __init__(self, rc, out, err):
                    self.rc = rc
                    self.stdout = out
                    self.stderr = err
                def run(self):
                    return [self.rc, self.stdout, self.stderr]
        def __init__(self):
            self.run_command = self.Runs.Command
        @property
        def virtualization_role(self):
            return 'guest'
        @property
        def virtualization_type(self):
            return 'kvm'
        @property
        def virtualization_subtype(self):
            return 'None'
        @property
        def virtualization_role_facts(self):
            return 'None'

# Generated at 2022-06-13 04:21:36.200914
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    module = FakeModule()
    system = FakeSysctl(module)
    system.module = module
    system.detect_sysctl()
    system.sysctl_path = '/sbin/sysctl'
    out = 'hypervisor'
    RC = 0
    expected = {'virtualization_type': 'xen', 'virtualization_role': 'guest'}
    result = system.detect_virt_product(out)
    assert result == expected
    out = 'Hyper-V'
    expected = {'virtualization_type': 'Hyper-V', 'virtualization_role': 'guest'}
    result = system.detect_virt_product(out)
    assert result == expected
    out = 'kvm'

# Generated at 2022-06-13 04:21:48.025348
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    class FakeModule(object):
        def __init__(self):
            self.run_command_calls = 0
            self.run_command_rc = 0
            self.run_command_out = 'OpenBSD'

        def get_bin_path(self, arg):
            return '/sbin/sysctl'

        def run_command(self, cmd):
            self.run_command_calls += 1
            if cmd.startswith('/sbin/sysctl -n hw.product'):
                return (self.run_command_rc, self.run_command_out, '')
            else:
                return (1, '', '')

    module = FakeModule()
    klass = VirtualSysctlDetectionMixin()
    klass.detect_virt_vendor('hw.product')
    assert k

# Generated at 2022-06-13 04:21:55.377201
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    test_obj = VirtualSysctlDetectionMixin()
    test_obj.module = ModuleStub()
    test_obj.sysctl_path = '/sbin/sysctl'
    from ansible_collections.ansible.community.tests.unit.modules.utils import set_module_args
    set_module_args(dict(path='/sbin/sysctl', key='kern.vm_guest'))
    out = test_obj.detect_virt_vendor(key='kern.vm_guest')
    assert 'virtualization_type' in out
    assert out['virtualization_type'] == 'vmm'
    assert out['virtualization_role'] == 'guest'



# Generated at 2022-06-13 04:22:00.931863
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    openbsd_virtual_product_facts = {
        'virtualization_type': 'virtualbox',
        'virtualization_role': 'guest',
        'virtualization_tech_guest': {'kvm', 'virtualbox'},
        'virtualization_tech_host': {}
    }

    openbsd_virtual_product_expected = {
        'virtualization_type': 'virtualbox',
        'virtualization_role': 'guest'
    }

    vmware_virtual_product_facts = {
        'virtualization_type': 'VMware',
        'virtualization_role': 'guest',
        'virtualization_tech_guest': {'kvm', 'VMware'},
        'virtualization_tech_host': {}
    }


# Generated at 2022-06-13 04:22:21.617787
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    module = type('', (), {'get_bin_path': lambda self, path: path,
                           'run_command': lambda self, cmd: (0, 'VirtualBox', '')})
    v = VirtualSysctlDetectionMixin()
    v.module = module
    facts = v.detect_virt_product('machdep.hypervisor')
    assert facts['virtualization_type'] == 'virtualbox'
    module = type('', (), {'get_bin_path': lambda self, path: path,
                           'run_command': lambda self, cmd: (0, 'KVM', '')})
    v.module = module
    facts = v.detect_virt_product('machdep.hypervisor')
    assert facts['virtualization_type'] == 'kvm'

# Generated at 2022-06-13 04:22:28.464036
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
        class FakeModule(object):
            def get_bin_path(self, command):
                return "/usr/sbin/sysctl"

# Generated at 2022-06-13 04:22:40.285866
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    class MockSystemFactsModule:
        def get_bin_path(self, path):
            return '/sbin/sysctl'

        def run_command(self, cmd):
            if (cmd == '/sbin/sysctl -n kern.vm_guest'):
                return (0, 'OpenBSD', None)
            else:
                return (1, '', None)

    mock_module = MockSystemFactsModule()

    class VirtuelSysctlDetectionMixinTester(VirtualSysctlDetectionMixin):
        def __init__(self, module):
            self.module = module
    virtuel_sysctl_detection_mixin = VirtuelSysctlDetectionMixinTester(mock_module)


# Generated at 2022-06-13 04:22:44.846047
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    from ansible.module_utils.facts.virtual.freebsd import VirtualSysctlDetectionMixin

    c = VirtualSysctlDetectionMixin()
    c.detect_virt_vendor("vm.vmtotal")

    assert c.sysctl_path is not None


# Generated at 2022-06-13 04:22:51.644081
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    module = sys.modules[__name__]
    setattr(module, "sysctl_path", "/usr/bin/sysctl")
    setattr(module, "run_command", lambda x: (0, "1", "err"))
    setattr(module, "get_bin_path", lambda x: "/usr/bin/sysctl")
    v = VirtualSysctlDetectionMixin()
    result = v.detect_virt_vendor("hw.model")
    assert result == {'virtualization_tech_guest': set(['kvm']), 'virtualization_tech_host': set([]), 'virtualization_role': 'guest', 'virtualization_type': 'kvm'}

# Generated at 2022-06-13 04:22:53.075786
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    VirtualSysctlDetectionMixin.detect_virt_product('hw.model')

# Generated at 2022-06-13 04:23:02.369030
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    class FreeBSDOS(object):
        pass

    module = FreeBSDOS()
    module.run_command = run_command_mock
    setattr(module, 'get_bin_path', lambda x: '/usr/bin/sysctl')

    #
    # All possible guest virtualization technologies
    #
    module.run_command_environ = {}
    module.run_command_rc = 0
    module.run_command_stdout = 'KVM'
    virtual_facts = VirtualSysctlDetectionMixin().detect_virt_product('hw.product')
    assert virtual_facts['virtualization_type'] == 'kvm'
    assert virtual_facts['virtualization_role'] == 'guest'

    module.run_command_stdout = 'kvm'
    virtual_facts = VirtualSysctlDetectionMixin().detect

# Generated at 2022-06-13 04:23:10.066933
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    import mock
    class obj(VirtualSysctlDetectionMixin):
        module = mock.Mock()

    instance = obj()

    with mock.patch.object(instance.module, 'run_command', return_value=(0, 'XenPV', '')):
        instance.detect_sysctl = mock.MagicMock()
        instance.detect_sysctl.return_value = True

        result = instance.detect_virt_product('hw.model')
        assert result['virtualization_type'] == 'xen'
        assert result['virtualization_role'] == 'guest'
        assert 'virtualization_tech_guest' in result
        assert 'virtualization_tech_host' in result


# Generated at 2022-06-13 04:23:12.871160
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    assert VirtualSysctlDetectionMixin.detect_virt_product(None, 'machdep.hypervisordebug') == \
        {
            'virtualization_type': 'kvm',
            'virtualization_role': 'guest',
            'virtualization_tech_guest': set(['kvm']),
            'virtualization_tech_host': set([])
        }



# Generated at 2022-06-13 04:23:20.642428
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    class MyModule(object):
        def __init__(self):
            self.params = {}

        def get_bin_path(self, arg):
            return '/sbin/sysctl'

        def run_command(self, arg):
            if arg == '/sbin/sysctl -n machdep.cpu.brand_string':
                return 0, 'KVM', ''
            elif arg == '/sbin/sysctl -n machdep.cpu.brand_string':
                return 0, 'KVM', ''
            elif arg == '/sbin/sysctl -n machdep.cpu.brand_string':
                return 0, 'HVM domU', ''
            elif arg == '/sbin/sysctl -n machdep.cpu.brand_string':
                return 0, 'VirtualBox', ''

# Generated at 2022-06-13 04:23:47.417140
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    class VirtualSysctlDetectionMixinFacts(object):
        def __init__(self):
            self.module = MockModule()
    class MockModule(object):
        def run_command(self, command):
            if command == 'sysctl -n kern.vm_guest':
                return 0, 'QEMU', ''
            else:
                return 0, 'OpenBSD', ''
        def get_bin_path(self, name):
            return '/sbin/sysctl'

    virtualfacts = VirtualSysctlDetectionMixinFacts()
    virtualfacts.detect_virt_vendor('kern.vm_guest')
    assert virtualfacts.detect_virt_vendor('kern.vm_guest')['virtualization_type'] == 'kvm'
    assert virtualfacts.detect_virt_vendor

# Generated at 2022-06-13 04:23:53.520614
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    from ansible.module_utils.facts import VirtualSysctlDetectionMixin
    import os
    import sys
    import unittest

    class FakeModule(object):
        def __init__(self):
            self.sysctl_path = None
            self.virt_result = None

        def get_bin_path(self, path):
            if self.sysctl_path:
                return self.sysctl_path
            return "/bin/sysctl"

        def run_command(self, command):
            if self.virt_result:
                return self.virt_result
            return 0, "Generic", ""

    class VirtualSysctlDetectionMixinTestCase(unittest.TestCase):
        def setUp(self):
            self.module = FakeModule()
            self.test_class = VirtualSysctlDetectionMixin()

# Generated at 2022-06-13 04:24:00.128493
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    from ansible.module_utils.facts.bsd.freebsd import VirtualSysctlDetectionMixin
    from unittest.mock import patch

    mock_out = ''
    mock_rc = 0
    mock_err = ''

    class MixinObject():
        module = None
        sysctl_path = None
        pass

    mixin_object = MixinObject()

    virtualization_run_command_mock = patch.object(
        MixinObject, 'run_command',
        return_value=(mock_rc, mock_out, mock_err))
    virtualization_run_command_mock.start()
    with virtualization_run_command_mock:
        expected_result = {'virtualization_tech_guest': set(),
                           'virtualization_tech_host': set()}
        result

# Generated at 2022-06-13 04:24:06.277322
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    from ansible.module_utils import basic
    sdm = VirtualSysctlDetectionMixin()
    sdm.module = basic.AnsibleModule(
        argument_spec = dict(),
    )
    monkeypatch_get_bin_path(sdm)
    monkeypatch_run_command(sdm)
    virtual_product_facts = sdm.detect_virt_product('hw.model')
    assert isinstance(virtual_product_facts, dict)


# Generated at 2022-06-13 04:24:17.050787
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    class MockModule(object):
        def __init__(self):
            self.virtual_vendor = 'QEMU'
            self.rc = 0
            self.sysctl_path = '/sbin/sysctl'

        def run_command(self, *args, **kwargs):
            return (self.rc, self.virtual_vendor, '')

    class AnsibleModule(object):
        def __init__(self):
            self.params = dict()
            self.virtual_vendor = dict()

        def fail_json(self, *args, **kwargs):
            self.exit_args = args
            self.exit_kwargs = kwargs
            raise Exception('fail_json')

        def exit_json(self, *args, **kwargs):
            self.exit_args = args
            self.exit

# Generated at 2022-06-13 04:24:22.627363
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    class TestModule(object):
        def get_bin_path(self, *args):
            return '/sbin/sysctl'
        def run_command(self, *args):
            return 0, 'VirtualBox', ''
    class TestClass(VirtualSysctlDetectionMixin):
        def __init__(self):
            self.module = TestModule()
    test_class = TestClass()
    assert 'virtualbox' in test_class.detect_virt_product('hw.model').get('virtualization_tech_guest')


# Generated at 2022-06-13 04:24:35.389117
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    handler = VirtualSysctlDetectionMixin()
    handler.module = MockModule()
    handler.sysctl_path = "/usr/bin/sysctl"
    handler.module.run_command.return_value = (0, "VirtualBox", "")
    result = handler.detect_virt_product("hw.model")
    assert result['virtualization_type'] == 'virtualbox'
    assert result['virtualization_role'] == 'guest'
    assert "virtualbox" in result['virtualization_tech_guest']

    handler.module.run_command.return_value = (1, "process exited with status 1", "")
    result = handler.detect_virt_product("hw.model")
    assert result['virtualization_role'] == 'guest'
    assert not result.has_key('virtualization_type')


# Generated at 2022-06-13 04:24:38.944311
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    # Test 1
    # virtualization_type = kvm , virtualization_role = guest
    # virtualization_tech_guest = set(['kvm']) , virtualization_tech_host = set()
    class TestClass:
        sysctl_path = "/usr/sbin/sysctl"
        def run_command(command, check_rc=True, close_fds=True, executable=None, data=None, binary_data=False):
            return 0, 'KVM', ''
    virtualization = VirtualSysctlDetectionMixin()
    virtualization.module = TestClass()

# Generated at 2022-06-13 04:24:49.343075
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    keys = ['machdep.cpu.features', 'machdep.hypervisor.vendor', 'machdep.dmi.system-product-name', 'machdep.dmi.product-version', 'machdep.dmi.product-name', 'security.jail.jailed']
    values = ['FPU,VME,DE,PSE,TSC,MSR,PAE,MCE,CX8,APIC,SEP,MTRR,PGE,MCA,CMOV,PAT,PSE36,CLFLUSH,DTS,ACPI,MMX,FXSR,SSE,SSE2,SS,HTT,TM,PBE', 'None', 'VirtualBox', '1.2', 'VirtualBox', '0']


# Generated at 2022-06-13 04:24:59.394405
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    class TestVirtualSysctlDetectionMixin(VirtualSysctlDetectionMixin):
        def detect_sysctl(self):
            self.sysctl_path = '/sbin/sysctl'
            self.sysctl_fail_path = '/sbin/sysctl_fail'

    class TestModule(object):
        def __init__(self, sysctl_path):
            self.sysctl_path = sysctl_path

        def get_bin_path(self, executable):
            if executable == 'sysctl':
                return self.sysctl_path
            else:
                return None

        def run_command(self, command):
            if command == '/sbin/sysctl -n hw.vendor':
                return (0, 'QEMU', '')

# Generated at 2022-06-13 04:25:48.266049
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    class MockModule(object):
        def run_command(self, arg):
            out = "KVM"
            return 0, out, None
        def get_bin_path(self, arg):
            bin_path = "sysctl"
            return bin_path
    class MockVirtualSysctlDetectionMixin(VirtualSysctlDetectionMixin):
        def __init__(self):
            self.module = MockModule()
    a = MockVirtualSysctlDetectionMixin()
    a.detect_virt_product()
    assert a.sysctl_path
    # Should set these values
    assert a.virtualization_type
    assert a.virtualization_role
    # Should be these values
    assert a.virtualization_type == 'kvm'
    assert a.virtualization_role == 'guest'

# Unit test

# Generated at 2022-06-13 04:25:54.708224
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    from ansible.module_utils.facts import VirtualSysctlDetectionMixin
    class TestModule(VirtualSysctlDetectionMixin):
        def __init__(self):
            self.sysctl_path = None
            self.runner = None
    t = TestModule()
    out = t.detect_virt_vendor('machdep.cpu.vendor')
    assert out['virtualization_tech_guest'] == set(['kvm'])
    assert out['virtualization_tech_host'] == set([])
    assert out['virtualization_type'] == 'kvm'
    assert out['virtualization_role'] == 'guest'
    out = t.detect_virt_vendor('hw.vmm.vm_guest')

# Generated at 2022-06-13 04:26:03.980623
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    from ansible.module_utils.facts.system.virtual.freebsd import VirtualSysctlDetectionMixin
    facter_module = VirtualSysctlDetectionMixin()
    facter_module.sysctl_path = '/sbin/sysctl'
    facter_module.module = FakeAnsibleModule()

    # QEMU
    expected_dict = {'virtualization_type': 'kvm', 'virtualization_role': 'guest', 'virtualization_tech_guest': set(['kvm']), 'virtualization_tech_host': set([])}
    actual_dict = facter_module.detect_virt_vendor('hw.product')
    assert actual_dict == expected_dict

    # OpenBSD

# Generated at 2022-06-13 04:26:10.243569
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    test_VirtualSysctlDetectionMixin = VirtualSysctlDetectionMixin()
    test_VirtualSysctlDetectionMixin.detect_sysctl = lambda: "/usr/bin/sysctl"
    test_VirtualSysctlDetectionMixin.module = lambda: "test"
    test_VirtualSysctlDetectionMixin.module.run_command = lambda x: (0, "OpenBSD", "")
    assert test_VirtualSysctlDetectionMixin.detect_virt_vendor("machdep.hypervisor_vendor") == {
        'virtualization_type': 'vmm',
        'virtualization_role': 'guest',
        'virtualization_tech_guest': set(['vmm']),
        'virtualization_tech_host': set()
    }


# Generated at 2022-06-13 04:26:15.037341
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    module = None
    obj = VirtualSysctlDetectionMixin()
    obj.module = module
    obj.sysctl_path = '/sbin/sysctl'

    rc = obj.detect_virt_vendor('vm.get_smp_cpus')
    assert rc == {
        'virtualization_type': 'vmm',
        'virtualization_role': 'guest',
        'virtualization_tech_guest': set(['vmm']),
        'virtualization_tech_host': set()
    }

# Generated at 2022-06-13 04:26:21.792230
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    class Module(object):
        def __init__(self):
            self.params = {'_ansible_version': '2.0.0.0'}

        def get_bin_path(self, name):
            return '/sbin/%s' % name

        def run_command(self, cmd):
            if cmd.startswith('/sbin/sysctl -n kern.vm_guest'):
                return 0, 'OpenBSD', ''
            elif cmd.startswith('/sbin/sysctl -n hw.model'):
                return 0, 'QEMU', ''

    class Facts(object):
        def __init__(self):
            self.os = 'FreeBSD'
            self.data = {}

        def get_data(self):
            return self.data


# Generated at 2022-06-13 04:26:26.777441
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    class TestModule:
        def __init__(self, specs):
            self.specs = specs

        def get_bin_path(self, *args, **kwargs):
            return self.specs.get('sysctl_path', '/sbin/sysctl')

    class TestVirtualSysctlDetectionMixin(VirtualSysctlDetectionMixin):
        def __init__(self, module):
            self.module = module
            self.sysctl_path = None

    try:
        from unittest.mock import Mock
    except ImportError:
        from mock import Mock

    module = TestModule(specs={
        'sysctl_path': '/sbin/sysctl',
        'run_command': {
            'rc': 0,
            'out': '',
            'err': ''
        }
    })



# Generated at 2022-06-13 04:26:36.952053
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    class FakeModule(object):
        def get_bin_path(self, name):
            return '/sbin/sysctl'

        def run_command(self, cmd):
            if "sysctl -n hw.model" == cmd:
                return 0, "QEMU Virtual CPU version 0.9.1", ""
            elif "sysctl -n machdep.cpu.vendor" == cmd:
                return 0, "GenuineIntel", ""
            elif "sysctl -n security.jail.jailed" == cmd:
                return 0, "1", ""
            elif "sysctl -n hw.machine" == cmd:
                return 0, "i386", ""
            elif "sysctl -n security.jail.jailed" == cmd:
                return 0, "1", ""

# Generated at 2022-06-13 04:26:41.127808
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    assert set(VirtualSysctlDetectionMixin().detect_virt_vendor('machdep.xen.guest_vendor')) == set({'virtualization_role': 'guest',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set(),
        'virtualization_type': 'kvm'})

# Generated at 2022-06-13 04:26:48.278029
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    class VirtualSysctlDetectionMixinModule:
        def get_bin_path(self, arg):
            return "/sbin/sysctl"

        def run_command(self, arg):
            return rc, out, err

    class VirtualSysctlDetectionMixinAnsibleModule:
        def __init__(self):
            self.params = {}
            self.virtual = None
            self.fail_json = False

    class VirtualSysctlDetectionMixinSysctl:
        def __init__(self, module, key):
            self.out=None
            self.err=None
            self.rc=None

    class VirtualSysctlDetectionMixinKernel:
        def __init__(self, module):
            self.kernel = None
            self.family = None
            self.arch = None
            self.machine = None

# Generated at 2022-06-13 04:28:14.402933
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    class FakeModule(object):
        def run_command(self, cmd):
            return 0, 'QEMU', ''

        def get_bin_path(self, binary):
            return '/usr/bin/sysctl'

    class FakeOSDetect(object):
        def __init__(self):
            self.module = FakeModule()
            self.sysctl_path = None

    detect = FakeOSDetect()
    result = detect.detect_virt_vendor('kern.vm_guest')
    assert result['virtualization_type'] == 'kvm'
    assert result['virtualization_role'] == 'guest'
    assert result['virtualization_tech_guest'] == {'kvm'}
    assert result['virtualization_tech_host'] == set()


# Generated at 2022-06-13 04:28:18.495536
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    obj = VirtualSysctlDetectionMixin()
    obj.module = MockModule()
    obj.module.run_command.return_value = (0, 'QEMU', '')
    expected_result = {'virtualization_tech_guest': {'kvm'}, 'virtualization_type': 'kvm', 'virtualization_tech_host': set(), 'virtualization_role': 'guest'}
    result = obj.detect_virt_vendor('machdep.dmi.system-vendor')
    assert result == expected_result


# Generated at 2022-06-13 04:28:28.782859
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    from ansible.module_utils.facts.virt.freebsd import VirtualSysctlDetectionMixin

    class MockModule(object):
        def __init__(self, module_name, module_args, bin_path='/bin/'):
            self.bin_path_cache = {}
            self.module_name = module_name
            self.module_args = module_args
            self.params = {}
            self.fail_json = lambda self, msg: msg
            self.run_command = lambda cmd, path=None, check_rc=True: (0, 'KVM', '')

        def get_bin_path(self, arg):
            if arg in self.bin_path_cache:
                return self.bin_path_cache[arg]

            # Return a path assuming we are in a FreeBSD jail.

# Generated at 2022-06-13 04:28:36.216363
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    from mock import MagicMock
    mod = MagicMock()
    mod.run_command.return_value = 1, '', ''

    sysctl_path = '/sbin/sysctl'
    mod.get_bin_path.return_value = sysctl_path

    klass = VirtualSysctlDetectionMixin()
    klass.module = mod

    klass.detect_virt_vendor('hw.model')
    cmd = "%s -n %s" % (sysctl_path, 'hw.model')
    mod.run_command.assert_called_with(cmd)
    mod.get_bin_path.assert_called_with('sysctl')


# Generated at 2022-06-13 04:28:45.365701
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    import sys
    import os
    import tempfile
    sys.path.append(os.path.join(os.path.dirname(__file__), '../lib'))
    from module_utils.facts.virtual.freebsd import VirtualSysctlDetectionMixin
    from ansible.module_utils.facts.virtual.freebsd import PlatformVirtualSysctlDetection
    from ansible.module_utils.facts.virtual.freebsd import Virtual

    v = Virtual()
    virtual_facts = dict()
    virtual_facts['virtualization_type'] = None
    virtual_facts['virtualization_role'] = None
    virtual_facts['virtualization_tech_host'] = None
    virtual_facts['virtualization_tech_guest'] = None

    v.get_virtual_facts(virtual_facts)
    virtual_facts = v

# Generated at 2022-06-13 04:28:55.662732
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    import sys
    import os
    import mock
    from units.compat import b

    sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
    from lib.ansible.module_utils.facts import VirtualSysctlDetectionMixin
    module = Mock(module_utils.facts, AnsibleModule=Mock(return_value=Mock(module)))
    module.run_command = Mock(return_value=(0, b('QEMU'), b('')))
    module.get_bin_path = Mock(return_value='/usr/bin/sysctl')
    virtual = VirtualSysctlDetectionMixin(module)
    virtual.detect_virt_vendor(key='hw.model')

# Generated at 2022-06-13 04:29:03.951720
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    from ansible.module_utils.facts.virtual.openbsd.util import VirtualSysctlDetectionMixin
    bsd = VirtualSysctlDetectionMixin()
    #Set sysctl command output
    class o():
        @staticmethod
        def run_command(cmd):
            return 0, "OpenBSD", ""
    bsd.module = o
    bsd.detect_virt_vendor('machdep.cpu_vendor')
    assert bsd.module.run_command.called
    assert bsd.module.run_command.call_args[0][0] == 'sysctl -n machdep.cpu_vendor'


# Generated at 2022-06-13 04:29:13.967924
# Unit test for method detect_virt_vendor of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_vendor():
    from ansible.utils.virtualsysctl import VirtualSysctlDetectionMixin
    from ansible.module_utils.six import with_metaclass
    from ansible.module_utils._text import to_native

    class FakeVirtualSysctlDetectionMixin(with_metaclass(VirtualSysctlDetectionMixin, object)):
        """ Compat class to provide a fake object to run methods against """
        module = None
        sysctl_path = None

        def __init__(self, module):
            self.module = module

    class FakeAnsibleModule(object):
        """ Helper class to provide a fake AnsibleModule object to run tests. """

        def __init__(self):
            self.rc = None
            self.cmd_result = {}
            self._output = None
            self._debug = None


# Generated at 2022-06-13 04:29:20.237900
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    test_class = VirtualSysctlDetectionMixin()
    test_class.sysctl_path = True
    params = []
    params.append(('security.jail.jailed', None))
    params.append(('hw.model', 'KVM'))
    params.append(('hw.model', 'kvm'))
    params.append(('hw.model', 'Bochs'))
    params.append(('hw.model', 'SmartDC'))
    params.append(('hw.model', 'HVM domU'))
    params.append(('hw.model', 'XenPVH'))
    params.append(('hw.model', 'XenPV'))
    params.append(('hw.model', 'XenPVHVM'))

# Generated at 2022-06-13 04:29:29.728768
# Unit test for method detect_virt_product of class VirtualSysctlDetectionMixin
def test_VirtualSysctlDetectionMixin_detect_virt_product():
    virt_product_list = ['QEMU', 'KVM', 'VMWARE', 'VirtualBox', 'HVM domU', 'XenPV', 'XenPVHVM', 'XenPVH', 'Hyper-V', 'Parallels', 'RHEV Hypervisor']
    virtual_product_facts = {}
    key = 'hw.product'
    obj = VirtualSysctlDetectionMixin()
    obj.sysctl_path = 'sysctl'
    obj.module = FakeAnsibleModule()
    for virt_product in virt_product_list:
        obj.module.run_command = FakeRunCommand(virt_product)
        virtual_product_facts = obj.detect_virt_product(key)
        assert virtual_product_facts['virtualization_type'] == virt_product.lower()
        assert virtual