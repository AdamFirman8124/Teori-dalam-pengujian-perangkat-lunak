

# Generated at 2022-06-13 03:59:37.522216
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtualCollector
    from ansible.module_utils.facts.virtual.hpux import HPVirtualProcessor
    from ansible.module_utils.facts.virtual.hpux import HPVMNetwork
    from ansible.module_utils.facts.virtual.hpux import HPVMVirtualDisk
    from ansible.module_utils.facts.virtual.hpux import HPVMPartition
    from ansible.module_utils.facts.virtual.hpux import HPVMNetworkAdapter
    from ansible.module_utils.facts.virtual.hpux import HPVMVirtualDiskDevice
    from ansible.module_utils.facts.virtual.hpux import HPCIOPath

# Generated at 2022-06-13 03:59:43.558526
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    test_class = HPUXVirtual()
    test_class.module = FakeModule()

    test_input = (0,
                  'HPVM 4.2 Running\n'
                  'HPVM Tools 4.2.2.0\n'
                  'Running HPVM vPar\n',
                  '')
    test_class.module.run_command.return_value = test_input
    result = test_class.get_virtual_facts()
    assert result['virtualization_type'] == 'guest'
    assert result['virtualization_role'] == 'HPVM vPar'

    test_input = (0,
                  'HPVM 4.2 Running\n'
                  'HPVM Tools 4.2.2.0\n'
                  'Running HPVM guest\n',
                  '')
    test_class.module.run_

# Generated at 2022-06-13 03:59:47.475549
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual = HPUXVirtual({})
    assert virtual.platform == "HP-UX"
    assert virtual.get_virtual_facts() == {'virtualization_type': 'host', 'virtualization_role': 'host', 'virtualization_tech_host': set(), 'virtualization_tech_guest': set()}

# Generated at 2022-06-13 03:59:55.718745
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    """
    This is a unit test of the class HPUXVirtual.
    """

    from os import path
    from ansible.module_utils.facts.virtual import params
    if path.exists('/usr/sbin/vecheck'):  # A test only available on HP-UX systems
        vecheckoutput = "/usr/sbin/vecheck\nnull"
    else:
        vecheckoutput = ""
    if path.exists('/opt/hpvm/bin/hpvminfo'):  # A test only available on HP-UX systems
        hpvminfooutput = "/opt/hpvm/bin/hpvminfo\nRunning HPVM IVM (Guest OS)"
    else:
        hpvminfooutput = ""

# Generated at 2022-06-13 04:00:03.978475
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    parsed_facts = None
    with open('output/hpux_virtual.txt', 'r') as f:
        virtual_data = f.read()

    h_virtual = HPUXVirtual(parsed_facts, virtual_data)
    assert h_virtual.facts['virtualization_type'] == 'guest'
    assert h_virtual.facts['virtualization_role'] == 'HP nPar'
    assert 'virtualization_tech_guest' in h_virtual.facts.keys()
    assert 'virtualization_tech_host' in h_virtual.facts.keys()
    assert h_virtual.facts['virtualization_tech_guest'] == {'HP nPar'}
    assert h_virtual.facts['virtualization_tech_host'] == set()

# Generated at 2022-06-13 04:00:08.209704
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    """
    Creates the class object for testing the constructor
    """
    module_args = dict(gather_subset=['!all', 'virtual'])
    custom_args = dict(module_args)
    set_module_args(custom_args)
    hpux_virtual = HPUXVirtual(module=AnsibleModule(**custom_args))
    assert hpux_virtual.system == 'HP-UX'


# Generated at 2022-06-13 04:00:13.320871
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    v = HPUXVirtual({})
    # Test the platform fact is correct
    assert v.get_platform() == 'HP-UX'
    # Test that the return of get_virtual_facts() is empty
    assert v.get_virtual_facts() == {}

