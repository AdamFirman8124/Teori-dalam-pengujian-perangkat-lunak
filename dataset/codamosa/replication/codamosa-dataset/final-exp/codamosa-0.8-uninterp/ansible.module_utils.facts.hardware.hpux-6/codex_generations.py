

# Generated at 2022-06-13 00:45:24.718457
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hw = HPUXHardware()
    collector = HPUXHardwareCollector(None, hw)
    assert collector._fact_class is hw
    assert collector._platform == 'HP-UX'

# Generated at 2022-06-13 00:45:30.321539
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    hardware = HPUXHardware()
    cpu_facts = hardware.get_cpu_facts({'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.23'})

    assert cpu_facts == {'processor': 'Intel Itanium 2 (1)', 'processor_cores': 12, 'processor_count': 12}


# Generated at 2022-06-13 00:45:33.619639
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hardware_collector = HPUXHardwareCollector()
    assert hardware_collector._fact_class == HPUXHardware
    assert hardware_collector._platform == 'HP-UX'
    assert hardware_collector.required_facts == set(['platform', 'distribution'])

# Generated at 2022-06-13 00:45:44.886855
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    module = MockModule()
    hw = HPUXHardware(module=module)

    collected_facts = dict(
        ansible_architecture='9000/800',
    )

    expected_facts = dict(
        processor_count=4,
    )

    cpu_facts = hw.get_cpu_facts(collected_facts=collected_facts)
    assert cpu_facts == expected_facts

    collected_facts = dict(
        ansible_architecture='ia64',
        ansible_distribution_version="B.11.23",
    )

    expected_facts = dict(
        processor_count=4,
        processor='Intel(R) Itanium(R) Processor 9560',
        processor_cores=1,
    )


# Generated at 2022-06-13 00:45:46.459786
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    h = HPUXHardwareCollector()
    assert h.platform == 'HP-UX'

# Generated at 2022-06-13 00:45:51.579691
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    # This test is to ensure bug-fix ANSIBLE-16881
    hw = HPUXHardware()
    collected_facts = {'ansible_distribution_version': 'B.11.23'}
    facts = hw.get_hw_facts(collected_facts=collected_facts)
    assert facts.get('firmware_version') == '3.60'

# Generated at 2022-06-13 00:45:56.101774
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    hardware_obj = HPUXHardware()
    collected_facts = {'ansible_architecture': '9000/800'}
    cpu_facts = hardware_obj.get_cpu_facts(collected_facts)
    assert cpu_facts['processor_count'] == 8



# Generated at 2022-06-13 00:46:03.982397
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    m = dict(platform='HP-UX', distribution='HP-UX')
    f = HPUXHardware(module=None)
    assert f.get_cpu_facts(collected_facts=m) == {'processor_count': 2}
    m['ansible_architecture'] = '9000/800'
    assert f.get_cpu_facts(collected_facts=m) == {'processor_count': 2}
    m['ansible_architecture'] = 'ia64'
    m['ansible_distribution_version'] = 'B.11.23'
    assert f.get_cpu_facts(collected_facts=m) == {'processor_count': 4, 'processor': 'Intel Itanium 2 9120D',
                                                  'processor_cores': 4}
    assert f.get_cpu_facts

# Generated at 2022-06-13 00:46:12.944614
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    # check if _fact_class is set
    try:
        hw_collector = HPUXHardwareCollector()
        assert '_fact_class' in dir(hw_collector)
        del hw_collector
    except NameError:
        pass

    # check if _platform is set
    try:
        hw_collector = HPUXHardwareCollector()
        assert '_platform' in dir(hw_collector)
        del hw_collector
    except NameError:
        pass

    # check if required_facts is set
    try:
        hw_collector = HPUXHardwareCollector()
        assert 'required_facts' in dir(hw_collector)
        del hw_collector
    except NameError:
        pass

