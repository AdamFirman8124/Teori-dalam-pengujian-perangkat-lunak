

# Generated at 2022-06-13 03:43:55.043113
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    v = FreeBSDVirtual({})

    # For now, just test that we can get virtual Facts.
    assert v.get_virtual_facts() is not None

# Generated at 2022-06-13 03:44:00.576847
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual_facts = FreeBSDVirtual({})

    # Pristine environment.
    #
    # The first few keys are added by VirtualCollector.get_virtual_facts, and
    # so aren't tested here.
    expected_virtual_facts = {
        'virtualization_role': '',
        'virtualization_type': '',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set(),
    }
    assert expected_virtual_facts == virtual_facts.get_virtual_facts()

    # Now, set up to return bogus virtualization info from the sysctl
    # calls.

# Generated at 2022-06-13 03:44:04.828613
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    facter_virtual_facts = {
        'virtual': 'None',
        'virtualization_role': 'guest',
        'virtualization_type': 'xen'
    }
    virtual_facts = FreeBSDVirtual({}).get_virtual_facts()
    assert facter_virtual_facts == virtual_facts

# Generated at 2022-06-13 03:44:07.250255
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    freebsd = FreeBSDVirtual()
    virtual_facts = freebsd.get_virtual_facts()

    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''

# Generated at 2022-06-13 03:44:10.253591
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    c = FreeBSDVirtualCollector()
    assert c._platform == 'FreeBSD'
    assert c._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:44:20.123840
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # Create the OpenBSDVirtual class, with faked sysctl values
    openbsd_virtual = FreeBSDVirtual({
        # kern.vm_guest
        'hw.vmm.vm':                      'VM',
        'hw.vmm.vm_guest':                'VM',

        # hw.hv_vendor
        'hv_vendor':                      'VMwareVMware',
        'hv_guest':                       'VMwareVMware',

        # security.jail.jailed
        'security.jail.jailed':           1,
        'jail_jailed':                    1,

        # hw.model
        'hw.model':                       'VMwareVMware',
        'hw_model':                       'VMwareVMware',

    })
    # Call the method
    virtual_facts = openbsd_

# Generated at 2022-06-13 03:44:23.135578
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    """
      Test to see if the FreeBSDVirtualCollector class is constructed correctly.
    """
    virtual_collector = FreeBSDVirtualCollector()
    assert virtual_collector._platform == 'FreeBSD'
    assert virtual_collector._fact_class == FreeBSDVirtual


# Generated at 2022-06-13 03:44:29.830364
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    v = FreeBSDVirtual()

    # Test for guest
    v.facts['hw.model'] = 'FreeBSD/amd64 (HVM domU)'
    vs = v.get_virtual_facts()
    assert 'freebsd' in vs['virtualization_tech_guest']
    assert vs['virtualization_type'] == 'hvm' and 'xen' not in vs['virtualization_tech_guest']

    v.facts['hw.model'] = 'FreeBSD/amd64 (XEN)'
    vs = v.get_virtual_facts()
    assert vs['virtualization_type'] == 'xen' and 'hvm' not in vs['virtualization_tech_guest']

    # Test for host
    v.facts['hw.model'] = 'FreeBSD/amd64 (Xen Hypervisor)'
    vs = v.get

# Generated at 2022-06-13 03:44:31.733106
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    x = FreeBSDVirtualCollector()
    assert x.__class__.__name__ == 'FreeBSDVirtualCollector'


# Generated at 2022-06-13 03:44:33.863394
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fvc = FreeBSDVirtualCollector()
    assert fvc._fact_class == FreeBSDVirtual
    assert fvc._platform == FreeBSDVirtual.platform

# Generated at 2022-06-13 03:44:41.543914
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    freebsd_virtual_collector_instance = FreeBSDVirtualCollector()
    assert freebsd_virtual_collector_instance._fact_class == FreeBSDVirtual
    assert freebsd_virtual_collector_instance._platform == 'FreeBSD'

# Generated at 2022-06-13 03:44:42.209180
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert FreeBSDVirtualCollector.platform == 'FreeBSD'


# Generated at 2022-06-13 03:44:45.322739
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_facts = FreeBSDVirtualCollector().collect()
    assert virtual_facts['virtualization_type'] != '' or \
        virtual_facts['virtualization_role'] != '' or \
        virtual_facts['virtualization_role'] != 'physical'

