

# Generated at 2022-06-13 00:45:29.720171
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hw_facts = HardwareCollector.factory(HPUXHardwareCollector)
    assert isinstance(hw_facts, HPUXHardwareCollector) is True
    assert isinstance(hw_facts._fact_class, HPUXHardware) is True
    assert hw_facts._platform == 'HP-UX'
    assert hw_facts.required_facts == {'platform', 'distribution'}

# Generated at 2022-06-13 00:45:37.231719
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    class ModuleStub(object):
        def run_command(self, *args, **kwargs):
            if args[0] == "/usr/bin/vmstat | tail -1":
                return 0, "procs\tmemory\tswap\tio\tsystem\tidle\n  r  b   avm   fre  re  pi  po  fr  sr  cy  in   sy  cs us sy id wa\n 0 0 16342 9899 0  0  0  0  0  0  0   2   0   0  3  0 97  0\n", ''
            if args[0] == "grep Physical /var/adm/syslog/syslog.log":
                return 0, "Aug 21 09:02:19 testserver vmunix: Physical: 4194304 Kbytes (2048 pages) free",

# Generated at 2022-06-13 00:45:43.533721
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    module = AnsibleModule(
        argument_spec = dict()
    )
    if not HPUXHardwareCollector.is_platform_supported(module):
        pytest.skip("platform not supported")
    hardware_facts = HPUXHardwareCollector.collect(module)
    assert hardware_facts['processor_count'] == 1200



# Generated at 2022-06-13 00:45:51.728966
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    module = AnsibleModule(argument_spec={})

    h = HPUXHardware(module=module)
    h.populate()
    assert 'processor' in h.facts
    assert 'processor_cores' in h.facts
    assert 'processor_count' in h.facts
    assert 'memfree_mb' in h.facts
    assert 'memtotal_mb' in h.facts
    assert 'swapfree_mb' in h.facts
    assert 'swaptotal_mb' in h.facts
    assert 'model' in h.facts
    assert 'firmware_version' in h.facts



# Generated at 2022-06-13 00:45:57.438440
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    facts = { 'ansible_architecture': '9000/785', 'ansible_distribution': 'HPUX' }
    obj = HPUXHardware(module=None, facts=facts)
    obj.get_memory_facts()
    assert obj.memory_facts.get('memtotal_mb') == 65536
    assert obj.memory_facts.get('memfree_mb') == 16



# Generated at 2022-06-13 00:46:02.136373
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    HardwareCollector.collectors['HP-UX'] = HPUXHardwareCollector
    hardware_collector = HPUXHardwareCollector()
    assert isinstance(hardware_collector, HPUXHardwareCollector)
    assert isinstance(hardware_collector.platform, str)
    assert isinstance(hardware_collector.required_facts, set)
    assert len(hardware_collector.required_facts) == 2

# Generated at 2022-06-13 00:46:12.486572
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    # Collected facts
    collected_facts = {'ansible_architecture': 'ia64',
                       'ansible_distribution': 'HP-UX',
                       'ansible_distribution_version': 'B.11.23'}
    # Expected facts
    expected_facts = {'processor': 'Intel Itanium 2 9100 series',
                      'processor_cores': 1,
                      'processor_count': 1}
    # Test module
    test_module = MockModule()
    test_module.params = {}
    # Test class
    hw_obj = HPUXHardware(test_module)
    # Test method
    cpu_facts = hw_obj.get_cpu_facts(collected_facts=collected_facts)
    assert cpu_facts == expected_facts



# Generated at 2022-06-13 00:46:23.803561
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    """
    Create a instance of HPUXHardware using a fake ansible module.
    Ansible module was replaced by MockAnsibleModule, defined in unit test library,
    that simulates real behavior of an AnsibleModule, calling real methods
    of the class, but with predefined return values.
    """
    # create a instance of class with defaults
    hardware = HPUXHardware()
    hardware.module = MockAnsibleModule()
    hardware.module.params = {}
    facts = hardware.populate()
    # create some specific return values for methods that are called by populate()
    hardware.module.run_command.return_value = (0, "8", '')
    hardware.module.file_exists.return_value = True
    hardware.module.get_bin_path.return_value = "/bin"

