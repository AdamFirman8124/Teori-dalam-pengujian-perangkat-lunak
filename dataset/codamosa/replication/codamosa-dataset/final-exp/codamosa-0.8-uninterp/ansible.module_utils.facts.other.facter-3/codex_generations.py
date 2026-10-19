

# Generated at 2022-06-13 01:58:51.987794
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():

    # case 1
    module = MockModule()
    module.run_command.return_value = 0, '/usr/bin/facter', ''
    testCollector = FacterFactCollector(module)
    ret = testCollector.find_facter(module)
    assert ret == '/usr/bin/facter'

    # case 2
    module = MockModule()
    module.run_command.return_value = 0, '/usr/bin/cfacter', ''
    testCollector = FacterFactCollector(module)
    ret = testCollector.find_facter(module)
    assert ret == '/usr/bin/cfacter'

    # case 3
    module = MockModule()
    module.run_command.return_value = 1, '', ''
    testCollector = FacterFactCollector(module)
    ret

# Generated at 2022-06-13 01:58:58.461535
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    # Creating instance of class module_utils.facts.collector.BaseFactCollector to stub method get_bin_path
    class StubBaseFactCollector:
        def get_bin_path(self, bin_name, opt_dirs=None):
            if bin_name == 'facter':
                # the second time will return None
                try:
                    return StubBaseFactCollector.return_get_bin_path
                except:
                    StubBaseFactCollector.return_get_bin_path = '/fake/facter_path'
                    return StubBaseFactCollector.return_get_bin_path
            else:
                return None
    # Creating instance of class module_utils.facts.collector.BaseFactCollector to stub method run_command

# Generated at 2022-06-13 01:59:09.074304
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    # Create a dummy module instance
    class DummyModule():
        def __init__(self):
            self.run_command_results = [
                (0, '{"facter_test1": "test1"}', ''),
                (1, 'unknown json', "Couldn't load nokogiri")
            ]
            self.run_command_index = 0
        def get_bin_path(self, executable, opt_dirs=None):
            if executable == 'facter':
                return '/usr/bin/facter'
            elif executable == 'cfacter':
                return '/opt/puppetlabs/bin/cfacter'
            else:
                return None

# Generated at 2022-06-13 01:59:13.658795
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    # test object initialization
    ffct = FacterFactCollector()
    # test collect method
    res = ffct.collect()
    assert isinstance(res, dict)
    assert 'facter' in ffct._fact_ids


# Generated at 2022-06-13 01:59:19.726721
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    class MockedModule(object):
        def get_bin_path(self, prog, opt_dirs=[]):
            if prog == 'cfacter':
                return '/opt/puppetlabs/bin/cfacter'
            elif prog == 'facter':
                return '/opt/facter/bin/facter'
            else:
                return None

        def run_command(self, cmd):
            if cmd == 'facter' or cmd == '/opt/facter/bin/facter --puppet --json':
                return 0, '{"some_fact": "some_value", "another_one": "another_value"}', ''

# Generated at 2022-06-13 01:59:29.455713
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    # in this test, we stub get_bin_path and run_command
    # these stubs return hard-coded paths
    facter_script = 'additional-facts/facter.sh'
    cfacter_script = 'additional-facts/cfacter.sh'

    # populate constants
    facter_path = './tests/unit/additional-facts/' + facter_script
    cfacter_script_path = './tests/unit/additional-facts/' + cfacter_script

    # populate fake bin path
    class Module:
        def get_bin_path(self, bin_name, opt_dirs=[]):
            return {
                'facter': facter_path,
                'cfacter': cfacter_script_path
            }[bin_name]


# Generated at 2022-06-13 01:59:38.672958
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    class TestModule():
        def get_bin_path(self, bin, opt_dirs=None):
            if bin == 'facter':
                return '/path/to/facter'
            elif bin == 'cfacter':
                return None
            else:
                return None

        def run_command(self, command):
            if command == '/path/to/facter --puppet --json' or command == '/path/to/cfacter --puppet --json':
                return 0, '{ "fake": "value" }', ''
            elif command == '/path/to/facter --puppet --json' or command == '/path/to/cfacter --puppet --json':
                return 0, 'Malformed JSON', ''
            else:
                return 1, '', ''

    test_module = TestModule()

