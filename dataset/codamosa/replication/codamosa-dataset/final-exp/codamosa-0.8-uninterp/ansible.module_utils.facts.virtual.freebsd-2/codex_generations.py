

# Generated at 2022-06-13 03:43:53.442967
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virt = FreeBSDVirtualCollector(None)
    assert isinstance(virt, VirtualCollector)
    assert isinstance(virt, FreeBSDVirtualCollector)

# Generated at 2022-06-13 03:43:59.662379
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    fbsd_virt = FreeBSDVirtual()
    # We read the virtual facts from the platform
    virtual_facts = fbsd_virt.get_virtual_facts()
    # We check the result
    assert isinstance(virtual_facts, dict)
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts



# Generated at 2022-06-13 03:44:01.165290
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert FreeBSDVirtualCollector()._platform == 'FreeBSD'
    assert FreeBSDVirtualCollector()._fact_class.platform == 'FreeBSD'

# Generated at 2022-06-13 03:44:07.138824
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    o = FreeBSDVirtual()
    o._module.exit_json = lambda **kwargs: kwargs
    o._get_sysctl = lambda *a: {'kern.vm_guest': 'domU'}
    o._get_dmesg = lambda *a: None
    o._get_smbios = lambda *a: None

    assert o.get_virtual_facts() == {'virtualization_type': 'xen', 'virtualization_role': 'guest'}

# Generated at 2022-06-13 03:44:10.556387
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():

    obj = FreeBSDVirtualCollector()
    assert obj.platform == 'FreeBSD'
    assert obj._fact_class == FreeBSDVirtual



# Generated at 2022-06-13 03:44:12.539098
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_collector = FreeBSDVirtualCollector()
    assert(isinstance(virtual_collector, FreeBSDVirtualCollector))


# Generated at 2022-06-13 03:44:14.973526
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fv = FreeBSDVirtualCollector()
    assert isinstance(fv, FreeBSDVirtualCollector)
    assert isinstance(fv.get_virtual_facts(), FreeBSDVirtual)

# Generated at 2022-06-13 03:44:17.494698
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    frbsdc = FreeBSDVirtualCollector()
    assert frbsdc.platform == 'FreeBSD'
    assert frbsdc._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:44:18.071924
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:44:19.033094
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert 'FreeBSD' == FreeBSDVirtualCollector._platform

# Generated at 2022-06-13 03:44:26.950043
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_collector = FreeBSDVirtualCollector()
    assert virtual_collector._platform == 'FreeBSD'
    assert virtual_collector._fact_class == FreeBSDVirtual
    assert virtual_collector.platform == 'FreeBSD'
    assert virtual_collector.fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:44:29.876989
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fs_ob = FreeBSDVirtualCollector()
    ob = fs_ob._fact_class
    print(ob)
    print(ob.platform)

# Test fetching virtualization facts

# Generated at 2022-06-13 03:44:40.240215
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():

    facts = {
        'virtualization_tech_host': set(),
        'virtualization_tech_guest': set(),
        'virtualization_type': '',
        'virtualization_role': '',
    }

    def exec_module(module):
        val = ''
        if module.params['abi_return'] == 'freebsd':
            val = True
        elif module.params['abi_return'] == 'openbsd':
            val = False
        return {
            'ansible_facts': {
                'platform_abi': {
                    'freebsd': val,
                    'openbsd': not val,
                }
            },
            'changed': False
        }

    class ModuleMock(object):
        params = {
            'abi_return': 'freebsd'
        }


# Generated at 2022-06-13 03:44:42.097750
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fc = FreeBSDVirtualCollector()
    assert isinstance(fc, FreeBSDVirtualCollector)


# Generated at 2022-06-13 03:44:44.840406
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    # Create instance of FreeBSDVirtualCollector class.
    obj = FreeBSDVirtualCollector()
    assert obj._platform == 'FreeBSD'
    assert obj._fact_class.__name__ == 'FreeBSDVirtual'

# Generated at 2022-06-13 03:44:46.591015
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virt_facts_obj = FreeBSDVirtual()
    facts = virt_facts_obj.get_virtual_facts()
    assert facts['virtualization_type'] in ('', 'xen', 'kvm', 'vmware', 'jail')
    assert facts['virtualization_role'] in ('', 'guest', 'host', 'guest,host')