# Generated at 2022-06-13 04:00:24.425188
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpu_virtual import HPUXVirtual
    import os
    import re
    import unittest

    mock_module = unittest.mock.MagicMock()
    mock_module.run_command.side_effect = [
        (0, "", ""),
        (0, "", ""),
        (0, "", ""),
        (0, "", ""),
    ]
    hpu_virtual = HPUXVirtual(mock_module)

    virtual_facts = hpu_virtual.get_virtual_facts()
    assert not virtual_facts
    mock_module.run_command.assert_any_call("/usr/sbin/vecheck")

# Generated at 2022-06-13 04:00:26.767757
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    v = HPUXVirtual()
    assert v.platform == 'HP-UX'



# Generated at 2022-06-13 04:00:34.206221
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    test_module = type('test module', (object,), dict())

    fake_run_command = [
        'hpvmstatus',
        'vecheck'
    ]

    def dummy_run_command(cmd):
        output = ''
        if cmd == 'hpvmstatus':
            output = '''
hpvmstatus: HPVM guest "ansibleTest" running on host "ansibleTestHost"
'''
        elif cmd == 'vecheck':
            output = '''
/usr/sbin/vecheck: Running standard (non-secure-guest) VE.
'''
        rc = 0
        return (rc, output, '')  # rc, stdout, stderr

    # Create a test module object with globals
    test_module.run_command = dummy_run_command
    test_module.glob

# Generated at 2022-06-13 04:00:42.559781
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual()
    assert hv is not None

# Generated at 2022-06-13 04:00:44.270680
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts = HPUXVirtual({})
    assert virtual_facts.platform == 'HP-UX'

# Generated at 2022-06-13 04:00:48.878138
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_test = HPUXVirtual()
    assert virtual_test.platform == 'HP-UX'
    assert virtual_test.virtualization_type == 'guest'
    assert virtual_test.virtualization_role == 'HP vPar'
    assert virtual_test.virtualization_tech_guest == set(['HP vPar'])
    assert virtual_test.virtualization_tech_host == set()

# Generated at 2022-06-13 04:00:59.389029
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    # We need to mock module_utils.basic.AnsibleModule.run_command
    from ansible.module_utils.basic import AnsibleModule
    original_run_command = AnsibleModule.run_command

    # Mock module_utils.basic.AnsibleModule.run_command
    def run_command_mock(*args, **kwargs):
        # Does the command being run match what we expect?
        cmd = args[0]
        if cmd == '/usr/sbin/vecheck':
            rc = 0
        elif cmd == '/opt/hpvm/bin/hpvminfo':
            rc = 0

# Generated at 2022-06-13 04:01:07.021051
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.virtual import HPUXVirtual
    from ansible.module_utils.facts.virtual import VirtualCollector
    # Test if setting collector._COLLECTORS works.
    HPUXVirtualCollector._COLLECTORS = {}
    VirtualCollector._COLLECTORS = {}
    collector.collectors.remove(HPUXVirtualCollector)
    collector.collectors.append(HPUXVirtualCollector)
    # Test if setting collector.HPUXVirtual._COLLECTORS works.
    HPUXVirtual._COLLECTORS = {}
    VirtualCollector._COLLECTORS = {}
    collector.collectors.remove(HPUXVirtualCollector)
    collector.collectors.append(HPUXVirtualCollector)

# Generated at 2022-06-13 04:01:10.114449
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual = HPUXVirtual()
    assert hpux_virtual.platform == 'HP-UX'
    assert hpux_virtual.get_virtual_facts() == {}


# Generated at 2022-06-13 04:01:14.401247
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    v = HPUXVirtual({})
    assert v.type == 'guest'
    assert v.role == 'HP vPar'

    v = HPUXVirtual({}, {'virtualization_type': 'guest', 'virtualization_role': 'HPVM vPar'})
    assert v.type == 'guest'
    assert v.role == 'HPVM vPar'

# Generated at 2022-06-13 04:01:24.306334
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts import ModuleDataCollector

    class FakeModule(object):
        def __init__(self, **kwargs):
            self.params = {
                'gather_subset': [],
                'filter': '*'
            }
            self.params.update(kwargs)
            self.facts = {'virtualization_tech_host': set(), 'virtualization_tech_guest': set()}

        def get_bin_path(self, binary, required=False, opt_dirs=[]):
            return '/usr/bin/' + binary

        def run_command(self, cmd, check_rc=True):
            if cmd == "/usr/sbin/vecheck":
                return (0, "", "")

