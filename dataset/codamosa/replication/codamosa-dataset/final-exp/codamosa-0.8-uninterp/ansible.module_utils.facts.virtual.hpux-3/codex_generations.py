

# Generated at 2022-06-13 03:59:37.445671
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    """
    Unit test for get_virtual_facts of class
    HPUXVirtual.
    """

    class ModuleMock():
        def __init__(self):
            self.run_command_results = []

        def run_command(self, command):
            return self.run_command_results.pop(0)

    class FactsMock():
        def __init__(self):
            self.module = ModuleMock()

    class VirtualMock(HPUXVirtual):
        def __init__(self):
            self.facts = FactsMock()
            self.module = ModuleMock()

    vecheck_output_vpar_guest = """
The HP-UX operating system is not a virtual partition.
"""


# Generated at 2022-06-13 03:59:39.269929
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_obj = HPUXVirtual(dict())
    assert virtual_obj.__class__.__name__ == 'HPUXVirtual'



# Generated at 2022-06-13 03:59:43.170064
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hypervisor = HPUXVirtual(dict(module=None))
    assert hypervisor.get_virtual_facts()['virtualization_tech_guest'] == set()



# Generated at 2022-06-13 03:59:44.613351
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    h = HPUXVirtual({})
    assert h.platform == 'HP-UX'

# Generated at 2022-06-13 03:59:50.921788
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpuxvirtual = HPUXVirtual()
    assert hpuxvirtual.platform == 'HP-UX'
    assert hpuxvirtual.get_virtual_facts()['virtualization_type'] == 'guest'
    assert hpuxvirtual.get_virtual_facts()['virtualization_role'] == 'HP vPar'
    assert hpuxvirtual.get_virtual_facts()['virtualization_tech_guest'] == set(['HP vPar'])
    assert hpuxvirtual.get_virtual_facts()['virtualization_tech_host'] == set([])


# Generated at 2022-06-13 03:59:57.500456
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    class MockModule:
        def run_command(self, args, check_rc=True):
            return (0, '', '')
    module = MockModule()
    facter_virtual = HPUXVirtual(module)

    # vecheck returns rc=0
    assert facter_virtual.get_virtual_facts() == {
        'virtualization_type': 'guest',
        'virtualization_role': 'HP vPar',
        'virtualization_tech_guest': {'HP vPar'},
        'virtualization_tech_host': set()
    }
    # hpvminfo returns rc=0

# Generated at 2022-06-13 04:00:07.273753
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    file_dict = {
        "/usr/sbin/vecheck": (0, "", ""),
        "/opt/hpvm/bin/hpvminfo": (0, "Running in HPVM vPar.\n", ""),
        "/opt/hpvm/bin/hpvminfo": (0, "Running in HPVM guest.\n", ""),
        "/opt/hpvm/bin/hpvminfo": (0, "Running in HPVM host.\n", ""),
        "/usr/sbin/parstatus": (0, "", "")
    }
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    vm = HPUXVirtual(module)
    vm.get_file_lines = lambda x: file_dict[x]
    vm.run

# Generated at 2022-06-13 04:00:14.670104
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():

    module = AnsibleModule(
        argument_spec=dict()
    )

    virtual_facts = dict(
        virtualization_type='guest',
        virtualization_role='HP vPar'
    )

    class TestHPUXVirtual(HPUXVirtual):
        def __init__(self):
            self.module = module

    virtual = TestHPUXVirtual()

    assert virtual.get_virtual_facts() == virtual_facts


# Generated at 2022-06-13 04:00:17.403368
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hx = HPUXVirtual()
    assert hx.platform == 'HP-UX'


# Generated at 2022-06-13 04:00:20.310198
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    v = HPUXVirtual()
    assert(v)
    assert(v.virtualization_type == 'HP-UX')
    assert(v.virtualization_role == 'HP-UX')
    assert(v.virtualization_role == 'HP-UX')

# Generated at 2022-06-13 04:00:31.245903
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    class MockModule(object):
        def run_command(self, command):
            return 0, '', ''
    module = MockModule()
    hpuxvirtual = HPUXVirtual(module)
    assert hpuxvirtual.get_virtual_facts() == {}

