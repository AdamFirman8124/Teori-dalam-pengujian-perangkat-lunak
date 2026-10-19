

# Generated at 2022-06-13 01:06:30.930740
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    module = AnsibleModuleMock()
    module.run_command = module_run_command
    sunos_hardware = SunOSHardware(module)
    res = sunos_hardware.get_dmi_facts()
    assert res['system_vendor'] == 'Oracle Corporation'
    assert res['product_name'] == 'SUNW,SPARC-Enterprise-T5120'

# Mock module

# Generated at 2022-06-13 01:06:38.003767
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    module = MockModule()
    hardware_facts = SunOSHardware(module)

    setattr(module, 'run_command', mock_run_command)

    uptime_facts = hardware_facts.get_uptime_facts()

    print("uptime_seconds is: %s" % uptime_facts['uptime_seconds'])

    uptime_seconds = int(time.time() - 1548249689)
    assert uptime_facts['uptime_seconds'] == uptime_seconds



# Generated at 2022-06-13 01:06:50.251564
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    class FakeModule(object):
        def run_command(self, args, **kwargs):
            return 0, demo_output, None

    device_facts = {}
    device_facts['devices'] = {}


# Generated at 2022-06-13 01:07:00.377329
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    module = AnsibleModule(argument_spec={})
    setattr(module, 'run_command', run_command)
    test_hw = SunOSHardware(module)
    result = test_hw.get_device_facts()
    assert 'devices' in result
    assert len(result['devices']) == 2
    assert 'sd0' in result['devices']
    assert 'sd1' in result['devices']

    assert result['devices']['sd0']['hard_errors'] == 0
    assert result['devices']['sd0']['predictive_failure_analysis'] == 0
    assert result['devices']['sd0']['illegal_request'] == 6
    assert result['devices']['sd0']['product'] == 'VBOX HARDDISK'

# Generated at 2022-06-13 01:07:04.978287
# Unit test for constructor of class SunOSHardwareCollector
def test_SunOSHardwareCollector():
    # Create a new SunOSHardwareCollector object
    hardware_collector = SunOSHardwareCollector()

    # Check if its a HardwareCollector
    assert isinstance(hardware_collector, HardwareCollector)

# Generated at 2022-06-13 01:07:12.994530
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    from ansible.module_utils.six import StringIO
    import datetime
    m = SunOSHardware()
    m.module = type("AnsibleModule", (object,), {"run_command": lambda self, x: (0, StringIO(x[0]), "")})()

    old_time = int(time.time())
    out = int(time.time() + datetime.timedelta(seconds=15).total_seconds())
    uptime_facts = m.get_uptime_facts()
    assert uptime_facts['uptime_seconds'] == out-old_time

# Generated at 2022-06-13 01:07:24.374546
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    module = None
    prtconf = """
Memory size: 16384 Megabytes
"""

    swap_cmd = """
swap_size:       32760k bytes allocated + 4544k reserved = 37304k
"""
    sun_facts = SunOSHardware(module)
    get_memory_facts = sun_facts.get_memory_facts()

    assert get_memory_facts['memtotal_mb'] == 16384
    assert get_memory_facts['swapfree_mb'] == 36
    assert get_memory_facts['swaptotal_mb'] == 36
    assert get_memory_facts['swap_allocated_mb'] == 32
    assert get_memory_facts['swap_reserved_mb'] == 4

# Generated at 2022-06-13 01:07:34.808641
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    class SunOSHardwareTest(SunOSHardware):
        def __init__(self, module):
            self.module = module

    class AnsibleModuleMock:
        run_command = None

        def __init__(self, run_command):
            self.run_command = run_command

    # Example output of: /usr/bin/kstat -p sderr:::Vendor sderr:::Size sderr:::Hard Errors sderr:::Soft Errors sderr:::Transport Errors sderr:::Media Error sderr:::Predictive Failure Analysis sderr:::Illegal Request
    # sderr:0:sd0,err:Hard Errors     0
    # sderr:0:sd0,err:Illegal Request 6
    # sderr:0:sd0,err:Media Error     0

# Generated at 2022-06-13 01:07:45.267851
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    module = AnsibleModule(argument_spec={})

    out = """Memory size: 16384 Megabytes"""
    module.run_command = MagicMock(return_value=(0, out, ""))

    out = """total: 13975396k bytes allocated + 101608k reser
    ved  = 13985500k used, 51238864k available"""
    module.run_command = MagicMock(return_value=(0, out, ""))

    hardware = SunOSHardware(module)
    facts = hardware.get_memory_facts()

    assert facts['swaptotal_mb'] == 6719
    assert facts['swapfree_mb'] == 24947
    assert facts['swap_reserved_mb'] == 4
    assert facts['swap_allocated_mb'] == 13983
    assert facts['memtotal_mb']

