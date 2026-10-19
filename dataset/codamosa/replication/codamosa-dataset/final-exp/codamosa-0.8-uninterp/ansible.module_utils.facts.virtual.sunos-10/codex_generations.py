

# Generated at 2022-06-13 04:20:37.875051
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual_facts = SunOSVirtual({})

    assert virtual_facts.virtual != None
    assert virtual_facts._platform == 'SunOS'

# Generated at 2022-06-13 04:20:39.796802
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual = SunOSVirtual({}, {}, {}, [])
    assert virtual.__dict__ == {}

# Generated at 2022-06-13 04:20:41.479194
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    from ansible.module_utils.facts.virtual.sunos.sunos import SunOSVirtual
    SunOSVirtual()

# Generated at 2022-06-13 04:20:44.082158
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    sysctl = SunOSVirtualCollector()
    assert SunOSVirtual == sysctl.fact_class
    assert 'SunOS' == sysctl.platform

# Generated at 2022-06-13 04:20:48.523576
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # Prepare unit test
    module_patcher = ModulePatcher()
    zonename_patcher = ModulePatcher('zonename')
    virtinfo_patcher = ModulePatcher('virtinfo')
    smbios_patcher = ModulePatcher('smbios')
    module_patcher.set_module_args(dict(gather_subset='!all,virtual'))

    # Run unit test

    # Without zone
    module_patcher.mock_run_command(rc=0, out='global', command=zonename_patcher.BIN_PATH)
    # Without vmware tools
    module_patcher.mock_run_command(rc=1, out='', command=smbios_patcher.BIN_PATH)
    # Without virtinfo

# Generated at 2022-06-13 04:20:56.387351
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    import pytest
    from ansible.module_utils.facts.virtual.sunos import SunOSVirtual

    correct_facts = {
        'virtualization_type': 'zone',
        'virtualization_role': 'guest',
        'container': 'zone',
        'virtualization_tech_guest': {'zone'},
        'virtualization_tech_host': set()
    }

    class MockModuleHelper(object):
        @staticmethod
        def get_bin_path(program):
            if program == 'zonename':
                def run_command(cmd):
                    return 0, 'nonglobal', 'stderr'

            return run_command

    # Mock class 'SunOSVirtual'

# Generated at 2022-06-13 04:20:59.936172
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    collector = SunOSVirtualCollector()
    assert collector._fact_class == SunOSVirtual
    assert collector._platform == 'SunOS'

# Generated at 2022-06-13 04:21:09.995986
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    from ansible_collections.ansible.community.tests.unit.compat.mock import MagicMock
    from ansible.module_utils.facts.virtual.sunos.SunOS import SunOSVirtualCollector

    mocked_module = MagicMock()

    collector = SunOSVirtualCollector(mocked_module, 'SunOS')

    assert collector._platform == 'SunOS'
    assert collector._fact_class.platform == 'SunOS'
    assert collector._fact_class.__name__ == 'SunOSVirtual'
    assert collector._fact_class.__module__ == 'ansible_collections.ansible.community.plugins.module_utils.facts.virtual.sunos.SunOS'

# Generated at 2022-06-13 04:21:19.557906
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # Set up a module and its arguments
    module = MockANSIRModule()
    facts = dict()

    # Set up some constants
    rc = 0
    out = ''
    err = ''

    # Set up the mocks
    module.run_command.side_effect = [
        (rc, 'global', err),  # zonename
        (rc, out, err),
        (rc, out, err)
    ]
    module.get_bin_path.side_effect = [
        '/usr/sbin/zonename',
        '/usr/sbin/modinfo'
    ]

    # Create the object
    virtual = SunOSVirtual(module=module)

    # Get the virtual facts
    facts = virtual.get_virtual_facts()

    # Check the facts
    assert 'virtualization_role' in facts
   

# Generated at 2022-06-13 04:21:28.319454
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = MockANSModule()
    sunosvirtual = SunOSVirtual(module)
    facts = sunosvirtual.get_virtual_facts()

    # Check that we only have the expected keys
    expected_keys = {
        'virtualization_tech_guest',
        'virtualization_tech_host',
        'virtualization_role',
        'virtualization_type',
        'container'
    }
    assert(expected_keys == facts.keys()), "Expected keys:\n\t{}\nGot:\n\t{}".format(
        '\n\t'.join(expected_keys),
        '\n\t'.join(facts.keys()))


