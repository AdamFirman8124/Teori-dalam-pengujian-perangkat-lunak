

# Generated at 2022-06-13 03:43:56.042123
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    facts = FreeBSDVirtual({}).get_virtual_facts()
    assert 'virtualization_type' in facts
    assert 'virtualization_role' in facts
    assert 'virtualization_tech_guest' in facts
    assert 'virtualization_tech_host' in facts

# Generated at 2022-06-13 03:43:59.810639
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual = FreeBSDVirtual()
    virtual_facts = virtual.get_virtual_facts()
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts

# Generated at 2022-06-13 03:44:06.108048
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    #: Set FreeBSDVirtual class to VirtualCollector._fact_class
    VirtualCollector._fact_class = FreeBSDVirtual

    #: Instance of FreeBSDVirtual class
    freebsd_virtual = FreeBSDVirtual()

    #: Test get_virtual_facts() when /proc/xen doesn't exist
    freebsd_virtual.sysctl.sysctl_exists = lambda key: False
    freebsd_virtual.sysctl.get_sysctl = lambda key: False
    freebsd_virtual.sysctl.get_sysctl_key = lambda key: ''
    virtual_facts = freebsd_virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''

    #: Test get_virtual_facts() when /proc/xen exists

# Generated at 2022-06-13 03:44:08.604625
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_collector = FreeBSDVirtualCollector()
    assert isinstance(virtual_collector, FreeBSDVirtualCollector)
    assert virtual_collector._platform == 'FreeBSD'
    assert isinstance(virtual_collector._fact_class, FreeBSDVirtual)

# Generated at 2022-06-13 03:44:11.225503
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    f = FreeBSDVirtualCollector()
    assert f.platform == 'FreeBSD'
    assert f._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:44:14.422705
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    test_obj = FreeBSDVirtualCollector()
    assert hasattr(test_obj, '_platform') and test_obj._platform == 'FreeBSD'
    assert hasattr(test_obj, '_fact_class') and test_obj._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:44:16.295532
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    bsd_virtual = FreeBSDVirtual({})
    virtual_facts = bsd_virtual.get_virtual_facts()
    assert virtual_facts['virtualization_tech_guest'] == set()
    assert virtual_facts['virtualization_tech_host'] == set()

# Generated at 2022-06-13 03:44:26.131292
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # Setup test data
    detect_virt_product_inputs = {
        'kern.vm_guest':  {'virtualization_type': 'hvm', 'virtualization_role': 'guest'},
        'hw.hv_vendor':   {'virtualization_type': 'kvm', 'virtualization_role': 'guest'},
        'security.jail.jailed': {'virtualization_type': 'jail', 'virtualization_role': ''}
    }

# Generated at 2022-06-13 03:44:34.614837
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # Test fact retrieval for Type: Bhyve, Guest: no, Host: no
    # hw.model = QEMU Virtual CPU version 2.5+
    model = 'QEMU Virtual CPU version 2.5+'
    virtual = FreeBSDVirtual()
    with open('/tmp/ansible.facts.d/virtual.fact', 'w') as fd:
        fd.write("""
        kern.vm_guest=none
        security.jail.jailed=0
        hw.hv_vendor=''
        """)
    virtual_facts = virtual._get_virtual_facts(model)
    assert virtual_facts['virtualization_type'] == 'qemu'
    assert virtual_facts['virtualization_role'] == ''

# Generated at 2022-06-13 03:44:39.843264
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # setup
    facts = {}
    # tests
    fact = FreeBSDVirtual({}, facts)
    virtual_facts = fact.get_virtual_facts()
    assert virtual_facts == {'virtualization_type': '', 'virtualization_role': '', 'virtualization_tech_guest': set(), 'virtualization_tech_host': set()}

# Generated at 2022-06-13 03:44:46.891733
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    facts = {}
    FreeBSDVirtualCollector(facts, None)
    assert 'virtualization_type' in facts
    assert 'virtualization_role' in facts
    assert 'virtualization_tech_guest' in facts
    assert 'virtualization_tech_host' in facts

