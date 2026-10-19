

# Generated at 2022-06-13 00:45:33.378206
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=['all'], required=False),
        )
    )
    collected_facts = {}
    hpux = HPUXHardware(module)
    # For systems where memory details aren't sent to syslog or the log has rotated, use parsed
    # adb output. Unfortunately /dev/kmem doesn't have world-read, so this only works as root.
    if os.access("/dev/kmem", os.R_OK):
        hpux.module.run_command = lambda x, **kw: (0, '', '')
    cpu_facts = hpux.get_cpu_facts(collected_facts=collected_facts)
    assert 'processor_count' in cpu_facts

# Generated at 2022-06-13 00:45:35.744508
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hhc = HPUXHardwareCollector()
    if hhc._platform != 'HP-UX':
        return False
    if hhc._fact_class.__name__ != 'HPUXHardware':
        return False
    return True


# Generated at 2022-06-13 00:45:40.534079
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():

    hw = HPUXHardwareCollector()
    assert isinstance(hw, HPUXHardwareCollector)
    assert hw._fact_class == HPUXHardware
    assert hw._platform == 'HP-UX'
    assert hw.required_facts == set(['platform', 'distribution'])

# Generated at 2022-06-13 00:45:52.842956
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    """Unit test for method get_hw_facts of class HPUXHardware."""
    from ansible.module_utils.facts.hardware.hpux import HPUXHardware
    facts_collected = {'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.23'}
    hpux_hardware = HPUXHardware(dict(params=dict()), facts_collected)
    hw_facts = hpux_hardware.get_hw_facts(facts_collected)
    assert hw_facts['model'] == 'ia64 hp server rx2660'
    assert hw_facts['firmware_version'] not in ('', '-')
    assert hw_facts['product_serial'] not in ('', '-')



# Generated at 2022-06-13 00:46:02.201507
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    """Test get_memory_facts method of HPUXHardware class.

    Do not run on Travis-CI or anywhere else without /dev/kmem.

    Requires a running HP-UX system with /dev/kmem world-read.
    """

    import pytest
    import subprocess
    from ansible.module_utils.facts.hardware.hpux import HPUXHardware

    hw = HPUXHardware(module=None)
    facts = hw.populate()

    try:
        assert facts['memfree_mb'] >= 0
        assert facts['memtotal_mb'] >= 0
        assert facts['swapfree_mb'] >= 0
        assert facts['swaptotal_mb'] >= 0
    except (AssertionError, KeyError):
        pytest.xfail("Memory facts probably did not run.")


# Unit test

# Generated at 2022-06-13 00:46:12.172124
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    module = type('', (), {})()
    module.run_command = lambda x: (0, '\nprocs    ---memory---                 ---swap---\n r  b   avm   fre    re    pi    po    fr   si   so   pi   po   fr   si   so  \n 0  0 28762  6249     0     0     0     0     0     0     0     0     0     0     0', '')
    module.debug = lambda x: 0
    module.config = lambda x: 0
    hardware = HPUXHardware(module)
    # Running properly
    hardware.get_memory_facts()
    # Running without vmstat command
    module.run_command = lambda x: (1, '', '')
    hardware.get_memory_facts()

# Generated at 2022-06-13 00:46:23.474884
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    module = type('AnsibleModuleFake', (), {})
    module.run_command = type('AnsibleRunCommandFakeHPUX', (), {})
    module.run_command.get_command_output = type('AnsibleRunCommandGetCommandOutputFake', (), {})
    module.run_command.get_command_output.out = [
        "Total addressable memory = 4294960000 = 409600 pages",
        "Physical: 409600 Kbytes = 400 MB",
        "Logical:  1632000 Kbytes = 1587 MB"]
    module.log = type('AnsibleLogFake', (), {})

    hw = HPUXHardware(module=module)

