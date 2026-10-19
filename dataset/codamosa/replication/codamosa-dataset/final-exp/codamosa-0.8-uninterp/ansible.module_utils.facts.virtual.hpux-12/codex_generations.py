

# Generated at 2022-06-13 03:59:32.743421
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    """ Test the constructor to make sure it sets the platform and
    virtual types """

    virtual_facts = HPUXVirtual()
    assert virtual_facts.platform == 'HP-UX'

# Generated at 2022-06-13 03:59:34.231740
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    x = HPUXVirtual()
    assert x
    x = HPUXVirtual(module=dict())
    assert x

# Generated at 2022-06-13 03:59:41.677379
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts import FactCollector
    import ansible.module_utils.facts.virtual.hpux as hpux

    test_data = {'virtualization_tech_host': set(), 'virtualization_tech_guest': set(),
                 'virtualization_type': '', 'virtualization_role': ''}

    vecheck_exists = hpux.os.path.exists.return_value
    hpvminfo_exists = hpux.os.path.exists.return_value
    parstatus_exists = hpux.os.path.exists.return_value

    #  vecheck returns 0
    hpux.HPUXVirtual._run_command.return_value = 0, 'HP vPar', None
    hpux.os.path.exists.return_value = vecheck_exists

# Generated at 2022-06-13 03:59:45.725682
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual({})
    assert hv.platform == 'HP-UX'
    assert hv.virtualization_type == 'guest'
    assert hv.virtualization_role == 'HPVM vPar'

# Generated at 2022-06-13 03:59:54.318023
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    # Test parameters
    test_HPUXVirtual = None
    virtual_facts = None
    vecheck_output = None
    hpvminfo_output = None

    # Test cases
    class test_HPUXVirtual:
        def __init__(self):
            self.module = None
        def run_command(self, command):
            return (0,vecheck_output,'')

    test_HPUXVirtual = test_HPUXVirtual()
    HPUXVirtual = HPUXVirtualCollector._fact_class(test_HPUXVirtual)

    vecheck_output = 'test vPAR'
    virtual_facts = HPUXVirtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'guest'
    assert virtual_facts['virtualization_role'] == 'HP vPar'



# Generated at 2022-06-13 03:59:56.660255
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    '''
    Test: Instantiate a class HPUXVirtual
    '''
    virtual = HPUXVirtual(dict())

    assert virtual

# Generated at 2022-06-13 03:59:58.149269
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual(dict())
    assert hv.platform == 'HP-UX'

# Generated at 2022-06-13 04:00:07.444902
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils.facts.collector.virtual import HPUXVirtual
    import os

    class TestModule(object):
        def __init__(self, params):
            self.params = params

    v = HPUXVirtual()
    v._module = TestModule(dict())
    os.path.exists = lambda x: True
    v.run_command = lambda x: (0, "", "")

    # Test HP vPar
    assert v.get_virtual_facts() == {'virtualization_type': 'guest', 'virtualization_role': 'HP vPar', 'virtualization_tech_guest': set(['HP vPar']), 'virtualization_tech_host': set([])}
    # Test HPVM vPar

# Generated at 2022-06-13 04:00:18.053775
# Unit test for method get_virtual_facts of class HPUXVirtual

# Generated at 2022-06-13 04:00:21.562913
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual = HPUXVirtual(None)
    assert virtual
    assert virtual.platform == 'HP-UX'
    assert virtual.fact_class == HPUXVirtual
    assert virtual.collector_class == HPUXVirtualCollector



# Generated at 2022-06-13 04:00:33.255298
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    module = AnsibleModule(argument_spec={})
    virtual_facts_class_instance = HPUXVirtual(module)
    assert virtual_facts_class_instance.platform == 'HP-UX'

# Generated at 2022-06-13 04:00:36.885299
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    module = DummyAnsibleModule()
    hpux_virtual = HPUXVirtual(module)
    assert hpux_virtual.platform == 'HP-UX'

    rc, out, err = module.run_command.call_args[0]
    assert rc == 0
    assert out == ''
    assert err == ''


