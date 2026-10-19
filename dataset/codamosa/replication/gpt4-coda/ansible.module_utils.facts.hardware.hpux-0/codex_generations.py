

# Generated at 2024-03-18 01:21:58.186783
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():    # Mocking the module and its run_command method
    module_mock = MagicMock()
    module_mock.run_command = MagicMock()

    # Mocking the outputs of the run_command method

# Generated at 2024-03-18 01:22:04.060826
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():    # Mocking the module and its run_command method
    module_mock = MagicMock()
    module_mock.run_command = MagicMock()

    # Mocking the outputs of the run_command method

# Generated at 2024-03-18 01:22:11.980413
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():    # Mocking the module and its run_command method
    module_mock = MagicMock()
    module_mock.run_command = MagicMock()

    # Mocking the collected_facts
    collected_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.31'
    }

    # Creating an instance of HPUXHardware with the mocked module
    hpux_hardware = HPUXHardware(module=module_mock)

    # Setting up the return values for the mocked run_command method

# Generated at 2024-03-18 01:22:17.265430
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():    # Mock the HPUXHardware class
    class MockHPUXHardware(HPUXHardware):
        def __init__(self, module):
            self.module = module

        def run_command(self, command, use_unsafe_shell=False):
            if command == "ioscan -FkCprocessor | wc -l":
                return 0, "4", ""
            elif command == "/usr/contrib/bin/machinfo | grep 'Number of CPUs'":
                return 0, "Number of CPUs = 2", ""
            elif command == "/usr/contrib/bin/machinfo | grep 'processor family'":
                return 0, "processor family: Intel(R) Itanium(R) Processor 9500 series", ""

# Generated at 2024-03-18 01:22:24.501554
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():    # Mocking collected_facts with sample architecture and distribution version
    collected_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.31'
    }

    # Mocking the module and its run_command method
    module_mock = MagicMock()

# Generated at 2024-03-18 01:22:29.905985
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():    # Mocking the necessary components for the test
    from unittest.mock import MagicMock, patch

    # Create an instance of the HPUXHardware class
    hw = HPUXHardware()

    # Mock the module attribute with a MagicMock object
    hw.module = MagicMock()
    hw.module.run_command = MagicMock()

    # Define the return values for the mocked run_command method

# Generated at 2024-03-18 01:22:35.785799
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():    # Mock the HPUXHardware class
    class MockHPUXHardware(HPUXHardware):
        def __init__(self, module):
            self.module = module

        def run_command(self, command, use_unsafe_shell=False):
            if command == "ioscan -FkCprocessor | wc -l":
                return 0, "4", ""
            elif command == "/usr/contrib/bin/machinfo | grep 'Number of CPUs'":
                return 0, "Number of CPUs = 2", ""
            elif command == "/usr/contrib/bin/machinfo | grep 'processor family'":
                return 0, "processor family: Intel(R) Itanium(R) Processor 9500 series", ""

# Generated at 2024-03-18 01:22:37.464207
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():    collector = HPUXHardwareCollector()

# Generated at 2024-03-18 01:22:42.771351
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():    # Mocking the collected_facts and the module object
    collected_facts = {
        'ansible_architecture': '9000/800',
        'ansible_distribution_version': 'B.11.31'
    }
    module_mock = MagicMock()

    # Mocking the run_command method to return predefined outputs
    def run_command_side_effect(cmd, use_unsafe_shell):
        if cmd.startswith("ioscan"):
            return (0, "4\n", "")
        elif cmd.startswith("/usr/contrib/bin/machinfo"):
            if 'Number of CPUs' in cmd:
                return (0, "Number of CPUs = 2", "")
            elif 'processor family' in cmd:
                return (0, "processor family: Intel(R) Itanium 2 9100 series", "")
            elif 'logical' in cmd:
                return (0, "2 logical processors (2 per socket)", "")

# Generated at 2024-03-18 01:22:49.057162
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():    # Mock the module and its run_command method
    module_mock = MagicMock()
    module_mock.run_command = MagicMock()

    # Create an instance of the HPUXHardware class with the mocked module
    hpux_hardware = HPUXHardware(module=module_mock)

    # Define the collected_facts to be used in the test
    collected_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.31'
    }

    # Set up the expected command and its output for the test case
    expected_command = "/usr/contrib/bin/machinfo | grep 'Number of CPUs'"
    expected_output = "Number of CPUs = 4\n"
    module_mock.run_command.return_value = (0, expected_output, '')

    # Call the method under test
    cpu_facts = hpux_hardware.get_cpu_facts(collected_facts=collected_facts)

    #

# Generated at 2024-03-18 01:23:02.379922
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():    collector = HPUXHardwareCollector()

# Generated at 2024-03-18 01:23:04.044803
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():    collector = HPUXHardwareCollector()

