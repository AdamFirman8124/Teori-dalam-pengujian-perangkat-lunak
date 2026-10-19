

# Generated at 2022-06-13 04:09:50.942811
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    assert NetBSDVirtual().platform == 'NetBSD'


# Generated at 2022-06-13 04:09:53.441198
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual = NetBSDVirtual()
    assert virtual.platform == 'NetBSD'


# Generated at 2022-06-13 04:10:00.047693
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    netbsd_virtual_fact = NetBSDVirtual()
    virtual_facts = netbsd_virtual_fact.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'xen'
    assert virtual_facts['virtualization_type'] != 'kvm'
    assert virtual_facts['virtualization_role'] == 'guest'
    assert virtual_facts['virtualization_role'] != 'host'
    assert 'xen' in virtual_facts['virtualization_tech_guest']
    assert 'xen' not in virtual_facts['virtualization_tech_host']
    assert 'kvm' not in virtual_facts['virtualization_tech_guest']
    assert 'kvm' not in virtual_facts['virtualization_tech_host']

# Generated at 2022-06-13 04:10:09.743172
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    fact_data = dict()
    fact_data['kernel'] = 'NetBSD'
    fact_data['system'] = dict()
    fact_data['system']['product_name'] = 'VMware Virtual Platform'
    fact_data['system']['product_version'] = 'None'

    expected_virtual_facts = dict()
    expected_virtual_facts['virtualization_type'] = 'VMware'
    expected_virtual_facts['virtualization_role'] = 'guest'
    expected_virtual_facts['virtualization_tech_guest'] = set(['vmware'])
    expected_virtual_facts['virtualization_tech_host'] = set(['vmware'])

    virtual_collector = NetBSDVirtualCollector(fact_data)
    virtual_facts = virtual_collector._fact_class().get_virtual_

# Generated at 2022-06-13 04:10:15.855509
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.netbsd import NetBSDVirtual

    netbsd_virtual_sysctl = NetBSDVirtual(dict())
    virtual_facts = netbsd_virtual_sysctl.get_virtual_facts()

    attrs_to_test = set(['virtualization_type', 'virtualization_role', 'virtualization_tech_guest', 'virtualization_tech_host'])
    assert all(attr in virtual_facts for attr in attrs_to_test)

# Generated at 2022-06-13 04:10:28.375944
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    # Required for NetBSDVirtualCollector.detect_virt_vendor()
    def get_sysctl_hw_vendor(sysctl_hw_name):
        """get_sysctl_hw_name mock

        This method is used by the "detect_virt_vendor" method.
        """
        if sysctl_hw_name == 'machdep.dmi.system-vendor':
            return 'OpenBSD'
        if sysctl_hw_name == 'machdep.hypervisor':
            return 'None'
        if sysctl_hw_name == 'machdep.dmi.system-product':
            return 'OpenBSD'
        return ''

    # Required for NetBSDVirtualCollector.detect_virt_product()

# Generated at 2022-06-13 04:10:32.331904
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    netbsd_virtual_collector_obj = NetBSDVirtualCollector()
    assert netbsd_virtual_collector_obj._fact_class == NetBSDVirtual
    assert netbsd_virtual_collector_obj._platform == 'NetBSD'

# Generated at 2022-06-13 04:10:37.279382
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual_collector = NetBSDVirtualCollector()
    virtual_facts = virtual_collector._get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'xen', 'The virtualization_type set by NetBSDVirtual is not equal to xen'
    assert virtual_facts['virtualization_role'] == 'guest', 'The virtualization_role set by NetBSDVirtual is not equal to guest'

# Generated at 2022-06-13 04:10:38.462969
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    v = NetBSDVirtual(None)
    assert v.platform == 'NetBSD'

# Generated at 2022-06-13 04:10:44.359488
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual_facts = NetBSDVirtual().get_virtual_facts()
    assert virtual_facts is not None
    assert virtual_facts['virtualization_type'] == "xen"
    assert virtual_facts['virtualization_role'] == "guest"
    assert virtual_facts['virtualization_tech_host'] == {"xen"}
    assert virtual_facts['virtualization_tech_guest'] == {"xen"}


# Generated at 2022-06-13 04:10:51.792091
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual_facts = NetBSDVirtual({}).get_virtual_facts()
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_enabled' in virtual_facts

# Generated at 2022-06-13 04:10:53.726820
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    x = NetBSDVirtualCollector()
    assert x._platform == 'NetBSD'
    assert x._fact_class == NetBSDVirtual