# Generated at 2022-06-13 00:46:23.845785
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    inst = HPUXHardware(dict(module=dict(run_command=lambda *args, **kwargs: (0, '', ''))))
    # Test get_memory_facts on ia64
    rc, out, err = inst.module.run_command("/usr/contrib/bin/machinfo | grep Memory", use_unsafe_shell=True)
    if re.search(r'Memory.*MB.*', out):
        inst.get_memory_facts(collected_facts=dict(ansible_architecture='ia64'))
        # Test get_memory_facts on ia64 with B.11.23
        inst.get_memory_facts(collected_facts=dict(ansible_architecture='ia64', ansible_distribution_version='B.11.23'))
        # Test get_memory_

# Generated at 2022-06-13 00:46:44.630717
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hp = HPUXHardwareCollector()
    assert isinstance(hp, HardwareCollector)
    assert hp.platform == 'HP-UX'
    assert hp.required_facts == {'platform', 'distribution'}
    assert hp._fact_class == HPUXHardware
    assert hp.collect()


# Generated at 2022-06-13 00:46:45.884597
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    h = HPUXHardwareCollector()
    assert h.platform == 'HP-UX'

# Generated at 2022-06-13 00:46:57.372715
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hw = HPUXHardwareCollector()
    # Test for the attributes of class HPUXHardwareCollector
    assert hw.platform == 'HP-UX', "Failed to initialize the attribute platform of class HPUXHardwareCollector"
    assert not hw.required_facts, "Failed to initialize the attribute required_facts of class HPUXHardwareCollector"
    assert not hw.optional_facts, "Failed to initialize the attribute optional_facts of class HPUXHardwareCollector"
    assert len(hw.collectors) == 0, "Failed to initialize the attribute collectors of class HPUXHardwareCollector"
    # Test for the methods of class HPUXHardwareCollector
    assert hw.supports_platform(), "Failed to determine platform support of class HPUXHardwareCollector"

# Generated at 2022-06-13 00:46:59.533990
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    c = HPUXHardwareCollector()
    assert c
    assert c._platform == 'HP-UX'
    assert c._fact_class.platform == 'HP-UX'
    assert c.required_facts == set(['platform', 'distribution'])

# Generated at 2022-06-13 00:47:09.854428
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    """
    Unit test for method get_memory_facts of class HPUXHardware
    :return:
    """
    mod_obj = __import__("ansible.module_utils.facts.hardware.hpux",
                         fromlist=["ansible.module_utils.facts.hardware.hpux"])

    mod_obj.run_command = lambda *args, **kwargs: (0, '     4096     4096     4096', '')
    result = mod_obj.HPUXHardware.get_memory_facts('ia64')
    assert result['memfree_mb'] == 4

    mod_obj.run_command = lambda *args, **kwargs: (0, '     4096     4096     4096', '')
    result = mod_obj.HPUXHardware.get_memory_facts('9000/800')

# Generated at 2022-06-13 00:47:17.999794
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    class Module():
        def run_command(self, cmd, use_unsafe_shell=None):
            if cmd == "/usr/sbin/swapinfo -m -d -f -q":
                return 0, "170572", None

# Generated at 2022-06-13 00:47:25.008032
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    collected_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.31'
    }
    h = HPUXHardware()
    h.module = FakeAnsibleModule()
    cpu_facts = h.get_cpu_facts(collected_facts=collected_facts)
    assert cpu_facts.get('processor_count') == 1
    assert cpu_facts.get('processor_cores') == 16
    assert cpu_facts.get('processor') == 'Intel(R) Itanium(R) processor 9500 series'

    collected_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.23'
    }
    h = HPUXHardware()

# Generated at 2022-06-13 00:47:32.388230
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    hw = HPUXHardware()
    facts = hw.populate()
    assert facts == {
        'memfree_mb': 1058,
        'memtotal_mb': 8192,
        'model': 'ia64 hp server integrity rx2660',
        'processor': '2.10 gigahertz Intel Itanium 2',
        'processor_cores': 4,
        'processor_count': 8,
        'swapfree_mb': 6,
        'swaptotal_mb': 2000
    }

