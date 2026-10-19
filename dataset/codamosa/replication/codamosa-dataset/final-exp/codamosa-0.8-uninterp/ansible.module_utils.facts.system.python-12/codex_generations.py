

# Generated at 2022-06-13 03:12:21.561075
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = PythonFactCollector()
    result = python_facts.collect()
    assert result['python']['version']['major'] == sys.version_info[0]
    assert result['python']['version']['minor'] == sys.version_info[1]
    assert result['python']['version']['micro'] == sys.version_info[2]
    assert result['python']['version']['releaselevel'] == sys.version_info[3]
    assert result['python']['version']['serial'] == sys.version_info[4]
    assert result['python']['version_info'] == list(sys.version_info)
    assert result['python']['executable'] == sys.executable
    assert result['python']['has_sscontext'] == HAS_SS

# Generated at 2022-06-13 03:12:38.284797
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector()
    facts = fact_collector.collect()
    assert facts['python']['version']['major'] == sys.version_info[0]
    # There are no assertNotEqual in Python 2, reusing assertIsNotNone
    assert facts['python']['version']['minor'] is not None
    assert facts['python']['version']['micro'] == sys.version_info[2]
    assert facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert facts['python']['version']['serial'] == sys.version_info[4]
    assert facts['python']['version_info'] == list(sys.version_info)
    assert facts['python']['executable'] == sys.executable
   

# Generated at 2022-06-13 03:12:52.395878
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pc = PythonFactCollector()
    facts = pc.collect()
    assert 'python' in facts
    assert isinstance(facts['python'], dict)
    assert 'version' in facts['python']
    assert 'version_info' in facts['python']
    assert 'executable' in facts['python']

# Generated at 2022-06-13 03:12:57.335035
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    collector = PythonFactCollector({})
    facts = collector.collect(module=None, collected_facts=None)
    assert facts['python']['version']['major'] == sys.version_info[0]
    assert facts['python']['version']['minor'] == sys.version_info[1]
    assert facts['python']['version']['micro'] == sys.version_info[2]
    assert facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert facts['python']['version']['serial'] == sys.version_info[4]
    assert facts['python']['version_info'] == list(sys.version_info)
    assert facts['python']['executable'] == sys.executable
    assert facts['python']['type']

# Generated at 2022-06-13 03:13:01.402387
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Test that PythonFactCollector.collect() returns a dictionary
    fact_collector_instance = PythonFactCollector()
    result = fact_collector_instance.collect()
    assert isinstance(result, dict)

    # Test that PythonFactCollector.collect() returns expected keys
    result_keys = set(result.keys())
    expected_result_keys = set(('python'))
    assert result_keys == expected_result_keys


# Generated at 2022-06-13 03:13:12.702296
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact_collector = PythonFactCollector()
    python_facts = python_fact_collector.collect()
    assert python_facts['python']['version']['major'] == sys.version_info[0]
    assert python_facts['python']['version']['minor'] == sys.version_info[1]
    assert python_facts['python']['version']['micro'] == sys.version_info[2]
    assert python_facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert python_facts['python']['version']['serial'] == sys.version_info[4]
    assert python_facts['python']['version_info'] == list(sys.version_info)

# Generated at 2022-06-13 03:13:21.176477
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    try:
        from ssl import create_default_context, SSLContext
        del create_default_context
        del SSLContext
        has_sslcontext = True
    except ImportError:
        has_sslcontext = False

    # This test expect python major version 2 or 3, and minor version 6 or 7
    assert sys.version_info[0] == 2 or sys.version_info[0] == 3
    assert sys.version_info[1] == 6 or sys.version_info[1] == 7


# Generated at 2022-06-13 03:13:25.980928
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    c = PythonFactCollector()
    assert isinstance(c.collect(), dict)
    assert 'python' in c.collect()
    assert 'version' in c.collect()['python']
    assert isinstance(c.collect()['python']['version'], dict)
    assert 'version_info' in c.collect()['python']
    assert isinstance(c.collect()['python']['version_info'], list)


# Generated at 2022-06-13 03:13:32.785437
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_collector = PythonFactCollector()
    collected_facts = python_collector.collect()

    assert len(collected_facts) == 1
    assert 'python' in collected_facts
    assert 'type' in collected_facts['python']
    assert 'version' in collected_facts['python']
    assert len(collected_facts['python']['version']) == 5
    assert 'executable' in collected_facts['python']
    assert 'has_sslcontext' in collected_facts['python']



