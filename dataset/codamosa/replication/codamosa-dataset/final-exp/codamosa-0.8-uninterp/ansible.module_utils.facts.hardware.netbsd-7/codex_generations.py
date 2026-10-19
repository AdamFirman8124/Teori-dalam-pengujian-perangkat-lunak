

# Generated at 2022-06-13 00:56:40.833435
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    module = AnsibleModuleMock()
    module.run_command = CommandResult
    NetBSDHardwareFactCollector.get_sysctl = get_sysctl
    NetBSDHardwareFactCollector.get_mount_facts = get_mount_facts
    NetBSDHardwareFactCollector.get_cpu_facts = get_cpu_facts
    NetBSDHardwareFactCollector.get_memory_facts = get_memory_facts
    NetBSDHardwareFactCollector.get_devices = get_devices
    NetBSDHardware().populate()



# Generated at 2022-06-13 00:56:44.304946
# Unit test for method get_memory_facts of class NetBSDHardware
def test_NetBSDHardware_get_memory_facts():
    netbsd = NetBSDHardware()
    netbsd.module = None
    netbsd.collect()
    assert netbsd.get_memory_facts()['memtotal_mb'] > 0

# Generated at 2022-06-13 00:56:52.597476
# Unit test for method get_dmi_facts of class NetBSDHardware
def test_NetBSDHardware_get_dmi_facts():
    netbsd_hardware = NetBSDHardware(module=None)
    netbsd_hardware.sysctl = {
        'machdep.dmi.system-vendor': 'Cx86',
        'machdep.dmi.system-product': 'VGC-LT15E',
        'machdep.dmi.system-version': 'System Version',
        'machdep.dmi.system-uuid': '514D3F5F-4C24-4DEC-9573-D018E4AD4DA2',
        'machdep.dmi.system-serial': '123456789'
    }

    result = netbsd_hardware.get_dmi_facts()
    assert len(result) == 5
    assert result['system_vendor'] == 'Cx86'
   

# Generated at 2022-06-13 00:57:00.402096
# Unit test for method get_dmi_facts of class NetBSDHardware
def test_NetBSDHardware_get_dmi_facts():
    # Prepare instance of class NetBSDHardware

    class MockModule(object):
        params = {'gather_timeout': 5}

    class MockModule2(object):
        params = {}

    hardware = NetBSDHardware(MockModule)
    hardware2 = NetBSDHardware(MockModule2)

    expected = {
        'product_name': 'VirtualBox',
        'product_version': '1.2',
        'product_uuid': '00000000-0000-0000-0000-000000000000',
        'product_serial': '0',
        'system_vendor': 'innotek GmbH'
    }


# Generated at 2022-06-13 00:57:01.989283
# Unit test for constructor of class NetBSDHardwareCollector
def test_NetBSDHardwareCollector():
    nhwc = NetBSDHardwareCollector()
    assert nhwc._fact_class == NetBSDHardware
    assert nhwc._platform == 'NetBSD'

# Generated at 2022-06-13 00:57:11.476113
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():

    # Getting diverse data
    class MockModule(object):
        def __init__(self):
            self.params = {}

        def run_command(self):
            return ('', '', 0)

    class MockCollector(object):
        def __init__(self, module):
            self.module = module

    module = MockModule()
    collector = MockCollector(module)
    hardware = NetBSDHardware(collector)
    facts = hardware.populate()

    # Lets check that we have the same data
    assert facts['devices'] == {}
    assert facts['processor_count'] > 0
    assert facts['processor_cores'] == 'NA'
    assert facts['processor'] == []
    assert facts['memfree_mb'] > 0
    assert facts['memtotal_mb'] > 0

# Generated at 2022-06-13 00:57:15.272581
# Unit test for method get_dmi_facts of class NetBSDHardware
def test_NetBSDHardware_get_dmi_facts():
    NetBSDHardware._module = NetBSDHardware._module
    NetBSDHardware._module.get_bin_path = lambda x: x
    netbsd_hw_instance = NetBSDHardware()
    result = netbsd_hw_instance.get_dmi_facts()
    assert 'system_vendor' in result

