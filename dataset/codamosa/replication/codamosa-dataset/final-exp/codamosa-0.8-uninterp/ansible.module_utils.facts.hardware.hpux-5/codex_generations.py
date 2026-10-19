

# Generated at 2022-06-13 00:45:32.197093
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    from ansible.module_utils.facts.hardware.hpux import HPUXHardware
    hw = HPUXHardware()
    hw_facts = hw.populate()
    assert hw_facts['processor_count'] == 2
    assert hw_facts['processor_cores'] == 4
    assert hw_facts['processor'] == 'Intel(R) Itanium(R) Processor '
    assert hw_facts['memtotal_mb'] == 204351
    assert hw_facts['memfree_mb'] == 4792
    assert hw_facts['swaptotal_mb'] == 131
    assert hw_facts['swapfree_mb'] == 131

# Generated at 2022-06-13 00:45:38.639702
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    '''
    Unit test for class HPUXHardware method populate.
    '''
    from ansible.module_utils.facts.hardware.hpux import HPUXHardware

    test = HPUXHardware()
    result = test.populate()
    assert result['firmware'] is not None
    assert result['processor_count'] is not None
    assert result['memtotal_mb'] is not None
    assert result['memfree_mb'] is not None
    assert result['swaptotal_mb'] is not None
    assert result['swapfree_mb'] is not None
    assert result['processor_cores'] is not None
    assert result['processor'] is not None
    assert result['model'] is not None


# Generated at 2022-06-13 00:45:44.170209
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    module = AnsibleModuleMock()
    collector=HPUXHardwareCollector(module)
    assert type(collector) is HPUXHardwareCollector
    assert collector._fact_class is HPUXHardware
    assert collector._platform is 'HP-UX'


# Generated at 2022-06-13 00:45:54.934095
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    hpu = HPUXHardware()
    hpu.module = FakeModule()
    hpu.module.run_command = FakeRunCommand()
    # Test for B.11.23 ia64
    hpu.get_cpu_facts({'ansible_architecture': 'ia64', "ansible_distribution_version": "B.11.23"})
    hpu.get_cpu_facts({'ansible_architecture': 'ia64', "ansible_distribution_version": "B.11.31"})
    hpu.get_cpu_facts({'ansible_architecture': 'ia64', "ansible_distribution_version": "B.11.31"})

# Generated at 2022-06-13 00:46:01.264930
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    hw = HPUXHardware()
    collected_facts = {'ansible_architecture': 'ia64', 'ansible_distribution': 'HP-UX', 'ansible_distribution_version': 'B.11.31'}

    hw_facts = hw.get_hw_facts(collected_facts)

    assert hw_facts == {'model': 'ia64 hp server rx2660',
                        'firmware_version': 'HPD8',
                        'product_serial': 'CZC5040K96'}

# Generated at 2022-06-13 00:46:11.810986
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():

    # Set parameters to test with
    collected_facts = {
        'platform': 'HP-UX',
        'distribution': 'B.11.31',
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.31',
        'ansible_host': 'hostname.fqdn',
        'ansible_system': 'HP-UX',
        'ansible_os_family': 'HPUX',
        'ansible_pkg_mgr': 'swinstall'
    }

    # Pass in values for get_hw_facts method of class HPUXHardware
    check_HPUXHardware_get_hw_facts = HPUXHardware()

# Generated at 2022-06-13 00:46:19.011078
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    hardware = HPUXHardware()
    hardware.module = AnsibleModule(
        argument_spec=dict(
        )
    )
    hardware.module.run_command = lambda *args, **kwargs: (0, '', '')
    hardware.populate()
    assert hardware.facts['processor'] == 'Intel(R) Itanium(R) Processor'
    assert hardware.facts['processor_count'] == 32
    assert hardware.facts['processor_cores'] == 64

