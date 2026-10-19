

# Generated at 2022-06-13 00:34:58.001232
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    from ansible.module_utils.facts.hardware import Hardware
    from ansible.module_utils.facts.sysctl import SysctlCollector
    from ansible.module_utils.facts import FactManager

    sysctl_mock = SysctlCollector(module=None, params=dict())
    sysctl_mock.sysctl = {
        "hw.ncpu": 2,
        "hw.physicalcpu": 4,
        "hw.activecpu": 4,
        "hw.logicalcpu": 8,
        "machdep.cpu.brand_string": "Intel(R)"
    }

    fact_manager = FactManager()
    fact_manager.collectors.append(sysctl_mock)
    hardware_facts = Hardware(module=None, fact_manager=fact_manager)

    cpu_facts = hardware_

# Generated at 2022-06-13 00:35:08.041382
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    from ansible.module_utils.six import PY3
    from ansible.module_utils.basic import AnsibleModule

    if PY3:
        def bytes_to_str(b):
            return b.decode('utf-8')
    else:
        def bytes_to_str(b):
            return b

    def module_exit(changed=False):
        module.exit_json(changed=changed)

    def get_bin_path_side_effect(*args, **kwargs):
        return '/usr/bin/' + args[0]

    darwin_hardware = DarwinHardware(AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    ))


# Generated at 2022-06-13 00:35:18.437580
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    mock_module = MagicMock()
    mock_module.run_command.return_value = (0, 'Total Number Of Cores: 4', '')
    mock_sysctl = {
        'machdep.cpu.brand_string': 'Intel(R) Core(TM) i7-3720QM CPU @ 2.60GHz',
        'machdep.cpu.core_count': 4
    }
    mock_hardware = DarwinHardware(mock_module)
    mock_hardware.sysctl = mock_sysctl
    mock_hardware.get_system_profile = MagicMock(return_value={'Processor Name': 'Intel Core i7',
                                                               'Processor Speed': '2.6 GHz'})
    cpu_facts = mock_hardware.get_cpu_facts()
    assert cpu_facts

# Generated at 2022-06-13 00:35:22.475264
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    module = None  # Can be passed to DarwinHardware
    hardware = DarwinHardware(module)
    uptime_facts = hardware.get_uptime_facts()
    assert isinstance(uptime_facts, dict)
    assert 'uptime_seconds' in uptime_facts

# Generated at 2022-06-13 00:35:31.758494
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    import module_utils.facts.hardware.darwin
    # Define module parameters
    params = {
        'run_command_environ_update': {
            'PATH': ['/usr/bin'],
        },
    }
    # Define module class
    module_class = type('Module', (), {})
    module = module_class()
    # Define module run_command function
    def run_command(self, cmd, encoding=None):
        return (0, 'hw.model: Macmini6,2\n', '')
    module.run_command = run_command
    module.params = params

    # init DarwinHardware class
    facts_module = module_utils.facts.hardware.darwin.DarwinHardware(module)
    # execute tested method
    result = facts_module.get_mac_facts()

# Generated at 2022-06-13 00:35:32.647047
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    a = DarwinHardwareCollector()
    print(a)

# Generated at 2022-06-13 00:35:42.034258
# Unit test for method get_memory_facts of class DarwinHardware

# Generated at 2022-06-13 00:35:42.525032
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    pass

# Generated at 2022-06-13 00:35:48.744118
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    module = AnsibleModule(
        argument_spec = dict()
    )

    Hardware = DarwinHardware(module=module)

    facts = Hardware.populate()

    for key in ['memtotal_mb', 'memfree_mb', 'model', 'osversion', 'osrevision', 'uptime_seconds']:
        assert key in facts


