

# Generated at 2024-05-31 02:29:51.308529
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():    module = type('obj', (object,), {'run_command': lambda self, cmd, use_unsafe_shell: (0, '4', '')})

# Generated at 2024-05-31 02:29:52.488330
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():    collector = HPUXHardwareCollector()

# Generated at 2024-05-31 02:29:55.584512
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    module = Mock()
    module.run_command = Mock(return_value=(0, "model_output", ""))
    collected_facts = {'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.23'}
    hpux_hardware = HPUXHardware(module)
    hw_facts = hpux_hardware.get_hw_facts(collected_facts=collected_facts)
    assert hw_facts['model'] == "model_output"
    module.run_command.assert_any_call("model")
    module.run_command.assert_any_call("/usr/contrib/bin/machinfo |grep -i 'Firmware revision' | grep -v BMC", use_unsafe_shell=True)
    module.run_command.assert_any_call("/usr/contrib/bin/machinfo |grep -i 'Machine serial number' ", use_unsafe_shell=True)

# Generated at 2024-05-31 02:29:57.404727
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():    module = type('obj', (object,), {'run_command': lambda self, cmd, use_unsafe_shell: (0, 'Memory: 8192 MB', '')})

# Generated at 2024-05-31 02:29:59.300252
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():    module = type('obj', (object,), {'run_command': lambda self, cmd, use_unsafe_shell: (0, '4', '')})

# Generated at 2024-05-31 02:30:01.929446
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():    module = type('module', (object,), {'run_command': lambda self, cmd, use_unsafe_shell: (0, '4', '')})

# Generated at 2024-05-31 02:30:03.296924
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():    collector = HPUXHardwareCollector()

# Generated at 2024-05-31 02:30:05.214703
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():    module = type('obj', (object,), {'run_command': lambda self, cmd, use_unsafe_shell: (0, 'Memory: 8192 MB', '')})

# Generated at 2024-05-31 02:30:14.244162
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():    module = type('obj', (object,), {'run_command': lambda self, cmd, use_unsafe_shell: (0, '4', '')})

# Generated at 2024-05-31 02:30:18.442697
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():    hpux_hardware = HPUXHardware(module=None)

# Generated at 2024-05-31 02:30:29.031114
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():    collector = HPUXHardwareCollector()

# Generated at 2024-05-31 02:30:32.199151
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():    module = type('obj', (object,), {'run_command': lambda self, cmd, use_unsafe_shell: (0, 'MockedModelOutput', '')})

# Generated at 2024-05-31 02:30:34.034061
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():    collector = HPUXHardwareCollector()

# Generated at 2024-05-31 02:30:37.660692
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():    module = type('module', (object,), {'run_command': lambda self, cmd, use_unsafe_shell: (0, '4', '')})()

# Generated at 2024-05-31 02:30:44.487651
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():    module = type('obj', (object,), {'run_command': lambda self, cmd, use_unsafe_shell: (0, 'MockedModelOutput', '')})

# Generated at 2024-05-31 02:30:51.098450
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():    module = type('obj', (object,), {'run_command': lambda self, cmd, use_unsafe_shell: (0, 'MockedModelOutput', '')})

# Generated at 2024-05-31 02:30:52.906321
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():    collector = HPUXHardwareCollector()

# Generated at 2024-05-31 02:30:57.259908
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():    module = type('obj', (object,), {'run_command': lambda self, cmd, use_unsafe_shell: (0, 'Memory: 8192 MB', '')})

# Generated at 2024-05-31 02:30:59.672609
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():    module = type('obj', (object,), {'run_command': lambda self, cmd, use_unsafe_shell: (0, 'Memory: 8192 MB', '')})

# Generated at 2024-05-31 02:31:04.202914
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():    hpux_hardware = HPUXHardware(module=None)

# Generated at 2024-05-31 02:31:27.337716
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():    hpux_hardware = HPUXHardware(module=None)

# Generated at 2024-05-31 02:31:29.480054
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():    module = type('obj', (object,), {'run_command': lambda self, cmd, use_unsafe_shell: (0, '4', '')})

# Generated at 2024-05-31 02:31:30.686588
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    collector = HPUXHardwareCollector()
    assert collector._fact_class == HPUXHardware
    assert collector._platform == 'HP-UX'
    assert collector.required_facts == set(['platform', 'distribution'])

# Generated at 2024-05-31 02:31:36.903964
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():    module = type('obj', (object,), {'run_command': lambda self, cmd, use_unsafe_shell: (0, 'MockModel\nMockFirmware\nMockSerial\n', '')})

