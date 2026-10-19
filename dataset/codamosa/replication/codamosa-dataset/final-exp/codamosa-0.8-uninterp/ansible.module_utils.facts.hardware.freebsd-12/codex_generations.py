

# Generated at 2022-06-13 00:45:27.664724
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    freebsd_hardware = FreeBSDHardwareCollector()
    assert freebsd_hardware.platform == 'FreeBSD'

# Generated at 2022-06-13 00:45:35.817875
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    module = AnsibleModule(argument_spec={})

    fb_hw = FreeBSDHardware(module)

    # Test:
    assert get_mount_size('/') == {'size_total': 164976604672, 'size_available': 77688864768}
    assert 'devices' in fb_hw.populate()
    assert 'swaptotal_mb' in fb_hw.populate()
    assert 'swapfree_mb' in fb_hw.populate()
    assert 'memfree_mb' in fb_hw.populate()
    assert 'memtotal_mb' in fb_hw.populate()
    assert 'uptime_seconds' in fb_hw.populate()
    assert 'processor_count' in fb_hw.populate()
    assert 'mounts' in fb

# Generated at 2022-06-13 00:45:46.620630
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    mock_module = MagicMock(name='ansible_module')
    mock_module.run_command.return_value = (0, 'hw.ncpu: 2', '')

    freebsd_hw = FreeBSDHardware(mock_module)
    cpu_facts = freebsd_hw.get_cpu_facts()
    assert cpu_facts == {'processor': ['Intel(R) Core(TM) i7 CPU 950  @ 3.07GHz', 'Intel(R) Core(TM) i7 CPU 950  @ 3.07GHz'],
                         'processor_cores': '2',
                         'processor_count': '2'}


# Generated at 2022-06-13 00:45:57.207623
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    class ModuleMock(object):
        def __init__(self):
            self.params = {'require_facts': True}

        def get_bin_path(self, executable, required=True):
            return "/usr/bin/%s" % executable

        def run_command(self, cmd, check_rc=True):
            return (0, out, err)

    class HardwareMock(FreeBSDHardware):
        def __init__(self):
            self.module = ModuleMock()
            self.populate()


# Generated at 2022-06-13 00:46:06.136294
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware
    hardware = FreeBSDHardware()
    out = hardware.get_cpu_facts()
    result = {'processor': ['Intel(R) Core(TM) i5-2500K CPU @ 3.30GHz', 'Intel(R) Core(TM) i5-2500K CPU @ 3.30GHz', 'Intel(R) Core(TM) i5-2500K CPU @ 3.30GHz', 'Intel(R) Core(TM) i5-2500K CPU @ 3.30GHz'], 'processor_cores': '4', 'processor_count': '4'}
    assert out == result

# Generated at 2022-06-13 00:46:14.407847
# Unit test for method get_dmi_facts of class FreeBSDHardware

# Generated at 2022-06-13 00:46:16.065661
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    assert isinstance(FreeBSDHardwareCollector(), (HardwareCollector))

# Generated at 2022-06-13 00:46:22.132622
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    fake_module = FakeModule()
    fact_collection = FreeBSDHardware(fake_module)
    uptime_facts = fact_collection.get_uptime_facts()
    # get_uptime_facts should be implemented, as FreeBSD is a "new" platform
    # We verify that uptime_facts is a dictionary and contains 'uptime_seconds'
    assert isinstance(uptime_facts, dict)
    assert 'uptime_seconds' in uptime_facts

# Generated at 2022-06-13 00:46:25.848929
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    class Module:
        def get_bin_path(self, object):
            return object

        def run_command(self, command, encoding=None):
            if b'kern.boottime' in command:
                return 0, b'{ sec = 1570043844, usec = 952499 }', b''
            else:
                raise Exception('Unknown command')

    module = Module()

    fact_class = FreeBSDHardware()
    uptime_facts = fact_class.get_uptime_facts(module)

    assert uptime_facts == {
        'uptime_seconds': 1570043844,
    }

# Generated at 2022-06-13 00:46:26.705411
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    assert FreeBSDHardwareCollector.platform == 'FreeBSD'

