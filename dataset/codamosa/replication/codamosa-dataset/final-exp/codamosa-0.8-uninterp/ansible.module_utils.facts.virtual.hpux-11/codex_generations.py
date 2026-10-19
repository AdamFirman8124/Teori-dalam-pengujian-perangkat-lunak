

# Generated at 2022-06-13 03:59:37.368339
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    """
    Test get_virtual_facts
    """
    # pylint: disable=no-self-use
    # pylint: disable=too-few-public-methods
    # pylint: disable=protected-access
    import ansible.module_utils.facts.virtual.hpux

    class MockModule():
        def __init__(self, params=None):
            self.params = params
        def fail_json(self, *args, **kwargs):
            raise Exception()
        def run_command(self, cmd):
            if cmd == '/usr/sbin/vecheck':
                return 0, 'a', 'b'
            elif cmd == '/opt/hpvm/bin/hpvminfo':
                return 0, 'Running HPVM guest', 'c'

# Generated at 2022-06-13 03:59:38.925940
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    x = HPUXVirtual({})
    assert x.platform == "HP-UX"


# Generated at 2022-06-13 03:59:40.233378
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    # Check if instance is created
    x = HPUXVirtual()
    assert x

# Generated at 2022-06-13 03:59:43.580667
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    """
    Constructor of class HPUXVirtual
    """
    hpux_virtual = HPUXVirtual(dict())
    assert hpux_virtual.platform == 'HP-UX'

# Generated at 2022-06-13 03:59:45.385698
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    facts = HPUXVirtual({}, {})
    assert facts.platform == 'HP-UX'

# Generated at 2022-06-13 03:59:54.052100
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpux import Virtual, VirtualCollector
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual, HPUXVirtualCollector

    # Create mock module
    class MockModule:
        def __init__(self):
            self.run_command = lambda x: (0, '', '')

    m = MockModule()

    # Test virtualization_type and virtualization_role

    # vecheck, hpvminfo, and parstatus all exist
    # hpvminfo outputs: Running HPVM vPar
    hpux_virtual = HPUXVirtual(m)
    hpux_virtual.get_virtual_facts()
    hpux_virtual.module.run_command = lambda x: (0, 'Running HPVM vPar', '')

# Generated at 2022-06-13 03:59:56.123166
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts = HPUXVirtual(dict())
    assert virtual_facts.platform == 'HP-UX'


# Generated at 2022-06-13 03:59:57.292681
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual()
    assert hv.platform == 'HP-UX'

# Generated at 2022-06-13 04:00:00.473718
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    module = AnsibleModuleMock()
    hpux_virtual_instance = HPUXVirtual(module)
    assert hpux_virtual_instance.platform == 'HP-UX'
    assert hpux_virtual_instance.module == module


# Generated at 2022-06-13 04:00:08.569130
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module_mock = AnsibleModuleMock({})
    h = HPUXVirtual(module_mock)

    # Test case: no virtualization technology
    h.module.run_command = AnsibleRunnerMock(0, "", "")
    virtual_facts = h.get_virtual_facts()
    assert virtual_facts['virtualization_type'].endswith('host')
    assert not virtual_facts['virtualization_tech_host']
    assert not virtual_facts['virtualization_tech_guest']

    # Test case: vPar virtualization technology
    h.module.run_command = AnsibleRunnerMock(0, "HP-UX vPars are enabled on this system.", "")
    virtual_facts = h.get_virtual_facts()

# Generated at 2022-06-13 04:00:16.780843
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    # Todo: write unit test
    pass

# Generated at 2022-06-13 04:00:19.159670
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    module = FakeAnsibleModule()
    hv = HPUXVirtual(module)
    assert hv.platform == 'HP-UX'



# Generated at 2022-06-13 04:00:28.336142
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils.facts.virtual import HPUXVirtual
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtualCollector
    # Prepare test data
    # This is data for VirtualCollector, it should be not changed
    platform_facts = ansible_facts
    platform_facts['ansible_os_family'] = "HP-UX"
    platform_facts['ansible_virtualization_type'] = "guest"
    # This is data for HPUXVirtualCollector, it should be not changed
    hp_ux_virtual_collector = HPUXVirtualCollector()
    hp_ux_virtual_collector.get_all()
    # This is data for HPUXVirtual, it should be changed
    hp_ux

