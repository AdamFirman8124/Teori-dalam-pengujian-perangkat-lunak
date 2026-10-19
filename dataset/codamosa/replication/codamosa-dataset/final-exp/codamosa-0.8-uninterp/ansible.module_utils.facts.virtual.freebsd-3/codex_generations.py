

# Generated at 2022-06-13 03:43:53.736864
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual = FreeBSDVirtual()
    virtual_facts = virtual.get_virtual_facts()

    assert virtual_facts['virtualization_type'] != ''
    assert virtual_facts['virtualization_role'] != ''

# Generated at 2022-06-13 03:44:02.353214
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    """
    Constructor of FreeBSDVirtualCollector should not fail when used with "with"
    and the context manager should return a FreeBSDVirtualCollector object.
    The collector should have a list of available virtual_facts, a running
    detect() function, and a running run() function.
    """
    with FreeBSDVirtualCollector() as collector:
        assert collector is not None
        assert hasattr(collector, 'virtual_facts')
        assert collector.virtual_facts

        # The collector should be able to march through the virtual reality.
        collector.detect()
        assert hasattr(collector, '_detected_facts')
        assert collector._detected_facts
        collector.run()
        assert hasattr(collector, '_collected_facts')
        assert collector._collected_facts

# Generated at 2022-06-13 03:44:05.398867
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    from ansible_collections.ansible.misc.tests.unit.modules.utils.virtual_facts.freebsd_virtual_facts import FreeBSDVirtualCollector
    FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:44:15.728415
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():

    sysctl_values = {
        'hw.hv_vendor': 'bhyve',
        'hw.model': 'FreeBSD/amd64',
        'security.jail.jailed': 1,
    }

    freebsd_vm_facts = FreeBSDVirtual({'module_setup': True}, sysctl_values)
    vm_facts = freebsd_vm_facts.get_virtual_facts()

    expected_vm_facts = {
        'virtualization_type': 'bhyve',
        'virtualization_role': 'host',
        'virtualization_tech_host': set(),
        'virtualization_tech_guest': {
            'jail',
        },
    }

    assert vm_facts == expected_vm_facts

# Generated at 2022-06-13 03:44:20.444020
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():

    testobj = FreeBSDVirtual({})
    result = testobj.get_virtual_facts()

    assert isinstance(result, dict)
    assert 'virtualization_type' in result
    assert 'virtualization_role' in result
    assert 'virtualization_tech_guest' in result
    assert 'virtualization_tech_host' in result

# Generated at 2022-06-13 03:44:22.466698
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    c = FreeBSDVirtualCollector()
    assert isinstance(c, VirtualCollector), "Unable to create FreeBSDVirtualCollector instance"

# Units test for constructor of class FreeBSDVirtual

# Generated at 2022-06-13 03:44:32.710680
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # Init the class and get the virtual facts
    freebsd_virtual = FreeBSDVirtual()
    virtual_facts = freebsd_virtual.get_virtual_facts()

    virtualization_type = virtual_facts.get('virtualization_type')
    virtualization_role = virtual_facts.get('virtualization_role')
    virtualization_tech_host = sorted(virtual_facts.get('virtualization_tech_host', set()))
    virtualization_tech_guest = sorted(virtual_facts.get('virtualization_tech_guest', set()))
    virtualization_product_name = virtual_facts.get('virtualization_product_name')

    # Testing
    assert virtualization_type != ''
    assert virtualization_role != ''
    assert virtualization_tech_host != []
    assert virtualization_tech_guest != []


# Generated at 2022-06-13 03:44:37.771842
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    facts = FreeBSDVirtual({})
    _virtual_facts = {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_tech_guest': set(['xen']),
        'virtualization_tech_host': set([])
    }
    assert facts.get_virtual_facts() == _virtual_facts

