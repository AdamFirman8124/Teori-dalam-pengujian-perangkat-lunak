

# Generated at 2022-06-13 03:59:31.168891
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    import json
    import platform
    from ansible.module_utils.facts.virtual.hpar import HPUXVirtual
    from ansible.module_utils.facts.virtual.hpvm import HPUXVirtual
    from ansible.module_utils.facts.virtual.npar import HPUXVirtual
    from ansible.module_utils.facts.virtual.ivm import HPUXVirtual
    from ansible.module_utils.facts.virtual.base import Virtual
    from ansible.utils.pycompat24 import get_exception
    class FakeModule:
        def __init__(self, exit_output):
            self.exit_output = exit_output
        def run_command(self, cmd):
            if 'vecheck' in cmd or 'hpvminfo' in cmd:
                if 'vecheck' in cmd:
                    cmd_

# Generated at 2022-06-13 03:59:33.372250
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual({})
    assert isinstance(hv, Virtual)
    assert hv.platform == 'HP-UX'



# Generated at 2022-06-13 03:59:41.137235
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts import collector

    class ModuleStub(object):
        class RunCommand(object):
            pass

        run_command = RunCommand()

    module_stub = ModuleStub()
    module_stub.run_command.return_value = (0,
                                            'Running as a HPVM guest\n#',
                                            '')
    guest_tech = set()
    host_tech = set()
    virtualization_facts = {
        'virtualization_type': 'guest',
        'virtualization_role': 'HPVM vPar',
        'virtualization_tech_guest': guest_tech,
        'virtualization_tech_host': host_tech
    }

    hpux_virtual = HPUXVirtual(module_stub)
    virtual_facts = hpux_virtual

# Generated at 2022-06-13 03:59:51.242971
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual

    hpux_virtual = HPUXVirtual()
    # vecheck exists
    with patch.dict(hpux_virtual.facts, {'is_hpux': True, 'system_vendor': 'HP'}):
        hpux_virtual.module = MagicMock()
        hpux_virtual.module.run_command.return_value = (0, 'output_vecheck', '')
        assert hpux_virtual.get_virtual_facts() == {'virtualization_type': 'guest',
                                            'virtualization_role': 'HP vPar',
                                            'virtualization_tech_guest': {'HP vPar'},
                                            'virtualization_tech_host': set()}
        hpux_virtual.module.run

# Generated at 2022-06-13 03:59:57.670780
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module = AnsibleModule(argument_spec={})
    hpux_virtual_obj = HPUXVirtual(module)

    # Test 1: API vecheck is available, so Virtualization type will be guest and Virtualization role will be HP vPar
    hpux_virtual_obj.module.run_command = mock_run_command_success
    hpux_virtual_obj.module.run_command.return_value = (0, "HP-UX HP-VirtualServer B.11.23 U ia64", "")
    hpux_virtual_obj.get_virtual_facts()
    assert hpux_virtual_obj._virtual_facts['virtualization_type'] == 'guest'
    assert hpux_virtual_obj._virtual_facts['virtualization_role'] == 'HP vPar'

    # Test 2: API hpvminfo is available, so

# Generated at 2022-06-13 04:00:07.274216
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpux.hpux import HPUXVirtual
    from ansible.module_utils.facts.virtual.hpux.hpux import HPUXVirtualCollector
    from ansible.module_utils.facts.virtual.hpux.hpux import _load_ansible_module_from_params

    virtual_facts = HPUXVirtual().get_virtual_facts()

    assert ('virtualization_type' in virtual_facts)
    assert ('virtualization_role' in virtual_facts)
    assert ('virtualization_tech_guest' in virtual_facts)
    assert ('virtualization_tech_host' in virtual_facts)

    #if running on a hypervisor, replace the module with a mock
    if virtual_facts['virtualization_type'] == 'host':
        VirtualCollector._module = _

# Generated at 2022-06-13 04:00:10.030178
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual = HPUXVirtual()
    virtual.populate()
    assert virtual.data['virtualization_type'] == 'guest'
    assert virtual.data['virtualization_role'] == 'HP vPar'
    assert virtual.data['virtualization_tech_guest'] == {'HP vPar'}
    assert virtual.data['virtualization_tech_host'] == set()

# Generated at 2022-06-13 04:00:12.681436
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual = HPUXVirtual()
    assert hpux_virtual.module == None


