

# Generated at 2022-06-13 04:20:40.607792
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    try:
        SunOSVirtualCollector()
        assert False
    except:
        assert True

# Generated at 2022-06-13 04:20:48.202937
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    fake_module = object()
    fake_module.run_command = lambda x: (0, "", "")
    fake_module.get_bin_path = lambda x: x

    facts = SunOSVirtual(fake_module).get_virtual_facts()
    assert 'zone' in facts['virtualization_tech_host']
    assert 'zone' not in facts['virtualization_tech_guest']
    assert 'container' not in facts

    fake_module.run_command = lambda x: (0, "global\n", "")
    fake_module.get_bin_path = lambda x: x

    facts = SunOSVirtual(fake_module).get_virtual_facts()
    assert 'zone' in facts['virtualization_tech_host']
    assert 'zone' not in facts['virtualization_tech_guest']

# Generated at 2022-06-13 04:20:50.336706
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    collector = SunOSVirtualCollector()
    assert collector._platform == 'SunOS'
    assert collector._fact_class == SunOSVirtual

# Generated at 2022-06-13 04:20:51.292151
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    x = SunOSVirtualCollector()
    assert x
    assert x._platform == 'SunOS'

# Generated at 2022-06-13 04:20:56.142102
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # Creating SunOSVirtual class for testing purposes
    class SunOSVirtualMock(SunOSVirtual):
        def __init__(self, params):
            self.module = params

    # Define data for testing purposes
    class Object(object):
        def __init__(self, params):
            self.params = params

        def get_bin_path(self, binary):
            return binary

        def run_command(self, cmd):
            if cmd == 'zonename':
                return (0, 'global', '')
            elif cmd == 'modinfo':
                return (0, '', '')
            elif cmd == 'virtinfo -p':
                return (0, 'DOMAINROLE|impl=LDoms|control=false|io=false|service=false|root=false', '')

# Generated at 2022-06-13 04:20:58.131748
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    assert isinstance(SunOSVirtualCollector(), VirtualCollector)

# Generated at 2022-06-13 04:21:00.337663
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    x = SunOSVirtualCollector()
    assert x is not None

# Generated at 2022-06-13 04:21:04.294933
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    obj = SunOSVirtual(module=None)
    # obj is instance of Virtual
    assert isinstance(obj, Virtual)
    # obj is instance of SunOSVirtual
    assert isinstance(obj, SunOSVirtual)

# Generated at 2022-06-13 04:21:05.854945
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    """ Test instantiation of class SunOSVirtualCollector """
    assert SunOSVirtualCollector(None, None)

# Generated at 2022-06-13 04:21:08.217442
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual = SunOSVirtual({})
    assert isinstance(virtual, SunOSVirtual)
    assert virtual.platform == 'SunOS'


# Generated at 2022-06-13 04:21:24.555050
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    '''
    Unit test for constructor of class SunOSVirtual
    '''
    sunos_virtual_object = SunOSVirtual({})
    assert sunos_virtual_object.platform == 'SunOS'

# Generated at 2022-06-13 04:21:26.416793
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    """
    SunOSVirtualCollector can be instantiated
    """

    SunOSVirtualCollector()


# Generated at 2022-06-13 04:21:30.282896
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual_facts = SunOSVirtual({}).populate()
    assert virtual_facts['virtualization_type'] is None
    assert virtual_facts['virtualization_role'] is None
    assert virtual_facts['container'] is None
    assert virtual_facts['virtualization_tech_guest'] == set([])
    assert virtual_facts['virtualization_tech_host'] == set([])