# Generated at 2022-06-13 01:07:51.611825
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    module = AnsibleModuleMock()
    sun_hw = SunOSHardware(module)
    module.run_command_environ_update = {'LANG': 'C', 'LC_ALL': 'C', 'LC_NUMERIC': 'C'}
    sun_hw.populate()
    assert sun_hw.cpu['processor'] == ['SUNW,UltraSPARC-IIi @ 167MHz']
    assert sun_hw.memory['memtotal_mb'] == 4096
    assert sun_hw.memory['swapfree_mb'] == 0
    assert sun_hw.memory['swaptotal_mb'] == 28
    assert sun_hw.memory['swap_allocated_mb'] == 28
    assert sun_hw.memory['swap_reserved'] == 28

# Generated at 2022-06-13 01:08:16.901466
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    import sys
    import tempfile
    import shutil
    import os
    from ansible_collections.ansible.community.plugins.module_utils import basic

    test_dir = tempfile.mkdtemp()


# Generated at 2022-06-13 01:08:28.057605
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    class ModuleMock(object):
        def __init__(self):
            self.params = {}
            self.run_command_environ_update = {}

        def get_bin_path(self, arg, opt_dirs=[]):
            return "/usr/bin/prtdiag"

        def run_command(self, cmd, environ_update=None, check_rc=True):
            rc = 0
            out = ''
            err = ''
            if cmd[0] == 'uname':
                out = 'i86pc'

# Generated at 2022-06-13 01:08:37.370493
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    module = MockModule({})
    sunos_hardware = SunOSHardware(module)
    sunos_hardware.get_memory_facts()

    assert module.run_command.call_count == 2
    # Assert prtconf command called
    assert module.run_command.call_args_list[0][0][0] == '/usr/sbin/prtconf'
    # Assert swap -s command called
    assert module.run_command.call_args_list[1][0][0] == '/usr/sbin/swap -s'



# Generated at 2022-06-13 01:08:41.179302
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    # Test case: Check if SunOSHardware().get_dmi_facts returns a dictionary
    # that contains a key 'System Configuration' and that the returned
    # dictionary has the expected values.
    hw = SunOSHardware()
    dmi_facts = hw.get_dmi_facts()
    assert dmi_facts['system_vendor'] == 'Sun Microsystems'
    assert dmi_facts['product_name'] == 'Sun Fire V240'



# Generated at 2022-06-13 01:08:53.786299
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    data = {
        'ansible_machine': 'i86pc',
    }
    sunoshardware = SunOSHardware('', data)

    facts1 = {
        'processor': ['i386 @ 3000MHz'],
        'processor_cores': 'NA',
        'processor_count': 1,
        'ansible_machine': 'i86pc',
    }

    facts2 = {
        'processor': ['SUNW,UltraSPARC-IV+ @ 1500MHz', 'SUNW,UltraSPARC-IV+ @ 1500MHz'],
        'processor_cores': 2,
        'processor_count': 2,
        'ansible_machine': 'sun4u',
    }

    assert sunoshardware.get_cpu_facts() == facts1
    assert sunoshardware.get_cpu_facts(data)

# Generated at 2022-06-13 01:09:06.227894
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    """
    This class provides unit test support for method populate of class
    SunOSHardware.
    """

    class ModuleMock(object):

        def get_bin_path(self, arg1, opt_dirs=None):
            return ("/usr/bin/prtdiag")

        def run_command_environ_update(self):
            return {'LANG': 'C', 'LC_ALL': 'C', 'LC_NUMERIC': 'C'}

    def run_command(arg1):
        if arg1 == "/usr/sbin/swap -s":
            return (0, "total: 8192k bytes allocated + 7680k reserved = 15872k "
                    "used, 20192k available", "")

# Generated at 2022-06-13 01:09:15.722930
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    """
    SunOSHardware get_cpu_facts()
    :return:
    """
    # FIXME:
    module = MockModule()
    facts = SunOSHardware()


# Generated at 2022-06-13 01:09:19.702822
# Unit test for constructor of class SunOSHardwareCollector
def test_SunOSHardwareCollector():
    # This constructor should always return an object.
    sunos_collector_object = SunOSHardwareCollector()
    # This object should be of type SunOSHardwareCollector.
    assert isinstance(sunos_collector_object, SunOSHardwareCollector)

