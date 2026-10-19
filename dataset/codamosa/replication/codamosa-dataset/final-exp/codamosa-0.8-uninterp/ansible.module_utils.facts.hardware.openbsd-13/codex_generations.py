

# Generated at 2022-06-13 01:06:27.235310
# Unit test for method get_memory_facts of class OpenBSDHardware
def test_OpenBSDHardware_get_memory_facts():
    fixture_data = {
        '/usr/bin/vmstat': '''\
procs    memory       page                    disks    traps          cpu
r b w    avm     fre  flt  re  pi  po  fr  sr wd0 fd0  int   sys   cs us sy id
0 0 0  47512   28160   51   0   0   0   0   0   1   0  116    89   17  0  1 99
        ''',
        'sysctl': {
            'hw.usermem': '1637895168',
        },
    }

    module = AnsibleModule(argument_spec={})
    hardware = OpenBSDHardware(module=module)

    # Override methods to force specific logic in the module to happen
    def get_file_content(path):
        return fixture_data[path]

   

# Generated at 2022-06-13 01:06:30.879451
# Unit test for constructor of class OpenBSDHardwareCollector
def test_OpenBSDHardwareCollector():
    openbsd_hardware_collector = OpenBSDHardwareCollector()
    assert openbsd_hardware_collector
    assert openbsd_hardware_collector._fact_class == OpenBSDHardware
    assert openbsd_hardware_collector._platform == 'OpenBSD'

# Generated at 2022-06-13 01:06:35.778908
# Unit test for method get_uptime_facts of class OpenBSDHardware
def test_OpenBSDHardware_get_uptime_facts():
    mocked_module = MockOpenBSDModule()
    mocked_module.run_command.return_value = (0, '1556373729', '')

    facts = OpenBSDHardware(mocked_module).get_uptime_facts()
    assert facts == {'uptime_seconds': 609}


# Generated at 2022-06-13 01:06:45.065228
# Unit test for method get_memory_facts of class OpenBSDHardware
def test_OpenBSDHardware_get_memory_facts():
    import pytest
    from ansible.module_utils.facts import Module

    # create a mock ansible module
    module = Module()
    module.run_command = MagicMock(return_value=(0, '47512   28160', 'none of your business'))

    # create a mock OpenBSDHardware object
    hardware = OpenBSDHardware(module=module)
    hardware.sysctl = {'hw.usermem': '546042880'}
    memory_facts = hardware.get_memory_facts()
    assert memory_facts['memfree_mb'] == 28160
    assert memory_facts['memtotal_mb'] == 532



# Generated at 2022-06-13 01:06:46.123246
# Unit test for constructor of class OpenBSDHardwareCollector
def test_OpenBSDHardwareCollector():
    OpenBSDHardwareCollector()  # noqa

# Generated at 2022-06-13 01:06:57.418546
# Unit test for method populate of class OpenBSDHardware
def test_OpenBSDHardware_populate():
    # Test with no data
    hardware = OpenBSDHardware({}, {}, {})
    hardware.populate()
    assert 'devices' in hardware.facts

    # Test with data
    hardware = OpenBSDHardware({}, {'hw.usermem': 1048576}, {})
    hardware.populate()
    assert hardware.facts['memtotal_mb'] == 1

    # Test with data and vmstat
    hardware = OpenBSDHardware({}, {'hw.usermem': 1048576}, {'/usr/bin/vmstat': 0})
    hardware.populate()
    assert hardware.facts['memtotal_mb'] == 1
    assert hardware.facts['memfree_mb'] == 0

    # Test with data and swapctl

# Generated at 2022-06-13 01:07:09.844967
# Unit test for method get_processor_facts of class OpenBSDHardware
def test_OpenBSDHardware_get_processor_facts():
    module = Mock()
    module.run_command.return_value = (0, 'amd64', '')
    mod = OpenBSDHardware(module)
    mod.sysctl = {'hw.ncpuonline': '2',
                  'hw.model': 'Intel(R) Core(TM) i5-3570K CPU @ 3.40GHz'}

    ret = mod.get_processor_facts()
    mod.module.run_command.assert_has_calls([
        call(['sysctl', '-n', 'hw.ncpuonline']),
        call(['sysctl', '-n', 'hw.model'])
    ])

