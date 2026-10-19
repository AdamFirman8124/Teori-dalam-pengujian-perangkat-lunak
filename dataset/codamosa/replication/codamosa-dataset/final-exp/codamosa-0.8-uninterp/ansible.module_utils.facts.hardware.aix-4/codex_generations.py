

# Generated at 2022-06-13 00:35:05.290484
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    hardware = AIXHardware()
    hardware.module = MockModule()

    cpu_facts = hardware.get_cpu_facts()

    assert cpu_facts['processor'] == 'PowerPC_POWER7'
    assert cpu_facts['processor_count'] == 4
    assert cpu_facts['processor_cores'] == 2


# Generated at 2022-06-13 00:35:16.777292
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    from ansible.module_utils.facts.hardware.aix import AIXHardware
    aixhw = AIXHardware()

    # Simple class with one method for mocking
    class test_aixhw(object):
        class module(object):
            def run_command(cmd):
                # Return a mocked result depend on command
                if cmd == "/usr/sbin/lsattr -El sys0 -a fwversion":
                    return 0, 'fwversion IBM,8233-E8B', ''
                elif cmd == "lsconf":
                    return 0, 'Machine Serial Number: 06B123456789\nLPAR Info: 5BFF\nSystem Model: IBM,8233-E8B\n', ''
                else:
                    return 1, '', ''
    aixhw.module = test_aixhw.module

   

# Generated at 2022-06-13 00:35:26.947749
# Unit test for method get_vgs_facts of class AIXHardware

# Generated at 2022-06-13 00:35:32.208353
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    facts = AIXHardware()
    facts.module.run_command = lambda args, **kwargs: (0, 'memory pages: 264947\nfree pages:    79070\n', None)
    facts.get_memory_facts()
    assert facts.facts['memtotal_mb'] == 107161
    assert facts.facts['memfree_mb'] == 31858



# Generated at 2022-06-13 00:35:41.705944
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    hostname = 'platform_AIX_test'
    # return values
    test_AIXHardware_get_dmi_facts.lsconf_path = '/usr/bin/lsconf'
    test_AIXHardware_get_dmi_facts.stdout = 'Machine Type: 8408-E8D\nMachine Serial Number: 00FJ6D4\nLPAR Info: 8ETC-VM-U01\nSystem Model: IBM,8408-E8D\n'
    test_AIXHardware_get_dmi_facts.stderr = ''
    test_AIXHardware_get_dmi_facts.rc = 0
    # mock module
    class MockAIXModule():
        def __init__(self):
            self.params = {'id': 0}


# Generated at 2022-06-13 00:35:54.035532
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    """ Unit test for method get_device_facts of class AIXHardware """
    import os
    import ansible.module_utils.facts.collector
    import ansible.module_utils.facts.hardware.aix
    import unittest

    module_mock = ansible.module_utils.facts.collector.ModuleMock()
    module_mock.run_command = lambda fs_cmd: (0, fs_cmd, '')
    module_mock.get_bin_path = lambda fs_cmd, required: "test"
    class_aix_hardware = ansible.module_utils.facts.hardware.aix.AIXHardware(module_mock)

    expected_key_names = ['state', 'type', 'attributes']

# Generated at 2022-06-13 00:36:02.211606
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    class ModuleDouble(object):
        def get_bin_path(self, cmd, required=False):
            return cmd

        def run_command(self, cmd, use_unsafe_shell=False):
            return 0, SAMPLE_MOUNT_OUTPUT, ""

    sample_obj = AIXHardware(ModuleDouble())
    res = sample_obj.get_mount_facts()

    assert res['mounts'][0]['mount'] == '/'
    assert res['mounts'][0]['device'] == '/dev/hd4'
    assert res['mounts'][0]['fstype'] == 'jfs'
    assert res['mounts'][0]['options'] == 'rw,log='
    assert res['mounts'][0]['time'] == 'Apr28'