# Generated at 2022-06-13 04:00:43.666236
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpuxvirtual=HPUXVirtual(None)
    set_member=set(['HP vPar', 'HP nPar', 'HPVM vPar', 'HPVM IVM', 'HPVM'])
    assert hpuxvirtual.platform=='HP-UX'
    assert hpuxvirtual.virtualization_type is None
    assert hpuxvirtual.virtualization_role is None
    assert hpuxvirtual.virtualization_tech_guest==set_member
    assert hpuxvirtual.virtualization_tech_host==None

# Generated at 2022-06-13 04:00:46.463070
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual({'module': None})
    assert hv._platform == 'HP-UX'
    assert hv.platform == 'HP-UX'

# Generated at 2022-06-13 04:00:49.899672
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module = AnsibleModule
    hpux = HPUXVirtual(module)
    facts = hpux.get_virtual_facts()
    assert_equals(facts['virtualization_type'], 'guest')
    assert_equals(facts['virtualization_role'], 'HP vPar')
    assert_equals(facts['virtualization_tech_guest'], set(['HP vPar']))

# Generated at 2022-06-13 04:01:00.294494
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    # For hpux the file /usr/sbin/vecheck exists and returns rc 0
    # if the system is a HP vPar and outputs nothing otherwise
    # The expected virtualization_type is guest and the expected
    # virtualization_role is HP vPar.
    mock_module = MagicMock(
        run_command=MagicMock(return_value=(0, '', ''))
    )
    mock_module.get_bin_path.side_effect = lambda arg: arg
    hpux_v = HPUXVirtual(mock_module)
    sut_virtual_facts = hpux_v.get_virtual_facts()
    assert sut_virtual_facts['virtualization_type'] == 'guest'
    assert sut_virtual_facts['virtualization_role'] == 'HP vPar'
    assert sut_virtual

# Generated at 2022-06-13 04:01:07.997625
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    """
    Unit test for method get_virtual_facts of class HPUXVirtual
    """

    module = AnsibleModule(argument_spec={})
    virtual = HPUXVirtual(module)

    # simulating vecheck command output
    class RunCmd():
        def __init__(self, out, rc=0):
            self.out = out
            self.rc = rc

        def run_command(self, cmd):
            return self.rc, self.out, ''

    # simulating a non HP-UX host
    virtual.module = RunCmd(out='', rc=1)
    assert virtual.get_virtual_facts() == {}

    # simulating a HP-UX host not in a guest with vmware like command output
    virtual.module = RunCmd(out='HPVM guest, running on host kvm', rc=0)


# Generated at 2022-06-13 04:01:12.180541
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    module = AnsibleModule(argument_spec={})
    virtual_facts = HPUXVirtual(module).get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'host'
    assert virtual_facts['virtualization_role'] == 'HPVM'

# Generated at 2022-06-13 04:01:17.540352
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    """
    Unit test for method get_virtual_facts of class HPUXVirtual
    """
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtualCollector
    from ansible.module_utils.facts.virtual.hpux import Virtual
    from ansible.module_utils.facts.virtual.hpux import VirtualCollector

    # Create an instance of HPUXVirtual
    hpux = HPUXVirtual()

    # Invoke get_virtual_facts
    hpux.get_virtual_facts()

    # Test assert

# Generated at 2022-06-13 04:01:19.088358
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux = HPUXVirtual()
    assert hpux.platform == 'HP-UX'


# Generated at 2022-06-13 04:01:39.820506
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    # Constructing a mock module
    from ansible.module_utils import basic
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.virtual import hpu
    mock_module = basic.AnsibleModule(
        argument_spec=collector.get_generic_collector_facts_argument_spec(),
        supports_check_mode=True
    )

    mock_module.run_command = hpu.run_command

    # Constructing an instance of class HPUXVirtual
    obj = hpu.HPUXVirtual(mock_module)

    # Calling method get_virtual_facts
    facts = obj.get_virtual_facts()
    assert 'virtualization_type' in facts
    assert 'virtualization_role' in facts
    assert 'virtualization_tech_guest' in facts


