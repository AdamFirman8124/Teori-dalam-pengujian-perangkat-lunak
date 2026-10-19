

# Generated at 2022-06-13 00:55:48.378614
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    from ansible.module_utils.facts.timeout import TimeoutError
    import os
    import stat
    from ansible.module_utils.facts.hardware.linux import LinuxHardware

    # A basic mocked implementation of the class LinuxHardware
    class MockLinuxHardware(LinuxHardware):
        def get_uptime_facts(self):
            return {'uptime_seconds': 1,
                    'uptime_string': '1'}

        def get_memory_facts(self):
            return {'memtotal_mb': 2,
                    'memfree_mb': 1,
                    'swaptotal_mb': 4,
                    'swapfree_mb': 3}

        def get_mount_facts(self):
            raise TimeoutError()

    setattr(os, 'stat', lambda *args: stat.S_IFDIR)
    hurd_

# Generated at 2022-06-13 00:55:54.467666
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware = HurdHardware()
    # Test without timeout
    facts = hardware.populate()
    assert 'uptime' in facts
    assert 'memtotal_mb' in facts
    assert 'memfree_mb' in facts
    assert 'swaptotal_mb' in facts
    assert 'swapfree_mb' in facts
    # Test with timeout
    hardware = HurdHardware()
    hardware.get_mount_facts = lambda: TimeoutError()
    facts = hardware.populate()
    assert 'mounts' not in facts

# Generated at 2022-06-13 00:56:00.269235
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    tmp_dir = mkdtemp()
    procfs_mock = MagicMock()
    procfs_mock.mount_point = tmp_dir
    os_subprocess_mock = MagicMock()
    with patch('ansible.module_utils.facts.hardware.linux.subprocess', os_subprocess_mock):
        with patch('ansible.module_utils.facts.hardware.base.subprocess', os_subprocess_mock):
            with patch('ansible.module_utils.facts.hardware.linux.ProcFS', procfs_mock):
                hardware = HurdHardware()
                assert hardware.populate()

# Generated at 2022-06-13 00:56:01.281156
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurdhw = HurdHardware()
    assert hurdhw.populate() is not None

# Generated at 2022-06-13 00:56:05.306458
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware_facts = {
        'uptime_seconds': '2097885',
        'uptime_seconds_readable': '24 days, 3 hours, 40 minutes, 5 seconds',
        'memfree_mb': '1388.97',
        'memtotal_mb': '8192.00',
        'swapfree_mb': '8191.90',
        'swaptotal_mb': '8191.99',
        'mounts': [{
            'filesystem': '/dev/sda1',
            'mount': '/boot/efi',
        }]
    }
    hurd = HurdHardware()

    assert (hurd.populate() == hardware_facts)

# Generated at 2022-06-13 00:56:08.770927
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    '''
    Test for method populate of class HurdHardware
    '''

    # Collecting all the facts
    linux_hardware_obj = HurdHardware()
    result = linux_hardware_obj.populate()
    assert isinstance(result, dict) is True


# Generated at 2022-06-13 00:56:16.488264
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware = HurdHardware()
    hardware_facts = hardware.populate()

    hostname = hardware_facts.get('ansible_fqdn', hardware_facts.get('ansible_hostname'))

    assert hardware_facts['ansible_system'] == 'GNU'
    assert hardware_facts['ansible_machine'] == 'i486'
    assert isinstance(hardware_facts['ansible_all_ipv4_addresses'], list)
    assert hardware_facts['ansible_processor'] == 'i486'
    assert hardware_facts['ansible_processor_cores'] == 1
    assert isinstance(hardware_facts['ansible_memtotal_mb'], int)
    assert hardware_facts['ansible_hostname'] == hostname

# Generated at 2022-06-13 00:56:25.292846
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    import pytest
    import os
    import subprocess
    from ansible.module_utils.facts.hardware.hurd import HurdHardware
    # Create test data
    facts = {'ansible_uptime_seconds': 3782988.75 }
    facts['ansible_memfree_mb'] = 0
    facts['ansible_kernel'] = b'GNU/Hurd'

    # Patch os.access to alway allow access
    @staticmethod
    def mock_access_side_effect(path, mode):
        return True

    # read return value

# Generated at 2022-06-13 00:56:28.132530
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # This mostly tests the mount fact gathering
    hw = HurdHardware()
    facts = hw.populate()
    assert facts['mounts']


if __name__ == '__main__':
    import pytest
    pytest.main([__file__])

# Generated at 2022-06-13 00:56:31.875731
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hw = HurdHardware()
    uptime_facts = hw.get_uptime_facts()
    memory_facts = hw.get_memory_facts()

    mount_facts = {}
    try:
        mount_facts = hw.get_mount_facts()
    except TimeoutError:
        pass

    hardware_facts = hw.populate()
    assert hardware_facts == dict(uptime_facts, **memory_facts, **mount_facts)

# Generated at 2022-06-13 00:56:36.267290
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    facter = HurdHardware()
    fact_data = facter.populate()
    assert 'swapfree_mb' in fact_data
    #assert 'memtotal_mb' in fact_data
    #assert 'memfree_mb' in fact_data
    #assert 'mounts' in fact_data