# Generated at 2022-06-13 04:00:30.307237
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    facts = HPUXVirtual({})
    assert facts.platform == 'HP-UX'
    assert facts.virtualization_type is None
    assert facts.virtualization_role is None


# Generated at 2022-06-13 04:00:33.624101
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual()
    assert hv.platform == 'HP-UX'
    assert hv.get_virtual_facts() == dict(virtualization_type=None,
                                            virtualization_role=None,
                                            virtualization_tech_host=set(),
                                            virtualization_tech_guest=set())

# Generated at 2022-06-13 04:00:38.642074
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():

    class MockModule(object):
        def run_command(self, cmd):
            if cmd == "/usr/sbin/vecheck":
                return 0, "", ""
            if cmd == "/usr/sbin/parstatus":
                return 0, "", ""
            if cmd == "/opt/hpvm/bin/hpvminfo":
                return 0, "foo", ""

    def MockRunner(module):
        return MockModule()

    HP = HPUXVirtual(runner=MockRunner)
    assert HP.get_virtual_facts() == {'virtualization_type': 'host',
                                      'virtualization_role': 'HPVM',
                                      'virtualization_tech_guest': {'HPVM', 'HP nPar'},
                                      'virtualization_tech_host': set()}

# Generated at 2022-06-13 04:00:40.172369
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts = HPUXVirtual()
    assert virtual_facts.platform == 'HP-UX'

# Generated at 2022-06-13 04:00:42.880838
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    """Badly written test to confirm get_virtual_facts returns the expected
       tuple
    """
    test_obj = HPUXVirtual()
    assert set(test_obj.get_virtual_facts()) == set(('virtualization_tech_host',
                                                     'virtualization_tech_guest',
                                                     'virtualization_role',
                                                     'virtualization_type'))

# Generated at 2022-06-13 04:00:44.510564
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts = HPUXVirtual()
    assert virtual_facts.platform == 'HP-UX'

# Generated at 2022-06-13 04:00:47.199668
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts = HPUXVirtual({})
    virtualization_type = virtual_facts.get_virtual_facts()['virtualization_type']
    assert virtualization_type == 'unknown'

# Generated at 2022-06-13 04:01:05.542376
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module = FakeModule()
    module.run_command = FakeRunCommand()
    module.run_command.results = {
        "vecheck": (0, "", ""),
        "hpvminfo": (0, "Running HPVM vPar", ""),
        "parstatus": (0, "", "")
    }

    v = HPUXVirtual(module)
    results = v.get_virtual_facts()
    assert results['virtualization_type'] == 'guest'
    assert results['virtualization_role'] == 'HPVM vPar'
    assert results['virtualization_tech_host'] == set(['HPVM'])
    assert results['virtualization_tech_guest'] == set(['HP vPar', 'HPVM vPar', 'HP nPar'])


# Generated at 2022-06-13 04:01:14.726165
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    import platform
    import sys
    import types

    module = types.ModuleType('ansible_test_get_virtual_facts')
    module.run_command = lambda x: (0, '', '')
    module.params = {}
    sys.modules['ansible_test_get_virtual_facts'] = module

    hpux_virtual = HPUXVirtual(module)
    result = hpux_virtual.get_virtual_facts()

    # If the underlying platform is not HPUX, then the result will be an
    # empty dictionary.
    if platform.system().lower() == 'hp-ux':
        assert result is not {}
        assert result['virtualization_type'] == 'guest'
        assert result['virtualization_role'] == 'HP vPar'

# Generated at 2022-06-13 04:01:17.698829
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    v = HPUXVirtual({'module_setup': True})
    assert v.platform == 'HP-UX'


# Generated at 2022-06-13 04:01:18.601316
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    assert HPUXVirtual().platform == 'HP-UX'

# Generated at 2022-06-13 04:01:19.712499
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    v = HPUXVirtual()
    assert v.platform == 'HP-UX'

