

# Generated at 2022-06-13 01:58:42.654844
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    assert FacterFactCollector().find_facter(module=None) is None



# Generated at 2022-06-13 01:58:54.192545
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    from ansible.module_utils.facts.system.facter import FacterFactCollector
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts._utils.collector import BaseFactCollector

    class FakeModule():
        def get_bin_path(self, executable, opt_dirs=None):
            return executable

        def run_command(self, cmd):
            return (0, '{"facter.test": "facter works!"}', '')

    fake_module = FakeModule()
    namespace = PrefixFactNamespace(namespace_name='facter', prefix='facter_')
    facter_fact_collector = FacterFactCollector(namespace=namespace)

# Generated at 2022-06-13 01:58:54.810704
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    pass

# Generated at 2022-06-13 01:59:06.712130
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    from ansible.module_utils.facts import ModuleInjector
    class MyFacterModule(ModuleInjector):
        def __init__(self, module_name=None, module_path=None,
                inject_facter=False, **kargs):
            super(MyFacterModule, self).__init__(module_name=module_name,
                    module_path=module_path, **kargs)
            self._inject_facter = inject_facter

        def get_bin_path(self, arg, **kwargs):
            facter_path = '/usr/bin/facter'
            if self._inject_facter:
                return facter_path
            else:
                return None


# Generated at 2022-06-13 01:59:17.086005
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    # First let's create an object out of FacterFactCollector class
    facter_fact_collector = FacterFactCollector()
    # Let's create a class that is representing a module
    class FakeModule:
        def get_bin_path(self, command, opt_dirs=[]):
            if command == 'facter':
                return "/usr/bin/facter"
            elif command == 'cfacter':
                return "/opt/puppetlabs/bin/cfacter"
            else:
                return None
    # Now let's create an object out of that class
    module = FakeModule()
    facter_path = facter_fact_collector.find_facter(module)
    # Let's use assertEqual to compare expected and actual output

# Generated at 2022-06-13 01:59:27.650540
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    def get_bin_path(self, executable, opt_dirs=[]):
        if executable == 'cfacter':
            return '/bin/cfacter'
        elif executable == 'facter':
            return '/usr/bin/facter'
        else:
            return ''

    def run_command(self, cmd, check_rc=True, close_fds=True):
        if cmd == '/bin/cfacter --puppet --json':
            return 0, json.dumps({'architecture': 'x86_64',
                                  'domain': 'na.example.com',
                                  'facterversion': '2.5.1'}), ''

# Generated at 2022-06-13 01:59:37.658767
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    import subprocess
    import os
    import sys

    # Patching module._AnsibleModule__init__
    # because _AnsibleModule__init__ of AnsibleModule is not public
    def mock__init__(self, argument_spec, bypass_checks=False, no_log=False, check_invalid_arguments=True,
                     mutually_exclusive=None, required_together=None, required_one_of=None, add_file_common_args=False,
                     supports_check_mode=False):
        pass

    class MockAnsibleModule(object):
        def __init__(self, *args, **kwargs):
            self.params = {}
            self.params['gather_subset'] = ['all']
            self.params['gather_timeout'] = 10
            # self.check_mode = False

# Generated at 2022-06-13 01:59:46.289035
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    """
    This function unit tests the method collect of the class FacterFactCollector. It first creates a
    mocked Ansible Module object and initializes the FacterFactCollector object. Then it calls its
    collect method. It compares the expected output with the output.
    """

    import unittest.mock as mock
    import json

    from ansible.module_utils.facts.collector import MemoryFactCollector
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector.facter import FacterFactCollector

    class MockModule(object):
        def __init__(self, params):
            self.params = params

        def run_command(self, arg):
            rc = 0

# Generated at 2022-06-13 01:59:55.431035
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    import tempfile
    import os
    import os.path

    # create a directory that looks like /opt/puppetlabs/bin
    dir1 = tempfile.mkdtemp(dir='/tmp', prefix='ansible_test_opt_puppetlabs_')
    dir2 = tempfile.mkdtemp(dir=dir1, prefix='bin_')
    # create a facter file within that directory
    facter_file = tempfile.NamedTemporaryFile(mode='w', prefix='facter_',
        suffix='_test', dir=dir2, delete=False, encoding='utf-8')
    facter_file.write('#!/usr/bin/env python\n')
    facter_file.flush()
    facter_file.close()