# Generated at 2022-06-13 03:44:47.943473
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    collector = FreeBSDVirtualCollector()
    assert collector.platform == 'FreeBSD'
    assert collector.fact_class == FreeBSDVirtual


# Generated at 2022-06-13 03:44:58.476272
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():

    # Set test values for method
    # if sysctl kern.vm_guest is set, virtualization_type and role set according to the value.
    # if the value of sysctl hw.hv_vendor is set to none, virtualization_type and role set according to the value of
    # sysctl hw.hv_vendor.
    # if the value of sysctl security.jail.jailed is set to 1, virtualization_type and role set according to the value of security.jail.jailed.
    # if the value of sysctl hw.model is set to none, virtualization_type and role set according to the value of hw.model.

    # Default value test

    virtual_facts_default = FreeBSDVirtual({})
    facts_default = virtual_facts_default.get_virtual_facts()
    assert facts

# Generated at 2022-06-13 03:45:08.872057
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # Mock sysctl output
    virtual_facts = {}

    # Set empty values as default
    virtual_facts['virtualization_type'] = ''
    virtual_facts['virtualization_role'] = ''

    kern_vm_guest = {}
    kern_vm_guest['sysctl'] = 'kern.vm_guest'
    kern_vm_guest['virtualization_tech_guest'] = set()
    kern_vm_guest['virtualization_tech_host'] = set()
    kern_vm_guest['virtualization_type'] = ''

    hw_hv_vendor = {}
    hw_hv_vendor['sysctl'] = 'hw.hv_vendor'
    hw_hv_vendor['virtualization_tech_guest'] = set()
   

# Generated at 2022-06-13 03:45:17.074362
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    """FreeBSD: return facts regarding virtualization state"""
    test_obj = FreeBSDVirtual({})
    test_obj.facts = dict()
    expected_facts = dict(
        virtualization_type='xen',
        virtualization_role='guest',
        virtualization_tech_guest={'xen'},
        virtualization_tech_host={'xen'}
    )
    # Call the get_virtual_facts under test
    test_obj.get_virtual_facts()
    assert test_obj.facts == expected_facts

# Generated at 2022-06-13 03:45:19.304936
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    import doctest
    module = doctest.testmod(FreeBSDVirtualCollector)
    assert module.failed == 0

# Generated at 2022-06-13 03:45:27.902449
# Unit test for method get_virtual_facts of class FreeBSDVirtual

# Generated at 2022-06-13 03:45:29.213646
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    f = FreeBSDVirtual({})
    f.get_virtual_facts()

# Generated at 2022-06-13 03:45:33.996435
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert VirtualCollector.get_platform() == 'FreeBSD'


# Generated at 2022-06-13 03:45:45.260806
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    import json

    # Create instance of FreeBSDVirtual
    freebsd_virtual = FreeBSDVirtual()

    # Expected virtual facts
    virtual_facts = {'virtualization_type': '', 'virtualization_role': '', 'virtualization_tech_host': set(), 'virtualization_tech_guest': set()}

    # Get virtual facts
    fact_ret = freebsd_virtual.get_virtual_facts()

    # Compare actual virtual facts with expected virtual facts
    assert fact_ret == virtual_facts

    # Compare actual virtual facts with output of module setup
    # Using the JSON parser as the output of module setup is in JSON format
    # Setup the input data
    input_data = dict()
    input_data['ansible_facts'] = fact_ret
    input_data['changed'] = False

    # Load the output data
    output_

# Generated at 2022-06-13 03:45:54.402863
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    kern_vm_guest = {
        'virtualization_tech_guest': [],
        'virtualization_tech_host': [],
    },
    hw_hv_vendor = {
        'virtualization_tech_guest': [],
        'virtualization_tech_host': [],
    }
    sec_jail_jailed = {
        'virtualization_tech_guest': [],
        'virtualization_tech_host': [],
    }
    hw_model = {
        'virtualization_tech_guest': [],
        'virtualization_tech_host': [],
    }
    virtual = FreeBSDVirtual()
    virtual.detect_virt_product = lambda sysctl_name: getattr(
        virtual, '_' + sysctl_name.replace(".", "_"))


# Generated at 2022-06-13 03:45:58.145927
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    # Constructor of class FreeBSDVirtualCollector should instantiate FreeBSDVirtual object.
    fbc = FreeBSDVirtualCollector()
    assert isinstance(fbc._fact, FreeBSDVirtual)

