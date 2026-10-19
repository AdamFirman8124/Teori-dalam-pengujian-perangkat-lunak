

# Generated at 2022-06-13 04:09:55.553064
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    netbsd = NetBSDVirtual()
    result = netbsd.get_virtual_facts()
    assert result['virtualization_type'] == ''
    assert result['virtualization_role'] == ''
    assert len(result['virtualization_tech_guest']) == 0
    assert len(result['virtualization_tech_host']) == 0

# Generated at 2022-06-13 04:09:58.621938
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual_facts = NetBSDVirtual()
    assert virtual_facts.platform == 'NetBSD'
    assert virtual_facts.get_virtual_facts() == {
        'virtualization_role': '',
        'virtualization_type': '',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set(),
    }

# Generated at 2022-06-13 04:09:59.695114
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    NetBSDVirtual(None, None)

# Generated at 2022-06-13 04:10:02.105512
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virt = NetBSDVirtual(None)
    assert isinstance(netbsd_virt, NetBSDVirtual)

# Generated at 2022-06-13 04:10:11.287493
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    import json
    from ansible.module_utils.facts.virtual.netbsd import NetBSDVirtual

    netbsd_virtual = NetBSDVirtual()

    with open('test/unit/module_utils/facts/virtual/netbsd/machdep.hypervisor') as f:
        machdep_hypervisor = f.read()

    with open('test/unit/module_utils/facts/virtual/netbsd/machdep.dmi.system-vendor') as f:
        machdep_dmi_system_vendor = f.read()

    with open('test/unit/module_utils/facts/virtual/netbsd/machdep.dmi.system-product') as f:
        machdep_dmi_system_product = f.read()


# Generated at 2022-06-13 04:10:18.273145
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual_facts = NetBSDVirtual()

    # Test of the constructor
    assert netbsd_virtual_facts.platform == 'NetBSD'
    assert set(netbsd_virtual_facts.get_virtual_facts().keys()) == \
        set(['virtualization_type',
             'virtualization_role',
             'virtualization_tech_guest',
             'virtualization_tech_host'])

# Generated at 2022-06-13 04:10:23.901759
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    v = NetBSDVirtual()
    result = v.get_virtual_facts()
    assert 'virtualization_type' in result
    assert 'virtualization_role' in result
    assert 'virtualization_tech_guest' in result
    assert 'virtualization_tech_host' in result
    assert 'virtualization_product' in result
    assert 'virtualization_vendor' in result

# Generated at 2022-06-13 04:10:25.993674
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virt = NetBSDVirtual()
    assert virt.platform == 'NetBSD'


# Generated at 2022-06-13 04:10:34.418895
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():

    # Test data for dmi
    class DmiTestData(object):
        def __init__(self, system_product_name, system_vendor):
            self.system_product_name = system_product_name
            self.system_vendor = system_vendor

    dmi_test_data = []
    dmi_test_data.append(DmiTestData('Dell R720xd Virtual Machine', 'Dell Inc.'))
    dmi_test_data.append(DmiTestData('KVM', 'Red Hat'))
    dmi_test_data.append(DmiTestData('OpenStack Nova', 'OpenStack Foundation'))
    dmi_test_data.append(DmiTestData('Amazon EC2', 'Amazon EC2'))

# Generated at 2022-06-13 04:10:36.987909
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    # Creating an instance of class NetBSDVirtual
    NetBSDVirtual_obj = NetBSDVirtual()
    print("Details of NetBSDVirtual object is:")
    print(NetBSDVirtual_obj.__dict__)


# Generated at 2022-06-13 04:10:43.517037
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual()
    assert netbsd_virtual.platform == 'NetBSD'
    assert netbsd_virtual.virtual == 'NetBSD'

# Generated at 2022-06-13 04:10:45.592200
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual_facts = NetBSDVirtual()
    assert virtual_facts.get_virtual_facts() == {}

# Generated at 2022-06-13 04:10:47.014195
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual_facts = NetBSDVirtual()
    assert virtual_facts._platform == 'NetBSD'

# Generated at 2022-06-13 04:10:51.537737
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual_facts = NetBSDVirtual().get_virtual_facts()
    assert isinstance(virtual_facts['virtualization_type'], str)
    assert isinstance(virtual_facts['virtualization_role'], str)
    assert isinstance(virtual_facts['virtualization_system'], str)

# Generated at 2022-06-13 04:10:58.459914
# Unit test for method get_virtual_facts of class NetBSDVirtual