# Generated at 2022-06-13 04:00:14.508302
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual = HPUXVirtual(dict(module=dict()))
    assert hpux_virtual.platform == 'HP-UX'


# Generated at 2022-06-13 04:00:24.452867
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    v = HPUXVirtual({})
    v.module = MagicMock()

# Generated at 2022-06-13 04:00:37.966490
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    # Test HP vPar
    module = HPUXVirtualCollector(dict(module_args=dict(gather_subset='!all')))
    module.module.run_command = mock_run_command
    module.module.run_command.return_value = (0, out_HPUXVirtual_vecheck, '')
    virtual_facts = module.get_virtual_facts()
    assert 'HP vPar' in virtual_facts['virtualization_tech_guest']
    assert virtual_facts['virtualization_type'] == 'guest'
    assert virtual_facts['virtualization_role'] == 'HP vPar'
    module.module.run_command.return_value = (0, out_HPUXVirtual_vecheck_not_guest, '')
    virtual_facts = module.get_virtual_facts()
   

# Generated at 2022-06-13 04:00:40.187415
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    v = HPUXVirtual({})
    assert "HPUXVirtual" == v.__class__.__name__
    assert "Virtual" == v.__class__.__bases__[0].__name__


# Generated at 2022-06-13 04:00:45.118996
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    # system/virtual is a dict with keys as below
    # gather_subset: ['all']
    # gather_timeout: 10
    system_virtual = {'gather_subset': ['all']}

    # module is a dict with keys as below
    # params: {'gather_subset': ['all']}
    # failed: False
    # message: ''
    # invocation: {'module_name': 'setup', 'module_args': {'filter': 'ansible_virtual'}}
    module = {'params': {'gather_subset': ['all']}, 'failed': False, 'message': '', 'invocation': {'module_name': 'setup', 'module_args': {'filter': 'ansible_virtual'}}}

    # This fake_module will be replace by original module

# Generated at 2022-06-13 04:00:48.105318
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts = HPUXVirtual(dict(), dict()).get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'host'
    assert len(virtual_facts['virtualization_tech_host']) == 1


# Generated at 2022-06-13 04:00:58.638682
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpu import HPUXVirtual
    from ansible.module_utils.facts.virtual.hpu import HPUXVirtualCollector
    from ansible.module_utils.facts import FactModule
    import sys
    try:
        import __builtin__
        builtin_module = __builtin__
    except ImportError:
        import builtins
        builtin_module = builtins
    original_import = builtin_module.__import__

    def import_mock(name, *args):
        if name == 'ansible.module_utils.facts.virtual.base':
            raise ImportError
        return original_import(name, *args)

    builtin_module.__import__ = import_mock


# Generated at 2022-06-13 04:01:06.719217
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    """
    Unit test for get_virtual_facts method.
    """
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual
    from ansible.module_utils.facts.virtual import Virtual
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtualCollector

    class TestModule(object):
        def run_command(self, arg):
            if arg == '/usr/sbin/vecheck':
                return [0, "./vecheck: HP virtual partition information\n./vecheck: Virtual Partition environment: OK", ""]
            elif arg == '/opt/hpvm/bin/hpvminfo':
                return [0, "HPVM guest", ""]

# Generated at 2022-06-13 04:01:15.548120
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    import os
    import tempfile

    from ansible.module_utils.facts.virtual.hpu import HPUXVirtual

    # Test on a system without vecheck and hpvminfo
    with tempfile.TemporaryDirectory() as tdir:
        orig_path = os.getenv('PATH')
        os.environ['PATH'] = tdir + ':' + orig_path
        virtual_facts = HPUXVirtual().get_virtual_facts()
        assert (not virtual_facts['virtualization_tech_host'])
        assert (not virtual_facts['virtualization_tech_guest'])
        os.environ['PATH'] = orig_path

    # Test on a system with vecheck
    with tempfile.TemporaryDirectory() as tdir:
        vecheck_path = os.path.join(tdir, 'vecheck')

# Generated at 2022-06-13 04:01:20.490525
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual()
    assert hv.virtualization_type == 'guest'
    assert hv.virtualization_role == 'HP vPar'
    assert hv.virtualization_tech_guest == set(['HP vPar'])
    assert hv.virtualization_tech_host == set()
    assert hv.platform == 'HP-UX'

