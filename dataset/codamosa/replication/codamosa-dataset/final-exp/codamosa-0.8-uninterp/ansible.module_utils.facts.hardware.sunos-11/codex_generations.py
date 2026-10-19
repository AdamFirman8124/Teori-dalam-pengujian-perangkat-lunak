

# Generated at 2022-06-13 01:06:30.089359
# Unit test for constructor of class SunOSHardwareCollector
def test_SunOSHardwareCollector():
    """
    Test for platform name and required facts
    """
    sunos_collector = SunOSHardwareCollector()

    assert sunos_collector.platform == 'SunOS'
    assert sunos_collector.required_facts == {'platform'}

# Generated at 2022-06-13 01:06:34.956363
# Unit test for constructor of class SunOSHardwareCollector
def test_SunOSHardwareCollector():
    platform = 'SunOS'
    required = set(['platform'])
    hardware_collector = SunOSHardwareCollector(platform,required)
    assert hardware_collector.platform is platform
    assert hardware_collector.required_facts is required
    assert isinstance(hardware_collector.collect(),dict)

# Generated at 2022-06-13 01:06:39.195428
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    cpu_facts = {}
    cpu_facts['processor'] = []
    cpu_facts['processor'].append('SUNW,SPARC-Enterprise')

    assert cpu_facts == SunOSHardware().get_cpu_facts()

# Generated at 2022-06-13 01:06:51.756982
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    module = AnsibleModule(
        argument_spec={}
    )

    # Create an instance
    sunosHardware = SunOSHardware(module)
    mem_facts=sunosHardware.get_memory_facts()

    assert "memtotal_mb" in mem_facts
    assert "swapfree_mb" in mem_facts
    assert "swaptotal_mb" in mem_facts
    assert "swap_allocated_mb" in mem_facts
    assert "swap_reserved_mb" in mem_facts
    assert mem_facts["memtotal_mb"] > 0
    assert mem_facts["swapfree_mb"] > 0
    assert mem_facts["swaptotal_mb"] > 0
    assert mem_facts["swap_allocated_mb"] >= 0

# Generated at 2022-06-13 01:07:00.939397
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    from ansible.module_utils.facts.collector import collector_mock

    mock_module = collector_mock.CollectorMock()
    mock_module.run_command.return_value = (0,
                                            'Memory size: 8192 Megabytes\n',
                                            '')
    facts_instance = SunOSHardware()
    facts_instance.module = mock_module
    discovered_facts = facts_instance.get_memory_facts()

    # test if memory_facts is a dict
    assert isinstance(discovered_facts, dict)

    # test if memory_facts has right number of entries
    assert len(discovered_facts) == 1

    # test if dict has right content
    assert discovered_facts == {'memtotal_mb': 8192}



# Generated at 2022-06-13 01:07:03.802117
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    module = AnsibleModuleMock({})
    hardware = SunOSHardware(module)
    facts = hardware.populate()
    assert facts['processor']
    assert facts['swapfree_mb']
    assert facts['swaptotal_mb']
    assert facts['memtotal_mb']


# Generated at 2022-06-13 01:07:15.238326
# Unit test for method get_device_facts of class SunOSHardware

# Generated at 2022-06-13 01:07:27.391680
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    """
    Test the populate method of SunOSHardware.
    """
    test_platform = 'SunOS'
    module = AnsibleModuleMock(platform=test_platform)
    module.run_command = run_command
    module.get_bin_path = get_bin_path
    module.get_file_content = get_file_content

    # Test return of populate method
    facts_obj = SunOSHardware(module)
    facts = facts_obj.populate()

    # Test cpu facts
    assert facts['processor_cores'] == 1
    assert facts['processor_count'] == 4

