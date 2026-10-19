

# Generated at 2022-06-13 04:09:56.985942
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual_facts = NetBSDVirtual().get_virtual_facts()
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts
    assert isinstance(virtual_facts['virtualization_tech_guest'], set)
    assert isinstance(virtual_facts['virtualization_tech_host'], set)

# Generated at 2022-06-13 04:10:01.316773
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    nbc = NetBSDVirtualCollector()
    assert nbc._platform == 'NetBSD'
    assert nbc._fact_class == NetBSDVirtual


# Generated at 2022-06-13 04:10:07.498357
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual_facts_dict = {'virtualization_role': 'guest',
                          'virtualization_type': 'vserver',
                          'virtualization_tech_guest': set(),
                          'virtualization_tech_host': set()}

    virtual_mock = NetBSDVirtual()
    virtual_mock.get_virtual_facts = lambda: virtual_facts_dict
    virtual_mock.collect()

    assert virtual_mock.virtual == virtual_facts_dict


# Generated at 2022-06-13 04:10:08.017113
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
        NetBSDVirtual()

# Generated at 2022-06-13 04:10:08.783455
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual = NetBSDVirtual(None)
    assert isinstance(virtual, NetBSDVirtual)

# Generated at 2022-06-13 04:10:11.418699
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual = NetBSDVirtual({})
    virtual_facts = virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'virtualbox'
    assert virtual_facts['virtualization_role'] == 'guest'
    assert virtual_facts['virtualization_tech_host'] == set()
    assert virtual_facts['virtualization_tech_guest'] == set()

# Generated at 2022-06-13 04:10:12.829951
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual = NetBSDVirtual(None)
    assert virtual



# Generated at 2022-06-13 04:10:14.944782
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virt = NetBSDVirtual({})

    assert virt.get_virtual_facts() == {}
    assert virt.platform == 'NetBSD'

# Generated at 2022-06-13 04:10:16.913538
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual_facts = NetBSDVirtual()
    assert virtual_facts.platform == 'NetBSD'

# Generated at 2022-06-13 04:10:20.061356
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
	assert NetBSDVirtualCollector._platform=='NetBSD', "Constructor of class NetBSDVirtualCollector test failed"


# Generated at 2022-06-13 04:10:32.884819
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():

    from ansible.module_utils.facts.virtual.netbsd import VirtualFacts
    from ansible.module_utils.facts.virtual.netbsd import VirtualFactsCollector
    from ansible.module_utils.facts.collector import FactsCollector

    collector = VirtualFactsCollector(FactsCollector())
    virtual_facts = VirtualFacts(collector)

    virtual_facts.sysctl = {
        'machdep.dmi.system-product': 'VirtualBox',
        'machdep.dmi.system-vendor': 'innotek GmbH',
        'machdep.hypervisor': '',
    }

    facts = virtual_facts.get_virtual_facts()

    assert facts['virtualization_type'] == 'VirtualBox', "Type should be VirtualBox"

# Generated at 2022-06-13 04:10:34.391024
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    assert NetBSDVirtualCollector._platform == 'NetBSD'
    assert NetBSDVirtualCollector._fact_class == NetBSDVirtual


# Generated at 2022-06-13 04:10:35.601630
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    facts = NetBSDVirtualCollector()
    assert facts._platform == 'NetBSD'
    assert facts._fact_class == NetBSDVirtual

# Generated at 2022-06-13 04:10:37.154636
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    nbsdCollector = NetBSDVirtualCollector()
    assert nbsdCollector is not None

# Generated at 2022-06-13 04:10:41.859472
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual_facts = NetBSDVirtual({}).get_virtual_facts()
    assert isinstance(virtual_facts, dict)
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts

# Generated at 2022-06-13 04:10:44.468010
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual()
    assert netbsd_virtual.platform == 'NetBSD'

# Generated at 2022-06-13 04:10:46.800137
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual_facts = NetBSDVirtual(None).get_virtual_facts()
    print(virtual_facts['virtualization_type'])


