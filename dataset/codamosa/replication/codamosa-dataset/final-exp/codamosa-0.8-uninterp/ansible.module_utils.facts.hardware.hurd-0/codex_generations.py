

# Generated at 2022-06-13 00:55:42.336873
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hw = HurdHardware()
    facts = hw.populate()
    assert 'ansible_memfree_mb' in facts
    assert 'ansible_memory_mb' in facts
    assert 'ansible_swapfree_mb' in facts
    assert 'ansible_swaptotal_mb' in facts
    assert 'ansible_mounts' in facts

# Generated at 2022-06-13 00:55:47.890600
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hhw = HurdHardware()
    hhw.get_uptime_facts = lambda: { 'uptime_seconds': 1 }
    hhw.get_memory_facts = lambda: { 'memtotal_mb': 1 }
    hhw.get_mount_facts = lambda: { 'mounts': [{ 'mount': '/' }] }

    assert hhw.populate() == {
        'uptime_seconds': 1,
        'memtotal_mb': 1,
        'mounts': [{ 'mount': '/' }]
    }

# Generated at 2022-06-13 00:55:52.110595
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    fact_class = HurdHardware()
    assert fact_class.populate() == {
        'memfree_mb': 0,
        'memtotal_mb': 0,
        'uptime_seconds': 0,
        'uptime_days': 0
    }

# Generated at 2022-06-13 00:55:57.884779
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    from ansible.module_utils.facts.hardware.hurd import HurdHardware
    from ansible.module_utils.facts.timeout import TimeoutError

    # Create a HurdHardware object with mock data for method get_memory_facts
    # and a mocked method get_mount_facts raising a TimeoutError
    hurd = HurdHardware(module=None)
    hurd.get_memory_facts = lambda: {'memory': {'total': 1, 'free': 2}}

# Generated at 2022-06-13 00:56:01.912431
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # Create a new object
    hardware_facts = HurdHardware()
    hw_facts = hardware_facts.populate()
    assert hw_facts.get('uptime_seconds') is not None
    assert hw_facts.get('memtotal_mb') is not None
    assert hw_facts.get('virtualization_type') is not None
    assert hw_facts.get('mounts') is not None

# Generated at 2022-06-13 00:56:12.410534
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    import os
    import time

    class MockProcfs:
        def __init__(self):
            self.p_uptime_content = '1598.77'
            self.uptime_content = '1598.77 1563.86'

# Generated at 2022-06-13 00:56:17.038267
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware = HurdHardware()
    hardware_facts = hardware.populate()
    assert hardware_facts['uptime_seconds'] > 0
    assert hardware_facts['uptime_seconds'] < 9223372036
    assert hardware_facts['uptime_days'] >= 0
    assert hardware_facts['uptime_hours'] >= 0
    assert hardware_facts['memory_mb'] > 0
    assert hardware_facts['swapfree_mb'] > 0
    assert hardware_facts['disktotal_gb'] > 0
    assert hardware_facts['diskfree_gb'] > 0

# Generated at 2022-06-13 00:56:25.711843
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    from ansible.module_utils.facts.hardware.linux import LinuxHardware

    mock_module = 'ansible.module_utils.facts.hardware.hurd'
    mock_collector = '%s.HurdHardwareCollector' % mock_module
    mock_LinuxHardware = '%s.LinuxHardware' % mock_module
    mock_uptime_facts = '%s.uptime_facts' % mock_LinuxHardware
    mock_memory_facts = '%s.memory_facts' % mock_LinuxHardware
    mock_mount_facts = '%s.mount_facts' % mock_LinuxHardware


# Generated at 2022-06-13 00:56:28.867767
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware = HurdHardware()
    hardware.populate()
    assert hardware.facts['ansible_system'] == 'GNU/Hurd'
    assert hardware.facts['ansible_processor'][0]['architecture'] == 'x86_64'