# Generated at 2024-03-18 01:23:09.249037
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():    # Mocking the module and its run_command method
    module_mock = MagicMock()
    module_mock.run_command = MagicMock()

    # Mocking the collected_facts dictionary
    collected_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.31'
    }

    # Creating an instance of HPUXHardware with the mocked module
    hpux_hardware = HPUXHardware(module=module_mock)

    # Setting up the return values for the mocked run_command method

# Generated at 2024-03-18 01:23:10.855019
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():    collector = HPUXHardwareCollector()

# Generated at 2024-03-18 01:23:19.924007
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():    # Mocking the module and its run_command method
    module_mock = MagicMock()
    module_mock.run_command = MagicMock()

    # Mocking the output of run_command for different scenarios

# Generated at 2024-03-18 01:23:22.371536
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():    collector = HPUXHardwareCollector()

# Generated at 2024-03-18 01:23:28.113318
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():    # Mocking the module and its run_command method
    module_mock = MagicMock()
    module_mock.run_command = MagicMock()

    # Mocking the collected_facts with a specific architecture and distribution version
    collected_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.31'
    }

    # Creating an instance of HPUXHardware with the mocked module
    hpux_hardware = HPUXHardware(module=module_mock)

    # Mocking the output of run_command for different commands

# Generated at 2024-03-18 01:23:33.249811
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():    # Mocking the module and its run_command method
    module_mock = MagicMock()
    module_mock.run_command = MagicMock()

    # Mocking the collected_facts dictionary
    collected_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.31'
    }

    # Creating an instance of HPUXHardware with the mocked module
    hpux_hardware = HPUXHardware(module=module_mock)

    # Setting up the return values for the mocked run_command method

# Generated at 2024-03-18 01:23:35.691950
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():    collector = HPUXHardwareCollector()

# Generated at 2024-03-18 01:23:42.155956
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():    # Mocking the module and its run_command method
    module_mock = MagicMock()
    module_mock.run_command = MagicMock()

    # Mocking the collected_facts with a specific architecture and distribution version
    collected_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.31'
    }

    # Creating an instance of HPUXHardware with the mocked module
    hpux_hardware = HPUXHardware(module=module_mock)

    # Mocking the output of run_command for different commands

# Generated at 2024-03-18 01:24:17.581165
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():    # Mocking collected_facts with sample architecture and distribution version
    collected_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.31'
    }

    # Mocking the module and its run_command method
    module_mock = MagicMock()

# Generated at 2024-03-18 01:24:23.196075
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():    # Mocking the necessary components for the test
    from unittest.mock import MagicMock, patch

    # Create an instance of the HPUXHardware class
    hw = HPUXHardware()

    # Mock the module attribute with a MagicMock object
    hw.module = MagicMock()
    hw.module.run_command = MagicMock()

    # Define the return values for the mocked run_command method

# Generated at 2024-03-18 01:24:28.112471
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():    # Mocking the necessary components for the test
    from unittest.mock import MagicMock, patch

    # Create an instance of the HPUXHardware class
    hw = HPUXHardware()

    # Mock the module attribute with a MagicMock object
    hw.module = MagicMock()
    hw.module.run_command = MagicMock()

    # Define the return values for the mocked run_command method

# Generated at 2024-03-18 01:24:35.359595
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():    # Mocking the module and its run_command method
    module_mock = MagicMock()
    module_mock.run_command = MagicMock()

    # Mocking the collected_facts with a specific architecture and distribution version
    collected_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.31'
    }

    # Creating an instance of HPUXHardware with the mocked module
    hpux_hardware = HPUXHardware(module=module_mock)

    # Mocking the output of run_command for different commands

# Generated at 2024-03-18 01:24:43.559694
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():    # Mocking the module and its run_command method
    module_mock = MagicMock()
    module_mock.run_command = MagicMock()

    # Mocking the collected_facts with architecture and distribution version
    collected_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.31'
    }

    # Creating an instance of HPUXHardware with the mocked module
    hpux_hardware = HPUXHardware(module=module_mock)

    # Setting up the return values for the mocked run_command method
    module_mock.run_command.side_effect = [
        (0, "model output", ""),
        (0, "Firmware revision: 20.20", ""),
        (0, "Machine serial number: MY12345678", "")
    ]

    # Calling the get_hw_facts method

# Generated at 2024-03-18 01:24:50.821410
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():    # Mocking the necessary components for the test
    from unittest.mock import MagicMock, patch

    # Create an instance of the HPUXHardware class
    hw = HPUXHardware()

    # Mock the module attribute with a MagicMock object
    hw.module = MagicMock()
    hw.module.run_command = MagicMock()

    # Define the return values for the mocked run_command method

# Generated at 2024-03-18 01:24:52.535999
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():    collector = HPUXHardwareCollector()