# Generated at 2022-06-13 01:59:47.064617
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils import basic
    from ansible.module_utils.six.moves import StringIO
    import os
    import tempfile

    # ensure that we don't run this test unless facter is installed
    facter_path = ansible_collector.get_ansible_collector().find_facter(basic.AnsibleModule(
    ).get_bin_path)
    if facter_path is None:
        return None

    # create a temp dir and files to use in the tests
    tmpdir = tempfile.mkdtemp()
    facter_path = os.path.join(tmpdir, 'facter')

    # write the binaries to the

# Generated at 2022-06-13 01:59:56.354678
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    from ansible.module_utils.facts import ModuleFaker

    fake_module = ModuleFaker()
    fake_module.params = {}

    # Set searchbin to ['/usr/bin/facter', '/opt/puppetlabs/bin/facter']
    fake_module.get_bin_path = lambda x, opt_dirs: '/usr/bin/facter' if x == 'cfacter' else '/opt/puppetlabs/bin/facter'
    facter = FacterFactCollector()
    # Facter binary should exist in '/opt/puppetlabs/bin'
    assert facter.find_facter(fake_module) == '/opt/puppetlabs/bin/facter'

    # Reset searchbin to ['/opt/puppetlabs/bin/cfacter']
    fake_module.get_

# Generated at 2022-06-13 02:00:01.402559
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils.facts.collector import resolve_collector_classes
    from ansible.module_utils._text import to_bytes

    test_classes = resolve_collector_classes(['*'])
    test_collector = get_collector_instance(test_classes)
    # Test with facter installed
    assert test_collector.get_facter_output({'get_bin_path': lambda path: path}) is not None
    # Test with facter not installed
    assert test_collector.get_facter_output({'get_bin_path': lambda path: None}) is None

# Generated at 2022-06-13 02:00:09.630359
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    class MockModule:
        def get_bin_path(self, *args, **kwargs):
            return "/bin/facter"

        def run_command(self, *args, **kwargs):
            return 0, '{"os":{"family":"RedHat","name":"CentOS","release":{"full":"7.1.1503","major":"7"}},"architecture":"x86_64"}', ""

    fake_module = MockModule()
    facter_fact_collector = FacterFactCollector()

    facter_output = facter_fact_collector.get_facter_output(fake_module)

    assert facter_output

# Generated at 2022-06-13 02:00:21.195170
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    import ansible.module_utils.facts.collector

    class DummyModule(object):
        def get_bin_path(self, binary, opt_dirs=[]):
            # TODO: parse and validate arguments
            # TODO: return an appropriate path. perhaps /bin/facter
            return '/usr/bin/facter'

        def run_command(self, command):
            # TODO: parse and validate arguments
            return 0, '{"facter_os": {"name": "DummyOS"}}', ''

    dummy_module = DummyModule()
    facter_fact_collector = ansible.module_utils.facts.collector.FacterFactCollector()

# Generated at 2022-06-13 02:00:28.983819
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.test_utils import TestModule
    import ansible.module_utils.facts.system.facter as facter_api

    class TestFacterFactCollector:
        def get_facter_output(self, module):
            # Mock return value of function get_facter_output
            return '{"facter_kernel": "Linux"}'

    module = TestModule()
    assert TestFacterFactCollector().get_facter_output(module) == '{"facter_kernel": "Linux"}'

# Generated at 2022-06-13 02:00:37.478120
# Unit test for method run_facter of class FacterFactCollector
def test_FacterFactCollector_run_facter():
    # Inject fake module with configurable return values of its methods
    mock_module = MockModule()
    test_collector = FacterFactCollector()
    test_collector.module = mock_module

    # No facter
    mock_module.run_command.return_value = (1, '', '')
    ret = test_collector.run_facter('', '')
    assert ret == (1, '', '')

    # Facter ok
    mock_module.run_command.return_value = (0, 'out', '')
    ret = test_collector.run_facter('', '')
    assert ret == (0, 'out', '')


