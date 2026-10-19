

# Generated at 2022-06-13 04:09:53.448249
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    my_NetBSDVirtualObject = NetBSDVirtual()
    my_NetBSDVirtualObject.get_virtual_facts()

# Generated at 2022-06-13 04:09:58.066898
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    facts = NetBSDVirtual().get_virtual_facts()
    assert len(facts) == 4
    assert isinstance(facts['virtualization_type'], str)
    assert isinstance(facts['virtualization_role'], str)
    assert isinstance(facts['virtualization_tech_guest'], set)
    assert isinstance(facts['virtualization_tech_host'], set)

# Generated at 2022-06-13 04:10:06.519003
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    '''Unit test for method get_virtual_facts of class NetBSDVirtual'''

    # Data construct for method get_virtual_facts of class NetBSDVirtual
    netbsd_virtual = NetBSDVirtual()
    expected_result = {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_tech_guest': set([]),
        'virtualization_tech_host': set([])
    }

    # Verification of method get_virtual_facts of class NetBSDVirtual
    result = netbsd_virtual.get_virtual_facts()
    assert result == expected_result

# Generated at 2022-06-13 04:10:10.830269
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():

    # Prepare test
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.facts.virtual.netbsd import NetBSDVirtual
    fake_facts = NetBSDVirtual()

    # Test function get_virtual_facts of class NetBSDVirtual
    assert fake_facts.get_virtual_facts() == {
        'virtualization_role': '',
        'virtualization_type': '',
        'virtualization_tech_host': set(),
        'virtualization_tech_guest': set(),
    }

# Generated at 2022-06-13 04:10:12.909833
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    v = NetBSDVirtual()
    assert v.platform == 'NetBSD'
    assert v.collector == NetBSDVirtualCollector


# Generated at 2022-06-13 04:10:19.183465
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virt_collector = NetBSDVirtualCollector()

    assert virt_collector.get_virtual_facts() == {
        'virtualization_role': 'guest',
        'virtualization_type': 'xen',
        'virtualization_technologies_guest': ['xen'],
        'virtualization_technologies_host': ['xen']
    }

# Generated at 2022-06-13 04:10:27.919423
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    test_facts = {}
    test_facts['kernel'] = 'NetBSD'
    netbsd_virtual = NetBSDVirtual({}, test_facts)
    netbsd_virtual.collect()

    # check virtualization_type and virtualization_role
    assert netbsd_virtual.virtual == 'NetBSD'
    assert netbsd_virtual.role == 'guest'

    # check virtualization_tech_guest and virtualization_tech_host
    assert netbsd_virtual.guest == set(['xen'])
    assert netbsd_virtual.host == set()


# Generated at 2022-06-13 04:10:29.488738
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    assert issubclass(NetBSDVirtual, Virtual)


# Generated at 2022-06-13 04:10:31.721348
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd = NetBSDVirtual()
    assert netbsd.platform == 'NetBSD'


# Generated at 2022-06-13 04:10:34.411686
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual_facts_obj = NetBSDVirtual()
    assert netbsd_virtual_facts_obj.platform == 'NetBSD'


# Generated at 2022-06-13 04:10:39.325367
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    netbsdvirtualcollector = NetBSDVirtualCollector()
    assert netbsdvirtualcollector.platform == 'NetBSD'

# Generated at 2022-06-13 04:10:41.142302
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual = NetBSDVirtual({}, {})
    assert virtual._platform == 'NetBSD'

# Generated at 2022-06-13 04:10:52.848682
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    # Test if get_virtual_facts returns correct values
    netbsd_virtual_fakefacts = {'machdep.dmi.system-product': 'VMWare Virtual Platform',
            'machdep.dmi.system-vendor': 'VMware, Inc.',
            'machdep.hypervisor': 'vmware'}

    expected_virtual_facts = {'virtualization_type': 'VMware',
            'virtualization_role': 'guest',
            'virtualization_tech_guest': set(['vmware']),
            'virtualization_tech_host': set(['vmware'])}

    netbsd_virtual_obj = NetBSDVirtual(netbsd_virtual_fakefacts, None)
    virtual_facts = netbsd_virtual_obj.get_virtual_facts()


# Generated at 2022-06-13 04:10:54.422665
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual_facts = VirtualCollector._get_virtual_facts_platform('NetBSD')
    assert virtual_facts is not None

# Generated at 2022-06-13 04:10:56.491482
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    collector = NetBSDVirtualCollector()
    virtual_facts = collector.get_virtual_facts()
    assert virtual_facts