# Generated at 2022-06-13 00:56:38.954504
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # build a temporary instance
    hardware = HurdHardware()

    # set the sysfs_path
    hardware.sysfs_path = '/tmp'

    # set the memory and mount fs to non empty values
    hardware.memory_fs = ['tmp1', 'tmp2']
    hardware.mount_fs = ['tmp1', 'tmp2']

    # set uptime information
    hardware.uptime_data = {'boottime': 'boottime'}

    hardware.memory_map = {
        'MemTotal': 'MemTotal',
        'MemFree': 'MemFree',
        'SwapTotal': 'SwapTotal',
        'SwapFree': 'SwapFree'
    }


# Generated at 2022-06-13 00:56:42.652192
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    p = HurdHardware()
    assert p.populate() != {}

# Generated at 2022-06-13 00:56:49.996102
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hw = HurdHardware()
    facts = hurd_hw.populate()
    assert facts['uptime_seconds'] >= 0
    assert facts['uptime_days'] >= 0
    assert facts['uptime_hours'] >= 0
    assert facts['uptime_minutes'] >= 0
    assert facts['memory']
    assert facts['memory']['total'] >= 0
    assert facts['memory']['free'] >= 0
    assert facts['memory']['swap']
    assert facts['memory']['swap']['total'] >= 0
    assert facts['memory']['swap']['free'] >= 0
    assert facts['mounts']

# Generated at 2022-06-13 00:56:59.141254
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hw = HurdHardware()
    hardware_facts = hurd_hw.populate()

    assert hardware_facts['uptime_seconds'] > 0
    assert hardware_facts['uptime_hours'] >= 0
    assert hardware_facts['uptime_days'] >= 0
    assert hardware_facts['uptime_seconds'] > hardware_facts['uptime_minutes']
    assert hardware_facts['uptime_minutes'] > hardware_facts['uptime_hours']
    assert hardware_facts['uptime_hours'] > hardware_facts['uptime_days']

    assert hardware_facts['memtotal_mb'] > 0
    assert hardware_facts['memtotal_gb'] >= 0
    assert hardware_facts['memfree_mb'] >= 0
    assert hardware_facts['memfree_gb'] >= 0

# Generated at 2022-06-13 00:57:04.415957
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hw = HurdHardware()
    facts = hw.populate()
    # test that all expected keys are returned
    assert 'uptime_seconds' in facts
    assert 'uptime_days' in facts
    assert 'uptime' in facts
    assert 'memfree_mb' in facts
    assert 'swapfree_mb' in facts
    assert 'mounts' in facts


# Generated at 2022-06-13 00:57:09.305566
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hh = HurdHardware()
    result = hh.populate({})
    assert result['uptime_seconds'] == 243408
    assert result['uptime_hours'] == 67
    assert result['uptime_days'] == 2
    assert 'memtotal_mb' in result and result['memtotal_mb'] == 7723
    assert len(result['mounts']) == 4

# Generated at 2022-06-13 00:57:15.013508
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    import mock
    mock_module = mock.Mock()
    mock_module.params = dict()
    hardware_facts = HurdHardware(mock_module).populate()
    assert hardware_facts['uptime_seconds'] > 0
    assert hardware_facts['memfree_mb'] > 0
    assert hardware_facts['memtotal_mb'] > 0
    assert hardware_facts['mounts'][0]['mount'] == '/'

# Generated at 2022-06-13 00:57:24.832549
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    fact = HurdHardware()
    fact.get_mount_facts = lambda: {'mounts': [{'device': '/dev/sda1',
                                                'mount': '/',
                                                'fstype': 'ext4'},
                                               {'device': 'tmpfs',
                                                'mount': '/dev/shm',
                                                'fstype': 'tmpfs'}]
                                   }

