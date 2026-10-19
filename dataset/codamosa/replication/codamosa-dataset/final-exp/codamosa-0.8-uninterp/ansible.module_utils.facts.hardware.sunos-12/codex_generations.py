

# Generated at 2022-06-13 01:06:29.579988
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    s = SunOSHardware()

    uptime_facts = s.get_uptime_facts()
    assert uptime_facts['uptime_seconds'] > 0

# Generated at 2022-06-13 01:06:39.564973
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():

    class MockModule(object):
        def __init__(self):
            self.run_command_environ_update = {}
        def run_command(self, args, check_rc=False, close_fds=True, executable=None, data=None, binary_data=False):
            return 1, '', 'Error'
        def get_bin_path(self, arg, opt_dirs=[]):
            if arg == "prtdiag":
                return "/usr/sbin/prtdiag"

    mock_module = MockModule()

    hardware = SunOSHardware(module=mock_module)

    facts = hardware.populate()

    assert hardware.uptime_facts == {'uptime_seconds': None}

# Generated at 2022-06-13 01:06:40.783176
# Unit test for constructor of class SunOSHardwareCollector
def test_SunOSHardwareCollector():
    SunOSHardwareCollector()

# Generated at 2022-06-13 01:06:49.561838
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    disks = {'sd0': {'hard_errors': 0, 'size': '5GiB', 'vendor': 'ATA', 'product': 'VBOX HARDDISK', 'predictive_failure_analysis': 0, 'media_errors': 0, 'serial': 'VB0ad2ec4d-074a', 'illegal_request': 6, 'soft_errors': 0, 'transport_errors': 0, 'revision': '1.0'}}
    assert SunOSHardware.get_device_facts(dict())['devices'] == disks

# Generated at 2022-06-13 01:06:50.625257
# Unit test for constructor of class SunOSHardwareCollector
def test_SunOSHardwareCollector():
    assert SunOSHardwareCollector.collect(dict()) is None

# Generated at 2022-06-13 01:06:56.456857
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    module = AnsibleModule(argument_spec={})
    hardware = SunOSHardware(module)
    facts = hardware.get_memory_facts()
    assert 'memtotal_mb' in facts
    assert 'swapfree_mb' in facts
    assert 'swaptotal_mb' in facts
    assert 'swap_allocated_mb' in facts
    assert 'swap_reserved_mb' in facts

# Generated at 2022-06-13 01:07:08.562631
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():

    class MockedModule:
        def __init__(self):
            # prtconf output
            self.mem = ("Memory size: 4096 Megabytes\n")
            # swap -s output
            self.swap = ("total: 74040k bytes allocated + 99328k reserved = 173368k used, \
                        109600k available\n")

        def run_command(self, command):
            if command[0] == "/usr/sbin/prtconf":
                return (0, self.mem, '')
            elif command[0] == "/usr/sbin/swap -s":
                return (0, self.swap, '')
            else:
                return (0, '', '')

    mocked_module = MockedModule()

    h = SunOSHardware(mocked_module)
    mem

# Generated at 2022-06-13 01:07:21.203468
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    h = SunOSHardware(None)
    h.module = FakeAnsibleModule()
    h.populate()

# Generated at 2022-06-13 01:07:32.479986
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    from ansible.module_utils.facts.os.sunos.hardware import SunOSHardware
    sun_obj = SunOSHardware()

    kstat_prtconf_output = {
        "command": ["/usr/sbin/prtconf"],
        "rc": 0,
        "stdout": "Memory size: 20480 Megabytes",
        "stderr": ""
    }

    kstat_swaps_output = {
        "command": ["/usr/sbin/swap", "-s"],
        "rc": 0,
        "stdout": "total: 131064k bytes allocated + 161724k reserved = 292788k used, 5696664k available",
        "stderr": ""
    }


# Generated at 2022-06-13 01:07:34.168045
# Unit test for constructor of class SunOSHardwareCollector
def test_SunOSHardwareCollector():
    SunOSHardwareCollector()

