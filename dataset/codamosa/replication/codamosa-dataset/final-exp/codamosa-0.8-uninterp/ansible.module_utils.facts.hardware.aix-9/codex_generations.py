

# Generated at 2022-06-13 00:35:10.111303
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    # Instantiate a class object of module `ansible.module_utils.facts.hardware.aix`
    aix_hw_object = AIXHardware()

    # Mock module `module` attribute of class object `aix_hw_object`
    class MockModule():
        def __init__(self):
            self.run_command = MagicMock(return_value=("", "Available 09-00 Processor", ""))

    aix_hw_object.module = MockModule()

    # Get CPU facts using method `get_cpu_facts` of class object `aix_hw_object`
    cpu_facts = aix_hw_object.get_cpu_facts()

    # Assert that function `get_cpu_facts` returned the required CPU facts
    assert cpu_facts['processor_count'] == 1

# Generated at 2022-06-13 00:35:19.912280
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    module = MockModule()
    module.run_command = Mock(return_value=(0, '/dev/hd4 / jfs rw,log=/dev/hd8 0 0\n/dev/hd2 /usr jfs rw,log=/dev/hd8 0 0', err))

    aixhw = AIXHardware(module)
    mount_facts = aixhw.get_mount_facts()


# Generated at 2022-06-13 00:35:23.619471
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    mock_module = type('AnsibleModule', (), {
        'run_command': lambda x: (1, '', ''),
        'get_bin_path': lambda x, required=False: "/usr/sbin/" + x
    })()
    facts = AIXHardware(mock_module)
    facts.populate()
    assert facts.memtotal_mb is not None
    assert facts.memfree_mb is not None
    assert facts.swaptotal_mb is not None
    assert facts.swapfree_mb is not None



# Generated at 2022-06-13 00:35:32.414183
# Unit test for method get_mount_facts of class AIXHardware

# Generated at 2022-06-13 00:35:41.872207
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    test_module = AnsibleModule(argument_spec=dict())
    test_module.get_bin_path = MagicMock(return_value='/usr/sbin/mount')

# Generated at 2022-06-13 00:35:54.533659
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    facts = {'module_setup': True}
    module = FakeAnsibleModule(facts)

    hardware = AIXHardware(module)

    # setting the non aix file

# Generated at 2022-06-13 00:36:04.647943
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    class Module:
        def get_bin_path(self, name, required=True):
            return '/usr/sbin/' + name

        def run_command(self, args, check_rc=True, close_fds=True, executable=None, data=None, binary_data=False, path_prefix=None, cwd=None, use_unsafe_shell=False, prompt_regex=None):
            if isinstance(args, (str, unicode)):
                args = args.split()
            if args[0] == 'lsvg' and args[1] == '-o':
                return 0, 'rootvg\nrealsyncvg\ntestvg', ''

# Generated at 2022-06-13 00:36:09.191697
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    dmi_facts = AIXHardware().get_dmi_facts()
    assert 'firmware_version' in dmi_facts
    assert 'product_serial' in dmi_facts
    assert 'lpar_info' in dmi_facts
    assert 'product_name' in dmi_facts

# Generated at 2022-06-13 00:36:19.759350
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.hardware.aix import AIXTestFacts

    ansible_module = basic.AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = False,
    )

    mount_facts = AIXTestFacts.get_mount_facts()

    assert mount_facts['mounts'][0]['device'] == '/dev/hd4'
    assert mount_facts['mounts'][0]['mount'] == '/'
    assert mount_facts['mounts'][1]['device'] == '10.64.32.90:/vol/vol1_32bit_aix6_xlc'

# Generated at 2022-06-13 00:36:28.496659
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    m = AIXHardware()
    vgs_facts = m.get_vgs_facts()
    assert vgs_facts['vgs']['testvg'][1]['pv_name'] == 'hdisk105'
    assert vgs_facts['vgs']['testvg'][1]['pp_size'] == '4 megabyte(s)'
    assert vgs_facts['vgs']['testvg'][1]['pv_state'] == 'active'
    assert vgs_facts['vgs']['testvg'][1]['total_pps'] == '999'
    assert vgs_facts['vgs']['testvg'][1]['free_pps'] == '838'

# Generated at 2022-06-13 00:36:56.270069
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    from ansible.module_utils.facts import ModuleRunner
    from ansible.module_utils.facts.collector import collect
    from ansible.module_utils.facts.hardware.aix import AIXHardware
    from ansible.module_utils.facts.system.distribution import Distribution
    m = ModuleRunner()
    AIXHardware.module = m
    distro = Distribution()
    distro.module = m
    assert AIXHardware().get_vgs_facts()['vgs']['rootvg'][0]['pp_size'] == '4 megabytes'


