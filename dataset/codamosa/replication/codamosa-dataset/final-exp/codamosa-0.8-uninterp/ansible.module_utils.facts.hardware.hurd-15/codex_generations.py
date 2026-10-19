

# Generated at 2022-06-13 00:55:47.816437
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # test on empty file
    h = HurdHardware()
    h.mount_re = '^(?P<device>[^\s]+)\s+(?P<mount_point>[^\s]+)\s+' \
                 '(?:(?P<filesystem>[^\s]+)\s+)?(?P<mount_options>[^\s]+)\s*'

    h.uptime_file = 'test/unit/module_utils/facts/hardware/uptime.empty'
    h.memory_file = '/proc/meminfo'
    h.mount_file = 'test/unit/module_utils/facts/hardware/mount.empty'
    facts = h.populate()
    assert facts == {}, 'Failed to parse empty uptime file'

# Generated at 2022-06-13 00:55:53.706194
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # Create a HurdHardware instance, to be tested
    h = HurdHardware()
    # Unit test the 'populate' method of HurdHardware
    data = h.populate()
    assert data is not None
    assert isinstance(data, dict)
    assert data['uptime_seconds'] > 1
    assert data['memory_mb']['real']['total'] > 1
    assert data['mounts'][0]['mount'] is not None

# Generated at 2022-06-13 00:56:00.913659
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    test_obj = HurdHardware()
    expected_output = {
        'uptime_seconds':148.111812,
        'memtotal_mb':131072,
        'memfree_mb':106216,
        'swaptotal_mb':0,
        'swapfree_mb':0,
        'mounts':[
            {
                'device':'/dev/hd0s1',
                'mount':'/',
                'fstype':'ufs',
                'options':['rw', 'suid', 'dev', 'exec'],
                'size_total':1073741824,
                'size_available':5404323840
            }
        ]
    }
    test_output = test_obj.populate()
    assert expected_output == test_output

# Generated at 2022-06-13 00:56:02.793398
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hh = HurdHardware()
    ret = hh.populate()
    assert ret is not None
    assert 'uptime' in ret
    assert 'swapfree_mb' in ret
    assert 'memfree_mb' in ret

# Generated at 2022-06-13 00:56:05.609407
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # In test_hurd_populate.py
    pass


# Generated at 2022-06-13 00:56:08.359377
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    h = HurdHardware()
    facts = h.populate()
    assert 'uptime_seconds' in facts
    assert 'memtotal_mb' in facts
    assert 'mounts' in facts

# Generated at 2022-06-13 00:56:13.538731
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hw_collector = HurdHardwareCollector()
    hurd_hw_facts = hurd_hw_collector.collect()

    assert hurd_hw_facts is not None
    assert isinstance(hurd_hw_facts, dict)
    assert 'uptime' in hurd_hw_facts
    assert 'uptime_seconds' in hurd_hw_facts
    assert 'memfree_mb' in hurd_hw_facts

# vim: expandtab:tabstop=4:shiftwidth=4

# Generated at 2022-06-13 00:56:17.035854
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    result = HurdHardware().populate()
    assert 'facter' not in result
    assert 'dmi' not in result
    assert 'ansible_uptime_seconds' in result

# Generated at 2022-06-13 00:56:25.711516
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # Test HurdHardware._populate
    hw = HurdHardware()

    populate_ret = hw.populate(collected_facts=dict())
    uptime_facts = hw.get_uptime_facts()
    memory_facts = hw.get_memory_facts()
    # mount_facts = hw.get_mount_facts()
    mount_facts = {}
    try:
        mount_facts = hw.get_mount_facts()
    except TimeoutError:
        pass

    assert type(populate_ret) == dict
    assert type(uptime_facts) == dict
    assert type(memory_facts) == dict
    assert type(mount_facts) == dict

    assert len(populate_ret) == len(uptime_facts) + len(memory_facts) + len(mount_facts)

