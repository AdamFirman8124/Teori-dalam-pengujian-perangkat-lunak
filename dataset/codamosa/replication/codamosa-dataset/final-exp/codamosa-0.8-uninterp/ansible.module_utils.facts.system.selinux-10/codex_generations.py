

# Generated at 2022-06-13 03:22:53.293161
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    facts_collection = SelinuxFactCollector()

    assert facts_collection.name == 'selinux'
    assert isinstance(facts_collection._fact_ids, set)

# Generated at 2022-06-13 03:22:56.734921
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
  selinux=SelinuxFactCollector()
  result = selinux.collect()
  assert result.get('selinux') is not None
  assert result.get('selinux_python_present') is not None

# Generated at 2022-06-13 03:23:07.066793
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():

    # The goal of this unit test is to make sure that SelinuxFactCollector.collect
    # methods returns correct facts when Python selinux module is present and when
    # it's not.
    fake_selinux_library = FakeSelinuxLibrary()
    selinux_collector = SelinuxFactCollector()
    selinux_facts = selinux_collector.collect(collected_facts=None)

    # If the SELinux Python library is missing, the only facts that are set are
    # selinux.status and selinux_python_present.
    if not HAVE_SELINUX:
        assert selinux_facts == {'selinux': {'status': 'Missing selinux Python library'},
                                 'selinux_python_present': False}
        return

    # If the library is present, all facts should

# Generated at 2022-06-13 03:23:09.775482
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    assert SelinuxFactCollector.name == 'selinux'
    assert 'selinux' in SelinuxFactCollector._fact_ids

# Generated at 2022-06-13 03:23:13.482125
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    fact_collector = SelinuxFactCollector()
    assert fact_collector.name == 'selinux'
    assert fact_collector._fact_ids is not None
    assert len(fact_collector._fact_ids) == 0

# Generated at 2022-06-13 03:23:20.829847
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():

    # given
    selinux_facts = {
        'status': 'enabled',
        'policyvers': '28',
        'config_mode': 'enforcing',
        'mode': 'enforcing',
        'type': 'targeted'
    }
    selinux_ansible_facts = {
        'selinux': selinux_facts,
        'selinux_python_present': True
    }

    # when
    selinux_collector = SelinuxFactCollector()
    result = selinux_collector.collect()

    # then
    assert result == selinux_ansible_facts

# Generated at 2022-06-13 03:23:21.565316
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    x = SelinuxFactCollector()
    assert x

# Generated at 2022-06-13 03:23:22.746621
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_collector = SelinuxFactCollector()
    assert selinux_collector.name == 'selinux'

# Generated at 2022-06-13 03:23:23.964559
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_facts = SelinuxFactCollector()
    assert selinux_facts is not None


# Generated at 2022-06-13 03:23:27.984752
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    fact_collector = SelinuxFactCollector()
    collected_facts = {}
    first_parsed_facts = fact_collector.collect(collected_facts)
    assert type(first_parsed_facts) == dict
    assert 'selinux' not in first_parsed_facts
    assert first_parsed_facts['selinux_python_present'] == False


# Generated at 2022-06-13 03:23:39.984174
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_facts = SelinuxFactCollector()
    assert selinux_facts.collect() == {
        'selinux': {
            'type': 'unknown',
            'policyvers': 'unknown',
            'mode': 'unknown',
            'config_mode': 'unknown',
            'status': 'disabled'
        },
        'selinux_python_present': True
    }

# Generated at 2022-06-13 03:23:47.470946
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():

    # Mock module and collected facts
    fake_module = object()
    fake_facts = {'selinux_python_present': False}

    # Mock calls to selinux for collecting facts
    def fake_is_selinux_enabled():
        return True

    def fake_security_getenforce():
        return 1

    def fake_security_policyvers():
        return 2

    def fake_selinux_getenforcemode():
        return (0,0)

    def fake_selinux_getpolicytype():
        return (0,'targeted')

    # Construct a SelinuxFactCollector
    selinux_fact_collector = SelinuxFactCollector()

    # Mock function call on selinux to is_selinux_enabled
    selinux.is_selinux_enabled = fake_is_selinux