# Generated at 2022-06-13 04:01:32.290519
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts import Facts
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual
    from ansible import context
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtualCollector

    mock_out = {'stdout': "", 'stdout_lines': [], 'stderr': "", 'rc': 0}

    mock_paths = ['/usr/sbin/vecheck', '/opt/hpvm/bin/hpvminfo', '/usr/sbin/parstatus']
    mock_results = [None]*len(mock_paths)

    def mock_run_command(self, cmd, check_rc=False):
        if cmd == mock_paths[0]:
            return mock_results[0]

# Generated at 2022-06-13 04:01:42.069408
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpux.vf import HPUXVirtual
    from ansible.module_utils.facts.virtual.hpux.vf import HPUXVirtualCollector
    from ansible.module_utils.facts.virtual.hpux.vf import test_HPUXVirtual_get_virtual_facts
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts.virtual.hpux.vf import HP_UX_VF_RESOURCES

    def _mock_ansible_module(resources):
        class AnsibleModuleMock(object):
            _ANSIBLE_ARGS = {
                'module_name': 'ansible_facts',
                'module_args': 'filter=ansible_virtual'
            }

# Generated at 2022-06-13 04:01:58.989106
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    # Check if a guest hp vPar
    if os.path.exists('/usr/sbin/vecheck'):
        # mf.run_command("/usr/sbin/vecheck") is called later
        # For now, it is just a stub, which returns a fake output
        rc, out, err = (0, "is a guest hp vPar", "")
        if rc == 0 and re.match('.*is a guest hp vPar.*', out):
            guest_tech = set()
            guest_tech.add('HP vPar')
            virtual_facts = {}
            virtual_facts['virtualization_type'] = 'guest'
            virtual_facts['virtualization_role'] = 'HP vPar'
            virtual_facts['virtualization_tech_guest'] = guest_tech

# Generated at 2022-06-13 04:02:00.657716
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual = HPUXVirtual(dict(((x, x) for x in range(10))))
    assert(isinstance(virtual, Virtual))


# Generated at 2022-06-13 04:02:01.670394
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual()
    assert hv.platform == 'HP-UX'

# Generated at 2022-06-13 04:02:07.919987
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    # Create an instance of HPUXVirtual
    virtual_obj = HPUXVirtual(dict(ANSIBLE_MODULE_ARGS=dict(gather_subset='all')))

    # Mock modules
    virtual_obj.module = Mock(params=dict())

    # if vecheck is not present
    if os.path.exists('/usr/sbin/vecheck'):
        rc, out, err = virtual_obj.module.run_command.return_value = (0, "Running HP vPar", "")
    else:
        rc, out, err = virtual_obj.module.run_command.return_value = (1, "", "")

    # if hpvminfo is not present
    if os.path.exists('/opt/hpvm/bin/hpvminfo'):
        rc, out, err

# Generated at 2022-06-13 04:02:11.581412
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual = HPUXVirtual(dict(module=dict()))
    assert virtual.platform == 'HP-UX'
    assert virtual.virtualization_type is None
    assert virtual.virtualization_role is None


# Generated at 2022-06-13 04:02:18.166275
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    class MockModule(object):
        def __init__(self, rc, out, err):
            self.rc = rc
            self.out = out
            self.err = err

        def run_command(self, cmd):
            return self.rc, self.out, self.err

    # Test for vecheck with rc=0 and parstatus with rc=0
    module = MockModule(0, "", "")
    virtual_facts = HPUXVirtual(module).get_virtual_facts()

# Generated at 2022-06-13 04:02:23.682027
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    with open('/tmp/hpu', 'w') as mock_hpu, \
            open('/tmp/vecheck', 'w') as mock_vecheck, \
            open('/tmp/hpvminfo', 'w') as mock_hpvminfo, \
            open('/tmp/parstatus', 'w') as mock_parstatus:
        mock_vecheck.write('')
        mock_hpvminfo.write('Running on HPVM vPar node')
        mock_parstatus.write('')
        mock_hpu.write('')

        os.environ['PATH'] = '/tmp'
        virtual_facts = HPUXVirtual().get_virtual_facts()

        assert virtual_facts['virtualization_type'] == 'guest'