# Generated at 2022-06-13 00:35:59.729105
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    module = type('', (), {})()
    module.run_command = lambda *args, **kwargs: (0, """\
Mach Virtual Memory Statistics: (page size of 4096 bytes)
Pages free:                          632359.
Pages active:                       11196476.
Pages inactive:                      5660197.
Pages speculative:                      7919.
Pages throttled:                           0.
Pages wired down:                     136286.
Pages purgeable:                         667.
""", '')
    class_instance = DarwinHardware(module)
    result = class_instance.get_memory_facts()
    assert result == {
        'memfree_mb': 632359 * 4096 // 1024 // 1024,
        'memtotal_mb': (11196476 + 5660197 + 136286) * 4096 // 1024 // 1024,
    }

# Generated at 2022-06-13 00:36:19.180201
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    from ansible.module_utils.facts.hardware.darwin import vm_stat_out_inactive_wired

    dh = DarwinHardware(dict(), dict())
    dh.get_memory_facts()

    # Test with vm_stat output
    dh = DarwinHardware(dict(), dict())
    old_run_command = dh.module.run_command
    dh.module.run_command = lambda command: (0, vm_stat_out_inactive_wired, None)

    # Verify we get expected output
    expected_result = {
        'memtotal_mb': 8192,
        'memfree_mb': 322,
    }

    result = dh.get_memory_facts()
    assert result == expected_result

    # Restore original run_command

# Generated at 2022-06-13 00:36:27.874650
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():

    # Fake class with a "run_command" method that returns the output we want.
    class FakeModule:
        def run_command(self, cmd, encoding=None):
            if cmd == ['/usr/sbin/sysctl', '-b', 'kern.boottime']:
                return (0, b' 1486305170\n', '')
            else:
                raise AssertionError("unexpected command: %s" % cmd)

        def get_bin_path(self, name):
            return '/usr/sbin/' + name

    module = FakeModule()
    hardware = DarwinHardware(module)
    assert hardware.get_uptime_facts() == {'uptime_seconds': 5}

# Generated at 2022-06-13 00:36:31.959132
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    module = FakeModule({'kern.boottime': '{ sec = 1457503399, usec = 643016 }'})
    hardware = DarwinHardware(module)
    expected_result = {'uptime_seconds': int(time.time()) - 1457503399}
    assert hardware.get_uptime_facts() == expected_result

# Generated at 2022-06-13 00:36:40.180716
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    import os


# Generated at 2022-06-13 00:36:52.611384
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    '''
    Test whether the get_cpu_facts method is working correctly.
    '''

    # Intel Mac
    module_mock = MagicMock()
    hardware = DarwinHardware(module_mock)
    hardware.sysctl = {
        'machdep.cpu.brand_string': 'Intel(R) Xeon(R) CPU E5-2670 0 @ 2.60GHz',
        'machdep.cpu.core_count': 1
    }
    cpu_facts = hardware.get_cpu_facts()
    assert cpu_facts['processor'] == 'Intel(R) Xeon(R) CPU E5-2670 0 @ 2.60GHz'
    assert cpu_facts['processor_cores'] == 1
    assert 'processor_vcpus' not in cpu_facts

    # Intel Mac (multiple cores)
    hardware.sys

# Generated at 2022-06-13 00:37:03.281060
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    out = {'logicalcpu': 8,
           'physicalcpu': 4,
           'physicalcpu_max': 4,
           'core_count': 8,
           'machdep.cpu.brand_string': 'Intel(R) Core(TM) i7-2635QM CPU @ 2.00GHz'}
    class MockModule():
        def run_command(self, cmd, encoding=None):
            return 0, out, ''
    class MockFactCollector():
        def __init__(self):
            self.facts = {
                'processor_cores': 4,
                'processor_vcpus': 8,
                'processor': 'Intel(R) Core(TM) i7-2635QM CPU @ 2.00GHz',
            }
    hw = DarwinHardware(MockModule(), MockFactCollector())
   

# Generated at 2022-06-13 00:37:13.269194
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    # Set up a test object
    class Options:
        def __init__(self, value=None):
            self.bin = None
            self.check_rc = None
            self.executable = None
            self.shell = None
            self.value = value

    class Params:
        def __init__(self, ansible_check_mode=None, ansible_debug=None, utp=None):
            self.ansible_check_mode = ansible_check_mode
            self.ansible_debug = ansible_debug
            self.ansible_verbosity = None
            self.utp = utp

    class AnsibleModule:
        def __init__(self, params=None):
            self.params = params

        def get_bin_path(self, path, required=False):
            return path

       

