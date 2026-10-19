

# Generated at 2022-06-13 03:43:53.295615
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virt = FreeBSDVirtualCollector()
    assert virt._platform == 'FreeBSD'
    assert repr(virt) == '<freebsd.FreeBSDVirtualCollector>'

# Generated at 2022-06-13 03:43:55.959378
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fbc = FreeBSDVirtualCollector()
    assert isinstance(fbc, VirtualCollector)
    assert fbc._platform == 'FreeBSD'
    assert fbc._fact_class is FreeBSDVirtual

# Generated at 2022-06-13 03:44:05.321328
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    """
    This test checks the facts returned by method get_virtual_facts
    """
    # Create virtual object
    v = FreeBSDVirtual()
    # Get virtual facts and check values
    virtual_facts = v.get_virtual_facts()
    assert isinstance(virtual_facts, dict)
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts
    assert isinstance(virtual_facts['virtualization_type'], str)
    assert isinstance(virtual_facts['virtualization_role'], str)
    assert isinstance(virtual_facts['virtualization_tech_guest'], set)

# Generated at 2022-06-13 03:44:06.879488
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    FreeBSDVirtualCollector()


# Generated at 2022-06-13 03:44:11.933946
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual_facts = FreeBSDVirtual().get_virtual_facts()
    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''
    assert virtual_facts['virtualization_tech_guest'] == set()
    assert virtual_facts['virtualization_tech_host'] == set()

# Generated at 2022-06-13 03:44:21.594400
# Unit test for method get_virtual_facts of class FreeBSDVirtual

# Generated at 2022-06-13 03:44:23.428430
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fbc = FreeBSDVirtualCollector()
    assert fbc._fact_class == FreeBSDVirtual
    assert fbc._platform == 'FreeBSD'

# Generated at 2022-06-13 03:44:25.360598
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    collector = FreeBSDVirtualCollector()
    assert collector.platform == 'FreeBSD'
    assert collector.fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:44:27.075293
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    collector = FreeBSDVirtualCollector()
    assert collector.platform == 'FreeBSD'
    assert collector._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:44:28.554008
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    frees = FreeBSDVirtual()
    assert frees.get_virtual_facts() == {'virtualization_type': '',
                                         'virtualization_role': ''}

# Generated at 2022-06-13 03:44:40.660421
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # pylint: disable=protected-access
    # Create instance of FreeBSDVirtual
    freebsd_virtual = FreeBSDVirtual()
    # Run the get_virtual_facts method of the instance
    facts = freebsd_virtual._get_virtual_facts()
    assert facts['virtualization_type'] == 'vmware'

# Generated at 2022-06-13 03:44:44.863694
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # Both of the _detect_virt_product and _detect_virt_vendor methods are
    # tested in their own test module.  Here, we only test the values those
    # methods return are set correctly.
    facter = FreeBSDVirtual()
    facter._detect_virt_product = lambda x: {'virtualization_type': 'xen',
                                             'virtualization_role': 'guest',
                                             'virtualization_tech_guest': set('xen'),
                                             'virtualization_tech_host': set('xen')}

# Generated at 2022-06-13 03:44:48.720058
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    """
    Unit test for method get_virtual_facts of class FreeBSDVirtual
    """
    virtual_facts = FreeBSDVirtual({}).get_virtual_facts()
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts


# Generated at 2022-06-13 03:44:50.695572
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_collector = FreeBSDVirtualCollector()
    assert isinstance(virtual_collector, VirtualCollector)


# Generated at 2022-06-13 03:45:00.231322
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():

    from ansible.module_utils.facts.virtual.freebsd import FreeBSDVirtual
    from ansible.module_utils.facts.virtual.sysctl import VirtualSysctlDetectionMixin

    class FreeBSDVirt(FreeBSDVirtual, VirtualSysctlDetectionMixin):
        platform = 'FreeBSD'

        def detect_virt_product(self, key):
            if key == 'kern.vm_guest':
                return {'virtualization_type': '', 'virtualization_role': '',
                        'virtualization_tech_guest': set(),
                        'virtualization_tech_host': set()}

# Generated at 2022-06-13 03:45:01.967305
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert FreeBSDVirtualCollector._platform == 'FreeBSD'
    assert FreeBSDVirtualCollector._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:45:04.282739
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    collect_virt = FreeBSDVirtualCollector()
    assert isinstance(collect_virt._fact_class, FreeBSDVirtual)

