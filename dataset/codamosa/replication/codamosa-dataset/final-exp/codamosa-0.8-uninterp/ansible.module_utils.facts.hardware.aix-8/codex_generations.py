

# Generated at 2022-06-13 00:35:08.154020
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    import sys
    import os
    import unittest

    class AIXHardwareTest(unittest.TestCase):
        def setUp(self):
            self.module = MockModule()

# Generated at 2022-06-13 00:35:14.646201
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    module = AnsibleModule(argument_spec={})

    hw = AIXHardware(module)
    dmi_facts = hw.get_dmi_facts()

    assert dmi_facts['firmware_version'] is not None
    assert dmi_facts['product_serial'] is not None
    assert dmi_facts['lpar_info'] is not None
    assert dmi_facts['product_name'] is not None

# Generated at 2022-06-13 00:35:21.948477
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.hardware.aix import AIXHardware
    from ansible.module_utils.facts.utils import get_file_content
    module = AnsibleModule(argument_spec={})

    # Get facts
    b_content_lsvg = to_bytes(get_file_content('./lsvg.sample.txt'))
    hardware_instance = AIXHardware(module)
    hardware_instance.module.run_command = MagicMock(return_value=(0, b_content_lsvg, ''))
    vgs_facts = hardware_instance.get_vgs_facts()

# Generated at 2022-06-13 00:35:31.503732
# Unit test for method get_vgs_facts of class AIXHardware

# Generated at 2022-06-13 00:35:41.064156
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    import sys
    import platform
    import unittest
    import mock

    if sys.version_info < (2, 7):
        import unittest2 as unittest

    with mock.patch("platform.machine"):
        test_class = AIXHardware(dict())

        def test_AIXHardware_lsdev_failed():
            with mock.patch("ansible.module_utils.facts.hardware.aix.AIXHardware.run_command", return_value=(2, '', '')) as mock_cmd:
                result = test_class.get_cpu_facts()
                mock_cmd.assert_called_with("/usr/sbin/lsdev -Cc processor")


# Generated at 2022-06-13 00:35:45.822874
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    facts = AIXHardware()
    assert facts.get_memory_facts() == {'memtotal_mb': 1048576,
                                        'memfree_mb': 400599,
                                        'swaptotal_mb': 21811,
                                        'swapfree_mb': 21506}


# Generated at 2022-06-13 00:35:57.468764
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():

    class AIXHardware_test():
        def __init__(self, device='hdisk0'):
            self.device = device
            self.facts = {}

        def run_command(self, cmd, use_unsafe_shell=False):
            out_lsattr = '''
                rw_timeout            True    False
                rq_timeout            True    False
                wq_timeout            True    False
                resize_maxfree        True    False
            '''

# Generated at 2022-06-13 00:35:59.299972
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    hw_collector = AIXHardwareCollector()
    assert hw_collector.platform == 'AIX'

# Generated at 2022-06-13 00:36:08.260240
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    out_mount_file1 = '''/dev/hd1 on / type jfs2 (log,sync)
/dev/hd4 on /var type jfs2 (log,sync)
/dev/hd2 on /tmp type jfs2 (log,sync)
/dev/hd9var on /home type jfs2 (log,sync)
/dev/hd3 on /usr type jfs2 (log,sync)
/dev/hd10opt on /opt type jfs2 (log,sync)
/dev/livedump on /var/adm/ras/livedump type jfs2 (log,sync)
'''

# Generated at 2022-06-13 00:36:18.980979
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    '''aix_mount_facts = get_mount_facts()'''


# Generated at 2022-06-13 00:36:40.783595
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    module = AnsibleModuleMock(argument_spec={})

    memory_facts = AIXHardware(module).get_memory_facts()

    assert memory_facts['memtotal_mb'] > 0
    assert memory_facts['memfree_mb'] > 0
    assert memory_facts['swaptotal_mb'] > 0
    assert memory_facts['swapfree_mb'] > 0



# Generated at 2022-06-13 00:36:52.140221
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    module = AnsibleModule(argument_spec={})
    hardware = AIXHardware(module)
    device_facts = hardware.get_device_facts()
    assert isinstance(device_facts, dict)
    assert 'devices' in device_facts
    assert isinstance(device_facts['devices'], dict)
    assert 'ent0' in device_facts['devices']
    assert 'state' in device_facts['devices']['ent0']
    assert 'type' in device_facts['devices']['ent0']
    assert 'attributes' in device_facts['devices']['ent0']
    assert isinstance(device_facts['devices']['ent0']['attributes'], dict)

