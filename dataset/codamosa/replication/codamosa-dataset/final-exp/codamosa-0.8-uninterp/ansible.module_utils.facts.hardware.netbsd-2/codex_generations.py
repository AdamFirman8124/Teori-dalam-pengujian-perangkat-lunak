

# Generated at 2022-06-13 00:57:54.985513
# Unit test for method get_cpu_facts of class NetBSDHardware
def test_NetBSDHardware_get_cpu_facts():
    h = NetBSDHardware()
    assert len(h.get_cpu_facts()['processor']) == 1
    assert h.get_cpu_facts()['processor_cores'] == 1

# Generated at 2022-06-13 00:58:05.596930
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():

    collected_facts = {}

    # Instantiate NetBSDHardware
    netbsd_hw = NetBSDHardware()

    # Invoke populate() with None, empty dict and populated dict
    facts = netbsd_hw.populate()
    assert facts['processor_count'] == 1
    assert facts['processor_cores'] == 1
    assert facts['processor'][0] == 'RISCV64'
    assert facts['MemTotal_mb'] == 4914
    assert facts['SwapTotal_mb'] == 0
    assert facts['MemFree_mb'] == 4880
    assert facts['SwapFree_mb'] == 0
    assert facts['product_name'] == 'RISC-V Generic'
    assert facts['product_serial'] == 'Not Specified'

# Generated at 2022-06-13 00:58:14.511697
# Unit test for method get_cpu_facts of class NetBSDHardware
def test_NetBSDHardware_get_cpu_facts():
    # Initialization of variables
    data = None
    key = None
    cpu_facts = {}
    i = 0
    physid = 0
    sockets = {}


# Generated at 2022-06-13 00:58:23.463274
# Unit test for method get_dmi_facts of class NetBSDHardware
def test_NetBSDHardware_get_dmi_facts():
    hardware = NetBSDHardware({'module_setup': True, 'gather_subset': ['all']})
    hardware.sysctl = {'machdep.dmi.system-product': 'Test Product',
                       'machdep.dmi.system-version': 'Test Version',
                       'machdep.dmi.system-uuid': 'Test UUID',
                       'machdep.dmi.system-serial': 'Test Serial',
                       'machdep.dmi.system-vendor': 'Test Vendor',
                       }

# Generated at 2022-06-13 00:58:32.488481
# Unit test for method get_dmi_facts of class NetBSDHardware
def test_NetBSDHardware_get_dmi_facts():
    device_number = 5
    mibs = {}
    for i in range(0, device_number):
        dmi_prefix = 'machdep.dmi.system-'
        mib = dmi_prefix + 'product'
        value = 'NetBSD' + str(i)
        mibs[mib] = value
        mib = dmi_prefix + 'version'
        value = 'Test' + str(i)
        mibs[mib] = value
        mib = dmi_prefix + 'uuid'
        value = '00000000-0000-0000-0000-0000000000' + str(i)
        mibs[mib] = value
        mib = dmi_prefix + 'serial'
        value = '00' + str(i)
        mibs[mib] = value


# Generated at 2022-06-13 00:58:43.376759
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    netbsd = NetBSDHardware()
    netbsd.module = MagicMock()
    netbsd.sysctl = {'machdep.dmi.system-product': 'TEST_PRODUCT_NAME',
                     'machdep.dmi.system-version': 'TEST_PRODUCT_VERSION',
                     'machdep.dmi.system-uuid': 'TEST_PRODUCT_UUID',
                     'machdep.dmi.system-serial': 'TEST_PRODUCT_SERIAL',
                     'machdep.dmi.system-vendor': 'TEST_SYSTEM_VENDOR',
                     'machdep.cpu.brand_string': 'TEST_BRAND_STRING'}
    netbsd.get_mount_facts = MagicMock()
    netbsd.get_mount

# Generated at 2022-06-13 00:58:46.261220
# Unit test for method get_dmi_facts of class NetBSDHardware
def test_NetBSDHardware_get_dmi_facts():
    netbsd_hardware_obj = NetBSDHardware()
    dmi_facts = netbsd_hardware_obj.get_dmi_facts()
    assert dmi_facts['system_vendor'] == 'NetBSD'

# Generated at 2022-06-13 00:58:49.076534
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    module = object()
    hw = NetBSDHardware(module)
    facts = {}
    hw.populate(facts)
    assert facts['system_vendor'] == 'NA'
    assert facts['product_name'] == 'NA'

# Generated at 2022-06-13 00:58:56.236333
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    module = AnsibleModuleMock()
    module.run_command.return_value = (0, '/dev/sda1 4871612 7004 4498580 1% /', '')
    memory_mock = {'machdep': {
        'dmi.system-product': 'VMware Virtual Platform',
        'dmi.system-version': 'None',
        'dmi.system-uuid': '42 42 42 42-42 42 42-42 42-42 42-42 42 42 42 42',
        'dmi.system-serial': 'VMware-42 42 42 42 42 42 42-42 42 42 42 42 42 42'}}
    module.get_sysctl.return_value = memory_mock
    with open('/proc/meminfo', 'r') as f:
        module.get_file_lines.return_

# Generated at 2022-06-13 00:59:06.661341
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    module = None

# Generated at 2022-06-13 01:01:27.731340
# Unit test for method get_cpu_facts of class NetBSDHardware
def test_NetBSDHardware_get_cpu_facts():
    hardware_object = NetBSDHardware({'ansible_facts': {}})
    cpu_facts = hardware_object.get_cpu_facts()

    assert cpu_facts['processor_count'] == 2
    assert cpu_facts['processor_cores'] == 2
    assert cpu_facts['processor'] == ['Intel(R) Core(TM)2 Duo CPU     T5850  @ 2.16GHz', 'Intel(R) Core(TM)2 Duo CPU     T5850  @ 2.16GHz']


