

# Generated at 2022-06-13 04:20:39.811892
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    c = SunOSVirtualCollector()
    assert c.platform == 'SunOS'
    assert c.fact_class._platform == 'SunOS'

# Generated at 2022-06-13 04:20:47.803230
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual_facts = SunOSVirtual({})
    assert virtual_facts.platform == 'SunOS'
    assert virtual_facts.get_virtual_facts() == {}
    if os.path.exists('/proc/vz'):
        assert virtual_facts.get_virtual_facts()['virtualization_type'] == 'virtuozzo'
        assert virtual_facts.get_virtual_facts()['virtualization_role'] == 'guest'
        assert virtual_facts.get_virtual_facts()['virtualization_tech_guest'] == {'virtuozzo'}
        assert 'virtualization_tech_host' not in virtual_facts.get_virtual_facts()
    if os.path.exists('/.SUNWnative'):
        assert virtual_facts.get_virtual_facts()['virtualization_role'] == 'guest'


# Generated at 2022-06-13 04:20:49.512843
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    sut = SunOSVirtual(dict(), dict())
    assert isinstance(sut, SunOSVirtual)


# Generated at 2022-06-13 04:20:51.287716
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    sunOSobj = SunOSVirtual({})
    assert sunOSobj.platform == 'SunOS'
    assert dict(sunOSobj.get_virtual_facts()) == {}


# Generated at 2022-06-13 04:20:58.016362
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = make_mock_module()
    virtual = SunOSVirtual(module)
    out = virtual.get_virtual_facts()
    assert out['virtualization_type'] == 'vmware'
    assert out['virtualization_role'] == 'guest'
    assert out['container'] == 'zone'
    assert 'virtualization_tech_host' in out
    assert 'virtualization_tech_guest' in out
    assert 'zone' in out['virtualization_tech_host']
    assert 'zone' in out['virtualization_tech_guest']
    assert 'vmware' in out['virtualization_tech_guest']
    assert 'lpar' not in out['virtualization_tech_guest']
    assert 'lpar' not in out['virtualization_tech_host']

# Generated at 2022-06-13 04:21:02.110429
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    sunos_vc = SunOSVirtualCollector()
    assert sunos_vc._platform == 'SunOS'
    assert sunos_vc._fact_class == SunOSVirtual

# Generated at 2022-06-13 04:21:04.294162
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual = SunOSVirtual({'module': None})
    assert virtual.platform == 'SunOS'

# Generated at 2022-06-13 04:21:14.676726
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils import basic
    import tempfile
    import os
    import json

    # Create temporary env with PATH and ANSIBLE_FACTS
    tmpd = tempfile.mkdtemp()
    env = os.environ.copy()
    env['PATH'] = tmpd + os.pathsep + env['PATH']
    env['ANSIBLE_FACTS'] = json.dumps({'is_sunos': True})

    # Create fake zonename command in temporary dir
    zonename = os.path.join(tmpd, 'zonename')
    with open(zonename, 'w') as f:
        f.write("#!/bin/sh\n")

# Generated at 2022-06-13 04:21:21.934725
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    '''Unit test for constructor of class SunOSVirtualCollector.'''
    # Define a mock module
    module = type('AnsibleModule', (object,), dict(
        fail_json=lambda *args: None,
        get_bin_path=lambda *args: None,
        run_command=lambda *args: None,
    ))

    collector = SunOSVirtualCollector(module=module)
    assert isinstance(collector, SunOSVirtualCollector)
    assert isinstance(collector._fact_class, SunOSVirtual)


# Generated at 2022-06-13 04:21:24.460431
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    x = SunOSVirtualCollector()
    assert x.platform == 'SunOS'
    assert x._fact_class == SunOSVirtual

# Generated at 2022-06-13 04:21:50.796951
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    sc = SunOSVirtualCollector()
    assert sc._platform == "SunOS"
    assert sc._fact_class == SunOSVirtual

