

# Generated at 2022-06-13 00:34:57.783602
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    import time

    darwin_hardware = DarwinHardware(module=None)
    # get the uptime in seconds
    time_before_uptime_seconds = int(time.time())
    uptime_seconds_facts = darwin_hardware.get_uptime_facts()
    time_after_uptime_seconds = int(time.time())
    if uptime_seconds_facts is not None:
        # should be in the range [time_before_uptime_seconds, time_after_uptime_seconds]
        assert uptime_seconds_facts['uptime_seconds'] >= time_before_uptime_seconds
        assert uptime_seconds_facts['uptime_seconds'] <= time_after_uptime_seconds

# Generated at 2022-06-13 00:35:08.045495
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    from unittest import TestCase, skip


    class TestDarwinHardware(TestCase):
        def run_cmd_mock(self, command):
            return (0, "hw.model: Power Mac G5\n", "")

        def test_get_mac_facts(self):
            module = MockModule()
            hardware = DarwinHardware(module)
            mac_facts = hardware.populate()
            self.assertEqual(mac_facts['machdep']['cpu']['brand_string'], 'Power Mac G5')
            self.assertEqual(mac_facts['model'], 'Power Mac G5')
            self.assertEqual(mac_facts['product_name'], 'Power Mac G5')


# Generated at 2022-06-13 00:35:18.389296
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    """ Test the darwin hardware class logic """
    import json
    import os
    import sys
    import tempfile

    class MockAnsibleModule:
        def __init__(self):
            self.run_command_args = {}
            self.run_command_rcs = {}
            self.run_command_outs = {}
            self.run_command_errs = {}

        @staticmethod
        def _get_command(command):
            # We don't care about the actual command, but the first element needs
            # to be a binary
            if command[0] == 'sysctl':
                mock_sysctl = os.path.join(os.path.dirname(__file__), 'mock_sysctl')
                mock_sysctl = os.path.abspath(mock_sysctl)

# Generated at 2022-06-13 00:35:27.710093
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    from ansible.module_utils.six import BytesIO
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware

    # Create mock module
    test_module = AnsibleModule(argument_spec=dict())
    test_module.run_command = mock.Mock(return_value=(0, "hw.model: iMac7,1\n", ""))

    # Get the facts
    fact_class = DarwinHardware(test_module)
    facts = fact_class.get_mac_facts()

    assert 'model' in facts
    assert facts['model'] == "iMac7,1"

    assert 'osversion' in facts
    assert 'osrevision' in facts

# Generated at 2022-06-13 00:35:29.643776
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    hc = DarwinHardwareCollector()
    assert isinstance(hc, HardwareCollector)
    assert hc._fact_class == DarwinHardware
    assert hc._platform == 'Darwin'

# Generated at 2022-06-13 00:35:31.579733
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    test_class = DarwinHardware(dict())
    test_class.get_system_profile()

# Generated at 2022-06-13 00:35:41.142772
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    module = AnsibleModule(argument_spec={})
    # Provide empty sysctl.
    module.params['gather_subset'] = '!all'
    module.params['filter'] = '*'
    
    darwin_collector = DarwinHardwareCollector(module=module)
    darwin_hardware = darwin_collector.collect()
    assert darwin_hardware is not None
    assert darwin_hardware.model is not None
    assert darwin_hardware.uptime_seconds is not None
    assert darwin_hardware.processor is not None
    assert darwin_hardware.processor_cores is not None
    assert darwin_hardware.memtotal_mb is not None
    assert darwin_hardware.memfree_mb is not None

# Unit

# Generated at 2022-06-13 00:35:44.465793
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    # DarwinHardware.get_cpu_facts()
    module = AnsibleModule(argument_spec=dict())
    obj = DarwinHardware(module)
    processor = obj.get_cpu_facts()['processor']
    assert processor.startswith('Intel') or processor.startswith('Power')

# Generated at 2022-06-13 00:35:55.085205
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    module = FakeModule()
    d = DarwinHardware(module, 'Darwin')
    rc, out, err = module.run_command("sysctl hw.model")
    if rc != 0:
        module.fail_json(msg='Unexpected output from "sysctl hw.model"')
    expected_model = out.splitlines()[-1].split()[1]

    expected = dict(model=expected_model, osversion=d.sysctl['kern.osversion'], osrevision=d.sysctl['kern.osrevision'])
    assert d.get_mac_facts() == expected



