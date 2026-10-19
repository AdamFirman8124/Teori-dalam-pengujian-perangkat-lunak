

# Generated at 2022-06-13 03:59:36.860022
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    from ansible.module_utils.facts.virtual.hpu import HPUXVirtual
    virtual_facts = HPUXVirtual()
    assert virtual_facts is not None
    assert os.path.exists('/usr/sbin/vecheck') is False
    assert os.path.exists('/opt/hpvm/bin/hpvminfo') is False
    assert os.path.exists('/usr/sbin/parstatus') is False
    assert virtual_facts.get_virtual_facts() == \
        {
            'virtualization_tech_host': set(),
            'virtualization_tech_guest': set()
        }

# Generated at 2022-06-13 03:59:38.121218
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual = HPUXVirtual(dict())
    assert virtual


# Generated at 2022-06-13 03:59:43.296008
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    class ModuleMock(object):
        def __init__(self, **kwargs):
            pass

        def run_command(self, *args, **kwargs):
            return 0, '', ''

    module = ModuleMock()
    hpux = HPUXVirtual(module)
    virtual_facts = hpux.get_virtual_facts()
    assert virtual_facts == {'virtualization_role': 'HP nPar',
                             'virtualization_type': 'guest',
                             'virtualization_tech_guest': {'HPVM IVM',
                                                           'HPVM vPar',
                                                           'HP nPar'},
                             'virtualization_tech_host': set()}

# Generated at 2022-06-13 03:59:52.403623
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    import module_utils.facts.virtual.hpux as hpux_virtual_mod

    hpux_virtual_obj = hpux_virtual_mod.HPUXVirtual({})

    def isfile_return(path):
        if path == '/usr/sbin/vecheck':
            return True
        elif path == '/opt/hpvm/bin/hpvminfo':
            return True
        elif path == '/usr/sbin/parstatus':
            return True
        else:
            return False

    def file_exist_sideeffect_1(path):
        if path == '/usr/sbin/vecheck':
            return True
        elif path == '/opt/hpvm/bin/hpvminfo':
            return True
        elif path == '/usr/sbin/parstatus':
            return True

# Generated at 2022-06-13 03:59:54.690214
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    """
    This method is used to test the constructor of class HPUXVirtual.
    """
    virtual = HPUXVirtual()
    assert virtual.platform == 'HP-UX'


# Generated at 2022-06-13 03:59:57.179490
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    sut = HPUXVirtual()
    assert sut._platform == 'HP-UX'
    assert sut.platform == 'HP-UX'
    assert sut._fact_class == HPUXVirtual


# Generated at 2022-06-13 04:00:04.224240
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    """
    Unit test for method get_virtual_facts of class HPUXVirtual
    """

    class ModuleMock(object):
        """
        Mock class for AnsibleModule
        """
        def __init__(self):
            self.params = {}
            self.exit_json = exit_json
            self.fail_json = fail_json

    class ExitJsonException(Exception):
        """
        Exception class for exit_json
        """
        pass

    class FailJsonException(Exception):
        """
        Exception class for fail_json
        """
        pass

    def exit_json(*args, **kwargs):
        """
        Mock for exit_json
        """
        if 'changed' in kwargs:
            raise ExitJsonException(kwargs['changed'])
        else:
            raise ExitJsonException

# Generated at 2022-06-13 04:00:15.340281
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():

    def run_mock(module, cmd):
        class A:
            pass
        r = A()
        r.rc = 0
        r.stdout = cmd
        r.stderr = ''
        return r

    module = AnsibleModule(argument_spec={})
    module.run_command = run_mock
    hpuxvirtual = HPUXVirtual(module)
    result = hpuxvirtual.get_virtual_facts()
    assert 'virtualization_type' in result
    assert 'virtualization_role' in result
    assert 'virtualization_tech_host' in result
    assert 'virtualization_tech_guest' in result
    assert 'virtualization_tech' in result
    assert result['virtualization_tech_guest'] == set()
    assert result['virtualization_tech_host'] == set()