# Generated at 2022-06-13 02:00:42.337851
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.collector import get_collector_instance

    module = get_collector_instance(FacterFactCollector)
    facter_path = module.find_facter(module)
    if facter_path is not None:
        return True

    return False


# Generated at 2022-06-13 02:00:52.177974
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    class Module:
        def __init__(self):
            self.bin_path_cache = {}

        def get_bin_path(self, executable, opt_dirs=[]):
            if executable == 'facter':
                return self.bin_path_cache['facter']
            if executable == 'cfacter':
                return self.bin_path_cache['cfacter']

    class FakeFacter:
        def __init__(self, path):
            self.path = path

    class FakeCfacter:
        def __init__(self, path):
            self.path = path

    def find_bin(executable):
        if executable == 'facter':
            return FakeFacter
        if executable == 'cfacter':
            return FakeCfacter


# Generated at 2022-06-13 02:01:01.086986
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    from ansible.module_utils.facts import module_reference
    from ansible.module_utils.facts.facts import with_module_reference
    from ansible.module_utils.facts.collector import get_collector_instance

    FORCE_COLLECTOR = {'facter': None, 'ohai': None, 'puppet': None, 'virtualenv': None, 'system': None}

    class ModuleReferenceForTesting(module_reference.ModuleReference):
        def __init__(self):
            self.real_module = None
            self.parameters = {
                'gather_subset': ['!all', 'min'],
                'gather_timeout': 10,
                'filter': '*'
            }
            self.extra_arguments = None
            self.check_mode = False

# Generated at 2022-06-13 02:01:09.381194
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    """ Unit test for method collect of class FacterFactCollector """

    class MockFacterModule:
        """ Mocked class for FacterFactCollector.collect """

        def get_bin_path(self, *path_info, **kwargs):
            """ Mocked method for get_bin_path """

            # Only path for facter is returned when facter is installed
            path_info = path_info[0]
            if path_info == 'facter':
                return '/opt/puppetlabs/bin/facter'
            elif path_info == 'cfacter':
                return None

            return None

        def run_command(self, *command, **kwargs):
            """ Mock method for run_command """

            # Command with the given path_info is executed only when
            # facter is installed

# Generated at 2022-06-13 02:01:19.318544
# Unit test for method run_facter of class FacterFactCollector
def test_FacterFactCollector_run_facter():
    import tempfile
    import shutil
    import os

    # Create a temporary directory
    tmpdir = tempfile.mkdtemp()

    facter = '''#!/bin/sh
echo '{"os":{"architecture":"x86_64","family":"Darwin","hardware":"","name":"MacOSX","release":{"build":"14C109","full":"14.4.0","major":"14","minor":"4"},"selinux":false},"osfamily":"Darwin","path":"/usr/bin:/bin:/usr/sbin:/sbin","kernel":"Darwin"}'
'''
    with open(os.path.join(tmpdir, "facter"), "wb") as f:
        f.write(facter)
    os.chmod(tmpdir + "/facter", 0o755)


# Generated at 2022-06-13 02:01:25.879443
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    class ModuleDummy():
        def __init__(self, run_rc, run_out, run_err, get_bin_path_rc):
            self._run_rc = run_rc
            self._run_out = run_out
            self._run_err = run_err
            self._get_bin_path_rc = get_bin_path_rc

        def get_bin_path(self, *args, **kwargs):
            return self._get_bin_path_rc

        def run_command(self, *args, **kwargs):
            return self._run_rc, self._run_out, self._run_err

    # Test a case where there is no facter command
    module = ModuleDummy(0, "", "", None)
    collector = FacterFactCollector()
    assert collector.get_

# Generated at 2022-06-13 02:01:32.707755
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    module = None
    facter_path = FacterFactCollector(module).find_facter(module)
    print(facter_path)



