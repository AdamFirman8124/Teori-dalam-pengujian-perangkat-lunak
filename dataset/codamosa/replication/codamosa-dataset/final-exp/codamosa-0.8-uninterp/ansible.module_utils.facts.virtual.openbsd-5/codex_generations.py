

# Generated at 2022-06-13 04:09:59.755393
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    """
    Unit test for method get_virtual_facts of class OpenBSDVirtual
    """
    results = {}

    ######################################################
    # Run module without parameters
    ######################################################
    results = OpenBSDVirtual().get_virtual_facts()

    # Check keys in the result
    key_list = [
        "virtualization_type",
        "virtualization_role",
        "virtualization_tech_guest",
        "virtualization_tech_host"
    ]
    for key in key_list:
        assert key in results

    # Check that virtualization_type is not set
    assert results['virtualization_type'] == ''
    assert results['virtualization_role'] == ''

    # Check that virtualization_tech_guest and virtualization_tech_host are empty sets

# Generated at 2022-06-13 04:10:09.746856
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    obj = OpenBSDVirtualCollector()

    # Case 1: i386 platform
    facts = {
        'platform': obj._platform,
        'architecture': 'i386',
        'kernel': obj._platform,
    }
    result = obj._fact_class(facts).get_virtual_facts()

    assert result['virtualization_type'] == 'vmm'
    assert result['virtualization_role'] == 'host'
    assert 'vmm' in result['virtualization_tech_host']

    # Case 2: amd64 platform
    facts['architecture'] = 'amd64'
    result = obj._fact_class(facts).get_virtual_facts()

    assert result['virtualization_type'] == 'vmm'
    assert result['virtualization_role'] == 'host'

# Generated at 2022-06-13 04:10:10.982892
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    assert OpenBSDVirtualCollector()._platform == 'OpenBSD'

# Generated at 2022-06-13 04:10:14.991117
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.openbsd import OpenBSDVirtual

    obj = OpenBSDVirtual()
    results = obj.get_virtual_facts()

    assert results['virtualization_type'] == ''
    assert results['virtualization_role'] == ''
    assert results['virtualization_product_name'] == ''

# Generated at 2022-06-13 04:10:21.967251
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virt_obj = OpenBSDVirtual()
    facts = virt_obj.get_virtual_facts()

    assert facts['virtualization_type'] == 'vmm'
    assert facts['virtualization_role'] == 'host'
    assert facts['virtualization_tech_guest'] == 'vmm'
    assert facts['virtualization_tech_host'] == 'vmm'

# Generated at 2022-06-13 04:10:24.958273
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    v_facts = OpenBSDVirtualCollector().collect()
    assert len(v_facts) == 7
    assert v_facts['virtualization_type'] == ''
    assert v_facts['virtualization_role'] == ''

# Generated at 2022-06-13 04:10:29.139778
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.virtual.openbsd import OpenBSDVirtualCollector
    vc = OpenBSDVirtualCollector()
    assert isinstance(vc, Collector)
    assert isinstance(vc, OpenBSDVirtualCollector)

# Generated at 2022-06-13 04:10:35.687180
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # Initialize a loaded module
    module = OpenBSDVirtualCollector.factory()

    # Initialize the instance of OpenBSDVirtual and call the method
    v = OpenBSDVirtual(module)
    vf = v.get_virtual_facts()

    # Make sure we have the correct keys
    assert set(vf.keys()) == set(['virtualization_type', 'virtualization_role', 'virtualization_tech_guest', 'virtualization_tech_host'])

# Generated at 2022-06-13 04:10:47.583984
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # init OpenBSDVirtual
    openbsd_virtual = OpenBSDVirtual()

    # test get_virtual_facts without dmesg.boot
    openbsd_virtual.detect_virt_product = lambda x: {'virtualization_type': 'hypervisor', 'virtualization_role': 'host',
                                                     'virtualization_tech_guest': set(), 'virtualization_tech_host': set()}
    openbsd_virtual.detect_virt_vendor = lambda x: {'virtualization_type': 'hypervisor', 'virtualization_role': 'host',
                                                    'virtualization_tech_guest': set(), 'virtualization_tech_host': set()}
    openbsd_virtual_facts = openbsd_virtual.get_virtual_facts()