# Generated at 2022-06-13 01:07:59.350184
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    # init class
    sh = SunOSHardware()

    # populate method
    d = sh.populate()

    assert 'processor' in d
    assert 'memtotal_mb' in d
    assert 'swapfree_mb' in d
    assert 'swaptotal_mb' in d
    assert 'swap_allocated_mb' in d
    assert 'swap_reserved_mb' in d
    assert 'mounts' in d
    assert 'system_vendor' in d
    assert 'product_name' in d
    assert 'devices' in d
    assert 'uptime_seconds' in d

# Generated at 2022-06-13 01:08:02.793113
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    module = DummyModule()
    hardware = SunOSHardware({}, module)
    dmi_facts = hardware.get_dmi_facts()
    assert dmi_facts == {
        'system_vendor': 'Sun Microsystems',
        'product_name': 'Sun Fire V490',
    }


# Generated at 2022-06-13 01:08:13.502418
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    # Test case 1:
    #   * Solaris 11.4, Oracle Corporation (prtdiag)
    test_in = 'System Configuration: Oracle Corporation sun4v SPARC T5-2'
    test_out = {'system_vendor': 'Oracle Corporation', 'product_name': 'sun4v SPARC T5-2'}
    assert SunOSHardware().get_dmi_facts({'platform': 'SunOS'}) == {}
    assert SunOSHardware().get_dmi_facts({'platform': 'SunOS', 'ansible_facts': {}}) == {}
    assert SunOSHardware().get_dmi_facts({'platform': 'SunOS', 'ansible_facts': {'dmi': {}}}) == {}

# Generated at 2022-06-13 01:08:15.436298
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    module = FakeAnsibleModule()
    h = SunOSHardware(module)
    cpu_facts = h.get_cpu_facts()
    assert cpu_facts['processor_count'] == 8
    assert cpu_facts['processor_cores'] == 32


# Generated at 2022-06-13 01:08:22.436386
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    class test_module():
        def run_command():
            pass

        def get_bin_path():
            pass

    class test_SunOSHardware(SunOSHardware):
        def __init__(self, module):
            self.module = test_module()

    test_obj = test_SunOSHardware(None)
    test_obj.get_device_facts()


if __name__ == '__main__':
    from ansible.module_utils.facts.hardware.sunos import SunOSHardware

    facts = SunOSHardware().populate()
    for k, v in sorted(facts.items()):
        print("%s: %s" % (k, v))

# Generated at 2022-06-13 01:08:32.951946
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():

    # Test case: run_command fails
    # Expected behaviour: module completes with failure
    mock_module = Mock(run_command=Mock(return_value=(1, '', '')))
    hardware_facts = SunOSHardware(mock_module).populate()
    assert not hardware_facts['failed']

    # Test case: run_command succeeds
    # Expected behaviour: module completes with succes
    mock_module = Mock(run_command=Mock(return_value=(0, '', '')))
    hardware_facts = SunOSHardware(mock_module).populate()
    assert not hardware_facts['failed']



# Generated at 2022-06-13 01:08:41.701179
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    _module = FakeModule()
    SunOSHardware(_module)
    _module.get_bin_path.side_effect = ['/usr/bin/kstat']

# Generated at 2022-06-13 01:08:45.578775
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    module = type('module', (object,), {'run_command_environ_update': {} })
    module.run_command = lambda *args, **kw: (0 ,'', '')
    sunoshardware = SunOSHardware(module)
    assert sunoshardware.populate()

# Generated at 2022-06-13 01:08:48.835033
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    hardware = SunOSHardware(dict(module=None))
    d = hardware.get_device_facts()
    assert d == {}