# Generated at 2022-06-13 02:00:03.235132
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    # Facts assignation
    facter_output = '{"ansible_facter1":"ansible_facter1-value"}'
    # Mock module instance
    module = MagicMock(name='AnsibleModule')
    # Mock method run_facter
    facter_collector = FacterFactCollector()
    facter_collector.run_facter = MagicMock(return_value=(0, facter_output, None))
    # Run test
    facts_dict = facter_collector.collect(module=module)
    # Assert correct result
    assert {"facter_facter1": "ansible_facter1-value"} == facts_dict


# Generated at 2022-06-13 02:00:11.178993
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():

    class MyModule(object):
        def get_bin_path(self, bin_path, opt_dirs=None):
            return '/usr/bin/' + bin_path

    module = MyModule()
    facter_path = FacterFactCollector(namespace='ansible_facts').find_facter(module)
    assert facter_path == '/usr/bin/cfacter'


# Generated at 2022-06-13 02:00:23.324391
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    from ansible.module_utils._text import to_bytes

    import mock
    import os
    import sys

    # Ensure that we get a version of mock on Python 2 and 3.
    try:
        import unittest.mock as mock
    except ImportError:
        pass

    # Since AnsibleModule isn't imported with import * in the module,
    # we use os.environ to set the environment
    os.environ['SHELL']='/bin/sh'
    os.environ['PATH']='/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
    os.environ['ANSIBLE_MODULE_ARGS']=json.dumps({})

    from ansible.module_utils.facts import ModuleableModule


# Generated at 2022-06-13 02:00:31.240382
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    """
    Test getting the output of facter
    :return:
    """

    import ansible.module_utils.facts.collector as collector

    # Mocks
    class module(object):

        fact_collectors = None
        fact_cache = None
        file_root = None
        config = None
        params = None
        tmpdir = None

        def __init__(self):
            self.params = {'gather_subset': 'all'}

        def get_bin_path(self, app, opt_dirs=None):
            return '/usr/bin/facter'

        def run_command(self, cmd):
            return 0, '{"ipaddress": "127.0.0.1"}', None

    fact_collector_obj = collector.FacterFactCollector()

    module_obj = module

# Generated at 2022-06-13 02:00:41.696700
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    import ansible.module_utils.facts.collector

    # Setup fake ansible module
    class FakeModule:
        def __init__(self):
            self.params = dict()

        def get_bin_path(self, path, opt_dirs=None, required=False):
            if path == 'cfacter':
                return '/opt/puppetlabs/bin/cfacter'
            return None

        def run_command(self, command):
            if command == '/opt/puppetlabs/bin/cfacter --puppet --json':
                return 0, '{ "ansible_uptime_seconds": "1337", "facterversion": "2.4.4" }', ''
            return 1, '', ''


# Generated at 2022-06-13 02:00:49.246891
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    facter_finder = FacterFactCollector()

    class MockModule:
        def get_bin_path(self, command, required=False, opt_dirs=[]):
            if command == 'cfacter':
                return '/opt/puppetlabs/bin/cfacter'
            elif command == 'facter':
                return '/usr/bin/facter'
            else:
                return None

    mock_module = MockModule()

    # Test that cfacter is preferred over facter
    assert facter_finder.find_facter(mock_module) == '/opt/puppetlabs/bin/cfacter'


# Generated at 2022-06-13 02:00:50.681937
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    assert FacterFactCollector().find_facter() == None

# Generated at 2022-06-13 02:00:52.856715
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    # test case execution
    collector = FacterFactCollector()
    module = None
    facter_path = collector.get_facter_output(module)

# Generated at 2022-06-13 02:00:59.093667
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    facter_path = '/opt/puppetlabs/bin/facter'

    class TestModule(object):
        def get_bin_path(self, bin, opt_dirs = []):
            return facter_path
        def run_command(self, facter_path):
            return 0, "{\"a\":1,\"b\":2}", ""

    collector = FacterFactCollector()
    assert collector.get_facter_output(TestModule()) == "{\"a\":1,\"b\":2}"

# Generated at 2022-06-13 02:01:02.399284
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    module = None
    collected_facts = {}

    ffc = FacterFactCollector()
    facter_dict = ffc.collect(module=module, collected_facts=collected_facts)
    assert isinstance(facter_dict, dict)
    assert len(facter_dict) > 0

