

# Generated at 2022-06-13 00:35:08.001544
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )


# Generated at 2022-06-13 00:35:18.349792
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    module = AnsibleModule(argument_spec={})
    hardware = AIXHardware()

    # Case when mount does not exist
    # In that case, mount command output is like...
    # Error: mount: 0042-056 Cannot mount /dev/cd0 on /cdrom. : A file or directory in the path name does not exist.
    mount_out = 'Error: %s\n' % hardware.module.get_bin_path('mount')

    hardware.module.run_command = lambda cmd: (0, mount_out, None)
    result = hardware.get_mount_facts()
    assert result == {'mounts': []}

    # Case when mount exists
    # In that case, mount command output is like...
    # /:
    # /dev/hd1 on / (jfs2)
    # /dev/hd

# Generated at 2022-06-13 00:35:28.786229
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    testargs = ['ansible-test_AIXHardware_get_dmi_facts', '--tree', '{}/tests/files/', '--args', 'lsattr -El sys0 -a fwversion', '--args', 'lsconf']

    from ansible.modules.system import dmi
    from ansible.module_utils.facts.hardware.aix import AIXHardware
    from ansible.module_utils._text import to_bytes

    AIXHardware.module = dmi

# Generated at 2022-06-13 00:35:33.313315
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    module = MockModule({})
    facts = AIXHardware.get_mount_facts(module)
    assert len(facts['mounts']) > 0
    assert {'mount': '/', 'fstype': 'jfs2', 'options': 'rw', 'device': '/dev/hd4'} in facts['mounts']


# Generated at 2022-06-13 00:35:42.500626
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    from ansible.module_utils.facts.hardware.aix import AIXHardware
    from ansible.module_utils.facts.hardware.base import HardwareCollector
    from ansible.module_utils.facts.utils import get_file_content

    test_data = get_file_content('test/unit/module_utils/facts/hardware/aix/mount.ascii')
    ah = AIXHardware()
    ah._module = MockModule()
    ah._module.run_command = Mock(return_value=(0, test_data, ''))
    ah._module.get_bin_path = Mock(return_value='/bin/mount')
    ah.populate()

# Generated at 2022-06-13 00:35:47.361941
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    module = AnsibleModule(argument_spec={})
    module.params = None
    aixhardware = AIXHardware(module)

    assert(aixhardware.get_mount_facts() == {'mounts': []})



# Generated at 2022-06-13 00:35:50.890308
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    x = AIXHardwareCollector()
    assert x.platform == "AIX"
    assert x._fact_class == AIXHardware
    assert x._fact_class().platform == "AIX"

# Generated at 2022-06-13 00:35:55.703969
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    hardware_collector = AIXHardwareCollector()
    hardware_collector.fact_class.module = AnsibleModule
    hardware_collector.fact_class.module.run_command = lambda *args, **kwargs: (0, "", "")
    hardware_collector.collect()


# Generated at 2022-06-13 00:36:05.680033
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    # example for nfs mount with nolock option
    nfs_mount_string1 = 'host:/dir/dir/dir /mountpoint nfs4 rw,nolock,intr,nfsvers=4,rsize=32768,wsize=32768,hard,proto=tcp,timeo=600,retrans=2,sec=sys,mountvers=3,mountport=32767 0 0'

    # example for nfs mount with no options
    nfs_mount_string2 = 'host:/dir/dir/dir /mountpoint nfs4 rw,nfsvers=4,rsize=32768,wsize=32768,hard,proto=tcp,timeo=600,retrans=2,sec=sys,mountvers=3,mountport=32767 0 0'

    # example for cifs mount

# Generated at 2022-06-13 00:36:16.389565
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():

    class testmodule():
        def __init__(self):
            self.run_command = Mock()

        def get_bin_path(self, bin, required):
            return bin

    test_module = testmodule()
    aix_hc = AIXHardware(test_module)
    mount_facts = aix_hc.get_mount_facts()

# Generated at 2022-06-13 00:36:39.851331
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():

    import sys

    # Temporary fix for:
    # Invoking `test_AIXHardware_get_dmi_facts` fails
    # This hack directly manipulates `sys.modules` to insert a mock module in
    # place of the `ansible.module_utils.facts.hardware.base` module.
    sys.modules['ansible.module_utils.facts.hardware.base'] = type('MockBase',
                                                                  (object, ),
                                                                  {'Hardware': AIXHardware})

    import ansible.module_utils.facts.hardware.aix

    # Call the method
    instance = ansible.module_utils.facts.hardware.aix.AIXHardware()
    result = instance.get_dmi_facts()

    # Return the result
    return result