# Generated at 2022-06-13 00:46:23.565448
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    test_module = AnsibleModule(argument_spec={})
    test_HPUXHardware = HPUXHardware(module=test_module)
    test_out = test_HPUXHardware.get_memory_facts()
    test_module.exit_json(changed=False, ansible_facts=dict(test_out))



# Generated at 2022-06-13 00:46:26.063816
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    hw = HPUXHardware()
    hw._module.run_command = lambda x: (0, 'A700', None)
    assert hw.get_hw_facts() == {'model': 'A700'}

# Generated at 2022-06-13 00:46:36.263258
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    hw = HPUXHardware()
    hw.module = MagicMock()
    hw.module.run_command.return_value = (0, '', '')
    hw.populate(collected_facts={'platform': 'HP-UX', 'distribution': 'B.11.31'})
    hw.get_cpu_facts.assert_called_once_with({'platform': 'HP-UX', 'distribution': 'B.11.31'})
    hw.get_hw_facts.assert_called_once_with({'platform': 'HP-UX', 'distribution': 'B.11.31'})
    hw.get_memory_facts.assert_called_once_with({'platform': 'HP-UX', 'distribution': 'B.11.31'})

# Generated at 2022-06-13 00:46:49.215524
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hpux_hardware_collector = HPUXHardwareCollector()
    assert hpux_hardware_collector._fact_class == HPUXHardware
    assert hpux_hardware_collector._platform == 'HP-UX'
    assert hpux_hardware_collector.required_facts == set(['platform', 'distribution'])

# Generated at 2022-06-13 00:46:50.826010
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    facts = HPUXHardwareCollector()
    assert facts._fact_class is HPUXHardware
    assert facts._platform == 'HP-UX'
    assert facts.required_facts == set(['platform', 'distribution'])



# Generated at 2022-06-13 00:47:00.709992
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    module = args = facts = {}
    collected_facts = {'platform': 'HP-UX', 'distribution': 'B.11.23'}
    hpux = HPUXHardware(module, collected_facts)
    hpux.module.run_command = lambda *args: (0, "HP Integrity rx2660", "")
    hpux.module.run_command = lambda *args: (0, "Firmware revision = 14.15", "")
    hpux.module.run_command = lambda *args: (0, "Machine serial number = CZ50345534", "")
    result = hpux.get_hw_facts(collected_facts)
    assert result['model'] == 'HP Integrity rx2660'
    assert result['firmware_version'] == '14.15'

# Generated at 2022-06-13 00:47:03.632878
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    hardware_facts = HPUXHardware()
    hardware_facts.populate()
    assert hardware_facts.get('memtotal_mb') >= 0
    assert hardware_facts.get('swaptotal_mb') >= 0

# Generated at 2022-06-13 00:47:12.934074
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    mem_dict = {'processor_count': 1, 'memtotal_mb': 1017, 'memfree_mb': 876,
                'swaptotal_mb': 240, 'swapfree_mb': 240}
    # Mock an HP-UX system with 1 GB of memory and 240 MB of swap space
    # Physical memory
    HPUXHardware.module.run_command = lambda command: (0, "1000256", None)

    # Available memory
    vmstat_out = "kthr memory page faults cpu\n----- ----------- ------------------------ ------------ -----------\n  r  b avm fre  re at pi po fr sr cy in sy cs us sy id   0   0 684 876 0 0 1 0 0 0 0 0 0 0 0 100 "

# Generated at 2022-06-13 00:47:19.890142
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    import pytest
    collected_facts = dict()

    # collected_facts['ansible_architecture'] = '9000/800'
    # h = HPUXHardware()
    # cpu_facts = h.get_cpu_facts(collected_facts=collected_facts)
    # assert cpu_facts['processor_count'] == 8

    # collected_facts['ansible_architecture'] = '9000/785'
    # h = HPUXHardware()
    # cpu_facts = h.get_cpu_facts(collected_facts=collected_facts)
    # assert cpu_facts['processor_count'] == 8

    # collected_facts['ansible_architecture'] = 'ia64'
    # collected_facts['ansible_distribution_version'] = 'B.11.23'
    # h =