# Generated at 2022-06-13 03:44:47.229429
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual_facts = {}
    host_tech = set()

    # Set empty values as default
    virtual_facts['virtualization_type'] = ''
    virtual_facts['virtualization_role'] = ''
    virtual_facts['virtualization_tech_guest'] = []
    virtual_facts['virtualization_tech_host'] = []
    # For FreeBSD set the platform value
    virtual_facts['distribution'] = 'FreeBSD'

    if os.path.exists('/dev/xen/xenstore'):
        host_tech.add('xen')
        virtual_facts['virtualization_type'] = 'xen'
        virtual_facts['virtualization_role'] = 'guest'

    if virtual_facts['virtualization_type'] == '':
        virtual_facts['virtualization_tech_host'] = host_tech



# Generated at 2022-06-13 03:44:50.901399
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    facts = FreeBSDVirtual()
    virtual_facts = facts.get_virtual_facts()
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts

# Generated at 2022-06-13 03:44:55.884444
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    o = FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:45:07.446019
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    from collections import namedtuple
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat.mock import patch
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.facts.virtual.sysctl import VirtualSysctlDetectionMixin

    TestResult = namedtuple('TestResult', ['return_code', 'stdout', 'stderr'])

    def test_detect_virt_product_side_effect(*args, **kwargs):
        if args[0] == 'kern.vm_guest':
            test_result = TestResult(0, 'bsd', '')
        elif args[0] == 'hw.hv_vendor':
            test_result = TestResult(0, 'ACRN', '')

# Generated at 2022-06-13 03:45:08.305998
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert FreeBSDVirtualCollector._platform == 'FreeBSD'

# Generated at 2022-06-13 03:45:09.446104
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert isinstance(FreeBSDVirtualCollector(), VirtualCollector)

# Generated at 2022-06-13 03:45:21.119750
# Unit test for method get_virtual_facts of class FreeBSDVirtual

# Generated at 2022-06-13 03:45:23.329107
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    """Unit test for constructor of class FreeBSDVirtualCollector"""
    virtual_collector = FreeBSDVirtualCollector()
    assert isinstance(virtual_collector, FreeBSDVirtualCollector)

# Generated at 2022-06-13 03:45:26.245424
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    """
    Constructor of class FreeBSDVirtualCollector
    """
    freebsd_virtual_collector = FreeBSDVirtualCollector()
    assert freebsd_virtual_collector._fact_class == FreeBSDVirtual
    assert freebsd_virtual_collector._platform == 'FreeBSD'

# Generated at 2022-06-13 03:45:35.076872
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    """This unit test uses the following fixtures
    - test/units/module_utils/facts/virtual/virtual_fact_data.json
    """
    # Specify the named tuple fields

# Generated at 2022-06-13 03:45:36.480847
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():

    x = FreeBSDVirtualCollector()
    assert x._platform == 'FreeBSD'

# Generated at 2022-06-13 03:45:39.787225
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    v = FreeBSDVirtualCollector()
    assert v.platform == 'FreeBSD'
    assert v.fact_class ==  FreeBSDVirtual

# Generated at 2022-06-13 03:45:49.053538
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    v = FreeBSDVirtual({})
    v_facts = v.get_virtual_facts()
    assert v_facts.get('virtualization_type') in [ '', 'xen' ], \
        'virtualization_type not set or not set correctly'
    assert v_facts.get('virtualization_role') in [ '', 'guest' ], \
        'virtualization_role not set or not set correctly'

# Generated at 2022-06-13 03:45:54.052356
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # Create facts instance
    virtual = FreeBSDVirtual({})

    # Run method get_virtual_facts of class FreeBSDVirtual
    result = virtual.get_virtual_facts()

    # Check result.
    assert result is not None
    assert result['virtualization_type'] in ('xen', 'kvm', 'openvz', 'lxc')
    assert result['virtualization_role'] in ('guest', 'host', 'guest,host')

# Generated at 2022-06-13 03:45:56.648192
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual_facts = FreeBSDVirtual({}).get_virtual_facts()
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts

