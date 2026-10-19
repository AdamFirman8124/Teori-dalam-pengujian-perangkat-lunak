

# Generated at 2022-06-13 03:59:28.010492
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    (virtual_facts, dummy) = HPUXVirtual().get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'guest'
    assert virtual_facts['virtualization_role'] == 'HP nPar'

# Generated at 2022-06-13 03:59:36.006519
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual = HPUXVirtual()
    assert len(virtual.subclasses) == 1
    assert virtual.subclasses[0] == virtual.__class__
    assert virtual.platform == 'HP-UX'
    assert len(virtual.file_paths) == 0
    assert len(virtual.files) == 0
    assert virtual.commands == {'hpvminfo': '/opt/hpvm/bin/hpvminfo', 'parstatus': '/usr/sbin/parstatus', 'vecheck': '/usr/sbin/vecheck'}
    assert virtual.virtual_facts == {}
    assert virtual.get_virtual_facts() == {}

# Generated at 2022-06-13 03:59:42.196120
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    host_tech = set()
    guest_tech = set()
    expected_keys = set(['virtualization_type',
                         'virtualization_role',
                         'virtualization_tech_guest',
                         'virtualization_tech_host'])

    virtual_facts = HPUXVirtual({}).get_virtual_facts()

    assert set(virtual_facts.keys()) == expected_keys
    assert isinstance(virtual_facts['virtualization_tech_guest'], set)
    assert isinstance(virtual_facts['virtualization_tech_host'], set)
    assert virtual_facts['virtualization_tech_guest'] == guest_tech
    assert virtual_facts['virtualization_tech_host'] == host_tech

# Generated at 2022-06-13 03:59:44.756057
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual = HPUXVirtual(None)
    assert hpux_virtual.platform == 'HP-UX'


# Generated at 2022-06-13 03:59:53.573921
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    """
    This test case tests the get_virtual_facts method of class HPUXVirtual.
    """
    HPUXVirtual_obj = HPUXVirtual({})

    # Test if class attributes have proper values
    assert HPUXVirtual_obj.platform == 'HP-UX'
    assert HPUXVirtual_obj.guest_tech == set()
    assert HPUXVirtual_obj.virtualization_type is None
    assert HPUXVirtual_obj.virtualization_role is None

    class FakeModule(object):
        def __init__(self):
            pass

        def run_command(self, cmd):
            return (0, 'Running HPVM guest', '')

    HPUXVirtual_obj.module = FakeModule()
    virtual_facts = HPUXVirtual_obj.get_virtual_facts()

    # Test if

# Generated at 2022-06-13 03:59:55.217684
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts = HPUXVirtual()
    assert virtual_facts.platform == 'HP-UX'


# Generated at 2022-06-13 04:00:02.985995
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    # The test code is HP-UX specific, so we mock the module.run_command
    import __builtin__
    mock_module = type("AnsibleModule", (), {})()
    mock_module.run_command = lambda x: (0, "Running HPVM guest", "")

    # Mock the module __builtin__ for the class definition
    import __builtin__
    class MockBuiltinModule:
        def __init__(self, module_name):
            setattr(self, 'module_name', module_name)
    mock_builtin_module = MockBuiltinModule('AnsibleModule')
    setattr(__builtin__, 'AnsibleModule', mock_builtin_module)

    # Create instance of class HPUXVirtual
    hpuxvirtual = HPUXVirtual(mock_module)
    virtual_

# Generated at 2022-06-13 04:00:08.675580
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual import HPUXVirtual
    module = FakeModule()
    virtual = HPUXVirtual(module)
    facts_dict = virtual.get_virtual_facts()

    assert facts_dict['virtualization_tech_guest'] == {'HP vPar', 'HPVM vPar', 'HPVM IVM', 'HPVM', 'HP nPar'}
    assert facts_dict['virtualization_tech_host'] == set()
    assert facts_dict['virtualization_type'] == 'guest'
    assert facts_dict['virtualization_role'] == 'HP vPar'



