

# Generated at 2022-06-13 00:55:49.037787
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # Test when /proc/self/mountinfo is present and readable
    hurd_hw = HurdHardware({}, {})
    hurd_hw.get_uptime_facts = lambda: {'uptime': 'somevalue'}
    hurd_hw.get_memory_facts = lambda: {'memory': 'somevalue'}
    hurd_hw.get_mount_facts = lambda: {'mounts': 'somevalue'}

    hardware_facts = hurd_hw.populate()
    assert hardware_facts['uptime'] == 'somevalue'
    assert hardware_facts['memory'] == 'somevalue'
    assert hardware_facts['mounts'] == 'somevalue'

    # Test when /proc/self/mountinfo is not present or readable
    hurd_hw = HurdHardware({}, {})
    hurd_hw.get_uptime_facts

# Generated at 2022-06-13 00:55:57.022336
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    mocked_facts = {}
    mocked_facts['ansible_all_ipv4_addresses'] = [
        '192.168.0.1',
        '172.16.30.43',
        '169.254.169.254'
    ]

# Generated at 2022-06-13 00:55:57.748515
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware = HurdHardware()
    hardware.populate()

# Generated at 2022-06-13 00:55:59.509993
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    unix_hardware = HurdHardware()
    # Test 'uptime' fact collecting
    assert "uptime" in unix_hardware.populate()

# Generated at 2022-06-13 00:56:02.197637
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware_collector = HurdHardwareCollector(None)
    hardware_instance = hardware_collector.collect()
    hardware_facts = hardware_instance.populate()
    assert hardware_facts['dmi']['system']['manufacturer'] == 'GNU'



# Generated at 2022-06-13 00:56:04.931250
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    h = HurdHardware()
    facts = h.populate()
    assert 'memory' in facts
    assert 'swap' in facts['memory']
    assert 'total' in facts['memory']['swap']
    assert facts['uptime']['hours'] > 0

    assert 'mounts' in facts
    assert len(facts['mounts']) > 0

# Generated at 2022-06-13 00:56:09.382384
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """
    Invoke populate and return the results. This method is called
    during unit tests and the output recorded so it can be used
    to verify the correctness of the implementation.
    :return: dictionary containing the facts
    """
    hw = HurdHardware()
    collected_facts = {}
    return hw.populate(collected_facts)

# Generated at 2022-06-13 00:56:15.199824
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    fact = HurdHardware()
    facts = fact.populate()

    assert isinstance(facts, dict)
    assert isinstance(facts['mounts'], list)
    assert isinstance(facts['memfree_mb'], int)
    assert isinstance(facts['memtotal_mb'], int)
    assert isinstance(facts['uptime_seconds'], int)
    assert isinstance(facts['uptime_seconds'], int)
    assert isinstance(facts['swapfree_mb'], int)
    assert isinstance(facts['swaptotal_mb'], int)

# Generated at 2022-06-13 00:56:21.933978
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware = HurdHardware()
    hardware_facts = hardware.populate()
    assert hardware_facts['uptime_seconds'] == int
    assert hardware_facts['uptime_hours'] == int
    assert hardware_facts['uptime_days'] == int
    assert hardware_facts['memtotal_mb'] == int
    assert hardware_facts['memfree_mb'] == int
    assert hardware_facts['swaptotal_mb'] == int
    assert hardware_facts['swapfree_mb'] == int
    assert hardware_facts['mounts'] == list

# Generated at 2022-06-13 00:56:22.801704
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    HurdHardware().populate()

# Generated at 2022-06-13 00:56:33.677535
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hw = HurdHardware()

    collected_facts = {
        'distribution': 'GNU/Hurd',
        'distribution_version': '0.8',
    }

    facts = hurd_hw.populate(collected_facts)

    assert facts['uptime_seconds'] > 0

    assert facts['memtotal_mb'] > 0
    assert facts['memfree_mb'] >= 0
    assert facts['swaptotal_mb'] >= 0
    assert facts['swapfree_mb'] >= 0

    mount_points = ['/']
    for mount in facts['mounts']:
        if mount['mount'] in mount_points:
            mount_points.remove(mount['mount'])

    assert len(mount_points) == 0

# Generated at 2022-06-13 00:56:35.508135
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    uh = HurdHardware()
    collected_facts = {}
    facts = uh.populate(collected_facts)
    assert facts['mounts']

# Generated at 2022-06-13 00:56:37.396821
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hardware = HurdHardware()
    collected_facts = {}
    result = hurd_hardware.populate(collected_facts)
    assert result