# Generated at 2022-06-13 04:11:05.857021
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    c = NetBSDVirtual()
    c.sysctl_output.append('machdep.hypervisor=BOCHS')
    virtual_facts = c.get_virtual_facts()
    expected_virtual_facts = {
        'virtualization_type': 'xen',
        'virtualization_role': 'guest',
        'virtualization_tech_guest': set(['xen']),
        'virtualization_tech_host': set(['bochs']),
    }
    assert virtual_facts == expected_virtual_facts

    c.sysctl_output[0] = 'machdep.hypervisor=Xen'
    virtual_facts = c.get_virtual_facts()

# Generated at 2022-06-13 04:11:07.774970
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virt = NetBSDVirtual()
    assert virt is not None

# Generated at 2022-06-13 04:11:10.016985
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    nb_virtual = NetBSDVirtual()
    assert nb_virtual.platform == 'NetBSD'


# Generated at 2022-06-13 04:11:11.898689
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    assert NetBSDVirtualCollector._platform == 'NetBSD'
    assert NetBSDVirtualCollector._fact_class == NetBSDVirtual

# Generated at 2022-06-13 04:11:13.466520
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    obj = NetBSDVirtualCollector()
    assert(obj.platform == 'NetBSD')


# Generated at 2022-06-13 04:11:18.648534
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    virtual_collector = NetBSDVirtualCollector()
    assert isinstance(virtual_collector._fact_class, NetBSDVirtual)
    assert virtual_collector._platform == 'NetBSD'

# Generated at 2022-06-13 04:11:20.718311
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    collector = NetBSDVirtualCollector()
    assert collector._platform == 'NetBSD'
    assert collector._fact_class == NetBSDVirtual

# Generated at 2022-06-13 04:11:22.876170
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual({}, {})
    assert netbsd_virtual.platform == 'NetBSD'

# Generated at 2022-06-13 04:11:31.923561
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    # NetBSD with vm.conf file
    fact_mock = VirtualFactMock('NetBSD', 'NetBSDVirtual',
                                conf_file='/etc/vm.conf')

# Generated at 2022-06-13 04:11:34.143890
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    NetBSDVirtualCollector()

# Generated at 2022-06-13 04:11:42.672993
# Unit test for method get_virtual_facts of class NetBSDVirtual

# Generated at 2022-06-13 04:11:45.232222
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    x = NetBSDVirtualCollector()
    assert x._facts['virtualization_type'] == ''

# Generated at 2022-06-13 04:11:46.946970
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    bsd = NetBSDVirtual()
    assert bsd.platform == 'NetBSD'


# Generated at 2022-06-13 04:11:48.211935
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    assert isinstance(NetBSDVirtualCollector(), VirtualCollector)

# Generated at 2022-06-13 04:11:51.120234
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    netbsd = NetBSDVirtualCollector()

# Generated at 2022-06-13 04:12:02.604321
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    netbsd_virtual_instance = NetBSDVirtual()
    virtual_facts = netbsd_virtual_instance.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'xen'
    assert virtual_facts['virtualization_role'] == 'guest'

# Generated at 2022-06-13 04:12:13.476563
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    # Test with no facts
    facts = {}
    expected_result = {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set(),
    }
    v = NetBSDVirtual(facts)
    assert v.get_virtual_facts() == expected_result

    # Test with existing facts
    facts = {
        'virtualization_type': 'existing_type',
        'virtualization_role': 'existing_role',
        'virtualization_tech_guest': set(['existing_guest']),
        'virtualization_tech_host': set(['existing_host']),
    }

# Generated at 2022-06-13 04:12:22.739009
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    test_NetBSDVirtual = NetBSDVirtual()
    # For testing we will be providing the return value of
    # sysctl_all(). The key of the dictionary is the sysctl name
    # and the values are the results. In this test we are providing
    # the sysctl results of Xen and a Physical system.

    # Test scenario 1: Virtualization Role: guest, Xen, Domain-U

# Generated at 2022-06-13 04:12:28.184807
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    netbsd = NetBSDVirtualCollector()
    assert netbsd.platform == "NetBSD"
    assert netbsd.fact_class._platform == "NetBSD"
    assert netbsd.fact_class.platform == "NetBSD"
    assert netbsd._platform == "NetBSD"

# Generated at 2022-06-13 04:12:30.751200
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    # Set up tested class
    tested_class = NetBSDVirtual()

    # Perform the test
    returned_value = tested_class.get_virtual_facts()



