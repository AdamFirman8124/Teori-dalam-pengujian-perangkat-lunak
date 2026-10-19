

# Generated at 2022-06-13 03:59:34.118461
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual()
    assert hv.platform == 'HP-UX'
    assert hv.virtualization_type == ''
    assert hv.virtualization_role == ''
    assert hv.virtualization_tech_host == set([])
    assert hv.virtualization_tech_guest == set([])



# Generated at 2022-06-13 03:59:41.605287
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    m = HPUXVirtual(dict(module=None))
    m.module.run_command = run_command

    # Test vPar
    m.os_version = 'B.11.31'
    assert m.get_virtual_facts() == {'virtualization_type': 'guest',
                                     'virtualization_tech_host': set(),
                                     'virtualization_role': 'HP vPar',
                                     'virtualization_tech_guest': {'HP vPar'}}

    # Test nPar
    m.os_version = 'B.11.31'

# Generated at 2022-06-13 03:59:43.774482
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hp_virtual = HPUXVirtual({})
    assert hp_virtual


# Generated at 2022-06-13 03:59:52.785752
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    class HPUXVirtual_get_virtual_facts():
        def __init__(self):
            self.exit_args = None
            self.exit_kwargs = None

        def exit_json(self, *args, **kwargs):
            self.exit_args = args
            self.exit_kwargs = kwargs

        def fail_json(self, *args, **kwargs):
            self.exit_args = args
            self.exit_kwargs = kwargs

        def run_command(self, cmd):
            return os.system('/usr/bin/printf "Running HPVM guest\n"')

    tmp_HPUXVirtual = HPUXVirtual()
    tmp_HPUXVirtual.module = HPUXVirtual_get_virtual_facts()
    tmp_HPUXVirtual.get_virtual_facts()

# Generated at 2022-06-13 03:59:54.196081
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_ins = HPUXVirtual()
    assert virtual_ins.platform == 'HP-UX'

# Generated at 2022-06-13 03:59:55.964880
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    node = HPUXVirtual({'module': None, 'fail_on_error': False})
    assert node.platform == 'HP-UX'


# Generated at 2022-06-13 04:00:03.439520
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual import HPUXVirtual
    from ansible.module_utils.facts.virtual.hpux import VirtualCollector
    from ansible.module_utils._text import to_bytes

    class ModuleMock(object):
        def __init__(self):
            self.params = {'gather_subset': '!all'}
            self.run_command = self.mock_run_command

        def mock_run_command(self, cmd):
            if 'vecheck' in cmd:
                return 0, to_bytes('*** Running HP vPar ***'), None
            elif 'hpvminfo' in cmd:
                return 0, to_bytes('*** Running HPVM host ***'), None

# Generated at 2022-06-13 04:00:05.309272
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts = HPUXVirtual({'module_setup': True}, {})
    assert virtual_facts.platform == 'HP-UX'

# Generated at 2022-06-13 04:00:07.273761
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    assert HPUXVirtual({}).get_virtual_facts() == {'virtualization_tech_guest': set(),
                                                   'virtualization_tech_host': set()}

# Generated at 2022-06-13 04:00:11.665124
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts = HPUXVirtual(dict())
    assert virtual_facts.platform == 'HP-UX'


# Unit tests for get_virtual_facts

# Generated at 2022-06-13 04:00:24.424527
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual()
    assert hv.__class__.__name__ == 'HPUXVirtual'
    assert hv.platform == 'HP-UX'


# Generated at 2022-06-13 04:00:26.766251
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts = HPUXVirtual()
    assert (virtual_facts.platform == 'HP-UX')


# Generated at 2022-06-13 04:00:31.092302
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    '''
    Unit test for constructor of class HPUXVirtual
    '''
    # Test facts
    test_facts = {'virtualization_type': 'guest',
                 'virtualization_role': 'HP vPar'}
    test_obj = HPUXVirtual(module=None)
    assert test_obj
    for key in test_facts:
        assert test_facts[key] == test_obj.facts[key]

