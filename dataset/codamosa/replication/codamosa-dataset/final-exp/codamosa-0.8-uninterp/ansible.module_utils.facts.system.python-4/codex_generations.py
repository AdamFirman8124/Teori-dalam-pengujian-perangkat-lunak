

# Generated at 2022-06-13 03:12:18.389469
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector()
    fact_collector.collect()

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


# Generated at 2022-06-13 03:12:37.248672
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """
    mock the modules called by PythonFactCollector.collect
    """
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts import collector
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts import ansible_collector

    mock_module = object()
    mock_collector = object()
    mock_modules = { 'ansible.module_utils.facts.ansible_collector': ansible_collector }
    import sys
    sys.version_info = (2, 7, 5, 'final', 0)
    sys.subversion = ('CPython', '2.7.5', '', '', '')
    sys.executable = '/tmp/test_python_path'


# Generated at 2022-06-13 03:12:39.512070
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pycollector = PythonFactCollector()
    result = pycollector.collect()
    assert 'python' in result
    assert 'version' in result['python']
    assert 'type' in result['python']
    assert 'version_info' in result['python']
    assert 'executable' in result['python']

# Generated at 2022-06-13 03:12:45.039496
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    col = PythonFactCollector()
    assert col.collect() == {'python': {'version': {'micro': 1,
                                                    'major': 3,
                                                    'minor': 5,
                                                    'releaselevel': 'final',
                                                    'serial': 0},
                                       'executable': '/usr/bin/python3.5',
                                       'has_sslcontext': True,
                                       'type': 'CPython',
                                       'version_info': [3, 5, 1, 'final', 0]}}


# Generated at 2022-06-13 03:12:48.895601
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector()
    fact_collector.collect()



# Generated at 2022-06-13 03:12:54.792446
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact = PythonFactCollector()
    assert python_fact.collect() == {'python': {'executable': '/usr/bin/python2.7', 'has_sslcontext': True, 'type': 'CPython', 'version': {'major': 2, 'micro': 7, 'minor': 7, 'releaselevel': 'final', 'serial': 0}, 'version_info': [2, 7, 7, 'final', 0]}}



# Generated at 2022-06-13 03:12:58.610850
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector()
    facts = pfc.collect()
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
    assert 'type' in python_facts
    assert 'has_sslcontext' in python_facts

# Generated at 2022-06-13 03:13:02.745923
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # TODO need a better test here, but this is a start
    from ansible.module_utils.facts.collector import Collectors
    collectors = Collectors()
    python_collector = collectors.get_collector('python')
    facts = python_collector.collect()
    assert 'python' in facts

# vim: set et ts=4 sw=4 sts=4

# Generated at 2022-06-13 03:13:07.307443
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    c = PythonFactCollector()

    def test_results(res, ansible_facts):
        assert res == ansible_facts
    c.collect(collected_facts={}, test_results=test_results)

# Generated at 2022-06-13 03:13:08.066231
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector()
    fact_collector.collect()


# Generated at 2022-06-13 03:13:12.398850
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    test_collector = PythonFactCollector()
    assert 'python' in test_collector.collect()

# Generated at 2022-06-13 03:13:20.883503
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Unit test for method collect of class PythonFactCollector
    # This is a basic smoke test. It checks that the assert
    # has no side effects. It would be great if someone wrote
    # a more complete test.
    c = PythonFactCollector()
    facts = c.collect()
    assert facts['python'] == {
      'executable': '/usr/bin/python2.7',
      'has_sslcontext': False,
      'version': {
        'releaselevel': 'final',
        'major': 2,
        'minor': 7,
        'micro': 9,
        'serial': 0
      },
      'type': 'CPython',
      'version_info': [
        2,
        7,
        9,
        'final',
        0
      ]
    }

# Generated at 2022-06-13 03:13:27.871620
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector()
    python_facts = pfc.collect()
    assert 'python' in python_facts
    for item in ['version', 'version_info', 'executable']: # and eventually more
        assert item in python_facts['python']
    assert isinstance(python_facts['python']['version'], dict)
    assert isinstance(python_facts['python']['version_info'], list)
    assert isinstance(python_facts['python']['has_sslcontext'], bool)
    assert python_facts['python']['executable'] == sys.executable

