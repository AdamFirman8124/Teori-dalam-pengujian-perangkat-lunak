

# Generated at 2022-06-13 03:01:55.274156
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    local_facts = LocalFactCollector()
    assert local_facts.name == 'local'

# Generated at 2022-06-13 03:02:06.692809
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes

    module = basic.AnsibleModule(argument_spec={})
    module.run_command = lambda x: (0, '{"localhost": {"ansible_facts": {"foo": "bar"}}}', '')
    local_facts = LocalFactCollector().collect(module=module)
    assert local_facts == {u'local': {'localhost': {u'ansible_facts': {u'foo': u'bar'}}}}

    module.run_command = lambda x: (0, '{"localhost": "bar"}', '')
    local_facts = LocalFactCollector().collect(module=module)
    assert local_facts == {u'local': {'localhost': u'bar'}}


# Generated at 2022-06-13 03:02:08.989852
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    local_fact_collector = LocalFactCollector()

    assert local_fact_collector.name == 'local'

# Generated at 2022-06-13 03:02:11.237304
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    assert(isinstance(LocalFactCollector(), BaseFactCollector))

# Generated at 2022-06-13 03:02:22.329890
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():

    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils.facts.collector import get_collector_name
    from ansible.module_utils.facts.collector import get_collector_status
    from ansible.module_utils.facts.collector import get_collector_exception
    from ansible.module_utils.facts.collector import set_collector_status
    from ansible.module_utils.facts.collector import set_collector_exception
    from ansible.module_utils.facts.collector import get_all_collector_classes


    collector = get_collector_instance('local')

    assert(collector)
    assert(get_collector_name(collector) == 'local')

# Generated at 2022-06-13 03:02:24.675790
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    local = LocalFactCollector()
    assert local.name == 'local'

# Generated at 2022-06-13 03:02:29.630080
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    CONTENT = {'fact_path': '/etc/ansible/facts.d'}
    local_collector = LocalFactCollector()
    test_data = local_collector.collect(CONTENT)
    assert type(test_data) == dict, 'test_data is not a dict'

test_LocalFactCollector_collect()

# Generated at 2022-06-13 03:02:31.509075
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    local_fact = LocalFactCollector()
    assert local_fact.name == 'local'

# Generated at 2022-06-13 03:02:40.534033
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    from ansible.module_utils.facts.collector import collect_facts
    from ansible.module_utils.facts import Facts
    from ansible.module_utils.facts.collector import BaseFactCollector
    import os
    import shutil
    from tempfile import mkdtemp
    from ansible.module_utils.six.moves import configparser

    # prepare fact_path with fact files in temp dir
    fact_path = mkdtemp()
    templ = os.path.join(fact_path, '%s.fact')
    config = configparser.ConfigParser()
    config.add_section('test')
    config.set('test', 'first', 'yes')
    config.set('test', 'second', 'no')

# Generated at 2022-06-13 03:02:46.520028
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    import os.path
    import shutil
    import tempfile

    from ansible.module_utils.facts import Facts
    from ansible.module_utils._text import to_bytes

    # create temporary fact path
    fact_path = tempfile.mkdtemp()

    # invalid fact
    invalid_fact_path = os.path.join(fact_path, 'invalid.fact')
    with open(invalid_fact_path, 'wb') as f:
        f.write(to_bytes(u'\ufeff#!/usr/bin/env python\nprint "Hello Ansible!"'))
    os.chmod(invalid_fact_path, 0o755)

    # valid fact
    valid_fact_path = os.path.join(fact_path, 'valid.fact')

# Generated at 2022-06-13 03:02:53.016891
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():

    # Verify the constructor
    local_facts = LocalFactCollector()
    assert local_facts is not None

# Generated at 2022-06-13 03:02:59.139825
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    test_cases = list()
    with open('../../../test/units/module_utils/facts/collector/fixtures/local_facts.json', 'rt') as f:
        for line in f:
            test_cases.append(json.loads(line))

    for test_case in test_cases:
        args = test_case.get('args',{})
        lfc = LocalFactCollector(**args)
        local_facts = lfc.collect(**args.get('collect_args', {}))
        assert local_facts == test_case['local_facts']

