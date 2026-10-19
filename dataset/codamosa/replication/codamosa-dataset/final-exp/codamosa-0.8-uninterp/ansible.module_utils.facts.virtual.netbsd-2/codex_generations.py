

# Generated at 2022-06-13 04:10:00.721675
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    netbsd_virtual_obj = NetBSDVirtual()
    test_result = netbsd_virtual_obj.get_virtual_facts()
    assert test_result['virtualization_type'] == ''
    assert test_result['virtualization_role'] == ''
    assert test_result['virtualization_tech_guest'] == set()
    assert test_result['virtualization_tech_host'] == set()

    netbsd_virtual_obj.sysctl = {'machdep.hypervisor': 'QEMU',
                                 'machdep.dmi.system-product': 'KVM',
                                 'machdep.dmi.system-vendor': 'Acme'}
    test_result = netbsd_virtual_obj.get_virtual_facts()

# Generated at 2022-06-13 04:10:02.156761
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    assert issubclass(NetBSDVirtualCollector, VirtualCollector)

# Generated at 2022-06-13 04:10:05.224881
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    virtual_collector = NetBSDVirtualCollector()
    assert virtual_collector._platform == 'NetBSD'
    assert virtual_collector._fact_class.__name__ == 'NetBSDVirtual'


# Generated at 2022-06-13 04:10:08.695190
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual_obj = NetBSDVirtual()
    virtual_obj._get_sysctl = MagicMock(return_value='QEMU')

    assert virtual_obj.platform == 'NetBSD'
    assert virtual_obj.get_virtual_facts() == {'virtualization_role': 'guest', 'virtualization_type': 'xen'}

# Generated at 2022-06-13 04:10:10.978849
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual_facts = NetBSDVirtual()
    assert virtual_facts.get_virtual_facts() == {
        'virtualization_role': '',
        'virtualization_type': '',
        'virtualization_technology_guest': [],
        'virtualization_technology_host': [],
    }

# Generated at 2022-06-13 04:10:12.119486
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    NetBSDVirtualCollector()

# Generated at 2022-06-13 04:10:13.681411
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    return_value = NetBSDVirtualCollector()
    assert return_value._platform == 'NetBSD'

# Generated at 2022-06-13 04:10:20.682284
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual = NetBSDVirtual()
    virtual_facts = virtual.get_virtual_facts()

    # This is a known VM
    assert virtual_facts['virtualization_type'] == 'xen'
    assert virtual_facts['virtualization_role'] == 'guest'
    assert 'xen' in virtual_facts['virtualization_tech_guest']
    assert virtual_facts['virtualization_tech_host'] == set()

# Generated at 2022-06-13 04:10:30.656110
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():

    # Initialise the class and its parent
    facts_object = NetBSDVirtual()
    facts_object.collect_platform_subset_facts = lambda *args, **kwargs: dict()

    # Set the values to be returned by the mocked methods and functions
    # syctl.filter returns lines containing all keys of the output dictionary

# Generated at 2022-06-13 04:10:32.906081
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    obj = NetBSDVirtualCollector()
    assert isinstance(obj, NetBSDVirtualCollector)

# Generated at 2022-06-13 04:10:37.632658
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    c = NetBSDVirtual({}, None)
    assert c != None

# Generated at 2022-06-13 04:10:43.465252
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual_facts = NetBSDVirtual().get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'xen'
    assert virtual_facts['virtualization_role'] == 'guest'
    assert virtual_facts['virtualization_type_role'] == 'guest/xen'
    assert virtual_facts['virtualization_full_facts'] == {'role': 'guest', 'type': 'xen'}

# Generated at 2022-06-13 04:10:45.888013
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual(dict(), dict())
    assert netbsd_virtual.platform == 'NetBSD'


# Generated at 2022-06-13 04:10:48.197389
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual_platform = NetBSDVirtual()
    assert netbsd_virtual_platform.platform == 'NetBSD'


