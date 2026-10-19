

# Generated at 2022-06-13 03:59:29.295274
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module = AnsibleModule(argument_spec={})
    virtual_collector = HPUXVirtualCollector(module)
    virtual = virtual_collector.collect()[0]
    virtual_facts = virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'guest'
    assert virtual_facts['virtualization_role'] == 'HP vPar'
    assert virtual_facts['virtualization_tech_guest'] == set(['HP vPar'])
    assert virtual_facts['virtualization_tech_host'] == set()


# Generated at 2022-06-13 03:59:32.611131
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts = HPUXVirtual({})
    assert virtual_facts._platform == 'HP-UX'
    assert virtual_facts._fact_class is HPUXVirtual


# Generated at 2022-06-13 03:59:35.066498
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    '''
    Test constructor of class HPUXVirtual
    '''
    hpx_virtual = HPUXVirtual(dict(), None)
    assert hpx_virtual.platform == 'HP-UX'


# Generated at 2022-06-13 03:59:40.790373
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_obj = HPUXVirtual()
    assert virtual_obj.virtualization_type == 'unknown'
    assert virtual_obj.virtualization_role == 'unknown'
    assert virtual_obj.virtualization_technique == 'unknown'
    assert virtual_obj.virtualization_technique_version == 'unknown'
    assert virtual_obj.virtualization_systems_hypervisor_hostname == 'unknown'
    assert virtual_obj.virtualization_systems_hypervisor_product == 'unknown'
    assert virtual_obj.virtualization_systems_hypervisor_version == 'unknown'
    assert virtual_obj.virtualization_systems_hypervisor_uuid == 'unknown'

# Generated at 2022-06-13 03:59:50.840172
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    import sys
    import tempfile
    from ansible.module_utils.facts.virtual.hpux.HPUXVirtual import HPUXVirtual
    import json

    class MockModule(object):
        def __init__(self, *args, **kwargs):
            self.exit_json = sys.exit
            self.fail_json = sys.exit
            self.run_command = kwargs.get('run_command', sys.exit)

    class Fake_FileObj(object):
        def __init__(self, path):
            self.path = path

    def create_file(con_file, data=None):
        if data:
            with open(con_file, "w+") as fd:
                fd.write(data)
        return Fake_FileObj(con_file)


# Generated at 2022-06-13 03:59:56.937355
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    '''Unit test for method get_virtual_facts of class HPUXVirtual'''
    HPUXVirtual_obj = HPUXVirtual()
    HPUXVirtual_obj.module = DummyAnsibleModule()
    expected_virtual_facts = {
                                'virtualization_type': u'guest',
                                'virtualization_role': u'HP vPar',
                                'virtualization_tech_guest': set([u'HP nPar', u'HP vPar']),
                                'virtualization_tech_host': []
                             }
    actual_virtual_facts = HPUXVirtual_obj.get_virtual_facts()
    assert actual_virtual_facts == expected_virtual_facts



# Generated at 2022-06-13 03:59:58.950241
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual = HPUXVirtual()
    assert virtual.virtualization_type == 'host' or virtual.virtualization_type == 'guest' or virtual.virtualization_type == 'container'

# Generated at 2022-06-13 04:00:02.591326
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    v = HPUXVirtual()
    v.module = FakeModule(
        params=dict(
            gather_subset=['!all', 'virtual'],
        ),
    )
    v.get_virtual_facts()
    return v.facts



# Generated at 2022-06-13 04:00:07.841358
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    import module_utils.facts.virtual.hp
    mod = module_utils.facts.virtual.hp
    h = mod.HPUXVirtual({'PATH': '/usr/bin:/bin'})
    facts = h.get_virtual_facts()
    assert facts['virtualization_type'] == 'host'
    assert facts['virtualization_role'] == 'HPVM'
    assert facts['virtualization_tech_guest'] == set(['HPVM'])
    assert facts['virtualization_tech_host'] == set()