# Generated at 2022-06-13 04:10:51.752638
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    facts = OpenBSDVirtual().get_virtual_facts()
    assert 'virtualization_type' in facts
    assert 'virtualization_role' in facts
    assert 'virtualization_tech_guest' in facts
    assert 'virtualization_tech_host' in facts

# Generated at 2022-06-13 04:10:56.740132
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    openbsd_virtual = OpenBSDVirtual()
    assert openbsd_virtual.get_virtual_facts() == {}

# Generated at 2022-06-13 04:11:06.029145
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # Let's create a 'OpenBSDVirtual' object
    obvd = OpenBSDVirtual()
    # Let's call private method 'get_virtual_facts'
    virtual_facts = obvd.get_virtual_facts()

    # Let's assert the returned dict
    assert type(virtual_facts) is dict, \
        "The returned value should be a dict"
    assert virtual_facts['virtualization_type'], \
        "The returned dict should have a non empty 'virtualization_type' key"
    assert virtual_facts['virtualization_role'], \
        "The returned dict should have a non empty 'virtualization_role' key"
    assert virtual_facts['virtualization_role'] in ['guest', 'host'], \
        "The value of 'virtualization_role' should be either 'guest' or 'host"

# Generated at 2022-06-13 04:11:11.279232
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    facts = {}
    OpenBSDVirtual().get_virtual_facts(facts)
    assert 'virtualization_role' in facts
    assert 'virtualization_type' in facts
    assert 'virtualization_tech_host' in facts
    assert 'virtualization_tech_guest' in facts

# Generated at 2022-06-13 04:11:13.963878
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    assert issubclass(OpenBSDVirtualCollector, VirtualCollector)
    assert OpenBSDVirtualCollector._fact_class is OpenBSDVirtual
    assert OpenBSDVirtualCollector._platform == 'OpenBSD'

# Generated at 2022-06-13 04:11:15.823913
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    virtual = OpenBSDVirtualCollector()
    assert virtual._platform == 'OpenBSD'
    assert virtual._fact_class == OpenBSDVirtual
    assert virtual.platform == 'OpenBSD'

# Generated at 2022-06-13 04:11:17.674749
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    class MyOpenBSDVirtualCollector(OpenBSDVirtualCollector):
        pass

    assert MyOpenBSDVirtualCollector(None, None)._fact_class == OpenBSDVirtual

# Generated at 2022-06-13 04:11:19.813002
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    facts_collector_obj = OpenBSDVirtualCollector()
    assert facts_collector_obj._fact_class.platform == 'OpenBSD'

# Generated at 2022-06-13 04:11:23.182916
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    # Test constructor of class OpenBSDVirtualCollector
    openbsd_virtual_collector = OpenBSDVirtualCollector()

    # Test the attribute of constructor
    assert openbsd_virtual_collector._platform == 'OpenBSD'

# Generated at 2022-06-13 04:11:32.037410
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual import OpenBSDVirtual
    from ansible.module_utils.facts.system.distribution import OpenBSDDistribution
    from ansible.module_utils.facts import FactManager

    manager = FactManager(collectors=[OpenBSDVirtualCollector, OpenBSDDistribution()])
    collected_facts = manager.collect(['virtual', 'distribution'])

    o = OpenBSDVirtual()
    o.platform = collected_facts['distribution']['name']
    o.distribution = collected_facts['distribution']
    o.sysctl = {'hw.product': 'VirtualBox', 'hw.vendor': 'OpenBSD'}


# Generated at 2022-06-13 04:11:40.202970
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    testobj = OpenBSDVirtual()
    testobj.dmesg_boot = 'test/test_utils/vmm_dmesg_boot'
    expected_virtual_facts = {
        'virtualization_role': 'host',
        'virtualization_type': 'vmm',
        'virtualization_tech_host': set(['vmm']),
        'virtualization_tech_guest': set([])
    }
    assert expected_virtual_facts == testobj.get_virtual_facts()

# Generated at 2022-06-13 04:11:48.090116
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    openbsd_virtual_collector = OpenBSDVirtualCollector()
    assert openbsd_virtual_collector._platform == 'OpenBSD'

# Generated at 2022-06-13 04:11:52.947400
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    openbsd_virtual = OpenBSDVirtual()
    openbsd_virtual.module = None

    openbsd_virtual.get_virtual_facts()

