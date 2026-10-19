

# Generated at 2022-06-13 03:12:25.260230
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pythonfc = PythonFactCollector()
    result = pythonfc.collect()
    assert 'python' in result
    assert isinstance(result['python'], dict)
    assert 'version' in result['python']
    assert isinstance(result['python']['version'], dict)
    assert 'major' in result['python']['version']
    assert isinstance(result['python']['version']['major'], int)
    assert 'minor' in result['python']['version']
    assert isinstance(result['python']['version']['minor'], int)
    assert 'micro' in result['python']['version']
    assert isinstance(result['python']['version']['micro'], int)
    assert 'releaselevel' in result['python']['version']

# Generated at 2022-06-13 03:12:31.927524
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector()
    result = pfc.collect()
    assert isinstance(result, dict)
    assert result['python']['version']['major'] == sys.version_info[0]
    assert result['python']['version']['minor'] == sys.version_info[1]
    assert result['python']['version']['micro'] == sys.version_info[2]
    assert result['python']['version']['releaselevel'] == sys.version_info[3]
    assert result['python']['version']['serial'] == sys.version_info[4]

# Generated at 2022-06-13 03:12:35.604891
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    from ansible.module_utils.facts import Collector

    c = Collector()

    # Test that collector was registered
    assert 'python' in c._fact_classes

    # Test collection
    facts = c.collect(module=None, collected_facts=None)
    assert facts['python']['type'] == 'cpython'
    assert facts['python']['executable'] == sys.executable
    assert facts['python']['has_sslcontext'] == HAS_SSLCONTEXT

# Generated at 2022-06-13 03:12:40.881428
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = PythonFactCollector().collect()['ansible_facts']['python']
    assert type(python_facts['version_info']) == list
    assert type(python_facts['version']['major']) == int
    assert type(python_facts['version']['minor']) == int
    assert type(python_facts['version']['micro']) == int
    assert type(python_facts['version']['releaselevel']) == str
    assert type(python_facts['version']['serial']) == int
    assert type(python_facts['executable']) == str
    assert type(python_facts['has_sslcontext']) == bool

# Generated at 2022-06-13 03:12:48.526167
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    try:
        import ssl
        ssl_ver = ssl.OPENSSL_VERSION
    except (ImportError, AttributeError):
        ssl_ver = None

    class TestClassPythonFactCollector(PythonFactCollector):
        def collect(self, module=None, collected_facts=None):
            return super(TestClassPythonFactCollector, self).collect(module, collected_facts)

    new_instance = TestClassPythonFactCollector()

    assert new_instance._fact_ids == set()

    facts = new_instance.collect()

    assert 'executable' in facts['python'].keys()

    if ssl_ver is None:
        assert facts['python']['has_sslcontext'] is False

    return True

# Generated at 2022-06-13 03:12:56.906650
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    import sys

    collector = PythonFactCollector()
    python_facts = collector.collect()

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


# Generated at 2022-06-13 03:13:04.470727
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    pc = PythonFactCollector()
    result = pc.collect()

    assert result['python']['type'] == 'CPython'
    assert result['python']['version']['major'] == sys.version_info[0]
    assert result['python']['version']['minor'] == sys.version_info[1]
    assert result['python']['version']['micro'] == sys.version_info[2]
    assert result['python']['version']['releaselevel'] == sys.version_info[3]
    assert result['python']['version']['serial'] == sys.version_info[4]
    assert result['python']['version_info'] == list(sys.version_info)
    assert result['python']['executable'] == sys.executable

# Generated at 2022-06-13 03:13:14.760714
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    module_mock = None
    collected_facts_mock = None
    python_fact_collector = PythonFactCollector()
    result = python_fact_collector.collect(module_mock, collected_facts_mock)

    assert result is not None, "No collect result was returned"
    assert isinstance(result, dict), "Result is not a dictionary"
    assert 'python' in result.keys(), "Result dictionary does not have a 'python' key"
    assert 'has_sslcontext' in result['python'].keys(), "Python dictionary does not have a 'has_sslcontext' key"
    assert 'type' in result['python'].keys(), "Python dictionary does not have a 'type' key"
    assert 'version' in result['python'].keys(), "Python dictionary does not have a 'version' key"

