

# Generated at 2022-06-13 01:06:31.517285
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    hardware = SunOSHardware()

    hardware.module.run_command = run_command
    hardware.module.get_bin_path = get_bin_path
    facts = hardware.populate()
    assert facts['memtotal_mb'] == 500


# Generated at 2022-06-13 01:06:43.329748
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    class MockModule(object):
        def __init__(self, **kwargs):
            self.facts = {}


# Generated at 2022-06-13 01:06:47.236826
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    from ansible.module_utils.facts.hardware.sunos import SunOSHardware

    sun_hw = SunOSHardware(dict())
    facts = sun_hw.get_memory_facts()
    assert facts['memtotal_mb'] > 0

# Generated at 2022-06-13 01:06:58.149091
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    # setup
    class TestSunOsHardware(SunOSHardware):
        def __init__(self, module):
            self.module = module

    def mock_run_command(path, environ):
        if '/usr/bin/uname' in path:
            return None, 'i86pc', ''
        elif ('/usr/platform/i86pc/sbin/prtdiag' in path
              or '/usr/platform/i86pc/sbin/prtdiag' in path):
            return 0, """System Configuration: VMware, Inc. VMware Virtual Platform
BIOS Configuration: Phoenix Technologies LTD 6.00 09/13/2012
""", ''

    class TestModule:
        def __init__(self):
            self.run_command = mock_run_command
            self.params = {}
            self.check_mode = False

# Generated at 2022-06-13 01:07:10.893285
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    """
    Test module for memomry facts of class SunOSHardwareCollector
    :return: void
    """
    import module_utils.facts.hardware.sunos as sunos_hw_utils

    hw_utils = sunos_hw_utils.SunOSHardwareCollector()
    hw_obj = hw_utils._fact_class()
    hw_obj.module = MagicMock()
    hw_obj.module.run_command.side_effect = [
        [0, "/usr/sbin/prtconf: Memory size: 16384 Megabytes\n", ""],
        [0, "/usr/sbin/swap -s:    total:    4091920k bytes allocated +  9194108k reserved  = 13286028k used, 29663480k available\n", ""]
    ]
   

# Generated at 2022-06-13 01:07:22.657266
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    HardwareCollector.collectors['SunOS'] = SunOSHardwareCollector
    facts = {}
    facts['platform'] = 'SunOS'
    harware = SunOSHardware(facts, {})
    result = harware.populate()
    assert 'processor' in result
    assert 'memtotal_mb' in result
    assert 'swapfree_mb' in result
    assert 'swaptotal_mb' in result
    assert 'swap_allocated_mb' in result
    assert 'swap_reserved_mb' in result
    assert 'system_vendor' in result
    assert 'product_name' in result
    assert 'mounts' in result
    assert 'devices' in result
    assert 'uptime_seconds' in result

# Generated at 2022-06-13 01:07:33.630606
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    from units.compat import unittest
    from units.compat.mock import Mock, patch

    import os
    #import sys
    #sys.path.append(os.path.dirname(__file__))
    #print (os.curdir)
    #print (os.path.dirname(os.path.abspath(__file__)))

    import os.path
    #print (os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))
    #print (os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', '..'))
    #print (os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', '

# Generated at 2022-06-13 01:07:44.342300
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    retrieved_facts = {'ansible_machine': 'i86pc',
                       'ansible_processor': ['Intel(R) Core(TM)2 Duo CPU     E6550  @ 2.33GHz']}
    module = AnsibleModuleMock()
    module.run_command = run_command_mock

    # Normal case
    prtdiag_output = 'System Configuration: Oracle Corporation sun4v SPARC T5220'
    hw = SunOSHardware(module)
    hw.get_dmi_facts()

    # Check for system vendor name
    assert hw.facts['system_vendor'] == 'Oracle Corporation'

    # Check for product
    assert hw.facts['product_name'] == 'sun4v SPARC T5220'



# Generated at 2022-06-13 01:07:51.235002
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    """This is a unit test for method get_device_facts of class SunOSHardware
    """
    # Test case to assert two dictionaries are equal
    def assert_dict_equal(dict_a, dict_b):
        # get the dict keys and sort them. this is done because
        # dict_a and dict_b may have keys that are out of order,
        # but the values are still the same
        dict_a_key_set = set(dict_a.keys())
        dict_b_key_set = set(dict_b.keys())
        dict_a_keys = sorted(dict_a_key_set)
        dict_b_keys = sorted(dict_b_key_set)
        assert (dict_a_key_set == dict_b_key_set), "dictionaries do not have the same keys"



