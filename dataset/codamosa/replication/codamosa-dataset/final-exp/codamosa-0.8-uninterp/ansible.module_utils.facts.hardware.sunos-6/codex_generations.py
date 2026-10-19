

# Generated at 2022-06-13 01:06:39.743224
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    context = {}
    context['ansible_facts'] = {}
    context['ansible_facts']['ansible_machine'] = 'i86pc'
    context['ansible_facts']['platform'] = 'SunOS'

    module = FakeAnsibleModule(context=context)

    hware = SunOSHardware(module)
    facts = hware.populate()

    assert facts['system_vendor'] == 'Oracle Corporation'
    assert facts['product_name'] == 'SUNW,SPARC-Enterprise-T5240'
    assert facts['processor_cores'] == 32
    assert facts['processor_count'] == 2
    assert facts['memtotal_mb'] == 131072
    assert facts['swaptotal_mb'] == 268435456
    assert facts['swap_allocated_mb'] == 0


# Generated at 2022-06-13 01:06:52.392230
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    import datetime
    from ansible.module_utils.six import PY3
    import json
    import re

    class FakeModule(object):
        def __init__(self, datetime_class=None):
            self.run_command_kstat_out = \
                'unix:0:system_misc:boot_time\t1548249689\n'
            self.run_command_kstat_rc = 0
            self.datetime_class = datetime_class
            self.datetime_now = None

        def run_command(self, cmd):
            if re.search(r'^/usr/bin/kstat -p unix:0:system_misc:boot_time$', ' '.join(cmd)):
                return self.run_command_kstat_rc, self.run_command_kstat

# Generated at 2022-06-13 01:07:03.007479
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    module_mock = Mock()
    module_mock.run_command.return_value = 1, "", ""
    sunos_hw = SunOSHardware(module_mock)

    # Test a product name that is not in the list of vendors
    sunos_hw._module.run_command.return_value = 1, "System Configuration:     KVM x86", ""
    assert sunos_hw.get_dmi_facts()['system_vendor'] == 'KVM x86'

    # Test a product name that is in the list of vendors
    sunos_hw._module.run_command.return_value = 1, "System Configuration:     Sun Microsystems sun4u", ""
    assert sunos_hw.get_dmi_facts()['system_vendor'] == "Sun Microsystems"

    # Test a product name

# Generated at 2022-06-13 01:07:14.294024
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    """
    For the given test cpufacts, memoryfacts, dmifacts, devicefacts, and uptimefacts
    populate should return the expected values for
    processor, memtotal_mb, system_vendor, product_name, processor_count,
    processor_cores and uptime_seconds
    """

# Generated at 2022-06-13 01:07:26.358889
# Unit test for method get_cpu_facts of class SunOSHardware

# Generated at 2022-06-13 01:07:35.779264
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    class MockRunCommand(object):
        def run_command(self, args, use_unsafe_shell=False):
            if args == ['/usr/bin/kstat cpu_info']:
                return 0, "module:   cpu_info\nbrand:   Sun Microsystems\nchip_id:         1", ''
            elif args == ['/usr/sbin/prtconf']:
                return 0, "Memory size: 8192 Megabytes\nSystem Configuration: Sun Microsystems sun4u", ''
            elif args == ['/usr/platform/SUNW,SPARC-Enterprise/sbin/prtdiag']:
                return 0, "System Configuration: Sun Microsystems sun4u\nSystem Configuration: Sun Microsystems sun4v\nSystem Configuration: Sun Microsystems sun4us", ''

# Generated at 2022-06-13 01:07:40.534446
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    module = MagicMock()
    module.run_command = MagicMock(return_value=[0, 'Memory size: 32768 Megabytes', ''])
    hardware = SunOSHardware(module)
    result = hardware.get_memory_facts()
    assert result['memtotal_mb'] == 32768