# Generated at 2022-06-13 00:37:16.888850
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    module = AnsibleModule(argument_spec={})
    hardware_collector = DarwinHardwareCollector(module=module)
    hardware_collector.populate()
    assert hardware_collector._facts['processor_cores'] == hardware_collector._facts['processor_vcpus']

# Generated at 2022-06-13 00:37:18.935240
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    darwin_hardware_collector = DarwinHardwareCollector()
    assert darwin_hardware_collector._fact_class == DarwinHardware

# Generated at 2022-06-13 00:37:26.016068
# Unit test for method get_memory_facts of class DarwinHardware

# Generated at 2022-06-13 00:37:48.555549
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )

    fake_sysctl = {
        'machdep.cpu.brand_string': 'Intel(R) Xeon(R) CPU E5-2698 v3 @ 2.30GHz',
        'machdep.cpu.core_count': '16'
    }
    hardware = DarwinHardware(module=module, sysctl=fake_sysctl)
    cpu_facts = hardware.get_cpu_facts()

    assert cpu_facts['processor_cores'] == '16'
    assert cpu_facts['processor'] == 'Intel(R) Xeon(R) CPU E5-2698 v3 @ 2.30GHz'



# Generated at 2022-06-13 00:37:57.421811
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    module = type('TestModule', (object, ), {
        'run_command': lambda *args, **kwargs: (0, struct.pack('@L', 1467694545) if args[1] == '-b' and args[2] == 'kern.boottime' else '', '')
    })

    fact_class = type('DarwinHardwareTest', (DarwinHardware, ), {
        'module': module,
        'get_mac_facts': lambda *args, **kwargs: {}
    })

    uptime_facts = fact_class.get_uptime_facts()
    assert uptime_facts == {'uptime_seconds': 1467694545}

# Generated at 2022-06-13 00:38:08.094144
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    args = dict(
        module=dict(
            run_command=dict(
                return_value=(0, 'brand_string: Intel(R) Core(TM) i5-4570 CPU @ 3.20GHz', '')
            )
        )
    )

    class fake_DarwinHardware(DarwinHardware):
        def __init__(self):
            self.sysctl = {
                'machdep.cpu.brand_string': 'Intel(R) Core(TM) i5-4570 CPU @ 3.20GHz',
                'machdep.cpu.core_count': 4
            }

    hardware_collector = fake_DarwinHardware()
    test_DarwinHardware_get_cpu_facts.facts = hardware_collector.get_cpu_facts()

# Generated at 2022-06-13 00:38:12.917110
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    # Test case 1: vm_stat command returns normal data
    module = AnsibleModule(argument_spec=dict())
    set_module_args(module)
    hardware = DarwinHardware(module)
    hardware.module.run_command = MagicMock(return_value=(0, VM_STAT_OUT_MEM_NORMAL, ''))
    memory_facts = hardware.get_memory_facts()
    assert memory_facts == EXP_MEM_NORMAL

    # Test case 3: vm_stat command returns special data
    print(VM_STAT_OUT_MEM_SPECIAL)
    hardware.module.run_command = MagicMock(return_value=(0, VM_STAT_OUT_MEM_SPECIAL, ''))
    memory_facts = hardware.get_memory_facts()
    assert memory_facts == EXP_MEM_SPEC

# Generated at 2022-06-13 00:38:24.346809
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    import pytest

    MacFacts = DarwinHardware()

    with pytest.raises(ValueError):
        MacFacts.get_cpu_facts()

    MacFacts.sysctl = {
        'hw.logicalcpu': '4',
        'hw.physicalcpu': '2',
        'machdep.cpu.core_count': '4',
        'machdep.cpu.brand_string': 'Intel(R) Core(TM) i7-3615QM CPU @ 2.30GHz'
    }

    cpu_facts = MacFacts.get_cpu_facts()

