

# Generated at 2022-06-13 00:35:10.270284
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    module = AnsibleModule(argument_spec={'filter': {'required': True}})
    module.run_command = MagicMock(return_value=(0, None, None))
    module.get_bin_path = MagicMock(return_value=True)
    module.run_command.return_value = (0, 'ent0 Available Virtual I/O Ethernet Adapter (l-lan)', None)
    hardware = AIXHardware(module)

    lsdev_cmd = hardware.module.get_bin_path('lsdev', True)
    lsattr_cmd = hardware.module.get_bin_path('lsattr', True)
    rc, out_lsdev, err = hardware.module.run_command(lsdev_cmd)
    module.run_command.return_value = (0, out_lsdev, None)


# Generated at 2022-06-13 00:35:19.444416
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    class ModuleStub(object):

        def get_bin_path(self, arg1, arg2=False):
            if arg1 == 'mount':
                return '/usr/sbin/mount'
            return ''

        def run_command(self, cmd):
            if cmd == '/usr/sbin/mount':
                return (0, '', '', '')
            return (0, '', '', '')

    class AIXHardwareStub(AIXHardware):

        def __init__(self, module):
            self.module = module

    module = ModuleStub()
    aixhardware = AIXHardwareStub(module)
    mount_facts = aixhardware.get_mount_facts()

    assert mount_facts['mounts'] == []

# Generated at 2022-06-13 00:35:26.412409
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    from ansible.module_utils.facts.hardware.aix import AIXHardware

    hardware = AIXHardware(dict())
    hardware_facts = hardware.populate()
    assert hardware_facts is not None
    assert hardware_facts['mounts'] is not None
    assert hardware_facts['vgs'] is not None
    assert hardware_facts['devices'] is not None
    assert hardware_facts['dmi'] is not None
    assert hardware_facts['cpu'] is not None
    assert hardware_facts['mem'] is not None

# Generated at 2022-06-13 00:35:33.878804
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    class TestModule():
        def __init__(self):
            self.result = dict(
                changed=False,
                msg='',
                rc=0,
                stdout='',
                stderr=''
            )


# Generated at 2022-06-13 00:35:42.822217
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    hardware = AIXHardware({})
    hardware.module = object()

    def run_command(self, cmd, use_unsafe_shell=False, check_rc=True):
        if cmd in ["lsvg", "lsvg -o", "lsvg -p rootvg", "lsvg rootvg",
                   "lsvg -p testvg", "lsvg testvg", "lsvg -p realsyncvg", "lsvg realsyncvg"]:
            return 0, VG_OUTPUT, ""
        return 0, "", ""
    hardware.module.run_command = run_command

    hardware.module.get_bin_path = lambda x, required=False, opt_dirs=[] : x
    hardware.module.get_bin_path = lambda x, required=False, opt_dirs=[]: x


# Generated at 2022-06-13 00:35:47.829502
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    module = AnsibleModule(argument_spec={})
    hwc = AIXHardwareCollector(module)
    assert hwc.platform == 'AIX'
    assert hwc.fact_class == AIXHardware



# Generated at 2022-06-13 00:35:51.915578
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    hardware_facts = AIXHardware(dict(), dict())
    dmi_facts = hardware_facts.get_dmi_facts()
    assert dmi_facts
    assert dmi_facts['lpar_info']


# Generated at 2022-06-13 00:35:54.623780
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    a = AIXHardwareCollector()
    assert a._platform == 'AIX'
    assert a._fact_class == AIXHardware

# Generated at 2022-06-13 00:35:57.833052
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    hd = AIXHardware()
    dmi_facts = hd.get_dmi_facts()
    assert('firmware_version' in dmi_facts, 'Firmware version is not in output')



# Generated at 2022-06-13 00:36:02.743778
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    module = AnsibleModule(argument_spec={})
    obj = AIXHardware(module)
    result = obj.get_mount_facts()
    assert 'mounts' in result, "Expected 'mounts' in result"
    assert isinstance(result['mounts'], list), "Expected list for result['mounts']"


# Generated at 2022-06-13 00:36:30.468429
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    module = AnsibleModule(argument_spec={'gather_subset': dict(type='list', default=['!all'])})
    if module.params['gather_subset'] == ['!all']:
        module.params['gather_subset'] = ['all']
    hardware = AIXHardware(module=module)
    hardware.populate()
    assert hardware.facts['memfree_mb'] is not None
    assert hardware.facts['memtotal_mb'] is not None
    assert hardware.facts['swapfree_mb'] is not None
    assert hardware.facts['swaptotal_mb'] is not None
    assert hardware.facts['processor'] is not None
    assert hardware.facts['processor_cores'] is not None
    assert hardware.facts['processor_count'] is not None