# Generated at 2022-06-13 00:46:33.685427
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    hw = HPUXHardware()
    hw.module.run_command = lambda x, **args: [0, "3", ""]
    collected_facts = {'ansible_architecture': '9000/800'}
    cpu_facts = hw.get_cpu_facts(collected_facts)
    assert cpu_facts == {'processor_count': 3}
    collected_facts = {'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.23'}
    cpu_facts = hw.get_cpu_facts(collected_facts)
    assert cpu_facts == {'processor_count': 3, 'processor': 'Intel(R) Itanium(R) Processor',
                         'processor_cores': 1}

# Generated at 2022-06-13 00:46:40.352534
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    hpux_hardware = HPUXHardware()
    hpux_hardware.module = MagicMock()
    hpux_hardware.module.run_command.return_value = 0, "3\n", ""

    collected_facts = {
        "ansible_architecture": "9000/800",
        "ansible_distribution_version": "B.11.31"
    }
    cpu_facts = hpux_hardware.get_cpu_facts(collected_facts)

    assert 'processor_count' in cpu_facts
    assert cpu_facts['processor_count'] == 3
    assert 'processor_cores' in cpu_facts
    assert cpu_facts['processor_cores'] == 1
    assert 'processor' in cpu_facts


# Generated at 2022-06-13 00:46:58.761469
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    module = AnsibleModuleMock()
    hardware = HPUXHardware(module)
    processor_count = hardware.get_cpu_facts(collected_facts={'ansible_architecture': '9000/800'})['processor_count']
    assert processor_count == 2
    processor_count = hardware.get_cpu_facts(collected_facts={'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.23'})['processor_count']
    assert processor_count == 16
    processor_count = hardware.get_cpu_facts(collected_facts={'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.31'})['processor_count']
    assert processor_count == 16
    processor_cores = hardware.get

# Generated at 2022-06-13 00:47:04.925013
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    collector = HPUXHardwareCollector(module)
    hardware = collector.collect()[0]
    cpu_facts = hardware.get_cpu_facts()
    assert 'processor_count' in cpu_facts.keys()
    assert 'processor' in cpu_facts.keys()
    assert 'processor_cores' in cpu_facts.keys()


# Generated at 2022-06-13 00:47:12.993963
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    collected_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.23'
    }
    hpu = HPUXHardware()
    memory_facts = hpu.get_memory_facts(collected_facts=collected_facts)

    assert isinstance(memory_facts['memfree_mb'], int)
    assert memory_facts['memfree_mb'] > 0
    assert isinstance(memory_facts['memtotal_mb'], int)
    assert memory_facts['memtotal_mb'] > 0
    assert isinstance(memory_facts['swapsize_mb'], int)
    assert memory_facts['swapsize_mb'] > 0


# Generated at 2022-06-13 00:47:15.117812
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    module = FakeAnsibleModule(platform='HP-UX',
                               distribution='B.11.31')
    facts_collector = HPUXHardwareCollector(module=module)
    hardware_obj = HPUXHardware()
    hardware_obj.populate()
    hardware_obj.get_hw_facts()



# Generated at 2022-06-13 00:47:20.956110
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    test_module = AnsibleModule(argument_spec={})
    test_hardware = HPUXHardware(test_module)
    test_facts = {
        "ansible_architecture": '9000/800'
    }
    cpu_facts = test_hardware.get_cpu_facts(test_facts)
    assert cpu_facts['processor_count'] == 4
    test_facts = {
        "ansible_architecture": 'ia64',
        "ansible_distribution_version": "B.11.23"
    }
    cpu_facts = test_hardware.get_cpu_facts(test_facts)
    assert cpu_facts['processor_count'] == 4
    assert cpu_facts['processor'] == 'Intel(R) Xeon(R) CPU        E7-2870  @ 2.40GHz'

