

# Generated at 2022-06-13 00:45:32.115373
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    module = AnsibleModule(argument_spec={})
    module.params = dict(gather_subset='all')
    hpu = HPUXHardware(module)

    rc, out, err = hpu.module.run_command("uname -srm")
    data = out.strip().split(' ')
    facts = dict(
        ansible_architecture=data[2],
        ansible_distribution=data[0],
        ansible_distribution_version=data[1]
    )

    hpu.populate(collected_facts=facts)
    hw_facts = hpu.platform_facts

    assert hw_facts['processor'] == "Intel(R) Xeon(R) CPU E7-4870 0 @ 2.40GHz"
    assert hw_facts['processor_cores'] == 40

# Generated at 2022-06-13 00:45:33.296110
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hc = HPUXHardwareCollector()
    assert hc.collect() == dict()

# Generated at 2022-06-13 00:45:38.903512
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    module = args = mock.MagicMock()
    module.run_command.return_value = (0, "0", "")
    collected_facts = {'ansible_architecture': '9000/800', 'ansible_distribution_version': 'B.11.31'}
    hw = HPUXHardware(module)
    assert hw.get_memory_facts(collected_facts=collected_facts) == {'memfree_mb': 0, 'memtotal_mb': 16384, 'swapfree_mb': 0, 'swaptotal_mb': 0}
    module.run_command.assert_called_once_with("/usr/bin/vmstat | tail -1", use_unsafe_shell=True)



# Generated at 2022-06-13 00:45:49.878054
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    facts = {
        'platform': 'HP-UX',
        'distribution': 'HP-UX',
        'architecture': 'ia64'
    }
    module = Mock(
        run_command=Mock(return_value=(0, '', '')),
        params=dict()
    )

    hphw = HPUXHardwareCollector(module=module, facts=facts).collect()[0]

    hphw.get_memory_facts()

    assert hphw.memory['memfree_mb']
    assert hphw.memory['memtotal_mb']
    assert hphw.memory['swaptotal_mb']
    assert hphw.memory['swapfree_mb']



# Generated at 2022-06-13 00:46:00.065041
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    hardware = HPUXHardware(dict(ansible_architecture='9000/800', ansible_distribution_version='B.11.31'))
    rc, out, err = hardware.module.run_command("echo -e '48CPUs=1536 Logical Processors\n2 Hyperthreading OPs\n8 cores per socket' | /usr/contrib/bin/machinfo", use_unsafe_shell=True)
    collected_facts = {'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.31'}
    cpu_facts = hardware.get_cpu_facts(collected_facts=collected_facts)
    assert cpu_facts['processor_count'] == 48
    assert cpu_facts['processor'] == "Intel Itanium 2 'McKinley'"
   

# Generated at 2022-06-13 00:46:10.667586
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    test_module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True,
    )
    test_hw_facts = HPUXHardwareCollector(test_module)
    my_facts = test_hw_facts.collect()
    # assert memtotal_mb > 0
    assert my_facts['ansible_memtotal_mb'] > 0
    # assert swapfree_mb > 0
    assert my_facts['ansible_swapfree_mb'] > 0
    # assert swapfree_mb < swaptotal_mb
    assert my_facts['ansible_swapfree_mb'] < my_facts['ansible_swaptotal_mb']
    # assert memfree+swapfree=memtotal+swaptotal

# Generated at 2022-06-13 00:46:15.508804
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hardware_collector = HPUXHardwareCollector()

    assert hardware_collector._fact_class == HPUXHardware
    assert hardware_collector._platform == 'HP-UX'
    assert hardware_collector.required_facts == set(['platform', 'distribution'])

# Generated at 2022-06-13 00:46:25.205970
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    test_object = HPUXHardware()
    collected_facts = {'distribution': 'HP-UX', 'architecture': 'ia64', 'distribution_version': 'B.11.31'}
    result = test_object.get_memory_facts(collected_facts)
    assert type(result) is dict
    assert 'memfree_mb' in result
    assert 'memtotal_mb' in result
    assert 'swaptotal_mb' in result
    assert 'swapfree_mb' in result
    assert type(result['memfree_mb']) is int
    assert type(result['memtotal_mb']) is int
    assert type(result['swaptotal_mb']) is int
    assert type(result['swapfree_mb']) is int