# Generated at 2022-06-13 01:09:21.431756
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    uptime_facts = {}
    uptime_facts['uptime_seconds'] = int(time.time())
    assert uptime_facts == SunOSHardware().get_uptime_facts()

# Generated at 2022-06-13 01:09:28.148019
# Unit test for method get_cpu_facts of class SunOSHardware

# Generated at 2022-06-13 01:09:52.773479
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    data = '''module: 0
instance: 0
name: cpu_info
class: misc
module:    cpu_info
instance:  0
cpu_type:  i86pc
brand:     Intel(r) Xeon(r) CPU E31270 @ 3.40GHz
clock_MHz: 3401
implementation: x86
architecture:   x86
chip_id:    0
clog_id:    0
core_id:    0
strand_id:  0'''
    module = MockModule()
    module.run_command_environ_update = {}
    hardware = SunOSHardware(module)
    rc, out, err = hardware.get_cpu_facts(module, {'ansible_machine': 'i86pc'})


# Generated at 2022-06-13 01:10:00.185392
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    module = AnsibleModule(argument_spec={})

    if module._name == 'sunos_hardware_facts':
        module.fail_json(msg='Ansible 2.4 is required for this module on SunOS/Solaris')

    # Skip if this is not a SunOS system
    if module.params['platform'] != 'SunOS':
        module.exit_json(ansible_facts={})

    try:
        SunOSHardware().populate()
    except Exception as e:
        module.fail_json(msg='Hardware populate failed with error %s' % to_native(e))



# Generated at 2022-06-13 01:10:11.890715
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    class FakeModule:
        def __init__(self):
            self.passed_command = None
            self.return_value = None

        def run_command(self, command, *args, **kwargs):
            self.passed_command = command
            return self.return_value

        def get_bin_path(self, *args, **kwargs):
            return "/usr/bin/prtdiag"


# Generated at 2022-06-13 01:10:17.455254
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    class FakeModule(object):
        def run_command(self, args, check_rc=False):
            return 0, "unix:0:system_misc:boot_time   15100000000\n", ""

    fm = FakeModule()

    sh = SunOSHardware(fm)
    uptime_facts = sh.get_uptime_facts()
    uptime_seconds = uptime_facts['uptime_seconds']

    assert isinstance(uptime_seconds, int)
    assert uptime_seconds > 0

# Generated at 2022-06-13 01:10:28.078935
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=['!all'], type='list')
        ),
        supports_check_mode=True
    )

    if not HAS_SOLARIS_FACTS:
        module.fail_json(msg='test_SunOSHardware_populate(): module sunos_facts is not importable')


# Generated at 2022-06-13 01:10:36.505029
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    class TestModule(object):
        def __init__(self):
            self.run_command_environ_update = {}

        def run_command(self, cmd, check_rc=None):
            return 0, 'System Configuration: Sun Microsystems sun4v', ''

    test_module = TestModule()
    hardware = SunOSHardware()
    hardware.module = test_module
    result = hardware.get_dmi_facts()
    assert result['system_vendor'] == 'Sun Microsystems'
    assert result['product_name'] == 'sun4v'

# Generated at 2022-06-13 01:10:41.577329
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    module = None
    # Output of /usr/bin/kstat cpu_info on a Solaris 11.4 system
    # module: cpu_info    instance: 0    module: cpu_info    class: misc    crtime: 1204.868213012    snaptime: 89486.628361842
    # brand:                   Intel(r) Xeon(r) CPU           E5-2690 v3 @ 2.60GHz
    # chip_id:                 0
    # clock_MHz:               2600.000000
    # cpu_fru:                
    # cpu_type:                x86
    # fpu_type:                x87
    # implementation:         x86
    # module: cpu_info    instance: 1    module: cpu_info    class: misc    crtime: 1204.868213012    snaptime: 89486.

# Generated at 2022-06-13 01:10:50.736837
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    from ansible.module_utils.facts.hardware.sunos import SunOSHardware
    import time, pytest
    test_time = 1548249689

    def mock_run_command(self, args):
        if args[0] == "/usr/bin/kstat":
            class FakeFile(object):
                def __init__(self, val):
                    self.val = val
                def read(self):
                    return self.val

            return 0, FakeFile(str(test_time)), ""
        return 0, "", ""

    fake_now = test_time + 10000
    fake_time = time.time
    time.time = lambda: fake_now
    test_object = SunOSHardware()

    test_object.run_command = mock_run_command
    uptime = test_object.get_uptime_facts