# Generated at 2022-06-13 00:47:22.868896
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():

    # Create Hardware object
    hardware = HPUXHardware()

    # Test for get_memory_facts method
    hardware.get_memory_facts()


# Generated at 2022-06-13 00:47:27.386907
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    module = None
    hardware = HPUXHardware(module)

    collected_facts = {'ansible_architecture': 'ia64', 'ansible_distribution_version': '11.31'}

    out = hardware.get_hw_facts(collected_facts=collected_facts)
    assert out['firmware_version'] == '1.63.2'
    assert out['model'] == 'ia64 hp server'
    assert out['product_serial'] == 'CZC3811J05'

# Generated at 2022-06-13 00:47:33.178878
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    # so that this will work without actually being on an HPUX system
    os.environ['PATH'] = os.pathsep.join(['/bin', os.environ['PATH']])
    HPUXHardwareCollector()

# Generated at 2022-06-13 00:47:36.404975
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hc = HPUXHardwareCollector()
    assert hc._fact_class == HPUXHardware
    assert hc._platform == 'HP-UX'
    assert hc.required_facts == set(['platform', 'distribution'])

# Generated at 2022-06-13 00:47:43.310883
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec={})
    module.get_bin_path = MagicMock(return_value=True)
    set_module_args(dict(
        gather_subset='all',
    ))
    result = HPUXHardware(module).get_cpu_facts()
    # Check the fact processor_count
    if result['processor_count'] != 2:
        module.fail_json(msg="The processor_count is incorrect")
    # Check the fact processor
    if result['processor'] != 'Intel(r) Itanium(r) 2 Processor family 9000 series':
        module.fail_json(msg="The processor is incorrect")
    # Check the fact processor_cores
    if result['processor_cores'] != 1:
        module.fail_json(msg="The processor_cores is incorrect")
    #

# Generated at 2022-06-13 00:48:12.136066
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    import pytest
    from ansible.module_utils.facts.hardware.hpux import HPUXHardware
    h = HPUXHardware(None)
    collected_facts = {
        'ansible_architecture': '9000/800',
        'ansible_distribution_version': 'B.11.23'
    }
    cpu_facts = h.get_cpu_facts(collected_facts=collected_facts)
    assert cpu_facts['processor_count'] == 1
    collected_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.23'
    }
    cpu_facts = h.get_cpu_facts(collected_facts=collected_facts)
    assert cpu_facts['processor_count'] == 2
   

# Generated at 2022-06-13 00:48:19.770491
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():

    input = {'ansible_architecture': 'ia64',
             'ansible_distribution_version': 'B.11.31'}

    # Capture result of the HPUXHardware class method get_memory_facts
    hw = HPUXHardware({})
    result = hw.get_memory_facts(collected_facts=input)

    for k, v in result.items():
        print("%s ---> %s" % (k, v))

    assert 'memfree_mb' in result
    assert 'memtotal_mb' in result
    assert 'swapfree_mb' in result
    assert 'swaptotal_mb' in result

# Generated at 2022-06-13 00:48:20.685929
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    HPUXHardwareCollector()

# Generated at 2022-06-13 00:48:25.382856
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    module = AnsibleModule(argument_spec={})
    hardware = HPUXHardware(module)
    hardware.populate()
    # Test all defined attributes are present
    for attr in ['processor', 'processor_cores', 'processor_count', 'memfree_mb', 'memtotal_mb', 'swaptotal_mb', 'swapfree_mb']:
        assert attr in hardware.facts

# Generated at 2022-06-13 00:48:30.192370
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hw = HPUXHardwareCollector()
    assert HPUXHardwareCollector._fact_class == HPUXHardware
    assert HPUXHardwareCollector._platform == 'HP-UX'
    assert HPUXHardwareCollector.required_facts == set(['platform', 'distribution'])

