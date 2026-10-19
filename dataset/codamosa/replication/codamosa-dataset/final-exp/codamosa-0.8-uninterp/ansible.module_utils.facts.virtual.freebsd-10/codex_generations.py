

# Generated at 2022-06-13 03:43:54.831850
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    from ansible.module_utils.facts import virtual
    f = virtual.FreeBSDVirtualCollector()
    assert f._fact_class == FreeBSDVirtual
    assert f._platform == 'FreeBSD'

# Generated at 2022-06-13 03:43:58.995202
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    freebsd_virtual = FreeBSDVirtualCollector()
    assert FreeBSDVirtualCollector._platform == 'FreeBSD'
    assert str(freebsd_virtual._fact_class(None, None)) == "<ansible.module_utils.facts.virtual.freebsd.FreeBSDVirtual(None, None)>"

# Generated at 2022-06-13 03:44:05.355195
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    import json
    from ansible.module_utils.facts import collector

    collector.load_collection_file('virtual', 'FreeBSD')
    facts = collector.collect(['virtual'], '', 'FreeBSD', '', '')

    # The following assertion must be true if the method get_virtual_facts is
    # implemented correctly.
    assert 'virtual' in facts
    assert facts['virtual'] == {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_tech_guest': {'freebsd'},
        'virtualization_tech_host': set()
    }

    # If you have added additional sysctl checks, please make sure to add
    # corresponding unit tests below.
    #
    # Additionally, make sure to check if the unit tests for the method
    # detect_virt_

# Generated at 2022-06-13 03:44:09.803627
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    # Call constructor
    fvc = FreeBSDVirtualCollector()
    assert fvc is not None
    assert fvc._platform == 'FreeBSD'
    assert issubclass(fvc._fact_class, FreeBSDVirtual)

# Generated at 2022-06-13 03:44:10.769116
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert FreeBSDVirtualCollector().platform == 'FreeBSD'

# Generated at 2022-06-13 03:44:20.562402
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # Test data
    kern_vm_guest_jail_host = {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_tech_guest': {'jail'},
        'virtualization_tech_host': {},
        'virtualization_vendor': '',
        'virtualization_product': '',
    }
    kern_vm_guest_jail_guest = {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_tech_guest': {'jail'},
        'virtualization_tech_host': {},
        'virtualization_vendor': '',
        'virtualization_product': '',
    }

# Generated at 2022-06-13 03:44:22.331839
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fvc = FreeBSDVirtualCollector()
    assert fvc._platform == 'FreeBSD'
    assert fvc._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:44:27.626902
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    bsdv = FreeBSDVirtual()
    facts = bsdv.get_virtual_facts()

    assert facts['virtualization_type'] == ''
    assert facts['virtualization_role'] == ''
    assert 'vbox' in facts['virtualization_tech_guest']
    assert 'vbox' in facts['virtualization_tech_host']



# Generated at 2022-06-13 03:44:29.803998
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fvc = FreeBSDVirtualCollector()
    assert fvc._platform == 'FreeBSD'
    assert fvc._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:44:31.690116
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_facts = FreeBSDVirtualCollector()

    assert virtual_facts._fact_class == FreeBSDVirtual
    assert virtual_facts._platform == 'FreeBSD'

# Generated at 2022-06-13 03:44:41.685344
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    vd = VirtualCollector("FreeBSD")
    assert isinstance(vd,VirtualCollector)


# Generated at 2022-06-13 03:44:49.375528
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # Set up the objects we need
    module = type('module', (object, ), {})
    module.params = {}
    module.exit_json = exit_json
    module.warn = warn
    module.fail_json = fail_json
    module.exit_json.called = False
    module.warn.called = False
    module.fail_json.called = False
    setattr(module, 'check_mode', False)
    virtual = FreeBSDVirtual(module)

    # Run the method under test
    virtual_facts = virtual.get_virtual_facts()

    # Assert the results
    assert(virtual_facts['virtualization_type'] == '')
    assert(virtual_facts['virtualization_role'] == '')
    assert(len(virtual_facts['virtualization_tech_host']) == 0)

# Generated at 2022-06-13 03:44:59.437656
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # Preparing tests
    # Windows XP host
    uname_output='FreeBSD 9.1-RELEASE-p3 FreeBSD 9.1-RELEASE-p3 #0: Wed Mar 21 02:30:07 UTC 2012     root@amd64-builder.daemonology.net:/usr/obj/usr/src/sys/GENERIC  amd64'