# Generated at 2022-06-13 04:00:24.506460
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    Params = {'ANSIBLE_MODULE_ARGS': {'gather_subset': ['all'], 'gather_timeout': 10, 'filter': '*'}}

    class MockModule(object):
        def __init__(self):
            self.params = Params

        def get_bin_path(self, arg, required=False, opt_dirs=[]):
            return '/bogus/bin/path'

        def run_command(self, cmd):
            if re.match('.*/usr/sbin/vecheck.*', cmd):
                return 0, '', ''
            elif re.match('.*/opt/hpvm/bin/hpvminfo.*', cmd):
                return 0, 'Running as HPVM vPar', ''

# Generated at 2022-06-13 04:00:26.940542
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    _fact_class = HPUXVirtual()
    assert _fact_class.platform == 'HP-UX'

# Generated at 2022-06-13 04:00:42.019708
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts import get_virtual_facts

    # Test for the case when vecheck file exists
    vecheck_virtual_facts = {
        'virtualization_type': 'guest',
        'virtualization_role': 'HP vPar',
        'virtualization_tech_guest': {'HP vPar'},
        'virtualization_tech_host': set()
    }
    assert get_virtual_facts(HPUXVirtual, 'HP-UX', ['/usr/sbin/vecheck']) == vecheck_virtual_facts

    # Test for the case when hpvminfo exists and is a vPar

# Generated at 2022-06-13 04:00:50.172219
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    """
    Unit test for method get_virtual_facts of class HPUXVirtual
    """
    import ansible.module_utils.facts.virtual.hpux_virtual as hpuxvirtual
    from ansible.module_utils.facts import Collector
    import ansible.module_utils.facts.virtual.base as base

    module = hpuxvirtual.AnsibleModuleMock()
    hpux_collector = HPUXVirtualCollector(module=module)
    hpux_fact = hpux_collector.collect()[base.VM_CLASS_NAME]
    assert hpux_fact.virtualization_type == "guest"
    assert hpux_fact.virtualization_role == "HP vPar"
    assert hpux_fact.virtualization_tech_host == set()
    assert hpux_fact.virtualization_tech_guest

# Generated at 2022-06-13 04:00:52.860665
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual("module")
    assert hv.platform == 'HP-UX'
    assert hv.get_virtual_facts() == {'virtualization_type': 'guest', 'virtualization_role': 'HP vPar'}

# Generated at 2022-06-13 04:00:55.174042
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts = HPUXVirtual({'module': None, 'share': None})
    assert virtual_facts.platform == 'HP-UX'

# Generated at 2022-06-13 04:00:58.189129
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual({})
    assert hv.platform == 'HP-UX'

# Generated at 2022-06-13 04:00:59.822594
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts = HPUXVirtual()

    assert virtual_facts.platform == 'HP-UX'

# Generated at 2022-06-13 04:01:03.629034
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    module = MockAnsibleModule()
    module.params = { 'gather_subset': [] }
    obj = HPUXVirtual(module=module)
    obj._get_facts()
    assert(obj.facts['virtualization_role'] == 'HPVM vPar')



# Generated at 2022-06-13 04:01:07.617253
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpuxv = HPUXVirtual()
    print(hpuxv.get_virtual_facts())

if __name__ == '__main__':
    test_HPUXVirtual()

# Generated at 2022-06-13 04:01:15.927059
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    # Dummy module
    class DummyModule:
        def run_command(self, command):
            class dummy_command:
                def __init__(self):
                    self.rc = 1
            return dummy_command()
    dummy_module = DummyModule()
    # Dummy module with run_command to return vpar status
    class dummy_run_command_vecheck:
        def __init__(self):
            self.rc = 0
    dummy_module1 = DummyModule()
    dummy_module1.run_command = dummy_run_command_vecheck()
    # Dummy module with run_command to return hpvm status
    class dummy_run_command_hpvminfo:
        def __init__(self):
            self.rc = 0
            self.out = "Running HPVM host"
    dummy_module

