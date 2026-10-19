

# Generated at 2022-06-13 00:35:07.681941
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    module = AnsibleModuleMock()
    module.run_command.return_value = (0, 'zsh: correct ' + 'cmd' + ' to ' + 'cmd [nyae]? y\n', '')
    aix_hardware = AIXHardware()
    aix_hardware.module = module
    result = aix_hardware.get_dmi_facts()
    assert 'firmware_version' in result
    assert 'product_serial' in result
    assert 'lpar_info' in result
    assert 'product_name' in result


# Generated at 2022-06-13 00:35:12.192497
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    hardware_class = AIXHardware(None)
    facts = hardware_class.get_dmi_facts()
    assert 'firmware_version' in facts
    assert 'lpar_info' in facts
    assert 'product_name' in facts
    assert 'product_serial' in facts

# Generated at 2022-06-13 00:35:16.942972
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    test_module = type('test_AIXHardware_get_cpu_facts_module', (object,), {'run_command': run_command})
    test_module.exit_json = exit_json
    test_module.fail_json = fail_json

    ah = AIXHardware(test_module)

    cpu_facts = ah.get_cpu_facts()
    assert cpu_facts['processor'] == 'PowerPC_POWER6'
    assert cpu_facts['processor_cores'] == 1
    assert cpu_facts['processor_count'] == 2


# Generated at 2022-06-13 00:35:26.936699
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    lines = '''memory pages
62476
active pages
59872
inactive pages
0
wire pages
22809
fictitious pages
1833
free pages
2590'''.split('\n')
    lines = map(lambda x: x.strip(), lines)
    module = MockModule()
    module.run_command = Mock(return_value=(0, lines, ""))
    hardware = AIXHardware(module=module)
    memory_facts = hardware.get_memory_facts()
    assert memory_facts == {'memfree_mb': 10.205078125, 'memtotal_mb': 245.15625}
    # test swapinfo
    assert memory_facts['swaptotal_mb'] == 396.75390625
    assert memory_facts['swapfree_mb'] == 396.748046875

#

# Generated at 2022-06-13 00:35:32.472187
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    hw_test = AIXHardware('module')
    vgs_test = hw_test.get_vgs_facts()
    assert vgs_test['vgs']['rootvg'][0]['pv_name'] in ('hdisk0', 'hdisk1')
    assert vgs_test['vgs']['rootvg'][0]['total_pps'] == '546'
    assert vgs_test['vgs']['realsyncvg'][0]['pp_size'] == '4 megabyte(s)'

# Generated at 2022-06-13 00:35:39.281820
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    module = type('', (), {})()
    module.run_command = lambda *args, **kwargs: (0, 'processor 0 Available 00-00\nprocessor 1 Available 00-01\nprocessor 2 Available 00-02\nprocessor 3 Available 00-03\n', '')
    ah = AIXHardware(module)
    fact, _ = ah.populate()
    assert fact['processor_count'] == 4
    assert fact['processor'] == 'PowerPC_POWER7'
    assert fact['processor_cores'] == 1


# Generated at 2022-06-13 00:35:42.737337
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    inp = {'module': {
        'get_bin_path': lambda x,y: 'x' if x == 'lsvg' else None
    }}
    obj = AIXHardwareCollector(inp)
    assert obj.lsvg_path == 'x'

# Generated at 2022-06-13 00:35:48.298247
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    module = MockModule()
    hardware = AIXHardware(module)
    setattr(module, 'run_command', fake_run_command)

# Generated at 2022-06-13 00:35:54.147725
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec={})
    hardware = AIXHardware(module)
    cpu_facts = hardware.get_cpu_facts()

    assert type(cpu_facts) == type({})
    assert 'processor' in cpu_facts
    assert 'processor_cores' in cpu_facts
    assert 'processor_count' in cpu_facts


# Generated at 2022-06-13 00:36:01.669519
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    module = AnsibleModule(
        argument_spec = dict(
            gather_subset=dict(default=['!all'], type='list')
        ),
        supports_check_mode=True
    )

    # If a command failed, it will show it in the result,
    # so we can handle it here
    if module.params['gather_subset'] == ['!all']:
        module.exit_json(changed=False, ansible_facts={})

    hardware_collector = AIXHardwareCollector(module=module)
    hardware_collector.collect()
    result = hardware_collector.get_facts()

    module.exit_json(changed=False, ansible_facts=result)


# Generated at 2022-06-13 00:36:23.521683
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    hardware_collector = AIXHardwareCollector()
    assert hardware_collector._platform == 'AIX'
    assert hardware_collector._fact_class == AIXHardware


