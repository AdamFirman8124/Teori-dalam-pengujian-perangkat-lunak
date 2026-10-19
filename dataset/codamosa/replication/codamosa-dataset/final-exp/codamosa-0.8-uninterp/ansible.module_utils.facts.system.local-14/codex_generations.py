

# Generated at 2022-06-13 03:01:57.125386
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    localFactCollector = LocalFactCollector()
    assert localFactCollector is not None

# Generated at 2022-06-13 03:01:57.987023
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    assert LocalFactCollector.name == 'local'

# Generated at 2022-06-13 03:02:09.781415
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    from ansible.module_utils.facts import ModuleFactCollector
    from ansible.module_utils.facts import get_collected_facts
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.utils import get_file_content
    import os
    import tempfile

    fact_base = 'test_fact'
    fact_path = tempfile.mkdtemp()
    fact_file = fact_path + '/' + fact_base + '.fact'

    fact_json = '{"fact1": "value1"}'
    fact_ini = "[Section]\nfact2=value2"
    fact_str = 'Test fact'
    fact_bin = to_bytes(12345)


# Generated at 2022-06-13 03:02:12.713815
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():

    r = LocalFactCollector()
    assert(r.name == 'local')
    assert(len(r._fact_ids) == 1)

# Generated at 2022-06-13 03:02:16.262468
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    # Create an object of LocalFactCollector
    lc = LocalFactCollector()

    # Check the name of the object
    assert lc.name == 'local'

# Generated at 2022-06-13 03:02:16.855031
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    pass

# Generated at 2022-06-13 03:02:18.662052
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    # Create instance of BaseFactCollector with parameters.
    BaseFactCollector.__init__()


# Generated at 2022-06-13 03:02:26.314743
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    testsys = {
        'ansible_facts': {
            'system': {
                'name': 'system1',
            }
        }
    }
    mod = {
        'params': {
            'fact_path': './test/unittests/module_utils/facts/collectors/local'
        },
        'warn': lambda x: print(x)
    }
    # test non-existent fact_path
    c = LocalFactCollector()
    facts = c.collect(module=mod, collected_facts=testsys)
    assert facts == {'local': {}}
    # test when fact_path is empty
    mod['params']['fact_path'] = ''
    facts = c.collect(module=mod, collected_facts=testsys)
    assert facts == {'local': {}}
    #

# Generated at 2022-06-13 03:02:29.790911
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    local_fact_collector = LocalFactCollector()
    assert local_fact_collector.name == 'local'
    assert isinstance(local_fact_collector._fact_ids, set)

# Generated at 2022-06-13 03:02:31.670057
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    test_instance = LocalFactCollector()
    assert test_instance.name == 'local'

# Generated at 2022-06-13 03:02:40.587378
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    local_fact_collector = LocalFactCollector()
    assert local_fact_collector.collect() == {'local': {}}

# Generated at 2022-06-13 03:02:42.142683
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():

    testclass = LocalFactCollector()

    assert testclass.name == 'local'
    assert 'local' in testclass._fact_ids

# Generated at 2022-06-13 03:02:51.874183
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    # create a fake module
    class FakeModule:
        def __init__(self):
            self.params = {}
        def run_command(self, cmd):
            return 0, '', ''
    fake_module = FakeModule()
    # test with fact_path defined, but not existing
    local_fact_collector = LocalFactCollector()
    collected_facts = local_fact_collector.collect(fake_module)
    assert 'local' in collected_facts
    assert len(collected_facts['local']) == 0
    # test with existing fact_path
    fake_module.params['fact_path'] = '../../../lib/ansible/module_utils/facts/facts.d/'
    collected_facts = local_fact_collector.collect(fake_module)
    assert 'local' in collected_facts