# Generated at 2022-06-13 04:00:18.075899
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtualCollector
    from ansible.module_utils.facts.virtual.hpux import HPUXCollector
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtualCollector

    os.path.exists = lambda x: True
    os.path.isfile = lambda x: True

    class Args:
        def __init__(self, module):
            self.module = module

    class Module:
        def __init__(self):
            self.run_command = lambda x: (0, '', '')

    args = Args(Module())
    hpux_collector = HPUXVirtualCollector(args)
    hp

# Generated at 2022-06-13 04:00:33.255944
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module = AnsibleModule(argument_spec={})
    virtual = HPUXVirtual(module)

    # with foo active
    module.run_command = Mock(return_value=(0, '', ''))
    facts = virtual.get_virtual_facts()
    assert facts == {
        'virtualization_type': 'guest',
        'virtualization_role': 'HP vPar',
        'virtualization_tech_host': set(),
        'virtualization_tech_guest': set(['HP vPar'])
    }

    # without foo active
    module.run_command = Mock(return_value=(256, '', ''))
    facts = virtual.get_virtual_facts()
    assert facts == {
        'virtualization_tech_host': set(),
        'virtualization_tech_guest': set(),
    }

# Generated at 2022-06-13 04:00:40.480536
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    '''Return virtual facts'''

    import os
    import subprocess
    class ModuleStub:
        def __init__(self):
            self.run_command_statistics = {'called': 0, 'rc': 0, 'out': 'Test', 'err': 'Test'}
            self.run_command_calls = []

        def run_command(self, args, check_rc=True):
            self.run_command_calls.append(args)
            self.run_command_statistics['called'] += 1
            return self.run_command_statistics['rc'], self.run_command_statistics['out'], self.run_command_statistics['err']

# Generated at 2022-06-13 04:00:46.596227
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    module = HPUXVirtual(dict())
    assert module.__class__.__name__ == 'HPUXVirtual'
    assert module.virtualization_type == 'guest'
    assert module.virtualization_role == 'HP vPar'
    assert module.virtualization_tech_guest == set(['HP vPar'])
    assert module.virtualization_tech_host == set()


# Generated at 2022-06-13 04:00:49.971666
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual({})
    assert hv.module.run_command.call_count == 0
    assert hv.facts['virtualization_type'] == 'host'
    assert hv.facts['virtualization_role'] == ''
    assert hv.facts['virtualization_tech_host'] == set()
    assert hv.facts['virtualization_tech_guest'] == set()



# Generated at 2022-06-13 04:00:53.841266
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpuxvirtual = HPUXVirtual()
    assert hpuxvirtual.virtualization_type == 'guest'
    assert hpuxvirtual.virtualization_type_role == 'HP nPar'
    assert hpuxvirtual.virtualization_tech_guest == set(['HP nPar', 'HP vPar'])
    assert hpuxvirtual.virtualization_tech_host == set()

# Generated at 2022-06-13 04:01:01.223391
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils import basic

    module = basic.AnsibleModule(
        argument_spec=dict()
    )

    virtual = HPUXVirtual(module)

    facts = virtual.get_virtual_facts()

    assert 'virtualization_tech_guest' in facts
    assert 'virtualization_tech_host' in facts
    assert 'virtualization_type' in facts
    assert 'virtualization_role' in facts

# Generated at 2022-06-13 04:01:02.455526
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():

    hpx_virtual = HPUXVirtual()
    hpx_virtual.module

# Generated at 2022-06-13 04:01:04.351323
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual({})
    assert hv.platform == 'HP-UX'
    assert hv.virtual_facts == {}


# Generated at 2022-06-13 04:01:15.074651
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    class HPUXVirtualModuleMock(object):
        CMD_RC = -1
        CMD_STDOUT = ''
        CMD_STDERR = ''
        def run_command(self, command):
            return HPUXVirtualModuleMock.CMD_RC, HPUXVirtualModuleMock.CMD_STDOUT, HPUXVirtualModuleMock.CMD_STDERR
    module = HPUXVirtualModuleMock()
    virtual = HPUXVirtual(module)
    virtual_facts = virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''
    assert virtual_facts['virtualization_tech_host'] == set()
    assert virtual_facts['virtualization_tech_guest'] == set()

    HPUXVirtualModuleM

