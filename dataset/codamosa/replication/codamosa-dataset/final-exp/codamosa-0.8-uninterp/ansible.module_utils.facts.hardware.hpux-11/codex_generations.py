

# Generated at 2022-06-13 00:45:32.771591
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    module = None
    collected_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': "B.11.31"
    }
    hw = HPUXHardware(module=module)
    new_facts = hw.get_hw_facts(collected_facts)
    assert type(new_facts) == dict
    assert new_facts['firmware_version'] == 'v3.00'
    assert new_facts['product_serial'] != ''
    assert new_facts['model'] == 'ia64 hp server rx2660'



# Generated at 2022-06-13 00:45:38.053047
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    test_module = AnsibleModule(
        argument_spec={}
    )
    test_module.params = {}
    hpux_hw = HPUXHardware()
    hpux_hw.module = test_module
    hpux_hw.populate()
    assert hpux_hw.facts['memfree_mb']
    assert hpux_hw.facts['memtotal_mb']
    assert hpux_hw.facts['swapfree_mb']
    assert hpux_hw.facts['swaptotal_mb']



# Generated at 2022-06-13 00:45:49.621636
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    module = MockAnsibleModule()
    hardware = HPUXHardware(module)
    hardware.populate()
    assert hardware.facts['processor_cores'] == 1
    assert hardware.facts['processor_count'] == 1
    assert hardware.facts['processor'] == 'Itanium 2'
    assert hardware.facts['memtotal_mb'] == 4096
    assert hardware.facts['memfree_mb'] == 3122
    assert hardware.facts['memavailable_mb'] == 3122
    assert hardware.facts['swaptotal_mb'] == 0
    assert hardware.facts['swapfree_mb'] == 0
    assert hardware.facts['model'] == 'ia64 hp server rx8620'
    assert hardware.facts['firmware_version'] == '1.95'

# Generated at 2022-06-13 00:45:51.934054
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    collector = HPUXHardwareCollector()
    assert isinstance(collector, HPUXHardwareCollector)


# Generated at 2022-06-13 00:45:58.325638
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec={})
    platform_facts = get_platform_facts(module)
    hardware = HPUXHardware(module)
    cpu_facts = hardware.get_cpu_facts(collected_facts=platform_facts)

    assert isinstance(cpu_facts, dict)
    assert 'processor' in cpu_facts
    assert 'processor_cores' in cpu_facts
    assert 'processor_count' in cpu_facts



# Generated at 2022-06-13 00:46:00.559715
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    h = HPUXHardwareCollector()
    assert h.platform == 'HP-UX'
    assert h.required_facts == {'distribution', 'platform'}

# Generated at 2022-06-13 00:46:11.120540
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec={})
    hw = HPUXHardware(module)
    collected_facts = {}

    # Test for model hp9000/785/C8000
    collected_facts['ansible_architecture'] = '9000/785'
    cpu_facts = hw.get_cpu_facts(collected_facts=collected_facts)
    assert cpu_facts['processor_count'] == 1
    assert cpu_facts['processor'] == ''
    assert cpu_facts['processor_cores'] == ''

    # Test for model ia64
    # Test for HP-UX version 11.31
    collected_facts['ansible_architecture'] = 'ia64'
    collected_facts['ansible_distribution_version'] = 'B.11.31'
    cpu_facts = hw.get

# Generated at 2022-06-13 00:46:17.353758
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    collected_facts = {'platform': 'HP-UX', 'distribution': 'HP-UX'}
    required_facts = set(['platform', 'distribution'])
    hpux_hw_collector = HPUXHardwareCollector(collected_facts)
    assert hpux_hw_collector.collected_facts == collected_facts
    assert hpux_hw_collector.required_facts == required_facts

