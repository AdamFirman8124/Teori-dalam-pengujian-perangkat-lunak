

# Generated at 2022-06-13 03:12:21.485507
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = PythonFactCollector().collect()

    version = python_facts['python']['version']
    version_info = python_facts['python']['version_info']
    executable = python_facts['python']['executable']
    has_sslcontext = python_facts['python']['has_sslcontext']

    assert isinstance(version, dict), "Failed to determine Python version."
    assert isinstance(version_info, list), "Failed to determine Python version_info."
    assert isinstance(executable, str), "Failed to determine Python executable path."
    assert isinstance(has_sslcontext, bool), "Failed to determine Python SSLContext support."

# Generated at 2022-06-13 03:12:24.209248
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    from ansible.module_utils.facts.collector import add_collector
    from ansible.module_utils.facts import collectors

    fact_collector = PythonFactCollector()

    fact_collector.collect()

# Generated at 2022-06-13 03:12:27.163844
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact_collector = PythonFactCollector()
    python_facts = python_fact_collector.collect()
    assert 'python' in python_facts.keys(), "Python facts does not contain python key"

# Generated at 2022-06-13 03:12:32.836924
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    assert PythonFactCollector.name == 'python'
    assert PythonFactCollector._fact_ids == set()
    assert PythonFactCollector.collect() == \
           {'python': {'version': {'major': 3, 'minor': 6, 'micro': 2,
                                   'releaselevel': 'final', 'serial': 0},
                       'version_info': [3, 6, 2, 'final', 0],
                       'executable': sys.executable,
                       'has_sslcontext': HAS_SSLCONTEXT,
                       'type': sys.implementation.name}}

# Generated at 2022-06-13 03:12:34.793445
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """Ensures the output of the method collect(self, module=None, collected_facts=None) is dict type"""
    x = PythonFactCollector()
    result = x.collect()
    assert isinstance(result, dict)

# Generated at 2022-06-13 03:12:37.288746
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = PythonFactCollector().collect()
    assert 'has_sslcontext' in python_facts['python']

# Generated at 2022-06-13 03:12:44.255938
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    facts_collector = Collector()
    pythonFactCollector = PythonFactCollector(facts_collector)

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

    # CPython

# Generated at 2022-06-13 03:12:46.773217
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    collector = PythonFactCollector()

    result = collector.collect(None, None)

    assert result['python']['version']['major'] == sys.version_info[0]