# Generated at 2022-06-13 02:01:43.238689
# Unit test for method get_facter_output of class FacterFactCollector

# Generated at 2022-06-13 02:01:51.263803
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    class MockModule():
        def get_bin_path(self, name, opt_dirs=[]):
            if name == 'cfacter':
                return '/opt/puppetlabs/bin/cfacter'
            elif name == 'facter':
                return '/usr/bin/facter'
            else:
                return None

    class FakeFacts():
        def __init__(self):
            self._facts = {}

    def make_mock_module():
        return MockModule()

    def make_fake_facts():
        return FakeFacts()

    # cfacter is present
    facter_collector = FacterFactCollector()
    facter_collector.find_facter(make_mock_module())

# Generated at 2022-06-13 02:01:57.847251
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    # fake module object
    class Options:
        def __init__(self):
            self.facter = True
    class AnsibleModule:
        def __init__(self):
            self.params = {}
            self.options = Options()
        def get_bin_path(self, something):
            return "facter"
        def run_command(self, facterpath):
            return 0, "{\"facter_blah\":\"blah\"}", ""
    amd = AnsibleModule()
    ff = FacterFactCollector()
    actual = ff.collect(amd)
    expected = {'facter_blah': 'blah'}
    assert(actual == expected)

# Generated at 2022-06-13 02:02:00.370358
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():

    from ansible.module_utils.facts import FacterFactCollector
    from ansible.module_utils import basic

    module_obj = basic.AnsibleModule(
        argument_spec = dict()
    )

    facter_path = FacterFactCollector().find_facter(module_obj)

    assert facter_path != None
    assert isinstance(facter_path, str)


# Generated at 2022-06-13 02:02:07.906434
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    import ansible.module_utils.facts.collectors.facter as facter_module
    import ansible.module_utils.facts.collectors.facter as facter_module

    facter = FacterFactCollector()
    module = facter_mock = facter_module.FacterModuleMock()
    facter_mock.run_command_results = (0, '{ "fact": "value" }', '')
    assert facter.get_facter_output(module) == '{ "fact": "value" }'

# Generated at 2022-06-13 02:02:16.369644
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    import ansible.module_utils.facts.collector
    class TestModule(object):
        def get_bin_path(self, name, opt_dirs=None):
            if name == 'facter':
                return '/opt/puppetlabs/bin/facter'
            return None
        def run_command(self, args):
            if args == '/opt/puppetlabs/bin/facter --puppet --json':
                return 0, '{}', ''
            return 1, '', ''
    facter = FacterFactCollector()
    result = facter.get_facter_output(TestModule())
    assert result == '{}'


# Generated at 2022-06-13 02:02:19.783036
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    class TestModule:
        def get_bin_path(self, arg1, arg2=None):
            return None

    collector = FacterFactCollector()
    facter_path = collector.find_facter(TestModule())

    assert facter_path is None

# Generated at 2022-06-13 02:02:27.368184
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    import subprocess
    import os
    class FakeModule(object):
        def __init__(self, **kwargs):
            self.params = kwargs

        def get_bin_path(self, path, opt_dirs):
            return 'facter'
        @staticmethod
        def run_command(cmd):
            return 0, '', ''
    class MockPopen:
        def __init__(self, *cmd, **kwargs):
            self.pid = 0
            self.returncode = 0
            self.stdout = subprocess.PIPE
            self.stderr = subprocess.PIPE

        def communicate(self):
            retval = dict()

# Generated at 2022-06-13 02:02:36.329031
# Unit test for method run_facter of class FacterFactCollector
def test_FacterFactCollector_run_facter():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector import Collector

    class TestModule:
        def get_bin_path(self, bin_path, opt_dir=None):
            if bin_path == 'facter':
                return '/usr/bin/facter'
            else:
                return None

        def run_command(self, bin_path):
            bin_path_list = bin_path.split()
            if bin_path_list[0] == '/usr/bin/facter':
                if '--json' in bin_path_list:
                    rc = 0
                    out = '{"kernel":"Linux"}'
                    err = ''
                else:
                    rc = 1
                    out = ''
                    err = 'Facter Error'

            return

