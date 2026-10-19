

# Generated at 2022-06-13 00:45:32.526352
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    collected_facts = {
        'ansible_architecture': '9000/800',
        'ansible_facts': {
            'distribution_version': 'B.11.31',
        }
    }
    test_obj = HPUXHardware(None, collected_facts)
    data = test_obj.get_memory_facts(collected_facts)
    assert data == {'swaptotal_mb': 3892, 'swapfree_mb': 3892, 'memfree_mb': 609, 'memtotal_mb': 2047}

    collected_facts['ansible_architecture'] = 'ia64'
    test_obj = HPUXHardware(None, collected_facts)
    data = test_obj.get_memory_facts(collected_facts)

# Generated at 2022-06-13 00:45:42.106419
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():

    # Create an instance of HPUXHardware
    hpux_hw_facts = HPUXHardware()

    # Create class for mocking HPUXHardware
    class MockHPUXHardware:
        def run_command(self, command, use_unsafe_shell=None):
            return (0, 'ia64', '')
    hpux_hw_facts.module = MockHPUXHardware()

    # Check result of method get_hw_facts
    result = hpux_hw_facts.get_hw_facts()
    assert ('model' in result)

    # Create class for mocking HPUXHardware
    class MockHPUXHardware:
        def run_command(self, command, use_unsafe_shell=None):
            return (0, 'B.11.31', '')

    hpux_hw_facts.module = MockH

# Generated at 2022-06-13 00:45:49.833446
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    new_module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=['!all'], type='list')
        ),
    )
    new_module.exit_json = exit_json
    hpux = HPUXHardwareCollector()
    hpux.module = new_module
    res = hpux.collect()
    assert isinstance(res, dict)
    assert 'model' in res
    assert 'firmware_version' in res
    assert 'product_serial' in res


# Generated at 2022-06-13 00:46:00.065860
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    collected_facts = {'platform': 'HP-UX',
                       'distribution': 'HP-UX',
                       'distribution_version': 'B.11.31',
                       'ansible_architecture': 'ia64'}
    # Test with hpux B.11.23
    collected_facts['distribution_version'] = 'B.11.23'
    hphw = HPUXHardware()
    hphw.module = MockModule()
    rc, out, err = hphw.module.run_command("/usr/contrib/bin/machinfo | grep 'Number of CPUs'")
    hphw.module.run_command.return_value = rc, 'Number of CPUs  = 4', err

# Generated at 2022-06-13 00:46:01.805597
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    my_instance = HPUXHardwareCollector()
    assert my_instance
    assert my_instance._platform == 'HP-UX'

# Generated at 2022-06-13 00:46:07.339814
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    test_module = type('AnsibleModuleMock', (object,), {'run_command': run_command_mock})()
    hardware = HPUXHardware(module=test_module)
    hardware.get_hw_facts()
    assert hardware.facts['model'] == 'HP9000/785 running HP-UX 11.11'



# Generated at 2022-06-13 00:46:09.831750
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    module = HPUXHardwareCollector()
    assert (module._platform == "HP-UX")
    assert isinstance(module._fact_class, HPUXHardware)

# Generated at 2022-06-13 00:46:19.925938
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    # Arguments for HPUXHardware.populate method
    collected_facts = {
        'platform': 'HP-UX',
        'ansible_architecture': 'ia64',
        'ansible_distribution': 'HP-UX',
        'ansible_distribution_version': 'B.11.31',
    }
    m = HPUXHardware()
    # Expected result
    result = {
        'product_serial': 'ABCDEFGHIJKLMNOPQRST',
        'firmware_version': 'HPUX',
        'model': 'HP-UX'
    }
    return m.populate(collected_facts) == result


# Generated at 2022-06-13 00:46:28.179825
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    test_module = type('TestModule', (), {'run_command': fake_run_command})
    test_stdin = ''
    test_stdout = ''
    test_stderr = ''
    test_args = {}
    test_facts = {
        'ansible_architecture': '9000/800',
        'ansible_distribution_version': 'B.11.31',
        'ansible_distribution': 'HP-UX',
    }
    test_hardware = HPUXHardware(test_module, test_stdin, test_stdout, test_stderr, test_args, test_facts)

# Generated at 2022-06-13 00:46:34.576031
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    hardware = HPUXHardware(module=module)
    hardware.module.run_command = MagicMock(return_value=(0, '9000/800', ''))
    hardware.module.run_command.__name__ = 'run_command'

    data = hardware.get_hw_facts()
    assert data['model'] == '9000/800'