# Generated at 2022-06-13 00:48:35.566648
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    module = get_test_module()
    hwx = HPUXHardware(module)
    hw_facts = hwx.get_hw_facts()
    assert hw_facts == {'model': 'ia64 hp server rx2800 i4', 'firmware_version': 'B.11.31.0904', 'product_serial': '13415QAC0'}


# Generated at 2022-06-13 00:48:38.735911
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    hardware = HPUXHardware()
    collected_facts = {'ansible_architecture': 'ia64'}
    hardware.populate(collected_facts)

# Generated at 2022-06-13 00:48:42.042659
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hpu = HPUXHardwareCollector()
    assert hpu.platform == "HP-UX"
    assert hpu.fact_class == HPUXHardware
    assert hpu.required_facts == set(['platform', 'distribution'])

# Generated at 2022-06-13 00:48:44.962521
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    hw_facts = {'product_serial': '00J1E31U6Y', 'firmware_version': "v5.0.5.5 (UEFI)"}

    ret = HPUXHardware({'ansible_facts': {'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.23'}}).get_hw_facts()
    assert ret == hw_facts

# Generated at 2022-06-13 00:48:51.342716
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    my_collector = HPUXHardwareCollector()
    assert my_collector._fact_class == HPUXHardware
    assert my_collector._platform == 'HP-UX'
    assert my_collector.required_facts == {'platform', 'distribution'}

# Generated at 2022-06-13 00:49:15.313488
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    module = FakeModule()
    hardware = HPUXHardware()
    hardware.module = module
    hardware.module.run_command = FakeRunCommand()

    hardware.module.run_command.set_command("/usr/contrib/bin/machinfo | grep Memory", stdout="Memory : 65034 MB")
    hardware.module.run_command.set_command("/usr/sbin/swapinfo -m -d -f -q", stdout="10240")
    hardware.module.run_command.set_command("/usr/sbin/swapinfo -m -d -f | egrep '^dev|^fs'", stdout="dev 		  fs 	   102400 	   102400")

# Generated at 2022-06-13 00:49:26.022269
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    module = AnsibleModuleMock(params={})
    hhw = HPUXHardware(module)
    test_facts = hhw.populate()

    assert 'processor' in test_facts.keys()
    assert 'processor_cores' in test_facts.keys()
    assert 'processor_count' in test_facts.keys()
    assert 'model' in test_facts.keys()
    assert 'firmware_version' in test_facts.keys()
    assert 'product_serial' in test_facts.keys()
    assert 'memtotal_mb' in test_facts.keys()
    assert 'memfree_mb' in test_facts.keys()
    assert 'swaptotal_mb' in test_facts.keys()
    assert 'swapfree_mb' in test_facts.keys()



# Generated at 2022-06-13 00:49:34.803776
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    # set up test classes
    hw = HPUXHardware({'module_setup': True, 'gather_subset': ['all']}, None)
    facts = {'ansible_architecture': '9000/785'}
    rc, out, err = hw.module.run_command.return_value = (0, '0', '')

    # run test
    cpu_facts = hw.get_cpu_facts(facts)
    hw.module.run_command.assert_called_with('ioscan -FkCprocessor | wc -l', use_unsafe_shell=True)
    assert cpu_facts == {'processor_count': 0}



# Generated at 2022-06-13 00:49:41.741191
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    module = FakeAnsibleModule()
    hardware = HPUXHardware(module, None)
    hw_facts = hardware.get_hw_facts()
    assert hw_facts['model'] == 'HP 9000/785'
    assert hw_facts['product_serial'] == '123456789'
    assert hw_facts['firmware_version'] == '11.18'



# Generated at 2022-06-13 00:49:52.118198
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    module = AnsibleModule(
        argument_spec=dict(
            filter=dict(default='', required=False),
        ),
        supports_check_mode=False
    )

    fake_module = FakeAnsibleModule({})
    fake_module.run_command = MagicMock()
    fake_module.run_command.return_value = (0, "", "")

    hw = HPUXHardware(fake_module)
    hw.module = fake_module
    hw.get_memory_facts()

    assert hw.memtotal_mb is not None
    assert hw.swaptotal_mb is not None
    assert hw.swapfree_mb is not None
    assert hw.memfree_mb is not None



