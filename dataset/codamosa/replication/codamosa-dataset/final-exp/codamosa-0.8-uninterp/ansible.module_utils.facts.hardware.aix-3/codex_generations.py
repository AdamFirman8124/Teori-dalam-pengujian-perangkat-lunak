

# Generated at 2022-06-13 00:35:00.405935
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    assert isinstance(AIXHardwareCollector(), AIXHardwareCollector)



# Generated at 2022-06-13 00:35:06.363684
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    # Test to check the get_dmi_facts method of class AIXHardware
    from ansible.module_utils.facts.collector.aix import AIXHardware
    module = AnsibleModule(argument_spec={})
    aix_obj = AIXHardware(module)
    dmi_facts = aix_obj.get_dmi_facts()
    assert dmi_facts['firmware_version'] is not None


# Generated at 2022-06-13 00:35:13.179309
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    class ModuleStub(object):
        def __init__(self, params):
            self.params = params
            self.run_command_status = 0

        def get_bin_path(self, exe, required=False):
            return '/bin/' + exe

    module = ModuleStub({})
    mod_AIXHardware = AIXHardware(module)
    assert mod_AIXHardware.get_mount_facts() == {}


# Generated at 2022-06-13 00:35:21.141557
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )

    # Mock lsdev and run populate
    lsdev_mock = MagicMock()
    lsdev_mock.__str__ = MagicMock(return_value='lsdev')
    aix = AIXHardware(module=module)

    with patch('ansible.module_utils.facts.hardware.aix.AIXHardware.get_cpu_facts', return_value={'processor': 'powerpc'}):
        aix.populate()

    # Assert that populate called right functions
    module.get_bin_path.assert_any_call('vmstat')
    module.get_bin_path.assert_any_call('lsps')

# Generated at 2022-06-13 00:35:24.423704
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    module = AnsibleModule(argument_spec={})
    hardware_collector = AIXHardwareCollector(module=module)
    assert hardware_collector.fact_class == AIXHardware


# Generated at 2022-06-13 00:35:31.349279
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    from ansible.module_utils.facts.hardware.aix import AIXHardware
    from ansible.module_utils.facts.utils import MockModule

    testmodule = MockModule()
    testmodule.run_command = lambda x: (0, 'proc0 Available 00-00 Processor', '')

    aix_hardware = AIXHardware(testmodule)
    cpu_facts = aix_hardware.get_cpu_facts()

    assert cpu_facts['processor_count'] == 1
    assert cpu_facts['processor'] == 'Processor'
    assert cpu_facts['processor_cores'] == 1


# Generated at 2022-06-13 00:35:40.945350
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    from ansible.module_utils.facts.hardware.aix import AIXHardware
    from ansible.module_utils._text import to_bytes
    import json

    res = AIXHardware().get_vgs_facts()

    res_str = to_bytes(json.dumps(res, indent=4, sort_keys=True))
    print(res_str)

    assert res['vgs']
    assert 'rootvg' in res['vgs']

    for vg in res['vgs']:
        assert res['vgs'][vg] != []
        for pv in res['vgs'][vg]:
            assert pv['pv_state']
            assert pv['pv_name']
            assert pv['total_pps']
            assert pv['free_pps']

# Generated at 2022-06-13 00:35:42.981796
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    test_obj = AIXHardwareCollector()
    assert test_obj.platform == 'AIX'
    assert test_obj.fact_class == AIXHardware


# Generated at 2022-06-13 00:35:47.173552
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    hardware_collector = AIXHardwareCollector()
    assert hardware_collector._platform == 'AIX'
    assert hardware_collector._fact_class == AIXHardware

# Generated at 2022-06-13 00:35:58.337407
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    """
    Unit test for method get_vgs_facts of class AIXHardware
    """

    # Test 1:
    # Test with data that should produce a dictionary containing
    # a valid vgs_facts

# Generated at 2022-06-13 00:36:26.383370
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    import lpar_info_mock
    import os
    from ansible.module_utils.basic import AnsibleModule

    sys_data_mock = lpar_info_mock.open()

    lsdev_cmd = os.path.join(os.path.dirname(__file__), 'lsdev_mock.out')
    vmstat_cmd = os.path.join(os.path.dirname(__file__), 'vmstat_mock.out')
    lsps_cmd = os.path.join(os.path.dirname(__file__), 'lsps_mock.out')


# Generated at 2022-06-13 00:36:27.828898
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    hc = AIXHardwareCollector()


# Generated at 2022-06-13 00:36:31.874419
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    # Arrange
    module = CustomModule()
    # Act
    aix_hardware = AIXHardwareCollector(module)
    # Assert
    assert aix_hardware
    assert aix_hardware._platform == 'AIX'
    assert aix_hardware._fact_class == AIXHardware


