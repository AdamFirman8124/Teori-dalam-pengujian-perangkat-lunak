

# Generated at 2022-06-13 03:12:18.102131
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    import sys
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
    factCollector = PythonFactCollector()
    assert factCollector.collect() == python_facts

# Generated at 2022-06-13 03:12:22.750898
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_collector = PythonFactCollector()
    facts = python_collector.collect()
    assert facts['python']['version']['major'] == sys.version_info[0]

# Generated at 2022-06-13 03:12:33.631915
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fc = PythonFactCollector()
    facts = fc.collect()
    assert 'python' in facts
    assert 'version' in facts['python']
    assert 'has_sslcontext' in facts['python']
    assert 'version_info' in facts['python']
    assert 'executable' in facts['python']
    assert 'type' in facts['python']



# Generated at 2022-06-13 03:12:41.058929
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Create a new instance of PythonFactCollector instance
    python_fact_collector = PythonFactCollector()

    # Check if collect method returns the expected dictionary
    assert python_fact_collector.collect() == {'python':{'executable':'/usr/bin/python',
                                                                             'has_sslcontext': True,
                                                                             'version':{'major':2,
                                                                                                 'minor':7,
                                                                                                 'micro':10,
                                                                                                 'releaselevel':'final',
                                                                                                 'serial':0},
                                                                             'version_info':[2,
                                                                                                     7,
                                                                                                     10,
                                                                                                     'final',
                                                                                                     0]}}

# Generated at 2022-06-13 03:12:48.907872
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    f = PythonFactCollector()
    my_facts = f.collect()

    assert my_facts == {
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

    if sys.version_info[0] >= 3:
        assert my_facts['python']['type'] == 'CPython'

# Generated at 2022-06-13 03:12:50.056303
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pass

# Generated at 2022-06-13 03:12:55.209567
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    assert sys.version_info[0] >= 2
    assert sys.version_info[1] >= 7
    assert sys.version_info[2] >= 0
    assert sys.version_info[3] in ('alpha', 'beta', 'candidate', 'final')
    assert sys.version_info[4] >= 0

    collector = PythonFactCollector()
    python_facts = collector.collect()

    # Basic python facts
    assert (python_facts['python']['version']['major'] == sys.version_info[0])
    assert (python_facts['python']['version']['minor'] == sys.version_info[1])
    assert (python_facts['python']['version']['micro'] == sys.version_info[2])

# Generated at 2022-06-13 03:12:58.056813
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact_collector = PythonFactCollector()
    assert 'python' in python_fact_collector.collect().keys()

# Generated at 2022-06-13 03:12:59.375534
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    foo = PythonFactCollector()

    res = foo.collect()
    assert res['python']['type'] is not None

# Generated at 2022-06-13 03:13:02.780629
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    c = PythonFactCollector()
    assert isinstance(c.collect(), dict)

# Generated at 2022-06-13 03:13:13.534599
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector()
    fact_collector.collect()
    assert fact_collector.collect() == {
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
            'type': sys.implementation.name
        }
    }

# Generated at 2022-06-13 03:13:20.816610
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    collector = PythonFactCollector()
    facts = collector.collect()
    assert facts == {'python': {
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
        'type': sys.subversion[0]
    }}


# Generated at 2022-06-13 03:13:24.194556
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    p = PythonFactCollector()
    python_facts = p.collect()

    assert 'python' in python_facts
    assert 'version' in python_facts['python']
    assert 'version_info' in python_facts['python']
    assert 'executable' in python_facts['python']
    assert 'type' in python_facts['python']
    assert 'has_sslcontext' in python_facts['python']


# Generated at 2022-06-13 03:13:33.849130
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    # Create a PythonFactCollector instance
    fact_collector_obj = PythonFactCollector()

    # Call method collect
    collected_facts = fact_collector_obj.collect()
    assert 'python' in collected_facts

    # Get the expected facts
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
            'has_sslcontext': HAS_SSLCONTEXT
        }
    }


