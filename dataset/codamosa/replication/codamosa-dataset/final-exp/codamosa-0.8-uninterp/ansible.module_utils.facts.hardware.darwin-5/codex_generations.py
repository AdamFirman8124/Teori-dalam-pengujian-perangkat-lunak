

# Generated at 2022-06-13 00:34:56.796770
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware

    expected_results = {'uptime_seconds' : 24 * 3600 + 12 * 60 + 34}
    # The value is based on the output of 'sysctl -b kern.boottime'

    test_value = b'\x80\x7a\x32\x01\x00\x00\x00\x00\x00\x00\x00\x00'
    test_object = DarwinHardware()
    test_object.sysctl = { 'kern.boottime': test_value }

    res = test_object.get_uptime_facts()
    assert res == expected_results

# Generated at 2022-06-13 00:35:07.761255
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    # Create mock module object
    module = type('module', (object,), {'run_command': classmethod(lambda *a, **kwa: (0, 'wired: 64255    active: 491819    inactive: 53889    free: 1159312', ''))})

    # Create mock type object
    type = type('type', (object,), {'__init__': lambda self, **kwargs: None})

    # Create dummy instance, and attach attributes.
    darwin_hardware = type()
    darwin_hardware.module = module
    darwin_hardware.sysctl = {'hw.memsize': '', 'hw.memsize_str': ''}

    # Call the function.
    result = darwin_hardware.get_memory_facts()

    # Check result.

# Generated at 2022-06-13 00:35:12.303003
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    actual = DarwinHardware({})._get_cpu_facts()
    expected = {'processor': 'Genuine Intel(R) CPU T2500 @ 2.00GHz',
                'processor_cores': '2', 'processor_vcpus': '2'}
    assert expected == actual

# Generated at 2022-06-13 00:35:19.575671
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    module = AnsibleModule(argument_spec={})
    module.run_command = MagicMock()
    module.run_command.return_value = (0, '', '')

    vm_stat_command = '/usr/bin/vm_stat'
    module.params['_ansible_remote_tmp'] = ''
    module.get_bin_path = MagicMock()
    module.get_bin_path.return_value = vm_stat_command

    result = dict()
    result['vm_stat_command'] = vm_stat_command

# Generated at 2022-06-13 00:35:29.740088
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    # Test set 1
    darwin_hardware = DarwinHardware(dict(), dict())
    darwin_hardware.sysctl = {'hw.model': 'MacPro6,1'}
    darwin_hardware.module.run_command = magic_mock(return_value=(0, 'hw.model: MacPro6,1', ''))
    facts = darwin_hardware.get_mac_facts()
    assert 'Mac Pro' == facts.get('model')
    assert 'Mac Pro' == facts.get('product_name')
    assert '15.3.0' == facts.get('osversion')
    assert '15.3.0' == facts.get('osrevision')

    # Test set 2
    darwin_hardware = DarwinHardware(dict(), dict())
    darwin_hard

# Generated at 2022-06-13 00:35:39.989733
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec={})
    hw = DarwinHardware(module)

    hw.sysctl = {
        'machdep.cpu.brand_string': 'Intel(R) Core(TM) i5-5250U CPU @ 1.60GHz',
        'machdep.cpu.core_count': 2,
        'hw.logicalcpu': 1,
        'hw.ncpu': 1,
        'hw.physicalcpu': 1,
    }

    expected = {
        'processor': u'Intel(R) Core(TM) i5-5250U CPU @ 1.60GHz',
        'processor_cores': 2,
        'processor_vcpus': 1,
    }

    # Run get_cpu_facts
    cpu_facts = hw.get_cpu_facts()


# Generated at 2022-06-13 00:35:49.217175
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    boottime = 1488380253
    boottime_bytes = struct.pack('@L', boottime)
    uptime = int(time.time()) - boottime

    class Module:
        def __init__(self):
            self.run_command_calls = []

        def run_command(self, cmd, encoding=None):
            self.run_command_calls.append(cmd)
            return (0, boottime_bytes, "")

        def get_bin_path(self, tool):
            return tool

    module = Module()
    hardware = DarwinHardware(module)
    facts = hardware.get_uptime_facts()
    assert facts == {'uptime_seconds': uptime}