# Generated at 2022-06-13 00:57:18.125971
# Unit test for constructor of class NetBSDHardwareCollector
def test_NetBSDHardwareCollector():
    netbsd = NetBSDHardwareCollector()
    assert netbsd is not None
    assert netbsd._fact_class == NetBSDHardware
    assert netbsd._platform == 'NetBSD'

# Generated at 2022-06-13 00:57:29.601875
# Unit test for method populate of class NetBSDHardware

# Generated at 2022-06-13 00:57:33.221893
# Unit test for method get_memory_facts of class NetBSDHardware
def test_NetBSDHardware_get_memory_facts():
    netbsd_hardware_obj = NetBSDHardware()
    netbsd_hardware_obj.sysctl = {'hw.ncpu': '2', 'hw.physmem': '2147483648'}
    memory_facts = netbsd_hardware_obj.get_memory_facts()
    assert memory_facts['memtotal_mb'] == 2048
    assert memory_facts['swaptotal_mb'] == 0
    assert memory_facts['swapfree_mb'] == 0
    assert memory_facts['memfree_mb'] == 0


# Generated at 2022-06-13 00:58:17.212545
# Unit test for constructor of class NetBSDHardwareCollector
def test_NetBSDHardwareCollector():
    h = NetBSDHardwareCollector()
    assert NetBSDHardwareCollector._fact_class == NetBSDHardware
    assert NetBSDHardwareCollector._platform == 'NetBSD'

# Generated at 2022-06-13 00:58:22.544192
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    # Assert memtotal_mb is an integer
    hardware = NetBSDHardware()
    hardware.module = MockModule()
    hardware.populate()
    assert isinstance(hardware.memtotal_mb, int)

    # Assert processor_count is present and an integer
    hardware = NetBSDHardware()
    hardware.module = MockModule()
    hardware.populate()
    assert isinstance(hardware.processor_count, int)



# Generated at 2022-06-13 00:58:25.725693
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    facts = {}
    hardware = NetBSDHardware(module=None, facts=facts, timeout=5)
    hardware.populate()
    assert hardware.facts == {}
    assert hardware.sysctl == {}

# Generated at 2022-06-13 00:58:31.884271
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    hardware_facts = NetBSDHardwareCollector().collect()

    assert hardware_facts['processor_count'] == 1
    assert hardware_facts['processor_cores'] == 1
    assert hardware_facts['processor'][0] == 'CPU'
    assert hardware_facts['memtotal_mb'] > 0
    assert hardware_facts['memfree_mb'] > 0
    assert hardware_facts['swaptotal_mb'] > 0
    assert hardware_facts['swapfree_mb'] > 0
    assert hardware_facts['system_vendor'] == 'Intel Corporation'

# Generated at 2022-06-13 00:58:38.378705
# Unit test for method get_dmi_facts of class NetBSDHardware
def test_NetBSDHardware_get_dmi_facts():
    find_file_mock = MagicMock(return_value=True)
    open_mock = MagicMock(return_value=True)

    class TestHardware(NetBSDHardware):
        def __init__(self):
            self.sysctl = {
                'machdep.dmi.system-product': 'Product',
                'machdep.dmi.system-version': 'Version',
                'machdep.dmi.system-uuid': 'UUID',
                'machdep.dmi.system-serial': 'Serial',
                'machdep.dmi.system-vendor': 'Vendor',
            }
            self.sysctl_available = True

        @staticmethod
        def _filesystem_exists(path):
            return find_file_mock(path)


# Generated at 2022-06-13 00:58:47.334353
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    # Collect test data
    data_processor = ['Intel(R) Core(TM) i3-2310M CPU @ 2.10GHz',
                      'Intel(R) Core(TM) i3-2310M CPU @ 2.10GHz',
                      'Intel(R) Core(TM) i3-2310M CPU @ 2.10GHz',
                      'Intel(R) Core(TM) i3-2310M CPU @ 2.10GHz']
    data_processor_cores = 4
    data_processor_count = 4
    data_memtotal_mb = 2019032
    data_swaptotal_mb = 2047996
    data_swapfree_mb = 2047996
    data_memfree_mb = 404276
    data_system_vendor = 'NEC Corporation'
    data_product_name = 'VirtualBox'