# Generated at 2022-06-13 04:11:57.509390
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # Create instance of OpenBSDVirtual
    openbsd_virtual = OpenBSDVirtual()

    # Create an empty dict and check if the result of get_virtual_facts
    # is in the same format
    facts = {}
    openbsd_virtual_facts = openbsd_virtual.get_virtual_facts()
    assert isinstance(openbsd_virtual_facts, dict)

# Generated at 2022-06-13 04:12:02.203305
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    obj = OpenBSDVirtualCollector()
    assert obj.platform == 'OpenBSD', 'Test failed! platform is not equal to OpenBSD.'
    assert obj.fact_class == OpenBSDVirtual, 'Test failed! fact_class is not equal to OpenBSDVirtual.'

# Generated at 2022-06-13 04:12:06.491846
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    openbsd_virtual_collector = OpenBSDVirtualCollector()
    assert openbsd_virtual_collector
    assert openbsd_virtual_collector._fact_class == OpenBSDVirtual
    assert openbsd_virtual_collector._platform == 'OpenBSD'

# Generated at 2022-06-13 04:12:13.027898
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    openbsdVirtual = OpenBSDVirtual()

    virtual_facts = openbsdVirtual.get_virtual_facts()
    assert sorted(virtual_facts['virtualization_tech_host']) == \
        sorted(['vmm'])
    assert sorted(virtual_facts['virtualization_tech_guest']) == \
        sorted([])

    assert virtual_facts['virtualization_type'] == 'vmm'
    assert virtual_facts['virtualization_role'] == 'host'


# Generated at 2022-06-13 04:12:17.307865
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    openbsd_virtual = OpenBSDVirtualCollector()
    output = openbsd_virtual.collect()

    assert output['virtualization_type'] == ''
    assert output['virtualization_role'] == ''
    assert output['virtualization_product'] == ''
    assert output['virtualization_product_version'] == ''

# Generated at 2022-06-13 04:12:24.017057
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virt = OpenBSDVirtual({})


# Generated at 2022-06-13 04:12:27.448333
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    openbsd_virtual = OpenBSDVirtual()
    openbsd_virtual_facts = openbsd_virtual.get_virtual_facts()
    assert isinstance(openbsd_virtual_facts, dict)

# Generated at 2022-06-13 04:12:32.548595
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    expected_facts = {'virtual_facts':
                          {'virtualization_role': 'guest',
                           'virtualization_type': 'vmm',
                           'virtualization_technologies': {'vmm'}
                           },
                      }
    virt_facts = OpenBSDVirtual().get_virtual_facts()
    assert virt_facts['virtualization_role'] in expected_facts['virtual_facts']['virtualization_role']
    assert virt_facts['virtualization_type'] in expected_facts['virtual_facts']['virtualization_type']
    assert virt_facts['virtualization_tech_guest'] == expected_facts['virtual_facts']['virtualization_technologies']

# Generated at 2022-06-13 04:12:45.352944
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    virtual_collector = OpenBSDVirtualCollector()
    assert virtual_collector._platform == 'OpenBSD'
    assert virtual_collector._fact_class == OpenBSDVirtual

# Generated at 2022-06-13 04:12:50.889106
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    test_class = OpenBSDVirtual()
    with open(OpenBSDVirtual.DMESG_BOOT) as fd:
        test_class.DMESG_BOOT = fd.name

    result = test_class.get_virtual_facts()
    assert result['virtualization_type'] == 'vmm'
    assert result['virtualization_role'] == 'host'

# Generated at 2022-06-13 04:12:54.201620
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    openbsd_virtual_collector = OpenBSDVirtualCollector()
    assert openbsd_virtual_collector._platform == 'OpenBSD'
    assert openbsd_virtual_collector._fact_class == OpenBSDVirtual

# Generated at 2022-06-13 04:12:56.748318
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    openbsd_collector = OpenBSDVirtualCollector()
    assert openbsd_collector._fact_class == OpenBSDVirtual
    assert openbsd_collector._platform == 'OpenBSD'

# Generated at 2022-06-13 04:12:58.135908
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    openbsd = OpenBSDVirtual({})
    openbsd.get_virtual_facts()

# Generated at 2022-06-13 04:13:04.038241
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    host_facts = dict()
    expected_facts = {'virtualization_type': 'vmm', 'virtualization_role': 'host', 'virtualization_tech_guest': set(), 'virtualization_tech_host': {'vmm'}}
    openbsd_virtual = OpenBSDVirtual(host_facts)
    resp_facts = openbsd_virtual.get_virtual_facts()
    assert resp_facts == expected_facts