# Generated at 2022-06-13 04:00:33.021481
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    c = HPUXVirtualCollector()
    assert c._fact_class is HPUXVirtual
    assert c._platform == 'HP-UX'

# Generated at 2022-06-13 04:00:34.927713
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual = HPUXVirtual()
    assert hpux_virtual.platform == 'HP-UX'
    assert hpux_virtual.get_virtual_facts() == {}


# Generated at 2022-06-13 04:00:37.128820
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hp_virtual = HPUXVirtual(dict())
    assert hp_virtual.platform == 'HP-UX'
    assert hp_virtual.get_virtual_facts()['virtualization_type'] == 'guest'
    assert hp_virtual.get_virtual_facts()['virtualization_role'] == 'HP nPar'

# Generated at 2022-06-13 04:00:40.202113
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virt = HPUXVirtual()
    assert virt.platform == 'HP-UX'
    assert virt.module == None
    assert virt.virtualization_type == None
    assert virt.virtualization_role == None


# Generated at 2022-06-13 04:00:41.389538
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    module = AnsibleModule(dict(), False)
    virtual = HPUXVirtual(module)
    assert isinstance(virtual, Virtual)

# Generated at 2022-06-13 04:00:42.837371
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual = HPUXVirtual(dict())
    assert virtual.platform == 'HP-UX'

# Generated at 2022-06-13 04:00:44.455787
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    x = HPUXVirtual(dict())
    assert x.platform == 'HP-UX'



# Generated at 2022-06-13 04:00:46.505522
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():

    obj = HPUXVirtual()
    assert obj.platform == 'HP-UX'



# Generated at 2022-06-13 04:00:48.418997
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    """
    Test the constructor of class HPUXVirtual
    """
    virtual_facts = HPUXVirtual()
    assert virtual_facts.platform == 'HP-UX'

# Generated at 2022-06-13 04:01:05.571371
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual

    module = basic.AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    # Hold all of the command outputs.
    command_outputs = {
        '/usr/sbin/vecheck': '',
        '/opt/hpvm/bin/hpvminfo': '',
        '/usr/sbin/parstatus': '',
    }

    # This is the returned facts.

# Generated at 2022-06-13 04:01:12.931125
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual import HPUXVirtual
    from ansible.module_utils.facts.module_utils import AnsibleModuleMock
    class Mock_module():
        def __init__(self):
            pass
    module = Mock_module()
    module.run_command = AnsibleModuleMock().run_command
    module.get_bin_path = AnsibleModuleMock().get_bin_path
    virtual = HPUXVirtual(module)
    virtual.get_virtual_facts()

# Generated at 2022-06-13 04:01:19.712441
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual
    from ansible.module_utils.facts import ModuleFiles
    module_files = ModuleFiles()
    facts = {}
    hpux_virtual = HPUXVirtual(module_files, facts)
    virtual_facts = hpux_virtual.get_virtual_facts()

    assert 'guest' in virtual_facts['virtualization_type']
    assert 'HP vPar' in virtual_facts['virtualization_role']

# Generated at 2022-06-13 04:01:21.242837
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual = HPUXVirtual()
    assert hpux_virtual.platform == 'HP-UX'

# Generated at 2022-06-13 04:01:28.961977
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module = AnsibleModule(argument_spec={'gather_subset': dict(default=[], type='list'), 'gather_timeout': dict(default=10, type='int')})
    v = HPUXVirtual(module)
    facts = v.get_virtual_facts()
    assert facts['virtualization_type'] == 'guest'
    assert facts['virtualization_role'] == 'HP vPar'
    assert facts['virtualization_tech_host'] == set()
    assert facts['virtualization_tech_guest'] == {'HP vPar'}

# Generated at 2022-06-13 04:01:39.979876
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():

    facts = HPUXVirtualCollector(None, 'HP-UX').collect()

    assert len(facts.keys()) > 0
    assert isinstance(facts['virtualization_type'], str) or facts['virtualization_type'] is None
    if facts['virtualization_type']:
        assert facts['virtualization_type'] in ('guest', 'host')
    # virtualization role is not always discovered on all platforms
    if facts['virtualization_role']:
        assert isinstance(facts['virtualization_role'], str)
    # virtualization technology is not always discovered on all platforms
    if facts['virtualization_type'] == 'guest':
        assert isinstance(facts['virtualization_tech_guest'], set)

