

# Generated at 2022-06-13 03:01:52.641980
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    fc = LocalFactCollector()
    result = fc.collect()
    assert result == {'local': {}}

# Generated at 2022-06-13 03:01:54.899613
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    o = LocalFactCollector()
    assert o.name == 'local'
    assert isinstance(o.name, str)

# Generated at 2022-06-13 03:01:56.142908
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    local_facts = LocalFactCollector()
    assert local_facts.name == 'local'

# Generated at 2022-06-13 03:02:02.688783
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    # Create a Mock Module
    module = type('', (object,), {
        'run_command': lambda x: (0, '{"name": "tests.ansible.com"}', ''),
        'warn': lambda x: None,
        'params': {
            'fact_path': '/tmp/ansible_facts'
        }
    })

    # Create a collector and call the collect method
    local_fact_collector = LocalFactCollector()
    facts = local_fact_collector.collect(module)

    # Check the facts is the one that we expect
    assert facts == {
        'local': {
            'test_fact': {"name": "tests.ansible.com"}
        }
    }

# Generated at 2022-06-13 03:02:14.516752
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    # Create a mock object
    class MockObject(object):
        def __init__(self, *args, **kwargs):
            pass

        def __getattr__(self, name):
            return super(MockObject, self).__getattr__(name)

    mock = MockObject()

    # Create an instance of the real class on which we are going to test the method collect
    local_fact_collector = LocalFactCollector()
    # Execute the method collect
    local_facts = local_fact_collector.collect(mock)
    # Check the result
    assert isinstance(local_facts, dict)
    assert isinstance(local_facts['local'], dict)
    assert isinstance(local_facts['local']['ansible_python_version'], int)

# Generated at 2022-06-13 03:02:21.668052
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    fact_path = './test_fixtures/module_utils/network/common/facts/local_facts'
    module_params = {
        'fact_path': fact_path
    }

    module = object()
    module.run_command = lambda x: (0, '', '')
    local_facts = LocalFactCollector().collect(module,
                                               module_params)
    assert local_facts['local']['ansible_local']['foo'] == 'bar'

# Generated at 2022-06-13 03:02:34.249191
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    module = object()
    fact_path = '/home/ansible'
    fact_file = 'facts.fact'
    file = fact_path + '/' + fact_file
    test_fact = 'test'
    to_text_value = b'\xe5\xa4\xa7\xe5\xae\x89\xe5\xbe\xbd'
    to_text_return_value = u'大安徽'

    def run_command(command):
        return 0, '', ''

    module.params = {'fact_path': fact_path}
    module.run_command = run_command

    class Parameter:
        def __init__(self, filename, fact_base, fact, warn, test_fact, file, to_text_return_value):
            self.filename = filename
           

# Generated at 2022-06-13 03:02:36.664813
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    local_collector = LocalFactCollector()
    assert local_collector.name == 'local'
    assert local_collector._fact_ids == set()


# Generated at 2022-06-13 03:02:43.316366
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():

    class MockLocalFactCollector(LocalFactCollector):
        def __init__(self):
            self.facts_collected = []

        def collect(self, module=None, collected_facts=None):
            facts = super(MockLocalFactCollector, self).collect(module=module, collected_facts=collected_facts)

            # Add each fact to the list of the facts collected
            for k,v in facts.items():
                self.facts_collected.append(k)

            return facts

    # Initialize the collector
    local_fact_collector = MockLocalFactCollector()

    # Assert that the collector collects the local facts
    assert 'local' in local_fact_collector.facts_collected

# Generated at 2022-06-13 03:02:52.200230
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    m = MockModule()
    m.params = dict(
        fact_path=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data/facts.d')
    )
    local_fact = LocalFactCollector()
    result = local_fact.collect(m)
    assert result['local']['one']['attr'] == '1'
    assert result['local']['two']['attr1'] == '2'
    assert result['local']['two']['attr2'] == '3'
    assert result['local']['test1'] == "[1, 2, 'test']"
    assert result['local']['test2'] == '{"test2": "test2"}'

# Generated at 2022-06-13 03:03:07.204108
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    fact_path = os.path.join(os.path.dirname(__file__), 'test-facts')
    local_facts = LocalFactCollector(fact_path)
    assert isinstance(local_facts, LocalFactCollector)

