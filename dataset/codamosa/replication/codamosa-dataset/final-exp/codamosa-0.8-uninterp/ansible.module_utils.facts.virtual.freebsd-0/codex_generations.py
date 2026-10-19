

# Generated at 2022-06-13 03:43:59.533062
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    """ Method 'get_virtual_facts' return correct virtual info for FreeBSD """
    # FreeBSD guest on bhyve
    #
    # virtualization_type=bhyve
    # virtualization_role=guest
    # virtualization_tech_guest=bhyve,freebsd
    # virtualization_tech_host=bhyve,freebsd
    _facts_kern_vm_guest = {
        'kern.vm_guest': 'bhyve',
        'hw.hv_vendor': '',
        'security.jail.jailed': '0',
        'hw.model': 'FreeBSD/amd64',
    }

    # FreeBSD jail
    #
    # virtualization_type=jail
    # virtualization_role=guest
    # virtualization_tech_guest=free

# Generated at 2022-06-13 03:44:01.292824
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    freebsd_collector = FreeBSDVirtualCollector()
    assert freebsd_collector.platform == 'FreeBSD'
    assert freebsd_collector._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:44:05.714060
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # Setup an instance of FreeBSDVirtual inside a FreeBSDVirtualCollector
    # instance, and then call its get_virtual_facts() method.
    facts = FreeBSDVirtual(FreeBSDVirtualCollector()).get_virtual_facts()
    assert 'virtualization_type' in facts
    assert 'virtualization_role' in facts

# Generated at 2022-06-13 03:44:07.138742
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert FreeBSDVirtualCollector._platform == 'FreeBSD'
    assert FreeBSDVirtualCollector._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:44:10.508649
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    obj_vf_freebsd = FreeBSDVirtualCollector()
    assert obj_vf_freebsd.platform == 'FreeBSD'

# Generated at 2022-06-13 03:44:12.148549
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    facts = FreeBSDVirtualCollector()
    assert "FreeBSDVirtual" == facts._fact_class.__name__

# Generated at 2022-06-13 03:44:21.777609
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # Patch sysctl_get, when called with only one argument.
    # In this case, the return value is hardcoded.
    # The second argument is the name of the variable, on which the return value
    # depends.
    def sysctl_get(name, variable):
        return {
            'kern.vm_guest': {
                'none': None,
                'freebsd': 'FreeBSD'
            },
            'hw.hv_vendor': {
                'none': None,
                'bhyve': 'bhyve'
            },
            'security.jail.jailed': {
                'no': 0,
                'yes': 1
            }
        }[name][variable]

    # Patch file_exists, when called with only one argument.
    # In this case, the return value is hard

# Generated at 2022-06-13 03:44:22.722965
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert FreeBSDVirtualCollector._platform == 'FreeBSD'

# Generated at 2022-06-13 03:44:29.612030
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    detect_virt_product = lambda x: {'virtualization_tech_guest': set(),
                                     'virtualization_tech_host': set(),
                                     'virtualization_type': '',
                                     'virtualization_role': ''}
    detect_virt_vendor = lambda x: {'virtualization_tech_guest': set(),
                                    'virtualization_tech_host': set(),
                                    'virtualization_type': '',
                                    'virtualization_role': ''}

# Generated at 2022-06-13 03:44:32.425756
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fvc = FreeBSDVirtualCollector()
    assert isinstance(fvc, VirtualCollector)
    assert isinstance(fvc._fact_class, FreeBSDVirtual)
    assert fvc._platform == 'FreeBSD'

# Generated at 2022-06-13 03:44:42.890528
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    """Unit test function get_virtual_facts of FreeBSDVirtual class
    """
    virtual_facts = {
        'virtualization_role': 'guest',
        'virtualization_type': 'xen',
        'virtualization_tech_guest': set(['xen']),
        'virtualization_tech_host': set([])
    }
    fbsd_virtual = FreeBSDVirtual()
    assert fbsd_virtual.get_virtual_facts() == virtual_facts

