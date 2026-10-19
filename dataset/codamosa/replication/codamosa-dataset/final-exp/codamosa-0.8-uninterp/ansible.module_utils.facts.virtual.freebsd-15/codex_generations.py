

# Generated at 2022-06-13 03:43:50.622695
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    f = FreeBSDVirtualCollector()
    assert f is not None

# Generated at 2022-06-13 03:43:54.272119
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    v = FreeBSDVirtual()
    facts = v.get_virtual_facts()

    assert facts['virtualization_role'] == ''
    assert facts['virtualization_type'] == ''

# Generated at 2022-06-13 03:43:58.833845
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    expected_facts = {
        "virtualization_type": "xen",
        "virtualization_role": "guest",
        "virtualization_tech_host": set(),
        "virtualization_tech_guest": set(['xen'])
    }
    facts = FreeBSDVirtual(None).get_virtual_facts()
    assert facts == expected_facts

# Generated at 2022-06-13 03:44:07.710502
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    guest_tech = set()
    host_tech = set()
    expected_virtual_facts = {'virtualization_type': '',
                              'virtualization_role': '',
                              'virtualization_tech_guest': guest_tech,
                              'virtualization_tech_host': host_tech}
    class FreeBSDVirtualMock(FreeBSDVirtual):
        def __init__(self):
            # Override the superclass constructor
            pass

        def detect_virt_product(self, sysctl_name):
            # Mock detect_virt_product so we can test get_virtual_facts
            # unconditionally
            return {'virtualization_type': '', 'virtualization_role': ''}

# Generated at 2022-06-13 03:44:10.724306
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert FreeBSDVirtualCollector().platform is 'FreeBSD'
    assert FreeBSDVirtualCollector()._fact_class is FreeBSDVirtual

# Generated at 2022-06-13 03:44:13.182990
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
        virtual_collector = FreeBSDVirtualCollector()
        assert virtual_collector.platform == 'FreeBSD'
        assert virtual_collector.fact_class.platform == 'FreeBSD'

# Generated at 2022-06-13 03:44:15.477530
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual = FreeBSDVirtualCollector(module=None)
    assert virtual._platform == 'FreeBSD'
    assert virtual._fact_class == FreeBSDVirtual


# Generated at 2022-06-13 03:44:25.585183
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    import pytest


# Generated at 2022-06-13 03:44:28.030562
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    collector = FreeBSDVirtualCollector()
    assert collector.platform == 'FreeBSD'
    assert collector.fact_class.platform == 'FreeBSD'

# Generated at 2022-06-13 03:44:30.953586
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    freebsd_virtual_collector = FreeBSDVirtualCollector()
    assert freebsd_virtual_collector.platform == 'FreeBSD'
    assert freebsd_virtual_collector._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:44:37.258197
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    from ansible.module_utils.facts.virtual.freebsd import FreeBSDVirtualCollector
    FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:44:41.950381
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fbc = FreeBSDVirtualCollector()
    assert fbc.platform == 'FreeBSD'
    assert fbc._fact_class.platform == 'FreeBSD'
    assert issubclass(fbc._fact_class, Virtual) is True
    assert issubclass(fbc._fact_class, VirtualSysctlDetectionMixin) is True


# Generated at 2022-06-13 03:44:49.488933
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # Test case facts
    kern_vm_guest = 'vmware'
    hw_hv_vendor = 'vmware'
    sec_jail_jailed = '0'
    hw_model = 'VirtualBox'

    # Create class object and mocks.
    module = type('Module', (object,), {})()
    module.get_bin_path = lambda x: ''
    module.run_command = lambda args, check_rc=None: (0, '', '')
    module.exit_json = lambda **kwargs: None
    module.fail_json = lambda **kwargs: None

    # Mock sysctl_present method.
    mocked_sysctl = type('Module', (object,), {})()

# Generated at 2022-06-13 03:44:50.050871
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:44:55.932747
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual_facts = FreeBSDVirtual.get_virtual_facts()
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts

# Generated at 2022-06-13 03:44:58.280735
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    freebsd_virtual = FreeBSDVirtual({})
    freebsd_virtual.get_virtual_facts()

