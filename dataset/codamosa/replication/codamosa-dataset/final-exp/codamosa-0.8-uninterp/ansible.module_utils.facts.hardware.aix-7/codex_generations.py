

# Generated at 2022-06-13 00:35:08.720114
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

# Generated at 2022-06-13 00:35:15.931354
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    hardware = AIXHardware()

    hardware.module = AnsibleModule(
        argument_spec = dict(
            filter = dict(default=None, required=False)
        ),
        supports_check_mode=True
    )

    hardware.module.run_command = MagicMock(return_value=(0, "IBM,7041-CR9", ""))
    dmi_facts = hardware.get_dmi_facts()
    assert dmi_facts['firmware_version'] == '7041-CR9'

# Generated at 2022-06-13 00:35:26.464809
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    import sys

    module = sys.modules['ansible.module_utils.facts.aix.hardware']
    aix_hardware = module.AIXHardware()
    vgs_facts = aix_hardware.get_vgs_facts()
    assert 'vgs' in vgs_facts
    assert type(vgs_facts['vgs']) is dict
    assert 'rootvg' in vgs_facts['vgs']
    assert 'realsyncvg' in vgs_facts['vgs']
    assert 'testvg' in vgs_facts['vgs']
    assert type(vgs_facts['vgs']['rootvg']) is list
    assert type(vgs_facts['vgs']['realsyncvg']) is list

# Generated at 2022-06-13 00:35:29.303001
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    from ansible.module_utils.facts import FactCollector
    fact_collector = FactCollector()
    fact_collector._collector = {'AIXHardware': AIXHardware(fact_collector)}
    fact_collector.populate()
    for fact in ['memtotal_mb', 'memfree_mb', 'swaptotal_mb', 'swapfree_mb']:
        assert fact in fact_collector.facts

# Generated at 2022-06-13 00:35:36.871981
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec={})
    module.run_command = MagicMock(return_value=('', 'Available processor types: POWER5 POWER6 POWER7 POWER8 POWER9\n', ''))
    ahw = AIXHardware(module)
    cpu_facts = ahw.get_cpu_facts()
    module.run_command.assert_called_once_with('/usr/sbin/lsdev -Cc processor')
    assert(cpu_facts['processor_count'] == 5)
    assert(cpu_facts['processor'] == 'POWER9')



# Generated at 2022-06-13 00:35:41.763235
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    facts = dict()
    facts['system'] = dict()
    set_module_args({})
    result = dict(changed=False, ansible_facts=dict(hardware=AIXHardware(module=AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=False,
    )).populate()))
    assert (result['ansible_facts'] == facts)



# Generated at 2022-06-13 00:35:48.956170
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    """
    Unit test for method get_mount_facts of class AIXHardware
    """
    from ansible.module_utils.facts.hardware.aix import AIXHardware
    aix_hardware = AIXHardware()
    module = get_module()
    aix_hardware.module = module
    aix_hardware.populate()
    assert aix_hardware.get_mount_facts() is not None


# Generated at 2022-06-13 00:36:00.087632
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    """
    Test cases for testing the method get_mount_facts of class AIXHardware.
    The method get_mount_facts is used to fetch information about the mounts on the system.
    """

# Generated at 2022-06-13 00:36:02.792321
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    hardware = AIXHardware({})
    hardware.populate()
    assert hardware.facts['mounts']
    assert hardware.facts['vgs']
    assert hardware.facts['devices']

# Generated at 2022-06-13 00:36:12.907348
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = False,
    )

    hardware_collector = AIXHardware(module)

    cpu_facts = hardware_collector.get_cpu_facts()
    memory_facts = hardware_collector.get_memory_facts()
    dmi_facts = hardware_collector.get_dmi_facts()
    vgs_facts = hardware_collector.get_vgs_facts()
    mount_facts = hardware_collector.get_mount_facts()
    devices_facts = hardware_collector.get_device_facts()

    module.exit_json(changed=False, ansible_facts=dict(hardware=hardware_collector.populate()))



# Generated at 2022-06-13 00:36:37.176352
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec={})
    aix_hardware = AIXHardware(module)
    cpu_facts = aix_hardware.get_cpu_facts()

    assert 'processor_count' in cpu_facts
    assert cpu_facts['processor_count'] > 0
    assert 'processor' in cpu_facts
    assert cpu_facts['processor'] is not None
    assert 'processor_cores' in cpu_facts
    assert cpu_facts['processor_cores'] > 0



