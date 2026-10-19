

# Generated at 2022-06-13 00:45:31.937414
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    module = FakeAnsibleModule()
    hardware_facts_instance = FreeBSDHardware(module)
    dmi_facts = hardware_facts_instance.get_dmi_facts()
    assert dmi_facts['system_vendor'] == "LENOVO"
    assert dmi_facts['product_name'] == "30BCCTO1WW"
    assert dmi_facts['product_version'] == "ThinkPad T420"
    assert dmi_facts['product_serial'] == "R9F0N34"
    assert dmi_facts['product_uuid'] == "eb1a0b2e-9069-11e8-9cd4-08002794d571"
    assert dmi_facts['chassis_serial'] == "None"

# Generated at 2022-06-13 00:45:38.874449
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    hw = FreeBSDHardware()
    rc, out, err = hw.module.run_command("%s vm.stats" % hw.module.get_bin_path('sysctl'), check_rc=False)
    for line in out.splitlines():
        data = line.split()
        if 'vm.stats.vm.v_page_size' in line:
            pagesize = int(data[1])
        if 'vm.stats.vm.v_page_count' in line:
            pagecount = int(data[1])
        if 'vm.stats.vm.v_free_count' in line:
            freecount = int(data[1])
    swapinfo = hw.module.get_bin_path('swapinfo')

# Generated at 2022-06-13 00:45:45.387326
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware
    hw = FreeBSDHardware()
    assert hw.get_memory_facts() == {'memtotal_mb': 3025, 'swaptotal_mb': 3072, 'swapfree_mb': 3072, 'memfree_mb': 2852}

# Generated at 2022-06-13 00:45:51.729440
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    """Unit test for method get_uptime_facts of class FreeBSDHardware."""
    module = FakeAnsibleModule()
    freebsd_hardware = FreeBSDHardware(module)
    uptime_facts = freebsd_hardware.get_uptime_facts()

    # Currently, simply verify that 'uptime_seconds' is present and isn't None.
    assert 'uptime_seconds' in uptime_facts
    assert uptime_facts['uptime_seconds'] is not None


# Generated at 2022-06-13 00:45:53.625514
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    collector = FreeBSDHardwareCollector()
    assert collector is not None
    assert collector._fact_class.platform == 'FreeBSD'

# Generated at 2022-06-13 00:45:56.918522
# Unit test for method get_device_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_device_facts():
    module = AnsibleModule(argument_spec={})

    hardware = FreeBSDHardware(module=module)
    res = hardware.get_device_facts()
    assert res['devices'] is not None



# Generated at 2022-06-13 00:46:04.426927
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    try:
        import re
        import subprocess
        import sys
        import unittest
        import mock
    except ImportError:
        print('skipping unit test')
        sys.exit()

    def check_mem(obj, l):
        # l: searchline
        # Return memory information value, abort if not found
        n = l.index('=')
        l = l[n + 1:]
        return l

    def get_output(obj, fname):
        f = open(fname, 'r')
        s = ''
        for l in f:
            if l.startswith('#'):
                continue
            if l.strip() != '':
                s += l
        return s


# Generated at 2022-06-13 00:46:08.606023
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    class MockModule:
        def get_bin_path(self, command):
            class FakeCommand:
                def __init__(self, command):
                    pass
                def __call__(self, *args, **kwargs):
                    if command == 'sysctl':
                        return (0, b'kern.boottime: { sec = 1570042570, usec = 893396 }', b'')
                    return (1, b'', b'not found')
            return FakeCommand(command)

    m = MockModule()
    f = FreeBSDHardware()

    f.module = m
    facts = f.get_uptime_facts()
    assert facts['uptime_seconds'] == 19094

# Generated at 2022-06-13 00:46:13.469688
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    module = AnsibleModule(
        argument_spec={'gather_subset': dict(default=['!all'], type='list')}
    )

# Generated at 2022-06-13 00:46:15.410430
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    m = FreeBSDHardware()
    assert 'uptime_seconds' in m.get_uptime_facts()

