

# Generated at 2022-06-13 03:59:32.330311
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts_object = HPUXVirtual(dict(), dict())
    assert virtual_facts_object.platform == 'HP-UX'

# Generated at 2022-06-13 03:59:40.432395
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from distutils.version import LooseVersion
    import ansible.module_utils.facts.virtual.hpux

    if LooseVersion(ansible.module_utils.facts.virtual.hpux.__version__) < LooseVersion('2.0'):
        return

    module = FakeModule()

    fake_vecheck_file = FakeFile()  # noqa: F841
    fake_hpvminfo_file = FakeFile(content='Running as HPVM guest')  # noqa: F841
    fake_parstatus_file = FakeFile()  # noqa: F841

    hpux_virtual = HPUXVirtual(module)
    virtual_facts = hpux_virtual.get_virtual_facts()
    assert virtual_facts['virtualization_tech_guest'] == {'HPVM IVM'}

# Generated at 2022-06-13 03:59:43.670449
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    v = HPUXVirtual()
    assert v.platform == 'HP-UX'
    assert v.virtualization_type == ''
    assert v.virtualization_role == ''

# Generated at 2022-06-13 03:59:52.680234
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():

    class TestModule(object):
        def __init__(self, **kwargs):
            self.params = kwargs

        def run_command(self, cmd):
            if re.match('.*vecheck.*', cmd):
                rc = 0
                out = "Running in a guest partition"
            elif re.match('.*hpvminfo.*', cmd):
                rc = 0
                out = "Running in a HPVM vPar"
            elif re.match('.*parstatus.*', cmd):
                rc = 1
                out = "No match"
            else:
                rc = 1
                out = "No match"
            return rc, out, ""

    class TestAnsibleModule(object):
        def __init__(self, params):
            self.params = params
            self.run_command = Test

# Generated at 2022-06-13 03:59:54.471625
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts = HPUXVirtual({})
    assert virtual_facts.platform == 'HP-UX'

# Generated at 2022-06-13 04:00:02.315604
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    HPUXVirtual._module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True)
    HPUXVirtual.get_virtual_facts()
    assert HPUXVirtual.facts['virtualization_type'] == 'guest'
    assert HPUXVirtual.facts['virtualization_role'] == 'HPVM'
    assert 'HPVM' in HPUXVirtual.facts['virtualization_tech_guest']
    assert 'HPVM IVM' not in HPUXVirtual.facts['virtualization_tech_guest']
    assert 'HPVM vPar' not in HPUXVirtual.facts['virtualization_tech_guest']
    assert 'HP nPar' not in HPUXVirtual.facts['virtualization_tech_guest']


# Generated at 2022-06-13 04:00:03.940639
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual(dict())
    assert hv.platform == 'HP-UX'

# Generated at 2022-06-13 04:00:10.370709
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module = DummyAnsibleModule()

    class ModuleUtils(object):

        def __init__(self):
            self.facts = {}

        def get_file_lines(self, filename):
            pass

        def get_platform(self):
            return 'HP-UX'

    class DummyFile(object):
        def __init__(self, content=None):
            self.content = content

        def read(self):
            return self.content

    class DummyOs(object):
        def __init__(self):
            self.path = DummyPath()
            self.os = None
            self.architecture = None

        def uname(self):
            return (self.os, None, None, None, self.architecture)


# Generated at 2022-06-13 04:00:14.440588
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts = HPUXVirtual('ansible.module_utils.facts.virtual.hpux.HPUXVirtual').populate()
    assert virtual_facts['virtualization_type'] == 'guest'
    assert virtual_facts['virtualization_role'] == 'HP vPar'

# Generated at 2022-06-13 04:00:17.718218
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    facts = dict()
    virtual = HPUXVirtual(module=None, facts=facts)
    assert virtual.platform == 'HP-UX'

