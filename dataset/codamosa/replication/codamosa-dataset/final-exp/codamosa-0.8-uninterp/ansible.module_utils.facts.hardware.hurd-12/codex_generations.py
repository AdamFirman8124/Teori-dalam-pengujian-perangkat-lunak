

# Generated at 2022-06-13 00:55:47.520337
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware_obj = HurdHardware()
    hardware_facts = hardware_obj.populate()
    assert hardware_facts['uptime'] == "20 days, 23 hours, 21 minutes, 14 seconds"
    assert hardware_facts['uptime_seconds'] == 2043319.43
    assert hardware_facts['memtotal_mb'] == 3869.0
    assert hardware_facts['virtual_memtotal_mb'] == 3869.0
    assert hardware_facts['memfree_mb'] == 3790.0
    assert hardware_facts['memavailable_mb'] == 3790.0
    assert hardware_facts['swaptotal_mb'] == 0.0
    assert hardware_facts['swapfree_mb'] == 0.0


# Generated at 2022-06-13 00:55:51.372328
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hw = HurdHardware()
    res = hurd_hw.populate()
    assert 'uptime_seconds' in res
    assert 'ansible_uptime_seconds' in res
    assert 'memtotal_mb' in res
    assert 'memfree_mb' in res
    assert 'swaptotal_mb' in res
    assert 'swapfree_mb' in res
    assert 'ansible_mounts' in res

# Generated at 2022-06-13 00:55:54.882277
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    class FakeLinuxHardware(HurdHardware):
        def get_mount_facts(self):
            return self.get_uptime_facts()

    hurd_facts = FakeLinuxHardware().populate()
    assert 'uptime_seconds' in hurd_facts, \
        'HurdHardware.get_uptime_facts() result not in hurd_facts.'

# Generated at 2022-06-13 00:55:55.737412
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hw = HurdHardware()
    assert isinstance(hw.populate(), dict)

# Generated at 2022-06-13 00:55:56.834097
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd = HurdHardware()

    facts = hurd.populate()

    assert isinstance(facts, dict)

# Generated at 2022-06-13 00:56:03.810741
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    from ansible.utils.display import Display
    from ansible.module_utils.facts import timeout
    from ansible.module_utils.facts.hardware.linux import get_mount_facts
    from ansible.module_utils.facts.hardware.linux import get_memory_facts
    from ansible.module_utils.facts.hardware.linux import get_uptime_facts
    from ansible.module_utils.facts.hardware.linux import get_stack_size
    from ansible.module_utils.facts.hardware.linux import get_uname_info
    from ansible.module_utils.facts.hardware.linux import parse_uname
    from ansible.module_utils.facts.hardware.linux import get_system_serial_number
    from ansible.module_utils.facts.hardware.linux import get_

# Generated at 2022-06-13 00:56:08.008586
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """
    Test for populate attribute of class HurdHardware
    """
    hurd_hardware = HurdHardware()
    test_hardware_facts = {"hardware_facts": {}}
    assert hurd_hardware.populate() == test_hardware_facts

# Generated at 2022-06-13 00:56:11.045899
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    fact_instance = HurdHardware()
    facts = fact_instance.populate()
    assert facts['uptime_seconds'] > 0
    assert 'MemTotal' in facts['ansible_memfree_mb']
    assert 'ansible_mounts' in facts

# Generated at 2022-06-13 00:56:14.831364
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware_facts = HurdHardware().populate()
    assert 'uptime_seconds' in hardware_facts
    assert 'uptime_days' in hardware_facts
    assert 'mounts' in hardware_facts
    assert 'swapfree_mb' in hardware_facts
    assert 'memfree_mb' in hardware_facts
    assert 'memtotal_mb' in hardware_facts

# Generated at 2022-06-13 00:56:17.365003
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hw = HurdHardware()
    hurd_hw.populate()
    assert 'mounts' in hurd_hw.data

# Generated at 2022-06-13 00:56:21.056205
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hw = HurdHardware()
    assert hw.populate()

