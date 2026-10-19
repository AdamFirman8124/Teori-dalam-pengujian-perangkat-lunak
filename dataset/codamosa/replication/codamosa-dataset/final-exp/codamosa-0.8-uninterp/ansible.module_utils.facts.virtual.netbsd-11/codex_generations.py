

# Generated at 2022-06-13 04:09:59.666715
# Unit test for method get_virtual_facts of class NetBSDVirtual

# Generated at 2022-06-13 04:10:00.905073
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    pass

# Generated at 2022-06-13 04:10:03.174853
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    obj = NetBSDVirtual()
    if obj.platform != 'NetBSD':
        raise Exception('Failed to setup class NetBSDVirtual')

# Generated at 2022-06-13 04:10:11.448144
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd = NetBSDVirtual()
    assert netbsd.platform == "NetBSD"
    assert netbsd.get_virtual_facts() == {
        'virtualization_role': '',
        'virtualization_type': '',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set(),
    }
    assert netbsd.get_virtual_facts()['virtualization_role'] == ''
    assert netbsd.get_virtual_facts()['virtualization_type'] == ''
    assert netbsd.get_virtual_facts()['virtualization_tech_guest'] == set()
    assert netbsd.get_virtual_facts()['virtualization_tech_host'] == set()



# Generated at 2022-06-13 04:10:15.510536
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtuals = NetBSDVirtual()
    for key in virtuals.data.keys():
        assert key == 'virtualization_type' or key == 'virtualization_role' or key == 'virtualization_subtype' \
            or key == 'virtualization_role' or key == 'virtualization_technology'

# Generated at 2022-06-13 04:10:18.720025
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsdv = NetBSDVirtual({})
    assert netbsdv.platform == 'NetBSD'

# Generated at 2022-06-13 04:10:23.169013
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    detector = NetBSDVirtual()
    facts = detector.get_virtual_facts()

    assert 'virtualization_type' in facts
    assert 'virtualization_role' in facts
    assert 'virtualization_tech_host' in facts
    assert 'virtualization_tech_guest' in facts

# Generated at 2022-06-13 04:10:26.885405
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    """Test if NetBSDVirtualCollector class constructor works as expected."""
    virtual_collector = NetBSDVirtualCollector()
    assert virtual_collector._fact_class == NetBSDVirtual
    assert virtual_collector._platform == 'NetBSD'

# Generated at 2022-06-13 04:10:28.876063
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual()
    assert netbsd_virtual.platform == 'NetBSD'



# Generated at 2022-06-13 04:10:33.757308
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual_facts = NetBSDVirtual({}).get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'xen'
    assert virtual_facts['virtualization_role'] == 'guest'


if __name__ == "__main__":
    test_NetBSDVirtual_get_virtual_facts()

# Generated at 2022-06-13 04:10:38.489412
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual_facts_data = NetBSDVirtualCollector().collect()
    assert 'virtualization_type' in virtual_facts_data

# Generated at 2022-06-13 04:10:50.168480
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    """ Check if the methods return the expected output """
    fake_sysctl = {
        'machdep.dmi.system-vendor': 'Google',
        'machdep.dmi.system-product': 'KVM',
        'machdep.hypervisor': ''
    }

    fake_file = {
        '/dev/xencons': True,
        '/dev/xen/evtchn': True,
        '/dev/xen/privcmd': True,
        '/proc/xen': True,
        '/proc/xen/capabilities': True,
        '/sys/hypervisor/type': False
    }

    info = NetBSDVirtual({'sysctl': fake_sysctl, 'file': fake_file})

    ret = info.get_virtual_facts()

    # Check if the method return a dictionary
   

# Generated at 2022-06-13 04:10:52.171272
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd = NetBSDVirtual()
    assert netbsd is not None
    assert netbsd.platform == 'NetBSD'

# Generated at 2022-06-13 04:10:53.891756
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsdVirtual = NetBSDVirtual()
    assert netbsdVirtual._platform == 'NetBSD'

# Generated at 2022-06-13 04:10:56.403098
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    # assert the from_sysinfo object was created
    netbsdvirtual_obj = NetBSDVirtual()
    assert netbsdvirtual_obj


