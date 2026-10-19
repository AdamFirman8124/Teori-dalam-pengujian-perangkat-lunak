

# Generated at 2022-06-13 04:05:27.378985
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    linux_virtual_collector = LinuxVirtualCollector()
    assert linux_virtual_collector.platform == 'Linux'

    linux_virtual = linux_virtual_collector.collect()
    assert linux_virtual.virtualization_role == 'guest'
    assert linux_virtual.virtualization_type == 'docker'

# Generated at 2022-06-13 04:05:27.938506
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    pass

# Generated at 2022-06-13 04:05:35.303625
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    # Test for virtualization
    collector_data = {
        'virtualization_type': 'kvm',
        'virtualization_role': 'guest',
        'virtualization_tech_guest': ['openshift', 'kvm', 'container', 'kubernetes'],
        'virtualization_tech_host': ['kvm'],
        'virt': 'kvm',
        'virtual': 'guest'
    }
    # Test for non-virtualization
    collector_data1 = {
        'virtualization_type': 'NA',
        'virtualization_role': 'NA',
        'virtualization_tech_guest': [],
        'virtualization_tech_host': [],
        'virt': 'NA',
        'virtual': 'NA'
    }
    module = AnsibleModule
    # Test when virtualization

# Generated at 2022-06-13 04:05:44.626323
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():

    # This class call get_virtual_facts of LinuxVirtual
    class FakeModule(object):
        @staticmethod
        def get_bin_path(binary):
            if binary == 'systemd-detect-virt':
                return '/bin/true'
            elif binary == 'chroot':
                return '/bin/false'
            elif binary == 'lscpu':
                return '/bin/false'
            elif binary == 'dmidecode':
                return '/bin/false'
            else:
                return None

    # This method call get_file_lines of LinuxVirtual
    class FakeFile(object):
        @staticmethod
        def get_file_lines(file_name):
            lines = []

# Generated at 2022-06-13 04:05:46.689931
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    # Constructor should return an _fact_class of LinuxVirtual, _platform as Linux
    cl = LinuxVirtualCollector()
    assert cl._fact_class == LinuxVirtual
    assert cl._platform == 'Linux'


# Generated at 2022-06-13 04:05:49.776466
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    # Set parameters
    ansible_module_instance = AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )
    # Initialize fixture
    obj = LinuxVirtual(ansible_module_instance)
    # Test method
    assert isinstance(obj.get_virtual_facts(), dict)

# Generated at 2022-06-13 04:05:54.338478
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    distro = DistroCollector().collect()
    virtual_collector = LinuxVirtualCollector(distro)
    assert virtual_collector.fact_class is not None
    assert virtual_collector.fact_class.name == 'virtual'
    assert virtual_collector.fact_class.platform == 'Linux'


# Generated at 2022-06-13 04:05:55.114847
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    assert True

# Generated at 2022-06-13 04:06:03.530370
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    module = AnsibleModule({})
    # LinuxVirtual instance
    linux_virtual = LinuxVirtual(module)
    # Get virtual_facts
    virtual_facts = linux_virtual.get_virtual_facts()
    # Asssertions
    assert virtual_facts == expected_virtual_facts, 'TEST FAILURE: get_virtual_fact method of class LinuxVirtual should return `%s` but returned `%s`' % (expected_virtual_facts, virtual_facts)
    # Exit the module and return the required facts
    module.exit_json(changed=False, ansible_facts=dict(virtual=virtual_facts))


# Generated at 2022-06-13 04:06:04.807921
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    c = LinuxVirtualCollector()
    assert c._fact_class == LinuxVirtual
    assert c._platform == 'Linux'