# Generated at 2022-06-13 00:46:26.803720
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    '''
    Test with this parameters:
     - syslog output from HP-UX machine without memory details
     - parsed adb output from HP-UX machine without memory details
    '''
    params = {}
    module = type('', (object,), params)
    module.run_command = MagicMock(return_value=(0, '', ''))

    class TestClass():
        def __init__(self):
            self.module = module

    test_obj = TestClass()

    # Test when syslog output has no memory details
    test_obj.module.run_command = MagicMock(return_value=(0, '', ERROR))
    result = HPUXHardware(test_obj).get_memory_facts()
    assert result == {}

    # Test with parsed adb output from HP-UX machine without memory details
    # /dev

# Generated at 2022-06-13 00:46:36.924399
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    hptest_module = MockHPUXHardwareModule()
    hptest_module.facts = {'ansible_distribution_version': 'B.11.23', 'ansible_architecture': 'ia64'}
    hptest = HPUXHardware(hptest_module)
    cpu_facts = hptest.get_cpu_facts()
    assert cpu_facts['processor_count'] == 2
    hptest_module.run_command.return_value = (0, '', '')
    hptest_module.facts = {'ansible_distribution_version': 'B.11.31', 'ansible_architecture': 'ia64'}
    hptest = HPUXHardware(hptest_module)
    cpu_facts = hptest.get_cpu_facts()

# Generated at 2022-06-13 00:46:52.673729
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    module = AnsibleModuleMock()
    hpux_hw = HPUXHardware(module=module)

    cpu_facts = {}
    # test get_cpu_facts with collected_facts = None
    cpu_facts_returned = hpux_hw.get_cpu_facts()
    assert cpu_facts_returned == cpu_facts

    collected_facts = {'ansible_architecture': '9000/800', 'ansible_distribution_version': 'B.11.31',
                       'ansible_memfree_mb': '675', 'ansible_memtotal_mb': '8192', 'ansible_swapfree_mb': '8436',
                       'ansible_swaptotal_mb': '8704'}

    # test get_cpu_facts with collected_facts = {'ansible_architecture': '

# Generated at 2022-06-13 00:47:02.609188
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    """
    This function tests method get_cpu_facts of class HPUXHardware
    """
    h = HPUXHardware()


# Generated at 2022-06-13 00:47:06.811758
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hw = HPUXHardwareCollector()
    assert hw._fact_class == HPUXHardware
    assert hw._platform == 'HP-UX'
    assert hw.required_facts == set(['platform', 'distribution'])


# Generated at 2022-06-13 00:47:14.739747
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    # Case 1 : 0 percent free memory
    test_module = type('test_module', (object, ), {
        'run_command': lambda *args, **kwargs: (
            # rc, out, err
            (0, 'total 16384', ''),
            # rc, out, err
            (0, 'memory  14408', ''),
        )
    })
    hardware = HPUXHardware(test_module)
    assert hardware.get_memory_facts() == {'memtotal_mb': 16, 'memfree_mb': 14}

    # Case 2 : 50 percent free memory

# Generated at 2022-06-13 00:47:18.108912
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    test_module = AnsibleModule(argument_spec={})
    if not HAS_LIB_HP_UX:
        module.fail_json(msg='Test could not be performed, hp-ux module not found.')
    else:
        test_obj = HPUXHardware()
        test_obj.module = test_module
        rc = test_obj.get_cpu_facts()

        assert 'processor_count' in rc.keys()
        assert 'processor' in rc.keys()


# Generated at 2022-06-13 00:47:21.461614
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    data = [{'ansible_architecture': '9000/800'}, {'ansible_architecture': '9000/785'}, {'ansible_architecture': 'ia64'}]
    for el in data:
        out = HPUXHardwareCollector.get_facts(el)
        assert out.__class__.__name__ == 'HPUXHardware'

# Generated at 2022-06-13 00:47:31.110814
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    """
    HPUXHardware - class to test
    """
    # Initializing test data
    module = AnsibleModuleMock()
    cpu_facts = {
        'processor': 'HP 9000/800 model 829',
        'processor_cores': 2,
        'processor_count': 2,
    }
    memory_facts = {
        'memfree_mb': 8192,
        'memtotal_mb': 8192,
        'swapfree_mb': 1024,
        'swaptotal_mb': 1024,
    }
    hw_facts = {
        'model': 'HP 9000/800 model 829',
        'firmware_version': 'HPHP-UX B.11.00 U',
        'product_serial': 'PCA7E0023DH',
    }

