

# Generated at 2022-06-13 03:44:00.889822
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    from ansible_collections.ansible.community.tests.unit.module_utils.facts.virtual.test_virtfact_collector import MockMemInfo
    from ansible_collections.ansible.community.tests.unit.module_utils.facts.virtual.test_virtfact_collector import MockCPUInfo

    meminfo = MockMemInfo()
    cpuinfo = MockCPUInfo()

    facts = FreeBSDVirtual(meminfo, cpuinfo).get_virtual_facts()

    assert facts['virtualization_type'] == 'xen'
    assert facts['virtualization_role'] == 'guest'
    assert sorted(facts['virtualization_tech_guest']) == ['xen']
    assert sorted(facts['virtualization_tech_host']) == []


# Generated at 2022-06-13 03:44:03.740391
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    f = FreeBSDVirtualCollector()
    assert f is not None
    assert f._platform == 'FreeBSD'
    assert f._fact_class == FreeBSDVirtual


# Generated at 2022-06-13 03:44:08.128183
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    """
    Test get_virtual_facts with a FreeBSD host.
    """
    test_obj = FreeBSDVirtual({})
    assert test_obj.get_virtual_facts() == {
        'virtualization_role': 'guest',
        'virtualization_type': 'xen',
        'virtualization_tech_guest': {'xen'},
        'virtualization_tech_host': set(),
    }

# Generated at 2022-06-13 03:44:15.226571
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    expected_result = {
        'virtualization_type': 'oracle',
        'virtualization_role': 'guest'
    }
    facts_module = FreeBSDVirtual('/')
    if 'oracle' in facts_module.platform_subclass['virtualization_type']:
        assert expected_result == facts_module.platform_subclass['virtualization_type']
    else:
        assert 'None' in facts_module.platform_subclass['virtualization_type']



# Generated at 2022-06-13 03:44:21.283758
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    if not FreeBSDVirtualCollector().platform:
        raise AssertionError("VirtualCollector() was not initialized properly. Missing "
                             "platform attribute.")
    if not FreeBSDVirtualCollector()._fact_class:
        raise AssertionError("VirtualCollector() was not initialized properly. Missing "
                             "_fact_class attribute.")
    if not FreeBSDVirtualCollector()._platform:
        raise AssertionError("VirtualCollector() was not initialized properly. Missing "
                             "_platform attribute.")

# Generated at 2022-06-13 03:44:22.330086
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    collector = FreeBSDVirtualCollector(None, None)



# Generated at 2022-06-13 03:44:29.478024
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():

    # Initialize
    freebsd_virtual = FreeBSDVirtual(module=None)

    # Construct test data
    # Example of os.uname()
    # ('FreeBSD',
    #  'justansible.local',
    #  '12.0-CURRENT',
    #  'FreeBSD 12.0-CURRENT #0 r334048: Thu Jun 22 08:34:05 UTC 2017',
    #  'amd64',
    #  'amd64')
    test_uname_result = (
        'FreeBSD',
        'justansible.local',
        '12.0-CURRENT',
        'FreeBSD 12.0-CURRENT #0 r334048: Thu Jun 22 08:34:05 UTC 2017',
        'amd64',
        'amd64')

# Generated at 2022-06-13 03:44:32.099995
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual = FreeBSDVirtual()
    facts = virtual.get_virtual_facts()
    assert facts['virtualization_type'] == 'xen'
    assert facts['virtualization_role'] == 'guest'

# Generated at 2022-06-13 03:44:33.824394
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    c = FreeBSDVirtualCollector()
    assert(c.collect()['virtual']['platform'] == 'FreeBSD')

# Generated at 2022-06-13 03:44:41.119342
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    """Unit test for method get_virtual_facts of class FreeBSDVirtual"""

    # Create a FreeBSDVirtual instance
    virt = FreeBSDVirtual()
    # Call method get_virtual_facts of the instance
    result = virt.get_virtual_facts()
    # Assert variables virtualization_type and virtualization_role
    # have expected values
    assert 'virtualization_type' in result
    assert 'virtualization_role' in result
    assert result['virtualization_type'] == ''
    assert result['virtualization_role'] == ''