# Generated at 2022-06-13 04:02:29.449652
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    import ansible.module_utils.facts.virtual.hpux
    result = ansible.module_utils.facts.virtual.hpux.HPUXVirtual(dict(ANSIBLE_MODULE_ARGS={})).get_virtual_facts()
    assert 'virtualization_type' in result
    assert 'virtualization_role' in result
    assert 'virtualization_tech_guest' in result
    assert 'virtualization_tech_host' in result

# Generated at 2022-06-13 04:02:30.350003
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    test_obj = HPUXVirtual(dict())
    assert test_obj


# Generated at 2022-06-13 04:02:32.163105
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    """
    Test for HPUXVirtual
    """
    my_hpxvirtual = HPUXVirtual(None)
    assert my_hpxvirtual.platform == 'HP-UX'
    del my_hpxvirtual


# Generated at 2022-06-13 04:03:05.645231
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module = FakeAnsibleModule()
    module.run_command = mock_run_command

    hpux_virtual = HPUXVirtual(module)
    virtual_facts = hpux_virtual.get_virtual_facts()
    assert 'virtualization_type' in virtual_facts
    if virtual_facts['virtualization_type'] == 'guest':
        assert 'virtualization_role' in virtual_facts
    else:
        assert 'virtualization_role' not in virtual_facts


# Generated at 2022-06-13 04:03:14.893928
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    class ModuleStub(object):
        def __init__(self):
            self.run_command_result = (0, '', '')

        def run_command(self, cmd):
            return self.run_command_result

    module = ModuleStub()

    h = HPUXVirtual(module)

    # HPVM
    module.run_command_result = (0, 'Running HPVM host', '')
    assert h.get_virtual_facts() == {
        'virtualization_role': 'HPVM',
        'virtualization_type': 'host',
        'virtualization_tech_guest': {'HPVM'},
        'virtualization_tech_host': set()
    }

    # HPVM - guest
    module.run_command_result = (0, 'Running HPVM guest', '')

# Generated at 2022-06-13 04:03:25.340353
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    """
    This unit test checks the method get_virtual_facts of class HPUXVirtual.
    """
    # variables for unit test
    class Module(object):
        pass

    # create module object
    module = Module()

    # create Virtual class object
    virtual = HPUXVirtual(module)

    # create the facts dictionary
    facts = {}

    # set the virtualization_tech_guest set in HPUXVirtual class object
    virtual.virtualization_tech_guest = set()

    # set the virtualization_tech_host set in HPUXVirtual class object
    virtual.virtualization_tech_host = set()

    # set the virtualization_type as guest in HPUXVirtual class object
    virtual.virtualization_type = 'guest'

    # set the virtualization_role as HP nPar in HPUXVirtual

# Generated at 2022-06-13 04:03:29.380085
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module_mock = mock.MagicMock()
    module_mock.run_command.return_value = (0, '', '')
    virtual_facts = HPUXVirtual(module_mock).get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'guest'
    assert virtual_facts['virtualization_role'] == 'HP vPar'

# Generated at 2022-06-13 04:03:39.843484
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    import subprocess
    from ansible.module_utils.facts.virtual.hpar import HPUXVirtual
    from ansible.module_utils.facts.virtual.hpar import HPUXVirtualCollector
    from ansible.module_utils.basic import AnsibleModule
    import tempfile
    import os
    import sys

    class TestModule(object):
        def __init__(self, run_command_fn):
            self.run_command_fn = run_command_fn

        def run_command(self, command, check_rc=None):
            rc = 0
            err = None
            out = None

            if command[0] == '/usr/sbin/vecheck':
                command[0] = '/bin/cat'