# Generated at 2022-06-13 00:47:40.011657
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    from ansible.module_utils.facts.hardware.hpux import HPUXHardware
    from ansible.module_utils.facts import FactManager

    class TestModule():
        def __init__(self, params):
            self.params = params

        def run_command(self, cmd, use_unsafe_shell):
            class TestExec():
                def __init__(self, output, rc, std_err):
                    self.output = output
                    self.std_err = std_err
                    self.rc = rc

            if cmd.endswith('vmstat'):
                return TestExec('', 0, '')
            if cmd.endswith('swapinfo -m -d -f -q'):
                return TestExec('', 0, '')

# Generated at 2022-06-13 00:47:43.184156
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    hw = HPUXHardware({'ansible_distribution': 'HP-UX'})
    collected_facts = {'ansible_architecture': 'ia64'}
    hw_facts = hw.get_hw_facts(collected_facts)
    assert hw_facts.get('model') == 'ia64 hp server rx2800 i2'

# Generated at 2022-06-13 00:47:55.182730
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    """
    To test the method get_memory_facts of the class HPUXHardware
    """
    module = AnsibleModule(argument_spec={})
    obj = HPUXHardware(module)
    collected_facts = {'ansible_architecture': 'ia64',
                       'ansible_distribution': 'HP-UX',
                       'ansible_distribution_file_parsed': True,
                       'ansible_distribution_file_path': '/etc/release',
                       'ansible_distribution_release': 'B.11.31',
                       'ansible_distribution_version': 'B.11.31',
                       'ansible_hostname': 'myserver',
                       'ansible_system': 'HP-UX'
                       }

# Generated at 2022-06-13 00:48:16.380050
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    class MockModule(object):
        def run_command(self, command, use_unsafe_shell=False):
            return (0, '', '')

    class MockCollectedFacts(object):
        def __init__(self):
            self.ansible_architecture = 'ia64'
            self.ansible_distribution_version = 'B.11.31'

    module = MockModule()
    collected_facts = MockCollectedFacts()
    hardware_facts = HPUXHardware(module).get_memory_facts(collected_facts)
    assert hardware_facts['memfree_mb'] == 0
    assert hardware_facts['memtotal_mb'] == 0
    assert hardware_facts['swaptotal_mb'] == 0
    assert hardware_facts['swapfree_mb'] == 0
    return True

#

# Generated at 2022-06-13 00:48:25.421799
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    class MockModule(object):
        def run_command(self, cmd, use_unsafe_shell=False):
            mock_data = {"/usr/contrib/bin/machinfo | grep 'Number of CPUs'": (0, "Number of CPUs = 2", ""),
                         "/usr/contrib/bin/machinfo | grep 'processor family'": (0, "processor family = Intel(R) Itanium(R) processor", ""),
                         "ioscan -FkCprocessor | wc -l": (0, "2", "")}
            return mock_data[cmd]

    module = MockModule()

    hw = HPUXHardware(module)
    collected_facts = {'ansible_architecture': 'ia64'}

# Generated at 2022-06-13 00:48:35.716568
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=False
    )
    # FAKE FACTS
    module.exit_json({
        "ansible_architecture": "9000/800",
        "ansible_distribution": "HPUX"
    })
    hw = HPUXHardware(module)
    facts = hw.populate()
    assert 'processor_count' in facts
    assert 'processor_cores' in facts
    assert 'processor' in facts
    assert 'model' in facts
    assert 'firmware_version' in facts

    module.exit_json({
        "ansible_architecture": "9000/785",
        "ansible_distribution": "HPUX"
    })
    hw = HPUXHardware(module)