# Generated at 2022-06-13 04:10:55.516002
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual_facts = NetBSDVirtual(None)
    host_virtual_facts = virtual_facts.get_virtual_facts()
    host_virtual_type = host_virtual_facts['virtualization_type']
    host_virtual_role = host_virtual_facts['virtualization_role']
    host_virtual_tech_guest = host_virtual_facts['virtualization_tech_guest']
    host_virtual_tech_host = host_virtual_facts['virtualization_tech_host']

    assert host_virtual_type == 'physical' or host_virtual_type == ''
    assert host_virtual_role == 'host' or host_virtual_role == ''
    assert host_virtual_tech_guest == set()
    assert host_virtual_tech_host == set()

# Generated at 2022-06-13 04:11:05.495935
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    import platform
    module_utils = platform.system() + '.' + platform.machine() + '.module_utils'
    setattr(__import__(module_utils, globals(), locals(), ['module_utils']), 'open_fw', lambda x: '')
    setattr(__import__(module_utils, globals(), locals(), ['module_utils']), 'sysctl', lambda x: x)
    setattr(__import__(module_utils, globals(), locals(), ['module_utils']), 'read_file', lambda x: x)
    setattr(__import__(module_utils, globals(), locals(), ['module_utils']), 'file_exists', lambda x: True)
    setattr(__import__(module_utils, globals(), locals(), ['module_utils']), 'which', lambda x: True)
    setattr

# Generated at 2022-06-13 04:11:08.043462
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virt = NetBSDVirtualCollector(None)
    assert virt.platform == 'NetBSD'

# Generated at 2022-06-13 04:11:18.222254
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual()
    assert netbsd_virtual.platform == 'NetBSD'

# Generated at 2022-06-13 04:11:20.858346
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    from ansible.module_utils.facts.virtual.netbsd import NetBSDVirtual as NetBSDVirtualModule

    netbsd_virtual = NetBSDVirtualModule()
    assert netbsd_virtual.platform == 'NetBSD'

# Generated at 2022-06-13 04:11:22.298357
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    NetBSDVirtualCollector()

# Generated at 2022-06-13 04:11:24.422740
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    netbsd_virtual_collector = NetBSDVirtualCollector()
    assert netbsd_virtual_collector is not None

# Generated at 2022-06-13 04:11:32.698201
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    from sys import version_info
    if version_info.major == 2:
        import __builtin__ as builtins  # pylint: disable=import-error
    else:
        import builtins
    netbsd_virtual = NetBSDVirtual(module=None)
    test_dict = {'machdep.dmi.system-product': 'Bochs',
                 'machdep.dmi.system-vendor': 'Bochs',
                 'machdep.hypervisor': '',
                 }
    with open('/proc/sys/') as patched_sysctl:
        setattr(builtins, 'open', lambda *args, **kwargs: patched_sysctl)
        setattr(netbsd_virtual, '_sysctl', lambda param: test_dict[param])
        virtual_facts = netbsd_

# Generated at 2022-06-13 04:11:34.604248
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    assert NetBSDVirtual()


# Generated at 2022-06-13 04:11:36.685640
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd = NetBSDVirtual()
    assert netbsd is not None



# Generated at 2022-06-13 04:11:38.361774
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virt = NetBSDVirtual({})
    assert virt._platform == 'NetBSD'

# Generated at 2022-06-13 04:11:45.792378
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    # Call the constructor of class NetBSDVirtual
    netbsd = NetBSDVirtual()

    # Test virtualization_type is '', virtualization_role is ''
    assert netbsd.virtual_info['virtualization_type'] == ''
    assert netbsd.virtual_info['virtualization_role'] == ''

# Generated at 2022-06-13 04:11:47.495812
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd = NetBSDVirtual()
    assert netbsd is not None


# Generated at 2022-06-13 04:12:11.687111
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.netbsd import NetBSDVirtual

    fixture_path = os.path.join(os.path.dirname(__file__), 'unit/fixtures/')
    fixture_file = open(fixture_path + 'machdep.dmi.system-vendor_HVM_domU')
    data = fixture_file.read()
    fixture_file.close()

    detected_virtual_facts = {}

    set_module_args({'sysctl_data': data})
    virtual_facts = NetBSDVirtual()
    detected_virtual_facts = virtual_facts.get_virtual_facts()

    assert detected_virtual_facts['virtualization_role'] == 'guest'
    assert detected_virtual_facts['virtualization_type'] == 'xen'

# Generated at 2022-06-13 04:12:14.580971
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual_module = NetBSDVirtual()
    assert netbsd_virtual_module.platform == 'NetBSD'