# Generated at 2022-06-13 01:11:01.457753
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    module = AnsibleModule({})
    hardware = SunOSHardware(module)
    collected_facts = {'ansible_machine': 'i86pc', 'ansible_system': 'SunOS'}
    facts = hardware.populate(collected_facts=collected_facts)

    assert facts['uptime_seconds'] > 0
    assert facts['devices']['sd0']['product'] != ''
    assert facts['devices']['sd0']['revision'] != ''
    assert facts['devices']['sd0']['size'] != ''
    assert facts['devices']['sd0']['vendor'] != ''

    assert facts['swap_reserved_mb'] >= 0
    assert facts['swap_allocated_mb'] >= 0
    assert facts['processor'][0] != ''

# Generated at 2022-06-13 01:11:08.379512
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    """Test populate() function of SunOSHardware class"""
    module = AnsibleModuleMock()
    SunOSHardwareInstance = SunOSHardware(module)
    SunOSHardwareInstance.module.run_command = run_command_mock
    SunOSHardwareInstance.get_dmi_facts = get_dmi_facts_mock
    SunOSHardwareInstance.get_mount_facts = get_mount_facts_mock
    SunOSHardwareInstance.get_device_facts = get_device_facts_mock
    SunOSHardwareInstance.get_uptime_facts = get_uptime_facts_mock
    SunOSHardwareInstance.get_memory_facts = get_memory_facts_mock
    SunOSHardwareInstance.get_cpu_facts = get_cpu_facts_mock
    SunOSHardwareInstance.populate()
    hardware_dict

# Generated at 2022-06-13 01:11:55.237740
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    module = type('', (), {})()

# Generated at 2022-06-13 01:11:59.625684
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    class MockModule:
        def run_command(self, command):
            if command == '/usr/bin/kstat -p unix:0:system_misc:boot_time':
                return [0, 'unix:0:system_misc:boot_time 1548249689', '']
            else:
                raise Exception("No success for command %s" % command)
    hw = SunOSHardware(MockModule())
    uptime_facts = hw.get_uptime_facts()
    assert uptime_facts['uptime_seconds'] > 0


# Generated at 2022-06-13 01:12:04.781767
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    device_facts = {
        'devices': {
            'sd0': {
                'hard_errors': '0',
                'illegal_request': '6',
                'media_errors': '0',
                'product': 'VBOX HARDDISK',
                'revision': '1.0',
                'serial': 'VB0ad2ec4d-074a',
                'size': '50.00 GB',
                'soft_errors': '0',
                'transport_errors': '0',
                'vendor': 'ATA',
                'predictive_failure_analysis': '0'
            }
        }
    }

    # FIXME(akroshny): missing test for 'sderr:0:sd0,err:Predictive Failure Analysis     0'
    # FIXME(akrosh

# Generated at 2022-06-13 01:12:08.282465
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    UptimeFacts = SunOSHardware().get_uptime_facts()
    assert UptimeFacts['uptime_seconds'] >= 0


# Generated at 2022-06-13 01:12:17.462526
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    # run_command return values
    rc = 0
    out = 'System Configuration: VMware, Inc. VMware Virtual Platform\n'
    err = ''

    # mock return values of run_command
    module = AnsibleModuleMock()
    module.run_command = MagicMock(return_value=(rc, out, err))

    # create an instance of SunOSHardware
    sunos_hw = SunOSHardware(module)
    dmi_facts = sunos_hw.get_dmi_facts()

    # assert values
    assert len(dmi_facts) == 2
    assert dmi_facts['system_vendor'] == 'VMware, Inc.'
    assert dmi_facts['product_name'] == 'VMware Virtual Platform'


import ansible.module_utils.facts.hardware.sunos

# Generated at 2022-06-13 01:12:24.570696
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    class MockModule(object):
        def run_command(self, cmd):
            return 0, 'System Configuration: Sun Microsystems  sun4v', ''

    module = MockModule()
    sunos_hardware = SunOSHardware(module)
    dmi_facts = sunos_hardware.get_dmi_facts()

    assert dmi_facts['system_vendor'] == 'Sun Microsystems'
    assert dmi_facts['product_name'] == 'sun4v'


# Generated at 2022-06-13 01:12:34.575864
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    test_device_facts = {
        'devices': {
            'sd0': {
                'predictive_failure_analysis': '0',
                'hard_errors': '0',
                'revision': '1.0',
                'product': 'VBOX HARDDISK',
                'media_errors': '0',
                'illegal_request': '6',
                'vendor': 'ATA',
                'transport_errors': '0',
                'serial': 'VB0ad2ec4d-074a',
                'soft_errors': '0',
                'size': '53687091200'
            }
        }
    }