# Generated at 2022-06-13 02:01:11.605410
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    import ansible
    import os
    testmodule = ansible.module_utils.facts.collector.Module(
        args=None,
        tmpdir=os.environ['TESTVARDIR'] + "/test-collectors",
        verbose=False,
        log_current_test="test_FacterFactCollector_get_facter_output",
        status_stdout_write=None,
        status_stderr_write=None,
        spec=None,
        exit_json=None
    )
    facterFactCollector = FacterFactCollector(collectors=None, namespace=None)
    FacterFactCollector.run_facter = lambda self, module, facter_path : (0, '{"fact1":"value1","fact2":"value2"}', '')
    result = facterFactCollect

# Generated at 2022-06-13 02:01:23.831540
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    from ansible.module_utils.facts import Collector
    from ansible.module_utils.facts.collector.system import SystemCollector
    from ansible.module_utils.facts.collector.facter import FacterFactCollector
    from ansible.module_utils.facts.collector.puppet import PuppetFactCollector
    from ansible.module_utils.facts.collector import ansible_collector

    collectors_list = [
        SystemCollector,
        PuppetFactCollector,
        FacterFactCollector
    ]

    # Create a non-ansible collector to test if find_facter works as intended.
    class NonAnsibleCollector(Collector):
        name = 'non_ansible'

        def __init__(self, module=None):
            self.module = module

    # Create a Collector that pret

# Generated at 2022-06-13 02:01:32.125983
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    import os
    import tempfile
    import shutil
    import sys
    import imp

    class TestModule:
        params = {}
        def __init__(self):
            self.params = {}
        def get_bin_path(self, arg1, opt_dirs=None):
            return os.path.join(self.params['bin_dir'], arg1)
        def run_command(self, arg1):
            return (self.params['rc'], self.params['stdout'], self.params['stderr'])

    # Create the temp dir
    tmpdir = tempfile.mkdtemp()
    print('Temp dir: {0}'.format(tmpdir))

    # Copy the current directory tree to a temp dir for this test

# Generated at 2022-06-13 02:01:37.893234
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    module = AnsibleModule(argument_spec={})

    ffc = FacterFactCollector()

    # we should find facter, on os's that have facter
    if module.which('facter'):
        facter_path = ffc.find_facter(module)
        assert facter_path == module.which('facter')


# a test module, with stubbed get_bin_path

# Generated at 2022-06-13 02:01:46.732760
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():

    class MockModule(object):
        def __init__(self):
            self.params = None

        def get_bin_path(self, executable, required=False, opt_dirs=[]):
            facter_path = '/usr/bin/facter'
            return facter_path

        def run_command(self, command):
            if self.params:
                return self.params.get('rc'), self.params.get('out'), self.params.get('err')
            else:
                return 0, '{"ansible_lsb":{"distcodename":"stretch","distdescription":"Debian GNU/Linux 9.5 (stretch)","distid":"Debian","distrelease":"9.5","majdistrelease":"9"}}', ''


# Generated at 2022-06-13 02:01:51.666446
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    from ansible.module_utils.facts import ansible_fact_cache
    from ansible.module_utils.basic import AnsibleModule
    
    module = AnsibleModule({})
    facter_facts = FacterFactCollector()
    ansible_fact_cache['facter'] = facter_facts.get_facter_output(module)
    
    assert 'facter' in ansible_fact_cache.keys()

# Generated at 2022-06-13 02:01:57.681587
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    module = MockModule()
    module.get_bin_path = mock.Mock(side_effect=lambda x: x)
    # Paths to facter present
    assert FacterFactCollector().find_facter(module) == 'facter'
    # Paths to cfacter present
    assert FacterFactCollector().find_facter(module) == 'cfacter'
    # Paths to facter and cfacter not present
    module.get_bin_path = mock.Mock(return_value=None)
    assert FacterFactCollector().find_facter(module) is None


# Generated at 2022-06-13 02:02:02.032307
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():

    class Module(object):
        def __init__(self, facter_path=None, cfacter_path=None, run_command=None):
            self.facter_path = facter_path
            self.cfacter_path = cfacter_path
            self.run_command = run_command

        def get_bin_path(self, *args, **kwargs):
            if self.facter_path:
                return self.facter_path
            if self.cfacter_path:
                return self.cfacter_path

            return None

    def run_command_mock(self, facter_path):
        if facter_path == '/usr/bin/facter --puppet --json':
            return 0, '{"kernel": "Linux"}', ''