# Generated at 2022-06-13 04:01:25.254177
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtualCollector
    from ansible.module_utils.facts.utils import FactsCommon
    import os

    class FakeCommandModule:
        """
        Fake command module
        """
        def __init__(self):
            self.run_command = os.system
            self.check_mode = False

    class FakeModuleUtilsFactsCommon(FactsCommon):
        """
        Fake module common utils
        """
        def __init__(self, module):
            self.module = module

    class FakeSysModule:
        """
        Fake sys module
        """

# Generated at 2022-06-13 04:01:46.929560
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    import mock
    from ansible.module_utils.facts.virtual.hpx import HPUXVirtual

    hpx_virtual = HPUXVirtual()
    hpx_virtual.module = mock.Mock()
    hpx_virtual.module.run_command.return_value = (0, "", "")
    assert hpx_virtual.get_virtual_facts() == {'virtualization_type': 'host',
                                               'virtualization_role': 'HPVM',
                                               'virtualization_tech_guest': set(['HPVM']),
                                               'virtualization_tech_host': set()}

    hpx_virtual.module.run_command.return_value = (0, "Running HPVM guest", "")

# Generated at 2022-06-13 04:01:53.629271
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():

    module = AnsibleModule(
        argument_spec = dict()
    )

    virtual_facts = HPUXVirtual(module).collect()
    assert virtual_facts['virtualization_type'] == 'host'
    assert virtual_facts['virtualization_role'] == 'HPVM'
    assert virtual_facts['virtualization_tech_guest'] == {'HPVM', 'HPVM vPar', 'HPVM IVM'}
    assert virtual_facts['virtualization_tech_host'] == set()


# Generated at 2022-06-13 04:01:54.871484
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual()
    assert hv.platform == 'HP-UX'


# Generated at 2022-06-13 04:01:58.029549
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    test_module = AnsibleModule(argument_spec={})
    virtual_facts = HPUXVirtual().get_virtual_facts()
    assert type(virtual_facts) == dict



# Generated at 2022-06-13 04:01:59.619115
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual()
    assert hv.platform == 'HP-UX'


# Generated at 2022-06-13 04:02:01.604377
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    facts = {}
    HPUXVirtual(facts, {}, {})
    assert 'virtualization_tech_guest' not in facts
    assert 'virtualization_tech_host' not in facts
    assert 'virtualization_type' not in facts
    assert 'virtualization_role' not in facts


# Generated at 2022-06-13 04:02:04.878252
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    import sys

    if sys.version_info[0] < 3:
        from mock import Mock
    else:
        from unittest.mock import Mock

    module = Mock()
    module.run_command = Mock(return_value=(0, '', ''))

    hv = HPUXVirtual(module)
    hv.get_virtual_facts()



# Generated at 2022-06-13 04:02:09.546241
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual import HPUXVirtual
    module = HPUXVirtual()
    facts = module.get_virtual_facts()
    assert facts['virtualization_technologies'] == ['HP nPar', 'HP vPar', 'HPVM', 'HPVM vPar', 'HPVM IVM']
    assert facts['virtualization_type'] == 'guest'
    assert facts['virtualization_role'] == 'HP nPar'
    assert facts['virtualization_tech_guest'] == set(['HP nPar', 'HP vPar', 'HPVM', 'HPVM vPar', 'HPVM IVM'])
    assert facts['virtualization_tech_host'] == set()

# Generated at 2022-06-13 04:02:13.235527
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():

    # test fixture
    fake_module = FakeAnsibleModule()
    h_module = HPUXVirtual()
    h_module.module = fake_module
    fake_module.run_command = run_command

    fact_result = h_module.get_virtual_facts()
    fact_expected = {
        "virtualization_type": "host",
        "virtualization_role": "HPVM",
        "virtualization_tech_host": set(['HPVM']),
        "virtualization_tech_guest": set(['HPVM'])
    }
    assert fact_result == fact_expected



# Generated at 2022-06-13 04:02:16.209845
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpar = HPUXVirtual()
    assert hpar.platform == 'HP-UX'


if __name__ == '__main__':
    test_HPUXVirtual()