# Generated at 2022-06-13 03:13:37.661993
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Get an instance of the class to be tested
    fc = PythonFactCollector()
    # Call the method and store the result in a variable
    facts = fc.collect()
    # Check that the result is not empty/None
    assert facts

# Generated at 2022-06-13 03:13:45.952391
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    module = None
    fact_collector = PythonFactCollector(module)
    facts = fact_collector.collect()
    assert facts['python']['version']['major'] == sys.version_info[0]
    assert facts['python']['version']['minor'] == sys.version_info[1]
    assert facts['python']['version']['micro'] == sys.version_info[2]
    assert facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert facts['python']['version']['serial'] == sys.version_info[4]
    assert facts['python']['version_info'] == list(sys.version_info)
    assert facts['python']['executable'] == sys.executable

# Generated at 2022-06-13 03:13:57.710433
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Arrange
    fact_collector = PythonFactCollector(None)

    # Act
    python_facts = fact_collector.collect()

    # Assert
    assert isinstance(python_facts, dict)
    assert 'python' in python_facts
    assert isinstance(python_facts['python'], dict)
    assert 'version' in python_facts['python']
    assert isinstance(python_facts['python']['version'], dict)
    assert 'major' in python_facts['python']['version']
    assert isinstance(python_facts['python']['version']['major'], int)
    assert 'minor' in python_facts['python']['version']
    assert isinstance(python_facts['python']['version']['minor'], int)
    assert 'micro' in python

# Generated at 2022-06-13 03:14:04.020403
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector(None, None)
    python_facts = pfc.collect()
    assert python_facts['python']['version_info'] == list(sys.version_info)
    assert python_facts['python']['executable'] == sys.executable
    assert isinstance(python_facts['python']['has_sslcontext'], bool)

# Generated at 2022-06-13 03:14:11.079141
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector()
    facts = fact_collector.collect()

    assert 'python' in facts
    assert 'version' in facts['python']
    assert 'version_info' in facts['python']
    assert 'executable' in facts['python']
    assert 'has_sslcontext' in facts['python']
    assert facts['python']['has_sslcontext'] == HAS_SSLCONTEXT

    assert 'type' in facts['python']
    try:
        assert facts['python']['type'] == sys.subversion[0]
    except AttributeError:
        try:
            assert facts['python']['type'] == sys.implementation.name
        except AttributeError:
            assert facts['python']['type'] == None

# Generated at 2022-06-13 03:14:21.357671
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    from ansible_collections.notstdlib.moveitallout.tests.unit.modules.utils import set_module_args
    from ansible_collections.notstdlib.moveitallout.plugins.modules import setup


# Generated at 2022-06-13 03:14:33.094841
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Create a new instance of PythonFactCollector
    p = PythonFactCollector()

    # Unit test with correct output
    assert 'python' in p.collect(None, None)
    assert 'type' in  p.collect(None, None)['python']
    assert 'version' in  p.collect(None, None)['python']
    assert 'major' in  p.collect(None, None)['python']['version']
    assert 'minor' in  p.collect(None, None)['python']['version']
    assert 'micro' in  p.collect(None, None)['python']['version']
    assert 'releaselevel' in  p.collect(None, None)['python']['version']
    assert 'serial' in  p.collect(None, None)['python']['version']


# Generated at 2022-06-13 03:14:35.601279
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector()
    py_info = pfc._collect()

    assert len(py_info) == 1
    assert 'python' in py_info


# Generated at 2022-06-13 03:14:44.030622
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    p = PythonFactCollector()
    f = p.collect(None, None)
    assert f['python']['version']['major'] == sys.version_info[0]
    assert f['python']['version']['minor'] == sys.version_info[1]
    assert f['python']['version']['micro'] == sys.version_info[2]
    assert f['python']['version']['releaselevel'] == sys.version_info[3]
    assert f['python']['version']['serial'] == sys.version_info[4]
    assert f['python']['version_info'] == list(sys.version_info)
    assert f['python']['executable'] == sys.executable
    assert f['python']['has_sslcontext'] == HAS_SS