# Generated at 2022-06-13 03:02:59.138710
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    import os
    import sys

    # Note: The following is a very complex test case. It's not meant to test the collection of facts.
    # Instead, it's meant to test how the facts collection reacts on broken/malicious inpupt.
    # For example: Malicious input could be a file that tries to execute a fork bomb and hangs the current ansible run.
    # This test case is meant to detect such problems.
    # These problems are very hard to detect during the development. Therefore the tests are done in a very complex manner.
    # The test data is stored in the directory ./test_data.
    # The test data can be created with the helper script ./test_data/create_test_data.py.
    # The file structure of the data directory is as follows:
    # /test_data
    #   /test_cases
    #      /test

# Generated at 2022-06-13 03:03:02.830261
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    assert LocalFactCollector._fact_ids == set()
    a = LocalFactCollector()
    assert a.name == 'local'
    assert a._fact_ids == set(['local']) or a._fact_ids == set(['local', 'ansible_local'])

# Generated at 2022-06-13 03:03:11.577819
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    import json
    import tempfile
    from ansible.module_utils.facts.utils import FactsCollector
    from ansible.module_utils.facts import collector
    from ansible.module_utils._text import to_bytes

    conf_json = {
        "local": {
            "custom-fact": '{ "foo": "bar" }',
        }
    }

    conf_ini = {
        "local": {
            "custom-fact-2": '[custom-fact-2]\n'
                             'key=value',
            "custom-fact-3": '[custom-fact-3]\n'
                             'key="value"',
            "custom-fact-4": ''
        }
    }

    def set_up_conf(conf):
        temp = tempfile.mkdtemp()

# Generated at 2022-06-13 03:03:14.449466
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    lfc = LocalFactCollector()

    # test for class attributes
    assert lfc.name == 'local'
    assert lfc._fact_ids == set()


# Generated at 2022-06-13 03:03:18.937855
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    module = AnsibleModule(argument_spec=dict(fact_path=dict(default='/tmp/ansible_facts')))
    fact_path = module.params.get('fact_path', None)
    local_fact_collector = LocalFactCollector()
    assert local_fact_collector.collect(module) == {'local': {}}

# Generated at 2022-06-13 03:03:30.383466
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    import tempfile

    test_fact = tempfile.NamedTemporaryFile(mode='w+t', delete=False)
    fake_fact_path = test_fact.name[:-5] + '*'
    print(fake_fact_path)
    local_fact = '{"test_fact": "test"}'
    test_fact.write(local_fact)
    test_fact.close()

    m = MockModule()
    lfc = LocalFactCollector()
    results = lfc.collect(module=m, fact_path=fake_fact_path)['local']
    assert results['test_fact'] == {'test_fact': 'test'}

    os.remove(test_fact.name)

# This class is used for Unit test for method collect of class LocalFactCollector

# Generated at 2022-06-13 03:03:40.506266
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():

    # The format for test cases is:
    #     {
    #        'inputs': {      - Test case inputs
    #            'module': {} - module argument
    #        },
    #        'exp_out': {     - Expected outputs
    #            'local': {}
    #        }
    #     }

    test_cases = [
        {
            'inputs': {
                'module': {
                    'run_command': lambda command: (
                        0,
                        '{"fact": "value"}',
                        ''
                    )
                }
            },
            'exp_out': {
                'local': {
                    'path': {
                        'fact': 'value'
                    }
                }
            }
        }
    ]


# Generated at 2022-06-13 03:03:54.414873
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    localFactCollector = LocalFactCollector()
    assert localFactCollector is not None

# Generated at 2022-06-13 03:03:57.248155
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    # create a LocalFactCollector object
    lf = LocalFactCollector()
    # confirm it is an instance of LocalFactCollector
    assert(hasattr(lf, 'collect'))

# Generated at 2022-06-13 03:03:59.789040
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():

    localFactCollector = LocalFactCollector()

    assert localFactCollector.name == 'local'
    assert localFactCollector._fact_ids == set()

# Generated at 2022-06-13 03:04:04.043845
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    fact_path = 'tests/unit/modules/test_fact_path'
    module = AnsibleModule(argument_spec={'fact_path': {'type': 'str', 'required': True}}, params={'fact_path': fact_path})
    assert LocalFactCollector(module)