# Generated at 2022-06-13 03:46:03.575407
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    facts = {}
    shared_facts = {'ansible_current_user': {'name': 'ansible'}}
    virtual_facts = FreeBSDVirtualCollector(facts, shared_facts).collect()

    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts

# Generated at 2022-06-13 03:46:06.623150
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_collector = FreeBSDVirtualCollector()
    assert virtual_collector.platform == 'FreeBSD'
    assert virtual_collector.fact_class == FreeBSDVirtual
    assert virtual_collector.fact_class._platform == 'FreeBSD'

# Generated at 2022-06-13 03:46:08.859909
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    bs = FreeBSDVirtualCollector()
    assert bs.platform == 'FreeBSD'
    assert bs._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:46:19.369488
# Unit test for method get_virtual_facts of class FreeBSDVirtual

# Generated at 2022-06-13 03:46:23.214817
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_facts = {}
    vc = FreeBSDVirtualCollector()
    virtual_facts = vc.collect(virtual_facts, None)
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts

# Generated at 2022-06-13 03:46:24.689625
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    x = FreeBSDVirtualCollector()
    assert x._platform == 'FreeBSD'


# Generated at 2022-06-13 03:46:44.784189
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    class TestFreeBSDVirtual:
        def __init__(self, os_release_content=None, os_release_path=None,
                     device_path=None, sysctl_kern_vm_guest_content=None,
                     sysctl_hw_hv_vendor_content=None,
                     sysctl_security_jail_jailed_content=None,
                     sysctl_hw_model=None):
            if os_release_content is not None:
                self._os_release_content = os_release_content
            else:
                self._os_release_content = None
            if os_release_path is not None:
                self._os_release_path = os_release_path
            else:
                self._os_release_path = None
            if device_path is not None:
                self._device

# Generated at 2022-06-13 03:46:45.938849
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
  assert isinstance(FreeBSDVirtualCollector(), FreeBSDVirtualCollector)

# Generated at 2022-06-13 03:46:46.933730
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:46:50.878699
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    facts = FreeBSDVirtualCollector()
    FACT_CLASS = facts._fact_class
    PLATFORM = facts._platform

    assert FACT_CLASS == FreeBSDVirtual
    assert PLATFORM == 'FreeBSD'

# Generated at 2022-06-13 03:46:52.788756
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    collector = FreeBSDVirtualCollector()
    assert collector is not None
    assert collector._platform == 'FreeBSD'
    assert collector._fact_class is FreeBSDVirtual

# Generated at 2022-06-13 03:47:01.925744
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.sysctl import FreeBSDVirtualSysctlDetectionMixin
    from ansible.module_utils.facts.virtual.openbsd import OpenBSDVirtualDetectionMixin
    from ansible.module_utils.facts.virtual.netbsd import NetBSDVirtualDetectionMixin

    class TestFreeBSDVirtual(FreeBSDVirtual, FreeBSDVirtualSysctlDetectionMixin, OpenBSDVirtualDetectionMixin, NetBSDVirtualDetectionMixin):
        platform = 'FreeBSD'

    virtual_facts = TestFreeBSDVirtual(None, None).get_virtual_facts()
    assert isinstance(virtual_facts, dict)
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts

# Generated at 2022-06-13 03:47:10.973598
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # Create dicts to mock sysctl outputs
    kern_vm_guest = {
        'kern.vm_guest': 'e1000',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set(['hypervisor']),
    }
    hw_hv_vendor = {
        'hw.hv_vendor': 'FreeBSD',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set(['hypervisor']),
    }
    sec_jail_jailed = {
        'security.jail.jailed': '1',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set(['jail']),
    }

# Generated at 2022-06-13 03:47:11.344364
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:47:13.035344
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_facts = FreeBSDVirtualCollector()
    assert virtual_facts._platform == "FreeBSD"
    assert virtual_facts._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:47:21.981261
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    '''Test get_virtual_facts method of FreeBSDVirtual class'''
    from ansible.module_utils import basic
    from ansible.module_utils.facts import collector

    # create FreeBSDVirtual object
    collect_subset = ['!all', '!min']
    gather_subset = ['!all', '!min']
    data = FreeBSDVirtual(collect_subset, gather_subset)
    # Mock facts to return an empty dictionary
    data.collect_subset = []
    data.gather_subset = []