# Generated at 2022-06-13 00:56:27.976586
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware_facts = HurdHardware()
    res = hardware_facts.populate()
    assert res == {'uptime_seconds': 375, 'memfree_mb': 8192, 'memtotal_mb': 32768, 'nodename': 'gnu', 'swapfree_mb': 0, 'mounts': [{'mount': '/', 'fstype': 'ufs', 'device': '/dev/hd0s1', 'options': ['rw'], 'options_list': ['rw']}, {'mount': '/tmp', 'fstype': 'tmpfs', 'device': 'tmpfs', 'options': ['rw'], 'options_list': ['rw']}], 'fqdn': 'gnu', 'swaptotal_mb': 0}

# Generated at 2022-06-13 00:56:31.750631
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hw = HurdHardware()
    facts = hw.populate()
    assert facts['uptime_seconds'] > 0
    assert 'total' in facts['mem_facts']['swap']
    assert 'available' in facts['mem_facts']['swap']
    assert 'total' in facts['mem_facts']['real']
    assert 'available' in facts['mem_facts']['real']
    assert '/' in facts['mounts']


# Generated at 2022-06-13 00:56:41.795502
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """
    Test populate function of class HurdHardware
    """
    # We create mock_file for memory information

# Generated at 2022-06-13 00:56:50.800513
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    class MockHurdHardware(HurdHardware):
        def get_uptime_facts(self):
            return {
                "uptime_seconds": 5000000
            }

        def get_memory_facts(self):
            return {
                "memfree_mb": 100,
                "memtotal_mb": 500,
                "swapfree_mb": 200,
                "swaptotal_mb": 600
            }
        def get_mount_facts(self):
            return {
                "/": {"mount": "/", "type": "hurd", "fstype": "vfat", "device": "/dev/hda1"},
                "/tmp": {"mount": "/tmp", "type": "hurd", "fstype": "tmpfs", "device": "tmpfs"}
            }

    mock_HurdHardware = MockHurdHardware()

# Generated at 2022-06-13 00:56:57.380593
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hardware = HurdHardware()
    response = hurd_hardware.populate()

    assert response["uptime"] is not None
    assert response["uptime_seconds"] > 0
    assert response["memtotal_mb"] > 0
    assert response["swaptotal_mb"] > 0
    assert response["devicemapper"] == 'unknown'

    assert len(response["mounts"]) > 0
    for mount in response["mounts"]:
        assert mount["mount"] is not None
        assert mount["device"] is not None
        assert mount["fstype"] is not None

# Generated at 2022-06-13 00:57:03.175966
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hhw = HurdHardware()

    hhw.uptime_facts = {'uptime_seconds': 86400}
    hhw.memory_facts = {'memtotal_mb': 100}
    hhw.mount_facts = {'mounts': [{'mount': '/', 'device': '/dev/hda3'}]}

    hardware_facts = hhw.populate()

    assert hardware_facts == {'uptime_seconds': 86400,
                              'memtotal_mb': 100,
                              'mounts': [{'mount': '/', 'device': '/dev/hda3'}]}

# Generated at 2022-06-13 00:57:04.641078
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    test_HurdHardware = HurdHardware()
    test_HurdHardware.populate()

# Generated at 2022-06-13 00:57:13.488594
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    uptime_facts = {'uptime_seconds': 100}
    memory_facts = {'memtotal_mb': 10}
    mount_facts = {'mounts': [{'mount': '/'}]}

    # Test if the method get_uptime_facts is called
    hw = HurdHardware()
    hw.get_uptime_facts = lambda: uptime_facts

    result = hw.populate()
    assert('uptime_seconds' in result)
    assert(result['uptime_seconds'] == 100)

    # Test if the method get_memory_facts is called
    hw = HurdHardware()
    hw.get_memory_facts = lambda: memory_facts

    result = hw.populate()
    assert('memtotal_mb' in result)

# Generated at 2022-06-13 00:57:19.834751
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurdhw = HurdHardware()
    collected_facts = {}
    uptime_facts = {}
    memory_facts = {}
    mount_facts = {}

    hurdhw.get_uptime_facts = lambda: uptime_facts
    hurdhw.get_memory_facts = lambda: memory_facts
    hurdhw.get_mount_facts = lambda: mount_facts

    result = hurdhw.populate(collected_facts)
    expected = {}
    expected.update(uptime_facts)
    expected.update(memory_facts)
    expected.update(mount_facts)

    assert result == expected

