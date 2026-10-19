

# Generated at 2022-06-13 03:12:19.464259
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python = PythonFactCollector()
    facts = python.collect()
    assert isinstance(facts['python']['version']['major'], int)
    assert isinstance(facts['python']['version']['minor'], int)
    assert isinstance(facts['python']['version']['micro'], int)
    assert isinstance(facts['python']['version']['releaselevel'], str)
    assert isinstance(facts['python']['version']['serial'], int)
    assert isinstance(facts['python']['version_info'], list)
    assert isinstance(facts['python']['executable'], str)
    assert isinstance(facts['python']['has_sslcontext'], bool)
    assert isinstance(facts['python']['type'], str) or facts

# Generated at 2022-06-13 03:12:37.401222
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Since we want to get 'python' as a fact, we go to great lengths to
    # ensure that we aren't getting the python version of the invoker which
    # could be 2.6, 2.7 or 3.4.  The same for the python type if the platform
    # supports it.  We hard code the values of python version and python type
    # for this unit test so the test results would work across platforms.
    # For example, 'python2' could be 'python2' or 'cpython2' and both are
    # correct and valid.

    # Make a copy of sys.version_info and sys.subversion so that we don't
    # alter the values of the invoker's sys.version_info and sys.subversion
    v_info = [x for x in sys.version_info]

# Generated at 2022-06-13 03:12:44.431412
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python = PythonFactCollector(None, None)
    python_facts = python.collect()

    assert isinstance(python_facts, dict)
    assert 'python' in python_facts

    python_facts = python_facts['python']

    assert isinstance(python_facts['version'], dict)
    assert python_facts['version']['major'] == sys.version_info[0]
    assert python_facts['version']['minor'] == sys.version_info[1]
    assert python_facts['version']['micro'] == sys.version_info[2]
    assert python_facts['version']['releaselevel'] == sys.version_info[3]
    assert python_facts['version']['serial'] == sys.version_info[4]


# Generated at 2022-06-13 03:12:47.238966
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """Test PythonFactCollector.collect method

    :return:
    """
    import doctest
    doctest.testmod(verbose=False, optionflags=doctest.ELLIPSIS)


# Generated at 2022-06-13 03:12:54.596787
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Instantiate object
    python_collector = PythonFactCollector()
    # Call collect method
    test_results = python_collector.collect()

    # Test results
    assert test_results['python']['version']['major'] >= 3
    assert test_results['python']['version_info'][0] >= 3
    assert test_results['python']['has_sslcontext'] is True

if __name__ == '__main__':
    pytest.main(['-v', __file__])

# Generated at 2022-06-13 03:13:12.285053
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = PythonFactCollector().collect(None, {})

    assert 'version' in python_facts['python']
    assert python_facts['python']['version']['major'] == sys.version_info[0]
    assert python_facts['python']['version']['minor'] == sys.version_info[1]
    assert python_facts['python']['version']['micro'] == sys.version_info[2]
    assert python_facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert python_facts['python']['version']['serial'] == sys.version_info[4]
    assert python_facts['python']['version_info'] == list(sys.version_info)
    assert python_facts['python']['executable']

# Generated at 2022-06-13 03:13:20.783513
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact_collector = PythonFactCollector()
    facts = python_fact_collector.collect()
    assert len(facts) == 1
    assert 'python' in facts
    python_fact = facts['python']
    assert 'version' in python_fact
    version_fact = python_fact['version']
    assert 'major' in version_fact
    assert isinstance(version_fact['major'], int)
    assert 'minor' in version_fact
    assert isinstance(version_fact['minor'], int)
    assert 'micro' in version_fact
    assert isinstance(version_fact['micro'], int)
    assert 'releaselevel' in version_fact
    assert isinstance(version_fact['releaselevel'], basestring)
    assert 'serial' in version_fact

# Generated at 2022-06-13 03:13:25.981110
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact = PythonFactCollector(None)
    collected_facts = {}
    python_facts = python_fact.collect(None, collected_facts)
    assert 'python' in python_facts
    assert 'version' in python_facts['python']
    assert 'version_info' in python_facts['python']
    assert 'executable' in python_facts['python']
    assert 'has_sslcontext' in python_facts['python']
    assert 'type' in python_facts['python']

