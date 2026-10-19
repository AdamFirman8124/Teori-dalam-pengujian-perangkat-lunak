

# Generated at 2022-06-13 00:45:30.407612
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    test_module = AnsibleModule(
            argument_spec = dict(),
            supports_check_mode = True
    )
    freebsd_hardware_facts_obj = FreeBSDHardware(test_module)
    cpu_facts = freebsd_hardware_facts_obj.get_cpu_facts()
    assert set(cpu_facts.keys()) == {'processor', 'processor_cores', 'processor_count'}


# Generated at 2022-06-13 00:45:37.788056
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():

    class MockModule(object):
        def __init__(self, returncode, output, errput):
            self.returncode = returncode
            self.output = output
            self.errput = errput

        def get_bin_path(self, arg):
            return '/usr/sbin/dmidecode'

        def run_command(self, cmd, encoding=None):
            if encoding:
                return self.returncode, self.output, self.errput
            else:
                return self.returncode, self.output, self.errput


# Generated at 2022-06-13 00:45:39.085514
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    '''
    Test method populate of class FreeBSDHardware
    '''
    # TODO: implement method test_FreeBSDHardware_populate
    pass

# Generated at 2022-06-13 00:45:40.877523
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    module = MockModule()
    class_ = FreeBSDHardware(module)
    assert class_.get_uptime_facts() == {
        'uptime_seconds': int(time.time() - 1522763769),
    }


# Generated at 2022-06-13 00:45:47.092183
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():

    #  Result of a run of 'sysctl -n hw.ncpu' command
    ncpu_output = b'8'

    # Result of a run of 'dmesg' command

# Generated at 2022-06-13 00:45:51.367343
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    """UnitTest: test FreeBSDHardwareCollector constructor"""
    collector = FreeBSDHardwareCollector()
    assert isinstance(collector, FreeBSDHardwareCollector)
    assert isinstance(collector, HardwareCollector)
    assert collector._platform == 'FreeBSD'
    assert collector._fact_class == FreeBSDHardware


# Generated at 2022-06-13 00:46:01.188017
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    from ansible.module_utils.facts import time
    import time

    class MockFreeBSDHardware(FreeBSDHardware):
        def __init__(self):
            self.module = MagicMock()

    h = MockFreeBSDHardware()

    # no /var/run/dmesg.boot should return empty dict
    mock_time = MagicMock(return_value=1234.0)
    time._time = mock_time
    assert h.get_uptime_facts() == {'uptime_seconds': 1234}

    # /var/run/dmesg.boot exists with boottime = 0

# Generated at 2022-06-13 00:46:07.051246
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    hw = FreeBSDHardware(dict())
    facts = hw.populate()
    assert 'processor' in facts
    assert 'processor_count' in facts
    assert 'processor_cores' in facts
    assert facts['processor_count'] >= 1
    assert facts['processor_cores'] >= 1
    assert len(facts['processor']) == facts['processor_count']



# Generated at 2022-06-13 00:46:12.254146
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    module = DummyAnsibleModule()
    hardware = FreeBSDHardware(module=module)
    result = hardware.get_cpu_facts()
    module.exit_json.assert_called_with(changed=False, ansible_facts={ 'processor': ['Geode(TM) Integrated Processor by AMD PCS'],
                                                                       'processor_cores': '1',
                                                                       'processor_count': '1' })



# Generated at 2022-06-13 00:46:23.565708
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    import os.path
    import sys
    import tempfile
    import unittest

    class MockModule(object):
        def __init__(self, module_name):
            self.module_name = module_name
            self.sysctl_test_exists = True

        def get_bin_path(self, name):
            if name == 'sysctl':
                return '/bin/sysctl'
            else:
                return None

        def run_command(self, cmd, check_rc=True):
            class MockHwVmStats(object):
                def __init__(self, size):
                    self.size = size