# Generated at 2022-06-13 04:21:52.182805
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    s = SunOSVirtualCollector()
    assert isinstance(s, SunOSVirtualCollector)

# Generated at 2022-06-13 04:21:53.627753
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    v = SunOSVirtual({})
    assert v.platform == 'SunOS'


# Generated at 2022-06-13 04:21:59.730086
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = AnsibleModuleMock()

    module.run_command = MagicMock(return_value=(0, 'global', ''))
    zonename = Virtual.get_bin_path(module, 'zonename')
    if zonename is not None:
        module.run_command = MagicMock(return_value=(1, '', ''))
        module.run_command = MagicMock(return_value=(0, 'testzone', ''))
        SunOSVirtual.get_virtual_facts(module)
        assert module.fail_json.called
        module.fail_json.reset_mock()

        module.run_command = MagicMock(return_value=(0, 'nope', ''))
        module.ls = MagicMock(return_value=True)
        Virtual.get_virtual_facts(module)
       

# Generated at 2022-06-13 04:22:07.330931
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    def get_bin_path(module):
        return '/bin/' + module
    module_mock = type('module', (object,), {
        'run_command': lambda self, cmd: (0, '', ''),
        'get_bin_path': get_bin_path,
    })()
    virtual_facts = SunOSVirtual(module_mock).get_virtual_facts()
    assert virtual_facts == {
        'virtualization_tech_host': set(),
        'virtualization_tech_guest': set(),
    }

# Generated at 2022-06-13 04:22:08.797907
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    sv = SunOSVirtual(dict())
    sv.get_virtual_facts()

# Generated at 2022-06-13 04:22:12.545017
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    from ansible.module_utils.facts import Collector
    c = Collector()
    sosvc = SunOSVirtualCollector(c)
    assert sosvc._fact_class == SunOSVirtual
    assert sosvc._platform == 'SunOS'



# Generated at 2022-06-13 04:22:14.073492
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    facts = SunOSVirtual()
    assert isinstance(facts, Virtual)

# Generated at 2022-06-13 04:22:15.640245
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual = SunOSVirtual(None)
    assert virtual.platform == 'SunOS'

# Generated at 2022-06-13 04:22:18.515036
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    x = SunOSVirtualCollector()
    assert x._platform == 'SunOS'
    assert x._fact_class is SunOSVirtual

# Generated at 2022-06-13 04:22:51.573035
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = AnsibleModule(
        argument_spec = dict()
    )
    module.params = dict()
    module.get_bin_path = mock.Mock(return_value='/usr/sbin')
    module.run_command = mock.Mock(return_value=(0, '', ''))

    obj = SunOSVirtual(module)
    obj.collect = mock.Mock(return_value=dict())
    obj.get_virtual_facts()

    module.get_bin_path.assert_any_call('zonename')
    module.get_bin_path.assert_any_call('virtinfo')
    module.get_bin_path.assert_any_call('modinfo')

    module.run_command.assert_any_call('zonename')

# Generated at 2022-06-13 04:23:01.277840
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = SunOSVirtual(None, None)
    module.module.exit_json = lambda a: None

    # Test full SunOS zone
    module.get_bin_path.side_effect = lambda a: os.path.join('/bin', a)
    module.run_command.side_effect = lambda a: (0, '/bin/zonename global', None)
    module.os.path.isdir.side_effect = lambda a: False

    virtual_facts = module.get_virtual_facts()

    assert_equals(virtual_facts["container"], "zone")
    assert_equals(virtual_facts["virtualization_role"], "host (guest)")
    assert_equals(virtual_facts["virtualization_type"], "zone")

# Generated at 2022-06-13 04:23:06.232908
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    module = FakeAnsibleModule()
    virtual = SunOSVirtual(module)

    assert virtual.virtualization_tech_guest == set()
    assert virtual.virtualization_tech_host == set()
    assert virtual.virtualization_type is None
    assert virtual.virtualization_role is None
    assert virtual.container is None


