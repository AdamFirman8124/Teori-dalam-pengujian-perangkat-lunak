

# Generated at 2022-06-13 03:59:38.659400
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    # initialize class
    virtual_facts = HPUXVirtual()
    # ansible module Mock class
    class AnsibleModuleMock(object):
        def __init__(self):
            self.run_command_counter = 0
            self.run_command_calls = {}

        def run_command(self, command):
            self.run_command_calls.setdefault(self.run_command_counter, command)
            self.run_command_counter += 1
            if command == "/usr/sbin/vecheck":
                return (0, "", "")
            elif command == "/opt/hpvm/bin/hpvminfo":
                return (0, "Running HPVM guest\n", "")
            elif command == "/usr/sbin/parstatus":
                return (0, "", "")
            return

# Generated at 2022-06-13 03:59:41.025150
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual
    h = HPUXVirtual()
    facts = h.get_virtual_facts()
    assert facts['virtualization_tech_guest'] == set()


# Generated at 2022-06-13 03:59:43.120329
# Unit test for method get_virtual_facts of class HPUXVirtual

# Generated at 2022-06-13 03:59:46.092806
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts = HPUXVirtual()
    assert virtual_facts.__class__.__name__ == 'HPUXVirtual'
    assert isinstance(virtual_facts, Virtual) is True


# Generated at 2022-06-13 03:59:47.951161
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual = HPUXVirtual()
    assert hpux_virtual.platform == "HP-UX"


# Generated at 2022-06-13 03:59:49.700923
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpx = HPUXVirtual(dict(module=None))
    assert hpx.platform == 'HP-UX'

# Generated at 2022-06-13 03:59:54.051314
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virt = HPUXVirtual({})
    assert virt.data['virtualization_type'] == 'guest'
    assert virt.data['virtualization_role'] == 'HP vPar'
    assert virt.data['virtualization_tech_guest'] == 'HP nPar'
    assert virt.data['virtualization_tech_host'] == 'HPVM'
    assert virt.data['virtualization_system'] == 'HPVM'

# Generated at 2022-06-13 03:59:57.102917
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
	hpx_virtual = HPUXVirtual()
	assert hpx_virtual.get_virtual_facts()['virtualization_tech_host'] == set()
	assert hpx_virtual.get_virtual_facts()['virtualization_tech_guest'] == set()

# Generated at 2022-06-13 04:00:04.199047
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts import ModuleTestCase
    from ansible.module_utils.facts.virtual.hpar import HPUXVirtual
    from ansible.module_utils.facts.virtual.ivm import HPUXVirtual
    from ansible.module_utils.facts.virtual.vm import HPUXVirtual

    class TestHPUXVirtualizationBase(ModuleTestCase):
        """
        Test class for AnsibleModuleUtilsVirtualizationHPUXModule
        """
        def setUp(self):
            """
            Setup function for ModuleTestCase class
            """
            super(TestHPUXVirtualizationBase, self).setUp()
            self.hpar = HPUXVirtual()
            self.ivm = HPUXVirtual()
            self.vm = HPUXVirtual()


# Generated at 2022-06-13 04:00:07.930089
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual = HPUXVirtual()
    assert virtual._facts['virtualization_type'] == 'guest'
    assert virtual._facts['virtualization_role'] == 'HP nPar'
    assert virtual._facts['virtualization_tech_guest'] == set(['HP nPar'])
    assert virtual._facts['virtualization_tech_host'] == set()


# Generated at 2022-06-13 04:00:24.508573
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    class MockModule:
        def __init__(self):
            self.run_command_response = [0, '', '']

        def run_command(self, args):
            return self.run_command_response

    class MockFactCollector:
        def __init__(self):
            self.module = MockModule()
            self.facts = {}
            self.collected_facts = {'ansible_system': 'HP-UX'}

    # test getting facts from OS command