# Generated at 2022-06-13 03:44:48.429629
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual = FreeBSDVirtualCollector()
    assert virtual._fact_class
    assert virtual._platform

# Generated at 2022-06-13 03:44:49.304475
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert FreeBSDVirtualCollector._platform == 'FreeBSD'

# Generated at 2022-06-13 03:44:55.884030
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # test virtual machine 'guest'
    virtual_facts = FreeBSDVirtual({}).get_virtual_facts()
    if os.path.exists('/dev/xen/xenstore'):
        assert virtual_facts['virtualization_type'] == 'xen'
        assert 'xen' in virtual_facts['virtualization_tech_guest']


# Generated at 2022-06-13 03:44:59.601405
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    facts = FreeBSDVirtualCollector()
    assert facts.get_all() == {}
    assert facts._platform == 'FreeBSD'
    assert facts._fact_class is FreeBSDVirtual

# Generated at 2022-06-13 03:45:01.768636
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    freebsdvirtual_collector = FreeBSDVirtualCollector()
    assert isinstance(freebsdvirtual_collector, VirtualCollector)

# Generated at 2022-06-13 03:45:06.392581
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.virtual.freebsd import FreeBSDVirtualCollector
    from ansible.module_utils.facts.virtual import VirtualCollector

    assert VirtualCollector == collector.get_platform_subclass(FreeBSDVirtualCollector)

# Generated at 2022-06-13 03:45:08.982643
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    facts_collector = FreeBSDVirtualCollector()
    assert(facts_collector._fact_class == FreeBSDVirtual)
    assert(facts_collector._platform == 'FreeBSD')


# Generated at 2022-06-13 03:45:14.408528
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual = FreeBSDVirtual()
    virtual_facts = virtual.get_virtual_facts()
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_product' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts
    assert isinstance(virtual_facts['virtualization_tech_guest'], set)
    assert isinstance(virtual_facts['virtualization_tech_host'], set)

# Generated at 2022-06-13 03:45:24.584268
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    import sys
    import types
    import pickle
    from ansible_collections.alliedtelesis.ats6200.tests.unit.compat import unittest
    from ansible_collections.alliedtelesis.ats6200.tests.unit.compat.mock import patch, Mock

    if sys.version_info[:2] == (2, 6):
        import__module = '__builtin__.__import__'
    else:
        import__module = 'builtins.__import__'


# Generated at 2022-06-13 03:45:36.738687
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual_facts = {'virtualization_type': '',
                     'virtualization_role': '',
                     'virtualization_tech_guest': set([]),
                     'virtualization_tech_host': set([])}
    try:
        from ansible.module_utils.facts.virtual.freebsd.Virtual import FreeBSDVirtual
        bsdVirt = FreeBSDVirtual(module=None)
    except ImportError:
        return

    # No detection
    # Case 1 : hw_hv_vendor:[''] kern_vm_guest:['', ''] security.jail.jailed:0
    #          hw.model:''
    assert virtual_facts == bsdVirt.get_virtual_facts()

    # Case 2 : hw_hv_vendor:['bhyve'] kern_vm_gu

# Generated at 2022-06-13 03:45:40.318285
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fc = FreeBSDVirtualCollector()
    assert(fc._platform == 'FreeBSD')
    assert(fc._fact_class == FreeBSDVirtual)

# Generated at 2022-06-13 03:45:50.296166
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.freebsd import FreeBSDVirtual
    from ansible.module_utils.facts.virtual.sysctl import VirtualSysctlDetectionMixin
    from ansible.module_utils._text import to_bytes
    # Create object test object
    obj = FreeBSDVirtual()
    # Read private variable virtualization_type of object FreeBSDVirtual
    virtualization_type = obj.virtualization_type
    # Read private variable virtualization_role of object FreeBSDVirtual
    virtualization_role = obj.virtualization_role
    # Create set of virtualization technology
    virtualizations_tech = set([to_bytes(u'kvm'), to_bytes(u'vmware'), to_bytes(u'virtualbox')])
    # Create set of host virtualization technology