# Generated at 2024-03-18 01:24:58.285572
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():    # Mocking the module and its run_command method
    module_mock = MagicMock()
    module_mock.run_command = MagicMock()

    # Mocking the os.access function
    with patch('os.access', return_value=True):
        # Creating an instance of HPUXHardware
        hpux_hardware = HPUXHardware(module=module_mock)

        # Mocking the output of run_command for different commands

# Generated at 2024-03-18 01:25:00.518924
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():    collector = HPUXHardwareCollector()

# Generated at 2024-03-18 01:25:07.019232
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():    # Mocking the collected_facts dictionary
    collected_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.31'
    }

    # Mocking the module object and its run_command method
    module_mock = MagicMock()

# Generated at 2024-03-18 01:26:16.663600
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():    # Mocking the module and its run_command method
    module_mock = MagicMock()
    module_mock.run_command = MagicMock()

    # Mocking the collected_facts dictionary
    collected_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.31'
    }

    # Creating an instance of HPUXHardware with the mocked module
    hpux_hardware = HPUXHardware(module=module_mock)

    # Setting up the return values for the mocked run_command method

# Generated at 2024-03-18 01:26:22.923282
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():    # Mocking collected_facts for testing purposes
    collected_facts = {
        'ansible_architecture': '9000/800',
        'ansible_distribution_version': 'B.11.31'
    }

    # Mocking the module and its run_command method
    module_mock = MagicMock()

# Generated at 2024-03-18 01:26:25.176948
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():    collector = HPUXHardwareCollector()

# Generated at 2024-03-18 01:26:31.938716
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():    # Mocking the HPUXHardware class and its dependencies
    module_mock = MagicMock()
    module_mock.run_command = MagicMock(side_effect=[
        (0, "  0  0  0  0  0  1234", ""),  # Mock vmstat output
        (0, "Physical: 8388608 Kbytes", ""),  # Mock grep Physical output
        (0, "8388608", ""),  # Mock adb output
        (0, "Memory = 16384 MB (15.999 GB)", ""),  # Mock machinfo output for Memory
        (0, "16384", ""),  # Mock swapinfo -q output
        (0, "dev  1  16384  8192", "")  # Mock swapinfo detailed output
    ])

    # Create an instance of the HPUXHardware class

# Generated at 2024-03-18 01:26:34.117637
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():    collector = HPUXHardwareCollector()

# Generated at 2024-03-18 01:26:40.767643
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():    # Mock the module and its run_command method
    module_mock = MagicMock()
    module_mock.run_command = MagicMock()

    # Create an instance of HPUXHardware with the mocked module
    hpux_hardware = HPUXHardware(module=module_mock)

    # Define the collected_facts to be used in the test
    collected_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.31'
    }

    # Set up the expected command and its output for the test case
    expected_command = "/usr/contrib/bin/machinfo | grep 'Number of CPUs'"
    expected_output = "Number of CPUs = 4\n"
    module_mock.run_command.return_value = (0, expected_output, '')

    # Call the method under test
    cpu_facts = hpux_hardware.get_cpu_facts(collected_facts=collected_facts)

    # Assert that

# Generated at 2024-03-18 01:26:42.268466
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():    collector = HPUXHardwareCollector()

# Generated at 2024-03-18 01:26:49.710093
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():    # Mocking collected_facts with sample architecture and distribution version
    collected_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.31'
    }

    # Mocking the module and its run_command method
    module_mock = MagicMock()

# Generated at 2024-03-18 01:26:54.448588
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():    # Mocking the module and its run_command method
    module_mock = MagicMock()
    module_mock.run_command = MagicMock()

    # Mocking the collected_facts
    collected_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.23'
    }

    # Creating an instance of HPUXHardware
    hpux_hardware = HPUXHardware(module=module_mock)

    # Setting up the return values for the mocked run_command
    module_mock.run_command.side_effect = [
        (0, "model output", ""),
        (0, "Firmware revision: 20.34", ""),
        (0, "Machine serial number: ABC1234567", "")
    ]

    # Calling the method to test
    hw_facts = hpux_hardware.get_hw_facts(collected_facts=collected_facts)

    # Assertions to validate the method functionality

# Generated at 2024-03-18 01:27:00.909584
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():    # Mocking the module and its run_command method
    module_mock = MagicMock()
    module_mock.run_command = MagicMock()

    # Mocking the collected_facts
    collected_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': "B.11.23"
    }

    # Creating an instance of HPUXHardware with the mocked module
    hpux_hardware = HPUXHardware(module=module_mock)

    # Setting up the return values for the mocked run_command method
    module_mock.run_command.side_effect = [
        (0, "model output", ""),
        (0, "Firmware revision: 20.34", ""),
        (0, "Machine serial number: ABC1234567", "")
    ]

    # Calling the get_hw_facts method
    hw_facts = hpux_hardware.get_hw_facts(collected_facts=collected_facts)

    # Assertions to

