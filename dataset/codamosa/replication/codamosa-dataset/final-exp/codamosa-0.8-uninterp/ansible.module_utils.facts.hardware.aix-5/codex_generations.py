

# Generated at 2022-06-13 00:35:10.345558
# Unit test for method get_device_facts of class AIXHardware

# Generated at 2022-06-13 00:35:11.756244
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    module = AnsibleModule(argument_spec={})

    hardware = AIXHardware(module=module)
    hardware.get_mount_facts()



# Generated at 2022-06-13 00:35:20.357039
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    # Arrange
    test_module = AnsibleModule(argument_spec={})
    test_module.run_command = MagicMock(return_value=(0, '00C880 Available 00-00-4C-00-00-00-00-00  Processor', ""))
    test_module.run_command.side_effect = [(0, '00C880 Available 00-00-4C-00-00-00-00-00  Processor', ""),
                                           (0, 'type PowerPC_POWER8', ""),
                                           (0, 'smt_threads 1', "")]
    test_hardware = AIXHardware(test_module)

    # Act
    test_hardware.get_cpu_facts()

    # Assert

# Generated at 2022-06-13 00:35:30.290745
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    from ansible_collections.ansible.community.tests.unit.modules.utils import AnsibleExitJson
    from ansible_collections.ansible.community.tests.unit.modules.utils import AnsibleFailJson
    from ansible_collections.ansible.community.tests.unit.modules.utils import set_module_args
    from ansible_collections.ansible.community.plugins.module_utils.facts.hardware.aix import AIXHardware
    from ansible.module_utils.facts import FactCollector

    module_name = 'ansible_collections.ansible.community.plugins.modules.hardware.aix'
    fact_class_name = 'AIXHardware'

    # generate test data.
    test_data = {}

# Generated at 2022-06-13 00:35:32.042032
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    x = AIXHardwareCollector()
    assert x.platform == 'AIX'


# Generated at 2022-06-13 00:35:34.499267
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    hwc = AIXHardwareCollector()
    assert hwc._platform == 'AIX'
    assert hwc._fact_class == AIXHardware


# Generated at 2022-06-13 00:35:40.417284
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    _module = type('_module', (object,), {})()
    _module.get_bin_path = lambda *args: '/usr/bin/%s' % args[0]
    _module.run_command = lambda *args, **kw: (0, '', '')
    _module.run_command.__name__ = 'run_command'
    _AIXHardware = AIXHardware(_module)
    _AIXHardware.get_vgs_facts()

# Generated at 2022-06-13 00:35:46.797642
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():

    # Mock class AIXHardware
    class AIXHardware(object):
        def __init__(self):
            # Mock module_utils.facts.utils.get_mount_size
            self.module = Mock(**{
                'get_bin_path.return_value' : '/usr/sbin/lsvg',
                'run_command.return_value' : (0,
                                              '/dev/hd4          /                       jfs2     log     yes     rw,intr,largefiles,log=/dev/hd8   rootvg',
                                              ''),
            })

        def module(self):
            return self.module

    hardware = AIXHardware()

    # Test with option '-o'
    mount_facts = hardware.get_mount_facts()

# Generated at 2022-06-13 00:35:58.062499
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    aix_hardware = AIXHardware()

    # Set the values of aix_hardware.module.run_command
    aix_hardware.module.run_command = lambda command, use_unsafe_shell=False: (0,
        "memory pages:                        46864\n"
        "memory page size (p.p.b.):            4 Kbytes,  4 pages per block\n"
        "free pages:                           46153", "")

    memory_facts = aix_hardware.get_memory_facts()
    assert memory_facts['memtotal_mb'] == 193
    assert memory_facts['memfree_mb'] == 183

    # Set the values of aix_hardware.module.run_command