# Generated at 2022-06-13 03:45:07.133223
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # Create an instance of FreeBSDVirtual class
    fvd = FreeBSDVirtual(None)

    # Create expected virtual_facts dictionary
    expected_dict = {
        "virtualization_type": "",
        "virtualization_role": "",
        "virtualization_tech_guest": set(),
        "virtualization_tech_host": set()
    }

    # Get virtual_facts dictionary from the function get_virtual_facts
    virtual_facts = fvd.get_virtual_facts()

    # Assert virtual_facts dictionary is what we expect
    assert virtual_facts == expected_dict

# Generated at 2022-06-13 03:45:08.982256
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    bf = FreeBSDVirtualCollector()
    assert bf.platform == 'FreeBSD'
    assert bf._fact_class == FreeBSDVirtual


# Generated at 2022-06-13 03:45:16.821064
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # Load stubbed module_utils and class under test
    from ansible.module_utils.facts.virtual.freebsd import FreeBSDVirtual

    # Instatiate class under test
    module_under_test = FreeBSDVirtual()

    # Test some values
    assert module_under_test.get_virtual_facts() == {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set()
    }

# Generated at 2022-06-13 03:45:22.559176
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual_facts = FreeBSDVirtual()
    virtual_facts = virtual_facts.get_virtual_facts()

    assert type(virtual_facts['virtualization_tech_guest']) is set
    assert type(virtual_facts['virtualization_tech_host']) is set
    assert 'hw_vendor' in virtual_facts['virtualization_tech_host']
    assert 'virtualization_vendor' in virtual_facts['virtualization_tech_host']

# Generated at 2022-06-13 03:45:26.802427
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    v_obj = FreeBSDVirtual()
    facts = v_obj.get_virtual_facts()
    assert facts['virtualization_type'] == 'xen'
    assert facts['virtualization_role'] == 'guest'
    assert facts['virtualization_tech_host'] == set(['xen'])
    assert facts['virtualization_tech_guest'] == set(['xen'])

# Generated at 2022-06-13 03:45:35.283507
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    from ansible_collections.community.general.tests.unit.compat.mock import MagicMock

    fbsd_virtual_facts_dict = {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_tech_guest': {'jail'},
        'virtualization_tech_host': set()
    }

    fbsd_kern_vm_guest_dict = {
        'hw.hv_vendor': '',
        'kern.vm_guest': 'other',
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_tech_guest': {'other'},
        'virtualization_tech_host': set()
    }

    # Virtualization is not supported for this platform
    mock

# Generated at 2022-06-13 03:45:39.471478
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    from ansible.module_utils.facts.virtual.freebsd import FreeBSDVirtualCollector
    assert FreeBSDVirtualCollector._platform == 'FreeBSD'
    assert FreeBSDVirtualCollector._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:45:50.339079
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    f = FreeBSDVirtualCollector()
    assert f is not None

# Generated at 2022-06-13 03:45:52.166569
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_collection = FreeBSDVirtualCollector()
    assert virtual_collection._platform == 'FreeBSD'
    assert virtual_collection._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:45:55.285047
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    f = FreeBSDVirtual({})
    facts = f.get_virtual_facts()
    assert facts['virtualization_type'] == ''
    assert facts['virtualization_role'] == ''
    assert facts['virtualization_tech_guest'] == set()
    assert facts['virtualization_tech_host'] == set()

# Generated at 2022-06-13 03:45:57.906803
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    f = FreeBSDVirtualCollector()
    assert isinstance(f._fact_class(), FreeBSDVirtual)
    assert f._platform == 'FreeBSD'

# Generated at 2022-06-13 03:46:00.490185
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    result = {'virtualization_type': '',
              'virtualization_role': ''}
    FreeBSDVirtualCollector(None, result)

# Generated at 2022-06-13 03:46:06.321805
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual = FreeBSDVirtual()
    virtual_facts = virtual.get_virtual_facts()
    # If we're not running FreeBSD then skip the test
    if virtual_facts['virtualization_type'] != "":
        return
    assert virtual_facts['virtualization_type'] == ""
    assert virtual_facts['virtualization_role'] == ""
    assert virtual_facts['virtualization_technology'] == ""