# Generated at 2022-06-13 03:46:01.780529
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    v = Virtual()
    facts = v.get_virtual_facts()
    assert facts['virtualization_role'] == 'guest'
    assert facts['virtualization_type'] in ('jail', 'xen')
    assert 'xen' in facts['virtualization_tech_guest']


# Generated at 2022-06-13 03:46:06.843685
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    target_obj = FreeBSDVirtualCollector()
    target_obj.collect()
    expected_obj = {
        'virtualization_role': 'guest',
        'virtualization_type': 'xen',
        'virtualization_technologies': {'guest': ['xen'], 'host': []}
    }

    assert expected_obj == target_obj.data

# Generated at 2022-06-13 03:46:08.397672
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    fv = FreeBSDVirtual()
    assert fv.get_virtual_facts() == {}

# Generated at 2022-06-13 03:46:13.197569
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual = FreeBSDVirtual()

    assert virtual.get_virtual_facts() == {
        'virtualization_type': 'xen',
        'virtualization_role': 'guest',
        'virtualization_tech_guest': set(['xen']),
        'virtualization_tech_host': set()
    }

# Generated at 2022-06-13 03:46:17.131456
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    f = FreeBSDVirtualCollector()
    assert isinstance(f,VirtualCollector)
    assert isinstance(f,FreeBSDVirtualCollector)
    assert not hasattr(f,'platform')
    assert isinstance(f.facts,FreeBSDVirtual)
    assert f.platform == 'FreeBSD'

# Generated at 2022-06-13 03:46:21.552683
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    v = FreeBSDVirtual()
    vfacts = v.get_virtual_facts()

    assert vfacts == {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set()
    }

# Generated at 2022-06-13 03:46:23.522654
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    facts = FreeBSDVirtual().get_virtual_facts()
    assert facts['virtualization_type'] == '' or \
        facts['virtualization_role'] == ''

# Generated at 2022-06-13 03:46:35.098414
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    from ansible.module_utils.facts import ansible_collector

    ansible_collector.collector.populate()
    collected_facts = ansible_collector.collector.fetch_facts(None, "FreeBSD", "", None, None)
    FreeBSD_virtual = FreeBSDVirtual({}, collected_facts)

    # FreeBSD in KVM
    virtual_facts = FreeBSD_virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'kvm'
    assert virtual_facts['virtualization_role'] == 'guest'
    assert 'kvm' in virtual_facts['virtualization_tech_guest']
    assert 'kvm' in virtual_facts['virtualization_tech_host']

    # FreeBSD in docker
    os.environ['container'] = 'docker'
    virtual_facts = FreeBSD_

# Generated at 2022-06-13 03:46:38.877710
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual_facts = FreeBSDVirtual({}).get_virtual_facts()
    assert isinstance(virtual_facts['virtualization_tech_host'], set)
    assert isinstance(virtual_facts['virtualization_tech_guest'], set)

# Generated at 2022-06-13 03:46:41.536339
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    collector = FreeBSDVirtualCollector()
    assert collector._platform == 'FreeBSD', 'platform should be FreeBSD'
    assert collector._fact_class == FreeBSDVirtual, 'should be FreeBSDVirtual'

# Generated at 2022-06-13 03:46:44.292711
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fvc = FreeBSDVirtualCollector()
    assert set(fvc.collector) == set([FreeBSDVirtual])
    assert fvc.platform == 'FreeBSD'



# Generated at 2022-06-13 03:46:51.324405
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    from ansible.module_utils.facts.virtual.freebsd import FreeBSDVirtualCollector
    from ansible.module_utils.facts.virtual.freebsd import FreeBSDVirtual
    virtual_collector = FreeBSDVirtualCollector()
    assert virtual_collector._platform == 'FreeBSD'
    assert virtual_collector._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:46:54.094948
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    # Constructor of class FreeBSDVirtualCollector should create an instance of class FreeBSDVirtualCollector
    class_name = FreeBSDVirtualCollector.__name__
    assert class_name == "FreeBSDVirtualCollector"

