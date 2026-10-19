

# Generated at 2022-06-13 00:45:33.538675
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    class ModuleMock():
        def __init__(self):
            self.bin_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'ansible'))

        def get_bin_path(self, exe):
            return os.path.join(self.bin_path, exe)

        def run_command(self, cmd, check_rc=True, encoding=None):
            p = os.path.join(self.bin_path, 'test/unit/module_utils/facts/test_get_memory_facts')
            return os.system(p + ' ' + cmd), '', ''

    h = FreeBSDHardware(ModuleMock())
    h.get_memory_facts()



# Generated at 2022-06-13 00:45:34.934150
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    freebsd_collector = FreeBSDHardwareCollector()
    assert freebsd_collector._platform == 'FreeBSD'


# Generated at 2022-06-13 00:45:37.851801
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    module = AnsibleModule(argument_spec={})
    populator = FreeBSDHardware(module=module)
    res = populator.populate()
    for necessary_fact in ['memtotal_mb', 'processor', 'uptime_seconds']:
        assert necessary_fact in res
    assert isinstance(res['processor'], list)

# Generated at 2022-06-13 00:45:50.273906
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    hw_fixture = FreeBSDHardware({}, {}, {}, {})

    # hw_fixture.get_cpu_facts()
    hw_fixture.module.get_bin_path = lambda x: '/sbin/' + x
    hw_fixture.module.run_command = lambda x, **kwargs: (0, 'hw.ncpu: 4', '')

    # hw_fixture.get_memory_facts()
    hw_fixture.module.run_command = lambda x, **kwargs: (0, 'vm.stats.vm.v_page_size: 16384\nvm.stats.vm.v_page_count: 8763732\nvm.stats.vm.v_free_count: 213466', '')

    # hw_fixture.get_uptime_facts

# Generated at 2022-06-13 00:45:58.335674
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    class ModuleProxy(object):
        def __init__(self, args):
            self.args = args
        def get_bin_path(self, arg):
            if arg == 'sysctl':
                return 'echo 47'
        def run_command(self, arg, check_rc=False, encoding='utf-8'):
            return (0, 'hw.ncpu: 47', None)
    module = ModuleProxy(None)
    hardware = FreeBSDHardware(module)
    cpu_facts = hardware.get_cpu_facts()
    assert cpu_facts['processor_cores'] == '47'


# Generated at 2022-06-13 00:46:08.588034
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    from ansible.module_utils.facts import ModuleFacts
    from ansible.module_utils.facts.collector import FactsCollector
    module = MockModule()
    stub_bin_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                 'unit_tests', 'stubbin')
    stub_dmidecode_output = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                         'unit_tests', 'stubbin', 'dmidecode.json')
    module.params['gather_subset'] = ['hardware']
    module.get_bin_path = Mock(return_value=stub_bin_path)
    result = ModuleFacts(module).get_facts()

# Generated at 2022-06-13 00:46:09.309623
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    fhc = FreeBSDHardwareCollector()
    assert fhc is not None

# Generated at 2022-06-13 00:46:11.892103
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    from ansible.module_utils import basic

    m = basic.AnsibleModule(
        argument_spec = dict(),
    )

    hw = FreeBSDHardware(m)
    uptime_facts = hw.get_uptime_facts()
    assert uptime_facts.keys() == ['uptime_seconds']
    assert uptime_facts['uptime_seconds'] > 0

# Generated at 2022-06-13 00:46:17.810525
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    module = AnsibleModule(argument_spec={})
    bsd = FreeBSDHardware(module=module)
    # Get uptime_seconds
    res = bsd.get_uptime_facts()['uptime_seconds']
    if not isinstance(res, int):
        module.fail_json(msg="get_uptime_facts return %s, is not int" % res)


# Generated at 2022-06-13 00:46:27.054320
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    class MockModule(object):
        def __init__(self):
            self.params = {}

        def run_command(self, cmd, encoding=None, check_rc=False):
            self.cmd = cmd
            return 1, '123', 'answer'

        def get_bin_path(self, cmd):
            return cmd

    class Args(object):
        def __init__(self, params):
            self.module = MockModule()
            self.module.params = params

    hardware = FreeBSDHardware(Args({}))
    facts = hardware.get_dmi_facts()
    assert facts['bios_date'] == 'NA'
    assert facts['bios_vendor'] == 'NA'
    assert facts['bios_version'] == 'NA'
    assert facts['board_asset_tag'] == 'NA'

