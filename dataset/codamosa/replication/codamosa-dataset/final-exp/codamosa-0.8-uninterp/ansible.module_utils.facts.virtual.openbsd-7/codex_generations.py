

# Generated at 2022-06-13 04:09:53.273122
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    vc = OpenBSDVirtualCollector()
    assert vc._platform == 'OpenBSD'
    assert vc._fact_class == OpenBSDVirtual

# Generated at 2022-06-13 04:09:55.082553
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    # Unit test for constructor of class OpenBSDVirtualCollector
    obj = OpenBSDVirtualCollector()
    print(obj)

# Generated at 2022-06-13 04:09:55.748563
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    OpenBSDVirtualCollector("")

# Generated at 2022-06-13 04:10:01.642001
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    openbsd_virtual_facts = OpenBSDVirtual({})
    # Test with a known dmesg.boot from a bhyve VM host

# Generated at 2022-06-13 04:10:10.901580
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # Define some helper functions
    def check_virtual_facts(virtual_facts, expected_result, test_name):
        if virtual_facts['virtualization_type'] != expected_result['virtualization_type']:
            print('The virtualization_type for %s does not match the expected value.' % (test_name, ))
            print('Expected: %s' % (expected_result['virtualization_type'], ))
            print('Found: %s' % (virtual_facts['virtualization_type'], ))
            raise AssertionError
        if virtual_facts['virtualization_role'] != expected_result['virtualization_role']:
            print('The virtualization_role for %s does not match the expected value.' % (test_name, ))

# Generated at 2022-06-13 04:10:15.984780
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    '''Unit test of get_virtual_facts of OpenBSDVirtual'''
    module = OpenBSDVirtual()
    ret = module.get_virtual_facts()

    assert ret['virtualization_tech_guest'] == set()
    assert ret['virtualization_tech_host'] == set()
    assert ret['virtualization_type'] == ''
    assert ret['virtualization_role'] == ''

# Generated at 2022-06-13 04:10:19.224979
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    virtual_collector = OpenBSDVirtualCollector()
    assert virtual_collector._fact_class.platform == 'OpenBSD'

# Generated at 2022-06-13 04:10:29.880631
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    v = OpenBSDVirtual()

    # Test common virtualization_type and virtualization_role
    v.get_file_content = lambda path: ""
    assert v.get_virtual_facts() == {'virtualization_type': '', 'virtualization_role': ''}

    # Test virtualization_type vmware and virtualization_role guest
    v.get_file_content = lambda path: 'vmware'
    assert v.get_virtual_facts() == {'virtualization_type': 'vmware', 'virtualization_role': 'guest'}

    # Test virtualization_type xen and virtualization_role guest
    v.get_file_content = lambda path: 'Xen domU'
    assert v.get_virtual_facts() == {'virtualization_type': 'xen', 'virtualization_role': 'guest'}

# Generated at 2022-06-13 04:10:32.232648
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    detect_virt_fact = OpenBSDVirtual()
    detect_virt_fact.get_virtual_facts()

# Generated at 2022-06-13 04:10:40.851904
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    vclass = OpenBSDVirtual()

# Generated at 2022-06-13 04:10:53.147160
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    """
    This is a unit test for get_virtual_facts() method in OpenBSDVirtual class.
    The method should return virtualization facts.
    """
    virtual = OpenBSDVirtual()
    virtual_facts = virtual.get_virtual_facts()

    assert virtual_facts['virtualization_type'] == 'vmm'
    assert virtual_facts['virtualization_role'] == 'host'
    assert virtual_facts['virtualization_tech_guest'] == set()
    assert virtual_facts['virtualization_tech_host'] == {'vmm'}
    assert virtual_facts['virtualization_product'] == ''
    assert virtual_facts['virtualization_vendor'] == ''

# Generated at 2022-06-13 04:10:56.691161
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    openbsd_virtual_collector = OpenBSDVirtualCollector()
    assert openbsd_virtual_collector._fact_class is OpenBSDVirtual
    assert openbsd_virtual_collector._platform is 'OpenBSD'

# Generated at 2022-06-13 04:10:58.311551
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    assert issubclass(OpenBSDVirtualCollector, VirtualCollector)


# Generated at 2022-06-13 04:11:02.067608
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    # Act
    openbsd_virtual_collector = OpenBSDVirtualCollector()

    # Assert
    # Verify if the virtual_collector is an instance of OpenBSDVirtualCollector
    assert isinstance(openbsd_virtual_collector, OpenBSDVirtualCollector)

# Generated at 2022-06-13 04:11:05.463714
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virtual = OpenBSDVirtual()
    virtual_facts = virtual.get_virtual_facts()

    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts

