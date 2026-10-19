

# Generated at 2022-06-13 00:45:29.807073
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    from ansible.module_utils.facts import ModuleFacts
    module_facts = ModuleFacts(module_name='freebsd_hardware_facts', module_runner=None, command_line_args=None)
    hardware_class = FreeBSDHardware(module_facts)
    uptime_facts = hardware_class.get_uptime_facts()
    assert isinstance(uptime_facts['uptime_seconds'], int)
    assert uptime_facts['uptime_seconds'] >= 0

# Generated at 2022-06-13 00:45:37.418305
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    import sys
    import AnsibleModule
    import __builtin__
    try:
        from unittest.mock import MagicMock
    except ImportError:
        from mock import MagicMock

    module = AnsibleModule.AnsibleModule(argument_spec={})
    module.run_command = MagicMock(return_value=[0, '# dmidecode 2.12', ''])
    module.get_bin_path = MagicMock(return_value='/usr/sbin/dmidecode')
    setattr(__builtin__, 'open', MagicMock(return_value=True))

    hardware = FreeBSDHardware(module)
    hardware.get_dmi_facts()

    module.run_command.assert_called_with('/usr/sbin/dmidecode -s bios-release-date')

   

# Generated at 2022-06-13 00:45:46.937976
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():

    class FakeModule:
        def run_command(self, command, encoding=None):
            return (0, "kern.boottime: 1561047255.0 0\n".encode(), "")

        def get_bin_path(self, name):
            return name

    hardware_obj = FreeBSDHardware()
    hardware_obj.module = FakeModule()

    result = hardware_obj.get_uptime_facts()
    assert type(result) is dict
    assert 'uptime_seconds' in result
    assert type(result['uptime_seconds']) is int



# Generated at 2022-06-13 00:45:54.614722
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware
    import pprint
    test_fact = FreeBSDHardware()
    test_fact.module = pprint
    test_fact_result = test_fact.populate()
    assert test_fact_result['processor'] == []
    assert test_fact_result['processor_cores'] == "2"
    assert test_fact_result['processor_count'] == "2"
    assert test_fact_result['devices'] == {}
    assert test_fact_result['uptime_seconds'] == 0

# Generated at 2022-06-13 00:46:03.188904
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    hardware = FreeBSDHardware()

    rc, out, err = hardware.module.run_command("sysctl vm.stats.vm.v_page_size", check_rc=False)
    pagesize = int(out.split()[2])
    rc, out, err = hardware.module.run_command("sysctl vm.stats.vm.v_page_count", check_rc=False)
    pagecount = int(out.split()[2])
    rc, out, err = hardware.module.run_command("sysctl vm.stats.vm.v_free_count", check_rc=False)
    freecount = int(out.split()[2])

    rc, outs, errs = hardware.module.run_command("swapinfo -k")
    data = outs.splitlines()[-1].split()

# Generated at 2022-06-13 00:46:09.150034
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    raw_cpu_facts = {
        'processor': ['AMD Athlon(tm) II X4 640 Processor'],
        'processor_cores': '4',
    }

    pr = FreeBSDHardware()
    cpu_facts = pr._get_cpu_facts()
    assert cpu_facts['processor'] == raw_cpu_facts['processor']
    assert cpu_facts['processor_cores'] == raw_cpu_facts['processor_cores']


# Generated at 2022-06-13 00:46:15.980882
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    module = AnsibleModule(
        argument_spec={
            "gather_subset": dict(default=['!all', '!min'], type='list'),
            "filter": dict(default=None, required=False)
        },
        supports_check_mode=False
    )

    hardware = FreeBSDHardware(module=module)
    hardware_facts = hardware.populate()
    assert hardware_facts['devices'] == {}
    assert hardware_facts['processor'] == []
    assert hardware_facts['processor_cores'] == '1'
    assert hardware_facts['processor_count'] == ''
    assert hardware_facts['memfree_mb'] == ''
    assert hardware_facts['memtotal_mb'] == ''
    assert hardware_facts['swapfree_mb'] == ''