# Generated at 2022-06-13 00:46:47.654769
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    # Create a FreeBSDHardware instance
    fhw = FreeBSDHardware()

    # Mock needed classes/methods
    class ModuleMock():
        def __init__(self):
            self.sysctl_available = True

        class FuncModuleError(Exception):
            pass

        def get_bin_path(self, binary, required=False):
            if binary == 'sysctl':
                return '/sbin/sysctl'
            else:
                return None

        def run_command(self, cmd, check_rc=True, encoding=None):
            return (0, 'hw.ncpu: 4', None)

    fhw.module = ModuleMock()

    cpu_facts = fhw.get_cpu_facts()
    assert cpu_facts['processor_count'] == '4', 'Proc count not detected properly'


# Generated at 2022-06-13 00:46:56.276359
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    """Test FreeBSDHardware get dmi facts method."""
    # sys.path.append("../")  # run from ansible-invenotry-grapher/tests
    from ansible_inventory_grapher.hardware import FreeBSDHardware
    from ansible_inventory_grapher.constants import DMIDECODE_PATH
    from ansible_inventory_grapher.constants import DMIDECODE_DICT

    fhw = FreeBSDHardware()
    # Mock dmidecode path
    fhw.module.get_bin_path = lambda x: DMIDECODE_PATH

    assert fhw.get_dmi_facts() == DMIDECODE_DICT



# Generated at 2022-06-13 00:47:02.750198
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    class MyModule:
        def run_command(self, command, check_rc=True, encoding=None):
            out = b'kern.boottime: Mon Mar 19 08:08:58 2018\n'
            return 0, out, ''
    
    module = MyModule()
    bsd_hw = FreeBSDHardware(module)

    uptime_facts = bsd_hw.get_uptime_facts()
    assert uptime_facts == {'uptime_seconds': 1521444938}


# Generated at 2022-06-13 00:47:12.359171
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware
    # dmidecode output example

# Generated at 2022-06-13 00:47:13.902522
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    # TODO: unittest for freebsd_facts dmi facts
    module = None
    try:
        freebsdhardware = FreeBSDHardware(module)
    except:
        pass



# Generated at 2022-06-13 00:47:19.265665
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    module = AnsibleModule(
        argument_spec={},
    )
    hw = FreeBSDHardware(module=module)
    hw.populate()

    assert 'memfree_mb' in hw.facts
    assert 'memtotal_mb' in hw.facts
    assert 'swapfree_mb' in hw.facts
    assert 'swaptotal_mb' in hw.facts
    assert 'processor' in hw.facts
    assert 'processor_cores' in hw.facts
    assert 'processor_count' in hw.facts
    assert 'devices' in hw.facts



# Generated at 2022-06-13 00:47:22.425024
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    hw = FreeBSDHardware()
    assert hw.get_memory_facts() == {'memfree_mb': 11, 'memtotal_mb': 2, 'swapfree_mb': 0, 'swaptotal_mb': 1}

# Generated at 2022-06-13 00:47:32.887108
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    '''Unit test for method get_dmi_facts of class FreeBSDHardware

    uses mocked output from dmidecode, stored in a textfile
    '''

    from ansible.module_utils import basic

    def mocked_run_command(args):
        # return rc, stdout, stderr
        return 0, load_fixture('dmidecode'), ''

    # mock_dmidecode_data is textfile with mocked dmidecode output
    dmidecode_data = load_fixture('dmidecode')
    # mock_dmi_dict

# Generated at 2022-06-13 00:47:38.172204
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )
    har = FreeBSDHardware(module)
    out = har.get_cpu_facts()
    assert out['processor'].index('Intel(R) Core(TM) i5-4210U CPU @ 1.70GHz') >= 0
    assert out['processor_count'] == '8'



# Generated at 2022-06-13 00:47:48.737309
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    dmi_facts = {}
    dmi_facts['system_vendor'] = b'\xc3\x89cole Polytechnique F\xc3\xa9d\xc3\xa9rale de Lausanne (EPFL)'
    dmi_facts['board_asset_tag'] = b'To Be Filled By O.E.M.'
    dmi_facts['board_name'] = b'Z97X-UD3H-BK'
    dmi_facts['chassis_version'] = b'To Be Filled By O.E.M.'
    dmi_facts['chassis_serial'] = b'To Be Filled By O.E.M.'
    dmi_facts['chassis_asset_tag'] = b'To Be Filled By O.E.M.'

