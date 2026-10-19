

# Generated at 2022-06-13 00:34:58.407971
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    import platform
    out = 'out'
    module = MagicMock()
    facts = DarwinHardware(module)
    facts.module.run_command.return_value = (0, out, '')
    facts.sysctl = {'kern.osversion': '10.9', 'kern.osrevision': '13A603'}
    mac_facts = facts.get_mac_facts()
    assert mac_facts['model'] == out.splitlines()[-1].split()[1]
    assert mac_facts['osversion'] == facts.sysctl['kern.osversion']
    assert mac_facts['osrevision'] == facts.sysctl['kern.osrevision']
    module.run_command.assert_called_with('sysctl hw.model')



# Generated at 2022-06-13 00:35:00.360428
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    darwin_hardware_collector = DarwinHardwareCollector()
    assert darwin_hardware_collector._platform == 'Darwin'

# Generated at 2022-06-13 00:35:09.579234
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    hardware = DarwinHardware()
    rc_cmd_sysctl_hw_model = 0
    out_cmd_sysctl_hw_model = 'hw.model: MacBookPro11,4\n'
    err_cmd_sysctl_hw_model = ''

    hardware.module.run_command = lambda cmd, **kwargs: (rc_cmd_sysctl_hw_model, out_cmd_sysctl_hw_model, err_cmd_sysctl_hw_model)
    hardware.sysctl = {
        'kern.osversion': '15.5.0',
        'kern.osrevision': '17F77'
    }

    mac_facts = hardware.get_mac_facts()

    assert mac_facts['osversion'] == '15.5.0'

# Generated at 2022-06-13 00:35:19.576151
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    # A fake module object
    class FakeModule:
        def __init__(self):
            self.run_command_results = []
            self.run_command_calls = []
            self.get_bin_path_results = []
            self.get_bin_path_calls = []

        def get_bin_path(self, arg):
            self.get_bin_path_calls.append(arg)
            return self.get_bin_path_results.pop()

        def run_command(self, args, encoding=None, errors='strict'):
            self.run_command_calls.append(args)
            return self.run_command_results.pop()

    # A fake vm_stat output

# Generated at 2022-06-13 00:35:26.936791
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    """
    Legacy test to verify the output of get_system_profile()
    """
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware

    module = FakeAnsibleModule()
    # Run the test
    obj = DarwinHardware(module)
    system_profile = obj.get_system_profile()

    # Make sure we got a dict
    assert isinstance(system_profile, dict)

    # Make sure the dict has more than 1 keys
    assert len(system_profile) > 1

    return True



# Generated at 2022-06-13 00:35:37.261076
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    
    # Set up a mock of sysctl()
    sysctl_method_name = 'sysctl'
    sysctl_method = Mock(return_value={
        'machdep.cpu.brand_string': 'Intel(R) Core(TM) i7-4790K CPU @ 4.00GHz',
        'machdep.cpu.core_count': 8,
    })

    # Set up a mock of system_profiler()
    system_profile_method_name = 'get_system_profile'
    system_profile_method = Mock(return_value={
        'Processor Name': 'PowerPC G4',
        'Processor Speed': '1 GHz',
    })

    # Patch sysctl and system_profiler methods

# Generated at 2022-06-13 00:35:40.108796
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    darwinHardwareCollector = DarwinHardwareCollector()
    assert darwinHardwareCollector.platform == 'Darwin'
    assert darwinHardwareCollector.fact_class == DarwinHardware

# Generated at 2022-06-13 00:35:46.630927
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    module = AnsibleModuleMock()
    module.run_command.return_value = (0, '2.2', '')
    darwin_hardware = DarwinHardware(module)
    darwin_hardware.get_mac_facts = mock.Mock(return_value={'model': 'MacBook Pro', 'osversion': '10.12.3', 'osrevision': '16D32'})
    darwin_hardware.get_cpu_facts = mock.Mock(return_value={'processor_cores': '4', 'processor': 'Intel(R) Core(TM) i7-4980HQ CPU @ 2.80GHz', 'processor_vcpus': ''})

