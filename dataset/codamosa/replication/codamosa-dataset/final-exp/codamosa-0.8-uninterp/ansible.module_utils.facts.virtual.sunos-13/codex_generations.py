

# Generated at 2022-06-13 04:20:50.512869
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # dict to simulate the host running on a bare metal Sparc machine
    facts_sparc = {
        'ansible_facts': {
            'architecture': 'sparc',
            'kernel': 'SunOS',
        }
    }
    # dict to simulate the host running inside a Solaris 8 or 9 branded zone
    facts_branded_zone = {
        'ansible_facts': {
            'architecture': 'sparc',
            'kernel': 'SunOS',
            'virtualization_role': 'guest',
            'virtualization_type': 'zone',
        }
    }
    # dict to simulate the host running inside a Solaris 10 non-global zone

# Generated at 2022-06-13 04:20:51.519808
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virt_facts = SunOSVirtual({'module': None})
    assert virt_facts is not None

# Generated at 2022-06-13 04:20:58.275923
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():

    from ansible.module_utils.facts.virtual.sunos import SunOSVirtual
    sunosvirtual = SunOSVirtual()

    # zone (global)
    sunosvirtual.module.run_command = lambda x: (0, 'global', '')
    sunosvirtual.module.get_bin_path = lambda x: '/bin/zonename'
    sunosvirtual.module.get_file_content = lambda x: ''
    assert sunosvirtual.get_virtual_facts() == {'container': 'zone',
                                                'virtualization_tech_guest': set([]),
                                                'virtualization_tech_host': set(['zone'])}

    # zone (nonglobal)
    sunosvirtual.module.run_command = lambda x: (0, 'roger', '')

# Generated at 2022-06-13 04:21:10.568855
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    mock_module = MockModule()

# Generated at 2022-06-13 04:21:14.787332
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virt = SunOSVirtual({}, {})
    assert virt.platform == 'SunOS'
    assert virt.guest_tech is None
    assert virt.host_tech is None
    assert virt.known_facts == set()
    assert virt.get_virtual_facts() == {}
    assert virt.get_facts() == {}

# Generated at 2022-06-13 04:21:19.942267
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    sv = SunOSVirtual({})
    assert sv.virtual_facts['virtualization_tech_guest'] == set()
    assert sv.virtual_facts['virtualization_tech_host'] == set()
    assert sv.virtual_facts['virtualization_type'] is None
    assert sv.virtual_facts['virtualization_role'] is None
    assert sv.virtual_facts['container'] is None

# Generated at 2022-06-13 04:21:22.280525
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    c = SunOSVirtualCollector()
    assert c.platform == 'SunOS'
    assert type(c.facts) != type(None)

# Generated at 2022-06-13 04:21:31.093266
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = FakeModule()
    output = {'failed': False}
    sunos = SunOSVirtual(module)

    # Test that it returns an empty dictionary when no virtualization command found
    module.run_command = lambda *cmd, **kwargs : (3, '', '')
    assert {} == sunos.get_virtual_facts()

    # Test that it returns correct facts with zonename "global"
    module.run_command = lambda *cmd, **kwargs : (0, 'global\n', '')
    assert {'virtualization_role': 'host', 'virtualization_type': 'zone',
                'virtualization_tech_guest': set(), 'virtualization_tech_host': set(['zone']),
                'container': None} == sunos.get_virtual_facts()

    # Test that it returns correct facts with z

# Generated at 2022-06-13 04:21:34.504606
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    """
    We check that the constructor of SunOSVirtual is working.
    """
    # Create a class Virtual object
    sunos_virtual_obj = SunOSVirtual()
    assert sunos_virtual_obj.platform == 'SunOS'
    assert sunos_virtual_obj.virtualization_role == 'guest'

# Generated at 2022-06-13 04:21:35.672274
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    assert isinstance(SunOSVirtualCollector(), SunOSVirtualCollector)