# Generated at 2022-06-13 03:44:47.664610
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:44:48.590909
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert FreeBSDVirtualCollector is not None

# Generated at 2022-06-13 03:44:50.177768
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    x = FreeBSDVirtualCollector()
    assert x.platform == 'FreeBSD'
    assert x._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:44:57.843633
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    """Unit test for method get_virtual_facts of class FreeBSDVirtual."""
    # Test case for non-virtual FreeBSD OS
    virtual = FreeBSDVirtual()
    virtual_facts = virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''
    assert 'xen' not in virtual_facts['virtualization_tech_guest']
    assert 'xen' not in virtual_facts['virtualization_tech_host']



# Generated at 2022-06-13 03:45:17.700010
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    from ansible_collections.ansible.community.tests.unit.compat import mock

    # Create a FreeBSDVirtual object for testing
    test_virt = FreeBSDVirtual()

    # Mock 'os.path.exists', always return False
    with mock.patch('os.path.exists') as m_exists:
        m_exists.return_value = False
        facts = test_virt.get_virtual_facts()
        assert facts['virtualization_type'] == ''
        assert facts['virtualization_role'] == ''

        assert facts['virtualization_tech_guest'] == set()
        assert facts['virtualization_tech_host'] == set()

    # Mock 'os.path.exists', always return True

# Generated at 2022-06-13 03:45:21.119001
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    """Unit test for constructor of class FreeBSDVirtualCollector"""
    def tst_FreeBSDVirtualCollector():
        """Unit inner test for constructor of class FreeBSDVirtualCollector"""
        _ = FreeBSDVirtualCollector()
    tst_FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:45:28.423323
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    import os
    import sys
    sys.modules['os'] = os

    class MockFreeBSDVirtual(FreeBSDVirtual):
        def __init__(self, module_manager):
            self.virtualization_type = 'noop'
            self.virtualization_role = 'noop'

        def detect_virt_product(self, sysctl_name):
            self.sysctl_name = sysctl_name
            return {
                'virtualization_type': 'the_virtualization_type',
                'virtualization_role': 'the_virtualization_role',
                'virtualization_tech_guest': set(),
                'virtualization_tech_host': set()
            }

        def detect_virt_vendor(self, hardware_model):
            self.hardware_model = hardware_model

# Generated at 2022-06-13 03:45:30.769727
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fbc = FreeBSDVirtualCollector()
    assert type(fbc) == FreeBSDVirtualCollector
    assert fbc.__class__.__name__ == 'FreeBSDVirtualCollector'

# Generated at 2022-06-13 03:45:37.853497
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    class FreeBSDVirtualMocked(FreeBSDVirtual):
        def __init__(self, sysfs_path='', sysctl_virtual='',
                     sysctl_machine='', vendor_info=None, sysctl=None):
            self.sysctl_virtual = sysctl_virtual
            self.sysctl_machine = sysctl_machine
            self.vendor_info = vendor_info
            self.sysctl = sysctl
            self.sysfs_path = sysfs_path

        def detect_virt_product(self, sysctl_virtual):
            if self.sysctl_virtual != '':
                res = self.sysctl.get(sysctl_virtual)
                res = {'virtualization_tech_host': [res], 'virtualization_tech_guest': [res]}

# Generated at 2022-06-13 03:45:41.635155
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    collectors = [c for c in VirtualCollector.__subclasses__()
                  if c._platform == 'FreeBSD']

    assert len(collectors) > 0
    assert isinstance(collectors[0], FreeBSDVirtualCollector)

# Generated at 2022-06-13 03:45:51.391157
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    """
    Return virtual facts on FreeBSD.
    """
    # Set up text fixtures
    # kern.vm_guest = 'none', hw.hv_vendor = 'N/A', security.jail.jailed = 0
    # hw.model = "Intel(R) Xeon(R) CPU E5-2680 v2 @ 2.80GHz"
    # We expect this to return 'virtualization_type': '',
    # 'virtualization_role': ''
    # 'virtualization_tech_guest': set(), 'virtualization_tech_host': set()
    kern_vm_guest = {'virtualization_type': '', 'kern.vm_guest': 'none'}
    hw_hv_vendor = None

# Generated at 2022-06-13 03:45:55.218534
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual = FreeBSDVirtual()
    assert virtual.get_virtual_facts() == {
        'virtualization_type': 'xen',
        'virtualization_role': 'guest',
        'virtualization_subtype': '',
        'virtualization_tech_guest': set(['xen']),
        'virtualization_tech_host': set()
    }