# Generated at 2022-06-13 04:11:02.023750
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual()
    assert netbsd_virtual.platform == 'NetBSD'
    assert netbsd_virtual._platform == 'NetBSD'
    assert netbsd_virtual.fact_class == 'NetBSDVirtual'
    assert netbsd_virtual._fact_class == 'NetBSDVirtual'
    assert netbsd_virtual.collector == 'NetBSDVirtualCollector'


# Generated at 2022-06-13 04:11:03.921004
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    F = NetBSDVirtual({}, {})
    assert F._platform == 'NetBSD'
    assert isinstance(F, VirtualSysctlDetectionMixin)

# Generated at 2022-06-13 04:11:09.660211
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():

    netbsd_virtual = NetBSDVirtual({}, {})
    netbsd_virtual.sysctl = {
        'machdep.dmi.system-product': 'VirtualBox',
        'machdep.dmi.system-vendor': 'innotek GmbH',
    }
    virtual_facts = netbsd_virtual.get_virtual_facts()

    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts

    assert virtual_facts['virtualization_type'] == 'virtualbox'
    assert virtual_facts['virtualization_role'] == 'guest'

# Generated at 2022-06-13 04:11:13.666830
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():

    netbsd_virtual_obj = NetBSDVirtual()
    assert netbsd_virtual_obj.get_virtual_facts() == {'virtualization_type': '', 'virtualization_role': '', 'virtualization_tech_host': set(), 'virtualization_tech_guest': set()}



# Generated at 2022-06-13 04:11:14.789847
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    obj = NetBSDVirtual("/")
    assert isinstance(obj, NetBSDVirtual)

# Generated at 2022-06-13 04:11:26.663226
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd = NetBSDVirtual()
    assert netbsd.platform == 'NetBSD'
    assert netbsd.virtualization_type == ''
    assert netbsd.virtualization_role == ''
    assert len(netbsd.virtualization_tech_guest) == 0
    assert len(netbsd.virtualization_tech_host) == 0

# Generated at 2022-06-13 04:11:33.893718
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    ''' Unit test for get_virtual_facts method of NetBSDVirtual '''


# Generated at 2022-06-13 04:11:36.427267
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual = NetBSDVirtual()
    result = virtual.get_virtual_facts()
    assert result['virtualization_type'] == ''

# Generated at 2022-06-13 04:11:38.610725
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    netbsd_collector = NetBSDVirtualCollector
    assert netbsd_collector._platform == 'NetBSD'

# Generated at 2022-06-13 04:11:45.384497
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual()
    assert isinstance(netbsd_virtual, NetBSDVirtual)
    assert isinstance(netbsd_virtual, Virtual)
    assert isinstance(netbsd_virtual, VirtualSysctlDetectionMixin)


# Generated at 2022-06-13 04:11:46.731430
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual_facts = NetBSDVirtual()
    assert virtual_facts.platform == 'NetBSD'

# Generated at 2022-06-13 04:11:50.141430
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual = NetBSDVirtual()
    virtual._virtual_facts = {}

    # Test if empty values are set as default
    test_default_facts = virtual.get_virtual_facts()
    assert test_default_facts['virtualization_type'] == ''
    assert test_default_facts['virtualization_role'] == ''

# Generated at 2022-06-13 04:11:54.976255
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    assert issubclass(NetBSDVirtualCollector, VirtualCollector)
    assert NetBSDVirtualCollector._platform == 'NetBSD'
    assert NetBSDVirtualCollector._fact_class == NetBSDVirtual

# Generated at 2022-06-13 04:11:56.417774
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual_facts = NetBSDVirtual(None)
    assert isinstance(virtual_facts, NetBSDVirtual)


# Generated at 2022-06-13 04:11:57.681263
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    os_v = NetBSDVirtual()
    assert os_v

if __name__ == '__main__':
    test_NetBSDVirtual()

# Generated at 2022-06-13 04:12:11.164029
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual_facts = NetBDSVirtual()

# Generated at 2022-06-13 04:12:19.456822
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    host_virtual_facts = {
        'virtualization_type': '',
        'virtualization_role': ''
    }
    virtual_facts = {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set()
    }
    expected_virtual_facts = host_virtual_facts.copy()
    expected_virtual_facts.update(virtual_facts)

    result = NetBSDVirtual()
    assert result.facts == expected_virtual_facts
    assert result.platform == 'NetBSD'


# Generated at 2022-06-13 04:12:21.090161
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    nvobj = NetBSDVirtualCollector().get_virtual_facts()
    assert nvobj['netbsd']