# Generated at 2022-06-13 04:01:45.775816
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    facts = HPUXVirtual()
    assert facts.platform == 'HP-UX', 'Expect HP-UX, get {}'.format(facts.platform)
    assert facts.virtualization_type == 'None', 'Expect None, get {}'.format(facts.virtualization_type)
    assert facts.virtualization_role == 'None', 'Expect None, get {}'.format(facts.virtualization_role)
    assert facts.virtualization_tech_host == set(), 'Expect a set(), get {}'.format(facts.virtualization_tech_host)
    assert facts.virtualization_tech_guest == set(), 'Expect a set(), get {}'.format(facts.virtualization_tech_guest)

# Generated at 2022-06-13 04:01:55.519028
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtualCollector
    from ansible.module_utils.facts.virtual.posix import BasePosixVirtual
    from ansible.module_utils.facts.virtual.posix import BasePosixVirtualCollector
    hpxv = HPUXVirtual(module=None)
    rc, out, err = hpxv.module.run_command("/usr/sbin/swlist | /usr/bin/awk '{print $1}' | /usr/bin/sort | /usr/bin/uniq")
    if rc == 0 and "HPVM" in out:
        hpxv._facts['virtualization_tech_host'].add('HPVM')
        hpxv._

# Generated at 2022-06-13 04:01:58.568450
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    vs = HPUXVirtual({})
    assert isinstance(vs, Virtual)
    assert vs.platform == 'HP-UX'
    assert vs.get_virtual_facts() == {}


# Generated at 2022-06-13 04:01:59.780111
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    assert HPUXVirtual().__class__.__name__ == 'HPUXVirtual'

# Generated at 2022-06-13 04:02:07.039293
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module = MockModule()
    cmd_rc = {'/usr/sbin/vecheck': 0, '/opt/hpvm/bin/hpvminfo': 0,
              '/usr/sbin/parstatus': 0}
    cmd_out = {'/usr/sbin/vecheck': 'Running in HP vPar as guest\n',
               '/opt/hpvm/bin/hpvminfo': 'Running in HPVM IVM\n',
               '/usr/sbin/parstatus': 'Running in HP nPar as guest\n'}
    cmd_err = {'/usr/sbin/vecheck': '', '/opt/hpvm/bin/hpvminfo': '',
               '/usr/sbin/parstatus': ''}
    module.run_command = mock_run_command(cmd_rc, cmd_out, cmd_err)

# Generated at 2022-06-13 04:02:13.126342
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts = HPUXVirtual({}).get_virtual_facts()
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts
    assert virtual_facts['virtualization_tech_guest'] == set()
    assert virtual_facts['virtualization_tech_host'] == set()

# Generated at 2022-06-13 04:02:19.242936
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    class HPUXModule:
        pass
    module = HPUXModule()
    hpux_virtual = HPUXVirtual(module)

    # No HP-UX specific virtual tech files, and no Linux files
    hpux_virtual.file_exists_dict = {
        '/usr/sbin/vecheck': False,
        '/opt/hpvm/bin/hpvminfo': False,
        '/usr/sbin/parstatus': False,
    }
    hpux_virtual.module.run_command = lambda *args, **kwargs: (0, '', '')
    assert hpux_virtual.get_virtual_facts() == {
        'virtualization_tech_host': set(),
        'virtualization_tech_guest': set(),
    }

    # vecheck: /usr/sbin/vecheck exists, is

# Generated at 2022-06-13 04:02:27.593421
# Unit test for method get_virtual_facts of class HPUXVirtual

# Generated at 2022-06-13 04:02:28.787318
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    HPUXVirtual(dict())

# Generated at 2022-06-13 04:02:40.702143
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual = HPUXVirtual()
    assert hpux_virtual.platform == "HP-UX"