# Generated at 2022-06-13 00:46:44.715037
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    fhw = FreeBSDHardware()
    fhw.module = MockModule()
    fhw.module.run_command = Mock(return_value=(0, '4', ''))
    expected_result = {'processor_cores': '4',
                       'processor': ['Intel(R) Core(TM) i3-4330T CPU @ 2.90GHz'],
                       'processor_count': '4'}
    result = fhw.get_cpu_facts()
    assert expected_result == result
    fhw.module.run_command.assert_called_once_with('/sbin/sysctl -n hw.ncpu')


# Generated at 2022-06-13 00:46:52.119023
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    """ test populate of class FreeBSDHardware

    A class is created and the populate method is executed.
    The class is compared to a dict as defined below.
    """
    class ModuleMock:
        def __init__(self):
            self.params = {}
            self.run_command_results = []

        def get_bin_path(self, arg):
            if arg == 'sysctl':
                return '/sbin/sysctl'
            if arg == 'swapinfo':
                return '/sbin/swapinfo'
            if arg == 'dmidecode':
                return '/usr/local/sbin/dmidecode'
            return None


# Generated at 2022-06-13 00:46:55.408878
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    ''' Unit test for constructor of class FreeBSDHardwareCollector '''
    fact_collector = FreeBSDHardwareCollector()
    assert fact_collector.platform == 'FreeBSD'
    assert fact_collector._fact_class == FreeBSDHardware


# Generated at 2022-06-13 00:47:05.835480
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    # define class
    hardware = FreeBSDHardware(None)
    hardware.module = AnsibleModule(argument_spec={})
    hardware.module.run_command = MagicMock(return_value=(0, 'vm.stats.vm.v_page_size: 16384\nvm.stats.vm.v_page_count: 2798360\nvm.stats.vm.v_free_count: 713894\n', ''))
    hardware.module.get_bin_path = MagicMock(return_value="/sbin/sysctl")

    # sysctl output: memory_facts
    memory_facts = hardware.get_memory_facts()
    assert isinstance(memory_facts, dict) is True
    assert isinstance(memory_facts['memtotal_mb'], int) is True
    assert memory_facts['memtotal_mb']

# Generated at 2022-06-13 00:47:13.915868
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    """
    Test the get_memory_facts method of the FreeBSDHardware class.
    """
    mock_module = type('', (), {})()  # we need a mock module
    mock_module.run_command = lambda x: ('', '', '')
    mock_module.get_bin_path = lambda x: 'sysctl'
    mock_module.fail_json = lambda x: False

    hw = FreeBSDHardware(mock_module)
    memory_facts = hw.get_memory_facts()
    assert 'memfree_mb' in memory_facts
    assert 'memtotal_mb' in memory_facts
    assert 'swapfree_mb' in memory_facts
    assert 'swaptotal_mb' in memory_facts


# Generated at 2022-06-13 00:47:16.020792
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    freebsd_hardware = FreeBSDHardware({})
    cpu_facts = freebsd_hardware.get_cpu_facts()
    assert 'processor' in cpu_facts
    assert 'processor_cores' in cpu_facts
    assert 'processor_count' in cpu_facts


# Generated at 2022-06-13 00:47:28.012541
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    # Test case: The FreeBSD platform does not implement the fact 'processor_cores'.
    #    This fact must be filled from 'Logical CPUs per core' line in dmesg.boot.
    # Output of command 'sysctl -n hw.ncpu'
    # 8
    # Output of command 'dmesg | grep 'Logical CPUs''
    # Logical CPUs per core: 2
    module = AnsibleModule(argument_spec={})

    # Arrange
    command_output = (
        "8\n",
        "",
        0,
    )


# Generated at 2022-06-13 00:47:32.505184
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec={'gather_subset': dict(type='list', default=['!all'])})
    inst = FreeBSDHardware(module)
    assert 'processor' in inst.get_cpu_facts()
    assert 'processor_cores' in inst.get_cpu_facts()
    assert 'processor_count' in inst.get_cpu_facts()