# Generated at 2022-06-13 00:46:49.123477
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    bin_path = '/sbin/dmidecode'

# Generated at 2022-06-13 00:46:50.415034
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    # Make sure the class can be instantiated
    module = FreeBSDHardwareCollector()
    assert module

# Generated at 2022-06-13 00:46:51.780874
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    import doctest
    doctest.testmod(FreeBSDHardware)

# Generated at 2022-06-13 00:46:54.692954
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    fhc = FreeBSDHardwareCollector()
    assert fhc.platform == 'FreeBSD'
    assert fhc.fact_class == FreeBSDHardware

# Unit Test for FreeBSDHardwareCollector method populate()

# Generated at 2022-06-13 00:46:59.406955
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    '''Unit test for FreeBSDHardwareCollector'''

    module = AnsibleModule(argument_spec={})
    result = FreeBSDHardwareCollector.get_instance(module)
    assert result is not None
    assert isinstance(result["FreeBSDHardwareCollector"], FreeBSDHardwareCollector)
    assert isinstance(result["FreeBSDHardwareCollector"].collect(), dict)


# Generated at 2022-06-13 00:47:06.136254
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    # Arrange
    module = AnsibleModuleMock()
    hw = FreeBSDHardware(module)

    # Act
    hw.populate()

    # Assert
    module.run_command.assert_called_with('sysctl vm.stats', check_rc=False)
    assert module.get_bin_path.call_args_list == [
        call('sysctl'),
        call('swapinfo'),
        call('dmidecode')
    ]

# Generated at 2022-06-13 00:47:10.933068
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    try:
        import platform
        platform.machine = lambda: 'i386'
        fhc = FreeBSDHardwareCollector(None)
        assert fhc.hardware._platform == 'FreeBSD'
        assert fhc.hardware.DMESG_BOOT == '/var/run/dmesg.boot'
    finally:
        try:
            del platform.machine
        except AttributeError:
            pass

# Generated at 2022-06-13 00:47:18.632498
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():

    class AnsibleModuleMock(object):
        class RunCommandResult(object):
            def __init__(self, rc, out, err):
                self.rc = rc
                self.out = out
                self.err = err

        def __init__(self, params={}):
            self.params = params

        def run_command(self, cmd, encoding=None):
            # TODO: generate test output for dmidecode -s <tag> commands
            print("command:", cmd)
            rc = 0
            out = ""
            err = ""
            return AnsibleModuleMock.RunCommandResult(rc, out, err)

        def get_bin_path(self, name, opt_dirs=[]):
            if name == "dmidecode":
                return "/usr/bin/dmidecode"

# Generated at 2022-06-13 00:47:28.696380
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    '''FreeBSDHardware: test get_cpu_facts method'''
    module = AnsibleModuleMock()
    hardware = FreeBSDHardware(module)

    hardware.module.params = {}
    cpu_facts = hardware.get_cpu_facts()
    assert cpu_facts['processor_count'] > 0
    assert len(cpu_facts['processor']) > 0

    # Assert that a reasonable number of processor_cores are returned.  Note
    # that a reasonable number is any integer, as there is no reasonable number
    # of processor cores.  It's not reasonable to assume that you will only
    # ever have 1, 2, 4, or 8.
    assert int(cpu_facts['processor_cores']) > 0



# Generated at 2022-06-13 00:47:37.963137
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():

    module = AnsibleModule(
        argument_spec=dict(
            timeout=dict(default=10, type='int'),
        )
    )

    dummy_dmidecode = DummyBinary(module, 'dmidecode')
    dummy_dmidecode.add_cmd(['-s', 'bios-release-date'],
                            'Wed Sep 23 10:35:56 2015', 0)
    dummy_dmidecode.add_cmd(['-s', 'bios-vendor'],
                            'None', 0)
    dummy_dmidecode.add_cmd(['-s', 'bios-version'],
                            'None', 0)
    dummy_dmidecode.add_cmd(['-s', 'baseboard-asset-tag'],
                            'None', 0)
    dummy_dmide

# Generated at 2022-06-13 00:47:55.399600
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    # TODO: implement
    assert True