# Generated at 2022-06-13 00:46:35.420816
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    """
    This is a unit-test to check the get_hw_facts of the class HPUXHardware.
    """
    # TODO: This unit test is only a first draft. It needs to be extended to check all
    #       possible return values of get_hw_facts in class HPUXHardware.

    # Create a fake module class to be able to mock subprocess.run
    class FakeModule:

        def run_command(cmd, use_unsafe_shell=False):
            """
            Method run_command is mocked to be able to test different return values.
            """
            # TODO: This is only a first draft. It needs to be extended to cover all the
            #       different expected return values of run_command.


# Generated at 2022-06-13 00:46:45.712472
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    hardware = HPUXHardware({'system_vendor': 'HP', 'ansible_distribution': 'HP-UX', 'ansible_distribution_version': 'B.11.23',
                             'ansible_architecture': 'ia64'})

    hw_facts = hardware.get_hw_facts()

    assert hw_facts['model'] == 'ia64 hp rx2620'
    assert hw_facts['firmware_version'] == 'B.11.23'
    assert hw_facts['product_serial'].startswith('CN')

    hardware = HPUXHardware({'system_vendor': 'HP', 'ansible_distribution': 'HP-UX', 'ansible_distribution_version': 'B.11.31',
                             'ansible_architecture': 'ia64'})

# Generated at 2022-06-13 00:47:04.210598
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    # Fact collection is platform dependent, so a subclass of Hardware must be tested.
    hpux_hw = HPUXHardware()


# Generated at 2022-06-13 00:47:13.220288
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    my_test_class = HPUXHardware()
    my_test_class.module = FakeAnsibleModule()
    my_test_facts = {'ansible_architecture': '9000/800'}
    my_test_facts_result = {'memfree_mb': 449,
                            'memtotal_mb': 3655,
                            'swapfree_mb': 675,
                            'swaptotal_mb': 675}
    my_test_class.module.run_command.return_value = (0, '543', '')
    my_test_class.get_cpu_facts = lambda: []
    assert (my_test_class.get_memory_facts(my_test_facts) ==
            my_test_facts_result)



# Generated at 2022-06-13 00:47:19.157011
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    """
    This test case verify if the method get_hw_facts of class HPUXHardware return correct value
    """
    myHPUXHardware = HPUXHardware({})
    collected_facts = {'ansible_architecture': 'ia64',
                       'ansible_distribution_version': 'B.11.23',
                       'ansible_module_name': 'setup',
                       'ansible_module_version': '2.0.0.0',
                       'ansible_platform': 'HP-UX',
                       'ansible_system': 'HP-UX',
                       'ansible_system_vendor': 'Hewlett-Packard'}
    assert myHPUXHardware.get_hw_facts(collected_facts)['firmware_version'] == '0x6379'

# Generated at 2022-06-13 00:47:21.639545
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    hw_hpux = HPUXHardware()
    hpux_cpu_facts = hw_hpux.get_cpu_facts()
    assert hpux_cpu_facts.get('processor_cores') == 8


# Generated at 2022-06-13 00:47:31.361726
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    test_module = AnsibleModule(argument_spec=dict())
    test_HPUXHardware = HPUXHardware(test_module)

    test_collected_facts = {'ansible_architecture': '9000/800', 'ansible_distribution': 'HP-UX'}
    result_dict = test_HPUXHardware.get_cpu_facts(test_collected_facts)

    assert result_dict['processor_count'] == 2
    assert result_dict['processor'] == 'Intel(R) Itanium(R) 9100 series processor @ 1.60GHz'
    assert result_dict['processor_cores'] == 2


# Generated at 2022-06-13 00:47:34.591773
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    """
    Test constructor of the HPUXHardwareCollector Class.
    """
    hardware_collector = HPUXHardwareCollector()
    assert hardware_collector.fact_class == HPUXHardware
    assert hardware_collector.platform == 'HP-UX'