# Generated at 2022-06-13 03:45:01.682548
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    bv = FreeBSDVirtualCollector()
    assert isinstance(bv, FreeBSDVirtualCollector)
    assert bv._fact_class is FreeBSDVirtual
    assert bv._platform == 'FreeBSD'


# Generated at 2022-06-13 03:45:03.219105
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fv = FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:45:13.850975
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual_facts = FreeBSDVirtual({}).get_virtual_facts()

    # Test a FreeBSD host in a jail
    assert virtual_facts['virtualization_role'] == 'guest'
    assert virtual_facts['virtualization_type'] == 'jail'
    assert virtual_facts['virtualization_tech_guest'] == set(['jail'])
    assert virtual_facts['virtualization_tech_host'] == set()

    # Test a FreeBSD host on bhyve
    virtual_facts = FreeBSDVirtual({'ansible_product_name': 'QEMU Standard PC (i440FX + PIIX, 1996)'}).get_virtual_facts()
    assert virtual_facts['virtualization_role'] == 'host'
    assert virtual_facts['virtualization_type'] == 'emulated'

# Generated at 2022-06-13 03:45:17.647666
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    freebsd_virtual = FreeBSDVirtual({}, {})
    freebsd_virtual._module = {}
    freebsd_virtual._module.fail_json = lambda *args, **kwargs: None
    freebsd_virtual.get_virtual_facts()

# Generated at 2022-06-13 03:45:23.551201
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    obj = FreeBSDVirtual()
    obj.get_virtual_facts()

# Generated at 2022-06-13 03:45:27.901738
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual_facts = FreeBSDVirtual().get_virtual_facts()
    expected_virtual_facts = {'virtualization_type': 'xen',
                              'virtualization_role': 'guest',
                              'virtualization_tech_guest': {'xen'},
                              'virtualization_tech_host': set(),
                              }
    assert virtual_facts == expected_virtual_facts

# Generated at 2022-06-13 03:45:29.967327
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    from ansible.module_utils.facts.virtual.freebsd import FreeBSDVirtualCollector
    assert FreeBSDVirtualCollector


# Generated at 2022-06-13 03:45:30.857023
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert FreeBSDVirtualCollector is not None

# Generated at 2022-06-13 03:45:34.255426
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    """
    Constructor of class FreeBSDVirtualCollector should set correct
    values to the instance variables _fact_class and _platform
    """
    virtual_collector = FreeBSDVirtualCollector()
    assert virtual_collector._fact_class == FreeBSDVirtual
    assert virtual_collector._platform == 'FreeBSD'

# Generated at 2022-06-13 03:45:37.011707
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fv = FreeBSDVirtualCollector()
    assert isinstance(fv, FreeBSDVirtualCollector)
    assert fv._platform == 'FreeBSD'
    assert isinstance(fv._fact_class, FreeBSDVirtual)

# Generated at 2022-06-13 03:45:42.120309
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    c = FreeBSDVirtual()
    facts = c.get_virtual_facts()
    # 'virtualization_type' is part of the return
    assert 'virtualization_type' in facts
    # 'virtualization_role' is part of the return
    assert 'virtualization_role' in facts

# Generated at 2022-06-13 03:45:51.788847
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    from ansible_collections.community.general.tests.unit.compat.mock import patch
    from ansible_collections.community.general.plugins.module_utils.facts import Collector

    facts = Collector()
    facts.collect()

    with patch.object(FreeBSDVirtual, 'detect_virt_product') as detect_virt_product, \
            patch.object(FreeBSDVirtual, 'detect_virt_vendor') as detect_virt_vendor:
        detect_virt_product.return_value = {}
        detect_virt_vendor.return_value = {}

        virtual_facts = FreeBSDVirtual(facts)


# Generated at 2022-06-13 03:45:52.606280
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert FreeBSDVirtualCollector(None, None, None)

# Generated at 2022-06-13 03:45:54.152299
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    freebsd = FreeBSDVirtualCollector()
    assert freebsd['virtualization_type'] == ''