# Generated at 2022-06-13 04:01:46.531067
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpar import HPUXVirtual
    from ansible.module_utils.facts.virtual.hpvm import HPUXVirtual
    from ansible.module_utils.facts.virtual.npar import HPUXVirtual
    facts = {}

# Generated at 2022-06-13 04:01:48.905513
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    v = HPUXVirtual()
    assert v.platform == 'HP-UX'

# Generated at 2022-06-13 04:01:56.931747
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    import mock
    import tempfile

    module = mock.MagicMock()
    module.run_command = mock.MagicMock()
    module.run_command.return_value = (0, '', '')
    module.params = {'gather_subset': ['!all', '!min']}

    tmp_file_handle, tmp_file_name = tempfile.mkstemp(text=True, prefix='out_')
    open(tmp_file_name, 'w').write('Running as HPVM guest.\n')
    HPUXVirtualCollector({'path_to_data': tmp_file_name}).get_virtual_facts()
    ret = module.run_command.call_count
    os.close(tmp_file_handle)
    os.unlink(tmp_file_name)

    # check

# Generated at 2022-06-13 04:02:01.455481
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    collect_mock = HPUXVirtualCollector()
    virtual_facts = collect_mock.get_virtual_facts()
    assert len(virtual_facts) == 4
    assert virtual_facts['virtualization_tech_guest'] == set()
    assert virtual_facts['virtualization_tech_host'] == set()
    assert virtual_facts['virtualization_role'] is None
    assert virtual_facts['virtualization_type'] is None

# Generated at 2022-06-13 04:02:13.127391
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual = HPUXVirtual()
    assert hpux_virtual.platform == 'HP-UX'


# Generated at 2022-06-13 04:02:17.882969
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible_collections.misc.not_a_real_collection.plugins.module_utils.facts.virtual.hpux import HPUXVirtual
    from ansible_collections.misc.not_a_real_collection.plugins.module_utils.facts.virtual.hpux import (
        HPUXVirtualCollector)
    from ansible_collections.misc.not_a_real_collection.plugins.module_utils.facts import ModuleFacts

    class MockModule:
        def __init__(self):
            pass

        def run_command(self, cmd):
            # Run command: /usr/sbin/vecheck
            if cmd == '/usr/sbin/vecheck':
                return 0, '', ''
            # Run command: /opt/hpvm/bin/hpvminfo

# Generated at 2022-06-13 04:02:20.035561
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual = HPUXVirtual()

    assert hpux_virtual.platform == 'HP-UX'
    assert hpux_virtual.product_name == 'HP-UX'
    assert type(hpux_virtual.get_virtual_facts()) is dict


# Generated at 2022-06-13 04:02:27.593465
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    """
    Unit test of method get_virtual_facts of class HPUXVirtual
    """
    hpu_virtual = HPUXVirtual()

    # Invoke method get_virtual_facts
    hpu_virtual_facts = hpu_virtual.get_virtual_facts()

    # Check attributes
    assert isinstance(hpu_virtual_facts, dict), "The method get_virtual_facts returns a dict"
    assert 'virtualization_type' in hpu_virtual_facts, "The returned dict contains the attribute virtualization_type"
    assert 'virtualization_role' in hpu_virtual_facts, "The returned dict contains the attribute virtualization_role"

# Generated at 2022-06-13 04:02:33.682642
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    A = HPUXVirtual(dict(ansible_facts={}), dict())
    A.module.run_command = lambda x: (1, '', '')
    ansible_facts = dict()
    virtual_facts = A.get_virtual_facts()
    ansible_facts.update(virtual_facts)
    assert ansible_facts == dict(virtualization_type=None)

    B = HPUXVirtual(dict(ansible_facts={}), dict())
    B.module.run_command = lambda x: (0, '', '')
    ansible_facts = dict()
    virtual_facts = B.get_virtual_facts()
    ansible_facts.update(virtual_facts)
    assert ansible_facts == dict(virtualization_role='HP vPar',
                                 virtualization_type='guest')

