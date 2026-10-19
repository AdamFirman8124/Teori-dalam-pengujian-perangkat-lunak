

# Generated at 2022-06-13 04:20:39.900077
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    from ansible.module_utils.facts import VirtualCollector
    a = VirtualCollector()
    b = SunOSVirtualCollector()
    assert(isinstance(b, VirtualCollector))
    assert(a._platform == b._platform)
    assert(a._fact_class == b._fact_class)

# Generated at 2022-06-13 04:20:43.173023
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    if os.name == 'posix':
        collector = VirtualCollector.factory()
        assert isinstance(collector, SunOSVirtualCollector)
        assert collector.platform == 'SunOS'
        assert collector._fact_class == SunOSVirtual

# Generated at 2022-06-13 04:20:44.138339
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    assert SunOSVirtualCollector._platform == 'SunOS'

# Generated at 2022-06-13 04:20:46.922769
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    """
    Create an instance of SunOSVirtualCollector
    """
    collector = SunOSVirtualCollector()
    assert collector
    assert isinstance(collector._fact_class, SunOSVirtual)

# Generated at 2022-06-13 04:20:48.603582
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    module = AnsibleModuleMock()
    SunOSVirtualCollector(module)

# Generated at 2022-06-13 04:20:51.689047
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = AnsibleModuleMock(params={})
    module.run_command = lambda args: (0, None, None)

    sunOSVirtual = SunOSVirtual(module)
    assert sunOSVirtual.get_virtual_facts() == {}

# Generated at 2022-06-13 04:20:52.673508
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    sv = SunOSVirtual({})
    assert sv.platform == 'SunOS'

# Generated at 2022-06-13 04:20:59.231880
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = FakeAnsibleModule()
    module.run_command = MockAnsibleModuleRunCommand()

    v = SunOSVirtual(module)
    assert v.get_virtual_facts() == {'virtualization_tech_guest': set(),
                                     'virtualization_tech_host': set()}

    module.run_command.set_command('zonename', returncode=0, out='global')
    assert v.get_virtual_facts() == {'virtualization_tech_guest': set(),
                                     'virtualization_tech_host': set([u'zone'])}

    module.run_command.set_command('zonename', returncode=0, out='non-global')

# Generated at 2022-06-13 04:21:10.760210
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.sunos import SunOSVirtual
    #
    # Test zone
    #
    # Test zone global
    test_module = AnsibleModuleMock()
    test_module.run_command = run_command_mock(
        rc=0,
        out='global',
    )
    test_SunOSVirtual = SunOSVirtual(module=test_module)
    facts = test_SunOSVirtual.get_virtual_facts()
    assert 'virtualization_tech_guest' in facts
    assert 'virtualization_tech_host' in facts
    assert facts['virtualization_tech_guest'] == set()
    assert facts['virtualization_tech_host'] == set('zone')
    # Test zone local
    test_module = AnsibleModuleMock()
    test_module.run

# Generated at 2022-06-13 04:21:12.073397
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    SunOSVirtualCollector()

# Generated at 2022-06-13 04:21:30.222410
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    facts = SunOSVirtual({})
    assert 'zone' in facts.guest_tech
    assert 'vmware' in facts.guest_tech
    assert 'virtualbox' in facts.guest_tech
    assert 'virtuozzo' in facts.guest_tech
    assert 'ldom' in facts.guest_tech
    assert 'vmware' in facts.guest_tech
    assert 'parallels' in facts.guest_tech
    assert 'xen' in facts.guest_tech
    assert 'kvm' in facts.guest_tech

# Generated at 2022-06-13 04:21:38.159581
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    import os, sys
    import unittest
    import mock
    sys.path.append('/usr/share/ansible')
    from ansible.module_utils import facts
    from ansible.module_utils.facts.virtual.sunos import SunOSVirtual

    class AnsibleModuleMock(object):
        def __init__(self):
            self.run_command = mock.MagicMock(return_value=(0, '', ''))
            self.get_bin_path = mock.MagicMock(return_value=None)
            self.fail_json = mock.MagicMock()

    class SunOSVirtualTest(unittest.TestCase):
        def setUp(self):
            self.module = AnsibleModuleMock()
            self.virtual = SunOSVirtual(self.module)


# Generated at 2022-06-13 04:21:39.736843
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual = SunOSVirtual(dict())
    assert 'SunOS' == virtual.platform