# Generated at 2022-06-13 00:57:31.886662
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd = HurdHardware()

    # Mock get_uptime_facts, get_memory_facts and get_mount_facts
    hurd.get_uptime_facts = lambda: { 'uptime_seconds': 42 }
    hurd.get_memory_facts = lambda: { 'memtotal_mb': 42 }
    hurd.get_mount_facts = lambda: { '/': { 'fstype': 'ext2' } }

    facts = hurd.populate()

    assert facts['uptime_seconds'] == 42
    assert facts['memtotal_mb'] == 42
    assert facts['mounts']['/']['fstype'] == 'ext2'

# Generated at 2022-06-13 00:57:39.343995
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # Init facts with GNU/Hurd platform type
    collected_facts = {'ansible_facts': {'ansible_system': 'GNU'}}

    # Create an instance of HurdHardware class
    hurd_system = HurdHardware()

    # Get facts from method populate of class HurdHardware
    hurd_hardware_facts = hurd_system.populate(collected_facts)

    # Check if ansible_facts are set
    assert 'ansible_facts' in hurd_hardware_facts
    # Check if the Linux hardware facts are set
    assert 'ansible_mounts' in hurd_hardware_facts['ansible_facts']
    assert 'ansible_memtotal_mb' in hurd_hardware_facts['ansible_facts']
    assert 'ansible_processor' in hurd_hardware_facts['ansible_facts']

# Generated at 2022-06-13 00:57:50.691187
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    with open('/proc/meminfo', 'rb') as f:
        facts = HurdHardware().populate()
        data = f.read()
        lines = data.splitlines()
        meminfo = {x.split(b':')[0].strip(): x.split(b':')[1].strip()
                   for x in lines}
        assert facts['memtotal_mb'] == int(meminfo[b'MemTotal'].split()[0]) / 1024
        assert facts['memfree_mb'] == int(meminfo[b'MemFree'].split()[0]) / 1024
        assert facts['swaptotal_mb'] == int(meminfo[b'SwapTotal'].split()[0]) / 1024
        assert facts['swapfree_mb'] == int(meminfo[b'SwapFree'].split()[0])

# Generated at 2022-06-13 00:57:57.553571
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hardware_facts = HurdHardware.populate()
    assert hurd_hardware_facts['uptime_seconds'] > -1, "uptime_seconds not populated as expected"
    assert hurd_hardware_facts['memory_mb']['real']['total'] > -1, "memory_mb not populated as expected"
    assert hurd_hardware_facts['mounts'] != {}, "mounts not populated as expected"

if __name__ == '__main__':
    test_HurdHardware_populate()

# Generated at 2022-06-13 00:58:05.925586
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # Define a fake class for the superclass
    class LinuxHardware(object):
        def get_uptime_facts(self):
            return {'uptime_seconds': 1}

        def get_memory_facts(self):
            return {'memtotal_mb': 2}

        def get_mount_facts(self):
            return {'mounts': [
                {'mount': '/', 'size_total': 3},
                {'mount': '/var', 'size_total': 4}
            ]}

    # Set up a fake class to mimic the standard hardwaredetect module
    class module:
        def __init__(self):
            self.fail_json = print
            self.params = {}

    # Set up a fake class to pass to the module with real HurdHardware class

# Generated at 2022-06-13 00:58:10.463961
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hw = HurdHardware()
    hw_facts = hw.populate()
    assert hw_facts.get('uptime')
    assert hw_facts.get('uptime_seconds')
    assert hw_facts.get('memory')
    assert hw_facts.get('swap')
    assert hw_facts['memory'].get('total')

# Generated at 2022-06-13 00:58:17.480470
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """
    Pass a mock object to class HurdHardware and check the collected facts
    """
    collected_facts = {
        'ansible_system': "Hurd",
        'ansible_architecture': "hurd-i386",
        'ansible_os_family': "Un*x"
    }

    h = HurdHardware()

    # mock for get_uptime_facts
    def mock_get_uptime_facts():
        return {'ansible_uptime_seconds': 15000}

    h.get_uptime_facts = mock_get_uptime_facts

    # mock for get_memory_facts

# Generated at 2022-06-13 00:58:22.715199
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    module = None
    collected_facts = None
    hardware = HurdHardware(module, collected_facts)
    facts = hardware.populate()

    # Test that the facts contain at least the mandatory
    # keys described in the module documentation
    assert 'uptime' in facts
    assert 'uptime_seconds' in facts
    assert 'memfree_mb' in facts
    assert 'memtotal_mb' in facts
    assert 'mounts' in facts

