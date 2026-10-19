

# Generated at 2022-06-13 01:06:38.137383
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    temp_mod = AnsibleModule(argument_spec={})
    obj = SunOSHardware(temp_mod)
    # sample kstat output:
    # unix:0:system_misc:boot_time 1548249689
    with patch.object(obj.module, "run_command", return_value=(0, 'unix:0:system_misc:boot_time 1548249689\n', '')):
        obj.get_uptime_facts()
        assert temp_mod.ansible_facts['uptime_seconds'] == int(time.time() - 1548249689)


# Generated at 2022-06-13 01:06:45.756697
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    module = AnsibleModuleMock()
    facts = SunOSHardware(module).populate()
    assert facts['uptime_seconds']
    assert facts['devices']
    assert facts['memtotal_mb']
    assert facts['swap_reserved_mb']
    assert facts['swapfree_mb']
    assert facts['processor']
    assert facts['processor_count']
    assert facts['processor_cores']
    assert facts['system_vendor']
    assert facts['product_name']

# Generated at 2022-06-13 01:06:48.881969
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    module = AnsibleModule(argument_spec={})
    hardware_facts = SunOSHardware(module).populate()
    assert hardware_facts['uptime_seconds'] > 0

# Generated at 2022-06-13 01:06:53.235543
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    module = FakeAnsibleModule()
    module.run_command = my_command
    m = SunOSHardware(module)
    memory_facts = m.get_memory_facts()
    assert memory_facts['memtotal_mb'] == 8192


# Generated at 2022-06-13 01:06:59.567847
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    hardware = SunOSHardware()
    hardware.module = MagicMock()
    hardware.module.run_command.return_value = (0,
                                                'System Configuration: Sun Microsystems sun4u',
                                                '')
    dmi_facts = hardware.get_dmi_facts()
    assert_equal(dmi_facts['system_vendor'], 'Sun Microsystems')
    assert_equal(dmi_facts['product_name'], 'sun4u')


# Generated at 2022-06-13 01:07:04.926252
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    from ansible.module_utils.facts.hardware.sunos import SunOSHardware

    obj = SunOSHardware({})
    obj.get_memory_facts()

    assert obj.facts['memtotal_mb'] == 3225



# Generated at 2022-06-13 01:07:15.399863
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    data = """
        System Configuration: VMware, Inc. VMware Virtual Platform
        System Configuration: VMware, Inc. VMware Virtual Platform
        System Configuration: Sun Microsystems sun4v
        System Configuration: Sun Microsystems sun4u
        System Configuration: Oracle Corporation sun4v
    """

    module = MockModule()
    dmi_facts = {}

    module.run_command.return_value = (0, data, None)
    sun_hw = SunOSHardware(module=module)

    dmi_facts = sun_hw.get_dmi_facts()
    assert "VMware Virtual Platform" == dmi_facts['product_name']
    assert "VMware, Inc." == dmi_facts['system_vendor']



# Generated at 2022-06-13 01:07:23.852251
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    module = MockModule({'ansible_system': 'SunOS', 'ansible_distribution': 'SunOS'})
    hardware = SunOSHardware(module)

    # Test method under normal condition
    test_out = 'unix:0:system_misc:boot_time     1548249689'
    hardware.module.run_command = Mock(return_value=(0, test_out, ''))

    result = hardware.get_uptime_facts()
    assert result['uptime_seconds'] == (int(time.time()) - 1548249689)

# Generated at 2022-06-13 01:07:34.475148
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    module = AnsibleModule(argument_spec={})

    out_prtconf = """
        Memory size: 16384 Megabytes
        """
    out_swap = """
          total:        8192k bytes allocated +    576k reserved =    8768k used,    80031k available
        """
    memory_facts = {'memtotal_mb': 16384, 'swapfree_mb': 77, 'swaptotal_mb': 8, 'swap_reserved_mb': 1,
                    'swap_allocated_mb': 8}

    mock_run_command = MagicMock(return_value=(0, out_prtconf, ''))
    module.run_command = mock_run_command

    mock_get_file_content = MagicMock(return_value='')