# Generated at 2022-06-13 00:36:00.526804
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    def mock_run_command(self, *args, **kwargs):
        return 0, """
Hardware:

Hardware Overview:

  Model Name: MacBook Air
  Model Identifier: MacBookAir4,1
  Processor Name: Intel Core i7
  Processor Speed: 1.8 GHz
  Number of Processors: 1
  Total Number of Cores: 2
  L2 Cache (per Core): 256 KB
  L3 Cache: 4 MB
  Memory: 4 GB
  Boot ROM Version: MBA41.0077.B0C
  SMC Version (system): 2.3f36
  Serial Number (system): C02KL5B5DJR8
  Hardware UUID: DAD9F9B1-FA2F-5A4E-BC4A-4AF4D12611E7

""", ''
    m = Darwin

# Generated at 2022-06-13 00:36:08.784102
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    module = MockModule()
    darwin_hardware = DarwinHardware(module)
    darwin_hardware.sysctl = {'hw.memsize': '4096'}
    darwin_hardware.get_bin_path = Mock(return_value='/usr/bin/vm_stat')

# Generated at 2022-06-13 00:36:11.332120
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    assert DarwinHardwareCollector._platform == 'Darwin'
    assert DarwinHardwareCollector._fact_class == DarwinHardware



# Generated at 2022-06-13 00:36:31.464158
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    module = AnsibleModule(argument_spec=dict())

    class MockDarwinHardware():
        def __init__(self):
            self.sysctl = dict()
            self.sysctl['hw.memsize'] = 1
            self.sysctl['hw.physicalcpu'] = 2
            self.sysctl['hw.logicalcpu'] = 3
            self.sysctl['hw.ncpu'] = 4
            self.sysctl['kern.osversion'] = 5
            self.sysctl['kern.osrevision'] = 6

        def get_system_profile(self):
            return dict()

        def get_mac_facts(self):
            return dict()

        def get_cpu_facts(self):
            return dict()

        def get_memory_facts(self):
            return dict()


# Generated at 2022-06-13 00:36:39.796033
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    # Setup module
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    module.params['gather_subset'] = ['!all', 'min']

    # Setup mock data

# Generated at 2022-06-13 00:36:52.139588
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    import datetime
    import time

    class TestModule(object):
        def __init__(self, tt):
            self.run_command_results = tt

        def run_command(self, cmd, encoding=None):
            return self.run_command_results.pop(0)

        def get_bin_path(self, cmd):
            return '/usr/sbin/' + cmd

    # Run 1: sysctl returns a value greater than the current time
    tt1 = [(0, b'2147483648.000000\n', '')]
    test_module1 = TestModule(tt1)
    test_hardware1 = DarwinHardware(test_module1)
    uptime_facts1 = test_hardware1.get_

# Generated at 2022-06-13 00:37:02.514976
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    module = type('MockModule', (object,), dict(run_command=lambda cmd, encoding: (0, '', ''),
                                                get_bin_path=lambda x: x))
    hw = DarwinHardware(module)


# Generated at 2022-06-13 00:37:12.680385
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    class ModuleMock(object):
        def __init__(self, rc, out, err):
            self.rc = rc
            self.out = out
            self.err = err

        def run_command(self, cmd):
            return self.rc, self.out, self.err

    def test(out, expected_result):
        module = ModuleMock(0, out, '')
        assert expected_result == DarwinHardware(module).get_system_profile()


# Generated at 2022-06-13 00:37:13.171668
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    DarwinHardwareCollector()

# Generated at 2022-06-13 00:37:16.783719
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    module = AnsibleModuleMock()
    facts_collector = DarwinHardwareCollector(module)
    expected_class = DarwinHardware
    assert facts_collector._fact_class == expected_class
    assert facts_collector._platform == "Darwin"


# Generated at 2022-06-13 00:37:24.911090
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    test_cases = [
        # kern.boottime, uptime_seconds
        ('{ sec = 1481429561, usec = 0 }', 168 * 60 * 60),
    ]

    for boottime, uptime_seconds in test_cases:
        # creating class attributes
        module = None
        sys = None
        _fact_class = None
        _platform = None
        sysctl = {}
        sysctl['kern.boottime'] = boottime

        # creating the module object
        class dummy:
            def __init__(self):
                pass
        module = dummy()

        # creating the sys object
        class dummy:
            def __init__(self):
                pass
        sys = dummy()
        sys.maxint = 2147483647

        # creating the _fact_class object (required for DarwinHardware
       