# Generated at 2022-06-13 04:12:27.448360
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virt_obj = NetBSDVirtual()
    virtual_facts = virt_obj.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''
    assert virtual_facts['virtualization_tech_host'] == set()
    assert virtual_facts['virtualization_tech_guest'] == set()

# Generated at 2022-06-13 04:12:29.194977
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virt = NetBSDVirtual({})
    assert virt.platform == 'NetBSD'



# Generated at 2022-06-13 04:12:31.990537
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    netbsd_virtual_collector = NetBSDVirtualCollector()
    assert netbsd_virtual_collector._fact_class == NetBSDVirtual
    assert netbsd_virtual_collector._platform == 'NetBSD'

# Generated at 2022-06-13 04:12:35.196537
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    # All checks are only performed if we're actually running on NetBSD
    if 'NetBSD' not in Virtual().facts:
        return

    # Check if all required facts are set
    required_facts = set(('virtualization_type', 'virtualization_role', 'virtualization_technology'))
    assert required_facts <= set(NetBSDVirtual(None).facts.keys())

# Generated at 2022-06-13 04:12:39.521074
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    # If environment variable is set to hypervisor, use it to report
    # virtualization_type
    os.environ['machdep.hypervisor'] = 'vbox'
    os.environ['machdep.dmi.system-product'] = 'bogus'
    os.environ['machdep.dmi.system-vendor'] = 'bogus'
    os.environ['machdep.dmi.chassis-asset-tag'] = 'bogus'
    netbsd_virtual = NetBSDVirtual()
    virtual_facts = netbsd_virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'vbox'
    assert virtual_facts['virtualization_role'] == 'host'

# Generated at 2022-06-13 04:12:49.247223
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    def mock_read_sysctl_if_exists(sysctl_key):
        m = {
            'machdep.hypervisor': 'QEMU',
            'machdep.dmi.system-vendor': 'NetBSD Foundation, Inc.',
            'machdep.dmi.system-product': 'VirtualBox'
        }
        if sysctl_key in m:
            return (0, m[sysctl_key], '')
        return (-1, '', '')

    module = type('AnsibleModule', (object, ), {})
    setattr(module, 'run_command', mock_read_sysctl_if_exists)

    netbsd_virtual = NetBSDVirtual()
    netbsd_virtual.get_module(module)

    virtual_facts = netbsd_virtual.get_

# Generated at 2022-06-13 04:12:52.634627
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netBSDVirtual = NetBSDVirtual()
    assert netBSDVirtual.platform == 'NetBSD'
    assert netBSDVirtual._platform == 'NetBSD'
    assert netBSDVirtual._fact_class == NetBSDVirtual


# Generated at 2022-06-13 04:13:28.041094
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    data = dict(
        platform = 'NetBSD',
        machdep_dmi_system_product = 'KVM',
        machdep_dmi_system_vendor = 'OpenStack Foundation',
        machdep_hypervisor = 'OpenStack Foundation',
        xencons = False
    )
    v = NetBSDVirtual(data)
    facts = v.get_virtual_facts()

    # Test if machdep.dmi.system-product and machdep.dmi_system-vendor is
    # empty.
    assert facts['virtualization_type'] == 'OpenStack Foundation'
    assert facts['virtualization_role'] == 'guest'
    assert facts['virtualization_tech_guest'] == set(['OpenStack Foundation', 'KVM'])

# Generated at 2022-06-13 04:13:29.655581
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual_facts = NetBSDVirtual()
    assert virtual_facts

# Generated at 2022-06-13 04:13:32.345426
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual_facts = {}
    virtual_facts = NetBSDVirtual().get_virtual_facts()

    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''

# Generated at 2022-06-13 04:13:32.881171
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    assert NetBSDVirtual()

# Generated at 2022-06-13 04:13:34.719920
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd = NetBSDVirtual()
    assert netbsd.platform == 'NetBSD'
    assert netbsd.virt_type == 'NetBSD'

# Generated at 2022-06-13 04:13:38.656461
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():

    # Test for empty v_type and v_role
    netbsd_virtual = NetBSDVirtual({'kernel': 'NETBSD'})

    assert netbsd_virtual
    assert netbsd_virtual.data == {}
    assert netbsd_virtual.platform == 'NetBSD'

