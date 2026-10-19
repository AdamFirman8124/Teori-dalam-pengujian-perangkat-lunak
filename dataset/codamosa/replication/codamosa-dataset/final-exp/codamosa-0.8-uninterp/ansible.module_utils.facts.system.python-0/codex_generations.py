

# Generated at 2022-06-13 03:12:22.779889
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    result = PythonFactCollector().collect()

    assert result['python']['executable'] == sys.executable
    assert result['python']['type'] == 'CPython'
    assert result['python']['has_sslcontext'] == HAS_SSLCONTEXT
    assert result['python']['version']['major'] == sys.version_info[0]
    assert result['python']['version']['minor'] == sys.version_info[1]
    assert result['python']['version']['micro'] == sys.version_info[2]
    assert result['python']['version']['releaselevel'] == sys.version_info[3]
    assert result['python']['version']['serial'] == sys.version_info[4]
    assert result['python']['version_info']

# Generated at 2022-06-13 03:12:35.717722
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Test without parameters
    python_facts = PythonFactCollector().collect()

    assert isinstance(python_facts, dict)
    assert 'python' in python_facts
    assert isinstance(python_facts['python'], dict)

    assert 'type' in python_facts['python']
    assert python_facts['python']['type'] in ('cpython', 'ironpython',
        'jython', 'pypy')

    # Test with parameters
    # Not yet implemented

# Generated at 2022-06-13 03:12:41.461262
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Get a new instance of PythonFactCollector
    pfc = PythonFactCollector()
    # Call its collect method
    res = pfc.collect()
    # Check that it returns a non-empty dict
    assert isinstance(res, dict)
    assert res
    # Check that the returned dict contains python
    assert 'python' in res
    # Check that the returned dict contains a version
    assert 'version' in res['python']
    # Check that the returned dict contains a major version
    assert 'major' in res['python']['version']
    # Check that the returned dict contains a minor version
    assert 'minor' in res['python']['version']
    # Check that the returned dict contains a micro version
    assert 'micro' in res['python']['version']
    # Check that the returned dict contains a releaselevel
   

# Generated at 2022-06-13 03:12:48.928776
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