# Generated at 2022-06-13 00:47:40.224893
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():

    class MockModule(object):
        def __init__(self):
            self.run_command_args = None
            self.run_command_rc = 0
            self.run_command_calls = 0

        def run_command(self, args):
            self.run_command_args = args
            self.run_command_calls += 1
            rc = self.run_command_rc
            if rc == 0:
                return rc, "Success", ""
            return rc, "", "error"

    module = MockModule()

    hardware = HPUXHardware()
    hardware.module = module

    hardware.get_hw_facts()

    assert module.run_command_args == "model"



# Generated at 2022-06-13 00:47:43.692939
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hardware_facts = HPUXHardwareCollector().collect(None, None)

    assert hardware_facts['ansible_processor_count'] == hardware_facts['ansible_processor_vcpus']
    assert hardware_facts['ansible_processor_cores'] == hardware_facts['ansible_processor_vcpus']
    assert hardware_facts['ansible_memtotal_mb'] == (hardware_facts['ansible_memtotal_mb'] / 1024)

# Generated at 2022-06-13 00:48:17.918838
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    """
    Test for method get_cpu_facts of class HPUXHardware
    """
    module = AnsibleModule(argument_spec={})
    module.params = {}
    collected_facts = {}

    # Testing this case
    collected_facts['ansible_distribution_version'] = "B.11.23"
    collected_facts['ansible_architecture'] = "ia64"
    hw = HPUXHardware(module)
    cpu_facts = hw.get_cpu_facts(collected_facts=collected_facts)
    assert cpu_facts['processor_count'] == 4

    # Testing this case
    collected_facts['ansible_distribution_version'] = "B.11.31"
    collected_facts['ansible_architecture'] = "ia64"
    hw = HPUXHardware

# Generated at 2022-06-13 00:48:24.143301
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    hostname = "host_name"
    collected_facts = {'ansible_architecture': 'ia64', 'ansible_distribution_version': "B.11.31"}
    hardware = HPUXHardware(hostname, collected_facts=collected_facts)
    memory_facts = hardware.get_memory_facts()
    assert memory_facts == {'memfree_mb': '67988', 'memtotal_mb': '99998', 'swaptotal_mb': '25', 'swapfree_mb': '25'}


# Generated at 2022-06-13 00:48:35.423146
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    # Testing get_hw_facts with ia64 OS
    test_data = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.23'
    }
    test_hw = HPUXHardware(module=None)
    assert test_hw.get_hw_facts(collected_facts=test_data) == {'model': 'ia64 hp server',
                                                               'firmware_version': 'J06',
                                                               'product_serial': 'US1234568', }

    # Testing get_memory_facts with ia64 OS
    test_data = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.31'
    }
    test_memory = H

# Generated at 2022-06-13 00:48:38.594962
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    module = AnsibleModuleMock()
    hardware_collector = HPUXHardwareCollector(module=module)
    assert hardware_collector._platform == 'HP-UX'

# Generated at 2022-06-13 00:48:46.960170
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    """
    Ensure that cpu facts are correctly returned.
    """
    mock_module = MockModule()
    mock_module.run_command.side_effect = [
        [0, "8\n", ""],
        [0, "processor family = Intel(R) Itanium(R) processor 9500 series\n", ""],
        [0, "4\n", ""]
    ]
    hw = HPUXHardware(mock_module, facts={'ansible_architecture': 'ia64',
                                          'ansible_distribution_version': 'B.11.23'})
    cpu_facts = hw.get_cpu_facts()
    assert cpu_facts['processor_count'] == 8
    assert cpu_facts['processor'] == 'Intel(R) Itanium(R) processor 9500 series'

# Generated at 2022-06-13 00:48:53.217306
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hardware_collector = HPUXHardwareCollector()
    assert hardware_collector.fact_class == HPUXHardware
    assert hardware_collector.platform == 'HP-UX'
    assert hardware_collector.required_facts == set(['platform', 'distribution'])