# Generated at 2022-06-13 04:21:51.368261
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = FakeAnsibleModule()

    class FakeSunOSVirtual(SunOSVirtual):
        def __init__(self, module):
            super(FakeSunOSVirtual, self).__init__(module)
            self.results = {
                "virtualization_type": "",
                "virtualization_role": "",
                "virtualization_tech_host": set(),
                "virtualization_tech_guest": set(),
                "container": "",
            }

        def _run_command(self, command):
            return (0, "", "")

        def _get_file_content(self, path):
            return ""

    def _get_file_content(path):
        return ""

    def _run_command(command):
        return (0, "", "")


# Generated at 2022-06-13 04:21:57.109609
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    '''Test case for get_virtual_facts of class SunOSVirtual'''
    module = AnsibleModuleMock()
    module.run_command = run_command_mock
    sunos_virtual = SunOSVirtual(module)

    # mocking module
    module.get_bin_path = lambda x: '/usr/sbin/zonename'
    module.run_command.return_value = (0, 'global', None)
    virtual_facts = sunos_virtual.get_virtual_facts()

    assert virtual_facts['virtualization_tech_host'] == set(['zone'])
    assert virtual_facts['virtualization_role'] == 'host'
    assert not 'virtualization_tech_guest' in virtual_facts

    # mocking module

# Generated at 2022-06-13 04:22:00.532457
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual_facts = SunOSVirtual({'module':None}, None, None)
    assert virtual_facts.platform == 'SunOS'
    assert virtual_facts.get_virtual_facts() == None
    assert SunOSVirtual.platform == 'SunOS'


# Generated at 2022-06-13 04:22:02.928104
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    vc = SunOSVirtualCollector()
    assert vc._platform == 'SunOS'
    assert vc._fact_class == SunOSVirtual

# Generated at 2022-06-13 04:22:13.467238
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # IMPORTANT:
    # test on SunOS requires a running zone 'zonetest'
    # test on SunOS requires a running branded zone 'zonetest8'
    # test on Solaris 11 requires a running zone with vmware-tools installed
    module = type('', (), {'run_command': run_command, 'get_bin_path': get_bin_path})
    virtual_facts = SunOSVirtual(module).get_virtual_facts()
    assert 'virtualization_role' in virtual_facts
    assert virtual_facts['virtualization_role'] == 'guest'
    assert 'virtualization_type' in virtual_facts
    assert virtual_facts['virtualization_type'] == 'zone'
    assert 'container' in virtual_facts
    assert virtual_facts['container'] == 'zone'

# Generated at 2022-06-13 04:22:17.873403
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    assert SunOSVirtual.platform == 'SunOS'
    assert SunOSVirtual.get_virtual_facts().get('virtualization_type', '') in ('', 'xen', 'parallels', 'vmware', 'virtualbox', 'kvm', 'virtuozzo')

# Generated at 2022-06-13 04:22:27.355111
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # Unit test setup
    class TestModule(object):
        def __init__(self, platform, run_command_return_value):
            self.platform = platform
            self.run_command_return_value = run_command_return_value

        def get_bin_path(self, executable):
            return '/bin/' + executable

        def run_command(self, command):
            if command == '/bin/zonename':
                return self.run_command_return_value[0]
            elif command == '/bin/modinfo':
                return self.run_command_return_value[1]

    # Unit test for get_virtual_facts: Solaris 10 global zone KVM guest
    test_module = TestModule('SunOS', ((0, 'global', ''), (0, 'vboxdrv: VirtualBox Support', '')))

# Generated at 2022-06-13 04:22:58.474214
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    # In this section, we test Virtual class by checking the output
    # of get_facts. If a change to the class breaks any of these tests,
    # then the change is incorrect.
    virtual_facts = SunOSVirtual({}, {})
    virtual_facts_output = virtual_facts.get_virtual_facts()
    assert 'virtualization_tech_host' in virtual_facts_output
    assert 'virtualization_tech_guest' in virtual_facts_output
    assert 'virtualization_role' in virtual_facts_output
    assert 'virtualization_type' in virtual_facts_output

# Generated at 2022-06-13 04:22:59.741277
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    facts = SunOSVirtual({})
    assert isinstance(facts, dict)