# Generated at 2022-06-13 04:01:21.946033
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpuxvirtual = HPUXVirtual()
    assert hpuxvirtual.platform == 'HP-UX'
    assert hpuxvirtual.virtual == {}
    assert hpuxvirtual.get_virtual_facts() == {}

# Generated at 2022-06-13 04:01:31.043837
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtualCollector
    from ansible.module_utils.facts.virtual import Virtual, VirtualCollector
    from ansible.module_utils.facts import ModuleStub

    hpux_virtual = HPUXVirtual(ModuleStub())
    hpux_virtual.collect()
    virtual_facts = hpux_virtual.get_virtual_facts()
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert virtual_facts['virtualization_role'] == 'HP nPar'
    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts
    assert HPU

# Generated at 2022-06-13 04:01:53.985172
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_collector = HPUXVirtualCollector()
    virtual_facts = virtual_collector.collect()
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts

# Generated at 2022-06-13 04:01:58.764021
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    v_obj = HPUXVirtual()
    assert v_obj.platform == 'HP-UX'
    assert not hasattr(v_obj, 'virtualization_type')
    assert not hasattr(v_obj, 'virtualization_role')
    assert not hasattr(v_obj, 'virtualization_tech_host')
    assert not hasattr(v_obj, 'virtualization_tech_guest')


# Generated at 2022-06-13 04:02:00.438456
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )
    hpux_virtual = HPUXVirtual(module)
    assert hpux_virtual.platform == 'HP-UX'


# Generated at 2022-06-13 04:02:01.704198
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpuxv = HPUXVirtual()
    assert hpuxv.platform == 'HP-UX'


# Generated at 2022-06-13 04:02:07.944129
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    m = HPUXVirtual({})
    d = dict()
    
    # Test option 1: Empty return
    d = m.get_virtual_facts()
    assert (d['virtualization_type'] == 'guest' and
            d['virtualization_role'] == 'HPVM IVM' and
            d['virtualization_tech_host'] == set() and
            d['virtualization_tech_guest'] == set(['HPVM IVM']))
    
    # Test option 2: Empty return
    d = m.get_virtual_facts()

# Generated at 2022-06-13 04:02:10.573037
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts = HPUXVirtual()
    assert virtual_facts._platform == 'HP-UX'


# Generated at 2022-06-13 04:02:13.624047
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    class TestModule(object):
        def run_command(self, *args, **kwargs):
            return 0, '', ''

    HPUXVirtual.module = TestModule()

    vObj = HPUXVirtual()
    vObj.get_virtual_facts()



# Generated at 2022-06-13 04:02:19.104829
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module = AnsibleModuleMock()
    module.run_command = AnsibleModuleMock.run_command
    module.run_command.side_effect = [
        (0, '', ''),
        (0, '', ''),
        (0, '', ''),
        (0, '', ''),
    ]
    h_virtual = HPUXVirtual(module)
    virtual_facts = h_virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'host'
    assert virtual_facts['virtualization_role'] == 'HPVM'
    assert virtual_facts['virtualization_tech_guest'] == set(['HPVM'])
    assert virtual_facts['virtualization_tech_host'] == set()

# Generated at 2022-06-13 04:02:19.882022
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module = None
    obj = HPUXVirtual(module)
    obj.get_virtual_facts()



# Generated at 2022-06-13 04:02:29.485492
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    '''
    Unit test method get_virtual_facts of class HPUXVirtual
    '''
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtualCollector

    virtual_obj = HPUXVirtual(dict(ANSIBLE_MODULE_ARGS={}))
    virtual_obj._module.run_command = lambda x: (0, "", "")
    virtual_obj._module.get_bin_path = lambda x: "/usr/sbin/parstatus"
    virtual_obj.get_virtual_facts()
    assert virtual_obj.virtual_facts['virtualization_type'] == 'guest'
    assert virtual_obj.virtual_facts['virtualization_role'] == 'HP nPar'

    virtual_obj

# Generated at 2022-06-13 04:03:01.951158
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_obj = HPUXVirtual({})
    assert virtual_obj.platform == 'HP-UX'
    assert virtual_obj.get_virtual_facts() == {}


# Generated at 2022-06-13 04:03:03.079034
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual = HPUXVirtual(dict())


if __name__ == '__main__':
    test_HPUXVirtual()