# Generated at 2022-06-13 00:48:03.558007
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    fixture = {
        'memtotal_mb': '1022',
        'memfree_mb': '72'
    }

    fact_class = FreeBSDHardware
    fact_instance = fact_class(dict())
    fact_instance.module = AnsibleModuleStub()
    fact_instance.module.run_command = run_command_stub
    fact = fact_instance.get_memory_facts()
    assert fact == fixture



# Generated at 2022-06-13 00:48:10.322878
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    '''Test FreeBSDHardware.populate() by creating a FreeBSDHardware object and
    call populate()
    '''
    from ansible.module_utils.facts import ModuleArgsParser
    from ansible.module_utils.facts.collector import BaseFactCollector
    module = AnsibleModuleMock()
    args = ModuleArgsParser.parse_kv({})
    base_collector = BaseFactCollector(module=module,
                                       collected_facts=dict(),
                                       args=args)
    freebsd_hardware_collector = FreeBSDHardwareCollector(base_collector)
    freebsd_hardware_collector._collect()



# Generated at 2022-06-13 00:48:20.390419
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    class FakeModule(object):
        def __init__(self):
            self.bin_path = {}
            self.bin_path['sysctl'] = '/usr/bin/sysctl'
        def get_bin_path(self, name):
            try:
                return self.bin_path[name]
            except KeyError:
                raise Exception("Binary %s not found." % name)
        def run_command(self, cmd, check_rc=True, encoding=None):
            if cmd == ['/usr/bin/sysctl', '-b', 'kern.boottime']:
                # Simulate kern.boottime returning a boot date that is
                # 40 days ago.
                return (0, struct.pack('@L', 40 * 24 * 3600), None)

# Generated at 2022-06-13 00:48:28.013221
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    from unittest import mock
    from calendar import timegm

    class MockFreeBSDHardware(FreeBSDHardware):
        platform = 'FreeBSD'

    class MockModule:
        def __init__(self):
            pass

        def get_bin_path(self, cmd, opt_dirs=[]):
            return '/bin/%s' % cmd

        def run_command(self, cmd, encoding=None, check_rc=True):
            return 0, 'kern.boottime: { sec = 1525283860, usec = 989476 } Fri May  4 10:51:00 2018\n', ''

    @mock.patch('ansible.module_utils.facts.hardware.freebsd.time.time')
    def run_test(time_mock):
        time_mock.return_value = 1525

# Generated at 2022-06-13 00:48:37.051810
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    module = AnsibleModuleMock()
    mod_utils = AnsibleModuleUtilsMock()

    # We create a mock module.run_command method to simulate
    # execution of sysctl, swapinfo and dmidecode binaries
    module.run_command = module_run_command

    hardware = FreeBSDHardware(module=module, module_utils=mod_utils)

    hardware_facts = hardware.populate()

    assert hardware_facts['uptime_seconds'] == 5654952
    assert hardware_facts['memtotal_mb'] == 4096
    assert hardware_facts['memfree_mb'] == 788
    assert hardware_facts['swaptotal_mb'] == 2096472
    assert hardware_facts['swapfree_mb'] == 2096472
    assert hardware_facts['processors'] == 1

# Generated at 2022-06-13 00:48:46.419619
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    module = AnsibleModule(argument_spec={})
    hardware = FreeBSDHardware(module=module)

    # Test that populate returns a dict
    fact_subset = hardware.populate()
    assert isinstance(fact_subset, dict)

    # Test that dict contains a list and a int
    assert 'processor' in fact_subset
    assert isinstance(fact_subset['processor'], list)
    assert 'processor_count' in fact_subset
    assert isinstance(fact_subset['processor_count'], int)
    assert 'memtotal_mb' in fact_subset
    assert isinstance(fact_subset['memtotal_mb'], int)
    assert 'memfree_mb' in fact_subset
    assert isinstance(fact_subset['memfree_mb'], int)

# Generated at 2022-06-13 00:48:59.877877
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    module_mock = AnsibleModule(
        argument_spec=dict()
    )

# Generated at 2022-06-13 00:49:07.562816
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware
    from ansible.module_utils.facts.utils import Collector
    from ansible.module_utils.facts.utils.timeout import TimeoutError

    bsd_hw = FreeBSDHardware({'module_setup': True})