# Generated at 2022-06-13 00:47:42.933782
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    hw = HPUXHardware({})

    # We need to mock the facts
    hw.module.run_command = Mock(return_value=[0, '', ''])
    hw.module.get_bin_path = Mock(return_value='/bin/true')

    collected_facts = {
        'ansible_architecture': '9000/800',
        'ansible_distribution_version': 'B.11.23',
    }

    cpu_facts = hw.get_cpu_facts(collected_facts=collected_facts)
    assert cpu_facts['processor_count'] == 32

    collected_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.23',
    }


# Generated at 2022-06-13 00:47:47.704842
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    FakeModule = type('FakeModule', (object,), {
        'run_command': lambda x: (0, 'fake_model\n', None)
    })
    hardware_fact = HPUXHardware(FakeModule)
    assert hardware_fact.get_hw_facts() == {'model': 'fake_model'}

# Generated at 2022-06-13 00:47:48.881007
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hc = HPUXHardwareCollector()
    assert hc.required_facts == set(['platform', 'distribution'])
    assert hc._platform == 'HP-UX'

# Generated at 2022-06-13 00:47:59.249274
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    failed_msg = "The method 'get_cpu_facts' of class HPUXHardware does not work as expected."

    # Test collect the file /var/adm/syslog/syslog.log exists
    module = AnsibleModule(argument_spec={})
    module.run_command = MagicMock(return_value=(0, 'Physical: 1234 Kbytes', None))
    hpux_hw = HPUXHardware(module)

    collected_facts = {'ansible_architecture': '9000/800'}
    expected = {'processor_count': 1}
    actual = hpux_hw.get_cpu_facts(collected_facts=collected_facts)

    assert actual == expected, failed_msg

    # Test collect the file /var/adm/syslog/syslog.log does not exists

# Generated at 2022-06-13 00:48:11.287031
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    # given
    class MockModule:
        pass
    module = MockModule()
    module.run_command = _run_command
    # when
    hw = HPUXHardware(module)
    cpu_facts = hw.get_cpu_facts(collected_facts=_collected_facts_for_get_cpu_facts)
    # then
    expected_facts = {
        'processor': 'Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz',
        'processor_cores': 32,
        'processor_count': 2
    }
    assert cpu_facts == expected_facts



# Generated at 2022-06-13 00:48:15.482390
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    """ Test constructor of class HPUXHardwareCollector """

    hw = HPUXHardwareCollector()
    assert hw != None
    assert hw._fact_class == HPUXHardware
    assert hw._platform == "HP-UX"
    assert hw.required_facts == set(['platform', 'distribution'])

# Generated at 2022-06-13 00:48:24.389020
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    hw = HPUXHardware({'module': None})
    assert hw.get_cpu_facts() == {}
    assert hw.get_cpu_facts({'ansible_architecture': '9000/800'}) == {}
    assert hw.get_cpu_facts({'ansible_architecture': '9000/800', 'ansible_distribution_version': 'B.11.31'}) == {}
    assert hw.get_cpu_facts({'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.23'}) == {}
    assert hw.get_cpu_facts({'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.31'}) == {}

# Generated at 2022-06-13 00:48:31.908483
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    facts = HPUXHardware()
    facts.module.run_command = lambda x: (0, 'HP rp3440 Server', '')
    facts.module.get_bin_path = lambda x: 'model'

    facts.get_hw_facts({'platform': 'HP-UX', 'distribution': 'HP-UX'})

    assert facts.facts['model'] == 'HP rp3440 Server'



# Generated at 2022-06-13 00:48:33.099965
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 00:48:43.258793
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    hardware = HPUXHardware({'platform': 'HP-UX', 'distribution': 'B.11.23'})
    rc, out, err = hardware.module.run_command('model')
    assert out.strip() == hardware.get_hw_facts()['model']
    rc, out, err = hardware.module.run_command('/usr/contrib/bin/machinfo |grep -i "Firmware revision" | grep -v BMC')
    assert out.strip().split('=')[1].strip() == hardware.get_hw_facts()['firmware_version']
    rc, out, err = hardware.module.run_command('/usr/contrib/bin/machinfo |grep -i "Machine serial number" ')

