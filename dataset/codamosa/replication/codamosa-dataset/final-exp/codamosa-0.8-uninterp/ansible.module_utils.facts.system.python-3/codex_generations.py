

# Generated at 2022-06-13 03:12:17.232249
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact = PythonFactCollector()
    collector_list = python_fact.collect()
    assert collector_list['python'] != []


# Generated at 2022-06-13 03:12:21.202707
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    collector = PythonFactCollector()
    actual = collector.collect()
    expected_keys = [u'python']
    assert set(actual.keys()) == set(expected_keys)
    assert 'version' in actual['python']
    assert 'version_info' in actual['python']
    assert 'executable' in actual['python']
    assert 'type' in actual['python']
    assert 'has_sslcontext' in actual['python']

# Generated at 2022-06-13 03:12:23.209129
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    m = PythonFactCollector()

    # Verify that method returns a dictionary
    assert isinstance(m.collect(), dict)

# Generated at 2022-06-13 03:12:27.519296
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector()
    result = fact_collector.collect()
    assert isinstance(result, dict)
    assert 'python' in result
    assert 'version' in result['python']
    assert 'type' in result['python']
    assert 'has_sslcontext' in result['python']

# Generated at 2022-06-13 03:12:34.039790
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    def test_module_has_docstring(obj):
        if hasattr(obj, '__doc__') and obj.__doc__:
            return True
        return False

    collector = PythonFactCollector()
    facts = collector.collect()

    assert facts is not None
    assert facts['python'] is not None
    assert facts['python']['version'] is not None
    assert facts['python']['version_info'] is not None
    assert facts['python']['executable'] is not None
    assert facts['python']['type'] is not None
    assert facts['python']['has_sslcontext'] == HAS_SSLCONTEXT
    assert test_module_has_docstring(sys) == True

# Generated at 2022-06-13 03:12:41.147159
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    # Test variable assignment
    logical_test = 'logical_test'
    conditional_test = 'conditional_test'
    del conditional_test

    # Test if, elif and else statements
    if logical_test:
        if_test = 'this is the if logic'
    elif conditional_test:
        elif_test = 'this is the elif logic'
    else:
        else_test = 'this is the else logic'

    # Test for loop
    for i in range(1,3):
        for_test = 'this is the for loop logic'

    # Test while loop
    while i < 5:
        while_test = 'this is the while loop logic'

    # Test try and except statements

# Generated at 2022-06-13 03:12:48.122084
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = PythonFactCollector().collect()
    assert python_facts['python']['version']['major'] == 3
    assert python_facts['python']['version']['minor'] == 5
    assert python_facts['python']['version']['micro'] == 1
    assert python_facts['python']['version']['releaselevel'] == 'final'
    assert python_facts['python']['version']['serial'] == 0
    assert python_facts['python']['executable'] == sys.executable
    assert python_facts['python']['type'] == sys.implementation.name
    assert python_facts['python']['has_sslcontext']

# Generated at 2022-06-13 03:12:56.800450
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    import sys
    import copy

    pfc = PythonFactCollector()

    python_facts = pfc.collect()
    assert 'python' in python_facts.keys()

    fact = python_facts['python']
    assert 'version' in fact
    assert 'version_info' in fact
    assert 'executable' in fact
    assert 'has_sslcontext' in fact

    # Should be a shallow copy so the original should not be modified
    assert sys.version_info == python_facts['python']['version_info']
    original_version_info = copy.deepcopy(sys.version_info)
    assert original_version_info == sys.version_info

    # Should be a shallow copy so the original should not be modified

# Generated at 2022-06-13 03:12:58.292568
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Test collect method
    python_fact_collector = PythonFactCollector()
    ansible_facts = python_fact_collector.collect()
    assert 'python' in ansible_facts.keys()

