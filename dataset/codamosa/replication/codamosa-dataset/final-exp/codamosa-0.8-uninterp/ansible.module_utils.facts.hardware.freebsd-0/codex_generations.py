

# Generated at 2022-06-13 00:45:35.385858
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    harware_obj = FreeBSDHardware(module)
    collected_facts = {
        "kernel": "FreeBSD",
        "kernel_version": "16.1-RELEASE-p7"
    }
    return_value = harware_obj.populate(collected_facts=collected_facts)
    assert 'memfree_mb' in return_value
    assert 'memtotal_mb' in return_value
    assert 'swapfree_mb' in return_value
    assert 'swaptotal_mb' in return_value
    assert 'processor_cores' in return_value
    assert 'processor_count' in return_value
    assert 'uptime_seconds' in return_value
    assert 'devices' in return_value

# Unit

# Generated at 2022-06-13 00:45:38.237564
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    hardware = FreeBSDHardwareCollector()
    # pylint: disable=protected-access
    assert hardware._platform == 'FreeBSD'
    assert hardware._fact_class == FreeBSDHardware

# Generated at 2022-06-13 00:45:47.934768
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    test_input = '''vm.stats.vm.v_page_size: 4096
vm.stats.vm.v_page_count: 8408048
vm.stats.vm.v_free_count: 8336883'''
    test_expected = {'swaptotal_mb': None, 'memfree_mb': 8336883, 'memtotal_mb': 33319, 'swapfree_mb': None}

    test_object = FreeBSDHardware(dict())
    test_output = test_object.get_memory_facts()

    assert test_output == test_expected

# Generated at 2022-06-13 00:45:55.804563
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    """FreeBSDHardware - get_memory_facts() returns expected dictionary"""

    example_swapinfo = '''Device          1M-blocks     Used    Avail Capacity
/dev/ada0p3        314368        0   314368     0%'''
    example_vm_stats = '''vm.stats.vm.v_page_size: 4096
vm.stats.vm.v_page_count: 2292738
vm.stats.vm.v_free_count: 785505'''

    module = AnsibleModule(argument_spec={})
    module.run_command = Mock(return_value=(0, example_swapinfo, ""))
    module.get_bin_path = Mock(return_value="swapinfo")

    sysctl = Mock()

# Generated at 2022-06-13 00:46:03.844564
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    # First, try to populate facts by reading /var/run/dmesg.boot file
    test_obj = FreeBSDHardware()
    test_obj.DMESG_BOOT = '/path/to/test/dmesg.boot'
    get_file_content_calls = [0]

    def mocked_get_file_content(filename, *args, **kwargs):
        if filename == FreeBSDHardware.DMESG_BOOT:
            get_file_content_calls[0] += 1

# Generated at 2022-06-13 00:46:09.241949
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    module = AnsibleModuleMock({})

    hardware = FreeBSDHardware(module)

    hardware.module.exit_json = exit_json
    hardware.module.fail_json = fail_json

    hardware.populate()

    hardware.module.exit_json(changed=False)
    hardware.module.fail_json(changed=False)

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 00:46:13.385201
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    try:
        # Test class structure
        hardware_collector = FreeBSDHardwareCollector()
        hardware_collector.hardware_name
        hardware_collector.platform
        hardware_collector.collect()
        hardware_collector.get_all_hardware_collector()
        hardware_collector.get_hardware_collector()
    except AttributeError:
        fail("Some attributes are missing in class FreeBSDHardwareCollector")

    # Test constructor
    try:
        hw = FreeBSDHardwareCollector().collect()
    except Exception as e:
        fail("Failed to create FreeBSDHardwareCollector: %s" % e)
    if hw is not None:
        pass
    else:
        fail("Failed to create FreeBSDHardwareCollector")

# Generated at 2022-06-13 00:46:23.889140
# Unit test for method get_memory_facts of class FreeBSDHardware

# Generated at 2022-06-13 00:46:27.811517
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    facts_dict = {'uname': 'FreeBSD'}
    hardware = FreeBSDHardware(facts_dict)
    memory_facts = hardware.get_memory_facts()
    assert isinstance(memory_facts, dict)
    assert all(x in memory_facts for x in ['memtotal_mb', 'memfree_mb', 'swaptotal_mb', 'swapfree_mb'])



# Generated at 2022-06-13 00:46:37.412980
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    # Testing FreeBSDHardware._get_dmi_facts when executed on
    # FreeBSD using dmidecode
    test_obj = FreeBSDHardware()

