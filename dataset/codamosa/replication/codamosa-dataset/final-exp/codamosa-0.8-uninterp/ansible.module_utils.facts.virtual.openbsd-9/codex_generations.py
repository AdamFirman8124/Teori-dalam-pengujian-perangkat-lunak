

# Generated at 2022-06-13 04:09:56.178766
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    from ansible_collections.misc.not_a_real_collection.plugins.module_utils.facts import collect_subset

    virtual_facts = OpenBSDVirtualCollector(collect_subset=['virtual']).get_virtual_facts()
    assert virtual_facts == {'virtualization_type': '', 'virtualization_role': ''}

# Generated at 2022-06-13 04:10:08.249434
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    v = OpenBSDVirtual()
    facts = {'ansible_facts': {}}
    facts['ansible_facts']['virtualization_type'] = None

    # Test for no virtualization information
    facts['ansible_facts']['virtualization_type'] = None
    facts['ansible_facts']['virtualization_role'] = None
    facts['ansible_facts']['virtualization_tech_guest'] = set()
    facts['ansible_facts']['virtualization_tech_host'] = set()
    v.get_virtual_facts(facts)
    assert facts['ansible_facts']['virtualization_type'] == ''
    assert facts['ansible_facts']['virtualization_role'] == ''
    assert facts['ansible_facts']['virtualization_tech_guest'] == set()

# Generated at 2022-06-13 04:10:19.295341
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    openbsd_virtual_facts = OpenBSDVirtual()
    openbsd_virtual_facts.collect_sysctl_facts = lambda: {
        'hw.product': 'BHYVE',
        'hw.vendor': 'BHYVE'
    }
    host_virtual_facts = openbsd_virtual_facts.get_virtual_facts()
    assert host_virtual_facts['virtualization_type'] == 'vmm', \
        "Type of Virtualization is not vmm."
    assert host_virtual_facts['virtualization_role'] == 'guest', \
        "Role of Virtualization is not guest."
    assert 'vmm' in host_virtual_facts['virtualization_tech_guest'], \
        "vmm is not in list of technologies."

# Generated at 2022-06-13 04:10:26.500905
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virtual_fact_instance = OpenBSDVirtual()
    virtual_facts_result = virtual_fact_instance.get_virtual_facts()

    assert virtual_facts_result['virtualization_type'] == 'vmm'
    assert virtual_facts_result['virtualization_role'] == 'host'
    assert 'vmm' in virtual_facts_result['virtualization_tech_host']
    assert 'vmm' not in virtual_facts_result['virtualization_tech_guest']

# Generated at 2022-06-13 04:10:34.693568
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    openbsd_virtual = OpenBSDVirtual({}, None)
    virtual_facts = {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set(),
        'virtual_product_name': ''
    }

    # No virtualization

# Generated at 2022-06-13 04:10:42.363415
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virtual = OpenBSDVirtual()
    # pylint: disable=protected-access
    # Virtualization facts from product
    virtual._valid_virtualization_products = {
        'OpenBSD': 'VMware, Inc.',
    }
    virtual_facts = virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'VMware'
    assert virtual_facts['virtualization_role'] == 'guest'
    assert 'VMware' in virtual_facts['virtualization_tech_guest']

    # Virtualization facts from vendor
    virtual.hw_vendor = 'OpenBSD'
    virtual_facts = virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'OpenBSD'
    assert virtual_facts['virtualization_role'] == 'host'

# Generated at 2022-06-13 04:10:45.037890
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    c = OpenBSDVirtualCollector()
    assert c.get_virtual_facts()['virtualization_type'] == ''

# Generated at 2022-06-13 04:10:51.152518
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # Set up data for this method
    v = OpenBSDVirtual()
    v.module = ''
    v.sysctl_virtualization = 'not set'

    # Execute method
    virtual_facts = v.get_virtual_facts()

    # Check results
    assert virtual_facts['virtualization_type'] == 'vmm'
    assert virtual_facts['virtualization_role'] == 'host'

# Generated at 2022-06-13 04:10:52.875872
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    try:
        OpenBSDVirtualCollector()
    except:
        assert False
        return
    assert True