# Generated at 2022-06-13 04:01:23.431316
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts import Facts

    mock_module = Facts(
        dict(
            command_parser=dict(
                module_args=''
            )
        )
    )

    mock_virtual = HPUXVirtual(mock_module)

    # Test get_virtual_facts()
    result = mock_virtual.get_virtual_facts()
    assert result == {'virtualization_tech_guest': set(['HP vPar']),
                      'virtualization_tech_host': set([]),
                      'virtualization_type': 'guest',
                      'virtualization_role': 'HP vPar'
                     }

# Generated at 2022-06-13 04:01:26.608383
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual()
    assert hv.platform == 'HP-UX'
    assert hv.virtualization_type == {}
    assert hv.virtualization_role == {}

# Generated at 2022-06-13 04:01:29.636711
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    fact_class = HPUXVirtual(dict(module=None))
    assert fact_class.platform == 'HP-UX'
    assert fact_class.get_virtual_facts() == {}


# Generated at 2022-06-13 04:01:40.468995
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    """
    HPUXVirtual_get_virtual_facts() returns a dict of virtual facts
    """
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual
    from ansible.module_utils._text import to_text

    class FakeModule(object):
        def __init__(self):
            self.run_command_environ_update = dict()

        def run_command(self, command):
            rc = 0
            err = ''
            if command == "/usr/sbin/vecheck":
                out = 'Virtualization technology is enabled on this system'
            elif command == "/opt/hpvm/bin/hpvminfo":
                out = ' Running as HPVM vPar'

# Generated at 2022-06-13 04:01:45.750831
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.collector import FactsCollector
    from ansible.module_utils.facts.virtual.hpu_virtual import HPUXVirtual
    from ansible.module_utils.facts.virtual.hpu_virtual import HPUXVirtualCollector

    my_collector = FactsCollector()
    my_virtual = HPUXVirtual()

    for cls in [HPUXVirtual, HPUXVirtualCollector, my_virtual, my_virtual._fact_class]:
        assert cls.platform == 'HP-UX'
        my_virtual.get_virtual_facts()


# Generated at 2022-06-13 04:02:17.652447
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts_dict = {'virtualization_type': 'guest', 'virtualization_role': 'HP nPar'}
    h = HPUXVirtual(None, virtual_facts_dict)
    assert h.get_virtual_facts()['virtualization_type'] == 'guest'
    assert h.get_virtual_facts()['virtualization_role'] == 'HP nPar'


# Generated at 2022-06-13 04:02:20.680167
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():

    hpux_virtual = HPUXVirtual(None)
    assert hpux_virtual.platform == 'HP-UX'
    assert hpux_virtual.get_virtual_facts() == {'virtualization_type': None,
                                                'virtualization_role': None,
                                                'virtualization_tech_guest': set(),
                                                'virtualization_tech_host': set(),
                                                }

# Generated at 2022-06-13 04:02:25.881224
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils import basic
    from ansible.module_utils.facts import collector

    m = basic.AnsibleModule(argument_spec={}, supports_check_mode=True)
    virtual = HPUXVirtual(m)
    assert ('guest' == virtual.facts['virtualization_type'])
    assert ('HPVM IVM' == virtual.facts['virtualization_role'])



# Generated at 2022-06-13 04:02:32.948501
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    def run_command(self, cmd):
        if cmd == "/usr/sbin/vecheck":
            return (0, "", "")
        if cmd == "/opt/hpvm/bin/hpvminfo":
            return (0, "Running state of HPVM vPar is normal", "")
        if cmd == "/usr/sbin/parstatus":
            return (0, "", "")
        return (0, "", "")

    module = type('', (), {})()
    module.run_command = run_command
    hpux_virtual = HPUXVirtual(module)
    virtual_facts = hpux_virtual.get_virtual_facts()
    assert(virtual_facts['virtualization_type'] == 'guest')
    assert(virtual_facts['virtualization_role'] == 'HPVM vPar')


#

# Generated at 2022-06-13 04:02:35.241689
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux = HPUXVirtual({})
    assert hpux.platform == 'HP-UX'
    assert hpux.get_virtual_facts() == {}


