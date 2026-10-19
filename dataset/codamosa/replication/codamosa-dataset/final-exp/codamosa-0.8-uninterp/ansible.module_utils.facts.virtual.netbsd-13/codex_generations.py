

# Generated at 2022-06-13 04:09:54.928101
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsdvirtual = NetBSDVirtual()
    assert netbsdvirtual


# Generated at 2022-06-13 04:09:56.100041
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    collect = NetBSDVirtualCollector()
    assert collect is not None

# Generated at 2022-06-13 04:09:56.577675
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    assert NetBSDVirtual

# Generated at 2022-06-13 04:10:03.723315
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    netbsd = NetBSDVirtual()
    facts = netbsd.get_virtual_facts()
    assert facts['virtualization_type'] == 'xen'
    assert facts['virtualization_role'] == 'guest'
    assert len(facts['virtualization_tech_guest']) == 1
    assert len(facts['virtualization_tech_host']) == 0

# Generated at 2022-06-13 04:10:12.830016
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    try:
        import xmlrpclib
    except ImportError:
        import xmlrpc.client as xmlrpclib
    try:
        from unittest.mock import patch, mock_open
    except ImportError:
        from mock import patch, mock_open

    virt_facts = NetBSDVirtual()

    virt_facts.sysctl = ['hw.product=VMWare Virtual Platform',
                         'hw.vendor=VMware, Inc.',
                         'machdep.hypervisor=VMware, Inc. (KVM variant)']


# Generated at 2022-06-13 04:10:14.562485
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    netbsd_virtual = NetBSDVirtual()
    assert netbsd_virtual.get_virtual_facts() == {}

# Generated at 2022-06-13 04:10:18.479352
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    my_NetBSDVirtualCollector = NetBSDVirtualCollector()
    assert type(my_NetBSDVirtualCollector) is NetBSDVirtualCollector


# Generated at 2022-06-13 04:10:22.539596
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    netbsd_virtual_collector = NetBSDVirtualCollector()
    assert netbsd_virtual_collector._fact_class == NetBSDVirtual
    assert netbsd_virtual_collector._platform == 'NetBSD'


# Generated at 2022-06-13 04:10:23.556717
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    NetBSDVirtual()



# Generated at 2022-06-13 04:10:26.044118
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual_facts = NetBSDVirtual()
    assert virtual_facts._platform == 'NetBSD'
    assert isinstance(virtual_facts, Virtual)

# Generated at 2022-06-13 04:10:34.330597
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virt = NetBSDVirtual()
    assert virt.get_virtual_facts() == {
        'virtualization_role': 'guest',
        'virtualization_type': 'xen',
        'virtualization_tech_guest': {'xen'},
        'virtualization_tech_host': set(),
    }

# Generated at 2022-06-13 04:10:35.964199
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual_facts = NetBSDVirtual()
    assert virtual_facts._platform == 'NetBSD'


# Generated at 2022-06-13 04:10:40.259512
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virt = NetBSDVirtual()
    virtual_facts = virt.get_virtual_facts()
    assert virtual_facts['virtualization_type'] in ('', 'xen', 'hvm')
    assert virtual_facts['virtualization_role'] in ('', 'guest')
    assert virtual_facts['virtualization_tech_guest'] != set()
    assert virtual_facts['virtualization_tech_host'] != set()

# Generated at 2022-06-13 04:10:44.806111
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    facts = NetBSDVirtual().get_virtual_facts()
    assert ('virtualization_type' in facts)
    assert ('virtualization_role' in facts)
    assert ('virtualization_tech_guest' in facts)
    assert ('virtualization_tech_host' in facts)

# Generated at 2022-06-13 04:10:46.609490
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    facts = NetBSDVirtual('')
    assert facts.platform == 'NetBSD'


# Generated at 2022-06-13 04:10:51.153997
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual()
    assert isinstance(netbsd_virtual, NetBSDVirtual)
    assert isinstance(netbsd_virtual, Virtual)
    assert isinstance(netbsd_virtual, VirtualSysctlDetectionMixin)