# Generated at 2022-06-13 03:12:57.024298
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """
    List of dictionaries containing a test case and the expected dictionary
    """
    test_cases = [
        (
            None,
            {
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
        )
    ]

    python_collector = PythonFactCollector()

    for test_case in test_cases:
        input_value,

# Generated at 2022-06-13 03:13:04.514310
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    from ansible.module_utils.facts.collector import get_fact_collector
    from ansible.module_utils.facts.utils import get_as_dict

    # Test PythonFactCollector
    test_fact_collector = get_fact_collector('python')
    collected_facts = test_fact_collector.collect()
    collected_facts_dict = get_as_dict(collected_facts)

    # We expect the Python version to be 2 or 3
    if sys.version_info[0] == 2:
        assert collected_facts_dict['python']['version']['major'] == 2
    elif sys.version_info[0] == 3:
        assert collected_facts_dict['python']['version']['major'] == 3
    else:
        assert False

    # We expect the Python version

# Generated at 2022-06-13 03:13:10.933488
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = PythonFactCollector().collect()
    assert isinstance(python_facts['python']['version'], dict)
    assert isinstance(python_facts['python']['version_info'], list)
    assert python_facts['python']['version']['releaselevel'] == 'final'
    assert python_facts['python']['type'] is not None
    assert python_facts['python']['has_sslcontext'] is not None

# Generated at 2022-06-13 03:13:19.680744
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils.facts.collector import BaseFactCollector
    test_host = 'TEST_HOSTNAME'
    test_sources = ['PythonFactCollector']
    fact_collector = FactCollector(test_sources, test_host)
    fact_collector.collect()
    assert 'python' in fact_collector._collected_facts
    # Check if all key facts are present
    # The following checks should be done with a facts dict created with
    # fact_collector.get_facts() but we mock it because it would be too
    # complicated to create
    test_facts_dict = fact_collector._collected_facts
    assert 'version' in test_facts_dict['python']
    assert 'version_info' in test

# Generated at 2022-06-13 03:13:25.867474
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector()
    actual = pfc.collect()
    assert actual['python']['version']['major'] == 3
    assert actual['python']['version']['minor'] == 5
    assert actual['python']['version']['micro'] == 1
    assert actual['python']['version']['releaselevel'] == 'final'
    assert actual['python']['version']['serial'] == 0
    assert actual['python']['type'] == 'CPython'


# Generated at 2022-06-13 03:13:31.001813
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Create a class object
    pfc = PythonFactCollector()

    # Assert that python version is not empty
    assert pfc.collect()['python']['version'] == {'major': sys.version_info[0], 'minor': sys.version_info[1], 'micro': sys.version_info[2], 'releaselevel': sys.version_info[3], 'serial': sys.version_info[4]}

# Generated at 2022-06-13 03:13:33.893161
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    PythonFactCollector().collect()

# Generated at 2022-06-13 03:13:42.886833
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    import sys
    collector = PythonFactCollector()
    facts = collector.collect()

    assert type(facts) == dict
    assert facts['python']['executable'] == sys.executable
    assert facts['python']['version']['major'] == sys.version_info[0]
    assert facts['python']['version']['minor'] == sys.version_info[1]
    assert facts['python']['version']['micro'] == sys.version_info[2]
    assert facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert facts['python']['version']['serial'] == sys.version_info[4]
    assert facts['python']['has_sslcontext'] == HAS_SSLCONTEXT

# Generated at 2022-06-13 03:13:49.676768
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Make sure method has a valid return value
    assert PythonFactCollector().collect()['python'] == {
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
        python_type = sys.subversion[0]
    except AttributeError:
        try:
            python_type = sys.implementation.name
        except AttributeError:
            python_type = None



# Generated at 2022-06-13 03:13:55.298566
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    # Create an instance of PythonFactCollector to test its method
    ifc = PythonFactCollector()
    facts = ifc.collect()

    # Check that facts are gathered well
    assert 'python' in facts
    assert 'version' in facts['python']
    assert 'version_info' in facts['python']
    assert 'executable' in facts['python']
    assert 'type' in facts['python']

# Generated at 2022-06-13 03:14:01.500255
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    _python_facts = {}
    _python_facts['python'] = {
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


# Generated at 2022-06-13 03:14:08.316570
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = PythonFactCollector().collect()
    value = python_facts.get('python')
    assert value['version'] == {'major': sys.version_info[0], 'minor': sys.version_info[1], 'micro': sys.version_info[2], 'releaselevel': sys.version_info[3], 'serial': sys.version_info[4]}
    assert value['version_info'] == list(sys.version_info)
    assert value['executable'] == sys.executable
    assert value['has_sslcontext'] == HAS_SSLCONTEXT

# Generated at 2022-06-13 03:14:12.170413
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_collector = PythonFactCollector()
    collected_facts = dict()
    python_facts = python_collector.collect(collected_facts=collected_facts)
    assert "python" in python_facts
    assert "version" in python_facts['python']
    assert "version_info" in python_facts['python']
    assert "executable" in python_facts['python']
    assert "has_sslcontext" in python_facts['python']


# Generated at 2022-06-13 03:14:20.498117
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = {
        'python': {
            'version': {
                'major': 2,
                'minor': 7,
                'micro': 9,
                'releaselevel': 'final',
                'serial': 0
            },
            'version_info': [
                2,
                7,
                9,
                'final',
                0
            ],
            'executable': '/usr/bin/python',
            'has_sslcontext': False,
            'type': 'CPython'
        }
    }
    pfc = PythonFactCollector()
    assert pfc.collect() == python_facts

# Generated at 2022-06-13 03:14:26.486124
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    python_fact_collector = PythonFactCollector()
    result = python_fact_collector.collect()
    assert result is not None
    assert 'python' in result
    assert 'type' in result['python']
    assert 'version' in result['python']
    assert 'has_sslcontext' in result['python']
    assert 'executable' in result['python']
    assert 'version_info' in result['python']


# Generated at 2022-06-13 03:14:30.781302
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    f = PythonFactCollector()
    assert isinstance(f.collect(), dict)
    assert 'python' in f.collect()
    assert 'version' in f.collect()['python']
    assert 'version_info' in f.collect()['python']
    assert 'executable' in f.collect()['python']
    assert isinstance(f.collect()['python']['version_info'], list)

# Generated at 2022-06-13 03:14:39.400547
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact_collector = PythonFactCollector()
    collected_facts = {}
    collected_facts['ansible_python'] = python_fact_collector.collect()
    assert collected_facts['ansible_python']['python']['version_info'][0] == 3
    assert collected_facts['ansible_python']['python']['version']['major'] == 3

# Generated at 2022-06-13 03:14:45.454061
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    py_fact_collector = PythonFactCollector()
    py_facts = py_fact_collector.collect(dict(), dict())
    assert isinstance(py_facts, dict)
    assert 'python' in py_facts
    assert isinstance(py_facts['python'], dict)
    assert 'type' in py_facts['python']
    assert isinstance(py_facts['python']['type'], str)
    assert 'has_sslcontext' in py_facts['python']
    assert isinstance(py_facts['python']['has_sslcontext'], bool)
    assert 'version' in py_facts['python']
    assert isinstance(py_facts['python']['version'], dict)
    assert 'major' in py_facts['python']['version']
    assert 'minor' in py_facts

# Generated at 2022-06-13 03:14:47.241300
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    py_col = PythonFactCollector()
    assert isinstance(py_col.collect(),dict)

# Generated at 2022-06-13 03:14:54.416183
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    collector = PythonFactCollector()

    facts = dict()
    collector.collect(collected_facts=facts)

    assert 'python' in facts
    assert isinstance(facts['python'], dict)
    assert isinstance(facts['python']['version'], dict)
    assert len(facts['python']['version_info']) == 5
    assert isinstance(facts['python']['type'], str)
    assert isinstance(facts['python']['executable'], str)
    assert isinstance(facts['python']['has_sslcontext'], bool)

# Generated at 2022-06-13 03:15:04.007844
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    collector = PythonFactCollector()
    if sys.version_info[0] < 3:
        python_facts = collector.collect()
        assert python_facts['python']['version']['major'] == 2
        assert python_facts['python']['version']['minor'] == 7
        assert python_facts['python']['executable'] == sys.executable
        assert python_facts['python']['type'] == 'CPython'
    else:
        python_facts = collector.collect()
        assert python_facts['python']['version']['major'] == 3
        assert python_facts['python']['type'] == 'CPython'
        assert python_facts['python']['executable'] == sys.executable

# Generated at 2022-06-13 03:15:07.761723
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = dict(PythonFactCollector().collect(collected_facts=dict()))

    assert isinstance(python_facts['python']['version']['major'], int)
    assert isinstance(python_facts['python']['version']['minor'], int)
    assert isinstance(python_facts['python']['version']['micro'], int)
    assert python_facts['python']['version']['releaselevel'] in ['alpha', 'beta', 'candidate', 'final']
    assert isinstance(python_facts['python']['version']['serial'], int)
    assert isinstance(python_facts['python']['version_info'], list)
    assert isinstance(python_facts['python']['executable'], str)

# Generated at 2022-06-13 03:15:12.989417
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector()
    fact_collector.collect()
    assert fact_collector.collect()['python']['implementation'] == 'CPython'
    assert fact_collector.collect()['python']['version']['major'] == 3
    assert fact_collector.collect()['python']['version']['minor'] == 6
    assert fact_collector.collect()['python']['version']['micro'] == 2

# Generated at 2022-06-13 03:15:23.627164
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Test if python's version_info is a tuple
    assert isinstance(sys.version_info, tuple)
    # Test if the length of python's version_info is 5
    assert len(sys.version_info) == 5
    # Test if the type of the elements of python's version_info is int
    assert isinstance(sys.version_info[0], int)
    assert isinstance(sys.version_info[1], int)
    assert isinstance(sys.version_info[2], int)
    assert isinstance(sys.version_info[3], str)
    assert isinstance(sys.version_info[4], int)

    fact_collector = PythonFactCollector()
    python_facts = fact_collector.collect()
    # Test if the key 'python' exists in the returned dict

# Generated at 2022-06-13 03:15:28.790408
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    import mock
    pfc = PythonFactCollector()

    # Testing that returned collected facts are correct

# Generated at 2022-06-13 03:15:35.514060
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Test the code is not raising any error
    facts_collector = PythonFactCollector()
    facts = facts_collector.collect()

    assert isinstance(facts, dict) and 'python' in facts
    assert isinstance(facts['python'], dict)
    assert isinstance(facts['python']['version'], dict)
    assert isinstance(facts['python']['version_info'], list)
    assert isinstance(facts['python']['executable'], str)
    assert isinstance(facts['python']['type'], str)
    assert isinstance(facts['python']['has_sslcontext'], bool)

# Generated at 2022-06-13 03:15:49.837291
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    import sys

    python_facts = PythonFactCollector().collect()

    assert python_facts['python']['version']['major'] == sys.version_info[0]
    assert python_facts['python']['version']['minor'] == sys.version_info[1]
    assert python_facts['python']['version']['micro'] == sys.version_info[2]
    assert python_facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert python_facts['python']['version']['serial'] == sys.version_info[4]
    assert python_facts['python']['version_info'] == list(sys.version_info)
    assert python_facts['python']['executable'] == sys.executable

# Generated at 2022-06-13 03:15:58.217883
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Required to work in unit tests
    sys.version_info = tuple([0]*5)
    sys.version = 'Python TEST'
    sys.executable = '/usr/bin/python'
    sys.subversion = ['CPython', '2.7.12']

    p = PythonFactCollector()
    assert p.collect() == {
        'python': {
            'version': {
                'major': 0,
                'minor': 0,
                'micro': 0,
                'releaselevel': '',
                'serial': 0
            },
            'version_info': [0, 0, 0, '', 0],
            'executable': '/usr/bin/python',
            'type': 'CPython',
            'has_sslcontext': False
        }
    }


# Generated at 2022-06-13 03:16:07.828664
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """
    Test function. It checks if the module returns a dictionary with the
    expected keys:
        * 'python': {
            * 'version': {
                * 'major': int,
                * 'minor': int,
                * 'micro': int,
                * 'releaselevel': int,
                * 'serial': int
            },
            * 'version_info': list<int>,
            * 'executable': str,
            * 'has_sslcontext': bool,
            * 'type': str,
        }
    """
    # Create an instance of the class
    fact_collector = PythonFactCollector()

    # Call the function collect
    facts = fact_collector.collect()

    # Check the type of the return value
    assert isinstance(facts, dict)

    # Check the content of the return value

# Generated at 2022-06-13 03:16:18.461240
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts import default_collectors


# Generated at 2022-06-13 03:16:21.067727
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = PythonFactCollector().collect()
    assert isinstance(python_facts, dict)
    assert python_facts['python']['version']['major'] == 2

# Generated at 2022-06-13 03:16:22.210312
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector()
    fact_collector.collect()

# Generated at 2022-06-13 03:16:31.108597
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

# Generated at 2022-06-13 03:16:33.709973
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    '''Unit tests for method collect of class PythonFactCollector.'''
    fact_collector = PythonFactCollector()
    fact_data = fact_collector.collect()
    # Verify that the collector collects data
    assert fact_data != {}

# Generated at 2022-06-13 03:16:35.614906
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact_collector = PythonFactCollector()
    # Check that the method returns a dictionary
    assert isinstance(python_fact_collector.collect(), dict)



# Generated at 2022-06-13 03:16:41.708670
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    import sys
    import types

    module = types.ModuleType('test')
    module.sys = sys

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
            'has_sslcontext': HAS_SSLCONTEXT,
        }
    }


# Generated at 2022-06-13 03:16:59.596609
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Prepare
    PFC = PythonFactCollector()
    assert PFC.name == 'python'
    expected_facts = {
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
                'has_sslcontext': HAS_SSLCONTEXT,
                'type': None
            }
        }