# Generated at 2022-06-13 04:02:36.141017
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpar = HPUXVirtual({})
    assert hpar is not None

# Generated at 2022-06-13 04:02:40.000918
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual import HPUXVirtual
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.basic import AnsibleModule
    h = HPUXVirtual(AnsibleModule)
    facts = h.get_virtual_facts()
    assert facts['virtualization_role'] in ['guest', None]
    assert facts['virtualization_type'] in ['guest', None]

# Generated at 2022-06-13 04:02:41.532960
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpuxvirtual = HPUXVirtual()
    assert hpuxvirtual.platform == 'HP-UX'


# Generated at 2022-06-13 04:02:46.568870
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    """
    Unit test for method get_virtual_facts of class HPUXVirtual
    """
    hpxv = HPUXVirtual(None)
    fake_module = O
    hpxv.module = fake_module
    hpxv.module.run_command = mock_run_command

    # virtualization_type: guest; virtualization_role: HPVM vPar
    rc = 0
    out = 'Running as HPVM vPar.'
    err = ''
    mock_run_command.side_effect = [(rc, out, err), ]
    fake_module.get_bin_path = lambda arg: arg
    virtual_facts = hpxv.get_virtual_facts()
    assert virtual_facts['virtualization_tech_guest'] == {'HPVM vPar'}

# Generated at 2022-06-13 04:02:54.743546
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    output1 = "hp_vpar_vm_linux"
    v = HPUXVirtual({}, output1)
    assert v._get_virtual_facts()['virtualization_type'] == 'guest'
    assert v._get_virtual_facts()['virtualization_role'] == 'HP vPar'
    assert v._get_virtual_facts()['virtualization_tech_host'] == set()
    assert v._get_virtual_facts()['virtualization_tech_guest'] == set(['HP vPar'])

    output2 = "hp_vm_vm_linux"
    v = HPUXVirtual({}, output2)
    assert v._get_virtual_facts()['virtualization_type'] == 'guest'
    assert v._get_virtual_facts()['virtualization_role'] == 'HPVM vPar'

# Generated at 2022-06-13 04:03:23.341114
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual({})
    assert hv.platform == 'HP-UX'

# Generated at 2022-06-13 04:03:25.463600
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    v = HPUXVirtual()
    #assert v._platform == "HP-UX"

# Generated at 2022-06-13 04:03:27.299627
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpx_virtual = HPUXVirtual(dict(module=dict()))
    assert hpx_virtual.platform == 'HP-UX'

# Generated at 2022-06-13 04:03:29.114003
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts = HPUXVirtual(dict())
    assert virtual_facts.platform == 'HP-UX'


# Generated at 2022-06-13 04:03:32.705682
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_fact_class_obj = HPUXVirtual()
    actual_result = virtual_fact_class_obj.get_virtual_facts()
    expected_result = {'virtualization_type': '',
                       'virtualization_role': '',
                       'virtualization_tech_guest': set([]),
                       'virtualization_tech_host': set([])}

    assert actual_result == expected_result

# Generated at 2022-06-13 04:03:43.572206
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    import tempfile

    f = tempfile.NamedTemporaryFile()
    parstatus_file = f.name

    ansible_included_virtual_facts_with_vecheck = {
        "virtualization_type": "guest",
        "virtualization_role": "HP vPar",
        "virtualization_tech_host": set([]),
        "virtualization_tech_guest": set(["HP vPar"])
    }
    ansible_included_virtual_facts = {
        "virtualization_type": "guest",
        "virtualization_role": "HP nPar",
        "virtualization_tech_host": set([]),
        "virtualization_tech_guest": set(["HP nPar"])
    }

# Generated at 2022-06-13 04:03:45.277796
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual = HPUXVirtual()
    assert virtual.platform == 'HP-UX'
    assert virtual.get_virtual_facts() is not None

# Generated at 2022-06-13 04:03:46.904838
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    x = HPUXVirtual()
    assert x.platform == 'HP-UX'
    assert x._platform == 'HP-UX'