# Generated at 2022-06-13 00:46:25.928028
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    import io
    import os
    import tempfile
    import unittest

    from ansible.module_utils.facts.hardware import FreeBSDHardware

    class TestFreeBSDHardware(unittest.TestCase):
        def test_get_dmi_facts(self):
            tmp_dir = tempfile.mkdtemp()

# Generated at 2022-06-13 00:46:36.110138
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    # Complete execution
    module = AnsibleModule(argument_spec=dict())
    module.get_bin_path = Mock(return_value='/usr/bin/sysctl')
    freebsd_hw = FreeBSDHardware(module)

    # Dummy output of sysctl vm.stats
    out = (
        'vm.stats.vm.v_page_size: 4096\n'
        'vm.stats.vm.v_page_count: 11329\n'
        'vm.stats.vm.v_free_count: 3065\n'
        'vm.stats.vm.v_inactive_clean_count: 2859\n'
        'vm.stats.vm.v_inactive_dirty_count: 8\n'
        'vm.stats.vm.v_wire_count: 590\n')

    #

# Generated at 2022-06-13 00:46:46.754527
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    """
    Unit test for method get_uptime_facts of class FreeBSDHardware
    """
    class ModuleMock:
        class RunCommandModuleMock:
            def __init__(self, rc, out, err):
                self.rc = rc
                self.out = out
                self.err = err

            def run_command(self, cmd, encoding=None):
                return (self.rc, self.out, self.err)

        def __init__(self, rc, out, err):
            self.rc = rc
            self.out = out
            self.err = err
            self.run_command_module_mock = FreeBSDHardwareCollector.test_FreeBSDHardware_get_uptime_facts.RunCommandModuleMock(rc, out, err)

        def get_bin_path(self, command):
            return

# Generated at 2022-06-13 00:47:00.289139
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    fhc = FreeBSDHardwareCollector()
    assert (fhc.platform == 'FreeBSD')
    assert (fhc._fact_class == FreeBSDHardware)


# Generated at 2022-06-13 00:47:10.399262
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():

    # Test values according to dmidecode output
    module = True
    module.run_command = mock_run_command
    test_dmi = FreeBSDHardware(module)

    # The fact value is the json output

# Generated at 2022-06-13 00:47:12.653895
# Unit test for method get_device_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_device_facts():
    device_facts = FreeBSDHardware().get_device_facts()
    check_devices = isinstance(device_facts['devices'], dict)
    assert check_devices


# Generated at 2022-06-13 00:47:14.153257
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    hardware_collector = FreeBSDHardwareCollector()
    assert hardware_collector._platform == 'FreeBSD'

# Generated at 2022-06-13 00:47:15.456809
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    module = AnsibleModule(argument_spec={})
    facts = FreeBSDHardware(module).populate()
    assert 'uptime_seconds' in facts


# Generated at 2022-06-13 00:47:27.011272
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    fake_module = FakeAnsibleModule({'dmesg_boot_content': 'CPU: Intel(R) Core(TM) i7-3770 CPU @ 3.40GHz (3400.03-MHz K8-class CPU)\nLogical CPUs per core: 1\nTotal Memory: 490135 MB\nFree Memory: 467336 MB\nFree Memory: 140777 MB\n'})
    collected_facts = {}
    test_instance = FreeBSDHardware(fake_module, collected_facts)
    test_cpu_facts = test_instance.get_cpu_facts()
    assert test_cpu_facts['processor'] == ['Intel(R) Core(TM) i7-3770 CPU @ 3.40GHz']
    assert test_cpu_facts['processor_cores'] == '1'

# Generated at 2022-06-13 00:47:30.944271
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    module = DummyAnsibleModule()
    hardware_object = FreeBSDHardware(module)
    hardware_object.populate()
    hardware_object.get_cpu_facts()
    assert hardware_object.facts['processor_count'] == hardware_object.module.run_command("sysctl -n hw.ncpu")[1]