# Generated at 2022-06-13 04:03:48.023501
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    # Create a fake module object
    module_args = {}
    module = AnsibleModule(argument_spec=module_args)

    # Create a HPUXVirtual object
    virtual = HPUXVirtual(module)

    # Create the facts to compare
    facts = {
             'virtualization_type': 'guest',
             'virtualization_role': 'HP vPar',
             'virtualization_tech_host': set(),
             'virtualization_tech_guest': set(['HP vPar'])
            }

    # Assert the facts returned by get_virtual_facts() matches the facts created above
    assert test_HPUXVirtual_get_virtual_facts.__name__ == HPUXVirtual.get_virtual_facts.__name__
    assert facts == virtual.get_virtual_facts()

# Generated at 2022-06-13 04:03:57.576266
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    import module_utils.facts.virtual.hpux as hpux_facts
    class TestModule(object):
        def run_command(self, command):
            if command == "/usr/sbin/vecheck":
                return 0, "hpar_status: Active\n", ""
            elif command == "/usr/sbin/parstatus":
                return 0, "PARstatus	PAR Status	Enabled\n", ""

    m = TestModule()
    hpux_facts.HPUXVirtual.module = m

    facts = hpux_facts.HPUXVirtual().get_virtual_facts()
    assert facts['virtualization_type'] == 'guest'
    assert facts['virtualization_role'] == 'HP nPar'
    assert facts['virtualization_tech_host'] == set()
    assert facts['virtualization_tech_guest']

# Generated at 2022-06-13 04:04:05.877103
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    hpux_virtual_facts = HPUXVirtual(dict(module=dict()))
    guest_tech = set()
    if os.path.exists('/usr/sbin/parstatus'):
        rc, out, err = hpux_virtual_facts.module.run_command("/usr/sbin/parstatus")
        if rc == 0:
            guest_tech.add('HP nPar')
    if os.path.exists('/usr/sbin/vecheck'):
        rc, out, err = hpux_virtual_facts.module.run_command("/usr/sbin/vecheck")
        if rc == 0:
            guest_tech.add('HP vPar')
    if os.path.exists('/opt/hpvm/bin/hpvminfo'):
        rc, out, err = hp

# Generated at 2022-06-13 04:04:07.731297
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virt = HPUXVirtual({})
    assert virt.platform == 'HP-UX'



# Generated at 2022-06-13 04:04:08.933657
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hp = HPUXVirtual({})
    assert HPUXVirtual.platform == 'HP-UX'


# Generated at 2022-06-13 04:04:47.087952
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    class TestModule(object):
        def run_command(self, args, check_rc=True):
            if args == '/usr/sbin/vecheck':
                return (0, '', '')
            if args == '/opt/hpvm/bin/hpvminfo':
                return (0, 'Running as a HPVM vPar in a HPVM Virtual Platform', '')
            if args == '/usr/sbin/parstatus':
                return (0, '', '')
            raise Exception("unexpected argument")

    test_module = TestModule()
    m = HPUXVirtual(test_module)
    result = m.get_virtual_facts()
    assert result['virtualization_tech_host'] == set()
    assert result['virtualization_tech_guest'] == {'HPVM', 'HPVM vPar'}
   

# Generated at 2022-06-13 04:04:58.288808
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    virtual_facts_test = HPUXVirtual(dict()).get_virtual_facts()
    assert virtual_facts_test['virtualization_type'] == 'guest'
    assert virtual_facts_test['virtualization_role'] == 'HP vPar'
    assert 'HP vPar' in virtual_facts_test['virtualization_tech_guest']
    assert 'HP nPar' in virtual_facts_test['virtualization_tech_guest']
    assert 'HPVM IVM' in virtual_facts_test['virtualization_tech_guest']
    assert 'HPVM' in virtual_facts_test['virtualization_tech_host']
    assert 'HPVM vPar' in virtual_facts_test['virtualization_tech_guest']

# Generated at 2022-06-13 04:05:07.031574
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from collections import namedtuple
    from ansible_collections.ansible.community.plugins.module_utils.facts.virtual.hux import HPUXVirtual

    MockModule = namedtuple('MockModule', ['run_command'])

    def run_command(command, check_rc=True):
        commands = {
            '/usr/sbin/vecheck': 0,
            '/opt/hpvm/bin/hpvminfo': 0,
            '/usr/sbin/parstatus': 0
        }
        return commands[command], '', ''

    mock_module = MockModule(run_command)
    fact_class = HPUXVirtual(mock_module)
    virtual_facts = fact_class.get_virtual_facts()

