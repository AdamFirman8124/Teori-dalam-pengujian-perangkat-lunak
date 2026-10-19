

# Generated at 2022-06-13 03:12:20.257793
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    try:
        # pylint: disable=no-member
        from ssl import create_default_context
        from ssl import SSLContext
        from ssl import PROTOCOL_SSLv23
        del create_default_context
        del SSLContext
    except ImportError:
        has_sslcontext = False
    else:
        has_sslcontext = True


# Generated at 2022-06-13 03:12:37.746035
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

# Generated at 2022-06-13 03:12:41.959951
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    py = PythonFactCollector()
    assert hasattr(py, 'name')
    assert hasattr(py, 'collect')
    facts = py.collect()
    assert 'version_info' in facts['python']
    assert 'version' in facts['python']
    assert 'executable' in facts['python']
    assert 'has_sslcontext' in facts['python']
    if 'type' in facts['python']:
        assert facts['python']['type']

# Generated at 2022-06-13 03:12:46.526303
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pyfact = PythonFactCollector()
    pyfacts = pyfact.collect()

    assert 'python' in pyfacts

    assert 'version' in pyfacts['python']
    assert 'version_info' in pyfacts['python']
    assert 'executable' in pyfacts['python']
    assert 'type' in pyfacts['python']
    assert 'has_sslcontext' in pyfacts['python']


# Generated at 2022-06-13 03:12:56.353410
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    module_mock = {}
    collected_facts_mock = {}
    python_fact_collector = PythonFactCollector()
    result = python_fact_collector.collect(module_mock, collected_facts_mock)
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

    # Manage Python versions which