# Generated at 2022-06-13 03:13:33.493440
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector.python_facts import PythonFactCollector
    pfc = PythonFactCollector()
    # Check if PythonFactCollector is a subclass of BaseFactCollector
    assert issubclass(PythonFactCollector, BaseFactCollector)
    # Test if the collect method really works
    assert isinstance(pfc.collect(), dict)

# Generated at 2022-06-13 03:13:35.908927
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Create a new instance of class PythonFactCollector
    fact_collector = PythonFactCollector()
    # Execute method collect and assert if it returns a dictionary
    assert isinstance(fact_collector.collect(), dict)

# Generated at 2022-06-13 03:13:38.135271
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector()
    fact_collector.collect({}, {})

# Generated at 2022-06-13 03:13:43.056972
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    mock_module = type('module', (object,), {'exit_json': lambda self, **kwargs: None})
    python_fact = PythonFactCollector()
    ret = python_fact.collect(module=mock_module)
    assert ret['python']
    assert len(ret['python'].keys()) == 5
    assert isinstance(ret['python']['version'], dict)
    assert len(ret['python']['version'].keys()) == 5
    assert isinstance(ret['python']['version_info'], list)
    assert len(ret['python']['version_info']) == 5
    assert ret['python']['has_sslcontext'] == HAS_SSLCONTEXT
    assert ret['python']['executable'] == sys.executable

# Generated at 2022-06-13 03:13:49.772168
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Test a standard install of python
    python_fact = PythonFactCollector()
    result = python_fact.collect()
    assert result == {'python': {'version': {'major': 2, 'minor': 7, 'micro': 15, 'releaselevel': 'final', 'serial': 0}, 'executable': '/usr/bin/python', 'has_sslcontext': True, 'type': 'CPython', 'version_info': [2, 7, 15, 'final', 0]}}

    # Test a virtualenv python
    python_fact = PythonFactCollector()
    result = python_fact.collect()

# Generated at 2022-06-13 03:13:59.131393
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    import pytest

    python_facts = {
        'python': {
            'version': {'major': 3, 'minor': 5, 'micro': 1, 'releaselevel': 'final', 'serial': 0},
            'version_info': [3, 5, 1, 'final', 0],
            'executable': '/usr/bin/python3',
            'type': 'CPython',
            'has_sslcontext': True
        }
    }

    collector = PythonFactCollector()
    facts = collector.collect()

    # version_info is a list, so we need to compare one element at the time
    for version in python_facts['python']['version_info']:
        assert version == facts['python']['version_info'][python_facts['python']['version_info'].index(version)]


# Generated at 2022-06-13 03:14:08.777860
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    collector = PythonFactCollector()
    result = collector.collect()

    assert isinstance(result, dict)
    assert result['python']['executable'] == sys.executable
    assert result['python']['has_sslcontext'] == HAS_SSLCONTEXT
    assert result['python']['version'] == {
        'major': sys.version_info[0],
        'minor': sys.version_info[1],
        'micro': sys.version_info[2],
        'releaselevel': sys.version_info[3],
        'serial': sys.version_info[4],
    }
    assert result['python']['version_info'] == list(sys.version_info)


# Generated at 2022-06-13 03:14:22.861962
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    vinfo = list(sys.version_info)
    exe = sys.executable

    try:
        subversion = sys.subversion[0]
    except AttributeError:
        try:
            subversion = sys.implementation.name
        except AttributeError:
            subversion = None

    pfc = PythonFactCollector('null')
    result = pfc.collect()

# Generated at 2022-06-13 03:14:30.690828
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = PythonFactCollector().collect()

    assert python_facts == {
        "python": {
            "version": {
                'major': sys.version_info[0],
                'minor': sys.version_info[1],
                'micro': sys.version_info[2],
                'releaselevel': sys.version_info[3],
                'serial': sys.version_info[4]
            },
            'version_info': list(sys.version_info),
            'executable': sys.executable,
            'has_sslcontext': HAS_SSLCONTEXT,
            'type': 'cpython'
        }
    }

# Generated at 2022-06-13 03:14:35.402313
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    # Create an instance of the PythonFactCollector class
    pfc = PythonFactCollector()

    # get the python facts
    python_facts = pfc.collect()

    # assert that the version info is a list
    assert(isinstance(python_facts['python']['version_info'], list))