# Generated at 2022-06-13 04:21:38.219843
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    # Create instance of class SunOSVirtualCollector
    sunos_virtual_collector = SunOSVirtualCollector()
    # Assert that the class SunOSVirtualCollector has been created and is of the right type
    assert sunos_virtual_collector is not None
    assert type(sunos_virtual_collector) == SunOSVirtualCollector
    # Assert that the class SunOSVirtualCollector has the right attribute _fact_class
    assert sunos_virtual_collector._fact_class is not None
    assert type(sunos_virtual_collector._fact_class) == type
    assert sunos_virtual_collector._fact_class.__name__ == 'SunOSVirtual'
    # Assert that the class SunOSVirtualCollector has the right attribute _platform
    assert sunos_virtual_collector._platform is not None

# Generated at 2022-06-13 04:21:39.316139
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual = SunOSVirtual(dict())
    assert virtual.platform == 'SunOS'


# Generated at 2022-06-13 04:21:39.936163
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    SunOSVirtual()

# Generated at 2022-06-13 04:21:51.495945
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = FakeAnsibleModule()
    virtual_facts = SunOSVirtual.get_virtual_facts(module)

    assert('virtualization_type' in virtual_facts)
    assert(virtual_facts['virtualization_type'] is None)
    assert('virtualization_role' in virtual_facts)
    assert(virtual_facts['virtualization_role'] is None)
    assert('container' in virtual_facts)
    assert(virtual_facts['container'] is None)

    module.run_command = run_command_globalzone
    virtual_facts = SunOSVirtual.get_virtual_facts(module)

    assert(virtual_facts['virtualization_type'] is None)
    assert(virtual_facts['virtualization_role'] is None)
    assert(virtual_facts['container'] is None)

    module.run_command = run_command

# Generated at 2022-06-13 04:21:57.165632
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = FakeModule()
    module.run_command = run_command
    module.get_bin_path = FakeGetBinPath()

    os_facts = {
        'os_family': 'Solaris',
        'distribution': 'SunOS',
        'distribution_version': '5.11',
    }

    for hypervisor in hypervisors.keys():
        for guest in hypervisors[hypervisor]['virtual_facts']:
            for guest_type in guest:
                # Test a guest
                os_facts['virtualization_type'] = hypervisor
                os_facts['virtualization_role'] = 'guest'
                os_facts['container'] = guest_type
                os_facts['virtualization_tech']['guest'] = set(guest[guest_type])

# Generated at 2022-06-13 04:21:58.223792
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    obj = SunOSVirtualCollector()
    assert obj.platform == 'SunOS'
    assert obj.fact_class.platform == 'SunOS'

# Generated at 2022-06-13 04:21:58.838641
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    x = SunOSVirtualCollector()

# Generated at 2022-06-13 04:22:30.508688
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():

    module = DummyAnsibleModule()
    module.run_command = Mock(return_value=(0, "global", ""))
    module.get_bin_path = Mock(side_effect=['/usr/bin/zonename', '/usr/sbin/modinfo'])
    mock_open = mock_open()
    with patch("ansible.module_utils.facts.virtual.sunos.open", mock_open, create=True):
        virtual_facts = SunOSVirtual().get_virtual_facts()
        assert virtual_facts['virtualization_tech_guest'] == set(['zone'])
        assert virtual_facts['virtualization_tech_host'] == set(['zone'])
        assert not virtual_facts.get('virtualization_type', None)
        assert not virtual_facts.get('virtualization_role', None)


# Generated at 2022-06-13 04:22:41.532100
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = AnsibleModule(argument_spec={})
    module.run_command = MagicMock(return_value=(0, '', ''))

    # Unit test 1: When we have a global zone
    module.run_command.return_value = (0, 'global', '')
    platform_virtual = SunOSVirtual(module)
    virtual_facts = platform_virtual.get_virtual_facts()
    assert virtual_facts['virtualization_tech_host'] == set(['zone'])
    assert virtual_facts['virtualization_tech_guest'] == set()

    # Unit test 2: When we have a non global zone
    module.run_command.return_value = (0, 'testzone', '')
    virtual_facts = platform_virtual.get_virtual_facts()
    assert virtual_facts['virtualization_tech_host']

