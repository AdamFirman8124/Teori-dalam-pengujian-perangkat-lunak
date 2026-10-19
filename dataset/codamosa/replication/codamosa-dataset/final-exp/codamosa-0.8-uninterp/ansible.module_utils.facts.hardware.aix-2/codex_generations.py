

# Generated at 2022-06-13 00:35:03.753679
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    aix_facts = AIXHardware(module)
    cpu_facts = aix_facts.get_cpu_facts()
    assert cpu_facts['processor'].startswith('Power')
    assert cpu_facts['processor_count'] > 0
    assert cpu_facts['processor_cores'] > 0


# Generated at 2022-06-13 00:35:05.288649
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    obj = AIXHardwareCollector()
    assert obj.platform == 'AIX'
    assert obj.fact_class == AIXHardware

# Generated at 2022-06-13 00:35:16.735474
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    hardware_instance = AIXHardware(dict())

    hardware_instance.module = Mock()
    hardware_instance.module.run_command.return_value = (0, MOUNT_OUT, '')

    mount_facts = hardware_instance.get_mount_facts()

    assert 'mounts' in mount_facts
    assert len(mount_facts['mounts']) == 4
    assert mount_facts['mounts'][0]['mount'] == '/'
    assert mount_facts['mounts'][1]['device'] == '/dev/hd4'
    assert mount_facts['mounts'][2]['fstype'] == 'nfs'
    assert mount_facts['mounts'][3]['options'] == 'rw,rsize=32768,hard,intr'

# Generated at 2022-06-13 00:35:25.650198
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    """
    Run a unit test on get_cpu_facts()
    """
    # Helper classes required to create an instance of ansible.module_utils.facts.hardware.base.Hardware()

# Generated at 2022-06-13 00:35:33.496281
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    module = AnsibleModule(argument_spec={})

    lsattr_path = module.get_bin_path("lsattr")
    if lsattr_path:
        # Memory size is 2097152 KB
        lsattr_out = """attribute value     description             user_set     P_Base
realmem            2097152   Real memory size in KBytes  False        True
"""
        # swapinfo output looks like:
        # Device          1M-blocks     Used    Avail Capacity
        # /dev/ada0p3        314368        0   314368     0%
        swapinfo_out = """Device          1M-blocks     Used    Avail Capacity
/dev/ada0p3        314368        0   314368     0%
"""

        module.run_command = Mock(return_value=(0, lsattr_out, ''))
       

# Generated at 2022-06-13 00:35:39.239602
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    import json
    from ansible.module_utils.facts.hardware.aix import AIXHardware
    module = AnsibleModuleMock()
    obj = AIXHardware(module)

    assert obj.populate() == {
        'processor': [],
        'processor_cores': 0,
        'processor_count': 0,
        'memtotal_mb': 0,
        'memfree_mb': 0
    }



# Generated at 2022-06-13 00:35:42.283758
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    aix = AIXHardware()
    expected = {
        'processor': u'PowerPC_POWER8',
        'processor_cores': 12,
        'processor_count': 12
    }
    assert aix.get_cpu_facts() == expected



# Generated at 2022-06-13 00:35:55.039248
# Unit test for method get_cpu_facts of class AIXHardware

# Generated at 2022-06-13 00:36:05.117570
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    import tempfile
    from ansible.module_utils.facts.hardware.aix import AIXHardware
    test_obj = AIXHardware({}, None)

    # Case 1: Check that facts are gathered when command succeeds
    test_obj.module.run_command = lambda x: (0, 'Available 00-00 Processor', '')
    test_obj.module.run_command = lambda x: (0, 'proc0 POWER7 Processor', '')
    test_obj.module.run_command = lambda x: (0, 'smt_threads Enabled', '')
    result = test_obj.get_cpu_facts()
    assert result["processor"] == "POWER7"
    assert result["processor_cores"] == 1
    assert result["processor_count"] == 1

    # Case 2: Check that facts are gathered when command succeeds


# Generated at 2022-06-13 00:36:15.996356
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    module = AnsibleModuleMock()


# Generated at 2022-06-13 00:36:37.391384
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    assert AIXHardware.get_memory_facts(None) == {'memfree_mb': 136984, 'memtotal_mb': 143360,
                                                  'swapfree_mb': 136984, 'swaptotal_mb': 143360}
    return

