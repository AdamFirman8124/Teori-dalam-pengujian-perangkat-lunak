

# Generated at 2022-06-13 00:55:45.116233
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hc = HurdHardwareCollector()
    collected_facts = {}
    hw = hc.collect(collected_facts)

    assert hw['uptime']
    assert hw['uptime_seconds']
    assert hw['memfree_mb']
    assert hw['memtotal_mb']
    assert hw['swapfree_mb']
    assert hw['swaptotal_mb']
    assert hw['mounts']

# Generated at 2022-06-13 00:55:49.012997
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hw = HurdHardware()
    hurd_facts = hurd_hw.populate()
    assert type(hurd_facts['uptime_seconds']) == int
    assert type(hurd_facts['memory_mb']) == dict
    assert type(hurd_facts['mounts']) == list
    assert type(hurd_facts['swapfree_mb']) == int

# Generated at 2022-06-13 00:55:57.020414
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    from ansible.module_utils import basic

    hardware = HurdHardware({'gather_subset': 'all'})
    hardware.collect()  # cache
    facts = hardware.get_facts()
    facts_dict = facts.copy().copy_dict()
    assert isinstance(facts_dict, dict)

    assert isinstance(facts_dict.get('uptime', {}).get('seconds', None), int)
    assert isinstance(facts_dict.get('uptime', {}).get('hours', None), int)
    assert isinstance(facts_dict.get('uptime', {}).get('days', None), int)
    assert isinstance(facts_dict.get('memory', {}).get('total', None),
                      (type(0), type(None)))

# Generated at 2022-06-13 00:56:03.988918
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # A map of parameters which will be passed to the module
    params = {
        'ANCHOR': 'test_hardware_Hurd'
    }

    # A map of existing facts
    collected_facts = {
        'kernel': 'GNU'
    }

    # We exclude parameters inherited from LinuxHardware whose scope
    # is not GNU/Hurd and whose initial values are null/empty strings
    excluded_params = [
        'distribution',
        'distribution_version',
        'distribution_release',
        'os_family',
        'selinux',
        'virtualization_type'
    ]

    # The return value of the module.
    # The test module will get this return value
    hardware_obj = HurdHardware(params)

    hardware_facts = hardware_obj.populate(collected_facts)

# Generated at 2022-06-13 00:56:08.810552
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """
    unit test for method populate of class HurdHardware
    :return:
    """
    hardware_facts = HurdHardware().populate()
    # Check keys
    assert sorted(hardware_facts.keys()) == ['uptime_seconds', 'memfree_mb', 'memtotal_mb', 'mounts']

# Generated at 2022-06-13 00:56:16.516966
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # Test setup
    hurd = HurdHardware({'gather_subset': ['all']})
    # Test setup
    hurd.get_uptime_facts = lambda : {'uptime_seconds': 1234, 'uptime_hours': 42}
    hurd.get_memory_facts = lambda : {'memtotal_mb': 1024, 'memfree_mb': 512}
    hurd.get_mount_facts = lambda: {'/': {'size_total': 10, 'fstype': 'Hurd'}}

    # Test
    facts = hurd.populate()
    # Test assertions

# Generated at 2022-06-13 00:56:17.453747
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd = HurdHardware()
    hurd.populate()

# Generated at 2022-06-13 00:56:25.505730
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # The function is executed by module_utils.facts.hardware.linux.LinuxHardware
    # so we have to do an integration test with the stubs of module_utils.facts.hardware
    from ansible.module_utils.facts import timeout
    from ansible.module_utils.facts.hardware.mount import Mount
    from ansible.module_utils.facts.hardware.base import MountError
    # Force the timeout exception to be raised
    timeout.TimeoutError = TimeoutError
    # Use a stub of Mount class and mock the get_mount_facts function to prevent
    # the script to use real output of mount syscall but to test the result
    # of get_mount_facts method.
    Mount.get_mount_facts = Mount.get_mount_facts()

# Generated at 2022-06-13 00:56:28.935458
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hw = HurdHardware()
    assert hw.get('uptime_seconds') > 0
    assert hw.get('uptime_days') > 0
    assert hw.get('memtotal_mb') > 0
    assert len(hw.get('mounts')) > 0

