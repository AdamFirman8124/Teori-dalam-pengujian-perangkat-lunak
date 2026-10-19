

# Generated at 2022-06-13 00:58:31.508102
# Unit test for method get_cpu_facts of class NetBSDHardware
def test_NetBSDHardware_get_cpu_facts():
    hw = NetBSDHardware()
    hw.module._socket_patch('/proc/cpuinfo', 'netbsd_cpuinfo')
    hw.populate()
    assert hw.facts['processor_count'] == 2
    assert hw.facts['processor_cores'] == 3

# Generated at 2022-06-13 00:58:36.314953
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    hardware_inst = NetBSDHardware(dict())
    facts = hardware_inst.populate()
    # We can't assert any specific value, as they depend on the system
    # so let's just make sure keys are present
    assert 'memfree_mb' in facts
    assert 'memtotal_mb' in facts
    assert 'swapfree_mb' in facts
    assert 'swaptotal_mb' in facts
    assert 'processor' in facts
    assert 'processor_cores' in facts
    assert 'processor_count' in facts
    assert 'devices' in facts

# Generated at 2022-06-13 00:58:39.823772
# Unit test for constructor of class NetBSDHardwareCollector
def test_NetBSDHardwareCollector():
    netbsdhw = NetBSDHardwareCollector()
    # NetBSDHardwareCollector is properly subclassed from HardwareCollector
    assert issubclass(netbsdhw.__class__, HardwareCollector)


# Generated at 2022-06-13 00:58:48.438664
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    hardware = NetBSDHardware()
    facts = dict()
    facts['ansible_processor'] = ['Intel(R) Xeon(R) CPU E5-2650 v3 @ 2.30GHz', 'Intel(R) Xeon(R) CPU E5-2650 v3 @ 2.30GHz']
    facts['ansible_processor_cores'] = 8
    facts['ansible_processor_count'] = 2
    facts['ansible_memfree_mb'] = 12179
    facts['ansible_memtotal_mb'] = 786432
    facts['ansible_swapfree_mb'] = 615580
    facts['ansible_swaptotal_mb'] = 615580

# Generated at 2022-06-13 00:58:49.912024
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    netbsdhardware = NetBSDHardware({})
    assert netbsdhardware.populate() != None

# Generated at 2022-06-13 00:58:59.014498
# Unit test for method get_dmi_facts of class NetBSDHardware
def test_NetBSDHardware_get_dmi_facts():
    class NetBSDHardwareMock(NetBSDHardware):
        def __init__(self, *args, **kwargs):
            self.sysctl = {'machdep.dmi.system-product': 'foo',
                           'machdep.dmi.system-version': 'bar',
                           'machdep.dmi.system-uuid': 'baz',
                           'machdep.dmi.system-serial': 'eggspam'}
            super(self.__class__, self).__init__(*args, **kwargs)

    test_obj = NetBSDHardwareMock({})

# Generated at 2022-06-13 00:59:04.119721
# Unit test for method get_dmi_facts of class NetBSDHardware
def test_NetBSDHardware_get_dmi_facts():
    module = type('AnsibleModule', (), dict(params={}))()
    hardware = NetBSDHardware(module)
    hardware.sysctl = {
        'machdep.dmi.system-product': 'SomeProduct',
        'machdep.dmi.system-version': '1.0',
        'machdep.dmi.system-uuid': '00000000-0000-0000-0000-000000000000',
        'machdep.dmi.system-serial': 'ABCDEFGHIJKL12345',
        'machdep.dmi.system-vendor': 'SomeVendor',
    }
    dmi_facts = hardware.get_dmi_facts()
    assert dmi_facts['product_name'] == 'SomeProduct'
    assert dmi_facts['product_version'] == '1.0'


# Generated at 2022-06-13 00:59:11.384708
# Unit test for method get_memory_facts of class NetBSDHardware
def test_NetBSDHardware_get_memory_facts():
    m = NetBSDHardware()
    test_data = """MemTotal:       16454600 kB
SwapTotal:      8388604 kB
MemFree:        14069624 kB
SwapFree:       8388580 kB"""
    m.get_file_content = lambda x: test_data
    m.get_file_lines = lambda x: test_data.splitlines()
    res = m.get_memory_facts()

    assert res['memtotal_mb'] == 15939
    assert res['swaptotal_mb'] == 8192
    assert res['memfree_mb'] == 13744
    assert res['swapfree_mb'] == 8192



# Generated at 2022-06-13 00:59:21.633431
# Unit test for method get_dmi_facts of class NetBSDHardware
def test_NetBSDHardware_get_dmi_facts():
    """
    NetBSDHardware.get_dmi_facts() Test
    """
    netbsd = NetBSDHardware(dict(), dict())
    sysctl = {
        'machdep.dmi.system-product': 'TEST1',
        'machdep.dmi.system-version': 'TEST2',
        'machdep.dmi.system-uuid': 'TEST3',
        'machdep.dmi.system-serial': 'TEST4',
        'machdep.dmi.system-vendor': 'TEST5',
    }

    expected = dict([(key.replace('machdep.dmi.', ''), value) for (key, value) in sysctl.items()])
    class_sysctl = netbsd.get_dmi_facts()