# Generated at 2022-06-13 04:23:06.400574
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # check facts in a container
    collector = SunOSVirtualCollector()
    facts = collector.get_virtual_facts(SunOSVirtual({'container': 'zone'}))
    assert 'zone' in facts['virtualization_tech_guest']
    assert 'container' in facts
    assert facts['container'] == 'zone'
    assert 'virtualization_type' in facts
    assert facts['virtualization_type'] == 'zone'
    assert 'virtualization_role' in facts
    assert facts['virtualization_role'] == 'guest'

    # Check facts on a host
    collector = SunOSVirtualCollector()
    facts = collector.get_virtual_facts(SunOSVirtual({'container': 'none'}))
    assert 'zone' in facts['virtualization_tech_host']
    assert 'container' not in facts

# Generated at 2022-06-13 04:23:08.783327
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    svt=SunOSVirtual({})
    facts = svt.get_virtual_facts()



# Generated at 2022-06-13 04:23:11.238693
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    collector = SunOSVirtualCollector()
    assert collector.get_fact_class() == SunOSVirtual
    assert collector.get_platform() == 'SunOS'

# Generated at 2022-06-13 04:23:19.190802
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = VirtualCollector(dict(ANSIBLE_MODULE_ARGS='', ansible_facts={}))
    facts = dict()
    # virtualization_type
    facts['virtualization_type'] = 'vmware'
    # virtualization_role
    facts['virtualization_role'] = 'guest'
    # virtualization_tech_host (set)
    facts['virtualization_tech_host'] = set(['zone'])
    # virtualization_tech_guest (set)
    facts['virtualization_tech_guest'] = set(['zone', 'vmware'])
    # container
    facts['container'] = 'zone'

    test = SunOSVirtual(module)
    assert facts == test.get_virtual_facts()

# Generated at 2022-06-13 04:23:26.758261
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    module = type('module', (object,), {'run_command': lambda *args, **kwargs: (0, "", "")})()
    virtual_facts = SunOSVirtual(module=module)
    assert 'virtualization_type' in virtual_facts.get_facts()
    assert 'virtualization_role' in virtual_facts.get_facts()
    assert 'virtualization_tech_host' in virtual_facts.get_facts()
    assert 'virtualization_tech_guest' in virtual_facts.get_facts()


# Generated at 2022-06-13 04:23:29.601635
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    virtual_collector = SunOSVirtualCollector()
    assert virtual_collector.platform == 'SunOS'
    assert virtual_collector.fact_class == SunOSVirtual


# Generated at 2022-06-13 04:23:32.161160
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    collector = SunOSVirtualCollector()
    assert collector.__class__.__name__ == 'SunOSVirtualCollector'

# Generated at 2022-06-13 04:23:33.141613
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    SunOSVirtualCollector()

# Generated at 2022-06-13 04:24:34.583078
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    '''Unit test for constructor of class SunOSVirtual'''
    from ansible_collections.community.general.tests.unit.compat.mock import Mock
    from ansible_collections.community.general.tests.unit.modules.utils import AnsibleFailJson, AnsibleExitJson

    results = {
        'virtualization_type': 'virtuozzo',
        'container': 'zone',
        'virtualization_role': 'guest',
        'virtualization_tech_guest': ['virtuozzo', 'zone'],
        'virtualization_tech_host': ['zone'],
    }

    module = Mock()
    setattr(module, '_ansible_module_installed', False)
    setattr(module, 'exit_json', AnsibleExitJson())

# Generated at 2022-06-13 04:24:37.417473
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    facts = {}
    SunOSVirtualCollector(facts, None)
    assert facts['virtualization_type'] == 'container'


# Generated at 2022-06-13 04:24:39.534934
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    svc = SunOSVirtualCollector()


# Generated at 2022-06-13 04:24:44.629373
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    virtual_collector = SunOSVirtualCollector()
    assert isinstance(virtual_collector, SunOSVirtualCollector)
    assert not hasattr(virtual_collector, '_platform')
    assert virtual_collector._fact_class == SunOSVirtual
    assert virtual_collector._platform == 'SunOS'

# Generated at 2022-06-13 04:24:54.313494
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    """Generates dict that is passed to the SunOSVirtual instance
    and compares the output of get_virtual_facts() w/ expected"""
    # generate input args to Instance
    args = {}
    args['paths'] = {'module_utils': 'ansible/module_utils'}
    args['module'] = MagicMock()

    # create instance of SunOSVirtual w/ args
    inst = SunOSVirtual(args)

    # create expected results for each test
    # each result will be a dict that maps dict key to dict value

    # global zone, no guest tools
    args['module'].run_command.return_value = (0, 'global', '')
    args['paths']['zonename'] = '/bin/zonename'

