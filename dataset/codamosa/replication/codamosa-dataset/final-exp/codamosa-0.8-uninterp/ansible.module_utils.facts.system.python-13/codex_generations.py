

# Generated at 2022-06-13 03:12:20.121438
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    import sys
    python_facts = PythonFactCollector().collect()['python']
    assert isinstance(python_facts, dict)
    assert 'version' in python_facts
    assert isinstance(python_facts['version'], dict)
    assert 'major' in python_facts['version']
    assert isinstance(python_facts['version']['major'], int)
    assert 'minor' in python_facts['version']
    assert isinstance(python_facts['version']['minor'], int)
    assert 'micro' in python_facts['version']
    assert isinstance(python_facts['version']['micro'], int)
    assert 'releaselevel' in python_facts['version']
    assert isinstance(python_facts['version']['releaselevel'], str)

# Generated at 2022-06-13 03:12:37.712499
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    from collections import namedtuple
    ansible_facts = dict()
    ansible_facts.update(dict(test=dict()))
    ansible_facts['test'].update(dict(python=dict()))
    ansible_facts['test']['python'].update(dict(version=dict()))
    ansible_facts['test']['python']['version'].update(dict(major=sys.version_info[0], minor=sys.version_info[1], micro=sys.version_info[2], releaselevel=sys.version_info[3], serial=sys.version_info[4]))
    ansible_facts['test']['python'].update(dict(executable=sys.executable))

# Generated at 2022-06-13 03:12:44.846795
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector()

    result = pfc.collect()

    assert(result['python']['version']['major'] == sys.version_info[0])
    assert(result['python']['version']['minor'] == sys.version_info[1])
    assert(result['python']['version']['micro'] == sys.version_info[2])
    assert(result['python']['version']['releaselevel'] == sys.version_info[3])
    assert(result['python']['version']['serial'] == sys.version_info[4])
    assert(result['python']['version_info'] == list(sys.version_info))
    assert(result['python']['has_sslcontext'] == HAS_SSLCONTEXT)


# Generated at 2022-06-13 03:12:54.921840
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    collector = PythonFactCollector()
    facts = collector.collect()

    assert 'python' in facts
    python_facts = facts['python']

    assert 'version' in python_facts
    version = python_facts['version']
    assert 'major' in version
    assert 'minor' in version
    assert 'micro' in version
    assert 'releaselevel' in version
    assert 'serial' in version
    assert 'version_info' in python_facts
    assert 'executable' in python_facts
    assert 'has_sslcontext' in python_facts
    assert 'type' in python_facts


# Generated at 2022-06-13 03:12:59.800472
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

# Generated at 2022-06-13 03:13:12.324814
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    # Create object and get it's fact
    python_fact_collector = PythonFactCollector()
    fact = python_fact_collector.collect()
    # print fact

    assert fact['python']['version']['major'] == sys.version_info[0]
    assert fact['python']['version']['minor'] == sys.version_info[1]
    assert fact['python']['version']['micro'] == sys.version_info[2]
    assert fact['python']['version']['releaselevel'] == sys.version_info[3]
    assert fact['python']['version']['serial'] == sys.version_info[4]
    assert fact['python']['version_info'] == list(sys.version_info)
    assert fact['python']['executable'] == sys

# Generated at 2022-06-13 03:13:20.815065
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """ Test case for
    PythonFactCollector_collect()
    """
    # pylint: disable=maybe-no-member
    python_collector = PythonFactCollector()

    python_facts = python_collector.collect()
    assert python_facts['python']['version']['major'] == sys.version_info[0]
    assert python_facts['python']['version']['minor'] == sys.version_info[1]
    assert python_facts['python']['version']['micro'] == sys.version_info[2]
    assert python_facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert python_facts['python']['version']['serial'] == sys.version_info[4]

# Generated at 2022-06-13 03:13:28.148930
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pc = PythonFactCollector()
    assert pc.collect()['python'] == {
        'executable': sys.executable,
        'has_sslcontext': HAS_SSLCONTEXT,
        'type': sys.subversion[0],
        'version': {
            'major': sys.version_info[0],
            'minor': sys.version_info[1],
            'micro': sys.version_info[2],
            'releaselevel': sys.version_info[3],
            'serial': sys.version_info[4],
        },
        'version_info': list(sys.version_info),
    }

