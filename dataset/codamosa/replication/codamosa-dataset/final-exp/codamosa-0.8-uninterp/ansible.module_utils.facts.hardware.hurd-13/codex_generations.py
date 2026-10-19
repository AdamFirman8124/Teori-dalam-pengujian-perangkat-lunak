

# Generated at 2022-06-13 00:55:42.078200
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # Create mock object and skip __init__ method
    facts = HurdHardware()
    facts.populate()
    assert facts.populate is not None

# Generated at 2022-06-13 00:55:49.985516
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    from ansible.module_utils.facts.hardware.linux import LinuxHardware
    from ansible.module_utils.facts.hardware.linux import LinuxHardwareCollector
    from ansible.module_utils.facts.timeout import TimeoutError

    class MockHurdHardware(HurdHardware):

        def get_uptime_facts(self):
            return {'uptime_seconds': 42}

        def get_memory_facts(self):
            return {'ansible_memtotal_mb': 42}

        def get_mount_facts(self):
            raise TimeoutError()

    hurd_hardware = MockHurdHardware('/fake_dir')
    facts = hurd_hardware.populate()
    assert facts['uptime_seconds'] == 42
    assert facts['ansible_memtotal_mb'] == 42

# Generated at 2022-06-13 00:55:51.843006
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    facts = {}
    HurdHardware.populate(facts)


if __name__ == '__main__':
    test_HurdHardware_populate()

# Generated at 2022-06-13 00:55:59.191760
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """
    Test whether method populate of HurdHardware builds correct dictionary
    """
    import os
    from ansible.module_utils.facts import hardware

    testfile = open(os.path.join(
        os.path.dirname(__file__), '../../data/facts/Hurd/test-procfs'))

    _linux_hardware = hardware.HurdHardware()
    _linux_hardware.meminfo_procfs = testfile
    result = _linux_hardware.populate()

    assert result['uptime'] == '15762957.36'

    assert result['memtotal_mb'] == '8188.015625'
    assert result['memtotal_kb'] == '8376872.0'
    assert result['memtotal'] == '8376872'

# Generated at 2022-06-13 00:55:59.962633
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd = HurdHardware()
    hurd.populate()


# Generated at 2022-06-13 00:56:05.119514
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """
    This method tests method populate of class HurdHardware.

    It mocks grub_default_facts, distro_facts and mount facts to
    test wheather the method returns expected results or not.

    It will fail if the expected value and returned value by method
    populate do not match.
    """

    class MockHurdHardware(HurdHardware):

        def _collect_mount_facts(self):
            return {
                '/': 'ext4',
                '/boot': 'ext4',
                '/boot/efi': 'vfat',
                '/shared': 'nfs4'
            }

        def _collect_uptime_facts(self):
            return {'uptime_seconds': 5479, 'uptime_days': 0}


# Generated at 2022-06-13 00:56:11.498357
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    test_obj = HurdHardware()
    from ansible.module_utils.facts.collector import FactsCollector
    facts_collector = FactsCollector()
    facts_collector.collect(['hardware'], test_obj, True)
    facts_dict = facts_collector.get_facts()
    assert 'uptime_seconds' in facts_dict['ansible_facts']
    assert 'ansible_memtotal_mb' in facts_dict['ansible_facts']
    assert 'ansible_mounts' in facts_dict['ansible_facts']

# Generated at 2022-06-13 00:56:12.904697
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hw = HurdHardware()
    sw = hw.populate()

    print(sw)

# Generated at 2022-06-13 00:56:15.855263
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hw = HurdHardware()
    hw.populate()
    assert "uptime" in hw.facts
    assert "memfree_mb" in hw.facts
    assert "swapfree_mb" in hw.facts
    assert "mounts" in hw.facts


# Generated at 2022-06-13 00:56:24.574431
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hd = HurdHardware()
    result = hd.populate()

    assert isinstance(result, dict) == True
    assert isinstance(result['uptime'], int) == True
    assert isinstance(result['memfree_mb'], int) == True
    assert isinstance(result['memtotal_mb'], int) == True

    assert isinstance(result['mounts'], list) == True
    assert isinstance(result['mounts'][0], dict) == True
    assert isinstance(result['mounts'][0]['mount'], str) == True
    assert isinstance(result['mounts'][0]['device'], str) == True
    assert isinstance(result['mounts'][0]['fstype'], str) == True



# Generated at 2022-06-13 00:56:29.725192
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # check if HurdHardware.populate does not return empty dictionary
    hurd_hardware = HurdHardware()
    popul = hurd_hardware.populate()
    assert isinstance(popul, dict)
    assert popul != {}

# Generated at 2022-06-13 00:56:40.012984
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # Setup
    facts = {}
    hw = HurdHardware()
    hw.get_uptime_facts = lambda x = None: {'uptime_seconds': '300'}
    hw.get_memory_facts = lambda x = None: {'memtotal_mb': '1024', 'memfree_mb': '768'}
    hw.get_mount_facts = lambda x = None: {'mounts': ['/dev/sda on /boot']}

    # Exercise
    facts.update(hw.populate())

    # Verify
    assert facts['uptime_seconds'] == 300
    assert facts['memtotal_mb'] == 1024
    assert facts['memfree_mb'] == 768
    assert facts['mounts'] == ['/dev/sda on /boot']



