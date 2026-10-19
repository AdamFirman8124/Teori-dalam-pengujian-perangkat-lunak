

# Generated at 2022-06-13 00:34:57.260528
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    fake_module = type('FakeModule', (object,), {})
    fake_module.run_command = lambda x: (0, '', '')
    processor = DarwinHardware(fake_module)
    processor.sysctl = get_sysctl(fake_module, ['hw', 'machdep', 'kern'])
    memory_facts = processor.get_memory_facts()
    assert memory_facts['memtotal_mb'] != 0
    assert memory_facts['memfree_mb'] != 0

# Generated at 2022-06-13 00:34:59.170017
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    DarwinHardware().populate()

# Generated at 2022-06-13 00:35:04.776154
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec={})
    hardware_collector = DarwinHardwareCollector(module=module)
    hardware = hardware_collector.collect()[0]
    cpu_facts = hardware.get_cpu_facts()
    assert cpu_facts['processor']
    assert cpu_facts['processor_cores']
    assert cpu_facts['processor_vcpus']


# Generated at 2022-06-13 00:35:16.069652
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    m = DarwinHardware()
    system_profile = m.get_system_profile()
    assert system_profile['Model Identifier'] == 'iMac9,1'
    assert system_profile['Processor Name'] == 'Intel Core 2 Duo'
    assert system_profile['Processor Speed'] == '3.06 GHz'
    assert system_profile['Number of Processors'] == '1'
    assert system_profile['Total Number of Cores'] == '2'
    assert system_profile['L2 Cache'] == '6 MB'
    assert system_profile['Memory'] == '4 GB'
    assert system_profile['Bus Speed'] == '1.07 GHz'
    assert system_profile['Boot ROM Version'] == 'IM91.008D.B08'
    assert system_profile['Serial Number'] == 'WW202KN2H2Y'
   

# Generated at 2022-06-13 00:35:26.463524
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    import os
    os.environ['ANSIBLE_UNIT_TEST'] = 'True'
    module = FakeAnsibleModule()
    darwin_hardware_obj = DarwinHardware(module)

    vm_stat_command = get_bin_path('vm_stat')

    os.environ['ANSIBLE_UNIT_TEST_WITHOUT_VM_STAT'] = 'True'
    assert darwin_hardware_obj.get_memory_facts() == {'memtotal_mb': 0, 'memfree_mb': 0}

    os.environ['ANSIBLE_UNIT_TEST_WITHOUT_VM_STAT'] = 'False'
    darwin_hardware_obj.module.run_command = FakeRunCommand

# Generated at 2022-06-13 00:35:32.858862
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():

    class FakeModule():
        def __init__(self):
            self.run_command = lambda x: (0, 'Model: MacBookAir6,2', '')

    fake_module = FakeModule()
    darwin_hw = DarwinHardware(fake_module)
    darwin_hw.sysctl = {'kern.osversion': '15A284', 'kern.osrevision': '14I291'}

    assert darwin_hw.get_mac_facts() == {'model': 'MacBookAir6,2', 'osversion': '15A284', 'osrevision': '14I291'}



# Generated at 2022-06-13 00:35:42.192236
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    def exec_module(module):
        return module.run_command(["/usr/bin/uname", "-m"])[1].rstrip('\r\n')

    def run(module):
        module.get_bin_path = get_bin_path
        module.run_command = run_command
        module.params = {}

        return DarwinHardware(module).populate()['processor']


# Generated at 2022-06-13 00:35:47.216113
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    import platform
    import pytest
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat import unittest
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.facts.hardware.darwin import DarwinHardware
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.facts.facts import Facts


# Generated at 2022-06-13 00:35:51.773293
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    out = """
      Hardware:

      Hardware Overview:

        Model Name: MacBook Pro
        Model Identifier: MacBookPro11,1
        Processor Name: Intel Core i7
        Processor Speed: 2.2 GHz
        Number of Processors: 1
        Total Number of Cores: 4
        L2 Cache (per Core): 256 KB
        L3 Cache: 6 MB
        Memory: 16 GB
        Boot ROM Version: MBP111.0138.B16
        SMC Version (system): 2.18f15
    """

    mac = DarwinHardware(dict())
    mac.module = DummyModule()
    mac.module.run_command = lambda x: (0, out, '')

