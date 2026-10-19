

# Generated at 2022-06-13 04:09:58.239471
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():

    # Test with non-OpenBSD platform
    facts_dict = {
        'platform': 'Linux',
    }
    collector = OpenBSDVirtualCollector(facts_dict, None)
    assert collector.platform == 'Linux'

    # Test with OpenBSD platform
    facts_dict['platform'] = 'OpenBSD'
    collector = OpenBSDVirtualCollector(facts_dict, None)
    assert collector.platform == 'OpenBSD'


# Generated at 2022-06-13 04:10:07.298834
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # Needed because class is used inside the class
    OpenBSDVirtual.DMESG_BOOT = './tests/facts/files/openbsd/dmesg.boot'
    virtual_facts = OpenBSDVirtual._get_virtual_facts()
    expected_virtual_facts = {
        'virtualization_type': 'vmm',
        'virtualization_role': 'host',
        'virtualization_tech_guest': set(['vmm']),
        'virtualization_tech_host': set(['vmm']),
        'virtualization_product_host': '',
        'virtualization_product_guest': ''
    }
    assert virtual_facts == expected_virtual_facts

# Generated at 2022-06-13 04:10:09.543904
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    openbsd_virtual = OpenBSDVirtual()
    openbsd_virtual_facts = openbsd_virtual.get_virtual_facts()
    assert openbsd_virtual_facts['virtualization_type'] in ['', 'vmm']

# Generated at 2022-06-13 04:10:15.275841
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    openbsd_virtual_module = OpenBSDVirtualCollector()
    openbsd_virtual_module.get_virtual_facts()
    assert openbsd_virtual_module.facts['virtualization_type'] == ''
    assert openbsd_virtual_module.facts['virtualization_role'] == ''
    assert openbsd_virtual_module.facts['virtualization_tech_guest'] == set()
    assert openbsd_virtual_module.facts['virtualization_tech_host'] == set()

# Generated at 2022-06-13 04:10:19.958446
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    assert issubclass(OpenBSDVirtualCollector, VirtualCollector)
    assert OpenBSDVirtualCollector._fact_class is OpenBSDVirtual
    assert OpenBSDVirtualCollector._platform == 'OpenBSD'

# Generated at 2022-06-13 04:10:30.168868
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # When 'hw.product' contains 'VirtualBox' and hw.vendor contains 'innotek'
    # virtualization_type and virtualization_role will be 'vbox' and 'guest'
    # virtualization_tech_guest will contains 'vbox' and 'uml' (from OpenBSD facts)
    # virtualization_tech_host will contains 'virtualbox' (from OpenBSD facts)
    openbsd_virtual = OpenBSDVirtual(facts={'hw': {'product': 'VirtualBox', 'vendor': 'innotek'}})
    virtual_facts = openbsd_virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'vbox'
    assert virtual_facts['virtualization_role'] == 'guest'

# Generated at 2022-06-13 04:10:39.837257
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    vb = OpenBSDVirtual(module=None)

    vb.sysctl = {
        'hw.vendor': 'genuineintel',
        'hw.product': 'Intel(R) Core(TM) i7-3770 CPU @ 3.40GHz',
        'machdep.hv_vendor': 'VMware',
        'machdep.hv_product': 'VMware Virtual Platform',
    }

    facts = vb.get_virtual_facts()

    # Check the returned virtualization_type
    assert facts['virtualization_type'] == 'VMware Virtual Platform'

    # Check the returned virtualization_role
    assert facts['virtualization_role'] == 'guest'

    # Check the returned virtualization_tech_guest
    assert facts['virtualization_tech_guest'] == set(['vmware'])

# Generated at 2022-06-13 04:10:40.403310
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    pass

# Generated at 2022-06-13 04:10:45.397128
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    """
    Constructor of OpenBSDVirtualCollector.
    """
    openbsd_virtual_collector = OpenBSDVirtualCollector()

    assert openbsd_virtual_collector._platform == 'OpenBSD'
    assert openbsd_virtual_collector._fact_class == OpenBSDVirtual

