

# Generated at 2022-06-13 00:35:06.303029
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    module = None

    expected = {
        'model': 'iMac11,3',
        'osversion': '16.7.0',
        'osrevision': '19414'
    }

    darwin_hardware = DarwinHardware(module)
    darwin_hardware.sysctl = {
        'kern.osversion': '16.7.0',
        'kern.osrevision': '19414'
    }
    darwin_hardware.module.run_command = lambda *arg: [0, 'iMac11,3\n', '']
    fact = darwin_hardware.get_mac_facts()
    assert fact == expected



# Generated at 2022-06-13 00:35:08.038413
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    hardware = DarwinHardware()
    hardware.get_cpu_facts()

# Generated at 2022-06-13 00:35:17.085907
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    mac_facts = {'model': 'MacBookPro13,2', 'osversion': '19.5.0', 'osrevision': 'Core'}
    mock_module = MockModule()
    get_sysctl_return = {'kern.osversion': '19.5.0', 'kern.osrevision': 'Core'}
    mock_module.run_command.return_value = (0, 'hw.model: MacBookPro13,2', '')

    hardware = DarwinHardware(mock_module)
    hardware.sysctl = get_sysctl_return

    assert(hardware.get_mac_facts() == mac_facts)



# Generated at 2022-06-13 00:35:27.119865
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    module = type('obj', (object,), {'run_command': test_DarwinHardware_run_command,
                                     'get_bin_path': test_DarwinHardware_get_bin_path})
    obj = DarwinHardware()
    obj.module = module
    hardware_facts = obj.populate()

# Generated at 2022-06-13 00:35:31.310831
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    module = MockModule()
    darwinHardware = DarwinHardware(module)
    macFacts = darwinHardware.get_mac_facts()
    assert macFacts['model'] == 'MacBookPro8,1'
    assert macFacts['osversion'] == '15.6.0'
    assert macFacts['osrevision'] == '19G73'



# Generated at 2022-06-13 00:35:40.904640
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    from ansible.module_utils.six import PY3
    from ansible.module_utils._text import to_bytes

    facts = DarwinHardware()

    import sys

    if sys.version_info[0] < 3:
        out1 = 'hw.model: cylinder\n'
        out2 = 'kern.osversion: 14.5.0\n'
        out3 = 'kern.osrevision: Darwin Kernel Version 14.5.0: Mon Jul 25 13:08:30 PDT 2016; root:xnu-2782.40.9~1/RELEASE_X86_64\n'
    else:
        out1 = to_bytes('hw.model: cylinder\n')
        out2 = to_bytes('kern.osversion: 14.5.0\n')

# Generated at 2022-06-13 00:35:47.272830
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    class MockModule:
        def run_command(self, command):
            return (0, 'sysctl: unknown oid \'hw.model\'', '')
    module = MockModule()
    darwin_hw = DarwinHardware(module)
    facts = darwin_hw.get_mac_facts()
    assert facts['product_name'] == ''
    assert facts['model'] == ''


# Generated at 2022-06-13 00:35:58.427070
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    module = AnsibleModule(argument_spec={})

    class TestDarwinHardware(DarwinHardware):
        def __init__(self):
            self.module = module

        def run_command(self, cmd, encoding=None):
            # Return the output of the `uptime` command.
            cmd_dir, cmd_file = os.path.split(cmd[0])
            if cmd_file == 'uptime':
                uptime_cmd = cmd
            else:
                uptime_cmd = ['/usr/bin/uptime']
            return module.run_command(uptime_cmd)

    hw = TestDarwinHardware()
    uptime_facts = hw.get_uptime_facts()
    assert uptime_facts['uptime_seconds'] == 10, uptime_facts['uptime_seconds']

# Generated at 2022-06-13 00:36:07.778418
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    import ansible.module_utils.facts.hardware.darwin as darwin

    module = MagicMock()
    # Un-set facts, so test methods get_mac_facts(), get_cpu_facts() and
    # get_memory_facts() will run
    module.params = dict(gather_subset=[])

    dh = darwin.DarwinHardware(module)

    # mock run_command return value of sysctl hw.model
    dh.module.run_command.side_effect = [
        (0, "hw.model: MacBookPro10,2", None),
    ]

    # mock run_command return value of sysctl kern.osversion

