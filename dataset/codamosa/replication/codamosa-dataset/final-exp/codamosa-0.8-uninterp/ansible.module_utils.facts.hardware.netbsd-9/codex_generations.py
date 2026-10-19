

# Generated at 2022-06-13 00:57:28.451696
# Unit test for constructor of class NetBSDHardwareCollector
def test_NetBSDHardwareCollector():

    obj = NetBSDHardwareCollector()
    assert obj.__class__.__name__ == 'NetBSDHardwareCollector'
    assert obj._fact_class.__name__ == 'NetBSDHardware'
    assert obj._platform == 'NetBSD'

# Generated at 2022-06-13 00:57:32.179279
# Unit test for constructor of class NetBSDHardwareCollector
def test_NetBSDHardwareCollector():
    netbsd_hw_collector = NetBSDHardwareCollector()
    assert netbsd_hw_collector.platform == 'NetBSD'
    assert netbsd_hw_collector.fact_class == NetBSDHardware

# Generated at 2022-06-13 00:57:34.003545
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    """
    Test method NetBSDHardware.populate
    """
    fact_module = NetBSDHardware()
    fact_module.populate()

# Generated at 2022-06-13 00:57:35.711699
# Unit test for constructor of class NetBSDHardwareCollector
def test_NetBSDHardwareCollector():
    netbsd_hardware_collector = NetBSDHardwareCollector()
    assert netbsd_hardware_collector is not None

# Generated at 2022-06-13 00:57:47.056691
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    # check that populate works with different types of sysctls
    test_sysctl = {
        'machdep.dmi.system-product': 'testproduct',
        'machdep.dmi.system-vendor': 'testvendor',
        'machdep.dmi.system-version': 'testversion',
        'machdep.dmi.system-uuid': 'testuuid',
        'machdep.dmi.system-serial': 'testserial'
    }

    # mock the module (NetBSDHardware get_sysctl method will call the module)
    module = type('module', (object,), {})()
    module.get_bin_path = lambda x: x
    module.run_command = lambda x: (0, '', '')
    module.get_mount_size = get_mount_

# Generated at 2022-06-13 00:57:54.442356
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    hardware_facts = NetBSDHardware().populate()
    assert isinstance(hardware_facts, dict)
    assert 'processor' in hardware_facts
    assert 'processor_cores' in hardware_facts
    assert 'processor_count' in hardware_facts
    assert 'memtotal_mb' in hardware_facts
    assert 'memfree_mb' in hardware_facts
    assert 'swaptotal_mb' in hardware_facts
    assert 'swapfree_mb' in hardware_facts

# Generated at 2022-06-13 00:58:01.113673
# Unit test for method get_memory_facts of class NetBSDHardware
def test_NetBSDHardware_get_memory_facts():
    netbsd_obj = NetBSDHardware({'ansible_facts': {}}, None)
    memory_facts = netbsd_obj.get_memory_facts()
    assert isinstance(memory_facts, dict)
    assert 'memtotal_mb' in memory_facts
    assert 'memfree_mb' in memory_facts
    assert 'swaptotal_mb' in memory_facts
    assert 'swapfree_mb' in memory_facts
    assert isinstance(memory_facts['memtotal_mb'], int)
    assert isinstance(memory_facts['memfree_mb'], int)
    assert isinstance(memory_facts['swaptotal_mb'], int)
    assert isinstance(memory_facts['swapfree_mb'], int)

# Generated at 2022-06-13 00:58:03.855528
# Unit test for constructor of class NetBSDHardwareCollector
def test_NetBSDHardwareCollector():
    hc = NetBSDHardwareCollector()
    h = hc.collect()
    assert h.get('ansible_facts', {}).get('netbsd_hw_facts', {}).get('devices', []) == []


# Generated at 2022-06-13 00:58:13.347886
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    module = MockModule()
    hardware = NetBSDHardware(module)

    hardware.get_cpu_facts = Mock(return_value={'processor_cores': 'NA',
                                                'processor_count': 42,
                                                'processor': ['Intel(R) Xeon(R) CPU E3-1220 V2 @ 3.10GHz']})
    hardware.get_memory_facts = Mock(return_value={'memfree_mb': 955,
                                                   'memtotal_mb': 3911,
                                                   'swapfree_mb': 1253,
                                                   'swaptotal_mb': 1253})

# Generated at 2022-06-13 00:58:16.625493
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    collected_facts = {'ansible_os_family': 'BSD'}
    netbsdhw = NetBSDHardware()
    netbsdhw.populate(collected_facts)

    assert netbsdhw.facts['processor_count'] >= 0

