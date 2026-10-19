

# Generated at 2022-06-13 04:09:56.215324
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    assert issubclass(OpenBSDVirtualCollector, VirtualCollector)
    assert OpenBSDVirtualCollector._platform == 'OpenBSD'
    assert OpenBSDVirtualCollector._fact_class == OpenBSDVirtual


# Generated at 2022-06-13 04:10:08.245338
# Unit test for method get_virtual_facts of class OpenBSDVirtual

# Generated at 2022-06-13 04:10:19.273856
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # Set a fake dmesg.boot
    dmesg_boot = ('OpenBSD 6.3-current (GENERIC) #0: Tue Jan  2 22:51:27 UTC 2018\n'
                  '    root@syspatch-64.openbsd.org:/usr/src/sys/arch/amd64/compile/GENERIC\n'
                  'vmm0 at mainbus0: SVM/RVI\n')

    virtual_facts = {'virtualization_tech_guest': set(),
                     'virtualization_tech_host': set(['vmm']),
                     'virtualization_type': 'vmm',
                     'virtualization_role': 'host'}

    with open(OpenBSDVirtual.DMESG_BOOT, 'w') as f:
        f.write(dmesg_boot)

   

# Generated at 2022-06-13 04:10:23.367604
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # pylint: disable=protected-access
    virtual_facts = OpenBSDVirtual().get_virtual_facts()
    assert virtual_facts and virtual_facts.get('virtualization_role'), \
        "Failed to detect OpenBSD virtualization role"

# Generated at 2022-06-13 04:10:24.396575
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    OpenBSDVirtualCollector()

# Generated at 2022-06-13 04:10:33.054313
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virtual = OpenBSDVirtual()
    # Inject some test data into device tree
    virtual._device_tree['hw.product'] = 'OpenBSD'
    virtual._device_tree['hw.vendor'] = 'OpenBSD'
    virtual._device_tree['hw.cpu.features'] = 'SVM'
    virtual._device_tree['hw.cpu.features'] = 'VMX'
    openbsd_virtual_facts = {
        'virtualization_type': 'vmm',
        'virtualization_role': 'host',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': {'vmm'},
    }
    assert openbsd_virtual_facts == virtual.get_virtual_facts()


# Generated at 2022-06-13 04:10:41.234552
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    fact_subclass = OpenBSDVirtual(None, None)

    # Test cases

# Generated at 2022-06-13 04:10:46.708619
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    openbsd_virtual = OpenBSDVirtualCollector()
    assert openbsd_virtual.platform == 'OpenBSD'
    assert openbsd_virtual._fact_class == OpenBSDVirtual
    assert openbsd_virtual._platform == 'OpenBSD'

if __name__ == '__main__':
    test_OpenBSDVirtualCollector()

# Generated at 2022-06-13 04:10:50.510443
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    # Constructor of OpenBSDVirtualCollector does not take any
    # argument. Verify it.
    p = OpenBSDVirtualCollector()
    assert isinstance(p._fact_class(), OpenBSDVirtual)

# Generated at 2022-06-13 04:10:57.906639
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # This is an example of output of 'sysctl hw.vendor hw.product'
    # on a AWS EC2 m5.xlarge instance.
    sysctl_output = '''hw.vendor=Intel Corporation
hw.product=Intel(R) Xeon(R) Platinum 8175M CPU @ 2.50GHz
'''
    virtual = OpenBSDVirtual('OpenBSD', sysctl_output)
    virtual_facts = virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'xen'
    assert virtual_facts['virtualization_role'] == 'guest'
    assert ('aws' in virtual_facts['virtualization_tech_guest'])
    assert ('xen' in virtual_facts['virtualization_tech_guest'])

# Generated at 2022-06-13 04:11:11.620699
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virtual = OpenBSDVirtual()
    virtual_facts = virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'vmm'
    assert virtual_facts['virtualization_role'] == 'host'
    assert 'vmm' in virtual_facts['virtualization_tech_host']
    assert len(virtual_facts['virtualization_tech_host']) == 1
    assert len(virtual_facts['virtualization_tech_guest']) == 0