# Generated at 2022-06-13 04:02:50.748348
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    fake_module = type('', (), {})()
    fake_module.run_command = classmethod(lambda x, y: (0, '', ''))

    fact = HPUXVirtual(fake_module)
    if fact.platform != 'HP-UX':
        raise AssertionError('Expected platform HP-UX')

    virtual_facts = fact.get_virtual_facts()
    if virtual_facts is None:
        raise AssertionError('get_virtual_facts should not return None')

    if virtual_facts['virtualization_type'] != 'guest':
        raise AssertionError('virtualization_type should be guest')

    if virtual_facts['virtualization_role'] != 'HP vPar':
        raise AssertionError('virtualization_role should be HP vPar')


# Generated at 2022-06-13 04:02:52.125478
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual = HPUXVirtual({})
    assert virtual
    assert virtual.platform == 'HP-UX'



# Generated at 2022-06-13 04:02:54.603751
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual(dict(module=None))
    assert hv.platform == 'HP-UX'
    assert hv.get_virtual_facts() == dict(
        virtualization_tech_guest=set(),
        virtualization_tech_host=set(),
    )

# Generated at 2022-06-13 04:02:59.447361
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    hpux_virtual = HPUXVirtual({})
    facts = hpux_virtual.get_virtual_facts()
    assert facts['virtualization_type'] == 'guest'
    assert facts['virtualization_role'] == 'HP nPar'
    assert facts['virtualization_tech_host'] == set()
    assert facts['virtualization_tech_guest'] == {'HP nPar'}

# Generated at 2022-06-13 04:03:06.765420
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual import Virtual
    from ansible.module_utils.facts.virtual.hp_ux import HPUXVirtual
    from ansible.module_utils.facts.virtual._utils import (
        FakeModule, FakeCommand
    )

    # set up the sut
    sut = HPUXVirtual()


# Generated at 2022-06-13 04:03:13.679193
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    params = {'module': MagicMock()}
    params = dict(params, **{'root_dir': '/'})
    params = dict(params, **{'gather_subset': '!all'})
    v = HPUXVirtual(params)
    assert v.params['root_dir'] == '/'
    assert v.params['gather_subset'] == '!all'
    assert v.root_dir == '/'
    assert v.gather_subset == '!all'


# Unit test class HPUXVirtualCollector

# Generated at 2022-06-13 04:03:16.038922
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual({})
    assert hv.platform == "HP-UX"



# Generated at 2022-06-13 04:03:26.536522
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpar import HPUXVirtual
    from ansible.module_utils.facts import ModuleBase
    from ansible.module_utils.facts.virtual.hpvm import HPUXVirtualCollector

    class AnsibleModule(ModuleBase):
        def __init__(self, *args, **kwargs):
            super(AnsibleModule, self).__init__(*args, **kwargs)
            self.tmpdir = kwargs['tmpdir']
            self.exit_args = []

        def run_command(self, *args, **kwargs):
            return (0, '', '')

    class FactsModule(object):
        def __init__(self, *args, **kwargs):
            pass


# Generated at 2022-06-13 04:03:33.614683
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    fake_module = FakeAnsibleModule()
    hpx = HPUXVirtual()
    hpx.module = fake_module
    fake_module.run_command = {
        ('/usr/sbin/vecheck',): (0, '', ''),
        ('/opt/hpvm/bin/hpvminfo',): (0, 'Running HPVM guest...', ''),
        ('/usr/sbin/parstatus',): (1, '', ''),
    }[(fake_module.last_command,)]
    facts = hpx.get_virtual_facts()
    assert facts['virtualization_type'] == 'guest'
    assert facts['virtualization_role'] == 'HPVM IVM'
    assert set(facts['virtualization_tech_host']) == set()

# Generated at 2022-06-13 04:03:50.361037
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module = type('', (), {'run_command': dummy_run_command})
    virtual = HPUXVirtual(module)
    virtual_facts = virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'guest'
    assert virtual_facts['virtualization_role'] == 'HPVM vPar'
    assert 'HPVM vPar' in virtual_facts['virtualization_tech_guest']
    assert 'HP nPar' in virtual_facts['virtualization_tech_guest']
    assert 'HP vPar' in virtual_facts['virtualization_tech_guest']
    assert 'HPVM IVM' in virtual_facts['virtualization_tech_guest']
    assert 'HPVM' in virtual_facts['virtualization_tech_host']