# Generated at 2022-06-13 01:07:59.774436
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    def _collect_kstat():
        return '''module: cpu_info
class: misc
instance: 0
chip_id   0
core_id   0
clock_MHz 1000
implementation     sparc
brand     sparcv9
"""
'''

    hardware = SunOSHardware(dict(), run_command=lambda x, y: [0, _collect_kstat(), ''])
    cpu_facts = hardware.get_cpu_facts()
    assert cpu_facts['processor_count'] == 1
    assert cpu_facts['processor_cores'] == 1
    assert cpu_facts['processor'] == ['sparcv9 @ 1000MHz']

# Generated at 2022-06-13 01:08:23.771721
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    module = AnsibleModuleMock()
    SunOSHardware_object = SunOSHardware(module, {'platform': 'SunOS'})
    setattr(SunOSHardware_object, '_device_facts', {'sd': {'product': '', 'revision': '', 'serial': '', 'size': '', 'vendor': '', 'hard_errors': '', 'soft_errors': '', 'transport_errors': '', 'media_errors': '', 'predictive_failure_analysis': '', 'illegal_request': ''}})

    # Method get_device_facts of class SunOSHardware is called
    device_facts = SunOSHardware_object.get_device_facts()

    assert device_facts.get('devices').get('sd').get('product') == 'VB0ad2ec4d-074a'



# Generated at 2022-06-13 01:08:36.105271
# Unit test for method get_memory_facts of class SunOSHardware

# Generated at 2022-06-13 01:08:39.619087
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    m = type('module', (object,), {'run_command': run_command})()
    h = SunOSHardware(m)
    m.run_command.side_effect = [[0, prtdiag_output, 0]]

    assert h.get_dmi_facts() == {'system_vendor': 'Oracle Corporation', 'product_name': 'SUN FIRE X4170 M2 Server'}



# Generated at 2022-06-13 01:08:42.537122
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    module = FakeAnsibleModule()

    hardware = SunOSHardware()
    hardware.set_module(module)

    dmi_facts = hardware.get_dmi_facts()
    assert dmi_facts['system_vendor'] == 'Sun Microsystems'
    assert dmi_facts['product_name'] == 'Sun Fire V440'



# Generated at 2022-06-13 01:08:51.952203
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    m = SunOSHardware({'module_setup': True, 'command_warnings': []})
    rc, out, err = m.module.run_command('/usr/bin/kstat -p unix:0:system_misc:ncpus')
    ncpus = out.split('\t')[1].rstrip()

    m.module.run_command.return_value = 0, kstat_cpu_info(int(ncpus)), ''
    cpu_facts = m.get_cpu_facts()

    assert cpu_facts['processor_count'] == int(ncpus)



# Generated at 2022-06-13 01:08:59.301695
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    module = SunOSHardware()

    # test with absent of 'ansible_machine'
    collected_facts = {}
    cpu_facts = module.get_cpu_facts(collected_facts)

    assert (cpu_facts['processor_count'] == 4)
    assert (cpu_facts['processor_cores'] == 4)
    assert (len(cpu_facts['processor']) == 4)
    assert (cpu_facts['processor'][0].startswith('Intel'))

    # test with present of 'ansible_machine'
    collected_facts = {'ansible_machine': 'i86pc'}
    cpu_facts = module.get_cpu_facts(collected_facts)

    assert (cpu_facts['processor_count'] == 4)
    assert (cpu_facts['processor_cores'] == 4)

# Generated at 2022-06-13 01:09:05.763285
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    from ansible.module_utils.facts.collector import FactsCollector

    fact_collector = FactsCollector()
    hardware = SunOSHardware(fact_collector)

    # Test the configuration where the product_name can be found
    prtdiag_output = """\
System Configuration: Oracle Corporation sun4v
Sun Fire T2000
   System clock frequency: 1000 MHz
"""
    with open('/etc/mnttab', 'w') as f:
        f.write('/dev/dsk/c0t0d0s0 /dev/rdsk/c0t0d0s0 ufs rw,intr,largefiles,logging,xattr,onerror=panic,dev=70001404 47835240');
    hardware.module = AnsibleModule(argument_spec={})

# Generated at 2022-06-13 01:09:15.422131
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    from ansible.module_utils.facts.utils import timeout
    from ansible.module_utils.facts.hardware.sunos import SunOSHardware

    class task:
        def __init__(self):
            self.tmpdir = 'tmpdir'
            self.warn_only = True
            self.register = dict()
            self.run_command = self._run_command
            self.get_bin_path = self._get_bin_path

        def _get_bin_path(self, cmd, opt_dirs=[]):
            return cmd

        def _run_command(self, cmd, check_rc=True, environ_update=None):
            return (0, 'unix:0:system_misc:boot_time 1548249689', '')