# Generated at 2022-06-13 04:24:56.153354
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    testobj = SunOSVirtual({})

    assert testobj.platform == 'SunOS'

# Generated at 2022-06-13 04:24:59.238632
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    # Create instance of SunOSVirtual
    sunos_virtual = SunOSVirtual({})
    # Assert that instance is created successfully and platform is set to SunOS
    assert sunos_virtual is not None
    assert sunos_virtual.platform == 'SunOS'

# Generated at 2022-06-13 04:25:02.324889
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virt = SunOSVirtual()
    assert virt
    assert 'container' in virt.facts
    assert 'virtualization_type' in virt.facts
    assert 'virtualization_role' in virt.facts
    assert 'virtualization_tech_guest' in virt.facts
    assert 'virtualization_tech_host' in virt.facts

# Generated at 2022-06-13 04:25:04.303742
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual_facts = SunOSVirtual(dict())
    assert virtual_facts.platform == 'SunOS'


# Generated at 2022-06-13 04:25:07.606490
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    module = AnsibleModuleMock()
    fact_class = SunOSVirtual(module)
    assert fact_class.platform == 'SunOS'
    assert fact_class.module == module


# Generated at 2022-06-13 04:26:56.984516
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    """
    Constructor test of class SunOSVirtual
      - without argument -> instance with attribute module unset
      - with invalid argument -> exception
      - with argument -> instance with attribute module set
    """
    # constructor without argument -> exception
    with pytest.raises(Exception) as e_info:
        test_instance = SunOSVirtual()
    assert "argument 'module' (position 1) must be specified" in str(e_info.value)
    # constructor with invalid argument
    test_instance = SunOSVirtual(module='foo')
    assert test_instance.module == 'foo'

# Generated at 2022-06-13 04:27:03.108021
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    # Create a SunOSVirtualCollector object
    sunos_virtual_collector = SunOSVirtualCollector()

    # Check result of get_platform function
    assert sunos_virtual_collector.get_platform() == 'SunOS'

    # Check result of get_fact_class function
    assert sunos_virtual_collector.get_fact_class() == SunOSVirtual

# Generated at 2022-06-13 04:27:08.826026
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    """
    Retrieve facts
    """
    # pylint: disable=protected-access
    virtual_facts = SunOSVirtual().get_virtual_facts()
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts

# Generated at 2022-06-13 04:27:10.058410
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    assert SunOSVirtualCollector._platform == 'SunOS'



# Generated at 2022-06-13 04:27:19.436469
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # Create the object
    obj = SunOSVirtual({})

    # Mock the module
    class GlobalModule:
        def __init__(self):
            self.params = {}

        def run_command(self, cmd):
            if 'zonename' in cmd:
                return (0, 'global', 'stdout')
            elif 'modinfo' in cmd:
                return (0, '', '')
            elif 'virtinfo' in cmd:
                return (0, '', '')
            elif 'smbios' in cmd:
                return (0, '', '')

        def get_bin_path(self, command):
            if command in ['zonename', 'modinfo', 'virtinfo', 'smbios']:
                return command

    obj.module = GlobalModule()

    # Test global zone

# Generated at 2022-06-13 04:27:20.767316
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual = SunOSVirtual(dict(module=None))
    assert virtual.platform == 'SunOS'

# Generated at 2022-06-13 04:27:22.325332
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    assert SunOSVirtualCollector.platform == 'SunOS'
    assert SunOSVirtualCollector._platform == 'SunOS'

# Generated at 2022-06-13 04:27:29.568268
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    host_tech = set()
    guest_tech = set()
    virtual_facts = {}
    virtual_facts['virtualization_tech_guest'] = guest_tech
    virtual_facts['virtualization_tech_host'] = host_tech
    result = SunOSVirtual(virtual_facts).get_virtual_facts()

    assert 'virtualization_type' in result
    assert 'virtualization_role' in result
    assert 'virtualization_tech_guest' in result
    assert 'virtualization_tech_host' in result

# Generated at 2022-06-13 04:27:30.863081
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual = SunOSVirtual(dict())
    assert virtual.platform == 'SunOS'

# Generated at 2022-06-13 04:27:34.582038
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    vc = SunOSVirtualCollector()
    vc.module.run_command = fake_run_command
    facts_list = vc.collect()
    virtual_facts = facts_list[0].get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'xen'
    assert virtual_facts['virtualization_role'] == 'guest'