# Generated at 2022-06-13 04:12:16.373506
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual_facts = NetBSDVirtual()
    assert virtual_facts._platform == "NetBSD"


# Generated at 2022-06-13 04:12:18.938497
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual()
    assert netbsd_virtual.platform == 'NetBSD'
    assert netbsd_virtual.get_virtual_facts() == {}



# Generated at 2022-06-13 04:12:19.644037
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    assert NetBSDVirtual().get_virtual_facts()['virtualization_type'] == ''

# Generated at 2022-06-13 04:12:25.341890
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual_obj = NetBSDVirtual()
    virtual_obj.sysctl = lambda x: 'NetBSD' if x == 'machdep.dmi.system-vendor' else ''
    virtual_obj.get_virtual_facts()
    virtual_obj.sysctl = lambda x: ''
    virtual_obj.get_virtual_facts()


# Generated at 2022-06-13 04:12:34.344878
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    netbsd_virtual = NetBSDVirtual("")

    # Testing machdep.dmi.system-product and machdep.dmi.system-vendor
    machdep_dmi_result = {
        "machdep.dmi.system-product": "OpenStack Nova",
        "machdep.dmi.system-vendor": "OpenStack Foundation"
    }
    expected_results = {
        'virtualization_type': 'openstack',
        'virtualization_role': 'guest',
        'virtualization_tech_host': set(),
        'virtualization_tech_guest': {'openstack'}
    }
    virtualization_facts = netbsd_virtual.get_virtual_facts(machdep_dmi_result)
    assert virtualization_facts == expected_results

    # Testing machdep.hyper

# Generated at 2022-06-13 04:12:40.505590
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    expected_virtual_platform_facts = {'virtualization_type': 'openvz', 'virtualization_role': 'guest',
                                       'virtualization_tech_guest': set(['openvz'])}

    platform = NetBSDVirtual()
    virtual_platform_facts = platform.collect()

    assert virtual_platform_facts == expected_virtual_platform_facts


# Generated at 2022-06-13 04:12:42.276061
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual()
    assert netbsd_virtual.platform == 'NetBSD'

# Generated at 2022-06-13 04:12:43.953687
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual = NetBSDVirtual()
    assert virtual.platform == 'NetBSD'

# Generated at 2022-06-13 04:13:19.640683
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    assert NetBSDVirtualCollector._platform == 'NetBSD'
    assert NetBSDVirtualCollector._fact_class._platform == 'NetBSD'
    assert NetBSDVirtualCollector._fact_class._fact_class == Virtual
    assert NetBSDVirtualCollector._fact_class._fact_class.platform == 'Base'
    assert NetBSDVirtualCollector._fact_class._virtualization_type_facts == []
    assert NetBSDVirtualCollector._fact_class._virtualization_type_trie is None
    assert NetBSDVirtualCollector._fact_class._virtualization_role_facts == []
    assert NetBSDVirtualCollector._fact_class._virtualization_role_trie is None
    assert NetBSDVirtualCollector._fact_class._virtualization_tech_facts == []
    assert NetBSDVirtualCollector._fact_class._virtualization_tech_t

# Generated at 2022-06-13 04:13:25.293339
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual = NetBSDVirtual()
    facts = virtual.collect()

    assert 'virtualization_type' in facts
    assert 'virtualization_role' in facts
    assert 'virtualization_tech_guest' in facts
    assert 'virtualization_tech_host' in facts

    assert facts['virtualization_type'] in ('', 'xen')

    assert facts['virtualization_role'] in ('', 'guest')

# Generated at 2022-06-13 04:13:31.309115
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    test_collector = NetBSDVirtualCollector()
    test_class = test_collector._fact_class()
    test_class.sysctl = dict(machdep_dmi_system_product='VirtualBox')
    test_class.sysctl = dict(machdep_dmi_system_vendor='innotek GmbH')
    guest_tech_set = set()
    guest_tech_set.add('xen')
    virtual_facts = dict(
        virtualization_type='xen',
        virtualization_role='guest',
        virtualization_tech_guest=guest_tech_set
    )
    assert virtual_facts == test_class.get_virtual_facts()

# Generated at 2022-06-13 04:13:33.163603
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual(module=None)
    assert netbsd_virtual.platform == 'NetBSD'


