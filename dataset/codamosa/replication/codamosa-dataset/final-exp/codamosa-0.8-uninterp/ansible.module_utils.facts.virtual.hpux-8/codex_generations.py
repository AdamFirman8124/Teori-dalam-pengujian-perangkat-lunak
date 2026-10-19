

# Generated at 2022-06-13 03:59:38.887203
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    import json
    import sys
    import tempfile
    import textwrap
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.virtual.hpx import HPUXVirtual

    MODULE_ARGS = {}
    module = basic.AnsibleModule(argument_spec=MODULE_ARGS)
    setattr(module, 'run_command', lambda *args, **kwargs: (0, 'out', 'err'))

    if sys.version_info[0] < 3:
        py_version = 'python2'
    else:
        py_version = 'python3'
    temp_dir = tempfile.mkdtemp(prefix='ansible_test_' + py_version)

# Generated at 2022-06-13 03:59:44.151388
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpux.hpux import HPUXVirtual
    from ansible.module_utils.facts.virtual import VirtualCollector
    import tempfile
    import os

    v = HPUXVirtual()

    # case 1: /usr/sbin/vecheck, /opt/hpvm/bin/hpvminfo and /usr/sbin/parstatus don't exist
    fd1, temp1 = tempfile.mkstemp()
    os.close(fd1)
    fd2, temp2 = tempfile.mkstemp()
    os.close(fd2)
    fd3, temp3 = tempfile.mkstemp()
    os.close(fd3)
    v.os = {'path': {'exists': [temp1, temp2, temp3]}}


# Generated at 2022-06-13 03:59:47.353131
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual({})
    hv.collect()
    assert hv.data.get('virtualization_tech_guest') is not None
    assert hv.data.get('virtualization_tech_host') is not None

# Generated at 2022-06-13 03:59:55.642242
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    """
    Test module for method get_virtual_facts of class HPUXVirtual
    """

    # Initialize the class object
    virtual_obj = HPUXVirtual()

    # Set os.path.exists side_effect
    side_effect_dict = {
        '/usr/sbin/vecheck': True,
        '/opt/hpvm/bin/hpvminfo': True,
        '/usr/sbin/parstatus': True
    }
    virtual_obj.module.os.path.exists.side_effect = lambda x: side_effect_dict.get(x, False)

    # Set ansible module run_command return values

# Generated at 2022-06-13 04:00:01.993310
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpux.test_import_module import TestImportModule
    from ansible.module_utils.facts.virtual.hpux.test_common import TestCommon
    from ansible.module_utils.facts.virtual.hpux.test_get_virtual_facts import TestGetVirtualFacts
    module = TestImportModule()
    common = TestCommon()
    get_virtual_facts = TestGetVirtualFacts()
    obj = HPUXVirtual(module)
    obj._common = common
    obj._get_virtual_facts = get_virtual_facts
    obj.get_virtual_facts()

# Generated at 2022-06-13 04:00:03.938629
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv_facts = HPUXVirtual(dict())
    assert hv_facts.platform == 'HP-UX'


# Generated at 2022-06-13 04:00:08.966047
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpuxVirtual = HPUXVirtual()
    assert hpuxVirtual.platform == 'HP-UX'
    assert hpuxVirtual.virtualization_tech_guest == set()
    assert hpuxVirtual.virtualization_tech_host == set()
    assert hpuxVirtual.virtualization_role == ""
    assert hpuxVirtual.virtualization_type == ""

# Generated at 2022-06-13 04:00:18.518023
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.collector.virtual import HPUXVirtual

    vecheck_out = """
    /opt/Ignite/bin/vecheck[20]: 0653-503 Cannot find the file /stand/vmunix
    The virtualization environment is HP-UX virtual partition.
    The virtualization path is /dev/hpvm/ve0
    """
    hpvminfo_out = "Running HPVM guest on HPVM host"
    parstatus_out = "Running HP-UX nPartition"
    mock_module = MockModule()
    mock_module.run_command = Mock(return_value=(0, vecheck_out, ""))
    hpux_virtual = HPUXVirtual(mock_module)
    facts = hpux_virtual.get_virtual_facts()
    assert facts['virtualization_type']

# Generated at 2022-06-13 04:00:22.738553
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    # Call the constructor
    hpux_virtual = HPUXVirtual()

    # Check if virtualization_type is correctly initialized
    assert hpux_virtual.virtualization_type == 'HP-UX'

    # Check if virtualization_role is correctly initialized
    assert hpux_virtual.virtualization_role == 'HP-UX'