# Generated at 2022-06-13 00:36:51.750954
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    class EmptyModule:
        def __init__(self, *args, **kwargs):
            self.params = {}
            self.check_mode = False
            self.run_command = lambda *args, **kwargs: ([0], '', '')

    class EmptyModule2(EmptyModule):
        def __init__(self, *args, **kwargs):
            super(EmptyModule2, self).__init__(*args, **kwargs)
            self.run_command = lambda *args, **kwargs: ([1], '', '')

    hw = AIXHardware(EmptyModule())
    hw1 = AIXHardware(EmptyModule2())
    print(hw.get_memory_facts())
    print(hw1.get_memory_facts())


# Generated at 2022-06-13 00:37:00.485980
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():

    class XModule(object):
        def run_command(self, cmd, use_unsafe_shell=False):
            if cmd.find("lsvg") != -1:
                return 0, open('/tmp/lsvg.out').read(), None
            if cmd.find("xargs") != -1:
                return 0, open('/tmp/xargs.out').read(), None
            if cmd.find("lsconf") != -1:
                return 0, open('/tmp/lsconf.out').read(), None
            if cmd.find("lsattr") != -1:
                return 0, open('/tmp/lsattr.out').read(), None

    obj = AIXHardware(XModule())
    facts = obj.get_vgs_facts()

# Generated at 2022-06-13 00:37:11.234223
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():

    class MockModule(object):
        def run_command(self, cmd):
            return 0, out, ''
        def get_bin_path(self, cmd, required=False):
            return cmd

    class MockFaiss(AIXHardware):
        def populate(self, collected_facts=None):
            self.module = MockModule()
            return self.get_vgs_facts()

    faiss = MockFaiss()

    # test for rootvg

# Generated at 2022-06-13 00:37:18.281993
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    import json
    module = AnsibleModule(argument_spec={})
    os = AIXHardwareCollector(module=module)

    # Use /etc/mnttab to simulate the output of mount command
    with open("/etc/mnttab") as mount_out:
        out = mount_out.read()
        mount_facts = os.get_mount_facts(out)

    with open("/etc/facts.d/mount.fact", "w") as mount_fact:
        mount_fact.write(json.dumps(mount_facts, indent=4))



# Generated at 2022-06-13 00:37:25.427325
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():

    class AIXHardware_Mock():
        def __init__(self):
            self.module = MockModule()

    class MockModule:
        def get_bin_path(self, command, opt_dirs=None):
            return "/usr/bin/" + command


# Generated at 2022-06-13 00:37:32.383111
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    from ansible.module_utils.facts.system.hardware import AIXHardware
    from ansible.module_utils.facts.utils import get_mount_size


# Generated at 2022-06-13 00:37:42.988475
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    test_module = AnsibleModule(argument_spec={})
    test_module.get_bin_path = lambda _: '/bin/mount'

# Generated at 2022-06-13 00:37:48.917678
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.six import StringIO


# Generated at 2022-06-13 00:37:53.148933
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    import platform
    from ansible.module_utils.facts.hardware.aix import AIXHardware
    from ansible.module_utils.facts.platforms import linux

    ah = AIXHardware(dict(module=linux))

    assert isinstance(ah, AIXHardware)
    assert ah.platform == 'AIX'

    vgs_facts = ah.get_mount_facts()
    assert len(vgs_facts) == 1
    assert isinstance(vgs_facts, dict)
    assert 'mounts' in vgs_facts
    assert isinstance(vgs_facts['mounts'], list)
    assert len(vgs_facts['mounts']) >= 1

# Generated at 2022-06-13 00:38:21.677874
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    module = type('test', (object,), dict(run_command=fake_run_command))()
    facts_obj = AIXHardware(module=module)
    # Return value of lsattr -El sys0 -a fwversion
    fake_rc = 0
    fake_out = 'firmware_version IBM,9111-515'
    fake_err = ''
    lsattr_cmd = "/usr/sbin/lsattr -El sys0 -a fwversion"
    ret = facts_obj.get_dmi_facts()
    assert ret['firmware_version'] == '9111-515'



# Generated at 2022-06-13 00:38:26.359239
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    module = AnsibleModule(argument_spec={})
    hw = AIXHardware(module=module)
    hw_facts = hw.populate()
    # Check that returned dictionary has the expected data for some keys
    assert 'memory' in hw_facts
    assert 'swap' in hw_facts['memory']
    assert 'processor' in hw_facts
    assert 'lpar_info' in hw_facts
    assert 'firmware_version' in hw_facts
    assert 'product_serial' in hw_facts
    assert 'product_name' in hw_facts