# Generated at 2022-06-13 00:49:53.806605
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    """
    Syntax: HPUXHardwareCollector().collect()
    """
    assert HPUXHardwareCollector()

# Generated at 2022-06-13 00:49:57.527591
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    # Setup a basic class
    module = AnsibleModule(argument_spec={})
    set_module_args(dict(gather_subset='!all'))
    my_obj = HPUXHardware(module)

    # Populate the facts
    facts = my_obj.populate()

    # processor_cores should be at least 1
    assert int(facts['processor_cores']) >= 1

    # processor_count can't be higher than the highest CPU ID
    assert int(facts['processor_count']) <= 32


# Generated at 2022-06-13 00:50:08.222081
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    flexmock(HPUXHardware)

# Generated at 2022-06-13 00:50:12.912810
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    module = MockModule()
    harware_collector = HPUXHardwareCollector(module=module)

    assert harware_collector.__class__.__name__ == 'HardwareCollector'
    assert harware_collector._fact_class == HPUXHardware
    assert harware_collector.required_facts == set(['platform', 'distribution'])



# Generated at 2022-06-13 00:50:18.763499
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    hardware = HPUXHardware(None)
    assert hardware.get_hw_facts({'ansible_architecture': 'ia64',
                                  'ansible_distribution_version': 'B.11.23'}) == {'model': 'ia64 hp server rx2600',
                                                                                  'firmware_version': 'v1.70 (12/14/2009)'}



# Generated at 2022-06-13 00:50:59.948237
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec={})
    hardware = HPUXHardware(module=module)
    facts = hardware.populate({'ansible_architecture': '9000/800'})
    assert facts['processor'] == 'HP-PA RISC'
    assert facts['processor_count'] == 2
    assert facts['processor_cores'] == 2
    assert facts['processor_threads_per_core'] == 2
    assert facts['processor_vcpus'] == 4
    facts = hardware.populate({'ansible_architecture': 'ia64'})
    assert facts['processor'] == 'Intel(R) Itanium(R) Processor 9560'
    assert facts['processor_count'] == 8
    assert facts['processor_cores'] == 8
    assert facts['processor_threads_per_core'] == 1

# Generated at 2022-06-13 00:51:09.241328
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    """ Function to test the method get_memory_facts of class HPUXHardware
    """
    hpux_hw_facts = HPUXHardware()
    # test memtotal_mb
    assert hpux_hw_facts.populate()["ansible_facts"]["memtotal_mb"] == 512
    # test memfree_mb
    assert hpux_hw_facts.populate()["ansible_facts"]["memfree_mb"] == 2
    # test swaptotal_mb
    assert hpux_hw_facts.populate()["ansible_facts"]["swaptotal_mb"] == 4
    # test swapfree_mb
    assert hpux_hw_facts.populate()["ansible_facts"]["swapfree_mb"] == 4
    # test processor_count

# Generated at 2022-06-13 00:51:10.983601
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hardware_collector = HPUXHardwareCollector()
    # Check if the object of HPUXHardwareCollector class is
    # instance of HarwareCollector base class
    assert isinstance(hardware_collector, HardwareCollector)

# Generated at 2022-06-13 00:51:15.904816
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    module = AnsibleModule(argument_spec={})
    hardware = HP9000Hardware()
    hardware.module = module
    hardware.populate()
    marker = '#ansible-hpux-hardware-get-memory-facts-end-marker'
    for line in hardware.get_memory_facts().read().splitlines():
        if line == marker:
            break
        print(line)



# Generated at 2022-06-13 00:51:23.529050
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    hardware = HPUXHardware()

    import ansible.module_utils.facts.hardware.hpux
    from ansible.module_utils.facts.hardware.hpux import HPUXHardware
    hardware_result = hardware.populate()
    ansible_hpux_dir = os.path.dirname(ansible.module_utils.facts.hardware.hpux.__file__)
    with open(os.path.join(ansible_hpux_dir, 'hpux_module.out')) as hpux_hardware_file:
        hpux_hardware_result = eval(hpux_hardware_file.read())
    assert hardware_result == hpux_hardware_result