# Generated at 2022-06-13 04:05:16.827533
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpuix import HPUXVirtual

# Generated at 2022-06-13 04:05:18.322934
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    m = HPUXVirtual({})
    assert m._platform == 'HP-UX'


# Generated at 2022-06-13 04:05:21.279349
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual = HPUXVirtual()
    assert virtual.module.check_mode is False
    assert virtual.module.run_command.called is False
    assert virtual.module.exit_json.called is False



# Generated at 2022-06-13 04:05:26.332525
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    v = HPUXVirtual('test')
    assert v.platform == 'HP-UX'
    assert v.get_virtual_facts() == {'virtualization_type': 'guest', 'virtualization_role': 'HP nPar', 'virtualization_tech_guest': set(['HP nPar']), 'virtualization_tech_host': set()}

# Generated at 2022-06-13 04:05:28.273412
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual()
    hv.get_virtual_facts()
    assert hv.platform == 'HP-UX'

# Generated at 2022-06-13 04:05:35.438461
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module = AnsibleModule(argument_spec={})
    vs_obj = HPUXVirtual(module)

    # When both vecheck and hpvminfo programs exist and return valid output.
    vs_obj.module.run_command = Mock(side_effect=side_effect_command)
    module.files = {
        '/usr/sbin/vecheck': {'mode': 'rwxrwxrwx', 'size': 0},
        '/opt/hpvm/bin/hpvminfo': {'mode': 'rwxrwxrwx', 'size': 0},
    }
    virtual_facts = vs_obj.get_virtual_facts()

# Generated at 2022-06-13 04:05:38.194105
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module = type('', (), {})
    module.run_command = run_command
    virtual_obj = HPUXVirtual(module)

    assert virtual_obj.get_virtual_facts() == {'virtualization_type': 'guest', 'virtualization_role': 'HP vPar',
                                               'virtualization_tech_host': set(),
                                               'virtualization_tech_guest': set(['HP vPar'])}



# Generated at 2022-06-13 04:06:00.435459
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual = HPUXVirtual()
    assert virtual.platform == 'HP-UX'


# Generated at 2022-06-13 04:06:02.202414
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual = HPUXVirtual(None)
    assert hpux_virtual.platform == 'HP-UX'


# Generated at 2022-06-13 04:06:05.101651
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual = HPUXVirtual()
    assert hpux_virtual.platform == 'HP-UX'

# Generated at 2022-06-13 04:06:14.241431
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module = AnsibleModule(argument_spec={})

    class AnsibleModuleMock:

        def run_command(self, command):
            if command == "/usr/sbin/vecheck":
                return 0, "", ""
            if command == "/opt/hpvm/bin/hpvminfo":
                return 0, "", ""
            if command == "/usr/sbin/parstatus":
                return 0, "", ""
            return 1, "", ""

    ve = HPUXVirtual(AnsibleModuleMock())
    ve_facts = ve.get_virtual_facts()

    assert ve_facts['virtualization_type'] == 'guest'
    assert ve_facts['virtualization_role'] == ''

# Generated at 2022-06-13 04:06:16.761012
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    v = HPUXVirtual()
    assert v is not None
    assert v.platform == 'HP-UX'

# Generated at 2022-06-13 04:06:26.851767
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    import tempfile
    import shutil
    from ansible.module_utils.facts import collect_facts
    class MockModule(object):
        def __init__(self, params=None, check_invalid_arguments=False, run_command=None):
            self.params = params
            self.check_invalid_arguments = check_invalid_arguments
            self.run_command = run_command
    tmpdir = tempfile.mkdtemp()
    vecheck = os.path.join(tmpdir, 'vecheck')
    open(vecheck, 'a').close()
    hpvminfo = os.path.join(tmpdir, 'hpvminfo')
    open(hpvminfo, 'a').close()
    parstatus = os.path.join(tmpdir, 'parstatus')

