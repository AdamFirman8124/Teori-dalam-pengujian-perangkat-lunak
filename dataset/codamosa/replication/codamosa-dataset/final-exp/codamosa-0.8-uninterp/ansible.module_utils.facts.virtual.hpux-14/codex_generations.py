

# Generated at 2022-06-13 03:59:31.713806
# Unit test for method get_virtual_facts of class HPUXVirtual

# Generated at 2022-06-13 03:59:34.811770
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():  # pylint: disable=too-many-public-methods
    module = FakeAnsibleModule()
    obj = HPUXVirtual(module)
    assert obj.platform == 'HP-UX'


# Unit test class for HP-UX Virtual VirtualCollector

# Generated at 2022-06-13 03:59:37.905026
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    host_facts = {'kernel': 'HP-UX'}
    host_virtual = HPUXVirtual(host_facts, None)
    assert host_virtual.platform == 'HP-UX'
    assert host_virtual.get_virtual_facts() == host_facts


# Generated at 2022-06-13 03:59:47.354084
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    # empty input
    input = {}
    v = HPUXVirtual(input)
    output = v.get_virtual_facts()
    assert output['virtualization_role'] is None
    assert output['virtualization_type'] is None
    assert output['virtualization_tech_guest'] == set()
    assert output['virtualization_tech_host'] == set()

    # Host

# Generated at 2022-06-13 03:59:55.642807
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    module = MockModule()
    hpux_virtual = HPUXVirtual(module)

    assert hpux_virtual.virtual_facts['virtualization_type'] == 'guest'
    assert hpux_virtual.virtual_facts['virtualization_role'] == 'HP vPar'

    assert ('HP vPar' in hpux_virtual.virtual_facts['virtualization_tech_guest'])
    assert ('HP nPar' in hpux_virtual.virtual_facts['virtualization_tech_guest'])
    assert ('HPVM vPar' in hpux_virtual.virtual_facts['virtualization_tech_guest'])
    assert ('HPVM IVM' in hpux_virtual.virtual_facts['virtualization_tech_guest'])

# Generated at 2022-06-13 03:59:58.664068
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual(dict())
    assert hv._platform == 'HP-UX'
    assert hv.virtualization_type == 'unknown'
    assert hv.virtualization_role == 'unknown'
    assert hv.virtualization_system == 'Unknown'

# Generated at 2022-06-13 04:00:02.677105
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpuxtest import FakeModule
    
    virtual = HPUXVirtual(FakeModule())
    facts = virtual.get_virtual_facts()
    assert 'virtualization_type' in facts.keys()
    assert 'virtualization_role' in facts.keys()

# Generated at 2022-06-13 04:00:09.771522
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    fixtures_path = os.path.join(os.path.dirname(__file__), 'fixtures')
    output = {}

    test_obj = HPUXVirtual(module=None)

    # 1. Test for vecheck
    output[0] = 'root@hpux~$ /usr/sbin/vecheck\nVPAR is installed\n'
    test_obj.module.run_command = lambda x: (0, output[0], '')
    virtual_facts = test_obj.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'guest'
    assert virtual_facts['virtualization_role'] == 'HP vPar'

    # 2. Test for hpvminfo

# Generated at 2022-06-13 04:00:15.283168
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():

    # Create instance of class HPUXVirtualCollector and call get_virtual_facts method
    hpu_vc = HPUXVirtualCollector()
    hpu_vc.get_virtual_facts()

    # Create instance of class HPUXVirtual
    hpu_v = HPUXVirtual()

    # Assert that object of class HPUXVirtual
    assert isinstance(hpu_v, HPUXVirtual)

# Generated at 2022-06-13 04:00:24.506259
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    # This is the return value of Virtual.is_virtual function
    # if running on virtual machine. It is a mock up.
    is_virtual = True
    # This is the return value of Virtual.run_command function
    # if running on virtual machine. It is a mock up.
    rc_out_err = (0, '', '')
    # This is a auto generated return value for get_virtual_facts function
    # of class HPUXVirtual under test.
    vecheck = HPUXVirtual._get_virtual_facts(HPUXVirtual,
                                             is_virtual,
                                             rc_out_err)
    assert vecheck['virtualization_type'] == 'guest'
    assert vecheck['virtualization_role'] == 'HP vPar'