# Generated at 2022-06-13 03:44:47.464858
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    freebsd_virtual_collector = FreeBSDVirtualCollector()
    assert freebsd_virtual_collector.platform == 'FreeBSD'
    assert freebsd_virtual_collector.fact_class._platform == 'FreeBSD'

# Generated at 2022-06-13 03:44:58.120293
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual = FreeBSDVirtual()

    # When the virtualization_type is not empty, then it will return itself
    sysctl = dict(
        virtualization_type='xen',
        virtualization_role='guest',
        virtualization_tech_host=set(),
        virtualization_tech_guest=set(['xen'])
    )

    # When all sysctl's value is empty, then it will return the values in hw.model
    # We don't care about _uname_file, so we only pass empty dict to the constructor
    virtual_vendor_facts = dict(
        virtualization_type='vbox',
        virtualization_role='guest',
        virtualization_tech_host=set(['vbox']),
        virtualization_tech_guest=set(['vbox'])
    )

    hw

# Generated at 2022-06-13 03:45:02.013349
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    # Test if FreeBSDVirtualCollector is properly created.
    fv_collector = FreeBSDVirtualCollector()
    assert fv_collector._platform == "FreeBSD"
    assert fv_collector._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:45:04.687458
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    freebsd_virtual = FreeBSDVirtual()
    freebsd_virtual._module = "module"
    freebsd_virtual.get_virtual_facts()

# Generated at 2022-06-13 03:45:15.472994
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    host_tech = set()
    guest_tech = set()
    expected = {'virtualization_type':'xen', 'virtualization_role':'guest'}
    BSDVirtual = FreeBSDVirtual()

    kern_vm_guest = {'virtualization_tech_guest': host_tech, 'virtualization_tech_host': guest_tech,
                     'virtualization_type': '', 'virtualization_role': ''}
    hw_hv_vendor = {'virtualization_tech_guest': host_tech, 'virtualization_tech_host': guest_tech,
                    'virtualization_type': '', 'virtualization_role': ''}

# Generated at 2022-06-13 03:45:25.379727
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual_facts = {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set(),
    }
    kern_vm_guest_results = {
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set(),
    }
    hw_hv_vendor_results = {
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set(),
    }
    sec_jail_jailed_results = {
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set(),
    }

# Generated at 2022-06-13 03:45:27.901716
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_collector = FreeBSDVirtualCollector()
    assert virtual_collector
    assert isinstance(virtual_collector._fact_class, Virtual)

# Generated at 2022-06-13 03:45:30.986111
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    v = FreeBSDVirtual({})
    virtual_facts = v.get_virtual_facts()

    assert virtual_facts['virtualization_type'] == 'xen'
    assert virtual_facts['virtualization_role'] == 'guest'

# Generated at 2022-06-13 03:45:34.364593
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    freebsd_virtual_fact = FreeBSDVirtual()
    assert freebsd_virtual_fact.get_virtual_facts() == \
            {'virtualization_role': '', 'virtualization_type': '',
            'virtualization_tech_guest': set(), 'virtualization_tech_host': set()}

# Generated at 2022-06-13 03:45:36.819840
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_collector = FreeBSDVirtualCollector()
    assert virtual_collector._platform == 'FreeBSD'
    assert virtual_collector._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:45:42.906038
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fv = FreeBSDVirtualCollector()
    assert fv.platform == 'FreeBSD'
    assert fv._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:45:52.531816
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.freebsd import FreeBSDVirtual
    from ansible.module_utils.facts.virtual.dict import VirtualDict

    v_dict = VirtualDict(
        ['kern.vm_guest', 'hw.model', 'hw.hv_vendor', 'security.jail.jailed'],
        {
            'kern.vm_guest': 'other',  # VirtualBox
            'hw.model': 'VirtualBox',
            'hw.hv_vendor': '',
            'security.jail.jailed': '0',
        },
    )

    v_facts = FreeBSDVirtual(v_dict).get_virtual_facts()

    assert v_facts['virtualization_type'] == 'virtualbox'