# Generated at 2022-06-13 04:11:16.417271
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    """
    Testing method get_virtual_facts of class OpenBSDVirtual
    """
    from ansible.module_utils.facts.virtual.openbsd import (
        OpenBSDVirtual
    )

    virtual = OpenBSDVirtual()
    assert virtual.get_virtual_facts().keys() == [
        'virtualization_role', 'virtualization_type', 'virtualization_technologies',
        'virtualization_tech_host', 'virtualization_tech_guest'
    ]

# Generated at 2022-06-13 04:11:23.439599
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    from ansible_collections.misc.not_a_real_collection.tests.unit.compat.mock import patch
    from ansible_collections.misc.not_a_real_collection.tests.unit.modules.utils import set_module_args


# Generated at 2022-06-13 04:11:29.516810
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    expected_result = {
        'virtualization_type': 'vmm',
        'virtualization_role': 'host',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set(['vmm'])
    }
    with patch('ansible.module_utils.facts.virtual.sysctl.open', mock_open(read_data='vmm0 at mainbus0: SVM/RVI')):
        assert OpenBSDVirtual().get_virtual_facts() == expected_result

# Generated at 2022-06-13 04:11:35.282972
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virtual = OpenBSDVirtual()
    assert virtual.get_virtual_facts() == {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_product': '',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set()
    }

# Generated at 2022-06-13 04:11:39.724170
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virtual_facts = OpenBSDVirtual().get_virtual_facts()
    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''
    assert not virtual_facts['virtualization_tech_guest']
    assert not virtual_facts['virtualization_tech_host']

# Generated at 2022-06-13 04:11:42.774365
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    # test creation of OpenBSDVirtualCollector object
    assert OpenBSDVirtualCollector() is not None

# Generated at 2022-06-13 04:11:45.792872
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    assert issubclass(OpenBSDVirtualCollector._fact_class, Virtual)
    assert OpenBSDVirtualCollector._platform == 'OpenBSD'

# Generated at 2022-06-13 04:11:49.965977
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    dut = OpenBSDVirtualCollector()
    # Check that _fact_class is defined
    assert dut._fact_class == OpenBSDVirtual
    # Check that _platform is defined
    assert dut._platform == 'OpenBSD'

# Test if the class OpenBSDVirtual returns the correct virtualization facts
# This test mocks the methods _platform() and _getcmd_uname()

# Generated at 2022-06-13 04:11:54.792902
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    vc = OpenBSDVirtualCollector()
    assert vc.platform == 'OpenBSD'
    assert vc._fact_class == OpenBSDVirtual
    assert vc._platform == 'OpenBSD'


# Generated at 2022-06-13 04:12:01.052925
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    pass

# Generated at 2022-06-13 04:12:04.695382
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    openbsd_virtual_facts = OpenBSDVirtual().get_virtual_facts()
    assert openbsd_virtual_facts['virtualization_type'] in (
        '', 'openbsd-vmm', 'paravirtualized', 'physical', 'vmm')

# Generated at 2022-06-13 04:12:11.831234
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    fact_klass = OpenBSDVirtual()
    facts = fact_klass.get_virtual_facts()

    assert 'virtualization_type' in facts
    assert 'virtualization_role' in facts
    assert 'virtualization_tech_guest' in facts
    assert 'virtualization_tech_host' in facts
    assert 'virtualization_product_name' in facts
    assert 'virtualization_product_version' in facts
    assert 'virtualization_product_serial' in facts



# Generated at 2022-06-13 04:12:15.712201
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    mock_module = type('AnsibleModule', (object,), {'params': {'gather_subset': ['!all', 'virtual']}})
    mock_module = mock_module()
    o = OpenBSDVirtual(mock_module)

    # OpenBSD doesn't support virtual fact
    assert o.get_virtual_facts() == {}


# Generated at 2022-06-13 04:12:17.044478
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virt = OpenBSDVirtual()
    virt.get_virtual_facts()