# Generated at 2022-06-13 00:58:54.951130
# Unit test for method get_dmi_facts of class NetBSDHardware
def test_NetBSDHardware_get_dmi_facts():
    MOCK_GET_SYSCTL = {'machdep.dmi.system-product': 'TEST_PRODUCT',
                       'machdep.dmi.system-version': 'TEST_VERSION',
                       'machdep.dmi.system-uuid': 'TEST_UUID',
                       'machdep.dmi.system-serial': 'TEST_SERIAL',
                       'machdep.dmi.system-vendor': 'TEST_VENDOR'}

    hardware = NetBSDHardware()
    hardware.sysctl = MOCK_GET_SYSCTL
    hardware_dmi_facts = hardware.get_dmi_facts()

    assert hardware_dmi_facts['product_name'] == 'TEST_PRODUCT'

# Generated at 2022-06-13 00:59:05.277499
# Unit test for method get_dmi_facts of class NetBSDHardware
def test_NetBSDHardware_get_dmi_facts():
    hardware_obj = NetBSDHardware()
    hardware_obj.sysctl = {'machdep.dmi.system-product': 'Thinkpad T440p',
                           'machdep.dmi.system-version': 'Not Available',
                           'machdep.dmi.system-uuid': '56 F9 39 86 72 06 BA 89-82 E5 1C 04 AE B1 1E 2B',
                           'machdep.dmi.system-serial': 'R9GXXH1',
                           'machdep.dmi.system-vendor': 'LENOVO'}

# Generated at 2022-06-13 00:59:11.421599
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    module = type('DummyModule', (object,), dict(params=dict()))()
    fact_class = NetBSDHardware(module)

    facts = fact_class.populate()

    assert 'processor' in facts
    assert facts['processor_count'] > 0
    assert facts['processor_cores'] >= facts['processor_count']
    assert facts['memtotal_mb'] > 0
    assert facts['memfree_mb'] > 0
    assert facts['swaptotal_mb'] >= 0
    assert facts['swapfree_mb'] >= 0



# Generated at 2022-06-13 00:59:21.662351
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    m = NetBSDHardwareCollector(None)
    results = m.collect()
    assert 'mounts' in results['ansible_facts']['ansible_mounts']
    for key in ('fstype', 'mount', 'options', 'size_available', 'size_total'):
        assert key in results['ansible_facts']['ansible_mounts'][0]
    assert 'processor' in results['ansible_facts']
    assert 'processor_cores' in results['ansible_facts']
    assert 'processor_count' in results['ansible_facts']
    assert 'product_name' in results['ansible_facts']
    assert 'system_vendor' in results['ansible_facts']
    assert 'product_version' in results['ansible_facts']
    assert 'product_uuid' in results

# Generated at 2022-06-13 01:00:08.978269
# Unit test for method get_dmi_facts of class NetBSDHardware
def test_NetBSDHardware_get_dmi_facts():
    m_get_file_content = '''machdep.dmi.system-product='System Product Name'
machdep.dmi.system-version='System Version'
machdep.dmi.system-uuid='00000000-0000-0000-0000-000000000000'
machdep.dmi.system-serial='System Serial Number'
machdep.dmi.system-vendor='System Vendor'''

# Generated at 2022-06-13 01:00:13.198182
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    collected_facts = {'ansible_system': 'NetBSD'}
    hardware_facts = NetBSDHardware(module=None).populate(collected_facts=collected_facts)

    assert hardware_facts['processor_count'] > 0

# Generated at 2022-06-13 01:00:22.566700
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    module = FakeModule()
    hw = NetBSDHardware(module)
    facts = hw.populate()
    assert facts['processor_count'] == 1
    assert facts['processor_cores'] == 1
    assert 'processor' in facts
    assert facts['MemTotal_mb'] == 1016
    assert facts['MemFree_mb'] == 504
    assert facts['SwapTotal_mb'] == 2559
    assert facts['SwapFree_mb'] == 2559
    mounts = facts['mounts']
    assert len(mounts) == 1
    assert mounts[0]['fstype'] == 'hammer'
    assert mounts[0]['mount'] == '/'
    assert mounts[0]['device'] == '/dev/vn0'
    assert mounts[0]['options'] == 'rw'