# Generated at 2022-06-13 00:35:58.245002
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    fake_module = {
        'run_command': lambda x, encoding=None, errors=None: ('', '', 1)
    }
    hw_collector = DarwinHardwareCollector(fake_module)
    assert hw_collector._platform == 'Darwin'
    assert hw_collector.sysctl is None
    assert hw_collector._fact_class is not None
    assert hw_collector._fact_class.platform == 'Darwin'

# Generated at 2022-06-13 00:36:18.555974
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    import os
    import shutil
    import tempfile

    fake_stdout_filepath = os.path.join(tempfile.gettempdir(), 'fake_stdout')
    fake_stderr_filepath = os.path.join(tempfile.gettempdir(), 'fake_stderr')

    # Create fake stdout and stderr files

# Generated at 2022-06-13 00:36:19.759344
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    assert issubclass(DarwinHardwareCollector, HardwareCollector)


# Generated at 2022-06-13 00:36:23.873208
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    hardware_object = DarwinHardware()

    hardware_object.module = MockModule()
    hardware_object.module.run_command.return_value = (0, '', '')

    hardware_object.populate({})

    assert hardware_object.facts['uptime_seconds'] == 64


# Generated at 2022-06-13 00:36:33.418593
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    module = AnsibleModule
    module.run_command = MagicMock(return_value=(0, '1', ''))
    darwin_obj = DarwinHardware()
    darwin_obj.populate()
    assert darwin_obj.sysctl['kern.osversion'] == '19.2.0'


if __name__ == '__main__':
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware as HardwareCollector
    from ansible.module_utils.six.moves import mock
    import pytest


# Generated at 2022-06-13 00:36:39.080439
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    module = AnsibleModule(argument_spec={})
    hardware = DarwinHardware(module)
    # Test the stubbed out data
    memory_facts = hardware.get_memory_facts()
    assert memory_facts['memtotal_mb'] == 10240
    assert memory_facts['memfree_mb'] == 0

# Generated at 2022-06-13 00:36:51.336163
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware

    class ModuleStub:
        def run_command(self, cmd, encoding=None):
            # date +%s -r /var/db/systemstats/kernel.db
            # This should return a timestamp in the past, relative to the
            # current time.
            seconds = int(time.time() - 86400)
            # Now generate the bytes that `sysctl -b` would return.
            # This includes the seconds and a microseconds field, but we
            # don't care about the first.
            # (1, 2) is an array of one element to generate a tuple of length
            # two
            return 0, struct.pack('@Ld', seconds, *(1, 2)), ''


# Generated at 2022-06-13 00:37:00.312390
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    import ansible.module_utils.facts.hardware.darwin as darwin
    import ansible.module_utils.facts.utils

    # test_output is the output of the command: system_profiler SPHardwareDataType

# Generated at 2022-06-13 00:37:11.121165
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    from ansible.module_utils._text import to_bytes

    def run_command_mock(self, cmd, encoding=None):
        if cmd == [sysctl_cmd, '-b', 'kern.boottime']:
            return 0, to_bytes('1516638278 613273000'), ''
        return 0, '', ''

    # Create and initialize mock module
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    import ansible.module_utils.facts.hardware.darwin
    import ansible.module_utils.facts.rpc
    import ansible.module_utils.facts.service

    sysctl_cmd = '/usr/sbin/sysctl'
    # Setup mocking in DarwinHardware
    ansible.module_utils.facts.hardware.darwin.get_bin_

# Generated at 2022-06-13 00:37:20.478552
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    class TestModule(object):
        def __init__(self):
            self.run_command = self.fake_run_command
            self.exit_json = self.fake_exit_json
            self.fail_json = self.fake_fail_json
            self.warn = self.fake_warn
            self.exit_json = self.fake_exit_json

        def fake_run_command(self, cmd_list):
            stdout = 'hw.model: x86_64\n'
            return 0, stdout, ''

        def fake_exit_json(self, **kwargs):
            sys.exit(0)

        def fake_fail_json(self, **kwargs):
            sys.exit(1)

        def fake_warn(self, **kwargs):
            pass