# Generated at 2022-06-13 04:23:08.587837
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    """
    Test get_virtual_facts of SunOSVirtual class.
    """
    pass  # TODO

# Generated at 2022-06-13 04:23:17.199674
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.sunos import SunOSVirtual
    import json

    module = get_test_module()
    data = {'module': module, 'virtual_facts': []}
    virtual_facts = SunOSVirtual(data)
    virtual_facts.get_virtual_facts()
    assert json.dumps(data['virtual_facts']) == '''{
        "virtualization_role": "guest",
        "virtualization_type": "kvm",
        "virtualization_tech_host": [
            "zone"
        ],
        "virtualization_tech_guest": [
            "zone",
            "kvm"
        ]
    }'''



# Generated at 2022-06-13 04:23:20.779786
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    fake_module = object()
    virtual_instance = SunOSVirtual(fake_module)
    assert virtual_instance.module == fake_module
    assert virtual_instance.platform == 'SunOS'


# Generated at 2022-06-13 04:23:26.472470
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # Test with an host in a zone
    zone_module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True,
    )
    zone_module.run_command = MagicMock(return_value=(0, "non-global", ""))
    zone_module.get_bin_path = MagicMock(return_value="/usr/sbin/zonename")
    virtual = SunOSVirtual(zone_module)
    assert virtual.get_virtual_facts() == {"container": "zone",
                                           "virtualization_role": "guest",
                                           "virtualization_tech_guest": set(["zone"]),
                                           "virtualization_tech_host": set()}

    # Test with an host in a branded zone

# Generated at 2022-06-13 04:23:36.543183
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.sunos import SunOSVirtual

    sunos = SunOSVirtual({})
    sunos.module = MockModule()

    # Test only the virtual_facts, the others are tested in test_Virtual
    virtual_facts = sunos.get_virtual_facts()
    
    assert virtual_facts['virtualization_tech_host'] == set(['zone'])
    assert virtual_facts['virtualization_tech_guest'] == set(['zone', 'vmware'])
    assert virtual_facts['virtualization_type'] == 'vmware'
    assert virtual_facts['container'] == 'zone'
    assert virtual_facts['virtualization_role'] == 'guest'

# MockModule is a class with a run_command method.
# Its only purpose is to mock the methods of a real AnsibleModule

# Generated at 2022-06-13 04:23:39.576061
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    test_class = SunOSVirtualCollector()
    assert test_class.platform == 'SunOS'
    assert test_class._fact_class == SunOSVirtual

# Generated at 2022-06-13 04:23:42.441054
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    facts = SunOSVirtualCollector.collect()
    assert 'virtualization' in facts
    fact = facts['virtualization']
    assert 'type' in fact
    assert 'role' in fact
    assert 'zone' in fact

# Generated at 2022-06-13 04:24:12.638245
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    module = AnsibleModule({})
    virt = SunOSVirtual(module)
    assert virt.module == module
    assert virt.platform == 'SunOS'
    assert virt.virtual_facts == {}

# Unit tests for get_virtual_facts method of class SunOSVirtual

# Generated at 2022-06-13 04:24:14.241717
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    assert SunOSVirtual().get_virtual_facts() == None


# Generated at 2022-06-13 04:24:15.864658
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    assert SunOSVirtualCollector()

# Generated at 2022-06-13 04:24:17.762019
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    x = SunOSVirtualCollector()
    assert x.platform == "SunOS"
    assert x._fact_class == SunOSVirtual

# Generated at 2022-06-13 04:24:19.203383
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virt = SunOSVirtual()
    assert type(virt) == SunOSVirtual


# Generated at 2022-06-13 04:24:21.682753
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    module = AnsibleModuleMock()
    module.params = {'gather_subset': 'virtual'}
    virtual = SunOSVirtual(module)
    assert(virtual.platform == 'SunOS')



# Generated at 2022-06-13 04:24:23.165994
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    result = SunOSVirtualCollector()
    assert result._platform == 'SunOS'