# Generated at 2022-06-13 00:56:40.405296
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # We first create a test object of class HurdHardware
    test_object = HurdHardware()

    # We then use it to set the state of the GNU/Hurd system under test
    # to a known state.
    test_object.set_initial_state()

    # Then we run the method under test.
    test_object.populate()

# Generated at 2022-06-13 00:56:43.897587
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    facts = HurdHardware().populate()
    assert 'uptime' in facts
    assert 'uptime_seconds' in facts
    assert 'memory' in facts
    assert 'mounts' in facts


# Generated at 2022-06-13 00:56:52.285614
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    import os
    import stat
    from ansible.module_utils.facts.hardware.hurd import HurdHardware
    from ansible.module_utils.facts.facts import Facts

    facts = Facts(module=None)

    # Setup procfs compatibility translator
    facts_dir = os.path.join(os.path.dirname(__file__),
                             '../../../../testing/lib/ansible_test/_data/facts/hurd/')
    procfs = os.path.join(facts_dir, 'proc')
    os.mkdir(procfs)
    os.chmod(procfs, stat.S_IRWXU | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH)

# Generated at 2022-06-13 00:56:58.423426
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    def mocked_get_uptime_facts(self):
        return {'uptime_seconds': 10}

    def mocked_get_memory_facts(self):
        return {'memory_mb': {'real': {'total': 1},
                              'swap': {'total': 2}}}

    def mocked_get_mount_facts(self):
        return {'mounts': []}

    hf = HurdHardware()
    hf.get_uptime_facts = mocked_get_uptime_facts
    hf.get_memory_facts = mocked_get_memory_facts
    hf.get_mount_facts = mocked_get_mount_facts

# Generated at 2022-06-13 00:56:59.616380
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hardware = HurdHardware()
    hurd_hardware.populate()

# Generated at 2022-06-13 00:57:03.245640
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hardware = HurdHardware()

    # We can't test without GNU/Hurd port, so raise ImportError
    import socket
    raise ImportError()

    # Assert that no exception is raised under normal circumstances
    hurd_hardware.populate()

# Generated at 2022-06-13 00:57:06.925695
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """
    HurdHardware.populate() should return a dict with facts
    """
    obj = HurdHardware()
    facts = obj.populate()
    assert isinstance(facts, dict)
    assert len(facts) > 0

# Generated at 2022-06-13 00:57:08.870594
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hw = HurdHardware()
    collected_facts = {}
    hw.populate(collected_facts)
    assert hw


# Generated at 2022-06-13 00:57:13.177237
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():

    # Ensure the default Hardware.populate() method works.
    h_obj = HurdHardware()
    result = h_obj.populate()
    assert result is not None
    assert 'uptime' in result
    assert 'memfree_mb' in result
    assert 'memtotal_mb' in result
    assert 'swapfree_mb' in result
    assert 'swaptotal_mb' in result

# Generated at 2022-06-13 00:57:16.059629
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    fact = HurdHardware()
    fact.collect()

    # method populate should add items to the facts dict
    assert bool(fact.facts)

# Generated at 2022-06-13 00:57:20.199674
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hw_mocker = HurdHardware(dict())
    result = hw_mocker.populate()
    assert result
    assert result['uptime_seconds'] > 0
    assert result['memtotal_mb'] != 0
    assert result['memfree_mb'] != 0
    assert result['swaptotal_mb'] is not None
    assert result['swapfree_mb'] is not None



# Generated at 2022-06-13 00:57:31.119947
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware = HurdHardware()
    hardware.get_uptime_facts = lambda: {'uptime_seconds': 123,
                                         'uptime_hours': 1}
    hardware.get_memory_facts = lambda: {'memtotal_mb': 123,
                                         'memfree_mb': 14}
    hardware.get_mount_facts = lambda: {'/': {'device': 'foo',
                                              'mount': '/'},
                                        '/home': {'device': 'bar',
                                                  'mount': '/home'}}
    hardware.populate()
    assert hardware.facts['uptime_seconds'] == 123
    assert hardware.facts['uptime_hours'] == 1
    assert hardware.facts['memtotal_mb'] == 123
    assert hardware.facts['memfree_mb'] == 14

# Generated at 2022-06-13 00:57:35.186777
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    class test_args():
        pass
    args = test_args()
    args.filter = None
    hw = HurdHardware(module=args)

    facts = hw.populate()
    assert 'memfree_mb' in facts
    assert 'swapfree_mb' in facts
    assert 'uptime_seconds' in facts
    assert 'mounts' in facts

# Generated at 2022-06-13 00:57:40.523768
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    import os
    import tempfile
    from ansible.module_utils._text import to_bytes

    hurd_meminfo = """
MemTotal:        1024 kB
"""
    with tempfile.NamedTemporaryFile(prefix='ansible_meminfo_') as meminfo:
        meminfo.write(to_bytes(hurd_meminfo))
        meminfo.flush()

        hurd_uptime = """
  12.00 (seconds)  up  0.00 (users)
"""
        with tempfile.NamedTemporaryFile(prefix='ansible_uptime_') as uptime:
            uptime.write(to_bytes(hurd_uptime))
            uptime.flush()