# Generated at 2022-06-13 04:02:39.720738
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpux.HPUXVirtual import HPUXVirtual

    hv_facts = HPUXVirtual({})
    hv_facts_dict = hv_facts.get_virtual_facts()
    assert isinstance(hv_facts_dict, dict)
    assert 'HPVM' in hv_facts_dict['virtualization_tech_guest']
    assert 'HPVM' in hv_facts_dict['virtualization_tech_host']
    assert hv_facts_dict['virtualization_type'] == 'host'
    assert hv_facts_dict['virtualization_role'] == 'HPVM'

# Generated at 2022-06-13 04:02:43.006251
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    virtual_facts = dict(HPUXVirtual(None).get_virtual_facts())
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts

# Generated at 2022-06-13 04:02:46.508408
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    from ansible.module_utils.facts import virtual
    new_hpux_virtual = virtual.HPUXVirtual({})
    assert new_hpux_virtual.platform == 'HP-UX'

# Generated at 2022-06-13 04:02:48.395908
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual = HPUXVirtual({})
    assert virtual._platform == 'HP-UX'


# Generated at 2022-06-13 04:02:53.231298
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    hvFact = HPUXVirtual()
    virtual_facts = hvFact.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'guest'
    assert virtual_facts['virtualization_role'] == 'HPVM'
    assert 'HPVM vPar' in virtual_facts['virtualization_tech_guest']
    assert virtual_facts['virtualization_tech_host'] == set()


# Generated at 2022-06-13 04:03:14.854824
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=False
    )
    if not hasattr(module, 'run_command'):
        module.run_command = run_command
    collect_subset = ['!all', 'virtual']
    instance = HPUXVirtualCollector(module=module)
    virtual_facts = instance.get_virtual_facts(collect_subset=collect_subset)
    assert isinstance(virtual_facts, dict)
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts

# Generated at 2022-06-13 04:03:16.293854
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual()
    assert hv.virt_type == 'HP-UX'


# Generated at 2022-06-13 04:03:26.195421
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    obj = HPUXVirtual(dict(module=256))
    obj.module.run_command = Mock(
        return_value=(0, 'Running HPVM vPar\n', ''))
    facts = obj.get_virtual_facts()
    assert facts['virtualization_type'] == 'guest'
    assert facts['virtualization_role'] == 'HPVM vPar'
    assert facts['virtualization_tech_guest'] == set(['HPVM vPar'])
    assert facts['virtualization_tech_host'] == set()

    obj.module.run_command = Mock(return_value=(0, '', 'Error'))
    facts = obj.get_virtual_facts()
    assert facts['virtualization_type'] == ''



# Generated at 2022-06-13 04:03:33.381214
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils.facts.virtual import HPUXVirtual
    from ansible.module_utils.facts.virtual.base import VirtualCollector

    # Create test collecter
    hv = HPUXVirtual(None)
    assert hv._platform == 'HP-UX'

    # Create test facts
    hv_collector = VirtualCollector(None, 'HP-UX')
    facts = ansible_facts({})

    # If a collector is instanciated with the wrong platform, virtual_facts
    # will be None.
    assert hv_collector.get_virtual_facts(facts) is None

    # Create test collector with the right platform
    hv_collector = VirtualCollector(None, 'HP-UX')
    assert hv._

# Generated at 2022-06-13 04:03:36.652435
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual = HPUXVirtual(dict(module=dict()))
    assert hpux_virtual.platform == 'HP-UX'


# Generated at 2022-06-13 04:03:38.012634
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual = HPUXVirtual(dict())
    assert virtual


# Generated at 2022-06-13 04:03:42.793200
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    HPUXVirtualCollector.collect()
    v = Virtual.read_facts()
    assert v['virtualization_type'] != 'host'
    assert v['virtualization_type'] != 'guest'
    assert v['virtualization_type'] == 'guest'
    assert v['virtualization_role'] != 'guest'

# Generated at 2022-06-13 04:03:44.515084
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():

    # Check whether all data was properly initialized
    obj = HPUXVirtual({})
    assert obj.platform == 'HP-UX'