# Generated at 2022-06-13 00:47:27.059517
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():

    module = FakeAnsibleModule()
    module.run_command = FakeRunCommand()
    # Define the adb output
    module.run_command.data["echo 'phys_mem_pages/D' | adb -k /stand/vmunix /dev/kmem | tail -1 | awk '{print $2}'"] = '262144'
    # Define the output of vmstat
    module.run_command.data["/usr/bin/vmstat | tail -1"] = "    1    0    4    9   12  270   29   16  464  156  0  0"
    hw = HPUXHardware(module)

# Generated at 2022-06-13 00:47:38.594153
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    hw = HPUXHardware()
    hw.module = MockModule()
    hw.module.run_command = Mock(return_value=(0, '', ''))
    hw.module.run_command.side_effect = None
    hw.module.run_command.side_effect = [
        (0, " 256", ''),
        (0, "16392", ''),
        (0, "Memory: 16384 MB", ''),
        (0, "  total:    36741 MB", ''),
        (0, "  total:    36741 MB", '')
    ]
    hw.populate = Mock()
    hw.populate.side_effect = None
    hw.populate.return_value = {'ansible_architecture': '9000/800'}
    assert h

# Generated at 2022-06-13 00:47:42.701820
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    module = Mock()
    module.run_command.return_value = (0, 'HP Integrity rx2660', '')
    hpux_hardware = HPUXHardware(module)
    hw_facts = hpux_hardware.get_hw_facts({'ansible_architecture': 'ia64',
                                           'ansible_distribution_version': 'B.11.23'})
    assert hw_facts == {'model': 'HP Integrity rx2660'}

# Generated at 2022-06-13 00:47:43.744866
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hw_collector = HPUXHardwareCollector()

# Generated at 2022-06-13 00:48:04.861463
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    module = AnsibleModule(
        argument_spec = dict()
    )
    collected_facts = {'ansible_architecture': 'ia64',
                       'ansible_distribution_version': 'B.11.31'}
    hardware = HPUXHardware(module)
    assert hardware.get_hw_facts(collected_facts) == {'model': 'HP Integrity rx8640 Server',
                                                      'firmware_version': '9.04',
                                                      'product_serial': '4DS4456A47'}
    collected_facts = {'ansible_architecture': '9000/800',
                       'ansible_distribution_version': 'B.11.31'}
    hardware = HPUXHardware(module)

# Generated at 2022-06-13 00:48:12.114222
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    class ModuleStub(object):
        def __init__(self):
            self.os_version = 'B.11.31'

        def run_command(self, command, use_unsafe_shell=None):
            if command == '/usr/bin/vmstat | tail -1':
                return (0, '  r b w  swap  free      re  mf pi po fr de sr m1 m2 m3 in sy cs us sy id', '')
            elif command == "grep Physical /var/adm/syslog/syslog.log":
                return (0, 'Aug 13 10:04:20  Physical: 8387864 Kbytes', '')

# Generated at 2022-06-13 00:48:13.688826
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    h = HPUXHardwareCollector()
    assert h.platform == 'HP-UX'


# Generated at 2022-06-13 00:48:23.171252
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    hw = HPUXHardware({})
    collected_facts = {'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.31'}
    hw.module.run_command = lambda x, **kwargs: (1, "", "")
    hw.module.exit_json = lambda x: x
    hw.module._failed = False
    hw.module.warn = lambda x: x
    result = hw.get_memory_facts(collected_facts)
    assert result == {}

    hw.module.run_command = lambda x, **kwargs: (0, "Physmem    :  2299712 Kbytes", "")
    result = hw.get_memory_facts(collected_facts)

# Generated at 2022-06-13 00:48:26.644979
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    cpu_facts = HPUXHardware().get_cpu_facts()
    assert type(cpu_facts) is dict
    assert 'processor_count' in cpu_facts


