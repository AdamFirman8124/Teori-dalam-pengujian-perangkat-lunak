

# Generated at 2022-06-13 00:56:35.942586
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    module = AnsibleModule({})
    hardware_collector = NetBSDHardwareCollector(module)
    facts = hardware_collector.collect()
    for required_fact in ['mounts', 'memtotal_mb', 'memfree_mb', 'processor_cores', 'processor_count', 'system_vendor']:
        assert required_fact in facts

# ansible-test compatibility layer

# Generated at 2022-06-13 00:56:36.738611
# Unit test for constructor of class NetBSDHardwareCollector
def test_NetBSDHardwareCollector():
    NetBSDHardwareCollector()


# Generated at 2022-06-13 00:56:46.953043
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    test_file_path = os.path.join(os.path.dirname(__file__),
                                  '..', '..', 'unit', 'module_utils', 'facts', 'hardware', 'test_data', 'NetBSD')

    # patch get_file_content()
    def _get_file_content(path, default=None):
        """Return content of the test data file."""
        if path.endswith("/proc/net/bonding/bond0"):
            return ""

        if path.endswith("/proc/cpuinfo"):
            filename = 'proc_cpuinfo_NetBSD.txt'
        elif path.endswith("/proc/meminfo"):
            filename = 'proc_meminfo_NetBSD.txt'

# Generated at 2022-06-13 00:56:55.810735
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    module = None
    hardware = NetBSDHardware(module)
    hardware_facts = hardware.populate()

    assert hardware_facts['devices']
    assert hardware_facts['devices']['net']
    assert hardware_facts['devices']['disk']
    assert hardware_facts['devices']['partition']
    assert hardware_facts['devices']['dmi']
    assert hardware_facts['processor']
    assert hardware_facts['processor_cores']
    assert hardware_facts['processor_count']
    assert hardware_facts['memfree_mb']
    assert hardware_facts['memtotal_mb']
    assert hardware_facts['swapfree_mb']
    assert hardware_facts['swaptotal_mb']

# Generated at 2022-06-13 00:56:56.983232
# Unit test for constructor of class NetBSDHardwareCollector
def test_NetBSDHardwareCollector():
    hw = NetBSDHardwareCollector()
    assert isinstance(hw, NetBSDHardwareCollector)


# Generated at 2022-06-13 00:57:04.295618
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    module = MockModule()
    hardware = NetBSDHardware(module)

    hardware._dmi_facts = {
        'product_name': 'Foo Bar',
        'system_vendor': 'ACME Corp.',
    }
    hardware._memory_facts = {
        'memfree_mb': 8192,
        'swaptotal_mb': 2048,
        'memtotal_mb': 32768,
        'swapfree_mb': 512,
    }
    hardware._cpu_facts = {
        'processor': ['foo', 'bar'],
        'processor_count': 2,
        'processor_cores': 2,
    }


# Generated at 2022-06-13 00:57:13.320961
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    netbsd_hw = NetBSDHardware(None)
    dmi_facts = {'product_name': 'i386',
                 'product_version': '6.1.3',
                 'product_serial': '',
                 'product_uuid': '',
                 'system_vendor': 'unknown',
                 'product_sku': ''}
    cpu_facts = {'processor': ['Intel(R) Core(TM) i5-4300U CPU @ 1.90GHz'],
                 'processor_cores': 2,
                 'processor_count': 4}

# Generated at 2022-06-13 00:57:17.443655
# Unit test for method get_cpu_facts of class NetBSDHardware
def test_NetBSDHardware_get_cpu_facts():
    expected = ['Intel(R) Xeon(R) CPU E5-2660 0 @ 2.20GHz']
    hardware_collector = NetBSDHardwareCollector()
    hardware = hardware_collector._fact_class()
    cpu_facts = hardware.get_cpu_facts()
    assert cpu_facts['processor'] == expected


# Generated at 2022-06-13 00:57:27.842598
# Unit test for method get_dmi_facts of class NetBSDHardware
def test_NetBSDHardware_get_dmi_facts():
    m = NetBSDHardware()
    dmi_facts = m.get_dmi_facts()
    assert dmi_facts == {'product_name': '',
                         'product_serial': '',
                         'product_uuid': '',
                         'product_version': '',
                         'system_vendor': '',
                         }
    # m.sysctl = {'machdep.dmi.system-product': '',
    #             'machdep.dmi.system-serial': '',
    #             'machdep.dmi.system-version': '',
    #             'machdep.dmi.system-uuid': '',
    #             'machdep.dmi.system-vendor': ''}