# Generated at 2022-06-13 03:46:05.446670
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    freebsd_virtual = FreeBSDVirtualCollector()
    assert freebsd_virtual._fact_class is FreeBSDVirtual
    assert freebsd_virtual._platform == 'FreeBSD'

# Generated at 2022-06-13 03:46:06.029339
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:46:07.177202
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    v = FreeBSDVirtualCollector()
    assert isinstance(v, FreeBSDVirtualCollector)

# Generated at 2022-06-13 03:46:08.719726
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    i = FreeBSDVirtualCollector()
    assert i.platform == 'FreeBSD'

# Generated at 2022-06-13 03:46:11.917058
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_collector = FreeBSDVirtualCollector()
    assert virtual_collector._platform == 'FreeBSD'
    assert virtual_collector._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:46:17.822597
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    facts_dict = FreeBSDVirtualCollector(None, None).collect()
    assert FreeBSDVirtualCollector._platform == 'FreeBSD'
    assert isinstance(facts_dict['virtualization_type'], str)
    assert isinstance(facts_dict['virtualization_role'], str)
    assert isinstance(facts_dict['virtualization_tech_guest'], set)
    assert isinstance(facts_dict['virtualization_tech_host'], set)

# Generated at 2022-06-13 03:46:27.169797
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # Setup
    data = {
        'platform': 'FreeBSD',
        'distribution': 'FreeBSD',
        'virtualization_type': '',
        'virtualization_role': '',
    }
    result = dict(changed=False, ansible_facts=dict(ansible_virtualization=data))

    # Execute
    fv = FreeBSDVirtual()
    result = fv.get_virtual_facts()

    # Assert
    # Assert
    assert result['ansible_virtualization']['virtualization_type'] == ""
    assert result['ansible_virtualization']['virtualization_role'] == ""
    assert result['ansible_virtualization']['virtualization_tech_guest'] == set()
    assert result['ansible_virtualization']['virtualization_tech_host'] == set()

# Generated at 2022-06-13 03:46:29.506467
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_collector = FreeBSDVirtualCollector()
    assert virtual_collector.platform == 'FreeBSD'
    assert virtual_collector._fact_class.platform == 'FreeBSD'

# Generated at 2022-06-13 03:46:35.794820
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    freebsd_virtual = FreeBSDVirtual()
    freebsd_virtual._platform_sysctl = {
        'hw.model': 'VirtualBox',
        'hw.hv_vendor': 'KVM',
        'kern.vm_guest': 'other',
        'security.jail.jailed': '0',
    }

    # Set virtual_facts to the values returned by get_virtual_facts
    virtual_facts = freebsd_virtual.get_virtual_facts()

    # Assert whether values match
    assert virtual_facts['virtualization_role'] == 'guest'
    assert virtual_facts['virtualization_type'] == 'virtualbox'
    assert 'vbox' in virtual_facts['virtualization_tech_guest']
    assert 'vbox' in virtual_facts['virtualization_tech_host']
   

# Generated at 2022-06-13 03:46:37.707265
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert FreeBSDVirtualCollector.platform == 'FreeBSD'
    assert FreeBSDVirtualCollector._fact_class == FreeBSDVirtual


# Generated at 2022-06-13 03:46:49.258656
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    for fact_class in [FreeBSDVirtual]:
        virtual = fact_class()
        virtual_facts = virtual.get_virtual_facts()
        assert isinstance(virtual_facts['virtualization_tech_guest'], set)
        assert isinstance(virtual_facts['virtualization_tech_host'], set)



# Generated at 2022-06-13 03:46:50.412988
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fvcs=FreeBSDVirtualCollector()
    fvcs.collect()


# Generated at 2022-06-13 03:46:53.549890
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    sut = FreeBSDVirtual()
    result = sut.get_virtual_facts()

    assert result['virtualization_type'] == ''
    assert result['virtualization_role'] == ''

# vim: expandtab tabstop=4 shiftwidth=4

# Generated at 2022-06-13 03:46:55.638557
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    FreeBSDVirtualCollector({}, {}).get_virtual_facts() \
        ['ansible_facts']['virtualization_type']