# Generated at 2022-06-13 01:08:57.972747
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    """
    This is an integration test.  The actual output of commands like swap(1M)
    or prtconf(1M) can't really be known in advance.  This is probably best
    done with an integration test.  Unfortunately, this
    test actually depends on the test environment having a swap partition.
    """

    module_mock = MockModule()

    hardware_instance = SunOSHardware(module_mock)
    facts = hardware_instance.populate()

    assert 'memtotal_mb' in facts
    assert 'swapfree_mb' in facts
    assert 'swaptotal_mb' in facts
    assert 'swap_allocated_mb' in facts
    assert 'swap_reserved_mb' in facts
    assert 'devices' in facts
    assert 'mounts' in facts

# Generated at 2022-06-13 01:09:18.494211
# Unit test for constructor of class SunOSHardwareCollector
def test_SunOSHardwareCollector():
    hardwareCollector = SunOSHardwareCollector()
    assert hardwareCollector is not None


# Generated at 2022-06-13 01:09:30.610101
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    module = AnsibleModule(argument_spec={})
    hardware = SunOSHardware(module)
    facts = hardware.get_device_facts()
    assert 'vendor' in facts['devices']['sda'], facts['devices']['sda']
    assert 'hard_errors' in facts['devices']['sda'], facts['devices']['sda']
    assert 'size' in facts['devices']['sda'], facts['devices']['sda']
    assert 'serial' in facts['devices']['sda'], facts['devices']['sda']
    assert 'predictive_failure_analysis' in facts['devices']['sda'], facts['devices']['sda']

# Generated at 2022-06-13 01:09:34.014326
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    collection = SunOSHardwareCollector()
    test_hardware_facts = collection.populate()
    assert 'system_vendor' in test_hardware_facts
    assert 'product_name' in test_hardware_facts


# Generated at 2022-06-13 01:09:39.141517
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    import json
    from ansible.module_utils.facts.hardware.sunos import SunOSHardware
    module = FakeModule()
    hardware = SunOSHardware(module)
    facts = hardware.populate()
    assert 'processor' in facts
    assert facts['processor_cores'] == facts['processor_count']
    assert facts['processor'] == ['Genuine Intel(R) CPU 0000 @ 2133.000MHz']
    assert facts['processor_count'] == 2
    assert facts['processor_cores'] == 2


# Generated at 2022-06-13 01:09:45.489120
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    from ansible.module_utils.facts.hardware.sunos import SunOSHardware

    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=['all'], type='list')
        )
    )

    hardware = SunOSHardware(module)
    system_vendor, product_name = hardware.get_dmi_facts()
    assert system_vendor == 'QEMU'
    assert product_name == 'Standard PC (i440FX + PIIX, 1996)'

# Generated at 2022-06-13 01:09:50.916538
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    """
    test_SunOSHardware_get_device_facts is a unit test for method get_device_facts of class SunOSHardware.
    """
    import ansible.module_utils.facts.hardware.sunos as sunos

    my_object = sunos.SunOSHardware()
    devices = my_object.get_device_facts()
    assert isinstance(devices['devices'], dict)
    assert 'sd0' in devices['devices']
    assert 'sd1' not in devices['devices']



# Generated at 2022-06-13 01:10:00.565467
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    class MockModule(object):
        def __init__(self, out, rc=0):
            self.out = out
            self.rc = rc

        def run_command(self, cmd):
            return (self.rc, self.out, None)

    # Test for empty out
    module = MockModule(out='')
    harware = SunOSHardware(module)
    assert harware.get_device_facts() == {}

    # Test for invalid out
    module = MockModule(out='error')
    harware = SunOSHardware(module)
    assert harware.get_device_facts() == {}

    # Test for empty out
    module = MockModule(out='sderr:0:sd0,err:Product VBOX HARDDISK   9')
    harware = SunOSHardware(module)
    assert har

# Generated at 2022-06-13 01:10:12.308143
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    """
    Test method get_cpu_facts of class SunOSHardware
    """

    # Test1: SunOSHardware.get_cpu_facts() Test
    # Arrange
    test_module = type('Module', (object,), {'run_command': test_run_command})

