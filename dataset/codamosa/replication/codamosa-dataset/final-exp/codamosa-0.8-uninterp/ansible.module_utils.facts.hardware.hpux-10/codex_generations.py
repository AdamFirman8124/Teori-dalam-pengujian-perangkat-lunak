

# Generated at 2022-06-13 00:45:27.672887
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    module = AnsibleModule(argument_spec={})
    hw = HPUXHardware(module)
    result = hw.populate()
    assert result['model'] == 'iLO3'
    assert result['processor_cores'] == '1'
    assert result['processor_count'] == '1'
    assert result['processor'] == 'Intel(R) Xeon(R) CPU           E5620  @ 2.40GHz'



# Generated at 2022-06-13 00:45:35.966491
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    facts = {}
    test_obj = HPUXHardware(facts)
    # HP-UX B.11.11 ia64
    test_obj.facts['ansible_architecture'] = 'ia64'
    test_obj.facts['ansible_distribution'] = 'HP-UX'
    test_obj.facts['ansible_distribution_version'] = "B.11.23"
    result = test_obj.get_cpu_facts()
    assert result['processor'] == 'Intel(R) Itanium(R) 9300  series processor'
    assert result['processor_cores'] == 288
    assert result['processor_count'] == 72
    # HP-UX B.11.31 ia64
    test_obj.facts['ansible_architecture'] = 'ia64'

# Generated at 2022-06-13 00:45:39.231353
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hardwareCollector = HPUXHardwareCollector()
    assert hardwareCollector._fact_class == HPUXHardware
    assert hardwareCollector._platform == 'HP-UX'

# Generated at 2022-06-13 00:45:42.533126
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hw_c = HPUXHardwareCollector()
    assert hw_c



# Generated at 2022-06-13 00:45:51.266392
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    # collected_facts: dict used by HPUXHardware
    collected_facts = {'ansible_architecture': '9000/800',
                                                'ansible_distribution_version': 'B.11.23'}
    hardware = HPUXHardware(None)
    cpu_facts = hardware.get_cpu_facts(collected_facts=collected_facts)
    if hardware.module:
        hardware.module.fail_json.assert_called_once_with(msg='Cannot find CPU info')
    assert cpu_facts == {'processor': '', 'processor_count': 0, 'processor_cores': 0}


# Generated at 2022-06-13 00:46:01.111019
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    # fake host
    collected_facts = {'platform': 'HP-UX', 'ansible_architecture': '9000/785', 'ansible_distribution_version': 'B.11.31'}
    # fake module
    module = type('', (), {'run_command': lambda x: (0, '', '')})
    # create HPUXHardware instance
    hardware = HPUXHardware(module)
    # get test result
    result = hardware.get_memory_facts(collected_facts=collected_facts)
    # test result
    assert result['memfree_mb'] is not None
    assert result['memtotal_mb'] is not None
    assert result['swaptotal_mb'] is not None
    assert result['swapfree_mb'] is not None


# Generated at 2022-06-13 00:46:09.605718
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    hw = HPUXHardware(dict(module=None), dict(ansible_architecture='9000/800', ansible_distribution='HP-UX'))
    res = hw.populate()
    assert 'processor_count' in res
    assert 'processor' in res
    assert 'processor_cores' in res
    assert 'memfree_mb' in res
    assert 'memtotal_mb' in res
    assert 'swapfree_mb' in res
    assert 'swaptotal_mb' in res
    assert 'model' in res
    assert 'firmware_version' in res



# Generated at 2022-06-13 00:46:21.509011
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    module = AnsibleModule(argument_spec={})
    hardware_class = HPUXHardwareCollector.collect(module=module)
    hardware = HPUXHardware(module)
    rc, out, err = hardware.module.run_command("hostname")
    collected_facts = dict(ansible_hostname=out.strip())
    hardware_facts = hardware.populate(collected_facts)
    hardware_facts = hardware_facts.get('ansible_facts')
    assert hardware_facts.get('processor_count') == hardware_class.get_cpu_facts().get('processor_count')
    assert hardware_facts.get('processor') == hardware_class.get_cpu_facts().get('processor')