# Generated at 2022-06-13 00:48:55.648030
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    hardware = HPUXHardware({'module_utils': 'dummy', 'ansible_module': 'dummy'})
    hardware.module.run_command = run_command_mock
    hardware.module.run_command.commands = {
        'model': "IA64 hp rx2620",
        '/usr/contrib/bin/machinfo | grep -i \'Firmware revision\' | grep -v BMC': 'Firmware revision=1.1',
        '/usr/contrib/bin/machinfo | grep -i \'Machine serial number\' ': 'Machine serial number=US_00000',
    }

    collected_facts = {}
    collected_facts['ansible_architecture'] = 'ia64'
    collected_facts['ansible_distribution_version'] = 'B.11.23'

    hardware_facts

# Generated at 2022-06-13 00:49:05.611982
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    # test if tcsu is loaded and ansible_hp_ux_version is present
    test_collected_facts = {
        'distribution': 'HP-UX',
        'architecture': 'ia64',
        'distribution_version': 'B.11.31',
    }

    hw = HPUXHardwareCollector(None, test_collected_facts).collect()[0]
    assert hw.platform == 'HP-UX'
    assert hw['processor_cores'] == 32
    assert hw['processor_count'] == 2

    test_collected_facts = {
        'distribution': 'HP-UX',
        'distribution_version': 'B.11.11',
        'architecture': '9000/800',
    }

# Generated at 2022-06-13 00:49:14.693700
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    module = AnsibleModule(argument_spec={})
    hardware = HPUXHardware(module)

    # Test populate without collected_facts parameter
    facts = hardware.populate()
    assert 'processor_cores' in facts
    assert 'memtotal_mb' in facts

    # Test populate with collected_facts parameter
    collected_facts = dict(ansible_architecture='9000/800', ansible_distribution_version='B.11.31')
    facts = hardware.populate(collected_facts=collected_facts)
    assert 'processor_cores' in facts
    assert 'memtotal_mb' in facts
    assert facts['memtotal_mb'] == 16
    # Test populate with collected_facts parameter

# Generated at 2022-06-13 00:49:18.304590
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hw = HPUXHardwareCollector()
    assert isinstance(hw, HPUXHardwareCollector)
    assert hw._fact_class == HPUXHardware
    assert hw._platform == 'HP-UX'
    assert hw.required_facts == set(['platform', 'distribution'])

# Generated at 2022-06-13 00:49:42.351454
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    from ansible.module_utils.facts.hardware.hpuxtest import MockModule
    mock_module = MockModule()
    for dist in ['11.31', '11.23']:
        for arch in ['ia64', '9000/800']:
            for version in ['B.11.23', 'B.11.31']:
                data = 'uname -a && /usr/sbin/swapinfo -m -d -f && /usr/bin/vmstat'
                if arch == 'ia64':
                    data += ' && /usr/contrib/bin/machinfo'
                data += " && echo 'HP-UX' && echo %s && echo %s" % (dist, version)
                rc, out, err = mock_module.run_command(data, use_unsafe_shell=True)
               

# Generated at 2022-06-13 00:49:52.739123
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    module = None
    collected_facts = None
    hw = HPUXHardware(module=module)

    # HP9000/800
    collected_facts = {'ansible_architecture': '9000/800'}
    cpu_facts = hw.get_cpu_facts(collected_facts=collected_facts)
    assert cpu_facts == {'processor_count': 1}

    # HP9000/785
    collected_facts = {'ansible_architecture': '9000/785'}
    cpu_facts = hw.get_cpu_facts(collected_facts=collected_facts)
    assert cpu_facts == {'processor_count': 1}

    # HP-UX IA64 B.11.23