# Generated at 2022-06-13 00:35:57.879520
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    # Prepare data
    out = b''
    cmd = ''
    rc = 0
    err = ''

    # Prepare args
    class Args:
        def __init__(self):
            self.bin_path = ''

    args = Args()

    # Prepare class
    class Bin:
        def __init__(self):
            pass

        def get(self, cmd, default=None, required=False, opt_dirs=[]):
            return cmd

    class Mod:
        def __init__(self):
            pass

        def get_bin_path(self, cmd, **kwargs):
            return cmd

        def run_command(self, cmd, encoding=None):
            return rc, out, err

    mod = Mod()
    mod.get_bin_path = Bin().get

# Generated at 2022-06-13 00:36:03.918552
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    module = None
    hardware_facts = DarwinHardware(module=module)
    test_set = [b'{ sec = 1569653349, usec = 794538 }']
    for test_out in test_set:
        test_out = test_out

        uptime_facts = hardware_facts.get_uptime_facts()
        assert isinstance(uptime_facts['uptime_seconds'], int)

# Generated at 2022-06-13 00:36:16.470652
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    darwin_hardware_collector = DarwinHardwareCollector()
    assert darwin_hardware_collector.platform == 'Darwin'
    assert darwin_hardware_collector.fact_class == DarwinHardware

# Generated at 2022-06-13 00:36:26.212965
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    import mock
    import sys
    import os

    class MockModule():
        def __init__(self, **kwargs):
            self.params = kwargs

        def get_bin_path(self, *args, **kwargs):
            return '/bin/sysctl'

        def run_command(self, *args, **kwargs):
            return 0, b'\x00\x00\x04\x25\x8b\x65\x0c\x40\x00\x00\x00\x00', ''

    m = mock.Mock(spec=MockModule)
    m.run_command.return_value = 0, b'\x00\x00\x04\x25\x8b\x65\x0c\x40\x00\x00\x00\x00',

# Generated at 2022-06-13 00:36:35.405518
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    import platform
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware

    test_sysctl = {
        'hw.memsize': '8589934592',
        'hw.ncpu': '8'
    }

    def mock_get_sysctl(module, keys):
        return test_sysctl

    monkeypatch.setattr(DarwinHardware, 'get_system_profile', lambda x: {})
    monkeypatch.setattr(DarwinHardware, 'sysctl', test_sysctl)
    monkeypatch.setattr(DarwinHardware, 'get_sysctl', mock_get_sysctl)
    monkeypatch.setattr(platform, 'system', lambda: 'Darwin')


# Generated at 2022-06-13 00:36:40.708632
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    module = FakeModule()
    hardware = DarwinHardware(module=module)

    # test default case
    module.run_command = FakeModuleRunCommand((0, 'hw.model: Intel(R) Core(TM) i7-6500U CPU @ 2.50GHz', ''))
    expected_result = {'model': 'Intel(R) Core(TM) i7-6500U CPU @ 2.50GHz', 'osversion': '', 'osrevision': ''}
    assert hardware.get_mac_facts() == expected_result

    # test case with sysctl returning a non zero rc
    module.run_command = FakeModuleRunCommand((1, '', 'ERROR'))
    expected_result = {'model': '', 'osversion': '', 'osrevision': ''}
    assert hardware.get_mac_facts() == expected_

# Generated at 2022-06-13 00:36:44.595880
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    module = AnsibleModule(dict())
    hardware_facts_module = DarwinHardware(module)
    hardware_facts = hardware_facts_module.populate()
    assert hardware_facts
    assert hardware_facts['product_name']

# Generated at 2022-06-13 00:36:51.335932
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    """
    Test get_system_profile method of DarwinHardware
    """
    args = {
        'ansible_facts': {}
    }
    import ansible.module_utils.facts.hardware.darwin
    system_profile = ansible.module_utils.facts.hardware.darwin.DarwinHardware.get_system_profile(args)
    assert isinstance(system_profile, dict)