# Generated at 2022-06-13 03:47:02.864391
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    prototype_facts = {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_tech_guest': {},
        'virtualization_tech_host': {},
    }
    prototype_facts_1 = {
        'virtualization_type': 'xen',
        'virtualization_role': 'guest',
        'virtualization_tech_guest': {'xen'},
        'virtualization_tech_host': set(),
    }
    prototype_facts_2 = {
        'virtualization_type': 'bhyve',
        'virtualization_role': 'host',
        'virtualization_tech_guest': {'bhyve'},
        'virtualization_tech_host': set(),
    }

# Generated at 2022-06-13 03:47:11.785110
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual_params = {
    }
    expected_virtual_facts = {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_tech_guest': set([]),
        'virtualization_tech_host': set([])
    }

    mock_platform = 'FreeBSD'
    mock_sysctl = {
        'kern.vm_guest': 'freebsd',
        'security.jail.jailed': '0',
        'hw.hv_vendor': 'VMWare',
        'hw.model': 'VMWare Virtual Platform'
    }

    # Define methods to use for testing

# Generated at 2022-06-13 03:47:13.423879
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert(FreeBSDVirtualCollector._platform == 'FreeBSD')
    assert(FreeBSDVirtualCollector._fact_class == FreeBSDVirtual)

# Generated at 2022-06-13 03:47:15.003334
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    fd = FreeBSDVirtual({})
    fd.get_virtual_facts()

# Generated at 2022-06-13 03:47:30.177420
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    facts_dict = dict()
    facts_dict['virtualization_type'] = 'xen'
    facts_dict['virtualization_role'] = 'guest'
    facts_dict['virtualization_tech_guest'] = {'xen'}
    facts_dict['virtualization_tech_host'] = set()
    freebsd = FreeBSDVirtualCollector(facts_dict)
    assert freebsd.get_facts() == facts_dict

# Generated at 2022-06-13 03:47:31.831378
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    x = FreeBSDVirtualCollector()
    assert x.platform == 'FreeBSD'
    assert x._fact_class is not None

# Generated at 2022-06-13 03:47:33.541421
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    facts = FreeBSDVirtualCollector()
    assert type(facts) is FreeBSDVirtualCollector
    assert type(facts.collect()) is dict

# Generated at 2022-06-13 03:47:40.451916
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():

    class MockFreeBSDVirtual(FreeBSDVirtual):
        def __init__(self):
            self.sysctl_facts = {'kern.vm_guest': 'other',
                                 'hw.model': 'VMWare Virtual Platform',
                                 'security.jail.jailed': 0}

    testobj = MockFreeBSDVirtual()
    testobj.facts = {}

    facts = testobj.get_virtual_facts()
    assert facts['virtualization_type'] == 'vmware'
    assert facts['virtualization_role'] == 'guest'
    assert facts['virtualization_tech_guest'] == set(['vmware'])
    assert facts['virtualization_tech_host'] == set()


# Generated at 2022-06-13 03:47:47.705148
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    example_data = {'virtualization_type': '',
                    'virtualization_role': '',
                    'virtualization_tech_guest': set(),
                    'virtualization_tech_host': set()}
    facts_instance = FreeBSDVirtualCollector()
    assert facts_instance._fact_class.platform == 'FreeBSD'
    assert facts_instance._platform == 'FreeBSD'
    assert facts_instance._fact_class._platform == 'FreeBSD'
    assert facts_instance.get_facts() == example_data

