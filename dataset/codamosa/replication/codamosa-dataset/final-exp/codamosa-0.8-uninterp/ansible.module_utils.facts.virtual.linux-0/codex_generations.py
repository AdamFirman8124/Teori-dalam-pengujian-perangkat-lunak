

# Generated at 2022-06-13 04:04:34.860260
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    # this test requires a linux system
    if not platform.system() == 'Linux':
        raise TestSkipError("Test requires a linux system")
    class ModuleMock:
        def get_bin_path(self, arg):
            if arg in ('dmidecode', 'systemd-detect-virt'):
                return '/usr/bin/env'
            return None
        def run_command(self, cmd):
            return 0, '', ''
    mod = ModuleMock()
    mod.run_command = Mock(return_value=(0, '/usr/bin/env', ''))
    fact_virtual = BasicSystemInfo(module=mod).get_virtual_facts()
    if fact_virtual['virtualization_type'] == 'NA':
        raise TestSkipped("Test requires a virtual host")
    # get_virtual_facts() returns a

# Generated at 2022-06-13 04:04:38.392550
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    # We don't want to run the full collector code
    # so we need to patch those that are used
    with patch.object(LinuxVirtualCollector, "_get_dmi_data") as pgd:
        pgd.return_value = {}
        virtual = LinuxVirtualCollector._fact_class(None)
        assert isinstance(virtual, Virtual)


# Generated at 2022-06-13 04:04:42.608173
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    with patch('ansible_collections.ansible.community.plugins.module_utils.facts.virtual.LinuxVirtualCollector.get_platform_parameters') as get_platform_parameters,\
         patch('ansible_collections.ansible.community.plugins.module_utils.facts.virtual.LinuxVirtualCollector.get_host_info_from_dmi') as get_host_info_from_dmi,\
         patch('ansible_collections.ansible.community.plugins.module_utils.facts.virtual.LinuxVirtualCollector.get_host_info_from_pci') as get_host_info_from_pci:
        get_platform_parameters.return_value = {'virtual_facts_class': LinuxVirtual, 'platform': 'Linux', 'virtual_facts_instance': None}
        get_host_info

# Generated at 2022-06-13 04:04:45.385960
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    module = FakeModule()
    lxc_path = os.path.join(os.path.dirname(__file__), 'lxc')
    lxc_info = {
        'lxc_info': True,
        'lxc_path': lxc_path,
    }
    collector = LinuxVirtualCollector(module=module, facts=lxc_info)
    return collector


# Generated at 2022-06-13 04:04:58.661881
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    """
    This is the test of get_virtual_facts method of class LinuxVirtual.
    """
    import imp
    import mock

    class ModuleMock(object):
        pass

    class ExecutionMock(object):
        pass

    module_mock = ModuleMock()
    module_mock.run_command = mock.MagicMock(return_value=(0, '', ''))
    module_mock.get_bin_path = mock.MagicMock(return_value='/bin/dmidecode')
    module_mock.get_file_content = mock.MagicMock(return_value='')

    exec_mock = ExecutionMock()
    exec_mock.module = module_mock

    linux_virtual = LinuxVirtual()

# Generated at 2022-06-13 04:05:00.194361
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    linux_virtual = LinuxVirtualCollector()
    assert linux_virtual._platform == 'Linux'
    assert linux_virtual._fact_class.__name__ == 'LinuxVirtual'


# Generated at 2022-06-13 04:05:03.642965
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    ansible_module_mock = AnsibleModuleMock()
    linux_virtual_obj = LinuxVirtual(ansible_module_mock)
    linux_virtual_obj.get_virtual_facts()


# Generated at 2022-06-13 04:05:06.853585
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    from ansible_collections.misc.not_a_real_collection.plugins.module_utils.facts import collector
    obj = collector.get_collector('virtual', 'Linux')
    assert obj.__class__.__name__ == 'LinuxVirtualCollector'

# Generated at 2022-06-13 04:05:10.788343
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode=True
    )
    virtual_facts = LinuxVirtual(module).get_virtual_facts()
    module.exit_json(virtual_facts=virtual_facts)


# Generated at 2022-06-13 04:05:19.853847
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    test_mod = AnsibleModule(argument_spec=dict())
    test_linux_virtual = LinuxVirtual(test_mod)
    test_linux_virtual.get_virtual_facts()
    # verify virtualization_type and virtualization_role
    if test_linux_virtual.virtual_facts['virtualization_type'] == 'NA':
        assert test_linux_virtual.virtual_facts['virtualization_role'] == 'NA'