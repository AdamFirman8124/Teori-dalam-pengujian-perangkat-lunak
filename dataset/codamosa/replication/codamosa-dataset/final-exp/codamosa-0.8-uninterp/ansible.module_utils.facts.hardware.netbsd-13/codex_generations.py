

# Generated at 2022-06-13 00:57:04.656866
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    # Create a NetBSDHardware object
    obj = NetBSDHardware()

    # We return a dictionary with the required and optional facts

# Generated at 2022-06-13 00:57:13.533974
# Unit test for method get_dmi_facts of class NetBSDHardware
def test_NetBSDHardware_get_dmi_facts():
    netbsd = NetBSDHardware({'ansible_facts': {'sysctl': {'machdep.dmi.system-product': 'Virt',
                                                           'machdep.dmi.system-version': 'None',
                                                           'machdep.dmi.system-uuid': '42f80cc6-b5a0-11e7-9a78-2d15aaf33ec2',
                                                           'machdep.dmi.system-serial': '42f80cc6-b5a0-11e7-9a78-2d15aaf33ec2',
                                                           'machdep.dmi.system-vendor': 'Bochs'}}})
    dmi_facts = netbsd.get_dmi_facts()
    assert dmi_

# Generated at 2022-06-13 00:57:21.198856
# Unit test for method get_dmi_facts of class NetBSDHardware
def test_NetBSDHardware_get_dmi_facts():
    netbsd_hw_obj = NetBSDHardware(None)
    netbsd_hw_obj._module.sysctl = {
        'machdep.dmi.system-uuid': 'UUID',
        'machdep.dmi.system-product': 'system-product',
        'machdep.dmi.system-version': 'system-version',
        'machdep.dmi.system-serial': 'system-serial',
        'machdep.dmi.system-vendor': 'system-vendor',
    }

    dmi_facts = netbsd_hw_obj.get_dmi_facts()
    assert dmi_facts['product_uuid'] == 'UUID'
    assert dmi_facts['product_name'] == 'system-product'

# Generated at 2022-06-13 00:57:32.024755
# Unit test for method get_dmi_facts of class NetBSDHardware
def test_NetBSDHardware_get_dmi_facts():

    mock_get_sysctl = [
        {'machdep.dmi.system-product': 'OpenBSD Virtual Machine'},
        {'machdep.dmi.system-version': 'Not Applicable'},
        {'machdep.dmi.system-uuid': '00000000-0000-0000-0000-000000000000'},
        {'machdep.dmi.system-serial': 'Not Specified'},
        {'machdep.dmi.system-vendor': 'OpenBSD'},
    ]

    # Testing the method get_dmi_facts with valid data
    NetBSD_hardware_obj = NetBSDHardware()
    NetBSD_hardware_obj.sysctl = mock_get_sysctl

# Generated at 2022-06-13 00:57:36.259448
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    netbsd_hardware = NetBSDHardware()
    collected_facts = {'ansible_facts': {'distribution': "NetBSD", 'distribution_version': "7.1", 'distribution_major_version': "7"}}
    ret = netbsd_hardware.populate(collected_facts=collected_facts)
    assert ret['ansible_processor_cores'] == 2


# Generated at 2022-06-13 00:57:46.077258
# Unit test for method get_dmi_facts of class NetBSDHardware
def test_NetBSDHardware_get_dmi_facts():
    netbsd_hardware = NetBSDHardware()
    test_sysctl = {'machdep.dmi.system-product': 'Test System',
                   'machdep.dmi.system-vendor': 'Test System Vendor',
                   'machdep.dmi.system-serial': 'ABCDEFG',
                   'machdep.dmi.system-version': '1.2.3',
                   'machdep.dmi.system-uuid': '00000000-0000-0000-0000-000000000000'}
    netbsd_hardware.sysctl = test_sysctl
    dmi_facts = netbsd_hardware.get_dmi_facts()
    assert dmi_facts == test_sysctl

# Generated at 2022-06-13 00:57:56.859169
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    """
        Testing populate method of NetBSDHardware class
    """