# Generated at 2022-06-13 04:02:58.569940
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts_obj = HPUXVirtual(dict())
    assert virtual_facts_obj.platform == 'HP-UX'
    assert virtual_facts_obj.get_virtual_facts() == {}


# Generated at 2022-06-13 04:03:04.607693
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual({},{},{})
    assert hv.get_virtual_facts()['virtualization_type'] == 'guest', "Failed to return correct virtualization_type"
    assert hv.get_virtual_facts()['virtualization_role'] == 'HP vPar', "Failed to return correct virtualization_role"
    assert hv.get_virtual_facts()['virtualization_tech_guest'] == set(['HP vPar']), "Failed to return correct virtualization_tech_guest"
    assert hv.get_virtual_facts()['virtualization_tech_host'] == set([]), "Failed to return correct virtualization_tech_host"



# Generated at 2022-06-13 04:03:09.096614
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    module = AnsibleModule(argument_spec={})
    virt = HPUXVirtual(module=module)
    out = dict(virtualization_type='host',
               virtualization_role='HPVM',
               virtualization_tech_guest=set(),
               virtualization_tech_host=set(['HPVM']))
    assert virt.get_virtual_facts() == out

# Generated at 2022-06-13 04:03:16.983447
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    import platform
    hpux_virtual_facts = HPUXVirtual(module=None)
    assert hpux_virtual_facts.platform == 'HP-UX'
    assert hpux_virtual_facts.virtualization_type is None
    assert hpux_virtual_facts.virtualization_role is None
    assert hpux_virtual_facts.virtualization_role_guest is None
    assert hpux_virtual_facts.virtualization_role_host is None
    assert hpux_virtual_facts.virtualization_role_guest is None
    assert hpux_virtual_facts.virtualization_role_host is None
    assert hpux_virtual_facts.virtualization_role_guest is None
    assert hpux_virtual_facts.virtualization_role_host is None

# Generated at 2022-06-13 04:03:20.232275
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual = HPUXVirtual()
    assert hpux_virtual.platform == 'HP-UX'
    assert hpux_virtual.get_virtual_facts() == {}

# End of test

# Generated at 2022-06-13 04:03:21.800623
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    h = HPUXVirtual('', '', '')
    assert h.platform == 'HP-UX'

# Generated at 2022-06-13 04:03:31.218474
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    """
    Test function for get_virtual_facts of class HPUXVirtual
    Checks for the output of the function for various cases
    """
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtualCollector
    from ansible.module_utils.facts.virtual.hpux import test_HPUXVirtual_get_virtual_facts as test_func
    class MockModule():
        def __init__(self):
            self.params = {}
            self.params['gather_subset'] = ['all']
            self.run_command = test_func.run_command

    class MockCollector():
        def __init__(self):
            self.module = MockModule()
            self.class_name = 'Virtual'

# Generated at 2022-06-13 04:03:36.438934
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    import tempfile
    import json
    import subprocess

    def run_command(module, cmd):
        proc = subprocess.Popen(cmd, shell=True,
         stdin=subprocess.PIPE,
         stdout=subprocess.PIPE,
         stderr=subprocess.PIPE,
         close_fds=True)
        output = proc.communicate()
        if proc.returncode == 0:
            return (0, output[0], None)
        else:
            return (proc.returncode, None, output[1])

    class Module(object):
        def __init__(self, tmpfile):
            self._tmpfile = tmpfile

        def fail_json(self, **args):
            pass


# Generated at 2022-06-13 04:03:43.970638
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    vm = HPUXVirtual({})
    vm.module = MagicMock()
    vm.module.run_command.return_value = 0, "Running HPVM guest, state=RUNNING\n", ""
    vm.get_virtual_facts()
    out = vm.facts

# Generated at 2022-06-13 04:03:50.320998
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    # First, remove all environment variables
    env = dict(os.environ)
    for k in env.keys():
        del os.environ[k]

    # Set environment variables
    vecheck = '/usr/sbin/vecheck'
    hpvminfo = '/opt/hpvm/bin/hpvminfo'
    parstatus = '/usr/sbin/parstatus'
    # File /usr/sbin/vecheck exists
    os.environ['TEST_HPUX_VECHECK'] = vecheck
    hv = HPUXVirtual()
    os.stat(vecheck)