# Generated at 2022-06-13 04:10:54.581069
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    v = NetBSDVirtual(None)
    assert v.platform == 'NetBSD'
    assert v.virtualization_type == ''
    assert v.virtualization_role == ''
    assert v.virtualization_tech_guest == set()
    assert v.virtualization_tech_host == set()


# Generated at 2022-06-13 04:10:59.775999
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    netbsd_virtual_collector = NetBSDVirtualCollector()
    assert isinstance(netbsd_virtual_collector, VirtualCollector)
    assert isinstance(netbsd_virtual_collector, NetBSDVirtualCollector)
    assert netbsd_virtual_collector._platform == 'NetBSD'


# Generated at 2022-06-13 04:11:01.680782
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    # Expect that no sysfs is present, so virtual_facts must be empty
    virtual = NetBSDVirtual({})
    assert virtual.data == {'virtualization_type': '',
                            'virtualization_role': '',
                            'virtualization_tech_guest': set(),
                            'virtualization_tech_host': set()}

# Generated at 2022-06-13 04:11:06.217036
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    facts = {'kernel': 'NetBSD'}
    expected_result = {
        'virtualization_role': 'guest',
        'virtualization_type': 'xen',
        'virtualization_tech_guest': set(['xen']),
        'virtualization_tech_host': set(),
    }

    nv = NetBSDVirtual(facts)
    result = nv.get_virtual_facts()
    assert result == expected_result

# Generated at 2022-06-13 04:11:14.354064
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual = NetBSDVirtual()
    assert virtual.get_virtual_facts() == {}

# Generated at 2022-06-13 04:11:21.677501
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    v = NetBSDVirtual()
    assert v.platform == 'NetBSD'
    assert v.get_virtual_facts() == {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_type_role': '',
        'virtualization_full': False,
        'virtualization_centric': 'host',
        'virtualization_guest_centric': 'guest',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set()
    }

# Generated at 2022-06-13 04:11:31.136608
# Unit test for constructor of class NetBSDVirtual

# Generated at 2022-06-13 04:11:35.383876
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual_facts = NetBSDVirtual()
    virtual_facts.platform = 'NetBSD'
    virtual_facts.get_virtual_facts()

# Generated at 2022-06-13 04:11:39.800827
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virt = NetBSDVirtual(dict())
    assert virt.platform == 'NetBSD'
    assert virt.get_virtual_facts() == {'virtualization_type': '', 'virtualization_role': '', 'virtualization_tech_guest': set(), 'virtualization_tech_host': set()}

# Generated at 2022-06-13 04:11:41.876620
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    # Verify that get_virtual_facts() returns a dictionary which looks like
    # {'virtualization_type': '',
    #  'virtualization_role': ''}
    netbsd = NetBSDVirtual()
    virtual_facts = netbsd.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''

# Generated at 2022-06-13 04:11:43.634891
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    assert issubclass(NetBSDVirtualCollector, VirtualCollector)


# Generated at 2022-06-13 04:11:46.597185
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    facts_inst = NetBSDVirtual('')
    assert isinstance(facts_inst, Virtual)
    assert isinstance(facts_inst, VirtualSysctlDetectionMixin)

# Generated at 2022-06-13 04:11:54.060983
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    mock_cmds = {
        "sysctl -n machdep.dmi.system-product": "KVM",
        "sysctl -n machdep.dmi.system-vendor": "Red Hat",
        "sysctl -n machdep.hypervisor": "Red Hat",
        "sysctl -n kern.hostname": "foo",
        "uname -a": "NetBSD",
    }
    expected_facts = {
        'virtualization_role': 'guest',
        'virtualization_type': 'kvm',
        'virtualization_tech_host': set(['kvm']),
        'virtualization_tech_guest': set(['kvm']),
    }
    NetBSDVirtualCollector._execute_module = lambda *args, **kwargs: mock_cmds
    gv = NetBSDVirtual

