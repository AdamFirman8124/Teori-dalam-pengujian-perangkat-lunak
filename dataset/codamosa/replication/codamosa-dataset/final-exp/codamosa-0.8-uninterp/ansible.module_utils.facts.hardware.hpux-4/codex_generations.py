

# Generated at 2022-06-13 00:45:28.480140
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    """Check that the constructor of class HPUXHardwareCollector works as expected"""

    my_HPUXHardwareCollector = HPUXHardwareCollector()
    assert my_HPUXHardwareCollector is not None
    assert my_HPUXHardwareCollector._platform == 'HP-UX'
    assert my_HPUXHardwareCollector._fact_class == HPUXHardware
    assert my_HPUXHardwareCollector.required_facts == set(['platform', 'distribution'])


# Generated at 2022-06-13 00:45:35.755288
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    module = AnsibleModule(argument_spec={})
    hardware = HPUXHardware(module=module)
    facts = hardware.populate()
    # Check cpu facts
    assert facts['processor_count'] != {}
    assert facts['processor_cores'] != {}
    assert facts['processor'] != {}
    # Check memory facts
    assert facts['memtotal_mb'] != {}
    assert facts['memfree_mb'] != {}
    assert facts['swaptotal_mb'] != {}
    assert facts['swapfree_mb'] != {}
    # Check hw facts
    assert facts['model'] != {}
    assert facts['firmware_version'] != {}
    assert facts['product_serial'] != {}

# Generated at 2022-06-13 00:45:48.531423
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    """
    This test uses mocked functions and classes.
    Mocking is not necessary, but this way we are not dependent on the output of commands.
    """
    module = None
    hpux_hardware = HPUXHardware(module)

    # Mocked function 'run_command'
    def run_command(command, use_unsafe_shell=False):
        if command == "model":
            return (0, "Rack Mount 110", "")
        else:
            return (-1, "", "")

    hpux_hardware.module.run_command = run_command
    hw_facts = hpux_hardware.get_hw_facts()
    assert "model" in hw_facts
    assert hw_facts["model"] == "Rack Mount 110"
    assert "product_serial" not in hw_facts

# Generated at 2022-06-13 00:45:57.533384
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    facts = {
        'ansible_architecture': '9000/800',
        'ansible_distribution': 'HP-UX',
        'ansible_distribution_major_version': 'B',
        'ansible_distribution_version': 'B.11.31'}
    hardware = HPUXHardware(module=None, facts=facts)
    memory_facts = hardware.get_memory_facts()
    expected_memory_facts = {'memfree_mb': 6455, 'memtotal_mb': 25056, 'swapfree_mb': 0, 'swaptotal_mb': 184320}
    assert memory_facts == expected_memory_facts

# Generated at 2022-06-13 00:46:08.492227
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    module = AnsibleModule(argument_spec={})
    hardware = HPUXHardware(module)

    # Note: create a temporary file with these contents.
    mock_out = ''
    # Note: create a temporary file with these contents.
    mock_err = ''

    # Note: created a mock object
    mock_run_command = MagicMock(side_effect=[(0, mock_out, mock_err), (0, mock_out, mock_err), (0, mock_out, mock_err)])
    hardware.module.run_command = mock_run_command

    # This is what we expect to be returned
    memtotal_mb = 4096
    memfree_mb = 4095
    swaptotal_mb = 4095
    swapfree_mb = 4095

# Generated at 2022-06-13 00:46:14.214339
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    module = MockModule()
    module.run_command = Mock(return_value=(0, "HP-UX", ""))
    collected_facts = {'ansible_architecture':'ia64', 'ansible_distribution':'HP-UX', 'ansible_distribution_version':'B.11.31'}
    hw = HPUXHardware(module)
    hw.fill_facter_facts(collected_facts)
    res = hw.get_hw_facts()
    assert res['model'] == 'HP-UX'