# Generated at 2022-06-13 03:14:54.705147
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector()
    collected_facts = fact_collector.collect()
    assert type(collected_facts['python']['version']) == dict
    assert type(collected_facts['python']['version']['major']) == int
    assert type(collected_facts['python']['version']['minor']) == int
    assert type(collected_facts['python']['version']['micro']) == int
    assert type(collected_facts['python']['version']['releaselevel']) == str
    assert type(collected_facts['python']['version']['serial']) == int
    assert type(collected_facts['python']['version_info']) == list
    assert type(collected_facts['python']['executable'])

# Generated at 2022-06-13 03:14:59.012580
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    collector = PythonFactCollector()
    actual = collector.collect()
    assert actual == {'python': {'version': {'major': 3, 'minor': 4, 'micro': 2, 'releaselevel': 'final', 'serial': 0},
                                 'version_info': [3, 4, 2, 'final', 0],
                                 'executable': '/usr/bin/python',
                                 'type': 'CPython',
                                 'has_sslcontext': True}}

# Generated at 2022-06-13 03:15:09.227941
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    '''Test method collect of class PythonFactCollector'''

    import sys
    import json
    import pytest

    # Get the version facts
    version = {
            'version': {
                'major': sys.version_info[0],
                'minor': sys.version_info[1],
                'micro': sys.version_info[2],
            },
            'version_info': list(sys.version_info),
            'executable': sys.executable,
            'has_sslcontext': HAS_SSLCONTEXT
    }

    # Add the rest of the fields
    try:
        version['type'] = sys.subversion[0]
    except AttributeError:
        try:
            version['type'] = sys.implementation.name
        except AttributeError:
            version['type'] = None

   

# Generated at 2022-06-13 03:15:16.582160
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    text = '''
python:
  has_sslcontext: True
  type: CPython
  version:
    major: 3
    minor: 6
    micro: 1
    releaselevel: final
    serial: 0
  version_info:
  - 3
  - 6
  - 1
  - 'final'
  - 0
'''
    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.six import PY2

    python_gather = get_collector_instance('python')
    result = python_gather.collect()

    if PY2:
        text = to_bytes(text)
    assert text == str(result)

# Generated at 2022-06-13 03:15:25.747275
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector()
    output = {'python': {
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
              }}

# Generated at 2022-06-13 03:15:35.446877
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    py_fact_collector = PythonFactCollector()
    # test with a normal python interpreter
    if sys.version_info[0] == 2:
        expected = {'python': {
            'version': {
                'major': 2,
                'minor': 7,
                'micro': 0,
                'releaselevel': 'final',
                'serial': 0
            },
            'version_info': [2, 7, 0, 'final', 0],
            'executable': '/usr/bin/python2.7',
            'has_sslcontext' : HAS_SSLCONTEXT
        }}

        # Test without subversion
        sys.subversion = None
        results = py_fact_collector.collect()
        assert results == expected

# Generated at 2022-06-13 03:15:39.353397
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    c = PythonFactCollector()
    assert c.collect() == {'python': {'version': {'major': 2, 'minor': 6, 'micro': 6, 'releaselevel': 'final', 'serial': 0}, 'version_info': [2, 6, 6, 'final', 0], 'executable': '/usr/bin/python', 'type': 'CPython', 'has_sslcontext': False}}, "fact() should return dict with version info"

# Generated at 2022-06-13 03:15:47.168134
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    # Initialize the class
    p = PythonFactCollector()

    # Call the method collect
    facts = p.collect()

    # Basic check
    assert 'python' in facts.keys()
    python = facts['python']
    assert 'version' in python.keys()
    version = python['version']
    assert 'major' in version.keys()
    assert 'minor' in version.keys()
    assert 'micro' in version.keys()
    assert 'releaselevel' in version.keys()
    assert 'serial' in version.keys()
    assert 'version_info' in python.keys()
    assert 'executable' in python.keys()
    assert 'has_sslcontext' in python.keys()
    assert 'type' in python.keys()