# Generated at 2022-06-13 00:36:15.116330
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    class MockModule(object):
        @staticmethod
        def run_command(*_args, **_kwargs):
            return 0, struct.pack('@L', 0), ''

        @staticmethod
        def get_bin_path(*_args, **_kwargs):
            return 'sysctl'

    module = MockModule()
    hardware = DarwinHardware(module)
    result = hardware.get_uptime_facts()
    assert result == {'uptime_seconds': int(time.time())}


# Generated at 2022-06-13 00:36:29.358285
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    # TODO: write unit test for method get_uptime_facts of class DarwinHardware
    # TODO: test get_uptime_facts for different values of kern.boottime
    return

# Generated at 2022-06-13 00:36:38.040956
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    test_module = FakeModule()

# Generated at 2022-06-13 00:36:40.449436
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    """ This method instantiates DarwinHardwareCollector without any arguments
    and makes sure that it doesn't throw any exceptions
    """
    DarwinHardwareCollector()

# Generated at 2022-06-13 00:36:52.941320
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    hw = DarwinHardware()
    hw.sysctl = {
            'machdep.cpu.brand_string': 'Intel(R) Core(TM) i7-6850K CPU @ 3.60GHz',
            'machdep.cpu.core_count': 6,
    }
    cpu_facts = hw.get_cpu_facts()
    assert cpu_facts['processor'] == 'Intel(R) Core(TM) i7-6850K CPU @ 3.60GHz'
    assert cpu_facts['processor_cores'] == 6
    assert cpu_facts['processor_vcpus'] is None

    hw = DarwinHardware()
    hw.sysctl = {
            'hw.physicalcpu': 4,
            'hw.logicalcpu': 8,
    }
    cpu_facts = hw.get_cpu_

# Generated at 2022-06-13 00:37:03.753473
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    import sys
    module_name = 'ansible.module_utils.facts.hardware.darwin'
    test_module = sys.modules[module_name]
    test_DarwinHardware_instance = DarwinHardware()

    # This is the test data.
    # It is a raw bytes representation of struct timeval.
    # struct timeval {
    #     time_t      tv_sec;     /* seconds */
    #     suseconds_t tv_usec;    /* microseconds */
    # };
    kern_boottime = b'\x00\x00\x00\x00 \x00'
    test_DarwinHardware_instance.module.run_command = lambda cmd, encoding=None: (0, kern_boottime, '')

    result = test_DarwinHardware_instance.get_uptime_facts()

# Generated at 2022-06-13 00:37:13.547611
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    module = FakeAnsibleModule()
    module.run_command = MockRunCommand()

# Generated at 2022-06-13 00:37:22.236322
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    import sys
    if sys.version_info[0] == 3:
        from unittest.mock import patch
    else:
        from mock import patch
    module = patch.object(DarwinHardware, 'module')
    fake_module = module.start()
    fake_module.run_command.return_value = [0, "hw.machdep.cpu.brand_string: Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz", ""]
    darwin_hardware = DarwinHardware()
    cpu_facts = darwin_hardware.get_cpu_facts()
    assert cpu_facts['processor'] == 'Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz'

# Generated at 2022-06-13 00:37:32.614090
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    class Options(object):
        quiet = False
        verbosity = 0
        timeout = 10
    class ModuleMock():
        def __init__(self, *args, **kwargs):
            self.run_command = self.run_command_mock
            self.params = {}
            self.check_mode = False


# Generated at 2022-06-13 00:37:43.179528
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    from ansible.module_utils._text import to_bytes

    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=False
    )

    mac_facts = module.params['ansible_facts']

    osversion = mac_facts['ansible_os_version']
    if osversion.startswith('10.9') or osversion.startswith('10.10'):
        mac_facts['ansible_product_name'] = 'MacBookPro11,3'
        mac_facts['ansible_processor'] = '2.6 GHz Intel Core i7'
        mac_facts['ansible_processor_cores'] = 4
        mac_facts['ansible_processor_vcpus'] = 8
        mac_facts['ansible_memtotal_mb'] = 16384