# Generated at 2022-06-13 04:13:08.111372
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    """Test OpenBSDVirtualCollector constructor"""
    o = OpenBSDVirtualCollector()
    assert o.platform == 'OpenBSD'
    assert o._fact_class.platform == 'OpenBSD'
    assert issubclass(o._fact_class, Virtual)
    assert isinstance(o._fact_class(), Virtual)

# Generated at 2022-06-13 04:13:10.803688
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    result = OpenBSDVirtual().get_virtual_facts()
    assert 'virtualization_type' in result
    assert 'virtualization_role' in result
    assert 'virtualization_tech_guest' in result
    assert 'virtualization_tech_host' in result

# Generated at 2022-06-13 04:13:19.686574
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.sysctl import VirtualSysctlDetectionMixin

    class FakeOpenBSDVirtual(OpenBSDVirtual, VirtualSysctlDetectionMixin):
        def detect_virt_product(self, sysctl_param):
            return dict(virtualization_type='', virtualization_role='', virtualization_product='', virtualization_tech_guest={}, virtualization_tech_host={})

        def detect_virt_vendor(self, sysctl_param):
            return dict(virtualization_type='vmm', virtualization_role='host', virtualization_product='', virtualization_tech_guest={}, virtualization_tech_host={})

    obj = FakeOpenBSDVirtual()
    facts = obj.get_virtual_facts()

    assert facts['virtualization_role'] == 'host'

# Generated at 2022-06-13 04:13:22.336895
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    expected = {
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set(),
        'virtualization_role': '',
        'virtualization_type': '',
        'virtualization_sysctl_support': True
    }
    result = OpenBSDVirtualCollector()
    assert result._fact_class._platform == expected['platform']
    assert result._fact_class.DMESG_BOOT == expected['platform']

# Generated at 2022-06-13 04:13:46.807385
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    assert issubclass(OpenBSDVirtualCollector, VirtualCollector)
    assert OpenBSDVirtualCollector._platform == 'OpenBSD'
    assert OpenBSDVirtualCollector._fact_class == OpenBSDVirtual


# Generated at 2022-06-13 04:13:48.863080
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    assert OpenBSDVirtualCollector._platform == 'OpenBSD'
    assert OpenBSDVirtualCollector._fact_class == OpenBSDVirtual

# Generated at 2022-06-13 04:13:58.897216
# Unit test for method get_virtual_facts of class OpenBSDVirtual

# Generated at 2022-06-13 04:14:05.615302
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virtual_facts = OpenBSDVirtual()
    virtual_facts_values = virtual_facts.get_virtual_facts()

    # Test type and role of virtualization facts
    assert virtual_facts_values['virtualization_type'] in ['', 'physical']
    assert virtual_facts_values['virtualization_role'] in ['', 'guest']

    # Test virtualization tech guest and host
    assert 'virtualization_tech_guest' in virtual_facts_values
    assert 'virtualization_tech_host' in virtual_facts_values

# Generated at 2022-06-13 04:14:06.618948
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    assert OpenBSDVirtualCollector


# Generated at 2022-06-13 04:14:11.935996
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virtual_facts = {}
    virtual_facts['virtualization_type'] = ''
    virtual_facts['virtualization_role'] = ''
    virtual_facts['virtualization_sysctl_facts'] = {'machdep.memsize': '1073741824',
                                                    'hw.vendor': 'IBM',
                                                    'hw.product': 'IBM System z9',
                                                    'hw.ncpu': '4',
                                                    'hw.model': 'IBM zEnterprise z11 EKM'}

    virtual_facts['virtualization_tech_host'] = set()
    virtual_facts['virtualization_tech_guest'] = set()

    # Set data for detection of guest type
    hw_product = 'IBM System z9'

    virtual_facts['virtualization_type'] = ''


# Generated at 2022-06-13 04:14:15.689824
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    # Import only the class without instantiating it
    from ansible_collections.ansible.community.plugins.module_utils.facts.virtual.collector import OpenBSDVirtualCollector