# Generated at 2022-06-13 03:45:04.903421
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:45:08.871865
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virt = FreeBSDVirtual()

    # Add virtualization_type and virtualization_role properties to the dict
    # returned by method get_virtual_facts of class FreeBSDVirtual
    assert virt.get_virtual_facts()['virtualization_type'] is not None
    assert virt.get_virtual_facts()['virtualization_role'] is not None

# Generated at 2022-06-13 03:45:14.930833
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual = FreeBSDVirtual()
    virtual_facts = virtual.get_virtual_facts()
    if virtual_facts['virtualization_type'] == 'xen':
        assert virtual_facts['virtualization_role'] == 'guest'
    assert virtual_facts['virtualization_tech_guest'] == set()
    assert virtual_facts['virtualization_tech_host'] == set()

# Generated at 2022-06-13 03:45:27.208934
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual = FreeBSDVirtual()
    virtual_facts = virtual.get_virtual_facts()
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts

# Generated at 2022-06-13 03:45:29.213912
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    """Ensure that the constructor returns an object with the expected type"""
    collector = FreeBSDVirtualCollector()
    assert isinstance(collector, FreeBSDVirtualCollector)

# Generated at 2022-06-13 03:45:31.406628
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    facts = FreeBSDVirtual({}).get_virtual_facts()
    assert 'virtualization_type' in facts
    assert 'virtualization_role' in facts
    assert 'virtualization_tech_host' in facts
    assert 'virtualization_tech_guest' in facts

# Generated at 2022-06-13 03:45:32.762869
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fv = FreeBSDVirtualCollector()
    assert fv.platform == 'FreeBSD'
    assert isinstance(fv.get_all(), dict)

# Generated at 2022-06-13 03:45:36.944737
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual_facts = FreeBSDVirtual().get_virtual_facts()

    assert set(virtual_facts['virtualization_tech_host']) == set()
    assert set(virtual_facts['virtualization_tech_guest']) == set()

    virtual_facts = FreeBSDVirtual(dict(platform='FreeBSD', kern_vm_guest='guest_xen, guest_openbsd')).get_virtual_facts()
    assert set(virtual_facts['virtualization_tech_host']) == set()
    assert set(virtual_facts['virtualization_tech_guest']) == set(['xen', 'openbsd'])

    virtual_facts = FreeBSDVirtual(dict(platform='FreeBSD', hw_hv_vendor='bhyve')).get_virtual_facts()

# Generated at 2022-06-13 03:45:39.834954
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    c = FreeBSDVirtualCollector()
    assert type(c).__name__ == 'FreeBSDVirtualCollector'

# Generated at 2022-06-13 03:45:45.766255
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    v = FreeBSDVirtual({})
    v.collect_platform_subset_facts = lambda *args, **kwargs: None
    v._module = FakeModule()
    v.get_virtual_facts()
    assert v.virtual_subtype == 'xen'
    assert v.virtual_facts['virtualization_type'] == 'xen'
    assert v.virtual_facts['virtualization_role'] == 'guest'



# Generated at 2022-06-13 03:45:47.326902
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    vc = FreeBSDVirtualCollector()
    assert type(vc) == FreeBSDVirtualCollector

# Generated at 2022-06-13 03:45:49.282927
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    collector = FreeBSDVirtualCollector()
    assert collector.platform == 'FreeBSD'
    assert collector.fact_class.platform == 'FreeBSD'

# Generated at 2022-06-13 03:45:51.351628
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    vc = FreeBSDVirtualCollector()
    assert vc._platform == 'FreeBSD'
    assert vc._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:46:02.559570
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual_facts = FreeBSDVirtual().get_virtual_facts()
    assert isinstance(virtual_facts, dict)

# Generated at 2022-06-13 03:46:08.909414
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # Test empty virtual facts
    virtual_facts = {}
    virtual_facts['virtualization_type'] = ''
    virtual_facts['virtualization_role'] = ''
    virtual_facts['virtualization_tech_host'] = set()
    virtual_facts['virtualization_tech_guest'] = set()

    # Test get_virtual_facts method
    vm = FreeBSDVirtual({'ansible_facts': {}})
    assert vm.get_virtual_facts() == virtual_facts