# Generated at 2022-06-13 04:21:43.018830
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    sunos_vc = SunOSVirtualCollector()
    assert sunos_vc._fact_class == SunOSVirtual
    assert sunos_vc._platform == 'SunOS'

# Generated at 2022-06-13 04:21:53.473752
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # Test data
    # Data for a zone
    ldd_data_for_a_zone = [
        'libc.so.1 => /lib/libc.so.1',
        'libuutil.so.1 => /lib/libuutil.so.1',
        'libdoor.so.1 => /lib/libdoor.so.1',
        'libgen.so.1 => /usr/lib/libgen.so.1',
        'ldd: libvboxguest.so: open failed: No such file or directory'
    ]
    # Data for a branded zone (solaris 8 or 9)

# Generated at 2022-06-13 04:21:55.775554
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    assert SunOSVirtualCollector._platform == 'SunOS'
    assert SunOSVirtualCollector._fact_class == SunOSVirtual

# Generated at 2022-06-13 04:21:59.836492
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual_facts = SunOSVirtual()
    assert isinstance(virtual_facts, SunOSVirtual)
    assert virtual_facts.platform == 'SunOS'

# Generated at 2022-06-13 04:22:02.688032
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    virtual_collector = SunOSVirtualCollector()
    assert virtual_collector._platform == 'SunOS'
    assert virtual_collector._fact_class == SunOSVirtual

# Generated at 2022-06-13 04:22:13.192405
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    SunOSVirtual._module = AnsibleModule(
        argument_spec = {
        },
    )

# Generated at 2022-06-13 04:22:17.966700
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    # Constructor for class SunOSVirtualCollector should create an object
    sunos_virtual_obj = SunOSVirtualCollector()

    # The object created above should be of class SunOSVirtualCollector
    assert isinstance(sunos_virtual_obj, SunOSVirtualCollector)


# Generated at 2022-06-13 04:22:19.454570
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    # Constructor should not throw an exception
    SunOSVirtualCollector()

# Generated at 2022-06-13 04:22:28.423134
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module_mock = MockModule()
    module_mock.params = {}
    module_mock.run_command = Mock(return_value=(0, 'zonename\nglobal', ''))
    module_mock.get_bin_path = Mock(return_value=True)
    module_mock.get_bin_path.side_effect = lambda arg: arg
    sunos_virtual = SunOSVirtual(module_mock)

    # Test vbox VM as zone
    module_mock.run_command = Mock(return_value=(0, 'zonename\nglobal', ''))

# Generated at 2022-06-13 04:22:40.287635
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = AnsibleModuleMock({})
    obj = SunOSVirtual(module=module)

    # Fake running inside a zone
    obj.module.run_command = Mock(return_value=(0, "global\n", ""))
    obj.get_virtual_facts()
    assert obj.facts['container'] == 'zone'
    assert obj.facts['virtualization_tech_host'] == set(['zone'])
    assert obj.facts['virtualization_tech_guest'] == set([])

    # Fake running inside a branded zone
    obj.module.get_bin_path = Mock(return_value=None)
    obj.is_file = Mock(return_value=False)
    os.path.isdir = Mock(return_value=True)
    obj.get_virtual_facts()
    assert obj.facts['container']

# Generated at 2022-06-13 04:22:57.660404
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    vs = SunOSVirtual({'module': None})
    assert vs.platform == 'SunOS'
    assert vs.virtualization_type == ''
    assert vs.virtualization_role == ''
    assert vs.container == ''
    assert vs.virtualization_tech_guest == set()
    assert vs.virtualization_tech_host == set()

# Generated at 2022-06-13 04:23:00.900603
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    """
    unit test for method get_virtual_facts of class SunOSVirtual
    """
    module = AnsibleModule(argument_spec=dict())
    virtual = SunOSVirtual(module=module)
    """
    TODO: write unit test (data virtualization_facts.json)
    """

# Generated at 2022-06-13 04:23:02.105475
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    assert SunOSVirtualCollector() is not None