# Generated at 2022-06-13 01:10:22.060092
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    # Create a sample module for test
    module = AnsibleModule(argument_spec={})

    # Create a instance of SunOSHardware class
    hardware_obj = SunOSHardware(module)

    # Create a sample prtdiag output
    sample_prtdiag_output = """System Configuration: Sun Microsystems sun4u
Sun Microsystems sun4u
Memory size: 8192 Megabytes"""

    # Store correct vendor, product name, and memtotal_mb
    correct_vendor = "Sun Microsystems"
    correct_product_name = "sun4u"
    correct_memtotal_mb = 8192

    # Check get_device_facts() method
    dmi_facts = hardware_obj.get_dmi_facts()
    assert dmi_facts['system_vendor'] == correct_vendor
    assert dmi_

# Generated at 2022-06-13 01:10:23.782405
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    module = AnsibleModule(argument_spec={})
    SunOSHardware.populate(SunOSHardware(), module)

# Generated at 2022-06-13 01:11:05.380217
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    import os
    import json
    import StringIO

    context = {}
    context['module'] = {}
    context['module']['run_command'] = _mock_run_command

    m = SunOSHardware()
    m.module = context['module']
    m.get_uptime_facts()

    assert m.uptime_facts['uptime_seconds'] == 1234

# Unit test helper method to mock 'run_command' method of module object

# Generated at 2022-06-13 01:11:07.850563
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    m = SunOSHardware()
    d = m.get_device_facts()
    assert isinstance(d, dict)


# Generated at 2022-06-13 01:11:08.827304
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    SunOSHardware().populate()

# Generated at 2022-06-13 01:11:16.873645
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    module = FakeModule()
    hardware_facts = SunOSHardware(module)

    # Initialize expected hardware facts
    hardware_facts.ansible_facts['dmi']['system_vendor'] = 'Sun Microsystems'
    hardware_facts.ansible_facts['dmi']['product_name'] = 'Sun Fire 280R'

    # Populate SunOSHardware with get_dmi_facts method
    hardware_facts.get_dmi_facts()

    # Verify if retrieved facts are the same as expected
    assert (hardware_facts.ansible_facts == {
        'dmi': {
            'system_vendor': 'Sun Microsystems',
            'product_name': 'Sun Fire 280R'
        }
    })



# Generated at 2022-06-13 01:11:23.080553
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    module = AnsibleModuleMock()
    module.run_command_environ_update = {'LANG': 'C', 'LC_ALL': 'C', 'LC_NUMERIC': 'C'}
    sunos_hardware = SunOSHardware(module)

    # SunOS-i86pc-10-current (unstable):

# Generated at 2022-06-13 01:11:31.935414
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    SunOSHardware_obj = SunOSHardware(dict())

    # Return data from prtdiag

# Generated at 2022-06-13 01:11:38.140397
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    """
    Unit test for method get_device_facts of class SunOSHardware.
    """
    from ansible.module_utils.facts.hardware.sunos import SunOSHardware

    device_facts = {
        "devices": {
            "sda": {
                "hard_errors": "0",
                "illegal_request": "0",
                "media_errors": "0",
                "predictive_failure_analysis": "0",
                "product": "QEMU HARDDISK",
                "revision": "1.0",
                "serial": "drive-ide0-1-0",
                "size": "10.00 GB",
                "soft_errors": "0",
                "transport_errors": "0",
                "vendor": "ATA",
            }
        },
    }



# Generated at 2022-06-13 01:11:50.520069
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    from ansible.module_utils.facts.collector.sunos import SunOSHardware
    from ansible.module_utils.facts.hardware.sunos import SunOSHardwareCollector
    from ansible.module_utils.facts.utils import get_file_content
    import socket

    # initializing data
    hardware = SunOSHardware({'module': None, 'lockfile': None, 'running_on_master': False})