# Generated at 2022-06-13 03:45:52.807817
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    obj = FreeBSDVirtualCollector()
    assert obj.platform == 'FreeBSD'
    assert issubclass(obj._fact_class, Virtual) is True
    assert obj._fact_class.platform == 'FreeBSD'

# Generated at 2022-06-13 03:45:53.312348
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:45:55.184334
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():

  # Test init
  collector = FreeBSDVirtualCollector()
  assert collector._platform == 'FreeBSD'
  assert collector._fact_class == FreeBSDVirtual
  assert collector.facts == {}


# Generated at 2022-06-13 03:46:01.286421
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    freebsd_virtual_facts = {"virtualization_role": "guest", "virtualization_type": "xen", "virtualization_tech_guest": set(["xen"]), "virtualization_tech_host": set()}
    freebsd_virtual = FreeBSDVirtual()
    assert freebsd_virtual.get_virtual_facts() == freebsd_virtual_facts

# Generated at 2022-06-13 03:46:04.402040
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    '''Unit test for method get_virtual_facts of class FreeBSDVirtual'''
    test_object = FreeBSDVirtual()

    assert test_object.get_virtual_facts() == {}

# Generated at 2022-06-13 03:46:08.023133
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    freebsd_virtual_collector = FreeBSDVirtualCollector()
    print(freebsd_virtual_collector._platform)
    assert freebsd_virtual_collector._platform == 'FreeBSD'

if __name__ == '__main__':
    test_FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:46:18.683511
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():

    sysctl_output = """
kern.vm_guest = 
hw.hv_vendor = None
security.jail.jailed = 
hw.model = Not applicable
    """
    expected_virtual_facts = {
        'virtualization_role': '',
        'virtualization_type': '',
        'virtualization_tech_host': {'vmware'},
        'virtualization_tech_guest': {'vmware', 'virtualbox', 'qemu', 'kvm', 'xen', 'hyperv'}
    }
    sysctl = FreeBSDVirtual(sysctl_output=sysctl_output)
    returned_virtual_facts = sysctl.get_virtual_facts()
    assert returned_virtual_facts == expected_virtual_facts



# Generated at 2022-06-13 03:46:34.135231
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # Init
    test_object = FreeBSDVirtual()

# Generated at 2022-06-13 03:46:44.784339
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    v = Virtual(None)

    d = {
        'kern.vm_guest': 'none',
        'hw.hv_vendor': 'bhyve',
        'security.jail.jailed': '0',
        'hw.model': 'Amazon EC2'
    }
    with v.Facts(d):
        assert isinstance(v.get_virtual_facts(), dict)
        assert v.get_virtual_facts()['virtualization_tech_host'] == set(['bhyve'])
        assert v.get_virtual_facts()['virtualization_tech_guest'] == set(['aws'])
        assert v.get_virtual_facts()['virtualization_role'] == 'guest'
        assert v.get_virtual_facts()['virtualization_type'] == 'aws'


# Generated at 2022-06-13 03:46:45.938042
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    facts = FreeBSDVirtualCollector()
    assert facts.collect() == facts.facts

# Generated at 2022-06-13 03:46:49.667146
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    _fact_class = FreeBSDVirtual()
    _virtual_facts = _fact_class.get_virtual_facts()
    assert isinstance(_virtual_facts, dict)

# Generated at 2022-06-13 03:46:52.389827
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual = FreeBSDVirtualCollector().collect()
    assert (virtual['virtualization_type'] == 'xen')
    assert (virtual['virtualization_role'] == 'guest')

# Generated at 2022-06-13 03:47:01.588347
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual import FreeBSDVirtual
    from os.path import exists

    fake_data = {
        'hw.hv_vendor': '',
        'kern.vm_guest': 'fake_vm_guest',
        'security.jail.jailed': '0'
    }
    facts_data = {
        'virtualization_type': '',
        'virtualization_role': ''
    }

    FreeBSD_get_virtual_facts = FreeBSDVirtual()
    FreeBSD_get_virtual_facts.get_virtual_facts(fake_data, facts_data)
    assert not exists('/dev/xen/xenstore')
    assert facts_data['virtualization_type'] == ''
    assert facts_data['virtualization_role'] == ''

