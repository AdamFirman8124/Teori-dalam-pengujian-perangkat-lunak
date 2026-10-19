

# Generated at 2022-06-13 03:59:31.346142
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual
    from ansible.module_utils.facts.virtual import VirtualCollector
    from ansible.module_utils.facts.virtual import BaseVirtual
    from ansible.module_utils import basic
    import mock

    mod_mock = mock.MagicMock()
    mod_mock.run_command.return_value = (0,"","")
    mod_mock.params = {}
    mod_mock.config = {}
    basic._ANSIBLE_ARGS = None
    # case 1: vecheck is available
    vcol_mock = mock.MagicMock()
    vcol_mock.module = mod_mock
    vcol_mock.platform = 'HP-UX'

# Generated at 2022-06-13 03:59:36.502358
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual
    from ansible.module_utils.facts.virtual.solaris import SolarisVirtual
    from ansible.module_utils.facts.virtual.aix import AIXVirtual
    from ansible.module_utils.facts.virtual.bsd import BSDVirtual
    from ansible.module_utils.facts.virtual.linux import LinuxVirtual
    from ansible.module_utils.facts.virtual.smartos import SmartOSVirtual
    from ansible.module_utils.facts.virtual.netbsd import NetBSDVirtual
    from ansible.module_utils.facts.virtual.openbsd import OpenBSDVirtual
    from ansible.module_utils.facts.virtual.freebsd import FreeBSDVirtual

    module_mock = Mock()
    module_mock.run_

# Generated at 2022-06-13 03:59:42.995840
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    import platform
    import os
    from ansible_collections.ansible.community.tests.unit.modules.utils import AnsibleExitJson, AnsibleFailJson, ModuleTestCase
    from ansible_collections.ansible.community.plugins.module_utils import basic
    from ansible_collections.ansible.community.plugins.module_utils._text import to_bytes

    class AnsibleModuleMock(object):
        def __init__(self, *args, **kwargs):
            self.params = kwargs

        def fail_json(self, *args, **kwargs):
            self.exit_args = args
            self.exit_kwargs = kwargs
            raise AnsibleFailJson(args, kwargs)

        def exit_json(self, *args, **kwargs):
            self.exit

# Generated at 2022-06-13 03:59:51.203617
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.basic import AnsibleModule
    import json

    hv = HPUXVirtual(AnsibleModule)
    hv_facts = hv.get_virtual_facts()
    expected_hv_facts = {"virtualization_type": "host",
                         "virtualization_role": "HPVM",
                         "virtualization_tech_host": set(['HPVM']),
                         "virtualization_tech_guest": set()}

    assert json.dumps(hv_facts, sort_keys=True) == json.dumps(expected_hv_facts, sort_keys=True),\
        "HPUXVirtual get_virtual_facts returning unexpected facts"

# Generated at 2022-06-13 03:59:57.653497
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpu import HPUXVirtual
    from ansible.module_utils.six import PY3
    import ansible.module_utils.facts.virtual.hpu as hpu
    virtual = HPUXVirtual(dict(module=hpu))
    virtual_facts = virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'guest'
    assert virtual_facts['virtualization_role'] == 'HP nPar'

    if PY3:
        # Python 3.x
        assert virtual_facts['virtualization_tech_guest'] == {'HP nPar'}
    else:
        # Python 2.x, because order is not defined
        assert virtual_facts['virtualization_tech_guest'] == set(['HP nPar'])

   

# Generated at 2022-06-13 04:00:00.538515
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual = HPUXVirtual(None)
    assert hpux_virtual.platform == 'HP-UX'



# Generated at 2022-06-13 04:00:02.274945
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    v = HPUXVirtual({}, {}, {})
    assert v is not None


# Generated at 2022-06-13 04:00:07.339299
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    # mock module and it's params
    from ansible.module_utils.facts import ModuleParameters
    import ansible.module_utils.facts.virtual.hpux
    module_params = ModuleParameters()
    module_params.params = {}

    # initialize Virtual class with module params
    obj = HPUXVirtual(module_params)
    obj.get_virtual_facts()
    assert 'virtualization_type' in obj.facts
    assert 'virtualization_role' in obj.facts