# Generated at 2022-06-13 03:14:43.907446
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector()
    # Test python 2.6
    sys.version_info = (2, 6, 6, 'final', 0)
    sys.executable = '/usr/bin/python'
    sys.subversion = ['CPython', '93799']
    # pylint: disable=protected-access
    pfc._fact_ids = set()
    # pylint: enable=protected-access
    # pylint: disable=assigning-non-slot

# Generated at 2022-06-13 03:14:54.704391
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """
    Testing PythonFactCollector.collect
    """
    # Initialize
    c = PythonFactCollector()
    pf = c.collect(module=None, collected_facts=None)
    # Verify
    assert pf['python']['version']['major'] == sys.version_info[0]
    assert pf['python']['version']['minor'] == sys.version_info[1]
    assert pf['python']['version']['micro'] == sys.version_info[2]
    assert pf['python']['version']['releaselevel'] == sys.version_info[3]
    assert pf['python']['version']['serial'] == sys.version_info[4]

# Generated at 2022-06-13 03:15:00.892694
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """
    Method to test the collect method of PythonFactCollector
    """
    import sys

    fc = PythonFactCollector()
    fd = fc.collect()

    assert list(fd.keys()) == ['python']
    assert list(fd['python'].keys()) == ['version', 'version_info',
                                         'executable', 'has_sslcontext', 'type']
    assert list(fd['python']['version'].keys()) == ['major', 'minor', 'micro',
                                                    'releaselevel', 'serial']
    assert fd['python']['version_info'] == list(sys.version_info)
    assert fd['python']['executable'] == sys.executable
    assert fd['python']['has_sslcontext'] == HAS_SSLCONTEXT

# Generated at 2022-06-13 03:15:02.727997
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fcol = PythonFactCollector()
    fdict = fcol.collect()
    assert fdict['python']['version']['major'] == 2
    assert fdict['python']['version']['minor'] >= 7
    assert fdict['python']['version_info'] == [2, 7, 13, 'final', 0]

# Generated at 2022-06-13 03:15:07.974899
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """
        :parameter module: The ansible module object
        :parameter collected_facts: Ansible facts
        :return: python facts
    """
    py_fact_collector = PythonFactCollector()
    python_facts = py_fact_collector.collect(collected_facts=None)
    print(python_facts)
    print(type(python_facts))

if __name__ == '__main__':
	test_PythonFactCollector_collect()

# Generated at 2022-06-13 03:15:15.868462
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    from ansible.module_utils.facts import ServerResponses
    from ansible.module_utils.facts.collector.python import PythonFactCollector

    response = ServerResponses()
    python_collector = PythonFactCollector()
    collected_facts = {}
    python_collector.collect(collected_facts)

    assert ('python' in collected_facts)

    # Make sure collection was successfull
    assert ('type' in collected_facts['python'])
    assert ('version' in collected_facts['python'])
    assert ('executable' in collected_facts['python'])

    # Make sure that the version is not None
    assert(collected_facts['python']['version']['major'] is not None)
    assert(collected_facts['python']['version']['minor'] is not None)

# Generated at 2022-06-13 03:15:24.654555
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact_collector = PythonFactCollector()

    # pylint: disable=protected-access
    result = python_fact_collector.collect()

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

# Generated at 2022-06-13 03:15:46.794477
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    '''
    Test the method PythonFactCollector.collect of the class
    PythonFactCollector.
    '''

    pfc = PythonFactCollector()

    # Test the collect method
    python_facts = pfc.collect()

    assert python_facts['python']['executable'] == sys.executable
    assert python_facts['python']['version']['major'] == sys.version_info[0]
    assert python_facts['python']['version']['minor'] == sys.version_info[1]
    assert python_facts['python']['version']['micro'] == sys.version_info[2]
    assert python_facts['python']['version']['releaselevel'] == sys.version_info[3]

# Generated at 2022-06-13 03:15:49.893310
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = PythonFactCollector().collect()
    assert(python_facts['python']['version']['major'] == sys.version_info[0] )

# Generated at 2022-06-13 03:15:56.503140
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # In this test we only verify that collect produces a valid structure.
    # We do not check that the values are correct, since that's not the goal of this test.
    python_fact_collector = PythonFactCollector()
    facts = python_fact_collector.collect()

    assert 'python' in facts
    assert 'version' in facts['python']
    assert 'version_info' in facts['python']
    assert 'executable' in facts['python']
    assert 'has_sslcontext' in facts['python']
    assert 'type' in facts['python']