# Generated at 2022-06-13 00:48:45.620432
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    hardware = HPUXHardware()
    hardware.module = MockModule()
    hardware.module.run_command.return_value = (0, '1', '')
    hardware.fact_subset = None
    hardware.populate({'ansible_architecture': '9000/800', 'ansible_distribution': 'HP-UX'})
    assert hardware.facts['memfree_mb'] == hardware.get_memory_facts()['memfree_mb']
    assert hardware.facts['swaptotal_mb'] == hardware.get_memory_facts()['swaptotal_mb']
    assert hardware.facts['swapfree_mb'] == hardware.get_memory_facts()['swapfree_mb']
    assert hardware.facts['memtotal_mb'] == hardware.get_memory_facts()['memtotal_mb']
    assert hardware

# Generated at 2022-06-13 00:48:59.259515
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    cpu_facts = HPUXHardware(dict(ansible_architecture='9000/800',
                                  ansible_distribution='HP-UX')).get_cpu_facts()
    assert cpu_facts['processor'] == 'HP-UX PA-RISC 2.0'
    assert cpu_facts['processor_cores'] == 1
    assert cpu_facts['processor_count'] == 1
    # for ia64 systems
    cpu_facts = HPUXHardware(dict(ansible_architecture='ia64',
                                  ansible_distribution='HP-UX',
                                  ansible_distribution_version='B.11.31')).get_cpu_facts()
    assert cpu_facts['processor_cores'] == 1
    assert cpu_facts['processor_count'] == 1
    # for ia64 systems
    cpu

# Generated at 2022-06-13 00:49:08.593742
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    import sys
    import types

    class Module(object):
        def __init__(self):
            self.run_command = types.MethodType(fake_run_command, self)


# Generated at 2022-06-13 00:49:17.892771
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    from ansible.module_utils.facts.hardware.hpux import HPUXHardware
    class module:
        def __init__(self):
            self.params = dict()

        def fail_json(self, *args, **kwargs): pass

    m = module()
    hw = HPUXHardware(module=m)
    collected_facts = {'ansible_architecture': 'ia64',
                       'ansible_distribution_version': 'B.11.23'}
    hw_facts = hw.get_hw_facts(collected_facts=collected_facts)
    assert hw_facts['firmware_version'] == '2009.11.20'

# Generated at 2022-06-13 00:49:19.573422
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hw = HPUXHardwareCollector()
    assert hw.required_facts == set(['platform', 'distribution'])


# Generated at 2022-06-13 00:49:27.181664
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():

    import sys

    my_class = HPUXHardware()
    my_class.module = sys.modules["ansible.module_utils.facts.hardware.hpux"]

    my_class.module.run_command = lambda x: (0, '', '')

    assert my_class.get_memory_facts() == {'memfree_mb': 0, 'memtotal_mb': 0, 'swaptotal_mb': 0, 'swapfree_mb': 0}

# Generated at 2022-06-13 00:49:31.383615
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    hw = HPUXHardware()

    collected_facts = {'ansible_architecture': 'ia64',
                       'ansible_distribution_version': 'B.11.23'}

    hw.get_hw_facts(collected_facts)

# Generated at 2022-06-13 00:49:48.245106
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    # Test for HPUXHardwareCollector
    inst = HPUXHardwareCollector()
    assert isinstance(inst, HPUXHardwareCollector)
    assert inst._platform == 'HP-UX'

# Generated at 2022-06-13 00:49:57.970912
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    # Check that facts don't change for these two cases.
    # Note that syslog is a real file and /dev/kmem is a dummy file for testing.
    # Both are valid cases for the class.
    mem_fact_outputs = {
        "grep Physical /var/adm/syslog/syslog.log":
            "[FATAL] Physical: 62336000 Kbytes\n",
        "echo 'phys_mem_pages/D' | adb -k /stand/vmunix /dev/kmem | tail -1 | awk '{print $2}'":
            "1766256"
    }
    collector = HPUXHardwareCollector(dict(), dict(), mem_fact_outputs)
    facts = collector.collect(dict(), dict())
    assert facts['memtotal_mb'] == 60308
   