# Generated at 2022-06-13 03:46:00.743880
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():  # pylint: disable=invalid-name
    from ansible.module_utils.facts.virtual.freebsd import FreeBSDVirtual
    freebsd_virtual_facts = FreeBSDVirtual()
    freebsd_virtual_facts.get_virtual_facts()


if __name__ == '__main__':
    test_FreeBSDVirtual_get_virtual_facts()

# Generated at 2022-06-13 03:46:05.779396
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # Setup
    fb = FreeBSDVirtual()

    # Test
    facts = fb.get_virtual_facts()

    # Assertions
    assert 'virtualization_type' in facts
    assert 'virtualization_role' in facts


if __name__ == '__main__':
    test_FreeBSDVirtual_get_virtual_facts()

# Generated at 2022-06-13 03:46:29.471322
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert FreeBSDVirtualCollector

# Generated at 2022-06-13 03:46:30.541162
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    VirtualCollector.collect(FreeBSDVirtualCollector, 'freebsd')

# Generated at 2022-06-13 03:46:32.450363
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_collector = FreeBSDVirtualCollector()
    assert virtual_collector.platform == 'FreeBSD'
    assert virtual_collector._fact_class == FreeBSDVirtual


# Generated at 2022-06-13 03:46:35.864481
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    freebsd_virtual_collector = FreeBSDVirtualCollector()
    assert freebsd_virtual_collector is not None

# Unit tests for constructor of class FreeBSDVirtual

# Generated at 2022-06-13 03:46:46.020473
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual = FreeBSDVirtual()

    # Basic facts
    virtual.sysctl_mock = {
        'kern.vm_guest': 'none',
        'hw.hv_vendor': 'None',
        'hw.model': 'VirtualBox',
        'security.jail.jailed': '0'
    }
    expected_facts = {
        # virtualization_type is VirtualBox
        'virtualization_type': 'VirtualBox',
        # virtualization_role is guest
        'virtualization_role': 'guest',
        # virtualization_tech_host is an empty set
        'virtualization_tech_host': set(),
        # virtualization_tech_guest is a set of {'VirtualBox'}
        'virtualization_tech_guest': set(['VirtualBox'])
    }
    facts = virtual

# Generated at 2022-06-13 03:46:48.018865
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    collector = FreeBSDVirtualCollector()
    assert collector.platform == 'FreeBSD'

# Generated at 2022-06-13 03:46:49.884468
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert FreeBSDVirtualCollector._fact_class.platform == 'FreeBSD'

# Generated at 2022-06-13 03:46:57.014760
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    module_name = 'ansible_test_get_virtual_facts'
    facts_module = __import__(module_name)
    virtual_facts = facts_module.Facts()

    # FreeBSD
    expected = {
        'virtualization_type': 'xen',
        'virtualization_role': 'guest',
        'virtualization_tech_guest': {'xen'},
        'virtualization_tech_host': set(),
    }
    if virtual_facts.get_virtual_facts() != expected:
        raise AssertionError('returned incorrect virtual facts')

# Generated at 2022-06-13 03:47:03.479463
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    # Create a FreeBSDVirtualCollector object
    freebsd_virtual = FreeBSDVirtualCollector()
    # Check if it is an instance of FreeBSDVirtualCollector
    assert isinstance(freebsd_virtual, FreeBSDVirtualCollector)
    # Check if it is an instance of VirtualCollector
    assert isinstance(freebsd_virtual, VirtualCollector)
    # Check if FreeBSDVirtualCollector.platform is 'FreeBSD'
    assert freebsd_virtual._platform == 'FreeBSD'
    # Check if the platform of FreebsdVirtualCollector is 'FreeBSD'
    assert freebsd_virtual.platform == 'FreeBSD'

# Generated at 2022-06-13 03:47:06.799209
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    facts_dict = FreeBSDVirtualCollector({}, {}).collect()
    assert isinstance(facts_dict, dict)
    assert isinstance(facts_dict['virtual'], dict)
    assert isinstance(facts_dict['virtual']['guest_tech'], set)

# Generated at 2022-06-13 03:47:58.406463
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    x = FreeBSDVirtualCollector()
    assert isinstance(x, FreeBSDVirtualCollector)