# Generated at 2022-06-13 01:09:28.401234
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    '''
    Unit tests for method get_dmi_facts of class SunOSHardware
    '''
    from ansible.module_utils.facts.hardware.sunos import SunOSHardware

    test_cases = [
        {
            'expected_output': {'system_vendor': 'Sun Microsystems', 'product_name': 'SUNW,Sun-Fire-V440'},
            'input_value': '''
System Configuration: Sun Microsystems  SUNW,Sun-Fire-V440
System clock frequency: 1200 MHz
Memory size: 4096 Megabytes
'''
        }
    ]

    sunoshardware = SunOSHardware()


# Generated at 2022-06-13 01:09:37.447151
# Unit test for method get_dmi_facts of class SunOSHardware

# Generated at 2022-06-13 01:10:14.193161
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    # Test SunOSHardware
    sunos = SunOSHardware()
    uptime_facts = {'uptime_seconds': 1548249689}
    test = sunos.get_uptime_facts()
    assert test == uptime_facts, "get_uptime_facts returned %s, expected %s" % (test, uptime_facts)

# Generated at 2022-06-13 01:10:19.220225
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    # prepare the test
    module = AnsibleModule(argument_spec={})
    # Dict with expected results
    expected = {
        "processor_cores": 2,
        "processor_count": 2,
        "processor": ["SPARC64-VII (chipid 0, clock 1200 MHz)", "SPARC64-VII (chipid 0, clock 1200 MHz)"],
    }
    # test method get_cpu_facts
    m = SunOSHardware()
    result = m.get_cpu_facts()
    assert result == expected

# Generated at 2022-06-13 01:10:30.707529
# Unit test for method get_cpu_facts of class SunOSHardware

# Generated at 2022-06-13 01:10:40.801008
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():

    class ModuleStub():

        def __init__(self, out, rc=0):
            self.rc = rc
            self.out = out

        def run_command(self, cmd, lan_env=False):
            return self.rc, self.out, ""

    class SunOSHardwareStub():

        def __init__(self, out, rc=0):
            self.module = ModuleStub(out, rc)


# Generated at 2022-06-13 01:10:43.870206
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    module = AnsibleModuleMock()
    hardware = SunOSHardware(module, 'SunOS')
    # mock the output of command "prtconf"
    hardware.module.run_command.return_value = (0, 'Memory size: 8192 Megabytes', '')

    facts = hardware.get_memory_facts()

    assert facts['memtotal_mb'] == 8192

# Generated at 2022-06-13 01:10:55.082730
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    import sys
    import os
    current_path = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.join(current_path, '../../'))
    from ansible.module_utils.facts.hardware.sunos import SunOSHardware

    sunoshardware = SunOSHardware()

    # test with prtdiag output

# Generated at 2022-06-13 01:11:02.064734
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    from units.modules.utils import AnsibleExitJson, AnsibleFailJson, ModuleTestCase, set_module_args
    module = AnsibleExitJson()
    set_module_args(dict(gather_subset='!all'))
    obj = SunOSHardware(module)
    res = obj.populate()
    assert 'memtotal_mb' in res
    assert 'memfree_mb' in res
    assert 'swaptotal_mb' in res
    assert 'swapfree_mb' in res


# Generated at 2022-06-13 01:11:04.440364
# Unit test for constructor of class SunOSHardwareCollector
def test_SunOSHardwareCollector():
    collector = SunOSHardwareCollector()
    assert collector.required_facts == {'platform'}
    assert collector.platform == 'SunOS'


# Generated at 2022-06-13 01:11:13.214436
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    module = type('AnsibleModule', (object,), dict(
        run_command=lambda *a, **kw: (0, "Memory size: 256 Megabytes", ''),
        get_bin_path=lambda *a, **kw: '/usr/sbin/prtconf',
        params=dict()
    ))
    harware = SunOSHardware(module)
    assert harware.get_memory_facts() == {'memtotal_mb': 256}
    harware.module.run_command = lambda *a, **kw: (1, '', 'Error:')
    assert harware.get_memory_facts() == {}



# Generated at 2022-06-13 01:11:19.978069
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    test_lines = '''module: sparcv9
cpu_type: sparcv9
ncpu: 1
implementation: sparc
brand: SUNW,SPARC-Enterprise
clock_MHz: 2000
chip_id: 0
core_id: 0
state: on-line
chip_id: 0
core_id: 1
state: on-line'''

    test_hardware_fact = SunOSHardware()

    cpu_facts = test_hardware_fact.get_cpu_facts()

    assert len(cpu_facts) == 4
    assert cpu_facts['processor'] == ['sparcv9 @ 2000MHz']
    assert cpu_facts['processor_count'] == 1
    assert cpu_facts['processor_cores'] == 2