# Generated at 2022-06-13 04:11:01.197656
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    virtual_facts = NetBSDVirtual()
    collector = NetBSDVirtualCollector()
    if collector._platform == 'Linux':
        assert collector._fact_class == virtual_facts

# Generated at 2022-06-13 04:11:02.462816
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual_test = NetBSDVirtual()
    assert virtual_test.platform == 'NetBSD'

# Generated at 2022-06-13 04:11:04.344169
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual_instance = NetBSDVirtual()
    assert netbsd_virtual_instance.platform == 'NetBSD'


# Generated at 2022-06-13 04:11:05.985852
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    x = NetBSDVirtualCollector()
    assert x.platform == 'NetBSD'
    assert x._fact_class == NetBSDVirtual

# Generated at 2022-06-13 04:11:12.379851
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    net_bsd = NetBSDVirtual()
    assert net_bsd.platform == 'NetBSD'
    assert net_bsd.virtualization_type == ''
    assert net_bsd.virtualization_role == ''
    assert net_bsd.virtualization_tech_guest == set()
    assert net_bsd.virtualization_tech_host == set()


# Generated at 2022-06-13 04:11:22.832500
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    virtual_collector = NetBSDVirtualCollector()
    assert virtual_collector.platform == 'NetBSD'
    assert virtual_collector._fact_class == NetBSDVirtual
    assert virtual_collector._fact_class.platform == 'NetBSD'


# Generated at 2022-06-13 04:11:26.146077
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    assert issubclass(NetBSDVirtualCollector, VirtualCollector)
    assert NetBSDVirtualCollector._platform == 'NetBSD'
    assert NetBSDVirtualCollector._fact_class == NetBSDVirtual


# Generated at 2022-06-13 04:11:30.361135
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    """
    Test the method get_virtual_facts of class NetBSDVirtual
    """
    netbsd_virtual = NetBSDVirtual()
    virtual_facts = netbsd_virtual.get_virtual_facts()
    assert isinstance(virtual_facts, dict)
    assert set(('virtualization_type', 'virtualization_role', 'virtualization_technologies')) == set(virtual_facts)

# Generated at 2022-06-13 04:11:31.913704
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual()
    assert netbsd_virtual.platform == 'NetBSD'


# Generated at 2022-06-13 04:11:34.604660
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    obj = NetBSDVirtual()
    assert obj.platform == 'NetBSD'

# Generated at 2022-06-13 04:11:36.218179
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual = NetBSDVirtual()
    assert virtual.platform == 'NetBSD'

# Generated at 2022-06-13 04:11:37.995403
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual({})


# Generated at 2022-06-13 04:11:42.447738
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual_obj = NetBSDVirtual()
    assert virtual_obj.platform == 'NetBSD'
    assert virtual_obj.sysctl_exists('machdep.hypervisor')
    assert virtual_obj.sysctl_exists('machdep.dmi.system-vendor')
    assert virtual_obj.sysctl_exists('machdep.dmi.system-product')
    assert virtual_obj._platform_virtual == 'NetBSD'
    assert virtual_obj._facts_virtual == 'NetBSD'


# Generated at 2022-06-13 04:11:47.813420
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    netbsd_virtual = NetBSDVirtual()

    host_tech = set()
    guest_tech = set()

    # Construct expected results for host_tech and guest_tech
    virtual_vendor_facts = netbsd_virtual.detect_virt_vendor('machdep.dmi.system-vendor')
    guest_tech.update(virtual_vendor_facts['virtualization_tech_guest'])
    host_tech.update(virtual_vendor_facts['virtualization_tech_host'])

    virtual_vendor_facts = netbsd_virtual.detect_virt_vendor('machdep.hypervisor')
    guest_tech.update(virtual_vendor_facts['virtualization_tech_guest'])

# Generated at 2022-06-13 04:11:55.484474
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    facts_obj = NetBSDVirtual({})
    facts = facts_obj.get_virtual_facts()
    assert facts['virtualization_type'] == 'xen'
    assert facts['virtualization_role'] == 'guest'
    assert facts['virtualization_tech_host'] == set(['xen'])
    assert facts['virtualization_tech_guest'] == set(['xen'])

# Generated at 2022-06-13 04:12:09.718552
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual_facts = NetBSDVirtual()
    assert virtual_facts.platform == 'NetBSD'