# Generated at 2022-06-13 00:37:26.624790
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    assert DarwinHardwareCollector.__name__ == 'DarwinHardwareCollector'
    d_hw_collector = DarwinHardwareCollector()


# Generated at 2022-06-13 00:37:38.760584
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    class ModuleStub:
        run_command = lambda self, command, encoding=None: (0, 'Test run_command', '')
        get_bin_path = lambda self, bin: bin
        module_utils = None

    def sysctl_stub(module, names):
        fn = '_'.join(names)
        return globals()['sysctl_stub{0}'.format(fn)](module)

    def sysctl_stubkern_osversion():
        return '16.6.0'

    def sysctl_stubkern_osrevision():
        return '1'

    def sysctl_stubhw_model():
        return 'MacPro6,1'


# Generated at 2022-06-13 00:38:01.493024
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    # Trivial test to make sure the place holder is valid:
    assert True

# Generated at 2022-06-13 00:38:11.447492
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    import os
    import random
    import stat
    import tempfile

    from ansible.module_utils.six import BytesIO
    from ansible.module_utils.basic import AnsibleModule

    class TestModule(object):
        stdin = None
        stdout = None
        stderr = None
        _ansible_fake_socket = None  # Used by AnsibleModule.__init__

        def __init__(self, *args, **kwargs):
            self.args = args
            self.params = kwargs

        def run_command(self, *args, **kwargs):
            rc = 0
            out = BytesIO()
            err = BytesIO()
            cmd = args[0]

            # Format of kern.boottime
            # Time since boot, including microseconds.
            # 64-bit

# Generated at 2022-06-13 00:38:17.335040
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    module = mock.MagicMock()
    darwin_hardware = DarwinHardware(module)

    result = darwin_hardware.populate()

    assert 'model' in result
    assert 'osversion' in result
    assert 'osrevision' in result
    assert 'uptime_seconds' in result
    assert 'processor' in result
    assert 'processor_cores' in result
    assert 'processor_vcpus' in result
    assert 'memtotal_mb' in result
    assert 'memfree_mb' in result


# Generated at 2022-06-13 00:38:23.888235
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    test_module = DummyAnsibleModule()
    # Test Mac OS X:
    facts = DarwinHardware(test_module).get_mac_facts()
    assert facts['model'] == 'Macmini5,1'
    assert facts['osversion'] == '15.5.0'
    assert facts['osrevision'] == '15F34'



# Generated at 2022-06-13 00:38:35.708639
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    module = AnsibleModule(argument_spec=dict())
    hardware = DarwinHardware(module=module)
    collected_facts = {
        'os': {
            'family': 'Darwin'
        }
    }
    facts = hardware.populate(collected_facts=collected_facts)

# Generated at 2022-06-13 00:38:37.533758
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    darwin_hw = DarwinHardwareCollector()
    assert darwin_hw is not None


# Generated at 2022-06-13 00:38:39.994068
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    darwin_hardware_collector = DarwinHardwareCollector()
    assert darwin_hardware_collector._fact_class == DarwinHardware
    assert darwin_hardware_collector._platform == 'Darwin'

# Generated at 2022-06-13 00:38:43.375598
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    # Create an instance of DarwinHardwareCollector
    hardware_collector = DarwinHardwareCollector()

    # Assert that it is of the correct class
    assert isinstance(hardware_collector, HardwareCollector)

    # Assert the platform value
    assert hardware_collector._platform == 'Darwin'

# Generated at 2022-06-13 00:38:55.370703
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    module = FakeModule()
    setattr(module, 'run_command', lambda x: (0, "brand_string: Intel(R) Core(TM) i5-3210M CPU @ 2.50GHz", None))
    setattr(module, 'get_bin_path', lambda x: "/usr/bin/system_profiler")
    hardware = DarwinHardware(module)

