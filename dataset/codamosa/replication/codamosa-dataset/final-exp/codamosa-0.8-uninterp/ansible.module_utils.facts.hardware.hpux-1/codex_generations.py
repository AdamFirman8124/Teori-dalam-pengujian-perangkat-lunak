

# Generated at 2022-06-13 00:45:31.445237
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    module = AnsibleModule(
        argument_spec={}
    )
    collected_facts = {'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.31'}
    memory_facts = HPUXHardware().get_memory_facts(collected_facts)
    assert memory_facts['swapfree_mb'] >= 0
    assert memory_facts['swaptotal_mb'] >= 0
    assert memory_facts['memfree_mb'] >= 0
    assert memory_facts['memtotal_mb'] >= 0


# Generated at 2022-06-13 00:45:38.305957
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    data = "\
        model 900/785\n\
        Firmware revision = OE.11.31.2144\n\
        Machine serial number = US123456789\n"
    hw_object = HPUXHardware()
    hw_object.module.run_command = run_command_mock
    result = hw_object.get_hw_facts()

    assert result.get('model') == '900/785'
    assert result.get('firmware_version') == 'OE.11.31.2144'
    assert result.get('product_serial') == 'US123456789'

    data = "        model 9000/800\n\
        Firmware revision = OE.11.31.2144\n"
    hw_object = HPUXHardware()

# Generated at 2022-06-13 00:45:46.727558
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    from ansible.module_utils.facts.hardware.hpu import HPUXHardware
    memory_facts_module = HPUXHardware(module=None)
    memory_facts = memory_facts_module.get_memory_facts()
    assert 'memtotal_mb' in memory_facts
    assert 'memfree_mb' in memory_facts
    assert 'swapfree_mb' in memory_facts
    assert 'swaptotal_mb' in memory_facts


# Generated at 2022-06-13 00:45:47.786056
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    x = HPUXHardwareCollector()

# Generated at 2022-06-13 00:45:49.884860
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    facts = {}
    hardware_collector = HPUXHardwareCollector()
    hardware_collector.get_facts(facts, {}, {}, None)

# Generated at 2022-06-13 00:45:56.505746
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    # Set values for testing
    MODEL_VALUE = 'hp 9000/785/C3000'
    FIRMWARE_VALUE = '5.6'
    PRODUCT_SERIAL_VALUE = 'ABC-1234567890'
    COLLECTED_FACTS = {
        'ansible_distribution': 'HP-UX',
        'ansible_distribution_version': 'B.11.31',
        'ansible_architecture': 'ia64',
        'platform': 'HP-UX'
    }

    # Init HPUXHardware object
    hpux_hardware = HPUXHardware(None)

    # Get result from method get_hw_facts of class HPUXHardware
    result = hpux_hardware.get_hw_facts(COLLECTED_FACTS)

    # Test result

# Generated at 2022-06-13 00:46:04.194695
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    # Set of return code, output, and error for method get_cpu_facts
    data = {'ansible_architecture': 'ia64',
            'ansible_distribution_version': 'B.11.23'}
    rc = 0
    out = "4"
    err = ""
    # Create mock for method run_command
    def run_command(self, cmd, use_unsafe_shell=False):
        return (rc, out, err)
    # Create mock for method get_cpu_facts with data, rc, out and err defined previously
    hardware_facts = HPUXHardware()
    hardware_facts.run_command = run_command
    hardware_facts.module.run_command = run_command
    # Get cpu_facts

# Generated at 2022-06-13 00:46:13.069912
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    module = AnsibleModuleStub({
    })
    hardware_obj = HPUXHardware(module)
    collected_facts = {'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.23'}
    hardware_facts = hardware_obj.populate(collected_facts)

    assert hardware_facts['processor_count']
    assert hardware_facts['processor']
    assert hardware_facts['processor_cores']
    assert hardware_facts['memfree_mb']
    assert hardware_facts['memtotal_mb']
    assert hardware_facts['swaptotal_mb']
    assert hardware_facts['swapfree_mb']
    assert hardware_facts['model']
    assert hardware_facts['firmware_version']