# Generated at 2022-06-13 04:00:18.390017
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    """
    Mock module class for testing method get_virtual_facts of class HPUXVirtual
    """
    class HPUXVirtual_MockModule(object):
        def __init__(self):
            self.run_command_args = []
            self.run_command_rc = 0
            self.run_command_out = ''
            self.run_command_err = ''

        def run_command(self, args):
            self.run_command_args = args
            return (self.run_command_rc, self.run_command_out,
                    self.run_command_err)
    # Case: Virtualization_type as guest and virtualization_role as HP vPar
    test_virtual_facts = HPUXVirtual_MockModule()
    test_virtual = HPUXVirtual(test_virtual_facts)
   

# Generated at 2022-06-13 04:00:23.157241
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtualCollector
    module = DummyModule()
    virtual = HPUXVirtual(module)
    virtual.get_virtual_facts()
    assert module.exit_args['failed'] is False
    assert module.exit_args['changed'] is False



# Generated at 2022-06-13 04:00:36.715050
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    module_args = dict()
    hpux_virtual = HPUXVirtual(module_args, False)

    assert hpux_virtual.platform == 'HP-UX'
    assert hpux_virtual._platform == 'HP-UX'
    assert hpux_virtual.module_args is module_args
    assert hpux_virtual.fallback is False


# Generated at 2022-06-13 04:00:42.816904
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():

    # ignore error when vecheck is not installed
    # ignore error when hpvminfo is not installed
    # ignore error when parestatus is not installed

    # happy path
    out = """ 
    
                          Virtual Environment Summary
    
   Virtual Environment            = Not Started
   Processor Partition            = Not Started
   HPVM                           = Not Supported
   
   
   
    """
    hpux = HPUXVirtual({'module_setup': True}, out, None)
    virtual_facts = hpux.get_virtual_facts()
    assert virtual_facts['virtualization_type'] is None
    assert virtual_facts['virtualization_role'] is None
    assert virtual_facts['virtualization_tech_host'] == set()
    assert virtual_facts['virtualization_tech_guest'] == set()

    # vecheck started
    out

# Generated at 2022-06-13 04:00:48.430768
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpux.HPUXVirtual import HPUXVirtual
    virtual = HPUXVirtual(dict())
    facts = virtual.get_virtual_facts()
    assert facts['virtualization_tech_host'] == set()
    assert facts['virtualization_tech_guest'] == set()
    assert facts['virtualization_role'] == 'HPVM IVM'
    assert facts['virtualization_type'] == 'guest'

# Generated at 2022-06-13 04:00:51.004649
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_obj = HPUXVirtual({})
    print(virtual_obj.platform)
    print(virtual_obj.get_virtual_facts())


# Generated at 2022-06-13 04:00:53.527871
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual

    facts = HPUXVirtual()
    virtual_facts = facts.get_virtual_facts()
    assert ('virtualization_type' in virtual_facts)

# Generated at 2022-06-13 04:01:04.323472
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module = AnsibleModule(argument_spec={})
    v = HPUXVirtual(module)

    # Mock function run_command with responses.
    def run_command_mock(self, args, check_rc=True):
        my_output = dict()
        my_output['rc'] = 0,
        my_output['stdout'] = """The system appears to be
        Running as a HPVM guest.
        Running as a HP vPar guest.
        Running as a HP nPar guest.
        """
        my_output['stderr'] = ""
        return my_output

    v.module.run_command = run_command_mock

    facts = v.get_virtual_facts()
    assert 'virtualization_type' in facts
    assert facts['virtualization_type'] == 'guest'

# Generated at 2022-06-13 04:01:15.047239
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module = FakeAnsibleModule()
    stat = FakeStat()
    isfile = FakeIsFile()
    islink = FakeIsLink()
    ismount = FakeIsMount()
    called = FakeCalled()
    run_command = FakeRunCommand()
    module.run_command = run_command
    module.stat = stat
    module.os.path.isfile = isfile
    module.os.path.islink = islink
    module.os.path.ismount = ismount
    module.sysfs.called = called

    # Virtualization technology: HP vPar on HP-UX 11.3
    try:
        virtual_facts = HPUXVirtual(module).get_virtual_facts()
    except Exception as e:
        module.fail_json(msg=e.message)

