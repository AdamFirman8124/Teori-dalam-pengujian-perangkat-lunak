

# Generated at 2022-06-13 00:45:30.824562
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    """
    Test get_memory_facts of class HPUXHardware.

    :return:
    """
    # Create HPUXHardware instance with module object for testing
    hpux_hw = HPUXHardware(dict(module=dict()))

    if hpux_hw.module.run_command("uname -s")[1] == 'HP-UX':
        memory_facts = hpux_hw.get_memory_facts()
        assert isinstance(memory_facts, dict)
        assert all(key in memory_facts for key in ['memtotal_mb', 'memfree_mb', 'swaptotal_mb', 'swapfree_mb'])
        assert memory_facts['memtotal_mb'] > 0
        assert memory_facts['memfree_mb'] > 0
        assert memory_facts['swaptotal_mb'] > 0


# Generated at 2022-06-13 00:45:33.143338
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hpux_hw_collector = HPUXHardwareCollector()
    assert hpux_hw_collector.platform == 'HP-UX'


# Generated at 2022-06-13 00:45:34.814788
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hpu_hw = HPUXHardwareCollector()
    assert hpu_hw.returns_multiple_facts is False



# Generated at 2022-06-13 00:45:37.361370
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hardware_collector = HPUXHardwareCollector(None)
    assert hardware_collector._platform == 'HP-UX'
    assert hardware_collector._fact_class == HPUXHardware
    assert hardware_collector.required_facts == set(['platform', 'distribution'])


# Generated at 2022-06-13 00:45:41.653535
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    """
        test_HPUXHardware_get_hw_facts: test get_hw_facts method of class HPUXHardware
    """
    import module_utils.facts.hardware.hpux as hpuxHardware_module
    class MockModule:
        def __init__(self):
            self.run_command_called = False
            self.run_command_result = 0, 'RX2660', ''
            self.run_command_result2 = 0, 'Firmware revision = v3.48', ''
        def run_command(self, *args, **kwargs):
            self.run_command_called = True
            return self.run_command_result
    module = MockModule()

# Generated at 2022-06-13 00:45:53.103665
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    input_data = {
        'ansible_architecture': '9000/785',
        'ansible_distribution_version': 'B.11.23'
    }
    test_hardware = HPUXHardware(dict(), dict())
    test_hardware.get_cpu_facts(collected_facts=input_data)
    assert test_hardware.facts['processor_count'] == 2
    assert test_hardware.facts['processor'] == 'Intel(R) Itanium 2 9100 series Processor'
    assert test_hardware.facts['processor_cores'] == 1
    input_data = {
        'ansible_architecture': '9000/800',
        'ansible_distribution_version': 'B.11.23'
    }

# Generated at 2022-06-13 00:45:57.207685
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    hardware = HPUXHardware()
    if hardware.get_cpu_facts():
        print("Test HPUXHardware get_cpu_facts PASSED")
    else:
        print("Test HPUXHardware get_cpu_facts FAILED")



# Generated at 2022-06-13 00:46:02.781453
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    from ansible.module_utils.facts.hardware.hpux import HPUXHardware

    mem_facts = HPUXHardware().get_memory_facts()
    assert mem_facts['memtotal_mb'] != 0
    assert mem_facts['memfree_mb'] != 0
    assert mem_facts['swaptotal_mb'] != 0
    assert mem_facts['swapfree_mb'] != 0

# Generated at 2022-06-13 00:46:12.751598
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.hardware import HPUXHardware
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector import Collector

    facts = {
        'ansible_architecture': '9000/800',
        'ansible_distribution': 'HP-UX',
        'ansible_distribution_version': 'B.11.23'
    }

    fake0 = BaseFactCollector(module=None)
    fake0.collect(platform=facts['ansible_architecture'], distribution=facts['ansible_distribution'],
                  distribution_version=facts['ansible_distribution_version'], fail_on_error=True)
    fake0.collect

# Generated at 2022-06-13 00:46:14.294958
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    HPUXHardwareCollector()

# Generated at 2022-06-13 00:46:27.420948
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    module = AnsibleModule(
        argument_spec={
            'gather_subset': dict(default=['!all']),
        }
    )

    hw_facts = HPUXHardware({
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.23'
    })

    res = hw_facts.get_hw_facts()

    assert res == {
        'model': 'rp7420',
        'firmware_version': '375E'
    }