# Generated at 2022-06-13 03:03:02.458970
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
   c = LocalFactCollector()
   assert (c.name == 'local')
   assert (c._fact_ids == set())

# Unit tests for collect() function in class LocalFactCollector
# when the fact_path is not specified

# Generated at 2022-06-13 03:03:06.087515
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    lfc = LocalFactCollector()
    results = lfc.collect()
    assert isinstance(results, dict)
    assert 'local' in results
    assert isinstance(results.get('local'), dict)

# Generated at 2022-06-13 03:03:07.317693
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    assert LocalFactCollector.name == 'local'

# Generated at 2022-06-13 03:03:11.680043
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    local_fact_collector = LocalFactCollector()
    assert local_fact_collector.name == 'local'
    assert local_fact_collector._fact_ids == set()
    assert local_fact_collector.collect() == {'local': {}}

# Generated at 2022-06-13 03:03:13.552475
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():

    assert LocalFactCollector.name == 'local'
    assert LocalFactCollector._fact_ids == set()

# Generated at 2022-06-13 03:03:20.325035
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    local_fact_collector = LocalFactCollector()
    assert isinstance(local_fact_collector, BaseFactCollector)
    assert hasattr(local_fact_collector, 'name')
    assert local_fact_collector.name == 'local'
    assert hasattr(local_fact_collector, '_fact_ids')
    assert isinstance(local_fact_collector._fact_ids, set)
    assert hasattr(local_fact_collector, 'collect')
    assert callable(local_fact_collector.collect)

# Generated at 2022-06-13 03:03:22.824353
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    local_facts = LocalFactCollector()
    assert local_facts.name == 'local'

# Generated at 2022-06-13 03:03:24.865635
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    lfc = LocalFactCollector()
    assert lfc.name == 'local'
    assert lfc._fact_ids == set()


# Generated at 2022-06-13 03:03:40.233763
# Unit test for method collect of class LocalFactCollector

# Generated at 2022-06-13 03:03:46.651060
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    file_path = os.path.dirname(__file__)
    fact_path = os.path.join(file_path, '../../../../test/units/module_utils/local_facts/')
    # AnsibleModule is not required here, but we don't have another way to get fact_path
    class MockAnsibleModule:
        params = {
            'fact_path': fact_path,
        }

        def warn(self, msg):
            pass

    local_facts = LocalFactCollector(MockAnsibleModule())
    assert local_facts.collect()['local']['fact1'] == 'value1'
    assert local_facts.collect()['local']['fact2'] == {'fact2_1': 'foo', 'fact2_2': 'bar'}
    assert local_facts.collect

# Generated at 2022-06-13 03:03:47.845008
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    assert isinstance(LocalFactCollector(), LocalFactCollector)

# Generated at 2022-06-13 03:03:50.009391
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    localFactCollector = LocalFactCollector()
    assert localFactCollector.name == 'local'
    assert isinstance(localFactCollector._fact_ids, set)


# Generated at 2022-06-13 03:04:00.682940
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    """Test the method LocalFactCollector.collect"""
    from ansible.module_utils.facts.collector import get_collector_class
    class MockedModule(object):
        def __init__(self, params):
            self.params = params
        def run_command(self, command):
            return 0, '', ''
    class MockedAnsibleModule(object):
        def __init__(self, **kwargs):
            self.params = kwargs
        def get_bin_path(self, executable, required=False, opt_dirs=[]):
            return executable
    mocked_module_params = {'ansible_module': MockedAnsibleModule, 'fact_path': 'tests/unit/modules/extras/test_facts/local_facts.d'}

# Generated at 2022-06-13 03:04:03.168015
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    local_fact_collector = LocalFactCollector()
    assert local_fact_collector.name == 'local'

# Generated at 2022-06-13 03:04:10.132992
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    # Constructor test
    local = LocalFactCollector()
    # Assert that the class is instance of BaseFactCollector
    assert isinstance(local, BaseFactCollector)
    # Assert that the class has a name
    assert local.name == 'local'
    # Assert that the class has a set object with fact ids
    assert isinstance(local._fact_ids, set)
    # Assert that the fact ids set is empty
    assert not local._fact_ids

