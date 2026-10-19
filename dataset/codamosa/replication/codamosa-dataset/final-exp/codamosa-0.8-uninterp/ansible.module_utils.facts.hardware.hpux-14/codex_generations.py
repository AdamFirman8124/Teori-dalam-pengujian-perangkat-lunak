

# Generated at 2022-06-13 00:45:26.905794
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    hardware = HPUXHardware()
    hardware.module = AnsibleModuleMock()
    hw_facts = hardware.get_hw_facts()
    assert hw_facts['model'] == 'ia64 hp server rx2800 i2'
    assert hw_facts['firmware_version'] == 'v5.6.0'
    assert hw_facts['product_serial'] == 'US12345'



# Generated at 2022-06-13 00:45:29.607821
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    out = """
    model
    9000/785
    """

    module = AnsibleModule(argument_spec={})

    facts = HPUXHardware().get_hw_facts(collected_facts={"ansible_architecture": "9000/785"})
    assert facts["model"] == "9000/785"



# Generated at 2022-06-13 00:45:37.149579
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    hw = HPUXHardware(dict(ansible_architecture="ia64", ansible_distribution_version="B.11.31"))


# Generated at 2022-06-13 00:45:38.986622
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hardware_collector = HPUXHardwareCollector()
    assert hardware_collector._fact_class == HPUXHardware

# Generated at 2022-06-13 00:45:45.549206
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    module = FakeModule({'ansible_architecture': 'ia64'})
    obj = HPUXHardware(module)
    result = obj.get_memory_facts(collected_facts={'ansible_architecture': 'ia64'})
    assert result == {}, "Result must be empty dictionary"



# Generated at 2022-06-13 00:45:53.520023
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    """
    Test get_memory_facts method of class HPUXHardware.
    """
    module_mock = Mock()
    module_mock.run_command.return_value = (0, '16384', '')
    h = HPUXHardware(module_mock)
    memory_facts = h.get_memory_facts()
    assert memory_facts['memfree_mb'] == 64
    assert memory_facts['memtotal_mb'] == 64
    assert memory_facts['swaptotal_mb'] == 0
    assert memory_facts['swapfree_mb'] == 0



# Generated at 2022-06-13 00:45:59.636447
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    hardware = HPUXHardware({})
    facts = hardware.populate()
    assert 'processor' in facts
    assert 'processor_cores' in facts
    assert 'processor_count' in facts
    assert 'model' in facts
    assert 'firmware' in facts
    assert 'memtotal_mb' in facts
    assert 'memfree_mb' in facts
    assert 'swaptotal_mb' in facts
    assert 'swapfree_mb' in facts

# Generated at 2022-06-13 00:46:10.053708
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    module = AnsibleModule(argument_spec={})
    hwinfo = HPUXHardware(module)

    collected_facts = {
        'ansible_architecture': '9000/800',
        'platform': 'HP-UX',
        'distribution': 'HP-UX',
    }
    rc, out, err = hwinfo.module.run_command("model")
    model = out.strip()
    rc, out, err = hwinfo.module.run_command("/usr/bin/vmstat | tail -1", use_unsafe_shell=True)
    data = int(re.sub(' +', ' ', out).split(' ')[5].strip())
    memfree = 4096 * data // 1024 // 1024


# Generated at 2022-06-13 00:46:18.701975
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    module = type('', (object,), {'run_command': run_command})()
    hw = HPUXHardware(module)
    collected_facts = {'ansible_architecture': 'ia64'}
    hw_facts = hw.get_hw_facts(collected_facts)
    assert hw_facts['model'] == 'ia64 hp server rx6600'
    assert hw_facts['firmware_version'] == '4.22'
    assert hw_facts['product_serial'] == 'USC03046UJ'


# Generated at 2022-06-13 00:46:27.299818
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():

    #input for test
    collected_facts = {
        "ansible_architecture": "ia64",
        "ansible_distribution_version": "B.11.31",
        }

    #output for test
    cpu_facts = {
        "processor": "Intel(R) Itanium(R) Processor 9340",
        "processor_count": 2,
        "processor_cores": 1
    }

    # instance of HPUXHardware
    hardware = HPUXHardware()

    # reference of test module
    hardware.module = MockModule()

    #launch method get_cpu_facts
    cpu_facts_result = hardware.get_cpu_facts(collected_facts)

    #assert result
    assert cpu_facts_result == cpu_facts



# Generated at 2022-06-13 00:46:38.755517
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    collector = HPUXHardwareCollector()
    assert collector._fact_class == HPUXHardware
    assert collector._platform == 'HP-UX'