# Generated at 2022-06-13 03:13:02.622844
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    py_facts = PythonFactCollector().collect()

    # Validate that we get the expected number of facts back
    # This may need to change if we add more facts to this collector
    assert len(py_facts) == 1

    # Make sure that we have some version facts
    assert 'version' in py_facts['python']

    # Make sure that the version facts are what we expect
    assert py_facts['python']['version']['major'] == sys.version_info[0]
    assert py_facts['python']['version']['minor'] == sys.version_info[1]
    assert py_facts['python']['version']['micro'] == sys.version_info[2]
    assert py_facts['python']['version']['releaselevel'] == sys.version_info[3]

# Generated at 2022-06-13 03:13:06.962706
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    assert isinstance(PythonFactCollector().collect()['python']['version'], dict)

# Generated at 2022-06-13 03:13:16.301703
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector()
    python_facts = pfc.collect()

    assert isinstance(python_facts, dict)
    assert isinstance(python_facts['python'], dict)
    assert isinstance(python_facts['python']['version'], dict)
    assert isinstance(python_facts['python']['version_info'], list)
    assert isinstance(python_facts['python']['version']['major'], int)
    assert isinstance(python_facts['python']['version']['minor'], int)
    assert isinstance(python_facts['python']['version']['micro'], int)
    assert isinstance(python_facts['python']['version']['releaselevel'], str)
    assert python_facts['python']['version']['releaselevel']

# Generated at 2022-06-13 03:13:26.679013
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = PythonFactCollector().collect()
    assert len(python_facts) == 1, 'Only 1 item expected in output'
    assert 'python' in python_facts.keys(), 'Key `python` expected in output'
    assert isinstance(python_facts['python']['version'], dict), '`version` is not a dict'
    assert isinstance(python_facts['python']['version_info'], list), '`version_info` is not a list'
    assert isinstance(python_facts['python']['executable'], str), '`executable` is not a str'
    assert isinstance(python_facts['python']['has_sslcontext'], bool), '`has_sslcontext` is not a bool'

# Generated at 2022-06-13 03:13:36.326675
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    # Create an instance of the PythonFactCollector class
    python_collector = PythonFactCollector()

    # Get the python fact using the collect method of PythonFactCollector class
    python_facts = python_collector.collect()

    assert python_facts['python']['version']['major'] == sys.version_info[0]
    assert python_facts['python']['version']['minor'] == sys.version_info[1]
    assert python_facts['python']['version']['micro'] == sys.version_info[2]
    assert python_facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert python_facts['python']['version']['serial'] == sys.version_info[4]

# Generated at 2022-06-13 03:13:47.864214
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_collector = PythonFactCollector()
    result = python_collector.collect()
    assert result



# Generated at 2022-06-13 03:13:58.150113
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = {}
    python_fact = PythonFactCollector()
    python_facts = python_fact.collect()

    # Test that python facts were collected
    assert python_facts['python']

    # Test that version_info included in python facts
    assert python_facts['python']['version_info']

    # Test that current major version of python is included
    assert python_facts['python']['version']['major']

    # Test that current minor version of python is included
    assert python_facts['python']['version']['minor']

    # Test that current micro version of python is included
    assert python_facts['python']['version']['micro']

    # Test that the release level of python is included
    assert python_facts['python']['version']['releaselevel']

    # Test that the serial

# Generated at 2022-06-13 03:14:05.131884
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = PythonFactCollector(None).collect()

    assert 'python' in python_facts
    assert 'version' in python_facts['python']
    assert 'has_sslcontext' in python_facts['python']
    assert 'executable' in python_facts['python']
    assert 'version_info' in python_facts['python']
    assert 'type' in python_facts['python']
    assert 'major' in python_facts['python']['version']
    assert 'minor' in python_facts['python']['version']
    assert 'micro' in python_facts['python']['version']
    assert 'releaselevel' in python_facts['python']['version']
    assert 'serial' in python_facts['python']['version']