# Generated at 2022-06-13 00:46:24.269442
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    hux = HPUXHardware({'ansible_architecture': 'ia64'})
    # test B.11.23
    assert hux.get_memory_facts({'ansible_distribution_version': 'B.11.23'}) == {'memfree_mb': 3152, 'memtotal_mb': 8192, 'swaptotal_mb': 1017, 'swapfree_mb': 1017}
    # test B.11.31
    assert hux.get_memory_facts({'ansible_distribution_version': 'B.11.31'}) == {'memfree_mb': 3184, 'memtotal_mb': 32768, 'swaptotal_mb': 1017, 'swapfree_mb': 1017}



# Generated at 2022-06-13 00:46:28.626376
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hpuxHardwareCollector = HPUXHardwareCollector()
    assert hpuxHardwareCollector.platform == "HP-UX"
    assert 'distribution' in hpuxHardwareCollector.required_facts
    assert 'platform' in hpuxHardwareCollector.required_facts
    assert isinstance(hpuxHardwareCollector.get_facts(), HPUXHardware)

# Generated at 2022-06-13 00:46:35.002192
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    hw = HPUXHardware()
    rc, out, err = hw.module.run_command("/usr/bin/uname -m")
    collected_facts = {}
    collected_facts['ansible_architecture'] = out.strip()
    data = hw.get_cpu_facts(collected_facts)
    assert 'processor_count' in data
    assert 'processor_cores' in data
    assert 'processor' in data


# Generated at 2022-06-13 00:46:38.714303
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    param = {}
    facts = {'ansible_architecture': '9000/800', 'ansible_distribution': 'HP-UX'}
    hw = HPUXHardware(param, facts)
    cpu_facts = hw.get_cpu_facts(collected_facts=facts)
    assert cpu_facts['processor_count'] == 2


# Generated at 2022-06-13 00:46:57.373063
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    from ansible.module_utils.facts.hardware.hpux import HPUXHardware
    import json
    test_name_1 = "test_HPUXHardware_get_cpu_facts_PARISC_1"
    test_file_name_1 = test_name_1 + ".json"
    test_name_2 = "test_HPUXHardware_get_cpu_facts_PARISC_2"
    test_file_name_2 = test_name_2 + ".json"
    test_name_3 = "test_HPUXHardware_get_cpu_facts_ia64_1"
    test_file_name_3 = test_name_3 + ".json"
    test_name_4 = "test_HPUXHardware_get_cpu_facts_ia64_2"
    test_file_name_4

# Generated at 2022-06-13 00:47:02.439773
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    from ansible.module_utils.facts.hardware.hpux import HPUXHardware
    from ansible.module_utils.facts import Facts
    # test for uname release B.11.23
    facts = Facts({'ansible_architecture': 'ia64', 'ansible_distribution': 'HP-UX', 'ansible_distribution_version': 'B.11.23'})
    hardware = HPUXHardware(facts)
    assert hardware.get_memory_facts() == {'swapfree_mb': 76, 'memfree_mb': 2912, 'swaptotal_mb': 76, 'memtotal_mb': 6454}
    # test for uname release B.11.31 < 1204

# Generated at 2022-06-13 00:47:05.039369
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hardware_collector = HPUXHardwareCollector({})

    assert hardware_collector.required_facts == set(['platform', 'distribution'])

# Generated at 2022-06-13 00:47:13.628450
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    host = {}
    hardware_object = HPUXHardware(module=None, host=host)
    hardware_object.get_memory_facts()
    hardware_object.get_memory_facts(collected_facts={'ansible_architecture': '9000/785'})
    hardware_object.get_memory_facts(collected_facts={'ansible_architecture': 'ia64'})
    hardware_object.get_memory_facts(collected_facts={'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.31'})
    hardware_object.get_memory_facts(collected_facts={'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.23'})



# Generated at 2022-06-13 00:47:17.174640
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    test_facter = HPUXHardware({})
    test_facter.module = {"run_command": mock_run_command}
    facts = test_facter.get_hw_facts()
    assert facts['model'] == 'ia64 hp server rx4640'
    assert facts['firmware_version'] == 'HPD3'
    assert facts['product_serial'] == 'US123456789'



# Generated at 2022-06-13 00:47:18.855831
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    """ Constructor HPUXHardwareCollector: should call parent class and set
    required facts.
    """

    obj = HPUXHardwareCollector()
    assert obj.required_facts == {'platform', 'distribution'}