# Generated at 2022-06-13 00:56:49.889536
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # Case: no timeout on _get_mount_facts call
    hurdhw = HurdHardware()
    hurdhw._get_mount_facts = lambda: {"mnt_facts": 1}
    hurdhw._get_memory_facts = lambda: {"mem_facts": 2}
    hurdhw._get_uptime_facts = lambda: {"uptime_facts": 3}
    facts = hurdhw.populate({})
    assert facts == {"uptime_facts": 3, "mem_facts": 2, "mnt_facts": 1}

    # Case: timeout on _get_mount_facts call
    hurdhw = HurdHardware()
    hurdhw._get_mount_facts = lambda: raise_TimeOutError()
    hurdhw._get_memory_facts = lambda: {"mem_facts": 2}

# Generated at 2022-06-13 00:56:55.527058
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    collector = HurdHardwareCollector()
    fact_class = collector._fact_class
    fact_class.get_mount_facts = lambda : {}
    fact_class.get_uptime_facts = lambda : {}
    fact_class.get_memory_facts = lambda : {}

    #pylint: disable=protected-access
    assert collector._fact_class.populate() == {}

# Generated at 2022-06-13 00:57:03.074626
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    from ansible.module_utils.facts.hardware.linux import LinuxHardware
    from ansible.module_utils.facts.timeout import TimeoutError

    hurd_hardware = HurdHardware()

    # Test uptime facts
    assert hurd_hardware.get_uptime_facts() == \
           LinuxHardware().get_uptime_facts()

    # Test memory facts
    assert hurd_hardware.get_memory_facts() == \
           LinuxHardware().get_memory_facts()

    # Test mount facts (fails with timeout)
    hurd_hardware.get_mount_facts = lambda: {}
    LinuxHardware.get_mount_facts = lambda _self: {}
    assert hurd_hardware.get_mount_facts() == \
           LinuxHardware().get_mount_facts()

    # Test hardware facts (all ok)
    hurd

# Generated at 2022-06-13 00:57:08.148858
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    collected_facts = {}
    hardware = HurdHardware()
    hardware_facts = hardware.populate(collected_facts=collected_facts)

    assert hardware_facts['uptime_seconds'] > 0
    assert hardware_facts['uptime_hours'] > 0
    assert hardware_facts['uptime_days'] > 0
    assert hardware_facts['total_physical_mem'] > 0

# Generated at 2022-06-13 00:57:16.640656
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    import inspect
    import os
    import pytest
    import re
    import json

    # ToDo: Introduce a fake module providing a mocked populate method.
    # Currently, the HurdHardware module and its test suite depend on the
    # LinuxHardware module to be present in the same directory. To avoid a
    # circular import, the test suite will import the LinuxHardware module
    # under a different name. Once the LinuxHardware module has been
    # refactored, the HurdHardware test suite can be cleaned up.
    #
    # As is, the LinuxHardware module has been refactored to use
    # HardwareCollector, so it is imported as HardwareCollector.
    #
    # The following code can be removed, once the LinuxHardware module does
    # not have to be listed as a dependency in the requirements file anymore.
    _path = os.path

# Generated at 2022-06-13 00:57:27.092671
# Unit test for method populate of class HurdHardware

# Generated at 2022-06-13 00:57:29.639713
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # Init helper class
    hw = HurdHardware()
    # Call the populate method
    return hw.populate()

# Generated at 2022-06-13 00:57:34.383446
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    from ansible.module_utils import basic
    from ansible.module_utils.facts import collector

    # Create a fact collector object
    facts_collector = collector.get_collector("HurdHardwareCollector")()

    # Create a mock AnsibleModule object
    mock_ansible_module = basic.AnsibleModule(argument_spec={})

    # Run the code to be tested
    facts_collector.populate(mock_ansible_module)

    # Assert that the value of ansible_mounts is correct
    ansible_mounts = mock_ansible_module.exit_json["ansible_facts"]["ansible_mounts"]

# Generated at 2022-06-13 00:57:37.798717
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    h = HurdHardware()
    assert h.populate()

# Generated at 2022-06-13 00:57:45.097642
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    h = HurdHardware()
    facts = h.populate()

    assert facts['uptime_seconds'] is not None
    assert facts['uptime_days'] is not None

    assert facts['memtotal_mb'] is not None
    assert facts['memfree_mb'] is not None
    assert facts['real_memory']['total'] is not None
    assert facts['real_memory']['free'] is not None

    assert facts['mounts']['/']['device'] is not None



# Generated at 2022-06-13 00:57:50.469695
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    from ansible.module_utils.facts import ansible_collector
    ansible_collector.collector._collected_facts = dict()
    hw = HurdHardware()
    hw.populate()
    assert "memory" in ansible_collector.collector._collected_facts
    assert ansible_collector.collector._collected_facts["memory"]["total"] > 0
    assert "uptime" in ansible_collector.collector._collected_facts
    assert "mounts" in ansible_collector.collector._collected_facts

# Generated at 2022-06-13 00:57:55.885215
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """
    Test correct facts are set for GNU Hurd.
    """
    facts = HurdHardware().populate()

    assert facts['uptime_seconds'] > 0
    assert 'swapfree_mb' in facts
    assert 'memfree_mb' in facts
    assert 'memtotal_mb' in facts
    assert facts['mounts'] > 0