# Generated at 2022-06-13 04:10:51.111003
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virtual_facts = OpenBSDVirtual().get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'vmm'
    assert virtual_facts['virtualization_role'] == 'host'
    assert virtual_facts['virtualization_tech_guest'] == set()
    assert virtual_facts['virtualization_tech_host'] == {'vmm'}

# Generated at 2022-06-13 04:10:56.791229
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    vc = OpenBSDVirtualCollector()
    assert vc._fact_class == OpenBSDVirtual
    assert vc._platform == 'OpenBSD'

# Generated at 2022-06-13 04:10:59.677969
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    my_OpenBSDVirtualCollector = OpenBSDVirtualCollector()
    assert isinstance(my_OpenBSDVirtualCollector, OpenBSDVirtualCollector)


# Generated at 2022-06-13 04:11:07.508030
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():

    class SysctlMock():
        def get(parameter):
            sysctl_info = {
                'hw.vendor': 'QEMU',
                'hw.product': '',
                'hw.machine': 'amd64',
            }
            return sysctl_info.get(parameter)

    openbsd_virtual = OpenBSDVirtual(SysctlMock)
    assert openbsd_virtual.get_virtual_facts().get('virtualization_type') == 'hvm'
    assert openbsd_virtual.get_virtual_facts().get('virtualization_role') == 'guest'
    assert openbsd_virtual.get_virtual_facts().get('virtualization_product') == ''
    assert 'virt' in openbsd_virtual.get_virtual_facts().get('virtualization_tech_guest')
   

# Generated at 2022-06-13 04:11:14.514445
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    fact_collector = OpenBSDVirtualCollector()
    facts = fact_collector.get_virtual_facts()
    assert 'virtualization_type' in facts
    assert 'virtualization_role' in facts
    assert 'virtualization_product_name' in facts
    assert 'virtualization_product_version' in facts
    assert 'virtualization_product_serial' in facts
    assert 'virtualization_product_uuid' in facts
    assert 'virtualization_product_vendor' in facts
    assert 'virtualization_product_family' in facts

# Generated at 2022-06-13 04:11:20.965039
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virtual_facts = OpenBSDVirtual().get_virtual_facts()

    # Test if values are in the facts
    assert virtual_facts['virtualization_type'] in ['', 'vmm']
    assert virtual_facts['virtualization_role'] in ['', 'host']
    assert len(virtual_facts['virtualization_tech_guest']) > 0 or len(virtual_facts['virtualization_tech_host']) > 0

# Generated at 2022-06-13 04:11:26.663829
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # pylint: disable=protected-access
    facts = OpenBSDVirtual().get_virtual_facts()
    assert facts['virtualization_type'] == 'vmm'
    assert facts['virtualization_role'] == 'host'
    assert facts['virtualization_tech_host'] == {'vmm'}
    assert facts['virtualization_tech_guest'] == set()

# Generated at 2022-06-13 04:11:32.174860
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virtual = OpenBSDVirtual()
    facts = virtual.get_facts()
    assert facts['virtualization_type'] == 'vmm'
    assert facts['virtualization_role'] == 'host'
    assert facts['virtualization_tech_host'] == set(['vmm'])
    assert facts['virtualization_tech_guest'] == set(['vmm'])

# Generated at 2022-06-13 04:11:35.858326
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    c = OpenBSDVirtualCollector()
    assert c._fact_class is OpenBSDVirtual
    assert c._platform == 'OpenBSD'

# Generated at 2022-06-13 04:11:43.387926
# Unit test for method get_virtual_facts of class OpenBSDVirtual

# Generated at 2022-06-13 04:11:46.404385
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virtual = OpenBSDVirtualCollector(None, None, None, {}).collect()[0]
    assert virtual.get_virtual_facts()['virtualization_role'] == ''


# Generated at 2022-06-13 04:12:00.302459
# Unit test for method get_virtual_facts of class OpenBSDVirtual