# Generated at 2022-06-13 04:00:17.981637
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    test_module = HPUXVirtual(dict(module=None))
    test_module.module.run_command = test_module.run_command
    # vecheck
    out = 'test\nbla'
    test_module.run_command_filters = dict(vecheck=out)
    virtual_facts = test_module.get_virtual_facts()
    assert 'virtualization_type' in virtual_facts
    assert virtual_facts['virtualization_type'] == 'guest'
    assert 'virtualization_role' in virtual_facts
    assert virtual_facts['virtualization_role'] == 'HP vPar'
    assert virtual_facts['virtualization_tech_guest'] == set(['HP vPar'])
    # hpvminfo
    out = 'test\nRunning guest in HPVM vPar mode.'
    test

# Generated at 2022-06-13 04:00:25.516868
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    """HP-UX Virtual test"""
    #@pylint: disable=no-member
    #@pylint: disable=no-name-in-module
    if not hasattr(os.path, 'exists'):
        #@pylint: disable=unused-variable
        os.path.exists = lambda x: False
    module = Mock(return_value=None)
    module.run_command = Mock(return_value=(0, 'output', 'error'))
    module.path = '/usr/sbin/'
    hpux_virtual = HPUXVirtual(module=module)
    hpux_virtual.get_virtual_facts()

# Generated at 2022-06-13 04:00:36.679334
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual()
    assert hv.platform == 'HP-UX'
    assert hv

# Generated at 2022-06-13 04:00:40.718348
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    h = HPUXVirtual()
    assert h.platform == 'HP-UX'
    assert h._platform == 'HP-UX'
    assert h.virtualization_type == ''
    assert h.virtualization_role == ''
    assert h.virtualization_tech_host == set()
    assert h.virtualization_tech_guest == set()
    assert h.virtualization_tech_info == {}
    assert h.virtualization_tech_info['HP-UX'] == {}

# Generated at 2022-06-13 04:00:43.342599
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual = HPUXVirtual(dict())
    assert hpux_virtual.platform == 'HP-UX'


# Generated at 2022-06-13 04:00:44.773890
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual()
    assert hv.platform == 'HP-UX'

# Generated at 2022-06-13 04:00:51.206396
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    """
    This is a unit test for ansible.module_utils.facts.hpux_virtual.py.

    It verifies that an instance of HPUXVirtual
    collects facts in the format expected by Ansible.
    """

    m = dict(
        ANSIBLE_MODULE_ARGS = dict(
            gather_subset = 'all'
        )
    )

    # Create an instance of HPUXVirtual
    inst = HPUXVirtual(m)
    inst.module.run_command = run_command_mock

    # Call the get_virtual_facts method
    virtual_facts = inst.get_virtual_facts()

    # Verify the output

# Generated at 2022-06-13 04:01:01.867168
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    import tempfile
    from ansible.module_utils.facts.virtual.hpar import HPUXVirtual
    from ansible.module_utils.facts.virtual.hpvm import HPUXVirtual
    from ansible.module_utils.facts.virtual.hpvm import HPUXVirtual
    from ansible.module_utils.facts.virtual.par import HPUXVirtual
    from ansible.module_utils.facts.virtual import VirtualCollector

    temp = tempfile.TemporaryDirectory()
    vecheck = os.path.join(temp.name, 'vecheck')
    hpvminfo = os.path.join(temp.name, 'hpvminfo')
    parstatus = os.path.join(temp.name, 'parstatus')

    # case 0: HP-UX guest running on HP vPar

# Generated at 2022-06-13 04:01:12.503625
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    class DummyModule(object):
        pass
    class DummyFacts(object):
        pass
    module = DummyModule()
    module.run_command = lambda *args, **kwargs: (0, '', '')
    module.get_bin_path = lambda *args, **kwargs: '/usr/bin/' + args[0]
    module.params = {}
    virtual_facts = HPUXVirtual(module).get_virtual_facts()
    assert virtual_facts['virtualization_tech_host'] == set()
    assert virtual_facts['virtualization_tech_guest'] == set(['HP nPar'])
    assert virtual_facts['virtualization_role'] == 'HP nPar'
    assert virtual_facts['virtualization_type'] == 'guest'

# Generated at 2022-06-13 04:01:13.011448
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    pass