# Generated at 2022-06-13 00:50:00.592219
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    sample_output1 = '''
 Memory: Total Physical = 12288 MB, Available Physical = 0 MB, Total Swap = 139268 MB, Swap in use = 0 MB, Virtual = 141560 MB, Unused Virtual = 0 MB
'''
    sample_output2 = '''
 Physical: 8387928 Kbytes Logical: 8387928 Kbytes
'''
    sample_output3 = '''
    Memory =  37920 MB
'''
    sample_output4 = '''
    phys_mem_pages/D
    252384
'''
    sample_output5 = '''
    Memory =  8192 MB
'''
    sample_output6 = '''
    Memory =  1200 MB
'''
    sample_output7 = '''
    Memory =  2048 MB
'''

# Generated at 2022-06-13 00:50:10.854116
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    """
    Unit test for class HPUXHardware.
    """
    import pytest
    from ansible.module_utils.facts.hardware.hpux import HPUXHardware

    hw = HPUXHardware(module=None)
    collected_facts = {'ansible_architecture': "9000/800",
                       'ansible_distribution': "HP-UX",
                       'ansible_distribution_version': "B.11.11"}
    memory_facts = hw.get_memory_facts(collected_facts)
    assert memory_facts
    assert memory_facts['memtotal_mb']

    collected_facts = {'ansible_architecture': "ia64",
                       'ansible_distribution': "HP-UX",
                       'ansible_distribution_version': "B.11.23"}

# Generated at 2022-06-13 00:50:17.798534
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    module = HPUXHardware(dict(ANSIBLE_MODULE_ARGS={}))
    module.populate({})
    assert module.facts['processor'] != ''
    assert module.facts['processor_cores'] != ''
    assert module.facts['processor_count'] != ''
    assert module.facts['model'] != ''
    assert module.facts['firmware_version'] != ''
    assert module.facts['memfree_mb'] != ''
    assert module.facts['memtotal_mb'] != ''
    assert module.facts['swaptotal_mb'] != ''
    assert module.facts['swapfree_mb'] != ''

# Generated at 2022-06-13 00:50:25.234020
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=['!all', '!min'], type='list'),
        ),
    )
    hardware = HPUXHardware(module)
    collected_facts = {'ansible_architecture': '9000/800', 'ansible_distribution_version': 'B.11.23'}
    hardware.get_cpu_facts(collected_facts)
    expected_results = {'processor_count': 1}
    assert hardware.populate() == expected_results

# Generated at 2022-06-13 00:50:30.102244
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=['all'], required=False)
        )
    )
    hardware = HPUXHardware()
    module.exit_json(ansible_facts={'ansible_hw_facts': hardware.populate()})



# Generated at 2022-06-13 00:50:40.555421
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    hardware = HPUXHardware()
    collected_facts = {'ansible_architecture': '9000/785'}

    hardware.module = MockModule({})
    hardware.module.run_command = Mock(return_value=(0, '2', None))

    cpu_facts = hardware.get_cpu_facts(collected_facts=collected_facts)

    assert cpu_facts['processor_count'] == 2
    assert cpu_facts['processor_cores'] is None
    assert cpu_facts['processor'] is None

    collected_facts = {'ansible_architecture': 'ia64'}
    collected_facts['ansible_distribution_version'] = 'B.11.23'
    hardware.module.run_command = Mock(return_value=(0, '2', None))
    hardware.module.run_command

# Generated at 2022-06-13 00:50:52.592686
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    hpux_hardware = HPUXHardware({})
    rc, out, err = hpux_hardware.module.run_command("/usr/contrib/bin/machinfo | grep Memory", use_unsafe_shell=True)
    mem_size = re.search(r'Memory[\ :=]*([0-9]*).*MB.*', out).groups()[0].strip()
    # Unit test for memory facts
    memory_facts = hpux_hardware.get_memory_facts(collected_facts={'ansible_architecture': 'ia64'})
    assert memory_facts['memtotal_mb'] == int(mem_size)
    assert memory_facts['memfree_mb'] >= 0
    assert memory_facts['swaptotal_mb'] >= 0