# Generated at 2022-06-13 03:13:22.511858
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact_collector = PythonFactCollector()
    collected_facts = {}
    facts = python_fact_collector.collect(collected_facts=collected_facts)

    assert 'python' in facts
    assert facts['python']['version']['major'] == sys.version_info[0]
    assert facts['python']['version']['minor'] == sys.version_info[1]
    assert facts['python']['version']['micro'] == sys.version_info[2]
    assert facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert facts['python']['version']['serial'] == sys.version_info[4]
    assert facts['python']['version_info'] == list(sys.version_info)
    assert facts

# Generated at 2022-06-13 03:13:32.028182
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector()
    pfc.collect()

# Generated at 2022-06-13 03:13:41.915284
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    test_collector = PythonFactCollector()
    res = test_collector.collect()
    assert isinstance(res, dict)
    assert isinstance(res['python']['version'], dict)
    assert isinstance(res['python']['version_info'], list)
    assert isinstance(res['python']['executable'], str)
    assert isinstance(res['python']['has_sslcontext'], bool)
    if sys.version_info[0] >= 3:
        assert isinstance(res['python']['type'], str)
    else:
        assert isinstance(res['python']['type'], type(None))

# Generated at 2022-06-13 03:13:48.083139
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector()
    result = fact_collector.collect()
    assert result == {
        'python': {
            'type': 'CPython',
            'version_info': [
                3,
                6,
                5,
                'final',
                0
            ],
            'version': {
                'releaselevel': 'final',
                'serial': 0,
                'major': 3,
                'minor': 6,
                'micro': 5
            },
            'executable': '/usr/bin/python3.6',
            'has_sslcontext': True
        }
    }

# Generated at 2022-06-13 03:13:58.252551
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """Test PythonFactCollector.collect."""
    # Instantiate the collector and get the facts
    python_facts = PythonFactCollector().collect()

    # Check the version
    assert python_facts['python']['version']['major'] == sys.version_info[0]
    assert python_facts['python']['version']['minor'] == sys.version_info[1]
    assert python_facts['python']['version']['micro'] == sys.version_info[2]

    assert python_facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert python_facts['python']['version']['serial'] == sys.version_info[4]

    assert python_facts['python']['version_info'] == list(sys.version_info)
   

# Generated at 2022-06-13 03:14:04.703352
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    from collections import namedtuple
    mod = namedtuple('module', 'params')
    pf = PythonFactCollector()
    python_facts = pf.collect(mod(params = {}))
    assert isinstance(python_facts, dict)
    assert isinstance(python_facts['python'], dict)
    assert isinstance(python_facts['python']['version'], dict)
    assert isinstance(python_facts['python']['version_info'], list)
    assert python_facts['python']['executable'] == sys.executable
    assert 'type' in python_facts['python']
    assert 'has_sslcontext' in python_facts['python']

# Generated at 2022-06-13 03:14:11.698249
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pf = PythonFactCollector()
    result = pf.collect()
    assert result['python']['version']['major'] == sys.version_info[0], 'Should return major version of Python.'
    assert result['python']['version']['minor'] == sys.version_info[1], 'Should return minor version of Python.'
    assert result['python']['version']['micro'] == sys.version_info[2], 'Should return micro version of Python.'
    assert result['python']['version']['releaselevel'] == sys.version_info[3], 'Should return releaselevel of Python.'
    assert result['python']['version']['serial'] == sys.version_info[4], 'Should return serial of Python.'

# Generated at 2022-06-13 03:14:15.963056
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Instantiate class
    python_fact_collector = PythonFactCollector()

    # Call method collect
    result = python_fact_collector.collect()

    # Assert if the result is not empty
    assert result

# Generated at 2022-06-13 03:14:25.523673
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector()
    res = fact_collector.collect()

    assert isinstance(res['python']['version'], dict)
    assert isinstance(res['python']['version']['major'], int)
    assert isinstance(res['python']['version']['minor'], int)
    assert isinstance(res['python']['version']['micro'], int)
    assert isinstance(res['python']['version']['releaselevel'], str)
    assert isinstance(res['python']['version']['serial'], int)
    assert isinstance(res['python']['version_info'], list)
    assert isinstance(res['python']['executable'], str)