# Generated at 2022-06-13 00:48:34.476603
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    hp_ux = HPUXHardware({'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.31'})

    rc, out, err = hp_ux.module.run_command.return_value = (0, '', '')
    rc, out, err = hp_ux.module.run_command.return_value = (0, 'separator=', '')
    rc, out, err = hp_ux.module.run_command.return_value = (0, 'Firmware revision =', '')

    hp_ux.get_hw_facts()

# Generated at 2022-06-13 00:48:44.488921
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    collected_facts = {'ansible_architecture': '9000/800', 'ansible_distribution_version': 'B.11.31'}
    hw = HPUXHardware(None, collected_facts)
    data = hw.get_memory_facts()
    assert data['memfree_mb'] == 2
    assert data['memtotal_mb'] == 2
    assert data['swaptotal_mb'] == 2
    assert data['swapfree_mb'] == 2
    collected_facts = {'ansible_architecture': 'ia64'}
    hw = HPUXHardware(None, collected_facts)
    data = hw.get_memory_facts()
    assert data['memfree_mb'] == 2
    assert data['memtotal_mb'] == 2

# Generated at 2022-06-13 00:48:56.720079
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    module = AnsibleModule(argument_spec={})
    collected_facts = {'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.31'}
    hardware_collector = HPUXHardware(module)
    test_memory_facts = hardware_collector.get_memory_facts(collected_facts=collected_facts)
    assert (test_memory_facts['swaptotal_mb'] == 512)
    # assert (test_memory_facts['swapfree_mb'] == 0)
    assert (test_memory_facts['memfree_mb'] == 19142)
    assert (test_memory_facts['memtotal_mb'] == 10107)

# Generated at 2022-06-13 00:49:06.131351
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    module = AnsibleModule(
        argspec=dict(
            fact_subset=dict(default='!all,!min'),
        )
    )
    collected_facts = dict(
        ansible_architecture='ia64',
        ansible_distribution='HP-UX',
        ansible_distribution_version='B.11.31',
    )
    hw_facts = HPUXHardware(module).get_hw_facts(collected_facts)
    assert hw_facts['model'] == 'HP Integrity rx8620 Server'
    assert hw_facts['product_serial'] == 'MFG3C4X7V2Q'
    assert hw_facts['firmware_version'] == 'v2.70 (10/22/07)'


# Generated at 2022-06-13 00:49:11.158267
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    hpu = HPUXHardware()
    hpu.module.run_command = lambda *args, **kwargs: ('', '', '')
    hpu.module.run_command.side_effect = [('0', '', ''), ('123908', '', ''), ('', '', '')]

    hpu.get_memory_facts()
    assert hpu.memtotal_mb == 825


# Generated at 2022-06-13 00:49:33.296900
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    module = AnsibleModule(
        argument_spec={}
    )
    hardware = HPUXHardware(module)

    # test model and firmware
    collected_facts = {
        'platform': 'HP-UX', 'distribution': 'HP-UX'
    }
    test_hw_facts = hardware.get_hw_facts(collected_facts)
    assert test_hw_facts['model'] == 'HP  9000/800'
    assert test_hw_facts['firmware_version'] == '2895'



# Generated at 2022-06-13 00:49:44.170926
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    import sys
    import json
    import pytest

    # Mock module for the tests and fake fact values
    class MockModule(object):
        def __init__(self, params):
            self.params = params

        def fail_json(self, *args, **kwargs):
            sys.exit(1)

        def run_command(self, command, use_unsafe_shell=False):
            if 'syslog' in command:
                return 0, 'Physical: 80000 Kbytes', None
            if 'adb' in command:
                return 0, '80000', None
            if 'vmstat' in command:
                return 0, ' procs    memory             page            disk          faults      cpu', None
            if 'swapinfo' in command:
                return 0, 'dev     fs     size  used avail capacity    -1', None

