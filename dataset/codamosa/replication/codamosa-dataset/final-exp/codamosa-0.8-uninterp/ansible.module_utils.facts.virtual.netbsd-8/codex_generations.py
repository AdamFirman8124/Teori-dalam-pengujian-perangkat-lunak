

# Generated at 2022-06-13 04:09:59.166342
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    def _read(filename):
        return ''
    expected_virtual_facts = {'virtualization_type': '', 'virtualization_role': '', 'virtualization_technologies_guest': set([]), 'virtualization_technologies_host': set([])}
    netbsd_virtual = NetBSDVirtual(None, None, _read)
    virtual_facts = netbsd_virtual.get_virtual_facts()
    assert virtual_facts == expected_virtual_facts
    netbsd_virtual.get_virtual_facts = get_virtual_facts
    virtual_facts = netbsd_virtual.get_virtual_facts()
    assert virtual_facts['virtualization_role'] == 'guest'
    assert virtual_facts['virtualization_type'] == 'xen'

# Generated at 2022-06-13 04:10:05.276103
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():

    # Get a NetBSDVirtual object from the factory
    netbsd_virtual_obj = NetBSDVirtual()

    # Check if the object is a NetBSDVirtual object
    assert isinstance(netbsd_virtual_obj, NetBSDVirtual)

    # Check if the inheritence is correct
    assert issubclass(NetBSDVirtual, Virtual)
    assert issubclass(NetBSDVirtual, VirtualSysctlDetectionMixin)

# Generated at 2022-06-13 04:10:08.049661
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsdvirtual = NetBSDVirtual()

    assert netbsdvirtual._platform == 'NetBSD'
    assert netbsdvirtual.platform == 'NetBSD'
    assert netbsdvirtual._fact_class == NetBSDVirtual
    assert netbsdvirtual.get_virtual_facts() == {}

# Generated at 2022-06-13 04:10:09.953713
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual = NetBSDVirtual()
    virtual_facts = virtual.get_virtual_facts()
    assert virtual_facts['virtualization_tech_host'] == set()
    assert virtual_facts['virtualization_tech_guest'] == set()

# Generated at 2022-06-13 04:10:12.791133
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    virtual_facts = NetBSDVirtualCollector().collect()
    assert virtual_facts['virtualization_type'] == 'xen'
    assert virtual_facts['virtualization_role'] == 'guest'

# Generated at 2022-06-13 04:10:18.223385
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual()
    assert netbsd_virtual.collect() == {
        'virtualization_role': '',
        'virtualization_type': '',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set(),
    }

# Generated at 2022-06-13 04:10:27.032397
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    has_xen = os.path.exists('/dev/xencons')

    virtual = NetBSDVirtual()
    virtual_facts = virtual.get_virtual_facts()

    assert virtual_facts['virtualization_tech_guest'] == set(['xen']) if has_xen else set([])
    assert virtual_facts['virtualization_tech_host'] == set([])
    assert virtual_facts['virtualization_type'] == 'xen' if has_xen else ''
    assert virtual_facts['virtualization_role'] == 'guest' if has_xen else ''

# Generated at 2022-06-13 04:10:34.936206
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    # NetBSD Virtual facts should not be detected on non-NetBSD platforms
    with open('tests/unittests/module_utils/facts/virtual/netbsd/machdep.dmi.system-product', 'wb') as f:
        f.write(b'')
    with open('tests/unittests/module_utils/facts/virtual/netbsd/machdep.dmi.system-vendor', 'wb') as f:
        f.write(b'')
    nv = NetBSDVirtual(module=None)
    with open('/etc/os-release', 'wb') as f:
        f.write(b'NAME=NotBSD\nID=notbsd\n')
    assert not nv.get_virtual_facts()

    # NetBSD Virtual facts should be detected on NetBSD platforms

# Generated at 2022-06-13 04:10:38.225155
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    '''Unit test for constructor of class NetBSDVirtualCollector'''
    collector = NetBSDVirtualCollector()
    assert isinstance(collector, NetBSDVirtualCollector)