# Generated at 2022-06-13 00:57:32.919620
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware = HurdHardware()
    hardware_facts = hardware.populate()

    assert hardware_facts is not None
    assert 'uptime' in hardware_facts
    assert hardware_facts['uptime'] > 0
    assert hardware_facts['uptime_seconds'] > 0
    assert 'memtotal_mb' in hardware_facts
    assert hardware_facts['memtotal_mb'] > 0
    assert 'swaptotal_mb' in hardware_facts
    assert hardware_facts['swaptotal_mb'] >= 0
    assert 'mounts' in hardware_facts
    assert len(hardware_facts['mounts']) > 0



# Generated at 2022-06-13 00:57:39.990268
# Unit test for method populate of class HurdHardware

# Generated at 2022-06-13 00:57:47.397674
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """
    Test populate()
    """
    facts_d = dict(ansible_facts=dict(ansible_uptime_seconds=2,
                                     ansible_uptime_string=" 1 day, 10:32:14",
                                     ansible_mounts=None))

    facts = HurdHardware(facts_d)
    result = facts.populate()

    assert result["uptime_seconds"] == 2
    assert result["uptime_string"] == " 1 day, 10:32:14"
    assert result["mounts"] == ""

# Generated at 2022-06-13 00:57:57.784390
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hh = HurdHardware()
    hw_facts = hh.populate()
    assert 'uptime' in hw_facts
    assert 'uptime_seconds' in hw_facts
    assert 'memtotal_mb' in hw_facts
    assert 'memfree_mb' in hw_facts
    assert 'swaptotal_mb' in hw_facts
    assert 'swapfree_mb' in hw_facts
    assert 'mounts' in hw_facts
    assert isinstance(hw_facts['mounts'], list)

# Generated at 2022-06-13 00:58:03.514065
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    collector = HurdHardwareCollector()
    fact_class = collector.collect()[0]

    assert hasattr(fact_class, 'uptime'), "uptime fact missing"
    assert hasattr(fact_class, 'memfree_mb'), "memfree_mb fact missing"
    assert hasattr(fact_class, 'swapfree_mb'), "swapfree_mb fact missing"

    assert hasattr(fact_class, 'mounts'), "mounts fact missing"

# Generated at 2022-06-13 00:58:06.610892
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    collector = HurdHardwareCollector()
    result = collector.collect()
    assert result['uptime_hours']

# Unit test function get_mount_facts of class HurdHardware

# Generated at 2022-06-13 00:58:08.103124
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hardware_instance = HurdHardware()
    hurd_hardware_instance.populate()

# Generated at 2022-06-13 00:58:16.302044
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    import sys
    import os
    import tempfile
    import pytest

    hardware_test_cases_dir = '/usr/share/ansible/testdata/facts/hardware/ansible_facts.d/HurdHardware'
    hardware_test_cases = os.listdir(hardware_test_cases_dir)
    hardware_test_cases.sort()

    parsers_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(parsers_dir)
    from parsers import get_parser

    from ansible.module_utils.facts.hardware.linux import LinuxHardware
    from ansible.module_utils.facts.timeout import TimeoutError


# Generated at 2022-06-13 00:58:18.636692
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hw_cls = HurdHardware()
    hw_cls.populate()
    pass

# Generated at 2022-06-13 00:58:24.597674
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hw = HurdHardware()
    collected_facts = {'ansible_facts': {'kernel': 'GNU/Hurd'}}
    hurd_hw.populate(collected_facts)
    assert collected_facts == {'ansible_facts':
        {'kernel': 'GNU/Hurd', 'hardware':
            {'uptime': {'seconds': 0, 'days': 0}},
         'memory': {'swap': {'total': 0,
                             'free': 0,
                             'used': 0},
                    'real': {'total': 0, 'free': 0, 'used': 0}},
         'mounts': []}}

# Generated at 2022-06-13 00:58:28.539323
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    '''
    Unit test for method populate of class HurdHardware.
    '''
    hurd_hardware = HurdHardware()
    assert 'uptime_seconds' in hurd_hardware.populate()
    assert 'memtotal_mb' in hurd_hardware.populate()