# Generated at 2022-06-13 04:00:33.189774
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module = FakeModule()
    hv = HPUXVirtual(module)

    module.run_command = lambda cmd: (0, 'Running HPVM host.', '')
    assert hv.get_virtual_facts() == {
        'virtualization_role': 'HPVM',
        'virtualization_type': 'host',
        'virtualization_tech_guest': set(['HPVM']),
        'virtualization_tech_host': set(),
    }

    module.run_command = lambda cmd: (0, 'Running HPVM guest.', '')

# Generated at 2022-06-13 04:00:40.451290
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    # test with guest on HP vPar
    ve_check_output = """
/usr/sbin/vecheck:  Virtual Partition enabled.
"""
    h = HPUXVirtual({'module_name': 'ansible', 'module_args': ''})
    setattr(h, 'module', MockModule(ve_check_output))
    assert h.get_virtual_facts() == {'virtualization_type': 'guest',
                                     'virtualization_role': 'HP vPar',
                                     'virtualization_tech_guest': {'HP vPar'},
                                     'virtualization_tech_host': set()}
    # test with guest on nPar

# Generated at 2022-06-13 04:00:41.462680
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    gv = HPUXVirtualCollector({}, {})
    assert gv.platform == 'HP-UX'

# Generated at 2022-06-13 04:00:49.263952
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hp_ux import HPUXVirtual
    # Test with os.path.exists(/usr/sbin/vecheck) True
    HPUXVirtual.module = MockOsPathExistsModule(['/usr/sbin/vecheck'], output=['0', '', ''])
    facts = {}
    expected_facts = {'virtualization_type': 'guest',
                      'virtualization_role': 'HP vPar',
                      'virtualization_tech_guest': {'HP vPar'},
                      'virtualization_tech_host': set()}
    HPUXVirtual().get_virtual_facts(facts)
    assert expected_facts == facts



# Generated at 2022-06-13 04:00:51.416891
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    HPUX_virtual = HPUXVirtual(dict(module=None))
    return True

# Unit test to check the resulting facts

# Generated at 2022-06-13 04:00:55.506810
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module = AnsibleModule(argument_spec={})
    virt = HPUXVirtual(module)
    facts = virt.get_virtual_facts()
    assert 'virtualization_tech_guest' in facts
    assert 'virtualization_tech_host' in facts
    assert 'virtualization_role' in facts
    assert 'virtualization_type' in facts

# Generated at 2022-06-13 04:00:58.593032
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts = HPUXVirtual()
    assert virtual_facts.platform == 'HP-UX'


# Generated at 2022-06-13 04:01:00.209999
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual = HPUXVirtual()
    assert hpux_virtual.platform == 'HP-UX'

# Generated at 2022-06-13 04:01:07.943608
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    import unittest
    import ansible.module_utils.facts.virtual.hpu
    import ansible.module_utils.facts.virtual.hpu as hp_facts

    hp_facts.os.path.exists = lambda x: True

    hp_facts.open = lambda x, y: FakeOpen("No vpars found.\n")
    hp_virtual = hp_facts.HPUXVirtual(None)
    assert hp_virtual.get_virtual_facts() == {'virtualization_type': 'guest',
                                              'virtualization_role': 'HP vPar',
                                              'virtualization_tech_host': set(),
                                              'virtualization_tech_guest': set(['HP vPar'])}


# Generated at 2022-06-13 04:01:31.188735
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module = DummyAnsibleModule()
    hpux_virtual = HPUXVirtual(module)
    facts = hpux_virtual.get_virtual_facts()
    assert 'virtualization_role' in facts
    assert 'virtualization_type' in facts
    assert 'virtualization_tech_guest' in facts
    assert 'virtualization_tech_host' in facts

# To unit test method get_virtual_facts of class HPUXVirtual, we need to have
# a dummy class since we have to mock out run_command. This is the dummy class.