# Generated at 2022-06-13 04:13:40.371002
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    netbsdvirt = NetBSDVirtual({})
    netbsdvirt.get_virtual_facts()

# Generated at 2022-06-13 04:13:43.899460
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual_object = NetBSDVirtual(module_args=dict(gather_subset=[])).get_virtual_facts()
    assert virtual_object['virtualization_type'] == ''
    assert virtual_object['virtualization_role'] == ''

# Generated at 2022-06-13 04:13:45.616473
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual = NetBSDVirtual(None)

    # Assert that the platform was set correctly
    assert(virtual.platform == 'NetBSD')

# Generated at 2022-06-13 04:13:49.050201
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual()
    assert isinstance(netbsd_virtual, NetBSDVirtual)



# Generated at 2022-06-13 04:14:49.212593
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    assert NetBSDVirtualCollector._platform == 'NetBSD'
    assert NetBSDVirtualCollector._fact_class == NetBSDVirtual

# Generated at 2022-06-13 04:14:50.404816
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    # Add test case here
    pass

# Generated at 2022-06-13 04:14:57.403834
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    """
    Test get_virtual_facts() method of class NetBSDVirtual
    :return: None
    """

    # Create NetBSDVirtual instance
    netbsdvirtual = NetBSDVirtual()

    sysctl_results = {
        'machdep.dmi.system-product': '',
        'machdep.dmi.system-vendor': '',
        'machdep.hypervisor': ''
    }

    netbsdvirtual._get_sysctl_info = lambda x: sysctl_results[x]
    facts_from_sysctl = netbsdvirtual._get_sysctl_info
    facts_from_sysctl.xen_not_found = False

    class TestOS:
        def __init__(self, uname_result):
            self.uname_result = uname_result

    # Test on

# Generated at 2022-06-13 04:15:02.743844
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual = NetBSDVirtual()

    facts = virtual.get_virtual_facts()

    assert facts['virtualization_type'] == 'xen'
    assert facts['virtualization_role'] == 'guest'
    assert 'xen' in facts['virtualization_tech_guest']
    assert facts['virtualization_tech_host'] == set()

# Generated at 2022-06-13 04:15:10.559074
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    #
    # Simple test using a constant mapping table
    #
    class Test(object):
        def __init__(self, val):
            self.value = val

        def readline(self):
            return self.value

    class TestVirtual(NetBSDVirtual):

        @property
        def sysctl_mapping(self):
            return {'machdep.hypervisor': {'Amazon EC2': 'xen'},
                    'machdep.dmi.system-product': {'KVM': 'kvm'}}

        def get(self, key):
            return Test('machdep.hypervisor')

    f = TestVirtual({})
    facts = f.get_virtual_facts()
    if facts['virtualization_type'] != 'xen' or facts['virtualization_role'] != 'guest':
        raise Ass

# Generated at 2022-06-13 04:15:11.644287
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    p = NetBSDVirtual()
    assert p.platform == 'NetBSD'


# Generated at 2022-06-13 04:15:13.015466
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    nbv = NetBSDVirtual()
    assert nbv


# Generated at 2022-06-13 04:15:16.606802
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    from ansible.module_utils.facts.virtual.netbsd import NetBSDVirtual, __virtualname__
    # pylint: disable=protected-access
    virtual = NetBSDVirtual()
    assert virtual._platform == NetBSDVirtual._platform
    assert virtual._fact_class == NetBSDVirtual._fact_class
    assert virtual.__virtualname__ == __virtualname__

# Generated at 2022-06-13 04:15:22.401152
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    """Unit test: get_virtual_facts method of NetBSDVirtual"""
    netbsd_virtual = NetBSDVirtual()
    results = netbsd_virtual.get_virtual_facts()
    assert isinstance(results['virtualization_type'], str)
    assert results['virtualization_type'] in [ '', 'xen', 'xen_dom0', 'xen_domu', 'kvm', 'virtualbox',
        'vmware', 'openvz', 'xenu', 'bhyve', 'hyper-v', 'ai']
    assert isinstance(results['virtualization_role'], str)
    assert results['virtualization_role'] in [ '', 'guest', 'host']
    assert isinstance(results['virtualization_tech_host'], set)

# Generated at 2022-06-13 04:15:25.684633
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    netbsd_virtual_collector = NetBSDVirtualCollector()
    assert netbsd_virtual_collector._fact_class is NetBSDVirtual
    assert netbsd_virtual_collector._platform is 'NetBSD'

