

# Generated at 2022-06-13 03:01:53.191476
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    lfc = LocalFactCollector()
    assert lfc.name == 'local'


# Generated at 2022-06-13 03:01:53.576572
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    pass

# Generated at 2022-06-13 03:01:56.775677
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    '''Unit test for constructor of class LocalFactCollector'''

    # The collector class needs to be instantiated to test any of its
    # attributes.
    local_collector = LocalFactCollector()

    assert local_collector.name == 'local'

# Generated at 2022-06-13 03:01:59.194789
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    local_fact_collector = LocalFactCollector()
    assert local_fact_collector.name == 'local'
    assert local_fact_collector.priority == 10
    assert local_fact_collector.enabled

# Generated at 2022-06-13 03:02:05.076078
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    # Create the class instance
    local_fact_collector = LocalFactCollector()
    # Set known data
    local_fact_collector.module = None
    local_fact_collector.collected_facts = None
    # Call the method and assert the result
    result = local_fact_collector.collect()
    assert isinstance(result, dict)
    assert 'local' in result

# Generated at 2022-06-13 03:02:17.987954
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    import os
    import tempfile
    from ansible.module_utils.facts.collector import BaseFactCollector

    class TestModule(object):
        def __init__(self, params):
            self.params = params

        def run_command(self, cmd):
            return(0, '{ "foo": "bar" }', '')

        def warn(self, msg):
            pass

    # Create a temporary directory
    tmpdir = tempfile.mkdtemp()

    # Create a temporary config file
    tmpfile = tempfile.NamedTemporaryFile(dir=tmpdir, delete=False)

    fact_path = tmpdir
    fact_file = tmpfile.name

    # Create a json fact file
    json_fact_file = fact_file + '.fact'

# Generated at 2022-06-13 03:02:22.104259
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    local_fact_collector = LocalFactCollector()
    assert local_fact_collector.name == 'local'
    assert isinstance(set(local_fact_collector._fact_ids), set)

    assert isinstance(local_fact_collector.collect(collected_facts=None), dict)

# Generated at 2022-06-13 03:02:34.256418
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils.facts.collector import Collector
    import ansible.module_utils.facts.system.distribution as distribution

    fact_collector = FactCollector(None)
    fact_collector.collectors = [LocalFactCollector(fact_collector), Collector(distribution, fact_collector)]
    facts = fact_collector._collect(dict(fact_path='test/unit/module_utils/facts/factsd'))
    os_facts = facts['system']['distribution']
    assert(os_facts == {'name': 'RedHat',
                        'version': '7.6',
                        'release': 'Core',
                        'family': 'RedHat',
                        'major': '7'
                        })

# Generated at 2022-06-13 03:02:35.944510
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
	localFactCollector = LocalFactCollector()
	assert localFactCollector

# Unit tests for LocalFactCollector().collect()

# Generated at 2022-06-13 03:02:43.553283
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    fake_fact_path = os.path.join(os.getcwd(), 'unit', 'ansible', 'module_utils', 'facts', 'fixtures', 'local')

# Generated at 2022-06-13 03:02:51.431419
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    facts = {}
    local_fact_collector = LocalFactCollector()
    result = local_fact_collector.collect(facts)

    assert result['local'] == {}

# Generated at 2022-06-13 03:02:53.324150
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    local_fact_collector = LocalFactCollector()
    assert local_fact_collector.name == 'local'
    assert local_fact_collector._fact_ids == set()

# Generated at 2022-06-13 03:02:55.785824
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    local_facts = {}
    local_facts['local'] = {}
    assert LocalFactCollector().collect(local_facts) == local_facts
    assert LocalFactCollector().collect() == {}

# Generated at 2022-06-13 03:02:56.946037
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    local = LocalFactCollector()
    assert local.name == 'local'

# Generated at 2022-06-13 03:03:02.776674
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    local_facts = {}
    shell_fact = {}
    local_facts['local'] = shell_fact
    def mock_run_command(self, cmd):
        shell_fact['test_shell_fact'] = {'fact': 'shell'}
        return (0, '', '')
    BaseFactCollector.run_command = mock_run_command
    LocalFactCollector().collect(collected_facts=None)

# Generated at 2022-06-13 03:03:05.665575
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    local_facts = LocalFactCollector()
    assert local_facts.name == 'local'
    assert local_facts._fact_ids == set()

