

# Generated at 2022-06-13 00:45:35.094402
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    import json
    import sys
    import unittest

    path = os.path.dirname(os.path.realpath(__file__))

    module = {
        'json': json,
        'os': os,
        'sys': sys,
        'run_command': lambda *x: "",
        'path': path
    }

    class args:
        foo = None

    sys.modules['ansible.module_utils.facts'] = args

    setattr(args, 'HPUXHardwareCollector', HPUXHardwareCollector)

    cpu_facts = {'ansible_architecture': '9000/800'}
    hw_facts = {'ansible_architecture': 'ia64'}

# Generated at 2022-06-13 00:45:47.610477
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    from ansible.module_utils.facts.hardware.hpux import HPUXHardware

    hw = HPUXHardware({'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.23'})

    hw.module.run_command = MagicMock(return_value=(0, 'HP rp4440', ''))
    hw.get_hw_facts()
    hw.module.run_command.assert_called_with('model')
    assert hw.facts['model'] == 'HP rp4440'

    hw.module.run_command = MagicMock(return_value=(0, 'Firmware revision = OE.11.23.3303', ''))
    hw.get_hw_facts()

# Generated at 2022-06-13 00:45:55.638346
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    h = HPUXHardware({})
    h.module = MagicMock()
    h.module.run_command("/usr/bin/vmstat | tail -1", use_unsafe_shell=True).return_value = (0, """procs -----------memory---------- ---swap-- -----io---- --system-- -----cpu------
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 1  0      0      0      0      0    0    0     0     0    0    0  0  0  0  0  0
 """, '')

# Generated at 2022-06-13 00:46:02.791199
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    hardware = HPUXHardware(module)

    collected_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.23'
    }

    memory_facts = hardware.get_memory_facts(collected_facts=collected_facts)
    assert memory_facts.get('memfree_mb')
    assert memory_facts.get('memtotal_mb')
    assert memory_facts.get('swaptotal_mb')
    assert memory_facts.get('swapfree_mb')



# Generated at 2022-06-13 00:46:12.786806
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    module = AnsibleModule(argument_spec={})
    hardware_collector = HPUXHardware(module=module)
    ansible_facts = {}
    hardware_facts = hardware_collector.populate(ansible_facts)

    assert hardware_facts['processor_count'] == 1
    assert hardware_facts['memtotal_mb'] <= hardware_facts['swaptotal_mb']
    assert hardware_facts['memfree_mb'] <= hardware_facts['memtotal_mb']
    assert hardware_facts['swapfree_mb'] <= hardware_facts['swaptotal_mb']
    assert hardware_facts['processor_cores'] == 1
    assert hardware_facts['processor'] == 'Intel Itanium 2'
    assert hardware_facts['firmware_version'] == '01.15'

# Generated at 2022-06-13 00:46:17.305372
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    module = type('Module', (object,), {'run_command': HPUXHardware.run_command})
    facts = HPUXHardware(module)
    rc, out, err = facts.module.run_command("cat")
    hw_facts = facts.get_hw_facts()
    assert hw_facts['model'] == 'ia64', "Expected result should be 'ia64' from 'model' command on HP-UX"
    assert hw_facts['firmware_version'] != "", "Expected result should not be empty from 'machinfo' command on HP-UX"
    assert hw_facts['product_serial'] == "", "Expected result should be empty"

# Generated at 2022-06-13 00:46:22.056450
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    module = AnsibleModule(argument_spec={})
    hw = HPUXHardware(module)

    assert hw.populate()['ansible_processor_cores'] == hw.facts['ansible_processor_cores']
    assert hw.populate()['ansible_processor_count'] == hw.facts['ansible_processor_count']
    assert hw.populate()['ansible_memtotal_mb'] == hw.facts['ansible_memtotal_mb']
    assert hw.populate()['ansible_memfree_mb'] == hw.facts['ansible_memfree_mb']
    assert hw.populate()['ansible_swaptotal_mb'] == hw.facts['ansible_swaptotal_mb']

