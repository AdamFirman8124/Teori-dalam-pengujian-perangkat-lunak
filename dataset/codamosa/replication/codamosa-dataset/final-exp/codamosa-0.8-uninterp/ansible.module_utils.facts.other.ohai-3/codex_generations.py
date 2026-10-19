

# Generated at 2022-06-13 01:58:47.895080
# Unit test for method run_ohai of class OhaiFactCollector
def test_OhaiFactCollector_run_ohai():
    from ansible.module_utils.basic import AnsibleModule
    a = AnsibleModule()
    x = OhaiFactCollector()

    x.run_ohai(a, '/opt/chef/bin/ohai')

    assert x is not None

# Generated at 2022-06-13 01:58:56.552445
# Unit test for method find_ohai of class OhaiFactCollector
def test_OhaiFactCollector_find_ohai():
    from ansible.module_utils.facts.ohai import OhaiFactCollector
    import os
    import tempfile

    ohai_names = ['testohai_0', 'testohai_1']

    # Generate a binary file to be used as ohai
    tmp = tempfile.NamedTemporaryFile(prefix='testohai', suffix='.sh',
                                      delete=False)
    tmp.write('''#!/bin/sh
echo '{"ohai": {"id": "test"}}'
''')
    tmp.close()
    os.chmod(tmp.name, 0o755)

    # Collect facts without a mock module
    facts = OhaiFactCollector().collect()
    assert facts == {}

    # Mock module to force ohai paths

# Generated at 2022-06-13 01:59:03.980784
# Unit test for method collect of class OhaiFactCollector
def test_OhaiFactCollector_collect():
    import ansible.module_utils.facts.collector
    ohai_fact_collector = ansible.module_utils.facts.collector.get_collector('ohai')
    assert ohai_fact_collector
    assert isinstance(ohai_fact_collector, OhaiFactCollector)
    assert ohai_fact_collector.name == 'ohai'
    assert ohai_fact_collector.collect() is None

# Generated at 2022-06-13 01:59:11.855466
# Unit test for method get_ohai_output of class OhaiFactCollector
def test_OhaiFactCollector_get_ohai_output():
    from ansible.module_utils.basic import AnsibleModule

    ohai_path = '/usr/bin/ohai'
    ohai_rc = 0
    ohai_stdout = json.dumps({'ohai': 'facts'})
    ohai_stderr = ''

    module = AnsibleModule(argument_spec={})
    ohai_output = OhaiFactCollector().get_ohai_output(module)
    assert ohai_output is None

    module.run_command = lambda command: (ohai_rc, ohai_stdout, ohai_stderr)
    module.get_bin_path = lambda command: ohai_path

    ohai_output = OhaiFactCollector().get_ohai_output(module)
    assert ohai_output == ohai_stdout

# Generated at 2022-06-13 01:59:16.724632
# Unit test for method collect of class OhaiFactCollector
def test_OhaiFactCollector_collect():

    class ModuleMock:

        def get_bin_path(self, arg):
            return '/usr/bin/%s' % arg

        def run_command(self, arg):
            return 0, '{"a": "b"}', ''

    module = ModuleMock()
    collector = OhaiFactCollector()

    v = collector.collect(module=module)

    assert v == {'a': 'b'}


# Generated at 2022-06-13 01:59:23.837902
# Unit test for method run_ohai of class OhaiFactCollector
def test_OhaiFactCollector_run_ohai():
    # For more information on testing facts please see
    # test/unit/ansible_test/_data/ansible_local.
    ohai_fact_collector = OhaiFactCollector()
    test_runner = TestRunner()
    test_runner.add_task(name='collect',
                         task_fixture=ohai_fact_collector,
                         mock_name='run_ohai',
                         response_fixture=None)
    test_runner.run()


# Generated at 2022-06-13 01:59:25.544395
# Unit test for method collect of class OhaiFactCollector
def test_OhaiFactCollector_collect():
    module = {}
    ohai_facts = OhaiFactCollector().collect(module)
    assert(ohai_facts)

# Generated at 2022-06-13 01:59:32.697352
# Unit test for method get_ohai_output of class OhaiFactCollector
def test_OhaiFactCollector_get_ohai_output():
    # Python 3.5+
    from unittest.mock import MagicMock, patch
    import module_utils.facts.collector
    # Python 2.7
    # from mock import MagicMock, patch
    # import ansible.module_utils.facts.collector as module_utils.facts.collector

    ohai_collector = OhaiFactCollector()

    fake_module = MagicMock()
    fake_module.get_bin_path.return_value = '/bin/ohai'
    fake_run_command_success = (0, '{"os":"Darwin"}', '')
    fake_run_command_failure = (1, '', '')
    fake_module.run_command.return_value = fake_run_command_success

    module_utils.facts.collector.which = MagicMock

# Generated at 2022-06-13 01:59:36.787885
# Unit test for method collect of class OhaiFactCollector
def test_OhaiFactCollector_collect():
    module = MockModule()
    ohai_collector = OhaiFactCollector()
    ohai_facts = ohai_collector.collect(module=module)
    assert isinstance(ohai_facts, dict)
    assert ohai_facts['ohai_uptime'] == '1'