# Generated at 2022-06-13 04:00:23.447525
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    assert Virtual


# Generated at 2022-06-13 04:00:37.366370
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module = AnsibleModuleMock()
    module.run_command.return_value = (0, "Running as HPVM vPar", '')
    virtual = HPUXVirtual(module)
    virtual_facts = virtual.get_virtual_facts()
    assert virtual_facts["virtualization_type"] == "guest"
    assert virtual_facts["virtualization_role"] == "HPVM vPar"

# Generated at 2022-06-13 04:00:41.662404
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    ''' Unit test for testing method get_virtual_facts of class HPUXVirtual
    '''
    from sys import version_info
    from ansible.module_utils.facts.virtual.hpuxvirtual import HPUXVirtual
    from ansible.module_utils.facts import ModuleStub
    from os import listdir
    from os.path import isdir, exists
    from tempfile import gettempdir

    # The HPUXVirtual object to test
    hv = HPUXVirtual(ModuleStub())

    # Stub for os.path.exists. The stub is used for all tests

# Generated at 2022-06-13 04:00:46.556101
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    """
    Class HPUXVirtual should initialize virtual_facts dictionary and
    set some of it's elements.
    """
    from ansible.module_utils.facts.virtual.default import DefaultVirtual
    from ansible.module_utils.facts.virtual.hpxs import HPUXVirtual

    # Create instance of HPUXVirtual, same as HPUXVirtual()
    hpux_virtual_module = HPUXVirtual()

    # Create dictionary, same as hpux_virtual_module.virtual_facts
    hpux_virtual_dict = {'virtualization_type': '',
                         'virtualization_role': '',
                         'virtualization_tech_guest': set(),
                         'virtualization_tech_host': set()}

    # Create instance of DefaultVirtual and copy it's property virtual_facts
    default_virtual_module = DefaultVirtual()

# Generated at 2022-06-13 04:00:49.344243
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    """
    (unit_tests.unit.module_utils.virtual.HPUX)
    Test HPUXVirtual
    """
    v = HPUXVirtual({})
    assert v

    # Test string representation for the HPUXVirtual class
    assert str(v) == "<HPUXVirtual>"



# Generated at 2022-06-13 04:00:51.793413
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virt_obj = HPUXVirtual(dict())
    assert virt_obj.platform == 'HP-UX'
    assert virt_obj.get_virtual_facts() == dict()

# Generated at 2022-06-13 04:00:53.140691
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hp_virtual = HPUXVirtual({})
    assert hp_virtual.platform == 'HP-UX'

# Generated at 2022-06-13 04:00:55.173644
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpu_virtual = HPUXVirtual()
    assert hpu_virtual.platform == 'HP-UX'

# Generated at 2022-06-13 04:00:58.548370
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual = HPUXVirtual()
    assert hpux_virtual.platform == 'HP-UX'


# Generated at 2022-06-13 04:01:00.166416
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts = HPUXVirtual(dict())
    assert virtual_facts.platform is 'HP-UX'

# Generated at 2022-06-13 04:01:02.036957
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual = HPUXVirtual(None)
    assert hpux_virtual.platform == 'HP-UX'

# Generated at 2022-06-13 04:01:28.102222
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts = HPUXVirtual()
    assert virtual_facts
    assert virtual_facts.platform == 'HP-UX'


# Generated at 2022-06-13 04:01:38.815879
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    def exec_module(module):
        return module.run_command("/usr/sbin/parstatus")
    facts = HPUXVirtual({}, exec_module=exec_module)
    virtual_facts = facts.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'guest'
    assert 'HP nPar' in virtual_facts['virtualization_tech_guest']
    assert 'HP nPar' in virtual_facts['virtualization_role']


# Collect virtualization technology guest and host facts only if we're
# running on HP-UX
collect_subset = ['all', 'virtual']
if __name__ == '__main__':
    from ansible.module_utils.facts import main
    main(HPUXVirtualCollector)

# Generated at 2022-06-13 04:01:45.916793
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts import ModuleStub
    from ansible.module_utils.facts.facts import Facts
    import sys

    module = ModuleStub()

    # Test nPar
    if sys.version_info[0] < 3:
        module.run_command = lambda command: (0, b'HPVM vPar', "")
    else:
        module.run_command = lambda command: (0, "HPVM vPar", b"")

    virtual = HPUXVirtual(module)
    virtual_facts = virtual.get_virtual_facts()
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert virtual_facts['virtualization_type'] == 'guest'
    assert virtual_facts['virtualization_role'] == 'HPVM vPar'