# Generated at 2022-06-13 00:37:08.633350
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    module = AnsibleModuleStub()
    hardware = AIXHardware(module)

    module.run_command = MagicMock(return_value=(0, "/usr/sbin/lsdev -Cc processor\n", ""))
    hardware.populate()
    assert hardware.cpu_facts['processor_count'] == 0
    assert hardware.cpu_facts['processor'] == None
    module.run_command.assert_called_once_with('/usr/sbin/lsdev -Cc processor')

    module.run_command = MagicMock(return_value=(0, "/usr/sbin/lsdev -Cc processor\nAvailable 04-00 Processor\nAvailable 05-00 Processor\nAvailable 06-00 Processor\nAvailable 07-00 Processor", ""))
    hardware.populate()
    assert hardware.cpu_facts['processor_count']

# Generated at 2022-06-13 00:37:18.977482
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    # Test when there are two luns
    rc = 0
    out_lsdev = """name status description
hdisk0 Available 00-00-02-2,0
hdisk1 Available LVM volume hdisk1
hdisk2 Available LVM volume hdisk2
hdisk3 Available LVM volume hdisk3
hdisk4 Available LVM volume hdisk4
hdisk5 Available LVM volume hdisk5"""

# Generated at 2022-06-13 00:37:24.677768
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    # Unit test for method get_vgs_facts of class AIXHardware
    file = open('test_AIXHardware_get_vgs_facts.txt', 'r')
    data = file.read()
    file.close()
    vgs_facts = AIXHardware._get_vgs_facts(data)
    assert vgs_facts['vgs']['rootvg'][0]['pv_name'] == 'hdisk0'
    assert vgs_facts['vgs']['rootvg'][0]['total_pps'] == '546'



# Generated at 2022-06-13 00:37:31.882878
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    module = AnsibleModuleMock()

    # run lsdev command and return output
    lsdev_path = "/usr/sbin/lsdev"
    lsdev_cmd = [lsdev_path, "-Cc", "adapter"]
    lsdev_out = """ent0 Available 10/100/1000 Base-TX PCI-Express"""
    module.run_command = lambda *args, **kwargs: (0, lsdev_out, None)

    # run lsattr command and return output
    lsattr_path = "/usr/sbin/lsattr"
    lsattr_cmd_1 = [lsattr_path, "-E", "-l", "ent0"]

# Generated at 2022-06-13 00:37:41.518435
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    test = AIXHardware()
    test.module = AnsibleModule(argument_spec={})
    rc, out, err = test.module.run_command("/usr/sbin/vmstat -v")
    assert rc == 0
    assert out
    rc, out, err = test.module.run_command("/usr/sbin/lsps -s")
    assert rc == 0
    assert out
    memory_facts = test.get_memory_facts()
    assert "memtotal_mb" in memory_facts
    assert "memfree_mb" in memory_facts
    assert "swaptotal_mb" in memory_facts
    assert "swapfree_mb" in memory_facts


# Generated at 2022-06-13 00:37:48.428040
# Unit test for method get_vgs_facts of class AIXHardware

# Generated at 2022-06-13 00:37:53.382096
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    A = AIXHardware()


# Generated at 2022-06-13 00:38:01.325752
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():

    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    # create the AIXHardware object
    aix_facts = AIXHardware(module)

    result = aix_facts.populate()

    assert result['firmware_version'] == '3.3'
    assert result['lpar_info'] == 'none'
    assert result['memfree_mb'] >= 1536
    assert result['memtotal_mb'] >= 16256
    assert result['mounts']
    assert result['product_name'] == 'IBM,7040-CR7'
    assert result['product_serial'] == 'M8HW9X0'
    assert result['processor'] == 'PowerPC_POWER8'
    assert result['processor_cores'] == 1

# Generated at 2022-06-13 00:38:04.355530
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    module = AnsibleModule(argument_spec={})
    collector = AIXHardwareCollector(module=module)
    assert collector.platform == 'AIX'
    assert collector.fact_class == AIXHardware


# Generated at 2022-06-13 00:38:47.865196
# Unit test for method get_memory_facts of class AIXHardware

# Generated at 2022-06-13 00:38:56.177399
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    module_args = dict(
        command_defaults=dict(
            executable='/bin/echo',
            removes='',
            creates='',
        ),
    )
    my_module = AnsibleModule(argument_spec=module_args,
                              supports_check_mode=True)

    my_module.safe_args.update({'PATH': '/bin:/usr/bin'})

    ah = AIXHardware(module=my_module)
    device_facts = ah.get_device_facts()
    assert 'devices' in device_facts