# Generated at 2022-06-13 00:56:35.803847
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """
    Test that the HurdHardware.populate() works correctly.

    """
    hurd_hardware = HurdHardware()

    def test_populate(self):
        uptime_facts = {
           'uptime_seconds': 1234,
           'uptime_hours': 0,
           'uptime_days': 0
        }
        memory_facts = {
           'memtotal_mb': 1280,
           'memfree_mb': 256,
           'memavail_mb': 256,
           'swaptotal_mb': 0,
           'swapfree_mb': 0
        }

# Generated at 2022-06-13 00:56:40.904246
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    facts = HurdHardware().populate()
    assert facts['uptime_days'] >= 0
    assert facts['uptime_minutes'] >= 0
    assert facts['uptime_seconds'] >= 0
    assert facts['memtotal_mb'] > 0

# Generated at 2022-06-13 00:56:47.378628
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # Test with empty fact
    hardware = HurdHardware()
    hardware_facts = hardware.populate({})
    assert not hardware_facts['uptime_seconds']

    # Test with empty fact and timeout of 1s
    hardware = HurdHardware(timeout=1)
    hardware_facts = hardware.populate({})
    assert not hardware_facts['mounts']
    assert not hardware_facts['system_memory']
    assert not hardware_facts['system_swap']

# Generated at 2022-06-13 00:56:48.921633
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_obj = HurdHardware()
    assert 'uptime_seconds' in hurd_obj.populate()

# Generated at 2022-06-13 00:56:58.145342
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    from ansible.module_utils.facts.timeout import TimeoutError
    from ansible.module_utils.facts.hardware.linux import LinuxHardware
    from ansible.module_utils.facts.hardware.linux import LinuxHardwareCollector

    hurd_hardware = HurdHardware()
    hurd_hardware_collector = HurdHardwareCollector()
    hurd_hardware_linux_hardware_collector = LinuxHardwareCollector()

    hurd_hardware_collector.collect(hurd_hardware, None)
    hurd_hardware_linux_hardware_collector.collect(hurd_hardware, None)

    assert isinstance(hurd_hardware, LinuxHardware)
    assert isinstance(hurd_hardware_collector, HurdHardwareCollector)

# Generated at 2022-06-13 00:57:03.075058
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # set up
    hhw = HurdHardware()
    # exercise
    result = hhw.populate()

    # verify
    assert result['uptime'] == 0
    assert result['uptime_days'] == 0
    assert result['uptime_hours'] == 0
    assert result['uptime_seconds'] == 0
    assert result['memtotal_mb'] == 0
    assert result['swapfree_mb'] == 0
    assert result['swaptotal_mb'] == 0


# Generated at 2022-06-13 00:57:07.680698
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """
    Test the module's methods for GNU Hurd
    """
    def mock_get_uptime_facts(self):
        """
        Mock of LinuxHardware's method get_uptime_facts
        """
        return {'uptime_seconds': 86408}

    def mock_get_memory_facts(self):
        """
        Mock of GNU Hurd's method get_memory_facts
        """
        return {'memfree_mb': 0, 'memtotal_mb': 0}

    def mock_get_mount_facts(self):
        """
        Mock of LinuxHardware's method get_mount_facts
        """
        return {'mounts': []}

    def mock_exec_command(self, module, cmd):
        """
        Mock of LinuxHardware's method exec_command
        """

# Generated at 2022-06-13 00:57:08.235313
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    pass

# Generated at 2022-06-13 00:57:13.213884
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    h = HurdHardware()
    facts = h.populate()
    assert isinstance(facts, dict)
    assert 'uptime' in facts
    assert 'uptime_seconds' in facts
    assert 'memtotal_mb' in facts
    assert 'memfree_mb' in facts
    assert 'swaptotal_mb' in facts
    assert 'swapfree_mb' in facts
    assert 'mounts' in facts
    assert facts['mounts'] == []