# Generated at 2022-06-13 00:46:32.537617
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    hardware_data = {}
    hardware_data['ansible_architecture'] = '9000/800'
    hardware_data['ansible_distribution_version'] = 'B.11.23'

    hardware_obj = HPUXHardware()
    hardware_obj.module = ansible_module_mock

    cpu_facts = hardware_obj.get_cpu_facts(hardware_data)

    assert cpu_facts['processor_count'] == 2

    hardware_data['ansible_architecture'] = 'ia64'
    hardware_data['ansible_distribution_version'] = 'B.11.31'

    cpu_facts = hardware_obj.get_cpu_facts(hardware_data)
    assert cpu_facts['processor_count'] == 4

# Generated at 2022-06-13 00:46:40.049850
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    hw_facts = HPUXHardware({}).get_hw_facts({'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.23'})
    assert hw_facts['firmware_version'] == '1.72'
    assert hw_facts['product_serial'] == 'CZC2118DQ6'

    hw_facts = HPUXHardware({}).get_hw_facts({'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.31'})
    assert hw_facts['firmware_version'] == '2.81' or hw_facts['firmware_version'] == '2.82'

# Generated at 2022-06-13 00:46:49.708805
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    module = AnsibleModule({})
    # Instantiate HPUXHardware.
    hw = HPUXHardware(module)
    # Instantiate HardwareCollector.
    hc = HPUXHardwareCollector(module=module)
    # only test with APA
    hc.facts.update({'ansible_architecture': '9000/785'})
    hc.facts.update({'ansible_distribution': 'HP-UX'})
    collected_facts = hc.collect()
    hardware_facts = hw.populate(collected_facts)

    assert hardware_facts['processor'] == 'PA-RISC 2.0' or hardware_facts['processor'] == 'PA-RISC 2.1'

# Generated at 2022-06-13 00:47:11.995895
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hw = HPUXHardwareCollector(None)  # noqa

# Generated at 2022-06-13 00:47:15.740771
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    m = HPUXHardware({})
    ansible_facts = {'ansible_architecture': '9000/800', 'ansible_distribution_version': "B.11.31"}
    cpu_facts = m.get_cpu_facts(ansible_facts)
    assert 'processor_count' in cpu_facts
    assert 'processor' in cpu_facts
    assert 'processor_cores' in cpu_facts


# Generated at 2022-06-13 00:47:18.878480
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    # Create instance of class HPUXHardware
    hw = HPUXHardware(None)

    hw_facts = hw.get_hw_facts({'platform': hw.platform, 'distribution': hw.platform})

    assert hw_facts.get('model') is not None
    assert hw_facts.get('firmware_version') is not None
    assert hw_facts.get('product_serial') is not None

# Generated at 2022-06-13 00:47:25.998011
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    module = MockModule()
    hardware = HPUXHardware(module)

    # PA-RISC tests
    cpu_facts = hardware.get_cpu_facts({'ansible_architecture': '9000/800'})
    assert cpu_facts == dict(processor_count=4, processor='PA-RISC 2.0')
    cpu_facts = hardware.get_cpu_facts({'ansible_architecture': '9000/785'})
    assert cpu_facts == dict(processor_count=2, processor='PA-RISC 1.0')

    # Itanium tests
    cpu_facts = hardware.get_cpu_facts({'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.23'})

# Generated at 2022-06-13 00:47:31.384565
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution': 'HP-UX',
        'ansible_distribution_version': 'B.11.23'
    }
    hardware = HPUXHardware(module=None)
    hw_facts = hardware.get_hw_facts(collected_facts=facts)
    assert hw_facts.get('firmware_version') == 'B.11.23'