# Generated at 2022-06-13 01:07:45.164031
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    """
    Test get_memory_facts of SunOSHardware class. The test runs
    command prtconf for platform SunOS and checks the output of
    the command to verify the expected output.
    """
    module = AnsibleModule(argument_spec={
        'fact_path': dict(required=True, type='path'),
        'gather_timeout': dict(required=True, type='int'),
        'filter': dict(required=True, type='str')
    })

    # Create object of class SunOSHardware
    sunos_hw = SunOSHardware(module=module)

    rc = 0
    out = """Memory size: 32768 Megabytes
"""
    err = ''

    # Create a mock for the Popen class
    popen_mock = mock.Mock()

    # Create a mock for the Popen instance
    pop

# Generated at 2022-06-13 01:08:06.765256
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    uptime_facts = {'uptime_seconds': 1548249689}

    uptime_facts_dummy = SunOSHardware.get_uptime_facts()
    assert uptime_facts_dummy == uptime_facts

# Generated at 2022-06-13 01:08:09.848382
# Unit test for constructor of class SunOSHardwareCollector
def test_SunOSHardwareCollector():
    hw = (None, SunOSHardwareCollector())     # set second parameter of this tuple
    assert hw[1]._platform == "SunOS"
    assert hw[1]._fact_class == SunOSHardware

# Generated at 2022-06-13 01:08:18.058034
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    from ansible.module_utils.facts.utils import MockModule
    from ansible.module_utils.facts.collector.sunos import SunOSHardwareCollector


# Generated at 2022-06-13 01:08:20.542515
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    # test method with json input
    SunOSHardware.get_uptime_facts("{}")

# Generated at 2022-06-13 01:08:24.639691
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    module_args = {}
    m = AnsibleModule(argument_spec=module_args)
    hardware = SunOSHardwareCollector.fetch_facts(m)['ansible_facts']

    assert hardware['system_memory']['total_mb'] > 0



# Generated at 2022-06-13 01:08:36.961652
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    module = FakeAnsibleModule()
    hardware = SunOSHardware()

    test_case = {'product': 'VBOX HARDDISK', 'revision': '1.0',
                 'serial': 'VB0ad2ec4d-074a', 'size': '5.0G',
                 'vendor': 'ATA', 'hard_errors': '0', 'soft_errors': '0',
                 'transport_errors': '0', 'media_errors': '0',
                 'predictive_failure_analysis': '0', 'illegal_request': '6',
                 }

    out = 'sderr:0:sd0,err:Hard Errors     0\n'
    out += 'sderr:0:sd0,err:Illegal Request 6\n'

# Generated at 2022-06-13 01:08:44.040469
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():

    fact_file = '/usr/platform/SUNW,Sun-Fire-T200/lib/fm/fmd/plugins/dist/fmd/protocol.so'
    # mock_run_command = "Sun Microsystems    sun4v"

# Generated at 2022-06-13 01:08:54.543892
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    m = SunOSHardware()

    cpu_facts = m.get_cpu_facts()
    memory_facts = m.get_memory_facts()
    dmi_facts = m.get_dmi_facts()
    device_facts = m.get_device_facts()
    uptime_facts = m.get_uptime_facts()

    mount_facts = {}
    try:
        mount_facts = m.get_mount_facts()
    except timeout.TimeoutError:
        pass

    return cpu_facts, memory_facts, dmi_facts, device_facts, uptime_facts, mount_facts

# vim: ai et ts=4 sw=4

# Generated at 2022-06-13 01:09:06.822141
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    module = None
    module_class = None
    class DummyModule:
        def get_bin_path(self, command, opt_dirs=[]):
            return command

        def run_command(self, command, check_rc=True):
            # return output from /usr/sbin/prtconf
            if 'prtconf' in command:
                out = 'Memory size: 8192 Megabytes'
                return 0, out, ''
            # return output from /usr/sbin/swap
            elif 'swap' in command:
                out = 'Total:      1025312k bytes allocated + 131808k reserved = 1157120k used, 288420k available'
                return 0, out, ''
            # return output from /usr/bin/uname command