# Generated at 2022-06-13 04:12:22.561996
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virtual_test_object = OpenBSDVirtual()

    # virtual_facts is a dictionary
    virtual_facts = virtual_test_object.get_virtual_facts()
    assert isinstance(virtual_facts, dict)

    # List of items and keys to look for in dictionary returned from get_virtual_facts()
    items = ['virtualization_type', 'virtualization_role', 'virtualization_tech_guest', 'virtualization_tech_host']
    keys = ['vendor', 'product']

    for item in items:
        assert item in virtual_facts

    for key in keys:
        assert key in virtual_facts['virtualization_tech_guest']

    assert len(virtual_facts['virtualization_tech_guest']) >= len(keys)
    assert len(virtual_facts) >= len(items)

# Generated at 2022-06-13 04:12:23.763270
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    collector = OpenBSDVirtualCollector()
    assert (collector.platform == 'OpenBSD')
    assert (collector.fact_class == OpenBSDVirtual)


# Generated at 2022-06-13 04:12:33.583384
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virtual = OpenBSDVirtual({})
    for key, value in virtual.get_virtual_facts().items():
        if key in ['virtualization_type', 'virtualization_role']:
            assert value in ['', 'hvm', 'vmware', 'vmm', 'vmware_workstation', 'virtualbox_ose', 'kvm', 'oracle', 'virtualbox']
        elif key == 'virtualization_product_name':
            assert value in ['', 'VMWare', 'VirtualBox', 'KVM', 'Oracle VM', 'Oracle Container Services']

# Generated at 2022-06-13 04:12:38.140690
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    assert issubclass(OpenBSDVirtualCollector, VirtualCollector)
    openbsd_virtual_collector = OpenBSDVirtualCollector()
    assert isinstance(openbsd_virtual_collector, VirtualCollector)


# Generated at 2022-06-13 04:12:48.080082
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    facts = {}
    results = {'virtualization_type': '', 'virtualization_role': ''}

    # hw.vendor is 'GenuineIntel' and hw.product is 'Virtual Box', that
    # indicates the machine is a guest
    facts['ansible_facts'] = {
        'kernel': 'OpenBSD',
        'sysctl': {
            'hw.vendor': 'GenuineIntel',
            'hw.product': 'Virtual Box',
        },
    }
    test_virtual = OpenBSDVirtual(facts)
    results['virtualization_type'] = 'VirtualBox'
    results['virtualization_role'] = 'guest'
    assert test_virtual.get_virtual_facts() == results

    # hw.vendor is 'GenuineIntel' and hw.product is 'Virtual Box', that
    #

# Generated at 2022-06-13 04:13:06.252950
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # Generate expected output
    expected_output = dict()
    expected_output['virtualization_type'] = 'vmm'
    expected_output['virtualization_role'] = 'host'
    expected_output['virtualization_tech_guest'] = set()
    expected_output['virtualization_tech_host'] = {'vmm'}

    v = OpenBSDVirtual('OpenBSD')
    output = v.get_virtual_facts()
    assert output == expected_output

# Generated at 2022-06-13 04:13:11.466428
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    mock_virtual_facts = {
        'hw.product': 'Virtual Box',
        'hw.vendor': 'QEMU',
        'virtualization_type': 'vmm',
        'virtualization_role': 'guest',
        'virtualization_tech_guest': ['hvm'],
        'virtualization_tech_host': ['vmm'],
    }

    collector = OpenBSDVirtualCollector()
    collector.collect()
    facts = collector.get_facts()

    assert facts['virtualization_facts'] == mock_virtual_facts

# Generated at 2022-06-13 04:13:12.734409
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    assert OpenBSDVirtualCollector.test

# Generated at 2022-06-13 04:13:15.573493
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    facts = OpenBSDVirtualCollector()
    assert facts._platform == 'OpenBSD'
    assert isinstance(facts._fact_class(), OpenBSDVirtual)


# Generated at 2022-06-13 04:13:27.046679
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    test_dir = os.path.dirname(os.path.abspath(__file__))
    test_file_path = os.path.join(test_dir, 'fixtures/get_virtual_facts_OpenBSD.json')


