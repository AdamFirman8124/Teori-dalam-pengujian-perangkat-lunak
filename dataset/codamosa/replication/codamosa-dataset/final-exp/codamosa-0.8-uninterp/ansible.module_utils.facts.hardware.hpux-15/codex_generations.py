

# Generated at 2022-06-13 00:45:28.012591
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    test_HPUXHardware = HPUXHardware()
    memory_facts = test_HPUXHardware.get_memory_facts()
    assert memory_facts['memfree_mb'] >= 0
    assert memory_facts['memtotal_mb'] >= 0
    assert memory_facts['swaptotal_mb'] >= 0
    assert memory_facts['swapfree_mb'] >= 0

# Generated at 2022-06-13 00:45:36.173473
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    module = AnsibleModule(
        argument_spec=dict(),
    )
    hardware = HPUXHardware(module=module)
    module.run_command = MagicMock(return_value=(0, 'HP 9000/785 xxxxxx', ''))
    hardware.get_hw_facts = method_type(test_HPUXHardware_get_hw_facts, hardware, HPUXHardware)
    module.run_command = MagicMock(return_value=(0, '    Firmware revision = B.11.23\n' +
                                                     '    Firmware Revision = B.11.23\n' +
                                                     'Machine serial number = FOOOOOOO', ''))
    hardware.get_hw_facts = method_type(test_HPUXHardware_get_hw_facts, hardware, HPUXHardware)
    facts

# Generated at 2022-06-13 00:45:45.604781
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hpux_hc = HPUXHardwareCollector()
    assert hpux_hc.platform == 'HP-UX'
    assert hpux_hc.fact_class._platform == 'HP-UX'
    assert hpux_hc.fact_class._fact_class == HPUXHardware._fact_class
    assert hpux_hc.required_facts == hpux_hc.fact_class.required_facts
    assert hpux_hc.fact_class.required_facts == {'platform', 'distribution'}

# Generated at 2022-06-13 00:45:51.115900
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    out = dict(ansible_architecture='ia64', ansible_distribution_version='B.11.23')
    hardware_obj = HPUXHardware(module=dict(), collected_facts=out)
    assert hardware_obj.get_hw_facts() == dict(firmware_version=';_17.16.03_;', model='ia64 hp server rx2660 base')


# Generated at 2022-06-13 00:45:51.740939
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    pass

# Generated at 2022-06-13 00:45:57.850538
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    c = HPUXHardware()
    c.module = MockModule()
    c.module.run_command.return_value = (0, "2048\n", "")
    result = c.get_memory_facts()
    assert result['memfree_mb'] == 20
    assert result['memtotal_mb'] == 0
    assert result['swaptotal_mb'] == 0
    assert result['swapfree_mb'] == 0



# Generated at 2022-06-13 00:46:00.684554
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    assert HPUXHardwareCollector._platform == 'HP-UX'
    assert HPUXHardwareCollector.required_facts == {'platform', 'distribution'}

# Generated at 2022-06-13 00:46:04.414741
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    obj = HPUXHardwareCollector()
    assert obj._fact_class == HPUXHardware
    assert obj._platform == 'HP-UX'
    assert obj.required_facts == set(['platform', 'distribution'])

# Generated at 2022-06-13 00:46:07.097445
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    test_instance = HPUXHardwareCollector()

    assert isinstance(test_instance, HardwareCollector)
    assert isinstance(test_instance._fact_class, HPUXHardware)

# Generated at 2022-06-13 00:46:09.082010
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    """Test constructor for HPUXHardwareCollector."""
    hardware_collector_object = HPUXHardwareCollector()
    assert hardware_collector_object.facts is None
    assert hardware_collector_object._fact_class._platform is None