# Generated at 2022-06-13 00:57:21.006398
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    import os
    import sys

    # remove the ansible injected 'lib' directory from module search path
    sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))))

    from ansible.module_utils.facts.hardware.hurd import HurdHardware
    import ansible.module_utils.facts.hardware.linux
    import ansible.module_utils.facts.timeout

    import contextlib

    class TestLinux(HurdHardware):

        def _time(self):
            return 0

        def _get_mount_facts(self):
            return {'mounts': []}


# Generated at 2022-06-13 00:57:31.842036
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """
    Unit test for method populate of class HurdHardware
    """
    hurd_hardware = HurdHardware()
    hurd_memory = {
        'MemTotal': '1838120 kB',
        'MemFree': '1650172 kB',
        'SwapTotal': '0 kB',
        'SwapFree': '0 kB',
    }

    hurd_mount = {
        '/': {'device': 'tmpfs', 'options': 'rw,relatime', 'mount_point': '/'}
    }

    result = hurd_hardware.populate()
    assert result['ansible_memfree_mb'] == 15980
    assert result['ansible_swaptotal_mb'] == 0
    assert result['ansible_devices']['/dev/sda']['size'] == 1099511627776

# Generated at 2022-06-13 00:57:38.129096
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    facts = HurdHardware()
    collected = {}

    facts.populate(collected)

    assert 'memory' in collected
    assert 'swap' in collected

# Generated at 2022-06-13 00:57:43.206858
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hh = HurdHardware()

    facts = hh.populate()

    assert facts['uptime_seconds'] >= 0
    assert facts['memtotal_mb'] > 0
    assert isinstance(facts['mounts'], list)
    assert len(facts['mounts']) >= 0
    assert 'mount' in facts['mounts'][0]

# Generated at 2022-06-13 00:57:48.800206
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    def mock_get_mount_facts_throws_timeout(self):
        raise TimeoutError

    hurd_hw = HurdHardware()
    hurd_hw.get_mount_facts = mock_get_mount_facts_throws_timeout
    hurd_hw.get_uptime_facts = lambda: {}
    hurd_hw.get_memory_facts = lambda: {}
    hurd_hw.populate()

# Generated at 2022-06-13 00:57:50.108212
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    h = HurdHardware()
    assert h.populate()

# Generated at 2022-06-13 00:57:55.799238
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware = HurdHardware()
    hardware.populate()
    assert len(hardware.data) == 4
    assert hardware.data['uptime_seconds'] == 3
    assert hardware.data['uptime_days'] == 0
    assert hardware.data['memtotal_mb'] >= 0
    assert len(hardware.data['mounts']) >= 0

# Generated at 2022-06-13 00:57:59.318259
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hw = HurdHardware()

    assert isinstance(hurd_hw.populate(), dict)

# Generated at 2022-06-13 00:58:03.553540
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    fact_module = HurdHardware()
    facts = fact_module.populate()
    assert facts["uptime_seconds"] > 0
    assert facts["uptime_hours"] > 0
    assert facts["uptime_days"] > 0
    assert facts["memfree_mb"] > 0
    assert facts["swapfree_mb"] > 0
    assert facts["mounts"] is not None

# Generated at 2022-06-13 00:58:08.721600
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hs = HurdHardware()
    hs.populate()
    assert 'uptime_seconds' in hs.facts
    assert 'memtotal_mb' in hs.facts
    assert 'memfree_mb' in hs.facts
    assert 'swaptotal_mb' in hs.facts
    assert 'swapfree_mb' in hs.facts

# Generated at 2022-06-13 00:58:12.316591
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware_facts = HurdHardware()
    facts = hardware_facts.populate()

    # Mount facts are not asserted because they are not tested on all platforms.
    assert facts['uptime_seconds'] >= 0
    assert facts['memory_mb']['total'] > 0

# Generated at 2022-06-13 00:58:13.204440
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    pass