# Generated at 2022-06-13 04:24:32.781356
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    """ Test the constructor of SunOSVirtual class
    """
    module = AnsibleModule({})
    cls = SunOSVirtual(module)
    assert cls.module == module
    assert cls.platform == 'SunOS'
    assert cls.get_virtual_facts.__module__ == 'ansible.module_utils.facts.virtual.sunos'
    assert cls.get_virtual_facts.__name__ == 'SunOSVirtual'
    assert cls.get_virtual_facts.__doc__ == '''Return virtualization-related facts'''

# Generated at 2022-06-13 04:24:43.390407
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = FakeModule()
    module.run_command = MagicMock(return_value=(0, 'global'))
    module.get_bin_path = MagicMock(return_value='/usr/sbin/zonename')
    virtual = SunOSVirtual(module)
    virtual.get_virtual_facts()
    assert virtual.virtual_facts['container'] == 'zone'
    assert virtual.virtual_facts['virtualization_role'] == 'host'
    assert virtual.virtual_facts['virtualization_tech_host'] == set('zone')
    assert virtual.virtual_facts['virtualization_tech_guest'] == set()

    module.run_command = MagicMock(return_value=(0, 'non-global'))

# Generated at 2022-06-13 04:24:48.768731
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    '''
    Test VirtualCollector() constructor
    '''
    module = collections.namedtuple('module', ['params'])
    module.params = {'gather_timeout': 1, 'gather_subset': []}
    vc = SunOSVirtualCollector(module)
    assert vc._platform == 'SunOS'
    assert vc._fact_class == SunOSVirtual



# Generated at 2022-06-13 04:25:21.333551
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = FakeAnsibleModule()
    module.run_command = fake_run_command
    module.get_bin_path = fake_get_bin_path
    virtual = SunOSVirtual(module)
    virtual_facts = virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''
    assert 'container' not in virtual_facts
    assert virtual_facts['virtualization_tech_guest'] == set()
    assert virtual_facts['virtualization_tech_host'] == set()


# Generated at 2022-06-13 04:25:23.269715
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual = SunOSVirtual('')
    assert virtual.platform == 'SunOS'

# Generated at 2022-06-13 04:25:26.541905
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    fc = SunOSVirtualCollector()
    assert fc.__class__.__name__ == "SunOSVirtualCollector"
    assert SunOSVirtualCollector._platform == 'SunOS'
    assert SunOSVirtualCollector._fact_class == SunOSVirtual

# Generated at 2022-06-13 04:25:34.580315
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # Setup
    module = FakeAnsibleModule()
    module.run_command.return_value = (0, 'global', '')  # zonename command

    # Test
    sunos_virtual = SunOSVirtual(module)
    virtual_facts = sunos_virtual.get_virtual_facts()

    # Assertions
    assert virtual_facts['virtualization_role'] == 'host'
    assert virtual_facts['virtualization_tech_host'] == set(['zone'])
    assert virtual_facts['virtualization_tech_guest'] == set()



# Generated at 2022-06-13 04:25:41.719610
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = AnsibleModuleMock()
    module.run_command = run_command_mock
    module.get_bin_path = get_bin_path_mock

    # define test values
    zonename = os.path.join(os.path.dirname(__file__), 'fixtures', 'virtual_facts_zonename.txt')
    modinfo = os.path.join(os.path.dirname(__file__), 'fixtures', 'virtual_facts_modinfo.txt')
    smbios = os.path.join(os.path.dirname(__file__), 'fixtures', 'virtual_facts_smbios.txt')
    virtinfo = os.path.join(os.path.dirname(__file__), 'fixtures', 'virtual_facts_virtinfo.txt')

    # read test

# Generated at 2022-06-13 04:25:51.776597
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    import imp
    import sys
    import os

    from ansible.module_utils.facts.virtual.sunos import SunOSVirtual

    # Import module snippets
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'plugins', 'module_utils'))
    sys.modules['ansible.module_utils.facts.virtual.sunos'] = SunOSVirtual

    imp.load_source('ansible.module_utils.facts.virtual.sunos', 'ansible/module_utils/facts/virtual/sunos.py')

    from ansible.module_utils.facts.virtual.sunos import SunOSVirtual

    class MockModule:
        def get_bin_path(self, executable):
            return '/opt/bin/'


