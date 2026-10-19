

# Generated at 2022-06-13 04:05:23.644759
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.linux_virtual import LinuxVirtual
    import os
    import shutil
    import tempfile

    test_dir_path = tempfile.mkdtemp()

    def add_file(path, content=None):
        with open('%s/%s' % (test_dir_path, path), 'w') as f:
            if content is not None:
                f.write(content)

    add_file('proc/1/cgroup', '9:devices:/user.slice/user-0.slice/session-2.scope')
    add_file('proc/1/comm', 'systemd')
    os.makedirs('%s/dev/kvm' % test_dir_path)

# Generated at 2022-06-13 04:05:29.361062
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    test_cases = {}
    test_cases['virtual'] = {}
    test_cases['virtual']['/proc/1/cgroup'] = '''11:memory:/user.slice
10:pids:/user.slice/user-1000.slice/session-1.scope
9:hugetlb:/
8:net_cls,net_prio:/
7:blkio:/user.slice
6:freezer:/
5:perf_event:/
4:devices:/user.slice/user-1000.slice/session-1.scope
3:cpuacct:/
2:cpu:/
1:name=systemd:/user.slice/user-1000.slice/session-1.scope'''

# Generated at 2022-06-13 04:05:32.008011
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    module = AnsibleModule(argument_spec={})
    collector = LinuxVirtualCollector(module)
    assert isinstance(collector.fact_class, LinuxVirtual)
    assert collector.platform == 'Linux'

# Generated at 2022-06-13 04:05:35.612943
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():

    # This is to just show the method usage
    virt = LinuxVirtual()
    virtual_facts = virt.get_virtual_facts()
    print(virtual_facts)


# Generated at 2022-06-13 04:05:44.853285
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    """ Unit test for testing method get_virtual_facts of class LinuxVirtual """

    # Creating a mock class object for the module object
    module_mock = MagicMock()
    module_mock.debug = False
    module_mock.fail_json.return_value = False
    module_mock.run_command.return_value = (0, '', '')
    module_mock.get_bin_path.return_value = 'dmidecode'

    # Creating a mock class object for the LinuxDistribution class
    linux_distro_mock = MagicMock()
    lsb_dist_id_mock = MagicMock()
    lsb_dist_id_mock.lower.return_value = 'centos'
    lsb_dist_release_mock = MagicMock()
    lsb_dist_

# Generated at 2022-06-13 04:05:47.978379
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    virtual_collector = LinuxVirtualCollector()
    assert virtual_collector._fact_class == LinuxVirtual
    assert virtual_collector._platform == 'Linux'
    assert virtual_collector.fact_class == LinuxVirtual
    assert virtual_collector.platform == 'Linux'
    assert virtual_collector.fact_subclass == 'Virtual'

# Generated at 2022-06-13 04:05:51.817786
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    """
    Return dictionary of virtualization facts for a Linux distribution.
    """
    # Unit test for method 'get_virtual_facts' of class 'LinuxVirtual'
    # 'a' is dict object with key 'virtualization_type' and value 'NA'
    # 'b' is dict object with key 'virtualization_role' and value 'NA'
    #t = LinuxVirtual(['a', 'b'])


# Generated at 2022-06-13 04:05:52.744291
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    # No test currently.
    pass

# Class LinuxVirtualizationDmidecode

# Generated at 2022-06-13 04:06:02.132604
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode=True
    )

    # VIRTUAL
    # Set up mock values
    virtual_dict = {
        'virtualization_role': 'guest',
        'virtualization_type': 'openvz',
        'virtualization_tech_host': set(),
        'virtualization_tech_guest': set()
    }
    virtual_dict['virtualization_tech_guest'] = set(['container', 'openvz'])

    # Define the class to be tested
    virtual = LinuxVirtual(module)

    # Make the tests
    assert virtual.get_virtual_facts() == virtual_dict

    # VIRTUAL_HOST
    # Set up mock values

# Generated at 2022-06-13 04:06:02.999851
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    h = LinuxVirtualCollector()
    assert h is not None
