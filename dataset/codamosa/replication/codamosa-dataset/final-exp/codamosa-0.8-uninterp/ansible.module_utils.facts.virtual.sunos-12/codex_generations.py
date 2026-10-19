

# Generated at 2022-06-13 04:20:39.490076
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    c = SunOSVirtualCollector()
    assert isinstance(c, SunOSVirtualCollector)
    assert c.platform == 'SunOS'
    assert c._platform == 'SunOS'
    assert c._fact_class == SunOSVirtual

# Generated at 2022-06-13 04:20:47.612149
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # Test on a SunOS machine without any virtualization
    module = FakeModule({})
    sunos = SunOSVirtual(module)
    assert sunos.get_virtual_facts() is None

    # Test on a SunOS machine with Sun Logical Domains

# Generated at 2022-06-13 04:20:49.340540
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual_facts = SunOSVirtual()
    assert virtual_facts.platform == 'SunOS'


# Generated at 2022-06-13 04:20:52.369104
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    c = SunOSVirtualCollector()
    assert hasattr(c, '_fact_class')
    assert hasattr(c, '_platform')
    assert c._fact_class == SunOSVirtual
    assert c._platform == 'SunOS'

# Generated at 2022-06-13 04:20:53.991896
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    v = SunOSVirtual({})
    assert v.platform == "SunOS"
    assert v.get_virtual_facts() == {}

# Generated at 2022-06-13 04:20:56.135276
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    module = type('SunOsModule', (object,), dict())()
    module.get_bin_path = lambda x=None: ""

    fact = SunOSVirtual(module)
    assert 'virtualization_role' not in fact.get_virtual_facts()

# Generated at 2022-06-13 04:21:01.001013
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    expected_results = {'virtualization_role': 'guest',
                        'container': 'zone',
                        'virtualization_type': 'virtualbox',
                        'virtualization_tech_host': set(['zone']),
                        'virtualization_tech_guest': set(['zone', 'virtualbox'])}
    _f = SunOSVirtual(None)
    # Set a bunch of values for the module class and the module instance
    class MockModule(object):
        def __init__(self):
            self.params = {}
            self.args = {}

        def get_bin_path(self, arg):
            path = None
            if arg == 'zonename':
                path = '/usr/bin/zonename'
            elif arg == 'modinfo':
                path = '/usr/bin/modinfo'

# Generated at 2022-06-13 04:21:07.218084
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    module = MagicMock()
    # Module has no bin path
    module.get_bin_path.side_effect = lambda _: None
    # Module has no zone
    module.run_command.side_effect = lambda _: (1, None, None)
    # SunOSVirtual constructor must raise an exception
    with pytest.raises(Exception):
        SunOSVirtual(module)

# Generated at 2022-06-13 04:21:15.487156
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    from ansible.module_utils import basic
    import ansible_collections.ansible.builtin.plugins.module_utils.virtualization as virtualization
    module = basic.AnsibleModule(
        argument_spec={},
        supports_check_mode=True)
    module_utils = virtualization.Virtualization()
    module.get_bin_path = module_utils.get_bin_path
    module.run_command = module_utils.run_command
    module.exit_json = module_utils.exit_json
    module.fail_json = module_utils.fail_json
    SunOSVirtual(module).get_virtual_facts()

# Generated at 2022-06-13 04:21:17.660864
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    # check with valid args
    module = FakeModule()
    sunos_virtual = SunOSVirtual(module)

    assert sunos_virtual.platform == 'SunOS'


# Generated at 2022-06-13 04:21:30.747806
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():

    # Test for value of variables when platforms is Solaris
    sunos = SunOSVirtual(None)
    assert 'SunOS' == sunos.platform

# Generated at 2022-06-13 04:21:33.180258
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    assert SunOSVirtualCollector._platform == 'SunOS'
    assert str(SunOSVirtualCollector._fact_class) == "<class 'ansible.module_utils.facts.virtual.sunos.SunOSVirtual'>"