# Generated at 2022-06-13 00:37:29.014215
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    from ansible.module_utils.facts.facts import Facts
    from ansible.module_utils._text import to_bytes

    mac_facts = DarwinHardware(module=Facts().module).get_mac_facts()
    assert 'model' in mac_facts
    assert 'osversion' in mac_facts
    assert 'osrevision' in mac_facts
    assert mac_facts['model'] == b'macbookair4,1'
    assert mac_facts['osversion'] == b'15.4.0'
    assert mac_facts['osrevision'] == b'15F34'

# Generated at 2022-06-13 00:37:57.203734
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    from ansible_collections.community.general.tests.unit.compat.mock import MagicMock

    m = MagicMock()

    # dict with multiple whitespaces in value,
    # and will be stripped by dict construction
    m.run_command = MagicMock(
        side_effect=[
            (0, '''Serial Number: C02S123456
                Hardware UUID: 0B4B4AB4-68BE-59A1-81F9-ABE0F9AF6789
                System Version: Version 13.1.0 (Build 17C205)
               ''', None)]
    )

    h = DarwinHardware(m)

    # test output
    result = h.get_system_profile()
    assert result['Serial Number'] == 'C02S123456'

# Generated at 2022-06-13 00:38:04.566182
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    module = AnsibleModule(argument_spec=dict())

    # Set up the mocked module and its parameters
    module.run_command = MagicMock(return_value=(0, 'hw.model: MacBookPro13,1\n', ''))

    facts_obj = DarwinHardware(module)

    expected = {'model': 'MacBookPro13,1',
                'osversion': '',
                'osrevision': ''}

    assert facts_obj.get_mac_facts() == expected



# Generated at 2022-06-13 00:38:08.891392
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    """
    This test validates the different scenarios
    """
    fakemodule = FakeModule()
    # Run 1:
    # - simulate that if the ssh call to vm_stat
    # - is executed successfully
    # - return a value
    fakemodule.run_command_rc = 0

# Generated at 2022-06-13 00:38:16.583803
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    import sys
    import tempfile

    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    from ansible.module_utils.facts.system.os import Darwin

    _, test_dir = tempfile.mkstemp()
    with open(test_dir, "w") as f:
        f.write("total: 4096\n")
        f.write("avail: 2048\n")
        f.write("used: 2048\n")
        f.write("free: 2048\n")

    memory_facts = DarwinHardware._get_memory_facts(Darwin({'sysctl': None, 'path': sys.path}), test_dir)
    print(memory_facts)

# Generated at 2022-06-13 00:38:23.406307
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    from ansible.module_utils.facts.hardware import DarwinHardwareCollector
    darwin_hw = DarwinHardwareCollector()
    assert hasattr(darwin_hw, '_fact_class')
    assert hasattr(darwin_hw, '_platform')
    assert darwin_hw._fact_class == DarwinHardware
    assert darwin_hw._platform == 'Darwin'



# Generated at 2022-06-13 00:38:29.884250
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    module = AnsibleModule(argument_spec={})
    hw = DarwinHardware(module=module)
    facts = hw.populate()

    assert 'osversion' in facts
    assert 'osrevision' in facts
    assert 'model' in facts
    assert 'uptime_seconds' in facts
    assert 'processor' in facts
    assert 'processor_vcpus' in facts
    assert 'processor_cores' in facts
    assert 'memtotal_mb' in facts
    assert 'memfree_mb' in facts

# Generated at 2022-06-13 00:38:41.130666
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():

    from ansible.module_utils.facts import Hardware
    from ansible.module_utils.facts.sysctl import get_sysctl
    from ansible.module_utils.facts.common.process import get_bin_path

    class OSModuleMock(object):
        def __init__(self):
            self.run_command_results = list()
            self.run_command_results.append((0, 'hw.model: x86_64\n', ''))
            self.run_command_results.append((0, 'hw.osversion: 16.7.0\n', ''))
            self.run_command_results.append((0, 'hw.osrevision: 1\n', ''))


# Generated at 2022-06-13 00:38:43.258728
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    module = MockAnsibleModule()
    hw = DarwinHardware(module)
    hw.populate()
    assert hw.platform == 'Darwin'

# Generated at 2022-06-13 00:38:44.411069
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    fc = DarwinHardwareCollector()
    assert fc.collect() is not None

