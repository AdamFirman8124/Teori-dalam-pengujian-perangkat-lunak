

# Generated at 2022-06-13 03:12:22.556292
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector()
    pfc._module = AnsibleModule(argument_spec={})
    pfc._collect_platform_facts = Mock(name='_collect_platform_facts')
    facts = pfc.collect()

    assert 'python' in facts
    for key in ('version', 'version_info', 'executable', 'has_sslcontext'):
        assert key in facts['python']
        assert facts['python'][key] is not None

    if hasattr(sys, 'subversion'):
        assert sys.subversion[0] == facts['python']['type']
    elif hasattr(sys, 'implementation'):
        assert sys.implementation.name == facts['python']['type']

# Unit test class

# Generated at 2022-06-13 03:12:38.784736
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    # this is the return value of collect
    module = None
    collected_facts = None

    python_fact_collector = PythonFactCollector()
    expected_result = {
        'python': {
            'type': 'CPython',
            'version_info':
            [3,
             4,
             0,
             'final',
             0],
            'executable':
            '/home/stuvwxy/bin/python34',
            'version': {
                'serial': 0,
                'micro': 0,
                'releaselevel': 'final',
                'minor': 4,
                'major': 3
            },
            'has_sslcontext': True
        }
    }

    result = python_fact_collector.collect(module, collected_facts)
    assert result == expected_result

# Generated at 2022-06-13 03:12:56.188928
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Collect simple facts
    pfc = PythonFactCollector()
    facts = pfc.collect()
    assert isinstance(facts, dict)
    assert 'python' in facts
    assert 'version_info' in facts['python']
    assert isinstance(facts['python']['version_info'], list)
    assert 'version' in facts['python']
    assert 'major' in facts['python']['version']
    assert 'minor' in facts['python']['version']
    assert 'micro' in facts['python']['version']
    assert 'releaselevel' in facts['python']['version']
    assert 'serial' in facts['python']['version']
    assert 'executable' in facts['python']
    if sys.version_info[0] >= 3:
        assert 'type' in facts['python']

# Generated at 2022-06-13 03:13:02.745302
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    collector = PythonFactCollector()
    result = collector.collect()
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

# Generated at 2022-06-13 03:13:05.358449
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector()
    assert pfc.collect()
# end of test_PythonFactCollector_collect()

# Generated at 2022-06-13 03:13:11.102880
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    collector = PythonFactCollector(None)
    result = collector._collect()
    assert(result['python']['version']['major'] > 0)
    assert(result['python']['version']['minor'] >= 0)
    assert(result['python']['version']['micro'] >= 0)
    assert(result['python']['version']['releaselevel'])
    assert(result['python']['version']['serial'] >= 0)
    assert(len(result['python']['version_info']) == 5)
    assert(result['python']['executable'])
    assert('has_sslcontext' in result['python'])


# Generated at 2022-06-13 03:13:16.898515
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = PythonFactCollector({}).collect()
    assert isinstance(python_facts, dict)
    assert 'python' in python_facts
    assert isinstance(python_facts['python'], dict)
    assert 'version' in python_facts['python']
    assert 'version_info' in python_facts['python']
    assert 'executable' in python_facts['python']
    assert 'has_sslcontext' in python_facts['python']
    assert 'type' in python_facts['python']
    assert isinstance(python_facts['python']['version'], dict)
    assert isinstance(python_facts['python']['version_info'], list)
    assert isinstance(python_facts['python']['executable'], unicode)

# Generated at 2022-06-13 03:13:19.724678
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    _x = PythonFactCollector()
    python_facts = _x.collect()
    assert 'python' in python_facts

# Generated at 2022-06-13 03:13:29.025477
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """
    This method will be called automatically during post processing and will
    test if the method collect of the class PythonFactCollector returns
    a dictionary whose keys are version, version_info and executable.
    """
    # Initialize PythonFactCollector object
    fact_collector_obj = PythonFactCollector()

    # Call method collect of PythonFactCollector object
    facts = fact_collector_obj.collect()

    # Assert that the keys of the returned dictionary are 'version',
    # 'version_info', and 'executable'
    assert isinstance(facts, dict)
    assert set(facts) == set(['python'])
    assert isinstance(facts['python'], dict)