# Generated at 2022-06-13 00:39:03.408882
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils.facts.collector.system import SystemCollector
    from ansible.module_utils.facts.collector.base import BaseFactCollector
    from ansible.module_utils.facts.collector import FactsCollector

    fact_collector = FactCollector(None, FactsCollector())
    system_collector = SystemCollector(fact_collector)
    fact_collector._module = None
    fact_collector.collector = [system_collector]
    hardware_collector = DarwinHardwareCollector(fact_collector)
    system_collector.set_children_collectors([hardware_collector])

    # mock the output of system_profiler SPHardwareDataType

# Generated at 2022-06-13 00:39:53.332638
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    test_obj = DarwinHardware()
    with open("unit/modules/utils/fixtures/facts/system_profiler.txt", "r") as fixture_file:
        test_obj.module.run_command = lambda *args, **kwargs: (0, fixture_file.read(), "")

# Generated at 2022-06-13 00:39:55.473669
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    collect = DarwinHardwareCollector()
    assert collect.platform == 'Darwin'
    assert collect.fact_class.platform == 'Darwin'


# Generated at 2022-06-13 00:40:03.014816
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec=dict())
    hardware = DarwinHardware(module)
    cpu_facts = hardware.get_cpu_facts()
    assert 'processor' in cpu_facts
    assert isinstance(cpu_facts['processor'], basestring)
    assert 'processor_cores' in cpu_facts
    assert isinstance(cpu_facts['processor_cores'], int)
    assert 'processor_vcpus' in cpu_facts
    assert isinstance(cpu_facts['processor_vcpus'], basestring)



# Generated at 2022-06-13 00:40:10.179458
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    module = object()

# Generated at 2022-06-13 00:40:16.613762
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    test_module = type('module', (object,), {
        'get_bin_path': lambda self, bin: bin,
        'run_command': lambda self, cmd: (0, "Pages wired down: 3\nPages active: 2\nPages inactive: 1\n", ""),
    })

    test_module = test_module()
    test_obj = DarwinHardware(test_module)
    result = test_obj.get_memory_facts()
    expected = {
        'memtotal_mb': 0,
        'memfree_mb': 0,
    }
    assert result == expected

# Generated at 2022-06-13 00:40:27.394554
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    module = FakeModule()
    hardware = DarwinHardware(module)

    module.run_command_args['rc'] = 0
    module.run_command_args['out'] = """hw.model: iMac13,2"""

    module.run_command_args['rc'] = 0
    module.run_command_args['out'] = """kern.osversion: 14.2.0
    kern.osrevision: 14C1514"""

    hardware.sysctl = {'kern.osversion': "14.2.0",
                       'kern.osrevision': "14C1514"}

    expected = {'model': 'iMac13,2',
                'osrevision': '14C1514',
                'osversion': '14.2.0'}

    assert expected == hardware.get_mac_facts()

# Generated at 2022-06-13 00:40:32.486865
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    module = None
    data1 = """
        {
            "uptime": "14:33 up 12 days, 21:50, 7 users, load averages: 2.04 2.40 2.38"
        }
        """
    data2 = """
        {
            "hostname": "local-hostname"
        }
        """
    data3 = """
        {
            "boottime": "1343134731.0"
        }
        """
    data4 = """
    {
        "path": [
            "/usr/bin",
            "/bin",
            "/usr/sbin",
            "/sbin"
        ]
    }
    """

# Generated at 2022-06-13 00:40:40.626615
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    # DarwinHardware.get_uptime_facts returns a dict with uptime_seconds value.
    # So, we create a dict with the same key and expected value.
    # And compare it to the result of DarwinHardware.get_uptime_facts
    module = MockModule()
    darwin_hardware = DarwinHardware(module=module)
    expected_uptime_facts = {'uptime_seconds': 123}
    real_uptime_facts = darwin_hardware.get_uptime_facts()
    assert real_uptime_facts == expected_uptime_facts



# Generated at 2022-06-13 00:40:44.361596
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    # A simple class instance creation should be enough to run
    # all the test cases from the class.
    test = DarwinHardwareCollector()
    assert test._fact_class is DarwinHardware

# Generated at 2022-06-13 00:40:54.298050
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    facts = {'module': {
        'run_command': lambda x, **kwargs: (0, '/usr/sbin/system_profiler SPHardwareDataType', '')
    }}
    m = DarwinHardware(facts, None)
    res = m.get_cpu_facts()
    assert res['processor'] == 'Intel Core i5 @ 2.2 GHz'
    assert res['processor_cores'] == 4
    assert res['processor_vcpus'] == ''

    facts = {'module': {
        'run_command': lambda x, **kwargs: (0, 'hw.model: PowerMac6,2\nhw.physicalcpu: 2\nhw.logicalcpu: 4\n', '')
    }}
    m = DarwinHardware(facts, None)
    res = m.get_cpu_facts()