# Generated at 2022-06-13 00:49:49.215983
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    facts_dict = dict(
        ansible_architecture='9000/800',
        ansible_distribution='HP-UX'
    )
    hardware_collector = HPUXHardwareCollector()
    hardware = hardware_collector.collect(facts_dict, None)

    assert hardware.platform == 'HP-UX'

# Generated at 2022-06-13 00:49:54.416775
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    module = AnsibleModuleMock()
    hw = HPUXHardware(module=module)
    facts = {'ansible_architecture': '9000/800', 'ansible_distribution_version': 'B.11.23'}
    assert hw.get_cpu_facts(collected_facts=facts).get('processor_count') == 4


# Generated at 2022-06-13 00:50:01.494140
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    """
    Test get_hw_facts() method of HPUXHardware class
    """
    hardware = HPUXHardware()
    hardware.module = AnsibleModule(argument_spec = dict())
    hardware.module.run_command = MagicMock(return_value=(0, 'ia64', ''))
    hardware.module.run_command = MagicMock(return_value=(0, 'B.11.23', ''))
    hardware.module.run_command = MagicMock(return_value=(0, 'HP Integrity Superdome', ''))
    hardware.module.run_command = MagicMock(return_value=(0, 'ROM Version OA170AA', ''))
    hardware.module.run_command = MagicMock(return_value=(0, 'Superdome Serial#: US12345678', ''))
    hw_

# Generated at 2022-06-13 00:50:04.956674
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    hpu_hw = HPUXHardware()
    facts = hpu_hw.populate()
    assert all(k in facts for k in ('processor_count',
                                    'processor_cores', 'processor'))


# Generated at 2022-06-13 00:50:06.471618
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    assert HPUXHardwareCollector(dict())


# Generated at 2022-06-13 00:50:16.037689
# Unit test for method get_cpu_facts of class HPUXHardware

# Generated at 2022-06-13 00:50:26.129716
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    # Given
    module = AnsibleModuleMock()
    module.run_command = MagicMock(return_value=(0, 'HP Integrity Superdome Server', ''))
    module.run_command = MagicMock(return_value=(0, 'Firmware revision: B.11.31.1370', ''))
    module.run_command = MagicMock(return_value=(0, '', ''))
    collected_facts = {'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.31'}

    # When
    obj = HPUXHardware()
    result = obj.get_hw_facts(collected_facts)

    # Then

# Generated at 2022-06-13 00:50:33.470406
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    hardware_facts = HPUXHardware()
    collected_facts = {
        'ansible_architecture': '9000/800',
        'ansible_processor_count': 2,
    }
    result = hardware_facts.get_memory_facts(collected_facts)
    assert result['memtotal_mb'] == 1024
    assert result['swaptotal_mb'] == 0
    assert result['swapfree_mb'] == 0
    assert result['memfree_mb'] == 962
    collected_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.23',
        'ansible_processor_count': 2,
    }
    result = hardware_facts.get_memory_facts(collected_facts)

# Generated at 2022-06-13 00:51:07.048786
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hardware_collector = HPUXHardwareCollector()
    assert hardware_collector.platform == 'HP-UX'
    assert hardware_collector.required_facts == set(['platform', 'distribution'])
    assert hardware_collector.fact_class == HPUXHardware


# Generated at 2022-06-13 00:51:13.572698
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    m_module = MagicMock()
    m_run_command = MagicMock()
    m_run_command.return_value = [0, '2', '']
    m_module.run_command = m_run_command
    h = HPUXHardware(m_module)
    h.get_cpu_facts(collected_facts={'ansible_architecture': 'ia64'})
    assert m_run_command.call_args_list == [call("/usr/contrib/bin/machinfo | grep 'Number of CPUs'", use_unsafe_shell=True),
                                            call("ioscan -FkCprocessor | wc -l", use_unsafe_shell=True)]
    m_module.run_command.reset_mock()