# Generated at 2022-06-13 00:57:42.035656
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware_facts = HurdHardware()
    assert hardware_facts.populate()

# Generated at 2022-06-13 00:57:47.798337
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hw = HurdHardware()

    facts = hurd_hw.populate()

    assert isinstance(facts, dict)
    assert 'uptime_seconds' in facts
    assert 'uptime_hours' in facts
    assert 'uptime_days' in facts
    assert 'virtual_memory' in facts
    assert 'memory_mb' in facts
    assert 'mounts' in facts
    assert isinstance(facts['mounts'], list)

# Generated at 2022-06-13 00:57:56.898545
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():

    target_fields = [
        'uptime',
        'uptime_seconds',
        'memoryfree_mb',
        'memoryfree_gb',
        'memoryfree',
        'memtotal_mb',
        'memtotal_gb',
        'memtotal',
        'swapfree_mb',
        'swapfree_gb',
        'swapfree',
        'swaptotal_mb',
        'swaptotal_gb',
        'swaptotal',
        'mounts'
    ]

    hurd_hardware = HurdHardware()

    assert all(field in hurd_hardware.populate() for field in target_fields)

# Generated at 2022-06-13 00:57:58.852706
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    h = HurdHardware()
    h.populate()
    assert h.uptime
    assert h.uptime.seconds
    assert h.uptime.days


# Generated at 2022-06-13 00:58:07.043472
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    from ansible.module_utils.facts.hardware.hurd import HurdHardware
    hardware = HurdHardware()

    fake_uptime_facts = dict(
        uptime_seconds=123456789,
        uptime_days=56,
        uptime_hours=14,
        uptime_minutes=13
        )

    fake_memory_facts = dict(
        ram=dict(
            total=15000000,
            used=6600000,
            free=8400000,
            free_percent=56,
            ),
        swap=dict(
            total=15000000,
            used=6600000,
            free=8400000,
            free_percent=56,
            ),
        )


# Generated at 2022-06-13 00:58:16.513921
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    HardwareCollector.KERNEL_NAME = 'GNU'
    hardware_collector = HurdHardwareCollector()
    hardware_facts = hardware_collector.collect(dict())
    assert hardware_facts['uptime_seconds'] == 148
    assert hardware_facts['uptime_hours'] == 0
    assert hardware_facts['uptime_days'] == 0

# Generated at 2022-06-13 00:58:23.788426
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    module_mock = Mock()
    class_mock.return_value = module_mock
    module_mock.get_memory_facts.return_value = {'memory_mb': 4, 'swap_mb': 1}
    module_mock.get_mount_facts.return_value = {'mounts': []}
    module_mock.get_uptime_facts.return_value = {'uptime_seconds': 12345}
    facts = module_mock.populate()
    assert facts == {'memory_mb': 4, 'swap_mb': 1, 'mounts': [], 'uptime_seconds': 12345}



# Generated at 2022-06-13 00:58:32.737972
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """
    Test HurdHardware.populate()
    """

    class MockHurdHardware(HurdHardware):

        def __init__(self, params):
            super(MockHurdHardware, self).__init__(params)
            self.get_uptime_facts_called = False
            self.get_memory_facts_called = False
            self.get_mount_facts_called = False

        def get_uptime_facts(self):
            self.get_uptime_facts_called = True
            return {'uptime_seconds': 4823.0}

        def get_memory_facts(self):
            self.get_memory_facts_called = True
            return {'memfree_mb': 489.732421875, 'memtotal_mb': 781.443359375}


# Generated at 2022-06-13 00:58:43.375562
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # Test if populate returns a dict object
    hardware = HurdHardware()

    collected_facts = {'product_name': 'GNU',
                       'kernel': 'GNU/Hurd',
                       'uptime_seconds': 0,
                       'memory_mb': {'total': 0, 'real': 0, 'swap': 0,
                                     'real_mb': 0, 'swap_mb': 0},
                       'mounts': [{'device': '/dev/hd0', 'mount': '/'}]}

    expected_facts = {'uptime': 0,
                      'memory': {'total_mb': 0, 'real_mb': 0,
                                 'swap_mb': 0},
                      'mounts': [{'device': '/dev/hd0', 'mount': '/'}]}

    hardware_facts = hardware.populate

# Generated at 2022-06-13 00:58:50.130590
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # Test 1: Input kernel_version = 3.18
    test_1 = HurdHardware()
    test_1.collector = {'kernel': 'GNU/Hurd'}
    facts = test_1.populate()
    assert facts['uptime'] <= 1
    assert facts['uptime_seconds'] <= 1
    assert facts['uptime_hours'] == 0
    assert facts['uptime_days'] == 0
    assert facts['memfree_mb'] <= 1
    assert facts['memtotal_mb'] <= 1
    assert facts['swapfree_mb'] <= 1
    assert facts['swaptotal_mb'] <= 1

