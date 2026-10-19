

# Generated at 2022-06-13 04:20:45.022450
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual import SunOSVirtual as SunOSVirtualModule
    module = SunOSVirtualModule()
    module.run_command = lambda *cmd: (0, '', '')
    module.get_bin_path = lambda *cmd: cmd[0]

    # Test that the function correctly differentiates between zone and global zone
    module.run_command = lambda *cmd: {b'zonename': (0, 'a', '')}.get(cmd[0], (0, '', ''))
    assert SunOSVirtual(module).get_virtual_facts() == {
        'container': 'zone',
        'virtualization_tech_guest': {'zone'},
        'virtualization_tech_host': set()
    }

# Generated at 2022-06-13 04:20:53.928723
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    """
    Unit test for method get_virtual_facts of class SunOSVirtual
    """
    virt = SunOSVirtual({})
    assert virt is not None

    # Fake the module and command
    virt.module = FakeAnsibleModule('', 'smbios')

    # Fake the output of command
    virt.module.run_command.return_value = (0, "VirtualBox\nParallels\nHVM domU\nVMware", "")
    # Run the function and check the result
    result = virt.get_virtual_facts()

# Generated at 2022-06-13 04:20:55.685806
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    """ Test if all attributes of SunOSVirtual are set correctly """
    SunOSVirtual_obj = SunOSVirtual(dict())
    assert SunOSVirtual_obj.platform == 'SunOS'

# Generated at 2022-06-13 04:20:59.967696
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # Get a SunOSVirtual instance
    v = SunOSVirtual({})

    # Mock the module so we can control the command executed
    v.module = MagicMock()

    # Test on a global zone
    v.module.run_command.return_value = (0, 'global\n', '')
    facts = v.get_virtual_facts()
    assert not facts['container']
    assert {'zone'} == facts['virtualization_tech_host']
    assert 'virtualization_tech_guest' not in facts
    assert 'virtualization_type' not in facts
    assert 'virtualization_role' not in facts

    # Test on a non global zone
    v.module.run_command.return_value = (0, 'testzone\n', '')
    facts = v.get_virtual_facts()

# Generated at 2022-06-13 04:21:02.481704
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    vm = SunOSVirtual(dict())
    assert vm.platform == 'SunOS'



# Generated at 2022-06-13 04:21:05.742273
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual = SunOSVirtual({'module': None})
    assert virtual.virtualization_type == 'zone'
    assert virtual.virtualization_role == 'guest'

# Generated at 2022-06-13 04:21:07.577238
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    module = None
    x = SunOSVirtual(module)
    assert x.platform == 'SunOS'


# Generated at 2022-06-13 04:21:09.648130
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    # Test creating object to run facts on
    x = SunOSVirtualCollector()
    assert x
    assert x._platform == 'SunOS'

# Generated at 2022-06-13 04:21:12.275222
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    s = SunOSVirtual()
    assert str(s.__class__) == 'facts.virtual.sunos.SunOSVirtual'

# Generated at 2022-06-13 04:21:23.005508
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():

    # Zone
    init_return = {"changed": False, "rc": 0, "stderr": "", "stdout": "global", "warnings": []}
    init_ansible_module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    init_ansible_module.run_command = Mock(return_value=init_return)
    init_ansible_module.get_bin_path = Mock(return_value='/usr/bin/zonename')
    sunosvirtual = SunOSVirtual(init_ansible_module)
    result = sunosvirtual.get_virtual_facts()
    assert 'virtualization_tech_guest' in result
    assert 'virtualization_tech_host' in result
    assert result['virtualization_tech_host'] == set(['zone'])

# Generated at 2022-06-13 04:21:36.010088
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    assert SunOSVirtualCollector.platform == 'SunOS'
    assert SunOSVirtualCollector._fact_class == SunOSVirtual


# Generated at 2022-06-13 04:21:36.792808
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    SunOSVirtualCollector()