# Generated at 2022-06-13 00:51:24.224421
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    """Unit test for method get_memory_facts of class HPUXHardware"""
    module_mock = AnsibleModule(argument_spec={})
    hw_mock = HPUXHardware(module_mock)
    hw_mock.module.run_command = run_command_mock
    collected_facts = {'ansible_architecture': '9000/800'}
    memory = hw_mock.get_memory_facts(collected_facts=collected_facts)
    assert memory.get('memfree_mb') == 59
    assert memory.get('memtotal_mb') == 3072
    assert memory.get('swapfree_mb') == 0
    assert memory.get('swaptotal_mb') == 0
    collected_facts = {'ansible_architecture': 'ia64'}

# Generated at 2022-06-13 00:51:29.455307
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    out = []
    out.append("9000/800\n")
    out.append("B.11.23\n")
    out.append("8\n")
    out.append("2\n")
    out.append("/usr/contrib/bin/machinfo: /usr/contrib/lib/libcma.sl.1: bad magic number\n")
    out.append("/usr/contrib/bin/machinfo: /usr/contrib/lib/libcma.sl.1: bad magic number\n")
    out.append("/usr/contrib/bin/machinfo: /usr/contrib/lib/libcma.sl.1: bad magic number\n")
    out.append("Intel Xeon\n")

# Generated at 2022-06-13 00:51:36.591052
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    # Make sure we are only running against HP-UX systems
    if os.path.isfile('/usr/contrib/bin/machinfo') and os.path.isfile('/usr/sbin/swapinfo'):
        hpux_hardware = HPUXHardwareCollector()
        assert hpux_hardware.platform == 'HP-UX'
        assert hpux_hardware.required_facts == set(['platform', 'distribution'])
        assert hpux_hardware._fact_class == HPUXHardware

# Generated at 2022-06-13 00:51:37.866025
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    x = HPUXHardwareCollector()

    assert x.platform == 'HP-UX'

# Generated at 2022-06-13 00:51:46.431683
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    module = AnsibleModule(
        argument_spec=dict(),
    )
    module.run_command = MagicMock(return_value=(0, "", ""))
    h = HPUXHardware(module=module)

    pagesize = 4096
    collected_facts = {}

    # a class method must not mutate the class
    saved_machinfo = h.machinfo

# Generated at 2022-06-13 00:51:53.402436
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    hw = HPUXHardware()
    hw.module = hw
    hw.module.run_command = run_command_mock
    hw.populate({'ansible_architecture': '9000/785'})
    hw.populate({'ansible_architecture': '9000/800'})

    hw.populate({'ansible_architecture': 'ia64'})
    hw.populate({'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.31'})
    hw.populate({'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.23'})



# Generated at 2022-06-13 00:51:59.973346
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    module = FakeAnsibleModule()
    hardware = HPUXHardware(module)
    hardware.get_memory_facts()
    memory_facts = module.exit_json['ansible_facts']['ansible_memfree_mb']
    assert memory_facts > 0

# Generated at 2022-06-13 00:52:04.174140
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    hardware = HPUXHardware({'ansible_architecture': 'ia64'})
    hardware.module = type('', (object,), {'run_command': lambda *_: (0, '', '')})
    hardware.get_memory_facts() == {'memfree_mb': 0, 'swaptotal_mb': 0, 'swapfree_mb': 0, 'memtotal_mb': 0}

# Generated at 2022-06-13 00:53:06.443678
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    """Test the constructor of HPUXHardwareCollector"""
    hwc = HPUXHardwareCollector()
    assert hwc._fact_class == HPUXHardware
    assert hwc._platform == 'HP-UX'

