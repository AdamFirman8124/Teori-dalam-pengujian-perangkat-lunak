

# Generated at 2022-06-13 00:45:33.842839
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    collected_facts = {}
    collected_facts['ansible_architecture'] = '9000/785'
    x = HPUXHardware(None, collected_facts)
    x.get_cpu_facts()
    assert x.get_cpu_facts()['processor_count'] == 2
    collected_facts['ansible_architecture'] = 'ia64'
    collected_facts['ansible_distribution_version'] = 'B.11.31'
    x = HPUXHardware(None, collected_facts)
    x.get_cpu_facts()
    assert x.get_cpu_facts()['processor_count'] == 2
    collected_facts['ansible_distribution_version'] = 'B.11.23'
    x = HPUXHardware(None, collected_facts)
    x.get_cpu_facts()

# Generated at 2022-06-13 00:45:35.227963
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    required_facts = set(['platform', 'distribution'])
    assert HPUXHardwareCollector.required_facts == required_facts

# Generated at 2022-06-13 00:45:47.884329
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    from ansible.module_utils.facts.hardware.hpux import HPUXHardware
    result = HPUXHardware().populate()
    assert result['processor_count'] == 4
    assert result['processor'] == 'Intel(R) Xeon(R) CPU E5520  @ 2.27GHz'
    assert result['processor_cores'] == 8
    assert result['memfree_mb'] == 54972
    assert result['memtotal_mb'] == 98788
    assert result['swaptotal_mb'] == 0
    assert result['swapfree_mb'] == 0
    assert result['model'] == 'ia64 hp server rx2660'
    assert result['firmware_version'] == 'B.11.31.1502.01'
    assert result['product_serial'] == 'CZJ7207JTB'

# Generated at 2022-06-13 00:45:52.141569
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hardware_collector = HPUXHardwareCollector()
    assert hardware_collector.platform == 'HP-UX'
    assert hardware_collector._fact_class == HPUXHardware
    assert hardware_collector.required_facts == set(['platform', 'distribution'])



# Generated at 2022-06-13 00:46:01.737077
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    hw = HPUXHardware()

    hw.module = FakeModule({'ansible_facts': {'distribution_version': 'B.11.23', 'architecture': 'ia64'}})
    hw.module.run_command = FakeRunCommand({'out': 'Firmware revision = 7.9'})
    assert hw.get_hw_facts() == {'firmware_version': '7.9'}

    hw.module = FakeModule({'ansible_facts': {'distribution_version': 'B.11.31', 'architecture': 'ia64'}})
    hw.module.run_command = FakeRunCommand({'out': 'Intel(R) Itanium(R) Processor 9350'})

# Generated at 2022-06-13 00:46:12.253035
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    module = AnsibleModule(argument_spec={})
    hardware_object = HPUXHardware(module)

    current_facts = dict(ansible_architecture='9000/800', ansible_distribution='HP-UX')
    hardware_object_populated = hardware_object.populate(collected_facts=current_facts)

# Generated at 2022-06-13 00:46:23.566728
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    class DummyModule(object):
        class DummyRunCommand(object):
            def __init__(self):
                self.out = "page-size: 4096\n"
                self.out += "pages-free: 2553732\n"
                self.out += "pages-total: 4114060\n"
        def __init__(self):
            self.run_command = self.DummyRunCommand()
    class DummyFactsModule(object):
        def __init__(self):
            self.ansible_architecture = '9000/800'
        def run_command(self, options, use_unsafe_shell=True):
            pass
    h = HPUXHardware(DummyModule(), DummyFactsModule())
    memory_facts = h.get_memory_facts()
    assert memory_facts

# Generated at 2022-06-13 00:46:25.264323
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hwcollector = HPUXHardwareCollector(None)
    assert hwcollector._platform == 'HP-UX'

# Generated at 2022-06-13 00:46:29.601974
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    hardware = HPUXHardware()
    facts = hardware.populate()
    assert type(facts['processor_count']) == int
    assert type(facts['processor_cores']) == int
    assert type(facts['processor']) == str