# Generated at 2022-06-13 00:56:36.390785
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    (facts_module_mock, platform_mock, distro_mock,
     hurd_hardware_mock) = prepare_mock_for_HurdHardware(
        '', 0, 1, '', '0', '0', '0')
    result = hurd_hardware_mock.populate()

    assert set(result) == set(['uptime', 'uptime_seconds', 'memoryfree_mb',
                               'memoryfree', 'memorytotal_mb', 'memorytotal',
                               'mounts', 'fstype', 'device'])


# Generated at 2022-06-13 00:56:50.071714
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    from ansible.module_utils.facts.hardware.hurd import HurdHardware
    hurd_hardware = HurdHardware()
    hurd_hardware.get_uptime_facts = lambda: {'uptime': 1}
    hurd_hardware.get_memory_facts = lambda: {'memory': {'total': 2}}
    hurd_hardware.get_mount_facts = lambda: {'mounts': [{'device': '3', 'mount': '4'}]}
    assert 1 == hurd_hardware.populate()['uptime']
    assert 2 == hurd_hardware.populate()['memory']['total']
    assert '3' == hurd_hardware.populate()['mounts'][0]['device']

# Generated at 2022-06-13 00:56:58.144999
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurdhw = HurdHardware()
    collected_facts = {'ansible_os_family': 'GNU/Hurd'}
    uptime_facts = {'last_boot_time': 'Thu Dec  7 16:50:17 CET 2023'}
    memory_facts = {'swapfree_mb': 2056}
    mount_facts = {'mounts': [{'mount': '/', 'device': '/dev/hd0s2', 'fstype': 'hurd'}]}
    res_hw_facts = hurdhw.populate(collected_facts)
    assert res_hw_facts == {**uptime_facts, **memory_facts, **mount_facts}


# Generated at 2022-06-13 00:57:01.903533
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """
    Unit test for method populate of class HurdHardware
    """

    hurd_hw = HurdHardware()
    facts = hurd_hw.populate()

    assert 'uptime' in facts
    assert 'memfree' in facts
    assert 'swapfree' in facts
    assert 'mounts' in facts

# Generated at 2022-06-13 00:57:03.903905
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hh = HurdHardware()
    facts = {'kernel': 'GNU'}
    collected_facts = {'ansible_facts': facts}
    hh.populate(collected_facts)

# Generated at 2022-06-13 00:57:11.859012
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    from ansible.module_utils.facts import FactManager

    hw_facts_list = []
    facts = FactManager(None, hw_facts_list).get_facts()

    kernel = facts['ansible_kernel']
    if kernel == 'GNU':
        assert len(hw_facts_list) == 1
        assert hw_facts_list[0].__class__.__name__ == 'HurdHardware'
    elif kernel == 'Linux':
        assert len(hw_facts_list) == 1
        assert hw_facts_list[0].__class__.__name__ == 'LinuxHardware'
    else:
        assert len(hw_facts_list) == 0

# Generated at 2022-06-13 00:57:12.919590
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    test_obj = HurdHardware()
    assert test_obj.populate()

# Generated at 2022-06-13 00:57:19.610460
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hardware_collector = HurdHardwareCollector()
    collected_facts = {}
    collected_facts['distribution'] = 'GNU'
    hurd_hardware_collector.populate(collected_facts)
    assert collected_facts['uptime_seconds'] > 0
    assert collected_facts['memtotal_mb'] > 0
    assert collected_facts['mem_mb'] > 0
    assert collected_facts['memfree_mb'] > 0
    assert collected_facts['swaptotal_mb'] > 0
    assert collected_facts['swapfree_mb'] > 0
    assert len(collected_facts['mounts']) >= 1

# Generated at 2022-06-13 00:57:24.831515
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # Create an object HurdHardware
    hh = HurdHardware()
    # test method populate of class HurdHardware
    hh.populate()
    # Check if facts are acquired successfully
    assert hh.facts['uptime_seconds'] != None
    assert hh.facts['memtotal_mb'] != None
    assert hh.facts['mounts'] != None