# Generated at 2022-06-13 03:47:04.173872
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    vc = FreeBSDVirtualCollector()
    assert vc._platform == 'FreeBSD'
    assert isinstance(vc._fact_class(), FreeBSDVirtual)


# Generated at 2022-06-13 03:47:06.924627
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    facts_collector = FreeBSDVirtualCollector()
    assert all([hasattr(facts_collector, var) for var in [
        '_platform', '_fact_class', '_fact_class_inst'
    ]])

# Generated at 2022-06-13 03:47:11.378280
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual = FreeBSDVirtual()
    virtual_facts = virtual.get_virtual_facts()

    assert isinstance(virtual_facts, dict)
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts

# Generated at 2022-06-13 03:47:16.125571
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    facts = {
        'kernel': 'FreeBSD',
        'system': 'FreeBSD',
        'system_version': '10.2-RELEASE-p9',
    }

    f = FreeBSDVirtual(facts)
    f.get_virtual_facts()

    assert f.virtual_facts == {
        'virtualization_role': 'guest',
        'virtualization_type': 'xen',
        'virtualization_tech_guest': set(['xen']),
        'virtualization_tech_host': set(['xen']),
    }

# Generated at 2022-06-13 03:47:34.734077
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    facts = FreeBSDVirtual(None, None, 'freebsd', '11.0-RELEASE-p5').get_virtual_facts()
    assert facts['virtualization_type'] != '', "FreeBSDVirtual.get_virtual_facts()"
    assert facts['virtualization_role'] != '', "FreeBSDVirtual.get_virtual_facts()"

# Generated at 2022-06-13 03:47:35.985395
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    obj = FreeBSDVirtualCollector()
    assert obj._fact_class == FreeBSDVirtual
    assert obj._platform == 'FreeBSD'

# Generated at 2022-06-13 03:47:39.093355
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virt = FreeBSDVirtual()
    facts = virt.get_all_facts()
    assert 'virtualization_type' in facts
    assert 'virtualization_role' in facts
    assert 'virtualization_tech_host' in facts
    assert 'virtualization_tech_guest' in facts

# Generated at 2022-06-13 03:47:40.385296
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    # FreeBSDVirtualCollector instantiated correctly
    assert isinstance(FreeBSDVirtualCollector(), VirtualCollector)

# Generated at 2022-06-13 03:47:43.639111
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    facts_dict = dict()
    # create FreeBSDVirtual instance with empty facts dict
    freebsd_virtual = FreeBSDVirtuao()
    freebsd_virtual_facts = freebsd_virtual.get_virtual_facts()
    assert freebsd_virtual_facts['virtualization_type'] == 'xen'
    assert freebsd_virtual_facts['virtualization_role'] == 'guest'

# Generated at 2022-06-13 03:47:46.379182
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_collector = FreeBSDVirtualCollector()
    assert virtual_collector  # ensure non-empty object


# Generated at 2022-06-13 03:47:54.638392
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    """
    Returns the expected output from get_virtual_facts
    """
    # Set up class instance for testing
    virtual = FreeBSDVirtual()

    # Define the output from this method that we expect
    expected_virtual_facts = {'virtualization_type': 'xen',
                              'virtualization_role': 'guest',
                              'virtualization_tech_host': set(),
                              'virtualization_tech_guest': {'xen'}}

    # Capture the results of the method under test
    virtual_facts = virtual.get_virtual_facts()

    # Compare the results against the expected values
    assert virtual_facts == expected_virtual_facts

# Generated at 2022-06-13 03:48:02.315990
# Unit test for method get_virtual_facts of class FreeBSDVirtual

# Generated at 2022-06-13 03:48:13.757149
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    f_virtual = FreeBSDVirtual(None)
    f_virtual.gather_device_facts = lambda self: {'device_links': {}}
    f_virtual.gather_kernel_facts = lambda self: {'kernel': 'FreeBSD'}

    expected = {
        'virtualization_type': '',
        'virtualization_role': '',
    }

    # AnsibleModule
    # (self, argument_spec=None, bypass_checks=None, no_log=False,
    #  check_invalid_arguments=None, mutually_exclusive=None, required_together=None,
    #  required_one_of=None, add_file_common_args=None, supports_check_mode=False,
    #  required_if=None, required_by=None)