# Generated at 2022-06-13 01:00:08.317088
# Unit test for method get_dmi_facts of class NetBSDHardware
def test_NetBSDHardware_get_dmi_facts():
    class MockModule:
        def __init__(self, value):
            self.value = value

        def run_command(self, cmd, check_rc=False):
            return (0, self.value, '')

    # No value
    mm = MockModule('')
    hw = NetBSDHardware(mm)
    dmi_facts = hw.get_dmi_facts()
    assert 'product_name' not in dmi_facts
    assert 'product_version' not in dmi_facts
    assert 'product_uuid' not in dmi_facts
    assert 'product_serial' not in dmi_facts
    assert 'system_vendor' not in dmi_facts

    # All values

# Generated at 2022-06-13 01:00:10.278073
# Unit test for constructor of class NetBSDHardwareCollector
def test_NetBSDHardwareCollector():
    """ Test the constructor of the class NetBSDHardwareCollector """
    obj = NetBSDHardwareCollector()
    assert obj.platform == "NetBSD"
    assert obj.fact_class == NetBSDHardware

# Generated at 2022-06-13 01:00:20.283629
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    mod = DummyModule()
    mod.facts = dict()
    mod.params = dict()
    mod.run_command = fake_run_command
    NetBSDHardwareCollector.populate(mod)

    assert 'processor' in mod.facts
    assert 'processor_cores' in mod.facts
    assert 'processor_count' in mod.facts
    assert 'memtotal_mb' in mod.facts
    assert 'memfree_mb' in mod.facts
    assert 'swaptotal_mb' in mod.facts
    assert 'swapfree_mb' in mod.facts
    assert 'devices' in mod.facts

    assert mod.facts['processor'][0] == 'Intel(R) Core(TM)2 Duo CPU     T7100  @ 1.80GHz'

# Generated at 2022-06-13 01:00:23.627062
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    m = NetBSDHardware()
    facts = m.populate()
    assert 'processor' in facts
    assert 'memtotal_mb' in facts
    assert 'memfree_mb' in facts
    assert 'swaptotal_mb' in facts
    assert 'swapfree_mb' in facts
    assert 'processor_cores' in facts
    assert 'processor_count' in facts

# Generated at 2022-06-13 01:00:29.158186
# Unit test for method populate of class NetBSDHardware

# Generated at 2022-06-13 01:00:39.396226
# Unit test for method get_memory_facts of class NetBSDHardware

# Generated at 2022-06-13 01:00:47.889260
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    """
    Test method populate of class NetBSDHardware
    """
    FakeModule = type('FakeModule', (object,), {})

# Generated at 2022-06-13 01:00:49.246921
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    netbsd_hw = NetBSDHardware(dict())
    netbsd_hw.populate()



# Generated at 2022-06-13 01:00:58.326461
# Unit test for method get_dmi_facts of class NetBSDHardware
def test_NetBSDHardware_get_dmi_facts():
    sysctl_dict = {'machdep.dmi.system-vendor': 'Lorem',
                   'machdep.dmi.system-product': 'Ipsum',
                   'machdep.dmi.system-version': '1.0',
                   'machdep.dmi.system-uuid': '00000000-0000-0000-0000-000000000000',
                   'machdep.dmi.system-serial': 'A1B2C3'}
    mh = NetBSDHardware(dict(), MockModule(sysctl=sysctl_dict))
    dmi_facts = mh.get_dmi_facts()

    assert 'product_name' in dmi_facts
    assert dmi_facts['product_name'] == 'Ipsum'

    assert 'product_version' in dmi_facts
    assert d

# Generated at 2022-06-13 01:00:59.594598
# Unit test for constructor of class NetBSDHardwareCollector
def test_NetBSDHardwareCollector():
    """Test NetBSDHardwareCollector"""
    NetBSDHardwareCollector()

# Generated at 2022-06-13 01:02:52.519955
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    m1 = NetBSDHardware({})
    facts = m1.populate()
    assert facts['processor'][0] == 'Intel(R) Core(TM) i7-5600U CPU @ 2.60GHz'
    assert facts['processor_count'] == 4
    assert facts['memtotal_mb'] == 16384
    assert facts['swaptotal_mb'] == 6144

# Generated at 2022-06-13 01:02:58.445031
# Unit test for method get_dmi_facts of class NetBSDHardware
def test_NetBSDHardware_get_dmi_facts():
    dmi_data = {
        'machdep.dmi.system-product': 'TEST',
        'machdep.dmi.system-version': 'TEST',
        'machdep.dmi.system-uuid': 'TEST',
        'machdep.dmi.system-serial': 'TEST',
        'machdep.dmi.system-vendor': 'TEST',
    }

    class FakeModule:
        def __init__(self):
            self.sysctl = dmi_data

    nhw = NetBSDHardware(module=FakeModule())
    nhw.get_dmi_facts() == dmi_data