# Generated at 2022-06-13 03:47:55.226709
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    from ansible.module_utils.facts import virtual
    from ansible.module_utils.facts.virtual.freebsd import Virtual, VirtualCollector
    from ansible.module_utils.facts.virtual.sysctl import VirtualSysctlDetectionMixin

    vc = virtual.VirtualCollector.factory()
    assert isinstance(vc, VirtualCollector)
    assert isinstance(vc, FreeBSDFacade)
    assert issubclass(vc._fact_class, Virtual)
    assert issubclass(vc._fact_class, VirtualSysctlDetectionMixin)

# Generated at 2022-06-13 03:47:55.717560
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    pass

# Generated at 2022-06-13 03:47:57.856152
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    myclass = FreeBSDVirtualCollector()
    assert hasattr(myclass, '_fact_class')
    assert hasattr(myclass, '_platform')


# Generated at 2022-06-13 03:48:04.353933
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    class TestFreeBSDVirtual(FreeBSDVirtual):
        def __init__(self, *args, **kwargs):
            self.kern_vm_guest_data = {'virtualization_tech_guest': set(),
                                       'virtualization_tech_host': set(),
                                       'virtualization_type': '',
                                       'virtualization_role': ''}
            self.hw_hv_vendor_data = {'virtualization_tech_guest': set(),
                                      'virtualization_tech_host': set(),
                                      'virtualization_type': '',
                                      'virtualization_role': ''}

# Generated at 2022-06-13 03:48:07.480958
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    collector = FreeBSDVirtualCollector()
    assert collector.platform == 'FreeBSD'
    assert collector._fact_class == FreeBSDVirtual


# Generated at 2022-06-13 03:48:39.457414
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.freebsd import FreeBSDVirtual
    from ansible.module_utils.facts.virtual.freebsd import (
        FreeBSDVirtualCollector as VirtualCollector
    )
    from ansible.module_utils.facts.virtual.freebsd import (
        VirtualSysctlDetectionMixin
    )
    facts = FreeBSDVirtualCollector().collect(None, None)
    # Check that the FreeBSDVirtual Class was chosen by the
    # VirtualCollector and the Virtual method called.
    assert isinstance(facts, FreeBSDVirtual)
    assert isinstance(facts, VirtualCollector)
    assert isinstance(facts, VirtualSysctlDetectionMixin)
    facts = facts.get_virtual_facts()
    assert facts['virtualization_type'] == 'xen'

# Generated at 2022-06-13 03:48:41.059989
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    # Note that the assertRaises() is expecting a type of exception.
    dummy_cls = VirtualCollector('')
    assertRaises(TypeError, dummy_cls)

# Generated at 2022-06-13 03:48:43.268943
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    '''Unit test constructor of class FreeBSDVirtualCollector'''
    virtual_facts_collector = FreeBSDVirtualCollector()

    assert virtual_facts_collector._platform == 'FreeBSD'
    assert virtual_facts_collector.platforms == ('FreeBSD',)
    assert virtual_facts_collector._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:48:54.580190
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual_facts_libvirtxml_host_guest = {
        'virtualization_type': 'kvm',
        'virtualization_role': 'host',
        'virtualization_tech_guest': set(['kvm']),
        'virtualization_tech_host': set(['kvm'])}
    virtual_facts_libvirtxml_guest = {
        'virtualization_type': 'kvm',
        'virtualization_role': 'guest',
        'virtualization_tech_guest': set(['kvm']),
        'virtualization_tech_host': set(['kvm'])}

# Generated at 2022-06-13 03:48:59.275554
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    module = FakeModule()
    fact_class = FreeBSDVirtual(module=module)
    virtual_facts = fact_class.get_virtual_facts()
    assert virtual_facts['virtualization_type'] is not None
    assert virtual_facts['virtualization_role'] is not None
    assert virtual_facts['virtualization_role'] == 'guest'
    assert virtual_facts['virtualization_type'] == 'xen'


# Generated at 2022-06-13 03:49:01.517123
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    collector = FreeBSDVirtualCollector()
    assert collector.platform == 'FreeBSD'
    assert collector.fact_class == FreeBSDVirtual
    assert collector.fact_class._platform == 'FreeBSD'