# Generated at 2022-06-13 00:50:08.360024
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec={})
    # Test complex case: B.11.23 IA64 /usr/contrib/bin/machinfo
    collected_facts = {'ansible_architecture': 'ia64', 'ansible_distribution_version': "B.11.23"}
    cpu_facts = HPUXHardware(module, collected_facts=collected_facts).get_cpu_facts()
    assert cpu_facts['processor_count'] == 2
    assert cpu_facts['processor'] == 'Intel(R) Itanium(R) 2 processor 9300 series'
    assert cpu_facts['processor_cores'] == 2
    # Test simple case: 9000/785
    collected_facts = {'ansible_architecture': '9000/785'}

# Generated at 2022-06-13 00:50:15.440416
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    hw_facts = {'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.23'}
    hardware = HPUXHardware()
    hardware.module = MockAnsibleModule(hw_facts=hw_facts)

    expected_hw_facts = {
        'firmware_version': "HPD2",
        'model': "ia64 hp server rx2620",
        'product_serial': None
    }
    hw_facts = hardware.get_hw_facts()
    assert hw_facts == expected_hw_facts



# Generated at 2022-06-13 00:50:24.348959
# Unit test for method get_memory_facts of class HPUXHardware

# Generated at 2022-06-13 00:50:26.752789
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hwc = HPUXHardwareCollector()
    assert hwc.__class__.__name__ == 'HPUXHardwareCollector'
    assert hwc.fact_class == HPUXHardware
    assert hwc.platform == 'HP-UX'

# Generated at 2022-06-13 00:50:30.181953
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    ansible_module = AnsibleModule(argument_spec={}, supports_check_mode=False)
    test_HPUXHardwareCollector = HPUXHardwareCollector(ansible_module=ansible_module)
    assert test_HPUXHardwareCollector._platform == 'HP-UX'

# Generated at 2022-06-13 00:50:40.638028
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():

    for (key, value) in (('architecture', '9000/800'),
                         ('architecture', '9000/785')):
        collected_facts = {'ansible_' + key: value}
        cpu_facts = HPUXHardware(collected_facts).get_cpu_facts(collected_facts=collected_facts)
        assert cpu_facts['processor_count'] == 2
        if value == '9000/785':
            assert cpu_facts['processor'] == 'CPU: 9000/785/Model JX'

    for (key, value) in (('architecture', 'ia64'),):
        collected_facts = {'ansible_' + key: value, 'ansible_distribution_version': 'B.11.31'}
        cpu_facts = HPUXHardware(collected_facts).get

# Generated at 2022-06-13 00:50:44.077662
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    # Arrange
    h = HPUXHardware()
    h.module = MagicMock()
    h.module.run_command = MagicMock(return_value=(0, '1', ''))
    # Act
    h.populate()
    # Assert
    assert h.facts['memtotal_mb'] == hs.memtotal_mb

# Generated at 2022-06-13 00:50:49.627849
# Unit test for constructor of class HPUXHardwareCollector

# Generated at 2022-06-13 00:51:12.010689
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    # initialization
    module = AnsibleModuleMock()
    module.run_command = run_command
    hardware = HPUXHardware(module=module)
    collected_facts = {'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.23'}
    # test
    hw_facts = hardware.get_hw_facts(collected_facts)
    assert hw_facts['model'] == 'ia64 hp server rx2800 i2'
    assert hw_facts['firmware_version'] == 'B.11.23.0207.2741'
    collected_facts = {'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.31'}

# Generated at 2022-06-13 00:51:19.989609
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    module = AnsibleModule(argument_spec={})

    mock_run_command = MagicMock(return_value=(0, '123', ''))
    mock_get_file_content = MagicMock(return_value='{"ansible_architecture": "ia64"}')
    mock_mkdtemp = MagicMock(return_value='/tmp/ansible_facts.d')
    mock_file = MagicMock(spec=file)
    mock_file.return_value = MagicMock(spec=file)
    mock_file.side_effect = [(mock_file.return_value, None), (mock_file.return_value, None),
                             (mock_file.return_value, None)]
    mock_open = MagicMock(return_value=mock_file)

# Generated at 2022-06-13 00:51:22.401607
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hardware_collector = HPUXHardwareCollector()
    assert hardware_collector._platform == 'HP-UX'
    assert hardware_collector.required_facts == set(['platform', 'distribution'])