# Generated at 2022-06-13 00:57:56.899567
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    pass

# Generated at 2022-06-13 00:58:02.227009
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    fact_class = HurdHardware()

    # Test with empty collected_facts
    facts = fact_class.populate()

    # Test that expected keys are present in facts
    assert 'uptime_seconds' in facts
    assert 'memfree_mb' in facts
    assert 'swapfree_mb' in facts
    assert 'mounts' in facts

# Generated at 2022-06-13 00:58:04.773146
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurdhardware = HurdHardware()
    hurdhardware.populate()

# Generated at 2022-06-13 00:58:13.768231
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    from ansible.module_utils.facts.facts import Facts

    # Test with an empty ansible_facts.
    fact_col = Facts(dict(), 'foo')
    fact_obj = HurdHardware(fact_col)
    facts_result = fact_obj.populate()

    assert facts_result['uptime_seconds'] > 0
    assert facts_result['uptime_days'] > 0

    assert facts_result['memtotal_mb'] > 0
    assert facts_result['memfree_mb'] > 0
    assert facts_result['swaptotal_mb'] == 0
    assert facts_result['swapfree_mb'] == 0

    assert facts_result['mounted_dev'] == '/dev/sda1'
    assert facts_result['mounted_size_gb'] > 0
    assert facts_result['mounted_used_gb']

# Generated at 2022-06-13 00:58:14.913146
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    f = HurdHardware()
    assert f.populate()

# Generated at 2022-06-13 00:58:23.735869
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    from ansible.module_utils.facts.hardware.linux import LinuxHardware
    from ansible.module_utils.facts.timeout import TimeoutError

    class MockHurdHardware(HurdHardware):
        """
        Mock class for testing of GNU Hurd populate method.
        """
        def get_uptime_facts(self):
            return {'uptime_seconds': 90}

        def get_memory_facts(self):
            return {'memtotal_mb': 1000}

        def get_mount_facts(self):
            raise TimeoutError

    mock_hurd_hardware = MockHurdHardware()
    populated_facts = mock_hurd_hardware.populate()

    # Asserting existence of uptime facts
    assert 'uptime_seconds' in populated_facts

# Generated at 2022-06-13 00:58:29.754544
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """
    test case for HurdHardware.populate method
    """
    from ansible.module_utils.facts.hardware import Hardware
    from ansible.module_utils.facts.hardware.hurd import HurdHardware

    hurdhw = HurdHardware()
    Hardware.dict_to_keyval(hurdhw.populate())

# Generated at 2022-06-13 00:58:36.845049
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # Check if the populate method correctly collects information from the
    # /proc virtual filesystem.
    from ansible.module_utils.facts.hardware.linux import TimeoutError
    from collections import namedtuple

    def get_os_vendor_mock():
        # Mock the get_os_vendor method of the base class
        return 'GNU'

    def get_uptime_facts_mock():
        # Mock the get_uptime_facts method of the LinuxHardware class
        return {'uptime_seconds': '42'}

    def get_memory_facts_mock():
        # Mock the get_memory_facts method of the LinuxHardware class
        return {'memtotal_mb': '1234'}


# Generated at 2022-06-13 00:58:41.584876
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    from ansible.module_utils.facts.timeout import TimeoutError
    import os
    import sys
    import mock

    this_dir = os.path.dirname(os.path.realpath(__file__))

    mock_get_file_content = mock.MagicMock(return_value='\n'.join(
        [
            'Filesystem            Size  Used Avail Capacity  Mounted on',
            '/dev/disk1s2         233Gi  135Gi   98Gi    59%    /'
        ]
    ))

# Generated at 2022-06-13 00:58:50.062696
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_facts = HurdHardware()
    facts = hurd_facts.populate()
    assert facts['uptime_seconds'] > 0
    assert facts['uptime_minutes'] > 0
    assert facts['uptime_hours'] > 0
    assert facts['uptime_days'] >= 0
    assert facts['uptime_seconds'] == facts['uptime_minutes'] * 60
    assert facts['uptime_minutes'] == facts['uptime_hours'] * 60
    assert facts['uptime_hours'] == facts['uptime_days'] * 24
    assert isinstance(facts['memtotal_mb'], int)
    assert isinstance(facts['memfree_mb'], int)
    assert isinstance(facts['swaptotal_mb'], int)
    assert isinstance(facts['swapfree_mb'], int)



# Generated at 2022-06-13 00:58:51.006804
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """
    Test populating the HurdHardware facts.
    """
    pass

# Generated at 2022-06-13 00:58:52.058039
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware = HurdHardware()
    hardware.populate()


# Generated at 2022-06-13 00:58:53.118552
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hw = HurdHardware()
    hurd_hw.populate()

# Generated at 2022-06-13 00:59:02.146574
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    from ansible.module_utils.facts.hardware.linux import LinuxHardware

    time_facts = {'uptime_seconds': 93710}
    memory_facts = {
        'memtotal_mb': 244, 'memfree_mb': 104, 'memavailable_mb': 134,
        'swaptotal_mb': 0, 'swapfree_mb': 0, 'swapcached_mb': 0,
        'cached_mb': 0, 'buffers_mb': 0, 'swap_mb': 0
    }