# Generated at 2022-06-13 00:47:22.993000
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    hpux_hw = HPUXHardware()
    collected_facts = {'ansible_architecture': '9000/800'}
    cpu_facts = hpux_hw.get_cpu_facts(collected_facts=collected_facts)[0]

    assert cpu_facts['processor_count'] == 8

    collected_facts = {'ansible_architecture': 'ia64'}
    collected_facts.update({'ansible_distribution_version': 'B.11.31'})
    memory_facts = hpux_hw.get_cpu_facts(collected_facts=collected_facts)[0]
    assert memory_facts['processor_count'] == 8



# Generated at 2022-06-13 00:47:33.339685
# Unit test for method get_hw_facts of class HPUXHardware

# Generated at 2022-06-13 00:47:39.860656
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    inst = HPUXHardware
    inst.module = type('_test_module', (object,), dict(run_command=lambda *args, **kwargs: (0, 'HP rx8620 IA64 rx8620-1000084541', '')))
    collected_facts = {'ansible_architecture': 'ia64',
                       'ansible_distribution_version': 'B.11.23'}
    facts = inst.get_hw_facts(collected_facts)
    assert facts == {'model': 'HP rx8620', 'firmware_version': '3.50'}

# Generated at 2022-06-13 00:47:41.890765
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():

    '''
    Unit test
    '''

    test_collector = HPUXHardwareCollector()
    assert test_collector.__class__.__name__ == 'HPUXHardwareCollector'


# Generated at 2022-06-13 00:48:03.587246
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    hardware = HPUXHardware()
    # Test on HP-UX 11.00
    hardware.module = type("AnsibleModule", (object,), dict(run_command=lambda self, cmd: (0, "test", "")))
    hardware.get_memory_facts()
    assert hardware.facts['memfree_mb'] == 0
    assert hardware.facts['memtotal_mb'] == 0
    assert hardware.facts['swaptotal_mb'] == 0
    assert hardware.facts['swapfree_mb'] == 0

    # Test on HP-UX 11.11
    hardware.module = type("AnsibleModule", (object,), dict(run_command=lambda self, cmd, use_unsafe_shell=True: (0, "test", "")))
    hardware.get_memory_facts()

# Generated at 2022-06-13 00:48:08.158771
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hpux_hw_collector = HPUXHardwareCollector()
    assert hpux_hw_collector.platform == 'HP-UX'
    assert hpux_hw_collector.required_facts == {'platform', 'distribution'}
    assert hpux_hw_collector.fact_class == HPUXHardware

# Generated at 2022-06-13 00:48:18.188468
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    # Test for method get_memory_facts()

    # Arrange
    # Define the collected_facts
    collected_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.31'
    }

    # Define the expected result
    expected = {
        'memfree_mb': 13,
        'memtotal_mb': 6,
    }

    # Act
    test_HPUXHardware = HPUXHardware()
    # Tested function gets the cmd, so we mock it

# Generated at 2022-06-13 00:48:22.133163
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    """Unit test for `HPUXHardware.populate` method."""
    # Initialize the class to be tested
    module = type('AnsibleModuleStub', (object,), {'run_command': run_command_stub})
    hw = HPUXHardware(module, 'test-hostname')

    # Create a simple test case, which return valid datas
    def run_command_stub(*args, **kw):
        (rc, out, err) = (0, '0', '')
        return (rc, out, err)

    # Perform the test
    res = hw.populate({'ansible_architecture': '9000/800'})


# Generated at 2022-06-13 00:48:32.862569
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    hardware = HPUXHardware(None)
    collected_facts = {'ansible_architecture': '9000/800'}
    hardware.get_memory_facts(collected_facts) == {'memfree_mb': 1497, 'swaptotal_mb': 0, 'swapfree_mb': 0, 'memtotal_mb': 6071}
    collected_facts['ansible_architecture'] = 'ia64'
    hardware.get_memory_facts(collected_facts) == {'memfree_mb': 1497, 'swaptotal_mb': 0, 'swapfree_mb': 0, 'memtotal_mb': 6071}
    collected_facts['ansible_architecture'] = '9000/foo'