# Generated at 2022-06-13 03:44:44.486535
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    c = FreeBSDVirtualCollector()
    assert isinstance(c, FreeBSDVirtualCollector)


# Generated at 2022-06-13 03:44:45.732056
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert FreeBSDVirtualCollector(None).platform == 'FreeBSD'


# Generated at 2022-06-13 03:44:51.261947
# Unit test for method get_virtual_facts of class FreeBSDVirtual

# Generated at 2022-06-13 03:44:54.317615
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert FreeBSDVirtualCollector._fact_class == FreeBSDVirtual
    assert FreeBSDVirtualCollector._platform == 'FreeBSD'

# Generated at 2022-06-13 03:44:58.771354
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    """
    Method get_virtual_facts of class FreeBSDVirtual
    should return a dictionary containing multiple items
    I assume that these items are the same as in
    platform_virtual_facts of class
    PlatformVirtualFactsCollector.
    """
    facts = FreeBSDVirtual()
    result = facts.get_virtual_facts()
    assert isinstance(result, dict)


# Test to verify that FreeBSDVirtualCollector class exists

# Generated at 2022-06-13 03:45:00.598275
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert FreeBSDVirtualCollector._platform == 'FreeBSD'
    assert FreeBSDVirtualCollector._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:45:04.743867
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    f = FreeBSDVirtualCollector()
    assert f._module_name == 'ansible.module_utils.facts.virtual.freebsd'
    assert f._fact_class == FreeBSDVirtual
    assert f._platform == 'FreeBSD'

# Generated at 2022-06-13 03:45:15.522294
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    from collections import namedtuple
    from ansible.module_utils.facts.virtual.sysctl import (
        VirtualSysctlDetectionMixin,
    )
    from ansible.module_utils.facts.virtual.base import Virtual, VirtualCollector
    from ansible.module_utils.facts.virtual.freebsd import (
        FreeBSDVirtual,
    )

    Data = namedtuple('Data', (
        'kern.vm_guest', 'hw.hv_vendor', 'security.jail.jailed', 'hw.model'
    ))

    ansible_module_mock = type('ansible_module_mock', (object, ), {})

    class MockVirtual(Virtual):
        def __init__(self, *args, **kwargs):
            pass


# Generated at 2022-06-13 03:45:24.371511
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    class MockSudo:
        def __init__(self, data):
            self.data = data

        def read_file(self, filename):
            return self.data[filename]

    def mock_isfile(filename):
        return filename in data


# Generated at 2022-06-13 03:45:32.355635
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_collector = FreeBSDVirtualCollector()
    assert virtual_collector.platform == 'FreeBSD'
    assert virtual_collector.collectors[0].platform == 'FreeBSD'
    assert virtual_collector.collectors[0]._platform == 'FreeBSD'
    assert isinstance(virtual_collector.collectors[0], FreeBSDVirtual)

# Generated at 2022-06-13 03:45:33.854009
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    fake_sysctl = FakeSysctl()
    f = FreeBSDVirtual({}, fake_sysctl)
    assert f.get_virtual_facts() == virtual_facts



# Generated at 2022-06-13 03:45:36.388873
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    facts = FreeBSDVirtualCollector()
    result = facts
    assert result._fact_class == FreeBSDVirtual
    assert result._platform == 'FreeBSD'


# Generated at 2022-06-13 03:45:40.412654
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    '''Unit test for constructor of class FreeBSDVirtualCollector'''
    collector = FreeBSDVirtualCollector()
    assert collector.platform == 'FreeBSD'
    assert collector._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:45:50.396728
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    from unittest import TestCase
    from mock import Mock

    sysctl = {'kern.vm_guest': 'vkernel',
              'hw.hv_vendor': 'bhyve',
              'security.jail.jailed': 0}

    facts = {'hw.model': '',
             'virtualization_type': '',
             'virtualization_role': '',
             'virtualization_tech_host': set(),
             'virtualization_tech_guest': set()}

    my_object = FreeBSDVirtual()

    def side_effect(name):
        return sysctl[name]

    with TestCase.assertRaises(TestCase, SystemExit) as cm:
        facts.update(my_object.get_virtual_facts())