# Generated at 2024-05-31 02:31:37.954897
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():    collector = HPUXHardwareCollector()

# Generated at 2024-05-31 02:31:41.442387
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():    module = type('obj', (object,), {'run_command': lambda self, cmd, use_unsafe_shell: (0, '4', '')})

# Generated at 2024-05-31 02:31:43.598623
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():    module = type('obj', (object,), {'run_command': lambda self, cmd, use_unsafe_shell: (0, 'Memory = 8192 MB', '')})

# Generated at 2024-05-31 02:31:44.995912
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():    collector = HPUXHardwareCollector()

# Generated at 2024-05-31 02:31:46.356931
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():    collector = HPUXHardwareCollector()

# Generated at 2024-05-31 02:31:48.938568
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():    module = type('obj', (object,), {'run_command': lambda self, cmd, use_unsafe_shell: (0, '4', '')})

# Generated at 2024-05-31 02:32:21.408522
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():    collector = HPUXHardwareCollector()

# Generated at 2024-05-31 02:32:23.136430
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():    collector = HPUXHardwareCollector()

# Generated at 2024-05-31 02:32:24.260989
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    collector = HPUXHardwareCollector()
    assert collector._fact_class == HPUXHardware
    assert collector._platform == 'HP-UX'
    assert collector.required_facts == set(['platform', 'distribution'])

# Generated at 2024-05-31 02:32:26.917095
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():    module = type('obj', (object,), {'run_command': lambda self, cmd, use_unsafe_shell: (0, 'MockModel\nMockFirmware\nMockSerial\n', '')})

# Generated at 2024-05-31 02:32:30.636937
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():    module = Mock()

# Generated at 2024-05-31 02:32:34.572740
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():    module = type('obj', (object,), {'run_command': lambda self, cmd, use_unsafe_shell: (0, 'MockedModelOutput', '')})

# Generated at 2024-05-31 02:32:35.761164
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():    collector = HPUXHardwareCollector()

# Generated at 2024-05-31 02:32:36.812148
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():    collector = HPUXHardwareCollector()

# Generated at 2024-05-31 02:32:39.132619
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():    module = type('obj', (object,), {'run_command': lambda self, cmd, use_unsafe_shell: (0, 'Memory = 8192 MB', '')})

# Generated at 2024-05-31 02:32:40.619638
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():    collector = HPUXHardwareCollector()

# Generated at 2024-05-31 02:33:13.889803
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():    module = type('obj', (object,), {'run_command': lambda self, cmd, use_unsafe_shell: (0, '4', '')})

# Generated at 2024-05-31 02:33:15.185042
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():    collector = HPUXHardwareCollector()

# Generated at 2024-05-31 02:33:19.563960
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():    module = type('module', (object,), {'run_command': lambda self, cmd, use_unsafe_shell: (0, '4', '')})

# Generated at 2024-05-31 02:33:21.909830
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():    module = type('obj', (object,), {'run_command': lambda self, cmd, use_unsafe_shell: (0, '4', '')})

# Generated at 2024-05-31 02:33:24.605715
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    module = Mock()
    module.run_command = Mock(side_effect=[
        (0, "HP-UX model", ""),
        (0, "Firmware revision: 1.2.3", ""),
        (0, "Machine serial number: ABC123", "")
    ])
    collected_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.23'
    }
    hpux_hardware = HPUXHardware(module)
    hw_facts = hpux_hardware.get_hw_facts(collected_facts=collected_facts)
    assert hw_facts['model'] == "HP-UX model"
    assert hw_facts['firmware_version'] == "1.2.3"
    assert hw_facts['product_serial'] == "ABC123"

# Generated at 2024-05-31 02:33:27.136146
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():    module = type('obj', (object,), {'run_command': lambda self, cmd, use_unsafe_shell: (0, 'Memory: 8192 MB', '')})

# Generated at 2024-05-31 02:33:30.050899
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():    module = type('obj', (object,), {'run_command': lambda self, cmd, use_unsafe_shell: (0, 'MockedModel\nMockedFirmware\nMockedSerial\n', '')})

# Generated at 2024-05-31 02:33:31.388764
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():    collector = HPUXHardwareCollector()

# Generated at 2024-05-31 02:33:33.000212
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():    collector = HPUXHardwareCollector()

# Generated at 2024-05-31 02:33:35.687233
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():    module = type('obj', (object,), {'run_command': lambda self, cmd, use_unsafe_shell: (0, '4', '')})

# Generated at 2024-05-31 02:34:39.302417
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():    module = type('obj', (object,), {'run_command': lambda self, cmd, use_unsafe_shell: (0, 'MockModel\nMockFirmware\nMockSerial\n', '')})