# Generated at 2022-06-13 00:57:30.526669
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hh = HurdHardware()
    hardware_facts = hh.populate()
    assert hardware_facts.get('uptime_seconds')
    assert hardware_facts.get('memory_mb')
    assert hardware_facts.get('mounts')
    assert hardware_facts.get('swapfree_mb')
    assert hardware_facts.get('swaptotal_mb')

# Generated at 2022-06-13 00:57:38.407751
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    import py.test
    import os

    # Create object of class HurdHardware and set test
    # values for its properties
    hardware = HurdHardware()
    hardware.version = 1
    hardware.uptime = {'seconds': 4}
    hardware.meminfo = {'MemTotal': '123456 kB', 'MemFree': '12345 kB'}

# Generated at 2022-06-13 00:57:46.255419
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hh = HurdHardware()
    collected_facts = {'distribution_major_version': '4'}
    output = hh.populate(collected_facts)
    assert {'swapfree_mb': '0.0', 'mounts': [], 'uptime_seconds': 0} == output

# Generated at 2022-06-13 00:57:51.554146
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """Unit test for method HurdHardware._populate"""
    _facts = {}
    _facts['uptime_seconds'] = 42
    _facts['uptime_users'] = {}

    class LinuxHardware(object):
        """Class mocking LinuxHardware base class."""
        @classmethod
        def get_uptime_facts(cls):
            """Method mocking get_uptime_facts method of class LinuxHardware."""
            return _facts

    HurdHardware.__bases__ = (LinuxHardware,)

    hardware_facts = HurdHardware().populate()

    assert 'uptime_seconds' in hardware_facts
    assert hardware_facts['uptime_seconds'] == 42

    assert 'uptime_users' in hardware_facts
    assert hardware_facts['uptime_users'] == {}

# Generated at 2022-06-13 00:58:00.467050
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():

    from ansible.module_utils.facts import timeout
    import os

    # Mock procfs compatibility translator

# Generated at 2022-06-13 00:58:05.092614
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # arrange
    hurd = HurdHardware()

    # act
    res = hurd.populate()

    # assert
    assert 'uptime_seconds' in res
    assert 'swapfree_mb' in res
    assert 'memfree_mb' in res
    assert 'memtotal_mb' in res
    assert 'mounts' in res
    assert 'fstype' in res[0]
    assert 'mount' in res[0]


# Generated at 2022-06-13 00:58:07.722700
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hw_facts = HurdHardware()
    facts = hw_facts.populate()
    assert 'uptime' in facts
    assert 'total_physical_memory' in facts
    assert 'mounts' in facts

# Generated at 2022-06-13 00:58:16.041633
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    from ansible.module_utils.facts import ModuleStub

    module_stub = ModuleStub()
    module_stub.exit_json = lambda **kwargs: None

    memfree = 'MemFree:        205304 kB'
    meminfo = '\n'.join([memfree])

    mount = 'rootfs on / type rootfs (rw,noexec,nosuid,size=19968k,nr_inodes=2496) \
proc on /proc type proc (rw,noexec,nosuid,nodev) \
devtmpfs on /dev type devtmpfs (rw,noexec,nosuid,size=19968k,nr_inodes=2496,mode=755) \
sysfs on /sys type sysfs (rw,noexec,nosuid,nodev)'


# Generated at 2022-06-13 00:58:24.361925
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hw_facts = HurdHardware()
    facts = {}

# Generated at 2022-06-13 00:58:26.735338
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hw = HurdHardware()
    assert hw.populate() == {'uptime_seconds': 1054, 'uptime_days': 1}

# Generated at 2022-06-13 00:58:30.451888
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hardware = HurdHardware()
    
    # HurdHardware.populate() should return a dict of hardware facts
    assert isinstance(hurd_hardware.populate(), dict)


if __name__ == '__main__':
    test_HurdHardware_populate()

# Generated at 2022-06-13 00:58:37.364266
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """
    HurdHardware.populate() as called by ansible.module_utils.facts.hardware.
    load_collector_classes(set())
    """

    collector = HurdHardwareCollector()
    collected_facts = collector.collect(None, None)

    assert 'uptime' in collected_facts
    assert 'uptime_seconds' in collected_facts
    assert 'uptime_hours' in collected_facts
    assert 'uptime_days' in collected_facts
    assert 'memtotal_mb' in collected_facts
    # The following tests are only run on Linux, not GNU/Hurd.
    #assert 'memfree_mb' in collected_facts
    #assert 'swaptotal_mb' in collected_facts
    #assert 'swapfree_mb' in collected_facts
    assert 'mounts' in collected_