# Generated at 2022-06-13 00:46:35.703272
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    content = 'vm.stats.vm.v_page_count: 609272\n'
    content += 'vm.stats.vm.v_page_size: 4096\n'
    content += 'vm.stats.vm.v_page_free_count: 247717\n'

# Generated at 2022-06-13 00:46:46.110015
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    # The kern.boottime sysctl returns a timestamp, in a special format. This
    # test verifies that the converted value is correct.
    from datetime import datetime

    # On FreeBSD, the default format is annoying to parse.
    # Use -b to get the raw value and decode it.
    sysctl_cmd = '/sbin/sysctl'
    cmd = [sysctl_cmd, '-b', 'kern.boottime']
    out = b'1535733078 1684017\n'

    # We need to get raw bytes, not UTF-8.
    rc, out, err = 256, out, b''

    # kern.boottime returns seconds and microseconds as two 64-bits
    # fields, but we are only interested in the first field.
    struct_format = '@L'
    struct_size

# Generated at 2022-06-13 00:46:57.372985
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    module = MockModule()
    hardware = FreeBSDHardware(module)

    # The first two samples are taken from a system where sysctl is
    # available, while the third is the output of sysctl on FreeBSD 11.0
    # (which has switched to a new format)

# Generated at 2022-06-13 00:47:02.439710
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    module = AnsibleModule(argument_spec={})
    hardware = FreeBSDHardware(module)


# Generated at 2022-06-13 00:47:11.808891
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    # Why: get_dmi_facts should return the bios_version from dmidecode
    from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware
    # Arrange
    fb_hardware = FreeBSDHardware()
    fb_hardware.module.get_bin_path = lambda x: "/usr/local/sbin/dmidecode"
    # Act
    fb_hardware.module.run_command = lambda x: ("0", "WZ520A.86A.0031.2019.0607.1940", "")
    # Assert
    assert (fb_hardware.get_dmi_facts()["bios_version"] == "WZ520A.86A.0031.2019.0607.1940")

# Generated at 2022-06-13 00:47:16.744277
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware
    from datetime import datetime, timezone, timedelta

    # Get a timezone offset and convert it to the string representation used
    # by the FreeBSD uptime sysctl.
    #
    # TODO: Ideally, we would use the system timezone here. However, since
    # all of our tests are running in UTC, our local timezone would be
    # `UTC+00:00`, which is not handled correctly by FreeBSD. Hard-coding
    # the offset until we have a way to obtain the system timezone.
    gmt_offset = '+01:00'

    # the FreeBSD uptime sysctl returns the number of seconds since
    # boot. Compute the number of seconds that have passed since
    # Jan 1, 1970 for the test.
    t0

# Generated at 2022-06-13 00:47:28.865371
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    """ Verifies method get_dmi_facts of class FreeBSDHardware """
    import tempfile
    import os

    # setup for unit test, below is an example output of dmidecode command
    #
    # # dmidecode 2.12
    # SMBIOS 2.4 present.
    #
    # Handle 0x0000, DMI type 0, 24 bytes
    # BIOS Information
    #     Vendor: Intel Corp.
    #     Version: 6ECN35WW (3.26 )
    #     Release Date: 04/13/2012
    #     Address: 0xE0000
    #     Runtime Size: 128 kB
    #     ROM Size: 1536 kB
    #     Characteristics:
    #         PCI is supported
    #         BIOS is upgradeable
    #         BIOS shadowing is allowed
    #         Boot from CD is

# Generated at 2022-06-13 00:47:34.764880
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    fh = FreeBSDHardware({})
    facts = fh.populate()
    expected_facts = {
        'processor': ['Intel(R) Core(TM) i7-3770 CPU @ 3.40GHz'],
        'processor_cores': '4',
        'processor_count': '1'
    }
    assert facts == expected_facts
    assert isinstance(facts['processor'], list)
    assert isinstance(facts['processor_cores'], str)
    assert isinstance(facts['processor_count'], str)