# Generated at 2022-06-13 00:57:29.955055
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    hardware = NetBSDHardware()
    hardware.populate()


# Generated at 2022-06-13 00:59:07.518398
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    hardware = NetBSDHardware(None)
    facts = hardware.populate()
    assert facts['devices'] == {}
    assert facts['processor_cores'] >= 1
    assert facts['processor_count'] >= 1
    assert facts['processor']
    assert facts['memtotal_mb'] >= 1024
    assert facts['swaptotal_mb'] >= 0
    assert facts['mounts']

# vim: set et ts=4 ai :

# Generated at 2022-06-13 00:59:10.385796
# Unit test for constructor of class NetBSDHardwareCollector
def test_NetBSDHardwareCollector():
    instance = NetBSDHardwareCollector()
    assert instance.get_platform() == 'NetBSD'
    assert instance.get_fact_class() == NetBSDHardware
    assert issubclass(instance.get_fact_class(), Hardware) is True


# Generated at 2022-06-13 00:59:11.512215
# Unit test for constructor of class NetBSDHardwareCollector
def test_NetBSDHardwareCollector():
    har_obj = NetBSDHardwareCollector()
    assert har_obj._fact_class.platform == 'NetBSD'

# Generated at 2022-06-13 00:59:21.745032
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    raw = {}

# Generated at 2022-06-13 00:59:24.198153
# Unit test for constructor of class NetBSDHardwareCollector
def test_NetBSDHardwareCollector():
    c = NetBSDHardwareCollector()

# Generated at 2022-06-13 00:59:26.864331
# Unit test for method get_dmi_facts of class NetBSDHardware
def test_NetBSDHardware_get_dmi_facts():
    class MockModule(object):
        pass

    module = MockModule()
    module.params= {}
    hardware = NetBSDHardware(module)

    assert hardware.get_dmi_facts()["product_name"] is not None

# Generated at 2022-06-13 00:59:35.833500
# Unit test for method get_dmi_facts of class NetBSDHardware
def test_NetBSDHardware_get_dmi_facts():
    fake_sysctl = {'machdep.dmi.system-product': 'Acer',
                   'machdep.dmi.system-version': '123',
                   'machdep.dmi.system-uuid': '123-456-789',
                   'machdep.dmi.system-serial': '123456789',
                   'machdep.dmi.system-vendor': 'ACER',
                   }
    test_hardware_facts = NetBSDHardware()
    test_hardware_facts.sysctl = fake_sysctl
    test_hardware_facts.populate()

    dmi_facts = test_hardware_facts.get_dmi_facts()
    print(dmi_facts)
    assert dmi_facts['system_vendor'] == 'ACER'

# Generated at 2022-06-13 00:59:45.711343
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    hardware = NetBSDHardware()

    # define constants for populate's return data structure
    PROCESSOR  = 'processor'
    PROC_COUNT = 'processor_count'
    PROC_CORES = 'processor_cores'
    MEMTOTAL = 'memtotal_mb'
    MEMFREE  = 'memfree_mb'
    SWAPTOTAL = 'swaptotal_mb'
    SWAPFREE  = 'swapfree_mb'
    DEVICES = 'devices'

    facts = hardware.populate()
    assert isinstance(facts[PROCESSOR], list)
    assert isinstance(facts[PROC_COUNT], int)
    assert isinstance(facts[PROC_CORES], (int, str))
    assert isinstance(facts[MEMTOTAL], int)

# Generated at 2022-06-13 00:59:53.224279
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    # GIVEN a dict of facts collected from NetBSD
    collected_facts = {
        'os': {
            'distribution': 'NetBSD',
            'version': '7.0.1'
        }
    }

    # WHEN initializing the NetBSDHardware class
    hardware_model = NetBSDHardware(collected_facts=collected_facts)

    # THEN the model should have attributes from the collected facts
    assert hardware_model.platform == 'NetBSD'
    assert hardware_model.collector == 'NetBSDHardwareCollector'
    assert hardware_model.version == '7.0.1'
    assert hardware_model.distribution == 'NetBSD'

    # GIVEN a fact called mib-sysctl