# Generated at 2022-06-13 02:02:06.794040
# Unit test for method run_facter of class FacterFactCollector
def test_FacterFactCollector_run_facter():
    facter_path = '/usr/bin/facter'
    module = AnsibleModule()

    ffc = FacterFactCollector()
    rc, out, err = ffc.run_facter(module, facter_path)
    assert rc == 0
    assert out != ''
    assert err == ''

# Generated at 2022-06-13 02:02:16.380898
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    module = None
    facter_dict = {}

    facter_output = '''
    {
        "facter_cmdline": {
            "value": [
                "foo=bar"
            ]
        },
        "facter_cmdline_foo": {
            "value": "bar"
        },
        "facter_cmdline_nofoo": {
            "value": null
        },
        "facter_cmdline_nofoo_bar": {
            "value": null
        }
    }
    '''

    fact_collector = FacterFactCollector()
    facter_dict = fact_collector.collect(module, facter_dict)

    assert facter_dict['facter_cmdline'] == facter_output

# Generated at 2022-06-13 02:02:25.159217
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    """Test collect method of FacterFactCollector."""
    # Using "retrieve" method of fact_module (AnsibleModule) as mock
    from ansible.module_utils.facts import fact_module
    fact_module.retrieve = lambda *args: None

    # Mocking method find_facter in order to avoid real execution of facter
    facter_path = '/some/path/facter-2.4.6/bin/facter'
    collector = FacterFactCollector()
    collector.find_facter = lambda *args: facter_path

    # Mocking method run_facter in order to avoid real execution of facter

# Generated at 2022-06-13 02:02:40.354106
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():

    # Import Ansible module_utils
    import ansible.module_utils.facts.collector

    # Make a mock AnsibleModule
    class MockAnsibleModule():

        def __init__(self):
            self.params = {}

        def fail_json (self, *args, **kwargs):
            self.exit_args = args
            self.exit_kwargs = kwargs
            raise Exception('fail_json')

        def get_bin_path(self, *args, **kwargs):
            return '/bin/facter'


# Generated at 2022-06-13 02:02:51.583969
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    facter_dict = PrefixFactNamespace(namespace_name='facter', prefix='facter_')
    f = FacterFactCollector(namespace=facter_dict)
    class mock_module:
        def __init__(self):
            return None

        def get_bin_path(self, bin_path, opt_dirs=None):
            return "/usr/bin/facter"


# Generated at 2022-06-13 02:02:58.887175
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    class FakeModule:
        class FakeModuleError(Exception):
            pass

        def __init__(self):
            self.module_args = dict() # not used
            self.params = dict() # not used
            self.facts = dict() # not used
            self.fail_json = self.FakeModuleError
            self.run_command_rc = 0
            self.run_command_result = dict() # key: command, value: (rc, out, err)
            self.get_bin_path_result = dict() # key: bin, value: path or None
            if len(self.run_command_result) == 0:
                self.run_command_result['facter --puppet --json'] = (0, '{"facter_kernel":"Linux","facter_ipaddress":"10.0.0.1"}', '')

# Generated at 2022-06-13 02:03:09.208026
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    # Creating instance of FacterFactCollector
    facter_fact_collector = FacterFactCollector()

    # Creating a mock class (an instance of AnsibleModule) with its attributes
    class TestAnsibleModule(object):
        def __init__(self):
            self.params = {}

        def get_bin_path(self, name, opt_dirs=[]):
            if name == "facter":
                return "/bin/dir/facter"
            return None

# Generated at 2022-06-13 02:03:19.517048
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    f = FacterFactCollector()

    # Test with bad json data
    class TestModule:
        def run_command(self):
            return 0, '{bad_json', ''
        def get_bin_path(self, *args, **kwargs):
            return '/usr/bin/facter'
    assert f.collect(TestModule()) == {}
    assert f.collect() == {}

    # Test with good json data
    class TestModule2:
        def run_command(self):
            return 0, '{"operatingsystem": "Ubuntu", "uptime_days": "6"}', ''
        def get_bin_path(self, *args, **kwargs):
            return '/usr/bin/facter'

