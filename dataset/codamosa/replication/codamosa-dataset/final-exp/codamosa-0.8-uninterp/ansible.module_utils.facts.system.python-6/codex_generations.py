

# Generated at 2022-06-13 03:12:14.243048
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact = PythonFactCollector() 
    python_fact.collect()

# Generated at 2022-06-13 03:12:16.205980
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    collector = PythonFactCollector()
    facts = collector.collect()
    assert facts.get('python')
    assert facts.get('python').get('version')
    assert facts.get('python').get('version_info')

# Generated at 2022-06-13 03:12:20.039886
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    try:
        # test normal invoke
        obj = PythonFactCollector()
        collected_facts = obj.collect()
        assert collected_facts['python']['type'] == 'CPython'

    except NotImplementedError:
        pass

if __name__ == '__main__':
    test_PythonFactCollector_collect()

# Generated at 2022-06-13 03:12:37.677886
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact_collector = PythonFactCollector()
    python_facts = python_fact_collector.collect()
    assert isinstance(python_facts, dict)
    assert 'python' in python_facts
    assert isinstance(python_facts['python'], dict)
    assert 'type' in python_facts['python']
    assert isinstance(python_facts['python']['type'], str)
    assert 'version' in python_facts['python']
    assert isinstance(python_facts['python']['version'], dict)
    assert 'major' in python_facts['python']['version']
    assert isinstance(python_facts['python']['version']['major'], int)
    assert 'minor' in python_facts['python']['version']

# Generated at 2022-06-13 03:12:39.926444
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    c = PythonFactCollector()
    p = c.collect()
    assert 'python' in p
    assert 'version' in p['python']
    assert 'version_info' in p['python']
    assert 'executable' in p['python']
    assert 'type' in p['python']

# Generated at 2022-06-13 03:12:48.175968
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = {}
    python_fact = {
        'version': {
            'major': sys.version_info[0],
            'minor': sys.version_info[1],
            'micro': sys.version_info[2],
            'releaselevel': sys.version_info[3],
            'serial': sys.version_info[4]
        },
        'version_info': list(sys.version_info),
        'executable': sys.executable,
        'type': '',
    }

    if HAS_SSLCONTEXT:
        python_fact['has_sslcontext'] = True
    else:
        python_fact['has_sslcontext'] = False

    if 'subversion' in sys.__dict__:
        python_fact['type'] = sys.subversion[0]

# Generated at 2022-06-13 03:12:55.442622
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = []
    python_fact_collector = PythonFactCollector()
    python_facts.append(python_fact_collector.collect())
    element = python_facts[0]
    print(element)
    assert 'python' in element
    python = element['python']
    assert 'type' in python
    assert 'version' in python
    assert 'executable' in python
    assert 'has_sslcontext' in python
    assert 'version_info' in python

if __name__ == '__main__':
    test_PythonFactCollector_collect()

# Generated at 2022-06-13 03:13:02.681065
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Arrange
    class_under_test = PythonFactCollector()

    # Act
    result = class_under_test.collect()

    # Assert
    assert isinstance(result['python']['version']['serial'], int)
    assert isinstance(result['python']['type'], str)
    assert isinstance(result['python']['version_info'], list)
    assert isinstance(result['python']['executable'], str)
    assert isinstance(result['python']['has_sslcontext'], bool)

# Test for the name of class PythonFactCollector

# Generated at 2022-06-13 03:13:13.305577
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """
    Test if it returns a dict of python facts
    """
    python_collector = PythonFactCollector()
    expected_dict = {
        'python':{
            'version': {
                'major': sys.version_info[0],
                'minor': sys.version_info[1],
                'micro': sys.version_info[2],
                'releaselevel': sys.version_info[3],
                'serial': sys.version_info[4]
            },
            'version_info': list(sys.version_info),
            'executable': sys.executable,
            'type': sys.subversion[0],
            'has_sslcontext': HAS_SSLCONTEXT
        }
    }

    result_dict = python_collector.collect()
    assert result_dict == expected_dict


