

# Generated at 2022-06-13 01:06:39.435581
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    class DummyModule:
        def run_command(self, cmd):
            rc = 0
            out = ('Memory size: 24576 Megabytes'
                   '\nTotal swap:      536870912 kbytes used,'
                   '    536870912 kbytes available')
            err = ''
            return rc, out, err

    fake_module = DummyModule()
    system = SunOSHardware(fake_module)
    memory_facts = system.get_memory_facts()

    assert memory_facts['memtotal_mb'] == 24576
    assert memory_facts['swaptotal_mb'] == 536870912
    assert memory_facts['swapfree_mb'] == 536870912


# Generated at 2022-06-13 01:06:52.020986
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():

    class test_object(object):
        def __init__(self, rc, out, err):
            self.rc = rc
            self.out = out
            self.err = err

        def run_command(self, args):
            return self.rc, self.out, self.err

    test_data = [
        {
            'rc': 0,
            'out': 'Memory size:     262144 Megabytes',
            'err': '',
            'result': {'memtotal_mb': 262144},
        },
        {
            'rc': 0,
            'out': 'Memory size:     65536 Megabytes',
            'err': '',
            'result': {'memtotal_mb': 65536},
        },
    ]


# Generated at 2022-06-13 01:07:00.815905
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    module_mock = Mock()
    module_mock.run_command.return_value = (0, 'System Configuration: Sun Microsystems sun4u', '')

    hardware_test_object = SunOSHardware(module_mock)

    dmi_facts = hardware_test_object.get_dmi_facts()

    assert dmi_facts == {'system_vendor': 'Sun Microsystems', 'product_name': 'sun4u'}

    module_mock.run_command.return_value = (0, 'System Configuration: VMware, Inc. VMware Virtual Platform', '')

    hardware_test_object = SunOSHardware(module_mock)

    dmi_facts = hardware_test_object.get_dmi_facts()


# Generated at 2022-06-13 01:07:12.366958
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    current_time = 1548249689
    boot_time = 1548249689
    out = 'unix:0:system_misc:boot_time\t%d' % boot_time

    hardware = SunOSHardware(dict(), dict())
    hardware.module.run_command = lambda args: (0, out, None)
    hardware.module.time.time = lambda: current_time

    assert hardware.get_uptime_facts() == {'uptime_seconds': 0}

    current_time = 1548249689
    boot_time = 1548240000
    out = 'unix:0:system_misc:boot_time\t%d' % boot_time

    hardware.module.run_command = lambda args: (0, out, None)
    hardware.module.time.time = lambda: current_time

    assert hardware

# Generated at 2022-06-13 01:07:17.704983
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    inp = "Memory size:           8192 Megabytes"
    expected = {'memtotal_mb': 8192}
    module = FakeModule(inp)
    sunoshardware = SunOSHardware(module)
    out = sunoshardware.get_memory_facts()
    assert out == expected



# Generated at 2022-06-13 01:07:23.044376
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    m = SunOSHardware()
    m.module = MockModule()
    m.module.run_command.return_value = (1, 'Memory size: 16384 Megabytes', '')
    facts = m.get_memory_facts()
    assert facts['memtotal_mb'] == 16384



# Generated at 2022-06-13 01:07:32.608322
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    class args(object):
        def __init__(self):
            self.free_form = False
            self.extra_user_facts = False
            self.timeout = 5
            self.gather_subset = None
            self.gather_timeout = 10
    my_args = args()
    my_facts_obj = SunOSHardware(my_args)
    my_facts_obj.module.run_command = mock_run_command
    uptime_facts = my_facts_obj.get_uptime_facts()
    expected = {
        'uptime_seconds': 1548249689
    }
    assert uptime_facts == expected


# Generated at 2022-06-13 01:07:34.316886
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    pass


# Generated at 2022-06-13 01:07:42.759300
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )

    sunos_fact_instance = SunOSHardware(module=module)
    memory_stats = sunos_fact_instance.get_memory_facts()

    assert 'memtotal_mb' in memory_stats
    assert 'swapfree_mb' in memory_stats
    assert 'swaptotal_mb' in memory_stats
    assert 'swap_allocated_mb' in memory_stats
    assert 'swap_reserved_mb' in memory_stats


# Generated at 2022-06-13 01:07:44.416616
# Unit test for constructor of class SunOSHardwareCollector
def test_SunOSHardwareCollector():
    assert SunOSHardwareCollector()._platform == 'SunOS'
    assert SunOSHardwareCollector()._fact_class == SunOSHardware