# Generated at 2022-06-13 03:45:52.208525
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    obj = FreeBSDVirtualCollector()
    assert obj._platform == 'FreeBSD'
    assert isinstance(obj._fact_class, FreeBSDVirtual)

# Generated at 2022-06-13 03:45:56.552647
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual_facts = FreeBSDVirtual()
    assert virtual_facts.get_virtual_facts() == dict(
        virtualization_type='',
        virtualization_role='',
        virtualization_tech_guest=set(),
        virtualization_tech_host=set()
    )

# Generated at 2022-06-13 03:46:02.511619
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # Call method under test
    virtual = FreeBSDVirtual()
    virtual_facts = virtual.get_virtual_facts()

    assert 'virtualization_type' in virtual_facts
    assert len(virtual_facts['virtualization_type']) > 0
    assert 'virtualization_role' in virtual_facts
    assert len(virtual_facts['virtualization_role']) > 0

# Generated at 2022-06-13 03:46:08.859949
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    facts = dict()
    freebsd_facts = dict()
    freebsd_facts['virtualization_role'] = ''
    freebsd_facts['virtualization_type'] = ''
    freebsd_facts['virtualization_tech_guest'] = set()
    freebsd_facts['virtualization_tech_host'] = set()
    facts['ansible_virtual'] = freebsd_facts
    assert FreeBSDVirtualCollector(facts, None).data == facts


# Generated at 2022-06-13 03:46:12.028610
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_collector = FreeBSDVirtualCollector()
    assert virtual_collector._platform == 'FreeBSD'
    assert virtual_collector._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:46:24.459610
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_collector = FreeBSDVirtualCollector()
    assert virtual_collector.platform == 'FreeBSD'
    assert virtual_collector.fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:46:26.307477
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual_facts = FreeBSDVirtual()

    # On a FreeBSD box
    assert len(virtual_facts.get_virtual_facts()) == 4

# Generated at 2022-06-13 03:46:29.580995
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # Virtualisation management detection
    assert FreeBSDVirtual().get_virtual_facts() == {
        'virtualization_role': '',
        'virtualization_type': '',
        'virtualization_technologies_guest': set(),
        'virtualization_technologies_host': set()
    }

# Generated at 2022-06-13 03:46:31.567639
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_facts = FreeBSDVirtualCollector(None).collect()
    # virtual_facts is empty
    assert (virtual_facts is None) or (len(virtual_facts) == 0)

# Generated at 2022-06-13 03:46:32.583869
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert FreeBSDVirtualCollector.virtual

# Generated at 2022-06-13 03:46:34.676585
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    test = FreeBSDVirtual()
    test.get_virtual_facts()

# Generated at 2022-06-13 03:46:36.617771
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    collector = FreeBSDVirtualCollector()
    assert isinstance(collector,FreeBSDVirtualCollector)

# Generated at 2022-06-13 03:46:46.572702
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():

    v = FreeBSDVirtual()

    # Set up mock sysctl data for a VM detection
    mock_sysctl_data = {}
    mock_sysctl_data['kern.vm_guest'] = 'vmware'
    mock_sysctl_data['hw.hv_vendor'] = 'bhyve'
    mock_sysctl_data['security.jail.jailed'] = 0
    v._sysctl = mock_sysctl_data

    # Set up mock model data for a VM detection
    mock_model_data = {}
    mock_model_data['hw_model'] = 'VMware Virtual Platform'
    mock_model_data['model'] = 'VMware Virtual Platform'
    v._product_name_data = mock_model_data


# Generated at 2022-06-13 03:46:57.282283
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual = FreeBSDVirtual('')

    # Mock sysctl output

# Generated at 2022-06-13 03:46:59.750284
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_collector = FreeBSDVirtualCollector()
    assert virtual_collector._platform == 'FreeBSD'
    assert virtual_collector._fact_class is FreeBSDVirtual

# Generated at 2022-06-13 03:47:17.325454
# Unit test for method get_virtual_facts of class FreeBSDVirtual