# Generated at 2022-06-13 03:03:13.712006
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    mock_module = {
        "run_command.return_value": (0, "test_out", ""),
        "warn.return_value": None,
        "params" : { "fact_path" : "/tmp/mock" }
    }
    mock_collector = {
        "get_file_content.return_value": "test_file_content",
        "to_text.return_value": "test_text"
    }
    mock_json = {
        "loads.return_value": "test_loads"
    }

# Generated at 2022-06-13 03:03:22.589158
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    from ansible.module_utils.facts.collector import AnsibleFactCollector
    from ansible.module_utils.facts import BaseFactCollector
    from ansible.module_utils.facts.collector import DictMerge
    from ansible.module_utils.facts.collector import BaseFileFactCollector
    from ansible.module_utils.facts.collector import _get_collectors
    from ansible.module_utils.facts.collector import get_collector_class
    from ansible.module_utils._text import to_text
    from ansible.module_utils.basic import AnsibleModule 
    import os
    import tempfile
    import sys
    import json
    import os
    import shutil
    import stat
    import glob
    import configparser


# Generated at 2022-06-13 03:03:24.024042
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    local_facts = LocalFactCollector()
    assert local_facts.name == 'local'
    assert local_facts._fact_ids == set()


# Generated at 2022-06-13 03:03:32.961633
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils import basic
    from ansible.module_utils.facts import ansible_collector

    m = basic.AnsibleModule(
        argument_spec = dict(
            fact_path=dict(type='str', required=True, default=None),
        ),
        supports_check_mode=True,
    )

    # Success (all files under fact dir with data)
    m.params['fact_path'] = os.path.join(os.path.dirname(__file__), 'fixtures/fact_files')

    c = ansible_collector.get_collector('local')
    facts = c.collect(m)

    assert facts['local'] == {'test_fact': {'test_attribute': 'success'}}

   

# Generated at 2022-06-13 03:03:36.686044
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    local_fact_collector = LocalFactCollector()
    assert isinstance(local_fact_collector, LocalFactCollector)
    assert local_fact_collector.name == 'local'
    assert local_fact_collector._fact_ids == set()

# Generated at 2022-06-13 03:03:38.862271
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    module = MockModule()
    local_facts = LocalFactCollector()
    local_facts.collect(module)
    assert(local_facts.name == 'local')


# Generated at 2022-06-13 03:03:40.033911
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    x = LocalFactCollector()
    assert x.name == "local"

# Generated at 2022-06-13 03:03:41.494097
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    assert LocalFactCollector.name == 'local'
    assert LocalFactCollector._fact_ids is not None

# Generated at 2022-06-13 03:03:42.561652
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    local_fc = LocalFactCollector()
    assert local_fc is not None

# Generated at 2022-06-13 03:03:57.883365
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    local_fact_collector = LocalFactCollector()
    assert local_fact_collector.name == 'local'
    assert isinstance(local_fact_collector._fact_ids, set)


# Generated at 2022-06-13 03:03:59.140087
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    assert True

# Generated at 2022-06-13 03:04:00.349995
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    test_obj = LocalFactCollector()
    assert test_obj.name == "local"

# Generated at 2022-06-13 03:04:02.226816
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():


    c = LocalFactCollector()
    assert c.name == 'local'

# Generated at 2022-06-13 03:04:11.561218
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    """test_LocalFactCollector_collect"""

    # Variables initialization
    fact_path = "test_LocalFactCollector_collect"
    fact_file1 = "test_LocalFactCollector_collect/test_fact.fact"
    fact_file2 = "test_LocalFactCollector_collect/test_exec.fact"

# Generated at 2022-06-13 03:04:21.064914
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
# Test case 1
    module = AnsibleModule(
        argument_spec=dict(
            fact_path=dict(type='str', default=None),
            filter=dict(type='list', elements='str', default='*'),
            gather_subset=dict(type='list', elements='str', default=['all'])
        )
    )

    local_facts = [{'local': {u'host': {u'ansible_python_version': 3, u'ansible_python_version_full': u'3.5.6'}}}]
    module.params.update({'fact_path': '/home/ansible/facts'})

    assert local_facts == LocalFactCollector.collect(module)


# Generated at 2022-06-13 03:04:21.427532
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    assert False