# Generated at 2022-06-13 04:12:10.440801
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    """
    Test get_virtual_facts() method of class OpenBSDVirtual
    """
    # Running this on OpenBSD host
    bsd_virtual_collector = OpenBSDVirtualCollector()
    bsd_virtual = bsd_virtual_collector.get_virtual_facts()

    # Virtualization type is vmm and role is host for OpenBSD host as
    # OpenBSD hypervisor is vmm(4)
    assert bsd_virtual['virtualization_type'] == 'vmm'
    assert bsd_virtual['virtualization_role'] == 'host'
    assert 'vmm' in bsd_virtual['virtualization_tech_host']
    assert bsd_virtual['virtualization_tech_guest'] == set()

# Generated at 2022-06-13 04:12:18.234311
# Unit test for method get_virtual_facts of class OpenBSDVirtual

# Generated at 2022-06-13 04:12:20.877460
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # Run get_virtual_facts of class OpenBSDVirtual
    virtual_facts = OpenBSDVirtual().get_virtual_facts()

    # Print the result
    for key, value in virtual_facts.items():
        print("%-32s: %s" % (key, value))

# vim: set et ts=4 sw=4 :

# Generated at 2022-06-13 04:12:32.100760
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # Create an instance of OpenBSDVirtual()
    openbsd_virtual = OpenBSDVirtual()

    # Init some fake 'facts' which will be used in the test
    setattr(openbsd_virtual.facts, 'hw_vendor', 'OpenBSD')
    setattr(openbsd_virtual.facts, 'hw_product', 'OpenBSD')

# Generated at 2022-06-13 04:12:36.131682
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    #
    # Unit test for get_virtual_facts method of OpenBSDVirtual
    #
    OpenBSDVirtual.get_virtual_facts()

# Generated at 2022-06-13 04:12:43.349804
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    facts_dict = dict()
    virtual = OpenBSDVirtual(facts_dict, None)
    virtual_facts = virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'vmm'
    assert virtual_facts['virtualization_role'] == 'host'
    assert virtual_facts['virtualization_tech_guest'] == set()
    assert virtual_facts['virtualization_tech_host'] == set(['vmm'])
    assert virtual_facts['virtualization_product_name'] == ''

# Generated at 2022-06-13 04:12:54.068456
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virtual_facts_test = {
        'virtualization_type': 'vmm',
        'virtualization_role': 'host',
        'virtualization_tech_guest': set(['vmm']),
        'virtualization_tech_host': set(['vmm'])
    }
    openbsd_virtual = OpenBSDVirtualCollector({'ansible_facts': {'kernel': 'OpenBSD'}})
    openbsd_virtual._module.params['gather_subset'] = ['!all', 'virtual']
    with open('/tmp/dmesg', 'w') as dmesg:
        dmesg.write('vmm0 at mainbus0: SVM/RVI\n')

# Generated at 2022-06-13 04:13:00.870507
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # Get module object
    virtual_facts = OpenBSDVirtual()

    # Check virtual facts when running on a physical system
    virtual_facts.sysctl = {'hw.vendor': 'OpenBSD', 'hw.product': 'OpenBSD'}
    virtual_facts.dmesg = {'vmm': False}
    facts = virtual_facts.get_virtual_facts()
    assert facts['virtualization_type'] == ''
    assert facts['virtualization_role'] == ''
    assert facts['virtualization_tech_guest'] == set()
    assert facts['virtualization_tech_host'] == set()

    # Check virtual facts when running on a guest
    virtual_facts.sysctl = {'hw.vendor': 'OpenBSD', 'hw.product': 'OpenBSD'}

# Generated at 2022-06-13 04:13:03.421064
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    openbsd_virtual_collector = OpenBSDVirtualCollector()
    assert openbsd_virtual_collector._fact_class is OpenBSDVirtual
    assert openbsd_virtual_collector._platform == 'OpenBSD'

# Generated at 2022-06-13 04:13:19.194543
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    openbsd_virtual_collector = OpenBSDVirtualCollector()
    print(openbsd_virtual_collector)


# Generated at 2022-06-13 04:13:20.788918
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    openbsd_virtual_collector = OpenBSDVirtualCollector()
    assert openbsd_virtual_collector._platform == 'OpenBSD'
    assert openbsd_virtual_collector._fact_class == OpenBSDVirtual