# Generated at 2022-06-13 03:13:36.163879
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Create a PythonFactCollector object for testing.
    python_fact_collector = PythonFactCollector()
    # Make sure the python fact collector is not empty.
    assert(python_fact_collector.collect() != {})

# Generated at 2022-06-13 03:13:43.859827
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    facts_result = {}
    fact_collector = PythonFactCollector()
    result = fact_collector.collect(collected_facts=facts_result)
    assert result['python'] == facts_result['ansible_python']
    assert 'version' in result['python']
    assert 'version_info' in result['python']

# Generated at 2022-06-13 03:13:52.098504
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_obj = PythonFactCollector()
    result = python_obj.collect()
    assert result['python']['version']['major'] == sys.version_info[0]
    assert result['python']['version']['minor'] == sys.version_info[1]
    assert result['python']['version']['micro'] == sys.version_info[2]


if __name__ == '__main__':
    test_PythonFactCollector_collect()

# Generated at 2022-06-13 03:13:58.115396
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector()
    python_facts = fact_collector.collect()
    assert 'ansible_python' in python_facts
    assert 'version' in python_facts['ansible_python']
    assert 'version_info' in python_facts['ansible_python']
    assert 'executable' in python_facts['ansible_python']
    assert 'type' in python_facts['ansible_python']

# Generated at 2022-06-13 03:14:05.519226
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    from ansible.module_utils.facts import collect
    from ansible.module_utils.facts.collector import Collector

    # Mock modules which are automatically loaded by the module loader.
    # We want to make sure collect only collects the python fact and not
    # the other facts as well.
    module_finder = collect.get_module_finder()
    mock_module_names = ['aiohttp', 'ansible.module_utils.facts.system',
                         'ansible.module_utils.facts.virtual',
                         'ansible.module_utils.facts.legacy']
    mock_module_finder = collect.MockModuleFinder(module_finder, mock_module_names)
    mock_module_loader = collect.ModuleLoader(mock_module_finder)

    # Collect the facts.
    python_collector = PythonFactCollector

# Generated at 2022-06-13 03:14:12.203780
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    # We need to mock the facts module to be able to assert on it
    import ansible.module_utils.facts.facts
    import copy
    old_facts = copy.deepcopy(ansible.module_utils.facts.facts.FACTS)

    # Run the collect method
    import ansible.module_utils.facts.collectors.python
    ansible.module_utils.facts.collectors.python.PythonFactCollector().collect()

    # Cleanup
    ansible.module_utils.facts.facts.FACTS = old_facts

    # Assert on the facts

# Generated at 2022-06-13 03:14:19.273040
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    collector = PythonFactCollector()
    python_facts = collector.collect()
    assert isinstance(python_facts, dict)
    assert 'python' in python_facts
    assert isinstance(python_facts['python'], dict)
    assert 'version' in python_facts['python']
    assert 'version_info' in python_facts['python']
    assert 'executable' in python_facts['python']
    assert 'has_sslcontext' in python_facts['python']

# Generated at 2022-06-13 03:14:28.625632
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = PythonFactCollector().collect()
    assert python_facts['python']['executable'] == sys.executable
    assert python_facts['python']['version']['major'] == sys.version_info[0]
    assert python_facts['python']['version']['minor'] == sys.version_info[1]
    assert python_facts['python']['version']['micro'] == sys.version_info[2]
    assert python_facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert python_facts['python']['version']['serial'] == sys.version_info[4]

# Generated at 2022-06-13 03:14:34.509184
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_collector = PythonFactCollector(None, None)
    python_facts = python_collector.collect()
    assert python_facts == {'python': {
        'version': {
            'major': sys.version_info[0],
            'minor': sys.version_info[1],
            'micro': sys.version_info[2],
            'releaselevel': sys.version_info[3],
            'serial': sys.version_info[4]
        },
        'version_info': list(sys.version_info),
        'executable': sys.executable,
        'has_sslcontext': HAS_SSLCONTEXT,
        'type': 'CPython'
    }}

# Generated at 2022-06-13 03:14:38.756056
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    from ansible.module_utils.facts.collector import get_collector_instance
    fact_collector = get_collector_instance(PythonFactCollector)
    python_facts = fact_collector.collect()
    assert python_facts['python']['has_sslcontext'] == HAS_SSLCONTEXT