# Generated at 2022-06-13 04:00:34.177938
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    from ansible.module_utils.facts.virtual import HPUXVirtual
    # Create an object of HPUXVirtual
    hpux_virtual_obj = HPUXVirtual(dict())
    # Assert that the platform variable is set to 'HP-UX'
    assert hpux_virtual_obj.platform == 'HP-UX'

# Generated at 2022-06-13 04:00:39.089087
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    # Create a module mock
    module = {}
    module['run_command'] = lambda x: (0, '', '')
    module['user_module_data_vardir'] = lambda x: ''

    virtual_facts = HPUXVirtual(module).get_virtual_facts()

    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts

# Generated at 2022-06-13 04:00:41.817292
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts = HPUXVirtual('dummy_module')
    assert virtual_facts.platform == 'HP-UX'
    assert virtual_facts._fact_class == HPUXVirtual

# Generated at 2022-06-13 04:00:44.157425
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual = HPUXVirtual(dict())
    assert hpux_virtual.platform == 'HP-UX'


# Generated at 2022-06-13 04:00:51.008193
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    class MockModule(object):
        def __init__(self):
            self.run_command_count = 0

        def run_command(self, cmd):
            if cmd == '/usr/sbin/vecheck':
                if self.run_command_count == 0:
                    self.run_command_count += 1
                    return 0, '', ''
                elif self.run_command_count == 1:
                    self.run_command_count += 1
                    return 0, '', ''
                elif self.run_command_count == 2:
                    self.run_command_count += 1
                    return 1, '', ''
            elif cmd == '/opt/hpvm/bin/hpvminfo':
                if self.run_command_count == 3:
                    self.run_command_count += 1

# Generated at 2022-06-13 04:00:52.437888
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts = HPUXVirtual()
    assert virtual_facts.platform == 'HP-UX'

# Generated at 2022-06-13 04:01:03.217801
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpu_x import HPUXVirtual
    from ansible.module_utils.facts.virtual.utils import AnsibleModuleMock

    # Mocking AnsibleModule class
    module = AnsibleModuleMock
    hpu_x_virtual = HPUXVirtual(module)
    virtual_facts = hpu_x_virtual.get_virtual_facts()

    # Expected output
    guest_tech = set(['HP nPar', 'HP vPar', 'HPVM vPar', 'HPVM IVM'])
    virtual_facts_expected = {'virtualization_role': 'HP nPar',
                              'virtualization_type': 'guest',
                              'virtualization_tech_guest': guest_tech
                             }
    assert virtual_facts == virtual_facts_expected



# Generated at 2022-06-13 04:01:28.750574
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual()
    assert hv.platform == 'HP-UX'

# Generated at 2022-06-13 04:01:30.453563
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hp_virtual_instance = HPUXVirtual({})
    assert hp_virtual_instance.platform == 'HP-UX'

# Generated at 2022-06-13 04:01:37.123486
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    c = HPUXVirtual({'module_setup': True}, 'ansible.module_utils.facts.virtual.hpux')
    # Set the effective user to root
    c.module.params['effective_user'] = 'root'
    facts = c.get_virtual_facts()
    assert facts == {
        'virtualization_type': 'guest',
        'virtualization_role': 'HPVM'
    }

# Generated at 2022-06-13 04:01:38.934683
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual()
    assert hv.platform == "HP-UX"


# Generated at 2022-06-13 04:01:40.410870
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual = HPUXVirtual()
    assert hpux_virtual.platform == 'HP-UX'

# Generated at 2022-06-13 04:01:42.979672
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():

    # Check for dictionary returned by constructor of HPUXVirtual class
    virtual_facts = HPUXVirtual({})
    assert isinstance(virtual_facts.get_virtual_facts(), dict)



# Generated at 2022-06-13 04:01:45.399553
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hvfacts = HPUXVirtual({})
    assert hvfacts.platform == 'HP-UX'
    assert len(hvfacts.get_virtual_facts()) == 4

