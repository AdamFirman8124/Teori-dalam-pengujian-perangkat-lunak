

# Generated at 2022-06-13 04:05:44.196935
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    '''
    Test LinuxVirtualCollector constructor
    '''
    from ansible.module_utils.facts.collector.virtual import LinuxVirtualCollector
    x = LinuxVirtualCollector()
    assert x._platform == 'Linux'
    assert x._fact_class == LinuxVirtual


# Generated at 2022-06-13 04:05:49.943490
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    # test for cloud-init virtualization facts
    module = AnsibleModule(argument_spec={})
    module.params = {}
    module.run_command = MagicMock(return_value=(0, '', ''))
    module.get_bin_path = MagicMock(return_value='/bin/dmidecode')
    module.get_file_lines = MagicMock(return_value=[''])
    module.get_file_content = MagicMock(return_value='')
    module.get_mount_size = MagicMock(return_value='')

# Generated at 2022-06-13 04:05:56.177948
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    module = AnsibleModule(argument_spec=dict())
    vm = LinuxVirtual(module)
    dmi = []
    lscpu = []
    cpuinfo = []
    with open('./test/unit/ansible_collections/ansible/os/plugins/facts/virtual/dmi') as f:
        dmi.extend(f.read().splitlines())
    with open('./test/unit/ansible_collections/ansible/os/plugins/facts/virtual/lscpu') as f:
        lscpu.extend(f.read().splitlines())
    with open('./test/unit/ansible_collections/ansible/os/plugins/facts/virtual/cpuinfo') as f:
        cpuinfo.extend(f.read().splitlines())

# Generated at 2022-06-13 04:06:00.169684
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    linux_virtual = LinuxVirtual()
    linux_virtual.module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    linux_virtual.get_virtual_facts()


# Generated at 2022-06-13 04:06:04.496639
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    Facter = MagicMock()
    facter_instance = MagicMock()
    Facter.return_value = facter_instance
    module = MagicMock()
    linux_virtual = LinuxVirtualCollector(Facter, module)

    # Instances of Facter and module are passed as parameters
    Facter.assert_called_once_with()
    Facter.return_value.add.assert_called_once_with(linux_virtual._fact_class._fact_name(), None, linux_virtual._fact_class,
                                                    [], linux_virtual._fact_class._platform)
    assert linux_virtual._fact_class._platform == linux_virtual._platform


# Generated at 2022-06-13 04:06:15.146016
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )

    target = LinuxVirtual(module)

    # no virtualization
    with patch.object(os.path, 'exists', return_value = False):
        result = target.get_virtual_facts()
        module.exit_json(**result)

    # lxc
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )
    target = LinuxVirtual(module)

    with patch.object(os.path, 'exists', return_value = True):
        with patch.object(os, 'access', return_value = True):
            with patch.object(target, 'get_file_content', return_value = "lxc"):
                result = target.get

# Generated at 2022-06-13 04:06:20.165554
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    import sys
    import doctest
    #import inspect
    #print(inspect.getsource(LinuxVirtual.get_virtual_facts))
    print(doctest.testmod(sys.modules[__name__]))


if __name__ == "__main__":
    test_LinuxVirtual_get_virtual_facts()



# Generated at 2022-06-13 04:06:22.652193
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    module = AnsibleModuleMock()
    vm = LinuxVirtualCollector(module)
    assert vm._fact_class == vm.fact_class
    assert vm._platform == vm.platform

# Generated at 2022-06-13 04:06:32.276099
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
	''' Unit test for method get_virtual_facts of class LinuxVirtual '''
	module = AnsibleModule( argument_spec = dict( ) )
	#get_virtual_facts has a dependency on a method "run_command" which is not defined
	#here.
	#Because of this, we use the get_virtual_facts of ModuleUtilsVirtualization
	#Hence, this test is actually a test for moduleutils virtualization
	linux_virtual = ModuleUtilsVirtualization( module )
	if linux_virtual.get_virtual_facts()["virtualization_type"] != "physical":
		raise AnsibleError("get_virtual_facts() test failed")


# Generated at 2022-06-13 04:06:40.333640
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    ####
    # Unit tests for method get_virtual_facts
    #  of class LinuxVirtual
    module = AnsibleModule(argument_spec={})
    main_obj = LinuxVirtual()

    # Check for host based on /proc/self/status
    main_obj.mock_run_command = True
    main_obj.mock_run_commands = []
    main_obj.mock_run_commands.append((0, "VxID:\t0", ""))
    result = main_obj.get_virtual_facts(module)
    assert result['virtualization_role'] == 'host'
    assert result['virtualization_type'] == 'linux_vserver'

    # Check for guest based on /proc/self/status
    main_obj.mock_run_command = True
    main_obj.mock