# Generated at 2022-06-13 01:07:46.084989
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    # FIXME: We should be mocking out run_command so we don't need to require root
    module = AnsibleModule(argument_spec={})
    fact_retriever = SunOSHardware(module)
    facts = fact_retriever.populate()

    assert facts['memtotal_mb'] > 0
    assert facts['swapfree_mb'] > 0
    assert facts['swaptotal_mb'] > 0
    assert facts['swap_allocated_mb'] > 0
    assert facts['swap_reserved_mb'] > 0

# Generated at 2022-06-13 01:07:47.542881
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    h = SunOSHardware()
    h.module.run_command = lambda *args, **kwargs: (0, '', '')

# Generated at 2022-06-13 01:07:53.345246
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    module = AnsibleModule(argument_spec={})
    # Testing SunOS 11.2

# Generated at 2022-06-13 01:08:17.336414
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    """
    This test is for method get_cpu_facts() of class SunOSHardware.
    """

    # Execute this method with the following output
    out = """module:   cpu_info
instance: 0
class:    misc
chip_id   0
clock_MHz 3000
state     ok
module:   cpu_info
instance: 1
class:    misc
chip_id   1
clock_MHz 3000
state     ok
module:   cpu_info
instance: 2
class:    misc
chip_id   2
clock_MHz 3000
state     ok"""

    # Create SunOSHardware object.
    SunOS_hw = SunOSHardware(None)

    # Execute get_cpu_facts() method with input out
    cpu_facts = SunOS_hw.get_cpu_facts()

    # Check the output.
    assert cpu_

# Generated at 2022-06-13 01:08:24.706842
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes

    module = AnsibleModule(argument_spec={})
    module.run_command = lambda x, *args, **kwargs: (0, to_bytes('''
System Configuration: VMware,  Inc. VMware Virtual Platform
Memory size: 8192 Megabytes

== Physical Memory Resources (pagesize 8192 bytes) ==

Current       Peak
Total         Used        Available      Used        Available
Memory        Memory
------        ------      ------         ------      ------
8388634       7292        8321811        7290        8322032
'''), to_bytes(''))
    hardware = SunOSHardwareCollector(module).collect()['ansible_facts']['ansible_hardware']

# Generated at 2022-06-13 01:08:31.767956
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    module = AnsibleModuleMock()
    module.run_command = MagicMock(return_value=(0, 'Memory size: 32768 Megabytes', ""))
    sunos_hardware = SunOSHardware()
    sunos_hardware.module = module
    result = sunos_hardware.get_memory_facts()
    assert result == {'memtotal_mb': 32768}



# Generated at 2022-06-13 01:08:41.211073
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    class MyModule(object):
        def get_bin_path(self, arg, opt_dirs=[]):
            return '/usr/sbin/prtdiag'

        def run_command(self, args):
            if args == ['/usr/sbin/prtdiag']:
                return 0, """System Configuration: Oracle Corporation  sun4v  SPARC Enterprise T2000
System Configuration: QEMU Standard PC (i440FX + PIIX, 1996)
System Configuration: VMware, Inc.    VMware Virtual Platform
System Configuration: Sun Microsystems sun4v SPARC Enterprise T2000
System Configuration: Oracle Corporation sun4v SPARC T4-4
System Configuration: Sun Microsystems sun4v SPARC Enterprise T2000", """

    platform = SunOSHardware(MyModule())
    dmi_facts = platform.get_dmi_facts()

# Generated at 2022-06-13 01:08:48.000101
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    mock_module = AnsibleModuleMock()
    mock_module.run_command_environ_update = {'LANG': 'C', 'LC_ALL': 'C'}
    SunOS_hw = SunOSHardware(mock_module)
    SunOS_hw.populate()

    assert mock_module.run_command.called
    assert type(SunOS_hw.facts) is dict