# Generated at 2022-06-13 04:03:05.851976
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    h = HPUXVirtual({})
    assert h.platform == 'HP-UX'
    assert not h.get_virtual_facts()


# Generated at 2022-06-13 04:03:07.626941
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    test_obj = HPUXVirtual(dict())
    assert test_obj


# Generated at 2022-06-13 04:03:16.506168
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts1 = {'virtualization_type': 'guest',
                      'virtualization_role': 'HP vPar'}
    virtual_facts2 = {'virtualization_type': 'guest',
                      'virtualization_role': 'HPVM vPar'}
    virtual_facts3 = {'virtualization_type': 'guest',
                      'virtualization_role': 'HPVM IVM'}
    virtual_facts4 = {'virtualization_type': 'host',
                      'virtualization_role': 'HPVM'}
    virtual_facts5 = {'virtualization_type': 'guest',
                      'virtualization_role': 'HP nPar'}

    virtual = HPUXVirtual()
    virtual.module = mock.MagicMock()

# Generated at 2022-06-13 04:03:21.762051
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual = HPUXVirtual()
    facts = hpux_virtual.get_virtual_facts()
    assert 'virtualization_type' in facts
    assert 'virtualization_role' in facts
    assert 'virtualization_tech_guest' in facts
    assert 'virtualization_tech_host' in facts
    assert facts['virtualization_type'] in ['host', 'guest']


# Generated at 2022-06-13 04:03:29.532216
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    v = HPUXVirtual({})
    assert v.facts['virtualization_type'] == 'host'
    assert not v.facts['virtualization_role']
    assert not v.facts['virtualization_tech_guest']
    assert not v.facts['virtualization_tech_host']

    v = HPUXVirtual({}, "test")
    assert v.facts['virtualization_type'] == 'host'
    assert not v.facts['virtualization_role']
    assert not v.facts['virtualization_tech_guest']
    assert not v.facts['virtualization_tech_host']



# Generated at 2022-06-13 04:03:39.883726
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():

    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts import Collector
    from ansible.module_utils.facts.virtual.hpar import HPUXVirtual

    def run_command(self, cmd, check_rc=True, close_fds=True, executable=None,
                    data=None, binary_data=False):
        module = self
        print(cmd)
        facts = {}
        if cmd == "/usr/sbin/parstatus":
            class HPAR:
                rc = 0
                out = to_bytes('')
                err = to_bytes('')
            return HPAR
        if cmd == "/usr/sbin/vecheck":
            class VECHECK:
                rc = 0

# Generated at 2022-06-13 04:03:48.286068
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module = AnsibleModuleMockHPUX()
    module.run_command = mock.Mock()

# Generated at 2022-06-13 04:03:49.607754
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    s = HPUXVirtual()
    assert s.platform == 'HP-UX'

# Generated at 2022-06-13 04:04:24.899546
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual
    AClass = HPUXVirtual()
    test_facts = AClass.get_virtual_facts()
    assert test_facts['virtualization_type'] == 'host'
    assert test_facts['virtualization_role'] == 'HPVM'
    assert 'HPVM' in test_facts['virtualization_tech_host']
    assert 'HPVM' in test_facts['virtualization_tech_guest']

# Generated at 2022-06-13 04:04:27.677677
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    module = FakeAnsibleModule()
    hpuxvirtual = HPUXVirtual(module)
    assert hpuxvirtual is not None



# Generated at 2022-06-13 04:04:29.673558
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual = HPUXVirtual({})
    assert hpux_virtual.platform == 'HP-UX'
    assert hpux_virtual.module == {}


# Generated at 2022-06-13 04:04:31.752873
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual = HPUXVirtual(dict(), dict())
    assert virtual.platform == "HP-UX"


# Generated at 2022-06-13 04:04:40.225851
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    """
    Unit testing for method get_virtual_facts of class HPUXVirtual
    """

    import ansible.module_utils.facts.virtual.hpux as hpux

    # Setting up a dummy class for the unit test
    class DummyHPUXVirtual(hpux.HPUXVirtual):
        """
        This is a dummy class for unit testing.
        """
        platform = 'HP-UX'

        def __init__(self, *args, **kwargs):
            """
            Constructor of the class.
            """
            self.module = None

    # Setting up a dummy module for the unit test