# Generated at 2022-06-13 01:00:23.367601
# Unit test for constructor of class NetBSDHardwareCollector
def test_NetBSDHardwareCollector():
    assert issubclass(NetBSDHardwareCollector, HardwareCollector)

# Generated at 2022-06-13 01:00:24.867693
# Unit test for constructor of class NetBSDHardwareCollector
def test_NetBSDHardwareCollector():
    collector = NetBSDHardwareCollector()
    assert collector.get_fact_class() == NetBSDHardware

# Generated at 2022-06-13 01:00:35.482860
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    netbsd_hw = NetBSDHardware({'gather_subset': ['!all', '!min']})
    ioerror_patch = mock.patch('ansible.module_utils.facts.hardware.netbsd.open',
                               side_effect=IOError)
    with ioerror_patch as mock_open:
        netbsd_hw.populate()
        assert not mock_open.called

    nocreate_patch = mock.patch('os.access',
                                side_effect=lambda x, y: True if y == os.R_OK else False)
    with nocreate_patch as mock_access:
        netbsd_hw.populate()
        assert mock_access.call_count == 4


# Generated at 2022-06-13 01:00:45.090108
# Unit test for method get_memory_facts of class NetBSDHardware
def test_NetBSDHardware_get_memory_facts():
    assert NetBSDHardware({}).get_memory_facts() == {}
    os.access = lambda path, mode: True
    target_get_meminfo = {'memtotal_mb': 2, 'swaptotal_mb': 4, 'memfree_mb': 8, 'swapfree_mb': 16}

# Generated at 2022-06-13 01:00:52.637761
# Unit test for method get_dmi_facts of class NetBSDHardware
def test_NetBSDHardware_get_dmi_facts():
    """Method ne get_dmi_facts of class NetBSDHardware return the dictionary like {'product_name': '',
    'product_version': '', 'product_uuid': '', 'product_serial': '', 'system_vendor': ''}
    """
    netbsd_hardware = NetBSDHardware()
    netbsd_hardware.sysctl = {
        'machdep.dmi.system-product': 'test',
        'machdep.dmi.system-version': 'test',
        'machdep.dmi.system-uuid': 'test',
        'machdep.dmi.system-serial': 'test',
        'machdep.dmi.system-vendor': 'test'
    }


# Generated at 2022-06-13 01:01:02.324710
# Unit test for method get_cpu_facts of class NetBSDHardware

# Generated at 2022-06-13 01:01:06.720914
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    from ansible.module_utils.facts.collector import TestModule

    module = TestModule()
    harware = NetBSDHardware(module)

    facts = harware.populate()
    assert 'processor' in facts
    assert 'memfree_mb' in facts
    assert 'machdep' in facts['ansible_facts']['sysctl']
    assert 'mounts' in facts

# Generated at 2022-06-13 01:01:55.226431
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    harw = NetBSDHardware(None)
    setattr(harw, "module", None)
    assert isinstance(harw.populate(), dict)

# Generated at 2022-06-13 01:01:59.512699
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    hardware_obj = NetBSDHardware()

    #Call method populate of class NetBSDHardware
    hardware_obj.populate()

    #Verify processed facts
    assert 'processor_cores' in hardware_obj.facts
    assert 'processor_count' in hardware_obj.facts
    assert 'processor' in hardware_obj.facts
    assert 'memtotal_mb' in hardware_obj.facts
    assert 'swaptotal_mb' in hardware_obj.facts
    assert 'dmi_system_vendor' in hardware_obj.facts
    assert 'dmi_product_serial' in hardware_obj.facts
    assert 'dmi_system_uuid' in hardware_obj.facts
    assert 'dmi_product_version' in hardware_obj.facts
    assert 'dmi_product_name' in hardware_obj.facts

