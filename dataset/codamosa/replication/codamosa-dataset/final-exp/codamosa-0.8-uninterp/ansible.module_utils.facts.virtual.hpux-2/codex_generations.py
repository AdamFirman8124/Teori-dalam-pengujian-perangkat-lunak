

# Generated at 2022-06-13 03:59:27.916928
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    """
    Unit test for method get_virtual_facts of class HPUXVirtual
    """
    class HPUXVirtual_test(HPUXVirtual):
        module = None
    facts = HPUXVirtual_test()
    assert isinstance(facts.get_virtual_facts(), dict)

# Generated at 2022-06-13 03:59:31.516647
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    """
    The HPUXVirtual class should be instantiable
    """
    h = HPUXVirtual({})
    assert h is not None


# Generated at 2022-06-13 03:59:36.777177
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    import sys
    import subprocess
    if sys.version_info[0] < 3 or (sys.version_info[0] == 3 and sys.version_info[1] < 4):
        from mock import patch
    else:
        from unittest.mock import patch

    hpx_virtual = HPUXVirtual()
    with patch('ansible.module_utils.facts.virtual.hpx.HPUXVirtual.module') as mock:
        mock.run_command.return_value = (0, "hpvm00: Running HPVM vPar (pid=9085)", "")
        virtual_facts = hpx_virtual.get_virtual_facts()

# Generated at 2022-06-13 03:59:41.052724
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts = HPUXVirtual(dict())
    assert virtual_facts.platform == 'HP-UX'

# # Unit test for constructor of class HPUXVirtualCollector
# def test_HPUXVirtualCollector():
#     virtual_facts = HPUXVirtualCollector(dict())
#     assert virtual_facts._fact_class is HPUXVirtual
#     assert virtual_facts._platform is 'HP-UX'
#

# Generated at 2022-06-13 03:59:51.124922
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual import HPUXVirtual
    from collections import namedtuple
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts import get_file_content

    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    # construct a namedtuple with some test values
    class TestModule(object):
        pass

    test_module = TestModule()

    class TestAnsibleModule(object):
        def __init__(self):
            self.params = dict()
            self.run_command_environ_update = dict()


# Generated at 2022-06-13 03:59:57.096057
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual import HPUXVirtual
    from ansible.module_utils import basic
    import json

    fake_module = basic.AnsibleModule(
        argument_spec={},
    )
    fake_module.exit_json = lambda **kwargs: kwargs
    fake_module.run_command = lambda *args, **kwargs: (0, '', '')
    HPUXVirtual.platform = 'test'

    assert not HPUXVirtual(fake_module).get_virtual_facts()['virtualization_type'] == 'host'
    assert not HPUXVirtual(fake_module).get_virtual_facts()['virtualization_type'] == 'guest'


# Generated at 2022-06-13 04:00:03.345204
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    module = AnsibleModule(argument_spec={'gather_subset': dict(required=False, type='list')})
    virtual_instance = HPUXVirtual(module)
    virtual_facts_dict = virtual_instance.get_virtual_facts()

    if not isinstance(virtual_facts_dict, dict):
        module.fail_json(msg='Failed to create HPUXVirtual facts dict')

    module.exit_json(ansible_facts=dict(ansible_virtualization=virtual_facts_dict))


if __name__ == '__main__':
    from ansible.module_utils.basic import AnsibleModule
    test_HPUXVirtual()

# Generated at 2022-06-13 04:00:10.101131
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual
    from ansible.module_utils.facts.virtual.base import Virtual, VirtualCollector
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes, to_text

    module = basic.AnsibleModule(
        argument_spec={},
        supports_check_mode=False,
    )

    hv = HPUXVirtual(module)
    guest_facts = hv.get_virtual_facts()
    assert guest_facts == {
        'virtualization_type': 'guest',
        'virtualization_role': 'HPVM vPar',
        'virtualization_tech_guest': set(['HPVM vPar']),
        'virtualization_tech_host': set(),
    }

