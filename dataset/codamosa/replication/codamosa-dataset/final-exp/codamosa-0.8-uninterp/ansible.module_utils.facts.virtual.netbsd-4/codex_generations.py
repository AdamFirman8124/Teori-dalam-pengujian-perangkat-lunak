

# Generated at 2022-06-13 04:09:55.396464
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    netbsdVirtualCollector = NetBSDVirtualCollector()
    assert netbsdVirtualCollector._fact_class == NetBSDVirtual

# Generated at 2022-06-13 04:09:56.504929
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd = NetBSDVirtual()
    assert netbsd.platform == "NetBSD"

# Generated at 2022-06-13 04:10:00.201594
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual(None, None)
    assert netbsd_virtual.platform == 'NetBSD'

# Generated at 2022-06-13 04:10:02.158565
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual()
    assert netbsd_virtual.platform == 'NetBSD'

# Generated at 2022-06-13 04:10:04.039433
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual_facts = NetBSDVirtual()
    virtual_facts.get_virtual_facts()


# Generated at 2022-06-13 04:10:05.771790
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    try:
        my_obj = NetBSDVirtualCollector()
    except Exception:
        assert False


# Generated at 2022-06-13 04:10:06.862299
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual_facts = NetBSDVirtual()
    assert virtual_facts.platform == 'NetBSD'

# Generated at 2022-06-13 04:10:12.431119
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.netbsd import VirtualNetBSD
    from ansible.module_utils.facts.virtual.netbsd import VirtualNetBSDCollector
    host_tech = set()
    guest_tech = set()
    virtual_facts = {}
    virtual_facts['virtualization_type'] = ''
    virtual_facts['virtualization_role'] = ''
    virtual_vendor_facts = VirtualNetBSD._detect_virt_vendor('machdep.hypervisor')
    guest_tech.update(virtual_vendor_facts['virtualization_tech_guest'])
    host_tech.update(virtual_vendor_facts['virtualization_tech_host'])
    virtual_facts.update(virtual_vendor_facts)
    virtual_product_facts = VirtualNetBSD._detect_virt_

# Generated at 2022-06-13 04:10:19.357774
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
  # Set up a mock of module Utils
  utils = Utils(platform='NetBSD', module=None)
  # Instantiate the NetBSDVirtual class.
  netbsd_virtual_class = NetBSDVirtual(utils)

  # Run the get_virtual_facts() method.
  virtual_facts = netbsd_virtual_class.get_virtual_facts()

  # Test result
  assert expected == virtual_facts


# Generated at 2022-06-13 04:10:26.549674
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    collector = NetBSDVirtualCollector({}, {})
    fact_class = collector._fact_class({}, {})
    virtual_facts = fact_class.get_virtual_facts()

    assert virtual_facts['virtualization_type'] == 'hardware'
    assert virtual_facts['virtualization_role'] == 'host'
    assert virtual_facts['virtualization_tech_guest'] == set()
    assert virtual_facts['virtualization_tech_host'] == {'hardware'}

# Generated at 2022-06-13 04:10:39.574249
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual = NetBSDVirtual()
    virtual._platform = 'NetBSD'

    # Test detection of no virtualization
    virtual._sysctl_all_info = {}
    virtual_facts = virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == ''
    assert not virtual_facts['virtualization_tech_guest']
    assert not virtual_facts['virtualization_tech_host']
    assert virtual_facts['virtualization_role'] == ''

    # Test detection of a nested virtualization
    virtual._sysctl_all_info = {'machdep.dmi.system-product': 'Xen HVM domU'}
    virtual_facts = virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'xen'

# Generated at 2022-06-13 04:10:41.898225
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    c = NetBSDVirtualCollector()
    f = c.fetch_virtual_facts()
    assert isinstance(f, NetBSDVirtual)



# Generated at 2022-06-13 04:10:53.477473
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virt = NetBSDVirtual({}, None)

    # empty sysctl
    virt.sysctl = {}

    # No virtualization
    assert virt.get_virtual_facts()['virtualization_type'] == ''

    # OpenVZ virtualization
    virt.sysctl = {'machdep.hypervisor': 'OpenVZ HN'}
    assert virt.get_virtual_facts()['virtualization_type'] == 'openvz'
    assert virt.get_virtual_facts()['virtualization_role'] == 'guest'

    # VirtualBox virtualization
    virt.sysctl = {'machdep.dmi.system-product': 'VirtualBox'}
    assert virt.get_virtual_facts()['virtualization_type'] == 'virtualbox'