# Generated at 2022-06-13 00:37:00.273067
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    import os


# Generated at 2022-06-13 00:37:02.722772
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    darwin_hw_collector = DarwinHardwareCollector(None)
    assert darwin_hw_collector.platform == 'Darwin'

# Generated at 2022-06-13 00:37:08.273770
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    not_booted = struct.pack('@L', 0)
    assert DarwinHardware._get_uptime_facts(not_booted) == {}

    one_day = struct.pack('@L', 24*60*60)
    assert DarwinHardware._get_uptime_facts(one_day) == {'uptime_seconds': 24*60*60}

# Generated at 2022-06-13 00:37:15.141384
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    module = MockAnsibleModule()
    module.run_command.return_value = (
        0,
        'hw.model: Power Macintosh\n',
        ''
    )
    dh = DarwinHardware(module)
    mac_facts = dh.get_mac_facts()
    assert mac_facts == {
        'model': 'Power Macintosh',
        'osversion': '15.6.0',
        'osrevision': '15.6.0'
    }



# Generated at 2022-06-13 00:37:40.124454
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    # Create a mock module and get the class under test
    mock_module = type('MockModule', (object,), dict())
    hardware = DarwinHardware(mock_module)

    # Mock sysctl to return a valid response
    hardware.sysctl = dict(kern_boottime=int(time.time() - 100))

    # Execute the method and validate the result
    assert hardware.get_uptime_facts() == {'uptime_seconds': hardware.sysctl['kern_boottime']}

# Generated at 2022-06-13 00:37:47.617637
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    from ansible.module_utils._text import to_bytes

    test_module = AnsibleModule(argument_spec=dict(
        gather_subset=dict(type='list', default=['all']),
    ))

    test_class = DarwinHardware(test_module)


# Generated at 2022-06-13 00:37:57.649284
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    module = MockAnsibleModule()
    hardware = DarwinHardware(module)
    hardware.sysctl = dict(
        machdep=dict(cpu=dict()),
        hw=dict(
            memsize=4294967296,
            physicalcpu=4,
            logicalcpu_max=4,
        ),
        kern=dict(osversion='15.6.0', osrevision=1671),
    )
    hardware.get_system_profile = lambda self: {'Processor Name': 'Intel Xeon', 'Processor Speed': '2.7 GHz'}
    hardware.get_mac_facts = lambda self: dict(model='MacBookPro8,1')
    hardware.get_cpu_facts = lambda self: dict(processor='Intel Xeon', processor_cores=4)

# Generated at 2022-06-13 00:38:08.353256
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )
    hardware = DarwinHardware(module)
    hardware_facts = hardware.populate()
    assert hardware_facts['model'] == '[Hardware Model]'  # Replace with a real value
    assert hardware_facts['processor'] == '[Processor Name]'  # Replace with a real value

# Generated at 2022-06-13 00:38:14.453761
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    from ansible_collections.community.general.plugins.module_utils.facts.hardware import DarwinHardware

    memory_facts = DarwinHardware().get_memory_facts()
    assert memory_facts['memtotal_mb'] > 0, "Memory facts should be > 0MB"
    assert memory_facts['memfree_mb'] >= 0, "Free memory facts should be >= 0MB"
    assert memory_facts['memtotal_mb'] >= memory_facts['memfree_mb'], "Total memory facts should be >= free memory facts"

# Generated at 2022-06-13 00:38:15.495003
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    assert issubclass(DarwinHardwareCollector, HardwareCollector)

# Generated at 2022-06-13 00:38:21.726356
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    module = AnsibleModule(argument_spec=dict())
    hardware = DarwinHardware(module)
    setattr(module, 'run_command', test_run_command)
    memory_facts = hardware.get_memory_facts()
    assert memory_facts['memtotal_mb'] == 1000
    assert memory_facts['memfree_mb'] == 500