# Generated at 2022-06-13 04:00:18.614476
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    guest_virtual_facts = dict(virtualization_type='guest',
                               virtualization_role='HP nPar',
                               virtualization_tech_host=set(),
                               virtualization_tech_guest=set(['HP nPar']))
    HP_parstatus_virtual = HPUXVirtual({'module_setup': True}, dict(virtualization_type='guest',
                                                                    virtualization_role='HP nPar',
                                                                    virtualization_tech_host=set(),
                                                                    virtualization_tech_guest=set(['HP nPar'])), dict())
    HP_parstatus_virtual.get_virtual_facts() == guest_virtual_facts
    HP_vecheck_virtual = HPUXVirtual({'module_setup': True}, dict(), dict())
    HP_vecheck_virtual.get

# Generated at 2022-06-13 04:00:21.710310
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    module = AnsibleModuleMock()

    virtual = HPUXVirtual(module)
    assert virtual._platform == 'HP-UX'
    assert virtual._fact_class == HPUXVirtual


# Generated at 2022-06-13 04:00:34.119698
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpuxv = HPUXVirtual(dict(), dict())

    assert hpuxv.platform == 'HP-UX'
    assert hpuxv.module == dict()
    assert hpuxv.fact_class == dict()



# Generated at 2022-06-13 04:00:41.163184
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    """
    Unit test for method get_virtual_facts of class HPUXVirtual
    """
    import collections
    import ansible.module_utils.facts.virtual

    # Create a mock module
    mock_module = collections.namedtuple('MockModule', ['run_command'])

    # Create a mock command with return code and output
    mock_command = collections.namedtuple('MockCommand', ['returncode', 'stdout'])

    # Define return value for method run_command of object mock_module
    mock_module.run_command.side_effect = [
        mock_command(0, "")
    ]

    virtual = ansible.module_utils.facts.virtual.HPUXVirtual()
    virtual.module = mock_module
    virtual_facts_dict = virtual.get_virtual_facts()
    expected_

# Generated at 2022-06-13 04:00:45.696802
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    # TODO
    module = object()
    class Facts():
        def __init__(self):
            self.system = 'HP-UX'
    module.params = {
        'gather_subset': '!all,min',
    }
    module.exit_json = lambda **kwargs: kwargs
    module.run_command = lambda command: (0, "", "")
    module.run_command.side_effect = {
        "/usr/sbin/vecheck": (1, "", ""),
        "/opt/hpvm/bin/hpvminfo": (1, "", ""),
        "/usr/sbin/parstatus": (1, "", ""),
    }.get(command, (0, "", ""))
    module.ansible_facts = {}
    virtual_facts = HPUX

# Generated at 2022-06-13 04:00:51.497067
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():

    def module_run_command_side_effect(*args, **kwargs):
        rc = 0
        out = ""
        err = ""
        if args[0] == "/usr/sbin/vecheck":
            rc = 0
            out = 'abc'
        elif args[0] == "/opt/hpvm/bin/hpvminfo":
            rc = 0
            out = 'Running on HPVM vPar'
        elif args[0] == "/usr/sbin/parstatus":
            rc = 0
            out = 'abc'
        return rc, out, err

    def os_path_exists_side_effect(*args, **kwargs):
        path = args[0]
        if path == '/usr/sbin/vecheck':
            return True

# Generated at 2022-06-13 04:01:01.525277
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils import basic
    import ansible.module_utils.facts.virtual.hpux
    from ansible.module_utils.facts.virtual import hpux

    HPUXVirtual.module = basic.AnsibleModule(
        argument_spec=dict()
    )
    HPUXVirtual.module.run_command = hpux.run_command

    facts = HPUXVirtual(HPUXVirtual.module).get_virtual_facts()
    assert facts['virtualization_type'] == 'guest'
    assert facts['virtualization_role'] == 'HPVM vPar'
    assert facts['virtualization_tech_guest'] == set(['HPVM vPar'])
    assert facts['virtualization_tech_host'] == set()

# Generated at 2022-06-13 04:01:02.818249
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual({})
    assert hv.platform == "HP-UX"

# Generated at 2022-06-13 04:01:04.856055
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    v = HPUXVirtual()
    assert v.platform == 'HP-UX'
    assert v.get_virtual_facts() == {}