# Generated at 2022-06-13 04:01:25.214944
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtualCollector
    from ansible.module_utils.facts.virtual import VirtualCollector
    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=[], type='list')
        )
    )
    HPUXVirtualCollector.gather_facts(module)
    facts_d = module.params['ansible_facts']
    assert('virtualization_tech_host' in facts_d)
    assert(facts_d['virtualization_tech_host'] == set())

# Generated at 2022-06-13 04:01:32.488499
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts import add_deprecated_fact

# Generated at 2022-06-13 04:01:33.941438
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    assert HPUXVirtual(dict()).platform == 'HP-UX'

# Generated at 2022-06-13 04:01:48.563395
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts = HPUXVirtual({'module_name': 'test'})
    assert virtual_facts.platform == 'HP-UX'

# Generated at 2022-06-13 04:01:49.854915
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual = HPUXVirtual()


# Generated at 2022-06-13 04:01:52.600342
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpuxv = HPUXVirtual({}, {}, "/usr/bin/ansible", False)
    assert hpuxv.module.run_command("/usr/bin/ansible") == (1, '', 'sample output')

# Generated at 2022-06-13 04:01:59.040894
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtualCollector
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtualModule
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtualVirtualization
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtualRole
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtualTech
    from ansible.module_utils.facts import ModuleTestCase
    from ansible.module_utils.facts import VirtualTestCase
    import ansible_collections.ansible.community.tests.unit.modules.utils.virtual_tests as virtual_tests

    #
    # HP-

# Generated at 2022-06-13 04:02:03.298453
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module = { 'run_command' : run_command }
    collector = HPUXVirtual(module)
    facts = collector.get_virtual_facts()
    assert(facts['virtualization_type'] == 'guest')
    assert(facts['virtualization_role'] == 'HPVM vPar')
    assert(facts['virtualization_tech_guest'] == set(['HPVM vPar']))
    assert(facts['virtualization_tech_host'] == set())


# Generated at 2022-06-13 04:02:06.500866
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual = HPUXVirtual()
    assert hpux_virtual.platform == 'HP-UX'
    assert hpux_virtual.get_virtual_facts() == {}

# Generated at 2022-06-13 04:02:09.933228
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virt = HPUXVirtual({})
    assert virt.virtualization_type == 'guest'
    assert virt.virtualization_role == 'HP nPar'

# Generated at 2022-06-13 04:02:12.178400
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    module = AnsibleModuleMock()
    hv = HPUXVirtual(module)
    assert hv.platform == 'HP-UX'


# Generated at 2022-06-13 04:02:15.221792
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    module = None
    following_facts = {'virtualization_tech_host': set(),
                       'virtualization_tech_guest': set(),
                       'virtualization_type': '',
                       'virtualization_role': ''}
    assert HPUXVirtual(module).get_virtual_facts() == following_facts

# Generated at 2022-06-13 04:02:18.564995
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module = AnsibleModule(argument_spec={})
    virtual_facts_obj = HPUXVirtual(module)
    virtual_facts = virtual_facts_obj.get_virtual_facts()
    assert virtual_facts['virtualization_type'] in ['host', 'guest']
    assert virtual_facts['virtualization_role'] in ['HP vPar', 'HP nPar', 'HPVM vPar', 'HPVM IVM', 'HPVM']


# Generated at 2022-06-13 04:02:56.438927
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    # create a stub module to pass as class parameter
    module = AnsibleModuleStub()

    # create a stub class for ansible.module_utils.facts.virtual.base.Virtual
    class VirtualStub(object):
        def __init__(self, module):
            self.module = module

        def run_command(self, cmd):
            return (0, '', '')

    class VirtualCollectorStub(object):
        _fact_class = HPUXVirtual
        _platform = 'HP-UX'

    module.AnsibleModuleStub = AnsibleModuleStub
    module.Virtual = VirtualStub
    module.VirtualCollector = VirtualCollectorStub

    virtual_facts = HPUXVirtual(module).get_virtual_facts()
    assert 'virtualization_role' in virtual_facts.keys()

# Generated at 2022-06-13 04:02:58.250453
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    HPUXVirtual()

if __name__ == '__main__':
    test_HPUXVirtual()

