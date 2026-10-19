

# Generated at 2022-06-13 04:09:53.729404
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    # Test without required parameter 'platform'
    try:
        NetBSDVirtualCollector()
    except TypeError as e:
        assert 'missing 3 required positional arguments' in str(e)

# Generated at 2022-06-13 04:09:55.474268
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual()
    assert netbsd_virtual.platform == 'NetBSD'

# Generated at 2022-06-13 04:10:01.466372
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    test_spec = {
        'virtualization_type': 'kvm',
        'virtualization_role': 'guest',
        'virtualization_tech_guest': {'kvm'},
        'virtualization_tech_host': {'kvm'},
    }

    test_result = {
        'virtualization_type': 'kvm',
        'virtualization_role': 'guest',
        'virtualization_tech_guest': 'kvm',
        'virtualization_tech_host': 'kvm',
    }

    module_path = '/fake/path/to/ansible_module.py'
    # Create instance of NetBSDVirtual
    netbsd_virtual = NetBSDVirtual(module_path)
    # Read test file

# Generated at 2022-06-13 04:10:02.109116
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    NetBSDVirtual()

# Generated at 2022-06-13 04:10:07.498477
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    # Test for 'virtualization_type' is empty
    netbsd_virtual_facts = NetBSDVirtual({})
    virtual_facts = netbsd_virtual_facts.get_virtual_facts()
    assert not virtual_facts['virtualization_type']
    assert not virtual_facts['virtualization_role']
    assert not virtual_facts['virtualization_tech_guest']
    assert not virtual_facts['virtualization_tech_host']

# Generated at 2022-06-13 04:10:08.824084
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd = NetBSDVirtual()
    assert netbsd.platform == 'NetBSD'



# Generated at 2022-06-13 04:10:10.112265
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual = NetBSDVirtual()
    virtual_facts = virtual.get_virtual_facts()
    assert isinstance(virtual_facts, dict)

# Generated at 2022-06-13 04:10:14.368408
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    results = dict(
        virtualization_type="xen",
        virtualization_role="guest",
        virtualization_tech_host=["xen"],
        virtualization_tech_guest=["xen"]
    )

    collector = NetBSDVirtualCollector()
    virtual = collector.collect()
    assert virtual.get_facts() == results

# Generated at 2022-06-13 04:10:15.684215
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual_facts = NetBSDVirtual({})
    virtual_facts.get_virtual_facts()

# Generated at 2022-06-13 04:10:18.916000
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual({}, {})

    assert netbsd_virtual is not None

# Generated at 2022-06-13 04:10:29.295622
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    fake_module = type('obj', (object,), {'params': {'gather_subset': '!all,!any'}})
    virtual_facts = NetBSDVirtual(fake_module).get_virtual_facts()
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_subtype' in virtual_facts
    assert 'virtualization_technologies_guest' in virtual_facts
    assert 'virtualization_technologies_host' in virtual_facts

# Generated at 2022-06-13 04:10:32.746656
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    netbsd_virtual = NetBSDVirtual()
    import json

    test_facts, expected_facts = netbsd_virtual.get_virtual_facts()

    assert test_facts == expected_facts


# Generated at 2022-06-13 04:10:33.569838
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    NetBSDVirtualCollector()


# Generated at 2022-06-13 04:10:35.836940
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsdvirtual = NetBSDVirtual()
    assert netbsdvirtual.collector_quality == 1024
    assert netbsdvirtual.platform == 'NetBSD'


# Generated at 2022-06-13 04:10:40.155461
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual()
    netbsd_virtual_collector = NetBSDVirtualCollector()

     # Test for attributes
    assert netbsd_virtual.platform == netbsd_virtual_collector._platform
    assert netbsd_virtual.get_virtual_facts.__func__ == netbsd_virtual_collector._fact_class.get_virtual_facts.__func__

# Generated at 2022-06-13 04:10:41.412323
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual = NetBSDVirtual(module=None)
    assert virtual

# Generated at 2022-06-13 04:10:53.066450
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    test_value_1 = {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_sysctl': {
            'machdep.dmi.system-vendor': 'VMWare, Inc.',
            'machdep.dmi.system-product': 'VMware Virtual Platform'
        }
    }
    test_value_2 = {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_sysctl': {
            'machdep.dmi.system-vendor': 'VMWare, Inc.',
            'machdep.dmi.system-product': 'VMware Virtual Platform',
            'machdep.hypervisor': 'VMWare, Inc.'
        }
    }
    test_value_3