# Generated at 2022-06-13 00:36:48.999152
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    module = AnsibleModule({})

    h = AIXHardware(module)
    result = h.populate()
    assert 'firmware_version' in result
    assert 'product_serial' in result
    assert 'processor_cores' in result
    assert 'processor_count' in result
    assert 'product_name' in result
    assert 'lpar_info' in result
    assert 'memfree_mb' in result
    assert 'memtotal_mb' in result
    assert 'processor' in result
    assert 'swapfree_mb' in result
    assert 'swaptotal_mb' in result
    assert 'vgs' in result
    assert 'devices' in result
    assert 'mounts' in result

# Unit tests for method get_cpu_facts of class AIXHardware

# Generated at 2022-06-13 00:36:52.951599
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    supported_facts_list = ['processor', 'processor_cores', 'processor_count', 'memtotal_mb', 'memfree_mb',
                            'swaptotal_mb', 'swapfree_mb', 'devices', 'mounts', 'firmware_version',
                            'product_serial', 'lpar_info', 'product_name', 'vgs']
    aix_hw_obj = AIXHardwareCollector()
    assert aix_hw_obj.platform == 'AIX'
    assert sorted(aix_hw_obj.supported_facts) == sorted(supported_facts_list)

# Generated at 2022-06-13 00:36:57.304812
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    hardware_test = AIXHardware(dict())
    hardware_test.module.run_command = run_command_test
    hardware_test.populate()
    facts = hardware_test.get_cpu_facts()

    assert facts['processor_count'] == 3
    assert facts['processor_cores'] == 4
    assert facts['processor'] == "POWER9"



# Generated at 2022-06-13 00:37:09.446145
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    # Create a class instance
    ah = AIXHardware({})

    # Create a test lsconf output
    lsconf_out = "Machine Type: 0000-1111\n"
    lsconf_out += "Machine Serial Number: FAB 12345\n"
    lsconf_out += "LPAR Info: 1 255\n"
    lsconf_out += "System Model: IBM,1111-22,12345\n"

    # Create facts dictionary
    facts = {}

    # Set lsconf command and its mock output
    facts['command_lsconf'] = '/usr/sbin/lsconf'
    facts['lsconf'] = lsconf_out

    # Get dmi facts
    dmi_facts = ah.get_dmi_facts(facts=facts)

    # Check the results

# Generated at 2022-06-13 00:37:11.361072
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    AIXHardware.get_device_facts('')



# Generated at 2022-06-13 00:37:20.622502
# Unit test for method get_device_facts of class AIXHardware

# Generated at 2022-06-13 00:37:32.248050
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    mem_data = """
memory pages                              (4KB):       9352504
memory pages                              (64KB):           0
memory pages                             (512KB):           0
memory pages                           (4MB):           2

free pages                                 (4KB):       9255467
free pages                                 (64KB):           0
free pages                                (512KB):           0
free pages                              (4MB):           2
"""
    test_module = AnsibleModule(argument_spec={})
    test_hardware = AIXHardware(test_module)
    test_hardware.populate(collected_facts={})
    test_hardware.get_memory_facts(mem_data)
    assert test_hardware.memtotal_mb == 9819
    assert test_hardware.memfree_mb == 9819

#

# Generated at 2022-06-13 00:37:41.520210
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    aix_hardware = AIXHardware()
    mount_facts = aix_hardware.get_mount_facts()
    mounts = mount_facts['mounts']
    for mount in mounts:
        for key, value in mount.iteritems():
            if key == 'mount':
                if value == '/':
                    assert mount['fstype'] == 'jfs2'
                elif value == '/usr':
                    assert mount['fstype'] == 'jfs2'
                elif value == '/var':
                    assert mount['fstype'] == 'jfs2'
                elif value == '/home':
                    assert mount['fstype'] == 'jfs2'

# Generated at 2022-06-13 00:37:47.318701
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():

    class MockModule:
        def run_command(self, cmd):
            lsdev_out = [
                'ent0 Available 02-00-04 Ethernet IVE',
                'ent1 Available 02-00-04 Ethernet IVE',
                'ent2 Available 02-00-04 Ethernet IVE'
            ]
            lsattr_out = [
                'type PowerPC_POWER8',
                'smt_threads 4'
            ]
            if cmd.startswith("/usr/sbin/lsdev"):
                return 0, '\n'.join(lsdev_out), ''
            if cmd.startswith("/usr/sbin/lsattr"):
                return 0, '\n'.join(lsattr_out), ''

    mock_module = MockModule()