# Generated at 2022-06-13 00:46:26.739771
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    #
    # Test with two processors
    #
    cpu_facts = HPUXHardware.get_cpu_facts({'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.31'})
    assert cpu_facts['processor_count'] == 2
    assert cpu_facts['processor_cores'] == 1
    #
    # Test with one processor
    #
    cpu_facts = HPUXHardware.get_cpu_facts({'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.23'})
    assert cpu_facts['processor_count'] == 1
    assert cpu_facts['processor_cores'] == 1
    #
    # Test with one processor and hyperthreading
    #

# Generated at 2022-06-13 00:46:36.856872
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    module = AnsibleModuleMock()
    hardware = HPUXHardware(module)
    collected_facts = dict(ansible_architecture='9000/800', ansible_distribution_version='B.11.23')
    cpu_facts = hardware.get_cpu_facts(collected_facts=collected_facts)
    assert cpu_facts['processor_count'] == 2, "HP-UX-hardware test case for method get_cpu_facts failed"
    collected_facts = dict(ansible_architecture='ia64', ansible_distribution_version='B.11.23')
    cpu_facts = hardware.get_cpu_facts(collected_facts=collected_facts)
    assert cpu_facts['processor_count'] == 2, "HP-UX-hardware test case for method get_cpu_facts failed"


# Generated at 2022-06-13 00:46:47.533965
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    import json
    import sys
    from ansible.module_utils.facts.hardware.hpux import HPUXHardware

    if sys.version_info[0] == 2:
        from StringIO import StringIO
    else:
        from io import StringIO

    if sys.version_info[0] < 3:
        open_mock = None
        builtin_open = '__builtin__.open'
    else:
        open_mock = None
        builtin_open = 'builtins.open'
    hpuxhardware = HPUXHardware(dict(ANSIBLE_MODULE_ARGS={'gather_subset': '!all,!min', 'gather_timeout': 10},
                                     ANSIBLE_MODULE_CONSTANTS={}))

    # Testing '9000/800'
    hp