# Generated at 2022-06-13 03:13:29.301541
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fc = PythonFactCollector()
    assert isinstance(fc.collect(), dict)

# Generated at 2022-06-13 03:13:30.179182
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # TODO: complete this unit test
    return True

# Generated at 2022-06-13 03:13:39.572594
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    import sys
    import pytest
    from ansible.module_utils.facts.collectors.python import PythonFactCollector

    # Define a mock class
    class MockPythonFactCollector(PythonFactCollector):
        # Mock method
        def __init__(self):
            super(MockPythonFactCollector, self).__init__()
    
    # Create an instance of MockPythonFactCollector
    mock_instance = MockPythonFactCollector()

    # Set instance attribute has_sslcontext
    mock_instance.has_sslcontext = True

    # Set instance attribute facts

# Generated at 2022-06-13 03:13:47.593319
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils._text import to_bytes

    if collector.fact_cache['python']['python_executable'] is None:
        # We only execute this test if we're running with Python
        # as opposed to some other implementation
        return

    fact_collector = PythonFactCollector()
    ansible_facts = {}
    fact_collector.collect(collected_facts=ansible_facts)

    assert isinstance(fact_collector, BaseFactCollector)
    assert fact_collector.name == 'python'

    expected_python_executable = to_bytes(sys.executable)

    assert ansible_facts['python']['version']['major'] == sys

# Generated at 2022-06-13 03:13:49.474340
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = PythonFactCollector().collect()
    assert 'python' in python_facts

# Generated at 2022-06-13 03:13:58.930412
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = PythonFactCollector()
    facts = python_facts.collect()
    assert facts['python']['version_info'] == list(sys.version_info)
    assert facts['python']['version']['major'] == sys.version_info[0]
    assert facts['python']['version']['minor'] == sys.version_info[1]
    assert facts['python']['version']['micro'] == sys.version_info[2]
    assert facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert facts['python']['version']['serial'] == sys.version_info[4]
    assert facts['python']['executable'] == sys.executable

# Generated at 2022-06-13 03:14:01.455779
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector()
    fact_collector.collect()
# vim: set filetype=python:eof:ts=4

# Generated at 2022-06-13 03:14:10.145820
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    
    # init PythonFactCollector
    fc = PythonFactCollector()

    # run collect method
    facts = fc.collect()

    # check result
    assert facts['python']
    assert facts['python']['version']['major'] == 3
    assert facts['python']['version']['minor'] == 4
    assert facts['python']['version']['micro'] == 0
    assert facts['python']['version']['releaselevel'] == 'final'
    assert facts['python']['version']['serial'] == 0
    assert facts['python']['version_info'] == [3, 4, 0, 'final', 0]
    assert facts['python']['executable']
    assert facts['python']['type'] == 'CPython'

# Generated at 2022-06-13 03:14:20.171777
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector()
    pf = pfc.collect()

    assert pf['python']['version']['major'] == sys.version_info[0]
    assert pf['python']['version']['minor'] == sys.version_info[1]
    assert pf['python']['version']['micro'] == sys.version_info[2]
    assert pf['python']['version']['releaselevel'] == sys.version_info[3]
    assert pf['python']['version']['serial'] == sys.version_info[4]
    assert pf['python']['version_info'] == list(sys.version_info)
    assert pf['python']['executable'] == sys.executable


# Generated at 2022-06-13 03:14:29.798898
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    try:
        import ssl
        has_sslcontext = True
    except ImportError:
        has_sslcontext = False

    o_pfc = PythonFactCollector()
    result = o_pfc.collect()

    assert result['python']['version']['major'] == sys.version_info[0]
    assert result['python']['version']['minor'] == sys.version_info[1]
    assert result['python']['version']['micro'] == sys.version_info[2]
    assert result['python']['version']['releaselevel'] == sys.version_info[3]
    assert result['python']['version']['serial'] == sys.version_info[4]
    assert result['python']['version_info'] == list(sys.version_info)
   

# Generated at 2022-06-13 03:14:41.144272
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fragment = '''
        {
            "python": {
                "executable": "/usr/bin/python",
                "has_sslcontext": true,
                "type": "CPython",
                "version": {
                    "major": 2,
                    "micro": 6,
                    "minor": 6,
                    "releaselevel": "final",
                    "serial": 0
                },
                "version_info": [
                    2,
                    6,
                    6,
                    "final",
                    0
                ]
            }
        }
    '''
    expected_result = eval(fragment)
    python_fact_collector = PythonFactCollector()
    result = python_fact_collector.collect()
    assert expected_result == result