# Generated at 2022-06-13 01:59:45.775946
# Unit test for method run_ohai of class OhaiFactCollector
def test_OhaiFactCollector_run_ohai():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    class TestFactCollector(BaseFactCollector):
        '''Test fact collector that creates a new namespace'''
        name = 'test'

        def __init__(self, collectors=None, namespace=None):
            super(TestFactCollector, self).__init__(collectors=collectors,
                                                    namespace=namespace)

    test_fact_collector = TestFactCollector(namespace=PrefixFactNamespace(namespace_name='test',
                                                                          prefix='test_'))

    class TestModule:
        '''Test module for testing method run_ohai of class OhaiFactCollector'''

# Generated at 2022-06-13 01:59:59.705185
# Unit test for method collect of class OhaiFactCollector
def test_OhaiFactCollector_collect():
    ohai_facts_data = '{"fqdn":"foo.example.org","ipaddress":"1.2.3.4"}'
    data_in = {'ansible_facts': {}}
    def fake_run_command_rc0(args, check_rc=True, close_fds=True, cwd=None, data=None, executable=None,
                             stdin=None, stdin_add_newline=True, strip_empty_ends=True, use_unsafe_shell=False,
                             environ_update=None, log_errors=True, encoding=None, errors=None, binary_data=False):
        return 0, ohai_facts_data, None


# Generated at 2022-06-13 02:00:02.276947
# Unit test for method find_ohai of class OhaiFactCollector
def test_OhaiFactCollector_find_ohai():

    from ansible.module_utils.facts.collector.ohai import OhaiFactCollector as OFC

    ofc = OFC()
    assert ofc.find_ohai('mock_object') is None

# Generated at 2022-06-13 02:00:12.782754
# Unit test for method get_ohai_output of class OhaiFactCollector
def test_OhaiFactCollector_get_ohai_output():
    import ansible.module_utils.facts.collector
    try:
        from unittest.mock import MagicMock
    except ImportError:
        from mock import MagicMock

    module = ansible.module_utils.facts.collector.BaseFactCollector()
    module.get_bin_path = MagicMock(return_value='/usr/bin/ohai')
    module.run_command = MagicMock(return_value=(0, 'test out', 'test err'))

    ohai_fc = ansible.module_utils.facts.ohai.OhaiFactCollector(module=module)
    assert ohai_fc.get_ohai_output(module) == 'test out'

# Generated at 2022-06-13 02:00:15.542589
# Unit test for method get_ohai_output of class OhaiFactCollector
def test_OhaiFactCollector_get_ohai_output():
    collector = OhaiFactCollector()
    ohai_output = collector.get_ohai_output(module)
    assert ohai_output is not None


# Generated at 2022-06-13 02:00:27.065822
# Unit test for method run_ohai of class OhaiFactCollector
def test_OhaiFactCollector_run_ohai():
    """
    This method is used to test the run_ohai method of class OhaiFactCollector.
    """
    from ansible.module_utils.facts.collector import get_collector_instance

    # Get an instance of the DummyAnsibleModule
    from ansible.module_utils.facts.test.dummy_ansible_module import DummyAnsibleModule
    module = DummyAnsibleModule()

    # Get an instance of the OhaiFactCollector
    ohai_collector = get_collector_instance(OhaiFactCollector)

    # Check that the run_ohai method of the OhaiFactCollector exits correctly
    assert ohai_collector.run_ohai(module, '/usr/bin/ohai')[0] == 0


# Generated at 2022-06-13 02:00:27.979286
# Unit test for method get_ohai_output of class OhaiFactCollector
def test_OhaiFactCollector_get_ohai_output():
    assert False, "FIXME"

# Generated at 2022-06-13 02:00:38.567412
# Unit test for method collect of class OhaiFactCollector
def test_OhaiFactCollector_collect():
    import os
    import json
    import sys
    import subprocess
    import tempfile
    import ansible.module_utils.facts.system.ohai as ohai_utils

    CMD = """#!/bin/sh
    echo '{"foo": "bar"}'
    """

    try:
        tmp = tempfile.NamedTemporaryFile()
        script_path = tmp.name
        tmp.write(CMD)
        tmp.flush()
        os.chmod(script_path, 0o755)
    except Exception as e:
        print("Temporary file creation failed - error code: %d (%s)" % (e.errno, e.strerror))
        sys.exit(1)

    def find_ohai_mock(self):
        return script_path

    facts_collector = ohai_utils

# Generated at 2022-06-13 02:00:41.857742
# Unit test for method get_ohai_output of class OhaiFactCollector
def test_OhaiFactCollector_get_ohai_output():
    import ansible.module_utils.facts.collector
    mod = ansible.module_utils.facts.collector.get_module(None)
    a = OhaiFactCollector()
    assert a.get_ohai_output(mod) is not None