# Generated at 2022-06-13 00:47:41.160659
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    m = FreeBSDHardware()
    def run_command(self, cmd, check_rc=True, encoding=None, data=None):
        return 0, "cpu0:  Intel(R) Core(TM) i3-2130 CPU @ 3.40GHz", ""
    m.module.run_command = run_command
    facts = m.get_cpu_facts()
    assert facts['processor'] == ['Intel(R) Core(TM) i3-2130 CPU @ 3.40GHz']
    assert facts['processor_count'] == 1



# Generated at 2022-06-13 00:47:53.654134
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    module = MagicMock()
    module.run_command.return_value = 0, 'some_value', ''

    fbsd_hw = FreeBSDHardware(module)

# Generated at 2022-06-13 00:48:23.683309
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    from ansible.module_utils.facts import FactCache

    module_mock = Mock()
    fact_mock = Mock()

    fh = FreeBSDHardware(module_mock, fact_mock)

    # mock structure
    # rc: return code
    # out: bytes output of sysctl -b, with boottime in seconds since the epoch
    # err: stderr output if any
    #
    # We mock two different outputs, one with and one without a fractional
    # part in seconds. We use the same value for both tests, which is the
    # epoch value for midnight 2020-07-17. We force a return value of
    # 2020-07-17T00:00:00 UTC as the uptime_seconds.

    # Without a fractional part in seconds
    rc = 0
    # bytes value of the epoch timestamp = 159

# Generated at 2022-06-13 00:48:34.895258
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    module = AnsibleModule(argument_spec={})
    collected_facts = {}
    hardware_facts = FreeBSDHardware(module)
    hardware_facts.populate(collected_facts)

    assert 'uptime_seconds' in collected_facts
    assert 'memfree_mb' in collected_facts
    assert 'memtotal_mb' in collected_facts
    assert 'swapfree_mb' in collected_facts
    assert 'swaptotal_mb' in collected_facts
    assert 'processor' in collected_facts
    assert 'processor_cores' in collected_facts
    assert 'processor_count' in collected_facts
    assert 'devices' in collected_facts
    assert 'mounts' in collected_facts


from ansible.module_utils.basic import *  # noqa: F841


# Generated at 2022-06-13 00:48:44.928546
# Unit test for method get_dmi_facts of class FreeBSDHardware

# Generated at 2022-06-13 00:48:51.814833
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )
    if not module.check_mode:
        module.exit_json(
            ansible_facts = dict(
                hardware = Hardware().populate()
            )
        )


# Generated at 2022-06-13 00:49:02.985954
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():

    # dmidecode does not exist on this platform
    module = get_test_module(dict(freebsd_version=901050))
    facts = FreeBSDHardware(module).get_dmi_facts()


# Generated at 2022-06-13 00:49:05.212344
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    fhc = FreeBSDHardwareCollector()
    assert fhc.platform == 'FreeBSD'
    assert fhc.fact_class._platform == 'FreeBSD'

# Generated at 2022-06-13 00:49:13.626500
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    import platform
    from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware
    from ansible.module_utils.facts.timeout import TimeoutError
    from ansible.module_utils.facts.utils import get_file_content

    from ansible_collections.ansible.community.tests.unit.compat import unittest

    class StubModule(object):
        """Stubs the relevant methods from the ansible module."""

        def run_command(self, args, check_rc=False):
            if args[0] == 'dmidecode':
                return 0, DMI_OUTPUT, ''
            else:
                raise Exception("unexpected command: %s" % args)

        def get_bin_path(self, name):
            return '/usr/sbin/%s' % name


# Generated at 2022-06-13 00:49:21.908043
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    """ Unit test for method FreeBSDHardware.get_uptime_facts

        FreeBSDHardware.get_uptime_facts must return exactly the same
        result as the shell command 'date +%%s' - 'kern.boottime' from sysctl
    """
    from ansible.module_utils.facts.timeout import timeout
    from ansible.module_utils.facts.utils import get_file_content

    dmesg_boot = get_file_content('/var/run/dmesg.boot')
    for line in dmesg_boot.splitlines():
        if 'Booting' in line:
            boot_time = line.split()[-2:-1]

    uptime_seconds = int(time.time()) - int(boot_time[0])