# Generated at 2022-06-13 01:07:35.295446
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    class mock:
        def __init__(self):
            self.params = {}
        def get_bin_path(self, path, opt_dirs=None):
            return path
    class fake:
        def __init__(self):
            self.module = mock()

    fact = SunOSHardware()
    fact.module = fake()
    fact.module.run_command = lambda command: (0, 'unix:0:system_misc:boot_time    1548249689', '')
    uptime_facts = fact.get_uptime_facts()
    assert uptime_facts['uptime_seconds'] == int(time.time() - 1548249689)

# Generated at 2022-06-13 01:07:41.624192
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    """
    Unit test of method populate of class SunOSHardware.

    :return:
    """
    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=False
    )

    hardware_facts_instance = SunOSHardware(module)
    facts = hardware_facts_instance.populate()
    for key, _ in facts.items():
        assert_equals(facts[key], 'NA')

# Generated at 2022-06-13 01:07:58.384180
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    t = SunOSHardware()
    assert 'uptime_seconds' in t.get_uptime_facts()

# Generated at 2022-06-13 01:08:06.605091
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    '''Unit test for method get_device_facts of class SunOSHardware'''
    import tempfile
    filename = tempfile.mktemp()

# Generated at 2022-06-13 01:08:10.420120
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    m = SunOSHardware({})
    result = m.populate()

    assert result['processor'] == ['SPARC T4 (chipid 0, clock 1800 MHz)']
    assert result['processor_count'] == 1
    assert result['processor_cores'] == 8



# Generated at 2022-06-13 01:08:18.397780
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    module = FakeAnsibleModule()
    module.run_command = Mock(return_value=(0, "", ""))
    module.run_command_environ_update = {"LANG":"en", "LC_ALL":"en", "LC_NUMERIC":"en"}
    hardware = SunOSHardware(module)

    # Test without the locale set
    module.run_command_environ_update = {}
    hardware.populate()

    # Verify exception is raised when we fail to parse the output
    module.run_command = Mock(return_value=(0,
                                            "Memory size: 16384 Megabytes",
                                            ""))
    hardware.populate()

    # Verify exception is raised when we don't get a match

# Generated at 2022-06-13 01:08:25.201247
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    """
     Test case to test the output of method
     populate of class SunOSHardware.
    """
    module = AnsibleModuleMock()
    module.run_command.return_value = ("", "", "")
    sunos_obj = SunOSHardware(module)
    facts_dictionary = sunos_obj.populate()
    assert facts_dictionary['processor'][0] == "SPARC32+ @ 400MHz"



# Generated at 2022-06-13 01:08:29.839989
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    module = FakeAnsibleModule()
    module._ansible_facts = {
            'ansible_machine': 'sparc',
            'ansible_processor': ['sparcv9', 'sparcv9', 'sparcv9']
    }
    sunos = SunOSHardware(module)
    cpu_facts = sunos.get_cpu_facts()

    assert 3 == cpu_facts['processor_count']
    assert 3 == cpu_facts['processor_cores']
    assert cpu_facts['processor'] == ['SUNW,UltraSPARC-T2+ @ 1500MHz', 'SUNW,UltraSPARC-T2+ @ 1500MHz', 'SUNW,UltraSPARC-T2+ @ 1500MHz']



# Generated at 2022-06-13 01:08:37.329986
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    from ansible.module_utils.facts.collector.sunos import SunOSHardware

    sunos_hw = SunOSHardware({}, None)

    current_time = int(time.time())
    fake_kstat_output = 'unix:0:system_misc:boot_time {}'.format(current_time - 10000)
    uptime_facts = sunos_hw.get_uptime_facts(fake_kstat_output)
    assert uptime_facts['uptime_seconds'] == 10000

# Generated at 2022-06-13 01:08:44.247239
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    # Create an instance of SunOSHardware
    sunos_hw = SunOSHardware()

    # Call method populate of class SunOSHardware
    # The return value of the method populate is a dictionary.
    sunos_facts = sunos_hw.populate()

    # Check keys of the dictionary return by method populate
    assert 'ansible_processor' in sunos_facts
    assert 'ansible_processor_cores' in sunos_facts
    assert 'ansible_processor_count' in sunos_facts
    assert 'ansible_memfree_mb' in sunos_facts
    assert 'ansible_memtotal_mb' in sunos_facts
    assert 'ansible_swapfree_mb' in sunos_facts
    assert 'ansible_swaptotal_mb' in sunos_facts