# Generated at 2022-06-13 02:00:48.099243
# Unit test for method get_ohai_output of class OhaiFactCollector
def test_OhaiFactCollector_get_ohai_output():
    from ansible.module_utils.facts import ModuleFacts

    module = ModuleFacts(
        '',
        '',
        {},
        {},
        '',
        '',
        '',
        ''
    )

    module.get_bin_path = lambda x: '/bin/ohai'
    module.run_command = lambda x: (0, '{ "a": "foo" }', '')

    ohai = OhaiFactCollector()
    ohai_output = ohai.get_ohai_output(module)
    assert ohai_output is not None
    assert ohai_output == '{ "a": "foo" }'


# Generated at 2022-06-13 02:00:58.816528
# Unit test for method collect of class OhaiFactCollector
def test_OhaiFactCollector_collect():
    m = MockModule()
    m.get_bin_path = Mock(name='get_bin_path')
    m.run_command = Mock(name='run_command')

# Generated at 2022-06-13 02:01:10.808624
# Unit test for method run_ohai of class OhaiFactCollector
def test_OhaiFactCollector_run_ohai():
    import ansible.module_utils.facts.collector
    import ansible.module_utils.basic
    import tempfile
    import os

    # Create temporary file to use as fake ohai executable
    ohai_dir = tempfile.mkdtemp()
    ohai_path = os.path.join(ohai_dir, "ohai")
    os.mkdir(ohai_path)

    # Create fake ohai executable which just prints the required output
    binfile = open(os.path.join(ohai_path, "ohai"), "w")
    expected_data = {"platform": "Linux", "kernel": {"release": "3.16.0-4-amd64"}}
    binfile.write("#!/bin/bash\n")

# Generated at 2022-06-13 02:01:16.618906
# Unit test for method find_ohai of class OhaiFactCollector
def test_OhaiFactCollector_find_ohai():
    import ansible.module_utils.facts.collector
    import ansible.modules.system.setup
    ohai = ansible.module_utils.facts.collector.OhaiFactCollector()
    mod = ansible.modules.system.setup.SetupModule()
    mod.params = {}
    ohai_path = ohai.find_ohai(mod)
    assert ohai_path is not None

# Generated at 2022-06-13 02:01:20.437268
# Unit test for method collect of class OhaiFactCollector
def test_OhaiFactCollector_collect():
    from ansible.module_utils.facts import FactCollector

    facts_collector = FactCollector()
    ohai_fact_collector = OhaiFactCollector(collectors=[facts_collector])

    ohai_facts = ohai_fact_collector.collect()
    assert 'ohai_kernel' in ohai_facts
    assert 'ohai_platform' in ohai_facts

# Generated at 2022-06-13 02:01:29.744272
# Unit test for method run_ohai of class OhaiFactCollector
def test_OhaiFactCollector_run_ohai():
    import ansible.module_utils.facts.collector
    from ansible.module_utils._text import to_bytes

    collector = OhaiFactCollector()
    module = ansible.module_utils.facts.collector.FactsCollector()
    ohai_path = collector.find_ohai(module)
    rc, out, err = collector.run_ohai(module, ohai_path)
    assert rc == 0, 'The return code of running ohai is %r, expected 0' % rc
    assert isinstance(out, to_bytes) and len(out) > 0, \
        'The output of running ohai is %r, expected non-empty string' % out
    assert len(err) == 0, 'The standard error of running ohai is %r, expected empty string' % err

    # Unit test for method get

# Generated at 2022-06-13 02:01:40.072296
# Unit test for method run_ohai of class OhaiFactCollector
def test_OhaiFactCollector_run_ohai():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts import Collector
    from ansible.module_utils.facts.utils import is_group_enabled
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    # FIXME: this should not be necessary
    import ansible.module_utils.facts.collector
    ansible.module_utils.facts.collector.Collector = Collector

    ohai_ns = PrefixFactNamespace(namespace_name='ohai',
                                  prefix='ohai_')
    ns_list = [ohai_ns]
    module_path = 'ansible.module_utils.facts.collectors.ohai'
    collectors_list = [module_path]

# Generated at 2022-06-13 02:01:43.320835
# Unit test for method get_ohai_output of class OhaiFactCollector
def test_OhaiFactCollector_get_ohai_output():
    try:
        from ansible.module_utils.basic import AnsibleModule
        m = AnsibleModule()
        o = OhaiFactCollector()
        return o.get_ohai_output(m)
    except Exception:
        return None

# Generated at 2022-06-13 02:01:50.910670
# Unit test for method get_ohai_output of class OhaiFactCollector
def test_OhaiFactCollector_get_ohai_output():
    import ansible.module_utils.facts.module_setup as module_setup
    import ansible.module_utils.facts.collectors.ohai as ohai

    facts = module_setup.get_module_facts()

    ohai_fact_collector = ohai.OhaiFactCollector()
    # The test below is expected to succeed by examining the JSON output of
    # the ohai binary in Ansible's test execution environment.
    # This test is not expected to succeed in a shell with no ohai available.
    ohai_fact_collector.get_ohai_output(facts)


