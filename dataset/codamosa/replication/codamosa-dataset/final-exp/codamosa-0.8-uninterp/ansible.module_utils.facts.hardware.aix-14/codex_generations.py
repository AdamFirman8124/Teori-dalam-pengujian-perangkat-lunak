

# Generated at 2022-06-13 00:35:01.443417
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    AIXHardwareCollector()

# Generated at 2022-06-13 00:35:09.922543
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():

    class FakeModule(object):
        def __init__(self):
            self.run_command_result = 0

# Generated at 2022-06-13 00:35:19.791442
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    h = AIXHardware({})

# Generated at 2022-06-13 00:35:29.940655
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    # Build test string using expected output from AIX command
    test_cmd_out = """
root@test_host:[/tmp]# /usr/sbin/lsattr -El sys0 -a fwversion
fwversion                    IBM,V7R2M0
"""
    # Build the expected result
    test_out_dict = {'firmware_version': 'V7R2M0'}

    # Build the test module with test command output
    test_module = get_test_module(test_cmd_out)

    # Create instance of AIXHardware for testing
    test_hw = AIXHardware(module=test_module)

    # Call the method get_dmi_facts
    out_dmi_facts = test_hw.get_dmi_facts()

    # Verify the return dictionary is as expected
    assert out_d

# Generated at 2022-06-13 00:35:39.989791
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    module = AnsibleModule(argument_spec={})
    hardware = AIXHardware(module)
    # when lsconf_path is not found in module
    lsconf_path = None
    assert hardware.get_dmi_facts() == None
    # when lsconf_path is found in module
    lsconf_path = '/usr/sbin/lsconf'
    hardware.module.get_bin_path = MagicMock(return_value='/usr/sbin/lsconf')
    hardware.module.run_command = MagicMock(return_value=(0, 'Machine Serial Number:70b06a6b', ''))
    lsconf_data = hardware.get_dmi_facts()
    assert lsconf_data['product_serial'] == '70b06a6b'
    # when lsconf_path is found in module but ls

# Generated at 2022-06-13 00:35:50.733942
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    params = {
        'module': {
            'run_command': run_command
        }
    }

    aix_hardware = AIXHardware(module=None, params=params)
    mount_facts = aix_hardware.get_mount_facts()

    assert mount_facts['mounts'][0]['mount'] == '/'
    assert mount_facts['mounts'][0]['device'] == '/dev/hd4'
    assert mount_facts['mounts'][0]['fstype'] == 'jfs2'
    assert mount_facts['mounts'][0]['options'] == 'rw'
    assert mount_facts['mounts'][0]['size_total'] == '999680'

# Generated at 2022-06-13 00:36:01.752487
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    (module, hardware_collector) = set_module_args("AIX")

    # Test lsattr output

# Generated at 2022-06-13 00:36:09.464792
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    """
    Test method get_vgs_facts of AIXHardware class
    """
    vgs_facts = AIXHardware().get_vgs_facts()
    assert vgs_facts['vgs']['rootvg'][0]['pp_size'] == "4 megabytes"
    assert vgs_facts['vgs']['rootvg'][0]['pv_name'] == "hdisk0"
    assert vgs_facts['vgs']['rootvg'][0]['total_pps'] == "546"
    assert vgs_facts['vgs']['realsyncvg'][0]['pv_name'] == "hdisk74"
    assert vgs_facts['vgs']['testvg'][0]['pv_name'] == "hdisk105"

# Generated at 2022-06-13 00:36:18.928870
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    _module = AnsibleModule(argument_spec=dict())

    _fact_class = AIXHardware(_module)
    fact_list = _fact_class.populate()

    test_list = [
                 'memfree_mb',
                 'memtotal_mb',
                 'swapfree_mb',
                 'swaptotal_mb',
                 'processor',
                 'processor_cores',
                 'processor_count',
                 'firmware_version',
                 'product_serial',
                 'lpar_info',
                 'product_name',
                 'vgs',
                 'devices',
                 'mounts']

    for fact in test_list:
        assert fact in fact_list