# Generated at 2022-06-13 00:46:45.352366
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    h = HPUXHardwareCollector()
    assert h.fact_class == HPUXHardware
    assert h.platform == 'HP-UX'
    assert h.required_facts == set(['platform', 'distribution'])

# Generated at 2022-06-13 00:46:48.177356
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    module = AnsibleModule(argument_spec=dict())
    collector = HPUXHardwareCollector(module=module)

    assert collector.platform == 'HP-UX'
    assert collector.required_facts == set(['platform', 'distribution'])



# Generated at 2022-06-13 00:46:58.253772
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    sparc = {'ansible_architecture': '9000/800'}
    ia64 = {'ansible_architecture': 'ia64'}
    ppc = {'ansible_architecture': '9000/785'}
    b11_23 = {'ansible_distribution_version': 'B.11.23'}
    b11_31 = {'ansible_distribution_version': 'B.11.31'}
    hpux_sparc = HPUXHardware(dict(sparc, **b11_23))
    hpux_ia64_11_23 = HPUXHardware(dict(ia64, **b11_23))
    hpux_ia64_11_31 = HPUXHardware(dict(ia64, **b11_31))
    hpux_pp

# Generated at 2022-06-13 00:47:04.844094
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=[], type='list')
        ),
        supports_check_mode=True)
    if not HAS_UNIX_UTILS_SUPPORT:
        module.fail_json(msg='HP-UX support requires python-unixadmin')
    failed_conditions = []
    facts_module = HPUXHardwareCollector(module=module)
    populate_result = facts_module.populate()
    assert 'processor_count' in populate_result
    assert 'processor' in populate_result
    assert 'processor_cores' in populate_result
    assert 'memtotal_mb' in populate_result
    assert 'memfree_mb' in populate_result
    assert 'swaptotal_mb' in populate_result

# Generated at 2022-06-13 00:47:09.594487
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hwc = HPUXHardwareCollector()
    assert hwc.platform == 'HP-UX'
    assert hwc.required_facts == set(['platform', 'distribution'])
    assert hwc.collectable_facts == set()
    assert hwc.validable_facts == set()
    assert hwc._fact_class == HPUXHardware

# Generated at 2022-06-13 00:47:17.827666
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    module = AnsibleModule(argument_spec={})
    module.mock_command(command='/usr/bin/vmstat', stdout='  0  100 101  ')
    module.mock_command(command='grep Physical /var/adm/syslog/syslog.log', stdout='Apr 24 00:00:01 hostname vmunix: Physical: 33554432 Kbytes')
    module.mock_command(command='echo "phys_mem_pages/D" | adb -k /stand/vmunix /dev/kmem | tail -1 | awk "{print $2}"', stdout='8388608')
    module.mock_command(command='/usr/sbin/swapinfo -m -d -f -q', stdout='1024')

# Generated at 2022-06-13 00:47:20.851474
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    hw = HPUXHardware()
    cpu_facts = hw.get_cpu_facts()
    assert isinstance(cpu_facts, dict)
    assert cpu_facts['processor_count'] > 0
    assert cpu_facts['processor'].startswith('Intel')
    assert cpu_facts['processor_cores'] > 0



# Generated at 2022-06-13 00:47:26.090830
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    hw = HPUXHardware({}, {})
    collected_facts = {
        'ansible_architecture': '9000/800',
        'ansible_distribution': 'HP-UX'
    }
    memory_facts = hw.get_memory_facts(collected_facts)
    assert memory_facts['swaptotal_mb'] > 0
    assert memory_facts['swapfree_mb'] > 0
    assert memory_facts['memtotal_mb'] > 0
    assert memory_facts['memfree_mb'] > 0



# Generated at 2022-06-13 00:47:34.793322
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec={'gather_subset': dict(default=['!all'], type='list')})
    hw = HPUXHardware(module)
    collected_facts = {'ansible_architecture': '9000/800'}
    facts = hw.get_cpu_facts(collected_facts=collected_facts)
    assert facts['processor_count'] == 32

    collected_facts = {'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.23'}
    facts = hw.get_cpu_facts(collected_facts=collected_facts)
    assert facts['processor'] == 'Intel(R) Itanium(R) Processor 9350'
    assert facts['processor_count'] == 2