# Generated at 2022-06-13 03:12:54.953775
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    c = PythonFactCollector()
    assert c.collect()['python'] == {
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

# Generated at 2022-06-13 03:12:58.238353
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """Test for collect method for PythonFactCollector."""
    py_dummy = PythonFactCollector()
    py_dummy.collect()
    assert 'python' in py_dummy.collect()

# Generated at 2022-06-13 03:13:12.399514
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    # test simple facts
    python_facts = PythonFactCollector().collect({}, {})
    assert python_facts['python']['version']['major'] == sys.version_info[0]
    assert python_facts['python']['version']['minor'] == sys.version_info[1]
    assert python_facts['python']['version']['micro'] == sys.version_info[2]
    assert python_facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert python_facts['python']['version']['serial'] == sys.version_info[4]
    assert python_facts['python']['version_info'] == list(sys.version_info)
    assert python_facts['python']['executable'] == sys.executable

    #

# Generated at 2022-06-13 03:13:17.254164
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Initialize BaseFactCollector class
    python_fact = PythonFactCollector()

    # Invoke method collect of class PythonFactCollector
    python_facts = python_fact.collect()

    # Check python_facts['python'] is True
    assert 'python' in python_facts
    assert python_facts['python']['version']['major'] is sys.version_info[0]

# Generated at 2022-06-13 03:13:22.272497
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    c = PythonFactCollector()
    res = c.collect()

    assert 'executable' in res['python']
    assert 'has_sslcontext' in res['python']
    assert 'type' in res['python']
    assert 'version' in res['python']
    assert 'version_info' in res['python']

# Generated at 2022-06-13 03:13:39.261103
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    p = PythonFactCollector()
    result = p.collect()
    assert result
    assert result == {
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

# Generated at 2022-06-13 03:13:47.335889
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Instantiation
    collector = PythonFactCollector()
    # collect method
    collected_facts = collector.collect()
    # Testing presence of mandatory entries:
    # - python
    assert "python" in collected_facts, "Fact 'python' missing in collected facts by {}".format(collector.name)
    # - version
    assert "version" in collected_facts["python"], "Fact 'python.version' missing in collected facts by {}".format(collector.name)
    # - version_info
    assert "version_info" in collected_facts["python"], "Fact 'python.version_info' missing in collected facts by {}".format(collector.name)
    # - executable
    assert "executable" in collected_facts["python"], "Fact 'python.executable' missing in collected facts by {}".format(collector.name)
   

# Generated at 2022-06-13 03:13:57.897457
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    import sys
    # Make sure we get reasonable defaults if sys.version_info doesn't exist
    python_facts = {
        'python': {
            'version': {
                'major': 'unknown',
                'minor': 'unknown',
                'micro': 'unknown',
                'releaselevel': 'unknown',
                'serial': 'unknown'
            },
            'version_info': 'unknown',
            'executable': sys.executable,
            'has_sslcontext': HAS_SSLCONTEXT
        }
    }

    expected = dict(sys=sys, sys_version_info = sys.version_info, sys_subversion = sys.subversion, HAS_SSLCONTEXT = HAS_SSLCONTEXT)
    test = PythonFactCollector()
    result = test.collect(expected)
    assert result == python_facts

# Generated at 2022-06-13 03:14:02.337595
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact = PythonFactCollector()
    facts = python_fact.collect()
    assert 'python' in facts
    assert 'version' in facts['python']
    assert 'version_info' in facts['python']
    assert 'executable' in facts['python']

# Generated at 2022-06-13 03:14:10.716983
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    PC = PythonFactCollector()
    result = PC.collect(None, None)
    assert result['python']['version']['major'] == sys.version_info[0]
    assert result['python']['version']['minor'] == sys.version_info[1]
    assert result['python']['version']['micro'] == sys.version_info[2]
    assert result['python']['version']['releaselevel'] == sys.version_info[3]
    assert result['python']['version']['serial'] == sys.version_info[4]
    assert result['python']['version_info'] == list(sys.version_info)
    assert result['python']['executable'] == sys.executable

# Generated at 2022-06-13 03:14:20.922942
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.utils import find_collector
    from ansible.module_utils.facts.system.python import PythonFactCollector

    c = Collector()
    f = Collector.get_fact_class('python')
    c.add_collector(f)
    facts = c.collect(module=None, collected_facts=None)

    fc = find_collector('python', PythonFactCollector)
    facts = fc.collect(module=None, collected_facts=None)
    assert 'python' in facts
    assert 'version' in facts['python']
    assert 'version_info' in facts['python']
    assert 'executable' in facts['python']
    assert 'has_sslcontext' in facts['python']

# Generated at 2022-06-13 03:14:25.407722
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Test that method collect of class PythonFactCollector works as expected
    python_fact_collector_obj = PythonFactCollector()
    pytho_facts = python_fact_collector_obj.collect()
    assert isinstance(pytho_facts, dict)
    assert 'python' in pytho_facts

# Generated at 2022-06-13 03:14:34.749999
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = {}
    python_fact_collector = PythonFactCollector()
    python_facts = python_fact_collector.collect()

    assert python_facts['python']['version']
    assert python_facts['python']['version_info']
    assert python_facts['python']['executable']

# Generated at 2022-06-13 03:14:40.643574
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector(None)
    result = pfc.collect()

    assert type(result) == dict
    assert 'python' in result
    assert 'type' in result['python']
    assert 'version' in result['python']
    assert 'has_sslcontext' in result['python']
    assert 'version_info' in result['python']
    assert 'executable' in result['python']

# Generated at 2022-06-13 03:14:48.216230
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = PythonFactCollector().collect()
    # checks at least one key
    assert python_facts['python']['executable']
    assert isinstance(python_facts['python']['version']['major'], int)
    assert isinstance(python_facts['python']['version_info'], list)
    assert isinstance(python_facts['python']['has_sslcontext'], bool)
    assert python_facts['python']['type'] in ['CPython', 'PyPy']

# Generated at 2022-06-13 03:14:53.216564
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    facts_collector = PythonFactCollector()
    collected_facts = facts_collector.collect()
    assert collected_facts['python']['version']['major'] == 2
    assert collected_facts['python']['type'] == 'CPython'
    assert isinstance(collected_facts['python']['version_info'], list)


# Generated at 2022-06-13 03:15:00.138227
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    python_fact_collector = PythonFactCollector()
    python_facts = python_fact_collector.collect(module=None, collected_facts=None)

    truth_dict = {
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


# Generated at 2022-06-13 03:15:09.651637
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    from ansible.module_utils.facts.collector import PythonFactCollector
    from ansible.module_utils.facts.system import PythonFactCollector
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes


# Generated at 2022-06-13 03:15:17.010091
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    import os
    import sys
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = PythonFactCollector()
    result = collector.collect()
    assert result == {
        'python': {
            'version': {
                'major': sys.version_info.major,
                'minor': sys.version_info.minor,
                'micro': sys.version_info.micro,
                'releaselevel': sys.version_info.releaselevel,
                'serial': sys.version_info.serial
            },
            'version_info': list(sys.version_info),
            'executable': sys.executable,
            'has_sslcontext': HAS_SSLCONTEXT,
            'type': sys.implementation.name
        }
    }


# Generated at 2022-06-13 03:15:33.256305
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """Unit test method collect of class PythonFactCollector"""
    pfc = PythonFactCollector({}, None)
    result = pfc.collect()

    assert 'python' in result
    assert result['python']['version']['major'] == 3
    assert result['python']['version']['minor'] == 6
    assert result['python']['version']['micro'] > 0
    assert result['python']['version']['releaselevel'] == 'final'
    assert result['python']['version']['serial'] > 0
    assert result['python']['version_info'] == [3, 6, 0, 'final', 0]
    assert result['python']['has_sslcontext'] is True

# Generated at 2022-06-13 03:15:39.103199
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector(None, None)
    facts = fact_collector.collect()
    assert facts['python']['version']['major'] == sys.version_info[0]
    assert facts['python']['version']['minor'] == sys.version_info[1]
    assert facts['python']['version']['micro'] == sys.version_info[2]
    assert facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert facts['python']['version']['serial'] == sys.version_info[4]
    assert facts['python']['version_info'] == list(sys.version_info)
    assert facts['python']['has_sslcontext'] == HAS_SSLCONTEXT

# Generated at 2022-06-13 03:15:41.865042
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fc = PythonFactCollector()
    facts = fc.collect(module=None, collected_facts=None)
    assert isinstance(facts['python'], dict)

# Generated at 2022-06-13 03:15:56.299041
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    c = PythonFactCollector()
    facts = c.collect()
    assert isinstance(facts['python']['version']['major'], int)
    assert isinstance(facts['python']['version']['minor'], int)
    assert isinstance(facts['python']['version']['micro'], int)
    assert isinstance(facts['python']['version']['releaselevel'], str)
    assert isinstance(facts['python']['version']['serial'], int)
    assert isinstance(facts['python']['has_sslcontext'], bool)
    assert facts['python']['has_sslcontext'] == HAS_SSLCONTEXT

# Generated at 2022-06-13 03:15:57.618830
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector()
    assert pfc.collect()['python']['version']['major'] == sys.version_info[0]

# Generated at 2022-06-13 03:16:01.797718
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    option_dict = {}
    fact_collector = PythonFactCollector(option_dict)
    fact_dict = fact_collector.collect()

    assert 'python' in fact_dict
    assert 'version' in fact_dict['python']
    assert 'type' in fact_dict['python']
    assert 'executable' in fact_dict['python']

# Generated at 2022-06-13 03:16:10.300784
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    import sys
    import ansible.module_utils.facts.collectors.python
    reload(sys)
    reload(ansible.module_utils.facts.collectors.python)

    py_col = ansible.module_utils.facts.collectors.python.PythonFactCollector()
    py_facts = py_col.collect()
    assert py_facts['python']['version']['major'] == sys.version_info[0]
    assert py_facts['python']['version']['minor'] == sys.version_info[1]
    assert py_facts['python']['version']['micro'] == sys.version_info[2]
    assert py_facts['python']['version']['releaselevel'] == sys.version_info[3]

# Generated at 2022-06-13 03:16:20.477339
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector()
    fact_collector._populate_allowed_collection_methods()
    collected_facts = fact_collector.collect(module=None, collected_facts={})
    assert collected_facts['python']['version']['major'] == sys.version_info[0]
    assert collected_facts['python']['version']['minor'] == sys.version_info[1]
    assert collected_facts['python']['version']['micro'] == sys.version_info[2]
    assert collected_facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert collected_facts['python']['version']['serial'] == sys.version_info[4]
    assert collected_facts['python']['version_info'] == list

# Generated at 2022-06-13 03:16:24.358298
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector()
    ret = {}
    ret = pfc.collect()
    assert 'python' in ret
    assert 'version' in ret['python']
    assert 'version_info' in ret['python']
    assert 'executable' in ret['python']
    assert 'has_sslcontext' in ret['python']
    assert 'type' in ret['python']

# Generated at 2022-06-13 03:16:31.538177
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    expected_python_facts = {
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

# Generated at 2022-06-13 03:16:33.329976
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_collector = PythonFactCollector()
    print(python_collector.collect())
    assert isinstance(python_collector.collect(),dict)

# Generated at 2022-06-13 03:16:37.566861
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # set up
    python_facts = PythonFactCollector()
    assert python_facts.collect().has_key('python')
    info = python_facts.collect()['python']
    assert info.has_key('type')
    assert info.has_key('version')
    assert info.has_key('version_info')
    assert info.has_key('has_sslcontext')
    assert info.has_key('executable')

    # clean up

# Generated at 2022-06-13 03:16:40.970451
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact_collector = PythonFactCollector()
    python_fact_collector.collect()

# Generated at 2022-06-13 03:16:59.559972
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """Test method collect of class PythonFactCollector"""
    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts import default_collectors

    # Instantiate a default set of collectors that will be available
    collector_list = default_collectors
    python_fact_collector = get_collector_instance(collector_list, 'python')
    fact_list = python_fact_collector.collect()

    assert fact_list is not None
    assert type(fact_list) is dict
    assert 'python' in fact_list.keys()
    assert 'version' in fact_list['python'].keys()
    assert 'version_info' in fact_list['python'].keys()

# Generated at 2022-06-13 03:17:01.166851
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    collector = PythonFactCollector()
    results = collector.collect()
    assert results is not None
    assert results.get('python') is not None

# Generated at 2022-06-13 03:17:05.449906
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # create a fact collector object
    fact = PythonFactCollector(None)

    # get the facts
    facts = fact.collect()

    # test for package facts
    for f in facts:
        assert f['ansible_facts'] == facts[f]


# Generated at 2022-06-13 03:17:13.232784
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact_collector = PythonFactCollector()

    test_facts = python_fact_collector.collect()

    assert test_facts['python']['version'] == {
        'major': sys.version_info[0],
        'minor': sys.version_info[1],
        'micro': sys.version_info[2],
        'releaselevel': sys.version_info[3],
        'serial': sys.version_info[4]
    }

    assert test_facts['python']['version_info'] == list(sys.version_info)

    assert test_facts['python'].get('type')

# Generated at 2022-06-13 03:17:19.933145
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    # Create instance of PythonFactCollector
    fact_collector = PythonFactCollector()

    # Mock method collect of BaseFactCollector
    fact_collector._read_config = lambda x,y: y

    # Call method collect of class PythonFactCollector
    python_facts = fact_collector.collect()

    # Assert that python_facts is a dictionary
    assert isinstance(python_facts, dict)
    assert 'python' in python_facts.keys()

    # Assert that python_facts['python'] is a dictionary with the correct keys
    assert isinstance(python_facts['python'], dict)
    assert 'version' in python_facts['python'].keys()
    assert 'version_info' in python_facts['python'].keys()
    assert 'executable' in python_facts['python'].keys()

    #

# Generated at 2022-06-13 03:17:22.054204
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """
    test for collection of python facts
    """
    py_fc = PythonFactCollector(None, None)
    py_facts = py_fc.collect()
    assert isinstance(py_facts, dict)

# Generated at 2022-06-13 03:17:22.795832
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    assert PythonFactCollector().collect()

# Generated at 2022-06-13 03:17:23.797805
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    collector = PythonFactCollector()

    assert isinstance(collector.collect(), dict)

# Generated at 2022-06-13 03:17:29.225618
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    module = None
    collected_facts = None
    collector = PythonFactCollector(module, collected_facts)
    facts = collector.collect()
    assert sorted(facts.keys()) == sorted(['python'])
    assert facts['python']['type'] == 'CPython'
    assert facts['python']['executable'] == sys.executable
    assert facts['python']['version_info'] == list(sys.version_info)
    assert facts['python']['version']['major'] == sys.version_info[0]
    assert facts['python']['version']['minor'] == sys.version_info[1]
    assert facts['python']['version']['micro'] == sys.version_info[2]
    assert facts['python']['version']['releaselevel'] == sys.version_

# Generated at 2022-06-13 03:17:31.575948
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Initialize a new PythonFactCollector class
    pfc = PythonFactCollector()
    # Test the collect method and assert if the returned value is an array
    assert isinstance(pfc.collect(), dict)

# Generated at 2022-06-13 03:17:50.424831
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    __test__ = True
    fc = PythonFactCollector()
    facts = fc.collect()

    assert isinstance(facts['python'], dict)
    assert isinstance(facts['python']['version_info'], list)
    assert isinstance(facts['python']['has_sslcontext'], bool)
    assert facts['python']['version']['releaselevel'] in ['alpha', 'beta', 'candidate', 'final']

# Generated at 2022-06-13 03:17:53.831353
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    py = PythonFactCollector()

    result = py.collect()
    assert 'python' in result
    assert isinstance(result['python']['version_info'], list)

# Generated at 2022-06-13 03:18:02.228778
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    from ansible.module_utils.facts import Collector
    from ansible.module_utils.facts.collector import get_collector_instance
    collector = get_collector_instance(Collector)
    python_collector = get_collector_instance(PythonFactCollector)
    # Test that fact collection is OK
    python_collector.collect(None, collector)
    # Test that fact collection is correct
    assert 'python' in collector
    assert collector['python']
    assert 'version' in collector['python']
    assert collector['python']['version']
    assert 'major' in collector['python']['version']
    assert collector['python']['version']['major'] == sys.version_info[0]
    assert 'minor' in collector['python']['version']

# Generated at 2022-06-13 03:18:10.826051
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = PythonFactCollector().collect()
    assert python_facts['python']['version']['major'] == sys.version_info[0], "Major version is incorrect"
    assert python_facts['python']['version']['minor'] == sys.version_info[1], "Minor version is incorrect"
    assert python_facts['python']['version']['micro'] == sys.version_info[2], "Micro version is incorrect"
    assert python_facts['python']['version']['releaselevel'] == sys.version_info[3], "Release level is incorrect"
    assert python_facts['python']['version']['serial'] == sys.version_info[4], "Serial is incorrect"

# Generated at 2022-06-13 03:18:16.014473
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts import ansible_facts
    collector = Collector(lambda: [PythonFactCollector()], ansible_facts)
    facts = collector.collect(module=None, collected_facts=None)
    assert 'python' in facts
    assert 'version' in facts['python']
    assert 'version_info' in facts['python']
    assert 'executable' in facts['python']
    assert 'has_sslcontext' in facts['python']
    assert 'type' in facts['python']
    assert type(facts['python']['version']) == dict
    assert type(facts['python']['version_info']) == list
    assert type(facts['python']['executable']) == str

# Generated at 2022-06-13 03:18:24.326196
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_collector = PythonFactCollector()
    results = python_collector.collect()
    assert results
    assert results['python']
    assert results['python']['version']
    assert results['python']['version_info']
    assert results['python']['executable']
    assert results['python']['has_sslcontext']
    # Ansible 2.3 and earlier had a bug where this was set to 'cpython-32'.
    # We keep it around for now so we don't break compat for anyone
    # that might have been using this fact.
    assert results['python']['type'] in ('cpython', 'cpython-32')

# Generated at 2022-06-13 03:18:32.783230
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    module = None
    collected_facts = None
    python_fact_collector = PythonFactCollector()
    python_facts = python_fact_collector.collect(module, collected_facts)
    assert python_facts['python']['version']['major'] == sys.version_info[0]
    assert python_facts['python']['version']['minor'] == sys.version_info[1]
    assert python_facts['python']['version']['micro'] == sys.version_info[2]
    assert python_facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert python_facts['python']['version']['serial'] == sys.version_info[4]

# Generated at 2022-06-13 03:18:37.737433
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """create an instance of PythonFactCollector and call collect"""
    py_col = PythonFactCollector()
    facts = py_col.collect()

    assert facts['python']['version']
    assert facts['python']['version_info']
    assert facts['python']['executable']
    assert facts['python']['has_sslcontext']
    assert facts['python']['type']

# Generated at 2022-06-13 03:18:39.146682
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    class_instance = PythonFactCollector()
    assert class_instance.collect() is not None


# Generated at 2022-06-13 03:18:42.786164
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    facts = PythonFactCollector().collect()
    assert isinstance(facts, dict)
    assert 'python' in facts
    assert isinstance(facts['python'], dict)
    assert 'version' in facts['python']
    assert 'version_info' in facts['python']
    assert 'executable' in facts['python']


# Generated at 2022-06-13 03:19:17.791082
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector(None, {})
    fact_collector.collect()

if __name__ == '__main__':
    test_PythonFactCollector_collect()

# Generated at 2022-06-13 03:19:28.003021
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    fcm = PythonFactCollector()

    if sys.version_info[3] == 'final':
        releaselevel = 'final'
    else:
        releaselevel = '%s%s' % (sys.version_info[3], sys.version_info[4])

    if HAS_SSLCONTEXT:
        has_sslcontext = True
    else:
        has_sslcontext = False

    try:
        type_ = sys.subversion[0]
    except AttributeError:
        try:
            type_ = sys.implementation.name
        except AttributeError:
            type_ = None


# Generated at 2022-06-13 03:19:33.086602
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    collector = PythonFactCollector()
    result = collector.collect()
    assert result['python']['executable'] == sys.executable
    assert result['python']['version']['major'] == sys.version_info[0]
    assert 'has_sslcontext' in result['python']
    if 'subversion' in sys.__dict__:
        assert result['python']['type'] == sys.subversion[0]
    elif 'implementation' in sys.__dict__:
        assert result['python']['type'] == sys.implementation.name
    else:
        assert result['python']['type'] is None

# Generated at 2022-06-13 03:19:43.006812
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    obj = PythonFactCollector()
    result = obj.collect()
    assert type(result) is dict, "Returned result is not a dictionary"
    assert len(result.keys()) > 0, "At least one key should be defined"
    test_version_key = 'version'
    assert test_version_key in result['python'], "The '{0}' key should be defined".format(test_version_key)
    # Now verify more keys in the 'version' sub-dictionary
    assert type(result['python']['version']) is dict, "The '{0}' key value is not a dictionary".format(test_version_key)
    test_version_keys = ['major', 'minor', 'micro', 'releaselevel', 'serial']

# Generated at 2022-06-13 03:19:47.354385
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """This unit test tests the method collect of class PythonFactCollector"""
    pfc = PythonFactCollector()

    # Testing
    collected_facts = pfc.collect()
    assert collected_facts['python']['version']['major'] == sys.version_info[0]
    assert collected_facts['python']['version']['minor'] == sys.version_info[1]
    assert collected_facts['python']['version']['micro'] == sys.version_info[2]
    assert collected_facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert collected_facts['python']['version']['serial'] == sys.version_info[4]
    assert collected_facts['python']['version_info'] == list(sys.version_info)
   

# Generated at 2022-06-13 03:19:56.776236
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    c = PythonFactCollector()
    assert c.collect()['python']['type'] in ['CPython', 'PyPy']
    assert c.collect()['python']['version']['major'] == sys.version_info[0]
    assert c.collect()['python']['version']['minor'] == sys.version_info[1]
    assert c.collect()['python']['version']['micro'] == sys.version_info[2]
    assert c.collect()['python']['version']['releaselevel'] == sys.version_info[3]
    assert c.collect()['python']['version']['serial'] == sys.version_info[4]
    assert c.collect()['python']['version_info'] == list(sys.version_info)
    assert c.collect

# Generated at 2022-06-13 03:20:05.651187
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pyfc = PythonFactCollector()
    facts = pyfc.collect()
    assert 'python' in facts

    py_facts = facts['python']
    assert 'version' in py_facts
    py_versions = py_facts['version']
    assert 0 < py_versions['major'] <= sys.maxint
    assert 0 <= py_versions['minor'] <= sys.maxint
    assert 0 <= py_versions['micro'] <= sys.maxint
    assert py_versions['releaselevel'] in ('alpha', 'beta', 'candidate', 'final')
    assert 0 <= py_versions['serial'] <= sys.maxint

    assert 'version_info' in py_facts
    assert isinstance(py_facts['version_info'], list)
    assert sys.version_info[0] == py_facts['version_info'][0]

# Generated at 2022-06-13 03:20:11.848149
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


# Generated at 2022-06-13 03:20:15.555849
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    collector = PythonFactCollector()
    facts = collector.collect()
    assert facts == {'python': {'version': {'major': 3, 'micro': 3, 'releaselevel': 'final', 'minor': 4, 'serial': 0}, 'executable': '/usr/bin/python', 'has_sslcontext': True, 'version_info': [3, 4, 3, 'final', 0], 'type': 'CPython'}}

# Generated at 2022-06-13 03:20:21.386971
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact_collector_object = PythonFactCollector()

    # If python executable is not present, test will raise an exception.
    # Hence, conditionally import and execute test_case.
    try:
        python_fact_collector_object.collect()
    except Exception:
        import os
        import pytest
        pytest.skip("python executable not found.")

    assert len(python_fact_collector_object.collect()) == 1
    assert 'python' in python_fact_collector_object.collect()

    assert 'version' in python_fact_collector_object.collect()['python']
    assert 'version_info' in python_fact_collector_object.collect()['python']
    assert 'executable' in python_fact_collector_object.collect()['python']
    assert 'type' in python_

# Generated at 2022-06-13 03:21:35.877255
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    python_facts = {'python': {
        'executable': '/usr/bin/python',
        'has_sslcontext': HAS_SSLCONTEXT,
        'type': 'CPython',
        'version_info': [2, 7, 12, 'final', 0],
        'version': {
            'major': 2,
            'minor': 7,
            'micro': 12,
            'releaselevel': 'final',
            'serial': 0
        }
    }}

    python_fact_collector = PythonFactCollector()
    collected_facts = {}
    python_fact_collector.collect(module=None, collected_facts=collected_facts)
    assert collected_facts == python_facts

# Tests for class PythonFactCollector added for coverage purposes

# Generated at 2022-06-13 03:21:40.996731
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fc = PythonFactCollector()
    facts = fc.collect()
    assert facts == {'python': {'type': 'CPython',
                                'version': {'micro': 1,
                                            'minor': 5,
                                            'releaselevel': 'final',
                                            'serial': 1,
                                            'major': 2},
                                'version_info': [2, 7, 17, 'final', 1],
                                'executable': '/usr/bin/python',
                                'has_sslcontext': True}}

# Generated at 2022-06-13 03:21:46.823620
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    '''
    PythonFactCollector.collect should return a dictionary
    with at least the following keys:
        - python.version.major
        - python.version.minor
        - python.version.micro
        - python.version.releaselevel
        - python.version.serial
        - python.version_info
        - python.executable
    '''

    python_facts = PythonFactCollector().collect()

    assert set(['major', 'minor', 'micro', 'releaselevel', 'serial']) <= set(python_facts['python']['version'])
    assert type(python_facts['python']['version_info']) is list
    assert type(python_facts['python']['executable']) is str

# Generated at 2022-06-13 03:21:49.701516
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector()
    python_facts = pfc.collect()
    assert 'python' in python_facts
    assert 'version' in python_facts['python']
    assert 'executable' in python_facts['python']
    assert 'has_sslcontext' in python_facts['python']

# Generated at 2022-06-13 03:22:00.383849
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_pc = PythonFactCollector()
    python_facts = python_pc.collect()['python']
    # Check if the version is in the expected format
    assert python_facts['version']['major'] in ['2', '3']
    # Check if the version is in the expected format
    assert python_facts['version']['minor'] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    assert python_facts['version']['micro'] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    assert python_facts['version']['releaselevel'] in ['alpha', 'beta', 'candidate', 'final']
    # Check if the serial is in the expected format


# Generated at 2022-06-13 03:22:05.274732
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    from ansible.module_utils.facts import collector

    py_collector = collector.get_collector('python')
    result = py_collector.collect({'python': {'version_info': list(sys.version_info), 'executable': sys.executable, 'has_sslcontext': HAS_SSLCONTEXT}}, {})
    py_collector.assert_print(result)


# Generated at 2022-06-13 03:22:06.172832
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector(None)
    pfc.collect()

# Generated at 2022-06-13 03:22:12.254362
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector()
    assert fact_collector.collect() == {'python': {'version': {'major': sys.version_info[0], 'minor': sys.version_info[1], 'micro': sys.version_info[2], 'releaselevel': sys.version_info[3], 'serial': sys.version_info[4]}, 'version_info': list(sys.version_info), 'executable': sys.executable, 'has_sslcontext': HAS_SSLCONTEXT}}

# Generated at 2022-06-13 03:22:14.017984
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    fact_collector = PythonFactCollector()
    facts = fact_collector.collect()
    assert facts['python']['version']['major'] == 3