# Generated at 2022-06-13 00:36:05.160165
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    module = DummyAnsibleModule()
    hardware_obj = DarwinHardware(module)
    # We mock the _get_system_profile() method to have a deterministic output.
    hardware_obj.get_system_profile = lambda: {
        'Processor Name': 'Intel Core 2 Duo',
        'Processor Speed': '2.66 GHz'
    }

# Generated at 2022-06-13 00:36:16.663240
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    assert issubclass(DarwinHardwareCollector, HardwareCollector)

# Generated at 2022-06-13 00:36:24.096641
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    m = ModuleStub()
    m.run_command.side_effect = [
        (0, u'hw.model: MacBookPro8,2', ''),
        (0, u'12.2.0', ''),
        (0, u'13C64', ''),
    ]
    h = DarwinHardware(m)
    facts = h.get_mac_facts()
    assert facts['model'] == 'MacBookPro8,2'
    assert facts['osversion'] == '12.2.0'
    assert facts['osrevision'] == '13C64'


# Generated at 2022-06-13 00:36:33.680922
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.hardware import darwin
    from ansible.module_utils.facts.hardware.base import Hardware
    basic._ANSIBLE_ARGS = to_bytes(basic._ANSIBLE_ARGS)

    hardware = darwin.DarwinHardware()

    # Just call the function without arguments to check that it runs without errors
    memory_facts = hardware.get_memory_facts()
    try:
        assert(isinstance(memory_facts['memfree_mb'], int))
        assert(isinstance(memory_facts['memtotal_mb'], int))
    except AssertionError as e:
        print('\nERROR: %s' % e)

# Generated at 2022-06-13 00:36:43.415522
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    module = AnsibleModule(argument_spec={})
    darwin_hw = DarwinHardware(module)
    facts = darwin_hw.populate()

    assert isinstance(facts, dict)
    assert 'uptime_seconds' in facts
    assert facts['uptime_seconds'] > 0

if __name__ == '__main__':
    from ansible.module_utils.basic import *
    from ansible.module_utils.facts import *

    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=['all'], type='list'),
        ),
        supports_check_mode=False,
        add_file_common_args=True,
    )
    darwin_hw = DarwinHardware(module)
    facts = darwin_hw.populate()


# Generated at 2022-06-13 00:36:55.619483
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )
    hardware = DarwinHardware(module)
    hardware.sysctl = dict()
    hardware.sysctl['machdep.cpu.brand_string'] = "Intel(R) Xeon(R) CPU E5-2690 v4 @ 2.60GHz"
    hardware.sysctl['machdep.cpu.core_count'] = 8
    cpu_facts = hardware.get_cpu_facts()
    assert cpu_facts == {
        "processor": "Intel(R) Xeon(R) CPU E5-2690 v4 @ 2.60GHz",
        "processor_cores": 8,
        "processor_vcpus": ""
    }


# Generated at 2022-06-13 00:37:00.342136
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    cpu_facts = DarwinHardware(module).get_cpu_facts()

    module.exit_json(ansible_facts=cpu_facts)


# Generated at 2022-06-13 00:37:06.099134
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils.facts.hardware import DarwinHardware

    mock_module = FactCollector().get_module()
    uptime_facts = DarwinHardware(mock_module).get_uptime_facts()
    assert uptime_facts



# Generated at 2022-06-13 00:37:14.330693
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    print("MAC OS X 10.4 and 10.5")
    darwin_hardware = DarwinHardware()
    darwin_hardware.sysctl =  {'kern.boottime': '{ sec = 1510992361, usec = 712164 } Fri Nov 24 07:06:01 2017'}
    uptime_facts = darwin_hardware.get_uptime_facts()
    assert uptime_facts['uptime_seconds'] == 1510992361

    print("MAC OS X 10.6 and later")
    darwin_hardware = DarwinHardware()
    darwin_hardware.sysctl =  {'kern.boottime': '{ sec = 1510992361, usec = 712164 }'}
    uptime_facts = darwin_hardware.get_uptime_

# Generated at 2022-06-13 00:37:22.755379
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    from ansible.module_utils import basic
    from ansible.module_utils.facts import collector

    # Create a basic AnsibleModule, assign it to a variable
    module = basic.AnsibleModule(argument_spec={})
    module.get_bin_path = lambda prog: '/usr/bin/' + prog

    # Create a collector, assign it to a variable
    fact_collector = collector.get_collector(module)

    # Get the DarwinHardware instance for the fact collector
    darwin_hardware_instance = fact_collector.get_hardware_instance()

    # The following is the output of the command '/usr/bin/vm_stat' on MacOS