# Generated at 2022-06-13 04:12:31.180126
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    NetBSDVirtual()

# Generated at 2022-06-13 04:12:38.686779
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    """Validates the return data in get_virtual_facts()."""
    virtual_obj = NetBSDVirtual()
    virtual_obj.get_virtual_facts()

    assert 'virtualization_type' in virtual_obj.data
    assert 'virtualization_role' in virtual_obj.data
    assert 'virtualization_tech_guest' in virtual_obj.data
    assert 'virtualization_tech_host' in virtual_obj.data

# Generated at 2022-06-13 04:12:41.082179
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    netbsd_virtual_collector = NetBSDVirtualCollector()
    assert(netbsd_virtual_collector.platform == 'NetBSD')

# Generated at 2022-06-13 04:12:45.605376
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    netbsd_virtual_fact = NetBSDVirtual()
    virtual_facts = netbsd_virtual_fact.get_virtual_facts()

    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts

# Generated at 2022-06-13 04:12:48.813528
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    netbsd = NetBSDVirtualCollector()
    assert netbsd.platform == 'NetBSD'
    assert netbsd._platform == 'NetBSD'
    assert netbsd._fact_class == NetBSDVirtual


# Generated at 2022-06-13 04:13:07.261634
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual_facts = NetBSDVirtual()
    virtual_facts.collect()

    assert virtual_facts.virtual_facts['virtualization_type'] == ''
    assert virtual_facts.virtual_facts['virtualization_role'] == ''
    assert virtual_facts.virtual_facts['virtualization_system'] == ''
    assert virtual_facts.virtual_facts['virtualization_product'] == ''
    assert virtual_facts.virtual_facts['virtualization_uuid'] == ''

# Generated at 2022-06-13 04:13:08.903819
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual_obj = NetBSDVirtual()
    assert netbsd_virtual_obj.get_virtual_facts() == {}

# Generated at 2022-06-13 04:13:10.201269
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    collector = NetBSDVirtualCollector()
    assert collector.platform is 'NetBSD'

# Generated at 2022-06-13 04:13:11.946256
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    pass

# Generated at 2022-06-13 04:13:19.902325
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    netbsd_virtual_test_class = NetBSDVirtual({})
    netbsd_virtual_test_class.get_sysctl_info = lambda param: 'Xen' if param == 'machdep.hypervisor' else None
    netbsd_virtual_test_class.get_dmi_info = lambda _: None
    netbsd_virtual_test_class.is_file_exists = lambda _: True

    expected_virtual_facts = dict(
        virtualization_role='guest',
        virtualization_type='xen',
        virtualization_tech_guest={'xen'},
        virtualization_tech_host={'xen'})
    actual_virtual_facts = netbsd_virtual_test_class.get_virtual_facts()
    assert expected_virtual_facts == actual_virtual_facts

# Generated at 2022-06-13 04:13:27.504409
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual = NetBSDVirtual()
    assert virtual._sysctl == '/sbin/sysctl'
    assert virtual._sysctl_machine == 'sysctl -n hw.machine'
    assert virtual._sysctl_system_vendor == 'sysctl -n machdep.dmi.system-vendor'
    assert virtual._sysctl_product_name == 'sysctl -n machdep.dmi.system-product'
    assert virtual._sysctl_hypervisor_vendor == 'sysctl -n machdep.hypervisor'
    assert virtual._sysctl_hypervisor_version == 'sysctl -n machdep.hypervisor.version'

# Generated at 2022-06-13 04:13:30.743913
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    netbsd_virtual_collector = NetBSDVirtualCollector()
    assert netbsd_virtual_collector._platform == 'NetBSD'
    assert netbsd_virtual_collector._fact_class == NetBSDVirtual

# Generated at 2022-06-13 04:13:38.083867
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    NetBSD_virtual_facts = {
        'virtualization_role': 'guest',
        'virtualization_type': 'openvz',
        'virtualization_tech_guest': set(['openvz']),
        'virtualization_tech_host': set(),
    }

    # To test this, we have to set the flag that tells 'machdep.hypervisor'
    # is present.
    VirtualSysctlDetectionMixin._sysctl_sysctlbyname = True
    virtual_facts = NetBSDVirtual().get_virtual_facts()
    assert virtual_facts == NetBSD_virtual_facts

# Generated at 2022-06-13 04:13:39.594807
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    facts = NetBSDVirtual()
    assert facts.platform == 'NetBSD'