# Generated at 2022-06-13 00:46:57.638624
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    '''
    Unit test for method get_hw_facts of class HPUXHardware
    '''
    mod_args = {
        'ansible_system_vendor': 'HP',  # needed to load this module
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.31'}
    hw_facts = {}

    fixture_path = os.path.join(os.path.dirname(__file__),
                                'fixtures',
                                'HPUXHardware_get_hw_facts.txt')
    with open(fixture_path, 'r') as fixture_file:
        fixture_data = fixture_file.read()

    hw = HPUXHardware(module=None, params=mod_args)
    hw.get_hw_

# Generated at 2022-06-13 00:47:01.585972
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    module = DummyModule()
    hw = HPUXHardware(module=module)
    facts = hw.populate()
    assert 'memtotal_mb' in facts
    assert 'memfree_mb' in facts
    assert 'swaptotal_mb' in facts
    assert 'swapfree_mb' in facts
    assert 'processor' in facts
    assert 'processor_count' in facts
    assert 'processor_cores' in facts
    assert 'model' in facts
    assert 'firmware' in facts

# Generated at 2022-06-13 00:47:11.421203
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    """Test method get_cpu_facts of class HPUXHardware"""
    module = AnsibleModule(
        argument_spec=dict()
    )
    module.mock_command('/usr/contrib/bin/machinfo', stdout=HPUX_MACHINFO_COMMAND_B11311_THREADS_ON)
    hardware_facts = HPUXHardware(module).populate()
    assert hardware_facts.get('processor_count') == 2
    assert hardware_facts.get('processor_cores') == 10
    assert hardware_facts.get('processor') == 'Intel(R) Xeon(R) CPU E5-2660 v2 @ 2.20GHz'


# Generated at 2022-06-13 00:47:14.273394
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hpux_hw_collector = HPUXHardwareCollector()
    assert hpux_hw_collector._fact_class is not None
    assert hpux_hw_collector._platform == 'HP-UX'



# Generated at 2022-06-13 00:47:18.642147
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    module = AnsibleModule(argument_spec={})
    hw = HPUXHardware(module)
    collected_facts = {'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.23'}
    hw.get_hw_facts(collected_facts)
    assert hw.model == 'ia64 hp machine'
    assert hw.firmware_version == 'P89 v2.04'


# Generated at 2022-06-13 00:47:21.228078
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    HardwareCollector.platforms['HP-UX'] = HPUXHardwareCollector
    hpux_hardware_collector = HardwareCollector("HP-UX", 'B.11.31', 'ia64')
    assert hpux_hardware_collector

# Class for unit test

# Generated at 2022-06-13 00:47:25.604904
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hw_collector = HPUXHardwareCollector()
    # Assert that the class attribute for fact class is set correctly
    assert hw_collector._fact_class == HPUXHardware
    # Assert that the class attribute for platform is set correctly
    assert hw_collector._platform == 'HP-UX'
    # Assert that the set of required facts is set correctly
    assert hw_collector.required_facts == set(['platform', 'distribution'])

# Generated at 2022-06-13 00:47:51.613905
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    hw = HPUXHardware({'module_setup': True}, {'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.23'})

    hw.module.run_command = lambda *args, **kwargs: (1, None, None)

    mem_facts = hw.get_memory_facts()
    assert mem_facts == {'memfree_mb': 0, 'memtotal_mb': 0, 'swapfree_mb': 0,
                         'swaptotal_mb': 0}, "Bad memory facts: %s" % mem_facts

# Generated at 2022-06-13 00:47:54.472278
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    h = HPUXHardware()
    collected_facts = {}
    result = h.get_memory_facts(collected_facts=collected_facts)



# Generated at 2022-06-13 00:48:02.842628
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    # Test of populate on HP-UX B.11.31
    module = MockModule(platform='HP-UX', distribution='HP-UX', distribution_version='B.11.31')
    hardware = HPUXHardware(module=module)

    # Test of populate on HP-UX B.11.23
    module = MockModule(platform='HP-UX', distribution='HP-UX', distribution_version='B.11.23')
    hardware = HPUXHardware(module=module)

    # Test of populate on HP-UX 9000/800
    module = MockModule(platform='HP-UX', ansible_architecture='9000/800')
    hardware = HPUXHardware(module=module)

    # Test of populate on HP-UX 9000/785

# Generated at 2022-06-13 00:48:08.006803
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    f = HPUXHardware(dict())
    facts = {'ansible_architecture': '9000/800'}
    result = f.get_memory_facts(facts)
    assert result['memfree_mb'] == 1279
    assert result['memtotal_mb'] == 1024
    assert result['swaptotal_mb'] == 3824
    assert result['swapfree_mb'] == 3299


# Generated at 2022-06-13 00:48:18.010266
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    Hw = HPUXHardware(None)
    collected_facts={}
    collected_facts['ansible_architecture'] = 'ia64'
    collected_facts['ansible_distribution_version'] = 'B.11.31'
    assert Hw.get_memory_facts(collected_facts) == {'memfree_mb': 8060, 'memtotal_mb': 9968, 'swapfree_mb': 0, 'swaptotal_mb': 0}
    collected_facts['ansible_architecture'] = '9000/785'
    collected_facts['ansible_distribution_version'] = 'B.11.31'

# Generated at 2022-06-13 00:48:21.397437
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    fact_class = HPUXHardwareCollector(None)
    assert fact_class.required_facts == set(['platform', 'distribution'])
    assert fact_class._platform == 'HP-UX'
    assert fact_class._fact_class == HPUXHardware



# Generated at 2022-06-13 00:48:28.574949
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    # Prepare test parameters
    module_mock = Mock()

    # Prepare test class
    hpux_hw = HPUXHardware(module_mock)

    # Prepare test return values
    rc_get_hw_facts = 0
    out_get_hw_facts = "9000/800"
    err_get_hw_facts = ""

    module_mock.run_command.side_effect = [
        (rc_get_hw_facts, out_get_hw_facts, err_get_hw_facts)
    ]

    # Run the get_hw_facts method
    result_get_hw_facts = hpux_hw._get_hw_facts()

    assert result_get_hw_facts == {'model': '9000/800'}

# Generated at 2022-06-13 00:48:37.248602
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec={})
    facts_collector = HPUXHardwareCollector
    cpu_facts = facts_collector._fact_class.get_cpu_facts(facts_collector, collected_facts={'ansible_architecture': '9000/800'})
    assert 'processor_cores' in cpu_facts
    assert 'processor_count' in cpu_facts
    assert 'processor' in cpu_facts

    cpu_facts = facts_collector._fact_class.get_cpu_facts(facts_collector, collected_facts={'ansible_architecture': '9000/785'})
    assert 'processor_cores' in cpu_facts
    assert 'processor_count' in cpu_facts
    assert 'processor' in cpu_facts

    cpu_facts = facts_collector._fact_class