# Generated at 2022-06-13 00:36:38.979771
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    class Options():
        def __init__(self, bin_path=False, always_collect_facts=False):
            self.bin_path = bin_path
            self.always_collect_facts = always_collect_facts

    class Module():
        def __init__(self, bin_path=False, always_collect_facts=False):
            self.bin_path = bin_path
            self.always_collect_facts = always_collect_facts
            self.options = Options(bin_path=bin_path, always_collect_facts=always_collect_facts)

        def get_bin_path(self, arg, required=False):
            if required:
                return "/usr/bin/" + arg
            else:
                return "/usr/bin/" + arg


# Generated at 2022-06-13 00:36:43.542188
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    from ansible.module_utils.facts.collector.hardware.aix import AIXHardware
    test_fact = AIXHardware()
    assert test_fact.get_device_facts()['devices']['fcs0']['attributes']['jumbo_frames'] == 'yes'

# Generated at 2022-06-13 00:36:49.845874
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    module = AIXModule()
    module.run_command = MagicMock(return_value=(0, mock_vmstat_v, ''))
    hardware = AIXHardware(module)
    assert hardware.get_memory_facts() == {
        'memtotal_mb': 2660,
        'memfree_mb': 2620
    }



# Generated at 2022-06-13 00:36:59.448644
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    module = AnsibleModule(argument_spec={})
    hardware = AIXHardware(module)

    vgs_facts = hardware.get_vgs_facts()
    assert isinstance(vgs_facts['vgs']['testvg'], list)
    assert isinstance(vgs_facts['vgs']['testvg'][0], dict)
    assert isinstance(vgs_facts['vgs']['testvg'][1], dict)
    assert isinstance(vgs_facts['vgs']['rootvg'], list)
    assert isinstance(vgs_facts['vgs']['rootvg'][0], dict)
    assert isinstance(vgs_facts['vgs']['rootvg'][1], dict)

# Generated at 2022-06-13 00:37:01.133729
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    ohc = AIXHardwareCollector()
    assert ohc.facts is None

# Generated at 2022-06-13 00:37:07.730187
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    hardware_facts = {}
    hardware_collector = AIXHardwareCollector(hardware_facts, None)
    assert hardware_collector is not None
    assert isinstance(hardware_collector, HardwareCollector)
    assert hardware_collector._platform == 'AIX'
    assert hardware_collector._fact_class is AIXHardware
    assert hardware_collector._config is None


# Generated at 2022-06-13 00:37:17.298978
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    module = ansible_module_mock()
    hardware = AIXHardware(module)
    lsvg_path = hardware.module.get_bin_path("lsvg")
    xargs_path = hardware.module.get_bin_path("xargs")
    cmd = "%s -o | %s %s -p" % (lsvg_path, xargs_path, lsvg_path)
    rc, out, err = hardware.module.run_command(cmd, use_unsafe_shell=True)
    if rc == 0 and out:
        vgs_facts = hardware.get_vgs_facts()
        assert vgs_facts['vgs']['rootvg'][0]['pp_size'] == '4 megabyte(s)'

# Generated at 2022-06-13 00:37:25.103934
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    class ModuleStub(object):
        def __init__(self):
            self._bin_path = {'xargs': "/usr/bin/xargs"}
        def run_command(self, cmd):
            out = "firmware_version:IBM,8233-E8B\nproduct_name:IBM,8233-E8B\nLpar Info:\nMachine Serial Number:0123456789"
            return (0, out, '')
        def get_bin_path(self, cmd):
            return "/usr/bin/xargs"
    module = ModuleStub()
    ah = AIXHardware(module)
    facts = ah.get_dmi_facts()
    assert facts["firmware_version"] == "IBM,8233-E8B"

# Generated at 2022-06-13 00:37:27.445065
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    # Create a class object from AIXHardwareCollector
    phc = AIXHardwareCollector()
    assert phc.platform == "AIX"
    assert phc._fact_class == AIXHardware


# Generated at 2022-06-13 00:38:14.063511
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.hardware.aix import AIXHardware

    aixhardware = AIXHardware({})