# Generated at 2022-06-13 00:37:32.292225
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    # Mock module to return a pre-defined output
    _sysctl = {'machdep.cpu.brand_string': 'Intel(R) Core(TM) i5-4260U CPU @ 1.40GHz'}
    module = MagicMock()
    module.run_command.return_value = (0, '', '')
    Hardware._get_sysctl = MagicMock(return_value=_sysctl)
    facts_collector = DarwinHardware(module)

    cpu_facts = facts_collector.get_cpu_facts()
    assert cpu_facts['processor'] == 'Intel(R) Core(TM) i5-4260U CPU @ 1.40GHz'
    assert cpu_facts['processor_cores'] == 1

# Generated at 2022-06-13 00:37:57.568309
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    module = AnsibleModuleStub()
    hw = DarwinHardware(module)
    expected_result = {
        'model': 'MacBookPro12,1',
        'osversion': '15.6.0',
        'osrevision': '20200',
    }
    assert hw.get_mac_facts() == expected_result



# Generated at 2022-06-13 00:38:05.359405
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    module = AnsibleModuleMock()
    hardware = DarwinHardware(module)
    hardware_facts = hardware.populate()
    assert hardware_facts['memtotal_mb'] == hardware_facts['memtotal_mb']
    assert hardware_facts['memfree_mb'] == hardware_facts['memfree_mb']
    assert hardware_facts['osversion'] == hardware_facts['osversion']
    assert hardware_facts['osrevision'] == hardware_facts['osrevision']
    assert hardware_facts['uptime_seconds'] == hardware_facts['uptime_seconds']

# Generated at 2022-06-13 00:38:14.719303
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    import sys

    import ansible.module_utils.facts.hardware.darwin as test_module

    if sys.version_info.major < 3:
        import __builtin__ as builtins  # pylint: disable=no-name-in-module,import-error
    else:
        import builtins  # pylint: disable=no-name-in-module,import-error

    # Replace the run_command method with one that returns the system_profiler
    # SPHardwareDataType output for the macbook air.

# Generated at 2022-06-13 00:38:26.866641
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    hostname_command = '/bin/hostname'
    module = AnsibleModule(
            argument_spec=dict(),
            supports_check_mode=True
    )
    os_obj = DarwinHardware(module)
    os_obj.sysctl = dict()
    os_obj.sysctl['hw.logicalcpu'] = 1
    os_obj.sysctl['hw.physicalcpu'] = 1
    os_obj.sysctl['machdep.cpu.core_count'] = 1
    os_obj.sysctl['machdep.cpu.brand_string'] = 'Darwin'
    module.run_command = MagicMock(return_value=(0, '', ''))
    cpu_facts = os_obj.get_cpu_facts()
    assert cpu_facts['processor_vcpus'] == '1'
    assert cpu

# Generated at 2022-06-13 00:38:38.724383
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode=True
    )

    # These are the static methods that are called in order
    # Therefore mock them out in the right order

# Generated at 2022-06-13 00:38:41.635191
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    collector = DarwinHardwareCollector()
    assert collector.get_platform() == 'Darwin'
    assert collector.get_fact_class() == DarwinHardware


# Generated at 2022-06-13 00:38:48.959433
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    # Test empty sysctl output
    test_DarwinHardware = DarwinHardware(None)
    test_DarwinHardware.sysctl = {}
    assert test_DarwinHardware.get_uptime_facts() == {}

    # Test with a fixed sysctl output
    test_DarwinHardware.sysctl = {'kern.boottime': '0', 'kern.version': '13.4.0'}
    assert test_DarwinHardware.get_uptime_facts() == {'uptime_seconds': 0}

    # Normal test case
    test_DarwinHardware.sysctl = {'kern.boottime': '1500000000'}
    assert test_DarwinHardware.get_uptime_facts() == {'uptime_seconds': int(time.time() - 150)}