# Generated at 2022-06-13 00:46:21.993623
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    facts = dict(
        distribution=dict(
            major_version='3',
            minor_version='4'
        ),
        platform='HP-UX',
        ansible_architecture='ia64',
        ansible_distribution_version='B.11.31'
    )

    h = HPUXHardware(module=None, facts=facts)

    hw_facts = h.get_hw_facts()
    print(hw_facts)
    if hw_facts.get('firmware_version') == 'I31 v1.20':
        sys.exit(0)
    else:
        sys.exit(1)

# Generated at 2022-06-13 00:46:25.308617
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    facts = dict(platform='HP-UX', distribution='HP-UX')
    hpux_hardware_collector = HPUXHardwareCollector(facts=facts,
                                                    module=dict())
    assert hpux_hardware_collector.facts == facts

# Generated at 2022-06-13 00:46:38.591455
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hp = HPUXHardwareCollector()
    assert hp.facts_class is HPUXHardware  # pylint: disable=E1101
    assert hp.platform == 'HP-UX'  # pylint: disable=E1101
    assert hp.required_facts == set(['platform', 'distribution'])  # pylint: disable=E1101



# Generated at 2022-06-13 00:46:48.958775
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    """Unit test for method get_hw_facts of class HPUXHardware"""
    hwinfo = HPUXHardware(dict(module=None))
    collected_facts = {"ansible_architecture": "ia64"}
    # Testing model
    rc, out, err = hwinfo.module.run_command("model")
    assert out.strip() == hwinfo.get_hw_facts(collected_facts)["model"]
    # Testing firmware_version
    rc, out, err = hwinfo.module.run_command("/usr/contrib/bin/machinfo |grep -i 'Firmware revision' | grep -v BMC", use_unsafe_shell=True)
    collected_facts["ansible_distribution_version"] = "B.11.23"

# Generated at 2022-06-13 00:46:51.497810
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    h = HPUXHardwareCollector()
    assert h._fact_class == HPUXHardware
    assert isinstance(h._fact_class, object)

# Generated at 2022-06-13 00:46:54.783681
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    from ansible.module_utils.facts.hardware.hpux import HPUXHardwareCollector
    hpux_collector = HPUXHardwareCollector()
    assert hpux_collector.__dict__['_platform'] == 'HP-UX'

# Generated at 2022-06-13 00:47:05.146709
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    module = AnsibleModuleMock()
    obj = HPUXHardware(module)
    rc, out, err = module.run_command("/usr/contrib/bin/machinfo |grep -i 'Firmware revision' | grep -v BMC", use_unsafe_shell=True)
    rc2, out2, err2 = module.run_command("/usr/contrib/bin/machinfo|grep -i 'Machine serial number'", use_unsafe_shell=True)
    hw_facts = obj.get_hw_facts({"ansible_distribution_version": "B.11.23"})
    assert hw_facts["product_serial"] == out2.split('=')[1].strip()

# Generated at 2022-06-13 00:47:12.359438
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    """
    unit test for method get_memory_facts of class HPUXHardware.
    """
    hpuxtestobj = HPUXHardware()
    collected_facts = {}
    collected_facts['ansible_architecture'] = 'ia64'
    collected_facts['ansible_distribution_version'] = 'B.11.23'
    memoryfacts = hpuxtestobj.get_memory_facts(collected_facts=collected_facts)
    assert memoryfacts == {'memfree_mb': 599, 'swaptotal_mb': 19, 'memtotal_mb': 16, 'swapfree_mb': 19}

# Generated at 2022-06-13 00:47:16.471029
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    # Givens
    module = AnsibleModule(
        argument_spec=dict()
    )
    collected_facts = dict(
        ansible_architecture='ia64',
        ansible_distribution='HP-UX',
        ansible_distribution_version='B.11.23'
    )

    # When
    hardware = HPUXHardware(module)
    hardware_facts = hardware.get_memory_facts(collected_facts=collected_facts)

    # Then
    assert hardware_facts['memfree_mb']
    assert hardware_facts['memtotal_mb']
    assert hardware_facts['swapfree_mb']
    assert hardware_facts['swaptotal_mb']