# Generated at 2022-06-13 03:16:06.341066
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """Unit test for PythonFactCollector.collect"""
    import ansible.module_utils.facts.collector.python

    py_collector = ansible.module_utils.facts.collector.python.PythonFactCollector()
    module = None
    collected_facts = None

    # Check if method collect returns the expected dictionary
    py_facts = py_collector.collect(module, collected_facts)

# Generated at 2022-06-13 03:16:17.851175
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    import sys
    from ansible.module_utils.facts.collector import FactsCollector
    from ansible.module_utils.facts import get_collector_instance
    from ansible.module_utils.facts.collector.python import PythonFactCollector
    facts_collector = FactsCollector()
    python_fact_collector = PythonFactCollector(facts_collector, {})
    result = python_fact_collector.collect()
    assert result['python']['version']['major'] == sys.version_info[0]
    assert result['python']['version']['minor'] == sys.version_info[1]
    assert result['python']['version']['micro'] == sys.version_info[2]
    assert result['python']['version']['releaselevel'] == sys.version_

# Generated at 2022-06-13 03:16:25.910072
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fc = PythonFactCollector()
    collected_facts = {}
    collected_facts['ansible_python_version'] = {
        'major': sys.version_info[0],
        'minor': sys.version_info[1],
        'micro': sys.version_info[2],
        'releaselevel': sys.version_info[3],
        'serial': sys.version_info[4]
    }
    collected_facts['ansible_python_version_info'] = list(sys.version_info)
    collected_facts['ansible_python_executable'] = sys.executable

# Generated at 2022-06-13 03:16:32.034870
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector()
    collected_facts = fact_collector.collect()
    python_facts = collected_facts['ansible_local']['python']
    assert python_facts['version_info'] == list(sys.version_info), "version_info is not correct. Check PythonFactCollector.collect method"
    # test if major and micro version match
    assert python_facts['version']['major'] == sys.version_info[0], "major version is not correct. Check PythonFactCollector.collect method"
    assert python_facts['version']['micro'] == sys.version_info[2], "micro version is not correct. Check PythonFactCollector.collect method"
    # test executable

# Generated at 2022-06-13 03:16:33.086112
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # basic test
    x = PythonFactCollector()
    x.collect()

# Generated at 2022-06-13 03:16:37.309028
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    from ansible.module_utils.facts.collector import get_collector_instance
    obj = get_collector_instance("PythonFactCollector")
    obj.collect()
    assert obj.facts['python']
    assert 'has_sslcontext' in obj.facts['python'].keys()
    assert 'version' in obj.facts['python']['version'].keys()
    assert 'type' in obj.facts['python'].keys()

# Generated at 2022-06-13 03:16:41.258842
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    module_mock = {}
    fact_collector = PythonFactCollector()

    fact_collector.collect(module_mock)

# Generated at 2022-06-13 03:16:59.669362
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_collector = PythonFactCollector()
    facts = python_collector.collect()
    assert facts['python']['version']['major'] == sys.version_info[0]
    assert facts['python']['version']['minor'] == sys.version_info[1]
    assert facts['python']['version']['micro'] == sys.version_info[2]
    assert facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert facts['python']['version']['serial'] == sys.version_info[4]
    assert facts['python']['version_info'] == list(sys.version_info)
    assert facts['python']['executable'] == sys.executable
    assert facts['python']['has_sslcontext'] == HAS

# Generated at 2022-06-13 03:17:01.323181
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector()
    result = pfc.collect()
    assert isinstance(result, dict)


# Generated at 2022-06-13 03:17:07.100898
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact_collector = PythonFactCollector()
    data = python_fact_collector.collect()
    assert data['python']['type'] == 'CPython'
    assert data['python']['version']['major'] == 3
    assert data['python']['version']['minor'] == 5
    assert data['python']['executable'].endswith('/python3')

# Generated at 2022-06-13 03:17:16.158027
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    py_fc = PythonFactCollector()
    result = py_fc.collect()
    assert type(result) == dict
    assert result.has_key('python')
    assert result['python']['version']['major'] == 3
    assert result['python']['version']['minor'] == 5
    assert result['python']['version']['micro'] == 0
    assert result['python']['version']['releaselevel'] == 'final'
    assert result['python']['version']['serial'] == 0
    assert result['python']['version_info'] == [3, 5, 0, 'final', 0]
    assert result['python']['executable'] == '/usr/bin/python'
    assert result['python']['has_sslcontext'] == True