# Generated at 2022-06-13 00:48:03.501983
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    class MockModule(object):
        def __init__(self):
            self.fail_json = lambda *a, **kw: False
            self.params = {}
            self.get_bin_path = lambda *a, **kw: False
            self.run_command = lambda *a, **kw: False

    class MockModule3_10(object):
        def __init__(self):
            self.fail_json = lambda *a, **kw: False
            self.params = {}
            self.get_bin_path = lambda *a, **kw: False
            self.run_command = lambda *a, **kw: (0, '2', '')

    class MockModule4(object):
        def __init__(self):
            self.fail_json = lambda *a, **kw: False
            self.params = {}


# Generated at 2022-06-13 00:48:09.918270
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    from ansible.module_utils.facts.freebsd import FreeBSDHardware
    hardware = FreeBSDHardware()
    sysctl = hardware.module.get_bin_path('sysctl')
    if sysctl:
        rc, out, err = hardware.module.run_command("%s vm.stats" % sysctl, check_rc=False)
        for line in out.splitlines():
            data = line.split()
            if 'vm.stats.vm.v_page_size' in line:
                pagesize = int(data[1])
            if 'vm.stats.vm.v_page_count' in line:
                pagecount = int(data[1])
            if 'vm.stats.vm.v_free_count' in line:
                freecount = int(data[1])

# Generated at 2022-06-13 00:48:20.032253
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    '''Unit test for method get_uptime_facts of class FreeBSDHardware'''
    import time
    import pytest

    module = AnsibleModuleMock()

    hardware = FreeBSDHardware(module)

    # Test that an invalid output returns empty dictionary
    module.run_command_mock.side_effect = [
        # The first call is to sysctl to fetch the boottime.
        (1, b'', b''),
    ]
    result = hardware.get_uptime_facts()
    assert result == {}

    # Test that a short output returns empty dictionary
    module.run_command_mock.side_effect = [
        # The first call is to sysctl to fetch the boottime.
        (0, b'', b''),
    ]
    result = hardware.get_uptime_facts()
    assert result == {}

# Generated at 2022-06-13 00:48:25.109630
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )

    h = FreeBSDHardware(module=module)
    m = h.get_memory_facts()
    assert m['memtotal_mb'] >= 0
    assert m['memfree_mb'] >= 0
    assert m['swaptotal_mb'] >= 0
    assert m['swapfree_mb'] >= 0


# Generated at 2022-06-13 00:48:27.987540
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    fhw = FreeBSDHardwareCollector()
    assert fhw.platform == 'FreeBSD'
    assert fhw._fact_class is FreeBSDHardware

# Generated at 2022-06-13 00:48:31.507443
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    module = AnsibleModule({})
    dmi_facts = dmi_facts = FreeBSDHardware.get_dmi_facts(module)
    assert dmi_facts is not None



# Generated at 2022-06-13 00:48:35.689489
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    module = AnsibleModule(argument_spec={})
    hardware = FreeBSDHardware(module)
    hardware.populate()
    assert hardware.memtotal_mb > 0
    assert hardware.memfree_mb > 0
    assert hardware.swaptotal_mb > 0
    assert hardware.swapfree_mb > 0



# Generated at 2022-06-13 00:48:37.714365
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    hw = FreeBSDHardwareCollector()
    assert hw



# Generated at 2022-06-13 00:48:46.478812
# Unit test for method get_cpu_facts of class FreeBSDHardware

# Generated at 2022-06-13 00:49:33.760411
# Unit test for method get_device_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_device_facts():
    """
    Unit test for method get_device_facts of class FreeBSDHardware
    """

    import tempfile
    import shutil

    temp_dir = tempfile.mkdtemp(prefix='ansible_test_FreeBSDHardware_get_device_facts')
    sys_dir = os.path.join(temp_dir, 'dev')
    os.mkdir(sys_dir)

    # Create a fake device
    device_name = 'ada0'
    device_file = os.path.join(sys_dir, device_name)
    with open(device_file, 'w') as f:
        f.write('unused')

    # Create a fake slice(s)
    slice_name = 'ada0s1a'
    slice_file = os.path.join(sys_dir, slice_name)