# Generated at 2024-03-18 01:29:10.669031
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():    # Mocking the module and its run_command method
    module_mock = MagicMock()
    module_mock.run_command = MagicMock()

    # Mocking the collected_facts with a specific architecture and distribution version
    collected_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.31'
    }

    # Creating an instance of HPUXHardware with the mocked module
    hpux_hardware = HPUXHardware(module=module_mock)

    # Mocking the output of run_command for different commands

# Generated at 2024-03-18 01:29:16.000160
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():    # Mocking the module and its run_command method
    module_mock = MagicMock()
    module_mock.run_command = MagicMock()

    # Mocking os.access to simulate /dev/kmem access

# Generated at 2024-03-18 01:29:17.719020
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():    collector = HPUXHardwareCollector()

# Generated at 2024-03-18 01:29:23.493837
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():    # Mocking the module and its run_command method
    module_mock = MagicMock()
    module_mock.run_command = MagicMock()

    # Mocking the outputs of the run_command method

# Generated at 2024-03-18 01:29:29.587745
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():    # Mocking the module and its run_command method
    module_mock = MagicMock()
    module_mock.run_command = MagicMock()

    # Mocking the collected_facts with a specific architecture and distribution version
    collected_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.31'
    }

    # Creating an instance of HPUXHardware with the mocked module
    hpux_hardware = HPUXHardware(module=module_mock)

    # Mocking the output of run_command for different commands

# Generated at 2024-03-18 01:29:36.935777
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():    # Mocking the module and its run_command method
    module_mock = MagicMock()
    module_mock.run_command = MagicMock()

    # Mocking the collected_facts
    collected_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': "B.11.23"
    }

    # Creating an instance of HPUXHardware
    hpux_hardware = HPUXHardware(module=module_mock)

    # Setting up the return values for the mocked run_command method
    module_mock.run_command.side_effect = [
        (0, "model output", ""),
        (0, "Firmware revision: 20.34", ""),
        (0, "Machine serial number: MXQ1234567", "")
    ]

    # Calling the get_hw_facts method
    hw_facts = hpux_hardware.get_hw_facts(collected_facts=collected_facts)

    # Assertions to check if the

# Generated at 2024-03-18 01:29:41.793812
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():    # Mocking the module and its run_command method
    module_mock = MagicMock()
    module_mock.run_command = MagicMock()

    # Mocking the outputs of the run_command method

# Generated at 2024-03-18 01:29:48.307340
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():    # Mocking the module and its run_command method
    module_mock = MagicMock()
    module_mock.run_command = MagicMock()

    # Creating an instance of HPUXHardware
    hpux_hardware = HPUXHardware(module=module_mock)

    # Mocking collected facts
    collected_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': "B.11.23"
    }

    # Setting up the return values for the mocked run_command method
    module_mock.run_command.side_effect = [
        (0, "model output", ""),
        (0, "Firmware revision: 20.20", ""),
        (0, "Machine serial number: ABC1234567", "")
    ]

    # Calling the method under test
    hw_facts = hpux_hardware.get_hw_facts(collected_facts=collected_facts)

    # Assertions to validate the returned hardware facts

# Generated at 2024-03-18 01:29:54.255182
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():    # Mocking the HPUXHardware class and its dependencies
    module_mock = MagicMock()
    module_mock.run_command = MagicMock(side_effect=[
        (0, "  5  0  0  0  0  1234", ""),  # Mock vmstat output
        (0, "Physical: 8388608 Kbytes", ""),  # Mock grep Physical output
        (0, "8388608", ""),  # Mock adb output
        (0, "Memory = 16384 MB (15.999 GB)", ""),  # Mock machinfo output for memtotal_mb
        (0, "16384", ""),  # Mock swapinfo -q output
        (0, "dev  1  1024  16384  0  0", "")  # Mock swapinfo detailed output
    ])

    # Create an instance of the HPUXHardware class
   

# Generated at 2024-03-18 01:30:00.758466
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():    # Mocking the module and its run_command method
    module_mock = MagicMock()
    module_mock.run_command = MagicMock()

    # Mocking the collected_facts
    collected_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': "B.11.23"
    }

    # Creating an instance of HPUXHardware with the mocked module
    hpux_hardware = HPUXHardware(module=module_mock)

    # Setting up the return values for the mocked run_command method
    module_mock.run_command.side_effect = [
        (0, "model output", ""),
        (0, "Firmware revision: 20.34", ""),
        (0, "Machine serial number: ABC1234567", "")
    ]

    # Calling the get_hw_facts method
    hw_facts = hpux_hardware.get_hw_facts(collected_facts=collected_facts)

    # Assertions to