# Generated at 2022-06-13 04:13:29.118734
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # Create mock module
    config_data = """
    class OpenBSDVirtual:
        DMESG_BOOT = 'unit_test_data/dmesg.boot'
        """
    ns = {}
    exec(config_data, globals(), ns)
    setattr(ns['OpenBSDVirtual'], 'platform', 'OpenBSD')
    mock_module = ns['OpenBSDVirtual']()

    result = mock_module.get_virtual_facts()
    assert result['virtualization_type'] == 'vmm'
    assert result['virtualization_role'] == 'host'
    assert result['virtualization_tech_guest'] == set()
    assert result['virtualization_tech_host'] == {'vmm'}


# Generated at 2022-06-13 04:13:33.203106
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    openbsd_virtual_collector = OpenBSDVirtualCollector()
    print(openbsd_virtual_collector.platform)
    print(openbsd_virtual_collector.fact_class)
    print(openbsd_virtual_collector._fact_class)
    print(openbsd_virtual_collector._platform)


# Generated at 2022-06-13 04:13:36.697271
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    openbsd_virtual_collector = OpenBSDVirtualCollector()
    assert openbsd_virtual_collector.virtual_facts['virtualization_type'] == ''
    assert openbsd_virtual_collector.virtual_facts['virtualization_role'] == ''

# Generated at 2022-06-13 04:13:38.148807
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    assert hasattr(OpenBSDVirtualCollector, 'collect')


# Generated at 2022-06-13 04:13:47.232214
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():

    fact_subclass = OpenBSDVirtual()
    # Set facts to get expected results.
    # The setter of the facts_module is not used because it has side effects
    # that we don't want in this test.
    fact_subclass.facts_module = type('FactsModule', (), {})()
    for fact in ['hw.product', 'hw.vendor']:
        fact_subclass.facts_module.get_file_content.return_value = fact
    facts = fact_subclass.get_virtual_facts()
    # Test vmm(4) host.
    fact_subclass.facts_module.get_file_content.return_value = 'vmm0 at mainbus0: SVM/RVI'
    facts = fact_subclass.get_virtual_facts()

# Generated at 2022-06-13 04:13:49.881522
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    openbsd_virtual_collector = OpenBSDVirtualCollector()
    assert openbsd_virtual_collector == {'OpenBSDVirtual': {'platform': 'OpenBSD'}}

# Generated at 2022-06-13 04:13:55.979126
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    openbsd = OpenBSDVirtual({})
    virtual_facts = openbsd.get_virtual_facts()
    assert type(virtual_facts) == dict
    assert 'virtualization_type' in virtual_facts.keys()
    assert 'virtualization_role' in virtual_facts.keys()
    assert 'virtualization_tech_guest' in virtual_facts.keys()
    assert 'virtualization_tech_host' in virtual_facts.keys()

# Generated at 2022-06-13 04:13:58.041307
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    openbsd_virtual_collector = OpenBSDVirtualCollector()
    assert openbsd_virtual_collector.platform == 'OpenBSD'

# Generated at 2022-06-13 04:14:30.097604
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    collector = OpenBSDVirtualCollector()
    assert collector is not None

# Generated at 2022-06-13 04:14:32.900636
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    virtual_collector = OpenBSDVirtualCollector()
    assert virtual_collector
    assert virtual_collector._fact_class == OpenBSDVirtual
    assert virtual_collector._platform == 'OpenBSD'

# Generated at 2022-06-13 04:14:43.329858
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # Test psd#16070
    dmesg_boot = b'psd16070: hw.vendor: QEMU\npsd16070: hw.product: Standard PC (Q35 + ICH9, 2009)\n'
    test_fixture = OpenBSDVirtual()
    test_fixture.DMESG_BOOT = '/tmp/foo'
    test_fixture.write_temp_file(test_fixture.DMESG_BOOT, dmesg_boot)
    expected_facts = {
        'virtualization_role': 'guest',
        'virtualization_type': 'kvm',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set(['kvm'])
    }
    actual_facts = test_fixture.get_virtual_facts

# Generated at 2022-06-13 04:14:45.041052
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    o = OpenBSDVirtualCollector()
    assert o._platform == 'OpenBSD'