# Generated at 2022-06-13 00:47:33.132916
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    fhc = FreeBSDHardwareCollector()
    assert fhc.platform == 'FreeBSD'
    assert fhc.fact_class == FreeBSDHardware


# Generated at 2022-06-13 00:47:41.942789
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware
    from ansible.module_utils.facts.timeout import TimeoutError
    from datetime import date
    import time

    # Get boot time from current time and uptime
    def get_boot_time(uptime):
        return date.fromtimestamp(time.time() - uptime)

    # Convert a date to a datetime object
    def date_to_datetime(date):
        return date.strftime('%Y%m%d') + 'T000000'


# Generated at 2022-06-13 00:47:49.156019
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    fhw = FreeBSDHardware(None)
    fhw._module = type(os)(os)
    fhw._module.get_bin_path = lambda *args: '/usr/sbin/dmidecode'
    fhw._module.run_command = lambda *args: (0, 'bios-version: 1', None)
    facts = fhw.get_dmi_facts()
    assert facts['bios_version'] == '1'

# Generated at 2022-06-13 00:48:06.125559
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    # Use the module's logger for now
    # print("Testing FreeBSDHardwareCollector constructor")
    fhwc = FreeBSDHardwareCollector()
    assert isinstance(fhwc, HardwareCollector)
    assert fhwc._fact_class == FreeBSDHardware
    assert fhwc._platform == 'FreeBSD'
    assert fhwc._last_update > 0



# Generated at 2022-06-13 00:48:08.120696
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    hardware = FreeBSDHardware()

    hardware_facts = hardware.populate()

    assert hardware_facts['uptime_seconds'] > 0

# Generated at 2022-06-13 00:48:18.142582
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    # Create a legacy facts instance and set legacy_mode as True.
    legacy_facts = dict()
    legacy_facts['ansible_facts'] = dict()
    legacy_facts['ansible_facts']['hardware'] = dict()
    legacy_facts['ansible_legacy_mode'] = True

    # Get a FreeBSDHardware instance.
    hardware = FreeBSDHardware()

    # Populate the instance with call to method populate.
    hardware.populate()

    # Verify that we have the expected items in the facts.
    assert 'processor' in hardware.facts
    assert 'processor_cores' in hardware.facts
    assert 'memtotal_mb' in hardware.facts
    assert 'memfree_mb' in hardware.facts
    assert 'swaptotal_mb' in hardware.facts
    assert 'swapfree_mb' in hardware.facts

# Generated at 2022-06-13 00:48:26.636727
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    FAKE_DMESG_BOOT_FILE = "fixtures/fake_dmesg_boot"

    # Assume dmesg.boot file is available
    hardware = FreeBSDHardware(None)
    hardware.DMESG_BOOT = FAKE_DMESG_BOOT_FILE
    cpu_facts = hardware.get_cpu_facts()
    assert cpu_facts['processor'] == ['Intel(R) Core(TM) i7-3770 CPU @ 3.40GHz',
                                      'Intel(R) Core(TM) i7-3770 CPU @ 3.40GHz']
    assert cpu_facts['processor_count'] == '2'
    assert cpu_facts['processor_cores'] == '4'

    # Now assume dmesg.boot file is not available
    hardware = FreeBSDHardware(None)
    hardware.DMESG

# Generated at 2022-06-13 00:48:35.142305
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    # pylint: disable=protected-access
    class MockModule(object):
        @staticmethod
        def run_command(cmd):
            if cmd == ['/usr/sbin/sysctl', '-b', 'kern.boottime']:
                return 0, '\x40\xcc\x05\x2c\x00\x00\x00\x00', None

        @staticmethod
        def get_bin_path(binary):
            return '/usr/sbin/sysctl'

    hardware = FreeBSDHardware()
    hardware.module = MockModule()
    assert hardware.get_uptime_facts() == {'uptime_seconds': 1438237039}

# Generated at 2022-06-13 00:48:37.906659
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    hc = FreeBSDHardwareCollector()
    assert hc.platform == 'FreeBSD'
    assert hc._fact_class == FreeBSDHardware