# Generated at 2022-06-13 00:38:59.605168
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    module = FakeAnsibleModule()
    hardware_facts = DarwinHardware(module)

    # Create a fake vm_stat output
    vm_stat_output = ''
    vm_stat_output += 'Mach Virtual Memory Statistics: (page size of 4096 bytes)\n'
    vm_stat_output += 'Pages free:                              251204.\n'
    vm_stat_output += 'Pages active:                            127101.\n'
    vm_stat_output += 'Pages inactive:                          122748.\n'
    vm_stat_output += 'Pages wired down:                        565376.\n'
    vm_stat_output += 'Pages purgeable:                            2.\n'
    vm_stat_output += '"Translation faults":                14271485.\n'

# Generated at 2022-06-13 00:39:04.083157
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    # Construct a fake module that run_command can use
    module = type('FakeModule', (object,), {
        'run_command': lambda self, command: (0, "hw.model: MacBookPro12,1\n", ''),
        'get_bin_path': lambda self, command: command,
    })
    hardware = DarwinHardware(module)
    mac_facts = hardware.get_mac_facts()
    assert mac_facts['model'] == 'MacBookPro12,1'


# Generated at 2022-06-13 00:39:16.109220
# Unit test for method get_memory_facts of class DarwinHardware

# Generated at 2022-06-13 00:39:43.836850
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    Hardware._module = None
    d = DarwinHardware()
    system_profile = { 'Model Name': 'MacBook Pro' }
    d.get_system_profile = lambda: system_profile
    d.sysctl = {}
    d.sysctl['kern.osversion'] = "15.6.0"
    d.sysctl['kern.osrevision'] = "201710"
    d.sysctl['hw.model'] = "MacBookPro13,2"
    mac_facts = d.get_mac_facts()
    assert mac_facts['model'] == 'MacBookPro13,2'


# Generated at 2022-06-13 00:39:47.543234
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    from ansible.module_utils.facts.hardware.mac import mac_data
    from ansible.module_utils.facts.hardware.base import Hardware
    from ansible.module_utils.facts.sysctl import get_sysctl
    
    hw = Hardware()
    hw.module = get_sysctl(hw.module, ['hw', 'machdep', 'kern'])

    model = DarwinHardware.get_mac_facts(hw)['model']
    assert(model == mac_data()['model'])


# Generated at 2022-06-13 00:39:53.894703
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    module = AnsibleModule(argument_spec=dict())
    hardware = DarwinHardware(module)
    hardware_facts = hardware.populate()
    assert hardware_facts['osversion']
    assert hardware_facts['osrevision']
    assert hardware_facts['model']
    assert hardware_facts['processor']
    assert hardware_facts['processor_cores']
    assert hardware_facts['memtotal_mb']
    assert hardware_facts['memfree_mb']
    assert hardware_facts['uptime_seconds']

# Generated at 2022-06-13 00:39:59.711611
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    import io
    import sys

    # Monkey patch stdin and stdout to avoid crashing the unittest suite
    # when importing module_utils.facts.hardware.darwin
    sys.stdin = io.StringIO('\n')
    sys.stdout = io.StringIO()
    dh = DarwinHardware(None)
    assert dh.get_system_profile() == {}

# Generated at 2022-06-13 00:40:06.920779
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    mac_facts = DarwinHardware.get_cpu_facts({'mac_facts': {'product_name': 'MacBookPro'}})
    assert mac_facts['processor_cores'] > 0
    assert mac_facts['processor'] != ''
    assert mac_facts['processor_vcpus'] >= mac_facts['processor_cores']

    mac_facts = DarwinHardware.get_cpu_facts({'mac_facts': {'product_name': 'MacPro'}})
    assert mac_facts['processor_cores'] > 0
    assert mac_facts['processor'] != ''
    assert mac_facts['processor_vcpus'] >= mac_facts['processor_cores']



# Generated at 2022-06-13 00:40:15.889930
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    module_args = dict()
    module = FakeModule(module_args=module_args)
    dh = DarwinHardware(module=module)

    # Test the facts
    facts = dh.populate()
    assert facts['osversion'] == '15.6.0'
    assert facts['osrevision'] == '15G1212'
    assert facts['processor'] == 'Intel(R) Core(TM) i7-4650U CPU @ 1.70GHz'
    assert facts['processor_cores'] == '2'
    assert facts['processor_vcpus'] == '4'
    assert facts['product_name'] == 'MacBookAir6,2'
    assert facts['memtotal_mb'] == '4096'
    assert facts['memfree_mb'] == '3188'
    assert facts['uptime_seconds'] == 10

# Generated at 2022-06-13 00:40:18.465381
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    hardware = DarwinHardware()
    system_profile = hardware.get_system_profile()
    assert system_profile != {}