# Generated at 2022-06-13 01:00:00.322101
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    netbsd_hardware = NetBSDHardware()
    import platform
    if platform.machine() != 'x86_64':
        return
    netbsd_hardware.populate()
    assert netbsd_hardware.facts['processor_count'] == 4
    assert netbsd_hardware.facts['processor_cores'] == 4
    assert netbsd_hardware.facts['processor'] == ['Intel(R) Core(TM) i7-2600 CPU @ 3.40GHz']
    assert netbsd_hardware.facts['memtotal_mb'] == 28953
    assert netbsd_hardware.facts['swaptotal_mb'] == 12904
    assert netbsd_hardware.facts['system_vendor'] == 'ASUSTeK Computer INC.'

# Generated at 2022-06-13 01:01:49.246472
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    # We need the following private symbol
    NetBSDHardware._platform = 'NetBSD'
    facter = NetBSDHardware()

    # We need a custom get_file_lines
    def custom_get_file_lines(filename):
        if filename == "/proc/meminfo":
            content = 'MemTotal:       16149652 kB\nMemFree:        6435208 kB\nSwapTotal:       5070348 kB\nSwapFree:        5070348 kB\n'

# Generated at 2022-06-13 01:01:57.828327
# Unit test for method get_cpu_facts of class NetBSDHardware
def test_NetBSDHardware_get_cpu_facts():
    data = '''
cpu: ARMv7 Processor rev 0 (v7l)
model name : Cortex-A8
BogoMIPS : 743.68
Features : swp half thumb fastmult edsp neon vfp vfpv3
CPU implementer : 0x41
CPU architecture: 7
CPU variant : 0x1
CPU part : 0xc09
CPU revision : 0

Hardware : Marvell PJ4Bv7-Dorado
Revision : 0000
Serial : 0000000000000000
'''
    data2 = '''
Intel(R) Atom(TM) CPU  N270   @ 1.60GHz
'''

# Generated at 2022-06-13 01:02:06.194898
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    """Test the NetBSDHardware's populate method
    """
    # Mock the sysctl(8) call
    mocked_sysctl = {'machdep.dmi.system-product': 'VirtualBox',
                     'machdep.dmi.system-vendor': 'innotek GmbH'}

    def mock_get_sysctl(*_, **__):
        return mocked_sysctl

    module = type("MockModule", (), {})()
    m = module.module = type("MockModuleDefinition", (), {})()
    m.fail_json = lambda *_, **__: (
        'Failed to collect the following facts: %s' % ', '.join(['hardware']))
    m.run_command = lambda *_, **__: (0, '', '')

# Generated at 2022-06-13 01:02:09.989306
# Unit test for method get_memory_facts of class NetBSDHardware
def test_NetBSDHardware_get_memory_facts():
    hardware = NetBSDHardware()
    hardware.module = None
    if os.access('/proc/meminfo', os.R_OK):
        for fact in NetBSDHardware.MEMORY_FACTS:
            re_pattern = "%s:\s*(\d+)" % fact
            match = re.search(re_pattern, get_file_content('/proc/meminfo'))
            assert match and int(match.groups()[0]) == hardware.get_memory_facts()["%s_mb" % fact.lower()] or match == None

# Generated at 2022-06-13 01:02:14.073116
# Unit test for constructor of class NetBSDHardwareCollector
def test_NetBSDHardwareCollector():
    assert issubclass(NetBSDHardwareCollector, HardwareCollector)
    netbsdHardwareCollector = NetBSDHardwareCollector()

    assert netbsdHardwareCollector._fact_class == NetBSDHardware
    assert netbsdHardwareCollector._platform == 'NetBSD'

# Generated at 2022-06-13 01:02:24.486843
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    """ UnitTest for method populate of class NetBSDHardware """
    def get_file_content_mock(path):
        if path == '/proc/cpuinfo':
            return '\n'.join([
                'Processor: ARMv6-compatible processor rev 7 (v6l)',
                'processor: 0',
                'processor: 1',
                'BogoMIPS: 0.08',
                'Features: swp half thumb fastmult vfp edsp java tls',
                'CPU implementer : 0x41',
                'CPU architecture: 7',
                'CPU variant : 0x0',
                'CPU part : 0xb76',
                'CPU revision : 7',
                'Hardware : Marvell SheevaPlug Reference Board',
                'Revision : 0000',
                'Serial : 0000000000000000',
            ])