# Generated at 2022-06-13 04:11:02.463445
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    openbsd_virtual = OpenBSDVirtual()
    virtual_facts = openbsd_virtual.get_virtual_facts()
    assert isinstance(virtual_facts, dict)
    assert isinstance(virtual_facts['virtualization_type'], basestring)
    assert virtual_facts['virtualization_type'] in ['virtualbox', '', 'vmm']
    assert virtual_facts['virtualization_role'] in ['host']
    assert isinstance(virtual_facts['virtualization_tech_guest'], set)
    assert isinstance(virtual_facts['virtualization_tech_host'], set)
    assert 'amd_vm' not in virtual_facts['virtualization_tech_host']
    assert 'vmm' in virtual_facts['virtualization_tech_host']

# Generated at 2022-06-13 04:11:14.433916
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # test OpenBSDVirtual.get_virtual_facts
    # Initialize OpenBSDVirtual object
    openbsd_virtual_obj = OpenBSDVirtual()

    # Test get_virtual_facts method
    facts = openbsd_virtual_obj.get_virtual_facts()
    assert facts == {'hw_product': '', 'hw_vendor': '', 'virtualization_type': '', 'virtualization_role': '', 'virtualization_tech_guest': set(), 'virtualization_tech_host': set()}

# Generated at 2022-06-13 04:11:22.784581
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # Arguments to the OpenBSDVirtual constructor
    facts = {}
    facts['kernel'] = 'OpenBSD'

    # Global options to the OpenBSDVirtual class
    options = {}

    # Instance of the OpenBSDVirtual class
    openbsd_virtual = OpenBSDVirtual(facts, options)

    # Test when nothing is detected
    virtual_facts = openbsd_virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''

    # Test with the vmm(4) driver detected
    openbsd_virtual.DMESG_BOOT = 'test/unit/files/dmesg.boot'
    virtual_facts = openbsd_virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'vmm'

# Generated at 2022-06-13 04:11:31.882427
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # Create a test object
    openbsd_virtual_obj = OpenBSDVirtual()

    # Return values
    expected_virtual_facts = {
        'virtualization_type': 'vmm',
        'virtualization_role': 'guest',
        'virtualization_tech_guest': set(['hvm']),
        'virtualization_tech_host': set(['vmm']),
        'virtual_product': 'VirtualBox',
        'virtual_product_version': '5.1',
        'virtual_product_serial': '0',
        'virtual_vendor': 'Oracle',
        'virtual_vendor_version': '5.1.18r114002'
    }

    # Create a fake file to read

# Generated at 2022-06-13 04:11:33.842528
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    v = OpenBSDVirtualCollector('OpenBSD')
    assert v.platform == 'OpenBSD'
    assert v.__class__._fact_class == OpenBSDVirtual
    assert v.__class__._platform == 'OpenBSD'



# Generated at 2022-06-13 04:11:42.517428
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # create an OpenBSDVirtual object and call get_virtual_facts
    o = OpenBSDVirtual({})
    facts = o.get_virtual_facts()

    # test the returned result
    # type
    assert 'virtualization_type' in facts
    assert 'virtualization_role' in facts
    assert 'virtualization_system' in facts
    assert 'virtualization_hypervisor' in facts
    assert 'virtualization_product_name' in facts
    assert 'virtualization_product_version' in facts
    assert 'virtualization_product_serial' in facts
    assert 'virtualization_product_uuid' in facts
    assert 'virtualization_product_family' in facts
    assert 'virtualization_product_vendor' in facts
    # value
    assert facts['virtualization_type'] == 'vmm'

# Generated at 2022-06-13 04:11:49.630455
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virtual = OpenBSDVirtual()
    facts = virtual.get_virtual_facts()

    assert facts['virtualization_type'] == 'vmm'
    assert facts['virtualization_role'] == 'host'
    assert facts['virtualization_tech_guest'] == set(['vmm', 'vmm'])
    assert facts['virtualization_tech_host'] == set(['vmm'])
    assert facts['virtualization_product_name'] == 'VMM'
    assert facts['virtualization_product_version'] == 'VMM 1.0'

# Generated at 2022-06-13 04:11:57.292180
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    """ This function performs unit test for method get_virtual_facts """
    bsd = OpenBSDVirtual()
    virtual_facts = bsd.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'vmm'
    assert virtual_facts['virtualization_role'] == 'host'
    assert virtual_facts['virtualization_tech_guest'] == set()
    assert virtual_facts['virtualization_tech_host'] == {'vmm'}