# Generated at 2022-06-13 03:13:35.655617
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector()
    fact_collector._module = None
    fact_collector._collected_facts = {}

    facts = fact_collector.collect(None, None)

    assert facts['python']['version']['major'] == sys.version_info[0]
    assert facts['python']['version']['minor'] == sys.version_info[1]
    assert facts['python']['version']['micro'] == sys.version_info[2]
    assert facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert facts['python']['version']['serial'] == sys.version_info[4]
    assert facts['python']['version_info'] == list(sys.version_info)

# Generated at 2022-06-13 03:13:38.034033
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fc = PythonFactCollector()
    facts = fc.collect()
    assert 'python' in facts
    for k in ['version_info', 'version', 'executable', 'has_sslcontext']:
        assert k in facts['python']

# Generated at 2022-06-13 03:13:41.135658
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = PythonFactCollector().collect()
    assert 'python' in python_facts

# Generated at 2022-06-13 03:13:46.704648
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact = PythonFactCollector()
    result = fact.collect()
    assert isinstance(result.get('python'), dict)
    assert isinstance(result.get('python').get('version'), dict)
    assert isinstance(result.get('python').get('version_info'), list)
    assert isinstance(result.get('python').get('executable'), str)
    assert isinstance(result.get('python').get('has_sslcontext'), bool)
    assert isinstance(result.get('python').get('type'), str)


# Generated at 2022-06-13 03:13:57.860434
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    argv_backup = sys.argv

# Generated at 2022-06-13 03:14:05.496990
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

# Generated at 2022-06-13 03:14:12.181102
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    # Test_PythonFactCollector_collect:
    #
    # Arrange:

    # SUT (System Under Test)
    python_fact_collector = PythonFactCollector()

    # Act:
    python_facts = python_fact_collector.collect()

    # Assert:
    assert python_facts['python']['version']['major'] == sys.version_info[0]
    assert python_facts['python']['version']['minor'] == sys.version_info[1]
    assert python_facts['python']['version']['micro'] == sys.version_info[2]
    assert python_facts['python']['version']['releaselevel'] == sys.version_info[3]
    assert python_facts['python']['version']['serial'] == sys.version_info

# Generated at 2022-06-13 03:14:22.419337
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    from ansible.module_utils.facts.collector import FactsCollector
    from ansible.module_utils.facts import get_all_facts
    from ansible.module_utils._text import to_bytes

    # Load FactsCollector with content of file tests/module_utils/facts/ansible_facts_test.json
    facts_collector = FactsCollector()
    facts_collector.module_name = 'FactsCollectorTestModule'
    facts_collector.module_args = to_bytes('')

    facts_collector.load_fact_file(__file__.rsplit('/', 1)[0] + '/ansible_facts_test.json')

    python_fact_collector = PythonFactCollector()

    collected_facts = {}

    # Get all facts

# Generated at 2022-06-13 03:14:29.480382
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_collector = PythonFactCollector()
    python_facts = python_collector.collect()
    assert python_facts['python']['version']['major'] == 3
    assert python_facts['python']['type'] == 'CPython'
    assert python_facts['python']['has_sslcontext'] == True
    assert python_facts['python']['version_info'] == [3, 4, 1, 'final', 0]
    assert python_facts['python']['executable'].endswith('bin/python3.4')

# Generated at 2022-06-13 03:14:33.703808
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    collector = PythonFactCollector()
    ansible_facts = collector.collect(collected_facts=None)
    assert isinstance(ansible_facts['python'], dict), "Facts is not a dict"

# Generated at 2022-06-13 03:14:36.498987
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    m = PythonFactCollector()
    res = m.collect()

    assert isinstance(res, dict)
    assert 'python' in res
    assert 'version' in res['python']


# Generated at 2022-06-13 03:14:41.853824
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
   python_fact_collector = PythonFactCollector()
   collected_facts = {}
   python_facts = python_fact_collector.collect(collected_facts)
   assert python_facts['python']['version']['major'] == sys.version_info[0]
   assert python_facts['python']['type'] == sys.subversion[0]