# Generated at 2022-06-13 03:48:04.687539
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    # Create an instance of FreeBSDVirtualCollector class.
    # This is done by module_utils/facts/virtual/collector.py
    # when module_utils/facts/virtual/__init__.py loads modules
    # in directory module_utils/facts/virtual/
    # FreeBSDVirtualCollector() is called.
    virtual_collector = FreeBSDVirtualCollector()
    # get_facts() is called when module_utils/facts/virtual/__init__.py
    # loads the virtual_facts plugin
    virtual_facts = virtual_collector.get_facts()
    # general cases
    assert virtual_facts['virtualization_type'] in ['', 'xen']
    assert virtual_facts['virtualization_role'] in ['', 'guest']
    # kern.vm_guest cases

# Generated at 2022-06-13 03:48:15.951080
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # Fake module, to be used at will
    class TestAnsibleModule(object):
        # Fake module input args
        params = {
            'gather_subset': ['virtual'],
            'gather_timeout': 10,
        }

    # Fake module, to be used at will
    class AnsibleModuleFake:
        def __init__(self, *args, **kwargs):
            self.params = kwargs.get('params')
            self.exit_json = kwargs.get('exit_json')

        def fail_json(self, *args, **kwargs):
            self.exit_json = kwargs['msg']
            return 0

    # Mocked functions to be used at will

# Generated at 2022-06-13 03:48:18.004058
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    """ Check test_FreeBSDVirtualCollector constructor """
    collector = FreeBSDVirtualCollector('/proc', '/sys', '/dev/xen')
    assert collector._root_dir == '/'

# Generated at 2022-06-13 03:48:19.002010
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    f = FreeBSDVirtualCollector()
    assert type(f) is FreeBSDVirtualCollector

# Generated at 2022-06-13 03:48:22.702200
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual_facts = FreeBSDVirtual().get_virtual_facts()
    facts_keys = [
        'virtualization_type', 'virtualization_role',
        'virtualization_tech_guest', 'virtualization_tech_host'
    ]

    for k in facts_keys:
        assert k in virtual_facts

# Generated at 2022-06-13 03:48:23.116469
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:48:25.584830
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
        os_platform = 'FreeBSD'
        collector = FreeBSDVirtualCollector(os_platform)
        assert collector._platform == os_platform
        assert collector._fact_class.platform == os_platform

# Generated at 2022-06-13 03:48:27.800702
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert FreeBSDVirtualCollector._platform == 'FreeBSD'
    assert FreeBSDVirtualCollector._fact_class == FreeBSDVirtual


# Generated at 2022-06-13 03:48:37.273737
# Unit test for method get_virtual_facts of class FreeBSDVirtual

# Generated at 2022-06-13 03:49:41.737717
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    # noinspection PyStatementEffect
    FreeBSDVirtualCollector

# Generated at 2022-06-13 03:49:44.342698
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    facts = FreeBSDVirtualCollector().collect(None, None)
    assert facts['ansible_virtualization_type'] == 'FreeBSD'

# Generated at 2022-06-13 03:49:54.359497
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    """
    Returns a dictionary of virtual facts for FreeBSD.
    This method is called by the Virtual subclass when
    populating fact_subset in collect().
    """
    # Suppress deprecation warning from calling VirtualCollector.collect()
    # (only seen when running tests from inside Ansible source code)
    import warnings
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=DeprecationWarning)
        fbsd_virtual_collector = FreeBSDVirtualCollector()
        fbsd_virtual_collector.collect()

# Generated at 2022-06-13 03:49:58.811085
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual_facts = FreeBSDVirtual().get_virtual_facts()
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts
    assert isinstance(virtual_facts['virtualization_tech_guest'], set)
    assert isinstance(virtual_facts['virtualization_tech_host'], set)

# Generated at 2022-06-13 03:50:00.306477
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    collector = FreeBSDVirtualCollector()
    assert collector._fact_class == FreeBSDVirtual
    assert collector._platform == 'FreeBSD'


# Generated at 2022-06-13 03:50:00.818016
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:50:03.353459
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    freebsd_virtual_collector = FreeBSDVirtualCollector()
    assert freebsd_virtual_collector._platform == 'FreeBSD'
    assert freebsd_virtual_collector._fact_class.platform == 'FreeBSD'

# Generated at 2022-06-13 03:50:04.463402
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert isinstance(FreeBSDVirtualCollector(), VirtualCollector)

