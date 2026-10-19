

# Generated at 2022-06-13 04:09:57.728426
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    openbsd_virtual = OpenBSDVirtual()
    virtual_facts = openbsd_virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'vmm'
    assert virtual_facts['virtualization_role'] == 'host'
    assert virtual_facts['virtualization_tech_guest'] == set()
    assert virtual_facts['virtualization_tech_host'] == {'vmm'}

# vim: set expandtab:ts=4:sw=4:

# Generated at 2022-06-13 04:10:01.795456
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    openbsd_virtual_collector = OpenBSDVirtualCollector()
    assert openbsd_virtual_collector.platform == 'OpenBSD'
    assert openbsd_virtual_collector.fact_class == OpenBSDVirtual

# Generated at 2022-06-13 04:10:11.082199
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    openbsd_virtual_facts = OpenBSDVirtual()
    # test with product 'OpenBSD'
    openbsd_virtual_facts.product = 'OpenBSD'
    virtual_facts = openbsd_virtual_facts.get_virtual_facts()
    assert not virtual_facts['virtualization_type']
    assert not virtual_facts['virtualization_role']
    assert not virtual_facts['virtualization_tech_guest']
    assert not virtual_facts['virtualization_tech_host']
    # test with product 'OpenBSD/amd64'
    openbsd_virtual_facts.product = 'OpenBSD/amd64'
    virtual_facts = openbsd_virtual_facts.get_virtual_facts()
    assert not virtual_facts['virtualization_type']
    assert not virtual_facts['virtualization_role']
    assert not virtual

# Generated at 2022-06-13 04:10:12.195898
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    OpenBSDVirtualCollector()

# Generated at 2022-06-13 04:10:13.851426
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    collector = OpenBSDVirtualCollector()
    assert collector.platform == 'OpenBSD'

# Generated at 2022-06-13 04:10:18.173272
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    openbsd_virtual = OpenBSDVirtualCollector()
    assert openbsd_virtual._fact_class == OpenBSDVirtual
    assert openbsd_virtual._platform == 'OpenBSD'


# Generated at 2022-06-13 04:10:29.023762
# Unit test for method get_virtual_facts of class OpenBSDVirtual

# Generated at 2022-06-13 04:10:38.901477
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    import mock

    facts = dict()
    facts['virtualization_type'] = ''
    facts['virtualization_role'] = ''
    facts['virtualization_tech_guest'] = set()
    facts['virtualization_tech_host'] = set()

    virtual_product_facts = dict()
    virtual_product_facts['virtualization_type'] = ''
    virtual_product_facts['virtualization_role'] = ''
    virtual_product_facts['virtualization_tech_guest'] = set()
    virtual_product_facts['virtualization_tech_host'] = set()

    virtual_vendor_facts = dict()
    virtual_vendor_facts['virtualization_type'] = ''
    virtual_vendor_facts['virtualization_role'] = ''
    virtual_vendor_facts['virtualization_tech_guest'] = set

# Generated at 2022-06-13 04:10:40.015527
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    OpenBSDVirtualCollector()



# Generated at 2022-06-13 04:10:41.258140
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    # Call to constructor should succeed
    OpenBSDVirtualCollector()

# Generated at 2022-06-13 04:10:50.933819
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    assert issubclass(OpenBSDVirtualCollector, VirtualCollector)
    assert OpenBSDVirtualCollector._fact_class == OpenBSDVirtual
    assert OpenBSDVirtualCollector._platform == 'OpenBSD'

# Generated at 2022-06-13 04:10:54.412665
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    openbsd_virtual = OpenBSDVirtual()
    facts = openbsd_virtual.get_virtual_facts()

    assert 'virtualization_type' in facts
    assert 'virtualization_role' in facts
    assert 'virtualization_tech_host' in facts
    assert 'virtualization_tech_guest' in facts

# Generated at 2022-06-13 04:10:56.893143
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    vc = OpenBSDVirtualCollector()
    assert vc._platform == 'OpenBSD'
    assert vc._fact_class == OpenBSDVirtual