# Generated at 2022-06-13 00:36:07.398524
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec={})
    ah = AIXHardware(module)
    rc, out, err = module.run_command("/usr/sbin/lsdev -Cc processor")
    cpu_facts = ah.get_cpu_facts()
    assert cpu_facts['processor'] == 'PowerPC_POWER7'
    assert cpu_facts['processor_count'] == 2
    assert cpu_facts['processor_cores'] == 1



# Generated at 2022-06-13 00:36:12.820845
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec=dict())
    hardware = AIXHardware(module)
    cpu_facts = hardware.get_cpu_facts()
    assert isinstance(cpu_facts['processor_cores'], int)
    assert isinstance(cpu_facts['processor_count'], int)
    assert cpu_facts['processor'] is not None


# Generated at 2022-06-13 00:36:17.750104
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec={})
    obj = AIXHardware(module)
    cpu_facts = {'processor': 'PowerPC_POWER9',
                 'processor_cores': 4,
                 'processor_count': 2}
    assert obj.get_cpu_facts() == cpu_facts


# Generated at 2022-06-13 00:36:51.336081
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    module = AnsibleModule(argument_spec={})
    cmd = module.get_bin_path('lsdev', True)

# Generated at 2022-06-13 00:36:53.556433
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    aix_hardware = AIXHardware(None)
    assert aix_hardware.get_memory_facts()['memtotal_mb'] == 32000

# Generated at 2022-06-13 00:37:01.451887
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    # it is needed to mock module_utils.facts.hardware.base.Hardware class
    module_utils_facts_hardware_base_Hardware = Hardware


# Generated at 2022-06-13 00:37:07.222035
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec={})
    hardware = AIXHardware(module)

    expected_cpu_facts = {'processor': u'POWER7+',
                          'processor_cores': 4,
                          'processor_count': 2}
    assert expected_cpu_facts == hardware.get_cpu_facts()


# Generated at 2022-06-13 00:37:17.576028
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    from ansible.module_utils.facts import Adapter
    from ansible.module_utils.facts.system.aix import AIXHardware

    fake_module = Adapter(command_timeout=15, connection_timeout=10, become_method=None, become_user=None)
    fake_module.get_bin_path = lambda x: x

# Generated at 2022-06-13 00:37:18.902950
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    test_hwcollector = AIXHardwareCollector()
    assert test_hwcollector.platform == AIXHardwareCollector._platform
    assert test_hwcollector.fact_class == AIXHardwareCollector._fact_class

# Generated at 2022-06-13 00:37:22.607966
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec={})
    module.exit_json = exit_json
    aix_hardware_obj = AIXHardware(module)
    cpu_facts = aix_hardware_obj.get_cpu_facts()
    assert cpu_facts['processor_cores'] < cpu_facts['processor_count']



# Generated at 2022-06-13 00:37:32.891520
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    module = MockModule()
    hardware = AIXHardware(module)

# Generated at 2022-06-13 00:37:39.287133
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    mod = AnsibleModule(
        argument_spec={},
        supports_check_mode=False
    )
    hardware = AIXHardware(mod)
    cpufacts = hardware.get_cpu_facts()
    assert cpufacts['processor'] is not None
    assert cpufacts['processor_cores'] is not None
    assert cpufacts['processor_count'] is not None


# Generated at 2022-06-13 00:37:47.038122
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():

    class Options(object):
        def __init__(self):
            self.remote_user = 'root'
            self._ansible_no_log = True

    class FakeModule(object):
        def __init__(self):
            self.options = Options()
            self.run_command = mock.MagicMock(return_value=(0, 'success', None))
            self.get_bin_path = mock.MagicMock(return_value='')

    device_facts = {}

# Generated at 2022-06-13 00:38:15.424180
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=['!all'], type='list'),
        ),
        supports_check_mode=True,
    )
    ah = AIXHardware(module=module)

    cpu_facts = ah.get_cpu_facts()
    assert cpu_facts['processor_cores'] == 4
    assert cpu_facts['processor'] == 'PowerPC_POWER8'
    assert cpu_facts['processor_count'] == 24