# Generated at 2022-06-13 00:48:46.179179
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    collected_facts = {
        'platform': 'HP-UX',
        'distribution': 'HP-UX',
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.23',
        'ansible_distribution': 'HP-UX',
    }

    hw = HPUXHardwareCollector(collected_facts, None)

    hw_facts = hw.collect()
    assert isinstance(hw_facts, dict)
    assert 'ansible_hw_memtotal_mb' in hw_facts
    assert 'ansible_hw_firmware_version' in hw_facts
    assert 'ansible_hw_processor' in hw_facts
    assert 'ansible_hw_product_serial' in hw_facts

# Generated at 2022-06-13 00:48:59.637967
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    module = AnsibleModule(argument_spec={})
    # Populate fake Ansible facts
    set_module_args(dict(
        ansible_architecture='ia64',
        ansible_distribution_version='B.11.31',
    ))
    from ansible.modules.system import hpux as hpux_module
    hpux_module.run_command = MagicMock(return_value=(0, '', ''))
    hpux_module.os = MagicMock()
    hpux_module.os.access = MagicMock(return_value=True)

# Generated at 2022-06-13 00:49:15.967111
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    hw = HPUXHardware()
    memory_facts = hw.get_memory_facts({})
    assert memory_facts['memfree_mb'] > 0
    assert memory_facts['memtotal_mb'] > 0
    assert memory_facts['swaptotal_mb'] > 0
    assert memory_facts['swapfree_mb'] > 0



# Generated at 2022-06-13 00:49:17.861245
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hc = HPUXHardwareCollector()
    assert hc.required_facts == set(['platform'])

# Generated at 2022-06-13 00:49:28.961740
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    hw = HPUXHardware()
    module = AnsibleModule(argument_spec={})
    hw.module = module
    hw.module.params = {'host': 'testhost'}
    hw.run_command = MagicMock()

    def run_command_mock(cmd):
        return 0, "12345 pages\n", ''

    hw.module.run_command = run_command_mock
    facts = hw.get_memory_facts(collected_facts={'ansible_architecture': 'ia64'})
    module.exit_json(ansible_facts={})
    assert facts['memfree_mb'] == 19
    assert facts['memtotal_mb'] > 0
    assert facts['swaptotal_mb'] > 0
    assert facts['swapfree_mb'] > 0

# Generated at 2022-06-13 00:49:36.766353
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    module = AnsibleModule(
        argument_spec = dict(
            gather_subset=dict(default=['!all'], type='list')
        ),
        supports_check_mode=True
    )

    hardware_obj = HPUXHardware(module=module)
    hardware_obj.populate()
    hardware_obj.get_cpu_facts()
    hardware_obj.get_memory_facts()
    hardware_obj.get_hw_facts()



# Generated at 2022-06-13 00:49:41.100325
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    facts = {}
    facts['ansible_architecture'] = 'ia64'
    facts['ansible_distribution_version'] = 'B.11.23'
    test = HPUXHardware(dict(module=None), facts)
    test.get_memory_facts(facts)