# Generated at 2022-06-13 04:10:49.880490
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    # Create object
    obj = NetBSDVirtual()

    # Test when machdep.hypervisor is xhyve
    sim_data = {
        'machdep.hypervisor': 'xhyve',
    }
    obj.sysctl.add_all_data(sim_data)

    # Test when machdep.dmi.system-vendor is VMware, Inc.
    sim_data = {
        'machdep.dmi.system-vendor': 'VMware, Inc.',
    }
    obj.sysctl.add_all_data(sim_data)

    # Test when machdep.dmi.system-product is VMware Virtual Platform
    sim_data = {
        'machdep.dmi.system-product': 'VMware Virtual Platform',
    }

# Generated at 2022-06-13 04:10:54.712027
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    _fact_class = NetBSDVirtualCollector()._fact_class
    assert _fact_class == NetBSDVirtual

# Generated at 2022-06-13 04:10:56.842569
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual()
    assert NetBSDVirtual._platform == 'NetBSD'


# Generated at 2022-06-13 04:11:06.106253
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    # Create sample sysctl output that matches the output used by this
    # class to detect virtual machine guests and hosts.
    sample_sysctl_output = {
        'machdep.dmi.system-vendor': 'Xen',
        'machdep.dmi.system-product': 'HVM domU',
        'machdep.hypervisor': 'Xen',
    }

    # Create a NetBSDVirtual object and set its sysctl_all property
    # to the sample output.
    virtual = NetBSDVirtual({}, sample_sysctl_output, [])

    # Get the virtual facts for this NetBSDVirtual object.
    virtual_facts = virtual.get_virtual_facts()

    # These are the virtual facts we expect to see.

# Generated at 2022-06-13 04:11:08.549309
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    assert isinstance(NetBSDVirtual(), Virtual)


# Generated at 2022-06-13 04:11:14.013027
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual_facts = NetBSDVirtual()
    assert virtual_facts.get_virtual_facts()['virtualization_type'] is ''
    assert virtual_facts.get_virtual_facts()['virtualization_role'] is ''
    assert virtual_facts.get_virtual_facts()['virtualization_tech_guest'] is not ''
    assert virtual_facts.get_virtual_facts()['virtualization_tech_host'] is not ''

# Generated at 2022-06-13 04:11:19.698625
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual = NetBSDVirtual()

    assert virtual.get_virtual_facts() == {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_product': '',
        'virtualization_systems': {},
    }

# Generated at 2022-06-13 04:11:22.247383
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual()
    assert netbsd_virtual.platform == 'NetBSD'


# Generated at 2022-06-13 04:11:23.947968
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    v = NetBSDVirtual()
    assert v.platform == 'NetBSD'

# Generated at 2022-06-13 04:11:26.145870
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual()
    assert netbsd_virtual.platform == 'NetBSD'


# Generated at 2022-06-13 04:11:28.152242
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsdv = NetBSDVirtual(None, None)
    assert netbsdv.platform == "NetBSD"


# Generated at 2022-06-13 04:11:37.549565
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    '''Unit test for constructor of class NetBSDVirtual'''
    vf = NetBSDVirtual()
    assert(vf.platform == 'NetBSD')


# Generated at 2022-06-13 04:11:42.034559
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    instance = NetBSDVirtual()
    assert instance.platform == 'NetBSD'

# Generated at 2022-06-13 04:11:51.614029
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual = NetBSDVirtual()

    with open('/proc/sys/dev/sensors/sensors0/temp0_input', 'w') as f:
        f.write('0')

    with open('/proc/sys/dev/sensors/sensors0/temp0_type', 'w') as f:
        f.write('KTCT-959-TZ')

    with open('/proc/sys/dev/sensors/sensors0/temp0_label', 'w') as f:
        f.write('CPU')

    with open('/proc/sys/dev/sensors/sensors0/temp2_input', 'w') as f:
        f.write('353')