# Generated at 2022-06-13 00:50:59.388948
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    """
    Test if method get_hw_facts() of class HPUXHardware works correctly.
    """

    # The following data will be returned by method get_hw_facts()
    model = 'HP-UX B.11.31 U ia64 0193959005'
    firmware_version = '2.55'
    product_serial = 'FCH142X42P'
    # Data used to test method get_hw_facts()
    collected_facts = {
        'distribution_version': 'B.11.31',
        'architecture': 'ia64',
        'platform': 'HP-UX'
    }

    hardware = HPUXHardware()

    hardware.get_hw_facts(collected_facts)

    assert hardware.model == model
    assert hardware.firmware_version == firmware_version

# Generated at 2022-06-13 00:51:30.175707
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hardware_facts = HPUXHardwareCollector()
    assert hardware_facts.__class__.__name__ == 'HPUXHardwareCollector'
    assert hardware_facts._fact_class == HPUXHardware
    assert hardware_facts._platform == 'HP-UX'
    assert hardware_facts.required_facts == {'platform', 'distribution'}


# Generated at 2022-06-13 00:51:40.016986
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    module = type('AnsibleModule', (object,), {'run_command': run_command})

    collected_facts = {'ansible_architecture': '9000/800'}
    hardware = HPUXHardware(module)
    cpu_facts = hardware.get_cpu_facts(collected_facts=collected_facts)
    assert cpu_facts['processor_count'] == 2

    collected_facts = {'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.23'}
    hardware = HPUXHardware(module)
    cpu_facts = hardware.get_cpu_facts(collected_facts=collected_facts)
    assert cpu_facts['processor_count'] == 1
    assert cpu_facts['processor'] == 'Intel(r) Itanium 2'
   

# Generated at 2022-06-13 00:51:43.183477
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hardware_collector = HPUXHardwareCollector()
    assert hardware_collector.platform == 'HP-UX'
    assert hardware_collector.required_facts == set(['platform', 'distribution'])
    assert hardware_collector._fact_class == HPUXHardware

# Generated at 2022-06-13 00:51:49.501658
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    # enable this test
    return
    facts = dict(
        ansible_architecture='ia64',
        ansible_system='HP-UX',
        ansible_distribution='HP-UX',
        ansible_distribution_version='B.11.23'
    )
    hp_hw = HPUXHardware(dict(module=dict(run_command=lambda x, **kwargs: (0, x, None))))
    hp_hw.populate(facts)
    assert hp_hw.firmware_version == 'HPD9'

# Generated at 2022-06-13 00:51:55.286543
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    module = AnsibleModule(argument_spec={})
    hardware = HPUXHardware(module)
    assert hardware.populate() == {'processor_count': 2,
                                   'processor_cores': 1,
                                   'processor': 'Intel(R) Itanium(R) 9500 series processor @ 1.73GHz',
                                   'memfree_mb': 3968,
                                   'memtotal_mb': 10153,
                                   'swaptotal_mb': 513,
                                   'swapfree_mb': 512,
                                   'model': '9000/785/E4900',
                                   'firmware_version': 'v1.10 (OE)',
                                   'product_serial': 'PA814S6D13'}



# Generated at 2022-06-13 00:52:03.457149
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    module = FakeModule()
    module.run_command = fake_run_command
    module.params = {'_ansible_webservice_passthrough': True}

    hpux_hardware = HPUXHardware(module)
    rc, out, err = module.run_command("uname -m")
    arch = out.strip('\n')
    collected_facts = {"ansible_architecture": arch}

    facts = hpux_hardware.populate(collected_facts=collected_facts)
    assert facts['processor_count'] == 2



# Generated at 2022-06-13 00:52:05.156988
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hpux_hwclass = HPUXHardwareCollector()
    assert hpux_hwclass._fact_class == HPUXHardware
    assert hpux_hwclass._platform == 'HP-UX'

# Generated at 2022-06-13 00:52:06.677712
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hpux_hw_collector = HPUXHardwareCollector()
    assert hpux_hw_collector.required_facts == {'distribution', 'platform'}

# Generated at 2022-06-13 00:52:16.033007
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    # Test on a 9000/785
    module = AnsibleModule(argument_spec={})
    set_module_args(dict(gather_subset='all', filter='*'))
    interfaces = HPUXHardware(module=module)
    collected_facts = {'ansible_architecture': '9000/785'}
    interfaces.populate(collected_facts)
    assert interfaces.facts['memtotal_mb'] == 8944
    assert interfaces.facts['memfree_mb'] == 5053
    assert interfaces.facts['swaptotal_mb'] == 8192
    assert interfaces.facts['swapfree_mb'] == 4456
    assert interfaces.facts['processor_count'] == 2
    assert interfaces.facts['model'] == 'HP 9000/785'