# Generated at 2022-06-13 00:58:25.789966
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    import os
    from ansible.module_utils.facts.hardware.linux import LinuxHardware
    from ansible.module_utils.facts.hardware.linux import LinuxHardwareCollector
    from ansible.module_utils.facts.timeout import TimeoutError
    from ansible.module_utils.facts.timeout import TimeoutManager

    default_uptime = None
    default_uptime_file = None
    default_memory_file = '/proc/meminfo'
    default_mount_file = '/proc/mounts'

    hurd_uptime_file = '/proc/uptime'
    hurd_memory_file = '/proc/meminfo'
    hurd_mount_file = '/proc/mounts'

    test_uptime_file = '/tmp/uptime-file'
    test_memory_file = '/tmp/meminfo-file'

# Generated at 2022-06-13 00:58:34.190765
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    test_uptime_facts = {'uptime': 27660.543183326721,
                         'uptime_days': 3.17960125471938,
                         'uptime_hours': 76.190434279999997,
                         'uptime_seconds': 27660.543183326721}
    test_memory_facts = {'memfree_mb': 1019.3056640625,
                         'memtotal_mb': 1030.900390625}

# Generated at 2022-06-13 00:58:35.863427
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    HurdHardware().populate()


# Generated at 2022-06-13 00:58:42.167546
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd = HurdHardware(None)
    facts = hurd.populate()
    assert facts['uptime_days'] == 0
    assert facts['uptime_hours'] == 0
    assert facts['uptime_seconds'] > 0
    assert facts['uptime'] == "0 days, 0:00:00.00"
    assert facts['memtotal_mb'] > 0
    assert facts['swaptotal_mb'] > 0
    assert 'filesystem' in facts['mounts'][0]

# Generated at 2022-06-13 00:58:50.561968
# Unit test for method populate of class HurdHardware

# Generated at 2022-06-13 00:58:53.299582
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # Create a gnu hurd hardware collector
    gnu_hurd_hardware_collector = HurdHardwareCollector()
    # Generate hardware facts
    hardware_facts = gnu_hurd_hardware_collector.populate()
    # Check if the following hardware facts exists
    assert 'uptime_seconds' in hardware_facts
    assert 'memtotal_mb' in hardware_facts
    # Check if the following optional hardware facts exists
    assert 'mounts' in hardware_facts

# Generated at 2022-06-13 00:58:54.140072
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hhw = HurdHardware()
    hhw.populate()

# Generated at 2022-06-13 00:59:04.030506
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    with open("tests/mockdata/proc.mounts") as f:
        proc_mounts_content = f.read()
    with open("tests/mockdata/meminfo") as f:
        meminfo_content = f.read()
    with open("tests/mockdata/uptime") as f:
        uptime_content = f.read()
    with open("tests/mockdata/proc.swaps") as f:
        proc_swaps_content = f.read()
    hw = HurdHardware()

# Generated at 2022-06-13 00:59:12.516725
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():

    hardware_facts = {}
    uptime_facts = {'uptime_seconds': 9230, 'uptime_string': '2 hours, 28 minutes'}

# Generated at 2022-06-13 00:59:19.588236
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """
    Test facts gathering on GNU Hurd
    """
    hurd_hardware = HurdHardware()
    collected_facts = {'ansible_os_family': 'GNU/Hurd'}
    results = hurd_hardware.populate(collected_facts)

    assert results['uptime_system'] > 0
    assert results['uptime_seconds'] > 0
    assert results['uptime_hours'] > 0
    assert results['uptime_days'] > 0
    assert results['memtotal_mb'] > 0
    assert results['memfree_mb'] >= 0
    assert results['swaptotal_mb'] >= 0
    assert results['swapfree_mb'] >= 0
    assert results['mounts']
    assert results['mounts'][0]['device_name'] == 'procfs'

# Generated at 2022-06-13 00:59:28.460925
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hardware = HurdHardware(None)
    hurd_hardware.populate()

# Generated at 2022-06-13 00:59:33.249888
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    import datetime

    hurdhw = HurdHardware()

    # Mock uptime facts
    hurdhw._uptime_strings = [' 17:29:12 up  7:49,  1 user,  load average: 0.00, 0.00, 0.00\n']
    hurdhw._uptime_seconds = int(datetime.timedelta(hours=7, minutes=49, seconds=12).total_seconds())

    # Mock memory facts
    hurdhw._meminfo = {
        'MemTotal': '5071012 kB',
        'MemFree': '1192 kB'
    }