# Generated at 2022-06-13 04:01:20.490351
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    '''
    Test get_virtual_facts method of HPUXVirtual class
    '''
    module = agnostic_fake_module_builder()

    module.run_command = lambda x: (0, '', '')

    hpuxvirtual = HPUXVirtual(module)

    assert hpuxvirtual.get_virtual_facts() == {}


# Generated at 2022-06-13 04:01:33.079938
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    module = FakeAnsibleModule()
    hpuxvirtual = HPUXVirtual(module)
    assert hpuxvirtual.platform == 'HP-UX'



# Generated at 2022-06-13 04:01:35.141376
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    v = HPUXVirtual({})
    assert isinstance(v, Virtual)
    assert v.platform == 'HP-UX'


# Generated at 2022-06-13 04:01:36.722016
# Unit test for method get_virtual_facts of class HPUXVirtual

# Generated at 2022-06-13 04:01:37.998279
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    # TODO: need to update the test with appropriate data
    pass

# Generated at 2022-06-13 04:01:39.345271
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    h = HPUXVirtual()
    assert h.get_virtual_facts()

# Generated at 2022-06-13 04:01:41.308179
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts = {}
    virtual_module = HPUXVirtual(virtual_facts)
    # TODO: Mock VTS and add unit test

# Generated at 2022-06-13 04:01:42.768076
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual = HPUXVirtual(dict(module=dict()))
    assert virtual.platform == 'HP-UX'

# Generated at 2022-06-13 04:01:44.141428
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virt = HPUXVirtual()
    assert virt.platform == 'HP-UX'


# Generated at 2022-06-13 04:01:45.777848
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual = HPUXVirtual()
    assert virtual.platform == "HP-UX"

# Generated at 2022-06-13 04:01:49.895247
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    """
    Test parameters of HPUXVirtual constructor
    """
    h = HPUXVirtual({})
    assert h.platform == 'HP-UX'
    assert h.guest_tech == set()
    assert h.host_tech == set()

# Generated at 2022-06-13 04:02:01.359537
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    obj = HPUXVirtual()
    assert obj.virtualization_type == {}
    assert obj.virtualization_role == {}
    assert obj.virtualization_tech_host == set()
    assert obj.virtualization_tech_guest == set()
    assert obj.platform == 'HP-UX'


# Generated at 2022-06-13 04:02:02.592195
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual = HPUXVirtual()

    assert hpux_virtual.platform == 'HP-UX'

# Generated at 2022-06-13 04:02:03.811849
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_obj = HPUXVirtual({})
    assert virtual_obj.platform == 'HP-UX'


# Generated at 2022-06-13 04:02:05.030877
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual({})
    assert hv.platform == 'HP-UX'

# Generated at 2022-06-13 04:02:10.421124
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    import tempfile
    import shutil
    import sys
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual
    from ansible.module_utils.facts.virtual.hpux import VirtualCollector

    # Make temporary directory, with
    # - file /usr/sbin/vecheck
    # - file /opt/hpvm/bin/hpvminfo
    # - file /usr/sbin/parstatus
    _temp_dir = to_bytes(tempfile.mkdtemp())
    _bin_dir = os.path.join(_temp_dir, b'bin')
    os.mkdir(_bin_dir)

    _vecheck_file = os.path.join(_bin_dir, b'vecheck')

# Generated at 2022-06-13 04:02:16.207363
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts_dict = HPUXVirtual(dict()).get_virtual_facts()
    assert virtual_facts_dict['virtualization_type'] == 'guest'
    assert virtual_facts_dict['virtualization_role'] == 'HP vPar'
    assert 'HPVM' in virtual_facts_dict['virtualization_tech_host']
    assert 'HPVM vPar' in virtual_facts_dict['virtualization_tech_guest']
    assert 'HPVM IVM' in virtual_facts_dict['virtualization_tech_guest']
    assert 'HP nPar' in virtual_facts_dict['virtualization_tech_guest']

# Generated at 2022-06-13 04:02:16.633594
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    HPUXVirtual()