# Generated at 2022-06-13 04:01:13.158437
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    # For Errors
    # fmt: off
    hpmodule = HPUXVirtual({
        'module_name': 'ansible.module_utils.facts.virtual',
        'module_args': ''
    })
    # fmt: on
    assert hpmodule.get_virtual_facts() == {
        'virtualization_type': 'guest',
        'virtualization_role': 'HP nPar',
        'virtualization_tech_guest': set(['HP nPar']),
        'virtualization_tech_host': set()
    }

# Generated at 2022-06-13 04:01:17.814730
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module = AnsibleModule(argument_spec={})
    virtual_facts = HPUXVirtual(module).get_virtual_facts()
    module.exit_json(changed=False, ansible_facts={"ansible_virtual_facts": virtual_facts})



# Generated at 2022-06-13 04:01:20.595628
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual = HPUXVirtual(dict())
    assert isinstance(virtual, HPUXVirtual)
    assert virtual.platform == 'HP-UX'
    assert virtual.virtualization_type == "host"
    assert virtual.virtualization_role == "HPVM"

# Generated at 2022-06-13 04:01:43.048929
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module = AnsibleModule(argument_spec = {})
    command = module.get_bin_path('vecheck', opt_dirs=['/usr/sbin'])
    if command is not None:
        vecheck_data = 'foo'
        module.run_command.return_value = (0, vecheck_data, None)
        virtual = HPUXVirtual(module)
        virtual_facts = virtual.get_virtual_facts()
        assert virtual_facts['virtualization_type'] == 'guest'
        assert virtual_facts['virtualization_role'] == 'HP vPar'
        assert virtual_facts['virtualization_tech_guest'] == set(['HP vPar'])
        assert virtual_facts['virtualization_tech_host'] == set()


# Generated at 2022-06-13 04:01:48.283353
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    facts = dict()
    hypervisor = HPUXVirtual(facts)
    vf = hypervisor.get_virtual_facts()
    assert 'virtualization_type' in vf
    assert 'virtualization_role' in vf
    assert 'virtualization_tech_guest' in vf
    assert 'virtualization_tech_host' in vf

# Generated at 2022-06-13 04:01:52.161262
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    test_module = 'ansible.module_utils.facts.virtual.hpux.HPUXVirtual'
    m = __import__(test_module, globals(), locals(), ['object'], 0)
    vm = m.HPUXVirtual()
    assert vm.platform == 'HP-UX'

# Generated at 2022-06-13 04:01:58.723556
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    ''' Unit test for method get_virtual_facts of class HPUXVirtual '''

    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtualCollector
    from ansible.module_utils._text import to_bytes

    from ansible.module_utils import basic
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtualCollector

    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual

    # Check that the method get_virtual_facts returns expected dict when running
    # on HP-UX vPar

# Generated at 2022-06-13 04:02:05.678228
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    """
    This will test the constructor of class HPUXVirtual and
    all methods of class Virtual.
    """
    module = AnsibleModule(
        argument_spec = dict(),
    )
    hpux_virtual = HPUXVirtualCollector.fetch_virtual_facts(module)
    if hpux_virtual:
        facts_result = hpux_virtual.get_facts()
        assert 'virtualization_type' in facts_result
        assert 'virtualization_role' in facts_result
        assert 'virtualization_tech' in facts_result
        assert 'virtualization_tech_details' in facts_result
        assert 'virtualization_tech_guest' in facts_result
        assert 'virtualization_tech_host' in facts_result
        assert 'virtualization_interfaces' in facts_result

# Generated at 2022-06-13 04:02:15.250133
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.HPUX import HPUXVirtual
    from ansible.module_utils.facts.virtual.posix.facter import VirtualFacterModule
    module = VirtualFacterModule()
    hparfact = HPUXVirtual(module)
    fact_data = hparfact.get_virtual_facts()
    assert fact_data.get('virtualization_type') == 'guest'
    assert fact_data.get('virtualization_role') == 'HP vPar'
    assert fact_data.get('virtualization_tech_host') == {'HPVM'}
    assert fact_data.get('virtualization_tech_guest') == {'HP vPar', 'HP nPar'}