# Generated at 2022-06-13 00:36:59.320724
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    test_obj = AIXHardware()

    def run_command(*args, **kwargs):
        return 0, 'Available    SMP PROCESSOR 0 Available    00-00\n' \
                  'Available    SMP PROCESSOR 1 Available    00-01\n', ''

    test_obj.module.run_command = run_command

    expected_result = {'processor': 'PowerPC_POWER6', 'processor_cores': 1, 'processor_count': 2}
    assert expected_result == test_obj.get_cpu_facts()



# Generated at 2022-06-13 00:37:10.529114
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    """
    Test method get_device_facts of class AIXHardware
    """
    fake_module = FakeModule()
    test_obj = AIXHardware(fake_module)

    expected_device_facts = {
        'devices': {
            'hdisk0': {
                'attributes': {},
                'state': 'Available',
                'type': 'Virtual SCSI Disk Drive'
            }
        }
    }

    fake_module.run_command_args = [
        [
            'lsdev',
            '-Cc',
            'disk'
        ],
        [
            'lsattr',
            '-E',
            '-l',
            'hdisk0'
        ]
    ]

    fake_module.run_command_rcs = [
        0,
        0
    ]

   

# Generated at 2022-06-13 00:37:20.020874
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    module = AnsibleModule(argument_spec=dict())
    hardware = AIXHardware(module)
    rc, out, err = module.run_command("cat /proc/mounts", use_unsafe_shell=True)
    mount_facts = hardware.get_mount_facts()
    x = re.search('\s+'.join([
        r'^(/[^\s]+)\s+([^\s]+)\s+(.+?)\s+(.+?)\s+(\d+)\s+(\d+)\s+(.+)$',
        r'^(/[^\s]+)\s+([^\s]+)\s+(.+?)\s+(.+?)\s+(\d+)\s+(\d+)\s+(.+)$']),
                  out, re.MULTILINE)
    assert x

# Generated at 2022-06-13 00:37:31.203658
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    module = AnsibleModule(
        argument_spec=dict(
            filter=dict(required=False, type='list')
        ),
        supports_check_mode=True
    )

    set_module_args(dict(filter=['*']))

    aixhw_obj = AIXHardware()
    result = aixhw_obj.get_mount_facts()

    # Return value should be dict with key mounts
    assert result.get('mounts') is not None, "Could not get mount facts"

    # Now check that mount info is correct
    dev_fs = ''

# Generated at 2022-06-13 00:37:42.064667
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    module = DummyModule()
    hardware = AIXHardware(module)
    collected_facts = {}
    collected_facts = hardware.populate()
    assert collected_facts['firmware_version'] == '6.1.6.0'
    assert collected_facts['product_serial'] == 'LZ0AC3A'
    assert collected_facts['lpar_info'] == '1 8 0'
    assert collected_facts['product_name'] == '0187A33'
    assert collected_facts['swaptotal_mb'] == 1
    assert collected_facts['swapfree_mb'] == 1
    assert collected_facts['memtotal_mb'] == 4088
    assert collected_facts['memfree_mb'] == 3494


# Unit tests for method get_memory_facts of class AIXHardware

# Generated at 2022-06-13 00:37:44.881866
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    module = AnsibleModule(argument_spec=dict())
    hardware = AIXHardware(module)
    assert hardware.get_mount_facts() == {'mounts': [{'mount': '/', 'fstype': 'jfs2'}]}


# Generated at 2022-06-13 00:37:48.072514
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    AIXHardware.module = AnsibleModule(argument_spec={})
    AIXHardware.module.run_command = lambda *args, **kwargs: (0, 'IBM,8247-21L', '')
    dmi_facts = AIXHardware.get_dmi_facts()
    assert 'firmware_version' in dmi_facts
    assert 'product_name' in dmi_facts
    assert 'lpar_info' in dmi_facts
    assert dmi_facts['firmware_version'] == '8247-21L'



# Generated at 2022-06-13 00:37:53.064371
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    class AnsibleModule:
        def __init__(self):
            self.params = {'test_method': 'get_device_facts'}
            self.run_command_environ_update = {}


# Generated at 2022-06-13 00:38:32.906616
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    aix_hw_collector = AIXHardwareCollector()
    assert aix_hw_collector._platform == 'AIX'
    assert aix_hw_collector._fact_class == AIXHardware
    assert isinstance(aix_hw_collector._fact_class(), AIXHardware)