# Generated at 2022-06-13 04:01:55.234522
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    class MockModule(object):
        def run_command(self, command):
            if command == '/usr/sbin/vecheck':
                return 0, "some output", ""
            elif command == '/opt/hpvm/bin/hpvminfo':
                return 0, "Running HPVM guest", ""
            elif command == '/usr/sbin/parstatus':
                return 0, "some output", ""

    class MockPopen2(object):
        def __init__(self, command):
            pass

    mock_module = MockModule()
    h = HPUXVirtual(mock_module)
    h._Popen2 = MockPopen2
    virtual_facts = h.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'guest'

# Generated at 2022-06-13 04:02:00.018328
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    """
    Test get_virtual_facts method of HPUXVirtual class
    """
    from ansible.module_utils.facts.virtual import HPUXVirtual
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.pycompat24 import get_exception
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts.collector import BaseFactCollector
    import sys

    class AnsibleModuleMock(AnsibleModule):
        def __init__(self, *args, **kwargs):
            self.params = {}
            self.params['gather_subset'] = ['all']
            self.params['gather_timeout'] = 1
            self.facts = {}
            self.exit_args = {}
            self.exit_args

# Generated at 2022-06-13 04:02:04.665570
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.virtual.hpux import virtual_facts_default_values
    from ansible.module_utils.facts.virtual.hpux import virtual_facts_result_values

    vm_hpvm = HPUXVirtual({'module': FakeModule()})
    vm_hpvm.os_release_content = to_bytes(virtual_facts_default_values['os_release_content'])
    vm_hpvm.os_release_content = to_bytes(virtual_facts_default_values['os_release_content'])
    vm_hpvm.uname_result = to_bytes(virtual_facts_default_values['uname_result'])
    vm_hpvm.module.run_command = run_command
    virtual_facts = vm_

# Generated at 2022-06-13 04:02:31.756223
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpu import HPUXVirtual
    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )
    obj = HPUXVirtual(module)
    data = obj.get_virtual_facts()
    assert type(data) is dict

# Generated at 2022-06-13 04:02:39.055141
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    import sys
    import imp
    import shutil
    import tempfile
    import ansible.module_utils.facts.virtual.hpuxtopar as hpuxtopar
    from ansible.module_utils.facts.virtual.hpuxtopar import HPUXVirtual

    # Method to create a temporary file
    def _create_file(path, content):
        f = open(path, 'w')
        f.write(content)
        f.close()
        return path

    # Create a temporary directory
    tmpdir = tempfile.mkdtemp()

    # Create a temporary module to mock AnsibleModule
    # sys.modules['ansible.module_utils.basic'] = imp.new_module('ansible.module_utils.basic')
    # sys.modules['ansible.module_utils.basic'].Ansible

# Generated at 2022-06-13 04:02:42.589915
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    facts = HPUXVirtual({}).get_virtual_facts()
    assert type(facts) is dict
    assert 'virtualization_type' in facts
    assert 'virtualization_role' in facts
    assert 'virtualization_tech_guest' in facts
    assert 'virtualization_tech_host' in facts
    assert facts['virtualization_tech_guest'] == set()
    assert facts['virtualization_tech_host'] == set()


# Generated at 2022-06-13 04:02:45.336103
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    test_obj = HPUXVirtual({}, {})
    assert test_obj.platform == 'HP-UX'

# Generated at 2022-06-13 04:02:48.837535
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual = HPUXVirtual({'module_setup': True}, None)
    assert hpux_virtual.get_virtual_facts() == {'virtualization_tech_host': set(), 'virtualization_tech_guest': set()}


# Generated at 2022-06-13 04:02:51.140604
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module = AnsibleModule(argument_spec={})
    hpuxvirtual = HPUXVirtual(module)
    hpuxvirtual.get_virtual_facts()

# Generated at 2022-06-13 04:02:52.571948
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hp_virtual = HPUXVirtual({})
    assert hp_virtual.platform == 'HP-UX'