# Generated at 2022-06-13 00:36:07.526683
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    hardware = AIXHardware()
    hardware.module.run_command = MagicMock(return_value=(0, '4096 memory pages' + '\n'
                                                          '0 free pages', ''))
    assert hardware.get_memory_facts()['memtotal_mb'] == 16
    assert hardware.get_memory_facts()['memfree_mb'] == 0
    assert hardware.get_memory_facts()['swaptotal_mb'] == 0
    assert hardware.get_memory_facts()['swapfree_mb'] == 0

    hardware.module.run_command = MagicMock(return_value=(0, '4096 memory pages' + '\n'
                                                          + '16 free pages', ''))

    assert hardware.get_memory_facts()['memtotal_mb'] == 16
    assert hardware.get_memory

# Generated at 2022-06-13 00:36:34.332918
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    from ansible.module_utils.facts.hardware.aix import AIXHardware
    from ansible.module_utils.facts.hardware.aix import test_vgs_facts_output

    test_obj = AIXHardware()
    test_obj.module = MockModule()
    test_obj.module.run_command.return_value = test_vgs_facts_output

    result = test_obj.get_vgs_facts()

# Generated at 2022-06-13 00:36:41.661875
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    # Given
    from ansible.module_utils.facts.hardware.aix import AIXHardware

    hardware = AIXHardware()
    hardware.module = Mock()


# Generated at 2022-06-13 00:36:53.731451
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    test_module = AnsibleModule(argument_spec={}, supports_check_mode=True)

    from ansible_collections.notstdlib.moveitallout.tests.unit.compat import unittest
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat.mock import patch


# Generated at 2022-06-13 00:37:01.473720
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    # Note: this test is for Python3, for Python2 we can use io module or
    # change the output of lsdev to bytes.
    from unittest.mock import patch
    from ansible.module_utils.facts.hardware.aix import AIXHardware
    module = AnsibleModuleMock()
    aix_hardware = AIXHardware(module)

# Generated at 2022-06-13 00:37:08.721768
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    class ModuleStub:
        class RunCommandResult:
            def __init__(self, rc, out, err):
                self.rc = rc
                self.out = out
                self.err = err
            def run_command(self, cmd):
                return self.rc, self.out, self.err

    m = ModuleStub()
    ah = AIXHardware(m)
    ah.populate()
    assert len(ah.facts['mounts']) == 2

# Generated at 2022-06-13 00:37:19.101451
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    module = MockModule()
    hardware = AIXHardware(module)

    # test 1, check command lsdev

# Generated at 2022-06-13 00:37:26.415844
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    hardware_obj = AIXHardware()


# Generated at 2022-06-13 00:37:38.469782
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    from ansible.module_utils import basic
    import json

    module = basic.AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True)
    module.run_command = lambda *cmd, **kwargs: (0, "", "")

    fact_instance = AIXHardware(module)
    fact_instance.populate()


# Generated at 2022-06-13 00:37:40.512672
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    module = AnsibleModule(argument_spec={})
    hardware = AIXHardware(module)
    hardware.get_mount_facts()



# Generated at 2022-06-13 00:37:47.875371
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    module = AnsibleModule(argument_spec={})
    module.run_command = mock.Mock(return_value=(0, "node mounted mounted RFS local", ""))
    hardware = AIXHardware(module)
    result_mounts = hardware.get_mount_facts()
    assert result_mounts == {'mounts': [{'mount': 'mounted', 'options': 'RFS', 'fstype': 'local', 'time': 'mounted', 'device': 'node'}]}
    module.run_command = mock.Mock(return_value=(0, "123.123.123.123:/path/to/mount mounted nfs rw,bg,hard,nointr,rsize=32768,wsize=32768,tcp,vers=3,timeo=600,actimeo=0 mounted", ""))

# Generated at 2022-06-13 00:38:13.672226
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    module = AnsibleModule({'module_utils': 'ansible.module_utils.facts.hardware.aix'})
    aixHardware = AIXHardware(module)

    lsconf_path = module.get_bin_path("lsconf")

    if lsconf_path:
        return aixHardware.get_dmi_facts()
    else:
        return {}



# Generated at 2022-06-13 00:38:14.971103
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    hw = AIXHardwareCollector()
    assert hw.fact_class == AIXHardware