# Generated at 2022-06-13 00:46:29.010734
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    """
    Check that get_hw_facts returns good values for HP-UX machine
    """
    module = MockModule()
    hardware = HPUXHardware(module)
    hardware.get_hw_facts({'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.23'})
    assert module.run_command.called
    # Returned value
    exp_value = {
        'firmware_version': 'I31 02/04/2009',
        'model': 'ia64 hp Superdome 2 server'
    }
    assert hardware.facts == exp_value



# Generated at 2022-06-13 00:46:32.854697
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    module = AnsibleModule(argument_spec={})
    module.exit_json = exit_json
    h = HPUXHardware(module)
    collected_facts = {
        "ansible_architecture": '9000/800'
    }
    d = h.get_memory_facts(collected_facts=collected_facts)

    assert 'memtotal_mb' in d
    assert d['memtotal_mb'] > 0
    assert 'memfree_mb' in d
    assert d['memfree_mb'] > 0
    assert 'swaptotal_mb' in d
    assert d['swaptotal_mb'] > 0
    assert 'swapfree_mb' in d
    assert d['swapfree_mb'] > 0



# Generated at 2022-06-13 00:46:40.153225
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    module = FakeAnsibleModule()
    hardware = HPUXHardware(module)
    hardware._module.run_command = FakeModuleRunCommand(cmd_rc=[0, 0, 0])
    hardware._module.run_command.cmd_out['model'] = "9000/800"

# Generated at 2022-06-13 00:46:53.822466
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    """
    Unit test for constructor of class HPUXHardwareCollector
    :return:
    """
    hc = HPUXHardwareCollector()
    assert hc._fact_class == HPUXHardware
    assert hc._platform == 'HP-UX'
    assert hc.required_facts == set(['platform', 'distribution'])

# Generated at 2022-06-13 00:46:57.597008
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    module = ansible.module_utils.basic.AnsibleModule
    args = {"gather_subset": ["all"]}
    setattr(module, 'params', args)
    hardware = HPUXHardware(module)
    hardware.populate(collected_facts=None)

# Generated at 2022-06-13 00:47:01.370500
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hardware_collector = HPUXHardwareCollector()
    assert hardware_collector._fact_class == HPUXHardware
    assert hardware_collector._platform == 'HP-UX'
    assert hardware_collector.required_facts == {'platform', 'distribution'}

# Generated at 2022-06-13 00:47:11.277610
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    # Create an instance of HPUXHardware for this test
    hphw = HPUXHardware()

    # Create an instance of mock module
    from ansible.module_utils.facts import module_utils
    from ansible.module_utils.facts.hardware import mock_module
    mm = mock_module.MockModule(module_utils)
    hphw.module = mm
    facts = {}
    facts['ansible_architecture'] = 'ia64'
    facts['ansible_distribution_version'] = "B.11.23"

    # Retrieve values for different parameters
    hw_facts = hphw.get_hw_facts(facts)

    # Test if the result is expected
    assert hw_facts['firmware_version'] == '"v2.75 (20/10/2009)"'


# Generated at 2022-06-13 00:47:17.688909
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    hardware = HPUXHardware()
    hardware.module = MockModule('ansible_architecture=ia64')
    hardware.module.run_command = Mock(return_value=('0', 'ia64', 'model'))
    hardware.module.run_command = Mock(return_value=('0', 'Firmware revision: 6.6', 'firmware_version'))
    result = hardware.get_hw_facts({'ansible_architecture': 'ia64'})
    assert result.get('firmware_version') == '6.6'
    assert result.get('model') == 'ia64'



# Generated at 2022-06-13 00:47:20.676912
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    required_facts = set(['platform', 'distribution'])
    hpux = HPUXHardwareCollector(required_facts=required_facts)
    assert hpux.platform == 'HP-UX'
    assert hpux.required_facts == required_facts
    assert hpux._fact_class == HPUXHardware


# Generated at 2022-06-13 00:47:26.686741
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=['!all'], type='list'),
            filter=dict(default=None, type='str')
        )
    )

    result = dict(
        changed=False,
        ansible_facts=dict(
            ansible_architecture='ia64',
            ansible_distribution='HP-UX',
            ansible_distribution_version='B.11.31'
        )
    )
    hardware_collector = HPUXHardwareCollector(module=module)
    hardware_collector.collect()
    assert result == hardware_collector.get_facts()