# Generated at 2022-06-13 03:46:11.800601
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    collector = FreeBSDVirtualCollector(None, None)
    assert collector.platform == 'FreeBSD'
    assert collector.fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:46:22.257255
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    module = AnsibleModule(
        argument_spec=dict()
    )

    # Mock VMware sysctl variables
    sysctl_res = dict(
        security_jail_jailed='0',
        kern_vm_guest='other',
        hw_model='',
        hw_hv_vendor='vmware',
        hw_hv_name='vmware',
        hw_hv_version='',
    )
    class ModuleMockVMware:
        def __init__(self):
            self.params = dict(
                sysctl=sysctl_res,
                path='/sbin:/usr/sbin:/bin:/usr/bin',
            )

    # Mock VirtualBox sysctl variables

# Generated at 2022-06-13 03:46:24.769015
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fv = FreeBSDVirtualCollector()
    assert isinstance(fv, FreeBSDVirtualCollector)
    assert fv.platform == 'FreeBSD'
    assert fv.fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:46:26.584549
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    vc = FreeBSDVirtualCollector()
    assert vc.platform == 'FreeBSD'
    assert vc._fact_class is FreeBSDVirtual

# Generated at 2022-06-13 03:46:28.084637
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fact = FreeBSDVirtualCollector()
    assert fact._fact_class == FreeBSDVirtual
    assert fact._platform == 'FreeBSD'

# Generated at 2022-06-13 03:46:35.141680
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    v = FreeBSDVirtual()
    facts = {}

    v.collect_sysctl_facts = lambda x: {'kern.vm_guest': 'none'}
    facts.update(v.get_virtual_facts())
    assert facts['virtualization_type'] == ''
    assert facts['virtualization_role'] == ''
    assert facts['virtualization_tech_guest'] == set()
    assert facts['virtualization_tech_host'] == set()

    v.collect_sysctl_facts = lambda x: {'kern.vm_guest': 'vmware'}
    facts.update(v.get_virtual_facts())
    assert facts['virtualization_type'] == 'vmware'
    assert facts['virtualization_role'] == 'guest'

# Generated at 2022-06-13 03:46:42.197330
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # Set of _virtual_facts that will be returned by method get_virtual_facts
    # when all of the sysctl/sysctl are defined.
    _virtual_facts = dict(
        virtualization_type='xen',
        virtualization_role='guest',
        virtualization_tech_host=set(['xen']),
        virtualization_tech_guest=set(['xen']),
        )

    # Execute method and validate
    assert FreeBSDVirtual.get_virtual_facts(None) == _virtual_facts

# Generated at 2022-06-13 03:46:45.397837
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_collector = FreeBSDVirtualCollector()
    assert virtual_collector._fact_class == FreeBSDVirtual
    assert virtual_collector._platform == 'FreeBSD'
    assert virtual_collector._fact_class._platform == 'FreeBSD'


# Generated at 2022-06-13 03:47:10.590801
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_class = FreeBSDVirtualCollector()
    assert virtual_class._fact_class == FreeBSDVirtual
    assert virtual_class._platform == 'FreeBSD'

# Generated at 2022-06-13 03:47:12.509409
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    fbsd_virtual = FreeBSDVirtual()
    result = fbsd_virtual.get_virtual_facts()

    assert result['virtualization_type'] == ''
    assert result['virtualization_role'] == ''
    assert result['virtualization_tech_guest'] == set()
    assert result['virtualization_tech_host'] == set()

# Generated at 2022-06-13 03:47:12.835924
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:47:13.578469
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    pass

# Generated at 2022-06-13 03:47:15.696644
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fv = FreeBSDVirtualCollector()
    assert fv._platform == 'FreeBSD'


# Generated at 2022-06-13 03:47:16.246839
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:47:21.192912
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    """
    Test the FreeBSDVirtual subclass of the Virtual class.
    """
    virtual = FreeBSDVirtual()

    # The following are examples of output of the three commands used
    # to detect FreeBSD virtualization_type and virtualization_role.
    # kern.vm_guest
    kern_vm_guest = (
        'none',
        'xen',
        'vmware',
        'pc98',
    )
    # hw.hv_vendor
    hw_hv_vendor = (
        'None',
        'Xen',
        'Bhyve',
    )
    # security.jail.jailed
    sec_jail_jailed = (
        0,
        1,
    )
    # hw.model

# Generated at 2022-06-13 03:47:21.919043
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert FreeBSDVirtualCollector(None, None, None)