# Generated at 2022-06-13 03:14:26.527581
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    assert PythonFactCollector.collect()

# Generated at 2022-06-13 03:14:33.967565
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    from collections import namedtuple
    from ansible.module_utils.facts.collector import FactsCollector

    python_version_info = namedtuple('version_info', ['major', 'minor', 'micro', 'releaselevel', 'serial'])
    python_version = namedtuple('version', ['version', 'version_info'])
    sys_mod = namedtuple('sys', ['version', 'version_info', 'executable', 'subversion', 'implementation'])
    sys_implementation_mod = namedtuple('implementation', ['name'])

    # create test_collector instance
    test_collector = PythonFactCollector()
    test_collector.collect()
    
    # create a mock FactsCollector instance
    test_facts_collector = FactsCollector()
    test_facts_collector.collectors

# Generated at 2022-06-13 03:14:43.265818
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fc = PythonFactCollector()
    import json
    import copy
    result = fc.collect()

    assert result['python']['version']['major'] == sys.version_info[0]
    assert result['python']['version']['minor'] == sys.version_info[1]
    assert result['python']['version']['micro'] == sys.version_info[2]
    assert result['python']['version']['releaselevel'] == sys.version_info[3]
    assert result['python']['version']['serial'] == sys.version_info[4]
    assert result['python']['version_info'] == list(sys.version_info)
    assert result['python']['executable'] == sys.executable