# Generated at 2022-06-13 03:47:47.549814
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    freebsd = VirtualCollector.factory()
    assert type(freebsd) == FreeBSDVirtualCollector


# Generated at 2022-06-13 03:47:57.358277
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # Initialize FreeBSDVirtual object
    freebsd_virtual = FreeBSDVirtual()
    freebsd_virtual.kern_vm_guest = 'Xen'
    freebsd_virtual.hw_hv_vendor = 'KVM'
    freebsd_virtual.virtualization_tech_guest = set('')
    freebsd_virtual.virtualization_tech_guest.add('Xen')
    freebsd_virtual.virtualization_tech_guest.add('KVM')
    freebsd_virtual.virtualization_tech_host = set('')
    functions = [
        (freebsd_virtual.is_xen, True),
        (freebsd_virtual.is_jail, False),
        (freebsd_virtual.is_kvm, True),
    ]
    # M

# Generated at 2022-06-13 03:47:58.481892
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    vc = FreeBSDVirtualCollector()
    assert vc is not None

# Generated at 2022-06-13 03:47:59.558651
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    bsdvirt = FreeBSDVirtual()
    bsdvirt.get_virtual_facts()

# Generated at 2022-06-13 03:48:02.920570
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    bsd_virtual = FreeBSDVirtual()
    facts = bsd_virtual.get_virtual_facts()

    assert facts['virtualization_type'] == 'xen'
    assert facts['virtualization_role'] == 'guest'
    assert facts['virtualization_tech_guest'] == set(['xen'])
    assert facts['virtualization_tech_host'] == set([])

# Generated at 2022-06-13 03:48:04.932273
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    collector = FreeBSDVirtualCollector()
    assert collector._fact_class == FreeBSDVirtual
    assert collector._platform == 'FreeBSD'



# Generated at 2022-06-13 03:48:08.170696
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    vc = FreeBSDVirtualCollector()
    assert vc._platform == 'FreeBSD'
    assert vc._fact_class == FreeBSDVirtual


# Generated at 2022-06-13 03:48:09.937371
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_collector = FreeBSDVirtualCollector()
    assert virtual_collector.platform == 'FreeBSD'

# Generated at 2022-06-13 03:48:13.978417
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    freebsd_virtual_collector = FreeBSDVirtualCollector()
    assert freebsd_virtual_collector.platform == 'FreeBSD'
    assert freebsd_virtual_collector.fact_class == FreeBSDVirtual


# Generated at 2022-06-13 03:48:15.667937
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fc = FreeBSDVirtualCollector()
    assert fc._platform == 'FreeBSD'
    assert fc._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:49:30.717577
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():

    # Preconditions
    assert True

    # Test with expected output
    """
    Dict with
    - virtualization_type
    - virtualization_role
    - virtualization_tech_guest
    - virtualization_tech_host
    """
    expected_output = {
        'virtualization_type': 'xen',
        'virtualization_role': 'guest',
        'virtualization_tech_guest': {'xen'},
        'virtualization_tech_host': {'xen'},
    }
    output = FreeBSDVirtual(
        module=None,
        subprocess_loader=None,
        subprocess_spy=None
    ).get_virtual_facts()
    assert isinstance(output, dict)
    assert expected_output == output

# Generated at 2022-06-13 03:49:31.452540
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    f = FreeBSDVirtualCollector()
    assert f is not None

# Generated at 2022-06-13 03:49:32.616886
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    bsd_virtual = FreeBSDVirtual(None)
    assert bsd_virtual.get_virtual_facts() == {}

# Generated at 2022-06-13 03:49:35.080114
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    """
    The following test case tests the constructor of class FreeBSDVirtualCollector by
    calling the constructor without any arguments
    """
    collector = FreeBSDVirtualCollector()
    assert collector is not None

# Generated at 2022-06-13 03:49:41.120457
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():

    # Testing on FreeBSD 10.2
    freebsd_virtual_facts = dict(
        virtualization_type = 'xen',
        virtualization_role = 'guest',
        virtualization_tech_guest = set(['xen']),
        virtualization_tech_host = set(['xen']),
    )

    # Create a temporary FreeBSDVirtual class for testing
    class TestFreeBSDVirtual(FreeBSDVirtual):
        def __init__(self):
            pass

    test_freebsd_virtual = TestFreeBSDVirtual()

    # Test if get_virtual_facts returns expected dict
    assert test_freebsd_virtual.get_virtual_facts() == freebsd_virtual_facts