# Generated at 2022-06-13 00:58:59.262807
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    import platform
    from . import linux_mem

    h = HurdHardware()
    # To test the method, we need to mock the module_utils functions
    # get_mount_facts, get_memory_facts, get_uptime_facts, and
    # get_distribution
    class MockModuleUtils(object):
        def get_mount_facts(self):
            return {}
        def get_memory_facts(self):
            return linux_mem.linux_mem_info()
        def get_uptime_facts(self):
            return {}
        def get_distribution(self):
            return {'vendor': 'GNU', 'version': platform.version()}

    # get_memory_facts() is not expected to raise TimeoutError
    hardware_facts = h.populate(MockModuleUtils())
    hardware_

# Generated at 2022-06-13 00:59:07.142354
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hardware = HurdHardware()
    collected_facts = hurd_hardware.populate()
    # Checking if memory facts are present
    assert 'mem_total' in collected_facts
    assert 'mem_free' in collected_facts
    assert 'mem_available' in collected_facts
    assert 'swap_total' in collected_facts
    assert 'swap_free' in collected_facts
    assert 'swap_available' in collected_facts
    # Checking if uptime fact is present
    assert 'uptime_seconds' in collected_facts
    # Checking if mounts facts are present
    assert 'mounts' in collected_facts
    # Checking if dirs facts are present
    assert 'dirs' in collected_facts

# Generated at 2022-06-13 00:59:14.874792
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    class MockUptime:
        """The mock of Uptime class for testing."""
        def __init__(self):
            self.up_time = (100, 10, 5)

    class MockMemory:
        """The mock of Memory class for testing."""
        def __init__(self):
            self.total = 123456789
            self.swap_total = 987654321

    class MockMount:
        """The mock of Mount class for testing."""
        def __init__(self):
            self.mounts = [{
                'type': 'ext4',
                'mount': '/',
                'device': '/dev/sda1',
            }]

    class MockHurdHardware:
        """The mock of HurdHardware class for testing."""

# Generated at 2022-06-13 00:59:18.006050
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    obj = HurdHardware()
    result = obj.populate()
    assert result is not None

# Generated at 2022-06-13 00:59:27.369629
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware_facts = HurdHardware()
    collected_facts = {}
    hardware_facts.populate(collected_facts)

    def assert_fact_exists(fact):
        assert hardware_facts.populate.__name__ in collected_facts
        assert fact in collected_facts[hardware_facts.populate.__name__]

    assert_fact_exists('uptime')
    assert_fact_exists('uptime_days')
    assert_fact_exists('uptime_hours')
    assert_fact_exists('uptime_seconds')
    assert_fact_exists('memory')
    assert_fact_exists('memory_mb')
    assert_fact_exists('swap')
    assert_fact_exists('swap_mb')

# Generated at 2022-06-13 00:59:30.885617
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hw = HurdHardware()
    hw_facts = hw.populate()
    assert 'uptime' in hw_facts
    assert 'uptime_seconds' in hw_facts
    assert 'memfree_mb' in hw_facts
    assert 'memtotal_mb' in hw_facts

# Generated at 2022-06-13 00:59:31.881356
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    from ansible.module_utils.facts.hardware.linux import LinuxHardware
    h = LinuxHardware()
    h.populate()
    assert type(h.populate()) is dict

# Generated at 2022-06-13 00:59:38.637242
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    import time
    import sys
    import os

    class MockTimeoutError(Exception):
        def __init__(self, *args, **kwargs):
            Exception.__init__(self, *args, **kwargs)

    class MockHurdHardware(HurdHardware):
        def get_uptime_facts(self):
            return {'uptime_seconds': 0}

        def get_memory_facts(self):
            return {'memtotal_mb': 0}

        def get_mount_facts(self):
            raise MockTimeoutError('Timed out')

    # Mock sys.platform to GNU
    current_platform = sys.platform
    sys.platform = 'GNU'

    # Mock os.path.exists
    current_os_path_exists = os.path.exists

# Generated at 2022-06-13 00:59:43.412619
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    a = HurdHardware()
    facts = a.populate()

    print(facts)

    assert isinstance(facts, dict)
    assert 'memfree_mb' in facts
    assert 'memtotal_mb' in facts
    assert 'swapfree_mb' in facts
    assert 'swaptotal_mb' in facts
    assert 'mounts' in facts

# Generated at 2022-06-13 00:59:44.242749
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd = HurdHardware()
    hurd.populate()

# Generated at 2022-06-13 00:59:47.357929
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware = HurdHardware()
    hardware_facts = hardware.populate()

    # For some unknown reason this is not working on travis
    # assert isinstance(hardware_facts, dict)

    assert len(hardware_facts) > 0

# Generated at 2022-06-13 00:59:48.911295
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hw = HurdHardware({})
    # default values
    assert hw.populate() == {}

# Generated at 2022-06-13 00:59:53.012305
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hw = HurdHardware()
    # Test facts, to be populated
    collected_facts = dict()
    # Check if facts are populated with tested method
    populated_facts = hurd_hw.populate(collected_facts)
    # Test if facts are populated
    assert isinstance(populated_facts, dict) and populated_facts

