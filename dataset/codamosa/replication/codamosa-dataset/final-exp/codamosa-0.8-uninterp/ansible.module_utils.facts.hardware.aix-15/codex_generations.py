

# Generated at 2022-06-13 00:35:04.410627
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    """Unit test for constructor of class AIXHardwareCollector"""
    aix_hardware_collector = AIXHardwareCollector(None)

    assert aix_hardware_collector._platform == 'AIX'

# Generated at 2022-06-13 00:35:08.200818
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    module = AnsibleModule(argument_spec={})
    hardware_collector = AIXHardwareCollector(module)
    assert hardware_collector._platform == 'AIX'
    assert hardware_collector._fact_class == AIXHardware


# Generated at 2022-06-13 00:35:13.225944
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    module = MockModule()
    f = AIXHardware(module)
    assert f.get_memory_facts() == {
        'memfree_mb': 3,
        'memtotal_mb': 5,
        'swapfree_mb': 2,
        'swaptotal_mb': 3
    }



# Generated at 2022-06-13 00:35:18.115068
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    data_out = '''memory pages
       679744 online
        21432 offline
       691176 total
     58442872 large
      1032304 small
    59476076 total
    '''
    mem_facts = AIXHardware().get_memory_facts()

    assert mem_facts['memtotal_mb'] == 1048576
    assert mem_facts['memfree_mb'] == 114409


# Generated at 2022-06-13 00:35:28.470180
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    misp = AIXHardware()

    class MockModule(object):
        def __init__(self):
            self.run_command = True

        def run_command(self, cmd, *args, **kwargs):
            if self.run_command:
                data = [0, 'data', 'err']
                self.run_command = False
                return data


# Generated at 2022-06-13 00:35:38.327279
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    module = AnsibleModule(argument_spec={
        'gather_subset': dict(default=[], type='list'),
        'filter': dict(default=None, type='str'),
    })
    facts_helper_mock = MagicMock(spec=FactsHelper)
    facts_helper_mock._module = module
    fact_module_mock = MagicMock(spec=AIXHardware)
    runtime_mock_fact_module = {
        'AIXHardware': fact_module_mock
    }

# Generated at 2022-06-13 00:35:43.102917
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    from ansible.module_utils.facts.hardware.aix import AIXHardware

    aix = AIXHardware()
    cpu_facts = aix.get_cpu_facts()

    assert 'processor' in cpu_facts
    assert 'processor_count' in cpu_facts
    assert 'processor_cores' in cpu_facts
    assert cpu_facts['processor_count'] > 0
    assert cpu_facts['processor_cores'] > 0



# Generated at 2022-06-13 00:35:50.522464
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    module = AnsibleModule(argument_spec=dict(
        filters=dict(default=['*'], type='list')
    ))
    hardware = AIXHardware(module=module)
    hardware.populate()
    facts = module.exit_json()['ansible_facts']
    assert facts['ansible_memfree_mb'] > 0
    assert facts['ansible_memtotal_mb'] > 0

# Generated at 2022-06-13 00:35:52.639010
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    x = AIXHardwareCollector()
    assert isinstance(x, AIXHardwareCollector)


# Generated at 2022-06-13 00:35:59.400408
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    module = AnsibleModule(
        argument_spec={})

    dmifacts_output = {
        'product_name': 'pSeries p570',
        'firmware_version': '1.1',
        'lpar_info': 'Hosting Partition',
        'product_serial': 'YAL12345'}

    hw = AIXHardware(module=module)

    hwfacts = hw.populate()
    assert dmifacts_output == hwfacts['dmi']

# Generated at 2022-06-13 00:36:26.080559
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    module = MagicMock()
    module.run_command.side_effect = [(0, 'foo', None), (0, 'bar', None), (0, 'foo1', None)]
    module.get_bin_path.side_effect = ["/usr/bin/mount", "/usr/bin/xargs", "/usr/sbin/lsvg"]

    h = AIXHardware(module)
    h.get_mount_facts()

    module.run_command.assert_called_with('/usr/bin/mount')
    module.get_bin_path.assert_called_with('mount')



# Generated at 2022-06-13 00:36:28.937499
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():

    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    ah = AIXHardware(module)

    ah.populate()

    module.exit_json(changed=False)



# Generated at 2022-06-13 00:36:37.657940
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    module = AnsibleModule(argument_spec={})
    hardware_facts_instance = AIXHardware(module=module)
    hardware_facts = hardware_facts_instance.populate()
    assert hardware_facts['firmware_version'] == 'IBM,8231-E1B', \
        "firmware version should be 'IBM,8231-E1B'"
    assert hardware_facts['product_name'] == '8231-E1B', \
        "product name should be '8231-E1B'"
    assert hardware_facts['product_serial'] == 'YALNAL', \
        "product serial should be 'YALNAL'"
    assert hardware_facts['processor_count'] == 8, \
        "processor count should be 8"