# Generated at 2022-06-13 04:03:58.968591
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    '''
    Unit test for method get_virtual_facts of class HPUXVirtual
    '''
    hpuxvirtual_obj = HPUXVirtual()
    hpuxvirtual_obj.module = MockAnsibleModule()
    hpuxvirtual_obj.module.run_command = MockHPVECheck()
    assert hpuxvirtual_obj.get_virtual_facts()['virtualization_role'] == 'HP vPar'
    hpuxvirtual_obj.module.run_command = MockHPVMINFO()
    assert hpuxvirtual_obj.get_virtual_facts()['virtualization_role'] == 'HPVM vPar'
    hpuxvirtual_obj.module.run_command = MockHPVMINFO1()
    assert hpuxvirtual_obj.get_virtual_facts()['virtualization_role'] == 'HPVM IVM'
    hp

# Generated at 2022-06-13 04:04:02.885981
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts = HPUXVirtual(None).get_virtual_facts()
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts

# Generated at 2022-06-13 04:04:04.511077
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual = HPUXVirtual()
    assert hpux_virtual.platform == HPUXVirtual._platform



# Generated at 2022-06-13 04:04:13.444048
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    """
    Test method get_virtual_facts of class HPUXVirtual
    """
    from ansible.module_utils import basic
    from ansible.module_utils.facts import collector

    # Setup AnsibleModule
    module = basic.AnsibleModule(
        argument_spec={}
    )

    module.exit_json = basic.AnsibleModule.exit_json
    module.fail_json = basic.AnsibleModule.fail_json

    # Assigning of class VirtualCollector and class HPUXVirtual
    collector.collector.collectors['HPUX'] = HPUXVirtualCollector()

    # Preparing the test cases
    vout = {}
    vout['virtualization_type'] = 'guest'
    vout['virtualization_role'] = 'HP vPar'

# Generated at 2022-06-13 04:04:14.321542
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    x = HPUXVirtual()
    assert x.platform == 'HP-UX'

# Generated at 2022-06-13 04:04:15.356625
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual = HPUXVirtual()
    assert virtual.platform == 'HP-UX'


# Generated at 2022-06-13 04:04:20.251417
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    class ModuleStub:
        def __init__(self):
            self.run_command_calls = []
            self.run_command_rc = []
            self.run_command_out = []
            self.run_command_err = []

        def run_command(self, cmd, check_rc=False):
            self.run_command_calls.append(cmd)
            rc = self.run_command_rc.pop(0)
            out = self.run_command_out.pop(0)
            err = self.run_command_err.pop(0)
            return rc, out, err

    class OSStub:
        def __init__(self):
            self.path_exists_calls = []
            self.path_exists_return_values = []


# Generated at 2022-06-13 04:04:26.185240
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpux_hp_virtual import HPUXVirtual
    from ansible.module_utils.facts.virtual.hpux_hp_virtual import HPUXVirtualCollector
    from ansible.module_utils.facts.virtual.hpux_hp_virtual import test_HPUXVirtual_get_virtual_facts
    from ansible.module_utils.facts.virtual.hpux_hp_virtual import test_HPUXVirtualCollector_collect_from_platform_virtual
    from ansible.module_utils.facts.virtual.hpux_hp_virtual import test_HPUXVirtualCollector_collect_from_platform_virtual_noparstatus
    from ansible.module_utils.facts.virtual.hpux_hp_virtual import test_HPUXVirtualCollector_collect_from_platform_

# Generated at 2022-06-13 04:04:31.913198
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    h = HPUXVirtual()
    h.module.run_command = lambda *args, **kwargs: (0, '', '')
    h.module.get_bin_path = lambda *args, **kwargs: '/usr/bin/whatever'
    assert h.get_virtual_facts() == {
        'virtualization_type': 'guest',
        'virtualization_role': 'HP vPar',
        'virtualization_tech_guest': {'HP vPar'},
        'virtualization_tech_host': set()
    }

# Generated at 2022-06-13 04:04:49.810238
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    v = HPUXVirtual({})
    assert not v.get_virtual_facts()