# Generated at 2022-06-13 04:02:58.917494
# Unit test for method get_virtual_facts of class HPUXVirtual

# Generated at 2022-06-13 04:03:05.827902
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    """
    This is a unit test for HPUXVirtual class of module facts.virtual.hpux
    """

# Generated at 2022-06-13 04:03:11.270121
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    # Create instance of class HPUXVirtual
    hpux_virtual = HPUXVirtual(module=None)

    # Check for attributes of class
    assert hpux_virtual is not None
    assert hpux_virtual.platform == 'HP-UX'
    assert hpux_virtual.get_virtual_facts() == {'virtualization_tech_guest': set(), 'virtualization_tech_host': set()}

# Generated at 2022-06-13 04:03:20.132721
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    import ansible.module_utils.facts.virtual.hpux_virtual as hpux_virtual
    import tempfile
    import shutil
    import sys

    # Create fakedir
    fakedir = tempfile.mkdtemp()

    # Create fake /usr/sbin/vecheck binary
    open(os.path.join(fakedir, 'usr', 'sbin', 'vecheck'), 'w').close()
    sys.path.insert(0, os.path.join(fakedir, 'usr', 'sbin'))
    hpux_virtual.HPUXVirtual.vecheck_cmd = 'vecheck'

    # Create fake /opt/hpvm/bin/hpvminfo binary
    open(os.path.join(fakedir, 'opt', 'hpvm', 'bin', 'hpvminfo'), 'w').close

# Generated at 2022-06-13 04:03:29.893893
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    # Mock module and module.run_command(cmd)
    module = MockAnsibleModule()
    module.run_command = MockRunCommand()

    # When parstatus exists
    module.run_command.rcs = [0]
    module.run_command.outs = ['TEST OUTPUT']

    # When vecheck exists
    module.run_command.rcs = [0]
    module.run_command.outs = ['TEST OUTPUT']
    HPUXVirtualCollector._platform = 'Linux'
    virtual_collector = HPUXVirtualCollector(module)
    facts = virtual_collector.collect()
    assert facts['virtualization_type'] == 'guest'
    assert facts['virtualization_role'] == 'HP nPar'
    assert facts['virtualization_tech_host'] == set()

# Generated at 2022-06-13 04:03:35.654893
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module = AnsibleModuleMock()
    module.run_command = run_command
    virtual = HPUXVirtual(module)

    # Test 1: OS is HP-UX and there is vecheck script = guest on vPar
    module.run_command.g_os_platform = 'HP-UX'
    module.run_command.g_path = '/usr/sbin/vecheck'
    virtual_facts = virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'guest'
    assert virtual_facts['virtualization_role'] == 'HP vPar'

    # Test 2: OS is HP-UX and there is hpvminfo script = guest on HPVM
    module.run_command.g_os_platform = 'HP-UX'

# Generated at 2022-06-13 04:03:45.314345
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    import sys
    import os
    import stat
    import tempfile
    import shutil

    class MockModule(object):
        def run_command(self, command): return 0, '', ''

    class MockStats(object):
        def __init__(self, st_mode):
            self.st_mode = st_mode

    hpx_virtual = HPUXVirtual(MockModule())

    # set up a temporary directory for testing
    hpx_temp_dir = tempfile.mkdtemp(prefix="ansible_hpx_virtual_testing_")

    # create temporary files to simulate vecheck executable
    os.mkdir(os.path.join(hpx_temp_dir, "usr"))
    os.mkdir(os.path.join(hpx_temp_dir, "usr", "sbin"))

# Generated at 2022-06-13 04:03:49.744482
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module = AnsibleModule(argument_spec=dict())
    hpux_virtual = HPUXVirtual(module=module, platform='HP-UX')
    assert hpux_virtual.get_virtual_facts() == {
        'virtualization_type': 'guest',
        'virtualization_role': 'HP nPar',
        'virtualization_tech_guest': {'HP nPar'},
        'virtualization_tech_host': set()
    }