# Generated at 2022-06-13 03:17:23.860122
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = PythonFactCollector().collect()
    
    assert type(python_facts) is dict
    assert python_facts.get('python') is not None
    assert type(python_facts.get('python')) is dict
    assert python_facts.get('python').get('type') is not None
    assert type(python_facts.get('python').get('type')) is str
    assert python_facts.get('python').get('version') is not None
    assert type(python_facts.get('python').get('version')) is dict
    assert python_facts.get('python').get('version').get('major') is not None
    assert type(python_facts.get('python').get('version').get('major')) is int

# Generated at 2022-06-13 03:17:32.945883
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
  import tempfile
  from ansible.module_utils.facts import FactsCollector
  from ansible.module_utils.facts import DefaultCollectors

  # Test with all python version
  for version in ('2.6', '2.7', '3.1', '3.2', '3.3', '3.4'):
    fd, path = tempfile.mkstemp()
    f = os.fdopen(fd, 'w')
    f.write("#!/usr/bin/env python%s\nimport sys\nprint(sys.version_info)" % version)
    f.close()
    os.chmod(path, 0o700)

    # Mock module_utils.facts.collectors to load collectos from PythonFactCollector

# Generated at 2022-06-13 03:17:39.598880
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_obj = PythonFactCollector()
    python_facts = python_obj.collect()
    assert 'python' in python_facts, "Failed to create python fact"
    assert 'type' in python_facts['python'], "Failed to create python fact type"
    assert 'version' in python_facts['python'], "Failed to create python fact version"
    assert 'version_info' in python_facts['python'], "Failed to create python fact version_info"
    assert 'executable' in python_facts['python'], "Failed to create python fact executable"
    assert 'has_sslcontext' in python_facts['python'], "Failed to create python fact has_sslcontext"
    assert 'major' in python_facts['python']['version'], "Failed to create python fact version major"

# Generated at 2022-06-13 03:17:49.403238
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python1 = PythonFactCollector()
    python_facts = python1.collect()
    assert python_facts == {u'python': {u'version_info': [2, 7, 12, u'final', 0], u'version': {u'major': 2, u'serial': 0, u'micro': 12, u'minor': 7, u'releaselevel': u'final'}, u'type': u'CPython', u'executable': u'/usr/bin/python', u'has_sslcontext': True}}
    assert python_facts['python']['version'] == {u'major': 2, u'serial': 0, u'micro': 12, u'minor': 7, u'releaselevel': u'final'}

# Generated at 2022-06-13 03:18:00.252813
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector()
    python_facts = pfc.collect()

    assert python_facts['python']['version']['major'] == sys.version_info[0]
    assert python_facts['python']['version']['minor'] == sys.version_info[1]
    assert python_facts['python']['version']['micro'] == sys.version_info[2]
    assert python_facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert python_facts['python']['version']['serial'] == sys.version_info[4]
    assert python_facts['python']['version_info'] == list(sys.version_info)
    assert python_facts['python']['executable'] == sys.executable
    assert python

# Generated at 2022-06-13 03:18:09.869133
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Get a basic fact collection instance
    f = PythonFactCollector()
    assert isinstance(f, BaseFactCollector)
    assert isinstance(f, PythonFactCollector)

    # Get the collection
    result = f.collect()
    assert isinstance(result, dict)
    assert 'python' in result
    assert isinstance(result['python'], dict)
    assert 'version' in result['python']
    assert isinstance(result['python']['version'], dict)
    assert 'major' in result['python']['version']
    assert isinstance(result['python']['version']['major'], int)
    assert 'minor' in result['python']['version']
    assert isinstance(result['python']['version']['minor'], int)

# Generated at 2022-06-13 03:18:30.188824
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector()

    python_facts = pfc.collect()
    assert 'python' in python_facts
    assert 'version' in python_facts['python']
    assert 'version_info' in python_facts['python']
    assert 'executable' in python_facts['python']
    assert 'type' in python_facts['python']