# Generated at 2022-06-13 03:15:57.146457
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # instantiate PythonFactCollector
    pfc = PythonFactCollector()

    # call method collect of PythonFactCollector
    result = pfc.collect()

    # test that result is a dictionary
    assert isinstance(result, dict)

    # test that result has key 'python'
    assert result.has_key('python')

    # test that result['python'] is a dictionary
    assert isinstance(result['python'], dict)

    # test that result['python'] has key 'type'
    assert result['python'].has_key('type')

    # test that result['python']['type'] is a string
    assert isinstance(result['python']['type'], str)

    # test that result['python']['type'] is not empty
    assert len(result['python']['type']) > 0

# Generated at 2022-06-13 03:16:04.172958
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_module = PythonFactCollector()
    assert python_module.collect() == {
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

# Generated at 2022-06-13 03:16:11.193114
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    facts = PythonFactCollector().collect()
    assert 'python' in facts
    assert facts['python']['version']['major'] == sys.version_info[0]
    assert facts['python']['version']['minor'] == sys.version_info[1]
    assert facts['python']['version']['micro'] == sys.version_info[2]
    assert facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert facts['python']['version']['serial'] == sys.version_info[4]
    assert facts['python']['version_info'] == list(sys.version_info)
    assert facts['python']['executable'] == sys.executable
    assert facts['python']['has_sslcontext'] == HAS_SSLCON

# Generated at 2022-06-13 03:16:20.877948
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python = PythonFactCollector()
    facts = python.collect(module=None, collected_facts=None)
    key = 'python'
    assert key in facts, "key " + key + " not found in facts"
    assert 'version' in facts[key], "key 'version' not found in " + key
    version_key = 'version'
    assert version_key in facts[key], "key " + version_key + " not found in " + key
    for id in ['major', 'minor', 'micro', 'releaselevel', 'serial']:
        assert id in facts[key][version_key], "key " + id + " not found in " + key + '.' + version_key
    assert 'version_info' in facts[key], "key 'version_info' not found in " + key

# Generated at 2022-06-13 03:16:25.438940
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.collector.python import PythonFactCollector
    from ansible.module_utils.facts.facts import Facts

    collector = Collector(None)
    collected_facts = Facts(None)
    pythonFacts = PythonFactCollector(None)

    facts_list = pythonFacts.collect(None, collected_facts)
    assert facts_list.get('python')

# Generated at 2022-06-13 03:16:31.884153
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    from ansible.module_utils.facts.collector import FactsCollector
    from ansible.module_utils.facts.facts import Facts

    system_python_facts = PythonFactCollector().collect()
    print("Python Version: " + str(system_python_facts['python']['version']['major']) + "." + str(system_python_facts['python']['version']['minor']))
    print("Python has SSLContext: " + str(system_python_facts['python']['has_sslcontext']))

    # Testing get_all_facts of FactsCollector
    facts_collector = FactsCollector()
    all_facts = facts_collector.get_all_facts(module_spec={'python2'})
    assert all_facts is not None, "Failed to get all facts."

    print

# Generated at 2022-06-13 03:16:32.991176
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    obj = PythonFactCollector()
    assert obj.collect() is not None

# Generated at 2022-06-13 03:16:33.497750
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pass

# Generated at 2022-06-13 03:16:40.291372
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """
    Unit test function to check whether the method collect of class
    PythonFactCollector returns the expected result.
    """
    pfc = PythonFactCollector()
    result = pfc.collect()
    assert "python" in result
    assert result["python"]["version"]["major"] == sys.version_info[0]
    assert result["python"]["version"]["minor"] == sys.version_info[1]
    assert result["python"]["version"]["micro"] == sys.version_info[2]
    assert result["python"]["version"]["releaselevel"] == sys.version_info[3]
    assert result["python"]["version"]["serial"] == sys.version_info[4]

# Generated at 2022-06-13 03:16:52.345439
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    collector = PythonFactCollector()
    result = collector.collect()

    assert result['python']['version']['major'] == sys.version_info[0]
    assert result['python']['version']['minor'] == sys.version_info[1]
    assert result['python']['version']['micro'] == sys.version_info[2]
    assert result['python']['version']['releaselevel'] == sys.version_info[3]
    assert result['python']['version']['serial'] == sys.version_info[4]
    assert result['python']['version_info'] == list(sys.version_info)
    assert result['python']['executable'] == sys.executable
    assert result['python']['has_sslcontext'] == HAS_SSLCONTEXT


# Generated at 2022-06-13 03:17:01.532834
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """Test the collect() method of the PythonFactCollector"""
    # python_version_info has the following structure:
    #      (major, minor, micro, releaselevel, serial)
    python_version_info = sys.version_info
    # python_version_info_list has the following structure:
    #      [major, minor, micro, releaselevel, serial]
    python_version_info_list = [python_version_info[0],
                                python_version_info[1],
                                python_version_info[2],
                                python_version_info[3],
                                python_version_info[4]]
    # Collect the facts
    collector = PythonFactCollector()
    collect_results = collector.collect()
    # Check the results
    # Check the 'python' section
    python_section = collect_results

# Generated at 2022-06-13 03:17:12.177525
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # create an instance of the PythonFactCollector class
    wf_test = PythonFactCollector()
    # invoke the collect method
    results = wf_test.collect()
    # assert the results with expected dictionary
    assert results == {'python': {'version': {'major': sys.version_info[0],
                                              'minor': sys.version_info[1],
                                              'micro': sys.version_info[2],
                                              'releaselevel': sys.version_info[3],
                                              'serial': sys.version_info[4]},
                                  'version_info': list(sys.version_info),
                                  'executable': sys.executable,
                                  'has_sslcontext': HAS_SSLCONTEXT,
                                  'type': sys.implementation.name}}

# Generated at 2022-06-13 03:17:19.210901
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    module = AnsibleModule(
        argument_spec = dict(),
    )
    fact_collector = PythonFactCollector(module=module)
    result = fact_collector.collect()

    assert 'python' in result
    assert type(result['python']) is dict
    assert 'version' in result['python']
    assert type(result['python']['version']) is dict
    assert 'major' in result['python']['version']
    assert type(result['python']['version']['major']) is int
    assert 'minor' in result['python']['version']
    assert type(result['python']['version']['minor']) is int
    assert 'micro' in result['python']['version']
    assert type(result['python']['version']['micro']) is int

# Generated at 2022-06-13 03:17:24.977859
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    p = PythonFactCollector()
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
            'has_sslcontext': HAS_SSLCONTEXT,
            'type': sys.implementation.name
        }
    }
    assert p.collect() == expected_result