# Generated at 2022-06-13 00:59:43.490572
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    import sys
    import psutil

    # Unset CPU_COUNT
    if 'CPU_COUNT' in sys.modules['ansible'].__dict__['_fact_cache']:
        del sys.modules['ansible'].__dict__['_fact_cache']['CPU_COUNT']

    # Check for CPU_COUNT < 0
    if psutil.cpu_count() < 0:
        return True

    # Check for CPU_COUNT == 0
    if psutil.cpu_count() == 0:
        return True

    # Initialize and populate
    hurd_hardware = HurdHardware()
    hurd_hardware.populate()

    # Check for CPU_COUNT > 0
    if psutil.cpu_count() > 0:
        return True

    return False

# Generated at 2022-06-13 00:59:49.983798
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # Arrange
    from unit.ansible_module import DummyAnsibleModule

    # Avoid 'No module named ansible_module_facts.hardware.HurdHardware' error
    global _HurdHardware
    _HurdHardware = HurdHardware

    hardware = HurdHardware(DummyAnsibleModule(load_fixture('uptime.output')))

    # Act
    result = hardware.populate()

    # Assert
    assert result['uptime_seconds'] == 200
    assert result['uptime_hours'] == 5
    assert result['uptime_days'] == 0
    assert result['uptime_days_long'] == 0



# Generated at 2022-06-13 00:59:54.863410
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    my_HurdHardware = HurdHardware()
    result = my_HurdHardware.populate()

    assert 'uptime' in result
    assert 'uptime_seconds' in result
    assert 'uptime_hours' in result
    assert 'memfree_mb' in result
    assert 'memtotal_mb' in result
    assert 'swapfree_mb' in result
    assert 'swaptotal_mb' in result
    assert 'mounts' in result

# Generated at 2022-06-13 01:00:01.588751
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():

    import time

    from ansible.module_utils.facts.hardware.linux import LinuxHardware

    from ansible.module_utils.facts.hardware.linux import LinuxMemory

    module = Mock(params=dict(), fail_json=dict())
    module.run_command = Mock(return_value=
                                dict(stdout="16:08:53 up 20:07,  1 user,  load average: 0.35, 0.22, 0.11",
                                     rc=0))

    linux_hw = LinuxHardware(module=module)
    uptime_facts = linux_hw.get_uptime_facts()


# Generated at 2022-06-13 01:00:09.729236
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hardware_provider = HurdHardware()
    hurd_hardware_facts = hurd_hardware_provider.populate()
    assert 'uptime_seconds' in hurd_hardware_facts.keys(), "uptime_seconds is missing"
    assert 'uptime_days' in hurd_hardware_facts.keys(), "uptime_days is missing"
    assert 'uptime_hours' in hurd_hardware_facts.keys(), "uptime_hours is missing"
    assert 'uptime_minutes' in hurd_hardware_facts.keys(), "uptime_minutes is missing"
    assert 'mem_total_mb' in hurd_hardware_facts.keys(), "mem_total_mb is missing"

# Generated at 2022-06-13 01:00:14.392487
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    facts = HurdHardware().populate()
    assert 'uptime' in facts
    assert 'uptime_seconds' in facts
    assert 'uptime_hours' in facts
    assert 'uptime_days' in facts
    assert 'memtotal_mb' in facts
    assert 'swaptotal_mb' in facts


# Generated at 2022-06-13 01:00:23.268693
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    class TestClass(object):
        def __init__(self):
            self.data = {}
            self.data['uptime_seconds'] = 5456
            self.data['sys_mem_total'] = 506664
            self.data['sys_mem_free'] = 57332
            self.data['sys_swap_total'] = 61952
            self.data['sys_swap_free'] = 61952
            self.data['proc_mounts'] = {}
            self.data['proc_mounts']['/dev/disk1s1'] = {
                'mount': '/',
                'block_total': 18969600,
                'block_free': 13631712
            }