# Generated at 2022-06-13 00:46:24.663660
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    # Test list of required facts
    required_facts = set(['platform', 'distribution'])
    obj = HPUXHardwareCollector()
    assert obj._platform == 'HP-UX'
    assert obj.required_facts == required_facts

# Generated at 2022-06-13 00:46:34.187743
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    from ansible.module_utils.facts import FactCollector
    facts_collector = FactCollector('ansible.module_utils.facts.hardware.hpux',
                                    {},
                                    [HPUXHardwareCollector],
                                    [],
                                    None)
    facts_collector.collect()
    collected_facts = facts_collector.ansible_facts
    processor_facts = HPUXHardware().get_memory_facts(collected_facts)
    assert ('memfree_mb' in processor_facts)
    assert ('memtotal_mb' in processor_facts)
    assert ('swaptotal_mb' in processor_facts)
    assert ('swapfree_mb' in processor_facts)



# Generated at 2022-06-13 00:46:48.957980
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    module = FakeAnsibleModule()
    hpu_hw = HPUXHardware(module=module)
    hpu_hw.get_memory_facts()

    assert hpu_hw.facts == {'memfree_mb': 0, 'memtotal_mb': 0, 'swapfree_mb': 0, 'swaptotal_mb': 0}


# Generated at 2022-06-13 00:46:59.066646
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    class TestHardwareCollector:
        def __init__(self, facts=None):
            self.facts = facts

    # Arrange
    hardwareCollector = HPUXHardwareCollector()

    # Act
    hardwareCollector.collect(
        TestHardwareCollector({'platform': 'HP-UX', 'distribution': 'HP-UX'})
    )

    # Assert
    assert hardwareCollector.facts['platform'] == 'HP-UX', 'Unexpected platform'
    assert hardwareCollector.facts['distribution'] == 'HP-UX', 'Unexpected distribution'
    assert hardwareCollector.facts['memfree_mb'] == 0, 'Unexpected memfree_mb'
    assert hardwareCollector.facts['memtotal_mb'] == 0, 'Unexpected memtotal_mb'

# Generated at 2022-06-13 00:47:09.422466
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    module = MockModule()
    hardware = HPUXHardware(module)

    # Case 1: tested values are returned
    # Case 2: tested values are not returned

# Generated at 2022-06-13 00:47:17.658295
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    test_module = AnsibleModule(argument_spec={})
    test_module.params = {}
    test_module.run_command = MagicMock(return_value=(0, "", ""))
    # I/O

# Generated at 2022-06-13 00:47:21.153559
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hardware_collector = HPUXHardwareCollector()
    fact_class = hardware_collector._fact_class
    platform = hardware_collector._platform
    required_facts = hardware_collector.required_facts

    assert fact_class() is not None
    assert HPUXHardware() is not None
    assert platform == 'HP-UX'
    assert required_facts == set(['platform', 'distribution'])

# Generated at 2022-06-13 00:47:26.120576
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    module = type('', (), {})()
    module.run_command = run_command
    hardware = HPUXHardware(module)
    collected_facts = {'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.31'}
    res = hardware.get_memory_facts(collected_facts)
    assert res == {'memfree_mb': 2321, 'memtotal_mb': 24005, 'swaptotal_mb': 49152, 'swapfree_mb': 48131}



# Generated at 2022-06-13 00:47:31.361772
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    module = AnsibleModule(argument_spec=dict())

    # Create instance of HPUXHardwareCollector
    hw_collector = HPUXHardwareCollector(module=module)

    # Test methods that should return a value
    assert hw_collector.collect() == {}