# Generated at 2022-06-13 01:03:00.281148
# Unit test for method get_cpu_facts of class NetBSDHardware
def test_NetBSDHardware_get_cpu_facts():
    cpu_facts = NetBSDHardware({}).get_cpu_facts()
    assert 'processor' in cpu_facts or 'processor_count' in cpu_facts


# Generated at 2022-06-13 01:03:10.577807
# Unit test for method get_dmi_facts of class NetBSDHardware
def test_NetBSDHardware_get_dmi_facts():
    module = type('fake', (object,), {'run_command': lambda x: "test"})
    netbsd_hardware = NetBSDHardware(module)
    sysctl = {
        'machdep.dmi.system-product': 'product_name',
        'machdep.dmi.system-version': 'product_version',
        'machdep.dmi.system-uuid': 'product_uuid',
        'machdep.dmi.system-serial': 'product_serial',
        'machdep.dmi.system-vendor': 'system_vendor',
    }

    netbsd_hardware.sysctl = sysctl
    result = netbsd_hardware.get_dmi_facts()
    assert result == sysctl

    # Test with no return value
    netbsd

# Generated at 2022-06-13 01:03:16.005688
# Unit test for method get_cpu_facts of class NetBSDHardware
def test_NetBSDHardware_get_cpu_facts():
    fixture = NetBSDHardware()
    fixture.module.run_command = lambda args, **kwargs: (0, '/usr/include', '')
    output = fixture.get_cpu_facts()
    assert output == {'processor': ['Intel(R) Core(TM) i5-3210M CPU @ 2.50GHz'], 'processor_count': 4, 'processor_cores': 2}


# Generated at 2022-06-13 01:03:19.853967
# Unit test for method get_cpu_facts of class NetBSDHardware
def test_NetBSDHardware_get_cpu_facts():
    # Get a test fixture
    netbsd_hardware = NetBSDHardware()

    # Call the method
    cpu_facts = netbsd_hardware.get_cpu_facts()

    # Check the result
    assert cpu_facts['processor']
    assert 'processor_count' in cpu_facts
    assert int(cpu_facts['processor_count']) >= 1
    assert 'processor_cores' in cpu_facts
    assert int(cpu_facts['processor_cores']) >= 1

# Generated at 2022-06-13 01:03:24.600982
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    module = MockModule()
    nb_hw = NetBSDHardware(module)

    cpu_facts = {'processor_count': 2, 'processor_cores': 4, 'processor': ['Intel(R) Atom(TM) CPU  N270   @ 1.60GHz']}
    memory_facts = {'swaptotal_mb': 1023, 'swapfree_mb': 767, 'memtotal_mb': 1019, 'memfree_mb': 511}

    assert nb_hw.populate() == cpu_facts.update(memory_facts)

# Generated at 2022-06-13 01:03:27.413591
# Unit test for method get_cpu_facts of class NetBSDHardware
def test_NetBSDHardware_get_cpu_facts():
    netbsd_hardware = NetBSDHardware()

    cpu_facts = netbsd_hardware.get_cpu_facts()

    assert type(cpu_facts) is dict
    assert 'processor' in cpu_facts
    assert 'processor_cores' in cpu_facts
    assert 'processor_count' in cpu_facts



# Generated at 2022-06-13 01:03:32.567932
# Unit test for method get_dmi_facts of class NetBSDHardware
def test_NetBSDHardware_get_dmi_facts():
    nhw = NetBSDHardware()
    # Fake sysctl(8) output
    nhw.sysctl = {
        'machdep.dmi.system-product': 'VMware7,1',
        'machdep.dmi.system-version': 'None',
        'machdep.dmi.system-uuid': 'None',
        'machdep.dmi.system-serial': 'None',
        'machdep.dmi.system-vendor': 'VMware, Inc.',
    }
    # Our method should build a correct structure

# Generated at 2022-06-13 01:03:42.828796
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    nbsd_hw = NetBSDHardware()
    nbsd_hw.module = get_mock_module('NetBSD')
    nbsd_hw.sysctl = get_mock_syscall()
    nbsd_hw.mounts = [{
        'device': '/dev/sdz1',
        'mount': '/',
        'fstype': 'zfs',
        'options': 'rw',
        'size_total': 1610612736,
        'size_available': 1019695104,
    }]
    nbsd_hw.populate()