# Generated at 2022-06-13 04:04:54.413567
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_hpux = HPUXVirtual(dict())
    virtual_hpux.get_virtual_facts()

# Generated at 2022-06-13 04:04:57.396811
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpx = HPUXVirtual()

    assert hpx.platform == 'HP-UX'

# Generated at 2022-06-13 04:05:06.559980
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    import sys

    if sys.version_info[0] == 2:
        import types
        class AnsibleModule(types.ModuleType):
            def __init__(self):
                pass
            def run_command(self, command):
                class RcOutErr():
                    def __init__(self):
                        self.rc = 0
                        self.out = ''
                        self.err = ''
                        self.stdout_lines = []
                        self.stderr_lines = []
                    def __getitem__(self, index):
                        return [self.rc, self.out, self.err][index]
                    def __iter__(self):
                        return iter([self.rc, self.out, self.err])
                if command == '/usr/sbin/vecheck':
                    rcouterr = RcOutErr()


# Generated at 2022-06-13 04:05:08.224963
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual = HPUXVirtual()
    assert hpux_virtual.platform == 'HP-UX'


# Generated at 2022-06-13 04:05:18.096276
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpuxtopology import HPUXVirtual
    virtual_facts = {}
    obj = HPUXVirtual(virtual_facts)
    obj.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'guest'
    assert virtual_facts['virtualization_role'] == 'HP vPar'
    virtual_facts = {}
    obj = HPUXVirtual(virtual_facts)
    obj.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'guest'
    assert virtual_facts['virtualization_role'] == 'HPVM'
    virtual_facts = {}
    obj = HPUXVirtual(virtual_facts)
    obj.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'guest'

# Generated at 2022-06-13 04:05:24.471844
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
   hv = HPUXVirtual(dict())
   assert hv.virtualization_type == 'guest' and hv.virtualization_role == 'HP nPar'
   assert hv.virtualization_tech_guest == set(['HP nPar']) and hv.virtualization_tech_host == set()
   assert hv.virtualization_system == '' and hv.virtualization_role == 'HP nPar'



# Generated at 2022-06-13 04:05:26.011469
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux_virtual = HPUXVirtual({})
    assert hpux_virtual.platform == 'HP-UX'

# Generated at 2022-06-13 04:05:34.028221
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils import basic
    import sys

    args = {
        'ANSIBLE_MODULE_ARGS': {
            'gather_subset': 'all',
        }
    }
    module = basic.AnsibleModule(**args)
    module.run_command = basic.AnsibleModule.run_command
    module.get_bin_path = basic.AnsibleModule.get_bin_path
    sys.modules['ansible.module_utils.facts'] = basic
    collector = HPUXVirtualCollector(module)
    virtual_facts_dict = collector.collect()['ansible_facts']['ansible_virtual']
    assert virtual_facts_dict['virtualization_type'] == 'host'

# Generated at 2022-06-13 04:05:39.193133
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    m = AnsibleModule(argument_spec={})

    # Mock linux_distribution ansible module method
    def mock_linux_distribution(self):
        return ['HP-UX']

    m.linux_distribution = mock_linux_distribution.__get__(m)

    # Mock run_command ansible module method
    def mock_run_command(self, cmd, check_rc=True, close_fds=True, executable=None, data=None):
        if cmd == "/usr/sbin/vecheck":
            return 0, "running on HP vPar", ""
        if cmd == "/opt/hpvm/bin/hpvminfo":
            return 0, "Running on HPVM vPar", ""
        if cmd == "/usr/sbin/parstatus":
            return 0, "running on HP nPar", ""
       

# Generated at 2022-06-13 04:05:41.078983
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    virtual_facts = HPUXVirtual(dict()).get_virtual_facts()

    assert isinstance(virtual_facts, dict)