# Generated at 2022-06-13 04:02:17.023124
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpuxVirtual = HPUXVirtual()
    assert hpuxVirtual != None
    hpuxVirtual = HPUXVirtual({"module": {"run_command": "run_command"}})
    assert hpuxVirtual != None

# Generated at 2022-06-13 04:02:18.138077
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual = HPUXVirtual(dict(), dict())
    assert virtual.platform == 'HP-UX'


# Generated at 2022-06-13 04:02:22.244882
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    """
    Unit tests for method get_virtual_facts of class HPUXVirtual
    """
    # pylint: disable=W0212
    data_files = {
        '/usr/sbin/vecheck': b'',
        '/usr/sbin/parstatus': b'These are not the parstatuses you are looking for.',
        '/opt/hpvm/bin/hpvminfo': b'Running an HPVM vPar, foo bar.\n'
                                  b'Running an HPVM guest, foo bar.\n'
                                  b'Running an HPVM host, foo bar.\n'
    }

    virtual_facts = HPUXVirtual(dict(), data_files).get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'guest'

# Generated at 2022-06-13 04:02:24.660846
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual = HPUXVirtual(None)
    assert virtual.platform == 'HP-UX'


# Generated at 2022-06-13 04:02:50.327209
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual import HPUXVirtual
    v = HPUXVirtual(None)

    vecheck = "vecheck: VM is enabled\n"
    hpvminfo = "Running as a HPVM vPar\n"
    parstatus = "Virtual Partition Active\n"

    d = {
        '/usr/sbin/vecheck': (0, vecheck, ''),
        '/opt/hpvm/bin/hpvminfo': (0, hpvminfo, ''),
        '/usr/sbin/parstatus': (0, parstatus, ''),
    }

    test_facts = v.get_virtual_facts()

    # Resetting modules to original state
    v.module.run_command = v.run_command
    v.module.get_bin_path = v.get_

# Generated at 2022-06-13 04:02:56.468135
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module = AnsibleModule(
        argument_spec = dict()
    )
    os.path.exists = lambda x : False
    module.run_command = lambda x : (0, 'Running HPVM guest', '')
    facts = HPUXVirtual({}).get_virtual_facts()
    assert facts['virtualization_type'] == 'guest'
    assert facts['virtualization_role'] == 'HPVM'
    assert 'HPVM' in facts['virtualization_tech_guest']
    assert 'HPVM' in facts['virtualization_tech_host']
    os.path.exists = lambda x : False
    module.run_command = lambda x : (0, 'Running HPVM vPar', '')
    facts = HPUXVirtual({}).get_virtual_facts()

# Generated at 2022-06-13 04:02:59.759796
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    # Create HPUXVirtual with default values.
    hpux_virtual = HPUXVirtual()

    # Create HPUXVirtual with specific values.
    hpux_virtual = HPUXVirtual(module=True)
    assert hpux_virtual
    assert hpux_virtual.platform == 'HP-UX'



# Generated at 2022-06-13 04:03:06.783447
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hplx_virtual_fact = HPUXVirtual({})
    assert hplx_virtual_fact.platform == 'HP-UX'
    assert type(hplx_virtual_fact.virtualization_type) is str
    assert type(hplx_virtual_fact.virtualization_role) is str
    assert type(hplx_virtual_fact.virtualization_tech_guest) is set
    assert type(hplx_virtual_fact.virtualization_tech_host) is set
    assert type(hplx_virtual_fact._name) is str

# Generated at 2022-06-13 04:03:07.995303
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
  HPUXVirtual().get_virtual_facts()

# Generated at 2022-06-13 04:03:11.388997
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    """
    Test HPUXVirtual Constructor
    """
    virtual = HPUXVirtual({})
    assert virtual.platform == 'HP-UX'
    assert virtual.virtualization_type == ''
    assert virtual.virtualization_role == ''