# Generated at 2022-06-13 03:47:21.362292
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # This is a FreeBSD system
    freebsd_virtual = FreeBSDVirtual()
    expected = {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set(),
    }
    res = freebsd_virtual.get_virtual_facts()
    assert res == expected

# Generated at 2022-06-13 03:47:24.938818
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_collector = FreeBSDVirtualCollector()
    assert isinstance(virtual_collector, FreeBSDVirtualCollector)
    assert virtual_collector._platform == 'FreeBSD'
    assert virtual_collector._fact_class == FreeBSDVirtual


# Generated at 2022-06-13 03:47:26.546590
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    collector = FreeBSDVirtualCollector()
    assert collector._platform == 'FreeBSD'
    assert collector._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:47:28.857589
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    foo = FreeBSDVirtualCollector()
    assert foo._fact_class == FreeBSDVirtual
    assert foo._platform == 'FreeBSD'


# Generated at 2022-06-13 03:47:29.434887
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:47:36.969951
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    from ansible.module_utils import basic
    from ansible.module_utils.facts import collector
    # setup basic args
    set_module_args = dict(gather_subset='virtual')
    with basic.AnsibleModule(argument_spec={}) as module:
        module.exit_json = basic.exit_json
        # Get facts
        facts_instance = collector.get_collector(
            'network',
            config=module._config,
        ).get_facts(module)
        facts = facts_instance.get_facts()
        # Set arguments for specific test case
        module.params = dict(gather_subset='network', filter=['interfaces'])
        # start test
        freebsd_virtual_instance = FreeBSDVirtual(module)
        virtual_facts = freebsd_virtual_instance.get_virtual

# Generated at 2022-06-13 03:47:38.926413
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    facts = FreeBSDVirtual().get_virtual_facts()
    assert facts['virtualization_type'] in ['', 'xen']
    assert facts['virtualization_role'] in ['', 'guest']

# Generated at 2022-06-13 03:47:45.088496
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    import ansible_collections.ansible.community.plugins.module_utils.facts.virtual.freebsd
    import collections
    import pprint
    from ansible_collections.ansible.community.plugins.module_utils.facts.virtual.sysctl import VirtualSysctlDetectionMixin

    # UNIT TEST: Init FreeBSDVirtualCollector and check implemented class
    facts = FreeBSDVirtualCollector()
    assert isinstance(facts, collections.Callable)
    assert isinstance(facts, VirtualSysctlDetectionMixin)
    assert isinstance(facts, FreeBSDVirtualCollector)
    assert isinstance(facts._fact_class, FreeBSDVirtual)
    assert isinstance(facts._platform, str)
    assert facts.platform == 'FreeBSD'
    # UNIT TEST: get_virtual_facts()

# Generated at 2022-06-13 03:47:47.391055
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    c = FreeBSDVirtualCollector()
    assert type(c) == FreeBSDVirtualCollector


# Generated at 2022-06-13 03:48:00.790779
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:48:01.696292
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    collector = FreeBSDVirtualCollector()
    assert isinstance(collector._fact_class, Virtual)


# Generated at 2022-06-13 03:48:03.286263
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    x = FreeBSDVirtualCollector()
    assert x.platform == 'FreeBSD'
    assert x._fact_class.platform == 'FreeBSD'


# Generated at 2022-06-13 03:48:04.890445
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual = FreeBSDVirtual()
    data = virtual.get_virtual_facts()
    assert 'virtualization_type' in data

# Generated at 2022-06-13 03:48:08.117843
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    pytest_virtual_collector = FreeBSDVirtualCollector()
    assert isinstance(pytest_virtual_collector,
                      FreeBSDVirtualCollector)

# Generated at 2022-06-13 03:48:11.372972
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_collector = FreeBSDVirtualCollector()
    assert virtual_collector._platform == 'FreeBSD'
    assert virtual_collector._fact_class == FreeBSDVirtual