# Generated at 2022-06-13 00:46:49.092519
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    class TestModule(object):
        def run_command(self, *args, **kwargs):
            return (0, 'Unit test', '')

    module = TestModule()

    # HP-UX ia64
    hw = HPUXHardware({'ansible_architecture':'ia64', 'ansible_distribution_version':'B.11.31'}, module)

    result = hw.get_memory_facts()
    assert result == {'swapfree_mb': 0, 'memtotal_mb': 12288, 'swaptotal_mb': 0, 'memfree_mb': 9256}

    # HP-UX PA-RISC
    hw = HPUXHardware({'ansible_architecture':'9000/800'}, module)

    result = hw.get_memory_facts()
   

# Generated at 2022-06-13 00:46:59.153045
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    """ Unit tests for get_cpu_facts method of class HPUXHardware """

    # Create an instance of AnsibleModule
    module = AnsibleModule(argument_spec={})
    # Create an instance of HPUXHardware
    hardware = HPUXHardware(module)

    # Set ansible_architecture fact
    collected_facts = dict(ansible_architecture='9000/800')
    # Unit test get_cpu_facts on 9000/800 architecture
    cpu_facts = hardware.get_cpu_facts(collected_facts=collected_facts)
    assert cpu_facts == {'processor_count': 12,
                         'processor_cores': 12
                        }, "Unexpected results: %s" % cpu_facts

    # Set ansible_architecture fact

# Generated at 2022-06-13 00:47:09.509271
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    module = AnsibleModuleMock()
    # Case 1: IA64 and HPUX B.11.23
    hardware = HPUXHardware(module, collected_facts={'ansible_architecture': "ia64",
                                                     'ansible_distribution_version': "B.11.23"})
    hardware.module.run_command.return_value = (0, "rp3410", "")
    hardware.module.run_command.return_value = (0, "rev=G.11.01; Firmware revision: G.11.01", "")
    hardware.module.run_command.return_value = (0, "Machine serial number = CZC0315HZ9", "")
    hardware.get_hw_facts()
    assert hardware.facts['model'] == "rp3410"

# Generated at 2022-06-13 00:47:16.523334
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    module = FakeAnsibleModule()
    module.run_command = MagicMock(return_value=(0, '0', ''))
    setattr(module, 'ansible_facts', {'platform': 'HP-UX'})
    hpuxhardware = HPUXHardware(module)

    # When
    result = hpuxhardware.populate()

    # Then
    assert result.get('model') == '0'
    assert result.get('processor') == '0'
    assert result.get('processor_count') == 0
    assert result.get('processor_cores') == 0
    assert result.get('memtotal_mb') == 0
    assert result.get('memfree_mb') == 0
    assert result.get('swaptotal_mb') == 0

# Generated at 2022-06-13 00:47:23.011385
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():

    # When machinfo return cores strings release B.11.31 > 1204
    out_machinfo_B_11_31 = 'Number of sockets = 2\n' \
                           'Number of cores   = 16\n' \
                           'Number of threads = 32\n' \
                           'Hyperthreading    = OFF'

    out_machinfo_B_11_31_2 = 'Number of sockets = 2\n' \
                             'Number of cores   = 4\n' \
                             'Number of threads = 8\n' \
                             'Hyperthreading    = OFF'

    out_machinfo_B_11_31_3 = 'Number of sockets = 2\n' \
                             'Number of cores   = 4\n' \
                             'Number of threads = 8\n' \
                            

# Generated at 2022-06-13 00:47:33.339380
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    """
    Unit test for testing the following method return values and output:
    - get memory facts for a PA-RISC system with maximum memory greater
      than 2GB
    - get memory facts for a PA-RISC system with maximum memory less than
      2GB
    - get memory facts for an IA-64 system without Hyperthreading
    - get memory facts for an IA-64 system with Hyperthreading
    """
    hw = HPUXHardware()
    facts = {'ansible_architecture': '9000/785'}
    memory_facts = hw.get_memory_facts(facts)
    assert memory_facts['memtotal_mb'] == 24576
    facts = {'ansible_architecture': '9000/800'}
    memory_facts = hw.get_memory_facts(facts)
    assert memory_

# Generated at 2022-06-13 00:47:36.641904
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hpux_fact_collector = HPUXHardwareCollector()
    assert hpux_fact_collector.platform == 'HP-UX'
    assert hpux_fact_collector.required_facts == set(['platform', 'distribution'])