# Generated at 2022-06-13 04:11:57.689653
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual = NetBSDVirtual()
    assert hasattr(virtual, '_platform_fact')
    assert hasattr(virtual, '_collector_platforms')
    assert virtual._platform_fact == 'NetBSDVirtual'
    assert virtual._collector_platforms == ['NetBSD']


# Generated at 2022-06-13 04:12:12.869765
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual = NetBSDVirtual(None)
    assert isinstance(virtual, NetBSDVirtual)


# Generated at 2022-06-13 04:12:14.662320
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual()
    assert netbsd_virtual

# Generated at 2022-06-13 04:12:18.166860
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual()
    assert netbsd_virtual._platform == 'NetBSD'
    assert netbsd_virtual._fact_class == NetBSDVirtual
    assert netbsd_virtual._virt_subsystem == 'sysctl'


# Generated at 2022-06-13 04:12:25.496781
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    a = NetBSDVirtual()
    assert(a.platform == 'NetBSD')

    # Test the get_virtual_facts() method
    assert(a.get_virtual_facts()['virtualization_type'] == '')
    assert(a.get_virtual_facts()['virtualization_role'] == '')
    assert(a.get_virtual_facts()['virtualization_tech_guest'] == set())
    assert(a.get_virtual_facts()['virtualization_tech_host'] == set())

# Generated at 2022-06-13 04:12:27.400531
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual = NetBSDVirtual()
    assert virtual._platform == 'NetBSD'



# Generated at 2022-06-13 04:12:29.870560
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    virtual_collector = NetBSDVirtualCollector()
    assert virtual_collector._platform == 'NetBSD'
    assert virtual_collector._fact_class.platform == 'NetBSD'

# Generated at 2022-06-13 04:12:35.659285
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    netbsd_virtual = NetBSDVirtual({})
    virtual_facts = netbsd_virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'xen'
    assert virtual_facts['virtualization_role'] == 'guest'
    assert 'xen' in virtual_facts['virtualization_tech_guest']
    assert virtual_facts['virtualization_tech_host'] == set()

# Generated at 2022-06-13 04:12:36.909977
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd = NetBSDVirtual()
    assert isinstance(netbsd, NetBSDVirtual)
    assert netbsd.platform == "NetBSD"


# Generated at 2022-06-13 04:12:39.494344
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    netbsd_virtual_collector = NetBSDVirtualCollector()
    assert netbsd_virtual_collector._platform == 'NetBSD'

# Generated at 2022-06-13 04:12:42.182499
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    netbsd = NetBSDVirtualCollector()
    assert netbsd.platform == 'NetBSD'
    assert netbsd.fact_class.platform == 'NetBSD'

# Generated at 2022-06-13 04:13:10.581165
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    x = NetBSDVirtualCollector()
    assert x._platform == 'NetBSD'

# Generated at 2022-06-13 04:13:15.741895
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual = NetBSDVirtual(module=None)

    # Fake machdep.dmi.system-product is "NetBSD"
    product = 'NetBSD'
    assert virtual.get_virtual_facts()['virtualization_type'] == ''
    assert virtual.get_virtual_facts()['virtualization_role'] == ''

    # Fake machdep.dmi.system-product is "VMware Virtual Platform"
    product = 'VMware Virtual Platform'
    assert virtual.get_virtual_facts()['virtualization_type'] == 'VMware'
    assert virtual.get_virtual_facts()['virtualization_role'] == 'guest'

    # Fake machdep.dmi.system-product is "VirtualBox"
    product = 'VirtualBox'
    assert virtual.get_virtual_facts()['virtualization_type'] == 'VirtualBox'
   

# Generated at 2022-06-13 04:13:19.191988
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual = NetBSDVirtual()
    assert virtual._platform == 'NetBSD'
    assert virtual._fact_class == NetBSDVirtual


