

# Generated at 2022-06-13 00:35:03.501801
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    module = AnsibleModule(argument_spec={})
    module.params = {}
    facts = AIXHardware(module).get_mount_facts()
    assert len(facts['mounts']) > 0

# Generated at 2022-06-13 00:35:07.302817
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    class TestModule:
        pass

    test_module = TestModule()
    test_module.params = {}
    test_module.run_command = run_command

    ah = AIXHardware()
    ah.module = test_module
    ah.populate()


# ===========================================
# Module execution.
#

# Generated at 2022-06-13 00:35:09.258057
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    hw = AIXHardwareCollector()
    assert hw.platform == 'AIX'
    assert hw.fact_class == AIXHardware

# Generated at 2022-06-13 00:35:15.749340
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    module = AnsibleModule(argument_spec={})
    hardware = Hardware(module)
    hardware_data = hardware.populate()
    assert hardware_data.get('processor')
    assert hardware_data.get('processor_cores')
    assert hardware_data.get('processor_count')
    assert hardware_data.get('memtotal_mb')
    assert hardware_data.get('swaptotal_mb')


# Generated at 2022-06-13 00:35:20.704994
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    module = AnsibleModule(
        argument_spec={
            'gather_subset': dict(default=[], type='list'),
        },
    )
    ah = AIXHardware(module)
    memory_facts = ah.get_memory_facts()
    assert memory_facts['memtotal_mb'] > 0
    assert memory_facts['memfree_mb'] >= 0
    assert 'swaptotal_mb' in memory_facts
    assert 'swapfree_mb' in memory_facts



# Generated at 2022-06-13 00:35:27.211956
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    module = AnsibleModule(argument_spec={})
    hardware_obj = AIXHardware(module)
    hardware_facts = hardware_obj.populate()

    assert hardware_facts['processor_count'] > 0
    assert hardware_facts['memtotal_mb'] > 0
    assert isinstance(hardware_facts['vgs'], dict)
    assert isinstance(hardware_facts['processor_cores'], int)
    assert isinstance(hardware_facts['devices'], dict)

# Generated at 2022-06-13 00:35:35.815292
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    test_module = AnsibleModule(argument_spec={})
    test_module.get_bin_path = MagicMock(return_value='/usr/sbin/lsdev')
    test_module.run_command = MagicMock(return_value=(0, 'proc0 Available 00-00 Processor\nproc1 Available 00-01 Processor', ''))
    test_module.__init__ = MagicMock(return_value=None)
    ahw = AIXHardware(test_module)
    assert ahw.get_cpu_facts() == {
            'processor': '00-00',
            'processor_cores': 4,
            'processor_count': 2
            }



# Generated at 2022-06-13 00:35:37.234791
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    module = FakeModule('')
    hardware = AIXHardware(module)
    hardware.get_vgs_facts()


# Generated at 2022-06-13 00:35:39.016787
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    h = AIXHardwareCollector()
    assert h.platform == 'AIX'
    assert h.fact_class == AIXHardware

# Generated at 2022-06-13 00:35:46.377778
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    test_AIXHardware = AIXHardware('/bin/ls', '/usr/bin/awk', '/usr/bin/cut', '/sbin/lvm', '/usr/sbin/lsvg', None, '/sbin/vgdisplay', '/usr/sbin/pvdisplay')

# Generated at 2022-06-13 00:36:15.914476
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():

    class Hardware(object):
        module = None

    class Module(object):
        def run_command(self, cmd):
            return None, ' ', None

    tmp_hardware = AIXHardware(Hardware())
    tmp_hardware.module = Module()

    assert re.match("^\d+$", str(tmp_hardware.get_memory_facts()['memtotal_mb']))
    assert re.match("^\d+$", str(tmp_hardware.get_memory_facts()['memfree_mb']))
    assert re.match("^\d+$", str(tmp_hardware.get_memory_facts()['swaptotal_mb']))
    assert re.match("^\d+$", str(tmp_hardware.get_memory_facts()['swapfree_mb']))