# Generated at 2022-06-13 04:10:53.726372
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual_facts = {}
    # Check that the type of the first argument is NetBSDVirtual
    assert isinstance(NetBSDVirtual(), NetBSDVirtual)
    # Make sure get_virtual_facts is called
    virtual_facts = NetBSDVirtual('/usr/bin/sysctl')
    assert virtual_facts['virtualization_type'] == "openvz"
    assert virtual_facts['virtualization_role'] == "guest"

# Generated at 2022-06-13 04:10:56.995555
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual({})
    assert netbsd_virtual.__class__.__name__ == "NetBSDVirtual"
    assert netbsd_virtual._platform == "NetBSD"


# Generated at 2022-06-13 04:10:58.029640
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    # FIXME: add unit test
    pass

# Generated at 2022-06-13 04:11:01.804549
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    fixture = {
        'machdep.dmi.system-product': 'VirtualBox',
        'machdep.dmi.system-vendor': 'innotek GmbH',
        'machdep.hypervisor': 'Xen',
    }
    result = {}
    result['virtualization_type'] = 'virtualbox'
    result['virtualization_role'] = 'guest'
    result['virtualization_tech_guest'] = set(['virtualbox'])
    result['virtualization_tech_host'] = set([])
    test_obj = NetBSDVirtual(fixture, result)
    assert test_obj.get_virtual_facts() == result

# Generated at 2022-06-13 04:11:02.983039
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    myNetBSDVirtualCollector = NetBSDVirtualCollector()
    assert myNetBSDVirtualCollector._fact_class == NetBSDVirtual
    assert myNetBSDVirtualCollector._platform == 'NetBSD'


# Generated at 2022-06-13 04:11:14.509337
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():

    # Create a NetBSDVirtual object
    test_obj = NetBSDVirtual()

    # Populate the 'machdep.dmi.system-vendor' and 'machdep.dmi.system-product'
    # sysctl properties with valid values
    host_vendor = 'VMware, Inc.'
    host_product = 'VMware Virtual Platform'
    test_obj.sysctl_properties['machdep.dmi.system-vendor'] = host_vendor
    test_obj.sysctl_properties['machdep.dmi.system-product'] = host_product

    # Populate the 'machdep.hypervisor' sysctl property with an invalid value
    hypervisor_type = 'none'
    test_obj.sysctl_properties['machdep.hypervisor'] = hypervisor_type

    # Create the expected dictionary

# Generated at 2022-06-13 04:11:19.052878
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    # Returned not empty dict
    assert NetBSDVirtual().get_virtual_facts()

# Generated at 2022-06-13 04:11:20.000634
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    NetBSDVirtualCollector()

# Generated at 2022-06-13 04:11:26.145813
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    from ansible.module_utils.facts.virtual.netbsd import NetBSDVirtual
    virtual = NetBSDVirtual()
    assert virtual.platform =='NetBSD'
    assert virtual.get_virtual_facts() == {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set(),
    }

# Generated at 2022-06-13 04:11:28.398987
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual_host_facts = NetBSDVirtual()
    assert virtual_host_facts.platform == 'NetBSD'


# Generated at 2022-06-13 04:11:40.130334
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    #
    # Test on a system running in a VirtualBox VM
    #
    dmi_output = [
        'dmi.system.vendor: innotek GmbH',
        'dmi.system.product: VirtualBox',
        'machdep.hypervisor: VirtualBox',
    ]
    sysctl_output = [
        'machdep.dmi.system-vendor: innotek GmbH',
        'machdep.dmi.system-product: VirtualBox',
        'machdep.dmi.system-version: 1.2-78657',
    ]

    netbsd_virtual = NetBSDVirtual(dmi_output, sysctl_output)
    virtual_facts = netbsd_virtual.get_virtual_facts()