# Generated at 2022-06-13 00:47:39.185638
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():

    # Constructor of class HPUXHardwareCollector
    hw = HPUXHardwareCollector()

    # Assertion that it is instance of class HardwareCollector
    assert isinstance(hw, HardwareCollector)

# Generated at 2022-06-13 00:47:45.006690
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    module = AnsibleModule(
        argument_spec=dict(
            ansible_facts=dict(required=True, type='dict'),
            gather_subset=dict(required=False, type='list'),
        )
    )

    # Load fake hardware facts for testing
    fake_facts = {
        'ansible_distribution': 'HP-UX',
        'ansible_distribution_version': 'B.11.31',
        'ansible_architecture': 'ia64'
    }
    module.params['ansible_facts'].update(fake_facts)
    HW = HPUXHardware(module)
    data = HW.get_hw_facts()
    assert data.get('model') == 'ia64 hp server rx8640'

# Generated at 2022-06-13 00:47:59.246163
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    memory_facts = {
        'processor_cores': 8,
        'memfree_mb': 1019,
        'memtotal_mb': 13146,
        'swapfree_mb': 4383,
        'swaptotal_mb': 9318,
        'processor': 'Intel(R) Itanium(R) CPU       T800  @ 1.53GHz',
        'processor_count': 32,
        'model': 'ia64 hp server rx2620',
        'firmware_version': 'v3.75'
    }
    hardware = HPUXHardware()
    facts = {}
    facts['ansible_architecture'] = 'ia64'
    facts['ansible_distribution_version'] = 'B.11.23'
    test_memory_facts = hardware.get_memory_facts(facts)


# Generated at 2022-06-13 00:48:05.795080
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    # Unit test for get_cpu_facts
    # initialize HPUXHardware class

    # HPUXHardware(module, facts, timeout=10)
    hpux = HPUXHardware(None, {}, 10)

    # get_cpu_facts(collected_facts)
    # x86_64 HP-UX B.11.31
    assert hpux.get_cpu_facts({'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.31'}) == {
        "processor_cores": 1,
        "processor_count": 2,
        "processor": "Intel(R) Itanium(R) processor"
    }

    # get_cpu_facts(collected_facts)
    # ia64 HP-UX B.11.23
    assert hpux.get_cpu

# Generated at 2022-06-13 00:48:09.395055
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hpux_hardware_collector = HPUXHardwareCollector()
    assert hpux_hardware_collector.required_facts == set(['platform', 'distribution'])
    assert hpux_hardware_collector._platform == 'HP-UX'
    assert hpux_hardware_collector._fact_class == HPUXHardware

# Generated at 2022-06-13 00:48:13.818532
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hpux_hw_collector = HPUXHardwareCollector()
    assert hpux_hw_collector._fact_class == HPUXHardware
    assert hpux_hw_collector._platform == 'HP-UX'
    assert hpux_hw_collector.required_facts == set(['platform', 'distribution'])

# Generated at 2022-06-13 00:48:15.185640
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hc = HPUXHardwareCollector()
    hc.collect()

# Generated at 2022-06-13 00:48:22.069880
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    mock_module = MockModule({'ansible_architecture': 'ia64', 'ansible_distribution_version': "B.11.31"})
    mock_module.run_command = Mock(return_value=(0, '123', ''))
    hardware = HPUXHardware(mock_module)
    facts = hardware.get_memory_facts()
    assert facts == {'memfree_mb': '123', 'memtotal_mb': None, 'swapfree_mb': '123', 'swaptotal_mb': '123'}



# Generated at 2022-06-13 00:48:26.150605
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hwc = HPUXHardwareCollector()
    assert hwc._fact_class == HPUXHardware
    assert hwc._platform == 'HP-UX'
    assert hwc.required_facts == set(['platform', 'distribution'])


# Generated at 2022-06-13 00:48:35.911775
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    import platform
    module = AnsibleModule(
        argument_spec={}
    )
    # cuz we can't change ansible_architecture in unit test directly
    platform.machine = lambda: '9000/800'
    module.run_command = lambda x: (0, '256\n', '')
    hpuxtest = HPUXHardware(module)
    assert hpuxtest.get_memory_facts() == {'memfree_mb': 256, 'memtotal_mb': 16256, 'swaptotal_mb': 0, 'swapfree_mb': 0}
    platform.machine = lambda: 'ia64'
    module.run_command = lambda x: (0, '4096\n', '')
    hpuxtest = HPUXHardware(module)
    assert hpuxtest.get_memory