# Generated at 2022-06-13 04:01:53.540449
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    HPUXVirtual = HPUXVirtual()
    HPUXVirtual._module = FakeAnsibleModule()
    HPUXVirtual.get_virtual_facts()
    assert HPUXVirtual.virtual_facts['virtualization_type'] == 'guest'
    assert HPUXVirtual.virtual_facts['virtualization_role'] == 'HP vPar'
    assert HPUXVirtual.virtual_facts['virtualization_tech_host'] == set()
    assert HPUXVirtual.virtual_facts['virtualization_tech_guest'] == set(['HP vPar'])


# Generated at 2022-06-13 04:01:59.646024
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    """
    test methods get_virtual_facts of class HPUXVirtual
    """
    module = type('FakeModule', (), {})
    module.run_command = lambda cmd: (cmd == '/usr/sbin/vecheck', '', '')
    BASE = HPUXVirtual(module=module)
    assert 'guest' == BASE.get_virtual_facts()['virtualization_type']
    assert 'HP vPar' == BASE.get_virtual_facts()['virtualization_role']
    assert set(['HP vPar']) == BASE.get_virtual_facts()['virtualization_tech_guest']
    assert set([]) == BASE.get_virtual_facts()['virtualization_tech_host']

# Generated at 2022-06-13 04:02:02.528610
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual({})
    facts = hv.get_virtual_facts()
    assert 'virtualization_type' in facts
    assert 'virtualization_role' in facts
    assert 'virtualization_tech_guest' in facts
    assert 'virtualization_tech_host' in facts

# Generated at 2022-06-13 04:02:02.981110
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    pass

# Generated at 2022-06-13 04:02:08.905866
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    '''
    Test case to verify the facts returned by get_virtual_facts
    method of HPUXVirtual class
    '''
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual
    rvalue = True
    hpux_obj = HPUXVirtual()
    hpux_obj.module = FakeAnsibleModule()
    virtual_facts = hpux_obj.get_virtual_facts()

    if virtual_facts['virtualization_tech_guest'] != set(['HP nPar']):
        rvalue = False
    if virtual_facts['virtualization_tech_host'] != set([]):
        rvalue = False
    if virtual_facts['virtualization_type'] != 'guest':
        rvalue = False

# Generated at 2022-06-13 04:02:12.448017
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual = Virtual()
    assert hpux_virtual._platform == 'HP-UX'
    assert hpux_virtual.virtualization_type is None
    assert hpux_virtual.virtualization_role is None

    hpux_virtual_collector = HPUXVirtualCollector()
    assert hpux_virtual_collector._platform == 'HP-UX'
    assert hpux_virtual._platform == 'HP-UX'
    assert hpux_virtual_collector._fact_class == HPUXVirtual
    assert hpux_virtual_collector._keywords == ['virtualization']

# Generated at 2022-06-13 04:02:14.434107
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    mp = HPUXVirtual(dict(module=dict(
        run_command=lambda *a, **kw: (0, '', ''))))
    assert mp.platform == 'HP-UX'

# Generated at 2022-06-13 04:02:54.796860
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():

    module = AnsibleModule(argument_spec = dict())

    def mock_run_command(command, *args, **kwargs):
        mocked_run_command = Mock(return_value=(0, '', ''))
        if command == '/usr/sbin/vecheck':
            mocked_run_command = Mock(return_value=(0, '/usr/sbin/vecheck', ''))
        elif command == '/opt/hpvm/bin/hpvminfo':
            mocked_run_command = Mock(return_value=(0, '/opt/hpvm/bin/hpvminfo', ''))
        elif command == '/usr/sbin/parstatus':
            mocked_run_command = Mock(return_value=(0, '/usr/sbin/parstatus', ''))
        return mocked_run_command


# Generated at 2022-06-13 04:02:58.138646
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    module = DummyAnsibleModule()
    virtual_instance = HPUXVirtual(module)
    virtual_instance.get_virtual_facts()
    assert 'virtualization_type' in module.exit_args

