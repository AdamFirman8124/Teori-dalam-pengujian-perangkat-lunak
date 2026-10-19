

# Generated at 2022-06-13 00:34:58.184591
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
	# We don't want the test to fail because we don't have the
	# tool on this system.
	from ansible.module_utils.facts.hardware.darwin import DarwinHardware
	import os
	import ansible.module_utils.facts.hardware.darwin
	backup_system_profiler = ansible.module_utils.facts.hardware.darwin.system_profiler
	ansible.module_utils.facts.hardware.darwin.system_profiler = '/usr/bin/which'

	# Run the test
	dummy_module = type('DummyModule', (), dict())()
	darwin_hardware = DarwinHardware(dummy_module)
	system_profile = darwin_hardware.get_system_profile()

	# Restore system_profiler
	ansible.module_utils.facts

# Generated at 2022-06-13 00:35:01.977430
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    system_profile = DarwinHardware._get_system_profile()
    assert system_profile['Serial Number (system)'] == 'ABCDEFG1234567'

# Generated at 2022-06-13 00:35:07.648742
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    d = DarwinHardware(module=None)
    d.sysctl = {'machdep.cpu.brand_string': 'Intel'}
    cpu_facts = d.get_cpu_facts()
    assert cpu_facts['processor'] == 'Intel'
    assert cpu_facts['processor_cores'] == '1'
    assert cpu_facts['processor_vcpus'] == ''

# Generated at 2022-06-13 00:35:18.031616
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    test_module = AnsibleModule(
        argument_spec=dict()
    )
    test_module.run_command = MagicMock(return_value=(0, '', ''))
    test_module.get_bin_path = MagicMock(return_value='run_command')
    dh = DarwinHardware(test_module)

    # Valid sysctl output

# Generated at 2022-06-13 00:35:28.426300
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    test_module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )
    test_DarwinHardware = DarwinHardware(test_module)
    test_DarwinHardware.sysctl = {'hw.memsize': 4294967296, 'hw.pagesize': 4096}
    test_DarwinHardware.module.run_command = lambda self, command: (0, "Pages free: 1106972.\nPages active: 879674.\nPages inactive: 847400.\nPages wired down: 211460.\n", "")
    memory_facts = test_DarwinHardware.get_memory_facts()
    assert memory_facts['memtotal_mb'] == 4096

# Generated at 2022-06-13 00:35:37.493626
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    module = MockModule()
    darwin_hardware = DarwinHardware(module=module)

    darwin_hardware.sysctl = {
            'hw.physicalcpu': 2,
            'hw.logicalcpu': 2,
            'machdep.cpu.brand_string': 'Intel Core i3 (3rd Gen) 2.50GHz',
            'machdep.cpu.core_count': 4
            }

    cpu_facts = {
            'processor': 'Intel Core i3 (3rd Gen) 2.50GHz',
            'processor_cores': 4,
            'processor_vcpus': 2
            }

    assert darwin_hardware.get_cpu_facts() == cpu_facts



# Generated at 2022-06-13 00:35:45.435176
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    # Build a mock module.
    import ansible.module_utils.facts.hardware.darwin
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware

    test_module = ansible.module_utils.facts.hardware.darwin.AnsibleModule(
        argument_spec=dict(
            filter=dict(default='', required=False),
            gather_subset=dict(default=['!all', '!min'], required=False),
        ),
        supports_check_mode=True
    )

    test_DarwinHardware = DarwinHardware(test_module)
    test_DarwinHardware.sysctl = {'hw.memsize': 1024}

    # Assert with a mock vmstat

# Generated at 2022-06-13 00:35:57.422601
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    class MockModule:
        def run_command(self, *args, **kwargs):
            if args[0] == ['/usr/sbin/system_profiler', "SPHardwareDataType"]:
                return (0, """

            Hardware:

              Hardware Overview:

                Model Name: MacBook Pro
                Model Identifier: MacBookPro13,1
                Processor Name: Dual-Core Intel Core i5
                Processor Speed: 2.9 GHz
                Number of Processors: 1
                Total Number of Cores: 2
                L2 Cache (per Core): 256 KB
                L3 Cache: 4 MB
                Memory: 8 GB
                Boot ROM Version: 1037.60.47.0.0 (iBridge: 17.16.10990.0.0,0)
                """, '')