# Generated at 2022-06-13 01:02:07.522984
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    netbsd_hw = NetBSDHardware()

    try:
        netbsd_hw.populate()
    except NotImplementedError as exc:
        # We're on an unsupported platform
        assert netbsd_hw.platform == netbsd_hw.sysname
        assert "populate() is not implemented" in str(exc)
    else:
        assert netbsd_hw.platform == netbsd_hw.sysname
        assert 'processor' in netbsd_hw.facts
        assert 'processor_cores' in netbsd_hw.facts
        assert 'processor_count' in netbsd_hw.facts
        assert 'memtotal_mb' in netbsd_hw.facts
        assert 'memfree_mb' in netbsd_hw.facts
        assert 'swaptotal_mb' in netbsd

# Generated at 2022-06-13 01:02:12.267594
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    module = AnsibleModuleMock()
    set_module_args(dict())
    NetBSDHardware(module).populate()
    # Check for methods that should be called
    assert module.get_file_content.call_count == 2
    assert module.get_file_lines.call_count == 1
    assert module.get_sysctl.call_count == 1

if __name__ == '__main__':
    from ansible.module_utils.basic import *
    from ansible.module_utils.facts import *
    from units.mock.procfs import ProcFileSystemMock

    module = AnsibleModuleMock()
    hardware_collector = NetBSDHardwareCollector(module=module)
    hardware_collector.collect()
    facts = module.exit_json.call_args[0][1]

# Generated at 2022-06-13 01:02:23.441940
# Unit test for method get_dmi_facts of class NetBSDHardware
def test_NetBSDHardware_get_dmi_facts():
    import collections

    module = collections.namedtuple('module', ['params'])
    hardware = NetBSDHardware(module(params=dict()))

    hardware.sysctl = {
        'machdep.dmi.system-product': 'VirtualBox',
        'machdep.dmi.system-version': '1.2',
        'machdep.dmi.system-uuid': '3',
        'machdep.dmi.system-serial': '4',
        'machdep.dmi.system-vendor': '5'
    }
    facts = hardware.get_dmi_facts()


# Generated at 2022-06-13 01:02:30.456393
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    hardware = NetBSDHardware({})
    hardware_facts = hardware.populate()

    assert hardware_facts['processor'][0] == 'Intel(R) Xeon(R) CPU E5-2683 v3 @ 2.00GHz'
    assert hardware_facts['processor_cores'] == 12
    assert hardware_facts['processor_count'] == 2
    assert hardware_facts['memtotal_mb'] == 32108
    assert hardware_facts['memfree_mb'] == 13515
    assert hardware_facts['swaptotal_mb'] == 102399
    assert hardware_facts['swapfree_mb'] == 102399
    assert hardware_facts['product_name'] == 'KVM'
    assert hardware_facts['product_version'] == ''
    assert hardware_facts['product_uuid'] == ''

# Generated at 2022-06-13 01:02:41.322723
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    # Create a instance of NetBSDHardware to test its method populate
    netbsd_hw = NetBSDHardware()

    # Create bogus data to make tests.
    # bogus_sysctl store the data for the sysctl(8) command

# Generated at 2022-06-13 01:02:50.375126
# Unit test for method get_dmi_facts of class NetBSDHardware
def test_NetBSDHardware_get_dmi_facts():
    class Module():
        def __init__(self):
            self.module = None

    class GetSysctl():
        def __init__(self, mydmi):
            self.mydmi = mydmi

        def get_sysctl(self, name):
            return self.mydmi


# Generated at 2022-06-13 01:02:51.966717
# Unit test for constructor of class NetBSDHardwareCollector
def test_NetBSDHardwareCollector():
    hc = NetBSDHardwareCollector()
    assert isinstance(hc, NetBSDHardwareCollector)


# Generated at 2022-06-13 01:02:56.812429
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    # *********************************************************************** #
    # This method is patched for now, because without network it is           #
    # impossible to gather enough information to construct valid facts.       #
    # Without e.g. a valid ip address, a successful call to dnslookup will    #
    # not be possible. A successful fact gathering would require the setup    #
    # of a complete network stack, or a modification of the dnslookup method  #
    # in the module_utils.                                                    #
    # *********************************************************************** #
    pass