# Generated at 2022-06-13 01:07:17.704210
# Unit test for method get_uptime_facts of class OpenBSDHardware
def test_OpenBSDHardware_get_uptime_facts():
    from ansible.module_utils.facts.openbsd import OpenBSDHardware
    from datetime import datetime
    import calendar
    import time

    test_kern_boottime = datetime.fromtimestamp(calendar.timegm(time.gmtime()) - (24*60*60)).timestamp()

    ret = OpenBSDHardware._get_uptime_facts(test_kern_boottime)
    assert(ret == {'uptime_seconds': 24 * 60 * 60})



# Generated at 2022-06-13 01:07:30.335683
# Unit test for method get_uptime_facts of class OpenBSDHardware
def test_OpenBSDHardware_get_uptime_facts():
    from ansible.module_utils.facts.collector import get_collector
    from ansible.module_utils.facts.timeout import FakeTimout

    class FakeModule(object):
        def __init__(self):
            self.run_command = test_OpenBSDHardware_get_uptime_facts_FakeModule_ansible_module_run_command

        def get_bin_path(self, x):
            return x

    class FakeCollector(object):
        def __init__(self):
            self.get_module_utils_facts = test_OpenBSDHardware_get_uptime_facts_FakeCollector_get_module_utils_facts


# Generated at 2022-06-13 01:07:42.096520
# Unit test for method get_memory_facts of class OpenBSDHardware
def test_OpenBSDHardware_get_memory_facts():
    module = DummyAnsibleModule()
    obshw = OpenBSDHardware(module)
    obshw.sysctl = {'hw.usermem': '2395738112'}

    # Test 1: get_memory_facts fails on /usr/bin/vmstat
    module.run_command = lambda x: (1, '', 'open: No such file or directory')
    get_memory_facts_result = obshw.get_memory_facts()
    assert get_memory_facts_result['memfree_mb'] == ''
    assert get_memory_facts_result['memtotal_mb'] == ''

    # Test 2: get_memory_facts fails on /sbin/swapctl
    module.run_command = lambda x: (1, '', 'open: No such file or directory')
    get_memory_facts_

# Generated at 2022-06-13 01:07:58.229384
# Unit test for method get_processor_facts of class OpenBSDHardware
def test_OpenBSDHardware_get_processor_facts():
    """
    unit test for method get_processor_facts of class OpenBSDHardware
    """
    # mock_module is used to mock a module playing the role of a AnsibleModule
    # object. This is necessary to allow the execution of
    # OpenBSDHardware.get_processor_facts()
    mock_module = MockAnsibleModule({'hw.ncpuonline':'2', 'hw.model' : 'Intel(R) Core(TM) i7-4770 CPU @ 3.40GHz'})

    # mock_module.run_command is used to mock the run_command method of
    # the AnsibleModule object. It is used to control the behavior of the
    # sysctl command.
    mock_module.run_command.return_value = (0, '', '')

    # get the object of OpenBSDHardware class
    hardware = Open

# Generated at 2022-06-13 01:08:05.401687
# Unit test for method get_memory_facts of class OpenBSDHardware
def test_OpenBSDHardware_get_memory_facts():
    test_module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    sysctl = {'hw.usermem': str(1024 * 1024 * 1024)}
    mock_run_command = Mock(return_value=(0, "", ""))
    test_module.run_command = mock_run_command
    test_OpenBSDHardware = OpenBSDHardware(test_module)
    test_OpenBSDHardware.sysctl = sysctl
    result = test_OpenBSDHardware.get_memory_facts()
    assert result == {'memfree_mb': 1024, 'memtotal_mb': 1024}