# Generated at 2022-06-13 00:38:26.230017
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    module = AnsibleModule(argument_spec={})
    hardware = DarwinHardware(module)
    content = hardware.populate()
    assert content['memtotal_mb'] is not None
    assert content['memfree_mb'] is not None
    assert content['processor'] is not None
    assert content['processor_cores'] is not None
    assert content['processor_vcpus'] is not None
    assert content['model'] is not None
    assert content['osversion'] is not None
    assert content['osrevision'] is not None
    assert content['uptime_seconds'] is not None

# Generated at 2022-06-13 00:38:37.399607
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    hardware = DarwinHardware()
    hardware.sysctl = {'kern.osversion': '1.0.0', 'kern.osrevision': '1.0.0'}
    rc, out, err = hardware.module.run_command("sysctl hw.model")

    hardware.populate()

    assert hardware.sysctl['kern.osversion'] == hardware.facts['osversion']
    assert hardware.sysctl['kern.osrevision'] == hardware.facts['osrevision']
    assert out.splitlines()[-1].split()[1] == hardware.facts['model']
    assert out.splitlines()[-1].split()[1] == hardware.facts['product_name']


# Generated at 2022-06-13 00:38:45.368720
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    mac_memory_facts = {'memtotal_mb': 8192, 'memfree_mb': 5013}

    mac = DarwinHardware()

    mac.sysctl = {'hw.memsize': '8589934592'}

    def mock_run_command(module, *args, **kwargs):
        module.run_command_environ_update = {
            'LC_ALL': 'C'
        }

# Generated at 2022-06-13 00:39:24.613058
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    # Get the standard imports out of the way
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    from ansible.module_utils.facts.hardware.darwin import test_DarwinHardware_get_uptime_facts

    # We need to do this to mock out get_binpath()
    from ansible.module_utils.facts.hardware.darwin import get_bin_path
    import ansible.module_utils.facts.hardware.darwin

    # Get the value of sysctl_cmd
    sysctl_cmd = ansible.module_utils.facts.hardware.darwin.get_bin_path('sysctl')

    # And now we mock it out

# Generated at 2022-06-13 00:39:26.774473
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    darwin_hardware_collector = DarwinHardwareCollector()
    assert darwin_hardware_collector is not None

# Generated at 2022-06-13 00:39:37.360323
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    import os

    # Create a fake module
    class MockModule():
        def __init__(self):
            self.run_command = os.system

    class MockFacts(object):
        def __init__(self):
            self._module = MockModule()
            self._sysctl = {'kern.boottime': 0}

        def get(self, key, default=None):
            return self._sysctl.get(key, default)

        def get_sysctl(self, sysctl_keys):
            return self._sysctl

        def which(self, command):
            return 'sysctl'

    fact = DarwinHardware()
    fact._facts = MockFacts()
    assert fact.get_uptime_facts() == {'uptime_seconds': 0}

# Generated at 2022-06-13 00:39:44.568527
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    free_mem = 1024
    rc = 0

# Generated at 2022-06-13 00:39:48.133477
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    # Arrange

    # Act
    darwin_hardware_collector = DarwinHardwareCollector()

    # Assert
    assert darwin_hardware_collector._fact_class == DarwinHardware

if __name__ == "__main__":
    test_DarwinHardwareCollector()

# Generated at 2022-06-13 00:39:58.980625
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    import os
    import mock
    import platform
    import tempfile
    import textwrap
    import time
    import unittest

    # TODO: Ideally, we would prevent the real module_utils/common/process.py
    # script from loading.  At the time of this writing, however, mock.patch
    # is not able to do this.  One of mock's developers has opened a ticket
    # for this behavior (https://bugs.python.org/issue25589).
    #
    # We could also consider using unittest.mock.patch.dict() to replace
    # sys.modules.  However, the mock documentation warns that this is
    # potentially fragile because the implementation may change, or
    # a third-party module may also change sys.modules.
    #
    # For now, we use a method that appears to work.