# Generated at 2022-06-13 04:04:53.563208
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux = HPUXVirtual({})
    assert hpux
    assert hpux.platform == 'HP-UX'

# Generated at 2022-06-13 04:04:54.671000
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    # pending
    pass


# Generated at 2022-06-13 04:04:57.972081
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_obj = HPUXVirtual()
    assert hpux_obj is not None


# Generated at 2022-06-13 04:05:06.907604
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module = AnsibleModule(
        argument_spec = dict(
            gather_subset=dict(default=['!all'], type='list')
        ),
        supports_check_mode=True
    )

    facts = dict()
    facts['virtualization_type'] = 'host'
    facts['virtualization_role'] = 'host'
    facts['virtualization_tech'] = set()

    if module.check_mode:
        return facts

    hpux_virtual = HPUXVirtual(module)
    facts_new = hpux_virtual.get_virtual_facts()
    virtual_facts = dict()
    virtual_facts['virtualization_type'] = 'host'
    virtual_facts['virtualization_role'] = 'host'
    virtual_facts['virtualization_tech_guest'] = set()

# Generated at 2022-06-13 04:05:08.988877
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux = HPUXVirtual({})
    assert hpux is not None

# Unit test if HPVM guest is detected by HPUXVirtual class

# Generated at 2022-06-13 04:05:14.038586
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    """
    Test HPUXVirtual constructor
    """

    # Test empty constructor
    hpuxvirt = HPUXVirtual()

    if hasattr(hpuxvirt, '_platform'):
        assert hpuxvirt._platform == 'HP-UX'

    if hasattr(hpuxvirt, '_fact_class'):
        assert hpuxvirt._fact_class == HPUXVirtual


# Generated at 2022-06-13 04:05:17.928749
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux = HPUXVirtual()
    assert hpux.platform == 'HP-UX'
    assert hasattr(hpux, 'module')
    assert hpux.module is None
    assert hasattr(hpux, 'get_virtual_facts')
    assert hpux.get_virtual_facts is not None


# Generated at 2022-06-13 04:05:26.373564
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    """
    This test is to check the values of virtual_facts defined in
    the HPUXVirtual class
    """
    virtual_facts_test_data = {
        'virtualization_type': 'guest',
        'virtualization_role': 'HP vPar',
        'virtualization_tech_guest': set(['HP vPar']),
        'virtualization_tech_host': set([])
    }
    src = HPUXVirtual(None)
    src.module.run_command = print_run_command
    virtual_facts = src.get_virtual_facts()
    assert virtual_facts == virtual_facts_test_data



# Generated at 2022-06-13 04:05:31.897317
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpu = HPUXVirtual()
    assert hpu.virtualization_type == 'guest' or hpu.virtualization_type == 'host' or hpu.virtualization_type == 'NA'
    assert hpu.virtualization_role == 'HPVM vPar' or hpu.virtualization_role == 'HPVM IVM' or hpu.virtualization_role == 'HPVM' \
                                                     or hpu.virtualization_role == 'HP nPar' or hpu.virtualization_role == 'HP vPar' \
                                                     or hpu.virtualization_role == 'NA'

# Generated at 2022-06-13 04:05:49.229821
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpu_hpux import HPUXVirtual
    from ansible.module_utils.facts.virtual.hpu_hpux import HPUXVirtualCollector
    from ansible.module_utils.facts.virtual.base import Virtual, VirtualCollector
    # Collect facts
    hpux_virtual_collector = HPUXVirtualCollector()
    hpux_virtual_collector.collect()
    hpux_virtual_fact = hpux_virtual_collector._fact_class(hpux_virtual_collector.get_all_facts())
    print(hpux_virtual_fact.get_virtual_facts())

if __name__ == '__main__':
    test_HPUXVirtual_get_virtual_facts()

# Generated at 2022-06-13 04:05:50.172604
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    obj = HPUXVirtual(module)
    assert obj


# Generated at 2022-06-13 04:05:51.932257
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts = HPUXVirtual({})
    assert virtual_facts.platform == 'HP-UX'

