

# Generated at 2022-06-13 04:09:54.775377
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual()
    assert netbsd_virtual


# Generated at 2022-06-13 04:09:56.553722
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual_facts = NetBSDVirtual()
    assert virtual_facts.get_virtual_facts()['virtualization_type'] == ''

# Generated at 2022-06-13 04:10:04.898771
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual = NetBSDVirtual()
    # Needs to be done before asserts to set static values
    virtual_facts = virtual.get_virtual_facts()
    virtual_facts['virtualization_type'] = 'xen'
    virtual_facts['virtualization_role'] = 'guest'
    virtual_facts['virtualization_tech_guest'] = {'xen'}
    virtual_facts['virtualization_tech_host'] = set()
    assert virtual.get_virtual_facts() == virtual_facts

# Generated at 2022-06-13 04:10:09.404656
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    # Create NetBSDVirtual object
    netbsd_virtual = NetBSDVirtual()
    # Create facts that should be detected by sysctl
    expected_facts = {
        'virtualization_type': 'virtualbox',
        'virtualization_role': 'guest',
        'virtualization_tech_guest': {'virtualbox', 'virtualbox_guest'},
        'virtualization_tech_host': {'virtualbox', 'virtualbox_host'}
    }
    # If we run this test on a non NetBSD host, return an empty dictionary
    if netbsd_virtual.platform != 'NetBSD':
        return {}
    # Create a sysctl_info dictionary

# Generated at 2022-06-13 04:10:10.270517
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual = NetBSDVirtual()
    assert virtual

# Generated at 2022-06-13 04:10:14.945053
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    expected = {
        'virtualization_type': 'VMWare',
        'virtualization_role': 'guest',
        'virtualization_tech_guest': set(['vmware', 'xen']),
        'virtualization_tech_host': set(['vmware'])}
    actual = NetBSDVirtual().get_virtual_facts()
    assert actual == expected

# Generated at 2022-06-13 04:10:27.480715
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    # Test data for raw sysctl data
    test_data_raw = {
        'machdep.dmi.system-product': 'VMware Virtual Platform',
        'machdep.dmi.system-vendor': 'VMware, Inc.',
        'machdep.hypervisor': 'Xen',
    }

    # Test data for expected output

# Generated at 2022-06-13 04:10:28.982942
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd = NetBSDVirtual()
    assert netbsd.platform == 'NetBSD'

# Generated at 2022-06-13 04:10:30.008072
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    assert NetBSDVirtual(dict())

# Generated at 2022-06-13 04:10:39.692071
# Unit test for method get_virtual_facts of class NetBSDVirtual

# Generated at 2022-06-13 04:10:50.858437
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    # Create a NetBSDVirtual object
    obj = NetBSDVirtual()

    # Set expected data
    expected = {'virtualization_type': 'VMWare',
                'virtualization_role': 'guest',
                'virtualization_tech_guest': set(['vmware']),
                'virtualization_tech_host': set(['vmware'])}

    # Get virtual facts
    actual = obj.get_virtual_facts()

    # Assert
    assert actual == expected



# Generated at 2022-06-13 04:10:58.041955
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    # Create test environment
    # Empty sysctl namespace
    class fake_sysctl(object):
        # All sysctl methods are stubbed
        def __call__(self):
            pass
        def __getitem__(self, key):
            pass

    class TestClass(NetBSDVirtual):
        def __init__(self, module):
            pass

    # Test for a bare metal system
    virtual_facts = TestClass.get_virtual_facts(
        TestClass('module'),
        fake_sysctl(),
        {'machdep.dmi.system-vendor': '',
         'machdep.dmi.system-product': '',
         'machdep.hypervisor': '' })
    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''
    assert virtual

# Generated at 2022-06-13 04:11:00.603905
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual_netbsd_obj = NetBSDVirtual({})
    assert virtual_netbsd_obj._platform == 'NetBSD'
    assert virtual_netbsd_obj.platform == 'NetBSD'


# Generated at 2022-06-13 04:11:02.549183
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    instance = NetBSDVirtualCollector()
    assert instance.platform == 'NetBSD'
    assert instance._fact_class == NetBSDVirtual