# Generated at 2022-06-13 00:38:13.970735
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    test_data_dir = './lib/ansible/module_utils/facts/hardware/aix'
    test_file_path = '%s/test_get_cpu_facts' % test_data_dir
    module = AnsibleModule(argument_spec=dict(
        gather_subset=dict(type='list', elements='str'),
        filter=dict(type='str'),
    ))

    with open(test_file_path) as fd:
        test_data = fd.read()

    hardware = AIXHardware(module)
    results = hardware.get_cpu_facts()
    assert results['processor_count'] == 8
    assert results['processor'] == 'POWER8'
    assert results['processor_cores'] == 2


# Generated at 2022-06-13 00:38:20.540014
# Unit test for method get_vgs_facts of class AIXHardware

# Generated at 2022-06-13 00:38:31.673501
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():

    from ansible.module_utils.facts import TestModule
    from ansible.module_utils.facts.hardware.aix import AIXHardware
    from ansible.module_utils._text import to_bytes

    # Test sample output of /usr/sbin/lsdev -Cc processor
    # Sample output of lsdev -Cc processor - it runs on aix
    test_command_output = 'proc0          Available  00-00 Processor\n' \
                          'proc1          Available  00-01 Processor\n' \
                          'proc2          Available  00-02 Processor\n' \
                          'proc3          Available  00-03 Processor\n'

    # Create test module
    test_module = TestModule({'path': '/usr/sbin:/etc/sbin'})
    # Call get_cpu_facts method of

# Generated at 2022-06-13 00:38:42.068907
# Unit test for method get_mount_facts of class AIXHardware

# Generated at 2022-06-13 00:38:53.715104
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    import sys
    import unittest
    import json

    class FakeAnsibleModule:
        def __init__(self):
            self._result = None
            self._return_value = None

        def get_bin_path(self, executable, required=False):
            return executable

        def run_command(self, executable, use_unsafe_shell=False):
            class FakeAnsibleModuleResult(object):
                def __init__(self):
                    self._result = None
                    self._return_value = None

                def __call__(self, result, return_value):
                    self._result = result
                    self._return_value = return_value
                    return self

                @property
                def rc(self):
                    return self._result

                @property
                def stdout(self):
                    return self._return_value

# Generated at 2022-06-13 00:39:02.342951
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    hardware_facts = AIXHardware()
    hardware_facts_result = hardware_facts.populate()
    assert hardware_facts_result['processor'] == 'PowerPC_POWER8'
    assert hardware_facts_result['firmware_version'] == '8233-EHB-2'
    assert hardware_facts_result['memtotal_mb'] == 1164
    assert hardware_facts_result['memfree_mb'] == 1138
    assert hardware_facts_result['swaptotal_mb'] == 6144
    assert hardware_facts_result['swapfree_mb'] == 6144

# Generated at 2022-06-13 00:39:10.202276
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    facts = AIXHardware().get_memory_facts()
    # These values are specific to my test box.  Change accordingly
    # if these tests are to be run
    expected = {'memtotal_mb': 20480,
                'memfree_mb': 12192,
                'swaptotal_mb': 124223,
                'swapfree_mb':  124056
    }
    for key in expected.keys():
        assert facts[key] == expected[key], 'Expected %s of %d but got %d' % (key, expected[key], facts[key])


# Generated at 2022-06-13 00:39:21.494539
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():

    test_obj = AIXHardware()
    # Create a test string for mount output
    # Two nfs mounts with no mount options
    mount_output = """Filesystem  MB blocks Free %Used    Iused %Iused Mounted on
/dev/hd4         206840 178703   13%   870920     5% /
/dev/hd2         655360 183546   72%  1056650    24% /usr
node1:/home     2048000  92822 100%        0     0% /home
node2:/export     524288  92822 100%        0     0% /export
"""
    # Create a test string for mount output
    # Two nfs mounts with mount options