# Generated at 2022-06-13 03:46:07.577963
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    x = FreeBSDVirtualCollector()
    assert x.platform == 'FreeBSD'

# Generated at 2022-06-13 03:46:16.979861
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    # Instantiate a FreeBSDVirtualCollector object
    freebsd_virtual_collector = FreeBSDVirtualCollector()
    assert freebsd_virtual_collector
    assert isinstance(freebsd_virtual_collector, FreeBSDVirtualCollector)
    # There should be 3 keys in the dictionary
    assert 3 == len(freebsd_virtual_collector.collect_candidate_names())
    # All keys in candidate_names should start with 'virtualization_'
    for key in freebsd_virtual_collector.collect_candidate_names():
        assert key.startswith('virtualization_')
    assert freebsd_virtual_collector.platform == 'FreeBSD'

# Generated at 2022-06-13 03:46:21.411185
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virt_facts = FreeBSDVirtual()

    assert virt_facts.get_virtual_facts() == {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set()
    }


# Generated at 2022-06-13 03:46:24.068070
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual = FreeBSDVirtual()
    virtual_facts = virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''

# Generated at 2022-06-13 03:46:49.564897
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert FreeBSDVirtualCollector.platform == 'FreeBSD'
    assert FreeBSDVirtualCollector.facts_class == FreeBSDVirtual

# Generated at 2022-06-13 03:46:51.933330
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fvc = FreeBSDVirtualCollector()
    assert fvc.platform == 'FreeBSD'
    assert fvc._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:46:53.601043
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert FreeBSDVirtualCollector()._platform == 'FreeBSD'
    assert FreeBSDVirtualCollector()._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:46:58.532785
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    fv = FreeBSDVirtual()
    virtual_facts = fv.get_virtual_facts()
    virtual_facts_correct = {
        'virtualization_type': 'xen',
        'virtualization_role': 'guest',
        'virtualization_tech_guest': {'xen'},
        'virtualization_tech_host': set(),
    }
    assert virtual_facts == virtual_facts_correct

# Generated at 2022-06-13 03:47:02.930685
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    facts = {'kernel': 'FreeBSD', 'kernel_version': '11.0-RELEASE'}
    f = FreeBSDVirtual(module=None, facts=facts)
    result = f.get_virtual_facts()
    assert 'virtualization_type' in result
    assert 'virtualization_role' in result
    assert 'virtualization_tech_guest' in result
    assert 'virtualization_tech_host' in result

# Generated at 2022-06-13 03:47:07.261714
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    v = FreeBSDVirtual()
    # Run the code
    expected = {'virtualization_tech_guest': set(['xen']), 'virtualization_type': 'xen',
                'virtualization_role': 'guest', 'virtualization_tech_host': set()}
    actual = v.get_virtual_facts()
    assert actual == expected



# Generated at 2022-06-13 03:47:09.237718
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    instance = FreeBSDVirtualCollector()
    assert isinstance(instance, FreeBSDVirtualCollector)
    assert isinstance(instance.collect(), dict)

# Generated at 2022-06-13 03:47:16.525778
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual_vendor_facts = dict()
    virtual_vendor_facts['virtualization_type'] = 'VMWare'

    sysctl_facts = dict()
    sysctl_facts['virtualization_type'] = 'VMWare'

    def mock_detect_virt_product(sysctl_key):
        if sysctl_key == 'kern.vm_guest':
            return sysctl_facts
        return sysctl_facts

    def mock_detect_virt_vendor(hw_key):
        if hw_key == 'hw.model':
            return virtual_vendor_facts
        return virtual_vendor_facts

    facts = FreeBSDVirtual()
    facts.detect_virt_product = mock_detect_virt_product
    facts.detect_virt_vendor = mock_detect_virt_v

# Generated at 2022-06-13 03:47:19.975903
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    """This test case will verify that constructor of
    FreeBSDVirtualCollector works as expected"""
    fb_virtual = FreeBSDVirtualCollector()
    assert isinstance(fb_virtual, VirtualCollector)
    assert fb_virtual.platform == 'FreeBSD'
    assert fb_virtual._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:47:22.622293
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    module_name = 'ansible.module_utils.facts.virtual.freebsd'
    virtual_collector = FreeBSDVirtualCollector(module_name)
    assert virtual_collector._fact_class == FreeBSDVirtual
    assert virtual_collector._platform == 'FreeBSD'