# Generated at 2022-06-13 00:59:09.255639
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """Test class HurdHardware.

    Directly instantiate class HurdHardware, call method populate and
    inspect result.

    :return: True if testcase succeed.

    """

    hurd_hardware = HurdHardware()
    collected_facts = { 'kernel': 'GNU' }

    hardware_facts = hurd_hardware.populate(collected_facts)

    assert hardware_facts['uptime_seconds'] > 0
    assert hardware_facts['uptime_days'] > 0
    assert hardware_facts['total_available_bytes'] > 0
    assert hardware_facts['total_available_mb'] > 0

# Generated at 2022-06-13 00:59:16.501236
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """
    Unit test for method populate of class HurdHardware.
    """

    # Create empty HurdHardware object
    hurd_hardware_obj = HurdHardware()

    # Call method populate
    result = hurd_hardware_obj.populate()

    assert result['uptime_seconds'] >= 0
    assert result['uptime_seconds'] == result['uptime_days'] * 86400 + result['uptime_hours'] * 3600 + \
        result['uptime_minutes'] * 60 + result['uptime_seconds']
    assert result['uptime_hours'] >= 0 and result['uptime_hours'] < 24
    assert result['uptime_minutes'] >= 0 and result['uptime_minutes'] < 60
    assert result['uptime_days'] >= 0

# Generated at 2022-06-13 00:59:23.778550
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    from ansible.module_utils.basic import AnsibleModule

    class MockModule(AnsibleModule):
        """
        Mocks an AnsibleModule for tests.
        """
        def __init__(self, *args, **kwargs):
            return super(MockModule, self).__init__(*args, **kwargs)

        def fail_json(self, *args, **kwargs):
            raise RuntimeError()

    module = MockModule(argument_spec={})
    hw_obj = HurdHardware(module)

    result = hw_obj.populate()
    assert hw_obj.platform == 'GNU'
    assert 'uptime' in result
    assert 'uptime_seconds' in result
    assert 'memory_mb' in result
    assert 'mounts' in result

# Generated at 2022-06-13 00:59:32.637242
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hardware_test = HurdHardware()
    hurd_hardware_test.is_linux = True

    hurd_mem_test = hurd_hardware_test.get_memory_facts()
    assert 'MemTotal' in hurd_mem_test
    assert 'MemFree' in hurd_mem_test
    assert 'SwapTotal' in hurd_mem_test
    assert 'SwapFree' in hurd_mem_test

    hurd_mount_test = hurd_hardware_test.get_mount_facts()
    assert 'mounts' in hurd_mount_test

    hurd_uptime_test = hurd_hardware_test.get_uptime_facts()
    assert 'uptime' in hurd_uptime_test

# Generated at 2022-06-13 00:59:39.057324
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # Initialize HurdHardware object
    hurd_hardware_obj = HurdHardware()
    # Dictionary with collected facts
    collected_facts = {}
    collected_facts = hurd_hardware_obj.populate(collected_facts)

    # assert statements
    assert collected_facts['uptime_seconds'] >= 0
    assert collected_facts['uptime_seconds'] <= 1490325710
    assert collected_facts['uptime_seconds'] == int(collected_facts['uptime_seconds'])
    assert collected_facts['uptime_hours'] >= 0
    assert collected_facts['uptime_hours'] <= 1658
    assert collected_facts['uptime_hours'] == int(collected_facts['uptime_hours'])
    assert collected_facts['uptime_days'] >= 0
    assert collected_facts['uptime_days']

# Generated at 2022-06-13 00:59:41.537550
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """Unit test for method populate of class HurdHardware"""
    hurd_hardware = HurdHardware()
    assert 'uptime' in hurd_hardware.populate()

# Generated at 2022-06-13 00:59:46.536217
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    from ansible.module_utils.facts.hardware.linux import LinuxHardware
    from ansible.module_utils.facts.hardware.hurd import HurdHardwareCollector
    linux_hardware = LinuxHardware(facts={})
    hurd_hardware = HurdHardwareCollector(facts={'ansible_system': 'GNU'})
    linux_hardware.populate()
    hurd_hardware.populate()
    assert linux_hardware.facts['ansible_mounts'] == hurd_hardware.facts['ansible_mounts']

# Generated at 2022-06-13 00:59:47.735863
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # See https://github.com/ansible/ansible/pull/34180 for test content
    pass

# Generated at 2022-06-13 00:59:51.908016
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hardware = HurdHardware('hurd')
    hardware_facts = hurd_hardware.populate()
    assert hardware_facts['uptime_seconds'] is not None
    assert hardware_facts['memory_mb']['real']['total'] is not None
    assert hardware_facts['ansible_mounts'] is not None

# Generated at 2022-06-13 00:59:59.669570
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """Test the populate() method of the HurdHardware class."""
    cpu_facts = {
        'processor': [
            {
                'processor': 0
            },
            {
                'processor': 1
            }
        ]
    }
    facts = {
        'ansible_processor_count': 2,
        'ansible_processor_vcpus': 2,
        'ansible_processor_cores': 2,
        'ansible_processor_threads_per_core': 1,
        'ansible_processor_vcpus_at_max_speed': 2
    }
    cpu_facts.update(facts)