# Generated at 2022-06-13 04:01:15.285857
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpuxv = HPUXVirtual({})
    assert hpuxv.platform == 'HP-UX'

# Generated at 2022-06-13 04:01:19.317153
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    """
    Function to perform unit test for constructor of class HPUXVirtual
    """
    # Call constructor of class HPUXVirtual
    obj = HPUXVirtual()

    # Check if it is instance of class Virtual
    assert isinstance(obj, Virtual) == True


# Generated at 2022-06-13 04:01:47.388020
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    """
    HPUXVirtual - class to collect virtualization facts on HP-UX
    """
    # Create instances of HPUXVirtual class
    # vecheck output
    vecheck_out = open('test/unittests/hpux_virtual/vecheck_out', 'rb')
    vecheck_out.read(1)  # skip first byte
    vecheck_out_string = vecheck_out.read()
    vecheck_out.close()
    # hpvminfo output
    hpvminfo_out = open('test/unittests/hpux_virtual/hpvminfo_out', 'rb')
    hpvminfo_out.read(1)  # skip first byte
    hpvminfo_out_string = hpvminfo_out.read()
    hpvminfo_out.close()
   

# Generated at 2022-06-13 04:01:55.197239
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual = HPUXVirtual("/usr/sbin/vecheck", "/opt/hpvm/bin/hpvminfo", "/usr/sbin/parstatus", "/usr/bin/uname", None, None, None)
    assert virtual
    assert virtual.module.get_bin_path('vecheck') == '/usr/sbin/vecheck'
    assert virtual.module.get_bin_path('hpvminfo') == '/opt/hpvm/bin/hpvminfo'
    assert virtual.module.get_bin_path('parstatus') == '/usr/sbin/parstatus'
    assert virtual.module.get_bin_path('uname') == '/usr/bin/uname'

# Generated at 2022-06-13 04:01:56.450622
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux1 = HPUXVirtual({})
    assert hpux1.platform == 'HP-UX'


# Generated at 2022-06-13 04:01:58.132313
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpuxvirt = HPUXVirtual()
    assert hpuxvirt
    assert hpuxvirt.platform == 'HP-UX'

# Generated at 2022-06-13 04:02:00.824257
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():

    facts = HPUXVirtual({}, {}).collect()

    assert 'virtualization_type' in facts
    assert 'virtualization_role' in facts
    assert 'virtualization_tech_guest' in facts
    assert 'virtualization_tech_host' in facts

# Generated at 2022-06-13 04:02:07.245930
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():

    # Test HP-UX machine as Host
    my_HPUXVirtual = HPUXVirtual({'module_name': 'unit_test'})
    my_HPUXVirtual.module.run_command = lambda x: (0, 'Running HPVM host', '')
    virtual_facts = my_HPUXVirtual.get_virtual_facts()
    assert 'virtualization_type' in virtual_facts
    assert virtual_facts['virtualization_type'] == 'host'
    assert 'virtualization_role' in virtual_facts
    assert virtual_facts['virtualization_role'] == 'HPVM'
    assert 'virtualization_tech_guest' in virtual_facts
    assert 'HPVM' in virtual_facts['virtualization_tech_guest']
    assert 'virtualization_tech_host' in virtual_facts
    assert not virtual_facts

# Generated at 2022-06-13 04:02:11.809386
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_obj = HPUXVirtual()
    assert virtual_obj.virtualization_type == 'guest'
    assert virtual_obj.virtualization_role == 'HP nPar'

# unittest for _get_virtual_facts() function of class HPUXVirtual

# Generated at 2022-06-13 04:02:18.299110
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual
    h = HPUXVirtual()
    if os.path.exists('/usr/sbin/parstatus'):
        assert h._get_virtual_facts() == {'virtualization_type': 'guest',
                                          'virtualization_role': 'HP nPar',
                                          'virtualization_tech_guest': {'HP nPar'},
                                          'virtualization_tech_host': set()}