# Generated at 2022-06-13 03:17:09.323277
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    from ansible_collections.ansible.community.plugins.module_utils.facts.collector import Collectors
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible_collections.ansible.community.plugins.module_utils.facts.collector import BaseFileSearch

    mock_module = 'ansible.module_utils.facts.collector'
    with mock.patch(mock_module + '.BaseFactCollector.collect') as mockcollect:
        pfc = PythonFactCollector()

        # set up test input
        module = mock.sentinel.module
        collected_facts = mock.sentinel.collected_facts

        # test input
        pfc.collect(module, collected_facts)

        # verify test output

# Generated at 2022-06-13 03:17:15.943565
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    import pytest, pprint
    myFactCollector = PythonFactCollector()
    test_facts = myFactCollector.collect()
    pprint.pprint(test_facts)
    assert test_facts['python']['executable'] == sys.executable
    assert test_facts['python']['has_sslcontext'] == HAS_SSLCONTEXT
    assert not 'python' not in test_facts
    assert not 'type' not in test_facts['python']
    assert not 'version' not in test_facts['python']
    assert not 'version_info' not in test_facts['python']

# Generated at 2022-06-13 03:17:23.639693
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """
    test_PythonFactCollector_collect
    """
    python_fact_collector = PythonFactCollector()
    test_result = python_fact_collector.collect()
    assert 'python' in test_result
    assert 'version' in test_result['python']
    assert type(test_result['python']['version']['major']) is int
    assert type(test_result['python']['version']['minor']) is int
    assert type(test_result['python']['version']['micro']) is int
    assert test_result['python']['version']['releaselevel'] in ['alpha', 'beta', 'candidate', 'final']
    assert type(test_result['python']['version']['serial']) is int