# Generated at 2022-06-13 00:56:42.279744
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware_facts = HurdHardware()
    facts = hardware_facts.populate()
    assert facts['uptime'] == 10000
    assert facts['memory']['memtotal'] == 10240
    assert facts['memory']['swapfree'] == 2048
    assert facts['mounts'][0]['path'] == "/"

# Generated at 2022-06-13 00:56:47.988507
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd = HurdHardware()
    facts = hurd.populate()
    assert 'uptime_seconds' in facts
    assert 'uptime_days' in facts
    assert 'uptime_hours' in facts
    assert 'uptime_minutes' in facts

    assert 'memory_mb' in facts
    assert 'memory_available_mb' in facts
    assert 'memory_swap_total_mb' in facts
    assert 'memory_swap_available_mb' in facts

# Generated at 2022-06-13 00:56:54.907918
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts import constants
    import os

    from collections import namedtuple
    from unittest import TestCase
    from mock import Mock, patch

    class Args(object):
        def __init__(self, path, collector):
            self.path = path
            self.collect_timeout = 30
            self.filter = collector

    module = namedtuple('AnsibleModule', ['params'])
    args = Args(os.path.dirname(__file__), 'HurdHardwareCollector')

    HurdHardwareCollector.FACTS = {}
    HurdHardwareCollector.COLLECTOR_PATH = os.path.dirname(__file__)

    mock_module = module(params=args)


# Generated at 2022-06-13 00:56:58.422809
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # Construct a test HurdHardware
    hurdhw = HurdHardware()
    # We should not have a system
    assert not hurdhw.system
    # Construct a mock facts object
    collected_facts = {
        'ansible_system': 'GNU',
    }
    # Populate the HurdHardware object
    hurdhw.populate(collected_facts)
    # We should now have a system
    assert hurdhw.system == 'GNU'

# Generated at 2022-06-13 00:57:05.241296
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """ Test if HurdHardware.populate() returns the expected information. """
    fake_uptime = ' 17:40:15 up  3:54,  1 user,  load average: 0.00, 0.00, 0.00'

    def exec_os_command(cmd):
        """ Fake the execution of an operating system command, so that
            it returns the information we want to test.
        """
        if cmd == 'uptime':
            return (fake_uptime, '')
        elif cmd == 'cat /proc/meminfo':
            memtotal = 'MemTotal:     1048576 kB'
            return (memtotal, '')
        elif cmd == 'df -T -P -l':
            return ('ext4 /home 5M 5M 0% /home', '')

    HardwareCollector.exec_os_command

# Generated at 2022-06-13 00:57:11.041793
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hw = HurdHardwareCollector()

    hardware_facts = hw.collect()
    print(hardware_facts)

    assert hardware_facts['uptime_seconds']
    assert hardware_facts['uptime_days']
    assert hardware_facts['memtotal_mb']
    assert hardware_facts['memfree_mb']
    assert hardware_facts['swaptotal_mb']
    assert hardware_facts['swapfree_mb']
    assert hardware_facts['partitions']

# Generated at 2022-06-13 00:57:20.495823
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware = HurdHardware()
    hardware_facts = hardware.populate()

    assert hardware_facts['uptime_seconds'] == 15
    assert hardware_facts['uptime_hours'] == '0'
    assert hardware_facts['uptime_days'] == '0'

    assert hardware_facts['memtotal_mb'] == 128
    assert hardware_facts['memfree_mb'] == 64
    assert hardware_facts['memavail_mb'] == 64
    assert hardware_facts['swaptotal_mb'] == 64
    assert hardware_facts['swapfree_mb'] == 64
    assert hardware_facts['swapcached_mb'] == 0
    assert hardware_facts['cached_mb'] == 32
    assert hardware_facts['buffers_mb'] == 0
    assert hardware_facts['active_mb'] == 32
    assert hardware_

# Generated at 2022-06-13 00:57:25.206588
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hardware = HurdHardware()

    # We don't know the contents of the collected_facts variable
    # so we don't test it here
    hurd_hardware.populate(None)
    assert True

# Generated at 2022-06-13 00:57:26.998906
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hw = HurdHardware()
    hw.collect()
    assert hw.data['uptime_seconds'] >= 0

# Generated at 2022-06-13 00:57:30.994480
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # Create an instance of class HurdHardware
    hurdhw_populate = HurdHardware()
    # Check that the class of the retured value is a dict
    assert(type(hurdhw_populate.populate()) is dict)