# Generated at 2022-06-13 00:36:40.288056
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    module = AnsibleModuleMock()
    module.get_bin_path = lambda x: x
    dev = AIXHardware(module)
    dev.get_vgs_facts()

# Generated at 2022-06-13 00:36:52.757744
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    lv = AIXHardware()

    test_string = \
        "rootvg:\n" \
        "PV_NAME           PV STATE          TOTAL PPs   FREE PPs    FREE DISTRIBUTION\n" \
        "hdisk0            active            546         0           00..00..00..00..00\n" \
        "hdisk1            active            546         113         00..00..00..21..92\n" \
        "\n" \
        "testvg:\n" \
        "PV_NAME           PV STATE          TOTAL PPs   FREE PPs    FREE DISTRIBUTION\n" \
        "hdisk105          active            999         838         200..39..199..200..200\n" \
        "hdisk106          active            999         599         200..00..00..199..200"



# Generated at 2022-06-13 00:36:56.610568
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    module = AnsibleModule(argument_spec={})
    aix_system_facts = AIXHardware()
    test_get_mount_facts = aix_system_facts.get_mount_facts()

    assert test_get_mount_facts is not None, 'AIX Hardware method get_mount_facts failed'



# Generated at 2022-06-13 00:37:08.897320
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():

    class Module:

        def __init__(self):
            self.params = {}
            self.params['gather_subset'] = ['hardware']

        def get_bin_path(self, executable):
            paths = ['/bin', '/usr/bin', '/sbin', '/usr/sbin', '/usr/sbin/lvm', '/usr/sbin/lvdisplay']
            return self.find_file_in_path(paths, executable)

        def find_file_in_path(self, paths, filename):
            for path in paths:
                if os.path.exists(path + '/' + filename):
                    return path + '/' + filename
            return False


# Generated at 2022-06-13 00:37:17.588758
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    tmp = AIXHardware()
    mount_facts = tmp.get_mount_facts()
    assert isinstance(mount_facts['mounts'], list)
    assert isinstance(mount_facts['mounts'][0]['mount'], str)
    assert isinstance(mount_facts['mounts'][0]['device'], str)
    assert isinstance(mount_facts['mounts'][0]['fstype'], str)
    assert isinstance(mount_facts['mounts'][0]['options'], str)
    assert isinstance(mount_facts['mounts'][0]['time'], str)


# Generated at 2022-06-13 00:37:21.416992
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    cpu_facts = AIXHardware.get_cpu_facts(None)
    assert isinstance(cpu_facts, dict)
    assert isinstance(cpu_facts['processor_count'], int)
    assert isinstance(cpu_facts['processor_cores'], int)
    assert isinstance(cpu_facts['processor'], list)


# Generated at 2022-06-13 00:37:32.514712
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    hw = AIXHardware()
    setattr(hw.module, 'run_command', run_command_mock)
    hw.get_mount_facts()
    assert hw.facts['mounts'][0]['mount'] == '/'
    assert hw.facts['mounts'][0]['device'] == '/dev/hd4'
    assert hw.facts['mounts'][0]['fstype'] == 'jfs2'
    assert hw.facts['mounts'][0]['options'] == 'rw'
    assert hw.facts['mounts'][0]['time'] == '23:48:03 Aug 25'

    assert hw.facts['mounts'][1]['mount'] == '/usr'

# Generated at 2022-06-13 00:38:00.930008
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    aixhw = AIXHardware({})
    pagesize = 4096

# Generated at 2022-06-13 00:38:10.882989
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    # Mocking result of lsattr -El sys0 -a fwversion command
    class ModuleMock:
        def __init__(self):
            self.run_command_results = []
            self.run_command_results.append((0, 'fwversion IBM,8233-E8B', None))

        def run_command(self, cmd, use_unsafe_shell=False):
            return self.run_command_results.pop()

    class AIXMock(AIXHardware):
        def __init__(self):
            self.facts = {}
            self.module = ModuleMock()
            super(AIXMock, self).populate()

    aix_facts = AIXMock()
    assert aix_facts.facts['firmware_version'] == 'IBM,8233-E8B'

#