# Generated at 2022-06-13 03:17:28.868357
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pyfact = PythonFactCollector()
    pyfact_dict = pyfact.collect()
    assert pyfact_dict['python']['version']['major'] == sys.version_info[0]
    assert pyfact_dict['python']['has_sslcontext'] == HAS_SSLCONTEXT

# Generated at 2022-06-13 03:17:31.819582
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
  results = PythonFactCollector().collect()
  assert isinstance(results['python']['type'], str)
  assert isinstance(results['python']['executable'], str)
  assert isinstance(results['python']["has_sslcontext"], bool)

# Generated at 2022-06-13 03:17:36.044780
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector()
    results = pfc.collect()
    assert type(results) is dict
    assert 'python' in results.keys()
    p = results['python']
    assert type(p) is dict
    assert 'executable' in p.keys()
    assert 'has_sslcontext' in p.keys()
    assert 'type' in p.keys()
    assert 'version' in p.keys()
    assert 'version_info' in p.keys()

# Generated at 2022-06-13 03:17:41.661710
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    import mock
    from ansible.module_utils.facts import ansible_facts

    test_collector = PythonFactCollector()

    with mock.patch.object(test_collector, 'collect_platform_facts') as mockcollect_platform_facts:
        mockcollect_platform_facts.return_value = dict()
        facts = test_collector.collect()