# Generated at 2022-06-13 04:00:42.390672
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual

    h = HPUXVirtual({})
    result = h.get_virtual_facts()
    assert result['virtualization_tech_guest'] == set([])
    assert result['virtualization_tech_host'] == set([])

    h.module.run_command = lambda x: (1, '', '')
    result = h.get_virtual_facts()
    assert result['virtualization_tech_guest'] == set([])
    assert result['virtualization_tech_host'] == set([])

    h.module.run_command = lambda x: (0, 'Running HPVM vPar', '')
    result = h.get_virtual_facts()

# Generated at 2022-06-13 04:00:45.715293
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():

    virtual_hpu = HPUXVirtual()
    if virtual_hpu._platform != "HP-UX":
        raise AssertionError()
    if virtual_hpu._fact_class.platform != "HP-UX":
        raise AssertionError()

# Generated at 2022-06-13 04:00:47.461682
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux = HPUXVirtual()
    assert hpux.platform == 'HP-UX'


# Generated at 2022-06-13 04:00:48.734319
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpu_virtual_ins = HPUXVirtual()
    assert hpu_virtual_ins.platform == 'HP-UX'


# Generated at 2022-06-13 04:00:50.659952
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    v = HPUXVirtual()
    assert v.platform == 'HP-UX'



# Generated at 2022-06-13 04:00:52.117305
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_obj = HPUXVirtual()
    assert virtual_obj.platform == 'HP-UX'


# Generated at 2022-06-13 04:00:53.739415
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    v = HPUXVirtualCollector.fetch_virtual_facts()
    assert isinstance(v, dict)
    assert 'virtualization_type' in v

# Generated at 2022-06-13 04:01:01.436506
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    expected_result = {
        'virtualization_type': 'guest',
        'virtualization_role': 'HP nPar',
        'virtualization_tech_host': set(),
        'virtualization_tech_guest': set(['HP nPar']),
    }
    hpux_virtual = HPUXVirtual(dict(module=None), None)
    facts_result = hpux_virtual.get_virtual_facts()
    assert facts_result == expected_result

# Generated at 2022-06-13 04:01:02.991606
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    module = AnsibleModule({})
    hv = HPUXVirtual(module)
    assert hv.platform == 'HP-UX'

# Generated at 2022-06-13 04:01:08.687858
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    test = HPUXVirtual()
    assert test.platform == 'HP-UX'
    assert test.get_virtual_facts() == {
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set(),
        'virtualization_type': '',
        'virtualization_role': '',
    }


# Generated at 2022-06-13 04:01:22.442332
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    assert HPUXVirtual.platform == 'HP-UX'

# Generated at 2022-06-13 04:01:25.581849
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    test_obj = HPUXVirtual({})
    virtual_facts = test_obj.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'guest'
    assert virtual_facts['virtualization_role'] == 'HP nPar'
    guest_tech = set(['HPVM guest', 'HPVM host', 'HP vPar', 'HP nPar'])
    host_tech = set()
    assert virtual_facts['virtualization_tech_guest'] == guest_tech
    assert virtual_facts['virtualization_tech_host'] == host_tech

# Generated at 2022-06-13 04:01:29.059690
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    v = HPUXVirtual({})
    assert v.platform == 'HP-UX'
    assert v.guest_facts == set()
    assert v.host_facts == set()


# Generated at 2022-06-13 04:01:31.945359
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual({})
    assert hv.platform == 'HP-UX'
    assert hv.type == 'guest'

# Generated at 2022-06-13 04:01:34.993940
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts = HPUXVirtual({})
    assert isinstance(virtual_facts, dict)

if __name__ == '__main__':
    test_HPUXVirtual()

# Generated at 2022-06-13 04:01:37.960931
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual = HPUXVirtual()
    assert hpux_virtual.platform == 'HP-UX'
    assert hpux_virtual.get_virtual_facts() == {}



# Generated at 2022-06-13 04:01:45.535047
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual
    from ansible.module_utils.facts.virtual.hpux import VirtualCollector

    hpux = HPUXVirtual()
    collector = VirtualCollector()

    class ModuleStub:
        def __init__(self):
            self._module = {}
            self._module['virtual_facts'] = {}
        def run_command(self, command, check_rc=True, close_fds=True, executable=None, data=None):
            if command == '/usr/sbin/vecheck':
                return (0, '', '')
            elif command == '/opt/hpvm/bin/hpvminfo':
                return (0, 'HPVM', '')