# Generated at 2022-06-13 04:02:53.606956
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual()
    assert 'HP-UX' == hv.platform

# Generated at 2022-06-13 04:02:56.341079
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts = HPUXVirtual()
    assert virtual_facts.platform == 'HP-UX'

# Generated at 2022-06-13 04:02:58.213085
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts = HPUXVirtual(dict(module=dict()))
    assert virtual_facts

# Generated at 2022-06-13 04:03:58.967863
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    class TestHPUXVirtual(HPUXVirtual):

        def __init__(self, module):
            self.module = module
            self.file_exists_outcome = {}
            self.file_exists_outcome['/usr/sbin/parstatus'] = True
            self.file_exists_outcome['/opt/hpvm/bin/hpvminfo'] = True
            self.file_exists_outcome['/usr/sbin/vecheck'] = True
            self.cmd_outcome = {}
            self.cmd_outcome['/usr/sbin/parstatus'] = (0, '', '')
            self.cmd_outcome['/opt/hpvm/bin/hpvminfo'] = (0, 'Running HPVM guest', '')

# Generated at 2022-06-13 04:04:06.486655
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    class DummyModule(object):
        pass

    class DummyModuleClass(object):
        def run_command(self, cmd, *args):
            if cmd == '/usr/sbin/vecheck':
                return 0, 'Running\n', None
            elif cmd == '/opt/hpvm/bin/hpvminfo':
                return 0, 'Running HPVM guest\n', None
            elif cmd == '/usr/sbin/parstatus':
                return 0, 'Running\n', None

    mymodule = DummyModule()
    mymodule.run_command = DummyModuleClass().run_command


# Generated at 2022-06-13 04:04:07.824956
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hypervisor = HPUXVirtual(dict())
    assert hypervisor.platform == 'HP-UX'

# Generated at 2022-06-13 04:04:09.439792
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual_obj = HPUXVirtual()

    # Test for platform attribute
    assert hpux_virtual_obj.platform == 'HP-UX'


# Generated at 2022-06-13 04:04:11.906129
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual()
    assert hv.__class__.__name__ == 'HPUXVirtual'

# Generated at 2022-06-13 04:04:16.972386
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts = HPUXVirtual(None).populate()
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts
    assert 'HP vPar' in virtual_facts['virtualization_tech_guest']
    assert 'HPVM vPar' in virtual_facts['virtualization_tech_guest']
    assert 'HPVM IVM' in virtual_facts['virtualization_tech_guest']
    assert 'HPVM' in virtual_facts['virtualization_tech_guest']
    assert 'HP nPar' in virtual_facts['virtualization_tech_guest']

# Generated at 2022-06-13 04:04:24.167841
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils import basic
    from ansible.module_utils.facts import ansible_collection_ignore_dirs

    m_run_command = basic.AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    m = HPUXVirtual(m_run_command)

    # Testing set() of empty
    test_get_virtual_facts = m.get_virtual_facts()
    assert (test_get_virtual_facts == {'virtualization_type': None,
                                       'virtualization_role': None,
                                       'virtualization_tech_host': set(),
                                       'virtualization_tech_guest': set()
                                       })

    # Testing set() of multiple

# Generated at 2022-06-13 04:04:25.185887
# Unit test for method get_virtual_facts of class HPUXVirtual

# Generated at 2022-06-13 04:04:27.380918
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual(dict())
    assert hv is not None

# Generated at 2022-06-13 04:04:33.784106
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes

    module_mock = basic.AnsibleModule(
        argument_spec=dict()
    )
    raw_dict = {
        'virtualization_tech_host': set(),
        'virtualization_tech_guest': {'HPVM', 'HP nPar'},
        'virtualization_role': 'HP nPar',
        'virtualization_type': 'guest'
    }
    raw_dict_2 = {
        'virtualization_tech_host': set(),
        'virtualization_tech_guest': {'HPVM vPar'},
        'virtualization_role': 'HPVM vPar',
        'virtualization_type': 'guest'
    }