# Generated at 2022-06-13 03:17:42.745885
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fc = PythonFactCollector()
    fc.collect()

# Generated at 2022-06-13 03:17:59.592297
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Create target object
    python_fact_collector = PythonFactCollector()
    # Try the collect method
    assert python_fact_collector.collect()

# Generated at 2022-06-13 03:18:03.109727
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """Unit test for method collect of class PythonFactCollector"""
    # create object
    p = PythonFactCollector()
    # get result
    result = p.collect()
    # assert
    assert result.get("python")
    assert 'version_info' in result.get("python")
    assert 'executable' in result.get("python")
    assert 'has_sslcontext' in result.get("python")

# Generated at 2022-06-13 03:18:11.383372
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    from ansible.module_utils.facts import collector
    # Create an instance of Class PythonFactCollector
    python_fc = collector.get_collector('python')
    # Get the facts
    facts = python_fc.collect()
    # Assert the type of facts is a dictionary
    assert isinstance(facts, dict)
    # Asserting keys of the facts
    expected_keys = (u'python')
    assert set(facts.keys()) == set(expected_keys)
    # Asserting some the facts
    facts_python = facts[u'python']
    assert isinstance(facts_python, dict)
    assert isinstance(facts_python['version'], dict)
    assert isinstance(facts_python['version_info'], list)
    assert isinstance(facts_python['executable'], str)

# Generated at 2022-06-13 03:18:16.053963
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pyfc = PythonFactCollector()
    py_facts = pyfc.collect()

    assert py_facts is not None
    assert 'python' in py_facts.keys()
    my_py_fact = py_facts['python']

    # Test python version information
    if (sys.version_info[0] < 3):
        assert 'version' in my_py_fact.keys()
        my_ver_fact = my_py_fact['version']

        assert 'major' in my_ver_fact.keys()
        assert 'minor' in my_ver_fact.keys()
        assert 'micro' in my_ver_fact.keys()
        assert 'releaselevel' in my_ver_fact.keys()
        assert 'serial' in my_ver_fact.keys()