# Generated at 2022-06-13 04:03:50.565976
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    # test data
    data = {
    }

    # mock AnsibleModule class
    class AnsibleModuleMock(object):
        def __init__(self, data, *args, **kwargs):
            self.params = data
            self.run_command = HPUXVirtualCollector.run_command
        def fail_json(*args, **kwargs):
            raise Exception("fail_json")

    # test with no virtualization tech
    module = AnsibleModuleMock(data)
    try:
        HPUXVirtual(module).get_virtual_facts()
        assert False
    except:
        assert True

    # test with vecheck
    module = AnsibleModuleMock(data)
    HPUXVirtualCollector.run_command = lambda self, data: (0, '', '')
    assert HPUXVirtual

# Generated at 2022-06-13 04:03:58.996294
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual import setup_module
    import ansible.module_utils.facts.virtual

    setup_module()
    # Initialize class HPUXVirtual and load get_virtual_facts method
    h = HPUXVirtual()
    h.module = ansible.module_utils.facts.virtual.AnsibleModuleFake('HP-UX')
    # Add some methods that are missing from the class
    h.module.run_command = run_command_fake
    h.module.exit_json = exit_json_fake

    facts_virtual = h.get_virtual_facts()

    assert facts_virtual['virtualization_tech_guest'] == set(['HPVM vPar'])
    assert facts_virtual['virtualization_tech_host'] == set()
    assert facts_virtual['virtualization_type']

# Generated at 2022-06-13 04:04:30.409886
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts = HPUXVirtual()
    assert virtual_facts.platform == 'HP-UX'


# Generated at 2022-06-13 04:04:39.385003
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtualCollector
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtualGuestCollector
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtualHostCollector

    hpuxvirtual = HPUXVirtual()
    hpuxvirtual_collector = HPUXVirtualCollector()
    hpuxvirtual_guest_collector = HPUXVirtualGuestCollector()
    hpuxvirtual_host_collector = HPUXVirtualHostCollector()

    assert len(hpuxvirtual_collector.collect()) > 0
    assert len(hpuxvirtual_guest_collector.collect()) == 0

# Generated at 2022-06-13 04:04:44.423881
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():

    virtual_facts_class_obj = HPUXVirtual()

    assert virtual_facts_class_obj.platform == 'HP-UX'
    assert virtual_facts_class_obj.get_virtual_facts() == {'virtualization_type': 'guest', 'virtualization_role': 'HPVM IVM', 'virtualization_tech_guest': {'HPVM IVM'}, 'virtualization_tech_host': set()}



# Generated at 2022-06-13 04:04:50.054366
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():

    from ansible.module_utils.facts.virtual.hpu import HPUXVirtual
    from ansible.module_utils import basic
    import ast

    fake_module = basic.AnsibleModule(
        argument_spec=dict()
    )
    fake_module.run_command = fake_run_command

    virtual_facts = HPUXVirtual({}, fake_module).get_virtual_facts()

    assert len(virtual_facts) == 4
    assert "virtualization_tech_guest" in virtual_facts
    assert "virtualization_tech_host" in virtual_facts
    assert "virtualization_type" in virtual_facts
    assert "virtualization_role" in virtual_facts
    assert ast.literal_eval(virtual_facts['virtualization_tech_guest']) == set(['HP vPar'])



# Generated at 2022-06-13 04:04:54.812789
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    module = AnsibleModuleMock()
    base = HPUXVirtual(module)
    assert base.platform == 'HP-UX'
    assert base._platform == 'HP-UX'


# Generated at 2022-06-13 04:04:59.720156
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_object = HPUXVirtual({})
    assert virtual_object.get_virtual_facts() == {
           'virtualization_tech_host': set([]),
           'virtualization_role': 'HPVM'
        }

# Generated at 2022-06-13 04:05:03.839135
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module = AnsibleModule(argument_spec={})
    virtual = HPUXVirtual(module=module)
    ansible_facts = {'ansible_virtual_facts': virtual.get_virtual_facts()}
    print(ansible_facts)


# Generated at 2022-06-13 04:05:12.103001
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts import FactModule
    module = FactModule()
    module = module.load_facts(module_name='ansible.module_utils.facts.virtual.hpux.HPUXVirtual',
                               module_args=dict(gather_subset=['!all', 'virtual']))
    module.get_facts()
    facts = dict(module._result['ansible_facts'])

    assert facts['virtualization_type'] == 'guest'
    assert facts['virtualization_role'] == 'HP nPar'
    assert facts['virtualization_tech_guest'] == set(['HP nPar'])
    assert facts['virtualization_tech_host'] == set([])