# Generated at 2022-06-13 00:58:03.173711
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    hardware = NetBSDHardwareCollector.collect()
    assert 'memfree_mb' in hardware.keys()
    assert 'memtotal_mb' in hardware.keys()
    assert 'swapfree_mb' in hardware.keys()
    assert 'swaptotal_mb' in hardware.keys()
    assert 'processor' in hardware.keys()
    assert 'processor_cores' in hardware.keys()
    assert 'processor_count' in hardware.keys()

# Generated at 2022-06-13 00:58:13.309831
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    """
    Test for method populate of class NetBSDHardware.
    """
    # Test with a DMI table with all the fields
    # We don't need to test each field, as fact_subset() is used every time.
    collected_facts = {'sysctl': {'machdep.dmi.system-product': 'VirtualBox',
                                  'machdep.dmi.system-uuid': '1',
                                  'machdep.dmi.system-vendor': '',
                                  'machdep.dmi.system-serial': '',
                                  'machdep.dmi.system-version': ''}}
    test_obj = NetBSDHardware({}, collected_facts)
    facts = test_obj.populate()


# Generated at 2022-06-13 00:58:22.682197
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    cpu_facts = {'processor': [],
                 'processor_cores': 'NA',
                 'processor_count': 0}
    memory_facts = {'memtotal_mb': 17458,
                    'memfree_mb': 3,
                    'swaptotal_mb': 'NA',
                    'swapfree_mb': 'NA'}

# Generated at 2022-06-13 00:59:45.234857
# Unit test for constructor of class NetBSDHardwareCollector
def test_NetBSDHardwareCollector():
    test_collector = NetBSDHardwareCollector()
    assert isinstance(test_collector, NetBSDHardwareCollector)


# Generated at 2022-06-13 00:59:51.974874
# Unit test for method get_dmi_facts of class NetBSDHardware
def test_NetBSDHardware_get_dmi_facts():
    from ansible.module_utils.facts.hardware.netbsd import NetBSDHardware
    from ansible.module_utils.facts.timeout import TimeoutError

    try:
        h = NetBSDHardware()
    except TimeoutError:
        pass

    dmi_facts = h.get_dmi_facts()

    assert isinstance(dmi_facts, dict)
    assert 'product_name' in dmi_facts
    assert 'product_version' in dmi_facts
    assert 'product_uuid' in dmi_facts
    assert 'product_serial' in dmi_facts
    assert 'system_vendor' in dmi_facts

# Generated at 2022-06-13 00:59:59.740405
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    """
    Test NetBSDHardware.populate
    """
    from ansible.module_utils.facts.collector import TestModule
    from ansible.module_utils.facts.collector.netbsd import NetBSDHardwareCollector

    module = TestModule({})
    hardware_collector = NetBSDHardwareCollector(module)
    hardware = hardware_collector.collect()[0]

    assert hardware.memfree_mb
    assert hardware.memtotal_mb
    assert hardware.swapfree_mb
    assert hardware.swaptotal_mb
    assert hardware.processor
    assert hardware.processor_cores
    assert hardware.processor_count
    assert hardware.system_vendor
    assert hardware.product_name
    assert hardware.product_serial
    assert hardware.product_version
    assert hardware.product_uuid
    assert hardware

# Generated at 2022-06-13 01:00:04.084457
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    netbsd_fixture = {
      'processor': [
        'ARMv7 Processor rev 1 (v7l)'
      ],
      'processor_count': 1,
      'processor_cores': 1,
      'memtotal_mb': 962,
      'memfree_mb': 665,
      'swaptotal_mb': 0,
      'swapfree_mb': 0,
      'product_name': 'Marvell Armada 370/XP Development Board',
      'product_serial': 'None',
      'product_uuid': '4c4c4544-0041-4d10-8042-b6c04f455836',
      'product_version': '1.0',
      'system_vendor': 'Marvell'
    }

    netbsd_hardware = NetBSDHardware()


# Generated at 2022-06-13 01:00:06.379360
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    hardware = NetBSDHardware({'module': None})
    hardware_facts = hardware.populate()
    assert hardware_facts['devices']['system'] == {'product': {'name': 'NetBSD/amd64', 'serial': '', 'uuid': '', 'version': ''}, 'vendor': {'name': 'NetBSD'}}