# Generated at 2022-06-13 00:49:38.532500
# Unit test for method get_device_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_device_facts():
    module = type('MockModule', (object,), {'get_bin_path': lambda self, x: '/dev/null', 'run_commnad': lambda self, x: None})()
    hardware = FreeBSDHardware(module)

    devices1 = hardware.get_device_facts()
    assert isinstance(devices1, dict)
    assert 'devices' in devices1

    # give the test a reasonable chance of succeeding
    assert devices1['devices']

    devices2 = hardware.get_device_facts()
    assert isinstance(devices2, dict)
    assert 'devices' in devices2

    # devices lists should be equal
    assert devices1 == devices2

# Generated at 2022-06-13 00:49:46.299609
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    module = AnsibleModule(argument_spec=dict())


# Generated at 2022-06-13 00:49:48.089395
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    f = FreeBSDHardwareCollector()
    assert f.platform == 'FreeBSD'


# Generated at 2022-06-13 00:49:57.968789
# Unit test for method get_device_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_device_facts():
    # Create a mock module class
    fake_module = type('AnsibleModule', (object,), {
        'fail_json': lambda self, msg: msg,
        'params': {},
        '_debug': lambda msg: msg,
        'get_bin_path': lambda self, s: s,
    })
    # Create an object of class FreeBSDHardware
    frbshw = FreeBSDHardware()
    # Create a mock object of class AnsibleModule
    frbshw.module = fake_module()
    # Create a fake directory
    os.mkdir('/dev')
    # Create a list of fake files
    fake_files = ['ada0', 'ada1', 'ada1s1', 'ada1s2', 'ada1s3']
    # Create the fake files

# Generated at 2022-06-13 00:50:03.266843
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    hw = FreeBSDHardware()

    # Test dmidecode output parsing
    dmi_bin = hw.module.get_bin_path('dmidecode')
    if dmi_bin is not None:
        # Set a dummy dmidecode command
        setattr(hw.module, 'dmidecode', 'echo')
        hw.get_dmi_facts()



# Generated at 2022-06-13 00:50:07.587476
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    module = AnsibleModule(argument_spec={})
    hardware = FreeBSDHardware(module)

    if hardware.get_uptime_facts()['uptime_seconds'] < 5:
        raise Exception('unexpected uptime: %s' % hardware.get_uptime_facts()['uptime_seconds'])


# Generated at 2022-06-13 00:50:14.608412
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    def sysctl_mock(self, module, *args, **kwargs):
        return 0, '2147483648', ''

    import mock

    # Create an instance of the FreeBSDHardware class
    hardware_ins = FreeBSDHardware()
    # Mock the sysctl syscall
    hardware_ins.module.run_command = mock.Mock(side_effect=sysctl_mock)
    # Call get_uptime_facts method
    uptime_facts = hardware_ins.get_uptime_facts()

    assert uptime_facts['uptime_seconds'] == 2147483648

# Generated at 2022-06-13 00:50:19.562215
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    # Get the boottime which is a string like this one:
    #
    # '{ sec = 1513314923, usec = 713849 } Thu Dec 28 11:12:03 2017\n'
    #
    # and convert it to a raw bytes string like this one:
    #
    # b'\x00\x00\x3a\xe8\x49\x2a\xec\x6e\x6b\x00\x00\x00\x00\x00\x00\x00\x12\x1c\x8b\x9b\x83\x2d\xc8\xdc\x00\x00\x00\x00\x00'
    #
    # in order to be able to call struct.unpack() on it.
    uptime_info = get

# Generated at 2022-06-13 00:50:23.860440
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    module = AnsibleModule(argument_spec={})
    hardware_facts = FreeBSDHardware(module).get_memory_facts()
    assert hardware_facts['memtotal_mb'] > 0
    assert hardware_facts['memfree_mb'] >= 0
    assert hardware_facts['swaptotal_mb'] > 0
    assert hardware_facts['swapfree_mb'] >= 0