# Generated at 2022-06-13 03:47:27.204826
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual_facts = FreeBSDVirtual().get_virtual_facts()
    assert len(virtual_facts) == 4
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts

# Generated at 2022-06-13 03:47:27.899739
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:47:54.027379
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    freebsd_collector = FreeBSDVirtualCollector()
    assert freebsd_collector

# Generated at 2022-06-13 03:47:57.745774
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual_facts = FreeBSDVirtual().get_virtual_facts()
    assert virtual_facts['virtualization_type'].startswith('xen') \
           or 'vmware' in virtual_facts['virtualization_type'] \
           or 'jail' in virtual_facts['virtualization_type'] \
           or virtual_facts['virtualization_type'] == ''

# Generated at 2022-06-13 03:47:58.229186
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:47:59.340365
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fact = FreeBSDVirtualCollector().collect()
    assert fact['virtualization_type'] != ''

# Generated at 2022-06-13 03:48:02.343253
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    from ansible.module_utils.facts.virtual import FreeBSDVirtualCollector
    fvc = FreeBSDVirtualCollector()
    assert fvc.name == 'FreeBSD'

# Generated at 2022-06-13 03:48:13.796428
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # There are no hypervisor sysctl, therefore virtualization_type/role and
    # tech_host should be empty
    fact = FreeBSDVirtual({}, {})
    facts = {
        'kern.vm_guest': 'none',
        'security.jail.jailed': '0',
        'hw.hv_vendor': 'none',
        'hw.model': 'i386'
    }
    assert fact.get_virtual_facts(facts) == {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_tech_host': set(),
        'virtualization_tech_guest': set(['hardware'])
    }

    # Virtualization_type should be set, because sysctl kern.vm_guest contains
    # a value other than 'none'


# Generated at 2022-06-13 03:48:16.224166
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    freebsd_virtual_collector = FreeBSDVirtualCollector()
    assert freebsd_virtual_collector._fact_class == FreeBSDVirtual
    assert freebsd_virtual_collector._platform == 'FreeBSD'

# Generated at 2022-06-13 03:48:18.839080
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    import sys
    if sys.version_info[0] == 2:
        assert issubclass(FreeBSDVirtualCollector, VirtualCollector)
    else:
        assert issubclass(FreeBSDVirtualCollector, VirtualCollector)

# Generated at 2022-06-13 03:48:20.666378
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert isinstance(FreeBSDVirtualCollector().get_virtual_facts()['virtualization_tech_host'], set)

# Generated at 2022-06-13 03:48:22.654414
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_facts_collector = FreeBSDVirtualCollector()
    assert virtual_facts_collector.platform == 'FreeBSD'
    assert virtual_facts_collector._fact_class.__name__ == 'FreeBSDVirtual'

# Generated at 2022-06-13 03:48:58.066847
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    facts_dict = dict()
    fvc = FreeBSDVirtualCollector(facts_dict)
    assert hasattr(fvc, 'platform')
    assert hasattr(fvc, '_fact_class')

# Generated at 2022-06-13 03:48:58.621623
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:49:01.189395
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    freebsd_virtual_collector = FreeBSDVirtualCollector()
    assert freebsd_virtual_collector._fact_class == FreeBSDVirtual
    assert freebsd_virtual_collector._platform == 'FreeBSD'

# Generated at 2022-06-13 03:49:08.357245
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    freebsd_virtual_facts = FreeBSDVirtual({})

    # No sysctl available, thus no virtualization_type, etc.
    # Since this is not a Virtualization system, we define:
    # - virtualization_type = ''
    # - virtualization_role = ''
    freebsd_virtual_facts.sysctl = {}
    freebsd_virtual_facts.now_remote = False
    freebsd_facts = freebsd_virtual_facts.get_virtual_facts()
    assert freebsd_facts['virtualization_type'] == ''
    assert freebsd_facts['virtualization_role'] == ''

    # sysctl available, but does not define any virtualization
    # Since this is not a Virtualization system, we define:
    # - virtualization_type = ''
    # - virtualization_role = ''
   

# Generated at 2022-06-13 03:49:10.562565
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    bootstrap = FreeBSDVirtualCollector()
    assert bootstrap._fact_class == FreeBSDVirtual
    assert bootstrap._platform == 'FreeBSD'