# Generated at 2022-06-13 00:58:44.254464
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_facts = HurdHardware()
    facts = hurd_facts.populate()

    assert facts['uptime_days'] == 7

    assert facts['memfree_mb'] == 'unknown'
    assert facts['memtotal_mb'] == 'unknown'

    assert facts['mounts'] != []



# Generated at 2022-06-13 00:58:48.354139
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware = HurdHardware()
    hardware_facts = hardware.populate()

    assert hardware_facts['uptime_seconds'] > 0
    assert hardware_facts['memtotal_mb'] > 0
    assert hardware_facts['memfree_mb'] >= 0
    assert hardware_facts['swaptotal_mb'] > 0
    assert hardware_facts['swapfree_mb'] >= 0

# Generated at 2022-06-13 00:58:55.695277
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    from ansible.module_utils.facts.hardware.linux import Memory
    import os
    import sys
    import yaml

    require_kernel = 'linux'
    if require_kernel != os.uname()[0].lower():
        print("Skipping tests that require kernel='%s'" % (require_kernel,))
        sys.exit(0)

    fact_class = HurdHardware
    fact_collector_class = HurdHardwareCollector
    platform = 'GNU'
    test_data_file = 'hardware/linux/files/test_linux_hardware.yaml'

    # prepare a fake file
    f = open(test_data_file)
    test_data = yaml.safe_load(f)
    f.close()


# Generated at 2022-06-13 00:59:03.065499
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hwh = HurdHardware()

    hwh.get_uptime_facts = lambda: {'uptime_seconds': 60}
    hwh.get_memory_facts = lambda: {'memtotal_mb': 16}
    hwh.get_mount_facts = lambda: {'mounts': [{'mount': '/'}]}

    assert hwh.populate() == {
        'uptime_seconds': 60,
        'memtotal_mb': 16,
        'mounts': [{'mount': '/'}]
    }

# Generated at 2022-06-13 00:59:11.755837
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    from ansible.module_utils.facts.hardware.linux import Hardware
    from ansible.module_utils.facts.hardware.hurd import HurdHardware
    from ansible.module_utils.facts.collector import HardwareCollector
    class MockHardware(Hardware):
        def __init__(self, platform):
            self.platform = platform

        def populate(self, collected_facts=None):
            memory_facts = {'memfree_mb': '100',
                            'memtotal_mb': '200',
                            'swapfree_mb': '300',
                            'swaptotal_mb': '400'}
            return memory_facts

    HardwareCollector.add_platform(MockHardware)
    hardware_collector = HardwareCollector()
    hardware_collector.populate()
    hardware_facts = hardware_

# Generated at 2022-06-13 00:59:21.924112
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hhw = HurdHardware()
    # Note : we cannot guarantee that /proc will be mounted
    # Hopefully for testing purposes it will be mounted
    facts = hhw.populate()
    assert isinstance(facts.get('uptime_seconds'), int)
    assert isinstance(facts.get('uptime_hours'), int)
    assert isinstance(facts.get('uptime_days'), int)
    assert isinstance(facts.get('uptime_minutes'), int)
    assert isinstance(facts.get('memtotal_mb'), int)
    assert isinstance(facts.get('memfree_mb'), int)
    assert isinstance(facts.get('swaptotal_mb'), int)
    assert isinstance(facts.get('swapfree_mb'), int)
    assert isinstance(facts.get('mounts'), list)

# Generated at 2022-06-13 00:59:33.159958
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hardware = HurdHardware()
    collected_facts = {'ansible_os_family': 'GNU/Hurd', 'ansible_architecture': 'x86_64', 'ansible_distribution': 'GNU/Hurd', 'ansible_distribution_version': '0.9', 'ansible_machine': 'x86_64'}