# Generated at 2022-06-13 03:46:56.919042
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    f = FreeBSDVirtualCollector()
    assert f._platform == 'FreeBSD'

# Generated at 2022-06-13 03:46:59.406518
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    collector = FreeBSDVirtualCollector(None)
    # This assert is simply to make sure we've properly constructed a
    # FreeBSDVirtualCollector
    assert collector.platform == 'FreeBSD'

# Generated at 2022-06-13 03:47:00.224976
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    BaseClass = FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:47:01.355636
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    instance = FreeBSDVirtualCollector()
    assert instance.platform == 'FreeBSD'

# Generated at 2022-06-13 03:47:02.439561
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    # It should not return an object of type None
    assert FreeBSDVirtualCollector() is not None

# Generated at 2022-06-13 03:47:08.194495
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    freebsd_virtual = FreeBSDVirtual()
    freebsd_virtual._module = None
    freebsd_virtual._module = MagicMock()
    freebsd_virtual._module.params = dict();
    freebsd_virtual._module.params['gather_subset'] = ['!all', '!min']
    assert freebsd_virtual.get_virtual_facts() == dict(virtualization_type='', virtualization_role='', virtualization_tech_guest=set(), virtualization_tech_host=set())

# Generated at 2022-06-13 03:47:27.511770
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    """This is to test the constructor of class FreeBSDVirtualCollector."""
    test_obj = FreeBSDVirtualCollector()
    assert test_obj._platform == 'FreeBSD'

# Generated at 2022-06-13 03:47:35.467602
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    import pytest

    # Make a dictionary of test cases with expected outputs
    # In this test, the keys are the arguments to get_virtual_facts
    # and the values are a dictionary containing the following keys:
    #  - 'virtualization_type': the string that should be returned by virtualization_type
    #  - 'virtualization_role': the string that should be returned by virtualization_role
    #  - 'virtualization_tech_guest': the string that should be returned by virtualization_tech_guest
    #  - 'virtualization_tech_host': the string that should be returned by virtualization_tech_host

# Generated at 2022-06-13 03:47:37.544216
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert FreeBSDVirtualCollector.platform == 'FreeBSD'
    assert FreeBSDVirtualCollector._fact_class == FreeBSDVirtual


# Generated at 2022-06-13 03:47:43.841424
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    from ansible_collections.ansible.community.tests.unit.module_utils.virtual.sysctl import FakeSysctlVirtProductDetection
    from ansible_collections.ansible.community.tests.unit.module_utils.virtual.sysctl import FakeSysctlVirtVendorDetection
    info = {'sysctl_virt_product': FakeSysctlVirtProductDetection(),
            'sysctl_virt_vendor': FakeSysctlVirtVendorDetection()}
    fake_freebsd = FreeBSDVirtual(info)
    expected = {
        'virtualization_type': 'kvm',
        'virtualization_role': 'guest',
        'virtualization_tech_guest': {'kvm'},
        'virtualization_tech_host': {'kvm'}
    }
    assert fake_freebs

# Generated at 2022-06-13 03:47:48.051198
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    # Instantiate FreeBSDVirtualCollector
    collector = FreeBSDVirtualCollector.collect()

    # Check if fact class is FreeBSDVirtual
    assert collector._fact_class == FreeBSDVirtual

    # Check if platform is FreeBSD
    assert collector._platform == 'FreeBSD'

# Generated at 2022-06-13 03:47:53.276789
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    chroot_facts = FreeBSDVirtual({}).get_virtual_facts()
    assert chroot_facts['virtualization_type'] == ''
    assert chroot_facts['virtualization_role'] == ''
    assert chroot_facts['virtualization_tech_host'] == set()
    assert chroot_facts['virtualization_tech_guest'] == set()

# Generated at 2022-06-13 03:48:01.174813
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    data_dir = os.path.join(os.getcwd(), 'data')
    test_modules_dir = os.path.join(data_dir, 'test_modules')
    test_module_names = os.listdir(test_modules_dir)
    test_module_names.sort()
    test_virtual_facts = {}
    fs = FreeBSDVirtual()
    for test_module_name in test_module_names:
        test_module_dir = os.path.join(test_modules_dir, test_module_name)
        # Collects vm_guest, hw_hv_vendor, jail_jailed, model
        if not os.listdir(test_module_dir):
            continue

        # Reads a test_name from a test module directory name
        # (e.g. ./test_modules