# Generated at 2022-06-13 00:38:50.895591
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    # Construct a mock DarwinHardware object with arbitrary (fake) values.
    mock_hw = DarwinHardware()

    # Define arbitrary (fake) sysctl results.
    mock_sysctl_results = {
        'hw.memsize': '742415360',
        'hw.physicalcpu': '4',
        'hw.logicalcpu': '8',
        'hw.model': 'MacPro4,1',
        'kern.osrevision': '15',
        'kern.osversion': 'Darwin Kernel Version 15.5.0: Wed Apr 13 23:06:17 PDT 2016; root:xnu-3248.50.21~8/RELEASE_X86_64'
    }

    # Define arbitrary (fake) vm_stat results.

# Generated at 2022-06-13 00:39:31.348324
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    test_class = DarwinHardware()
    out = """
Mach Virtual Memory Statistics: (page size of 4096 bytes)
Pages free:                          996939.
Pages active:                        812554.
Pages inactive:                      542750.
Pages speculative:                   151181.
Pages throttled:                       8718.
Pages wired down:                    939332.
Pages purgeable:                          0.
"Translation faults":              49329966.
Pages copy-on-write:                9872753.
Pages zero filled:                 45342452.
Pages reactivated:                     8375.
Pageins:                           21342713.
Pageouts:                              549.
Object cache: 14 hits of 23717 lookups (0% hit rate)
"""
    setattr(test_class, 'get_uptime_facts', lambda: 'test')
   

# Generated at 2022-06-13 00:39:34.440488
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    cpu_facts = DarwinHardware(dict()).get_cpu_facts()
    assert 'processor' in cpu_facts
    assert 'processor_cores' in cpu_facts
    assert isinstance(cpu_facts['processor_cores'], int)

# Generated at 2022-06-13 00:39:42.725827
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    """
    Testing get_memory_facts method of class DarwinHardware.
    """
    real_class = DarwinHardware
    class MockDarwinModule(object):
        def __init__(self):
            self.params = dict()


# Generated at 2022-06-13 00:39:47.456763
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    """This test case checks the return value of get_mac_facts method
    """
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    from ansible.module_utils.facts.sysctl import get_sysctl

    darwin_hardware = DarwinHardware(dict(), None)
    darwin_hardware.sysctl = get_sysctl(None, ['hw', 'machdep', 'kern'])
    darwin_hardware.get_mac_facts()


# Generated at 2022-06-13 00:39:55.433902
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    from ansible.module_utils.six import BytesIO
    import mock

    kern_boottime = 1458551255
    mock_module = mock.MagicMock()
    mock_module.run_command.return_value = (0, BytesIO(struct.pack('@L', kern_boottime)), None)
    mock_module.get_bin_path.return_value = '/bin/sysctl'
    d = DarwinHardware(mock_module)
    results = d.get_uptime_facts()
    uptime_seconds = int(time.time() - kern_boottime)
    assert results == {'uptime_seconds': uptime_seconds}

# Generated at 2022-06-13 00:39:58.894488
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    p = DarwinHardware()
    facts = p.populate()
    assert facts['model'] == 'MacBookAir4,2'


# Generated at 2022-06-13 00:40:02.891781
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    macFacts = DarwinHardware(module).get_mac_facts()

    assert macFacts is not None
    assert 'model' in macFacts
    assert 'osversion' in macFacts
    assert 'osrevision' in macFacts

# Generated at 2022-06-13 00:40:10.105978
# Unit test for method get_mac_facts of class DarwinHardware

# Generated at 2022-06-13 00:40:14.399801
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    macfacts = DarwinHardware()
    facts = macfacts.populate()
    assert facts['model'] == 'MacBookPro10,1'
    assert facts['processor_cores'] == 2
    assert facts['memtotal_mb'] == 8192
    assert facts['memfree_mb'] == 6779
    assert facts['uptime_seconds'] == 958978

# Generated at 2022-06-13 00:40:15.888627
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    my_obj = DarwinHardwareCollector()
    assert my_obj._platform == 'Darwin'

# Generated at 2022-06-13 00:41:37.299589
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():

    test_mac_facts = {
            'model': 'MacBookPro',
            'osversion': '19.6.0',
            'osrevision': '15G14033'
            }

    test_sysctl = dict()
    test_sysctl['hw.model'] = 'MacBookPro'
    test_sysctl['kern.osversion'] = '19.6.0'
    test_sysctl['kern.osrevision'] = '15G14033'
    import ansible.module_utils.facts.hardware.darwin
    facts_class = ansible.module_utils.facts.hardware.darwin.DarwinHardware

    test_hardware = facts_class(None)
    test_hardware.sysctl = test_sysctl

    assert test_hardware.get_mac_facts() == test