# Generated at 2022-06-13 04:13:45.476304
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    # Test if required information is provided
    virtual = NetBSDVirtual()
    assert 'hypervisor_facts' in virtual.provided_facts
    assert 'virtualization_type' in virtual.provided_facts
    assert 'virtualization_role' in virtual.provided_facts
    assert 'virtualization_type_role' in virtual.provided_facts
    assert 'virtualization_tech_guest' in virtual.provided_facts
    assert 'virtualization_tech_host' in virtual.provided_facts

# Generated at 2022-06-13 04:14:24.645257
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    DETECTED_VIRT_PRODUCT_VIRT_VENDOR = \
    {'virtualization_type': '',
     'virtualization_role': '',
     'virtualization_product_name': '',
     'virtualization_product_version': '',
     'virtualization_product_serial': '',
     'virtualization_vendor_name': '',
     'virtualization_vendor_version': '',
     'virtualization_vendor_serial': '',
     'virtualization_product_uuid': '',
     'virtualization_type_role': '',
     'virtualization_tech_guest': set([]),
     'virtualization_tech_host': set([])}


# Generated at 2022-06-13 04:14:26.820005
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual_facts = NetBSDVirtual()
    virtual_facts = netbsd_virtual_facts.get_virtual_facts()
    assert virtual_facts['virtualization_type'] != ''

# Generated at 2022-06-13 04:14:30.591336
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    vm = NetBSDVirtual()
    assert isinstance(vm, NetBSDVirtual)

    vm_facts = vm.get_virtual_facts()
    assert isinstance(vm_facts, dict)
    assert vm_facts['virtualization_type'] == ''
    assert vm_facts['virtualization_role'] == ''
    assert len(vm_facts['virtualization_tech_guest']) == 0
    assert len(vm_facts['virtualization_tech_host']) == 0

# Generated at 2022-06-13 04:14:31.938690
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():

    netbsd_virtual = NetBSDVirtual()

    assert netbsd_virtual.platform == "NetBSD"

# Generated at 2022-06-13 04:14:42.880885
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    sysctl_output = (
        'machdep.xen.cpufreq_min: 0\n'
        'machdep.xen.cpufreq_max: 2500\n'
        'machdep.dmi.system-product: "HVM domU"\n'
        'machdep.hypervisor: xen\n')

    netbsd_virtual = NetBSDVirtual(sysctl_output, None)
    virtual_facts = netbsd_virtual.get_virtual_facts()

    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts

    assert virtual_facts['virtualization_type'] == 'xen'
    assert virtual

# Generated at 2022-06-13 04:14:45.254631
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    facts = NetBSDVirtualCollector()
    assert isinstance(facts, NetBSDVirtualCollector)
    assert isinstance(facts.get_virtual_facts(), dict)

# Generated at 2022-06-13 04:14:52.493060
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.netbsd import NetBSDVirtual
    nbsdv = NetBSDVirtual()
    expected_virtual_facts = dict(
        virtualization_type='xen',
        virtualization_role='guest',
        virtualization_tech_guest={'xen'},
        virtualization_tech_host={'xen'}
    )
    assert nbsdv.get_virtual_facts() == expected_virtual_facts

# Generated at 2022-06-13 04:14:54.405487
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    # Does not need to do anything
    # If any of the fact collection classes need to be tested,
    # it should be done here
    pass

# Generated at 2022-06-13 04:14:55.633258
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual_facts = NetBSDVirtual()
    assert virtual_facts.platform == 'NetBSD'

# Generated at 2022-06-13 04:15:05.979298
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    expected_virtual_facts = {'virtualization_role': 'guest',
                              'virtualization_type': 'xen',
                              'virtualization_tech_guest': {'xen'},
                              'virtualization_tech_host': set()}

    def _get_sysctl_mock(name, default=None):
        # Return values for known sysctl nodes
        sysctl_dict = {'machdep.dmi.system-product':
                       'HVM domU',
                       'machdep.hypervisor':
                       'NetBSD/amd64 dom0'}
        return sysctl_dict.get(name, default)

    def _os_path_exists_mock(path, default=None):
        # Return values for known paths
        path_dict = {'/dev/xencons': True}

# Generated at 2022-06-13 04:16:14.423443
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    nv = NetBSDVirtualCollector()
    assert nv._fact_class is NetBSDVirtual
    assert nv._platform == 'NetBSD'

# Generated at 2022-06-13 04:16:15.732525
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual = NetBSDVirtual({})
    assert virtual.platform == 'NetBSD'


