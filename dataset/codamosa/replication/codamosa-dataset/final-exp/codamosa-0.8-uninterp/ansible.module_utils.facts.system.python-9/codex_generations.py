

# Generated at 2022-06-13 03:12:16.573044
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    c = PythonFactCollector()
    facts = c.collect()
    assert 'python' in facts
    assert 'version' in facts['python']
    assert 'version_info' in facts['python']
    assert 'executable' in facts['python']


if __name__ == '__main__':
    print(__doc__)

# Generated at 2022-06-13 03:12:21.067726
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    python_facts = PythonFactCollector().collect()

    # Check if version_info is correct
    if sys.version_info[0] != python_facts['python']['version']['major'] or \
        sys.version_info[1] != python_facts['python']['version']['minor'] or \
        sys.version_info[2] != python_facts['python']['version']['micro'] or \
        sys.version_info[3] != python_facts['python']['version']['releaselevel'] or \
        sys.version_info[4] != python_facts['python']['version']['serial']:
            raise Exception("PythonCollector: collect: version or version_info is wrong")

    # Check if executable is correct

# Generated at 2022-06-13 03:12:36.555083
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    # Initialize PythonFactCollector object
    python_collector = PythonFactCollector()

    # Call method collect of PythonFactCollector object
    python_facts = python_collector.collect()

    assert python_facts['python']['version']
    assert python_facts['python']['version_info']
    assert python_facts['python']['executable']
    assert python_facts['python']['type']
    assert python_facts['python']['has_sslcontext']

    # Print fact data collected
    print (python_facts)

if __name__ == "__main__":
    test_PythonFactCollector_collect()

# Generated at 2022-06-13 03:12:38.560198
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Create an instance
    python_collector_instance = PythonFactCollector()

    # Call method collect
    python_collector_instance.collect()

if __name__ == '__main__':
    test_PythonFactCollector_collect()

# Generated at 2022-06-13 03:12:56.188934
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = PythonFactCollector()
    facts = python_facts.collect()
    assert facts['python']['version']['major'] == sys.version_info[0]
    assert facts['python']['version']['minor'] == sys.version_info[1]
    assert facts['python']['version']['micro'] == sys.version_info[2]
    assert facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert facts['python']['version']['serial'] == sys.version_info[4]
    assert facts['python']['version_info'] == list(sys.version_info)
    assert facts['python']['executable'] == sys.executable
    assert facts['python']['has_sslcontext'] == HAS_SS

# Generated at 2022-06-13 03:13:00.201394
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    pfc = PythonFactCollector()
    pf = pfc.collect()

    assert isinstance(pf['python']['version'] , dict)
    assert isinstance(pf['python']['version_info'] , list)
    assert isinstance(pf['python']['executable'] , (type(''), type(u'')))
    assert isinstance(pf['python']['has_sslcontext'] , bool)
    assert isinstance(pf['python']['type'] , (type(''), type(u'')))


if __name__ == '__main__':
    test_PythonFactCollector_collect()
    # sys.exit(1)

# Generated at 2022-06-13 03:13:05.299256
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """Pytest for PythonFactCollector().collect() should return python"""
    result = PythonFactCollector().collect(module=None,
                                           collected_facts=None)
    assert result['python']


# Generated at 2022-06-13 03:13:15.089924
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """
    Check that method collect of class PythonFactCollector
    return correct result for every version of python

    :return:
    """
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


# Generated at 2022-06-13 03:13:24.588834
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """
    This function is used to test collect method of PythonFactCollector
    :return:
    """
    python_facts = PythonFactCollector().collect()

    assert isinstance(python_facts, dict)
    assert isinstance(python_facts['python'], dict)
    assert isinstance(python_facts['python']['version'], dict)
    assert isinstance(python_facts['python']['version_info'], list)
    assert isinstance(python_facts['python']['executable'], str)
    assert isinstance(python_facts['python']['has_sslcontext'], bool)

# Generated at 2022-06-13 03:13:26.640585
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """
    Test if a fact is returned
    """

    factcollector = PythonFactCollector()
    assert factcollector.collect(module=None, collected_facts=None)