# Generated at 2022-06-13 03:23:50.058975
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux = SelinuxFactCollector()
    assert isinstance(selinux, SelinuxFactCollector)


# Generated at 2022-06-13 03:23:51.254722
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    SelinuxFactCollector()

# Generated at 2022-06-13 03:23:52.254756
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    assert callable(SelinuxFactCollector)

# Generated at 2022-06-13 03:23:55.880281
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    module = None
    collected_facts = {}
    assert SelinuxFactCollector().collect(module, collected_facts) == {
        'selinux': {
            'status': 'Missing selinux Python library'
        },
        'selinux_python_present': False
    }

# Generated at 2022-06-13 03:24:07.463419
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # Disable selinux
    selinux.selinux_setenforce(0)
    selinux.selinux_setenforcemode(0)
    selinux.security_setenforce(0)

    selinux_facts = SelinuxFactCollector().collect()
    assert selinux_facts['selinux']['status'] == 'disabled'
    assert selinux_facts['selinux']['config_mode'] == 'disabled'
    assert selinux_facts['selinux']['mode'] == 'disabled'
    assert selinux_facts['selinux']['type'] in ['unknown', 'targeted']
    assert selinux_facts['selinux']['policyvers'] == 'unknown'
    assert selinux_facts['selinux_python_present']

    # Enable selinux

# Generated at 2022-06-13 03:24:08.054363
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    pass

# Generated at 2022-06-13 03:24:08.637400
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    assert False

# Generated at 2022-06-13 03:24:11.885285
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    assert SelinuxFactCollector().collect() == {
        'selinux': {'config_mode': 'unknown', 'status': 'Unknown selinux Python library'},
        'selinux_python_present': False
    }

# Generated at 2022-06-13 03:24:31.001849
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    fact_collector = SelinuxFactCollector()
    if HAVE_SELINUX:
        assert fact_collector.collect() == {'selinux': {'status': 'enabled', 'policyvers': selinux.security_policyvers(), 'config_mode': SELINUX_MODE_DICT[selinux.selinux_getenforcemode()[1]], 'mode': SELINUX_MODE_DICT[selinux.security_getenforce()], 'type': selinux.selinux_getpolicytype()[1]}, 'selinux_python_present': True}
    else:
        assert fact_collector.collect() == {'selinux': {'status': 'Missing selinux Python library'}, 'selinux_python_present': False}

# Generated at 2022-06-13 03:24:34.279304
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    '''Test that constructor creates a SelinuxFactCollector object'''
    selinux_fact_collector = SelinuxFactCollector()
    assert isinstance(selinux_fact_collector, SelinuxFactCollector)

# Generated at 2022-06-13 03:24:36.422666
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    # Test instance attribute values
    fact_collector = SelinuxFactCollector()
    assert fact_collector.name == 'selinux'
    assert fact_collector._fact_ids == set()


# Generated at 2022-06-13 03:24:39.856435
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    collector = SelinuxFactCollector()
    facts = collector.collect()
    assert 'selinux' in facts
    assert 'status' in facts['selinux']
    assert 'config_mode' in facts['selinux']

# Generated at 2022-06-13 03:24:42.964890
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():

    # Constructor of class SelinuxFactCollector should set member
    # 'name' to 'selinux'
    fc = SelinuxFactCollector()
    assert fc.name == 'selinux'


# Generated at 2022-06-13 03:24:46.326666
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    '''
    Unit test for constructor of class SelinuxFactCollector
    '''
    facts_collector = SelinuxFactCollector()
    assert facts_collector.name == 'selinux'


# Generated at 2022-06-13 03:24:51.504188
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    """
    Unit test for constructor of class SelinuxFactCollector
    """
    selinux_collector = SelinuxFactCollector()
    assert selinux_collector.name == 'selinux'
    assert selinux_collector._fact_ids == set()
    collected_facts = {}
    selinux_facts = selinux_collector.collect(collected_facts=collected_facts)
    assert selinux_facts == {'selinux': {'status': 'Missing selinux Python library'}, 
        'selinux_python_present': False}
    assert collected_facts == {}