# Generated at 2022-06-13 04:05:55.554848
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual({})
    assert 'virtualization_type' not in hv.data
    assert 'virtualization_role' not in hv.data
    assert 'virtualization_tech_host' not in hv.data
    assert 'virtualization_tech_guest' not in hv.data

# Generated at 2022-06-13 04:05:59.151853
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts = HPUXVirtual({})
    assert virtual_facts.virtualization_type == 'guest'
    assert virtual_facts.virtualization_role == 'HP vPar'

# Generated at 2022-06-13 04:06:05.231274
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    """
    Test method get_virtual_facts of class HPUXVirtual
    """
    from ansible.module_utils.facts.virtual.hpux import PlatformVirtual

    m = PlatformVirtual()
    vfacts = HPUXVirtual(module=m).get_virtual_facts()
    assert isinstance(vfacts, dict)
    assert 'virtualization_type' in vfacts
    assert 'virtualization_role' in vfacts

# Generated at 2022-06-13 04:06:06.389536
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpxv = HPUXVirtual()
    assert hpxv


# Generated at 2022-06-13 04:06:16.985054
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    """
    Test method get_virtual_facts of class HPUXVirtual.
    It returns a dict with virtualization_type and virtualization_role if it
    detects a virtual guest.
    """
    hpxvirtual = HPUXVirtual()
    os.path.exists = MagicMock(return_value=True)
    hpxvirtual.module.run_command = MagicMock(return_value=(0, '', ''))
    virtual_facts = hpxvirtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'guest'
    assert virtual_facts['virtualization_role'] == 'HP vPar'
    assert virtual_facts['virtualization_tech_guest'] == set(['HP vPar'])


# Generated at 2022-06-13 04:06:21.110975
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    hv = HPUXVirtual()
    vf = hv.get_virtual_facts()
    assert 'virtualization_type' not in vf
    assert 'virtualization_role' not in vf
    assert 'virtualization_tech_guest' not in vf
    assert 'virtualization_tech_host' not in vf


# Generated at 2022-06-13 04:06:22.571921
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual()
    assert hv.platform == 'HP-UX'

# Generated at 2022-06-13 04:06:47.091194
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual = HPUXVirtual()
    assert virtual.platform == 'HP-UX'
    assert virtual.get_virtual_facts() is None

# Generated at 2022-06-13 04:06:54.590082
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual import HPUXVirtual
    class FakeModule:

        def run_command(self, path):
            if path == '/usr/sbin/vecheck':
                return 0, '', ''
            elif path == '/opt/hpvm/bin/hpvminfo':
                return 0, 'Running as HPVM guest\n', ''
            elif path == '/usr/sbin/parstatus':
                return 0, '', ''

        def get_bin_path(self, path):
            return path

    facter = HPUXVirtual(FakeModule())
    virtual_facts = facter.get_virtual_facts()
    assert virtual_facts
    assert virtual_facts['virtualization_type'] == 'guest'

# Generated at 2022-06-13 04:06:58.873665
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )

    virtual_facts = HPUXVirtual(module).get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'host'
    assert virtual_facts['virtualization_role'] == 'HPVM'


# Generated at 2022-06-13 04:07:01.906226
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts = HPUXVirtual()
    assert(virtual_facts.platform == 'HP-UX')


# Generated at 2022-06-13 04:07:08.755607
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    # Test for guest on HP vPar
    module = FakeModule(
        dict(
            run_command=HPUXVirtual.run_command,
        ),
        '/usr/sbin/vecheck',
        '',
        True,
    )
    hpux_virtual = HPUXVirtual(module)
    assert hpux_virtual.get_virtual_facts() == \
        dict(
            virtualization_type="guest",
            virtualization_role="HP vPar",
            virtualization_tech_guest=set(['HP vPar']),
            virtualization_tech_host=set(),
        )

    # Test for guest on HPVM vPar

# Generated at 2022-06-13 04:07:09.692871
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    h = HPUXVirtual()
    assert h.platform == 'HP-UX'

# Generated at 2022-06-13 04:07:11.121453
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpxvirtual = HPUXVirtual(dict())
    assert hpxvirtual.platform == 'HP-UX'