# Generated at 2022-06-13 00:49:16.368949
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    module = AnsibleModule(argument_spec={})
    hardware_collector = FreeBSDHardwareCollector(module=module, timeout=10)
    hardware = hardware_collector.collect()[0]
    dmi_facts = hardware.get_dmi_facts()
    for dmi_fact in dmi_facts:
        assert dmi_facts[dmi_fact] != 'NA'

    cpu_facts = hardware.get_cpu_facts()
    assert cpu_facts['processor_count'] != ''
    assert len(cpu_facts['processor']) == 1

    memory_facts = hardware.get_memory_facts()
    assert memory_facts['memfree_mb'] != ''
    assert memory_facts['memtotal_mb'] != ''

    uptime_facts = hardware.get_uptime_facts()

# Generated at 2022-06-13 00:49:23.470702
# Unit test for method get_device_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_device_facts():
    import pytest
    import ansible.module_utils.facts.hardware.freebsd as freebsd_hw_module
    import os

    class TestModule(object):
        def __init__(self):
            self.exit_json = None
            self.fail_json = None

        def get_bin_path(self, arg, required=False, opt_dirs=[]):
            return '/sbin/sysctl'


# Generated at 2022-06-13 00:49:43.182320
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    with open('./ansible_test/test_units/test_units.json') as data:
        testdata = json.load(data)
    test_obj = FreeBSDHardware(module=None)
    failures = 0
    for data in testdata:
        if data['method'] == 'get_memory_facts': 
            if test_obj.get_memory_facts() != data['outcome']:
                failures += 1
    if failures == 0:
        print("Unit test for get_memory_facts of class FreeBSDHardware succesful")
    else:
        print("Unit test for get_memory_facts of class FreeBSDHardware unsuccesful")

# Generated at 2022-06-13 00:49:53.717631
# Unit test for method get_cpu_facts of class FreeBSDHardware

# Generated at 2022-06-13 00:50:01.198306
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    from ansible.module_utils.facts.collector import get_collector
    from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware
    from ansible.module_utils.facts.hardware.base import HardwareCollector

    class FakeModule():
        def __init__(self):
            self.params = {}
            self.exit_json = lambda *a, **b: None

        def get_bin_path(self, *args, **kwargs):
            return "fake_path"

        def run_command(self, *args, **kwargs):
            return 0, "fake_result", "fake_error"

    module = FakeModule()

    # test with empty result
    hardware_collector = get_collector('hardware', module=module)
    assert FreeBSDHardwareCollector in hardware_collector

# Generated at 2022-06-13 00:50:08.125082
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    mock_module = MockModule()
    hardware = FreeBSDHardware(module=mock_module)
    debugger = pudb.set_trace
    mock_module.run_command.return_value = (0, "4", "")
    cpu_facts = hardware.get_cpu_facts()
    assert cpu_facts['processor_count'] == "4"
    assert len(cpu_facts['processor']) == 4
    assert cpu_facts['processor_cores'] == "2"


# Generated at 2022-06-13 00:50:17.178277
# Unit test for method get_dmi_facts of class FreeBSDHardware

# Generated at 2022-06-13 00:50:24.318258
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    class Options(object):
        def __init__(self):
            self.bin_path = os.environ.get('PATH', '')

    class HardwareModule(object):
        def __init__(self):
            self.options = Options()

        def get_bin_path(self, executable, required=False):
            return self.options.bin_path

        def run_command(self, cmd, encoding=None, check_rc=True,
                        close_fds=True, executable=None, data=None):
            expected_bytes = struct.pack(struct.Struct('@L').format,
                                         int(time.time()))
            return 0, expected_bytes, ''

    class TestFreeBSDHardware(FreeBSDHardware):
        def __init__(self):
            self.module = HardwareModule()


# Generated at 2022-06-13 00:50:33.106814
# Unit test for method get_dmi_facts of class FreeBSDHardware

# Generated at 2022-06-13 00:50:40.746612
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    from ansible.module_utils.facts.utils import collect_subset
    from ansible.module_utils.facts import ModuleFacts

    def run_module():
        module_args = dict()
        result = dict(
            ansible_facts=dict(
                hardware=dict(),
            ),
            changed=False,
        )
        module = ModuleFacts(
            argument_spec=module_args,
            supports_check_mode=False,
            facts_module=False
        )

        with collect_subset(['hardware']) as facts:
            res = module.run()
            result['ansible_facts'] = res['ansible_facts']
            result['changed'] = res['changed']
        return result

    result = run_module()