# Generated at 2022-06-13 00:57:35.968572
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    class mock_linux:
        def populate(self):
            return {'uptime': 1, 'memory': 1, 'mount': 1}

    hardware = HurdHardware()
    hardware.linux = mock_linux()

    result = hardware.populate()

    assert 'uptime' in result
    assert result['uptime'] == 1
    assert 'memory' in result
    assert result['memory'] == 1
    assert 'mount' in result
    assert result['mount'] == 1


# Generated at 2022-06-13 00:57:37.009650
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hw = HurdHardware()
    assert hw.populate()

# Generated at 2022-06-13 00:57:42.282240
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """ Test of method populate of class HurdHardware """
    hurd_hw = HurdHardware()

    # Test the uptime facts
    uptime_facts = hurd_hw.get_uptime_facts()
    assert 'uptime' in uptime_facts
    assert 'uptime_seconds' in uptime_facts
    assert 'boot_time' in uptime_facts

    # Test the memory facts
    memory_facts = hurd_hw.get_memory_facts()
    assert 'memfree_mb' in memory_facts
    assert 'swapfree_mb' in memory_facts

    # Test the mount facts
    mount_facts = hurd_hw.get_mount_facts()
    assert 'mounts' in mount_facts

    # Test the class method populate
    hardware_facts = hurd_hw.populate()
    assert 'uptime'

# Generated at 2022-06-13 00:57:53.792480
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hh = HurdHardware()

# Generated at 2022-06-13 00:57:57.971216
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    class MockClass(object):
        MODULE_COMPLEX_ARGS = {'gather_timeout': 5}

    module_mock = MockClass()
    hurd_hardware = HurdHardware(module_mock)
    try:
        facts = hurd_hardware.populate()
    except:
        return False
    return bool(facts)


# Generated at 2022-06-13 00:58:01.941326
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hhw = HurdHardware()
    facts = hhw.populate()
    assert "uptime" in facts
    assert "uptime_seconds" in facts
    assert "uptime_hours" in facts
    assert "uptime_days" in facts
    assert "memory" in facts
    assert "swap" in facts

# Generated at 2022-06-13 00:58:03.095001
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # TODO: Unit test for method populate of class HurdHardware
    pass

# Generated at 2022-06-13 00:58:05.156716
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    pass

# Generated at 2022-06-13 00:58:14.079451
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    from ansible.module_utils.facts.hardware.linux import _get_mount_facts
    import sys

    hurd_hw = HurdHardwareCollector()
    hurd_hw._get_mount_facts = _get_mount_facts
    hurd_hw.cache = {
        'ansible_mounts': {}
    }

    collected_facts = {
        'ansible_distribution': 'GNU/Hurd',
        'ansible_distribution_version': '0.8',
        'ansible_product_name': 'GNU/Hurd',
        'ansible_product_serial': None,
        'ansible_product_uuid': None,
        'ansible_command_timeout': 60
    }


# Generated at 2022-06-13 00:58:21.077040
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hw = HurdHardware()
    hw.populate()
    assert hw.size_total is not None
    assert hw.size_available is not None
    assert 'size_total_kb' in hw.size_total
    assert 'size_available_kb' in hw.size_available
    assert 'size_used_kb' in hw.size_total
    assert 'size_available_percent' in hw.size_available
    assert 'size_used_percent' in hw.size_total
    assert 'uptime_seconds' in hw.uptime

# Generated at 2022-06-13 00:58:22.185386
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurdhw = HurdHardware()
    hurdhw.populate()


# Generated at 2022-06-13 00:58:29.151722
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    h = HurdHardware()
    facts = h.populate()
    assert facts["uptime_hours"]
    assert facts["uptime_seconds"]
    assert facts["system_memtotal_mb"]
    assert facts["memfree_mb"]
    assert facts["memavailable_mb"]
    assert facts["swapfree_mb"]
    assert facts["swaptotal_mb"]
    assert facts["/"]


if __name__ == '__main__':
    test_HurdHardware_populate()

# Generated at 2022-06-13 00:58:33.016161
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    h = HurdHardware()

    # Return a mocked fact collection
    def my_function():
        return {"ansible_processor": ["i386", "xscale", "x86_64"]}
    h.populate = my_function
    facts = h.populate()

    assert facts['ansible_processor'] == ["i386", "xscale", "x86_64"]