# Generated at 2022-06-13 04:03:47.897211
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virt = HPUXVirtual()
    assert virt.platform == 'HP-UX'

# Generated at 2022-06-13 04:03:48.997697
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    fact_class = HPUXVirtual
    print(fact_class.platform, fact_class.get_virtual_facts())

# Generated at 2022-06-13 04:04:48.592858
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils import basic
    module = basic.AnsibleModule(
        argument_spec = dict()
    )
    module.run_command = run_command
    hpux_virtual = HPUXVirtual(module)
    virtual_facts = hpux_virtual.get_virtual_facts()
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts


# Generated at 2022-06-13 04:04:59.432874
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    host_virtual = HPUXVirtualCollector(None).collect()['ansible_facts']['ansible_virtualization_facts']
    assert os.path.exists('/usr/sbin/parstatus') or os.path.exists('/usr/sbin/vecheck') or os.path.exists('/opt/hpvm/bin/hpvminfo')
    assert not (os.path.exists('/usr/sbin/parstatus') and os.path.exists('/usr/sbin/vecheck'))
    if host_virtual['virtualization_type'] == 'guest':
        assert host_virtual['virtualization_type'] != 'host'
        assert re.match('.*Virtualization.*', host_virtual['virtualization_role'])

# Generated at 2022-06-13 04:05:07.375381
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    '''
    Unit test for constructor of class HPUXVirtual
    '''
    # Test with valid argument
    HPUXVirtual(dict())

    # Test with invalid argument
    try:
        HPUXVirtual('')
    except TypeError as e:
        assert 'argument must be a dictionary' in str(e)
    try:
        HPUXVirtual(12.0)
    except TypeError as e:
        assert 'argument must be a dictionary' in str(e)
    try:
        HPUXVirtual([])
    except TypeError as e:
        assert 'argument must be a dictionary' in str(e)
    try:
        HPUXVirtual(())
    except TypeError as e:
        assert 'argument must be a dictionary' in str(e)

# Generated at 2022-06-13 04:05:10.991827
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    facts_mock = {}
    module_mock = AnsibleModule(argument_spec = dict())
    virtual = HPUXVirtual(module=module_mock)
    assert virtual.get_virtual_facts() == facts_mock


# Generated at 2022-06-13 04:05:12.493363
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    obj = HPUXVirtual({})
    assert obj.platform == 'HP-UX'



# Generated at 2022-06-13 04:05:21.095861
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.HPUX_hp_vm import HPUXVirtual

    C = HPUXVirtual()
    VF = C.get_virtual_facts()

    assert 'virtualization_type' in VF
    assert 'virtualization_role' in VF

    assert 'virtualization_tech_guest' in VF
    assert 'virtualization_tech_host' in VF

    assert VF['virtualization_tech_host'] == set()

    assert len(VF['virtualization_tech_guest']) <= 3
    assert 'HP nPar' in VF['virtualization_tech_guest']
    assert 'HP vPar' in VF['virtualization_tech_guest']

# Generated at 2022-06-13 04:05:23.869663
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual = HPUXVirtual(dict(module=None))
    assert hpux_virtual.get_virtual_facts() is not None

# Generated at 2022-06-13 04:05:26.691392
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual()
    assert hv.get_virtual_facts()['virtualization_type'] == 'guest'
    assert hv.get_virtual_facts()['virtualization_role'] == 'HP vPar'

# Generated at 2022-06-13 04:05:31.010854
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual = HPUXVirtual(dict())
    assert hpux_virtual.get_virtual_facts() == {'virtualization_type': 'guest',
                                                'virtualization_role': 'HP vPar',
                                                'virtualization_tech_guest': set(['HP vPar']),
                                                'virtualization_tech_host': set()}

# Generated at 2022-06-13 04:05:34.395505
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    """
    Test class HPUXVirtual constructor, assuming default OS (HP-UX)
    """
    h = HPUXVirtual(dict(module=dict()))
    assert h.virtualization_type == 'unknown'
    assert h.virtualization_role == 'unknown'
    assert h.virtualization_tech_guest == set()
    assert h.virtualization_tech_host == set()