# Generated at 2022-06-13 03:45:56.148828
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual = FreeBSDVirtual()
    virtual_facts = virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''

# Generated at 2022-06-13 03:45:57.508182
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    f = FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:45:59.182665
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    x = FreeBSDVirtualCollector()
    assert x.platform == 'FreeBSD'

# Generated at 2022-06-13 03:46:09.921397
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    freebsd_virtual = FreeBSDVirtual()

    # Get normal virtual fact
    freebsd_virtual.get_virtual_facts = lambda: {'virtualization_type': 'kvm',
                                                 'virtualization_role': 'guest',
                                                 'virtualization_tech_host': ['kvm', 'libvirt'],
                                                 'virtualization_tech_guest': ['kvm', 'libvirt'],
                                                 }
    assert freebsd_virtual.get_virtual_facts() == {'virtualization_type': 'kvm',
                                                   'virtualization_role': 'guest',
                                                   'virtualization_tech_host': ['kvm', 'libvirt'],
                                                   'virtualization_tech_guest': ['kvm', 'libvirt'],
                                                   }

    # Get

# Generated at 2022-06-13 03:46:11.708402
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual_facts = FreeBSDVirtual({}).get_virtual_facts()
    assert isinstance(virtual_facts, dict)
    for item in ['virtualization_type', 'virtualization_role']:
        assert item in virtual_facts

# Generated at 2022-06-13 03:46:12.909605
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert FreeBSDVirtualCollector._platform == 'FreeBSD'
    assert FreeBSDVirtualCollector._fact_class == FreeBSDVirtual


# Generated at 2022-06-13 03:46:15.782439
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    collector = FreeBSDVirtualCollector()
    assert collector.platform == 'FreeBSD'
    assert collector._fact_class == FreeBSDVirtual
    assert collector._platform == 'FreeBSD'

# Generated at 2022-06-13 03:46:19.658394
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual = FreeBSDVirtual()
    virtual_facts = virtual.get_virtual_facts()
    # Test if there is a virtualization_type key in the return dictionary
    assert 'virtualization_type' in virtual_facts
    # Test if there is a virtualization_role key in the return dictionary
    assert 'virtualization_role' in virtual_facts

# Generated at 2022-06-13 03:46:24.384755
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    VirtualCollector()

# Generated at 2022-06-13 03:46:25.937542
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    x = FreeBSDVirtualCollector()
    assert x.platform == 'FreeBSD'
    assert x.fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:46:27.400608
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    obj = FreeBSDVirtualCollector()
    assert obj.platform == 'FreeBSD'
    assert obj.fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:46:29.715615
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    collector = FreeBSDVirtualCollector('dummy_data')
    virtual_facts = collector.get_virtual_facts()
    assert virtual_facts.get('virtualization_role') == 'guest'
    assert virtual_facts.get('virtualization_type') == 'xen'
    assert 'xen' in virtual_facts.get('virtualization_tech_guest')
    assert 'xen' in virtual_facts.get('virtualization_tech_host')

# Generated at 2022-06-13 03:46:35.591783
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # pylint: disable=protected-access
    # Successful case
    module_utils = VirtualCollector._import_module_utils('FreeBSD')
    facts_module = FreeBSDVirtualCollector(module_utils=module_utils).collect()
    # If this call raises, get_virtual_facts has failed
    facts_module.populate()

    # Unsuccessful case: no module_utils imported
    facts_module = FreeBSDVirtualCollector().collect()
    ret = facts_module.get_virtual_facts()
    assert ret == {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set(),
    }



# Generated at 2022-06-13 03:46:38.397817
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fact_collector = FreeBSDVirtualCollector()
    assert fact_collector.platform == 'FreeBSD'
    assert fact_collector._fact_class == FreeBSDVirtual