# Generated at 2022-06-13 04:12:09.670615
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    #
    # Conditions that should return an empty dict
    #
    assert OpenBSDVirtual().get_virtual_facts() == {}

    #
    # Conditions that should return the virtual_facts dict
    #
    # Host capable of virtualization
    assert OpenBSDVirtual(content={'hw.vendor': 'OpenBSD', 'hw.product': 'Generic x86'}).get_virtual_facts() == {
        'virtualization_tech_host': {'vmm'},
        'virtualization_tech_guest': {},
        'virtualization_role': 'host',
        'virtualization_type': 'vmm',
        'virtualization_system': '',
        'virtualization_product_version': ''
    }


# Generated at 2022-06-13 04:12:14.860113
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virtual_facts_data = dict(
        virtualization_type='xen',
        virtualization_role='guest',
        virtualization_tech_guest='xen',
        virtualization_tech_host='xen',
    )
    virtual = OpenBSDVirtual()
    dict_to_check = virtual.get_virtual_facts()
    for key, val in virtual_facts_data.items():
        assert val == dict_to_check[key]

# Generated at 2022-06-13 04:12:21.410368
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():

    virtual_facts = {'virtualization_role': 'guest',
                     'virtualization_type': 'vmm',
                     'virtualization_technologies': ['vmm'],
                     'virtualization_tech_host': ['vmm'],
                     'virtualization_tech_guest': ['vmm']}

    class Collector(object):
        fact_class = OpenBSDVirtual

    collector = Collector()
    klass = OpenBSDVirtual
    klass.collector = collector
    instance = OpenBSDVirtual()
    assert instance.get_virtual_facts() == virtual_facts

# Generated at 2022-06-13 04:12:44.648567
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virtual_facts = {}
    virtual = OpenBSDVirtual(module=None)

    vmm_dmesg_boot = ['vmm0 at mainbus0: SVM/RVI']
    xenhvm_dmesg_boot = ['xenhvm0 at mainbus0: using VT-x']
    host_tech_list = ['vmm', 'xenhvm']
    guest_tech_list = []
    virtual_type = 'OpenBSD'
    virtual_role = 'host'

    def mock_get_file_content(file_path, default=None):
        if file_path == OpenBSDVirtual.DMESG_BOOT:
            return '\n'.join(vmm_dmesg_boot)

    virtual._get_file_content = mock_get_file_content
    virtual_facts = virtual.get_virtual

# Generated at 2022-06-13 04:12:46.131715
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    assert issubclass(OpenBSDVirtualCollector, VirtualCollector)

# Generated at 2022-06-13 04:12:56.539480
# Unit test for method get_virtual_facts of class OpenBSDVirtual

# Generated at 2022-06-13 04:13:07.101650
# Unit test for method get_virtual_facts of class OpenBSDVirtual

# Generated at 2022-06-13 04:13:11.425815
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    openbsd_virtual_collector = OpenBSDVirtualCollector()
    assert openbsd_virtual_collector.platform == OpenBSDVirtual._platform

# Generated at 2022-06-13 04:13:19.777461
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    import platform

    # Initialize the OpenBSDVirtual objects
    virtual_obj = OpenBSDVirtualCollector()
    virtual_fact = virtual_obj.get_virtual_facts()

    sysname, nodename, release, version, machine, processor = platform.uname()

    # Check the returned value for 'virtualization_type'
    if sysname == 'OpenBSD':
        if virtual_fact['virtualization_type'] == '':
            error_msg = "Virtualization type is not detected properly"
            raise AssertionError(error_msg)

    # Check the value of 'virtualization_role'
    if virtual_fact['virtualization_type'] != '':
        if virtual_fact['virtualization_role'] == '':
            error_msg = "Virtualization role is not detected properly"
            raise AssertionError(error_msg)



# Generated at 2022-06-13 04:13:25.913485
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    assert OpenBSDVirtualCollector._platform == 'OpenBSD'
    assert OpenBSDVirtualCollector._fact_class == OpenBSDVirtual
    collector = OpenBSDVirtualCollector()
    assert collector._platform == 'OpenBSD'
    assert collector._fact_class == OpenBSDVirtual
    assert collector.platform == 'OpenBSD'
    assert collector.fact_class == OpenBSDVirtual
    assert collector.fact_class().__class__ == OpenBSDVirtual


# Generated at 2022-06-13 04:13:28.008825
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    openbsd_vc = OpenBSDVirtualCollector()
    assert openbsd_vc.platform == 'OpenBSD'
    assert openbsd_vc._fact_class == OpenBSDVirtual