# Generated at 2022-06-13 03:03:10.138225
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    module = None
    local_facts = {"ansible_facts" : {"local" : {"ansible_processor_cores":1,"ansible_processor":2}}}
    local_collector = LocalFactCollector()
    assert local_collector.collect(module, local_facts) == local_facts

# Generated at 2022-06-13 03:03:13.631579
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    """Tests if LocalFactCollector._collect() returns a dictionary."""

    from ansible.module_utils.facts.collectors.local import LocalFactCollector

    localFactCollector = LocalFactCollector()

    assert isinstance(localFactCollector.collect(), dict)

# Generated at 2022-06-13 03:03:17.365030
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    local_fact_collector = LocalFactCollector()
    assert local_fact_collector
    assert local_fact_collector.name == 'local'
    assert local_fact_collector._fact_ids == set()


# Generated at 2022-06-13 03:03:21.934544
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    """
    Test to check the constructor of class LocalFactCollector
    """
    local_fact_collector = LocalFactCollector()

    assert type(local_fact_collector) == LocalFactCollector
    assert local_fact_collector.name == "local"
    assert local_fact_collector._fact_ids == set()
    assert local_fact_collector._legacy_warnings == ['local']


# Generated at 2022-06-13 03:03:37.312657
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    # Instantiate class
    instance = LocalFactCollector()

    assert instance.name == 'local'
    #assert instance._fact_ids == set()
    # FIXME: This needs to be fixed to have a default value that matches what is done in the code
    assert instance._fact_ids == set()

# Generated at 2022-06-13 03:03:39.855244
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    import ansible.module_utils
    obj = LocalFactCollector()
    module = ansible.module_utils.basic.AnsibleModule({})
    assert obj.collect(module) == None


# Generated at 2022-06-13 03:03:41.625530
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    local_facts = LocalFactCollector()
    assert local_facts.name == 'local'
    assert local_facts._fact_ids == set()

# Generated at 2022-06-13 03:03:45.659500
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    from ansible.module_utils.facts.collector import collect_facts
    fact_path = '/opt/local/facts/'
    module = None
    for fact_vars in collect_facts(module, 'dummy_path', [], [LocalFactCollector],
                                   fact_path).values():
        assert fact_vars['local'] == {}

# Generated at 2022-06-13 03:03:48.833406
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    local = LocalFactCollector()
    assert local.name == "local"

    assert isinstance(local._fact_ids, set)
    assert local._fact_ids == set()

    assert hasattr(local, 'collect')
    assert callable(local.collect)

# Generated at 2022-06-13 03:03:59.861214
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    from ansible.module_utils.facts.utils import get_file_content
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils import basic

    import tempfile
    import os

    class MyModule(object):
        def __init__(self, params):
            self.params = params

        def run_command(self, command):
            return (0, '', '')

    class MyBasic(object):
        def __init__(self):
            self.params = {}

    class MyFacts(object):
        def __init__(self, facts=None):
            self.facts = facts

        def get(self, key, default=None):
            return self.facts.get(key, default)


# Generated at 2022-06-13 03:04:01.616841
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    x = LocalFactCollector()
    assert x.name == 'local'

# Generated at 2022-06-13 03:04:02.218586
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    pass

# Generated at 2022-06-13 03:04:07.248260
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    module = AnsibleModule(
        argument_spec={
            'fact_path': {'default': '/etc/ansible/facts.d', 'type': 'str'},
        }
    )
    local_facts = LocalFactCollector()
    local_facts.options = {'fact_path': '/etc/ansible/facts.d'}
    local_facts.collect(module)

# Generated at 2022-06-13 03:04:14.419496
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    from ansible.module_utils.facts.collector import FakeModule
    from ansible.module_utils import basic
    import ansible_local

    local_facts = ansible_local.setup_module_object()
    module = FakeModule()
    local_facts = local_facts['ansible_local']
    local_facts['module'] = module
    # Assert that fact_path exists and contains at least 1 file
    fact_path_exists = False
    for file_path in basic._ANSIBLE_ARGS.value:
        if 'fact_path' in file_path:
            fact_path_exists = True
            fact_path_value = file_path.split('=')[1]

# Generated at 2022-06-13 03:04:38.539346
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    x = LocalFactCollector()
    assert x.name == 'local'
    assert not x._fact_ids
    assert x.collect() == {'local': {}}

# Generated at 2022-06-13 03:04:39.655705
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    local_fact_collector = LocalFactCollector()


# Generated at 2022-06-13 03:04:41.914071
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    lfc = LocalFactCollector()
    (facts, _warnings) = lfc.collect()
    assert facts