# Generated at 2022-06-13 00:47:37.810085
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hpux_hardware_collector = HPUXHardwareCollector()
    assert hpux_hardware_collector.fact_class == HPUXHardware
    assert hpux_hardware_collector.platform == 'HP-UX'

# Generated at 2022-06-13 00:48:12.114737
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    module = FakeAnsibleModule()
    hardware = HPUXHardware(module)
    collected_facts = {
        'platform': 'HP-UX',
        'distribution': 'HP-UX',
        'ansible_architecture': 'ia64',
        'ansible_distribution': 'HP-UX',
        'ansible_distribution_version': 'B.11.23'
    }
    hw_facts = hardware.get_hw_facts(collected_facts=collected_facts)
    assert hw_facts['model'] == 'ia64 hp server rx7640'
    assert hw_facts['firmware_version'] == 'B.11.23.3100.23'

    # B.11.31

# Generated at 2022-06-13 00:48:17.964979
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    facts = {'ansible_distribution': 'HP-UX', 'ansible_system': 'HP-UX', 'ansible_architecture': 'ia64'}
    collected_facts = {'ansible_distribution': 'HP-UX', 'ansible_system': 'HP-UX', 'ansible_architecture': 'ia64'}
    result = HPUXHardwareCollector._get_fact_class(None, facts, collected_facts)
    assert result == HPUXHardware

# Generated at 2022-06-13 00:48:26.485125
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    """
    test for HPUX Hardware get_hw_facts
    """
    hw = HPUXHardware()
    hw.module = Mock()
    hw.module.run_command.return_value = ("", "model 9000/800/C8000", "")
    out = hw.get_hw_facts()
    assert out['model'] == '9000/800/C8000'


if __name__ == '__main__':
    # Unit test for HPUXHardware
    from ansible.module_utils import facts
    import sys
    fh = facts.AnsibleFacts(facts_module=HPUXHardwareCollector,
                            resources={'command': '/usr/sbin/swapinfo'})
    ansible_facts = fh.populate()

# Generated at 2022-06-13 00:48:34.977429
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    module = FakeModule()
    result = HPUXHardwareCollector(module).collect()
    assert 'ansible_processor_count' in result
    assert result['ansible_processor_count'] == 32
    assert 'ansible_processor' in result
    assert result['ansible_processor'] == 'Intel(R) Itanium(R) processor'
    assert 'ansible_processor_cores' in result
    assert result['ansible_processor_cores'] == 32
    assert 'ansible_memtotal_mb' in result
    assert result['ansible_memtotal_mb'] == 16384


if __name__ == '__main__':
    test_HPUXHardwareCollector()

# Generated at 2022-06-13 00:48:45.049504
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    try:
        import hpuxfacts.module
    except ImportError:
        hpuxfacts = None


# Generated at 2022-06-13 00:48:58.603989
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    # Stub class
    class AnsibleModule(object):
        def run_command(self, command, use_unsafe_shell=False):
            if command == "model":
                return 0, "hp rx6600", ""
            if command == "/usr/contrib/bin/machinfo |grep -i 'Firmware revision' | grep -v BMC":
                return 0, "Firmware revision: OA.03.61", ""
            if command == "/usr/contrib/bin/machinfo |grep -i 'Machine serial number' ":
                return 0, "Machine serial number=US12345678", ""

    test_obj = HPUXHardware(ansible_module=AnsibleModule())

    # Test get_hw_facts method of HPUXHardware class
    assert test_obj.get_hw_facts

# Generated at 2022-06-13 00:49:08.029102
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec=dict())
    hw = HPUXHardware(module)

    cpu_facts = hw.get_cpu_facts(collected_facts={'ansible_architecture': '9000/800'})
    assert cpu_facts['processor_count'] == 2

    cpu_facts = hw.get_cpu_facts(collected_facts={'ansible_architecture': 'ia64'})
    assert 'processor_count' not in cpu_facts
    cpu_facts = hw.get_cpu_facts(collected_facts={'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.23'})
    assert cpu_facts['processor_count'] == 2