# Generated at 2022-06-13 00:39:02.968971
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    class AIXModule:
        def run_command(self, cmd):
            out = '''memory pages
		      40940671
		      memory type
		      4K
		      free pages
		      40242886
		      pin pages
		      0'''
            return 0, out, ""

    class AIXHardware:
        def __init__(self, module):
            self.module = module

    hardware = AIXHardware(AIXModule())
    facts = hardware.get_memory_facts()
    assert facts['memtotal_mb'] == 164689
    assert facts['memfree_mb'] == 162814



# Generated at 2022-06-13 00:39:08.494235
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    module = AnsibleModule(argument_spec=dict())
    hardware = AIXHardware(module=module)
    facts = hardware.get_memory_facts()
    assert facts['memtotal_mb'] >= 0
    assert facts['memfree_mb'] >= 0
    assert facts['swaptotal_mb'] >= 0
    assert facts['swapfree_mb'] >= 0

# Generated at 2022-06-13 00:39:19.400930
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    from ansible.module_utils.facts.hardware.aix import AIXHardware
    import platform

    class TestModule(object):
        def __init__(self):
            self.run_command_lines = []
            self.run_command_rcs = []
            self.run_command_calls = 0

        def get_bin_path(self, arg, required=False):
            if arg == 'lsconf':
                return "/usr/sbin/" + arg
            elif arg == 'lsattr':
                return "/usr/bin/" + arg
            elif arg == 'lsvg':
                return "/usr/sbin/" + arg
            elif arg == 'xargs':
                return "/usr/bin/" + arg
            elif arg == 'mount':
                return "/usr/sbin/" + arg


# Generated at 2022-06-13 00:39:21.822637
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    assert AIXHardware.get_dmi_facts.__doc__ == "Get DMI Facts"
    assert AIXHardware.get_dmi_facts.__name__ == "get_dmi_facts"

# Generated at 2022-06-13 00:39:32.591510
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    import os
    import subprocess

    # create mock lsvg and lsvg -p output contents
    lsvg_path = os.path.join('/tmp', 'lsvg')
    open(lsvg_path, 'w').close()
    mock_lsvg = open(lsvg_path, 'w')
    mock_lsvg.write("rootvg:\nVG STATE: active PP SIZE: 512 megabyte(s)\n")
    mock_lsvg.write("QUORUM: 2 (Enabled)  TOTAL PPs: 1264 (650240 megabytes)\n")
    mock_lsvg.write("VG DESCRIPTORS: 4 STALE PPs: 0 ALLOCATABLE: yes\n")
    mock_lsvg.write("MAX LVs: 256 FREE PPs: 0 (0 megabytes)\n")
    mock_ls

# Generated at 2022-06-13 00:39:41.106126
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    aixhw = AIXHardware()
    aixhw.module.get_bin_path = lambda x: "/usr/bin/%s" % x
    aixhw.module.run_command = lambda x: (0, test_aix_dmi_facts_output, '')
    f = aixhw.get_dmi_facts()
    assert f['firmware_version'] == 's6100-09-06-1725'
    assert f['product_serial'] == 'NA50Z1F'
    assert 'lpar_info' in f
    assert f['product_name'] == '9131-52A'



# Generated at 2022-06-13 00:39:48.220608
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    module = AnsibleModuleMock()
    aix_hardware_collector = AIXHardwareCollector(module)
    assert isinstance(aix_hardware_collector, AIXHardwareCollector)

    # test AIXHardwareCollector class without passing module argument
    with pytest.raises(Exception) as exception:
        assert AIXHardwareCollector()
    assert str(exception.value) == 'missing required arguments: AnsibleModule'

    # test AIXHardwareCollector class by passing a module argument of wrong type
    with pytest.raises(Exception) as exception:
        assert AIXHardwareCollector(AnsibleModuleMock(wrong_type=True))
    assert str(exception.value) == 'ansible module type should be <class \'ansible.module_utils.basic.AnsibleModule\'>'



# Generated at 2022-06-13 00:39:59.064929
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    class Options:
        def __init__(self):
            self.gathering = 'smart'

    class Module:
        def __init__(self):
            self.options = Options()
            self.params = {}
        def run_command(self, args, check_rc=True):
            #output from vmstat -v
            result = ""