# Generated at 2022-06-13 00:48:39.877887
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hc = HPUXHardwareCollector()
    assert HPUXHardwareCollector._fact_class == HPUXHardware
    assert hc.platform == 'HP-UX'
    assert hc.required_facts == set(['platform', 'distribution'])

# Generated at 2022-06-13 00:48:45.360097
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec=dict(ansible_architecture=dict(type='str', default='ia64'),
                                              ansible_distribution_version=dict(type='str', default='B.11.31')))
    hardware = HPUXHardware(module=module)
    facts = hardware.get_cpu_facts()
    assert facts['processor_count'] > 0
    assert facts['processor_cores'] > 0
    assert facts['processor']


# Generated at 2022-06-13 00:48:56.441259
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    hw_fact = HPUXHardware(dict(ansible_architecture='ia64', ansible_distribution_version='B.11.23'))
    facts = hw_fact.get_cpu_facts()
    assert facts['processor_count'] == 1
    hw_fact = HPUXHardware(dict(ansible_architecture='ia64', ansible_distribution_version='B.11.31'))
    facts = hw_fact.get_cpu_facts()
    assert facts['processor_count'] == 1


# Generated at 2022-06-13 00:49:02.536652
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    data = ['L-Class', '', '']
    rc = 0
    module = type('', (), {'run_command': lambda *x, **y: (rc, '\n'.join(data), '')})()
    hardware = HPUXHardware(module)
    hardware.get_hw_facts()
    assert hardware.facts.get('model') == data[0]
    assert hardware.facts.get('firmware_version') == data[1]

# Generated at 2022-06-13 00:49:11.568115
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    hw = HPUXHardware()

    # Test Parisc
    facts = {'ansible_architecture': '9000/800'}
    rc, stdout, stderr = hw.module.run_command("cat /opt/ansible/test/unit/ansible/module_utils/facts/hardware/test_hpux_cpu.txt")
    data = stdout.strip().splitlines()
    out = []
    for line in data[3:]:
        line = re.sub(' +', ' ', line)
        fields = line.split(' ')
        out.append(' '.join(fields[2:]).strip())

# Generated at 2022-06-13 00:49:15.966841
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    collected_facts = {
        'platform': 'HP-UX',
        'distribution': 'HP-UX',
    }
    hardware_facts = HPUXHardware(module=None)
    facts = hardware_facts.get_hw_facts(collected_facts)
    assert 'model' in facts
    assert 'firmware_version' in facts
    assert 'product_serial' in facts



# Generated at 2022-06-13 00:49:22.111844
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    class HPUXHardwareMock:
        def __init__(self):
            self.facts = {'ansible_architecture': None}
        def run_command(self, cmd, use_unsafe_shell=False):
            return [0, "", ""]

    hw = HPUXHardwareMock()
    ret = HPUXHardware._get_memory_facts(hw)
    assert not ret

# Generated at 2022-06-13 00:49:32.787184
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    # region Create test environment
    import sys
    import os
    import tempfile

    # create a temp file that ioscan -FkCprocessor command will return
    with tempfile.NamedTemporaryFile(mode="w+") as tempfile_ioscan:
        test_data = """processor  0       0        0/0/3/0          proc0
processor  1       1        0/0/3/1          proc1
processor  2       2        0/0/3/2          proc2
processor  3       3        0/0/3/3          proc3"""
        tempfile_ioscan.write(test_data)
        tempfile_ioscan.flush()
        os.fsync(tempfile_ioscan.fileno())

        # create a temp file that machinfo command will return

# Generated at 2022-06-13 00:49:43.833087
# Unit test for method get_cpu_facts of class HPUXHardware

# Generated at 2022-06-13 00:49:54.550324
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    test_hardware = HPUXHardware({'module': object()})
    result = test_hardware.populate()
    if not result.get('processor_count'):
        raise AssertionError()
    if result.get('processor_cores') == None:
        raise AssertionError()
    if not result.get('memtotal_mb'):
        raise AssertionError()
    if not result.get('memfree_mb'):
        raise AssertionError()
    if not result.get('swaptotal_mb'):
        raise AssertionError()
    if not result.get('swapfree_mb'):
        raise AssertionError()
    rc, out, err = test_hardware.module.run_command("/usr/contrib/bin/machinfo | grep 'Memory'")

# Generated at 2022-06-13 00:49:59.655796
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    hardware = HPUXHardware({'platform': 'HP-UX'})

    collected_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': "B.11.31",
        'ansible_distribution': 'HP-UX',
        'ansible_os_family': "hpux",
    }

    cpu_facts = hardware.get_cpu_facts(collected_facts)

    assert cpu_facts['processor_count'] == 1
    assert cpu_facts['processor_cores'] == 2
    assert cpu_facts['processor'] == 'Intel(R) Itanium'