# Generated at 2022-06-13 04:13:37.945018
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    expected_facts = {'virtualization_type': 'vmm', 'virtualization_role': 'host',
                      'virtualization_tech_guest': set(), 'virtualization_tech_host': {'vmm'},
                      'virtualization_product': '', 'virtualization_system': ''}
    expected_facts_new = {'virtualization_type': 'vmm', 'virtualization_role': 'host',
                      'virtualization_tech_guest': {'vmm'}, 'virtualization_tech_host': {'vmm', 'jail'},
                      'virtualization_product': '', 'virtualization_system': ''}
    new_facts = OpenBSDVirtual().__init__(None).get_virtual_facts()

    if new_facts['virtualization_tech_guest'] != set():
        assert new_facts == expected

# Generated at 2022-06-13 04:13:47.206679
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # Create expected values
    expected_virtual_facts = dict()
    expected_virtual_facts['virtualization_type'] = 'vmm'
    expected_virtual_facts['virtualization_role'] = 'host'
    expected_virtual_facts['virtualization_tech_host'] = {'vmm'}
    expected_virtual_facts['virtualization_tech_guest'] = set()
    expected_virtual_facts['virtualization_product_name'] = ''
    expected_virtual_facts['virtualization_product_version'] = ''
    expected_virtual_facts['virtualization_product_default'] = ''
    # Check the virtual facts
    openbsd_virtual = OpenBSDVirtual()
    virtual_facts = openbsd_virtual.get_virtual_facts()

# Generated at 2022-06-13 04:14:16.898790
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    openbsd_virtual_facts = OpenBSDVirtual()
    assert isinstance(openbsd_virtual_facts.get_virtual_facts(), dict)

# Generated at 2022-06-13 04:14:25.313307
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    fake_sysctl_values = {
        'hw.vendor': 'OpenBSD',
        'hw.product': 'ProBook 440 G2'}
    fake_readlines = [
        'vmm0 at mainbus0: SVM/RVI'
        ]

    openbsd_virtual = OpenBSDVirtual()
    openbsd_virtual.collect_sysctl_facts = lambda: fake_sysctl_values
    openbsd_virtual._read_lines_from_file = lambda filename: fake_readlines
    virtual_facts = openbsd_virtual.get_virtual_facts()

    assert virtual_facts['virtualization_type'] == 'vmm'
    assert virtual_facts['virtualization_role'] == 'host'
    assert virtual_facts['virtualization_technologies'] == {'vmm'}

# Generated at 2022-06-13 04:14:31.485760
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    ansible_module = MockAnsibleModule()
    openbsd_virtual = OpenBSDVirtual(ansible_module)

    # Mock dmesg, hw.product and hw.vendor sysctl variables
    # Run get_virtual_facts() and assert correct results
    dmesg_boot = 'vmm0 at mainbus0: SVM/RVI'
    hw_product = 'VMWARE,VMWARE Virtual Platform'
    hw_vendor = 'QEMU'
    openbsd_virtual.get_sysctl_output.side_effect = [
        {
            'dmesg.boot': dmesg_boot,
            'hw.product': hw_product,
            'hw.vendor': hw_vendor
        }
    ]

# Generated at 2022-06-13 04:14:41.415139
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    options = dict()
    OpenBSDVirtualMix = OpenBSDVirtual(options)
    virtual_facts = OpenBSDVirtualMix.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''
    assert virtual_facts['virtualization_product_name'] == ''
    assert virtual_facts['virtualization_product_version'] == ''
    assert virtual_facts['virtualization_product_serial'] == ''
    assert virtual_facts['virtualization_sysctl_name'] == ''
    assert virtual_facts['virtualization_sysctl_value'] == ''
    assert not virtual_facts['virtualization_tech_guest']
    assert not virtual_facts['virtualization_tech_host']

# Generated at 2022-06-13 04:14:52.492428
# Unit test for method get_virtual_facts of class OpenBSDVirtual

# Generated at 2022-06-13 04:14:57.583458
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    openbsd_facts = OpenBSDVirtualCollector(None, None, None, None).collect()
    assert 'virtualization_type' in openbsd_facts
    assert 'virtualization_role' in openbsd_facts
    assert 'virtualization_technologies' in openbsd_facts
    assert 'virtualization_technologies_guest' in openbsd_facts
    assert 'virtualization_technologies_host' in openbsd_facts

# Generated at 2022-06-13 04:15:07.584906
# Unit test for method get_virtual_facts of class OpenBSDVirtual