# Generated at 2022-06-13 03:14:54.826289
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    # This is a simplistic test to see if we can get a non-empty fact dict
    fact_collector = PythonFactCollector()
    facts = fact_collector.collect()
    assert facts == {'python': {
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

# Generated at 2022-06-13 03:15:00.307248
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """Unit test for method collect of class PythonFactCollector."""
    collector = PythonFactCollector()

    # Check a few known keys
    result = collector.collect()
    assert 'python' in result, 'python fact missing'
    assert 'version' in result['python'], 'python.version fact missing'
    assert 'version_info' in result['python'], 'python.version_info fact missing'
    assert 'executable' in result['python'], 'python.executable fact missing'
    assert 'has_sslcontext' in result['python'], 'python.has_sslcontext fact missing'
    assert 'type' in result['python'], 'python.type fact missing'

# Generated at 2022-06-13 03:15:02.519590
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pf = PythonFactCollector()
    assert 'python' in pf.collect()

# Generated at 2022-06-13 03:15:11.188009
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    c = PythonFactCollector()
    f = c.collect()

    assert 'python' in f
    # python_version_info
    assert isinstance(f['python']['version_info'], list)
    assert len(f['python']['version_info']) == 5
    # python_version
    assert isinstance(f['python']['version'], dict)
    assert len(f['python']['version']) == 5
    for key in ['major', 'minor', 'micro', 'releaselevel', 'serial']:
        assert key in f['python']['version']
        assert isinstance(f['python']['version'][key], int)
    # python_executable
    assert isinstance(f['python']['executable'], str)
    # python_type
    assert isinstance

# Generated at 2022-06-13 03:15:14.985709
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    expected = {
        'python': {
            'version': {
                'major': 2,
                'micro': 7,
                'minor': 13,
                'releaselevel': 'final',
                'serial': 0
            },
            'executable': '/usr/bin/python2.7',
            'has_sslcontext': False,
            'type': 'CPython',
            'version_info': [2, 7, 13, 'final', 0]
        }
    }

    python_fact_collector = PythonFactCollector()
    python_facts = python_fact_collector.collect()

    assert python_facts == expected


# Generated at 2022-06-13 03:15:24.693937
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    try:
        python_facts = PythonFactCollector({}).collect()
        assert python_facts['python']
        assert python_facts['python']['version']
        assert python_facts['python']['version']['major']
        assert python_facts['python']['version']['minor']
        assert python_facts['python']['version']['micro']
        assert python_facts['python']['version']['releaselevel']
        assert python_facts['python']['version']['serial']
        assert python_facts['python']['version_info']
        assert python_facts['python']['executable']
        assert python_facts['python']['type']
        assert python_facts['python']['has_sslcontext']
    except AttributeError:
        assert False

# Generated at 2022-06-13 03:15:34.888903
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    ansible_module = lambda: None
    ansible_module.params = {}
    ansible_module.exit_json = lambda x: None

    python_fact_collector = PythonFactCollector()

    py_version = ".".join(map(str, sys.version_info[:3]))

# Generated at 2022-06-13 03:15:35.800252
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector()
    fact_collector.collect()

# Generated at 2022-06-13 03:15:41.000063
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pyfc = PythonFactCollector()
    assert pyfc.collect() == {
        "python": {
            "version": {
                "major": sys.version_info[0],
                "minor": sys.version_info[1],
                "micro": sys.version_info[2],
                "releaselevel": sys.version_info[3],
                "serial": sys.version_info[4]
            },
            "version_info": list(sys.version_info),
            "executable": sys.executable,
            "has_sslcontext": HAS_SSLCONTEXT,
            "type": "CPython"
        }
    }

# Generated at 2022-06-13 03:15:49.627982
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    p = PythonFactCollector()
    out = p.collect()
    assert isinstance(out, dict)
    keys = ['python']
    assert set(out).difference(keys) == set()
    python_keys = ['version', 'version_info', 'executable', 'has_sslcontext', 'type']
    assert set(out['python']).difference(python_keys) == set()
    version_keys = ['major', 'minor', 'micro', 'releaselevel', 'serial']
    assert set(out['python']['version']).difference(version_keys) == set()
    assert isinstance(out['python']['version']['major'], int)
    assert isinstance(out['python']['version']['minor'], int)

# Generated at 2022-06-13 03:15:59.171891
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact_collector = PythonFactCollector()
    facts = python_fact_collector.collect()
    assert isinstance(facts['python'], dict)

# Generated at 2022-06-13 03:16:15.499749
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    collector = PythonFactCollector()
    assert collector.collect()['python'] == {
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

# Generated at 2022-06-13 03:16:31.030373
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pc = PythonFactCollector()
    res = pc.collect()
    assert 'python' in res['ansible_facts']
    assert 'version' in res['ansible_facts']['python']
    assert 'major' in res['ansible_facts']['python']['version']
    assert 'minor' in res['ansible_facts']['python']['version']
    assert 'micro' in res['ansible_facts']['python']['version']
    assert 'releaselevel' in res['ansible_facts']['python']['version']
    assert 'serial' in res['ansible_facts']['python']['version']
    assert 'version_info' in res['ansible_facts']['python']
    assert 'executable' in res['ansible_facts']['python']

# Generated at 2022-06-13 03:16:38.315321
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

# Generated at 2022-06-13 03:16:39.978366
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    fact_collector = PythonFactCollector()
    facts = fact_collector.collect()

    assert facts['python']['version']['major'] == sys.version_info[0]

# Generated at 2022-06-13 03:16:45.823839
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    argspec = {}
    argspec['module'] = dict()
    argspec['collected_facts'] = dict()
    obj = PythonFactCollector()
    sys.modules['ansible'] = mock.Mock()
    sys.modules['ansible.module_utils'] = mock.Mock()
    sys.modules['ansible.module_utils.facts'] = mock.Mock()
    sys.modules['ansible.module_utils.facts.collector'] = mock.Mock()


# Generated at 2022-06-13 03:16:50.444794
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Create the test object
    python_fact_collector = PythonFactCollector()

    # Fake values to return and test with
    fake_sys_version_info = (1, 2, 3, 'final', 0)
    fake_sys_version_info_str = '1.2.3 final (0)'
    fake_sys_executable = '/fake/path/from/sys.executable'

    # Stub out functions used by this method as part of the test
    def fake__sys_version_info():
        return fake_sys_version_info

    def fake__sys_version_info_str():
        return fake_sys_version_info_str

    def fake__sys_executable():
        return fake_sys_executable

    from ansible.module_utils.facts.collector.python import \
        PythonFactCollector

# Generated at 2022-06-13 03:17:00.837402
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """
    Tests PythonFactCollector.collect
    """
    collector = PythonFactCollector()

    # If a Python2 major version is < 3, let's assume it's 2.7 or lower.

# Generated at 2022-06-13 03:17:10.787051
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    '''
    Test the collects facts method
    '''
    fact_collector = PythonFactCollector()
    result = fact_collector.collect()

    assert result['python']['version'] == {
        'major': sys.version_info[0],
        'minor': sys.version_info[1],
        'micro': sys.version_info[2],
        'releaselevel': sys.version_info[3],
        'serial': sys.version_info[4]
    }

    assert result['python']['version_info'] == list(sys.version_info)

    assert result['python']['executable'] == sys.executable

    assert result['python']['has_sslcontext'] == HAS_SSLCONTEXT

# Generated at 2022-06-13 03:17:13.895518
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    from ansible.module_utils.facts.collector import FactsCollector

    pfc = PythonFactCollector()
    pfc.collect()

    assert pfc.name == 'python'
    assert pfc._fact_ids == set(['python'])


# Generated at 2022-06-13 03:17:32.790492
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    tf = PythonFactCollector()
    assert tf is not None

    facts = tf.collect()
    assert "python" in facts
    assert "version" in facts["python"]
    assert "has_sslcontext" in facts["python"]
    assert "version_info" in facts["python"]
    assert "executable" in facts["python"]
    assert "type" in facts["python"]

    # This is the only test that fails on Python 3.5
    if sys.version_info[1] != 5:
        assert len(facts["python"]["version_info"]) == 5

    assert facts["python"]["version"]["releaselevel"] in ["alpha", "beta", "candidate", "final"]
    assert facts["python"]["version"]["serial"] == -1

# Generated at 2022-06-13 03:17:38.635150
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector()
    facts = pfc.collect()

    assert 'python' in facts
    assert 'type' in facts['python']
    assert isinstance(facts['python']['type'], str)
    assert 'version' in facts['python']
    assert 'version_info' in facts['python']
    assert isinstance(facts['python']['version_info'], list)
    assert 'executable' in facts['python']
    assert isinstance(facts['python']['executable'], str)
    assert 'has_sslcontext' in facts['python']
    assert isinstance(facts['python']['has_sslcontext'], bool)

# Generated at 2022-06-13 03:17:49.173994
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector()
    collected_facts = pfc.collect()
    assert 'python' in collected_facts.keys()
    assert 'version' in collected_facts['python'].keys()
    assert 'version_info' in collected_facts['python'].keys()
    assert 'major' in collected_facts['python']['version'].keys()
    assert 'minor' in collected_facts['python']['version'].keys()
    assert 'micro' in collected_facts['python']['version'].keys()
    assert 'releaselevel' in collected_facts['python']['version'].keys()
    assert 'serial' in collected_facts['python']['version'].keys()
    assert 'executable' in collected_facts['python'].keys()
    assert 'has_sslcontext' in collected_facts

# Generated at 2022-06-13 03:17:59.937695
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils.facts.collector.system import SystemFactCollector
    from ansible.module_utils.facts.collector.virtual import VirtualFactCollector
    from ansible.module_utils.facts.collector.pip import PipFactCollector
    collected_facts = {}
    python_collector = PythonFactCollector()
    python_collector.collect(collected_facts = collected_facts)
    # TODO: Check if it is possible to check when type == None
    assert collected_facts["python"]["version"]["major"] == 3
    assert collected_facts["python"]["version"]["minor"] == 7

# Generated at 2022-06-13 03:18:01.245921
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact_collector = PythonFactCollector()
    python_fact_collector.collect()

# Generated at 2022-06-13 03:18:04.013396
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    gfc = PythonFactCollector()
    assert gfc.collect()

    # includes sslcontext fact
    assert 'has_sslcontext' in gfc.collect()['python']

# Generated at 2022-06-13 03:18:11.933504
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_collector = PythonFactCollector()
    # execute collect method:
    python_collector.collect()
    # get collected facts
    facts = python_collector.get_facts()
    # test if expected facts are in the collected facts
    assert facts['python']
    assert facts['python']['executable'] == sys.executable
    assert type(facts['python']['version_info']) == list
    assert len(facts['python']['version_info']) == 5
    assert type(facts['python']['version']) == dict
    assert len(facts['python']['version']) == 5
    assert facts['python']['version']['major'] == sys.version_info[0]
    assert facts['python']['version']['minor'] == sys.version_info[1]

# Generated at 2022-06-13 03:18:13.440573
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = PythonFactCollector().collect()
    assert 'python' in python_facts
    assert 'type' in python_facts['python']
    assert 'version' in python_facts['python']

# Generated at 2022-06-13 03:18:15.000332
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # initialize the module object
    module = None
    # initialize the instance object
    instance = PythonFactCollector()
    # return the python facts
    return instance.collect(module)

# Generated at 2022-06-13 03:18:18.375740
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Create a PythonFactCollector object
    p = PythonFactCollector()

    # Test that we get version info
    version = p.collect()['python']['version']
    assert version['major'] >= 2
    assert 0 <= version['minor'] <= 9

    # Test that we get version_info
    version_info = p.collect()['python']['version_info']
    assert isinstance(version_info, list)

    # Test that we get executable
    assert isinstance(p.collect()['python']['executable'], basestring)

    # Test  that we get has_sslcontext
    assert isinstance(p.collect()['python']['has_sslcontext'], bool)

# Generated at 2022-06-13 03:18:51.641402
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = PythonFactCollector().collect()
    assert 'python' in python_facts
    assert 'version' in python_facts['python']
    assert 'has_sslcontext' in python_facts['python']

# Generated at 2022-06-13 03:18:59.734486
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    '''Unit test for method collect of class PythonFactCollector'''
    python_fact_collector = PythonFactCollector()
    python_facts = python_fact_collector.collect()

    assert 'python' in python_facts

    assert 'version' in python_facts['python']
    assert 'version_info' in python_facts['python']
    assert 'executable' in python_facts['python']
    assert 'has_sslcontext' in python_facts['python']
    assert 'type' in python_facts['python']

    assert 'major' in python_facts['python']['version']
    assert 'minor' in python_facts['python']['version']
    assert 'micro' in python_facts['python']['version']
    assert 'releaselevel' in python_facts['python']['version']

# Generated at 2022-06-13 03:19:08.698838
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # create PythonFactCollector object
    test_python = PythonFactCollector()

    # collect
    test_python_facts = test_python.collect()

    # assert
    assert 'python' in test_python_facts, "python is missing in facts"
    python = test_python_facts['python']
    assert 'version' in python, "version is missing in facts"
    version = python['version']
    assert version['major'] == sys.version_info[0], "major version mismatch"
    assert version['minor'] == sys.version_info[1], "minor version mismatch"
    assert version['micro'] == sys.version_info[2], "micro version mismatch"
    assert version['releaselevel'] == sys.version_info[3], "releaselevel version mismatch"

# Generated at 2022-06-13 03:19:10.551353
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    try:
        python_collector = PythonFactCollector()
        result = python_collector.collect()
        assert result
    except:
       print ("test_PythonFactCollector_collect() failed")
       raise

# Generated at 2022-06-13 03:19:22.334016
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Create an instance of PythonFactCollector
    py_fact_collector = PythonFactCollector()
    # Collect facts
    facts = py_fact_collector.collect()
    # Assert that the collect method returns a dictionary
    assert isinstance(facts, dict)
    # Assert that the dictionary includes a 'python' key
    assert ('python' in facts)
    # Assert that the 'python' key has the proper value
    assert (facts['python']['version']['major'] == sys.version_info[0])
    assert (facts['python']['version']['minor'] == sys.version_info[1])
    assert (facts['python']['version']['micro'] == sys.version_info[2])

# Generated at 2022-06-13 03:19:31.374344
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    import sys
    import pytest
    sys.modules['ansible.module_utils.facts.collector'] = pytest.Mock()
    sys.modules['platform'] = pytest.Mock()
    sys.modules['platform'].python_version = lambda: '2.7.18'
    sys.modules['platform'].platform = lambda: 'Darwin-16.7.0-x86_64-i386-64bit'
    sys.modules['platform'].dist = lambda: ('', '', '')
    sys.modules['platform'].mac_ver = lambda: ('', ('', '', ''), '')
    sys.modules['platform'].python_implementation = lambda: 'CPython'
    sys.modules['platform'].win32_ver = lambda: ('','','','','','','','','')

# Generated at 2022-06-13 03:19:34.289794
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pc = PythonFactCollector(None)
    python_facts = pc.collect()
    assert python_facts.get('python')

# Generated at 2022-06-13 03:19:39.729336
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = {'python': {'version': {'major': 2.7, 'minor': 12,
        'micro': 0, 'releaselevel': 'final', 'serial': 0},
        'version_info': [2, 7, 12, 'final', 0], 'executable': '/usr/bin/python',
        'has_sslcontext': True}}
    assert PythonFactCollector().collect() == python_facts

# Generated at 2022-06-13 03:19:45.228999
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    c = PythonFactCollector()
    facts = c.collect()
    assert isinstance(facts, dict)
    assert 'python' in facts
    assert isinstance(facts['python'], dict)
    assert 'version' in facts['python']
    assert 'version_info' in facts['python']
    assert 'executable' in facts['python']
    assert 'has_sslcontext' in facts['python']

# Generated at 2022-06-13 03:19:54.921166
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_info = PythonFactCollector().collect()

    assert len(python_info) == 1
    assert python_info['python']['version']['major'] == sys.version_info[0]
    assert python_info['python']['version']['minor'] == sys.version_info[1]
    assert python_info['python']['version']['micro'] == sys.version_info[2]
    assert python_info['python']['version']['releaselevel'] == sys.version_info[3]
    assert python_info['python']['version']['serial'] == sys.version_info[4]
    assert python_info['python']['version_info'] == list(sys.version_info)
    assert python_info['python']['executable'] == sys.executable


# Generated at 2022-06-13 03:21:05.286264
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    # Create a PythonFactCollector object and call its collect method
    pf = PythonFactCollector()
    collected_facts = pf.collect(collected_facts={})
    #print(collected_facts)

    # Check each dictionary item
    assert 'python' in collected_facts
    assert 'version' in collected_facts['python']
    assert 'type' in collected_facts['python']
    assert 'has_sslcontext' in collected_facts['python']
    assert 'executable' in collected_facts['python']
    assert 'version_info' in collected_facts['python']
    assert 'major' in collected_facts['python']['version']
    assert 'minor' in collected_facts['python']['version']
    assert 'micro' in collected_facts['python']['version']

# Generated at 2022-06-13 03:21:10.936888
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():

    # Set up the test PythonFactCollector
    pf = PythonFactCollector()

    # All PythonFactCollector._fact_ids should be in the result
    assert set(pf._fact_ids).issubset(pf.collect())

    # If HAS_SSLCONTEXT == True, then result['python']['has_sslcontext'] should be True
    if HAS_SSLCONTEXT:
        assert pf.collect()['python']['has_sslcontext'] == True

    # If HAS_SSLCONTEXT == False, then result['python']['has_sslcontext'] should be False
    if not HAS_SSLCONTEXT:
        assert pf.collect()['python']['has_sslcontext'] == False

    # If sys.implementation is defined, then result['python']['type'] should be equal to

# Generated at 2022-06-13 03:21:12.884565
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """Test that PythonFactCollector().collect() returns expected dictionary."""

    assert 'python' in PythonFactCollector().collect()

# Generated at 2022-06-13 03:21:14.180222
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    py_fc = PythonFactCollector()
    py_fc.collect()

# Generated at 2022-06-13 03:21:17.767263
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_facts = PythonFactCollector().collect()

    assert 'python' in python_facts
    assert 'version' in python_facts['python']
    assert 'version_info' in python_facts['python']
    assert 'executable' in python_facts['python']
    assert python_facts['python']['executable'] == sys.executable


# Generated at 2022-06-13 03:21:19.941400
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    python_fact_collector = PythonFactCollector()
    python_facts = python_fact_collector.collect()
    assert isinstance(python_facts['python']['version']['major'], int)
    assert isinstance(python_facts['python']['version_info'], list)
    assert isinstance(python_facts['python']['has_sslcontext'], bool)

# Generated at 2022-06-13 03:21:25.653522
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    collector = PythonFactCollector()
    facts = collector.collect()
    assert facts['python']['version'] == {
        'major': sys.version_info[0],
        'minor': sys.version_info[1],
        'micro': sys.version_info[2],
        'releaselevel': sys.version_info[3],
        'serial': sys.version_info[4]
    }
    assert facts['python']['version_info'] == list(sys.version_info)
    assert facts['python']['executable'] == sys.executable
    assert facts['python']['has_sslcontext'] == HAS_SSLCONTEXT
    if hasattr(sys, 'subversion'):
        assert facts['python']['type'] == sys.subversion[0]

# Generated at 2022-06-13 03:21:31.357161
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    assert PythonFactCollector().collect() == {
        "python": {
            "executable": "/usr/bin/python3",
            "has_sslcontext": True,
            "type": "CPython",
            "version": {
                "major": 3,
                "micro": 4,
                "minor": 4,
                "releaselevel": "final",
                "serial": 0},
            "version_info": [3, 4, 4, "final", 0]
        }
    }

# Generated at 2022-06-13 03:21:36.770716
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    pfc = PythonFactCollector()
    python_facts = pfc.collect()
    assert python_facts['python']['version']['major'] == sys.version_info[0]
    assert python_facts['python']['has_sslcontext'] == HAS_SSLCONTEXT

    if hasattr(sys, 'implementation'):
        assert python_facts['python']['type'] == sys.implementation.name
    else:
        assert python_facts['python']['type'] == None

    assert python_facts['python']['version']['releaselevel'] == sys.version_info[3]

# Generated at 2022-06-13 03:21:42.285466
# Unit test for method collect of class PythonFactCollector
def test_PythonFactCollector_collect():
    """
    Unit test for method collect of class PythonFactCollector.
    """
    py_fact_collector = PythonFactCollector()
    py_facts = py_fact_collector.collect()
    assert py_facts == {'python': {'has_sslcontext': HAS_SSLCONTEXT, 'version': {'major': sys.version_info[0], 'minor': sys.version_info[1], 'micro': sys.version_info[2], 'releaselevel': sys.version_info[3], 'serial': sys.version_info[4]}, 'type': sys.implementation.name, 'version_info': list(sys.version_info), 'executable': sys.executable}}