# Generated at 2022-06-13 03:48:15.414421
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    bsd = FreeBSDVirtualCollector()
    assert bsd.platform == 'FreeBSD'
    assert bsd._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:49:15.973082
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():

    # Given a set of simple facts
    given_sysctl = dict(virtualization_tech_host=set(), virtualization_tech_guest=set())
    given_hw_model = dict(virtualization_tech_host=set(), virtualization_tech_guest=set())

    # And a FreeBSDVirtual object
    fbsd_virtual = FreeBSDVirtual(dict(), given_sysctl, given_hw_model)

    # When we get virtual facts
    facts = fbsd_virtual.get_virtual_facts()

    # Then we should get the expected facts
    assert facts == dict(
            virtualization_type='',
            virtualization_role='',
            virtualization_tech_host=set(),
            virtualization_tech_guest=set(),
    )


# Generated at 2022-06-13 03:49:18.841292
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert FreeBSDVirtualCollector._platform == "FreeBSD"
    assert FreeBSDVirtualCollector._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:49:21.005095
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    f = FreeBSDVirtualCollector()
    assert f.platform == 'FreeBSD'
    assert f._fact_class.platform == 'FreeBSD'

# Generated at 2022-06-13 03:49:29.405812
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    '''Test get_virtual_facts method of FreeBSDVirtual with different sysctl values'''
    import os
    import sys
    import unittest
    from unittest.mock import MagicMock, patch
    import json
    import platform

    # unittest_utils will handle putting a fake sysctl command in the PATH
    fixture_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'sysctl')
    ansible_module = MagicMock()
    ansible_module.get_bin_path.return_value = '/fakebin/sysctl'
    ansible_module.params = {}
    setattr(ansible_module, '_ansible_sysctl_fixtures', json.load(open(os.path.join(fixture_path, 'sysctl.json'))))

   

# Generated at 2022-06-13 03:49:30.209260
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_collector = FreeBSDVirtualCollector()
    assert virtual_collector is not None

# Generated at 2022-06-13 03:49:31.656971
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert issubclass(FreeBSDVirtualCollector, VirtualCollector)
    assert FreeBSDVirtualCollector._platform == 'FreeBSD'
    assert FreeBSDVirtualCollector._fact_class == FreeBSDVirtual


# Generated at 2022-06-13 03:49:32.559895
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fvc = FreeBSDVirtualCollector()
    assert isinstance(fvc, VirtualCollector)

# Generated at 2022-06-13 03:49:35.665963
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    obj = FreeBSDVirtualCollector()
    assert hasattr(obj, '_fact_class')
    assert obj._fact_class == FreeBSDVirtual
    assert hasattr(obj, '_platform')
    assert obj._platform == 'FreeBSD'

# Generated at 2022-06-13 03:49:37.914486
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    bfc = FreeBSDVirtualCollector()
    assert isinstance(bfc, FreeBSDVirtualCollector)
    assert isinstance(bfc._fact_class, FreeBSDVirtual)
    assert bfc._platform == 'FreeBSD'

# Generated at 2022-06-13 03:49:39.471416
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    F = FreeBSDVirtualCollector()
    assert F.platform == 'FreeBSD'
    assert F._fact_class == FreeBSDVirtual


# Generated at 2022-06-13 03:50:48.605964
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    vc = FreeBSDVirtualCollector()
    assert vc.platform == 'FreeBSD'
    assert vc._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:50:58.370861
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.sysctl import VirtualSysctlDetectionMixin
    from ansible.module_utils.facts.virtual.sysctl import load_sysctl_facts

    # Given sysctl facts
    sysctl_facts = load_sysctl_facts()

    # Given a FreeBSDVirtual instance
    freebsdvirtual = FreeBSDVirtual(sysctl_facts)

    # When get_virtual_facts is called
    freebsdvirtual_facts = freebsdvirtual.get_virtual_facts()

    # Then virtualization_type is 'xen'
    assert freebsdvirtual_facts['virtualization_type'] == 'xen'

    # And virtualization_role is 'guest'
    assert freebsdvirtual_facts['virtualization_role'] == 'guest'

    # And virtualization_type is 'vmware