# Generated at 2022-06-13 00:38:19.523546
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    from ansible.module_utils.facts import hardware as hardware_utils

    module = AnsibleModule(argument_spec={})
    fact_module = hardware_utils.Hardware(module)
    fact_module.populate()

    if fact_module.data['firmware_version'] != "IBM,8245-22L":
        raise Exception("Failed to gather firmware version.")
    if fact_module.data['product_name'] != "81953NA":
        raise Exception("Failed to gather product name.")
    if fact_module.data['product_serial'] != "CSDWX1X":
        raise Exception("Failed to gather product serial.")

    rc = len(fact_module.data['vgs']['rootvg'])

# Generated at 2022-06-13 00:38:31.157359
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    module = AnsibleModuleMock()
    hardware = AIXHardware(module)
    hardware.module.run_command = run_command

    device_facts = hardware.get_device_facts()

    # Check device_facts return value
    assert 'devices' in device_facts, "devices key is missing in device_facts"

    # Check if device_facts is a dictionary
    assert isinstance(device_facts['devices'], dict), "The devices key should be a dictionary"

    # Check if the device_facts dictionary has been filled with all devices
    assert len(device_facts['devices']) == 4, "device_facts dictionary should contains 4 devices"

    # Check device details for device: rmt0
    assert 'rmt0' in device_facts['devices'], "rmt0 device should be in device_facts"

# Generated at 2022-06-13 00:38:38.893691
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    """
    Test class AIXHardware. It is necessary as class AIXHardware is a subclass of Hardware.
    """
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=False
    )

    aix_hardware = AIXHardware(module)

    facts = aix_hardware.get_cpu_facts()
    assert 'processor_count' in facts
    assert 'processor' in facts
    assert 'processor_cores' in facts



# Generated at 2022-06-13 00:38:47.597855
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    module = AnsibleModule(argument_spec=dict())
    hardware = AIXHardware(module)

    # create dummy file
    tmp_aix_vgs_file = 'aix_vgs.txt'
    aix_vgs_file = open(tmp_aix_vgs_file, 'w')

# Generated at 2022-06-13 00:38:53.293011
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    # We just create an instance of the class and assert that the class and
    # platform we set up is what we get.
    aix_hw = AIXHardwareCollector()
    assert aix_hw.platform == 'AIX'
    assert aix_hw.fact_class == AIXHardware


# Generated at 2022-06-13 00:39:02.228012
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    text = """
     64M  memory pages
  34019M  large memory pages
       0  large memory pages currently in use
    4096  bytes per page
       4  bytes per physical (I/O) page
    4096  bytes per virtual (logical) page
       0  free memory pages
       0  free memory pages with zero fill
  314368  free large memory pages
    4096  system page size
   128M  minimum free pages needed to avoid quarantining
    512M  maximum free pages needed to avoid quarantining
"""
    expected = {'memtotal_mb': 64*1024, 'memfree_mb': 53*1024}
    assert AIXHardware.get_memory_facts(None, text) == expected


# Generated at 2022-06-13 00:39:05.223260
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    vgs_facts = AIXHardware(dict(ANSIBLE_MODULE_ARGS={})).get_vgs_facts()
    assert 'vgs' in vgs_facts

# Generated at 2022-06-13 00:39:16.674368
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    from ansible.module_utils.facts import FactCollector

    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )

    fact_collector = FactCollector(module=module)

    # simulate the content of /proc/meminfo

# Generated at 2022-06-13 00:40:06.445697
# Unit test for method get_mount_facts of class AIXHardware

# Generated at 2022-06-13 00:40:13.710238
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    module = MagicMock()
    setattr(module, 'run_command', MagicMock(return_value=(0, 'name type description\nproc0 Available Processor\nproc1 Available Processor\n', '')))
    setattr(module, 'get_bin_path', MagicMock(return_value='/usr/sbin/'))

    aix = AIXHardware(module)
    output = aix.get_cpu_facts()

    assert output['processor'] == "Processor"
    assert output['processor_count'] == 2
    assert output['processor_cores'] == 1


# Generated at 2022-06-13 00:40:18.893105
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    collector = AIXHardwareCollector()
    if collector is None:
        raise AssertionError("Failed to create AIXHardwareCollector")
    if collector._platform != 'AIX':
        raise AssertionError("Invalid class type")
    if collector._fact_class != AIXHardware:
        raise AssertionError("Invalid fact class type")


# Generated at 2022-06-13 00:40:23.040661
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    facts = AIXHardwareCollector(None)
    assert facts.platform == 'AIX'
    assert facts.fact_class == AIXHardware


# Generated at 2022-06-13 00:40:31.662261
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    module = get_module_mock()

# Generated at 2022-06-13 00:40:33.719457
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    aix_hw_clctr = AIXHardwareCollector()
    assert aix_hw_clctr._fact_class == AIXHardware