# Generated at 2022-06-13 04:13:39.260823
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    # Facts dictionary
    facts = {}
    # Expected results dictionary
    results = {'virtualization_type': '',
               'virtualization_role': '',
               'virtualization_tech_guest': set(),
               'virtualization_tech_host': set()}

    netbsd = NetBSDVirtual(module=None)
    netbsd.populate()
    facts.update(netbsd.get_virtual_facts())

    assert facts == results

# Generated at 2022-06-13 04:13:43.127780
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    """ Test the constructor of class NetBSDVirtual """
    netbsd_virtual = NetBSDVirtual()
    assert isinstance(netbsd_virtual, NetBSDVirtual) and isinstance(netbsd_virtual, Virtual)
    assert netbsd_virtual.platform == 'NetBSD'

# Generated at 2022-06-13 04:13:49.547446
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():

    netbsd_virtual = NetBSDVirtual()

    def mock_read_file_from_sysctl_if_exists(key):
        if key == 'machdep.dmi.system-product':
            return 'KVM'
        elif key == 'machdep.dmi.system-vendor':
            return 'Red Hat'
        else:
            raise IOError('No such file or directory')

    netbsd_virtual.read_file_from_sysctl_if_exists = mock_read_file_from_sysctl_if_exists

    virtual_facts = netbsd_virtual.get_virtual_facts()

    assert virtual_facts['virtualization_type'] == 'KVM'
    assert virtual_facts['virtualization_role'] == 'guest'
    assert virtual_facts['virtualization_system']

# Generated at 2022-06-13 04:13:55.284220
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    netbsd_virtual = NetBSDVirtual({})
    virtual_facts = netbsd_virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''
    assert set(virtual_facts['virtualization_tech_guest']) == set()
    assert set(virtual_facts['virtualization_tech_host']) == set()

# Generated at 2022-06-13 04:14:05.228548
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual = NetBSDVirtual(module=None)

    # mock machdep.dmi.system-product
    def _sysctl_mocked(item):
        if item == 'machdep.dmi.system-product':
            return 'VMware Virtual Platform'
        if item == 'machdep.dmi.system-vendor':
            return 'VMware, Inc.'
        if item == 'machdep.hypervisor':
            return 'VMware Virtual Platform'
        return None

    setattr(virtual, '_sysctl_get', _sysctl_mocked)
    facts = virtual.get_virtual_facts()
    assert facts['virtualization_type'] == 'kvm'
    assert facts['virtualization_role'] == 'guest'
    assert facts['virtualization_tech_host'] == set(['kvm'])


# Generated at 2022-06-13 04:14:06.279432
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    assert issubclass(NetBSDVirtualCollector, VirtualCollector)


# Generated at 2022-06-13 04:15:11.063788
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat.mock import patch
    import sys

    if sys.version_info[:2] == (2, 6):
        import unittest2 as unittest
    else:
        import unittest

    class TestNetBSDVirtual(unittest.TestCase):
        def setUp(self):
            self.netbsdvirtual_instance = NetBSDVirtual()

        def test_get_virtual_facts(self):
            self.netbsdvirtual_instance.sysctl = {
                "machdep.dmi.system-product": "VirtualBox",
                "machdep.dmi.system-vendor": "innotek GmbH",
                "machdep.hypervisor": ""
            }

            virtual_facts = self

# Generated at 2022-06-13 04:15:20.947094
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    """Returns virtual information Dict for NetBSD platform."""
    virtual_facts = {'virtualization_type': '', 'virtualization_role': ''}
    virtual_facts_obj = NetBSDVirtual()

    # Machdep.dmi.system-vendor: Xen HVM domU
    virtual_facts_obj._facts = {'machdep.dmi.system-vendor': 'Xen HVM domU'}
    virtual_facts.update(virtual_facts_obj.get_virtual_facts())
    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''

    # Machdep.dmi.system-vendor: Xen HVM domU
    virtual_facts_obj._facts = {'machdep.hypervisor': 'Xen'}

# Generated at 2022-06-13 04:15:23.677203
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    c = NetBSDVirtualCollector()
    assert c._platform == 'NetBSD'
    assert c._fact_class is not None

# Generated at 2022-06-13 04:15:25.604956
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual_facts = NetBSDVirtual({})
    assert virtual_facts.platform == 'NetBSD'