# Generated at 2022-06-13 01:00:00.064713
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hw_collector = HurdHardwareCollector()

    collected_facts = {
        u'ansible_machine': u'x86_64',
        u'ansible_memtotal_mb': 8192,
        u'ansible_os_family': u'GNU/kFreeBSD',
        u'ansible_pkg_mgr': u'deb',
        u'ansible_processor_cores': 4,
        u'ansible_system': u'Debian',
        u'ansible_system_vendor': u'PCI device 0x8086:0x1510',
        u'ansible_virtualization_role': u'host',
        u'ansible_virtualization_type': u'physical',
        u'ansible_kernel': u'4.15.0-1-gnu',
    }



# Generated at 2022-06-13 01:00:03.265421
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hardware_collector = HurdHardwareCollector()
    hurd_hardware = hurd_hardware_collector.collect()
    assert 'ansible_mounts' in hurd_hardware
    assert 'ansible_memtotal_mb' in hurd_hardware



# Generated at 2022-06-13 01:00:06.823148
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    assert type(HurdHardware().populate()) == dict

# Generated at 2022-06-13 01:00:08.418189
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """Unit test for method populate of class HurdHardware."""
    test_instance = HurdHardware()
    assert test_instance.populate()

# Generated at 2022-06-13 01:00:11.283542
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    "Test ansible.module_utils.facts.hardware.HurdHardware.populate"
    # Create an instance of HurdHardware
    hardware = HurdHardware()
    # Populate the instance
    hardware.populate()
    # Assert that the fact 'mounts' is not empty
    assert len(hardware.facts['mounts']) >= 2

# Generated at 2022-06-13 01:00:20.458232
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # Test case
    hurd_hardware_obj = HurdHardware()
    result = hurd_hardware_obj.populate()

    assert result
    assert result['uptime']
    assert result['uptime']['seconds']
    assert result['memtotal_mb']
    assert result['memfree_mb']
    assert result['swaptotal_mb']
    assert result['swapfree_mb']
    assert result['mounts']
    assert result['mounts']['/,/hurd']
    assert result['mounts']['/,/hurd']['device'] == '/dev/hd0s1'
    assert result['mounts']['/,/hurd']['mount'] == '/'


# Generated at 2022-06-13 01:00:23.777934
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # TODO: should test with real procfs data
    collected_facts = {}
    h = HurdHardware(collected_facts)
    result = h.populate()
    assert 'uptime_seconds' in result
    assert 'uptime_days' in result
    assert 'memory_mb' in result
    assert 'memory_mb_raw' in result
    assert 'mounts' in result

# Generated at 2022-06-13 01:00:29.357554
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hw = HurdHardware()
    hw_facts_dict = hw.populate()
    assert hw_facts_dict['uptime_seconds'] == 1
    assert hw_facts_dict['memory_mb']['real']['total'] == 2
    assert hw_facts_dict['mounts'] == [{'mount': 'path', 'device': '/dev/fake_device'}]

# Generated at 2022-06-13 01:00:33.624301
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """
    Basic test for method populate of class HurdHardware.
    """
    from ansible.module_utils.facts.hardware.hurd import HurdHardware
    hurdhw = HurdHardware()

    assert isinstance(hurdhw.populate(), dict)

# Generated at 2022-06-13 01:00:43.134700
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # create a subclass of HurdHardware to access protected methods
    class MyHurdHardware(HurdHardware):
        def __init__(self):
            pass

        def get_uptime_facts(self):
            return {'uptime_seconds': 77, 'uptime_days': 0}

        def get_memory_facts(self):
            return {'memtotal_mb': 123, 'memfree_mb': 456}

        def get_mount_facts(self):
            return {'mounts': [{'device': '/dev/sda1', 'mount': '/'}, {'device': 'none', 'mount': '/dev'}], 'fstypes': {'/dev/sda2': 'ext3'}}

    # create the MyHurdHardware instance
    obj_HurdHardware = MyHurdHardware()

    # create expected

# Generated at 2022-06-13 01:00:44.737926
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    collector = HurdHardwareCollector()
    facts = collector.collect()
    assert facts['uptime']

# Generated at 2022-06-13 01:00:52.323471
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():

    from ansible.module_utils.facts.facts import Facts
    from ansible.module_utils.facts.timeout import TimeoutError
    from ansible.module_utils.facts.hardware.hurd import HurdHardware

    # mock get_uptime_facts
    def mock_get_uptime_facts():
        return {'uptime': '1343793.79 10320.22'}
    HurdHardware.get_uptime_facts = mock_get_uptime_facts

    # mock get_memory_facts
    def mock_get_memory_facts():
        return {'memory': {'total': '16384', 'free': '16384'}}
    HurdHardware.get_memory_facts = mock_get_memory_facts

    # mock get_mount_facts

# Generated at 2022-06-13 01:01:03.734183
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware_instance = HurdHardware()
    hardware_facts = hardware_instance.populate()
    assert hardware_facts['uptime']
    assert hardware_facts['uptime_seconds']
    assert hardware_facts['memfree_mb']
    assert hardware_facts['memtotal_mb']