# Generated at 2022-06-13 04:21:36.787615
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    module = ansible_mock.AnsibleModule(
        argument_spec={},
    )
    sv = SunOSVirtual(module)
    assert sv.platform == 'SunOS'
    assert sv.virtualization_type == ''
    assert sv.virtualization_role == ''
    assert sv.container == ''



# Generated at 2022-06-13 04:21:40.251616
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    # In this module, the constructor for Virtual always returns
    # a class object of the subclass that corresponds to the platform.
    # So if the constructor works, we simply verify that the object
    # returned by the constructor is an instance of the subclass
    # applicable to the current platform.
    # Since the subclass and platform are fixed, it doesn't matter
    # what arguments are passed to the constructor.
    assert isinstance(Virtual('any_module'), SunOSVirtual)

# Generated at 2022-06-13 04:21:49.834519
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.solaris import VirtualFacts
    virtual_facts = VirtualFacts()
    if virtual_facts._solaris_guest_facts:
        assert virtual_facts._solaris_guest_facts['virtualization_type'] == 'virtuozzo'
        assert virtual_facts._solaris_guest_facts['virtualization_role'] == 'guest'
    if virtual_facts._solaris_host_facts:
        assert 'virtualization_type' not in virtual_facts._solaris_host_facts
        assert 'virtualization_role' not in virtual_facts._solaris_host_facts

# Generated at 2022-06-13 04:21:56.993690
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.sunos import SunOSVirtual
    sysctl = '/usr/sbin/modinfo | /bin/grep -q "VMware"'
    def sysctl_side_effect(module):
        if module == 'modinfo':
            return sysctl
        return None
    sysctl_mock = lambda x: sysctl_side_effect(x)
    facts = {
        'kernel': 'SunOS',
        'program_files': '/bin,/usr/bin',
    }
    set_module_args = {
    }
    module = Mock(exit_json=exit_json, set_facts=set_facts)
    module.run_command = Mock(return_value=(0, '', ''))
    module.get_bin_path = sysctl_mock

# Generated at 2022-06-13 04:22:00.027179
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    module = FakeModule()
    v = SunOSVirtual(module)
    assert v is not None

# Helper functions for testing



# Generated at 2022-06-13 04:22:11.056883
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    """Test get_virtual_facts() of SunOSVirtual class."""
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes

    # Create a SunOSVirtual class object to test 
    sunos_virtual_obj = SunOSVirtual({})

    # Create a mock module
    module = basic.AnsibleModule({})
    module.run_command = lambda *args, **kw: (0, to_bytes(""), "")

    # Set up module mock
    sunos_virtual_obj.module = module

    # Add the required files and directories to the mock filesystem
    module.tmpdir = mkdtemp()
    os.makedirs(os.path.join(module.tmpdir, "proc"))

# Generated at 2022-06-13 04:22:21.116091
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    import tempfile
    tmpdir = tempfile.mkdtemp()
    module = FakeModule(tmpdir)
    virt_facts = SunOSVirtual(module=module).get_virtual_facts()
    assert virt_facts == {'container': 'zone',
                          'virtualization_role': 'guest',
                          'virtualization_tech_host': {'zone'},
                          'virtualization_tech_guest': {'zone'},
                          'virtualization_type': 'vmware'}
    tmpdir = tempfile.mkdtemp()
    module = FakeModule(tmpdir)
    virt_facts = SunOSVirtual(module=module).get_virtual_facts()
    assert virt_facts == {}



# Generated at 2022-06-13 04:22:29.309607
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.sunos import SunOSVirtual
    from ansible.module_utils.facts.virtual.sunos import SunOSVirtualCollector


# Generated at 2022-06-13 04:22:45.543445
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    collected_facts = dict()
    SunOSVirtual(collected_facts=collected_facts)
    assert collected_facts['virtualization_type'] == 'SunOS'

# Generated at 2022-06-13 04:22:52.479448
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = DummyAnsibleModule()
    virtual = SunOSVirtual(module)

    module.run_command.return_value = (
        0,
        "\n".join([
            "vmware",
            "VirtualBox",
            "KVM",
            "Solaris Logical Domains",
        ]),
        ""
    )
    virtual_facts = virtual.get_virtual_facts()
    assert virtual_facts == {
        'virtualization_tech_guest': set(['vmware', 'virtualbox', 'kvm', 'ldom']),
        'virtualization_type': 'vmware',
        'virtualization_role': 'guest',
        'virtualization_tech_host': set()
    }