# Generated at 2022-06-13 03:14:10.746211
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Arrange
    from ansible.module_utils.facts import Facts
    python_fact_collector = PythonFactCollector()
    facts = Facts()

    # Act
    python_fact_collector.collect(facts=facts)

    # Assert
    assert 'python' in facts.ansible_facts
    assert 'version' in facts.ansible_facts['python']
    assert 'version_info' in facts.ansible_facts['python']
    assert 'executable' in facts.ansible_facts['python']
    assert 'has_sslcontext' in facts.ansible_facts['python']

# Generated at 2022-06-13 03:14:20.966766
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

# Generated at 2022-06-13 03:14:30.465032
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    expected = {'python': {'version': {'major': sys.version_info[0], 'minor': sys.version_info[1], 'micro': sys.version_info[2], 'releaselevel': sys.version_info[3], 'serial': sys.version_info[4]}, 'version_info': list(sys.version_info), 'executable': sys.executable, 'has_sslcontext': HAS_SSLCONTEXT}}

    try:
        expected['python']['type'] = sys.subversion[0]
    except AttributeError:
        try:
            expected['python']['type'] = sys.implementation.name
        except AttributeError:
            expected['python']['type'] = None

    result = PythonFactCollector().collect()

    assert result == expected

# Generated at 2022-06-13 03:14:37.252276
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector()
    result = pfc.collect(collected_facts={})

    assert result['python']['type'] == 'CPython'
    assert result['python']['version']['major'] == 3

# Generated at 2022-06-13 03:14:39.399655
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact_collector = PythonFactCollector()
    assert python_fact_collector.collect()

# Generated at 2022-06-13 03:14:41.256949
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector()
    assert pfc.collect()

# Generated at 2022-06-13 03:14:46.060192
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector()
    fact_collector.collect(module=None, collected_facts={})
    assert fact_collector.collect(module=None, collected_facts={})['python']['version']['major'] == sys.version_info[0]

# Generated at 2022-06-13 03:14:55.688221
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    mod = ModuleStub()
    mod.params = {}
    collector = PythonFactCollector(module=mod)
    facts = collector.collect()

    assert facts['python']['type'] == 'CPython'
    assert facts['python']['version']['major'] == sys.version_info[0]
    assert facts['python']['version']['minor'] == sys.version_info[1]
    assert facts['python']['version']['micro'] == sys.version_info[2]
    assert facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert facts['python']['version']['serial'] == sys.version_info[4]
    assert facts['python']['version_info'] == list(sys.version_info)
    assert facts

# Generated at 2022-06-13 03:14:59.913305
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    collected_facts = dict()
    pfc = PythonFactCollector()
    facts = pfc.collect(collected_facts=collected_facts)
    assert facts["python"]["version"]["major"] == sys.version_info[0]
    assert facts["python"]["type"] == sys.implementation.name