# Generated at 2022-06-13 00:47:38.155672
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    module = AnsibleModule(argument_spec={})
    hardware = HPUXHardware(module)
    rc, out, err = module.run_command("/usr/contrib/bin/machinfo | grep Memory", use_unsafe_shell=True)
    data = re.search(r'Memory[\ :=]*([0-9]*).*MB.*', out).groups()[0].strip()
    rc, out, err = module.run_command("/usr/sbin/swapinfo -m -d -f -q")
    swap = int(out.strip())
    rc, out, err = module.run_command("/usr/sbin/swapinfo -m -d -f | egrep '^dev|^fs'", use_unsafe_shell=True)
    swapfree = 0

# Generated at 2022-06-13 00:47:39.347500
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    assert isinstance(HPUXHardwareCollector(), HardwareCollector)

# Generated at 2022-06-13 00:47:45.088813
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    # Initialize empty facts object
    facts_object = HPUXHardware(dict())

    # Populate facts related to memory
    memory_facts = facts_object.get_memory_facts()
    assert 'memtotal_mb' in memory_facts.keys()
    assert 'memfree_mb' in memory_facts.keys()
    assert 'swapfree_mb' in memory_facts.keys()
    assert 'swaptotal_mb' in memory_facts.keys()

    # Populate facts related to CPU
    cpu_facts = facts_object.get_cpu_facts()
    assert 'processor_count' in cpu_facts.keys()
    assert 'processor' in cpu_facts.keys()
    assert 'processor_cores' in cpu_facts.keys()

    # Populate facts related to HW
    hw_facts = facts_object

# Generated at 2022-06-13 00:48:14.982468
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    module_args = dict(
        gather_subset='all',
        filter='*',
    )
    gathered_facts = {}
    # test populate with B.11.23
    gathered_facts['ansible_architecture'] = 'ia64'
    gathered_facts['ansible_distribution_version'] = 'B.11.23'
    module = FakeModule(module_args, gathered_facts=gathered_facts)
    hardware = HPUXHardware(module)
    hardware.populate()
    dest = '/tmp/ansible_test_HPUXHardware_populate'
    file = open(dest, 'w')
    file.write(str(hardware.facts))
    file.close()
    file = open(dest, 'r')
    data = file.read()
    file.close()
    os

# Generated at 2022-06-13 00:48:24.347152
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    module = None
    hw = HPUXHardware(module)
    collected_facts = dict(ansible_architecture='ia64',
                           ansible_distribution_version='B.11.23')

    memory_facts = hw.get_memory_facts(collected_facts=collected_facts)
    memtotal_mb = memory_facts['memtotal_mb']
    memfree_mb = memory_facts['memfree_mb']
    swaptotal_mb = memory_facts['swaptotal_mb']
    swapfree_mb = memory_facts['swapfree_mb']

    assert(memtotal_mb > 0)
    assert(memfree_mb > 0)
    assert(swaptotal_mb > 0)
    assert(swapfree_mb > 0)


# Generated at 2022-06-13 00:48:29.975568
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    with open('/proc/meminfo') as meminfo_file:
        meminfo_file_content = meminfo_file.read()
    test_meminfo = meminfo_file_content.splitlines()
    test_meminfo.extend(['MemTotal:       100000', 'MemFree:         5000', 'Buffers:         1000', 'Cached:          2000'])
    test_meminfo.append('SwapTotal:       512000')
    test_meminfo.append('SwapFree:        480000')
    module = dict(SELECTED_MODULE_NAME='whoami', PATH='/sbin:/usr/sbin:/bin:/usr/bin')

    hardware = HPUXHardware(module)
    hardware.module.run_command = mock.Mock(return_value=(0, '', ''))