# Generated at 2022-06-13 04:23:06.232293
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    '''
    Test for SunOSVirtual.get_virtual_facts().
    :return:
    '''
    from ansible.module_utils.facts.collector.sunos import SunOSVirtual

    mock_module = MagicMock()
    mock_module.run_command = MagicMock(return_value=(0, '', ''))
    mock_module.get_bin_path = MagicMock(return_value='/usr/bin/zonename')
    sun = SunOSVirtual(mock_module)

    sun.facts = {'system': {'sunos': {'brand_string': 'solaris'}}}

    # Global zone
    sun.facts['system']['sunos']['brand_string'] = 'solaris'
    rc, out, err = sun.module.run_command.return_value


# Generated at 2022-06-13 04:23:08.192501
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    s = SunOSVirtual({})
    assert s.platform == 'SunOS'

# Generated at 2022-06-13 04:23:11.025643
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    obj = SunOSVirtualCollector()
    assert(obj.platform == 'SunOS')
    assert(obj._fact_class is SunOSVirtual)


# Generated at 2022-06-13 04:23:19.505579
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    # Test bare metal
    v = SunOSVirtual({'ansible_facts': {'is_sunos': True}})
    assert not v.is_virtual()

    # Test zone
    v = SunOSVirtual({'ansible_facts': {'is_sunos': True, 'zonename': 'global'}})
    assert v.is_virtual()
    assert not v.is_container()
    assert not v.is_zone()

    v = SunOSVirtual({'ansible_facts': {'is_sunos': True, 'zonename': 'non-global'}})
    assert v.is_virtual()
    assert v.is_container()
    assert v.is_zone()

    # Test branded zone

# Generated at 2022-06-13 04:23:31.377879
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = FakeAnsibleModule()
    module.run_command = FakeRunCommand(module)
    module.run_command.set_command("/usr/sbin/virtinfo -p", 'PID|3983\nDOMAINROLE|impl=LDoms|control=false|io=false|service=false|root=false\n')
    module.run_command.set_command("/usr/bin/zonename", 'global\n')
    module.run_command.set_command("/usr/bin/modinfo", 'id:    161  class:    misc  rev:    1.0  hwrev:  1.1\n  compat:  h/w\n  name:  VMware VMXNET3 Virtual NIC Driver\n\n')

# Generated at 2022-06-13 04:23:41.250881
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = FakeAnsibleModule()
    module.run_command = run_command
    module.get_bin_path = get_bin_path
    module.get_all_text = get_all_text
    module.is_file = is_file
    fact_module = SunOSVirtual(module)
    fact_module.get_virtual_facts()
    virtual_facts = fact_module.virtual_facts
    if 'virtualization_tech_guest' not in virtual_facts:
        assert False, "virtualization_tech_guest is missing"
    else:
        assert virtual_facts['virtualization_tech_guest'] == {'zone', 'vmware'}, "virtualization_tech_guest contains invalid values"

# Generated at 2022-06-13 04:23:42.362914
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    x = SunOSVirtualCollector()
    assert x._platform == 'SunOS'

# Generated at 2022-06-13 04:24:18.495604
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    def set_module_args(args):
        module_args = dict()
        for k, v in args.items():
            module_args[k] = v
        module.params = module_args

    module = Mock()
    set_module_args({})

    def get_bin_path_side_effect(arg):
        if arg == 'zonename':
            return '/usr/bin/zonename'
        if arg == 'modinfo':
            return 'modinfo'
        if arg == 'smbios':
            return 'smbios'
        if arg == 'virtinfo':
            return 'virtinfo'

    module.get_bin_path.side_effect = get_bin_path_side_effect


# Generated at 2022-06-13 04:24:19.322223
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    assert SunOSVirtual(dict()) != None

# Generated at 2022-06-13 04:24:26.567930
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = None

    virtual_facts = SunOSVirtual(module).get_virtual_facts()

    assert isinstance(virtual_facts, dict)
    assert 'virtualization_type' in virtual_facts

    # ldom tests
    virtual_facts1 = {
        'container': 'zone',
        'virtualization_role': 'host (control,io,service,root)',
        'virtualization_type': 'ldom',
        'virtualization_tech_guest': set(['ldom', 'zone']),
        'virtualization_tech_host': set(['zone']),
    }