# Generated at 2022-06-13 00:47:21.773245
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    # Setup module
    module = AnsibleModule(argument_spec=dict())
    module.exit_json = lambda: 0

    # Instantiate HPUXHardware class
    hpux_hardware = HPUXHardware(module)
    # Populate method
    hpux_hardware.populate()
    # Retrieve facts
    facts = hpux_hardware.get_facts()
    # Assertions
    for fact in ['processor', 'processor_cores', 'processor_count', 'model', 'firmware_version',
                 'memfree_mb', 'memtotal_mb', 'swapfree_mb', 'swaptotal_mb']:
        assert fact in facts

# Generated at 2022-06-13 00:47:28.874803
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    cpu_facts = {
        'ansible_processor_cores': 8,
        'ansible_processor_count': 8,
        'ansible_processor': 'Intel(R) Itanium(R) Processor 9300 Sequence'
    }
    hpx_hw_facts = HPUXHardware()
    assert hpx_hw_facts.get_cpu_facts(collected_facts={'ansible_distribution_version': 'B.11.31'}) == cpu_facts
    hpx_hw_facts = HPUXHardware()
    assert hpx_hw_facts.get_cpu_facts(collected_facts={'ansible_distribution_version': 'B.11.23'}) == cpu_facts


# Generated at 2022-06-13 00:47:33.776814
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hpux_hw_collector = HPUXHardwareCollector()
    assert hpux_hw_collector._platform == 'HP-UX'
    assert hpux_hw_collector.required_facts == set(['platform', 'distribution'])

# Generated at 2022-06-13 00:48:01.534055
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    '''
    Checks get_cpu_facts from HPUXHardware class.
    '''
    h_facts = HPUXHardware()
    collected_facts = {'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.31'}
    cpu_facts = h_facts.get_cpu_facts(collected_facts=collected_facts)
    assert cpu_facts['processor']
    assert cpu_facts['processor_cores']
    assert cpu_facts['processor_count']

    collected_facts = {'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.23'}
    cpu_facts = h_facts.get_cpu_facts(collected_facts=collected_facts)
    assert cpu_facts['processor']


# Generated at 2022-06-13 00:48:07.133454
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    module = type('obj', (object,), {})()
    setattr(module, 'run_command', run_command)
    hardware = HPUXHardware(module)

    collected_facts = {"ansible_architecture": "9000/800", "ansible_distribution_version": None}
    cpu_facts = hardware.get_cpu_facts(collected_facts)
    assert cpu_facts == {'processor_count': 128}


# Generated at 2022-06-13 00:48:17.388905
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    class module:
        def run_command(self, cmd, use_unsafe_shell=False):
            if cmd == "/usr/bin/vmstat | tail -1":
                return 0, " procs   memory page                  disk          faults    cpu", ""
            elif cmd == "grep Physical /var/adm/syslog/syslog.log":
                return 0,
                """
                Physical: 73800 Kbytes
                Physical: 73800 Kbytes
                Physical: 73800 Kbytes
                Physical: 73800 Kbytes
                """, ""
            elif cmd == "echo 'phys_mem_pages/D' | adb -k /stand/vmunix /dev/kmem | tail -1 | awk '{print $2}'":
                return 0, "1024", ""

# Generated at 2022-06-13 00:48:23.683885
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    config = [ 'ansible_system', 'ansible_product_serial', 'ansible_firmware_version', 'ansible_distribution_version','ansible_architecture']
    hw_collector = HPUXHardwareCollector(config)
    assert hw_collector.config == config
    assert hw_collector._fact_class == HPUXHardware
    assert hw_collector._platform == 'HP-UX'
    assert hw_collector.required_facts == set(['platform', 'distribution'])

# Generated at 2022-06-13 00:48:34.895385
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    """Unit test for method get_memory_facts of class HPUXHardware"""
    mem_facts = {'memfree_mb': None, 'memtotal_mb': None, 'swaptotal_mb': None, 'swapfree_mb': None}
    hw = HPUXHardware()
    hw.module = AnsibleModule()
    hw.module.run_command = run_command

# Generated at 2022-06-13 00:48:44.969272
# Unit test for method get_memory_facts of class HPUXHardware