# Generated at 2022-06-13 00:49:15.478725
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    hardware = HPUXHardware(dict())
    rc, out, err = hardware.module.run_command("/usr/sbin/swapinfo -m -d -f -q")
    hardware_facts = hardware.populate()

    assert hardware_facts.get('memtotal_mb') in range(int(out) // 1024, int(out) // 1024 + 1)
    assert hardware_facts.get('memfree_mb') in range(int(out) // 1024, int(out) // 1024 + 1)
    assert hardware_facts.get('processor_cores') in range(1, 16)

# Unit tests for HPUXHardware

# Generated at 2022-06-13 00:49:19.130672
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hux_hw_collector = HPUXHardwareCollector
    assert hux_hw_collector.required_facts == set(['platform', 'distribution'])
    assert hux_hw_collector._platform == 'HP-UX'
    assert hux_hw_collector._fact_class == HPUXHardware

# Generated at 2022-06-13 00:49:29.389200
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    module = AnsibleModule(argument_spec={})
    hw = HPUXHardware(module=module)
    facts = {
        'ansible_architecture': '9000/785',
    }
    hw.populate(collected_facts=facts)
    assert hw.facts['processor_count'] == 4

    facts = {
        'ansible_architecture': 'ia64',
    }
    hw.populate(collected_facts=facts)
    assert hw.facts['processor_count'] == 2
    assert hw.facts['processor_cores'] == 12
    assert hw.facts['processor'] == 'Itanium 9300, "Montvale"'



# Generated at 2022-06-13 00:50:03.850358
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    module = AnsibleModule(argument_spec={})
    collected_facts = {"ansible_architecture": "ia64", "ansible_distribution_version": "B.11.31"}
    hpu = HPUXHardware(module)
    hpu.get_memory_facts(collected_facts)


# Generated at 2022-06-13 00:50:13.895575
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    collected_facts = {'distribution': 'HP-UX'}
    module = MockModule()
    hardware = HPUXHardware(module=module)
    hardware.collect_facts = lambda: collected_facts
    out = hardware.get_hw_facts()

    assert out['model'] == 'ia64 hp server rx2660'
    assert out['firmware_version'] == 'V1.00'
    collected_facts = {'distribution': 'HP-UX', 'architecture': 'ia64'}
    hardware = HPUXHardware(module=module)
    hardware.collect_facts = lambda: collected_facts
    out = hardware.get_hw_facts()

    assert out['model'] == 'HP Integrity rx2660 Server'
    assert out['firmware_version'] == 'V1.0'

# Generated at 2022-06-13 00:50:17.073253
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    collector = HPUXHardwareCollector({'platform': 'HP-UX'})
    assert collector.fact_class == HPUXHardware
    assert collector.platform == 'HP-UX'
    assert collector.required_facts == set(['platform', 'distribution'])


# Generated at 2022-06-13 00:50:21.484468
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    # construct a unique fact to ensure class is loaded
    fact = 'distribution'
    fact_value = 'HP-UX'
    my_collector = HPUXHardwareCollector({fact: fact_value})
    assert my_collector.facts == {fact: fact_value}
    assert my_collector.platform == 'HP-UX'
    assert my_collector.required_facts == set(['platform', 'distribution'])


# Generated at 2022-06-13 00:50:31.907324
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    class MockModule(object):
        def __init__(self):
            self.run_command = MagicMock()

    class MockCollector(object):
        def __init__(self):
            self.facts = {'ansible_architecture': '9000/800',
                          'ansible_processor_count': 1,
                          'ansible_processor_cores': 1}

    class MockHardware(HPUXHardware):
        def __init__(self):
            self.module = MockModule()
            self.collector = MockCollector()

    module = MockHardware()
    module.get_memory_facts()
    assert module.facts['memtotal_mb'] == 1536
    assert module.facts['memfree_mb'] == 1536
    assert module.facts['swaptotal_mb'] == 80

# Generated at 2022-06-13 00:50:35.958321
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hpux_hw_collector = HPUXHardwareCollector()
    assert hpux_hw_collector
    assert hpux_hw_collector.platform == 'HP-UX'
    assert hpux_hw_collector.required_facts == set(['platform', 'distribution'])

# Generated at 2022-06-13 00:50:44.290876
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    class HPModule(object):
        def __init__(self, out):
            self.out = out

        def run_command(self, command, use_unsafe_shell=False):
            return 0, self.out, ''

    class HPFacts(object):
        def __init__(self, facts):
            self.ansible_facts = {'ansible_facts': facts}
        def get(self, key):
            return self.ansible_facts['ansible_facts'][key]

    class TestClassHPUXHardware(HPUXHardware):
        def __init__(self, module, facts):
            self.module = module
            self.facts = facts

        def populate(self):
            return ''

    hp_module = HPModule("free memory:        267 MB")
    hp_facts =  HPFacts

# Generated at 2022-06-13 00:50:49.612713
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    h = HPUXHardware({'ansible_architecture': '9000/800'})
    h.module.run_command = lambda x: ('0', '47024 ', '')
    assert h.get_memory_facts() == {
        'memfree_mb': 112,
        'memtotal_mb': 115
    }

    h = HPUXHardware({'ansible_architecture': '9000/785'})
    h.module.run_command = lambda x: ('0', '47024 ', '')
    assert h.get_memory_facts() == {
        'memfree_mb': 112,
        'memtotal_mb': 115
    }

    h = HPUXHardware({'ansible_architecture': 'ia64'})

# Generated at 2022-06-13 00:50:51.812583
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    facts = dict(platform='HP-UX', distribution='B.11.31')
    result = HPUXHardwareCollector.factory(facts)
    assert isinstance(result, HPUXHardwareCollector)

# Generated at 2022-06-13 00:50:58.714715
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    module = FakeAnsibleModule()
    module.params = {}
    # test without kernel mem as non root and with kernel mem as root
    if os.getuid() == 0:
        module.run_command = mock_run_command(1, '/usr/bin/vmstat | tail -1', '0 0 0 0 0 146 0')
    else:
        module.run_command = mock_run_command(1, '/usr/bin/vmstat | tail -1', '0 0 0 0 0 146 0')
    # test on B.11.23
    module.ansible_facts = {'architecture': 'ia64', 'distribution_version': 'B.11.23'}

# Generated at 2022-06-13 00:51:33.202255
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    # Collected facts
    collected_facts = {'platform': 'linux'}

    # Test object
    hpux_hardware_collector = HPUXHardwareCollector(module=None, collected_facts=collected_facts)
    assert hpux_hardware_collector.required_facts == {'platform', 'distribution'}
    assert hpux_hardware_collector._platform == 'HP-UX'

# Generated at 2022-06-13 00:51:42.669810
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    hw = HPUXHardware()
    hw.module.run_command = lambda *args, **kwargs: (0, 'HP-UX', None)
    hw.module.run_command_environ_update = {
        'BASH_ENV': '/usr/opt/ags/hp/bashrc',
        'ENV': '/usr/opt/ags/hp/bashrc'}
    hw.module.run_command = lambda *args, **kwargs: (0, 'HP-UX B.11.31 ia64 0896938135', None)
    hw.module.run_command = lambda *args, **kwargs: (0, '9000/785/B1000', None)
    hw.module.run_command_environ_update = {}

# Generated at 2022-06-13 00:51:45.652592
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    module = MockModule()
    collected_facts = {'ansible_architecture': '9000/800',
                       'ansible_distribution_version': 'B.11.23'}
    hpux_hw = HPUXHardware(module)
    facts = hpux_hw.get_memory_facts(collected_facts=collected_facts)
    assert facts['memtotal_mb'] == 49152
    assert facts['swaptotal_mb'] == 3841
    assert facts['swapfree_mb'] == 2527


# Generated at 2022-06-13 00:51:53.291165
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    # Setup test data
    collected_facts = {'ansible_architecture': 'ia64', 'ansible_distribution_version': "B.11.31"}
    # Mocks
    hpuxtestobj = HPUXHardware(dict())
    hpuxtestobj.module = MagicMock()
    hpuxtestobj.module.run_command.return_value = (0, "16 15 16", '')
    expected_result = {'swapfree_mb': 47, 'memfree_mb': 1040, 'memtotal_mb': 2048, 'swaptotal_mb': 2048}
    # Run test
    result = hpuxtestobj.get_memory_facts(collected_facts)
    # Check result
    assert result == expected_result
    assert hpuxtestobj.module.run_command.call

# Generated at 2022-06-13 00:51:57.092651
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    collector = HPUXHardwareCollector()

    assert collector._fact_class is HPUXHardware
    assert collector._platform is 'HP-UX'

# Generated at 2022-06-13 00:52:01.454035
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    hpux_hw = HPUXHardware({}, {})
    cpu_facts = hpux_hw.get_cpu_facts()

    assert cpu_facts['processor_count'] >= 1
    assert cpu_facts['processor_cores'] >= 1

# Generated at 2022-06-13 00:52:05.182736
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=['!all'], type='list')
        ),
        supports_check_mode=True
    )
    hw = HPUXHardware(module=module)
    hw_facts = hw.populate()
    module.exit_json(ansible_facts=hw_facts, changed=False)