# Generated at 2022-06-13 03:48:20.220970
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    '''
    Tests functionality of get_virtual_facts method of FreeBSDVirtual class
    '''
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts.virtual import VirtualCollector
    from ansible.module_utils.facts.virtual.freebsd import FreeBSDVirtual
    from ansible.module_utils.facts.virtual.freebsd import FreeBSDVirtualCollector
    from ansible.module_utils.facts.virtual.sysctl import VirtualSysctlDetectionMixin
    import os

    os.path.exists = lambda path: False
    ansible_collector.pop(FreeBSDVirtualCollector, None)
    fact = FreeBSDVirtual()
    facts = fact.get_virtual_facts()

# Generated at 2022-06-13 03:48:20.617266
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:48:21.864940
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_collector = FreeBSDVirtualCollector()
    assert isinstance(virtual_collector, FreeBSDVirtualCollector)

# Generated at 2022-06-13 03:48:22.307364
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:48:25.546225
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fbvc = FreeBSDVirtualCollector()
    assert isinstance(fbvc, VirtualCollector)
    assert isinstance(fbvc._fact_class, FreeBSDVirtual)
    assert fbvc._fact_class.platform == 'FreeBSD'

# Generated at 2022-06-13 03:48:26.411948
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:48:30.584469
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual_facts = FreeBSDVirtual({}).get_virtual_facts()
    assert virtual_facts['virtualization_type'] in ('', 'xen')
    assert virtual_facts['virtualization_role'] in ('', 'guest')
    assert virtual_facts['virtualization_technology'] in ('', 'HVM')

# Generated at 2022-06-13 03:48:39.561943
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    from ansible.module_utils import basic

    class ModuleStub:
        def __init__(self, params):
            self.params = params
            self.exit_json_called = False

        def exit_json(self, **kwargs):
            self.exit_json_called = True
            self.exit_json_dict = kwargs

    class ModuleExitException(Exception):
        pass

    class ArgumentSpecStub:
        def __init__(self):
            self.argument_spec = {}

    class AnsibleModuleStub:
        def __init__(self, argument_spec, **kwargs):
            self.params = {}
            self.exit_json = basic.AnsibleModule.exit_json
            self.fail_json = basic.AnsibleModule.fail_json


# Generated at 2022-06-13 03:48:42.375773
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert FreeBSDVirtualCollector.__name__ == "FreeBSDVirtualCollector"
    assert FreeBSDVirtualCollector._platform == 'FreeBSD'
    assert FreeBSDVirtualCollector._fact_class == FreeBSDVirtual


# Generated at 2022-06-13 03:48:45.262589
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    freebsd_virtual_collector = FreeBSDVirtualCollector()
    assert freebsd_virtual_collector._platform == 'FreeBSD'
    assert freebsd_virtual_collector._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:49:51.114172
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    # Test the constructor of the class FreeBSDVirtualCollector
    # There is no constructor
    assert True

# Generated at 2022-06-13 03:49:53.242762
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    facts = FreeBSDVirtualCollector().collect()
    assert facts['ansible_virtualization_type'] == 'xen'
    assert facts['ansible_virtualization_role'] == 'guest'

# Generated at 2022-06-13 03:49:54.871028
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_collector = FreeBSDVirtualCollector()
    assert virtual_collector.platform == 'FreeBSD'

# Generated at 2022-06-13 03:49:56.259470
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    facts_module = FreeBSDVirtualCollector(None, None)
    assert facts_module is not None

# Generated at 2022-06-13 03:49:57.583817
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    obj = FreeBSDVirtualCollector()
    assert obj._platform == 'FreeBSD'
    assert obj.platform == 'FreeBSD'

# Generated at 2022-06-13 03:50:04.374740
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # dummy data of sysctl from FreeBSD
    kern_vm_guest = 'none'
    hw_model = 'VirtualBox'
    security_jail_jailed = 0
    hw_hv_vendor = ''

    virtual = FreeBSDVirtual()

    # test for Virtualization role as host
    virtual_facts = virtual.get_virtual_facts()

    # test for FreeBSD virtualization type as none
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''
    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts

# Generated at 2022-06-13 03:50:06.448181
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_collector = FreeBSDVirtualCollector()
    assert virtual_collector._platform == 'FreeBSD'
    assert virtual_collector._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:50:09.794920
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    potential_new_fact = FreeBSDVirtualCollector()
    assert potential_new_fact._platform == 'FreeBSD'
    assert potential_new_fact._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:50:11.745691
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    f = FreeBSDVirtualCollector()
    assert f


# Generated at 2022-06-13 03:50:19.768892
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    v = FreeBSDVirtual("")
    v.sysctl_product_data = {}

    # Test empty facts
    assert v.get_virtual_facts().items() <= dict(
        virtualization_type='',
        virtualization_role='',
        virtualization_tech_host=set(),
        virtualization_tech_guest=set()
    ).items()

    # Test virtualization_role == 'guest'
    v.sysctl_product_data = {'kern.vm_guest': 'freebsd', 'hw.hv_vendor': 'freebsd'}

# Generated at 2022-06-13 03:51:37.050828
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # FreeBSDHost
    host = FreeBSDVirtual(module=None)

    # Check the virtual facts of a FreeBSDVirtual
    assert host.get_virtual_facts() == {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set(),
    }

# Generated at 2022-06-13 03:51:45.796548
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    freebsd_virtual = FreeBSDVirtual()
    freebsd_virtual.read_pipe = mock_read_pipe
    freebsd_virtual.read_file = mock_read_file
    freebsd_virtual.get_sysctl_value = mock_get_sysctl_value
    freebsd_virtual.get_dmesg_value = mock_get_dmesg_value

    expected = {
        'virtualization_type': 'xen',
        'virtualization_role': 'guest',
        'virtualization_tech_guest': ['xen'],
        'virtualization_tech_host': ['xen'],
    }
    result = freebsd_virtual.get_virtual_facts()
    assert expected == result


# Generated at 2022-06-13 03:51:47.599743
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert(FreeBSDVirtualCollector._fact_class == FreeBSDVirtual)
    assert(FreeBSDVirtualCollector._platform == 'FreeBSD')

# Generated at 2022-06-13 03:51:50.329117
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    """
    Test the constructor of the FreeBSDVirtualCollector class.
    """
    freebsd_virtual = FreeBSDVirtualCollector()
    assert freebsd_virtual._fact_class == FreeBSDVirtual
    assert freebsd_virtual._platform == 'FreeBSD'

# Generated at 2022-06-13 03:51:52.345865
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    c = FreeBSDVirtualCollector()
    assert c.platform == 'FreeBSD'
    assert c._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:51:54.342096
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fvc = FreeBSDVirtualCollector()
    assert fvc.platform == 'FreeBSD'
    assert fvc.fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:51:57.912460
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    # Test instantiation of object for FreeBSDPlatform
    fvc = FreeBSDVirtualCollector()
    assert fvc != None
    assert isinstance(fvc, FreeBSDVirtualCollector)
    assert fvc._platform == "FreeBSD"
    assert fvc._fact_class.platform == "FreeBSD"



# Generated at 2022-06-13 03:51:59.008436
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert issubclass(FreeBSDVirtualCollector, VirtualCollector)

# Generated at 2022-06-13 03:52:01.830440
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert issubclass(FreeBSDVirtualCollector, VirtualCollector)
    assert FreeBSDVirtualCollector._platform == 'FreeBSD'
    assert FreeBSDVirtualCollector._fact_class == FreeBSDVirtual

    # Check that object is of right type
    assert isinstance(FreeBSDVirtualCollector(), VirtualCollector)


# Generated at 2022-06-13 03:52:11.163050
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    fb_virtual = FreeBSDVirtual({})
    fb_virtual.detect_virt_product = lambda x: dict(virtualization_tech_guest=set(['kvm']), virtualization_tech_host=set(['kvm']))
    fb_virtual.detect_virt_vendor = lambda x: dict(virtualization_tech_guest=set(['virtualbox']), virtualization_tech_host=set(['virtualbox']))
    fb_virtual.get_virtual_facts() == {'virtualization_tech_guest': set(['kvm', 'virtualbox']), 'virtualization_tech_host': set(['kvm', 'virtualbox']), 'virtualization_type': 'kvm', 'virtualization_role': 'guest'}