# Generated at 2022-06-13 00:41:18.922696
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    module = AnsibleModule(argument_spec={})
    hardware = AIXHardware(module=module)
    res = hardware.get_dmi_facts()
    if res['firmware_version'] is None:
        assert False
    if res['product_serial'] is None:
        assert False
    if res['lpar_info'] is None:
        assert False
    if res['product_name'] is None:
        assert False


# Generated at 2022-06-13 00:41:28.974368
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    import sys
    import os
    import filecmp

    class TestModule(object):
        def __init__(self, platform, args):
            self.platform = platform
            self.args = args
            self.run_command_calls = []

        def fail_json(self, *args, **kwargs):
            print("FAIL:", kwargs['msg'], file=sys.stderr)
            print("ARGS:", args, file=sys.stderr)
            sys.exit(1)

        def run_command(self, args, **kwargs):
            self.run_command_calls.append(args)

# Generated at 2022-06-13 00:41:38.644383
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    module = AnsibleModule(argument_spec={})


# Generated at 2022-06-13 00:41:46.680040
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    from os import path
    from unit.ansible_module.utils.facts.test_collection.fake_module import FakeModule

    vgs_facts = {}
    vgs_facts['vgs'] = {}
    vgs_facts['vgs']['rootvg'] = [{'pv_name': 'hdisk0', 'pv_state': 'active', 'pp_size': '4 megabyte(s)', 'total_pps': '546', 'free_pps': '0'},
                                  {'pv_name': 'hdisk1', 'pv_state': 'active', 'pp_size': '4 megabyte(s)', 'total_pps': '546', 'free_pps': '113'}]

# Generated at 2022-06-13 00:41:52.044929
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    aixhw = AIXHardware()
    aixhw.module.run_command = run_command_mock()
    cpu_facts = aixhw.get_cpu_facts()
    assert {'processor': ['PowerPC_POWER8'], 'processor_cores': 2, 'processor_count': 4} == cpu_facts                 


# Generated at 2022-06-13 00:42:00.660040
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    module = AnsibleModule(argument_spec={})
    set_module_args(module.params)
    module.exit_json = exit_json
    aix_hardware = AIXHardware(module)
    aix_hardware_facts = aix_hardware.populate()
    assert aix_hardware_facts['firmware_version'] == '1.74'
    assert aix_hardware_facts['lpar_info'] == 'None'
    assert aix_hardware_facts['memfree_mb'] > aix_hardware_facts['memtotal_mb']/2
    assert aix_hardware_facts['mounts'] is not None
    assert aix_hardware_facts['processor'] == 'PowerPC_POWER8'

# Generated at 2022-06-13 00:42:06.442821
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    """
    Test that AIXHardware.get_device_facts() can return device attributes.
    """
    module = AnsibleModule(argument_spec=dict())
    hardware = AIXHardware(module)

    device_facts = hardware.get_device_facts()
    assert device_facts['devices']['fscsi0']['type'] == 'IBM,16/4 FC PCI-X Adapter'
    assert device_facts['devices']['fscsi0']['attributes']['bus_intr_lvl'] == '5'



# Generated at 2022-06-13 00:42:16.092085
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    module = AnsibleModule(argument_spec={})
    module.exit_json = exit_json
    hw = AIXHardware(module)

    cpu_facts = hw.get_cpu_facts()
    memory_facts = hw.get_memory_facts()
    dmi_facts = hw.get_dmi_facts()
    vgs_facts = hw.get_vgs_facts()
    device_facts = hw.get_device_facts()
    mount_facts = hw.get_mount_facts()

    collected_facts = hw.populate()

    assert(collected_facts != None)
    assert(collected_facts['processor_cores'] == cpu_facts['processor_cores'])
    assert(collected_facts['processor_count'] == cpu_facts['processor_count'])

# Generated at 2022-06-13 00:42:24.742228
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():

    aix_hardware = AIXHardware()

    aix_hardware.module.run_command = run_command_mock

# Generated at 2022-06-13 00:42:32.016636
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    module = AnsibleModule(argument_spec={})
    hardware = AIXHardware(module)
    facts = hardware.populate()

    result = hardware.get_cpu_facts()
    for key in ['processor_cores', 'processor', 'processor_count']:
        assert key in result
    assert isinstance(result['processor_cores'], int)
    assert isinstance(result['processor_count'], int)

    result = hardware.get_memory_facts()
    for key in ['swapfree_mb', 'memtotal_mb', 'swaptotal_mb', 'memfree_mb']:
        assert key in result
    assert isinstance(result['memfree_mb'], int)
    assert isinstance(result['memtotal_mb'], int)
    assert isinstance(result['swapfree_mb'], int)