# Generated at 2022-06-13 00:51:24.073748
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    fact_class = HPUXHardwareCollector(None, None, None)
    assert fact_class.required_facts == set(['platform', 'distribution'])



# Generated at 2022-06-13 00:51:26.567027
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    """
    Test constructor of class HPUXHardwareCollector.
    """
    rh = HPUXHardwareCollector({'platform': 'HP-UX'})
    assert rh.platform == 'HP-UX'
    assert rh._fact_class == HPUXHardware



# Generated at 2022-06-13 00:51:28.347426
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hc = HPUXHardwareCollector({}, object())
    assert hc.__class__.__name__ == 'HPUXHardwareCollector'

# Generated at 2022-06-13 00:51:38.521759
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    class MockModule:
        def __init__(self):
            self.run_command_line = ''
            self.run_command = ''

    class MockFacts:
        def __init__(self):
            self.ansible_architecture = ''
            self.ansible_distribution_version = ''

    class MockHardware:
        def __init__(self):
            self.facts = MockFacts()

    hw = HPUXHardware()
    hw.module = MockModule()
    hw.module.run_command = lambda a, b: (0, '', '')
    hw.populate()

    # Test model
    hw.module.run_command = lambda a, b: (0, '9000/800', '')
    hw.populate()

    # Test firmware
    h

# Generated at 2022-06-13 00:51:47.057059
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    class FakeModule:
        def __init__(self, *args, **kwargs):
            pass

        def run_command(self, cmd, use_unsafe_shell=False):
            if cmd == "ioscan -FkCprocessor | wc -l":
                return 0, "2", ""
            elif cmd == "ioscan -FkCprocessor | wc -l":
                return 0, "3", ""
            elif cmd == "/usr/contrib/bin/machinfo | egrep 'socket[s]?$' | tail -1":
                return 0, "2", ""
            elif cmd == "/usr/contrib/bin/machinfo | grep Intel |cut -d' ' -f4-":
                return 0, "Intel(r) Itanium(r) Processor 9350", ""

# Generated at 2022-06-13 00:51:51.918722
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    module = AnsibleModule(argument_spec={})
    facts = module.exit_json(ansible_facts={'ansible_architecture': 'ia64'})
    hw_c = HPUXHardwareCollector()
    obj = hw_c.collect(facts=facts['ansible_facts'], hidden_facts={})
    obj.populate()
    assert type(obj) == HPUXHardware
    assert obj.platform == 'HP-UX'


# Generated at 2022-06-13 00:51:54.748097
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hw_collector = HPUXHardwareCollector()
    assert hw_collector
    assert isinstance(hw_collector, HardwareCollector)
    assert hw_collector._fact_class == HPUXHardware
    assert hw_collector._platform == 'HP-UX'
    assert hw_collector.required_facts == set(['platform', 'distribution'])

# Generated at 2022-06-13 00:52:15.313242
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    module = FakeAnsibleModule()
    hardware = HPUXHardware(module)
    facts = hardware.populate({'ansible_architecture': '9000/800'})
    assert facts['processor'] == 'HP-PA rp2470'
    assert facts['processor_cores'] == 2
    assert facts['processor_count'] == 2
    assert facts['processor_threads_per_core'] == 1


# Generated at 2022-06-13 00:52:22.561378
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec={})
    hardware_facts = HPUXHardware(module=module)
    collected_facts = {'ansible_architecture': '9000/800',
                       'ansible_distribution_version': 'B.11.31'}
    cpu_facts = hardware_facts.get_cpu_facts(collected_facts)
    assert cpu_facts == {'processor_count': 2, 'processor_cores': 4, 'processor': 'Intel(R) Itanium(R) processor 9650'}

    # Unit test for method get_memory_facts of class HPUXHardware
    def test_HPUXHardware_get_memory_facts():
        module = AnsibleModule(argument_spec={})

        hardware_facts = HPUXHardware(module=module)