# Generated at 2022-06-13 01:08:10.372150
# Unit test for method get_dmi_facts of class OpenBSDHardware
def test_OpenBSDHardware_get_dmi_facts():
    '''Unit test for method get_dmi_facts of class OpenBSDHardware'''
    facts = OpenBSDHardwareCollector().collect()
    assert 'dmi' in facts['ansible_facts']['ansible_hardware']
    assert 'product_uuid' in facts['ansible_facts']['ansible_hardware']['dmi']


# Generated at 2022-06-13 01:08:18.371659
# Unit test for method populate of class OpenBSDHardware
def test_OpenBSDHardware_populate():

    class MockModule(object):
        def __init__(self):
            self.params = {}
            self.run_command = lambda x, **kwargs: ('', '', 0)
            self.get_bin_path = lambda x: '/usr/bin/vmstat'

    class MockSysctl(dict):
        def __init__(self, values):
            for k in values:
                v = values[k]
                if not isinstance(v, dict):
                    v = to_text(v, errors='surrogate_or_strict')
                self[k] = v

        def __getitem__(self, k):
            try:
                return dict.__getitem__(self, k)
            except KeyError:
                return ''

    module = MockModule()


# Generated at 2022-06-13 01:08:21.274178
# Unit test for constructor of class OpenBSDHardwareCollector
def test_OpenBSDHardwareCollector():
    module = ansible.module_utils.basic.AnsibleModule(argument_spec={})
    assert OpenBSDHardwareCollector(module)

# Generated at 2022-06-13 01:08:32.274503
# Unit test for method get_uptime_facts of class OpenBSDHardware
def test_OpenBSDHardware_get_uptime_facts():
    uptime_seconds = 100
    uptime_command = "echo %d" % uptime_seconds
    module = mock_module_helper()
    module.params['gather_subset'] = ['!all', 'hardware']
    module.params['filter'] = '*'
    hardware = OpenBSDHardware(module=module)
    hardware.sysctl = {'kern.boottime': uptime_seconds}
    hardware.module.run_command = mock_run_command
    hardware.module.get_bin_path = mock_get_bin_path

    results = hardware.populate()

    assert 'uptime_seconds' in results
    assert results['uptime_seconds'] == uptime_seconds



# Generated at 2022-06-13 01:08:34.082701
# Unit test for constructor of class OpenBSDHardwareCollector
def test_OpenBSDHardwareCollector():
    result = OpenBSDHardwareCollector()
    assert result._platform == 'OpenBSD'

# Generated at 2022-06-13 01:08:42.339847
# Unit test for method populate of class OpenBSDHardware
def test_OpenBSDHardware_populate():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=False)
    result = OpenBSDHardware(module).populate()
    assert result['devices'].__len__() > 0
    assert result['devices'][0].__len__() > 0
    assert result['memtotal_mb'] > 0
    assert result['memfree_mb'] > 0
    assert result['swaptotal_mb'] > 0
    assert result['swapfree_mb'] > 0
    assert result['processor'].__len__() > 0
    assert result['processor'][0].__len__() > 0
    assert result['processor_cores'] > 0
    assert result['processor_count'] > 0
    assert result['processor_speed'] > 0
    assert result['uptime_seconds'] > 0

# Unit test

# Generated at 2022-06-13 01:08:44.451374
# Unit test for constructor of class OpenBSDHardwareCollector
def test_OpenBSDHardwareCollector():
    hardware_collector = OpenBSDHardwareCollector()
    assert hardware_collector
    assert hardware_collector.platform == 'OpenBSD'

# Generated at 2022-06-13 01:08:48.105760
# Unit test for constructor of class OpenBSDHardwareCollector
def test_OpenBSDHardwareCollector():
    expected = [
        OpenBSDHardware,
        ]
    hwc = OpenBSDHardwareCollector()
    actual = hwc.collect()

    assert actual == expected

# Generated at 2022-06-13 01:09:10.918405
# Unit test for method populate of class OpenBSDHardware
def test_OpenBSDHardware_populate():
    module = AnsibleModule(argument_spec=dict())
    openbsd_hw = OpenBSDHardware(module=module)