# Generated at 2022-06-13 00:58:31.619920
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    h = HurdHardware()
    facts = h.populate()
    assert 'memory' in facts
    assert 'swap' in facts
    assert 'mounts' in facts
    assert 'fstype' in facts['mounts'][0]


# Generated at 2022-06-13 00:58:36.873426
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_facts = HurdHardware()
    hurd_facts.populate()
    assert hurd_facts.uptime['seconds'] is not None
    assert hurd_facts.uptime['hours'] is not None
    assert hurd_facts.uptime['minutes'] is not None
    assert hurd_facts.uptime['days'] is not None

    assert hurd_facts.memory['swapfree_mb'] is not None
    assert hurd_facts.memory['swapfree'] is not None
    assert hurd_facts.memory['swaptotal_mb'] is not None
    assert hurd_facts.memory['swaptotal'] is not None

# Generated at 2022-06-13 00:58:45.967480
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    h = HurdHardware()
    facts = h.populate()
    assert "memfree_mb" in facts
    assert "swapfree_mb" in facts
    assert "mounts" in facts

# Generated at 2022-06-13 00:58:46.811361
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hardware = HurdHardware()
    assert isinstance(hurd_hardware.populate(), dict)

# Generated at 2022-06-13 00:58:51.557741
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    collected_facts = {}

    # Mock the method get_uptime_facts to return arbitrary uptime facts
    import time
    from datetime import datetime
    from datetime import timedelta
    from ansible.module_utils.facts.hardware.linux import LinuxHardware
    from ansible.module_utils.facts.timeout import TimeoutError
    LinuxHardware.get_uptime_facts = staticmethod(lambda: {
        'uptime': timedelta(days=time.time()/60/60/24),
        'uptime_seconds': time.time()
    })

    # Mock the method get_memory_facts to return arbitrary memory facts
    LinuxHardware._get_total_memory = staticmethod(lambda: (1337, 1024))

    # Mock the method get_memory_facts to return arbitrary memory facts
    LinuxHardware._get_mount_facts

# Generated at 2022-06-13 00:58:53.029187
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # FIXME: test this properly
    pass

# Generated at 2022-06-13 00:58:58.389850
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    wrk_dir = "/tmp/ansible_test/"
    class_name = "HurdHardware"
    tst_man_fact_dir = wrk_dir + class_name + "_manual_facts/"
    tst_exp_fact_dir = wrk_dir + class_name + "_expected_facts/"

    # Populate facts
    HurdHardware().populate()

    # Compare created facts with expected ones
    import filecmp
    assert filecmp.cmpfiles(
        tst_man_fact_dir, tst_exp_fact_dir,
        ["ansible_mounts", "ansible_uptime_seconds", "ansible_memtotal_mb"],
        shallow=False
    )

# Generated at 2022-06-13 00:59:02.182284
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    test_HurdHardware = HurdHardware()
    test_collector = HurdHardwareCollector()
    test_HurdHardware.populate()
    test_fact_class = HurdHardware
    assert test_HurdHardware._fact_class == test_fact_class
    assert test_HurdHardware._platform == test_collector._platform

# Generated at 2022-06-13 00:59:06.772961
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hardware_collector = HurdHardwareCollector()
    hurd_hardware_collector._get_memory_facts = lambda: {}
    hurd_hardware_collector._get_mount_facts = lambda: {}
    hurd_hardware_collector._get_uptime_facts = lambda: {}
    assert type(hurd_hardware_collector.populate()) == dict

# Generated at 2022-06-13 00:59:13.655545
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware = HurdHardware()
    hardware.facts['ansible_processor_count'] = 10
    hardware.facts['ansible_system'] = 'Hurd'

    hardware.populate()

    # mount_facts should not be populated (simulate timeout)
    assert not hardware.facts['ansible_mounts']
    assert hardware.facts['ansible_uptime_seconds'] == 0
    assert hardware.facts['ansible_memfree_mb'] is not None
    assert hardware.facts['ansible_memtotal_mb'] is not None
    assert hardware.facts['ansible_swaptotal_mb'] is not None
    assert hardware.facts['ansible_swapfree_mb'] is not None