# Generated at 2022-06-13 04:11:48.796896
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    # create empty class for testing method
    test_class = NetBSDVirtual()

    # run method get_virtual_facts of class DarwinVirtual
    fact_virt_dict = test_class.get_virtual_facts()

    assert isinstance(fact_virt_dict, dict), "Returned result is not instance of dict."
    assert 'virtualization_type' in fact_virt_dict, "Returned result doesn't contain 'virtualization_type'."
    assert 'virtualization_role' in fact_virt_dict, "Returned result doesn't contain 'virtualization_role'."


# Generated at 2022-06-13 04:11:58.173862
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    netbsd_virtual_collector = NetBSDVirtualCollector()
    assert netbsd_virtual_collector.platform == 'NetBSD'
    assert isinstance(netbsd_virtual_collector._fact_class, NetBSDVirtual)
    assert set(netbsd_virtual_collector.files) == set([
        '/proc/cpuinfo',
        '/proc/self/status',
        '/proc/version',
        '/sys/devices/virtual/dmi/id/product_name',
        '/sys/devices/virtual/dmi/id/sys_vendor',
        '/sysctl'
    ])

# Generated at 2022-06-13 04:12:01.522823
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    netbsd = NetBSDVirtualCollector()
    assert netbsd.platform == 'NetBSD'
    assert netbsd._fact_class == NetBSDVirtual



# Generated at 2022-06-13 04:12:06.909043
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    import unittest

    class MyTestCase(unittest.TestCase):
        def setUp(self):
            self.netbsd_virtual = NetBSDVirtual()

    mytestcase = MyTestCase()
    mytestcase.setUp()
    mytestcase.assertEqual(mytestcase.netbsd_virtual.platform, 'NetBSD')

# Generated at 2022-06-13 04:12:08.771593
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual_facts = NetBSDVirtual()
    assert virtual_facts.platform == 'NetBSD'


# Generated at 2022-06-13 04:12:16.560154
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    NetBSDVirtual('NetBSD')

# Generated at 2022-06-13 04:12:18.492292
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    assert(NetBSDVirtualCollector._platform == 'NetBSD')
    assert(NetBSDVirtualCollector._fact_class == NetBSDVirtual)

# Generated at 2022-06-13 04:12:29.145014
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    hypervisor_product_facts = {'machdep.dmi.system-product': '9000v'}
    hypervisor_vendor_facts = {'machdep.dmi.system-vendor': 'HPE', 'machdep.hypervisor': 'HPE'}
    empty_facts = {}
    facts_list = [hypervisor_product_facts, hypervisor_vendor_facts, empty_facts]
    expected_output = {'virtualization_type': 'HPVM', 'virtualization_role': 'guest',
                       'virtualization_tech_guest': {'HPVM'}, 'virtualization_tech_host':
                       {'HPVM'}}

    output = NetBSDVirtual(facts_list).get_virtual_facts()
    assert output == expected_output

# Generated at 2022-06-13 04:12:30.923611
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual()

    assert netbsd_virtual.platform == 'NetBSD'


# Generated at 2022-06-13 04:12:35.658408
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    netbsd_virtual = NetBSDVirtual()
    virtual_facts = netbsd_virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] in ['', 'kvm']
    assert virtual_facts['virtualization_role'] in ['', 'guest']

# Generated at 2022-06-13 04:12:41.453968
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual()
    assert netbsd_virtual.platform == 'NetBSD'
    assert netbsd_virtual.virtualization_type == ''
    assert netbsd_virtual.virtualization_role == ''
    assert netbsd_virtual.virtualization_tech_guest == set()
    assert netbsd_virtual.virtualization_tech_host == set()

# Generated at 2022-06-13 04:12:43.557945
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual({}, {}, {})
    assert netbsd_virtual.platform == 'NetBSD'