# Generated at 2022-06-13 01:09:22.560186
# Unit test for method populate of class OpenBSDHardware
def test_OpenBSDHardware_populate():
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )

    oh = OpenBSDHardware(module)
    facts = oh.populate()

    keys = [
        'devices',
        'memfree_mb',
        'memtotal_mb',
        'mounts',
        'processor',
        'processor_cores',
        'processor_count',
        'product_name',
        'product_serial',
        'product_uuid',
        'sysctl',
        'system_vendor',
        'uptime_seconds',
    ]
    for key in keys:
        assert key in facts


# Generated at 2022-06-13 01:09:29.153210
# Unit test for method get_memory_facts of class OpenBSDHardware
def test_OpenBSDHardware_get_memory_facts():
    from ansible.module_utils.facts.hardware import OpenBSDHardware
    from ansible.module_utils.facts.system.bsd import OpenBSDSystem
    from ansible.module_utils.facts.system.bsd import OpenBSDNetwork
    def fake_run_command(self, cmd, check_rc=True):
        if cmd == "/usr/bin/vmstat":
            return 0, "procs    memory       page                    disks    traps          cpu\nr b w    avm     fre  flt  re  pi  po  fr  sr wd0 fd0  int   sys   cs us sy id\n0 0 0  47512   28160   51   0   0   0   0   0   1   0  116    89   17  0  1 99", ""

# Generated at 2022-06-13 01:09:30.114456
# Unit test for constructor of class OpenBSDHardwareCollector
def test_OpenBSDHardwareCollector():
    OpenBSDHardwareCollector()



# Generated at 2022-06-13 01:09:35.839907
# Unit test for method get_uptime_facts of class OpenBSDHardware
def test_OpenBSDHardware_get_uptime_facts():
    hardware = OpenBSDHardware()

    mock_result = {
        'kern.boottime': '1535675470',
    }
    sysctl_mock = {
        'kern.boottime': '1535675470',
    }

    hardware.sysctl = sysctl_mock

    expected_result = {
        'uptime_seconds': int(time.time()) - 1535675470,
    }

    assert expected_result == hardware.get_uptime_facts()

# Generated at 2022-06-13 01:09:40.588945
# Unit test for constructor of class OpenBSDHardwareCollector
def test_OpenBSDHardwareCollector():
    inst_OpenBSDHardwareCollector = OpenBSDHardwareCollector()
    assert inst_OpenBSDHardwareCollector._fact_class == OpenBSDHardware
    assert inst_OpenBSDHardwareCollector._platform == 'OpenBSD'

# Generated at 2022-06-13 01:09:42.519595
# Unit test for constructor of class OpenBSDHardwareCollector
def test_OpenBSDHardwareCollector():
    o = OpenBSDHardwareCollector()
    assert o._platform == 'OpenBSD'
    assert o._fact_class == OpenBSDHardware

# Generated at 2022-06-13 01:09:51.176924
# Unit test for constructor of class OpenBSDHardwareCollector
def test_OpenBSDHardwareCollector():

    import sys
    import tempfile

    sys.path.insert(0, '..')
    from ansible.module_utils import basic
    from ansible.module_utils.facts import collector

    d = tempfile.mkdtemp()
    fh = open(d + '/class_OpenBSDHardwareCollector.txt', mode='wt')
    collector.collector = OpenBSDHardwareCollector
    dummy_module = basic.AnsibleModule(
        argument_spec = dict(
            gather_subset=dict(default=['!all'], type='list')
        )
    )
    fh.write(repr(collector.get_collector_facts(dummy_module)))
    fh.close()
    sys.path.pop(0)

# run above unit test

# Generated at 2022-06-13 01:10:00.797275
# Unit test for method get_uptime_facts of class OpenBSDHardware
def test_OpenBSDHardware_get_uptime_facts():
    # import module and class without a deprecation warning
    import ansible.module_utils.facts.hardware.openbsd as openbsd

    class TestHardware():
        # init a TestHardware object with a boottime
        def __init__(self, bt):
            self.sysctl = {
                'kern.boottime': bt,
            }

        # get the boottime from self.sysctl
        def run_command(self, cmd):
            if cmd == ['/sbin/sysctl', '-n', 'kern.boottime']:
                return (0, self.sysctl['kern.boottime'], '')

            return (0, '', '')

        # we fake the time with a variable
        def time(self):
            return self.current_time

    assert openbsd.OpenBSD