# Generated at 2022-06-13 04:22:57.710060
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    # Test SunOSVirtual() constructor.
    sunosvirt = SunOSVirtual(dict())
    assert sunosvirt is not None
    # Test SunOSVirtual().get_virtual_facts()
    sunosvirtfacts = sunosvirt.get_virtual_facts()
    assert sunosvirtfacts is not None
    assert type(sunosvirtfacts) == dict


# Generated at 2022-06-13 04:23:00.018772
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    module = AnsibleModule(argument_spec={})
    platform = SunOSVirtual(module)

    assert platform.get_virtual_facts() == {}


# Generated at 2022-06-13 04:23:02.106876
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual_facts = SunOSVirtual()
    assert virtual_facts.platform == 'SunOS'

# Generated at 2022-06-13 04:23:04.959878
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    vc = SunOSVirtualCollector()
    assert vc._platform == "SunOS"
    assert vc._fact_class.platform == "SunOS"


# Generated at 2022-06-13 04:23:09.672851
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # Patch Virtual._run_commands() to return dummy output
    def run_commands(module, command):
        if command == "/usr/sbin/prtconf -pv":
            return 0, "", ""
        elif command == "hostid":
            return 0, "0000000000000000", ""
        elif command == "hostname":
            return 0, "test.example.org", ""
        elif command == "/usr/sbin/virtinfo -p":
            return 0, "DOMAINROLE|impl=LDoms|control=false|io=false|service=false|root=false", ""
        elif command == "/usr/sbin/zonename":
            return 0, "global", ""
        elif command == "/usr/sbin/smbios":
            return 0, "", ""

# Generated at 2022-06-13 04:23:11.969798
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    c = SunOSVirtualCollector()
    assert c.platform == 'SunOS'
    assert c.fact_class.__name__ == 'SunOSVirtual'

# Generated at 2022-06-13 04:23:22.092961
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    fake_module = FakeModule({
        'zonename': 'zonename',
        'virtinfo': 'virtinfo',
        'smbios': 'smbios',
        'modinfo': 'modinfo',
    })
    fact_class = SunOSVirtual(fake_module)
    facts = fact_class.get_virtual_facts()
    assert facts == {'container': 'zone',
                     'virtualization_type': 'vmware',
                     'virtualization_role': 'guest',
                     'virtualization_tech_host': {'zone'},
                     'virtualization_tech_guest': {'zone', 'vmware'}}



# Generated at 2022-06-13 04:23:23.532679
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    result = SunOSVirtual({})
    assert result.platform == 'SunOS'

# Generated at 2022-06-13 04:23:53.505327
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    SunOSVirtualCollector()

# Generated at 2022-06-13 04:23:55.320954
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    svc = SunOSVirtualCollector()
    assert svc._fact_class == SunOSVirtual
    assert svc._platform == 'SunOS'

# Generated at 2022-06-13 04:24:01.264591
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    test_module = {
        "run_command.return_value": (0, "", ""),  # no errors
        "get_bin_path.return_value": "/usr/bin/smbios"
    }
    test_module_dict = {
        "run_command.return_value": (0, "", ""),  # no errors
        "get_bin_path.return_value": "/usr/bin/smbios"
    }
    test_module_fail = {
        "run_command.return_value": (1, "", ""),  # errors
        "get_bin_path.return_value": "/usr/bin/smbios"
    }
    virtual = SunOSVirtual(test_module, test_module_dict)

    # Run the method on an unset module

# Generated at 2022-06-13 04:24:02.744146
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    x = SunOSVirtualCollector()
    assert x._fact_class._platform == 'SunOS'

# Generated at 2022-06-13 04:24:04.758270
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    # Make sure the constructor is not abstract
    SunOSVirtual()