# Generated at 2022-06-13 00:58:31.996745
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    host_name = 'test_hurd'
    platform = 'GNU'
    cpu_count = 1
    cpu_count_logical = 1
    cpu_vendor_id = 'GenuineIntel'
    cpu_model_name = 'Intel(R) Core(TM)2 CPU T5500 @ 1.66GHz'
    cpu_freq = 1666000000
    cpu_architecture = 'x86_64'

# Generated at 2022-06-13 00:58:43.331687
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    collector = HurdHardwareCollector()
    collected_facts = dict()
    hardware_facts = collector.populate(collected_facts)

    assert 'uptime_seconds' in hardware_facts
    assert isinstance(hardware_facts['uptime_seconds'], int)

    assert 'uptime_days' in hardware_facts
    assert isinstance(hardware_facts['uptime_days'], int)

    assert 'uptime_hours' in hardware_facts
    assert isinstance(hardware_facts['uptime_hours'], int)

    assert 'uptime_minutes' in hardware_facts
    assert isinstance(hardware_facts['uptime_minutes'], int)

    assert 'memtotal_mb' in hardware_facts
    assert isinstance(hardware_facts['memtotal_mb'], int)


# Generated at 2022-06-13 00:58:54.143348
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware = HurdHardware()
    hardware.populate()
    uptime = hardware.uptime
    ram = hardware.ram
    memory = hardware.memory

    assert(uptime['days'] >= 0)
    assert(uptime['hours'] >= 0)
    assert(uptime['minutes'] >= 0)
    assert(uptime['seconds'] >= 0)

    assert(0 in ram.values())
    assert(0 in memory.values())

# Generated at 2022-06-13 00:58:59.487373
# Unit test for method populate of class HurdHardware

# Generated at 2022-06-13 00:58:59.990213
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    pass

# Generated at 2022-06-13 00:59:04.108382
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # Setup an HurdHardware object for testing
    hurdhw = HurdHardware()

    # Test that method does not return None
    assert hurdhw.populate() is not None, "method populate returned None"
    # Test that method runs
    assert isinstance(hurdhw.populate(), dict), "method populate did not return a dict"


# Generated at 2022-06-13 00:59:12.590157
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    _platform = 'GNU'
    _distribution = 'Hurd'
    _platform_version = ''
    _system = 'GNU'
    _distribution_release = ''
    _distribution_version = ''
    _kernel_version = 5
    _hostname = 'host'
    _virtualization_type = 'physical'

    with open('ansible/module_utils/facts/hardware/tests/unit/fixtures/Hurd/memoryinfo', 'r') as f:
        fact_hurd_memoryinfo = f.read()
    with open('ansible/module_utils/facts/hardware/tests/unit/fixtures/Hurd/mount', 'r') as f:
        fact_hurd_mount = f.read()

    hurd_hardware_facts = HurdHardware()
    hurd_hardware_

# Generated at 2022-06-13 00:59:19.624189
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    o = HurdHardware()
    facts = o.populate()
    elist = []

    if not facts["uptime_seconds"]:
        elist.append("uptime_seconds")
    if not facts["uptime_hours"]:
        elist.append("uptime_hours")
    if not facts["uptime_days"]:
        elist.append("uptime_days")
    if not facts["totalmem_mb"]:
        elist.append("totalmem_mb")
    if not facts["memfree_mb"]:
        elist.append("memfree_mb")
    if not facts["swapfree_mb"]:
        elist.append("swapfree_mb")
    if elist:
        for item in elist:
            print("Failed to collect %s fact" % (item))


# Generated at 2022-06-13 00:59:30.640634
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    collector = HurdHardwareCollector()
    fact_instance = collector.get_fact_instance()
    collected_facts = {'ansible_facts': {'hardware': {}}}
    collected_facts['ansible_facts']['hardware']['uptime_seconds'] = 3600
    collected_facts['ansible_facts']['hardware']['memfree_mb'] = 1234
    collected_facts['ansible_facts']['hardware']['swapfree_mb'] = 2345
    collected_facts['ansible_facts']['hardware']['/'] = {'mount': '/', 'size_total': 5000,
                                                        'size_available': 2000, 'device': 'dev/root'}