# Generated at 2022-06-13 04:05:00.006132
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    class MockModule(object):
        def __init__(self, params):
            self.params = params

        def run_command(self, cmd):
            if re.match('.*vecheck.*', cmd):
                if self.params['vecheck'] == 'vpar':
                    return (0, '', '')
                elif self.params['vecheck'] == 'npar':
                    return (1, '', '')
            elif re.match('.*hpvminfo.*', cmd):
                if self.params['hpvminfo'] == 'vpar':
                    return (0, 'Running HPVM vPar', '')
                elif self.params['hpvminfo'] == 'ivm':
                    return (0, 'Running HPVM guest', '')

# Generated at 2022-06-13 04:05:03.079197
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual()
    assert hv.platform == 'HP-UX'

if __name__ == '__main__':
    test_HPUXVirtual()

# Generated at 2022-06-13 04:05:06.781212
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    v = HPUXVirtual({})
    assert v.platform == 'HP-UX'
    assert v.get_virtual_facts() == {'virtualization_tech_host': set(), 'virtualization_tech_guest': set()}


# Generated at 2022-06-13 04:05:08.184215
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual({})
    assert hv._platform == 'HP-UX'


# Generated at 2022-06-13 04:05:10.830107
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    module = MockModule()
    hpx = HPUXVirtual(module)
    assert hpx.platform == 'HP-UX'



# Generated at 2022-06-13 04:05:19.818026
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    import mock

    mock_module = mock.MagicMock()

    mock_module.run_command.side_effect = [
        ## run_command: /usr/sbin/vecheck
        (0, """
/usr/sbin/vecheck: Checking for virtualization: HP vPar
/usr/sbin/vecheck: This is a virtual machine, type HP vPar
""", ""),
        ## run_command: /opt/hpvm/bin/hpvminfo
        (0, """
Virtual Machine name = HVM1
Virtual Machine state = Running
Virtual Machine type = HPVM vPar
""", ""),
        ## run_command: /usr/sbin/parstatus
        (0, """
This is a virtual machine, type HP nPar
""", "")
    ]


# Generated at 2022-06-13 04:05:21.095129
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    h = HPUXVirtual({})
    assert h.platform == 'HP-UX'

# Generated at 2022-06-13 04:05:23.496799
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_obj = HPUXVirtual()
    assert virtual_obj.platform == 'HP-UX'

# Generated at 2022-06-13 04:05:32.117668
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )
    def m_run_command(command):
        if command == "/usr/sbin/vecheck":
            return 0, "", ""
        if command == "/opt/hpvm/bin/hpvminfo":
            return 0, "Running HPVM IVM", ""
        if command == "/usr/sbin/parstatus":
            return 0, "", ""
    module.run_command = m_run_command

    # Patching method exists of class os.path
    def m_exists(path):
        if path == '/usr/sbin/vecheck':
            return True
        if path == '/opt/hpvm/bin/hpvminfo':
            return True

# Generated at 2022-06-13 04:05:42.237823
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    # This test requires that this module has been executed within the context
    # of Ansible's test_runner.py script, i.e. with the working directory set
    # to the root of the Ansible source repository.
    module = HPUXVirtualCollector._create_fake_ansible_module()
    virtual_inst = HPUXVirtual(module)
    virtual_facts = virtual_inst.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'guest'
    assert virtual_facts['virtualization_role'] == 'HP vPar'
    assert virtual_facts['virtualization_tech_guest'] == set(['HP vPar'])
    assert virtual_facts['virtualization_tech_host'] == set()
    assert virtual_facts['virtualization_system'] == ''

# Generated at 2022-06-13 04:07:22.397831
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    facts = {}
    module = AnsibleModule(argument_spec={})

    fact = HPUXVirtual({'module': module, 'ansible_facts': facts})
    result = fact.get_virtual_facts()
    assert result == {'virtualization_tech_guest': set(), 'virtualization_tech_host': set()}


# Generated at 2022-06-13 04:07:24.629943
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module = AnsibleModuleMock()
    h = HPUXVirtual(module)

    assert h.get_virtual_facts() == {
        'virtualization_type': 'guest',
        'virtualization_role': 'HP vPar',
        'virtualization_tech_guest': {'HP vPar'},
        'virtualization_tech_host': set(),
    }


# Generated at 2022-06-13 04:07:29.215949
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    iv = HPUXVirtual({})
    assert iv
    assert iv.platform == 'HP-UX'
    assert iv.get_virtual_facts() == {}