# Generated at 2022-06-13 00:40:40.675357
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=False
    )
    hardware = AIXHardware()
    hardware.module = module
    hardware.populate()
    assert hardware.facts['memtotal_mb'] > 0
    assert hardware.facts['memfree_mb'] > 0
    assert hardware.facts['swaptotal_mb'] > 0
    assert hardware.facts['swapfree_mb'] > 0


# Generated at 2022-06-13 00:40:51.339309
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    lsdev_output = """
name status  description
hdisk0 Available   SCSI Disk Drive
...
"""

    lsattr_output = """
attribute  value  description        user_settable  PP
type       rdac   Disk Type          False          True
pv          yes   Physical Volume    False          True
5g        yes   5-Gigabyte Volume   False          True
...
"""

    expected_results = {
        "devices": {
            "hdisk0": {
                "state": "Available",
                "type": "SCSI Disk Drive",
                "attributes": {
                    "type": "rdac",
                    "pv": "yes",
                    "5g": "yes"
                }
            }
        }
    }

    ah = AIXHardware()
    ah.module = MagicMock()

    #

# Generated at 2022-06-13 00:40:54.270191
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    """
    Test that AIXHardwareCollector instantiates objects
    """
    c = AIXHardwareCollector()
    assert isinstance(c, AIXHardwareCollector)
    assert isinstance(c.collect(), AIXHardware)

# Generated at 2022-06-13 00:40:56.494135
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    hardware_collector = AIXHardwareCollector()

    assert AIXHardwareCollector._platform == "AIX"
    assert hardware_collector.platform == "AIX"
    assert hardware_collector.fact_class == AIXHardware


# Generated at 2022-06-13 00:42:23.277629
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    aix = AIXHardwareCollector()

    # Check that platform is set
    assert aix._platform == 'AIX'

    # Check that fact_class is set
    assert aix._fact_class == AIXHardware

# Generated at 2022-06-13 00:42:26.908467
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    with_path_lookup = True
    fake_module = MockModule()
    # instantiate collector object
    objct = AIXHardwareCollector(fake_module, with_path_lookup)

    # check attributes of object
    assert objct._platform == 'AIX'
    assert objct._fact_class == AIXHardware
    return



# Generated at 2022-06-13 00:42:27.978664
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    collector = AIXHardwareCollector()
    assert collector.platform == 'AIX'

# Generated at 2022-06-13 00:42:34.635523
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    aixhw = AIXHardware()
    # Simulate a shell command output for method get_vgs_facts()
    aixhw.module.run_command = mock_run_command

# Generated at 2022-06-13 00:42:45.118153
# Unit test for method get_dmi_facts of class AIXHardware

# Generated at 2022-06-13 00:42:53.471439
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    failed = False

    if not failed:
        try:
            ah = AIXHardware(module)
        except Exception:
            failed = True
    if not failed:
        try:
            facts = ah.get_dmi_facts()
        except Exception:
            failed = True
            facts = None
    if not failed:
        assert facts is not None, "Expected non-None object"
        assert isinstance(facts, dict), "Expected dict as facts but got %s" % type(facts)
        assert not facts, "expected empty dict but got %s" % facts
    else:
        assert False, "Something went wrong"



# Generated at 2022-06-13 00:43:02.080746
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    class TestModule(object):
        def __init__(self):
            class TestShell(object):
                def __init__(self):
                    self.run_command_result = (0, get_vgs_facts_test_input, '')
                def run_command(self, arg1, **kwargs):
                    return self.run_command_result
            self.shell = TestShell()
            self.get_bin_path_result = '/usr/bin/lsvg'
            self.get_bin_path_arg = None
        def get_bin_path(self, arg1, **kwargs):
            self.get_bin_path_arg = arg1
            return self.get_bin_path_result
    module = TestModule()
    ah = AIXHardware(module=module)

# Generated at 2022-06-13 00:43:04.010485
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    hw = AIXHardwareCollector()
    assert hw.platform == 'AIX'

# Generated at 2022-06-13 00:43:11.457256
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    # create mocks
    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=False
    )
    hal = AIXHardware({'module': module})


# Generated at 2022-06-13 00:43:21.316299
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    module = AnsibleModule(argument_spec={})

    # Create a mock object and set it as module.run_command to be used later
    mocked_module = mock.MagicMock()
    mocked_module.run_command = mock.MagicMock(return_value=(0, 'test_aix_device', ''))

    # Create a mock AnsibleModule object
    hw = AIXHardware(mocked_module)
    hw.module = mocked_module

    # Run method get_device_facts, import re to validate regex
    hw.get_device_facts()
    hw.module.run_command.assert_called_once_with(['lsdev'])