# Generated at 2022-06-13 00:59:24.391582
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    hw = NetBSDHardware()
    hw.populate()

# Generated at 2022-06-13 01:02:44.346446
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    module = type('AnsibleModule', (object,), {'params': {'gather_subset': ['all']}})()
    ins = NetBSDHardware(module)
    ins.populate()
    assert 'processor' in ins.facts
    assert 'processor_cores' in ins.facts
    assert 'memtotal_mb' in ins.facts


if __name__ == '__main__':
    # Unit test
    import doctest
    doctest.testmod()

    # Run module as a script
    from ansible.module_utils.facts.collector import main
    main(NetBSDHardwareCollector)

# Generated at 2022-06-13 01:02:47.141467
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    hardware = NetBSDHardware()
    hardware_facts = hardware.populate()
    assert hardware_facts['processor_count'] > 0
    assert hardware_facts['memtotal_mb'] > 0
    assert hardware_facts['swaptotal_mb'] >= 0

# Generated at 2022-06-13 01:02:55.383234
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    module = AnsibleModuleMock()
    module.run_command = run_command
    netbsd_hw = NetBSDHardware(module)
    facts = netbsd_hw.populate()
    assert facts['mounts'][0]['mount'] == '/'
    assert facts['processor_cores'] == 2
    assert facts['processor_count'] == 2
    assert facts['processor'][0] == 'ARMv6-compatible processor rev 7 (v6l)'
    assert facts['processor'][1] == 'ARMv6-compatible processor rev 7 (v6l)'
    assert facts['memtotal_mb'] == 1016
    assert facts['memfree_mb'] == 92
    assert facts['swaptotal_mb'] == 0
    assert facts['swapfree_mb'] == 0

# Generated at 2022-06-13 01:02:56.441162
# Unit test for constructor of class NetBSDHardwareCollector
def test_NetBSDHardwareCollector():
    collector = NetBSDHardwareCollector()
    assert collector.collect() == collector._platform

# Generated at 2022-06-13 01:03:02.648803
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    module = 'ansible.module_utils.facts.hardware.netbsd'
    netbsd_hw = NetBSDHardware(module)
    cpu_facts = netbsd_hw.get_cpu_facts()
    memory_facts = netbsd_hw.get_memory_facts()
    dmi_facts = netbsd_hw.get_dmi_facts()
    assert cpu_facts['processor_cores'] > 0
    assert cpu_facts['processor_count'] > 0
    assert memory_facts['memtotal_mb'] > 0
    assert memory_facts['memfree_mb'] > 0
    assert memory_facts['swaptotal_mb'] > 0
    assert memory_facts['swapfree_mb'] >= 0
    assert dmi_facts['product_name'] != ''

# Generated at 2022-06-13 01:03:04.271350
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    hw = NetBSDHardware({}, True)
    hw.populate()

# Generated at 2022-06-13 01:03:14.937709
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    netbsd_hardware = NetBSDHardware()
    collected_facts = {
        'system_vendor': '',
        'processor': '',
        'devices': [],
        'mounts': None
    }


# Generated at 2022-06-13 01:03:22.427960
# Unit test for method get_dmi_facts of class NetBSDHardware
def test_NetBSDHardware_get_dmi_facts():
    class MockSysctl:
        def __init__(self, sysctl):
            self._sysctl = sysctl

        def __getitem__(self, key):
            if key in self._sysctl:
                return self._sysctl[key]
            raise KeyError(key)

    class MockModule:
        def __init__(self, sysctl=None):
            self._sysctl = sysctl

        def get_bin_path(self, executable, required=False):
            return "sysctl"

        def run_command(self, executable, args, check_rc=True):
            if executable != "sysctl":
                raise ValueError("Invalid executable '%s' invoked." % executable)
            key = args[0]

# Generated at 2022-06-13 01:03:24.426280
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    facts = NetBSDHardware()
    if hasattr(facts, 'populate'):
        facts.populate()
        assert('mounts' in facts.facts)
        assert('processor_cores' in facts.facts)

# Generated at 2022-06-13 01:03:29.730024
# Unit test for method get_dmi_facts of class NetBSDHardware
def test_NetBSDHardware_get_dmi_facts():
    netbsd_hardware = NetBSDHardware({})
    netbsd_hardware.sysctl = {'machdep.dmi.system-product': 'fooproduct',
                              'machdep.dmi.system-version': '1.0',
                              'machdep.dmi.system-uuid': 'bb88b5e5-b1f3-405e-9c57-2d0aacfdc8e8',
                              'machdep.dmi.system-serial': '123456789',
                              'machdep.dmi.system-vendor': 'foovendor'}
    dmi_facts = netbsd_hardware.get_dmi_facts()
    assert dmi_facts['product_name'] == 'fooproduct'
    assert dmi