# Generated at 2022-06-13 00:46:53.448229
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    facts = FreeBSDHardware(None).get_cpu_facts()
    assert facts['processor'] != []
    assert facts['processor_count'] != ''
    assert facts['processor_cores'] != ''



# Generated at 2022-06-13 00:46:57.597271
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    f = FreeBSDHardware(module=module)
    cpu_facts = f.get_cpu_facts()
    assert 2 == cpu_facts['processor_count']
    assert 2 == len(cpu_facts['processor'])

# Generated at 2022-06-13 00:47:04.320914
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():

    class ModuleMock:

        def get_bin_path(self, path):
            return '/bin/' + path

        def run_command(self, command):

            # Fake output of 'swapinfo' command
            if command.endswith('swapinfo -k'):
                out = 'Device          1M-blocks     Used    Avail Capacity\n/dev/ada0p3        314368        0   314368     0%'
                err = ''
                rc = 0
            # Fake output of 'sysctl vm.stats' command

# Generated at 2022-06-13 00:47:12.962380
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    module = MockAnsibleModule()
    mock_dmesg_boot = (
        "CPU:            Intel(R) Xeon(R) CPU E5-2670 0 @ 2.60GHz (2594.88-MHz K8-class CPU)\n"
        "Origin = \"GenuineIntel\"  Id = 0x306d4  Family = 6  Model = 3d  Stepping = 4\n"
        "Features=0xbfebfbff  Features2=0x20100  AMD Features=0x28100800  AMD Features2=0x1\n"
        "Logical CPUs per core: 2\n"
        "real memory  = 8589934592 (8192 MB)\n"
        "avail memory = 8285945856 (7921 MB)\n"
    )

# Generated at 2022-06-13 00:47:20.234540
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    # Getting the same facts from a FreeBSD machine
    module = AnsibleModule(argument_spec={'gather_subset': dict(type='list', default=['!all'])})
    set_module_args(dict(gather_subset=['all']))
    freebsd_hw = FreeBSDHardware(module)
    freebsd_hw.populate()
    freebsd_facts = freebsd_hw.facts

    # Creating a object of class FreeBSDHardware and testing the method get_memory_facts
    module = AnsibleModule(argument_spec={'gather_subset': dict(type='list', default=['!all'])})
    set_module_args(dict(gather_subset=['all']))
    freebsd_hw = FreeBSDHardware(module)

# Generated at 2022-06-13 00:47:31.036030
# Unit test for method get_dmi_facts of class FreeBSDHardware

# Generated at 2022-06-13 00:47:40.271948
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():

    class FakeModule(object):
        def __init__(self, params=None):
            self.params = params
            self.run_command_results = {
                ('sysctl -n hw.ncpu'): ('0', '', 0),
                ('sysctl vm.stats'): ('', '', 0),
                ('swapinfo -k'): ('', '', 0),
            }

        def run_command(self, command, check_rc=True, encoding=None):
            return self.run_command_results[tuple(command)]

        def get_bin_path(self, executable):
            return '/sbin/' + executable

    fake_module = FakeModule()
    fhw = FreeBSDHardware(fake_module)


# Generated at 2022-06-13 00:47:53.369180
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts import gather_subset
    from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.utils import get_file_content
    from collections import namedtuple
    from ansible.module_utils import basic
    import json

    FakeModule = namedtuple('FakeModule', ('params', 'run_command'))
    FakeDmesg = namedtuple('FakeDmesg', ('dmesg'))
    FakeSysctl = namedtuple('FakeSysctl', ('sysctl'))

    # dmesg.boot exists and readable => dmesg.boot content is used
    dmesg = FakeD

# Generated at 2022-06-13 00:48:02.119393
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    # Create an instance
    freebsd_hardware = FreeBSDHardware()

    # Create a sysctl mock
    sysctl_mock = "/usr/sbin/sysctl"

    # Create a swapinfo mock
    swapinfo_mock = "/sbin/swapinfo"

    # Create a dmidecode mock
    dmidecode_mock = "/usr/sbin/dmidecode"

    # Define memory_facts dict
    memory_facts = {
            "memtotal_mb": "979",
            "memfree_mb": "786",
            "swaptotal_mb": 0,
            "swapfree_mb": 0
    }

    # Call method get_memory_facts and compare with expected dict