# Generated at 2022-06-13 00:59:32.712286
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """
    Test module of HurdHardware.populate()
    """
    hurd_hardware = HurdHardware({})
    hurd_hardware.populate()
    assert False

# Generated at 2022-06-13 00:59:43.257839
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """
    Create a fake mountpoint, fake uptime and fake /proc/meminfo

    Every test method should have this signature.
    """
    import tempfile
    import os
    import re

    # Create a fake mountpoint
    suffix = '_ansible_test_facts'
    mount_dir = tempfile.mkdtemp(suffix)

# Generated at 2022-06-13 00:59:44.792103
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware_facts = HurdHardware().populate()
    assert isinstance(hardware_facts, dict)

# Generated at 2022-06-13 01:00:08.574814
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # Setup a HurdHardware object and test the populate method.
    hurd_hardware = HurdHardware()
    collected_facts = hurd_hardware.populate()

    assert(collected_facts['uptime_seconds'] == 4)
    assert(collected_facts['uptime_days'] == 0)
    assert(collected_facts['memfree_mb'] == 306)
    assert(collected_facts['memtotal_mb'] == 1024)
    assert(collected_facts['swaptotal_mb'] == 1023)
    assert(collected_facts['swapfree_mb'] == 1023)

    # Just sanity check the collected mount facts
    keys = collected_facts['mounts'][0].keys()
    assert(len(keys) == 8)
    assert('device' in keys)

# Generated at 2022-06-13 01:00:13.337501
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # Create an instance of HurdHardware
    hardware = HurdHardware()
    # Try to populate the facts
    hardware.populate()
    # Assert the facts named 'kernel' and 'mounts' are collected, then the
    # method populate succeeds
    assert hardware.facts['kernel']
    assert hardware.facts['mounts']

# Generated at 2022-06-13 01:00:22.648915
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # Setup test data
    collected_facts = {}
    collected_facts['mounts'] = [{
        'device': 'test_device',
        'mount': 'test_mount',
        'fstype': 'test_fstype',
        'options': 'test_options',
        'size_total': 123456,
        'size_available': 12345,
        'size_used': 111111
    }]
    collected_facts['uptime_seconds'] = 1234567

    # Test that the populate method of HurdHardware can be called and return
    # a dict of facts
    hw = HurdHardware()
    facts = hw.populate(collected_facts)

# Generated at 2022-06-13 01:00:33.197698
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """
    Test multiple calls to method populate with different facts
    produced by a mock. Returned dictionary should not change.
    """
    hardware = HurdHardware()
    hardware._uptime = {'ansible_uptime_seconds': 42}
    hardware._memory = {'ansible_memtotal_mb': 1337}
    collected = hardware.populate()

    assert collected['ansible_uptime_seconds'] == 42
    assert collected['ansible_memtotal_mb'] == 1337

    mocks = [
      {'ansible_uptime_seconds': 42, 'ansible_memtotal_mb': 1337},
      {'ansible_uptime_seconds': 7, 'ansible_memtotal_mb': 0}
    ]
    for i, mock in enumerate(mocks):
        hardware._uptime = mock
       

# Generated at 2022-06-13 01:00:42.736710
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    collected_facts = {'ansible_os_family': 'Debian',
                       'ansible_lsb': {'id': 'GNU/Hurd',
                                       'release': '1.0',
                                       'codename': 'Debian',
                                       'major_release': '1.0'}}
    hw = HurdHardware(collected_facts)
    hardware_facts = hw.populate()
    assert hardware_facts['uptime_seconds'] > 0
    assert hardware_facts['uptime_hours'] > 0
    assert hardware_facts['uptime_days'] > 0
    assert hardware_facts['memtotal_mb'] > 0
    assert hardware_facts['memfree_mb'] >= 0
    assert hardware_facts['swaptotal_mb'] > 0

# Generated at 2022-06-13 01:00:43.596437
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    h = HurdHardware()
    h.populate()

# Generated at 2022-06-13 01:00:51.383480
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """
    Test facts derived by method populate of HurdHardware.
    """
    import os
    import tempfile

    from ansible.module_utils.facts.hardware.hurd import HurdHardware

    # Create a temporary directory for mocking the filesystem of GNU Hurd
    tmp_dir = tempfile.TemporaryDirectory()

    # Create procfs compatibility translator files in the temporary directory
    os.makedirs(os.path.join(tmp_dir.name, 'proc', '3'), exist_ok=True)
    os.makedirs(os.path.join(tmp_dir.name, 'proc', '4'), exist_ok=True)
    os.makedirs(os.path.join(tmp_dir.name, 'proc', '5'), exist_ok=True)

    # Populate the temporary directory with procfs compatibility translator files