# Generated at 2022-06-13 03:13:19.544461
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # arrange
    pfc = PythonFactCollector()

    # act
    python_facts = pfc.collect()

    # assert
    assert isinstance(python_facts['python']['version'], dict)
    assert isinstance(python_facts['python']['version_info'], list)
    assert isinstance(python_facts['python']['executable'], str)
    assert isinstance(python_facts['python']['has_sslcontext'], bool)
    assert isinstance(python_facts['python']['type'], str)

# Generated at 2022-06-13 03:13:31.042811
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fc = PythonFactCollector()
    facts = python_fc.collect()
    assert facts == {'python': {'version': {'major': sys.version_info[0],
                                            'minor': sys.version_info[1],
                                            'micro': sys.version_info[2],
                                            'releaselevel': sys.version_info[3],
                                            'serial': sys.version_info[4]},
                                'version_info': list(sys.version_info),
                                'executable': sys.executable,
                                'has_sslcontext': HAS_SSLCONTEXT,
                                'type': sys.subversion[0]}}

# Generated at 2022-06-13 03:13:34.974735
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    # Create a test class
    collector = PythonFactCollector()

    # Test that python facts can be collected
    assert collector.collect() == {
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

# Generated at 2022-06-13 03:13:38.005837
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    instance = PythonFactCollector()
    result = instance.collect(None, None)

    assert 'python' in result
    assert 'version' in result['python']
    assert 'version_info' in result['python']
    assert 'executable' in result['python']
    assert 'has_sslcontext' in result['python']

# Generated at 2022-06-13 03:13:41.597062
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    collector = PythonFactCollector()
    facts = collector.collect()
    assert type(facts) == dict
    assert 'python' in facts
    assert type(facts['python']) == dict
    assert 'version' in facts['python']
    assert 'version_info' in facts['python']
    assert 'executable' in facts['python']
    assert 'has_sslcontext' in facts['python']
    assert 'type' in facts['python']
    assert facts['python']['type'] == 'CPython'

# Generated at 2022-06-13 03:13:43.218298
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact_collector = PythonFactCollector()
    print(python_fact_collector.collect())

# Generated at 2022-06-13 03:13:48.421210
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector()
    assert pfc.collect()['python'] == {
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

# Generated at 2022-06-13 03:13:56.584711
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector()
    fact_collector.collect()
    want = {
        'python': {
            'type': 'CPython',
            'version': {
                'major': 3,
                'micro': 4,
                'minor': 4,
                'releaselevel': 'final',
                'serial': 0
            },
            'version_info': [3, 4, 4, 'final', 0],
            'executable': '/usr/bin/python',
            'has_sslcontext': True
        }
    }
    assert fact_collector.collect() == want

# Generated at 2022-06-13 03:14:01.997584
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

# Generated at 2022-06-13 03:14:04.342151
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pc = PythonFactCollector()
    facts = pc.collect()
    assert 'python' in facts

# Generated at 2022-06-13 03:14:11.474862
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """This will only test attributes of the return value, not the
    actual values themselves.

    As tests are guaranteed to be running on Python 2.7+, has_sslcontext
    should always be True.
    """
    py_facts = PythonFactCollector().collect()
    assert py_facts is not None
    assert type(py_facts) is dict
    assert py_facts['python'] is not None
    assert type(py_facts['python']) is dict
    assert py_facts['python']['has_sslcontext'] is True
    assert py_facts['python']['version'] is not None
    assert type(py_facts['python']['version']) is dict
    assert py_facts['python']['version_info'] is not None
    assert type(py_facts['python']['version_info']) is list


# Generated at 2022-06-13 03:14:27.878883
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    import sys

    f = PythonFactCollector()
    assert f.collect() == {'python': {'version': {'major': sys.version_info[0], 'minor': sys.version_info[1], 'micro': sys.version_info[2], 'releaselevel': sys.version_info[3], 'serial': sys.version_info[4]}, 'version_info': list(sys.version_info), 'executable': sys.executable, 'has_sslcontext': HAS_SSLCONTEXT, 'type': sys.implementation.name}}

test_PythonFactCollector_collect()

# Generated at 2022-06-13 03:14:32.962043
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = PythonFactCollector().collect()
    assert 'python' == python_facts.keys()[0]
    assert 'version' == python_facts['python'].keys()[0]
    assert 'version_info' == python_facts['python'].keys()[1]
    assert 'executable' == python_facts['python'].keys()[2]
    assert 'has_sslcontext' == python_facts['python'].keys()[3]
    assert 'type' == python_facts['python'].keys()[4]

# Generated at 2022-06-13 03:14:42.688096
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    import platform

    pc = PythonFactCollector()
    collected_python_facts = pc.collect()

    assert collected_python_facts['python']['version']['major'] == sys.version_info[0]
    assert collected_python_facts['python']['version']['minor'] == sys.version_info[1]
    assert collected_python_facts['python']['version']['micro'] == sys.version_info[2]
    assert collected_python_facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert collected_python_facts['python']['version']['serial'] == sys.version_info[4]


# Generated at 2022-06-13 03:14:45.908523
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector(None, None)
    # pfc.collect()

# Generated at 2022-06-13 03:14:55.571558
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    import ansible_test
    from ansible.module_utils.facts import collector

    # Create instance
    pfc = PythonFactCollector()

    # Validate that an empty dictionary is returned
    collected_facts = {}
    test_dict = pfc.collect(module=ansible_test, collected_facts=collected_facts)

# Generated at 2022-06-13 03:14:56.564806
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    py_fc = PythonFactCollector()
    py_fc.collect()

# Generated at 2022-06-13 03:15:06.962143
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Test for Python 3.4.0, 3.4.1, 3.4.2, 3.4.3, 3.4.4
    for major, minor, micro, releaselevel, serial in [(3, 4, 0, 'final', 0),
                                                      (3, 4, 1, 'final', 0),
                                                      (3, 4, 2, 'final', 0),
                                                      (3, 4, 3, 'final', 0),
                                                      (3, 4, 4, 'final', 0)]:
        pfc = PythonFactCollector()
        python_facts = pfc.collect()
        assert python_facts['python']['version']['major'] == major
        assert python_facts['python']['version']['minor'] == minor

# Generated at 2022-06-13 03:15:08.331661
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pc = PythonFactCollector()
    assert isinstance(pc.collect(), dict)

# Generated at 2022-06-13 03:15:10.026810
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    obj = PythonFactCollector()
    ansible_facts = obj.collect()
    assert 'python' in ansible_facts

# Generated at 2022-06-13 03:15:16.303420
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact = PythonFactCollector()
    facts = python_fact.collect()
    assert facts['python']['version']['major'] == sys.version_info[0]
    assert facts['python']['version']['minor'] == sys.version_info[1]
    assert facts['python']['version']['micro'] == sys.version_info[2]
    assert facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert facts['python']['version']['serial'] == sys.version_info[4]
    assert facts['python']['version_info'] == list(sys.version_info)

# Generated at 2022-06-13 03:15:40.359429
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    my_python_fact_collector = PythonFactCollector()
    my_python_fact_collector.collect()


# Generated at 2022-06-13 03:15:43.041864
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact_collector = PythonFactCollector()
    result_facts = python_fact_collector.collect()
    assert  result_facts['python']['type'] == 'CPython'

# Generated at 2022-06-13 03:15:45.346642
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pyfc = PythonFactCollector()
    pyfacts = pyfc.collect()
    assert pyfacts.values()[0]['type']
    assert pyfacts.values()[0]['version']
    assert pyfacts.values()[0]['version_info']
    assert pyfacts.values()[0]['executable']
    assert pyfacts.values()[0]['has_sslcontext']


# Generated at 2022-06-13 03:15:46.303602
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    m = PythonFactCollector()
    facts = m.collect()
    assert facts['python']['type'] == 'CPython'

# Generated at 2022-06-13 03:15:50.242486
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact_collector = PythonFactCollector()
    python_facts = python_fact_collector.collect()

    assert isinstance(python_facts, dict) == True
    assert python_facts['python']['has_sslcontext'] == HAS_SSLCONTEXT
    assert python_facts['python']['executable'] == sys.executable
    assert python_facts['python']['version_info'] == list(sys.version_info)

    try:
        python_facts['python']['type'] = sys.subversion[0]
    except AttributeError:
        try:
            python_facts['python']['type'] = sys.implementation.name
        except AttributeError:
            python_facts['python']['type'] = None


# Generated at 2022-06-13 03:15:58.367246
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    module = FakeModule()
    collected_facts = dict()
    collector = PythonFactCollector(module=module)
    result = collector.collect(module, collected_facts)

    assert 'python' in result
    assert result['python']['version']['major'] == sys.version_info[0]
    assert result['python']['version']['minor'] == sys.version_info[1]
    assert result['python']['version']['micro'] == sys.version_info[2]
    assert result['python']['version']['releaselevel'] == sys.version_info[3]
    assert result['python']['version']['serial'] == sys.version_info[4]
    assert result['python']['version_info'] == list(sys.version_info)

# Generated at 2022-06-13 03:16:07.963875
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """Test PythonFactCollector.collect."""
    # Test if python_facts returns the expected python informations.
    python_facts_collector = PythonFactCollector()
    python_facts = python_facts_collector.collect()

    assert python_facts['python']['version']['major'] == sys.version_info[0]
    assert python_facts['python']['version']['minor'] == sys.version_info[1]
    assert python_facts['python']['version']['micro'] == sys.version_info[2]
    assert python_facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert python_facts['python']['version']['serial'] == sys.version_info[4]

# Generated at 2022-06-13 03:16:10.281623
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_collector = PythonFactCollector()
    assert python_collector.collect() is not None

# Generated at 2022-06-13 03:16:20.476897
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    import sys
    collected_facts = {}
    
    pfc = PythonFactCollector()
    result = pfc.collect(collected_facts=collected_facts)
    assert result['python']['version']['major'] == sys.version_info[0]
    assert result['python']['version']['minor'] == sys.version_info[1]
    assert result['python']['version']['micro'] == sys.version_info[2]
    assert result['python']['version']['releaselevel'] == sys.version_info[3]
    assert result['python']['version']['serial'] == sys.version_info[4]
    assert result['python']['version_info'] == list(sys.version_info)
    assert result['python']['executable'] == sys

# Generated at 2022-06-13 03:16:23.198618
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact_collector = PythonFactCollector()
    python_facts = python_fact_collector.collect()

    assert python_facts['python']['type'] is not None
    assert python_facts['python']['type'] == 'python'

# Generated at 2022-06-13 03:16:59.446657
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    py = PythonFactCollector()
    facts = py.collect()
    assert set(facts['python']['version'].keys()) == set(['major', 'minor', 'micro', 'releaselevel', 'serial'])
    assert len(facts['python']['version_info']) == 5
    assert facts['python']['has_sslcontext'] == HAS_SSLCONTEXT
    assert facts['python']['executable'] == sys.executable
    assert facts['python']['type'] == 'CPython'

# Generated at 2022-06-13 03:17:09.109493
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # arrange
    test_collector = PythonFactCollector()

    # act
    test_result = test_collector.collect()

    # assert
    assert test_result['python']['version']['major'] == sys.version_info[0]
    assert test_result['python']['version']['minor'] == sys.version_info[1]
    assert test_result['python']['version']['micro'] == sys.version_info[2]
    assert test_result['python']['version']['releaselevel'] == sys.version_info[3]
    assert test_result['python']['version']['serial'] == sys.version_info[4]
    assert test_result['python']['version_info'] == list(sys.version_info)

# Generated at 2022-06-13 03:17:17.587766
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # NOTE: We are not testing 'python.type' here, since we want to test whatever
    # 'python_type' fact is available at the moment, not check for a specific value.
    # We are also not testing the exact value of 'python.executable' in order to not
    # bring any OS-specific files into the unit test.
    collector = PythonFactCollector()
    result = collector.collect()

# Generated at 2022-06-13 03:17:23.944991
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    expected = {
        'python': {
            'version': {
                'major': 3,
                'minor': 6,
                'micro': 2,
                'releaselevel': 'final',
                'serial': 0
            },
            'version_info': [3, 6, 2, 'final', 0],
            'executable': '/usr/bin/python',
            'type': 'CPython',
            'has_sslcontext': True,
        }
    }
    collector = PythonFactCollector()
    result = collector.collect()
    assert result == expected

# Generated at 2022-06-13 03:17:33.038437
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact = PythonFactCollector()
    ret = fact.collect()
    assert 'python' in ret
    assert 'version' in ret['python']
    assert 'version_info' in ret['python']
    assert 'executable' in ret['python']

    ret_version = ret['python']['version']
    ret_version_info = ret['python']['version_info']
    ret_executable = ret['python']['executable']
    assert 'major' in ret_version
    assert 'minor' in ret_version
    assert 'micro' in ret_version
    assert 'releaselevel' in ret_version
    assert 'serial' in ret_version
    assert 'type' in ret['python']
    assert 'has_sslcontext' in ret['python']

    # Make sure int is returned for major and minor
   

# Generated at 2022-06-13 03:17:34.097337
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    obj = PythonFactCollector()
    assert isinstance(obj.collect(), dict)

# Generated at 2022-06-13 03:17:40.354393
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """PythonFactCollector - collect()
    """
    pyfc = PythonFactCollector()
    pyfacts = pyfc.collect()
    assert pyfacts['python']['version']['major'] == 3
    assert pyfacts['python']['version']['minor'] == 5
    assert pyfacts['python']['version']['micro'] == 1
    assert pyfacts['python']['version']['releaselevel'] == 'final'
    assert pyfacts['python']['version']['serial'] == 0
    assert pyfacts['python']['version_info'] == list(sys.version_info)
    assert pyfacts['python']['executable'] == sys.executable
    assert pyfacts['python']['has_sslcontext'] == HAS_SSLCONTEXT

# vim: expandtab filetype=

# Generated at 2022-06-13 03:17:46.014115
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = PythonFactCollector().collect()
    assert 'python' in python_facts
    assert 'version' in python_facts['python']
    assert 'version_info' in python_facts['python']
    assert 'executable' in python_facts['python']
    assert 'type' in python_facts['python']
    assert 'has_sslcontext' in python_facts['python']

# Generated at 2022-06-13 03:17:52.273116
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """
    Returns dictonary with following keys:
    * python.version.major
    * python.version.minor
    * python.version.micro
    * python.version.releaselevel
    * python.version.serial
    * python.version_info
    * python.executable
    * python.has_sslcontext
    """
    c = PythonFactCollector()
    r = c.collect()
    assert 'python' in r
    assert 'version' in r['python']
    assert isinstance(r['python']['version']['major'], int)
    assert isinstance(r['python']['version']['minor'], int)
    assert isinstance(r['python']['version']['micro'], int)

# Generated at 2022-06-13 03:18:01.247755
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """
    Return the Python information of ansible remote host.
    """
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


# Generated at 2022-06-13 03:19:08.666944
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    module = {}
    collected_facts = {}
    fact_collector = PythonFactCollector()
    facts = fact_collector.collect(module=module, collected_facts=collected_facts)
    assert facts['python']['version']['major'] == 3
    assert facts['python']['version']['releaselevel'] == 'final'
    assert facts['python']['version_info'] == [3, 5, 0, 'final', 0]
    assert facts['python']['executable'] == sys.executable
    assert facts['python']['has_sslcontext'] == HAS_SSLCONTEXT
    assert facts['python']['type'] == 'CPython'


# Generated at 2022-06-13 03:19:13.987126
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Create a PythonFactCollector object
    py_collector = PythonFactCollector()
    # Call the collect method
    py_collector.collect()
    collected_facts = py_collector.collect()
    # Check that the version_info key is correctly filled
    assert collected_facts['python']['version_info'] == list(sys.version_info)
    # Check that the executable key is correctly filled
    assert collected_facts['python']['executable'] == sys.executable
    # Check that the has_sslcontext key is correctly filled
    assert collected_facts['python']['has_sslcontext'] == HAS_SSLCONTEXT
    # Check that the type key is correctly filled

# Generated at 2022-06-13 03:19:17.790455
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Check with an empty argument
    result = PythonFactCollector().collect()
    assert result['python']['version']['major'] == sys.version_info[0]

# Generated at 2022-06-13 03:19:28.029523
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    collector = PythonFactCollector()
    results = collector.collect()
    assert type(results) == dict, 'results is not a dictionary'
    assert len(results) == 1, 'results has more than one key'
    assert 'python' in results, 'python key missing from results'
    assert type(results['python']) == dict, 'python key is not a dictionary'
    assert 'version' in results['python'], 'version key missing from results'
    assert type(results['python']['version']) == dict, 'version key is not a dictionary'
    assert len(results['python']['version']) == 5
    assert 'major' in results['python']['version']
    assert type(results['python']['version']['major']) == int
    assert 'minor' in results['python']['version']

# Generated at 2022-06-13 03:19:38.669082
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Singleton instance of PythonFactCollector
    fact_collector = PythonFactCollector(None)

    # Make sure collect does not return an empty dictionary
    assert fact_collector.collect() != {}

    # Make sure collect returns a dictionary (and not a list or None)
    assert isinstance(fact_collector.collect(), dict)

    # Make sure that the returned dictionary, by the collect method, only
    # contains the "python" key
    assert fact_collector.collect().keys() == ['python']

    # Make sure that the "python" key is a dictionary
    assert isinstance(fact_collector.collect()['python'], dict)

    # Make sure that the "python" key contains a "version", "version_info",
    # "executable" and "has_sslcontext" keys

# Generated at 2022-06-13 03:19:40.983151
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    collect_result = PythonFactCollector().collect()
    assert 'python' in collect_result
    assert 'version_info' in collect_result['python']

# Generated at 2022-06-13 03:19:50.532467
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Create a PythonFactCollector with the just-created module
    python_collector = PythonFactCollector(module=None, collected_facts={})
    assert isinstance(python_collector, BaseFactCollector)
    # Collect facts
    python_facts = python_collector.collect()
    # Assert that there is a 'python' key in the collected facts
    assert 'python' in python_facts
    # Assert that the 'python' key is a dictionary
    assert isinstance(python_facts['python'], dict)
    # Assert that the 'python' key is not empty
    assert python_facts['python'] != {}
    # Assert that the 'version' key is in the 'python' dictionary
    assert 'version' in python_facts['python']
    # Assert that the 'version' key is a dictionary

# Generated at 2022-06-13 03:19:59.055539
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # set up arguments used by the ansible module
    args = {
        'gather_subset': '!all',
        'gather_timeout': 10,
        'filter': '*'
    }

    # collect the facts
    pfc = PythonFactCollector()
    facts = pfc.collect(args)
    python_facts = facts.get('python')

    # test if the method collect returns a dict
    assert isinstance(facts, dict)

    # test if the dict contains a dict for the module 'python'
    assert python_facts is not None

    # test if the dict contains the major version info
    assert python_facts['version']['major'] > 0

    # test if the dict contains the minor version info
    assert python_facts['version']['minor'] >= 0

    # test if the dict contains the

# Generated at 2022-06-13 03:20:07.020361
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

# Generated at 2022-06-13 03:20:09.790404
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """
    Unit test method collect of class PythonFactCollector.

    """
    tst_PythonFactColl = PythonFactCollector()
    tst_PythonFactColl.collect()