# Generated at 2022-06-13 04:10:55.923593
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    netbsd_collector = NetBSDVirtualCollector()
    assert netbsd_collector.platform == 'NetBSD'


# Generated at 2022-06-13 04:11:02.813361
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual()
    assert netbsd_virtual.platform == 'NetBSD'
    assert netbsd_virtual._sysctl_platform == 'NetBSD'
    assert netbsd_virtual._sysctl_virt_type_map == {
        'bhyve': 'bhyve',
        '4.1-5.1': 'kvm',
        '4.2-5.2': 'kvm',
        '6.0': 'kvm'
    }

# Generated at 2022-06-13 04:11:12.858619
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():

    # Create an instance of NetBSDVirtual
    netbsd_virt = NetBSDVirtual()

    # Test the virtual_facts dictionary returned by the
    # get_virtual_facts method
    netbsd_virtual_facts = netbsd_virt.get_virtual_facts()
    assert 'virtualization_type' in netbsd_virtual_facts
    assert 'virtualization_role' in netbsd_virtual_facts
    assert 'virtualization_full_role' in netbsd_virtual_facts
    assert 'virtualization_tech_guest' in netbsd_virtual_facts
    assert 'virtualization_tech_host' in netbsd_virtual_facts

# Generated at 2022-06-13 04:11:13.705731
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    NetBSDVirtualCollector()

# Generated at 2022-06-13 04:11:18.066920
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    vc = NetBSDVirtualCollector()
    assert vc._fact_class() is not None
    assert vc._platform == 'NetBSD'

# Generated at 2022-06-13 04:11:18.781959
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    NetBSDVirtualCollector()

# Generated at 2022-06-13 04:11:29.133946
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    # Case 1: No virtualization
    virt_product_facts = {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_product': '',
        'virtualization_version': '',
        'virtualization_tech_host': set(),
        'virtualization_tech_guest': set()
    }
    with open('/proc/cpuinfo', 'r') as cpuinfo:
        cpuinfo_data = cpuinfo.read()
    with open('/proc/self/status', 'r') as status:
        status_data = status.read()
    for data in [cpuinfo_data, status_data]:
        virtual = NetBSDVirtual()
        virtual.collect(data, '/proc/cpuinfo')
        assert virt_product_facts == virtual.get_virtual_facts()

   

# Generated at 2022-06-13 04:11:37.000483
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    v = NetBSDVirtual()
    f = v.get_virtual_facts()
    assert 'virtualization_type' in f
    assert 'virtualization_role' in f
    assert 'virtualization_tech_guest' in f
    assert 'virtualization_tech_host' in f
    assert 'virtualization_product_facts' in f
    assert 'virtualization_vendor_facts' in f
    assert 'virtualization_product' in f
    assert 'virtualization_vendor' in f

# Generated at 2022-06-13 04:11:45.931483
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    assert NetBSDVirtualCollector._platform == 'NetBSD'
    assert NetBSDVirtualCollector._fact_class == NetBSDVirtual


# Generated at 2022-06-13 04:11:51.276035
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    # Make an instance of NetBSDVirtual and test the output of method get_virtual_facts()
    facts = NetBSDVirtual()
    result = facts.get_virtual_facts()
    assert result['virtualization_type'] == 'vmware'
    assert result['virtualization_role'] == 'guest'
    assert result['virtualization_tech_guest'] == set(['vmware', 'kvm'])
    assert result['virtualization_tech_host'] == set(['vmware', 'kvm'])

# Generated at 2022-06-13 04:11:52.056263
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    return NetBSDVirtual({})


# Generated at 2022-06-13 04:11:55.321135
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    virtual_collector_object = NetBSDVirtualCollector()
    assert isinstance(virtual_collector_object._fact_class, NetBSDVirtual)
    assert virtual_collector_object._platform == 'NetBSD'

# Generated at 2022-06-13 04:11:58.802286
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual_facts = NetBSDVirtual()
    assert netbsd_virtual_facts.get_virtual_facts() == {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set()
    }

# Generated at 2022-06-13 04:12:00.938698
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd = NetBSDVirtual()
    assert netbsd.platform == 'NetBSD'


# Generated at 2022-06-13 04:12:02.152581
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    NetBSDVirtualCollector().get_virtual_facts()