# Generated at 2022-06-13 04:12:12.585492
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    nvc = NetBSDVirtualCollector()
    assert nvc
    assert nvc._platform == 'NetBSD'
    assert nvc._fact_class == NetBSDVirtual


# Generated at 2022-06-13 04:12:22.267981
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    data = {
        'machdep.dmi.system-product': 'vm',
        'machdep.dmi.system-vendor': 'vmware',
        'machdep.hypervisor': 'vmware',
    }
    platform_values = {
        'Linux': '',
        'FreeBSD': '',
        'OpenBSD': '',
        'NetBSD': 'NetBSD',
        'Windows': '',
    }
    expected_result = {
        'virtualization_type': 'vmware',
        'virtualization_role': 'guest',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': {'vmware'},
    }


# Generated at 2022-06-13 04:12:33.384302
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual import NetBSDVirtual

    class MockModule(object):
        def __init__(self, **kwargs):
            for key, val in kwargs.items():
                setattr(self, key, val)

        def fail_json(self, *args, **kwargs):
            raise Exception()

    class MockFactCollector(object):
        @staticmethod
        def get_sysctl(param):
            if param == 'machdep.dmi.system-product':
                return ['ec2']
            elif param == 'machdep.dmi.system-vendor':
                return ['Amazon EC2']
            elif param == 'machdep.hypervisor':
                return ['Xen']


# Generated at 2022-06-13 04:12:44.837450
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    c = NetBSDVirtual({})
    c.collect_sysctl_facts = lambda: {
        'machdep.dmi.system-vendor': 'VirtualBox',
        'machdep.dmi.system-product': 'VirtualBox',
        'machdep.hypervisor': 'VirtualBox'
    }

    virtual_facts = c.get_virtual_facts()

    assert 'virtualization_type' in virtual_facts
    assert virtual_facts['virtualization_type'] == 'virtualbox'
    assert 'virtualization_role' in virtual_facts
    assert virtual_facts['virtualization_role'] == 'guest'

    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualbox' in virtual_facts['virtualization_tech_guest']
    assert 'virtualization_tech_host' in virtual

# Generated at 2022-06-13 04:12:50.762942
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    # TODO: write unit test for NetBSD if this is possible.
    # The challenge is that no matter what I have tried, I have not been able to
    # get dmidecode to run. It is always saying it cannot open /dev/mem.
    # VirtualSysctlDetectionMixin is impossible to test without dmidecode.
    # A unit test for this class without dmidecode is of little use.
    pass

# Generated at 2022-06-13 04:12:56.163797
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    netbsd_virtual = NetBSDVirtual({}, {}, {})

    assert netbsd_virtual.get_virtual_facts() == {
        'virtualization_type': 'xen',
        'virtualization_role': 'guest',
        'virtualization_tech_guest': set(['xen']),
        'virtualization_tech_host': set(['xen']),
    }

# Generated at 2022-06-13 04:12:56.953368
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    assert NetBSDVirtual({})

# Generated at 2022-06-13 04:12:59.835731
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual = NetBSDVirtual({}, [])
    assert virtual == {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_system': '',
        'virtualization_server': '',
        'virtualization_role': '',
        'virtualization_technologies': set()
    }

# Generated at 2022-06-13 04:13:02.135620
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual_facts = NetBSDVirtual()

    assert netbsd_virtual_facts.platform == 'NetBSD'


# Generated at 2022-06-13 04:13:26.751872
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual_facts_class_instance = NetBSDVirtual()
    virtual_facts_class_instance.sysctl_virtual_facts = dict()

    # Test for NetBSD as guest
    virtual_facts_class_instance.sysctl_virtual_facts['machdep.dmi.system-product'] = 'NetBSD'
    virtual_facts = virtual_facts_class_instance.get_virtual_facts()

    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''
    assert virtual_facts['virtualization_tech_guest'] == set()
    assert virtual_facts['virtualization_tech_host'] == set(['netbsd'])

    # Test for NetBSD as host

# Generated at 2022-06-13 04:13:37.132367
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    netbsd_virtual = NetBSDVirtual()

    sysctl_values = {
        'hw.vendor': 'QEMU',
        'machdep.dmi.system-product': 'Standard PC (i440FX + PIIX, 1996)',
        'machdep.dmi.system-vendor': 'QEMU',
        'machdep.hypervisor': 'qemu'
    }

    virtual_facts = netbsd_virtual.get_virtual_facts(sysctl_values)

    assert virtual_facts['virtualization_type'] == 'qemu'
    assert virtual_facts['virtualization_role'] == 'guest'
    assert virtual_facts['virtualization_product'] == 'Standard PC (i440FX + PIIX, 1996)'