# Generated at 2022-06-13 00:48:40.121307
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    facts_dict = {
        'platform': 'HP-UX',
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.31'
    }

    hardware_collector = HPUXHardwareCollector(facts_dict)
    hw = hardware_collector.collect()

    assert isinstance(hw, dict)
    assert 'model' in hw
    assert 'firmware_version' in hw
    assert 'product_serial' in hw
    assert hw['model'] == 'ia64 hp server rx4640'
    assert hw['firmware_version'] == 'iLO 2 2.53'
    assert hw['product_serial'] == 'USC03929'



# Generated at 2022-06-13 00:48:43.960582
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    h = HPUXHardwareCollector()
    assert h.__class__.__name__ == 'HPUXHardwareCollector'
    assert h.platform == 'HP-UX'
    assert h.fact_class == HPUXHardware
    assert str(h.required_facts) == "{'platform', 'distribution'}"

# Generated at 2022-06-13 00:48:46.669426
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hw_obj = HPUXHardwareCollector()
    assert hw_obj.platform == 'HP-UX'
    assert hw_obj.required_facts == set(['platform', 'distribution'])
    assert hw_obj.optional_facts == set([])


# Generated at 2022-06-13 00:48:51.532697
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    module = FakeModule({})
    hardware = HPUXHardware(module)

    # Test on success
    module = FakeModule({"ansible_architecture": "9000/800", "ansible_distribution_version": "B.11.23"})
    hardware = HPUXHardware(module)
    hardware.get_memory_facts()
    assert hardware.facts['memtotal_mb'] == 14280
    assert hardware.facts['swaptotal_mb'] == 67108864
    assert hardware.facts['swapfree_mb'] == 67108864
    assert hardware.facts['memfree_mb'] == 14035

    # Test on error
    module = FakeModule({"ansible_architecture": "9000/800", "ansible_distribution_version": "B.11.11"})
    hardware = HPU

# Generated at 2022-06-13 00:49:02.766723
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    test_module = type('module', (object,), {})()
    setattr(test_module, 'run_command', lambda _, use_unsafe_shell=False: ('', '', ''))
    test_HPUXHardware = HPUXHardware(test_module, {'processor': '9000/800'})
    test_HPUXHardware.get_cpu_facts()
    assert test_HPUXHardware.cpu_facts['processor_count'] == 1

    test_HPUXHardware = HPUXHardware(test_module, {'processor': '9000/785'})
    test_HPUXHardware.get_cpu_facts()
    assert test_HPUXHardware.cpu_facts['processor_count'] == 1


# Generated at 2022-06-13 00:49:05.008242
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hw = HPUXHardwareCollector()
    assert(hw.platform == 'HP-UX')
    assert(hw._fact_class == HPUXHardware)

# Generated at 2022-06-13 00:49:09.848004
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    data = {
        'ansible_architecture': 'ia64',
        'ansible_distribution': 'HP-UX',
        'ansible_distribution_version': 'B.11.31'
    }
    hardware = HPUXHardware({}, data, data)
    assert hardware.get_memory_facts() == {'swaptotal_mb': 6523, 'swapfree_mb': 6399, 'memtotal_mb': 2048, 'memfree_mb': 275}

# Generated at 2022-06-13 00:50:13.810677
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    m = HPUXHardware({})
    m.module.run_command = lambda *args, **kwargs: (0, '1', '')
    m.module.params = {'gather_subset': ['all']}
    facts = m.populate()
    assert facts['memfree_mb'] == '1'
    assert facts['memtotal_mb'] == '1'
    assert facts['swapfree_mb'] == '1'
    assert facts['swaptotal_mb'] == '1'
    assert facts['processor'] == '1'
    assert facts['processor_cores'] == '1'
    assert facts['processor_count'] == '1'
    assert facts['model'] == '1'
    m.module.run_command = lambda *args, **kwargs: (1, '', '')
    facts