# Generated at 2022-06-13 01:08:55.955748
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    module = FakeAnsibleModule(platform='SunOS')
    class_mocker = ClassMocker()
    class_mocker.mock_module(module)
    module.run_command.return_value = (0, 'unix:0:system_misc:boot_time    1548249689', None)
    uptime_facts = SunOSHardware(module=module).get_uptime_facts()
    expected_facts = {'uptime_seconds': int(time.time() - 1548249689)}
    assert uptime_facts == expected_facts


# Generated at 2022-06-13 01:09:08.067077
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    class module:
        def __init__(self):
            self.exit_json = exit_json
        def run_command(self, args, check_rc=True):
            return rc, out, err
    def exit_json(**kw):
        pass


# Generated at 2022-06-13 01:09:12.219366
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    module = AnsibleModule(argument_spec={})
    hardware = SunOSHardware(module)
    hardware.populate()
    assert hardware.facts['system_vendor'] == 'QEMU'
    assert hardware.facts['product_name'] == 'Standard PC (i440FX + PIIX, 1996)'



# Generated at 2022-06-13 01:09:19.364850
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    from ansible.module_utils.six import StringIO
    mock_module = StringIO()

# Generated at 2022-06-13 01:09:26.176752
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    import sys
    import os
    import stat
    import inspect

    from ansible.module_utils.facts.hardware.sunos import SunOSHardware

    # create the SunOSHardware class object with the module_utils object
    module_args = {}
    module = AnsibleModuleMock(**module_args)
    hardware_obj = SunOSHardware(module)

    # get the path of the SunOSHardware class
    hardware_path = os.path.dirname(inspect.getfile(SunOSHardware))

    # replace the kstat binary with a script
    kstat = os.path.join(hardware_path, '_get_device_facts.sh')
    os.chmod(kstat, stat.S_IRWXU)
    os.environ['ANSIBLE_KSTAT_BIN'] = kstat

    #

# Generated at 2022-06-13 01:10:07.102826
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    module = FakeAnsibleModule()
    module.run_command_environ_update = {'LANG': 'C', 'LC_ALL': 'C', 'LC_NUMERIC': 'C'}

    def fake_run_command(*args, **kwargs):
        """
        get_dmi_facts() calls run_command(). Override it to provide
        canned responses for the unit tests.
        """
        if args[0] == "/usr/bin/uname -i":
            return 0, "i86pc\n", None
        elif args[0][-8:] == "prtdiag":
            return 0, "System Configuration: Oracle Corporation sun4v\nSun Fire X4270 M2 Server", None

    # This is the output of prtdiag on one of our test systems.
    # It is included here

# Generated at 2022-06-13 01:10:13.219784
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():

    hardware = SunOSHardware()
    hardware.module = MagicMock()
    hardware.module.run_command.return_value = 0, "", ""

    hardware.populate()

    hardware.module.run_command.assert_any_call("/usr/sbin/prtconf")
    hardware.module.run_command.assert_any_call("/usr/sbin/swap -s")



# Generated at 2022-06-13 01:10:17.345312
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    module = AnsibleModule(argument_spec={})
    hardware_obj = SunOSHardware(module)
    dmi_facts = hardware_obj.get_dmi_facts()

    assert isinstance(dmi_facts, dict)
    assert 'system_vendor' in dmi_facts
    assert 'product_name' in dmi_facts


# Generated at 2022-06-13 01:10:23.642067
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    pf = 'SunOS'
    module = type('', (), {})()

    module.get_bin_path = lambda x: x
    module.run_command = lambda x: ("0", 1548411849, "")

    h = SunOSHardware(module=module)
    result = h.get_uptime_facts()
    expected = { 'uptime_seconds': 3600 }
    assert result == expected


# Generated at 2022-06-13 01:10:34.358133
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    '''Unit test for method get_cpu_facts of class SunOSHardware'''

    hardware = SunOSHardware()

    hardware.module = MockModule()
    hardware.module.run_command.return_value = (0, CPU_FACTS_CONTENT, '')

    cpu_facts = hardware.get_cpu_facts()

    assert cpu_facts['processor_count'] == 16
    assert cpu_facts['processor_cores'] == 16