# Generated at 2022-06-13 00:36:00.769102
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    """
    Test class constructor.
    """
    fact_class = DarwinHardwareCollector()

    assert fact_class._fact_class is DarwinHardware
    assert fact_class._platform == 'Darwin'



# Generated at 2022-06-13 00:36:08.923424
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    uptime_facts_values = dict()
    uptime_facts_values['uptime_seconds'] = 3600
    uptime_facts_test_values = dict()

    class MockModule:
        def __init__(self):
            self.run_command_results = [(0, b'{ epoch = 1512642654;' + b'\n  microseconds = 0;\n}', '')]
            self.run_command_calls = 0

        def get_bin_path(self, name):
            return '/usr/sbin/sysctl'

        def run_command(self, cmd, encoding=None):
            self.run_command_calls += 1
            if self.run_command_calls > len(self.run_command_results):
                return (-1, '', 'stubbed error')

           

# Generated at 2022-06-13 00:36:28.264576
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    class MockModule(object):
        def run_command(self, command):
            if command == ['vm_stat']:
                return 0, '''
Mach Virtual Memory Statistics: (page size of 4096 bytes, cache hits 0%)
free active   spec inactive   wire   faults     copy    0fill reactive   pageins  pageout
782144 528068114  91648 108790688 118620688 535520688    0    63326487848   9233855808     0
                ''', ''
            raise Exception('Unexpected command: %s' % ' '.join(command))

    mock_module = MockModule()

    def mock_get_bin_path(name):
        if name == 'vm_stat':
            return '/usr/bin/vm_stat'
        raise Exception('Unexpected command: %s' % name)

   

# Generated at 2022-06-13 00:36:31.588800
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    module = FakeAnsibleModule()
    module.run_command = Mock(side_effect=mocked_run_command)
    hardware = DarwinHardware(module=module)
    cpu_facts = hardware.get_cpu_facts()
    assert cpu_facts['processor_cores'] == '6'
    assert cpu_facts['processor_vcpus'] == '12'



# Generated at 2022-06-13 00:36:35.405160
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    dh = DarwinHardware(module)
    facts = dh.populate()
    assert facts['memtotal_mb'] > 0
    assert facts['memfree_mb'] >= 0
    assert facts['processor'] != ''

# Generated at 2022-06-13 00:36:42.789020
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    (rc, out, err) = module.run_command('sysctl machdep.cpu.brand_string')
    if rc == 0:
        cpu_facts = DarwinHardware().get_cpu_facts()
        assert cpu_facts['processor'] == out.splitlines()[-1].split()[1]
    else:
        (rc, out, err) = module.run_command('/usr/sbin/system_profiler SPHardwareDataType')
        if rc == 0:
            cpu_facts = DarwinHardware().get_cpu_facts()
            assert cpu_facts['processor'] == ' '.join(out.splitlines()[2].split()[1:])


# Generated at 2022-06-13 00:36:55.365158
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    from ansible.module_utils.facts.collector import BaseFactsCollector

    module = BaseFactsCollector.get_module()
    hardware = DarwinHardware(module)
    mac_facts = hardware.get_mac_facts()

    module.run_command.return_value = 0, '', ''
    module.run_command.side_effect = [
        (0, 'kern.osversion: 10.9.5\nkern.osrevision: 13F34', ''),
        (0, 'hw.model: MacBookAir6,2\nhw.memsize: 8589934592', ''),
        (0, 'hw.physicalcpu: 2\nhw.logicalcpu: 4', '')
        ]

    hardware.populate()


# Generated at 2022-06-13 00:37:07.640691
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    """Test get_memory_facts
    """

    class Options(object):

        def __init__(self):
            self.sudo = True
            self.sudo_user = None
            self.ask_sudo_pass = False
            self.ask_pass = False
            self.become = False
            self.become_method = None
            self.become_user = None
            self.ask_become_pass = False
            self.verbosity = 0

    class Module(object):

        def __init__(self):
            self.params = {}

        def get_bin_path(self, *args):
            return args[0]