# Generated at 2022-06-13 03:04:07.968769
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    d = LocalFactCollector()
    assert d

    assert d.name == 'local'
    assert d.fact_subset == ['!all', '!facter', '!ohai', 'local']
    assert d._fact_ids == set()

# Test the collect() function of class LocalFactCollector

# Generated at 2022-06-13 03:04:10.255577
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    a = LocalFactCollector()
    assert len(a.name) > 0
    assert len(a._fact_ids) == 0
    assert len(a.collect()) == 0

# Generated at 2022-06-13 03:04:15.015122
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    local_fact_collector = LocalFactCollector()
    assert local_fact_collector.name == 'local'
    assert local_fact_collector._fact_ids == set()


# Generated at 2022-06-13 03:04:18.014092
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    Module = type('Module', (object,), {'params': {}, 'warn': None})
    module = Module()
    module.run_command = lambda fn: (1, "error", "out")
    module.warn = lambda msg: None
    local_fc = LocalFactCollector()
    assert local_fc.collect(module) == {'local': {'test': 'error loading fact - output of running "test" was not utf-8'}}

# Generated at 2022-06-13 03:04:21.812126
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    local_fact_collector = LocalFactCollector()
    assert isinstance(local_fact_collector, LocalFactCollector)
    assert isinstance(local_fact_collector.name, str)
    assert local_fact_collector.name == 'local'
    assert isinstance(local_fact_collector._fact_ids, set)

# Generated at 2022-06-13 03:04:22.675164
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    assert LocalFactCollector().name == 'local'

# Generated at 2022-06-13 03:04:47.276791
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    # FIXME
    assert False, "Test not implemented"

# Generated at 2022-06-13 03:04:49.389658
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    local_fact_collector = LocalFactCollector('/usr/path')
    assert local_fact_collector.name == 'local'
    assert len(local_fact_collector._fact_ids) == 0

# Generated at 2022-06-13 03:04:54.357331
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    # given
    fact_path = os.path.join(os.getcwd(), "lib/ansible/module_utils/facts/local")
    tmp_file = '/tmp/test_file'
    tmp_content = "test_file"

    # when
    local_collector = LocalFactCollector()
    facts = {'module': {'params': {'fact_path': fact_path}}}
    with open(tmp_file, 'w') as f:
      f.write(tmp_content)

    output = local_collector.collect(facts)

    # then
    os.remove(tmp_file)
    assert output['local']['test']['content'] == tmp_content

# Generated at 2022-06-13 03:04:59.427117
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    fact_collector = LocalFactCollector()

    # test name
    name = fact_collector.name
    assert name == 'local'

    # test excluded_facts
    excluded_facts = fact_collector.excluded_facts
    assert excluded_facts == set()

    # test fact_ids
    fact_ids = fact_collector.fact_ids
    assert fact_ids == set()

# Generated at 2022-06-13 03:04:59.795480
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    pass

# Generated at 2022-06-13 03:05:01.061493
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    local_collector = LocalFactCollector()
    assert local_collector.name == "local"

# Generated at 2022-06-13 03:05:10.567034
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    from ansible.module_utils.facts.utils import AnsibleModule
    from ansible.module_utils.facts.collector import BaseFactCollector

    ansible_module = AnsibleModule(
        argument_spec={ 'fact_path': dict(default='/etc/ansible', type='str')},
        supports_check_mode=True
    )

    ansible_module.params = {
        'fact_path': '/Users/jane.doe/ansible/facts',
        'gather_subset': ['all']
    }

    local_fact_collector = LocalFactCollector(ansible_module)
    facts = local_fact_collector.collect()


# Generated at 2022-06-13 03:05:21.021620
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts import FactCollector

    module_mock = Mock()
    module_mock.params = {
        'fact_path': '/usr/local'
    }
    module_mock.run_command = Mock()
    module_mock.run_command.side_effect = ['{"fact1": "value1"}', '{"fact2": "value2"}']

    local_fact_collector = LocalFactCollector(module=module_mock)
    assert isinstance(local_fact_collector, LocalFactCollector) is True

    result = local_fact_collector.collect()

    assert result['local']['fact1'] == 'value1'