# Generated at 2022-06-13 04:11:08.990521
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    class MockNetBSDVirtual(NetBSDVirtual):
        VIRTUAL_PRODUCT_MAPPING = {'/sys/devices/virtual/dmi/id/product_name': 'Test Virtual Product'}
        VIRTUAL_VENDOR_MAPPING = {'/sys/devices/virtual/dmi/id/sys_vendor': 'Test Virtual Vendor'}
        SYSCTL_VIRT_PRODUCT_KEYS = {'hw.model': ['Test Hardware Model']}
        SYSCTL_VIRT_VENDOR_KEYS = {'hw.model': ['Test Hardware Model']}

        def _get_sysctl_value(self, key):
            if key == 'machdep.dmi.system-product':
                return '/sys/devices/virtual/dmi/id/product_name'

# Generated at 2022-06-13 04:11:13.225634
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virt_facts = NetBSDVirtual()

    assert virt_facts.get_virtual_facts() == {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set()
    }

# Generated at 2022-06-13 04:11:17.924462
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    """Test NetBSDVirtual constructor"""
    netbsd_virtual = NetBSDVirtual({}, {})
    assert netbsd_virtual.platform == 'NetBSD'
    assert netbsd_virtual.virtualization_type == ''
    assert netbsd_virtual.virtualization_role == ''
    assert netbsd_virtual.virtualization_tech_guest == set()
    assert netbsd_virtual.virtualization_tech_host == set()
    assert netbsd_virtual.enabled is False

# Generated at 2022-06-13 04:11:23.581757
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    from ansible_collections.ansible.community.tests.unit.compat import unittest
    from ansible_collections.ansible.community.tests.unit.compat.mock import patch, MagicMock
    from ansible.module_utils.facts.virtual.netbsd import NetBSDVirtual

    class TestNetBSDVirtual(NetBSDVirtual):
        def __init__(self, module):
            pass

        def get_file_content(self, path):
            if path == '/dev/ksyms':
                return ("cgd0 at cgddriver0: no crypto key provided; "
                        "encryption disabled [partition not present]\n"
                        "cgd1 at cgddriver0: no crypto key provided; "
                        "encryption disabled [partition not present]\n")

# Generated at 2022-06-13 04:11:29.266300
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virt_obj = NetBSDVirtual()
    virtual_facts = virt_obj.get_virtual_facts()

    assert virtual_facts['virtualization_type'] != ''
    assert virtual_facts['virtualization_type'] in \
           virtual_facts['virtualization_tech_guest']
    assert virtual_facts['virtualization_type'] in \
           virtual_facts['virtualization_tech_host']
    assert virtual_facts['virtualization_role'] != ''

    assert virtual_facts['virtualization_role'] in \
           ['guest', 'host']

# Generated at 2022-06-13 04:11:33.849920
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    netbsd_vc = NetBSDVirtualCollector()
    assert netbsd_vc
    assert netbsd_vc._platform == 'NetBSD'
    assert netbsd_vc._fact_class == NetBSDVirtual


# Generated at 2022-06-13 04:11:39.534542
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual('sysctl')
    assert netbsd_virtual.cmd == 'sysctl'

# Generated at 2022-06-13 04:11:43.949642
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    collector = NetBSDVirtualCollector()
    assert collector.__class__.__name__ == 'NetBSDVirtualCollector'
    assert collector._platform == 'NetBSD'


# Generated at 2022-06-13 04:11:45.738481
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    """Check if the class can be instantiated."""
    NetBSDVirtual()

# Generated at 2022-06-13 04:11:48.449544
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    netbsd_collector = NetBSDVirtualCollector()
    assert netbsd_collector._platform == 'NetBSD'
    assert netbsd_collector._fact_class == NetBSDVirtual


# Generated at 2022-06-13 04:11:52.833118
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual()
    assert isinstance(netbsd_virtual, NetBSDVirtual)

# Generated at 2022-06-13 04:12:00.475712
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():

    # Test data
    dmi_system_vendor_values = [
        'HVM domU',
        'ACME, Inc.',
    ]

    dmi_system_product_values = [
        'ACME 2000',
        'HVM domU',
    ]

    machdep_hypervisor_values = [
        'None',
        'ACME 2000',
    ]

    # Test class
    test_netbsd_virtual_collector = NetBSDVirtualCollector()


# Generated at 2022-06-13 04:12:01.629612
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    NetBSDVirtualCollector()

# Generated at 2022-06-13 04:12:04.451231
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    data = NetBSDVirtual({})
    assert data.platform == "NetBSD"
    assert data.virtualization_type == ""
    assert data.virtualization_role == ""