# Generated at 2022-06-13 03:13:34.340571
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_infos = PythonFactCollector().collect()
    assert 'python' in python_infos
    assert 'type' in python_infos['python']
    assert 'version' in python_infos['python']
    assert 'version_info' in python_infos['python']
    assert 'executable' in python_infos['python']
    assert 'has_sslcontext' in python_infos['python']

# Generated at 2022-06-13 03:13:46.638797
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fc = PythonFactCollector()
    collected_facts = fc.collect()

    # General check
    assert 'python' in collected_facts
    assert isinstance(collected_facts['python'], dict)

    assert 'version' in collected_facts['python']
    assert isinstance(collected_facts['python']['version'], dict)
    assert 'version_info' in collected_facts['python']
    assert isinstance(collected_facts['python']['version_info'], list)
    assert 'executable' in collected_facts['python']
    assert isinstance(collected_facts['python']['executable'], str)
    assert 'type' in collected_facts['python']

# Generated at 2022-06-13 03:14:00.399855
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    # Test the facts returned by collect()
    pythonfactcollector = PythonFactCollector()
    facts = pythonfactcollector.collect()

    assert 'python' in facts
    python_facts = facts['python']
    assert 'version' in python_facts
    assert 'version_info' in python_facts
    assert 'executable' in python_facts
    assert 'has_sslcontext' in python_facts

    version_facts = python_facts['version']
    for key in ('major', 'minor', 'micro', 'releaselevel', 'serial'):
        assert key in version_facts

    for key in ('major', 'minor', 'micro', 'releaselevel', 'serial'):
        assert version_facts[key] is not None

    assert version_facts['major'] == sys.version_info[0]

# Generated at 2022-06-13 03:14:09.395181
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    py_fc = PythonFactCollector()
    mocker_pfc = lambda method_name: mocker.patch.object(py_fc, method_name)
    mocker_pfc('get_file_content').return_value = None  # disable get_file_content
    mocker_pfc('get_file_lines').return_value = None  # disable get_file_lines
    mocker_pfc('get_mount_size').return_value = None  # disable get_mount_size
    mocker_pfc('get_mount_info').return_value = []  # disable get_mount_info
    mocker_pfc('get_cmd_output').return_value = None  # disable get_cmd_output
    mocker_pfc('get_cmd_input').return_value = None  # disable get_cmd_

# Generated at 2022-06-13 03:14:12.772523
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    import ansible.constants
    ansible.constants.HOST_VARIABLE_NAME = 'hostvars'
    import ansible.module_utils.facts.collector
    import ansible.module_utils.facts.system.python
    ansible.module_utils.facts.collector.BaseFactCollector.__bases__ = (ansible.module_utils.facts.system.python.PythonFactCollector,)
    python_facts = ansible.module_utils.facts.collector.BaseFactCollector().collect()
    assert isinstance(python_facts, dict)
    assert set(['ansible_python']) == set(python_facts.keys())
    assert isinstance(python_facts['ansible_python'], dict)

# Generated at 2022-06-13 03:14:22.861210
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """
    Users may run Ansible in one of three ways:

    1. Using Python virtualenv, via "ansible".
    2. Using Python virtualenv, via "python setup.py test".
    3. Using Python's 'venv' module, via "python -m venv ansible && . ansible/bin/activate && python setup.py test".
    4. Using Python's 'venv' module, via "python3 -m venv ansible && . ansible/bin/activate && python3 setup.py test".

    Scenarios 1 and 2 leads to a virtualenv install, scenario 3 and 4 to a venv install.

    Scenario 1 sets "python.executable" to <virtualenv>/bin/python.
    Scenario 2 sets "python.executable" to <venv>/bin/python.
    """
    fact_collect

# Generated at 2022-06-13 03:14:30.430026
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector()
    facts = fact_collector.collect()
    assert 'python' in facts.keys()
    assert 'version' in facts['python'].keys()
    assert 'version_info' in facts['python'].keys()
    assert 'executable' in facts['python'].keys()
    assert 'has_sslcontext' in facts['python'].keys()
    assert 'type' in facts['python'].keys()
    assert isinstance(facts['python']['version_info'], list)
    assert isinstance(facts['python']['type'], str)

# Generated at 2022-06-13 03:14:36.320255
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    c = PythonFactCollector()
    facts = c.collect()
    assert facts['python']['type'] == 'CPython'
    assert facts['python']['version']['major'] == 3
    assert facts['python']['version']['minor'] == 6
    assert facts['python']['version']['micro'] == 0
    assert facts['python']['version']['releaselevel'] == 'final'
    assert facts['python']['version']['serial'] == 0
    assert facts['python']['version_info'] == list(sys.version_info)
    assert facts['python']['executable'] == sys.executable
    assert facts['python']['has_sslcontext'] == HAS_SSLCONTEXT