# Generated at 2022-06-13 04:05:13.847785
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual({}, {}, {})
    assert hv.platform == 'HP-UX'

# Generated at 2022-06-13 04:05:15.168529
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    x = HPUXVirtual({}, None)
    assert x is not None

# Generated at 2022-06-13 04:05:58.220162
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    guest_tech_set = set(['HP vPar', 'HPVM vPar', 'HPVM IVM', 'HP nPar'])
    host_tech_set = set(['HPVM'])
    hpux_virtual = HPUXVirtual()
    assert hpux_virtual
    assert sorted(guest_tech_set) == sorted(hpux_virtual.virtualization_tech_guest)
    assert sorted(host_tech_set) == sorted(hpux_virtual.virtualization_tech_host)
    assert hpux_virtual.virtualization_type == 'guest'
    assert hpux_virtual.virtualization_role == 'HP nPar'

# Generated at 2022-06-13 04:06:00.080385
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    v = HPUXVirtual({})
    assert v is not None

# Generated at 2022-06-13 04:06:01.602660
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual = HPUXVirtual()
    assert virtual.platform == 'HP-UX'


# Generated at 2022-06-13 04:06:04.788874
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    h = HPUXVirtual(dict())
    assert hasattr(h, 'platform')
    assert hasattr(h, 'get_virtual_facts')

# Generated at 2022-06-13 04:06:15.286461
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    v = HPUXVirtual(None)

    host_tech = set()
    guest_tech = set()

    virtual_facts = v.get_virtual_facts()
    assert virtual_facts['virtualization_tech_guest'] == guest_tech
    assert virtual_facts['virtualization_tech_host'] == host_tech

    # HP vPar virtualization
    v.module.run_command = lambda x: (0, "HP-UX vPars Virtual Partition Manager", "")
    virtual_facts = v.get_virtual_facts()
    guest_tech.add('HP vPar')
    assert virtual_facts['virtualization_tech_guest'] == guest_tech
    assert virtual_facts['virtualization_tech_host'] == host_tech
    assert virtual_facts['virtualization_type'] == 'guest'
    assert virtual

# Generated at 2022-06-13 04:06:20.913121
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual
    import pytest
    class MyModule(object):
        def run_command(self):
            return (0, '', '')

    virtual_facts = HPUXVirtual(module=MyModule()).get_virtual_facts()
    assert len(virtual_facts.keys()) == 4
    assert virtual_facts['virtualization_tech_guest'] == set()
    assert virtual_facts['virtualization_tech_host'] == set()
    assert virtual_facts['virtualization_type'] == 'guest'
    assert virtual_facts['virtualization_role'] == 'HP vPar'


# Generated at 2022-06-13 04:06:24.152251
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    # Define values of instance attributes
    virtual = HPUXVirtual()
    assert virtual.platform == 'HP-UX'
    assert virtual.virtualization_type == None
    assert virtual.virtualization_role == None


# Generated at 2022-06-13 04:06:35.537957
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    # Test /usr/sbin/parstatus
    module = FakeAnsibleModule()
    hpuxvirtual = HPUXVirtual(module=module)
    rc, out, err = module.run_command('/usr/sbin/parstatus')
    hpuxvirtual.get_virtual_facts()
    assert hpuxvirtual.facts['virtualization_type'] == 'guest'
    assert hpuxvirtual.facts['virtualization_role'] == 'HP nPar'
    assert hpuxvirtual.facts['virtualization_tech_guest'] == set(['HP nPar'])
    assert hpuxvirtual.facts['virtualization_tech_host'] == set()
    # Test /usr/sbin/vecheck
    module = FakeAnsibleModule()
    hpuxvirtual = HPUXVirtual(module=module)
    rc, out, err

# Generated at 2022-06-13 04:06:37.321837
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    facts = {}
    vm = HPUXVirtual(module=None)
    facts = vm.get_virtual_facts()
    assert 'virtualization_type' in facts
    assert 'virtualization_role' in facts
    assert 'virtualization_tech_host' in facts
    assert 'virtualization_tech_guest' in facts

