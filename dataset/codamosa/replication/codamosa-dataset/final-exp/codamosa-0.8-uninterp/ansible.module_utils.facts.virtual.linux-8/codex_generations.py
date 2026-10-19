

# Generated at 2022-06-13 04:06:01.525177
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    from collections import namedtuple
    module = namedtuple('module', ['OS_FAMILY', 'run_command', 'get_bin_path'])
    module.OS_FAMILY = 'linux'

    def mock_run_command(cmd, path):
        if cmd == 'lscpu':
            return (0, 'Hypervisor: Linux KVM', '')

    def mock_get_bin_path(bin):
        if bin == 'lscpu':
            return '/usr/bin/lscpu'

    module.run_command = mock_run_command
    module.get_bin_path = mock_get_bin_path

    lv = LinuxVirtual(module)
    virtual_facts = lv.get_virtual_facts()

    assert virtual_facts['virtualization_type'] == 'kvm'

# Generated at 2022-06-13 04:06:01.977538
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    LinuxVirtualCollector()

# Generated at 2022-06-13 04:06:06.074770
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    return {'linux_virtual': {'virtualization_type': 'virtualbox', 'virtualization_role': 'guest', 'virtualization_tech_guest': {'virtualbox'}, 'virtualization_tech_host': {}}}

# Generated at 2022-06-13 04:06:11.038291
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    facts = LinuxVirtualCollector(None, None).collect()
    assert isinstance(facts, dict)
    # Check returned facts
    assert 'virtual_fact' in facts
    assert isinstance(facts['virtual_fact'], dict)
    # Check virtual_fact key for value "virtual"
    assert 'virtual' in facts['virtual_fact']
    virtual_val = facts['virtual_fact']['virtual']
    assert isinstance(virtual_val, (bool, int))
    # Check virtual_fact key for value "virtualization_type"
    assert 'virtualization_type' in facts['virtual_fact']
    vtype_val = facts['virtual_fact']['virtualization_type']
    assert vtype_val == 'NA'
    # Check virtual_fact key for value "virtualization_role"

# Generated at 2022-06-13 04:06:21.386306
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    f = tempfile.NamedTemporaryFile(mode='w', delete=True)
    filename = f.name
    f.close()
    l = LinuxVirtual()
    l.module = FakeAnsibleModule()
    l.module.exit_json = exit_json
    l.module.fail_json = exit_failed
    l.get_file_lines = lambda x: []
    l.get_file_content = lambda x: ""
    l.module.get_bin_path = lambda x: None
    with open(filename, 'w') as f:
        f.write('RHEV Hypervisor')
    l.get_file_content = lambda x: "0" if x.endswith('/virtual') else "RHEV Hypervisor" if x.endswith('/sys_vendor') else "RHV"

# Generated at 2022-06-13 04:06:25.340107
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    c = LinuxVirtualCollector()
    assert isinstance(c, VirtualCollector)
    assert isinstance(c, LinuxVirtualCollector)
    assert c._platform == 'Linux'
    assert c._fact_class == LinuxVirtual


# Generated at 2022-06-13 04:06:36.260438
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    # Set values required for testing
    module = AnsibleModule(
        argument_spec = dict()
    )
    module._system_info = dict()
    module._system_info['distribution'] = dict()
    module._system_info['distribution']['name'] = 'RedHat'
    virtual = LinuxVirtual(module)
    virtual_facts = virtual.get_virtual_facts()
    assert virtual_facts['virtualization_role'] == 'guest'
    assert virtual_facts['virtualization_type'] == 'lxc'
    assert 'lxc' in virtual_facts['virtualization_tech_guest']
    assert 'Host' in virtual_facts['virtualization_tech_host']
    assert 'lxc' in virtual_facts['virtualization_tech_host']

# Generated at 2022-06-13 04:06:42.552771
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=False
    )
    lv = LinuxVirtual(module)
    facts = lv.get_virtual_facts()
    assert isinstance(facts, dict)
    assert 'virtualization_role' in facts
    assert isinstance(facts['virtualization_role'], str)
    assert facts['virtualization_role'] in ('host', 'guest', 'unknown')
    assert 'virtualization_type' in facts
    assert isinstance(facts['virtualization_type'], str)

# Generated at 2022-06-13 04:06:47.925608
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    """
    Return virtualization facts for Linux
    Return virtualization facts for all Linux variants
    """
    module, host_sys_class, host_sys_devices, host_proc_cpuinfo, host_proc_modules, host_proc_mounts, host_proc_1, host_proc_self, host_proc_vz, host_proc_lve, host_sys_vendor, host_sys_devices_virtual, host_dmi_id, host_run_systemd = mock_linux_virtual_data()
    module.exit_json = MagicMock()
    host_sys_class.exists.return_value = True
    host_sys_devices.exists.return_value = True
    host_proc_cpuinfo.exists.return_value = True
    host_proc_self.exists.return_value = True

# Generated at 2022-06-13 04:06:52.899660
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    import platform
    import sys
    class FakeModule(object):
        def __init__(self):
            self.sys_platform = platform.system()
            self.run_command_called = 0
            self.run_command_string = ""

        def get_bin_path(self, binary, opts=None, fail_on_missing=False):
            return binary

        def run_command(self, args, check_rc=True):
            self.run_command_string = " ".join(args)
            self.run_command_called += 1
            return (1, "Output", "Error")

    a = LinuxVirtualCollector(FakeModule())
    a.collect()
    assert a._fact_class == LinuxVirtual
    assert a._platform == 'Linux'