# Generated at 2022-06-13 00:50:09.914922
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    class Module():
        """ Minimalistic ansible module stub """
        def __init__(self, module_args):
            self.params = module_args

        def run_command(self, cmd, use_unsafe_shell=False):
            if 'model' in cmd:
                return 0, 'Itanium B132L', ''
            elif 'machinfo' in cmd:
                return 0, 'Firmware revision = 8.2.1.4-C    Machine serial number = ITANIUM  Machine model number = Itanium rp3410', ''
        def fail_json(self, **kwargs):
            pass
    class Facts():
        def get(self, fact, default=None):
            if fact == 'platform':
                return 'HP-UX'

# Generated at 2022-06-13 00:50:27.805544
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=['!all'], type='list')
        ),
        supports_check_mode=True
    )
    shared_obj = HardwareCollector
    hw_collect_obj = HPUXHardwareCollector()
    isinstance(hw_collect_obj, shared_obj)
    assert hw_collect_obj._platform == 'HP-UX'
    assert hw_collect_obj.required_facts == {'platform', 'distribution'}
    assert hw_collect_obj._fact_class.platform == 'HP-UX'
    assert hw_collect_obj._fact_class.__name__ == 'HPUXHardware'


# Generated at 2022-06-13 00:50:30.279153
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    obj = HPUXHardwareCollector({}, {})
    assert obj.facts == {}
    assert obj.required_facts == set(['platform', 'distribution'])
    assert obj.platform == 'HP-UX'
    assert obj.fact_class == HPUXHardware

# Generated at 2022-06-13 00:50:40.761327
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    hw = HPUXHardware()
    collected_facts = {'ansible_architecture': '9000/800', 'ansible_distribution_version': 'B.11.23'}
    cpu_facts = hw.get_cpu_facts(collected_facts)
    assert cpu_facts['processor_count'] == 8
    assert cpu_facts['processor'] == 'Intel Itanium 2'
    assert cpu_facts['processor_cores'] == 8

    collected_facts = {'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.23'}
    cpu_facts = hw.get_cpu_facts(collected_facts)
    assert cpu_facts['processor_count'] == 8
    assert cpu_facts['processor'] == 'Intel Itanium 2'
    assert cpu

# Generated at 2022-06-13 00:50:49.205550
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    hardware_obj = HPUXHardware({
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.23',
    })
    hardware_obj.get_hw_facts()
    assert hardware_obj.facts['model'] == 'rp3440'

#Unit test for method get_memory_facts of class HPUXHardware

# Generated at 2022-06-13 00:50:53.559169
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    module = AnsibleModule()
    # adb output is from a system with 4G of RAM, so memory facts should come back as 393216
    # (4G in MB)
    module.run_command = Mock(return_value=(0, "phys_mem_pages/D\nphys_mem_pages:      0x0000f000", ""))
    hw = HPUXHardware()
    hw.module = module
    hw.populate()
    assert hw.facts['memtotal_mb'] == 393216

# Generated at 2022-06-13 00:50:59.913026
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    import sys
    import tempfile
    test_module = sys.modules[__name__]
    hpux_hardware = HPUXHardware(test_module)
    hpux_hardware.module.run_command =  lambda x: (0, "phys_mem_pages/D = 80000", None)
    result = hpux_hardware.get_memory_facts()
    assert result['memfree_mb'] == 1024, "Error in memfree_mb calculation"
    assert result['memtotal_mb'] == 3125, "Error in memtotal_mb calculation"
    assert result['swapfree_mb'] == 0, "Error in swapfree_mb calculation"
    assert result['swaptotal_mb'] == 0, "Error in swaptotal_mb calculation"


# Generated at 2022-06-13 00:51:09.202772
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    # Create an instance of class HPUXHardware
    test = HPUXHardware()

    # Create a temporary file containing faked output of 'model' command
    with open("model.txt", 'w') as f:
        f.write("9000/785\n")

    # Create a temporary file containing faked output of '/usr/contrib/bin/machinfo |grep -i 'Firmware revision'' command
    with open("machinfo.txt", 'w') as f:
        f.write("Firmware revision = 'D49F'\n")

    # Create a temporary file containing faked output of '/usr/contrib/bin/machinfo |grep -i 'Machine serial number'' command

# Generated at 2022-06-13 00:51:12.774605
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    module = AnsibleModule(argument_spec=dict())
    hardware_obj = HPUXHardware(module=module)
    hardware_obj.get_hw_facts(collected_facts={'ansible_architecture': 'ia64'})