# Generated at 2022-06-13 00:47:40.581122
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    facts = {}
    facts['ansible_architecture'] = '9000/800'
    hardware = HPUXHardware(module=None)
    cpu_facts = hardware.get_cpu_facts()
    if not cpu_facts['processor_count']:
        raise Exception('test_HPUXHardware_get_cpu_facts: Failed to get processor count')

    facts = {}
    facts['ansible_architecture'] = '9000/785'
    hardware = HPUXHardware(module=None)
    cpu_facts = hardware.get_cpu_facts()
    if not cpu_facts['processor_count']:
        raise Exception('test_HPUXHardware_get_cpu_facts: Failed to get processor count')

    facts = {}
    facts['ansible_architecture'] = 'ia64'

# Generated at 2022-06-13 00:47:43.864980
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hd = HPUXHardwareCollector()
    assert isinstance(hd, HPUXHardwareCollector)
    assert isinstance(hd._fact_class, HPUXHardware)

# Generated at 2022-06-13 00:47:44.444710
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    pass

# Generated at 2022-06-13 00:47:47.773374
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():

    hardware = HPUXHardware({}, None)

    hardware.get_memory_facts({'ansible_architecture': '9000/800'})



# Generated at 2022-06-13 00:47:58.605783
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )
    hardware = HPUXHardware(module)

    # Test get_cpu_facts methods
    results = hardware.get_cpu_facts(collected_facts={'ansible_architecture': '9000/800'})
    assert results == {'processor_cores': 2, 'processor_count': 2, 'processor': 'PA-RISC 2.0'}

    results = hardware.get_cpu_facts(collected_facts={'ansible_architecture': '9000/785'})
    assert results == {'processor_cores': 1, 'processor_count': 1, 'processor': 'Intel 32-bit'}


# Generated at 2022-06-13 00:48:21.943884
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    class Result:
        def __init__(self, rc, out, err):
            self.rc = rc
            self.stdout = out
            self.stderr = err

    class RunCommand:
        def __init__(self):
            self.called = 0

# Generated at 2022-06-13 00:48:28.819304
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    # Unit test with response from vmstat with memfree = 14165
    hw_module = HPUXHardware()
    hw_module.module = MockModule(architecture='9000/800')
    hw_module.module.run_command = Mock(
        return_value=(0, '    procs   ---swap-- -----io---- --system-- -----cpu------\n r b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st\n0 0 14165 14165 14165 14165    0    0     2     1    2    2  2  0 98  0  0', ''))
    memory_facts = hw_module.get_memory_facts()

# Generated at 2022-06-13 00:48:36.647104
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    hw = HPUXHardware()
    hw.module.run_command = lambda *args, **kwargs: ('', '0', '')

    collected_facts = {'ansible_architecture': '9000/800'}
    cpu_facts = hw.get_cpu_facts(collected_facts=collected_facts)
    assert cpu_facts['processor_count'] == 1

    collected_facts = {'ansible_architecture': 'ia64',
                       'ansible_distribution_version': 'B.11.23'}
    cpu_facts = hw.get_cpu_facts(collected_facts=collected_facts)
    assert cpu_facts['processor_count'] == 1


# Generated at 2022-06-13 00:48:37.800988
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    collected_facts = {'ansible_architecture': 'ia64'}
    HPUXHardwareCollector.get_hw_facts(collected_facts)



# Generated at 2022-06-13 00:48:46.506314
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec={})
    hardware = HPUXHardware(module)
    # Get facts with ansible_architecture 9000/850
    collected_facts_1 = {
        "ansible_architecture": "9000/850"
    }
    assert hardware.get_cpu_facts(collected_facts_1) == {'processor_count': 8}
    # Get facts with ansible_architecture 9000/785
    collected_facts_2 = {
        "ansible_architecture": "9000/785"
    }
    assert hardware.get_cpu_facts(collected_facts_2) == {'processor_count': 2}
    # Get facts with ansible_architecture ia64  ansible_distribution_version B.11.23

# Generated at 2022-06-13 00:48:59.882705
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    import sys
    if sys.version_info[0] < 3:
        import __builtin__ as builtins
    else:
        import builtins

    from ansible.module_utils.facts.hardware.hpux import HPUXHardware
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector
    from ansible.module_utils.facts.system.platform import PlatformFactCollector
    from ansible.module_utils.facts.system.architecture import ArchitectureFactCollector

    builtins.__ansible_module_mock = type('AnsibleModuleMock', (object,), {
        'run_command': lambda *args, **kwargs: (0, "8192", None),
    })()