# Generated at 2022-06-13 03:46:47.699093
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    freebsd_virtual = FreeBSDVirtual()
    freebsd_virtual.get_virtual_facts = MagicMock(return_value={
        'virtualization_type': 'xen',
        'virtualization_role': 'guest',
        'virtualization_tech_guest': set(['hvm'])
    })
    freebsd_virtual_facts = freebsd_virtual.get_virtual_facts()
    assert freebsd_virtual_facts['virtualization_type'] == 'xen'
    assert freebsd_virtual_facts['virtualization_role'] == 'guest'
    assert 'hvm' in freebsd_virtual_facts['virtualization_tech_guest']
    assert 'xen' in freebsd_virtual_facts['virtualization_tech_guest']
    assert 'kvm' not in free

# Generated at 2022-06-13 03:46:50.007422
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    collected_facts = FreeBSDVirtualCollector()
    assert collected_facts.platform == 'FreeBSD'



# Generated at 2022-06-13 03:46:52.252473
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    result = FreeBSDVirtualCollector()
    assert(result._platform == 'FreeBSD')
    assert(result._fact_class == FreeBSDVirtual)

# Generated at 2022-06-13 03:47:01.472868
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # Normal FreeBSD system
    freebsd_virtual = FreeBSDVirtual({})
    freebsd_virtual.get_virtual_facts()
    assert freebsd_virtual.virtual_facts['virtualization_type'] == ''
    assert freebsd_virtual.virtual_facts['virtualization_role'] == ''
    assert freebsd_virtual.virtual_facts['virtualization_technology_host'] == set()
    assert freebsd_virtual.virtual_facts['virtualization_technology_guest'] == set()

    # Virtualbox system
    freebsd_virtual = FreeBSDVirtual({'hw_model': 'VirtualBox 1'})
    freebsd_virtual.get_virtual_facts()
    assert freebsd_virtual.virtual_facts['virtualization_type'] == 'virtualbox'

# Generated at 2022-06-13 03:47:10.064517
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    '''Unit test for method get_virtual_facts of class FreeBSDVirtual'''
    obj_FreeBSDVirtual = FreeBSDVirtual()

    assert obj_FreeBSDVirtual.get_virtual_facts() == {
        'virtualization_role': '',
        'virtualization_type': '',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set()
    }

# Generated at 2022-06-13 03:47:11.624189
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fvc = FreeBSDVirtualCollector()
    facts = fvc.collect()
    assert isinstance(facts, dict)

# Generated at 2022-06-13 03:47:14.123198
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    vc = FreeBSDVirtualCollector()
    assert isinstance(vc, VirtualCollector)
    assert vc._platform == 'FreeBSD'
    assert vc._fact_class == FreeBSDVirtual
    assert vc.platforms == ('FreeBSD',)

# Generated at 2022-06-13 03:47:17.612509
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert issubclass(FreeBSDVirtualCollector, VirtualCollector)
    assert not issubclass(FreeBSDVirtualCollector, Virtual)
    assert FreeBSDVirtualCollector._fact_class == FreeBSDVirtual
    assert FreeBSDVirtualCollector._platform == 'FreeBSD'


# Generated at 2022-06-13 03:47:21.289615
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    facts = FreeBSDVirtual({}).get_virtual_facts()
    assert facts['virtualization_type'] in ['', 'xen']
    assert facts['virtualization_role'] in ['', 'guest']
    assert facts['virtualization_tech_guest'] == set()
    assert facts['virtualization_tech_host'] == set()

# Generated at 2022-06-13 03:47:30.977538
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.freebsd import FreeBSDVirtual
    from ansible.module_utils.facts.virtual.sysctl import VirtualSysctlDetectionMixin

    class FreeBSDVirtualTest(FreeBSDVirtual, VirtualSysctlDetectionMixin):
        pass

    fr = FreeBSDVirtualTest()
    fr.sysctl_cmd = 'sysctl -a'
    fr.sysctl_lines = [
        'kern.vm_guest=jail',
        'hw.hv_vendor=BHYVE',
        'security.jail.jailed=1',
        'hw.model=Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz'
    ]
    virtual_facts = fr.get_virtual_facts()