# Generated at 2022-06-13 00:58:37.305764
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    from ansible.module_utils.facts.hardware.linux import LinuxHardware

    facts = dict()
    hardware = HurdHardware(facts)

    class FakeModule:
        ''' Fake AnsibleModule. '''

        def __init__(self):
            self.params = {}

    module = FakeModule()
    hardware.populate(module)

    assert 'uptime' in facts
    assert 'uptime_seconds' in facts
    assert 'memory_mb' in facts
    assert 'mounts' in facts

# Generated at 2022-06-13 00:58:40.244218
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    ''' Test the function HurdHardware.populate() '''

    dummy_self = DummySelf()
    HurdHardware.populate(dummy_self)



# Generated at 2022-06-13 00:58:41.597493
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    res = HurdHardware().populate()
    print(res)

# Generated at 2022-06-13 00:58:44.954267
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # Basic setup
    hh_dict = {'fqdn': ()}
    facts = HurdHardware()
    facts.populate()

    # Test function of Hardware.populate
    hh_dict = facts.populate(hh_dict)


# Generated at 2022-06-13 00:58:55.374121
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    class MockModule(object):
        def __init__(self):
            self.params = {'gather_mount_facts': True}

    class MockLibrary(object):
        def __init__(self):
            self.module = MockModule()

    hurd_hardware = HurdHardware(MockLibrary())
    facts = hurd_hardware.populate()

# Generated at 2022-06-13 00:59:00.805653
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # Create new instance
    facts = HurdHardware()

    # Ensure the are no facts currently stored
    assert facts.populated is False
    assert facts.facts == {}

    # Populate the facts
    facts.populate()

    # Ensure no facts returned as GNU Hurd platform is not supported
    assert facts.populated is False
    assert facts.facts == {}

# Generated at 2022-06-13 00:59:09.576337
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    mock_facts = {
        'distribution_system': 'GNU',
    }
    hurdhw = HurdHardware(mock_facts)
    test_facts = hurdhw.populate()
    assert test_facts is not None
    assert test_facts['uptime_seconds'] > 0
    assert test_facts['memtotal_mb'] > 0
    assert test_facts['swaptotal_mb'] > 0
    assert 'mounts' in test_facts
    assert len(test_facts['mounts']) > 0
    assert 'sys' in test_facts['mounts'][0]['mount']
    assert 'proc' in test_facts['mounts'][1]['mount']
    assert 'dev' in test_facts['mounts'][2]['mount']

# Generated at 2022-06-13 00:59:10.990129
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hardware_obj = HurdHardware()
    hurd_hardware_obj.collect()
    assert isinstance(hurd_hardware_obj.get_facts(), dict)

# Generated at 2022-06-13 00:59:21.233580
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware = HurdHardware()
    hardware.populate()
    assert hardware.uptime is not None, "Uptime not found"
    assert hardware.uptime.get('seconds', None) is not None, "Uptime seconds not found"
    assert hardware.uptime.get('hours', None) is not None, "Uptime hours not found"
    assert hardware.memory is not None, "Memory not found"
    assert hardware.memory.get('memtotal_mb', None) is not None, "Memory total not found"
    assert hardware.memory.get('memfree_mb', None) is not None, "Memory free not found"
    assert hardware.memory.get('swaptotal_mb', None) is not None, "Swap total not found"
    assert hardware.memory.get('swapfree_mb', None) is not None

# Generated at 2022-06-13 00:59:32.402856
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    class MockModule:
        def fail_json(self, *args):
            raise Exception('fail_json called')

    class MockCollector:
        class MockLsbRelease:
            def __init__(self):
                self.lsb_distributor_id = 'Debian'
                self.lsb_release = '9.2'

        def __init__(self):
            self.lsb_release = self.MockLsbRelease()

    class TestHurdHardware(HurdHardware):
        def __init__(self, module):
            self.module = module

        def get_uptime_facts(self):
            return {'uptime': 10}


# Generated at 2022-06-13 00:59:38.932339
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    import sys
    import subprocess

    facts = HurdHardware().populate()

    assert 'uptime_seconds' in facts
    assert isinstance(facts['uptime_seconds'], float)

    assert 'uptime_hours' in facts
    assert isinstance(facts['uptime_hours'], float)

    assert 'uptime_days' in facts
    assert isinstance(facts['uptime_days'], float)

    assert 'memtotal_mb' in facts
    assert isinstance(facts['memtotal_mb'], int)
    assert facts['memtotal_mb'] > 0

    assert 'memfree_mb' in facts
    assert isinstance(facts['memfree_mb'], int)

    assert 'swaptotal_mb' in facts
    assert isinstance(facts['swaptotal_mb'], int)