# Generated at 2022-06-13 03:24:56.953530
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fc = SelinuxFactCollector()
    assert selinux_fc.name == 'selinux'
    assert selinux_fc.fact_id == 'selinux'
    assert selinux_fc._fact_ids == set()


# Generated at 2022-06-13 03:25:07.030777
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    if HAVE_SELINUX:
        selinux.is_selinux_enabled = lambda: False
    else:
        class FakeModuleUtil(object):
            def is_selinux_enabled(self):
                return False

        selinux = FakeModuleUtil()

    fact_collector = SelinuxFactCollector()
    facts = fact_collector.collect()
    assert facts['selinux'] == { 'status': 'disabled' }

    if HAVE_SELINUX:
        selinux.is_selinux_enabled = lambda: True
    else:
        selinux.is_selinux_enabled = lambda: True

    facts = fact_collector.collect()
    assert facts['selinux'].get('status') == 'enabled'
    assert facts['selinux'].get('policyvers')

# Generated at 2022-06-13 03:25:18.579616
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    """
    Unit test for class SelinuxFactCollector
    """
    module = None
    collected_facts = None

    # If the system has selinux library, the test passes.
    if SelinuxFactCollector.HAVE_SELINUX:
        df_collector = SelinuxFactCollector()
        df_collector.collect(module, collected_facts)
        assert 'selinux' in df_collector.collect(module, collected_facts)

    # The test fails if the system does not have selinux library.
    else:
        df_collector = SelinuxFactCollector()
        df_collector.collect(module, collected_facts)
        assert 'selinux' not in df_collector.collect(module, collected_facts)

# Generated at 2022-06-13 03:25:46.657569
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # Mock the module_utils.compat.selinux module
    def noop(*args, **kwargs):
        pass
    selinux.is_selinux_enabled = Mock(side_effect=noop)
    selinux.security_policyvers = Mock(side_effect=noop)
    selinux.security_getenforce = Mock(side_effect=noop)
    selinux.selinux_getpolicytype = Mock(side_effect=noop)
    selinux.selinux_getenforcemode = Mock(side_effect=noop)

    # Test when selinux library is missing
    if not HAVE_SELINUX:
        facts = SelinuxFactCollector().collect()
        assert facts['selinux'] == 'Missing selinux Python library'

# Generated at 2022-06-13 03:25:53.327429
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    from ansible.module_utils.facts import collector
    selinux_facts = collector.get_collector('selinux').collect()
    assert 'selinux_python_present' in selinux_facts
    if selinux_facts['selinux_python_present']:
        assert 'selinux' in selinux_facts
        assert 'status' in selinux_facts['selinux']
        assert 'config_mode' in selinux_facts['selinux']
        assert 'mode' in selinux_facts['selinux']
        assert 'type' in selinux_facts['selinux']
        assert 'policyvers' in selinux_facts['selinux']
    else:
        assert 'selinux' not in selinux_facts

# Generated at 2022-06-13 03:25:55.654146
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    obj = SelinuxFactCollector()
    assert obj.name == 'selinux'
    assert obj._fact_ids == set()


# Generated at 2022-06-13 03:26:01.392011
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    with open(os.devnull, 'w') as null_fds:
        selinux_fc = SelinuxFactCollector(None, None, None, extra_module_args=['test'],
                                          connection=None, runner_cache=None,
                                          module_cache=None, stderr=null_fds,
                                          stdout=null_fds)
        assert selinux_fc is not None
        assert selinux_fc.name == 'selinux'
        assert selinux_fc._fact_ids == set()

# Generated at 2022-06-13 03:26:03.756695
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    test_obj = SelinuxFactCollector()
    assert test_obj.name == 'selinux'
    assert test_obj._fact_ids == set()


# Generated at 2022-06-13 03:26:07.276930
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_facts = SelinuxFactCollector()
    # Procedure:
    # selinux_facts.collect()
    # assertEqual(selinux_facts._fact_ids, set(['selinux', 'selinux_python_present']))