# Generated at 2022-06-13 00:36:30.851457
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    module = AnsibleModule(
        argument_spec={
            'gather_subset': dict(default=['all'], type='list')
        },
        supports_check_mode=True
    )

    if not AIXHardwareCollector.fetch_all(module):
        module.exit_json(changed=False)

    result = {}
    for fact in module.list_facts():
        result[fact] = module.get_fact(fact)

    result['ansible_facts'] = module.ansible_facts
    module.exit_json(ansible_facts=result)



# Generated at 2022-06-13 00:36:38.152453
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    from ansible_collections.ansible.community.tests.unit.compat.mock import MagicMock

    module = MagicMock()
    data = '''
IBM,8247-42L
'''
    module.run_command.return_value = (0, data, '')
    module.get_bin_path.return_value = '/usr/sbin/lsconf'

    hw = AIXHardware(module)
    facts = hw.populate()
    assert 'firmware_version' in facts
    assert 'product_serial' in facts
    assert 'lpar_info' in facts
    assert 'product_name' in facts



# Generated at 2022-06-13 00:36:42.305591
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    _fact_class = AIXHardwareCollector()
    assert _fact_class._platform == 'AIX'
    assert _fact_class._fact_class == AIXHardware
    assert isinstance(_fact_class._fact_class(dict()), Hardware)

# Generated at 2022-06-13 00:36:54.919131
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    from ansible.module_utils.facts.hardware.aix import AIXHardware
    aix_hardware = AIXHardware()

    lsdev_cmd = aix_hardware.module.get_bin_path('lsdev')
    lsattr_cmd = aix_hardware.module.get_bin_path('lsattr')

    aix_hardware.module.run_command = lambda x, **kwargs: (0, LSDEV_CMD_OUTPUT, '')
    aix_hardware.module.get_bin_path = lambda x, **kwargs: x

    device_facts = aix_hardware.get_device_facts()
    assert 'devices' in device_facts
    assert 'ent0' in device_facts['devices']

# Generated at 2022-06-13 00:37:01.739447
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    m_run_command = None
    tested_class = AIXHardware(dict(module=m_run_command))

    m_run_command.run_command.return_value = (0, "1  2123\n2   545", None)
    memory_facts = tested_class.get_memory_facts()
    assert memory_facts['memtotal_mb'] == 2123
    assert memory_facts['swaptotal_mb'] == 0
    assert memory_facts['swapfree_mb'] == 0

    m_run_command.run_command.return_value = (0, "1  2123\n2   545", None)
    memory_facts = tested_class.get_memory_facts()
    assert memory_facts['memtotal_mb'] == 2123
    assert memory_facts['swaptotal_mb']

# Generated at 2022-06-13 00:37:05.626836
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    from ansible.module_utils.facts.hardware.aix import AIXHardware
    aixhw = AIXHardware()
    return aixhw.get_mount_facts()


# Generated at 2022-06-13 00:37:14.124638
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    hardware = AIXHardware()
    hardware.module = MagicMock()
    hardware.module.run_command = MagicMock()

    hardware.module.run_command.return_value = 0, "IBM,8247-22L", ""
    hardware.module.get_bin_path = MagicMock()
    hardware.module.get_bin_path.return_value = "/usr/sbin/lsconf"

    hardware.module.run_command.return_value = 0, "Machine Serial Number: Z0123456789\nLPAR Info: 1 IODF", ""
    hardware.module.run_command.return_value = 0, "System Model:\nMachine Serial Number: Z0123456789\nLPAR Info: 1 IODF\nSystem Model: IBM,8247-22L", ""

    dmi_facts

# Generated at 2022-06-13 00:37:19.825022
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    """
    Test the constructor of AIXHardwareCollector
    """
    fact_class = 'ansible.module_utils.facts.hardware.aix.AIXHardwareCollector'
    fact_class_obj = AIXHardwareCollector()
    assert fact_class_obj._platform == 'AIX'
    assert fact_class_obj._fact_class == 'ansible.module_utils.facts.hardware.aix.AIXHardware'
    

# Generated at 2022-06-13 00:37:25.704238
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    class ModuleStub():
        def run_command(self, command):
            return 0, 'proc1 Available 00-00-04-00-00-41-00-00\nproc2 Available 00-00-04-00-00-41-00-00\n', ''
    assert AIXHardware(ModuleStub()).get_cpu_facts() == {'processor_count': 2, 'processor': 'PowerPC_POWER8'}