# Generated at 2022-06-13 04:10:54.268562
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virt = NetBSDVirtual()
    assert virt._platform == 'NetBSD'

# Generated at 2022-06-13 04:10:55.560137
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    assert isinstance(NetBSDVirtualCollector(), VirtualCollector)


# Generated at 2022-06-13 04:11:05.528424
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    # Test Init
    obj = NetBSDVirtual()
    assert obj._platform == 'NetBSD'
    assert obj.sysctl_values == {}
    assert obj.virtual_2_dict('vm_guest', 'NetBSD', 'host') == {'virtualization_type': 'vm_guest', 'virtualization_role': 'host',
                                                                'virtualization_system': 'NetBSD'}
    assert obj.virtual_2_dict('vm_guest', '', 'host') == {'virtualization_type': 'vm_guest', 'virtualization_role': 'host'}
    assert obj.virtual_2_dict('vm_guest', '', '') == {'virtualization_type': 'vm_guest'}

# Generated at 2022-06-13 04:11:15.484840
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virt = NetBSDVirtual()
    virtual_facts = virt.get_virtual_facts()
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts

# Generated at 2022-06-13 04:11:19.181875
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual()
    # Test the constructor of class NetBSDVirtual
    assert netbsd_virtual.platform == 'NetBSD'

# Generated at 2022-06-13 04:11:19.848546
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    NetBSDVirtual()

# Generated at 2022-06-13 04:11:22.457935
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    obj = NetBSDVirtualCollector()
    assert obj.platform == 'NetBSD'
    assert obj._fact_class == NetBSDVirtual

# Generated at 2022-06-13 04:11:23.784582
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    NetBSDVirtualCollector()

# Generated at 2022-06-13 04:11:25.603026
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual()
    assert netbsd_virtual.platform == 'NetBSD'

# Generated at 2022-06-13 04:11:29.001035
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual(None)
    assert isinstance(netbsd_virtual, NetBSDVirtual)
    assert isinstance(netbsd_virtual._platform, str)
    assert isinstance(netbsd_virtual._fact_class, NetBSDVirtual)


# Generated at 2022-06-13 04:11:35.167836
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    # Test that we correctly detect that we're running inside a virtual
    # machine.
    if os.path.exists('/proc/sys/xen'):
        expect_facts = {'virtualization_role': 'guest',
                        'virtualization_type': 'xen',
                        'virtualization_tech_guest': {'xen'},
                        'virtualization_tech_host': set(),
                        'virtualization_product_version': '',
                        'virtualization_product': ''}
        assert expect_facts == NetBSDVirtual().get_virtual_facts()

    # Test that we correctly detect that we're running on a host.

# Generated at 2022-06-13 04:11:42.068845
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():

    test_facts = {
        'machdep.dmi.system-product': 'KVM',
        'machdep.dmi.system-vendor': 'OpenBSD',
    }

    expected_facts = {
        'virtualization_type': 'kvm',
        'virtualization_role': 'guest',
        'virtualization_tech_guest': {'kvm'},
        'virtualization_tech_host': {'kvm'}
    }

    module = CustomModule(test_facts)
    virtual_facts = NetBSDVirtual(module).get_virtual_facts()
    assert virtual_facts == expected_facts



# Generated at 2022-06-13 04:11:43.035200
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    NetBSDVirtualCollector()

# Generated at 2022-06-13 04:11:58.773782
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virt = NetBSDVirtual()
    actual = virt.get_virtual_facts()
    expected = {'virtualization_type': '', 'virtualization_role': '', 'virtualization_tech_guest': set(), 'virtualization_tech_host': set()}
    assert actual == expected

# Generated at 2022-06-13 04:12:10.393423
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    # Arrange
    collector = NetBSDVirtualCollector()
    kvm_guest = {}
    kvm_host = {}
    # Act
    kvm_guest = collector.collect(['machdep.dmi.system-product=KVM', 'machdep.hypervisor=QEMU', 'machdep.hypervisor.domain=guest'], [])['ansible_facts']
    kvm_host = collector.collect(['machdep.dmi.system-product=KVM', 'machdep.hypervisor=QEMU', 'machdep.hypervisor.domain=host'], [])['ansible_facts']

    # Assert
    assert kvm_guest['ansible_virtualization_type'] == 'kvm'
    assert kvm_guest['ansible_virtualization_role']