# Generated at 2022-06-13 01:10:42.376196
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    fake_module = AnsibleModuleMock()
    fake_module.run_command.return_value = (0, "System Configuration: VMware, Inc. VMware Virtual Platform", "")

    hardware = SunOSHardware(fake_module)

    dmi_facts = hardware.get_dmi_facts()

    # Check that we get the right values
    fake_module.run_command.assert_called_with('/usr/bin/uname -i')

    assert (dmi_facts['system_vendor'] == 'VMware, Inc.')
    assert (dmi_facts['product_name'] == 'VMware Virtual Platform')



# Generated at 2022-06-13 01:10:46.234166
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )

    # FIXME: This test will fail if it is executed on a different platform
    h = SunOSHardware(module=module)
    module.exit_json(ansible_facts=h.populate())



# Generated at 2022-06-13 01:10:56.425945
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    module = AnsibleModule(argument_spec={})

    # Create an instance of the SunOSHardware class
    sunos_hardware_instance = SunOSHardware(module)

    # Create a facts structure and add an empty devices dictionary to it
    facts_dict = {}
    facts_dict['devices'] = {}

    # Create device_facts_dict which is what we expect the function to return
    device_facts_dict = {}

# Generated at 2022-06-13 01:11:00.668923
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    hardware_facts = SunOSHardware()
    hardware_facts.module = AnsibleModuleMock()
    hardware_facts.module.run_command_environ_update = {'LANG': 'C', 'LC_ALL': 'C', 'LC_NUMERIC': 'C'}



# Generated at 2022-06-13 01:11:02.145431
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    module = AnsibleModule(argument_spec={})
    facts = SunOSHardware().get_memory_facts()
    assert facts['memtotal_mb'] is not None

# Generated at 2022-06-13 01:12:16.031583
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    test_data = [
        (
            '\nSystem Configuration: VMware, Inc. VMware Virtual Platform\n',
            dict(system_vendor="VMware, Inc.", product_name="VMware Virtual Platform")
        ),
        (
            '\nSystem Configuration: Sun Microsystems  sun4v SPARC T4-2 Server\n',
            dict(system_vendor="Sun Microsystems", product_name="sun4v SPARC T4-2 Server")
        )
    ]
    for data, dmi_facts in test_data:
        test = SunOSHardware()
        test.module = MagicMock()
        test.module.run_command.return_value = (
            0,
            data,
            '',
        )
        result = test.get_dmi_facts()
        assert result == dmi

# Generated at 2022-06-13 01:12:27.699614
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    module = MagicMock()
    hardware = SunOSHardware(module)
    module.run_command = MagicMock(return_value=(0, "/usr/bin/kstat cpu_info", ""))
    hardware.get_cpu_facts = MagicMock(return_value=dict())
    hardware.get_memory_facts = MagicMock(return_value=dict())
    hardware.get_mount_facts = MagicMock(return_value=dict())
    hardware.get_dmi_facts = MagicMock(return_value=dict())
    hardware.get_device_facts = MagicMock(return_value=dict())
    hardware.get_uptime_facts = MagicMock(return_value=dict())

    hardware.populate()

    hardware.get_cpu_facts.assert_called_once_with()

# Generated at 2022-06-13 01:12:36.288062
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    SunOSHardware.platform = 'SunOS'

    class TestModuleArgumentSpec:
        def __init__(self):
            self.supports_check_mode = False
            self.argument_spec = dict()

        def run_command(self, args, check_rc=True, environ_update=None):
            test_cases = {
                'prtconf': (0, 'Memory size: 8192 Megabytes', ''),
                'swap -s': (0, 'Total: 496788k bytes allocated + 76684k reserved = 573472k used, 2608360k available', '')
            }
            return test_cases[args[0]]

    class TestAnsibleModule:
        def __init__(self):
            self.params = dict()
            self.argument_spec = TestModuleArgumentSpec().argument