# Generated at 2022-06-13 00:51:20.698530
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    test_module = type('AnsibleModule', (object,), {'run_command': run_command})()
    test_get_hw_facts = HPUXHardware(module=test_module).get_hw_facts(collected_facts={'ansible_architecture': 'ia64'})
    assert test_get_hw_facts == {'firmware_version': 'B.11.31', 'product_serial': 'CZC048024T', 'model': 'ia64 hp Integrity rx7640 Server'}
    test_get_hw_facts = HPUXHardware(module=test_module).get_hw_facts(collected_facts={'ansible_architecture': '9000/800'})

# Generated at 2022-06-13 00:51:23.115305
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    collector = HPUXHardwareCollector()
    assert isinstance(collector, HPUXHardwareCollector)
    assert "requirements_exclude_any" in collector.options
    assert "ansible_facts" in collector.options

# Generated at 2022-06-13 00:51:45.170945
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    module = AnsibleModule(argument_spec={})
    hardware_collector = HPUXHardwareCollector(module=module)
    hw = hardware_collector.collect()[0]
    facts = hw.populate(collected_facts={'platform': 'HP-UX', 'ansible_distribution_version': 'B.11.31'})

# Generated at 2022-06-13 00:51:52.978768
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    test_module = AnsibleModule(argument_spec={})
    test_module.params = {}
    obj = HPUXHardware(module=test_module)

    # For ia64 systems
    obj.module.run_command = MagicMock(side_effect=[(1, '', ''), (0, 'Firmware revision = HP-UX 11iv3 B.11.31.1305', ''),
                                                    (0, 'Machine serial number = 5543', '')])
    assert obj.get_hw_facts() == {'firmware_version': 'HP-UX 11iv3 B.11.31.1305', 'product_serial': '5543'}

# Generated at 2022-06-13 00:52:02.525566
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    data = {}
    data['ansible_architecture'] = '9000/800'
    data['ansible_distribution_version'] = "B.11.31"

    hardware = HPUXHardware(module=None, collected_facts=data)
    cpu_facts = hardware.get_cpu_facts(collected_facts=data)
    assert cpu_facts['processor_count'] == 2
    assert cpu_facts['processor_cores'] == 2
    assert cpu_facts['processor'] == 'Intel(R) Itanium(R) Processor 9320'



# Generated at 2022-06-13 00:52:04.952494
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    assert HPUXHardwareCollector.platform == 'HP-UX'
    assert HPUXHardwareCollector.required_facts == set(['platform', 'distribution'])
    assert HPUXHardwareCollector._fact_class == HPUXHardware
    assert HPUXHardwareCollector._platform == 'HP-UX'

# Generated at 2022-06-13 00:52:08.350642
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hostname = 'testhost'
    fakedevices = ['a', 'b', 'c']
    fact_cache = dict()
    fact_cache['hostname'] = hostname
    fact_cache['devices'] = fakedevices

    _collector = HPUXHardwareCollector(fact_cache)
    assert _collector.fact_cache == dict(hostname=hostname, devices=fakedevices)

# Unit tests for function populate of class HPUXHardwareCollector

# Generated at 2022-06-13 00:52:17.574657
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    '''Unit test for method get_hw_facts of class HPUXHardware'''

    class MyModule:
        def __init__(self, run_command_args=None, run_command_rcs=None):
            self.run_command_args = run_command_args
            self.run_command_rcs = run_command_rcs

        def run_command(self, args, **kwargs):
            if args == self.run_command_args:
                out = self.run_command_args
            else:
                out = b"HP Integrity Superdome X with Express Band"

            if self.run_command_rcs is not None:
                rc = self.run_command_rcs.pop()
            else:
                rc = 0

            return rc, out, ''


# Generated at 2022-06-13 00:52:24.092881
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    # Initialize cachedir
    hw = HPUXHardware({'module_setup': True, 'cachedir': '/tmp'})
    hw.module.run_command = lambda *_: (0, '4', '')
    hw.get_cpu_facts() == {'processor_count': 4}
    hw.module.run_command = lambda *_: (0, '', '')
    hw.get_cpu_facts({'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.23'})
    expected = {'processor_count': 2, 'processor': 'Intel(R) Itanium(R) Processor', 'processor_cores': 6}