# Generated at 2022-06-13 02:02:56.211156
# Unit test for method run_facter of class FacterFactCollector
def test_FacterFactCollector_run_facter():
    from ansible.module_utils.facts.collector import get_collector_instance

    facter = get_collector_instance('facter')
    assert facter
    assert isinstance(facter, FacterFactCollector)

    fake_module = FakeAnsibleModule()
    fake_facter_path = '/usr/bin/facter'

    # Exercise method run_facter() of class FacterFactCollector. We expect that the
    # fake_stdout and fake_stderr will be returned
    rc, out, err = facter.run_facter(fake_module, fake_facter_path)
    # FIXME: this test is worthless, since the module.run_command() method
    # will always return 0:
    #
    #   if rc != 0:
    #       raise Exception("%s failed

# Generated at 2022-06-13 02:03:06.863381
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    class MockModule:
        def get_bin_path(self, command, opt_dirs=[]):
            return '/usr/bin/facter'


# Generated at 2022-06-13 02:03:10.240232
# Unit test for method run_facter of class FacterFactCollector
def test_FacterFactCollector_run_facter():
    import sys
    import types

    sys.modules['ansible.module_utils.facts.collector'] = types.ModuleType('ansible.module_utils.facts.collector')

# Generated at 2022-06-13 02:03:11.439915
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    """test_FacterFactCollector_collect
    """
    pass

# Generated at 2022-06-13 02:03:21.917591
# Unit test for method run_facter of class FacterFactCollector
def test_FacterFactCollector_run_facter():
    import ansible.module_utils.facts.collector
    import ansible.module_utils.facts.namespace
    import ansible.module_utils.facts.utils

    class MockModule(object):
        def __init__(self):
            self.params = {
                '_ansible_checksum_version': 2,
                '_ansible_collection_name': 'test_collection',
                '_ansible_module_name': 'test_module'
            }
            self.args = {}
            self.version_info = { 'python': '2.7', 'python_version': '2.7' }
        def get_bin_path(self, executable, opt_dirs=()):
            return '/usr/bin/%s' % executable


# Generated at 2022-06-13 02:03:26.060849
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    class Module(object):
        def __init__(self, bin_paths):
            self._bin_paths = bin_paths

        def get_bin_path(self, executable, opt_dirs=[]):
            if executable in self._bin_paths:
                return self._bin_paths[executable]
            return None

        def run_command(self, command):
            if command in self._bin_paths:
                return 0, self._bin_paths[command]
            return -1, '', 'command not found'

    class BaseFactCollector(object):
        def __init__(self, collectors=None, namespace=None):
            self._collectors = collectors
            self.namespace = namespace


# Generated at 2022-06-13 02:03:32.424417
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    # Setup
    collector = FacterFactCollector(namespace=PrefixFactNamespace(namespace_name='facter', prefix='facter_'))
    module = MockModule()
    module.run_command = MockFunction(return_code=0, stdout='{"os":{"family":"Archlinux"},"system":{"uptime":{"days":0}}}')
    module.get_bin_path = MockFunction(return_value='/bin/facter')
    # Test
    facts = collector.collect(module=module)
    assert facts == {'facter_os': {'family': 'Archlinux'}, 'facter_system': {'uptime': {'days': 0}}}


# Generated at 2022-06-13 02:03:43.820319
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    import os
    import tempfile
    import shutil
    from ansible.module_utils.facts import ansible_collect
    from ansible.module_utils.facts.collector import get_collector_class

    # Create a fake facter module that outputs a valid json
    facter_json = dict(fact1='facter_value1', fact2=2, fact3=0.33, fact4=True)
    facter_json_str = json.dumps(facter_json)