# Generated at 2022-06-13 04:22:47.295890
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    sunosvirtual = SunOSVirtual()
    assert 'zone' in sunosvirtual.virtualization_tech_guest
    if 'zone' in sunosvirtual.virtualization_tech_guest:
        assert sunosvirtual.virtualization_type == 'zone'
        assert sunosvirtual.virtualization_role == 'guest'
        assert sunosvirtual.container == 'zone'

# Generated at 2022-06-13 04:22:51.808868
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    assert SunOSVirtualCollector._platform == 'SunOS'
    assert SunOSVirtualCollector._fact_class == SunOSVirtual
    assert issubclass(SunOSVirtualCollector._fact_class, Virtual)


# Generated at 2022-06-13 04:22:56.600187
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    module = FakeAnsibleModule()
    module.run_command = MagicMock(return_value=(0, 'zonename: global\n', ''))
    sunos = SunOSVirtual(module)
    assert sunos.platform == 'SunOS'
    assert sunos.get_virtual_facts() == {}


# Generated at 2022-06-13 04:22:59.035725
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    virtual_collector = SunOSVirtualCollector()

    assert virtual_collector.platform == 'SunOS'
    assert virtual_collector.fact_class == SunOSVirtual

# Generated at 2022-06-13 04:23:00.592386
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    x = SunOSVirtual()
    assert x.platform == 'SunOS'



# Generated at 2022-06-13 04:23:04.373178
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    virtual_collector = SunOSVirtualCollector({})
    assert virtual_collector._fact_class == SunOSVirtual
    assert virtual_collector._platform == 'SunOS'


# Generated at 2022-06-13 04:23:08.639155
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    # The following is call by ansible
    # ansible localhost -m setup -a "filter=ansible_virtual"
    # We need to check that the module detected by Ansible is the expected one
    from ansible.module_utils.facts import ansible_virtual
    facts_module = ansible_virtual
    assert facts_module.SunOSVirtualCollector._platform == 'SunOS'

# Generated at 2022-06-13 04:23:10.104371
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual = SunOSVirtual({})
    virtual.get_all_facts()

# Generated at 2022-06-13 04:24:05.370992
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    module_args = dict()
    module_args.update(dict(
        gather_subset = [],
        filter = '*'
    ))
    module = MockModule(**module_args)
    SunOSVirtual(module=module)

# Generated at 2022-06-13 04:24:08.232101
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    module = AnsibleModuleMock()
    virt = SunOSVirtual(module)

    assert not virt.virtualization
    assert virt.virtualization_type is None
    assert virt.virtualization_role is None
    assert virt.container is None



# Generated at 2022-06-13 04:24:12.201050
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    virt_fact_collector = SunOSVirtualCollector()
    assert virt_fact_collector._platform == 'SunOS'
    assert virt_fact_collector._fact_class == SunOSVirtual

# Generated at 2022-06-13 04:24:15.264595
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    class Options:
        def __init__(self):
            self.disable_kernel_facts = False
    import sys
    import inspect
    options = Options()
    virtual_collector = SunOSVirtualCollector(sys.modules[__name__], options)
    assert virtual_collector.__class__ == SunOSVirtualCollector
    assert virtual_collector.module.__name__ == __name__
    assert virtual_collector.options == options



# Generated at 2022-06-13 04:24:16.521647
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    v = SunOSVirtual()
    val = v.get_virtual_facts()
    assert isinstance(val, dict)

# Generated at 2022-06-13 04:24:20.183108
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    module = ansible_mock_module('/bin/true', '/bin/true')
    fact = SunOSVirtual(module, 'test_SunOSVirtual')
    assert isinstance(fact, SunOSVirtual)
    assert fact.platform == 'SunOS'
    module.exit_json(ansible_facts={})


# Generated at 2022-06-13 04:24:21.085993
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    SunOSVirtualCollector()

# Generated at 2022-06-13 04:24:22.140670
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual = SunOSVirtual({})
    assert virtual.platform == "SunOS"