# Generated at 2022-06-13 01:02:28.716949
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    hardware = NetBSDHardware()
    hardware_facts = hardware.populate()

    assert 'processor' in hardware_facts
    assert 'processor_cores' in hardware_facts
    assert 'processor_count' in hardware_facts
    assert 'memfree_mb' in hardware_facts
    assert 'memtotal_mb' in hardware_facts
    assert 'swapfree_mb' in hardware_facts
    assert 'swaptotal_mb' in hardware_facts

# Generated at 2022-06-13 01:02:40.261722
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    netbsd_hardware = NetBSDHardware()

# Generated at 2022-06-13 01:02:46.786752
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    hardware_collector = NetBSDHardwareCollector()
    hardware_collector._module = lambda *args, **kwargs: None
    hardware_collector._module.run_command = lambda *args, **kwargs: None
    hardware_collector._module.run_command.return_value = (0, get_file_content('../../utils/test_data/netbsd_hardware_facts'), '')

    facts = hardware_collector.collect()
    assert facts['processor_count'] == 2
    assert facts['processor_cores'] == 4

# Generated at 2022-06-13 01:02:49.641023
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    args = {"ansible_facts": {}}
    NetBSDHardware(args).populate()

    for fact in NetBSDHardware.MEMORY_FACTS:
        assert fact.lower()+"_mb" in args["ansible_facts"]

# Generated at 2022-06-13 01:05:02.676850
# Unit test for method get_cpu_facts of class NetBSDHardware
def test_NetBSDHardware_get_cpu_facts():
    cpu_facts = NetBSDHardware().get_cpu_facts()
    assert len(cpu_facts) == 0 or \
           sorted(cpu_facts.keys()) == [
               'processor', 'processor_cores', 'processor_count'
           ]

# Generated at 2022-06-13 01:05:11.413479
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    module = FakeAnsibleModule()
    hw = NetBSDHardware(module)
    hw.populate()

# Generated at 2022-06-13 01:05:12.425250
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    hardware = NetBSDHardware(None)
    hardware.populate()

# Generated at 2022-06-13 01:05:18.258991
# Unit test for method get_cpu_facts of class NetBSDHardware

# Generated at 2022-06-13 01:05:25.996410
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    '''
    test populate() of NetBSDHardware
    '''
    memory_facts = {'memtotal_mb': 36632, 'memfree_mb': 2991, 'swaptotal_mb': 0, 'swapfree_mb': 0}
    cpu_facts = {'processor': ['Intel(R) Xeon(R) CPU E3-1230 V2 @ 3.30GHz']}
    mount_facts = {'mounts': [{'mount': '/', 'device': '/dev/ld0a',
                               'fstype': 'ffs', 'options': 'rw,local,async,-s,-u,-w',
                               'size_total': 9962601472, 'size_available': 16105512960}]}

# Generated at 2022-06-13 01:05:28.706621
# Unit test for constructor of class NetBSDHardwareCollector
def test_NetBSDHardwareCollector():
    # Constructor for class NetBSDHardwareCollector should set _fact_class and
    # _platform
    nwhc = NetBSDHardwareCollector()
    assert nwhc._fact_class is NetBSDHardware
    assert nwhc._platform == 'NetBSD'

# Generated at 2022-06-13 01:05:33.912982
# Unit test for method get_dmi_facts of class NetBSDHardware
def test_NetBSDHardware_get_dmi_facts():
    fake_module = type('', (), {})
    fake_module.fail_json = lambda **kwargs: None
    hardware = NetBSDHardware(fake_module)

    # Test empty dict
    hardware.sysctl = {}
    assert hardware.get_dmi_facts() == {}

    # Test one fact
    hardware.sysctl = {'machdep.dmi.system-vendor': 'Vendor'}
    assert hardware.get_dmi_facts() == {'system_vendor': 'Vendor'}

    # Test multiple facts
    hardware.sysctl = {'machdep.dmi.system-product': 'Product',
                       'machdep.dmi.system-version': 'Version'}