# Generated at 2022-06-13 00:47:36.019680
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    required_facts = set(['platform', 'distribution'])
    hw_collector = HPUXHardwareCollector(required_facts)
    assert required_facts == hw_collector.required_facts
    assert HPUXHardware == hw_collector._fact_class
    assert 'HP-UX' == hw_collector._platform

# Generated at 2022-06-13 00:47:38.976739
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hw_c = HPUXHardwareCollector()
    assert hw_c.fact_class == HPUXHardware
    assert hw_c.platform == 'HP-UX'
    assert hw_c.required_facts == set(['platform', 'distribution'])

# Generated at 2022-06-13 00:47:42.561762
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    _fact_class = HPUXHardware
    _platform = 'HP-UX'
    required_facts = set(['platform', 'distribution'])
    hw_facts = HPUXHardwareCollector(None, None)
    assert hw_facts.required_facts == required_facts
    assert hw_facts._fact_class == _fact_class
    assert hw_facts._platform == _platform


# Generated at 2022-06-13 00:48:02.906508
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    """Unit tests for method get_memory_facts for class HPUXHardware"""
    from ansible.module_utils.facts.hardware.hpux import HPUXHardware
    from ansible.module_utils.facts.hardware.base import BaseHardware
    module = BaseHardware.get_module()
    inventory = {'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.23'}
    obj = HPUXHardware(module)
    memory_facts = obj.get_memory_facts(inventory)
    assert memory_facts['memtotal_mb'] > 0
    assert memory_facts['memfree_mb'] > 0
    assert memory_facts['swaptotal_mb'] > 0
    assert memory_facts['swapfree_mb'] > 0



# Generated at 2022-06-13 00:48:05.955550
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    h = HPUXHardwareCollector()
    assert isinstance(h, HardwareCollector)
    assert h._platform is 'HP-UX'
    assert h._fact_class is HPUXHardware

# Generated at 2022-06-13 00:48:12.365906
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.hardware.hpux import HPUXHardwareCollector
    from ansible.module_utils.facts.hardware.hpux import HPUXHardware
    from ansible.module_utils.facts.system.base import SystemCollector
    from ansible.module_utils.facts.system.hpux import HPUXSystem
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual
    from ansible.module_utils.facts.virtual.base import VirtualCollector
    import json


# Generated at 2022-06-13 00:48:21.853265
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    collected_facts = {'ansible_architecture': '9000/800'}
    h = HPUXHardware(None)
    memory_facts = h.get_memory_facts(collected_facts=collected_facts)
    assert memory_facts.get('memtotal_mb') == 8 * 1024
    assert memory_facts.get('memfree_mb') <= 8 * 1024
    assert memory_facts.get('swaptotal_mb') <= 1024
    assert memory_facts.get('swapfree_mb') <= 1024

    collected_facts = {'ansible_architecture': 'ia64'}
    h = HPUXHardware(None)
    memory_facts = h.get_memory_facts(collected_facts=collected_facts)
    assert memory_facts.get('memtotal_mb') == 32 * 1024

# Generated at 2022-06-13 00:48:27.592014
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    fake_module = type('', (), {})()
    fake_module.run_command = lambda *args, **kwargs: (None, None, None)
    fake_facts = {'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.31'}
    test_object = HPUXHardware()
    test_object.module = fake_module
    fake_module.run_command = lambda *args, **kwargs: (0, "B.11.31", None)
    assert test_object.populate(collected_facts=fake_facts)

# Generated at 2022-06-13 00:48:28.548944
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    HPUXHardwareCollector()


# Generated at 2022-06-13 00:48:31.192304
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hw_collector = HPUXHardwareCollector()
    assert hw_collector.fact_class == HPUXHardware

# Generated at 2022-06-13 00:48:32.876897
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    m = HPUXHardwareCollector()
    assert m._platform == 'HP-UX'