# Generated at 2022-06-13 03:51:00.822261
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    # Get instance of class FreeBSDVirtualCollector
    instance = FreeBSDVirtualCollector()

    # Checks if instance is an instance of class FreeBSDVirtualCollector
    assert isinstance(instance, FreeBSDVirtualCollector)



# Generated at 2022-06-13 03:51:02.974198
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    '''
    Unit test for the constructor of class FreeBSDVirtualCollector
    '''
    assert FreeBSDVirtualCollector

# Generated at 2022-06-13 03:51:03.971911
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    obj = FreeBSDVirtualCollector()
    assert obj._platform == 'FreeBSD'

# Generated at 2022-06-13 03:51:05.416097
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    collector = FreeBSDVirtualCollector()
    assert collector.platform == 'FreeBSD'
    assert collector._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:51:07.817906
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual_facts = FreeBSDVirtual({}).get_virtual_facts()
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts



# Generated at 2022-06-13 03:51:09.108738
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fb = FreeBSDVirtualCollector()
    assert isinstance(fb._fact_class, type)

# Generated at 2022-06-13 03:51:14.353622
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # Constructor
    fbsd_virtual = FreeBSDVirtual()

    # Test cases
    # hw.model = 'VirtualBox'
    virtual_facts = fbsd_virtual.get_virtual_facts(
        hw_model="VirtualBox",
        kern_vm_guest="none",
        hw_hv_vendor="none"
    )
    assert virtual_facts['virtualization_type'] == 'virtualbox'
    assert virtual_facts['virtualization_role'] == 'guest'

    # Check for the vm detection
    # kern.vm_guest = 'vmware'

# Generated at 2022-06-13 03:51:19.535239
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.freebsd import VirtualFacts
    virtual_facts = VirtualFacts(dict(), dict())
    freebsd_virtual = FreeBSDVirtual(virtual_facts)

    virtual_facts.sysctl['kern.vm_guest'] = 'vmware'
    virtual_facts.sysctl['hw.hv_vendor'] = 'bhyve'
    virtual_facts.sysctl['security.jail.jailed'] = '0'

    expected = {
        'virtualization_type': 'vmware',
        'virtualization_role': 'guest',
        'virtualization_tech_guest': set(['vmware']),
        'virtualization_tech_host': set(['bhyve']),
    }
    actual = freebsd_virtual.get_virtual_facts()

# Generated at 2022-06-13 03:53:35.824910
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    f = FreeBSDVirtual({})
    assert f.get_virtual_facts() == {'virtualization_type': '', 'virtualization_role': '', 'virtualization_tech_host': set(['FreeBSD']), 'virtualization_tech_guest': set([])}

# Generated at 2022-06-13 03:53:36.714740
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert isinstance(FreeBSDVirtualCollector(), VirtualCollector)

# Generated at 2022-06-13 03:53:38.601822
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    collector = FreeBSDVirtualCollector()

    assert collector.platform == 'FreeBSD'
    assert collector._fact_class == FreeBSDVirtual
    assert collector._virtuals == {}

# Generated at 2022-06-13 03:53:40.747342
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    assert isinstance(FreeBSDVirtual().get_virtual_facts(), dict)

# Generated at 2022-06-13 03:53:48.833180
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():

    # Attributes for FreeBSDVirtual
    # Set empty values as default
    params = dict(
        virtualization_type='',
        virtualization_role='',
        virtualization_tech_host=set(),
        virtualization_tech_guest=set(),
    )

    # Create FreeBSDVirtual object
    virtual = FreeBSDVirtual(params)

    # Store the results of get_virtual_facts
    virtual_facts = virtual._get_virtual_facts()

    # Check that the results are correct
    assert virtual_facts['virtualization_role'] == ''
    assert virtual_facts['virtualization_type'] == ''
    assert not virtual_facts['virtualization_tech_host']
    assert not virtual_facts['virtualization_tech_guest']