# Generated at 2022-06-13 00:49:32.532930
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    # Test setup
    module = MockModule()
    dmi_info = OrderedDict()
    dmi_info['system-manufacturer'] = "FUJITSU"
    dmi_info['system-product-name'] = "VL10"
    dmi_info['system-uuid'] = "1A2B3C4D-1A2B-1A2B-1A2B-1A2B3C4D5E6F"
    dmi_info['system-serial-number'] = "Test"
    dmi_info['system-version'] = "Test"
    dmi_info['bios-release-date'] = "08/30/2012"
    dmi_info['bios-vendor'] = "FUJITSU//Phoenix Technologies LTD"

# Generated at 2022-06-13 00:49:43.642508
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    m = FreeBSDHardware()

    # Test that an empty output raise an exception
    cmd = ['/bin/true']
    rc, out, err = m.module.run_command(cmd, encoding=None)
    assert rc == 0
    assert len(out) == 0
    try:
        m.get_uptime_facts()
        assert False
    except Exception:
        assert True

    # Test that an insufficient output raise an exception
    cmd = ['/bin/true']
    rc, out, err = m.module.run_command(cmd, encoding=None)
    assert rc == 0
    assert len(out) == 0
    try:
        m.get_uptime_facts()
        assert False
    except Exception:
        assert True

    # Test that an incorrect output raise an exception

# Generated at 2022-06-13 00:50:47.039777
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    mod = AnsibleModule(argument_spec={})
    x = FreeBSDHardware(mod)
    x.populate()
    assert x.data['uptime_seconds'] is not None
    assert x.data['memfree_mb'] > 0
    assert x.data['memtotal_mb'] > 0
    assert len(x.data['processor']) > 0
    assert x.data['processor_cores'] is not None
    assert x.data['processor_count'] is not None
    assert x.data['devices'] is not None
    assert x.data['bios_date'] is not None
    assert x.data['bios_vendor'] is not None
    assert x.data['bios_version'] is not None
    assert x.data['board_asset_tag'] is not None

# Generated at 2022-06-13 00:50:52.017997
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    module = get_module_mock()
    sysctl = get_bin_path_mock(module)
    if sysctl is None:
        sysctl = get_bin_path_mock(module, True)
    if sysctl:
        module.run_command = get_run_command_mock()
        syctl_output = '''
vm.stats.vm.v_page_size: 16384
vm.stats.vm.v_page_count: 779204
vm.stats.vm.v_free_count: 779204'''
        module.run_command.return_value = (0, syctl_output, "")
        hardware = FreeBSDHardware(module)
        memory_facts = hardware.get_memory_facts()

# Generated at 2022-06-13 00:50:55.935581
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    hardware = FreeBSDHardware()
    output = hardware.populate()

    assert output['processor'][0] == 'Genuine Intel(R) CPU 0000 @ 2.30GHz'
    assert output['processor_cores'] == '1'
    assert output['processor_count'] == '1'
    assert output['devices'] != {}
    assert output['mounts'][0]['size_total'] == 2047


# Generated at 2022-06-13 00:50:59.450842
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    module = DummyAnsibleModule()
    obj = FreeBSDHardwareCollector(module)
    assert obj.platform == 'FreeBSD'
    assert obj.fact_class == FreeBSDHardware


# Generated at 2022-06-13 00:51:04.853497
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )

    hardware = FreeBSDHardware(module)
    hardware_facts = hardware.populate()
    assert hardware_facts['uptime_seconds'] > 0
    assert hardware_facts['devices'] is not None
    assert hardware_facts['processor'] is not None
    assert hardware_facts['memtotal_mb'] > 0


# Generated at 2022-06-13 00:51:10.553186
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    test_module = type('test_module', (object,), {})
    test_module.get_bin_path = lambda x: ''
    test_module.run_command = lambda x: (0, '', '')
    test_module._get_file_content = lambda x: ''
    test_module._get_mount_size = lambda x: {}
    test_freebsd_hardware = FreeBSDHardware(test_module)
    test_freebsd_hardware.populate()
    assert test_freebsd_hardware.platform == 'FreeBSD'