# Generated at 2022-06-13 04:02:23.240021
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual
    module = FakeAnsibleModule()
    virtual_ins = HPUXVirtual(module)
    virtual_ins.module.run_command = run_command
    virtual_ins.os_path_exists = os_path_exists
    virtual_ins.extended = True
    facts = virtual_ins.get_virtual_facts()
    assert facts['virtualization_type'] == 'guest'
    assert facts['virtualization_role'] == 'HPVM vPar'
    assert 'guest' in facts['virtualization_tech_guest']
    assert not facts['virtualization_tech_host']



# Generated at 2022-06-13 04:02:27.887835
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    host_virtual = HPUXVirtualCollector.collect(None, None)
    assert host_virtual['virtualization_type'] == 'host'
    assert sorted(host_virtual['virtualization_tech_host']) == ['HPVM']
    assert host_virtual['virtualization_tech_guest'] == set()


# Generated at 2022-06-13 04:02:58.533914
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_obj = HPUXVirtual()
    assert 'HPUXVirtual' == virtual_obj.__class__.__name__
    assert 'HP-UX' == virtual_obj.platform


# Generated at 2022-06-13 04:03:05.219626
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    # Arrange
    # Dummy AnsibleModule object
    from ansible.module_utils.facts import ModuleDict
    from ansible.module_utils.facts import ansible_module

    from ansible.module_utils.facts.virtual import HPUXVirtual
    testobj = HPUXVirtual(ansible_module)

    os.path.exists = lambda x: True

    testobj.module.run_command = \
        lambda x: (0, 'Running HPVM host', '')

    expected = {'virtualization_type': 'host',
                'virtualization_role': 'HPVM',
                'virtualization_tech_host': set(['HPVM']),
                'virtualization_tech_guest': set()}

    # Act
    actual = testobj.get_virtual_facts()

    # Assert
   

# Generated at 2022-06-13 04:03:07.137526
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual = HPUXVirtual()
    assert hpux_virtual.platform == 'HP-UX'


# Generated at 2022-06-13 04:03:16.407945
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    """
    Verify that the correct virtual_facts are returned for
    each virtualization type/role combination:
      host/HPVM
      guest/HPVM IVM
      guest/HPVM vPar
      guest/nPar
      guest/vPar
    """
    import ansible.module_utils.facts.virtual.hpux
    from ansible.module_utils.facts import ModuleConfig
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual

    # setup the test modules
    config = ModuleConfig('HP-UX', None, None, 'command')
    module = AnsibleModule(config)
    virtual = HPUXVirtual(module)

    # set up mock functions to gain control over execution of
    # os.path.exists("/opt/hpvm/bin/hpvminfo")

# Generated at 2022-06-13 04:03:17.807091
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    sut = HPUXVirtual()
    assert sut.platform == 'HP-UX'


# Generated at 2022-06-13 04:03:27.541988
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    # Problem: Constructor of HPUXVirtual() expects an instance of AnsibleModule
    from ansible.module_utils.facts import __file__ as base_file
    base_path = os.path.join(os.path.abspath(base_file), '..', '..', '..')
    module_path = os.path.join(base_path, 'lib', 'ansible', 'modules', 'system')
    virtual_inst = HPUXVirtual(dict(ANSPATH=base_path, MODULESPATH=module_path, OFFLINE_JSON_FILTER=''), '/etc/ansible/facts.d')
    assert isinstance(virtual_inst, HPUXVirtual)


# Generated at 2022-06-13 04:03:31.250156
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    # Test with HPUXVirtual, we expect it is a subclass of Virtual.
    assert issubclass(HPUXVirtual, Virtual)
    # Test instantiation of HPUXVirtual
    virtual_obj = HPUXVirtualCollector.collect()
    assert virtual_obj['virtualization_type'] == 'guest'
    assert virtual_obj['virtualization_role'] == 'HP vPar'

# Generated at 2022-06-13 04:03:34.927545
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts = HPUXVirtualCollector._get_virtual_facts_platform()
    assert virtual_facts['virtualization_tech_guest'] == {'HPVM vPar',
                                                          'HP vPar', 'HP nPar',
                                                          'HPVM IVM'}
    assert virtual_facts['virtualization_tech_host'] == set()
    assert virtual_facts['virtualization_type'] == 'guest'
    assert virtual_facts['virtualization_role'] == 'HP vPar'

# Generated at 2022-06-13 04:03:37.304381
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    module = AnsibleModule(argument_spec={})
    virtual_obj = HPUXVirtual(module)