# Generated at 2022-06-13 04:01:41.765102
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    class HPUXModuleFake:
        def __init__(self):
            self.params = {}
            self.params['gather_subset'] = ['all']

        def exit_json(self, rc, out):
            return rc, out

        def run_command(self, command):
            return 0, '', ''

    class AnsibleModuleFake:
        def __init__(self):
            self.check_mode = False
            self.params = {}
            self.params['filter'] = '*'
            self.params['gather_subset'] = 'all'
            self.params['gather_timeout'] = 10
            self.params['filter'] = '*'
            self.fail_json = ExitJson
            self.exit_json = ExitJson
            self.run_command = RunCommand


# Generated at 2022-06-13 04:01:52.439584
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    """ Unit test for method get_virtual_facts of class HPUXVirtual """
    test_obj = HPUXVirtual()
    assert(test_obj.get_virtual_facts()['virtualization_type'] == 'host')
    assert(test_obj.get_virtual_facts()['virtualization_role'] == 'HPVM')
    assert('HPVM' in test_obj.get_virtual_facts()['virtualization_tech_guest'])
    assert('HPVM IVM' in test_obj.get_virtual_facts()['virtualization_tech_guest'])
    assert('HPVM vPar' in test_obj.get_virtual_facts()['virtualization_tech_guest'])
    assert('HP nPar' in test_obj.get_virtual_facts()['virtualization_tech_guest'])

# Generated at 2022-06-13 04:01:56.198418
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():

    virtual_instance = HPUXVirtual()
    assert virtual_instance._platform == 'HP-UX'
    assert virtual_instance._fact_class == 'HPUXVirtual'

    virtual_collector_instance = HPUXVirtualCollector()
    assert virtual_collector_instance._fact_class == HPUXVirtual
    assert virtual_collector_instance._platform == 'HP-UX'

# Generated at 2022-06-13 04:02:03.875340
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module = FakeAnsibleModule()
    module.mock_command("/usr/sbin/vecheck")
    module.mock_command("/opt/hpvm/bin/hpvminfo")
    module.mock_command("/usr/sbin/parstatus")
    hp_facts = HPUXVirtual(module).get_virtual_facts()
    assert hp_facts['virtualization_tech_guest'] == set()
    assert hp_facts['virtualization_tech_host'] == set()
    assert hp_facts['virtualization_type'] == 'guest'
    assert hp_facts['virtualization_role'] == 'HP vPar'

    module.run_command("/usr/sbin/vecheck").set_rc(1)

# Generated at 2022-06-13 04:02:05.369973
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts = HPUXVirtual(dict())
    assert virtual_facts.platform == 'HP-UX'



# Generated at 2022-06-13 04:02:06.717808
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts_hpux = HPUXVirtual({}, {})
    assert virtual_facts_hpux.platform == 'HP-UX'


# Generated at 2022-06-13 04:02:09.731560
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual = HPUXVirtual(dict())
    assert virtual.platform == 'HP-UX'


# Generated at 2022-06-13 04:02:12.863178
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    """
    This function tests get_virtual_facts by checking result not empty.
    """
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual
    result = HPUXVirtual.get_virtual_facts(None)
    assert result != None


# Generated at 2022-06-13 04:02:19.058514
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module = AnsibleModuleMock()
    run_command_result = ([0, '', ''], 0, '')
    module.run_command = MagicMock(return_value=run_command_result)
    h = HPUXVirtual(module)

    h.path_exists = MagicMock(return_value=True)
    h.get_file_content = MagicMock(return_value='')
    assert(h.get_virtual_facts() == {'virtualization_tech_host': set(), 'virtualization_tech_guest': set(['HP nPar'])})
    h.path_exists.assert_called_with('/usr/sbin/parstatus')
    h.get_file_content.assert_not_called()


# Generated at 2022-06-13 04:03:25.853296
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    class ModuleMock(object):
        def __init__(self):
            self.run_command = lambda x, check_rc=True: (0, x, '')
            self.params = {}

    class Facts(object):
        def __init__(self):
            self.module = ModuleMock()
            self.current_platform = "HP-UX"
            self.gather_subset = lambda x: ['all']
            self.get_filesystems = lambda x: []
            self.get_mount_points = lambda x: []

        def get(self, key, default=None):
            return default

    from ansible.module_utils.facts.virtual import HPUXVirtual
    hp_virtual_obj = HPUXVirtual(Facts())
    hp_virtual_obj.get_virtual_facts()

