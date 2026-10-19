

# Generated at 2022-06-13 00:55:43.924104
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """
    This function tests the population of facts for GNU/Hurd systems.
    """
    hurdhardware_obj = HurdHardwareCollector()
    hurdhardware_obj.populate()
    assert 'uptime_seconds' in hurdhardware_obj.facts

# Generated at 2022-06-13 00:55:51.229687
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    from mock import patch, Mock

    # Fact check to make sure that the class is detected for GNU/Hurd
    fact_collector = HurdHardwareCollector()
    collected_facts = fact_collector.collect(None, None)
    assert collected_facts['kernel'] == 'GNU'

    # Make sure the populate method returns something of the correct type
    # by mocking the other functions in the HurdHardware class
    fact_instance = HurdHardware()

    with patch.object(HurdHardware, 'get_mount_facts') as mock_mount:
        mock_mount.return_value = {'mounts': []}

        with patch.object(HurdHardware, 'get_uptime_facts') as mock_uptime:
            mock_uptime.return_value = {'uptime': 0}


# Generated at 2022-06-13 00:55:53.347270
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """
    Unit test for method populate of class HurdHardware
    """
    hurd_hardware_obj = HurdHardware()
    hurd_hardware_obj.populate()

# Generated at 2022-06-13 00:55:59.180229
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    from ansible.module_utils.facts.utils import get_file_content
    from ansible.module_utils._text import to_native
    from ansible.module_utils.facts import timeout

    def mock_get_mount_facts_successful(self):
        return get_file_content(
            os.path.join(os.path.dirname(os.path.realpath(__file__)),
                         'get_mount_facts_successful'))

    def mock_get_mount_facts_timeout(self):
        timeout.wait_for_connect(self.module, 'mount')

    HurdHardware.get_mount_facts = mock_get_mount_facts_successful
    hurd_hardware = HurdHardware()
    hurd_hardware_facts = hurd_hardware.populate()

# Generated at 2022-06-13 00:56:05.298047
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    from ansible.module_utils.facts.timeout import TimeoutError
    from ansible.module_utils.facts.hardware.linux import LinuxHardware
    from ansible.module_utils.facts.hardware.linux import LinuxHardwareCollector
    import ansible.module_utils.facts.hardware.linux

    hardware_collector = LinuxHardwareCollector.init_factory()
    hardware_collector.get_uptime_facts = lambda self: {'uptime': 'uptime'}
    hardware_collector.get_memory_facts = lambda self: {'memory': 'memory'}
    hardware_collector.get_mount_facts = lambda self: {'mount': 'mount'}
    ansible.module_utils.facts.hardware.linux.LinuxHardwareCollector = hardware_collector

    hardware_collector = HurdHardware

# Generated at 2022-06-13 00:56:14.015374
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """Test the population of the hardware facts on GNU/Hurd
    """

    # Tested with the following return values:
    #   $ grep -oP "\d+" /proc/uptime
    #   4353192
    #   13
    #   $ grep -oP "\d+" /proc/meminfo
    #   1297362
    #   93396
    #   109464
    #   3133050
    #   196863
    #   324531
    #   0
    #   0
    #   0
    #   0
    #   0
    #   0
    #   0
    #   0
    #   0
    #   0
    #   0
    #   0
    #   553
    #   0
    #   0
    #   0


# Generated at 2022-06-13 00:56:19.109407
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    h = HurdHardware()
    hardware_facts = h.populate()
    assert 'uptime_seconds' in hardware_facts
    assert 'ram' in hardware_facts['memory']
    assert 'swap' in hardware_facts['memory']
    assert hardware_facts['mounts'][0]['fstype'] == 'ext4'

# Generated at 2022-06-13 00:56:23.021026
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """
    Test method 'populate' of class HurdHardware
    """
    hurdHardware = HurdHardware()
    if hurdHardware.populate() is not None:
        print('populate method got run without errors.')
    else:
        print('populate method failed due to error.')

# Generated at 2022-06-13 00:56:23.528683
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    pass

# Generated at 2022-06-13 00:56:27.576598
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    h = HurdHardware()
    collected_facts = {}
    facts = h.populate(collected_facts)
    assert facts['uptime_seconds'] == None
    assert facts['uptime_days'] == None
    assert facts['memory_mb'] == None
    assert facts['swapfree_mb'] == None
    assert facts['swaptotal_mb'] == None
    assert facts['mounts'] == {}