# Generated at 2022-06-13 00:40:00.212029
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    facts = DarwinHardwareCollector(None)
    assert facts.platform == 'Darwin'

# Generated at 2022-06-13 00:40:08.370104
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    import platform
    import re

    module = AnsibleModuleMock()
    darwin_hw = DarwinHardware(module)
    darwin_hw.sysctl = {
        'hw.model': 'iMacPro1,1',
        'kern.osversion': 'Darwin Kernel Version 17.3.0: Fri Nov 3 21:18:23 PST 2017; root:xnu-4570.31.3~1/RELEASE_X86_64',
        'kern.osrevision': '17.3.0'
    }

    mac_facts = darwin_hw.get_mac_facts()
    # Test model
    assert mac_facts.get('model', None) == 'iMacPro1,1'
    # Test osversion

# Generated at 2022-06-13 00:40:17.166975
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware

    m = object()
    dh = DarwinHardware(m)

    rc = 0
    out = '''Hardware:

  Hardware Overview:

    Model Name: iMac
    Model Identifier: iMac10,1
    Processor Name: Intel Core 2 Duo
    Processor Speed: 3.06 GHz
    Number Of Processors: 1
    Total Number Of Cores: 2
    L2 Cache: 6 MB
    Memory: 4 GB
    Bus Speed: 1.07 GHz
    Boot ROM Version: IM101.007A.B03
    SMC Version: 1.49f2
    Serial Number: QP0340E6GHR
    Hardware UUID: 00000000-0000-1000-8000-00C04F56ED52

'''
    err = ''
    result

# Generated at 2022-06-13 00:40:23.609378
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    module = type('TestModule', (object,), dict(run_command=test_DarwinHardware_get_uptime_facts_run_command))

    darwin_hardware = DarwinHardware(module)
    uptime_facts = darwin_hardware.get_uptime_facts()

    assert uptime_facts == {
        'uptime_seconds': 123456789,
    }



# Generated at 2022-06-13 00:41:40.327932
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    # Valid output of kern.boottime from macOS 10.12.1 on a kernel Darwin 16.1.0.
    test_kern_boottime = b'\xF3\xC4\n\x00i\x00\x00\x00\x00\x00\x00'
    module = object()
    hardware = DarwinHardware(module)

    assert hardware.get_uptime_facts() == {
        'uptime_seconds': 300,
    }

# Generated at 2022-06-13 00:41:44.043252
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    myself = DarwinHardware()
    myself.module.run_command = lambda x: [0, "hw.machdep.cpu.brand_string=Intel(R) Core(TM) i7-4790K CPU @ 4.00GHz\nhw.physicalcpu=4", ""]
    cpu_facts = myself.get_cpu_facts()
    assert 'Intel(R) Core(TM) i7-4790K CPU @ 4.00GHz' == cpu_facts['processor']
    assert '4' == cpu_facts['processor_cores']
    assert '4' == cpu_facts['processor_vcpus']


# Generated at 2022-06-13 00:41:54.881121
# Unit test for method get_system_profile of class DarwinHardware

# Generated at 2022-06-13 00:42:02.740966
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    darwin_system_profile = [
        'Model Name: MacBook Pro',
        'Processor Name: Intel Core i7',
        'Processor Speed: 2.3 GHz',
        'Number of Processors: 1',
        'Total Number of Cores: 4',
        'L2 Cache (per Core): 256 KB',
        'L3 Cache: 6 MB',
        'Memory: 16 GB',
        'Boot ROM Version: MBP101.00EE.B03',
        'SMC Version (system): 2.7f0',
        'Serial Number (system): C02QE7VQG3QH',
        'Hardware UUID: D5EC5C5F-57B7-5687-B1F9-FC132729D890'
    ]