# Generated at 2022-06-13 04:24:38.101580
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    Virt = SunOSVirtual()
    # This is dummy data. The output of the get_virtual_facts method is currently tested
    # on a Solaris 11 Express installation, the output for a Solaris 10 branded zone on
    # the same box and a Solaris 10 installation. (They could be mixed into separate tests.)
    # The output of this method can also be influenced by the host system, as you can see
    # in the code above.
    expected_facts = {'virtualization_type': 'vmware',
                      'virtualization_role': 'guest',
                      'container': 'zone',
                      'virtualization_tech_host': set(['zone']),
                      'virtualization_tech_guest': set(['zone', 'vmware'])}
    assert expected_facts == Virt.get_virtual_facts()

# Generated at 2022-06-13 04:24:39.900879
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    module = None
    sunos_virtual_collector = SunOSVirtualCollector(module)
    assert isinstance(sunos_virtual_collector._fact_class, type(SunOSVirtual))

# Generated at 2022-06-13 04:24:44.897318
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    """This is a constructor test for the SunOSVirtualCollector class
    """
    x = SunOSVirtualCollector()
    assert isinstance(x, SunOSVirtualCollector)

if __name__ == '__main__':
    import pytest
    pytest.main([__file__])

# Generated at 2022-06-13 04:24:46.479915
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual = SunOSVirtual()
    assert virtual.__class__.__name__ == 'SunOSVirtual'

# Generated at 2022-06-13 04:24:48.425637
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    """
    Checks whether SunOSVirtualCollector can be instantiated.
    """
    collector = SunOSVirtualCollector()

    assert collector is not None

# Generated at 2022-06-13 04:24:49.960934
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    sunos = SunOSVirtual(None)
    assert SunOSVirtual



# Generated at 2022-06-13 04:24:57.519663
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    test_module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True,
    )

    test_SunOSVirtual = SunOSVirtual(test_module)

    expected_facts = {'virtualization_role': 'guest',
                      'container': 'zone',
                      'virtualization_type': 'vmware',
                      'virtualization_tech_host': set(),
                      'virtualization_tech_guest': set(['zone', 'vmware'])}

    assert expected_facts == test_SunOSVirtual._get_virtual_facts()



# Generated at 2022-06-13 04:25:49.738262
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    module = SunOSVirtualCollector.get_module()
    result = SunOSVirtualCollector.collect(module)
    assert isinstance(result, dict)
    assert 'virtualization_tech_guest' in result
    assert 'virtualization_tech_host' in result
    assert 'virtualization_type' in result
    assert 'virtualization_role' in result
    assert 'container' in result

# Generated at 2022-06-13 04:25:51.111820
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
  collector = SunOSVirtualCollector(dict())
  assert isinstance(collector, SunOSVirtualCollector)

# Generated at 2022-06-13 04:26:00.020874
# Unit test for method get_virtual_facts of class SunOSVirtual

# Generated at 2022-06-13 04:26:02.674417
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    module = MockModule()
    VirtualCollector._platform = 'SunOS'

    assert str(SunOSVirtual(module)) == 'SunOSVirtual'


# Generated at 2022-06-13 04:26:04.560888
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    sunos_virtual = SunOSVirtual(dict())
    assert sunos_virtual._platform == 'SunOS'
    assert sunos_virtual._fact_class._platform == 'SunOS'

# Generated at 2022-06-13 04:26:13.292182
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # pylint: disable=protected-access, unused-argument
    module = create_fake_module()
    collector = SunOSVirtualCollector(module=module)
    virtual = collector._fact_class(module=module)

    # Without ldom
    fake_path_exists('/proc/vz')
    module.run_command.return_value = (0, 'DOMAINROLE|impl=LDoms|control=false|io=false|service=false|root=false', '')
    virtual_facts = virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'ldom'
    assert virtual_facts['virtualization_role'] == 'guest'
    assert 'ldm' in virtual_facts['virtualization_tech_guest']

    # With /proc/vz
    fake_path

# Generated at 2022-06-13 04:26:14.301307
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    collector = SunOSVirtualCollector()
    assert collector.platform == 'SunOS'