# Generated at 2022-06-13 00:46:38.138868
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    mock_module = type('', (), {
        "run_command": lambda self, *args, **kwargs: (0, "", ""),
        "check_for_prompt": lambda *args, **kwargs: True,
    })
    mock_module.params = {
        'gather_subset': [],
    }
    mock_class = type('HPUXHardware', (object,), {
        'module': mock_module
    })
    mock_hw = mock_class()

    with open("tests/units/module_utils/facts/hardware/hpmemory", "r") as hpmemory_file:
        hpmemory = hpmemory_file.read()
        mock_module.run_command = lambda *args, **kwargs: (0, hpmemory, "")

   

# Generated at 2022-06-13 00:46:58.080836
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    HardwareCollector.collectors['HP-UX'] = HPUXHardwareCollector()
    HPUXHardwareCollector.collectors['HP-UX'] = HPUXHardwareCollector()
    collected_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.23'
    }
    HPUXHardwareCollector.collectors['HP-UX']._platform = 'HP-UX'
    HPUXHardwareCollector.collectors['HP-UX']._fact_class.module = MagicMock(run_command=MagicMock(return_value=(0, "", "")))
    hw = HPUXHardwareCollector.collectors['HP-UX']._fact_class()
    hw.get_hw_facts(collected_facts)


# Generated at 2022-06-13 00:47:04.772865
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    hardware = HPUXHardware()

    cpu_facts = hardware.get_cpu_facts({'ansible_architecture': '9000/800'})
    assert cpu_facts['processor_count'] == 4

    cpu_facts = hardware.get_cpu_facts({'ansible_architecture': '9000/785'})
    assert cpu_facts['processor_count'] == 4

    cpu_facts = hardware.get_cpu_facts({'ansible_architecture': 'ia64'})
    assert cpu_facts['processor'] == 'Intel(R) Itanium(R) Processor 9360'
    assert cpu_facts['processor_count'] == 1
    assert cpu_facts['processor_cores'] == 1


# Generated at 2022-06-13 00:47:13.436316
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    Modules = {"run_command": dict()}
    Modules["run_command"]["/usr/bin/vmstat | tail -1"] = (0, "  17   4785  1119236125  584   24  304621     0     0     0     0     0     0    0    0    0    0    0", "")
    Modules["run_command"]["grep Physical /var/adm/syslog/syslog.log"] = (0, "Jun  5 12:02:32 home vmunix: Physical: 2098176 Kbytes", "")

# Generated at 2022-06-13 00:47:17.423498
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    data = {
        'ansible_facts': {
            'ansible_architecture': 'ia64'
        }
    }
    hp = HPUXHardware(module=None, collected_facts=data)
    hp._module.run_command = mock_run_command
    facts = hp.get_cpu_facts()
    assert facts['processor_count'] == 4
    assert facts['processor'] == 'Intel Itanium 2'
    assert facts['processor_cores'] == 4


# Generated at 2022-06-13 00:47:24.314633
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    module = AnsibleModule(argument_spec={})
    hardware = HPUXHardware(module)
    hardware.module.run_command = MagicMock(return_value=(0, 'HP-UX', ''))
    hardware.module.run_command = MagicMock(return_value=(0, 'B.11.31', ''))
    hardware.module.run_command = MagicMock(return_value=(0, 'ia64', ''))
    hardware.module.run_command = MagicMock(return_value=(0, 'Intel(R) Itanium(R) processor 9300 series', ''))
    hardware.module.run_command = MagicMock(return_value=(0, 'Firmware revision = B.11.31.2205', ''))

# Generated at 2022-06-13 00:47:28.442705
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hardware_collector = HPUXHardwareCollector()
    assert hardware_collector._fact_class == HPUXHardware
    assert hardware_collector._platform == 'HP-UX'
    assert hardware_collector.required_facts == set(['platform', 'distribution'])

# Generated at 2022-06-13 00:47:33.978181
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    module = FakeAnsibleModule()
    hardware = HPUXHardware()
    hardware.module = module
    collected_facts = {}
    collected_facts['ansible_architecture'] = '9000/800'
    hardware.get_memory_facts(collected_facts)