# Generated at 2022-06-13 03:17:32.787965
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    import sys

    x = PythonFactCollector()
    facts = x.collect()

    assert facts['python']['executable'] == sys.executable, 'incorrect python executable detected'
    assert facts['python']['version']['major'] == sys.version_info[0], 'incorrect python major version detected'
    assert facts['python']['version']['minor'] == sys.version_info[1], 'incorrect python minor version detected'
    assert facts['python']['version']['micro'] == sys.version_info[2], 'incorrect python micro version detected'
    assert facts['python']['version']['releaselevel'] == sys.version_info[3], 'incorrect python release level detected'

# Generated at 2022-06-13 03:17:39.473368
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = {
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
            'version_info': list(sys.version_info)
        }
    }
    try:
        python_facts['python']['type'] = sys.subversion[0]
    except AttributeError:
        try:
            python_facts['python']['type'] = sys.implementation.name
        except AttributeError:
            python

# Generated at 2022-06-13 03:17:48.747183
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """Unit test for method collect of class PythonFactCollector"""
    pc = PythonFactCollector()
    facts = pc.collect()
    assert(facts['python']['executable'] == sys.executable)
    assert(facts['python']['type'] in ('CPython', 'IronPython', 'Jython', 'PyPy'))
    assert(facts['python']['version']['major'] == 3)
    assert(facts['python']['version']['minor'] == 4)
    assert(facts['python']['version']['serial'] == 3)
    assert(facts['python']['version']['releaselevel'] == 'final')
    assert(facts['python']['has_sslcontext'] == HAS_SSLCONTEXT)