# Generated at 2022-06-13 04:03:13.143261
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():

    virt = HPUXVirtual()
    assert virt.platform == 'HP-UX'
    assert virt.name == 'hpu_virtual'


# Generated at 2022-06-13 04:03:17.131220
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    '''Unit test for constructor of class HPUXVirtual'''
    '''test_HPUXVirtual is a constructor of class HPUXVirtual'''
    hpux_virtual = HPUXVirtual(None)
    assert hpux_virtual.__class__.__name__ == 'HPUXVirtual', 'test_HPUXVirtual() failed!'


# Generated at 2022-06-13 04:03:19.167496
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    module = AnsibleModule
    virtual = HPUXVirtual(module)
    assert virtual.platform == 'HP-UX'

# Generated at 2022-06-13 04:03:29.230716
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils import basic

    module = basic.AnsibleModule(
        argument_spec=dict()
    )
    from ansible.module_utils._text import to_bytes

    virtual = HPUXVirtual(module)
    virtual_facts = virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'host'
    assert virtual_facts['virtualization_role'] == 'HPVM'
    assert 'HPVM vPar' in virtual_facts['virtualization_tech_guest']
    assert 'HPVM IVM' in virtual_facts['virtualization_tech_guest']
    assert 'HP vPar' in virtual_facts['virtualization_tech_guest']
    assert 'HP nPar' in virtual_facts['virtualization_tech_guest']

# Generated at 2022-06-13 04:04:01.137002
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    # Test with basic facts without any virtualization
    # Expected result: virtualization_type = None, virtualization_role = None,
    #                  virtualization_tech_guest = set(), virtualization_tech_host = set()
    facts = dict()
    facts['distribution'] = 'HP-UX'
    facts['system'] = 'HP-UX'
    virtual_facts = HPUXVirtual(facts).get_virtual_facts()
    assert virtual_facts['virtualization_type'] is None
    assert virtual_facts['virtualization_role'] is None
    assert virtual_facts['virtualization_tech_guest'] == set()
    assert virtual_facts['virtualization_tech_host'] == set()

    # Test with vPar facts
    # Expected result: virtualization_type = guest, virtualization_role = HP vPar,


# Generated at 2022-06-13 04:04:07.845825
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    """
    This testcase collects virtual facts on a HP-UX system.
    This test is intended to aid development, and is not meant to be
    production quality.
    """
    import ansible.module_utils.facts.virtual.hpux_virtual as hpux_virtual

    hpux_virtual.HPUXVirtual.__init__(hpux_virtual)
    virtual_facts = hpux_virtual.HPUXVirtual.get_virtual_facts(hpux_virtual)
    assert isinstance(virtual_facts, dict)
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert isinstance(virtual_facts['virtualization_tech_guest'], set)
    assert isinstance(virtual_facts['virtualization_tech_host'], set)


# Generated at 2022-06-13 04:04:09.219083
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    x = HPUXVirtual({})
    assert x.platform == 'HP-UX'

# Generated at 2022-06-13 04:04:13.136234
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual()
    assert hv._platform == 'HP-UX'
    assert hv.get_virtual_facts() == {
        'virtualization_type': 'host',
        'virtualization_role': None,
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set(['HPVM', 'HP nPar', 'HP vPar', 'HPVM vPar', 'HPVM IVM'])
    }
    assert hv.get_virtual_facts()['virtualization_type'] == 'host'


# Generated at 2022-06-13 04:04:16.498201
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module = {
    }
    virtualization_facts = HPUXVirtual(module).get_virtual_facts()
    assert len(virtualization_facts) == 5
    assert virtualization_facts['virtualization_type'] == 'guest'
    assert virtualization_facts['virtualization_role'] == 'HP nPar'
    assert len(virtualization_facts['virtualization_tech_host']) == 0
    assert len(virtualization_facts['virtualization_tech_guest']) == 3

# Generated at 2022-06-13 04:04:18.874376
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():

    facts = dict()
    facts['virtual'] = HPUXVirtual(None).get_virtual_facts()
    print(facts['virtual'])