# Generated at 2022-06-13 04:06:34.399320
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    # Test multiple virtualization technology
    module = AnsibleModule(
        argument_spec=dict()
    )
    set_module_args(dict(gather_subset='!all,!any,virtual'))
    # hpvm nPar
    hpvm_npar_facts = dict(
        virtualization_tech_guest=set(['HPVM IVM', 'HP nPar']),
        virtualization_tech_host=set(),
        virtualization_type='guest',
        virtualization_role='HPVM IVM',
    )
    # hpvm IVM

# Generated at 2022-06-13 04:06:37.921429
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpuxvirtual = HPUXVirtual({})
    assert hpuxvirtual.platform == 'HP-UX'
    assert hpuxvirtual.collector_class == HPUXVirtualCollector
    hpuxvirtual = HPUXVirtual({'module_setup': True})
    assert hpuxvirtual.get_virtual_facts()


# Generated at 2022-06-13 04:06:40.260424
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    v = HPUXVirtual({})
    assert v.platform == 'HP-UX'


# Generated at 2022-06-13 04:06:45.489960
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    import ansible.module_utils.facts.virtual.hpux as hpux
    test_obj = hpux.HPUXVirtual()
    test_obj.module = MockModule()
    assert hpux.HPUXVirtual().get_virtual_facts() == {'virtualization_type': 'host', 'virtualization_role': 'HPVM',
                                                     'virtualization_tech_host': {'HPVM'}, 'virtualization_tech_guest': set()}



# Generated at 2022-06-13 04:06:53.283288
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts import FactCollector
    import json

    # Setup Facts instance for collection
    fake_dist = {
        'distribution': 'HP-UX',
        'distribution_version': 'B.11.31',
    }

    # Note: the following code is needed to fake the module
    #       import within the Facts class
    class AnsibleModuleFake:

        def __init__(self):
            self.params = {}

        def fail_json(self, *args, **kwargs):
            pass

        def run_command(self, *args, **kwargs):
            if args[0] == "/usr/sbin/vecheck":
                return (0, '', '')

# Generated at 2022-06-13 04:06:58.046899
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpux import HPUXVirtual
    from ansible.module_utils._text import to_text
    from ansible.module_utils.six import BytesIO
    import ansible.module_utils.facts.virtual.hpux

    class RunCommandAnsibleModuleMock():
        class AnsibleModule():
            def __init__(self):
                self.run_command = RunCommandAnsibleModuleMock()

        def __init__(self):
            self.params = {'virtualization_type': 'guest',
                           'virtualization_role': 'HP vPar'}


# Generated at 2022-06-13 04:07:03.828671
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    data = HPUXVirtualCollector.collect()
    assert data['virtualization_tech_guest'] == set(['HPVM', 'HP nPar', 'HP vPar', 'HPVM vPar', 'HPVM IVM'])
    assert data['virtualization_tech_host'] == set(['HPVM'])
    assert data['virtualization_role'] == 'HPVM'
    assert data['virtualization_type'] == 'host'

# Generated at 2022-06-13 04:07:07.565173
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    # This method runs only on HP-UX
    module = MockModule()
    virt = HPUXVirtual(module)
    assert virt.get_virtual_facts() == {'virtualization_tech_guest': set(),
                                        'virtualization_tech_host': set(),
                                        'virtualization_type': 'host',
                                        'virtualization_role': 'HPVM'}



# Generated at 2022-06-13 04:07:14.807075
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    dmidecode_out = """HPVM host"""
    hpvm_out = """hpvminfo
        Running: HPVM host
        Version: B.11.31
        HPVM Guest status:
        ivm01: Running HPVM HP-UX vpar
        ivm02: Running HPVM HP-UX vpar
        ivm03: Running HPVM HP-UX vpar
    """
    vecheck_out = """vecheck
        hpvm01: HPVM HP-UX vpar
        hpvpar: HPVM HP-UX vpar
    """
    parstatus_out = """parstatus
        hpvm02: HPVM HP-UX npar
        hpvpar: HPVM HP-UX npar
    """

# Generated at 2022-06-13 04:07:24.063920
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    _temporary_module_args = {'gather_subset': '!all,min'}
    _ansible_module = AnsibleModule(argument_spec=_temporary_module_args, supports_check_mode=False)
    _ansible_module.run_command = Mock(return_value=(0, '', ''))
    _ansible_module.exit_json = Mock(return_value='dummy')

    hpux_virtual = HPUXVirtual(_ansible_module)
    hpux_virtual.get_virtual_facts()