# Generated at 2022-06-13 00:59:36.631521
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hardware_obj = HurdHardware()
    collected_facts = {}
    collected_facts['os'] = {'name': 'GNU'}
    collected_facts['ansible_facts'] = {}
    result = hurd_hardware_obj.populate(collected_facts)
    assert isinstance(result, dict)
    assert result['uptime']['seconds'] == 3600

# Generated at 2022-06-13 00:59:42.457491
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    print()
    hurd_hardware = HurdHardware()
    facts = hurd_hardware.populate()
    assert facts['uptime']
    assert facts['uptime_seconds']
    assert facts['uptime_days']
    assert facts['memtotal_mb']
    assert 'memfree_mb' in facts
    assert 'swaptotal_mb' in facts
    assert 'swapfree_mb' in facts
    assert 'mounts' in facts

# Generated at 2022-06-13 00:59:45.376157
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    h = HurdHardware()
    h.populate()
    # memory_facts
    assert 'MemTotal' in h.fact_dict
    assert 'MemFree' in h.fact_dict
    # uptime_facts
  

# Generated at 2022-06-13 00:59:59.669127
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    import re

    hurd_facts = {
        'uptime_seconds': 100,                                                 # example value
        'uptime_days': 1,                                                      # example value
        'uptime_hours': 4,                                                     # example value
        'uptime_minutes': 0,                                                   # example value
        'kernel': 'GNU',                                                       # example value
        'os_family': 'GNU/Hurd'                                                # example value
    }

    hurd_hw = HurdHardware()
    facts_dict = hurd_hw.populate()

    for key in hurd_facts:
        assert (key in facts_dict)
        if key == 'uptime_seconds':
            assert (re.match(r'\A[0-9]+\Z', str(facts_dict[key])))

# Generated at 2022-06-13 01:00:02.739711
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware_facts = HurdHardware()
    memory_facts = hardware_facts.get_memory_facts()
    assert 'memtotal_mb' in memory_facts
    assert 'memfree_mb' in memory_facts

# Generated at 2022-06-13 01:00:11.188237
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    _hurd_hardware = HurdHardware()
    # Get and check facts for GNU/Hurd system
    _hurd_facts = _hurd_hardware.populate()
    assert isinstance(_hurd_facts, dict)
    assert 'uptime_seconds' in _hurd_facts
    assert 'uptime_hours' in _hurd_facts
    assert 'uptime_days' in _hurd_facts
    assert 'memfree_mb' in _hurd_facts
    assert 'memtotal_mb' in _hurd_facts
    assert 'swapfree_mb' in _hurd_facts
    assert 'swaptotal_mb' in _hurd_facts
    assert 'mounts' in _hurd_facts

# Generated at 2022-06-13 01:00:12.149135
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    inst = HurdHardware()
    inst.populate()

# Generated at 2022-06-13 01:00:13.337059
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    c = HurdHardware()
    c.populate()

# Generated at 2022-06-13 01:00:19.330978
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware_facts = HurdHardware().populate()
    assert not hardware_facts['uptime'] == hardware_facts['uptime_seconds'] == 0
    assert hardware_facts['memfree_mb'] < hardware_facts['memtotal_mb']
    assert hardware_facts['swapfree_mb'] < hardware_facts['swaptotal_mb']
    assert hardware_facts['filesystems'] == hardware_facts['filesystems_info']
    assert hardware_facts['filesystems']

# Generated at 2022-06-13 01:00:21.894778
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware = HurdHardware()
    hardware_facts = hardware.populate()

    assert hardware_facts
    assert hardware_facts['memory_mb']['real']['total'] > 0
    assert hardware_facts['uptime_seconds'] > 0

# Generated at 2022-06-13 01:00:24.064796
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hardware_obj = HurdHardware()
    hurd_hardware_result = hurd_hardware_obj.populate()

    assert type(hurd_hardware_result) == dict
    assert 'memtotal_mb' in hurd_hardware_result

# Generated at 2022-06-13 01:00:27.309009
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """
    Unit test for method popluate of class HurdHardware for GNU/Hurd
    """
    hw = HurdHardware()
    facts = hw.populate()

    assert 'uptime' in facts
    assert 'uptime_seconds' in facts
    assert 'memfree_mb' in facts
    assert 'memtotal_mb' in facts
    assert 'swaptotal_mb' in facts
    assert 'swapfree_mb' in facts