# Generated at 2022-06-13 00:37:49.428886
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():

    class MockModule(object):
        class RunCommand(object):
            def run_command(params):
                if not params:
                    raise Exception("Error, Command %s not recognized", params)


# Generated at 2022-06-13 00:37:55.257533
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():

    # create instance of class AIXHardware for test
    hw_aix_obj = AIXHardware()

    # create empty dict for collected_facts
    collected_facts = {}

    # set object attribute "module" with fake AnsibleModule object
    # used only method run_command of AnsibleModule object
    class AnsibleModuleFake:
        def __init__(self):
            self.params = {}

        def run_command(self, cmd, use_unsafe_shell=False):
            _out = ""
            _rc = 0
            _err = ""


# Generated at 2022-06-13 00:37:57.416806
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec={})
    hardware = AIXHardware(module=module)
    processor_count = hardware.get_cpu_facts()['processor_count']
    assert isinstance(processor_count, int)
    assert processor_count > 0



# Generated at 2022-06-13 00:38:08.093633
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    module = AnsibleModule(argument_spec={})

    hardware = AIXHardware(module)
    hardware.populate()
    facts = module.params['ansible_facts']
    assert facts['ansible_processor_count'] == 2
    assert facts['ansible_processor'] == 'PowerPC_POWER7'
    assert facts['ansible_processor_cores'] == 8
    assert facts['ansible_memtotal_mb'] == 301056
    assert facts['ansible_memfree_mb'] == 63
    assert facts['ansible_swaptotal_mb'] == 314368
    assert facts['ansible_swapfree_mb'] == 314368

    vgs_facts = hardware.get_vgs_facts()

# Generated at 2022-06-13 00:38:11.713814
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    mock_module = type('AnsibleModule', (object,), dict(
        params=dict(),
        run_command=lambda *_, **__: (0, """memory pages:              164768
free pages:               11578
""", ''),
        get_bin_path=lambda *_, **__: '/bin/true'
    ))()
    platform = AIXHardware(mock_module)
    result = platform.populate()
    assert 'memtotal_mb' in result
    assert result['memtotal_mb'] == 65
    assert 'memfree_mb' in result
    assert result['memfree_mb'] == 4


# Generated at 2022-06-13 00:38:14.937504
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    """
    Unit test for method get_vgs_facts of class AIXHardware
    """
    vgs_facts = {}
    vgs_facts['vgs'] = {}

    module = None
    hardware = AIXHardware(module=module)
    vgs_facts = hardware.get_vgs_facts()



# Generated at 2022-06-13 00:38:27.100381
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    facts = AIXHardware()
    cmd = 'lsvg -o | xargs lsvg -p'
    rc, out, err = facts.module.run_command(cmd)
    test_result = facts.get_vgs_facts()
    for k_vgs, v_vgs in test_result.items():
        for k_vg, v_vg in v_vgs.items():
            for ele in v_vg:
                v_pv_name = ele['pv_name']
                v_pv_state = ele['pv_state']
                v_total_pps = ele['total_pps']
                v_free_pps = ele['free_pps']
                v_pp_size = ele['pp_size']

# Generated at 2022-06-13 00:38:38.935696
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():

    module = AnsibleModule(argument_spec={})

    hardware = AIXHardware(module)

    # Method populate return a dict with all facts
    hardware_facts = hardware.populate()

    # Check if it is a dict
    assert isinstance(hardware_facts, dict)

    # Check if all facts are present
    assert 'processor' in hardware_facts
    assert 'processor_cores' in hardware_facts
    assert 'processor_count' in hardware_facts
    assert 'memtotal_mb' in hardware_facts
    assert 'memfree_mb' in hardware_facts
    assert 'firmware_version' in hardware_facts
    assert 'product_serial' in hardware_facts
    assert 'product_name' in hardware_facts
    assert 'lpar_info' in hardware_facts
    assert 'swaptotal_mb' in hardware

# Generated at 2022-06-13 00:38:47.633623
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    recout = '''firmware_version:IBM,8247-22L'''
    class TestModule:
        def __init__(self):
            self.params = {}
            self.params['gather_subset'] = ['all']

        def get_bin_path(self, cmd, required=False):
            if "lsattr" == cmd:
                return "/usr/sbin/lsattr"
            elif "lsconf" == cmd:
                return "/usr/sbin/lsconf"
            else:
                return ""

        def run_command(self, cmd, check_rc=True, use_unsafe_shell=True):
            if cmd == "/usr/sbin/lsattr -El sys0 -a fwversion":
                return 0, recout, ""