# Generated at 2022-06-13 00:47:41.953246
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():

    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=[], required=False),
        ),
    )

    # Init HPUXHardware Class to test get_cpu_facts method.
    test_obj = HPUXHardware(module)
    cpu_facts = test_obj.get_cpu_facts()

    # Assertion to check length of test_cpu_facts
    assert len(cpu_facts) == 4

    # Assertion to check values of test_cpu_facts
    assert cpu_facts['processor_count'] == int(os.sysconf('SC_NPROCESSORS_ONLN'))
    assert cpu_facts['processor_cores'] == int(os.sysconf('SC_NPROCESSORS_ONLN'))

# Generated at 2022-06-13 00:47:54.513471
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    class MockModule(object):
        def __init__(self, params=None):
            self.params = params
        def run_command(self, command, *args, **kwargs):
            if self.params.get('ansible_architecture') in ['9000/800', '9000/785']:
                return (0, '1', '')
            elif self.params.get('ansible_architecture') == 'ia64':
                # Mock B.11.23 machinfo output
                if self.params.get('ansible_distribution_version') == 'B.11.23':
                    return (0, 'Intel Itanium family 2 processor\n', '')
                # Mock B.11.31 machinfo output

# Generated at 2022-06-13 00:47:58.206023
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )

    hpux_hw = HPUXHardware(module=module)
    hpux_hw.populate()
    assert hpux_hw.facts['processor_count'] == 8
    assert hpux_hw.facts['memtotal_mb'] == 16384
    assert hpux_hw.facts['swaptotal_mb'] == 32768
    assert hpux_hw.facts['model'] == 'ia64 hp server rx8640'
    assert hpux_hw.facts['firmware_version'] == 'B.11.31.1410'

# Generated at 2022-06-13 00:48:18.450931
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    data = {
        'ansible_architecture': 'ia64',
        'ansible_distribution': 'HP-UX',
        'ansible_distribution_version': 'B.11.31',
    }
    hardware = HPUXHardware(dict(module=None), data)
    assert hardware.get_hw_facts() == {
        'firmware_version': '11.31.823.0',
        'model': 'ia64 hp server rx2800 i2',
        'product_serial': 'W8KDTC099'
    }


# Generated at 2022-06-13 00:48:19.725127
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    assert isinstance(HPUXHardwareCollector(), HardwareCollector)



# Generated at 2022-06-13 00:48:25.899361
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hw_collector = HPUXHardwareCollector()
    assert isinstance(hw_collector, HPUXHardwareCollector)
    assert hw_collector.fact_class == HPUXHardware
    assert hw_collector.platform == 'HP-UX'
    assert hw_collector.required_facts == set(['platform', 'distribution'])
    assert hw_collector._collected_facts is None
    assert hw_collector._fact_class is None
    assert hw_collector._platform is None


# Generated at 2022-06-13 00:48:30.629448
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    module = AnsibleModule(argument_spec=dict(
        gather_subset=dict(default=['all'], type='list'),
    ))

    result = HPUXHardware(module).get_hw_facts()
    assert "model" in result
    assert result["model"] == "hp9000/800"

# Generated at 2022-06-13 00:48:35.044279
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    # Mock of ansible module functions
    module = AnsibleModuleMock()
    module.run_command = run_command_mock

    hpux_hw = HPUXHardware(module)
    memory = hpux_hw.get_memory_facts()

    assert memory['memfree_mb'] == 200

# Generated at 2022-06-13 00:48:43.798110
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    module = type('', (object,), {})
    module.fail_json = lambda *args, **kw: args
    module.run_command = lambda *args, **kw: (0, "", "")
    hw = HPUXHardware()
    hw.module = module
    collected_facts = {'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.31'}
    hw_facts = hw.get_hw_facts(collected_facts)
    assert hw_facts['firmware_version'] is not None
    assert hw_facts['product_serial'] is not None