# Generated at 2022-06-13 00:50:50.259018
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    test_module = type('test', (), {})()
    test_module.params = {}
    test_module.run_command = lambda self, _, check_rc=False: (0, 'hw.ncpu: 4', '')
    test_module.get_bin_path = lambda self, _: None

    fbsd_hw = FreeBSDHardware(test_module)
    fbsd_hw.populate()

    assert fbsd_hw.facts['processor_count'] == 4



# Generated at 2022-06-13 00:50:50.853939
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    x = FreeBSDHardwareCollector()
    print(x)

# Generated at 2022-06-13 00:51:07.739043
# Unit test for method populate of class FreeBSDHardware

# Generated at 2022-06-13 00:51:13.252870
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    out = 'hw.ncpu: 4\n'
    fb = FreeBSDHardware({'run_command': lambda x: (0, out, '')})
    cpu_facts = fb.get_cpu_facts()
    assert cpu_facts['processor_count'] == '4'



# Generated at 2022-06-13 00:51:23.971477
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    class TestModule():
        def __init__(self, rc, out, err):
            self.rc = rc
            self.out = out
            self.err = err

        def get_bin_path(self, name, required=False):
            return '/bin/true'

        def run_command(self, cmd, encoding=None, check_rc=True):
            return self.rc, self.out, self.err

    # Invoke the function with a valid buffer.
    # The value must be a kern.boottime buffer as described in sysctl(3).
    tm = TestModule(0, b'\x4c\xad\xcd\x00\x38\xc4\x01\x00', '')
    h = FreeBSDHardware()

    h.module = tm
    result = h.get_upt

# Generated at 2022-06-13 00:51:29.843427
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    m = FreeBSDHardwareCollector()
    facts = m.collect(None, None)

    # Tests for get_cpu_facts of class FreeBSDHardware
    assert len(facts['processor']) > 0
    assert facts['processor_cores'] >= 0
    assert facts['processor_count'] >= 0

    # Tests for get_memory_facts of class FreeBSDHardware
    assert facts['memtotal_mb'] >= 0
    assert facts['memfree_mb'] >= 0
    assert facts['swaptotal_mb'] >= 0
    assert facts['swapfree_mb'] >= 0

    # Tests for get_uptime_facts of class FreeBSDHardware
    assert facts['uptime_seconds'] >= 0

    # Tests for get_dmi_facts of class FreeBSDHardware

# Generated at 2022-06-13 00:51:30.481016
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    pass

# Generated at 2022-06-13 00:51:40.311109
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    # Prepare the mocks
    class ModuleMock:
        def __init__(self):
            self.run_command_return_value = (0, '', '')
            self.run_command_arg = None

        def get_bin_path(self, name, opt_dirs=[]):
            return '/bin/%s' % name

        def run_command(self, args, check_rc=False, encoding=None):
            self.run_command_arg = args
            return self.run_command_return_value

    class ArgsMock:
        def __init__(self):
            self.timeout = 30

    class FactsMock:
        def __init__(self):
            self.__cache = {}

        def __getitem__(self, key):
            return self.__cache[key]

       

# Generated at 2022-06-13 00:51:48.938317
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    t = FreeBSDHardware()
    t.module.exit_json = lambda x: x
    
    out = '2'
    t.module.run_command = lambda cmd, check_rc=False: (0, out, '')
    cpu_facts = t.get_cpu_facts()
    assert cpu_facts['processor_count'] == out
    assert cpu_facts['processor'] == []

    out = 'CPU:\s+AMD64'
    t.module.run_command = lambda cmd, check_rc=False: (0, out, '')
    cpu_facts = t.get_cpu_facts()
    assert cpu_facts['processor_count'] == '2'
    assert cpu_facts['processor'] == ['AMD64']

    out = 'CPU:\s+AMD64, Logical CPUs per core: 1'
    t.module

# Generated at 2022-06-13 00:51:56.349265
# Unit test for method get_cpu_facts of class FreeBSDHardware

# Generated at 2022-06-13 00:52:01.196199
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():

    hw = FreeBSDHardware()
    cpu_facts = hw.get_cpu_facts()
    assert cpu_facts['processor_count'] is not None
    assert cpu_facts['processor_cores'] is not None
    assert len(cpu_facts['processor']) > 0



# Generated at 2022-06-13 00:52:09.293029
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    hw = FreeBSDHardware({'ansible_facts': {}})
    hw.populate()
    assert 'memfree_mb' in hw.facts
    assert 'memtotal_mb' in hw.facts
    assert 'swapfree_mb' in hw.facts
    assert 'swaptotal_mb' in hw.facts
    assert 'processor' in hw.facts
    assert 'processor_cores' in hw.facts
    assert 'processor_count' in hw.facts
    assert 'devices' in hw.facts
    assert 'uptime_seconds' in hw.facts
    assert 'mounts' in hw.facts