# Generated at 2022-06-13 00:38:22.514522
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    module = AnsibleModuleMock({})
    hardware = AIXHardware(module)
    hardware.module.run_command = run_command_mock

    hardware_facts = hardware.get_cpu_facts()
    assert hardware_facts == {'processor_cores': 1,
                              'processor': 'PowerPC_POWER7',
                              'processor_count': 4}


# Generated at 2022-06-13 00:38:34.248190
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.module_utils.facts.aix import AIXHardware
    from ansible.module_utils.facts.aix import AIXHardwareCollector
    from ansible.module_utils.facts.aix import aix_collector
    import sys

    module = sys.modules['ansible.module_utils.facts.aix']
    aix_collector.AIXHardware = AIXHardware
    aix_collector.AIXHardwareCollector = AIXHardwareCollector

    if getattr(module, '__package__', None) is None:
        module.__package__ = "ansible.module_utils.facts.aix"

# Generated at 2022-06-13 00:38:41.190377
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    testhw = AIXHardware({})
    testhw.module.run_command = lambda x: (0, '/usr/sbin/lsattr -El sys0 -a fwversion IBM,8233-E8B', '')
    testhw.lsconf_path = '/usr/sbin/lsconf'
    testhw.lsconf_out = """
System Model: IBM,8233-E8B
Machine Serial Number: 12345
LPAR Info: 1 DP
"""
    dmi_facts = testhw.get_dmi_facts()
    assert dmi_facts['firmware_version'] == 'IBM,8233-E8B'
    assert dmi_facts['product_serial'] == '12345'
    assert dmi_facts['lpar_info'] == '1 DP'

# Generated at 2022-06-13 00:38:52.617826
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    module = AnsibleModule(argument_spec={})
    fact_instance = AIXHardware(module=module)
    dmidecode_facts = {'system': {'product': {'name': 'IBM,8286-41A', 'serial': '00F1234', 'uuid': '00112233-4455-6677-8899-AABBCCDDEEFF'}},
                       'baseboard': {'manufacturer': 'IBM Corporation'},
                       'bios': {'vendor': 'IBM -[828621X]-', 'version': '08J1523P', 'date': '09/27/2018'}}
    dmi_facts = fact_instance.get_dmi_facts(dmidecode_facts)

# Generated at 2022-06-13 00:38:59.439741
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    """
    Unit test for retrieving of AIX memory facts
    """
    task_vars = dict(ansible_facts={})
    module_name = 'test_module'
    module_args = {'filter': '*'}
    tmp = AIXHardware(module_name, module_args, task_vars)
    result = tmp.get_memory_facts()
    assert 'memtotal_mb' in result
    assert 'memfree_mb' in result
    assert 'swaptotal_mb' in result
    assert 'swapfree_mb' in result



# Generated at 2022-06-13 00:39:03.337581
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    module = AnsibleModule(argument_spec={})
    aix = AIXHardware(module)
    mounts = aix.get_mount_facts()['mounts']
    assert len(mounts) >= 1

# Generated at 2022-06-13 00:39:15.578658
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.utils import get_mount_size
    hard = AIXHardware(dict(ansible_mounts=None, ansible_devices=None))

    assert(hard.get_mount_facts() == {})


# Generated at 2022-06-13 00:39:21.526888
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    module = AnsibleModuleMock()
    module.run_command = Mock(return_value=(0, "proc0 Available 00-00-1E2  PROCESSOR", ""))
    facts = AIXHardware(module)
    cpu_facts = facts.get_cpu_facts()
    assert cpu_facts.get('processor_count') == 1
    assert cpu_facts.get('processor') == '00-00-1E2'
    assert cpu_facts.get('processor_cores') is None