# Generated at 2022-06-13 04:05:23.824811
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module = FakeAnsibleModule()
    test_obj = HPUXVirtual(module)
    test_obj.get_virtual_facts()
    assert 'virtualization_type' in module.exit_json
    assert 'virtualization_role' in module.exit_json
    assert 'virtualization_tech_guest' in module.exit_json

# Generated at 2022-06-13 04:05:26.546842
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual
    virtual_machine = HPUXVirtual()
    virtual_machine.module = AnsibleModule(argument_spec={})
    assert virtual_machine.get_virtual_facts() == {
        'virtualization_type': 'guest',
        'virtualization_role': 'HP vPar'
    }

# Generated at 2022-06-13 04:05:31.867341
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    module = FakeModule()
    virt_facts = HPUXVirtualCollector.collect(module)
    assert len(virt_facts['virtualization_tech_guest']) >= 1
    assert len(virt_facts['virtualization_tech_host']) == 0
    assert virt_facts['virtualization_type'] == 'guest'
    assert virt_facts['virtualization_role'] == 'HP nPar'

# Mocked AnsibleModule for testing the HP-UX specific subclass of Virtual

# Generated at 2022-06-13 04:05:34.821492
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    test_module = HPUXVirtual()
    assert test_module.platform == 'HP-UX', "Incorrect platform, expected HP-UX"

# Generated at 2022-06-13 04:05:37.020840
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual = HPUXVirtual({"module": None})
    assert virtual.platform == 'HP-UX'
    assert virtual.get_virtual_facts() == {}

# Generated at 2022-06-13 04:05:45.797487
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    # Test data for get_virtual_facts method
    test_data = dict(
        # Input data
        rc=dict(
            stdout=dict(
                vecheck='',
                hpvminfo='',
                parstatus='',
            )
        ),
        # Test data
        test=dict(
            result=dict(
                virtualization_type=None,
                virtualization_role=None,
                virtualization_tech_guest=set(),
                virtualization_tech_host=set(),
            ),
        )
    )

    # Prepare mock for module test
    module = MagicMock()

# Generated at 2022-06-13 04:05:48.997994
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    # TODO: Add tests for the following attributes when we have a proper test setup with docker available
    # virtualization_type = None
    # virtualization_role = None
    # virtualization_tech_guest = []
    # virtualization_tech_host = []
    vp = HPUXVirtual(dict(module=dict()))
    assert vp is not None

# Generated at 2022-06-13 04:05:56.792638
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    virtual_facts_expected = {
        'virtualization_type': 'guest',
        'virtualization_role': 'HPVM vPar',
        'virtualization_tech_guest': set(['HPVM vPar']),
        'virtualization_tech_host': set(),
    }
    module = FakeModule({
        '/usr/sbin/vecheck': '',
        '/opt/hpvm/bin/hpvminfo': 'Running on HPVM vPar',
    })
    virtual = HPUXVirtual(module)
    facts = virtual.get_facts()
    assert facts['virtualization_type'] == virtual_facts_expected['virtualization_type']
    assert facts['virtualization_role'] == virtual_facts_expected['virtualization_role']
    assert facts['virtualization_tech_guest'] == virtual_facts_expected

# Generated at 2022-06-13 04:06:07.723237
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    """
    HPUXVirtual.get_virtual_facts() Test
    """

    # Constructor is tested in the test_hpux_virtual_collector
    hpux_virtual = HPUXVirtual({})

    # Test get_virtual_facts method when the virtualization type is HP vPar
    hpux_virtual.module.run_command = lambda x: (0, 'HPVM vPar', '')
    hpux_virtual.os.path.exists = lambda x: True
    virtual_facts = hpux_virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'guest'
    assert virtual_facts['virtualization_role'] == 'HPVM vPar'
    assert virtual_facts['virtualization_tech_guest'] == {'HPVM vPar'}