# Generated at 2022-06-13 01:00:04.792056
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hh = HurdHardware()
    hh.populate()

    assert 'uptime_seconds' in hh.facts, \
        "Key 'uptime_seconds' not found in dict of facts"
    assert 'memory_mb' in hh.facts, \
        "Key 'memory_mb' not found in dict of facts"
    assert 'mounts' in hh.facts, \
        "Key 'mounts' not found in dict of facts"

# Generated at 2022-06-13 01:00:08.902925
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """
    Test for method: HurdHardware.populate
    """
    # Run test
    hurd_hardware = HurdHardware()
    facts = hurd_hardware.populate()
    # Check result
    assert facts['uptime_seconds'] > 0
    assert facts['memory']['total'] > 0
    assert facts['mounts']


# Generated at 2022-06-13 01:00:20.448982
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    collected_facts = {}
    collected_facts['ansible_architecture'] = 'i386'
    collected_facts['ansible_machine_id'] = '123'
    collected_facts['ansible_system'] = 'Hurd'
    collected_facts['ansible_distribution'] = 'GNU'
    collected_facts['ansible_os_family'] = 'GNU/Hurd'
    collected_facts['ansible_distribution_major_version'] = '0'
    collected_facts['ansible_distribution_version'] = '0.9'
    collected_facts['ansible_distribution_release'] = '0.9/0.3'
    collected_facts['ansible_architecture'] = 'i386'
    linux_hw = HurdHardware(collected_facts, 'default')

# Generated at 2022-06-13 01:00:23.028292
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hardware = HurdHardware()
    collected_facts = {'distribution_version': '0.5'}
    hardware_facts = hurd_hardware.populate(collected_facts=collected_facts)

    assert hardware_facts['uptime_days'] == 0

# Generated at 2022-06-13 01:00:24.327489
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    obj = HurdHardware()
    result = obj.populate()
    assert 'memory' in result

# Generated at 2022-06-13 01:00:33.324073
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware_fetcher = HurdHardware()
    hardware_fetcher.get_uptime_facts = lambda: {'uptime': '1d'}
    hardware_fetcher.get_memory_facts = lambda: {'memtotal': '8192'}
    hardware_fetcher.get_mount_facts = lambda: {'mounts': ['mount1', 'mount2']}

    expected_facts = {
        'uptime': '1d',
        'memtotal': '8192',
        'mounts': ['mount1', 'mount2']
    }

    actual_facts = hardware_fetcher.populate()
    assert expected_facts == actual_facts

# Generated at 2022-06-13 01:00:34.531112
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hw = HurdHardware()
    hw.populate()

# Generated at 2022-06-13 01:00:37.082583
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # Test for the collect method of class HurdHardware
    hardware = HurdHardware()
    hardware.collect()

    # Test for the get_mount_facts method of class HurdHardware
    hardware.get_mount_facts()

# Generated at 2022-06-13 01:00:46.657815
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    from ansible.module_utils.facts.module import FactsModule
    from ansible.module_utils.facts import timeout
    from ansible.module_utils.facts.hardware.linux import Uptime
    from ansible.module_utils.facts.hardware.linux import Mount
    from ansible.module_utils.facts.hardware.linux import LinuxMemory

    def platform_mock():
        return ['GNU']

    def sysfs_mock(path):
        return None

    def mount_mock(path):
        return None

    def read_file_mock(path):
        if path == '/proc/sys/fs/store/timeout':
            return ['1']
        elif path == '/proc/sys/fs/store/timeout/user':
            return ['1']

# Generated at 2022-06-13 01:00:54.578313
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    class ModuleMock(object):
        def __init__(self, *args, **kwargs):
            super(ModuleMock, self).__init__()
            self.params = kwargs

    class CallModuleMock(object):
        def __init__(self, *args, **kwargs):
            super(CallModuleMock, self).__init__()
            self.params = kwargs

        def __call__(self, module_name, *args, **kwargs):
            return {
                        module_name: {
                            'cmd': "cat /proc/uptime",
                            'stdout': "12345.67 89101.11",
                            'rc': 0,
                            'changed': False,
                            'warnings': []
                        }
                    }[module_name]

    collected_

# Generated at 2022-06-13 01:00:59.118680
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurdHardware = HurdHardware()
    collected_facts = {}
    expected_facts = {
        'uptime_seconds': 15.0,
        'time_offset': 3600,
        'uptime_start': 15.0
    }

    facts = hurdHardware.populate(collected_facts)
    assert expected_facts == facts


# Generated at 2022-06-13 01:01:08.492021
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """
    Test method populate of class HurdHardware by mocking LinuxHardware.get_uptime_facts and
    LinuxHardware.get_memory_facts.
    """

    # Mocking base classes method
    class MockedLinuxHardware(LinuxHardware):
        def get_uptime_facts(self):
            return {'uptime_seconds': 1234.56}

        def get_memory_facts(self):
            return {'memtotal_mb': 123}

    import pytest

    hurd_hardware = HurdHardware(MockedLinuxHardware)
    collected_facts = {}
    hurd_hardware.populate(collected_facts)

    assert 'uptime_seconds' in collected_facts
    assert collected_facts['uptime_seconds'] == 1234.56

    assert 'memtotal_mb' in collected_facts
    assert collected_facts