# Generated at 2022-06-13 01:00:11.396080
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    hardware_facts = NetBSDHardware()
    collected_facts = hardware_facts.populate()
    assert 'processor_cores' in collected_facts.keys()
    assert 'processor_count' in collected_facts.keys()
    assert 'devices' in collected_facts.keys()
    assert 'processor' in collected_facts.keys()
    assert 'memfree_mb' in collected_facts.keys()
    assert 'memtotal_mb' in collected_facts.keys()
    assert 'swapfree_mb' in collected_facts.keys()
    assert 'swaptotal_mb' in collected_facts.keys()

# Generated at 2022-06-13 01:00:21.175770
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    from ansible.module_utils.facts import FactManager
    facts = FactManager()
    intel_platforms = ['x86_64', 'i386']
    if facts.get('ansible_system', None) == 'NetBSD' and facts.get('ansible_machine', None) in intel_platforms:
        h = NetBSDHardware(module=None)
        h.populate()
        assert h.get_facts()['processor'][0] == 'Intel(R) Core(TM) i7-2720QM CPU @ 2.20GHz'
        assert h.get_facts()['processor_cores'] == '4'
        assert h.get_facts()['processor_count'] == '4'
        assert h.get_facts()['memfree_mb'] == 1624

# Generated at 2022-06-13 01:00:25.324409
# Unit test for method get_memory_facts of class NetBSDHardware
def test_NetBSDHardware_get_memory_facts():
    from ansible.module_utils._text import to_bytes
    module = 'fake'
    hardware = NetBSDHardware(module)
    hardware.populate()
    memory_facts = hardware.get_memory_facts()
    assert memory_facts.get("memtotal_mb") == 1
    assert memory_facts.get("swaptotal_mb") == 2
    assert memory_facts.get("memfree_mb") == 3
    assert memory_facts.get("swapfree_mb") == 4


# Generated at 2022-06-13 01:00:28.751592
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    mock_module = AnsibleModuleMock(params={})
    hardware = NetBSDHardware(mock_module)
    hardware.populate()
    assert hardware.facts['processor_count']



# Generated at 2022-06-13 01:00:33.665595
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    """ Test populate method of NetBSDHardware class for known data """
    hardware_facts = NetBSDHardware()
    hardware_facts.populate()
    assert hardware_facts.data['system_vendor'] == 'The NetBSD Foundation, Inc.'
    assert hardware_facts.data['processor'] == ['ARMv7 Processor rev 2 (v7l)']

# Generated at 2022-06-13 01:02:02.213126
# Unit test for method get_dmi_facts of class NetBSDHardware
def test_NetBSDHardware_get_dmi_facts():
    class MockModule():
        def fail_json(self, *a, **k):
            raise RuntimeError("it failed")

    class MockGetSysctl():
        def __init__(self, module):
            pass

        def get(self):
            return {
                'machdep.dmi.system-product': 'Product name',
                'machdep.dmi.system-version': 'Product version',
                'machdep.dmi.system-uuid': '0-0-0-0',
                'machdep.dmi.system-serial': '1234',
                'machdep.dmi.system-vendor': 'System vendor',
            }

    module = MockModule()
    get_sysctl_mock = MockGetSysctl(module)

# Generated at 2022-06-13 01:02:04.244391
# Unit test for method get_cpu_facts of class NetBSDHardware
def test_NetBSDHardware_get_cpu_facts():
    netbsd_hardware = NetBSDHardware()
    cpu_facts = netbsd_hardware.get_cpu_facts()
    assert 'processor' in cpu_facts
    assert 'processor_count' in cpu_facts
    assert 'processor_cores' in cpu_facts

# Generated at 2022-06-13 01:02:05.892534
# Unit test for constructor of class NetBSDHardwareCollector
def test_NetBSDHardwareCollector():
    hardware_collector = NetBSDHardwareCollector()
    assert isinstance(hardware_collector, NetBSDHardwareCollector)
    assert isinstance(hardware_collector.collect(), NetBSDHardware)