# Generated at 2022-06-13 01:12:29.177360
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    from ansible.module_utils.facts import facts

    obj = facts.SunOSHardware()
    memory_facts = obj.get_memory_facts()
    assert 'memtotal_mb' in memory_facts



# Generated at 2022-06-13 01:12:37.239346
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    """
    This function tests the get_dmi_facts method of the SunOSHardware Class.
    """

    # Define a test class and create a class instance
    class Test():
        """
        This class is used to provide mock methods for get_dmi_facts method.
        """
        def __init__(self, module):
            self.module = module
            self.run_command = self.real_run_command

        def real_run_command(self, cmd):
            """
            This method is used to provide the real implementation of run_command.
            :param cmd: The command that is given as input.
            :return: rc:  The return code of the command.
                     out: The standard output string.
                     err: The error string.
            """

# Generated at 2022-06-13 01:12:48.630028
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    """
    Validate uptime facts on Solaris 8/9
    """

    cmd_output = """unix:0:system_misc:boot_time    1548249689"""
    expected_uptime_facts = {'uptime_seconds': 1067289}

    facts_object = SunOSHardware()
    time_mock = lambda: 1548349689
    time_mock_method = Mock(return_value=time_mock())
    time_mock_object = Mock()
    time_mock_object.time = time_mock_method
    facts_object.time = time_mock_object
    run_command_mock_object = Mock()
    run_command_mock_object.return_value = (0, cmd_output, '')
    facts_object.module.run_command = run_

# Generated at 2022-06-13 01:12:54.181121
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    module = AnsibleModule(argument_spec={})
    fact_collector = SunOSHardware(module=module)

    memory_facts = fact_collector.get_memory_facts()

    # Both swapfree_mb and swaptotal_mb should be present
    assert 'swapfree_mb' in memory_facts
    assert 'swaptotal_mb' in memory_facts
    assert 'memtotal_mb' in memory_facts



# Generated at 2022-06-13 01:13:01.441212
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    cpu_facts = {'processor': ['SUNW,UltraSPARC-II @ 250MHz']}
    module = MagicMock()
    out = 'module: SUNW,UltraSPARC-II  clock_MHz: 250  chip_id: 0  impl_id: 2  board_id: 0  cpu_address_size: 32  cpu_id: 8  cpu_type: 150\nmodule: SUNW,UltraSPARC-II  clock_MHz: 250  chip_id: 0  impl_id: 2  board_id: 0  cpu_address_size: 32  cpu_id: 8  cpu_type: 150\n'
    module.run_command.return_value = [
        0, out, 'Some error']
    sunOSHardware = SunOSHardware()
    assert cpu_facts == sunOSHardware.get_cpu_facts

# Generated at 2022-06-13 01:13:11.599387
# Unit test for method get_cpu_facts of class SunOSHardware

# Generated at 2022-06-13 01:13:14.763411
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    module = AnsibleModule(argument_spec={})
    obj = SunOSHardware(module)
    rc, out, err = module.run_command('uname -s')
    assert rc == 0 and out == 'SunOS\n'

# Generated at 2022-06-13 01:13:22.521844
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    hardware = SunOSHardware(dict())

    prtdiag_sample_output = """
System Configuration: VMware, Inc. VMware Virtual Platform
Sun Microsystems sun4v
System clock frequency: 1000 MHz
Memory size: 4096 Megabytes
===============================================================================
   Processor   Processor  Processor  Processor
      ID       Implementor     Architecture      Frequency
-------------------------------------------------------------------------------
       0                         SPARC64-V        1000 MHz
       1                         SPARC64-V        1000 MHz
"""
    rc, out, err = hardware.module.run_command.return_value = (0, prtdiag_sample_output, '')

    dmi_facts = hardware.get_dmi_facts()

    hardware.module.run_command.assert_called_with('/usr/bin/prtdiag')

# Generated at 2022-06-13 01:13:30.070166
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    test_obj = SunOSHardware()

    test_obj.module = MagicMock()
    test_obj.module.run_command.return_value = (0, 'System Configuration: Oracle Corporation sun4u', '')

    assert test_obj.get_dmi_facts() == {'system_vendor': 'Oracle Corporation', 'product_name': 'sun4u'}
    test_obj.module.run_command.assert_called_once_with('/usr/bin/uname -i')

# Generated at 2022-06-13 01:13:31.723260
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    h = SunOSHardware._get_uptime_facts()
    assert 'uptime_seconds' in h