# Generated at 2022-06-13 01:00:24.779958
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hw = HurdHardwareCollector()
    memory_facts = hurd_hw.get_memory_facts()
    assert type(memory_facts['memory']['memtotal_mb']) == int

# Generated at 2022-06-13 01:00:44.117370
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    pass


# Generated at 2022-06-13 01:00:48.868632
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware = HurdHardware()
    hardware_facts = hardware.populate()
    assert hardware_facts['uptime_minutes'] >= 0
    assert hardware_facts['uptime_seconds'] >= 0
    assert hardware_facts['uptime_hours'] >= 0
    assert hardware_facts['uptime_days'] >= 0
    assert hardware_facts['memtotal_mb'] >= 0
    assert 'mounts' in hardware_facts
    assert hardware_facts['mounts'] >= 0


# Generated at 2022-06-13 01:00:50.685671
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hardware = HurdHardware()

    # Test if the returned dict is not empty
    result = hurd_hardware.populate()
    assert result != {}

# Generated at 2022-06-13 01:00:52.210561
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    facts = HurdHardware().populate()
    assert facts['uptime_min'] is not None

# Generated at 2022-06-13 01:01:01.943446
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    import mock
    import pytest
    from ansible.module_utils.facts.timeout import TimeoutError

    # Arrange
    module_mock = mock.MagicMock()
    module_mock.params = {}
    module_mock.params['gather_timeout'] = 5

    hurd_hardware_mock = mock.MagicMock()
    hurd_hardware_mock.populate.return_value={}
    with mock.patch('ansible.module_utils.facts.hardware.hurd.LinuxHardware', new=mock.MagicMock()):
        # Act
        ret = hurd_hardware_mock.populate()

        # Assert
        hurd_hardware_mock.populate.assert_called()
        assert ret == {}

    # Arrange

# Generated at 2022-06-13 01:01:11.490469
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """
    Unit test for method populate of class HurdHardware.
    """
    hurd_hw = HurdHardware()
    collected_facts = {}
    hurd_facts = hurd_hw.populate(collected_facts)
    assert 'uptime' in hurd_facts
    assert 'system' in hurd_facts
    assert 'hostname' in hurd_facts
    assert 'uptime' in hurd_facts
    assert 'fqdn' in hurd_facts
    assert 'uptime_days' in hurd_facts
    assert 'uptime_seconds' in hurd_facts
    assert 'uptime_hours' in hurd_facts
    assert 'uptime_minutes' in hurd_facts
    assert 'cpu_count' in hurd_facts
    assert 'cpu_chipcount' in hurd_facts
    assert 'cpu_model' in hurd_facts


# Generated at 2022-06-13 01:01:14.807848
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    import sys
    import json

    hurd = HurdHardware()
    try:
        print(json.dumps(hurd.populate(), indent=4))
    except TimeoutError:
        e = sys.exc_info()[1]
        print('%s: %s' % (e.__class__.__name__, e))



# Generated at 2022-06-13 01:01:16.934963
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware = HurdHardware()
    hardware.populate()
    assert hardware.uptime
    assert hardware.memfree_mb
    assert hardware.memtotal_mb
    assert hardware.swaptotal_mb
    assert hardware.swapfree_mb
    assert hardware.mounts

# Generated at 2022-06-13 01:01:18.119276
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware = HurdHardware()
    hardware.populate()

# Generated at 2022-06-13 01:01:26.560287
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    import json
    from ansible.module_utils.facts import timeout

    class TimeoutFixture:
        def __enter__(self):
            self.old_timeout = timeout.FACTS_TIMER
            timeout.FACTS_TIMER = 1

        def __exit__(self, exc_type, exc_value, traceback):
            timeout.FACTS_TIMER = self.old_timeout

    hurdhw = HurdHardware()
    with TimeoutFixture():
        try:
            hurdhw.populate()
        except Exception as e:
            assert isinstance(e, TimeoutError)
        else:
            assert False