# Generated at 2022-06-13 00:38:16.714103
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    collector = AIXHardwareCollector()
    assert Collector is not None
    assert Collector.platform == 'AIX'

# Generated at 2022-06-13 00:38:27.280847
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    module = AnsibleModule(argument_spec={})
    hardware = AIXHardware(module)

    module.run_command = Mock(return_value=(0, MOCK_VMSTAT_OUT, ''))

    memory_facts = hardware.get_memory_facts()
    assert 'memtotal_mb' in memory_facts
    assert memory_facts['memtotal_mb'] == 3873
    assert 'memfree_mb' in memory_facts
    assert memory_facts['memfree_mb'] == 3690
    assert 'swaptotal_mb' in memory_facts
    assert memory_facts['swaptotal_mb'] == 2048
    assert 'swapfree_mb' in memory_facts
    assert memory_facts['swapfree_mb'] == 1483



# Generated at 2022-06-13 00:38:29.307630
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    collector = AIXHardwareCollector()
    assert collector._platform == 'AIX'
    assert collector._fact_class == AIXHardware

# Generated at 2022-06-13 00:38:41.059568
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    module = AnsibleModule(argument_spec={})
    hardware = AIXHardware(module=module)
    cpu_facts = hardware.get_cpu_facts()
    assert 'processor' in cpu_facts
    assert 'processor_count' in cpu_facts
    assert 'processor_cores' in cpu_facts
    memory_facts = hardware.get_memory_facts()
    assert 'memtotal_mb' in memory_facts
    assert 'memfree_mb' in memory_facts
    assert 'swaptotal_mb' in memory_facts
    assert 'swapfree_mb' in memory_facts
    dmi_facts = hardware.get_dmi_facts()
    assert 'firmware_version' in dmi_facts
    assert 'product_serial' in dmi_facts
    assert 'lpar_info' in dmi_facts

# Generated at 2022-06-13 00:38:45.368471
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    from ansible.module_utils.facts.hardware.aix import AIXHardware
    from ansible.module_utils.facts.hardware.aix import test_get_mount_facts as test_ansible_aix_mount_facts
    aix_hw = AIXHardware()
    assert test_ansible_aix_mount_facts(aix_hw.get_mount_facts())

# Generated at 2022-06-13 00:38:55.055829
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    hardware = AIXHardware()
    hardware.module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    memory_facts = hardware.get_memory_facts()
    assert memory_facts['memfree_mb'] == 0
    assert memory_facts['memtotal_mb'] == 0
    assert memory_facts['swapfree_mb'] == 0
    assert memory_facts['swaptotal_mb'] == 0
    assert len(memory_facts['processor']) == 0
    assert memory_facts['processor_cores'] == 0
    assert memory_facts['processor_count'] == 0


# Generated at 2022-06-13 00:39:03.208312
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    """Class AIXHardware: _get_memory_facts()"""

    # Mock class for module running
    class MockModule:
        # Properties
        params = {
            'gather_subset': ['!config', 'min']
        }

        # Runs a command and returns stdout, rc and byte stderr
        def run_command(self, cmd, use_unsafe_shell=False):
            # For test purposes, this method returns
            # the following values:
            #
            # cmd and args: commands must include the command called,
            # its arguments and a return code
            #
            # stdout: output of command
            #
            # stderr: error message in bytes
            #
            # stderr_text: error message in string
            cmd = ['/usr/bin/vmstat']

# Generated at 2022-06-13 00:39:15.507835
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    module = AnsibleModule(argument_spec={})
    hwobj = AIXHardware(module)
    lsvg_path = 'tests/unit/module_utils/facts/hardware/aix_lsvg'
    xargs_path = 'tests/unit/module_utils/facts/hardware/aix_xargs'
    vgs_facts = {}
    vgs_facts['vgs'] = {}

# Generated at 2022-06-13 00:39:23.835979
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    """Test method get_memory_facts of class AIXHardware

    Test input and expected result are from

    http://www.ibm.com/support/knowledgecenter/ssw_aix_72/com.ibm.aix.cmds4/vmstat.htm
    """