# Generated at 2022-06-13 01:00:55.704671
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hw = HurdHardware()
    hw.populate()
    # From subclass LinuxHardware
    assert hw.module.params['filter'] == ['!lo']
    assert hw.module.params['gather_network_resources'] == 'strict'
    # From class Hardware
    assert hw.module.params['gather_subset'] == ['all']

# Generated at 2022-06-13 01:01:00.500525
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    h = HurdHardware()
    facts = h.populate()
    assert 'uptime_seconds' in facts
    assert 'uptime_days' in facts
    assert 'memtotal_mb' in facts
    assert 'memfree_mb' in facts
    assert 'swaptotal_mb' in facts
    assert 'swapfree_mb' in facts

# Generated at 2022-06-13 01:01:03.805018
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """Check GNU/Hurd specific subclass of Hardware.
    Define memory and mount facts based on procfs compatibility translator
    mimicking the interface of the Linux kernel.
    """
    get_uptime_facts = lambda self: {'uptime': 1.123}
    get_memory_facts = lambda self: {'memtotal': 1000, 'memfree': 500}
    get_mount_facts = lambda self: {'mounts': []}
    hw = HurdHardware()
    hw.get_uptime_facts = get_uptime_facts.__get__(hw, HurdHardware)
    hw.get_memory_facts = get_memory_facts.__get__(hw, HurdHardware)
    hw.get_mount_facts = get_mount_facts.__get__(hw, HurdHardware)
    hw

# Generated at 2022-06-13 01:01:45.161465
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # Stub out superclass methods
    def get_uptime_facts():
        return {}
    def get_memory_facts():
        return {}
    def get_mount_facts():
        return {}
    HurdHardware.get_uptime_facts = get_uptime_facts
    HurdHardware.get_memory_facts = get_memory_facts
    HurdHardware.get_mount_facts = get_mount_facts
    hurd_hardware = HurdHardware()
    assert isinstance(hurd_hardware.populate(), dict)
    # Remove stubs
    del HurdHardware.get_uptime_facts
    del HurdHardware.get_memory_facts
    del HurdHardware.get_mount_facts

# Generated at 2022-06-13 01:01:47.618121
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    facts = HurdHardware()
    results = facts.populate()
    assert results['uptime']
    assert results['uptime_seconds']
    assert results['memtotal_mb']
    assert results['swaptotal_mb']

# Generated at 2022-06-13 01:01:51.987557
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    h = HurdHardware()
    f = h.populate()

    assert isinstance(f, dict)
    assert 'memory' in f
    assert 'swap' in f
    assert 'uptime' in f
    assert 'boot_time' in f
    assert 'mounts' in f


# Generated at 2022-06-13 01:01:52.518187
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    pass

# Generated at 2022-06-13 01:02:01.333972
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    import sys
    import os.path
    import tempfile
    import time
    import errno
    from ansible.module_utils.facts import timeout
    from ansible.module_utils.facts.hardware.linux import LinuxHardware
    from ansible.module_utils.facts.hardware.hurd import HurdHardware

    class TestHurdHardware(HurdHardware):
        def __init__(self):
            pass

        def _mangle_uptime(self, uptime_fmt):
            return uptime_fmt

        def _get_uptime_seconds(self):
            return 42


# Generated at 2022-06-13 01:02:06.475397
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    fact = HurdHardware()
    fact.populate()

    assert fact.populate() == {
        'uptime': 647,
        'uptime_hours': 0,
        'uptime_seconds': 647,
        'virtualization_role': 'guest',
        'virtualization_type': None,
        'memory_mb': {
            'real': {
                'total': 7961
            },
            'swap': {
                'total': 1
            }
        }
    }