# Generated at 2022-06-13 03:05:21.424409
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    assert True

# Generated at 2022-06-13 03:05:29.993591
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    import os

    test_path = os.path.dirname(__file__) + "/../../lib/ansible/module_utils/facts"
    test_path = to_bytes(test_path, errors='surrogate_or_strict')
    file_path = os.path.join(test_path, "test.fact")
    file_content = "some random content"
    open(file_path, 'w').write(file_content)

    # Generate fake module.params
    setattr(basic.AnsibleModule, 'params', {'fact_path': test_path})

    # create a file in fact_path
    local_facts = LocalFactCollector()
    facts = local_facts.collect

# Generated at 2022-06-13 03:06:32.019474
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    pass

# Ansible-style gather_facts call

# Generated at 2022-06-13 03:06:35.304750
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    expected = LocalFactCollector()
    assert expected.name == 'local'
    assert expected._fact_ids == set()

# Generated at 2022-06-13 03:06:36.433035
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    l = LocalFactCollector()
    assert l.name == 'local'

# Generated at 2022-06-13 03:06:44.276991
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    fact_path = '/home/vagrant/ansible/test/unit/module_utils/facts/platform/test_local_facts/test_local_facts'
    module = AnsibleModule(argument_spec={'fact_path': {'type': 'str', 'default': fact_path}})
    local_facts = LocalFactCollector().collect(module=module)
    assert local_facts['local']
    assert len(local_facts['local'].keys()) == 3
    assert local_facts['local']['not_executable']['key'] == 'value'
    assert local_facts['local']['not_executable_json']['key'] == 'value'
    assert local_facts['local']['executable'] == 'executable'

# Generated at 2022-06-13 03:06:47.144324
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    f = LocalFactCollector()
    assert f.name == 'local'


# Generated at 2022-06-13 03:06:49.291422
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    x = LocalFactCollector()
    assert x.collect() == { u'local': {} }

# Generated at 2022-06-13 03:07:05.955030
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    fact_path = "fake/path"
    fail_msg = "Could not execute fact script (fake/path"

    import ansible.module_utils.facts.collectors.local as local
    def get_file_content(fn, default=""):
        if fn == fact_path + "/fake.fact":
            return '{"version": "1.0.0"}'
        elif fn == fact_path + "/fake_script.fact":
            return '#!/bin/sh\necho "hello"'
        else:
            return default
    local.get_file_content = get_file_content

    class RunCommand(object):
        def __init__(self, rc, out, err):
            self.rc = rc
            self.out = out
            self.err = err

# Generated at 2022-06-13 03:07:07.261410
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    lfc = LocalFactCollector()
    assert lfc.name == 'local'

# Generated at 2022-06-13 03:07:12.411501
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    ''' local.py:test_LocalFactCollector '''
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    import ansible.module_utils.facts.collector

    m = basic.AnsibleModule(
        argument_spec={
            "fact_path": {
                "default": "/tmp/facts.d",
                "type": 'str'
            }
        },
        supports_check_mode=True,
    )

    # Run constructor test
    testobj = ansible.mo

# Generated at 2022-06-13 03:07:21.585545
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    test_module = AnsibleModule(argument_spec={
        'fact_path': dict(required=False, type='path', default=None)
    })
    local_facts_collector = LocalFactCollector()
    result = local_facts_collector.collect(test_module)
    assert(result['local']['test_facter_script'] == 'facter')
    assert(result['local']['test_json_file'] == {
        'test': {
            'test_json_file': 'True'
        }
    })
    assert(result['local']['test_ini_file'] == {
        'test': {
            'test_ini_file': 'True'
        }
    })


# Generated at 2022-06-13 03:09:42.927129
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    result = LocalFactCollector()
    assert result
    assert result.name == 'local'
    assert result._fact_ids == set()



# Generated at 2022-06-13 03:09:47.797729
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    class TestModule:
        def __init__(self, params):
            self.params = params

    test_module = TestModule({})
    LocalFactCollector().collect(test_module)