# Generated at 2022-06-13 03:18:38.930667
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # mock the sys module
    sys = MockSysModule()
    sys.version_info = MockVersionInfo(0, 0, 0, 'final', 0)
    sys.executable = "/path/to/executable"
    sys.version = "x.x.x"
    sys.implementation = MockImplementation(name='CPython')

    # create the module_utils object
    python_mod_utils = PythonFactCollector(None, None)

    # call the collect method
    results = python_mod_utils.collect(None, None)

# Generated at 2022-06-13 03:18:44.156748
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    facts_collector = PythonFactCollector()
    facts = facts_collector.collect()
    assert 'python' in facts
    assert isinstance(facts.get('python'), dict)
    assert 'version_info' in facts['python']
    assert isinstance(facts['python']['version_info'], list)
    assert len(facts['python']['version_info']) == 5
    assert 'executable' in facts['python']
    assert 'has_sslcontext' in facts['python']
    assert 'version' in facts['python']

# Generated at 2022-06-13 03:18:50.595405
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector()
    result = pfc.collect()
    assert result['python']['version']['major'] == sys.version_info[0]
    assert result['python']['version']['minor'] == sys.version_info[1]
    assert result['python']['version']['micro'] == sys.version_info[2]
    assert result['python']['version']['releaselevel'] == sys.version_info[3]
    assert result['python']['version']['serial'] == sys.version_info[4]
    assert result['python']['version_info'] == list(sys.version_info)
    assert result['python']['executable'] == sys.executable
    assert result['python']['has_sslcontext'] == HAS_SSLCON

# Generated at 2022-06-13 03:18:52.754414
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    py_fact_collector = PythonFactCollector()
    fact_list = py_fact_collector.collect()
    assert fact_list is not None

# Generated at 2022-06-13 03:18:59.401456
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    expected = {'python': {
        'executable': sys.executable,
        'version': {
            'major': sys.version_info[0],
            'micro': sys.version_info[2],
            'minor': sys.version_info[1],
            'releaselevel': sys.version_info[3],
            'serial': sys.version_info[4]
        },
        'version_info': list(sys.version_info),
        'type': 'CPython',
        'has_sslcontext': HAS_SSLCONTEXT
    }}

    actual = PythonFactCollector().collect()

    assert expected == actual

# Generated at 2022-06-13 03:19:04.488206
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fc = PythonFactCollector()
    res = fc.collect()
    assert isinstance(res, dict)
    assert 'python' in res
    assert 'version' in res['python']
    assert 'version_info' in res['python']
    assert 'executable' in res['python']
    assert 'type' in res['python']

# Generated at 2022-06-13 03:19:10.529975
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    collector = PythonFactCollector()
    facts = collector.collect()
    assert 'python' in facts
    assert 'version' in facts['python']
    assert 'major' in facts['python']['version']
    assert 'minor' in facts['python']['version']
    assert 'micro' in facts['python']['version']
    assert 'releaselevel' in facts['python']['version']
    assert 'serial' in facts['python']['version']
    assert 'version_info' in facts['python']
    assert 'executable' in facts['python']
    assert 'type' in facts['python']
    assert 'has_sslcontext' in facts['python']

# Generated at 2022-06-13 03:19:15.225543
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    module_name = 'unit_test_ansible_module'
    module_args = {}
    python_fact_collector = PythonFactCollector('unit_test', module_name, module_args)
    python_facts = python_fact_collector.collect()
    assert len(python_facts.keys()) == 1
    assert 'python' in python_facts
    # Check for python version
    assert 'version' in python_facts['python']
    assert 'major' in python_facts['python']['version']
    assert 'minor' in python_facts['python']['version']
    assert 'micro' in python_facts['python']['version']
    assert 'releaselevel' in python_facts['python']['version']
    assert 'serial' in python_facts['python']['version']
    # Check for python

# Generated at 2022-06-13 03:19:18.655120
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    py_info = PythonFactCollector().collect()
    assert py_info['python']['executable'] == sys.executable


# Generated at 2022-06-13 03:19:51.849585
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_collector = PythonFactCollector()
    python_collector.collect()


# Generated at 2022-06-13 03:19:59.650305
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Cast to class to use classmethod (requirement for _get_collector_name)
    fact_collector = PythonFactCollector()

    new_facts = fact_collector.collect()
    assert new_facts['python']['version']['major'] == sys.version_info[0]
    assert new_facts['python']['version']['minor'] == sys.version_info[1]
    assert new_facts['python']['version']['micro'] == sys.version_info[2]
    assert new_facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert new_facts['python']['version']['serial'] == sys.version_info[4]