# Generated at 2022-06-13 00:48:42.961319
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    test_obj = HPUXHardware()
    collected_facts = {"ansible_architecture": "9000/785"}
    cpu_facts = {'processor_count': 4}
    assert test_obj.get_cpu_facts(collected_facts=collected_facts) == cpu_facts
    collected_facts = {"ansible_architecture": "ia64"}
    cpu_facts = {'processor_cores': 4, 'processor_count': 4, 'processor': 'Intel(R) Itanium(R) Processor 9100 series'}
    assert test_obj.get_cpu_facts(collected_facts=collected_facts) == cpu_facts
    collected_facts = {"ansible_architecture": "ia64", "ansible_distribution_version": "B.11.31"}

# Generated at 2022-06-13 00:48:44.670760
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hardware_collector = HPUXHardwareCollector()
    assert hardware_collector.platform == 'HP-UX'
    assert hardware_collector.fact_class == HPUXHardware



# Generated at 2022-06-13 00:48:50.310469
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    hardware = HPUXHardware(dict(ansible_architecture='9000/800', ansible_distribution='HP-UX'))
    result = hardware.get_cpu_facts()
    assert result.get('processor_count') == 2

# Generated at 2022-06-13 00:49:01.882335
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    # Calling HPUXHardware class
    hw = HPUXHardware({'hw_facts': {'ansible_architecture': 'ia64',
                                    'ansible_distribution_version': 'B.11.31'}})
    hw_facts = hw.get_hw_facts()
    # Assert hardware facts
    assert hw_facts['firmware_version'] == 'P63'
    assert hw_facts['product_serial'] == 'MYMACHINE'

    # Calling HPUXHardware class
    hw = HPUXHardware({'hw_facts': {'ansible_architecture': 'ia64',
                                    'ansible_distribution_version': 'B.11.23'}})
    hw_facts = hw.get_hw_facts()
    # Assert hardware facts

# Generated at 2022-06-13 00:49:04.887541
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hardwareCollector = HPUXHardwareCollector(None)

    # Test __init__
    assert hardwareCollector._platform == 'HP-UX'
    assert hardwareCollector.required_facts == set(['platform', 'distribution'])



# Generated at 2022-06-13 00:49:31.710078
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    my_hw = HPUXHardware()

    # Test get_memory_facts method on HP-UX 9000/800
    data = '''
Mem:           0K             0K             0K             0K
Swap:       49152K             0K        49152K             0K
'''
    my_hw.module.run_command = lambda *args, **kwargs: (0, data, '')
    result = my_hw.get_memory_facts()
    assert result['memtotal_mb'] == 0
    assert result['memfree_mb'] == 0
    assert result['swaptotal_mb'] == 48
    assert result['swapfree_mb'] == 48

    # Test get_memory_facts method on HP-UX ia64

# Generated at 2022-06-13 00:49:43.108419
# Unit test for method get_cpu_facts of class HPUXHardware

# Generated at 2022-06-13 00:49:53.631639
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    """Unit test for method get_hw_facts of class HPUXHardware"""
    hw = HPUXHardware({})

    hw.module.run_command = lambda x: ('', '', '')
    assert 'firmware_version' not in hw.get_hw_facts()
    assert 'product_serial' not in hw.get_hw_facts()

    hw.module.run_command = lambda x: ('0', 'HPUX', '')
    assert 'firmware_version' in hw.get_hw_facts()
    assert 'product_serial' in hw.get_hw_facts()

    hw.module.run_command = lambda x: ('2', 'HPUX', '')
    assert 'firmware_version' not in hw.get_hw_facts()

# Generated at 2022-06-13 00:50:01.144142
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    hw = HPUXHardware({})
    collected_facts = dict()

    # Test case : 11.23, ia64
    collected_facts['ansible_architecture'] = 'ia64'
    collected_facts['ansible_distribution_version'] = 'B.11.23'
    hw_facts = hw.get_hw_facts(collected_facts)
    assert hw_facts['model'] == 'HP Integrity rx2800 i4'
    assert hw_facts['firmware_version'] == '1.0'

    # Test case : 11.31, ia64
    collected_facts['ansible_architecture'] = 'ia64'
    collected_facts['ansible_distribution_version'] = 'B.11.31'
    hw_facts = hw.get_hw