# Generated at 2022-06-13 04:21:39.160983
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual_facts = SunOSVirtual()
    assert virtual_facts._platform == 'SunOS'

# Generated at 2022-06-13 04:21:43.072404
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = FakeModule()
    facts = SunOSVirtualCollector(module).get_virtual_facts()
    assert 'zone' == facts['virtualization_tech_host']
    assert 'zone' == facts['virtualization_tech_guest']

# Generated at 2022-06-13 04:21:46.018266
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    module = MagicMock()

    v = SunOSVirtual(module=module)

    assert v.module == module
    assert v.platform == 'SunOS'

# Generated at 2022-06-13 04:21:50.873299
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # Create an instance of the class to be tested
    virtual_facts = SunOSVirtual()

    # This test will check if the function returns an empty dict when
    # no virtualization technology is found.
    virtual_facts.module.run_command = lambda x: (1, '', '')
    virtual_facts.module.get_bin_path = lambda x: ''
    assert {} == virtual_facts.get_virtual_facts()


# Generated at 2022-06-13 04:21:53.486933
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    from ansible.module_utils.facts.virtual.sunos import SunOSVirtual
    sunos_virtual = SunOSVirtual('/usr/bin/ansible')
    assert(sunos_virtual is not None)


# Generated at 2022-06-13 04:21:56.730357
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    v = SunOSVirtual({}, {}, {})
    assert v.platform == 'SunOS'
    assert v.facts == {}

# Generated at 2022-06-13 04:21:59.286769
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    # init and test class instance
    SunOSVirtual().get_virtual_facts()

# Generated at 2022-06-13 04:22:04.237406
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    v = SunOSVirtual(module)

    virtual_facts = v.get_virtual_facts()
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts

# Generated at 2022-06-13 04:22:18.565405
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    try:
        SunOSVirtualCollector()
        assert True
    except Exception:
        assert False

# Generated at 2022-06-13 04:22:27.787587
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    v = SunOSVirtual({})

    # Test with zone
    v.module.run_command = Mock(return_value=(0, 'global', ''))
    v.module.get_bin_path = Mock(return_value='/bin/zonename')
    v.os.path.exists = Mock(side_effect=[False, True, False, True, False, False, False, False, False, False, True, False, True, False, False])
    facts = v.get_virtual_facts()
    assert facts['container'] == 'zone'
    assert 'virtualization_type' not in facts
    assert 'virtualization_role' not in facts

    # Test with vmware branded zone
    v.module.run_command = Mock(return_value=(0, 'global', ''))

# Generated at 2022-06-13 04:22:40.167722
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # Test empty output
    module = MockModule(params={})
    SunOSVirtual.module = module
    SunOSVirtual.get_virtual_facts()
    module.run_command.assert_called_with('/usr/sbin/virtinfo -p')
    assert SunOSVirtual.facts == {}
    module.run_command.reset_mock()

    # Test ldoms
    module = MockModule(params={})
    module.run_command.return_value = (0, """DOMAINROLE|impl=LDoms|control=false|io=false|service=false|root=false""", "")
    SunOSVirtual.module = module
    SunOSVirtual.get_virtual_facts()
    module.run_command.assert_called_with('/usr/sbin/virtinfo -p')
    assert SunOSVirtual.facts

# Generated at 2022-06-13 04:22:42.326902
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    c = SunOSVirtualCollector()
    assert c._fact_class == SunOSVirtual
    assert c._platform == 'SunOS'

# Generated at 2022-06-13 04:22:47.009357
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():

    # Instantiate class SunOSVirtual
    fact_obj = SunOSVirtual({})

    # Check value of virtualization_type
    assert fact_obj.virtualization_type is None

    # Check value of virtualization_role
    assert fact_obj.virtualization_role is None

# Generated at 2022-06-13 04:22:48.544980
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    v = SunOSVirtual({})
    assert v.get_virtual_facts() == {}