# Generated at 2022-06-13 00:48:46.460381
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    hardware_facts = HPUXHardware({'productname': 'vmware', 'memorysize': '1'})
    assert hardware_facts.get_memory_facts() == {'memfree_mb': 48, 'memtotal_mb': 1}

# Generated at 2022-06-13 00:48:59.877736
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    import json
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.hardware.hpux import HPUXHardware
    from ansible.module_utils.facts import ServiceManager
    from ansible.module_utils.facts import TimeoutException

    collected_facts = {
        'platform': 'HP-UX',
        'distribution': 'HP-UX',
        'distribution_version': 'B.11.23',
        'ansible_architecture': 'ia64'
    }


# Generated at 2022-06-13 00:49:07.243574
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    hostinfo = HPUXHardwareCollector()
    module = hostinfo._populate()
    assert 'processor_cores' in module.facts
    assert 'processor_count' in module.facts
    assert 'processor' in module.facts
    assert 'memfree_mb' in module.facts
    assert 'memtotal_mb' in module.facts
    assert 'swapfree_mb' in module.facts
    assert 'swaptotal_mb' in module.facts
    assert 'model' in module.facts
    assert 'firmware_version' in module.facts
    assert 'product_serial' in module.facts

# Generated at 2022-06-13 00:49:09.236938
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():

    # Create the class object
    my_obj = HPUXHardware()

    # Run test
    my_obj.get_memory_facts()



# Generated at 2022-06-13 00:49:37.957865
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hw = HPUXHardwareCollector()
    assert hw.platform is 'HP-UX'
    assert hw._fact_class is HPUXHardware

# Generated at 2022-06-13 00:49:40.174751
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    facts = HPUXHardwareCollector()
    assert isinstance(facts, HPUXHardware)
    assert facts._platform == 'HP-UX'

# Generated at 2022-06-13 00:49:47.201382
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():

    # Create instance of class HPUXHardware
    hardware = HPUXHardware({})

    # Create instance of class HardwareCollector
    hardwarecollector = HPUXHardwareCollector({})

    # Create collected facts
    # Run method
    cpu_facts = hardware.get_cpu_facts({'ansible_architecture': '9000/800'})

    # Assertions
    assert isinstance(cpu_facts, dict)
    assert cpu_facts['processor_count'] == int(2)
    assert 'processor' not in cpu_facts
    assert 'processor_cores' not in cpu_facts

    # Create collected facts
    collected_facts = {'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.23'}

    # Run method
    cpu_facts = hardware.get

# Generated at 2022-06-13 00:49:55.900645
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    module = FakeAnsibleModule()
    hardware = HPUXHardware(module)
    hardware_facts = hardware.populate(None)
    assert('memfree_mb' in hardware_facts)
    assert('processor_cores' in hardware_facts)
    assert('processor_count' in hardware_facts)
    assert('memtotal_mb' in hardware_facts)
    assert('swapfree_mb' in hardware_facts)
    assert('swaptotal_mb' in hardware_facts)
    assert('processor' in hardware_facts)
    assert('model' in hardware_facts)
    assert('firmware_version' in hardware_facts)


# Generated at 2022-06-13 00:49:58.053472
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():

    h = HPUXHardwareCollector(None)

    assert h.platform == 'HP-UX'
    assert h.required_facts == set(['platform', 'distribution'])

# Generated at 2022-06-13 00:50:04.537004
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    facts = dict(
        ansible_architecture='9000/800',
        ansible_distribution='HP-UX',
        ansible_distribution_version='B.11.31',
        ansible_system='HP-UX'
    )

    hardware_collector = HPUXHardwareCollector(module=None, facts=facts)

    assert hardware_collector.platform == 'HP-UX'
    assert hardware_collector.required_facts == set(['platform', 'distribution'])

# Generated at 2022-06-13 00:50:13.463547
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    from ansible.module_utils.facts.hardware.hpux import HPUXHardware
    from ansible.module_utils.facts.collections import CollectedFacts

    collected_facts = CollectedFacts({"distribution": "B.11.31", "platform": "HP-UX", "firmware_version": "B.11.31.1706", "product_serial": "CZ12345678"})
    hw_obj = HPUXHardware({})
    facts_dict = hw_obj.get_hw_facts(collected_facts=collected_facts)
    assert 'firmware_version' in facts_dict
    assert 'product_serial' in facts_dict