# Generated at 2022-06-13 00:48:50.882246
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hw = HPUXHardwareCollector()
    assert hw.legacy_collector is None
    assert hw.required_facts == {'platform', 'distribution'}
    assert hw.platform == 'HP-UX'



# Generated at 2022-06-13 00:49:02.256661
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    collected_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': "B.11.23"
    }
    hw = HPUXHardware()
    hw_facts = hw.get_hw_facts(collected_facts=collected_facts)
    assert hw_facts['firmware_version'] == 'L-SK-F-00'
    assert hw_facts['model'] == '9000/800/K570'
    assert hw_facts['product_serial'] == 'CZF30855ZK'

    collected_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': "B.11.31"
    }
    hw = HPUXHardware()
    hw

# Generated at 2022-06-13 00:49:09.005974
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    out = {'ansible_facts': {
        'ansible_system_vendor': 'HP ',
        'ansible_architecture': '9000/800',
        'ansible_distribution': 'HP-UX',
        'ansible_distribution_version': 'B.11.11'}
    }
    hw = HPUXHardware(None)
    facts = hw.populate(out['ansible_facts'])
    assert facts['memfree_mb']
    assert facts['memtotal_mb']
    assert facts['swaptotal_mb']
    assert facts['swapfree_mb']



# Generated at 2022-06-13 00:49:15.277660
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    hardware_facts = HPUXHardware().populate()
    assert hardware_facts['processor_count'] == hardware_facts['processor_cores']
    assert hardware_facts['firmware_version'] >= hardware_facts['ansible_facts']['firmware_version']
    assert hardware_facts['firmware_version'] == hardware_facts['ansible_facts']['firmware_version']
    assert hardware_facts['product_serial'] == hardware_facts['ansible_facts']['product_serial']

# Generated at 2022-06-13 00:49:40.352036
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    test_hardware = HPUXHardware({})
    test_hardware.module = MagicMock()

    test_hardware.module.run_command.return_value = (0, "110  memory pages freed\n", "")
    pagesize = 4096
    test_hardware.get_memory_facts()
    assert test_hardware.facts['memfree_mb'] == (pagesize * 110 // 1024 // 1024)

    test_hardware.module.run_command.return_value = (0, "Physical: 71064 Kbytes", "")
    test_hardware.facts['ansible_architecture'] = '9000/800'
    test_hardware.get_memory_facts()
    assert test_hardware.facts['memtotal_mb'] == 71064 // 1024

    test_hardware.module.run

# Generated at 2022-06-13 00:49:47.224117
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    h = HPUXHardware({'platform': '', 'distribution': 'HP-UX'})
    # Test with PA-RISC
    rc, out, err = h.module.run_command("model | grep -e 9000/785 -e 9000/800", use_unsafe_shell=True)
    if rc == 0:
        h._collected_facts = {'ansible_architecture': '9000/785'}
        result = h.get_cpu_facts()
        assert result['processor_cores'] is None
        assert result['processor'] is None
        assert result['processor_count'] == 2
        # Test with Itanium
    else:
        h._collected_facts = {'ansible_architecture': 'ia64'}
        # Test with B.11.31 > 1204
        h.module

# Generated at 2022-06-13 00:49:57.269621
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    class ModuleMock(object):
        def __init__(self, rc, out, err, module_name):
            self.rc = rc
            self.out = out
            self.err = err
            try:
                self.run_command = self.run_command_class(self.rc, self.out, self.err)
            except TypeError:
                self.run_command = self.run_command_class(self.rc, self.out, self.err, module_name)


# Generated at 2022-06-13 00:50:03.103988
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    test_subject = HPUXHardware({}, {'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.23'})
    result = test_subject.get_hw_facts()
    assert result == {'firmware_version': 'MP HPUX.09.00.00.00.00.0E', 'model': 'ia64 hp server rx2660'}

# Generated at 2022-06-13 00:50:04.535786
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    import doctest
    doctest.testmod(verbose=True)


# Generated at 2022-06-13 00:50:09.396508
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hpux_hw_collector = HPUXHardwareCollector()
    assert hpux_hw_collector._fact_class == HPUXHardware
    assert hpux_hw_collector._platform == 'HP-UX'
    assert hpux_hw_collector.required_facts == set(['platform', 'distribution'])



# Generated at 2022-06-13 00:50:18.123818
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    # Create a fake module
    module = AnsibleModule(argument_spec={})
    # Create collector
    collector = HPUXHardwareCollector()
    # Create a dictionary containing all required facts, declare the processor and architecture to test
    facts = {'platform': 'HP-UX', 'distribution': 'B.11.31'}
    # Create a hardware instance using the fake module, the collector and the facts
    hw = HPUXHardware(module=module, collector=collector, collected_facts=facts)
    # Call the method
    hw.populate()

    # Check the values are correctly found
    assert hw.processor_count == 2
    assert hw.processor_cores == 8
    assert hw.processor == 'Intel(R) Itanium(R)  Processor 9500  series'
    assert hw.memtotal

# Generated at 2022-06-13 00:50:29.168717
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    module = FakeAnsibleModule()
    hw = HPUXHardware()
    collected_facts = {'ansible_architecture': '9000/800', 'ansible_distribution_version': None}
    result = hw.populate(collected_facts)
    assert result == {'processor_count': 18}

    collected_facts = {'ansible_architecture': '9000/785', 'ansible_distribution_version': None}
    result = hw.populate(collected_facts)
    assert result == {'processor_count': 8}

    collected_facts = {'ansible_architecture': 'ia64', 'ansible_distribution_version': "B.11.23"}
    result = hw.populate(collected_facts)

# Generated at 2022-06-13 00:50:37.283552
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    memory_facts = {
        'memfree_mb': 2934,
        'memtotal_mb': 8192,
        'swapfree_mb': 3098,
        'swaptotal_mb': 3173,
    }

    # Collected facts
    collected_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.31',
    }

    hardware = HPUXHardware(None)

    # Unit test the method
    assert hardware.get_memory_facts(collected_facts=collected_facts) == memory_facts