# Generated at 2024-05-31 02:34:40.812249
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():    collector = HPUXHardwareCollector()

# Generated at 2024-05-31 02:34:44.465600
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():    module = type('obj', (object,), {'run_command': lambda self, cmd, use_unsafe_shell: (0, 'Memory = 8192 MB', '')})

# Generated at 2024-05-31 02:34:45.720991
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():    collector = HPUXHardwareCollector()

# Generated at 2024-05-31 02:34:49.454075
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():    module = type('module', (object,), {'run_command': lambda self, cmd, use_unsafe_shell: (0, '4', '')})

# Generated at 2024-05-31 02:34:52.354387
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():    module = type('obj', (object,), {'run_command': lambda self, cmd, use_unsafe_shell: (0, '4', '')})

# Generated at 2024-05-31 02:34:55.063503
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():    module = type('module', (object,), {'run_command': lambda self, cmd, use_unsafe_shell: (0, 'MockModel\nMockFirmware\nMockSerial\n', '')})

# Generated at 2024-05-31 02:34:58.708357
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():    module = type('module', (object,), {'run_command': lambda self, cmd, use_unsafe_shell: (0, '4', '')})

# Generated at 2024-05-31 02:35:00.888109
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():    collector = HPUXHardwareCollector()

# Generated at 2024-05-31 02:35:03.581234
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():    module = type('obj', (object,), {'run_command': lambda self, cmd, use_unsafe_shell: (0, '4', '')})

# Generated at 2024-05-31 02:36:05.338040
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():    collector = HPUXHardwareCollector()

# Generated at 2024-05-31 02:36:10.830278
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():    hpux_hardware = HPUXHardware(module=None)

# Generated at 2024-05-31 02:36:13.310605
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():    module = type('obj', (object,), {'run_command': lambda self, cmd, use_unsafe_shell: (0, 'Memory: 8192 MB', '')})

# Generated at 2024-05-31 02:36:16.648618
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():    module = type('obj', (object,), {'run_command': lambda self, cmd, use_unsafe_shell: (0, '4', '')})

# Generated at 2024-05-31 02:36:19.383187
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():    module = type('obj', (object,), {'run_command': lambda self, cmd, use_unsafe_shell: (0, '4', '')})

# Generated at 2024-05-31 02:36:20.692374
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():    collector = HPUXHardwareCollector()

# Generated at 2024-05-31 02:36:22.884606
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():    module = type('obj', (object,), {'run_command': lambda self, cmd, use_unsafe_shell: (0, '4', '')})

# Generated at 2024-05-31 02:36:26.615518
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():    module = type('obj', (object,), {'run_command': lambda self, cmd, use_unsafe_shell: (0, 'Memory: 8192 MB', '')})

# Generated at 2024-05-31 02:36:28.387887
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():    collector = HPUXHardwareCollector()

# Generated at 2024-05-31 02:36:33.156252
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():    hpux_hardware = HPUXHardware(module=None)

# Generated at 2024-05-31 02:38:39.978368
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():    module = type('obj', (object,), {'run_command': lambda self, cmd, use_unsafe_shell: (0, '4', '')})

# Generated at 2024-05-31 02:38:43.492257
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():    module = type('module', (object,), {'run_command': lambda self, cmd, use_unsafe_shell: (0, '4', '')})

# Generated at 2024-05-31 02:38:49.021879
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():    module = Mock()

# Generated at 2024-05-31 02:38:52.189915
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():    module = type('obj', (object,), {'run_command': lambda self, cmd, use_unsafe_shell: (0, '4', '')})

# Generated at 2024-05-31 02:38:54.015543
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():    collector = HPUXHardwareCollector()

# Generated at 2024-05-31 02:38:57.818763
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():    module = type('obj', (object,), {'run_command': lambda self, cmd, use_unsafe_shell: (0, '4', '')})

# Generated at 2024-05-31 02:39:01.692947
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():    module = type('obj', (object,), {'run_command': lambda self, cmd, use_unsafe_shell: (0, 'Model Output\n', '')})

# Generated at 2024-05-31 02:39:07.132927
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():    module = type('obj', (object,), {'run_command': lambda self, cmd, use_unsafe_shell: (0, '4', '')})

# Generated at 2024-05-31 02:39:12.185672
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():    hpux_hardware = HPUXHardware(module=None)

# Generated at 2024-05-31 02:39:15.307573
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():    module = type('obj', (object,), {'run_command': lambda self, cmd, use_unsafe_shell: (0, 'Memory: 8192 MB', '')})