# Generated at 2022-06-13 00:52:31.661348
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    # Create an instance of argument spec
    argument_spec = dict(
        gather_subset=dict(default=['!all', 'min'], type='list')
    )
    # Create a mock for class HPUXHardware:
    hw = HPUXHardware(module=dict(argument_spec=argument_spec, check_mode=False))
    # Create a mock for returned object of run_command
    rc = 0
    err = ''
    out = 'Kbytes 1024  4096'
    hw.module.run_command = lambda *args, **kwargs: (rc, out, err)
    memory_facts = hw.get_memory_facts()
    assert isinstance(memory_facts, dict)
    assert 'memfree_mb' in memory_facts.keys()
    assert 'memtotal_mb' not in memory_

# Generated at 2022-06-13 00:52:36.523772
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():

    class dummy:
        pass

    class module:
        pass

    Hardware_object = HPUXHardware()
    Hardware_object.module = module()
    Hardware_object.module.run_command = lambda command, use_unsafe_shell=False: \
                                          (0, "", "")
    Hardware_object.module.run_command.return_value = (0, "", "")
    Hardware_object.populate()


# Generated at 2022-06-13 00:52:43.688535
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    module = FakeModule()
    hardware = HPUXHardware(module)
    collected_facts = {'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.23'}
    memory_facts = hardware.get_memory_facts(collected_facts=collected_facts)
    assert hardware.module.run_command.call_count == 4
    assert memory_facts['memfree_mb'] >= 0
    assert memory_facts['memtotal_mb'] > 0
    assert memory_facts['swaptotal_mb'] > 0
    assert memory_facts['swapfree_mb'] >= 0



# Generated at 2022-06-13 00:52:59.377158
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    x = HPUXHardwareCollector()
    assert x.required_facts == set(['platform', 'distribution']), 'Failed to create HPUXHardwareCollector instance'

# Generated at 2022-06-13 00:53:03.310272
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    module = type('AnsibleModule', (object,), {})()
    module.run_command = MagicMock(return_value=(0, 'Test\n', ''))
    hardware = HPUXHardware(module)
    hw_facts = hardware.get_hw_facts()
    assert hw_facts['model'] == 'Test'

# Generated at 2022-06-13 00:53:06.407417
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hw_collector = HPUXHardwareCollector(None)
    assert len(hw_collector.required_facts) == 2
    assert hw_collector._fact_class == HPUXHardware
    assert hw_collector._platform == 'HP-UX'


# Generated at 2022-06-13 00:53:13.183328
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    collected_facts = dict()
    collected_facts['ansible_architecture'] = '9000/800'
    hardware = HPUXHardware(module=dict(), collected_facts=collected_facts)
    hardware_facts = hardware.populate()

    assert hardware_facts['processor_count'] == 2
    assert hardware_facts['memfree_mb'] > 0
    assert hardware_facts['memtotal_mb'] > 0
    assert hardware_facts['swaptotal_mb'] > 0
    assert hardware_facts['swapfree_mb'] > 0
    assert hardware_facts['firmware_version'] == ''
    assert hardware_facts['product_serial'] == ''
    assert hardware_facts['model']


# Generated at 2022-06-13 00:53:22.541403
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    hpux_hardware = HPUXHardware(dict())
    collected_facts = {'ansible_architecture': '9000/800'}
    cpu_facts = hpux_hardware.get_cpu_facts(collected_facts=collected_facts)
    assert cpu_facts['processor_count'] == 1
    collected_facts = {'ansible_architecture': 'ia64'}
    cpu_facts = hpux_hardware.get_cpu_facts(collected_facts=collected_facts)
    assert cpu_facts['processor'] == 'Intel Family : 11 Model : 1 Stepping : 1'
    assert cpu_facts['processor_cores'] == 2
    assert cpu_facts['processor_count'] == 2

# Generated at 2022-06-13 00:53:26.891863
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    test_module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )
    test_system = HPUXHardware()
    test_system.module = test_module
    assert test_system.get_memory_facts() == 'memory_facts'

# Generated at 2022-06-13 00:53:28.887144
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    collector = HPUXHardwareCollector(module=None)

    assert collector._fact_class == HPUXHardware
    assert collector._platform == 'HP-UX'

# Generated at 2022-06-13 00:53:40.515937
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    module = AnsibleModule(argument_spec=dict())
    module.run_command = mock.Mock(return_value=(0, 'test_model', ''))
    hw = HPUXHardware(module=module)
    facts = hw.get_hw_facts()
    assert facts.get('model') == 'test_model'
    assert facts.get('firmware_version') is None
    assert facts.get('product_serial') is None
    module.run_command = mock.Mock(return_value=(0, 'HP-UX B.11.31 U ia64 0129726431', ''))
    hw = HPUXHardware(module=module)
    facts = hw.get_hw_facts()
    assert facts.get('model') == 'test_model'