# Generated at 2022-06-13 03:17:59.120643
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    fc = PythonFactCollector()
    collected_facts = Collector().collect(module=None)
    collected_facts = fc.collect(collected_facts=collected_facts)
    assert isinstance(collected_facts['python']['version']['major'], int)
    assert isinstance(collected_facts['python']['version']['minor'], int)
    assert isinstance(collected_facts['python']['version']['micro'], int)
    assert isinstance(collected_facts['python']['version']['releaselevel'], AnsibleUnsafeText)

# Generated at 2022-06-13 03:18:04.369796
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = PythonFactCollector().collect()

    assert python_facts == {
        'python': {
            'executable': sys.executable,
            'has_sslcontext': HAS_SSLCONTEXT,
            'type': sys.implementation.name,
            'version': {
                'major': sys.version_info[0],
                'minor': sys.version_info[1],
                'micro': sys.version_info[2],
                'releaselevel': sys.version_info[3],
                'serial': sys.version_info[4]
            },
            'version_info': list(sys.version_info)
        }
    }

# Generated at 2022-06-13 03:18:09.346956
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_collector = PythonFactCollector()
    ret = python_collector.collect()
    assert ret.get('python', None) is not None
    assert ret['python'].get('version', None) is not None
    assert ret['python'].get('version_info', None) is not None
    assert ret['python'].get('executable', None) is not None
    assert ret['python'].get('type', None) is not None