# Generated at 2022-06-13 04:04:25.195661
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    mock_module = type('MockModule', (object,), {'run_command': HPUXVirtual._exec_cmd})
    mock_module_instance = mock_module()
    HPUXVirtual._module = mock_module_instance

    # Test for guest
    HPUXVirtual._exec_cmd = lambda self, *args, **kwargs: (0, 'Mock output', 'Mock stderr')
    assert HPUXVirtual(mock_module_instance).get_virtual_facts() == {
        'virtualization_type': 'guest',
        'virtualization_role': 'HP vPar',
        'virtualization_tech_guest': set(['HP vPar']),
        'virtualization_tech_host': set([]),
    }

    # Test for host

# Generated at 2022-06-13 04:04:27.763067
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts = HPUXVirtual(dict(), dict())
    assert virtual_facts.gather() == None

# Generated at 2022-06-13 04:04:33.990243
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    # Test with HP nPar
    module = get_module_mock(dict(rc=0,
                                  out="""
HPVM Host machine is running
HPVM Host machine is running
""",
                                  err=''))
    virtual_facts = HPUXVirtual(module)
    virtual_facts_dict = virtual_facts.get_virtual_facts()
    assert virtual_facts_dict['virtualization_type'] == 'guest'
    assert virtual_facts_dict['virtualization_role'] == 'HP nPar'
    assert 'HPVM IVM' not in virtual_facts_dict['virtualization_tech_host']
    assert 'HPVM IVM' not in virtual_facts_dict['virtualization_tech_guest']
    assert 'HPVM vPar' not in virtual_facts_dict['virtualization_tech_host']
   

# Generated at 2022-06-13 04:04:42.738637
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtualCollector
    from ansible.module_utils.facts.virtual.hpux import get_virtual_facts
    from ansible.module_utils.facts.virtual.hpux import VirtualCollector

    # Get the module source path
    source_path = os.path.dirname(os.path.realpath(__file__))
    # Get the module source data dir path
    test_data_dir_path = os.path.join(source_path, 'test_data', 'get_virtual_facts')

    # HPUXVirtual
    obj_hpux_virtual = HPUXVirtual()

# Generated at 2022-06-13 04:05:33.665206
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module = AnsibleModule({})
    virtual = HPUXVirtual(module)

    virt_facts = virtual.get_virtual_facts()

    assert virt_facts['virtualization_type'] == 'guest'
    assert virt_facts['virtualization_role'] == 'HP vPar'
    assert virt_facts['virtualization_tech_guest'] == set(['HP vPar'])
    assert virt_facts['virtualization_tech_host'] == set([])


if __name__ == '__main__':
    from ansible.module_utils.basic import *
    import sys
    if sys.argv[1] == 'test_HPUXVirtual_get_virtual_facts':
        test_HPUXVirtual_get_virtual_facts()

# Generated at 2022-06-13 04:05:40.434996
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtualCollector
    virtual_collector = HPUXVirtualCollector()
    virtual_instance = virtual_collector.fetch_virtual_facts('guest')
    print(virtual_instance.get_virtual_facts())
    virtual_instance = virtual_collector.fetch_virtual_facts('host')
    print(virtual_instance.get_virtual_facts())

# Generated at 2022-06-13 04:05:42.248323
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    HPUXVirt = HPUXVirtual('module')
    assert HPUXVirt.platform == 'HP-UX'



# Generated at 2022-06-13 04:05:44.528333
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual()
    assert hv.platform == 'HP-UX', 'test_HPUXVirtual assert#1 has failed'

# Generated at 2022-06-13 04:05:45.977490
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_class = HPUXVirtual(dict())
    assert virtual_class.platform == 'HP-UX'


# Generated at 2022-06-13 04:05:51.947522
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    """HPUXVirtual - get_virtual_facts(module) return facts
    """
    class ModuleStub:
        def run_command(self, cmd):
            if cmd == "/usr/sbin/vecheck":
                return 0, "", ""
            elif cmd == "/opt/hpvm/bin/hpvminfo":
                return 0, "Running: HPVM vPar", ""
            elif cmd == "/usr/sbin/parstatus":
                return 0, "", ""
            else:
                return 0, "", ""
            
    h = HPUXVirtual(ModuleStub())
    facts = h.get_virtual_facts()
    assert facts['virtualization_type'] == 'guest'
    assert facts['virtualization_role'] == 'HPVM vPar'