# Generated at 2022-06-13 01:12:45.341458
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():

    # The kstat command will return a fake answer in seconds
    # In order to keep unit tests deterministic, the boot time is hardcoded (1/1/1970 00:00:00)
    # So the uptime in seconds is the same as the uptime in human format

    test_kstat_out = "unix:0:system_misc:boot_time    0"
    test_uname_out = "SunOS"


# Generated at 2022-06-13 01:12:48.239852
# Unit test for constructor of class SunOSHardwareCollector
def test_SunOSHardwareCollector():
    collectors = [c for c in HardwareCollector.__subclasses__()]
    assert(SunOSHardwareCollector in collectors)

# Generated at 2022-06-13 01:12:56.352648
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    """
    Test for method 'get_device_facts'
    """
    m = type(
        'MyModule',
        (),
        {
            'get_bin_path': lambda self, *args, **kwargs: 0,
            'run_command': lambda self, *args, **kwargs: 0,
        }
    )
    m.module_args = {}
    sun_hw = SunOSHardware(m)
    assert isinstance(sun_hw.get_device_facts(), dict)
    assert 'devices' in sun_hw.get_device_facts().keys()
    assert isinstance(sun_hw.get_device_facts()['devices'], dict)

# Generated at 2022-06-13 01:14:05.907301
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    test_object = SunOSHardware({'ansible_facts': {'platform': 'SunOS'}})
    assert test_object.get_uptime_facts() == {'uptime_seconds': test_object.uptime_second}

# Generated at 2022-06-13 01:14:08.789907
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
  facts = SunOSHardware()
  test_facts = {}
  test_facts = facts.get_memory_facts()
  assert test_facts['memtotal_mb'] > 0

# Generated at 2022-06-13 01:14:16.650180
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():

    # Test with a line that matches system_conf_regexp
    prtdiag_out = "System Configuration:\tOracle Corporation\tOracle Corporation sun4v Sun Fire T2000"
    SunOSHardware_get_dmi_facts = SunOSHardware()
    SunOSHardware_get_dmi_facts.module.run_command = lambda x: [0, prtdiag_out, '']  # noqa
    facts = SunOSHardware_get_dmi_facts.populate()
    assert facts['system_vendor'] == 'Oracle Corporation'
    assert facts['product_name'] == 'Oracle Corporation sun4v Sun Fire T2000'

    # Test with a line that doesn't match system_conf_regexp
    prtdiag_out = "System Configuration: Oracle Corporation Oracle Corporation sun4v Sun Fire T2000"
    SunOS

# Generated at 2022-06-13 01:14:25.179937
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    h = SunOSHardware()
    facts = h.populate()
    assert isinstance(facts['memtotal_mb'], int)
    assert isinstance(facts['swaptotal_mb'], int)
    assert isinstance(facts['swapfree_mb'], int)
    assert isinstance(facts['swap_allocated_mb'], int)
    assert isinstance(facts['swap_reserved_mb'], int)
    assert isinstance(facts['system_vendor'], str)
    assert isinstance(facts['processor'], list)
    assert isinstance(facts['processor_cores'], int)
    assert isinstance(facts['processor_count'], int)
    assert isinstance(facts['devices'], dict)
    assert isinstance(facts['uptime_seconds'], int)

# Generated at 2022-06-13 01:14:28.689193
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    module = AnsibleModule(argument_spec={})

    # create instance of SunOSHardware
    phy_mem = SunOSHardware(module)
    facts = phy_mem.get_dmi_facts()
    module.exit_json(ansible_facts={'ansible_dmi': facts})



# Generated at 2022-06-13 01:14:31.850600
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec={})
    hardware = SunOSHardware(module=module)
    cpu_info = hardware.get_cpu_facts()
    assert 'processor' in cpu_info
    assert 'processor_cores' in cpu_info
    assert 'processor_count' in cpu_info


# Generated at 2022-06-13 01:14:41.472198
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )


# Generated at 2022-06-13 01:14:44.010478
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec={})
    hardware_facts = SunOSHardware(module)
    out = hardware_facts.get_cpu_facts()
    assert out['processor']
    assert out['processor_cores']
    assert out['processor_count']

# Generated at 2022-06-13 01:14:49.606108
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    module = None

# Generated at 2022-06-13 01:14:55.074146
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    facts = SunOSHardware().get_memory_facts()
    assert(facts['memtotal_mb'] >= 64)
    assert(facts['swaptotal_mb'] >= 0)
    assert(facts['swapfree_mb'] >= 0)
    assert(facts['swap_reserved_mb'] >= 0)
    assert(facts['swap_allocated_mb'] >= 0)