# Generated at 2022-06-13 00:59:41.538307
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hardware = HurdHardware()
    collected_facts = None
    results = hurd_hardware.populate(collected_facts)

    assert results is not None


# Generated at 2022-06-13 00:59:43.650846
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_facts = HurdHardware()
    actual = hurd_facts.populate()
    assert(isinstance(actual, dict) and len(actual) >= 1)

# Generated at 2022-06-13 00:59:51.651262
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """
    Check that the populate method is working as expected.
    """

    # Arrange
    hh = HurdHardware()
    hh.get_mount_facts = lambda: {'mounts': 'xyz'}
    hh.get_uptime_facts = lambda: {'uptime_seconds': 'abc'}
    hh.get_memory_facts = lambda: {'memfree_mb': '123'}

    # Action
    hardware_facts = hh.populate()

    # Assert
    assert hardware_facts['mounts'] == 'xyz'
    assert hardware_facts['uptime_seconds'] == 'abc'
    assert hardware_facts['memfree_mb'] == '123'



# Generated at 2022-06-13 01:00:03.772576
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    h = HurdHardware()

    facts = h.populate()

    keys = [
        'mounts',
        'memtotal_mb',
        'swaptotal_mb',
        'uptime_seconds',
        'uptime_hours',
        'uptime_days'
    ]

    for key in keys:
        assert key in facts

# Generated at 2022-06-13 01:00:04.897171
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hardware = HurdHardware()
    network_facts = hurd_hardware.populate()
    assert network_facts['uptime_seconds']

# Generated at 2022-06-13 01:00:07.359986
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    from ansible.module_utils.facts import hardware
    hardware_dict = hardware.HardwareCollector().get_facts()
    assert hardware_dict['uptime_format'] == '%d days, %d hours, %d minutes, %d seconds'
    assert hardware_dict['mounts'][0]['mount'] == '/'

# Generated at 2022-06-13 01:00:08.883153
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hardware = HurdHardware()
    factors = hurd_hardware.populate()
    assert 'kernel' in factors
    assert 'system' in factors

# Generated at 2022-06-13 01:00:11.837898
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    from ansible.module_utils import basic

    hardware = HurdHardware(basic.AnsibleModule)
    hardware_facts = hardware.populate()

    assert hardware_facts.get('uptime_seconds')
    assert hardware_facts.get('uptime_days')
    assert hardware_facts.get('memory_mb')
    assert hardware_facts.get('mounts')

# Generated at 2022-06-13 01:00:21.502910
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    from ansible.module_utils.facts.collector import ModuleDepError
    from ansible_collections.ansible.misc.tests.unit.compat.mock import Mock, PropertyMock
    from ansible_collections.ansible.misc.tests.unit.modules.utils import set_module_args

    module = Mock()
    set_module_args({})

    collector = HurdHardwareCollector(module=module)
    collector.populate()
    facts = module.exit_json.call_args[0][1]
    assert 'memory' in facts, 'memory fact not in output'
    assert 'swap' in facts, 'swap fact not in output'
    assert 'uptime' in facts, 'uptime fact not in output'
    assert 'mounts' in facts, 'mounts fact not in output'
   

# Generated at 2022-06-13 01:00:24.826811
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    import mock
    mock_module_util = mock.MagicMock()
    collector = HurdHardwareCollector()

    # One important part of a HardwareCollector is the platform
    assert collector.platform == 'GNU'

    assert not collector.populate(mock_module_util)

    # One important part of a HardwareCollector is the fact_class
    assert collector.fact_class == HurdHardware

# vim: set et ts=4 sw=4 :

# Generated at 2022-06-13 01:00:29.878083
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """Test the method populate of class HurdHardware."""
    hurd_handler = HurdHardware()
    assert isinstance(hurd_handler, HardwareCollector)
    assert isinstance(hurd_handler, HurdHardware)
    assert isinstance(hurd_handler, LinuxHardware)
    assert hurd_handler.platform == 'GNU'