# Generated at 2022-06-13 00:36:37.579355
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    module = AnsibleModule(argument_spec=dict())
    module.params = None
    hardware = AIXHardware(module)
    facts = hardware.populate()
    assert set(facts.keys()) == set(['memfree_mb', 'memtotal_mb', 'swapfree_mb', 'swaptotal_mb', 'processor', 'processor_cores', 'processor_count', 'firmware_version', 'product_serial', 'lpar_info', 'product_name', 'mounts', 'vgs', 'devices'])

# Generated at 2022-06-13 00:36:43.786952
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():

    def lsconf_side_effect(pathnames):
        if 'lsconf' in pathnames:
            return 'lsconf'
        else:
            return None

    class AIXModuleMock(object):
        run_command = None
        get_bin_path = lsconf_side_effect
        options = {}

        def __init__(self):
            self.params = {}
            self.exit_args = None
            self.exit_kwargs = None
            self.fail_json_args = None
            self.fail_json_kwargs = None

        def fail_json(self, *args, **kwargs):
            self.fail_json_args = args
            self.fail_json_kwargs = kwargs

        def exit_json(self, *args, **kwargs):
            self.exit_args = args

# Generated at 2022-06-13 00:36:55.275052
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    hardware = AIXHardware(None)

    out = """Firmware Version: IBM,SF240_314
        Machine Serial Number: VWK8GNER
        LPAR Info: 1 EMP 2 ENT 8 CEC
        Firmware Version: IBM,SF240_314
        Machine Serial Number: VWK8GNER
        LPAR Info: 1 EMP 2 ENT 8 CEC
        System Model: IBM,8408-E8D"""

    assert hardware.get_dmi_facts() == {'product_serial': 'VWK8GNER', 'lpar_info': '1 EMP 2 ENT 8 CEC', 'firmware_version': 'SF240_314', 'product_name': '8408-E8D'}

# Generated at 2022-06-13 00:37:07.546141
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():

    aixhardware_obj = AIXHardware(None)
    aixhardware_obj.module = MagicMock()

    # No vg
    aixhardware_obj.module.get_bin_path.side_effect = [None, None]
    aixhardware_obj.get_vgs_facts() == {}

    # 1 vg
    aixhardware_obj.module.get_bin_path.side_effect = ['/usr/sbin/lsvg', '/usr/bin/xargs']

# Generated at 2022-06-13 00:37:13.462488
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    module = AnsibleModule(argument_spec={})
    hardware = AIXHardware(module)
    facts = hardware.get_dmi_facts()
    assert 'firmware_version' in facts
    assert 'product_serial' in facts
    assert 'lpar_info' in facts
    assert 'product_name' in facts
    assert facts['firmware_version'] == 'V7.2'

# Generated at 2022-06-13 00:37:20.214465
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    module = AnsibleModule(argument_spec={})
    harware = AIXHardware(module=module)
    out = harware.populate()

    assert len(out['processor']) > 0
    assert out['processor_cores'] >= 0
    assert out['processor_count'] >= 0
    assert out['memtotal_mb'] >= 0
    assert out['memfree_mb'] >= 0
    assert out['swaptotal_mb'] >= 0
    assert out['swapfree_mb'] >= 0
    assert out['firmware_version'] > 0



# Generated at 2022-06-13 00:37:27.230288
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    """
    Unit test for method AIXHardware.get_mount_facts
    """
    module = AnsibleModule(argument_spec={})
    ah = AIXHardware(module)

    # Test with a sample output of mount command.

# Generated at 2022-06-13 00:38:14.023943
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    aixhw = AIXHardware()

    # create case data

# Generated at 2022-06-13 00:38:20.599292
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    module = AnsibleModule(argument_spec={})
    hardware = AIXHardware(module=module)

    # Test vg facts

# Generated at 2022-06-13 00:38:23.314531
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    # Only run the unit test if we are running on AIX
    platform_facts = {}
    if Hardware.get_platform() == 'AIX':
        platform_facts = Hardware().populate()

    assert 'firmware_version' in platform_facts


# Generated at 2022-06-13 00:38:25.402750
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    instance = AIXHardwareCollector()
    assert instance.platform == 'AIX'
    assert instance.fact_class == AIXHardware


# Generated at 2022-06-13 00:38:37.354746
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    # create a class instance
    aixhw = AIXHardware()

    # create a test output from mount command

# Generated at 2022-06-13 00:38:40.141959
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    test_module = AnsibleModule(argument_spec={})
    test_class = AIXHardware(test_module)
    test_result = test_class.get_mount_facts()

    assert(test_result)