# Generated at 2022-06-13 01:00:36.744667
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """
    Test gather facts for GNU Hurd.

    Verify the validity of results returned by gather facts for GNU Hurd
    instance of class HurdHardware.

    :return:
        Test result as boolean value.
    """
    # Initialize test variable
    hurd_hardware = HurdHardware()
    # Get test Hurd facts
    hurd_facts = hurd_hardware.populate()
    # Verify test result
    assert isinstance(hurd_facts['memfree_mb'], int)
    assert isinstance(hurd_facts['memtotal_mb'], int)
    assert isinstance(hurd_facts['swapfree_mb'], int)
    assert isinstance(hurd_facts['swaptotal_mb'], int)
    assert isinstance(hurd_facts['uptime_seconds'], int)

# Unit

# Generated at 2022-06-13 01:00:58.284190
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hw = HurdHardware()
    mem = hw.get_memory_facts()
    upt = hw.get_uptime_facts()
    mnt = hw.get_mount_facts()
    collected_facts = hw.populate()
    assert collected_facts == dict(mem.items() + upt.items() + mnt.items())

# Generated at 2022-06-13 01:01:07.281021
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    from ansible.module_utils.facts.hardware.hurd import HurdHardware
    from ansible.module_utils.facts.timeout import TimeoutError
    import sys

    # Hack to avoid the error "No module named ..."
    def resource_facts(module_name):
        return {
            'sys': sys,
            'time': time,
            'psutil': psutil,
            'lm-sensors': lm_sensors,
            'platform': platform,
            'errno': errno,
            'stat': stat,
            'resource': resource
        }[module_name]

    sys.modules['ansible.module_utils.facts.system'] = MockModule()
    sys.modules['ansible.module_utils.facts.system'].resource_facts = resource_facts

# Generated at 2022-06-13 01:01:13.397278
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hh = HurdHardware()
    hh.populate()

    assert hh.uptime is not None
    assert hh.uptime > -1

    assert hh.memory['swapfree'] > -1
    assert hh.memory['swaptotal'] > -1
    assert hh.memory['memtotal'] > -1
    assert hh.memory['memfree'] > -1
    assert hh.memory['memavail'] > -1

    assert len(hh.mounts) > -1

# Generated at 2022-06-13 01:01:24.585544
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    mocked_facts = {
        'ansible_system': 'GNU',
    }


# Generated at 2022-06-13 01:01:26.079114
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hw = HurdHardware()
    hw.populate()

# Generated at 2022-06-13 01:01:33.164875
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hw_facts = HurdHardware("/proc/fs/procfs")

# Generated at 2022-06-13 01:01:35.278342
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hardware = HurdHardware()
    facts = hurd_hardware.populate()
    assert 'uptime' in facts
    assert facts['uptime'] != 0


# Generated at 2022-06-13 01:01:41.502546
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hh = HurdHardware()

    uptime_facts = {'uptime': 1, 'uptime_days': 0, 'uptime_hours': 0,
                    'uptime_minutes': 0, 'uptime_seconds': 1,
                    'uptime_days_minutes': '0d:0h:0m'}

    mount_facts = {}

    memory_facts = {'memtotal_mb': 1, 'memfree_mb': 1, 'swaptotal_mb': 0,
                    'swapfree_mb': 0}
    assert hh.populate() == dict(list(uptime_facts.items()) +
                                 list(memory_facts.items()) +
                                 list(mount_facts.items()))

# Generated at 2022-06-13 01:01:47.076976
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hd = HurdHardware()
    ansible_facts = hd.populate()
    assert len(ansible_facts) > 2
    assert ansible_facts['uptime_seconds'] > 0
    assert ansible_facts['uptime_days'] >= 0
    assert ansible_facts['system_vendor']
    assert ansible_facts['virtualization_role'] == 'guest'
    assert ansible_facts['virtualization_type'] == 'kvm'
    assert ansible_facts['memory_mb']['real']['total']
    assert ansible_facts['memory_mb']['swap']['total'] == 0