# Generated at 2022-06-13 00:39:53.530835
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    Hardware.module = MagicMock()
    Hardware.module.run_command.return_value = 0, 'memory pages: 30000\nfree pages: 2000', ''
    ah = AIXHardware()
    memory_facts = ah.get_memory_facts()
    assert memory_facts['memfree_mb'] == 2000 * 4096 // 1024 // 1024
    assert memory_facts['memtotal_mb'] == 30000 * 4096 // 1024 // 1024

# Generated at 2022-06-13 00:40:03.871613
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    device_facts = {}
    device_facts['devices'] = {}


# Generated at 2022-06-13 00:40:08.461934
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=['!all', '!min'], type='list')
        ),
        supports_check_mode=True
    )

    result = AIXHardware(module).populate()
    assert 'memtotal_mb' in result
    assert 'memfree_mb' in result
    assert 'swaptotal_mb' in result
    assert 'swapfree_mb' in result



# Generated at 2022-06-13 00:40:13.581495
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    A = AIXHardware()
    out = A.populate()
    assert type(out) is dict
    assert 'processor_count' in out.keys()
    assert 'memtotal_mb' in out.keys()
    assert 'memfree_mb' in out.keys()
    assert 'firmware_version' in out.keys()
    assert 'vgs' in out.keys()


# Generated at 2022-06-13 00:40:20.333214
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    class ModuleStub(object):
        def __init__(self, out):
            self.out = out

        def run_command(self, cmd):
            return 0, self.out, ''


# Generated at 2022-06-13 00:40:30.566407
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    # Create a dummy module which is required to
    # instantiate a instance of Hardware class
    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )
    mock_module = Mock(module)

    # instantiate AIXHardware class
    aix_hw = AIXHardware(mock_module)
    aix_hw.populate()

    # Assert that facts were populated
    assert aix_hw.facts['processor'][0] == 'PowerPC_POWER8'
    assert aix_hw.facts['processor_cores'] == 48
    assert aix_hw.facts['processor_count'] == 2
    assert aix_hw.facts['memtotal_mb'] > 0
    assert aix_hw.facts['memfree_mb'] > 0
    assert aix_hw

# Generated at 2022-06-13 00:40:42.310534
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    def lsdev_side_effect(ignore):
        return 0, \
               '''hdisk0 Available 00-00-01-2,0
hdisk1 Available 00-01-01
ent0 Available Virtual I/O Ethernet Adapter (l-lan)
ent0 Available Virtual I/O Ethernet Adapter (l-lan)
ent0 Available Virtual I/O Ethernet Adapter (l-lan)
ent0 Available Virtual I/O Ethernet Adapter (l-lan)''', ''


# Generated at 2022-06-13 00:40:45.372018
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    hw = AIXHardwareCollector()
    assert isinstance(hw, HardwareCollector), 'isinstance(AIXHardwareCollector(), HardwareCollector) == True'

# Generated at 2022-06-13 00:40:55.413505
# Unit test for method get_mount_facts of class AIXHardware

# Generated at 2022-06-13 00:40:59.469420
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    module = AnsibleModule(argument_spec={})

    aix_facts = AIXHardware()

    rc, out, err = aix_facts.module.run_command("/usr/sbin/lsattr -El sys0 -a fwversion")
    aix_facts.module.exit_json(changed=False, ansible_facts={'dmi_facts': aix_facts.get_dmi_facts()})



# Generated at 2022-06-13 00:41:36.366852
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    module = AnsibleModule(argument_spec={}, supports_check_mode=False)
    hardware = AIXHardware(module)

    lsvg_path = hardware.module.get_bin_path("lsvg")
    xargs_path = hardware.module.get_bin_path("xargs")
    if not lsvg_path or not xargs_path:
        module.fail_json(msg="Commands 'lsvg' and/or 'xargs' not found")

    cmd = "%s -o | %s %s -p" % (lsvg_path, xargs_path, lsvg_path)
    rc, out, err = module.run_command(cmd, use_unsafe_shell=True)
    if rc == 0 and out:
        vgs_facts = {}