# Generated at 2022-06-13 00:48:42.961746
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    HPUXHardware_obj = HPUXHardware()
    collected_facts = {'ansible_architecture': '9000/800',
                       'ansible_distribution_version': 'B.11.23',
                       'ansible_distribution': 'HP-UX'}
    cpu_facts = HPUXHardware_obj.get_cpu_facts(collected_facts)
    assert cpu_facts['processor_count'] == 16
    collected_facts = {'ansible_architecture': 'ia64',
                       'ansible_distribution_version': 'B.11.23',
                       'ansible_distribution': 'HP-UX'}
    cpu_facts = HPUXHardware_obj.get_cpu_facts(collected_facts)

# Generated at 2022-06-13 00:48:44.643485
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    module = None
    module = Mock(return_value='')
    HPUXHardwareObj = HPUXHardware(module)
    HPUXHardwareObj.get_hw_facts()



# Generated at 2022-06-13 00:49:02.094453
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    mock_module = type('MockModule', (object,), {'run_command': MagicMock(return_value=(0, "", ""))})
    mock_module.run_command.return_value = (0, " 2 ", "")
    os.access = MagicMock(return_value=True)
    mock_module.run_command.return_value = (0, " 2 ", "")
    test_obj = HPUXHardware(mock_module)
    test_obj.get_memory_facts()



# Generated at 2022-06-13 00:49:06.687207
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    hw = HPUXHardware({'ansible_facts': {'ansible_architecture': '9000/800'}})
    hw.module.run_command = lambda *args, **kwargs: (0, ' ', '')
    mem_facts = hw.get_memory_facts()
    assert mem_facts['memfree_mb']
    assert mem_facts['memtotal_mb']

# Generated at 2022-06-13 00:49:15.642858
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec=dict())

    # This is how you'd normally instantiate
    hw = HPUXHardware(module=module)

    # Example collected_facts for an HP-UX PA-RISC server
    collected_facts = {'processor': 'PA-8800 processor', 'machine': '9000/785', 'architecture': '9000/785',
                       'ansible_architecture': '9000/785', 'ansible_machine': '9000/785'}

    # Example collected_facts for an HP-UX Itanium server

# Generated at 2022-06-13 00:49:26.526964
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    # Set up instance of class HPUXHardware
    test_hw_instance = HPUXHardware(None)
    # Set up some facts
    collected_facts = {
        'ansible_architecture': '9000/800',
        'ansible_distribution_version': 'B.11.23'
    }
    # Call the method with test input
    memory_facts = test_hw_instance.get_memory_facts(collected_facts)
    assert memory_facts == {'swaptotal_mb': 0, 'memfree_mb': 20, 'swapfree_mb': 0, 'memtotal_mb': 146}
    collected_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.23'
    }

# Generated at 2022-06-13 00:49:31.479157
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    hw = HPUXHardware({'platform': 'HP-UX', 'distribution': 'B.11.31'})
    assert isinstance(hw.get_hw_facts(), dict)
    assert set(hw.get_hw_facts().keys()) == set(['model', 'firmware_version', 'product_serial'])


# Generated at 2022-06-13 00:49:42.913137
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    facts = {
        'ansible_architecture': '9000/800',
        'ansible_machine_id': '0x2baba1fefa61d5a00a80552e9b3d12c0',
        'ansible_machine_id_short': '2baba1fefa61d5a00a80552e9b3d12c0'
    }
    module = MagicMock()
    module.run_command.return_value = (0, '', '')
    os_access = patch('os.access').start()
    os_access.return_value = True
    hw = HPUXHardware(module)
    hw.get_memory_facts(facts)
    assert hw.facts['memfree_mb'] == 61488



# Generated at 2022-06-13 00:49:47.181794
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    """test_HPUXHardwareCollector"""
    # Instantiate HPUXHardwareCollector object
    hw_collector = HPUXHardwareCollector()
    # Assert that hw_collector is HPUXHardwareCollector object
    assert isinstance(hw_collector, HPUXHardwareCollector)