# Generated at 2022-06-13 00:50:05.007861
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hpux_collector = HPUXHardwareCollector()
    assert hpux_collector.platform == 'HP-UX'
    assert hpux_collector.required_facts == set(['platform', 'distribution'])
    assert hpux_collector._fact_class == HPUXHardware

# Generated at 2022-06-13 00:50:14.859152
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    # Set up test input
    fake_collected_facts = {'ansible_architecture': '9000\/800'}
    fake_module = FakeAnsibleModule()
    fake_module.run_command.return_value = (0, '     0 nfsswap', '')
    fake_module.run_command.return_value = (0, 'swap_pages_free:         42', '')
    fake_module.run_command.return_value = (0, 'Physical:  524288 Kbytes', '')
    # Run method
    results = HPUXHardware.get_memory_facts(fake_module, fake_collected_facts)
    # Check results
    assert results['memfree_mb'] == 1032
    assert results['swaptotal_mb'] == 0

# Generated at 2022-06-13 00:50:18.385097
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    # Test with required facts known
    required_facts = {'platform': 'HP-UX', 'distribution': 'HPUX'}
    hpux = HPUXHardwareCollector(required_facts)
    assert hpux._platform == 'HP-UX'
    assert hpux.required_facts == set(['platform', 'distribution'])

# Generated at 2022-06-13 00:50:22.970202
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    module = type('testmodule', (object,), {'run_command': get_run_command_return_value})

    module_instance = HPUXHardware()
    module_instance.module = module
    collected_facts = {'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.31'}

    memory_facts = module_instance.get_memory_facts(collected_facts)
    assert memory_facts == {'memfree_mb': 1200, 'memtotal_mb': 1234, 'swaptotal_mb': 34, 'swapfree_mb': 1}



# Generated at 2022-06-13 00:50:32.553584
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    module = AnsibleModule(argument_spec={})
    hw = HPUXHardware(module)

    rc, out, err = module.run_command("model")
    model = out.strip()
    rc, out, err = module.run_command("/usr/contrib/bin/machinfo |grep -i 'Firmware revision' | grep -v BMC")
    firmware_version = out.strip().split(':')[1].strip()
    rc, out, err = module.run_command("/usr/contrib/bin/machinfo |grep -i 'Machine serial number' ")
    product_serial = out.strip().split(':')[1].strip()


# Generated at 2022-06-13 00:50:42.206196
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    # Mock
    class MockModule:
        def run_command(self, cmd, use_unsafe_shell=False):
            if cmd == "ioscan -FkCprocessor | wc -l":
                return 0, "4\n", None
            elif cmd == "/usr/contrib/bin/machinfo | grep 'Number of CPUs'":
                return 0, "Number of CPUs = 4\n", None
            elif cmd == "/usr/contrib/bin/machinfo | grep 'processor family'":
                return 0, "processor family : Intel(R) Xeon(R) CPU  E5-2650  0 @ 2.00GHz\n", None
        # Return values for tests on HP-UX B.11.31

# Generated at 2022-06-13 00:51:05.140456
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    test_data = {}
    test_data['ansible_distribution_version'] = 'B.11.23'
    test_data['ansible_architecture'] = 'ia64'
    test_data['ansible_distribution'] = 'HP-UX'
    h = HPUXHardware(None, test_data)
    hw = h.get_hw_facts()
    assert hw['firmware_version'] == 'B.11.23'
    assert hw['product_serial'] == 'QA18C58796'



# Generated at 2022-06-13 00:51:15.761260
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec={})
    module.params = {'path': '/usr/bin:/bin'}
    instance = HPUXHardware(module=module)
    cpu_facts = {'processor_count': 2, 'processor_cores': 2, 'processor': 'Intel(R) Itanium 2 9100 series processor'}
    assert instance.get_cpu_facts(
        collected_facts=dict(ansible_architecture="ia64", ansible_distribution_version="B.11.31")) == cpu_facts
    cpu_facts = {'processor_cores': 2, 'processor_count': 2}
    assert instance.get_cpu_facts(
        collected_facts=dict(ansible_architecture="9000/800", ansible_distribution_version="B.11.31")) == cpu_