# Generated at 2022-06-13 00:37:49.064120
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    # Test 1, vm_stat command not present
    module = AnsibleModule(argument_spec={})
    hardware_obj = DarwinHardware(module, 'hw')
    hardware_obj.get_bin_path = MagicMock(return_value=None)
    result = hardware_obj.get_memory_facts()
    assert result == {'memtotal_mb': 0, 'memfree_mb': 0}

    # Test 2, vm_stat command present and no output
    module = AnsibleModule(argument_spec={})
    hardware_obj = DarwinHardware(module, 'hw')
    hardware_obj.get_bin_path = MagicMock(return_value='/usr/bin/vm_stat')
    hardware_obj.module.run_command = MagicMock(return_value=(0, None, None))
    result = hardware_obj

# Generated at 2022-06-13 00:38:09.012172
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    hardware = DarwinHardware()
    hardware.sysctl = {
        'machdep.cpu.brand_string': 'Intel(R) Xeon(R) CPU E5-2630 v3 @ 2.40GHz',
        'machdep.cpu.core_count': '16',
        'hw.physicalcpu': '16',
        'hw.logicalcpu': '32',
    }
    cpu_facts = hardware.get_cpu_facts()
    assert cpu_facts['processor_cores'] == 16
    assert cpu_facts['processor'] == 'Intel(R) Xeon(R) CPU E5-2630 v3 @ 2.40GHz'
    assert cpu_facts['processor_vcpus'] == 32


# Generated at 2022-06-13 00:38:17.427837
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    import os

    # Create a module object
    fake_module = type(os)('ansible_fake_module')
    fake_module.run_command = lambda *args, **kwargs: (0, '', '')

    # Create a DarwinHardware object with a mocked run_command
    darwin_hw = DarwinHardware(fake_module)

# Generated at 2022-06-13 00:38:19.650924
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    h = DarwinHardwareCollector()
    assert h.get_platform() == 'Darwin'


# Generated at 2022-06-13 00:38:24.257817
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    collector = DarwinHardwareCollector()
    assert isinstance(collector, HardwareCollector)
    assert collector.platform == 'Darwin'
    assert collector.fact_class == DarwinHardware

# Unit test to test DarwinHardware instantiation

# Generated at 2022-06-13 00:38:36.084005
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    import ansible
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware

    hardware_facts = DarwinHardware()
    memory_stats = dict()

    total_used = 0
    page_size = 4096

    memory_stats['Pages wired down'] = '0'
    memory_stats['Pages active'] = '9077'
    memory_stats['Pages inactive'] = '7469'
    memory_stats['Pages free'] = '17776'

    if memory_stats.get('Pages wired down'):
        total_used += int(memory_stats['Pages wired down']) * page_size
    if memory_stats.get('Pages active'):
        total_used += int(memory_stats['Pages active']) * page_size

# Generated at 2022-06-13 00:38:44.223369
# Unit test for method get_memory_facts of class DarwinHardware

# Generated at 2022-06-13 00:38:56.496758
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
  module = AnsibleModuleMock()

# Generated at 2022-06-13 00:39:04.082387
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    class MockModule(object):
        def __init__(self, raw_out, raw_err, rc):
            self.raw_out = raw_out
            self.raw_err = raw_err
            self.rc = rc

        def run_command(self, cmd, encoding=None):
            return (self.rc, self.raw_out, self.raw_err)

        def get_bin_path(self, cmd):
            return cmd

    btime = int(time.time())
    btime_packed = struct.pack('@L', btime)

    hw = DarwinHardware()
    hw.module = MockModule(btime_packed, None, 0)

    facts = hw.get_uptime_facts()
    assert facts['uptime_seconds'] == int(time.time() - btime)

# Generated at 2022-06-13 00:39:16.107869
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    # On OSX, the output is like:
    # sysctl -b hw.machdep.cpu.brand_string
    # Intel(R) Core(TM) i5-5257U CPU @ 2.70GHz
    # sysctl -b hw.physicalcpu
    # 4
    # sysctl -b hw.logicalcpu
    # 8

    # Test with Intel CPU
    # Test with known value
    sysctl = {'machdep.cpu.brand_string': 'Intel(R) Core(TM) i5-5257U CPU @ 2.70GHz',
              'hw.physicalcpu': 4,
              'hw.logicalcpu': 8}

    hardware = DarwinHardware(dict(), None)
    hardware.sysctl = sysctl
    cpu_facts = hardware.get_cpu_facts()

    assert cpu_