# Generated at 2022-06-13 04:14:25.027935
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # Create a OpenBSDVirtual object
    openbsd_virtual_obj = OpenBSDVirtual(module=None, facts=None)
    # Test the method get_virtual_facts with a platform, a host and guest
    # capabilities
    assert {'virtualization_type': 'vmm',
            'virtualization_role': 'guest',
            'virtualization_tech_guest': set(['chroot', 'vmm']),
            'virtualization_tech_host': set(['vmm'])} \
            == openbsd_virtual_obj.get_virtual_facts(platform='OpenBSD',
                                                     vendor='OpenBSD',
                                                     product='OpenBSD')
    # Test the method get_virtual_facts with a platform, only host capabilities

# Generated at 2022-06-13 04:14:31.301371
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    """OpenBSDVirtual - get_virtual_facts() - virtualization_type
    """
    # Test for the case where hw.vendor is 'GenuineIntel' and hw.product
    # is 'QEMU Virtual CPU version (cpu64-rhel6)'
    # hw.vendor entry example:
    #   "hw.vendor=GenuineIntel"
    # hw.product entry example:
    #   "hw.product=QEMU Virtual CPU version (cpu64-rhel6)"
    facts_data = {}
    facts_data['hw_vendor'] = 'GenuineIntel'
    facts_data['hw_product'] = 'QEMU Virtual CPU version (cpu64-rhel6)'
    test_openbsdvirtual = OpenBSDVirtual({'ansible_facts': facts_data})
    result = test

# Generated at 2022-06-13 04:14:34.867054
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virtual_facts = OpenBSDVirtual().get_virtual_facts()
    # Check the virtualization_type is a string
    assert virtual_facts['virtualization_type'], ''

# Generated at 2022-06-13 04:15:02.650467
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    openbsd_virtual_collector = OpenBSDVirtualCollector()
    assert openbsd_virtual_collector._fact_class == OpenBSDVirtual
    assert openbsd_virtual_collector._platform == 'OpenBSD'

# Generated at 2022-06-13 04:15:05.980288
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    facts = {
        'kernel': 'OpenBSD',
        'os_family': 'OpenBSD',
        'virtual': 'OpenBSD'
    }
    instance = OpenBSDVirtual({})
    instance.get_virtual_facts()
    assert facts == instance.facts

# Generated at 2022-06-13 04:15:08.248403
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virt_facts = OpenBSDVirtual().get_virtual_facts()

    assert virt_facts['virtualization_type'] == 'vmm'
    assert virt_facts['virtualization_role'] == 'host'

# Generated at 2022-06-13 04:15:18.013101
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    openbsd_virtual = OpenBSDVirtual()
    # Mock dmesg.boot to test OpenBSD host
    openbsd_virtual.get_file_lines = lambda x: ['VMM: (SVM/RVI)']
    openbsd_virtual.get_file_content = lambda x: False
    facts = openbsd_virtual.get_virtual_facts()
    assert facts['virtualization_type'] == 'vmm'
    assert facts['virtualization_role'] == 'host'
    assert 'vmm' in facts['virtualization_tech_host']
    # Mock dmesg.boot to test OpenBSD guest
    openbsd_virtual.get_file_lines = lambda x: []
    facts = openbsd_virtual.get_virtual_facts()
    assert facts['virtualization_type'] == ''

# Generated at 2022-06-13 04:15:29.059450
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # Create mock object for set
    set_mock = set()
    # Create two instances of OpenBSDVirtual
    virtual_fact = OpenBSDVirtual()
    virtual_collector = OpenBSDVirtualCollector()

    # Return values for VirtualSysctlDetectionMixin.detect_virt_product
    def virt_product_side_effect(keyword):
        return {
            'virtualization_type': 'virtualbox',
            'virtualization_role': 'guest',
            'virtualization_tech_guest': set_mock,
            'virtualization_tech_host': set_mock
        }

    # Return values for VirtualSysctlDetectionMixin.detect_virt_vendor

# Generated at 2022-06-13 04:15:34.081959
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    openbsd_virtual_collector = OpenBSDVirtualCollector()
    assert openbsd_virtual_collector._platform == 'OpenBSD'
    assert openbsd_virtual_collector._fact_class.__name__ == 'OpenBSDVirtual'
    assert openbsd_virtual_collector._fact_class.platform == 'OpenBSD'


# Generated at 2022-06-13 04:15:34.924979
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    openbsd_virtual_collector = OpenBSDVirtualCollector()
    assert isinstance(openbsd_virtual_collector, OpenBSDVirtualCollector)