# Generated at 2022-06-13 04:03:03.749016
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    datadir = os.path.dirname(__file__) + "/../unit/output/"
    module = FakeModule(datadir)

    fake = HPUXVirtual(module=module)
    fake_virtual_facts = fake.get_virtual_facts()
    virtual_facts = {}
    virtual_facts['virtualization_type'] = 'guest'
    virtual_facts['virtualization_role'] = 'HP nPar'
    virtual_facts['virtualization_tech_guest'] = set(['HP nPar'])
    virtual_facts['virtualization_tech_host'] = set()

    assert fake_virtual_facts == virtual_facts

# Generated at 2022-06-13 04:03:08.875575
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    vmod = HPUXVirtual({})
    vmod.module.run_command = lambda *args, **kwargs: (0, '', '')
    vmod.module.get_bin_path = lambda *args, **kwargs: '/usr/bin/mocked'
    facts = vmod.get_virtual_facts()
    # facts['virtualization_type'] is a multivalue
    assert 'guest' in facts['virtualization_type']
    assert 'host' in facts['virtualization_type']

# Generated at 2022-06-13 04:03:17.393358
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual
    from ansible.module_utils.facts.virtual_collector import VirtualCollector
    from ansible.module_utils.facts.virtual_collector import Virtual
    import os


    # Case 1 - test method get_virtual_facts when there is no virtualization
    instance = HPUXVirtual()
    instance.module.run_command = os.system
    os.system = lambda x: (1, '', '')
    virtual_facts = instance.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'physical'
    assert virtual_facts['virtualization_role'] == 'physical'
    assert virtual_facts['virtualization_tech_guest'] == set()

# Generated at 2022-06-13 04:03:28.100076
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual
    from ansible.module_utils.six import PY2

    # Setup a class object for testing
    _HPUXVirtual = HPUXVirtual()

    # Setup a class object for testing
    if PY2:
        import __builtin__ as builtins
    else:
        import builtins

    class RunCommandMock():
        def __init__(self):
            self.rc = 0
            self.out = ''
            self.err = ''

        # pylint: disable=unused-argument
        def __call__(self, module, cmd):
            if cmd.endswith('vecheck'):
                self.rc = 0
                self.out = ''
                self.err = ''

# Generated at 2022-06-13 04:03:34.543466
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    # Test the method HPUXVirtual.get_virtual_facts
    from ansible.module_utils.facts import FactCollector

    module = AnsibleModule(
        argument_spec = dict(
            gather_subset=dict(default=['!all', 'virtual'], type='list')
        )
    )

    fact_collector = FactCollector(module=module,
        collector_class=HPUXVirtualCollector)
    fact_collector.collect()
    facts = module.exit_json['ansible_facts']
    virtual = facts['ansible_virtual']
    assert all(key in virtual for key in
        ['virtualization_type', 'virtualization_role'])

# Generated at 2022-06-13 04:03:44.979360
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    params = {'module_name': 'AnsibleModule'}
    mod = FakeModule(params)

    hpx_virtual = HPUXVirtual(mod)

    # Test: parstatus exists
    params['module_run_command'] = 'parstatus'
    params['module_run_command_rc'] = 0
    params['module_run_command_out'] = 'some output'
    assert hpx_virtual.get_virtual_facts() == {'virtualization_type': 'guest', 'virtualization_role': 'HP nPar',
                                               'virtualization_tech_guest': set(['HP nPar']), 'virtualization_tech_host': set()}

    # Test: hpvminfo exists
    params['module_run_command'] = 'hpvminfo'

# Generated at 2022-06-13 04:03:47.993382
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    module = AnsibleModule({})
    hpux = HPUXVirtual(module)
    virtual_facts = hpux.get_virtual_facts()
    assert virtual_facts['virtualization_type'] is 'guest'
    assert virtual_facts['virtualization_role'] is 'HP nPar'



# Generated at 2022-06-13 04:03:49.291010
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    test_HPUXVirtual = HPUXVirtual()
    assert test_HPUXVirtual.platform == 'HP-UX'



# Generated at 2022-06-13 04:05:00.261435
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    # First, we need to instantiate the module class
    module = FakeModule()
    # Instantiate the class to be tested
    class_to_test = HPUXVirtual(module)
    # Test with one file
    class_to_test.run_command = lambda x: (0, '', '')
    class_to_test.file_exists = lambda x: True
    class_to_test.get_virtual_facts()

    # Test with another file
    class_to_test.file_exists = lambda x: False
    class_to_test.run_command = lambda x: (1, '', '')
    class_to_test.get_virtual_facts()

    # Test with a file and a command
    class_to_test.file_exists = lambda x: True