# Generated at 2022-06-13 03:14:41.292871
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_collector = PythonFactCollector()
    python_facts = python_collector.collect()
    assert isinstance(python_facts, dict)

# Generated at 2022-06-13 03:14:57.746959
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact_collector = PythonFactCollector()
    fact_result = python_fact_collector.collect()

    assert fact_result['python']['version_info'][0] == sys.version_info[0]
    assert fact_result['python']['version_info'][1] == sys.version_info[1]
    assert fact_result['python']['version_info'][2] == sys.version_info[2]
    assert fact_result['python']['version_info'][3] == sys.version_info[3]
    assert fact_result['python']['version_info'][4] == sys.version_info[4]
    assert fact_result['python']['version']['major'] == sys.version_info[0]

# Generated at 2022-06-13 03:15:04.872958
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pyfc = PythonFactCollector()
    py_facts = pyfc.collect()
    assert 'python' in py_facts
    assert 'version' in py_facts['python']
    assert 'version_info' in py_facts['python']
    assert 'executable' in py_facts['python']
    assert 'type' in py_facts['python']
    assert 'has_sslcontext' in py_facts['python']
    assert 'has_sslcontext' in py_facts['python']

# Generated at 2022-06-13 03:15:13.400530
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    tf = PythonFactCollector()
    assert isinstance(tf.collect(), dict)

# Generated at 2022-06-13 03:15:18.717893
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Check if the collect method of class PythonFactCollector return the correct result
    python_facts = PythonFactCollector().collect()
    assert python_facts['python'] is not None
    assert python_facts['python']['version'] is not None
    assert python_facts['python']['version_info'] is not None
    assert python_facts['python']['version']['major'] == sys.version_info[0]
    assert python_facts['python']['version']['minor'] == sys.version_info[1]
    assert python_facts['python']['version']['micro'] == sys.version_info[2]
    assert python_facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert python_facts['python']['version']['serial']

# Generated at 2022-06-13 03:15:26.050854
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    from ansible.module_utils.facts.collector import get_collector_instance, AnsibleCollector
    # As we are using the same facts as the Ansible module, we do not need to test it
    del AnsibleCollector
    ipf = get_collector_instance('python')
    assert ipf.get_facts() == {'python': {'version': {'micro': 4, 'releaselevel': 'final', 'major': 2, 'serial': 0, 'minor': 7}, 'version_info': [2, 7, 4, 'final', 0], 'executable': '/usr/bin/python', 'has_sslcontext': False, 'type': 'CPython'}}

# Generated at 2022-06-13 03:15:33.833779
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # mock the collect method
    instance = PythonFactCollector()
    assert instance.collect() == \
        {'python': {
            'version': {
                'major': sys.version_info[0],
                'minor': sys.version_info[1],
                'micro': sys.version_info[2],
                'releaselevel': sys.version_info[3],
                'serial': sys.version_info[4]
            },
            'version_info': list(sys.version_info),
            'executable': sys.executable,
            'has_sslcontext': HAS_SSLCONTEXT
        }}

# Generated at 2022-06-13 03:15:39.403573
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    """
    Test :meth:`ansible.module_utils.facts.system.python.PythonFactCollector.collect`
    """
    # Test functionality when HAS_SSLCONTEXT is true
    sys.version_info = (2, 7, 12, 'final', 0)
    sys.executable = '/usr/bin/python'
    sys.subversion = ('CPython', '', '')
    python_fact_collector = PythonFactCollector()

# Generated at 2022-06-13 03:15:44.204161
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    c = PythonFactCollector()
    r = {'python': {'has_sslcontext': True, 'executable': '/usr/bin/python', 'version_info': [2, 7, 5, 'final', 0], 'type': 'CPython', 'version': {'releaselevel': 'final', 'serial': 0, 'major': 2, 'minor': 7, 'micro': 5}}}
    assert r == c.collect()

# Generated at 2022-06-13 03:15:57.486633
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    assert PythonFactCollector.collect() == {'python': {'version': {'major': 2, 'micro': 5, 'minor': 2, 'releaselevel': 'final', 'serial': 0}, 'executable': '/usr/bin/python', 'version_info': [2, 2, 5, 'final', 0], 'type': 'CPython', 'has_sslcontext': False}}