# Generated at 2022-06-13 00:48:39.062670
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    hw = FreeBSDHardware(None)
    hardware_facts = hw.populate()
    assert hardware_facts['uptime_seconds'] >= 0

# Generated at 2022-06-13 00:48:40.408473
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    collection = FreeBSDHardwareCollector()
    assert collection._platform == 'FreeBSD'

# Generated at 2022-06-13 00:48:44.713307
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    class OptionsModule(object):
        def __init__(self, bin_ansible_callbacks, rc=0, out='', err=''):
            self.bin_ansible_callbacks = bin_ansible_callbacks
            self.rc = rc
            self.out = out
            self.err = err

        def get_bin_path(self, arg, *args, **kwargs):
            if arg == 'dmidecode':
                return self.bin_ansible_callbacks

        def run_command(self, arg, *args, **kwargs):
            return self.rc, self.out, self.err


# Generated at 2022-06-13 00:48:56.674858
# Unit test for method get_device_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_device_facts():
    """
    Test that get_device_facts returns expected device information
    """
    test_obj = FreeBSDHardware()
    test_output = {'devices': {u'da0': [u'da0s1', u'da0s2a', u'da0s2b', u'da0s2c'],
                               u'da1': [u'da1s1'],
                               u'da2': [u'da2s1'],
                               u'da3': [u'da3s1'],
                               u'da4': [u'da4s1']}}
    assert test_obj.get_device_facts() == test_output



# Generated at 2022-06-13 00:49:32.400459
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware

    test_data = {
        'get_mount_facts': '/etc/fstab',
        'get_memory_facts': '/dev/ada0p4',
        'get_cpu_facts': '/dev/ada0p4',
        'get_uptime_facts': '/dev/ada0p4',
        'get_device_facts': '/dev/ada0p4',
        'get_dmi_facts': '/dev/ada0p4',
    }

    hw = FreeBSDHardware({}, test_data)

    uptime_facts = hw.get_uptime_facts()
    assert uptime_facts['uptime_seconds'] > 0

    memory_facts = hw.get_memory_facts()

# Generated at 2022-06-13 00:49:38.877908
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware

    # Arrange
    test_obj = FreeBSDHardware()
    test_obj.module = DummyModule()

    # Act
    result = test_obj.get_dmi_facts()

    # Assert
    assert result['product_name'] == 'VMware Virtual Platform'



# Generated at 2022-06-13 00:49:44.015696
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    """ Unit test for method populate of class FreeBSDHardware """
    h = FreeBSDHardware()
    h.module = MockModule()
    h.module.run_command.return_value = (0, '4096', '')
    h.module.get_bin_path.return_value = '/usr/sbin/sysctl'

    result = h.populate()
    assert result['memfree_mb'] == 3867



# Generated at 2022-06-13 00:49:47.333616
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    from ansible.module_utils.facts.module_freebsd_hardware import FreeBSDHardware
    hardware = FreeBSDHardware()

    assert hardware.get_uptime_facts() == {'uptime_seconds': 0}



# Generated at 2022-06-13 00:49:57.350075
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    import tempfile
    from distutils.version import LooseVersion
    import platform
    from ansible.module_utils._text import to_bytes

    if platform.system() != 'FreeBSD' or LooseVersion(platform.release()) < LooseVersion('10.0'):
        # No way to test this function without FreeBSD 10.0+
        return

    def test_up(value):
        test_dict = FreeBSDHardware().get_uptime_facts()
        assert test_dict['uptime_seconds'] == value, 'Expected: %d, got %d' % (value, test_dict['uptime_seconds'])

    # Create a test file.
    tmpfile = tempfile.NamedTemporaryFile('wb')
    kern_boottime = 123456789