# Generated at 2022-06-13 04:02:21.559745
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    """
    This function returns a dict of virtualization facts for a
    HP-UX virtualization system
    """
    from ansible.module_utils.facts.virtual.hpux.test_hpux_virtual import (
        MockModule, MockRunner)
    module = MockModule()
    runner = MockRunner()
    hpux_virtual = HPUXVirtual(module, runner=runner)
    hpux_virtual.get_virtual_facts()
    assert hpux_virtual.virtual_facts['virtualization_tech_guest'] == \
           set(['HP vPar', 'HPVM vPar', 'HPVM IVM', 'HPVM', 'HP nPar'])
    assert hpux_virtual.virtual_facts['virtualization_tech_host'] == \
           set()
    assert hpux_virtual.virtual_facts['virtualization_type']

# Generated at 2022-06-13 04:02:31.211267
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module = AnsibleModule(argument_spec={})
    virtual = HPUXVirtual(module)

    # unit test: if vecheck installed and parstatus not installed, returns HP vPar
    module.run_command = MagicMock(return_value=(0, '', ''))
    module.file_exists = MagicMock(side_effect=[True, False])
    assert virtual.get_virtual_facts() == {'virtualization_type': 'guest',
                                           'virtualization_role': 'HP vPar',
                                           'virtualization_tech_host': set(),
                                           'virtualization_tech_guest': {'HP vPar'}}

    # unit test: if vecheck and parstatus installed, returns HP vPar
    module.run_command = MagicMock(return_value=(0, '', ''))


# Generated at 2022-06-13 04:02:32.333449
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    a = HPUXVirtual()
    assert a.platform == 'HP-UX'


# Generated at 2022-06-13 04:02:50.255046
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes

    m = basic.AnsibleModule(argument_spec={})

    v = HPUXVirtual(m)
    v.module.run_command = lambda *args, **kwargs: (0, '', '')

    assert 'virtualization_role' in v.get_virtual_facts()

# Generated at 2022-06-13 04:02:51.258593
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    import pytest
    factory = HPUXVirtual()
    assert factory.platform == 'HP-UX'


# Generated at 2022-06-13 04:02:52.433147
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual = HPUXVirtual()
    assert virtual.platform == 'HP-UX'

# Generated at 2022-06-13 04:02:52.969866
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    HPUXVirtual()

# Generated at 2022-06-13 04:03:02.727852
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():

    from ansible.module_utils.facts.virtual import HPUXVirtual
    from ansible.module_utils.facts.virtual.hpux.hpux_virtual import HPUXVirtualCollector
    from ansible.module_utils.facts import HPSSACommand

    class FakeModule:
        def __init__(self, name, params):
            pass


# Generated at 2022-06-13 04:03:07.922824
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpar import HPUXVirtual
    hpar = HPUXVirtual()
    facts = hpar.get_virtual_facts()
    assert facts['virtualization_type'] == 'guest'
    assert facts['virtualization_role'] == 'HP nPar'
    assert facts['virtualization_tech_guest'] == set(['HP nPar'])
    assert facts['virtualization_tech_host'] == set()


# Generated at 2022-06-13 04:03:10.590683
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual = HPUXVirtual({'module_setup':True})
    assert hpux_virtual.module == None
    assert hpux_virtual.platform == 'HP-UX'

# Generated at 2022-06-13 04:03:19.469915
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts import ansible_facts

    module = None
    facts = ansible_facts.AnsibleFacts(module)
    virtual = HPUXVirtual(facts)

    # HP vPar
    if os.path.isfile('/usr/sbin/vecheck'):
        virtual._executable_exists['vecheck'] = True
    # HPVM
    if os.path.isfile('/opt/hpvm/bin/hpvminfo'):
        virtual._executable_exists['hpvminfo'] = True
    # HP nPar
    if os.path.isfile('/usr/sbin/parstatus'):
        virtual._executable_exists['parstatus'] = True

    virtual_facts = virtual.get_virtual_facts()
    assert 'virtualization_type'