# Generated at 2022-06-13 00:38:50.235434
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    x = AIXHardwareCollector()
    assert x._platform == 'AIX'
    assert x._fact_class == AIXHardware

# Generated at 2022-06-13 00:39:13.171364
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    aix_hw_collector = AIXHardwareCollector(None)
    assert aix_hw_collector._platform == 'AIX'

# Generated at 2022-06-13 00:39:22.724358
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    module = FakeAnsibleModule()
    hardware = AIXHardware(module)

# Generated at 2022-06-13 00:39:28.790384
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    module = AnsibleModule(argument_spec={})
    hardware = AIXHardware(module)
    out_file = open('/tmp/lsdev.out', 'r')
    out_lsdev = out_file.read()
    out_file.close()
    hardware.module.run_command = MagicMock(return_value=(0, out_lsdev, ''))
    out_file = open('/tmp/lsattr.out', 'r')
    out_lsattr = out_file.read()
    out_file.close()
    hardware.module.run_command = MagicMock(return_value=(0, out_lsattr, ''))
    results = hardware.get_device_facts()
    devices = results['devices']
    assert len(devices) == 13

# Generated at 2022-06-13 00:39:39.390479
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    """
    Test get_vgs_facts of class AIXHardware.
    """

# Generated at 2022-06-13 00:39:43.052522
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    module = AnsibleModule(argument_spec=dict())

    hw = AIXHardware(module=module)
    results = hw.get_memory_facts()
    assert results == {
        'memfree_mb': 0,
        'memtotal_mb': 0,
        'swapfree_mb': 0,
        'swaptotal_mb': 0
    }

# Generated at 2022-06-13 00:39:44.700802
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    """Unit test to test method get_memory_facts of class AIXHardware"""
    hardware_facts = AIXHardware(dict())
    hardware_facts.populate()


# Generated at 2022-06-13 00:39:49.173248
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    """
    Unit test for method get_device_facts of class AIXHardware
    """
    module = AnsibleModule(argument_spec={})
    hardware = AIXHardware(module)

    result = hardware.get_device_facts()
    assert(isinstance(result, dict))
    assert('devices' in result)
    assert(isinstance(result['devices'], dict))

# Generated at 2022-06-13 00:39:59.878775
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    t = AIXHardware()

    t.module = MagicMock()
    t.module.get_bin_path.return_value = "/usr/sbin/lsconf"
    t.module.run_command.return_value = (0, "/etc/objrepos/ppc/lsconf output", '')
    t.module.run_command.return_value = (0, "/etc/objrepos/ppc/lsattr -El sys0 -a fwversion output", '')

    hardware_facts = t.get_dmi_facts()
    # test expected output
    assert hardware_facts['firmware_version'] == 'firmware_version'
    assert hardware_facts['product_name'] == 'product_name'
    assert hardware_facts['product_serial'] == 'product_serial'

# Generated at 2022-06-13 00:40:01.831237
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    x = AIXHardwareCollector()
    assert x._platform == 'AIX'
    assert x._fact_class == AIXHardware

# Generated at 2022-06-13 00:40:09.445002
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    from ansible.module_utils.facts.hardware.aix import AIXHardware
    hardware_facts = AIXHardware()

# Generated at 2022-06-13 00:40:52.066172
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    from ansible.module_utils.facts.hardware.aix import AIXHardware
    aix_hardware = AIXHardware({})
    aix_hardware.collect(None)
    memory_facts = aix_hardware.populate()


# Generated at 2022-06-13 00:40:59.882086
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    module = AnsibleModule(argument_spec={})
    hardware = AIXHardware(module)
    facts = {}

    pagesize = 4096
    cmd = "/usr/bin/vmstat -v"
    rc = 0
    out = '''
    memory pages     :    69027
    free pages       :     2199
    '''
    err = ''
    # Define facts to be returned by method run_command
    module.run_command = MagicMock(return_value=(rc, out, err))

    memory_facts = hardware.get_memory_facts()
    module.run_command.assert_called_with(cmd)
    assert memory_facts['memtotal_mb'] == pagesize * 69027 // 1024 // 1024
    assert memory_facts['memfree_mb'] == pagesize * 2199 // 1024 // 1024