# Generated at 2022-06-13 00:51:18.010226
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hwc = HPUXHardwareCollector(HPUXHardware)
    assert hwc._fact_class == HPUXHardware
    assert hwc._platform == 'HP-UX'


# Generated at 2022-06-13 00:51:25.960672
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    """
    Test method get_cpu_facts of class HPUXHardware
    """
    hardware = HPUXHardware(dict())
    hw_facts = hardware.get_cpu_facts(collected_facts={'ansible_architecture': '9000/800',
                                                       'ansible_distribution_version': 'B.11.23'})
    assert hw_facts['processor_count'] == 1
    assert hw_facts['processor'] == 'Intel(R) Itanium 2 processor'
    assert hw_facts['processor_cores'] == 1

    hw_facts = hardware.get_cpu_facts(collected_facts={'ansible_architecture': 'ia64',
                                                       'ansible_distribution_version': 'B.11.23'})

# Generated at 2022-06-13 00:51:30.567522
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hw_module = HPUXHardwareCollector()
    assert hw_module is not None
    assert hw_module._platform == 'HP-UX'
    assert hw_module._fact_class.platform == 'HP-UX'
    assert hw_module.required_facts == set(['platform', 'distribution'])

# Generated at 2022-06-13 00:51:40.391280
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    pag = 4096
    # send back 6 pages free to simulate 512MB of free mem
    module = AnsibleModule(dict(files=dict(kmem='/dev/null')))
    module.run_command = MagicMock(return_value=(0, "unused\nunused\n un unsed\n unused\n unused\n unused\n 6\n unused", ""))
    hardware = HPUXHardware(module)
    collected_facts = {'ansible_architecture': '9000/785'}
    hardware.populate(collected_facts)
    assert hardware.memfree_mb == pag // 1024 // 1024 * 6
    # send back "Memory       =14984 MB" and no Physical line to simulate 14984MB of mem

# Generated at 2022-06-13 00:51:43.486811
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    module = AnsibleModule(argument_spec={})
    facts = HPUXHardware().get_hw_facts({'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.23'})
    assert facts == {
        'model': 'ia64 hp server rx4640',
        'firmware_version': 'AB.11.00',
        'product_serial': 'USHAH1'
    }

# Generated at 2022-06-13 00:51:51.740449
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    results = {}

    results['ansible_architecture'] = 'ia64'
    results['ansible_distribution_version'] = 'B.11.23'
    results['ansible_distribution'] = 'HP-UX'
    results['ansible_system'] = 'HP-UX'

    hpc = HPUXHardwareCollector(results)


# Generated at 2022-06-13 00:51:55.828531
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    module = AnsibleModule(argument_spec=dict())
    hardware_obj = HPUXHardware(module)
    collected_facts = {'ansible_architecture': 'ia64'}
    memory_facts_result = hardware_obj.get_memory_facts(collected_facts=collected_facts)
    assert memory_facts_result['memtotal_mb'] == 127000
    assert memory_facts_result['memfree_mb'] == 87
    assert memory_facts_result['swaptotal_mb'] == 32767
    assert memory_facts_result['swapfree_mb'] == 32767



# Generated at 2022-06-13 00:52:05.265959
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    # Test with platform 'ia64', distribution_version 'B.11.23' and architecture '9000/800' or '9000/785'
    cpu_facts = HPUXHardware.get_cpu_facts(None, collected_facts={'ansible_architecture': '9000/800',
                                                                  'ansible_ia64': 'ia64',
                                                                  'ansible_distribution_version': 'B.11.23'})
    assert cpu_facts['processor_count'] == 24
    assert cpu_facts['processor_cores'] == 12
    assert cpu_facts['processor'] == 'Intel Itanium2'
    # Test with platform 'ia64', distribution_version 'B.11.31' and architecture 'ia64'