# Generated at 2022-06-13 04:13:37.469894
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    o = OpenBSDVirtual({}, {}, {})
    # No match for 'hw.product' and 'hw.vendor'
    o.get_file_content = lambda x: ''
    # Definition of virtualization_type and virtualization_role missing
    result = o.get_virtual_facts()
    assert result == {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set()
    }
    # Definition of virtualization_type and virtualization_role present in
    # 'hw.product'
    o.get_file_content = lambda x: ''
    o.get_file_lines = lambda x: ['Intel Corporation 440FX - 82441FX PMC [Natoma] (virtual machine monitor)']


# Generated at 2022-06-13 04:13:41.563518
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    o = OpenBSDVirtualCollector()
    assert o.get_virtual_facts() == {'virtualization_role': '',
                                     'virtualization_type': '',
                                     'virtualization_tech_guest': set(),
                                     'virtualization_tech_host': set()}

# Generated at 2022-06-13 04:13:46.774422
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # Run OpenBSDVirtual.get_virtual_facts to get host virtual facts
    openbsd_virtual = OpenBSDVirtual()
    openbsd_virtual_facts = openbsd_virtual.get_virtual_facts()

    # Assert the virtualization_type value
    assert openbsd_virtual_facts['virtualization_type'] == 'vmm'

    # Assert the virtualization_role value
    assert openbsd_virtual_facts['virtualization_role'] == 'host'

# Generated at 2022-06-13 04:13:51.801348
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    virtual_facts = OpenBSDVirtualCollector(None).collect()
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts

# Generated at 2022-06-13 04:13:53.035122
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    obj = OpenBSDVirtualCollector()
    assert obj != None

# Generated at 2022-06-13 04:14:27.932889
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    _test_virtual_facts = {
        'virtualization_type': 'vmm',
        'virtualization_role': 'host',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': {'vmm'}
    }
    _test_virtual_facts_str = '\n'.join(['%s: %s' % (key, value) for key, value in _test_virtual_facts.items()])

    print('test_OpenBSDVirtual_get_virtual_facts:')
    print(_test_virtual_facts_str)
    virtual_facts = OpenBSDVirtualCollector.fetch_virtual_facts()
    print('%s\n' % virtual_facts)
    print('Compare result:')
    print(_test_virtual_facts == virtual_facts)



# Generated at 2022-06-13 04:14:32.007241
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virt = OpenBSDVirtual()
    (guest_tech, host_tech, virtual_type, virtual_role) = virt.get_virtual_facts()
    assert guest_tech == set()
    assert host_tech == set()
    assert virtual_type == ''
    assert virtual_role == ''

# Generated at 2022-06-13 04:14:36.533467
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    openbsd_virtual_collector = OpenBSDVirtualCollector()
    assert openbsd_virtual_collector._fact_class == OpenBSDVirtual
    assert openbsd_virtual_collector._platform == 'OpenBSD'


# Generated at 2022-06-13 04:14:38.475732
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    assert OpenBSDVirtualCollector._platform == 'OpenBSD'
    assert OpenBSDVirtualCollector._fact_class == OpenBSDVirtual

# Generated at 2022-06-13 04:14:42.637862
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virtual_facts = OpenBSDVirtual({}).get_virtual_facts()
    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''
    assert virtual_facts['virtualization_tech_host'] == set()
    assert virtual_facts['virtualization_tech_guest'] == set()

# Generated at 2022-06-13 04:14:46.372744
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    virtual_collector = OpenBSDVirtualCollector()
    assert len(virtual_collector.platforms) == 1
    assert virtual_collector.platforms[0] == 'OpenBSD'
    assert virtual_collector.fact_class == OpenBSDVirtual

# Generated at 2022-06-13 04:14:49.211152
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    openbsd_virtual_obj = OpenBSDVirtual(module=None)
    openbsd_virtual_obj.get_virtual_facts()

# Generated at 2022-06-13 04:14:58.863823
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():

    # OpeBSD 6.5 virtual VM on qemu on OpenBSD 6.5
    content_hw_product = """
OpenBSD Virtual Machine
    """
    content_hw_vendor = """
GenuineIntel
    """
    content_dmesg_boot = """
vmm0 at mainbus0: VMX/EPT
vmm0: AMD Ryzen 5 2600X Six-Core Processor (3300.06-MHz K8-class CPU)
    """

    facter_virtual = OpenBSDVirtual()
    facter_virtual.get_file_content = lambda filename: {
        'hw.product': content_hw_product,
        'hw.vendor': content_hw_vendor,
        OpenBSDVirtual.DMESG_BOOT: content_dmesg_boot,
    }[filename]
    virtual_facts = fact