# Generated at 2022-06-13 00:41:09.074616
# Unit test for method get_dmi_facts of class AIXHardware
def test_AIXHardware_get_dmi_facts():
    from ansible.module_utils.facts.collector import AIXHardwareCollector

    test_AIXHardware_object = AIXHardwareCollector()
    test_AIXHardware_object.module = MockModule()

    # Success test case
    test_AIXHardware_object.module.run_command.return_value = (0, 'test_intel', '')
    assert test_AIXHardware_object.get_dmi_facts() == {'firmware_version': 'test_intel'}
    test_AIXHardware_object.module.run_command.assert_called_with('/usr/sbin/lsattr -El sys0 -a fwversion')

    # Failure test case
    test_AIXHardware_object.module.run_command.return_value = (1, '', '')
    assert test_AIX

# Generated at 2022-06-13 00:41:13.918964
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    hardware = AIXHardware()

    hardware.module = MockModule()
    hardware.module.run_command.return_value = (0,
"""memory pages:                             359369
free pages:                                178125""", "")

    facts = hardware.get_memory_facts()
    assert facts['memtotal_mb'] == 7157
    assert facts['memfree_mb'] == 3504


# Generated at 2022-06-13 00:41:23.453602
# Unit test for method get_memory_facts of class AIXHardware
def test_AIXHardware_get_memory_facts():
    # get_memory_check inputs and outputs
    vmstat_inputs = [
        "procs                  memory             page                 disks              faults              cpu\n"
        "r  b   p  swpd   free  re  mf  pi  po  fr   de   sr   s0  s1  s2    in    sy    cs    us    sy    id  "
        "  wa  st\n"
        "0  0   0     0 261452   0   0   0   0   0  122  122   0   0   0   204  1051  1255   309   15   83  0   0 "
        "0\n"
    ]

    vmstat_output = [
    ]

    # run test get_memory_facts
    print("Starting test_get_memory_facts")
    test_memory

# Generated at 2022-06-13 00:41:32.557092
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    cmd = 'echo "proc0 Available 00-00 Processor\nproc1 Available 00-01 Processor" | /usr/bin/cat'
    m = AnsibleModule(argument_spec=dict(), check_invalid_arguments=False)
    m._debug = False
    m.run_command = MagicMock(return_value=(0, cmd, None))
    h = AIXHardware(m)

    result = h.get_cpu_facts()
    assert result['processor'] == 'Available'
    assert result['processor_cores'] == 4
    assert result['processor_count'] == 2



# Generated at 2022-06-13 00:41:38.301105
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    from ansible.module_utils.facts.hardware.aix import AIXHardware

    module = AnsibleModule()
    tmp = AIXHardware(module=module)
    aix_hardware = AIXHardware(module=module)
    rc, out, err = module.run_command("cat /var/tmp/lsvg.out")

    if rc == 0 and out:
        vgs_facts = aix_hardware.get_vgs_facts()

        assert vgs_facts["vgs"]

# Generated at 2022-06-13 00:41:39.373963
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    hardware = AIXHardwareCollector()
    assert hardware._platform == 'AIX'
    assert hardware._fact_class == AIXHardware

# Generated at 2022-06-13 00:41:48.059078
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    """
        Unit test for method 'get_device_facts' of class AIXHardware under
        various conditions.
    """

    # (1) test for device 'fcs0'
    device_name = 'fcs0'
    device_state = 'Available'
    device_type = '32-bit Fibre Channel'
    attr_name = 'adapter_type'
    attr_parameter = 'fcs'
    device_attrs = { attr_name: attr_parameter }
    lsdev_cmd = "lsdev -Cc adapter"
    lsattr_cmd_args = "lsattr -E -l %s" % device_name

    class FakeModule:
        def get_bin_path(self, bin_path, required=False):
            return True


# Generated at 2022-06-13 00:41:57.704238
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    module = AnsibleModule(argument_spec={})
    facts = AIXHardware(module).populate()

    assert facts['firmware_version'] == '1.11'
    assert facts['memory_mb']['real']['total'] == 8589934592
    assert facts['memory_mb']['real']['free'] == 536870912
    assert facts['memory_mb']['swap']['total'] == 274877906944
    assert facts['memory_mb']['swap']['free'] == 234827771904
    assert facts['processor_cores'] == 72
    assert facts['processor_count'] == 72
    assert facts['processor'] == 'PowerPC_POWER8'



# Generated at 2022-06-13 00:43:39.409558
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    m = AnsibleModuleMock()
    x = AIXHardware(m)
    x.populate()
    assert 'processor' in x.facts
    assert 'firmware_version' in x.facts
    assert 'lpar_info' in x.facts
    assert 'product_name' in x.facts
    assert 'product_serial' in x.facts
    assert 'swapfree_mb' in x.facts
    assert 'swaptotal_mb' in x.facts
    assert 'vgs' in x.facts
    assert 'mounts' in x.facts
    assert 'devices' in x.facts