if __name__ == '__main__':
    test_LocalFactCollector()

# Generated at 2022-06-13 03:04:13.281169
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    fc = LocalFactCollector()
    assert fc.name == 'local'

# Generated at 2022-06-13 03:04:16.056883
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    x = LocalFactCollector()
    assert x.name == 'local'
    assert x._fact_ids == {'local'}


# Generated at 2022-06-13 03:04:17.588201
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    l = LocalFactCollector()
    assert l.name == 'local'
    assert l._fact_ids == set()

# Generated at 2022-06-13 03:04:23.468593
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    pass # TODO: implement unit test

# Generated at 2022-06-13 03:04:34.086540
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    # Use mock
    from unittest.mock import MagicMock
    mock_module = MagicMock()
    mock_module.params = { 'fact_path': '/some/path/' }
    mock_module.run_command = MagicMock()

    # Create instances of required classes
    base_fact_collector = BaseFactCollector()
    local_fact_collector = LocalFactCollector(base_fact_collector)

    # Use mock
    import io
    import sys

    # Mock open builtin function
    mock_open = MagicMock()
    f = io.StringIO()
    fact_content = 'some_key: some_value'
    f.write(fact_content)
    mock_open.return_value = f

# Generated at 2022-06-13 03:04:34.865711
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    pass

# Generated at 2022-06-13 03:04:40.323367
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    # create object
    local_fact_collector_object = LocalFactCollector()
    # check if object is of instance BaseFactCollector
    assert isinstance(local_fact_collector_object, BaseFactCollector)
    # check if name is local
    assert local_fact_collector_object.name == "local"
    # check if fact_ids is a set()
    assert local_fact_collector_object._fact_ids == set()


# Generated at 2022-06-13 03:04:48.849911
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():

    import os

    test_dir = os.path.dirname(os.path.realpath(__file__))
    data_dir = os.path.join(test_dir, "..", "..", "data")
    ansible_local_facts_dir = os.path.join(data_dir, "facts.d")

    # Create Collector & set attributes
    lfc = LocalFactCollector()
    lfc.module = None

    # The test facts.d
    lfc.module.params = {'fact_path': ansible_local_facts_dir}

    # Run the collect method
    result = lfc.collect()

    # Expected result

# Generated at 2022-06-13 03:04:50.352504
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    collector = LocalFactCollector()
    assert collector.name == "local"
    assert isinstance(collector._fact_ids, set)

# Generated at 2022-06-13 03:04:52.538559
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    assert LocalFactCollector is not None

# Generated at 2022-06-13 03:04:56.748620
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    """Test constructor of class LocalFactCollector."""
    assert LocalFactCollector.name == "local"
    assert LocalFactCollector.priority == 80
    assert isinstance(LocalFactCollector._fact_ids, set)
    assert len(LocalFactCollector._fact_ids) == 0
    assert isinstance(LocalFactCollector.collect(), dict)

# Generated at 2022-06-13 03:04:58.610899
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    LF = LocalFactCollector()
    assert LF.name == 'local'
    assert LF._fact_ids == set()


# Generated at 2022-06-13 03:05:04.589326
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts import ansible_local
    from ansible.module_utils.facts.utils import get_file_content

    # Set up class object
    fact_path = os.path.dirname(os.path.realpath(__file__)) + '/utils/local/files'
    local_col = LocalFactCollector()
    local_col.name = 'local'

    # Test fact_path exists
    module = basic.AnsibleModule(
        argument_spec={
            'fact_path': {'type': 'path', 'required': True},
        },
    )
    module.params['fact_path'] = fact_path
    collected_facts = {}
    local_facts = local

# Generated at 2022-06-13 03:05:17.065868
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    lfc = LocalFactCollector()
    assert lfc.name == 'local'
    assert isinstance(lfc._fact_ids, set)

# Generated at 2022-06-13 03:05:19.002867
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    lfc = LocalFactCollector()
    # Test if method collect is returning a dictionary
    assert isinstance(lfc.collect(), dict)