# Generated at 2022-06-13 04:11:15.997480
# Unit test for method get_virtual_facts of class OpenBSDVirtual

# Generated at 2022-06-13 04:11:20.002364
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    openbsd_virtual_collector = OpenBSDVirtualCollector()
    assert openbsd_virtual_collector._platform == "OpenBSD"
    assert openbsd_virtual_collector._fact_class == OpenBSDVirtual

# Generated at 2022-06-13 04:11:23.732317
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    openbsd_virtual_collector = OpenBSDVirtualCollector()
    assert openbsd_virtual_collector._fact_class is OpenBSDVirtual
    assert openbsd_virtual_collector._platform == 'OpenBSD'

# Generated at 2022-06-13 04:11:29.764023
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    openbsd_virtual_collector_object = OpenBSDVirtualCollector()

    # Check if object type is OpenBSDVirtualCollector
    assert (type(openbsd_virtual_collector_object) == OpenBSDVirtualCollector)

    # Check if object's fact_class is OpenBSDVirtual
    assert (openbsd_virtual_collector_object._fact_class == OpenBSDVirtual)

    # Check if object's platform is OpenBSD
    assert (openbsd_virtual_collector_object._platform == 'OpenBSD')

# Generated at 2022-06-13 04:11:36.064832
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    openbsd_virtual = OpenBSDVirtual()
    expected = {'virtualization_type': '', 'virtualization_role': 'host',
                'virtualization_tech_host': set(['vmm']),
                'virtualization_tech_guest': set()}
    assert openbsd_virtual.get_virtual_facts() == expected

# Generated at 2022-06-13 04:11:46.319440
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    collector = OpenBSDVirtualCollector()
    facts = collector.get_virtual_facts()
    assert facts['virtualization_tech'] == 'qemu'
    assert facts['virtualization_type'] == 'kvm'
    assert facts['virtualization_role'] == 'guest'

# Generated at 2022-06-13 04:11:53.919112
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    """
    Test class Virtual with OpenBSD OS.

    The tests are based on the following dmesg.boot:
    https://github.com/kyleam/ansible-facts/blob/master/dmesg.boot.OpenBSD
    """
    # Set default values
    d = {'virtualization_type': '',
         'virtualization_role': '',
         'virtualization_tech_host': set(),
         'virtualization_tech_guest': set()}
    collector = VirtualCollector(None, OpenBSDVirtualCollector._platform)
    facts = collector._create_facts()

    # Test OpenBSD host

# Generated at 2022-06-13 04:12:00.905653
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():

    from ansible.module_utils.facts.virtual.openbsd import OpenBSDVirtual
    from ansible.module_utils.facts.virtual.sysctl import VirtualSysctlDetectionMixin
    import pytest

    # object
    my_test_class = OpenBSDVirtual()
    my_test_class.facts = {}
    #mock get_file_content
    my_test_class.get_file_content = lambda x: ''

    #mock detect_virt_vendor
    my_test_class.detect_virt_vendor = lambda x: {'virtualization_type': '',
                                                  'virtualization_role': '',
                                                  'virtualization_tech_guest': set([]),
                                                  'virtualization_tech_host': set(['vmm'])}

    #mock detect_

# Generated at 2022-06-13 04:12:02.884155
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    instance = OpenBSDVirtualCollector()
    assert isinstance(instance, OpenBSDVirtualCollector)


# Generated at 2022-06-13 04:12:05.152658
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    vc = OpenBSDVirtualCollector()
    assert vc._platform == 'OpenBSD'
    assert vc._fact_class == OpenBSDVirtual

# Generated at 2022-06-13 04:12:07.946944
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    assert(OpenBSDVirtualCollector._fact_class == OpenBSDVirtual)
    assert(OpenBSDVirtualCollector._platform == 'OpenBSD')

# Generated at 2022-06-13 04:12:16.793338
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():

    test_sysctl_dict = {
        'hw.product': 'VMware6 virtual machine',
        'hw.vendor': 'VMware, Inc.',
        'hw.model': 'VMware6'
    }

    test_sysctl_dict_invalid = {
        'hw.product': '',
        'hw.vendor': '',
        'hw.model': ''
    }

    test_sysctl_dict_vmm = {
        'hw.vendor': 'XXX Inc.',
        'hw.model': 'Intel(R) Xeon(R) CPU E5-2690 v4 @ 2.60GHz'
    }

    test_sysctl_dict_openbsd_hv = {
        'hw.vendor': 'XXX Inc.',
        'hw.model': 'Hypervisor'
    }