# Generated at 2022-06-13 01:01:49.685967
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hwh = HurdHardware()
    hwh.populate()

# Generated at 2022-06-13 01:02:26.723273
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """Test HurdHardware.populate()."""
    # pylint: disable=protected-access
    hurd_hardware = HurdHardware()
    collected_facts = {}
    expected_facts = {
        'uptime_seconds': 0,
        'swapfree_mb': 0,
        'memtotal_mb': 0,
        'memfree_mb': 0,
        'mounts': [],
    }
    assert hurd_hardware.populate(collected_facts) == expected_facts

# Generated at 2022-06-13 01:02:28.291279
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """Unit test for method populate of class HurdHardware."""
    hurdHardware = HurdHardware()
    assert len(hurdHardware.populate()) != 0

# Generated at 2022-06-13 01:02:39.728052
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    fake_module = FakeModule()
    fact_class = HurdHardware(fake_module)
    uptime_facts = {'uptime_seconds': 20, 'uptime_hours': 0, 'uptime_days': 1}
    memory_facts = {'memfree_mb': 10, 'memtotal_mb': 100}
    mount_facts = {
        'mounts': [
            {
                'mount': '/',
                'device': '/dev/root',
                'fstype': 'ext4',
                'size_total': 20,
                'size_available': 10,
                'size_used': 10,
                'mount_options': ['ro', 'errors=remount-ro']
            }
        ]
    }

    fact_class._get_uptime_facts = lambda self: uptime_facts
    fact

# Generated at 2022-06-13 01:02:44.004228
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    '''Unit test for method populate of class HurdHardware'''
    fact_class = HurdHardware()
    collected_facts = {}
    hardware_facts = {}
    uptime_facts = {}
    memory_facts = {}
    mount_facts = {}
    hardware_facts.update(uptime_facts)
    hardware_facts.update(memory_facts)
    hardware_facts.update(mount_facts)
    assert fact_class.populate(collected_facts) == hardware_facts

# Generated at 2022-06-13 01:02:46.429969
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    dummy_facts = dict()
    collector = HurdHardwareCollector()
    facts = collector.collect(dummy_facts, {'gather_timeout': 0})

    assert facts

# Generated at 2022-06-13 01:02:54.731088
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hw = HurdHardware()
    result = hw.populate()
    assert len(result) > 0
    assert result['uptime_seconds'] > 0
    assert result['uptime_seconds'] > 0
    assert 'MemTotal' in result
    assert result['MemTotal'] > 0
    assert 'SwapTotal' in result
    assert result['SwapTotal'] >= 0
    assert 'devtmpfs' in result['mounts']
    assert result['mounts']['devtmpfs']['fstype'] == 'devtmpfs'
    assert 'proc' in result['mounts']
    assert result['mounts']['proc']['fstype'] == 'proc'
    assert 'sysfs' in result['mounts']

# Generated at 2022-06-13 01:03:01.230293
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    from ansible.module_utils.facts.hardware.hurd import HurdHardware
    hardware_facts = HurdHardware()
    collected_facts = {
        'PATH': '/tmp/ansible-test/bin:/tmp/ansible-test/python/bin:/tmp/ansible-test/sh/bin:/home/user/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
        'LANG': 'C.UTF-8',
        'PWD': '/tmp/ansible-test',
        'HOME': '/home/user',
    }
    populated_facts = hardware_facts.populate(collected_facts=collected_facts)
    assert populated_facts['uptime_seconds'] > 0
    assert populated_

# Generated at 2022-06-13 01:03:04.020559
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    ihc = HurdHardware()
    facts = ihc.populate()
    assert facts == {'uptime': {'days': 0, 'hours': 0, 'seconds': 0}, 'memory': {}}

# Generated at 2022-06-13 01:03:10.758668
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware = HurdHardware()

    uptime_facts = hardware.get_uptime_facts()
    memory_facts = hardware.get_memory_facts()

    mount_facts = {}
    try:
        mount_facts = hardware.get_mount_facts()
    except TimeoutError:
        pass

    all_facts = uptime_facts.copy()
    all_facts.update(memory_facts)
    all_facts.update(mount_facts)

    assert hardware.populate() == all_facts