# Generated at 2022-06-13 03:14:39.757227
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    collector = PythonFactCollector()

    result = collector.collect()
    assert result['python']['executable'] is not None
    assert result['python']['version_info'] is not None
    assert result['python']['version'] is not None

# Generated at 2022-06-13 03:14:49.796805
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector()
    fact_collector.collect()
    expected_facts = {'python': {
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
    assert fact_collector.collect() == expected_facts


# Generated at 2022-06-13 03:14:55.648569
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """Validate PythonFactCollector().collect() output against a subset of sys module attributes.
    """
    import sys
    python_facts = PythonFactCollector().collect()
    assert python_facts['python']['executable'] == sys.executable
    assert python_facts['python']['has_sslcontext'] == HAS_SSLCONTEXT
    assert python_facts['python']['version']['major'] == sys.version_info[0]
# end of test_PythonFactCollector_collect()

# Generated at 2022-06-13 03:15:06.104849
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    py_fact_collector = PythonFactCollector()
    py_facts = py_fact_collector.collect()

    assert py_facts.get('python') is not None
    assert isinstance(py_facts['python'], dict)
    assert 'version' in py_facts['python']
    assert 'version_info' in py_facts['python']
    assert 'executable' in py_facts['python']
    assert 'has_sslcontext' in py_facts['python']

# Generated at 2022-06-13 03:15:09.042584
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    facts_collector = PythonFactCollector()

    facts = facts_collector.collect()

    assert facts is not None
    assert len(facts) == 1
    assert facts['python'] is not None
    assert len(facts['python']) > 0

# Generated at 2022-06-13 03:15:16.209752
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_collector = PythonFactCollector(None)
    python_result = python_collector.collect()
    assert python_result['python']['version']['major'] == sys.version_info[0]
    assert python_result['python']['version']['minor'] == sys.version_info[1]
    assert python_result['python']['version']['micro'] == sys.version_info[2]
    assert python_result['python']['version']['releaselevel'] == sys.version_info[3]
    assert python_result['python']['version']['serial'] == sys.version_info[4]
    assert python_result['python']['version_info'] == list(sys.version_info)

# Generated at 2022-06-13 03:15:17.434094
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector()
    pfc.collect()

# Generated at 2022-06-13 03:15:21.820568
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    c = PythonFactCollector()
    facts = c.collect()
    assert 'python' in facts
    assert 'version' in facts['python']
    assert 'version_info' in facts['python']
    assert 'executable' in facts['python']
    assert 'has_sslcontext' in facts['python']

# Generated at 2022-06-13 03:15:23.380706
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector()
    assert isinstance(fact_collector.collect(), dict)

# Generated at 2022-06-13 03:15:34.254889
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector()
    facts = pfc.collect()

    assert(facts['python']['version']['major'] == sys.version_info[0])
    assert(facts['python']['version']['minor'] == sys.version_info[1])
    assert(facts['python']['version']['micro'] == sys.version_info[2])
    assert(facts['python']['version']['releaselevel'] == sys.version_info[3])
    assert(facts['python']['version']['serial'] == sys.version_info[4])
    assert(facts['python']['version_info'] == list(sys.version_info))
    assert(facts['python']['executable'] == sys.executable)

# Generated at 2022-06-13 03:15:40.567885
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    # Use a mock importer instead of actual one to simulate Python 3.3
    import mock
    from ansible.module_utils.facts.collector import PythonFactCollector
    pfc = PythonFactCollector()
    import sys
    with mock.patch.object(sys, 'version_info', return_value=(3, 3, 0, 'final', 0)):
        assert('python' in pfc.collect())
        assert(pfc.collect()['python']['version']['major'] == 3)
        assert(pfc.collect()['python']['version']['minor'] == 3)
        assert(pfc.collect()['python']['version']['micro'] == 0)
        assert(pfc.collect()['python']['version']['releaselevel'] == 'final')

# Generated at 2022-06-13 03:15:42.159713
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    p = PythonFactCollector()
    assert isinstance(p.collect(None, None), dict)

# Generated at 2022-06-13 03:15:47.779167
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = PythonFactCollector().collect()
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

# Generated at 2022-06-13 03:16:04.901677
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    c = PythonFactCollector()
    result = c.collect()
    assert result['python']['version']['major'] == sys.version_info[0]
    assert result['python']['version']['minor'] == sys.version_info[1]
    assert result['python']['version']['micro'] == sys.version_info[2]
    assert result['python']['version']['releaselevel'] == sys.version_info[3]
    assert result['python']['version']['serial'] == sys.version_info[4]
    assert result['python']['version_info'] == list(sys.version_info)
    assert result['python']['executable'] == sys.executable
    assert result['python']['has_sslcontext'] == HAS_SSLCONTEXT


# Generated at 2022-06-13 03:16:11.081776
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = PythonFactCollector().collect()
    assert python_facts['python']['version']['major'] == 3
    assert python_facts['python']['version']['minor'] == 7
    test_python_version_info = (3, 7, 2, 'final', 0)
    assert python_facts['python']['version_info'] == list(test_python_version_info)
    # Test executable name
    assert python_facts['python']['executable'].endswith("python")
    # Test type
    assert python_facts['python']['type'] == "CPython"
    assert python_facts['python']['has_sslcontext'] == True

# Generated at 2022-06-13 03:16:19.751502
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact_collector = PythonFactCollector()
    result = python_fact_collector.collect()
    assert 'python' in result
    assert result['python']['version']['major'] == sys.version_info[0]
    assert result['python']['version']['releaselevel'] == sys.version_info[3]
    assert result['python']['version_info'] == list(sys.version_info)
    assert result['python']['executable'] == sys.executable
    assert result['python']['has_sslcontext'] == HAS_SSLCONTEXT
    try:
        assert result['python']['type'] == sys.implementation.name
    except AttributeError:
        pass

# Generated at 2022-06-13 03:16:21.597970
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector()
    fact_collector.collect()


# Generated at 2022-06-13 03:16:27.197446
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    # Check if the method collect of class PythonFactCollector
    # return the expected value
    py_collector = PythonFactCollector()
    collected_facts = {}
    py_collector.collect(collected_facts)
    assert collected_facts['python'] is not None

# Generated at 2022-06-13 03:16:34.031691
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    py_fact_collector = PythonFactCollector()
    module = None
    collected_facts = {}
    python_facts = py_fact_collector.collect(module=module, collected_facts=collected_facts)
    assert python_facts['python']['type'] == 'CPython'
    assert python_facts['python']['executable'] == sys.executable
    assert python_facts['python']['version_info'] == list(sys.version_info)
    assert python_facts['python']['version']['major'] == sys.version_info[0]
    assert python_facts['python']['version']['minor'] == sys.version_info[1]
    assert python_facts['python']['version']['micro'] == sys.version_info[2]
    assert python_facts

# Generated at 2022-06-13 03:16:37.661970
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    c = PythonFactCollector()
    facts = c.collect()

    assert isinstance(facts, dict)
    assert 'python' in facts
    assert isinstance(facts['python'], dict)

    for key in ['version', 'version_info', 'executable', 'type', 'has_sslcontext']:
        assert key in facts['python']


# Generated at 2022-06-13 03:16:44.900540
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    python_facts = PythonFactCollector().collect()

    assert(python_facts['python']['version']['major'] == 3)
    assert(python_facts['python']['version']['minor'] == 7)
    assert(python_facts['python']['version']['micro'] == 3)
    assert(python_facts['python']['version']['releaselevel'] == 'final')
    assert(python_facts['python']['version']['serial'] == 0)
    assert(python_facts['python']['type'] == 'CPython')
    assert(python_facts['python']['has_sslcontext'] == True)

# Generated at 2022-06-13 03:16:46.973957
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Test to collect facts only
    pc = PythonFactCollector()
    result = pc.collect(None, None)
    assert result['python']['version']['major'] == sys.version_info[0]
    assert result['python']['has_sslcontext'] == HAS_SSLCONTEXT

# Generated at 2022-06-13 03:16:52.847472
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = PythonFactCollector().collect()

    assert isinstance(python_facts, dict)
    assert isinstance(python_facts['python'], dict)
    assert isinstance(python_facts['python']['version'], dict)
    assert isinstance(python_facts['python']['version_info'], list)

    assert 'major' in python_facts['python']['version']
    assert 'minor' in python_facts['python']['version']
    assert 'micro' in python_facts['python']['version']
    assert 'releaselevel' in python_facts['python']['version']
    assert 'serial' in python_facts['python']['version']
    assert 'executable' in python_facts['python']
    assert 'has_sslcontext' in python_facts['python']


# Generated at 2022-06-13 03:17:18.383247
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    from ansible.module_utils.facts.collector import collect_subset_facts

    test_collector = PythonFactCollector()

    facts = collect_subset_facts(subset=['python'])
    # Verify major, minor, micro, releaselevel and serial
    assert facts['python']['version']['major'] == sys.version_info[0]
    assert facts['python']['version']['minor'] == sys.version_info[1]
    assert facts['python']['version']['micro'] == sys.version_info[2]
    assert facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert facts['python']['version']['serial'] == sys.version_info[4]
    # Verify version_info

# Generated at 2022-06-13 03:17:24.882102
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector()

    facts = fact_collector.collect()
    assert facts['python']['version'] == {
        'major': sys.version_info[0],
        'minor': sys.version_info[1],
        'micro': sys.version_info[2],
        'releaselevel': sys.version_info[3],
        'serial': sys.version_info[4]
    }
    assert facts['python']['version_info'] == list(sys.version_info)
    assert facts['python']['type'] == 'CPython'
    assert facts['python']['executable'] == sys.executable
    assert facts['python']['has_sslcontext'] == HAS_SSLCONTEXT

# Generated at 2022-06-13 03:17:33.279401
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    module = None
    collected_facts = None
    python_facts = PythonFactCollector().collect(module, collected_facts)
    assert 'python' in python_facts
    assert 'version' in python_facts['python']
    assert 'major' in python_facts['python']['version']
    assert 'minor' in python_facts['python']['version']
    assert 'micro' in python_facts['python']['version']
    assert 'releaselevel' in python_facts['python']['version']
    assert 'serial' in python_facts['python']['version']
    assert 'version_info' in python_facts['python']
    assert 'type' in python_facts['python']
    assert 'executable' in python_facts['python']
    assert 'has_sslcontext' in python_facts['python']

# Generated at 2022-06-13 03:17:35.190779
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pyth = PythonFactCollector()
    collected_facts = {}
    returned_facts = pyth.collect(collected_facts=collected_facts)
    assert returned_facts != None

# Generated at 2022-06-13 03:17:36.439743
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pyf = PythonFactCollector(None, None)
    pyf.collect()

# Generated at 2022-06-13 03:17:37.410597
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector()
    assert isinstance(pfc.collect(), dict)

# Generated at 2022-06-13 03:17:42.599908
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Test for py2.6 stdlib
    sys.implementation = None
    sys.subversion = ['CPython', '2.6.9', '', '', '']
    collector = PythonFactCollector()
    assert collector.collect() == {
        'python': {
            'type': 'CPython',
            'version': {
                'major': 2,
                'minor': 6,
                'micro': 9,
                'releaselevel': 'final',
                'serial': 0
            },
            'version_info': [2, 6, 9, 'final', 0],
            'executable': '/bin/python',
            'has_sslcontext': False
        }
    }

    # Test for py2.7 stdlib
    sys.implementation = None

# Generated at 2022-06-13 03:17:47.771360
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    c = PythonFactCollector()
    result = c.collect()

    assert 'python' in result
    assert 'version' in result['python']
    assert 'version_info' in result['python']
    assert 'executable' in result['python']
    assert 'has_sslcontext' in result['python']

# Generated at 2022-06-13 03:17:48.268049
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pass

# Generated at 2022-06-13 03:17:56.070475
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    collector = PythonFactCollector()
    facts_dict = collector.collect()

    assert 'python' in facts_dict
    assert isinstance(facts_dict.get('python'), dict)
    assert facts_dict.get('python').get('type') is not None
    assert isinstance(facts_dict.get('python').get('version'), dict)
    assert isinstance(facts_dict.get('python').get('version_info'), list)
    assert facts_dict.get('python').get('executable') is not None
    assert isinstance(facts_dict.get('python').get('has_sslcontext'), bool)

# Generated at 2022-06-13 03:18:20.056936
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pf = PythonFactCollector()
    assert pf.collect() == {
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

# Generated at 2022-06-13 03:18:23.064668
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    c = PythonFactCollector()

    facts = c.collect()
    assert isinstance(facts, dict)
    assert isinstance(facts['python'], dict)


if __name__ == '__main__':
    # Unit test
    test_PythonFactCollector_collect()

# Generated at 2022-06-13 03:18:31.060872
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pc = PythonFactCollector()
    facts = pc.collect()

    assert type(facts) is dict, "Test expecting 'dict' type, got: %s" % type(facts)
    assert 'python' in facts, "Test expecting 'python' key in 'dict' type, got: %s" % facts
    assert 'version' in facts['python'], "Test expecting 'version' key in 'dict' type, got: %s" % facts['python']
    assert 'version_info' in facts['python'], "Test expecting 'version_info' key in 'dict' type, got: %s" % facts['python']
    assert 'executable' in facts['python'], "Test expecting 'executable' key in 'dict' type, got: %s" % facts['python']

# Generated at 2022-06-13 03:18:32.547158
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    collector = PythonFactCollector()
    python_facts = collector.collect_once()
    assert python_facts is not None

# Generated at 2022-06-13 03:18:33.401638
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    PythonFactCollector.collect()

# Generated at 2022-06-13 03:18:40.704545
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector()
    actual_output = fact_collector.collect()

    expected_output = {
        'python': {'version': {'major': sys.version_info[0], 'minor': sys.version_info[1], 'micro': sys.version_info[2],
                               'releaselevel': sys.version_info[3], 'serial': sys.version_info[4]},
                   'version_info': list(sys.version_info), 'executable': sys.executable,
                   'has_sslcontext': HAS_SSLCONTEXT, 'type': sys.implementation.name}}

    assert actual_output == expected_output

# Generated at 2022-06-13 03:18:45.694138
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    collector = PythonFactCollector()
    result = collector.collect()
    assert result == {
        'python': {
            'version': {
                'major': 2,
                'minor': 7,
                'micro': 12,
                'releaselevel': 'final',
                'serial': 0
            },
            'version_info': [2, 7, 12, 'final', 0],
            'executable': '/usr/bin/python',
            'has_sslcontext': True
        }
    }

# Generated at 2022-06-13 03:18:50.180688
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pci = PythonFactCollector()
    result = pci.collect()
    assert result == {'python': 
        {
            'version': {
                'major': 3,
                'minor': 7,
                'micro': 0,
                'releaselevel': 'final',
                'serial': 0
            }, 
            'version_info': [3, 7, 0, 'final', 0], 
            'executable': '/usr/local/bin/python3', 
            'has_sslcontext': True, 
            'type': 'CPython'
        } 
    }

# Generated at 2022-06-13 03:18:52.035706
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_collector = PythonFactCollector()
    assert python_collector.collect()

# Generated at 2022-06-13 03:18:58.972771
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector()
    pfc._module = mock.Mock()
    pfc._module.params = {}

    actual = pfc.collect()
    assert actual == {'python': {'has_sslcontext': True,
                                 'executable': sys.executable,
                                 'version': {'major': 3,
                                             'minor': 6,
                                             'micro': 9,
                                             'releaselevel': 'final',
                                             'serial': 0},
                                 'type': 'CPython',
                                 'version_info': [3, 6, 9, 'final', 0]}}

# Generated at 2022-06-13 03:19:43.834050
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

# Generated at 2022-06-13 03:19:53.649667
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    '''
    Test for python specific facts
    :return:
    '''
    print('Testing method collect in class PythonFactCollector')
    from ansible.module_utils.facts.collectors.python import PythonFactCollector
    pfc = PythonFactCollector()
    all_facts = pfc.collect()
    print(all_facts)
    assert all_facts['python']['version']['major'] == sys.version_info[0]
    assert all_facts['python']['version']['minor'] == sys.version_info[1]
    assert all_facts['python']['version']['micro'] == sys.version_info[2]
    assert all_facts['python']['version']['releaselevel'] == sys.version_info[3]

# Generated at 2022-06-13 03:20:03.332692
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    obj = PythonFactCollector()

    result = obj.collect(module=None, collected_facts=None)

    assert result['python']['version']['major'] == 3
    assert result['python']['version']['minor'] == 5
    assert result['python']['version']['micro'] == 2
    assert result['python']['version']['releaselevel'] == 'final'
    assert result['python']['version']['serial'] == 0
    assert result['python']['version_info'][0] == 3
    assert result['python']['version_info'][1] == 5
    assert result['python']['version_info'][2] == 2
    assert result['python']['version_info'][3] == 'final'

# Generated at 2022-06-13 03:20:04.919730
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector()
    fact_collector.collect()


# Generated at 2022-06-13 03:20:11.371047
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pc = PythonFactCollector()

    # Get the facts
    facts = pc.collect(module=None, collected_facts=None)

    # Assert that the facts are correct type
    assert type(facts) is dict

    # Assert that fact 'python' is present
    assert 'python' in facts

    # Assert that fact 'python' is of correct type
    assert type(facts['python']) is dict

    # Assert that 'python' has key 'version'
    assert 'version' in facts['python']

    # Assert that 'version' is of correct type
    assert type(facts['python']['version']) is dict

    # Assert that 'version' has key 'major'
    assert 'major' in facts['python']['version']

    # Assert that 'version' has key 'minor'

# Generated at 2022-06-13 03:20:18.078681
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    # Create object of class PythonFactCollector and get python facts
    python_facts = PythonFactCollector().collect()

    # Test if python facts are collected
    assert python_facts['python']['version']['major'] == sys.version_info[0]
    assert python_facts['python']['version']['minor'] == sys.version_info[1]
    assert python_facts['python']['version']['micro'] == sys.version_info[2]
    assert python_facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert python_facts['python']['version']['serial'] == sys.version_info[4]
    assert python_facts['python']['version_info'] == list(sys.version_info)

# Generated at 2022-06-13 03:20:27.664023
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector.python import PythonFactCollector
    from ansible.module_utils.facts.processor import FactsProcessor
    from ansible.module_utils.facts.processor.python import PythonProcessor
    facts_processor = FactsProcessor()
    BaseFactCollector._fact_processors[None] = facts_processor
    collector_name = 'python'
    collector = PythonFactCollector()
    BaseFactCollector._fact_collectors[collector_name] = collector
    collections = BaseFactCollector.collect(collector)
    assert collections[collector_name]['python']['version']['major'] == 3

# Generated at 2022-06-13 03:20:37.134654
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    collector = PythonFactCollector()
    facts = collector.collect()

    assert isinstance(facts, dict)
    assert isinstance(facts['python'], dict)
    assert isinstance(facts['python']['version_info'], list)
    assert isinstance(facts['python']['version'], dict)
    assert isinstance(facts['python']['version']['releaselevel'], str)
    assert isinstance(facts['python']['version']['serial'], int)
    assert isinstance(facts['python']['has_sslcontext'], bool)

    if facts['python']['type'] is not None:
        assert isinstance(facts['python']['type'], str)

# Generated at 2022-06-13 03:20:39.531841
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    collector = PythonFactCollector()
    facts = collector.collect()
    assert 'python' in facts
    assert 'version' in facts['python']
    assert 'version_info' in facts['python']

# Generated at 2022-06-13 03:20:46.519084
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    def sys_version_info(*args):
        return (2, 6, 9, 'final', 0)

    def sys_executable(*args):
        return 'python'

    fact_collector = PythonFactCollector()
    fact_collector.collect = sys_version_info
    fact_collector.collect = sys_executable
    result = fact_collector.collect()
    assert result == {'python':
                      {'version':
                       {'major': 2, 'minor': 6, 'micro': 9, 'releaselevel': 'final', 'serial': 0},
                       'version_info': [2, 6, 9, 'final', 0],
                       'executable': 'python',
                       'has_sslcontext': False}
                     }

# Generated at 2022-06-13 03:22:08.074047
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """
    Test the collect method for PythonFactCollector.
    """
    # creates the fact collector
    fact = PythonFactCollector()
    # creates a fact data structure
    fact_data = {}
    # sets the python facts
    python_facts = fact.collect(collected_facts=fact_data)
    # retrieves the python version and version_info
    python_version = python_facts['python']['version']
    python_version_info = python_facts['python']['version_info']
    # creates the expected result data

# Generated at 2022-06-13 03:22:10.508363
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact_collector = PythonFactCollector()
    result = python_fact_collector.collect()
    assert result['python']

# Generated at 2022-06-13 03:22:17.482326
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """Test that collect returns a dict with versions from sys.version_info."""
    pf = PythonFactCollector()
    svi = sys.version_info
    print(svi)
    expected = {
        'version': {
            'major': svi[0],
            'minor': svi[1],
            'micro': svi[2],
            'releaselevel': svi[3],
            'serial': svi[4]
        },
        'version_info': list(svi),
        'executable': sys.executable,
        'has_sslcontext': HAS_SSLCONTEXT
    }
    print(expected)