# Generated at 2022-06-13 01:02:11.150876
# Unit test for method get_dmi_facts of class NetBSDHardware
def test_NetBSDHardware_get_dmi_facts():
    fake_module = type('FakeModule', (object,), {
        'get_bin_path': lambda s, executable, opt_dirs: '/sbin/sysctl',
    })
    fake_args = type('FakeArgs', (object,), {
        '_raw_params': {},
        'async_timeout': 60
    })
    fake_timeout = type('FakeTimeout', (object,), {
        '__call__': lambda s, t, f, a: f(*a),
        '__enter__': lambda s: s,
        '__exit__': lambda s, e, tb, *a: None
    })


# Generated at 2022-06-13 01:02:22.254130
# Unit test for method get_memory_facts of class NetBSDHardware
def test_NetBSDHardware_get_memory_facts():
    datadir = os.path.join(os.path.dirname(__file__), 'fixtures')
    srcfile = os.path.join(datadir, 'meminfo')
    targetfile = os.path.join(datadir, 'meminfo.target')
    facts = NetBSDHardware()
    res = facts.get_memory_facts()
    with open(targetfile, 'r') as f:
        for line in f:
            data = line.split(":", 1)
            key = data[0].strip()
            # model name is for Intel arch, Processor (mind the uppercase P)
            # works for some ARM devices, like the Sheevaplug.
            if key in NetBSDHardware.MEMORY_FACTS:
                val = data[1].strip().split(' ')[0]

# Generated at 2022-06-13 01:02:28.325464
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    """
    This function is used to test populate function of class NetBSDHardware
    """
    dmi_obj = {'machdep.dmi.system-product': 'Raspberry Pi',
               'machdep.dmi.system-uuid': '00000000-0000-0000-0000-ffffffffffff',
               'machdep.dmi.system-vendor': 'Raspberry Pi Foundation',
               'machdep.dmi.system-version': '1.0'}
    hardware = NetBSDHardware(module=None)
    hardware.sysctl = dmi_obj
    hardware.populate()

# Generated at 2022-06-13 01:02:39.812896
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    from ansible.module_utils.facts import Hardware

    # Create a system with 1 socket and 4 cores
    physid = 0
    sockets = {}
    cpu_facts = {}
    cpu_facts['processor'] = []
    for i in range(0, 4):
        cpu_facts['processor'].append("Processor %d" % i)
        sockets[physid] = 4
    cpu_facts['processor_count'] = len(sockets)
    cpu_facts['processor_cores'] = reduce(lambda x, y: x + y, sockets.values())

    memory_facts = {}
    memory_facts['memtotal_mb'] = 4096
    memory_facts['memfree_mb'] = 2048

    # Create a fake /etc/fstab file

# Generated at 2022-06-13 01:02:46.994803
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():

    module = AnsibleModule(
        argument_spec=dict(
        )
    )

    # empty collect_facts
    nbhd = NetBSDHardware(module=module)
    facts = nbhd.populate(collected_facts={})
    assert 'processor' in facts
    assert 'processor_count' in facts
    assert 'processor_cores' in facts
    assert 'memfree_mb' in facts
    assert 'memtotal_mb' in facts
    assert 'swapfree_mb' in facts
    assert 'swaptotal_mb' in facts
    assert 'product_name' in facts
    assert 'product_serial' in facts
    assert 'product_version' in facts
    assert 'product_uuid' in facts
    assert 'system_vendor' in facts
    assert 'mounts' in facts

# Unit

# Generated at 2022-06-13 01:02:55.236434
# Unit test for method get_dmi_facts of class NetBSDHardware
def test_NetBSDHardware_get_dmi_facts():
    nbhd = NetBSDHardware()
    nbhd.module = True

# Generated at 2022-06-13 01:03:01.688445
# Unit test for method get_dmi_facts of class NetBSDHardware
def test_NetBSDHardware_get_dmi_facts():
    '''
    Checks that get_dmi_facts returns expected values.
    '''
    class NewBSDHardware(NetBSDHardware):
        '''
        A subclass of NetBSDHardware created to provide mocks for
        get_sysctl.
        '''
        def __init__(self, *args, **kwargs):
            self.mock_sysctl = {
                'machdep.dmi.system-product': 'ROCKPro64',
                'machdep.dmi.system-version': '1.0',
                'machdep.dmi.system-uuid': '0x000000000000',
                'machdep.dmi.system-serial': '0x000000000000',
                'machdep.dmi.system-vendor': 'Pine64',
            }