# Generated at 2022-06-13 01:11:55.481891
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    hardware = SunOSHardware()
    hardware.module = FakeAnsibleModule()
    hardware.module.run_command = MagicMock(return_value=(0, 'System Configuration: Sun Microsystems sun4u', None))
    dmi_facts = hardware.get_dmi_facts()
    assert dmi_facts['system_vendor'] == 'Sun Microsystems'
    assert dmi_facts['product_name'] == 'sun4u'



# Generated at 2022-06-13 01:12:01.334910
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    module = MagicMock()
    module.run_command.return_value = (0, EXAMPLE_KSTAT_OUTPUT, None)
    sunos_hw = SunOSHardware(module)
    result = sunos_hw.get_cpu_facts()
    assert type(result) is dict
    assert 'processor' in result
    assert 'processor_count' in result
    assert 'processor_cores' in result
    assert result['processor'] == ['Sun UltraSPARC-III+ @ 1667MHz', 'Sun UltraSPARC-III+ @ 1667MHz']
    assert result['processor_count'] == 2
    assert result['processor_cores'] == 64



# Generated at 2022-06-13 01:12:50.106237
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    module = AnsibleModule(
        argument_spec={
            'filter': {'required': False, 'type': 'list'}
        }
    )

    # Create a mock of the command '/usr/sbin/prtconf'
    mock_module = MagicMock()
    mock_module.run_command = MagicMock(
        return_value=(
            0,
            "Memory size: 64 Megabytes\n"
            "System Peripherals (Software Nodes):\n"
            "  SUNW,Sun-Fire-V240\n"
            "  SUNW,Sun-Fire-V240\n",
            ''
        )
    )
    # Create an instance of SunOSHardware
    obj = SunOSHardware(module=mock_module)
    # Call method get_memory_facts of class SunOSHardware using

# Generated at 2022-06-13 01:12:51.722436
# Unit test for constructor of class SunOSHardwareCollector
def test_SunOSHardwareCollector():
    collector = SunOSHardwareCollector()
    assert collector is not None

# Generated at 2022-06-13 01:12:57.323112
# Unit test for constructor of class SunOSHardwareCollector
def test_SunOSHardwareCollector():
    module = AnsibleModule(argument_spec=dict())
    shared_facts = SharedFactsBase()
    collector = SunOSHardwareCollector(module=module, shared_facts=shared_facts)

    assert collector.required_facts == collector._fact_class.required_facts
    assert collector._platform == collector._fact_class.platform
    assert collector.platform == collector._fact_class.platform
    assert collector.fact_class == collector._fact_class
    assert collector.fact_class().get_memory_facts() is not None
    assert collector.fact_class().get_dmi_facts() is not None



# Generated at 2022-06-13 01:13:04.433022
# Unit test for constructor of class SunOSHardwareCollector
def test_SunOSHardwareCollector():
    # Fake module
    class FakeModule(object):
        HOST_META = {
            'data': [
                {'path': 'constructed_by',
                 'value': 'SunOSHardwareCollector'}
            ]
        }

    # Create object for class SunOSHardwareCollector
    collector = SunOSHardwareCollector(FakeModule)

    # Check result of method get_fact_class
    assert 'hardware' == collector.get_fact_class()

    # Check result of method get_platform
    assert 'SunOS' == collector.get_platform()

    # Check result of method get_required_facts
    assert set(['platform']) == collector.get_required_facts()

# Generated at 2022-06-13 01:13:11.643710
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    modules = dict(
        run_command=dict(
            return_value=(0, "System Configuration: VMware, Inc. VMware Virtual Platform (1.0)\n", "")
        )
    )
    # initialize the class
    obj = SunOSHardware(module=FakeModule(**modules))
    obj.get_dmi_facts()
    assert obj.sys_vendor == 'VMware, Inc.'
    assert obj.product_name == 'VMware Virtual Platform'