# Generated at 2022-06-13 00:48:57.203258
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    def get_module(ansible_facts):
        return type('module', (object,), {'run_command': run_command, 'module': type('module', (object,), {'params': {'gather_subset': 'all'}}), 'get_bin_path': lambda *_: "/usr/sbin/swapinfo"})(ansible_facts)

    def run_command(cmd, *_):
        if cmd == "ioscan -FkCprocessor | wc -l":
            return 0, "4\n", ""
        if cmd == "/usr/contrib/bin/machinfo | grep 'Number of CPUs'":
            return 0, "Number of CPUs              = 8\n", ""

# Generated at 2022-06-13 00:49:06.849065
# Unit test for method get_memory_facts of class HPUXHardware

# Generated at 2022-06-13 00:49:15.770429
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    params = {'module': object(), 'use_unsafe_shell': object()}
    hpux_hardware = HPUXHardware(params)
    hpux_hardware.populate({'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.23'})
    for method in ('run_command',):
        setattr(hpux_hardware.module, method, lambda *args, **kwargs: (0, '', ''))
    hpux_hardware.get_hw_facts()
    hpux_hardware.populate({'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.31'})

# Generated at 2022-06-13 00:49:26.714701
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec={})
    hardware = HPUXHardware(module=module)
    collected_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.31'
    }
    memory_facts = hardware.get_cpu_facts(collected_facts=collected_facts)
    assert memory_facts['processor_cores'] == 2
    assert memory_facts['processor_count'] == 2

    collected_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.23'
    }
    memory_facts = hardware.get_cpu_facts(collected_facts=collected_facts)
    assert memory_facts['processor_cores'] == 2


# Generated at 2022-06-13 00:49:45.094835
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    module = AnsibleModule(argument_spec={})
    hardware_facts = HPUXHardware(module).populate()

    out = {'processor': 'Intel(R) Itanium(R) Processor', 'processor_cores': 85,
           'processor_count': 15, 'memtotal_mb': 40000, 'memfree_mb': 9673,
           'swaptotal_mb': 34816, 'swapfree_mb': 34816}

    print(hardware_facts)
    assert hardware_facts == out, "Failed to gather or parse hardware facts"

# Tests for class HPUXHardwareCollector

# Generated at 2022-06-13 00:49:49.083317
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    phc = HPUXHardwareCollector()
    assert phc._fact_class == HPUXHardware
    assert phc._platform == 'HP-UX'
    assert phc.required_facts == set(['platform', 'distribution'])



# Generated at 2022-06-13 00:49:58.496610
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    class ModuleStub(object):
        def __init__(self):
            self.return_values = {}

        def run_command(self, command):
            key = command.split()[0]
            return self.return_values[key]

    module_stub = ModuleStub()
    module_stub.return_values = {
        "vmstat": (0, "r b w swap free re mf pi po fr de sr m1 m2 m3 m4 md in sy cs us sy id 0 0 0 3353892 2 sp sh s5 s6 fr pa sr dy pw x <<emalloc>> <<t_vmem>> <<v_vmem>>", ""),
        "echo": (0, "3145728", '')
    }
    hardware = HPUXHardware(module_stub)
    hw_facts = hardware

# Generated at 2022-06-13 00:50:02.950532
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    hw = HPUXHardware(dict(platform='HP-UX'))
    hw.module.run_command = lambda *args, **kw: (0, 'hp server rx2660', '')
    hw.get_hw_facts()
    assert hw.facts['model'] == 'hp server rx2660'

# Generated at 2022-06-13 00:50:03.985565
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    HPUXHardware().get_cpu_facts()

# Generated at 2022-06-13 00:50:05.006982
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    HPUXHardwareCollector()

# Generated at 2022-06-13 00:50:09.069735
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hpux = HPUXHardwareCollector()
    assert hpux._platform == 'HP-UX'
    assert hpux.required_facts == set(['platform', 'distribution'])
    assert hpux._fact_class == HPUXHardware