# Generated at 2022-06-13 04:03:40.351799
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    '''
    Test to check the parameters in constructor of class HPUXVirtual
    '''
    hp_virtual = HPUXVirtual(None)
    assert hp_virtual.platform == 'HP-UX'
    assert hp_virtual.module == None

# Generated at 2022-06-13 04:04:47.239049
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    # GIVEN a class instance
    hpux = HPUXVirtual({}, {})
    
    # WHEN get_virtual_facts is called
    # hpux.module.run_command = lambda arg: (0, '', '')
    hpux.module.run_command = lambda arg: (1, '', '')
    virtual_facts = hpux.get_virtual_facts()
    # THEN _get_virtual_facts returns
    assert virtual_facts == {'virtualization_type': None,
                             'virtualization_role': None,
                             'virtualization_tech_host': set(),
                             'virtualization_tech_guest': set()}


# Generated at 2022-06-13 04:04:58.782845
# Unit test for method get_virtual_facts of class HPUXVirtual

# Generated at 2022-06-13 04:05:03.324316
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module = AnsibleModuleMock()
    facts = HPUXVirtual(module).get_virtual_facts()

    assert 'virtualization_tech_guest' in facts
    assert 'virtualization_tech_host' in facts
    assert 'virtualization_type' in facts
    assert 'virtualization_role' in facts

# Generated at 2022-06-13 04:05:04.982368
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    # Test with valid arguments
    HPUXVirtual(dict())

# Generated at 2022-06-13 04:05:06.960659
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts = HPUXVirtual(dict())
    assert virtual_facts.platform == 'HP-UX'


# Generated at 2022-06-13 04:05:12.144626
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts import ModuleFacts
    module = ModuleFacts()
    virtual_facts = HPUXVirtual().get_virtual_facts()
    assert 'virtualization_type' not in virtual_facts
    assert 'virtualization_role' not in virtual_facts
    assert 'virtualization_tech_guest' not in virtual_facts
    assert 'virtualization_tech_host' not in virtual_facts

# Generated at 2022-06-13 04:05:18.871690
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module = HPUXVirtual._get_test_module("test", "HP-UX")
    module.run_command = HPUXVirtual._get_test_run_command("test", "HP-UX")
    virtual = HPUXVirtual(module)
    assert virtual.get_virtual_facts() == {
        'virtualization_type': 'guest',
        'virtualization_role': 'HPVM IVM',
        'virtualization_tech_host': set(),
        'virtualization_tech_guest': {'HPVM IVM'}
    }


# Generated at 2022-06-13 04:05:28.273704
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    class MockAnsibleModule(object):
        def __init__(self):
            self.params = {'gather_subset': '!all,'}

        def get_bin_path(self, arg, required=False, opt_dirs=[]):
            return '/bin/' + arg

        def run_command(self, cmd):
            class MockCommandResult(object):
                def __init__(self):
                    self.rc = 0
            return MockCommandResult()

    class MockHPVMParams(object):
        def __init__(self):
            self.hpvm_guest = False
            self.hpvm_host = False
            self.hpvm_vpar = False
            self.npar = False
            self.vpar = False

    hpsp = MockHPVMParams()


# Generated at 2022-06-13 04:05:30.810638
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    """
    This is a unittest for constructor of class HPUXVirtual
    """
    hpux = HPUXVirtual()
    assert hpux.platform == 'HP-UX'


# Generated at 2022-06-13 04:05:35.613882
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    """ Unit test: get_virtual_facts of class HPUXVirtual """

    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = False)

    hpux_module = HPUXVirtual(module=module)
    hpux_module.get_virtual_facts()

# Generated at 2022-06-13 04:07:12.391594
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual = HPUXVirtual()
    virtual_facts = virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'guest'
    assert virtual_facts['virtualization_role'] == 'HP vPar'
    assert 'HP vPar' in virtual_facts['virtualization_tech_guest']
    assert virtual_facts['virtualization_tech_host'] == set()