# Generated at 2022-06-13 03:18:32.693667
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    py_facts = PythonFactCollector()
    facts = py_facts.collect(None, None)

    assert facts['python']['version']['major'] == sys.version_info[0]
    assert facts['python']['version']['minor'] == sys.version_info[1]
    assert facts['python']['version']['micro'] == sys.version_info[2]
    assert facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert facts['python']['version']['serial'] == sys.version_info[4]
    assert facts['python']['version_info'] == list(sys.version_info)
    assert facts['python']['executable'] == sys.executable
    assert facts['python']['has_sslcontext']

# Generated at 2022-06-13 03:18:41.375728
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    collector = PythonFactCollector()

    facts = collector.collect()

    assert facts['python']['version']['major'] == sys.version_info[0]
    assert facts['python']['version']['minor'] == sys.version_info[1]
    assert facts['python']['version']['micro'] == sys.version_info[2]
    assert facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert facts['python']['version']['serial'] == sys.version_info[4]
    assert facts['python']['version_info'] == list(sys.version_info)
    assert facts['python']['executable'] == sys.executable
    assert facts['python']['has_sslcontext'] == HAS_SSLCONTEXT

# Generated at 2022-06-13 03:18:48.543433
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """
    Python is installed, but the test does not have the executable.
    """
    instance = PythonFactCollector()
    ansible_facts = {'ansible_python': {}}
    result = instance.collect(module=None, collected_facts=ansible_facts)

    assert result['ansible_python']['version_info'] == list(sys.version_info)
    assert result['ansible_python']['version']['major'] == sys.version_info[0]
    assert result['ansible_python']['version']['minor'] == sys.version_info[1]
    assert result['ansible_python']['version']['micro'] == sys.version_info[2]

# Generated at 2022-06-13 03:18:54.542616
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    PythonFactCollector._fact_ids = set()
    facts = PythonFactCollector().collect()
    assert 'python' in facts
    assert 'version' in facts['python']
    assert 'version_info' in facts['python']
    assert 'executable' in facts['python']
    assert 'has_sslcontext' in facts['python']
    assert 'type' in facts['python']