# Generated at 2022-06-13 01:02:17.566623
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """
    Test HurdHardware.populate method.
    """
    from ansible.module_utils.facts.hardware.linux import LinuxHardware
    from ansible.module_utils.facts.timeout import TimeoutError

    # Prepare test data
    collected_facts = {}
    collected_facts['kernel'] = 'GNU'
    collected_facts['os_family'] = 'GNU/Hurd'
    collected_facts['system'] = 'GNU'
    dummy_linux_hardware = LinuxHardware()
    dummy_linux_hardware.get_uptime_facts = lambda: {'uptime_seconds': 0}
    dummy_linux_hardware.get_memory_facts = lambda: {'memory_mb': {'real': {'total': 0}} }

# Generated at 2022-06-13 01:02:18.996439
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # no_platform_facts is tested in LinuxHardware
    pass

# Generated at 2022-06-13 01:02:27.951719
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hh = HurdHardware()
    hh.populate()
    assert hh.populate() == {
        'uptime': {'seconds': 286596, 'hours': 79, 'days': 3},
        'memory': {
            'swap': {'available': 0, 'total': 0},
            'real': {
                'available': 5497577472,
                'used': 135946240,
                'total': 5633521664
            }
        },
        'mounts': [
            {'device': '/dev/hd0s1', 'fstype': 'hfs', 'mount': '/', 'size_total': 41943040},
            {'device': 'none', 'fstype': 'procfs', 'mount': '/proc', 'size_total': 0}
        ]
    }

# Generated at 2022-06-13 01:02:29.003625
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hd = HurdHardware()
    hd.populate()

# Generated at 2022-06-13 01:03:11.017536
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    from ansible.module_utils.facts.timeout import TimeoutError
    hardware = HurdHardware()
    hardware.files = {
        '/proc/uptime': '1\n2\n',
        '/proc/meminfo': 'MemTotal:       100\nMemFree:         50\nBuffers:         5\nCached:          5\n',
        '/proc/mounts': '',
        '/proc/swaps': '',
    }
    hardware.get_mount_facts = lambda: {'mounts': 'a'}
    hardware.get_uptime_facts = lambda: {'uptime': 'a'}
    hardware.get_memory_facts = lambda: {'memory': 'a'}
    hardware.populate()
    hardware.get_mount_facts = lambda: {'mounts': 'a'}

# Generated at 2022-06-13 01:03:17.233206
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hw_obj = HurdHardware()
    collected_facts = {}
    hw_facts = hw_obj.populate(collected_facts)

    assert 'uptime_seconds' in hw_facts
    assert 'uptime_days' in hw_facts
    assert 'memfree_mb' in hw_facts
    assert 'memtotal_mb' in hw_facts
    assert 'swaptotal_mb' in hw_facts
    assert 'swapfree_mb' in hw_facts

# Generated at 2022-06-13 01:03:17.975247
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    h = HurdHardware()
    h.populate()

# Generated at 2022-06-13 01:03:20.957817
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hr = HurdHardware()
    h = {}
    h.update(hr.get_uptime_facts())
    h.update(hr.get_memory_facts())
    h.update(hr.get_mount_facts())

    # Just test for a few facts for now
    assert h
    assert h['uptime_seconds'] > 0
    assert h['total_real_mem'] > 0


# Generated at 2022-06-13 01:03:23.388028
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    from ansible.module_utils.facts import hardware, linux

    hw = hardware.HurdHardware()
    assert isinstance(hw, linux.LinuxHardware)
    assert hw._platform == 'GNU'

# Generated at 2022-06-13 01:03:29.300530
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware = HurdHardware()
    hardware.populate()
    assert hardware.uptime['seconds'] is not None
    assert hardware.uptime['days'] is not None
    assert hardware.uptime['hours'] is not None
    assert hardware.uptime['minutes'] is not None
    assert hardware.memory['swapfree_mb'] is not None
    assert hardware.memory['swaptotal_mb'] is not None
    assert hardware.memory['memfree_mb'] is not None
    assert hardware.memory['memtotal_mb'] is not None
    assert hardware.memory['swapfree'] is not None
    assert hardware.memory['swaptotal'] is not None
    assert hardware.memory['memfree'] is not None
    assert hardware.memory['memtotal'] is not None
    assert hardware.memory['real']['total'] is not None