# Generated at 2022-06-13 01:01:24.586182
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hh = HurdHardware()

# Generated at 2022-06-13 01:01:31.275521
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hh = HurdHardware()
    hh.get_uptime_facts = lambda: {'uptime_seconds': 1}
    hh.get_memory_facts = lambda: {'memtotal_mb': 1}
    hh.get_mount_facts = lambda: {'mounts': [{'partition': '/', 'mount': '/'}]}
    hh.populate()
    assert hh.facts['uptime_seconds'] == 1
    assert hh.facts['memtotal_mb'] == 1
    assert hh.facts['mounts'] == [{'partition': '/', 'mount': '/'}]

# Generated at 2022-06-13 01:01:37.111639
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    ansible_module = AnsibleModule()
    hurd_hw = HurdHardware(ansible_module)
    res = hurd_hw.populate()

    REQUIRED_KEYS = [
        'uptime',
        'uptime_seconds',
        'uptime_days',
        'memfree_mb',
        'memtotal_mb',
        'swapfree_mb',
        'swaptotal_mb',
    ]

    for key in REQUIRED_KEYS:
        assert key in res
        assert res[key] is not None



# Generated at 2022-06-13 01:01:37.767414
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware = HurdHardware()
    hardware.collect()

# Generated at 2022-06-13 01:01:43.432939
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hardware = HurdHardware()
    collected_facts = {}
    facts = hurd_hardware.populate(collected_facts)
    assert facts['uptime_seconds'] == 0
    assert facts['uptime_days'] == 0
    assert facts['uptime_hours'] == 0
    assert facts['uptime_minutes'] == 0
    assert facts['ram']['total'] == 0
    assert facts['ram']['available'] == 0
    assert facts['ram']['used'] == 0
    assert facts['ram']['percent'] == 0
    assert facts['ram']['free'] == 0

# Generated at 2022-06-13 01:01:50.161304
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """
    Basic unit tests for HurdHardware class
    """
    hurd_sysclass_path = 'ansible.module_utils.facts.hardware.linux.hw_HurdHardwareCollector.HurdHardwareCollector.sysclass_path'
    hurd_cpuinfo_path = 'ansible.module_utils.facts.local.linux.LinuxHardwareCollector.LinuxHardwareCollector.cpuinfo_path'
    import os  # import MUST be here, otherwise mock does not work
    from mock import patch  # import MUST be here, otherwise mock does not work
    from ansible.module_utils.facts.hardware.hurd import HurdHardware

    ################################################################################
    # Test 'get_uptime_facts()' method of HurdHardware
    ################################################################################

# Generated at 2022-06-13 01:01:50.709497
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    pass

# Generated at 2022-06-13 01:01:54.283487
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    collected_facts = {'ansible_os_family': 'GNU/Hurd'}
    hurd_hardware = HurdHardware()

    # define empty data type
    expected_result = {}

    result = hurd_hardware.populate(collected_facts)
    assert result == expected_result

# Generated at 2022-06-13 01:02:02.936571
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """ HurdHardware - test populate method

    This test checks if it's possible to retrieve the expected dictionary
    of facts when calling populate method.
    """
    hardware_collector = HurdHardwareCollector()
    hardware_facts = hardware_collector.collect()

    assert isinstance(hardware_facts, dict)
    assert hardware_facts['os_family'] == 'GNU'
    assert hardware_facts['platform'] == 'GNU'
    assert isinstance(hardware_facts['uptime_seconds'], int)
    assert hardware_facts['uptime_seconds'] >= 0
    assert isinstance(hardware_facts['memtotal_mb'], int)
    assert hardware_facts['memtotal_mb'] >= 0
    assert hardware_facts['memory_mb']['real']['total'] >= 0

# Generated at 2022-06-13 01:02:04.979106
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    collected_facts = {
        'ansible_facts': {
            'kernel': 'GNU',
            'system': 'GNU/Hurd',
        },
    }

    hurd_hardware = HurdHardware()
    hurd_hardware.populate(collected_facts)

# Generated at 2022-06-13 01:02:24.525063
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # Fake the output of LinuxHardware.get_uptime_facts
    class FakeLinuxHardware:
        def get_uptime_facts(self):
            uptime_facts = {'uptime_days': 5, 'uptime_hours': 5, 'uptime_seconds': 5, 'uptime_minutes': 5}
            return uptime_facts

    # Fake the output of LinuxHardware.get_memory_facts
    def get_memory_facts():
        memory_facts = {'memfree_mb': 5, 'memtotal_mb': 5}
        return memory_facts

    # Fake the output of LinuxHardware.get_mount_facts
    def get_mount_facts():
        mount_facts = {'mounts': [{'device': 'device', 'mount': 'mount', 'fstype': 'fstype'}]}
        return

# Generated at 2022-06-13 01:02:31.109995
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hw = HurdHardware()

    collected_facts = {"ansible_distribution_version": "1.2",
                       "ansible_distribution": "GNU",
                       "ansible_fips": False}

    hardware_facts = hurd_hw.populate(collected_facts)


# Generated at 2022-06-13 01:02:37.729704
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    import os
    from ansible_collections.ansible.community.plugins.module_utils.facts import hardware
    hw = hardware.HurdHardware()
    os.environ['ANSIBLE_COLLECTIONS_PATHS'] = ':'.join(
        [os.path.join(hardware.__file__, '../../../../../')]
    )
    assert isinstance(hw.populate(), dict)