# Generated at 2022-06-13 04:12:14.731940
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    # construct a dummy file like /dev/xen/evtchn that is normally
    # used to detect xen
    f = open('/dev/xen/evtchn', 'w')
    f.close()

    # construct a dummy file like /dev/xencons that is used to detect xen
    f = open('/dev/xencons', 'w')
    f.close()


# Generated at 2022-06-13 04:12:21.911357
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    netbsd_virtual = NetBSDVirtual()

    expected = {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_tech_guest': set(['xen']),
        'virtualization_tech_host': set()
    }

    actual = netbsd_virtual.get_virtual_facts()

    del actual['virtualization_sysctl_machdep_dmi_system_product']
    del actual['virtualization_sysctl_machdep_dmi_system_vendor']
    del actual['virtualization_sysctl_machdep_hypervisor']

    assert actual == expected

# Generated at 2022-06-13 04:12:31.947822
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    netbsd_virtual_collector = NetBSDVirtualCollector()
    assert netbsd_virtual_collector._platform == 'NetBSD'
    assert netbsd_virtual_collector._fact_class == NetBSDVirtual

# Generated at 2022-06-13 04:12:33.031299
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual = NetBSDVirtual()
    assert virtual.platform == 'NetBSD'

# Generated at 2022-06-13 04:12:44.805020
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    # Prepare mocks and test data.
    # Method 'detect_virt_vendor'
    mock_detect_virt_vendor_return_value = {
        'virtualization_tech_host': set(),
        'virtualization_tech_guest': set(),
        'virtualization_type': '',
        'virtualization_role': ''
    }
    # VirtualSysctlDetectionMixin._get_sysctl(key)
    mock_sysctl_values = {
        'machdep.dmi.system-product': 'OpenBSD Virtual Machine',
        'machdep.dmi.system-vendor': 'iXsystems, Inc.',
        'machdep.hypervisor': 'OpenBSD VM'
    }

    # Set up the mocks.
    #
    # @patch(target, **kwargs

# Generated at 2022-06-13 04:12:55.662149
# Unit test for method get_virtual_facts of class NetBSDVirtual

# Generated at 2022-06-13 04:13:01.638393
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    collector = NetBSDVirtualCollector()
    assert collector.platform == 'NetBSD'
    assert collector._fact_class == NetBSDVirtual
    assert collector._virtual_files == ['machdep.dmi.system-product', 'machdep.dmi.system-vendor', 'machdep.hypervisor']
    assert collector._virtual_commands == []



# Generated at 2022-06-13 04:13:10.449858
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    fake_sysctl_fact_data='{"machdep.hypervisor": "xen", "machdep.dmi.system-vendor": "BOCHS", "machdep.dmi.system-product": "Bochs"}'
    module = {"sysctl": fake_sysctl_fact_data}
    virtual = NetBSDVirtualCollector(module=module, version=2)
    result = virtual.get_virtual_facts()
    assert result['virtualization_type'] == 'xen'
    assert result['virtualization_role'] == 'guest'
    assert result['virtualization_tech'] == {'xen'}
    assert result['virtualization_tech_guest'] == result['virtualization_tech']
    assert result['virtualization_tech_host'] == set()

# Generated at 2022-06-13 04:13:12.462627
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    NetBSDVirtualCollector()

# Generated at 2022-06-13 04:13:18.698132
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual_facts = NetBSDVirtual().get_virtual_facts()
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts

    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_type'] == ''
    assert len(virtual_facts['virtualization_tech_guest']) == 0
    assert len(virtual_facts['virtualization_tech_host']) == 0

# Generated at 2022-06-13 04:13:28.425502
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    netbsd_virtual_facts = NetBSDVirtual()

    # sysctl -n machdep.dmi.system-vendor, machdep.dmi.system-product and machdep.hypervisor exists
    # xen domain
    os.environ['VIRTUAL_PRODUCT_FACTS'] = '{"machdep.dmi.system-product": "None", "machdep.dmi.system-vendor": "None"}'
    os.environ['VIRTUAL_VENDOR_FACTS'] = '{"machdep.dmi.system-vendor": "VMWare", "machdep.hypervisor": "VMWare"}'
    os.environ['XEN_SYSCTL_EXISTS'] = 'True'

# Generated at 2022-06-13 04:13:38.556296
# Unit test for method get_virtual_facts of class NetBSDVirtual

# Generated at 2022-06-13 04:13:58.265889
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual_facts = NetBSDVirtualCollector().get_all_facts()
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts
    assert 'virtualization_products' in virtual_facts