# Generated at 2022-06-13 00:36:25.090979
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    test_module = AnsibleModule(argument_spec={})
    hardware_facts = AIXHardware(test_module)

    facts = hardware_facts.populate()
    assert 'processor' in facts
    assert 'processor_cores' in facts
    assert 'processor_count' in facts
    assert 'memtotal_mb' in facts
    assert 'memfree_mb' in facts
    assert 'swaptotal_mb' in facts
    assert 'swapfree_mb' in facts
    assert 'firmware_version' in facts
    assert 'product_serial' in facts
    assert 'lpar_info' in facts
    assert 'product_name' in facts
    assert 'vgs' in facts
    assert 'mounts' in facts
    assert 'devices' in facts
    

# Generated at 2022-06-13 00:36:32.012313
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    HW = AIXHardware()
    hw_facts = HW.populate()
    assert hw_facts['firmware_version'] == '2.10'
    assert hw_facts['product_serial'] == '02CK569'
    assert hw_facts['lpar_info'] == '1 CEC'
    assert hw_facts['product_name'] == 'IBM,8233-E8B'
    assert hw_facts['mounts'] == []
    assert hw_facts['vgs'] == {}
    assert hw_facts['devices'] == {}

# Generated at 2022-06-13 00:36:40.211414
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    # memory facts which will be checked
    memory_facts = {'memtotal_mb': 0,
                    'memfree_mb': 0,
                    'swaptotal_mb': 0,
                    'swapfree_mb': 0}
    # expected output of 'vmstat -v' command
    out = "memory pages        65536\n" \
          "memory pages free       0\n" \
          "real memory      268435456\n" \
          "free memory      268418560\n" \
          "shared memory        2048\n" \
          "buffered memory        0\n" \
          "memory in use (Mb)   167.91\n" \
          "virtual memory  8589934592\n" \
          "free virtual memory 8589933568"

    # expected output of 'lsps

# Generated at 2022-06-13 00:36:52.663433
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    # Inputs
    device_facts_helper = AIXHardware(None)
    # Outputs

# Generated at 2022-06-13 00:37:03.334066
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    class test_module(object):
        args = None
        def get_bin_path(self, arg, opt_dirs=[]):
            return '/usr/sbin/mount'

        def run_command(self, cmd, use_unsafe_shell=False):
            class test_result(object):
                def __init__(self, rc, out, err):
                    self.rc = rc
                    self.stdout = out
                    self.stderr = err

            if self.args == 'no_data':
                return test_result(0, '', '')
            elif self.args == 'one_mount':
                return test_result(0, 'node         mounted        mounted over    vfs      date        options\n/dev/hd4          /              jfs2    May 27 12:41    rw', '')


# Generated at 2022-06-13 00:37:13.300581
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    class MockModule(object):
        def __init__(self):
            self.params = {}
            self.params['filter'] = 'host'

        def get_bin_path(self, name, required=False):
            if name == 'lsdev':
                return '/usr/sbin/lsdev'
            elif name == 'lsattr':
                return '/usr/sbin/lsattr'
            else:
                return None

        def run_command(self, cmd, check_rc=None, environ_update=None, use_unsafe_shell=None):

            stdout = ''
            if cmd == ['/usr/sbin/lsdev']:
                stdout = "name                  status         description                                                   \n"

# Generated at 2022-06-13 00:37:22.040432
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    module = AnsibleModule({})
    hardware = AIXHardware(module=module)

    # Simulate the file /usr/sbin/lsdev -Cc processor
    # All lines have been removed except the part with processor
    test_file = open("/tmp/cpuinfo", "w")
    test_file.write("proc0 Available 00-00 Processor\n")
    test_file.write("proc1 Available 00-01 Processor\n")
    test_file.write("proc2 Available 00-02 Processor\n")
    test_file.write("proc3 Available 00-03 Processor\n")
    test_file.close()

    # Simulate the file /usr/sbin/lsattr -El proc0 -a type
    # All lines have been removed except the part with type

# Generated at 2022-06-13 00:37:32.556518
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes

    m = basic.AnsibleModule(
        argument_spec=dict(),
    )

    m.params = dict()

    h = AIXHardware(m)

    # Test with mount output from AIX 7.2

# Generated at 2022-06-13 00:37:43.142360
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    import sys
    if sys.version_info[0] < 3:
        import __builtin__ as builtins
    else:
        import builtins

    # setup
    module = AIXHardwareCollector.get_platform_module()

    # Test lsdev, vmstat
    module.run_command = lambda x: (0, "memory pages: 100\nfree pages: 20\n", '')

    # Test lsattr
    module.run_command = lambda x: (0, "type PowerPC_POWER5\n", '')

    # Test lsps
    module.run_command = lambda x: (0, "10MB: 1%", '')

    # Test lsconf