# Generated at 2022-06-13 04:12:07.802242
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual_facts = NetBSDVirtual().get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'xen'
    assert virtual_facts['virtualization_role'] == 'guest'
    assert 'xen' in virtual_facts['virtualization_tech_guest']
    assert 'xen' in virtual_facts['virtualization_tech_host']

# Generated at 2022-06-13 04:12:12.671230
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual_facts = NetBSDVirtual()

    # Some values are hardcoded because we only need to check if
    # the key is present in the dict returned.
    assert 'virtualization_type' in virtual_facts.get_virtual_facts()
    assert 'virtualization_role' in virtual_facts.get_virtual_facts()


# Generated at 2022-06-13 04:12:15.807366
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual_fact = NetBSDVirtual('NetBSD')
    assert virtual_fact.platform == 'NetBSD'
    assert virtual_fact.get_virtual_facts() == {}

# Generated at 2022-06-13 04:12:33.383467
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    facts = dict()
    virtual = NetBSDVirtual(module=None)
    facts = virtual.get_virtual_facts()
    assert facts['virtualization_type'] == 'xen'
    assert facts['virtualization_role'] == 'guest'
    assert isinstance(facts['virtualization_tech_guest'], set)
    assert isinstance(facts['virtualization_tech_host'], set)
    assert 'xen' in facts['virtualization_tech_guest']

# Generated at 2022-06-13 04:12:36.645262
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual()
    assert netbsd_virtual is not None
    assert netbsd_virtual.platform == 'NetBSD'

# Generated at 2022-06-13 04:12:39.790805
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    netbsd_virtual = NetBSDVirtualCollector()
    assert netbsd_virtual.platform == "NetBSD"
    assert netbsd_virtual._fact_class == NetBSDVirtual

# Generated at 2022-06-13 04:12:41.987626
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    nv = NetBSDVirtualCollector()
    assert nv.platform == 'NetBSD'
    assert nv.fact_class == 'NetBSDVirtual'

# Generated at 2022-06-13 04:12:43.999233
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual({})

    assert netbsd_virtual is not None

# Generated at 2022-06-13 04:12:47.910171
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd = NetBSDVirtual({'ansible_facts':{}})
    assert netbsd.virtualization_type == ''
    assert netbsd.virtualization_role == ''
    assert netbsd.virtualization_technology_host == set()
    assert netbsd.virtualization_technology_guest == set()

# Generated at 2022-06-13 04:12:51.488383
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual(module=None)
    assert netbsd_virtual.platform == "NetBSD"
    assert netbsd_virtual.virtual == "NetBSD"


# Generated at 2022-06-13 04:12:55.588823
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virt = NetBSDVirtual()
    assert virt.get_virtual_facts() == {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set(),
    }

# Generated at 2022-06-13 04:13:01.620645
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    #############################################
    # Return empty if no machdep.dmi.system-product or machdep.hypervisor
    # is found and no xen device is found
    #############################################
    open_name = 'ansible.module_utils.facts.virtual.netbsd.open'
    with mock.patch(open_name, mock.mock_open(read_data="")):
        virtual = NetBSDVirtual({})
        virtual_facts = virtual.get_virtual_facts()
        # Assert that result is empty
        assert {} == virtual_facts

    #############################################
    # Test hypervisor prefix
    #############################################
    open_name = 'ansible.module_utils.facts.virtual.netbsd.open'

# Generated at 2022-06-13 04:13:03.382158
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    netbsd_virtual_collector = NetBSDVirtualCollector()
    assert netbsd_virtual_collector is not None


# Generated at 2022-06-13 04:13:30.249355
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual()
    assert netbsd_virtual is not None


# Generated at 2022-06-13 04:13:31.205379
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    assert NetBSDVirtualCollector.__doc__ is not None

# Generated at 2022-06-13 04:13:34.066119
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    netbsd_virtual_collector = NetBSDVirtualCollector()
    assert netbsd_virtual_collector._fact_class is NetBSDVirtual
    assert netbsd_virtual_collector._platform is 'NetBSD'


# Generated at 2022-06-13 04:13:36.818843
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    x = NetBSDVirtualCollector()
    assert x