# Generated at 2022-06-13 00:59:18.667264
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware_instance = HurdHardware()
    hardware_instance.populate()
    assert hardware_instance._memtotal is not None
    assert hardware_instance._vendor is None
    assert hardware_instance._product is None
    assert hardware_instance._serial is None
    assert hardware_instance._fstype is not None

# Generated at 2022-06-13 00:59:29.378881
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware = HurdHardware()


# Generated at 2022-06-13 00:59:53.132895
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurdhw = HurdHardware()
    hurdhw.hostname = 'myhostname'
    hurdhw.product_name = 'myproductname'
    hurdhw.product_version = 'myproductversion'
    hurdhw.product_serial = 'myproductserial'
    hurdhw.product_uuid = 'myproductuuid'
    hurdhw.subsystem = 'my_subsystem'
    hurdhw.uptime = 'myuptime'
    hurdhw.memory = 'mymemory'
    hurdhw.swap = 'myswap'
    hurdhw.mounts = 'mymounts'

    # mock the get_uptime_facts method
    hurdhw.get_uptime_facts = MagicMock()
    hurdhw.populate()
    assert hurdhw.get_uptime_facts.called == True

    # mock

# Generated at 2022-06-13 00:59:58.333044
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    collector = HurdHardwareCollector()
    facts = collector.collect(None, None)
    assert facts['uptime'] == 63
    assert facts['uptime_days'] == 0
    assert facts['uptime_hours'] == 0
    assert facts['uptime_minutes'] == 0
    assert facts['uptime_seconds'] == 63
    assert facts['memtotal_mb'] == 1024
    assert facts['swaptotal_mb'] == 0
    # mount facts are unreliable
    # assert facts['filesystems']['/'] == 'ext4'

# Generated at 2022-06-13 00:59:59.920466
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware = HurdHardware()
    hardware.populate()

    assert hardware.memory['MemTotal'] == 12582912
    assert hardware.uptime['seconds'] == 3869991

# Generated at 2022-06-13 01:00:03.658376
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware = HurdHardware()
    hardware._get_mount_facts = lambda: {'mounts': []}
    hardware._get_uptime_facts = lambda: {'uptime_seconds': 0}
    hardware._get_memory_facts = lambda: {'ansible_memtotal_mb': 0}
    populated_facts = hardware.populate()

    assert 'ansible_uptime_seconds' in populated_facts
    assert 'ansible_memtotal_mb' in populated_facts
    assert 'ansible_mounts' in populated_facts

# Generated at 2022-06-13 01:00:06.662843
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hw = HurdHardware()
    collected_facts = {
        'ansible_architecture': 'x86_64'
    }
    hurd_hw.populate(collected_facts)

# Generated at 2022-06-13 01:00:10.042461
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware_collector = HurdHardwareCollector()
    hardware_facts = hardware_collector.populate()

    assert hardware_facts['uptime_seconds']
    assert hardware_facts['memtotal_mb']
    assert hardware_facts['memfree_mb']
    assert hardware_facts['swaptotal_mb']
    assert hardware_facts['swapfree_mb']

# Generated at 2022-06-13 01:00:20.240218
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    class HurdHardware(HurdHardware):
        def __getattr__(self, attr):
            '''Getter for the uptime facts.'''
            if attr == 'uptime_facts':
                return {
                    '_ansible_uptime_seconds': 3699,
                    '_ansible_uptime_days': 0,
                }

            '''Getter for the memory facts.'''
            if attr == 'memory_facts':
                return {
                    '_ansible_memtotal_mb': 907,
                    '_ansible_swaptotal_mb': 1,
                }

            '''Getter for the mount facts.'''