# Generated at 2022-06-13 03:13:35.728278
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """
    This is a unit test for method "collect" of class "PythonFactCollector".
    """
    pf = PythonFactCollector()
    pf_collect = pf.collect()

    assert isinstance(pf_collect, dict)
    assert pf_collect['python']['version']['major'] == 3
    assert isinstance(pf_collect['python']['version_info'], list)

# Generated at 2022-06-13 03:13:44.861553
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    fact_collector = PythonFactCollector()
    collected_facts = fact_collector.collect(module=None, collected_facts={})
    # Check that we have the 'python' key in the collected facts
    assert 'python' in collected_facts
    # Check that all the keys of the 'python' subdictionary are in the
    # returned dictionary
    assert 'version' in collected_facts['python']
    assert 'version_info' in collected_facts['python']
    assert 'executable' in collected_facts['python']
    assert 'type' in collected_facts['python']
    assert 'has_sslcontext' in collected_facts['python']

    # Check that we have the 'major', 'minor', 'micro', 'releaselevel'
    # and 'serial' keys in the 'version' subdictionary

# Generated at 2022-06-13 03:13:49.973875
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact_collector = PythonFactCollector()
    python_facts = python_fact_collector.collect()
    assert python_facts['python']['version']['major'] >= 2

# Generated at 2022-06-13 03:13:59.266461
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact_collector = PythonFactCollector()
    py_facts = python_fact_collector.collect()
    assert py_facts['python']['version']
    assert isinstance(py_facts['python']['version']['major'], int)
    assert isinstance(py_facts['python']['version']['minor'], int)
    assert isinstance(py_facts['python']['version']['micro'], int)
    assert isinstance(py_facts['python']['version']['releaselevel'], str)
    assert isinstance(py_facts['python']['version']['serial'], int)
    assert py_facts['python']['version_info']
    assert isinstance(py_facts['python']['version_info'], list)
    assert py_

# Generated at 2022-06-13 03:14:03.472900
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector()
    fact_cache = fact_collector.collect(None, None)
    assert isinstance(fact_cache, dict)
    assert isinstance(fact_cache['python'], dict)

# Generated at 2022-06-13 03:14:04.712310
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    fact_collector = PythonFactCollector()
    fact_collector.collect()

# Generated at 2022-06-13 03:14:08.566289
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = PythonFactCollector().collect()
    assert 'python' in python_facts
    assert 'version' in python_facts['python']
    assert 'version_info' in python_facts['python']
    assert 'executable' in python_facts['python']
    assert 'has_sslcontext' in python_facts['python']
    assert 'type' in python_facts['python']

# Generated at 2022-06-13 03:14:15.380295
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_collector = PythonFactCollector()
    returned_facts = python_collector.collect()

    # Assert python fact contains key 'python'
    assert returned_facts.has_key('python')

    # Assert python fact contains key 'version'
    assert returned_facts['python'].has_key('version')

    # Assert python fact contains key 'version_info'
    assert returned_facts['python'].has_key('version_info')

    # Assert python fact contains key 'executable'
    assert returned_facts['python'].has_key('executable')

# Generated at 2022-06-13 03:14:24.673336
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # By default, collect() should iterate over all subclasses of
    # BaseFactCollector and invoke their collect() methods.
    c = PythonFactCollector()
    collected_facts = {}
    c.collect(collected_facts=collected_facts)

    assert 'python' in collected_facts
    assert 'version' in collected_facts['python']
    assert 'major' in collected_facts['python']['version']
    assert 'minor' in collected_facts['python']['version']
    assert 'micro' in collected_facts['python']['version']
    assert 'releaselevel' in collected_facts['python']['version']
    assert 'serial' in collected_facts['python']['version']
    assert 'version_info' in collected_facts['python']

# Generated at 2022-06-13 03:14:33.178608
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """
    Unit test for method collect of class PythonFactCollector
    """
    pfc = PythonFactCollector()
    # Tests for python2
    if sys.version_info[0] == 2:
        assert len(pfc.collect().values()) == 1
        assert pfc.collect().values()[0]['executable'] == sys.executable
        assert pfc.collect().values()[0]['has_sslcontext'] == False
        assert 'type' in pfc.collect().values()[0]
        assert 'version' in pfc.collect().values()[0]
        assert 'version_info' in pfc.collect().values()[0]

    # Tests for python3
    elif sys.version_info[0] == 3:
        assert len(pfc.collect().values()) == 1
        assert p