# Generated at 2022-06-13 00:38:48.087126
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    module = MockModule()
    lsvg_path = '/usr/sbin/lsvg'
    xargs_path = '/usr/bin/xargs'
    cmd = "%s -o | %s %s -p" % (lsvg_path, xargs_path, lsvg_path)
    module.run_command.return_value = (0, out_lsvg_p, '')
    cmd = "/usr/sbin/lsvg rootvg"
    module.run_command.return_value = (0, out_lsvg_rootvg, '')
    module.get_bin_path.return_value = True
    hardware = AIXHardware(module)
    vgs_facts = hardware.get_vgs_facts()

# Generated at 2022-06-13 00:38:59.108008
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():

    module = AnsibleModule(argument_spec={})
    facts = AIXHardware(module)
    vgs_facts = facts.get_vgs_facts()

# Generated at 2022-06-13 00:39:05.685029
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    # Test with memory and network facts
    module = AnsibleModule(argument_spec=dict())
    hardware_facts = AIXHardware(module).populate()

    keys = ['firmware_version', 'lpar_info', 'memfree_mb', 'memtotal_mb',
            'processor', 'processor_cores', 'processor_count',
            'product_name', 'product_serial', 'swapfree_mb', 'swaptotal_mb',
            'vgs', 'devices', 'mounts']
    for key in keys:
        assert key in hardware_facts.keys(), 'Key missing: %s' % key

    # Test with memory and network facts
    module = AnsibleModule(argument_spec=dict())
    hardware_facts = AIXHardware(module).populate()


# Generated at 2022-06-13 00:39:07.659409
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    module = FakeModule()
    hardware = AIXHardware(module)
    hardware.get_device_facts()



# Generated at 2022-06-13 00:39:59.627159
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():

    module = AnsibleModule(
        argument_spec = dict(
        ),
        supports_check_mode=True
    )

    ah = AIXHardware(module=module)

    facts = ah.get_mount_facts()

    assert 'mounts' in facts
    assert '/' in facts['mounts']
    assert '/cifs' in facts['mounts']
    assert '/cifs/foo' in facts['mounts']
    assert '/nfs' in facts['mounts']
    assert '/nfs/foo' in facts['mounts']

    mounts = facts['mounts']

    for line in mounts:
        assert 'mount' in line
        assert 'device' in line
        assert 'fstype' in line
        assert 'options' in line
        assert 'time' in line

# Generated at 2022-06-13 00:40:07.915963
# Unit test for method get_memory_facts of class AIXHardware

# Generated at 2022-06-13 00:40:11.876501
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    class TestModule(object):
        def run_command(self, cmd, use_unsafe_shell=False):
            return 0, '', ''

        def get_bin_path(self, name, required=True):
            return 'lsvg'


# Generated at 2022-06-13 00:40:19.260110
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():

    class test_AIXHardware_obj(object):

        def __init__(self):
            self.module = None

        def get_bin_path(self, bin_path, required=False):
            return '/usr/sbin/mount'

        def run_command(self, cmd, use_unsafe_shell=False, check_rc=True, executable=None, data=None):
            if cmd == '/usr/sbin/mount':
                return 0, 'node       mounted        mounted over    vfs       date        options\n/dev/hd4     /             /dev/hd2      jfs2       Nov 28 22:24... \n-hosts:/home  /home         nfs          rw,bg,hard,intr,rsize=32768... Nov 30 00:32..', ''
            return 0, '', ''

    my

# Generated at 2022-06-13 00:40:26.326701
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    hd = AIXHardware(dict(module=dict(run_command = lambda *args, **kwargs: (0, '', ''))))
    hd.populate()
    assert hd.facts['processor']
    assert hd.facts['memtotal_mb']
    assert hd.facts['firmware_version']
    assert hd.facts['vgs']
    assert hd.facts['devices']



# Generated at 2022-06-13 00:40:33.803936
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():

    class MyFactModule:
        def __init__(self, module_name='ansible.module_utils.facts.hardware.aix.AIXHardware'):
            self.ansible_module = MyAnsibleModule(module_name)

        def run_command(self, command, use_unsafe_shell=False):
            output = ''
            if command.startswith(AIXHardware._lsdev_cmd):
                output = LSDEV_OUTPUT
            elif command.startswith(AIXHardware._lsattr_cmd):
                output = LSATTR_OUTPUT
            elif command.startswith(AIXHardware._vmstat_cmd):
                output = VMSTAT_OUTPUT
            elif command.startswith(AIXHardware._lsps_cmd):
                output = LSPS_OUTPUT

# Generated at 2022-06-13 00:40:45.776706
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    class FakeModule(object):
        pass

    m = FakeModule()


# Generated at 2022-06-13 00:40:55.620755
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():

    class ModuleMock:
        def __init__(self):
            self.args = 'args'
            self.module = 'module'
            self.log = 'log'
            self.run_command_count = 0
            self.run_command_rc = 0
            self.run_command_cmd = ''
            self.run_command_stdout = 0
            self.run_command_stderr = ''
            self.run_command_unsafe_shell = False
            self.get_bin_path_path_str = ''
            self.get_bin_path_default_path = ''
            self.get_bin_path_path = ''

        def get_bin_path(self, path_str, default_path=None):
            self.get_bin_path_path_str = path_str