# Generated at 2022-06-13 00:50:12.648687
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hardware_collector = HPUXHardwareCollector()
    assert hardware_collector._fact_class == HPUXHardware
    assert hardware_collector._platform == 'HP-UX'
    assert hardware_collector.required_facts == set(['platform', 'distribution'])

# Generated at 2022-06-13 00:50:16.925300
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    hw_facts = HPUXHardware().get_hw_facts()
    assert hw_facts['model'] in ['HP rp8420', 'HP rp8440'], "The model is not correctly parsed"
    assert hw_facts['firmware_version'] in ['C.11.31', 'C.11.31'], "The firmware_version is not correctly parsed"

# Generated at 2022-06-13 00:50:27.762214
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    facts = {'ansible_architecture': '9000/800', 'ansible_distribution_version': 'B.11.31'}
    hw = HPUXHardware(module=None, collected_facts=facts)
    cpu_facts = hw.get_cpu_facts(collected_facts=facts)
    assert cpu_facts['processor_count'] == 16
    assert cpu_facts['processor'] == 'Intel(R) Itanium(R) Processor 9350'
    assert cpu_facts['processor_cores'] == 8

    facts = {'ansible_architecture': '9000/785', 'ansible_distribution_version': 'B.11.31'}
    hw = HPUXHardware(module=None, collected_facts=facts)

# Generated at 2022-06-13 00:50:46.987394
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    prospector = HPUXHardwareCollector()
    collected_facts = {'ansible_architecture': 'ia64', 'ansible_distribution': 'HP-UX', 'ansible_distribution_version': 'B.11.23'}
    hardware = prospector.populate_facts(collected_facts)
    assert hardware['firmware_version'] == 'B.11.23'
    assert hardware['model'] == 'ia64 ia64 ia64'
    collected_facts = {'ansible_architecture': 'ia64', 'ansible_distribution': 'HP-UX', 'ansible_distribution_version': 'B.11.31'}
    hardware = prospector.populate_facts(collected_facts)
    assert hardware['firmware_version'] == 'B.11.31'
   

# Generated at 2022-06-13 00:50:51.051360
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    module = AnsibleModule(argument_spec={})
    hpuxhw = HPUXHardware()
    hpuxhw.get_memory_facts()



# Generated at 2022-06-13 00:50:53.804684
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    mem_facts = HPUXHardware().get_memory_facts()
    mem_keys = ['memfree_mb', 'memtotal_mb', 'swaptotal_mb', 'swapfree_mb']
    assert sorted(mem_keys) == sorted(mem_facts.keys())

# Generated at 2022-06-13 00:51:00.247692
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    mock_module = MockModule()
    mock_module.params = {'gather_subset': '!all,!min'}
    mock_module.run_command = Mock(return_value=(0, '', ''))
    HPUXHardware_class_instance = HPUXHardware(mock_module)

    # Test with no parameter
    mock_module.run_command = Mock(return_value=(0, '10', ''))
    HPUXHardware_class_instance.populate()
    assert HPUXHardware_class_instance.facts == {}

    # Test with gather_subset: all
    mock_module.params = {'gather_subset': 'all'}
    mock_module.run_command = Mock(return_value=(0, '10', ''))

# Generated at 2022-06-13 00:51:09.458126
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    module = AnsibleModule(argument_spec={})
    hpux_hardware = HPUXHardware(module)
    collected_facts = {
        'platform': 'HP-UX',
        'ansible_architecture': 'ia64'
    }
    result = hpux_hardware.get_memory_facts(collected_facts)
    assert result
    collected_facts = {
        'platform': 'HP-UX',
        'ansible_architecture': '9000/800'
    }
    result = hpux_hardware.get_memory_facts(collected_facts)
    assert result
    collected_facts = {
        'platform': 'HP-UX',
        'ansible_architecture': '9000/785'
    }