# Generated at 2022-06-13 04:24:15.906392
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = type('', (), {})()
    module.run_command = run_command
    module.get_bin_path = get_bin_path
    Base = type('', (object,), {})
    module.Base = Base
    module.exit_json = Base
    module.fail_json = Base
    virtual = SunOSVirtual(module)
    v = virtual.get_virtual_facts()
    assert v['virtualization_type'] == 'vmware'
    assert v['virtualization_role'] == 'guest'
    assert 'container' in v
    assert v['container'] == 'zone'
    assert 'virtualization_tech_guest' in v
    assert 'virtualization_tech_host' in v
    assert 'vmware' in v['virtualization_tech_guest']

# Generated at 2022-06-13 04:24:23.979636
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = FakeAnsibleModule()
    module.basic_argument_spec['path'] = {
        'env': [],
        'default': ['/bin', '/sbin', '/usr/bin', '/usr/sbin', '/usr/local/bin', '/usr/local/sbin'],
        'type': 'list'
    }
    virtual = SunOSVirtual(module)
    virtual_facts = virtual.get_virtual_facts()
    assert virtual_facts == {
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set(),
    }
    module.run_command = FakeRunCommandLDoms()
    virtual = SunOSVirtual(module)
    virtual_facts = virtual.get_virtual_facts()

# Generated at 2022-06-13 04:24:33.335833
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True)
    module.run_command = MagicMock(return_value=(0, 'VMware', ''))
    module.get_bin_path = MagicMock(return_value=True)
    vm = SunOSVirtual(module)
    vm.get_virtual_facts()
    module.run_command.assert_has_calls([call(['modinfo']), call(['zonename']), call(['virtinfo', '-p'])])

# Generated at 2022-06-13 04:24:34.757683
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    h = SunOSVirtual()
    assert h.get_virtual_facts()

# Generated at 2022-06-13 04:24:37.831171
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    sunosv_collector = SunOSVirtualCollector(None)
    assert sunosv_collector._platform is 'SunOS'

# Generated at 2022-06-13 04:25:29.404697
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    facts = SunOSVirtualCollector()
    assert isinstance(facts, SunOSVirtualCollector)
    assert facts._platform == 'SunOS'
    assert facts._fact_class == SunOSVirtual

# Generated at 2022-06-13 04:25:32.945272
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    """test_SunOSVirtualCollector.py: tests constructor of class
    SunOSVirtualCollector
    """
    sunos_virtual_collector = SunOSVirtualCollector()
    assert sunos_virtual_collector.platform == 'SunOS'
    assert sunos_virtual_collector._fact_class == SunOSVirtual

# Generated at 2022-06-13 04:25:35.330164
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    virtual_collector = SunOSVirtualCollector()
    assert virtual_collector is not None
    assert virtual_collector.fact_class == SunOSVirtual
    assert virtual_collector.platform == 'SunOS'

# Generated at 2022-06-13 04:25:36.142623
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    SunOSVirtualCollector()

# Generated at 2022-06-13 04:25:47.993387
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    module = type('MockModule', (object,), dict())
    module.run_command = dict()
    module.run_command['return_codes'] = dict()
    module.run_command['stdout'] = dict()
    module.run_command['stdout']['vmware'] = 'VMware'
    module.run_command['stdout']['virtualbox'] = 'VirtualBox'
    module.run_command['stdout']['kvm'] = 'KVM'
    module.run_command['stdout']['xen'] = 'HVM domU'
    module.run_command['stdout']['parallels'] = 'Parallels'
    module.run_command['return_codes']['vmware'] = 0

# Generated at 2022-06-13 04:25:52.962187
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    os_platform = 'SunOS'
    os_dist = ''
    os_version = ''
    os_major_version = ''
    os_minor_version = ''
    os_build = ''
    os_codename = ''

    vc = SunOSVirtualCollector(os_platform, os_dist, os_version, os_major_version, os_minor_version, os_build, os_codename)
    assert isinstance(vc, SunOSVirtualCollector)
    assert vc.platform == 'SunOS'

# Generated at 2022-06-13 04:25:55.833274
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual_facts_results = SunOSVirtual({})
    assert 'virtualization_type' in virtual_facts_results
    assert 'virtualization_role' in virtual_facts_results
    assert 'container' in virtual_facts_results