# Generated at 2022-06-13 04:11:03.088044
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    netbsd_virtual_facts = dict(
        virtualization_type='',
        virtualization_role='',
        virtualization_tech_guest=set(),
        virtualization_tech_host=set(),
    )
    # Test for empty values
    assert NetBSDVirtual().get_virtual_facts() == netbsd_virtual_facts

    # Test for values from vmware
    netbsd_virtual_facts['virtualization_type'] = 'vmware'
    netbsd_virtual_facts['virtualization_role'] = 'guest'
    netbsd_virtual_facts['virtualization_tech_guest'].add('vmware')
    assert NetBSDVirtual().get_virtual_facts() == netbsd_virtual_facts

# Generated at 2022-06-13 04:11:13.385988
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    netbsd_virtual = NetBSDVirtual()
    res = netbsd_virtual.get_virtual_facts()

    # Result
    assert res.keys() == {'virtualization_type', 'virtualization_role', 'virtualization_tech_host', 'virtualization_tech_guest', 'virtualization_sysctl_args'}
    assert res['virtualization_tech_host'] == set()
    assert res['virtualization_tech_guest'] == {'kvm', 'xen'}
    assert res['virtualization_sysctl_args'] == ['machdep.dmi.system-vendor', 'machdep.dmi.system-product', 'machdep.hypervisor']

# Generated at 2022-06-13 04:11:17.444977
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    fake_sysctl_data = {
        'machdep.dmi.system-product': 'ABCD',
        'machdep.dmi.system-vendor': 'AB',
        'machdep.hypervisor': 'hypervisor_type'
    }
    test_virtual = NetBSDVirtual(sysctl_data=fake_sysctl_data)
    test_facts = test_virtual.get_virtual_facts()
    virtual_facts = {}
    virtual_facts['virtualization_type'] = 'hypervisor_type'
    virtual_facts['virtualization_role'] = 'guest'
    virtual_facts['virtualization_tech_host'] = 'hypervisor_type'
    virtual_facts['virtualization_tech_guest'] = 'hypervisor_type'
    assert test_facts == virtual_facts

# Generated at 2022-06-13 04:11:19.017583
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual(None)
    assert isinstance(netbsd_virtual, NetBSDVirtual)


# Generated at 2022-06-13 04:11:20.825878
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd = NetBSDVirtual({}, None)
    assert netbsd.platform == 'NetBSD'


# Generated at 2022-06-13 04:11:24.570078
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    netbsd_virtual_collector = NetBSDVirtualCollector()
    assert netbsd_virtual_collector._fact_class is NetBSDVirtual
    assert netbsd_virtual_collector._platform == "NetBSD"

# Generated at 2022-06-13 04:11:30.646677
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    os_platform = 'NetBSD'
    os_version = '9.0'
    os_family = 'BSD'
    os_major_version = '9'
    collector = NetBSDVirtualCollector(os_platform, os_version, os_family, os_major_version)
    assert collector._platform == os_platform
    assert collector._platform_version == os_version
    assert collector._platform_family == os_family
    assert collector._platform_major_version == os_major_version
    assert collector._fact_class._platform == os_platform

# Generated at 2022-06-13 04:11:38.656690
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    VirtualCollector.test_virtual_collector(NetBSDVirtual())

# Generated at 2022-06-13 04:11:50.755302
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    def _get_sysctl_check_output(self, facts, sysctl_fact, default=''):
        return {
            'machdep.dmi.system-product': 'KVM',
            'machdep.dmi.system-vendor': 'QEMU',
            'machdep.hypervisor': 'KVM'
        }.get(sysctl_fact, default)

    NetBSDVirtual.detect_virt_product = _get_sysctl_check_output
    NetBSDVirtual.detect_virt_vendor = _get_sysctl_check_output

    data = NetBSDVirtual().get_virtual_facts()
    assert data['virtualization_type'] == 'kvm'
    assert data['virtualization_role'] == 'guest'

# Generated at 2022-06-13 04:11:52.128616
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    facts = NetBSDVirtualCollector()
    assert facts is not None, 'Unable to create instance of NetBSDVirtualCollector'

# Generated at 2022-06-13 04:11:54.656963
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    obj = NetBSDVirtualCollector()
    assert obj._platform == 'NetBSD'
    assert obj._fact_class.platform == 'NetBSD'

# Generated at 2022-06-13 04:11:57.031703
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():

    virtual_facts = NetBSDVirtual(module=None).get_virtual_facts()

    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts

# Generated at 2022-06-13 04:11:59.706254
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual_facts = NetBSDVirtual({}, {}, {}, {}, {})
    assert virtual_facts.platform == 'NetBSD'
    assert virtual_facts.get_virtual_facts() == {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set(),
        'virtualization_product_name': '',
        'virtualization_product_version': '',
    }