# Generated at 2022-06-13 00:53:12.596707
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    hardware = HPUXHardware()
    collected_facts = {
        'ansible_architecture': '9000/800',
    }
    pagesize = 4096
    rc, out, err = hardware.module.run_command("/usr/bin/vmstat | tail -1", use_unsafe_shell=True)
    data = int(re.sub(' +', ' ', out).split(' ')[5].strip())
    expected_memfree_mb = pagesize * data // 1024 // 1024

    rc, out, err = hardware.module.run_command("echo 'phys_mem_pages/D' | adb -k /stand/vmunix /dev/kmem | tail -1 | awk '{print $2}'",
                                               use_unsafe_shell=True)
    if not err:
        expected_mem

# Generated at 2022-06-13 00:53:21.341119
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    my_hosts = [{'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.23', 'ansible_platform': 'HP-UX'},
                {'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.31', 'ansible_platform': 'HP-UX'}]
    for host in my_hosts:
        h = HPUXHardware(module=None)
        output = h.get_hw_facts(collected_facts=host)
        assert output['model'] == 'ia64 hp Integrity rx8640 Server'
        assert output['firmware_version']
        assert output['product_serial']

# Generated at 2022-06-13 00:53:27.093183
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    class Obj:
        def __init__(self):
            self.module = Obj()
            self.module.run_command = command_exec
    def command_exec(cmd):
        return 0, "Rx2620", ""
    hw = HPUXHardware(Obj())
    assert hw.get_hw_facts() == {'model': 'Rx2620'}


# Generated at 2022-06-13 00:53:32.467961
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    module = FakeAnsibleModule()
    hardware = HPUXHardware(module)
    processor_facts = hardware.populate()
    expected = {'processor_cores': 16,
                'processor': 'Intel(R) Itanium(R) Processor 9650',
                'processor_count': 2,
                'memtotal_mb': 16384,
                'memfree_mb': 14702,
                'model': 'ia64 hp server rx6600',
                'firmware_version': 'B.11.31.2038'}
    assert processor_facts == expected

# Generated at 2022-06-13 00:53:34.784888
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    module_mock = MockModule()
    hardware_obj = HPUXHardware(module_mock)
    hardware_obj.get_memory_facts()

# Generated at 2022-06-13 00:53:43.175570
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    collected_facts = {'ansible_system_vendor': 'HP',
                       'ansible_distribution': 'HP-UX',
                       'ansible_distribution_version': 'B.11.31',
                       'ansible_architecture': 'ia64'}
    mem_facts = HPUXHardware(None).get_memory_facts(collected_facts=collected_facts)
    assert mem_facts['memtotal_mb'] == 10240
    assert mem_facts['memfree_mb'] == 723
    assert mem_facts['swapfree_mb'] == 793
    assert mem_facts['swaptotal_mb'] == 793

# Generated at 2022-06-13 00:53:48.590043
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    h = HPUXHardware({})
    h.module = '(ansible.module_utils.facts.hardware.hpu_ux.AnsibleModule)'
    h.module.run_command = fake_run_command

    # Parse memory facts
    if os.environ.get('TEST_MACHINE') == '715':
        # pymum returns 0 for memtotal_mb and swapfree_mb
        assert h.get_memory_facts({'ansible_architecture': '9000/800'}) == {'memtotal_mb': 0, 'swapfree_mb': 0, 'swaptotal_mb': 240, 'memfree_mb': 0}

# Generated at 2022-06-13 00:53:53.029873
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    print("Get an instance of HPUXHardwareCollector")
    hw_collector = HPUXHardwareCollector()
    hw_collector.collect()
    print("Test HPUXHardwareCollector passed.")
    assert(1)


# Generated at 2022-06-13 00:53:59.688689
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    from ansible.module_utils.facts.hardware.hpuxtestdata import hw_data_input

    hardware = HPUXHardware()
    hardware.get_memory_facts(collected_facts=hw_data_input)

    assert hardware.facts['memfree_mb'] == 210
    assert hardware.facts['memtotal_mb'] == 4975
    assert hardware.facts['swaptotal_mb']  == 755
    assert hardware.facts['swapfree_mb'] == 755