# Generated at 2022-06-13 00:50:20.485772
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    m = HPUXHardware(dict(ansible_facts={'ansible_distribution': 'HP-UX', 'ansible_distribution_version': 'B.11.31', 'ansible_architecture': 'ia64'}))
    hw_facts = m.get_hw_facts()
    assert hw_facts['firmware_version'] == 'I20B'
    assert hw_facts['model'] == 'rp4440'
    assert hw_facts['product_serial'] == 'USC6128RU6'


# Generated at 2022-06-13 00:50:29.622091
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    hardware = HPUXHardware({'platform': 'HP-UX', 'distribution': 'HP-UX'})
    in_hw_facts = {'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.23'}
    out_hw_facts = {'model': 'B180L', 'firmware_version': 'B180L.03.03', 'product_serial': 'CZH72265NT'}
    assert hardware.get_hw_facts(collected_facts=in_hw_facts) == out_hw_facts



# Generated at 2022-06-13 00:50:35.721089
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    test_module = AnsibleModule(argument_spec={})
    hardware_instance = HPUXHardware(test_module)
    hardware_instance.populate({'memory_mb': {'real': {'total': 135558}}})
    hardware_instance.get_memory_facts()
    assert hardware_instance.collected_facts['ansible_memtotal_mb'] == 135558



# Generated at 2022-06-13 00:50:54.953601
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    hpux_hw = HPUXHardware()
    collected_facts = {'ansible_architecture': '9000/800'}
    hpux_hw.populate(collected_facts)
    memory_facts = hpux_hw.get_memory_facts(collected_facts)
    assert memory_facts['swaptotal_mb'] == 128
    assert memory_facts['swapfree_mb'] == 0
    assert memory_facts['memfree_mb'] == 976
    assert memory_facts['memtotal_mb'] == 4096
    collected_facts = {'ansible_architecture': 'ia64'}
    hpux_hw.populate(collected_facts)
    memory_facts = hpux_hw.get_memory_facts(collected_facts)
    assert memory_facts['swaptotal_mb']

# Generated at 2022-06-13 00:51:05.099893
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    module = AnsibleModuleFake({
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.31'
    })
    hardware = HPUXHardware(module)
    hardware_facts = hardware.populate()

    assert hardware_facts['processor_count'] > 0
    assert hardware_facts['processor_count'] == hardware_facts['processor_cores']
    assert hardware_facts['processor']
    assert hardware_facts['memtotal_mb'] > 0
    assert hardware_facts['memfree_mb'] > 0
    assert hardware_facts['swaptotal_mb'] > 0
    assert hardware_facts['swapfree_mb'] > 0
    assert hardware_facts['product_serial']
    assert hardware_facts['model']
    assert hardware_facts['firmware_version']

# Generated at 2022-06-13 00:51:12.372165
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    m = HPUXHardware()
    # architecture 9000/800
    m.module.params = {'architecture': '9000/800', 'version': '11.31'}
    m.get_memory_facts()
    assert m.memfree_mb == 48783
    assert m.memtotal_mb == 101332
    assert m.swapfree_mb == 72399
    assert m.swaptotal_mb == 72405

    # architecture ia64
    m.module.params = {'architecture': 'ia64', 'version': 'B.11.23'}
    m.get_memory_facts()
    assert m.memfree_mb == 48783
    assert m.memtotal_mb == 101332
    assert m.swapfree_mb == 72399
    assert m.swaptotal_

# Generated at 2022-06-13 00:51:23.903838
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    test_module = type('', (object,), {})

    def test_run_command(self, cmd, use_unsafe_shell=False, **kwargs):
        if cmd == "ioscan -FkCprocessor | wc -l":
            out = "4"
        elif cmd.startswith("/usr/contrib/bin/machinfo"):
            out = """
  number of sockets = 2
  number of cores per socket = 6
  number of threads per core = 1
  total number of logical processors = 12
  total number of physical processors = 12
"""