# Generated at 2022-06-13 04:07:38.733879
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    '''Unit test method get_virtual_facts of class Virtual on platform HP-UX'''
    # Simple test
    # Run the method
    _platform = 'HP-UX'
    _fact_class = 'HPUXVirtual'
    _fact_module = __import__(_fact_class, globals(), locals(), [_fact_class], 0)
    _fact_class = getattr(_fact_module, _fact_class)
    vm = _fact_class({},{})
    _virtual_facts = vm.get_virtual_facts()

    # Check that all required keys are present
    assert 'virtualization_type' in _virtual_facts
    assert 'virtualization_role' in _virtual_facts
    assert 'virtualization_tech_guest' in _virtual_facts
    assert 'virtualization_tech_host' in _virtual_

# Generated at 2022-06-13 04:07:41.911734
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    fake_module = FakeModule()
    facts = HPUXVirtual(module=fake_module).get_virtual_facts()
    assert facts['virtualization_type'] == 'guest'
    assert facts['virtualization_role'] == 'HP vPar'
    assert 'HP vPar' in facts['virtualization_tech_host']
    assert 'HP vPar' in facts['virtualization_tech_guest']



# Generated at 2022-06-13 04:07:51.477895
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpux.HPUXVirtual import HPUXVirtual
    from ansible.module_utils.facts.virtual.hpux.HPUXVirtual import test_HPUXVirtual_get_virtual_facts

    # create HP-UXVirtual object with no input parameters
    hpux_virtual = HPUXVirtual(dict(), dict())

    # create mock of method ansible_module.run_command
    def run_command(self, cmd):
        dict = {}
        dict['/usr/sbin/vecheck'] = [0, 'parmgr:  This is a vPar', '']
        dict['/opt/hpvm/bin/hpvminfo'] = [0, 'Running HPVM host', '']

# Generated at 2022-06-13 04:07:57.775923
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpx_pa_risc import HPUXVirtual
    import pytest
    import sys, os
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../')
    sys.path.append(path)
    from ansible.module_utils.facts.virtual import VirtualCollector

    # Testing 'HP Par'
    hpxvirtual = HPUXVirtual()
    hpxvirtual.module.run_command = lambda x: (0, "Running HP-VM guest", '')
    hpxvirtual.module.get_bin_path = lambda x: '/usr/sbin/vecheck'
    virtual_facts = hpxvirtual.get_virtual_facts()

# Generated at 2022-06-13 04:08:06.883401
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts import ModuleFacts
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual, HPUXVirtualCollector
    from ansible.module_utils.facts.virtual.base import Virtual, VirtualCollector
    from ansible.module_utils.facts.system.distribution import Distribution

    class MockModuleUtil():
        def __init__(self):
            self.run_command = lambda x, return_rc=False: (0, '', '')

        def supports_check_mode(self):
            return False

        def exit_json(self, changed=False, ansible_facts=dict()):
            pass

    class MockModuleFacts():
        def __init__(self):
            self.collectors = []

        def populate(self):
            self.collectors

# Generated at 2022-06-13 04:08:13.602212
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    test_module = AnsibleModule(
        argument_spec=dict()
    )
    mock_module = Mock(return_value=test_module)
    mock_ansible_module = HPUXVirtual(mock_module)

    mock_run_command = Mock(return_value=(0, 'test_run_command_output', 'test_run_command_error'))
    mock_ansible_module.module.run_command = mock_run_command

    facts = {}
    assert mock_ansible_module.get_virtual_facts(facts) == {'virtualization_tech_guest': set(), 'virtualization_tech_host': set()}

    mock_run_command.return_value = (0, 'Running HPVM vPar', 'test_run_command_error')
    facts = {}
    assert mock_ans

# Generated at 2022-06-13 04:08:17.187476
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    """ Unit test for method get_virtual_facts of class HPUXVirtual """
    vf = HPUXVirtual()
    facts = vf.get_virtual_facts()
    vf.module.exit_json(changed=False, ansible_facts=facts)

if __name__ == '__main__':
    test_HPUXVirtual_get_virtual_facts()