# Generated at 2022-06-13 04:14:07.528764
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    """Test get_virtual_facts function of class NetBSDVirtual"""
    # Set up
    netbsd_obj = NetBSDVirtual()
    machdep_dict = dict()

    # Test 1: No machdep data
    expected = dict()
    expected['virtualization_type'] = ''
    expected['virtualization_role'] = ''

    actual = netbsd_obj.get_virtual_facts()
    assert actual == expected, "actual: %s expected: %s" % (actual, expected)

    # Test 2: machdep.hypervisor set
    machdep_dict['machdep.hypervisor'] = 'xhyve'

    expected = dict()
    expected['virtualization_type'] = 'xhyve'
    expected['virtualization_technology_host'] = set(['xhyve'])

# Generated at 2022-06-13 04:14:10.175205
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_obj = NetBSDVirtual()
    assert netbsd_obj.platform == 'NetBSD'


# Generated at 2022-06-13 04:14:10.953904
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual = NetBSDVirtual()
    assert virtual

# Generated at 2022-06-13 04:14:11.489508
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    NetBSDVirtual()

# Generated at 2022-06-13 04:14:12.207417
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual = NetBSDVirtual()
    assert virtual is not None

# Generated at 2022-06-13 04:14:22.772091
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():

    get_virtual_facts_netbsd = NetBSDVirtual(None).get_virtual_facts()
    assert 'virtualization_type' in get_virtual_facts_netbsd
    assert 'virtualization_role' in get_virtual_facts_netbsd
    assert 'virtualization_type_role' in get_virtual_facts_netbsd
    assert 'virtualization_tech_guest' in get_virtual_facts_netbsd
    assert 'virtualization_tech_host' in get_virtual_facts_netbsd
    assert get_virtual_facts_netbsd['virtualization_type'] in ['', 'virtualbox', 'vmware', 'kvm', 'xen', 'prl', 'openvz', 'vserver']

# Generated at 2022-06-13 04:14:26.397371
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd = NetBSDVirtual(module=dict())

    assert netbsd.platform == 'NetBSD'

    assert hasattr(netbsd, 'get_virtual_facts')
    assert callable(netbsd.get_virtual_facts)

    assert hasattr(netbsd, 'is_container')
    assert callable(netbsd.is_container)

# Generated at 2022-06-13 04:14:27.063721
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    assert NetBSDVirtual({})

# Generated at 2022-06-13 04:14:38.102843
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    def test_file(path, content):
        if os.path.exists(path):
            os.unlink(path)
        return open(path, 'w+b').write(content.encode('utf-8'))

    def test_sysctl(name, content):
        test_file('/proc/sys/%s' % name, content)

    def test_machdep():
        test_sysctl('machdep.hypervisor', 'none')
        test_sysctl('machdep.dmi.system-product', 'vmware')
        test_sysctl('machdep.dmi.system-vendor', 'vmware')
        test_sysctl('machdep.dmi.system-uuid', 'testuuid')

# Generated at 2022-06-13 04:15:09.303369
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsdvirtual = NetBSDVirtual(None)
    assert netbsdvirtual.platform == 'NetBSD'

# Generated at 2022-06-13 04:15:11.560764
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    nv = NetBSDVirtual(None)
    assert nv is not None


# Generated at 2022-06-13 04:15:18.277213
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtuals = ('VirtualBox', 'VMware', 'QEMU', 'KVM', 'Bochs', 'Xen', 'Microsoft', 'Parallels', 'Virtual Machine', 'Other', 'BareMetal', 'Hyper-V')
    virtualization_roles = ('guest', 'host', 'container')
    virtualization_tech_host = ('kvm', 'qemu', 'vbox', 'vmware', 'xen', 'bochs', 'hyperv', 'kvm', 'parallels', 'qemu', 'vmware', 'other')
    virtualization_tech_guest = ('xen', 'kvm', 'parallels', 'vbox', 'vmware', 'xen', 'hyperv', 'kvm', 'parallels', 'qemu', 'vmware', 'other')

# Generated at 2022-06-13 04:15:29.575636
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    facts = {}

    fake_sysctl_data = {
        'machdep.hypervisor': 'Amazon EC2',
        'machdep.dmi.system-vendor': 'Amazon EC2',
        'machdep.dmi.system-product': '',
        'machdep.cpu.vendor': 'GenuineIntel',
        'machdep.cpu.model': 'Intel(R) Xeon(R) CPU E5-2670 v2 @ 2.50GHz',
    }