# Generated at 2022-06-13 00:52:50.900923
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    import unittest

    class TestFreeBSDHardware(unittest.TestCase):
        def setup(self):
            self.freebsd_hardware = FreeBSDHardware()

        def test_get_memory_facts_swap_info(self):
            memory_facts = {}
            memory_facts['swaptotal_mb'] = 1024
            memory_facts['swapfree_mb'] = 512
            self.freebsd_hardware.module.run_command = lambda x: (0, 'Device          1M-blocks     Used    Avail Capacity\n/dev/ada0p3        1024        512    512   50%\n', '')
            self.assertEqual(self.freebsd_hardware.get_memory_facts(), memory_facts)
            memory_facts['swaptotal_mb'] = None
            memory_facts

# Generated at 2022-06-13 00:53:02.226782
# Unit test for method get_dmi_facts of class FreeBSDHardware

# Generated at 2022-06-13 00:53:10.769950
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    import tempfile
    import shutil

    class module_mock:
        def get_bin_path(self, module):
            return 'sysctl'

        def run_command(self, command, encoding=None, check_rc=None):
            if command != 'sysctl -b kern.boottime':
                return (1, '', '')
            return (0, b'\x00\x00\x00\x00\x00\x00\x00\x00', '')

    class hardware_mock(FreeBSDHardware):
        def __init__(self):
            self.module = module_mock()

    hw = hardware_mock()
    uptime_facts = hw.get_uptime_facts()

    assert type(uptime_facts) is dict
    assert 'uptime_seconds'

# Generated at 2022-06-13 00:53:13.308748
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    import pytest
    from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware

    freebsd_machine = FreeBSDHardware()
    freebsd_machine._module = None
    freebsd_machine._module = None
    freebsd_machine.get_cpu_facts()



# Generated at 2022-06-13 00:53:17.937585
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    module = AnsibleModule(argument_spec={})
    module.get_bin_path = Mock(return_value='')
    hardware = FreeBSDHardware(module)
    mock = Mock(return_value=('', '1\n', ''))
    with patch.object(hardware.module, 'run_command', mock):
        memory_facts = hardware.get_memory_facts()
    assert memory_facts['memtotal_mb'] == '1'



# Generated at 2022-06-13 00:53:28.633476
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    module = FakeAnsibleModule()
    hardware = FreeBSDHardware(module)

    module.get_bin_path.return_value = '/usr/sbin/dmidecode'

    # No dmidecode binary
    module.get_bin_path.return_value = False
    module.run_command.return_value = (1, None, None)

    facts = hardware.get_dmi_facts()
    module.fail_json.assert_called_with(
        msg='Failed to get dmi facts from binary dmidecode',
        rc=1,
        stdout=None,
        stderr=None
    )

    # Valid dmidecode binary with --string-type option
    module.get_bin_path.return_value = '/usr/sbin/dmidecode'
    module.run_command

# Generated at 2022-06-13 00:53:32.382089
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    module = FakeModule()
    hardware = FreeBSDHardware(module)
    hardware.populate()


# Generated at 2022-06-13 00:53:35.136581
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    from ansible.module_utils.facts import ModuleArgs, Facts
    modargs = ModuleArgs({})
    facts = Facts(module_args=modargs)
    hardware = FreeBSDHardware(facts, modargs)
    mem_facts = hardware.get_memory_facts()
    assert 'memfree_mb' in mem_facts
    assert 'memtotal_mb' in mem_facts
    assert 'swapfree_mb' in mem_facts
    assert 'swaptotal_mb' in mem_facts

# Generated at 2022-06-13 00:53:40.474633
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    import platform
    import sys
    sys.platform = 'FreeBSD'
    platform.system = lambda: 'Darwin'
    f = FreeBSDHardwareCollector()
    assert isinstance(f, FreeBSDHardwareCollector)
    assert hasattr(f, '_fact_class')
    assert hasattr(f, '_platform')
    assert f._fact_class.platform == 'FreeBSD'
    assert f._platform == 'FreeBSD'


# Generated at 2022-06-13 00:53:46.869855
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    import sys
    import unittest
    from unittest.mock import Mock
    sys.modules['ansible'] = Mock()
    import ansible.module_utils