# Generated at 2022-06-13 00:46:32.959865
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    facts = {
        'ansible_architecture': '9000/800',
        'ansible_distribution_version': 'B.11.23'}
    hardware = HPUXHardware(dict(), facts)

    hardware._module.run_command = lambda *args, **kwargs: (0, "1", None)

# Generated at 2022-06-13 00:46:37.513824
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts import collectors
    from ansible.module_utils.facts.hardware.hpux_hardware import HPUXHardwareCollector
    assert issubclass(HPUXHardwareCollector, BaseFactCollector)
    # Test proper registration
    assert HPUXHardwareCollector in collectors._collectors['HP-UX']

# Generated at 2022-06-13 00:46:48.214189
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    import json
    hpux_hardware = HPUXHardware({})
    # collect_facts = {'ansible_os_family': 'HPUX', 'ansible_architecture': '9000/800', 'ansible_distribution_version': 'B.11.31'}
    collect_facts = {'ansible_os_family': 'HPUX', 'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.31'}
    # collect_facts = {'ansible_os_family': 'HPUX', 'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.23'}
    memory_facts = hpux_hardware.get_memory_facts(collected_facts=collect_facts)

# Generated at 2022-06-13 00:46:54.502575
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec={})
    hardware = HPUXHardware(module=module)
    hardware.populate()
    hardware_facts = hardware.get_cpu_facts()
    assert hardware_facts.get('processor_count'), "HP-UX processor_count fact not retrieved"
    assert hardware_facts.get('processor'), "HP-UX processor fact not retrieved"
    assert hardware_facts.get('processor_cores'), "HP-UX processor_cores fact not retrieved"

# Generated at 2022-06-13 00:46:55.504644
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    HPUXHardwareCollector()


# Generated at 2022-06-13 00:46:59.449635
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    module = AnsibleModule()
    facts = HPUXHardware(module)
    result = facts.get_hw_facts()
    assert isinstance(result, dict)
    assert 'model' in result.keys()
    assert 'firmware_version' in result.keys()


# Generated at 2022-06-13 00:47:04.924919
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    # Creating an instance of class HPUXHardwareCollector
    hardware_collector = HPUXHardwareCollector()

    # Testing instance attributes
    assert hardware_collector._fact_class == HPUXHardware
    assert hardware_collector._platform == 'HP-UX'
    assert hardware_collector.required_facts == {'platform', 'distribution'}


# Generated at 2022-06-13 00:47:10.313855
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    hardware_obj = HPUXHardware()
    hardware_obj.module = mock_module
    hardware_obj.module.run_command.return_value = (0, '5124792', '')

    hardware_obj.get_memory_facts()

    hardware_obj.module.run_command.assert_called_with("/usr/bin/vmstat | tail -1", use_unsafe_shell=True)


# Generated at 2022-06-13 00:47:18.208730
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    from ansible.module_utils.facts.hardware.hpux import HPUXHardware
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.six import PY3
    from ansible.module_utils.six.moves import StringIO


    class TestModule:
        def __init__(self, params):
            self.params = params
            self.tmpdir = tempfile.mkdtemp()
        def run_command(self, cmd, use_unsafe_shell=None, check_rc=True):
            if cmd == "/usr/bin/vmstat | tail -1":
                return(0, "search_page_dir 164589 0\n", '')

# Generated at 2022-06-13 00:47:31.622776
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hardware_collector = HPUXHardwareCollector()
    assert hardware_collector._platform == 'HP-UX'

    assert hardware_collector.required_facts == {'platform', 'distribution'}

# Generated at 2022-06-13 00:47:40.397758
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    import json
    import unittest

    class AnsibleModuleFake(object):
        def __init__(self, module_args=None):
            self.params = json.loads("{}")
            self.run_command_calls = []

# Generated at 2022-06-13 00:47:43.865019
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    instance = HPUXHardwareCollector()
    assert instance.platform == 'HP-UX'
    assert instance.required_facts == set(['platform', 'distribution'])

# Generated at 2022-06-13 00:47:52.273860
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    class FakeModule(object):
        def __init__(self):
            self.run_command = lambda x, y: (0, '', '')
    test_class = HPUXHardware([])
    setattr(test_class, 'module', FakeModule())

    test_class.populate()

    assert test_class.memfree_mb
    assert test_class.memtotal_mb
    assert test_class.swapfree_mb
    assert test_class.swaptotal_mb