# Generated at 2022-06-13 03:47:33.852149
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual = FreeBSDVirtual(module=None)
    virtual_facts = virtual.get_virtual_facts()

    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts

# Generated at 2022-06-13 03:47:35.498732
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    testobj = FreeBSDVirtualCollector()
    assert testobj._platform == 'FreeBSD'
    assert testobj._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:47:37.932788
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    freebsd_virtual_collector = FreeBSDVirtualCollector()
    assert freebsd_virtual_collector._fact_class == FreeBSDVirtual
    assert freebsd_virtual_collector._platform == 'FreeBSD'

# Generated at 2022-06-13 03:47:40.997181
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    """
    This is a unit test for method get_virtual_facts.
    """

    virtual_facts = {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set()
    }

    virtual = FreeBSDVirtual()

    assert virtual_facts == virtual.get_virtual_facts()

# Generated at 2022-06-13 03:47:51.434958
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    bsd_virtual = FreeBSDVirtual()
    res_dict = bsd_virtual.get_virtual_facts()
    assert res_dict.get('virtualization_type') == ''
    assert res_dict.get('virtualization_role') == ''
    assert res_dict.get('virtualization_tech_host') == set()
    assert res_dict.get('virtualization_tech_guest') == set()

# Generated at 2022-06-13 03:47:53.678919
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    collector = FreeBSDVirtualCollector()
    assert isinstance(collector._fact_class, FreeBSDVirtual)
    assert collector._platform == 'FreeBSD'

# Generated at 2022-06-13 03:47:56.073406
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    f = FreeBSDVirtualCollector()
    assert f.__class__.__name__ == 'FreeBSDVirtualCollector'
    assert f._platform == 'FreeBSD'
    assert f._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:47:57.553868
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    facts = FreeBSDVirtualCollector()
    assert facts._platform == 'FreeBSD'
    assert facts._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:48:04.172129
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():

    # Arrange
    os_mock = mock.Mock()
    os_mock.path.exists.return_value = False
    sysctl_mock = mock.Mock()
    hw_mock = mock.Mock()
    virtual_facts = {'virtualization_type': '',
                     'virtualization_role': '',
                     'virtualization_tech_guest': set(),
                     'virtualization_tech_host': set()}

    # Assert
    assert FreeBSDVirtual(sysctl_mock, os_mock, hw_mock).get_virtual_facts() == virtual_facts

    # Arrange
    os_mock = mock.Mock()
    os_mock.path.exists.return_value = True
    sysctl_mock = mock.Mock()
    hw

# Generated at 2022-06-13 03:48:09.658219
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    fbsd_virtual = FreeBSDVirtual()
    virtual_facts = fbsd_virtual.get_virtual_facts()
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts

# Generated at 2022-06-13 03:48:12.530394
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virt_facts = FreeBSDVirtualCollector()
    assert virt_facts._fact_class == FreeBSDVirtual
    assert virt_facts._platform == 'FreeBSD'

# Generated at 2022-06-13 03:48:14.230875
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fv_col = FreeBSDVirtualCollector()
    assert fv_col.platform == 'FreeBSD'

# Generated at 2022-06-13 03:48:17.329938
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    vc = FreeBSDVirtualCollector()
    assert vc._platform == 'FreeBSD'

    assert isinstance(vc._fact_class, type)
    assert issubclass(vc._fact_class, Virtual)
    assert vc._fact_class.platform == 'FreeBSD'

# Generated at 2022-06-13 03:48:18.956285
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_facts = FreeBSDVirtualCollector.collect()
    assert "virtualization_type" in virtual_facts
    assert "virtualization_role" in virtual_facts

# Generated at 2022-06-13 03:48:32.015148
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fbc = FreeBSDVirtualCollector()
    assert isinstance(fbc, FreeBSDVirtual)

# Generated at 2022-06-13 03:48:40.652836
# Unit test for method get_virtual_facts of class FreeBSDVirtual