# Generated at 2022-06-13 04:24:23.133732
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    SunOSVirtualCollector()

# Generated at 2022-06-13 04:24:35.978770
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    from ansible.module_utils import basic
    module = basic.AnsibleModule(
        argument_spec=dict()
    )
    module.run_command = lambda x: (0, '', '')
    module.get_bin_path = lambda x: '/usr/sbin/zonename'

    # Case: zonename is available (kernelzone and native zone)
    sunos = SunOSVirtual(module)
    virtual_facts = sunos.get_virtual_facts()
    assert virtual_facts == {
        'virtualization_tech_host': set(),
        'virtualization_tech_guest': set(),
        'virtualization_role': 'host',
        'virtualization_type': None,
        'container': 'zone'
    }

    # Case: branded zone

# Generated at 2022-06-13 04:26:25.945710
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():

    module_mock = Mock()
    module_mock.run_command.return_value = (0, "global", "")
    module_mock.get_bin_path.return_value = '/bin/zonename'

    virt = SunOSVirtual(module_mock, {})
    facts = virt.get_virtual_facts()

    assert facts['virtualization_type'] == 'zone'
    assert facts['virtualization_role'] == 'host'

# Generated at 2022-06-13 04:26:36.386660
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils.facts.virtual.sunos import SunOSVirtual

    # FIXME: use the mock library instead
    real_run_command = SunOSVirtual.run_command

    class MockOS:
        pass

    class MockModule:
        def __init__(self, params):
            self.os = MockOS()
            self.params = params

        def get_bin_path(self, name, required=False):
            if name == 'zonename':
                return '/bin/zonename'
            if name == 'modinfo':
                return '/sbin/modinfo'
            if name == 'virtinfo':
                return '/usr/sbin/virtinfo'

# Generated at 2022-06-13 04:26:44.598375
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = FakeModule()
    modinfo = FakeCommand('/usr/bin/modinfo', '', 0)
    zonename = FakeCommand('/usr/sbin/zonename', 'global\n', 0)
    virtinfo = FakeCommand('/usr/sbin/virtinfo', '', 0)
    smbios = FakeCommand('/usr/sbin/smbios', '', 0)

    module.run_command = FakeRunCommand([
        modinfo,
        zonename,
        virtinfo,
        smbios
    ])

    module.get_bin_path = FakeGetBinPath(True)

    SunOSVirtual(module).get_virtual_facts()



# Generated at 2022-06-13 04:26:49.403662
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual_facts = {}
    virtual = SunOSVirtual(None)
    virtual_facts = virtual.get_virtual_facts()

    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts

# Generated at 2022-06-13 04:26:58.406264
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    """Test SunOSVirtualCollector() constructor"""

    sunos_sys_class_virt_facts = {
        'virtualization_tech_guest': set(['vmware', 'zone']),
        'virtualization_tech_host': set(['zone']),
        'virtualization_role': 'guest',
        'virtualization_type': 'vmware',
        'container': 'zone'
    }

# Generated at 2022-06-13 04:26:59.490814
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    SunOSVirtualCollector()

# Generated at 2022-06-13 04:27:03.198596
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    '''Unit test for constructor of class SunOSVirtualCollector'''
    svc = SunOSVirtualCollector()
    assert svc.platform == 'SunOS'
    assert svc.fact_class == SunOSVirtual

# Generated at 2022-06-13 04:27:06.784899
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual = SunOSVirtual(dict(module=dict()))
    assert virtual.get_virtual_facts() == {'virtualization_tech_host': set(), 'virtualization_tech_guest': set()}


# Generated at 2022-06-13 04:27:07.983609
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    obj = SunOSVirtualCollector()
    assert obj.platform == 'SunOS'

# Generated at 2022-06-13 04:27:09.325072
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    sunos = SunOSVirtualCollector()
    assert sunos.platform == 'SunOS'