# Generated at 2022-06-13 00:51:28.745919
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    # set up mock values for testing
    # Note that memtotal_mb is too large for a real HP-UX server
    memtotal_mb = 1234
    memfree_mb = 123
    swaptotal_mb = 456
    swapfree_mb = 45
    # String returned by vmstat when a server doesn't have swap configured
    vmstat_nomem = "  0  1234  1234  456  45"
    # String returned by vmstat when a server has swap configured
    vmstat_mem = "  0  500  500  500  450"
    module.run_command = mock.Mock(return_value=(0, vmstat_mem, None))

# Generated at 2022-06-13 00:51:33.478652
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    params = {'ANSIBLE_MODULE_ARGS': {'fact_path': '/etc/ansible/facts.d', 'gather_subset': 'all', 'gather_timeout': 10}}
    collected_facts = dict()
    collected_facts['ansible_architecture'] = 'ia64'
    collected_facts['ansible_distribution_version'] = 'B.11.31'
    module = FakeModule(params=params, collected_facts=collected_facts)

    hpx = HPUXHardware(module)
    hw_facts = hpx.get_hw_facts()
    assert hw_facts['firmware_version'] == '2015.09.08.15.17'
    assert hw_facts['model'] == 'ia64'

# Generated at 2022-06-13 00:51:37.468862
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hardware_collector = HPUXHardwareCollector()
    assert hardware_collector._fact_class == HPUXHardware
    assert hardware_collector._platform == 'HP-UX'
    assert hardware_collector.required_facts == set(['platform','distribution'])

# Generated at 2022-06-13 00:51:42.140779
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    config2 = dict(set(), required_facts=['ansible_distribution'], optional_facts=[])
    config = dict(set(), required_facts=['ansible_distribution'], optional_facts=[])
    hpuxhardware = HPUXHardwareCollector(config2)
    config = hpuxhardware.config
    assert config.required_facts == set(['ansible_distribution'])

# Generated at 2022-06-13 00:51:44.494217
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    hardware = HPUXHardware(dict(platform='HP-UX', ansible_architecture='9000/800'))
    cpu_facts = hardware.get_cpu_facts()

    assert cpu_facts['processor_count'] == 1
    assert cpu_facts['processor_cores'] == 1
    assert cpu_facts['processor'] == 'PA-RISC'


# Generated at 2022-06-13 00:53:04.963692
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    hpuxtest = HPUXHardware()
    page_size = 4096
    # Test on a HP-UX 9000/800 architecture
    collected_facts = {'ansible_architecture': '9000/800', 'ansible_distribution': 'hp-ux'}
    test_in = 'kthr   memory            page              faults      cpu\n' \
              '----- ----------- ------------------------ ------------ -----------\n' \
              'r  b   avm   fre  re  at    pi  po  fr   sr  cy  in   sy  cs us sy id wa\n' \
              '0  0  1554  519  0  0   0   0   0   0  28  71   0   4   6  0  0 100  0'

# Generated at 2022-06-13 00:53:12.734380
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    hw = HPUXHardware()
    hw.module.run_command = lambda x, y=None: (0, "", "")
    results = hw.get_cpu_facts()
    assert results['processor'] == 'Intel Itanium2 processor'
    assert results['processor_cores'] == 2
    assert results['processor_count'] == 1
    hw.module.run_command = lambda x, y=None: (0, "", "")
    results = hw.get_memory_facts()
    assert results['memfree_mb'] == 256
    assert results['memtotal_mb'] == 1024
    assert results['swapfree_mb'] == 0
    assert results['swaptotal_mb'] == 0
    hw.module.run_command = lambda x, y=None: (0, "", "")