# Generated at 2022-06-13 00:36:28.669704
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    import os
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts.collector import BaseFileModuleFactsCollector

    # Setup
    test_path = os.path.dirname(__file__)
    test_inputs = {'lsconf': 'lsconf.txt',
                   'vmstat': 'vmstat.txt'}
    test_files = {}
    collector = ansible_collector._collect_platform_facts(AIXHardwareCollector)
    assert isinstance(collector, AIXHardwareCollector), 'AIXHardware collector is invalid type'
    facts_collector = collector._fact_class()
    assert isinstance(facts_collector, AIXHardware), 'facts_collector is invalid type'

# Generated at 2022-06-13 00:36:52.850826
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    module = AnsibleModule(argument_spec=dict())
    har = AIXHardware(module)
    module.run_command = MagicMock(return_value=(0, 'test', ''))
    result = har.populate()
    assert 'swaptotal_mb' in result
    assert 'swapfree_mb' in result
    assert 'mounts' in result


# Generated at 2022-06-13 00:37:00.294123
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec={})
    facts = dict()
    hardware = AIXHardware(module)
    facts = hardware.populate()
    assert facts['memtotal_mb'] is not None
    assert facts['memfree_mb'] is not None
    assert facts['swaptotal_mb'] is not None
    assert facts['swapfree_mb'] is not None
    assert facts['processor'] is not None
    assert facts['processor_cores'] is not None
    assert facts['processor_count'] is not None

# Generated at 2022-06-13 00:37:03.945947
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec={})
    hardware = AIXHardware()
    cpu_facts = hardware.get_cpu_facts()
    assert cpu_facts['processor_count'] > 0
    assert cpu_facts['processor']



# Generated at 2022-06-13 00:37:13.633061
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    from ansible.module_utils.facts.hardware.aix import AIXHardware
    import mock

    test_args = {
        "run_command_data": {
            ("/usr/sbin/lsattr -El sys0 -a fwversion",): ("sys0 fwversion IBM,8205-E6C  1  True", "", 0),
            ("/usr/sbin/lsconf",): (
                "Machine Serial Number: 02G38296\n"
                "System Model: IBM,9117-570\n"
                "Machine Type: 9117-570\n"
                "LPAR Info: 1 29 2\n"
                "LPAR Characteristics: "
            ),
        }
    }

    module = mock.Mock()

# Generated at 2022-06-13 00:37:22.300458
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    """
    Test for method get_memory_facts of class AIXHardware
    """
    module = AnsibleModuleFake({})
    hardware = AIXHardware(module)
    rc, out, err = module.run_command("/usr/bin/vmstat -v")
    for line in out.splitlines():
        data = line.split()
        if 'memory pages' in line:
            pagecount = int(data[0])
        if 'free pages' in line:
            freecount = int(data[0])

# Generated at 2022-06-13 00:37:32.666901
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    from ansible.module_utils.facts.hardware.aix import AIXHardware
    aixhw = AIXHardware()
    vgs_facts = aixhw.get_vgs_facts()
    assert vgs_facts['vgs']['rootvg'][0]['pv_name'] == 'hdisk0'
    assert vgs_facts['vgs']['rootvg'][0]['pp_size'] == '4 megabyte(s)'
    assert vgs_facts['vgs']['rootvg'][0]['pv_state'] == 'active'
    assert vgs_facts['vgs']['rootvg'][0]['free_pps'] == '0'
    assert vgs_facts['vgs']['rootvg'][0]['total_pps'] == '546'


# Generated at 2022-06-13 00:37:43.216190
# Unit test for method get_dmi_facts of class AIXHardware

# Generated at 2022-06-13 00:37:49.105267
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    module = MockModule()
    hardware = AIXHardware(module)

    # Create an empty AIXHardware object
    collected_facts = {}

    # Populate the object
    hardware.populate(collected_facts)

    assert collected_facts['dmi']['system']['firmware_version'] == 'IBM,8233-E8B'
    assert collected_facts['dmi']['system']['product_name'] == '8233-E8B'
    assert collected_facts['dmi']['system']['product_serial'] == 'E1L0BML'
    assert collected_facts['dmi']['system']['lpar_info'] == '5,5'
    assert collected_facts['processor']['count'] == 4