# Generated at 2022-06-13 04:22:06.860809
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    platform_virtual_collector = SunOSVirtualCollector()
    assert platform_virtual_collector.platform == 'SunOS'
    assert platform_virtual_collector._fact_class == SunOSVirtual

# Generated at 2022-06-13 04:22:08.667386
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual_facts = SunOSVirtual(dict())
    assert virtual_facts.platform == 'SunOS'

# Generated at 2022-06-13 04:22:16.936523
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual import SunOSVirtual
    from ansible.module_utils.facts.virtual.base import Virtual, VirtualCollector
    from ansible.module_utils.facts.virtual.base import Context

    context = Context()
    v = SunOSVirtual(context=context)

    # Test function get_virtual_facts
    # Input data
    # Test that the method returns the correct dictionary
    assert(v.get_virtual_facts() == {'virtualization_tech_guest': set(),
                                     'virtualization_tech_host': set()})



# Generated at 2022-06-13 04:22:21.435199
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    results = SunOSVirtual()
    assert results.platform == 'SunOS'
    assert results.virtualization_type is None
    assert results.virtualization_role is None
    assert results.virtualization_tech_host is None
    assert results.virtualization_tech_guest is None
    assert results.container is None

# Generated at 2022-06-13 04:22:29.505488
# Unit test for method get_virtual_facts of class SunOSVirtual

# Generated at 2022-06-13 04:22:32.995066
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    """
    temp test function
    @return:
    """
    # obj = SunOSVirtualCollector()
    # obj.collect()
    # for item in obj.data:
    #     print(item)

    pass

# Generated at 2022-06-13 04:22:35.159939
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    # Instantiate
    module = AnsibleModuleMock({})
    v = SunOSVirtual(module)
    assert v

# Generated at 2022-06-13 04:22:37.764785
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    from ansible.module_utils.facts.virtual import Virtual, SunOSVirtual
    assert isinstance(Virtual(), Virtual)
    assert isinstance(SunOSVirtual(), SunOSVirtual)

# Generated at 2022-06-13 04:22:41.798979
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    test_object = SunOSVirtual({})

    test_object.module.run_command = lambda x: (0, x, '')
    test_object.module.get_bin_path = lambda x: x

    # zone
    assert test_object.get_virtual_facts() == {'container': 'zone',
                                               'virtualization_type': 'zone',
                                               'virtualization_role': 'guest',
                                               'virtualization_tech_guest': set(['zone']),
                                               'virtualization_tech_host': set()}

    # zone + domaining
    test_object.module.run_command = lambda x: (0, '', '')
    test_object.module.get_bin_path = lambda x: ''

# Generated at 2022-06-13 04:22:51.288083
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    """
    Test case for method get_virtual_facts of class SunOSVirtual
    """
    import tempfile
    from ansible.module_utils.facts.virtual.SunOS import SunOSVirtual

    # Create an instance of SunOSVirtual
    sunos_virtual = SunOSVirtual()

    # Mock zonename command
    zonename = tempfile.NamedTemporaryFile('w')
    zonename.write("""#!/bin/sh
        echo "$*"
        """)
    zonename.flush()
    sunos_virtual.module.get_bin_path = lambda x: zonename.name

    # Mock modinfo command
    modinfo = tempfile.NamedTemporaryFile('w')

# Generated at 2022-06-13 04:23:20.699282
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    """Unit test class SunOSVirtualCollector
    """
    SunOSVirtualCollector()

# Generated at 2022-06-13 04:23:24.556672
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = None
    virtual_facts = {}

    # Make sure we get empty virtual_facts for a bare metal system
    virtual = SunOSVirtual(module)
    virtual_facts = virtual.get_virtual_facts()

    # For now just check that we got a dictionary back
    assert(type(virtual_facts) is dict)



# Generated at 2022-06-13 04:23:31.971246
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    # Check with facts without any values
    v = SunOSVirtual({})
    assert v.get_virtual_facts() == dict()

    # Check with facts with values
    mock_facter_facts = dict(container='zone')
    v = SunOSVirtual(mock_facter_facts)
    assert v.get_virtual_facts() == dict(container='zone')
    assert v.platform == 'SunOS'