# Generated at 2022-06-13 04:05:07.829151
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module = Dummy()
    module.run_command = DummyFunction
    facter = HPUXVirtual(module)
    facter._assemble_virtual_facts()
    assert facter.virtual_facts['virtualization_type'] == 'guest'
    assert 'HP vPar' in facter.virtual_facts['virtualization_tech_guest']
    assert 'HP nPar' in facter.virtual_facts['virtualization_tech_guest']
    assert 'HPVM vPar' in facter.virtual_facts['virtualization_tech_guest']
    assert 'HPVM IVM' in facter.virtual_facts['virtualization_tech_guest']
    assert facter.virtual_facts['virtualization_role'] == 'HP nPar'



# Generated at 2022-06-13 04:05:10.789034
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual_facts = HPUXVirtual()
    assert hpux_virtual_facts._platform == 'HP-UX', 'Test for _platform failed!'


# Generated at 2022-06-13 04:05:11.306809
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    HPUXVirtual()

# Generated at 2022-06-13 04:05:20.188070
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    # If a module is run with "-c", then the module variables are parsed and
    # used to populate the constructor. If the module is not run with "-c", then
    # the constructor is called with no args.
    #
    # When this module is executed with "-c", the "module" object is not
    # defined.  This hack allows us to run this test behavior with "-c" and
    # without "-c"
    global module
    class Options():
        connection = 42
    global module
    module = Options()
    module.run_command = run_command

    # Get the virtual facts for a guest HP-UX system runnning vPar
    virtual_facts = HPUXVirtual().get_virtual_facts()
    assert 'guest' == virtual_facts['virtualization_type']

# Generated at 2022-06-13 04:05:29.632835
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    m = AnsibleModuleMock()
    m.run_command.return_value = 0, 'output', ''
    hv = HPUXVirtual(m)
    vf = hv.get_virtual_facts()
    assert 'virtualization_type' in vf
    assert 'virtualization_role' in vf
    assert vf['virtualization_type'] == 'guest'
    assert vf['virtualization_role'] in ['HP vPar', 'HPVM vPar', 'HPVM IVM', 'HP nPar']
    # assert 'HPVM' in vf['virtualization_technologies']
    # assert 'HPVM IVM' in vf['virtualization_technologies']
    # assert 'HPVM vPar' in vf['virtualization_technologies']
    # assert 'HP vPar' in vf['virtual

# Generated at 2022-06-13 04:05:39.699047
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    """Unit test for method get_virtual_facts of class HPUXVirtual"""

    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils.facts.virtual import HPUXVirtual

    # Create a new subclass of class Virtual
    class HPUXVirtual_test(HPUXVirtual):
        """Test subclass of class HPUXVirtual"""

        platform = 'HP-UX'

        def __init__(self, module):
            super(HPUXVirtual_test, self).__init__(module)
            self.virtual_facts_cache = {}

    # Instantiate a new FactCollector object
    fact_collector = FactCollector()

    # Instantiate a new HPUXVirtual_test object

# Generated at 2022-06-13 04:05:48.412305
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    # Test on host with active hpvm, par and vpar
    # check if facts are correctly set
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True,
    )
    module.run_command = MagicMock(side_effect=[(0, 'test', ''), (0, 'test', ''), (0, 'test', '')])
    os.path.exists = MagicMock(side_effect=[True, True, True])
    virtual = HPUXVirtual(module)
    facts = virtual.get_virtual_facts()
    assert facts['virtualization_type'] == 'guest'
    assert facts['virtualization_role'] == 'HPVM vPar'

# Generated at 2022-06-13 04:05:56.231775
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    import sys
    import os
    import re

    if sys.version_info[0] > 2:
        from unittest.mock import Mock
    else:
        from mock import Mock

    # Fake module object
    module = Mock()
    module.run_command.return_value = (0, '', '')

    # Fake version file
    version_file = os.path.join(os.path.dirname(__file__), 'unittests', 'version.txt')
    module.get_bin_path.return_value = version_file

    HPUXVirtualInstance = HPUXVirtual(module=module)

# Generated at 2022-06-13 04:05:59.327100
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_obj = HPUXVirtual(dict(), dict(), dict())
    assert virtual_obj.platform == 'HP-UX'