# Generated at 2022-06-13 00:49:09.075850
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    hw = HPUXHardware({'platform': 'HP-UX', 'ansible_architecture': '9000/800', 'ansible_distribution_version': 'B.11.23'})
    data = hw.get_cpu_facts({'ansible_architecture': '9000/800', 'ansible_distribution_version': 'B.11.23'})
    assert data == {
        'processor_count': 15,
        'processor_cores': 1
    }
    hw = HPUXHardware({'platform': 'HP-UX', 'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.23'})

# Generated at 2022-06-13 00:49:16.128433
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    test_module = type('test_module', (object,), {
        'run_command': lambda *args, **kwargs: (0, 'MA8700', None),
        'get_bin_path': lambda *args, **kwargs: '/some/path'
    })

    test_HPUXHardware_object = HPUXHardware(test_module)
    hw_facts = test_HPUXHardware_object.get_hw_facts(collected_facts={'ansible_architecture': '9000/800'})
    assert hw_facts['model'] == 'MA8700'


# Generated at 2022-06-13 00:49:27.227102
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    # test required facts for Ubuntu
    ubuntu_required_facts = set(HPUXHardwareCollector.required_facts)
    ubuntu_required_facts.add('distribution_version')

    # prepare mock module
    mock_module = type('AnsibleModule', (), {})
    mock_module.params = {}

    # init collector
    collector = HPUXHardwareCollector(mock_module)
    facts = collector.collect()

    assert isinstance(facts, dict)
    # check all required facts are present
    if facts['distribution'] == 'Ubuntu':
        assert ubuntu_required_facts.issubset(facts.keys())

# Generated at 2022-06-13 00:49:39.180579
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    try:
        import module_utils.facts as facts
        import module_utils.facts.hardware.hpux as hpux
    except ImportError:
        return
    module = facts.module_utils.get_url_connection_module()
    setattr(module, 'run_command', lambda *args, **kwargs: hpux.run_command(module, *args, **kwargs))
    setattr(module, 'get_platform', lambda *args, **kwargs: hpux.get_platform(module, *args, **kwargs))
    hpux_hw = hpux.HPUXHardware()
    hpux_hw.module = module


# Generated at 2022-06-13 00:50:16.968819
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    result = {}
    facts = dict(platform='HP-UX', distribution='B.11.11 U')
    result['processor_count'] = 1
    result['processor_cores'] = 1
    result['processor'] = 'Intel PA-RISC processor'

    facts['ansible_architecture'] = '9000/800'
    assert result == HPUXHardware().get_cpu_facts(collected_facts=facts)
    facts['ansible_architecture'] = '9000/785'
    assert result == HPUXHardware().get_cpu_facts(collected_facts=facts)
    facts['ansible_architecture'] = 'ia64'

    facts['ansible_distribution_version'] = 'B.11.31'
    result['processor_count'] = 2

# Generated at 2022-06-13 00:50:18.495163
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    obj = HPUXHardwareCollector()
    assert obj
    assert repr(obj)
    assert obj.platform == 'HP-UX'


# Generated at 2022-06-13 00:50:29.553065
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    """
    Test method get_cpu_facts
    """
    # Test for distribution_version B.11.23
    dic = {'ansible_distribution_version': 'B.11.23', 'ansible_architecture': 'ia64'}
    h = HPUXHardware()
    h.module = object()
    h.module.run_command = MagicMock(return_value=(1, '0', '0'))
    data = h.get_cpu_facts(collected_facts=dic)
    assert data['processor'] is None
    assert data['processor_cores'] is None
    assert data['processor_count'] is None
    h.module.run_command.return_value = (0, '4', '')