# Generated at 2022-06-13 04:03:33.131517
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts import ModuleArgsParser
    from ansible.module_utils.facts.virtual.hpar import Virtual, HPUXVirtualCollector

    ansible_module = MockAnsibleModule(argument_spec=dict())
    argument_spec = dict()
    arguments = ModuleArgsParser.from_params(ansible_module.params, argument_spec)
    virtual = HPUXVirtualCollector.fetch_virtual_facts(arguments)

    # Test guest
    module = MockAnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True,
        run_command_stubber=True,
    )
    module.run_command_stubber.set_command('/usr/sbin/parstatus', (0, 'parstatus', ''))
    module.run_command

# Generated at 2022-06-13 04:03:35.777215
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virt = HPUXVirtual(dict())
    assert virt.platform == 'HP-UX'


# Generated at 2022-06-13 04:03:38.060785
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual = HPUXVirtual(dict(module=dict()))
    assert hpux_virtual.platform == 'HP-UX'


# Generated at 2022-06-13 04:03:43.462182
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpx_virtual = HPUXVirtual(None)
    assert hpx_virtual.platform == 'HP-UX'
    assert hpx_virtual.get_virtual_facts() == {'virtualization_type': 'guest', 'virtualization_role': 'HP vPar', 'virtualization_tech_guest': {'HP vPar'}, 'virtualization_tech_host': set()}



# Generated at 2022-06-13 04:03:45.170432
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual = HPUXVirtual(dict(module=None))
    assert hpux_virtual.platform == 'HP-UX'


# Generated at 2022-06-13 04:03:48.627350
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module = MockModule()
    hpuxvirtual = HPUXVirtual(module)
    hpuxvirtual.module.run_command = Mock(return_value=(0, None, None))
    hpuxvirtual.get_virtual_facts()
    assert hpuxvirtual.facts['virtualization_type'] == 'host'
    print("Done.")

# Unit test to test HPUXVirtual.platform

# Generated at 2022-06-13 04:03:52.070541
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpu = HPUXVirtual()
    hpu.get_virtual_facts()

    assert hpu.virtualization_type == 'guest'
    assert hpu.virtualization_role == 'HPVM'

# Generated at 2022-06-13 04:03:58.313444
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    test_module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=['!all'], type='list')
        ),
        supports_check_mode=True
    )

    # Create a HPUXVirtual object
    virt_obj = HPUXVirtual(module=test_module)

    # Run method get_virtual_facts to get virtualization facts
    virtual_facts = virt_obj.get_virtual_facts()

    # Assert method get_virtual_facts return value
    test_module.exit_json(ansible_facts=dict(ansible_virtualization=virtual_facts))

# Generated at 2022-06-13 04:04:05.254076
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    Virtual.module = MagicMock()
    Virtual.module.run_command.return_value = (
        0,
        "Running as HPVM guest system - HPVM 5.1 (05.01.00.00 HPVM IR1) reboot_notify",
        ""
    )
    hpux_virtual = HPUXVirtual()
    assert hpux_virtual.get_virtual_facts() == {
        'virtualization_type': 'guest',
        'virtualization_role': 'HPVM IVM',
        'virtualization_tech_guest': set(['HPVM IVM']),
        'virtualization_tech_host': set()
    }

# Generated at 2022-06-13 04:05:46.888036
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.facts import FactManager
    from ansible.module_utils.facts.virtual.base import BaseVirtual, VirtualCollector

    module = MockModule()
    facts = FactManager(module=module, collect_subset=['virtual'])
    HPUXVirtual.get_virtual_facts(module)
    assert module.run_command.call_count == 0

    module = MockModule(**ImmutableDict({'run_command.return_value': (
        0, 'HPVM guest', '')}))
    facts = FactManager(module=module, collect_subset=['virtual'])