# Generated at 2022-06-13 04:07:48.734647
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    mock_module = MockModule()
    mock_module.run_command = Mock(side_effect=[(0, '', ''), (0, '', ''), (0, '', '')])
    mock_module.stat = Mock(return_value=MockStatResult(0o777))
    mock_module.isfile = Mock(return_value=True)
    mock_module.isdir = Mock(return_value=False)
    test_obj = HPUXVirtual(mock_module)
    assert test_obj.get_virtual_facts() == {
        'virtualization_type': 'guest',
        'virtualization_role': 'HP nPar',
        'virtualization_tech_guest': set(['HP nPar']),
        'virtualization_tech_host': set()
    }

# Generated at 2022-06-13 04:07:49.776621
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    module = DummyAnsibleModule()
    virtual = HPUXVirtual(module)
    assert virtual.platform == 'HP-UX'



# Generated at 2022-06-13 04:07:54.023477
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpux import Virtual, HPUXVirtual
    virtual_facts = Virtual()
    facts_for_testing = HPUXVirtual(virtual_facts)
    test_case = dict()
    test_case['virtualization_tech_guest'] = set()
    test_case['virtualization_tech_host'] = set()
    if os.path.exists('/usr/sbin/vecheck'):
        test_case['virtualization_type'] = 'guest'
        test_case['virtualization_role'] = 'HP vPar'
        test_case['virtualization_tech_guest'] = test_case['virtualization_tech_guest'].union(set(['HP vPar']))

# Generated at 2022-06-13 04:07:59.179228
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    # Test that both guest and host facts work correctly
    module = FakeModule()
    module.run_command = FakeRunCommand({"/usr/sbin/parstatus": 0,
                                         "/usr/sbin/vecheck": 0,
                                         "/opt/hpvm/bin/hpvminfo": 2})
    virtual = HPUXVirtual(module)
    virtual.get_virtual_facts()
    assert 'virtualization_role' in virtual.facts
    assert virtual.facts['virtualization_role'] == 'HP nPar'
    assert 'virtualization_type' in virtual.facts
    assert virtual.facts['virtualization_type'] == 'guest'
    assert 'virtualization_tech_guest' in virtual.facts
    assert 'virtualization_tech_host' in virtual.facts
    assert 'HP nPar' in virtual.facts

# Generated at 2022-06-13 04:08:01.702287
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    """
    Create Virtual object
    """
    hpux = HPUXVirtual()
    assert hpux.platform == 'HP-UX'
    assert hpux.virtualization_type == ''
    assert hpux.virtualization_role == ''

# Generated at 2022-06-13 04:08:09.923229
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    m = HPUXVirtual({})
    m.module.run_command = lambda *args, **kwargs: (0, '', '') # no error
    # Mock the output of vecheck
    m.module.run_command = lambda cmd: (0, ' vecheck: Running in HP vPar environment. ', '') \
        if cmd == '/usr/sbin/vecheck' else (0, '', '')
    virtual_facts = m.get_virtual_facts()
    assert virtual_facts.get('virtualization_type') == 'guest'
    assert virtual_facts.get('virtualization_role') == 'HP vPar'
    assert virtual_facts.get('virtualization_tech_guest') == set(['HP vPar'])
    assert virtual_facts.get('virtualization_tech_host') == set()
   

# Generated at 2022-06-13 04:08:12.038307
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    '''
    Unit test to test the constructor of HPUXVirtual class
    '''
    hpux_virtual_obj = HPUXVirtual()
    assert hpux_virtual_obj


# Generated at 2022-06-13 04:08:12.705259
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv=HPUXVirtual()

# Generated at 2022-06-13 04:08:15.912299
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    v = HPUXVirtual(dict())
    assert v.platform == 'HP-UX'
    assert v.virtualization_type is None
    assert v.virtualization_role is None
    assert v.virtualization_tech_host == set()
    assert v.virtualization_tech_guest == set()


# Generated at 2022-06-13 04:08:24.836756
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    this_module = os.path.normpath(os.path.dirname(__file__))
    fixtures_path = os.path.join(this_module, 'fixtures')
    fixture_file = os.path.join(fixtures_path, 'hpux_vecheck_output.txt')
    with open(fixture_file) as hpux_vecheck_output:
        hpux_vecheck_output_text = hpux_vecheck_output.read()
        virtual = HPUXVirtual()
        virtual.module.run_command = lambda x: (0, hpux_vecheck_output_text, '')

        # For now we are returning an empty dict, but this could change in
        # the future