# Generated at 2022-06-13 00:52:25.935415
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    hw = HPUXHardware({})
    collected_facts = {'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.23'}

    rc, out, err = hw.module.run_command.return_value = (0,
                                                         "Separator = ':'\nFirmware revision : 825\nMachine serial number : 6XJ\n", None)
    hw_facts = hw.get_hw_facts(collected_facts=collected_facts)
    assert hw_facts == {'firmware_version': '825', 'product_serial': '6XJ'}

    # Newer version of machinfo
    collected_facts['ansible_distribution_version'] = 'B.11.31'


# Generated at 2022-06-13 00:52:29.164147
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    required_facts = set(['platform', 'distribution'])

    h = HPUXHardwareCollector()
    assert h._fact_class == HPUXHardware
    assert h._platform == 'HP-UX'
    assert h.required_facts == required_facts

# Unit tests for class HPUXHardware

# Generated at 2022-06-13 00:52:39.194751
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    import os
    import sys
    import shutil
    import tempfile
    import textwrap

    tempdir = tempfile.mkdtemp()

    # setup module arguments
    args = dict(
        ansible_facts=dict(ansible_architecture='ia64', ansible_distribution_version='B.11.31'),
        _ansible_tmpdir=tempdir,
        _ansible_keep_remote_files=False,
    )

    # Prepare test setup data

# Generated at 2022-06-13 00:52:40.163932
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    h = HPUXHardwareCollector()
    assert h.platform == 'HP-UX'

# Generated at 2022-06-13 00:52:50.184630
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    """
    Collection of tests for the get_cpu_facts method of the HPUXHardware
    class.
    """

    # The following facts are needed for the method to function correctly.
    # The variables themselves are not valid values and are only used for
    # testing purposes
    collected_facts = {
        'ansible_architecture': '9000/800',
        'ansible_distribution_version': 'B.11.23',
    }

    hw = HPUXHardware(None)
    cpu_facts = hw.get_cpu_facts(collected_facts=collected_facts)

    assert 'processor_count' in cpu_facts
    assert cpu_facts['processor_count'] > 0

    hw = HPUXHardware(None)

# Generated at 2022-06-13 00:52:53.221291
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hardware_collector = HPUXHardwareCollector()

    assert hardware_collector is not None
    assert hardware_collector._fact_class == HPUXHardware
    assert hardware_collector._platform == 'HP-UX'
    assert hardware_collector.required_facts == set(['platform', 'distribution'])

# Generated at 2022-06-13 00:53:01.878401
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    test_module = AnsibleModule(
        argument_spec={
            'gather_subset': dict(default=['!all'], type='list'),
        },
        supports_check_mode=True)


# Generated at 2022-06-13 00:53:07.933992
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    # Default facts from ansible (hardware fact could be different on each HP-UX system)
    collected_facts = {
        'ansible_facts': {
            'ansible_architecture': '9000/785',
            'ansible_distribution': 'HP-UX'
        }
    }
    # Expected returned hash
    expected_memory_facts = {
        'memfree_mb': 437,
        'memtotal_mb': 511,
        'swaptotal_mb': 0,
        'swapfree_mb': 0
    }
    # Instance of Hardware class
    hw = HPUXHardware()
    # Call method
    memory_facts = hw.get_memory_facts(collected_facts=collected_facts)
    # Check if method return expected hash

# Generated at 2022-06-13 00:53:14.906510
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    module = AnsibleModule(argument_spec={})
    har = HPUXHardware(module)

    # Test memory facts
    # Test CPU facts
    # Test HW facts
    # Test architecture 9000/800
    r = har.populate({'platform': 'HP-UX', 'ansible_distribution': 'HP-UX', 'ansible_architecture': '9000/800',
                      'ansible_distribution_version': 'B.11.11'})
    assert r['processor_count'] == 1
    assert r['processor_cores'] == 1
    assert r['processor'] == 'PA-RISC 1.1'
    assert r['memtotal_mb'] > 0
    assert r['memfree_mb'] > 0
    assert r['swaptotal_mb'] > 0
    assert r['swapfree_mb']

# Generated at 2022-06-13 00:53:16.744827
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    c = HPUXHardwareCollector()
    assert c.required_facts == set(['platform', 'distribution'])