# Generated at 2022-06-13 00:48:01.386030
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    test_architectures = {
        '9000/800': {
            'processor_count': 12,
            'processor': '',
            'processor_cores': 2,
        },
        '9000/785': {
            'processor_count': 8,
            'processor': '',
            'processor_cores': 2,
        },
        'ia64': {
            'processor_count': 36,
            'processor': 'Intel(R) Xeon(R) CPU E7-8860 v2 @ 2.26GHz',
            'processor_cores': 12,
        },
    }


# Generated at 2022-06-13 00:48:03.856334
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    h = HPUXHardwareCollector()
    assert h.platform == 'HP-UX'
    assert h.required_facts == {'platform', 'distribution'}
    assert h._fact_class == HPUXHardware


# Generated at 2022-06-13 00:48:10.103618
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    module = AnsibleModule(argument_spec=dict())
    hardware_collector = HPUXHardwareCollector(module=module)
    hardware = hardware_collector.collect()[0]
    assert hardware.platform == 'HP-UX'
    assert hardware.memfree_mb
    assert hardware.memtotal_mb
    assert hardware.swapfree_mb
    assert hardware.swaptotal_mb
    assert hardware.processor
    assert hardware.processor_cores
    assert hardware.processor_count
    assert hardware.model
    assert hardware.firmware_version



# Generated at 2022-06-13 00:48:17.004277
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    x = HPUXHardwareCollector()
    assert isinstance(x, HardwareCollector)
    # Class should have set _fact_class to HPUXHardware
    assert x._fact_class == HPUXHardware
    # Class should have set _platform to "HP-UX"
    assert x._platform == "HP-UX"
    # Class should have set required_facts to a set containing "platform" and "distribution"
    assert x.required_facts == set(['platform', 'distribution'])

# Generated at 2022-06-13 00:48:24.991626
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    # Create a HPUX Hardware instance and test get_hw_facts method
    collected_facts = {'platform': 'HP-UX',
                       'ansible_architecture': 'ia64',
                       'ansible_distribution_version': 'B.11.31'}
    hw = HPUXHardware()
    hw.module = MockModule()
    hw.module.run_command = Mock(return_value=(0, 'server xxxxxx', ''))

    hw_facts = hw.get_hw_facts(collected_facts)
    assert hw_facts['product_serial'] == ' xxxxxxxxxx'
    assert hw_facts['firmware_version'] == 'xxxxxxxxxxx'



# Generated at 2022-06-13 00:48:30.869744
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hpux_hardware_collector = HPUXHardwareCollector()

    assert hpux_hardware_collector._fact_class == HPUXHardware
    assert hpux_hardware_collector._platform == 'HP-UX'
    assert hpux_hardware_collector.required_facts == {'platform', 'distribution'}

# Generated at 2022-06-13 00:48:58.929527
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    module = AnsibleModule(argument_spec={})
    hardware = HPUXHardware(module)
    collected_facts = {
        'ansible_architecture': "ia64",
        'ansible_distribution_version': "B.11.31",
    }
    expected_facts = {
        'swaptotal_mb': 515,
        'memtotal_mb': 128000,
        'memfree_mb': 903,
        'swapfree_mb': 515
    }
    facts = hardware.get_memory_facts(collected_facts=collected_facts)
    assert_equal(facts, expected_facts)



# Generated at 2022-06-13 00:48:59.877714
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    HPUXHardware.get_memory_facts()

# Generated at 2022-06-13 00:49:09.075579
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    from ansible.module_utils.facts.hardware.hpux import HPUXHardware
    h = HPUXHardware('')
    # machinfo usage
    assert h.get_memory_facts(collected_facts={'ansible_architecture': 'ia64',
                                               'ansible_distribution_version': 'B.11.23'}) == {'swapfree_mb': 995,
                                                                                               'swaptotal_mb': 995,
                                                                                               'memfree_mb': 705,
                                                                                               'memtotal_mb': 773}


# Generated at 2022-06-13 00:49:18.444815
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    raw_output_ia64_23 = """
Memory : 944 MB
BMC version : 2.40
Firmware revision : A.08.00
Processor family : Intel(R) Itanium(R) Processor
System Board : HP Integrity rx4640
System Firmware revision : 1.12
System Firmware Build : 01/09/03
Machine serial number : FR3309X9G3
"""