# Generated at 2022-06-13 00:50:44.649424
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    hardware_obj = HPUXHardware({'platform': 'HP-UX', 'distribution': 'HP-UX'}, None)
    hardware_obj.get_cpu_facts({'ansible_architecture': '9000/800'})
    hardware_obj.get_cpu_facts({'ansible_architecture': '9000/785'})
    hardware_obj.get_cpu_facts({'ansible_architecture': 'ia64',
                                'ansible_distribution_version': 'B.11.23'})
    hardware_obj.get_cpu_facts({'ansible_architecture': 'ia64',
                                'ansible_distribution_version': 'B.11.31'})


# Generated at 2022-06-13 00:51:17.368365
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    module = AnsibleModule(argument_spec={})
    hw = HPUXHardware(module)

    input_data = { 'ansible_architecture' : '9000/800' }
    module.run_command = Mock()
    if input_data['ansible_architecture'] == '9000/800':
        module.run_command.return_value = (0, "Physical: 163840 Kbytes", "")
    hw_facts = hw.get_memory_facts(input_data)

    assert hw_facts['memtotal_mb'] == input_data['ansible_architecture']

# Generated at 2022-06-13 00:51:25.435459
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    module = HPUXHardwareCollector.get_platform_option('module')
    module.run_command = lambda x: (0, "", "")
    hphardware = HPUXHardware({'module': module})
    collected_facts = {}
    collected_facts['ansible_architecture'] = 'ia64'
    collected_facts['ansible_distribution_version'] = 'B.11.23'
    memory_facts = hphardware.get_memory_facts(collected_facts)

    assert memory_facts['memfree_mb'] == 0
    assert memory_facts['memtotal_mb'] == 0
    assert memory_facts['swaptotal_mb'] == 0
    assert memory_facts['swapfree_mb'] == 0


# Generated at 2022-06-13 00:51:34.359129
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    module = MockModule()
    fct = HPUXHardware(module=module, collected_facts=None)

    # Test case 1
    pagesize = 4096
    rc, out, err = module.run_command("/usr/bin/vmstat | tail -1", use_unsafe_shell=True)
    data = int(re.sub(' +', ' ', out).split(' ')[5].strip())
    mem = pagesize * data // 1024 // 1024

    assert fct.get_memory_facts() == {'swaptotal_mb': '', 'swapfree_mb': '', 'memtotal_mb': '', 'memfree_mb': mem}