# Generated at 2022-06-13 00:49:56.902609
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    module = AnsibleModuleMock()
    module.run_command = run_command_mock
    h = HPUXHardware(module)
    facts = h.populate()
    assert facts == {'processor': 'Intel(R) Xeon(R) CPU E7-8890 v4 @ 2.20GHz',
                     'processor_cores': 30,
                     'processor_count': 2,
                     'memfree_mb': 86664,
                     'memtotal_mb': 103364,
                     'swapfree_mb': 819,
                     'swaptotal_mb': 819,
                     'model': 'HP Integrity rx2800 i2',
                     'firmware_version': 'HP-UX 11iv3 C.03.03'}



# Generated at 2022-06-13 00:50:00.250825
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    my_module = AnsibleModule(argument_spec={})
    my_obj = HPUXHardware(module=my_module)
    collected_facts = {"ansible_architecture": "ia64", "ansible_distribution_version": "B.11.23"}
    my_obj.get_hw_facts(collected_facts)

    return True


# Generated at 2022-06-13 00:50:10.473327
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    facts = {'ansible_architecture': '9000/800', 'ansible_distribution_version': 'B.11.31'}
    hpu = HPUXHardware(dict(), facts)
    cpu_facts = hpu.get_cpu_facts()
    assert cpu_facts['processor_count'] == 4
    assert cpu_facts['processor_cores'] == 1
    assert cpu_facts['processor'] == 'Intel(R) Itanium(R) 2 9100 series (1.59 GHz)'
    facts = {'ansible_architecture': '9000/800', 'ansible_distribution_version': 'B.11.23'}
    hpu = HPUXHardware(dict(), facts)
    cpu_facts = hpu.get_cpu_facts()
    assert cpu_facts['processor_count'] == 4

# Generated at 2022-06-13 00:50:37.414693
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    hw = HPUXHardware()
    hw.module = AnsibleModuleMock()
    hw.module.run_command.return_value = (0, "server1.example.com", "")
    hw.populate()
    assert hw.facts['model'] == "server1.example.com"



# Generated at 2022-06-13 00:50:45.223825
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    # Define parameters
    collected_facts_up = {'ansible_architecture': '9000/800', 'ansible_lsb': {'codename': 'B.11.11', 'major_release': '11', 'minor_release': '11', 'distributor': 'HP', 'description': 'B.11.11'}}
    collected_facts_ia64 = {'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.31', 'ansible_lsb': {'codename': 'B.11.31', 'major_release': '11', 'minor_release': '31', 'distributor': 'HP', 'description': 'B.11.31'}}


# Generated at 2022-06-13 00:50:50.550852
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    class MockModule:
        def __init__(self):
            self.params = dict()
            self.changed = False
            self.failed = False

# Generated at 2022-06-13 00:50:57.637908
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    module = ansible.module_utils.basic.AnsibleModule(
            argument_spec=dict(
                gather_subset=dict(default=['all'], type='list'),
                filter=dict(default=None, type='list')
            ))

    test_hardware = HPUXHardware()
    test_hardware.module = module
    test_hardware.platform = 'HP-UX'
    test_hardware.distribution = 'HP-UX'

    test_hardware.cpu_facts = {
        'processor': 'Intel(R) Itanium(R) Processor at 1.60GHz', 'processor_cores': 8, 'processor_count': 32
    }


# Generated at 2022-06-13 00:51:07.957499
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    class ModuleStub(object):
        def __init__(self):
            self.run_command_results = (1, "", "")

        def run_command(self, cmd, check_rc=True):
            return self.run_command_results

    module = ModuleStub()
    hphw = HPUXHardware(module)

    # Test normal
    module.run_command_results = (0, "", "")
    out = hphw.get_memory_facts()
    assert 'memfree_mb' in out.keys()
    assert 'memtotal_mb' in out.keys()
    assert 'swaptotal_mb' in out.keys()
    assert 'swapfree_mb' in out.keys()

    # Test error
    module.run_command_results = (1, "", "")