# Generated at 2022-06-13 03:16:07.242870
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    from ansible.module_utils import basic

    python_facts = PythonFactCollector().collect()
    module = basic.AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )
    facts = module.params['ansible_facts']
    assert facts['python']['has_sslcontext'] == python_facts['python']['has_sslcontext']
    assert facts['python']['executable'] == python_facts['python']['executable']
    assert facts['python']['version']['micro'] == python_facts['python']['version']['micro']
    assert facts['python']['version']['major'] == python_facts['python']['version']['major']

# Generated at 2022-06-13 03:16:31.029315
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = PythonFactCollector().collect()
    assert 'version' in python_facts['python']
    assert python_facts['python']['version']['major'] == sys.version_info[0]
    assert python_facts['python']['version']['major'] == sys.version_info[0]
    assert python_facts['python']['version']['minor'] == sys.version_info[1]
    assert python_facts['python']['version']['micro'] == sys.version_info[2]
    assert python_facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert python_facts['python']['version']['serial'] == sys.version_info[4]

# Generated at 2022-06-13 03:16:38.314856
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    # Test default values
    python_facts = PythonFactCollector().collect()
    assert python_facts['python']['version']['major'] == 3
    assert python_facts['python']['version']['minor'] == 6
    assert python_facts['python']['version']['micro'] == 5
    assert python_facts['python']['version']['releaselevel'] == 'final'
    assert python_facts['python']['version']['serial'] == 0
    assert python_facts['python']['version_info'] == [3, 6, 5, 'final', 0]

    # Test py27 legacy
    python_facts = PythonFactCollector().collect(collected_facts=dict(python=dict(version=dict(major='2', minor='7'))))

# Generated at 2022-06-13 03:16:43.279729
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    c = PythonFactCollector()
    assert c.collect() == {'python':
                           {'version': {'major': sys.version_info[0],
                                        'minor': sys.version_info[1],
                                        'micro': sys.version_info[2],
                                        'releaselevel': sys.version_info[3],
                                        'serial': sys.version_info[4]},
                            'version_info': list(sys.version_info),
                            'executable': sys.executable,
                            'has_sslcontext': HAS_SSLCONTEXT,
                            'type': 'CPython' if sys.version_info[0] == 2 else 'CPython3'}}

# Generated at 2022-06-13 03:16:48.972559
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = {}

    # Arrange
    # Act
    python_facts = PythonFactCollector().collect()

    # Assert

    # Version
    if sys.version_info[0] < 3:
        assert python_facts['python']['version']['major'] == 2
        assert python_facts['python']['version']['minor'] == 7
        assert python_facts['python']['version']['micro'] == 5
        assert python_facts['python']['version']['releaselevel'] == 'final'
        assert python_facts['python']['version']['serial'] == 0
    else:
        assert python_facts['python']['version']['major'] == 3
        assert python_facts['python']['version']['minor'] == 4
        assert python_facts

# Generated at 2022-06-13 03:16:59.559741
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pf = PythonFactCollector()
    result = pf.collect()
    assert 'python' in result
    assert result['python']['version']['major'] == sys.version_info[0]
    assert result['python']['version']['minor'] == sys.version_info[1]
    assert result['python']['version']['micro'] == sys.version_info[2]
    assert result['python']['version']['releaselevel'] == sys.version_info[3]
    assert result['python']['version']['serial'] == sys.version_info[4]
    assert result['python']['version_info'] == list(sys.version_info)
    assert result['python']['executable'] == sys.executable

# Generated at 2022-06-13 03:17:09.277413
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    my_test_python_fact_collector = PythonFactCollector()
    result = my_test_python_fact_collector.collect()
    expected_result = {'python': {
        'version': {
            'major': sys.version_info[0],
            'minor': sys.version_info[1],
            'micro': sys.version_info[2],
            'releaselevel': sys.version_info[3],
            'serial': sys.version_info[4]
        },
        'version_info': list(sys.version_info),
        'executable': sys.executable,
        'has_sslcontext': HAS_SSLCONTEXT
    }}


# Generated at 2022-06-13 03:17:18.324778
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Test with no argument 'module'
    python_facts = PythonFactCollector().collect()
    assert python_facts['python']['version']['major'] == sys.version_info[0]
    assert python_facts['python']['version']['minor'] == sys.version_info[1]
    assert python_facts['python']['version']['micro'] == sys.version_info[2]
    assert python_facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert python_facts['python']['version']['serial'] == sys.version_info[4]
    assert python_facts['python']['version_info'] == list(sys.version_info)
    assert python_facts['python']['executable'] == sys.executable
   