# Generated at 2022-06-13 04:11:52.648885
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual = NetBSDVirtual(module=None)
    assert virtual.platform == 'NetBSD'

# Generated at 2022-06-13 04:11:58.174305
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    facts = NetBSDVirtual()
    virtual_facts = facts.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''
    assert virtual_facts['virtualization_technology'] == ''
    assert virtual_facts['virtualization_type_role'] == ''
    assert len(virtual_facts['virtualization_tech_guest']) == 0
    assert len(virtual_facts['virtualization_tech_host']) == 0

# Generated at 2022-06-13 04:12:04.097795
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from facts.virtual.netbsd import NetBSDVirtual

    netbsd_virtual_instance = NetBSDVirtual()

    assert netbsd_virtual_instance.platform == 'NetBSD'


# Generated at 2022-06-13 04:12:04.968561
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    virtual_collector = NetBSDVirtualCollector()
    assert virtual_collector is not None


# Generated at 2022-06-13 04:12:05.597228
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    NetBSDVirtual()

# Generated at 2022-06-13 04:12:08.375612
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    obj = NetBSDVirtual()
    assert obj.platform == 'NetBSD'
    assert obj.guests is None
    assert obj.hypervisor is None

# Generated at 2022-06-13 04:12:11.736709
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsdvirtual = NetBSDVirtual()

    # Test for NetBSD virtual facts
    assert netbsdvirtual.get_virtual_facts() == netbsdvirtual.get_all_facts()['ansible_virtual']

# Generated at 2022-06-13 04:12:27.862385
# Unit test for constructor of class NetBSDVirtualCollector

# Generated at 2022-06-13 04:12:29.960120
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    test_object = NetBSDVirtual(given_facts={})
    assert test_object.platform == 'NetBSD'


# Generated at 2022-06-13 04:12:31.754233
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual_facts = NetBSDVirtual()
    assert virtual_facts.platform == 'NetBSD'


# Generated at 2022-06-13 04:12:38.133475
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():

    virtual_facts = {
        "virtualization_role": "",
        "virtualization_type": "",
        "virtualization_tech_host": {},
        "virtualization_tech_guest": {},
    }
    assert NetBSDVirtual(module=None).get_virtual_facts() == virtual_facts

# Generated at 2022-06-13 04:12:40.298689
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsdvirtual = NetBSDVirtual()
    assert netbsdvirtual.platform == 'NetBSD'

# Generated at 2022-06-13 04:12:43.222991
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    collector = NetBSDVirtualCollector()
    facts = collector.get_virtual_facts()

    assert facts['virtualization_role'] == 'guest'
    assert facts['virtualization_type'] == 'xen'

# Generated at 2022-06-13 04:12:44.853393
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual()
    assert netbsd_virtual.platform == 'NetBSD'

# Generated at 2022-06-13 04:12:48.081046
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    netbsd_virtual_collector = NetBSDVirtualCollector()
    assert netbsd_virtual_collector._fact_class == NetBSDVirtual
    assert netbsd_virtual_collector._platform == 'NetBSD'

# Generated at 2022-06-13 04:12:51.288572
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual_facts = NetBSDVirtualCollector().get_virtual_facts()
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts

# Generated at 2022-06-13 04:12:53.573796
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    netbsd_virtual_collector = NetBSDVirtualCollector()
    assert netbsd_virtual_collector._fact_class.__name__ == 'NetBSDVirtual'
    assert netbsd_virtual_collector._platform == 'NetBSD'



# Generated at 2022-06-13 04:13:23.203527
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    # Constructor of class NetBSDVirtual
    virt = NetBSDVirtual()

    # Constructor of class VirtualCollector
    virt_col = NetBSDVirtualCollector()

    assert virt_col._fact_class == virt.__class__
    assert virt_col._platform == 'NetBSD'

# Generated at 2022-06-13 04:13:27.080995
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd = NetBSDVirtual({})

    # Check that we are overriding the correct methods and properties
    assert netbsd.platform == 'NetBSD'
    assert netbsd.get_virtual_facts.__func__ == NetBSDVirtual.get_virtual_facts.__func__