# Generated at 2022-06-13 00:41:42.896258
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    module = AnsibleModule(argument_spec={})

    hardware = AIXHardware(module=module)

    hardware_facts = hardware.populate()

    assert hardware_facts['firmware_version'] is not None
    assert hardware_facts['lpar_info'] is not None
    assert hardware_facts['processor'] is not None
    assert hardware_facts['processor_cores'] is not None
    assert hardware_facts['processor_count'] is not None
    assert hardware_facts['product_name'] is not None
    assert hardware_facts['product_serial'] is not None
    assert hardware_facts['vgs'] is not None
    assert hardware_facts['devices'] is not None


if __name__ == '__main__':
    from ansible.module_utils.basic import *
    main()

# Generated at 2022-06-13 00:41:53.644659
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    """
    Unit test for method get_device_facts of class AIXHardware
    """

    # Create a fake module
    module = DummyModule()

    # Create an AIXHardware object
    aix_hardware_obj = AIXHardware(module)

    # Create a fake output from command line
    lsdev_cmd = aix_hardware_obj.module.get_bin_path('lsdev', True)
    lsattr_cmd = aix_hardware_obj.module.get_bin_path('lsattr', True)


# Generated at 2022-06-13 00:42:01.880040
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    from ansible.module_utils.facts.hardware.aix import AIXHardware

    module = AnsibleModule(argument_spec={})
    hardware = AIXHardware(module)

    vgs_facts = hardware.get_vgs_facts()
    assert vgs_facts['vgs']['rootvg'][0]['pv_name'] == 'hdisk0'
    assert vgs_facts['vgs']['rootvg'][0]['total_pps'] == '546'
    assert vgs_facts['vgs']['rootvg'][1]['pv_name'] == 'hdisk1'
    assert vgs_facts['vgs']['rootvg'][1]['total_pps'] == '546'

# Generated at 2022-06-13 00:42:09.513808
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    from ansible.module_utils.facts.hardware.aix import AIXHardware
    from ansible.module_utils.facts import cached
    from ansible.module_utils.facts.utils import get_file_content
    from ansible.module_utils.facts.collector import BaseFileCacheCollector
    import json
    import os
    import shlex
    import sys

    class _Module:
        class _Command:
            def __init__(self, path, return_code, stdout, stderr):
                self._path = path
                self._return_code = return_code
                self._stdout = stdout
                self._stderr = stderr

            def run_command(self, cmd, use_unsafe_shell=None, check_rc=None):
                cmd = shlex.split(cmd)


# Generated at 2022-06-13 00:42:13.241762
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    aix_hardware = AIXHardware()
    assert aix_hardware.get_memory_facts() == {'memfree_mb': 943, 'memtotal_mb': 1007, 'swapfree_mb': 0, 'swaptotal_mb': 0}


# Generated at 2022-06-13 00:42:21.128714
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    """
    Test method get_dmi_facts of class AIXHardware.
    """
    module = AnsibleModule(argument_spec={})
    hardware = AIXHardware()
    hardware.module = module

    out = StringIO()
    out.write('firmware_version:IBM,1A143B')
    out.seek(0)
    module.run_command = MagicMock(return_value=(0, out.read(), ''))
    dmi_facts = hardware.get_dmi_facts()
    assert dmi_facts["firmware_version"] == 'IBM,1A143B'
    out.close()

# Generated at 2022-06-13 00:42:26.041590
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    module = AnsibleModule(argument_spec={})
    hardware = AIXHardware(module)
    hardware.populate()
    assert hardware.facts['processor_count'] > 0
    assert 'processor_cores' in hardware.facts
    assert hardware.facts['memtotal_mb'] > 0
    assert hardware.facts['memfree_mb'] > 0
    assert hardware.facts['mounts']
    assert hardware.facts['vgs']
    assert hardware.facts['firmware_version']