# Generated at 2022-06-13 01:09:16.149699
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    # create a SunOSHardware object
    sunos_hardware = SunOSHardware(dict())

    # fake output of command /usr/sbin/prtconf
    prtconf_output = 'Memory size: 8192 Megabytes'

    # fake module for mocking module.run_command
    class FakeModule():
        def __init__(self):
            self.run_command = None

    # create a fake module object
    module = FakeModule()

    # mock module.run_command

# Generated at 2022-06-13 01:09:36.365379
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    hardware = SunOSHardware()
    result = hardware.populate()
    assert 'memtotal_mb' in result
    assert 'devices' in result

# Generated at 2022-06-13 01:09:45.403685
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    module = AnsibleModuleMock(platform='SunOS', run_command_environ_update={'LANG': 'C', 'LC_ALL': 'C', 'LC_NUMERIC': 'C'}, get_bin_path=None)
    module.run_command = run_command_mock
    hardware = SunOSHardware(module)
    facts = hardware.get_memory_facts()
    assert facts == {'memtotal_mb': 17408, 'swap_reserved_mb': 0, 'swapfree_mb': 0, 'swaptotal_mb': 0, 'swap_allocated_mb': 0}



# Generated at 2022-06-13 01:09:53.027821
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    from ansible.module_utils.facts.facts import Facts
    from ansible.module_utils._text import to_bytes

    module = get_mock_module()
    fact_subclass = get_mock_fact_subclass()
    facts_instance = Facts(module)
    fact_subclass._collected_facts = facts_instance.get_facts()


# Generated at 2022-06-13 01:10:01.897417
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    """
    Unit test for method get_device_facts of class SunOSHardware.
    This unit test will:
        * Run the method get_device_facts and check if the device facts
          are returned
    """

# Generated at 2022-06-13 01:10:13.815008
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    soh = SunOSHardware()

    # Define mock data for method run_command.
    # we mock data for testing the case when 'kstat' works correctly and returns correct data
    soh.module.run_command = lambda *args, **kwargs: (0, 'unix:0:system_misc:boot_time    1548249689', None)
    uptime_facts = soh.get_uptime_facts()
    assert uptime_facts['uptime_seconds'] == int(time.time() - 1548249689)

    # we mock data for testing the case when 'kstat' returns no data, the result should be None
    # we mock data for testing the case when 'kstat' works incorrectly and returns no data
    soh.module.run_command = lambda *args, **kwargs: (1, None, None)

# Generated at 2022-06-13 01:10:23.958517
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    module = AnsibleModule(argument_spec={})
    hardware_obj = SunOSHardware(module)

    hardware_obj.populate()

    assert 'processor' in hardware_obj.data
    assert 'memtotal_mb' in hardware_obj.data
    assert 'processor_cores' in hardware_obj.data
    assert 'processor_count' in hardware_obj.data
    assert 'swap_reserved_mb' in hardware_obj.data
    assert 'swap_allocated_mb' in hardware_obj.data
    assert 'swaptotal_mb' in hardware_obj.data
    assert 'swapfree_mb' in hardware_obj.data
    assert 'system_vendor' in hardware_obj.data
    assert 'product_name' in hardware_obj.data
    assert 'devices' in hardware_obj.data


# Generated at 2022-06-13 01:10:34.674363
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    a = SunOSHardware()
    b = a.get_device_facts()
    assert type(b) is dict
    assert 'devices' in b.keys()

# Generated at 2022-06-13 01:10:38.287985
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    hardware = SunOSHardware()
    hardware_facts = hardware.populate()

    # check if 'processor' key exists
    assert 'processor' in hardware_facts

    # check if a value is returned
    assert hardware_facts['processor']


# Generated at 2022-06-13 01:10:47.165720
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    facts = {}
    facts['ansible_facts'] = {}

    # Test with collect command returning out and err without any value
    facts['ansible_facts']['collect'] = {"collect_command": "/usr/sbin/prtconf",
                                         "collect_command_out": "",
                                         "collec_command_err": ""}
    memfacts = SunOSHardware._get_memory_facts(facts)
    assert memfacts['memtotal_mb'] == 0

    # Test with collect command returning a string value in out
    memfacts['ansible_facts']['collect'] = {"collect_command": "/usr/sbin/prtconf",
                                            "collect_command_out": "Memory size: 8192 Megabytes",
                                            "collec_command_err": ""}
    memfacts = SunOS