# Generated at 2022-06-13 00:56:33.715836
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware_facts = {}
    hurd_hw = HurdHardware()
    hardware_facts_result = hurd_hw.populate()
    assert hardware_facts == hardware_facts_result


# Generated at 2022-06-13 00:56:38.928070
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hh = HurdHardware()

    facts = hh.populate()

    # check that the 'uptime' key exists in the facts dict
    assert 'uptime' in facts

    # check that the 'uptime_days' key exists in the facts dict
    assert 'uptime_days' in facts

    # check that the 'uptime_hours' key exists in the facts dict
    assert 'uptime_hours' in facts

    # check that the 'uptime_seconds' key exists in the facts dict
    assert 'uptime_seconds' in facts

    # check that the 'memfree_mb' key exists in the facts dict
    assert 'memfree_mb' in facts

    # check that the 'swapfree_mb' key exists in the facts dict
    assert 'swapfree_mb' in facts

    # check that the 'memtotal

# Generated at 2022-06-13 00:56:42.613660
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hw = HurdHardware()
    collected_facts = {}
    hurd_hw.populate(collected_facts)

    # testing a fact result
    assert collected_facts['uptime'] == '0 days, 0 hours, 0 minutes, 0 seconds'

# Generated at 2022-06-13 00:56:49.282020
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    linux_collector = LinuxHardware()
    hurd_collector = HurdHardware()

    collected_facts = {}

    # Call Linux version to populate its hierarchy
    linux_collector.populate()

    # Call Hurd version of populate
    hurd_collector.populate()

    # Compare against Linux version
    assert linux_collector.uptime_facts == hurd_collector.uptime_facts
    assert hurd_collector.memory_facts == linux_collector.memory_facts
    assert hurd_collector.mount_facts == linux_collector.mount_facts

# Generated at 2022-06-13 00:56:58.488577
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    from mock import patch

    test_hardware = HurdHardware()

    # get_uptime_facts()
    test_uptime_facts = dict(uptime='42')
    with patch.object(test_hardware, 'get_uptime_facts') as mock_get_uptime_facts:
        mock_get_uptime_facts.return_value = test_uptime_facts
        test_hardware.populate()
        mock_get_uptime_facts.assert_called_once_with()

    # get_memory_facts()
    test_memory_facts = dict(memory='42')
    with patch.object(test_hardware, 'get_memory_facts') as mock_get_memory_facts:
        mock_get_memory_facts.return_value = test_memory_facts

# Generated at 2022-06-13 00:57:08.365292
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hw = HurdHardware()

    hw.get_mount_facts = lambda: {'mounts': [{'device': '/dev/', 'mount': '/', 'type': 'hurd', 'options': 'rw,relatime'}]}
    hw.get_memory_facts = lambda: {'ansible_memfree_mb': '38', 'ansible_memtotal_mb': '1012', 'ansible_swaptotal_mb': '1014', 'ansible_memtotal_mb': '1012', 'ansible_swapfree_mb': '1014'}
    hw.get_uptime_facts = lambda: {'ansible_uptime_seconds': '17991'}

    hw.populate()

    assert hw.uptime['seconds'] == 17991

# Generated at 2022-06-13 00:57:09.586618
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    uut = HurdHardware()
    assert type(uut.populate()) == dict

# Generated at 2022-06-13 00:57:12.919110
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # instance HurdHardware class
    hh = HurdHardware()

    # call the method populate with a dictionary of collected_facts
    hh.get_mount_facts()
    hh.get_memory_facts()
    hh.get_uptime_facts()
    hh.populate(collected_facts={})

# Generated at 2022-06-13 00:57:19.003932
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    facts_dict = {'ansible_facts': {}}
    hw = HurdHardware(facts_dict)
    facts_dict = hw.populate()
    assert 'ansible_facts' in facts_dict
    assert 'hardware' in facts_dict['ansible_facts']
    assert 'uptime' in facts_dict['ansible_facts']['hardware']
    assert 'memtotal_mb' in facts_dict['ansible_facts']['hardware']
    assert 'disks' in facts_dict['ansible_facts']['hardware']