# Generated at 2022-06-13 00:51:14.664049
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():

    # Setup the mocks
    module = AnsibleModuleMock()
    module_result = dict(
        changed=False,
        memory_facts=dict(),
    )

    # Setup the class we are going to test
    hpux_hardware = HPUXHardware(module=module)

    # Now we can execute the code we want to test
    memory_facts = hpux_hardware.get_memory_facts()

    # Check that the result is correct
    module_result['memory_facts'] = memory_facts

    assert module_result == dict(
        changed=False,
        memory_facts=dict(
            memfree_mb=1472,
            memtotal_mb=8192,
            swapfree_mb=0,
            swaptotal_mb=8192,
        ),
    )



# Generated at 2022-06-13 00:51:18.942589
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    """
    Unit test for method get_memory_facts of class HPUXHardware
    """
    hpux_hardware_obj = HPUXHardware()
    memory_facts = hpux_hardware_obj.get_memory_facts(collected_facts={'ansible_architecture':'9000/800'})
    assert memory_facts['memtotal_mb'] == 2048
    assert memory_facts['swaptotal_mb'] == 15120

# Generated at 2022-06-13 00:51:24.950099
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    class DummyModule:

        def run_command(self, cmd):
            out = b'total:  16075   2911   12857   6257   4042  100344  473968  712096  633880\n' \
                  b'free:   78245  655571\n'

            return 0, out, ''

    h = HPUXHardware(DummyModule())

    assert h.get_memory_facts() == {
        'swaptotal_mb': 633880,
        'memtotal_mb': 712096,
        'memfree_mb': 6257,
        'swapfree_mb': 655571
    }



# Generated at 2022-06-13 00:51:35.423368
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    module = MockModule()
    collect_facts = False
    hardware = HPUXHardware(module)

    # Test B.11.11 PA
    collected_facts = {
        'ansible_architecture': '9000/800',
        'ansible_distribution_version': 'B.11.11'
    }
    cpu_facts = hardware.get_cpu_facts(collected_facts=collected_facts)
    assert cpu_facts['processor'] == 'PA 88000@1.00GHz'
    assert cpu_facts['processor_cores'] == '150'

    # Test B.11.23 IA64
    collected_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.23'
    }

# Generated at 2022-06-13 00:51:44.302457
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    """
    Unit test for method get_cpu_facts of class HPUXHardware
    """
    hpux = HPUXHardware()
    hpux.module = AnsibleModule(argument_spec={})
    hpux.module.run_command = Mock(return_value=(0, '', ''))
    hpux.module.run_command.return_value = [0, '2', '']

    # Setting ansible_architecture to a supported architecture
    hpux.module.ansible_facts = {'ansible_architecture': '9000/800'}
    cpu_facts = hpux.get_cpu_facts()
    assert cpu_facts == {'processor_count': 2}

    # Setting ansible_architecture to a supported architecture

# Generated at 2022-06-13 00:52:18.166982
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    _module = AnsibleModule(
        argument_spec=dict(
            filter=dict(required=False, type='list', default=['!*'])
        ),
        supports_check_mode=True
    )

    hpuxhardware = HPUXHardware(_module)
    # On PA-RISC systems, syslog.log is parsed.
    collected_facts = {'ansible_architecture': '9000/800'}
    memory_facts = hpuxhardware.get_memory_facts(collected_facts=collected_facts)
    assert isinstance(memory_facts['memfree_mb'], int)
    assert isinstance(memory_facts['memtotal_mb'], int)
    assert isinstance(memory_facts['swapfree_mb'], int)

# Generated at 2022-06-13 00:52:27.627870
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    data = dict(ansible_architecture='9000/800')
    module = FakeAnsibleModule(
        data,
        textwrap.dedent("""
        "vmstat" (currently not installed)
        "grep" (currently not installed)
        """),
        textwrap.dedent("""
        "machinfo" (currently not installed)
        """)
    )
    hardware = HPUXHardware(module)
    rc, out, err = module.run_command("grep Physical /var/adm/syslog/syslog.log")
    assert "AttributeError" in err

    data = dict(ansible_architecture='ia64')
    data['ansible_distribution_version'] = "B.11.23"