# Generated at 2022-06-13 01:10:51.610804
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    # UUT
    test_class = SunOSHardware()
    # Test object, This must match the following regex:
    #       "sderr:\d:\w+,err:\w+\s{1,}"
    #       "sderr:0:sd0,err:Hard Errors     0"

# Generated at 2022-06-13 01:11:38.990975
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    # Create a similar instance of the module used in unit tests
    module = lambda: None

    # Instance of SunOSHardware
    sunos = SunOSHardware(module=module)

    # Known facts about the instance
    setattr(module, 'run_command', lambda *b, **k: (0, b'', ''))

    # Store known facts value in the instance
    sunos.populate()

    assert sunos.facts['system_vendor'] == 'Sun Microsystems'
    assert sunos.facts['memtotal_mb'] == 1073737536
    assert sunos.facts['processor'] == []
    assert sunos.facts['processor_cores'] == 'NA'
    assert sunos.facts['processor_count'] == 0

# Generated at 2022-06-13 01:11:51.187225
# Unit test for method get_cpu_facts of class SunOSHardware

# Generated at 2022-06-13 01:11:52.766169
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    n = SunOSHardware()
    result = n.get_device_facts()
    assert 'devices' in result

# Generated at 2022-06-13 01:11:55.773689
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    hardware_facts = SunOSHardware()
    facts = hardware_facts.get_memory_facts()
    assert facts["swap_allocated_mb"] == 0
    assert facts["swap_reserved_mb"] == 0
    assert facts["swaptotal_mb"] == 0
    assert facts["swapfree_mb"] == 0
    assert facts["memtotal_mb"] == 0

# Generated at 2022-06-13 01:12:00.119682
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    module = AnsibleModuleMock()
    hardware = SunOSHardware(module)
    cpu_facts = hardware.get_cpu_facts()

    assert cpu_facts['ansible_processor_cores'] == cpu_facts['processor_cores']
    assert cpu_facts['ansible_processor_count'] == cpu_facts['processor_count']
    assert len(cpu_facts['processor']) == cpu_facts['processor_count']
    assert cpu_facts['processor_cores'] is not None
    assert cpu_facts['processor_count'] is not None



# Generated at 2022-06-13 01:12:07.814903
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    module = AnsibleModule(argument_spec={})
    module.run_command = MagicMock()


# Generated at 2022-06-13 01:12:15.492605
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    module = MockModule()
    sunoshardware = SunOSHardware(module=module)


# Generated at 2022-06-13 01:12:20.392563
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    uptime_facts = {
        'uptime_seconds': 1548249689
    }
    uptime_out = (
        'unix:0:system_misc:boot_time\t1548249689\n'
    )
    fact_module = SunOSHardware()
    fact_module.module.run_command = Mock(return_value=(0, uptime_out, ''))
    assert uptime_facts == fact_module.get_uptime_facts()

import pytest
from ansible.module_utils.common.process import get_bin_path
from unittest.mock import Mock, patch
from ansible.module_utils._text import to_bytes


# Generated at 2022-06-13 01:12:30.459173
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():

    from ansible.module_utils.facts.hardware.sunos import SunOSHardware

    class MockTime(object):
        def __init__(self, current_time):
            self.current_time = current_time

        def time(self):
            return self.current_time

    # passed in kstat output has no boot_time
    m = SunOSHardware(MockTime(1548249689))
    assert m.get_uptime_facts() is None

    # passed in kstat output has boot_time
    m = SunOSHardware(MockTime(1548249710))
    result = m.get_uptime_facts()
    assert result['uptime_seconds'] == 21

# Generated at 2022-06-13 01:12:34.098904
# Unit test for constructor of class SunOSHardwareCollector
def test_SunOSHardwareCollector():
    hardwareCollector = SunOSHardwareCollector()
    assert hardwareCollector.platform == 'SunOS'
    assert hardwareCollector._fact_class == SunOSHardware
    assert hardwareCollector._platform == 'SunOS'
    assert hardwareCollector.required_facts == set(['platform'])