# Generated at 2022-06-13 02:01:58.557271
# Unit test for method find_ohai of class OhaiFactCollector
def test_OhaiFactCollector_find_ohai():
    class ModuleObj(object):
        def get_bin_path(self, filename):
            return "./bin/%s" % filename

    module = ModuleObj()
    ohai_fact_collector = OhaiFactCollector()

    # test the successful execution of find_ohai when the bin directory exists
    mock_ohai_bin_path = ohai_fact_collector.find_ohai(module)
    assert mock_ohai_bin_path == './bin/ohai'

    # test the successful of test_OhaiFactCollector_find_ohai when the bin directory does not exist
    def mock_get_bin_path(self, filename):
        raise OSError
    module.get_bin_path = mock_get_bin_path.__get__(module, module.__class__)
    mock_

# Generated at 2022-06-13 02:02:05.185329
# Unit test for method collect of class OhaiFactCollector
def test_OhaiFactCollector_collect():
    # given
    class Module(object):
        def get_bin_path(self, name):
            pass

        def run_command(self, name):
            pass

    ohai_collector = OhaiFactCollector()
    module = Module()
    # when
    ohai_facts = ohai_collector.collect(module)
    # then
    assert ohai_facts != None



# Generated at 2022-06-13 02:02:11.253828
# Unit test for method get_ohai_output of class OhaiFactCollector
def test_OhaiFactCollector_get_ohai_output():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts import Facts, OhaiFactCollector

    test_collector = OhaiFactCollector()
    test_module = AnsibleModule(argument_spec=dict())
    expected_facts_collector = None
    expected_facts = {}
    actual_facts_collector = test_collector.get_ohai_output(test_module)

    assert actual_facts_collector == expected_facts_collector


# Generated at 2022-06-13 02:02:23.097251
# Unit test for method get_ohai_output of class OhaiFactCollector
def test_OhaiFactCollector_get_ohai_output():
    module = AnsibleModule(argument_spec={})
    module.exit_json = lambda changed, ansible_facts: ansible_facts
    OhaiFactCollector().get_ohai_output(module)

# Generated at 2022-06-13 02:02:28.912248
# Unit test for method get_ohai_output of class OhaiFactCollector
def test_OhaiFactCollector_get_ohai_output():
    from ansible.module_utils.facts.test.test_ohai import TestModule
    ohai = OhaiFactCollector()
    test_module = TestModule(params=dict())
    ohai_output = ohai.get_ohai_output(test_module)
    assert ohai_output is not None
    assert 'fqdn' in ohai_output
    assert 'kernel' in ohai_output

# Generated at 2022-06-13 02:02:33.670989
# Unit test for method get_ohai_output of class OhaiFactCollector
def test_OhaiFactCollector_get_ohai_output():
    class Mock:
        pass

    module = Mock()
    module.get_bin_path = lambda _: 'totally_a_path'
    module.run_command = lambda _: (0, '{"foo": "bar"}', '')

    c = OhaiFactCollector()
    ohai_output = c.get_ohai_output(module)
    assert ohai_output == '{"foo": "bar"}'

# Generated at 2022-06-13 02:02:40.274686
# Unit test for method collect of class OhaiFactCollector
def test_OhaiFactCollector_collect():
    '''Unit test for method collect of class OhaiFactCollector.'''

    class TestModule(object):
        def __init__(self, return_value):
            self.return_value = return_value
        def get_bin_path(self, path, required=False):
            return path
        def run_command(self, cmd):
            return self.return_value

    test_module_return_value = (0, '{"platform":"ubuntu", "platform_version":"14.04"}', '')
    test_module = TestModule(test_module_return_value)

    ohfc = OhaiFactCollector()
    test_results = ohfc.collect(test_module)

    assert test_results == {"platform":"ubuntu", "platform_version":"14.04"}

# Generated at 2022-06-13 02:02:51.016914
# Unit test for method collect of class OhaiFactCollector
def test_OhaiFactCollector_collect():
    from ansible.module_utils.facts.collector import MockModule
    from ansible.module_utils.facts.collector import MockCollector

    mock_module = MockModule()
    fake_ohai_output = '{"kernel": {"os": "Darwin"}}'
    mock_module.run_command = lambda x: (0, fake_ohai_output, '')
    mock_module.get_bin_path = lambda x: '/usr/bin/ohai'

    ohai_collector = OhaiFactCollector(collectors=MockCollector())
    collect = ohai_collector.collect(mock_module)

    assert collect
    assert collect['ohai_kernel']
    assert collect['ohai_kernel']['os'] == 'Darwin'


# Generated at 2022-06-13 02:02:58.670859
# Unit test for method collect of class OhaiFactCollector
def test_OhaiFactCollector_collect():
    import mock
    import types

    module = mock.Mock()

    mock_module = mock.Mock()
    mock_out = '''
    {
        "id": "test",
        "name": "test"
    }
    '''
    mock_module.run_command = mock.Mock(return_value=(0, mock_out, ''))
    def get_bin_path(bin_name):
        if bin_name == 'ohai':
            return '/bin/ohai'
        return None
    mock_module.get_bin_path = types.MethodType(get_bin_path, mock_module)

    ohai_fact_collector = OhaiFactCollector(module=mock_module)
    facts = ohai_fact_collector.collect()