# Generated at 2022-06-13 03:05:20.894550
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    local_fact_collector = LocalFactCollector()
    assert local_fact_collector
    assert local_fact_collector.name == "local"

# Generated at 2022-06-13 03:05:27.236397
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    # Parameters
    module_params = {
        'fact_path': '~/facts'
    }

    class Module:
        def __init__(self, params):
            self.params = params

        def run_command(self, cmd):
            return 0, '', ''

        def warn(self, str):
            self.warned = str

    module = Module(module_params)

    collector = LocalFactCollector()
    collected_facts = collector.collect(module)

    # Results
    assert collected_facts == {'local': {}}, 'Actual result does not match expected result.'

# Generated at 2022-06-13 03:05:36.643099
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    # Create a simple ansible module
    module = AnsibleModule(
        argument_spec={
            'fact_path': {'type': 'str', 'default': None},
        },
        supports_check_mode=True,
    )

    # Create expected result
    expected = {
        'local': {
            'ansible_test': {
                'test': 'test'
            }
        }
    }

    # Create collected_facts
    collected_facts = {}

    # Load LocalFactCollector
    import ansible.module_utils.facts.local as FactCollector

    # Instantiate LocalFactCollector
    fact_collector = FactCollector.LocalFactCollector()

    # Run LocalFactCollector method collect
    result = fact_collector.collect(module=module, collected_facts=collected_facts)



# Generated at 2022-06-13 03:05:41.254882
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    facts = LocalFactCollector()
    assert len(facts.collect()) == 0

    facts = LocalFactCollector({
        'fact_path': '/path/to/files',
        'module': MockModule(module_name='module',
                             path='/path/to/files'),
    })

    os.makedirs('/path/to/files')
    with open('/path/to/files/fact.fact', 'w') as f:
        f.write('FACT=value')

    assert len(facts.collect()) == 1
    assert 'local' in facts.collect()
    assert 'fact' in facts.collect()['local']
    assert facts.collect()['local']['fact']['FACT'] == 'value'
    os.unlink('/path/to/files/fact.fact')


# Generated at 2022-06-13 03:05:51.602694
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.utils import get_file_content
    import os
    import tempfile

    class module:
        def __init__(self, params):
            self.params = params
        def fail_json(self, msg, **kwargs):
            assert False, msg
        def warn(self, msg):
            pass
        def run_command(self, cmd):
            return 0, get_file_content(cmd), ''

    module_params = dict(
        fact_path = tempfile.mkdtemp(),
    )
    collector = Collector(module(module_params))
    collector.collect()
    facts = collector.get_facts()

    # directory does not exist

# Generated at 2022-06-13 03:05:53.179405
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    lfc = LocalFactCollector()
    assert lfc
    assert lfc.name == 'local'

# Generated at 2022-06-13 03:05:54.571634
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    local_fact_collector = LocalFactCollector()
    assert local_fact_collector.name == 'local'

# Generated at 2022-06-13 03:06:04.940858
# Unit test for method collect of class LocalFactCollector

# Generated at 2022-06-13 03:06:34.177384
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    import __main__
    from ansible.module_utils.facts.collector import get_collector_class
    local_fact_collector = get_collector_class('local')
    assert isinstance(local_fact_collector(), BaseFactCollector)

# Generated at 2022-06-13 03:06:35.859239
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    local_facts_collector = LocalFactCollector()
    assert local_facts_collector.name == 'local'

# Generated at 2022-06-13 03:06:36.946567
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    l = LocalFactCollector()
    assert l.name == 'local'

# Generated at 2022-06-13 03:06:52.785486
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():

    class Module(object):

        def __init__(self, params=None):
            self.params = {'fact_path': None}
            if params:
                self.params.update(params)

        def warn(self, msg):
            pass

    # CASE: When fact_path does not exists, then collect should return local_facts
    params = {'fact_path': 'not_existing_dir'}
    module = Module(params)
    lfc = LocalFactCollector()
    assert lfc.collect(module=module) == {'local': {}}

    # CASE: When fact_path exists, then collect should return the local_facts
    params = {'fact_path': './'}
    module = Module(params)
    lfc = LocalFactCollector()