# Generated at 2022-06-13 00:37:18.019881
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec=dict())
    hardware = DarwinHardware(module)

    hardware.sysctl = {
        'machdep.cpu.brand_string': 'Intel(R) ZX-4545L @ 2.35GHz',
        'machdep.cpu.core_count': '2',
    }

    cpu_facts = hardware.get_cpu_facts()
    assert cpu_facts['processor'] == hardware.sysctl['machdep.cpu.brand_string']
    assert int(cpu_facts['processor_cores']) == int(hardware.sysctl['machdep.cpu.core_count'])
    assert cpu_facts['processor_vcpus'] == hardware.sysctl.get('hw.logicalcpu') or hardware.sysctl.get('hw.ncpu') or ''

# Unit

# Generated at 2022-06-13 00:37:25.658353
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    import pytest

    class MockModule(object):
        # Keep the class names and doctest strings in sync with the
        # production implementation.

        def run_command(self, cmd, encoding=None):
            class MockRC(object):
                def __init__(self, returncode):
                    self.returncode = returncode

            if isinstance(cmd, list):
                cmd = ' '.join(cmd)

            if cmd == 'sysctl -b kern.boottime':
                # Return a raw string (bytes on Python 2 and unicode on
                # Python 3) for the mocked output of the sysctl
                # command.
                return MockRC(0), b'\x74\x16\x0c\x00\x8f\xdf\x00\x00', ''

# Generated at 2022-06-13 00:37:28.779336
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    module = type('FakeModule', (object,), dict(run_command=lambda cmd: (0, 'foo: bar\n', '')))()
    hardware = DarwinHardware(module)

    system_profile = hardware.get_system_profile()
    assert system_profile == dict(foo='bar')



# Generated at 2022-06-13 00:37:39.640719
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    hw = DarwinHardware(None)
    hw.get_system_profile = lambda: {
        'Processor Name': 'Intel(R) Core(TM) i7-6820HQ CPU @ 2.70GHz',
        'Processor Speed': '2.7 GHz'
    }
    hw.get_mac_facts = lambda: {}
    hw.get_memory_facts = lambda: {}
    hw.get_uptime_facts = lambda: {}
    hw.get_cpu_facts = lambda: {}

    facts = hw.populate()
    assert facts['processor'] == 'Intel(R) Core(TM) i7-6820HQ CPU @ 2.70GHz @ 2.7 GHz'
    assert facts['processor_cores'] == '4'

# Generated at 2022-06-13 00:38:08.645531
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    class MockModule:
        def __init__(self, params):
            self.params = params

        def run_command(self, command):
            if self.params['model'] == 'MacPro6,1':
                return (0, 'hw.model: Intel(R) Core(TM) i7-4870HQ CPU @ 2.50GHz', '')
            elif self.params['model'] == 'iMac14,2':
                return (0, 'hw.model: Intel(R) Core(TM) i5-4570R CPU @ 2.70GHz', '')
            elif self.params['model'] == 'iMac14,1':
                return (0, 'hw.model: Intel(R) Core(TM) i7-4771 CPU @ 3.50GHz', '')

# Generated at 2022-06-13 00:38:12.460694
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    """
    Test for get_mac_facts method of class DarwinHardware.
    """
    hardware_obj = DarwinHardware()

    result = hardware_obj.get_mac_facts()
    assert 'osversion' in result
    assert 'osrevision' in result



# Generated at 2022-06-13 00:38:19.479667
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    import sys

    # Import the common_utils module
    from ansible.module_utils.facts.hardware.common import Memory
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware

    # Set the desired attributes
    memory_size = "64G"
    pages = {
        'Pages wired down':  1048576,   # 1024M
        'Pages active':      2097152,   # 2048M
        'Pages inactive':    3145728,   # 3072M
    }
    expected_obj = Memory(memory_size, pages)

    # Create a DarwinHardware object
    obj = DarwinHardware()

    # Call the get_memory_facts method and get the resulting memory_facts
    memory_facts = obj.get_memory_facts()

    # Compare memory_facts with expected values