# Generated at 2022-06-13 04:03:21.525860
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    # Test hptru64 module
    hptru64 = HPUXVirtual()
    assert hptru64.platform == 'HP-UX'

# Generated at 2022-06-13 04:03:23.578059
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virt = HPUXVirtual(None)
    assert virt.platform == 'HP-UX'
    assert virt.module == None

# Generated at 2022-06-13 04:03:51.436227
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    virt = HPUXVirtual(None)
    assert virt.get_virtual_facts() == {}

# Generated at 2022-06-13 04:03:59.263993
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    """
    Test virtual_facts returns the correct information for HP-UX
    """
    fake_module = type('', (object,), {
        'run_command': lambda self, args: (
            0, 'Running HPVM vPar', '') if args == "/opt/hpvm/bin/hpvminfo"
            else (0, 'HP nPar', '') if args == "/usr/sbin/parstatus"
            else (0, '', ''),
        'params': {},
        'exit_json': lambda self, **args: args,
        'fail_json': lambda self, **args: args,
    })()

    virtual = HPUXVirtual(fake_module)
    virtual_facts = virtual.get_virtual_facts()
    assert virtual_facts['virtualization_role'] == "HPVM vPar"
   

# Generated at 2022-06-13 04:04:01.161256
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpx = HPUXVirtual(None)
    assert hpx.platform == 'HP-UX'
    assert hpx.__class__.__name__ == 'HPUXVirtual'
    assert hpx._Virtual__module is None

# Generated at 2022-06-13 04:04:05.944382
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    facts_dict = {}
    class HPUXModuleMock:
        params = {'gather_subset':'!all,!min'}
        def run_command(self, command):
            if command == '/usr/sbin/vecheck':
                return (0, '', '')
            elif command == '/opt/hpvm/bin/hpvminfo':
                return (0,'Running on HPVM vPar:\n\n','')
            elif command == '/usr/sbin/parstatus':
                return (1,'','')
            else:
                return (1,'','')
    class HPUXModuleAnsibleMock():
        run_command = HPUXModuleMock().run_command
        params = {'gather_subset':'!all,!min'}
    hpux

# Generated at 2022-06-13 04:04:13.923289
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible_collections.ansible.community.tests.unit.compat.mock import create_autospec, patch, MagicMock
    from ansible_collections.ansible.community.plugins.module_utils.facts import Virtual

    module = MagicMock()
    # the constructor will run the virtual_subclass() method which
    # sets the self.subclass attribute to the subclass (HPUXVirtual)
    # instance of class Virtual.
    # So we patch the method virtual_subclass() to return HPUXVirtual
    # instance.
    module.virtual_subclass = create_autospec(Virtual.virtual_subclass)
    module.virtual_subclass.return_value = HPUXVirtual(module)
    # the constructor will run the get_virtual_facts() method which
    # sets the self.facts attribute to

# Generated at 2022-06-13 04:04:15.660767
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    """
    Unit test for get_virtual_facts of class HPUXVirtual
    """
    #TODO: add unit test
    pass

# Generated at 2022-06-13 04:04:18.036366
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    v = HPUXVirtual({})
    assert v.platform == 'HP-UX'


# Generated at 2022-06-13 04:04:19.561075
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual()
    assert hv._platform == 'HP-UX'
    assert hv._fact_class == HPUXVirtual

# Generated at 2022-06-13 04:04:24.634086
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    test_module = fake_module(
        params=dict(
            gather_subset=['!all', 'virtual'],
        )
    )
    test_HPUXVirtual = HPUXVirtual(module=test_module)
    out_expected = dict(
        virtualization_type='guest',
        virtualization_role='HP vPar',
        virtualization_tech_guest={'HP vPar'},
        virtualization_tech_host=set()
    )

    out = test_HPUXVirtual.get_virtual_facts()
    assert out == out_expected


# Generated at 2022-06-13 04:04:28.022583
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual = HPUXVirtual({})
    assert hpux_virtual.module
    assert hpux_virtual.platform == 'HP-UX'
    assert hpux_virtual._virtual_facts == {}