# Generated at 2022-06-13 04:12:23.926567
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    facter_virtual_results = {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set(),
    }

    virtual = OpenBSDVirtual(facter_virtual_results, None)

    # get_virtual_facts should return a dict
    assert isinstance(virtual.get_virtual_facts(), dict)

    # get_virtual_facts should not return an empty dict
    assert virtual.get_virtual_facts() != {}

# Generated at 2022-06-13 04:12:33.682377
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # Initialize a OpenBSDVirtual object to test method get_virtual_facts
    virtual = OpenBSDVirtual()

    # Case 1: Returns empty values if no virtualization tech detected
    virtual_facts = virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''
    assert not virtual_facts['virtualization_tech_guest']
    assert not virtual_facts['virtualization_tech_host']

    # Case 2: Returns virtualization type 'vmm', role 'host' and virtual
    # technologies 'vmm' and 'host' if vmm attached
    with open(OpenBSDVirtual.DMESG_BOOT, 'w') as f:
        f.write('vmm0 at mainbus0: VMX/EPT')

# Generated at 2022-06-13 04:12:36.241455
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    collector = OpenBSDVirtualCollector()
    assert isinstance(collector, OpenBSDVirtualCollector)

# Generated at 2022-06-13 04:12:48.300449
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    OpenBSDVirtualCollector()

# Generated at 2022-06-13 04:12:51.152994
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    openbsd_virtual_collector = OpenBSDVirtualCollector()
    assert openbsd_virtual_collector._fact_class.platform == 'OpenBSD'

# Generated at 2022-06-13 04:12:52.262153
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    OpenBSDVirtualCollector()

# Generated at 2022-06-13 04:12:54.689859
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    openbsd_virtual_collector = OpenBSDVirtualCollector({}, {}, {})
    openbsd_virtual_collector.get_virtual_facts()

# Generated at 2022-06-13 04:13:01.199495
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.virtual.openbsd import OpenBSDVirtualCollector

    # Create an instance of OpenBSDVirtualCollector
    virtual_collector = OpenBSDVirtualCollector()
    assert(virtual_collector.__class__.__name__ == 'OpenBSDVirtualCollector')
    assert(virtual_collector._platform == 'OpenBSD')
    assert(virtual_collector._fact_class.__name__ == 'OpenBSDVirtual')

    # Replace the 'virtual' key of the Collector object with an instance
    # of OpenBSDVirtualCollector
    collector.collector[collector.OS_FAMILY].pop('virtual')
    collector.collector[collector.OS_FAMILY]['virtual'] = virtual_collector


# Generated at 2022-06-13 04:13:10.345810
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # OpenBSD 6.7 GENERIC#1361 amd64
    facts = {'kernel': 'OpenBSD'}
    openbsd_virtual = OpenBSDVirtual(facts, None)
    virtual_facts = openbsd_virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'OpenBSD'
    assert virtual_facts['virtualization_role'] == 'guest'
    assert virtual_facts['virtualization_tech_guest'] == set()
    assert virtual_facts['virtualization_tech_host'] == set()

    # OpenBSD 6.7 GENERIC.MP#1361 amd64
    facts = {'kernel': 'OpenBSD',
             'product_name': 'VirtualBox',
             'product_version': '5.2.26r128414'}

# Generated at 2022-06-13 04:13:13.746458
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    obj = OpenBSDVirtualCollector()
    assert obj._fact_class is OpenBSDVirtual
    assert obj._platform == 'OpenBSD'

# Generated at 2022-06-13 04:13:15.662433
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    obj = OpenBSDVirtualCollector()
    assert isinstance(obj, OpenBSDVirtualCollector)


# Generated at 2022-06-13 04:13:27.081327
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    from ansible.module_utils.facts.utils import get_file_content
    from ansible.module_utils.facts.virtual.openbsd import OpenBSDVirtual
    from ansible.module_utils.six import StringIO


# Generated at 2022-06-13 04:13:30.660149
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    openbsd_virtual_collector = OpenBSDVirtualCollector()
    assert openbsd_virtual_collector._platform == 'OpenBSD'
    assert openbsd_virtual_collector._fact_class == OpenBSDVirtual

# Generated at 2022-06-13 04:13:59.051200
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    class OpenBSDVirtual_test(OpenBSDVirtual):
        platform = 'OpenBSD'
        DMESG_BOOT = './dmesg-boot'

    obv = OpenBSDVirtual_test()
    virtual_facts = obv.get_virtual_facts()
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts

# Generated at 2022-06-13 04:14:05.770301
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virtual = OpenBSDVirtual()
    virtual_facts = virtual.get_virtual_facts()
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts
    assert 'virtualization_guest_topology' in virtual_facts
    assert 'virtualization_product' in virtual_facts
    assert 'virtualization_product_version' in virtual_facts