# Generated at 2022-06-13 00:38:31.104677
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    dh = DarwinHardware(None)
    dh.sysctl = {
        'machdep.cpu.brand_string': 'Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz',
        'machdep.cpu.core_count': '4',
        'hw.physicalcpu': '8',
        'hw.logicalcpu': '16',
        }

    cpu_facts = dh.get_cpu_facts()
    assert cpu_facts['processor'] == 'Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz'
    assert cpu_facts['processor_cores'] == '4'
    assert cpu_facts['processor_vcpus'] == '16'


# Generated at 2022-06-13 00:38:41.759891
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    test_module = AnsibleModule(argument_spec={})
    test_class = DarwinHardware(module=test_module)


# Generated at 2022-06-13 00:38:53.294010
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():

    class MockModule(object):

        def __init__(self):
            self.run_command_called = False
            self.run_command_result = (0, '', '')

        def run_command(self, args, encoding=None):
            self.run_command_called = True
            return self.run_command_result

        def get_bin_path(self, arg):
            return '/bin/vm_stat'

    class TestDarwinHardware(DarwinHardware):

        def __init__(self, module):
            self.module = module

        def get_system_profile(self):
            return dict()

        def get_mac_facts(self):
            return dict()

        def get_cpu_facts(self):
            return dict()

        def get_uptime_facts(self):
            return dict()



# Generated at 2022-06-13 00:39:00.233376
# Unit test for method get_memory_facts of class DarwinHardware

# Generated at 2022-06-13 00:39:02.938072
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    darwinhw = DarwinHardwareCollector()
    assert darwinhw._platform == "Darwin"

    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    assert darwinhw._fact_class == DarwinHardware


# Generated at 2022-06-13 00:39:15.328348
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    module = MockAnsibleModule()
    # Test on positive case. We simulate a boot time of 500 seconds.
    module.run_command.return_value = (0, struct.pack('@L', int(time.time() - 500)), '')
    hardware = DarwinHardware(module, 'test_DarwinHardware_get_uptime_facts')
    uptime_facts = hardware.get_uptime_facts()
    assert uptime_facts == {
        'uptime_seconds': 500
    }
    assert module.run_command.call_count == 1
    # Test on bad data case. We simulate an empty output.
    module.run_command.return_value = (0, '', '')
    uptime_facts = hardware.get_uptime_facts()
    assert uptime_facts == {}
    assert module.run_

# Generated at 2022-06-13 00:39:19.399799
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    module = AnsibleModule(argument_spec={})
    obj = DarwinHardware(module)
    facts = obj.populate()
    assert facts['osversion'] == '160200'
    assert facts['osrevision'] == '14'
    assert facts['model'] == 'MacPro2,1'


# Generated at 2022-06-13 00:40:04.675917
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    import mock
    mod = mock.Mock()
    har = DarwinHardware(mod)

    data = {'kern.boottime': '1589691254'}
    with mock.patch('ansible.module_utils.facts.hardware.darwin.DarwinHardware.get_sysctl', return_value=data) as sysctl:
        har.get_uptime_facts()
    mod.run_command.assert_called_with(['/usr/sbin/sysctl', '-b', 'kern.boottime'])
    sysctl.assert_called_with(mod, ['kern.boottime'])

# Generated at 2022-06-13 00:40:07.395614
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=False
    )

    hardware_obj = DarwinHardware(module)
    hardware_obj.populate()

# Generated at 2022-06-13 00:40:16.036436
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    def sysctl_darwin_boottime(module, option):
        class boottime:
            def pack(self, arg):
                return b'\x00\x00\x00\x00\x00\x00\x00\x00'

        return boottime()

    from ansible.module_utils.facts.hardware.darwin import DarwinHardware

    module = FakeModule()
    module.run_command = make_mock_command()
    module.get_bin_path = make_mock_get_bin_path()
    module.sysctl = sysctl_darwin_boottime

    h = DarwinHardware(module)

    uptime_facts = h.get_uptime_facts()
    assert uptime_facts['uptime_seconds'] > 0