# Generated at 2022-06-13 04:05:04.449284
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    hv = HPUXVirtual()
    hv.module = FakeAnsibleModule()
    hv.module.run_command = lambda x: (0, 'output', '')
    facts = hv.get_virtual_facts()
    assert facts['virtualization_type'] == 'guest'
    assert facts['virtualization_role'] == 'HP vPar'
    assert facts['virtualization_tech_guest'] == set(['HP vPar'])
    assert facts['virtualization_tech_host'] == set()



# Generated at 2022-06-13 04:05:07.991029
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    v = HPUXVirtual({})
    assert v.platform == "HP-UX"
    assert v.virtualization_type == ""
    assert v.virtualization_role == ""
    assert v.virtualization_tech_guest == set()
    assert v.virtualization_tech_host == set()


# Generated at 2022-06-13 04:05:10.244985
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virt_class = HPUXVirtual()
    assert virt_class.platform == 'HP-UX'


# Generated at 2022-06-13 04:05:19.297701
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible_module_hphostfacts import MockModule
    from ansible_module_hphostfacts import MockRunner

    # Populate mocks
    mock_module = MockModule()
    mock_runner_vecheck = MockRunner(cmd=r'/usr/sbin/vecheck',
                                     rc=0,
                                     out='',
                                     err='')
    mock_runner_hpvminfo_host = MockRunner(cmd=r'/opt/hpvm/bin/hpvminfo',
                                           rc=0,
                                           out='Running as HPVM host.',
                                           err='')

# Generated at 2022-06-13 04:05:21.096554
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual = HPUXVirtual({})
    assert hpux_virtual.module.run_command.call_count == 0


# Generated at 2022-06-13 04:05:23.496738
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    obj = HPUXVirtual()
    assert obj.platform == 'HP-UX'


# Generated at 2022-06-13 04:05:25.317944
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpuxvirtual = HPUXVirtual(dict(module=None))
    assert hpuxvirtual.platform == 'HP-UX'


# Generated at 2022-06-13 04:05:26.893536
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts = HPUXVirtual({})
    assert virtual_facts.platform == 'HP-UX'


# Generated at 2022-06-13 04:05:34.616971
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    # Set the values of module, vecheck, hpvminfo, parstatus, and parstatus output
    module = type('', (object,), {'run_command': lambda self, cmd: (0, cmd, None)})()
    vecheck = '/usr/sbin/vecheck'
    hpvminfo = '/opt/hpvm/bin/hpvminfo'
    parstatus = '/usr/sbin/parstatus'
    hpvminfo_out = 'Running on HPVM host'
    out = 'running in HP vPar'
    hpvminfo_out2 = 'Running on HPVM guest'
    parstatus_out = 'running in HP nPar'

    # Create the HPUXVirtual object

# Generated at 2022-06-13 04:05:36.122240
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual = HPUXVirtual(dict())
    assert virtual


# Generated at 2022-06-13 04:06:16.393941
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    assert HPUXVirtual(dict()).platform == 'HP-UX'

# Generated at 2022-06-13 04:06:26.498858
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    import os
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtualCollector
    from ansible.module_utils.facts.virtual.hpux import Virtual, VirtualCollector
    base_patcher = mock.patch('ansible.module_utils.facts.virtual.base.Virtual')
    base_patcher.start()
    vc_patcher = mock.patch('ansible.module_utils.facts.virtual.base.VirtualCollector')
    vc_patcher.start()
    os_patcher = mock.patch('ansible.module_utils.facts.virtual.hpux.os')
    mock_os = os_patcher.start()

# Generated at 2022-06-13 04:06:36.950573
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual
    from ansible.module_utils.facts.virtual import VirtualCollector
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtualCollector

    # Expected output
    data = dict(
        virtualization_type='guest',
        virtualization_role='HP nPar'
    )

    # Mock object of the class VirtualCollector
    module = VirtualCollector()

    # Mock object of the class HPUXVirtual
    virtual = HPUXVirtual(module)

    virtual.virtualization_type = ''
    virtual.virtualization_role = ''

    # Mock functions called by get_virtual_facts
    def isfile(path):
        return True

    def run_command(cmd):
        return 0, True, ''