# Generated at 2022-06-13 04:13:39.439240
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    d = NetBSDVirtualCollector()
    assert d._platform == 'NetBSD'
    assert d._fact_class == NetBSDVirtual

# Generated at 2022-06-13 04:13:40.372490
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    assert NetBSDVirtualCollector().platform == 'NetBSD'

# Generated at 2022-06-13 04:13:42.576512
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual()
    assert netbsd_virtual.platform == 'NetBSD'

# Generated at 2022-06-13 04:13:45.592373
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    netBSDVirtualCollector = NetBSDVirtualCollector()
    assert netBSDVirtualCollector._fact_class == NetBSDVirtual
    assert netBSDVirtualCollector._platform == 'NetBSD'

# Generated at 2022-06-13 04:13:51.186952
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual = NetBSDVirtual({'ansible_facts': {}})
    # result when running on a real KVM hypervisor
    assert virtual.get_virtual_facts() == {
        'virtualization_type': '',
        'virtualization_role': ''}


# Generated at 2022-06-13 04:13:53.914686
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    v = NetBSDVirtual({})
    r = v.get_virtual_facts()
    assert r['virtualization_tech_guest'] == set()
    assert r['virtualization_tech_host'] == set()

# Generated at 2022-06-13 04:14:01.028796
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
  # Create an instance of class NetBSDVirtual
  netbsdVirtual = NetBSDVirtual(None)

  # Call method get_virtual_facts
  netbsdVirtual_get_virtual_facts = netbsdVirtual.get_virtual_facts()

  # Assert if Virtualization Type is `None`
  assert netbsdVirtual_get_virtual_facts['virtualization_type'] is not None

  # Assert if Virtualization Role is `None`
  assert netbsdVirtual_get_virtual_facts['virtualization_role'] is not None

# Generated at 2022-06-13 04:14:02.778437
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual_facts_obj = NetBSDVirtual()
    assert virtual_facts_obj.platform == 'NetBSD'

# Generated at 2022-06-13 04:14:38.781054
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    facts = NetBSDVirtual()
    virtual_facts = facts.get_virtual_facts()
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts


# Generated at 2022-06-13 04:14:48.428919
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    fake_module = type('obj', (object,), {'params': {}})
    fake_module.exit_json = lambda v: v

    netbsd_virtual = NetBSDVirtual()
    virtual_facts = netbsd_virtual.get_virtual_facts()
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_technologies' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts
    assert virtual_facts['virtualization_tech_guest'] is not None
    assert virtual_facts['virtualization_tech_host'] is not None

# Generated at 2022-06-13 04:14:51.879458
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    virtual = NetBSDVirtualCollector()
    assert virtual.platform == 'NetBSD'
    assert virtual.get_virtual_facts().keys() == virtual._fact_class.COLLECTION_TO_ATTRS['all'].keys()

# Generated at 2022-06-13 04:14:53.261159
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    virtual_collector = NetBSDVirtualCollector()
    assert virtual_collector is not None

# Generated at 2022-06-13 04:14:58.862879
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    netbsd_virtual = NetBSDVirtual()

    virtual_facts = netbsd_virtual.get_virtual_facts()

    assert virtual_facts['virtualization_type'] == 'kvm'
    assert virtual_facts['virtualization_role'] == 'guest'
    assert virtual_facts['virtualization_tech_host'] == {'kvm', 'qemu'}
    assert virtual_facts['virtualization_tech_guest'] == {'kvm', 'qemu', 'qemu-kvm'}

# Generated at 2022-06-13 04:15:01.955376
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    c = NetBSDVirtualCollector()
    assert c.platform == 'NetBSD'
    assert c._fact_class == NetBSDVirtual


# Generated at 2022-06-13 04:15:03.186685
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    # To be implemented
    return True


# Generated at 2022-06-13 04:15:07.497923
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.netbsd import NetBSDVirtual
    import os, sys
    import unittest

    # Workaround for AnsibleBug for Python 2.6 and 2.7
    # https://github.com/ansible/ansible/issues/20189
    try:
        from mock import patch
    except ImportError:
        from unittest.mock import patch

    # Test Case 1: get_virtual_facts() returns the correct dictonary
    #              when machdep.dmi.system-product is set to 'Bochs'