# Generated at 2022-06-13 03:50:08.451772
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual = FreeBSDVirtual()
    virtual_facts = virtual.get_virtual_facts()

    assert virtual_facts['virtualization_role'] in ['guest', 'host', '']
    assert virtual_facts['virtualization_type'] in ['xen', 'jail', '', 'linux']

# Generated at 2022-06-13 03:50:10.707967
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fv = FreeBSDVirtualCollector()
    assert(isinstance(fv, FreeBSDVirtualCollector))

# Generated at 2022-06-13 03:52:37.442246
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    from ansible.module_utils.facts.virtual.freebsd import FreeBSDVirtualCollector
    from ansible.module_utils.facts.virtual import Virtual
    from ansible.module_utils.facts.virtual.sysctl import VirtualSysctlDetectionMixin
    if not issubclass(FreeBSDVirtualCollector._fact_class, Virtual):
        raise AssertionError()
    if not issubclass(FreeBSDVirtualCollector._fact_class, VirtualSysctlDetectionMixin):
        raise AssertionError()

if __name__ == '__main__':
    test_FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:52:40.788966
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual_facts = FreeBSDVirtual({}).get_virtual_facts()
    assert isinstance(virtual_facts, dict)
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts

# Generated at 2022-06-13 03:52:43.758619
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fake_os_uname = namedtuple('fake_os_uname', ['sysname'])
    fake_os_uname_value = fake_os_uname(sysname='FreeBSD')
    collector = FreeBSDVirtualCollector(fake_os_uname_value, {})
    assert isinstance(collector, FreeBSDVirtualCollector)

# Generated at 2022-06-13 03:52:48.327910
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # Empty dict.
    _sysctl_test_vars = {
        'kern.vm_guest': '',
        'hw.hv_vendor': '',
        'security.jail.jailed': '',
        'hw.model': '',
    }
    _sysctl_test = {
        'FreeBSD': {
            'sysctl': _sysctl_test_vars
        }
    }
    _hardware_test = {
        'FreeBSD': {
            'hardware': 'i386'
        }
    }
    _custom_facts_test = {
        'FreeBSD': {
            'custom_facts': {}
        }
    }

    import pytest
    from ansible.module_utils.facts import Collector

# Generated at 2022-06-13 03:52:49.948618
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert isinstance(FreeBSDVirtualCollector('hw.model'),
                      FreeBSDVirtualCollector)

# Generated at 2022-06-13 03:52:56.495216
# Unit test for method get_virtual_facts of class FreeBSDVirtual

# Generated at 2022-06-13 03:52:57.455195
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    freebsd_virtual = FreeBSDVirtualCollector()
    assert isinstance(freebsd_virtual, FreeBSDVirtualCollector)

# Generated at 2022-06-13 03:53:06.013792
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    sys1 = {'kern.vm_guest': 'vmware', 'hw.hv_vendor': 'Bhyve',
            'security.jail.jailed': '1'}
    sys2 = {'kern.vm_guest': 'vmware', 'hw.hv_vendor': 'Bhyve',
            'security.jail.jailed': '0'}
    sys3 = {'kern.vm_guest': 'other', 'hw.hv_vendor': 'Bhyve',
            'security.jail.jailed': '0'}
    sys4 = {'kern.vm_guest': '', 'hw.hv_vendor': 'Bhyve',
            'security.jail.jailed': '0'}

# Generated at 2022-06-13 03:53:07.991015
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    facts = dict()
    VirtualCollector(facts, FreeBSDVirtualCollector._platform)
    assert facts['virtualization_type'] == 'xen'
    assert facts['virtualization_role'] == 'guest'

# Generated at 2022-06-13 03:53:16.935896
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    current = os.path.dirname(os.path.abspath(__file__))
    sysctl_pairs = [
        ('security.jail.jailed=0', ''),
        ('security.jail.jailed=1', 'jail'),
    ]

    for sysctl in sysctl_pairs:
        path = current + os.sep + sysctl[0]
        f = open(path, 'w')
        f.close()
        virtual_facts = FreeBSDVirtual().get_virtual_facts()
        if sysctl[1] == '':
            assert virtual_facts['virtualization_type'] == ''
            assert virtual_facts['virtualization_role'] == ''
            assert virtual_facts['virtualization_tech_guest'] == set()
            assert virtual_facts['virtualization_tech_host'] == set