# Generated at 2022-06-13 04:12:46.751748
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    netbsd_virtual_facts = NetBSDVirtual(None).get_virtual_facts()
    assert netbsd_virtual_facts['virtualization_type'] == ''
    assert netbsd_virtual_facts['virtualization_role'] == ''

# Generated at 2022-06-13 04:12:52.261034
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    # Create a NetBSDVirtual object
    netbsd_virtual_obj = NetBSDVirtual()

    # Check the virtualization_type value
    assert netbsd_virtual_obj.get_virtual_facts()['virtualization_type'] == ''

    # Check the virtualization_role value
    assert netbsd_virtual_obj.get_virtual_facts()['virtualization_role'] == ''

# Generated at 2022-06-13 04:12:54.296539
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    netbsd_virtual = NetBSDVirtual()
    netbsd_virtual.get_virtual_facts()

# Generated at 2022-06-13 04:13:10.345091
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    test_NetBSDVirtual = NetBSDVirtualCollector()
    assert test_NetBSDVirtual._fact_class == NetBSDVirtual
    assert test_NetBSDVirtual._platform == 'NetBSD'

# Generated at 2022-06-13 04:13:17.085747
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    # Constructor should fail without argument
    try:
        NetBSDVirtual()
    except TypeError:
        pass
    else:
        raise AssertionError("NetBSDVirtual() should have failed without argument")

    # Constructor should fail without argument
    try:
        NetBSDVirtual(None)
    except TypeError:
        pass
    else:
        raise AssertionError("NetBSDVirtual() should have failed without argument")


# Generated at 2022-06-13 04:13:20.581419
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    '''
    Create an instance of NetBSDVirtual
    '''
    netbsd_virtual_obj = NetBSDVirtual()
    assert isinstance(netbsd_virtual_obj, NetBSDVirtual)


# Generated at 2022-06-13 04:13:22.571609
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    netbsd_virtual = NetBSDVirtual()
    assert {} == netbsd_virtual.get_virtual_facts()

# Generated at 2022-06-13 04:13:26.528736
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual_facts = NetBSDVirtual().get_virtual_facts()
    assert virtual_facts['virtualization_role'] == ''
    assert virtual_facts['virtualization_type'] == ''
    assert not virtual_facts['virtualization_tech_guest']
    assert not virtual_facts['virtualization_tech_host']

# Generated at 2022-06-13 04:13:31.082442
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    detect_virt = NetBSDVirtual()
    virtual_facts = detect_virt.get_virtual_facts()

    assert virtual_facts['virtualization_type']
    assert virtual_facts['virtualization_role']
    assert virtual_facts['virtualization_tech_guest']
    assert virtual_facts['virtualization_tech_host']

# Generated at 2022-06-13 04:13:34.265458
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    virtual_collector = NetBSDVirtualCollector()
    assert isinstance(virtual_collector, NetBSDVirtualCollector)
    assert virtual_collector.platform == 'NetBSD'
    assert virtual_collector._fact_class == NetBSDVirtual


# Generated at 2022-06-13 04:13:42.577023
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    facts = NetBSDVirtual({}).get_virtual_facts()
    assert facts['virtualization_type'] == ''
    assert facts['virtualization_role'] == ''
    assert facts['virtualization_system'] == ''
    assert facts['virtualization_uuid'] == ''
    assert facts['virtualization_product_name'] == ''
    assert facts['virtual_product_name'] == ''
    assert facts['virtual_product_version'] == ''
    assert facts['virtual_product_serial'] == ''
    assert facts['virtual_product_uuid'] == ''
    assert facts['virtualization_tech_guest'] == set()
    assert facts['virtualization_tech_host'] == set()


# Generated at 2022-06-13 04:13:44.212863
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    """
    Just check that it instantiates.
    """
    NetBSDVirtual()

# Generated at 2022-06-13 04:13:45.015652
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virt = NetBSDVirtual()
    assert virt is not None

# Generated at 2022-06-13 04:14:19.003831
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual = NetBSDVirtual()
    assert virtual.platform == 'NetBSD'
    assert not bool(virtual)