# Generated at 2022-06-13 00:57:24.350845
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """
    Unit test for method populate of class HurdHardware.
    """
    hurd_hardware_facts = HurdHardware()
    hurd_hardware_facts.populate()
    assert 'uptime_seconds' in hurd_hardware_facts.get_all()
    assert 'memfree_mb' in hurd_hardware_facts.get_all()

# Generated at 2022-06-13 00:57:35.637668
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    already_collected_facts = dict(
        uptime=123, mem_total=0, mem_swap_total=1,
        ansible_mounts=["a", "b"], ansible_devices=["d", "e"], ansible_all_ipv4_addresses=["f"],
        ansible_all_ipv6_addresses=["g"]
    )

# Generated at 2022-06-13 00:57:39.315398
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    class TestArgs():
        def __init__(self):
            self.gather_subset = None

    # Initialize class
    module_args = TestArgs()
    hurdhardware = HurdHardware(module_args)

    # Call method populate
    hurdhardware.populate()

    # Assert if isinstance(hurdhardware, HurdHardware)
    assert isinstance(hurdhardware, HurdHardware)

# Generated at 2022-06-13 00:57:40.668942
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
  assert True

# Generated at 2022-06-13 00:57:47.635199
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware = HurdHardware()
    hardware_facts = hardware.populate()

    assert hardware_facts['uptime_seconds'] > 0
    assert hardware_facts['uptime_hours'] > 0

    assert hardware_facts['memtotal_mb'] > 0
    assert hardware_facts['memfree_mb'] >= 0
    assert hardware_facts['memavail_mb'] >= 0
    assert hardware_facts['swaptotal_mb'] >= 0
    assert hardware_facts['swapfree_mb'] >= 0

    assert hardware_facts['mounts']

# Generated at 2022-06-13 00:57:58.264803
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    import pytest
    from ansible.module_utils.facts.timeout import TimeoutError

    # Test HurdHardware.populate success
    hurd_facts_list = {'uptime_seconds': 123,
                       'uptime_days': 123,
                       'memtotal_mb': 123,
                       'memfree_mb': 123,
                       'memcached_mb': 123,
                       'swaptotal_mb': 123,
                       'swapfree_mb': 123,
                       'partitions_mount': "/"
                       }
    hurd = HurdHardware(module=None)
    hurd.get_uptime_facts = lambda: {'uptime_seconds': 123, 'uptime_days': 123}

# Generated at 2022-06-13 00:58:00.019912
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd = HurdHardware()
    result = hurd.populate()
    assert result['uptime'] > 0

# Generated at 2022-06-13 00:58:07.702257
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    try:
        set()
    except:
        import sets
        sets  # workaround for pyflakes issue #13
    class MockGNUHardware(HurdHardware):
        """Mock subclass of HurdHardware to bypass loading of facts modules"""

# Generated at 2022-06-13 00:58:12.712530
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware = HurdHardware()
    hardware.populate()

    # Check that the mount facts were collected
    assert hardware.mounts

    # Check that the uptime facts were collected
    assert hardware.uptime_seconds >= 0
    assert hardware.uptime_string

    # Check that the memory facts were collected
    assert hardware.memfree_mb >= 0
    assert hardware.memtotal_mb >= 0


# Generated at 2022-06-13 00:58:16.178923
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hardware = HurdHardware()
    hurd_hardware_facts = {'uptime': [], 'memtotal_mb': [], 'swapfree_mb': [], 'mounts': []}
    assert hurd_hardware_facts == hurd_hardware.populate()

# Generated at 2022-06-13 00:58:20.195096
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware_obj = HurdHardware()
    fact_dict = hardware_obj.populate()
    assert fact_dict == {'mounts': [], 'memtotal_mb': 0, 'memfree_mb': 0, 'uptime_seconds': 0, 'uptime_days': 0}

# Generated at 2022-06-13 00:58:27.311674
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hardware = HurdHardware()
    data = hurd_hardware.populate()

    assert data['uptime'] > 0
    assert data['uptime_seconds'] > 0
    assert data['memtotal_mb'] > 0
    assert len(data['mounts']) > 0