# Generated at 2022-06-13 01:00:24.618173
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """Unit test for method populate of class HurdHardware"""
    hurd_hardware = HurdHardware()

    # Test exception handling in case of a TimeoutError
    def mock_get_mount_facts(self):
        """Mock method get_mount_facts of class HurdHardware"""
        raise TimeoutError('Test: TimeoutError')
    hurd_hardware.get_mount_facts = mock_get_mount_facts.__get__(hurd_hardware, HurdHardware)

    assert hurd_hardware.populate() == {}

# Generated at 2022-06-13 01:00:29.205307
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_fact = HurdHardware()
    result = hurd_fact.populate()
    assert 'uptime' in result
    assert 'uptime_seconds' in result
    assert 'memtotal_mb' in result
    assert 'swaptotal_mb' in result
    assert 'mounts' in result


# Generated at 2022-06-13 01:00:35.295731
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    obj = HurdHardware()

    uptime_facts = obj.get_uptime_facts()
    memory_facts = obj.get_memory_facts()

    mount_facts = {}
    try:
        mount_facts = obj.get_mount_facts()
    except TimeoutError:
        pass

    facts = {}
    facts.update(uptime_facts)
    facts.update(memory_facts)
    facts.update(mount_facts)

    assert facts == obj.populate()

# Generated at 2022-06-13 01:01:17.426461
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hw_col = HurdHardwareCollector()
    hurd_hw_col.populate()
    assert isinstance(hurd_hw_col.get_facts(), dict)

# Generated at 2022-06-13 01:01:19.163080
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hh = HurdHardware()
    hh.populate()

# Generated at 2022-06-13 01:01:24.543998
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    facts = HurdHardware()
    collected_facts = facts.populate()
    assert collected_facts['uptime_seconds'] > 0
    assert collected_facts['uptime_hours'] > 0
    assert collected_facts['uptime_days'] >= 0
    assert collected_facts['memtotal_mb'] > 0
    assert 'mnt' in collected_facts
    assert len(collected_facts['mnt'])

# Generated at 2022-06-13 01:01:27.859258
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hardware = HurdHardware()
    collected_facts = {'ansible_architecture': 'unknown'}
    hurd_hardware.populate(collected_facts)
    assert collected_facts['ansible_architecture'] == 'unknown'

# Generated at 2022-06-13 01:01:31.355562
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """
    Unit test for method populate of class HurdHardware
    """

    # Instance of HurdHardware
    hardware = HurdHardware()

    # Checking facts returned by method populate
    facts = hardware.populate()

    # Testing method return type
    assert isinstance(facts, dict)

    # Testing method return
    assert len(facts) > 0

# Generated at 2022-06-13 01:01:36.859189
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    module_mock = Mock()
    hw = HurdHardware(module_mock)
    result = hw.populate()
    assert result == {'uptime': 2961886, 'uptime_seconds': 2961886, 'uptime_hours': 82, 'uptime_days': 3, 'memfree_mb': 434, 'memtotal_mb': 995, 'swapfree_mb': 8191, 'swaptotal_mb': 8191}

if __name__ == '__main__':
    test_HurdHardware_populate()

# Generated at 2022-06-13 01:01:41.941268
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    import sys
    import os.path
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
    libvirt_module_utils_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'module_utils', 'libvirt.py')
    libvirt = imp.load_source('libvirt', libvirt_module_utils_path)
    hurd_hardware = HurdHardware()
    facts = {}
    facts.update(hurd_hardware.populate())
    # TODO: unit test the facts

# Generated at 2022-06-13 01:01:43.243024
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    fact_collector = HurdHardwareCollector()
    facts = fact_collector.collect()
    assert facts['mounts']
    assert facts['uptime']

# Generated at 2022-06-13 01:01:43.984360
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    assert HurdHardware().populate()

# Generated at 2022-06-13 01:01:47.805953
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    import unittest.mock as mock

    facts = HurdHardware()

    # Make sure that mount facts are not gathered
    with mock.patch.object(facts, 'get_mount_facts') as mock_mount_facts:
        mock_mount_facts.side_effect = TimeoutError
        facts.populate()
        assert mock_mount_facts.call_count == 1


