

# Generated at 2022-06-13 04:05:13.122690
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    virtual = LinuxVirtual()

    # test case 1: no virtualization
    with mock.patch.object(platform, 'system') as mock_system:
        mock_system.return_value = 'Linux'
        with mock.patch.object(os.path, 'exists') as mock_exists:
            mock_exists.return_value = False
            assert virtual.get_virtual_facts() == {'virtualization_type': 'NA', 'virtualization_role': 'NA', 'virtualization_tech_host': set(), 'virtualization_tech_guest': set()}

    # test case 2: no virtualization
    with mock.patch.object(platform, 'system') as mock_system:
        mock_system.return_value = 'Linux'

# Generated at 2022-06-13 04:05:17.275671
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    # pylint: disable=protected-access
    virtual = LinuxVirtual()
    virtual_facts = virtual._get_virtual_facts()
    assert virtual_facts is  not None
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts

# Generated at 2022-06-13 04:05:22.375087
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode=True)

    linux_virtual = LinuxVirtual(module)
    expected_virtualization_facts = {
        'virtualization_role': u'guest',
        'virtualization_type': u'virtualbox',
        'virtualization_tech_guest': set(['virtualbox']),
        'virtualization_tech_host': set(['virtualbox'])
    }
    assert linux_virtual.get_virtual_facts() == expected_virtualization_facts


# Generated at 2022-06-13 04:05:31.068681
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    '''Unit test for constructor of class LinuxVirtualCollector'''
    module = AnsibleModuleMock()
    fact_collector = LinuxVirtualCollector(module)
    assert fact_collector.platform == 'Linux'
    assert fact_collector.fact_class == LinuxVirtual
    assert fact_collector.name == 'virtual'
    assert fact_collector.required_plugin_filters == [
        'or',
        [
            'cmd:cat',
            'cmd:dmesg',
            'cmd:ls',
            'cmd:lscpu',
            'cmd:lspci',
            'cmd:virt-what',
            'cmd:dmidecode',
            'file:*/proc/cpuinfo'
        ]
    ]
    assert fact_collector.optional_plugin_filters == []

# Unit

# Generated at 2022-06-13 04:05:41.399770
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    vm = LinuxVirtual()
    # Test case: virtualization_type == 'kvm' and virtualization_role == 'guest'
    vm.module.run_command = MagicMock(return_value=(0, '/proc/self/cgroup:10:memory:/docker/3c5fc8f47069d831f7a0b2c8d8ffd03423a955f5e1c3df815d8d5fdf6d986b6a',
                                                   ''))
    vm.get_file_content = MagicMock(return_value="QEMU Standard PC")
    vm.get_file_lines = MagicMock(return_value=["model name : QEMU Virtual CPU", "model name : QEMU Virtual CPU"])

# Generated at 2022-06-13 04:05:43.111488
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    # Unit test for constructor of class LinuxVirtualCollector
    virtual = LinuxVirtualCollector()
    assert virtual._platform == 'Linux'
    assert virtual._fact_class.__name__ == 'LinuxVirtual'


# Generated at 2022-06-13 04:05:48.501321
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    obj = LinuxVirtualCollector()
    assert obj.platform == 'Linux'
    assert obj.fact_class == LinuxVirtual
    assert obj.collect() == {
        'virtualization_role': 'guest',
        'virtualization_type': 'docker',
        'virtualization_tech_guest': set(['docker', 'container']),
        'virtualization_tech_host': set()}

if __name__ == "__main__":
    test_LinuxVirtualCollector()

# Generated at 2022-06-13 04:05:51.894013
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode=True
    )
    lv = LinuxVirtual(module=module)
    # Test call to a method get_virtual_facts of object lv
    # Test template of returned value expected against discovered value
    module.exit_json(changed=False, meta=lv.get_virtual_facts())


# Generated at 2022-06-13 04:05:52.470647
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    LinuxVirtualCollector()

# Generated at 2022-06-13 04:06:01.757365
# Unit test for method get_virtual_facts of class LinuxVirtual