# Generated at 2022-06-13 01:13:19.254699
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    class MockModule:
        def __init__(self):
            self.run_command_results = []
            self.run_command_calls = []

        def run_command(self, args):
            self.run_command_calls.append(args)
            return self.run_command_results.pop(0)

    class MockFacts:
        def __init__(self, platform):
            self.ansible_facts = {
                'ansible_facts': {
                    'platform': platform
                },
            }

    class MockSunOSHardware():
        def __init__(self, module, collected_facts):
            self.module = module
            self.collected_facts = collected_facts


# Generated at 2022-06-13 01:13:25.416018
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    module = FakeAnsibleModule()
    obj = SunOSHardware(module)
    rc, out, err = module.run_command("/usr/bin/kstat cpu_info")

    cpu_facts = get_cpu_facts(module)

    brand = ''
    physid = 0
    sockets = {}

    for line in out.splitlines():
        if len(line) < 1:
            continue

        data = line.split(None, 1)
        key = data[0].strip()

        # "brand" works on Solaris 10 & 11. "implementation" for Solaris 9.
        if key == 'module:':
            brand = ''
        elif key == 'brand':
            brand = data[1].strip()
        elif key == 'clock_MHz':
            clock_mhz = data[1].strip()

# Generated at 2022-06-13 01:13:35.022171
# Unit test for method get_memory_facts of class SunOSHardware

# Generated at 2022-06-13 01:13:42.444016
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    class TestModule:
        def run_command_environ_update(self, args):
            pass

        def get_bin_path(self, exe, opt_dirs=None):
            return "/usr/bin/kstat"

        def run_command(self, args):
            if isinstance(args, str):
                args = str.split(args)
            if args[0] != "/usr/bin/kstat":
                return 1, '', ''
            if args[1] != "cpu_info":
                return 1, '', ''
            return 0, '''module: cpu_info
instance: 0
clock_MHz  3000
chip_id    1
implementation     SPARC-Enterprise
brand      sun4v
''', ''


# Generated at 2022-06-13 01:13:53.323392
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    # case1
    test_module = SunOSHardware()
    test_module.module.run_command = (lambda x: (0, 'System Configuration: \
                                                 Sun Microsystems sun4v SPARC Enterprise T5220', ''))

    assert test_module.get_dmi_facts() == {'system_vendor': 'Sun Microsystems', 'product_name': 'sun4v SPARC Enterprise T5220'}

    # case2
    test_module = SunOSHardware()
    test_module.module.run_command = (lambda x: (0, 'System Configuration: \
                                                 Oracle Corporation sun4v SPARC Enterprise T5220', ''))


# Generated at 2022-06-13 01:14:43.416021
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    import ansible.module_utils.facts.hardware.sunos

    hostname = ansible.module_utils.facts.hardware.sunos.SunOSHardware()
    out = hostname.populate()
    assert isinstance(out, dict)

# Generated at 2022-06-13 01:14:49.164437
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    test_device_facts = {}
    test_device_facts['devices'] = {}
    test_device_facts['devices']['sda'] = {}
    test_device_facts['devices']['sda']['vendor'] = 'ATA'
    test_device_facts['devices']['sda']['product'] = 'VBOX HARDDISK'
    test_device_facts['devices']['sda']['serial'] = 'VB0ad2ec4d-074a'
    test_device_facts['devices']['sda']['revision'] = '1.0'
    test_device_facts['devices']['sda']['size'] = '53687091200'
    test_device_facts['devices']['sda']['soft_errors'] = '0'

# Generated at 2022-06-13 01:14:58.587741
# Unit test for method populate of class SunOSHardware