# Generated at 2022-06-13 00:39:54.056809
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec={})
    hardware_obj = AIXHardware(module)

    rc, out, err = module.run_command("/usr/sbin/lsdev -Cc processor")
    for line in out.splitlines():
        if 'Available' in line:
            data = line.split(' ')
            cpudev = data[0]

    rc, out, err = module.run_command("/usr/sbin/lsattr -El " + cpudev + " -a type")
    data = out.split(' ')
    cpu_type = data[1]

    rc, out, err = module.run_command("/usr/sbin/lsattr -El " + cpudev + " -a smt_threads")
    data = out.split(' ')
    cpu_c

# Generated at 2022-06-13 00:40:04.430436
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes

    hardware = AIXHardware()
    hardware.module = basic.AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    hardware.module.run_command = lambda *args, **kwargs: (0, to_bytes("""ent0 Available 00-00-00-00-00-00
ent0 Available 00-00-00-00-00-00
ent1 Defined
ent1 Defined
ent2 Defined
ent2 Defined"""), to_bytes(""))


# Generated at 2022-06-13 00:40:10.822605
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    module = AnsibleModule(argument_spec={})
    hardwareCollector = AIXHardware(module=module)

    # execute get_device_facts() method of class AIXHardware
    device_facts = hardwareCollector.get_device_facts()

    # check if we have the device ibmveth0
    assert 'ibmveth0' in device_facts['devices']

    # check if the attribute size_mb has value 1024 for the device ibmveth0
    assert int(device_facts['devices']['ibmveth0']['attributes']['size_mb']) == 1024

    # check if we have the device hdisk0
    assert 'hdisk0' in device_facts['devices']
    # check if the attribute size_mb has value 32768 for the device hdisk0

# Generated at 2022-06-13 00:40:18.642930
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():

    class MockModule:
        def __init__(self):
            self.run_command_calls = 0
            self.run_command_results = [[0, 'proc0 Available 00-00 Processor\n' +
                                            'proc1 Available 00-01 Processor\n' +
                                            'proc1 Available 00-01 Processor\n' +
                                            'proc1 Available 00-01 Processor\n' +
                                            'proc2 Available 00-02 Processor\n', None]]

        def run_command(self, args, check_rc=True, close_fds=True, use_unsafe_shell=False):
            self.run_command_calls += 1
            return self.run_command_results.pop(0)

    module = MockModule()

    hardware = AIXHardware(module)


# Generated at 2022-06-13 00:40:24.570780
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    test_module = AnsibleModule(argument_spec=dict())
    test_obj = AIXHardware(test_module)
    test_facts = test_obj.populate()
    assert 'processor' in test_facts
    assert 'processor_cores' in test_facts
    assert 'processor_count' in test_facts


# Generated at 2022-06-13 00:40:32.687299
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    input = """
page-reclaims 59932
page-steals 0
pages-free 17062
pages-inactive 4795
pages-paging 14398
pages-pp_kernel 120463
pages-vmm_heap_sz 2048
pages-vmm_heap_sz_max 2048
pages-wired 291567
physical-memory-bytes 32988694528
physical-memory-bytes-free 688601088
swap-io-in 0
swap-io-out 0
swap-pages-in 0
swap-pages-out 0
swap-vsids-in 0
swap-vsids-out 0
"""

    expected = {'memtotal_mb': 32000, 'swaptotal_mb': 0, 'memfree_mb': 670, 'swapfree_mb': 0}

   

# Generated at 2022-06-13 00:40:44.665509
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    module = AnsibleModule(argument_spec={})
    module.exit_json = exit_json
    module.fail_json = fail_json
    module.run_command = MagicMock()

    memtotal_mb = 4096
    memfree_mb = 1024
    swaptotal_mb = 1024
    swapfree_mb = 512

    module.run_command.side_effect = [
        (0, "memory pages:         %d\nfree pages:           %d" % (memtotal_mb / 4, memfree_mb / 4), None),
        (0, "Device          1M-blocks     Used    Avail Capacity\n/dev/ada0p3        %d        0   %d     0%%" % (swaptotal_mb, swapfree_mb), None)
    ]

    hardware = AIXHardware(module)