# Generated at 2022-06-13 00:47:41.512759
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    class AnsibleModuleMock:
        def get_bin_path(self, cmd, required=False):
            return '/bin/%s' % cmd

        def run_command(self, cmd, encoding=None, check_rc=True,  # noqa: A002
                        errors=None, log_messages=True, capture_error=False, binary_data=False):
            return (0, '', '')

    class FactModuleMock:
        module = AnsibleModuleMock()

    facts = {}
    dmi_facts = {}

# Generated at 2022-06-13 00:47:48.439354
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    from ansible.module_utils.facts.collector import FactsCollector
    fc = FactsCollector()
    fh = fc.collect(['hardware'], gather_subset=['!all'],
                    fact_path='ansible.module_utils.facts.hardware.freebsd')
    assert fh['ansible_facts']['hardware']['uptime_seconds'] > 0

# Generated at 2022-06-13 00:48:16.565507
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():

    # FreeBSDHardwareCollector object init
    fhwc = FreeBSDHardwareCollector()
    assert isinstance(fhwc, FreeBSDHardwareCollector)
    assert fhwc._platform == 'FreeBSD'
    assert fhwc._fact_class == FreeBSDHardware

# Generated at 2022-06-13 00:48:25.531026
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware
    import tempfile
    import textwrap


# Generated at 2022-06-13 00:48:35.717607
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware
    hardware = FreeBSDHardware()
    hardware.populate()
    if hardware.memfree_mb is not None:
        assert hardware.memfree_mb >= 0
    if hardware.memtotal_mb is not None:
        assert hardware.memtotal_mb >= 0
    if hardware.swapfree_mb is not None:
        assert hardware.swapfree_mb >= 0
    if hardware.swaptotal_mb is not None:
        assert hardware.swaptotal_mb >= 0
    for cpu in hardware.processor:
        assert isinstance(cpu, str)
    if hardware.processor_cores is not None:
        assert hardware.processor_cores >= 0
    if hardware.processor_count is not None:
        assert hardware.processor_count >= 0

# Generated at 2022-06-13 00:48:45.618803
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    import sys

    class TestModule(object):
        """ AnsibleModule mock """
        def __init__(self, run_command_args, bin_path_args):
            self.run_command_args = run_command_args
            self.bin_path_args = bin_path_args

        def get_bin_path(self, arg, opt_dirs=[]):
            """get_bin_path mock"""
            if arg in self.bin_path_args:
                return self.bin_path_args[arg]
            else:
                return None

        def run_command(self, args, check_rc=False, encoding='utf-8', errors='surrogate_then_replace'):
            """run_command mock"""
            if args[:2] == self.run_command_args[0]:
                return self

# Generated at 2022-06-13 00:48:59.251354
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    # basic test: current time and boottime are two hours apart
    dmesg_boot = """
Copyright (c) 1992-2018 The FreeBSD Project.
Copyright (c) 1979, 1980, 1983, 1986, 1988, 1989, 1991, 1992, 1993, 1994
	The Regents of the University of California. All rights reserved.
FreeBSD is a registered trademark of The FreeBSD Foundation.
FreeBSD 12.0-CURRENT r338435 GENERIC riscv
FreeBSD clang version 6.0.1 (tags/RELEASE_601/final 335540) (based on LLVM 6.0.1)
    VT(efifb): resolution 640x480
VT(efifb): depth/bpp 8/8
VT(efifb): font width/height 9/16
""".strip()
    mock_module = type('', (), {})()


# Generated at 2022-06-13 00:49:01.124359
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    module = AnsibleModule(argument_spec=dict())
    fbsd_hw = FreeBSDHardware()
    print(fbsd_hw.get_dmi_facts())