# Generated at 2022-06-13 01:10:04.866875
# Unit test for method get_uptime_facts of class OpenBSDHardware
def test_OpenBSDHardware_get_uptime_facts():
    # Prepare a mock module object
    module = Mock()

    # Prepare a mock sysctl command output
    module.run_command.return_value = (0, "1575399407", "")

    # Prepare a mock OpenBSDHardware instance
    hardware = OpenBSDHardware(module)

    # Get the uptime facts
    uptime_facts = hardware.get_uptime_facts()

    # Verify output of get_uptime_facts
    assert uptime_facts['uptime_seconds'] == int(time.time() - int("1575399407"))

# Generated at 2022-06-13 01:10:48.496502
# Unit test for method get_memory_facts of class OpenBSDHardware
def test_OpenBSDHardware_get_memory_facts():
    module = DummyModule()
    # DummyModule does not have to run as root
    OpenBSDHardware(module).get_mount_facts = DummyMethod(return_value=None)

    hardware = OpenBSDHardware(module)
    vmstat_output = " procs    memory       page                    disks    traps          cpu\n" \
                    " r b w    avm     fre  flt  re  pi  po  fr  sr wd0 fd0  int   sys   cs us sy id\n" \
                    " 0 0 0  47512   28160   51   0   0   0   0   0   1   0  116    89   17  0  1 99"
    hardware.module.run_command = DummyMethod(return_value=(0, vmstat_output, ""))
    memory_facts = hardware.get_memory

# Generated at 2022-06-13 01:10:52.821571
# Unit test for method get_memory_facts of class OpenBSDHardware
def test_OpenBSDHardware_get_memory_facts():
    module = OpenBSDHardware()
    module.sysctl = {'hw.usermem': '100000'}
    memory_facts = {'memfree_mb': 3, 'memtotal_mb': 100}
    assert module.get_memory_facts() == memory_facts

# Generated at 2022-06-13 01:11:03.334839
# Unit test for method get_uptime_facts of class OpenBSDHardware
def test_OpenBSDHardware_get_uptime_facts():
    import time
    import sys
    import textwrap
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.hardware.openbsd import OpenBSDHardware

    fake_sysctl = to_bytes(textwrap.dedent(u'''\
        hw.ncpuonline=2
        hw.usermem=2155846656
        hw.disknames=wd0,wd1
        hw.model=OpenBSD
        '''))

    module = mock.MagicMock()
    module.run_command.return_value = (0, fake_sysctl, b'')

    facts = OpenBSDHardware(module)
    uptime_facts = facts.get_uptime_facts()


# Generated at 2022-06-13 01:11:09.962831
# Unit test for method get_uptime_facts of class OpenBSDHardware
def test_OpenBSDHardware_get_uptime_facts():
    class TestModule():
        def get_bin_path(self, arg):
            return '/sbin/sysctl'

    instance = OpenBSDHardware()
    instance.module = TestModule()

    facts = instance.get_uptime_facts()
    assert 'uptime_seconds' in facts

    instance.uptime_seconds = 0
    facts = instance.get_uptime_facts()
    assert 'uptime_seconds' in facts

# Generated at 2022-06-13 01:11:18.269161
# Unit test for method get_uptime_facts of class OpenBSDHardware
def test_OpenBSDHardware_get_uptime_facts():
    class FakeModuleError(Exception):
        pass

    class FakeModule(object):
        def __init__(self, rc, out, err, timeout):
            self.rc = rc
            self.cmd = None
            self.out = out
            self.err = err
            self.timeout = timeout
            self.time_out = False

        def get_bin_path(self, *kwargs):
            return '/sbin/sysctl'