# Generated at 2022-06-13 02:03:29.939669
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    class Module(object):
        def get_bin_path(self, executable, opt_dirs=None):
            return '/usr/bin/facter'


# Generated at 2022-06-13 02:03:41.222397
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    class FakeModule(object):
        def get_bin_path(self, exe, opt_dirs):
            return '/usr/local/bin/facter'


# Generated at 2022-06-13 02:03:49.637198
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    # Test the method get_facter_output of class FacterFactCollector with a valid output
    # of the execution of command 'facter'
    def mocked_run_command(self, cmd):
        return 0,'mocked valid output', ''
    facter_fact_collector = FacterFactCollector(None, None)

    facter_fact_collector.run_command = mocked_run_command
    fixture_facter_path = 'path/to/facter'
    assert facter_fact_collector.get_facter_output(facter_path=fixture_facter_path) == 'mocked valid output'

    # Test the method get_facter_output of class FacterFactCollector with a invalid output
    # of the execution of command 'facter'

# Generated at 2022-06-13 02:03:57.388126
# Unit test for method run_facter of class FacterFactCollector
def test_FacterFactCollector_run_facter():

    try:
        import mock
    except ImportError:
        raise SkipTest("mock python library not installed")

    class MockModule(object):

        def __init__(self, rc, out, err):
            self.rc = rc
            self.out = out
            self.err = err

        def get_bin_path(self, name, opt_dirs=None):
            return '/bin/' + name

        def run_command(self, cmd):
            return (self.rc, self.out, self.err)

    # passing test case
    mock_module = MockModule(0, '{"hostname": "ansible-test", "fqdn": "ansible-test.example.com"}\n', '')
    facter_fact_collector = FacterFactCollector()
    facter_path = facter

# Generated at 2022-06-13 02:04:01.239852
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    import ansible.module_utils.facts.namespace
    module = ansible.module_utils.facts.namespace.BaseModule()
    collector = FacterFactCollector()
    facter_path = collector.find_facter(module)
    assert facter_path

# Test for method get_facter_output of class FacterFactCollector

# Generated at 2022-06-13 02:04:30.222939
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    class MockModule:
        def __init__(self, facter_path):
            self.facter_path = facter_path
            self.facter_bin_path = None

        def get_bin_path(self, name, opt_dirs=None, required=False):
            self.facter_bin_path = name
            return self.facter_path

    class MockFacterFactCollector(FacterFactCollector):
        def __init__(self, collectors=None, namespace=None):
            super(MockFacterFactCollector, self).__init__(collectors=collectors,
                                                          namespace=namespace)

        def find_facter(self, module):
            return super(MockFacterFactCollector, self).find_facter(module)

    collector = MockFacterFactCollect

# Generated at 2022-06-13 02:04:35.223451
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    import tempfile

    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    class FakeModule(object):
        def __init__(self):
            self.params = {}

        def get_bin_path(self, name, opt_dirs=[]):
            if name == 'facter':
                return '/usr/bin/facter'
            elif name == 'cfacter':
                return None

    facter = FacterFactCollector(namespace=PrefixFactNamespace(prefix='facter_'))
    facts = facter.collect(module=FakeModule())

    assert 'facter_processor0' in facts



# Generated at 2022-06-13 02:04:44.279089
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    class FakeModule():
        def run_command(self, cmd):
            return 0, '{"a": 1, "b": 2, "c": "3"}', ''

        def get_bin_path(self, *args, **kwargs):
            return '/usr/bin/facter'

    ffc = FacterFactCollector()
    module = FakeModule()
    output = ffc.get_facter_output(module)
    assert output == '{"a": 1, "b": 2, "c": "3"}'

    del module.run_command
    module.run_command = lambda cmd: (1, '', '')
    assert ffc.get_facter_output(module) is None

    del module.run_command
    module.run_command = lambda cmd: (1, None, None)
    assert f

# Generated at 2022-06-13 02:04:54.667906
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    import platform
    # Can NOT be tested in Windows environment
    if platform.system() == 'Windows':
        return

    from ansible.module_utils.facts import collector

    # Use a custom module which looks into /tmp/ansible_python_facts
    from ansible.module_utils.facts.test_module import TestModule

    # test find_facter in case of facter installed
    from tempfile import mkdtemp
    from shutil import rmtree
    from os import makedirs
    from os import sep
    from os.path import join

    # Create a tmp dir to work
    tmp_path = mkdtemp()

    # Create a tmp facter dir
    facter_path = join(tmp_path, 'facter')
    makedirs(facter_path)

    # Create a facter bin file
    fact