# Generated at 2022-06-13 04:12:12.669195
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual(module=None)
    assert netbsd_virtual.platform == 'NetBSD'


# Generated at 2022-06-13 04:12:21.638050
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():

    class FakeSysctl:
        def __init__(self, **kwargs):
            self.return_values = kwargs

        def sysctlbyname(self, name):
            return self.return_values[name]

    new_virtual = NetBSDVirtual(FakeSysctl(machdep_dmi_system_vendor='QEMU',
                                           machdep_dmi_system_product='Standard PC (Q35 + ICH9, 2009))',
                                           machdep_hypervisor=''))

    # Test returned values
    assert new_virtual.get_virtual_facts()['virtualization_type'] == 'kvm'
    assert new_virtual.get_virtual_facts()['virtualization_role'] == 'guest'

# Generated at 2022-06-13 04:12:26.039323
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    assert NetBSDVirtualCollector().platform == 'NetBSD'
    assert NetBSDVirtualCollector()._platform == 'NetBSD'
    assert NetBSDVirtualCollector()._fact_class == NetBSDVirtual


# Generated at 2022-06-13 04:12:32.100549
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    netbsd = NetBSDVirtual()
    facts = netbsd.get_virtual_facts()

    assert facts['virtualization_status']
    assert 'virtualization_type' in facts
    assert 'virtualization_role' in facts
    assert 'virtualization_system' in facts
    assert 'virtualization_role' in facts
    assert 'virtualization_product' in facts
    assert 'virtualization_tech_guest' in facts
    assert 'virtualization_tech_host' in facts

# Generated at 2022-06-13 04:12:37.189979
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    netbsd_collector = NetBSDVirtualCollector()
    assert netbsd_collector._platform == "NetBSD"
    assert netbsd_collector._fact_class == NetBSDVirtual

# Generated at 2022-06-13 04:12:40.252010
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    netbsd_virtual_collector = NetBSDVirtualCollector()

    assert netbsd_virtual_collector._fact_class
    assert netbsd_virtual_collector._platform

# Generated at 2022-06-13 04:12:41.703724
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    assert NetBSDVirtual().platform == 'NetBSD'


# Generated at 2022-06-13 04:12:42.882188
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    virtual_collector = NetBSDVirtualCollector()

# Generated at 2022-06-13 04:13:15.483336
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    nbv = NetBSDVirtualCollector()
    nbv_factclass = nbv._fact_class
    nbv_platform = nbv._platform
    assert nbv_factclass.platform == 'NetBSD'
    assert nbv_platform == 'NetBSD'

# Generated at 2022-06-13 04:13:25.834209
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    '''Unit test for method NetBSDVirtual.get_virtual_facts()'''
    # Create an instance of class NetBSDVirtual
    test_instance = NetBSDVirtual()

    # Set virtualization_type and virtualization_role to empty strings
    test_instance.facts['virtualization_type'] = ''
    test_instance.facts['virtualization_role'] = ''

    # Get the facts for the NetBSDVirtual class
    test_facts = NetBSDVirtual().get_virtual_facts()

    # Assert that some virtualization_type and virtualization_role is returned
    assert test_facts['virtualization_type'] != ''
    assert test_facts['virtualization_role'] != ''

# Generated at 2022-06-13 04:13:28.062411
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    netbsd_virtual_facts_device = NetBSDVirtualCollector()
    netbsd_virtual_facts_device.get_virtual_facts()

# Generated at 2022-06-13 04:13:30.470868
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual(module=None)
    assert netbsd_virtual is not None


# Generated at 2022-06-13 04:13:32.037409
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    netbsd_virtual_collector = NetBSDVirtualCollector()
    assert netbsd_virtual_collector._fact_class is NetBSDVirtual
    assert netbsd_virtual_collector._platform == 'NetBSD'

# Generated at 2022-06-13 04:13:33.902806
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    module = NetBSDVirtualCollector()
    assert module.platform == 'NetBSD'
    assert module._fact_class == NetBSDVirtual