# Generated at 2022-06-13 01:08:55.991418
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    # Create a simple version of SunOSHardware
    class TestSunOSHardware(SunOSHardware):
        def __init__(self, module):
            self.module = module

    class TestModule:
        def __init__(self, run_command_result):
            self.run_command_result = run_command_result

        def run_command(self, cmd, environ_update=None, check_rc=True, close_fds=True, data=None):
            return self.run_command_result

        def get_bin_path(self, app, opt_dirs=None):
            return "/usr/sbin/%s" % app

    # Create an instance of the TestSunOSHardware class
    tsh = TestSunOSHardware(TestModule(""))

    # Create a valid kstat command output

# Generated at 2022-06-13 01:09:08.114980
# Unit test for method get_device_facts of class SunOSHardware

# Generated at 2022-06-13 01:09:29.219399
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    module = AnsibleModule(argument_spec={})
    hardware = SunOSHardware(module=module)
    facts = hardware.populate()
    assert facts['system_vendor'].startswith('Oracle Corporation')

# Generated at 2022-06-13 01:09:38.052031
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    import mock
    from ansible.module_utils.facts.hardware.sunos import SunOSHardware

    module = mock.Mock()

    class MockReturnObj():
        stdout = "Sun Microsystems  Sun Fire V440 Server"

    class MockReturnObj2():
        stdout = "Sun Microsystems  "

    class MockReturnObj3():
        stdout = "                Sun Fire V440 Server"

    class MockReturnObj4():
        stdout = " Sun Microsystems   Sun Fire V440 Server"

    class MockReturnObj5():
        stdout = "Sun MicrosystemsSun Fire V440 Server"

    module.run_command = mock.Mock(return_value=(0, MockReturnObj().stdout, "Error"))
    hw = SunOSHardware(module)

# Generated at 2022-06-13 01:09:40.630725
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    m = SunOSHardware()

    device_facts = m.get_device_facts()
    assert device_facts['devices'].get('sd0') is not None

# Generated at 2022-06-13 01:09:42.561681
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    m = SunOSHardware(dict())
    d = m.populate()
    assert d['memtotal_mb']



# Generated at 2022-06-13 01:09:51.208610
# Unit test for method get_device_facts of class SunOSHardware
def test_SunOSHardware_get_device_facts():
    test_sd = '''sderr:::Product               VBOX HARDDISK   9
sderr:::Revision              1.0
sderr:::Serial No             VB0ad2ec4d-074a
sderr:::Size    53687091200
sderr:::Vendor  ATA
sderr:::Hard Errors           0
sderr:::Illegal Request       0
sderr:::Media Error           0
sderr:::Predictive Failure Analysis       0
sderr:::Soft Errors           0
sderr:::Transport Errors      0'''
    test_sd_instances = frozenset(line.split(':')[1] for line in test_sd.split('\n') if line.startswith('sderr'))
    assert test_sd_inst

# Generated at 2022-06-13 01:09:55.016659
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    # Create instance of class SunOSHardware without arguments
    s = SunOSHardware()
    # call populate method and get result
    r = s.populate()
    # check that result is empty
    assert 0 == len(r)

# Generated at 2022-06-13 01:10:02.691053
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    hardware = SunOSHardware()
    hardware.module = AnsibleModule({})
    hardware.module.run_command = MagicMock(return_value=(0, '', ''))
    hardware.module.run_command_environ_update = {}