# Generated at 2022-06-13 01:02:42.854922
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    import os

    collected_facts = {'kernel_name': 'GNU'}
    class_instance = HurdHardware()
    class_instance.kernel = 'GNU'
    result = class_instance.populate(collected_facts)
    assert result['uptime']['days'] == os.path.getsize(
        '/hurd/mach_interface/uptime')
    assert result['memtotal_mb'] == os.path.getsize(
        '/proc/meminfo') / 1024

# Generated at 2022-06-13 01:02:51.888816
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # Test HurdHardware.populate()
    hh = HurdHardware()
    collected_facts = hh.populate()

    # We expect collected_facts to have a key 'memory'
    assert 'memory' in collected_facts

    # Test that we have expected keys in collected_facts['memory']
    memory_keys = [
        'total', 'swapfree', 'swaptotal', 'memfree', 'memtotal', 'active',
        'inactive', 'vmalloc_total', 'vmalloc_used', 'vmalloc_chunk',
        'hugepages_total', 'hugepages_free', 'hugepages_rsvd',
        'hugepages_surp', 'hugepagesize', 'buffers', 'cached'
    ]
    for key in collected_facts['memory']:
        assert key in memory_keys

    #

# Generated at 2022-06-13 01:02:58.876786
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # Set up a fake hardware object
    hardware_object = HurdHardware({})

    # Test a successful populate method call
    hardware_object.get_uptime_facts = MagicMock(return_value={
        'uptime_seconds': 50000
    })
    hardware_object.get_memory_facts = MagicMock(return_value={
        'memtotal_mb': 500,
        'memfree_mb': 300
    })
    hardware_object.get_mount_facts = MagicMock(return_value={
        '/': {
            'device': 'foo'
        }
    })
    hardware_facts = hardware_object.populate()

# Generated at 2022-06-13 01:03:09.327856
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    h = HurdHardware()

    # get_uptime_facts() mockup
    def get_uptime_facts_mockup(*args, **kwargs):
        return { 'uptime_seconds': 10 }

    # get_memory_facts() mockup
    def get_memory_facts_mockup(*args, **kwargs):
        return { 'memory_mb': 10 }

    # get_mount_facts() mockup
    def get_mount_facts_mockup(*args, **kwargs):
        return { 'mounts': [ { 'mount': '/', 'device': '/dev/hda' } ] }

    # Mockup methods
    h.get_uptime_facts = get_uptime_facts_mockup
    h.get_memory_facts = get_memory_facts_mockup

# Generated at 2022-06-13 01:03:15.930401
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hh = HurdHardware()

    hh.get_uptime_facts = lambda: {'uptime_seconds': 5}
    hh.get_memory_facts = lambda: {'memtotal_mb': 10}
    hh.get_mount_facts = lambda: {'mounts': [1, 2, 3]}

    result = hh.populate()

    assert result['uptime_seconds'] == 5
    assert result['memtotal_mb'] == 10
    assert result['mounts'] == [1, 2, 3]


# Generated at 2022-06-13 01:03:17.341526
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hardware = HurdHardware()
    hurd_hardware.populate()


# Generated at 2022-06-13 01:03:24.486152
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    from ansible.module_utils.facts.hardware.linux import LinuxHardware
    hardware = HurdHardware()

    hardware_facts = hardware.populate()

    # check some facts
    assert hardware_facts['uptime_seconds'] > 0
    assert hardware_facts['uptime_hours'] > 0
    assert hardware_facts['uptime_days'] > 0
    assert hardware_facts['memory_mb'] > 0
    assert 'swap' in hardware_facts
    assert hardware_facts['swap']['total'] > 0
    assert hardware_facts['swap']['free'] > 0

    # check mount facts
    assert 'mounts' in hardware_facts
    assert len(hardware_facts['mounts']) > 0
    mount = hardware_facts['mounts'][0]
    linux_mount = {}

# Generated at 2022-06-13 01:03:48.946908
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    test_HurdHardware = HurdHardware()
    test_dict = {}
    test_dict.update(test_HurdHardware.get_uptime_facts())
    test_dict.update(test_HurdHardware.get_memory_facts())
    return test_dict

# Generated at 2022-06-13 01:03:54.909977
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    from ansible.module_utils.facts.hardware.hurd import HurdHardware
    testhw = HurdHardware()
    testhw.sysctl = 'test/sysctl.txt'
    testhw.mountinfo = 'test/mountinfo.txt'
    testhw.meminfo = 'test/meminfo.txt'
    testhw.dataset = 'test'
    testhw.collect()
    assert testhw.facts['uptime_seconds'] == 1726641
    assert testhw.facts['uptime_days'] == 1
    assert testhw.facts['uptime_hours'] == 21
    assert testhw.facts['uptime_seconds'] == 1726641
    assert testhw.facts['memtotal_mb'] == 2441
    assert testhw.facts['memfree_mb'] == 1881
    assert testhw.facts