# Generated at 2022-06-13 00:52:31.885780
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    """
    Test function get_hw_facts of class LinuxHardware.
    In these tests, we create an instance of class HPUXHardware and
    call it get_hw_facts function with a list of collected facts. We then test
    the return value of the function by checking the value of the dictionary
    keys model and firmware.
    """
    mock_module = MagicMock()
    mock_module.run_command.side_effect = [("", "ia64", ""), ("", "HP-UX", ""), ("", "B.11.31", "")]

    hw_facts = HPUXHardware(mock_module)
    hw_facts.get_hw_facts()
    assert hw_facts.model == "HP-UX"
    assert hw_facts.firmware == ""

# Generated at 2022-06-13 00:52:36.125087
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    facts = dict(
        platform='HP-UX',
        distribution='HP-UX',
    )

    # Call method
    hpx_hw_collector = HPUXHardwareCollector()

    # Assert result
    assert hpx_hw_collector._platform == 'HP-UX'
    assert hpx_hw_collector._fact_class == HPUXHardware


# Generated at 2022-06-13 00:52:41.688453
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    hpux_hardware = HPUXHardware(module=None)
    collected_facts = dict(ansible_architecture="9000/800")
    data = hpux_hardware.get_memory_facts(collected_facts=collected_facts)

    assert data['memfree_mb']
    assert data['memtotal_mb']
    assert data['swaptotal_mb']
    assert data['swapfree_mb']



# Generated at 2022-06-13 00:52:50.221039
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    module = AnsibleModule(argument_spec={})
    hardware = HPUXHardware(module)
    # Total memory should be reported in MB
    data = hardware.get_memory_facts()
    assert data['memtotal_mb'] > 0
    assert isinstance(data['memtotal_mb'], int)
    # Swap should be reported in MB
    assert data['swaptotal_mb'] > 0
    assert isinstance(data['swaptotal_mb'], int)
    assert data['memfree_mb'] < data['memtotal_mb']
    assert data['swapfree_mb'] < data['swaptotal_mb']


# Generated at 2022-06-13 00:53:01.556038
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    module = AnsibleModule(argument_spec={})
    harware_obj = HPUXHardware(module=module)

    cpu_facts = harware_obj.get_cpu_facts()
    memory_facts = harware_obj.get_memory_facts()
    hw_facts = harware_obj.get_hw_facts()

    harware_obj.populate()

    cpu_facts.update(memory_facts)
    cpu_facts.update(hw_facts)

    for k, v in harware_obj.facts.items():
        if k in cpu_facts:
            if v == cpu_facts[k]:
                print("Fact %s matched" % k)
            else:
                print("Fact %s not matched" % k)
                print("Expected: %s" % cpu_facts[k])
                print

# Generated at 2022-06-13 00:53:07.839628
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    """
    Return data for memory facts
    """
    facts = {'ansible_architecture': 'ia64'}
    test_class = HPUXHardware(None, facts)
    test_class.module.run_command = run_command_mock
    memory_facts = test_class.get_memory_facts()
    assert(memory_facts['memtotal_mb'] == 16384)

# Generated at 2022-06-13 00:53:12.827279
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils.facts.hardware import Hardware
    from ansible.module_utils.facts.hardware.hpux import HPUXHardwareCollector

    collected_facts = FactCollector(None, {'platform': 'HP-UX'}, None).collect()
    hpux_hw = HPUXHardwareCollector(None, collected_facts, None).collect()['hpux']
    assert isinstance(hpux_hw, Hardware)

# Generated at 2022-06-13 00:53:19.104195
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hw_collector = HPUXHardwareCollector({'platform': 'HP-UX', 'distribution': 'B.11.31'})
    assert hw_collector.required_facts == set(['platform', 'distribution'])
    assert hw_collector._platform == 'HP-UX'
    assert hw_collector._fact_class == HPUXHardware