# Generated at 2022-06-13 03:17:25.071844
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Test the collect method of class PythonFactCollector
    py_fc = PythonFactCollector()
    result = py_fc.collect()

    ver = result['python']['version']
    assert ver['major'] == sys.version_info[0]
    assert ver['minor'] == sys.version_info[1]
    assert ver['micro'] == sys.version_info[2]
    assert ver['releaselevel'] == sys.version_info[3]
    assert ver['serial'] == sys.version_info[4]

    assert result['python']['version_info'] == list(sys.version_info)
    assert result['python']['executable'] == sys.executable
    assert result['python']['has_sslcontext'] == HAS_SSLCONTEXT


# Generated at 2022-06-13 03:17:29.926434
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.collector import BaseFactCollector

    PythonFactCollector.collect()
    BaseFactCollector.collect(Collector())
    BaseFactCollector.collect()
    BaseFactCollector.collect(module=None)
    BaseFactCollector.collect(collected_facts=None)


# Generated at 2022-06-13 03:17:36.253143
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    class CollectedFacts(dict):
        pass

    collected_facts = CollectedFacts()

    collector = PythonFactCollector()
    assert collector.collect(collected_facts=collected_facts) == {
        'python': {
            'executable': sys.executable,
            'has_sslcontext': HAS_SSLCONTEXT,
            'version': {
                'major': sys.version_info[0],
                'minor': sys.version_info[1],
                'micro': sys.version_info[2],
                'releaselevel': sys.version_info[3],
                'serial': sys.version_info[4]
            },
            'version_info': list(sys.version_info),
            'type': sys.implementation.name
        }
    }

# Generated at 2022-06-13 03:17:52.080222
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector()
    result = fact_collector.collect()
    assert result['python']['version_info'][0] == sys.version_info[0]
    assert result['python']['version_info'][1] == sys.version_info[1]
    assert result['python']['version_info'][2] == sys.version_info[2]
    assert result['python']['version_info'][3] == sys.version_info[3]
    assert result['python']['version_info'][4] == sys.version_info[4]
    assert result['python']['version']['major'] == sys.version_info[0]
    assert result['python']['version']['minor'] == sys.version_info[1]

# Generated at 2022-06-13 03:17:55.137367
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector()
    collected_facts = {}
    collected_facts = pfc.collect(collected_facts=collected_facts)
    assert isinstance(collected_facts, dict)

# Generated at 2022-06-13 03:18:01.313135
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    collector = PythonFactCollector()
    python_facts = collector.collect()

    assert isinstance(python_facts, dict)
    assert 'python' in python_facts
    assert 'version' in python_facts['python']
    assert isinstance(python_facts['python']['version'], dict)
    assert 'version_info' in python_facts['python']
    assert isinstance(python_facts['python']['version_info'], list)
    assert 'executable' in python_facts['python']
    assert 'type' in python_facts['python']

# Generated at 2022-06-13 03:18:03.673139
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    x = PythonFactCollector()
    y = x.collect(module=None, collected_facts={})
    assert isinstance(y['python'],dict)

# Generated at 2022-06-13 03:18:10.729801
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = PythonFactCollector().collect()
    assert python_facts['python']['version'] == {
        'major': sys.version_info[0],
        'minor': sys.version_info[1],
        'micro': sys.version_info[2],
        'releaselevel': sys.version_info[3],
        'serial': sys.version_info[4]
    }
    assert python_facts['python']['version_info'] == list(sys.version_info)
    assert python_facts['python']['executable'] == sys.executable
    assert python_facts['python']['has_sslcontext'] == HAS_SSLCONTEXT

# Generated at 2022-06-13 03:18:15.903888
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_collector = PythonFactCollector()

    python_facts_result = python_collector.collect()
    assert python_facts_result['python']['version']['major'] == sys.version_info[0]
    assert python_facts_result['python']['version']['minor'] == sys.version_info[1]
    assert python_facts_result['python']['version']['micro'] == sys.version_info[2]
    assert python_facts_result['python']['version']['releaselevel'] == sys.version_info[3]
    assert python_facts_result['python']['version']['serial'] == sys.version_info[4]
    assert python_facts_result['python']['version_info'] == list(sys.version_info)
    assert python_