# Generated at 2022-06-13 03:48:13.907611
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    f = FreeBSDVirtualCollector()
    assert f._platform == 'FreeBSD'
    assert f._fact_class == FreeBSDVirtual
    assert f._fact_class().platform == 'FreeBSD'

# Generated at 2022-06-13 03:48:17.292790
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual = FreeBSDVirtual()
    virtual_facts = virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'xen'
    assert 'virtualbox' in virtual_facts['virtualization_tech_guest']
    assert 'virtualbox' in virtual_facts['virtualization_tech_host']

# Generated at 2022-06-13 03:48:18.620318
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    x = FreeBSDVirtualCollector()
    assert x._platform == 'FreeBSD'
    assert x._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:48:20.199802
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    x = FreeBSDVirtualCollector()
    assert isinstance(x, VirtualCollector)

# Generated at 2022-06-13 03:48:58.779300
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:49:00.324953
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fvc = FreeBSDVirtualCollector('')
    assert fvc.platform == 'FreeBSD'

# Generated at 2022-06-13 03:49:01.597544
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert issubclass(FreeBSDVirtualCollector, VirtualCollector)


# Generated at 2022-06-13 03:49:03.351068
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    try:
        FreeBSDVirtualCollector()
    except NameError:
        assert(False)
# Unit test end


# Generated at 2022-06-13 03:49:09.543263
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    """
    Unit test for method get_virtual_facts of class FreeBSDVirtual.
    """
    NO_VIRT_TYPE = ''
    NO_VIRT_ROLE = ''
    NO_VIRT_TECH_GUEST = set()
    NO_VIRT_TECH_HOST = set()

    virtual_type = 'xen'
    virtual_role = 'guest'
    virtual_tech_guest = set()
    virtual_tech_host = set()

    facts = {
        'virtualization_type': NO_VIRT_TYPE,
        'virtualization_role': NO_VIRT_ROLE,
        'virtualization_tech_guest': NO_VIRT_TECH_GUEST,
        'virtualization_tech_host': NO_VIRT_TECH_HOST
    }

    mock_facts

# Generated at 2022-06-13 03:49:12.791098
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    '''Unit test for constructor of class FreeBSDVirtualCollector'''
    assert FreeBSDVirtualCollector._platform == 'FreeBSD'
    assert FreeBSDVirtualCollector._fact_class.platform == 'FreeBSD'


# Generated at 2022-06-13 03:49:15.193021
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    vdObj1 = Virtual( module=None )
    vdObj2 = FreeBSDVirtual( module=None )
    assert vdObj1.get_virtual_facts() == vdObj2.get_virtual_facts()

# Generated at 2022-06-13 03:49:16.202287
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    """This is a virtual test for FreeBSD"""
    assert True

# Generated at 2022-06-13 03:49:18.594341
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert isinstance(FreeBSDVirtualCollector(None), VirtualCollector)

# Generated at 2022-06-13 03:49:22.784818
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    freebsd_virtual = FreeBSDVirtualCollector()
    assert freebsd_virtual._fact_class is not None
    assert freebsd_virtual._fact_class.platform == 'FreeBSD'
    assert freebsd_virtual._platform == 'FreeBSD'
    assert freebsd_virtual.collect()['virtualization_type'] != ''

# Generated at 2022-06-13 03:50:32.614908
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    detect = FreeBSDVirtualCollector()
    assert detect._platform == 'FreeBSD'
    assert detect._fact_class.platform == 'FreeBSD'


# Generated at 2022-06-13 03:50:40.248220
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    fv = FreeBSDVirtual()

    def create(name, value):
        return {'sysctl': {name: value}}


# Generated at 2022-06-13 03:50:42.785554
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_collector = FreeBSDVirtualCollector()
    assert virtual_collector._platform == 'FreeBSD'
    assert virtual_collector._fact_class is not None