# Generated at 2022-06-13 04:15:09.610612
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    assert NetBSDVirtualCollector._platform == 'NetBSD'
    assert NetBSDVirtualCollector._fact_class == NetBSDVirtual


# Generated at 2022-06-13 04:15:12.715717
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    collector = NetBSDVirtualCollector()

    # Test the instance of class NetBSDVirtualCollector
    assert isinstance(collector, NetBSDVirtualCollector)


# Generated at 2022-06-13 04:16:26.020547
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    from ansible.module_utils.facts.collector import VirtualCollector
    virtual_collector = VirtualCollector
    for name, obj in list(virtual_collector.__dict__.items()):
        if hasattr(obj, '__bases__'):
            assert NetBSDVirtualCollector in obj.__bases__

# Generated at 2022-06-13 04:16:35.171783
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsdvirtual = NetBSDVirtual()
    assert netbsdvirtual.platform == 'NetBSD'
    assert 'virtualization_type' in netbsdvirtual.facts
    assert 'virtualization_role' in netbsdvirtual.facts
    assert 'virtualization_system' in netbsdvirtual.facts
    assert 'virtualization_hypervisor' in netbsdvirtual.facts
    assert 'virtualization_product_name' in netbsdvirtual.facts
    assert 'virtualization_product_version' in netbsdvirtual.facts
    assert 'virtualization_product_serial' in netbsdvirtual.facts
    assert 'virtualization_product_uuid' in netbsdvirtual.facts

# Generated at 2022-06-13 04:16:36.982718
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    module = AnsibleModule(argument_spec={})
    v = NetBSDVirtual(module)
    assert v.get_virtual_facts()


# Generated at 2022-06-13 04:16:37.731280
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    assert NetBSDVirtualCollector



# Generated at 2022-06-13 04:16:38.799904
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    assert NetBSDVirtualCollector._platform == NetBSDVirtual.platform


# Generated at 2022-06-13 04:16:44.529658
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual = NetBSDVirtual()
    virtual_facts = virtual.get_virtual_facts()
    expected_virtual_facts = {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set()
    }

    assert virtual_facts == expected_virtual_facts

# Generated at 2022-06-13 04:16:49.898240
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    virtual_collector = NetBSDVirtualCollector()
    # Confirm that object is of class NetBSDVirtualCollector, or a subclass
    assert isinstance(virtual_collector, NetBSDVirtualCollector)
    # Confirm that object is of class VirtualCollector, or a subclass
    assert isinstance(virtual_collector, VirtualCollector)
    # Confirm that object is of class BaseVirtualCollector, or a subclass
    assert isinstance(virtual_collector, VirtualCollector)


# Generated at 2022-06-13 04:17:00.507668
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    instance = NetBSDVirtual({})
    instance.sysctl_facts = {'hw.product': 'iMac14,2',
                              'hw.machine': 'amd64',
                              'machdep.dmi.system-product': 'iMac14,2',
                              'machdep.dmi.system-vendor': 'Apple Inc.',
                              'machdep.hypervisor': 'XEN',
                             }
    assert instance.get_virtual_facts() == {
        'virtualization_type': 'xen',
        'virtualization_role': 'guest',
        'virtualization_tech_guest': set(['xen']),
        'virtualization_tech_host': set(['xen']),
    }

# Generated at 2022-06-13 04:17:03.931547
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual_fact = NetBSDVirtual()
    assert isinstance(virtual_fact._platform, str) == True
    assert isinstance(virtual_fact._fact_class, bool) == False


# Generated at 2022-06-13 04:17:05.646275
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual = NetBSDVirtual(None)
    assert virtual.platform == 'NetBSD'


# Generated at 2022-06-13 04:19:48.267509
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    # Specify a dictionary containing key, value pairs
    # of the sysctl variables to be returned from
    # the VirtualNetBSD class method get_sysctl_facts
    sysctl_facts = {}

    # key: machdep.dmi.system-vendor
    # value: a string identifying the virtualization product
    #        or platform eg. 'KVM' or 'VMware'
    sysctl_facts['machdep.dmi.system-vendor'] = 'GNU/kFreeBSD'

    # key: machdep.dmi.system-product
    # value: a string identifying the virtualization product
    #        or platform eg. 'KVM' or 'VMware'
    sysctl_facts['machdep.dmi.system-product'] = 'Debian GNU/kFreeBSD'

    # key: machdep.hypervisor