# Generated at 2022-06-13 01:04:53.124167
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    netbsd_hw = NetBSDHardware()
    collected_facts = netbsd_hw.populate()
    assert 'machdep' in collected_facts
    assert collected_facts['machdep']['cpu_vendor'] == 'GenuineIntel'
    assert collected_facts['machdep']['cpu_brand'] == 'Intel(R) Core(TM) i7-8650U CPU @ 1.90GHz'
    assert collected_facts['machdep']['cpu_family'] == 6
    assert collected_facts['machdep']['cpu_model'] == 142
    assert collected_facts['machdep']['cpu_stepping'] == 10
    assert collected_facts['machdep']['cpu_clock'] == 1900

# Generated at 2022-06-13 01:05:01.702216
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    netbsd_hardware_facts = NetBSDHardware(None, None)
    facts = netbsd_hardware_facts.populate()
    assert isinstance(facts['processor_cores'], int)
    assert isinstance(facts['processor_count'], int)
    assert isinstance(facts['processor'], list)
    assert isinstance(facts['memfree_mb'], int)
    assert isinstance(facts['memtotal_mb'], int)
    assert isinstance(facts['swapfree_mb'], int)
    assert isinstance(facts['swaptotal_mb'], int)
    assert isinstance(facts['mounts'], list)
    for m in facts['mounts']:
        assert isinstance(m['size_total'], int)
        assert isinstance(m['size_available'], int)

# Generated at 2022-06-13 01:05:10.370523
# Unit test for method get_dmi_facts of class NetBSDHardware
def test_NetBSDHardware_get_dmi_facts():
    module = None
    netbsd_hw = NetBSDHardware(module)


# Generated at 2022-06-13 01:05:12.100024
# Unit test for method get_dmi_facts of class NetBSDHardware
def test_NetBSDHardware_get_dmi_facts():
    module = MockModule({})
    facts = NetBSDHardware(module).get_dmi_facts()
    assert len(facts) == 0



# Generated at 2022-06-13 01:05:18.018123
# Unit test for method get_dmi_facts of class NetBSDHardware
def test_NetBSDHardware_get_dmi_facts():
    class MyNetBSDHardware(NetBSDHardware):
        def __init__(self, module, collected_facts=None):
            '''Bypass __init__ of NetBSDHardware so to not invoke sysctl(1)
            '''
            self.module = module
            self.collected_facts = collected_facts

    # Simulate call from get_sysctl()
    facts = {}

# Generated at 2022-06-13 01:05:21.222794
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    hardware = NetBSDHardware()
    hardware = hardware.populate()
    assert hardware['processor_cores'] == "NA"
    assert hardware['processor_count'] == 1
    assert hardware['processor_vcpus'] == 1

# Generated at 2022-06-13 01:05:27.930321
# Unit test for method get_dmi_facts of class NetBSDHardware
def test_NetBSDHardware_get_dmi_facts():
    class MockModule:
        def __init__(self):
            self.params = dict()
            self.fail_json = lambda **kwargs: None

        def exit_json(self, **kwargs):
            return

        def fail_json(self, **kwargs):
            return

    class MockHardware:
        def __init__(self, facts):
            self._facts = facts
            self._module = MockModule()

        def collect(self):
            return self._facts


# Generated at 2022-06-13 01:05:35.835265
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    module = AnsibleModuleMock()
    hardware = NetBSDHardware(module)
    facts = hardware.populate()
    assert facts['processor'][0] == 'Intel(R) Pentium(R) 4 CPU 2.00GHz'
    assert facts['processor_cores'] == 'NA'
    assert facts['processor_count'] == 1
    assert facts['memtotal_mb'] == 100
    assert facts['memfree_mb'] == 10
    assert facts['swaptotal_mb'] == 200
    assert facts['swapfree_mb'] == 20
    assert facts['devices'] == {}
    assert facts['product_name'] == 'Dell Computer Corporation'
    assert facts['system_vendor'] == 'Dell Computer Corporation'
    assert 'mounts' in facts

# Generated at 2022-06-13 01:05:36.658071
# Unit test for constructor of class NetBSDHardwareCollector
def test_NetBSDHardwareCollector():
    NetBSDHardwareCollector()