# Generated at 2022-06-13 03:49:12.791824
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    collector = FreeBSDVirtualCollector()
    assert isinstance(collector._collector, FreeBSDVirtual)


# Generated at 2022-06-13 03:49:22.908117
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    from ansible_collections.ansible.community.plugins.module_utils.facts.virtual.freebsd import Virtual
    from ansible_collections.ansible.community.plugins.module_utils.facts.virtual.sysctl import VirtualSysctlDetectionMixin

    virtual = Virtual()
    virtual.platform = 'FreeBSD'
    # Mock the sysctl dictionary
    virtual.sysctl = {'hw.hv_vendor': 'QEMU',
                      'kern.vm_guest': 'none',
                      'security.jail.jailed': '0',
                      'hw.model': 'AMD-Opteron-2378'}

# Generated at 2022-06-13 03:49:24.731241
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    facts = FreeBSDVirtualCollector()
    assert facts.platform == 'FreeBSD'
    assert isinstance(facts.collect(), dict)



# Generated at 2022-06-13 03:49:28.440599
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    ''' unit tests for FreeBSDVirtualCollector() '''

    # Create a FreeBSDVirtualCollector object and then check all of the
    # attributes of the object
    obj = FreeBSDVirtualCollector()
    assert obj._platform == 'FreeBSD'
    assert obj._fact_class == FreeBSDVirtual
    assert obj._fact_class._platform == 'FreeBSD'

# Generated at 2022-06-13 03:49:29.787240
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    bsd_virtual_fact = FreeBSDVirtual({})
    bsd_virtual_fact.get_virtual_facts()

# Generated at 2022-06-13 03:50:14.662508
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():

    # test for 'xen' virtualizations
    sysctl_kern = '''
kern.vm_guest=xen
hw.hv_vendor=XEN
security.jail.jailed=0
    '''

    sysctl_vendor = 'VMware Virtual Platform'

    virtual = FreeBSDVirtual(sysctl_kern=sysctl_kern, sysctl_vendor=sysctl_vendor)
    virtual_facts = virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'xen'
    assert virtual_facts['virtualization_role'] == 'guest'
    assert virtual_facts['virtualization_tech_guest'] == {'xen'}
    assert virtual_facts['virtualization_tech_host'] == set()

    # test for 'openvz' virtual

# Generated at 2022-06-13 03:50:15.836504
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    result = FreeBSDVirtualCollector()
    assert result is not None

# Generated at 2022-06-13 03:50:17.927470
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_collector = FreeBSDVirtualCollector()
    assert isinstance(virtual_collector._fact_class, FreeBSDVirtual)
    assert virtual_collector._platform == 'FreeBSD'

# Generated at 2022-06-13 03:50:20.939990
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    # Test for subclass of VirtualCollector
    assert issubclass(FreeBSDVirtualCollector, VirtualCollector)
    # Test for class of FreeBSDVirtualCollector
    assert FreeBSDVirtualCollector == FreeBSDVirtualCollector()
    # Test for class of FreeBSDVirtualCollector.fact_class
    assert FreeBSDVirtual == FreeBSDVirtualCollector.fact_class
    # Test for class of FreeBSDVirtualCollector.fact_class.platform
    assert 'FreeBSD' == FreeBSDVirtualCollector.fact_class.platform
    # Test for instantiation of FreeBSDVirtualCollector
    assert FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:50:22.276457
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_collector = FreeBSDVirtualCollector()
    assert virtual_collector._platform == 'FreeBSD'

# Generated at 2022-06-13 03:50:23.520326
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_collector = FreeBSDVirtualCollector()
    assert virtual_collector is not None

# Generated at 2022-06-13 03:50:24.763144
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    v = FreeBSDVirtualCollector()
    assert v.platform == 'FreeBSD'

# Generated at 2022-06-13 03:50:26.949256
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    d = FreeBSDVirtualCollector(None)
    assert d.platform == 'FreeBSD'

# Generated at 2022-06-13 03:50:30.085846
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    # Create instance of FreeBSDVirtualCollector
    fvc = FreeBSDVirtualCollector()
    # Verify class attribute _platform
    assert fvc._platform == 'FreeBSD'
    # Verify class attribute _fact_class
    assert fvc._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:50:31.059525
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:51:44.083197
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fb = FreeBSDVirtualCollector()
    assert fb._platform == "FreeBSD"
    assert isinstance(fb._fact_class, FreeBSDVirtual)