# Generated at 2022-06-13 00:40:48.319004
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec={})
    hardware = AIXHardware(module)

    expected = {
        "processor": "PowerPC_POWER7",
        "processor_cores": 2,
        "processor_count": 2
    }

    assert hardware.get_cpu_facts() == expected


# Generated at 2022-06-13 00:40:57.276413
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    # create unix command mock
    module_mock = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    # Mocking the run_command

# Generated at 2022-06-13 00:41:04.215827
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    aix_hardware = AIXHardware(None)
    from os.path import dirname, abspath, join

    datadir = join(dirname(abspath(__file__)), 'ansible_module_facts')
    ifile = open(join(datadir, 'lsvg_output_aix71.txt'))
    lines = ifile.read()
    ifile.close()


# Generated at 2022-06-13 00:41:37.398262
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    # Simulate AIX vmstat output
    vmstat_out = '''procs              memory            page              disks             faults                 cpu
r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa  pc ec sc ov
2  1  5454   479  0  0  0  0   36   0   0   0   0  0  0  0  0  0  0  0  0  0
0  0  5454   479  0  0  0  0    0   0   1   0   0  0  0  0  0  0  0  0  0  0'''
    # Simulate AIX lsps output

# Generated at 2022-06-13 00:41:42.486633
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    """
    AIXHardware:
    - memfree_mb
    - memtotal_mb
    - swapfree_mb
    - swaptotal_mb
    - processor (a list)
    - processor_cores
    - processor_count
    """

    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils._text import to_bytes


# Generated at 2022-06-13 00:41:53.109169
# Unit test for method get_vgs_facts of class AIXHardware

# Generated at 2022-06-13 00:42:01.504487
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():

    # Initialize the class
    aix_set_data = AIXHardware()

    # For testing method get_memory_facts, create a dummy file with
    # required facts
    vmstat_out = """
     memory pages
        85100       0     83513     0.0
    seg_tab_size          524288
    """
    aix_set_data.module.run_command = lambda x, **kwargs: (0, vmstat_out, '')

    # Call the method
    mem_facts = aix_set_data.get_memory_facts()

    # Assert for validating the result
    assert 'swapfree_mb' not in mem_facts

    assert 'memtotal_mb' in mem_facts
    assert mem_facts['memtotal_mb'] == 83513


# Generated at 2022-06-13 00:42:03.801770
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    hardware_collector_obj = AIXHardwareCollector()
    assert hardware_collector_obj.platform == 'AIX'
    assert hardware_collector_obj.fact_class == AIXHardware


# Generated at 2022-06-13 00:42:08.822576
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    hardware = AIXHardware()
    hardware.module = MockModule()
    hardware.module.run_command = Mock(return_value=(0, 'test_string', ''))
    hardware.get_memory_facts()

    assert hardware.module.run_command.call_count == 2
    expected_args = [('/usr/bin/vmstat -v',),
                     ('/usr/sbin/lsps -s',)]
    hardware.module.run_command.assert_has_calls(expected_args)


# Generated at 2022-06-13 00:42:12.261465
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    module = None
    collector = AIXHardwareCollector(module)
    assert collector._platform == 'AIX'
    assert collector._fact_class == AIXHardware

# Generated at 2022-06-13 00:42:21.697844
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    from ansible.module_utils.facts.collector.hardware.aix import AIXHardware
    hardware = AIXHardware()
    hardware.module.run_command = command_mock

    hardware_facts = hardware.get_mount_facts()

# Generated at 2022-06-13 00:42:23.825219
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():

    AIXHardwareCollector.get_device_facts()



if __name__ == '__main__':
    test_AIXHardware_get_device_facts()

# Generated at 2022-06-13 00:42:26.940047
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec={})
    hardware = AIXHardware(module)
    facts = hardware.populate()

    assert facts['processor'] == 'PowerPC_POWER5'
    assert facts['processor_cores'] == 1
    assert facts['processor_count'] == 2