# Generated at 2022-06-13 04:26:16.657490
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # Initialize the instance
    SunOSVirtual_instance = SunOSVirtual()
    # Run the method get_virtual_facts
    SunOSVirtual_result = SunOSVirtual_instance.get_virtual_facts()
    assert not SunOSVirtual_result

# ===========================================

# Generated at 2022-06-13 04:26:20.594190
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    facts = SunOSVirtual({}, {})
    assert facts._platform == "SunOS"
    assert facts._fact_class == SunOSVirtual

# Generated at 2022-06-13 04:26:21.762910
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    vc = SunOSVirtualCollector(None)
    assert vc.platform == 'SunOS'

# Generated at 2022-06-13 04:28:04.731607
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    """
    Test the get_virtual_facts method of SunOSVirtual
    """
    module = AnsibleModule(argument_spec={})
    module.run_command = MagicMock(return_value=(0, "global", ""))
    module.get_bin_path = MagicMock(side_effect=lambda x: '/bin/zonename')
    sunos_virtual = SunOSVirtual(module)

    assert sunos_virtual.get_virtual_facts() == {'virtualization_tech_host': {'zone'}, 'virtualization_tech_guest': set()}

    module = AnsibleModule(argument_spec={})
    module.run_command = MagicMock(return_value=(0, "", ""))
    module.get_bin_path = MagicMock(side_effect=lambda x: '/bin/zonename')


# Generated at 2022-06-13 04:28:06.743676
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual = SunOSVirtual(None)
    assert virtual.platform == 'SunOS'

# Generated at 2022-06-13 04:28:14.495016
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    module_name = 'ansible.module_utils.facts.virtual.sunos.SunOSVirtualCollector'
    args = { "module": "foo" }
    sun_virtual_collector = SunOSVirtualCollector(**args)
    assert sun_virtual_collector
    assert sun_virtual_collector._fact_class.__name__ == "SunOSVirtual"
    assert sun_virtual_collector._platform == "SunOS"
    assert sun_virtual_collector._name == "SunOS"
    assert sun_virtual_collector._module == "foo"

# Generated at 2022-06-13 04:28:21.696100
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    virtual = SunOSVirtual({})
    virtual.module.run_command = lambda x: (0, "", "")

    def exists(path):
        return True

    virtual.module.fetch_file = lambda path, data: (None, None)
    virtual.module.get_bin_path = lambda command: True
    virtual.module._is_executable = exists
    virtual.module.exists = exists
    assert virtual.get_virtual_facts() == {}

# Generated at 2022-06-13 04:28:30.874143
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():

    # Create an instance of class SunOSVirtual
    test = SunOSVirtual()

    # Try to run get_virtual_facts with various values for virtualization_type

# Generated at 2022-06-13 04:28:32.550343
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    # Instantiate the class
    SunOSVirtualCollector()

# Generated at 2022-06-13 04:28:33.344495
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    SunOSVirtualCollector()

# Generated at 2022-06-13 04:28:35.939517
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    assert SunOSVirtualCollector.platform == 'SunOS'
    assert SunOSVirtualCollector.priority == 10
    assert SunOSVirtualCollector._platform == 'SunOS'
    assert SunOSVirtualCollector._fact_class == SunOSVirtual



# Generated at 2022-06-13 04:28:40.002569
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    module = FakeAnsibleModule()
    virtual = SunOSVirtual(module)

    assert virtual.platform == 'SunOS'

# Test get_virtual_facts on a linux system with LXC container

# Generated at 2022-06-13 04:28:48.290232
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # If a file exists at this path, the container is a zone
    with mock.patch('os.path.isdir', return_value=False):
        # If a command exists at this bin path, the global zone is a container
        with mock.patch('os.path.exists', side_effect=[True]):
            # If a command exists at this bin path, the global zone is virtualized
            with mock.patch('os.path.exists', side_effect=[True]):
                # If a command returns a specific exit code, the global zone is virtualized with a specific type
                with mock.patch('ansible.module_utils.facts.virtual.sunos.SunOSVirtual.module.run_command', return_value=(0, 'VMware', '')):
                    sunos_virtual = SunOSVirtual(dict(module=MagicMock()))