# Generated at 2022-06-13 01:08:11.774233
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    from ansible.module_utils.facts import Collector
    from ansible.module_utils.facts import ansible_facts

    # Create a SunOSHardware instance and test get_uptime_facts using a
    # mocked run_command()
    class MockModule(object):
        def __init__(self):
            self.run_command_calls = 0
            self.run_command_args = []

        def run_command(self, *args, **kwargs):
            self.run_command_calls += 1
            self.run_command_args.append(args)

            if args[0] == 'kstat':
                boot_time = int(time.time()) - 100
                return 0, '%d' % boot_time, ''
            return 0, '', ''

    module = MockModule()

    sh = SunOS

# Generated at 2022-06-13 01:08:20.719770
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    # Test for both solaris 9 and solaris 10 for get_cpu_facts
    sunos_hw = SunOSHardware()

    # mock get_file_content
    get_file_content = sunos_hw.module.get_file_content
    get_file_content.return_value = 'SunOS release 5.9 Version Generic_122300-61 64-bit\n'

    cpu_facts = sunos_hw.get_cpu_facts()
    assert cpu_facts['processor_cores'] == 'NA'
    assert cpu_facts['processor_count'] == 8
    assert cpu_facts['processor'][0].startswith('UltraSPARC-III')
    assert cpu_facts['processor'][0].endswith('@ 1000MHz')

# Generated at 2022-06-13 01:08:25.777178
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    facts = SunOSHardware()
    facts.module.run_command = lambda cmd, opt_dirs: (0, "Sun Microsystems T1000", "")
    ret = facts.get_dmi_facts()
    assert ret['system_vendor'] == "Sun Microsystems"
    assert ret['product_name'] == "T1000"

# Generated at 2022-06-13 01:08:36.830142
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    from ansible.module_utils import basic
    from ansible.module_utils.facts import collector

    mocked_module = basic.AnsibleModule(
        argument_spec={
        },
        supports_check_mode=False
    )

    def mocked_run_command(self, cmd, check_rc=True):
        return (0, 'System Configuration: Sun Microsystems sun4v', None)

    mocked_module.run_command = mocked_run_command

    osx_facts = collector.get_platform_facts(mocked_module)

    assert osx_facts['system_vendor'] == 'Sun Microsystems'
    assert osx_facts['product_name'] == 'sun4v'

# Generated at 2022-06-13 01:08:40.554017
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    """
    Unit test for method get_device_facts of class SunOSHardware
    """
    facts = SunOSHardware().get_device_facts()
    assert ('devices' in facts) is True
    if facts['devices']:
        ("sd0" in facts['devices']) is True
    else:
        assert facts['devices'] == {}

# Generated at 2022-06-13 01:08:46.326816
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    cpu_facts = SunOSHardware().get_cpu_facts()
    assert isinstance(cpu_facts, dict)
    assert 'processor' in cpu_facts
    assert isinstance(cpu_facts['processor'], list)
    assert cpu_facts['processor_count'] is not None
    assert cpu_facts['processor_cores'] is not None


# Generated at 2022-06-13 01:08:51.671888
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    module = AnsibleModule(argument_spec={})
    hw = SunOSHardware()
    facts = hw.populate()
    assert facts['devices']['sda']['hard_errors'] == '0'
    module.exit_json(**facts)


# Generated at 2022-06-13 01:08:59.173238
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    # This test runs with facts from unit test/lib/ansible/modules/system/test_facts.py
    # If a test fails, the facts in this file may be out of date.
    facts = {
        "ansible_distribution": "SunOS",
        "ansible_distribution_release": "11.0",
        "ansible_distribution_release_build": "arclite2.0",
        "ansible_distribution_system": "SunOS",
        "ansible_machine": "i86pc"
    }
    hardware = SunOSHardware(facts)
    hfacts = hardware.populate()

    assert hfacts['processor'] == ['Intel(r) Core(tm) i7-4578U CPU @ 3.00GHz']
    assert hfacts['processor_count'] == 1

# Generated at 2022-06-13 01:09:02.251438
# Unit test for constructor of class SunOSHardwareCollector
def test_SunOSHardwareCollector():
    sc = SunOSHardwareCollector()
    assert sc.platform == 'SunOS'
    assert sc._fact_class == SunOSHardware
    assert sc.required_facts == set(['platform'])



# Generated at 2022-06-13 01:09:12.793275
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    data = '''module: cpu_info
instance: 0
class: misc
clock_MHz       400
chip_id         0
implementation  sparc
state           on-line
cpu_type        sparcv9
brand           sun4v
'''
    module = type('module', (), dict(run_command=lambda x, env=None, data=data: (0, data, None)))
    facts_data = SunOSHardware(module).get_cpu_facts()
    assert facts_data['processor'][0] == 'sparcv9 @ 400MHz'

    data = '''module: cpu_info
instance: 0
class: misc
brand           sun4v
'''
    module = type('module', (), dict(run_command=lambda x, env=None, data=data: (0, data, None)))
    facts_data