# Generated at 2022-06-13 00:49:19.469304
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hpux = HPUXHardwareCollector()
    assert hpux.supported()

# Generated at 2022-06-13 00:49:30.957796
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    module = FakeAnsibleModule()
    module.run_command = run_command_mock
    facts_instance = HPUXHardware(module)
    facts = facts_instance.populate()
    expected_facts = {'processor': 'Intel(R) Itanium(R) Processor 9320',
                      'processor_cores': 4,
                      'processor_count': 1,
                      'memtotal_mb': 8192,
                      'memfree_mb': 5192,
                      'swapfree_mb': 1024,
                      'swaptotal_mb': 1024,
                      'model': 'rp3440',
                      'firmware_version': 'B.11.31',
                      'product_serial': 'ABCDEFGHIJ'}
    assert facts == expected_facts



# Generated at 2022-06-13 00:49:40.961374
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    collected_facts = {'ansible_distribution': 'HP-UX', 'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.31'}
    hardware_collector = HPUXHardwareCollector(module=None)
    hw_facts = hardware_collector.get_hw_facts(collected_facts=collected_facts)
    assert hw_facts['product_serial'] == '171197A9GQ'
    assert hw_facts['firmware_version'] == 'B.11.31.0703'
    assert hw_facts['model'] == 'ia64 hp server rx7640'


# Generated at 2022-06-13 00:49:49.755708
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    hw = HPUXHardware({'distribution': 'HP-UX'})
    facts = {'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.31'}
    hw.module.run_command = mock_command
    cpu_facts = hw.get_cpu_facts(facts)
    assert cpu_facts['processor'] == 'Intel(R) Itanium(R) processor 9220 1.60GHz'
    assert cpu_facts['processor_count'] == 4
    assert cpu_facts['processor_cores'] == 4


# Generated at 2022-06-13 00:49:58.956613
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=False
    )

    # B.11.31 HP-UX Itanium
    info_hw = HPUXHardware()
    collected_facts = {'ansible_architecture': 'ia64',
                       'ansible_distribution_version': 'B.11.31'}
    result = info_hw.get_cpu_facts(collected_facts)
    assert result['processor_count'] == 4
    assert result['processor_cores'] == 6
    assert result['processor'] == 'Intel(R) Itanium(R)  Processor 9350'

    # B.11.23 HP-UX Itanium

# Generated at 2022-06-13 00:50:04.290663
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    module = os
    Hardware = HPUXHardware(module)
    Hardware.module.run_command = mock_run_command
    Hardware.get_memory_facts()
    assert Hardware.facts['swaptotal_mb'] == 100
    assert Hardware.facts['swapfree_mb'] == 50
    assert Hardware.facts['memtotal_mb'] == 4096
    assert Hardware.facts['memfree_mb'] == 3072


# Generated at 2022-06-13 00:50:26.378236
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    """Test the get_memory_facts method of the HPUXHardware class"""
    hw = HPUXHardware({})

    collected_facts = {
        'ansible_architecture': '9000/800',
        'ansible_distribution': 'HP-UX',
    }

    expected_facts = {
        'memtotal_mb': 2028,
        'memfree_mb': 1205,
        'swaptotal_mb': 2016,
        'swapfree_mb': 2015,
    }


# Generated at 2022-06-13 00:50:33.608015
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    '''
    Unit test for method HPUXHardware.populate()
    '''
    # Test known combination of version and architecture
    collected_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution': 'HP-UX',
        'ansible_distribution_version': 'B.11.31',
        'platform': 'HP-UX',
        'distribution': 'HP-UX'
    }
    hw = HPUXHardware(None, collected_facts)

# Generated at 2022-06-13 00:50:42.739671
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    test_module = AnsibleModule(argument_spec={})
    test_module.params['ANSIBLE_MODULE_ARGS'] = ''
    test_module.params['ANSIBLE_MODULE_RETVAL'] = 0
    test_module.params['ANSIBLE_MODULE_SELINUX_SPECFILE'] = ''
    test_module.params['ANSIBLE_MODULE_SET_FACT'] = ''

    hw = HPUXHardware(module=test_module)
    result = hw.get_memory_facts()

    assert result['memtotal_mb'] == int(result['memtotal_mb'])
    assert result['memfree_mb'] == int(result['memfree_mb'])
    assert result['swaptotal_mb'] == int(result['swaptotal_mb'])