# Generated at 2022-06-13 03:51:46.126977
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual_facts = FreeBSDVirtual().get_virtual_facts()
    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''

# Generated at 2022-06-13 03:51:47.567941
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    collector = FreeBSDVirtualCollector()
    assert collector.platform == 'FreeBSD'
    assert collector.fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:51:49.440160
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    instances = FreeBSDVirtualCollector.fetch_virtual_instances()
    instance = instances[0]
    assert instance.platform == 'FreeBSD'


# Generated at 2022-06-13 03:51:50.715614
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    "Check FreeBSDVirtualCollector constructor"
    fvirt = FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:51:54.043012
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual_facts = FreeBSDVirtual(None).get_virtual_facts()
    assert isinstance(virtual_facts, dict)
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts

# Generated at 2022-06-13 03:51:57.262012
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual = FreeBSDVirtual({})
    assert 'virtualization_type' in virtual.get_virtual_facts()
    assert 'virtualization_role' in virtual.get_virtual_facts()
    assert 'virtualization_type_role' in virtual.get_virtual_facts()


# Generated at 2022-06-13 03:52:00.675514
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # Sample virtual_facts returned by class FreeBSDVirtual for a FreeBSD host.
    facts = {u'virtualization_type': u'', u'virtualization_role': u'',
             u'virtualization_tech_guest': set(),
             u'virtualization_tech_host': set()}

    assert FreeBSDVirtual(None).get_virtual_facts() == facts

# Generated at 2022-06-13 03:52:03.065380
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    v = FreeBSDVirtual()
    v.facts_cache = dict()
    v.collect_platform_subset_facts = lambda: None
    v.get_virtual_facts()
    assert v.facts['virtualization_type'] == 'xen'
    assert v.facts['virtualization_role'] == 'guest'

# Generated at 2022-06-13 03:52:05.105528
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fv = FreeBSDVirtualCollector()
    assert fv._platform == 'FreeBSD'
    assert isinstance(fv._fact_class, FreeBSDVirtual)

# Generated at 2022-06-13 03:53:19.304024
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    from ansible.module_utils.facts.virtual.freebsd import FreeBSDVirtualCollector
    from ansible.module_utils.facts.virtual.base import VirtualCollector

    f = FreeBSDVirtualCollector()
    assert isinstance(f, VirtualCollector)
    assert f.platform == 'FreeBSD'
    assert f.fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:53:21.590543
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    _FreeBSDVirtualCollector = FreeBSDVirtualCollector()
    assert _FreeBSDVirtualCollector._platform == 'FreeBSD'

# Generated at 2022-06-13 03:53:29.816830
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():

    def hw_model(value):
        return {'hw.model': value}

    def kern_vm_guest(value):
        return {'kern.vm_guest': value}

    def hw_hv_vendor(value):
        return {'hw.hv_vendor': value}

    def sec_jail_jailed(value):
        return {'security.jail.jailed': value}

    def test_data(args, expected_results, *kwargs):
        obj = FreeBSDVirtual({}, *kwargs)
        obj.detect_virt_product = lambda x: args.get(x, {})
        obj.detect_virt_vendor = lambda x: args.get(x, {})
        results = obj.get_virtual_facts()

# Generated at 2022-06-13 03:53:36.783587
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    '''Unit test for method get_virtual_facts of class FreeBSDVirtual'''
    virtual = FreeBSDVirtual(None)
    virtual.sysctl_return = {
        'security.jail.jailed': '1',
        'hw.hv_vendor': 'bhyve',
        'security.jail.name': 'VM',
        'kern.vm_guest': 'bhyve',
        'hw.model': 'FreeBSD'
    }
    virtual_facts = virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'bhyve'
    assert virtual_facts['virtualization_role'] == 'guest'
    assert 'vmware' in virtual_facts['virtualization_tech_host']
    assert 'bhyve' in virtual_facts['virtualization_tech_guest']

# Generated at 2022-06-13 03:53:47.073380
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    facts = {}
    facts['kernel'] = 'FreeBSD'

    # Test get_virtual_facts on a virtual host
    kern_vm_guest_return = {'kern.vm_guest': 'bhyve'}
    hw_hv_vendor_return = {'hw.hv_vendor': 'bhyve'}
    sec_jail_jailed_return = {'security.jail.jailed': 0}
    virtual_vendor_facts_return = {'hw.model': 'vmm'}