# Generated at 2022-06-13 03:49:04.475434
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    expected_platform = 'FreeBSD'
    expected_fact_class = FreeBSDVirtual

    fvc = FreeBSDVirtualCollector()
    platform = fvc._platform
    fact_class = fvc._fact_class

    assert platform == expected_platform
    assert fact_class == expected_fact_class

# Generated at 2022-06-13 03:49:05.398521
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    collection = FreeBSDVirtualCollector()
    assert collection is not None

# Generated at 2022-06-13 03:49:15.352482
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    '''Unit test for method get_virtual_facts of class FreeBSDVirtual.'''

    class TestFreeBSDVirtual(FreeBSDVirtual):
        '''A subclass of FreeBSDVirtual, using stubs for all external calls
        '''
        def __init__(self):
            super(TestFreeBSDVirtual, self).__init__()
            self.detect_virt_product_calls = []
            self.detect_virt_vendor_calls = []
        def detect_virt_product(self, product):
            self.detect_virt_product_calls.append(product)

# Generated at 2022-06-13 03:49:22.907108
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert FreeBSDVirtualCollector._platform == 'FreeBSD'
    assert FreeBSDVirtualCollector._fact_class == FreeBSDVirtual
    assert FreeBSDVirtualCollector.platform == 'FreeBSD'
    assert FreeBSDVirtualCollector.fact_class == FreeBSDVirtual

# Test that all sysctls from __virtual__ can be found
# Test that all sysctls from __virtual_vendor__ can be found
# Test that all sysctls from __virtual_sysctl__ can be found
# Test that all sysctls from get_virtual_facts() can be found

# Generated at 2022-06-13 03:50:17.887033
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    collect = FreeBSDVirtualCollector()
    assert collect.platform == "FreeBSD"
    assert collect._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:50:19.625817
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    clc = FreeBSDVirtualCollector('FreeBSD')
    assert clc.platform == 'FreeBSD'
    assert clc._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:50:21.065034
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    vc = FreeBSDVirtualCollector()
    assert isinstance(vc._fact_class, FreeBSDVirtual)

# Generated at 2022-06-13 03:50:23.083155
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    x = FreeBSDVirtualCollector()
    assert x._platform == "FreeBSD"
    assert issubclass(x._fact_class, Virtual)


# Generated at 2022-06-13 03:50:24.354055
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual = FreeBSDVirtual("FreeBSD", "")
    virtual.get_virtual_facts()

# Generated at 2022-06-13 03:50:33.936405
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # Get current directory and path of this file
    cur_dir = os.path.dirname(os.path.realpath(__file__))

    # Create object
    objFreeBSDVirtual = FreeBSDVirtual()

    # Get virtual facts for 'FreeBSD'
    objFreeBSDVirtual.get_virtual_facts()

    # Get values from virtual facts
    virtual_type = objFreeBSDVirtual.virtual_facts['virtualization_type']
    virtual_role = objFreeBSDVirtual.virtual_facts['virtualization_role']
    virtual_tech_guest = objFreeBSDVirtual.virtual_facts['virtualization_tech_guest']
    virtual_tech_host = objFreeBSDVirtual.virtual_facts['virtualization_tech_host']

    # Assertion for virtualization_type

# Generated at 2022-06-13 03:50:35.867971
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    '''
    Test to verify correct creation of FreeBSDVirtualCollector instance
    '''
    assert FreeBSDVirtualCollector()._platform == 'FreeBSD'

# Generated at 2022-06-13 03:50:42.306665
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    s = {}

    s['kern.vm_guest'] = 'None'
    s['hw.hv_vendor'] = 'None'
    s['security.jail.jailed'] = 'None'
    s['hw.model'] = 'amd64'

    v = FreeBSDVirtual(s, False, 'freebsd')
    vf = v.get_virtual_facts()

    assert vf['virtualization_type'] == ''
    assert vf['virtualization_role'] == ''
    assert 'xen' not in vf['virtualization_tech_guest']
    assert 'xen' not in vf['virtualization_tech_host']
    assert 'kvm' not in vf['virtualization_tech_guest']
    assert 'kvm' not in vf['virtualization_tech_host']