# Generated at 2022-06-13 04:14:21.561951
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual_collector = NetBSDVirtualCollector()
    assert netbsd_virtual_collector._platform is not None
    assert netbsd_virtual_collector._fact_class is not None

# Generated at 2022-06-13 04:14:29.242885
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    netbsdvirtual = NetBSDVirtual()


# Generated at 2022-06-13 04:14:31.181481
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    my_module = NetBSDVirtual()
    assert(my_module.platform == 'NetBSD')


# Generated at 2022-06-13 04:14:33.478200
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    vc = NetBSDVirtualCollector()
    assert vc._fact_class == NetBSDVirtual
    assert vc._platform == 'NetBSD'

# Generated at 2022-06-13 04:14:35.169063
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    NetBSDVirtualCollector()

# Generated at 2022-06-13 04:14:38.150277
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual = NetBSDVirtual({'ansible_processor': 'sparc64'})
    assert virtual.platform == 'NetBSD'
    assert virtual.machdep['architecture'] == 'sparc64'

# Generated at 2022-06-13 04:14:43.040681
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    return_value = {}
    return_value['virtualization_type'] = 'xen'
    return_value['virtualization_role'] = 'guest'
    return_value['virtualization_tech_host'] = 'xen'
    return_value['virtualization_tech_guest'] = 'xen'
    obj = NetBSDVirtual()
    assert obj.get_virtual_facts() == return_value

# Generated at 2022-06-13 04:14:46.461977
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    test = NetBSDVirtual()
    test_facts = {'virtualization_type': '', 'virtualization_role': ''}
    returned_facts = test.get_virtual_facts()
    assert returned_facts == test_facts

# Generated at 2022-06-13 04:14:51.328264
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual_facts = VirtualCollector._collect_platform_facts(NetBSDVirtual)
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts

# Generated at 2022-06-13 04:15:56.010431
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    v = NetBSDVirtual()
    assert v.fact_class == NetBSDVirtual
    assert v.platform == 'NetBSD'



# Generated at 2022-06-13 04:15:58.291207
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual()
    assert netbsd_virtual != None
    assert netbsd_virtual.platform == 'NetBSD'

# Generated at 2022-06-13 04:16:07.615718
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    # run_tests is defined in the base class
    # pylint: disable=protected-access
    ansible_facts = dict()
    facts_instance = VirtualCollector._platforms['NetBSD']()
    facts_instance._populate()
    facts = facts_instance.get_facts()
    for k, v in facts.items():
        ansible_facts[k] = v
    assert ansible_facts['virtualization_type'] == ''
    assert ansible_facts['virtualization_role'] == ''
    assert 'virtualization_tech' in ansible_facts

# Generated at 2022-06-13 04:16:09.148955
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual()
    assert netbsd_virtual.platform == 'NetBSD'

# Generated at 2022-06-13 04:16:18.421087
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    # NetBSD 6.1.5 (GENERIC) running on QEMU
    #
    # machdep.dmi.system-vendor: QEMU
    # machdep.dmi.system-product: Standard PC (i440FX + PIIX, 1996)
    # machdep.hypervisor: QEMU VirtIO Hypervisor
    # machdep.dmi.system-version: pc-i440fx-1.5
    # machdep.dmi.sysvendor: OpenBSD
    # machdep.dmi.product: QEMU Virtual Machine
    # machdep.dmi.board-vendor: QEMU
    # machdep.dmi.product-version: 1.5
    # machdep.dmi.board-version: 0.0

    facts = {}