# Generated at 2022-06-13 03:48:03.311920
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_collector = FreeBSDVirtualCollector()

    # Assert the object we got back is what we were expecting.
    assert virtual_collector._platform == 'FreeBSD'
    assert virtual_collector._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:48:14.626302
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual_facts = {}

    # Test if facts are correctly set for VMware guest
    hw_model_facts = {
        'hw.model': 'VMware Virtual Platform',
        'virtualization_tech_guest': set(['vmware']),
        'virtualization_type': 'vmware',
        'virtualization_role': 'guest',
    }
    kern_vm_guest_facts = {
        'kern.vm_guest': 'vmware',
        'virtualization_tech_guest': set(['vmware']),
        'virtualization_type': 'vmware',
        'virtualization_role': 'guest',
    }


# Generated at 2022-06-13 03:48:21.833455
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    '''
    Test get_virtual_facts of class FreeBSDVirtual
    '''
    from unittest import TestCase
    from unittest.mock import MagicMock
    from unittest.mock import patch
    class TestFreeBSDVirtual(TestCase):
        def setUp(self):
            self.test_virtual_fact = FreeBSDVirtual(module=None)

    # To keep the test runs clean, we remove the previously cached facts
    # We don't want to cache the facts here, as we should get the same result
    # every time the function is called
    # This test is independent of the platform it is run on, so if there are
    # any cached facts, we just remove them
    if os.path.exists(os.path.expanduser('~/.ansible/tmp/ansible_virtual_facts')):
        os

# Generated at 2022-06-13 03:49:06.893869
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:49:09.374582
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    # Check if FreeBSDVirtualCollector initializes properly
    freebsd_virtual = FreeBSDVirtualCollector()
    assert freebsd_virtual is not None

# Generated at 2022-06-13 03:49:15.446045
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # Prepare test values
    test_virtual_facts = {
        'virtualization_type': 'xen',
        'virtualization_role': 'guest',
        'virtualization_enabled': True,
        'virtualization_tech_host': set(),
        'virtualization_tech_guest': set(['xen']),
    }

    # Create test object
    freebsd_virtual = FreeBSDVirtual(module=None)

    # Call get_virtual_facts
    result = freebsd_virtual.get_virtual_facts()

    # Check result
    assert result == test_virtual_facts

# Generated at 2022-06-13 03:49:17.945882
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    obj = FreeBSDVirtualCollector()
    assert isinstance(obj, FreeBSDVirtualCollector)

# Generated at 2022-06-13 03:49:20.018557
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_collector = FreeBSDVirtualCollector()
    assert virtual_collector.fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:49:28.477241
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # prepare Virtual instance
    virtual_collector = FreeBSDVirtualCollector()
    virtual_collector._init()

    virtual = FreeBSDVirtual(virtual_collector)

    # prepare test data
    kern_vm_guest = {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_tech_host': set(),
        'virtualization_tech_guest': set()
    }

    hw_hv_vendor = {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_tech_host': set(),
        'virtualization_tech_guest': set()
    }


# Generated at 2022-06-13 03:49:30.212175
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_facts_collector = FreeBSDVirtualCollector()
    assert virtual_facts_collector._platform == 'FreeBSD'
    assert virtual_facts_collector._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:49:31.465319
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual = FreeBSDVirtual()
    virtual_facts = virtual.get_virtual_facts()
    print(str(virtual_facts))

# Generated at 2022-06-13 03:49:34.939589
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    collected_facts = {'ansible_facts': {'hostvars': 'hostvars'}}
    assert FreeBSDVirtualCollector(collected_facts)._platform == 'FreeBSD'
    assert FreeBSDVirtualCollector(collected_facts)._fact_class \
                                                    .__name__ == 'FreeBSDVirtual'