# Generated at 2022-06-13 01:09:47.701096
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    '''
    Test for method get_device_facts in class SunOSHardware.
    '''
    test_module = SunOSHardware()

    # Test for results of get_device_facts method
    device_facts = test_module.get_device_facts()

    assert 'devices' in device_facts

# Generated at 2022-06-13 01:09:58.554386
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    import sys
    import json
    import platform
    from ansible.module_utils.facts import timeout

    module = sys.modules['ansible.module_utils.facts.hardware.sunos']
    timeout.TimeoutError = Exception


# Generated at 2022-06-13 01:10:09.943377
# Unit test for method get_cpu_facts of class SunOSHardware

# Generated at 2022-06-13 01:10:16.023381
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    tmp_fct = SunOSHardware()
    # Mock the output of prtdiag
    prtdiag_out = 'System Configuration: VMware, Inc. VMware Virtual Platform\n'
    tmp_fct.module.run_command = lambda x: (0, prtdiag_out, '')
    dmi_facts = tmp_fct.get_dmi_facts()

    assert dmi_facts['system_vendor'] == 'VMware, Inc.'
    assert dmi_facts['product_name'] == 'VMware Virtual Platform'
    assert len(dmi_facts) == 2



# Generated at 2022-06-13 01:10:22.467608
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    """ Test get_dmi_facts method of class SunOSHardware """
    solaris_hardware = SunOSHardware(dict(module=dict()))

    # Valid Solaris system_conf output
    solaris_hardware.module.run_command = lambda x: (0, 'System Configuration: Oracle Corporation sun4v', '')

    dmi_facts = solaris_hardware.get_dmi_facts()

    assert dmi_facts['system_vendor'] == 'Oracle Corporation'
    assert dmi_facts['product_name'] == 'sun4v'

    # Invalid Solaris system_conf output
    solaris_hardware.module.run_command = lambda x: (0, 'System Configuration: Oracle Corporation', '')

    dmi_facts = solaris_hardware.get_dmi_facts()

    assert dmi_facts

# Generated at 2022-06-13 01:10:33.188633
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    test_model = 'VirtualBox'
    test_vendor = 'Oracle Corporation'

    test_cpu_facts = {'processor': ['Intel(r) Core(tm) i7-5557U CPU @ 3.10GHz']}
    test_mem_facts = {'memtotal_mb': 8192,
                      'swapfree_mb': 8192,
                      'swaptotal_mb': 8192,
                      'swap_allocated_mb': 0,
                      'swap_reserved_mb': 0}


# Generated at 2022-06-13 01:10:42.962805
# Unit test for method get_dmi_facts of class SunOSHardware

# Generated at 2022-06-13 01:10:53.030466
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    # Create a SunOSHardware instance
    sh = SunOSHardware()
    # Create a test file
    test_kstat_file = open("/tmp/test_kstat_file.txt","w")
    test_kstat_file.write("module: pri \n")
    test_kstat_file.write("clock_MHz 9.999999e+03 \n")
    test_kstat_file.write("chip_id 0 \n")
    test_kstat_file.write("brand sun4u \n")
    test_kstat_file.write("implementation SPARC-T4 \n")
    test_kstat_file.write("module: pri \n")
    test_kstat_file.write("clock_MHz 9.999999e+03 \n")

# Generated at 2022-06-13 01:10:58.728351
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    module = AnsibleModule(
        argument_spec = dict(),
    )

    result = SunOSHardware.get_dmi_facts(
            {
                'module': module,
            }
        )
    assert result['system_vendor'] == 'Sun Microsystems'
    assert result['product_name'] == 'Sun Fire V490'


# Generated at 2022-06-13 01:11:04.318743
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    module = AnsibleModuleMock()
    sun_os_hardware = SunOSHardware(module)
    collected_facts = {}
    collected_facts['ansible_machine'] = 'i86pc'

    sun_os_hardware.populate(collected_facts)

    assert sun_os_hardware.facts['processor_count'] == 1
    assert sun_os_hardware.facts['processor_cores'] == 1
    assert sun_os_hardware.facts['processor'] != []