# Generated at 2022-06-13 03:14:42.387212
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    py_fact = PythonFactCollector()
    py_fact.collect()


# Generated at 2022-06-13 03:14:53.299610
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    result = PythonFactCollector().collect(None, None)

    # We don't know the details of the system running these tests, so we
    # can't assert specific values. All we can do is test for existence
    # of the expected keys.
    assert "python" in result
    assert "version" in result["python"]
    assert "version_info" in result["python"]
    assert "executable" in result["python"]
    assert "has_sslcontext" in result["python"]
    assert "type" in result["python"]

# Generated at 2022-06-13 03:14:54.629279
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pass

# Generated at 2022-06-13 03:14:58.727593
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_collector = PythonFactCollector()
    assert python_collector.collect() == {'python': {'version': {'micro': 2, 'releaselevel': 'final', 'major': 2, 'serial': 0, 'minor': 7}, 'version_info': [2, 7, 2, 'final', 0], 'type': 'CPython', 'executable': sys.executable, 'has_sslcontext': True}}

# Generated at 2022-06-13 03:15:07.294484
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    collector = PythonFactCollector()
    facts = collector.collect()
    assert isinstance(facts, dict)
    for fact in facts['python']['version_info']:
        assert isinstance(fact, int)
    for fact in ['major', 'minor', 'micro', 'releaselevel', 'serial']:
        assert isinstance(facts['python']['version'][fact], int)
    for fact in ['executable', 'type']:
        assert isinstance(facts['python'][fact], type(None)) or isinstance(facts['python'][fact], str)
    assert isinstance(facts['python']['has_sslcontext'], bool)

# Generated at 2022-06-13 03:15:13.829064
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    # get a PythonFactCollector
    py_collector = PythonFactCollector()

    # test the results of the collect method
    py_facts = py_collector.collect()
    assert py_facts['python']['version']['major'] >= 2
    assert py_facts['python']['version']['minor'] >= 6
    assert py_facts['python']['version']['releaselevel'] in ('beta', 'candidate', 'final')
    assert py_facts['python']['version']['serial'] >= 0
    assert len(py_facts['python']['version_info']) == 5

# Generated at 2022-06-13 03:15:17.510344
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    #
    # Object instantiation
    #
    pfc = PythonFactCollector()

    #
    # Perform test
    #
    result = pfc.collect()

    #
    # Check result
    #
    assert 'python' in result

# Generated at 2022-06-13 03:15:26.344770
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector({}, {})
    facts = fact_collector.collect()
    assert 'python' in facts
    assert facts['python']['version']['major'] == sys.version_info[0]
    assert facts['python']['version']['minor'] == sys.version_info[1]
    assert facts['python']['version']['micro'] == sys.version_info[2]
    assert facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert facts['python']['version']['serial'] == sys.version_info[4]
    assert facts['python']['version_info'] == list(sys.version_info)
    assert facts['python']['executable'] == sys.executable

# Generated at 2022-06-13 03:15:32.006223
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    collector = PythonFactCollector
    obj = collector()
    assert obj.collect() == {'python': {'version': {'major': 2, 'minor': 7, 'micro': 12, 'releaselevel': 'final', 'serial': 0}, 'version_info': [2, 7, 12, 'final', 0], 'executable': '/usr/bin/python', 'has_sslcontext': False, 'type': 'python'}}

# Generated at 2022-06-13 03:15:43.486055
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """
        Create a Fake module and use it as argument of collect method of
        PythonFactCollector.
        Check if the method collect returns a dict with key python.
    """
    class FakeModule(object):
        pass

    fake_module = FakeModule()
    fact_collector = PythonFactCollector()
    fact_collector.collect(fake_module, None)
    assert 'python' in fact_collector.collect(fake_module, None)

# Generated at 2022-06-13 03:15:49.390384
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """Test that the _collect_python method works correctly
    """

    # setup test environment
    pf_collector = PythonFactCollector()
    results = pf_collector.collect()

    # verify results are valid
    assert isinstance(results, dict) == True
    assert isinstance(results['python'], dict) == True
    assert isinstance(results['python']['version'], dict) == True
    assert isinstance(results['python']['version_info'], list) == True
    assert results['python']['type'] in ['Jython', 'PyPy'] or results['python']['type'] is None
    assert isinstance(results['python']['executable'], str) == True