# Generated at 2022-06-13 03:15:07.488788
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    collector = PythonFactCollector()
    facts = collector.collect()
    assert facts['python'] == {
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


# Generated at 2022-06-13 03:15:14.989996
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    assert sys.version_info[:5] == (2, 7, 13, 'final', 0)
    assert sys.executable == '/usr/bin/python'
    assert HAS_SSLCONTEXT is False

    collector = PythonFactCollector()
    assert collector.collect() == {
        'python': {
            'type': 'CPython',
            'version': {
                'major': 2,
                'minor': 7,
                'micro': 13,
                'releaselevel': 'final',
                'serial': 0
            },
            'version_info': [2, 7, 13, 'final', 0],
            'has_sslcontext': HAS_SSLCONTEXT,
            'executable': sys.executable
        }
    }

# Generated at 2022-06-13 03:15:24.693036
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = PythonFactCollector().collect()
    assert isinstance(python_facts, dict)
    assert isinstance(python_facts['python'], dict)
    assert isinstance(python_facts['python']['version'], dict)
    assert isinstance(python_facts['python']['version_info'], list)
    assert python_facts['python']['version']['major'] == sys.version_info[0]
    assert python_facts['python']['version']['minor'] == sys.version_info[1]
    assert python_facts['python']['version']['micro'] == sys.version_info[2]
    assert python_facts['python']['version']['releaselevel'] == sys.version_info[3]

# Generated at 2022-06-13 03:15:34.889112
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_collector = PythonFactCollector()
    python_facts = python_collector.collect()
    assert python_facts['python']['version']['major'] == sys.version_info[0]
    assert python_facts['python']['version']['minor'] == sys.version_info[1]
    assert python_facts['python']['version']['micro'] == sys.version_info[2]
    assert python_facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert python_facts['python']['version']['serial'] == sys.version_info[4]
    assert python_facts['python']['version_info'] == list(sys.version_info)
    assert python_facts['python']['executable'] == sys.executable

# Generated at 2022-06-13 03:15:49.703226
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector()

    # test with no data passed in
    result = pfc.collect()

    assert isinstance(result, dict)
    assert 'python' in result
    assert isinstance(result['python'], dict)
    assert 'version' in result['python']
    assert isinstance(result['python']['version'], dict)
    assert 'major' in result['python']['version']
    assert 'minor' in result['python']['version']
    assert 'micro' in result['python']['version']
    assert 'releaselevel' in result['python']['version']
    assert 'serial' in result['python']['version']
    assert 'version_info' in result['python']
    assert isinstance(result['python']['version_info'], list)

# Generated at 2022-06-13 03:15:53.176862
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    collector = PythonFactCollector()
    result = collector.collect()
    assert result
    assert 'python' in result
    assert result['python']['version']['major'] > 1

# Generated at 2022-06-13 03:16:03.449429
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    '''
    Unit test for method collect of class PythonFactCollector
    '''
    python_fact_collector = PythonFactCollector()
    python_facts = python_fact_collector.collect()
    python_facts_expected = {
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


# Generated at 2022-06-13 03:16:07.473645
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector()
    fact_collector.collection_max_depth = 2
    collected_facts = {}
    fact_collector.collect(collected_facts=collected_facts)
    assert collected_facts == fact_collector.collect()


# Generated at 2022-06-13 03:16:08.931476
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    assert PythonFactCollector().collect() is not None

# Generated at 2022-06-13 03:16:19.191482
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """ Test method collect of class PythonFactCollector
    """
    pfc = PythonFactCollector()
    py_facts = pfc.collect()
    assert py_facts['python']['version']['major'] == sys.version_info[0]
    assert py_facts['python']['version']['minor'] == sys.version_info[1]
    assert py_facts['python']['version']['micro'] == sys.version_info[2]
    assert py_facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert py_facts['python']['version']['serial'] == sys.version_info[4]
    assert py_facts['python']['version_info'] == list(sys.version_info)

# Generated at 2022-06-13 03:16:25.654499
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = {
        "python": {
            "executable": "/usr/local/bin/python",
            "has_sslcontext": True,
            "type": "CPython",
            "version": {
                "major": 2,
                "minor": 7,
                "micro": 12,
                "releaselevel": "final",
                "serial": 0
            },
            "version_info": [
                2,
                7,
                12,
                "final",
                0
            ]
        }
    }

    collector = PythonFactCollector()
    facts_dict = collector.collect()
    assert facts_dict == python_facts

# Generated at 2022-06-13 03:16:31.955589
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    module = object()
    collected_facts = {}
    # method collect must return python facts

# Generated at 2022-06-13 03:16:35.282667
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    py = PythonFactCollector()

    assert len(py.collect()) > 0
    assert py.collect()['python']['version_info'][0] == 2 or py.collect()['python']['version_info'][0] == 3
    assert py.collect()['python']['version_info'][1] >= 6

# Generated at 2022-06-13 03:16:40.985583
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact_collector = PythonFactCollector()
    assert python_fact_collector.collect() == {
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
            'type': sys.subversion[0],
            'has_sslcontext': HAS_SSLCONTEXT
        }
    }

# Generated at 2022-06-13 03:16:57.068675
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    c = PythonFactCollector()
    data = c.collect()
    assert 'python' in data

# Generated at 2022-06-13 03:16:58.357114
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pf = PythonFactCollector()
    assert 'python' in pf.collect()

# Generated at 2022-06-13 03:17:03.148141
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact_collector = PythonFactCollector()
    assert python_fact_collector.collect() == {
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
            'type': 'CPython'
        }
    }