# Generated at 2022-06-13 00:58:35.234009
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    from ansible.module_utils.facts.timeout import TimeoutError
    from ansible.module_utils.facts.hardware.hurd import (
        HurdHardware,
        HurdHardwareCollector,
    )

    class mock_LinuxHardware():
        def __init__(self):
            self.test_dictionary = {}

        def populate(self, collected_facts=None):
            return self.test_dictionary

        def get_uptime_facts(self):
            self.test_dictionary['uptime'] = 'test_uptime'
            self.test_dictionary['uptime_seconds'] = 'test_uptime_seconds'
            return self.test_dictionary


# Generated at 2022-06-13 00:58:45.332187
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """
    given
    - a HurdHardware instance

    when
    - the populate method of the HurdHardware class is called

    then
    - the facts dict is not empty

    - the keys and values of the returned dict match the result of
      HurdHardware.get_uptime_facts()

    - the keys and values of the returned dict match the result of
      HurdHardware.get_memory_facts()

    - the keys and values of the returned dict match the result of
      HurdHardware.get_mount_facts()
    """
    hurd_hardware = HurdHardware()
    facts = hurd_hardware.populate()
    assert facts
    assert facts == hurd_hardware.get_uptime_facts()
    assert facts == hurd_hardware.get_memory_facts()
    assert facts == hurd_hardware.get_

# Generated at 2022-06-13 00:58:47.190010
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # Setup:
    hw = HurdHardware()

    # Exercise:
    # Verify:
    assert hw.populate()



# Generated at 2022-06-13 00:58:48.708781
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hh = HurdHardware()
    hh.populate()
    assert hh.populated is True

# Generated at 2022-06-13 00:58:55.956600
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():

    hurdhw = HurdHardware()

    # Testing correct values of keys
    assert 'uptime' in hurdhw.populate().keys()
    assert 'uptime_seconds' in hurdhw.populate().keys()
    assert 'memtotal' in hurdhw.populate().keys()
    assert 'memfree' in hurdhw.populate().keys()
    assert 'swaptotal' in hurdhw.populate().keys()
    assert 'swapfree' in hurdhw.populate().keys()

    # Testing value type
    assert isinstance(hurdhw.populate()['uptime'], str)
    assert isinstance(hurdhw.populate()['uptime_seconds'], int)
    assert isinstance(hurdhw.populate()['memtotal'], int)

# Generated at 2022-06-13 00:59:02.147494
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware = HurdHardware()
    hardware_facts = hardware.populate()
    uptime_facts = hardware.get_uptime_facts()
    memory_facts = hardware.get_memory_facts()
    mount_facts = hardware.get_mount_facts()
    assert hardware_facts.keys() == set(uptime_facts.keys()).union(set(memory_facts.keys())).union(set(mount_facts.keys()))


# Generated at 2022-06-13 00:59:05.038097
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # pylint: disable=protected-access
    hurd_hardware = HurdHardware()
    hurd_hardware.populate()
    assert hurd_hardware._facts["mounts"]

# Generated at 2022-06-13 00:59:07.379168
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurdhardware = HurdHardware()
    collected_facts = {}
    hurdhardware.populate(collected_facts)

# vim: set et ts=4 sw=4 :

# Generated at 2022-06-13 00:59:13.823494
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware = HurdHardware()

    hardware.file_module = MockFileModule()
    hardware.get_file_content = MockGetFileContent()
    hardware.is_mount_procfs = MockIsMountProcfs()
    hardware.is_stale_procfs_mount = MockIsStaleProcfsMount()
    hardware.get_uptime_facts = MockGetUptimeFacts()
    hardware.get_memory_facts = MockGetMemoryFacts()
    hardware.get_mount_facts = MockGetMountFacts()

    # First call to populate
    hardware.populate()

    # Second call to populate
    hardware.populate()



# Generated at 2022-06-13 00:59:29.257383
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # Test with an empty dictionary.
    hw = HurdHardware()
    assert hw.populate() == hw.populate({})

    # Test with a dictionary containing some supported facts.
    hw = HurdHardware({'ansible_architecture': 'x86_64'})
    hardware_facts = hw.populate()
    assert hardware_facts['architecture'] == 'x86_64'