# Generated at 2022-06-13 04:15:06.378870
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virtual_facts = OpenBSDVirtual({}).get_virtual_facts()
    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_type_hvm'] == False
    assert virtual_facts['virtualization_role'] == ''
    assert virtual_facts['virtualization_role_guest'] == False
    assert virtual_facts['virtualization_role_host'] == False
    assert virtual_facts['virtualization_tech_guest'] == set()
    assert virtual_facts['virtualization_tech_host'] == set()

# Generated at 2022-06-13 04:15:12.905171
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    openbsd_virtual = OpenBSDVirtual()
    # Virtualization product test
    openbsd_virtual.facts['hw_product'] = 'VirtualBox'
    result = openbsd_virtual.get_virtual_facts()
    assert result['virtualization_type'] == 'virtualbox'
    assert result['virtualization_role'] == 'guest'
    assert 'virtualbox' in result['virtualization_tech_guest']

    # Virtualization vendor test
    openbsd_virtual.facts['hw_vendor'] = 'QEMU'
    result = openbsd_virtual.get_virtual_facts()
    assert result['virtualization_type'] == 'kvm'
    assert result['virtualization_role'] == 'guest'
    assert 'kvm' in result['virtualization_tech_guest']

    # Virtualization vendor

# Generated at 2022-06-13 04:16:10.500318
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    assert OpenBSDVirtualCollector().platform == 'OpenBSD'

# Generated at 2022-06-13 04:16:14.822125
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    from ansible_collections.ansible.community.tests.unit.modules.utils import set_module_args
    set_module_args({})
    module = OpenBSDVirtual()
    module.gather_facts()
    facts = module.get_facts()
    assert facts['virtualization_type'] == 'vmm'
    assert facts['virtualization_role'] == 'host'

# Generated at 2022-06-13 04:16:24.933745
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # Default parameters should return empty strings
    openbsd_virtual = OpenBSDVirtual()
    openbsd_virtual_facts = openbsd_virtual.get_virtual_facts()
    if openbsd_virtual_facts['virtualization_type'] != '':
        print("Invalid default OpenBSD virtualization_type fact")
        exit(1)
    if openbsd_virtual_facts['virtualization_role'] != '':
        print("Invalid default OpenBSD virtualization_role fact")
        exit(1)

    # OpenBSD provides hw.product on VirtIO platform
    # hw.product: VirtIO Network Card
    # hw.vendor: 1
    # virtio
    # host

# Generated at 2022-06-13 04:16:30.068078
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    facts = {}

    # Get the class object
    OpenBSDVirtualObj = OpenBSDVirtual()

    # Get the facts
    actual_virtual_facts = OpenBSDVirtualObj.get_virtual_facts()

    print("Expected virtual facts: %s,\nActual virtual facts: %s" % (facts, actual_virtual_facts))
    assert actual_virtual_facts == facts

# Generated at 2022-06-13 04:16:32.107287
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virtual_facts = OpenBSDVirtual().get_virtual_facts()
    assert virtual_facts['virtualization_type'] != ''

# Generated at 2022-06-13 04:16:34.621576
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    virtual_facts = OpenBSDVirtualCollector()
    assert virtual_facts._platform == "OpenBSD"
    assert virtual_facts._fact_class == OpenBSDVirtual

# Generated at 2022-06-13 04:16:37.388965
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    openbsd_virtual_collector = OpenBSDVirtualCollector()
    assert isinstance(openbsd_virtual_collector, OpenBSDVirtualCollector)
    assert openbsd_virtual_collector.platform == 'OpenBSD'