# Generated at 2022-06-13 03:16:00.969215
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector()
    result = pfc.collect()

    # Verify that the result is a dict
    assert isinstance(result, dict)
    assert isinstance(result['python'], dict)

    # Verify that we have python version info
    assert isinstance(result['python']['version'], dict)

    # Verify that we have the executable path
    if sys.platform == 'win32':
        assert result['python']['executable'] == 'python.exe'
    else:
        assert result['python']['executable'] == 'python'

# Generated at 2022-06-13 03:16:09.781163
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """Test PythonFactCollector._collect()"""
    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils.facts.collector import BaseFactCollector
    #
    # First test without paramters:
    module = None
    collected_facts = {}
    facts = FactCollector
    #
    fact_collector = PythonFactCollector()
    fact_collector.collect(module=module, collected_facts=collected_facts)
    #
    assert(fact_collector)
    assert(isinstance(fact_collector, BaseFactCollector))
    assert(hasattr(fact_collector, 'name'))
    assert(hasattr(fact_collector, '_fact_ids'))
    assert(hasattr(fact_collector, 'collect'))
    #
    return

# Generated at 2022-06-13 03:16:19.640630
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    with mock.patch.dict(sys.modules, {
        'ssl': mock.MagicMock(**{'create_default_context.side_effect': AttributeError}),
        'os': mock.MagicMock(**{'environ.__getitem__.side_effect': ('/usr/bin/python', None, None)})
    }):
        result = PythonFactCollector().collect()

# Generated at 2022-06-13 03:16:25.757292
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    c = PythonFactCollector()
    python_facts = c.collect()
    assert c.name == "python"
    assert python_facts is not None
    assert python_facts.get("python") is not None
    assert python_facts.get("python").get("version") is not None
    assert python_facts.get("python").get("version_info") is not None
    assert python_facts.get("python").get("executable") is not None
    assert python_facts.get("python").get("has_sslcontext") is not None
    assert python_facts.get("python").get("type") is not None

# Generated at 2022-06-13 03:16:30.533966
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts import get_collector_instance

    collector = get_collector_instance(Collector, 'python')

    output = collector.collect()
    assert 'python' in output
    assert 'version' in output['python']
    assert 'version_info' in output['python']
    assert 'executable' in output['python']
    assert 'has_sslcontext' in output['python']
    assert 'type' in output['python']

# Generated at 2022-06-13 03:16:35.961191
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector()
    assert pfc.collect() == {'python': {'executable': '/usr/bin/python',
                                        'has_sslcontext': True,
                                        'type': 'CPython',
                                        'version': {'major': 2,
                                                    'minor': 7,
                                                    'micro': 12,
                                                    'releaselevel': 'final',
                                                    'serial': 0},
                                        'version_info': [2, 7, 12, 'final', 0]}}

# Generated at 2022-06-13 03:16:40.923291
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = PythonFactCollector().collect()
    assert python_facts['python']['version']['major'] == sys.version_info[0]

# Generated at 2022-06-13 03:16:42.090842
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector()
    pfc.collect()

# Generated at 2022-06-13 03:16:47.717992
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    result = PythonFactCollector().collect()
    assert 'python' in result
    assert 'version' in result['python']
    assert 'version_info' in result['python']
    assert 'executable' in result['python']
    assert 'has_sslcontext' in result['python']
    assert 'type' in result['python']
    assert isinstance(result['python']['version'], dict)
    assert isinstance(result['python']['version_info'], list)
    assert isinstance(result['python']['executable'], str)
    assert isinstance(result['python']['has_sslcontext'], bool)
    assert isinstance(result['python']['type'], str) or result['python']['type'] is None

# Generated at 2022-06-13 03:16:52.128674
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact_collector = PythonFactCollector()
    assert python_fact_collector.collect() == {
        'python': {
            'type': 'CPython',
            'version_info': [3, 4, 0, 'final', 0],
            'version': {
                'micro': 0,
                'serial': 0,
                'minor': 4,
                'releaselevel': 'final',
                'major': 3
            },
            'executable': '/usr/bin/python3.4',
            'has_sslcontext': True,
        }
    }