# Generated at 2022-06-13 00:38:38.243755
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    test_out = b'''proc0          Available 00-00 Processor
proc1          Available 00-01 Processor
proc2          Available 00-02 Processor
proc3          Available 00-03 Processor
proc4          Available 00-04 Processor
proc5          Available 00-05 Processor
proc6          Available 00-06 Processor
proc7          Available 00-07 Processor
proc8          Available 00-08 Processor'''

    module = type('', (), {})()
    module.run_command = type('', (), {'__getitem__': lambda _, i: {0: 0, 1: test_out, 2: ''}[i]})
    obj = AIXHardware(module)
    facts = obj.get_cpu_facts()

    assert facts['processor'] == 'PowerPC_POWER8'
    assert facts['processor_cores'] == 4

# Generated at 2022-06-13 00:38:47.561447
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    test_AIXHardware = AIXHardware(module)
    # fake data
    test_lsdev_output = '''
name         status  description
ent0      Available 10/100 Mbps Ethernet PCI Adapter (14106902)
ent1      Available 10/100 Mbps Ethernet PCI Adapter (14106902)
ent2      Available 10/100 Mbps Ethernet PCI Adapter (14106902)
ent3      Available 10/100 Mbps Ethernet PCI Adapter (14106902)'''


# Generated at 2022-06-13 00:38:58.731723
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    vgs_facts = []


# Generated at 2022-06-13 00:39:05.464966
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True)


# Generated at 2022-06-13 00:39:16.798632
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():

    module = AnsibleModule(argument_spec=dict())


# Generated at 2022-06-13 00:39:21.527426
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    # Mock module class
    module = type('module', (object,), {'run_command': lambda *args, **kwargs: (0, '', '')})()

    hardware = AIXHardware(module)
    facts = hardware.get_cpu_facts()
    assert 'processor' in facts
    assert 'processor_count' in facts
    assert 'processor_cores' in facts


# Generated at 2022-06-13 00:39:32.324917
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    class Args():
        def __init__(self):
            self.gather_subset = []

    class Module():
        def get_bin_path(self, cmd, required=True):
            if required:
                raise ValueError
            return None

        def run_command(self, cmd, use_unsafe_shell=None):
            if cmd == "/usr/bin/vmstat -v":
                out = """
                memory pages :    30000  (PGTBL)
                free memory  :    10000 (OK)
                """

# Generated at 2022-06-13 00:39:38.890320
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    from ansible.module_utils.facts.collector import FactsCollector
    from ansible.module_utils.facts.hardware.aix import AIXHardware
    from ansible.module_utils.facts.utils import get_mount_size

    aix_facts = AIXHardware()

    mem_facts = aix_facts.get_memory_facts()

    assert 'memtotal_mb' in mem_facts
    assert 'memfree_mb' in mem_facts
    assert 'swaptotal_mb' in mem_facts
    assert 'swapfree_mb' in mem_facts

# Generated at 2022-06-13 00:40:27.738957
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    mem_facts = {
        'memfree_mb': 2,
        'memtotal_mb': 16,
        'swapfree_mb': 16,
        'swaptotal_mb': 16
    }

    aix_hw = AIXHardware({'ansible_facts': {}})
    aix_hw.module.run_command = Mock(
        return_value=(0, "/usr/sbin/vmstat -v", "")
    )

# Generated at 2022-06-13 00:40:29.025761
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    module = AnsibleModule(argument_spec={}, supports_check_mode=False)
    hardware = AIXHardware(module)
    facts = hardware.populate()

    assert len(facts) > 0



# Generated at 2022-06-13 00:40:33.904565
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )


# Generated at 2022-06-13 00:40:37.646164
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    hardware_collector = AIXHardwareCollector()
    assert hardware_collector is not None
    assert hardware_collector._platform == 'AIX'
    assert hardware_collector._fact_class == AIXHardware

# Generated at 2022-06-13 00:40:41.811365
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    module = AnsibleModule(argument_spec={})
    hardware_collector = AIXHardwareCollector(module)
    assert hardware_collector.fact_class is AIXHardware
    assert hardware_collector.platform == 'AIX'


# Generated at 2022-06-13 00:40:51.696476
# Unit test for method get_mount_facts of class AIXHardware

# Generated at 2022-06-13 00:40:59.216284
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    module = AnsibleModule(argument_spec={})
    aix_collector = AIXHardwareCollector(module=module)
    cmd = (
        "echo 'IBM,8235-E2D\n' | /usr/sbin/lsattr -El sys0 -a fwversion; "
        "echo ' Machine Serial Number..........: 12345\n"
        " LPAR Info..........................: 1 10 00C25A4B4C4D4E4F4\n"
        " System Model.......................: IBM,8235-E2D\n"
        " Serial Number......................: 12345\n' | /usr/sbin/lsconf"
    )
    rc, out, err = aix_collector.module.run_command(cmd)

# Generated at 2022-06-13 00:41:05.426137
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    mocked_module = MockAnsibleModule()

# Generated at 2022-06-13 00:41:12.845954
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    module = AnsibleModule(argument_spec={})
    hardware = AIXHardware(module)

    # Minimal output of vmstat command