# Generated at 2022-06-13 03:49:38.307986
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    facts = FreeBSDVirtual({}, {}).get_virtual_facts()
    assert facts['virtualization_type'] == 'FreeBSD jail'
    assert 'virtual_guest' not in facts
    assert 'virtual_host' not in facts
    assert 'virtualization_tech_host' not in facts
    assert 'virtualization_tech_guest' not in facts

# Generated at 2022-06-13 03:51:10.540615
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_facts_collector = FreeBSDVirtualCollector()
    assert virtual_facts_collector._platform == 'FreeBSD'
    assert virtual_facts_collector._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:51:13.126452
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fg = FreeBSDVirtualCollector()
    assert fg.platform == 'FreeBSD'
    assert fg.fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:51:18.959063
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.sysctl import VirtualSysctlDetectionMixin
    from ansible.module_utils.facts import virtual
    del virtual.VirtualCollector


# Generated at 2022-06-13 03:51:22.344891
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    facts = FreeBSDVirtual({}).get_virtual_facts()
    assert facts['virtualization_type'] == '' or facts['virtualization_type'] in ('xen', 'vmware', 'jail')
    assert facts['virtualization_role'] == '' or facts['virtualization_role'] in ('guest', 'host')

# Generated at 2022-06-13 03:51:24.148597
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fvc = FreeBSDVirtualCollector()
    assert(fvc._platform == 'FreeBSD')

# Generated at 2022-06-13 03:51:26.953918
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    """ Unit test for constructor of class FreeBSDVirtualCollector """
    fre_virtual = FreeBSDVirtualCollector()
    assert (fre_virtual.platform == 'FreeBSD')
    assert (fre_virtual._fact_class.platform == 'FreeBSD')
    assert (fre_virtual._fact_class.__name__ == 'FreeBSDVirtual')

# Generated at 2022-06-13 03:51:37.392753
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():

    # Setup the test
    testobj = FreeBSDVirtual()

    # Test case #1: {'virtualization_type': 'xen', 'virtualization_role': 'guest', 'virtualization_tech_host': set(), 'virtualization_tech_guest': set(['xen'])}
    testobj.facts['kern.vm_guest'] = 'none'
    testobj.facts['hw.hv_vendor'] = ''
    testobj.facts['security.jail.jailed'] = 0
    testobj.facts['hw.model'] = 'FreeBSD virtual machine'
    testobj.facts['os_family'] = 'FreeBSD'

    results = testobj.get_virtual_facts()
    assert results['virtualization_type'] == 'xen'
    assert results['virtualization_role'] == 'guest'

# Generated at 2022-06-13 03:51:45.981269
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    v = FreeBSDVirtual()

    # FreeBSD guests
    try:
        with open("/proc/self/status", "r") as fd:
            contents = fd.read()
    except Exception:
        contents = ""
    if 'VxID: 1' in contents:
        assert({'virtualization_type': 'xen',
                'virtualization_role': 'guest',
                'virtualization_tech_guest': {'xen'},
                'virtualization_tech_host': set()} == FreeBSDVirtual().get_virtual_facts())

# Generated at 2022-06-13 03:51:49.339979
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    obj1 = FreeBSDVirtualCollector()
    obj2 = FreeBSDVirtualCollector()

    assert id(obj1) == id(obj2)
    assert isinstance(obj1._fact_class, FreeBSDVirtual)
    assert id(obj1._platform) == id(obj2._platform)
    assert obj1._platform == obj2._platform

# Generated at 2022-06-13 03:51:58.565569
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual = FreeBSDVirtual(module=None)

    # Test for jails
    virtual._get_virtual_facts = lambda : {'security.jail.jailed': 1}
    virtual_facts = virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'jail'
    assert virtual_facts['virtualization_role'] == 'guest'
    assert 'linux' in virtual_facts['virtualization_tech_guest']
    assert 'linux' in virtual_facts['virtualization_tech_host']

    # Test for devfs_jail_devfs_ruleset=1  (Xen domU)
    virtual._get_virtual_facts = lambda : {'security.jail.jailed': 2}
    virtual_facts = virtual.get_virtual_facts()