# Generated at 2022-06-13 03:09:54.491686
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    module = FakeAnsibleModule(
        params={'fact_path': 'examples/facts.d'}
    )

    local_fact_collector = LocalFactCollector()
    result = local_fact_collector.collect(module)
    assert result['local'] == {
        'special_variable': {
            'key': 'value'
        },
        'special_variable_json': {
            'key': 'value'
        },
        'key_has_dots': {
            'key': 'value'
        },
        'empty_key_has_dots': {
            'key': 'value'
        }
    }


# Generated at 2022-06-13 03:09:59.302627
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    # Arrange
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts import ansible_local
    from ansible.module_utils import basic
    module = basic.AnsibleModule(argument_spec=dict(fact_path=dict()))
    module.params = {'fact_path': os.path.join(os.path.dirname(ansible_local.__file__), 'facts.d')}
    module.warn = lambda x: None
    module.run_command = lambda x: (0, '{"example": "fact"}', '')
    local_fact_collector = LocalFactCollector()

    # Act
    facts = local_fact_collector.collect(module=module)
    # Assert
    if 'local' not in facts:
        raise Exception

# Generated at 2022-06-13 03:10:09.145551
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    import ansible.constants as C
    import ansible.module_utils.facts.collectors.local as local

    # If a fact has 'local.test_fact' as its identifier, it will not be returned
    # by collect() if we have already seen it.  For unit tests, we only
    # run collect() once, so we can just set that set to empty.
    local.LocalFactCollector._fact_ids.clear()

    # Create a Module object
    _module = ansible.module_utils.basic.AnsibleModule(
        argument_spec={
            'fact_path': {'type': 'path', 'required': False, 'default': '/etc/ansible/facts.d'},
        }
    )

    # Create a LocalFactCollector object
    _localFactCollector = local.LocalFactCollector()

# Generated at 2022-06-13 03:10:11.240264
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    local_facts = LocalFactCollector()
    assert local_facts.name == 'local'
    assert local_facts._fact_ids == set()

# Generated at 2022-06-13 03:10:14.088019
# Unit test for constructor of class LocalFactCollector
def test_LocalFactCollector():
    d = LocalFactCollector()
    assert d.name == 'local'
    assert d._fact_ids == set()

# Generated at 2022-06-13 03:10:21.185893
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    f = LocalFactCollector()

    result = f.collect()
    assert result['local'] == {}

    opt_fact_path = os.path.join(os.path.abspath('.'), 'lib/ansible/module_utils/facts/local/')
    result = f.collect(module=object, module_params={'fact_path': opt_fact_path})
    assert 'local' in result
    assert 'test_fact' in result['local']
    assert result['local']['test_fact'] == 'test fact'
    assert 'test_fact_no_ext' in result['local']
    assert result['local']['test_fact_no_ext'] == 'test fact no ext'
    assert 'test_fact_json' in result['local']

# Generated at 2022-06-13 03:10:25.457241
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    test_module = {
        'params': {
            'fact_path': '.'
        },
        'warn': lambda x: None,
        'run_command': lambda x: (0, '{"foo": "bar"}', '')
    }

    fact_collector = LocalFactCollector()
    fact_collector.collect(test_module)
    assert 'local' in fact_collector.collect(test_module)

# Generated at 2022-06-13 03:10:32.085620
# Unit test for method collect of class LocalFactCollector
def test_LocalFactCollector_collect():
    # Setup
    local_fact_collector = LocalFactCollector()
    module = AnsibleModule(argument_spec={
        'fact_path': {'type': 'str', 'required': False, 'default': 'custom-fact-path'}
    })
    module.run_command = Mock(return_value=(0, '{}', ''))
    # No file so we should get an empty result
    result = local_fact_collector.collect(module)
    assert result == {'local': {}}

    # Create file to test .fact extension
    factfile = NamedTemporaryFile(suffix='.fact', delete=False)
    factfile.close()
    result = local_fact_collector.collect(module)
    # Test that we have file
    assert os.path.exists(factfile.name)
   