# Generated at 2022-06-13 04:05:47.630119
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    assert HPUXVirtual.platform == 'HP-UX'

# Generated at 2022-06-13 04:05:49.871846
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    facts = HPUXVirtual('ansible.module_utils.facts.virtual.hpu')
    assert facts.get_virtual_facts() == {
        'virtualization_type': 'guest',
        'virtualization_role': 'HP vPar'
    }

# Generated at 2022-06-13 04:05:57.470672
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    if os.path.exists('/usr/sbin/vecheck'):
        result = {'virtualization_type': 'guest', 'virtualization_role': 'HP vPar', 'virtualization_tech_guest': {'HP vPar'}, 'virtualization_tech_host': set()}
    elif os.path.exists('/opt/hpvm/bin/hpvminfo'):
        result = {'virtualization_type': 'host', 'virtualization_role': 'HPVM', 'virtualization_tech_guest': {'HPVM'}, 'virtualization_tech_host': set()}

# Generated at 2022-06-13 04:05:59.817667
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual = HPUXVirtual("")
    assert virtual.platform == "HP-UX"

# Generated at 2022-06-13 04:06:01.365092
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual = HPUXVirtual()
    assert hpux_virtual is not None


# Generated at 2022-06-13 04:06:04.186678
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual = HPUXVirtual()
    assert hpux_virtual.data['virtualization_type'] == 'host'
    assert hpux_virtual.data['virtualization_role'] == 'HPVM'
    assert hpux_virtual.data['virtualization_tech_guest'] == set(['HPVM'])
    assert hpux_virtual.data['virtualization_tech_host'] == set()


# Generated at 2022-06-13 04:06:06.155241
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts = HPUXVirtual()
    assert virtual_facts.platform == 'HP-UX'

# Generated at 2022-06-13 04:06:13.163515
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    class TestModule(object):
        def run_command(self, *args, **kwargs):
            return 0, '', ''
    testmodule = TestModule()
    virtual = HPUXVirtual(testmodule)
    assert virtual.get_virtual_facts() ==\
        {'virtualization_type': 'guest',
         'virtualization_role': 'HP nPar',
         'virtualization_tech_guest': set(['HP nPar']),
         'virtualization_tech_host': set()}

# Generated at 2022-06-13 04:06:23.410221
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    import types
    module = types.ModuleType('ansible_test_HPUXVirtual')
    module.run_command = lambda *_: (0, '', '')
    hpux_virtual = HPUXVirtual(module)

    if os.path.exists('/usr/sbin/vecheck'):
        os.path.exists = lambda *_: True
        virtual_facts = hpux_virtual.get_virtual_facts()
        assert virtual_facts['virtualization_type'] == 'guest'
        assert virtual_facts['virtualization_role'] == 'HP vPar'
        assert virtual_facts['virtualization_tech_guest'] == {'HP vPar'}
        assert virtual_facts['virtualization_tech_host'] == set()

# Generated at 2022-06-13 04:08:29.228149
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual import HPUXVirtual
    from ansible.module_utils.facts import ModuleStub
    module = ModuleStub()
    facts_obj = HPUXVirtual(module)

    # Test 1: Test for HP nPar
    module.run_command = Mock(return_value=(0, '', ''))

# Generated at 2022-06-13 04:08:37.427095
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    # no virtualisation
    m = HPUXVirtual({})
    assert m.get_virtual_facts() == {'virtualization_type': 'host',
                                     'virtualization_role': 'host',
                                     'virtualization_tech_host': set(),
                                     'virtualization_tech_guest': set()}
    # hpvminfo
    m = HPUXVirtual({'path_exists@/opt/hpvm/bin/hpvminfo': True,
                     'run_command@/opt/hpvm/bin/hpvminfo': (0,
                                                            " Running HPVM host, hpvm:hpvm_control, hostname:hpvm_con, hpvm:hpvm_control",
                                                            "")})