# Generated at 2022-06-13 04:00:34.928424
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    # Create virtual object
    virtual = HPUXVirtual({})

    # Create facts object
    facts = {}
    # Create is_file_mock object for mocking isfile method of os.path module
    is_file_mock = True
    def side_effect(path):
        global is_file_mock
        if path == '/usr/sbin/vecheck':
            if is_file_mock:
                return True
            else:
                return False
        elif path == '/opt/hpvm/bin/hpvminfo':
            return True
        elif path == '/usr/sbin/parstatus':
            return True

    # Configure module_run_command mock object
    def side_effect(command):
        global is_file_mock

# Generated at 2022-06-13 04:00:36.540051
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    assert HPUXVirtual(dict(module=None)).platform == 'HP-UX'

# Generated at 2022-06-13 04:00:42.701793
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible_collections.misc.not_a_real_collection.plugins.module_utils.facts.virtual.hpu import HPUXVirtual
    from ansible.module_utils.facts.virtual.base import Virtual
    virtual = HPUXVirtual({})
    virtual.module = FakeAnsibleModule()
    virtual.command_exists = lambda x: True
    facts = virtual.get_virtual_facts()
    assert isinstance(facts, Virtual)
    assert facts.platform == 'HP-UX'
    assert facts.virtualization_type == 'guest'
    assert facts.virtualization_role.startswith('HP ')
    assert facts.virtualization_tech_guest == set(['HP ' + facts.virtualization_role])
    assert facts.virtualization_tech_host == set()