# Generated at 2022-06-13 01:01:05.099118
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hw = HurdHardware()
    return hw.populate()

# Generated at 2022-06-13 01:01:13.916772
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware = HurdHardware()
    hardware_facts = hardware.populate()
    assert hardware_facts['uptime_seconds'] > 0
    assert hardware_facts['uptime_hours'] > 0
    assert hardware_facts['uptime_days'] > 0
    assert hardware_facts['uptime_seconds'] == hardware_facts['uptime_minutes'] * 60
    assert hardware_facts['uptime_minutes'] == hardware_facts['uptime_hours'] * 60
    assert hardware_facts['uptime_hours'] == hardware_facts['uptime_days'] * 24
    assert hardware_facts['memtotal_mb'] > 0
    assert hardware_facts['memfree_mb'] > 0
    assert hardware_facts['memavailable_mb'] > 0
    assert hardware_facts['swaptotal_mb'] > 0

# Generated at 2022-06-13 01:01:19.654836
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # pylint: disable=import-error
    from ansible.module_utils.facts.hardware.hurd import HurdHardware
    hardware = HurdHardware()
    hardware_facts = hardware.populate()
    assert hardware_facts['uptime_seconds'] == 0
    assert hardware_facts['memory_mb']['real']['total'] == 0.0

# Generated at 2022-06-13 01:01:21.198682
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hw = HurdHardware()

    assert hw.populate()

# Generated at 2022-06-13 01:01:23.117830
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    obj = HurdHardware()
    obj.populate()
    assert(obj.memtotal is not None)

# Generated at 2022-06-13 01:01:27.515768
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    comm = 'getconf.sh'
    h = HurdHardware(module=None, resource_facts=None)
    h.module.run_command = lambda x: (0, '', '')
    h.module.get_bin_path = lambda x: comm
    collected_facts = h.populate()
    assert collected_facts == {}

# Generated at 2022-06-13 01:01:35.156255
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # This test checks that the mock HurdHardware.get_mount_facts() method
    # is called once with two arguments which are the set of collected facts
    # and a timeout value of 2.0
    from ansible.module_utils.facts.hardware.hurd import HurdHardware
    from ansible.module_utils.facts.hardware.linux import LinuxHardware
    hardware = HurdHardware()
    hardware.get_mount_facts = mock.Mock()
    hardware.get_mount_facts.return_value = {'mounts': []}
    hardware.populate(collected_facts={'created_by_ansible_version': '1.2.3'}, timeout=2.0)

# Generated at 2022-06-13 01:01:41.801086
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurdhw = HurdHardware()

    collected_facts = {
        'system': 'GNU/Hurd',
    }

    expected = {
        'uptime_seconds': 0,
        'uptime_seconds_readable': '0 seconds',
        'memfree_mb': 0,
        'memtotal_mb': 0,
        'swapfree_mb': 0,
        'swaptotal_mb': 0,
        'mounts': [],
    }

    uptime_facts = hurdhw.get_uptime_facts()
    memory_facts = hurdhw.get_memory_facts()

    mount_facts = {}
    try:
        mount_facts = hurdhw.get_mount_facts()
    except TimeoutError:
        pass

    facts = {}
    facts.update(uptime_facts)
    facts

# Generated at 2022-06-13 01:01:42.917410
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hw = HurdHardware()

    assert hw.populate()


# Generated at 2022-06-13 01:02:01.045721
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # Test case 1:
    hurd = HurdHardware()
    expected_result = {'dummy_key': 'dummy_value'}
    hurd.get_uptime_facts = lambda: {'dummy_key': 'dummy_value'}
    hurd.get_memory_facts = lambda: {'memory_facts': {}}
    hurd.get_mount_facts = lambda: {'mount_facts': {}}
    assert (hurd.populate() == expected_result)

    # Test case 2:
    hurd = HurdHardware()
    expected_result = {'dummy_key': 'dummy_value'}
    hurd.get_uptime_facts = lambda: {'dummy_key': 'dummy_value'}
    hurd.get_memory_facts = lambda: {'memory_facts': {}}


# Generated at 2022-06-13 01:02:03.520488
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    import ansible.module_utils.facts.hardware.hurd
    hardware = ansible.module_utils.facts.hardware.hurd.HurdHardwareCollector
    hardware.populate()

# Generated at 2022-06-13 01:02:07.765022
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """
    Test case for testing the populate method
    """
    hw = HurdHardware()
    facts = hw.populate()
    memory_facts = facts['memory']
    assert memory_facts['memtotal_mb'] >= 0
    uptime_facts = facts['uptime']
    assert uptime_facts['seconds'] >= 0
    mount_facts = facts['mounts']
    assert mount_facts[0]['mount'] == '/'

# Generated at 2022-06-13 01:02:09.365251
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """Unit test for method populate of class HurdHardware
    """
    # Init
    module = None
    h = HurdHardware(module=module)

    # Run
    h.populate()