# Generated at 2022-06-13 04:04:42.808972
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts = HPUXVirtual()
    assert virtual_facts.platform == 'HP-UX'
    virtual_facts.get_virtual_facts()


# Generated at 2022-06-13 04:04:48.978164
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    class MockModule(object):
        def __init__(self):
            self.run_command = Mock(return_value=(0, 'some_output', ''))

    class MockHPUXVirtual(HPUXVirtual):
        def __init__(self):
            self.module = MockModule()

    MockHPUXVirtual._platform = 'HP-UX'
    hpux_virtual = MockHPUXVirtual()

    # vecheck exists and output is 'Running HP vPar
    hpux_virtual.module.run_command = Mock(return_value=(0, 'Running HP vPar', ''))
    os.path.exists = Mock(return_value=True)
    assert hpux_virtual.get_virtual_facts()['virtualization_type'] == 'guest'

    # vecheck exists and output is 'Running HP VM guest'

# Generated at 2022-06-13 04:04:59.567752
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts import _VirtualFactCollector
    from ansible.module_utils.facts.virtual import HPUXVirtualCollector
    from ansible.module_utils.facts.virtual.posix import POSIXVirtual
    from ansible.module_utils.facts.virtual.base import Virtual
    from ansible.module_utils.facts.virtual.base import VirtualCollector

    # List of return values by mocked functions
    # Define here arguments that would normally be provided by the thing they are mocking
    vecheck_out = ('', 0)
    hpvminfo_out = ('', 0)
    parstatus_out = ('', 0)

    class MockModule(object):
        def __init__(self):
            self.run_command = lambda x: eval(x + '_out')


# Generated at 2022-06-13 04:05:07.671458
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    # Create an instance of class HP-UXVirtual
    module = AnsibleModule(
        argument_spec={
            'collect_facts': {'type': 'bool', 'default': True},
            'filter': {'type': 'list'},
        }
    )

    # Create an instance of class HPUXVirtual and get virtual facts
    hpux = HPUXVirtual(module)
    virtual_facts = hpux.get_virtual_facts()

    # Assert whether virtualization_type and virtualization_role are set to correct value
    assert virtual_facts['virtualization_type'] == 'guest'
    assert virtual_facts['virtualization_role'] == 'HP vPar'

    # Assert whether virtualization_tech_guest and virtualization_tech_host are set to correct value

# Generated at 2022-06-13 04:05:13.019803
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    class TestModule(object):
        pass
    test_module = TestModule()
    test_module.run_command = run_command_mock

    hpux_virtual = HPUXVirtual(test_module)
    facts = hpux_virtual.get_virtual_facts()
    assert facts['virtualization_type'] == 'guest'
    assert facts['virtualization_role'] == 'HP nPar'



# Generated at 2022-06-13 04:05:56.888463
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    assert HPUXVirtual().data['virtualization_type'] == 'guest'
    assert HPUXVirtual().data['virtualization_role'] == 'HP vPar'
    assert HPUXVirtual().data['virtualization_tech_host'] == set()
    assert HPUXVirtual().data['virtualization_tech_guest'] == {'HP vPar'}


# Generated at 2022-06-13 04:06:07.814295
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual
    from ansible.module_utils.six import PY2
    from ansible.module_utils.six.moves import builtins

    class AnsibleModuleMock():
        def __init__(self):
            self.run_command = lambda x: (0, "output", "")

    class Fake_HPUXVirtual(HPUXVirtual):
        def get_virtual_facts(self):
            return {
                'virtualization_role': 'HP vPar'
            }

    try:
        pwd = builtins.__dict__['__builtins__']['__import__']('pwd')
        user = pwd.getpwuid(os.getuid())[0]
    except Exception:
        user = 'ansible'

# Generated at 2022-06-13 04:06:19.383592
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    fake_module = FakeAnsibleModule()
    fake_module.mock_command("/usr/sbin/vecheck", 0, "")
    fake_module.mock_command("/opt/hpvm/bin/hpvminfo", 0, "")
    fake_module.mock_command("/usr/sbin/parstatus", 0, "")
    virtual = HPUXVirtual(fake_module)

    virtual.get_virtual_facts()

    assert(fake_module.run_command.call_count == 3)
    fake_module.run_command.assert_any_call("/usr/sbin/vecheck")
    fake_module.run_command.assert_any_call("/opt/hpvm/bin/hpvminfo")