# Generated at 2022-06-13 03:20:01.687598
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    c = PythonFactCollector()
    assert c.collect()['python']['type'] in ['CPython', 'IronPython', 'StacklessPython', 'PyPy', 'Jython']

# Generated at 2022-06-13 03:20:04.169321
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    from ansible.module_utils.facts.collector import CollectedFacts
    py_fc = PythonFactCollector()
    py_fc.collect(collected_facts=CollectedFacts(None))

# Generated at 2022-06-13 03:20:10.024824
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
 

# Generated at 2022-06-13 03:20:16.901973
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    import mock
    # Create a PythonFactCollector object
    my_collector = PythonFactCollector()

    type(my_collector).name = 'python'

    # Create a mock for sys.version_info
    sys.version_info = mock.Mock()
    type(sys.version_info).__getitem__ = mock.Mock(side_effect=[0,1,2,3,4])

    sys.version_info_list = [0, 1, 2, 3, 4]

    # Create a mock for sys.executable
    sys.executable = mock.Mock()

    type(sys).__dict__ = {'subversion': ['type'], 'version_info': sys.version_info_list, 'executable': sys.executable, 'implementation': {'name': 'type'}}

    # Create

# Generated at 2022-06-13 03:20:21.388637
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    collector = PythonFactCollector()
    result = collector.collect()
    assert type(result) == dict
    assert isinstance(result['python']['version_info'], list)

# Generated at 2022-06-13 03:20:28.702617
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    from ansible.module_utils import facts as module_utils_facts_a7cbb6f1b6f2410a8e4b4db4a1d69ea7
    f = PythonFactCollector()
    f.collect()
    result = {'python':
                {'type': 'CPython',
                 'executable': '/usr/local/bin/python2.7',
                 'has_sslcontext': True,
                 'version':
                     {'micro': 7,
                      'major': 2,
                      'minor': 7,
                      'releaselevel': 'final',
                      'serial': 0},
                 'version_info': [2, 7, 7, 'final', 0]},
              'python_version': '2.7.7'}
    assert f.get_facts() == result

# Generated at 2022-06-13 03:20:39.079809
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    collector = PythonFactCollector()
    facts = collector.collect()
    assert facts['python']['version_info'] == list(sys.version_info)
    assert facts['python']['version']['major'] == sys.version_info[0]
    assert facts['python']['version']['minor'] == sys.version_info[1]
    assert facts['python']['version']['micro'] == sys.version_info[2]
    assert facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert facts['python']['version']['serial'] == sys.version_info[4]
    assert facts['python']['executable'] == sys.executable
    assert facts['python']['has_sslcontext'] == HAS_SSLCONTEXT


# Generated at 2022-06-13 03:20:46.627025
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    import sys
    import pytest

    # Create an instance of the fact collector
    fact_collector = PythonFactCollector()

    # Call the method collect of the fact collector
    python_facts = fact_collector.collect()

    # Assert the result of the collect
    assert isinstance(python_facts, dict)

# Generated at 2022-06-13 03:22:05.242191
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    # A subclass of PythonFactCollector to expose protected members
    class TestPythonFactCollector(PythonFactCollector):
        def __init__(self):
            super(TestPythonFactCollector, self).__init__()
            # Initialize attributes
            self._fact_ids = set()
            self._facts = {}

        # Expose protected method collect
        def _collect(self, module=None, collected_facts=None):
            return self.collect(module, collected_facts)

    # Initialize a TestPythonFactCollector
    f = TestPythonFactCollector()

    # Compare version_info from test_module_utils.module_utils.facts.test_collector.py file
    # with version_info from test_module_utils.module_utils.facts.test_collector.py file
    # which is imported at the start of

# Generated at 2022-06-13 03:22:10.912762
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    c = PythonFactCollector()
    facts = c.collect()
    assert isinstance(facts, dict)
    assert 'python' in facts
    assert isinstance(facts['python'], dict)
    assert isinstance(facts['python']['version'], dict)
    assert isinstance(facts['python']['version_info'], list)
    assert isinstance(facts['python']['executable'], basestring)
    assert isinstance(facts['python']['has_sslcontext'], bool)