# Generated at 2022-06-13 03:17:01.202692
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector()
    assert isinstance(pfc.collect(), dict)

# Generated at 2022-06-13 03:17:04.634456
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    c = PythonFactCollector()
    result = c.collect()
    assert 'python' in result
    assert result['python']['version']['major'] == sys.version_info[0]

# Generated at 2022-06-13 03:17:05.154654
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pass

# Generated at 2022-06-13 03:17:12.569326
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    # Instantiate
    collector = PythonFactCollector()

    # Call method collect
    collected_facts = collector.collect()
    # TODO: Use assertIsInstance() in Ansible 2.10
    assert isinstance(collected_facts, dict)

    assert 'python' in collected_facts
    assert 'version' in collected_facts['python']
    assert 'version_info' in collected_facts['python']
    assert 'executable' in collected_facts['python']
    assert 'type' in collected_facts['python']
    assert 'has_sslcontext' in collected_facts['python']

# Generated at 2022-06-13 03:17:19.496084
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

# Generated at 2022-06-13 03:17:20.653677
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Tested by sanity
    pass

# Generated at 2022-06-13 03:17:27.109019
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector import PythonFactCollector
    import sys

    base_fact_collector_obj = BaseFactCollector()
    python_fact_collector_obj = PythonFactCollector(base_fact_collector_obj)
    python_facts = python_fact_collector_obj.collect()

    assert isinstance(python_facts['python'], dict)
    assert isinstance(python_facts['python']['version']['major'], int)
    assert isinstance(python_facts['python']['version']['minor'], int)
    assert isinstance(python_facts['python']['version']['micro'], int)

# Generated at 2022-06-13 03:17:34.679412
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    import mock

    mock_module = mock.Mock()
    facts_list = ['ansible_python', 'ansible_python_version']
    test_inst = PythonFactCollector()

    # add an ansible_python fact to the list of facts collected
    ret = test_inst.collect(mock_module, facts_list)
    assert ret == {'ansible_python': {u'version': {u'releaselevel': u'final',
        u'major': 2, u'minor': 7, u'micro': 11, u'serial': 0},
        u'executable': '/usr/bin/python',
        'has_sslcontext': True,
        u'version_info': [2, 7, 11, u'final', 0],
        u'type': u'CPython'}}

# Generated at 2022-06-13 03:17:35.691095
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    assert hasattr(PythonFactCollector, 'collect'), "Class PythonFactCollector does not have required method 'collect'"

# Generated at 2022-06-13 03:17:40.559029
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pythonfc = PythonFactCollector()

    facts = pythonfc.collect()

    assert facts['python']
    assert facts['python']['executable']
    assert facts['python']['version']
    assert facts['python']['version']['major'] == sys.version_info[0]
    assert facts['python']['version']['minor'] == sys.version_info[1]
    assert facts['python']['version']['micro'] == sys.version_info[2]
    assert facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert facts['python']['version']['serial'] == sys.version_info[4]
    assert facts['python']['has_sslcontext'] == HAS_SSLCONTEXT

# Generated at 2022-06-13 03:18:02.432030
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    from ansible.module_utils.facts import collector
    collector.add_collector(PythonFactCollector)
    facts_dict = collector.collect(none_type=None, collected_facts={})
    assert 'python' in facts_dict
    # Specific versions are not tested since they change over time
    assert 'version' in facts_dict['python']
    assert 'version_info' in facts_dict['python']
    assert 'executable' in facts_dict['python']
    assert 'type' in facts_dict['python']
    assert 'has_sslcontext' in facts_dict['python']

# Generated at 2022-06-13 03:18:10.986138
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    from ansible.module_utils.facts.collector import get_collector_instance

    # Get instance of PythonFactCollector class
    fact_collector = get_collector_instance('python')

    # Call method collect
    facts = fact_collector.collect()

    # Assert the correctness of collected facts
    assert facts['python']['version']['major'] == sys.version_info[0]
    assert facts['python']['version']['minor'] == sys.version_info[1]
    assert facts['python']['version']['micro'] == sys.version_info[2]
    assert facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert facts['python']['version']['serial'] == sys.version_info[4]