# Generated at 2022-06-13 02:03:09.018712
# Unit test for method get_ohai_output of class OhaiFactCollector
def test_OhaiFactCollector_get_ohai_output():
    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils.facts.namespace import FactsNamespace
    from ansible.module_utils.facts.util import set_module
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector
    from ansible.module_utils._text import to_text

    distribution_facts = DistributionFactCollector().collect(module=set_module(None))
    if not distribution_facts:
        sys.exit(0)

    distro_name = distribution_facts['distribution_name']
    distro_version = distribution_facts['distribution_version']
    distro_major_version = distribution_facts['distribution_major_version']

    module = set_module(None)
    module.run_command = Magic

# Generated at 2022-06-13 02:03:17.064500
# Unit test for method find_ohai of class OhaiFactCollector
def test_OhaiFactCollector_find_ohai():

    ohai_fact_collector = OhaiFactCollector()
    class fake_module():
        class fake_path():
            def split(self):
                return ['/usr/bin', 'ohai']
        def get_bin_path(self, binary):
            path = self.fake_path()
            if binary == 'ohai':
                return path
            return None

    module = fake_module()
    ohai_path = ohai_fact_collector.find_ohai(module)

    expected_ohai_path = '/usr/bin/ohai'
    assert ohai_path == expected_ohai_path


# Generated at 2022-06-13 02:03:23.195701
# Unit test for method collect of class OhaiFactCollector
def test_OhaiFactCollector_collect():
    module = MockModule()
    module.params = {}
    module.run_command = lambda command, check_rc=True, close_fds=True: (0, '{"platform": "Mock_OS", "platform_version": "1.0"}', '')
    ohai_collector = OhaiFactCollector()
    ohai_facts = ohai_collector.collect(module)
    assert ohai_facts['ohai_platform'] == 'Mock_OS'


# Generated at 2022-06-13 02:03:30.761440
# Unit test for method collect of class OhaiFactCollector
def test_OhaiFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector

    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes

    class AnsibleModule(basic.AnsibleModule):
        def __init__(self):
            super(AnsibleModule, self).__init__()
            self.params = {}

        def fail_json(self, **kwargs):
            pass

        def exit_json(self, **kwargs):
            pass

    ansible_module = AnsibleModule()

    ohai_fact_collector = OhaiFactCollector(collected_facts=None)
    ohai_fact_collector.collect(module=ansible_module)
    assert(ohai_fact_collector._fact_ids == set([]))


# Generated at 2022-06-13 02:03:54.040355
# Unit test for method get_ohai_output of class OhaiFactCollector
def test_OhaiFactCollector_get_ohai_output():
    from ansible.module_utils.facts.collector.ohai import OhaiFactCollector
    from ansible.module_utils import basic
    ohai_module = basic.AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )
    ohai_collector = OhaiFactCollector()
    output = ohai_collector.get_ohai_output(ohai_module)
    assert output is not None

# Generated at 2022-06-13 02:03:56.557898
# Unit test for method collect of class OhaiFactCollector
def test_OhaiFactCollector_collect():
    myFacCol = OhaiFactCollector()
    facts = myFacCol.collect()
    assert (type(facts) is dict)


# Generated at 2022-06-13 02:04:02.557266
# Unit test for method collect of class OhaiFactCollector
def test_OhaiFactCollector_collect():
    ohai_output = """
    {
    "foo": {
        "spam": "hello world"
    },
    "bar": "baz",
    "baz": 1234
    }
    """

    def run_ohai(ohai_path):
        return 0, ohai_output, None
    f = OhaiFactCollector()
    f._run_ohai = run_ohai

    assert f.collect() == {'foo': {'spam': 'hello world'},
                           'bar': 'baz',
                           'baz': 1234}

# Generated at 2022-06-13 02:04:10.267328
# Unit test for method collect of class OhaiFactCollector
def test_OhaiFactCollector_collect():
    from ansible.module_utils.six import PY2

    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    namespace = PrefixFactNamespace(namespace_name='ohai',
                                    prefix='ohai_')

    # Ohai fact collector
    collector = OhaiFactCollector(namespace=namespace)

    # Mock ohai output
    mock_ohai_output = b'{"fqdn":"myhost.mydomain.com","ipaddress":"1.2.3.4","macaddress":"01:02:03:04"}'


    # Mock module object
    class MockModule(object):

        # Mock get_bin_path()
        def get_bin_path(self, path):
            return "/bin/ohai"

        # Mock run_command()

# Generated at 2022-06-13 02:04:13.791136
# Unit test for method find_ohai of class OhaiFactCollector
def test_OhaiFactCollector_find_ohai():
    import ansible.module_utils.facts.collector
    import ansible.module_utils.facts

    ohai_path = ansible.module_utils.facts.collector.OhaiFactCollector().find_ohai(ansible.module_utils.facts.Facts())
    assert(ohai_path)