# Generated at 2022-06-13 04:01:53.469353
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.utils.path import find_binary
    import ansible.module_utils.facts.virtual.hpux
    path = find_binary('cat')
    module = get_module_mock()
    module.run_command = get_cmd_data(path, 'cat', 'cat', 'Linux')
    hpux_instance = ansible.module_utils.facts.virtual.hpux.HPUXVirtual(module)
    hpux_instance_return = hpux_instance.get_virtual_facts()
    print("hpux_instance_return is %s" % hpux_instance_return)


# Generated at 2022-06-13 04:01:59.602253
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    hpu = HPUXVirtual()

    assert hpu.get_virtual_facts() == {
        'virtualization_type': 'host',
        'virtualization_role': 'HPVM',
        'virtualization_tech_guest': {'HPVM'},
        'virtualization_tech_host': set()
    }

    hpu.module.run_command = lambda a, check_rc=False: (0, '', '')
    hpu.module.get_bin_path = lambda a: True
    assert hpu.get_virtual_facts() == {
        'virtualization_type': 'guest',
        'virtualization_role': 'HP nPar',
        'virtualization_tech_guest': {'HP nPar'},
        'virtualization_tech_host': set()
    }

# Generated at 2022-06-13 04:02:01.456477
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    virtual = HPUXVirtual({})
    virtual._module = Dummy()
    virtual._module.run_command = Dummy()
    virtual.get_virtual_facts()

# Generated at 2022-06-13 04:02:19.818792
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.collector.virtual.hpu_x import HPUXVirtual
    from ansible.module_utils.facts.collector.virtual.tests.test_hpu_x import (
        FakeHPUXModule
    )

    # Create instance of FakeModule
    fake_module = FakeHPUXModule()

    # Create instance of HPUXVirtual
    hpu_xvirtual = HPUXVirtual(module=fake_module)

    # Test when /usr/sbin/vecheck exists and vecheck returns HP vPar as running
    fake_module.run_command = lambda x: [0, 'Running HP vPar', '']
    fake_module.file_exists = lambda x: True
    virtual_facts = hpu_xvirtual.get_virtual_facts()

# Generated at 2022-06-13 04:02:27.553590
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts = HPUXVirtual()
    assert isinstance(virtual_facts, dict)
    assert isinstance(virtual_facts['virtualization_type'], str) or \
        virtual_facts['virtualization_type'] == None
    assert isinstance(virtual_facts['virtualization_role'], str) or \
        virtual_facts['virtualization_role'] == None
    assert isinstance(virtual_facts['virtualization_tech_host'], set) or \
        virtual_facts['virtualization_tech_host'] == None
    assert isinstance(virtual_facts['virtualization_tech_guest'], set) or \
        virtual_facts['virtualization_tech_guest'] == None

# Generated at 2022-06-13 04:02:29.550449
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts = HPUXVirtual(dict(module=None))
    assert virtual_facts.platform == 'HP-UX'

# Generated at 2022-06-13 04:02:34.602690
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts import fact_cache
    from ansible.module_utils.facts.virtual import HPUXVirtual as HPUXVirtualModuleUtils

    m = HPUXVirtualModuleUtils()

    # Test when /usr/sbin/vecheck exists
    fact_cache.FACT_CACHE['virtual'] = {}
    m.module.run_command = lambda x: (0, '', '')
    m.module.get_bin_path = lambda x: '/usr/sbin/' + x
    m.get_virtual_facts()
    assert fact_cache.FACT_CACHE['virtual']['virtualization_type'] == 'guest'
    assert fact_cache.FACT_CACHE['virtual']['virtualization_role'] == 'HP vPar'

# Generated at 2022-06-13 04:02:42.817762
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    """
    Test method get_virtual_facts of class HPUXVirtual
    """
    module = FakeModule()
    # Test with no installed virtualization technology
    virtual = HPUXVirtual(module)
    virtual_facts = virtual.get_virtual_facts()
    assert virtual_facts['virtualization_tech_guest'] == set()
    assert virtual_facts['virtualization_tech_host'] == set()

    # Test with HP vPar installed
    module.run_command.return_value = (0, "HP vPar installed", None)
    virtual = HPUXVirtual(module)
    virtual_facts = virtual.get_virtual_facts()
    assert virtual_facts['virtualization_tech_guest'] == set(['HP vPar'])
    assert virtual_facts['virtualization_tech_host'] == set()
    assert virtual

# Generated at 2022-06-13 04:02:46.507387
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts = HPUXVirtual()
    assert virtual_facts._platform == 'HP-UX'
    assert virtual_facts._fact_class is HPUXVirtual