# Generated at 2022-06-13 04:13:32.015507
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    os_facts = {}
    os_facts['kernel'] = 'NetBSD'
    os_facts['kernel_version'] = '7.0_STABLE'
    os_facts['os_family'] = 'OpenBSD'
    os_facts['distribution'] = 'OpenBSD'
    NetBSDVirtual(os_facts, None)

# Generated at 2022-06-13 04:13:34.225166
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual_facts = NetBSDVirtual().get_virtual_facts()
    assert not virtual_facts['virtualization_type']
    assert not virtual_facts['virtualization_role']

# Generated at 2022-06-13 04:13:37.801212
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual(None)
    netbsd_virtual.get_virtual_facts()
    assert netbsd_virtual.platform == 'NetBSD'

# Generated at 2022-06-13 04:13:42.185274
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    sut = NetBSDVirtualCollector()

    assert str(sut) == '<NetBSDVirtualCollector(NetBSDVirtual)>'
    assert isinstance(sut.platform, str)
    assert isinstance(sut._fact_class, NetBSDVirtual)
    assert isinstance(sut._platform, str)

# Generated at 2022-06-13 04:13:48.035578
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual_facts = NetBSDVirtual().get_virtual_facts()
    assert isinstance(virtual_facts, dict)
    assert list(virtual_facts.keys()) == ['virtualization_type', 'virtualization_role', 'virtualization_tech_guest', 'virtualization_tech_host']
    assert isinstance(virtual_facts['virtualization_type'], str)
    assert isinstance(virtual_facts['virtualization_role'], str)
    assert isinstance(virtual_facts['virtualization_tech_guest'], set)
    assert isinstance(virtual_facts['virtualization_tech_host'], set)

# Generated at 2022-06-13 04:13:58.229083
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual import BaseVirtual
    from ansible.module_utils.facts.virtual import VirtualCollector

    from ansible.module_utils.facts.virtual.netbsd import NetBSDVirtual
    from ansible.module_utils.facts.virtual.netbsd import NetBSDVirtualCollector

    BaseVirtual.declarative_facts_constructors = []
    VirtualCollector.collectors = []

    BaseVirtual.register_virtual_collector_class(NetBSDVirtualCollector)
    facts_dict = NetBSDVirtual().get_virtual_facts()

    assert facts_dict.get('virtualization_type') == 'Parallels'
    assert facts_dict['virtualization_role'] == 'guest'

# Generated at 2022-06-13 04:13:59.427781
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    v = NetBSDVirtual(None)
    assert v._platform == 'NetBSD'

# Generated at 2022-06-13 04:14:03.232236
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    '''
    Test NetBSDVirtualCollector constructor
    '''
    netbsd_virtual = NetBSDVirtualCollector()
    assert netbsd_virtual
    assert isinstance(netbsd_virtual, NetBSDVirtualCollector)

# Generated at 2022-06-13 04:15:05.154908
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    netbsd_virtual_collector = NetBSDVirtualCollector()
    assert netbsd_virtual_collector._platform == 'NetBSD'
    assert netbsd_virtual_collector._fact_class.platform == 'NetBSD'
    assert netbsd_virtual_collector._fact_class.__name__ == 'NetBSDVirtual'

# Generated at 2022-06-13 04:15:11.435761
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    sysctl_data = {
        'hw.model': 'AMD Athlon(tm) II X4 640 Processor',
        'machdep.dmi.system-product': 'To Be Filled By O.E.M.',
        'machdep.dmi.system-vendor': 'To Be Filled By O.E.M.',
        'machdep.hypervisor': ''
    }

    netbsd_virtual = NetBSDVirtual(sysctl_data=sysctl_data)
    facts = netbsd_virtual.get_virtual_facts()
    assert 'vmware' in facts['virtualization_type']
    assert 'guest' in facts['virtualization_role']