# Generated at 2022-06-13 02:03:54.161143
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():

    # mock a module so we can control its behavior
    class _fake_module(object):

        def __init__(self):
            self.params = {
                'ansible_facter_collection': True,
            }
            self.facts = dict()

        def get_bin_path(self, name, opt_dirs=[]):
            # return the literal requested path
            return name

        def run_command(self, cmd):
            return 0, json.dumps({'fact_key': 'fact_value'}), ""
    fake_module = _fake_module()

    # initialize collector
    ffc = FacterFactCollector()

    # call collect method
    ffc.collect(module=fake_module)

    # verify what the method returns

# Generated at 2022-06-13 02:04:03.767826
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    # create some test data
    artifact_data=json.dumps({"facter": {"id": "root", "system32": "C:\\Windows\\system32"}}, sort_keys=True)
    artifact_file = open("/tmp/facter_fact.json","w")
    artifact_file.write(artifact_data)
    artifact_file.close()
    # create some mock module data for the test
    class MockModule(object):
        def __init__(self, params):
            self.params = params
            self.check_mode = False
        def get_bin_path(self, bin, opt_dirs=None):
            return '/tmp/facter_fact.json'

# Generated at 2022-06-13 02:04:32.207622
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    # test_module is a mock of AnsibleModule
    test_module = AnsibleModule(argument_spec={})

    # mock_find_facter is a mock of the method find_facter of class FacterFactCollector
    # mock_find_facter is a mock of the method find_facter of class FacterFactCollector
    # mock_find_facter has no side-effects and returns "facter"

# Generated at 2022-06-13 02:04:39.267527
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts.collector import get_collector_instance

    # create a mock module so we can test this
    # pretend facter is installed and works, so expect non-empty facter dict
    module = AnsibleModule()
    module.run_command = lambda x, **kwargs: (0, "{}", "")
    module.get_bin_path = lambda x, **kwargs: "/usr/bin/facter"

    facter = get_collector_instance(FacterFactCollector)
    facter_output = facter.get_facter_output(module)
    assert facter_output is not None

    # pretend facter is not installed
    module.get_bin_path = lambda x, **kwargs: None
    fact

# Generated at 2022-06-13 02:04:43.918143
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    # Create mock module object
    module = type('', (), {})()
    module.run_command = lambda x: (0, '{"operatingsystem":"CentOS"}', '')
    module.get_bin_path = lambda x: '/usr/local/bin/cfacter'

    # Create instance of FacterFactCollector class
    collector = FacterFactCollector()

    facter_output = collector.get_facter_output(module)

    print(json.loads(facter_output))

# Run if called as a script
if __name__ == '__main__':
    test_FacterFactCollector_get_facter_output()

# Generated at 2022-06-13 02:04:51.219274
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    class MockModule(object):
        def get_bin_path(self, path, opt_dirs=None):
            if path == 'facter':
                return '/opt/puppetlabs/bin/facter'
            return None

    module = MockModule()

    collector = FacterFactCollector(module=module)

    facter_path = collector.find_facter(module)
    assert facter_path == '/opt/puppetlabs/bin/facter'


# Generated at 2022-06-13 02:04:58.994762
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector import NamespaceConfig
    class TestCollector(BaseFactCollector):
        name = 'test'

        def collect(self, module=None, collected_facts=None):
            return 'hello world'

    class MockModule:
        def __init__(self):
            self.params = {}
        def get_bin_path(self, bin_name, opt_dirs=[]):
            return '/usr/bin/' + bin_name
        def run_command(self, args):
            return 0, '{"hello": "world"}', ''

    module = MockModule()

# Generated at 2022-06-13 02:05:09.431998
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    from ansible.module_utils.facts.collector import LocalHierarchyCollector
    from ansible.module_utils.facts.collector import get_collector_instance

    class MockModule:
        def __init__(self):
            self.paths = None

        def get_bin_path(self, binary, opt_dirs=None):
            if binary == 'facter':
                return '/usr/bin/facter'
            if binary == 'cfacter':
                return None
            return None

        def run_command(self, cmd):
            if cmd == '/usr/bin/facter --puppet --json':
                return 0, json.dumps({'a': 1, 'b': 2}), ''