# Generated at 2022-06-13 03:18:16.206275
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact_collector = PythonFactCollector()
    result = python_fact_collector.collect()

    assert result['python']['version']['major'] == sys.version_info[0]
    assert result['python']['version']['minor'] == sys.version_info[1]
    assert result['python']['version']['micro'] == sys.version_info[2]
    assert result['python']['version']['releaselevel'] == sys.version_info[3]
    assert result['python']['version']['serial'] == sys.version_info[4]
    assert result['python']['version_info'] == list(sys.version_info)
    assert result['python']['executable'] == sys.executable

# Generated at 2022-06-13 03:18:25.456480
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector()
    fact_result = fact_collector.collect()
    assert "python" in fact_result
    assert fact_result['python']['version']['major'] == sys.version_info[0]
    assert fact_result['python']['version']['minor'] == sys.version_info[1]
    assert fact_result['python']['version']['micro'] == sys.version_info[2]
    assert fact_result['python']['version']['releaselevel'] == sys.version_info[3]
    assert fact_result['python']['version']['serial'] == sys.version_info[4]
    assert fact_result['python']['version_info'] == list(sys.version_info)

# Generated at 2022-06-13 03:18:33.276667
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    collector = PythonFactCollector()
    facts = collector.collect()
    assert isinstance(facts, dict)
    assert 'python' in facts
    assert isinstance(facts['python'], dict)
    assert 'version' in facts['python']
    assert isinstance(facts['python']['version'], dict)
    assert 'version_info' in facts['python']
    assert isinstance(facts['python']['version_info'], list)
    assert 'executable' in facts['python']
    assert isinstance(facts['python']['executable'], str)
    assert 'has_sslcontext' in facts['python']
    assert isinstance(facts['python']['has_sslcontext'], bool)

# Generated at 2022-06-13 03:18:39.717524
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector()
    result = fact_collector.collect()
    assert result['python']['executable']
    assert result['python']['version']['major']
    assert result['python']['version']['minor']
    assert result['python']['version']['micro']
    assert result['python']['version']['releaselevel']
    assert result['python']['version']['serial']
    assert result['python']['version_info']
    assert result['python']['type']

# Generated at 2022-06-13 03:18:41.157758
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pc = PythonFactCollector()

    # pc.collect should return a dict
    assert isinstance(pc.collect(),dict)

# Generated at 2022-06-13 03:18:48.365508
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # pylint: disable=line-too-long
    """
    Unit-test PythonFactCollector.collect under various configurations
    """
    # pylint: disable=protected-access
    # Arrange
    pythonfactcollector_obj = PythonFactCollector()
    python_facts = {}

# Generated at 2022-06-13 03:18:49.774348
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector(None)
    pfc.collect()


# Generated at 2022-06-13 03:18:56.439972
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    # Create a PythonFactCollector object
    python_collector = PythonFactCollector()

    # Check what is return by the collect method
    python_facts = python_collector.collect()

    # Check number of keys in return dict (python, ansible_env)
    assert len(python_facts.keys()) == 1

    # Check if python_facts['python'] is a dict
    assert isinstance(python_facts['python'], dict)