# Generated at 2022-06-13 00:51:52.801761
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    '''Validate FreeBSDHardware.get_uptime_facts'''

    from ansible.module_utils.facts.utils import py23_compat
    from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware

    for test in [('kern.boottime: { sec = 1602274162, usec = 866194 }', 1602274162866194),
                 ('kern.boottime: { sec = 1611179346, usec = 805100 }', 16111793460805100)]:
        hardware = FreeBSDHardware(None)

        time_function = lambda: test[1]
        orig_time = time.time
        time.time = time_function
        retval = hardware.get_uptime_facts()
        time.time = orig_time

        sec, usec = py23_

# Generated at 2022-06-13 00:51:56.988471
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    module = AnsibleModule(argument_spec={})
    hardware_collector = FreeBSDHardwareCollector(module=module)
    hardware = hardware_collector.collect()
    assert hardware.platform == 'FreeBSD'

# Generated at 2022-06-13 00:52:05.898001
# Unit test for method get_dmi_facts of class FreeBSDHardware

# Generated at 2022-06-13 00:52:15.791972
# Unit test for method get_device_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_device_facts():
    import sys
    import json

    module = sys.modules[__name__]

    setattr(module, 'module', AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    ))

    test_hw = FreeBSDHardware()

    # Create test directory
    os.makedirs('/dev')

    # Create test devices
    fd, test_dev = tempfile.mkstemp(dir='/dev', prefix='ada')
    os.close(fd)

    fd, test_slice = tempfile.mkstemp(dir='/dev', prefix='ada')
    os.close(fd)


# Generated at 2022-06-13 00:52:22.276696
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    # create a class instance
    test = FreeBSDHardware()
    # create data for test
    test.module = -1
    test.module.get_bin_path = lambda: "/usr/bin/env"
    # call method to test
    result = test.get_cpu_facts()
    # check the result
    assert result == {'processor': ['Intel(R) Core(TM) i5-2410M CPU @ 2.30GHz'],
  'processor_cores': '2', 'processor_count': '2'}


# Generated at 2022-06-13 00:52:30.493773
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    class TestModule:
        def __init__(self, params):
            self.params = params

        def get_bin_path(self, cmd, required=False):
            return '/sbin/sysctl'

        def run_command(self, cmd, encoding=None):
            return (0, os.urandom(struct.calcsize('@L')), "")

    spec = {
        'time_taken': 0.01,
    }

    module = TestModule(spec)
    obj_freebsd = FreeBSDHardware(module=module)
    obj_freebsd.get_uptime_facts()

# For testing, update the module path so we can load the mimimal version
import sys


# Generated at 2022-06-13 00:52:35.383790
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    # Test without dmidecode command
    test_obj = FreeBSDHardware()
    test_obj.get_bin_path = lambda x: None
    assert 'NA' in test_obj.get_dmi_facts().values()

    # Test with dmidecode command
    test_obj.module.run_command = lambda x: (0, 'some value', '')
    assert 'NA' not in test_obj.get_dmi_facts().values()

# Generated at 2022-06-13 00:52:44.169428
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    import time
    import datetime
    import pytz
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware
    from ansible.module_utils.facts.timeout import TimeoutError, timeout

    class TestModule:
        def __init__(self, *args):
            pass

        def get_bin_path(self, *args):
            return None

        def run_command(self, *args):
            return 0, to_bytes(args[0]), None

    tm = TestModule()
    fh = FreeBSDHardware(module=tm)
    start_time = int(time.time())

    # Call get_uptime_facts() without specifying kern.boottime
    (rc, out, err) = tm.run_command

# Generated at 2022-06-13 00:52:46.699699
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    import ansible.module_utils.facts.hardware.freebsd
    h = ansible.module_utils.facts.hardware.freebsd.FreeBSDHardware()
    h.populate()


# Generated at 2022-06-13 00:52:51.813175
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    # Create a test module
    # monkey patching for testing
    module = type('FauxAnsibleModule', (object,), dict(
        check_mode=False,
        exit_json=print,
        fail_json=print,
        get_bin_path=lambda k: '/sbin/sysctl' if k == 'sysctl' else None,
    ))()

    test = FreeBSDHardware(module=module)
    test.get_memory_facts()