# Mock class for AnsibleModule

# Generated at 2022-06-13 00:51:43.588978
# Unit test for method get_memory_facts of class HPUXHardware

# Generated at 2022-06-13 00:51:46.146755
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hc = HPUXHardwareCollector({
        'platform': 'HP-UX',
        'distribution': 'HP-UX',
    })
    assert hc._platform == 'HP-UX'

# Generated at 2022-06-13 00:51:53.615304
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    # Dict with collected facts
    collected_facts = {
        'platform': 'HP-UX',
        'ansible_architecture': '9000/800',
        'ansible_distribution': 'HP-UX',
        'ansible_distribution_major_version': 'B.11.31'
    }

    # Create instance of class HPUXHardware
    hpu_hw = HPUXHardware(None)

    # Test with collected_facts as param
    cpu_facts = hpu_hw.get_cpu_facts(collected_facts)
    assert type(cpu_facts) == dict
    assert cpu_facts['processor'] == 'Intel Itanium'
    assert cpu_facts['processor_cores'] == 1
    assert cpu_facts['processor_count'] == 1

# Generated at 2022-06-13 00:52:05.017894
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    """ Unit test for HPUXHardware.get_hw_facts """
    import shlex
    from ansible.module_utils.facts.hardware.hpux import HPUXHardware
    import ansible.module_utils.basic
    import ansible.module_utils.facts.hardware.base

    class AnsibleModuleMock:
        """ Module Mocking class used to mock Ansible run_command and get_bin_path methods """
        def __init__(self):
            """ Class constructor """
            self.run_command_args = None
            self.run_command_rc = 0
            self.run_command_out = ''
            self.run_command_err = ''
            self.run_command_invoked = False
            self.get_bin_path_args = None
            self.get_bin_path_rc = 0

# Generated at 2022-06-13 00:52:10.228983
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    module = FakeAnsibleModule()
    hardware = HPUXHardware(module)

    rc, out, err = module.run_command.call_args_list[0][0]
    assert rc == 0
    assert out == '18'
    assert not err

    rc, out, err = module.run_command.call_args_list[1][0]
    assert rc == 0
    assert out == '1'
    assert not err


# Generated at 2022-06-13 00:52:16.585625
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    loader = lambda *args, **kwargs: None
    mocked_module = type('MockedModule', (), {'run_command': loader})()
    mocked_module.fail_json = lambda *args, **kwargs: None
    mocked_module.get_bin_path = loader
    collector = HPUXHardwareCollector(module=mocked_module)
    assert collector.module is mocked_module
    assert collector.platform == 'HP-UX'
    assert collector.fact_class == HPUXHardware

# Generated at 2022-06-13 00:52:23.047461
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    test_param = {
            'platform': 'HP-UX',
            'distribution': 'HP-UX',
        }
    hw_collector = HPUXHardwareCollector(module=None, facts=test_param)

    module = None
    facts = dict(test_param)
    fact_class = HPUXHardware
    platform = HPUXHardwareCollector._platform
    required_facts = hw_collector.required_facts

    assert hw_collector.module == module
    assert hw_collector.facts == facts
    assert hw_collector.fact_class == fact_class
    assert hw_collector.platform == platform
    assert hw_collector.required_facts == required_facts



# Generated at 2022-06-13 00:53:23.251902
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    '''
    Test case to check the function get_memory_facts of class HPUXHardware
    '''
    # create a instance of class HPUXHardware
    test_instance = HPUXHardware()
    # create a dictionary to store the result
    result = dict()
    # Run the method get_memory_facts of class HPUXHardware
    result = test_instance.get_memory_facts()
    # check if the result is not None
    assert result is not None


# Generated at 2022-06-13 00:53:29.806290
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    module = AnsibleModule(argument_spec={})
    hardware_obj = HPUXHardware(module)
    collected_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.23'
    }
    hardware_facts = hardware_obj.populate(collected_facts)
    assert hardware_facts['processor_count'] == 4
    assert hardware_facts['processor'] == 'Intel(R) Itanium(R) Processor 9560'