# Generated at 2022-06-13 00:59:31.192515
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware_collector = HurdHardwareCollector()
    hardware = hardware_collector.collect()
    assert type(hardware) == dict

# Generated at 2022-06-13 00:59:38.188658
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # Override imported os with a mock.
    import sys
    sys.modules['os'] = MockOS
    import ansible.module_utils.facts.hardware.hurd as hurd_module
    facts_collector = hurd_module.HurdHardwareCollector()
    # Call to the method populate

# Generated at 2022-06-13 00:59:47.719930
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    from ansible.module_utils.facts.timeout import TimeoutError
    hurdhw = HurdHardware()
    expected = {
        'uptime_seconds': 5,
        'mem_swap_percent': 0.0,
        'mem_total_mb': 0.0,
        'mem_free_mb': 0.0,
        'mem_used_percent': 0.0,
        'mounts': []
    }
    hurdhw.get_uptime_facts = lambda: {'uptime_seconds': 5}
    hurdhw.get_memory_facts = lambda: {
        'mem_swap_percent': 0.0,
        'mem_total_mb': 0.0,
        'mem_free_mb': 0.0,
        'mem_used_percent': 0.0,
    }
    hurd

# Generated at 2022-06-13 00:59:56.475925
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    class HurdHardwareMock(HurdHardware):
        def get_uptime_facts(self):
            return {'uptime_seconds': 3600,
                    'uptime_hours': '1',
                    'uptime_days': 1}
        def get_memory_facts(self):
            return {'memory_mb': {'swap': {'total': 1, 'used': 0, 'free': 1},
                                  'real': {'total': 2, 'used': 1, 'free': 1}}}
        def get_mount_facts(self):
            return {'mounts':
                    [{'device': '/dev/sda1',
                      'mount': '/',
                      'fstype': 'ext4',
                      'options': 'rw,relatime'}]}

    h = HurdHardwareMock()
    facts

# Generated at 2022-06-13 01:00:02.041409
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # Test case 1: Platform distinct of GNU
    # Expected:
    #   facts = {}
    platform = 'Windows'
    hh = HurdHardware(platform)
    facts = hh.populate()
    assert facts == {}

    # Test case 2: Platform distinct of GNU
    # Expected:
    #   facts = {'processor': ['Intel(R) Core(TM) i7-4790 CPU @ 3.60GHz']}
    platform = 'Linux'
    hh = HurdHardware(platform)
    facts = hh.populate()
    assert 'processor' in facts
    assert facts['processor'][0] == 'Intel(R) Core(TM) i7-4790 CPU @ 3.60GHz'



# Generated at 2022-06-13 01:00:07.431092
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware = HurdHardware()

    hardware._os_version = '1.2.3'
    hardware.collector = HurdHardwareCollector()

    hardware.get_memory_facts = lambda: {'memory_mb': {'real': {'total': 100}, 'swap': {'total': 200}}}
    hardware.get_uptime_facts = lambda: {'uptime': {'seconds': 100}}
    hardware.get_mount_facts = lambda: {'mounts': {'/dev/sda1': {'size_total': 1, 'size_available': 2}}}

    result = hardware.populate()

    assert result['memory_mb']['real']['total'] == 100
    assert result['memory_mb']['swap']['total'] == 200
    assert result['uptime']['seconds'] == 100

# Generated at 2022-06-13 01:00:09.220834
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    facts = {}
    hurd_hardware = HurdHardware()
    facts_dict = hurd_hardware.populate()

    for key in facts_dict.keys():
        assert key in facts

# Generated at 2022-06-13 01:00:14.668879
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """
    Get facts of GNU Hurd
    """

    hurd_hardware_obj = HurdHardware()
    facts = hurd_hardware_obj.populate()

    assert facts['uptime_seconds']
    assert facts['uptime_days']
    assert facts['memfree_mb']
    assert facts['swapfree_mb']
    assert facts['mounts']

# Generated at 2022-06-13 01:00:22.145457
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware = HurdHardware()
    hardware_facts = hardware.populate()
    assert hardware_facts['uptime'] > 0
    assert hardware_facts['uptime_seconds'] > 0
    assert hardware_facts['uptime_hours'] > 0
    assert hardware_facts['uptime_days'] > 0
    assert hardware_facts['swapfree_mb'] > 0
    assert hardware_facts['memfree_mb'] > 0
    assert hardware_facts['memtotal_mb'] > 0
    assert hardware_facts['memavailable_mb'] > 0
    assert hardware_facts['ansible_mounts'] > 0