# Generated at 2022-06-13 00:37:51.467153
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    if AIXHardwareCollector._platform != 'AIX':
        raise Exception('AIXHardwareCollector._platform is not AIX')
    if AIXHardwareCollector._fact_class != AIXHardware:
        raise Exception('AIXHardwareCollector._fact_class is not AIXHardware')


# Generated at 2022-06-13 00:37:57.284181
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    module = AnsibleModule(argument_spec=dict())

    class TestAIXHardware():
        def __init__(self, module):
            self.module = module

        def get_bin_path(self, binary_name, required=False, opt_dirs=[]):
            if binary_name == 'mount':
                return '/tmp/mount'

    class TestAnsibleModule():
        def __init__(self):
            self.name = 'test_module'

        def run_command(self, command, use_unsafe_shell=False):
            cmd_file = open('/tmp/mount', 'w')

# Generated at 2022-06-13 00:38:39.370519
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    hardware_collector = AIXHardwareCollector()
    assert isinstance(hardware_collector, HardwareCollector)
    assert hardware_collector._platform == 'AIX'
    assert hardware_collector.__class__._platform == 'AIX'
    assert hardware_collector._fact_class == AIXHardware
    assert hardware_collector.__class__._fact_class == AIXHardware


# Generated at 2022-06-13 00:38:47.668239
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    module = FakeAnsibleModule()

    lsdev_path = '/usr/sbin/lsdev'
    lsattr_path = '/usr/sbin/lsattr'
    lsdev_cmd = [lsdev_path]
    lsattr_cmd = [lsattr_path, '-E', '-l', 'hdisk0']
    module.set_command(lsdev_cmd, '''
    hdisk0 Available 00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00 EMC SYMMETRIX    Disk
    ''')
    module.set_command(lsattr_cmd, '''
    queue_depth     1
    ''')

    hw = AIXHardware(module)
    device_facts = hw.get_device_

# Generated at 2022-06-13 00:38:51.492492
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    hardware_collector = AIXHardwareCollector()

    assert hardware_collector.platform == 'AIX'
    assert hardware_collector.fact_class == AIXHardware

# Generated at 2022-06-13 00:39:00.888973
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    from ansible_collections.ansible.community.tests.unit.compat.mock import patch


# Generated at 2022-06-13 00:39:04.000836
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec={})
    hardware = AIXHardware(module)
    cpu_facts = hardware.get_cpu_facts()
    assert cpu_facts['processor_count'] > 0


# Generated at 2022-06-13 00:39:09.855574
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    """
    This is the unittest for method get_vgs_facts of class AIXHardware
    """
    module_mock = AnsibleModule(argument_spec={}, supports_check_mode=True)
    harware_obj = AIXHardware(module_mock)
    vgs_facts = harware_obj.get_vgs_facts()
    assert vgs_facts is not {}



# Generated at 2022-06-13 00:39:17.752548
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    module = AnsibleModuleMock(
        dict(
            command="/usr/sbin/lsattr -El sys0 -a fwversion",
            rc=0,
            out="Firmware Version IBM,8309-E8D_050     Firmware Version",
            err=""
        )
    )
    hardware = AIXHardware(module)
    assert hardware.get_dmi_facts() == dict(firmware_version='8309-E8D_050')

# Generated at 2022-06-13 00:39:25.183433
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    import os
    import sys
    sys.path.insert(1, os.getcwd())
    from ansible.module_utils.facts import Hardware, HardwareCollector, AIXHardware
    from ansible.module_utils.facts.hardware.aix import AIXHardware as AIXHardwareFact
    from ansible.module_utils.facts.utils import get_mount_size
    from ansible.module_utils.facts.collector import BaseFactCollector

    from ansible.module_utils.six import StringIO

    test_file_name = "test_AIXHardware_get_cpu_facts.txt"

    if os.path.isfile(test_file_name):
        os.remove(test_file_name)
    inputfile = open(test_file_name, "w+")

# Generated at 2022-06-13 00:39:27.112139
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    module = AnsibleModule(argument_spec={})
    ah = AIXHardware(module)
    ah.get_mount_facts()