# Generated at 2022-06-13 04:22:59.602118
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    module = AnsibleModuleMock()
    module.run_command.return_value = 0, '', ''
    module.get_bin_path.side_effect = lambda x: x
    sv = SunOSVirtual(module)
    assert sv.module == module
    assert isinstance(sv.virtual_facts, dict)
    assert len(sv.virtual_facts) == 0

# Unit tests for the facts provided by class SunOSVirtual

# Generated at 2022-06-13 04:23:02.055200
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    result = SunOSVirtual.get_virtual_facts("")
    assert result is not None

# Generated at 2022-06-13 04:23:10.674399
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    from ansible.module_utils.facts import gather_subset

    # Create a mock module
    from ansible.module_utils.facts import ModuleFacts
    module = ModuleFacts(
            # The argument name of module_arg_spec, 'platform' must match
            # the value of _platform of VirtualCollector, or the VirtualCollector
            # of this platform will not be loaded.
            platform='SunOS',
            # The value of 'platform' must match the platform name in the
            # inventory file
            inventory_platform='SunOS',
            gather_subset=gather_subset
    )
    # Define some mocked functions to be called by the module
    # `get_bin_path` is called to check if the binary exists.
    def mock_get_bin_path(path, required=False):
        return path


# Generated at 2022-06-13 04:23:17.965190
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    datadir = os.path.join(os.path.dirname(__file__), 'fixtures/virtual')
    url_base = "file://" + datadir
    module = DummyModule()

    virtual = SunOSVirtual(module)

    for fixture in ['SunOS_virtual.txt', 'SunOS_zone.txt', 'SunOS_smbios.txt']:
        virtual.get_file_lines = Mock(return_value=get_file_content(url_base, fixture))
        fact = virtual.get_virtual_facts()
        assert fact == get_file_content(url_base, fixture + '.ansible_facts')

# Generated at 2022-06-13 04:23:46.056718
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = AnsibleModule(argument_spec = dict())
    virtual = SunOSVirtual(module)
    virtual_facts = virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'xen'
    assert virtual_facts['virtualization_role'] == 'guest'

# Generated at 2022-06-13 04:23:52.603589
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = FakeAnsibleModule()

    def isdir_mock(path):
        return os.path.normpath(path) == os.path.normpath('/.SUNWnative')

    def exists_mock(path):
        return os.path.normpath(path) == os.path.normpath('/proc/vz')

    if module.virt_facts == None:
        module.virt_facts = SunOSVirtual(module)

    module.virt_facts.module.get_bin_path = FakeGetBinPath()
    module.virt_facts.module.run_command = FakeRunCommand()

    module.virt_facts.os.path.isdir = isdir_mock
    module.virt_facts.os.path.exists = exists_mock

    vf = module.virt_facts.get_

# Generated at 2022-06-13 04:23:54.573208
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    assert SunOSVirtualCollector().platform == 'SunOS'
    assert SunOSVirtualCollector()._fact_class == SunOSVirtual

# Generated at 2022-06-13 04:23:56.057923
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virt_facts = SunOSVirtual(dict())
    assert virt_facts.virtual_facts['platform'] == 'SunOS'



# Generated at 2022-06-13 04:23:59.620680
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    x = SunOSVirtual({})
    x.module.run_command =  lambda x: (0, "DOMAINROLE|impl=LDoms|control=false|io=false|service=false|root=false\nDOMAINROLE|impl=LDoms|control=false|io=true|service=true|root=false", '')
    x.module.get_bin_path = lambda x: True
    print(x.get_virtual_facts())

# Generated at 2022-06-13 04:24:02.358135
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual_facts = SunOSVirtual({}, {})
    assert virtual_facts.platform == 'SunOS'
    assert virtual_facts.virtualization_type is None
    assert virtual_facts.virtualization_role is None
    assert virtual_facts.container is None