# Generated at 2022-06-13 03:26:14.548253
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    '''SelinuxFactCollector.collect()'''

    # Create a test class for the method collect of the class SelinuxFactCollector
    class TestSelinuxFactCollector():

        # Create a mock for the function selinux.is_selinux_enabled so that when called
        # with no arguments, it always returns True
        def mock_selinux_is_selinux_enabled(self):
            return True

        # Create a mock for the function selinux.security_policyvers so that when called
        # with no arguments, it always returns 25
        def mock_selinux_security_policyvers(self):
            return 25

        # Create a mock for the function selinux.selinux_getenforcemode so that when called
        # with no arguments, it always returns 0,0

# Generated at 2022-06-13 03:26:15.220560
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    pass

# Generated at 2022-06-13 03:26:22.857020
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    mock_module = MockModule()
    mock_module.params = {
        'gather_subset': ['!all', 'selinux'],
        'gather_timeout': 10,
        'filter': '*'
    }
    mock_collector = SelinuxFactCollector(mock_module)
    # Patch
    with patch('ansible.module_utils.facts.collector.get_file_content', return_value=''):
        facts = mock_collector.collect(mock_module)
    assert facts == {'selinux': {'status': 'disabled'}, 'selinux_python_present': False}

# Generated at 2022-06-13 03:26:24.645465
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_facts = SelinuxFactCollector.collect()
    assert isinstance(selinux_facts, dict)


# Generated at 2022-06-13 03:27:07.292869
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    if HAVE_SELINUX:
        # noinspection PyUnresolvedReferences
        selinux.is_selinux_enabled = ...
        # noinspection PyUnresolvedReferences
        selinux.security_policyvers = ...
        # noinspection PyUnresolvedReferences
        selinux.selinux_getenforcemode = ...
        # noinspection PyUnresolvedReferences
        selinux.security_getenforce = ...
        # noinspection PyUnresolvedReferences
        selinux.selinux_getpolicytype = ...


# Generated at 2022-06-13 03:27:08.579115
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    SelinuxFactCollector.collect()

# Generated at 2022-06-13 03:27:19.675098
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
  # Use case 0 - Python library present, SELinux enabled, on Fedora
  selinux_config = """
SELINUX=enforcing
SELINUX_CONFIG_MODE=enforcing
SELINUXTYPE=targeted
"""

  selinux_contexts = """
system_u:object_r:etc_t:s0
system_u:object_r:etc_t:s0
system_u:object_r:etc_t:s0
system_u:object_r:passwd_etc_t:s0
"""


# Generated at 2022-06-13 03:27:24.625244
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():

    # Test for constructor of class SelinuxFactCollector
    se = SelinuxFactCollector()

    # Test for the values of _fact_ids
    assert se._fact_ids == {'selinux_python_present', 'selinux'}


# Generated at 2022-06-13 03:27:27.735117
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector is not None


# Generated at 2022-06-13 03:27:35.735521
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    from ansible.module_utils.facts.collector import FactsCollector
    from ansible.module_utils.facts.collector.selinux import SelinuxFactCollector

    facts_collector = FactsCollector()
    selinux_fact_collector = SelinuxFactCollector()

    all_collectors = facts_collector.collectors
    # all_collectors is a list, we must convert it to a set in order to compare it
    # with the set of _fact_ids of SelinuxFactCollector
    assert set(all_collectors) == selinux_fact_collector._fact_ids

# Generated at 2022-06-13 03:27:45.986230
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # When selinux Python library is missing check that only
    # status and selinux_python_present are set
    class FakeModule(object):
        def __init__(self):
            self.params = {}

    class FakeCollector(object):
        def __init__(self):
            self.collected_facts = {}

    fake_module = FakeModule()
    fake_collector = FakeCollector()

    key_list = SelinuxFactCollector.collect(fake_module, fake_collector.collected_facts).keys()
    assert set(key_list) == set(['selinux', 'selinux_python_present'])
    assert SelinuxFactCollector.collect(fake_module, fake_collector.collected_facts)["selinux_python_present"] == False
    assert SelinuxFact