# Generated at 2022-06-13 04:08:47.128724
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    class ModuleMock():
        def __init__(self):
            self.run_command_result = dict(rc=0,
                                           stdout='',
                                           stderr='')
        def run_command(self, cmd, check_rc=True):
            return self.run_command_result

    class HPUXVirtualMock(HPUXVirtual):
        def get_file_content(self, path):
            return ''
        def get_uname_field(self, field):
            return self.uname_result
        def get_sysctl(self, key):
            return self.sysctl_result
        def get_cmdline(self, key):
            return self.cmdline_result
        def get_mount_size(self, path):
            return 0

# Generated at 2022-06-13 04:08:57.792436
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    module = os.path.realpath(__file__)
    facts = dict()
    virtual = HPUXVirtual(module, facts)
    virtual.get_virtual_facts()
    virtual.populate()
    facts = virtual.facts
    assert facts['virtualization_role'] == u'HPVM vPar' or \
           facts['virtualization_role'] == u'HPVM IVM' or \
           facts['virtualization_role'] == u'HPVM' or \
           facts['virtualization_role'] == u'HP nPar' or \
           facts['virtualization_role'] == u'HP vPar'
    assert facts['virtualization_type'] == u'guest'
    assert len(facts['virtualization_tech_guest']) > 0
    assert len(facts['virtualization_tech_host']) == 0

# Generated at 2022-06-13 04:08:59.681179
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts = HPUXVirtual()
    assert virtual_facts._platform == 'HP-UX'
    assert len(virtual_facts.get_virtual_facts()) == 3

# Generated at 2022-06-13 04:09:02.469833
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual = HPUXVirtual(dict())
    assert hpux_virtual.platform == 'HP-UX'


# Generated at 2022-06-13 04:09:09.519491
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts import Virtual
    from ansible.module_utils.facts.virtual.hpux import Virtual
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtualCollector
    from ansible.module_utils.facts.virtual.hpux import test_HPUXVirtual_get_virtual_facts
    import IPython
    Virtual.get_virtual_facts = test_HPUXVirtual_get_virtual_facts.Virtual.get_virtual_facts
    HPUXVirtual.get_virtual_facts = test_HPUXVirtual_get_virtual_facts.HPUXVirtual.get_virtual_facts
    HPUXVirtualCollector.get_virtual_facts = test_HPUXVirtual_get_virtual

# Generated at 2022-06-13 04:09:10.328734
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    assert HPUXVirtual(dict()) is not None

# Generated at 2022-06-13 04:09:17.627625
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    """
    Test the method get_virtual_facts of class HPUXVirtual
    """
    module = AnsibleModule(
        argument_spec=dict()
    )

    if not os.path.exists('/usr/sbin/vecheck'):
        open('/usr/sbin/vecheck', 'a').close()
    if not os.path.exists('/opt/hpvm/bin/hpvminfo'):
        open('/opt/hpvm/bin/hpvminfo', 'a').close()
    if not os.path.exists('/usr/sbin/parstatus'):
        open('/usr/sbin/parstatus', 'a').close()

    hpuxv = HPUXVirtual(module)


# Generated at 2022-06-13 04:09:25.303916
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    module = FakeAnsibleModule()
    hpux_collector = HPUXVirtual(module=module)
    if os.path.exists('/usr/sbin/vecheck'):
        hpux_collector.get_virtual_facts()
        assert hpux_collector.facts['virtualization_type'] == 'guest'
        assert hpux_collector.facts['virtualization_role'] == 'HP vPar'
        assert hpux_collector.facts['virtualization_tech_guest'] == set(['HP vPar'])
        assert hpux_collector.facts['virtualization_tech_host'] == set([])
    if os.path.exists('/opt/hpvm/bin/hpvminfo'):
        hpux_collector.get_virtual_facts()
        assert hpux_collector