# Generated at 2022-06-13 00:52:25.735743
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    def run(module, result):
        module.exit_json(**result)

    class AnsibleModule:
        def __init__(self, results):
            self.results = results

        def run_command(self, command, use_unsafe_shell=True):
            return self.results

    hpx = HPUXHardware()
    hpx.module = AnsibleModule({'ansible_architecture': '9000/800', 'ansible_distribution_version': 'B.11.31', 'ansible_facts': {}})

    model = 'Integrity rx2620'
    hpx.module.run_command = lambda x, y: (0, model, '')
    results = hpx.get_cpu_facts()
    assert results
    assert results['processor_count'] == 2

# Generated at 2022-06-13 00:52:59.075781
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    data = {}
    data['ansible_architecture'] = 'ia64'
    data['ansible_distribution_version'] = 'B.11.23'
    test_HPUX = HPUXHardware(None)
    test_HPUX.get_memory_facts(data)

# Generated at 2022-06-13 00:53:06.434052
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    module = AnsibleModule(supports_check_mode=True)
    redhat_hw = HPUXHardware()
    # if ia64 and not B.11.31
    collected_facts = {'ansible_architecture': 'ia64', 'ansible_distribution_version': "B.11.23"}
    hw_facts = dict(ansible_machine_id='', ansible_product_name='', ansible_product_serial='', ansible_system_vendor='',
                    ansible_product_uuid='', ansible_bios_version='', ansible_modalias='', ansible_product_name='',
                    ansible_firmware_version='', ansible_system_vendor='', ansible_os_family='HP-UX')
    hardware_facts = redhat_hw.get_

# Generated at 2022-06-13 00:53:11.370365
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    module = AnsibleModule(
        argument_spec={},
    )

    h = HPUXHardware(module)
    hw_facts = h.get_hw_facts()
    assert hw_facts['model'] == 'ia64 hp server rx2660'
    assert hw_facts['firmware_version'] == '3.3.3'
    assert hw_facts['product_serial'] == 'US1234567890'


# Generated at 2022-06-13 00:53:13.827845
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    args = {}
    module = AnsibleModule(argument_spec=args)
    hw = HPUXHardware(module)
    collected_facts = {'ansible_architecture': '9000/800',
                       'ansible_distribution_version': 'B.11.23'}
    hw.populate(collected_facts)


# Generated at 2022-06-13 00:53:21.291119
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    hardware_facts = HPUXHardware()
    facts = dict(distribution='HP-UX', distribution_version='11.31')
    hardware_facts.populate(collected_facts=facts)
    assert hardware_facts.facts['processor_cores'] == 120
    assert hardware_facts.facts['processor_count'] == 2
    assert hardware_facts.facts['processor'] == 'Intel(R) Itanium(R) 9300  series'
    assert hardware_facts.facts['model'] == 'ia64 hp 9000/800/L2000'
    assert hardware_facts.facts['firmware_version'] == 'B.11.31'
    assert hardware_facts.facts['product_serial'] == 'LXXX-XXXXXX'
    assert hardware_facts.facts['memtotal_mb'] == 73152

# Generated at 2022-06-13 00:53:30.965666
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    testobj = HPUXHardware({'platform': 'HP-UX', 'distribution': 'HP-UX'})

    # Test the default case where everything has been logged
    # to syslog.
    testobj.module.run_command = lambda x: (0, 'Wed Jul 9 09:39:10 2014  Physical: 492736 Kbytes', None)
    assert testobj.get_memory_facts() == {'memfree_mb': 123, 'memtotal_mb': 479,
                                          'swapfree_mb': 496, 'swaptotal_mb': 496}

    testobj._get_getconf_pagesize = lambda *args: 4096
    testobj.module.run_command = get_mock_getconf_pagesize_command

    # Test the case where /dev/kmem has been opened, but nothing