# Generated at 2022-06-13 02:05:15.341519
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    m = {}
    m['run_command'] = lambda x: ('', '{ "os": { "family": "RedHat", "name": "CentOS", "release": { "full": "7.3.1611", "major": "7", "minor": "3" }, "selinux": { "enabled": true, "enforced": true, "policy_version": "28" } }, "puppetversion": "3.8.7", "augeas": { "version": "1.4.0", "lens_dir": "/opt/puppetlabs/puppet/share/augeas/lenses", "plugindir": "/opt/puppetlabs/puppet/lib/ruby/vendor_ruby/facter/augeas.rb/augeas" } }')
    m['get_bin_path']

# Generated at 2022-06-13 02:05:23.337277
# Unit test for method collect of class FacterFactCollector

# Generated at 2022-06-13 02:05:27.566928
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    '''
    Unit test to check method find_facter of class FacterFactCollector
    '''
    module = AnsibleModule(argument_spec={})
    ffc = FacterFactCollector(namespace='test')

    facts = module.ansible_facts
    facts['path'] = "/home/test/.ansible/tmp/ansible-tmp-1554720643.59-108260046001870/test/bin"
    module.ansible_facts = facts

    assert ffc.find_facter(module) == "/home/test/.ansible/tmp/ansible-tmp-1554720643.59-108260046001870/test/bin/facter"


# Generated at 2022-06-13 02:05:37.517639
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    class ModuleMock(object):
        def __init__(self, facter_path):
            self.facter_path = facter_path

        def get_bin_path(self, app, opt_dirs=None, required=False):
            if app == 'facter':
                return self.facter_path

            return None

    # Test with facter not installed
    module = ModuleMock(None)
    facter = FacterFactCollector()
    assert facter.find_facter(module) == None

    # Test with facter installed
    module = ModuleMock('/usr/bin/facter')
    facter = FacterFactCollector()
    assert facter.find_facter(module) == '/usr/bin/facter'

    # Install facter installed in opt_dirs

# Generated at 2022-06-13 02:06:29.942659
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    test_module = 'ansible.module_utils.facts.tests.sources.facter.facter_mock'
    test_fact_collector_class_name = 'FacterFactCollector'
    test_class_method = 'collect'
    test_spec = 'ansible.module_utils.facts.tests.facter_spec'

    helpers.run_unit_test_method_helper(test_class_method,
                                        test_module,
                                        test_fact_collector_class_name,
                                        test_spec)


# Generated at 2022-06-13 02:06:37.223671
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    # Init the Facter instance
    facter = FacterFactCollector()
    # Init the module mock
    module = AnsibleModuleMock()
    # Set module get_bin_path return value
    module.get_bin_path_return_value = "/foo/facter"
    # Call find_facter method
    facter_path = facter.find_facter(module)
    # Check that facter method has been called correctly
    module.get_bin_path.assert_called_once_with('facter', opt_dirs=['/opt/puppetlabs/bin'])
    # Check return value
    assert facter_path == "/foo/facter"


# Generated at 2022-06-13 02:06:47.749745
# Unit test for method run_facter of class FacterFactCollector
def test_FacterFactCollector_run_facter():
    import StringIO

    class FakeModule:
        def __init__(self):
            self.exit_json = dict()
            self.fail_json = dict()
            self.exit_args = None
            self.fail_args = None

        def exit_json(self, **kwargs):
            self.exit_args = kwargs

        def fail_json(self, **kwargs):
            self.fail_args = kwargs


# Generated at 2022-06-13 02:06:54.642760
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    from ansible.module_utils.facts.collector import get_collector_instance
    facter_collector = get_collector_instance(
        FacterFactCollector.name, FacterFactCollector)
    dummy_module = DummyModule({
        '/usr/bin/facter': '/usr/bin/facter',
        '/opt/puppetlabs/bin/facter': '/opt/puppetlabs/bin/facter',
        '/opt/puppetlabs/bin/cfacter': '/opt/puppetlabs/bin/cfacter',
    })
    assert facter_collector.find_facter(dummy_module) == '/opt/puppetlabs/bin/cfacter'