# Generated at 2022-06-13 00:49:09.480682
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    ''' unit test for get_dmi_facts of FreeBSDHardware class '''

    from ansible.module_utils.facts.hardware.bsd import FreeBSDHardware
    from ansible.module_utils.facts import timeout

    facts = FreeBSDHardware(timeout)
    facts.populate()
    content = ''

    # generate system-uuid
    import uuid
    content += 'System Information\n'
    content += '\tManufacturer: Unknown\n'
    content += '\tProduct Name: Unknown\n'
    content += '\tVersion: Unknown\n'
    content += '\tSerial Number: Unknown\n'
    content += '\tUUID: %s\n' % uuid.uuid4()
    content += '\tWake-up Type: Power Switch\n'

# Generated at 2022-06-13 00:49:18.076380
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    class Module(object):
        def __init__(self, rc, out=None, err=None, bin_path='/bin/false', check_rc=True):
            self.rc = rc
            self.out = out
            self.err = err
            self.check_rc = check_rc
            self.bin_path = bin_path

        def get_bin_path(self, executable, required=False):
            return self.bin_path

        def run_command(self, cmd, encoding=None, check_rc=None):
            if check_rc is None:
                check_rc = self.check_rc
            if check_rc:
                return (self.rc, self.out, self.err)
            else:
                return (self.rc, self.out.encode(encoding), self.err)



# Generated at 2022-06-13 00:49:24.534813
# Unit test for method get_device_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_device_facts():
    try:
        import ansible
    except ImportError:
        # Ansible not installed, exit test
        return

    if ansible.__version__ < '2.4':
        # Ansible does not contain the module_utils import_module for versions
        # below 2.4.
        return

    from ansible.module_utils.facts import timeout

    actions = {
        'get_binary_path': dict(paths='/sbin'),
        'run_command': dict(rc=0, err='', out='', stdout='', stderr=''),
        'get_file_content': dict(content='')
    }

# Generated at 2022-06-13 00:49:35.220926
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():

    from ansible.module_utils.facts import ModuleFactCollector

    dmesg_boot_file = "tests/unit/module_utils/facts/hardware/FreeBSD/dmesg_boot_file"
    fh = open(dmesg_boot_file, 'w')
    fh.write("CPU: AMD Ryzen 5 1600 Six-Core Processor (2294.10-MHz K8-class CPU)")
    fh.write("Logical CPUs per core: 1")
    fh.close()

    freebsd_hardware = FreeBSDHardware()
    freebsd_hardware.module = ModuleFactCollector()
    freebsd_hardware.module.get_bin_path = lambda x: True
    freebsd_hardware.module.run_command = lambda x: (0, 'dummy', '')
   

# Generated at 2022-06-13 00:50:33.080682
# Unit test for method populate of class FreeBSDHardware

# Generated at 2022-06-13 00:50:42.523504
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    class _module(object):
        def get_bin_path(self, _, required=False):
            return 'sysctl'

        def run_command(self, cmd, encoding=None, check_rc=True, close_fds=True):
            out = struct.pack('@L', 1503575909)
            return (0, out, '')

    class _sysctl_cmd():
        class _resource():
            def __enter__(self):
                return self
            def __exit__(self, a, b, c):
                pass

        def __init__(self, cmd):
            self.cmd = cmd
            self.returncode = 0

        def communicate(self):
            out = struct.pack('@L', 1503575909)
            return (out, '')


# Generated at 2022-06-13 00:50:50.258627
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    import mock
    import time

    module = mock.Mock()
    module.run_command = mock.Mock()
    module.run_command.return_value = (0, struct.pack('@L', int(time.time() - 10)), '')
    h = FreeBSDHardware()
    h.populate(module)
    assert 'uptime_seconds' in h.get_facts()


# Generated at 2022-06-13 00:50:54.712450
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    module = AnsibleModuleMock()
    module.run_command = mock.Mock(return_value=(0, '3329966554', None))
    freebsd_hardware = FreeBSDHardware(module)
    freebsd_hardware.module.run_command = module.run_command

    up_time_facts = freebsd_hardware.get_uptime_facts()
    assert up_time_facts['uptime_seconds'] == 3329966554