# Generated at 2022-06-13 00:36:48.999954
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    from ansible.module_utils.facts.aix import AIXHardware
    from ansible.module_utils.facts.hardware.aix import AIXHardwareCollector

    module = AnsibleModule(
        argument_spec = dict(
            gather_subset=dict(default=['all'], type='list')
        ),
        supports_check_mode=True
    )

    aix_hardware_collector = AIXHardwareCollector(module=module)
    aix_hardware = AIXHardware(module=module)
    aix_hardware.populate()
    expected = {'processor_cores': 4,
                'processor': 'PowerPC_POWER9',
                'processor_count': 2}
    actual = aix_hardware.cpu

# Generated at 2022-06-13 00:36:54.907751
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    from ansible.module_utils.facts.hardware.aix import AIXHardware
    from ansible.module_utils.facts.collector import MockModule
    from ansible.module_utils.facts.collector import MockCommand

    module = MockModule()

# Generated at 2022-06-13 00:37:00.125135
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    from ansible.module_utils.facts.hardware.aix import AIXHardware

    raw_facts = {
        'hardware': {},
    }
    aix_hw = AIXHardware(None, raw_facts, None)
    cpu_facts = aix_hw.get_cpu_facts()
    assert cpu_facts['processor_cores'] == int(2)
    assert cpu_facts['processor_count'] == int(2)
    assert cpu_facts['processor'] == 'PowerPC_POWER8'



# Generated at 2022-06-13 00:37:10.966102
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    from ansible.module_utils.facts.hardware.aix import AIXHardware
    device_facts = AIXHardware().get_device_facts()

    # Ensure that device_facts is a dict
    assert isinstance(device_facts, dict)

    # Ensure that expected keys are present in device_facts dict
    assert 'devices' in device_facts

    # Ensure that keys in fact dict are as per expected list
    assert set(['devices']).issubset(device_facts.keys())

    # Ensure that devices key is a dict
    assert isinstance(device_facts['devices'], dict)

    # Ensure that devices dict has expected key-value pairs
    assert 'ent0' in device_facts['devices']
    assert 'ent1' in device_facts['devices']
    assert 'ent2' in device_facts['devices']

    #

# Generated at 2022-06-13 00:37:20.365872
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    '''
    Unit test for method get_mount_facts of class AIXHardware
    '''
    mount_facts = {'mounts': []}
    aix_hw = AIXHardware(module=None)

    # Generate mount_out:

# Generated at 2022-06-13 00:37:29.682442
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    test_module = type('TestModule', (object,), {'run_command': run_command})
    test_module.params = params = {}
    test_module.exit_json = exit_json
    test_module.fail_json = fail_json
    test_module.get_bin_path = get_bin_path
    test_module.check_mode = False
    test_instance = AIXHardware(test_module)

    result = test_instance.get_cpu_facts()
    assert result['processor_count'] == 25
    assert result['processor_cores'] == 8
    assert result['processor'] == 'POWER6'



# Generated at 2022-06-13 00:37:40.643300
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes

    test_utils = basic.AnsibleModule(
        argument_spec = dict()
    )

    # Test 1
    test_module = AIXHardware(test_utils.params)
    test_module.module = test_utils

# Generated at 2022-06-13 00:37:47.956868
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    fake_module = None
    hi = AIXHardware(fake_module)
    lsdev_cmd = hi.module.get_bin_path('lsdev', True)
    lsattr_cmd = hi.module.get_bin_path('lsattr', True)
    hi.module.run_command = MagicMock(return_value=(0, lsdev_out, None))
    hi.module.run_command = MagicMock(return_value=(0, lsattr_out, None))
    hi.get_device_facts()
    lsattr_cmd_args = [lsattr_cmd, '-E', '-l', 'ent0']
    hi.module.run_command.assert_has_calls([call(lsdev_cmd), call(lsattr_cmd_args)])

# Generated at 2022-06-13 00:37:52.927698
# Unit test for method get_memory_facts of class AIXHardware

# Generated at 2022-06-13 00:38:24.027817
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    module_mock = AnsibleModuleMock()
    lsdev_cmd = '/usr/sbin/lsdev -Cc adapter'
    cmd_mock = CommandMock(module_mock, lsdev_cmd)
    RC_MOCK = 0
    STDOUT_MOCK = """fcs0 Available   FC Adapter
fscsi0 Available  FC SCSI I/O Controller
fscsi1 Available  FC SCSI I/O Controller
ent0 Available   10/100 Ethernet PCI Adapter (14106902)"""
    STDERR_MOCK = ''
    cmd_mock.set_results(RC_MOCK, STDOUT_MOCK, STDERR_MOCK)

    module_mock.run_command = MagicMock(return_value=cmd_mock)