# Generated at 2022-06-13 00:51:28.760565
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    module = AnsibleModule(
        argument_spec=dict()
    )

    hardware = HPUXHardware(module=module)
    collected_facts = dict(
        ansible_architecture='ia64',
        ansible_distribution_version='B.11.23'
    )
    hardware_facts = hardware.get_hw_facts(collected_facts=collected_facts)
    assert len(hardware_facts.keys()) == 2
    #assert hardware_facts['model'] == 'ia64 HP Integrity rx6600 Server'
    assert hardware_facts['firmware_version'] == 'B.11.23.3920'



# Generated at 2022-06-13 00:51:31.794492
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    h = HPUXHardwareCollector()
    assert h.fact_class == HPUXHardware
    assert h.platform == 'HP-UX'

# Unit tests for constructor of class HPUXHardware

# Generated at 2022-06-13 00:51:39.143844
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    test_module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )
    test_HPUXHardware = HPUXHardware(module=test_module, collected_facts={})
    test_memory_facts = test_HPUXHardware.get_memory_facts()
    assert 'memtotal_mb' in test_memory_facts
    assert 'memfree_mb' in test_memory_facts
    assert 'swaptotal_mb' in test_memory_facts
    assert 'swapfree_mb' in test_memory_facts



# Generated at 2022-06-13 00:51:47.583115
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    # We are going to instantiate a HPUXHardware object
    hpux_hardware = HPUXHardware()
    # We are going to insert data in the collected_facts dictionary
    # so that the method get_cpu_facts will be able to call them
    collected_facts = {}
    collected_facts['ansible_architecture'] = '9000/800'
    cpu_facts = hpux_hardware.get_cpu_facts(collected_facts=collected_facts)
    # We are going to test if the method get_cpu_facts return a dictionary
    # containing the expected keys
    assert 'processor_count' in cpu_facts.keys()
    # We are going to test if the method get_cpu_facts return a dictionary
    # containing the expected values
    assert type(cpu_facts['processor_count']) == int


# Generated at 2022-06-13 00:51:54.511445
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    module = AnsibleModule()
    module.run_command = Mock(return_value=0)
    module.params.get = Mock(return_value=0)
    hpux_hardware = HPUXHardware(module)
    facts = {
        'ansible_architecture': '9000/800',
        'ansible_distribution_version': 'B.11.23',
        'ansible_machine_id': 'xxxx',
        'ansible_os_family': 'unix',
        'ansible_pkg_mgr': 'swinstall'
    }

    # Test 1 cpu_facts
    cpu_facts = hpux_hardware.get_cpu_facts()
    assert cpu_facts['processor_count'] == 1
    # Test 2 cpu_facts

# Generated at 2022-06-13 00:51:59.805432
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    hw_facts = HPUXHardware().get_hw_facts()
    assert hw_facts['model'] is not None
    assert hw_facts['firmware_version'] is not None

# Generated at 2022-06-13 00:52:34.057427
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():

    class TestModule(object):
        def run_command(self, args):
            stdout = ''
            stderr = ''
            rc = 0
            return rc, stdout, stderr

    # create instance of HPUXHardware class and call method get_hw_facts
    hpu = HPUXHardware(TestModule())
    hw_facts = hpu.get_hw_facts()
    assert hw_facts['model'] == ''
    assert hw_facts['firmware_version'] == ''

# Generated at 2022-06-13 00:52:38.319881
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    module = AnsibleModuleMock()
    hardware_obj = HPUXHardware(module)
    facts = hardware_obj.get_hw_facts()
    assert facts['model'] == 'ia64 hp 9000/780'
    assert facts['firmware'] == '9.06'



# Generated at 2022-06-13 00:52:46.356329
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    module = FakeAnsibleModule()
    # We need to set the module params as the collector doesn't call the function
    module.params = {
        'config': 'none',
        'gather_subset': 'default',
        '_ansible_version': '2.3.0',
        'filter': '*',
        '_ansible_no_log': False,
        '_ansible_debug': False,
        '_ansible_check_mode': False
    }

    hphw = HPUXHardware(module)