# Generated at 2022-06-13 00:39:38.053333
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    class MockModule:

        class MockRunCommand:
            def __init__(self, cmd, return_code, out, err):
                self.cmd = cmd
                self.return_code = return_code
                self.out = out
                self.err = err

            def __call__(self, *cmd, **kwargs):
                return self.return_code, self.out, self.err

        def __init__(self, run_command, bin_paths):
            self.run_command = self.MockRunCommand(self.MockRunCommand, 0, "", "")
            self.bin_path = self.MockRunCommand(self.MockRunCommand, 0, bin_paths, "")

        def get_bin_path(self, file, required=False):
            return self.bin_path.cmd

# Generated at 2022-06-13 00:40:56.012624
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    aix_hw = AIXHardware(None)
    dmi_facts = aix_hw.get_dmi_facts()
    assert dmi_facts['firmware_version'] == '7.2.0.0'
    assert 'product_name' in dmi_facts
    assert 'product_serial' in dmi_facts
    assert 'lpar_info' in dmi_facts

# Generated at 2022-06-13 00:40:58.863067
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    module = AnsibleModule(argument_spec={})
    result = {}
    tmp = AIXHardware(module)
    test = tmp.get_mount_facts()
    result = test.get('mounts')
    assert result is not None, "failed to fetch mount"

# Generated at 2022-06-13 00:41:03.654659
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    test_module = AnsibleModule(argument_spec={})
    hardware = AIXHardware(test_module)
    test_out = """
    fwversion Available "IBM,810-24E"
    """
    test_module.run_command.return_value = (0, test_out, "")

    dmi_facts = hardware.get_dmi_facts()

    assert 'firmware_version' in dmi_facts
    assert 'product_serial' in dmi_facts
    assert 'lpar_info' in dmi_facts
    assert 'product_name' in dmi_facts

# Generated at 2022-06-13 00:41:06.811139
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec={})
    hardware = AIXHardware(module)
    cpu_facts = hardware.get_cpu_facts()
    assert 'processor' in cpu_facts
    assert 'processor_cores' in cpu_facts
    assert 'processor_count' in cpu_facts



# Generated at 2022-06-13 00:41:11.046698
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    from ansible.module_utils.facts import collector
    import os

    if not os.path.isfile("/etc/redhat-release"):
        aix_obj = AIXHardwareCollector()
        assert isinstance(aix_obj, AIXHardwareCollector)
        assert isinstance(aix_obj.collect(), dict)
        assert isinstance(collector.collect('hardware'), dict)
    else:
        pass

# Generated at 2022-06-13 00:41:21.505217
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    class Presenter(object):
        def __init__(self, module):
            self.module = module


# Generated at 2022-06-13 00:41:24.398978
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    aix_hw_collector = AIXHardwareCollector()
    assert aix_hw_collector._platform == 'AIX'
    assert aix_hw_collector._fact_class == AIXHardware


# Generated at 2022-06-13 00:41:35.834422
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    hw = AIXHardware({}, {}, {}, {}, {})

    input_ = """
fscsi0 Available 00-00
fscsi1 Available 00-01
fscsi2 Available 00-02
fscsi3 Available 00-03
hdisk0 Available
hdisk1 Available
hdisk2 Available
hdisk3 Available
fcs0 Available
fcs1 Available
fcs2 Available
fcs3 Available
fcs4 Available
fcs5 Available
"""


# Generated at 2022-06-13 00:41:42.754315
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    from ansible.module_utils.facts import FactCollector

    class AIXModule:
        def __init__(self):
            self.params = {}

        def run_command(self, cmd, use_unsafe_shell=False):
            class AIXResponse:
                def __init__(self, rc=0, out="", err=""):
                    self.rc = rc
                    self.stdout = out
                    self.stderr = err


# Generated at 2022-06-13 00:41:45.996807
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    module = AnsibleModule(argument_spec=dict())
    ah = AIXHardware(module=module)
    if ah.get_mount_facts():
        raise AssertionError("Failed to get mount facts")

# Generated at 2022-06-13 00:44:39.063280
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    module = AnsibleModule(
        argument_spec=dict()
    )
    hardware = AIXHardware(module=module)
    data = hardware.get_memory_facts()
    assert data['memtotal_mb'] > 0