# Generated at 2022-06-13 03:18:24.959770
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Test that the collect method returns the expected data when
    # supplied with collected_facts = None.
    python_facts = PythonFactCollector().collect()
    assert python_facts == {
        'python': {
            'executable': sys.executable,
            'has_sslcontext': HAS_SSLCONTEXT,
            'type': 'CPython',
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

# Generated at 2022-06-13 03:18:29.104117
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils.facts.collector import FactCollector
    collector = FactCollector()
    collector.collect(fail_on_error=False)
    python_facts = ansible_facts['ansible_python']
    assert not python_facts is None

# Generated at 2022-06-13 03:18:37.918645
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector()
    fact_collector.collect()
    python_facts = fact_collector.collect()

    # Asserting python_facts is a dict
    assert isinstance(python_facts, dict)
    # Asserting python_facts has 'python' as a key
    assert ('python' in python_facts)
    # Asserting python_facts['python'] is a dict
    assert isinstance(python_facts['python'], dict)
    # Asserting python_facts['python'] has 'version' as a key
    assert ('version' in python_facts['python'])
    # Asserting python_facts['python']['version'] is a dict
    assert isinstance(python_facts['python']['version'], dict)
    # Asserting python_facts['python']['

# Generated at 2022-06-13 03:18:42.424292
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    py_fc = PythonFactCollector()
    result = py_fc.collect()
    assert result == {'python': {'executable': '/usr/bin/python', 'has_sslcontext': False, 'version': {'major': 2, 'micro': 7, 'minor': 12, 'releaselevel': 'final', 'serial': 0}, 'version_info': [2, 7, 12, 'final', 0], 'type': 'CPython'}}

# Generated at 2022-06-13 03:18:49.323975
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """
        Unit test to check collection of python facts using
        method collect of class PythonFactCollector.
    """
    py_col = PythonFactCollector()

    # The following test verifies if python facts are collected
    # correctly
    py_col_facts = py_col.collect()
    assert py_col_facts['python']['version']['major'] == sys.version_info[0],\
        ("Version major of python should be {0} and not {1}"
            .format(sys.version_info[0], py_col_facts['python']['version']['major']))

# Generated at 2022-06-13 03:18:57.557026
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    from ansible.module_utils.facts.collector.python import PythonFactCollector
    from ansible.module_utils.facts.collector import BaseFactCollector

    pfc = PythonFactCollector(None)
    assert isinstance(pfc, BaseFactCollector)

    facts_dict = pfc.collect()
    assert 'python' in facts_dict
    assert 'version' in facts_dict['python']
    assert 'version_info' in facts_dict['python']
    assert 'executable' in facts_dict['python']
    assert 'has_sslcontext' in facts_dict['python']
    assert 'type' in facts_dict['python']

# Generated at 2022-06-13 03:19:38.668841
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_collector = PythonFactCollector()
    results = python_collector.collect()

    assert results['python']['version']['major'] == sys.version_info[0]
    assert results['python']['version']['minor'] == sys.version_info[1]
    assert results['python']['version']['micro'] == sys.version_info[2]
    assert results['python']['version']['releaselevel'] == sys.version_info[3]
    assert results['python']['version']['serial'] == sys.version_info[4]
    assert results['python']['version_info'] == list(sys.version_info)
    assert results['python']['executable'] == sys.executable
    assert results['python']['has_sslcontext'] == HAS

# Generated at 2022-06-13 03:19:46.183325
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    collected_facts = {'ansible_python': {'has_sslcontext': True,
                                          'version': {'major': 2,
                                                      'micro': 7,
                                                      'minor': 12,
                                                      'releaselevel': 'final',
                                                      'serial': 0},
                                          'type': 'CPython',
                                          'version_info': [2, 7, 12, 'final', 0]},
                       'ansible_python_version': '2.7.12'}

    assert PythonFactCollector().collect(collected_facts=collected_facts) == collected_facts

# Generated at 2022-06-13 03:19:47.480819
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pycoll = PythonFactCollector()

    assert pycoll.collect() is not None

# Generated at 2022-06-13 03:19:56.873867
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = PythonFactCollector().collect()
    assert 'python' in python_facts

    python_info = python_facts['python']
    assert isinstance(python_info, dict)

    assert 'version' in python_info
    version = python_info['version']
    assert isinstance(version, dict)
    assert 'major' in version
    assert isinstance(version['major'], int)
    assert 'minor' in version
    assert isinstance(version['minor'], int)
    assert 'micro' in version
    assert isinstance(version['micro'], int)
    assert 'releaselevel' in version
    assert isinstance(version['releaselevel'], str)
    assert 'serial' in version
    assert isinstance(version['serial'], int)

    assert 'version_info' in python_info
   

# Generated at 2022-06-13 03:20:04.920550
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """
    Unit test for method collect of class PythonFactCollector
    """
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
            'has_sslcontext': HAS_SSLCONTEXT
        }
    }

# Generated at 2022-06-13 03:20:10.356037
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    collector = PythonFactCollector()
    assert collector.collect().get('python') == {
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
        'type': sys.subversion[0]
    }

# Generated at 2022-06-13 03:20:14.504375
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pc = PythonFactCollector(None)
    facts_dict = pc.collect()
    assert set(facts_dict.keys()) == set(['python']), 'test_PythonFactCollector_collect assert #1 has failed.'
    assert set(facts_dict['python'].keys()) == set(['version', 'version_info', 'executable', 'has_sslcontext']), 'test_PythonFactCollector_collect assert #2 has failed.'