# Generated at 2022-06-13 00:50:48.187446
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hwc = HPUXHardwareCollector()
    assert hwc.required_facts == set(['platform', 'distribution'])
    assert hwc._fact_class == HPUXHardware
    assert hwc._platform == 'HP-UX'



# Generated at 2022-06-13 00:50:54.972941
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    hw = HPUXHardware()
    hw.module = FakeModule()
    hw.module.run_command.return_value = (0, '31416', '')
    hw.module.set_module_args({})

    hw_facts = hw.get_memory_facts()
    # memfree_mb
    assert hw_facts['memfree_mb'] == 31416
    # memtotal_mb
    hw.module.run_command.return_value = (0, '123456 123456', '')
    hw_facts = hw.get_memory_facts()
    assert hw_facts['memtotal_mb'] == 123456
    # swapfree_mb
    hw.module.run_command.return_value = (0, '65432', '')

# Generated at 2022-06-13 00:51:01.651176
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    os.environ['PAGESIZE'] = '4096'
    mock_module = MockModule()
    mock_module.run_command = Mock(return_value=(0, '     0     19     61     62     62     26     63      0      0      0', ''))
    hardware = HPUXHardware(mock_module)
    memory_facts = hardware.get_memory_facts()
    assert memory_facts.get('memfree_mb') == 4
    assert memory_facts.get('memtotal_mb') == 63



# Generated at 2022-06-13 00:51:03.210232
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    h = HPUXHardware()
    h.get_memory_facts()



# Generated at 2022-06-13 00:51:08.692650
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    hw = HPUXHardware()
    if hw:
        hw_facts = hw.get_hw_facts()
        assert hw_facts['product_name'] == 'HP-UX'
        assert hw_facts['firmware_version'] == 'B.11.11.2909'
        assert hw_facts['product_serial'] == '123456789012345'
        assert hw_facts['model'] == 'HP-UX ia64 9000/785'

# Generated at 2022-06-13 00:51:14.392394
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    module = AnsibleModule(
        argument_spec = dict(
            ansible_architecture=dict(default='ia64'),
            ansible_distribution_version=dict(default='B.11.31'),
        )
    )

    # Declare test data
    collected_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.31',
    }

    facts = HPUXHardware(module).get_hw_facts(collected_facts)
    assert facts['model'] == 'hp Workstation zx2000'
    assert facts['firmware_version'] == 'H6/0C'
    assert facts['product_serial'] == 'BNQKACB'


# Generated at 2022-06-13 00:51:24.299067
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    import sys
    import json
    import unittest
    sys.path.append('/usr/lib/python2.7/dist-packages/ansible')
    from ansible.module_utils.facts.hardware.hpx import HPUXHardware
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts import FactCollector

    from ansible.module_utils.facts.hardware.base import HardwareCollector
    from ansible.module_utils.facts.hardware.hpx import HPUXHardware

    class TestHPUXHardware_get_memory_facts(unittest.TestCase):
        def test_hpx_11_23(self):
            '''
            Test on hpux 11.23
            '''

# Generated at 2022-06-13 00:51:54.487136
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    hardware = HPUXHardware({'ansible_architecture': '9000/800'})
    hardware.module.run_command = lambda x: ('', '', '')
    hardware.module.run_command.side_effect = [
        ('', '12800', ''), ('', 'Physical: 6000 Kbytes', ''),
        ('', 'Memory =  2560 MB', ''), ('', '100100100100100100', ''),
        ('', 'dev   32        64        32        0      swap', None), # we don't care about error here
        ('', '', ''),
    ]
    assert hardware.get_memory_facts() == {
        'memfree_mb': 4, 'memtotal_mb': 2, 'swapfree_mb': 2, 'swaptotal_mb': 50,
    }

# Generated at 2022-06-13 00:52:05.129283
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    h = HPUXHardware(dict())
    rc, out, err = h.module.run_command("echo 'disable_ansible_module_hardware_collection=True' > /etc/ansible/facts.d/disable_hardware_collection.fact")
    facts = h.populate()
    assert facts['processor'] == 'Intel(R) Itanium(R) Processor 9100 series'
    assert facts['processor_cores'] == 8
    assert facts['processor_count'] == 2
    assert facts['memtotal_mb'] == 16384
    assert facts['memfree_mb'] == 15355
    assert facts['swaptotal_mb'] == 57344
    assert facts['swapfree_mb'] == 55867
    assert facts['model'] == 'ia64 hp server rx2800 i2'