# Generated at 2022-06-13 01:00:46.246542
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurdhw = HurdHardware()
    hurdhw.populate()
    assert(hurdhw.uptime['seconds'] >= 0)
    assert(hurdhw.memory['ram'] >= 0)
    assert(hurdhw.memory['swap'] >= 0)
    assert(hurdhw.memory['total'] >= 0)
    assert(hurdhw.memory['used'] >= 0)
    assert(hurdhw.memory['free'] >= 0)
    assert(hurdhw.memory['available'] >= 0)

# Generated at 2022-06-13 01:00:51.666495
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hw_facts_obj = HurdHardware()
    hw_facts = hw_facts_obj.populate()

    assert hw_facts['uptime_seconds'] == 10
    assert hw_facts['memory_mb']['real']['total'] == 100
    assert hw_facts['memory_mb']['swap']['total'] == 100
    assert hw_facts['mounts']['/']['size_total'] == 1024
    assert hw_facts['mounts']['/']['space_avail'] == 1023


# Generated at 2022-06-13 01:00:58.368491
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """
    Test populating of HurdHardware class
    :return:
    """
    hh = HurdHardware()
    assert hh is not None
    collected = hh.populate()
    assert "uptime" in collected
    assert "kernel" in collected
    assert "uptime_seconds" in collected
    assert "memfree_mb" in collected
    assert "swapfree_mb" in collected
    assert "memtotal_mb" in collected
    assert "swaptotal_mb" in collected
    assert "vmalloc_total" in collected

# Generated at 2022-06-13 01:01:07.354925
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    h = HurdHardware()
    result = h.populate()

    # Check memory facts
    assert 'Memory' in result
    assert result['Memory']['MemTotal'] > 0
    assert result['Memory']['SwapTotal'] == 0
    assert 'MemFree' in result['Memory']
    assert 'SwapFree' in result['Memory']
    assert 'SwapCached' in result['Memory']
    assert 'Buffers' in result['Memory']
    assert 'Active' in result['Memory']
    assert 'Inactive' in result['Memory']
    assert 'AnonPages' in result['Memory']
    assert 'Cached' in result['Memory']
    assert 'Active(anon)' in result['Memory']
    assert 'Inactive(anon)' in result['Memory']
    assert 'Active(file)' in result['Memory']


# Generated at 2022-06-13 01:01:09.826905
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware_facts = HurdHardware().populate()
    print(hardware_facts)
    assert 'uptime_seconds' in hardware_facts


# Generated at 2022-06-13 01:01:13.075882
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware = HurdHardware()
    collected_facts = hardware.populate()
    assert collected_facts['uptime_seconds'] is not None
    assert collected_facts['memtotal_mb'] is not None
    assert collected_facts['mounts'] is not None

# Generated at 2022-06-13 01:01:18.917881
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    class MockModule(object):
        pass

    module = MockModule()
    module.params = {'gather_timeout': 1}

    def mock_get_processor_facts_dict(facts):
        facts['processor'] = (['cpu0', 'cpu1'], 'Intel(R) Core(TM) i7-4600U CPU @ 2.10GHz')

    def mock_get_uptime_facts_dict(facts):
        facts['uptime_seconds'] = 117415.76

    def mock_get_memory_facts_dict(facts):
        facts['memtotal_mb'] = 8056.06


# Generated at 2022-06-13 01:01:27.472829
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    import json

    # Mock facts collected from GNU Hurd
    facts = {
        'system': 'GNU',
        'distribution': 'GNU/Hurd',
        'distribution_version': '1.0'
    }

    # Test method populate of class HurdHardware
    hurd_hw = HurdHardware()
    hw_facts = hurd_hw.populate(facts)

    # Compare with reference results from a GNU Hurd machine
    with open('test/unit/test_utils/test_facts/test_hardware/GNU_ref.json', 'r') as ref_file:
        ref = json.load(ref_file)

    assert hw_facts == ref