# Generated at 2022-06-13 04:02:48.396350
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual({})
    assert hv.platform == 'HP-UX'



# Generated at 2022-06-13 04:02:52.966351
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    module = type('MockModule', (object, ), {'run_command': lambda args, check_rc=True: (0, 'output', '')})
    fake_module = module()
    facts = HPUXVirtual(fake_module).get_virtual_facts()
    assert facts['virtualization_type'] == 'guest'
    assert facts['virtualization_role'] == 'HP vPar'

# Generated at 2022-06-13 04:02:56.131121
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    h = HPUXVirtualCollector(None)
    assert h.guest == set()
    assert h.host == set()

# Generated at 2022-06-13 04:02:59.113208
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    vv = HPUXVirtual({})
    assert vv.platform == 'HP-UX'
    assert vv.get_virtual_facts() == {'virtualization_tech_host': set(),
                                      'virtualization_tech_guest': set()}

# Generated at 2022-06-13 04:03:28.782251
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual = HPUXVirtual({}, {})
    assert hpux_virtual.platform == 'HP-UX'


# Generated at 2022-06-13 04:03:39.802024
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module = FakeModule()
    module.run_command = FakeRunCommand
    obj = HPUXVirtual(module)

    # check function returns correct virtual facts if vecheck exists
    module.stat = {'/usr/sbin/vecheck': (1, 2, 3)}
    assert obj.get_virtual_facts() == {'virtualization_type': 'guest', 'virtualization_role': 'HP vPar', 'virtualization_tech_host': set(), 'virtualization_tech_guest': set(['HP vPar'])}

    # check function returns correct virtual facts if hpvminfo exists and guest
    module.stat = {'/usr/sbin/vecheck': (0, 0, 0)}
    module.stat = {'/opt/hpvm/bin/hpvminfo': (1, 2, 3)}
    assert obj.get

# Generated at 2022-06-13 04:03:42.445087
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    h = HPUXVirtual({})
    assert h.platform == 'HP-UX'
    assert h.get_virtual_facts() is None

# Generated at 2022-06-13 04:03:49.437686
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    """
    Test that the code runs without raising Exceptions and correct facts are returned
    :return:
    """
    vecheck_content = """
        #
        # Support for virtualization:
        #
        #   Supported on this system:       Yes
        #   Support for HP-UX partitions:   Yes
        #   Support for containers:         Yes
        #   Support for HPVM Software:      No
        #
        # ==================================================
        # HPVM:
        #
        # HPVM is not installed on this system.
        #
        # ==================================================
        # Containers:
        #
        # There are no active containers on this system.
        #
        # ==================================================
        # Partitions:
        #
        # No active partitions on this system.
        #
        # ==================================================
        """

    hpvmin

# Generated at 2022-06-13 04:03:56.465713
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts = {'virtualization_type': 'host', 'virtualization_role': 'host'}

    hpux_virtual = HPUXVirtual(module=None)
    host_tech = hpux_virtual.host_tech()
    guest_tech = hpux_virtual.guest_tech()
    facts = hpux_virtual.get_virtual_facts()
    assert not len(host_tech)
    assert not len(guest_tech)
    assert 'virtualization_type' not in facts
    assert 'virtualization_role' not in facts

# Generated at 2022-06-13 04:04:01.883142
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual = HPUXVirtual(dict())
    assert hpux_virtual.platform == 'HP-UX'
    assert hpux_virtual.virtualization_type is None
    assert hpux_virtual.virtualization_role is None
    assert hpux_virtual.virtualization_tech_host == set()
    assert hpux_virtual.virtualization_tech_guest == set()

# Generated at 2022-06-13 04:04:04.707608
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual = HPUXVirtual({})
    assert virtual.guest_virtual_facts == None
    assert virtual.host_virtual_facts == None
    assert virtual.virtual_facts == {}
    assert virtual.virtual_facts_string == "TBD"


# Generated at 2022-06-13 04:04:13.513288
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    import ansible.module_utils.facts.virtual.hpux
    import ansible.module_utils.facts.virtual.base
    import ansible.module_utils.facts.virtual.linux
    import ansible.module_utils.facts.virtual.xen
    import ansible.module_utils.facts.virtual.kvm
    import ansible.module_utils.facts.virtual.openvz
    import ansible.module_utils.facts.virtual.parallels
    import ansible.module_utils.facts.virtual.vmware
    import sys
    import tempfile
    import ansible.module_utils.netutils
    import ansible.module_utils.network.common.utils

    class ModuleStub():
        def __init__(self):
            self.debug_msgs = []
            self.params = []