# Generated at 2022-06-13 00:43:44.073581
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    """
    Unit test for get_cpu_facts method of class AIXHardware
    """
    expected_result = {
        'processor_cores': 8,
        'processor': 'PowerPC_POWER8',
        'processor_count': 12
        }
    module = AnsibleModule(argument_spec={})
    hardware = AIXHardware(module)
    results = hardware.get_cpu_facts()
    assert results == expected_result


# Generated at 2022-06-13 00:43:51.698438
# Unit test for method get_cpu_facts of class AIXHardware
def test_AIXHardware_get_cpu_facts():
    """
    Unit test for method get_cpu_facts of class AIXHardware
    """
    # pylint: disable=W0212

# Generated at 2022-06-13 00:43:56.374703
# Unit test for method get_device_facts of class AIXHardware
def test_AIXHardware_get_device_facts():
    """
    Return test data for AIXHardware.get_device_facts()
    """

# Generated at 2022-06-13 00:44:05.740471
# Unit test for method get_vgs_facts of class AIXHardware
def test_AIXHardware_get_vgs_facts():
    from ansible.module_utils.facts.hardware.aix import AIXHardware
    facts = AIXHardware()
    vgs_facts = facts.get_vgs_facts()
    assert vgs_facts
    assert vgs_facts['vgs']['rootvg'] is not None
    assert vgs_facts['vgs']['rootvg'][0]['pv_name'] == 'hdisk0'
    assert vgs_facts['vgs']['rootvg'][0]['pv_state'] == 'active'
    assert vgs_facts['vgs']['rootvg'][0]['total_pps'] == '546'
    assert vgs_facts['vgs']['rootvg'][0]['free_pps'] == '8'

# Generated at 2022-06-13 00:44:13.648085
# Unit test for method populate of class AIXHardware
def test_AIXHardware_populate():
    from ansible.module_utils.facts.hardware.aix import AIXHardware, AIXHardwareCollector
    module = AnsibleModule(argument_spec={})

    hardware_facts = AIXHardwareCollector()
    hardware_facts.populate()

    assert hardware_facts._facts['processor_count'] == 2, 'processor_count is not 2'
    assert hardware_facts._facts['processor'] == 'PowerPC_POWER7', 'processor is not correct'
    assert hardware_facts._facts['processor_cores'] == 1, 'processor_cores is not 1'
    assert hardware_facts._facts['memtotal_mb'] > 0, 'memtotal_mb is not set'
    assert hardware_facts._facts['memfree_mb'] > 0, 'memfree_mb is not set'

# Generated at 2022-06-13 00:44:15.406950
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    module = AnsibleModule(dict())
    my_obj = AIXHardwareCollector(module)
    module.exit_json(changed=False)


# Generated at 2022-06-13 00:44:16.759215
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    assert AIXHardwareCollector._platform == 'AIX'
    assert AIXHardwareCollector._fact_class is AIXHardware



# Generated at 2022-06-13 00:44:19.818973
# Unit test for constructor of class AIXHardwareCollector
def test_AIXHardwareCollector():
    module = AnsibleModule(argument_spec={})
    hwCollector_facts = AIXHardwareCollector(module)
    assert isinstance(hwCollector_facts._fact_class, AIXHardware)
    assert isinstance(hwCollector_facts._fact_class.module, AnsibleModule)


if __name__ == '__main__':
    from ansible.module_utils.basic import *
    test_AIXHardwareCollector()

# Generated at 2022-06-13 00:44:29.259689
# Unit test for method get_mount_facts of class AIXHardware
def test_AIXHardware_get_mount_facts():
    from ansible.module_utils.facts.processor.aix import AIXHardware
    from ansible.module_utils.facts import Collector

    module = AnsibleModuleMock()

    module.run_command = AnsibleModuleMock.run_command
    module.get_bin_path = AnsibleModuleMock.get_bin_path

    facts_collector = Collector(module=module)
    hardware_collector = AIXHardware(module, [facts_collector])
    mounts = hardware_collector.get_mount_facts()

    if mounts:
        mounts = mounts['mounts']

        assert mounts[0]['mount'] == "/"
        assert mounts[0]['device'] == "/dev/hd4"
        assert mounts[0]['fstype'] == "jfs2"
        assert mounts[0]['options']