# Generated at 2022-06-13 00:50:34.021966
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.hardware.hpux import HPUXHardware

    hw = HPUXHardware(basic.AnsibleModule(
    ))

# Generated at 2022-06-13 00:50:41.006150
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=False
    )
    hw_facts = HPUXHardware(module)
    collected_facts = {'ansible_architecture': '9000/800'}
    cpu_facts = hw_facts.get_cpu_facts(collected_facts)
    assert cpu_facts['processor_count'] == 6
    collected_facts_ia64_11_23 = {'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.23'}
    cpu_facts_ia64_11_23 = hw_facts.get_cpu_facts(collected_facts_ia64_11_23)

# Generated at 2022-06-13 00:50:52.638150
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    test_module = AnsibleModule(argument_spec={})
    test_class = HPUXHardware(test_module)
    test_class.populate()
    assert test_class.facts['memfree_mb'] == '2628'
    assert test_class.facts['memtotal_mb'] == '49429'
    assert test_class.facts['swapfree_mb'] == '0'
    assert test_class.facts['swaptotal_mb'] == '13424'
    assert test_class.facts['processor'] == 'Intel(R) Xeon(R) CPU E5-2660 v4 @ 2.00GHz'
    assert test_class.facts['processor_cores'] == '16'
    assert test_class.facts['processor_count'] == '2'

# Generated at 2022-06-13 00:50:56.496953
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hw = HPUXHardwareCollector()
    assert hw.platform == 'HP-UX'
    assert hw._fact_class == HPUXHardware
    assert hw._platform == 'HP-UX'
    assert hw.required_facts == set(['platform', 'distribution'])


# Generated at 2022-06-13 00:51:06.800013
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    module = AnsibleModule(argument_spec={})
    hardware = HPUXHardware(module)

    # Set up the inputs and expected return
    pagesize = 4096
    rc_vmstat = 0
    out_vmstat = 'r b   pswpin  pswpout  fault     cpu  in  sy  cs us sy id   wa  pc  pi  po  fr de sr m1 m1 m1 m5  in   sy  cs us sy id   wa  pc  pi  po  fr de sr  d1  d1  d1 d5   in   sy  cs us sy id   wa  pc  pi  po  fr de sr  d1  d1  d1 d5'
    err_vmstat = ''
    rc_adb = 0
    out_adb = 'phys_mem_pages:  262144'


# Generated at 2022-06-13 00:51:12.899962
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    hardware = HPUXHardware({})
    facts = hardware.get_memory_facts({})
    assert facts
    assert facts['memfree_mb']
    assert facts['memtotal_mb']
    assert facts['swaptotal_mb']
    assert facts['swapfree_mb']

# Generated at 2022-06-13 00:51:20.516673
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    module = DummyAnsibleModule()
    hw = HPUXHardware(module)
    info = hw.populate()
    assert info['processor'] == 'Intel(R) Xeon(R) CPU E5-2620 0 @ 2.00GHz'
    assert info['processor_count'] == 2
    assert info['processor_cores'] == 16
    assert info['memtotal_mb'] == 65536
    assert info['memfree_mb'] == 53348
    assert info['swaptotal_mb'] == 0
    assert info['swapfree_mb'] == 0
    assert info['model'] == 'ia64 hp server rx2800 i2'
    assert info['firmware_version'] == 'B.11.31.1602'



# Generated at 2022-06-13 00:52:18.961861
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    ahc = HPUXHardwareCollector()
    assert ahc.platform == 'HP-UX'
    assert ahc.fact_class == HPUXHardware

# Generated at 2022-06-13 00:52:28.162018
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    hardware = HPUXHardware(None)
    # test when ansible_distribution_version is B.11.31
    hardware.facts = {"ansible_distribution_version": "B.11.31", "ansible_architecture": "ia64"}
    memory = hardware.get_memory_facts()
    assert isinstance(memory, dict)
    assert memory['memtotal_mb'] == 14336
    assert memory['memfree_mb'] == 14177
    # test when ansible_distribution_version is B.11.23
    hardware.facts = {"ansible_distribution_version": "B.11.23", "ansible_architecture": "ia64"}
    memory = hardware.get_memory_facts()
    assert isinstance(memory, dict)
    assert memory['memtotal_mb'] == 13888
   