# Generated at 2022-06-13 00:48:10.297864
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    class Module:

        def __init__(self):
            self.run_command_calls = 0
            self.get_bin_path_calls = 0

        def get_bin_path(self, name):
            self.get_bin_path_calls += 1
            return {
                'sysctl': '/sbin/sysctl',
            }[name]

        def run_command(self, args, encoding=None):
            self.run_command_calls += 1

            if self.run_command_calls == 1:
                return 1, '', ''
            elif self.run_command_calls == 2:
                return 0, 'kern.boottime: { 10, 512345678 } Sun Feb  3 11:17:35 2019\n', ''

# Generated at 2022-06-13 00:48:32.862040
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    freebsd_hardware = FreeBSDHardware()
    cpu_facts = freebsd_hardware.get_cpu_facts()
    memory_facts = freebsd_hardware.get_memory_facts()
    uptime_facts = freebsd_hardware.get_uptime_facts()
    dmi_facts = freebsd_hardware.get_dmi_facts()
    device_facts = freebsd_hardware.get_device_facts()
    mount_facts = freebsd_hardware.get_mount_facts()
    freebsd_hardware_facts = freebsd_hardware.populate(None)
    freebsd_hardware_facts.update(cpu_facts)
    freebsd_hardware_facts.update(memory_facts)

# Generated at 2022-06-13 00:48:42.961897
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    sample_out_swap_total = 'Device          1M-blocks     Used    Avail Capacity\n/dev/ada0p3        314368        0   314368     0%\n'
    sample_out_swap_total_bsd = b'Device          1M-blocks     Used    Avail Capacity\n/dev/ada0p3        314368        0   314368     0%\n'
    sample_out_swap_none = ''
    sample_out_mem_stats = 'hw.pagesize: 4096\nhw.physmem: 149767168\nhw.usermem: 140140544\n'
    test_module = type('test_module', (), {'run_command': lambda *args, **kwargs: (0, sample_out_swap_total_bsd, '')})
    test

# Generated at 2022-06-13 00:48:45.850209
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    h = FreeBSDHardware()
    facts = {'ansible_system': 'FreeBSD'}
    h.populate(facts)
    dmi_facts = h.get_dmi_facts()
    assert dmi_facts['system_vendor'] != 'NA'
    assert dmi_facts['product_name'] != 'NA'

# Generated at 2022-06-13 00:48:52.117984
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware
    fh = FreeBSDHardware(dict())
    fh.module = MockModule()
    assert type(fh.populate()) is dict


# Generated at 2022-06-13 00:49:03.287819
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    # Test when sysctl is not there
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    module.params['gather_timeout'] = 0
    fbsd_hw_collector = FreeBSDHardwareCollector(module=module)
    mem_fact = fbsd_hw_collector.collect()['memory']
    assert mem_fact['swaptotal_mb'] == -1
    assert mem_fact['swapfree_mb'] == -1

    # Test with sysctl but no swap
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    module.params['gather_timeout'] = 0
    fbsd_hw_collector = FreeBSDHardwareCollector(module=module)

# Generated at 2022-06-13 00:49:12.073322
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    class FreeBSDSysModule:
        def get_bin_path(self, name):
            return name

    class FreeBSDSysModuleRunCommand:
        def run_command(self, cmd, encoding=None):
            ''' fake the command output
            '''
            if cmd[-1] == 'b':
                rc = 0

# Generated at 2022-06-13 00:49:20.595390
# Unit test for method populate of class FreeBSDHardware

# Generated at 2022-06-13 00:49:25.557790
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    # Test to get dmi facts by FreeBSDHardware().get_dmi_facts()
    module = AnsibleModule(argument_spec={})
    hardware_inst = FreeBSDHardware(module)

    dmi_facts = hardware_inst.get_dmi_facts()
    assert dmi_facts is not None



# Generated at 2022-06-13 00:49:37.392642
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    # load test facts
    freebsd_facts_file_name = os.path.join(os.path.dirname(__file__), 'unit', 'modules', 'hardware', 'FreeBSD_hardware_dmidecode_facts.json')
    with open(freebsd_facts_file_name) as test_facts:
        test_facts_dict = json.load(test_facts)

    # initialize instance of class FreeBSDHardware
    module = type('TestModule', (object,), {})()
    module.run_command = run_command_stub
    freebsd_hardware = FreeBSDHardware(module)

    dmi_facts = freebsd_hardware.get_dmi_facts()