# Generated at 2022-06-13 01:11:21.241642
# Unit test for method get_device_facts of class OpenBSDHardware
def test_OpenBSDHardware_get_device_facts():
    hardware = OpenBSDHardware(dict(module=None, sysctl={'hw.disknames':'wd0,wd1'}))
    hardware.sysctl = {'hw.disknames': 'wd0,wd1'}
    device_facts = hardware.get_device_facts()
    assert device_facts == {'devices': ['wd0', 'wd1']}


# Generated at 2022-06-13 01:11:26.994738
# Unit test for method populate of class OpenBSDHardware
def test_OpenBSDHardware_populate():
    data = get_sysctl(object(), ['hw'])

    hardware = OpenBSDHardware(object())
    facts = hardware.populate(collected_facts=data)

    assert 'memtotal_mb' in facts
    assert 'memfree_mb' in facts
    assert 'swaptotal_mb' in facts
    assert 'swapfree_mb' in facts
    assert 'processor' in facts
    assert 'processor_cores' in facts
    assert 'processor_count' in facts
    assert 'mounts' in facts

# Generated at 2022-06-13 01:11:34.678318
# Unit test for method populate of class OpenBSDHardware
def test_OpenBSDHardware_populate():

    # Test for get_mount_facts()
    def get_mount_facts(self):
        return {'mounts': [{'mount': '/',
                            'device': '/dev/wd0a',
                            'fstype': 'ffs',
                            'options': 'rw',
                            'size_total': 7180224,
                            'size_available': 6767312,
                            'inodes_total': 61440,
                            'inodes_available': 58212}]}
    OpenBSDHardware.get_mount_facts = get_mount_facts

    # Test for get_memory_facts()

# Generated at 2022-06-13 01:11:46.119601
# Unit test for method get_dmi_facts of class OpenBSDHardware
def test_OpenBSDHardware_get_dmi_facts():
    fixtures = {'hw.product': 'SOMEPRODUCT',
                'hw.version': 'SOMEVERSION',
                'hw.uuid': 'SOME-UUID',
                'hw.serialno': 'SOMESERIAL',
                'hw.vendor': 'SOMEVENDOR'}
    hw = OpenBSDHardware(module=None, sysctl=fixtures)
    dmi_facts = hw.get_dmi_facts()
    assert dmi_facts == {'product_name': 'SOMEPRODUCT',
                         'product_version': 'SOMEVERSION',
                         'product_uuid': 'SOME-UUID',
                         'product_serial': 'SOMESERIAL',
                         'system_vendor': 'SOMEVENDOR'}

# Generated at 2022-06-13 01:11:46.722359
# Unit test for method get_processor_facts of class OpenBSDHardware
def test_OpenBSDHardware_get_processor_facts():
    pass

# Generated at 2022-06-13 01:13:10.469732
# Unit test for method populate of class OpenBSDHardware
def test_OpenBSDHardware_populate():
    hw = OpenBSDHardware(dict())
    assert 'memtotal_mb' in hw.populate()
    assert 'swapfree_mb' in hw.populate()

# Generated at 2022-06-13 01:13:15.345945
# Unit test for method get_uptime_facts of class OpenBSDHardware
def test_OpenBSDHardware_get_uptime_facts():
    # pylint: disable=W0212,C0103
    module = MockModule()
    module.run_command = Mock(return_value=(0, '1572963480', ''))

    hardware_collector = OpenBSDHardwareCollector(module=module)
    hardware = hardware_collector.collect()

    assert hardware.get_uptime_facts() == {'uptime_seconds': 1572963480}

# Generated at 2022-06-13 01:13:21.963136
# Unit test for method get_uptime_facts of class OpenBSDHardware
def test_OpenBSDHardware_get_uptime_facts():
    """
    Test the method get_uptime_facts of the class OpenBSDHardware.
    """
    # Boot time of the system
    boot_time = time.time()
    # Mock the module and all its modules
    module = AnsibleModule(argument_spec=dict())
    module.run_command = MagicMock(return_value=(0, boot_time, ''))

    # Get the facts
    hardware = OpenBSDHardware(module)
    facts = hardware.get_uptime_facts()
    # Check the facts
    assert 'uptime_seconds' in facts
    assert facts['uptime_seconds'] >= 0
    assert facts['uptime_seconds'] <= time.time() - boot_time