# Generated at 2022-06-13 02:04:58.590219
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    from ansible.module_utils.facts.namespace import FactsNamespace
    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils.facts.collector import get_collectors_for_namespace
    from ansible.module_utils.facts.collector import get_namespace_info
    from ansible.module_utils.facts.collector import get_namespace_data
    from ansible.module_utils.facts.collector import get_fact_namespace_data

    collector_instance = get_collector_instance(FacterFactCollector)
    assert collector_instance is not None
    assert isinstance(collector_instance, FacterFactCollector)

# Generated at 2022-06-13 02:05:09.061619
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    import os
    import tempfile
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts import module_utils

    bfc_facter = FacterFactCollector()

    class TestModule(object):
        def __init__(self):
            self.params = {'_ansible_version': "2.0.0.2"}

        def get_bin_path(self, prog, opt_dirs=[]):
            if prog == 'facter':
                if os.path.exists('/opt/puppetlabs/bin/facter'):
                    return '/opt/puppetlabs/bin/facter'
                else:
                    return '/usr/bin/facter'

# Generated at 2022-06-13 02:05:14.871594
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    import sys
    # Python 3.6
    if sys.version_info >= (3, 6):
        import unittest.mock as mock
    # Python 3.5
    else:
        import mock

    m_module = mock.MagicMock()
    m_rc = mock.MagicMock()
    m_command = mock.MagicMock()
    m_run_command = mock.MagicMock()

    # run_facter returns 0 with json facts
    m_run_command.return_value = 0, '{"kernel":"Linux"}', ''
    facter_dict = {'kernel': 'Linux'}

    m_module.get_bin_path.return_value = '/usr/bin/facter'

    collector = FacterFactCollector()
    result = collector.collect(m_module)

    assert fact

# Generated at 2022-06-13 02:05:17.116020
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    # fixture
    ffc = FacterFactCollector()

    # test
    assert ffc.find_facter(None) == None

# Generated at 2022-06-13 02:05:24.987192
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    # Create a mock module to use with the method find_facter
    class MockModule(object):
        def __init__(self, module_paths):
            self.module_paths = module_paths

        def get_bin_path(self, name, opt_dirs=None):
            return self.module_paths.get(name, None)

    # Unit test for default case
    module_paths = {}
    module = MockModule(module_paths)
    facter_collector = FacterFactCollector()
    result = facter_collector.find_facter(module)
    assert result is None

    # Unit test for cfacter case
    module_paths = {"cfacter": "/opt/puppetlabs/bin/cfacter"}
    module = MockModule(module_paths)
    fact

# Generated at 2022-06-13 02:05:35.558937
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    facter_output = b'{"values":{"architecture":"amd64","augeasversion":"1.4.0","selinux":"false"},"timestamp":"2016-12-14 16:17:38 +0000","environment":"production"}'
    facter_dict = json.loads(facter_output)
    module = MockModule()
    facter_path = module.get_bin_path('facter', opt_dirs=['/opt/puppetlabs/bin'])
    rc, out, err = module.run_command(facter_path + " --puppet --json")
    facter_collector = FacterFactCollector()
    assert facter_collector.get_facter_output(module) == facter_output

# Generated at 2022-06-13 02:06:26.744354
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    # pylint: disable=import-error
    import ansible.module_utils.facts.collector
    modules = {'find_facter': lambda module: '/usr/bin/cfacter',
               'run_command': lambda facter_path: (0, '{"a": "b"}', '')}
    fact_collector = FacterFactCollector()
    # pylint: disable=no-member
    fact_collector.__dict__.update(modules)
    facter_output = fact_collector.get_facter_output(None)
    assert json.loads(facter_output) == {"a": "b"}

# Generated at 2022-06-13 02:06:32.007500
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    # test case 1
    module = mock_module()
    module.binary_exists.side_effect = lambda path: path == '/opt/puppetlabs/bin/facter'
    collector = FacterFactCollector()
    assert collector.find_facter(module) == "/opt/puppetlabs/bin/facter"

    # test case 2
    module = mock_module()
    module.binary_exists.side_effect = lambda path: path == '/opt/puppetlabs/bin/cfacter'
    collector = FacterFactCollector()
    assert collector.find_facter(module) == "/opt/puppetlabs/bin/cfacter"

    # test case 3
    module = mock_module()