# Generated at 2022-06-13 00:38:35.427539
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    mod = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default='!all', type='list')
        ),
        supports_check_mode=True,
    )

    if hasattr(mod.params, 'gather_subset'):
        mod.params['gather_subset'] = ['all']

    hardware = DarwinHardware(module=mod)
    output = hardware.populate()

    assert 'model' in output
    assert 'processor_cores' in output
    assert 'processor' in output
    assert 'memtotal_mb' in output
    assert 'memfree_mb' in output
    assert 'uptime_seconds' in output
    assert 'processor_vcpus' in output

# Generated at 2022-06-13 00:38:43.369974
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    import ansible.module_utils.facts.hardware.darwin as module
    module_args = dict()
    module_args['ansible_facts'] = dict()
    module_args['ansible_facts']['ansible_system'] = 'darwin'
    module_args['ansible_facts']['ansible_architecture'] = 'x86_64'
    module_args['ansible_facts']['ansible_distribution'] = 'mac_os_x'
    module_args['ansible_facts']['ansible_distribution_version'] = '10.12.5'
    module_args['ansible_facts']['ansible_kernel'] = 'Darwin'
    module_args['ansible_facts']['ansible_system_vendor'] = 'Apple Inc.'
    module_

# Generated at 2022-06-13 00:38:49.069224
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    module = AnsibleModule(argument_spec={})
    module.params = {}
    mh = DarwinHardware(module)
    mh.get_mac_facts = lambda: {
        'osversion': '15.3.0',
        'osrevision': '15D21',
        'model': 'MacBookAir7,2',
    }
    facts = mh.populate()

    assert facts['osversion'] == '15.3.0'
    assert facts['osrevision'] == '15D21'
    assert facts['model'] == 'MacBookAir7,2'



# Generated at 2022-06-13 00:38:59.724679
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    import os
    import sys
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.six import iteritems

    # Create a fake AnsibleModule
    class FakeAnsibleModule:
        def __init__(self, **kwargs):
            self.params = ImmutableDict()
            self.params.update(kwargs)

        def run_command(self, args, encoding=None):
            out = sys.modules[__name__].test_out
            rc = 0
            err = ''
            return rc, out, err

    # Use the fake AnsibleModule
    ansible_facts.system = 'Darwin'
    ansible_facts.module = FakeAnsibleModule()

    # Create a

# Generated at 2022-06-13 00:39:08.726342
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    hardware_facts = DarwinHardware().populate()
    # check if osrevision and model are set
    assert hardware_facts['osrevision']
    assert hardware_facts['model']
    # check if processor_cores and processor model are set
    assert hardware_facts['processor_cores'] > 0
    assert hardware_facts['processor']
    # check if uptime_seconds is set
    assert hardware_facts['uptime_seconds']
    # check if memtotal_mb and memfree_mb are set
    assert hardware_facts['memtotal_mb']
    assert hardware_facts['memfree_mb']

# Generated at 2022-06-13 00:39:52.200575
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    hardware = DarwinHardware({})
    hardware.sysctl = get_sysctl({}, ['hw', 'machdep', 'kern'])
    mac_facts = hardware.get_mac_facts()
    assert mac_facts['osversion'] == '16.7.0'
    assert mac_facts['osrevision'] == '201707091617'
    assert mac_facts['model'] == 'MacBookPro10,2'


# Generated at 2022-06-13 00:40:02.608961
# Unit test for method get_uptime_facts of class DarwinHardware
def test_DarwinHardware_get_uptime_facts():
    class Module(object):
        class RunCommand(object):
            def __init__(self, out, rc=0):
                self.out = out
                self.rc = rc

            def __call__(self, *args, **kwargs):
                return self.rc, self.out, ''

        def __init__(self):
            self.run_command = self.RunCommand
            self.get_bin_path = lambda x: 'sysctl'

    module = Module()

    # Pretend that we are running on macOS 10.14.1 (18B75)
    #
    # $ sysctl kern.boottime
    # kern.boottime: { sec = 0x59c8db99, usec = 0x2d7b } Thu Jul 26 13:36:41 2018

    dh = DarwinHardware(module)