# Generated at 2022-06-13 04:12:11.318079
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    # Test with existing sysctl machdep.dmi.system-vendor
    guest_tech = set()
    host_tech = set()
    virtual_facts = {
        'machdep.dmi.system-product': 'VirtualBox',
        'machdep.dmi.system-vendor': 'innotek GmbH'
    }
    test = NetBSDVirtual(virtual_facts)
    (virtual_product_facts, virtual_vendor_facts) = test.get_virtual_facts()
    guest_tech.update(virtual_product_facts['virtualization_tech_guest'])
    host_tech.update(virtual_product_facts['virtualization_tech_host'])
    guest_tech.update(virtual_vendor_facts['virtualization_tech_guest'])

# Generated at 2022-06-13 04:12:15.646854
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    netbsd_get_virtual_facts = {
        'virtualization_type': 'xen',
        'virtualization_role': 'guest',
        'virtualization_tech_guest': {'xen'},
    }

    netbsd_virtual = NetBSDVirtual(None)

    # Return virtual facts dictionary
    assert netbsd_get_virtual_facts == netbsd_virtual.get_virtual_facts()

# Generated at 2022-06-13 04:12:17.671776
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual_facts = NetBSDVirtual({}).get_virtual_facts()
    assert 'virtualization_type' in virtual_facts



# Generated at 2022-06-13 04:12:18.856147
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual = NetBSDVirtual()
    assert virtual.platform == 'NetBSD'

# Generated at 2022-06-13 04:12:35.047158
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    fact_obj = NetBSDVirtual()
    result = fact_obj.get_virtual_facts()
    assert 'virtualization_type' in result

# Generated at 2022-06-13 04:12:36.703576
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    v = NetBSDVirtual()
    assert v.platform == 'NetBSD'

# Generated at 2022-06-13 04:12:40.745169
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    virtual_collector = NetBSDVirtualCollector()
    assert virtual_collector.platform == 'NetBSD'
    assert virtual_collector._fact_class._platform == 'NetBSD'
    assert virtual_collector._fact_class._fact_class is None

# Generated at 2022-06-13 04:12:41.792659
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    assert NetBSDVirtualCollector != None

# Generated at 2022-06-13 04:12:51.153884
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    mock_sysctl_file = '''
machdep.dmi.system-product = "PowerEdge C6320"
machdep.dmi.system-vendor = "Dell Inc."
machdep.hypervisor = "KVM"
'''
    virtual_facts = NetBSDVirtual(sysctl_file=mock_sysctl_file).get_virtual_facts()

    assert virtual_facts['virtualization_type'] == 'kvm'
    assert virtual_facts['virtualization_role'] == 'guest'
    assert virtual_facts['virtualization_tech_guest'] == {'kvm'}
    assert virtual_facts['virtualization_tech_host'] == {'kvm'}



# Generated at 2022-06-13 04:12:54.827998
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual = NetBSDVirtual()
    virtual_facts = virtual.get_virtual_facts()
    assert('virtualization_type' in virtual_facts)
    assert('virtualization_role' in virtual_facts)
    assert('virtualization_tech_guest' in virtual_facts)
    assert('virtualization_tech_host' in virtual_facts)

# Generated at 2022-06-13 04:12:56.678258
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    v = NetBSDVirtual()
    assert v.get_virtual_facts()
    assert v.platform == 'NetBSD'


# Generated at 2022-06-13 04:13:02.169925
# Unit test for method get_virtual_facts of class NetBSDVirtual

# Generated at 2022-06-13 04:13:03.614218
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual = NetBSDVirtual()
    assert virtual.platform == 'NetBSD'


# Generated at 2022-06-13 04:13:06.706101
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual({'module': {}})
    assert netbsd_virtual.sysctl_exists('machdep.dmi.system-product')

# Generated at 2022-06-13 04:13:22.296233
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual(None)
    assert isinstance(netbsd_virtual, NetBSDVirtual)


# Generated at 2022-06-13 04:13:24.470790
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual = NetBSDVirtual()
    assert virtual._platform == "NetBSD"
    assert virtual._fact_class == NetBSDVirtual


# Generated at 2022-06-13 04:13:26.224601
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual("cmdline")
    assert netbsd_virtual is not None

# Generated at 2022-06-13 04:13:29.152301
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():

    virtual_facts = NetBSDVirtual(None).get_virtual_facts()

    # Test an attribute
    assert isinstance(virtual_facts['virtualization_type'], str)