# Generated at 2022-06-13 04:06:42.698425
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    from platform import system
    from ansible.module_utils.facts.virtual.hpu import HPUXVirtual
    from ansible.module_utils.facts.virtual.hpu import HPUXVirtualCollector
    from ansible.module_utils.facts.virtual import VirtualCollector

    if system() == 'HP-UX':
        assert issubclass(HPUXVirtual, VirtualCollector)
        assert HPUXVirtualCollector.__name__ == 'HPUXVirtualCollector'
        assert 'virtualization_type' in HPUXVirtualCollector.virtual_facts_type

# Generated at 2022-06-13 04:06:51.771814
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts import Facts
    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtualHttpApi
    import json

    # Test scenario 1:
    # Test 'HP-UX' virtual_type guest on 'HP vPar'
    # Input facts:
    # - ansible_virtualization_type: 'guest'
    # - ansible_virtualization_role: 'HP vPar'
    # - ansible_system: 'HP-UX'
    # Output facts:
    # - ansible_virtualization_type: 'guest'
    # - ansible_virtualization_role: 'HP vPar'
    # - ansible_virtualization_tech_host: set()
    # -

# Generated at 2022-06-13 04:06:57.167471
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    """
    Unit test for method get_virtual_facts of class HPUXVirtual
    """
    from ansible.module_utils.basic import AnsibleModule

    # Mock module class to pass to the module get_bin_path method
    mock_module = AnsibleModule(
        argument_spec = dict(
            foo = dict(type='str', required=False)
        )
    )

    # Mocking the module.run_command method
    if os.path.exists('/usr/sbin/vecheck'):
        mock_module.run_command.return_value = (0, 'Successful', '')
    else:
        mock_module.run_command.return_value = (1, '', '')

    # Mock class to pass to the HPUXVirtual instance

# Generated at 2022-06-13 04:07:06.132752
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    """
    This is an unit test for method get_virtual_facts of class HPUXVirtual
    """
    # Following are the stubs for method run_command
    (rc1, out1, err1) = (0, '', '')
    (rc2, out2, err2) = (0,
                         'Running on a HPVM IVM', '')
    (rc3, out3, err3) = (0,
                         'Running on a HPVM vPar', '')
    (rc4, out4, err4) = (0,
                         'Running on a HPVM guest', '')
    (rc5, out5, err5) = (0,
                         'Running on a HPVM host', '')

# Generated at 2022-06-13 04:07:12.447119
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts import ModuleStub

    # First test case
    # file /usr/sbin/vecheck does not exists
    # file /opt/hpvm/bin/hpvminfo does not exists
    # file /usr/sbin/parstatus does not exists
    module = ModuleStub(argument_spec={})
    module.run_command = Mock(side_effect=[(1, '', ''), (1, '', ''), (1, '', '')])
    hpux_virtual = HPUXVirtual(module)
    virtual_facts = hpux_virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'unknown'
    assert virtual_facts['virtualization_role'] == ''
    assert virtual_facts['virtualization_tech_host'] == set()

# Generated at 2022-06-13 04:07:17.020248
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    m = HPUXVirtual({'ansible_facts': {}})
    facts = m.get_virtual_facts()
    assert facts['virtualization_type'] == 'guest'
    assert facts['virtualization_role'] == 'HP vPar'
    assert facts['virtualization_tech_guest'] == {'HP vPar'}
    assert facts['virtualization_tech_host'] == set()


# Generated at 2022-06-13 04:07:19.349935
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual
    from ansible.module_utils.facts.virtual.base import VirtualCollector
    hv = HPUXVirtual()
    virtual_facts = hv.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'host'
    assert virtual_facts['virtualization_role'] == 'HPVM'