# Generated at 2022-06-13 01:03:34.644559
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    from ansible.module_utils.facts.hardware import Hardware
    from ansible.module_utils.facts.timeout import TimeoutError

    hardware = Hardware()
    hurd_hardware = HurdHardware()
    hurd_hardware.populate(hardware)
    
    assert hardware.uptime_seconds >= 0
    assert hardware.uptime_seconds is not None
    assert hardware.uptime_seconds > 60

    assert hardware.uptime_days >= 0
    assert hardware.uptime_days is not None
    assert hardware.uptime_days > 0

    assert hardware.memtotal_mb >= 0
    assert hardware.memtotal_mb is not None
    assert hardware.memtotal_mb > 0

    assert hardware.memfree_mb >= 0
    assert hardware.memfree_mb is not None

# Generated at 2022-06-13 01:03:40.758964
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hardware = HurdHardware()
    hardware.populate()
    assert hardware.populate()['uptime']
    assert hardware.populate()['uptime_seconds']
    assert hardware.populate()['memtotal_mb']
    assert hardware.populate()['memfree_mb']
    assert hardware.populate()['memavailable_mb']
    assert hardware.populate()['swaptotal_mb']
    assert hardware.populate()['swapfree_mb']
    assert hardware.populate()['mounts']

# Generated at 2022-06-13 01:03:49.689157
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    # we are not actually interested in HurdHardware class itself
    # we are interested in ``LinuxHardware`` class
    # so let's just mock the parent class' method as appropriate
    # and confirm that the subclass indeed calls it with the
    # correct parameters
    from mock import patch, call
    from ansible.module_utils.facts.hardware.hurd import HurdHardware
    with patch.object(HurdHardware, 'get_uptime_facts') as get_uptime_facts, \
            patch.object(HurdHardware, 'get_memory_facts') as get_memory_facts, \
            patch.object(HurdHardware, 'get_mount_facts') as get_mount_facts:
        get_uptime_facts.return_value = {'uptime': 1}

# Generated at 2022-06-13 01:03:56.130670
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """Test if method populate of class HurdHardware works correctly"""

    class MockHurdHardware(HurdHardware):
        """Mock class for testing"""

        def get_mount_facts(self):
            """Mock function for testing"""
            return {'mounts': ['Mock']}

        def get_memory_facts(self):
            """Mock function for testing"""
            return {'memtotal_mb': 'Mock'}

        def get_uptime_facts(self):
            """Mock function for testing"""
            return {'uptime': 'Mock'}

    dummy = MockHurdHardware()
    ret = dummy.populate()
    assert 'mounts' in ret
    assert 'memtotal_mb' in ret
    assert 'uptime' in ret

# Generated at 2022-06-13 01:05:27.783745
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hw = HurdHardware()
    hw.collect()
    assert 'uptime_seconds' in hw.facts
    assert 'uptime_hours' in hw.facts
    assert 'uptime_days' in hw.facts
    assert 'uptime' in hw.facts
    assert 'memfree_mb' in hw.facts
    assert 'memtotal_mb' in hw.facts
    assert 'swapfree_mb' in hw.facts
    assert 'swaptotal_mb' in hw.facts
    assert 'mounts' in hw.facts

# Generated at 2022-06-13 01:05:28.677309
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hw = HurdHardware()
    hurd_hw.populate()

# Generated at 2022-06-13 01:05:33.888266
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    hurd_hardware_facts = HurdHardware()
    hurd_hardware_facts_ref = dict()
    hurd_hardware_facts_ref['uptime_seconds'] = 100
    hurd_hardware_facts_ref['uptime_hours'] = 0
    hurd_hardware_facts_ref['uptime_days'] = 0
    hurd_hardware_facts_ref['memtotal_mb'] = 100
    hurd_hardware_facts_ref['memfree_mb'] = 90
    hurd_hardware_facts_ref['memavailable_mb'] = 60
    hurd_hardware_facts_ref['mounts'] = \
        [{'mount': '/', 'device': '/dev/hda1'}]

    assert(hurd_hardware_facts.populate() == hurd_hardware_facts_ref)

# Generated at 2022-06-13 01:05:38.706349
# Unit test for method populate of class HurdHardware
def test_HurdHardware_populate():
    """ Check if facts for Hurd are populated correctly """
    hurd_hw = HurdHardware()
    facts = hurd_hw.populate()

    assert facts['uptime_seconds']
    assert facts['uptime_days']
    assert facts['uptime']
    assert facts['mem_total']
    assert facts['mem_free']
    assert facts['swap_total']
    assert facts['swap_free']