# Generated at 2022-06-13 04:06:19.386666
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    """ Unit test for method get_virtual_facts of class HPUXVirtual """
    required_facts = {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_tech_guest': '',
        'virtualization_tech_host': ''
    }

    host_virtual_facts = {
        'virtualization_type': 'host',
        'virtualization_role': 'HPVM',
        'virtualization_tech_guest': set([]),
        'virtualization_tech_host': set(['HPVM'])
    }


# Generated at 2022-06-13 04:08:30.194047
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils import basic
    module = basic.AnsibleModule(
        argument_spec = dict()
    )
    hpuxvirtual = HPUXVirtual(module)
    res = hpuxvirtual.get_virtual_facts()
    if 'HP vPar' in res['virtualization_tech_guest']:
        assert res['virtualization_type'] == 'guest'
        assert res['virtualization_role'] == 'HP vPar'
    elif 'HPVM vPar' in res['virtualization_tech_guest']:
        assert res['virtualization_type'] == 'guest'
        assert res['virtualization_role'] == 'HPVM vPar'

# Generated at 2022-06-13 04:08:38.638004
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts import Facts
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual
    import ansible.module_utils.facts.virtual.hpux as hpux

    hpux.os = mock_module('os')
    hpux.os.path.exists = lambda x: x == '/usr/sbin/vecheck'
    hpux.os.path.isfile = lambda x: x == '/usr/sbin/parstatus'
    hpux.HPUXVirtual.module = hpux.AnsibleModule({})
    hpux.HPUXVirtual.module.run_command = lambda x: (0, '', '')

    facts = Facts(HPUXVirtual, {}, lambda x, y: None).populate()

# Generated at 2022-06-13 04:08:40.474271
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual()
    assert hv.platform == 'HP-UX'

# Generated at 2022-06-13 04:08:41.694751
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    test_class = HPUXVirtual()
    assert test_class.platform == 'HP-UX'


# Generated at 2022-06-13 04:08:52.105866
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    """
    Unit test for method get_virtual_facts of class HPUXVirtual.
    """
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual
    from ansible.module_utils.six import StringIO
    from ansible.module_utils.ansible_release import __version__

    instances = list()
    # Case 1: when rc=0 and out matches regex.
    arg1 = StringIO("""Running HPVM vPar""")
    arg2 = StringIO("")
    arg3 = 0
    res = HPUXVirtual.get_virtual_facts(arg1, arg2, arg3)

# Generated at 2022-06-13 04:08:53.487946
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual = HPUXVirtual(dict())
    assert virtual.platform == 'HP-UX'
    assert virtual.guest_tech == set()
    assert virtual.host_tech == set()


# Generated at 2022-06-13 04:08:57.541183
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virt_obj = HPUXVirtual()
    assert virt_obj.virtualization_type is None
    assert virt_obj.virtualization_role is None
    assert virt_obj.virtualization_tech_host == set()
    assert virt_obj.virtualization_tech_guest == set()

# Generated at 2022-06-13 04:08:59.982448
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual = HPUXVirtual(dict())
    assert isinstance(virtual, HPUXVirtual)
    assert virtual.platform == 'HP-UX'
    assert hasattr(virtual, 'get_virtual_facts')


# Generated at 2022-06-13 04:09:02.507127
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual = HPUXVirtual(None)
    assert hpux_virtual.platform == 'HP-UX'


# Generated at 2022-06-13 04:09:09.539804
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual
    from ansible.module_utils.facts import FactModule
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtualCollector
    from ansible.module_utils.facts.collector import BaseFactCollector

    class AnsibleModuleFake(object):
        def __init__(self):
            self.params = {}
            self.params['gather_subset'] = ['!all', 'virtual']
            self.run_command_calls = []
            self.run_command_rcs = []
            self.run_command_exceptions = []

        def run_command(self, command):
            self.run_command_calls.append(command)
            (rc, out, err) = self.run_command