# Generated at 2022-06-13 04:08:32.119042
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    module = FakeModule()
    facts = HPUXVirtual(module).get_virtual_facts()

    assert 'virtualization_type' in facts
    assert 'virtualization_role' in facts
    assert 'virtualization_tech_guest' in facts
    assert 'virtualization_tech_host' in facts

    assert facts['virtualization_type'] == 'guest'
    assert facts['virtualization_role'] == 'HP nPar'
    assert facts['virtualization_tech_guest'] == {'HP nPar'}
    assert facts['virtualization_tech_host'] == set()


# Mock for AnsibleModule

# Generated at 2022-06-13 04:08:41.800576
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    ''' HPUXVirtual() loads correct virtualization_type when running on hpux '''

    class Module:
        def __init__(self):
            self.params = {}

        def run_command(self, cmd):
            out = ''

# Generated at 2022-06-13 04:08:43.276543
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hpux = HPUXVirtual({}, {})
    assert hpux.platform == 'HP-UX'

# Generated at 2022-06-13 04:08:48.787470
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    virtual_facts_dict = {
        'virtualization_type': 'guest',
        'virtualization_role': 'HP vPar',
        'virtualization_tech_guest': set(['HP vPar']),
        'virtualization_tech_host': set()}

    virtual_facts_object = HPUXVirtual(dict())
    virtual_facts = virtual_facts_object.get_virtual_facts()
    assert virtual_facts == virtual_facts_dict

# Generated at 2022-06-13 04:08:54.363035
# Unit test for constructor of class HPUXVirtual
def test_HPUXVirtual():
    hv = HPUXVirtual()
    assert hv.virtualization_tech_host == set()
    assert hv.virtualization_tech_guest == set()
    assert hv.virtualization_role == None
    assert hv.virtualization_type == None

if __name__ == '__main__':
    test_HPUXVirtual()

# Generated at 2022-06-13 04:09:01.830245
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    import ansible.module_utils.facts.virtual.hpux_virtual as hpux_virtual
    import tempfile

    # mock module and commands
    fake_module = type('module', (object,), {
        'run_command': lambda *args, **kwargs: (
            0,
            '',
            ''
        ),
    })
    possible_binary = ['/usr/sbin/vecheck', '/opt/hpvm/bin/hpvminfo', '/usr/sbin/parstatus']
    for pb in possible_binary:
        tmp_dir = tempfile.mkdtemp()
        os.mkdir(os.path.join(tmp_dir, pb))
        hpux_virtual.HPUXVirtual.module = fake_module

        # execute test
        vf = hpux_virtual.HPUXVirtual

# Generated at 2022-06-13 04:09:08.776609
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.hpar import HPUXVirtual
    module = ansible_mock
    v = HPUXVirtual(module)

    v.module.run_command.return_value = (0, 'output', 'error')
    v.module.params = {}
    v.module.params['gather_subset'] = []
    virtual_facts = v.get_virtual_facts()

    assert virtual_facts['virtualization_type'] == 'guest'
    assert virtual_facts['virtualization_role'] == 'HP nPar'
    assert 'HP nPar' in virtual_facts['virtualization_tech_guest']
    assert len(virtual_facts['virtualization_tech_guest']) == 1



# Generated at 2022-06-13 04:09:16.589299
# Unit test for method get_virtual_facts of class HPUXVirtual
def test_HPUXVirtual_get_virtual_facts():
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.collector import DefaultCollector

    module = MockModule()
    mod_dict = dict()
    mod_dict['ansible_module_my_var1'] = 'my_var1'
    mod_dict['ansible_module_my_var2'] = 'my_var2'
    module.params = mod_dict

    virt = HPUXVirtual(module)

    class MockModuleUtilsFactsCollectorCollector(object):
        def __init__(self, module=None, support_check_mode=True,
                     dummy_arg='dummy'):
            self.module = module
            self.dummy_arg = dummy_arg
            return

        def get_collectors(self):
            collection = dict()
            collection