# Generated at 2022-06-13 03:06:58.065943
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    fake_module = type('', (), {'run_command': run_command, 'params': {'fact_path': '.', 'provider': {'password': 'pass'}}})
    fake_module.params = {'fact_path': '.', 'provider': {'password': 'pass'}}
    base_fact_collector = BaseFactCollector()

    # Test case 1
    # Testing when fact_path is not provided
    local_fact_collector = LocalFactCollector(base_fact_collector)
    result = local_fact_collector.collect(fake_module, {})

    assert result == {}

    # Test case 2
    # Testing when fact_path is provided and file exists, and file has valid json

# Generated at 2022-06-13 03:07:02.151985
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    local_fact_obj = LocalFactCollector()
    attributes = {'params': {'fact_path': None}}
    local_fact_obj.collect(attributes, {})
    assert local_fact_obj.name == 'local'
    assert local_fact_obj._fact_ids == set()

# Generated at 2022-06-13 03:07:04.412986
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    assert LocalFactCollector.name == 'local'
    assert isinstance(LocalFactCollector._fact_ids, set)
    assert isinstance(LocalFactCollector.collect(), dict)

# Generated at 2022-06-13 03:07:06.361022
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    local = LocalFactCollector()
    local_facts = local.collect()
    assert local_facts['local'] == {}, 'Creation of object LocalFactCollector failed'

# Generated at 2022-06-13 03:07:08.211779
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    local_fact_collector = LocalFactCollector()
    assert local_fact_collector.name == 'local'

# Generated at 2022-06-13 03:07:09.255113
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():

    obj = LocalFactCollector()
    assert obj.name == 'local'

# Generated at 2022-06-13 03:08:14.689618
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():

    # test with empty state
    collector = LocalFactCollector()
    result = collector.collect()
    assert result == {'local': {}}

    # test with basic state
    class FakeModule(object):
        def __init__(self):
            self.params = {'fact_path': '/tmp'}
            self.warn = []
            self.run_command_results = [(0, '', '')]
        def warn(self, msg):
            self.warn.append(msg)
        def run_command(self, cmd):
            return self.run_command_results.pop(0)

    module = FakeModule()

    # test with nonexisting path
    module.run_command_results = [(0, '/tmp/a.fact', '')]
    result = collector.collect(module)

# Generated at 2022-06-13 03:08:16.207603
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    lfc = LocalFactCollector()
    assert lfc.name == 'local'
    assert len(lfc._fact_ids) == 0
    assert lfc.collect() == {}

# Generated at 2022-06-13 03:08:26.236197
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    import sys
    import os
    import tempfile
    local = sys.modules[__name__]

    m = MockModule()
    f = local.LocalFactCollector(m)

    # create a temp dir for data
    test_dir = tempfile.mkdtemp()
    os.chdir(test_dir)

    fact_path = '%s/local' % test_dir
    os.mkdir(fact_path)
    m.params = {'fact_path': fact_path}

    # create some data
    data = {'walrus': 5}
    with open('%s/walrus.fact' % fact_path, 'w') as fd:
        fd.write(json.dumps(data))

    # test fact
    local_facts = f.collect()
    assert 'local' in local

# Generated at 2022-06-13 03:08:27.468946
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    pass

# Generated at 2022-06-13 03:08:28.272226
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    local_fact_collector = LocalFactCollector()

    assert local_fact_collector.name == 'local'

# Generated at 2022-06-13 03:08:30.377635
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    argument_spec = dict(fact_path='/etc/ansible/facts.d')
    local_fact_collector = LocalFactCollector(argument_spec)
    assert local_fact_collector.name == 'local'

# Generated at 2022-06-13 03:08:32.177486
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    fact_c = LocalFactCollector()
    assert fact_c.name == 'local'

# Generated at 2022-06-13 03:08:39.803867
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    # Disable pylint warning due to https://github.com/PyCQA/pylint/issues/73
    class TestModule(object):  # pylint: disable=too-few-public-methods
        ''' test class for AnsibleModule '''
        def __init__(self):
            self.params = dict()

        def run_command(self, cmd):
            return (0, 'test fact', '')

        def warn(self, msg):
            pass

    test_module = TestModule()
    test_facts = LocalFactCollector(module=test_module).collect()
    assert test_facts == {'local': {'test': 'test fact'}}