# Generated at 2022-06-13 01:00:40.156999
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    from ansible.module_utils.facts.timeout import TimeoutError
    import pytest
    from ansible.module_utils.facts.hardware.linux import LinuxHardware
    from ansible.module_utils.facts.hardware.linux import LinuxHardwareCollector

    platform = 'GNU'

    # Let's patch AnsibleModule to get 'run_command' attribute
    class FakeAnsibleModule:
        def __init__(self):
            self.run_command = lambda x: None
        def fail_json(self, msg):
            print(msg)

    # Let's patch LinuxHardware
    def raise_timeout_error(self):
        raise TimeoutError

    class FakeLinuxHardware(LinuxHardware):
        get_mount_facts = raise_timeout_error

    hurd_hardware = FakeHurdHardware(FakeAnsibleModule())

# Generated at 2022-06-13 01:00:45.303532
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hardware_collector = HurdHardwareCollector()
    hurd_hardware_collector.populate()
    assert hurd_hardware_collector.facts['uptime_seconds'] == 0
    assert hurd_hardware_collector.facts['uptime_hours'] == 0
    assert hurd_hardware_collector.facts['uptime_days'] == 0
    assert hurd_hardware_collector.facts['swapfree_mb'] == 0

# Generated at 2022-06-13 01:01:05.794877
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    pass



# Generated at 2022-06-13 01:01:09.175546
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    h = HurdHardware()
    hardware_facts = h.populate()

    assert hardware_facts['uptime_seconds'] > 0
    assert hardware_facts['memory_mb']['real']['total'] > 0
    assert len(hardware_facts['mounts']) > 0

# Generated at 2022-06-13 01:01:16.523622
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hw = HurdHardware()

    # test get_uptime_facts()
    uptime_facts = hurd_hw.get_uptime_facts()
    assert ('uptime' in uptime_facts)

    # test get_memory_facts()
    memory_facts = hurd_hw.get_memory_facts()
    assert ('memtotal_mb' in memory_facts)
    assert ('memfree_mb' in memory_facts)
    assert ('memavailable_mb' in memory_facts)

    # test get_mount_facts()
    mount_facts = hurd_hw.get_mount_facts()
    assert ('mounts' in mount_facts)

    # test populate()
    hardware_facts = hurd_hw.populate()
    assert ('uptime' in hardware_facts)

# Generated at 2022-06-13 01:01:26.991903
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware = HurdHardware()
    collected_facts = {}
    collected_facts['ansible_virtualization_role'] = 'guest'
    collected_facts['ansible_machine_id'] = 'unit_test_machine_id'
    memory_facts = {}
    memory_facts['ansible_swapfree_mb'] = 0
    memory_facts['ansible_memfree_mb'] = 0
    memory_facts['ansible_memtotal_mb'] = 0
    memory_facts['ansible_swaptotal_mb'] = 0
    memory_facts['ansible_memavail_mb'] = 0
    uptime_facts = {}
    uptime_facts['ansible_uptime_seconds'] = 0
    uptime_facts['ansible_uptime_hours'] = 0
    mount_facts = {}
    mount_

# Generated at 2022-06-13 01:01:30.831034
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """
    Unit test for method populate of class HurdHardware.
    """
    hh = HurdHardware()
    facts = hh.populate()

    assert 'uptime' in facts
    assert 'uptime_seconds' in facts
    assert 'memtotal_mb' in facts
    assert 'memfree_mb' in facts
    assert 'mounts' in facts


# Generated at 2022-06-13 01:01:32.350027
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hardware = HurdHardware()
    assert(hurd_hardware.populate())



# Generated at 2022-06-13 01:01:39.094107
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # Init the class
    hurd_hardware = HurdHardware()

    # Create a collected facts
    collected_facts = dict()
    # Populate the collected facts
    hurd_hardware.populate(collected_facts)
    # The following system facts are expected:
    # - uptime_seconds
    # - memory_mb
    # - swapfree_mb
    # - swapfree_mb
    # - mounts
    assert collected_facts['uptime_seconds'] == 0
    assert collected_facts['memory_mb'] == 0
    assert collected_facts['swapfree_mb'] == None
    assert collected_facts['swapfree_mb'] == None
    assert collected_facts['mounts'] != None

# Generated at 2022-06-13 01:01:44.093635
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurdhw = HurdHardware()
    uptime_facts = hurdhw.get_uptime_facts()
    memory_facts = hurdhw.get_memory_facts()

    mount_facts = {}
    try:
        mount_facts = hurdhw.get_mount_facts()
    except TimeoutError:
        pass

    hurdhw.populate()

    assert uptime_facts == hurdhw.populate()
    assert memory_facts == hurdhw.populate()
    assert mount_facts == hurdhw.populate()