# Generated at 2022-06-13 02:06:59.637129
# Unit test for method run_facter of class FacterFactCollector
def test_FacterFactCollector_run_facter():
    # Given a FacterFactCollector object
    facter_collector = FacterFactCollector()
    # When we run the run_facter method
    result = facter_collector.run_facter('test', '/usr/bin/facter')
    # Then we should get a tuple with 0 as first element
    assert result[0] == 0


# Generated at 2022-06-13 02:07:07.200464
# Unit test for method run_facter of class FacterFactCollector
def test_FacterFactCollector_run_facter():
    import os
    import tempfile
    import ansible
    import ansible.module_utils

    my_module = ansible.module_utils.basic.AnsibleModule(
        argument_spec=dict()
    )

    # Make sure we have facter installed, before running this test
    try:
        os.environ['PATH'] = '{0}:{1}'.format(os.environ['PATH'],
                                              '/opt/puppetlabs/bin/')
        facter_path = my_module.get_bin_path('facter')
    except Exception as e:
        assert False, 'Failed to find facter binary: {0}'.format(str(e))

    # Create a fake facter file
    facter_file_handle, facter_file_path = tempfile.mkstemp()


# Generated at 2022-06-13 02:07:17.499475
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    module = ()

    m_find_facter = FacterFactCollector.find_facter
    m_run_facter = FacterFactCollector.run_facter
    def find_facter(self, module):
        m_find_facter(self, module)
        return '/opt/puppetlabs/bin/cfacter'

    def run_facter(self, module, facter_path):
        m_run_facter(self, module, facter_path)
        return 0, '{"blah": "foo"}', ''

    FacterFactCollector.find_facter = find_facter
    FacterFactCollector.run_facter = run_facter
    facter_output = FacterFactCollector().get_facter_output(module)

# Generated at 2022-06-13 02:07:27.626210
# Unit test for method run_facter of class FacterFactCollector
def test_FacterFactCollector_run_facter():
    class UUTModule(object):
        class FakeUUT(object):
            def __init__(self, module):
                self.module = module

            def run_command(self, cmd):
                return 0, '{ "some_fact": "some_value" }', ''

        def __init__(self):
            self.bin_path = self.FakeUUT(self)

    module = UUTModule()
    uut = FacterFactCollector()

    rc, out, err = uut.run_facter(module, '/bin/facter')
    assert rc == 0
    assert len(out) > 0
    assert err == ''

    rc, out, err = uut.run_facter(module, '/nonexistent/facter')
    assert rc == 1
    assert len(out) == 0

# Generated at 2022-06-13 02:07:35.328519
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    from collections import namedtuple
    from ansible.module_utils._text import to_bytes

    class FakeModule:
        def __init__(self, facter=None):
            self.facter = facter
            self.stdout = to_bytes("")
            self.stderr = to_bytes("")
            self.rc = 0

        def get_bin_path(self, bin_path, opt_dirs=None):
            return self.facter

        def run_command(self, cmd, environ_update=None, check_rc=False, cwd=None, data=None, binary_data=False):
            fake_result = namedtuple('Result', 'rc stdout stderr')
            return fake_result(self.rc, self.stdout, self.stderr)


# Generated at 2022-06-13 02:07:44.957071
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    mock_module = MockModule(paths=['/bin', '/sbin/', '/usr/bin', '/usr/sbin', '/usr/local/bin', '/usr/local/sbin', '/opt/puppetlabs/bin'])
    facter_collector = FacterFactCollector(module=mock_module)
    facter_path = facter_collector.find_facter(mock_module)
    assert facter_path is None

    mock_module = MockModule(paths=['/bin', '/sbin/', '/usr/bin', '/usr/sbin', '/usr/local/bin', '/usr/local/sbin', '/opt/puppetlabs/bin'], files=['/opt/puppetlabs/bin/facter'])