# Generated at 2022-06-13 00:49:44.812078
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    hardware_facts = HPUXHardware()
    result = hardware_facts.get_cpu_facts()
    assert 'processor_count' in result
    assert 'processor_cores' in result
    assert 'processor' in result

# Generated at 2022-06-13 00:49:55.300146
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    hardware = HPUXHardware({})
    collected_facts = {'ansible_facts': {'ansible_architecture': 'ia64',
                                         'ansible_distribution_version': 'B.11.23'},
                       'changed': False}
    hw_facts = hardware.get_hw_facts(collected_facts=collected_facts)
    assert hw_facts == {'model': 'ia64 hp server rx3600', 'firmware_version': '11.23'}
    collected_facts = {'ansible_facts': {'ansible_architecture': 'ia64',
                                         'ansible_distribution_version': 'B.11.31'},
                       'changed': False}

# Generated at 2022-06-13 00:50:00.318792
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    collected_facts = dict(ansible_architecture="9000/785")
    hardware = HPUXHardware(module=dict())

# Generated at 2022-06-13 00:50:10.547458
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    def run_run_command(self, cmd, check_rc=True, close_fds=True, executable=None,
                        data=None, binary_data=False, path_prefix=None, cwd=None,
                        use_unsafe_shell=False, prompt_regex=None, environ_update=None,
                        umask=None, encoding=None, errors='surrogate_then_replace'):
        if cmd == "uname -p":
            return 0, "ia64", ""

# Generated at 2022-06-13 00:50:18.861659
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    hw_fact = HPUXHardware
    hw_fact.module = type('', (), {})()
    hw_fact.module.run_command = lambda command, **kwargs: (0, ' model      : rp7410', None)
    hw_fact.get_hw_facts = lambda **kwargs: hw_fact.get_hw_facts(**kwargs)
    hw_facts = hw_fact.get_hw_facts()
    assert hw_facts['model'] == 'rp7410'

    hw_fact.module.run_command = lambda command, **kwargs: (0, ' model      : rp7410\nBMC Firmware Revision = 1.60', None)
    hw_fact.get_hw_facts = lambda **kwargs: hw_fact.get_hw

# Generated at 2022-06-13 00:50:50.042217
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    module = type('', (), {})()

    # Add attributes to module
    def run_command(command):
        if command == "model":
            out = "Super model"
        elif command == "/usr/contrib/bin/machinfo |grep -i 'Firmware revision' | grep -v BMC":
            out = "Firmware revision: G1234"
        elif command == "/usr/contrib/bin/machinfo |grep -i 'Machine serial number' ":
            out = "Machine serial number: K1234"
        return 0, out, ''
    module.run_command = run_command

    # Add attributes to platform
    platform = type('', (), {})()
    platform.system = lambda: 'HP-UX'
    platform.dist = lambda: ['HP-UX']

# Generated at 2022-06-13 00:50:52.498323
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    fact = HPUXHardware()
    assert fact.get_memory_facts() == {'memtotal_mb': 32768, 'memfree_mb': 32278, 'swapfree_mb': 49152, 'swaptotal_mb': 49152}

# Generated at 2022-06-13 00:50:58.362877
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    module = AnsibleModule(argument_spec={})

    facts = {}
    facts['platform'] = 'HP-UX'
    facts['distribution'] = 'B.11.31'
    facts['architecture'] = 'ia64'

    expected = {}
    expected['model'] = 'hp rx2660'
    expected['firmware_version'] = 'B.11.31.0894'
    expected['product_serial'] = '5894327'

    obj = HPUXHardware(module=module, collected_facts=facts)
    result = obj.populate()

    assert type(result) == dict
    assert expected == result