# Generated at 2022-06-13 00:40:22.025778
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    darwin_hardware_collector = DarwinHardwareCollector()
    assert darwin_hardware_collector._platform == 'Darwin'

# Generated at 2022-06-13 00:40:30.921553
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    os_version = '16.2.0'
    brief_sample = '''
Hardware:

    Hardware Overview:

      Model Name: Mac Pro
      Model Identifier: MacPro5,1
      Processor Name: Quad-Core Intel Xeon
      Processor Speed: 3.2 GHz
      Number of Processors: 1
      Total Number of Cores: 4
      L2 Cache (per Core): 256 KB
      L3 Cache: 8 MB
      Memory: 16 GB
      Boot ROM Version: MP51.007F.B03
      SMC Version (system): 1.39f9
    '''

# Generated at 2022-06-13 00:40:42.361860
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    import unittest
    import mock

    class FakeModule(object):
        def __init__(self):
            self.params = {}
        def get_bin_path(self, name):
            return name

    def run_command(args, encoding=None):
        return 0, FAKESYSCTL_UPTIME, ''

    FAKESYSCTL_UPTIME = ''
    for i in range(4):
        FAKESYSCTL_UPTIME += struct.pack('@L', i ** 2)

    module = FakeModule()
    module.run_command = run_command

    hardware = DarwinHardware(module)
    facts = hardware.populate()
    assert facts['uptime_seconds'] == 30


if __name__ == '__main__':
    unittest.main()

# Generated at 2022-06-13 00:41:34.781369
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    fake_module = FakeModule({})
    my_DarwinHardware = DarwinHardware(module=fake_module)
    system_profile = my_DarwinHardware.get_system_profile()
    assert (system_profile['Serial Number (system)'] == 'C02XXXXXXJMG')
    assert (system_profile['Number of Processors'] == '1')
    assert (system_profile['Memory'] == '8 GB')
    assert (system_profile['Boot ROM Version'] == 'MMB0216.0138.B00')
    assert (system_profile['SMC Version (system)'] == '2.23f24')

# Generated at 2022-06-13 00:41:41.491736
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    class FakeModule(object):
        def run_command(self, command):
            return 0, '\n'.join(['Machinetype: x86_64', 'Model: iMac14,2', 'CPU Type: Intel Core i7', 'CPU Speed: 3,5 GHz']), ''

    fake_module = FakeModule()
    hardware_module = DarwinHardware(fake_module)
    system_profile = hardware_module.get_system_profile()

    assert len(system_profile) == 3
    assert system_profile['Model'] == 'iMac14,2'
    assert system_profile['CPU Type'] == 'Intel Core i7'
    assert system_profile['CPU Speed'] == '3,5 GHz'

# Generated at 2022-06-13 00:41:43.711366
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    test_out = 'hw.model: MacBookPro12,1'
    mac_facts = DarwinHardware().get_mac_facts()

    assert mac_facts['model'] == 'MacBookPro12,1'


# Generated at 2022-06-13 00:41:45.996334
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    # Create a class object of class DarwinHardwareCollector
    mac_obj = DarwinHardwareCollector()
    assert True

# Generated at 2022-06-13 00:41:56.036374
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    """
    Test function populate of class DarwinHardware
    """
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    from ansible.module_utils.facts.collector.system import SystemCollector
    from ansible.module_utils.facts.collector import gather_subset_information
    import sys
    import os
    import subprocess

    class MockDarwinHardwareModule:
        """
        Mock class for ansible.module_utils.basic.AnsibleModule
        used in the function 'populate' of class DarwinHardware
        """
        def __init__(self):
            self.params = {}

        def fail_json(self, *args, **kwargs):
            pass

        def run_command(self, args, **kwargs):
            cmd = args.split(' ')

# Generated at 2022-06-13 00:41:58.087860
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    HAR = DarwinHardwareCollector()
    assert HAR._platform == 'Darwin'
    assert HAR._fact_class == DarwinHardware
    

# Generated at 2022-06-13 00:42:04.873798
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    m = DarwinHardware()

# Generated at 2022-06-13 00:42:06.423083
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    """Test DarwinHardwareCollector initializer."""
    collector = DarwinHardwareCollector()
    assert collector.platform == 'Darwin'
    assert collector._fact_class == DarwinHardware