# Generated at 2022-06-13 01:12:18.207985
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    module = AnsibleModule(argument_spec=dict())

    # Create a new instance of class SunOSHardware
    sunos_hw = SunOSHardware(module)

    # Create a mockout of prtdiag
    # Use 2345 as the System Configuration: Oracle Corporation
    # because using Oracle Corporation as the test will pass on real hardware
    prt_diag = """\
System Configuration: 2345 X86
System Configuration: 2345 sun4v
"""
    (fd, fname) = tempfile.mkstemp()
    f = os.fdopen(fd, 'w')
    f.write(prt_diag)
    f.close()

    # Mock the module.run_command on class SunOSHardware
    # so that instead of running prtdiag, we use the mockout
    # of prtdiag.
   

# Generated at 2022-06-13 01:12:27.838172
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    mock_module = MagicMock()
    mock_module.run_command.return_value = (0, '', '')
    sunoshardware = SunOSHardware(mock_module)

    expected = {'processor_cores': 'NA', 'processor_count': 1, 'processor': [''], 'memtotal_mb': 0, 'swapfree_mb': 0, 'swaptotal_mb': 0, 'swap_allocated_mb': 0, 'swap_reserved_mb': 0}
    assert sunoshardware.populate() == expected, 'populate method of class SunOSHardware did not return expected value'


# Generated at 2022-06-13 01:12:36.381266
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    module = AnsibleModuleStub()
    test_data = """
Memory size: 4096 Megabytes
    """
    module.run_command.side_effect = [
        (0, test_data, ''),
        (0, "8192K        total        \n 8192K        used         \n    0K        free         \n", '')
    ]
    facts = SunOSHardware.get_memory_facts(None, module)
    module.run_command.assert_has_calls([call(['/usr/sbin/prtconf']),
                                         call(['/usr/sbin/swap', '-s'])])
    assert facts['memtotal_mb'] == 4096
    assert facts['swapfree_mb'] == 8
    assert facts['swaptotal_mb'] == 8

# Generated at 2022-06-13 01:12:48.504486
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    test_hardware = SunOSHardware()

    # create a class with run_command method
    class RunModule:
        def __init__(self):
            test_hardware.module = self
            self.output = []


# Generated at 2022-06-13 01:12:57.800611
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
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

    class test_module_class:
        def __init__(self, data):
            self.run_command = data


# Generated at 2022-06-13 01:13:04.069367
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    """
    The purpose of this test is to ensure that the cpu facts are collected
    correctly for SunOS.
    """
    hardware = SunOSHardware({})
    hardware.module.run_command = lambda x: ('', '', '')
    hardware.module.run_command_environ_update = {}  # noqa: F841
    hardware.populate()
    assert hardware.cpu()['processor_cores'] == 'NA'
    assert hardware.cpu()['processor_count'] == 0
    assert hardware.cpu()['processor'] == []



# Generated at 2022-06-13 01:13:14.835537
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():

    class ModuleStub():

        class RunCommandResult():
            def __init__(self, out, rc, err):
                self.out = out
                self.rc = rc
                self.err = err

        def run_command(self, command):
            if command == "/usr/bin/uname -i":
                return self.RunCommandResult("i86pc", 0, "")
            else:
                return self.RunCommandResult("", 1, "")

        def get_bin_path(self, program, opt_dirs=[]):
            return ""

    sunOSHardware = SunOSHardware(ModuleStub())
    dmi_facts = sunOSHardware.get_dmi_facts()
    assert('system_vendor' not in dmi_facts)
    assert('product_name' not in dmi_facts)

   

# Generated at 2022-06-13 01:13:22.610727
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    def mock_run_cmd(cmd):
        if cmd == '/usr/bin/kstat cpu_info':
            output = """module:  cpu_info
instance: 0
class:    misc
chip_id:  0
clock_MHz:   2600.000000
brand:    Genuine Intel(R) CPU           P4-3.00GHz
implementation: x86
revision: 4 
module:  cpu_info
instance: 0
class:    misc
chip_id:  1
clock_MHz:   2600.000000
brand:    Genuine Intel(R) CPU           P4-3.00GHz
implementation: x86
revision: 4 """
            return 0, output, ''
        else:
            raise Exception("not expected cmd: %s" % cmd)

    hw = SunOSHardware()

# Generated at 2022-06-13 01:13:23.699627
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    # FIXME
    pass

# Generated at 2022-06-13 01:13:30.414927
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():

    class FakeModule(object):
        def run_command(self, *args, **kwargs):
            return 0, 'unix:0:system_misc:boot_time 1548249689\n', ''

    test_obj = SunOSHardware(FakeModule())
    uptime_facts = test_obj.get_uptime_facts()

    assert uptime_facts['uptime_seconds'] == int(time.time() - 1548249689)