# Generated at 2022-06-13 03:48:50.452448
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # testing for KVM/QEMU
    guest_tech_list = ['qemu', 'kvm', 'hvm']
    host_tech_list = ['qemu', 'kvm', 'hvm']
    facter = FreeBSDVirtual(dict(hw_model='QEMU Virtual CPU version 2.5+'), dict(kern_vm_guest='other-bsd', hw_hv_vendor='KVMKVMKVM', security_jail_jailed=2))
    facts = facter.get_virtual_facts()

    assert facts['virtualization_type'] == 'kvm'
    assert facts['virtualization_role'] == 'guest'
    assert facts['virtualization_tech_guest'] == set(guest_tech_list)

# Generated at 2022-06-13 03:48:54.453440
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    facter = FreeBSDVirtual('freebsd')
    facter._get_virtual_facts()
    if facter.sysctl is None:
        raise AssertionError("facter._get_virtual_facts() failed")

# Generated at 2022-06-13 03:48:56.987517
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert FreeBSDVirtualCollector.__name__ == 'FreeBSDVirtualCollector'
    assert FreeBSDVirtualCollector._fact_class.__name__ == 'FreeBSDVirtual'
    assert FreeBSDVirtualCollector._platform == 'FreeBSD'

# Generated at 2022-06-13 03:49:05.356254
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    testobj = FreeBSDVirtual()

    # Testdata

# Generated at 2022-06-13 03:49:06.706562
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fbc = FreeBSDVirtualCollector()
    assert fbc.platform == 'FreeBSD'
    assert fbc.fact_class == FreeBSDVirtual


# Generated at 2022-06-13 03:49:11.724544
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    class TestFreeBSDVirtual(FreeBSDVirtual):
        @property
        def sysctl_all(self):
            return {
                    'kern.vm_guest': 'unknown',
                    'hw.model': 'VirtualBox',
                    'hw.hv_vendor': 'KVM',
                    'security.jail.jailed': '0'
            }

    test_obj = TestFreeBSDVirtual()
    vf = test_obj.get_virtual_facts()
    assert vf['virtualization_type'] == 'kvm'
    assert vf['virtualization_role'] == 'guest'
    assert vf['virtualization_tech_guest'] == {'kvm'}
    assert vf['virtualization_tech_host'] == {'kvm'}

# Generated at 2022-06-13 03:49:14.388316
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual_facts = FreeBSDVirtual(None).get_virtual_facts()
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts

# Generated at 2022-06-13 03:49:21.004270
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    fbsd_virtual = FreeBSDVirtual()
    test_facts = {'virtual_facts':
        {'virtualization_type': 'xen',
         'virtualization_role': 'guest',
         'virtualization_tech_guest': {'xen'},
         'virtualization_tech_host': set()}
    }
    assert(test_facts == fbsd_virtual.get_virtual_facts())

# Generated at 2022-06-13 03:49:55.431042
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    facts = FreeBSDVirtual({}).get_virtual_facts()

    # Test that the required fields have been populated
    assert 'virtualization_type' in facts
    assert 'virtualization_role' in facts

# Generated at 2022-06-13 03:49:56.518138
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert FreeBSDVirtualCollector.platform == 'FreeBSD'


# Generated at 2022-06-13 03:49:58.586611
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    freebsd_virtual_collector = FreeBSDVirtualCollector()
    assert freebsd_virtual_collector._platform == 'FreeBSD'
    assert freebsd_virtual_collector._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:50:03.625811
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    fake_freebsd_virtual = FreeBSDVirtual({}, {}, {})
    fake_freebsd_virtual.sysctl = {
        'hw.hv_vendor': 'bhyve',
        'kern.vm_guest': 'freebsd',
        'security.jail.jailed': 0,
        'security.jail.prison_uuid': '',
    }
    facts = fake_freebsd_virtual.get_virtual_facts()
    assert 'virtualization_role' in facts
    assert 'virtualization_type' in facts