# Generated at 2022-06-13 00:38:26.109839
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    hardware_collector_obj = AIXHardwareCollector()
    assert hardware_collector_obj is not None


# Generated at 2022-06-13 00:38:38.024064
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    module = AnsibleModule(argument_spec={})

    AIXHardware_obj = AIXHardware(module)

    lsdev_cmd = module.get_bin_path('lsdev', True)
    out_lsdev = '''ent0 Available 00-00-E8-5B-B9-D4 Ethernet Adapter (lp-aea)
ent1 Available 00-00-E8-5B-B9-D5 Ethernet Adapter (lp-aea)
ent2 Defined   06-00-EB-09-11-23 Ethernet Adapter (lp-tapa)
ent3 Available 06-00-EB-09-11-24 Ethernet Adapter (lp-tapa)'''

    lsattr_cmd = module.get_bin_path('lsattr', True)

# Generated at 2022-06-13 00:38:41.436205
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    hardware_collector = AIXHardwareCollector()
    assert hardware_collector.platform == 'AIX'
    assert hardware_collector.fact_class == AIXHardware

# Generated at 2022-06-13 00:38:47.413226
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    module = MockModule()
    aix_hw = AIXHardware(module)

    # test for cpu facts
    aix_hw.module.run_command = Mock(return_value=(0, "", ""))
    cpu_facts = aix_hw.get_cpu_facts()
    assert cpu_facts["processor"] == "PowerPC_POWER8"
    assert cpu_facts["processor_cores"] == 4
    assert cpu_facts["processor_count"] == 2



# Generated at 2022-06-13 00:38:58.604489
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    aixhw_obj = AIXHardware()
    lsconf_path = aixhw_obj.module.get_bin_path("lsconf")

    rc, out, err = aixhw_obj.module.run_command(lsconf_path)
    dmi_facts = aixhw_obj.get_dmi_facts()

    if rc == 0 and out:
        for line in out.splitlines():
            data = line.split(':')
            if 'Machine Serial Number' in line:
                assert dmi_facts['product_serial'] == data[1].strip()
            if 'LPAR Info' in line:
                assert dmi_facts['lpar_info'] == data[1].strip()
            if 'System Model' in line:
                assert dmi_facts['product_name'] == data[1].strip()

# Generated at 2022-06-13 00:39:05.385724
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    sys.modules['ansible.module_utils.basic'] = Mock()
    sys.modules['ansible.module_utils.facts.platform'] = Mock()

    from ansible.module_utils.facts.hardware.aix import AIXHardware
    f = AIXHardware()

    # mock module input parameters
    f.module.run_command = Mock()
    f.module.run_command.return_value = (0, "", "")

    # Mock xargs and lsvg commands
    f.get_bin_path = Mock()
    f.get_bin_path.side_effect = ["/usr/bin/lsvg", "/usr/bin/xargs"]
    lsvg_cmd = "/usr/bin/lsvg -o | /usr/bin/xargs /usr/bin/lsvg -p"

    # Root

# Generated at 2022-06-13 00:39:16.768276
# Unit test for method get_mount_facts of class AIXHardware

# Generated at 2022-06-13 00:39:24.580888
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    class ModuleFake:
        def __init__(self, params=None):
            self.params = params
            if params is None:
                self.params = dict()
            self.params['check_invalid_arguments'] = False

        @staticmethod
        def get_bin_path(name, required=False):
            return '/usr/sbin/' + name

        def run_command(self, cmd, use_unsafe_shell=False):
            p = 'lsvg -o | xargs lsvg -p'

# Generated at 2022-06-13 00:39:29.542186
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    class MockModule(object):
        def __init__(self):
            self.params = {}

        def run_command(self, command, use_unsafe_shell=False):
            out = '''memory pages
            100000
            free pages
            50000'''
            return 0, out, ''

        def get_bin_path(self, path, opt_dirs=[]):
            return path

    test_module = MockModule()

    ah = AIXHardware(test_module)
    memory_facts = ah.get_memory_facts()
    assert memory_facts['memtotal_mb'] == 977
    assert memory_facts['memfree_mb'] == 488