# Generated at 2022-06-13 00:40:09.949175
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    from ansible.module_utils.facts import FactCollector

    # Instantiate DarwinHardware class
    dh = DarwinHardware()

    # Create a dictionary containing the output of sysctl hw.model
    sysctl_hw_model = ['hw.model: ', 'i386']

    # Create a dictionary containing the output of sysctl machdep.cpu.brand_string
    sysctl_machdep_cpu_brand_string = {'machdep.cpu.brand_string': 'Intel(R) Core(TM) i5-2520M CPU @ 2.50GHz'}

    # Create a dictionary containing the output of sysctl hw.physicalcpu
    sysctl_hw_physicalcpu = {'hw.physicalcpu': 2}

    # Create a dictionary containing the output of sysctl hw.physicalcpu

# Generated at 2022-06-13 00:40:12.294107
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    darwin_collector = DarwinHardwareCollector()
    assert darwin_collector
    assert darwin_collector.platform == 'Darwin'

# Generated at 2022-06-13 00:40:13.161888
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    assert DarwinHardwareCollector is not None

# Generated at 2022-06-13 00:40:20.082856
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    from ansible.module_utils.facts.hardware.darwin import DarwinHardware
    hardware_object = DarwinHardware()

    ret = hardware_object.populate()
    assert ret['model'] == "MacBookPro8,1", "Error - model fact is not correct."
    assert ret['osversion'] == 'Darwin Kernel Version 16.7.0', "Error - osversion fact is not correct."
    assert ret['osrevision'] == 'Darwin Kernel Version 16.7.0', "Error - osrevision fact is not correct."
    assert ret['processor'] == '2.2 GHz Intel Core i7', "Error - processor fact is not correct."
    assert ret['processor_cores'] == '4', "Error - processor_cores fact is not correct."

# Generated at 2022-06-13 00:40:30.566212
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    class ModuleMock(object):
        def __init__(self):
            self._run_command_rc = 0

# Generated at 2022-06-13 00:40:40.117695
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    fake_ansible_module = FakeAnsibleModule()
    darwin_hardware = DarwinHardware(fake_ansible_module)
    darwin_hardware_facts = darwin_hardware.populate()
    assert 'osversion' in darwin_hardware_facts
    assert 'osrevision' in darwin_hardware_facts
    assert 'uptime_seconds' in darwin_hardware_facts
    assert 'memtotal_mb' in darwin_hardware_facts
    assert 'memfree_mb' in darwin_hardware_facts
    assert 'processor' in darwin_hardware_facts


# Generated at 2022-06-13 00:40:50.822294
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    module = AnsibleModuleMock()
    darwin = DarwinHardware(module)
    # If the vm_stat command is not found, the function should just return
    # an empty dict.
    darwin.get_bin_path = lambda x: None
    assert darwin.get_memory_facts() == {}

    # If the vm_stat command was found, the function should return a dict
    # with memory values.
    darwin.get_bin_path = lambda x: './vm_stat'


# Generated at 2022-06-13 00:40:58.971131
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    # Simulate a module with a non-zero return code value from command vm_stat
    module = FakeModule(result={"rc": 1})
    darwin_hardware = DarwinHardware(module)
    free_memory_bytes = darwin_hardware.get_memory_facts()['memfree_mb']
    assert free_memory_bytes == 0

    # Simulate a module with a zero return code value and a command output

# Generated at 2022-06-13 00:42:23.280560
# Unit test for method get_memory_facts of class DarwinHardware

# Generated at 2022-06-13 00:42:30.036894
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=False
    )

    dh = DarwinHardware(module)
    dh.populate()
    assert dh.facts['model'] == 'MacBookAir7,2'
    assert dh.facts['osversion'] == '15.4.0'
    assert dh.facts['osrevision'] == '15.4.0'
    assert dh.facts['processor'] == 'Intel(R) Core(TM) i7-5650U CPU @ 2.20GHz'
    assert dh.facts['processor_cores'] == '2'
    assert dh.facts['processor_vcpus'] == '4'
    assert dh.facts['memtotal_mb'] == 8192
    assert dh.facts['memfree_mb'] == 0