# Generated at 2022-06-13 01:12:48.461837
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    import json


# Generated at 2022-06-13 01:12:57.762563
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    # FIXME: This unit test is incorrect
    facter = SunOSHardware()
    facts = facter.get_device_facts()
    assert facts['devices']['sd0']['product'] == 'VBOX HARDDISK'
    assert facts['devices']['sd0']['revision'] == '1.0'
    assert facts['devices']['sd0']['serial'] == 'VB0ad2ec4d-074a'
    assert facts['devices']['sd0']['size'] == '50GB'
    assert facts['devices']['sd0']['vendor'] == 'ATA'
    assert facts['devices']['sd0']['hard_errors'] == '0'
    assert facts['devices']['sd0']['soft_errors'] == '0'

# Generated at 2022-06-13 01:13:05.137049
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    # Empty dict input
    facts = {}
    # Get an instance of SunOSHardware class
    hardware = SunOSHardware()
    # Populate the facts dict with SunOSHardware data
    facts = hardware.populate()

    assert facts['processor_count'] > 0
    assert isinstance(facts['processor'], list)
    assert isinstance(facts['ansible_devices'], dict)
    assert facts['ansible_devices'] != {}
    assert isinstance(facts['ansible_uptime_seconds'], int)
    assert facts['ansible_uptime_seconds'] > 0
    assert isinstance(facts['ansible_mounts'], list)
    assert facts['ansible_mounts'] != []

# Generated at 2022-06-13 01:13:15.453927
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    device_facts = {}
    device_facts['devices'] = {}

    disk_stats = {
        'Product': 'product',
        'Revision': 'revision',
        'Serial No': 'serial',
        'Size': 'size',
        'Vendor': 'vendor',
        'Hard Errors': 'hard_errors',
        'Soft Errors': 'soft_errors',
        'Transport Errors': 'transport_errors',
        'Media Error': 'media_errors',
        'Predictive Failure Analysis': 'predictive_failure_analysis',
        'Illegal Request': 'illegal_request',
    }

    cmd = ['/usr/bin/kstat', '-p']

    for ds in disk_stats:
        cmd.append('sderr:::%s' % ds)

    d = {}


# Generated at 2022-06-13 01:13:22.943676
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    test_hardware = SunOSHardware()
    test_hardware.module = AnsibleModule(argument_spec={})
    test_fstab = """System Configuration: VMware, Inc. VMware Virtual Platform
                   System Configuration: QEMU Standard PC (i440FX + PIIX, 1996)
                   System Configuration: Sun Microsystems sun4v
                   System Configuration: Oracle Corporation sun4v
                   System Configuration: Oracle Corporation sun4u
                   System Configuration: Fujitsu PRIMERGY RX200 S6"""
    test_hardware.module.run_command = mock.MagicMock(return_value=(0, test_fstab, None))

    dmi_facts = test_hardware.get_dmi_facts()

    assert dmi_facts['product_name'] == "VMware Virtual Platform"

# Generated at 2022-06-13 01:13:27.119660
# Unit test for method get_cpu_facts of class SunOSHardware

# Generated at 2022-06-13 01:13:35.280668
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    # This populates the `ansible_facts`
    SunOSHardware().populate()

    # Using the module_utils facts helper
    results = get_file_content('/tmp/facts')
    assert results['ansible_facts']['ansible_processor_count'] == 1
    assert results['ansible_facts']['ansible_processor_cores'] == 1
    assert 'ansible_memtotal_mb' in results['ansible_facts']
    assert 'ansible_swapfree_mb' in results['ansible_facts']
    assert 'ansible_swaptotal_mb' in results['ansible_facts']
    assert 'ansible_processor' in results['ansible_facts']