# Generated at 2022-06-13 04:15:29.226237
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    data = NetBSDVirtual({})
    assert data.platform == 'NetBSD'
    assert data.virtualization_type == ''
    assert data.virtualization_role == ''
    assert data.virtualization_tech_host == set()
    assert data.virtualization_tech_guest == set()

# Generated at 2022-06-13 04:15:30.379106
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual = NetBSDVirtual()
    assert virtual._platform == "NetBSD"

# Generated at 2022-06-13 04:15:32.172882
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    assert NetBSDVirtual({}) != None

# Generated at 2022-06-13 04:15:36.562386
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual_facts = NetBSDVirtual(None).get_virtual_facts()

    if 'virtualization_type' in virtual_facts:
        assert virtual_facts['virtualization_type'] in ('kvm', '', 'virtualbox')
    if 'virtualization_role' in virtual_facts:
        assert virtual_facts['virtualization_role'] in ('guest', 'host', '')

# Generated at 2022-06-13 04:15:39.445044
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    assert NetBSDVirtualCollector._platform == 'NetBSD'
    assert issubclass(NetBSDVirtualCollector._fact_class, Virtual)
    assert NetBSDVirtualCollector.collect()['virtualization_type'] == 'kvm'


# Generated at 2022-06-13 04:15:42.313884
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():

    virt = NetBSDVirtual()
    facts = virt.get_virtual_facts()

    assert facts['virtualization_type'].startswith('vbox')
    assert 'virtualbox' in facts['virtualization_tech_guest']
    assert 'virtualbox' in facts['virtualization_tech_host']

# Generated at 2022-06-13 04:18:14.042221
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual_facts = NetBSDVirtual()
    expected_dictionary = {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_tech_host': set(),
        'virtualization_tech_guest': set()
    }

    result = virtual_facts.get_virtual_facts()
    assert result == expected_dictionary, "Failed to get virtual facts. Expected {0} and got {1}.".format(expected_dictionary, result)

# Generated at 2022-06-13 04:18:21.872777
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    netbsd = NetBSDVirtual()
    netbsd_facts = netbsd.get_virtual_facts()
    assert type(netbsd_facts['virtualization_type']) is type(str())
    assert type(netbsd_facts['virtualization_role']) is type(str())
    if netbsd_facts['virtualization_type']:
        assert type(netbsd_facts['virtualization_type_full']) is type(str())
    assert type(netbsd_facts['virtualization_tech_guest']) is type(set())
    assert type(netbsd_facts['virtualization_tech_host']) is type(set())

# Generated at 2022-06-13 04:18:25.077235
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual_netbsd = NetBSDVirtual()
    assert virtual_netbsd.platform == 'NetBSD'


# Generated at 2022-06-13 04:18:32.039050
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    facts = NetBSDVirtualCollector().get_facts()
    # Assert that ansible_virtualization_type is set
    assert 'ansible_virtualization_type' in facts

    # Assert that value of ansible_virtualization_type is set to 'xen'
    assert facts['ansible_virtualization_type'] == 'xen'

    # Assert that ansible_virtualization_role is set
    assert 'ansible_virtualization_role' in facts

    # Assert that value of ansible_virtualization_role is set to 'guest'
    assert facts['ansible_virtualization_role'] == 'guest'

# Generated at 2022-06-13 04:18:36.958918
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    test = NetBSDVirtual()
    assert test.get_virtual_facts()['virtualization_type'] == ''
    assert 'unknown' in test.get_virtual_facts()['virtualization_role']

# Generated at 2022-06-13 04:18:38.929539
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    assert NetBSDVirtualCollector.get_platform() == 'NetBSD'
    assert NetBSDVirtualCollector._fact_class == NetBSDVirtual

# Generated at 2022-06-13 04:18:41.779316
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    netbsd_virtual = NetBSDVirtualCollector()
    assert netbsd_virtual._fact_class == NetBSDVirtual
    assert netbsd_virtual._platform == 'NetBSD'


# Generated at 2022-06-13 04:18:44.458571
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    # Arrange
    netbsd = NetBSDVirtual()

    # Assert
    assert netbsd._platform == 'NetBSD'
    assert netbsd._fact_class == 'NetBSDVirtual'

# Generated at 2022-06-13 04:18:51.237040
# Unit test for method get_virtual_facts of class NetBSDVirtual

# Generated at 2022-06-13 04:18:52.959323
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual()
    assert netbsd_virtual.platform == 'NetBSD'