# Generated at 2022-06-13 01:04:03.982550
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """
    Create a mock hardware collector and verify the
    method populate populates it with the expected
    facts.
    """
    hw = HurdHardware()
    uptime_facts = hw.get_uptime_facts()
    memory_facts = hw.get_memory_facts()
    mount_facts = hw.get_mount_facts()

    hw.populate()
    facts = hw.get_facts()

    for key in uptime_facts:
        assert facts[key] == uptime_facts[key]

    for key in memory_facts:
        assert facts[key] == memory_facts[key]

    for key in mount_facts:
        assert facts[key] == mount_facts[key]

# Generated at 2022-06-13 01:04:11.751882
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """Test that the GNU Hurd specific subclass of Hardware
    collects the expected facts.
    """
    facts_dict = HurdHardware().populate()

    assert facts_dict
    assert 'uptime_seconds' in facts_dict
    assert 'uptime_days' in facts_dict
    assert 'uptime_hours' in facts_dict
    assert 'uptime_minutes' in facts_dict

    assert 'memtotal_mb' in facts_dict
    assert 'memfree_mb' in facts_dict
    assert 'swaptotal_mb' in facts_dict
    assert 'swapfree_mb' in facts_dict

    assert 'mounts' in facts_dict
    assert isinstance(facts_dict['mounts'], list)

# Generated at 2022-06-13 01:04:19.102802
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # We need a fake ansible_system_vendor to be set, since the HurdHardware
    # class inherits from LinuxHardware.
    collected_facts = {'ansible_system_vendor': 'Foo'}
    expected_facts = {
        'memory_mb': {'nocache': 0, 'real': 0, 'swap': 0, 'total': 0},
        'uptime_seconds': 0,
        'mounts': {}
    }

    hh = HurdHardware()
    actual_facts = hh.populate(collected_facts)

    assert actual_facts == expected_facts


# Generated at 2022-06-13 01:04:23.046448
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    test_facts = {
        'distribution': 'GNU',
        'architecture': 'x86_64'
    }
    hardware = HurdHardware(test_facts)
    hardware_facts = hardware.populate()
    assert hardware_facts['uptime_seconds'] == 0
    assert hardware_facts['uptime_days'] == 0.0


# Generated at 2022-06-13 01:04:30.554943
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """
    Unit test for method populate of class HurdHardware.
    """
    # Initialize the instance
    hurd_hardware_collector = HurdHardware()

    # Run the populate method
    hurd_hardware_collector.populate()

    # Verify the results
    assert 'path' in hurd_hardware_collector.mounts
    assert '/' in hurd_hardware_collector.mounts
    assert '/dev' in hurd_hardware_collector.mounts
    assert '/dev/pts' in hurd_hardware_collector.mounts
    assert '/home' in hurd_hardware_collector.mounts
    assert '/proc' in hurd_hardware_collector.mounts
    assert '/run' in hurd_hardware_collector.mounts
    assert '/sys' in hurd_hardware_collect

# Generated at 2022-06-13 01:04:32.660839
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hw = HurdHardware()
    hurd_hw.populate()

    assert 'uptime' in hurd_hw.facts
    assert isinstance(hurd_hw.facts['uptime'], int)

# Generated at 2022-06-13 01:04:35.121492
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # Test with empty collected_facts
    hurd_Hardware = HurdHardware(collected_facts={})
    hurd_Hardware.populate()
    # Test with non empty collected_facts
    hurd_Hardware = HurdHardware(collected_facts={'os_family': 'Debian'})
    hurd_Hardware.populate()

# Generated at 2022-06-13 01:04:36.647796
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hw = HurdHardware()
    hw.collect()
    collected_facts = hw.get_facts()
    assert collected_facts['uptime']
    assert collected_facts['memtotal_mb']
    assert collected_facts['virtual']

# Generated at 2022-06-13 01:05:25.947346
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    module = AnsibleModule(
        argument_spec = dict()
    )

    # Set up mocked classes
    def get_ansible_module():
        return module

    def get_memory_facts():
        return {
            "memtotal_mb": 16,
            "memfree_mb": 0,
            "swaptotal_mb": 1,
            "swapfree_mb": 1,
            "active_mb": 15,
            "inactive_mb": 1,
            "cached_mb": 2,
            "real_memory_mb": 16,
        }


# Generated at 2022-06-13 01:05:31.202867
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hw = HurdHardware({'uname_result': {'system': 'GNU', 'kernel': 'GNU'}})
    uptime_facts = hw.get_uptime_facts()
    memory_facts = hw.get_memory_facts()
    mount_facts = hw.get_mount_facts()
    system_facts = hw.populate()

    assert uptime_facts == system_facts
    assert memory_facts == system_facts
    assert mount_facts == system_facts

# Generated at 2022-06-13 01:05:39.922811
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """Unit test of method populate of class HurdHardware"""
    import sys
    import os
    import shutil
    import tempfile

    # Create temporary directory
    tmpdir = tempfile.mkdtemp()

    # Create a temporary module or copy the real module in temporary
    # directory
    shutil.copyfile(
        os.path.join(os.path.dirname(os.path.abspath(__file__)),
                     'module_utils/facts/hardware/linux'),
        os.path.join(tmpdir, 'linux'))
    os.chmod(os.path.join(tmpdir, 'linux'), 0o744)

    # Create a temporary class HurdHardware or copy the real class HurdHardware
    # in temporary directory