# Generated at 2022-06-13 00:54:32.040144
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    module = AnsibleModuleMock()
    module.run_command = run_command_mock

    h = HPUXHardware(module=module)

    h.get_memory_facts()

    assert h.facts['memtotal_mb'] == 3245
    assert h.facts['memfree_mb'] == 3073
    assert h.facts['swaptotal_mb'] == 922
    assert h.facts['swapfree_mb'] == 922


# Generated at 2022-06-13 00:54:38.988315
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    from ansible.module_utils.facts.hardware.hpux import HPUXHardware

    module = HPUXHardware()
    collected_facts = {'ansible_architecture': 'ia64',
                       'ansible_distribution_version': 'B.11.31'}
    memory_facts = module.get_memory_facts(collected_facts=collected_facts)
    assert memory_facts['memtotal_mb'] == 913
    assert memory_facts['memfree_mb'] == 748
    assert memory_facts['swaptotal_mb'] == 716
    assert memory_facts['swapfree_mb'] == 716



# Generated at 2022-06-13 00:54:43.882060
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    module = AnsibleModule({})
    hw = HPUXHardware(module=module)
    cpu_facts = hw.get_cpu_facts({'ansible_architecture': '9000/800'})
    assert cpu_facts['processor_count'] == 2
    cpu_facts = hw.get_cpu_facts({'ansible_architecture': 'ia64'})
    assert cpu_facts['processor_cores'] == 42
    assert cpu_facts['processor_count'] == 16
    assert cpu_facts['processor'] == 'Intel(R) Xeon(R) CPU E7-4870  @ 2.40GHz'


# Generated at 2022-06-13 00:54:52.327994
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    h = HPUXHardware({'system': 'HP-UX',
                      'distribution': 'HP-UX',
                      'distribution_version': 'B.11.23',
                      'architecture': 'ia64'})
    h.module = MockModule({'architecture' : 'ia64'})
    h.module.run_command = Mock(return_value=(0, '', ''))
    h.get_hw_facts()

    h.module.run_command.assert_called_with('/usr/contrib/bin/machinfo |grep -i \'Machine serial number\' ',
                                            use_unsafe_shell=True)



# Generated at 2022-06-13 00:55:01.529757
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    module = FakeModule('9000/800')
    module.run_command = MagicMock(return_value=(0, '', ''))
    hardware = HPUXHardware(module=module)
    hardware.module.run_command.side_effect = [(0, '512', ''), (0, '972864', ''), (0, '204800', ''), (0, '0', '')]
    collected_facts = {'ansible_architecture':'9000/800'}
    memory_facts = hardware.get_memory_facts(collected_facts)
    assert memory_facts['memfree_mb'] == 512
    assert memory_facts['memtotal_mb'] == 953
    assert memory_facts['swapfree_mb'] == 200
    assert memory_facts['swaptotal_mb'] == 200
    memory

# Generated at 2022-06-13 00:55:05.421674
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    mock = MagicMock(return_value=(0, 'IA64_HP_LOADPARM=0x1             ', ''))
    with patch.object(HPUXHardware, 'run_command', mock):
        test_obj = HPUXHardware(MagicMock())
        result = test_obj.get_hw_facts()
        assert result['model'] == 'IA64_HP_LOADPARM=0x1             '

# Generated at 2022-06-13 00:55:11.458416
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    """Unit tests for getting facts from HPUXHardware class."""
    h = HPUXHardware()
    h.module = AnsibleModule(argument_spec={})
    h.module.run_command = lambda *args, **kwargs: (0, "", "")

    # run the populate method
    facts = h.populate()
    assert sorted(facts) == sorted([
        'processor',
        'processor_cores',
        'processor_count',
        'memfree_mb',
        'memtotal_mb',
        'swapfree_mb',
        'swaptotal_mb'])