# Generated at 2022-06-13 04:06:29.326502
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hw = HPUXVirtual(dict(), dict())
    assert hw.get_virtual_facts() is not None

# Generated at 2022-06-13 04:06:36.554701
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    out = "TEST_OUTPUT"
    rc = 0
    err = None
    vs = HPUXVirtual({})
    vs.module = MockModule(out=out, rc=rc, err=err)
    vs.module.run_command = Mock(return_value=(rc, out, err))
    os.path = Mock()
    vs.get_virtual_facts()
    if os.path.exists.call_count == 1:
        if vs.module.run_command.call_count == 2:
            return True
    return False



# Generated at 2022-06-13 04:06:38.147064
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual = HPUXVirtual({},{},{})
    assert type(hpux_virtual) == HPUXVirtual


# Generated at 2022-06-13 04:06:43.152658
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module = AnsibleModule(
        argument_spec=dict()
    )
    hw = HPUXVirtual(module)
    virtual_facts = hw.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'guest'
    assert virtual_facts['virtualization_role'] == 'HPVM'
    assert 'HPVM' in virtual_facts['virtualization_tech_guest']


# Generated at 2022-06-13 04:07:15.320485
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual = HPUXVirtual(None)
    assert hpux_virtual.platform == 'HP-UX'


# Generated at 2022-06-13 04:07:18.105911
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_fact = HPUXVirtual()
    assert virtual_fact.platform == 'HP-UX'
    assert virtual_fact.get_virtual_facts() == {
        'virtualization_type': 'host',
        'virtualization_role': 'HPVM',
        'virtualization_tech_guest': set(['HPVM']),
        'virtualization_tech_host': set()
    }

# Generated at 2022-06-13 04:07:20.651704
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    from ansible.module_utils.facts.virtual.hpar import HPUXVirtual
    obj = HPUXVirtual()
    assert obj.platform == 'HP-UX'

# Generated at 2022-06-13 04:07:24.296889
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    """
    Unit test for method get_virtual_facts of class
    HPUXVirtual
    """
    facts = HPUXVirtual().get_virtual_facts()
    assert 'virtualization_type' in facts
    assert 'virtualization_role' in facts
    assert 'virtualization_tech_guest' in facts
    assert 'virtualization_tech_host' in facts

# Generated at 2022-06-13 04:07:30.321410
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    virtual_facts = None
    f = HPUXVirtual({})
    virtual_facts = f.get_virtual_facts()
    assert virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_type' in virtual_facts

# Generated at 2022-06-13 04:07:37.936911
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual
    module = AnsibleModule(argument_spec=dict())
    hpux_virtual = HPUXVirtual(module)
    virtual_facts = hpux_virtual.get_virtual_facts()
    assert virtual_facts == {'virtualization_tech_guest': set(['HPVM IVM', 'HP vPar', 'HP nPar']),
                             'virtualization_role': 'HP nPar',
                             'virtualization_tech_host': set([]),
                             'virtualization_type': 'guest'}

# Generated at 2022-06-13 04:07:39.157635
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    test_hpux_virtual = HPUXVirtual({},{},{})
    assert test_hpux_virtual.platform == 'HP-UX'


# Generated at 2022-06-13 04:07:41.862993
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    v = HPUXVirtual({})
    assert v.platform == 'HP-UX'
    assert v.get_virtual_facts() == {
        'virtualization_type': None,
        'virtualization_type_role': None,
        'virtualization_tech_host': set(),
        'virtualization_tech_guest': set(),
    }

# Generated at 2022-06-13 04:07:51.477820
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    mock_module = MockModule()
    mock_module.run_command.side_effect = [
        (0, '', ''),
        (0, 'Running in vPar with 1 CPU(s)', '')
    ]
    virtual_facts_collector = HPUXVirtual(mock_module)
    virtual_facts = virtual_facts_collector.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'guest'
    assert virtual_facts['virtualization_role'] == 'HP vPar'
    assert virtual_facts['virtualization_tech_guest'] == set(['HP vPar'])
    assert 'virtualization_tech_host' not in virtual_facts
    # Check that run_command() is called for each of the files we are attempting to verify