# Generated at 2022-06-13 04:07:04.635838
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts = HPUXVirtual()
    assert virtual_facts.platform == 'HP-UX'
    assert virtual_facts.is_guest is None
    assert virtual_facts.is_hypervisor is None


# Generated at 2022-06-13 04:07:11.181360
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module = mock.MagicMock()
    module.run_command = mock.MagicMock()

    class HPUXVirtual(HPUXVirtual):
        def __init__(self, module):
            self.module = module

    virtual_collector = HPUXVirtual(module)

    # Test vPar
    module.run_command.return_value = (0, "", "")
    rc, out, err = virtual_collector.get_virtual_facts()
    assert rc['virtualization_type'] == 'guest'
    assert rc['virtualization_role'] == 'HP vPar'
    assert rc['virtualization_tech_guest'] == set(['HP vPar'])
    assert rc['virtualization_tech_host'] == set([])

    # Test vPar

# Generated at 2022-06-13 04:07:13.953787
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual = HPUXVirtual({})
    assert isinstance(hpux_virtual, HPUXVirtual)
    assert hpux_virtual.platform == 'HP-UX'
    assert hpux_virtual.get_virtual_facts() == {}



# Generated at 2022-06-13 04:07:17.167198
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    module = AnsibleModule(argument_spec={})
    my_HPUXVirtual_obj = HPUXVirtual(module)
    assert repr(my_HPUXVirtual_obj) == "<HPUXVirtual(result={}, module='ansible.modules.system.hp_hardware.HPUXVirtual', sys_path=['/usr/sbin', '/usr/bin', '/sbin', '/bin'], result_dict=None, virtual_facts={})>"

# Generated at 2022-06-13 04:07:18.596864
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    v = HPUXVirtual({})
    assert v

# Generated at 2022-06-13 04:07:20.588841
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts = HPUXVirtual({})
    assert virtual_facts.platform == 'HP-UX'



# Generated at 2022-06-13 04:07:26.615117
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.six import PY2
    from ansible.module_utils.facts.collector.base import BaseFactCollector
    from ansible.module_utils.facts.virtual.hpu import HPUXVirtual
    from ansible.module_utils.facts.virtual.hpu import HPUXVirtualCollector
    from ansible.module_utils.facts.virtual.hpu import test_HPUXVirtual_get_virtual_facts
    from ansible.module_utils.facts.virtual.hpu import VirtualHPUXModule
    class MockModule(object):

        def __init__(self):
            self.params = {}
            self.called = None
            self.run_command = self.mock_run_command

        def mock_run_command(self, command):
            self.called = command
           

# Generated at 2022-06-13 04:07:32.728771
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():  # pylint: disable=too-many-locals
    """Unit test for constructor of class HPUXVirtual"""
    module = AnsibleModuleDummy()
    virtual = HPUXVirtual(module)
    virtual_facts_expected = {
        'virtualization_type': 'guest',
        'virtualization_role': 'HPVM vPar',
        'virtualization_tech_guest': set(['HPVM vPar']),
        'virtualization_tech_host': set([]),
    }

    module.run_command.return_value = (0, "Running HPVM vPar", None)
    virtual_facts = virtual.get_virtual_facts()
    assert virtual_facts == virtual_facts_expected
    assert module.run_command.call_count == 1

    module.run_command.return_value = False
   

# Generated at 2022-06-13 04:07:41.369581
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpu import HPUXVirtual
    from ansible.module_utils.facts.virtual.hpu import HPUXVirtualCollector
    from ansible.module_utils import basic
    module = basic.AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    if module._debug:
        module.debug('Test setup done')
        module.exit_json(changed=False)

    test_HPUXVirtual = HPUXVirtual(module)
    test_HPUXVirtualCollector = HPUXVirtualCollector(module)
    test_HPUXVirtualCollector.collect()
    test_virtual_facts = test_HPUXVirtual.get_virtual_facts()


# Generated at 2022-06-13 04:07:45.807112
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpuv = HPUXVirtual()
    assert hpuv.platform == 'HP-UX'
    # hpuv.get_virtual_facts()