# Generated at 2022-06-13 03:04:49.044652
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    module = ansible.module_utils.basic.AnsibleModule(argument_spec=dict(fact_path=dict(type='path')))
    module.params['fact_path'] = '/tmp/facts'
    module.run_command = MagicMock(return_value=(0, 'success', ''))

    collector = LocalFactCollector()
    result = collector.collect(module=module)
    assert result == {'local': {'fake_fact1': '{"fake_info1": "fake_value1"}', 'fake_fact2': 'FAILURE running fact script', 'fake_fact3': '{"fake_info3_1": "fake_value3_1", "fake_info3_2": "fake_value3_2"}'}}

# Generated at 2022-06-13 03:04:50.187536
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    module = object()
    assert LocalFactCollector.__init__(module)


# Generated at 2022-06-13 03:04:55.536042
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    from ansible.module_utils.facts import reload_module_utils_facts
    import tempfile
    import shutil
    import os

    # setup env
    tmpdir = tempfile.mkdtemp()
    os.mkdir(os.path.join(tmpdir, 'facts.d'))
    os.environ['ANSIBLE_LOCAL_TEMP'] = tmpdir
    os.environ['ANSIBLE_COLLECTIONS_PATHS'] = ''
    os.environ['ANSIBLE_LIBRARY'] = ''

    # avoid polluting the local fact cache with any data from previous runs
    reload_module_utils_facts()

    # create the local fact config file
    configfile = os.path.join(tmpdir, 'ansible.cfg')

# Generated at 2022-06-13 03:05:03.398088
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    from ansible.module_utils.facts.collector import FactsCollector

    FactsCollector.collection_registry.clear()
    def mock_params(**kwargs):
        return Mock(params=kwargs)

    def mock_run_command(command, **kwargs):
        if command == 'echo_stream':
            return 0, '', ''
        if command == 'echo_one_line':
            return 0, 'hi', ''
        if command == 'echo_one_json':
            return 0, '{"hi": "there"}', ''
        if command == 'echo_one_ini':
            return 0, '[DEFAULT]\nopt = value', ''
        if command == 'echo_bad_json':
            return 0, '{', ''

# Generated at 2022-06-13 03:05:05.722679
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    lfc = LocalFactCollector()
    assert lfc.name == 'local'
    assert lfc._fact_ids == set()


# Generated at 2022-06-13 03:05:08.274078
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    q = LocalFactCollector()
    assert q.name == 'local'
    assert isinstance(q.collect(), dict)
    assert isinstance(q._fact_ids, set)


# Generated at 2022-06-13 03:05:14.916944
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    m = AnsibleModule(argument_spec={'fact_path': {'type': 'str', 'required': True}})

    lfc = LocalFactCollector()
    facts = lfc.collect(module=m, collected_facts=None)

    assert facts['local']['fact_base'] == {
        'sub_fact_one': 'value_one',
        'sub_fact_two': 'value_two'
    }

# Generated at 2022-06-13 03:06:14.990605
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():

    class Module(object):
        def __init__(self):
            self.params = {}

        def _run_command(self, cmd):
            return (0, '{}', '')

        def run_command(self, cmd):
            return self._run_command(cmd)

    module = Module()
    module.params['fact_path'] = 'test/unit/module_utils/facts/fixtures/local/'
    local_facts = LocalFactCollector().collect(module=module)

    # Test to assert that the dictionary local_facts is not empty
    assert local_facts != {}

    # Test to assert that 'local' key is present in the dictionary local_facts
    assert 'local' in local_facts

    # Test to assert that the 'cmd' value is equal to "echo '{\"item\":\"value\"}'"


# Generated at 2022-06-13 03:06:17.698308
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    assert LocalFactCollector.name == 'local'
    assert isinstance(LocalFactCollector._fact_ids, set)

# Generated at 2022-06-13 03:06:25.261036
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    import tempfile
    tmpdir = tempfile.mkdtemp()

    fd, script_path = tempfile.mkstemp(
        prefix='ansible_local_fact_script',
        suffix='.fact',
        dir=tmpdir
    )
    os.close(fd)
    os.chmod(script_path, 0o755)
    open(script_path, 'a').close()

    fd, ini_path = tempfile.mkstemp(
        prefix='ansible_local_fact',
        suffix='.fact',
        dir=tmpdir
    )
    os.close(fd)
    with open(ini_path, 'w') as f:
        f.write(u'[foo]\n')
        f.write(u'bar=baz\n')

    fd, json