# Generated at 2022-06-13 00:52:30.585268
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    hw = HPUXHardware()
    hw.module = FakeModule()
    hw.module.run_command = run_command
    hw.module.run_command.side_effect = (('0', '', ''), ('', '', 'error'), ('0', '', ''), ('0', '', ''))

    facts = hx.get_memory_facts()
    assert facts['memfree_mb'] == 32
    assert facts['memtotal_mb'] == 0
    assert facts['swaptotal_mb'] == 0
    assert facts['swapfree_mb'] == 0

    hw.module.run_command.side_effect = (('0', '', ''), ('', '', ''), ('0', '', ''), ('0', '', ''))

    facts = hx.get_memory_facts()

# Generated at 2022-06-13 00:52:32.582655
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    from ansible.module_utils.facts.collector.hpux import HPUXHardware
    module = HPUXHardware()
    module.module = FakeModule()
    module.module.run_command.return_value = (0, None, None)
    module.module.params = {}
    module.populate()


# Generated at 2022-06-13 00:52:39.946224
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    module = AnsibleModule(argument_spec=dict())
    func_name = 'ansible.module_utils.facts.hardware.hpux.HPUXHardware.get_hw_facts'
    facts_module = 'ansible.module_utils.facts.hardware.hpux'

    # Patch AnsibleModule
    am = AnsibleModule
    AnsibleModule = MagicMock()
    instance = MagicMock()
    AnsibleModule.return_value = instance
    instance.params = None
    instance.run_command.return_value = (0, "model 9000/800\n", None)

    # Patch load_platform_subclass
    lps = ('ansible.module_utils.facts.hardware.hpux.HPUXHardwareCollector'
           '.load_platform_subclass')

# Generated at 2022-06-13 00:52:49.889281
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    from collections import namedtuple
    from ansible_collections.community.general.plugins.module_utils.facts.facts import Facts
    FakeCollectedFacts = namedtuple(
        'FakeCollectedFacts',
        ['ansible_architecture', 'ansible_distribution_version'])
    _hw = HPUXHardware({})
    module = FakeModuleMock()
    _hw.module = module
    _hw.get_hw_facts(FakeCollectedFacts(ansible_architecture='ia64',
                                        ansible_distribution_version='B.11.23'))
    cmd = module.run_command.call_args_list[0][0][0]
    assert cmd == "model"
    cmd = module.run_command.call_args_list[1][0][0]
   

# Generated at 2022-06-13 00:52:56.170512
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    hardware = HPUXHardware()
    collected_facts = {'ansible_architecture': '9000/800', 'ansible_distribution_version': 'B.11.31'}
    # PA_RISC
    cpu_facts = hardware.get_cpu_facts()
    assert cpu_facts.get('processor_count') == 8
    assert cpu_facts.get('processor_cores') == 8
    assert cpu_facts.get('processor') == '800'
    # Itanium
    collected_facts = {'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.23'}
    cpu_facts = hardware.get_cpu_facts()
    assert cpu_facts.get('processor_cores') == 8
    assert cpu_facts.get('processor_count') == 1

# Generated at 2022-06-13 00:53:01.897666
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    collected_facts = {'platform': 'HP-UX', 'ansible_distribution_version': 'B.11.23'}
    hardware_obj = HPUXHardware(module=None)
    data = hardware_obj.get_hw_facts(collected_facts=collected_facts)

    assert data['model'] == 'ia64 hp server rx2800 i4'
    assert data['firmware_version'] == 'B.11.23'

# Generated at 2022-06-13 00:53:05.116599
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    module = AnsibleModule(
        argument_spec=dict(),
    )

    h = HPUXHardware(module=module)

    assert h.get_memory_facts() == {}



# Generated at 2022-06-13 00:53:09.102227
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    module = AnsibleMockModule()
    module.run_command = Mock(return_value=(0, "1", ""))
    hw = HPUXHardware(module=module)
    assert hw.get_memory_facts() == {'memtotal_mb': 0, 'memfree_mb': 1, 'swaptotal_mb': 0, 'swapfree_mb': 0}