# Generated at 2022-06-13 00:51:03.325219
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    module = AnsibleModule(argument_spec={})
    module.params = {}
    module.params['gather_subset'] = ['all']
    collected_facts = dict(ansible_architecture='ia64',
                           ansible_distribution='HP-UX',
                           ansible_distribution_major_version='11',
                           ansible_distribution_release='B.11.31',
                           ansible_distribution_version='B.11.31')
    hardware_Facts = HPUXHardware(module)
    facts = hardware_Facts.populate(collected_facts=collected_facts)

# Generated at 2022-06-13 00:51:13.540184
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    hpux_hardware = HPUXHardware(None)

    # Test with ia64, B.11.23
    hpux_hardware.get_cpu_facts({'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.23'})

    # Test with ia64 but with bad generated machinfo
    hpux_hardware.get_cpu_facts({'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.31'})

    # Test with 9000/785 and ok generated machinfo
    hpux_hardware.get_cpu_facts({'ansible_architecture': '9000/785', 'ansible_distribution_version': 'B.11.31'})

    # Test with 9000/785 and ok generated machinfo

# Generated at 2022-06-13 00:51:21.369408
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    cap_mem_total = 0
    cap_mem_free = 0
    cap_swap_total = 0
    cap_swap_free = 0
    # this is the object under test
    hw = HPUXHardware()

    hw.collected_facts = {'ansible_architecture': 'ia64'}

    rc, out, err = hw.module.run_command("/usr/contrib/bin/machinfo | grep Memory", use_unsafe_shell=True)
    data = re.search(r'Memory[\ :=]*([0-9]*).*MB.*', out).groups()[0].strip()
    cap_mem_total = int(data)


# Generated at 2022-06-13 00:51:26.759025
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    hpxhw = HPUXHardware({})
    dct = hpxhw.populate({'ansible_architecture': '9000/800', 'ansible_distribution_version': 'B.11.23'})
    assert dct == {'processor': 'Intel Itanium 2 9000 series', 'firmware_version': '4.22', 'processor_count': 4, 'memtotal_mb': 16384, 'processor_cores': 4, 'swaptotal_mb': 16384, 'memfree_mb': 16384, 'swapfree_mb': 16383, 'model': 'HP Server rx2660'}

# Generated at 2022-06-13 00:51:28.731287
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hhc = HPUXHardwareCollector()
    assert hhc.required_facts == set(['platform', 'distribution'])

# Generated at 2022-06-13 00:51:32.173881
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    h = HPUXHardwareCollector()
    assert h.platform == 'HP-UX'
    assert h.required_facts == set(['platform', 'distribution'])
    assert h.fact_class == HPUXHardware



# Generated at 2022-06-13 00:51:35.247401
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    ins = HPUXHardwareCollector()
    assert ins._fact_class == HPUXHardware
    assert ins._platform == 'HP-UX'
    assert ins.required_facts == set(['platform', 'distribution'])

# Generated at 2022-06-13 00:52:03.189508
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hpux = HPUXHardwareCollector()
    assert hpux._fact_class == HPUXHardware
    assert hpux._platform == 'HP-UX'

# Generated at 2022-06-13 00:52:07.966826
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():

    module = AnsibleModule(
        argument_spec=dict(),
    )

    hpux_hw = HPUXHardware(module)

    rc = 0
    out = "X86  ( X86  )"
    err = ""
    hpux_hw._module.run_command = MagicMock(return_value=(rc, out, err))

    hpux_hw.populate()
    assert hpux_hw.model == out.strip()

    rc = 0
    out = "Machine serial number:   XXXXXXX"
    err = ""
    hpux_hw._module.run_command = MagicMock(return_value=(rc, out, err))

    hpux_hw.populate()
    assert hpux_hw.product_serial == out.split(':')[1].strip()

    rc = 0
    out

# Generated at 2022-06-13 00:52:13.634693
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    facts = dict(platform='HP-UX', distribution='HP-UX')
    set_module_args(dict(gather_subset=['all'], filter=['*']))
    hpux_hw_collector = HPUXHardwareCollector(module=AnsibleModule(
        argument_spec=dict()
    ), facts=facts)
    assert hpux_hw_collector.platform == 'HP-UX'