# Generated at 2022-06-13 04:15:35.067045
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    netbsd = NetBSDVirtual()

    virtual_facts = netbsd.get_virtual_facts()

    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts


# Generated at 2022-06-13 04:15:37.027229
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual = NetBSDVirtual()
    assert virtual._platform == 'NetBSD'
    assert virtual.platform == 'NetBSD'
    assert virtual.get_virtual_facts() == virtual.facts

# Generated at 2022-06-13 04:15:40.743505
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    # Test that the virtual_facts has the following key
    ans = NetBSDVirtual()
    keys = [
        'virtualization_role',
        'virtualization_type',
        'virtualization_tech_guest',
        'virtualization_tech_host']
    for key in keys:
        assert key in ans.virtual_facts

# Generated at 2022-06-13 04:15:45.016709
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    nvcol = NetBSDVirtualCollector()
    assert nvcol._platform == 'NetBSD'
    assert nvcol._fact_class == NetBSDVirtual

# Generated at 2022-06-13 04:15:46.036567
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    v = NetBSDVirtual()
    v.get_virtual_facts()



# Generated at 2022-06-13 04:15:47.411145
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd = NetBSDVirtual(None, None)

    assert netbsd.platform == 'NetBSD'


# Generated at 2022-06-13 04:17:07.327816
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    assert NetBSDVirtual.platform == 'NetBSD'

# Generated at 2022-06-13 04:17:08.729814
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsdvirtual = NetBSDVirtual()
    assert netbsdvirtual.platform == "NetBSD"


# Generated at 2022-06-13 04:17:10.667216
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual = NetBSDVirtual()
    virtual.get_virtual_facts()

# Generated at 2022-06-13 04:17:18.276849
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():

    nv = NetBSDVirtual()

    assert nv.platform == 'NetBSD'
    assert nv.kernel == 'NetBSD'

    # Test for empty data
    def fake_sysctl_get(args):
        return ''
    nv.get_sysctl = fake_sysctl_get

    facts = nv.get_virtual_facts()

    assert facts['virtualization_type'] == ''
    assert facts['virtualization_role'] == ''
    assert facts['virtualization_tech_guest'] == set()
    assert facts['virtualization_tech_host'] == set()

# Generated at 2022-06-13 04:17:25.148973
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    # Test with empty sysctl facts
    def emptySysctlFacts(name):
        return (None, None)

    virtual_netbsd = NetBSDVirtual(emptySysctlFacts)
    facts = virtual_netbsd.get_virtual_facts()

    assert facts['virtualization_type'] == ''
    assert facts['virtualization_role'] == ''

    # Test with a kvm sysctl facts
    def kvmSysctlFacts(name):
        if name == "machdep.dmi.system-product":
            return ("KVM", True)
        return (None, None)

    virtual_netbsd = NetBSDVirtual(kvmSysctlFacts)
    facts = virtual_netbsd.get_virtual_facts()

    assert facts['virtualization_type'] == 'kvm'

# Generated at 2022-06-13 04:17:32.816567
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    res = dict([
        ('virtualization_type', 'kvm'),
        ('virtualization_role', 'guest')
    ])

    mock_sysctl_output = dict([
        ('machdep.dmi.system-product', 'KVM'),
    ])

    mock_kvm_sysctl_output = dict([
        ('machdep.dmi.system-product', 'KVM'),
        ('machdep.dmi.system-vendor', 'KVM'),
    ])

    mock_virtualbox_sysctl_output = dict([
        ('machdep.dmi.system-product', 'VirtualBox'),
        ('machdep.dmi.system-vendor', 'innotek GmbH'),
    ])


# Generated at 2022-06-13 04:17:35.061735
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd = NetBSDVirtual()
    assert netbsd._platform == "NetBSD"


# Generated at 2022-06-13 04:17:36.321466
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    c = NetBSDVirtualCollector()
    assert c._platform == 'NetBSD'

# Generated at 2022-06-13 04:17:38.663288
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    c = NetBSDVirtualCollector()
    assert c._fact_class == NetBSDVirtual
    assert c._platform == 'NetBSD'

# Generated at 2022-06-13 04:17:40.208065
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual = NetBSDVirtual()
    assert virtual.os is not None
    assert virtual.platform == 'NetBSD'