# Generated at 2022-06-13 00:52:07.957763
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    facts = {'ansible_architecture':'9000/800'}
    h = HPUXHardwareCollector.factory(facts)
    result = h.get_cpu_facts()
    assert result['processor_count'] == 2
    assert result['processor'] == 'PA-RISC 1.1'
    assert result['processor_cores'] == 1

# Generated at 2022-06-13 00:52:11.062394
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hardware_collector = HPUXHardwareCollector()
    assert hardware_collector._fact_class == HPUXHardware
    assert hardware_collector._platform == 'HP-UX'
    assert hardware_collector.required_facts == set(['platform', 'distribution'])

# Generated at 2022-06-13 00:52:20.060720
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils.facts.hardware.hpu_ux import HPUXHardware
    hpux_hw = HPUXHardware()
    facts = FactCollector().get_facts()
    facts['ansible_architecture'] = '9000/800'
    hpux_hw.populate(facts)
    assert hpux_hw.data['processor_count'] == 2
    assert hpux_hw.data['processor'] == 'PA-RISC 2.0'
    assert hpux_hw.data['processor_cores'] == 2
    assert hpux_hw.data['memtotal_mb'] == "4096"
    assert hpux_hw.data['memfree_mb'] == "4096"

# Generated at 2022-06-13 00:52:52.876165
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hardware_collector_obj = HPUXHardwareCollector()
    assert hardware_collector_obj.fact_class == HPUXHardware
    assert hardware_collector_obj.platform == 'HP-UX'
    assert hardware_collector_obj.required_facts == set(['platform', 'distribution'])