# Generated at 2022-06-13 04:11:05.028174
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    test_input = {
        'host_virtual_facts': {'hw.vendor': "NetBSD"},
    }
    openbsd_virtual = OpenBSDVirtual(test_input)
    facts = openbsd_virtual.get_virtual_facts()
    assert facts['virtualization_type'] == ''

    test_input = {
        'host_virtual_facts': {'hw.vendor': "OpenBSD"},
    }
    openbsd_virtual = OpenBSDVirtual(test_input)
    facts = openbsd_virtual.get_virtual_facts()
    assert facts['virtualization_type'] == 'vmm'
    assert facts['virtualization_role'] == 'host'

# Generated at 2022-06-13 04:11:08.446091
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    v = Virtual()
    vfacts = v.get_virtual_facts()
    assert 'virtualization_type' in vfacts

# Generated at 2022-06-13 04:11:17.245745
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    openbsd_virtual = OpenBSDVirtual()

    # Set empty values as default
    openbsd_virtual.facts['virtualization_type'] = ''
    openbsd_virtual.facts['virtualization_role'] = ''
    openbsd_virtual.facts['virtualization_tech_guest'] = set()
    openbsd_virtual.facts['virtualization_tech_host'] = set()

    openbsd_virtual.detect_virt_vendor = lambda x: {'virtualization_type': 'vmm',
                                                    'virtualization_role': 'guest',
                                                    'virtualization_tech_guest': set(['vmm']),
                                                    'virtualization_tech_host': set(['vmm'])}


# Generated at 2022-06-13 04:11:19.695616
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    openbsd_virtual = OpenBSDVirtualCollector()
    assert isinstance(openbsd_virtual, OpenBSDVirtualCollector)


# Generated at 2022-06-13 04:11:25.016101
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virt_facts = OpenBSDVirtual()
    virtual_facts = virt_facts.get_virtual_facts()
    assert 'virtualization_tech_host' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts

# Generated at 2022-06-13 04:11:33.002911
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    openbsd_virtual = OpenBSDVirtual()
    openbsd_virtual.sysctl_val = {
        'hw.vendor': 'VirtualBox',
        'hw.product': 'VirtualBox',
    }

# Generated at 2022-06-13 04:11:39.217464
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virt = OpenBSDVirtual()
    facts = virt.get_virtual_facts()
    assert facts['virtualization_type'] == ''
    assert facts['virtualization_role'] == ''
    assert facts['virtualization_tech_guest'] == set()
    assert facts['virtualization_tech_host'] == set()
    assert facts['virtualization_product_name'] == ''

# Generated at 2022-06-13 04:11:53.706792
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    vm = OpenBSDVirtualCollector()
    assert isinstance(vm, OpenBSDVirtualCollector)

# Generated at 2022-06-13 04:12:00.826211
# Unit test for method get_virtual_facts of class OpenBSDVirtual

# Generated at 2022-06-13 04:12:12.226889
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    class MockOpenBSDVirtual(OpenBSDVirtual):
        def detect_virt_vendor(self, *args, **kwargs):
            return {'virtualization_type': 'virtualbox', 'virtualization_role': 'guest',
                    'virtualization_tech_guest': ['vbox'], 'virtualization_tech_host': []}

        def detect_virt_product(self, *args, **kwargs):
            return {'virtualization_type': '', 'virtualization_role': '',
                    'virtualization_tech_guest': [], 'virtualization_tech_host': []}

    virtual_facts = MockOpenBSDVirtual().get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'virtualbox'
    assert virtual_facts['virtualization_role'] == 'guest'