# Generated at 2022-06-13 04:06:27.211847
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    import sys
    import unittest
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual

    class TestAnsibleModuleUtilsFactsVirtualHpux(unittest.TestCase):
        '''
        Unit tests for method get_virtual_facts of class HP-UXVirtual
        '''
        # pylint: disable=too-many-public-methods,missing-docstring

        # TODO: implement tests
        def test_1(self):
            self.assertEqual(1, 1)

    if __name__ == '__main__':
        unittest.main()

# Generated at 2022-06-13 04:06:29.536289
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_obj = HPUXVirtualCollector()
    assert virtual_obj._platform == 'HP-UX'

# Generated at 2022-06-13 04:06:30.945083
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    x = HPUXVirtual(dict())
    assert type(x) == HPUXVirtual

# Generated at 2022-06-13 04:06:37.177479
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    HPUXVirtual_test = HPUXVirtual(dict(module=dict(run_command=fake_run_command)))
    facts = dict()
    facts['virtualization_type'] = 'guest'
    facts['virtualization_role'] = 'HPVM IVM'
    facts['virtualization_tech_guest'] = set(['HPVM IVM'])
    facts['virtualization_tech_host'] = None
    assert facts == HPUXVirtual_test.get_virtual_facts()


# Generated at 2022-06-13 04:06:41.975224
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    #Create instance of class HPUXVirtual
    hpxvirtual = HPUXVirtual()
    hpxvirtual_result = {
       "virtualization_role": "",
       "virtualization_type": "",
       "virtualization_tech_guest": set(),
       "virtualization_tech_host": set(),
       "virtualization_systems": []
    }
    assert hpxvirtual.get_virtual_facts() == hpxvirtual_result

# Generated at 2022-06-13 04:06:44.785086
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    module = AnsibleModuleMock()
    v = HPUXVirtual(module)
    assert v
    assert v.platform == HPUXVirtual.platform


# Generated at 2022-06-13 04:06:46.122451
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    h_virtual = HPUXVirtual()
    assert h_virtual is not None

# Generated at 2022-06-13 04:09:00.197095
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    """
    This function unit test the get_virtual_facts() method of the HPUXVirtual class
    :return:
    """
    hv = HPUXVirtual()

    hv.is_file_exists_mock = lambda x: False
    ret = hv.get_virtual_facts()
    assert ret == {'virtualization_tech_host': set(), 'virtualization_tech_guest': set(),
                   'virtualization_type': '', 'virtualization_role': ''}

    hv.is_file_exists_mock = lambda x: True
    hv.is_dir_exists_mock = lambda x: False
    hv.run_command_mock = lambda x: (0, 'fake', '')
    ret = hv.get_virtual_facts()

# Generated at 2022-06-13 04:09:02.009506
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual()
    assert hv.platform == 'HP-UX'

# Generated at 2022-06-13 04:09:03.554629
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual({}, {})
    assert hv.platform == 'HP-UX'


# Generated at 2022-06-13 04:09:05.021927
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    v = HPUXVirtual({}, {})
    assert v._platform is 'HP-UX'


# Generated at 2022-06-13 04:09:06.750178
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virt = HPUXVirtual()
    assert virt.facts['virtualization_type'] == 'host'

# Generated at 2022-06-13 04:09:10.407078
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpx_virtual = HPUXVirtual('ansible.module_utils.facts.virtual.HPUXVirtual')
    assert hpx_virtual.platform == 'HP-UX'

if __name__ == '__main__':
    test_HPUXVirtual()

# Generated at 2022-06-13 04:09:11.809902
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    obj = HPUXVirtual()
    assert obj.platform == 'HP-UX'

# Generated at 2022-06-13 04:09:12.884361
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    assert HPUXVirtual(None).platform == 'HP-UX'

# Generated at 2022-06-13 04:09:19.604535
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    import sys
    # support for multiple versions of python
    file_relative_path = os.path.dirname(__file__)
    __mod_name__ = os.path.splitext(os.path.basename(__file__))[0]
    # test methods are named as test_<test_id>_<method_id>_<input_id>
    # test_id is either 'unit' or 'integration'
    test_id = __mod_name__.split('_')[1]
    # method to be tested
    test_method = sys.modules[__name__].__dict__.get(__mod_name__).__dict__.get('HPUXVirtual').get_virtual_facts
    # name of the class