# Generated at 2022-06-13 00:52:50.550167
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hpux_hw_collector = HPUXHardwareCollector()
    assert isinstance(hpux_hw_collector, HPUXHardwareCollector)
    assert hpux_hw_collector.platform == 'HP-UX'
    assert hpux_hw_collector._required_facts == set(['platform', 'distribution'])

# Generated at 2022-06-13 00:52:56.093150
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    collected_facts = dict(ansible_architecture='ia64')
    module = FakeAnsibleModule(collected_facts)
    hpux_hardware = HPUXHardware(module)
    hpux_hardware.get_memory_facts(collected_facts=collected_facts)



# Generated at 2022-06-13 00:53:04.906888
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():

    # Initialization
    module = AnsibleModule(argument_spec={})
    hw = HPUXHardware(module)
    # Empty dictionary
    hw_facts = {}
    # Dictonary with facts

# Generated at 2022-06-13 00:53:12.673878
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():

    # Unit test
    #
    # Arrange
    #
    collected_facts = {
        'ansible_architecture': '9000/785'
    }

    module = MockModule()
    moduledir = os.path.dirname(__file__)
    mock_vmstat_data = ""
    with open(os.path.join(moduledir, 'mock_vmstat_data.txt'), 'r') as mock_vmstat_file:
        for mock_vmstat_line in mock_vmstat_file:
            mock_vmstat_data += mock_vmstat_line.strip() + "\n"
    mock_adb_data = ""

# Generated at 2022-06-13 00:53:17.456077
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
        hardware = HPUXHardware({'module_name': 'Ignore', 'module_args': 'Ignore'}, check_invalid_arguments=False)
        hw_facts = hardware.get_hw_facts({'platform': 'HP-UX', 'distribution': 'HP-UX'})
        assert(hw_facts['firmware_version'] == 'B.11.31')


# Generated at 2022-06-13 00:53:28.131162
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    module = type('module', (object,), {'run_command': dummy_run_command})()
    h = HPUXHardware(module)

    # Test IA64
    rc, out, err = module.run_command("/usr/sbin/swapinfo -m -d -f -q", use_unsafe_shell=True)
    swaptotal = out.split('\n')[0].strip()

    rc, out, err = module.run_command("/usr/contrib/bin/machinfo | grep Memory", use_unsafe_shell=True)
    data = re.search(r'Memory[\ :=]*([0-9]*).*MB.*', out).groups()[0].strip()


# Generated at 2022-06-13 00:53:32.073407
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    cpu_facts = HPUXHardware().get_cpu_facts()
    assert(cpu_facts['processor_count'])



# Generated at 2022-06-13 00:55:01.475970
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    h = HPUXHardware()
    cpu_facts = h.get_cpu_facts(collected_facts={'ansible_architecture': '9000/800'})
    assert cpu_facts['processor_count'] == 8
    assert cpu_facts['processor_cores'] == 8
    assert cpu_facts['processor'] == 'PA-RISC 1.1'
    cpu_facts = h.get_cpu_facts(collected_facts={'ansible_architecture': 'ia64'})
    if cpu_facts['processor_count'] == 2 and cpu_facts['processor_cores'] == 128:
        assert cpu_facts['processor'] == 'Intel(R) Itanium(R) Processor 9340'

# Generated at 2022-06-13 00:55:09.547744
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    # Test for HP 9000/800
    p = HPUXHardware()
    p.module = None
    test_data = {
        'ansible_architecture': '9000/800',
        'ansible_distribution_version': '11.31',
        'ansible_system_vendor': 'Hewlett-Packard'
    }
    pagesize = 4096
    memory_facts = {}
    rc, out, err = p.module.run_command("/usr/bin/vmstat | tail -1", use_unsafe_shell=True)
    data = int(re.sub(' +', ' ', out).split(' ')[5].strip())
    memory_facts['memfree_mb'] = pagesize * data // 1024 // 1024