# Generated at 2022-06-13 01:02:20.562112
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """
    Test if correct info is populated in the facts_dict
    """
    hurd_facts = HurdHardware()
    facts_dict = hurd_facts.populate()
    mount_facts = hurd_facts.get_mount_facts()

    assert 'uptime_seconds' in facts_dict
    assert isinstance(facts_dict['uptime_seconds'], int)

    assert 'memtotal_mb' in facts_dict
    assert isinstance(facts_dict['memtotal_mb'], int)

    assert 'vendor' in facts_dict
    assert 'product' in facts_dict
    assert 'virtualization_type' in facts_dict
    assert 'serial' in facts_dict

    for fs_mount in mount_facts['mounts']:
        assert 'mount' in fs_mount
        assert 'device' in fs_mount


# Generated at 2022-06-13 01:02:21.408316
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware = HurdHardware()
    hardware.populate()

# Generated at 2022-06-13 01:02:28.018851
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hw = HurdHardware()

    facts = hw.populate()
    assert facts['uptime_days'] == int(facts['uptime_seconds'] / 60 / 60 / 24)
    assert facts['uptime_hours'] == int(facts['uptime_seconds'] / 60 / 60 % 24)
    assert facts['uptime_seconds'] > 0

    assert facts['memfree_mb'] + facts['swapfree_mb'] == facts['memtotal_mb'] + facts['swaptotal_mb']
    assert facts['memtotal_mb'] > 0
    assert facts['swaptotal_mb'] > 0

    assert '/' in facts['mounts']

# Generated at 2022-06-13 01:02:36.422718
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware_facts = HurdHardware().populate()
    assert hardware_facts.get('uptime_days') == 0
    assert hardware_facts.get('uptime_hours') == 0
    assert hardware_facts.get('uptime_seconds') == 0
    assert hardware_facts.get('uptime_minutes') == 0
    assert hardware_facts.get('uptime_summary') == '0 seconds'
    assert hardware_facts.get('memfree_mb') == 0
    assert hardware_facts.get('memtotal_mb') == 0



# Generated at 2022-06-13 01:02:44.208134
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # Mock the translator that reads memory and mount facts
    def translator_mock():
        return {'memtotal': '1000000000', 'memfree': '100', 'swaptotal': '100000', 'swapfree': '100', '/dev/sda1/': {'type': 'ext4', 'mount': '/', 'size': '10000', 'available': '100'}, '/dev/sdb1/': {'type': 'fuse', 'mount': '/home', 'size': '20000', 'available': '200'}, '/dev/sdb1/': {'type': 'fuse', 'mount': '/home', 'size': '20000', 'available': '200'}}

    # Mock the uptime and procfs translator
    def uptime_translator_mock():
        return {'boottime': '123456'}



# Generated at 2022-06-13 01:02:50.208367
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_h = {
        'uptime': {'seconds': 0, 'days': 0},
        'memory': {
            'swap': {'available': 0, 'capacity': 0.0},
            'virtual': {'available': 0, 'capacity': 0.0},
            'real': {'available': 0, 'capacity': 0.0}
        },
        'mounts': [
            {'device': '/dev/root', 'mount': '/', 'fstype': 'tmpfs'},
            {'device': '/dev/hd0s1', 'mount': '/home', 'fstype': 'ext2'}
        ]
    }
    hurd_hw = HurdHardware()
    assert hurd_h == hurd_hw.populate()

# Generated at 2022-06-13 01:03:19.197437
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware = HurdHardware()

    hardware_facts = hardware.populate()

    assert hardware_facts['uptime'] >= 0
    assert hardware_facts['memtotal_mb'] > 0
    assert hardware_facts['swaptotal_mb'] >= 0

# Generated at 2022-06-13 01:03:25.990091
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """
    Test if the method populate of class HurdHardware with a
    mock for LinuxHardware.populate() works as expected.
    """
    from ansible.module_utils.facts.hardware import HurdHardware
    import unittest.mock

    class MockLinuxHardware:
        def populate(self):
            return {'uptime_seconds': 12345, 'memory_mb': {'real': {'total': 1234567890}, 'swap': {'total': 1234567890}}}

    # Patch class LinuxHardware
    with unittest.mock.patch.object(HurdHardware, '_LinuxHardware', new=MockLinuxHardware):
        hhw = HurdHardware()
        ret = hhw.populate()


# Generated at 2022-06-13 01:03:30.906055
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware = HurdHardware()
    hardware_facts = hardware.populate()

    assert hardware_facts["uptime_seconds"] == 3600
    assert hardware_facts["uptime_hours"] == 1
    assert hardware_facts["uptime_days"] == 0
    assert hardware_facts["uptime"] == "1 hour"

    assert hardware_facts["memtotal_mb"] == 512
    assert hardware_facts["memfree_mb"] == 256
    assert hardware_facts["memavailable_mb"] == 0

    assert hardware_facts["swaptotal_mb"] == 1023
    assert hardware_facts["swapfree_mb"] == 512
    assert hardware_facts["swapcached_mb"] == 256

    assert hardware_facts["kernel_modules"] == set(["module1", "module2"])