# Generated at 2022-06-13 00:52:38.411439
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    # Test if we can get hardware facts on old HP-UX version
    module = AnsibleModule(argument_spec={})
    collected_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.23',
    }
    hardware_obj = HPUXHardware(module=module)
    facts = hardware_obj.get_hw_facts(collected_facts=collected_facts)
    assert facts['firmware_version']

    # Test if we can get hardware facts on B.11.31 HP-UX version
    collected_facts['ansible_distribution_version'] = 'B.11.31'
    facts = hardware_obj.get_hw_facts(collected_facts=collected_facts)
    assert facts['model']

# Generated at 2022-06-13 00:52:46.426238
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():

    # Initialize a class instance
    hpux_hw = HPUXHardware()

    collected_facts = dict(ansible_architecture='ia64', ansible_distribution_version='B.11.31')

    # Check if method populate returns a dictionary of processor data
    cpu_facts = hpux_hw.get_cpu_facts(collected_facts=collected_facts)
    assert isinstance(cpu_facts, dict)
    assert 'processor_count' in cpu_facts
    assert 'processor' in cpu_facts
    assert 'processor_cores' in cpu_facts

    # Check if method populate returns a dictionary of memory data
    memory_facts = hpux_hw.get_memory_facts(collected_facts=collected_facts)
    assert isinstance(memory_facts, dict)
    assert 'memfree_mb'

# Generated at 2022-06-13 00:52:48.916788
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    """
    This function is testing the constructor of the class:
    HPUXHardwareCollector
    """
    HPUXHardwareCollector()


# Generated at 2022-06-13 00:52:55.674850
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    facts = {}
    hardware = HPUXHardware(module=None)
    result = hardware.populate()
    assert type(result.get('processor_count')) == int
    assert type(result.get('processor_cores')) == int
    assert type(result.get('memfree_mb')) == int
    assert type(result.get('memtotal_mb')) == int
    assert type(result.get('swaptotal_mb')) == int
    assert type(result.get('swapfree_mb')) == int
    if 'processor' in result:
        assert type(result.get('processor')) == str
    assert type(result.get('model')) == str
    assert type(result.get('firmware_version')) == str

# Generated at 2022-06-13 00:53:01.690368
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    platform_facts = dict(platform='HP-UX')
    distribution_facts = dict(distribution="B.11.23")
    facts = dict(platform_facts, **distribution_facts)
    hpux_hw_collector = HPUXHardwareCollector(module=None, facts=facts)
    assert hpux_hw_collector
    assert hpux_hw_collector._platform == 'HP-UX'
    assert hpux_hw_collector._fact_class == HPUXHardware

# Generated at 2022-06-13 00:53:07.113204
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    facts = {"platform": "HP-UX", "distribution": "B.11.31"}
    test_hwcollector = HPUXHardwareCollector(facts)
    assert isinstance(test_hwcollector, HardwareCollector)
    assert test_hwcollector.facts == facts



# Generated at 2022-06-13 00:53:12.796227
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    hh = HPUXHardware()
    collected_facts = {'ansible_architecture': '9000/800', 'platform': 'HP-UX'}
    mem_facts = hh.get_memory_facts(collected_facts=collected_facts)
    assert mem_facts.get('memfree_mb') == 1332
    assert mem_facts.get('memtotal_mb') == 3227
    assert mem_facts.get('swaptotal_mb') == 122880
    assert mem_facts.get('swapfree_mb') == 51840


# Generated at 2022-06-13 00:53:17.177604
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    hw = HPUXHardware()
    hw.module.run_command = lambda x: [0, '2', '']
    hw.module.params = {'gather_subset': ['all'],
                        'filter': '*'}
    assert hw.get_cpu_facts() == {'processor_count': 2}