# Generated at 2022-06-13 00:39:22.286267
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    module = AnsibleModule(argument_spec={
        'module_setup': {
            'type': 'bool',
            'default': False,
        },
    })

    hardware = DarwinHardware({'PATH': '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'}, module=module)
    # This tests works only on Darwin hosts, so we can mock the sysctl
    # binary to simulate an arbitrary uptime.
    #
    # We could also use the kernel_boottime fixture from Ansible’s test
    # suite, but that would only allow us to test one fixed time.
    #
    # To test a value other than 0, we have to “fake” the sysctl command
    # and its output to contain the Unix epoch.
    desired_uptime = 0


# Generated at 2022-06-13 00:39:59.711827
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    sysctl_output = {
        'hw.ncpu': '8',
        'hw.physicalcpu': '4',
        'hw.logicalcpu': '8',
        'machdep.cpu.core_count': '4',
        'machdep.cpu.brand_string': 'Intel(R) Core(TM) i7-4850HQ CPU @ 2.30GHz',
    }

    hardware = DarwinHardware()
    hardware.sysctl = sysctl_output

    assert hardware.get_cpu_facts() == {
        'processor': 'Intel(R) Core(TM) i7-4850HQ CPU @ 2.30GHz',
        'processor_cores': '4',
        'processor_vcpus': '8',
    }



# Generated at 2022-06-13 00:40:00.647272
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    x = DarwinHardwareCollector()
    assert x

# Generated at 2022-06-13 00:40:04.484284
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    m = DarwinHardware(None)
    assert m.get_system_profile() == {'Model Identifier': 'MacBookPro8,1', 'Processor Name': 'Intel Core i7', 'Processor Speed': '2.2 GHz'}

# Generated at 2022-06-13 00:40:13.628487
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    module = MockModule()

    # Set up a fake sysctl output
    module.run_command = Mock(return_value=(0, sysctl_output, ''))


# Generated at 2022-06-13 00:40:20.354359
# Unit test for method populate of class DarwinHardware

# Generated at 2022-06-13 00:40:30.566053
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    module = None
    # Test with Intel CPU

# Generated at 2022-06-13 00:40:42.311415
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    import unittest
    import mock

    class MockModule(object):
        def __init__(self):
            pass

        def run_command(self, args, encoding=None):
            return (0, '0001^@\xec\xa9\x00\x00\x00\x00\x00\x00', None)

        def get_bin_path(self, cmd):
            return '/usr/sbin/sysctl'

    class MockTime(object):
        def __init__(self):
            pass

        def time(self):
            return 1455938961

    class TestDarwinHardware(unittest.TestCase):
        module = MockModule()
        time = MockTime()


# Generated at 2022-06-13 00:40:52.149775
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    try:
        import __builtin__ as builtins  # Python 2
    except ImportError:
        import builtins  # Python 3

    class MockModule(object):
        def get_bin_path(self, filename):
            return filename

        def run_command(self, command, encoding=None):
            if 'sysctl' in command:
                # Returns 2017-06-15 08:44:46 +0000
                return (0, '\x00\x00\x00\x00\xa8\x9d\x00\x00\xf2[\x01\x00\x00\x00\x01\x00\x00', None)
            return (0, 'Invalid command', None)

    class MockTime(object):
        def time(self):
            # Same date as in the sysctl output
            return

# Generated at 2022-06-13 00:40:59.909812
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    import sys
    if sys.version_info[0] == 2:
        from StringIO import StringIO
    else:
        from io import StringIO
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware


# Generated at 2022-06-13 00:41:03.052682
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    """
    Constructor test of class DarwinHardwareCollector
    """
    darwin_collector = DarwinHardwareCollector()
    assert darwin_collector.platform == 'Darwin'
    assert darwin_collector._fact_class == DarwinHardware