# Generated at 2022-06-13 04:07:14.103883
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual = HPUXVirtual()
    assert virtual.platform == 'HP-UX'
    assert virtual.virtualization_type == 'host'
    assert virtual.virtualization_role == ''
    assert virtual.virtualization_tech_host == set()
    assert virtual.virtualization_tech_guest == set()

# Unit test of the method get_virtual_facts() in class HPUXVirtual

# Generated at 2022-06-13 04:07:16.094278
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual()
    assert hv.platform == 'HP-UX'


# Generated at 2022-06-13 04:07:24.490905
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    import sys
    import os
    import re
    import tempfile

    class ModuleStub(object):

        def __init__(self):
            self.params = { }
            self.run_command_rc = 0
            self.run_command_out = ""
            self.run_command_err = ""


        def run_command(self, command):
            return self.run_command_rc, self.run_command_out, self.run_command_err


    if sys.version_info[:2] <= (2, 6):
        import unittest2 as unittest
    else:
        import unittest
    import tempfile


# Generated at 2022-06-13 04:07:56.962562
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual()
    assert hv.platform == 'HP-UX'

# Generated at 2022-06-13 04:08:00.760602
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True)
    #Instantiate HPUXVirtual object and check for expected output
    hv = HPUXVirtual(module)
    assert hv.get_virtual_facts() == {}



# Generated at 2022-06-13 04:08:02.253001
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts = HPUXVirtual(dict(), "")
    assert virtual_facts.platform == 'HP-UX'


# Generated at 2022-06-13 04:08:10.421394
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts import ModuleStub
    from ansible.module_utils.facts.virtual import HPUXVirtual
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common._collections_compat import MutableMapping, MutableSequence

    def run_command_mock(command):
        if command.startswith("/usr/sbin/vecheck"):
            return (0, "Test output from vecheck", "")
        elif command.startswith("/opt/hpvm/bin/hpvminfo"):
            return (0, "Test output from hpvminfo", "")
        elif command.startswith("/usr/sbin/parstatus"):
            return (0, "Test output from parstatus", "")

# Generated at 2022-06-13 04:08:15.143014
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    """Constructor test"""
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    if not HPUXVirtual(module).is_platform_supported():
        module.fail_json(msg='HP-UX not supported')
    virtual_facts = HPUXVirtual(module).get_facts()
    module.exit_json(changed=False, ansible_facts=dict(virtual=virtual_facts))



# Generated at 2022-06-13 04:08:18.079017
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    h = HPUXVirtual({})

    (virtual_type, virtual_role,
     virtual_tech_guest, virtual_tech_host) = h.get_virtual_facts()

    assert virtual_type == 'guest'
    assert virtual_role == 'HP nPar'
    assert 'HP nPar' in virtual_tech_guest
    assert len(virtual_tech_host) == 0

# Generated at 2022-06-13 04:08:19.852603
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    m = HPUXVirtual({})
    assert m.platform == m.platform

# Generated at 2022-06-13 04:08:21.627110
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    """Unit testing for constructor of class HPUXVirtual"""
    virtual_facts = HPUXVirtual()
    print(vars(virtual_facts))


# Generated at 2022-06-13 04:08:23.049582
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    v = HPUXVirtual({})
    assert v.platform == 'HP-UX'

# Generated at 2022-06-13 04:08:30.939611
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    class ModuleStub:
        def run_command(self, command):
            class TestArgs:
                def __init__(self, out, rc):
                    self.out = out
                    self.rc = rc

            out = err = None
            rc = 0
            if 'vecheck' in command:
                out = "Parallel Virtual Machine (PVM) for HP-UX is NOT running."
                rc = 0
            elif 'hpvminfo' in command:
                out = "HPVM Virtual Machines (IVM) for HP-UX is NOT running."
                rc = 0
            elif 'parstatus' in command:
                out = None
                rc = 1
            return TestArgs(out, rc)

    module_stub = ModuleStub()
    hpux_virtual = HPUXVirtual(module_stub)