# Generated at 2022-06-13 03:20:20.559369
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    c = PythonFactCollector()
    facts = c.collect()
    assert facts['python']['version']['major'] == sys.version_info[0]
    assert facts['python']['version']['minor'] == sys.version_info[1]
    assert facts['python']['version']['micro'] == sys.version_info[2]
    assert facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert facts['python']['version']['serial'] == sys.version_info[4]
    assert facts['python']['version_info'] == list(sys.version_info)
    assert facts['python']['executable'] == sys.executable
    assert facts['python']['has_sslcontext'] == HAS_SSLCONTEXT


# Generated at 2022-06-13 03:20:22.747522
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector()
    fact_collector.collect()


if __name__ == '__main__':
    test_PythonFactCollector_collect()

# Generated at 2022-06-13 03:20:28.370035
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """Test PythonFactCollector.collect()."""
    fact_collector = PythonFactCollector()
    collected_facts = fact_collector.collect()
    assert collected_facts is not None, 'PythonFactCollector.collect did not collect any data'
    assert 'python' in collected_facts,\
        'PythonFactCollector.collect did not collect any python related facts'
    keys = ['version', 'version_info', 'executable', 'type']
    for key in keys:
        assert key in collected_facts['python'],\
            'Key {} not found in collected python facts'.format(key)

# Generated at 2022-06-13 03:21:43.367106
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = PythonFactCollector().collect()
    assert 'python' in python_facts, "Failed to convert python version to dict"
    python_version = python_facts['python']
    assert 'version' in python_version, "Failed to set python version"
    assert 'version_info' in python_version, "Failed to set python version_info"
    assert 'executable' in python_version, "Failed to set python executable"
    assert 'has_sslcontext' in python_version, "Failed to set python has_sslcontext"
    assert 'type' in python_version, "Failed to set python type"

# Test for method collect of class PythonFactCollector for Python 2.4

# Generated at 2022-06-13 03:21:49.493420
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = PythonFactCollector().collect()
    assert sys.version_info[0] == python_facts['python']['version']['major']
    assert sys.version_info[1] == python_facts['python']['version']['minor']
    assert sys.version_info[2] == python_facts['python']['version']['micro']
    assert sys.version_info[3] == python_facts['python']['version']['releaselevel']
    assert sys.version_info[4] == python_facts['python']['version']['serial']
    assert list(sys.version_info) == python_facts['python']['version_info']
    assert sys.executable == python_facts['python']['executable']
    assert HAS_SSLCONTEXT == python_

# Generated at 2022-06-13 03:21:54.993776
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector()
    facts = pfc.collect()
    assert pfc.name == 'python'
    assert facts['python']['version']['major'] == sys.version_info[0]
    assert facts['python']['version']['minor'] == sys.version_info[1]
    assert facts['python']['version']['micro'] == sys.version_info[2]
    assert facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert facts['python']['version']['serial'] == sys.version_info[4]
    assert facts['python']['version_info'] == list(sys.version_info)
    assert facts['python']['executable'] == sys.executable

# Generated at 2022-06-13 03:21:57.216940
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact_collector = PythonFactCollector()
    assert python_fact_collector.collect() != {}


# Generated at 2022-06-13 03:22:00.140541
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = PythonFactCollector().collect()
    assert python_facts['python']['version']['major'] == sys.version_info[0]

# Generated at 2022-06-13 03:22:07.156275
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pf = PythonFactCollector()
    res = pf.collect()
    assert 'python' in res
    assert res['python']['has_sslcontext'] == HAS_SSLCONTEXT
    assert 'type' in res['python']
    assert res['python']['type'] in ['CPython', 'Jython', 'PyPy']
    assert 'version' in res['python']
    assert 'version_info' in res['python']
    assert res['python']['version']['releaselevel'] in ('alpha', 'beta', 'candidate', 'final')
    assert res['python']['version']['serial'] in (0, 1)
    assert res['python']['executable'] == sys.executable

# Generated at 2022-06-13 03:22:10.912243
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """PythonFactCollector - test for collect method"""
    # Create a PythonFactCollector object
    obj = PythonFactCollector()

    # Test collect method with default values
    ret = obj.collect()
    assert isinstance(ret, dict)
    assert 'python' in ret