# Generated at 2022-06-13 02:04:18.205773
# Unit test for method collect of class OhaiFactCollector
def test_OhaiFactCollector_collect():
    class mock_module(object):
        def get_bin_path(self, path, opt_dirs=[]):
            return True

        def run_command(self, path):
            return 0, "", ""

    module = mock_module()

    ohai_collector = OhaiFactCollector()
    ohai_facts = ohai_collector.collect(module)

    assert ohai_facts



# Generated at 2022-06-13 02:04:22.004620
# Unit test for method run_ohai of class OhaiFactCollector
def test_OhaiFactCollector_run_ohai():
    module = AnsibleModuleMock()
    module = AnsibleModuleMock()
    ohai_path = '/usr/bin/ohai'
    rc, out, err = OhaiFactCollector().run_ohai(module, ohai_path)
    assert rc == 0

# This is necessary in order to dynamically create test cases.
# In AnsibleModuleMock() method, class_name attribute is appended.

# Generated at 2022-06-13 02:04:25.476733
# Unit test for method find_ohai of class OhaiFactCollector
def test_OhaiFactCollector_find_ohai():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts.collector import BaseFactCollector

    namespace = PrefixFactNamespace(namespace_name='ohai',
                                    prefix='ohai_')
    ohai_coll = OhaiFactCollector(namespace=namespace)
    assert ohai_coll is not None
    ohai_coll.find_ohai()



# Generated at 2022-06-13 02:04:31.804501
# Unit test for method find_ohai of class OhaiFactCollector
def test_OhaiFactCollector_find_ohai():
    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils import basic

    ohai_fact_collector = get_collector_instance('ohai')
    module = basic.AnsibleModule(argument_spec={})

    if ohai_fact_collector.find_ohai(module):
        ohai_path = ohai_fact_collector.find_ohai(module)
        assert "ohai" == ohai_path.split("/")[-1]

    else:
        assert "ohai" not in ohai_fact_collector.find_ohai(module)


# Generated at 2022-06-13 02:04:32.742753
# Unit test for method find_ohai of class OhaiFactCollector
def test_OhaiFactCollector_find_ohai():
    collector = OhaiFactCollector()
    assert not collector.find_ohai(None)

# Generated at 2022-06-13 02:05:16.606292
# Unit test for method find_ohai of class OhaiFactCollector
def test_OhaiFactCollector_find_ohai():
    import ansible.module_utils.facts.collector
    from ansible.module_utils.facts.collector import get_collector_instance

    type(ansible.module_utils.facts.collector)._COLLECTORS = None
    collector = get_collector_instance(OhaiFactCollector)
    assert(collector._find_ohai is not None)
    assert(collector.find_ohai is not None)


# Generated at 2022-06-13 02:05:24.448181
# Unit test for method find_ohai of class OhaiFactCollector
def test_OhaiFactCollector_find_ohai():
    # Using the MockedModule class from test_ansible_module we can easily
    # mock up the parts we need.
    from ansible.module_utils import basic
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils.facts import timeout

    ohai_fact_collector = OhaiFactCollector(collectors=None, namespace=None)
    module = basic.AnsibleModule(argument_spec={})

    # Test when ohai is found
    ohai_fact_collector.getbin = lambda x: x
    assert ohai_fact_collector.find_ohai(module) == 'ohai'

    # Test when ohai is not found
    ohai_fact_collector.getbin = lambda x: None
    assert ohai_fact_collector.find_oh

# Generated at 2022-06-13 02:05:30.478149
# Unit test for method get_ohai_output of class OhaiFactCollector
def test_OhaiFactCollector_get_ohai_output():
    def run_ohai(ohai_path):
        # We don't want to test the output of ohai, so we just return
        # something hardcoded.
        #
        # NOTE: This test assumes the output of ohai is a JSON object
        # with the top-level key 'fqdn'
        import json
        facts = {"fqdn": "myhost.mydomain.com"}
        facts_json = json.dumps(facts)

        # Return the JSON string as if it were the output of ohai
        return 0, facts_json, ''

    # Patch run_ohai with our mocked version
    import ansible.module_utils.facts.ohai as ohai
    old_run_ohai = ohai.run_ohai
    ohai.run_ohai = run_ohai

    # Create our object


# Generated at 2022-06-13 02:05:32.718109
# Unit test for method get_ohai_output of class OhaiFactCollector
def test_OhaiFactCollector_get_ohai_output():
    # we cannot really test this method because there is no way of telling if Ohai is installed on the system running the unit tests
    assert True

# Generated at 2022-06-13 02:05:33.622165
# Unit test for method collect of class OhaiFactCollector
def test_OhaiFactCollector_collect():
    assert 1 == 1