# Generated at 2022-06-13 04:12:22.132376
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    ov = OpenBSDVirtual()
    ov.sysctl_output = {'hw.product': 'OpenBSD', 'hw.vendor': 'GenuineIntel'}
    facts = ov.get_virtual_facts()
    assert facts['virtualization_type'] == ''
    assert facts['virtualization_role'] == ''
    assert facts['virtualization_tech_guest'] == set()
    assert facts['virtualization_tech_host'] == set()

    ov.sysctl_output = {'hw.product': '', 'hw.vendor': 'OpenBSD'}
    facts = ov.get_virtual_facts()
    assert facts['virtualization_type'] == 'OpenBSD'
    assert facts['virtualization_role'] == ''
    assert facts['virtualization_tech_guest'] == set()

# Generated at 2022-06-13 04:12:25.893394
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    virtual = OpenBSDVirtualCollector()
    assert virtual.platform == 'OpenBSD'
    assert virtual._fact_class == OpenBSDVirtual

# Generated at 2022-06-13 04:12:34.611275
# Unit test for method get_virtual_facts of class OpenBSDVirtual

# Generated at 2022-06-13 04:12:37.404591
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    assert OpenBSDVirtualCollector._platform == 'OpenBSD'
    assert OpenBSDVirtualCollector._fact_class == OpenBSDVirtual


# Generated at 2022-06-13 04:12:43.850105
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    from module_utils.facts.virtual.openbsd import OpenBSDVirtual

    # Create an instance of the OpenBSDVirtual class
    test_instance = OpenBSDVirtual()

    # Get the virtual facts for OpenBSDVirtual
    virtual_facts = test_instance.get_virtual_facts()

    assert virtual_facts['virtualization_type'] == ''

    assert 'virtualization_tech_guest' not in virtual_facts

    assert 'virtualization_tech_host' not in virtual_facts

# Generated at 2022-06-13 04:12:46.673764
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    openbsd_virtual_collector = OpenBSDVirtualCollector()
    assert openbsd_virtual_collector._fact_class is OpenBSDVirtual
    assert openbsd_virtual_collector._platform is 'OpenBSD'

# Generated at 2022-06-13 04:12:50.931699
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    v = OpenBSDVirtual({})
    v._init_sysctl_cache()
    v.facts['system'] = 'OpenBSD'
    import inspect
    args = inspect.getargspec(v.get_virtual_facts)

    assert len(args[0]) == 1


# Generated at 2022-06-13 04:13:06.924908
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virtual = OpenBSDVirtualCollector().collect()[0]
    facts = virtual.get_virtual_facts()
    assert facts['virtualization_type'] == 'vmm'
    assert facts['virtualization_role'] == 'host'
    assert facts['virtualization_tech_host'] == {'vmm'}

# Generated at 2022-06-13 04:13:10.588862
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virtual = OpenBSDVirtual()
    virtual_facts = virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''
    assert virtual_facts['virtualization_tech_host'] == set()
    assert virtual_facts['virtualization_tech_guest'] == set()

# Generated at 2022-06-13 04:13:13.789408
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virtual = OpenBSDVirtual()
    setattr(virtual, '_virtual_facts', {})

    # Set empty values as default
    virtual._virtual_facts['virtualization_type'] = ''
    virtual._virtual_facts['virtualization_role'] = ''

    virtual_facts = virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''

# Generated at 2022-06-13 04:13:16.038906
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    x = OpenBSDVirtualCollector()
    assert x.platform == 'OpenBSD'
    assert x._fact_class == OpenBSDVirtual

# Generated at 2022-06-13 04:13:18.779975
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    openbsdvirtual = OpenBSDVirtualCollector()
    assert openbsdvirtual._fact_class is not None

# Generated at 2022-06-13 04:13:22.897389
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    facts = OpenBSDVirtual()

    #testing virtualization_type and virtualization_role
    assert facts.get_virtual_facts()['virtualization_type'] == 'vmm'
    assert facts.get_virtual_facts()['virtualization_role'] == 'host'