# Generated at 2022-06-13 01:10:10.908408
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    module_mock = Mock()
    module_mock.run_command.return_value = (0, 'unix:0:system_misc:boot_time    1548249689', '')
    module_mock.get_bin_path.return_value = '/usr/bin/kstat'

    hardware = SunOSHardware(module_mock)
    assert hardware.get_uptime_facts() == {'uptime_seconds': int(time.time()) - 1548249689}

# Generated at 2022-06-13 01:10:19.223183
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    import subprocess

    def run_command(module, cmd, check_rc=True):
        sp = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        rc = sp.wait()
        out = sp.stdout.read().strip()
        err = sp.stderr.read().strip()
        return rc, out, err

    class Module(object):
        def __init__(self):
            self.run_command = run_command

    m = Module()

    # Replace time.time() with integer value
    save_time_time = time.time
    time.time = lambda: 1548249689

    h = SunOSHardware()
    facts = h.get_uptime_facts()


# Generated at 2022-06-13 01:10:30.707046
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.facts.hardware.sunos import SunOSHardware

    # check for prtdiag output for given answers
    prtdiag_answer1 = 'System Configuration: Sun Microsystems  sun4v  Sun Fire T2000'
    prtdiag_answer2 = 'System Configuration: Oracle Corporation sun4v  sun4v'
    prtdiag_answer3 = 'System Configuration: VMware, Inc.  VMware Virtual Platform'
    prtdiag_answer4 = 'System Configuration: QEMU Standard PC (i440FX + PIIX, 1996)'
    prtdiag_answer5 = 'System Configuration: Fujitsu Primergy TX200 S8'

    expected_vendor_answer1 = 'Sun Microsystems'
    expected_vendor_answer

# Generated at 2022-06-13 01:11:13.345901
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    module = MagicMock()
    module.run_command = MagicMock(return_value=(0, '', ''))
    module.run_command_environ_update = {}

    h = SunOSHardware(module)
    h.populate()
    module.run_command.assert_has_calls([
        call('/usr/bin/kstat cpu_info'),
        call(['/usr/sbin/prtconf']),
        call('/usr/sbin/swap -s'),
        call('/usr/bin/uname -i'),
        call(['/usr/sbin/prtdiag']),
        call('/usr/bin/kstat -p'),
        call('/usr/bin/kstat -p unix:0:system_misc:boot_time'),
    ])

# Generated at 2022-06-13 01:11:19.258280
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

    hardware = SunOSHardware()
    cmd = ['/usr/bin/kstat', '-p']


# Generated at 2022-06-13 01:11:26.753497
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    result = SunOSHardware().get_memory_facts()
    assert isinstance(result, dict)
    assert result
    assert 'swapfree_mb' in result
    assert isinstance(result['swapfree_mb'], int)
    assert 'memtotal_mb' in result
    assert isinstance(result['memtotal_mb'], int)
    assert 'swap_reserved_mb' in result
    assert isinstance(result['swap_reserved_mb'], int)
    assert 'swap_allocated_mb' in result
    assert isinstance(result['swap_allocated_mb'], int)

# Generated at 2022-06-13 01:11:34.487204
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    module = AnsibleModuleMock({})
    m = SunOSHardware(module)

    rc, out, err = m.module.run_command(["/usr/sbin/prtconf"])
    for line in out.splitlines():
        if 'Memory size' in line:
            memory_size = int(line.split()[2])

    rc, out, err = m.module.run_command(["/usr/sbin/swap", "-s"])
    allocated = int(out.split()[1][:-1])
    reserved = int(out.split()[5][:-1])
    used = int(out.split()[8][:-1])
    free = int(out.split()[10][:-1])

    swap_free = free // 1024
    swap_total = (free + used) // 1024

# Generated at 2022-06-13 01:11:41.492285
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    '''
    Test method get_memory_facts for class SunOSHardware.
    Tests for method get_memory_facts in class SunOSHardware
    '''
    # Test 1
    hw = SunOSHardware()
    assert hw.get_memory_facts() == {'swap_allocated_mb': 1024,
                                     'swap_reserved_mb': 50,
                                     'swaptotal_mb': 1050,
                                     'swapfree_mb': 1024,
                                     'memtotal_mb': 651}