# Generated at 2022-06-13 03:27:55.557838
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # Create a test object instance of class SelinuxFactCollector
    test_instance = SelinuxFactCollector()

    # Define test params
    test_params = dict()

    # Define expected result
    expected_result = dict(selinux=dict(
        config_mode='unknown',
        mode='unknown',
        status='disabled',
        type='unknown',
        policyvers='unknown')
    )

    # Execute method collect
    actual_result = test_instance.collect(module=None, collected_facts=None)

    # Ensure that all expected keys are present in the actual result
    if set(actual_result) == set(expected_result):
        # If all expected keys are present, ensure that the values match as well
        if actual_result == expected_result:
            return True
        else:
            return False

# Generated at 2022-06-13 03:27:56.555377
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    SELinuxFactCollector()

# Generated at 2022-06-13 03:28:01.056880
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinuxFactCollector = SelinuxFactCollector()
    assert selinuxFactCollector.name == 'selinux'
    assert selinuxFactCollector.priority == 30
    assert selinuxFactCollector._fact_ids == set()

# Generated at 2022-06-13 03:29:43.229063
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    """
    Tests to ensure that the collector works and collects data.
    """
    import platform
    import pytest

    # Mock the platform.system() method in platform module
    # to return a fake system
    system = 'Linux'
    platform.system = lambda: system

    # Mock the selinux.is_selinux_enabled() method in selinux
    # to return a fake status
    selinux.is_selinux_enabled = lambda: True

    # Mock the selinux.security_policyvers() method in selinux
    # to return a fake policy version
    selinux.security_policyvers = lambda: '28'

    # Mock the selinux.selinux_getenforcemode() method in selinux
    # to return a fake config mode

# Generated at 2022-06-13 03:29:45.290462
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    obj = SelinuxFactCollector()
    assert obj.name == 'selinux'

# Generated at 2022-06-13 03:29:48.508679
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    sfc = SelinuxFactCollector()
    assert sfc.name == 'selinux'
    assert isinstance(sfc._fact_ids, set)
    assert hasattr(sfc, 'collect')
    assert callable(sfc.collect)

# Generated at 2022-06-13 03:29:51.470372
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.name == 'selinux'
    assert len(selinux_fact_collector._fact_ids) == 0


# Generated at 2022-06-13 03:29:55.116854
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    p = SelinuxFactCollector()
    assert p.name == 'selinux'

# Generated at 2022-06-13 03:30:00.661457
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_fact_collector = SelinuxFactCollector()
    selinux_facts = selinux_fact_collector.collect()
    assert selinux_facts['selinux']['type'] != 'unknown'
    assert selinux_facts['selinux']['status'] != 'unknown'
    assert selinux_facts['selinux']['policyvers'] != 'unknown'

# Generated at 2022-06-13 03:30:01.611427
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    SelinuxFactCollector().collect()

# Generated at 2022-06-13 03:30:07.472480
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # Instantiate a SelinuxFactCollector object
    selinux_fact_collector = SelinuxFactCollector()
    # Get the method under test
    collect_method = selinux_fact_collector.collect
    # Get the return value from the method under test
    selinux_facts = collect_method()
    # Check the return value
    assert isinstance(selinux_facts, dict)
    assert 'selinux_python_present' in selinux_facts
    if selinux_facts['selinux_python_present'] == True:
        assert 'selinux' in selinux_facts
        assert 'status' in selinux_facts['selinux']
        if selinux_facts['selinux']['status'] == 'enabled':
            assert 'policyvers' in selinux_facts['selinux']


# Generated at 2022-06-13 03:30:17.455003
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # Create a single test for class SelinuxFactCollector
    test_collector = SelinuxFactCollector()

    # We can't assume that we have the selinux Python library, so we have to
    # test its availability.
    try:
        import selinux
    except ImportError:
        # We are unable to test SelinuxFactCollector.collect() if selinux is
        # not present so simply return an empty result. If selinux is not
        # present, we know that no data will be present in the collector.
        facts_dict = {}
    else:
        # If selinux is present, return a dict representing the output
        # of a test collect
        facts_dict = test_collector.collect()
    return facts_dict

# vim: expandtab tabstop=4 shiftwidth=4

# Generated at 2022-06-13 03:30:18.387186
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    assert SelinuxFactCollector() is not None