# Generated at 2022-06-13 01:01:35.077357
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware_facts = {}

    # Testing LinuxHardware.get_uptime_facts()
    output = """100.02 2467.10
"""
    runner_mock = RunnerMock(
        module='linux_facts.get_uptime_facts',
        module_args={'file_exists': True},
        module_result={
            'failed': False,
            'changed': False,
            'ansible_facts': {'uptime_seconds': 100.02, 'uptime_minutes': 1.67, 'uptime_hours': 0.028, 'uptime_days': 0.00047}
        },
        module_output=output
    )
    hardware_facts.update(runner_mock.get_uptime_facts())

    # Testing LinuxHardware.get_memory_facts()

# Generated at 2022-06-13 01:01:36.747339
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hw = HurdHardware()
    hw.collect()

    # Assert that populating all facts does not raise an exception
    hw.populate()

# Generated at 2022-06-13 01:02:22.085522
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    h_facts = HurdHardware()
    collected_facts = {}
    hardware_facts = h_facts.populate(collected_facts)

    assert hardware_facts['uptime_hours'] > 0
    assert hardware_facts['uptime_seconds'] > 0

    assert 'MemTotal' in hardware_facts['mem_facts']
    assert 'MemFree' in hardware_facts['mem_facts']
    assert 'SwapTotal' in hardware_facts['mem_facts']
    assert 'SwapFree' in hardware_facts['mem_facts']

    assert 'mounts' in hardware_facts

# Generated at 2022-06-13 01:02:26.504993
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hw = HurdHardware()
    hw_facts = hw.populate()
    assert 'uptime' in hw_facts
    assert 'uptime_seconds' in hw_facts
    assert 'memory_mb' in hw_facts
    assert 'swapfree_mb' in hw_facts
    assert 'mounts' in hw_facts
    assert 'mounts' in hw_facts

# Generated at 2022-06-13 01:02:27.214954
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware = HurdHardware()
    hardware.populate()

# Generated at 2022-06-13 01:02:38.459706
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hardware = HurdHardware()
    fact_names = ['uptime', 'uptime_seconds', 'uptime_hours',
                  'uptime_days', 'mounts', 'swapfree_mb', 'swaptotal_mb',
                  'memtotal_mb', 'memfree_mb', 'memavailable_mb']
    facts = hurd_hardware.populate()

    # Test that we got the correct facts
    assert len(facts) == len(fact_names)
    for fact_name in fact_names:
        assert fact_name in facts

    # Test that we got valid data
    assert isinstance(facts['uptime_seconds'], int)
    assert isinstance(facts['uptime_hours'], int)
    assert isinstance(facts['uptime_days'], int)

# Generated at 2022-06-13 01:02:42.637425
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    class MockHardwareLinux(HurdHardware):
        def get_uptime_facts(self):
            return {"uptime": "0:00"}

        def get_memory_facts(self):
            return {}

        def get_mount_facts(self):
            return {}

    hw = MockHardwareLinux()
    assert hw.populate() == {
        'uptime': '0:00'
    }

# Generated at 2022-06-13 01:02:51.549864
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hw = HurdHardware()
    hw._collect_file_facts = lambda *args, **kwargs: {}
    hw._parse_meminfo = lambda *args, **kwargs: {}
    hw._parse_mountinfo = lambda *args, **kwargs: {}
    hw._parse_swaps = lambda *args, **kwargs: {}
    hw._parse_uptime = lambda *args, **kwargs: {}
    hw._get_cmdline = lambda *args, **kwargs: {}
    hw._parse_cpus = lambda *args, **kwargs: {}
    output = hw.populate()
    assert output['uptime_seconds'] == 0
    assert output['uptime_hours'] == 0
    assert output['uptime_days'] == 0

# Generated at 2022-06-13 01:02:52.950628
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd = HurdHardware()
    hurd_facts = hurd.populate()
    assert 'mounts' in hurd_facts

# Generated at 2022-06-13 01:02:59.540326
# Unit test for method populate of class HurdHardware

# Generated at 2022-06-13 01:03:10.278214
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    import json
    import os
    import sys

    dirname = os.path.dirname(__file__)
    output_file_path = os.path.join(dirname, 'proc_mounts')

    if sys.version_info.major >= 3:
        output_text = open(output_file_path, encoding='utf-8').read()
    else:
        output_text = open(output_file_path).read()