# Generated at 2022-06-13 04:13:30.602437
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # Create an object of class OpenBSDVirtual
    test_subject = OpenBSDVirtual()

    # Create some test data
    test_sysctl_content = {
        'hw.vendor': 'QEMU',
        'hw.product': 'Standard PC (Q35 + ICH9, 2009)'
    }

    test_dmesg_boot_content = '''
vmm0 at mainbus0: VMX/EPT
'''

    # Create a mock of get_file_content function
    def test_get_file_content(filename):
        if filename == OpenBSDVirtual.SYSCTL:
            return test_sysctl_content
        elif filename == OpenBSDVirtual.DMESG_BOOT:
            return test_dmesg_boot_content
        else:
            raise FileNotFoundError

    # Set the test

# Generated at 2022-06-13 04:13:41.547446
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    openbsd_virtual = OpenBSDVirtual()

    # Virtualization facts can be detected by hw.product sysctl
    sysctl_file_name = openbsd_virtual.sysctl_file_name
    sysctl_file_name_orig = sysctl_file_name
    openbsd_virtual.sysctl_file_name = 'sysctl_hw.product.xen'
    virtual_facts = openbsd_virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'xen'
    assert virtual_facts['virtualization_role'] == 'guest'
    assert virtual_facts['virtualization_tech_guest'] == {'xen'}
    assert virtual_facts['virtualization_tech_host'] == set()

    # Virtualization facts can be detected by hw.vendor sysctl

# Generated at 2022-06-13 04:13:44.756277
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    openbsd_virtual_collector = OpenBSDVirtualCollector()
    assert openbsd_virtual_collector.platform == 'OpenBSD'
    assert openbsd_virtual_collector.fact_class == OpenBSDVirtual



# Generated at 2022-06-13 04:13:46.905130
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    openbsd_virtual_collector = OpenBSDVirtualCollector()
    assert openbsd_virtual_collector._fact_class == OpenBSDVirtual
    assert openbsd_virtual_collector._platform == 'OpenBSD'

# Generated at 2022-06-13 04:14:17.345049
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    openbsd_virtual_collector = OpenBSDVirtualCollector()
    assert openbsd_virtual_collector.platform == 'OpenBSD'

# Generated at 2022-06-13 04:14:25.537919
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    openbsd_virtual = OpenBSDVirtual()

# Generated at 2022-06-13 04:14:27.406270
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    """
    Constructor test for class OpenBSDVirtualCollector
    """
    class_openbsd = OpenBSDVirtualCollector()
    assert class_openbsd._fact_class == OpenBSDVirtual


# Generated at 2022-06-13 04:14:29.132720
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    get_virtual_facts = OpenBSDVirtualCollector()
    assert get_virtual_facts._fact_class == OpenBSDVirtual
    assert get_virtual_facts._platform == 'OpenBSD'

# Generated at 2022-06-13 04:14:29.962260
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    x = OpenBSDVirtualCollector()
    assert x.platform == 'OpenBSD'

# Generated at 2022-06-13 04:14:30.540941
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    OpenBSDVirtualCollector()

# Generated at 2022-06-13 04:14:31.321275
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    OpenBSDVirtualCollector()

# Generated at 2022-06-13 04:14:32.070262
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    OpenBSDVirtualCollector().collect()

# Generated at 2022-06-13 04:14:38.637083
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    openbsd_virtual_facts = OpenBSDVirtual().get_virtual_facts()

    assert openbsd_virtual_facts['virtualization_type'] == ''
    assert openbsd_virtual_facts['virtualization_role'] == ''
    assert len(openbsd_virtual_facts['virtualization_tech_guest']) == 0
    assert len(openbsd_virtual_facts['virtualization_tech_host']) == 0

# Generated at 2022-06-13 04:14:40.941465
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    assert OpenBSDVirtualCollector._platform == 'OpenBSD'
    assert OpenBSDVirtualCollector._fact_class == OpenBSDVirtual
    assert OpenBSDVirtualCollector.platform == 'OpenBSD'

# Generated at 2022-06-13 04:15:32.732267
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    assert hasattr(OpenBSDVirtualCollector, '_fact_class')
    assert hasattr(OpenBSDVirtualCollector, '_platform')