# Generated at 2022-06-13 00:52:17.694788
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    module = AnsibleModule(argument_spec=dict())
    hardware = HPUXHardware(module=module)
    memory_facts = hardware.get_memory_facts()
    assert memory_facts['memfree_mb']
    assert memory_facts['memtotal_mb']
    assert memory_facts['swaptotal_mb']
    assert memory_facts['swapfree_mb']



# Generated at 2022-06-13 00:52:26.921556
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    module = AnsibleModule(argument_spec={})
    hardware_facts_instance = HPUXHardware(module)
    hardware_facts_instance.module.run_command = MagicMock(
        return_value=(0, ' ', ''))
    hardware_facts_instance.collect_platform_subset_facts = MagicMock(
        return_value={'ansible_architecture': '9000/800'})
    hardware_facts_instance.get_memory_facts()

    # Test case when machine is PA-RISC
    hardware_facts_instance.collect_platform_subset_facts = MagicMock(
        return_value={'ansible_architecture': '9000/785'})
    hardware_facts_instance.get_memory_facts()

    # Test case when machine is Itanium

# Generated at 2022-06-13 00:52:30.711583
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hw_facts = HPUXHardwareCollector()
    assert hw_facts._platform == "HP-UX"
    assert hw_facts._fact_class == HPUXHardware

# Generated at 2022-06-13 00:52:36.562660
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    cpu_facts = HPUXHardware.get_cpu_facts(None, {'ansible_architecture': '9000/800'})
    assert cpu_facts['processor_count'] == 2
    cpu_facts = HPUXHardware.get_cpu_facts(None, {'ansible_architecture': 'ia64'})
    assert cpu_facts['processor_count'] == 2
    assert cpu_facts['processor_cores'] == 2
    assert cpu_facts['processor'] == 'Intel(R) Itanium(R) Processor'

# Generated at 2022-06-13 00:52:45.155807
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    collected_facts = {
        'platform': 'HP-UX',
        'distribution': 'HP-UX',
        'ansible_distribution': 'HP-UX',
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.31'
    }
    hardware = HPUXHardware()
    cpu_facts = hardware.get_cpu_facts(collected_facts=collected_facts)
    assert cpu_facts.get('processor_cores') == 1

# Generated at 2022-06-13 00:52:50.427317
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    fake_module = DummyAnsibleModule()
    hpux_system = HPUXHardware(module=fake_module)
    facts = hpux_system.get_hw_facts()

    assert facts['model'] == "IA64 hp server rx4610"
    assert facts['firmware_version'] == "v2.00"
    assert facts['product_serial'] == "MXU81101U0"


# Generated at 2022-06-13 00:52:56.687446
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    """Unit tests for 'ansible.module_utils.facts.hardware.hpux.HPUXHardware.get_memory_facts'."""
    result = {"memfree_mb": 16, "memtotal_mb": 32, "swaptotal_mb": 16, "swapfree_mb": 16}
    assert HPUXHardware().get_memory_facts() == result

# Generated at 2022-06-13 00:54:02.827208
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    module = FakeAnsibleModule()
    module.run_command = FakeRunCommand()
    facts = HPUXHardware(module).get_memory_facts()
    if not isinstance(facts, dict):
        raise Exception("get_memory_facts return value is not a dict")
    for fact in ['memfree_mb', 'memtotal_mb', 'swapfree_mb', 'swaptotal_mb']:
        if fact not in facts:
            raise Exception("get_memory_facts did not return fact %s" % fact)
        if not isinstance(facts[fact], int):
            raise Exception("fact %s is not an int" % fact)