# Generated at 2022-06-13 04:13:46.420138
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    from ansible.module_utils.facts import FactCollector

    virt = NetBSDVirtual({})

    # Test 1: No xend

    # Test 2: No machdep.dmi.system-vendor
    file_detect_virt_vendor_sysctl_mock_value = '''
    machdep.hypervisor.name: Sun VirtualBox
    machdep.hypervisor.vendor: innotek GmbH
    machdep.hypervisor.version: 1.2
    '''

    file_detect_virt_product_sysctl_mock_value = ''

    facts = FactCollector({}, {}, virt._platform).collect(
        gather_subset='all',
        filter_spec=dict(),
    )

    assert 'virtualization_type' in facts
    assert 'virtualization_role' in facts
   

# Generated at 2022-06-13 04:13:52.446921
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    netbsd_virtual_facts = NetBSDVirtualCollector().get_virtual_facts()
    assert 'virtualization_type' in netbsd_virtual_facts
    assert 'virtualization_role' in netbsd_virtual_facts
    assert 'virtualization_tech_guest' in netbsd_virtual_facts
    assert 'virtualization_tech_host' in netbsd_virtual_facts

# Generated at 2022-06-13 04:13:54.031158
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual()
    assert netbsd_virtual.platform == 'NetBSD'

# Generated at 2022-06-13 04:13:56.753788
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd = NetBSDVirtual()
    assert netbsd is not None
    result = netbsd.collect()
    assert 'virtualization_type' in result

# Generated at 2022-06-13 04:13:58.580725
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    nbv = NetBSDVirtual(None)
    assert nbv is not None
    assert nbv.platform == 'NetBSD'


# Generated at 2022-06-13 04:14:01.206228
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual_facts = NetBSDVirtual()

    # collects facts
    assert isinstance(virtual_facts.collect(), dict)


# Generated at 2022-06-13 04:15:07.524483
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual_facts = {}
    with open('/proc/cpuinfo', 'r') as f:
        for line in f:
            if line.strip():
                if ':' in line:
                    key, value = line.split(':', 1)
                    virtual_facts[key.strip()] = value.strip()
                else:
                    virtual_facts[line.strip()] = ''
    virtual_facts['kernel_osrelease'] = '6.99.2'
    nv = NetBSDVirtual(virtual_facts=virtual_facts)
    assert nv.get_virtual_facts() == {'virtualization_type': 'xen', 'virtualization_role': 'guest', 'virtualization_tech_host': set(), 'virtualization_tech_guest': set(['xen'])}

# Generated at 2022-06-13 04:15:09.906636
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    v = NetBSDVirtual()
    assert(v.platform == 'NetBSD')
    assert(v.get_virtual_facts() is not None)

# Generated at 2022-06-13 04:15:12.759771
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    check = NetBSDVirtualCollector()
    assert check._platform == 'NetBSD'
    assert check._fact_class == NetBSDVirtual

# Generated at 2022-06-13 04:15:14.472679
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    facts = NetBSDVirtual()
    assert facts.get_virtual_facts()['virtualization_type'] == ''
    assert facts.get_virtual_facts()['virtualization_role'] == ''

# Generated at 2022-06-13 04:15:25.077401
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    test_fixture = {
        'machdep.dmi.system-product': 'VMware Virtual Platform',
        'machdep.dmi.system-vendor': 'VMware Inc.',
        'machdep.hypervisor': 'VMware, Inc.',
    }

    netbsd_virtual = NetBSDVirtual(module=None, additional_facts=test_fixture)
    virtual_facts = netbsd_virtual.get_virtual_facts()

    assert virtual_facts['virtualization_type'] == 'VMware'
    assert virtual_facts['virtualization_role'] == 'guest'
    assert virtual_facts['virtualization_tech_guest'] == set(['vmware'])
    assert virtual_facts['virtualization_tech_host'] == set(['vmware'])

# Generated at 2022-06-13 04:15:27.487745
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtualObject = NetBSDVirtual()
    assert virtualObject is not None

# Generated at 2022-06-13 04:15:30.488910
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd = NetBSDVirtual()
    assert netbsd.platform == 'NetBSD'
    assert netbsd.get_virtual_facts() == dict(virtualization_type=None, virtualization_role=None)

# Generated at 2022-06-13 04:15:32.936399
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    # NetBSDVirtualCollector(module, [sysctl_facts=None])
    NetBSDVirtualCollector(None)

# Generated at 2022-06-13 04:15:34.190676
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual = NetBSDVirtual({})
    assert virtual is not None