# Generated at 2022-06-13 03:17:13.232128
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact = PythonFactCollector()
    assert isinstance(python_fact, BaseFactCollector)
    assert isinstance(python_fact, object)
    assert python_fact.collect() is not None
    assert python_fact.collect()['python']['version']['major'] == sys.version_info[0]
    assert python_fact.collect()['python']['version']['minor'] == sys.version_info[1]
    assert python_fact.collect()['python']['version']['micro'] == sys.version_info[2]
    assert python_fact.collect()['python']['version']['releaselevel'] == sys.version_info[3]
    assert python_fact.collect()['python']['version']['serial'] == sys.version_info[4]

# Generated at 2022-06-13 03:17:19.971443
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector()
    facts = pfc.collect()

    assert 'python' in facts
    assert 'version' in facts['python']
    assert 'major' in facts['python']['version']
    assert isinstance(facts['python']['version']['major'], int)
    assert 'minor' in facts['python']['version']
    assert isinstance(facts['python']['version']['minor'], int)
    assert 'micro' in facts['python']['version']
    assert isinstance(facts['python']['version']['micro'], int)
    assert 'releaselevel' in facts['python']['version']
    assert isinstance(facts['python']['version']['releaselevel'], str)

# Generated at 2022-06-13 03:17:26.368350
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = PythonFactCollector().collect()
    assert python_facts['python']['version']['major'] == 2 or python_facts['python']['version']['major'] == 3
    assert python_facts['python']['version']['minor'] >= 6
    assert python_facts['python']['version']['releaselevel'] in ['alpha', 'beta', 'candidate', 'final']
    assert isinstance(python_facts['python']['version_info'], list)
    assert python_facts['python']['type'] in ['CPython', 'IronPython', 'Jython', 'PyPy']
    assert python_facts['python']['has_sslcontext'] is True or python_facts['python']['has_sslcontext'] is False


# Generated at 2022-06-13 03:17:34.138792
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    m_collector = PythonFactCollector()
    m_collector.collect()
    res = m_collector.get_facts()
    assert res['python']['version_info'][0] == sys.version_info[0]
    assert res['python']['version_info'][1] == sys.version_info[1]
    assert res['python']['version_info'][2] == sys.version_info[2]
    assert res['python']['version_info'][3] == sys.version_info[3]
    assert res['python']['version_info'][4] == sys.version_info[4]
    assert res['python']['executable'] == sys.executable
    assert res['python']['has_sslcontext'] == HAS_SSLCONTEXT

# Generated at 2022-06-13 03:17:37.282651
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fake_module = type('module', (object,), {})()
    python_fc = PythonFactCollector(fake_module)

    # Make sure it has all the fact ids that we want
    fact_ids = set(python_fc.collect().keys())
    assert python_fc._fact_ids.issubset(fact_ids)

# Generated at 2022-06-13 03:17:41.719811
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    facts = PythonFactCollector().collect()
    assert facts == {
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
            'type': sys.version.split()[0]
        }
    }

# Generated at 2022-06-13 03:17:48.116664
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.system.python import PythonFactCollector
    pf = PythonFactCollector()
    result = pf.collect()
    assert result['python']['type'] == 'cpython'

if __name__ == '__main__':
    test_PythonFactCollector_collect()

# Generated at 2022-06-13 03:18:21.234032
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pgfc = PythonFactCollector()
    facts = pgfc.collect()
    assert 'python' in facts, "Missing 'python' key in collected facts"



# Generated at 2022-06-13 03:18:21.926952
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector()
    fact_collector.collect()

# Generated at 2022-06-13 03:18:22.967239
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    _x = PythonFactCollector()
    assert (_x.collect() is not None)