# Generated at 2022-06-13 02:05:41.268913
# Unit test for method get_ohai_output of class OhaiFactCollector
def test_OhaiFactCollector_get_ohai_output():
    # Test setup
    ohai_path = "/tmp/does_not_exist"

    class MockOs(object):
        def getenv(self, varname):
            return None

    class MockModule(object):
        # Mocking basic method we need for this particular method test
        def get_bin_path(self, bin_name, opt_dirs=None):
            return ohai_path

        def run_command(self, cmd):
            return 1, "", "ohai not found, or could not be run"

        os = MockOs()

    ohai_collector = OhaiFactCollector()

    # Test
    out = ohai_collector.get_ohai_output(MockModule())

    # Test result
    assert out is None



# Generated at 2022-06-13 02:05:48.366960
# Unit test for method get_ohai_output of class OhaiFactCollector
def test_OhaiFactCollector_get_ohai_output():
    """
    Test case to verify if the ohai_output is correctly extracted.
    """
    from ansible.module_utils.facts.ohai import OhaiFactCollector
    class MockModule:
        """ MockModule class stub. """
        def get_bin_path(self, cmd):
            return "/usr/bin/ohai"
        def run_command(self, ohai_path):
            out = { "top": { "ohai": { "name": "ohai" } } }
            return 0, json.dumps(out), ""
    mock_module = MockModule()
    ohai_fact_collector = OhaiFactCollector()
    ohai_output = ohai_fact_collector.get_ohai_output(mock_module)
    assert isinstance(ohai_output, str)
    out

# Generated at 2022-06-13 02:05:59.749808
# Unit test for method collect of class OhaiFactCollector
def test_OhaiFactCollector_collect():
  # Run a test on find_ohai to determine the path of ohai binary
    def test_find_ohai():
        ohai_path = OhaiFactCollector.find_ohai(self)
        return ohai_path

  # Run a test on run_ohai to run ohai binary and get output from it
    def test_run_ohai():
        rc, out, err = OhaiFactCollector.run_ohai(self, ohai_path)
        return rc, out, err

  # Run a test on get_ohai_output to get the output from run_ohai
    def test_get_ohai_output():
        ohai_output = OhaiFactCollector.get_ohai_output(self, rc, out, err)
        return ohai_output

  # Run a test on collect to get

# Generated at 2022-06-13 02:06:09.982080
# Unit test for method get_ohai_output of class OhaiFactCollector
def test_OhaiFactCollector_get_ohai_output():
    import ansible.module_utils.facts.collector
    from ansible.module_utils.facts import collectors

    collectors['ohai'] = OhaiFactCollector()

    def exists(path):
        if path == '/usr/bin/ohai':
            return True
        return False

    # Make sure the module_utils.facts.collector.run_command doesn't get called
    # from the get_ohai_output method, just a dummy function that returns
    # None, None, None, so the OhaiFactCollector.run_ohai doesn't run
    def run_command(command):
        return None, None, None

    ansible.module_utils.facts.collector.os.path.exists = exists
    ansible.module_utils.facts.collector.run_command = run_command

    ohai_facts

# Generated at 2022-06-13 02:06:15.733577
# Unit test for method get_ohai_output of class OhaiFactCollector
def test_OhaiFactCollector_get_ohai_output():
    from ansible.module_utils.facts import TESTING_INFRASTRUCTURE_MODULE

    ohai_output = """{
    "platform_family": "mac_os_x",
    "platform": "mac_os_x",
    "platform_version": "10.11.6",
    "os_version": "10.11",
    "os_version_major": "10",
    "os_version_minor": "11"
    }"""

    class MockOhaiModule:
        def get_bin_path(self, path, opt_dirs=[]):
            return 'ohai'
        def run_command(self, path):
            return 0, ohai_output, ''

    ohai_fact_collector = OhaiFactCollector([])
    ohai_facts = ohai_fact_

# Generated at 2022-06-13 02:07:40.537954
# Unit test for method collect of class OhaiFactCollector
def test_OhaiFactCollector_collect():
    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts.utils import get_file_content
    from ansible.module_utils._text import to_bytes

    fake_module = get_file_content('module_utils/facts/utils/module.py')
    fake_module = to_bytes(fake_module)
    module = type(to_bytes('module'))
    module.run_command = lambda cmd: (0, '{}', None)
    module.get_bin_path = lambda cmd: 'ohai'
    
    default_collector = get_collector_instance('default')
    default_collector._module = module
    ohai_collector = get

# Generated at 2022-06-13 02:07:47.635391
# Unit test for method collect of class OhaiFactCollector
def test_OhaiFactCollector_collect():
    import ansible.module_utils.facts.collector
    import ansible.module_utils.facts.namespace
    import ansible.module_utils.facts.system.distribution
    import ansible.module_utils.facts.system.distribution_release

    ohai_facts = {
            'bar': 'baz',
            'cheese': {
                'swiss': True,
                'cheddar': False,
                }
            }

    class FakeModule:
        def run_command(self, cmd):
            rc, out, err = 0, json.dumps(ohai_facts), ''
            return rc, out, err

        def get_bin_path(self, path):
            return path

    class FakeCollector:
        _fact_ids = {'bar': None, 'cheese': None}