# Generated at 2022-06-13 00:54:02.566989
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    """

    Check the facts got from HPUXHardware

    """
    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=['!all'], type='list')
        ),
        supports_check_mode=True)

    if not module.check_mode:
        hpux_hardware_facts = HPUXHardware(module).populate()
    else:
        hpux_hardware_facts = dict(
            ansible_facts=dict(
                ansible_architecture="ia64",
                ansible_distribution="HP-UX",
                ansible_distribution_version="B.11.23",
            )
        )


# Generated at 2022-06-13 00:54:08.118606
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    module = AnsibleModule(argument_spec={'gather_subset': dict(type='list', default=['all'])})
    result = HPUXHardwareCollector(module=module).collect()
    assert result is not None, "test_HPUXHardwareCollector: Constructor of class HPUXHardwareCollector has returned 'None'."
    assert type(result) is dict, "test_HPUXHardwareCollector: Constructor of class HPUXHardwareCollector has not returned a dictionary."

# Generated at 2022-06-13 00:54:15.314999
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    memory_facts = HPUXHardware().get_memory_facts()
    assert memory_facts.get('memfree_mb') is not None
    assert type(memory_facts['memfree_mb']) is int
    assert memory_facts.get('memtotal_mb') is not None
    assert type(memory_facts['memtotal_mb']) is int
    assert memory_facts.get('swaptotal_mb') is not None
    assert type(memory_facts['swaptotal_mb']) is int
    assert memory_facts.get('swapfree_mb') is not None
    assert type(memory_facts['swapfree_mb']) is int

# Generated at 2022-06-13 00:54:24.462677
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    facts = {'ansible_architecture': '9000/800', 'ansible_distribution': 'HP-UX'}
    hw = HPUXHardware(module=None, facts=facts)
    assert hw.get_memory_facts() == {'memfree_mb': 5144, 'memtotal_mb': 16384, 'swaptotal_mb': 1537, 'swapfree_mb': 1537}
    facts = {'ansible_architecture': '9000/800', 'ansible_distribution_version': 'B.11.22', 'ansible_distribution': 'HP-UX'}
    hw = HPUXHardware(module=None, facts=facts)

# Generated at 2022-06-13 00:54:27.481262
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    module = FakeModule()
    module.run_command = lambda x: (0, 'BL870c i2', '')
    hw_facts = HPUXHardware(module).get_hw_facts()
    assert hw_facts['model'] == 'BL870c i2'


# Generated at 2022-06-13 00:54:35.937962
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    m = HPUXHardware({})
    assert 'processor_count' in m.get_cpu_facts({
        'ansible_architecture': '9000/800'
    })
    assert m.get_cpu_facts({
        'ansible_architecture': '9000/800'
    }).get('processor_count') == 2
    assert 'processor_cores' in m.get_cpu_facts({
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.23'
    })
    assert 'processor' in m.get_cpu_facts({
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.23'
    })

# Generated at 2022-06-13 00:54:42.290283
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    module = Mock()
    module.run_command.return_value = (0, '', '')
    hpux_hw = HPUXHardware(module)
    collected_facts = {'ansible_architecture': 'ia64'}
    cpu_facts = hpux_hw.get_cpu_facts(collected_facts=collected_facts)
    assert cpu_facts == {'processor_count': 2}
    collected_facts = {'ansible_architecture': '9000/800'}
    cpu_facts = hpux_hw.get_cpu_facts(collected_facts=collected_facts)
    assert cpu_facts == {'processor_count': 2}


# Generated at 2022-06-13 00:54:47.558731
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    hardware = HPUXHardware()
    cpu_facts = hardware.get_cpu_facts(collected_facts={'ansible_architecture': 'hppa', 'ansible_distribution_version': 'B.11.23'})
    assert cpu_facts['processor_count'] == 1

# Generated at 2022-06-13 00:54:51.169921
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hw_facts = HPUXHardwareCollector()
    assert hw_facts._fact_class is not None
    assert hw_facts._platform is not None
    assert hw_facts.required_facts == {'platform', 'distribution'}

# Generated at 2022-06-13 00:55:01.478524
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    collected_facts = dict(ansible_architecture='9000/800')