# Generated at 2022-06-13 00:53:40.651350
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    hw = HPUXHardware()
    hw.module = MockModule()

    # Test with a real server with firmware version
    hw.module.run_command.side_effect = [
        (0, "ia64", None),
        (0, "HPUX11i-v3", None),
        (0, "rp7420", None),
        (0, "Firmware revision = HPUX v2.24", None),
        (0, "Machine serial number = CZC5840BGF", None)
    ]
    facts = hw.populate()
    assert facts['model'] == "rp7420"
    assert facts['firmware_version'] == "HPUX v2.24"
    assert facts['product_serial'] == "CZC5840BGF"

# Generated at 2022-06-13 00:53:46.988004
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    hpu = HPUXHardware()
    data = hpu.get_cpu_facts({"ansible_architecture": "9000/800", "ansible_distribution_version": "B.11.23"})
    assert data['processor_count'] == 1
    data = hpu.get_cpu_facts({"ansible_architecture": "ia64", "ansible_distribution_version": "B.11.23"})
    assert data['processor_count'] == 2
    assert data['processor'] == 'Intel(R) Itanium(R) Processor'
    assert data['processor_cores'] == 2
    data = hpu.get_cpu_facts({"ansible_architecture": "ia64", "ansible_distribution_version": "B.11.31"})

# Generated at 2022-06-13 00:53:58.321403
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    # Initialize a class HPUXHardware
    test_hw = HPUXHardware({})
    # Test method populate with a mock
    test_hw.get_cpu_facts = lambda: {'processor_count': 1, 'processor': "Intel Itanium 2 9000 series"}
    test_hw.get_memory_facts = lambda: {'memfree_mb': 2, 'memtotal_mb': 2, 'swaptotal_mb': 2, 'swapfree_mb': 2}
    test_hw.get_hw_facts = lambda: {'model': 'HP-UX B.11.31 U ia64', 'firmware_version': 'B.01.02', 'product_serial': 'MSX7P9'}
    # call method populate
    test_hw.populate()
    # assert the result
    assert test_hw

# Generated at 2022-06-13 00:54:05.022898
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    """
    Test function that define firmware version and product serial on HP-UX
    """
    m = HPUXHardware()
    m.module = object()

    setattr(m, 'module', object())
    # Set dummy values for ansible_facts
    setattr(m, 'ansible_facts', {'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.23'})
    m.module.run_command = lambda x: (0, u'Firmware revision = 1.1.1.1', '')
    result = m.get_hw_facts()
    assert result['firmware_version'] == '1.1.1.1'
    expected_keys = ['firmware_version']
    assert sorted(result.keys()) == sorted(expected_keys)


# Generated at 2022-06-13 00:54:07.081253
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hpxhw = HPUXHardwareCollector()
    assert hpxhw.required_facts == set(['platform', 'distribution'])

# Generated at 2022-06-13 00:54:10.020097
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hhc = HPUXHardwareCollector(None, {'platform': 'HP-UX', 'distribution': 'HP-UX'}, None)
    assert hhc.platform == 'HP-UX'
    assert hhc.required_facts == set(['platform', 'distribution'])

# Generated at 2022-06-13 00:54:17.290851
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    hw = HPUXHardware({'platform': 'HP-UX', 'distribution': 'B.11.31'})
    hw.module = MagicMock()
    hw.module.run_command.side_effect = [
        (0, 'rp3410', ''),
        (0, 'Firmware revision: P71.08.01', ''),
        (0, 'Machine serial number: CZ2330CSQJ', '')
    ]
    resp = hw.get_hw_facts()
    assert resp['model'] == 'rp3410'
    assert resp['firmware_version'] == 'P71.08.01'
    assert resp['product_serial'] == 'CZ2330CSQJ'


if __name__ == '__main__':
    import pytest
    pytest

# Generated at 2022-06-13 00:54:19.370397
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    x = HPUXHardwareCollector()
    assert x._platform == 'HP-UX'
    assert x._fact_class == HPUXHardware