# Generated at 2022-06-13 03:50:48.473571
# Unit test for method get_virtual_facts of class FreeBSDVirtual

# Generated at 2022-06-13 03:50:51.049181
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert isinstance(FreeBSDVirtualCollector(), VirtualCollector)
    assert FreeBSDVirtualCollector()._platform == 'FreeBSD'
    assert isinstance(FreeBSDVirtualCollector()._fact_class, FreeBSDVirtual)


# Generated at 2022-06-13 03:52:38.609370
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    import json
    import subprocess
    vf = FreeBSDVirtual()
    result = vf.get_virtual_facts()
    assert result['virtualization_type'] == ''
    assert result['virtualization_role'] == ''

# Generated at 2022-06-13 03:52:39.624057
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert isinstance(FreeBSDVirtualCollector(), VirtualCollector)

# Generated at 2022-06-13 03:52:42.371808
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    ''' Constructor test for FreeBSDVirtualCollector '''
    freebsd_virtual_collector = FreeBSDVirtualCollector()
    assert freebsd_virtual_collector._fact_class is FreeBSDVirtual
    assert freebsd_virtual_collector._platform == 'FreeBSD'

# Generated at 2022-06-13 03:52:43.758964
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    d = FreeBSDVirtualCollector()
    assert d._platform == 'FreeBSD'
    assert isinstance(d._fact_class(d), FreeBSDVirtual)

# Generated at 2022-06-13 03:52:46.152494
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virt = FreeBSDVirtual({})
    virtual_facts = virt.get_virtual_facts()
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts


# Generated at 2022-06-13 03:52:52.168951
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    class MyFreeBSDVirtualCollector(FreeBSDVirtualCollector):
        def __init__(self, **kwargs):
            super(MyFreeBSDVirtualCollector, self).__init__(**kwargs)
            self.kwargs = kwargs

    myfreebsdvirtualcollector = MyFreeBSDVirtualCollector(
        module=None,
        additional_facts={}
    )
    assert myfreebsdvirtualcollector.platform == 'FreeBSD'
    assert myfreebsdvirtualcollector._fact_class == FreeBSDVirtual


# Generated at 2022-06-13 03:52:54.459572
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    '''
        Checks if _fact_class is FreeBSDVirtual and _platform is FreeBSD
    '''
    f = FreeBSDVirtualCollector(None)
    assert f._fact_class == FreeBSDVirtual
    assert f._platform == 'FreeBSD'


# Generated at 2022-06-13 03:52:55.783558
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    test_object = FreeBSDVirtualCollector()
    assert test_object._fact_class == FreeBSDVirtual
    assert test_object._platform == 'FreeBSD'

# Generated at 2022-06-13 03:53:00.561435
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    class FakeSysctl(object):
        def __init__(self):
            self.xen_kern_vm_guest = None
            self.hw_hv_vendor = None
            self.security_jail_jailed = None
            self.hw_model = None

    fake_sysctl = FakeSysctl()

    class FakeHardware(object):
        def __init__(self, sysctl):
            self.sysctl = sysctl

        def detect_hw(self):
            return {
                'manufacturer': 'GenuineIntel',
                'product_name': ''
            }

    fake_hardware = FakeHardware(fake_sysctl)

    class FakeFreeBSDVirtual(FreeBSDVirtual):
        def __init__(self, sysctl, hardware):
            self.sysctl = sysctl
            self.hardware

# Generated at 2022-06-13 03:53:02.561920
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    f = FreeBSDVirtualCollector()
    assert f.platform == 'FreeBSD'
    assert f._fact_class  == FreeBSDVirtual