# Generated at 2022-06-13 00:52:07.699401
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    hardware = HPUXHardware()
    hw_facts = hardware.get_hw_facts({'distribution': 'HP-UX', 'architecture': 'ia64'})

    assert 'model' in hw_facts
    assert 'firmware_version' in hw_facts
    assert 'product_serial' in hw_facts

# Generated at 2022-06-13 00:52:14.373593
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    mod_obj = AnsibleModule({
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.23'
    })
    collected_facts = {}
    hardware_obj = HPUXHardware(mod_obj)
    hw_facts = hardware_obj.get_hw_facts(collected_facts)

    assert hw_facts.get('firmware_version') == '412'
    assert hw_facts.get('product_serial') == 'ABC1234'

# Generated at 2022-06-13 00:52:17.428598
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    HPUXHardware = HPUXHardware()
    return HPUXHardware.get_hw_facts(collected_facts={'ansible_architecture': 'ia64',
                                                     'ansible_distribution_version': 'B.11.23'})


# Generated at 2022-06-13 00:52:24.020601
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    # Initializing arguments
    class module:
        def run_command(self, *args, **kwargs):
            if args[0] == "model":
                return (0, "HP Superdome 2", "")
            elif args[0] == "/usr/contrib/bin/machinfo | grep -i 'Firmware revision' | grep -v BMC":
                return (0, "Firmware Revision = OA R4.10", "")
            elif args[0] == "/usr/contrib/bin/machinfo | grep -i 'Machine serial number' ":
                return (0, "Machine serial number = US-xxxx-xxxx", "")
        def fail_json(self, *args, **kwargs):
            pass
    class collected_facts:
        ansible_architecture = 'ia64'


# Generated at 2022-06-13 00:52:27.396652
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hardware_collector = HPUXHardwareCollector()
    assert hardware_collector._platform == 'HP-UX'
    assert hardware_collector._fact_class == HPUXHardware
    assert hardware_collector.required_facts == {'platform', 'distribution'}

# Generated at 2022-06-13 00:52:34.480839
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    module = FakeModule({'ansible_architecture': '9000/800'})
    h = HPUXHardware(module)
    ret = h.populate()
    assert ret['processor_count'] == 1
    assert ret['swaptotal_mb'] == 1420
    assert ret['swapfree_mb'] == 1420
    assert ret['firmware_version'] == 'B.11.23'
    assert ret['model'] == 'ia64 hp server rx7640'


# Generated at 2022-06-13 00:52:41.689262
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    hpux_hardware = HPUXHardware()
    hpux_hardware.module = AnsibleModule()

    def mockrun_command(self, cmd, *args, **kwargs):
        out = 'processor       : 1\n'
        return 0, out, ""

    hpux_hardware.module.run_command = mockrun_command

    hpux_hardware.populate({'ansible_architecture': '9000/785', 'ansible_distribution': 'HP-UX'})
    assert hpux_hardware.get_cpu_facts() == {'processor_count': 1}



# Generated at 2022-06-13 00:52:51.779486
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    hpux_hardware = HPUXHardware()
    collected_facts = {'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.31'}
    hpux_hardware_facts = hpux_hardware.populate(collected_facts)
    assert hpux_hardware_facts.get('processor') == 'Intel(R) Itanium(R) processor'
    assert hpux_hardware_facts.get('processor_cores') == 4
    assert hpux_hardware_facts.get('processor_count') == 4
    assert hpux_hardware_facts.get('memtotal_mb') == 263696
    assert hpux_hardware_facts.get('memfree_mb') == 108828

# Generated at 2022-06-13 00:53:59.613912
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    module = AnsibleModule(argument_spec={})
    hw = HPUXHardware(module=module)
    facts = hw.get_facts()
    assert facts['ansible_hw_model'] == "ia64 hp server rx8640"
    assert facts['ansible_hw_firmware_version'] == "v2.22"
    assert facts['ansible_hw_product_serial'] == "US12345678"