# Generated at 2022-06-13 00:39:54.863965
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    hardware_collector = AIXHardwareCollector()
    assert hardware_collector.__class__.__name__ == 'AIXHardwareCollector'
    assert hardware_collector.platform == 'AIX'

# Generated at 2022-06-13 00:40:05.233853
# Unit test for method get_device_facts of class AIXHardware

# Generated at 2022-06-13 00:40:14.600053
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    class AIXHardware_Mock:
        def __init__(self, module):
            self.module = module
            self.module.run_command = lambda cmd: ('', '', '')

        def get_cpu_facts(self):
            return {}

        def get_memory_facts(self):
            return {}

        def get_dmi_facts(self):
            return {}

        def get_vgs_facts(self):
            return {}

        def get_mount_facts(self):
            return {}

    class Module_mock:
        def __init__(self, hardware_obj):
            self.hardware = hardware_obj

        def get_bin_path(self, arg1, arg2=None):
            return ''


# Generated at 2022-06-13 00:40:18.163681
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    module_mock = Mock()
    aix_hardware_collector = AIXHardwareCollector(module_mock, {}, [])

    assert 'AIX' == aix_hardware_collector._platform
    assert 'ansible.module_utils.facts.hardware.aix.AIXHardware' == aix_hardware_collector._fact_class


# Generated at 2022-06-13 00:40:22.949039
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    """ This function instantiates a AIXHardwareCollector object,
        calls the call (method) and returns the result of the call for test.
    """
    obj = AIXHardwareCollector()
    result = obj.call()
    return result

# Generated at 2022-06-13 00:40:31.611360
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    module = AnsibleModule(argument_spec={})
    hardware_obj = AIXHardware(module)
    res_dict = hardware_obj.populate()
    assert res_dict['processor'][0] == 'PowerPC_POWER8'
    assert res_dict['processor_count'] == 4
    assert res_dict['processor_cores'] == 1
    assert res_dict['memtotal_mb'] > 0
    assert res_dict['memfree_mb'] > 0
    assert res_dict['swaptotal_mb'] > 0
    assert res_dict['swapfree_mb'] > 0
    assert res_dict['firmware_version'] is not None
    assert res_dict['product_serial'] is not None
    assert res_dict['lpar_info'] is not None
    assert res_dict['product_name']

# Generated at 2022-06-13 00:40:42.940339
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    aix_hardware = AIXHardware()
    lscfg_path = aix_hardware.module.get_bin_path("lsconf")
    lscfg_output = """
        System Model:       IBM,8286-42A
        Machine Serial Number:      JXX2WC6
        Processor Type:    PowerPC_POWER8
        Number Of Processors:       1
        Processor Clock Speed:      3700 MHz
        CPU Type:          64-bit
        Kernel Type:       64-bit
        LPAR Info:         1 POSIX Entitlement
        AIX Version:       7.1
        #

    """
    aix_hardware.module.run_command.return_value = (0, lscfg_output, '')
    dmi_facts = aix_hardware.get_dmi_facts()

   

# Generated at 2022-06-13 00:40:52.762733
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    import os
    import tempfile

    # Prepare the test environment
    tmpdir = tempfile.mkdtemp()

    # Create some input files
    open(os.path.join(tmpdir, 'vmstat'), 'w').write("""
System configuration: lcpu=4 ent=0.50 mode=Uncapped
kthr      memory              page              faults      cpu
----- ----------- ------------------------ ------------ -----------
 r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
 2  0  4155  5218  0  0  34  0    0    0  17   11   9  0  0  0  0 100
""")

    # Assign the test module params
    module_params = {'libdir': tmpdir}

    # Create the return object


# Generated at 2022-06-13 00:40:59.395444
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    module = AnsibleModuleMock()
    obj = AIXHardware(module)
    module.run_command.side_effect = [('0', 'total mem = 38016384,   free mem = 6780048', ''),
                                      ('0', '    memory pages       =    136320', ''),
                                      ('0', '        free pages     =      81312', '')]
    result = obj.get_memory_facts()
    assert result
    assert result['memtotal_mb'] == 36642
    assert result['memfree_mb'] == 6580
    assert result['swaptotal_mb'] == 16099
    assert result['swapfree_mb'] == 16099