# Generated at 2022-06-13 04:14:55.104855
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virtual = OpenBSDVirtual()

    # Test with empty dmesg.boot content
    mock_content = '''
foo
bar
'''
    virtual._get_file_content = lambda x: mock_content
    virtual_facts = virtual.get_virtual_facts()
    assert virtual_facts['virtualization_tech_guest'] == set()
    assert virtual_facts['virtualization_tech_host'] == set()
    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''

    # Test with virtualization technology found in dmesg.boot
    mock_content = '''
foo
bar
vmm0 at mainbus0: SVM/RVI
baz
'''
    virtual._get_file_content = lambda x: mock_content
    virtual_facts = virtual.get

# Generated at 2022-06-13 04:14:56.540409
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    assert issubclass(OpenBSDVirtualCollector, VirtualCollector)


# Generated at 2022-06-13 04:14:58.664919
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    virtual_collector = OpenBSDVirtualCollector()
    assert virtual_collector._platform == 'OpenBSD'
    assert virtual_collector._fact_class == OpenBSDVirtual

# Generated at 2022-06-13 04:15:01.693539
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    '''
    Test OpenBSDVirtualCollector constructor
    '''
    set_module_args({})
    OpenBSDVirtualCollector()


# Generated at 2022-06-13 04:15:06.377015
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    openbsd_virtual = OpenBSDVirtual()

    assert openbsd_virtual.get_virtual_facts() == {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_technologies': [],
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set()
    }

# Generated at 2022-06-13 04:15:09.571845
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    facts_objs = OpenBSDVirtual()
    facts = facts_objs.get_virtual_facts()
    assert facts['virtualization_type'] == 'vmm'
    assert facts['virtualization_role'] == 'host'

# Generated at 2022-06-13 04:16:12.867523
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    v = OpenBSDVirtual({}, {})
    facts = v.get_virtual_facts()
    assert facts['virtualization_type'] == 'vmm'
    assert facts['virtualization_role'] == 'host'
    assert facts['virtualization_technology'] == 'vmm'

# Generated at 2022-06-13 04:16:19.351745
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    openbsd_virtual = OpenBSDVirtual()
    # Return empty dict on OpenBSD when no virtualization is detected
    assert openbsd_virtual.get_virtual_facts() == {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_product_name': '',
        'virtualization_product_version': '',
        'virtualization_product_vendor': '',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set(),
    }

# Generated at 2022-06-13 04:16:23.373541
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    module = OpenBSDVirtual()
    module.module_init({})
    module.get_virtual_facts()
    assert module.virtual_facts['virtualization_type'] == 'OpenBSD'
    assert module.virtual_facts['virtualization_role'] == 'guest'

# Generated at 2022-06-13 04:16:25.657253
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    openbsd_virtual = OpenBSDVirtual()
    openbsd_virtual.get_virtual_facts()
    assert openbsd_virtual.facts['virtualization_role'] == ''

# Generated at 2022-06-13 04:16:28.291689
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # the get_virtual_facts method is not implemented yet
    assert OpenBSDVirtual('OpenBSD').get_virtual_facts() == {}

# Generated at 2022-06-13 04:16:31.701783
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    openbsd_virtual = OpenBSDVirtual()

    # Positive tests with no virtualization/resource
    result = openbsd_virtual.get_virtual_facts()
    assert result['virtualization_type'] == ''
    assert result['virtualization_role'] == ''
    assert len(result['virtualization_tech_guest']) == 0
    assert len(result['virtualization_tech_host']) == 0

    # Positive tests with only hypervisor resource
    openbsd_virtual.RESOURCES = {"hw.vendor": "hostVendor", "hw.product": "hostProduct"}

    result = openbsd_virtual.get_virtual_facts()
    assert result['virtualization_type'] == 'hostVendor'
    assert result['virtualization_role'] == 'host'

# Generated at 2022-06-13 04:16:34.406715
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    v = OpenBSDVirtualCollector()
    assert v._fact_class == OpenBSDVirtual
    assert v._platform == 'OpenBSD'