# Generated at 2022-06-13 01:02:07.039103
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware = HurdHardware()
    collected_facts = hardware.populate()

    assert isinstance(collected_facts, dict)

    assert 'uptime' in collected_facts
    assert isinstance(collected_facts['uptime'], (int, float))

    assert 'uptime_seconds' in collected_facts
    assert isinstance(collected_facts['uptime_seconds'], (int, float))

    assert 'memtotal_mb' in collected_facts
    assert isinstance(collected_facts['memtotal_mb'], (int, float))

    assert 'mounts' in collected_facts
    assert isinstance(collected_facts['mounts'], list)

# Generated at 2022-06-13 01:02:16.304023
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """
    Unit test for method populate of class HurdHardware
    """
    linux_hw=HurdHardware()
    uptime_facts = linux_hw.get_uptime_facts()
    memory_facts = linux_hw.get_memory_facts()
    try:
        mount_facts = linux_hw.get_mount_facts()
    except TimeoutError:
        pass
    hardware_facts=linux_hw.populate()
    assert set(list(uptime_facts.keys()) + list(memory_facts.keys()) + list(mount_facts.keys())) == set(list(hardware_facts.keys()))

# Generated at 2022-06-13 01:02:20.793111
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hardware = HurdHardware()
    collected_facts = {}

# Generated at 2022-06-13 01:02:21.645269
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware = HurdHardware()
    hardware.populate()

# Generated at 2022-06-13 01:02:23.312754
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hw_collector = HurdHardwareCollector()
    assert hw_collector.populate()


# Generated at 2022-06-13 01:02:29.541193
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware = HurdHardware()

    # Test if hardware.get_uptime_facts() doesn't raise an exception
    _ = hardware.get_uptime_facts()

    # Test if hardware.get_memory_facts() doesn't raise an exception
    _ = hardware.get_memory_facts()

    # Test if hardware.get_mount_facts() doesn't raise an exception
    try:
        _ = hardware.get_mount_facts()
    except TimeoutError:
        pass

    # Test if hardware.populate() doesn't raise an exception
    collected_facts = {}
    _ = hardware.populate(collected_facts=collected_facts)



# Generated at 2022-06-13 01:02:37.689545
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    collected_facts = dict(ansible_local=dict(test='local_value'))
    hardware = HurdHardware(collected_facts)
    hardware.populate()
    facts = hardware.get_facts()

    assert facts['ansible_local']['test'] == 'local_value'
    assert facts['ansible_uptime_seconds'] == 0
    assert facts['ansible_memtotal_mb'] == 0
    assert facts['ansible_mounts'] == []

# Generated at 2022-06-13 01:02:39.603028
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    "Test method populate of class HurdHardware"
    # Create a HurdHardware object
    hw = HurdHardware()



# Generated at 2022-06-13 01:02:46.872258
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    args = {}
    args['module'] = None
    args['persistent_connection'] = None
    args['gather_subset'] = None
    args['filter'] = None
    args['gather_timeout'] = None
    args['check_mode'] = None

    fact_class = HurdHardware(args)
    fact_class.populate()

    assert fact_class.facts['uptime_seconds'] != None
    assert fact_class.facts['uptime_hours'] != None
    assert fact_class.facts['uptime_days'] != None
    assert fact_class.facts['memtotal_mb'] != None
    assert fact_class.facts['swaptotal_mb'] != None
    assert fact_class.facts['mounts'] != None
    assert fact_class.facts['ansible_mounts'] != None

# Generated at 2022-06-13 01:02:53.967022
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hw = HurdHardware()

    f = open('./unit/modules/hardware/fixtures/procfs.part.Hurd.linux_meminfo')
    hw.linux_meminfo_content = f.read()
    f.close()

    f = open('./unit/modules/hardware/fixtures/procfs.part.Hurd.proc_mounts')
    hw.proc_mounts_content = f.read()
    f.close()

    hw.uptime_content = '189862.36 76662.93\n'

    collected_facts = hw.populate()

    assert collected_facts['uptime'] == 189862.36