# Generated at 2022-06-13 04:15:41.095742
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # Test data
    test_value_hw_vendor = 'Virtual Machine Vendor'
    test_value_hw_product = 'Virtual Machine Product'
    test_value_vendor_vendor = 'Virtual Machine Vendor'
    test_value_vendor_product = 'Virtual Machine Product'
    test_value_vendor_version = 'Virtual Machine Version'
    test_value_vendor_serial = 'VM0'
    test_value_vendor_uuid = 'Virtual Machine UUID'

    test_value_vendor_key_product = 'OpenBSD'
    test_value_vendor_key_version = 'Virtual Machine Version'
    test_value_vendor_key_serial = 'VM0'

    test_value_dmesg = '''
vmm0 at mainbus0: VMX/EPT
'''



# Generated at 2022-06-13 04:15:46.733240
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    mock_ansible_module = MockAnsibleModule()
    test_OpenBSDVirtual = OpenBSDVirtual(mock_ansible_module)
    
    # Test a host machine
    with mock.patch('ansible.module_utils.facts.virtual.OpenBSDVirtual.get_file_content', return_value='vmm0 at mainbus0: SVM/RVI'):
        test_OpenBSDVirtual.get_virtual_facts()

    expected_virtual_facts = {'virtualization_role': 'host',
                              'virtualization_type': 'vmm',
                              'virtualization_tech_host': {'vmm'},
                              'virtualization_tech_guest': set()}

    assert(mock_ansible_module.exit_json.called)

# Generated at 2022-06-13 04:15:52.556121
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    """
    Test get_virtual_facts with valid two dmesg.boot entries.
    """

    virtual_facts = {'virtualization_type': 'vmm',
                     'virtualization_role': 'host',
                     'virtualization_tech_guest': {'vmm'},
                     'virtualization_tech_host': {'vmm'},
                     'virtualization_product_name': '',
                     'virtualization_product_version': '',
                     'virtualization_product_serial': ''}

    test_get_virtual_facts = OpenBSDVirtual.get_virtual_facts(OpenBSDVirtual())
    assert test_get_virtual_facts == virtual_facts



# Generated at 2022-06-13 04:16:01.667220
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    openbsd_virtual_collector = OpenBSDVirtualCollector()
    openbsd_virtual_collector.collect()
    facts = openbsd_virtual_collector.get_facts()
    extra_facts = openbsd_virtual_collector.get_extra_facts()
    virtual_facts = extra_facts['ansible_virtualization_facts']
    assert virtual_facts['virtualization_type'] == 'vmm'
    assert virtual_facts['virtualization_role'] == 'host'
    assert 'vmm' in virtual_facts['virtualization_tech_guest']
    assert 'vmm' in virtual_facts['virtualization_tech_host']

# Generated at 2022-06-13 04:16:12.650113
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # Test with no virtualization
    virtual_facts = OpenBSDVirtual().get_virtual_facts()
    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''
    assert virtual_facts['virtualization_tech_guest'] == set()
    assert virtual_facts['virtualization_tech_host'] == set()

    # Test when dmesg indicates vmm capabilities
    virtual_facts = OpenBSDVirtual(dmesg_boot=['vmm0 at mainbus0: SVM/RVI',
                                               'vmm1 at mainbus0: VMX/EPT']).get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'vmm'
    assert virtual_facts['virtualization_role'] == 'host'

# Generated at 2022-06-13 04:16:14.285604
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    collector = OpenBSDVirtualCollector()
    assert collector.platform == 'OpenBSD'
    assert collector._fact_class == OpenBSDVirtual

# Generated at 2022-06-13 04:16:18.287954
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    expected = {'virtualization_role': '',
                'virtualization_type': '',
                'virtualization_tech_guest': set(),
                'virtualization_tech_host': set()}
    actual = OpenBSDVirtual.get_virtual_facts()
    assert actual == expected

# Generated at 2022-06-13 04:16:19.838900
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    openbsd_virtual_collector = OpenBSDVirtualCollector()
    assert openbsd_virtual_collector is not None