# Generated at 2022-06-13 00:53:35.546962
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hw_facts = HPUXHardwareCollector()

    assert hw_facts._fact_class == HPUXHardware
    assert hw_facts._platform == 'HP-UX'
    assert set(hw_facts.required_facts) == set(['platform', 'distribution'])

# Generated at 2022-06-13 00:53:39.259830
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    h = HPUXHardwareCollector({'platform': 'HP-UX',
                               'distribution': 'HP-UX'})

    assert isinstance(h, HPUXHardwareCollector)
    assert h.required_facts == set(['platform', 'distribution'])

# Generated at 2022-06-13 00:53:46.003055
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    class TestModule(object):
        def __init__(self, run_command_results):
            self.run_command_results = run_command_results
            self.run_command_calls = []

        def run_command(self, cmd, use_unsafe_shell=False):
            self.run_command_calls.append(cmd)
            return self.run_command_results.pop(0)

    cpu_facts_test_data = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.23',
        'ansible_architecture': 'B.11.23',
    }

    hpux = HPUXHardware()

    # test get_cpu_facts(collected_facts=None)

# Generated at 2022-06-13 00:53:57.759348
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    module = mock.MagicMock()
    module.run_command.return_value = (1, "", "error")
    hwh = HPUXHardware(module)
    hwh.populate()

# Generated at 2022-06-13 00:54:40.617498
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    import pytest
    from ansible.module_utils.facts.hardware.hpux import HPUXHardware
    from ansible.module_utils.facts.utils.file import file_exists
    from ansible.module_utils.facts.utils.file import file_is_readable
    from ansible.module_utils.facts.utils.file import file_is_writable
    from ansible.module_utils.facts.utils.file import file_text_matches_regex_list

    # Test get_memory_facts method of class HPUXHardware on IA64 B.11.31

# Generated at 2022-06-13 00:54:45.766111
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    from ansible.module_utils.facts import hardware
    from ansible.module_utils._text import to_text

    module = AnsibleModule(supports_check_mode=False)
    h = hardware.HPUXHardware()
    h.module = module
    os.environ["LANG"] = "C"
    os.environ["LC_ALL"] = "C"

    rc, out, err = module.run_command("/usr/bin/vmstat | tail -1", use_unsafe_shell=True)
    data = int(re.sub(' +', ' ', to_text(out)).split(' ')[5].strip())
    memory_facts = h.get_memory_facts()

    assert memory_facts['memfree_mb'] == data * 4 // 1024 // 1024

    rc, out, err = module.run

# Generated at 2022-06-13 00:54:52.264139
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    HPUX = HPUXHardware()
    data = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.23'
    }
    HPUX.module = MockModule()
    HPUX.module.run_command.return_value = (0, '', '')
    result = HPUX.get_hw_facts(data)
    assert 'firmware_version' in result
    assert 'model' in result



# Generated at 2022-06-13 00:54:59.448456
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    module = AnsibleModule(dict(ANSIBLE_MODULE_ARGS={}), supports_check_mode=False)
    set_module_args(dict(ANSIBLE_MODULE_ARGS={}))
    mock_run_command = MagicMock()
    mock_run_command.return_value = 'mymodel'
    module.run_command = mock_run_command
    hwfact = HPUXHardware(module)
    result = hwfact.get_hw_facts()
    assert result['model'] == 'mymodel'


# Generated at 2022-06-13 00:55:07.554932
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    """
    test case for HPUXHardware populate method
    """

    module = AnsibleModule(argument_spec={})
    module.run_command.return_value = (0, '', '')
    module.exit_json = MagicMock()
    module.exit_json.side_effect = SystemExit

    hwe = HPUXHardware(module)
    hwe.populate()
    module.exit_json.assert_called_once_with(
        changed=False,
        ansible_facts=dict(
            ansible_processor_count=4,
            ansible_processor_cores=2,
            ansible_processor_threads_per_core=2,
            ansible_processor='Intel(R) Itanium(R) Processor 9300 series',
        )
    )