# Generated at 2022-06-13 04:15:08.967280
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    t = OpenBSDVirtualCollector()
    assert t is not None

# Generated at 2022-06-13 04:15:11.959331
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    fact_class = OpenBSDVirtual({})
    virtual_facts = fact_class.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == ''

# Generated at 2022-06-13 04:15:22.007120
# Unit test for method get_virtual_facts of class OpenBSDVirtual

# Generated at 2022-06-13 04:16:25.635039
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    test_virtual_get_virtual_facts(OpenBSDVirtual)

# Generated at 2022-06-13 04:16:26.197972
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    pass



# Generated at 2022-06-13 04:16:36.715294
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # Unit test for method get_virtual_facts of class OpenBSDVirtual when
    # running on OpenBSD inside VMware Desktop
    hw_vendor = 'GenuineIntel'
    hw_product = 'QEMU Virtual CPU version 2.5+'
    virtualsysctl = {'hw.vendor': hw_vendor,
                     'hw.product': hw_product,
                     'hw.vendor_id': hw_vendor,
                     'hw.product_id': hw_product}
    dmesgboot = ''

    virtual_facts = OpenBSDVirtual.get_virtual_facts(virtualsysctl,
                                                     dmesgboot)
    assert virtual_facts['virtualization_type'] == 'vmware'
    assert virtual_facts['virtualization_role'] == 'guest'

# Generated at 2022-06-13 04:16:47.547216
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    """
    Check if output of method get_virtual_facts of class OpenBSDVirtual
    matches exactly with reference value
    """
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from utils.platform import Platform

    platform = Platform()
    platform.populate_facts()

    virtual = OpenBSDVirtual()
    virtual_facts = virtual.get_virtual_facts()
    reference_dict = {'virtualization_type': '',
                      'virtualization_role': '',
                      'virtualization_tech_host': {},
                      'virtualization_tech_guest': {}}
    assert virtual_facts == reference_dict


# Generated at 2022-06-13 04:16:56.802747
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    spec = dict(
        last_path_component='OpenBSDVirtual.py',
        command_callable=None
    )

    # Get an instance of OpenBSDVirtual
    openBSDVirtual = OpenBSDVirtual(spec)

    # Get the virtual facts from the instance
    facts = openBSDVirtual.get_virtual_facts()

    print("Virtualization facts: \n")
    print(facts)
    print("\n")

    # Testing the virtualization type
    assert facts['virtualization_type'] != ''

    # Testing the virtualization role
    assert facts['virtualization_role'] != ''

# Generated at 2022-06-13 04:17:07.456100
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    class MyOpenBSDVirtual(OpenBSDVirtual):
        def __init__(self):
            self.facts = {}
            self.facts['virtualization_type'] = ''
            self.facts['virtualization_role'] = ''
            self.facts['virtualization_product_name'] = ''
            self.facts['virtualization_product_version'] = ''
            self.facts['virtualization_product_serial'] = ''
            self.facts['virtualization_product_uuid'] = ''
            self.facts['virtualization_tech_guest'] = set()
            self.facts['virtualization_tech_host'] = set()

    openbsd_virtual = MyOpenBSDVirtual()

# Generated at 2022-06-13 04:17:18.018721
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():

    # hw.vendor match:
    hw_vendor = 'Is This A HAT?  It Is!  HATs are for Everyone  ('
    sut = OpenBSDVirtual()
    sut.facts = {'hw.vendor': hw_vendor}
    facts = sut.get_virtual_facts()
    assert facts['virtualization_type'] == ''
    assert facts['virtualization_role'] == ''
    assert facts['virtualization_tech_guest'] == set(['hyperv'])
    assert facts['virtualization_tech_host'] == set(['hyperv'])

    # hw.vendor match:
    hw_vendor = 'Raspberry Pi Foundation'
    sut = OpenBSDVirtual()
    sut.facts = {'hw.vendor': hw_vendor}
   

# Generated at 2022-06-13 04:17:20.330447
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    virtual = OpenBSDVirtualCollector()
    assert isinstance(virtual, VirtualCollector)
    assert virtual._fact_class.platform == 'OpenBSD'

# Generated at 2022-06-13 04:17:25.647166
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # Create an instance of OpenBSDVirtual
    collect_obj = OpenBSDVirtualCollector()

    # Call method get_virtual_facts
    result = collect_obj.get_virtual_facts()

    # Check if 'virtualization_type' is a key in the result
    assert 'virtualization_type' in result.keys()

    # Check if 'virtualization_role' is a key in the result
    assert 'virtualization_role' in result.keys()

    # Check if 'virtualization_tech_guest' is a key in the result
    assert 'virtualization_tech_guest' in result.keys()

    # Check if 'virtualization_tech_host' is a key in the result
    assert 'virtualization_tech_host' in result.keys()