# Generated at 2022-06-13 01:03:17.446080
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hw = HurdHardware(module=None)

    hw.get_mount_facts = lambda: {'mounts': 'this is mount facts'}
    hw.get_uptime_facts = lambda: {'uptime': 'this is uptime facts'}
    hw.get_memory_facts = lambda: {'memory': 'this is memory facts'}

    hw.populate()

    assert hw.facts['uptime'] == 'this is uptime facts'
    assert hw.facts['memory'] == 'this is memory facts'
    assert hw.facts['mounts'] == 'this is mount facts'

# Generated at 2022-06-13 01:04:51.718669
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurdhw = HurdHardware()
    retfacts = hurdhw.populate()
    assert retfacts['memory']['swap']['total'] == 3331
    assert retfacts['memory']['swap']['avail'] == 3331
    assert retfacts['memory']['swap']['used'] == 0
    assert retfacts['memory']['swap']['free'] == 3331
    assert retfacts['memory']['swap']['percent'] == 0.0
    assert retfacts['memory']['swap']['sin'] == 0
    assert retfacts['memory']['swap']['sout'] == 0
    assert retfacts['memory']['memtotal'] == 934
    assert retfacts['memory']['memfree'] == 934

# Generated at 2022-06-13 01:04:56.856963
# Unit test for method populate of class HurdHardware

# Generated at 2022-06-13 01:04:58.776807
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hardware = HurdHardware()
    assert isinstance(hurd_hardware.populate(), dict)


# Generated at 2022-06-13 01:05:06.797196
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # create an instance of class HurdHardware
    hurd_hardware = HurdHardware()

    # create an instance of class HurdHardwareCollector
    hurd_hardware_collector = HurdHardwareCollector()

    # call method populate of class HurdHardware
    facts = hurd_hardware.populate(collected_facts=hurd_hardware_collector.get_facts())

    # check the result

# Generated at 2022-06-13 01:05:14.968729
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    data = {
        'ansible_facts': {
            'ansible_uptime_seconds': 300,
            'ansible_mounts': [
                {'mount': '/', 'size_available': 4190260224,
                 'size_total': 4190332928, 'device': '/dev/sda3', 'fstype': 'ext4'},
                {'mount': '/boot', 'size_available': 4190260224,
                 'size_total': 4190416896, 'device': '/dev/sda1', 'fstype': 'ext4'},
            ]
        }
    }

    hardware = HurdHardware()
    collected_facts = hardware.populate()

    assert collected_facts['uptime_seconds'] == 300
    assert collected_facts['memtotal_mb'] > 0
    assert collected_

# Generated at 2022-06-13 01:05:16.477077
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hw = HurdHardware()
    hw.collect()
    assert hw.facts['uptime_seconds']
    assert hw.facts['memory_mb']['real']['total']

# Generated at 2022-06-13 01:05:23.728903
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hardware = HurdHardware()

    # Create fake facts collected from system
    collected_facts = {
        'system': 'GNU',
        'distribution': 'GNU',
        'distribution_release': 'hurd',
        'distribution_version': '18.5'
    }

    # Create fake uptime and memory informations that we expect to have in facts
    expected_uptime_facts = {
        'uptime_seconds': 33673,
        'uptime_days': 0
    }


# Generated at 2022-06-13 01:05:25.407589
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurdhw = HurdHardware()
    assert hurdhw.populate() is not None

# Generated at 2022-06-13 01:05:30.414141
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware = HurdHardware({})
    hardware.populate()
    assert hardware.memory_facts['MemTotal'] == 4172460
    assert hardware.uptime_facts['uptime'] == 1384
    assert hardware.uptime_facts['uptime_hours'] == 1
    assert hardware.uptime_facts['uptime_days'] == 0
    assert hardware.uptime_facts['uptime_seconds'] == 1384
    assert hardware.mount_facts['/'] == '/dev/hd0'

# Generated at 2022-06-13 01:05:32.212125
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    h = HurdHardware()
    hw_facts = h.populate()
    # Verify the correct dictionaries were created
    assert 'memory' in hw_facts
    assert 'uptime' in hw_facts