# Generated at 2022-06-13 04:16:28.450749
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    # Create instance of Virtual
    virtual = NetBSDVirtual()

    # Create test function inputs
    data = dict()

    # Set virtualization_type to VMware ESX
    data['machdep.dmi.system-vendor'] = 'VMware, Inc.'
    data['machdep.dmi.system-product'] = 'VMware Virtual Platform'
    virtual_facts = virtual.get_virtual_facts(data)
    assert virtual_facts['virtualization_type'] == 'VMware'
    assert virtual_facts['virtualization_role'] == 'guest'

    # Set virtualization_type to XEN
    data['machdep.dmi.system-vendor'] = ''
    data['machdep.dmi.system-product'] = ''
    data['machdep.hypervisor'] = 'Xen'
    virtual

# Generated at 2022-06-13 04:16:28.956453
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    NetBSDVirtual()

# Generated at 2022-06-13 04:16:33.583506
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual_facts = NetBSDVirtual().get_virtual_facts()
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts

# Generated at 2022-06-13 04:16:41.171047
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    data = {'machdep.dmi.system-product': 'VirtualBox',
            'machdep.dmi.system-vendor': 'Oracle Corporation',
            'machdep.hypervisor': 'VirtualBox'}
    assert NetBSDVirtual(data).get_virtual_facts()['virtualization_type'] == "virtualbox"
    assert NetBSDVirtual(data).get_virtual_facts()['virtualization_role'] == "guest"
    assert NetBSDVirtual(data).get_virtual_facts()['virtualization_tech'] == {"hypervisor", "virtualbox"}
    assert NetBSDVirtual(data).get_virtual_facts()['virtualization_tech_guest'] == {"hypervisor"}
    assert NetBSDVirtual(data).get_virtual_facts()['virtualization_tech_host'] == {"hypervisor"}

# Generated at 2022-06-13 04:16:43.566673
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    # run unit test when ran standalone (not from Ansible)
    if __name__ == '__main__':
        import doctest
        doctest.testmod()

# Generated at 2022-06-13 04:19:29.802008
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual({})
    assert netbsd_virtual.platform == 'NetBSD'

# Generated at 2022-06-13 04:19:33.909413
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    netbsd_virtual_collector = NetBSDVirtualCollector()
    assert netbsd_virtual_collector._fact_class == NetBSDVirtual
    assert netbsd_virtual_collector._platform == 'NetBSD'


# Generated at 2022-06-13 04:19:43.136250
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    # sysctl_output looks like:
    # machdep.dmi.system-vendor = Xen
    # machdep.dmi.system-product = HVM domU
    sysctl_output = u'''
machdep.dmi.system-vendor = Xen
machdep.dmi.system-product = HVM domU
machdep.hypervisor.guest = NetBSD
machdep.hypervisor.host = vmware
'''
    expected_facts = {
        'virtualization_type': 'vmware',
        'virtualization_role': 'guest',
        'virtualization_technologies': ['xen', 'vmware'],
    }
    result = NetBSDVirtual(context_wrap(sysctl_output)).get_virtual_facts()
    assert result == expected_facts

# Generated at 2022-06-13 04:19:43.963467
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    facts_init = NetBSDVirtual()
    assert isinstance(facts_init, Virtual)

# Generated at 2022-06-13 04:19:44.573087
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    d_ = NetBSDVirtual()


# Generated at 2022-06-13 04:19:48.439905
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    assert issubclass(NetBSDVirtualCollector, VirtualCollector)


# Generated at 2022-06-13 04:19:55.018977
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    fact_dict = {
        'machdep.dmi.system-vendor': 'Parallels Software International Inc.',
        'machdep.dmi.system-product': 'Parallels Virtual Platform',
        'machdep.hypervisor': '',
        }
    res = NetBSDVirtual(fact_dict).get_virtual_facts()
    assert 'virtualization_type' in res
    assert res['virtualization_type'] == 'parallels'
    assert 'virtualization_role' in res
    assert res['virtualization_role'] == 'guest'
    assert 'virtualization_tech_guest' in res
    assert 'virtualization_tech_host' in res
    assert res['virtualization_tech_guest'] == set(['parallels'])