# Generated at 2022-06-13 00:42:16.007185
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    test_data = """
Hardware:

    Hardware Overview:

      Model Name: MacBook Pro
      Model Identifier: MacBookPro11,2
      Processor Name: Intel Core i7
      Processor Speed: 2,8 GHz
      Number of Processors: 1
      Total Number of Cores: 2
      L2 Cache (per Core): 256 KB
      L3 Cache: 6 MB
      Memory: 16 GB
      Boot ROM Version: MBP112.0138.B16
      SMC Version (system): 2.18f15
      Serial Number (system): C02PS3SFG3Q5
      Hardware UUID: 00000000-0000-1000-8000-0012C02PS3SF

"""
    m = DarwinHardware(dict(module=None))

# Generated at 2022-06-13 00:42:19.693026
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    f = DarwinHardware()
    cmd = f.module.run_command
    rc, out, err = cmd.call_args[0]
    assert rc == 0
    assert out == b'\x00\x00\x00\x00\x00\x00\x00\x00'

# Generated at 2022-06-13 00:44:04.203299
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    import os

    class TestModule(object):
        def __init__(self):
            self.run_command_results = []
            self.run_command_calls = []

        def get_bin_path(self, name):
            if name == 'system_profiler':
                return '/usr/sbin/system_profiler'
            else:
                raise ValueError


        def run_command(self, args):
            self.run_command_calls.append(args)
            return self.run_command_results.pop(0)


    class TestSysctl(dict):
        def __init__(self, values_dict):
            dict.__init__(self)
            self.update(values_dict)


# Generated at 2022-06-13 00:44:10.541228
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():

    import time

    class Msg:
        def __init__(self):
            self.stdout_lines = ["{0}".format(int(time.time()))]

    class FakeModule:
        def run_command(self, command, encoding):
            return 0, Msg(), ''

        def get_bin_path(self, command):
            return ''

    d = DarwinHardware()
    d.module = FakeModule()
    uptime_facts = d.get_uptime_facts()
    assert uptime_facts['uptime_seconds'] == 0
    assert 'uptime_days' not in uptime_facts

# Generated at 2022-06-13 00:44:14.234182
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    cpu_facts = DarwinHardware(None, None).get_cpu_facts()
    assert isinstance(cpu_facts, dict)
    assert isinstance(cpu_facts['processor'], str)
    assert isinstance(cpu_facts['processor_cores'], int)
    assert isinstance(cpu_facts['processor_vcpus'], str)


# Generated at 2022-06-13 00:44:19.761936
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():

    hardware = DarwinHardware()

    hardware.sysctl = {
        'machdep.cpu.core_count': 4,
        'hw.memsize': 8589934592,
        'hw.ncpu': 4,
        'hw.physicalcpu': 4,
        'hw.logicalcpu': 4,
        'machdep.cpu.brand_string': 'Intel(R) Core(TM) i7-5820K CPU @ 3.30GHz',
        'hw.model': 'Macmini7,1',
        'kern.osversion': '19D76',
        'kern.osrevision': '15.6.0',
    }

# Generated at 2022-06-13 00:44:29.259812
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    module = AnsibleModule(argument_spec={})
    hardware_collector = DarwinHardwareCollector(module=module)
    hardware_collector.populate()
    ansible_facts = hardware_collector.get_facts()

    assert ansible_facts['processor']
    assert ansible_facts['processor_cores']
    assert ansible_facts['memtotal_mb']
    assert ansible_facts['memfree_mb']
    assert ansible_facts['model']
    assert ansible_facts['osversion']
    assert ansible_facts['osrevision']
    assert ansible_facts['uptime_seconds']


from ansible.module_utils.basic import AnsibleModule
if __name__ == '__main__':
    # Unit test
    import pytest

# Generated at 2022-06-13 00:44:36.298365
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    class TestModule:
        def __init__(self, params):
            self.params = params
        def run_command(self, command, encoding=None):
            return 123, '', ''

    class FakeHardware(DarwinHardware):
        def __init__(self, module):
            self.module = module

        def get_bin_path(self, binary):
            return binary

    class TestFacts:
        def __init__(self, params, module_name):
            pass
        def populate(self):
            return {}

    TestFacts.__name__ = "ansible.module_utils.facts.hardware.TestFacts"
    facts = TestFacts(dict(), "test")
    module = TestModule([])
    hardware = FakeHardware(module)
    hardware.machdep_dict = {}