# Generated at 2022-06-13 00:51:16.743147
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    assert HPUXHardware(dict(ansible_facts=dict(ansible_architecture='9000/800'))).get_cpu_facts() == dict(processor_count=1)
    assert HPUXHardware(dict(ansible_facts=dict(ansible_distribution_version='B.11.23',
                                                ansible_architecture='ia64'))).get_cpu_facts() == dict(processor_count=2,
                                                                                                     processor_cores=4,
                                                                                                     processor='Intel(R) Itanium(R) Processor 9340')

# Generated at 2022-06-13 00:51:21.444260
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    """
    Unit test for constructor of class HPUXHardwareCollector.
    """
    collector = HPUXHardwareCollector()
    assert collector._fact_class == HPUXHardware
    assert collector._platform == 'HP-UX'
    assert collector.required_facts == set(['platform', 'distribution'])

if __name__ == '__main__':
    test_HPUXHardwareCollector()

# Generated at 2022-06-13 00:51:27.375212
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    h = HPUXHardware()
    collected_facts = {'ansible_architecture': '9000/800', 'ansible_distribution_version': 'B.11.31'}

    # Test with ansible_architecture 9000/800
    cpu_facts = h.get_cpu_facts(collected_facts=collected_facts)
    assert cpu_facts['processor_count'] == 4
    assert cpu_facts['processor_cores'] == 2
    assert cpu_facts['processor'] == 'HP PA-RISC 8500'

    # Test with ansible_architecture 9000/785
    collected_facts['ansible_architecture'] = '9000/785'
    cpu_facts = h.get_cpu_facts(collected_facts=collected_facts)
    assert cpu_facts['processor_count']

# Generated at 2022-06-13 00:51:30.082094
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    hardware = HPUXHardware()
    facts = hardware.populate()


if __name__ == '__main__':
    test_HPUXHardware_populate()

# Generated at 2022-06-13 00:51:32.253779
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hw_collector = HPUXHardwareCollector()
    assert hw_collector._platform == 'HP-UX'


# Generated at 2022-06-13 00:52:16.270272
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    m = HPUXHardware()
    collected_facts = {'platform': 'HP-UX', 'distribution': 'HP-UX', 'ansible_architecture': '9000/800', 'ansible_distribution_version': 'B.11.23'}
    cpu_facts = m.get_cpu_facts(collected_facts=collected_facts)
    assert cpu_facts['processor_count'] == 2
    assert cpu_facts['processor_cores'] == 1

# Generated at 2022-06-13 00:52:20.136616
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hardware_collector = HPUXHardwareCollector()

    assert hardware_collector._fact_class == HPUXHardware
    assert hardware_collector._platform == 'HP-UX'
    assert hardware_collector.required_facts == set(['platform', 'distribution'])

# Generated at 2022-06-13 00:52:23.543431
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    module = AnsibleModule(argument_spec={})
    hardware = HPUXHardware(module)
    hardware.get_hw_facts({'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.23'})

# Generated at 2022-06-13 00:52:31.267718
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    h = HPUXHardware({})
    h.module = FakeAnsibleModule()
    # Test for physical machine
    h.module.run_command = MagicMock(return_value=(0, ' ', ''))
    facts = h.get_memory_facts({'ansible_architecture': '9000/800'})
    assert facts['memfree_mb'] == 0
    assert facts['memtotal_mb'] == 0
    assert facts['swaptotal_mb'] == 0
    assert facts['swapfree_mb'] == 0
    # Test for virtual machine where machinfo doesn't contain information about memory
    h.module.run_command = MagicMock(return_value=(0, ' ', ''))