# Generated at 2022-06-13 04:16:44.119779
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    openbsd_virtual_facts = OpenBSDVirtual({})

    # Test an OpenBSD AMD host
    facts = dict(
        ansible_product_name='OpenBSD',
        ansible_machine='amd64',
        ansible_system='OpenBSD'
    )
    assert openbsd_virtual_facts.get_virtual_facts(facts) == dict(
        virtualization_type='',
        virtualization_role='',
        virtualization_tech_guest=set(),
        virtualization_tech_host=set()
    )

    # Test an OpenBSD VirtualBox guest
    facts = dict(
        ansible_product_name='OpenBSD',
        ansible_machine='amd64',
        ansible_system='OpenBSD',
        ansible_virtualization_type='VirtualBox'
    )
    assert openbsd_

# Generated at 2022-06-13 04:16:47.353114
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virt = OpenBSDVirtual()
    virt.get_virtual_facts()
    assert virt.virtual_facts['virtualization_type'] is not None, \
        "virtual_facts['virtualization_type'] returned is empty"

# Generated at 2022-06-13 04:16:54.193862
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    import os
    # Create a OpenBSDVirtual object
    virtual_facts_obj = OpenBSDVirtual()

    # Run get_virtual_facts and put result in virtual_facts
    virtual_facts = virtual_facts_obj.get_virtual_facts()

    # Unit test for return value of method get_virtual_facts
    assert os.path.isfile(OpenBSDVirtual.DMESG_BOOT)

# Generated at 2022-06-13 04:19:12.706003
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # Test with host virtualization type vmm
    test_dmesg_boot = '/var/run/dmesg.boot'
    test_dmesg_boot_content = '''OpenBSD 6.6-stable (GENERIC.MP) #0: Wed Aug  5
    vmm0 at mainbus0: SVM/RVI
    cpu0: AMD EPYC (7601) Quad-Core Processor (1794.07-MHz K8-class CPU)'''
    test_dmesg_boot_handle = file(test_dmesg_boot, 'w')
    test_dmesg_boot_handle.write(test_dmesg_boot_content)
    test_dmesg_boot_handle.close()

    test_svm_rvi = OpenBSDVirtual()
    virtual_facts = test_svm_

# Generated at 2022-06-13 04:19:21.830644
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    import json
    import os
    import sys

    # Mock the module parameters class
    # necessary for get_file_content()
    module = sys.modules['ansible.module_utils.facts.virtual.openbsd']
    module.AnsibleModule = type(
        'MockAnsibleModule',
        (),
        {
            'params': {
                'gather_subset': ['all']
            }
        }
    )
    module.os.path.isfile = lambda x: True
    module.get_file_content = lambda x:\
        json.dumps(
            {
                'hw.vendor': 'QEMU',
                'hw.product': 'Standard PC (Q35 + ICH9, 2009)'
            }
        )

    # Create an instance of OpenBSDVirtual
    openbs

# Generated at 2022-06-13 04:19:24.756243
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # Use unit test for VirtualSysctlDetectionMixin
    VirtualSysctlDetectionMixin_test('OpenBSD')

# Generated at 2022-06-13 04:19:32.835732
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():

    openbsd = OpenBSDVirtual({})

# Generated at 2022-06-13 04:19:35.793966
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    openbsd_virtual = OpenBSDVirtual()
    openbsd_virtual.get_virtual_facts()


if __name__ == '__main__':
    test_OpenBSDVirtual_get_virtual_facts()

# Generated at 2022-06-13 04:19:38.267258
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    openbsd_virtual = OpenBSDVirtual()
    openbsd_virtual.get_virtual_facts()


# Generated at 2022-06-13 04:19:44.991204
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    import datetime
    import pytest
    import tempfile

    from ansible.module_utils.facts.virtual.openbsd import OpenBSDVirtual

    # Test data for method get_virtual_facts of class OpenBSDVirtual

# Generated at 2022-06-13 04:19:52.947433
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    sysctl = {'hw.vendor': 'iXsystems Inc.', 'hw.product': 'Virtual Machine'}
    test_virtual = OpenBSDVirtual(sysctl=sysctl)
    virtual_facts = test_virtual.get_virtual_facts()

    assert virtual_facts['virtualization_type'] == 'vmware'
    assert virtual_facts['virtualization_role'] == 'guest'
    assert virtual_facts['virtualization_tech_guest'] == {'vmware'}
    assert virtual_facts['virtualization_tech_host'] == set()