# Generated at 2022-06-13 00:50:06.029435
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    # Test check if FreeBSDHardware.get_uptime_facts works as expected.
    def dummy_run_command(command, **kwargs):
        """Dummy function to return output from dmesg command."""
        return (0, kern_boottime(), '')

    # Test check if FreeBSDHardware.get_uptime_facts return no error.
    module = DummyModule(run_command=dummy_run_command)
    fact_class = FreeBSDHardware(module)
    # Test if expected uptime value is returned.

# Generated at 2022-06-13 00:50:15.645885
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    # mock ansible module
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )

    # mock cpu facts

# Generated at 2022-06-13 00:50:20.250839
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    import sys
    if sys.version_info[0] == 2:
        import mock
    else:
        from unittest import mock

    class MockModule(object):
        def get_bin_path(self, executable):
            return '/usr/local/sbin/dmidecode'

    class MockRunCommand(object):
        def __init__(self, rc, out, err):
            self.rc = rc
            self.out = out
            self.err = err

        def run_command(self, cmd, encoding=None):
            return self.rc, self.out, self.err

    class MockHardware(FreeBSDHardware):
        def __init__(self):
            self.module = MockModule()


# Generated at 2022-06-13 00:50:27.619876
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():

    class AnsibleModule:

        def __init__(self, dmipath):
            self.dmipath = dmipath

        def get_bin_path(self, command):
            if command == 'dmidecode' and os.path.isfile(self.dmipath):
                return self.dmipath
            else:
                return None

        def run_command(self, command, check_rc=False, encoding=None):
            (dmibin, dmiparam) = command.split()
            output = ''

# Generated at 2022-06-13 00:50:37.004359
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    from ansible.module_utils.facts.collector import BaseFactCollector
    class dummyModule:
        def get_bin_path(self, arg):
            return '/usr/sbin/dmidecode'
        def run_command(self, arg, **kwargs):
            if arg == '/usr/sbin/dmidecode -s bios-release-date':
                return (0, '01/26/2015', None)
            if arg == '/usr/sbin/dmidecode -s bios-vendor':
                return (0, 'Phoenix', None)
            if arg == '/usr/sbin/dmidecode -s bios-version':
                return (0, 'V1.25', None)

# Generated at 2022-06-13 00:51:09.772596
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    hardware_obj = FreeBSDHardware()

    # Test empty result
    ret = hardware_obj.get_uptime_facts()
    assert ret == {}

    # Test positive result
    ret = hardware_obj.get_uptime_facts()
    assert ret.get('uptime_seconds') >= 0


# Generated at 2022-06-13 00:51:18.390659
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    from ansible.module_utils.facts import timeout
    from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware
    import time

    # Mock the system uptime using kern.boottime
    sysctl = FreeBSDHardware.module.get_bin_path('sysctl')
    uptime_secs = int(time.time())
    cmd = ['%s -w kern.boottime=%d' % (sysctl, uptime_secs)]
    rc, _, _ = FreeBSDHardware.module.run_command(cmd)
    if rc != 0:
        raise Exception('fail to mock the uptime')

    # Get the uptime
    freebsd_hardware = FreeBSDHardware()
    uptime_facts = freebsd_hardware.get_uptime_facts()

# Generated at 2022-06-13 00:51:26.232293
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    test_module = AnsibleModule(
        argument_spec=dict(),
    )

    test_module.params = {}

    args = {
        'module': test_module
    }

    hw = FreeBSDHardware(args)

    # function to run
    func = 'get_dmi_facts'

    # check if the key is in facts
    facts = hw.get_dmi_facts()

    # check general facts
    bios_date = test_module.get_bin_path('dmidecode')
    bios_vendor = test_module.get_bin_path('dmidecode')
    bios_version = test_module.get_bin_path('dmidecode')
    board_asset_tag = test_module.get_bin_path('dmidecode')
    board_name = test_module.get_

# Generated at 2022-06-13 00:51:36.362453
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    '''Unit test for get_dmi_facts'''
    module = AnsibleModule(argument_spec=dict())
    hw = FreeBSDHardware()
    dmi_facts = hw.get_dmi_facts()

    # dmidecode is not available on some systems, in that case the
    # method should return an empty dict.
    if hw.module.get_bin_path('dmidecode') is None:
        assert dmi_facts == {}
        return

    # Check that the method returns a dictionary
    assert isinstance(dmi_facts, dict)

    # Check that all keys in DMI_DICT are present