# Generated at 2022-06-13 03:18:58.110040
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = PythonFactCollector.collect()

    assert 'python' in python_facts
    assert 'type' in python_facts['python']
    assert 'version' in python_facts['python']
    assert 'version_info' in python_facts['python']
    assert 'executable' in python_facts['python']
    assert 'has_sslcontext' in python_facts['python']

# Generated at 2022-06-13 03:19:05.003942
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = PythonFactCollector().collect()
    assert python_facts['python']['version']['major'] >= 0
    assert python_facts['python']['version']['minor'] >= 0
    assert python_facts['python']['version']['micro'] >= 0
    assert python_facts['python']['version']['releaselevel'] in ['alpha', 'beta', 'candidate', 'final']
    assert python_facts['python']['version']['serial'] >= 0

# Generated at 2022-06-13 03:19:06.887605
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_collector = PythonFactCollector()
    # collect method should return a dictionary
    assert isinstance(python_collector.collect(), dict)

# Generated at 2022-06-13 03:19:12.856471
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Note that this collects the *current* system Python, not the Python
    # used to run Ansible.
    python_collector = PythonFactCollector()
    facts = python_collector.collect()
    assert facts['python']['version']['major'] == sys.version_info[0]
    assert facts['python']['version']['minor'] == sys.version_info[1]
    assert facts['python']['version']['micro'] == sys.version_info[2]
    assert facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert facts['python']['version']['serial'] == sys.version_info[4]
    assert facts['python']['version_info'] == list(sys.version_info)

# Generated at 2022-06-13 03:19:23.726277
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    import types
    import sys
    import mock
    import os
    import platform

    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils._text import to_text
    from ansible.module_utils.facts import collector

    # Create a mock for the BaseFactCollector and set some return values
    mocked_basefactcollector = mock.create_autospec(BaseFactCollector)
    mocked_basefactcollector.file_exists.return_value = False
    mocked_basefactcollector.parse_win32reg.return_value = None
    mocked_basefactcollector.read_file.return_value = to_text('')

    # Create a mock for the collector module
    mocked_collector = mock.create_autospec(collector)
    mocked_

# Generated at 2022-06-13 03:19:31.950974
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = PythonFactCollector().collect()
    assert len(python_facts) == 1
    assert python_facts['python']['version']['major'] == sys.version_info[0]
    assert python_facts['python']['version']['minor'] == sys.version_info[1]
    assert python_facts['python']['version']['micro'] == sys.version_info[2]
    assert python_facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert python_facts['python']['version']['serial'] == sys.version_info[4]
    assert python_facts['python']['version_info'] == list(sys.version_info)
    assert python_facts['python']['executable'] == sys.executable


# Generated at 2022-06-13 03:20:02.270570
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    c = PythonFactCollector()

    facts = c.collect()

    assert 'python' in facts


# Generated at 2022-06-13 03:20:08.972034
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = PythonFactCollector().collect()

    assert isinstance(python_facts, dict)
    assert len(python_facts) == 1
    assert 'python' in python_facts

    assert isinstance(python_facts["python"], dict)
    assert len(python_facts["python"]) == 5

    assert isinstance(python_facts["python"]["version"], dict)
    assert isinstance(python_facts["python"]["version_info"], list)
    assert isinstance(python_facts["python"]["executable"], str)
    assert isinstance(python_facts["python"]["type"], str)
    assert isinstance(python_facts["python"]["has_sslcontext"], bool)

# Generated at 2022-06-13 03:20:15.956323
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    test_collector = PythonFactCollector()
    collected_facts = test_collector.collect()

    assert collected_facts['python']['version']['major'] == sys.version_info[0]
    assert collected_facts['python']['version']['minor'] == sys.version_info[1]
    assert collected_facts['python']['version']['micro'] == sys.version_info[2]
    assert collected_facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert collected_facts['python']['version']['serial'] == sys.version_info[4]
    assert collected_facts['python']['version_info'] == list(sys.version_info)
    assert collected_facts['python']['executable'] == sys.executable