# Generated at 2022-06-13 00:49:43.642026
# Unit test for method get_cpu_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_cpu_facts():
    # create class instance
    harware = FreeBSDHardware(None)
    cpu_facts = harware.get_cpu_facts()

    # expected output
    expected_cpu_facts = {
        'processor': ['Intel(R) Core(TM) i5-4210M CPU @ 2.60GHz'],
        'processor_cores': '2',
        'processor_count': '2'
    }

    # assert if test output and expected output matches
    assert(cpu_facts == expected_cpu_facts)



# Generated at 2022-06-13 00:50:09.069315
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    pass


# Generated at 2022-06-13 00:50:13.490025
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    # Initializing the class
    o_hardware = FreeBSDHardware(None)
    o_hardware.module.get_bin_path = lambda x: x
    o_hardware.module.run_command = lambda x, encoding=None: (0, "vm.stats.vm.v_page_size: 2048\nvm.stats.vm.v_page_count: 131072\nvm.stats.vm.v_free_count: 59066", '')

    # Initializing data to be used by the test
    facts = {}

    # Calling the method under test
    o_hardware.get_memory_facts(facts)

    # Asserting the results
    assert facts['memtotal_mb'] == 64
    assert facts['memfree_mb'] == 28


# Generated at 2022-06-13 00:50:17.935187
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    from ansible.module_utils import basic
    module = basic.AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=False
    )

    if module.get_bin_path('dmidecode'):
        fhw = FreeBSDHardware(module)
        dmi_facts = fhw.get_dmi_facts()
        assert isinstance(dmi_facts, dict)
        bkeys = ['system_vendor', 'system_serial', 'product_name', 'product_version',
                 'product_serial', 'product_uuid', 'board_vendor', 'board_name', 'board_version',
                 'chassis_vendor', 'form_factor']
        for key in bkeys:
            assert key in dmi_facts
        # Verify that the attribute is not added if there is no dm

# Generated at 2022-06-13 00:50:18.391594
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    FreeBSDHardwareCollector()

# Generated at 2022-06-13 00:50:21.562831
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    from ansible.module_utils.facts import collector

    x = collector.get_platform_fact_collector('FreeBSD')
    assert x is not None
    assert isinstance(x, FreeBSDHardwareCollector)
    assert x.platform == 'FreeBSD'
    assert x._platform == 'FreeBSD'

# Generated at 2022-06-13 00:50:25.484401
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    module = AnsibleModule(argument_spec={})
    hardware = FreeBSDHardware(module)
    memory_facts = hardware.get_memory_facts()
    assert memory_facts['memtotal_mb'] > 0
    assert memory_facts['memfree_mb'] > 0
    assert memory_facts['swaptotal_mb'] > 0
    assert memory_facts['swapfree_mb'] > 0


# Generated at 2022-06-13 00:50:30.107553
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    module = AnsibleModule(argument_spec={})
    gather_subset = ['all']
    gather_timeout = 10
    hardware = FreeBSDHardware(module=module)
    hardware.populate(gather_subset, gather_timeout)
    assert hardware.facts['processor_count'] == 1
    assert 'memtotal_mb' in hardware.facts

# Generated at 2022-06-13 00:50:40.555363
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    module = AnsibleModule(
        argument_spec=dict(),
    )

    hardware_collector = FreeBSDHardwareCollector(module=module)
    hardware_collector.collect()
    facts = hardware_collector.get_facts()

    assert facts['devices']
    assert facts['devices']['ada0']
    assert facts['devices']['ada0'][0]
    assert facts['devices']['ada0'][0].startswith('ada0s')
    assert facts['memtotal_mb']
    assert 'memfree_mb' in facts
    assert 'swaptotal_mb' in facts
    assert 'swapfree_mb' in facts
    assert 'processor' in facts
    assert facts['processor'][0]
    assert 'processor_cores' in facts
    assert 'processor_count' in facts
   

# Generated at 2022-06-13 00:50:52.594111
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    import unittest

    class MyModule(object):
        def __init__(self):
            self.params = {}

        def run_command(self, command, encoding=None, check_rc=True, check_stderr=True, check_start=True):
            if command == ['/sbin/sysctl', '-b', 'kern.boottime']:
                return 0, '1542245977.154225', ''
            else:
                self.fail(command)

        def fail(self, msg):
            raise Exception(msg)

    class MyTestCase(unittest.TestCase):
        def test_get_uptime_facts(self):
            mymodule = MyModule()
            myfacts = FreeBSDHardware(mymodule)
            current_time = int(time.time())
            uptime_facts