# Generated at 2022-06-13 00:50:59.961700
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    # pylint: disable=protected-access
    module = AnsibleModule(
        argument_spec=dict(gather_subset=dict(default=[], type='list'))
    )
    result = dict(
        changed=False,
        ansible_facts=dict(hardware=FreeBSDHardware(module).populate()),
    )
    module.exit_json(**result)



# Generated at 2022-06-13 00:51:09.235096
# Unit test for method get_device_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_device_facts():
    import tempfile
    dirs = {}

    # create dummy directories
    for dev in ['ada0', 'ada0s1a', 'ada0s1f', 'ada0s1g', 'ada0s1h', 'ada0s1w', 'ada1', 'ada1s1a', 'ada1s1b', 'ada2', 'ada2s2', 'ada2s2a']:
        dirs[dev] = tempfile.TemporaryDirectory()
    # run unit test
    test_object = FreeBSDHardware()
    data = test_object.get_device_facts()

# Generated at 2022-06-13 00:51:14.484833
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    test_module_dir = os.path.dirname(__file__)
    test_dmesg_boot_file = os.path.join(test_module_dir, '../../unimplemented/test/dmesg_boot')
    fh = FreeBSDHardware()
    fh.module = type('', (), {})
    fh.module.get_bin_path = lambda x: test_dmesg_boot_file
    fh.module.run_command = lambda x, check_rc=False, encoding="utf-8": (0, "4", '')
    cpu_facts = fh.get_cpu_facts()


# Generated at 2022-06-13 00:51:22.308786
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    mod_utils = __import__('ansible.module_utils', fromlist=['ansible'])
    mod = __import__('ansible.module_utils.facts.hardware.freebsd', fromlist=['ansible'])
    mod_utils.basic.AnsibleModule = mod.freebsd.AnsibleModule
    mod_utils.facts.hardware.freebsd.AnsibleModule = mod.freebsd.AnsibleModule
    module = mod_utils.facts.hardware.freebsd.AnsibleModule(
        argument_spec=dict()
    )
    sys_path = __import__('sys').path
    sys_path.append('/usr/lib/python2.7/site-packages')

# Generated at 2022-06-13 00:51:28.702486
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    module = AnsibleModule(argument_spec={}, supports_check_mode=False)
    memory_facts = FreeBSDHardware(module).get_memory_facts()

    size_regex_1 = re.compile(r'^\d+(\.\d+)?$')  # Format is xxx or xxx.yy

    # Check that there is no unexpected key in data
    keys_expected = ['memfree_mb', 'memtotal_mb', 'swapfree_mb', 'swaptotal_mb']
    keys_actual = list(memory_facts.keys())
    assert keys_expected == keys_actual

    # Check that there is no unexpected key in data
    for key_memory_fact in list(memory_facts.keys()):
        assert size_regex_1.match(memory_facts[key_memory_fact])


# Unit

# Generated at 2022-06-13 00:51:38.860471
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    from ansible.module_utils import basic
    module = basic.AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    hardware = FreeBSDHardware(module=module)
    dmi_facts_result = hardware.get_dmi_facts()
    # Test result
    assert isinstance(dmi_facts_result, dict)
    # Test key bios_date
    assert "bios_date" in dmi_facts_result
    assert isinstance(dmi_facts_result['bios_date'], str)
    # Test key bios_vendor
    assert "bios_vendor" in dmi_facts_result
    assert isinstance(dmi_facts_result['bios_vendor'], str)
    # Test key bios_version

# Generated at 2022-06-13 00:53:18.511158
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    module = AnsibleModule(argument_spec={})
    hardware = FreeBSDHardware(module)
    dmi_facts = hardware.get_dmi_facts()
    assert dmi_facts['system_vendor'] == 'NA'


# Generated at 2022-06-13 00:53:22.702226
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    '''Unit test for constructor of class FreeBSDHardwareCollector'''
    my_obj = FreeBSDHardwareCollector()
    assert my_obj
    assert my_obj._fact_class == FreeBSDHardware
    assert my_obj._platform == 'FreeBSD'