# Generated at 2022-06-13 03:04:22.496314
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    local_fact_collector = LocalFactCollector()
    assert local_fact_collector

# Generated at 2022-06-13 03:04:33.087722
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    fact_path = '.ansible/tmp/facts'
    os.mkdir(os.path.join('.ansible', 'tmp'))
    os.mkdir(fact_path)
    git_fact = os.path.join(fact_path, 'git.fact')
    touch_fact = os.path.join(fact_path, 'touch.fact')
    os.mknod(git_fact)

# Generated at 2022-06-13 03:04:34.821020
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    lc = LocalFactCollector()
    assert lc.name == 'local'
    assert lc._fact_ids == set()


# Generated at 2022-06-13 03:05:09.642831
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    # Test Param setup
    module = type('', (), {'params': {'fact_path': 'test_local_facts/test_fact_path'},
                            'run_command': {}, 'warn': {}})()

    # Test run
    local_fact_collector = LocalFactCollector()
    local_facts = local_fact_collector.collect(module=module)

    # Test Asserts
    assert local_facts['local']["test_fact"]["test_fact_key"] == "test_fact_value"
    assert local_facts['local']["test_fact"]["test_fact_key_2"] == "test_fact_value_2"

# Generated at 2022-06-13 03:05:12.014895
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    assert isinstance(LocalFactCollector(), LocalFactCollector)

# Generated at 2022-06-13 03:05:13.363011
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    x = LocalFactCollector()
    assert x.name == 'local'
    assert x._fact_ids == set()
    assert x.priority == 99

# Generated at 2022-06-13 03:05:14.959018
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    d = LocalFactCollector()
    assert d.name == 'local'
    assert d._fact_ids == set()

# Generated at 2022-06-13 03:05:23.248466
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    module = MockModule()
    module.params['fact_path'] = '../../facts/library/facts.d'
    module.run_command = MockRunCommand()

    actual = LocalFactCollector.collect(module)

# Generated at 2022-06-13 03:05:25.070217
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    lfc = LocalFactCollector()
    assert lfc.name == 'local'
    assert lfc._fact_ids == set()

# Generated at 2022-06-13 03:05:26.504632
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    local_fact_collector_obj = LocalFactCollector()
    assert local_fact_collector_obj

# Generated at 2022-06-13 03:05:28.475681
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    x = LocalFactCollector()
    assert x.name == 'local'
    assert x._fact_ids == set()


# Generated at 2022-06-13 03:05:31.728201
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    '''Unit test for constructor of class LocalFactCollector'''
    local_fact_collector = LocalFactCollector()
    assert local_fact_collector is not None

# Generated at 2022-06-13 03:05:33.609497
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    lfc = LocalFactCollector()
    assert lfc.name == 'local'
    assert lfc._fact_ids == set()


# Generated at 2022-06-13 03:06:48.747754
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    fact_path = '/tmp/test_facts'
    module = type('', (), {})()
    module.params = {
        'fact_path': fact_path
    }
    collector = LocalFactCollector()
    result = collector.collect(module=module)
    assert result


# Generated at 2022-06-13 03:06:50.129317
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    local_fact = LocalFactCollector()
    assert local_fact.name == 'local'
    assert local_fact._fact_ids == set()

# Generated at 2022-06-13 03:06:50.532765
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    pass

# Generated at 2022-06-13 03:06:51.615229
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    local_fact_collector = LocalFactCollector()
    assert local_fact_collector.collect() == {}

# Generated at 2022-06-13 03:06:54.963802
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    # Test module load
    test_module = AnsibleModule(argument_spec=dict(
        fact_path=dict(required=True),
    ))
    # Create Instance of LocalFactCollector
    fact_collector = LocalFactCollector()
    fact_collector.collect(module=test_module)
    # test local facts creation
    assert 'local' in fact_collector.collect(module=test_module)


# Generated at 2022-06-13 03:07:01.447420
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
   result = LocalFactCollector().collect()
   assert 'local' in result
   assert result['local'] == {
       'ansible_env': {
           'HOME': '/home/tower',
       },
       'ansible_python_version': {
           'major': 2,
           'minor': 7,
           'micro': 5,
           'releaselevel': 'final',
           'serial': 0,
       },
       'ansible_machine_id': 'ea9b91453a7f4a16a41eb3b8d8c0b7e2',
       'ansible_python_executable': '/usr/bin/python',
       'ansible_processor_vcpus': 8,
       'ansible_processor_count': 4,
   }