# Generated at 2022-06-13 03:18:25.216293
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    import unittest
    import ansible.module_utils.facts.collector.python
    testcase_dict = {
        'python': {
            'version': {
                'major': sys.version_info[0],
                'minor': sys.version_info[1],
                'micro': sys.version_info[2],
                'releaselevel': sys.version_info[3],
                'serial': sys.version_info[4]
            },
            'version_info': list(sys.version_info),
            'executable': sys.executable,
            'has_sslcontext': HAS_SSLCONTEXT
        }
    }

# Generated at 2022-06-13 03:18:27.304133
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    c = PythonFactCollector()
    assert isinstance(c.collect(), dict)
    assert 'version_info' in c.collect()['python']

# Generated at 2022-06-13 03:18:34.571506
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    expected_facts = {
        'python': {
            'executable': sys.executable,
            'has_sslcontext': HAS_SSLCONTEXT,
            'version': {'major': sys.version_info[0],
                        'micro': sys.version_info[2],
                        'minor': sys.version_info[1],
                        'releaselevel': sys.version_info[3],
                        'serial': sys.version_info[4]},
            'version_info': list(sys.version_info),
            'type': sys.implementation.name
        }
    }

    assert PythonFactCollector().collect() == expected_facts

# Generated at 2022-06-13 03:18:35.736126
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector()
    assert 'python' in pfc.collect()

# Generated at 2022-06-13 03:18:54.459108
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    factCollector = PythonFactCollector()
    factCollector.collect()

# Generated at 2022-06-13 03:18:58.650149
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """ test the PythonFactCollector.collect method"""
    # assert that we get the expected version info
    # note that we don't check for the releaselevel and serial as those can
    # differ depending on the Python version, e.g. for 3.4.2:
    # ansible --version: ('3', '4', '2', 'final', 0)
    # python -c 'import sys; print(sys.version_info)' ('3', '4', '2', 'final', 0)
    # python --version: 3.4.2 (default, Sep  4 2016, 03:33:39) [GCC 5.4.0 20160609]

    import sys
    from ansible.module_utils.facts.collector import BaseFactCollector
    pc = PythonFactCollector()
    pc.collect()

# Generated at 2022-06-13 03:19:00.515889
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    PythonFactCollector().collect()

# Generated at 2022-06-13 03:19:04.375314
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    import sys
    # get a fresh instance of PythonFactCollector
    pfc = PythonFactCollector()
    pfc.collect()

    # make assertions about the results
    assert isinstance(pfc.name, str)
    assert isinstance(pfc.collect(), dict)

# Generated at 2022-06-13 03:19:10.186368
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector()
    assert fact_collector.collect() == {'python': {'version': {'major': sys.version_info[0], 'minor': sys.version_info[1],
        'micro': sys.version_info[2], 'releaselevel': sys.version_info[3], 'serial': sys.version_info[4]},
        'version_info': list(sys.version_info),
        'executable': sys.executable,
        'has_sslcontext': HAS_SSLCONTEXT,
        'type': '%s' % sys.version.split('[')[0].strip()}}

# Generated at 2022-06-13 03:19:15.371368
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    collector = PythonFactCollector()
    result = collector.collect()
    assert result
    assert type(result) is dict
    assert 'python' in result
    assert result['python']
    assert type(result['python']) is dict
    assert 'version' in result['python']
    assert result['python']['version']
    assert type(result['python']['version']) is dict
    assert 'major' in result['python']['version']
    assert type(result['python']['version']['major']) is int
    assert result['python']['version']['major'] == sys.version_info[0], \
        "Python major version is not the returned value of sys.version_info[0]"
    assert 'minor' in result['python']['version']

# Generated at 2022-06-13 03:19:20.139502
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    collector = PythonFactCollector()
    fact = collector.collect()
    assert fact['python']['has_sslcontext'] == HAS_SSLCONTEXT
    assert fact['python']['version']['major'] == sys.version_info[0]

# Generated at 2022-06-13 03:19:21.755427
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector()
    pfc.collect()
    assert isinstance(pfc.collect(), dict)

# Generated at 2022-06-13 03:19:30.021058
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    py_collected_facts = {'ansible_local': {'python': {'version': {'major': 2,
                                                                    'minor': 7,
                                                                    'micro': 5,
                                                                    'releaselevel': u'standard',
                                                                    'serial': 0},
                                                      'executable': 'test_python',
                                                      'has_sslcontext': True,
                                                      'type': 'CPython'}}}
    py_collector = PythonFactCollector()
    assert py_collected_facts['ansible_local']['python'] == py_collector.collect()['ansible_local']['python']