# Generated at 2022-06-13 04:15:42.165946
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual = NetBSDVirtual()
    virtual_facts = virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''
    assert virtual_facts['virtualization_system'] == ''
    assert virtual_facts['virtualization_uuid'] == ''
    assert virtual_facts['virtualization_virt_type'] == ''
    assert virtual_facts['virtualization_product_name'] == ''
    assert virtual_facts['virtualization_product_version'] == ''
    assert virtual_facts['virtualization_host_system'] == ''
    assert virtual_facts['virtualization_host_uuid'] == ''
    assert virtual_facts['virtualization_host_name'] == ''
    assert virtual_facts['virtualization_host_date'] == ''

# Generated at 2022-06-13 04:18:13.192053
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    """
     Test for NetBSDVirtual class function get_virtual_facts
     This test requires the following commands to exist:
     - sysctl -a
    """
    os_facts = {
        'kernel': 'NetBSD',
    }

    # Test with Docker
    sysctl_output = {
        'machdep.dmi.system-product': 'Docker',
        'machdep.dmi.system-vendor': 'Docker',
    }

    virtual_facts = {}
    virtual_facts['os_facts'] = os_facts
    virtual_facts['sysctl_output'] = sysctl_output

# Generated at 2022-06-13 04:18:13.862258
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    NetBSDVirtualCollector()

# Generated at 2022-06-13 04:18:16.751739
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual(None, None)
    assert netbsd_virtual.platform == 'NetBSD'


# Generated at 2022-06-13 04:18:23.526434
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    # Import module and create instance of NetBSDVirtual
    from ansible.module_utils.facts.virtual import NetBSDVirtual
    virt_inst = NetBSDVirtual()

    # Create mock of sysctl_output()
    import mock
    sysctl_output_mock = mock.Mock(return_value='Dell Inc. \
        PowerEdge R720xd \
        /0YJPT4/CN7060491K0013/ \
        ')
    with mock.patch.multiple('ansible.module_utils.facts.virtual.netbsd',
            sysctl_output=sysctl_output_mock):
        virtual_facts_output = virt_inst.get_virtual_facts()
        assert virtual_facts_output['virtualization_type'] == 'kvm'

# Generated at 2022-06-13 04:18:30.613074
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual()
    assert netbsd_virtual.platform == 'NetBSD'
    assert not netbsd_virtual.is_linux()
    assert netbsd_virtual.is_netbsd()
    assert not netbsd_virtual.is_openbsd()
    assert not netbsd_virtual.is_aix()
    assert not netbsd_virtual.is_freebsd()
    assert not netbsd_virtual.is_solaris()
    assert not netbsd_virtual.is_windows()


# Generated at 2022-06-13 04:18:32.459729
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual()

    # Valid values
    assert netbsd_virtual._platform == 'NetBSD'
    assert netbsd_virtual._fact_class == NetBSDVirtual


# Generated at 2022-06-13 04:18:43.575741
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    facts = {
        'kernel': 'NetBSD',
        'virtualization_sysctl_facts': {
            'machdep.dmi.system-vendor': 'IBM',
            'machdep.hypervisor': 'Foo Vendor'
        },
    }

    # Test IBM as system vendor
    d = NetBSDVirtual(facts)
    virtual_facts = d.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'kvm'
    assert virtual_facts['virtualization_role'] == 'host'
    assert 'host_machine' in virtual_facts
    assert 'product_name' in virtual_facts
    assert 'product_version' in virtual_facts

    # Test Foo Vendor as hypervisor

# Generated at 2022-06-13 04:18:48.023573
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    # Create collector
    collector = NetBSDVirtualCollector()
    # Create an instance of the Virtual class using the collector
    virtual = NetBSDVirtual(collector=collector)
    assert virtual.get_virtual_facts() == {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_technologies_guest': set(),
        'virtualization_technologies_host': set()
    }

# Generated at 2022-06-13 04:18:50.431697
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    c = NetBSDVirtual()
    c.collect()
    assert c.get_virtual_facts() == {'virtualization_type': '', 'virtualization_role': '', 'virtualization_tech_guest': set(), 'virtualization_tech_host': set()}

# Generated at 2022-06-13 04:18:55.252065
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    my_data = {
        'machdep.dmi.system-vendor': 'LENOVO',
        'machdep.dmi.system-product': '30880F8',
        'machdep.hypervisor': 'VMware'
    }

    ansible_facts = {}
    for k, v in my_data.items():
        ansible_facts[k] = v

    obj = NetBSDVirtual()
    obj.collect(ansible_facts=ansible_facts)