# Generated at 2022-06-13 01:11:51.021976
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    def run_kstat(module, command):
        return 0, command, ''

    class MyHardware(SunOSHardware):
        def run_command(self, command, **kwargs):
            return run_kstat(self.module, command)

    module = object()
    hw = MyHardware(module)
    hw.get_memory_facts() == {'memtotal_mb': -1,
                              'swapfree_mb': -1,
                              'swaptotal_mb': -1,
                              'swap_allocated_mb': -1,
                              'swap_reserved_mb': -1}



# Generated at 2022-06-13 01:11:59.315473
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():

    class MockModule:
        pass

    mod = MockModule()
    mod.run_command_environ_update = {}

    def get_file_content(path):
        current_file_path = os.path.dirname(__file__)
        fstab_file_path = os.path.join(
            current_file_path,
            'test',
            'fixtures',
            'SunOS',
            'fstab',
        )
        fstab = os.path.abspath(fstab_file_path)
        return open(fstab).read()

    hardware = SunOSHardware(module=mod,
                             timeout=1.0,
                             collected_facts={'ansible_machine': 'i86pc'},
                             get_file_content=get_file_content)

# Generated at 2022-06-13 01:12:07.230990
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    # Expected test data
    prtdiag_output = "System Configuration: Oracle Corporation sun4v Sun Fire T2000\n"
    # Parameter prtdiag_path is used for testing purpose only
    # Parameter run_command uses the mocked method _fake_run_command
    facts = SunOSHardware(dict(ANSIBLE_MODULE_ARGS={'prtdiag_path': '/bin/true'}, module=MockModule(run_command=_fake_run_command)))

    # Call the tested method
    result = facts.get_dmi_facts()

    # Verify the results
    assert result['system_vendor'] == 'Oracle Corporation'
    assert result['product_name'] == 'sun4v Sun Fire T2000'



# Generated at 2022-06-13 01:12:16.751077
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    mock_module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True)

# Generated at 2022-06-13 01:12:18.794721
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    module = AnsibleMock()
    facts_class = SunOSHardware(module)
    rc, out, err = facts_class.module.run_command(["/usr/sbin/prtconf"])
    assert "Memory size" in out



# Generated at 2022-06-13 01:13:29.409993
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    line1 = 'unix:0:system_misc:boot_time    1548249689'

    sunos = SunOSHardware()

    out = ''.join(line1 + '\n')
    uptime = sunos.get_uptime_facts()

    assert uptime['uptime_seconds'] == int(time.time() - 1548249689)

# Generated at 2022-06-13 01:13:32.798751
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    # Generate test object
    sun_hw = SunOSHardware()

    # Call method under test
    uptime_facts = sun_hw.get_uptime_facts()
    assert type(uptime_facts['uptime_seconds']) == int


# Generated at 2022-06-13 01:13:36.251929
# Unit test for method populate of class SunOSHardware
def test_SunOSHardware_populate():
    hardware_obj = SunOSHardware({'module_setup': True, 'gather_subset': ['all']}, None)
    res = hardware_obj.populate()
    assert res.get('ansible_system_vendor') == 'Oracle Corporation'
    assert res.get('ansible_product_name').split()[0] == 'sun4v'
    assert res.get('ansible_memtotal_mb') > 0
    assert res.get('ansible_swaptotal_mb') > 0

# Generated at 2022-06-13 01:13:39.852599
# Unit test for method get_memory_facts of class SunOSHardware
def test_SunOSHardware_get_memory_facts():
    module = AnsibleModule(argument_spec=dict())

    mock_run_command = MagicMock(return_value=(0, 'Memory size: 8192 Megabytes', ''))
    module.run_command = mock_run_command

    hardware = SunOSHardware(module=module)
    hardware.collect()
    assert hardware.memory_facts['memtotal_mb'] == 8192