# Generated at 2022-06-13 04:13:35.449898
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd = NetBSDVirtual()
    assert netbsd.platform == 'NetBSD'
    assert netbsd.guest_facts() == {}
    assert netbsd.host_facts() == {}
    assert netbsd.get_virtual_facts() == {}

    netbsd = NetBSDVirtual(module=None)
    assert netbsd.platform == 'NetBSD'
    assert netbsd.guest_facts() == {}
    assert netbsd.host_facts() == {}
    assert netbsd.get_virtual_facts() == {}


# Generated at 2022-06-13 04:13:40.625454
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual_facts = NetBSDVirtual().get_virtual_facts()
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts

# Generated at 2022-06-13 04:13:43.619573
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    assert NetBSDVirtualCollector._platform == 'NetBSD'
    assert NetBSDVirtualCollector._fact_class == NetBSDVirtual
    assert isinstance(NetBSDVirtualCollector()._collect_platform_subset(), dict)

# Generated at 2022-06-13 04:13:49.716656
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    """
    Test cases for get_virtual_facts of NetBSDVirtual class
    """

    _open = open

    def open(path, mode='r'):
        if path == '/dev/xencons':
            raise IOError
        else:
            return _open(path, mode)

    module = type('os', (object,), {'open': open})()

    netbsd_virtual = NetBSDVirtual(module=module)

    # Test case: No virtualization, no hypervisor
    # Result: virtualization_type should be empty and
    # virtualization_tech_guest and virtualization_tech_host should be empty set

# Generated at 2022-06-13 04:13:59.623053
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    # Return values for 'sysctl -n ...'
    sysctl_return_values = {
        'machdep.dmi.system-product': 'VirtualBox',
        'machdep.dmi.system-vendor': 'innotek GmbH',
        'machdep.hypervisor': '',
    }

    # Return values for os.path.exists()
    os_path_exists = {
        '/dev/xencons': False,
    }

    fact_collector = NetBSDVirtualCollector(sysctl_return_values=sysctl_return_values, os_path_exists=os_path_exists)
    virtual_facts = fact_collector.collect()

    assert virtual_facts['virtualization_type'] == 'virtualbox'

# Generated at 2022-06-13 04:14:02.856641
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():

    virtual_facts = NetBSDVirtual().get_virtual_facts()

    # Test the virtual_facts
    assert virtual_facts['virtualization_type'] == 'xen'

# Generated at 2022-06-13 04:14:36.334116
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    with open('/proc/mounts', 'r') as f:
        assert NetBSDVirtual(f.read()).populate() is not None

# Generated at 2022-06-13 04:14:44.739492
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual_test_cases = dict(
        NetBSDVirtual=dict(
            input=dict(),
            output=dict(
                virtualization_type='',
                virtualization_role='',
                virtualization_system='',
                virtualization_hypervisor='',
                virtualization_tech_guest=set(),
                virtualization_tech_host=set()
            )
        )
    )

    for test_case, expected_result in netbsd_virtual_test_cases.items():
        # Unit test for constructor
        ins = NetBSDVirtual(expected_result['input'])

        # Check virtualization facts
        assert ins.get_virtual_facts() == expected_result['output']



# Generated at 2022-06-13 04:14:47.795862
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    try:
        NetBSDVirtualCollector()
    except Exception as e:
        assert type(e) == AssertionError

# Generated at 2022-06-13 04:14:49.134982
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    assert issubclass(NetBSDVirtualCollector, VirtualCollector)


# Generated at 2022-06-13 04:14:51.854206
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    c = NetBSDVirtualCollector()
    assert c.platform == 'NetBSD'
    assert c.fact_class == NetBSDVirtual

# Generated at 2022-06-13 04:14:54.789526
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    facts = NetBSDVirtual().get_virtual_facts()
    assert len(facts['virtualization_tech_guest']) >= 0
    assert len(facts['virtualization_tech_host']) >= 0
    assert facts['virtualization_type']

# Generated at 2022-06-13 04:14:55.947826
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():

    this_class = NetBSDVirtual('')
    assert this_class


# Generated at 2022-06-13 04:14:57.661219
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual()
    assert netbsd_virtual.platform == 'NetBSD'

# Generated at 2022-06-13 04:14:59.913885
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    c = NetBSDVirtualCollector()
    assert c.platform == 'NetBSD'
    assert c.fact_class == NetBSDVirtual

# Generated at 2022-06-13 04:15:01.902346
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual = NetBSDVirtual()
    assert virtual.platform == 'NetBSD'

# Generated at 2022-06-13 04:16:16.466024
# Unit test for constructor of class NetBSDVirtual