# Generated at 2022-06-13 00:52:40.569648
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    platform_facts = {
        'platform': 'HP-UX',
        'distribution': 'HP-UX',
        'distribution_version': 'B.11.31',
        'architecture': 'ia64'
    }
    module = AnsibleModule(argument_spec={})
    module.exit_json = MagicMock()
    hardware = HPUXHardware(module, platform_facts)
    hardware.populate()
    assert(module.exit_json.called)
    assert(module.exit_json.call_count == 1)
    assert(module.exit_json.call_args[0][0]['ansible_facts']['processor_count'] == 2)
    assert(module.exit_json.call_args[0][0]['ansible_facts']['memtotal_mb'] == 1015)

# Generated at 2022-06-13 00:52:46.222782
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    hw = HPUXHardware()
    hw.module = AnsibleModuleMock()
    hw.module.run_command = run_command_mock
    assert hw.get_memory_facts() == {'swapfree_mb': 256, 'swaptotal_mb': 256, 'memtotal_mb': 8192, 'memfree_mb': 8192}


# Helpers



# Generated at 2022-06-13 00:52:54.192258
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    class Module():
        def __init__(self):
            self.run_command = test_HPUXHardware_get_hw_facts.run_command
            self.params = {}
        def fail_json(self, *args, **kwargs):
            raise AssertionError(kwargs['msg'])

    class AnsibleModule():
        def __init__(self, module, **kwargs):
            self.params = module.params
            self.exit_json = module.exit_json

    module = Module()
    ansible = AnsibleModule(module)

    hardware = HPUXHardware(ansible)
    collected_facts = {'platform': 'HP-UX', 'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.23'}

# Generated at 2022-06-13 00:53:00.770740
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    m = HPUXHardware({'platform': 'HP-UX'})
    m.module = Mock(run_command=Mock(return_value=(0, "1", "")))
    collected_facts = {'ansible_architecture': '9000/800'}
    expected_cpu_facts = {'processor_count': 1}
    cpu_facts = m.get_cpu_facts(collected_facts=collected_facts)
    assert cpu_facts == expected_cpu_facts


# Generated at 2022-06-13 00:53:04.611188
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    memory_facts = HPUXHardware().get_memory_facts()
    assert isinstance(memory_facts, dict)
    for key in ['memfree_mb', 'memtotal_mb', 'swaptotal_mb', 'swapfree_mb']:
        assert key in memory_facts


if __name__ == '__main__':
    import pytest
    pytest.main()

# Generated at 2022-06-13 00:53:09.859016
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    collected_facts = {'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.31'}
    hw = HPUXHardware()
    cpu_facts = hw.get_cpu_facts(collected_facts)
    assert cpu_facts['processor_count'] == 2
    assert cpu_facts['processor'] == "Intel(r) Itanium(r) 2 Processor"
    assert cpu_facts['processor_cores'] == 2



# Generated at 2022-06-13 00:54:58.543017
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    test_module = AnsibleModule(argument_spec={})
    hw_facts = {}

    def run_command_mock(self, cmd, *args, **kwargs):
        if cmd == "model":
            out = "ia64 hp server rx8620"
            return 0, out, ""
        elif cmd == "/usr/contrib/bin/machinfo |grep -i 'Firmware revision' | grep -v BMC":
            return 0, "Firmware revision: OA 3.53", ""
        elif cmd == "/usr/contrib/bin/machinfo |grep -i 'Machine serial number' ":
            return 0, "Machine serial number: ABCDEFG1234567890", ""

    test_module.run_command = run_command_mock

# Generated at 2022-06-13 00:55:01.751487
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    h = HPUXHardwareCollector()
    assert h._fact_class == HPUXHardware
    assert h._platform == 'HP-UX'
    assert h.required_facts == {'platform', 'distribution'}

# Generated at 2022-06-13 00:55:03.778536
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hpc = HPUXHardwareCollector()
    assert hpc.required_facts == set(['platform', 'distribution'])
    assert hpc._platform == 'HP-UX'