# Generated at 2022-06-13 00:40:26.858058
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    import sys
    module = sys.modules['unit.modules.test_darwin']

    # Create a mock class for running commands
    class Bunch(object):
        def __init__(self):
            self.rc = 0
            self.stdout = None
            self.stderr = None

    # Create a mock class for module
    class AnsibleModule(object):
        def __init__(self):
            self.run_command = Bunch()

        def get_bin_path(self, *args, **kwargs):
            return '/sbin/sysctl'

    # Fake the module class
    sys.modules['ansible.module_utils.facts.hardware.darwin'] = module
    module.AnsibleModule = AnsibleModule
    module.Hardware = DarwinHardware

    # Fake the boottime.
    boottime

# Generated at 2022-06-13 00:40:31.937820
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    os_output = """Hardware Overview:
      Model Name: MacBook Pro
      Model Identifier: MacBookPro11,2
      Processor Name: Intel Core i7
      Processor Speed: 2 GHz
      Number of Processors: 1
      Total Number of Cores: 4
      L2 Cache (per Core): 256 KB
      L3 Cache: 6 MB
      Memory: 16 GB
      Boot ROM Version: MBP112.0138.B07
      SMC Version (system): 2.18f15
      Serial Number (system): C02SV1S0DVF7
      Hardware UUID: 00000000-0000-1000-8000-A39B50C06E35
"""
    mac_facts = DarwinHardware()
    mac_facts.module = MockModule()

# Generated at 2022-06-13 00:40:37.935662
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    module = AnsibleModule(argument_spec={})
    hardware = DarwinHardware(module)
    result = hardware.populate()

    assert 'model' in result
    assert 'osversion' in result
    assert 'osrevision' in result
    assert 'processor_cores' in result
    assert 'processor_vcpus' in result
    assert 'memtotal_mb' in result
    assert 'memfree_mb' in result

# Generated at 2022-06-13 00:40:46.879630
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    """Ensure that the uptime_seconds fact is calculated correctly"""

    class FakeModule(object):
        def get_bin_path(self, name):
            return name

        def run_command(self, cmd, encoding=None):
            return 0, b'{ sec = 1530544962, usec = 268861 }', None

    fake_module = FakeModule()
    expected_uptime_seconds = int(time.time()) - 1530544962
    uptime_facts = DarwinHardware(fake_module).get_uptime_facts()

    assert uptime_facts['uptime_seconds'] == expected_uptime_seconds

# Generated at 2022-06-13 00:40:49.329631
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    darwin_hw_collector = DarwinHardwareCollector()
    assert DarwinHardwareCollector
    assert darwin_hw_collector is not None


# Generated at 2022-06-13 00:40:57.918266
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    import pytest
    from mock import patch, MagicMock

    module = MagicMock()

    sysclt_cmd = MagicMock()
    sysclt_cmd.return_value = "/usr/sbin/sysctl"
    module.get_bin_path = sysclt_cmd

    uptime_seconds = 1595704817 - 1595704786  # python time.time()
    with patch.object(DarwinHardware, 'run_command') as run_cmd:
        run_cmd.return_value = (0, struct.pack('@L', 1595704786), '')

        dh = DarwinHardware()

        # Define get_bin_path function in module
        dh.module = module

        # Run the method to test
        ret = dh.get_uptime_facts()

        # Verify

# Generated at 2022-06-13 00:41:01.030365
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    module = FakeAnsibleModule({'sysctl': {'hw.model': 'hw.model: MacBookAir5,2'}})
    hardware = DarwinHardware(module)
    ansible_facts = hardware.get_mac_facts()
    assert ansible_facts['model'] == 'MacBookAir5,2'


# Generated at 2022-06-13 00:42:20.042017
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    darwinHardwareCollector = DarwinHardwareCollector()
    assert darwinHardwareCollector.platform == 'Darwin'
    assert darwinHardwareCollector._platform == 'Darwin'
    assert darwinHardwareCollector.fact_class == DarwinHardware
    assert darwinHardwareCollector._fact_class == DarwinHardware