# Generated at 2022-06-13 04:14:07.301460
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    virtual_collector = OpenBSDVirtualCollector()
    assert virtual_collector.__class__.__name__ == 'OpenBSDVirtualCollector'

# Generated at 2022-06-13 04:14:10.602249
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    detector = OpenBSDVirtualCollector()
    virtual_facts = detector.get_virtual_facts()

    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''

# Generated at 2022-06-13 04:14:12.174853
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    os_virtual = OpenBSDVirtualCollector()
    assert os_virtual._platform == 'OpenBSD'
    assert os_virtual._fact_class == OpenBSDVirtual

# Generated at 2022-06-13 04:14:13.644107
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virt = OpenBSDVirtual()
    result = virt.get_virtual_facts()
    assert 'virtualization_type' in result
    assert 'virtualization_role' in result
    assert 'virtualization_tech_guest' in result
    assert 'virtualization_tech_host' in result

# Generated at 2022-06-13 04:14:23.094077
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    """Unit tests for get_virtual_facts of class OpenBSDVirtual."""
    openbsdvirtual_collector = OpenBSDVirtualCollector()

    # Set expected values
    expected = {
        'virtualization_type': '',
        'virtualization_role': ''
    }

    # Test default values, when no virtualization running.
    openbsdvirtual_collector.module.get_bin_path = lambda x: None
    openbsdvirtual_collector.module.get_file_content = lambda x: ""

    assert openbsdvirtual_collector.get_virtual_facts() == expected

    # Test VBoxGuestAdditions
    openbsdvirtual_collector.module.get_bin_path = lambda x: True

# Generated at 2022-06-13 04:14:29.962322
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virtual = OpenBSDVirtual({})

# Generated at 2022-06-13 04:14:40.493125
# Unit test for method get_virtual_facts of class OpenBSDVirtual

# Generated at 2022-06-13 04:14:51.410895
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    '''
    validate get_virtual_facts() against lscpu on a x86-64 system
    with CPU that has SVM
    '''
    n = OpenBSDVirtual()
    # The expected result is a string.
    expected = {'virtualization_type': 'vmm', 'virtualization_role': 'host',
                'virtualization_tech_host': {'vmm'},
                'virtualization_tech_guest': set()}
    actual = n.get_virtual_facts()
    assert actual == expected, "Failed to detect OpenBSD virtualization with no vmm(4) attached"

    # The expected result is a string.

# Generated at 2022-06-13 04:15:41.796755
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    o = OpenBSDVirtualCollector()

# Generated at 2022-06-13 04:15:45.558898
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    openbsd_virtual = OpenBSDVirtual()
    return openbsd_virtual.get_virtual_facts()

# Generated at 2022-06-13 04:15:46.676078
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    collector = OpenBSDVirtualCollector()
    assert collector.platform == 'OpenBSD'

# Generated at 2022-06-13 04:15:49.204957
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    openbsd_virtual_facts = OpenBSDVirtual()
    assert openbsd_virtual_facts.get_virtual_facts() == {
        'virtualization_role': 'guest',
        'virtualization_type': 'vmm',
        'virtualization_tech_guest': set(['vmm']),
        'virtualization_tech_host': set(['vmm'])
    }

# Generated at 2022-06-13 04:15:54.007078
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virt = OpenBSDVirtual()
    gathered_facts = {}
    fake_product_facts = {
        'virtualization_type': 'xxx',
        'virtualization_role': 'xxx',
        'virtualization_tech_guest': ['xxx'],
        'virtualization_tech_host': ['xxx']
    }
    fake_vendor_facts = {
        'virtualization_type': 'xxx',
        'virtualization_role': 'xxx',
        'virtualization_tech_guest': ['xxx'],
        'virtualization_tech_host': ['xxx']
    }

    # Test case 1: Virtualization tech products or vendors are not set as empty
    virtual_facts = virt.get_virtual_facts()

# Generated at 2022-06-13 04:15:54.786807
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    _obj = OpenBSDVirtualCollector()
    assert _obj.platform == 'OpenBSD'


# Generated at 2022-06-13 04:15:58.655072
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    openbsd = OpenBSDVirtual()
    facts = {}

    # If a virtualization technology is detected two vars are set:
    #   virtualization_type: The name of the type of virtualization
    #   virtualization_role: If the host is a host or a guest
    dmesg_boot = '''
    Hyper-V Generic Cpu Svm Release: 2.0
    Hyper-V Enlightened Data Path: not supported
    '''

    facts['dmesg_boot'] = dmesg_boot
    v_facts = openbsd.get_virtual_facts(facts)
    assert v_facts['virtualization_type'] == 'hyperv'
    assert v_facts['virtualization_role'] == 'host'
    assert v_facts['virtualization_tech_guest'] == set()