# Generated at 2022-06-13 01:03:40.617972
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hw = HurdHardware()

    collected_facts = {
        "kernel": "GNU",
        "distribution_major_version": "1.0",
    }
    hw.populate(collected_facts)
    assert hw.uptime
    assert hw.uptime['seconds'] == 140000
    assert hw.uptime['hours'] == 39
    assert hw.uptime['days'] == 1
    assert hw.memtotal_mb
    assert hw.memtotal_mb == 128
    assert hw.memfree_mb
    assert hw.memfree_mb == 11
    assert hw.swaptotal_mb
    assert hw.swaptotal_mb == 0
    assert hw.swapfree_mb
    assert hw.swapfree_mb == 0

    assert h

# Generated at 2022-06-13 01:03:49.554175
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.utils import get_file_content
    import platform

    if platform.system() != 'GNU':
        return

    hardware_collector = HurdHardwareCollector()
    collected_facts = {}
    hardware_collector.populate(collected_facts=collected_facts)

    meminfo_content = get_file_content('/proc/meminfo')
    meminfo_content = to_bytes(meminfo_content, errors='surrogate_or_strict')


# Generated at 2022-06-13 01:03:56.133570
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """
    Unit test of method populate of class HurdHardware
    """
    h = HurdHardware()
    hardware_facts = h.populate()
    keys = hardware_facts.keys()
    print(keys)
    assert hardware_facts['mounts'][0]['mount'] == "/"
    assert hardware_facts['mounts'][0]['device'] == "/dev/hd0s1"
    assert hardware_facts['mounts'][1]['mount'] == "/home/vagrant"
    assert hardware_facts['mounts'][1]['device'] == "/dev/hd0s2"
    assert hardware_facts['fstype'] == "ext2"
    assert hardware_facts['swapfree_mb'] == 512
    assert hardware_facts['memfree_mb'] == 982

# Generated at 2022-06-13 01:03:59.909024
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hardware = HurdHardware()
    hardware_facts = hurd_hardware.populate()
    assert hardware_facts['uptime_seconds'] != 0
    assert hardware_facts['uptime_days'] != 0
    assert hardware_facts['ram'] != 0
    assert hardware_facts['swap'] != 0

# Generated at 2022-06-13 01:04:05.574210
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    collected_facts = None
    test_hurd_hardware = HurdHardware(collected_facts)
    assert isinstance(test_hurd_hardware, HurdHardware)
    populated_hardware_facts = test_hurd_hardware.populate(collected_facts)
    assert isinstance(populated_hardware_facts, dict)
    assert 'mounts' in populated_hardware_facts.keys()

# Generated at 2022-06-13 01:04:13.061132
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware = HurdHardware()
    hardware_facts = hardware.populate()
    assert hardware_facts['uptime_seconds'] == 0
    assert hardware_facts['processor_cores'] == 0
    assert hardware_facts['memory_mb']['real']['total'] == 0
    assert hardware_facts['memory_mb']['real']['free'] == 0
    assert hardware_facts['memory_mb']['swap']['total'] == 0
    assert hardware_facts['memory_mb']['swap']['free'] == 0
    assert hardware_facts['memory_mb']['virtual']['total'] == 0
    assert hardware_facts['memory_mb']['virtual']['free'] == 0
    assert hardware_facts['memory_mb']['hugepages']['total'] == 0

#

# Generated at 2022-06-13 01:04:21.603056
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    class TestHurdHardware(HurdHardware):
        def get_uptime_facts(self):
            return {'uptime_seconds': 1234567}

        def get_memory_facts(self):
            return {'mem_total': 1048576}

        def get_mount_facts(self):
            return {'/dev/sda1': {'device': 'dev/sda1', 'mount': '/'}}

    facts = TestHurdHardware().populate()
    assert facts['uptime_seconds'] == 1234567
    assert facts['mem_total'] == 1048576
    assert facts['/dev/sda1']['device'] == 'dev/sda1'
    assert facts['/dev/sda1']['mount'] == '/'

# Generated at 2022-06-13 01:05:28.695041
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    module = AnsibleModule(argument_spec = dict())
    hardware = module.get_hardware_collector('HurdHardware')

    result = hardware.populate()

    assert result['uptime']
    assert result['uptime_seconds']
    assert result['uptime_days']
    assert result['uptime_hours']
    assert result['uptime_minutes']
    assert result['memtotal_mb']
    assert result['memfree_mb']
    assert result['swaptotal_mb']
    assert result['swapfree_mb']
    assert result['mounts']

# Generated at 2022-06-13 01:05:37.063142
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # Unit test for method populate of class HurdHardware
    hurd_hw = HurdHardware()
    collected_facts = {'ansible_architecture': 'x86_64'}
    hw_facts = hurd_hw.populate(collected_facts=collected_facts)
    assert isinstance(hw_facts, dict)

    # ignore if no test_file exported
    if not hurd_hw.test_file.exists():
        return

    assert 'ansible_uptime_seconds' in hw_facts
    assert isinstance(hw_facts['ansible_uptime_seconds'], int)
    assert hw_facts['ansible_uptime_seconds'] > 0

    assert 'ansible_uptime_string' in hw_facts