# Generated at 2022-06-13 00:39:27.855006
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    # pylint: disable=import-error,no-name-in-module
    # Ansible imports
    from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import dict_merge
    from ansible_collections.ansible.netcommon.plugins.module_utils.facts.collector import BaseFactCollector
    # Unit test imports
    from units.module_utils.facts.collector.hardware.aix import AIXHardwareCollector
    from units.module_utils.facts.utils import mock_module

    # Prepared fixture

# Generated at 2022-06-13 00:39:33.929715
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec={})
    hardware = AIXHardware(module)
    facts = hardware.populate()
    assert "processor" in facts
    assert "processor_count" in facts
    assert facts["processor_count"] > 0
    assert "processor_cores" in facts
    assert facts["processor_cores"] > 0


# Generated at 2022-06-13 00:40:07.584312
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    # Create a test instance of AIXHardware and provide a mock_module
    test_instance = AIXHardware({})
    test_instance.module = mock_module = MagicMock()

    # Provide a mock return value for calls to module.run_command
    mock_module.run_command.return_value = (0, '/usr/sbin/lsdev -Cc processor\nproc0 Available 00-00 Processor\nproc4 Available 00-04 Processor\n', '')

    # Execute the code to be tested
    test_instance.get_cpu_facts()

    # Assert that the expected facts are defined
    assert 'processor' in test_instance.facts
    assert 'processor_cores' in test_instance.facts
    assert 'processor_count' in test_instance.facts

    # Assert that the expected value is returned

# Generated at 2022-06-13 00:40:16.512439
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    hardware = AIXHardware()
    hardware.module = DummyAnsibleModule()


# Generated at 2022-06-13 00:40:22.570592
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    module = AnsibleModuleMock(argument_spec={})
    module.exit_json = exit_json

    hardware_obj = AIXHardware(module)

    mount_facts = hardware_obj.get_mount_facts()

    assert mount_facts is not None
    assert 'mounts' in mount_facts
    assert isinstance(mount_facts['mounts'], list)



# Generated at 2022-06-13 00:40:28.867149
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():

    module = AnsibleModule(
        argument_spec=dict(
            filter=dict(default='*', required=False),
            gather_subset=dict(default=['!all'], required=False),
        ),
        supports_check_mode=True)
    ansible_facts = {}

    aix_hardware = AIXHardware(module)
    ansible_facts['ansible_hw_facts'] = aix_hardware.populate()

    module.exit_json(ansible_facts=ansible_facts)


# Generated at 2022-06-13 00:40:35.288927
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    fake_module = object()
    fake_module.run_command = object()
    fake_module.get_bin_path = object()
    fake_module.get_bin_path.return_value = '/usr/sbin/mount'

# Generated at 2022-06-13 00:40:38.115733
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    hardware_collector = AIXHardwareCollector()
    assert hardware_collector.platform == 'AIX'


# Generated at 2022-06-13 00:40:48.831281
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    module = AnsibleModule()
    hardware = AIXHardware(module)
    vgs_facts = hardware.get_vgs_facts()

# Generated at 2022-06-13 00:40:51.410344
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    hw_collector = AIXHardwareCollector()
    assert hw_collector._platform == 'AIX'
    assert hw_collector._fact_class == 'AIXHardware'

# Generated at 2022-06-13 00:40:59.414257
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():

    module = AnsibleModule(argument_spec=dict())
    ah = AIXHardware(module)
    vgs_facts = ah.get_vgs_facts()
    assert sorted(vgs_facts) == ['vgs']

    assert sorted(vgs_facts['vgs']) == ['rootvg', 'realsyncvg', 'testvg']


# Generated at 2022-06-13 00:41:03.145108
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    module = AnsibleModuleMock()
    hardware = AIXHardware(module)
    cpu_facts = hardware.get_cpu_facts()

    assert cpu_facts['processor'] == 'PowerPC_POWER8'
    assert cpu_facts['processor_cores'] == 4
    assert cpu_facts['processor_count'] == 24



# Generated at 2022-06-13 00:41:57.582791
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    module = AnsibleModule(argument_spec={})
    facts = AIXHardware(module).populate()
    assert facts['processor_count'] == 6
    assert facts['processor'] == 'PowerPC_POWER8'
    assert facts['processor_cores'] == 3
    assert facts['memtotal_mb'] == '8168'
    assert facts['memfree_mb'] == '716'
    assert facts['swaptotal_mb'] == '4096'
    assert facts['swapfree_mb'] == '4096'
    assert facts['firmware_version'] == '7235-C4A'
    assert facts['product_serial'] == '00f19bbB0c0'
    assert facts['lpar_info'] == '8'
    assert facts['product_name'] == '8977-AC1'
   