# Generated at 2022-06-13 04:16:06.943772
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    openbsd_virtual_obj = OpenBSDVirtual()
    result = openbsd_virtual_obj.get_virtual_facts()
    assert(result['virtualization_type'] == '')
    assert(result['virtualization_role'] == '')
    assert(result['virtualization_product'] == '')
    assert(result['virtualization_system'] == '')
    assert(result['virtualization_tech_host'] == set())
    assert(result['virtualization_tech_guest'] == set())

# Generated at 2022-06-13 04:16:09.934567
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    openbsd_virtual_collector = OpenBSDVirtualCollector()
    assert type(openbsd_virtual_collector._platform) is str
    assert isinstance(openbsd_virtual_collector._fact_class, OpenBSDVirtual)

# Generated at 2022-06-13 04:16:11.258218
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    assert OpenBSDVirtualCollector._fact_class == OpenBSDVirtual
    assert OpenBSDVirtualCollector._platform == 'OpenBSD'

# Generated at 2022-06-13 04:18:31.951793
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # Get the current module
    module = __import__(__name__)
    # Insert a buffer with the dmesg.boot content
    module.Virtual.DMESG_BOOT = 'tests/unit/module_utils/facts/virtual/openbsd/virtual_dmesg.boot'
    openbsd_virtual = module.OpenBSDVirtual()
    # Get the result of method 'get_virtual_facts'
    result = openbsd_virtual.get_virtual_facts()
    # If no virtualization, virtualization type and role are "".
    assert result['virtualization_type'] == ""
    assert result['virtualization_role'] == ""
    # If virtualization_tech_guest is vmm, virtualization_type is vmm.
    assert result['virtualization_tech_guest'] == {"vmm"}

# Generated at 2022-06-13 04:18:35.613736
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    assert OpenBSDVirtualCollector._platform == 'OpenBSD'
    assert OpenBSDVirtualCollector._fact_class == OpenBSDVirtual

# Generated at 2022-06-13 04:18:36.599940
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    assert OpenBSDVirtualCollector._platform == 'OpenBSD'

# Generated at 2022-06-13 04:18:40.502895
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    assert OpenBSDVirtual().get_virtual_facts() == dict(
        virtualization_type='',
        virtualization_role='',
        virtualization_product='',
        virtualization_vendor='',
        virtualization_tech_host=set([]),
        virtualization_tech_guest=set([]),
    )

# Generated at 2022-06-13 04:18:44.187359
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    v = OpenBSDVirtual()
    facts = v.get_virtual_facts()
    assert facts['virtualization_type'] == 'vmm'
    assert facts['virtualization_role'] == 'host'
    assert facts['virtualization_tech_guest'] == set(['vmm', 'vmm'])

# Generated at 2022-06-13 04:18:45.821224
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    assert OpenBSDVirtualCollector()._fact_class is OpenBSDVirtual
    assert OpenBSDVirtualCollector()._platform == 'OpenBSD'

# Generated at 2022-06-13 04:18:48.755916
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virtual_facts = OpenBSDVirtual(module=None).get_virtual_facts()

    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts

    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts

# Generated at 2022-06-13 04:18:50.884330
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virtual_facts = OpenBSDVirtual()
    result = virtual_facts.get_virtual_facts()
    assert 'virtualization_type' in result
    assert 'virtualization_role' in result
    assert 'virtualization_tech_host' in result

# Generated at 2022-06-13 04:19:00.964561
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    ov = OpenBSDVirtual()
    ov.collect()
    virtual_facts = ov.get_virtual_facts()

    # stub_data() returns a dictionary of data if all stubs are enabled
    if ov.stub_data():
        assert 'virtualization_tech_guest' in virtual_facts and virtual_facts['virtualization_tech_guest'] == set(['virtualbox'])
        assert 'virtualization_tech_host' in virtual_facts and virtual_facts['virtualization_tech_host'] == set()
        assert 'virtualization_type' in virtual_facts and virtual_facts['virtualization_type'] == 'virtualbox'
        assert 'virtualization_role' in virtual_facts and virtual_facts['virtualization_role'] == 'guest'

# Generated at 2022-06-13 04:19:04.510112
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virtual = OpenBSDVirtual(module=None)

    assert virtual.get_virtual_facts() == {
        'virtualization_role': 'host',
        'virtualization_type': 'vmm',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set(['vmm'])}