# Generated at 2022-06-13 00:54:05.852667
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    class HPModule:
        def run_command(self, cmd, use_unsafe_shell=True):
            # Simulate the output of the machinfo command when the distribution version is B.11.23
            if "machinfo" in cmd:
                return 0, "socket            = 1\n" \
                           "processor family  = Intel(R) Itanium(R) Processor\n" \
                           "processor        = Itanium 9300 series\n" \
                           "processor id     = 4\n" \
                           "number of cores  = 2\n" \
                           "number of threads = 8\n", ""
            # Simulate the output of the ioscan command when the distribution version is B.11.23
            if "ioscan" in cmd:
                return 0, "8\n", ""
            # Simulate

# Generated at 2022-06-13 00:54:14.641057
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    module = type('DummyModule', (object,), dict(run_command=lambda x: (0, '', '')))
    mod_fact = type('DummyAnsibleModule', (object,), dict(module=module))
    hpux_hardware = HPUXHardware(mod_fact)
    collected_facts = {}
    cpu_facts = {}
    collected_facts['ansible_architecture'] = '9000/800'
    cpu_facts = hpux_hardware.get_cpu_facts(collected_facts=collected_facts)
    assert cpu_facts['processor_count'] > 0
    collected_facts['ansible_architecture'] = 'ia64'
    collected_facts['ansible_distribution_version'] = "B.11.23"
    cpu_facts = hpux_hardware.get

# Generated at 2022-06-13 00:54:22.728599
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    hpux_hw_facts = HPUXHardware()
    hpux_hw_facts.module.run_command = lambda x: (0, 'HP-UX', '')
    hpux_hw_facts.module.run_command = lambda x: (0, 'A.11.23', '')
    hpux_hw_facts.get_hw_facts()
    hpux_hw_facts.module.run_command = lambda x: (0, 'HP 9000/800', '')
    hpux_hw_facts.module.run_command = lambda x: (0, 'B.11.31', '')
    hpux_hw_facts.get_hw_facts()

# Generated at 2022-06-13 00:54:30.166272
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    """
    Validate that HPUXHardware.get_hw_facts returns serial number and firmware version
    """
    class MockModule(object):
        def __init__(self):
            self.run_command = MagicMock(return_value=(0, 'model: rp2430\n', None))

    mock_module = MockModule()

    # Create a set of hardware facts that will be returned by the hardware instance
    hardware_facts = {
        'model': 'rp2430',
        'firmware_version': 'B.11.31.1906',
        'product_serial': 'ZZZZZZZZZZZZZZ',
    }

    # Create an instance of the HPUXHardware class
    hpux_hardware = HPUXHardware(mock_module)

    # Create a dictionary of the facts that would be returned

# Generated at 2022-06-13 00:54:35.196072
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=['!all'], type='list')
        )
    )
    collected_facts = dict(
        distribution='HP-UX',
        distribution_version='B.11.23'
    )
    hardware_info = HPUXHardware(module)
    facts = hardware_info.populate(collected_facts)
    assert facts['product_serial'] ==  'ABCD1234'
    assert facts['firmware_version'] == 'V7.85'


# Generated at 2022-06-13 00:54:42.491432
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    hardware_facts = {'ansible_architecture': '9000/800'}
    module = type('', (object,), {'run_command': run_command_mock})
    hw = HPUXHardware(module)
    hw.populate(hardware_facts)
    assert_equals(hw.memory['memfree_mb'], 24)
    assert_equals(hw.memory['memtotal_mb'], 1024)
    assert_equals(hw.memory['swapfree_mb'], 32)
    assert_equals(hw.memory['swaptotal_mb'], 64)
    assert_equals(hw.cpu['processor_count'], 2)
    assert_equals(hw.cpu['processor_cores'], 1)

# Generated at 2022-06-13 00:54:50.491431
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    hardware = HPUXHardware(None)
    collected_facts = {'ansible_architecture': '9000/800'}
    memory_facts = hardware.get_memory_facts(collected_facts=collected_facts)
    assert memory_facts['memtotal_mb'] >= 0
    assert memory_facts['memfree_mb'] >= 0
    assert memory_facts['swaptotal_mb'] >= 0
    assert memory_facts['swapfree_mb'] >= 0



# Generated at 2022-06-13 00:54:56.292191
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hwc = HPUXHardwareCollector()
    assert hwc._fact_class == HPUXHardware
    assert hwc._platform == 'HP-UX'
    assert hwc.required_facts == set(['platform', 'distribution'])


# Generated at 2022-06-13 00:54:58.676800
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    assert HPUXHardwareCollector._fact_class == HPUXHardware
    assert HPUXHardwareCollector._platform == 'HP-UX'