# Generated at 2022-06-13 03:20:26.470827
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    from ansible_collections.ansible.community.tests.unit.compat.mock import patch, MagicMock
    # mock facts for method collect
    COLLECTED_FACTS = {}
    MODULE = MagicMock()
    # Create instance of class
    PFC = PythonFactCollector()
    # execute method collect of class PythonFactCollector
    FACTS = PFC.collect(MODULE, COLLECTED_FACTS)

# Generated at 2022-06-13 03:20:28.971170
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    collector = PythonFactCollector()
    facts = collector.collect()
    assert facts['python']['version']['major'] >= 2
    assert facts['python']['version']['minor'] >= 4

# Generated at 2022-06-13 03:20:39.216887
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # The following facts should be returned
    expected = {'python': {
                    'version':
                        {
                            'major': 3,
                            'minor': 4,
                            'micro': 0,
                            'releaselevel': 'final',
                            'serial': 0
                        },
                    'version_info':
                        [3, 4, 0, 'final', 0],
                    'executable':
                        sys.executable,
                    'has_sslcontext':
                        HAS_SSLCONTEXT,
                    'type':
                        [name for name in ('cpython', 'ironpython',
                                           'pypy', 'jython', 'stackless')
                         if name in sys.implementation.name][0]
                }}

    # We must be sure the return is the good one
    assert expected == PythonFactCollector().collect

# Generated at 2022-06-13 03:20:46.698563
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    '''Test that PythonFactCollector.collect returns a dictionary as expected'''

    import sys
    import json

    python_collector = PythonFactCollector()
    python_facts = python_collector.collect()

    # Check if version_info and version are sane
    assert python_facts['python']['version_info'][6] == 'final'
    assert python_facts['python']['version']['releaselevel'] == 'final'
    assert python_facts['python']['version']['serial'] == 0
    assert python_facts['python']['version']['micro'] == sys.version_info[2]
    assert python_facts['python']['version']['major'] == sys.version_info[0]

# Generated at 2022-06-13 03:20:51.552448
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    col = PythonFactCollector()
    collected_facts = {}
    col.collect(collected_facts=collected_facts)
    assert collected_facts['python']['version']['major'] == sys.version_info[0]
    assert collected_facts['python']['version']['minor'] == sys.version_info[1]
    assert collected_facts['python']['version']['micro'] == sys.version_info[2]
    assert collected_facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert collected_facts['python']['version']['serial'] == sys.version_info[4]
    assert collected_facts['python']['version_info'] == list(sys.version_info)

# Generated at 2022-06-13 03:20:56.722671
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector()
    facts = fact_collector.collect()

    assert 'python' in facts, 'Python fact is missing'

    python_fact = facts['python']
    print(python_fact)

    assert 'version' in python_fact, 'Python fact version is missing'
    assert 'executable' in python_fact, 'Python fact executable is missing'
    assert 'has_sslcontext' in python_fact, 'Python fact has_sslcontext is missing'

# Generated at 2022-06-13 03:20:57.974180
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_collector = PythonFactCollector()
    result = python_collector.collect()
    assert 'python' in result

# Generated at 2022-06-13 03:22:08.050984
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Create an object of class PythonFactCollector
    obj = PythonFactCollector()

    # Test that the object's method returns the correct result
    assert obj.collect()['python'] == {
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
    # Try to get the name of implementation bases on sys.subversion

# Generated at 2022-06-13 03:22:14.718571
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector()

    assert pfc.collect() == {'python': {
        'executable': sys.executable,
        'has_sslcontext': HAS_SSLCONTEXT,
        'type': 'cpython',
        'version': {
            'major': sys.version_info[0],
            'minor': sys.version_info[1],
            'micro': sys.version_info[2],
            'releaselevel': sys.version_info[3],
            'serial': sys.version_info[4]
        },
        'version_info': list(sys.version_info)
        }
    }