# Generated at 2022-06-13 04:13:44.912637
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual = NetBSDVirtual({}, {})

    # Set values of sysctl_facts with a dictionary that contain virtualization facts
    virtual.sysctl_facts = {
        'machdep.dmi.system-vendor': 'Amazon EC2',
        'machdep.dmi.system-product': '',
        'machdep.hypervisor': 'qemu',
    }

    # Make get_virtual_facts() return values
    virtual_facts = virtual.get_virtual_facts()

    # Assertion for virtual_facts
    assert virtual_facts['virtualization_type'] == 'xen'
    assert virtual_facts['virtualization_role'] == 'guest'
    assert virtual_facts['virtualization_type_role'] == 'xen_guest'
    assert virtual_facts['virtualization_tech_guest']

# Generated at 2022-06-13 04:13:48.374054
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual()
    assert netbsd_virtual


# Generated at 2022-06-13 04:13:51.888058
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    """
    Checks if get_virtual_facts function returns a dictionary
    """
    result = type(NetBSDVirtual().get_virtual_facts())
    assert result == dict, "The result should be a dictionary"

# Generated at 2022-06-13 04:13:53.111492
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    assert issubclass(NetBSDVirtualCollector, VirtualCollector)

# Generated at 2022-06-13 04:14:55.751277
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    new_NetBSDVirtualCollector = NetBSDVirtualCollector()
    assert new_NetBSDVirtualCollector._fact_class == NetBSDVirtual
    assert new_NetBSDVirtualCollector._platform == 'NetBSD'

# Generated at 2022-06-13 04:14:57.502570
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual()
    assert netbsd_virtual.platform == "NetBSD"

# Generated at 2022-06-13 04:15:07.519316
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    sysinfo = {
        'machdep.dmi.system-product': 'VirtualBox',
        'machdep.dmi.system-vendor': 'innotek GmbH',
        'machdep.dmi.system-version': '1.2',
        'machdep.dmi.product-uuid': '',
        'machdep.dmi.product-serial': '',
        'machdep.hypervisor': 'VirtualBox',
    }
    virtual_obj = NetBSDVirtual(sysinfo)
    assert virtual_obj._platform == 'NetBSD'

    virtual_facts = virtual_obj.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'VirtualBox'
    assert virtual_facts['virtualization_role'] == 'guest'

# Generated at 2022-06-13 04:15:17.503757
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual()
    # Test with empty sysctl string
    assert len(netbsd_virtual.get_virtual_facts()) > 0
    assert netbsd_virtual.get_virtual_facts()['virtualization_type'] == ''
    assert netbsd_virtual.get_virtual_facts()['virtualization_role'] == ''
    # Test with a fake sysctl string
    netbsd_virtual.sysctl = {
        'machdep.dmi.system-product': 'test_xen',
        'machdep.dmi.system-vendor': 'test_xen',
        'machdep.hypervisor': 'test_xen'}
    assert netbsd_virtual.get_virtual_facts()['virtualization_type'] == 'xen'
    assert netbsd_virtual

# Generated at 2022-06-13 04:15:27.566417
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual = NetBSDVirtual()
    virtual.collect_sysctl_keys = lambda x: {'machdep.dmi.system-vendor': 'Parallels Software International Inc.',
                                             'machdep.dmi.system-product': 'Parallels Virtual Platform',
                                             'machdep.hypervisor': 'Xen'}
    # Parallels Virtual Platform on NetBSD
    virtual_facts = virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'parallel'
    assert virtual_facts['virtualization_role'] == 'guest'
    assert virtual_facts['virtualization_full'] == 'guest'
    assert virtual_facts['virtualization_technology'] == 'xen'

# Generated at 2022-06-13 04:15:37.471554
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    # Create instance of class NetBSDVirtual
    instance_NetBSDVirtual = NetBSDVirtual()

    # Virtual class is derived from VirtualSysctlDetectionMixin
    assert(hasattr(instance_NetBSDVirtual, '_sysctl_cmd'))
    assert(hasattr(instance_NetBSDVirtual, '_sysctl_cmd_params'))
    assert(hasattr(instance_NetBSDVirtual, '_sysctl_fact_mappings'))
    assert(hasattr(instance_NetBSDVirtual, '_sysctl_defaults'))
    assert(hasattr(instance_NetBSDVirtual, '_sysctl_vendor_facts'))
    assert(hasattr(instance_NetBSDVirtual, '_sysctl_product_facts'))
    assert(hasattr(instance_NetBSDVirtual, '_sysctl_vm_role_facts'))