# Generated at 2022-06-13 00:54:13.124533
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    data = {"ansible_architecture": "9000/800", "ansible_distribution_version": "B.11.31"}
    check_data = {"processor_count": 2, "processor_cores": 2, "processor": "Intel(R) Itanium(R) Processor 9215"}
    h = HPUXHardware()
    assert check_data == h.get_cpu_facts(data)

    data = {"ansible_architecture": "9000/800", "ansible_distribution_version": "B.11.23"}
    check_data = {"processor_count": 2, "processor": "Intel(R) Itanium(R) Processor 9140", "processor_cores": 2}
    assert check_data == h.get_cpu_facts(data)


# Generated at 2022-06-13 00:54:15.092419
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hardware = HPUXHardwareCollector()
    assert hardware._fact_class == HPUXHardware
    assert hardware._platform == 'HP-UX'
    assert hardware.required_facts == set(['platform', 'distribution'])

# Generated at 2022-06-13 00:54:20.100607
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hardware_collector_obj = HPUXHardwareCollector()
    assert hardware_collector_obj.required_facts == set(['platform', 'distribution'])
    assert hardware_collector_obj.platform == 'HP-UX'
    assert isinstance(hardware_collector_obj._fact_class, HPUXHardware)


# Generated at 2022-06-13 00:54:27.538752
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    """
    Unit test of get_memory_facts of class HPUXHardware
    """

    class MockModule(object):
        def __init__(self):
            self.run_command = Mock(return_value=('command_rc', 'command_out', 'command_err'))
            self.params = {}

        def fail_json(self, *args, **kwargs):
            pass

    class MockFacts(object):
        def __init__(self):
            self.facts = {}

        def __call__(self):
            return self.facts

    mock_module = MockModule()
    mock_facts = MockFacts()

    # test case 1
    mock_facts.facts = {'ansible_architecture': 'ia64'}
    hardware = HPUXHardware(mock_module, mock_facts)

# Generated at 2022-06-13 00:54:31.191347
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    hw = HPUXHardware()
    facts = hw.get_hw_facts()
    assert facts == {'model': 'B132L', 'firmware_version': 'hpl_hpi_v.4.4.4.4 060321 (01/15/07)', 'product_serial': 'US123456789'}

# Generated at 2022-06-13 00:54:39.568310
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    test_class = HPUXHardware({})
    test_case = {'ansible_architecture': '9000/800'}
    result = test_class.get_cpu_facts(collected_facts=test_case)
    assert result == {'processor_count': 1}

    test_case = {'ansible_architecture': '9000/785'}
    result = test_class.get_cpu_facts(collected_facts=test_case)
    assert result == {'processor_count': 2}

    test_case = {'ansible_architecture': 'ia64'}
    test_case2 = {'ansible_distribution_version': 'B.11.23'}
    result = test_class.get_cpu_facts(collected_facts=test_case)
    assert result

# Generated at 2022-06-13 00:54:49.142500
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    module = AnsibleModule(
        argument_spec=dict(
            ansible_architecture='ia64',
            ansible_distribution_version='B.11.23'
        )
    )
    hpux_hw = HPUXHardware(module)
    cpu_facts = hpux_hw.get_cpu_facts()
    assert isinstance(cpu_facts, dict)
    assert cpu_facts['processor_count'] == 4
    assert cpu_facts['processor'] == 'Intel(R) Itanium 2 9100 series CPU @ 1.60GHz'
    assert cpu_facts['processor_cores'] == 2

# Generated at 2022-06-13 00:54:51.354863
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hardware_collector = HPUXHardwareCollector()
    assert hardware_collector.required_facts == set(['platform', 'distribution'])


# Generated at 2022-06-13 00:54:59.687883
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    """
    Unit test for method get_memory_facts of class HPUXHardware

    :return:
    """
    this_module = AnsibleModule(argument_spec={})
    this_HPUXHardware = HPUXHardware(module=this_module)

    return_value = this_HPUXHardware.get_memory_facts()
    assert return_value['swaptotal_mb'] == 896
    assert return_value['memtotal_mb'] == 2046
    assert return_value['memfree_mb'] == 383
    assert return_value['swapfree_mb'] == 896