# Generated at 2022-06-13 01:13:49.426308
# Unit test for method get_cpu_facts of class SunOSHardware
def test_SunOSHardware_get_cpu_facts():
    cpu_facts = dict(processor=['SPARC-Enterprise-T5120'])
    cpu_facts_expected = dict(processor=cpu_facts['processor'],
                              processor_cores=1,
                              processor_count=1)

    hardware = SunOSHardware
    got_cpu_facts = hardware.get_cpu_facts(cpu_facts)
    assert cpu_facts_expected == got_cpu_facts
# End test for method get_cpu_facts of class SunOSHardware


# Generated at 2022-06-13 01:13:53.585601
# Unit test for method get_dmi_facts of class SunOSHardware
def test_SunOSHardware_get_dmi_facts():
    test_obj = SunOSHardware()
    test_obj.module.run_command = lambda command, check_rc=True, close_fds=True: (0,
                                                                                  'System Configuration: Cisco Systems UCS C240 M3 \n\
 System Configuration: Sun Microsystems Sun Fire V490\n\
 System Configuration: QEMU Standard PC (Q35 + ICH9, 2009)', None)
    expected_dict = {'system_vendor': u'Cisco Systems',
                     'product_name': u'UCS C240 M3'}
    assert expected_dict == test_obj.get_dmi_facts()


# Generated at 2022-06-13 01:13:58.350647
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    module = AnsibleModule(argument_spec={})
    module.run_command = MagicMock(return_value=(0, "unix:0:system_misc:boot_time    1548249689", ""))
    uptime_facts = SunOSHardware().get_uptime_facts()
    assert uptime_facts['uptime_seconds'] == 31212190

# Generated at 2022-06-13 01:14:03.799635
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    ansible_module = AnsibleModule()
    h = SunOSHardware(ansible_module)
    h.module.run_command = lambda cmd: (0, 'unix:0:system_misc:boot_time    1548249689', '')

    facts = h.get_uptime_facts()
    # Parse the output from ansible.module_utils.facts.hardware.SunOSHardware.get_uptime_facts()
    uptime_seconds = int(facts['uptime_seconds'])
    # Assert that the uptime is less than 60 seconds
    assert uptime_seconds > 0 and uptime_seconds < 60

# Generated at 2022-06-13 01:14:12.236376
# Unit test for method get_uptime_facts of class SunOSHardware
def test_SunOSHardware_get_uptime_facts():
    # Create SunOSHardware object
    sunos = SunOSHardware()

    # Set-up string and integer that simulate output of subprocess.Popen()
    cmd = 'kstat -p unix:0:system_misc:boot_time'
    # Set up current time
    current_time = int(time.time())
    # Set up boot time
    boot_time = current_time - 10
    out = cmd + '\t' + str(boot_time)
    err = 0

    # Call method get_uptime_facts and save the value of uptime in UP
    UP = sunos.get_uptime_facts(out, err)

    # Check the result
    assert UP['uptime_seconds'] == 10


# Generated at 2022-06-13 01:14:20.064540
# Unit test for constructor of class SunOSHardwareCollector
def test_SunOSHardwareCollector():
    facts = SunOSHardwareCollector().collect()
    assert 'processor' in facts
    assert 'memtotal_mb' in facts
    assert 'swapfree_mb' in facts
    assert 'swaptotal_mb' in facts
    assert 'swap_allocated_mb' in facts
    assert 'swap_reserved_mb' in facts
    assert facts['uptime_seconds'] > 0
    assert 'system_vendor' in facts
    assert 'product_name' in facts
    assert 'vendor' in facts['devices']['sd0']
    assert 'product' in facts['devices']['sd0']
    assert 'revision' in facts['devices']['sd0']
    assert 'serial' in facts['devices']['sd0']
    assert 'size' in facts['devices']['sd0']
   