# Generated at 2022-06-13 04:13:24.881861
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual_facts = NetBSDVirtual().get_virtual_facts()
    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''
    assert virtual_facts['virtualization_system'] == ''
    assert virtual_facts['virtualization_role'] == ''
    assert 'virtual_guest_total' in virtual_facts
    assert 'virtual_guest_active' in virtual_facts

# Generated at 2022-06-13 04:13:26.263136
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
   assert NetBSDVirtualCollector._fact_class == NetBSDVirtual


# Generated at 2022-06-13 04:13:30.783405
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    net = NetBSDVirtual()
    virtual = net.get_virtual_facts()
    assert virtual['virtualization_type'] == ''
    assert virtual['virtualization_role'] == ''
    assert virtual['virtualization_tech_guest'] == set()
    assert virtual['virtualization_tech_host'] == set()

# Generated at 2022-06-13 04:13:31.641262
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    NetBSDVirtualCollector()

# Generated at 2022-06-13 04:13:35.089036
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    facts = NetBSDVirtualCollector().collect()['ansible_facts']['ansible_virtualization_facts']
    assert facts['virtualization_type'] == ''
    assert facts['virtualization_role'] == ''
    assert facts['virtualization_system'] == ''
    assert facts['virtualization_product'] == ''

# Generated at 2022-06-13 04:13:38.657048
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual({'system_vendor': 'Amazon EC2'})
    assert netbsd_virtual.data['virtualization_type'] == 'xen'
    assert netbsd_virtual.data['virtualization_role'] == 'guest'

# Generated at 2022-06-13 04:13:41.096571
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    lns = NetBSDVirtualCollector()
    assert lns._platform == 'NetBSD'
    assert lns._fact_class is NetBSDVirtual

# Generated at 2022-06-13 04:14:46.572093
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual = NetBSDVirtual()
    virtual_facts = virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == ''

# Generated at 2022-06-13 04:14:49.638314
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual()
    assert netbsd_virtual.platform == 'NetBSD'


# Generated at 2022-06-13 04:14:53.285168
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    test_virtual_instance = NetBSDVirtual()
    virtual_facts = test_virtual_instance.get_virtual_facts()

    assert isinstance(virtual_facts, dict)
    assert isinstance(virtual_facts['virtualization_type'], str)
    assert isinstance(virtual_facts['virtualization_role'], str)

# Generated at 2022-06-13 04:14:55.753023
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    netBSD_facts = NetBSDVirtualCollector(None, None, None)
    assert netBSD_facts._platform == 'NetBSD'
    assert netBSD_facts._fact_class == NetBSDVirtual

# Generated at 2022-06-13 04:14:58.144132
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual_facts = NetBSDVirtual()
    assert virtual_facts._platform == 'NetBSD'
    assert virtual_facts.get_virtual_facts() == {}



# Generated at 2022-06-13 04:15:03.593793
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    netbsdvirtual = NetBSDVirtual()
    assert netbsdvirtual.get_virtual_facts() == {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_tech_host': set(),
        'virtualization_tech_guest': set()
    }



# Generated at 2022-06-13 04:15:07.449692
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    v = NetBSDVirtual()
    assert v is not None
    assert v._platform == 'NetBSD'
    assert isinstance(v._detect_virt_product, dict)
    assert isinstance(v._detect_virt_vendor, dict)
    assert v._fact_class is NetBSDVirtual
    assert v._platform is 'NetBSD'

# Generated at 2022-06-13 04:15:12.451811
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.netbsd import NetBSDVirtual

    # Get the virtual fact  value from fact_subset.get_virtual_facts method
    virtual_facts = NetBSDVirtual().get_virtual_facts()

    # The assert below will fail until you implement the code.
    assert virtual_facts['virtualization_type'] == ''