# Generated at 2022-06-13 00:51:41.095032
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    module = fake_ansible_module()
    hardware = FreeBSDHardware(module)

    cpu_facts = hardware.get_cpu_facts()

    assert cpu_facts['processor'] == ['Intel(R) Core(TM) i5-5350U CPU @ 1.80GHz']
    assert cpu_facts['processor_cores'] == 1
    assert cpu_facts['processor_count'] == 1


# Generated at 2022-06-13 00:51:48.820371
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    def fake_sysctl(kern_boottime):
        def fake_sysctl_command(*args, **kwargs):
            kern_boottime_str = '{:016x}'.format(kern_boottime)
            return 0, kern_boottime_str, ''
        return fake_sysctl_command

    # Check that the uptime is correct
    kern_boottime = int(time.time()) - 5
    module = FakeModule()
    class FakeFreeBSDModule(object):
        def __init__(self):
            self.module = module
            self.run_command = fake_sysctl(kern_boottime)
    fact_class = FreeBSDHardware(FakeFreeBSDModule())
    uptime_facts = fact_class.get_uptime_facts()


# Generated at 2022-06-13 00:51:53.986008
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    module = AnsibleModule(argument_spec={})
    hardware = FreeBSDHardware(module)

    # always return an int, when rc == 0
    uptime_facts = hardware.get_uptime_facts()
    if not isinstance(uptime_facts['uptime_seconds'], int):
        module.exit_json(changed=False, meta={'uptime_seconds': uptime_facts['uptime_seconds']})
    else:
        module.exit_json(changed=False)



# Generated at 2022-06-13 00:52:05.103278
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():

    # Disable pylint messages for test
    # pylint: disable=no-self-use,unused-argument,protected-access

    from ansible import constants as C

    # Create test instance
    test_instance = FreeBSDHardware()

    # Create virtual command function for call by methods
    class MockModule(object):

        def __init__(self, module_args=None, check_invalid_arguments=False,
                     bypass_checks=False, no_log=False, use_plugins=None,
                     stdin=None, stdout=None, stderr=None, run_once=False,
                     check_conditional=None, context=None):
            self.run_command = Mock(return_value=(0, '', ''))

        def get_bin_path(self, path, required=False):
            return path



# Generated at 2022-06-13 00:52:10.514709
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    module = AnsibleModule(argument_spec={'gather_subset': dict(default=['all'], type='list'),
                                          'filter': dict(required=False, default=None)})
    result = FreeBSDHardware.populate()

    module.exit_json(ansible_facts=dict(hardware=result))


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 00:52:19.602578
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    import os
    import json
    import platform
    import sys
    import tempfile
    import time
    import mock

    import ansible.module_utils.facts.hardware.freebsd
    import ansible.module_utils.facts.hardware.freebsd as FH

    from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware

    cur_time = time.time()
    if platform.system() == 'FreeBSD':
        cur_time_shim = cur_time
    else:
        cur_time_shim = cur_time * 1e6 + 123456

    with tempfile.TemporaryDirectory() as tmpdirname:
        filepath = os.path.join(tmpdirname, 'kern.boottime')
        with open(filepath, 'wb') as f:
            f

# Generated at 2022-06-13 00:53:56.104335
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    class ModuleStub():
        def __init__(self, rc, out, err):
            self.rc = rc
            self.out = out
            self.err = err
            self.run_command_calls = 0

        def get_bin_path(self, name):
            if name == 'sysctl':
                return 'sysctl'

        def run_command(self, command, check_rc=True, encoding=None):
            self.run_command_calls += 1
            if self.run_command_calls > 1:
                return (self.rc, self.out, self.err)

    class AnsibleModuleStub():
        def __init__(self, rc, out, err):
            self.module = ModuleStub(rc, out, err)

    # Test 1: Successful run of 'sysctl