# Generated at 2022-06-13 02:06:41.622972
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector import get_collector_instance

    class MyTestModule(object):
        def __init__(self):
            self.facter = None

        def get_bin_path(self, name, path=None, opt_dirs=[]):
            if name == 'facter' and self.facter:
                return self.facter
            return None

    class CollectorModule(BaseFactCollector):
        name = 'test_collector'
        _fact_ids = set()


# Generated at 2022-06-13 02:06:50.758733
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    from ansible.module_utils.facts.utils import ModuleUtils
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts import collector
    import os
    import tempfile

    # create test directories
    tmpdir = tempfile.mkdtemp()
    tmpdir1 = os.path.join(tmpdir, 'bin')
    os.mkdir(tmpdir1)
    tmpdir2 = os.path.join(tmpdir, 'sbin')
    os.mkdir(tmpdir2)
    tmpdir3 = os.path.join(tmpdir, 'opt', 'puppetlabs', 'bin')
    os.makedirs(tmpdir3)

    # create test scripts
    facter_script = os.path.join(tmpdir1, 'facter')

# Generated at 2022-06-13 02:06:52.380804
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    facter_path = FacterFactCollector().find_facter('invalid')
    assert facter_path is None

# Generated at 2022-06-13 02:07:01.195705
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    class module(object):
        def __init__(self, find_bin_path_result):
            self.find_bin_path_result = find_bin_path_result
            self.run_command_return_value = (1, "", "")

        def get_bin_path(self, name, opt_dirs=[]):
            return self.find_bin_path_result

        def run_command(self, command):
            return self.run_command_return_value

    # No facter, no facter_output
    ffc = FacterFactCollector()
    ffc.find_facter = lambda m: None

    assert ffc.collect(module=module(None)) == {}

    # No cfacter, facter with no JSON output, no facter_output
    ffc = FacterFactCollector()

# Generated at 2022-06-13 02:07:08.438585
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():

    # Create the object FacterFactCollector
    facter = FacterFactCollector()

    # Unit test: collect - no facter installed
    class ModuleMock:
        def get_bin_path(self, name, opt_dirs=None):
            return None
    module = ModuleMock()
    assert facter.collect(module) == {}

    # Unit test: collect - facter installed, but no json output
    def get_bin_path(self, name, opt_dirs=None):
        '''Mock method which return the path for facter'''
        return 'facter'
    module.get_bin_path = get_bin_path

    def run_command(self, cmd):
        '''Mock method for run_command'''
        return 1, '...', '...'
    module.run_

# Generated at 2022-06-13 02:07:14.285053
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    module = mock.MagicMock()
    some_path = '/some/path'
    module.get_bin_path.return_value = some_path # mock return value of module.get_bin_path
    collector = FacterFactCollector()

    assert collector.find_facter(module) == some_path # check if collector.find_facter calls module.get_bin_path with the correct argument



# Generated at 2022-06-13 02:07:21.071305
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():

    from ansible.module_utils.facts.collector import MockModule
    from ansible.module_utils.facts.collector import MockSubprocess
    from ansible.module_utils.facts.collector import MockAnsibleModule

    module = MockModule()
    module.run_command = MockSubprocess.run_command
    ansible_module = MockAnsibleModule()
    ansible_module.get_bin_path = MockAnsibleModule.get_bin_path

    facter_path = FacterFactCollector().find_facter(ansible_module)
    assert facter_path

    facter_path = FacterFactCollector().find_facter(module)
    assert facter_path is None



# Generated at 2022-06-13 02:07:29.372952
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    ff = FacterFactCollector()
    class MockModule(object):
        def get_bin_path(self, arg, opt_dirs=[]):
            return '/usr/bin/{}'.format(arg) if '{}'.format(arg) in ['facter', 'cfacter'] else None

    class MockModule1(object):
        def get_bin_path(self, arg, opt_dirs=[]):
            return '/usr/bin/{}'.format(arg) if '{}'.format(arg) in ['cfacter', 'facter'] else None
    assert ff.find_facter(MockModule()) == '/usr/bin/facter'
    assert ff.find_facter(MockModule1()) == '/usr/bin/cfacter'