# Generated at 2022-06-13 00:38:13.632363
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True)
    module.run_command = MagicMock(return_value=(1, '', ''))
    set_module_args(dict(gather_subset='!all,!min'))
    aix_hw = AIXHardware(module)
    result = aix_hw.populate()
    modules_result = aix_hw.get_device_facts()

    assert type(modules_result) == dict
    assert 'devices' in modules_result
    assert type(modules_result['devices']) == dict
    assert 'hdisk1' in modules_result['devices']
    assert 'state' in modules_result['devices']['hdisk1']

# Generated at 2022-06-13 00:38:16.196924
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    module = MockModule()
    aix_hardware = AIXHardware(module)
    aix_hardware._module = module

    aix_hardware.get_device_facts()

    assert module.run_command.called

# Generated at 2022-06-13 00:38:22.143916
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    """
    Test method get_dmi_facts of class AIXHardware.
    """
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.hardware.aix import AIXHardware

    # lsattr output for sys0 -a fwversion
    lsattr_out = to_bytes('IBM,8247-22L')
    # lsconf output when $lsconf | grep 'LPAR Info'

# Generated at 2022-06-13 00:38:33.371236
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    test_module = type('', (object,), {})()
    test_module.run_command = type('', (object,), {})()
    test_module.run_command.__name__ = 'run_command'
    test_module.run_command.__call__ = lambda self, args: (0, r'fwversion   lpp_source_publisher,IBM,6.1.0.0', '')

    test_AIXHardware = AIXHardware()
    test_AIXHardware.module = test_module

    assert test_AIXHardware.get_dmi_facts() == {'firmware_version': '6.1.0.0', 'product_serial': '', 'lpar_info': '', 'product_name': ''}

# Generated at 2022-06-13 00:38:42.431842
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    from ansible.module_utils.facts.collector.hardware.aix import AIXHardware
    from ansible.module_utils.facts.collector.hardware import Hardware
    hardware = AIXHardware()

    hardware.module.get_bin_path = lambda arg: arg
    hardware.module.run_command = lambda arg: (0, '''
IBM,8233-E8B
    Machine Serial Number          : YM006073
    Machine Model Number           : 8233-E8B
    LPAR Info                      : 1 2 G
    H/W Serial Number              : YM006073
    Machine Type                   : 8233
    Firmware Version               : IBM,8233-E8B
    Firmware Version               : IBM,8233-E8B
''', '')

    dmi_facts = hardware.get_dmi

# Generated at 2022-06-13 00:38:49.700895
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    module = AnsibleModule(
        argument_spec={
            'gather_subset': dict(default=['!all'], type='list'),
            'filter': dict(default=None, type='str'),
        },
        supports_check_mode=True
    )

    if not HAS_AIX_MODULE_UTILS:
        module.fail_json(msg=missing_required_lib('IBMi OS Modules'), exception=AIX_IMP_ERR)

    result = {}
    result['failed'] = False

    # Get hardware facts
    aix_hw = AIXHardware(module)
    result['ansible_facts'] = aix_hw.populate()
    result['ansible_facts']['ansible_processor'] = ' '.join(result['ansible_facts']['ansible_processor'])

# Generated at 2022-06-13 00:38:53.806084
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    module = AnsibleModule(argument_spec={})
    collector = AIXHardwareCollector(module=module)
    assert collector.platform == 'AIX'
    assert collector.fact_class == AIXHardware


# Generated at 2022-06-13 00:39:02.374426
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    module = AnsibleModule(argument_spec={})
    AIXHardwareInstance = AIXHardware(module)


# Generated at 2022-06-13 00:39:14.915544
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    """
    Unit test for method get_dmi_facts of class AIXHardware
    """
    NX_MOCK_DMI_FACTS = {
    "firmware_version": "CUMULUS VERSION: 1.1",
    "lpar_info": "8 Virtual I/O Server Virtual Machine",
    "product_name": "8231-E2B",
    "product_serial": "8172Z0C"
    }


# Generated at 2022-06-13 00:39:20.035685
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    facts = AIXHardware(module=module)
    assert facts.get_cpu_facts()['processor_cores'] == 16
    assert facts.get_cpu_facts()['processor_count'] == 4
    assert facts.get_cpu_facts()['processor'] == 'PowerPC_POWER8'