# Generated at 2022-06-13 01:03:56.628714
# Unit test for constructor of class NetBSDHardwareCollector
def test_NetBSDHardwareCollector():
    netbsd_hardware = NetBSDHardwareCollector()

if __name__ == '__main__':
    test_NetBSDHardwareCollector()

# Generated at 2022-06-13 01:04:06.429004
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    my_obj = NetBSDHardware()
    my_obj.module = AnsibleModuleMock()

    my_obj.sysctl = {
        'machdep.dmi.system-product': 'VirtualBox',
        'machdep.dmi.system-vendor': 'innotek GmbH',
        'machdep.dmi.system-version': '1.2-1234',
        'machdep.dmi.system-uuid': 'a0a1a2a3-b1b2-c3c4-d5d6-e7e8f9fafa1a',
        'machdep.dmi.system-serial': '2.0-1234-1234',
    }

    out = my_obj.populate()

# Generated at 2022-06-13 01:04:12.008488
# Unit test for method get_cpu_facts of class NetBSDHardware
def test_NetBSDHardware_get_cpu_facts():
    nh = NetBSDHardware()
    cpu_facts = nh.get_cpu_facts()
    assert cpu_facts['processor_count'] == 2
    assert cpu_facts['processor_cores'] == 1
    assert cpu_facts['processor'][0] == 'Intel(R) Atom(TM) CPU  E600  @ 1.50GHz'
    assert cpu_facts['processor'][1] == 'Intel(R) Atom(TM) CPU  E600  @ 1.50GHz'


# Generated at 2022-06-13 01:04:15.699030
# Unit test for constructor of class NetBSDHardwareCollector
def test_NetBSDHardwareCollector():
    assert NetBSDHardwareCollector._platform == 'NetBSD'
    assert NetBSDHardwareCollector._fact_class is NetBSDHardware
    assert NetBSDHardwareCollector.platform == 'NetBSD'
    assert NetBSDHardwareCollector.fact_class is NetBSDHardware


# Generated at 2022-06-13 01:04:17.691617
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    module = None

    # No assert for now since we have no way to mock the kernel part
    NetBSDHardwareCollector(module).collect()

# Generated at 2022-06-13 01:04:20.220135
# Unit test for method get_memory_facts of class NetBSDHardware
def test_NetBSDHardware_get_memory_facts():
    new_NetBSDHardware = NetBSDHardware()
    result = new_NetBSDHardware.get_memory_facts()
    assert result['swaptotal_mb'] == 818752


# Generated at 2022-06-13 01:04:25.838433
# Unit test for method get_dmi_facts of class NetBSDHardware
def test_NetBSDHardware_get_dmi_facts():
    facts = NetBSDHardware({"ANSIBLE_SYSTEM_MODULES": "/path/to/fake/sysctl.d"})
    expected_facts = {
        "product_name": "Laptop",
        "product_version": "14.04.3 LTS",
        "product_uuid": "AABBCCDD-AABB-CCDD-EEFF-0123456789AB",
        "product_serial": "CZ125A",
        "system_vendor": "System76",
    }
    assert facts.get_dmi_facts() == expected_facts

# Generated at 2022-06-13 01:04:27.781633
# Unit test for constructor of class NetBSDHardwareCollector
def test_NetBSDHardwareCollector():
    hc = NetBSDHardwareCollector()
    assert hc._fact_class == NetBSDHardware
    assert hc._platform == 'NetBSD'


# Generated at 2022-06-13 01:04:28.544299
# Unit test for constructor of class NetBSDHardwareCollector
def test_NetBSDHardwareCollector():
    NetBSDHardwareCollector()

# Generated at 2022-06-13 01:04:31.650311
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    netbsd_hw = NetBSDHardware(dict())
    netbsd_hw.module = lambda: None
    netbsd_hw.module.run_command = lambda x: '2' if x == 'getconf LONG_BIT' else ''
    assert 'mounts' in netbsd_hw.populate()