# Generated at 2022-06-13 01:01:47.651266
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_collector = HurdHardwareCollector()
    hurd_facts = hurd_collector.collect()

    assert hurd_facts['uptime'] == 42
    assert hurd_facts['uptime_days'] == 1
    assert hurd_facts['uptime_hours'] == 1
    assert hurd_facts['uptime_seconds'] == 42
    assert hurd_facts['swapfree_mb'] > 0

# Generated at 2022-06-13 01:01:57.166012
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # Testing the GNU Hurd subclass of the Linux subclass of Hardware Collector
    hurd = LinuxHardware()
    facts = hurd.populate()
    assert 'uptime_seconds' in facts
    assert 'uptime_days' in facts
    assert 'uptime_hours' in facts
    assert 'uptime_seconds' in facts
    assert 'uptime' in facts
    assert 'memtotal_mb' in facts
    assert 'pmemtotal_mb' in facts
    assert 'memfree_mb' in facts
    assert 'memavail_mb' in facts
    assert 'swaptotal_mb' in facts
    assert 'swapfree_mb' in facts
    assert 'swapcached_mb' in facts
    assert 'swap' in facts
    assert 'active' in facts['swap']

# Generated at 2022-06-13 01:02:32.887996
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_facts = HurdHardware()
    hurd_facts.populate()

# Generated at 2022-06-13 01:02:36.291614
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware = HurdHardware()

    facts = hardware.populate()

    expected_keys = sorted(['uptime', 'mounts', 'memory_mb', 'memory_mb_real'])

    assert sorted(facts.keys()) == expected_keys

# Generated at 2022-06-13 01:02:40.505660
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hw_facts = HurdHardware().populate()
    assert hw_facts.get('uptime') > 0
    assert hw_facts.get('uptime_days') >= 0
    assert hw_facts.get('memtotal_mb') > 0
    assert hw_facts.get('memfree_mb') >= 0


# Generated at 2022-06-13 01:02:47.100853
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware = HurdHardware()

    hardware_facts = hardware.populate()

    assert hardware_facts
    assert hardware_facts['uptime_seconds']
    assert hardware_facts['uptime_seconds'] > 0
    assert hardware_facts['uptime_pretty']
    assert hardware_facts['uptime_pretty'] == '0 days, 00:00'
    assert hardware_facts['memory_mb']
    assert hardware_facts['memory_mb'] > 0
    assert hardware_facts['swap_mb']
    assert hardware_facts['swap_mb'] > 0


# Generated at 2022-06-13 01:02:55.058656
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    h = HurdHardware()
    collected_facts = {}
    collected_facts = h.populate(collected_facts)
    # Assert that the collected information is of type dict.
    assert isinstance(collected_facts, dict)
    # Assert that some required information has been collected.
    assert collected_facts['uptime'] != ''
    assert collected_facts['uptime_seconds'] != ''
    assert collected_facts['memtotal_mb'] != ''
    assert collected_facts['memfree_mb'] != ''
    assert collected_facts['swaptotal_mb'] != ''
    assert collected_facts['swapfree_mb'] != ''
    assert collected_facts['suid_dumpable'] == '0'
    assert collected_facts['mounts'] != ''

# Generated at 2022-06-13 01:02:58.407521
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hardware = HurdHardware()
    facts = hurd_hardware.populate()

    assert facts.get('mounts')
    assert facts.get('uptime')
    assert facts.get('memtotal_mb')
    assert facts.get('swaps')
    assert facts.get('memcached_mb')
    assert facts.get('memavailable_mb')

# Generated at 2022-06-13 01:03:00.963772
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware = HurdHardware()

    # Run method populate of class HurdHardware
    hardware.populate()

    # Check if memory_mb has the right type
    assert isinstance(hardware.memory_mb, dict)

# Generated at 2022-06-13 01:03:06.574050
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurdHardware = HurdHardware()
    hurdHardware.populate()
    assert isinstance(hurdHardware.uptime_seconds(), int)
    assert isinstance(hurdHardware.memtotal_mb, float)
    assert isinstance(hurdHardware.memfree_mb, float)
    assert isinstance(hurdHardware.swapfree_mb, float)
    assert isinstance(hurdHardware.mounts, dict)

# Generated at 2022-06-13 01:03:07.337346
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    pass

# Generated at 2022-06-13 01:03:16.721125
# Unit test for method populate of class HurdHardware