# Generated at 2022-06-13 04:26:01.048423
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.sunos import Virtual
    module = MockAnsibleModule()
    virtual = SunOSVirtual(module)

    # Method get_virtual_facts - run in global zone
    zonename_output = "global"
    zonename_rc = 0
    module.get_bin_path = Mock(side_effect=lambda x: '/usr/bin/zonename')
    module.run_command = Mock(side_effect=lambda x: (zonename_rc, zonename_output, None))
    module.exists = Mock(side_effect=lambda x: False)
    facts = virtual.get_virtual_facts()
    assert facts['virtualization_type'] == ''
    assert facts['virtualization_role'] == ''
    assert facts['container'] == ''

# Generated at 2022-06-13 04:26:02.440523
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    x = SunOSVirtualCollector()
    assert x._platform == 'SunOS'

# Generated at 2022-06-13 04:26:03.808108
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    x = SunOSVirtual(dict(module=None))
    assert x.platform == "SunOS"

# Generated at 2022-06-13 04:26:05.362086
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    test_obj = SunOSVirtual({})

    assert test_obj.platform == 'SunOS'

# Generated at 2022-06-13 04:27:03.066024
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    # This should not raise any exception
    SunOSVirtualCollector()

# Generated at 2022-06-13 04:27:13.411129
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():

    class MockModule(object):
        """
        Class for mocking module
        """
        def __init__(self):
            self.params = {}
            self.args = {}
            self.facts = {}

        def get_bin_path(self, cmd):
            self.facts = {}
            if cmd == 'zonename':
                return '/usr/sbin/zonename'
            elif cmd == 'modinfo':
                return '/usr/sbin/modinfo'
            elif cmd == 'virtinfo':
                return '/usr/sbin/virtinfo'
            elif cmd == 'smbios':
                return '/usr/sbin/smbios'
            return None

        def run_command(self, *args, **kwargs):
            """
            Method for mocking the module.run_command method
            """

# Generated at 2022-06-13 04:27:16.958229
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # The facts should be the same as the name of the class
    facts = SunOSVirtual().get_virtual_facts()
    assert facts == SunOSVirtual().get_virtual_facts(), 'The facts should be the same as the name of the class'

# Generated at 2022-06-13 04:27:25.260067
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    """
    This is a basic test case to instantiate SunOSVirtualCollector and
    check, if it raises the correct exception upon instantiation.
    """
    module = type('module', (object,), {})
    setattr(module, 'get_bin_path', lambda x: x)
    collector = SunOSVirtualCollector(module)
    assert type(collector) == SunOSVirtualCollector, 'Is not of type SunOSVirtualCollector.'
    try:
        collector.collect()
    except Exception as e:
        assert type(e) == NotImplementedError, 'Exception raised is not of type NotImplementedError.'
        assert e.args[0] == 'VirtualCollector is abstract.', 'Exception raised does not contain expected string.'

# Generated at 2022-06-13 04:27:26.796143
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    v = SunOSVirtual({}, {}, 'SunOS')
    assert v._platform == 'SunOS'


# Generated at 2022-06-13 04:27:29.385355
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # This is a pretty useless test case, but at least we make sure we don't have a syntax error.
    SunOSVirtual({}, None).get_virtual_facts()

# Generated at 2022-06-13 04:27:36.588746
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    class MockModule(object):
        def __init__(self, result):
            self.result = result

        def get_bin_path(self, name, required=False):
            if name == 'zonename':
                return True
            elif name == 'modinfo':
                return True
            else:
                return False

        def run_command(self, args):
            return self.result
    # Scenario:
    # Zonename returns “global”
    # modinfo finds a virtualization type
    mock_module = MockModule((0, "global\n", ""))
    mock_module.run_command = MockModule((0, "", ""))