# Generated at 2022-06-13 00:41:59.717158
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():

    # Prepare
    module = MockModule()
    AIXHardwareCollector(module)

    # Assert
    module.fail_json.assert_not_called()

# Generated at 2022-06-13 00:42:02.335514
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    hw_collector = AIXHardwareCollector()
    assert isinstance(hw_collector, HardwareCollector)
    assert hw_collector.platform == 'AIX'
    assert hw_collector._fact_class == AIXHardware


# Generated at 2022-06-13 00:42:09.895910
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    hardware = AIXHardware()
    hardware.module = MagicMock()
    hardware.module.get_bin_path.return_value = "path/to/mount_cmd"

# Generated at 2022-06-13 00:42:19.571809
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    lsdev_path = '/usr/sbin/lsdev'
    lsattr_path = '/usr/sbin/lsattr'
    out1 = b'''
proc0 Available 00-00 Processor
proc1 Available 00-01 Processor
    '''
    out2 = b'''
type PowerPC_POWER7
    '''
    out3 = b'''
smt_threads 2
    '''
    cpu_facts = {
        'processor': 'PowerPC_POWER7',
        'processor_cores': 2,
        'processor_count': 2
    }

    def mock_run_command(arg1, arg2=None):
        rc = 0
        out = b''
        err = b''
        if arg1.strip() == lsdev_path:
            out = out1

# Generated at 2022-06-13 00:42:27.480981
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    module = AnsibleModule(argument_spec={})
    hardware = AIXHardware(module)

    # Test get_cpu_facts
    cpu_facts = hardware.get_cpu_facts()
    assert cpu_facts['processor_cores'] == 0
    assert cpu_facts['processor_count'] == 0

    # Test get_memory_facts
    memory_facts = hardware.get_memory_facts()
    assert memory_facts['memtotal_mb'] == 0
    assert memory_facts['memfree_mb'] == 0

    # Test get_dmi_facts
    dmi_facts = hardware.get_dmi_facts()
    assert dmi_facts['firmware_version'] == ''
    assert dmi_facts['lpar_info'] == ''
    assert dmi_facts['product_name'] == ''
    assert dmi

# Generated at 2022-06-13 00:42:34.275481
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    module = AnsibleModule(argument_spec={})
    harware_facts = AIXHardwareCollector().collect(module, [])

    # Test cpu facts
    assert harware_facts['processor'] == ['POWER8']
    assert harware_facts['processor_cores'] == 4
    assert harware_facts['processor_count'] == 1

    # Test memory facts
    assert harware_facts['memtotal_mb'] == 4313
    assert harware_facts['memfree_mb'] == 4
    assert harware_facts['swaptotal_mb'] == 2047
    assert harware_facts['swapfree_mb'] == 2046

    # Test dmi facts
    assert harware_facts['firmware_version'] == '1.20'

# Generated at 2022-06-13 00:42:44.618295
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    from ansible.module_utils.facts import Collector

    class MockModule(object):
        def __init__(self, name):
            self.name = name
            self.path = ""

        def get_bin_path(self, name, required=False):
            return self.path


# Generated at 2022-06-13 00:42:49.276136
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    class MockModule(object):
        def run_command(self, *cmd):
            return (0,"memory pages:   523776\nfree pages:     523776\n","")

    mock_module = MockModule()
    hardware = AIXHardware(mock_module)
    memory_facts = hardware.get_memory_facts()
    assert memory_facts['memtotal_mb'] == 523776 * 4 / 1024 / 1024
    assert memory_facts['memfree_mb'] == 523776 * 4 / 1024 / 1024

# Unit test to check that get_memory_facts returns correct swaptotal and swapfree
# values when swapinfo command returns good data.

# Generated at 2022-06-13 00:42:52.046301
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    hardware = AIXHardwareCollector()
    assert hardware._platform == 'AIX'
    assert hardware._fact_class.platform == 'AIX'
    assert hardware._fact_class.populate() == hardware.collect()