# Generated at 2022-06-13 00:53:01.109828
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    h = HPUXHardware({})
    collected_facts = {'ansible_architecture': 'ia64',
                       'ansible_distribution': 'HP-UX',
                       'ansible_distribution_version': 'B.11.23'}
    expected = {'firmware_version': 'P65 07/06/2006',
                'model': 'ia64 hp server rx4640',
                'product_serial': 'CZH8311S5S',
                'support_level': 'unsupported'}
    assert dict(h.get_hw_facts(collected_facts), **expected) == expected



# Generated at 2022-06-13 00:53:04.682143
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    try:
        HPUXHardwareCollector()
    except Exception:
        assert False, "Can not create an instance of HPUXHardwareCollector"
    else:
        assert True, "Can create an instance of HPUXHardwareCollector"

# Generated at 2022-06-13 00:53:12.543514
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    module = FakeModule()
    os_hardware = HPUXHardware(module)
    os_hardware.populate()
    assert os_hardware.facts['memfree_mb'] == '11'
    assert os_hardware.facts['memtotal_mb'] == '44'
    assert os_hardware.facts['swaptotal_mb'] == '33'
    assert os_hardware.facts['swapfree_mb'] == '11'
    assert os_hardware.facts['processor_count'] == '2'
    assert os_hardware.facts['processor_cores'] == '2'
    assert os_hardware.facts['model'] == 'ia64 hp server rx2600'
    assert os_hardware.facts['firmware_version'] == 'HP-UX 11.31'
    assert os_hard

# Generated at 2022-06-13 00:53:19.885568
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    module = FakeAnsibleModule()
    ansible_facts = module.set_fact({
        'platform': 'HP-UX',
        'distribution': 'B.11.31'
    })
    hardware_collector = HPUXHardwareCollector(module, ansible_facts, None)
    assert hardware_collector._fact_class.platform == 'HP-UX'
    assert hardware_collector.required_facts == set(['platform', 'distribution'])
    assert hardware_collector._platform == 'HP-UX'



# Generated at 2022-06-13 00:53:30.474218
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    class HPUXHardwareModule:
        def __init__(self):
            self.params = {}

        def run_command(self, cmd, use_unsafe_shell=False):
            out = ''
            err = ''

            if 'uname' in cmd:
                out = 'HP-UX'

            if 'machinfo' in cmd:
                out = '''
 Intel(r) Itanium(r) Processor 9140
  CPU number 0, speed 2.4 GHz
  16 logical CPUS, 16 available
  Processor family Intel(r) Itanium(r) processor
  System type HP Integrity rx2660
  Number of processors = 2
'''

            if 'psrset' in cmd:
                out = 'LCPU: ON'

            return 0, out, err

    collected_facts = {}
    module = HPU