# Generated at 2022-06-13 04:25:57.580325
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    from ansible.module_utils.facts import virtual
    virtual_test = virtual.SunOSVirtual()
    assert virtual_test.platform == 'SunOS'

# Generated at 2022-06-13 04:26:00.965174
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    from ansible.module_utils.facts.virtual.sunos.SunOSVirtualCollector import (SunOSVirtualCollector)
    obj = SunOSVirtualCollector()
    assert obj.platform == 'SunOS'

# Generated at 2022-06-13 04:26:06.782097
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    """
    Makes sure that the method get_virtual_fact of class SunOSVirtual, returns
    the correct dictionary with virtual facts.
    """
    facts = {}
    v = SunOSVirtual(facts=facts)
    results = v.get_virtual_facts()
    expected_results = {}

    # show the gathered virtual facts
    for item in results:
        print("%s => %s" % (item, results[item]))

    # assert that the results are equal to the expected ones
    for item in expected_results:
        assert expected_results[item] == results[item]

# Generated at 2022-06-13 04:27:52.682015
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virt = SunOSVirtual()
    assert virt.data is not None

# Generated at 2022-06-13 04:27:54.039628
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    collector = SunOSVirtualCollector()
    assert collector.platform == "SunOS"
    assert collector.fact_class == SunOSVirtual

# Generated at 2022-06-13 04:27:58.257529
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    """
    Test the module constructor of SunOSVirtualCollector
    """
    module = dict()
    module['virtual'] = 'SunOSVirtualCollector'
    collector = SunOSVirtualCollector(module)
    assert isinstance(collector._fact_class, SunOSVirtual)
    assert collector._platform == 'SunOS'


# Generated at 2022-06-13 04:28:00.015593
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    vc = SunOSVirtualCollector()
    assert vc._fact_class == SunOSVirtual
    assert vc._platform == 'SunOS'

# Generated at 2022-06-13 04:28:01.052175
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual = SunOSVirtual({})
    assert virtual.platform == 'SunOS'

# Generated at 2022-06-13 04:28:02.059167
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    v = SunOSVirtual()
    assert v.platform == 'SunOS'

# Generated at 2022-06-13 04:28:07.539380
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = AnsibleModule(argument_spec={})

    facts_mock = {
        'product_name': 'Oracle Corporation',
        'distribution': 'Oracle Solaris'
    }

    def get_bin_path_mock(name, required=False):
        return "/path/to/bin/%s" % name

    module.get_bin_path = get_bin_path_mock
    module.run_command = run_command

    def run_command_mock(cmd, *args, **kwargs):
        if "zonename" in cmd:
            return (0, 'global\n', '')
        if "smbios" in args:
            return (0, '', '')
        if "modinfo" in cmd:
            return (1, '', '')

# Generated at 2022-06-13 04:28:16.764168
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes

    m = basic.AnsibleModule(
        argument_spec=dict()
    )

    # Note: the test case for detecting hypervisors present in a zone are based on the
    # presence of the output of the 'modinfo' command.
    # The test case for branded zone is based on presence of directory /.SUNWnative.
    # To avoid creating a SunOS zone and installing those tools, we are testing against
    # files instead.

    # Global zone, first try to detect a branded zone (by the /.SUNWnative directory)
    setattr(m, 'run_command', lambda *args, **kwargs: (0, "/SUNW native", ""))

# Generated at 2022-06-13 04:28:22.831785
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    obj1 = SunOSVirtual('ansible.module_utils.facts.virtual.sunos.SunOSVirtual')
    obj2 = SunOSVirtual('ansible.module_utils.facts.virtual.sunos.SunOSVirtual', 'ansible.module_utils.facts.virtual.base.Virtual')
    assert obj1.platform == 'SunOS'
    assert obj2.platform == 'SunOS'


# Generated at 2022-06-13 04:28:24.801882
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    ''' Unit test for constructor of class SunOSVirtualCollector. '''
    collector = SunOSVirtualCollector()
    assert collector is not None