# Generated at 2022-06-13 03:50:43.899281
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fbc = FreeBSDVirtualCollector()
    assert fbc.platform == 'FreeBSD'
    assert fbc._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:50:46.659316
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    os.environ['PROCFS_PATH'] = os.environ['PROCFS'] = os.environ['SYSCTL'] = os.environ['CMDLINE'] = '/'
    __virtualcollector = FreeBSDVirtualCollector()
    assert __virtualcollector.platform == 'FreeBSD'
    assert __virtualcollector.fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:50:51.368855
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():

    # Test Xen host
    with open('/proc/xen/capabilities', 'w') as f:
        f.write('control_d\n')

    # Test FreeBSD jail host
    os.mkdir('/proc/1')
    with open('/proc/1/status', 'w') as f:
        f.write('Name:\tjail\nState:\tJailed\nPid:\t1\nPPid:\t0\n')

    # Test FreeBSD jail guest
    with open('/proc/self/status', 'w') as f:
        f.write('Name:\tjail\nState:\tJailed\nPid:\t1\nPPid:\t1\n')
    virtual = FreeBSDVirtual.detect()
    assert 'virtualization_role' in virtual

# Generated at 2022-06-13 03:50:52.223473
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    result = FreeBSDVirtualCollector()
    assert result

# Generated at 2022-06-13 03:51:01.985553
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    class Empty():
        ''' Empty Class '''
        def __init__(self):
            self.methods = []

    facts = Empty()
    facts.virtual_facts = {}
    facts.virtual_facts['virtualization_type'] = ''
    facts.virtual_facts['virtualization_role'] = ''
    virtual_facts = {}
    virtual_facts['virtualization_tech_guest'] = set()
    virtual_facts['virtualization_tech_host'] = set()
    FreeBSDVirtual._sysctl_detection_methods = []
    FreeBSDVirtual._virtual_vendor_detection_methods = []

    virtual = FreeBSDVirtualCollector(facts)
    virtual.get_virtual_facts()
    assert facts.virtual_facts['virtualization_type'] == ''
    assert facts.virtual_facts['virtualization_role'] == ''

# Generated at 2022-06-13 03:51:10.057493
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    kern_vm_guest = {
        'virtualization_tech_guest': set(['kvm', 'bhyve']),
        'virtualization_tech_host': set(['kvm', 'bhyve']),
        'virtualization_type': 'kvm',
        'virtualization_role': 'guest'
    }

    hw_hv_vendor = {
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set(),
        'virtualization_type': '',
        'virtualization_role': ''
    }


# Generated at 2022-06-13 03:51:17.643392
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    fixture = { 'ansible_facts': {
        'virtualization_type': '',
        'virtualization_role': '',
        'kernel': 'FreeBSD',
        'gather_subset': ['all']
    } }
    module = AnsibleModule(fixture)
    # Uses .detect_virt_product from VirtualSysctlDetectionMixin
    # Uses .detect_virt_vendor from VirtualSysctlDetectionMixin
    data = FreeBSDVirtual(module).get_virtual_facts()

    assert data['virtualization_type'] in ["", "tmpfs", "xen"]
    assert data['virtualization_role'] in ["", "guest"]
    assert isinstance(data['virtualization_tech_guest'], set)
    assert isinstance(data['virtualization_tech_host'], set)

# Generated at 2022-06-13 03:53:38.342089
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    """Test get_virtual_facts() of FreeBSDVirtual
    """
    virt = FreeBSDVirtual()

    # Case 1: VMware host
    set_module_args({'filter': 'hw.model'})
    with open(os.path.join(os.path.dirname(__file__), 'responses', 'sysctl_hw_model'), 'r') as f:
        out = f.read()
    facts = virt.get_virtual_facts(out)
    assert facts['virtualization_type'] == 'vmware'
    assert facts['virtualization_role'] == 'host'
    assert facts['virtualization_tech_host'] == set(['vmware'])
    assert facts['virtualization_tech_guest'] == set([])

    # Case 2: VMware guest

# Generated at 2022-06-13 03:53:42.960393
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    """
    Test FreeBSDVirtualCollector constructor
    """
    virt_facts = FreeBSDVirtualCollector()

    assert virt_facts.platform == 'FreeBSD'
    assert virt_facts.get_virtual_facts().__class__.__name__ == 'FreeBSDVirtual'