# Generated at 2022-06-13 03:07:03.058948
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    local = LocalFactCollector()
    assert local.name == 'local'
    assert local._fact_ids == set()

# Generated at 2022-06-13 03:07:21.127311
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    from ansible.module_utils._text import to_bytes
    from ansible.utils.display import Display
    from ansible.module_utils.facts import ansible_local_facts
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector
    from ansible.module_utils.facts.system.distribution.freebsd import FreeBSDDistributionFactCollector
    from ansible.module_utils.facts.system.distribution.smartos import SmartOSDistributionFactCollector
    from ansible.module_utils.facts.utils import exec_file_ext
    from ansible.module_utils.facts.utils import get_file_content
    import os
    import tempfile

    # fixtures
    display = Display()
    test_fact_path = '/tmp/test/fixtures/facts'

    # produce a temporary

# Generated at 2022-06-13 03:07:25.298197
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    localFactCollector=LocalFactCollector()

    params = {}
    params['fact_path'] = '/etc/ansible/facts.d/'

    try:
        localFactCollector.collect(params)
    except Exception as e:
        assert False, "collect method of LocalFactCollector class throw exception: " + str(e)

    # TODO: check local_fact result

    assert True

# Generated at 2022-06-13 03:07:28.318403
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    local = LocalFactCollector()
    assert local.name == 'local'
    assert local._fact_ids == set()

# Generated at 2022-06-13 03:10:08.160369
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
  assert LocalFactCollector().name == 'local'

# Generated at 2022-06-13 03:10:16.329583
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    # this is mostly to get a coverage report
    import os
    test_file = '/tmp/test_LocalFactCollector_collect.fact'
    with open(test_file, 'w') as f:
        f.write('[section1]\noption1: value1\noption2: value2\n')

    try:
        fc = LocalFactCollector()
        facts = fc.collect()
        assert('local' in facts)
        assert(isinstance(facts['local'], dict))
        assert('test_LocalFactCollector_collect' in facts['local'])
        assert(isinstance(facts['local']['test_LocalFactCollector_collect'], dict))

    finally:
        os.unlink(test_file)

# Generated at 2022-06-13 03:10:27.577947
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    local_fact_collector_instance = LocalFactCollector()
    assert local_fact_collector_instance.name == 'local'


# Generated at 2022-06-13 03:10:29.128537
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    module = AnsibleModule()
    local_fact_collector = LocalFactCollector()
    assert local_fact_collector.collect(module) == dict()

# Generated at 2022-06-13 03:10:30.868220
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    lfc = LocalFactCollector()
    assert lfc.name == 'local'
    assert isinstance(lfc._fact_ids, set)

# Generated at 2022-06-13 03:10:39.511244
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    lfc = LocalFactCollector('test')
    lfc.collect()

# Generated at 2022-06-13 03:10:45.469607
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    from ansible.module_utils.common._collections_compat import Mapping
    os.environ['ANSIBLE_FACT_CACHE'] = '/tmp'
    os.environ['ANSIBLE_FACT_CACHE_PLUGIN'] = 'jsonfile'
    os.environ['ANSIBLE_FACT_CACHE_PLUGIN_CONNECTION'] = '{}'
    dict = {u'test1': u'fact1', u'test2': u'fact2'}
    module = Mock()
    module.params = dict
    module.run_command = Mock()
    module.run_command.return_value = [0, '{"test1": "fact1", "test2": "fact2"}', '']
    module.warn = Mock()
    module.warn.return_value = None

# Generated at 2022-06-13 03:10:46.359277
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    assert LocalFactCollector.name == 'local'

# Generated at 2022-06-13 03:10:50.708175
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    module = None
    collected_facts = None

    fact_path = ''
    module_params = {'fact_path':fact_path}

    local_fact_collector = LocalFactCollector()
    local_facts = local_fact_collector.collect(module, collected_facts)
    assert local_facts['local'] == {}


# Generated at 2022-06-13 03:10:53.941026
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    LFC = LocalFactCollector()
    assert 'local' == LFC.name
    assert LFC._fact_ids == set()