# Generated at 2022-06-13 04:16:36.902420
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    """
    Constructor for class OpenBSDVirtualCollector
    """
    assert OpenBSDVirtualCollector._platform == 'OpenBSD'
    assert OpenBSDVirtualCollector._fact_class == OpenBSDVirtual

# Generated at 2022-06-13 04:16:43.478557
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    """Unit test for method get_virtual_facts of class OpenBSDVirtual."""
    virtual_facts = dict()
    # Create an instance of class OpenBSDVirtual
    openbsd_virtual = OpenBSDVirtual()
    # Test method get_virtual_facts of class OpenBSDVirtual
    virtual_facts = openbsd_virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] in ('vmm', '') or \
            'virtualization_tech_guest' in virtual_facts, \
            'virtualization_type is not a key of virtual_facts'
    assert virtual_facts['virtualization_role'] in ('host', '') or \
            'virtualization_tech_host' in virtual_facts, \
            'virtualization_role is not a key of virtual_facts'

# Generated at 2022-06-13 04:16:47.547783
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():

    openBSDCollector = OpenBSDVirtualCollector()
    assert openBSDCollector._platform == 'OpenBSD'
    assert openBSDCollector._fact_class == OpenBSDVirtual


if __name__ == '__main__':
    test_OpenBSDVirtualCollector()

# Generated at 2022-06-13 04:19:14.005697
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    openbsd_virtual = OpenBSDVirtual()
    facts = openbsd_virtual.get_virtual_facts()
    assert facts['virtualization_type'] == 'vmm'
    assert facts['virtualization_role'] == 'host'
    assert 'vmm' in facts['virtualization_tech_host']
    assert 'vmm' not in facts['virtualization_tech_guest']

# Generated at 2022-06-13 04:19:16.606077
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    c = OpenBSDVirtualCollector()
    assert c.platform == 'OpenBSD'


# Generated at 2022-06-13 04:19:18.642854
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    fixture = OpenBSDVirtualCollector()
    assert fixture._fact_class is OpenBSDVirtual
    assert fixture._platform is 'OpenBSD'

# Generated at 2022-06-13 04:19:20.899687
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    obj = OpenBSDVirtualCollector()
    assert obj.platform == 'OpenBSD'
    assert obj.fact_class == OpenBSDVirtual
    assert obj.fact_class().platform == 'OpenBSD'


# Generated at 2022-06-13 04:19:31.436631
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    module_utils = 'ansible.module_utils.facts.virtual.openbsd'
    get_virtual_facts_function = 'get_virtual_facts'
    get_virtual_facts_args = []
    get_virtual_facts_kwargs = {}
    input_data = {
        'platform': 'OpenBSD',
    }
    expected_return = {
        'virtualization_role': '',
        'virtualization_type': '',
        'virtualization_tech_host': set(['vmm']),
        'virtualization_tech_guest': set(['vmm']),
        'virtualization_product_name': '',
    }

# Generated at 2022-06-13 04:19:41.632609
# Unit test for method get_virtual_facts of class OpenBSDVirtual

# Generated at 2022-06-13 04:19:46.634714
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    class MockModule(object):
        def __init__(self, params):
            self.params = params

        def fail_json(self, *args, **kwargs):
            self.exit_args = args
            self.exit_kwargs = kwargs
            raise Exception('fail_json')

    module = MockModule({})

    # Set up some mock sysctl data for testing
    class MockSysctlData(object):
        def __init__(self):
            self.data = {}

        def get(self, name):
            return self.data.get(name)

        def set(self, name, value):
            self.data[name] = value

    sysctl_data = MockSysctlData()
    module.get_bin_path = lambda x: '/sbin/sysctl'

    # VirtualSysctlDetectionMix

# Generated at 2022-06-13 04:19:52.348928
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # mock dmesg.boot
    virtual = OpenBSDVirtual()
    OpenBSDVirtual.DMESG_BOOT = 'tests/unit/module_utils/facts/virtual/mock_data/openbsd_dmesg_boot'

    # Store result
    result = virtual.get_virtual_facts()

    assert result['virtualization_role'] == 'guest'
    assert result['virtualization_type'] == 'qemu'