# Generated at 2022-06-13 03:06:42.777419
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    import ansible.module_utils.facts.collectors as collectors

    collectors.FACT_CACHE = {}
    module = None
    collected_facts = None

    local_collector = collectors.get_collector('local')
    test_local_facts = local_collector.collect(
        module=module, collected_facts=collected_facts)

    # Local fact collector collects a 'local' dictionary in main
    # facts dictionary
    assert 'local' in test_local_facts

    # Local fact dictionary should be populated with 'local' facts
    assert len(test_local_facts['local']) > 0

# Generated at 2022-06-13 03:06:44.203397
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
   assert LocalFactCollector()

# Generated at 2022-06-13 03:06:46.611265
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    x = LocalFactCollector()
    assert x.name == 'local'

# Generated at 2022-06-13 03:06:54.863303
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():

    from ansible.module_utils import basic
    from ansible.module_utils.facts import ipv6_interface_facts
    from ansible.module_utils.facts import local
    from ansible.module_utils.facts import virtual
    from ansible.module_utils._text import to_bytes, to_text

    class Mock:
        def __init__(self):
            self.params = {}
            self.warnings = []

        def run_command(self, cmd):
            out = None

            # Add test data

# Generated at 2022-06-13 03:06:58.934221
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    import pytest
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collectors.local import LocalFactCollector
    import os

    lfc = LocalFactCollector()
    collected_facts = {}
    collected_facts['ansible_local'] = {'local': {'NOT_EXISTS': 'Expected value'}}
    lfc.collect(collected_facts=collected_facts)
    assert collected_facts['ansible_local']['local']['NOT_EXISTS'] == 'Expected value'


# Generated at 2022-06-13 03:07:01.001630
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    local = LocalFactCollector()
    assert local.name == 'local'
    assert local._fact_ids == set()


# Generated at 2022-06-13 03:07:02.647821
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    local_fact_collector = LocalFactCollector()
    assert local_fact_collector.name == 'local'

# Generated at 2022-06-13 03:09:09.560423
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    f_obj = LocalFactCollector()
    assert f_obj is not None
    assert f_obj.name == 'local'


# Generated at 2022-06-13 03:09:10.457046
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    assert 'local' == LocalFactCollector().name

# Generated at 2022-06-13 03:09:19.871969
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    import os
    import pytest

    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector.local import LocalFactCollector

    dummy_module = None
    fact_path = os.path.join(os.path.dirname(__file__), os.pardir, 'unit', 'fixtures', 'facts')
    local_fact_collector = LocalFactCollector({ 'fact_path': fact_path }, dummy_module)

    local_facts = local_fact_collector.collect()

    assert 'local' in local_facts
    assert isinstance(local_facts['local'], dict)

# Generated at 2022-06-13 03:09:20.320220
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    pass

# Generated at 2022-06-13 03:09:23.387655
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    # Initialize a LocalFactCollector and get its local facts
    collector = LocalFactCollector()
    facts = collector.collect()

    # Check that the local facts are empty
    assert facts == {'local': {}}

# Generated at 2022-06-13 03:09:33.524680
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    assert LocalFactCollector.name == 'local'
    l = LocalFactCollector()
    assert l.name == 'local'
    assert l._fact_ids == set()


# Generated at 2022-06-13 03:09:42.833200
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():

    test_executable_file = os.path.dirname(__file__) + '/../../test/fixtures/ansible_local_facts/executable.fact'
    test_json_file = os.path.dirname(__file__) + '/../../test/fixtures/ansible_local_facts/json.fact'
    test_ini_file = os.path.dirname(__file__) + '/../../test/fixtures/ansible_local_facts/ini.fact'
    test_non_readable_file = os.path.dirname(__file__) + '/../../test/fixtures/ansible_local_facts/non_readable.fact'

# Generated at 2022-06-13 03:09:48.347303
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    fact_collector = LocalFactCollector()
    assert fact_collector.name == 'local'
    assert isinstance(fact_collector._fact_ids, set)
    assert fact_collector._fact_ids == set()

# Generated at 2022-06-13 03:09:50.244459
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    obj = LocalFactCollector()
    assert isinstance(obj, LocalFactCollector)


# Generated at 2022-06-13 03:10:02.895824
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    ans_m = AnsibleModule(argument_spec=dict(
        fact_path=dict(default='/etc/ansible/facts.d', type='path'),
    ))
    fc = LocalFactCollector()
    fc._init_collected_facts()
    fc.collect(ans_m)
    print(fc._collected_facts)