# Generated at 2022-06-13 00:50:23.780208
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    # Test of method get_cpu_facts with release B.11.31
    facts = HPUXHardware().get_cpu_facts(collected_facts={'ansible_architecture': "ia64", 'ansible_distribution_version': "B.11.31"})
    assert facts["processor"] == "Intel Itanium 9300 model 12"
    assert facts["processor_count"] == 2
    assert facts["processor_cores"] == 4
    # Test of method get_cpu_facts with release B.11.23
    facts = HPUXHardware().get_cpu_facts(collected_facts={'ansible_architecture': "ia64", 'ansible_distribution_version': "B.11.23"})
    assert facts["processor"] == "Intel Itanium 9300 model 12"
    assert facts["processor_count"]

# Generated at 2022-06-13 00:50:32.833176
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    # Prepare test data
    test_hardware = HPUXHardware({'module': 'fake'})

    test_hardware.module.run_command = lambda *args, **kwargs: (0, "1234", None)
    test_hardware.module.run_command.side_effect = lambda *args, **kwargs: (0, "1234", None)

    # Run test
    test_hardware.populate({})

    # Assertions
    assert test_hardware.facts.get('memfree_mb', None) == 4
    assert test_hardware.facts.get('memtotal_mb', None) == 4
    assert test_hardware.facts.get('swapfree_mb', None) == 0
    assert test_hardware.facts.get('swaptotal_mb', None) == 0

# Generated at 2022-06-13 00:50:42.485673
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec=dict())
    # test get_cpu_facts with empty collected_facts
    hpux_hardware = HPUXHardware(module)
    cpu_facts_empty = hpux_hardware.get_cpu_facts()
    assert cpu_facts_empty == {}
    # test get_cpu_facts with B.11.23 on PA-RISC
    collected_facts = dict()
    collected_facts['ansible_architecture'] = '9000/800'
    hpux_hardware = HPUXHardware(module)
    cpu_facts_B11_23_parisc = hpux_hardware.get_cpu_facts(collected_facts=collected_facts)
    assert cpu_facts_B11_23_parisc == {'processor_count': 1}
    # test get

# Generated at 2022-06-13 00:50:49.880674
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    # Testing inventory module
    hpx_inv = HPUXHardwareCollector()
    assert hpx_inv.platform == 'HP-UX'
    assert hpx_inv._platform == 'HP-UX'
    assert hpx_inv.required_facts == set(['platform', 'distribution'])
    assert hpx_inv._fact_class == HPUXHardware



# Generated at 2022-06-13 00:50:55.471511
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    hardware = HPUXHardware()
    hardware.module = FakeModule({'ansible_distribution': 'HP-UX', 'ansible_distribution_version': 'B.11.23'})
    hardware.module.run_command = lambda cmd, **kwargs: (0, 'Intel(R) Itanium(R) Family NUMA qid 0', '')
    hw_facts = hardware.get_hw_facts()

    assert hw_facts['model'] == 'Intel(R) Itanium(R) Family NUMA qid 0'
    assert hw_facts['firmware_version'] == ''



# Generated at 2022-06-13 00:51:01.615072
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    data = {'ansible_architecture': 'ia64',
            'ansible_distribution_version': "B.11.31"}
    h = HPUXHardware(dict(), data)
    result = h.populate()
    assert result.get('processor_count') == 4
    assert result.get('processor') == 'Intel(R) Itanium(R) Processor 9330'
    assert result.get('processor_cores') == 8
    assert resul

# Generated at 2022-06-13 00:51:10.479726
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    mock_module = MagicMock()

# Generated at 2022-06-13 00:51:18.604092
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    module = type('', (object,), {})
    module.run_command = type('', (object,), {})
    arguments = {'ansible_architecture': '9000/800'}
    module.run_command.return_value = (0, '/usr/bin/vmstat | tail -1: procs --------memory----- ---swap-- -----io---- --system-- -----cpu------\n r  b   avm   fre  re  pi  po  fr  sr   cy   in   sy   cs  us  sy  id  wa  st', '')
    hardware_facts = HPUXHardware(module, arguments).get_memory_facts()
    assert hardware_facts['memfree_mb'] == 16
    assert hardware_facts['memtotal_mb'] == 2048