# Generated at 2022-06-13 00:41:58.655383
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    class_ = DarwinHardware
    sysctl = {'hw': {'memsize': '1024'}, 'kern': {'osversion': '8', 'osrevision': '3'}}
    obj = class_({'module_mock': {'run_command': lambda x, encoding=None: (0, '2', ''), 'get_bin_path': lambda x: x}}, sysctl=sysctl)

    obj.get_system_profile = lambda : {'Processor Name': '2', 'Processor Speed': '3'}
    rc, out, err = obj.module.run_command("sysctl hw.model")
    assert rc == 0
    assert out.splitlines()[-1].split() == ['hw.model:', '2']


# Generated at 2022-06-13 00:42:04.070376
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    system_profile = DarwinHardware().get_system_profile()
    assert system_profile['System Version'] == 'OS X 10.10.5 (14F27)'
    assert system_profile['Model Name'] == 'MacBook Air'
    assert system_profile['Processor Name'] == 'Intel Core i5'
    assert system_profile['Processor Speed'] == '1.4 GHz'
    assert system_profile['Boot ROM Version'] == 'MBLL.0045.B00'

# Generated at 2022-06-13 00:42:05.443195
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    obj = DarwinHardwareCollector()
    assert obj._fact_class == DarwinHardware
    assert obj._platform == 'Darwin'

# Generated at 2022-06-13 00:42:12.283155
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec={})
    module.sysctl = dict()

    # Intel
    module.sysctl['machdep.cpu.brand_string'] = 'Intel(R) Core(TM) i7-6920HQ CPU @ 2.90GHz'
    module.sysctl['machdep.cpu.core_count'] = '4'

    intel_cpu_facts = DarwinHardware(module).get_cpu_facts()

    assert intel_cpu_facts['processor'] == 'Intel(R) Core(TM) i7-6920HQ CPU @ 2.90GHz'
    assert intel_cpu_facts['processor_cores'] == '4'

    # PowerPC

# Generated at 2022-06-13 00:42:21.737492
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    # pylint: disable=protected-access
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    import os
    import tempfile

    darwin = DarwinHardware({'module': None, 'tmpdir': tempfile.gettempdir()})
    rc, out, err = os.system('which system_profiler > /dev/null 2>&1')
    if rc == 0:
        # If system_profiler is available, ensure it returns the expected type
        system_profile = darwin.get_system_profile()
        assert isinstance(system_profile, dict)
    else:
        # If system_profiler is not available, ensure it returns dict()
        system_profile = darwin.get_system_profile()
        assert isinstance(system_profile, dict)
        assert system_

# Generated at 2022-06-13 00:42:28.806443
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    from ansible.module_utils.facts.collector.hardware.darwin import DarwinHardware
    module = AnsibleModuleMock({})
    darwin = DarwinHardware(module)
    darwin.get_mac_facts = Mock()
    darwin.get_cpu_facts = Mock()
    darwin.get_memory_facts = Mock()
    darwin.get_uptime_facts = Mock()
    darwin.populate()
    darwin.get_mac_facts.assert_called_once()
    darwin.get_cpu_facts.assert_called_once()
    darwin.get_memory_facts.assert_called_once()
    darwin.get_uptime_facts.assert_called_once()



# Generated at 2022-06-13 00:42:33.997020
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    #
    # Module parameters
    #
    params = {
    }

    #
    # Test fixture
    #
    def get_bin_path(exe):
        """Dummy function that always return '/bin/sh'"""
        return '/bin/sh'

    #
    # Test procedure
    #
    darwinHardware = DarwinHardware(params, None)
    darwinHardware.module.get_bin_path = get_bin_path

    #
    # Default test
    #
    result = darwinHardware.populate()
    assert result.get('model') == 'MacBookPro10,1'

# Generated at 2022-06-13 00:42:44.147682
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    sysctl_cmd = '/usr/sbin/sysctl'

# Generated at 2022-06-13 00:42:48.756853
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    mac_facts = DarwinHardware().get_mac_facts()
    assert mac_facts['osversion'].startswith('16')
    assert mac_facts['osrevision'].startswith('16')
    assert mac_facts['model'].startswith('MacBook')


# Generated at 2022-06-13 00:42:57.137952
# Unit test for method get_cpu_facts of class DarwinHardware