# Generated at 2022-06-13 04:24:06.430080
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    # construct an instance of SunOSVirtual class,
    # and test if it is an instance of Virtual class
    sunos_virtual_facts = SunOSVirtual({})
    assert isinstance(sunos_virtual_facts, Virtual)
    assert sunos_virtual_facts.platform == 'SunOS'

# Generated at 2022-06-13 04:24:07.629676
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    # Run a very minimal test.
    SunOSVirtual({}, {})

# Generated at 2022-06-13 04:24:10.963365
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # All the tests are done in class virtual_collector.
    # Method get_virtual_facts is called from there.
    pass

# Generated at 2022-06-13 04:24:12.072141
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    """
    Constructor test
    """
    virtual_facts = SunOSVirtual({})
    assert virtual_facts.platform == 'SunOS'

# Generated at 2022-06-13 04:25:08.587248
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # Create a dummy module
    module = AnsibleModule(argument_spec={})

    # Create a dummy command
    class Command(object):
        def __init__(self, rc, out, err):
            self.rc = rc
            self.stdout = out
            self.stderr = err

        def run(self, *args, **kwargs):
            return (self.rc, self.stdout, self.stderr)

    # Create a dummy file
    class File(object):
        def __init__(self, exists, isdir):
            self.exists = exists
            self.isdir = isdir

        def exists(self):
            return self.exists

        def isdir(self):
            return self.isdir

    # Create a dummy module class

# Generated at 2022-06-13 04:25:20.255709
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # Set up Virtual instance
    virtual_instance = SunOSVirtual()

    # No stubs
    assert virtual_instance.get_virtual_facts() is None

    # Fake stubs
    class MockModule:
        def __init__(self):
            self.run_command = lambda *args, **kwargs: (0, '/usr/sbin/virtinfo -p\nfake\nDOMAINROLE|impl=LDoms|control=true|io=true|service=false|root=false', '')
            self.get_bin_path = lambda *args, **kargs: '/usr/sbin/virtinfo'
    virtual_instance.module = MockModule()

# Generated at 2022-06-13 04:25:24.422989
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    x = SunOSVirtualCollector()
    assert isinstance(x, SunOSVirtualCollector)
    assert isinstance(x, VirtualCollector)
    assert x._platform == 'SunOS'
    assert x._fact_class == SunOSVirtual


# Generated at 2022-06-13 04:25:25.667280
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual = SunOSVirtual(dict())

# Generated at 2022-06-13 04:25:29.447976
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    vc = SunOSVirtualCollector()
    assert vc.platform == 'SunOS'
    assert vc._fact_class == SunOSVirtual
    assert vc._platform == 'SunOS'


# Generated at 2022-06-13 04:25:32.614786
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    v = SunOSVirtual({})
    assert v.name == 'SunOS_virtual'
    assert v.platform == 'SunOS'
    assert v.virtualization_type == 'zone'
    assert v.virtualization_role == 'host'


# Generated at 2022-06-13 04:25:33.708027
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    '''Unit test for constructor of class SunOSVirtual'''
    SunOSVirtual()

# Generated at 2022-06-13 04:25:35.526260
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    sunosvcc = SunOSVirtualCollector()
    assert sunosvcc._platform is not None
    assert sunosvcc._fact_class is not None

# Generated at 2022-06-13 04:25:40.778260
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    module = type('', (), {})()
    module.run_command = lambda x: (0, '', '')
    module.get_bin_path = lambda x: '/bin/' + x

    v = SunOSVirtual(module)
    v.get_virtual_facts()
    assert v.virtualization_type == "vmware"
    assert v.virtualization_role == "guest"
    assert v.virtualization_tech_host == set()
    assert v.virtualization_tech_guest == set(["vmware"])
    assert v.container == "zone"