# Generated at 2022-06-13 00:38:38.593880
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    aixhw = AIXHardware({})
    collected_facts = {'ansible_os_family': 'AIX'}
    output = aixhw.populate(collected_facts)
    assert output['processor_cores'] == output['processor_count']
    assert type(output['processor_cores']) == int
    assert type(output['processor_count']) == int


# Generated at 2022-06-13 00:38:41.311523
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    x = AIXHardwareCollector()
    assert x.platform == 'AIX'
    assert x.fact_class == AIXHardware

# Generated at 2022-06-13 00:38:52.722189
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec={})
    ah = AIXHardware(module)

    rc, out, err = ah.module.run_command("/usr/sbin/lsdev -Cc processor")
    if out:
        i = 0
        for line in out.splitlines():
            if 'Available' in line:
                if i == 0:
                    data = line.split(' ')
                    cpudev = data[0]
                i += 1
            cpu_facts = {'processor_count': int(i)}

            rc, out, err = ah.module.run_command("/usr/sbin/lsattr -El " + cpudev + " -a type")
            data = out.split(' ')
            cpu_facts['processor'] = data[1]

            rc, out, err = ah.module

# Generated at 2022-06-13 00:38:55.691918
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    module = AnsibleModule(argument_spec={})
    hardware = AIXHardware(module=module)
    dmi_facts = hardware.get_dmi_facts()
    assert dmi_facts['firmware_version']
    assert dmi_facts['product_serial']
    assert dmi_facts['product_name']
    assert dmi_facts['lpar_info']

# Generated at 2022-06-13 00:38:58.099630
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    collector = AIXHardwareCollector()
    assert collector.platform == 'AIX'
    assert collector._fact_class.platform == 'AIX'


# Generated at 2022-06-13 00:39:08.540677
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    module = AnsibleModule(argument_spec={})
    facts = AIXHardware(module).populate()

    assert facts['mounts'] is not None
    for m in facts['mounts']:
        assert m['mount'] is not None
        assert m['device'] is not None
        assert m['fstype'] is not None
        assert m['options'] is not None
        assert m['time'] is not None
        assert m['size_total'] is not None
        assert m['size_used'] is not None
        assert m['size_available'] is not None
        assert m['size_percent'] is not None



# Generated at 2022-06-13 00:39:19.155300
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():

    class FakeModule:
        def get_bin_path(self, exe, required=True):
            return '/usr/sbin/' + exe

        def run_command(self, cmd):
            return 0, "", ""

    mount_facts = {}
    hw = AIXHardware(FakeModule())
    mount_facts = hw.get_mount_facts()

    if mount_facts['mounts']:
        print("Received mounts:")
        for mount in mount_facts['mounts']:
            print("%s" % mount)
    else:
        raise Exception("test_AIXHardware_get_mount_facts: failed, no mount")

if __name__ == '__main__':
    test_AIXHardware_get_mount_facts()

# Generated at 2022-06-13 00:39:20.633935
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    collector = AIXHardwareCollector()
    assert collector._platform == 'AIX'
    assert collector._fact_class == AIXHardware


# Generated at 2022-06-13 00:39:31.421848
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    """
    Tests get_mount_facts method of AIXHardware class.
        :return: None
    """
    """
    Tests get_mount_facts method of AIXHardware class.
        :return: None
    """
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.hardware.aix import AIXHardware
    from ansible.module_utils.six import StringIO
    test_obj = AIXHardware()

    # Test-case: For all sub-tests, mount output serves as input to test.
    # This output sourced from https://www.ibm.com/support/knowledgecenter/ssw_aix_72/com.ibm.aix.cmds5/mount.htm

# Generated at 2022-06-13 00:40:49.384502
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    hardware = AIXHardware()

    vgs_facts = hardware.get_vgs_facts()
    assert vgs_facts['vgs']['rootvg'][0]['pv_name'] == 'hdisk0'
    assert vgs_facts['vgs']['rootvg'][1]['pv_name'] == 'hdisk1'
    assert vgs_facts['vgs']['realsyncvg'][0]['pv_name'] == 'hdisk74'
    assert vgs_facts['vgs']['testvg'][0]['pv_name'] == 'hdisk105'
    assert vgs_facts['vgs']['testvg'][1]['pv_name'] == 'hdisk106'

# Generated at 2022-06-13 00:40:52.589675
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    import sys

    module = sys.modules['ansible.module_utils.facts.hardware.aix']

    hw_facts = AIXHardware()
    hw_facts._module = module
    hw_facts.populate()