# Generated at 2022-06-13 03:08:48.194307
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():

    import os
    from ansible.module_utils.facts.facts import Facts

    from test.units.module_utils.facts.facts_fixture import (
        FactsFixture,
        fake_file_content,
    )

    #def fake_module_params_get(self, key, default=None):
    #    if key == 'fact_path':
    #        return '/tmp/path'

    #def fake_run_command(fn):
    #    rc, out, err = 0, 'out', 'err'
    #    return rc, out, err

    #def fake_is_file(self, path):
    #    return True

    #def fake_exists(self, path):
    #    return True

    #def fake_get_file_content(self, path):
    #    return path.replace

# Generated at 2022-06-13 03:08:49.391460
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    obj = LocalFactCollector()
    assert obj.name == 'local'
    assert obj._fact_ids == set()

# Generated at 2022-06-13 03:10:57.145763
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    import pytest
    from ansible.module_utils.facts import FactsCollector

    fc = FactsCollector()
    local_facts = fc.collect(module=None, collected_facts=None)

    assert local_facts == {'local': {u'helloworld': u'Hello World'}}

# Generated at 2022-06-13 03:10:58.939513
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    module = AnsibleModule(argument_spec=dict(fact_path=dict(type='str')))
    result = LocalFactCollector.collect(module=module)
    assert isinstance(result, dict)

# Generated at 2022-06-13 03:11:08.011533
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    fact_path = '/test/path/'
    fact_path2 = ''
    fact_path3 = '/test/path/'
    local_fact = LocalFactCollector(fact_path)
    local_fact2 = LocalFactCollector(fact_path2)
    local_fact3 = LocalFactCollector(fact_path3)
    assert local_fact._fact_ids == set(['local'])
    assert local_fact2._fact_ids == set(['local'])
    assert local_fact3._fact_ids == set(['local'])
    assert local_fact.name is 'local'
    assert local_fact2.name is 'local'
    assert local_fact3.name is 'local'
    assert local_fact._fact_path is '/test/path/'
    assert local_fact2._fact_

# Generated at 2022-06-13 03:11:09.728126
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    test = LocalFactCollector()
    assert test.name == 'local'
    assert isinstance(test._fact_ids, set)

# Generated at 2022-06-13 03:11:11.152015
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    x = LocalFactCollector()
    assert x.name == 'local'
    assert x._fact_ids == set()

# Generated at 2022-06-13 03:11:12.726319
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    localFactCollectorObj = LocalFactCollector()
    assert localFactCollectorObj.name == 'local', 'Failed to create LocalFactCollector class'

# Generated at 2022-06-13 03:11:13.917064
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    local_fact_collector = LocalFactCollector()
    assert local_fact_collector.name == 'local'
    assert isinstance(local_fact_collector._fact_ids, set)


# Generated at 2022-06-13 03:11:19.270170
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    from ansible.module_utils.facts.collector import AnsibleModule
    import tempfile

    fn = tempfile.mktemp()

    try:
        with open(fn, "w") as f:
            data = '{"a_fact": "a_value"}'
            f.write(data)

        module = AnsibleModule(argument_spec={})
        mod_params = {'fact_path': fn}
        module.params = mod_params
        local = LocalFactCollector()

        facts = local.collect(module)
        assert facts['local']['a_fact'] == 'a_value'
    finally:
        os.remove(fn)

# Generated at 2022-06-13 03:11:24.220354
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    """
    Test LocalFactCollector.collect()
    """
    # Create a str object
    s = str
    # Create a instance of class LocalFactCollector
    local_fact_collector = LocalFactCollector()
    # Call method collect of LocalFactCollector
    result = local_fact_collector.collect()
    # Check the result
    assert isinstance(result, dict)
    assert isinstance(result.get('local', None), dict)
    assert not result['local']

# Generated at 2022-06-13 03:11:24.533927
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    pass