# Generated at 2022-06-13 00:53:46.895502
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    collected_facts = {'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.23'}
    hphw = HPUXHardware()
    hphw.module = MockModule()
    facts = hphw.populate(collected_facts)
    assert facts['processor'] == 'Intel(R) Itanium(R) Family Montecito'
    assert facts['processor_count'] == 2
    assert facts['processor_cores'] == 2
    assert facts['memtotal_mb'] == 1005
    assert facts['memfree_mb'] == 239
    assert facts['swaptotal_mb'] == 2046
    assert facts['swapfree_mb'] == 184
    assert facts['model'] == 'ia64 hp Integrity rx2620'

# Generated at 2022-06-13 00:53:58.281890
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    """Test get_memory_facts() of HPUXHardware class."""
    # Testing with HP-UX 9000/800 architecture.
    mock_args = {'ansible_architecture': '9000/800',
                 'ansible_distribution': 'HP-UX',
                 'ansible_distribution_major_version': 'B.11.31',
                 'ansible_distribution_version': 'B.11.31'}
    assert HPUXHardware.get_memory_facts(mock_args) == {'memfree_mb': 0, 'memtotal_mb': 16384, 'swapfree_mb': 40567, 'swaptotal_mb': 40576}

    # Testing with HP-UX 9000/785 architecture.

# Generated at 2022-06-13 00:54:25.082765
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    module_mock = AnsibleModule(
        argument_spec={
            'gather_subset': dict(type='list', default=['!all', '!min']),
            'gather_timeout': dict(type='int', default=10),
            'filter': dict(type='str', default='*')
        }
    )

    hw_mock = HPUXHardware(module_mock)

    # vmstat return values
    vms = {'swapfree': 0,
           'memtotal': 3145728}
    vms_mock = {'ansible_architecture': '9000/800',
                'ansible_distribution_version': 'B.11.23'}

    # vmstat

# Generated at 2022-06-13 00:54:28.042223
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    hardware = HPUXHardware()
    collected_facts = {'ansible_architecture': 'ia64',
                       'ansible_distribution_version': 'B.11.31'}
    cpu_facts = hardware.get_cpu_facts(collected_facts)
    assert cpu_facts['processor_count'] == 4

# Generated at 2022-06-13 00:54:36.552393
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():

    module = AnsibleModule(argument_spec={})

    # Prepare some test data

# Generated at 2022-06-13 00:54:43.382655
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    module = type('MockModule', (object,), {})()
    module.run_command = type('MockRunCommand', (object,), {})()

# Generated at 2022-06-13 00:54:52.972720
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    # Init ansible module
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    # Init HPUXHardware instance
    h = HPUXHardware(module=module)

    # Init facts
    facts = {
        'ansible_architecture': '9000/800'
    }

    # First test - syslog.log exists and contains memory info
    rc, out, err = module.run_command("grep Physical syslog.log")
    module.run_command.return_value = (0, "Aug 27 08:57:02  Physical: 4096 Kbytes", None)
    module.run_command.return_value = (0, "86400", None)
    module.run_command.return_value = (0, "471860", None)
   

# Generated at 2022-06-13 00:55:02.762976
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():

    # Test scenario where memory details aren't sent to syslog
    # Test will run against docker image hpux/11.31 which doesn't have
    # /var/adm/syslog/syslog.log
    module = os.environ['ANSIBLE_MODULE_UTILS']
    facts = HPUXHardwareCollector.collect(module, '/run/ansible_facts', {})
    test_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.31'
    }
    hardware = HPUXHardware(facts, test_facts)
    hardware_facts = hardware.populate()
    assert hardware_facts['memtotal_mb'] == 1024  # 1024MB = 1GB



# Generated at 2022-06-13 00:55:10.258449
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    hardware_module = HPUXHardware(dict(ANSIBLE_MODULE_ARGS={'gather_subset': 'all'}), dict())
    hardware_module.module.run_command = lambda *args: (0, 'test model', '')
    hardware_module.module.run_command = lambda *args: (0, 'test Firmware revision', '')
    hardware_module.module.run_command = lambda *args: (0, 'test Machine serial number', '')
    hw_facts = hardware_module.get_hw_facts()
    assert hw_facts['model'] == 'test model'
    assert hw_facts['firmware_version'] == 'test Firmware revision'
    assert hw_facts['product_serial'] == 'test Machine serial number'