# Generated at 2022-06-13 00:42:08.034997
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    HW = DarwinHardware()
    HW.sysctl = {'kern.osversion': '16.6.0'}
    HW.get_system_profile = lambda: {'Processor Name': 'Intel i7', 'Processor Speed': '2 GHz'}
    result = HW.get_mac_facts()
    assert result['osversion'] == '16.6.0'
    assert result['model'] == 'Intel i7'
    assert result['product_name'] == 'Intel i7'
    assert result['osrevision'] == ''


# Generated at 2022-06-13 00:42:13.645818
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    hardware = DarwinHardware({})
    hardware.sysctl = {
        'kern.osversion': '10.13.1',
        'kern.osrevision': '15B42',
    }
    hardware.get_system_profile = lambda: {
        'Processor Name': 'Intel Core i7',
        'Processor Speed': '3.4 GHz',
    }

    hardware.module.run_command = lambda cmd: (0, 'hw.model: MacBookPro13,1\n', '')

    expected_mac_facts = {
        'model': 'MacBookPro13,1',
        'osversion': '10.13.1',
        'osrevision': '15B42',
    }

    assert hardware.get_mac_facts() == expected_mac_facts


# Generated at 2022-06-13 00:42:23.241019
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    test_string = '''Hardware:

    Hardware Overview:

      Model Name: MacBook Pro
      Model Identifier: MacBookPro11,1
      Processor Name: Intel Core i5
      Processor Speed: 2.6 GHz
      Number of Processors: 1
      Total Number of Cores: 2
      L2 Cache (per Core): 256 KB
      L3 Cache: 3 MB
      Memory: 8 GB
      Boot ROM Version: MBP111.0138.B17
      SMC Version (system): 2.18f15
      Serial Number (system): C02N55R5DTFJ
      Hardware UUID: 0ABE31BD-7D21-5D2C-935C-DBDA03FBCF1C

'''


# Generated at 2022-06-13 00:42:30.012358
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    hardware = DarwinHardware()

    # Test for Intel Mac Pro
    hardware.sysctl = {'machdep.cpu.brand_string': 'Intel(R) Xeon(R) CPU E5-2667 0 @ 2.90GHz', 'machdep.cpu.core_count': 2}
    cpu_facts = hardware.get_cpu_facts()
    assert cpu_facts == {'processor': 'Intel(R) Xeon(R) CPU E5-2667 0 @ 2.90GHz', 'processor_cores': 2, 'processor_vcpus': None}

    # Test for PowerPC
    hardware.sysctl = {'hw.physicalcpu': 2}
    cpu_facts = hardware.get_cpu_facts()
    assert 'processor' in cpu_facts
    assert cpu_facts['processor_cores'] == 2
    assert cpu_facts

# Generated at 2022-06-13 00:42:35.005786
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    module = FakeModule(
        dict(
            filename='/usr/bin/vm_stat',
            check_invalid_arguments=False,
        ),
        dict(),
    )

    def run_command(command, *args, **kwargs):
        encoding = kwargs.get('encoding')
        if encoding == 'utf-8':
            return 1, '', ''
        elif encoding is None:
            # We only care about the time difference between the current time
            # and kern.boottime.
            return 0, '1', ''
        else:
            return None, None, None

    module.run_command = run_command

    def get_bin_path(cmd):
        return '/usr/bin/%s' % cmd

    module.get_bin_path = get_bin_path


# Generated at 2022-06-13 00:42:45.604324
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    class DarwinHardwareStub(DarwinHardware):
        def __init__(self, module=None):
            super(DarwinHardwareStub, self).__init__(module=module)

        @property
        def sysctl(self):
            return {'hw.memsize': '16777216'}

    darwin_hardware_stub = DarwinHardwareStub()
    memory_facts = darwin_hardware_stub.get_memory_facts()

    # Total memory is hard-coded to 16777216 bytes
    assert memory_facts['memtotal_mb'] == 16
    # vm_stat stubbed to return 0 for all fields except Pages wired down
    assert memory_facts['memfree_mb'] == 16