# Generated at 2022-06-13 00:42:33.004789
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    mount_facts = AIXHardware.get_mount_facts(AIXHardware)

    assert mount_facts['mounts'][0]['mount'] == '/dev/hd4'
    assert mount_facts['mounts'][0]['device'] == 'hd4'
    assert mount_facts['mounts'][0]['fstype'] == 'jfs2'
    assert mount_facts['mounts'][0]['options'] == 'rw,log=/dev/hd8'
    assert mount_facts['mounts'][0]['time'] == 'Thu Jan  5 13:02:26 2017'
    assert mount_facts['mounts'][0]['size_available'] == 0
    assert mount_facts['mounts'][0]['size_total'] == 0

    assert mount_facts['mounts'][1]['mount']

# Generated at 2022-06-13 00:42:42.393803
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )


# Generated at 2022-06-13 00:43:46.129345
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.hardware.aix import AIXHardware
    mem_facts = AIXHardware().get_memory_facts()
    assert mem_facts['memtotal_mb'] > 0
    assert mem_facts['memfree_mb'] > 0
    assert mem_facts['swaptotal_mb'] > 0
    assert mem_facts['swapfree_mb'] > 0


# Generated at 2022-06-13 00:43:53.340892
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    AIXHardware.module = None
    AIXHardware.module = MagicMock()
    AIXHardware.module.run_command.return_value = (0, '', '')

# Generated at 2022-06-13 00:43:59.331908
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    module_mock = AnsibleModuleMock()
    lsvg_mock = "/usr/sbin/lsvg"
    xargs_mock = "/usr/bin/xargs"

# Generated at 2022-06-13 00:44:08.151044
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    module = AnsibleModule(
        argument_spec={
            'gather_subset': dict(default=[], type='list')
        }
    )

    fake_module = type("module", (object,), {
        "run_command": run_command,
        "get_bin_path": my_get_bin_path
    })

    aix_hardware = AIXHardware(fake_module)
    dmi_facts = aix_hardware.get_dmi_facts()

    assert dmi_facts['product_serial'] == '12345'
    assert dmi_facts['lpar_info'] == 'test lpar'
    assert dmi_facts['firmware_version'] == '1.1'
    assert dmi_facts['product_name'] == 'test product'



# Generated at 2022-06-13 00:44:15.751122
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    """
    ansible-test units --python -v --junit --debug test_utils.py just
    """

    from ansible.module_utils.facts.hardware.aix import AIXHardware
    import sys
    import os
    import tempfile
    from ansible.module_utils._text import to_bytes


# Generated at 2022-06-13 00:44:25.721209
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=['!all'], type='list')
        ),
        supports_check_mode=True
    )

    if not HAS_AIX_MODULES:
        module.fail_json(msg='There is no AIX modules installed')

    inv_data = Hardware(module).populate()
    cpu_facts = AIXHardware.get_cpu_facts()
    memory_facts = AIXHardware.get_memory_facts()
    dmi_facts = AIXHardware.get_dmi_facts()
    vgs_facts = AIXHardware.get_vgs_facts()
    mount_facts = AIXHardware.get_mount_facts()
    devices_facts = AIXHardware.get_device_facts()


# Generated at 2022-06-13 00:44:33.972610
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    module = AnsibleModuleMock()
    hardware = AIXHardware(module)

    output_lsdev = '''
    name status description
    fcs0 Available 16/4 FC Adapter
    fscsi0 Available 16/4 FC SCSI I/F
    hdisk0 Available 9133-55A ST9500423AS        
    mem0 Available  16384 MB memory
    mem1 Available  24576 MB memory
    mem2 Available  32768 MB memory
    mem3 Available  16384 MB memory
    proc0 Available  Processors
    proc4 Available  Processors
    proc8 Available  Processors
    vscsi0 Available Virtual SCSI Client Adapter
    '''


# Generated at 2022-06-13 00:44:41.408897
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    # Put in a fake module
    module = type('Module', (object,), {'run_command': fake_run_command})
    # Get module object for aix
    mod_obj = AIXHardware(module=module)

    # test method populate using a fake lsdev output