# Generated at 2022-06-13 04:23:34.318782
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    """Tests that the correct Virtual class is created for the platform"""
    x = SunOSVirtualCollector()
    assert x._fact_class.platform == 'SunOS'

# Generated at 2022-06-13 04:23:35.246238
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    assert len(SunOSVirtual().get_virtual_facts()) > 0

# Generated at 2022-06-13 04:23:45.063709
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # Define sample output of the "zonename" command
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=False)
    module.run_command = MagicMock()
    module.get_bin_path = Mock(return_value='/usr/bin/zonename')
    module.run_command.side_effect = [
        (0, 'zone', ''),
        (0, 'zone', ''),
    ]

    # Define sample output of the "virtinfo" command

# Generated at 2022-06-13 04:23:46.719943
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    c = SunOSVirtualCollector()

    assert c._fact_class is SunOSVirtual
    assert c._platform is 'SunOS'

# Generated at 2022-06-13 04:23:53.099403
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():

    # Success scenario
    class test_module:
        def get_bin_path(self, command):
            return '/bin/' + command
        def run_command(self, command):
            return 0, 'out', 'err'
    test_module.run_command.__name__ = 'run_command'
    test_module.get_bin_path.__name__ = 'get_bin_path'

    test_virtual = SunOSVirtual(module=test_module)
    test_virtual_facts = test_virtual.get_virtual_facts()
    assert test_virtual_facts == {}

    # Host scenario
    class test_module:
        def get_bin_path(self, command):
            if command == 'smbios':
                return '/bin/smbios'
            else:
                return None

# Generated at 2022-06-13 04:23:54.709790
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
  module = AnsibleModule()
  collector = SunOSVirtual(module)
  assert collector.get_virtual_facts() == {}

# Generated at 2022-06-13 04:24:00.826389
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = FakeAnsibleModule()
    module.run_command.return_value = (1, 'foo', 'bar')

    s = SunOSVirtual(module)

    # Returncode != 0
    module.run_command.return_value = (1, '', '')
    assert 'virtualization_type' not in s.get_virtual_facts()
    assert 'virtualization_role' not in s.get_virtual_facts()
    assert 'container' not in s.get_virtual_facts()
    assert 'virtualization_tech_host' not in s.get_virtual_facts()
    assert 'virtualization_tech_guest' not in s.get_virtual_facts()

    # Returncode = 0 but no vmid
    module.run_command.return_value = (0, '', '')

# Generated at 2022-06-13 04:24:55.516657
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    SunOSVirtualCollector()

# Generated at 2022-06-13 04:24:57.760254
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    collector = SunOSVirtualCollector()
    assert collector._platform == 'SunOS'
    assert collector._fact_class is SunOSVirtual



# Generated at 2022-06-13 04:25:03.010121
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    """This testcase tests the constructor of class SunOSVirtualCollector"""
    # Apply constructor without any parameters
    sunosvirtualcollector = SunOSVirtualCollector()
    # Check the content of the created object
    assert(sunosvirtualcollector._fact_class == SunOSVirtual)
    assert(sunosvirtualcollector._platform == 'SunOS')


# Generated at 2022-06-13 04:25:14.021998
# Unit test for method get_virtual_facts of class SunOSVirtual

# Generated at 2022-06-13 04:25:14.926033
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    assert SunOSVirtual()

# Generated at 2022-06-13 04:25:15.904374
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    SunOSVirtualCollector()

# Generated at 2022-06-13 04:25:16.784773
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virt = SunOSVirtual()

# Generated at 2022-06-13 04:25:21.163513
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    virtualCollector = SunOSVirtualCollector()
    # Test platform attribute
    assert virtualCollector._platform == 'SunOS'
    # Test fact class attribute
    assert virtualCollector._fact_class == SunOSVirtual