# Generated at 2022-06-13 03:49:44.014977
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # All tests are not supported on FreeBSD
    assert FreeBSDVirtual().get_virtual_facts() == {}

# Generated at 2022-06-13 03:49:45.171683
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    result = FreeBSDVirtualCollector()
    assert result._platform == 'FreeBSD'

# Generated at 2022-06-13 03:49:47.336633
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    vc = FreeBSDVirtualCollector()
    assert vc


# Generated at 2022-06-13 03:49:48.893632
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert FreeBSDVirtualCollector._platform == 'FreeBSD'
    assert FreeBSDVirtualCollector._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:49:52.756757
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    detected_facts = FreeBSDVirtual().get_virtual_facts()
    assert os.path.exists('/dev/xen/xenstore') == (
        detected_facts['virtualization_type'] == 'xen' and
        detected_facts['virtualization_role'] == 'guest'
    )

# Generated at 2022-06-13 03:52:14.474495
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    facter_virtual = FreeBSDVirtual(None)
    facts = facter_virtual.get_virtual_facts()
    assert facts['virtualization_type'] == 'xen'
    assert facts['virtualization_role'] == 'guest'

# Generated at 2022-06-13 03:52:17.281720
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    facts = VirtualCollector.get_virtual_facts()

    assert facts is not None
    assert 'virtualization_type' in facts
    assert 'virtualization_role' in facts
    assert 'virtualization_tech_host' in facts

# Generated at 2022-06-13 03:52:24.239146
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.sysctl import FreeBSDSysctlDetectionMixin
    from ansible.module_utils.facts.virtual.vendor import (FreeBSDVirtualVendorDetectionMixin)

    class MockFreeBSDVirtual(FreeBSDSysctlDetectionMixin,
                             FreeBSDVirtualVendorDetectionMixin,
                             FreeBSDVirtual):
        pass

    obj = MockFreeBSDVirtual({})
    actual = obj.get_virtual_facts()
    expected = {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set(),
    }
    assert actual == expected

# Generated at 2022-06-13 03:52:26.730109
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fvc = FreeBSDVirtualCollector()
    assert fvc._platform == 'FreeBSD'
    assert fvc._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:52:28.165369
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fvc = FreeBSDVirtualCollector()
    assert fvc.platform == 'FreeBSD'
    assert fvc.fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:52:30.855312
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():

    fbk = FreeBSDVirtual()

    # FreeBSD Virtual facts
    result_fbk = dict(virtualization_type='xen',
                      virtualization_role='guest',
                      virtualization_thu_host=['xen'],
                      virtualization_tech_guest=['xen'])
    assert result_fbk == fbk.get_virtual_facts()

# Generated at 2022-06-13 03:52:31.975227
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    freebsd_virtual_collector = FreeBSDVirtualCollector()
    assert freebsd_virtual_collector._platform == 'FreeBSD'

# Generated at 2022-06-13 03:52:36.169660
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual = FreeBSDVirtual()
    # Get current values of sysctl entries and remember them.
    saved_sysctl = {}
    for s in ('hw.model', 'kern.vm_guest', 'security.jail.jailed', 'hw.hv_vendor'):
        current_value = virtual._get_current_sysctl(s)
        saved_sysctl[s] = current_value
    # Set some non-standard values.
    new_sysctl = {'hw.model': 'QEMU Virtual CPU version 2.5.0',
                  'kern.vm_guest': 'other',
                  'security.jail.jailed': '1',
                  'hw.hv_vendor': 'test_vendor_id'}
    for s in new_sysctl:
        virtual._set_current_sys

# Generated at 2022-06-13 03:52:39.361154
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    from ansible.module_utils.facts.virtual.freebsd import FreeBSDVirtualCollector
    import ansible.module_utils.facts.virtual.sysctl

    assert FreeBSDVirtualCollector._platform == 'FreeBSD'
    assert isinstance(FreeBSDVirtualCollector._fact_class(dict(), dict()), FreeBSDVirtual)



# Generated at 2022-06-13 03:52:41.068336
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    freebsd_virtual_collector = FreeBSDVirtualCollector([])
    assert freebsd_virtual_collector._platform == 'FreeBSD'