# Generated at 2022-06-13 04:27:38.052592
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual_facts = SunOSVirtual()
    assert virtual_facts._platform == 'SunOS'

# Generated at 2022-06-13 04:27:39.012371
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    SunOSVirtualCollector()

# Generated at 2022-06-13 04:27:41.670232
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    sunos_virtual_collector = SunOSVirtualCollector()
    assert sunos_virtual_collector._platform == 'SunOS'
    assert sunos_virtual_collector._fact_class is SunOSVirtual

# Generated at 2022-06-13 04:28:57.116632
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    sunos_virtual_collector = SunOSVirtualCollector()
    assert sunos_virtual_collector._fact_class == SunOSVirtual
    assert sunos_virtual_collector._platform == 'SunOS'


# Generated at 2022-06-13 04:29:07.368305
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # Create a dummy module
    module = AnsibleModule(argument_spec={})

    # Create a dummy class for it's methods to return the required
    # data.
    class DummyModule(object):
        def run_command(self, args):
            # rc 0
            # stdout:
            # global
            # stderr:
            rc0 = (0, 'global', '')

            # rc 0
            # stdout:
            # modinfo: could not open module /kernel/misc/vmware: No such file or directory
            # modinfo: could not open module /kernel/misc/virtualbox: No such file or directory
            # modinfo: could not open module /kernel/misc/virtio: No such file or directory
            # modinfo: could not open module /kernel/misc/kvm: No such file or directory
           

# Generated at 2022-06-13 04:29:09.935412
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    c = SunOSVirtualCollector()
    assert c._fact_class == SunOSVirtual
    assert c._platform == 'SunOS'

# Generated at 2022-06-13 04:29:10.666717
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    SunOSVirtualCollector()

# Generated at 2022-06-13 04:29:14.744963
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    #
    # I'd like to test the facts returned by get_virtual_facts() here, but
    # I don't know how to do this without calling AnsibleModule.run_command()
    # and that's not possible in a unit test.  If you know how, please fix this.
    #
    pass

# Generated at 2022-06-13 04:29:16.478374
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    obj = SunOSVirtualCollector()
    assert obj._platform == 'SunOS'
    assert obj._fact_class == SunOSVirtual



# Generated at 2022-06-13 04:29:23.831494
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # Test with nothing in /proc
    test_module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    test_module.exit_json = MagicMock(return_value=None)
    SunOSVirtual.get_virtual_facts(test_module)
    test_module.exit_json.assert_called_once_with(
        changed=False,
        ansible_facts={
            'virtualization_tech_guest': set(),
            'virtualization_tech_host': set()
        }
    )

# Generated at 2022-06-13 04:29:30.987050
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    """Test get_virtual_facts of SunOSVirtual without zone or VM type (other than zone)"""
    module = type('AnsModule', (object,), {'get_bin_path': lambda self, name: None, 'run_command': lambda self, cmd: (0, "", "")})()
    virtual = SunOSVirtual(module)
    expected_virtual_facts = {
        'container': None,
        'virtualization_type': None,
        'virtualization_role': None,
        'virtualization_tech_host': set(),
        'virtualization_tech_guest': set()
    }
    assert virtual.get_virtual_facts() == expected_virtual_facts



# Generated at 2022-06-13 04:29:32.320161
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    virtual = SunOSVirtualCollector()
    assert virtual



# Generated at 2022-06-13 04:29:38.612642
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    virtual = SunOSVirtual()
    virtual._module = FakeAnsibleModule({
        'path': '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/bin/X11:/usr/games:/opt/VirtualBox/bin:/usr/sfw/bin:/usr/sfw/sbin:/opt/ecs/bin'
    })
    result = virtual.get_virtual_facts()
    assert 'virtualization_type' in result
    assert 'virtualization_role' in result
    assert 'container' in result
    assert 'virtualization_tech_guest' in result
    assert 'virtualization_tech_host' in result