# Generated at 2022-06-13 03:19:31.156188
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector()
    fact_collector.collect()

# Generated at 2022-06-13 03:20:10.521641
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Tests the collect method
    from ansible.module_utils.facts.collector import BaseFactCollector
    import sys
    import platform
    import os

    # Construct a mock 'ansible.module_utils.facts.collector.BaseFactCollector' class
    class MockBaseFactCollector(BaseFactCollector):

        def __init__(self, *args, **kwargs):
            BaseFactCollector.__init__(self, *args, **kwargs)
            self.collectors = ['python', 'redhat', 'system']

        def build_collector_list(self, module=None, collected_facts=None):
            return self.collectors

    class MockRedHatFactCollector(BaseFactCollector):

        def __init__(self, *args, **kwargs):
            BaseFactCollector.__init__

# Generated at 2022-06-13 03:20:11.887824
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector(None)
    pfc.collect()



# Generated at 2022-06-13 03:20:15.343322
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    python_facts = PythonFactCollector()
    facts = python_facts.collect()

    assert 'python' in facts
    assert 'version' in facts['python']
    assert 'version_info' in facts['python']
    assert 'executable' in facts['python']
    assert 'has_sslcontext' in facts['python']
    assert 'type' in facts['python']

# Generated at 2022-06-13 03:20:21.241500
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector()
    fact_data = fact_collector.collect()
    assert fact_data is not None
    assert fact_data['python']['executable'] == sys.executable
    assert fact_data['python']['version']['major'] == sys.version_info[0]
    assert fact_data['python']['version']['minor'] == sys.version_info[1]
    assert fact_data['python']['version']['micro'] == sys.version_info[2]
    assert fact_data['python']['version']['releaselevel'] == sys.version_info[3]
    assert fact_data['python']['version']['serial'] == sys.version_info[4]
    assert fact_data['python']['version_info']

# Generated at 2022-06-13 03:20:30.153953
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact_collector = PythonFactCollector()

    python_facts = python_fact_collector.collect()

    assert 'python' in python_facts
    assert 'version' in python_facts['python']
    assert 'version_info' in python_facts['python']
    assert 'executable' in python_facts['python']
    assert 'type' in python_facts['python']
    assert 'has_sslcontext' in python_facts['python']
    assert 'version' in python_facts['python']

    assert isinstance(python_facts['python']['version']['major'], int)
    assert isinstance(python_facts['python']['version_info'], list)
    assert isinstance(python_facts['python']['executable'], str)

# Generated at 2022-06-13 03:20:39.754741
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Object PythonFactCollector is created
    # Dictionary with values for facts is returned
    assert PythonFactCollector().collect() == {
        'python': {
            'version': {
                'major': (sys.version_info[0]),
                'minor': (sys.version_info[1]),
                'micro': (sys.version_info[2]),
                'releaselevel': (sys.version_info[3]),
                'serial': (sys.version_info[4]),
            },
            'version_info': list(sys.version_info),
            'executable': sys.executable,
            'type': sys.subversion[0] if hasattr(sys, 'subversion') else sys.implementation.name,
            'has_sslcontext': HAS_SSLCONTEXT
        }
    }

# Generated at 2022-06-13 03:20:47.123228
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact_collector = PythonFactCollector()
    collected_facts = {}
    result = python_fact_collector.collect(collected_facts=collected_facts)
    assert type(result['python']) is dict
    assert type(result['python']['version']) is dict
    assert type(result['python']['version']['major']) is int
    assert type(result['python']['version']['minor']) is int
    assert type(result['python']['version']['micro']) is int
    assert type(result['python']['version']['releaselevel']) is str
    assert type(result['python']['version']['serial']) is int
    assert type(result['python']['version_info']) is list

# Generated at 2022-06-13 03:20:48.132551
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector()
    fact_collector.collect()