# Generated at 2022-06-13 01:01:34.126492
# Unit test for method get_dmi_facts of class NetBSDHardware
def test_NetBSDHardware_get_dmi_facts():
    module = AnsibleModule(argument_spec={})
    mock_sysctl = {}
    sysctl_to_dmi = {
        'machdep.dmi.system-product': 'product_name',
        'machdep.dmi.system-version': 'product_version',
        'machdep.dmi.system-uuid': 'product_uuid',
        'machdep.dmi.system-serial': 'product_serial',
        'machdep.dmi.system-vendor': 'system_vendor',
    }

    for mib in sysctl_to_dmi:
        mock_sysctl[mib] = mib

    def mocked_get_sysctl(*args, **kwargs):
        return mock_sysctl

    # This is the way we mock the sysctl function
    Net

# Generated at 2022-06-13 01:01:41.161281
# Unit test for method populate of class NetBSDHardware

# Generated at 2022-06-13 01:01:43.433145
# Unit test for constructor of class NetBSDHardwareCollector
def test_NetBSDHardwareCollector():
    hw = NetBSDHardwareCollector()
    assert hw.platform == 'NetBSD'
    assert hw.fact_class == NetBSDHardware


# Generated at 2022-06-13 01:01:50.160602
# Unit test for method get_dmi_facts of class NetBSDHardware
def test_NetBSDHardware_get_dmi_facts():
    h = NetBSDHardware()
    # These mibs are for testing purposes only
    h.sysctl = {
        'machdep.dmi.system-product': 'TEST',
        'machdep.dmi.system-version': '1.0',
        'machdep.dmi.system-uuid': 'xxxxxxxx-xxx-xxx-xxx-xxxxxxxxxxxx',
        'machdep.dmi.system-serial': 'deadc0de',
        'machdep.dmi.system-vendor': 'test',
    }
    dmi_facts = h.get_dmi_facts()
    assert dmi_facts['product_name'] == 'TEST'
    assert dmi_facts['product_version'] == '1.0'

# Generated at 2022-06-13 01:01:58.816570
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    module = NetBSDHardwareCollector._create_mock_module()
    # populate() cannot be tested in a reliable way as it operates on various
    # files.
    get_file_content = NetBSDHardware._create_mock_get_file_content()
    get_file_content.add_file_content('/etc/fstab', """
/dev/wd0a / ffs rw,log 1 1
/dev/wd0k /home ffs rw,log 1 2
tmpfs /tmp tmpfs rw,log,-s=64M,-i=512 0 0
kernfs /kern kernfs rw 0 0
ptyfs /dev/pts ptyfs rw 0 0
procfs /proc procfs rw,linux 0 0
"""
                                       )

    get_file_lines = NetBSDHardware._create_

# Generated at 2022-06-13 01:02:06.970919
# Unit test for method get_dmi_facts of class NetBSDHardware
def test_NetBSDHardware_get_dmi_facts():
    h = NetBSDHardware({})
    h.sysctl = {
        'machdep.dmi.system-product': 'PRODUCT',
        'machdep.dmi.system-version': 'VERSION',
        'machdep.dmi.system-uuid': 'UUID',
        'machdep.dmi.system-serial': 'SERIAL',
        'machdep.dmi.system-vendor': 'VENDOR',
    }
    dmi_facts = h.get_dmi_facts()
    assert dmi_facts == {
        'product_name': 'PRODUCT',
        'product_version': 'VERSION',
        'product_uuid': 'UUID',
        'product_serial': 'SERIAL',
        'system_vendor': 'VENDOR',
    }

# Generated at 2022-06-13 01:02:10.248893
# Unit test for method get_cpu_facts of class NetBSDHardware
def test_NetBSDHardware_get_cpu_facts():
    cpu_facts = NetBSDHardware().get_cpu_facts()
    assert isinstance(cpu_facts['processor_count'], int)
    assert not isinstance(cpu_facts['processor_count'], type(None))
    assert isinstance(cpu_facts['processor_cores'], int)
    assert not isinstance(cpu_facts['processor_cores'], type(None))
    assert cpu_facts['processor_count'] > 0
    assert cpu_facts['processor_cores'] > 0

# Generated at 2022-06-13 01:02:21.288680
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    """
    Test method populate of the class NetBSDHardware.
    """
    from ansible.module_utils import basic
    from ansible.module_utils.facts import cache
    from ansible.module_utils.facts.collector.netbsd import NetBSDHardwareCollector
    import ansible.module_utils.facts.hardware.netbsd
    import sys

    module = basic.AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=['!all'], type='list')
        )
    )

    sys.modules['ansible.module_utils.facts.hardware.netbsd'] = ansible.module_utils.facts.hardware.netbsd
    sys.modules['ansible.module_utils.facts.collector.netbsd'] = ansible.module_utils

# Generated at 2022-06-13 01:02:23.651196
# Unit test for constructor of class NetBSDHardwareCollector
def test_NetBSDHardwareCollector():
    HardwareCollector.collectors['NetBSD'] = NetBSDHardwareCollector
    hw = NetBSDHardwareCollector.factory()
    assert isinstance(hw, NetBSDHardware)

# Generated at 2022-06-13 01:05:46.042518
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    # pylint: disable=redefined-outer-name
    import ansible.module_utils.facts.hardware
    import ansible.module_utils.facts.utils
    import ansible.module_utils.facts.sysctl
    import ansible.module_utils.facts
    import ansible.module_utils.facts.hardware.netbsd

    module = ansible.module_utils.facts.FactsModule()
    module.debug = False
    module.fail_json = False