# Generated at 2022-06-13 04:15:13.183127
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual()
    assert netbsd_virtual.platform == 'NetBSD'

# Generated at 2022-06-13 04:15:13.861603
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    NetBSDVirtual({})



# Generated at 2022-06-13 04:15:15.889461
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    # Set up object and call constructor
    NetBSDVirtual_object = NetBSDVirtual()

    # Assert the correct platform
    assert NetBSDVirtual_object.platform == 'NetBSD'

# Generated at 2022-06-13 04:15:18.735809
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    """ get_virtual_facts() is a method of NetBSDVirtual class """
    # Test empty case
    virtual_facts = NetBSDVirtual({'kernel': ''}).get_virtual_facts()

    assert virtual_facts['virtualization_role'] == ''
    assert virtual_facts['virtualization_type'] == ''

# Generated at 2022-06-13 04:15:21.922603
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    netbsd_virtual = NetBSDVirtual(module=None)
    netbsd_virtual.get_virtual_facts()
    assert len(netbsd_virtual.virtual_facts) > 0

# Generated at 2022-06-13 04:15:23.633459
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virt_obj = NetBSDVirtual()
    assert virt_obj.platform == 'NetBSD'

# Generated at 2022-06-13 04:15:34.121858
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual import NetBSDVirtual
    from ansible.module_utils.facts.virtual.base import VirtualCollector

    # Set up mocks for get_file_lines method of VirtualCollector class
    class VirtualCollectorMock(VirtualCollector):
        def __init__(self, platform=None, sysctl=None):
            pass

        def get_file_lines(self, path):
            return lines

    # Test empty output of get_file_lines
    nv = NetBSDVirtual(VirtualCollectorMock())
    virtual_facts = nv.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''
    assert virtual_facts['virtualization_tech_host'] == set()

# Generated at 2022-06-13 04:15:42.165191
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    facts_obj = NetBSDVirtual()
    # On NetBSD, we have 2 cases to be tested:
    #
    # case 1: machdep.dmi.system-vendor: VMware, Inc.
    #   Expected result = virtualization_type: vmware, virtualization_role: guest
    # case 2: machdep.hypervisor: Xen
    #   Expected result = virtualization_type: xen, virtualization_role: guest
    # case 3: machdep.hypervisor: None/Empty
    #   Expected result = virtualization_type: ''

# Generated at 2022-06-13 04:18:11.203875
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual_facts = NetBSDVirtual()
    assert virtual_facts._platform == 'NetBSD'
    assert virtual_facts._fact_class.__name__ == 'NetBSDVirtual'

# Generated at 2022-06-13 04:18:13.948712
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    """
    Parameterized constructor test for NetBSDVirtualCollector

    """
    instance = NetBSDVirtualCollector()
    assert type(instance) == NetBSDVirtualCollector

# Generated at 2022-06-13 04:18:15.750990
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    NetBSDVirtual.get_virtual_facts()

# Generated at 2022-06-13 04:18:18.137660
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual({}, {}, None, {})
    assert(netbsd_virtual.platform == 'NetBSD')


# Generated at 2022-06-13 04:18:19.219977
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual_facts = NetBSDVirtual()
    assert virtual_facts.platform == 'NetBSD'

# Generated at 2022-06-13 04:18:19.755137
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual = NetBSDVirtual()
    assert virtual._platform == "NetBSD"

# Generated at 2022-06-13 04:18:21.301960
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual = NetBSDVirtual({}, None)
    assert virtual.platform == 'NetBSD'

# Generated at 2022-06-13 04:18:24.765198
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd = NetBSDVirtual()
    assert isinstance(netbsd, NetBSDVirtual)

# Generated at 2022-06-13 04:18:26.955193
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual_facts = NetBSDVirtual()
    assert virtual_facts.platform == 'NetBSD'


# Generated at 2022-06-13 04:18:28.511733
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    netbsd_facts = NetBSDVirtualCollector()
    assert netbsd_facts._platform == 'NetBSD'