# Generated at 2022-06-13 04:16:18.724537
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virt = NetBSDVirtual()
    assert virt.platform == "NetBSD"


# Generated at 2022-06-13 04:16:24.546632
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    netbsd_virtual_facts = NetBSDVirtual()
    netbsd_virtual_facts.read_sysctl_facts = lambda x: {'machdep.dmi.system-product': 'OpenStack Compute',
                                                        'machdep.dmi.system-vendor': 'OpenStack',
                                                        'machdep.hypervisor': 'OpenStack'}
    assert 'virtualization_role' in netbsd_virtual_facts.get_virtual_facts()

# Generated at 2022-06-13 04:16:28.292278
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    facts = NetBSDVirtual().get_virtual_facts()
    assert 'virtualization_role' in facts
    assert 'virtualization_type' in facts
    assert 'virtualization_tech_guest' in facts
    assert 'virtualization_tech_host' in facts

# Generated at 2022-06-13 04:16:30.213430
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual(None, None, None)
    assert netbsd_virtual.get_virtual_facts() is not None

# Generated at 2022-06-13 04:16:37.139023
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    netbsd_virtual_facts = NetBSDVirtual()
    virtual_facts = netbsd_virtual_facts.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''
    assert virtual_facts['virtualization_system'] == ''
    assert virtual_facts['virtualization_product'] == ''
    assert virtual_facts['virtualization_tech_guest'] == set()
    assert virtual_facts['virtualization_tech_host'] == set()


# Generated at 2022-06-13 04:16:38.221348
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual = NetBSDVirtual()
    assert virtual.platform == 'NetBSD'

# Generated at 2022-06-13 04:16:44.664410
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    """Test get_virtual_facts method of NetBSDVirtual"""


# Generated at 2022-06-13 04:16:46.365680
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    c = NetBSDVirtualCollector()
    assert c is not None

# Generated at 2022-06-13 04:16:48.110212
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    nv = NetBSDVirtual()
    assert nv.platform == 'NetBSD'


# Generated at 2022-06-13 04:19:31.951784
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual(context_wrap())
    netbsd_virtual_facts = netbsd_virtual.get_virtual_facts()
    assert netbsd_virtual_facts['virtualization_type'] == 'xen'
    assert netbsd_virtual_facts['virtualization_role'] == 'guest'
    assert 'xen' in netbsd_virtual_facts['virtualization_tech_guest']
    assert 'xen' in netbsd_virtual_facts['virtualization_tech_host']
    assert netbsd_virtual_facts['virtualization_product'] == 'HVM domU'


# Generated at 2022-06-13 04:19:36.911123
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual_facts = NetBSDVirtual().get_virtual_facts()
    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''
    assert not virtual_facts['virtualization_tech_guest']
    assert not virtual_facts['virtualization_tech_host']

# Generated at 2022-06-13 04:19:38.612400
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    instance = NetBSDVirtualCollector()
    assert isinstance(instance, NetBSDVirtual) is True

# Generated at 2022-06-13 04:19:42.599000
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    facts = NetBSDVirtual().get_virtual_facts()
    assert 'virtualization_type' in facts
    assert 'virtualization_role' in facts
    assert 'virtualization_tech_guest' in facts
    assert 'virtualization_tech_host' in facts
    assert 'virtualization_product_name' in facts
    assert 'virtualization_product_version' in facts
    assert 'virtualization_product_serial' in facts

# Generated at 2022-06-13 04:19:43.854335
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd = NetBSDVirtual()
    assert netbsd.platform == "NetBSD"


# Generated at 2022-06-13 04:19:44.997173
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    v = NetBSDVirtual({})
    assert v._platform == 'NetBSD'
    assert v._fact_class == NetBSDVirtual


# Generated at 2022-06-13 04:19:47.734039
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    assert NetBSDVirtual()



# Generated at 2022-06-13 04:19:54.862421
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual = NetBSDVirtual()
    result = virtual.get_virtual_facts()
    assert result['virtualization_type'] == ''
    assert result['virtualization_role'] == ''

    # Test case for guest
    virtual.facts['machdep.dmi.system-product'] = 'VirtualBox'
    result = virtual.get_virtual_facts()
    assert result['virtualization_type'] == 'virtualbox'
    assert result['virtualization_role'] == 'guest'

    # Test case for host
    virtual.facts['machdep.dmi.system-product'] = 'VMWare Virtual Platform'
    result = virtual.get_virtual_facts()
    assert result['virtualization_type'] == 'vmware'
    assert result['virtualization_role'] == 'host'

    # Test case for guest
    virtual.facts