# Generated at 2022-06-13 04:16:25.041954
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    test_obj = NetBSDVirtual()
    assert test_obj
    assert test_obj.platform == 'NetBSD'
    assert test_obj.get_virtual_facts() == {}
    assert test_obj.detect_virt_product() == {
        'virtualization_type': '', 'virtualization_role': '',
        'virtualization_tech_guest': set(), 'virtualization_tech_host': set()
    }
    assert test_obj.detect_virt_vendor() == {
        'virtualization_type': '', 'virtualization_role': '',
        'virtualization_tech_guest': set(), 'virtualization_tech_host': set()
    }


# Generated at 2022-06-13 04:16:27.677525
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual = NetBSDVirtual({'kernel': 'darwin'}, None)
    assert virtual.platform == 'NetBSD'


# Generated at 2022-06-13 04:16:30.041270
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual_facts = NetBSDVirtual('fake_data')
    assert virtual_facts.data == 'fake_data'
    assert virtual_facts.platform == 'NetBSD'

# Generated at 2022-06-13 04:16:34.002222
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    netbsd_virtual_collector = NetBSDVirtualCollector()
    assert netbsd_virtual_collector._platform == 'NetBSD'
    assert netbsd_virtual_collector._fact_class == NetBSDVirtual


# Generated at 2022-06-13 04:16:35.239544
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    obj = NetBSDVirtual()
    assert obj.platform == 'NetBSD'

# Generated at 2022-06-13 04:16:41.255448
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.netbsd_virtual import NetBSDVirtual

    x = NetBSDVirtual()

    assert x.get_virtual_facts() == {
        'virtualization_role': '',
        'virtualization_type': '',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set(),
        'virtualization_product_facts': [],
    }

# Generated at 2022-06-13 04:16:46.748723
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    # Create a NetBSDVirtual object
    netbsd_virtual_obj = NetBSDVirtual(
        module=None,  # We don't need module object
        sysctl_path="../../module_utils/facts/virtual/sysctl.py",  # Path of sysctl file
        sysctl_exe="echo",  # Command used to execute the sysctl command.
        proc_path='../../module_utils/facts/virtual/proc.py'  # Path of proc file
    )

    # This is the output of the
    # machdep.dmi.system-product=VirtualBox and machdep.dmi.system-vendor=innotek GmbH
    # command.
    # The output of this command is used to detect the virt product and virt vendor
    # respectively.

# Generated at 2022-06-13 04:16:53.225791
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual_facts = NetBSDVirtual().get_virtual_facts()
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts

# Generated at 2022-06-13 04:19:34.555686
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    # Set up Virtual object
    NetBSDVirtual_fact_obj = NetBSDVirtual(module=None)

    # Run method with known inputs
    input_data = {'kernel': 'NetBSD'}
    out = NetBSDVirtual_fact_obj.get_virtual_facts(data=input_data)

    assert out['virtualization_type'] == ''
    assert out['virtualization_role'] == ''
    assert out['virtualization_tech_guest'] == set()
    assert out['virtualization_tech_host'] == set()

    input_data = {'kernel': 'NetBSD', 'machdep.dmi.system-vendor': ', QEMU'}
    out = NetBSDVirtual_fact_obj.get_virtual_facts(data=input_data)

    assert out['virtualization_type'] == 'hvm'


# Generated at 2022-06-13 04:19:38.464268
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    netbsd = NetBSDVirtualCollector()
    assert netbsd.platform == 'NetBSD'
    assert netbsd.fact_class._platform == 'NetBSD'

# Generated at 2022-06-13 04:19:42.199666
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual = NetBSDVirtual({})
    assert virtual._platform == 'NetBSD'

    virtual = NetBSDVirtual({}, gather_subset=['!all', 'virtual'])
    assert virtual._platform == 'NetBSD'

    virtual = NetBSDVirtual({}, gather_subset=['all', '!virtual'])
    assert virtual._platform is None


# Generated at 2022-06-13 04:19:47.351894
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    # Create fake file
    from os.path import expanduser
    from tempfile import mkstemp

    (fd, file_name) = mkstemp()
    # Setup fake content
    hypervisor_content = 'some hypervisor'
    dmi_content = (
        'System Information\n'
        '    Manufacturer: Virtualbox\n'
        '    Product Name: VirtualBox\n'
        '    Version: 5.1.6\n'
    )
    os.write(fd, bytes(hypervisor_content, encoding='ascii'))
    os.close(fd)

    # Setup fake files
    dmi_file_name = expanduser('~/modules/ansible/facts/virtual/netbsd/dmi')