# Generated at 2022-06-13 00:42:30.399379
# Unit test for constructor of class DarwinHardwareCollector
def test_DarwinHardwareCollector():
    DarwinHardwareCollector()

# Generated at 2022-06-13 00:42:35.917593
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    fake_module = FakeAnsibleModule()
    darwin_hardware = DarwinHardware(fake_module)

    # Populate facts, then test each one
    darwin_hardware.populate()
    # model
    assert darwin_hardware.facts['model'] == 'MacBookPro10.1'
    # processor
    assert darwin_hardware.facts['processor'] == 'Intel(R) Core(TM) i7-3615QM CPU @ 2.30GHz'
    # processor_cores
    assert darwin_hardware.facts['processor_cores'] == '8'
    # processor_vcpus
    assert darwin_hardware.facts['processor_vcpus'] == '8'
    # memtotal_mb

# Generated at 2022-06-13 00:42:46.530599
# Unit test for method get_memory_facts of class DarwinHardware
def test_DarwinHardware_get_memory_facts():
    import mock
    import platform

    # Prepare the test fixture

# Generated at 2022-06-13 00:42:55.416602
# Unit test for method get_system_profile of class DarwinHardware

# Generated at 2022-06-13 00:43:00.608855
# Unit test for method get_cpu_facts of class DarwinHardware
def test_DarwinHardware_get_cpu_facts():
    m = MockModule()
    m.run_command.return_value = (0, 'foo @ bar', '')
    expected = {'processor': 'foo @ bar', 'processor_cores': '2', 'processor_vcpus': ''}
    facts = DarwinHardware(m).get_cpu_facts()
    assert facts == expected


# Generated at 2022-06-13 00:43:08.897379
# Unit test for method populate of class DarwinHardware
def test_DarwinHardware_populate():
    class TestModule(object):

        def __init__(self):
            self.run_command_calls = []
            self.run_command_results = []
            self.get_bin_path_calls = []
            self.get_bin_path_results = []

        def run_command(self, command):
            self.run_command_calls.append(command)
            return self.run_command_results.pop(0)

        def get_bin_path(self, command):
            self.get_bin_path_calls.append(command)
            return self.get_bin_path_results.pop(0)

    class TestCollector(DarwinHardwareCollector):

        def __init__(self, module):
            self.module = module
            self.collect_calls = []


# Generated at 2022-06-13 00:43:16.599834
# Unit test for method get_mac_facts of class DarwinHardware
def test_DarwinHardware_get_mac_facts():
    module = AnsibleModuleMock({})
    hardware = DarwinHardware(module)
    hardware.sysctl = OrderedDict()
    hardware.sysctl['kern.osversion'] = '12.9.7'
    hardware.sysctl['kern.osrevision'] = '1811'
    mac_facts = hardware.get_mac_facts()
    assert mac_facts['osversion'] == '12.9.7'
    assert mac_facts['osrevision'] == '1811'
    # Actually the model is "MacBookAir7,2" but this is the value returned by system_profiler
    assert mac_facts['model'] == 'MacBook Air'
    assert mac_facts['product_name'] == 'MacBook Air'


# Generated at 2022-06-13 00:43:25.726786
# Unit test for method get_system_profile of class DarwinHardware
def test_DarwinHardware_get_system_profile():
    hardware = DarwinHardware()
    hardware.module = MagicMock()
    hardware.module.run_command.return_value = (0, "Hardware:\n  Hardware Overview:\n      Model Name: MacBook Pro\n      Model Identifier: MacBookPro10,1\n      Processor Name: Intel Core i5\n      Processor Speed: 2.6 GHz\n      Number of Processors: 1\n      Total Number of Cores: 2\n      L2 Cache (per Core): 256 KB\n      L3 Cache: 3 MB\n      Memory: 8 GB\n", "")
    system_profile = hardware.get_system_profile()