# Generated at 2022-06-13 00:41:00.166122
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    class module():
        def __init__(self, params=None, check_mode=None, module_arg_spec=None, use_unsafe_shell=None):
            self.params = params
            self.check_mode = check_mode
            self.module_arg_spec = module_arg_spec
            self.use_unsafe_shell = use_unsafe_shell

        def get_bin_path(self, executable, required=False):
            if 'lsconf' in executable:
                return "/usr/sbin/lsconf"
            return None

        def run_command(self, command):
            return 0, "Machine Serial Number: YLZ-D20000\nLPAR Info: 1 12 NOT AVAILABLE\nSystem Model: IBM,8201-E4B\n", ""


# Generated at 2022-06-13 00:41:09.293677
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    # test data
    out = """rootvg:
    PV_NAME           PV STATE          TOTAL PPs   FREE PPs    FREE DISTRIBUTION
    hdisk0            active            546         0           00..00..00..00..00
    hdisk1            active            546         113         00..00..00..21..92
    realsyncvg:
    PV_NAME           PV STATE          TOTAL PPs   FREE PPs    FREE DISTRIBUTION
    hdisk74           active            1999        6           00..00..00..00..06
    testvg:
    PV_NAME           PV STATE          TOTAL PPs   FREE PPs    FREE DISTRIBUTION
    hdisk105          active            999         838         200..39..199..200..200
    hdisk106          active            999         599         200..00..00..199..200"""

   

# Generated at 2022-06-13 00:41:17.589294
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    aix_hw = AIXHardware()
    memory_facts = aix_hw.get_memory_facts()
    assert 'memtotal_mb' in memory_facts
    assert isinstance(memory_facts['memtotal_mb'], int)
    assert 'memfree_mb' in memory_facts
    assert isinstance(memory_facts['memfree_mb'], int)
    assert 'swaptotal_mb' in memory_facts
    assert isinstance(memory_facts['swaptotal_mb'], int)
    assert 'swapfree_mb' in memory_facts
    assert isinstance(memory_facts['swapfree_mb'], int)

# Generated at 2022-06-13 00:41:21.119397
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    # create the instance
    aix_hw = AIXHardware()

    # get the facts from the instance
    facts = aix_hw.get_cpu_facts()
    assert facts['processor']
    assert facts['processor_cores']
    assert facts['processor_count']



# Generated at 2022-06-13 00:41:25.640132
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    test_AIXHardware = AIXHardware()
    assert test_AIXHardware.get_memory_facts() == {
        'memtotal_mb': 8192,
        'memfree_mb': 8191,
        'swapfree_mb': 0,
        'swaptotal_mb': 0
    }, 'did not return expected memory facts'



# Generated at 2022-06-13 00:41:28.759436
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    hw = AIXHardwareCollector()
    assert hw.fact_class == AIXHardware
    assert hw.platform == 'AIX'

# Generated at 2022-06-13 00:41:33.781436
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    aix_hw = AIXHardware({})
    dmi_facts = aix_hw.get_dmi_facts()
    assert('product_serial' in dmi_facts)
    assert('firmware_version' in dmi_facts)
    assert('product_name' in dmi_facts)



# Generated at 2022-06-13 00:41:41.505764
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    module = AnsibleModule(
        argument_spec = dict()
    )

    hardware = AIXHardware(module)

# Generated at 2022-06-13 00:44:22.297710
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    params = {}
    module = AnsibleModule(argument_spec={})
    hardware = AIXHardware()
    hardware.module = module
    hardware.populate()
    vgs_facts = hardware.get_vgs_facts()

# Generated at 2022-06-13 00:44:31.025111
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    class MockModule:
        def __init__(self, run_command_results):
            self.run_command_results = run_command_results
            self.run_command_calls = []

        def run_command(self, cmd, use_unsafe_shell=False):
            self.run_command_calls.append(cmd)
            return self.run_command_results.pop(0)


# Generated at 2022-06-13 00:44:32.817731
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    hardware_collector = AIXHardwareCollector()
    assert hardware_collector._platform == 'AIX'
    assert hardware_collector._fact_class == AIXHardware

# Generated at 2022-06-13 00:44:39.780531
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    import platform
    import sys
    import tempfile
    import os
    import shutil
    import re
    import json

    # Create a temporary directory
    tmpdir = tempfile.mkdtemp()

    # Create a temporary python module
    module = os.path.join(tmpdir, 'ansible_test_utils.py')
    f = open(module, 'w')