# Generated at 2022-06-13 04:17:28.965868
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    collector = OpenBSDVirtualCollector()
    assert(isinstance(collector, OpenBSDVirtualCollector))
    assert(collector.platform == 'OpenBSD')
    assert(collector._fact_class == OpenBSDVirtual)
    assert(collector._fact_class().platform == 'OpenBSD')

# Generated at 2022-06-13 04:18:44.225953
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    a = OpenBSDVirtualCollector()
    assert a._platform == 'OpenBSD'
    assert a._fact_class == OpenBSDVirtual


# Generated at 2022-06-13 04:18:51.066004
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # Set up a OpenBSDVirtual object
    openbsd_virtual = OpenBSDVirtual()

    # Run get_virtual_facts and get the result
    result = openbsd_virtual.get_virtual_facts()

    # Make sure the expected keys are present in the result
    assert all(item in result for item in ['virtualization_type', 'virtualization_role'])
    assert all(item in result for item in ['virtualization_tech_guest', 'virtualization_tech_host'])

    # Check if the keys have the correct type
    assert type(result['virtualization_type']) is str
    assert type(result['virtualization_role']) is str
    assert type(result['virtualization_tech_guest']) is set
    assert type(result['virtualization_tech_host']) is set

# Generated at 2022-06-13 04:19:01.201552
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.openbsd import OpenBSDVirtual
    from ansible.module_utils.facts.virtual import Virtual, VirtualCollector
    from ansible.module_utils.facts.virtual.sysctl import VirtualSysctlDetectionMixin

    # The following lines are the sample content of dmesg.boot
    # They are used for testing.

# Generated at 2022-06-13 04:19:04.435574
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # Construct the class object
    obj = OpenBSDVirtual()

    # Return value of get_virtual_facts
    return_value = obj.get_virtual_facts()

    # Check the type of return value
    assert isinstance(return_value, dict)



# Generated at 2022-06-13 04:19:11.619371
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    from ansible_collections.ansible.misc.tests.unit.compat.mock import patch

    patch.object(Virtual, 'get_cached_facts',
                 side_effect=Virtual.get_cached_facts)

    patch.object(Virtual, '_get_cmdline',
                 side_effect=Virtual._get_cmdline)

    patch.object(get_file_content, 'get_file_content',
                 return_value='')

    virt = OpenBSDVirtual()
    virtual_facts = virt.get_virtual_facts()

    assert isinstance(virtual_facts['virtualization_type'], str)
    assert isinstance(virtual_facts['virtualization_role'], str)
    assert isinstance(virtual_facts['virtualization_tech_guest'], set)

# Generated at 2022-06-13 04:19:13.302700
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    try:
        OpenBSDVirtualCollector()
    except Exception as e:
        assert(False)


# Generated at 2022-06-13 04:19:15.320484
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    # pylint: disable=protected-access
    assert OpenBSDVirtualCollector._platform == 'OpenBSD'

# Generated at 2022-06-13 04:19:18.242677
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    """
    Runs a unit test on the constructor of class OpenBSDVirtualCollector.
    """
    obj = OpenBSDVirtualCollector()
    assert obj.platform == 'OpenBSD'

# Generated at 2022-06-13 04:19:21.741914
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    from ansible.module_utils import basic
    from ansible.module_utils.facts import collector

    module = basic.AnsibleModule(
        argument_spec = dict()
    )
    facts_collector = collector.get_collector(module)
    virtual = facts_collector.get_virtual_facts()
    assert 'virtualization_type' in virtual

# Generated at 2022-06-13 04:19:31.732406
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virt_type = ['vmm']
    virt_role = 'host'
    expected = {
        'virtualization_type': 'vmm',
        'virtualization_role': 'host',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set(virt_type)
    }
    dmesg = "vmm0 at mainbus0: SVM/RVI\n"
    OpenBSDVirtual.DMESG_BOOT = '/tmp/dmesg.boot'
    open(OpenBSDVirtual.DMESG_BOOT, 'w').write(dmesg)

    openbsd_virtual = OpenBSDVirtual()
    facts = openbsd_virtual.get_virtual_facts()
    assert facts == expected