# Generated at 2022-06-13 03:18:30.948534
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact_collector = PythonFactCollector()
    facts = python_fact_collector.collect()
    assert facts['python'] == { 'version': { 'major': sys.version_info[0],
            'minor': sys.version_info[1], 'micro': sys.version_info[2],
            'releaselevel': sys.version_info[3], 'serial': sys.version_info[4]},
            'version_info': list(sys.version_info), 
            'executable': sys.executable, 'has_sslcontext': HAS_SSLCONTEXT }
    assert 'version' in facts['python']
    assert 'version_info' in facts['python']
    assert 'executable' in facts['python']
    assert 'has_sslcontext' in facts['python']
    assert 'type' in facts

# Generated at 2022-06-13 03:18:39.679898
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    from ansible.module_utils.facts import get_collector_instance

    # Only apply the test if we have SSLContext support
    if HAS_SSLCONTEXT:
        python = get_collector_instance(PythonFactCollector).collect()
        assert python['python']['version']['major'] == sys.version_info[0]
        assert python['python']['version']['minor'] == sys.version_info[1]
        assert python['python']['version']['micro'] == sys.version_info[2]
        assert python['python']['version']['releaselevel'] == sys.version_info[3]
        assert python['python']['version']['serial'] == sys.version_info[4]

# Generated at 2022-06-13 03:18:47.228413
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """
    This test case verifies that PythonFactCollector.collect method does
    not return wrong python dict
    """
    # pylint: disable=W0212
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
        'has_sslcontext': HAS_SSLCONTEXT,
        'type': sys.implementation.name
    }