# Generated at 2022-06-13 00:51:25.566394
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    """Test to check the response of get_hw_facts method of HPUXHardware class"""
    class TestModule:
        def __init__(self):
            self.params = {}
            self.run_command = self.fake_run_command
            self.exit_json = self.fake_exit_json
            self.fail_json = self.fake_fail_json
        def fake_exit_json(self, **kwargs):
            pass

        def fake_fail_json(self, **kwargs):
            pass

        def fake_run_command(self, cmd, use_unsafe_shell=False):
            """Fake run_command: looks for the command and return proper output"""
            """
            expected values of rc:
            0: No error
            1: Error
            2: Command not found
            """

# Generated at 2022-06-13 00:52:22.339133
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    h = HPUXHardwareCollector()
    assert h.platform == 'HP-UX'

    h = HPUXHardwareCollector(platform='Linux')
    assert h.platform == 'HP-UX'


# Generated at 2022-06-13 00:52:23.842312
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hpuxHardwareCollector = HPUXHardwareCollector()
    assert hpuxHardwareCollector.__class__.__name__ == 'HPUXHardwareCollector'


# Generated at 2022-06-13 00:52:29.267983
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=['all'], type='list'),
        ),
        supports_check_mode=False,
    )
    module.run_command = MagicMock(return_value=(0, 'test_model', ''))
    hw_facts = HPUXHardware(module=module)
    ansible_facts = hw_facts.populate()
    assert 'model' in ansible_facts



# Generated at 2022-06-13 00:52:31.330234
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hw_facts = HPUXHardwareCollector(None, None, None)
    assert hw_facts.platform == 'HP-UX'
    assert hw_facts.required_facts == set(['platform', 'distribution'])
    assert hw_facts._fact_class == HPUXHardware

# Generated at 2022-06-13 00:52:34.233921
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    h = HPUXHardwareCollector()
    assert h.platform == 'HP-UX'
    assert h.required_facts == set(['platform', 'distribution'])


# Unit tests for constructor and additional method for class HPUXHardware

# Generated at 2022-06-13 00:52:43.190509
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    module = MockModule()
    class_instance = HPUXHardware(module)
    module.run_command.return_value = (0, '1', '')
    collected_facts = {'ansible_architecture': '9000/800'}
    result = class_instance.get_cpu_facts(collected_facts=collected_facts)
    assert result == {'processor_count': 1}
    collected_facts = {'ansible_architecture': 'ia64'}
    result = class_instance.get_cpu_facts(collected_facts=collected_facts)
    assert result == {}
    module.run_command.return_value = (0, 'Intel(r) Itanium(r) 9300 series processor @ 1.60GHz', '')

# Generated at 2022-06-13 00:52:50.990511
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    be = HPUXHardware()
    hardware_facts = be.populate()

    hardware_facts['model'].strip().startswith('B')
    hardware_facts['memfree_mb'] > 0
    hardware_facts['memtotal_mb'] > 0
    hardware_facts['swapfree_mb'] > 0
    hardware_facts['swaptotal_mb'] > 0
    hardware_facts['processor'] != ''
    hardware_facts['processor_cores'] > 0
    hardware_facts['processor_count'] > 0
    hardware_facts['product_serial'] != ''
    hardware_facts['firmware_version'] != ''


# Generated at 2022-06-13 00:53:02.226912
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    # Initialize
    module_args = {
        'architecture': 'ia64',
        'distribution_version': 'B.11.23'
    }
    hw = HPUXHardware(module_args)
    rc, out, err = hw.module.run_command("echo 'phys_mem_pages/D' | adb -k /stand/vmunix /dev/kmem | tail -1 | awk '{print $2}'",
                                         use_unsafe_shell=True)
    memtotal_kb = int(out)
    # Test all in one

# Generated at 2022-06-13 00:53:09.296241
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec={})
    HardwareCollector._instance = HPUXHardwareCollector()
    module.params = {
        'dest': '/tmp/facts',
        'gather_subset': 'all'
    }
    collected_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution': 'HP-UX',
        'ansible_distribution_version': 'B.11.31'
    }
    HardwareCollector._instance.get_all(module, collected_facts)