# Generated at 2022-06-13 00:41:14.033978
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    """Test constructor of class AIXHardwareCollector"""
    AIXHardwareCollector()

# Generated at 2022-06-13 00:42:32.914465
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    test_module = AnsibleModule(argument_spec={})
    test_aix_hardware = AIXHardware(test_module)

    # Success scenario

# Generated at 2022-06-13 00:42:37.384533
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    test_module = AnsibleModule(argument_spec={})
    test_module.run_command = MagicMock(return_value=(0, '', ''))
    expected_result = {
        'processor': 'PowerPC_POWER8',
        'processor_count': 4,
        'processor_cores': 1
    }
    result = AIXHardware(module=test_module).get_cpu_facts()
    assert result == expected_result


# Generated at 2022-06-13 00:42:39.322818
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    module = AnsibleModule(argument_spec={})
    AIXHardware.get_mount_facts(module)

# Generated at 2022-06-13 00:42:48.686378
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    from ansible.module_utils.facts.hardware.aix import AIXHardware
    facts = AIXHardware().get_device_facts()
    assert 'devices' in facts
    assert 'fcs0' in facts['devices']
    assert 'state' in facts['devices']['fcs0']
    assert 'type' in facts['devices']['fcs0']
    assert 'attributes' in facts['devices']['fcs0']
    assert 'CIO_IGNORE' in facts['devices']['fcs0']['attributes']
    assert 'True' == facts['devices']['fcs0']['attributes']['CIO_IGNORE']


# Generated at 2022-06-13 00:42:53.101767
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    module = AnsibleModule(argument_spec={})
    hardware = AIXHardware(module)

    # get_dmi_facts() return a dict
    assert isinstance(hardware.get_dmi_facts(), dict)

    # get_dmi_facts() return a dict with at least 4 keys
    assert len(hardware.get_dmi_facts()) >= 4



# Generated at 2022-06-13 00:42:59.801753
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    class Module(object):
        def __init__(self):
            self.params = {}
        def run_command(self, cmd):
            return 0, out_lsdev, err_lsdev

    module = Module()
    out_lsdev = '''proc0 Available 00-00 Processor
proc4 Available 00-04 Processor'''
    err_lsdev = ''
    aix_hardware = AIXHardware(module)
    cpu_facts = aix_hardware.get_cpu_facts()

    assert 'processor' in cpu_facts
    assert cpu_facts['processor_count'] == 2
    assert cpu_facts['processor_cores'] == 1
    assert cpu_facts['processor'] == 'PowerPC_POWER7'



# Generated at 2022-06-13 00:43:07.953101
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    module = AnsibleModule(argument_spec=dict())
    hardware = AIXHardware(module)
    device_facts = hardware.get_device_facts()
    assert 'devices' in device_facts
    assert 'ent0' in device_facts['devices']
    assert 'state' in device_facts['devices']['ent0']
    assert 'type' in device_facts['devices']['ent0']
    assert 'attributes' in device_facts['devices']['ent0']
    assert 'dev_name' in device_facts['devices']['ent0']['attributes']
    assert 'state' in device_facts['devices']['ent0']
    assert device_facts['devices']['ent0']['state'] == 'Available'
    assert 'type' in device_facts['devices']['ent0']

# Generated at 2022-06-13 00:43:16.875027
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    class MockModule(object):
        def __init__(self):
            self.run_command_calls = []
            self.params = {}
            self.params['gather_subset'] = '!all'
            self.params['gather_timeout'] = 10
            self.params['gather_network_resources'] = 'yes'
            self.check_mode = False
            self.exit_json = None
            self.fail_json = None

        def get_bin_path(self, executable, required=False):
            if executable == 'mount':
                return '/usr/sbin/mount'


# Generated at 2022-06-13 00:43:25.888156
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    set_module_args(dict(gather_subset='hardware'))
    ah = AIXHardware(module=module)
    ah.populate()
    facts = module.exit_json(changed=False, ansible_facts=dict(ah.facts))
    assert 'devices' in facts['ansible_facts'].keys()
    assert 'ent0' in facts['ansible_facts']['devices'].keys()
    assert 'state' in facts['ansible_facts']['devices']['ent0'].keys()
    assert 'type' in facts['ansible_facts']['devices']['ent0'].keys()

# Generated at 2022-06-13 00:43:32.870690
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    module = AnsibleModuleMock()
    module.run_command = CommandResultMock(rc=0, out='proc0 Available 00-00 Processor\nproc1 Available 00-01 Processor', err='')
    hardware = AIXHardware(module)
    cpu_facts = hardware.get_cpu_facts()
    assert cpu_facts['processor'] == 'Processor'
    assert cpu_facts['processor_cores'] == 2
    assert cpu_facts['processor_count'] == 2