# Generated at 2022-06-13 00:54:01.781165
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    module = mock.MagicMock()
    setattr(module, 'get_bin_path', lambda x: 'swapinfo')
    setattr(module, 'run_command', lambda x: (0, 'Device          1M-blocks     Used    Avail Capacity\n/dev/ada0p3        314368        0   314368     0%', ''))
    hardware = FreeBSDHardware(module)
    memory_facts = hardware.get_memory_facts()
    assert memory_facts == {'swaptotal_mb': 314368, 'swapfree_mb': 314368}



# Generated at 2022-06-13 00:54:07.306056
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    _mock_module = FakeAnsibleModule()
    _mock_module.run_command = FakeRunCommand(
        stdout=open('tests/unittests/utils/module_utils/facts/hardware/FreeBSD/dmesg.boot').read())
    _fbsd_hw = FreeBSDHardware(_mock_module)

# Generated at 2022-06-13 00:54:07.769246
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    return True

# Generated at 2022-06-13 00:54:16.081849
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    import subprocess as sp

    # This is not a real unit test, but this is a simple way to test the
    # FreeBSDHardware class in isolation.
    # This is based on:
    #   https://stackoverflow.com/a/26736342/2476373

    # Set up dummy modules
    class DummyModule:
        class DummyFailJson:
            def __call__(self, msg):
                raise RuntimeError(msg)
        fail_json = DummyFailJson()

        class DummyRunCommand:
            def __init__(self):
                self.cmd = []
                self.rc = 0
                self.out = ''
                self.err = ''
                self.check_rc = True
            def __call__(self, cmd, check_rc=False):
                self.cmd = cmd
                return

# Generated at 2022-06-13 00:54:25.049366
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    import sys
    import tempfile
    from ansible.module_utils.facts.utils import get_file_content
    from ansible.module_utils.facts.timeout import TimeoutError

    th = FreeBSDHardware()
    th.module = sys.modules[__name__]

    dmi_bin = sys.modules[__name__].get_bin_path('dmidecode')

# Generated at 2022-06-13 00:54:33.029704
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    class FreeBSDFakeModule(object):
        def __init__(self):
            self.rc = 0
            self.results = []
            self.run_command_called = False

        def run_command(self, cmd, check_rc=False, encoding=None):
            self.run_command_called = True
            (out, err) = self.results.pop(0)
            return self.rc, out, err

    module = FreeBSDFakeModule()

    # Test with successful command
    test_obj = FreeBSDHardware(module=module)
    module.results = [
        ["bintime 1437262259.049680 sec 16384000 usec", ""],
    ]

    uptime_facts = test_obj.get_uptime_facts()
    assert module.run_command_called

# Generated at 2022-06-13 00:54:40.829799
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    '''
    unit test to check the constructor of class FreeBSDHardwareCollector
    '''
    # create instance of FreeBSDHardwareCollector class
    freebsd_hardware_collector = FreeBSDHardwareCollector()

    # check result of instance of class FreeBSDHardwareCollector
    assert isinstance(freebsd_hardware_collector, HardwareCollector)
    assert isinstance(freebsd_hardware_collector, FreeBSDHardwareCollector)

    # check _fact_class member of instance of class FreeBSDHardwareCollector
    assert freebsd_hardware_collector._fact_class == FreeBSDHardware
    assert freebsd_hardware_collector.fact_class == FreeBSDHardware

    # check _platform member of instance of class FreeBSDHardwareCollector
    assert freebsd_hardware_collector._platform == 'FreeBSD'
    assert freebsd_

# Generated at 2022-06-13 00:54:44.408340
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    fact_dict = FreeBSDHardware().get_cpu_facts()
    assert fact_dict.get('processor_count')
    assert fact_dict.get('processor')
    assert fact_dict.get('processor_cores')

# Generated at 2022-06-13 00:54:46.314297
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    f = FreeBSDHardware()
    assert f.get_uptime_facts() == {'uptime_seconds': 0}