# Generated at 2022-06-13 04:16:26.446209
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # define ansible facts
    ansible_facts = {}

    # define expected results
    expected_results = {
        'virtualization_type': 'vmm',
        'virtualization_role': 'host',
        'virtualization_tech_guest': set(['vmm']),
        'virtualization_tech_host': set(['vmm']),
    }

    virtual_facts_obj = OpenBSDVirtual()
    virtual_facts = virtual_facts_obj.get_virtual_facts()

    assert virtual_facts == expected_results

# Generated at 2022-06-13 04:18:46.002758
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.sysctl import VirtualSysctlDetectionMixin
    from ansible.module_utils.facts.virtual.openbsd import OpenBSDVirtual


# Generated at 2022-06-13 04:18:49.168058
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virt_facts = OpenBSDVirtual(module=None).get_virtual_facts()
    assert virt_facts['virtualization_tech_guest'] == set()
    assert virt_facts['virtualization_tech_host'] == set()
    assert virt_facts['virtualization_type'] == ''
    assert virt_facts['virtualization_role'] == ''

# Generated at 2022-06-13 04:18:54.375397
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    OpenBSDVirtualCollector.detect_virtual_facts = VirtualCollector.detect_virtual_facts
    OpenBSDVirtualCollector.detect_virtual_facts.collector = OpenBSDVirtualCollector()
    fact_result = OpenBSDVirtualCollector.detect_virtual_facts()
    for fact in fact_result:
        if fact == 'virtualization_role':
            assert fact_result[fact] == 'host' or fact_result[fact] == ''
        elif fact == 'virtualization_type':
            assert fact_result[fact] == 'vmm' or fact_result[fact] == ''
        elif fact == 'virtualization_tech_guest':
            assert fact_result[fact] == set()
        elif fact == 'virtualization_tech_host':
            assert fact_result[fact] == set()
       

# Generated at 2022-06-13 04:18:57.859805
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virt = OpenBSDVirtual()
    virtual_facts = virt.get_virtual_facts()
    assert virtual_facts == {
        'virtualization_role': 'host',
        'virtualization_type': '',
        'virtualization_tech_host': set(),
        'virtualization_tech_guest': set()
    }



# Generated at 2022-06-13 04:19:01.731083
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    openbsd_virtual_collector = OpenBSDVirtualCollector()
    assert openbsd_virtual_collector._fact_class == OpenBSDVirtual

# Generated at 2022-06-13 04:19:04.607185
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    openbsd_virtual_collector = OpenBSDVirtualCollector()
    assert openbsd_virtual_collector._platform == 'OpenBSD'
    assert openbsd_virtual_collector._fact_class == OpenBSDVirtual


# Generated at 2022-06-13 04:19:07.524476
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virtual_facts = OpenBSDVirtual().get_virtual_facts()
    assert type(virtual_facts) is dict
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts

# Generated at 2022-06-13 04:19:14.254989
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # Create a mock of class OpenBSDVirtual
    openbsd_virtual = OpenBSDVirtual()

    # Create a mock of the method detect_virt_vendor
    def mock_detect_virt_vendor(*args, **kwargs):
        return {'virtualization_type': 'vmm',
                'virtualization_role': 'host',
                'virtualization_tech_guest': set(['svm']),
                'virtualization_tech_host': set(['svm'])}
    openbsd_virtual.detect_virt_vendor = mock_detect_virt_vendor

    # Create a mock of the method detect_virt_product

# Generated at 2022-06-13 04:19:18.171523
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    openbsdvirtualclass = OpenBSDVirtualCollector()
    assert openbsdvirtualclass._platform == 'OpenBSD'
    assert openbsdvirtualclass._fact_class.platform == 'OpenBSD'



# Generated at 2022-06-13 04:19:19.923700
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    assert OpenBSDVirtualCollector._platform == 'OpenBSD'
    assert OpenBSDVirtualCollector._fact_class == OpenBSDVirtual