# Generated at 2022-06-13 04:04:16.897596
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    parsed_facts = dict(
        virtualization_type='guest',
        virtualization_role='HPVM guest',
        virtualization_technologies=[
            'HPVM guest',
        ],
    )
    facts = dict(
        ansible_virtual=dict(
        )
    )
    c = HPUXVirtual(dict(module=None, facts=facts))
    virtual_facts = c.get_virtual_facts()
    assert virtual_facts == parsed_facts

# Generated at 2022-06-13 04:04:18.958510
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    facts = HPUXVirtual(None).get_virtual_facts()
    assert 'virtualization_type' not in facts


# Generated at 2022-06-13 04:04:51.105341
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    h = HPUXVirtual()
    assert h.platform == 'HP-UX'

# Generated at 2022-06-13 04:05:00.056701
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module = AnsibleModule(
        argument_spec=dict()
    )

    if not HP_UX_VIRTUAL_FACT_DATA:
        module.exit_json(changed=False, ansible_facts=dict())

    fake_module = FakeAnsibleModule(module)
    hpux_virtual_obj = HPUXVirtual(fake_module)
    fake_module.run_command.return_value = HP_UX_VIRTUAL_FACT_DATA[0]
    facts = hpux_virtual_obj.get_virtual_facts()
    assert facts == HP_UX_VIRTUAL_FACT_DATA[1]


# Generated at 2022-06-13 04:05:04.406676
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpx_v = HPUXVirtual(dict())
    assert hpx_v.platform == 'HP-UX'
    assert hpx_v.get_virtual_facts() == {
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set()
    }


# Generated at 2022-06-13 04:05:06.017893
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual({})
    assert hv.platform == 'HP-UX'

# Generated at 2022-06-13 04:05:08.146504
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():

    virtual_facts = HPUXVirtual()
    assert virtual_facts.module == None
    assert virtual_facts._collector_class == HPUXVirtualCollector


# Generated at 2022-06-13 04:05:14.760005
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    obj = HPUXVirtual()
    obj._module = MockModule()
    obj._module.run_command.return_value = 0, '', ''
    virtual_facts = obj.get_virtual_facts()
    assert virtual_facts['virtualization_type'] is None
    assert virtual_facts['virtualization_role'] is None
    assert virtual_facts['virtualization_tech_guest'] == set()
    assert virtual_facts['virtualization_tech_host'] == set()

# Mock class for module

# Generated at 2022-06-13 04:05:16.576168
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    dud_obj = HPUXVirtual({})
    assert(dud_obj.platform == HPUXVirtual.platform)

# Generated at 2022-06-13 04:05:20.317846
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    h = HPUXVirtual()
    assert h.get_virtual_facts() == {
        'virtualization_type': 'guest',
        'virtualization_role': 'HP vPar',
        'virtualization_tech_guest': set(['HP vPar']),
        'virtualization_tech_host': set()
    }

# Generated at 2022-06-13 04:05:29.795330
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module = AnsibleModule(argument_spec=dict())
    # input data
    # _get_virtual_facts should return None because /usr/sbin/parstatus doesn't exist
    module.run_command = mock.MagicMock(return_value=(1, '', ''))
    hpux_virtual = HPUXVirtual(module)
    facts = hpux_virtual.get_virtual_facts()
    assert facts['virtualization_type'] == ''
    assert facts['virtualization_role'] == ''
    # Preparation for next test case
    module.run_command = mock.MagicMock(return_value=(0, 'Running on HPVM host', ''))
    # _get_virtual_facts should return None because it returned exit status 0 but it is not matching pattern
    hpux_virtual = HPUXVirtual(module)

# Generated at 2022-06-13 04:05:31.125127
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    h = HPUXVirtual(None)
    assert h.platform == 'HP-UX'

# Generated at 2022-06-13 04:06:13.756757
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    v = HPUXVirtual("module")
    os.stat('/usr/sbin/vecheck')
    os.stat('/opt/hpvm/bin/hpvminfo')
    os.stat('/usr/sbin/parstatus')
    assert v.platform == 'HP-UX'