# Generated at 2022-06-13 01:03:14.614109
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hardware = HurdHardware()
    collected_facts = {'ansible_kernel': 'GNU'}
    assert 'ansible_uptime_seconds' in hurd_hardware.populate(collected_facts)



# Generated at 2022-06-13 01:04:33.647323
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    from ansible.module_utils.facts import timeout

    # Timeout exception
    hardware = HurdHardware(timeout=0.1)
    hardware._executor = ShellExecutor(
        binary='true',
        timeout=0.1
    )
    hardware._executor._executor = 'shell'
    try:
        hardware.populate()
    except TimeoutError:
        pass
    else:
        raise Exception('test_HurdHardware_populate failed')

# Unit tests for module module_utils.facts.hardware.linux

# Generated at 2022-06-13 01:04:34.717773
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hardware = HurdHardware()
    assert {} == hurd_hardware.populate()

# Generated at 2022-06-13 01:04:37.791270
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hw = HurdHardware()
    facts = hw.populate()
    assert isinstance(facts, dict)
    assert len(facts) > 0
    assert 'uptime_seconds' in facts
    assert 'memtotal_mb' in facts
    assert 'mounts' in facts


if __name__ == '__main__':
    import pytest
    pytest.main('-v')

# Generated at 2022-06-13 01:04:47.177195
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    class MockModule:
        def fail_json(self):
            pass

    facts = {
        "ansible_architecture": "x86_64",
        "ansible_distribution": "GNU",
        "ansible_distribution_version": "0.7",
        "ansible_os_family": "GNU",
        "ansible_system": "x86_64-pc-linux-gnu",
        "ansible_system_vendor": "",
        
    }
    h = HurdHardware(module=MockModule(), facts=facts)
    h.populate()
    print(h.memory)
    print(h.uptime)
    print(h.mounts)
    assert h.memory['MemFree'] == 1845844
    assert h.uptime['seconds'] > 0

# Generated at 2022-06-13 01:04:49.383626
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    facts = HurdHardware().populate()
    assert facts['uptime_seconds'] > 0
    assert facts['uptime_days'] > 0
    assert facts['memory_mb']['real']['total'] > 0
    assert len(facts['mounts']) > 0

# Generated at 2022-06-13 01:04:52.685653
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware_facts = {}
    hardware = HurdHardware()
    hardware.collect()
    uptime_facts = hardware.get_uptime_facts()
    memory_facts = hardware.get_memory_facts()
    mount_facts = hardware.get_mount_facts()

    hardware_facts.update(uptime_facts)
    hardware_facts.update(memory_facts)
    hardware_facts.update(mount_facts)


# Generated at 2022-06-13 01:04:55.027132
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware = HurdHardware()
    hardware_facts = hardware.populate()

    assert hardware_facts is not None
    assert 'uptime_seconds' in hardware_facts
    assert 'uptime_hours' in hardware_facts
    assert 'uptime_days' in hardware_facts
    assert 'memfree_mb' in hardware_facts

# Generated at 2022-06-13 01:04:57.923078
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # Test a default HurdHardware instance
    hurd_hardware = HurdHardware()
    hurd_hardware.populate()

    # Test HurdHardware when no data can be found
    hurd_hardware = HurdHardware()
    hurd_hardware.get_mount_facts = lambda: {}
    hurd_hardware.get_memory_facts = lambda: {}
    hurd_hardware.get_uptime_facts = lambda: {}
    hurd_hardware.populate()

# Generated at 2022-06-13 01:05:04.073836
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurdhw = HurdHardware()
    assert not hurdhw.get('ansible_mounts')
    assert hurdhw.get('ansible_processor_vcpus') == 1
    hurdhw.populate()
    assert isinstance(hurdhw.get('ansible_mounts'),dict)
    assert hurdhw.get('ansible_processor_vcpus') == 1
    assert hurdhw.get('ansible_system') == 'GNU'
    assert hurdhw.get('ansible_machine_id') == ''
    assert hurdhw.get('ansible_pkg_mgr') == 'dpkg'

# Generated at 2022-06-13 01:05:05.441061
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hw = HurdHardware()
    result = hw.populate()
    assert len(result) > 0