# Generated at 2022-06-13 04:00:50.404510
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    # Unit test is currently only available on a HP-UX,
    # so do not run it if running on another platform
    if os.name != 'posix':
        return
    import platform as p
    if p.system().lower() != 'hp-ux':
        return

    from ansible.module_utils.facts import Collector
    from ansible.module_utils._text import to_bytes

    class HPModule:
        def __init__(self):
            self.params = {}
            self.fail_json = lambda **kwargs: None

        def run_command(self, cmd):
            import subprocess
            p = subprocess.Popen(cmd,
                                 shell=True,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
            stdout, stderr

# Generated at 2022-06-13 04:01:01.007049
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():

    facts = dict()
    # Prepare the test fixture
    m = type('', (object,), {'run_command': lambda x: (0, '', '')})()
    # Prepare the parameters
    params = dict()
    params['ansible_facts'] = facts
    params['module'] = m
    hv = HPUXVirtual(params)
    # Execute method
    result = hv.get_virtual_facts()
    # Check the result
    assert result['virtualization_type'] == 'guest'
    assert result['virtualization_role'] == 'HP vPar'
    assert len(result['virtualization_tech_guest']) == 1
    assert result['virtualization_tech_guest'] == {'HP vPar'}
    assert len(result['virtualization_tech_host']) == 0

# Generated at 2022-06-13 04:01:03.518486
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    module = FakeAnsibleModule()
    virt_obj = HPUXVirtual(module)
    assert virt_obj.module == module
    assert virt_obj.platform == 'HP-UX'


# Generated at 2022-06-13 04:01:05.965304
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual = HPUXVirtual()
    assert virtual._platform == 'HP-UX'

# Generated at 2022-06-13 04:01:11.617832
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts = HPUXVirtual(dict())
    assert virtual_facts.platform == 'HP-UX'
    assert virtual_facts.get_virtual_facts() == {
        'virtualization_role': '',
        'virtualization_type': '',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set()
    }

# Generated at 2022-06-13 04:01:13.480178
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual = HPUXVirtual(dict())
    assert hpux_virtual.virtual_facts == {}


# Generated at 2022-06-13 04:01:15.905431
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual = HPUXVirtual(None)
    assert hpux_virtual.platform == "HP-UX"



# Generated at 2022-06-13 04:01:29.109012
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    inst = HPUXVirtual({})
    assert inst


# Generated at 2022-06-13 04:01:34.954343
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual = HPUXVirtual(dict())
    assert virtual
    assert virtual.get_virtual_facts() == dict(
        virtualization_type='guest',
        virtualization_role='HP vPar',
        virtualization_tech_host=set(),
        virtualization_tech_guest=set(['HP vPar'])
    )

# Generated at 2022-06-13 04:01:43.812209
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    # Mock out get_virtual_facts
    class MockHPUXVirtual(HPUXVirtual):
        def __init__(self, module):
            self.module = module
        def _run_command(self, command):
            pass

    # Set up the mocks
    class MockModule():
        def __init__(self):
            self.run_command_called = False
            self.run_command_value = ()
            self.run_command_return_value = False
        def run_command(self, command):
            self.run_command_called = True
            self.run_command_value = command
            return self.run_command_return_value
    mod = MockModule()

    # Test 1: HP vPar
    mod.run_command_return_value = (0, 'HP vPar', '')
   

# Generated at 2022-06-13 04:01:48.562689
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    """Unit test for method get_virtual_facts of class HPUXVirtual"""
    from ansible.module_utils import basic
    module = basic.AnsibleModule(argument_spec={})

    m = HPUXVirtual(module)
    m.get_virtual_facts()

# Generated at 2022-06-13 04:01:53.983055
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpu import HPUXVirtual
    module_mock = MockModule()
    hpux_virtual = HPUXVirtual(module_mock)
    hpux_virtual.module.run_command = mock_run_command
    virtual_facts = hpux_virtual.get_virtual_facts()

    assert virtual_facts['virtualization_type'] == 'guest'
    assert virtual_facts['virtualization_role'] == 'HPVM IVM'

# Generated at 2022-06-13 04:01:55.653369
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_obj = HPUXVirtual(dict())
    assert virtual_obj.platform == 'HP-UX'


# Generated at 2022-06-13 04:02:03.653762
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual = HPUXVirtual(None)
    assert virtual.virtualization_type is None
    assert virtual.virtualization_role is None
    assert virtual.virtualization_system is None
    assert virtual.virtualization_subsystem is None
    assert virtual.virtualization_hypervisor_version is None
    assert virtual.virtualization_product_name is None
    assert virtual.virtualization_product_version is None
    assert virtual.virtualization_product_serial is None
    assert virtual.virtualization_host_name is None
    assert virtual.virtualization_host_uuid is None
    assert virtual.virtualization_host_system is None
    assert virtual.virtualization_host_subsystem is None
    assert virtual.virtualization_host_product_name is None
    assert virtual.virtualization_host_product_version is None
    assert virtual.virtualization

# Generated at 2022-06-13 04:02:05.666521
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual = HPUXVirtual(dict())
    assert hpux_virtual.platform == 'HP-UX'


# Generated at 2022-06-13 04:02:09.757002
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    '''HPUXVirtual class constructor'''
    virtual_inst = HPUXVirtual({})
    assert virtual_inst.platform == 'HP-UX'

# Generated at 2022-06-13 04:02:16.967708
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    import tempfile
    import os

    # We need the path to the module.
    module_path = os.path.join(tempfile.gettempdir(), "ansible_test_file_for_HPUXVirtual")

    # Create a temporary module file for testing
    with open(module_path, "w") as temp_module:
        temp_module.write('')

    # make a temporary ansible.cfg file with the test module path in it
    ansible_cfg_path = os.path.join(tempfile.gettempdir(), 'ansible.cfg')
    with open(ansible_cfg_path, 'w') as temp_config:
        temp_config.write('[defaults]\n')
        temp_config.write('library = %s\n' % module_path)

    # set ANSIBLE_

# Generated at 2022-06-13 04:02:48.398360
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts = HPUXVirtual(dict())
    assert virtual_facts.platform == 'HP-UX'



# Generated at 2022-06-13 04:02:50.956807
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_hpux = HPUXVirtual(dict(module=dict()))
    assert virtual_hpux is not None
    assert virtual_hpux.platform == 'HP-UX'

# Generated at 2022-06-13 04:02:52.606436
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    module = None
    v = HPUXVirtual(module)
    assert v.platform == 'HP-UX'


# Generated at 2022-06-13 04:02:57.750236
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    ''' Test outcome of method get_virtual_facts of class HPUXVirtual '''
    # Setup test object
    class_HPUXVirtual = HPUXVirtual({})

    # Test get_virtual_facts method and check result
    result = class_HPUXVirtual.get_virtual_facts()
    print(result)

# Generated at 2022-06-13 04:03:04.441094
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    class ModuleStub:
        def run_command(self, command):
            if command == "/usr/sbin/vecheck":
                return (0, "", "")
            if command == "/opt/hpvm/bin/hpvminfo":
                return (0, "Running HPVM guest", "")
            if command == "/usr/sbin/parstatus":
                return (0, "", "")
            return (1, "", "")
    hpx_object = HPUXVirtual(ModuleStub())
    assert hpx_object.get_virtual_facts() == dict(
        virtualization_type='guest',
        virtualization_role='HPVM IVM',
        virtualization_tech_guest=set(['HPVM IVM']),
        virtualization_tech_host=set([])
    )

# Generated at 2022-06-13 04:03:13.374489
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    class MockModule:
        def run_command(self, cmd):
            if cmd == '/usr/sbin/vecheck':
                return (0, '', '')
            if cmd == '/opt/hpvm/bin/hpvminfo':
                return (0, 'Running under HPVM guest', '')
            if cmd == '/usr/sbin/parstatus':
                return (0, '', '')
            raise RuntimeError('unexpected invocation of run_command')
    import sys
    dummy_module = MockModule()
    sys.modules['ansible.module_utils.facts.virtual.base'] = sys.modules['ansible.module_utils.facts.virtual.hpux']

# Generated at 2022-06-13 04:03:14.930689
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    test_obj = HPUXVirtual()
    assert(test_obj.platform == 'HP-UX')

# Generated at 2022-06-13 04:03:17.010170
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual = HPUXVirtual(dict(module=None))
    assert hpux_virtual.platform == 'HP-UX'

# Generated at 2022-06-13 04:03:21.368111
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    module = type('module', (), {})()
    run_command = module.run_command = lambda cmd: (0, '', '')
    run_command.__module__ = 'h'
    h = HPUXVirtual(module)
    assert h.platform == 'HP-UX'


# Generated at 2022-06-13 04:03:23.386133
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    v1 = HPUXVirtual()
    assert v1.platform == 'HP-UX'


# Generated at 2022-06-13 04:04:32.308130
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module = AnsibleModule(argument_spec={})
    hpu = HPUXVirtual({}, module)
    expected_facts = {'virtualization_tech_guest': set(['HP nPar', 'HP vPar', 'HPVM', 'HPVM IVM', 'HPVM vPar']),
                      'virtualization_tech_host': set([]),
                      'virtualization_role': 'HPVM IVM',
                      'virtualization_type': 'guest'}
    hpu.module.run_command = Mock(return_value=(0, "Running HPVM guest", ""))
    hpu.module.run_command = Mock(return_value=(0, "Running HPVM vPar", ""))
    hpu.module.run_command = Mock(return_value=(0, "Running HPVM host", ""))
    hpu.module

# Generated at 2022-06-13 04:04:40.731513
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    import sys
    import tempfile

    tmpdir = tempfile.mkdtemp()
    orig_cwd = os.getcwd()
    os.chdir(tmpdir)

    module = sys.modules['ansible.module_utils.facts.virtual.hpux']
    virtual = module.HPUXVirtual(module)
    virtual_facts = virtual.get_virtual_facts()

    assert not os.path.exists('/usr/sbin/vecheck')
    assert not os.path.exists('/opt/hpvm/bin/hpvminfo')
    assert not os.path.exists('/usr/sbin/parstatus')

    with open('/usr/sbin/vecheck', 'w') as f:
        f.write("#!/bin/sh\necho 'Installed'")

# Generated at 2022-06-13 04:04:42.123353
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    HPUXVirtual()


# Generated at 2022-06-13 04:04:44.860111
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    import ansible.module_utils.facts.virtual.hpux.get_virtual_facts
    HPUXVirtual_obj = HPUXVirtual()
    result = HPUXVirtual_obj.get_virtual_facts()
    assert result['virtualization_type'] == 'guest'

# Generated at 2022-06-13 04:04:50.333721
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    ###########################################################################
    class ModuleMock(object):
        def __init__(self):
            self.params = {}
            self.return_value = None
        def run_command(self, *args, **kwargs):
            return ['', '', 0]

    class FactsCollectorMock(object):
        def __init__(self, module):
            self.module = module
            self.collector = {}
        def __getitem__(self, key):
            return self.collector[key]
        def __setitem__(self, key, value):
            self.collector[key] = value
        def __delitem__(self, key):
            del self.collector[key]

    ###########################################################################
    import pytest
    ###########################################################################
    hpu = HPUXVirtual

# Generated at 2022-06-13 04:04:58.511545
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    # Defining the arguments into a dictionary
    module_args = {'path': '/usr/sbin/vecheck', 'regex': r'^(.*)hp$'}

    # Creating an instance of class HPUXVirtual
    virtual_class = HPUXVirtual(module=None, module_args=module_args)
    # Printing the contents of the class
    print(virtual_class.get_virtual_facts())
    assert virtual_class.get_virtual_facts() == {'virtualization_type': 'guest', 'virtualization_role': 'HP vPar'}

# Generated at 2022-06-13 04:05:07.111094
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():

    class ModuleMock():
        def __init__(self):
            self.run_command_args = ()
            self.run_command_rcs = {}
            self.run_command_rcs[('/usr/sbin/vecheck',)] = 0
            self.run_command_rcs[('/opt/hpvm/bin/hpvminfo',)] = 0
            self.run_command_rcs[('/usr/sbin/parstatus',)] = 0

        def run_command(self, args):
            """Mock's module.run_command method.  Returns either a successful
            return code and result or a failed return code and an empty result
            depending on the arg passed to module.run_command."""
            rc = self.run_command_rcs[args]
            return (rc, '', '')



# Generated at 2022-06-13 04:05:10.661645
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual_obj = HPUXVirtual(dict(module='AnsibleModule'))
    assert hpux_virtual_obj.platform == 'HP-UX'
    assert hpux_virtual_obj.get_virtual_facts() == {}

# Generated at 2022-06-13 04:05:13.700016
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    '''
    Unit test case that checks the get_virtual_facts()
    method of HPUXVirtual.
    '''
    virtual = HPUXVirtual()
    virtual_facts = virtual.get_virtual_facts()
    print(virtual_facts)

# Generated at 2022-06-13 04:05:15.432924
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    assert HPUXVirtual.platform == 'HP-UX'
    assert HPUXVirtual.get_virtual_facts() == {}

# Generated at 2022-06-13 04:05:57.362685
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    facts = HPUXVirtual({}).get_virtual_facts()
    assert facts['virtualization_tech_guest'] == set()
    assert facts['virtualization_tech_host'] == set()
    assert facts['virtualization_type'] == 'guest'
    assert facts['virtualization_role'] == 'HP vPar'



# Generated at 2022-06-13 04:06:06.074729
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    # Define the expected results
    expected_virtual_facts = {
        "virtualization_type": 'guest',
        "virtualization_role": 'HP vPar',
        "virtualization_tech_guest": set(['HP vPar']),
        "virtualization_tech_host": set([])
    }
    # Initialize virtualization modules
    hpux_virtual = HPUXVirtual({})
    # Get virtual facts and compare to expected
    virtual_facts = hpux_virtual.get_virtual_facts()
    assert virtual_facts == expected_virtual_facts

# Generated at 2022-06-13 04:06:07.504715
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual = HPUXVirtual(None)
    assert virtual.platform == 'HP-UX'



# Generated at 2022-06-13 04:06:10.421899
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts = HPUXVirtual({})
    assert virtual_facts.platform == 'HP-UX'

# Generated at 2022-06-13 04:06:14.282212
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    class FakeModule(object):
        def run_command(self, cmd):
            if cmd == '/usr/sbin/vecheck':
                return 0, '', ''
            elif cmd == '/opt/hpvm/bin/hpvminfo':
                return 0, 'Running HPVM vPar technology', ''
            elif cmd == '/usr/sbin/parstatus':
                return 0, '', ''
            else:
                return False, '', ''
    fake_module = FakeModule()
    p = HPUXVirtual(fake_module)
    vf = p.get_virtual_facts()
    assert 'virtualization_type' in vf.keys()
    assert 'virtualization_role' in vf.keys()
    assert 'virtualization_tech_guest' in vf.keys()

# Generated at 2022-06-13 04:06:25.013647
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    class TestModule():
        def __init__(self):
            self.run_command = ''
        def run_command(self, cmd, check_rc=False):
            if self.run_command == 'vecheck':
                return (0, 'test_output', '')
            elif self.run_command == 'hpvminfo':
                return (0, 'Running HPVM guest', '')
            elif self.run_command == 'parstatus':
                return (0, 'test_output', '')
            else:
                return (127, '', '')

    class TestFactCollector(HPUXVirtual):
        def __init__(self, module):
            self.module = module

    module = TestModule()

    def expected_result(run_command):
        module.run_command = run_command
       

# Generated at 2022-06-13 04:06:35.884956
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    """ Unit test for method get_virtual_facts of class HPUXVirtual """

    h = HPUXVirtual()

    # Mock some of the get_virtual_facts dependencies
    h.module = type('MockModule', (), dict(run_command=mock_run_command))
    h.module.run_command.return_value = mock_run_command_return_value

    # Mock those dependencies that don't change in the course of the test
    h.uname = mock_uname

    # Run get_virtual_facts
    virtual_facts = h.get_virtual_facts()

    # Assert the expected results match the actual results
    assert virtual_facts['virtualization_tech_guest'] == {'HPVM'}
    assert virtual_facts['virtualization_tech_host'] == set()

# Generated at 2022-06-13 04:06:37.788859
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual = HPUXVirtual()
    assert virtual
    assert virtual.guest_tech() == set()
    assert virtual.host_tech() == set()


# Generated at 2022-06-13 04:06:42.730579
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module = AnsibleModule(argument_spec={})
    module.run_command = Mock()
    module.run_command.return_value = (0, 'Sample text for testing.', '')

    hpux_virtual_collector = HPUXVirtual(module)
    virtual_facts = hpux_virtual_collector.get_virtual_facts()
    assert virtual_facts.get('virtualization_type') == 'guest'


# Generated at 2022-06-13 04:06:45.028315
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux = HPUXVirtual({})
    assert hpux.platform == 'HP-UX'

# Generated at 2022-06-13 04:08:50.351363
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual = HPUXVirtual({})
    assert virtual.__class__.__name__ == 'HPUXVirtual'


# Generated at 2022-06-13 04:08:51.965329
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    v = HPUXVirtual({})
    assert v.platform == 'HP-UX'

# Generated at 2022-06-13 04:08:52.904893
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_obj = HPUXVirtual()
    assert virtual_obj.platform == 'HP-UX'

# Generated at 2022-06-13 04:08:53.800818
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    assert issubclass(HPUXVirtual, Virtual)

# Generated at 2022-06-13 04:08:56.807988
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual
    x = HPUXVirtual()
    assert x.platform == 'HP-UX'

# Generated at 2022-06-13 04:08:59.296774
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    v = HPUXVirtual()
    assert v.platform == "HP-UX"
    assert v.get_virtual_facts() == {'virtualization_tech_host': set(), 'virtualization_tech_guest': set()}


# Generated at 2022-06-13 04:09:02.239241
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual = HPUXVirtual()
    assert hpux_virtual.platform == 'HP-UX'


# Generated at 2022-06-13 04:09:04.177503
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual_info = HPUXVirtual(dict(module=dict()))
    assert hpux_virtual_info


# Generated at 2022-06-13 04:09:06.471913
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    test_object = HPUXVirtual(dict())
    assert test_object.platform == 'HP-UX'
    assert test_object.virtual_facts == {}


# Generated at 2022-06-13 04:09:10.678062
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual()
    assert hv.platform == 'HP-UX'
    assert hv.virtualization_tech_guest == set()
    assert hv.virtualization_tech_host == set()
    assert hv.virtualization_type is None
    assert hv.virtualization_role is None