# Generated at 2022-06-13 00:38:25.952748
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    import unittest
    from ansible.module_utils.facts.hardware.aix import AIXHardware

    class AnsibleModuleFake(object):

        def __init__(self):
            self.params = {'gather_subset': 'all'}
            self.args = {}

        def run_command(self, command, use_unsafe_shell=False):
            if command == '/usr/sbin/lsattr -El sys0 -a fwversion':
                return 0, 'fwversion IBM,1.1.1.1', ''
            elif command == '/usr/sbin/lsconf':
                out = (
                    'Machine Serial Number: XXXXXXXXXXXX\n'
                    'LPAR Info: xxxxxxxxxxxx\n'
                    'System Model: IBM,xxxxxxxx-xxx'
                )
                return 0,

# Generated at 2022-06-13 00:38:28.003498
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    facts = AIXHardwareCollector()
    assert(facts._platform == 'AIX')
    assert(facts._fact_class == AIXHardware)

# Generated at 2022-06-13 00:38:39.769530
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    hw = AIXHardware()

    # Test get_cpu_facts
    hw.get_cpu_facts = lambda: {'processor': ['PowerPC_POWER9'], 'processor_cores': 1, 'processor_count': 1}
    # Test get_memory_facts
    hw.get_memory_facts = lambda: {'memfree_mb': 19, 'memtotal_mb': 20, 'swapfree_mb': 20, 'swaptotal_mb': 20}
    # Test get_dmi_facts
    hw.get_dmi_facts = lambda: {'firmware_version': 'IBM,U8240195', 'product_serial': 'U8240195', 'product_name': 'IBM,8284-22A'}
    # Test get_vgs_facts
    hw

# Generated at 2022-06-13 00:38:45.691916
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():

    """
    Create an instance of AIXHardware and call its method get_memory_facts.

    :return:
    """
    # Create an instance of class AIXHardware
    hardware_obj = AIXHardware(None)

    # Call the function
    result = hardware_obj.get_memory_facts()

    # Check the result
    if isinstance(result, dict):
        print("OK")
    else:
        print("NOK")


# Run the test when this file is called directly
if __name__ == '__main__':

    test_AIXHardware_get_memory_facts()

# Generated at 2022-06-13 00:38:57.353839
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    from ansible.module_utils.facts.hardware import AIXHardware
    aix_hardware = AIXHardware()

    aix_hardware.module.run_command = mock_run_command_returning_output(
        [
            "/usr/sbin/lsdev -Cc processor",
            "proc0 Available 00-00 Processor\nproc1 Defined   00-01 Processor\nproc2 Defined   00-02 Processor\nproc3 Available 00-03 Processor"
        ],
        [
            "/usr/sbin/lsattr -El proc0 -a type",
            "type PowerPC_POWER6 True"
        ],
        [
            "/usr/sbin/lsattr -El proc0 -a smt_threads",
            "smt_threads 2 True"
        ]
    )
    cpu_

# Generated at 2022-06-13 00:39:00.232901
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    """
    test should instantiate a instance of AIXHardwareCollector
    """
    hw_col = AIXHardwareCollector()
    assert hw_col
    assert hw_col._platform == 'AIX'

# Generated at 2022-06-13 00:39:10.865450
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    hardware = AIXHardware()
    out = """ name=IBM,11112-222 type=TYPE1 fwversion=IBM,12.34.56"""
    hardware.module.run_command.return_value = (0, out, '')

    out = """ Machine Serial Number: XXXXXXXX"""
    hardware.module.run_command.return_value = (0, out, '')

    out = """ LPAR Info: NAME=LPARNAME"""
    hardware.module.run_command.return_value = (0, out, '')

    out = """ System Model: IBM,9039-ABC"""
    hardware.module.run_command.return_value = (0, out, '')

    hardware.module.get_bin_path.return_value = '/usr/bin/lsconf'

    result = hardware.get_dmi

# Generated at 2022-06-13 00:39:22.105997
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    module = DummyAnsibleModule()
    hardware = AIXHardware(module)

# Generated at 2022-06-13 00:39:26.386759
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec={})
    ah = AIXHardware(module=module)
    cpu_facts = ah.get_cpu_facts()
    assert cpu_facts.get('processor')
    assert cpu_facts.get('processor_count')
    assert cpu_facts.get('processor_cores')



