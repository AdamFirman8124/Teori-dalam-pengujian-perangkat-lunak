

# Generated at 2022-06-13 04:06:11.601127
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    module = ansible_module_get_virtual_facts

    first_list = (
        'docker',
        'container',
        'lxc',
        'podman',
        'openvz',
        'containerd',
        'systemd-nspawn'
    )

    second_list = (
        'docker',
        'container',
        'lxc',
        'podman',
        'openvz',
        'containerd'
    )

    # Pass empty dict for module input parameters
    set_module_args({})

    # Instantiate class under test
    linux_virtual_obj = LinuxVirtual(ansible_module=module)

    # Run get_virtual_facts method of class under test
    facts = linux_virtual_obj.get_virtual_facts()

    # Check whether all expected keys are present in the

# Generated at 2022-06-13 04:06:18.395158
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    module = None
    linux_virtual = LinuxVirtual(module)
    virtual_facts = linux_virtual.get_virtual_facts()


    assert virtual_facts['virtualization_type'] == 'NA'
    assert virtual_facts['virtualization_role'] == 'NA'
    assert virtual_facts['virtualization_tech_guest'] == set()
    assert virtual_facts['virtualization_tech_host'] == set()




# Generated at 2022-06-13 04:06:21.577529
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    """Test for constructor of class LinuxVirtualCollector"""
    mock_module = Mock()
    collector = LinuxVirtualCollector(mock_module)
    assert collector is not None
    assert collector._platform == "Linux"
    assert collector._fact_class == LinuxVirtual


# Generated at 2022-06-13 04:06:23.484705
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    assert False, "No test for method LinuxVirtual.get_virtual_facts"

# Class LinuxCollector


# Generated at 2022-06-13 04:06:28.393034
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    module = AnsibleModule(argument_spec=dict())
    virtual_collector = LinuxVirtualCollector(module=module)
    assert virtual_collector.module == module
    assert virtual_collector.platform == 'Linux'


# Generated at 2022-06-13 04:06:37.790009
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    module = AnsibleModule(
        argument_spec = dict(
            gather_subset = dict(default=['all'], type='list')
        ),
        supports_check_mode=True
    )

    # - fails if dmidecode is not installed
    # - fails if module.run_command fails
    # - fails if get_file_content fails
    # - fails if get_file_lines fails
    module.run_command = Mock(return_value=(1, '', ''))
    module.get_bin_path = Mock(return_value='/usr/sbin/dmidecode')
    vm = LinuxVirtual(module)
    vm.get_file_content = Mock(return_value='my_content')
    vm.get_file_lines = Mock(return_value=['my_line'])

    # -

# Generated at 2022-06-13 04:06:39.539579
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    lx_virtual = LinuxVirtualCollector()
    assert lx_virtual._fact_class == LinuxVirtual
    assert lx_virtual._platform == 'Linux'


# Generated at 2022-06-13 04:06:45.173688
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    """This function initiates the LinuxVirtualCollector class
    and collects virtualization facts.
    """
    # Initiating LinuxVirtualCollector class
    fact_subclass = LinuxVirtualCollector()
    _fact_class = fact_subclass._fact_class
    _platform = fact_subclass._platform
    facts = fact_subclass.collect()
    for fact in facts:
        # Checking if the facts are collected
        if fact in facts:
            assert fact in facts
        # Checking if the fact class is LinuxVirtual
        if fact_subclass._fact_class is _fact_class:
            assert fact_subclass._fact_class is _fact_class
        # Checking if the platform is Linux
        if fact_subclass._platform is _platform:
            assert fact_subclass._platform is _platform
        # Checking if the virtualization facts are

# Generated at 2022-06-13 04:06:50.511575
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )

    # Get command line parameters
    # pylint: disable=no-name-in-module
    from ansible_collections.ansible.community.plugins.module_utils.basic import AnsibleModule
    module = AnsibleModule(
        argument_spec = dict(
            wanted = dict(required=False, type='list', default=['virtualization_type', 'virtualization_role', 'virtualization_technologies']),
        ),
        supports_check_mode = True
    )
    # pylint: enable=no-name-in-module
    virtual = LinuxVirtual(module)

    # Run it and check results
    facts = virtual.get_virtual_facts()

# Generated at 2022-06-13 04:06:57.719587
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    from ansible_collections.ansible.community.tests.unit.compat.mock import MagicMock
    from ansible_collections.ansible.community.plugins.module_utils.facts.collectors.virtual import LinuxVirtualCollector
    from ansible_collections.ansible.community.plugins.module_utils.facts.collectors.virtual.linux import LinuxVirtual

    the_module = MagicMock()
    facts_d = {}
    col = LinuxVirtualCollector(the_module, facts_d)
    assert isinstance(col._fact_class, LinuxVirtual)
    assert col._platform == 'Linux'
    assert col._fact_class._platform == 'Linux'