# Generated at 2022-06-13 04:07:53.308536
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    vp = HPUXVirtual(None)
    assert vp.platform == 'HP-UX'
    assert vp.virtual_type == 'hppa'

# Generated at 2022-06-13 04:08:29.460371
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual()
    assert hv.platform == 'HP-UX'
    assert hv.to_dict() == {'virtualization_role': None, 'virtualization_type': None, 'virtualization_tech_guest': set(), 'virtualization_tech_host': set()}


# Generated at 2022-06-13 04:08:32.886990
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    '''Unit test for class HPUXVirtual'''
    virtual_facts = HPUXVirtual().get_virtual_facts()
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts

# Generated at 2022-06-13 04:08:38.038843
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():

    # Create a HP-UXVirtual object
    hpux_virtual_obj = HPUXVirtual()

    # Create a test module object
    from ansible.module_utils.facts.test import TestAnsibleModule
    test_module = TestAnsibleModule(
        name='test',
        module_args='',
        ansible_facts=hpux_virtual_obj.get_facts()
    )

    # Set the commands return values for the virtual executable files
    if hpux_virtual_obj.module.get_bin_path('vecheck'):
        # Create HP vPar
        hpux_virtual_obj.module.run_command = MagicMock(return_value=(0, '', ''))

# Generated at 2022-06-13 04:08:45.210992
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpu import HPUXVirtual
    try:
        mock_module = Mock()
        mock_module.run_command = Mock(return_value=(0, '', ''))
        hp_obj = HPUXVirtual(mock_module)
        hp_obj.get_virtual_facts()
    except Exception as e:
        print("Failed get_virtual_facts unit test")
        raise e

if __name__ == '__main__':
    test_HPUXVirtual_get_virtual_facts()

# Generated at 2022-06-13 04:08:51.604808
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    HPUXVirtualCollector = HPUXVirtualCollector()
    HPUXVirtual = HPUXVirtualCollector._fact_class
    HPUXVirtual = HPUXVirtual()
    output = HPUXVirtual.get_virtual_facts()
    if isinstance(output, dict):
        assert 'virtualization_type' in output
        assert 'virtualization_role' in output
    else:
        assert False, '_get_virtual_facts() must return a dictionary'

# Generated at 2022-06-13 04:08:54.756766
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    module = Virtual(dict(ANSIBLE_MODULE_ARGS={}))
    hv = HPUXVirtual(module)
    assert module == hv._module
    assert 'HP-UX' == hv.platform


# Generated at 2022-06-13 04:08:56.698155
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    v = HPUXVirtual({})
    assert v.platform == 'HP-UX'

# Generated at 2022-06-13 04:09:02.546965
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    import ansible.module_utils.facts.virtual.hpux_virtual as hpux_virtual
    hpux_virtual.os.path.exists = lambda x: True
    hpux_virtual.os.path.isfile = lambda x: True
    hpux_virtual.os.access = lambda x, y: True
    hpux_virtual.os.stat = lambda x: FakeStat()

    module = FakeModule()

    module.run_command = lambda x: (0, '', '')
    fake_virtual_facts = {}
    fake_virtual_facts["virtualization_type"] = "host"
    fake_virtual_facts["virtualization_role"] = "HPVM"
    fake_virtual_facts["virtualization_tech_host"] = set(["HPVM"])

# Generated at 2022-06-13 04:09:07.592868
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual = HPUXVirtual({})
    assert virtual.platform == 'HP-UX'
    assert virtual.get_virtual_facts()['virtualization_type'] == 'guest'
    assert virtual.get_virtual_facts()['virtualization_role'] == 'HP nPar'
    assert 'HP nPar' in virtual.get_virtual_facts()['virtualization_tech_guest']
    assert 'HPVM' in virtual.get_virtual_facts()['virtualization_tech_host']

# Generated at 2022-06-13 04:09:08.403046
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual = HPUXVirtual()
    assert virtual.platform == 'HP-UX'