# Generated at 2022-06-13 04:17:47.772956
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    netbsd_virtual_collector = NetBSDVirtualCollector()
    assert netbsd_virtual_collector._platform == 'NetBSD'

# Generated at 2022-06-13 04:17:52.832709
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    sysctl = lambda x: None
    sysctl.__getitem__ = lambda s, x: None
    os.path.isdir = lambda p: False
    virtual_class = NetBSDVirtual(sysctl=sysctl)
    assert virtual_class.platform == 'NetBSD'
    assert virtual_class.virtual == 'NetBSD'
    assert virtual_class.get_virtual_facts() == {
        'virtualization_role': '',
        'virtualization_type': '',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set(),
    }

# Generated at 2022-06-13 04:17:59.076551
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():

    # Setup
    test_obj = NetBSDVirtual()
    test_obj.collect_sysctl_facts = lambda: {
        'machdep.dmi.system-product': 'OpenStack KVM',
        'machdep.dmi.system-vendor': 'OpenStack Foundation',
        'machdep.hypervisor': 'KVM'
    }

    os.path.exists = lambda x: False

    # Test
    virtual_facts = test_obj.get_virtual_facts()

    # Assertions
    assert virtual_facts['virtualization_type'] == 'kvm'
    assert virtual_facts['virtualization_role'] == 'guest'
    assert virtual_facts['virtualization_tech_guest'] == {'kvm'}
    assert virtual_facts['virtualization_tech_host'] == set()



# Generated at 2022-06-13 04:17:59.775201
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    # This test is not yet written
    assert True

# Generated at 2022-06-13 04:18:06.677936
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    mock_module = type("module", (object, ), dict(exit_json=lambda self, **kwargs: None, fail_json=lambda self, **kwargs: None))()
    netbsd_virtual = NetBSDVirtual(mock_module)

    hypervisor_file = {'machdep.dmi.system-product': 'VirtualBox',
                       'machdep.dmi.system-vendor': 'Oracle Corporation',
                       'machdep.hypervisor': ''}
    netbsd_virtual.read_file_on_module = lambda x: hypervisor_file.get(x, None)

    results = netbsd_virtual.get_virtual_facts()

    assert(results['virtualization_type'] == 'virtualbox')
    assert(results['virtualization_role'] == 'guest')

# Generated at 2022-06-13 04:18:10.027257
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    # Run on a NetBSD system
    if VirtualCollector.get_platform() != 'NetBSD':
        return
    virtual = NetBSDVirtual()
    virtual_facts = virtual.get_virtual_facts()
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_tech' in virtual_facts

if __name__ == '__main__':
    test_NetBSDVirtual_get_virtual_facts()

# Generated at 2022-06-13 04:18:13.567896
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    netbsd_virtual_collector = NetBSDVirtualCollector()
    assert netbsd_virtual_collector._platform == 'NetBSD'
    assert netbsd_virtual_collector._fact_class.platform == 'NetBSD'

# Generated at 2022-06-13 04:18:19.721125
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    test_obj = NetBSDVirtual()
    result = test_obj.get_virtual_facts()

    if result is not None:
        assert 'virtualization_type' in result
        assert 'virtualization_role' in result
        assert 'virtualization_tech_guest' in result
        assert 'virtualization_tech_host' in result
        assert 'virtualization_product_name' in result
        assert 'virtualization_product_version' in result


# Generated at 2022-06-13 04:18:31.071985
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():

    netbsd_virtual = NetBSDVirtual()
    netbsd_virtual_facts = netbsd_virtual.get_virtual_facts()

    assert 'virtualization_tech_host' in netbsd_virtual_facts
    assert len(netbsd_virtual_facts['virtualization_tech_host']) >= 0

    assert 'virtualization_tech_guest' in netbsd_virtual_facts
    assert len(netbsd_virtual_facts['virtualization_tech_guest']) >= 0

    assert netbsd_virtual_facts['virtualization_type'] in ['docker', 'kvm', 'openvz', 'oracle', 'parallels', 'virtualbox', 'vmware', 'xen']
    assert netbsd_virtual_facts['virtualization_role'] in ['guest', 'host']

# Generated at 2022-06-13 04:18:33.146576
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    b = NetBSDVirtual({'module_setup': {'filter': ''}}, None, None)
    assert isinstance(b, Virtual)