# Generated at 2022-06-13 03:50:13.665632
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    '''Unit test method get_virtual_facts of class FreeBSDVirtual'''
    class VirtualSysctlDetectionMixinTest(FreeBSDVirtual):
        '''Test class for FreeBSDVirtual class.'''
        def detect_virt_product(self, item):
            '''Fake method for test class VirtualSysctlDetectionMixinTest.'''

# Generated at 2022-06-13 03:50:17.965848
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual = FreeBSDVirtual()
    virtual_facts = virtual.get_virtual_facts()
    assert type(virtual_facts) is dict
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualization_system' in virtual_facts

# Generated at 2022-06-13 03:50:19.475404
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    obj = FreeBSDVirtualCollector()
    assert obj.platform == 'FreeBSD'
    assert obj._fact_class.platform == 'FreeBSD'
    assert issubclass(obj._fact_class, Virtual)
    assert obj.collect() is not None

# Generated at 2022-06-13 03:50:21.153246
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_facts = FreeBSDVirtualCollector().collect()
    assert 'freebsd' in virtual_facts['ansible_virtual_subtype']

# Generated at 2022-06-13 03:50:25.254913
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # file device.hints does not exist
    facts = FreeBSDVirtual({})
    facts.collect()
    expected_virtual_facts = {'virtualization_role': '', 'virtualization_tech_guest': set([]), 'virtualization_tech_host': set([]), 'virtualization_type': ''}
    assert facts.virtual_facts == expected_virtual_facts


# Generated at 2022-06-13 03:50:29.030116
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    facts = FreeBSDVirtual({}).get_virtual_facts()
    assert 'virtualization_type' in facts
    assert 'virtualization_role' in facts
    assert 'virtualization_tech_guest' in facts
    assert 'virtualization_tech_host' in facts

# Generated at 2022-06-13 03:51:41.470804
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual = FreeBSDVirtual()
    virtual_facts = virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''

# Generated at 2022-06-13 03:51:44.046585
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    fv = FreeBSDVirtual()
    result = fv.get_virtual_facts()
    assert result.get('virtualization_type') == 'xen'
    assert result.get('virtualization_role') == 'guest'

# Generated at 2022-06-13 03:51:45.493933
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert FreeBSDVirtualCollector._fact_class is FreeBSDVirtual
    assert FreeBSDVirtualCollector._platform == 'FreeBSD'

# Generated at 2022-06-13 03:51:47.291785
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    vc = FreeBSDVirtualCollector()
    assert vc._platform == 'FreeBSD'
    assert vc._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:51:50.254242
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_collector = FreeBSDVirtualCollector()

    # Test return value of constructor
    assert virtual_collector._platform == 'FreeBSD'
    assert virtual_collector._fact_class == FreeBSDVirtual
    assert virtual_collector._fact_class.platform == 'FreeBSD'

# Generated at 2022-06-13 03:51:52.957233
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    facts_dict = VirtualCollector._get_platform_fact_classes()
    print(facts_dict)
    assert 'FreeBSDVirtualCollector' in facts_dict

# Generated at 2022-06-13 03:52:01.114340
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    fact_class = FreeBSDVirtual()
    fact_class.sysctl_return = {
        "hw.hv_vendor": "my_vendor",
        "hw.model": "my_model",
        "kern.vm_guest": "my_guest",
        "security.jail.jailed": "my_jailed"
    }
    fact_class.hw_model_return = {
        "virtualization_type": "invalid_type",
        "virtualization_role": "invalid_role",
        "virtualization_vendor": "invalid_vendor",
        "virtualization_product": "invalid_product",
        "virtualization_tech_guest": ["invalid_guest_tech"],
        "virtualization_tech_host": ["invalid_host_tech"]
    }



# Generated at 2022-06-13 03:52:02.180469
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    obj = FreeBSDVirtualCollector()
    assert obj.platform == 'FreeBSD'
    assert obj._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:52:03.453277
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    return FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:52:03.977754
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert FreeBSDVirtualCollector