# Generated at 2022-06-13 00:53:51.008209
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hw_facts = HPUXHardwareCollector()
    assert isinstance(hw_facts, HardwareCollector)
    assert hw_facts.platform == 'HP-UX'
    assert hw_facts.required_facts == set(['platform', 'distribution'])


# Generated at 2022-06-13 00:53:51.515970
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    HPUXHardwareCollector()

# Generated at 2022-06-13 00:53:58.046689
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    collected_facts = dict(platform="HP-UX", distribution="B.11.00")
    module = FakeAnsibleModule()
    hw_facts = HPUXHardware(module).get_hw_facts(collected_facts=collected_facts)
    assert hw_facts['model'] == 'hp 9000/800 k370'
    assert hw_facts['firmware_version'] == 'HPUX'



# Generated at 2022-06-13 00:53:58.879072
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    return


# Generated at 2022-06-13 00:54:05.370708
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    module = MockModule()
    hardware = HPUXHardware(module)
    hardware.module.run_command = Mock(return_value=(0, 'ia64 rx7620', ''))
    hardware.module.run_command = Mock(return_value=(0, 'B.11.31', ''))
    hw_facts = hardware.get_hw_facts()
    assert hw_facts['model'] == 'ia64 rx7620'
    assert hw_facts['firmware_version'] == '4.88'
    # Test for machine without serial
    hardware.module.run_command = Mock(return_value=(1, '', ''))
    hw_facts = hardware.get_hw_facts()
    assert 'product_serial' not in hw_facts.keys()



# Generated at 2022-06-13 00:54:11.894592
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    module = AnsibleModuleStub(
        dict(
            ansible_facts=dict(
                ansible_architecture='9000/800'
            )
        )
    )
    hw = HPUXHardware(module)
    assert hw.get_memory_facts() == dict(
        memtotal_mb=3932,
        memfree_mb=1596,
        swaptotal_mb=10240,
        swapfree_mb=10240
    )



# Generated at 2022-06-13 00:54:19.976725
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    """
    Unit test for method populate of class HPUXHardware
    """

    collected_facts = {
        "ansible_architecture": "9000/785",
        "ansible_distribution_version": "B.11.31",
        "platform": "HP-UX",
        "ansible_distribution": "HP-UX"
    }

    hardware_data = HPUXHardware(None, collected_facts).populate()
    assert hardware_data['processor_cores'] == 8
    assert hardware_data['processor_count'] == 2
    assert hardware_data['processor'] == 'Intel(R) Itanium(R) Processor'
    assert hardware_data['memtotal_mb'] == 2048
    assert hardware_data['memfree_mb'] == 539
    assert hardware_data['swapfree_mb'] == 25

# Generated at 2022-06-13 00:54:27.505706
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    HPUXhw_facts = HPUXHardware(dict(ansible_facts={
                                                    'platform': 'HP-UX',
                                                    'ansible_architecture': 'ia64',
                                                    'ansible_distribution_version': 'B.11.31',
                                                    }
                                    ), mock.MagicMock()).populate()
    assert 'model' in HPUXhw_facts
    assert 'firmware_version' in HPUXhw_facts
    assert 'product_serial' in HPUXhw_facts
    assert 'memfree_mb' in HPUXhw_facts
    assert 'memtotal_mb' in HPUXhw_facts
    assert 'swapfree_mb' in HPUXhw_facts
    assert 'swaptotal_mb' in HPUXhw_facts


# Generated at 2022-06-13 00:54:31.781500
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hwcollector = HPUXHardwareCollector()
    assert hwcollector.__class__.__name__ == 'HPUXHardwareCollector'
    assert hwcollector._fact_class.__name__ == 'HPUXHardware'
    assert hwcollector._platform == 'HP-UX'
    assert hwcollector._required_facts == set(['platform', 'distribution'])


# Generated at 2022-06-13 00:54:35.344286
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hardware_collector = HPUXHardwareCollector(module=dict())
    assert hardware_collector._platform == 'HP-UX'
    assert hardware_collector._fact_class.platform == 'HP-UX'
    assert hardware_collector.required_facts == set(['platform', 'distribution'])