# Generated at 2022-06-13 01:13:56.509038
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    sunosHardware = SunOSHardware(None)

    # Case 1: Test that it works with a normal input
    inStr = 'System Configuration: Sun Microsystems  sun4u'
    assert sunosHardware.get_dmi_facts() == {}

    # Case 2: Test that it works with a normal input
    inStr = 'System Configuration: Sun Microsystems  sun4u'
    sunosHardware.module.run_command.return_value = (0, inStr, '')
    assert sunosHardware.get_dmi_facts() == {'system_vendor': 'Sun Microsystems',
                                             'product_name': 'sun4u'}

    # Case 3: Test that it works with an incomplete string
    inStr = 'System Configuration:'

# Generated at 2022-06-13 01:14:00.792624
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    from ansible.module_utils.facts.hardware.sunos import SunOSHardware
    sunos_hardware = SunOSHardware()
    dmi = {}
    dmi = sunos_hardware.get_dmi_facts()
    assert dmi['system_vendor'] == "Oracle Corporation"
    assert dmi['product_name'] == "Oracle Database Appliance X6-2-HA"


# Generated at 2022-06-13 01:14:07.180176
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec = dict()
    )

    module.exit_json(
        ansible_facts = dict(
            ansible_processor=['SPARC-Enterprise-T5120', 'SPARC-Enterprise-T5120'],
            ansible_processor_cores=32,
            ansible_processor_count=2,
        ),
    )


# Generated at 2022-06-13 01:14:14.872969
# Unit test for method get_device_facts of class SunOSHardware

# Generated at 2022-06-13 01:14:19.196231
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )

    hardware_collector = SunOSHardwareCollector(module=module)
    hardware_collector.collect(module)
    hardware_collector.populate()
    result = hardware_collector.get_facts()

    module.exit_json(ansible_facts=dict(hardware=result))

# Generated at 2022-06-13 01:14:27.353830
# Unit test for method get_dmi_facts of class SunOSHardware

# Generated at 2022-06-13 01:14:33.925168
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    import platform

    monkeypatch.setattr(platform, 'system', lambda: "SunOS")
    hardware = SunOSHardware()


# Generated at 2022-06-13 01:14:42.520942
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    """
    This is a test for the method populate() of class SunOSHardware.
    This test uses mock module to mock run_command method. It makes sure that the
    method populate() is called with the expected parameters.
    """
    from ansible.module_utils.facts.hardware.sunos import SunOSHardware
    from ansible.module_utils.facts import timeout
    from ansible.module_utils.six.moves import builtins
    from ansible.module_utils.six import PY3

    module = fake_ansible_module()

    if PY3:
        builtins.open = open

    # Mock cpu facts
    mock_cpu_facts = {
        'processor': ['sparcv9+vis@800MHz'],
        'processor_count': 2,
        'processor_cores': 4
    }


# Generated at 2022-06-13 01:14:47.181902
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )
    if not module.check_mode:
        SunOSHardware._module = module
        SunOSHardware._check_module_imports()
        SunOSHardware._module = None
    cpu_facts = SunOSHardware.get_cpu_facts()
    assert cpu_facts['processor'].__len__() > 0


# Generated at 2022-06-13 01:14:52.254234
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    from ansible.module_utils.facts.hardware.sunos import SunOSHardware
    from ansible.module_utils.facts.collector import FactCollector

    hardware_facts = SunOSHardware(module=None)
    fact_collector = FactCollector()
    fact_collector.collect(module=None)

    for vendor in [
        "Fujitsu",
        "Oracle Corporation",
        "QEMU",
        "Sun Microsystems",
        "VMware, Inc.",
    ]:
        hardware_facts.module.run_command.return_value = 0, "System Configuration: %s Sun Fire V490" % vendor, ''
        SunOSHardware.get_dmi_facts(hardware_facts)
        assert hardware_facts.facts['dmi']['system_vendor'] == vendor