# Generated at 2022-06-13 00:41:08.258792
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.hardware.aix import AIXHardware
    from ansible.module_utils.facts.utils import get_file_content
    from ansible.module_utils.facts.utils import get_mount_size
    from ansible.module_utils.facts import ModuleTestCase

    # Create a fake module
    fake_module = ModuleTestCase.create_ansible_module()

    # Create a fake lsdev
    fake_lsdev_path = fake_module.tmpdir + '/lsdev'
    fake_lsdev_content = get_file_content('utils/fixtures/aix/lsdev')
    fake_module.register_file(fake_lsdev_path, fake_lsdev_content)

    # Create a fake lsattr

# Generated at 2022-06-13 00:41:55.400325
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    # This test will not run on AIX
    pass

# Generated at 2022-06-13 00:42:00.627765
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    module_path = 'ansible.module_utils.facts.hardware.aix.AIXHardware'
    aixhw = __import__(module_path, fromlist=['AIXHardware'])
    aixhw.AIXHardware.module = AnsibleModuleDummy()

    device_facts = aixhw.AIXHardware().get_device_facts()
    # assert whether there are some devices in dictionary
    assert device_facts['devices']


# Generated at 2022-06-13 00:42:08.598149
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )

    processor_cores = 4
    processor_count = 2
    processor = "PowerPC_POWER8"
    test_out = "proc0 Available PowerPC_POWER8 Processor 00-00\nproc1 Available PowerPC_POWER8 Processor 00-01"
    mock_run_command = MagicMock(return_value=(0, test_out, ''))
    setattr(module, 'run_command', mock_run_command)

    fact_class = AIXHardware(module)
    fact_class.populate()

    assert fact_class.processor_cores == processor_cores
    assert fact_class.processor_count == processor_count
    assert fact_class.processor == processor



# Generated at 2022-06-13 00:42:15.916327
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    class TestModuleAIXHardware:
        def run_command(self, cmd):
            return 0, "memory pages                : 29891\nfree pages                    : 29891", ""
    module = TestModuleAIXHardware()
    hardware = AIXHardware(module=module)
    test_memory_facts = hardware.get_memory_facts()

    assert test_memory_facts['memfree_mb'] == 119
    assert test_memory_facts['memtotal_mb'] == 118


# Generated at 2022-06-13 00:42:24.561453
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    '''
    unit test for method populate of class AIXHardware.
    In fact it is a integration test for class AIXHardware,
    as the get_*_facts methods of this class use run_command
    of class AnsibleModule which will call the module executed.
    '''
    # Create a instance of class AnsibleModule
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    module.run_command = MagicMock(return_value=(0, '', ''))

    # Create a instance of class AIXHardware
    aix_hw = AIXHardware(module)
    aix_hw.populate()

    # As the AnsibleModule class's run_command method has been mocked,
    # it will not run any real commands.
    # So we just assert that run

# Generated at 2022-06-13 00:42:31.892723
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    class ModuleStub(object):
        def get_bin_path(self, path, required=False):
            return '/usr/sbin/%s' % path
        def run_command(self, cmd):
            if cmd.startswith('/usr/sbin/lsvg -o'):
                return 0, vgs_out, ''
            if cmd.startswith('/usr/sbin/xargs'):
                return 0, '', ''
            if cmd.startswith('/usr/sbin/lsvg'):
                return 0, lsvg_out, ''
        def fail_json(self, **args):
            print("FAIL:" + str(args))
            exit(1)


# Generated at 2022-06-13 00:42:33.756407
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    aix_hardware_collector = AIXHardwareCollector()
    assert aix_hardware_collector._platform == "AIX"
    assert aix_hardware_collector._fact_class == AIXHardware


# Generated at 2022-06-13 00:42:40.048379
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    module = FakeAnsibleModule()
    hardware_cls = AIXHardware(module)
    hardware_cls.module.run_command = fake_run_command

    hardware_cls.get_memory_facts()

    assert hardware_cls.facts['memtotal_mb'] == 16
    assert hardware_cls.facts['memfree_mb'] == 16
    assert hardware_cls.facts['swaptotal_mb'] == 10
    assert hardware_cls.facts['swapfree_mb'] == 5


#Unit test for method get_cpu_facts of class AIXHardware

# Generated at 2022-06-13 00:42:42.347940
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    # No exception raised when creating class object
    AIXHardwareCollector()

# Generated at 2022-06-13 00:42:47.356082
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    module = type('module', (object,), {
        'run_command': run_command,
    })
    aix_hardware = AIXHardware(module)

    assert aix_hardware.get_cpu_facts() == {
        'processor': 'PowerPC_POWER8',
        'processor_cores': 2,
        'processor_count': 4,
    }