# Generated at 2022-06-13 00:53:22.418443
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec=dict(
        ansible_facts=dict(required=False, type='dict'),
        collected_facts=dict(required=False, type='dict'),
    ))

    set_module_args(dict(collected_facts=dict(ansible_distribution_version="B.11.31")))
    m = HPUXHardware(module=module)
    data = m.get_cpu_facts()
    assert data['processor_count'] == 16
    assert data['processor_cores'] == 8
    assert data['processor'] == "Intel(R) Xeon(R) CPU E5-2640 v3 @ 2.60GHz"

    set_module_args(dict(collected_facts=dict(ansible_distribution_version="B.11.23")))
    m = HPUX

# Generated at 2022-06-13 00:53:27.516965
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hpux_hw_collector = HPUXHardwareCollector()
    assert isinstance(hpux_hw_collector, HPUXHardwareCollector)
    assert hpux_hw_collector.platform == 'HP-UX'
    assert hpux_hw_collector.required_facts == set(['platform', 'distribution'])


# Generated at 2022-06-13 00:53:33.856299
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    hardware = HPUXHardware({'module': None, 'gather_subset': ['!all', '!min']})
    result = hardware.get_memory_facts({'ansible_architecture': '9000/800'})
    assert result.get('memfree_mb') == 2048
    assert result.get('swaptotal_mb') == 32768
    assert result.get('swapfree_mb') == 16384
    assert result.get('memtotal_mb') == 8192
    result = hardware.get_memory_facts({'ansible_architecture': 'ia64'})
    assert result.get('memfree_mb') == 2048
    assert result.get('swaptotal_mb') == 65408
    assert result.get('swapfree_mb') == 16384

# Generated at 2022-06-13 00:53:38.354377
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    hw = HPUXHardware({'module_setup': True, 'gather_subset': ['all']})
    hw_facts = hw.get_hw_facts()
    assert hw_facts['product_serial'] is not None
    assert hw_facts['firmware_version'] is not None
    assert hw_facts['model'] is not None

# Generated at 2022-06-13 00:53:45.530749
# Unit test for method get_memory_facts of class HPUXHardware

# Generated at 2022-06-13 00:53:57.358920
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    cpu_facts = HPUXHardware().get_cpu_facts(collected_facts={'ansible_architecture': 'ia64',
                                                             'ansible_distribution_version': 'B.11.23'})
    assert cpu_facts['processor_count'] == 1
    assert cpu_facts['processor'] == 'Intel(R) Itanium(R) 9500 series processor @ 1.73GHz'
    assert cpu_facts['processor_cores'] == 1

    cpu_facts = HPUXHardware().get_cpu_facts(collected_facts={'ansible_architecture': 'ia64',
                                                             'ansible_distribution_version': 'B.11.31'})
    assert cpu_facts['processor_count'] == 2

# Generated at 2022-06-13 00:54:02.968831
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    module = AnsibleModule(
        argument_spec={
            'gather_subset': dict(default=['!all'], type='list'),
        },
    )
    obj = HPUXHardware(module)
    memory_facts = obj.get_memory_facts()

    assert isinstance(memory_facts.get('memtotal_mb'), int)
    assert isinstance(memory_facts.get('memfree_mb'), int)
    assert isinstance(memory_facts.get('swaptotal_mb'), int)
    assert isinstance(memory_facts.get('swapfree_mb'), int)


# Generated at 2022-06-13 00:54:12.910951
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    module = FakeModule()
    hardware = HPUXHardware(module)
    hardware.populate()

    assert hardware.facts['processor_count'] == 12
    assert hardware.facts['processor'] == 'Intel(R) Itanium(R) Processor 9320'
    assert hardware.facts['memtotal_mb'] == 32768
    assert hardware.facts['memfree_mb'] == 4
    assert hardware.facts['processor_cores'] == 12
    assert hardware.facts['firmware_version'] == 'Firmware revision: v2.23'
    assert hardware.facts['product_serial'] == 'Machine serial number: USER11110UM5'
    assert hardware.facts['swaptotal_mb'] == 1031
    assert hardware.facts['swapfree_mb'] == 231