# Generated at 2022-06-13 01:04:23.472245
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    import ansible.module_utils.facts.system.hurd_facts as system_facts
    hw = HurdHardware(system_facts)
    hardware_facts = hw.populate(collected_facts=None)
    assert isinstance(hardware_facts, dict)
    assert hardware_facts['uptime_seconds'] == int or None
    assert hardware_facts['uptime_hours'] == int or None
    assert hardware_facts['uptime_days'] == int or None
    assert hardware_facts['memfree_mb'] == int or None
    assert hardware_facts['memtotal_mb'] == int or None
    assert hardware_facts['swapfree_mb'] == int or None
    assert hardware_facts['swaptotal_mb'] == int or None

# vim: set et ts=4 sw=4 sts=4

# Generated at 2022-06-13 01:04:26.926886
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    from ansible.module_utils.facts.hardware.hurd import HurdHardware
    hurdhw = HurdHardware()
    hurdhw.populate()
    assert 'hardware' in hurdhw.facts
    assert 'uptime_seconds' in hurdhw.facts['hardware']
    assert 'memtotal_mb' in hurdhw.facts['hardware']

# Generated at 2022-06-13 01:04:27.428111
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    pass

# Generated at 2022-06-13 01:04:32.727040
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    from ansible.module_utils.facts.hardware.linux import LinuxHardware

    LinuxHardware.get_memory_facts = lambda *args, **kwargs: {'memory': 'info'}
    LinuxHardware.get_uptime_facts = lambda *args, **kwargs: {'uptime': 'info'}
    HurdHardware.get_mount_facts = lambda *args, **kwargs: {'mounts': 'info'}

    hardware = HurdHardware()
    hardware.populate()
    assert hardware.memtotal and hardware.memfree and hardware.uptime

# Generated at 2022-06-13 01:04:38.436705
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    from ansible.module_utils.facts import ModuleFactCollector
    from ansible.module_utils.facts.hardware import HurdHardwareCollector
    import subprocess
    # output of the program when calling it with "test" as the argument

# Generated at 2022-06-13 01:04:42.637518
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    h = HurdHardware()
    facts = h.populate()
    mem_facts = h.get_memory_facts()
    uptime_facts = h.get_uptime_facts()
    mount_facts = h.get_mount_facts()
    assert(facts == {'uptime': uptime_facts, 'memory': mem_facts,
                     'mounts': mount_facts})

# Generated at 2022-06-13 01:04:46.924672
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    module = AnsibleModule(argument_spec={})
    fact_collector = HurdHardwareCollector(module)
    hardware_facts = fact_collector.collect(module, [])
    assert hardware_facts['uptime_seconds'] > 0
    assert hardware_facts['uptime_hours'] > 0
    assert hardware_facts['uptime_days'] > 0
    assert hardware_facts['memfree_mb'] > 0
    assert hardware_facts['memtotal_mb'] > 0
    assert hardware_facts['swapfree_mb'] >= 0
    assert hardware_facts['swaptotal_mb'] >= 0
    assert hardware_facts['mounts'] is not None
    assert len(hardware_facts['mounts']) > 0

# Generated at 2022-06-13 01:04:50.984787
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hw = HurdHardware()

    # Checks if all fields are in the fact
    fact = hw.populate()
    assert 'uptime' in fact
    assert 'uptime_seconds' in fact
    assert 'memfree_mb' in fact
    assert 'memtotal_mb' in fact
    assert 'swaptotal_mb' in fact
    assert 'swapfree_mb' in fact

# Generated at 2022-06-13 01:04:52.766986
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    collecter = HurdHardwareCollector('GNU')
    collected_facs = {}
    collecter.populate(collected_facs)

# Generated at 2022-06-13 01:04:53.667309
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    h = HurdHardware()
    assert h.populate() != {}