# Generated at 2022-06-13 01:04:51.625058
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    import sys
    sys.path.append("../")
    from module_utils.facts.hardware.linux import LinuxHardware

    # Create an instance of class HurdHardware
    hrud1 = HurdHardware()
    hrud1.populate()
    
    # Create an instance of class LinuxHardware
    linux1 = LinuxHardware()
    linux1.populate()
    
    # Check if the class of hrud1 is HurdHardware or not
    if isinstance(hrud1, HurdHardware):
        print("True")
    else:
        print("False")

    # Check if the class of linux1 is LinuxHardware or not
    if isinstance(linux1, LinuxHardware):
        print("True")
    else:
        print("False")


# Generated at 2022-06-13 01:04:52.266506
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    fact = HurdHardware()
    fact.populate()

# Generated at 2022-06-13 01:04:57.461803
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware_data = {'uptime_seconds': 1234567,
                     'uptime_timestamp': '2020-01-23T11:50:27Z',
                     'uptime_booted_timestamp': '2020-01-20T11:50:27Z',
                     'memtotal_mb': 1234,
                     'swaptotal_mb': 567,
                     'mounts': [{'mount': '/', 'device': '/dev/hda1'}]}
    hardware_obj = HurdHardware()
    hardware_obj.populate(hardware_data)
    assert hardware_obj.uptime_seconds == 1234567
    assert hardware_obj.uptime_timestamp == '2020-01-23T11:50:27Z'

# Generated at 2022-06-13 01:05:00.268638
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    os_facts = HurdHardware().populate()
    assert os_facts['uptime']['days']
    assert os_facts['memory']['swapfree_mb']
    assert os_facts['mounts'][0]['size_total']

# Generated at 2022-06-13 01:05:06.828219
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hw = HurdHardware()

    hw_facts = hw.populate()

    assert(isinstance(hw_facts, dict))
    assert(isinstance(hw_facts['uptime'], int))
    assert(isinstance(hw_facts['uptime_seconds'], int))
    assert(isinstance(hw_facts['memtotal_mb'], int))
    assert(isinstance(hw_facts['memfree_mb'], int))
    assert(isinstance(hw_facts['swaptotal_mb'], int))
    assert(isinstance(hw_facts['swapfree_mb'], int))

    assert(isinstance(hw_facts['mounts'], list))

# Generated at 2022-06-13 01:05:11.334647
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    fact = HurdHardwareCollector()
    result = fact.get_facts()
    assert set(result.keys()) == set(['memfree_mb', 'uptime_seconds', 'uptime_hours',
                               'memtotal_mb', 'mounts', 'uptime_days',
                               'uptime_minutes'])

# Generated at 2022-06-13 01:05:13.129469
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware = HurdHardware()
    hardware.populate()

    assert hardware.facts['memfree_mb'] == 576
    assert hardware.facts['memtotal_mb'] == 576

# Generated at 2022-06-13 01:05:15.303450
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hw = HurdHardware()
    # module_utils.facts.hardware.base.TimeoutError is not defined in Hurd system,
    # so this call will raise NameError.
    assert not hurd_hw.populate()



# Generated at 2022-06-13 01:05:22.601726
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    from ..module_utils.facts.timeout import TimeoutError
    from ..module_utils.facts.hardware.linux import LinuxHardware

    # Sadly, we need to mock the functions in LinuxHardware, even though
    # they are disabled in LinuxHardware (condition set to false).
    LinuxHardware.enable_procfs_uptime = True
    LinuxHardware.enable_procfs_filesystems = True
    LinuxHardware.enable_sysfs_filesystems = True

    def mock_get_uptime_facts():
        return {
            'uptime_seconds': 5,
            'uptime_days': 0,
            'uptime_hours': 0,
            'uptime_minutes': 0
        }

    def mock_get_memory_facts():
        return {
            'memtotal_mb': 10
        }


# Generated at 2022-06-13 01:05:29.125103
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    from ansible.module_utils.facts import TimeoutException
    from ansible.module_utils.facts.hardware.linux import Hardware
    from ansible.module_utils.facts.mount import MountFactCollector
    from ansible.module_utils.facts.system.linux import LinuxSysctlFactCollector
    import pytest

    class TestLinuxHardware(LinuxHardware):
        def __init__(self):
            self.sysctl = LinuxSysctlFactCollector
            self.mount = MountFactCollector

    # pylint: disable=unused-argument,protected-access
    def raise_timeout_exception(*args, **kwargs):
        raise TimeoutException()

    def return_dictionary(*args, **kwargs):
        return { 'test1': 'test2' }