# Generated at 2022-06-13 00:40:12.299627
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    class MockModule(object):
        def run_command(self, cmd, use_unsafe_shell=False):
            if cmd == '/usr/sbin/lsattr -El sys0 -a fwversion':
                return 0, 'fwversion IBM,8233-E8B', ''
            if cmd == '/usr/sbin/lsconf':
                return 0, 'lpar_info:1-10-5-5258-0\nMachine Serial Number:0987654321\nSystem Model:IBM,8233-E8B', ''

    class MockFactCollector(object):
        def __init__(self):
            self.module = MockModule()

    hw = AIXHardware(MockFactCollector())
    facts = hw.get_dmi_facts()

# Generated at 2022-06-13 00:40:22.526666
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    vgs_facts = AIXHardware(dict(), dict()).get_vgs_facts()

# Generated at 2022-06-13 00:40:31.304962
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    """
    Unit test for AIXHardware.get_vgs_facts()
    """
    from ansible.module_utils.facts import ModuleFacts

    class FakeModule(object):
        def __init__(self, module_name):
            self.__module_name = module_name

        def get_bin_path(self, exe, required=False):
            return 'lsvg'

        def run_command(self, cmd, use_unsafe_shell=False):
            if cmd == 'lsvg -o':
                return 0, 'rootvg\nrealsyncvg\ntestvg', ''

# Generated at 2022-06-13 00:40:42.580699
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    module = AnsibleModule(argument_spec={})
    module.params = {}
    hardware = AIXHardware(module)
    assert hardware._platform == 'AIX'
    assert hardware._fact_class == AIXHardware


# Generated at 2022-06-13 00:40:47.219009
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    """
    The test case will test the method get_mount_facts of class AIXHardware
    """
    module = AnsibleModule({})
    aix_facts_obj = AIXHardware(module)

    #Calls get_mount_facts method of class AIXHardware
    aix_facts_obj.get_mount_facts()


# Generated at 2022-06-13 00:40:56.317771
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    module = AnsibleModule(argument_spec={})
    hardware = AIXHardware(module)

    hardware.module.run_command = mock.Mock(return_value=(0, '', ''))
    hardware.module.get_bin_path = mock.Mock(return_value=True)


# Generated at 2022-06-13 00:41:02.905833
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    module = AnsibleModule(argument_spec={})
    hardware = AIXHardware(module)

    lsvg_path = module.get_bin_path("lsvg")
    if lsvg_path:
        rc, out, err = module.run_command("%s -o | %s rootvg" % (lsvg_path, lsvg_path))
        if rc == 0 and out:
            dmi_facts = hardware.get_dmi_facts()
            assert dmi_facts['firmware_version'] is not None
            assert dmi_facts['lpar_info'] is not None
            assert dmi_facts['product_name'] is not None
            assert dmi_facts['product_serial'] is not None



# Generated at 2022-06-13 00:41:05.173556
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    test_AIXHardwareCollector = AIXHardwareCollector()
    assert (str(type(test_AIXHardwareCollector)) == "<class 'ansible.module_utils.facts.hardware.aix.AIXHardwareCollector'>")


# Generated at 2022-06-13 00:41:09.763761
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    """ Unit test for method get_cpu_facts of class AIXHardware """
    module = AnsibleModule(argument_spec={})
    hardware_facts = AIXHardware(module)
    cpu_facts = hardware_facts.get_cpu_facts()
    assert cpu_facts['processor'] == 'PowerPC_POWER8'
    assert cpu_facts['processor_cores'] == 4
    assert cpu_facts['processor_count'] == 2



# Generated at 2022-06-13 00:41:16.052563
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    class Object(object):
        module = None
        bin_path = None
        run_command = None
    aix_hw = AIXHardware(Object())
    aix_hw._mount_facts = None


# Generated at 2022-06-13 00:42:45.486234
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    module = AnsibleModule(
        argument_spec={})
    hardware = AIXHardware(module)
    memory_facts = hardware.get_memory_facts()
    assert 'memtotal_mb' in memory_facts
    assert 'memfree_mb' in memory_facts
    assert 'swaptotal_mb' in memory_facts
    assert 'swapfree_mb' in memory_facts
    assert 'swaptotal_mb' in memory_facts
    assert 'swapfree_mb' in memory_facts