# Generated at 2022-06-13 00:41:39.256821
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    module = object()
    darwin_hardware_collector = DarwinHardwareCollector(module)
    assert darwin_hardware_collector._fact_class == DarwinHardware
    assert darwin_hardware_collector._platform == 'Darwin'



# Generated at 2022-06-13 00:41:43.645431
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    class TestModule(object):
        def get_bin_path(self, arg):
            assert arg == 'sysctl'
            return arg

        def run_command(self, cmd, encoding=None):
            assert cmd == ['sysctl', '-b', 'kern.boottime']
            return 0, '\x00\x00\x00\x00\x00\x00\x00\x00', ''

    test_module = TestModule()
    darwin_hardware = DarwinHardware(test_module)
    facts = darwin_hardware.get_uptime_facts()
    assert facts == {
        'uptime_seconds': int(time.time()),  # seconds since epoch (now)
    }

# Generated at 2022-06-13 00:41:54.438168
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():

    # Create a dummy module
    module = AnsibleModule({})

    bare_metal_facts = {
        '/bin/uname': 'Darwin',
        'os.darwin_version': '13',
        'sysctl.get.hw.model': {'result': 'MacBookPro', 'rc': 0},
        'sysctl.get.kern.osversion': {'result': '15.3.0', 'rc': 0},
        'sysctl.get.kern.osrevision': {'result': '14G29', 'rc': 0},
    }


# Generated at 2022-06-13 00:42:02.466646
# Unit test for method get_system_profile of class DarwinHardware

# Generated at 2022-06-13 00:42:03.877951
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    result = DarwinHardwareCollector()
    assert result is not None
    assert isinstance(result, DarwinHardwareCollector)

# Generated at 2022-06-13 00:42:11.181422
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    test_system_profile_output = """
Hardware:

    Hardware Overview:

      Model Name: Mac Pro
      Model Identifier: MacPro2,1
      Processor Name: Quad-Core Intel Xeon
      Processor Speed: 2.66 GHz
      Number of Processors: 2
      Total Number of Cores: 8
      L2 Cache (per Processor): 12 MB
      Memory: 8 GB
      Bus Speed: 1.33 GHz
      Boot ROM Version: MP21.007F.B05
      SMC Version (system): 1.12f5
      Serial Number (system): G88532072CY
      Hardware UUID: 00000000-0000-1000-8000-0016CBB12502

"""
    dh_obj = DarwinHardware
    system_profile = dh_obj.get_system_profile(None, test_system_profile_output)

# Generated at 2022-06-13 00:42:20.467093
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    module = binary_type('')
    darwin_hw = DarwinHardware(module)
    darwin_hw.sysctl = {
        'machdep.cpu.brand_string': 'Intel(R) Core(TM) i7-3615QM CPU @ 2.30GHz',
        'machdep.cpu.core_count': '4',
        'hw.physicalcpu': '4',
        'hw.logicalcpu': '8',
    }
    cpu_facts = darwin_hw.get_cpu_facts()
    assert cpu_facts['processor'] == 'Intel(R) Core(TM) i7-3615QM CPU @ 2.30GHz'
    assert cpu_facts['processor_cores'] == '4'
    assert cpu_facts['processor_vcpus'] == '8'

    d

# Generated at 2022-06-13 00:42:28.152070
# Unit test for method get_cpu_facts of class DarwinHardware

# Generated at 2022-06-13 00:42:34.560922
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    module = AnsibleModule(argument_spec={})
    hw = module.get_bin_path('hw')
    kernel_version_cmd = module.get_bin_path('sw_vers')
    module.run_command = MagicMock(return_value=(0, "hw.model: x86_64", ''))
    module.run_command.return_value = (0, "5.0.0", '')
    hw_obj = DarwinHardware(module)
    facts = hw_obj.get_mac_facts()
    assert facts['model'] == 'x86_64'
    assert facts['model'] == 'x86_64'
    assert facts['osversion'] == '5.0.0'
    assert facts['osrevision'] == '5.0.0'