# Generated at 2022-06-13 02:07:55.031361
# Unit test for method get_ohai_output of class OhaiFactCollector
def test_OhaiFactCollector_get_ohai_output():
    method = OhaiFactCollector.get_ohai_output
    method.func_code = PrefixFactNamespace.get_bin_path.im_func.func_code
    class FakeModule():
        def get_bin_path(self, cmd):
            return '/usr/bin/{0}'.format(cmd)
        def run_command(self, cmd):
            return (0, '{"file": {"system": "posix"}}', '')
    module = FakeModule()
    ohai_output = method(None, module)
    assert ohai_output == '{"file": {"system": "posix"}}'

# Generated at 2022-06-13 02:08:02.429648
# Unit test for method get_ohai_output of class OhaiFactCollector
def test_OhaiFactCollector_get_ohai_output():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.module_utils.six import string_types
    from ansible.module_utils.six.moves import shlex_quote
    from ansible.module_utils.facts import default_collectors

    # BaseFactCollector instance used to mock a module

# Generated at 2022-06-13 02:08:09.880266
# Unit test for method run_ohai of class OhaiFactCollector
def test_OhaiFactCollector_run_ohai():
    module = AnsibleModuleMock()
    ohai_path = '/usr/bin/ohai'
    ohai_out = '{"platform": "redhat"}'
    rc = 0

    def mock_run_command(path):
        assert path == ohai_path
        return rc, ohai_out, ''

    module.run_command = mock_run_command

    collector = OhaiFactCollector()
    rc, out, err = collector.run_ohai(module, ohai_path)
    assert out == ohai_out
    assert err == ''
    assert rc == rc



# Generated at 2022-06-13 02:08:13.203383
# Unit test for method collect of class OhaiFactCollector
def test_OhaiFactCollector_collect():
    class TestModule(object):
        def get_bin_path(self, binary_name):
            return "ohai"
        def run_command(self, cmd):
            try:
                with open("/tmp/ohai.json", "r") as f:
                    return (0, f.read(), "")
            except IOError:
                return None
    m = TestModule()
    fc = OhaiFactCollector()
    return fc.collect(m)

# Generated at 2022-06-13 02:08:18.156153
# Unit test for method get_ohai_output of class OhaiFactCollector
def test_OhaiFactCollector_get_ohai_output():
    ohai_path = 'bin/ohai'
    ohai_facts = {
        'dmi': {
            'system': {
            'manufacturer': 'VMware, Inc.',
            'serial_number': 'VMware-56 4d 2b 5a 2b 55 6a-f9 2d 79 bd 62 5f 3e',
            'uuid': '42 42 42 42-42 42 42 42-42 42 42 42-42 42 42 42',
            'product_name': 'VMware Virtual Platform',
            'family': 'Virtual Machine',
            'version': 'None'}}}

    ohai_out = json.dumps(ohai_facts)

    module_mock = AnsibleModuleMock()
    module_mock.run_command.return_value = (0, ohai_out, '')

    o

# Generated at 2022-06-13 02:08:28.217520
# Unit test for method get_ohai_output of class OhaiFactCollector
def test_OhaiFactCollector_get_ohai_output():
    try:
        from ansible.module_utils.facts import ansible_collector
        import ansible.module_utils.facts.collector
        import ansible.module_utils
    except ImportError:
        import pytest
        pytest.skip('Unable to import ansible library',
                    allow_module_level=True)

    ohai_fact_collector = OhaiFactCollector(collectors=ansible_collector)

    module_utils_get_bin_path_orig = ansible.module_utils.facts.collector.ModuleUtils.get_bin_path
    ansible.module_utils.facts.collector.ModuleUtils.get_bin_path = lambda x, y: False
    assert ohai_fact_collector.get_ohai_output({}) is None

# Generated at 2022-06-13 02:08:36.349123
# Unit test for method get_ohai_output of class OhaiFactCollector
def test_OhaiFactCollector_get_ohai_output():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.compat import PY3
    from ansible.module_utils.facts.ohai.ohai import test_get_module_path
    from ansible.module_utils.facts.ohai.ohai import test_get_module_args

    module = None
    try:
        module = test_get_module_path()
    except:
        # FIXME: no error handling is done
        pass

    if PY3:
        # Need byte literal
        raw_json = to_bytes('{"network": {"interfaces": {"eth0": {"addresses": {"00:0c:29:ca:7a:bc": {"family": "lladdr"}}}}}}')

# Generated at 2022-06-13 02:08:43.845875
# Unit test for method collect of class OhaiFactCollector
def test_OhaiFactCollector_collect():
    # Test that collect() returns the desired fact:
    #  ohai_platform_version
    # If value of this fact is the string 'unittest', then collect()
    # is achieving its desired output in this test:
    ohai_platform_version = 'unittest'
    ohai_output = json.dumps({'platform_version': ohai_platform_version})
    ohai_fact_collector = OhaiFactCollector()
    ohai_fact_collector.run_ohai = Mock(return_value=(0, ohai_output, None))
    ohai_fact_collector.get_ohai_output = Mock(return_value=ohai_output)
    result = ohai_fact_collector.collect()
    assert result['ohai_platform_version'] == ohai_platform_version