# Generated at 2022-06-13 04:15:39.478657
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual()
    assert netbsd_virtual.platform == 'NetBSD'


# Generated at 2022-06-13 04:15:45.448429
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    import sys
    import stat
    import pprint
    import json

    # Constructor
    nv_collector = NetBSDVirtualCollector()
    nv_facts = NetBSDVirtualCollector().collect()

    # e.g. print(json.dumps(nv_facts, indent=4))

    # Verify the result
    try:
        assert isinstance(nv_facts, dict)
    except AssertionError:
        print("FAILURE: Type of nv_facts is not dict.")
        sys.exit(1)

    # e.g. print("virtual_product_facts: " + str(nv_facts['virtual_product_facts']))

# Generated at 2022-06-13 04:15:45.821146
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    pass

# Generated at 2022-06-13 04:15:47.175029
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    collector = NetBSDVirtualCollector()
    assert collector._fact_class is NetBSDVirtual
    assert collector._platform == 'NetBSD'


# Generated at 2022-06-13 04:17:02.033519
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    virtual_facts = NetBSDVirtualCollector()
    assert virtual_facts._fact_class == NetBSDVirtual
    assert virtual_facts._platform == 'NetBSD'

# Generated at 2022-06-13 04:17:05.454743
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    netbsd_virtual_facts = NetBSDVirtual({}, {}, {}, {})
    data = netbsd_virtual_facts.get_virtual_facts()
    assert type(data) is dict

# Generated at 2022-06-13 04:17:07.276066
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd = NetBSDVirtualCollector()
    assert netbsd.get_virtual_facts() == {}

# Generated at 2022-06-13 04:17:16.706201
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    fake_sysctl_machdep_dmi = {
        'machdep.dmi.system-vendor': 'IBM',
        'machdep.dmi.system-product': 'z/VM',
    }

    expected_virtual_facts = {
        'virtualization_type': 'z/vm',
        'virtualization_role': 'guest',
        'virtualization_tech_guest': {'z/vm'},
        'virtualization_tech_host': {},
    }

    NetBSDVirtualCollector._detect_virt_with_sysctl = lambda _: fake_sysctl_machdep_dmi
    assert NetBSDVirtualCollector.fetch_virtual_facts() == expected_virtual_facts

# Generated at 2022-06-13 04:17:20.404918
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual()
    # Constructor doesn't set sysctl_search_strings, so call it here to
    # satisfy the caller
    netbsd_virtual.sysctl_search_strings()


# Generated at 2022-06-13 04:17:21.953451
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual(None)
    assert netbsd_virtual.platform == 'NetBSD'


# Generated at 2022-06-13 04:17:26.791735
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual = NetBSDVirtual()
    facts = virtual.get_virtual_facts()
    assert facts['virtualization_tech_guest'] == {'xen'}
    assert facts['virtualization_type'] == 'xen'
    assert facts['virtualization_role'] == 'guest'

# Generated at 2022-06-13 04:17:27.484461
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    NetBSDVirtual({})

# Generated at 2022-06-13 04:17:34.005892
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    # Hyper-V Virtual Machine
    sysctl_hypervisormachdep_attr = {
        "machdep.hypervisor": "Hypervisor"
    }
    hyperv_virtual_facts = {
        'virtualization_type': 'microsoft',
        'virtualization_role': 'guest',
        'virtualization_tech_guest': set(['hyperv']),
        'virtualization_tech_host': set(['hyperv']),
    }

    # VMware Virtual Machine
    sysctl_vmwaremachdep_attr = {
        "machdep.dmi.system-product": "VMware Virtual Platform",
        "machdep.dmi.system-vendor": "VMware, Inc.",
    }

# Generated at 2022-06-13 04:17:40.708453
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual = NetBSDVirtualCollector.fetch_virtual_facts()
    assert virtual['virtualization_type'] == ''
    assert virtual['virtualization_role'] == ''
    # The detect_virt_product and detect_virt_vendor functions in base.py
    # will run a sysctl -a command, which is known to hang on a number of
    # NetBSD platforms. In order to avoid hanging, we stub them out.
    assert virtual['virtualization_tech_guest'] == set()
    assert virtual['virtualization_tech_host'] == set()