# Generated at 2022-06-13 04:25:51.112225
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    from ansible.module_utils.facts.sunos import SunOSVirtual
    module = AnsibleModuleMock(exit_json=None)
    module.run_command = AnsibleModuleMock.run_command
    v_obj = SunOSVirtual(module=module)
    # Stubbing the module.run_command() method so we can test whether it has been called with the right command
    def check_run_command(command, check_rc=True, close_fds=True, executable=None, data=None, binary_data=False, path_prefix=None):
        if "zonename" in command:
            return (0, "global", "")

# Generated at 2022-06-13 04:27:45.430491
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # Mock module object
    class MockModule(object):
        @staticmethod
        def get_bin_path(bin_path, required=False):
            return bin_path

        @staticmethod
        def run_command(command):
            if command[0] == 'zonename':
                return 0, 'global', ''
            elif command[0] == 'modinfo':
                return 0, 'ID CLASS   SIZE     REV  STATE NAME' \
                         '    a   467427      1  4.0  O.K. VMware' \
                         ' |   b   467571      1  4.0  O.K. VirtualBox', ''
            else:
                return 0, '', ''

    module = MockModule()

    # Test on a machine running in a global zone
    virtual = SunOSVirtual(module)
   

# Generated at 2022-06-13 04:27:46.261249
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    SunOSVirtualCollector()

# Generated at 2022-06-13 04:27:50.721227
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    from ansible.module_utils.facts.virtual.sunos import SunOSVirtualCollector
    svc = SunOSVirtualCollector()
    assert svc.platform == 'SunOS'
    assert svc._fact_class == SunOSVirtual



# Generated at 2022-06-13 04:27:52.991803
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    """
    This unit test verifies that the VirtualCollector class is not abstract and
    can be constructed.
    """
    SunOSVirtualCollector()

# Generated at 2022-06-13 04:27:57.964697
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    # Create a SunOSVirtual object
    my_SunOSVirtual = SunOSVirtual(module=None)

    # Check it's really a SunOSVirtual object
    if isinstance(my_SunOSVirtual, SunOSVirtual) is False:
        raise AssertionError("Failed to instantiate SunOSVirtual object")

    # Tests will probably be added later but for the moment we can assume that's it :-)


# Generated at 2022-06-13 04:28:04.857667
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = AnsibleModule(argument_spec={})
    # host is not virtualized
    modinfo = "ID\t0\tvboxguest\t\tVirtualBox Guest Additions for SunOS\n"
    smbios = "VMware\n"
    virtinfo = "virtinfo: LDoms not available\n"
    rc = 0
    virtual = SunOSVirtual(module=module)
    facts = virtual.get_virtual_facts(modinfo=modinfo, smbios=smbios, virtinfo=virtinfo, rc=rc)
    assert not facts['virtualization_type']
    assert not facts['virtualization_role']
    assert facts['virtualization_tech_guest'] == set()
    assert facts['virtualization_tech_host'] == set()

    # host is a guest

# Generated at 2022-06-13 04:28:05.653968
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    v = SunOSVirtual({})
    assert v.facts == {}


# Generated at 2022-06-13 04:28:07.122918
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual_obj = SunOSVirtual()
    assert virtual_obj._platform == 'SunOS'

# Generated at 2022-06-13 04:28:08.109421
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    module_mock = type('module_mock', (object,), {})()
    SunOSVirtualCollector(module_mock)

# Generated at 2022-06-13 04:28:17.163331
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # First test case: we are not in any kind of virtual environment
    module = MockModule()
    cmds = {
        'zonename': '',
        'modinfo': '',
        'virtinfo': '',
        'smbios': '',
    }
    module.get_bin_path.side_effect = lambda x: cmds.get(x, '')
    virt_facts = SunOSVirtual(module).get_virtual_facts()
    assert 'virtualization_type' not in virt_facts
    assert 'virtualization_role' not in virt_facts
    assert 'virtualization_tech_host' not in virt_facts
    assert 'virtualization_tech_guest' not in virt_facts
# TODO: more test cases
# - Global zone of a host running Domains
# - Guest of a host running LDoms
