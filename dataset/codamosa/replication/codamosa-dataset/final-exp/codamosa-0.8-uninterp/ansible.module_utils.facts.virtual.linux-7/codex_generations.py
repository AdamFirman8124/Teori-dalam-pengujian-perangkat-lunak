

# Generated at 2022-06-13 04:04:46.438774
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.linux import LinuxVirtual
    virtual = LinuxVirtual()
    virtual_facts = virtual.get_virtual_facts()
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts

if __name__ == '__main__':
    print(test_LinuxVirtual_get_virtual_facts())

# Generated at 2022-06-13 04:04:58.690780
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    linux_virtual = LinuxVirtual()
    linux_virtual.module = AnsibleModule({})
    get_file_lines = MagicMock()
    get_file_lines.return_value = ('1:name=systemd:/user.slice/user-1000.slice/session-1.scope',)
    linux_virtual.get_file_lines = get_file_lines
    gfh = MagicMock()

# Generated at 2022-06-13 04:05:00.702416
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    module = AnsibleModule(argument_spec={})
    linux_virtual_collector = LinuxVirtualCollector(module=module)
    assert linux_virtual_collector._platform == "Linux"
    assert linux_virtual_collector._fact_class == LinuxVirtual


# Generated at 2022-06-13 04:05:08.054500
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():

    LM = LinuxVirtual()
    LM.module = MagicMock(return_value=None)
    LM.module.get_bin_path = MagicMock(return_value=None)
    LM.module.run_command = MagicMock(return_value=(0, '', ''))

    LM.module.get_bin_path.return_value = '/bin/lscpu'
    LM.module.run_command.return_value = (0, 'Hypervisor: KVM\n', '')
    host_tech = set(['KVM'])
    guest_tech = set(['containers'])
    assert LM.get_virtual_facts() == dict(virtualization_tech_host=host_tech, virtualization_tech_guest=guest_tech, virtualization_role='host', virtualization_type='kvm')



# Generated at 2022-06-13 04:05:11.109085
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    result = {'virtualization_type': 'xen', 'virtualization_role': 'guest'}
    assert LinuxVirtual().get_virtual_facts() == result


# Generated at 2022-06-13 04:05:12.500556
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )
    lv = LinuxVirtual(module)
    lv.get_virtual_facts()


# Generated at 2022-06-13 04:05:21.126318
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    # Create a dummy module for testing
    class DummyModule:
        def get_bin_path(self, arg):
            return 'dummy_bin_path'
    dummy_module = DummyModule()
    # Create a dummy facts class for testing
    class DummyFacts:
        def __init__(self):
            self.data = {}
            self.data['ansible_lsb'] = {}
            self.data['ansible_lsb']['codename'] = 'dummy_codename'
            self.data['ansible_os_family'] = 'dummy_os_family'
            self.data['ansible_distribution'] = 'dummy_distribution'
            self.data['ansible_distribution_version'] = 'dummy_distribution_version'

# Generated at 2022-06-13 04:05:26.251095
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    """
        Test that LinuxVirtualCollector is an instance of
        VirtualCollector and LinuxVirtual.
    """
    linux_virtual = LinuxVirtualCollector()
    assert isinstance(linux_virtual, VirtualCollector)
    assert isinstance(linux_virtual._fact_class, LinuxVirtual)


if __name__ == '__main__':
    print(__doc__)

# Generated at 2022-06-13 04:05:27.937553
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    _LinuxVirtualCollector = LinuxVirtualCollector()
    assert _LinuxVirtualCollector is not None


# Generated at 2022-06-13 04:05:38.070712
# Unit test for method get_virtual_facts of class LinuxVirtual