# Generated at 2022-06-13 03:18:56.948176
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector()
    result = fact_collector.collect()
    expected = {
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
    if sys.version_info[0] == 2:
        expected['python']['type'] = sys.subversion[0]

# Generated at 2022-06-13 03:19:06.556910
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    result = PythonFactCollector().collect(None, None)

    assert result['python']['version']['major'] == sys.version_info[0]
    assert result['python']['version']['minor'] == sys.version_info[1]
    assert result['python']['version']['micro'] == sys.version_info[2]
    assert result['python']['version']['releaselevel'] == sys.version_info[3]
    assert result['python']['version']['serial'] == sys.version_info[4]
    assert result['python']['version_info'] == list(sys.version_info)
    assert result['python']['executable'] == sys.executable
    assert result['python']['has_sslcontext'] == HAS_SSLCONTEXT

# Generated at 2022-06-13 03:19:12.009693
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact_collector = PythonFactCollector()
    facts = python_fact_collector.collect()
    assert isinstance(facts, dict)
    assert isinstance(facts['python'], dict)
    python_fact = facts['python']
    assert isinstance(python_fact['version'], dict)
    assert isinstance(python_fact['version_info'], list)
    assert isinstance(python_fact['executable'], str)
    assert isinstance(python_fact['has_sslcontext'], bool)
    if python_fact['type'] is None:
        assert python_fact['type'] is None
    else:
        assert isinstance(python_fact['type'], str)

# Generated at 2022-06-13 03:19:13.506213
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pythonfactcollector_object = PythonFactCollector()
    assert isinstance(pythonfactcollector_object, PythonFactCollector)
    pythonfactcollector_object.collect()

# Generated at 2022-06-13 03:20:23.201657
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    collector = PythonFactCollector()
    facts = collector.collect()

    assert 'python' in facts
    assert facts['python']['version']['major'] == sys.version_info[0]
    assert facts['python']['version']['minor'] == sys.version_info[1]
    assert facts['python']['version']['micro'] == sys.version_info[2]
    assert facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert facts['python']['version']['serial'] == sys.version_info[4]
    assert facts['python']['version_info'] == list(sys.version_info)
    assert facts['python']['executable'] == sys.executable
    assert facts['python']['has_sslcontext']

# Generated at 2022-06-13 03:20:29.685121
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector()
    python_facts = pfc.collect(None, None)
    assert python_facts['python']['version']['major'] == sys.version_info[0]
    assert python_facts['python']['version']['minor'] == sys.version_info[1]
    assert python_facts['python']['version']['micro'] == sys.version_info[2]
    assert python_facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert python_facts['python']['version']['serial'] == sys.version_info[4]
    assert python_facts['python']['version_info'] == list(sys.version_info)
    assert python_facts['python']['executable'] == sys.executable

# Generated at 2022-06-13 03:20:34.997206
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    '''Unit test for method collect of class PythonFactCollector'''
    python_facts = PythonFactCollector().collect()
    assert 'python' in python_facts
    assert 'version' in python_facts['python']
    assert 'version_info' in python_facts['python']
    assert 'executable' in python_facts['python']
    assert 'has_sslcontext' in python_facts['python']


# Generated at 2022-06-13 03:20:41.924030
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    py_fact_collector = PythonFactCollector()

    result = py_fact_collector.collect()
    expected_result = {
        'python': {
            'executable': '/usr/bin/python2.7',
            'version_info': [2, 7, 6, 'final', 0],
            'type': 'CPython',
            'version': {
                'releaselevel': 'final',
                'serial': 0,
                'major': 2,
                'micro': 6,
                'minor': 7
            },
            'has_sslcontext': False
        }
    }
    assert result == expected_result

# Generated at 2022-06-13 03:20:48.680838
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector()
    ansible_facts = fact_collector.collect()
    assert isinstance(ansible_facts['python'], dict)
    assert isinstance(ansible_facts['python']['version'], dict)
    assert isinstance(ansible_facts['python']['version']['major'], int)
    assert isinstance(ansible_facts['python']['version']['minor'], int)
    assert isinstance(ansible_facts['python']['version']['micro'], int)
    assert isinstance(ansible_facts['python']['version']['releaselevel'], str)
    assert isinstance(ansible_facts['python']['version']['serial'], int)

# Generated at 2022-06-13 03:20:53.035947
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector(None)
    pfc._collect_platform_subset = MockFactCollector._collect_platform_subset
    facts = pfc.collect()
    assert facts['python']['version']['major'] == 3
    assert 'has_sslcontext' in facts['python']


# Generated at 2022-06-13 03:21:00.839963
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

# Generated at 2022-06-13 03:21:06.498796
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    import sys

    class MockModule(object):
        def __init__(self):
            self.params = {}

    class MockCollectedFacts(object):
        def __init__(self):
            self.cache = {}

    module = MockModule()
    collected_facts = MockCollectedFacts()
    fact_collector = PythonFactCollector(module=module, collected_facts=collected_facts)

    python_facts = fact_collector.collect()
    try:
        python_type = sys.subversion[0]
    except AttributeError:
        try:
            python_type = sys.implementation.name
        except AttributeError:
            python_type = None


# Generated at 2022-06-13 03:21:13.892183
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    import pytest
    from ansible.module_utils.facts.collector import Collector

    # Test case when we are running on Ansible's testing framework
    def test_running_on_ansible():
        obj = PythonFactCollector()
        obj._collect_platform_facts = lambda **kwargs: {
            'platform': {
              'distribution': 'ansible',
              'distribution_version': 'testing'
            }
        }
        obj.collect()
        assert obj.facts['python']['type'] == 'testing'

    # Test that when we are running on CPython, version_info is
    # correctly returned
    def test_running_on_cpython():
        obj = PythonFactCollector()
        obj.collect()
        assert obj.facts['python']['type'] == 'cpython'
        assert obj

# Generated at 2022-06-13 03:21:17.766241
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fc = PythonFactCollector()
    # As of Python 2.7 and 3.2, there is no way to mock sys modules.
    # We will just check if calling collect() method will return python_facts
    # with keys 'python' and 'version'.
    python_facts = fc.collect()
    assert python_facts.has_key('python')
    assert python_facts.has_key('version')