# Generated at 2022-06-13 00:51:15.518305
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    class _ModuleExit(Exception):
        pass

    class BIN_PATH:
        sysctl = '/sbin/sysctl'

    class _Module(object):
        def __init__(self):
            self.params = {}

        def get_bin_path(self, arg, opt_dirs=[]):
            return BIN_PATH.get(arg)

        def run_command(self, args, check_rc=True, close_fds=True, executable=None, data=None, binary_data=False, path_prefix=None, cwd=None, use_unsafe_shell=False, prompt_regex=None, environ_update=None, umask=None, encoding=None):
            class _NamedTuple(object):
                pass
            rc = 0

# Generated at 2022-06-13 00:51:22.992169
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():

    from ansible_collections.ansible.community.tests.unit.modules.utils import set_module_args
    module = AnsibleModule(
        argument_spec={
            'gather_subset': dict(default=['all'], type='list'),
            'gather_timeout': dict(default=10, type='int')
        },
        supports_check_mode=False
    )


# Generated at 2022-06-13 00:51:26.975178
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    class TestModule:
        def get_bin_path(self, binary):
            return sysctl_cmd
    class TestTime:
        def time(self):
            return int(time.time())
    test_time = TestTime()
    test_time.time = TestTime.time
    hardware = FreeBSDHardware(TestModule(), test_time)
    sysctl_cmd = hardware.module.get_bin_path('sysctl')
    uptime_facts = hardware.get_uptime_facts()
    assert 'uptime_seconds' in uptime_facts

# Generated at 2022-06-13 00:51:34.627637
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    module = AnsibleModule(argument_spec={})
    facts = FreeBSDHardware(module).populate()
    assert "processor_cores" in facts
    assert "memtotal_mb" in facts
    assert "memfree_mb" in facts
    assert "swaptotal_mb" in facts
    assert "swapfree_mb" in facts
    assert "processor_count" in facts
    assert isinstance(facts['processor'], list)
    assert "devices" in facts
    assert isinstance(facts['devices'], dict)
    assert "uptime_seconds" in facts
    assert facts['uptime_seconds'] > 0

# Generated at 2022-06-13 00:54:38.140464
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    module = MockModule()
    freebsd_hardware = FreeBSDHardware(module)
    freebsd_hardware.populate()
    assert freebsd_hardware.facts['uptime_seconds'] == 1523641654

# Generated at 2022-06-13 00:54:42.950630
# Unit test for method get_device_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_device_facts():
    module = argparse.ArgumentParser()
    setattr(module, 'get_bin_path', lambda x, opt=None: '/bin/' + x)
    setattr(module, 'get_file_content', get_file_content)
    setattr(module, 'run_command', run_command)
    fh = FreeBSDHardware(module)
    assert fh.get_device_facts() == {
        'devices': {
            'da0': ['da0s1'],
            'da1': ['da1s1']
        }
    }


# Generated at 2022-06-13 00:54:46.567931
# Unit test for method get_device_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_device_facts():
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode=True
    )
    fhw = FreeBSDHardware(module)

    # testing
    assert fhw.get_device_facts() != ''

# Generated at 2022-06-13 00:54:53.048442
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    module = MockModule()
    module.run_command = Mock(return_value=(0, '', ''))
    module.get_bin_path = Mock(return_value="/usr/sbin/dmidecode")

    # Create a FreeBSDHardware object
    f = FreeBSDHardware(module=module)

    # call the method
    f.get_dmi_facts()

    # Check that the function run_command was called
    module.run_command.assert_called_with('/usr/sbin/dmidecode -s system-version')



# Generated at 2022-06-13 00:55:03.138155
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    from ansible.module_utils.facts.collector import CallbackModule
    from ansible.module_utils.facts import timeout
    import os
    import sys
    import tempfile

    # We need to run timeout() for testing. The decorator is not applied to private methods.
    def timeout_decorator(method):
        return timeout(method)

    with tempfile.TemporaryDirectory() as temp_directory_name:
        sys.path.insert(0, temp_directory_name)
        callback_module_filename = os.path.join(temp_directory_name, 'callback_module.py')