# Generated at 2022-06-13 04:15:39.905548
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virtual_facts = OpenBSDVirtual().get_virtual_facts()
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts
    assert 'virtual_packages' in virtual_facts
    assert 'virtual_pkgs_fullversion' in virtual_facts
    assert 'virtual_pkgs_version' in virtual_facts

# Generated at 2022-06-13 04:15:44.483947
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    facts = OpenBSDVirtualCollector()
    assert isinstance(facts, VirtualCollector)
    assert isinstance(facts, OpenBSDVirtualCollector)
    assert facts._platform == 'OpenBSD'
    assert facts._fact_class == OpenBSDVirtual

# Generated at 2022-06-13 04:15:46.953888
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    virt_collector = OpenBSDVirtualCollector()
    assert virt_collector._fact_class is not None
    assert virt_collector._platform == 'OpenBSD'



# Generated at 2022-06-13 04:16:53.016822
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    o = OpenBSDVirtual()
    virtual_facts = o.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'vmm'
    assert virtual_facts['virtualization_role'] == 'host'

# Generated at 2022-06-13 04:17:00.423176
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virtual_facts={}
    OpenBSDVirtual.get_virtual_facts(virtual_facts)

    # Check expected facts are defined
    assert 'virtualization_type' in virtual_facts, 'virtualization_type fact not defined'
    assert 'virtualization_role' in virtual_facts, 'virtualization_role fact not defined'
    assert 'virtualization_tech_guest' in virtual_facts, 'virtualization_tech_guest fact not defined'
    assert 'virtualization_tech_host' in virtual_facts, 'virtualization_tech_host fact not defined'

# Generated at 2022-06-13 04:17:01.267309
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    OpenBSDVirtualCollector()

# Generated at 2022-06-13 04:17:02.346991
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    vc = OpenBSDVirtualCollector()
    assert vc._platform == 'OpenBSD'

# Generated at 2022-06-13 04:17:03.972435
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    OpenBSDVirtualCollector()

# Generated at 2022-06-13 04:17:07.620111
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():

    # Initialize the collector object
    openbsd_virtual_collector = OpenBSDVirtualCollector()

    # Test the __init__ method
    assert openbsd_virtual_collector._platform == 'OpenBSD'
    assert openbsd_virtual_collector._fact_class == OpenBSDVirtual

# Generated at 2022-06-13 04:17:10.342601
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    openbsd_virtual = OpenBSDVirtualCollector(None)
    assert openbsd_virtual._fact_class == OpenBSDVirtual
    assert openbsd_virtual._platform == 'OpenBSD'

# Generated at 2022-06-13 04:17:17.959095
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # Create an instance of class OpenBSDVirtual
    test_virtual = OpenBSDVirtual()

    # Create a dict with expected virtual facts
    expected_virtual_facts = {}
    expected_virtual_facts['virtualization_type'] = 'vmm'
    expected_virtual_facts['virtualization_role'] = 'host'
    expected_virtual_facts['virtualization_tech_guest'] = set()
    expected_virtual_facts['virtualization_tech_host'] = set(['vmm'])

    # Asserts
    assert expected_virtual_facts == test_virtual.get_virtual_facts()

# Generated at 2022-06-13 04:17:22.419897
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    o = OpenBSDVirtual()
    virtual_facts = o.get_virtual_facts()
    assert 'virtualization_tech_guest' in virtual_facts.keys()
    assert 'virtualization_tech_host' in virtual_facts.keys()
    assert 'virtualization_type' in virtual_facts.keys()
    assert 'virtualization_role' in virtual_facts.keys()


# Generated at 2022-06-13 04:17:26.270212
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    vc = OpenBSDVirtualCollector()
    assert vc._fact_class is OpenBSDVirtual
    assert vc._platform is 'OpenBSD'


# Generated at 2022-06-13 04:19:53.481312
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # Initialize OpenBSDVirtual
    module = OpenBSDVirtual()

    # Expected values of virtual_facts
    expected_virtual_facts = dict(
        virtualization_type='vmm',
        virtualization_role='host',
        virtualization_tech_guest=set(),
        virtualization_tech_host=set(['vmm']),
        virt_what=[]
    )

    # Return value of method get_virtual_facts
    return_get_virtual_facts = module.get_virtual_facts()

    # Check answers
    assert return_get_virtual_facts == expected_virtual_facts