# Generated at 2022-06-13 04:15:18.612170
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    ns = {'module': {'params': {'gather_subset': ['!all', 'virtual']}}}
    netbsd_virtual_obj = NetBSDVirtual(set(), ns, False)

    assert netbsd_virtual_obj.get_virtual_facts() == {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_type_role': '',
        'virtualization_technologies': set(),
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set(),
        'virtualization_tech_guest_text': '',
        'virtualization_tech_host_text': '',
    }


# Generated at 2022-06-13 04:15:24.740604
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    collector = NetBSDVirtualCollector()
    facts = {}
    expected_facts = {
    'virtualization_role': '',
    'virtualization_type': '',
    'virtualization_tech_guest': set(),
    'virtualization_tech_host': set()}
    collector.get_virtual_facts(facts)
    assert facts == expected_facts

# Generated at 2022-06-13 04:18:02.490637
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual_facts = NetBSDVirtual()
    assert virtual_facts.platform == 'NetBSD'
    assert virtual_facts.get_virtual_facts() == {}

# Generated at 2022-06-13 04:18:04.221590
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    assert NetBSDVirtualCollector(None, None, None)._platform == 'NetBSD'
    assert NetBSDVirtualCollector(None, None, None)._fact_class == NetBSDVirtual

# Generated at 2022-06-13 04:18:04.860858
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    assert NetBSDVirtualCollector._platform == 'NetBSD'

# Generated at 2022-06-13 04:18:06.419588
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    assert NetBSDVirtualCollector._platform == 'NetBSD'
    assert NetBSDVirtualCollector._fact_class == NetBSDVirtual

# Generated at 2022-06-13 04:18:08.453867
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():

    netbsd_virtual = NetBSDVirtual({'module_setup': {'filter': ['*']}})
    facts = {'module_setup': {'filter': ['*']}}

    virtual_facts = netbsd_virtual.get_virtual_facts()
    assert virtual_facts == facts

# Generated at 2022-06-13 04:18:18.621129
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    # Test case where all virtualization information is returned.
    virtual_facts = {
        'virtualization_type': 'xen',
        'virtualization_role': 'guest',
        'virtualization_tech_guest': ['xen'],
        'virtualization_tech_host': ['xen']
    }
    nvd = NetBSDVirtual({'machdep.dmi.system-product': 'HVM domU'}, {})
    nvd1 = NetBSDVirtual({'machdep.hypervisor': 'xen'}, {})
    assert(nvd.get_virtual_facts() == virtual_facts)
    assert(nvd1.get_virtual_facts() == virtual_facts)

    # Test case where only part of the virtualization information is returned.

# Generated at 2022-06-13 04:18:20.982567
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    test_VirtualCollector = NetBSDVirtualCollector()
    assert test_VirtualCollector._fact_class == NetBSDVirtual
    assert test_VirtualCollector._platform == 'NetBSD'


# Generated at 2022-06-13 04:18:25.768944
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    """Test constructor of class NetBSDVirtualCollector"""
    fact_class = NetBSDVirtualCollector(None, None)
    assert fact_class._platform == 'NetBSD'
    assert fact_class._fact_class == NetBSDVirtual


# Generated at 2022-06-13 04:18:33.342649
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    platform = NetBSDVirtual()

    # test with isolation and machdep.dmi.system-vendor as 'KVM'
    with open('/proc/sysctl', 'w') as proc_sysctl:
        proc_sysctl.write('machdep.hypervisor: foo\n')
    with open('/proc/curproc/cmdline', 'w') as proc_cmdline:
        proc_cmdline.write('foo bar')
    with open('/proc/cpuinfo', 'w') as proc_cpuinfo:
        proc_cpuinfo.write('foo bar')
    with open('/dev/xencons', 'w') as dev_xencons:
        pass


# Generated at 2022-06-13 04:18:36.322925
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual = NetBSDVirtual()
    assert virtual.platform == 'NetBSD'
    assert virtual._platform == 'NetBSD'