# Generated at 2022-06-13 00:42:50.960099
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    m = AIXHardwareCollector({})
    module = AnsibleModule(argument_spec={})
    # create an instance of AIXHardware
    aix_hardware = AIXHardware(module)
    aix_hardware.populate_facts()
    cpu_facts = aix_hardware.get_cpu_facts()
    assert 'processor_count' in cpu_facts
    assert 'processor' in cpu_facts
    assert 'processor_cores' in cpu_facts


# Generated at 2022-06-13 00:42:58.823753
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    """
    Unit test of AIXHardware.get_memory_facts
    """
    from ansible.module_utils.facts.hardware.aix import AIXHardware
    import unittest

    class TestAIXHardware(unittest.TestCase):
        """
        Unit test of AIXHardware.get_memory_facts
        """
        def setUp(self):
            """
            Setup variables
            """
            self.vmstatOutput = """
            memory pages:    161906
                    pin:      2986
              pout:      1261
            free pages:     127096
                    pin:      2986
              pout:      1261
            """


# Generated at 2022-06-13 00:43:06.764083
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    import json

    # get some testdata
    testdata_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + '/testdata/'
    test_file = 'aix_lsattr_lsdev_output.json'

    with open(testdata_path + test_file) as data_file:
        data = json.load(data_file)
        lsattr_out = data['lsattr_out']
        lsdev_out = data['lsdev_out']

    # create the test object and add the testdata
    obj = AIXHardware()
    obj.module = AnsibleModule(argument_spec = dict())
    obj.lsdev_out = lsdev_out
    obj.lsattr_out = lsattr_out

    # run the populate method
    out

# Generated at 2022-06-13 00:43:07.965010
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    module = AnsibleModule(argument_spec={})
    hardware = AIXHardware(module)
    hardware.populate()
    assert hardware.populate() is not None


# Generated at 2022-06-13 00:43:16.873881
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    facts_module = AnsibleModule(argument_spec={})
    # When system platform is AIX
    aix_facts = AIXHardwareCollector(facts_module)
    # Then aix_facts is class AIXHardware and their parent class
    assert isinstance(aix_facts, AIXHardwareCollector)
    assert isinstance(aix_facts, HardwareCollector)
    # And has_lspv, has_lsvg and has_mount attributes are True
    assert hasattr(aix_facts, 'has_lspv')
    assert hasattr(aix_facts, 'has_lsvg')
    assert hasattr(aix_facts, 'has_mount')
    assert aix_facts.has_lspv == True
    assert aix_facts.has_lsvg == True
    assert aix_facts.has

# Generated at 2022-06-13 00:43:23.295407
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    aix_hw = AIXHardware()
    aix_hw.module.run_command = cmd_run
    cpu_facts = aix_hw.get_cpu_facts()
    assert 'processor' in cpu_facts
    assert 'processor_core' in cpu_facts
    assert 'processor_cores' in cpu_facts
    assert 'processor_count' in cpu_facts



# Generated at 2022-06-13 00:43:29.112167
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.hardware.aix import AIXHardware
    from ansible.module_utils.facts.utils import get_file_lines

    class TestModule(object):
        def __init__(self):
            self.params = {'gather_subset': ['!all', 'hardware']}

        def fail_json(self, *args, **kwargs):
            self.exit_args = args
            self.exit_kwargs = kwargs
            raise Exception('fail_json')

        def run_command(self, *args, **kwargs):
            return get_file_lines('unit/ansible/module_utils/tests/unit/utils/vmstat_v.stdout'), '', 0


# Generated at 2022-06-13 00:43:37.119113
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    module = AnsibleModule(argument_spec={})
    hardware_collector = AIXHardwareCollector(module=module)
    hardware_collector.populate()
    hardware_facts = hardware_collector.get_facts()
    assert hardware_facts['mounts'][0]['mount'] == '/'
    assert hardware_facts['mounts'][0]['device'] == '/dev/hd4'
    assert hardware_facts['mounts'][0]['fstype'] == 'jfs2'
    assert hardware_facts['mounts'][0]['time'] == 'Tue May 21 11:11:20 2019'
    assert hardware_facts['mounts'][0]['options'] == 'rw,log=/dev/hd8'
    assert hardware_facts['mounts'][0]['size_total'] == 112943553536

# Generated at 2022-06-13 00:43:45.995827
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    module = AnsibleModuleMock()