# Generated at 2022-06-13 00:53:34.594536
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hardware_collector = HPUXHardwareCollector()
    assert hardware_collector._fact_class == HPUXHardware
    assert hardware_collector._platform == 'HP-UX'

# Generated at 2022-06-13 00:53:40.052361
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    facts = dict(hostvars=None, ansible_architecture='ia64', ansible_distribution='HP-UX', ansible_distribution_version='B.11.31')
    result = HPUXHardwareCollector(facts, None)
    assert(result._fact_class is HPUXHardware)
    assert(result._platform == 'HP-UX')
    assert(result.required_facts == set(['platform', 'distribution']))

# Generated at 2022-06-13 00:53:46.337683
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    args = {
        'ansible_facts': {
            'ansible_architecture': 'ia64',
            'ansible_distribution': 'HP-UX',
            'ansible_distribution_version': 'B.11.31'
        }
    }
    set_module_args(args)
    obj = HPUXHardwareCollector(load_fixture('ansible_module_get_cpu_facts.py',
                                             s='''var1: value1
var2: value2'''),
                               facts_module=ansible_module)
    res = obj.collect()
    assert 'ansible_processor' in res
    assert 'ansible_processor_cores' in res
    assert 'ansible_processor_count' in res

# Generated at 2022-06-13 00:53:57.999963
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    """
    Test HPUXHardware.get_cpu_facts method
    """
    import tempfile
    test_str = """
This is test string for cpu_facts
"""
    tmpdir = tempfile.mkdtemp()
    fp = open(tmpdir + "/test_cpu_facts", 'w')
    fp.write(test_str)
    fp.close()
    new_hpux_hardware_instance = HPUXHardware({}, tmpdir + "/test_cpu_facts")
    collected_facts = {'ansible_architecture': '9000/800'}
    expected_result = {'processor_count': 1}
    assert new_hpux_hardware_instance.get_cpu_facts(collected_facts) == expected_result


# Generated at 2022-06-13 00:54:51.131322
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    facts = {
        'platform': 'HP-UX',
        'architecture': 'ia64',
        'distribution_release': 'B.11.23',
        'ansible_architecture': 'ia64',
        'ansible_distribution_release': 'B.11.23',
    }
    data = HPUXHardware(module=None, collected_facts=facts)
    assert data.get_hw_facts() == {'firmware_version': 'P39', 'model': 'ia64 hp server rx2660'}



# Generated at 2022-06-13 00:55:00.706833
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    from ansible.module_utils.facts.hardware.hpux import HPUXHardware
    from ansible.module_utils.facts.collection import FactCollection
    from ansible.module_utils.facts.hardware.base import BaseHardware

    facts = FactCollection()
    facts.collect_facts()

    hw = HPUXHardware(facts)
    memory = hw.get_memory_facts(facts)

    assert isinstance(hw, HPUXHardware)
    assert isinstance(hw, BaseHardware)
    assert 'memfree_mb' in memory
    assert 'memtotal_mb' in memory
    assert 'swapfree_mb' in memory
    assert 'swaptotal_mb' in memory



# Generated at 2022-06-13 00:55:04.317809
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    required_params = {
        'module': None,
        'subset': None
    }

    hw_collector = HPUXHardwareCollector(**required_params)
    assert hw_collector.required_facts == set(['platform', 'distribution'])


# Generated at 2022-06-13 00:55:05.265770
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hc = HPUXHardwareCollector()
    assert hc


# Generated at 2022-06-13 00:55:15.045731
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    with open('./test/data/hpux_machinfo_firmware.txt') as f:
        m_machinfo_firmware = f.read()
    with open('./test/data/hpux_machinfo_serial_number.txt') as f:
        m_machinfo_serial_number = f.read()
    module = AnsibleModule(argument_spec={})

    h = HPUXHardware(module=module)

    class RunCommand(object):
        def __init__(self, rc, stdout, stderr):
            self.rc = rc
            self.stdout = stdout
            self.stderr = stderr

    class AnsibleModule(object):
        def __init__(self, argument_spec):
            pass