# Generated at 2022-06-13 00:42:58.374263
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    """
    This is a unit test for method get_memory_facts of class AIXHardware.
    """

    # Initialize test variables
    AnsibleModule = AnsibleModuleMock('aix_hardware')
    AH = AIXHardware(AnsibleModule)

    memory_facts_return_value = {'swapfree_mb': '2', 'swaptotal_mb': '3',
                                 'memfree_mb': '0', 'memtotal_mb': '1'}

    # Test with expected swap free
    memfree_mb = '0'
    memtotal_mb = '1'
    swaptotal_mb = '3'
    swapfree_mb = '2'

# Generated at 2022-06-13 00:43:03.467354
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    """
    Unit test for populate method of class AIXHardware
    """
    import os
    from ansible.module_utils.facts import fact_collector

    # define test params
    can_run_commands = True
    # disable command execution
    os.environ['ANSIBLE_RUN_COMMANDS'] = 'False'
    os.environ['ANSIBLE_NOCOWS'] = '1'
    # run code
    fact_collector.collect(can_run_commands)

# Generated at 2022-06-13 00:43:10.848729
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=False)
    hardware = AIXHardware(module=module)
    facts = hardware.populate()

    assert 'memtotal_mb' in facts
    assert 'memfree_mb' in facts
    assert 'swaptotal_mb' in facts
    assert 'swapfree_mb' in facts
    assert 'processor' in facts
    assert 'processor_cores' in facts
    assert 'processor_count' in facts
    assert 'firmware_version' in facts
    assert 'product_serial' in facts
    assert 'lpar_info' in facts
    assert 'product_name' in facts
    assert 'vgs' in facts
    assert 'mounts' in facts
    assert 'devices' in facts

# Generated at 2022-06-13 00:43:16.084836
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    module = type('', (object,), {})()
    module.run_command = lambda *args: (0, 'proc0        Available 00-00 Processor', '')
    m = AIXHardware(module)
    fact = m.get_cpu_facts()
    assert fact['processor'] == 'POWER5'
    assert fact['processor_count'] == 1
    assert fact['processor_cores'] == 1



# Generated at 2022-06-13 00:43:21.992966
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    """
    Given: a new instance of AIXHardwareCollector
    When: invoked
    Then: an instance of a HardwareCollector based class is returned
    """
    hc = AIXHardwareCollector()
    assert isinstance(hc, HardwareCollector)
    assert hc.__class__.__name__ == 'AIXHardwareCollector'



# Generated at 2022-06-13 00:43:28.026472
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    facts_module = {
        "run_command.return_value": ("", "", None),
        "get_bin_path.side_effect": lambda x: {
            "lsdev": "/usr/bin/lsdev",
            "lsattr": "/usr/bin/lsattr",
        }.get(x, "")
    }

    class AIXHardwareMock(AIXHardware):
        def __init__(self):
            self.module = MagicMock()
            self.module.configure_mock(**facts_module)
            super(AIXHardwareMock, self).__init__()

    # Output from `lsdev` command

# Generated at 2022-06-13 00:43:32.483371
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=False
    )

    # Create the instance of AIXHardwareCollector
    hw_collector = AIXHardwareCollector(module)

    # Let's test the attributes of the instance
    assert hw_collector.platform == 'AIX'
    assert hw_collector.fact_class == AIXHardware



# Generated at 2022-06-13 00:43:41.192237
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    testobj = AIXHardware()

# Generated at 2022-06-13 00:43:49.047076
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    from ansible.module_utils import basic
    from ansible.module_utils.facts import ansible_collector

    ansible_collector.collect(None)
    collector = ansible_collector._COLLECTIONS['hardware']

    if isinstance(collector, AIXHardwareCollector):
        ahw = collector._fact_class({'module': basic.AnsibleModule(argument_spec={})})
        facts = ahw.get_device_facts()['devices']
        assert len(facts) > 0
        assert 'hdisk0' in facts
        assert facts['hdisk0']['state'] == 'Available'
        assert facts['hdisk0']['attributes']['dev_size'] == '59882680'

# Generated at 2022-06-13 00:43:55.910308
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    module = AnsibleModule(argument_spec={})
    hardware = AIXHardware(module)