# Generated at 2022-06-13 00:40:49.966710
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    hardware = AIXHardware(dict())

    rc = 0
    out = """
proc0  Available 00-00 Processor 0
proc1  Available 00-01 Processor 1
proc2  Available 00-02 Processor 2
proc3  Available 00-03 Processor 3
proc4  Available 00-04 Processor 4
proc5  Available 00-05 Processor 5
proc6  Available 00-06 Processor 6
proc7  Available 00-07 Processor 7
"""
    err = ''

    hardware.module.run_command = lambda *args, **kwargs: (rc, out, err)

    rc = 0
    out = """type PowerPC_POWER8
smt_threads 2
"""
    err = ''
    hardware.module.run_command = lambda *args, **kwargs: (rc, out, err)

    actual_cpu_facts = hardware.get_

# Generated at 2022-06-13 00:40:51.664183
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    assert AIXHardwareCollector._platform == 'AIX'
    assert AIXHardwareCollector._fact_class is AIXHardware

# Generated at 2022-06-13 00:40:59.626576
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():

    class ModuleStub:
        def __init__(self):
            self.run_command_calls = []
            self._run_command_results = {}
            self.get_bin_path_calls = []
            self._get_bin_path_results = {}

        def run_command(self, cmd, use_unsafe_shell=False):
            self.run_command_calls.append({
                'cmd': cmd,
                'use_unsafe_shell': use_unsafe_shell
            })
            return self._run_command_results[cmd]

        def get_bin_path(self, name, required=False):
            self.get_bin_path_calls.append({
                'name': name,
                'required': required
            })

# Generated at 2022-06-13 00:41:05.666858
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    import re

    test_AIX = AIXHardware(None)
    test_vg = []
    # test rootvg on test machine
    test_vg.append("rootvg:\n\
    PV_NAME           PV STATE          TOTAL PPs   FREE PPs    FREE DISTRIBUTION\n\
    hdisk0            active            546         0           00..00..00..00..00\n\
    hdisk1            active            546         113         00..00..00..21..92")
    # test testvg on test machine

# Generated at 2022-06-13 00:41:07.659573
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():

    test_obj = AIXHardware()
    assert test_obj.get_mount_facts() == {'mounts': []}



# Generated at 2022-06-13 00:41:10.723791
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    from ansible.module_utils.facts.hardware.aix import AIXHardwareCollector
    aix_collector = AIXHardwareCollector()
    assert aix_collector.platform == 'AIX'
    assert aix_collector._fact_class == AIXHardware


# Generated at 2022-06-13 00:41:16.812011
# Unit test for method get_mount_facts of class AIXHardware

# Generated at 2022-06-13 00:41:20.462079
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    """
    Test AIXHardwareCollector class instantiation
    """
    hw = AIXHardwareCollector()
    assert AIXHardwareCollector._platform == 'AIX'
    assert hw.get_fact_class() == AIXHardware


# Generated at 2022-06-13 00:41:30.924585
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    """
    Test AIXHardware.get_memory_facts()
    """

    h = AIXHardware(dict(module=None))
    test_output = """
        memory pages:        8388608
        large memory pages:  0
        huge memory pages:   0
        pinned pages:        0
        large pinned pages:  0
        free pages:          8058107
    """
    h.module.run_command = lambda *args, **kwargs: (0, test_output, None)
    results = h.get_memory_facts()
    assert results['memtotal_mb'] == 32768
    assert results['memfree_mb'] == 31338


# Generated at 2022-06-13 00:41:34.518170
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    aix_hw_collector = AIXHardwareCollector()

    # Assert that the hardwareCollector platform is set to AIX
    assert aix_hw_collector.platform == 'AIX', 'Constructor for AIXHardwareCollector failed'

# Generated at 2022-06-13 00:44:26.293909
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    hardware_info = AIXHardwareCollector().collect()
    assert hardware_info._platform == 'AIX'


# Generated at 2022-06-13 00:44:34.489830
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    """
    Test the method get_vgs_facts
    """
    test_file = open('/tmp/ansible_facts/module_utils_facts_hardware_aix_test', 'r')
    test_out = test_file.read()
    test_hardware = AIXHardware()
    out = test_hardware.get_vgs_facts()

# Generated at 2022-06-13 00:44:42.647019
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    class FakeModule():
        def __init__(self, params):
            self.params = params
            self.run_command_value = 0

        def run_command(self, cmd, use_unsafe_shell=False):
            if cmd.startswith("/usr/sbin/lsattr -El sys0 -a fwversion"):
                out = "fwversion IBM,8233-E8B"
            else:
                out = "Machine Serial Number: 123456789"
            return (self.run_command_value, out, '')

        def get_bin_path(self, path, required=True):
            return path
    expected_facts = {'firmware_version': '8233-E8B', 'product_serial': '123456789'}
    test_module = FakeModule({})
   