# Generated at 2022-06-13 00:53:31.964541
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    test_config = {
        'module_utils': 'ansible.module_utils.facts.hardware.freebsd',
        'module_utils_arguments': '',
        'facter_config': '/dev/null',
        'facter_facts': '{}',
        'ohai_config': '/dev/null',
        'ohai_facts': '{}',
        'sysctl_config': '/dev/null',
        'sysctl_facts': '{}'
    }
    test_module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    test_module.params = test_config

    hardware_class = FreeBSDHardware(test_module)
    hardware_facts = hardware_class.populate()

# Generated at 2022-06-13 00:53:41.383377
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    import platform
    import os
    import mock
    import sys
    import platform
    from ansible.module_utils.facts import timeout
    sys.modules['platform'] = platform
    sys.modules['timeout'] = timeout
    module = mock.MagicMock()
    module.run_command.return_value = (0, 'baseboard-asset-tag: None\n', '')
    module.get_bin_path.return_value = '/usr/sbin/dmidecode'
    setattr(module, '_dmi_vendors', ['hpe'])
    m = FreeBSDHardware(module)

# Generated at 2022-06-13 00:53:45.129438
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    '''
    Unit test for method get_cpu_facts of class FreeBSDHardware
    '''

    from ansible.module_utils.facts.facts.freebsd import FreeBSDHardware
    fhw = FreeBSDHardware(None)
    fhw.module.run_command = lambda x: (0, '/var/run/dmesg.boot', '')
    cpu_facts = fhw.get_cpu_facts()
    print(cpu_facts)


# Generated at 2022-06-13 00:53:56.962474
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    """ Unit test for get_dmi_facts method of class FreeBSDHardware """
    # mock the module class
    def module_get_bin_path(self, arg):
        if arg == 'dmidecode':
            return '/sbin/dmidecode'
        else:
            return 'Not found'

    # create an instance of class FreeBSDHardware
    fh = FreeBSDHardware()
    # mock the module class
    fh.module.get_bin_path = module_get_bin_path.__get__(fh, fh.__class__)
    #
    # run method and check result
    dmi_facts = fh.get_dmi_facts()
    if dmi_facts['bios_date'] != 'NA':
        assert type(dmi_facts['bios_date']) is str

# Generated at 2022-06-13 00:54:01.357526
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    test = {}
    test['chassis_serial'] = 'L123456789'
    test['bios_date'] = '12/31/2010'
    test['bios_vendor'] = 'test'
    test['form_factor'] = '1'
    test['bios_version'] = '123.456'
    test['board_asset_tag'] = 'board asset tag'
    test['board_name'] = 'board name'
    test['board_serial'] = 'L123456789'
    test['board_vendor'] = 'test'
    test['board_version'] = '123.456'
    test['chassis_asset_tag'] = 'chassis asset tag'
    test['chassis_vendor'] = 'test'
    test['product_name'] = 'system product name'

# Generated at 2022-06-13 00:54:05.924666
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():

    test_module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=['!all'], type='list')
        ),
        supports_check_mode=True
    )

    test_FreeBSDHardware = FreeBSDHardware(module=test_module)
    result = test_FreeBSDHardware.get_memory_facts()

    assert type(result['memfree_mb']) == int
    assert type(result['memtotal_mb']) == int
    assert type(result['swapfree_mb']) == int
    assert type(result['swaptotal_mb']) == int

# Generated at 2022-06-13 00:54:07.080405
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    hardware = FreeBSDHardware()
    # We cannot test this class method
    assert True

# Generated at 2022-06-13 00:54:12.414459
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    testmodule = AnsibleModule(
        argument_spec = dict(
        ),
        supports_check_mode=True,
    )
    fhw = FreeBSDHardware(module=testmodule)
    dmi = fhw.get_dmi_facts()
    assert 'board_vendor' in dmi
    assert 'product_name' in dmi
    assert 'product_serial' in dmi