# Generated at 2022-06-13 03:20:57.390120
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    import sys
    import unittest

    class MockModule(object):
        def __init__(self, shell, python_env=None, executable=None):
            self.shell = shell
            self.python_env = python_env
            self.executable = executable

    class MockOS(object):
        @staticmethod
        def path():
            class MockPath(object):
                @staticmethod
                def exists(path):
                    if path == 'fakepath':
                        return False
                    else:
                        return True
            return MockPath

    class MockExecutable(object):
        pass

    class MockSys(object):
        pass

    _collector = PythonFactCollector()

    class TestPythonFactCollector(unittest.TestCase):
        def test_SysExecutable(self):
            _collector.sys = MockSys

# Generated at 2022-06-13 03:21:01.464409
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    result = dict()

    python_facts = PythonFactCollector().collect()
    for key in python_facts:
        val = python_facts[key]
        result[key] = val

    assert 'python' in result
    assert 'version' in result['python']
    assert 'version_info' in result['python']
    assert 'executable' in result['python']
    assert 'has_sslcontext' in result['python']

    return result

# Generated at 2022-06-13 03:21:43.580850
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    import sys
    import sysconfig
    python_version_info = sys.version_info
    python_version = '.'.join([str(i) for i in python_version_info[0:3]])
    pypy_prefix = ''
    if python_version_info[0] == 3:
        pypy_prefix = 'pypy3'
    elif python_version_info[0] == 2:
        pypy_prefix = 'pypy'

# Generated at 2022-06-13 03:21:49.497596
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python = PythonFactCollector()

    # create a mock dict to store facts collected
    test_dict = dict()

    # call method collect
    returned_dict = python.collect(collected_facts=test_dict)

    assert returned_dict is None
    assert test_dict["python"]["version"]["major"] == sys.version_info[0]
    assert test_dict["python"]["version"]["minor"] == sys.version_info[1]
    assert test_dict["python"]["version"]["micro"] == sys.version_info[2]
    assert test_dict["python"]["version"]["releaselevel"] == sys.version_info[3]
    assert test_dict["python"]["version"]["serial"] == sys.version_info[4]

# Generated at 2022-06-13 03:21:51.968589
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector()
    result = fact_collector.collect()
    assert isinstance(result.get('python'), dict)
    assert isinstance(result.get('python').get('version'), dict)
    assert isinstance(result.get('python').get('version_info'), list)
    assert isinstance(result.get('python').get('has_sslcontext'), bool)


# Generated at 2022-06-13 03:22:03.450845
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    from ansible.module_utils.facts.collector import FactsCollector
    from ansible.module_utils._text import to_bytes  # noqa: F401 # pylint: disable=unused-import

    # Get PythonFactCollector object
    python_facts_collector = FactsCollector.get_collector('python')

    # Get a dict with the results of calling collect()
    python_facts = python_facts_collector.collect()

    # Test the type of the result
    assert type(python_facts) is dict, "Result has incorrect type"

    # Test the contents of the result
    test_keys = ['python', 'ansible_python']
    for key in test_keys:
        assert key in python_facts, "Result does not contain expected key '%s'" % key

# Generated at 2022-06-13 03:22:09.237985
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    test_collector = PythonFactCollector()
    fake_facts = {}

    returned_facts = test_collector.collect(collected_facts=fake_facts)

    assert isinstance(returned_facts, dict)
    assert debug_info.name == 'python'
    assert debug_info.fact_ids == set()
    assert isinstance(returned_facts['python']['version'], dict)
    assert isinstance(returned_facts['python']['version']['major'], int)
    assert isinstance(returned_facts['python']['version']['minor'], int)
    assert isinstance(returned_facts['python']['version']['micro'], int)
    assert isinstance(returned_facts['python']['version']['releaselevel'], str)

# Generated at 2022-06-13 03:22:11.596366
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact_collector = PythonFactCollector()
    # test case where all the expected data is available, actual data is not checked
    python_fact_collector.collect()



# Generated at 2022-06-13 03:22:13.472368
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact_collector = PythonFactCollector()
    assert isinstance(python_fact_collector, PythonFactCollector)

# Generated at 2022-06-13 03:22:19.575376
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    c = PythonFactCollector()

    result = c.collect()

    assert result['python']
    assert type(result['python']) is dict
    assert result['python']['version']
    assert type(result['python']['version']) is dict
    assert result['python']['version']['major']
    assert type(result['python']['version']['major']) is int
    assert result['python']['version']['minor']
    assert type(result['python']['version']['minor']) is int
    assert result['python']['version']['micro']
    assert type(result['python']['version']['micro']) is int
    assert result['python']['version']['releaselevel']