# Generated at 2022-06-13 04:25:23.922943
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    x = SunOSVirtualCollector()
    assert x.platform == 'SunOS'
    assert x._fact_class ==  SunOSVirtual



# Generated at 2022-06-13 04:25:26.181123
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    collector = SunOSVirtualCollector()
    assert collector.fact_class == SunOSVirtual
    assert collector.platform == 'SunOS'


# Generated at 2022-06-13 04:27:26.994183
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    pass

# Generated at 2022-06-13 04:27:28.170232
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    result = SunOSVirtualCollector()
    assert result.platform == 'SunOS'

# Generated at 2022-06-13 04:27:36.045435
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = DummyModule()
    empty = DummyModule()

    # zonename is present and global
    zonename = DummyModule()
    zonename.get_bin_path.return_value = '/usr/bin/zonename'
    zonename.run_command.return_value = (0, 'global', '')
    facts = SunOSVirtual(zonename).get_virtual_facts()
    assert facts['virtualization_tech_host'] == set(['zone'])

    # zonename is present, and non-global
    zonename = DummyModule()
    zonename.get_bin_path.return_value = '/usr/bin/zonename'
    zonename.run_command.return_value = (0, 'myzone', '')
    facts = SunOSVirtual(zonename).get

# Generated at 2022-06-13 04:27:45.185372
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    class MockModule(object):
        def __init__(self, params):
            self.params = params

        def fail_json(self, *args, **kwargs):
            pass

        def get_bin_path(self, *args, **kwargs):
            if args[0] == 'smbios':
                return '/usr/sbin/smbios'
            elif args[0] == 'zonename':
                return '/usr/bin/zonename'
            else:
                return None


# Generated at 2022-06-13 04:27:55.859365
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():

    module_mock = MagicMock(name='module')
    module_mock.run_command.side_effect = [('stdout1', 'stderr1', 0), ('stdout2', 'stderr2', 0), ('stdout3', 'stderr3', 0)]
    module_mock.get_bin_path.side_effect = ['/usr/bin/zonename', '/usr/bin/modinfo', '/usr/sbin/virtinfo', '/usr/sbin/smbios']
    module_mock.fail_json.side_effect = Exception
    module_mock.check_mode = False

    sunos_virtual = SunOSVirtual(module_mock)

    # Unit test without virtinfo/smbios
    results = sunos_virtual.get_virtual_facts()

# Generated at 2022-06-13 04:27:59.803323
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual = SunOSVirtual(dict())
    assert virtual.platform == 'SunOS'
    assert virtual.virtualization_type is None
    assert virtual.virtualization_role is None
    assert virtual.virtualization_tech_guest == set()
    assert virtual.virtualization_tech_host == set()
    assert virtual.container is None

# Generated at 2022-06-13 04:28:00.863592
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    m = SunOSVirtual(dict())
    assert m.platform == 'SunOS'

# Generated at 2022-06-13 04:28:02.112900
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    collection = SunOSVirtualCollector(None, None)
    assert collection._platform == 'SunOS'

# Generated at 2022-06-13 04:28:06.453605
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    """
    This is a unit test for testing the constructor of the SunOSVirtualCollector class.
    """
    sunos_collector = SunOSVirtualCollector()
    assert sunos_collector.platform == 'SunOS'
    assert sunos_collector.fact_class == SunOSVirtual

# Generated at 2022-06-13 04:28:16.005614
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = FakeAnsibleModule()
    virtual = SunOSVirtual(module)

    # Fake the return value of module.run_command
    def run_command(cmd, check_rc=True):
        return 0, None, None
    module.run_command = run_command

    # Fake the return value of module.get_bin_path
    def get_bin_path(name, opt_dirs=[]):
        return name
    module.get_bin_path = get_bin_path

    # Fake the existence of files in /proc
    def exists(path):
        if path == '/proc/vz':
            return True
        return False
    os.path.exists = exists

    # Fake the output from virtinfo