# Generated at 2022-06-13 00:42:27.834354
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    from ansible.module_utils.facts import fact_cache
    from ansible.module_utils.facts.system.distribution import Distribution
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.virtual import Virtual

    from ansible.module_utils.facts.hardware.darwin import DarwinHardware

    from ansible.module_utils.facts.hardware.base import Hardware

    from ansible.module_utils.facts.hardware.darwin import DarwinHardwareCollector

    class Args:
        def __init__(self, module):
            self.module = module

    class TestModule:
        def __init__(self):
            self.run_command_environ_update = dict()
            self.run_command_rc = None
            self.run_command_out = None


# Generated at 2022-06-13 00:42:34.513140
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    class MockModule(object):
        def __init__(self, dict):
            self.params = dict
            self.exit_json = exit_json


# Generated at 2022-06-13 00:42:44.983926
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    from collections import namedtuple
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware

    module = namedtuple('module', ['run_command'])

    # Run command returns a tuple of three elements
    #   1. Command's return code
    #   2. Standard output (as a string)
    #   3. Standard error (as a string)
    run_command_return_value = (0, u'hw.model: MacPro4,1', '')

    # '__exit__' should be called with a tuple containing the following parameters:
    #   - type: (Exception class)
    #   - value: (Exception's value)
    #   - traceback: (Traceback object)
    # This should be called exactly once, when '__enter__' returns
    exit_expected_call_param

# Generated at 2022-06-13 00:42:53.991040
# Unit test for method get_system_profile of class DarwinHardware

# Generated at 2022-06-13 00:42:55.452283
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    # Just create an instance to check that not error occurs.
    DarwinHardwareCollector()


# Generated at 2022-06-13 00:43:04.214999
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    # Create a DarwinHardware object
    darwin_hw = DarwinHardware(dict())

    # Test on an Intel processor
    darwin_hw.sysctl = {
        'machdep.cpu.brand_string': 'Intel(R) Core(TM) i7-3770 CPU @ 3.40GHz',
        'machdep.cpu.core_count': 4
    }

    cpu_facts = darwin_hw.get_cpu_facts()
    assert (cpu_facts['processor'] == 'Intel(R) Core(TM) i7-3770 CPU @ 3.40GHz')
    assert (cpu_facts['processor_cores'] == 4)
    assert (cpu_facts['processor_vcpus'] == '')

    # Test on a PowerPC processor

# Generated at 2022-06-13 00:43:11.601908
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():

    class MockModule:
        def __init__(self, vm_stat_command, vm_stat_command_output_lines):
            self._vm_stat_command = vm_stat_command
            self._vm_stat_command_output_lines = vm_stat_command_output_lines
            self.params = dict()

        def get_bin_path(self, name, required=False):
            if name == 'vm_stat':
                return self._vm_stat_command
            else:
                assert False

        def run_command(self, cmd, encoding=None):
            if cmd == self._vm_stat_command:
                out = '\n'.join(self._vm_stat_command_output_lines)
                return 0, out, ''
            else:
                assert False


# Generated at 2022-06-13 00:43:13.065461
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    hardware = DarwinHardware()
    sp = hardware.get_system_profile()
    assert(sp)
    assert('Serial Number' in sp)

# Generated at 2022-06-13 00:43:24.180668
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    import io
    import unittest
    import unittest.mock as mock

    from ansible.module_utils.common.process import get_bin_path

    mock_module = mock.MagicMock()
    mock_module.run_command.return_value = (0, io.StringIO("""Hardware Overview:

      Model Name: MacBook Pro
      Model Identifier: MacBookPro3,1
      Processor Name: Intel Core 2 Duo
      Processor Speed: 2 GHz
      Number of Processors: 1
      Total Number of Cores: 2
      L2 Cache: 4 MB
      Memory: 2 GB
      Bus Speed: 800 MHz
""").read(), '')
    mock_module.get_bin_path.side_effect = get_bin_path

    darwin_hardware = DarwinHardware(mock_module)
    res = d