# Generated at 2022-06-13 04:06:38.589121
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual(dict(module=dict()))
    assert hv.platform == 'HP-UX'


# Generated at 2022-06-13 04:08:40.407338
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible_collections.ansible.community.tests.unit.modules.utils import AnsibleExitJson
    from ansible_collections.ansible.community.tests.unit.modules.utils import AnsibleFailJson
    from ansible_collections.ansible.community.tests.unit.modules.utils import ModuleTestCase
    from ansible_collections.ansible.community.tests.unit.modules.utils import set_module_args

    class TestHPUXVirtual(HPUXVirtual):
        def __init__(self, module):
            self.module = module

    # Test HP-UX virtualization_type as guest
    module_args = set_module_args()
    module = ModuleTestCase(pass_argv=['-vvvv'], argument_spec=dict(), supports_check_mode=False)

# Generated at 2022-06-13 04:08:43.341541
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    hux = HPUXVirtual()
    hux.module = MockModule()
    assert hux.get_virtual_facts() == {'virtualization_type': None, 'virtualization_role': None, 'virtualization_tech_guest': set(), 'virtualization_tech_host': set()}


# Generated at 2022-06-13 04:08:48.898442
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual = HPUXVirtual()
    assert virtual.platform == 'HP-UX'
    assert virtual.virtualization_type == 'unknown'
    assert virtual.virtualization_role == 'unknown'
    assert len(virtual.virtualization_tech_guest) == 0
    assert len(virtual.virtualization_tech_host) == 0
    assert virtual.virtualization_guest_uuid is None
    assert virtual.virtualization_host_uuid is None

# Generated at 2022-06-13 04:08:52.328851
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    v = HPUXVirtual()

    assert v._platform == 'HP-UX'
    assert v.get_virtual_facts() == {}
    assert v.get_virtual_facts() == {}

# Generated at 2022-06-13 04:09:00.996347
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.test.test_hpu import m_run_command
    from ansible.module_utils.facts.virtual.test.test_hpu import m_exists
    from ansible.module_utils.facts.virtual.test.test_hpu import TestModule
    from ansible.module_utils.facts import virtual
    import os

    class MockModule():
        class RunCommand():
            def __init__(self, a, b, c):
                return
            def __call__(self):
                return (0, 'test', '')

        class Exists():
            def __init__(self, a):
                return
            def __call__(self):
                return True

        def __init__(self):
            self.run_command = MockModule.RunCommand

# Generated at 2022-06-13 04:09:03.119400
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual = HPUXVirtual()
    assert hpux_virtual.platform == 'HP-UX'

# Generated at 2022-06-13 04:09:04.874612
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual(dict())
    assert hv is not None
    assert hv.platform == 'HP-UX'



# Generated at 2022-06-13 04:09:06.614839
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual(dict())
    assert isinstance(hv, HPUXVirtual)


# Generated at 2022-06-13 04:09:15.245801
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    import mock
    import tempfile

    tmp_file_name = 'hp-ux_virtual_facts.txt'
    tmp_file_path = os.path.join(tempfile.gettempdir(), tmp_file_name)

    # Create a mock module, this is needed because we want to mock the
    # module.run_command() method. The method needs a module object
    # to pass. So we provide the mock object.
    module = mock.MagicMock()
    # Create an instance of HPUXVirtual.
    test_hpuX_virtual = HPUXVirtual(module)
    # Create a dictionary that returns the value for the keys
    # "stdout", "stdout_lines" and "rc" of the method run_command()
    # when called with '/usr/sbin/vecheck'.
    side_effect_dict

# Generated at 2022-06-13 04:09:20.984770
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    """
    Unit test for method get_virtual_facts of class HPUXVirtual
    """
    hp_ux_virtual = HPUXVirtual()

    # Test 1
    # When /usr/sbin/vecheck exists
    hp_ux_virtual.module.run_command.return_value = (0, "HP-UX vPars", "")
    hp_ux_virtual.module.stat.return_value = (0, "")
    hp_ux_virtual.module.os.path.exists.return_value = True
    virtual_facts = hp_ux_virtual.get_virtual_facts()

    assert virtual_facts['virtualization_type'] == 'guest'
    assert virtual_facts['virtualization_role'] == 'HP vPar'