# Generated at 2022-06-13 03:14:50.706113
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    import sys

    python_facts = PythonFactCollector().collect()

    assert python_facts == {
        'python': {
            'type': 'CPython',
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

# Generated at 2022-06-13 03:14:57.004188
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    py_fc = PythonFactCollector()
    collected_facts = py_fc.collect()
    assert collected_facts['python']['version']['major'] == 3
    assert collected_facts['python']['version']['minor'] == 5
    assert collected_facts['python']['version']['micro'] == 4
    assert collected_facts['python']['version']['releaselevel'] == 'final'
    assert collected_facts['python']['version']['serial'] == 0
    assert collected_facts['python']['type'] == 'CPython'

# Generated at 2022-06-13 03:15:05.837156
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    test_python_facts = {
        'python': {
            'executable': '/usr/bin/python',
            'has_sslcontext': True,
            'type': 'CPython',
            'version': {
                'major': '2',
                'micro': '7',
                'minor': '9',
                'releaselevel': 'final',
                'serial': '0'
            },
            'version_info': [2, 7, 9, 'final', 0]
        }
    }

    pythonFactCollector = PythonFactCollector()
    result = pythonFactCollector.collect()
    assert result == test_python_facts

# Generated at 2022-06-13 03:15:14.259857
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    collector = PythonFactCollector()

    facts = collector.collect()
    assert facts.get('python') is not None
    assert facts['python'].get('version') is not None
    assert facts['python']['version'].get('major') is not None
    assert facts['python']['version'].get('minor') is not None
    assert facts['python']['version'].get('micro') is not None
    assert facts['python']['version'].get('releaselevel') is not None
    assert facts['python']['version'].get('serial') is not None
    assert facts['python'].get('version_info') is not None
    assert facts['python'].get('executable') is not None
    assert facts['python'].get('has_sslcontext') is not None

# Generated at 2022-06-13 03:15:24.233065
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """
    Unit test for method collect of class PythonFactCollector
    """
    # Test setup
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

# Generated at 2022-06-13 03:15:34.628713
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """Test the collect() method of the PythonFactCollector"""

    # Create a PythonFactCollector
    python_facts_collector = PythonFactCollector(
        module=None,
        collected_facts=None
    )

    # Collect our Python facts
    facts = python_facts_collector.collect(
        module=None,
        collected_facts=None
    )

    # Did we get the expected keys?
    assert sorted(facts.keys()) == ['python']
    assert sorted(facts['python'].keys()) == ['executable', 'has_sslcontext', 'type', 'version', 'version_info']

    # Did we get the expected values?
    assert isinstance(facts['python']['version']['major'], int)
    assert isinstance(facts['python']['version']['minor'], int)

# Generated at 2022-06-13 03:15:40.951801
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    import sys
    collector = PythonFactCollector()
    actual_facts = collector.collect()

    expected_version_info = list(sys.version_info)
    expected_version = {
        'major': sys.version_info[0],
        'minor': sys.version_info[1],
        'micro': sys.version_info[2],
        'releaselevel': sys.version_info[3],
        'serial': sys.version_info[4]
    }
    expected_executable = sys.executable
    expected_has_sslcontext = HAS_SSLCONTEXT

    try:
        expected_type = sys.subversion[0]
    except AttributeError:
        try:
            expected_type = sys.implementation.name
        except AttributeError:
            expected_type = None

    expected_

# Generated at 2022-06-13 03:15:49.629566
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = dict()
    python_facts['python'] = dict()
    python_facts['python']['version'] = dict()
    python_facts['python']['version']['major'] = sys.version_info[0]
    python_facts['python']['version']['minor'] = sys.version_info[1]
    python_facts['python']['version']['micro'] = sys.version_info[2]
    python_facts['python']['version']['releaselevel'] = sys.version_info[3]
    python_facts['python']['version']['serial'] = sys.version_info[4]
    python_facts['python']['version_info'] = list()

# Generated at 2022-06-13 03:15:57.915894
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    class AnsibleModuleMock():
        def __init__(self, params):
            self.params = params

    class AnsibleFactsMock():
        def __init__(self, module):
            self.module = module

    class BaseFactCollectorMock():
        def __init__(self):
            self.test = 'test'

    ansible_module = AnsibleModuleMock('value')
    ansible_facts = AnsibleFactsMock(ansible_module)
    ansible_collector = BaseFactCollectorMock()
    ansible_python_collector = PythonFactCollector(ansible_module, ansible_facts, ansible_collector)

    result = ansible_python_collector.collect()

    assert 'python' in result

# Generated at 2022-06-13 03:16:01.683532
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    python_facts = PythonFactCollector().collect()

    assert 'python' in python_facts
    assert 'version' in python_facts['python']
    assert 'version_info' in python_facts['python']
    assert 'executable' in python_facts['python']
    assert 'type' in python_facts['python']
    assert 'has_sslcontext' in python_facts['python']

    # Check the executable is valid and executable
    import os
    assert os.path.exists(python_facts['python']['executable'])
    assert os.access(python_facts['python']['executable'], os.X_OK)

# Generated at 2022-06-13 03:16:19.529080
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact_collector = PythonFactCollector()
    python_facts = python_fact_collector.collect()
    assert 'python' in python_facts.keys()
    python = python_facts['python']
    assert 'version' in python.keys()
    version = python['version']
    assert 'major' in version.keys()
    assert 'minor' in version.keys()
    assert 'micro' in version.keys()
    assert 'releaselevel' in version.keys()
    assert 'serial' in version.keys()
    assert 'version_info' in python.keys()
    version_info = python['version_info']
    assert len(version_info) == 5
    assert version_info[0] == version['major']
    assert version_info[1] == version['minor']

# Generated at 2022-06-13 03:16:26.803753
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.collector.python import PythonFactCollector
    import ansible.module_utils.facts.collector.python as python_collector
    import sys
    c = Collector()
    p = PythonFactCollector(c)

    p.collect()

    assert c.fact_cache['python']
    assert c.fact_cache['python']['executable'] == sys.executable
    assert c.fact_cache['python']['version_info'] == sys.version_info
    assert c.fact_cache['python']['has_sslcontext'] == python_collector.HAS_SSLCONTEXT
    assert c.fact_cache['python']['version']['major'] == sys.version_info[0]


# Generated at 2022-06-13 03:16:31.160582
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact_collector = PythonFactCollector()
    result = python_fact_collector.collect()
    assert result == {'python': {'version': {'major': 3, 'minor': 8, 'micro': 2, 'releaselevel': 'final', 'serial': 0},
                                 'version_info': [3, 8, 2, 'final', 0],
                                 'executable': '/home/travis/virtualenv/python3.8.2/bin/python',
                                 'has_sslcontext': True,
                                 'type': 'CPython'}}

# Generated at 2022-06-13 03:16:38.426156
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact_collector = PythonFactCollector()
    data = python_fact_collector.collect()
    assert data['python']['version']['major'] == sys.version_info[0]
    assert data['python']['version']['minor'] == sys.version_info[1]
    assert data['python']['version']['micro'] == sys.version_info[2]
    assert data['python']['version']['releaselevel'] == sys.version_info[3]
    assert data['python']['version']['serial'] == sys.version_info[4]
    assert data['python']['version_info'] == list(sys.version_info)
    assert data['python']['executable'] == sys.executable

# Generated at 2022-06-13 03:16:40.529385
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = PythonFactCollector().collect()
    assert 'python' in python_facts
    assert 'executable' in python_facts['python']
    assert 'version' in python_facts['python']
    assert 'type' in python_facts['python']

# Generated at 2022-06-13 03:16:45.268041
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    expected_facts = {
        'python': {
            'has_sslcontext': True,
            'executable': sys.executable,
            'version_info': list(sys.version_info),
            'type': sys.implementation.name,
            'version': {
                'releaselevel': sys.version_info[3],
                'micro': sys.version_info[2],
                'serial': sys.version_info[4],
                'major': sys.version_info[0],
                'minor': sys.version_info[1]
            }
        }
    }

    assert expected_facts == PythonFactCollector().collect()

# Generated at 2022-06-13 03:16:46.196269
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    py_collector = PythonFactCollector()
    result = py_collector.collect()
    print(result)

# Generated at 2022-06-13 03:16:48.415924
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    facter = PythonFactCollector()
    result = facter.collect()
    assert result['python']['version_info'] == list(sys.version_info)
    assert result['python']['executable'] == sys.executable
    assert isinstance(result['python']['version']['major'], int)

# Generated at 2022-06-13 03:16:49.510414
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    c = PythonFactCollector()
    assert dict == c.collect().__class__
    assert 'python' in c.collect()

# Generated at 2022-06-13 03:16:57.068006
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Given a PythonFactCollector instance
    python_collector = PythonFactCollector()

    # When I call its method collect
    python_facts = python_collector.collect()

    # Then I get a dictionary of facts about Python
    assert 'version' in python_facts['python']
    assert 'version_info' in python_facts['python']
    assert 'executable' in python_facts['python']
    assert 'has_sslcontext' in python_facts['python']

# Generated at 2022-06-13 03:17:10.867746
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    sys.modules['ansible_collected_facts'] = BaseFactCollector()
    # Create a instance of class C
    python_fact_collector = PythonFactCollector()
    # Call the collect method
    facts = python_fact_collector.collect()
    # Assert if the facts are generated or not
    assert ('python' in facts)

# Generated at 2022-06-13 03:17:18.353886
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    '''Test collect() of PythonFactCollector class'''
    python_fact_collector = PythonFactCollector()
    python_facts = python_fact_collector.collect()
    assert 'python' in python_facts
    assert 'version' in python_facts['python']
    assert 'version_info' in python_facts['python']
    assert 'major' in python_facts['python']['version']
    assert 'minor' in python_facts['python']['version']
    assert 'micro' in python_facts['python']['version']
    assert 'releaselevel' in python_facts['python']['version']
    assert 'serial' in python_facts['python']['version']
    assert 'has_sslcontext' in python_facts['python']


# Generated at 2022-06-13 03:17:25.101324
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    os_facts = {}
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
        'has_sslcontext': HAS_SSLCONTEXT}


# Generated at 2022-06-13 03:17:33.337431
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fake_module = {'params': {'filter': '*'}}

    # The version information would be returned in a format like (2, 7, 9, 'final', 0). To mock it, I need to
    # create a tuple object in which the first four elements are constants
    sys.version_info = (2, 7, 9, 'final', 0)
    sys.executable = 'path/to/python2.7'
    sys.implementation = type('sys.implementation', (object,), {'name': 'cpython'})()

    python_facts = PythonFactCollector().collect(fake_module)
    assert len(python_facts) == 1
    assert python_facts['python']['version']['major'] == sys.version_info[0]

# Generated at 2022-06-13 03:17:34.627537
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    result = PythonFactCollector().collect()
    assert 'python' in result
    assert isinstance(result['python']['version_info'], list)

# Generated at 2022-06-13 03:17:39.932957
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    foo_instance = PythonFactCollector()

# Generated at 2022-06-13 03:17:46.672957
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    class MockModule(object):
        def __init__(self):
            self.params = dict()

    class MockCollectedFacts(object):
        def __init__(self):
            self.data = dict()

    python_collector = PythonFactCollector()
    module = MockModule()
    collected_facts = MockCollectedFacts()
    results = python_collector.collect(module=module, collected_facts=collected_facts)

    assert 'python' in results

# Generated at 2022-06-13 03:17:49.580156
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    collector = PythonFactCollector()
    python_facts = collector.collect()
    assert 'python' in python_facts
    assert 'version' in python_facts['python']
    assert 'version_info' in python_facts['python']
    assert 'type' in python_facts['python']

# Generated at 2022-06-13 03:18:00.398303
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    '''This test runs the collect method of class PythonFactCollector and
    checks the result for correctness.
    '''
    import ansible.module_utils.facts.collector
    import sys

    fact_collector = ansible.module_utils.facts.collector.get_collector('python')
    result = fact_collector.collect()


# Generated at 2022-06-13 03:18:10.038348
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    import ansible.module_utils.facts.collector

    # Mock ansible.module_utils.facts.collector.BaseFactCollector
    BaseFactCollector_mock = ansible.module_utils.facts.collector.BaseFactCollector
    BaseFactCollector_mock.__new__ = lambda cls, *args, **kwargs: BaseFactCollector_mock
    BaseFactCollector_mock.__init__ = lambda self, *args, **kwargs: None
    BaseFactCollector_mock.name = 'test_BaseFactCollector'
    sys.modules["ansible.module_utils.facts.collector.BaseFactCollector"] = BaseFactCollector_mock
    from ansible.module_utils.facts.collector.python import PythonFactCollector

    pfc = PythonFactCollector()


# Generated at 2022-06-13 03:18:35.374856
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """Return collected facts."""
    python_fact_collector = PythonFactCollector()
    facts = python_fact_collector.collect()

    assert facts['python']
    assert facts['python']['version']['major'] == sys.version_info[0]
    assert facts['python']['version']['minor'] == sys.version_info[1]
    assert facts['python']['version']['micro'] == sys.version_info[2]
    assert facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert facts['python']['version']['serial'] == sys.version_info[4]
    assert facts['python']['version_info'] == list(sys.version_info)
    assert facts['python']['executable'] == sys

# Generated at 2022-06-13 03:18:43.352635
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    c = PythonFactCollector()
    assert isinstance(c.collect()['python']['version'], dict)
    assert isinstance(c.collect()['python']['version_info'], list)
    assert c.collect()['python']['version']['major'] == sys.version_info[0]
    assert c.collect()['python']['version']['minor'] == sys.version_info[1]
    assert c.collect()['python']['version']['micro'] == sys.version_info[2]
    assert c.collect()['python']['version']['releaselevel'] == sys.version_info[3]
    assert c.collect()['python']['version']['serial'] == sys.version_info[4]

# Generated at 2022-06-13 03:18:48.543787
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector()
    assert fact_collector.collect() == {
        'python': {
            'type': 'CPython',
            'has_sslcontext': HAS_SSLCONTEXT,
            'version_info': [2, 7, 2, 'final', 0],
            'executable': '/usr/bin/python',
            'version': {
                'micro': 2,
                'minor': 7,
                'releaselevel': 'final',
                'serial': 0,
                'major': 2
            }
        }
    }

# Generated at 2022-06-13 03:18:58.211979
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """Test function to check python version info"""
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

    # Check python type if sys.subversion exists
    if hasattr(sys, "subversion"):
        python_facts['python']['type'] = sys.subversion[0]

# Generated at 2022-06-13 03:19:04.554541
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    collector = PythonFactCollector({})
    facts = collector.collect(None, None)
    assert facts == {'python': {'version': {'major': 2, 'minor': 7, 'micro': 12, 'releaselevel': 'final', 'serial': 0}, 'version_info': [2, 7, 12, 'final', 0], 'executable': '/usr/bin/python', 'has_sslcontext': True, 'type': 'CPython'}}

# Generated at 2022-06-13 03:19:10.104186
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Mock method
    class MockModule(object):
        pass
    mock_module = MockModule()

    import sys
    real_sys = sys
    result = None
    sys = real_sys

# Generated at 2022-06-13 03:19:14.526850
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """
    Test the PythonFactCollector.collect method with a tiny unit test.

    The test is implemented in python3.x
    """
    if sys.version_info[0] < 3:
        raise RuntimeError('This test requires python3')

    pfc = PythonFactCollector()

    result = pfc.collect()

    assert 'python' in result.keys()
    assert 'version' in result['python'].keys()
    assert 'executable' in result['python'].keys()
    assert 'has_sslcontext' in result['python'].keys()
    assert result['python']['has_sslcontext'] is True

# Generated at 2022-06-13 03:19:25.853934
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    collector = PythonFactCollector()
    result = collector.collect()

    # Execution should be successful
    assert result['success'] == True

    # Check if values are as expected
    assert result['ansible_facts']['python']['version']['major'] == sys.version_info[0]
    assert result['ansible_facts']['python']['version']['minor'] == sys.version_info[1]
    assert result['ansible_facts']['python']['version']['micro'] == sys.version_info[2]
    assert result['ansible_facts']['python']['version']['releaselevel'] == sys.version_info[3]
    assert result['ansible_facts']['python']['version']['serial'] == sys.version_info[4]


# Generated at 2022-06-13 03:19:28.890101
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    py_fact_collector = PythonFactCollector()
    python_facts = py_fact_collector.collect()
    assert python_facts['python']['version']['major'] == sys.version_info[0]

# Generated at 2022-06-13 03:19:34.246777
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector()
    pfc.collect()
    pfc_collected = pfc.collect()

    # Check that collected python facts are not empty
    assert pfc_collected['python']

    # Check that version_info is a list with 5 integers
    assert isinstance(pfc_collected['python']['version_info'], list)
    assert len(pfc_collected['python']['version_info']) == 5
    assert all(isinstance(item, int) for item in pfc_collected['python']['version_info'])

    # Check that executable is a string
    assert isinstance(pfc_collected['python']['executable'], basestring)

    # Check that has_sslcontext is a bool

# Generated at 2022-06-13 03:19:58.972378
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python = PythonFactCollector()
    result = python.collect()
    assert len(result['python']) == 5
    assert result['python']['version']['major'] == sys.version_info[0]
    assert result['python']['version']['minor'] == sys.version_info[1]
    assert result['python']['version']['micro'] == sys.version_info[2]
    assert result['python']['version']['releaselevel'] == sys.version_info[3]
    assert result['python']['version']['serial'] == sys.version_info[4]
    assert result['python']['version_info'] == list(sys.version_info)
    assert result['python']['executable'] == sys.executable

# Generated at 2022-06-13 03:20:00.483889
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    assert 'python' == PythonFactCollector().name
    assert PythonFactCollector().collect()['python']

# Generated at 2022-06-13 03:20:03.055101
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    collect_obj = PythonFactCollector()
    results = collect_obj.collect()
    assert isinstance(results['python'], dict)
    assert results['python']['version']['major'] >= 2



# Generated at 2022-06-13 03:20:07.019797
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    collector = PythonFactCollector(None)

    test_data = collector.collect()

    assert isinstance(test_data, dict)
    assert 'python' in test_data
    assert 'version_info' in test_data['python']
    assert 'executable' in test_data['python']
    assert 'has_sslcontext' in test_data['python']

# Generated at 2022-06-13 03:20:14.758627
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # pylint: disable=missing-docstring
    pyfc = PythonFactCollector()

    # Test collecting facts
    facts = pyfc.collect()

    # Test that we have the 'python' key
    assert 'python' in facts.keys()

    # Test that we have the 'version' key with a dictionary
    assert 'version' in facts['python'].keys()
    assert isinstance(facts['python']['version'], dict)

    # Test that we have the 'version_info' key with a list
    assert 'version_info' in facts['python'].keys()
    assert isinstance(facts['python']['version_info'], list)

    # Test that we have the 'executable' key with an executable path
    assert 'executable' in facts['python'].keys()

# Generated at 2022-06-13 03:20:25.342834
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector()
    facts = fact_collector.collect()
    assert facts['python']['version']['major'] == sys.version_info[0]
    assert facts['python']['version']['minor'] == sys.version_info[1]
    assert facts['python']['version']['micro'] == sys.version_info[2]
    assert facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert facts['python']['version']['serial'] == sys.version_info[4]
    assert facts['python']['version_info'] == list(sys.version_info)
    assert facts['python']['executable'] == sys.executable
    assert 'has_sslcontext' in facts['python']

# Generated at 2022-06-13 03:20:34.997148
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    f = PythonFactCollector()
    fact_data = f.collect()
    assert 'python' in fact_data
    assert fact_data['python']['version']['major'] == sys.version_info[0]
    assert fact_data['python']['version']['minor'] == sys.version_info[1]
    assert fact_data['python']['version']['micro'] == sys.version_info[2]
    assert fact_data['python']['version']['releaselevel'] == sys.version_info[3]
    assert fact_data['python']['version']['serial'] == sys.version_info[4]
    assert fact_data['python']['version_info'] == list(sys.version_info)

# Generated at 2022-06-13 03:20:39.460747
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector()

    fact_collector.collect()
    assert 'python' in fact_collector._collected_facts
    assert 'fact_ids' in fact_collector._collected_facts['python']

    assert fact_collector._collected_facts['python']['fact_ids'] == \
        fact_collector.collect()['fact_ids']

# Generated at 2022-06-13 03:20:46.935068
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils.facts.collectors.python import PythonFactCollector
    from ansible.module_utils._text import to_bytes

    python_collector = PythonFactCollector(FactCollector)
    fact_dict = python_collector.collect()

# Generated at 2022-06-13 03:20:48.887969
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pc = PythonFactCollector()
    result = pc.collect()

# Generated at 2022-06-13 03:21:33.476845
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    PyFC = PythonFactCollector
    pyfc = PyFC()

    # Take python version from sys.version
    # sys.version: '2.7.10 (default, Mar  1 2015, 18:58:54) \n[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.56)]'
    # sys.version_info: (2, 7, 10, 'final', 0)

# Generated at 2022-06-13 03:21:34.741050
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact_collector = PythonFactCollector()
    assert type(python_fact_collector.collect()) is dict

# Generated at 2022-06-13 03:21:36.420568
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    py_fc = PythonFactCollector()
    assert isinstance(py_fc.collect(), dict)
    assert isinstance(py_fc.collect(), dict)

# Generated at 2022-06-13 03:21:43.569081
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    import sys
    import tests.utils as utils
    class MockFactCollector(BaseFactCollector):
        def __init__(self):
            self._fact_ids = set()

    facts = {}
    fact_collector = PythonFactCollector(MockFactCollector())
    python_facts = fact_collector.collect(collected_facts=facts)
    assert python_facts['python']['version']['major'] == sys.version_info[0]
    assert python_facts['python']['version']['minor'] == sys.version_info[1]
    assert python_facts['python']['version']['micro'] == sys.version_info[2]
    assert python_facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert python_facts

# Generated at 2022-06-13 03:21:45.566483
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    import ansible.module_utils.facts.collector as facts_collector
    fc = facts_collector.PythonFactCollector()
    facts = fc.collect()
    assert 'python' in facts

# Generated at 2022-06-13 03:21:50.552321
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact_collector = PythonFactCollector()
    result = python_fact_collector.collect()
    assert result['python']
    assert result['python']['version']
    assert result['python']['version']['major']
    assert result['python']['version']['minor']
    assert result['python']['version']['micro']
    assert result['python']['version']['releaselevel']
    assert result['python']['version']['serial']
    assert result['python']['version_info']
    assert result['python']['executable']
    assert result['python']['has_sslcontext']
    assert result['python']['type']

# Generated at 2022-06-13 03:21:57.608683
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact_collector = PythonFactCollector()
    output = python_fact_collector.collect()
    assert type(output) is dict
    assert output['python']['executable'] == sys.executable
    assert type(output['python']['version']) is dict
    assert type(output['python']['version_info']) is list
    assert type(output['python']['has_sslcontext']) is bool
    assert output['python']['type'] is not None

# Generated at 2022-06-13 03:22:04.228751
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    p = PythonFactCollector()
    facts = p.collect()
    assert isinstance(facts, dict)
    assert isinstance(facts['python']['version'], dict)
    assert isinstance(facts['python']['version_info'], list)
    assert isinstance(facts['python']['executable'], str)
    assert isinstance(facts['python']['type'], str)
    assert isinstance(facts['python']['has_sslcontext'], bool)

# Generated at 2022-06-13 03:22:07.602779
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    import sys
    from ansible.module_utils.facts.collector import BaseFactCollector
    pfc = PythonFactCollector()
    assert isinstance(pfc, BaseFactCollector)
    assert pfc.name == 'python'
    assert pfc._fact_ids == set()
    assert isinstance(pfc.collect(), dict)

# Test idempotentcy of method collect of class PythonFactCollector

# Generated at 2022-06-13 03:22:15.508657
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """
    Unit test for method collect of class PythonFactCollector
    """

    # Initialize class instance
    python_facts = PythonFactCollector()

    # Collect facts
    facts = python_facts.collect()

    # Check version_info
    assert isinstance(facts['python']['version_info'], list)
    # Check version
    assert isinstance(facts['python']['version'], dict)
    assert isinstance(facts['python']['version']['major'], int)
    assert isinstance(facts['python']['version']['minor'], int)
    assert isinstance(facts['python']['version']['micro'], int)
    assert facts['python']['version']['releaselevel'] in ['alpha', 'beta', 'candidate', 'final']