# Generated at 2022-06-13 00:40:57.071594
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    collector = AIXHardwareCollector()
    assert collector.platform == 'AIX'
    assert collector.fact_class == AIXHardware


# Generated at 2022-06-13 00:41:04.029307
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    """
    Test get_vgs_facts method of class AIXHardware
    """
    hw = AIXHardware()
    rc, out, err = hw.module.run_command("/usr/sbin/lsvg -o")
    if out:
        data = out.split()
        # lsps returns disk name with p
        disk = data[0] + 'p'
        cmd = "/usr/sbin/lsps"
        rc, out, err = hw.module.run_command(cmd)
        if out:
            data = out.split()
            pp_size = data[3]
            cmd = "/usr/sbin/lsvg -p " + disk
            rc, out, err = hw.module.run_command(cmd)

# Generated at 2022-06-13 00:41:53.060511
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    test_module = AnsibleModule(argument_spec={})
    test_module.run_command = MagicMock(return_value=(0, 'proc0 Available 00-00 00-00 PowerPC_POWER7', ''))
    test_AIXHardware = AIXHardware(test_module)
    test_AIXHardware.get_cpu_facts()
    assert test_AIXHardware._populate_called == {'processor': [], 'processor_count': 1, 'processor_cores': 8}

# Unit tests for method get_memory_facts of class AIXHardware

# Generated at 2022-06-13 00:41:59.756746
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    class local_module(object):
        def __init__(self, **kwargs):
            self.params = kwargs
            self.fail_json = exit

        def run_command(self, cmd):
            out = '''memory pages :  153754
free pages   :   53942'''
            return (0, out, '')
    module = local_module()
    facts = AIXHardware(module).get_memory_facts()
    assert facts['memtotal_mb'] == 93
    assert facts['memfree_mb'] == 33
    assert 'swaptotal_mb' not in facts


# Generated at 2022-06-13 00:42:07.677940
# Unit test for method get_memory_facts of class AIXHardware

# Generated at 2022-06-13 00:42:11.629240
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    import sys
    sys.modules['ansible'] = type('FakeAnsibleModule', (object,), {})
    """
    module = FakeAnsibleModule()
    module.run_command = FakeAnsibleModuleRunCommand()
    hw = AIXHardware(module)
    dmi_facts = hw.get_dmi_facts()
    assert(dmi_facts['serial'] == '0A0E5EZ')
    """

# Generated at 2022-06-13 00:42:21.007315
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    test_module = AnsibleModule(
        argument_spec=dict(
        )
    )

    test_module.lsvg_mock = "/usr/sbin/lsvg -o VG_NAME"
    test_module.xargs_mock = "/usr/bin/xargs -n1 /usr/sbin/lsvg -p VG_NAME"
    test_module.lsvg_cmd = "/usr/sbin/lsvg"

# Generated at 2022-06-13 00:42:28.556491
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.hardware.aix import AIXHardware
    import ansible_collections.ansible.community.plugins.module_utils.facts.hardware.aix as aix_utils

    lsdev_cmd = AIXHardware(aix_utils.ANSIBLE_MODULE)
    lsdev_cmd.module.get_bin_path = lambda x, z: x

    device_facts = lsdev_cmd.get_device_facts()
    assert isinstance(device_facts, dict)
    assert isinstance(device_facts['devices'], dict)

# Generated at 2022-06-13 00:42:35.023393
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    # Create a AIXHardware object with empty mounts list
    test_AIXHardware = AIXHardware()
    test_AIXHardware.mounts = []
    # Set the out of mount command

# Generated at 2022-06-13 00:42:45.603575
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    from ansible.module_utils.facts.hardware.aix import AIXHardware
    aix_hardware = AIXHardware(None)

# Generated at 2022-06-13 00:42:54.584798
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    module = AnsibleModule(argument_spec=dict())
    hardware = AIXHardwareCollector(module=module).collect()[0]

# Generated at 2022-06-13 00:43:03.477750
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    """Method get_dmi_facts of class AIXHardware should return the
        firmware_version, product_serial, lpar_info, product_name"""
    class Options:
        def __init__(self, bin_path):
            self.module_path = bin_path

    class RunCommandMock(object):
        def __init__(self):
            self.commands = [
                ['uname -s', 0, 'AIX', ''],
                ['lsattr -El sys0 -a fwversion', 0, 'fwversion IBM,8233-E8B', ''],
                ['lsconf', 0, 'Machine Serial Number:     TESTSLOT01\nLPAR Info:0-7-AIX-21-1\nSystem Model: IBM,8233-E8B', ''],
            ]