# Generated at 2022-06-13 03:14:54.979045
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    # Input data to test method
    input_data = {}

    # Expected result of the method
    expected_result = {
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

    # Run test
    fact_collector = PythonFactCollector()
    actual_result = fact_collector.collect(input_data)

    # Verify results
   

# Generated at 2022-06-13 03:15:01.079259
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    import sys
    import ssl
    fact_collector = PythonFactCollector()

    facts = fact_collector.collect()
    python_facts = facts['python']

    assert python_facts['version']['major'] == sys.version_info[0]
    assert python_facts['version']['minor'] == sys.version_info[1]
    assert python_facts['version']['micro'] == sys.version_info[2]
    assert python_facts['version']['releaselevel'] == sys.version_info[3]
    assert python_facts['version']['serial'] == sys.version_info[4]
    assert python_facts['version_info'] == list(sys.version_info)
    assert python_facts['executable'] == sys.executable

# Generated at 2022-06-13 03:15:17.262932
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Unit test description
    # 1. Create a PythonFactCollector instance
    # 2. Run collection
    # 3. Check returned facts and that fact ids are properly set

    fact_collector = PythonFactCollector()
    facts = fact_collector.collect()

    assert facts == {
        'python': {
            'type': 'CPython',
            'version_info': [2, 7, 16, 'final', 0],
            'executable': '/usr/bin/python',
            'has_sslcontext': True,
            'version': {
                'releaselevel': 'final',
                'major': 2,
                'serial': 0,
                'micro': 16,
                'minor': 7
            }
        }
    }
    assert fact_collector._fact_ids == {'python'}

# Generated at 2022-06-13 03:15:22.004930
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    the_collector = PythonFactCollector({}, None)
    the_facts = the_collector.collect({}, None)

    assert type(the_facts['python']) is dict
    assert type(the_facts['python']['version']) is dict
    assert type(the_facts['python']['version_info']) is list

# Generated at 2022-06-13 03:15:29.779836
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    import platform

    from ansible.module_utils.facts.collector import FactsCollector
    facts = FactsCollector()
    python_collector = facts.collectors['python']
    data = python_collector.collect()

    assert set(data.keys()) == {'python'}
    python_info = data['python']

    assert set(python_info.keys()) == {'version', 'version_info', 'executable', 'type', 'has_sslcontext'}
    assert python_info['version_info'][:2] == list(sys.version_info)[:2]
    assert python_info['executable'] == sys.executable
    assert python_info['type'] == python_collector.name

# Generated at 2022-06-13 03:15:46.631372
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    python_facts = {}

    python_facts['python'] = {
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

    try:
        python_facts['python']['type'] = sys.subversion[0]
    except AttributeError:
        try:
            python_facts['python']['type'] = sys.implementation.name
        except AttributeError:
            python

# Generated at 2022-06-13 03:15:50.865760
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_info = PythonFactCollector().collect()

    assert python_info['python']
    assert python_info['python']['version']
    assert python_info['python']['version']['major']
    assert python_info['python']['version']['minor']
    assert python_info['python']['version']['micro']
    assert python_info['python']['version']['releaselevel']
    assert python_info['python']['version']['serial']
    assert python_info['python']['version_info']
    assert python_info['python']['executable']

# Generated at 2022-06-13 03:15:56.862555
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    import json
    import pprint
    facts = PythonFactCollector().collect()
    print("Facts")
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(facts)
    print("JSON:\n" + json.dumps(facts, sort_keys=True, indent=4))

# Generated at 2022-06-13 03:16:01.467033
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    collector = PythonFactCollector()
    facts = collector.collect()

    # Since version_info is a tuple, the default comparison
    # operator will compare by values not by type.
    assert isinstance(facts['python']['version_info'], list)

    # Make sure 'has_sslcontext' is always a boolean.
    assert isinstance(facts['python']['has_sslcontext'], bool)

# Generated at 2022-06-13 03:16:10.081915
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector()
    # return value of collect() should be a dict
    assert isinstance(pfc.collect(), dict)
    # return value of collect() should have keys python
    assert 'python' in pfc.collect()
    # return value of collect()['python'] should be a dict
    assert isinstance(pfc.collect()['python'], dict)
    # return value of collect()['python'] should have keys type, executable, version and has_sslcontext
    assert 'type' in pfc.collect()['python']
    assert 'executable' in pfc.collect()['python']
    assert 'version' in pfc.collect()['python']
    assert 'has_sslcontext' in pfc.collect()['python']
    # return value of collect()['python']['version'] should be a dict
   

# Generated at 2022-06-13 03:16:14.701118
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    collector = PythonFactCollector()
    assert collector.collect()

# Generated at 2022-06-13 03:16:23.384189
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact_collector = PythonFactCollector(None)
    python_facts = python_fact_collector.collect()

    # Check if the major version is correctly set
    assert python_facts['python']['version']['major'] == sys.version_info[0]

    # Check if the minor version is correctly set
    assert python_facts['python']['version']['minor'] == sys.version_info[1]

    # Check if the micro version is correctly set
    assert python_facts['python']['version']['micro'] == sys.version_info[2]

    # Check if the releaselevel is correctly set
    assert python_facts['python']['version']['releaselevel'] == sys.version_info[3]

    # Check if the serial is correctly set

# Generated at 2022-06-13 03:16:28.297841
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = PythonFactCollector().collect()

    assert isinstance(python_facts, dict)
    assert 'python' in python_facts.keys()
    assert 'version_info' in python_facts['python'].keys()
    assert 'executable' in python_facts['python'].keys()
    assert 'has_sslcontext' in python_facts['python'].keys()

# Generated at 2022-06-13 03:16:35.347334
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    c = PythonFactCollector()
    results = c.collect()

# Generated at 2022-06-13 03:16:36.802600
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact_collector = PythonFactCollector()
    assert isinstance(python_fact_collector.collect(), dict)

# Generated at 2022-06-13 03:16:41.667485
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_collector = PythonFactCollector()
    assert isinstance(python_collector, PythonFactCollector)
    assert python_collector.name == 'python'
    assert 'python' in python_collector.collect()

# Generated at 2022-06-13 03:16:43.819019
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector()
    fact_collector._module = None
    collected_facts = {}
    fact_collector.collect(module=None, collected_facts=collected_facts)
    assert collected_facts

# Generated at 2022-06-13 03:16:46.173704
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = PythonFactCollector().collect()

    assert {'python'} == python_facts.keys()
    assert {'version', 'version_info', 'executable', 'has_sslcontext', 'type'} == python_facts['python'].keys()

# Generated at 2022-06-13 03:16:48.206863
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    _module = None
    _collected_facts = None
    collector = PythonFactCollector(_module, _collected_facts)
    assert collector._fact_ids == set()
    assert collector.name == 'python'
    assert isinstance(collector.collect(), dict)

# Generated at 2022-06-13 03:16:49.399537
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    py_fact_collector = PythonFactCollector()
    py_fact_collector.collect()

# Generated at 2022-06-13 03:17:01.842531
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """ Tests for method collect of class PythonFactCollector """
    cc = PythonFactCollector()
    facts = cc.collect()
    assert facts['python']['version_info'][0] == sys.version_info[0]
    assert facts['python']['version_info'][1] == sys.version_info[1]
    assert facts['python']['version_info'][2] == sys.version_info[2]
    assert facts['python']['version_info'][3] == sys.version_info[3]
    assert facts['python']['version_info'][4] == sys.version_info[4]
    assert facts['python']['version']['major'] == sys.version_info[0]
    assert facts['python']['version']['minor'] == sys.version

# Generated at 2022-06-13 03:17:06.424911
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    from ansible.module_utils.facts import Facts
    from ansible.module_utils.facts.collectors.python import PythonFactCollector

    python_fact_collector = PythonFactCollector()
    facts = Facts(dict(), python_fact_collector)

    assert type(facts.get('python')) is dict

# Generated at 2022-06-13 03:17:07.990597
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector()
    fact_collector.collect()


# Generated at 2022-06-13 03:17:16.863098
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_collector = PythonFactCollector()
    python_facts = python_collector.collect()
    expected_result = {
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

    # patch the result to match CIs

# Generated at 2022-06-13 03:17:20.936466
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    facts = PythonFactCollector(None, None).collect()
    assert isinstance(facts['python']['version'], dict)
    assert isinstance(facts['python']['version_info'], list)
    assert isinstance(facts['python']['executable'], str)
    assert isinstance(facts['python']['type'], str)
    assert isinstance(facts['python']['has_sslcontext'], bool)

# Generated at 2022-06-13 03:17:21.950815
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    test_collector = PythonFactCollector()
    assert test_collector.collect()

# Generated at 2022-06-13 03:17:31.930004
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils.facts.collectors import which

    def test_python_facts(facts):
        assert 'python' in facts
        assert 'version' in facts['python']
        ver = facts['python']['version']
        assert 'major' in ver
        assert 'minor' in ver
        assert 'micro' in ver
        assert 'releaselevel' in ver
        assert 'serial' in ver
        assert 'version_info' in facts['python']
        assert 'executable' in facts['python']
        assert 'has_sslcontext' in facts['python'] or 'type' in facts['python']

    python_bin = which.which('python')

    facts = FactCollector(None, python_bin).collect()

# Generated at 2022-06-13 03:17:38.723600
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = PythonFactCollector().collect()
    assert python_facts['python']['version']['major'] == sys.version_info[0]
    assert python_facts['python']['version']['minor'] == sys.version_info[1]
    assert python_facts['python']['version']['micro'] == sys.version_info[2]
    assert python_facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert python_facts['python']['version']['serial'] == sys.version_info[4]
    assert python_facts['python']['version_info'] == list(sys.version_info)
    assert python_facts['python']['executable'] == sys.executable

# Generated at 2022-06-13 03:17:49.177433
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_collector = PythonFactCollector()

    result = python_collector.collect()

    assert result.get('python', None) is not None, \
        "The fact 'python' must exist"
    python_fact = result['python']
    assert python_fact.get('version', None) is not None, \
        "The fact 'python.version' must exist"
    assert python_fact.get('executable', None) is not None, \
        "The fact 'python.executable' must exist"
    assert python_fact.get('version_info', None) is not None, \
        "The fact 'python.version_info' must exist"
    assert python_fact.get('has_sslcontext', None) is not None, \
        "The fact 'python.has_sslcontext' must exist"

# Generated at 2022-06-13 03:17:55.413546
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    python_fact_collector = PythonFactCollector()
    result = python_fact_collector.collect()

    # Verify code returned 0
    assert result['ansible_facts']['python']['version']['releaselevel'] == 'final'
    assert result['ansible_facts']['python']['has_sslcontext'] == HAS_SSLCONTEXT

# Generated at 2022-06-13 03:18:11.212708
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    pfc = PythonFactCollector()
    # Get the version number for Python3
    # This should be a tuple which starts with 3
    fact = pfc.collect()
    assert fact['python']['version']['major'] == sys.version_info[0]
    assert fact['python']['version']['minor'] == sys.version_info[1]
    assert fact['python']['version']['micro'] == sys.version_info[2]
    assert fact['python']['version']['releaselevel'] == sys.version_info[3]
    assert fact['python']['version']['serial'] == sys.version_info[4]
    assert fact['python']['version_info'] == list(sys.version_info)

# Generated at 2022-06-13 03:18:15.306305
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    module = mock.MagicMock()
    module.params = {'gather_subset': None}
    module.params.update({'gather_timeout': 10, 'filter': '*'})
    collected_facts = {}

    pythonfact = PythonFactCollector(module)
    result = {}
    result.update(pythonfact.collect(module, collected_facts))
    assert 'python' in result.keys()
    for key in ['version', 'version_info', 'executable', 'has_sslcontext', 'type']:
        assert key in result['python'].keys()


# Generated at 2022-06-13 03:18:24.612596
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """Sets up a PythonFactCollector and tests the collect method
    """

    # Create PythonFactCollector object
    py_collector = PythonFactCollector()

    # Get the facts
    py_facts = py_collector.collect()

    # Check if the 'python' key exists in the facts
    assert 'python' in py_facts

    # Check if the 'python' key contains a dictionary
    assert isinstance(py_facts['python'], dict)

    # Create the expected facts

# Generated at 2022-06-13 03:18:29.146164
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    collector = PythonFactCollector()
    facts = collector.collect(None, None)
    assert 'python' in facts
    assert 'version' in facts['python']
    assert 'version_info' in facts['python']
    assert 'executable' in facts['python']
    assert 'type' in facts['python']
    assert 'has_sslcontext' in facts['python']

# Generated at 2022-06-13 03:18:35.660413
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    collector = PythonFactCollector()
    collected_facts = collector.collect()
    expected_result = {
        'python': {'executable': '/usr/bin/python',
                   'has_sslcontext': True,
                   'version': {'major': 2,
                               'minor': 7,
                               'micro': 12,
                               'releaselevel': 'final',
                               'serial': 0},
                   'version_info': [2, 7, 12, 'final', 0],
                   'type': 'CPython'}
    }
    assert collected_facts == expected_result

# Generated at 2022-06-13 03:18:39.717611
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    py_collector = PythonFactCollector()
    facts = py_collector.collect()

    assert facts is not None
    for key in ('major', 'minor', 'micro', 'releaselevel', 'serial'):
        assert key in facts['python']['version']
    for key in ('executable', 'type', 'has_sslcontext'):
        assert key in facts['python']

# Generated at 2022-06-13 03:18:46.222219
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector()
    facts = pfc.collect()
    assert 'python' in facts
    assert 'version_info' in facts['python']
    assert 'version' in facts['python']
    assert 'major' in facts['python']['version']
    assert 'minor' in facts['python']['version']
    assert 'micro' in facts['python']['version']
    assert 'releaselevel' in facts['python']['version']
    assert 'serial' in facts['python']['version']
    assert 'executable' in facts['python']
    assert 'has_sslcontext' in facts['python']
    assert 'type' in facts['python']

# Generated at 2022-06-13 03:18:55.188500
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Test the collect method of PythonFactCollector class
    fixture = PythonFactCollector()
    result = fixture.collect()
    assert 'python' in result
    assert 'version' in result['python']
    assert 'major' in result['python']['version']
    assert 'minor' in result['python']['version']
    assert 'micro' in result['python']['version']
    assert 'releaselevel' in result['python']['version']
    assert 'serial' in result['python']['version']
    assert 'version_info' in result['python']
    assert 'executable' in result['python']
    assert 'has_sslcontext' in result['python']
    assert 'type' in result['python']

# Generated at 2022-06-13 03:19:04.554562
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    fake_module = None
    fake_collected_facts = None
    fact_collector = PythonFactCollector(fake_module, fake_collected_facts)

    facts = fact_collector.collect(fake_module, fake_collected_facts)
    assert facts['python']['version']['major'] == sys.version_info[0]
    assert facts['python']['version']['minor'] == sys.version_info[1]
    assert facts['python']['version']['micro'] == sys.version_info[2]
    assert facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert facts['python']['version']['serial'] == sys.version_info[4]

# Generated at 2022-06-13 03:19:07.569940
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fake_module = 'fake-ansible-module'
    fake_facts = 'fake-collected-facts'
    pfc = PythonFactCollector()
    pf = pfc.collect(fake_module, fake_facts)
    assert isinstance(pf, dict)

# Generated at 2022-06-13 03:19:31.528257
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector()
    result = pfc.collect()
    assert result['python']['version']['major'] == 3
    assert result['python']['version']['minor'] == 6
    assert result['python']['version']['micro'] == 1
    assert result['python']['version']['releaselevel'] == 'final'
    assert result['python']['version']['serial'] == 0
    assert result['python']['version_info'] == [3, 6, 1, 'final', 0]
    assert result['python']['executable'] == sys.executable
    assert result['python']['has_sslcontext'] == HAS_SSLCONTEXT
    assert result['python']['type'] == sys.subversion[0]

# Generated at 2022-06-13 03:19:41.616290
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact_collector = PythonFactCollector()

    # Test default values
    collected_facts = {}
    expected_facts = {}
    expected_facts['python'] = {
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


# Generated at 2022-06-13 03:19:43.273600
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    c = PythonFactCollector()
    result = c.collect()
    assert isinstance(result, dict)
    assert "python" in result.keys()
    assert "version" in result["python"].keys()
    assert "executable" in result["python"].keys()

# Generated at 2022-06-13 03:19:47.580767
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pc = PythonFactCollector()
    res = pc.collect()
    assert 'python' in res
    python = res['python']
    assert 'version' in python
    assert 'version_info' in python
    assert 'has_sslcontext' in python
    assert 'executable' in python

    assert 'type' in python
    assert 'version' in python['version']
    assert 'major' in python['version']
    assert 'minor' in python['version']
    assert 'micro' in python['version']
    assert 'releaselevel' in python['version']
    assert 'serial' in python['version']

    assert isinstance(python['version']['major'], int)
    assert isinstance(python['version']['minor'], int)
    assert isinstance(python['version']['micro'], int)

# Generated at 2022-06-13 03:19:48.894289
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    print('TEST COLLECT')
    PythonFactCollector().collect()

# Generated at 2022-06-13 03:19:57.840469
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Create instance of a class PythonFactCollector
    python_fact_collector = PythonFactCollector()
    # Gather and return the python facts
    facts = python_fact_collector.collect()
    # Assert that facts is a dict
    assert isinstance(facts, dict)
    # Assert that the python fact key has a dict value
    assert 'python' in facts
    # Assert that the python dict has a 'version' key with dict value
    assert 'version' in facts['python']
    # Assert that the version dict has a 'major' key with int value
    assert 'major' in facts['python']['version']
    assert isinstance(facts['python']['version']['major'], int)
    # Assert that the version dict has a 'minor' key with int value
    assert 'minor'

# Generated at 2022-06-13 03:20:02.770281
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector()
    collected_facts = fact_collector.collect(module=None, collected_facts=None)
    assert 'python' in collected_facts
    assert 'version' in collected_facts['python']
    assert 'version_info' in collected_facts['python']
    assert 'executable' in collected_facts['python']
    assert 'type' in collected_facts['python']

# Generated at 2022-06-13 03:20:07.349463
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = PythonFactCollector().collect()

    assert isinstance(python_facts, dict)
    assert 'python' in python_facts
    assert isinstance(python_facts['python'], dict)
    assert 'version' in python_facts['python']
    assert 'version_info' in python_facts['python']
    assert 'executable' in python_facts['python']
    assert isinstance(python_facts['python']['version'], dict)

# Generated at 2022-06-13 03:20:11.917859
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector()
    fact = fact_collector.collect()
    assert fact is not None
    assert 'python' in fact
    assert 'version' in fact['python']
    assert 'version_info' in fact['python']
    assert 'executable' in fact['python']
    assert 'type' in fact['python']
    assert 'has_sslcontext' in fact['python']

# Generated at 2022-06-13 03:20:22.747380
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    import sys

    class TestFactCollectorPlugin(PythonFactCollector):
        name = 'test'

        def collect(self, module=None, collected_facts=None):
            return {'test': 'this is a test'}

    p = TestFactCollectorPlugin()

    # Check for version_info
    assert 'version_info' in p.collect()['python']
    assert isinstance(p.collect()['python']['version_info'], list)
    assert isinstance(p.collect()['python']['version']['version_info'], list)
    assert p.collect()['python']['version']['version_info'] == p.collect()['python']['version_info']

    # Check for executable
    assert 'executable' in p.collect()['python']

# Generated at 2022-06-13 03:20:58.998070
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    import sys

    # We need the version to be a tuple.
    old_version = sys.version
    sys.version = '2.7.11 (default, Dec  5 2015, 14:44:53) \n'\
            '[GCC 4.2.1 Compatible Apple LLVM 7.0.0 (clang-700.1.76)]'
    sys.version_info = tuple([int(x) for x in sys.version.split()[0].split('.')])
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collectors import PythonFactCollector
    collector = PythonFactCollector()
    data = collector.collect()
    print(data)
    assert(data['python']['version']['major'] == 2)

# Generated at 2022-06-13 03:21:05.981230
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    class TestArgs:
        ansible_python_interpreter = '/path/to/python'
        ansible_python_version = '2.6.6'

    import sys

    sys.version_info = (2, 6, 6, 'final', 0)
    sys.executable = '/path/to/python'
    sys.subversion = ['CPython', '2.6.6']

    python_fact_collector = PythonFactCollector()
    facts = python_fact_collector.collect(TestArgs)

    assert facts['python']['executable'] == '/path/to/python'
    assert facts['python']['version']['major'] == 2
    assert facts['python']['version']['minor'] == 6
    assert facts['python']['version']['micro'] == 6
   

# Generated at 2022-06-13 03:21:11.439039
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact_collector = PythonFactCollector()

    python_facts = python_fact_collector.collect()

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


# Generated at 2022-06-13 03:21:13.440053
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    from ansible.module_utils.facts import FactCollector
    PythonFactCollector.collect(FactCollector)

# Generated at 2022-06-13 03:21:19.300481
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    python_facts = {
        'python': {
            'executable': '/usr/bin/python',
            'has_sslcontext': True,
            'type': 'CPython',
            'version': {
                'releaselevel': 'final',
                'major': 2,
                'minor': 7,
                'micro': 10,
                'serial': 0},
            'version_info': [2, 7, 10, 'final', 0]
            }
        }

    python_fact_collector = PythonFactCollector()
    facts = python_fact_collector.collect()
    assert facts == python_facts


# Generated at 2022-06-13 03:21:23.917466
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    collector = PythonFactCollector()
    assert collector.collect() == {
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

# Generated at 2022-06-13 03:21:32.546452
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Setup
    python_fact_collector = PythonFactCollector()
    # Exercise
    facts = python_fact_collector.collect()
    # Verify
    assert facts['python']['has_sslcontext']
    assert facts['python']['version']['major'] == sys.version_info[0]
    assert facts['python']['version']['minor'] == sys.version_info[1]
    assert facts['python']['version']['micro'] == sys.version_info[2]
    assert facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert facts['python']['version']['serial'] == sys.version_info[4]
    assert facts['python']['version_info'] == list(sys.version_info)

# Generated at 2022-06-13 03:21:36.865625
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    module = None
    collected_facts = None

    python_fc = PythonFactCollector()

    # call the method
    result = python_fc.collect(module, collected_facts)

    # assert if the result is as expected
    assert "python" in result
    if sys.version_info[0] >= 3:
        assert result["python"]["has_sslcontext"] == True
    else:
        assert result["python"]["has_sslcontext"] == False

# Generated at 2022-06-13 03:21:41.379722
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """Test method collect of class PythonFactCollector.

    The method is always returning a dictionary.
    The dictionary has key 'python' with a number of items.
    We check that the keys are the ones we expect.
    """
    pfc = PythonFactCollector()
    f = pfc.collect()
    assert 'python' in f
    assert 'version' in f['python']
    assert 'version_info' in f['python']
    assert 'executable' in f['python']
    assert 'type' in f['python']

# Generated at 2022-06-13 03:21:42.661467
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
  test_collector = PythonFactCollector()
  test_collector.collect()