# Generated at 2022-06-13 01:13:27.220240
# Unit test for method populate of class OpenBSDHardware
def test_OpenBSDHardware_populate():
    module = AnsibleModule(argument_spec={})
    hardware = OpenBSDHardware(module)
    hardware.populate()
    hardware_facts = hardware.get_facts()
    assert hardware_facts['system_vendor'] == 'OpenBSD'
    assert hardware_facts['mounts']
    assert hardware_facts['memtotal_mb'] == 512

# Generated at 2022-06-13 01:13:28.867501
# Unit test for constructor of class OpenBSDHardwareCollector
def test_OpenBSDHardwareCollector():
   hardware = OpenBSDHardwareCollector()
   assert hardware.platform == 'OpenBSD'

# Generated at 2022-06-13 01:13:36.682565
# Unit test for method get_memory_facts of class OpenBSDHardware
def test_OpenBSDHardware_get_memory_facts():
    from ansible.module_utils.facts.utils import FactsParams
    OpenBSDHardware_object = OpenBSDHardware(module=FactsParams())
    sysctl_hw = {'hw.usermem': 641 * 1024 * 1024,
                 'hw.ncpuonline': 1,
                 'hw.model': 'Intel(R) Core(TM) i5-4250U CPU @ 1.30GHz'}
    OpenBSDHardware_object.sysctl = sysctl_hw

    facts = OpenBSDHardware_object.get_memory_facts()
    assert facts['memfree_mb'] == 28160 // 1024
    assert facts['memtotal_mb'] == 641
    assert facts['swapfree_mb'] == 69268 // 1024



# Generated at 2022-06-13 01:13:39.465465
# Unit test for method populate of class OpenBSDHardware
def test_OpenBSDHardware_populate():
    hardware_facts = OpenBSDHardware()
    hardware_facts.populate()
    assert hardware_facts.facts['uptime_seconds'] > 0
    assert hardware_facts.facts['memtotal_mb'] > 0
    assert hardware_facts.facts['swaptotal_mb'] > 0

# Generated at 2022-06-13 01:13:51.428584
# Unit test for method get_uptime_facts of class OpenBSDHardware
def test_OpenBSDHardware_get_uptime_facts():
    openbsd_hardware = OpenBSDHardware()
    openbsd_hardware.module = FakeModule()

    # Fake the kern.boottime sysctl to be one second less than the
    # current epoch time, so the uptime is one second. This is the
    # simplest case to test.
    current_epoch_time = int(time.time())
    expected_uptime = current_epoch_time - 1
    openbsd_hardware.sysctl = {'kern.boottime': str(expected_uptime)}

    openbsd_hardware_uptime_facts = openbsd_hardware.get_uptime_facts()
    assert openbsd_hardware_uptime_facts['uptime_seconds'] == 1


# Generated at 2022-06-13 01:13:52.640738
# Unit test for constructor of class OpenBSDHardwareCollector
def test_OpenBSDHardwareCollector():
    hw = OpenBSDHardwareCollector()
    assert hw # did it construct?

# Generated at 2022-06-13 01:14:01.568919
# Unit test for method get_uptime_facts of class OpenBSDHardware
def test_OpenBSDHardware_get_uptime_facts():
    from ansible.module_utils import basic
    from ansible.module_utils.facts import collector

    def run_command_mock(*args, **kwargs):
        if args[0] == ['/sbin/sysctl', '-n', 'kern.boottime']:
            return 0, '1518156910', ''
        else:
            raise AssertionError('Please mock run_command if you want to test OpenBSDHardware.get_uptime_facts')

    def get_bin_path_mock(*args, **kwargs):
        return '/sbin/sysctl'

    OpenBSDHardware.run_command = run_command_mock
    OpenBSDHardware.get_bin_path = get_bin_path_mock