# Generated at 2022-06-13 01:02:56.631518
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hardware = HurdHardware()
    facts = hurd_hardware.populate()
    assert facts['uptime_seconds'] == 0
    assert facts['memory_mb']['swap']['total'] == 0

# Generated at 2022-06-13 01:02:58.631060
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """
    Construct a HurdHardware object and invoke populate method
    """
    hardware = HurdHardware()
    hardware_facts = hardware.populate()
    assert hardware_facts['uptime'] != 0

# Generated at 2022-06-13 01:03:04.242816
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    class MockHurdHardware:
        def __init__(self, platform, module):
            self._platform = platform
            self._module = module
            self._facts = {}
            self._memory = {}
            self._mounts = {}

    class module:
        params = {}

        def fail_json(self, **kwargs): pass

    class facts:
        collected_facts = {
            'kernel': 'GNU',
            'ansible_facts': {}
        }

    class mount:
        def __init__(self, device, mountpoint, fstype, opts):
            self.device = device
            self.mount = mountpoint
            self.fstype = fstype
            self.opts = opts


# Generated at 2022-06-13 01:03:05.196409
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware = HurdHardware()
    hardware.populate()

# Generated at 2022-06-13 01:03:15.739251
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    import mock
    import os
    import sys

    # Setup mock objects for testing
    test_timeout_exception = TimeoutError('timeout')

    mock_collected_facts = {}
    mock_collected_facts['ansible_facts'] = {}
    mock_collected_facts['ansible_facts']['distribution'] = 'GNU'

    mock_uptime_facts = {}
    mock_uptime_facts['ansible_uptime'] = '1 days, 2 hours, 3 minutes, 4 seconds'
    mock_uptime_facts['ansible_uptime_seconds'] = 12345678

    mock_memory_facts = {}

# Generated at 2022-06-13 01:03:17.694448
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    "Test for method populate of class HurdHardware"
    test_obj = HurdHardware()
    result = test_obj.populate()
    assert result['uptime']

# Generated at 2022-06-13 01:03:20.512272
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware = HurdHardware()
    hardware.populate()

    assert hardware.facts['uptime_seconds'] > 0
    assert hardware.facts['virtualization_type'] == 'Physical'

    assert hardware.facts['virtual'] == {}
    assert hardware.facts['mounts']

# Generated at 2022-06-13 01:03:26.880847
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    test_data = {
        'uptime_seconds': '786435',
        'uptime_days': '9',
        'uptime_hours': '9',
        'uptime_minutes': '3',
        'uptime_seconds': '55',
        'active_processors': '1',
        'total_processors': '1',
        'total_physical_memory': '2097152',
        'total_usable_memory': '2097152',
        'mounted': [
            {'mount': '/', 'device': '/dev/hd0s1', 'fstype': 'hfs', 'options': ''},
            {'mount': 'proc', 'device': '/proc', 'fstype': 'procfs', 'options': ''}
        ]
    }


# Generated at 2022-06-13 01:03:29.300621
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hw = HurdHardware()
    facts = hw.populate()
    assert facts['uptime_seconds'] > 0
    assert facts['memory_mb']['real']['total'] >= 0
    assert sorted(facts.keys()) == ['mounts', 'memory_mb', 'uptime_seconds']

# Generated at 2022-06-13 01:03:34.566962
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware = HurdHardware()
    hardware_facts = hardware.populate()

    # Test hardware.uptime fact
    assert hardware_facts['uptime_seconds'] > 0
    assert 'uptime_formatted' in hardware_facts

    # Test hardware.memory fact
    assert hardware_facts['memory']['total'] > 0
    assert hardware_facts['memory']['swap'].get('total') > 0

    # Test hardware.mount fact
    assert hardware_facts['mounts'] is not None
    assert len(hardware_facts['mounts']) > 0