# Generated at 2022-06-13 00:42:22.646279
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    import os
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    mem_facts = DarwinHardware()
    mem_facts.module = os
    facts = mem_facts.get_memory_facts()
    assert facts['memtotal_mb'] == int(mem_facts.sysctl['hw.memsize']) // 1024 // 1024
    assert 'memfree_mb' in facts


# Generated at 2022-06-13 00:42:29.627250
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    class MockModule(object):
        def __init__(self, out, rc):
            self.out = out
            self.rc = rc
            self.run_command_called = 0

        def run_command(self, command):
            self.run_command_called += 1
            return self.rc, self.out, ""


# Generated at 2022-06-13 00:42:33.520643
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    mock_module = type("MockModule",(object,),{"run_command": (0, "hw.model: macbookair4,2\n", ""), "get_bin_path": (0, "/usr/bin/vm_stat\n", "")})
    mock_module = mock_module()

    class DarwinHardwareTest(DarwinHardware):
        module = mock_module

    d = DarwinHardwareTest()
    d.get_mac_facts()

# Generated at 2022-06-13 00:42:34.407773
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    d = DarwinHardwareCollector()
    assert d.get_platform() == 'Darwin'

# Generated at 2022-06-13 00:42:37.145229
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    test_hardware = DarwinHardware()
    test_hardware.module = object()
    test_hardware.module.run_command = run_command_mock
    test_result = {'memtotal_mb': 60000, 'memfree_mb': 10000}

    if test_hardware.get_memory_facts() != test_result:
        raise AssertionError("Test failed, expected: %s, result: %s" % (test_result, test_hardware.get_memory_facts()))



# Generated at 2022-06-13 00:42:47.896419
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    class FakeModule:
        def run_command(self, cmd):
            class FakeResult:
                rc = 0
                err = ''
                out = ''

                def __init__(self, rc, out, err):
                    self.rc = rc
                    self.out = out
                    self.err = err
            if cmd[0] != "/usr/sbin/system_profiler":
                FakeResult(1, '', 'Not system_profiler')

            if cmd[1] != "SPHardwareDataType":
                FakeResult(1, '', 'Not SPHardwareDataType')


# Generated at 2022-06-13 00:42:56.354948
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    class Options():
        def __init__(self, module=None):
            self.module = module
    class Module():
        def __init__(self):
            self.options = Options(module=self)
        def verbose(self): return False
        def get_bin_path(self, option):
            return '/usr/sbin/system_profiler'

# Generated at 2022-06-13 00:43:04.958928
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    import unittest

# Generated at 2022-06-13 00:43:11.060143
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    import re
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware

    darwin_hardware = DarwinHardware(None)

    # Setup the module argument spec
    argument_spec = dict()
    darwin_hardware.module = AnsibleModule(argument_spec=argument_spec,
                                           supports_check_mode=True)

    # Set module.run_command to a mock
    darwin_hardware.module.run_command = MagicMock(return_value=(0, "hw.model: Intel Core i7", ""))

    # Execute
    mac_facts = darwin_hardware.get_mac_facts()

    # Assert
    assert mac_facts['model'] == 'Intel Core i7'
   

# Generated at 2022-06-13 00:43:22.029547
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    hardware = DarwinHardware(dict(module=None))
    hardware.sysctl = dict(machdep=dict(cpu=dict(brand_string='Intel Core i5 - 1.2 GHz', core_count='2')))
    cpu_facts = hardware.get_cpu_facts()
    assert cpu_facts.get('processor') == 'Intel Core i5 - 1.2 GHz'
    assert cpu_facts.get('processor_cores') == '2'

    hardware.sysctl = dict(hw=dict(physicalcpu='4'))
    cpu_facts = hardware.get_cpu_facts()
    assert cpu_facts.get('processor') == '%s @ %s' % ('PowerPC G4', '1.0 GHz')
    assert cpu_facts.get('processor_cores') == '4'