# Generated at 2022-06-13 04:05:53.521409
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_collector = HPUXVirtualCollector()
    virtual_obj = HPUXVirtual(module=None)
    assert virtual_obj._platform == 'HP-UX'

# Generated at 2022-06-13 04:05:57.657800
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module = AnsibleModule(
        argument_spec={
        },
        supports_check_mode=True
    )

    h = HPUXVirtual(module)

    facts = h.get_virtual_facts()

    assert facts['virtualization_tech_guest'] == set()
    assert facts['virtualization_role'] == None
    assert facts['virtualization_type'] == None

# Generated at 2022-06-13 04:06:00.340022
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hvf = HPUXVirtual({})
    assert hvf.platform == 'HP-UX'


# Generated at 2022-06-13 04:06:11.455136
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    import os
    # Create an instance of HPUXVirtual

# Generated at 2022-06-13 04:07:08.538425
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    v = HPUXVirtual({})
    assert v.platform == "HP-UX"
    assert v.get_virtual_facts() == {'virtualization_type': 'guest', 'virtualization_role': 'HP nPar', 'virtualization_tech_guest': set(['HP nPar']), 'virtualization_tech_host': set()}

# Generated at 2022-06-13 04:07:10.952435
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True)
    hpx = HPUXVirtual(module)
    assert hpx.platform == 'HP-UX'
    assert hpx._platform == 'HP-UX'

# Generated at 2022-06-13 04:07:16.616399
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    class TestModule(object):
        def __init__(self):
            self.exit_json = lambda x: None

        def run_command(self, cmd):
            return  0, '', ''

    module = TestModule()
    virtual = HPUXVirtual(module)
    virtual_facts = virtual.get_virtual_facts()

    guest_tech = virtual_facts['virtualization_tech_guest']
    host_tech = virtual_facts['virtualization_tech_host']
    assert set(['HP nPar', 'HP vPar', 'HPVM']) == guest_tech
    assert set() == host_tech
    assert virtual_facts['virtualization_type'] == 'guest'
    assert virtual_facts['virtualization_role'] == 'HP nPar'


# Generated at 2022-06-13 04:07:21.294819
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    _module = AnsibleModuleMock({'name': 'hpux', 'module_utils.basic.AnsibleModule.run_command.return_value': (0, 'output', 'error')})
    _get_virtual_facts = HPUXVirtual(_module).get_virtual_facts()
    assert _get_virtual_facts['virtualization_type'] == 'guest'

# Generated at 2022-06-13 04:07:22.543257
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual(dict(module=dict()))
    assert hv.platform == 'HP-UX'

# Generated at 2022-06-13 04:07:24.922308
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    """
    Unit test to check the constructor of class HPUXVirtual
    """
    unit_test = HPUXVirtual()
    assert unit_test
    assert unit_test.platform == 'HP-UX'


# Generated at 2022-06-13 04:07:29.457700
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    module = AnsibleModule(argument_spec={})
    virt = HPUXVirtual(module)
    assert virt.platform == 'HP-UX'


# Generated at 2022-06-13 04:07:31.146316
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual_obj = HPUXVirtual()
    assert hpux_virtual_obj.platform == 'HP-UX'


# Generated at 2022-06-13 04:07:36.693696
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    f = HPUXVirtual({})
    res = f.get_virtual_facts()
    assert 'virtualization_type' in res
    assert 'virtualization_role' in res
    assert 'virtualization_tech_host' in res
    assert 'virtualization_tech_guest' in res
    assert isinstance(res['virtualization_tech_host'], set)
    assert isinstance(res['virtualization_tech_guest'], set)

# Generated at 2022-06-13 04:07:37.866066
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    """
    Create an instance of HPUXVirtual
    """
    hpux = HPUXVirtual(dict(), dict())
    assert hpux.platform == 'HP-UX'