# Generated at 2022-06-13 04:06:24.070421
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    '''Unit test for method get_virtual_facts of class HPUXVirtual'''
    class TestModule(object):
        def __init__(self):
            self.run_command_calls = []

        def run_command(self, args):
            self.run_command_calls.append(args)
            if args == '/usr/sbin/vecheck':
                return 0, 'Running HP vPar', ''
            if args == '/opt/hpvm/bin/hpvminfo':
                return 0, 'Running HPVM vPar', ''
            return 127, '', ''
    mod = TestModule()
    virtual = HPUXVirtual(module=mod)
    result = virtual.get_virtual_facts()

# Generated at 2022-06-13 04:06:35.537224
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    fake_module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )

    # Getting all the virtual facts on a HP-UX host
    # should be the same than getting facts with
    # the HPUXVirtualCollector.

    # Mocking the following methods of AnsibleModule:
    # - run_command
    # - get_bin_path
    # - file_exists
    fake_module.run_command = Mock(return_value=(0,'',''))
    fake_module.get_bin_path = Mock(side_effect=lambda arg: '/usr/sbin/'+arg)
    fake_module.file_exists = Mock(side_effect=lambda arg: os.path.exists(arg))

    hv = HPUXVirtual(fake_module)
    facts

# Generated at 2022-06-13 04:06:36.697335
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    v = HPUXVirtual({})
    assert v.platform == 'HP-UX'

# Generated at 2022-06-13 04:06:38.242712
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpuxvirtual = HPUXVirtual({})
    assert hpuxvirtual._Virtual__module.__class__.__name__ == 'AnsibleModule'

# Generated at 2022-06-13 04:06:40.382522
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_obj = HPUXVirtual()


# Generated at 2022-06-13 04:06:42.914450
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=False
    )
    fake_module = FakeModule(module)
    HPUXVirtual(fake_module).get_virtual_facts()
    assert module.run_command.called

# Generated at 2022-06-13 04:06:45.578713
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    assert issubclass(HPUXVirtual, Virtual)
    assert HPUXVirtual.platform == 'HP-UX'



# Generated at 2022-06-13 04:06:46.964876
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hp_virtual = HPUXVirtual()
    assert hp_virtual.platform == "HP-UX"


# Generated at 2022-06-13 04:06:54.470266
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtualCollector

    hpux_virtual = HPUXVirtual()
    # if no virtualization technology is found, the result should be an empty dict
    assert hpux_virtual.get_virtual_facts() == {}

    hpux_gathering = HPUXVirtualCollector({}, {})
    hpux_gathering._module = mock.MagicMock(spec_set=ansible.module_utils.basic.AnsibleModule)

    # if /usr/sbin/vecheck exists and the command return code is zero, the result should be guest
    hpux_gathering._module.run_command.return_value = (0, '', '')
    hpux_gathering

# Generated at 2022-06-13 04:08:57.897589
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts = HPUXVirtual()
    assert virtual_facts.platform == 'HP-UX'



# Generated at 2022-06-13 04:08:59.227141
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    v = HPUXVirtual({}, {}, {})
    assert v.platform == 'HP-UX'

# Generated at 2022-06-13 04:09:00.706114
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts_object = HPUXVirtual()
    assert virtual_facts_object.platform == 'HP-UX'


# Generated at 2022-06-13 04:09:03.342336
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    x = HPUXVirtual()
    assert x.virtualization_type == 'guest'
    assert x.virtualization_role == 'HPVM'

# Generated at 2022-06-13 04:09:08.478387
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    module = AnsibleModuleStub()
    # no output
    module.run_command_output['stdout'] = ''
    # no error
    module.run_command_output['stderr'] = ''
    v = HPUXVirtual(module)
    assert v != None
    assert v.get_virtual_facts() == dict(
        virtualization_type='',
        virtualization_role='',
        virtualization_tech_host=set(),
        virtualization_tech_guest=set()
    )


# Generated at 2022-06-13 04:09:11.572113
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    mock_module = type('module', (object,), {
        'run_command': lambda x: (0, '', '')
    })
    virtual = HPUXVirtual(module=mock_module)
    assert virtual.platform == 'HP-UX'


# Generated at 2022-06-13 04:09:16.286105
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    result = HPUXVirtual({})
    assert result.platform == 'HP-UX'
    assert result.virtualization_type is None
    assert result.virtualization_role is None
    assert result.virtualization_tech_host == set()
    assert result.virtualization_tech_guest == set()
    assert result.container_type is None
    assert result.container_path is None
    assert result.container_runtime is None
    assert result.container_id is None