# Generated at 2022-06-13 03:13:03.929452
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact_collector = PythonFactCollector()
    python_facts = python_fact_collector.collect()
    assert python_facts['python'] == {
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
    assert 'type' in python_facts['python']
    assert python_facts['python']['type'] is not None

# Generated at 2022-06-13 03:13:06.968357
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact = PythonFactCollector()
    assert python_fact.collect == PythonFactCollector.collect

# Generated at 2022-06-13 03:13:12.198747
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    def _get_overrides():
        return {'python': {'version': {'major': 'override',}} }
    def _get_collector():
        return  PythonFactCollector(_get_overrides())


# Generated at 2022-06-13 03:13:13.909560
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    result_dict = PythonFactCollector().collect()
    assert 'python' in result_dict
    assert len(result_dict) == 1

# Generated at 2022-06-13 03:13:22.138477
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Initialize PythonFactCollector object.
    pyfact = PythonFactCollector()

    # Get facts by calling method collect of class PythonFactCollector.
    fact_data = pyfact.collect()

    # Ensure method collect of class PythonFactCollector returned expected results.
    assert 'python' in fact_data
    assert 'executable' in fact_data['python']
    assert 'has_sslcontext' in fact_data['python']
    assert 'type' in fact_data['python']
    assert 'version' in fact_data['python']
    assert 'version_info' in fact_data['python']
    assert 'major' in fact_data['python']['version']
    assert 'minor' in fact_data['python']['version']
    assert 'micro' in fact_data['python']['version']

# Generated at 2022-06-13 03:13:28.227419
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    collector = PythonFactCollector()
    collected_facts = collector.collect()
    assert 'python' in collected_facts
    assert 'version' in collected_facts['python']
    assert 'version_info' in collected_facts['python']
    assert 'executable' in collected_facts['python']
    assert 'type' in collected_facts['python']

# Generated at 2022-06-13 03:13:37.152344
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    ''' Test method collect of class PythonFactCollector. '''
    # Test with no module.
    python_collector = PythonFactCollector()
    assert python_collector.collect() == {'python': {
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
    }}

    # Test with a module.

# Generated at 2022-06-13 03:13:45.616934
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    result = dict()
    def test_collect(collector, module=None, collected_facts=None):
        result['python'] = collector.collect(module, collected_facts)
    collector = PythonFactCollector()
    test_collect(collector)
    assert isinstance(result['python'], dict)
    assert 'version' in result['python']['python']
    assert 'version_info' in result['python']['python']
    assert 'executable' in result['python']['python']
    assert 'type' in result['python']['python']
    assert 'major' in result['python']['python']['version']
    assert 'minor' in result['python']['python']['version']
    assert 'micro' in result['python']['python']['version']

# Generated at 2022-06-13 03:13:57.632458
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    import sys
    import json
    import pytest

    from ansible.module_utils.facts import collector

    python_facts = collector.collect_module_facts('python')
    assert 'python' in python_facts.keys()

    python_version = python_facts['python']['version']
    assert python_version['major'] == sys.version_info[0]
    assert python_version['minor'] == sys.version_info[1]
    assert python_version['micro'] == sys.version_info[2]
    assert python_version['releaselevel'] == sys.version_info[3]
    assert python_version['serial'] == sys.version_info[4]

    python_version_info = python_facts['python']['version_info']
    assert python_version_info == list(sys.version_info)

# Generated at 2022-06-13 03:14:08.031636
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts import Facts
    module = object()
    facts_instance = Facts(module)

    collector = PythonFactCollector(module=module)
    collected_facts = collector.collect(module=module, collected_facts=facts_instance)

    assert type(collected_facts) is dict
    assert collected_facts.get('python')
    assert type(collected_facts['python']) is dict
    assert collected_facts['python']['version']
    assert type(collected_facts['python']['version']) is dict
    assert collected_facts['python']['version']['major'] == 3
    assert type(collected_facts['python']['version']['major']) is int

# Generated at 2022-06-13 03:14:16.693274
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """Test PythonFactCollector.collect"""

    # Fill in the facts which should be collected
    expected_facts = {
        "python": {
            "executable": sys.executable,
            "has_sslcontext": HAS_SSLCONTEXT,
            "version": {
                "major": sys.version_info[0],
                "minor": sys.version_info[1],
                "micro": sys.version_info[2],
                "releaselevel": sys.version_info[3],
                "serial": sys.version_info[4]
            },
            "version_info": list(sys.version_info)
        }
    }

# Generated at 2022-06-13 03:14:26.445621
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_collector = PythonFactCollector()
    result = python_collector.collect()
    assert 'python' in result
    assert 'executable' in result['python']
    assert 'has_sslcontext' in result['python']
    assert 'version' in result['python']
    assert 'version_info' in result['python']
    assert 'type' in result['python']

    # Test for attribute error
    python_collector = PythonFactCollector()
    result = python_collector.collect()
    assert 'python' in result
    assert 'executable' in result['python']
    assert 'has_sslcontext' in result['python']
    assert 'version' in result['python']
    assert 'version_info' in result['python']
    assert 'type' in result['python']


# Generated at 2022-06-13 03:14:33.913107
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

# Generated at 2022-06-13 03:14:43.259085
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    py = PythonFactCollector()
    result = py.collect()

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


# Generated at 2022-06-13 03:14:50.663276
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    collector = PythonFactCollector()
    assert collector.collect() == {'python': {'version': {'major': 2, 'minor': 7, 'micro': 12, 'releaselevel': 'final', 'serial': 0}, 'version_info': [2, 7, 12, 'final', 0], 'executable': '/usr/bin/python', 'type': 'CPython', 'has_sslcontext': True}}, 'Wrong data returned from collect'

# Generated at 2022-06-13 03:14:56.224437
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector()
    fact_collector.collect()
    assert len(fact_collector.collect()) == 1

# Generated at 2022-06-13 03:15:03.730119
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """ Test to collect facts about python interpreter.
    """
    python_fact_collector = PythonFactCollector()
    python_facts = python_fact_collector.collect()
    assert 'python' in python_facts
    assert 'version' in python_facts['python']
    assert 'type' in python_facts['python']
    assert 'executable' in python_facts['python']
    assert 'version_info' in python_facts['python']
    assert 'has_sslcontext' in python_facts['python']

# Generated at 2022-06-13 03:15:05.835435
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector()
    fact_collector.collect()
    python_facts = fact_collector.collect()
    assert python_facts is not None

# Generated at 2022-06-13 03:15:19.376580
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    result = PythonFactCollector().collect()
    assert len(result["python"]["version_info"]) > 0
    assert "python" in result
    assert "version" in result["python"]
    assert "executable" in result["python"]
    if "type" in result["python"]:
        assert result["python"]["type"] == "CPython" or result["python"]["type"] == "PyPy"
    assert result["python"]["has_sslcontext"] is True

# Generated at 2022-06-13 03:15:23.665656
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """ Test collect method of PythonFactCollector
    """

    # Test empty input
    print("Test empty input")
    facts = PythonFactCollector().collect()
    print(facts)

    # Test valid input
    print("Test valid input")
    module = {}
    facts = PythonFactCollector().collect(module=module)
    print(facts)

# Generated at 2022-06-13 03:15:26.153231
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fc = PythonFactCollector()
    result = python_fc.collect()
    assert result

# Generated at 2022-06-13 03:15:35.646673
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """ Test the collect method of class PythonFactCollector"""
    python_facts = PythonFactCollector().collect()
    assert python_facts['python']['version']['major'] == sys.version_info[0]
    assert python_facts['python']['version']['minor'] == sys.version_info[1]
    assert python_facts['python']['version']['micro'] == sys.version_info[2]
    assert python_facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert python_facts['python']['version']['serial'] == sys.version_info[4]
    assert python_facts['python']['version_info'] == list(sys.version_info)

# Generated at 2022-06-13 03:15:38.014894
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # prepare for test
    pc = PythonFactCollector()

    # test and get result
    result = pc.collect()

    # ensure version_info is a list
    assert isinstance(result['python']['version_info'], list)

# Generated at 2022-06-13 03:15:47.162135
# Unit test for method collect of class PythonFactCollector

# Generated at 2022-06-13 03:15:54.277310
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector()

    pfc_collect = pfc.collect()

    python_facts = {'python': {'version': {'major': 3, 'minor': 4, 'micro': 8, 'releaselevel': 'final', 'serial': 0}, 'version_info': [3, 4, 8, 'final', 0], 'executable': '/usr/bin/python3.4'}}

    assert pfc_collect == python_facts

# Generated at 2022-06-13 03:16:10.346061
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
        python_fact_collector = PythonFactCollector()
        facts = python_fact_collector.collect()
        assert python_fact_collector.name == 'python'
        assert facts['python']['version']['major'] == sys.version_info[0]
        assert facts['python']['version']['minor'] == sys.version_info[1]
        assert facts['python']['version']['micro'] == sys.version_info[2]
        assert facts['python']['version']['releaselevel'] == sys.version_info[3]
        assert facts['python']['version']['serial'] == sys.version_info[4]
        assert facts['python']['version_info'] == list(sys.version_info)
        assert facts['python']['executable'] == sys

# Generated at 2022-06-13 03:16:20.521708
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    import distro
    distro_info = distro.info()
    python_fact_collector = PythonFactCollector()
    python_facts = python_fact_collector.collect()
    assert python_facts
    assert 'python' in python_facts
    assert python_facts['python']['version']['major'] == sys.version_info[0]
    assert python_facts['python']['version']['minor'] == sys.version_info[1]
    assert python_facts['python']['version']['micro'] == sys.version_info[2]
    assert python_facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert python_facts['python']['version']['serial'] == sys.version_info[4]
    assert python_facts

# Generated at 2022-06-13 03:16:27.045814
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Setup AnsibleModule to use with PythonFactCollector
    python_fact_collector = PythonFactCollector(module=None)

    # Get python facts to test that the values are correct
    python_facts = python_fact_collector.collect()

    # Assert that python facts are correct
    assert python_facts['python']['version']['major'] == sys.version_info[0]
    assert python_facts['python']['version']['minor'] == sys.version_info[1]
    assert python_facts['python']['version']['micro'] == sys.version_info[2]
    assert python_facts['python']['version']['releaselevel'] == sys.version_info[3]

# Generated at 2022-06-13 03:16:28.321250
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact_collector = PythonFactCollector()
    assert 'python' in python_fact_collector.collect()


# Generated at 2022-06-13 03:16:30.379989
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    p = PythonFactCollector()

    # When HAS_SSLCONTEXT is True, has_sslcontext is expected to be True
    fact_data = p.collect()
    assert fact_data['python']['has_sslcontext']

# Generated at 2022-06-13 03:16:44.079151
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Create empty class
    python_collector = PythonFactCollector()

    # Collect python facts
    facts_dictionary = python_collector.collect(module=None, collected_facts=None)
    python_facts = facts_dictionary.get('python')

    assert python_facts is not None

    assert 'version' in python_facts
    assert 'version_info' in python_facts
    assert 'type' in python_facts
    assert 'executable' in python_facts
    assert 'has_sslcontext' in python_facts

# Generated at 2022-06-13 03:16:49.508395
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():  # pylint: disable=too-many-locals,redefined-outer-name,too-many-nested-blocks,too-many-branches,too-many-statements
    from ansible.module_utils.facts.collector import collect_subset

    collection = collect_subset(['python'])

    assert 'python' in collection, collection

    python_collection = collection['python']

    assert 'python' in python_collection, python_collection

    python_info = python_collection['python']

    assert 'version' in python_info, python_info
    version = python_info['version']
    assert 'major' in version, version
    assert 'minor' in version, version
    assert 'micro' in version, version
    assert 'releaselevel' in version, version
    assert 'serial' in version, version

   

# Generated at 2022-06-13 03:17:00.163001
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

# Generated at 2022-06-13 03:17:10.828265
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = PythonFactCollector().collect()
    assert isinstance(python_facts['python']['version']['major'], int)
    assert isinstance(python_facts['python']['version']['minor'], int)
    assert isinstance(python_facts['python']['version']['micro'], int)
    assert isinstance(python_facts['python']['version']['releaselevel'], str)
    assert isinstance(python_facts['python']['version']['serial'], int)
    assert isinstance(python_facts['python']['version_info'], list)
    assert isinstance(python_facts['python']['executable'], str)
    assert isinstance(python_facts['python']['has_sslcontext'], bool)

# Generated at 2022-06-13 03:17:20.114281
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    try:
        import ansible
        del ansible
        has_ansible = True
    except ImportError:
        has_ansible = False

    d = {
        'ansible': has_ansible,
        'python': {
            'has_sslcontext': HAS_SSLCONTEXT,
            'type': sys.implementation.name,
            'version': {
                'major': sys.version_info[0],
                'micro': sys.version_info[2],
                'minor': sys.version_info[1],
                'releaselevel': sys.version_info[3],
                'serial': sys.version_info[4]
            },
            'version_info': list(sys.version_info),
            'executable': sys.executable
        }
    }

    collector = PythonFactCollector

# Generated at 2022-06-13 03:17:40.106418
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact = PythonFactCollector()

    facts = python_fact.collect()

    assert facts['python']['type'] is not None
    assert facts['python']['version']['major'] is not None
    assert facts['python']['version']['minor'] is not None
    assert facts['python']['version']['micro'] is not None
    assert facts['python']['version']['releaselevel'] is not None
    assert facts['python']['version']['serial'] is not None
    assert facts['python']['version_info'] is not None
    assert facts['python']['executable'] is not None
    assert facts['python']['has_sslcontext'] is not None

# Generated at 2022-06-13 03:17:44.503773
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    # Setup
    # Canned data
    sys.version_info = (3, 6, 7, 'final', 0)
    sys.executable = '/usr/bin/python'
    sys.subversion = ('CPython', '3.6.7', 'default')

    # Test
    python_collector = PythonFactCollector()
    facts = python_collector.collect()

    # Check
    assert facts['python']['version'] == {
        'major': 3,
        'minor': 6,
        'micro': 7,
        'releaselevel': 'final',
        'serial': 0
    }
    assert facts['python']['version_info'] == [3, 6, 7, 'final', 0]
    assert facts['python']['executable'] == '/usr/bin/python'

# Generated at 2022-06-13 03:17:52.100449
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    
    python_fact_collector = PythonFactCollector()
    actual_facts_collected = python_fact_collector.collect()

    expected_version_info = list(sys.version_info)
    expected_data = {
        'python': {
            'version': {
                'major': sys.version_info[0],
                'minor': sys.version_info[1],
                'micro': sys.version_info[2],
                'releaselevel': sys.version_info[3],
                'serial': sys.version_info[4]
            },
            'version_info': expected_version_info,
            'executable': sys.executable,
            'type': sys.subversion[0],
            'has_sslcontext': HAS_SSLCONTEXT
        }
    }

    assert actual_

# Generated at 2022-06-13 03:17:54.743566
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = PythonFactCollector().collect()
    assert 'python' in python_facts, python_facts
    assert 'version' in python_facts['python'], python_facts['python']

# Generated at 2022-06-13 03:18:02.772218
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    temp = {}
    c = PythonFactCollector()
    result = c.collect(temp)
    python_version = sys.version_info
    assert result['python']['version'] == {'micro': python_version[2],
                                           'major': python_version[0],
                                           'minor': python_version[1],
                                           'releaselevel': python_version[3],
                                           'serial': python_version[4]}
    assert result['python']['version_info'] == list(sys.version_info)
    assert result['python']['executable'] == sys.executable
    assert result['python']['has_sslcontext'] == HAS_SSLCONTEXT


# Generated at 2022-06-13 03:18:11.180761
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pycol = PythonFactCollector()
    result = pycol.collect()
    assert 'python' in result
    assert 'version' in result['python']
    assert result['python']['version']['major'] == sys.version_info[0]
    assert result['python']['version']['minor'] == sys.version_info[1]
    assert result['python']['version']['micro'] == sys.version_info[2]
    assert result['python']['version']['releaselevel'] == sys.version_info[3]
    assert result['python']['version']['serial'] == sys.version_info[4]
    assert 'version_info' in result['python']
    assert result['python']['version_info'] == list(sys.version_info)

# Generated at 2022-06-13 03:18:16.357214
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector()
    facts = pfc.collect()
    assert facts['python']['version']['major'] == sys.version_info[0]
    assert facts['python']['version']['minor'] == sys.version_info[1]
    assert facts['python']['version']['micro'] == sys.version_info[2]
    assert facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert facts['python']['version']['serial'] == sys.version_info[4]
    assert facts['python']['version_info'] == list(sys.version_info)
    assert facts['python']['executable'] == sys.executable
    assert facts['python']['has_sslcontext'] == HAS_SSLCON

# Generated at 2022-06-13 03:18:25.476755
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector()
    python_facts = pfc.collect()
    if sys.version_info[0] >= 3:
        assert python_facts['python']['version'] == {
            'major': 3,
            'minor': 6,
            'micro': 0,
            'releaselevel': 'final',
            'serial': 0
        }
        assert python_facts['python']['version_info'] == [3, 6, 0, 'final', 0]
    else:
        assert python_facts['python']['version'] == {
            'major': 2,
            'minor': 7,
            'micro': 0,
            'releaselevel': 'final',
            'serial': 0
        }

# Generated at 2022-06-13 03:18:29.705886
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = PythonFactCollector().collect()
    assert python_facts['python']['version_info'] == list(sys.version_info)
    assert 'executable' in python_facts['python']
    assert 'has_sslcontext' in python_facts['python']
    assert 'type' in python_facts['python']

# Generated at 2022-06-13 03:18:30.834225
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pf = PythonFactCollector()
    pf.collect()


# Generated at 2022-06-13 03:19:09.874917
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    from ansible.module_utils.facts.collector import PythonFactCollector
    from ansible.module_utils._text import to_bytes
    import ssl
    test_fact_collector = PythonFactCollector()
    result = test_fact_collector.collect()
    assert 'python' in result
    if ssl.OPENSSL_VERSION_INFO[0] >= 1 and ssl.OPENSSL_VERSION_INFO[1] >= 1:
        assert result['python']['has_sslcontext'] == True
    else:
        assert result['python']['has_sslcontext'] == False
    assert 'executable' in result['python']
    assert result['python']['version'] == {'serial': 0, 'micro': 0, 'releaselevel': 'final', 'major': 3, 'minor': 6}
   

# Generated at 2022-06-13 03:19:10.726005
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pyf = PythonFactCollector()
    pyf.collect()

# Generated at 2022-06-13 03:19:21.999953
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Try with no facts
    fact_collector = PythonFactCollector(None)
    assert fact_collector.collect() == {}

    # Try with empty facts
    facts = {}
    fact_collector = PythonFactCollector(None)
    assert fact_collector.collect(collected_facts=facts) == {}

    # Try with some facts
    facts = {'some': 'facts'}
    fact_collector = PythonFactCollector(None)
    assert fact_collector.collect(collected_facts=facts) == {}

    # Try with 'python' fact
    facts = {'python': {'some': 'facts'}}
    fact_collector = PythonFactCollector(None)
    assert fact_collector.collect(collected_facts=facts) == facts

# Generated at 2022-06-13 03:19:31.157889
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
    assert result['python']['has_sslcontext'] == HAS_SSLCONTEXT

    if sys.implementation.name:
        assert result

# Generated at 2022-06-13 03:19:41.544927
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Create a instance of AnsibleModule
    module = AnsibleModule(
        argument_spec = dict()
    )
    # Instantiate a instance of the collector
    instance = PythonFactCollector(module=module)
    # Make sure the class variable _fact_id is a set
    assert isinstance(instance._fact_ids, set), "class variable _fact_ids is not a set"
    # Make sure the value of _fact_id is correct
    assert instance._fact_ids == set(['python']), "value of class variable _fact_ids is incorrect"
    # Make sure the method collect returns a dict
    assert isinstance(instance.collect(), dict), "method collect did not return a dict"

from ansible.module_utils.basic import AnsibleModule
# Instantiate a instance of the AnsibleModule

# Generated at 2022-06-13 03:19:45.873840
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    from ansible.module_utils.facts import collector
    collector.add_collector(PythonFactCollector())
    collected_facts = collector.collect(None, None)
    for key in ('python', 'python.version', 'python.version_info', 'python.executable', 'python.has_sslcontext'):
        assert key in collected_facts
    assert collected_facts['python']['type'] in ('CPython', 'PyPy', 'Jython', None)
    assert isinstance(collected_facts['python']['version'], dict)
    assert isinstance(collected_facts['python']['version_info'], list)
    assert isinstance(collected_facts['python']['executable'], str)
    assert isinstance(collected_facts['python']['has_sslcontext'], bool)
   

# Generated at 2022-06-13 03:19:51.117907
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = PythonFactCollector().collect()
    assert type(python_facts) == dict
    assert 'python' in python_facts
    assert type(python_facts['python']) == dict
    assert type(python_facts['python']['version']) == dict
    assert type(python_facts['python']['version']['releaselevel']) == str
    assert type(python_facts['python']['version']['serial']) == int


# Generated at 2022-06-13 03:19:59.371157
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    collector = PythonFactCollector()

    # Should parse python version, python type and executable
    collected_facts = collector.collect()

    assert 'python' in collected_facts
    assert type(collected_facts['python']) is dict

    assert 'version' in collected_facts['python']
    assert type(collected_facts['python']['version']) is dict

    assert 'major' in collected_facts['python']['version']
    assert type(collected_facts['python']['version']['major']) is int

    assert 'minor' in collected_facts['python']['version']
    assert type(collected_facts['python']['version']['minor']) is int

    assert 'micro' in collected_facts['python']['version']

# Generated at 2022-06-13 03:20:07.314209
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    py_facts = PythonFactCollector().collect()
    assert py_facts['python']['version']['major'] == sys.version_info[0]
    assert py_facts['python']['version']['minor'] == sys.version_info[1]
    assert py_facts['python']['version']['micro'] == sys.version_info[2]
    assert py_facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert py_facts['python']['version']['serial'] == sys.version_info[4]
    assert py_facts['python']['version_info'] == list(sys.version_info)
    assert py_facts['python']['executable'] == sys.executable

# Generated at 2022-06-13 03:20:15.162073
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fc = PythonFactCollector()

    # Test with empty collected_facts
    result = fc.collect(collected_facts={})
    assert result == {'python': {'version': {'major': sys.version_info[0], 'minor': sys.version_info[1], 'micro': sys.version_info[2], 'releaselevel': sys.version_info[3], 'serial': sys.version_info[4]}, 'version_info': list(sys.version_info), 'executable': sys.executable, 'has_sslcontext': hasattr(sys, '_base_executable'), 'type': sys.subversion[0]}}

    # Test with a non empty collected_facts
    # Add a 'python' fact

# Generated at 2022-06-13 03:21:22.565187
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    collector_instance = PythonFactCollector()
    assert isinstance(collector_instance.collect(), dict)

# Generated at 2022-06-13 03:21:30.656058
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    import unittest
    import tempfile

    sys.modules.pop('ansible.module_utils.facts.collector.python', None)

    import ansible.module_utils.facts.collector.python

    class TestPythonFactCollectorCollect(unittest.TestCase):

        def setUp(self):
            ansible.module_utils.facts.collector.python.sys = sys
            self.python_fact_collector = ansible.module_utils.facts.collector.python.PythonFactCollector()

        def test_collect(self):
            import ansible.module_utils.facts.collector

            ansible.module_utils.facts.collector.sys = sys

            import sys
            import ssl

            sys.modules.pop('ssl', None)

            sys.modules['ssl'] = ssl
            sys

# Generated at 2022-06-13 03:21:35.613065
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Create an instance of class PythonFactCollector
    python_fact_collector = PythonFactCollector()

    # Call method collect
    # Note: we cannot predict the value of the facts that method collect
    #       returns, so we will not bother testing this value.
    python_fact_collector.collect()

    # Check if instance variables of class PythonFactCollector
    # are set as expected
    assert len(python_fact_collector._fact_ids) == 1
    assert python_fact_collector._fact_ids == set(['python'])

# Generated at 2022-06-13 03:21:43.007165
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    from ansible.module_utils.facts import collector

    facts_collector = collector.get_collector('python')
    python_facts = facts_collector.collect()

    assert python_facts['python']['version']['major'] == sys.version_info[0]
    assert python_facts['python']['version']['minor'] == sys.version_info[1]
    assert python_facts['python']['version']['micro'] == sys.version_info[2]
    assert python_facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert python_facts['python']['version']['serial'] == sys.version_info[4]
    assert python_facts['python']['version_info'] == list(sys.version_info)
   

# Generated at 2022-06-13 03:21:45.747071
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    py_facts = PythonFactCollector().collect()
    assert 'python' in py_facts
    assert 'version' in py_facts['python']
    assert 'version_info' in py_facts['python']
    assert 'executable' in py_facts['python']
    assert 'type' in py_facts['python']

# Generated at 2022-06-13 03:21:49.564489
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    sut = PythonFactCollector()
    result = sut.collect()
    assert result['python']['version'] == \
        {'major': 2, 'minor': 7, 'micro': 12, 'releaselevel': 'final', 'serial': 0}
    assert result['python']['version_info'] == [2, 7, 12, 'final', 0]
    assert result['python']['executable'] == sys.executable
    assert result['python']['has_sslcontext'] == HAS_SSLCONTEXT

# Generated at 2022-06-13 03:21:50.296306
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    myfact = PythonFactCollector()
    assert isinstance(myfact.collect(), dict)

# Generated at 2022-06-13 03:21:53.584976
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector()
    pfacts = pfc.collect()
    assert len(pfacts) == 1
    assert pfacts['python']['version']['major'] == sys.version_info[0]

# Generated at 2022-06-13 03:22:03.878522
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    temp_class = PythonFactCollector()
    python_dict = temp_class.collect()
    assert 'python' in python_dict
    assert 'version' in python_dict['python']
    assert 'version_info' in python_dict['python']
    assert 'has_sslcontext' in python_dict['python']
    assert 'executable' in python_dict['python']
    assert 'type' in python_dict['python']
    assert 'major' in python_dict['python']['version']
    assert 'minor' in python_dict['python']['version']
    assert 'micro' in python_dict['python']['version']
    assert 'releaselevel' in python_dict['python']['version']
    assert 'serial' in python_dict['python']['version']

# Generated at 2022-06-13 03:22:07.952801
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_collector = PythonFactCollector()
    actual_result = python_collector.collect()
    expected_result = {'python': {'type': 'CPython', 'version': {'releaselevel': 'final', 'minor': 5, 'major': 2, 'micro': 7, 'serial': 0}, 'version_info': [2, 7, 17, 'final', 0], 'executable': '/usr/bin/python', 'has_sslcontext': False}}
    assert actual_result == expected_result