# Generated at 2022-06-13 00:50:59.252514
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    """
    Unit test for method get_uptime_facts of class FreeBSDHardware

    """
    from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware

    fake_module = FakeModule()
    hardware = FreeBSDHardware(fake_module)
    uptime_facts = hardware.get_uptime_facts()

    print("uptime_facts: %s" % uptime_facts)


if __name__ == "__main__":
    test_FreeBSDHardware_get_uptime_facts()

# Generated at 2022-06-13 00:52:15.272127
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware
    import os
    import pytest

    # get values from dmidecode
    def test_dmidecode():
        dmidecode = FreeBSDHardware.DMI_DICT.keys()
        dmidecode_bin = FreeBSDHardware.module.get_bin_path('dmidecode')
        assert dmidecode_bin is not None
        result = {}

        for key in dmidecode:
            path = "%s -s %s" % (dmidecode_bin, FreeBSDHardware.DMI_DICT[key])
            (rc, out, err) = FreeBSDHardware.module.run_command(path)
            out = ''.join([line for line in out.splitlines() if not line.startswith('#')])  # Strip

# Generated at 2022-06-13 00:52:20.618246
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():
    module = AnsibleModuleMock({'command': '/usr/sbin/dmidecode'})
    hardware = FreeBSDHardware(module=module)
    facts = hardware.get_dmi_facts()
    for key in ['system_vendor', 'product_uuid', 'product_serial',
                'product_version', 'product_name']:
        if key not in facts.keys():
            module.fail_json(msg="The key %s is missing in the facts dict!" % key)



# Generated at 2022-06-13 00:52:25.087581
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    module = AnsibleModule(argument_spec={})
    hardware = FreeBSDHardware(module)
    hardware.populate()
    for f in ['processor', 'processor_cores', 'processor_count',
              'memtotal_mb', 'memfree_mb',
              'uptime_seconds', 'devices', 'mounts']:
        assert f in hardware.facts

# Generated at 2022-06-13 00:52:35.613879
# Unit test for method get_memory_facts of class FreeBSDHardware

# Generated at 2022-06-13 00:52:44.356550
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    Hardware._get_mount_facts = get_mount_facts
    def get_file_content_mock_data():
        return """
devfs                           1  1  0   100%    /dev
/dev/gpt/swapfs                 0     0   100%    /tmp
/dev/gpt/rootfs                 0     0   100%    /
/dev/gpt/usrfs                  0     0   100%    /usr
/dev/gpt/varfs                  0     0   100%    /var
/dev/gpt/varfs-local            0     0   100%    /var/local
/dev/gpt/varfs-tmp              0     0   100%    /var/tmp
/dev/gpt/varfs-obj              0     0   100%    /var/obj
"""

# Generated at 2022-06-13 00:52:51.204782
# Unit test for method populate of class FreeBSDHardware
def test_FreeBSDHardware_populate():
    module = AnsibleModule(argument_spec={'gather_subset': dict(default=['all'])})
    if module.params['gather_subset'] == ['all']:
        hardware = FreeBSDHardware(module)
        result = hardware.populate()
        assert result['devices']
        assert result['processor_cores']
        assert result['processor_count']
        assert result['processor']
        assert result['memtotal_mb']
        assert result['memfree_mb']
        assert result['swaptotal_mb']
        assert result['swapfree_mb']
        assert result['mounts']
        assert result['uptime_seconds']
        assert result['bios_date']
        assert result['bios_vendor']
        assert result['bios_version']
        assert result['board_asset_tag']

# Generated at 2022-06-13 00:52:53.184713
# Unit test for constructor of class FreeBSDHardwareCollector
def test_FreeBSDHardwareCollector():
    assert FreeBSDHardwareCollector.collect()

# Generated at 2022-06-13 00:53:02.905119
# Unit test for method get_dmi_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_dmi_facts():

    class AnsibleModuleMock(object):
        command = ''
        rc = 0
        bin_path = 'bin/'

# Generated at 2022-06-13 00:53:10.917308
# Unit test for method get_memory_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_memory_facts():
    m = FreeBSDHardware()

    import textwrap
    # Create a fake dmesg_boot file

# Generated at 2022-06-13 00:53:13.230963
# Unit test for method get_uptime_facts of class FreeBSDHardware
def test_FreeBSDHardware_get_uptime_facts():
    from ansible.module_utils.facts import TestModule
    test_module = TestModule({})
    hardware = FreeBSDHardware(test_module)
    uptime_facts = hardware.get_uptime_facts()

    assert uptime_facts.get('uptime_seconds')