# Generated at 2022-06-13 04:07:17.827039
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():

    # Create a mock module
    mock_module = type('AnsibleModule', (object,), {})()

    # Create a mock class for the base module.
    mock_base_module = type('AnsibleModuleBase', (object,), {})()

    # Set return values for mock module methods
    mock_module.run_command.return_value = (1, 'some_output', 'some_err')
    mock_module.fail_json.return_value = {'msg': 'some_msg'}
    mock_module.exit_json.return_value = {'changed': False, 'ansible_facts': {}}

    # Create a virtual fact class
    hp_virtual = HPUXVirtual(mock_module)

    # Create patchers

# Generated at 2022-06-13 04:07:25.357784
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    def mock_module_run_command(module, args):
        if args == "/usr/sbin/vecheck":
            return 0, '', ''
        if args == "/opt/hpvm/bin/hpvminfo":
            return 0, 'Running HPVM guest', ''
        if args == "/usr/sbin/parstatus":
            return 0, '', ''
        return 1, '', ''

    mock_module = MockModule(run_command=mock_module_run_command)
    mock_module.exit_json = Mock()
    virtual = HPUXVirtual(mock_module)
    virtual_facts = virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'guest'
    assert virtual_facts['virtualization_role'] == 'HPVM IVM'

# Generated at 2022-06-13 04:07:29.698537
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts = HPUXVirtual()
    assert virtual_facts.platform == "HP-UX"
    assert isinstance(virtual_facts.get_virtual_facts(), dict)


# Generated at 2022-06-13 04:07:39.076351
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    import sys
    import re
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtualCollector
    from ansible.module_utils._text import to_bytes

    FAKE_PATH = '/fakepath'
    sys.modules['ansible.module_utils.facts.virtual.hpux'] = sys.modules[__name__]

    HPUXVirtualCollector.platform = 'HP-UX'
    HPUXVirtualCollector.collect()
    assert 'virtualization_type' in HPUXVirtualCollector.virtual.virtual_facts
    assert 'virtualization_role' in HPUXVirtualCollector.virtual.virtual_facts

# Generated at 2022-06-13 04:07:44.007978
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():

    # Code to create a dummy module and class with supporting functions
    #
    # TODO: Add unit test to check verfication on each supported platform
    #
    #
    class AnsibleModule(object):
        def __init__(self):
            self.run_command_called = 0
            self.run_command_rc = -1
            self.run_command_out = ''
            self.run_command_err = ''

        def run_command(self, arg):
            self.run_command_called += 1
            self.run_command_rc = -1
            self.run_command_out = ''
            self.run_command_err = ''

            if arg == '/usr/sbin/vecheck':
                if self.run_command_called == 1:
                    self.run_command_rc = 1
                   

# Generated at 2022-06-13 04:07:51.884761
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    import sys
    import os
    import ansible.module_utils.facts.virtual.hpux as hpux
    sys.modules['ansible'] = type('AnsibleMockModule', (object,), {})()
    sys.modules['ansible.module_utils'] = type('AnsibleModuleUtilsMockModule', (object,), {})()
    sys.modules['ansible.module_utils.facts'] = type('FactsMockModule', (object,), {})()
    sys.modules['ansible.module_utils.facts.virtual'] = type('VirtualMockModule', (object,), {})()
    hpux.__name__ = 'ansible.module_utils.facts.virtual.hpux'
    fact_obj = hpux.HPUXVirtual()

# Generated at 2022-06-13 04:07:53.672518
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    ''' Unit test for constructor of class HPUXVirtual '''
    test_virtual = HPUXVirtual(dict())
    assert test_virtual


# Generated at 2022-06-13 04:07:58.953749
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    class _Module:
        def __init__(self):
            self.run_command = run_command

    class _Os:
        path = path

    class _Virtual(HPUXVirtual):
        def __init__(self, module):
            self.module = module

    module = _Module()
    virtual = _Virtual(module)
    os = _Os()
    os.path.exists = _os_path_exists
    virtual._os = os
    virtual.get_virtual_facts = virtual_facts

    assert virtual_facts() == {
        'virtualization_role': 'HP vPar',
        'virtualization_type': 'guest',
        'virtualization_tech_guest': {'HP vPar'},
        'virtualization_tech_host': set()
    }


# Mock method run_command

# Generated at 2022-06-13 04:08:00.021005
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    HPUXVirtual()