# Generated at 2022-06-13 03:19:41.194590
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    try:
        from ssl import create_default_context, SSLContext
        del create_default_context
        del SSLContext
        HAS_SSLCONTEXT = True
    except ImportError:
        HAS_SSLCONTEXT = False

    python_facts = {
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

# Generated at 2022-06-13 03:19:50.725937
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts_dict = {
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
    python_facts_dict['python']['type'] = sys.subversion[0]

    pfc = PythonFactCollector()
    collected_facts = pfc.collect()
    assert collected_facts['ansible_python'] == python_facts_dict



# Generated at 2022-06-13 03:19:56.531834
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    # Make sure the method collect is present
    assert hasattr(PythonFactCollector, 'collect'), "Class PythonFactCollector does not have a collect method"

    # Make sure the method is callable
    assert callable(PythonFactCollector.collect), "Method collect is not callable"

    # Make sure the method returns a dictionary
    assert type(PythonFactCollector.collect()) == dict, "Return value of collect method is not a dictionary"


# Generated at 2022-06-13 03:20:01.687554
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact_collector = PythonFactCollector()
    result = python_fact_collector.collect()
    assert isinstance(result, dict)
    assert len(result['python']['version_info']) == 5
    assert 'version' in result['python']
    assert 'executable' in result['python']
    assert 'has_sslcontext' in result['python']
    assert 'type' in result['python']

# Generated at 2022-06-13 03:20:09.223937
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    for py_ver in ('2.6', '2.7', '3.2', '3.3', '3.4', '3.5'):
        fact_collector = PythonFactCollector(module=None,
                                             collected_facts={})
        facts = fact_collector.collect(module=None,
                                       collected_facts={})
        print("Python facts for python version %s: %s" % (py_ver, facts))
        assert sys.version_info[0] == facts['python']['version']['major']
        assert sys.version_info[1] == facts['python']['version']['minor']
        assert sys.version_info[2] == facts['python']['version']['micro']

# Generated at 2022-06-13 03:20:14.329019
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


# Generated at 2022-06-13 03:20:15.708181
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pc = PythonFactCollector()
    assert 'python' in pc.collect()

# Generated at 2022-06-13 03:20:21.502753
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pythonFactCollector = PythonFactCollector()

    actual = pythonFactCollector.collect()
    assert actual['python']['version']['major'] == sys.version_info[0]
    assert actual['python']['version']['minor'] == sys.version_info[1]
    assert actual['python']['version']['micro'] == sys.version_info[2]
    assert actual['python']['version']['releaselevel'] == sys.version_info[3]
    assert actual['python']['version']['serial'] == sys.version_info[4]

    assert actual['python']['version_info'] == list(sys.version_info)
    assert actual['python']['executable'] == sys.executable
    assert actual['python']['has_sslcontext'] == HAS

# Generated at 2022-06-13 03:20:28.771124
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fc = PythonFactCollector
    facts = fc.collect()
    if not isinstance(facts, dict):
        raise Exception("Returned facts are not a dict")
    if 'python' not in facts.keys():
        raise Exception("Python not in returned facts")
    if not isinstance(facts['python'], dict):
        raise Exception("Python facts are not a dict")
    if 'version' not in facts['python'].keys():
        raise Exception("Python version not in python facts")
    if not isinstance(facts['python']['version'], dict):
        raise Exception("Python version facts are not a dict")
    if 'version_info' not in facts['python'].keys():
        raise Exception("Python version info not in python facts")

# Generated at 2022-06-13 03:20:32.393325
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector()
    facts = fact_collector.collect()
    assert facts['python']['version']['releaselevel'] == 'final'
    assert facts['python']['executable'] == sys.executable

# Generated at 2022-06-13 03:21:51.512758
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Import module
    import ansible.module_utils.facts.collectors.python as test_python

    # Instantiate class
    my_obj = test_python.PythonFactCollector()

    # Test collect method
    my_obj.collect()

    # Compare results
    assert my_obj.collect() == {'python': {'version': {'major': 3, 'minor': 6, 'micro': 4, 'releaselevel': 'final', 'serial': 0}, 'version_info': [3, 6, 4, 'final', 0], 'executable': '/usr/bin/python', 'has_sslcontext': True, 'type': 'CPython'}}

# Generated at 2022-06-13 03:22:02.754275
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector()
    test_facts = pfc.collect()

    assert 'ansible_python' in test_facts
    assert 'python' in test_facts['ansible_python']
    assert 'version' in test_facts['ansible_python']['python']
    assert 'major' in test_facts['ansible_python']['python']['version']
    assert 'minor' in test_facts['ansible_python']['python']['version']
    assert 'micro' in test_facts['ansible_python']['python']['version']
    assert 'releaselevel' in test_facts['ansible_python']['python']['version']
    assert 'serial' in test_facts['ansible_python']['python']['version']
    assert 'version_info'

# Generated at 2022-06-13 03:22:09.058897
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

# Generated at 2022-06-13 03:22:11.869893
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    try:
        pfc = PythonFactCollector()
    except:
        assert False, "Failed to instantiate PythonFactCollector"

    try:
        pfc.collect()
    except:
        assert False, "Error running fact collector"

# Generated at 2022-06-13 03:22:18.429961
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """
    Tests for AnsibleModule.run_command use wrong python version for
    sys.version_info, so we have to fix it here.
    """
    sys.version_info = (1, 2, 3, 'alpha', 5)
    python_fact_collector = PythonFactCollector()
    result = python_fact_collector.collect()
    assert result

    # Test that the result has the correct structure
    assert result['python']['version']['major'] == 1
    assert result['python']['version']['minor'] == 2
    assert result['python']['version']['micro'] == 3
    assert result['python']['version']['releaselevel'] == 'alpha'
    assert result['python']['version']['serial'] == 5