# Generated at 2022-06-13 01:15:06.718975
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    """Test populate for SunOSHardware class."""
    mock_module = MockModule()
    mock_module.get_bin_path = Mock(return_value='/usr/bin/prtdiag')

    facts = {}
    hardwarecollector = SunOSHardwareCollector(mock_module)
    hardwareinstance = hardwarecollector.collect(facts)
    assert hardwareinstance.populate()['memory_mb']['real']['total'] == 16384
    assert hardwareinstance.populate()['processor'][0] == 'Sun Microsystems SPARC Enterprise T5120'
    assert hardwareinstance.populate()['processor_cores'] == 16
    assert hardwareinstance.populate()['processor_count'] == 1
    assert hardwareinstance.populate()['system_vendor'] == 'Oracle Corporation'

# Generated at 2022-06-13 01:15:11.428519
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    device_facts = SunOSHardware.get_device_facts(None)
    assert 'devices' in device_facts


# We use this to allow Solaris to match more generically as a Unix platform
# and let the SunOS Hardware subclass define the platform more specifically.
collect_subset = ['!all', '!min']
# Solaris uses kstat rather than sysctl so there is a seperate collection
# method defined in this class.
collect_subset.append('hardware')

# For testing module outside of ansible
if __name__ == '__main__':
    SunOSHardwareCollector.main()

# Generated at 2022-06-13 01:15:19.459981
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    expected_cpu_facts = {
        'processor': ['SPARC64-VII (chipid 0, clock 2300 MHz) @ 2300MHz'],
        'processor_cores': 2,
        'processor_count': 2
    }
    # unit test for SPARC hardware
    hardware = SunOSHardware()
    hardware.module = DummyAnsibleModule()
    hardware.module.run_command.side_effect = run_command
    collected_facts = {}
    collected_facts['ansible_machine'] = 'sun4v'
    try:
        cpu_facts = hardware.get_cpu_facts(collected_facts)
    except:
        cpu_facts = None
    assert cpu_facts == expected_cpu_facts


# Generated at 2022-06-13 01:15:25.894553
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    results = {}

    # Set values for test
    results['ansible_machine'] = 'i86pc'

    # Test with i86pc
    facts = SunOSHardware().get_cpu_facts(results)

    assert len(facts) == 4
    assert facts['processor'][0] == 'GenuineIntel'
    assert facts['processor_cores'] == 'NA'
    assert facts['processor_count'] == 2
    assert facts['processor'][1] == 'GenuineIntel @ 2400MHz'

    # Test with sparcv9
    results['ansible_machine'] = 'sparcv9'
    facts = SunOSHardware().get_cpu_facts(results)

    assert facts['processor'][0] == 'GenuineIntel @ 2400MHz'
    assert facts['processor_cores'] == 2

# Generated at 2022-06-13 01:15:27.619950
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    # setup
    h = SunOSHardware({})
    # execute
    result = h.populate()
    # verify
    assert result



# Generated at 2022-06-13 01:15:38.078814
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    import json
    import sys

    # Mock module
    class MockModule():
        def __init__(self):
            self.run_command_environ_update = None
        def run_command(self, args, check_rc=True):
            if 'kstat cpu_info' in args:
                return 0, "module: cpu_info\nbrand\t\tGenuineIntel\nchip_id\t\t\t0\nclock_MHz\t\t2394.858\nimplementation\t\tIntel(r) Xeon(r) CPU E5-2697 v2 @ 2.70GHz\n", ""
            elif 'prtconf' in args:
                return 0, "Memory size: 8192 Megabytes\n", ""

# Generated at 2022-06-13 01:15:44.727521
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    hardware = SunOSHardware()
    hardware.solaris_cpu_data = '''module:   cpu_info
instance: 0
class:    misc
chip_id   0
clock_MHz 1550
core_id   0
implementation  SPARC-T5
model    48
module   cpu_info
state    ok
brand    sunw,SPARC-T5
revision  0x3000085
serial_number unknown
'''
    hardware.solaris_data_dict = {'ansible_machine': 'i86pc'}
    ansible_facts = hardware.populate()

    assert ansible_facts['processor'] == ['SPARC-T5 @ 1550MHz']
    assert ansible_facts['processor_count'] == 1
    assert ansible_facts['processor_cores'] == 1