# Generated at 2022-06-13 00:53:14.150169
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    module = AnsibleModule(argument_spec={})
    collected_facts = {'ansible_architecture': 'ia64', 'ansible_distribution': 'HP-UX'}
    hardware = HPUXHardware(module)
    facts = {'memtotal_mb': 4096, 'swaptotal_mb': 2048, 'swapfree_mb': 1024, 'memfree_mb': 2048}

    if module.check_mode:
        module.fail_json(msg='In check mode it is not possible to run commands')
    else:
        out = hardware.get_memory_facts(collected_facts=collected_facts)
        assert out == facts



# Generated at 2022-06-13 00:54:18.378274
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
   hhc = HPUXHardwareCollector()
   assert hhc.platform == 'HP-UX'
   assert hhc.required_facts == set(['platform', 'distribution'])


# Generated at 2022-06-13 00:54:24.879632
# Unit test for method get_hw_facts of class HPUXHardware

# Generated at 2022-06-13 00:54:28.327178
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    test_obj = HPUXHardware({})
    result = test_obj.get_hw_facts({'platform': 'Linux'})
    assert result == {}


# Generated at 2022-06-13 00:54:29.861864
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hardware_collector = HPUXHardwareCollector()
    assert hardware_collector._fact_class == HPUXHardware

# Generated at 2022-06-13 00:54:31.344131
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hwc = HPUXHardwareCollector()
    assert hwc._facts['distribution'] == 'HP-UX'

# Generated at 2022-06-13 00:54:39.761031
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    # prepare test data for get_cpu_facts
    cpu_facts_data = {
        'ansible_architecture': '9000/800',
        'ansible_distribution_version': 'B.11.31',
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.31',
    }


# Generated at 2022-06-13 00:54:45.931482
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    module = AnsibleModuleMock()
    module.params = {}
    hw = HPUXHardware({'mock': module})
    out = hw.get_hw_facts()
    assert out['model'] == '9000/800'
    assert out['firmware_version'] == 'B.11.11'
    assert out['product_serial'] == '90000000'



# Generated at 2022-06-13 00:54:55.348332
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():

    # create new instance of HPUXHardware class
    hw = HPUXHardware({
        'distribution_version': 'B.11.23',
        'architecture': 'ia64'
    })

    # invoke get_hw_facts() and get list of facts
    # this run is for a system of Release B.11.23
    facts = hw.get_hw_facts()

    # assert facts
    assert facts['model'] == 'ia64 hp server rx4640'
    assert facts['firmware_version'] == '0108'
    assert facts['product_serial'] == 'RZ532A00086'

    # create new instance of HPUXHardware class

# Generated at 2022-06-13 00:55:02.665409
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():

    # test HP-UX with CPU count from ioscan and processor from machinfo
    module = FakeAnsibleModule()
    module.params = {'gather_subset': 'all'}
    collected_facts = dict(
        ansible_architecture='ia64',
        ansible_distribution_version='B.11.23'
    )
    hardware = HPUXHardware(module=module)
    cpu_facts = hardware.get_cpu_facts(collected_facts=collected_facts)
    assert cpu_facts['processor_count'] == 2
    assert cpu_facts['processor'] == 'Intel(R) Itanium(R) Processor'

    # test HP-UX with CPU count from machinfo and processor from machinfo
    module = FakeAnsibleModule()

# Generated at 2022-06-13 00:55:10.626198
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    class TestFacts:
        def __init__(self):
            self.facts = {}

        def get(self, fact):
            return self.facts.get(fact, None)

        def set(self, key, value):
            self.facts[key] = value

    class TestModule:
        def __init__(self, facts):
            self.facts = facts

            self.warnings = []

            self.run_command_calls = []
            self.run_command_responses = []

        def run_command(self, cmd, use_unsafe_shell=False):
            self.run_command_calls.append(cmd)

            return self.run_command_responses.pop(0)

    hpuxtest = HPUXHardware()

    test_facts = TestFacts()
    test_facts