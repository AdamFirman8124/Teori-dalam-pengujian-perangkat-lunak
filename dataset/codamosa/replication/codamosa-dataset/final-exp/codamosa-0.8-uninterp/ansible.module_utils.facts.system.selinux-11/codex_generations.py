

# Generated at 2022-06-13 03:22:56.085782
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_facts = SelinuxFactCollector()
    assert selinux_facts


# Generated at 2022-06-13 03:23:06.714411
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # Create mock selinux object
    class MockSelinux:
        def is_selinux_enabled(self):
            return True

        def security_policyvers(self):
            return '2'

        def selinux_getenforcemode(self):
            return (0, 1)

        def security_getenforce(self):
            return 1

        def selinux_getpolicytype(self):
            return (0, 'targeted')

    # Create mock module object
    class MockModule:
        pass

    # Create mock module utils
    class MockModuleUtils:
        def compat(self):
            return MockSelinux()

    # Get instance of SelinuxFactCollector
    selinux_collector = SelinuxFactCollector()

    # Create mock module utils
    module_utils = MockModuleUtils()

# Generated at 2022-06-13 03:23:13.359214
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    print('Running selinux fact collector constructor')
    cf = SelinuxFactCollector()
    assert hasattr(cf, 'name') and cf.name == 'selinux', ('Selinux fact collector has no name or has the wrong name')
    assert hasattr(cf, '_fact_ids') and isinstance(cf._fact_ids, set), ('Selinux fact collector has no _fact_ids or has the wrong type')


# Generated at 2022-06-13 03:23:18.681117
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # If selinux.so is not available at all, don't even run the test.
    selinux_py_found = False
    try:
        import selinux
        selinux_py_found = True
    except ImportError:
        pass

    if not selinux_py_found:
        return

    selinux_fact_collector = SelinuxFactCollector()
    facts = selinux_fact_collector.collect()
    assert 'selinux' in facts
    assert 'status' in facts['selinux']

# Generated at 2022-06-13 03:23:20.400377
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_collector = SelinuxFactCollector()
    assert selinux_collector.name == "selinux"

# Generated at 2022-06-13 03:23:27.818605
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # Test the method with no selinux library present
    collector = SelinuxFactCollector()
    mock_module = MagicMock()
    mock_module.params = {}
    mock_facts = {}
    facts = collector.collect(module=mock_module, collected_facts=mock_facts)
    assert facts == {
        'selinux_python_present': False,
        'selinux': {
            'status': 'Missing selinux Python library'
        }
    }

    # Mock selinux module
    # status = enabled
    # policyvers = 24
    # config_mode = enforcing
    # mode = enforcing
    # type = targeted
    with patch('ansible.module_utils.selinux') as selinux_mock:
        selinux_mock.selinux_getenforcemode.return_

# Generated at 2022-06-13 03:23:28.463154
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    obj = SelinuxFactCollector()
    obj.collect()

# Generated at 2022-06-13 03:23:29.341249
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    assert SelinuxFactCollector()

# Generated at 2022-06-13 03:23:32.240168
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    '''
    Test the constructor of class SelinuxFactCollector
    '''

    selinux_collector = SelinuxFactCollector()

    assert selinux_collector.name == 'selinux'
    assert selinux_collector._fact_ids == set()

# Generated at 2022-06-13 03:23:37.585161
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    my_collector = SelinuxFactCollector()
    assert my_collector.name == 'selinux'
    assert my_collector.collect() == {'selinux': {}, 'selinux_python_present': False}

# Generated at 2022-06-13 03:23:49.189936
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_helpers = SelinuxFactCollector()
    selinux_helpers.collect()

# Generated at 2022-06-13 03:23:50.549189
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    assert isinstance(SelinuxFactCollector(), SelinuxFactCollector)

# Generated at 2022-06-13 03:23:51.782990
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    SelinuxFactCollector().collect()

# Generated at 2022-06-13 03:23:54.763200
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.name == 'selinux'
    assert selinux_fact_collector._fact_ids == set()

# Generated at 2022-06-13 03:24:01.930330
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    fc = SelinuxFactCollector()
    facts = fc.collect()

    if HAVE_SELINUX:
        assert facts['selinux']['config_mode'] in ('enforcing', 'permissive', 'disabled', 'unknown')
        assert facts['selinux']['mode'] in ('enforcing', 'permissive', 'disabled', 'unknown')
        assert facts['selinux']['type'] in ('targeted', 'minimum', 'mls', 'unknown')
        assert facts['selinux']['status'] in ('enabled', 'disabled')
        assert facts['selinux']['policyvers']
    else:
        assert facts['selinux']['status'] == 'Missing selinux Python library'
    assert facts['selinux_python_present']

# Generated at 2022-06-13 03:24:04.509170
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    #Create instance of SelinuxFactCollector
    f = SelinuxFactCollector()


# Generated at 2022-06-13 03:24:08.142714
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    obj1 = SelinuxFactCollector()
    obj2 = SelinuxFactCollector()
    assert obj1.name == 'selinux'
    assert obj2.name == 'selinux'
    assert obj1.collect() == obj2.collect()

# Generated at 2022-06-13 03:24:12.719686
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_collector = SelinuxFactCollector()
    # assume default selinux params
    selinux_collector.collect()
    assert selinux_collector.name == 'selinux'
    assert selinux_collector._fact_ids == set()
    selinux_collector.get_facts().keys() == ['selinux', 'selinux_python_present']

# Generated at 2022-06-13 03:24:17.033448
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    # In the absence of the selinux module, we only get what we can
    collector = SelinuxFactCollector()
    collected_facts = collector.collect()
    assert collected_facts['selinux']['status'] == 'Missing selinux Python library'
    assert collected_facts['selinux_python_present'] is False

# Generated at 2022-06-13 03:24:19.545171
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.name == 'selinux'
    assert selinux_fact_collector._fact_ids == set()

# Generated at 2022-06-13 03:24:46.497532
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    """
    The test_SelinuxFactCollector_collect function helps to cover the following test scenario:

    If selinux library is missing, only set the status and selinux_python_present since
    there is no way to tell if SELinux is enabled or disabled on the system
    without the library.
    """

    mock_HAVE_SELINUX = True
    mock_selinux = 'selinux'
    mock_function_value = 'function value'
    mock_selinux_getenforcemode = 'selinux getenforcemode'
    mock_selinux_getpolicytype = 'selinux getpolicytype'
    mock_selinux_enabled = 'selinux enabled'
    mock_security_getenforce = 'security getenforce'

# Generated at 2022-06-13 03:24:49.788871
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    mock_module = Mock()
    mock_facts = {'selinux_python_present': True, 'selinux': {'status': 'enabled', 'policyvers': '123', 'config_mode': 'enforcing', 'mode': 'enforcing', 'type': 'targeted'}}
    collector = SelinuxFactCollector()
    collected_facts = collector.collect(mock_module, mock_facts)
    assert collected_facts == {'selinux_python_present': True, 'selinux': {'status': 'enabled', 'policyvers': '123', 'config_mode': 'enforcing', 'mode': 'enforcing', 'type': 'targeted'}}


# Generated at 2022-06-13 03:24:54.312821
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    module = None
    collected_facts = None

    collector = SelinuxFactCollector
    mode = collector.collect(module=module, collected_facts=collected_facts)

    assert type(mode) is dict
    assert 'selinux_python_present' in mode
    assert 'selinux' in mode

    if mode['selinux_python_present'] is True:
        assert 'status' in mode['selinux']
        assert 'mode' in mode['selinux']
        assert 'type' in mode['selinux']
        assert 'config_mode' in mode['selinux']
        assert 'policyvers' in mode['selinux']

# Generated at 2022-06-13 03:24:56.364312
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    sp = SelinuxFactCollector()
    assert sp.name == 'selinux'

# Generated at 2022-06-13 03:25:00.429917
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_test = SelinuxFactCollector()
    result = selinux_test.collect()
    assert result.keys() == {'selinux', 'selinux_python_present'}
    assert result['selinux'] == {'status': 'disabled'}

# Generated at 2022-06-13 03:25:03.559786
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.name == 'selinux'
    assert selinux_fact_collector._fact_ids == set()

# Generated at 2022-06-13 03:25:04.725754
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    SelinuxFactCollector().collect()

# Generated at 2022-06-13 03:25:06.837981
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    assert SelinuxFactCollector.name == 'selinux'
    assert SelinuxFactCollector._fact_ids == set()


# Generated at 2022-06-13 03:25:09.864201
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    Selinux_fact_collector = SelinuxFactCollector()
    # No errors should be raised
    Selinux_fact_collector.collect()

# Generated at 2022-06-13 03:25:19.315281
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    from ansible.module_utils.facts import collector
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.facts.collectors import selinux
    test_class = collector.create_collector('selinux')
    obj = test_class()
    res = obj.collect()
    assert isinstance(res, dict)
    assert 'selinux' in res
    assert 'policyvers' in res['selinux']
    assert 'config_mode' in res['selinux']
    assert 'mode' in res['selinux']
    assert 'type' in res['selinux']
    assert 'status' in res['selinux']

# Generated at 2022-06-13 03:25:47.754833
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_collector = SelinuxFactCollector()
    # Mock selinux.is_selinux_enabled() to return True
    selinux_collector.is_selinux_enabled = lambda: True
    # Mock selinux.security_policyvers() to return '24'
    selinux_collector.security_policyvers = lambda: 24
    # Mock selinux.selinux_getenforcemode() to return (0, 1)
    selinux_collector.selinux_getenforcemode = lambda: (0, 1)
    # Mock selinux.security_getenforce() to return 1
    selinux_collector.security_getenforce = lambda: 1
    # Mock selinux.selinux_getpolicytype() to return (0, 'targeted')
    selinux_collector.selinux

# Generated at 2022-06-13 03:25:55.181155
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    from ansible.module_utils.facts.collector import FactsCollector
    from ansible.module_utils.facts.collector.selinux import SelinuxFactCollector
    tester = SelinuxFactCollector()
    assert isinstance(tester, SelinuxFactCollector)
    assert isinstance(tester, BaseFactCollector)
    assert tester.name == 'selinux'

# Generated at 2022-06-13 03:25:56.594079
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    pass

# vim: expandtab tabstop=4 shiftwidth=4

# Generated at 2022-06-13 03:25:58.276024
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    fact_collector = SelinuxFactCollector()
    assert fact_collector.collect()

# Generated at 2022-06-13 03:26:00.281114
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.name == 'selinux'


# Generated at 2022-06-13 03:26:09.266352
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # Create a dummy AnsibleModule instance and call the collect method of the class
    # SelinuxFactCollector.
    import ansible.module_utils.facts.collector
    import ansible.module_utils.facts.cache
    class DummyAnsibleModule:
        def __init__(self):
            self.params = {}
        def fail_json(self, msg):
            import sys
            sys.exit(1)
        def exit_json(self, data=None, **kwargs):
            import sys
            sys.exit(0)
    ansible_module_instance = DummyAnsibleModule()
    facts_cache_instance = ansible.module_utils.facts.cache.FactCache(ansible_module_instance)
    collector_instance = ansible.module_utils.facts.collector.get_collector

# Generated at 2022-06-13 03:26:15.679441
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # Monkeypatching selinux.is_selinux_enabled method to return True
    selinux.is_selinux_enabled = lambda: True
    # Monkeypatching selinux.security_policyvers() method to return a valid policy version
    policy_ver = '28'
    selinux.security_policyvers = lambda: policy_ver
    # Monkeypatching selinux.selinux_getenforcemode() method to return a valid mode
    selinux.selinux_getenforcemode = lambda: (0, 1)
    # Monkeypatching selinux.security_getenforce() method to return a valid mode
    selinux.security_getenforce = lambda: 1
    # Monkeypatching selinux.selinux_getpolicytype() method to return a valid policy type
    policy_type = 'targeted'

# Generated at 2022-06-13 03:26:24.829947
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    import sys
    if sys.version_info[0] < 3:
        from mock import Mock, patch
    else:
        from unittest.mock import Mock, patch

    from ansible.module_utils.facts.collector import BaseFactCollector

    with patch("ansible.module_utils.compat.selinux.is_selinux_enabled") as mock_is_selinux_enabled:
        mock_is_selinux_enabled.return_value = True

        with patch("ansible.module_utils.compat.selinux.security_policyvers") as mock_security_policyvers:
            mock_security_policyvers.return_value = 123456


# Generated at 2022-06-13 03:26:32.023638
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    module = None
    collected_facts = {'selinux': {}}

    expected_gather_subset = {
        "selinux": {
            "config_mode": "unknown",
            "mode": "unknown",
            "status": "enabled",
            "type": "unknown"
        }
    }

    result = SelinuxFactCollector.collect(module, collected_facts)
    assert result == expected_gather_subset

# Generated at 2022-06-13 03:26:43.539027
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_collector = SelinuxFactCollector()

    # Set mock values for Python library
    selinux_collector.module = MagicMock()
    selinux_collector.module.run_command.return_value = 0
    selinux_collector.module.run_command.return_value = "SELinux status: enabled"

    # Return valid valyes for the selinux Python library
    selinux.is_selinux_enabled.return_value = True
    selinux.selinux_getenforcemode.return_value = (0, 1)

    selinux.security_policyvers.return_value = 28
    selinux.security_getenforce.return_value = 1
    selinux.selinux_getpolicytype.return_value = (0, 'targeted')

    # Execute method collect

# Generated at 2022-06-13 03:27:06.125008
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # Mock selinux library
    mock_selinux = MockSelinuxModule()
    mock_selinux.is_selinux_enabled.return_value = True
    with patch.dict('sys.modules', {'selinux': mock_selinux}):
        selinux_fact_collector = SelinuxFactCollector()
        result = selinux_fact_collector.collect()
        assert 'selinux' in result
        assert 'selinux_python_present' in result
        assert 'status' in result['selinux']
        assert 'config_mode' in result['selinux']
        assert 'mode' in result['selinux']
        assert 'type' in result['selinux']
        assert 'policyvers' in result['selinux']

        # Mock that selinux is not enabled on

# Generated at 2022-06-13 03:27:18.617579
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():

    # Set the selinux library to None
    setattr(selinux, '__file__', None)

    # Test if we have the selinux library
    selinux_present = HAVE_SELINUX

    # Construct a class for the test
    class TestCollector(SelinuxFactCollector):
        name = 'test_collect'

    # Test if we have the selinux library
    if selinux_present:
        if not selinux.is_selinux_enabled():
            # If we have the selinux library but SELinux is disabled, return the expected
            # facts dictionary with 'status' set to "disabled"
            test_collector = TestCollector()

            facts = test_collector.collect()
            assert facts['selinux']['status'] == 'disabled'

# Generated at 2022-06-13 03:27:21.090338
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_collector = SelinuxFactCollector()
    assert selinux_collector.name == 'selinux'


# Generated at 2022-06-13 03:27:31.030135
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    """
    Create a fake module object with just enough attributes to satisfy above
    code, and invoke the collect method
    """
    module = MagicMock()
    collected_facts = {}
    selinux_fact_collector = SelinuxFactCollector()
    result = selinux_fact_collector.collect(module=module, collected_facts=collected_facts)
    selinux_facts = result['selinux']

    assert selinux_fact_collector.name == 'selinux'
    assert selinux_facts['status'] == 'disabled'
    assert selinux_facts['policyvers'] == 'unknown'
    assert selinux_facts['config_mode'] == 'unknown'
    assert selinux_facts['mode'] == 'unknown'
    assert selinux_facts['type'] == 'unknown'

# Generated at 2022-06-13 03:27:36.193387
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    from ansible.module_utils.facts.collector import Collector
    c = SelinuxFactCollector()
    assert c.name == 'selinux'
    assert c.collector == 'SelinuxFactCollector'
    assert c.requirements == 'selinux'
    assert c._fact_ids == set()

# Generated at 2022-06-13 03:27:46.586993
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    from ansible.module_utils.facts.collector.selinux import SelinuxFactCollector
    from ansible.module_utils.facts.collector.base import BaseFactCollector

    import sys

    # selinux Python library is not installed
    if 'selinux' not in sys.modules:
        facts_dict = {
            'selinux': {
                'status': 'Missing selinux Python library',
                'config_mode': 'unknown',
                'mode': 'unknown',
                'type': 'unknown'
            },
            'selinux_python_present': False
        }

        # Instantiate the collector

        # Mock the selinux module and set the is_selinux_enabled method to return False
        import ansible.module_utils.selinux

# Generated at 2022-06-13 03:27:48.099283
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    tf = SelinuxFactCollector()
    assert tf.name == 'selinux'

# Generated at 2022-06-13 03:27:48.979424
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    SelinuxFactCollector()

# Generated at 2022-06-13 03:27:51.584028
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.name == 'selinux'
    assert selinux_fact_collector._fact_ids == set()


# Generated at 2022-06-13 03:27:56.733650
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    import pytest

    selinux_facts = SelinuxFactCollector().collect()

    # Selinux Python library should always be present
    assert selinux_facts['selinux_python_present']

    if not selinux_facts['selinux']['status'] == "disabled":
        assert selinux_facts['selinux']['status'] == 'enabled'
        assert selinux_facts['selinux']['mode'] != 'unknown'
        assert selinux_facts['selinux']['type'] != 'unknown'
        assert selinux_facts['selinux']['config_mode'] != 'unknown'
        assert selinux_facts['selinux']['policyvers'] != 'unknown'

# Generated at 2022-06-13 03:28:47.012528
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.name == 'selinux'
    assert selinux_fact_collector._fact_ids == set()


# Generated at 2022-06-13 03:28:48.177216
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()


# Generated at 2022-06-13 03:28:50.076114
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.name == 'selinux'


# Generated at 2022-06-13 03:28:59.885024
# Unit test for method collect of class SelinuxFactCollector

# Generated at 2022-06-13 03:29:01.772993
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    sc = SelinuxFactCollector()
    assert sc.name == 'selinux'
    assert sc._fact_ids == set([])


# Generated at 2022-06-13 03:29:04.349356
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fc = SelinuxFactCollector()
    assert selinux_fc.name == 'selinux'
    assert isinstance(selinux_fc._fact_ids, set)

# Generated at 2022-06-13 03:29:05.864121
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    SelinuxFactCollector().collect()

# Generated at 2022-06-13 03:29:14.371303
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    """Verify the method collect works with expected values"""
    collector = SelinuxFactCollector()
    result = collector.collect(module=None, collected_facts=None)
    assert result['selinux_python_present'] == True
    assert result['selinux']['status'] == 'disabled'
    assert result['selinux']['policyvers'] == 'unknown'
    assert result['selinux']['config_mode'] == 'unknown'
    assert result['selinux']['mode'] == 'unknown'
    assert result['selinux']['type'] == 'unknown'

# Generated at 2022-06-13 03:29:15.163917
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    SelinuxFactCollector()

# Generated at 2022-06-13 03:29:17.362150
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    SELINUX_FACT_COLLECTOR = SelinuxFactCollector()
    assert SELINUX_FACT_COLLECTOR.name == 'selinux'


# Generated at 2022-06-13 03:30:42.324891
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux = SelinuxFactCollector()
    collected_facts = {}
    collected_facts['ansible_selinux_python_present'] = False

    selinux_facts = {}
    selinux_facts['status'] = 'Missing selinux Python library'
    collected_facts['selinux'] = selinux_facts

    assert selinux.collect(collected_facts=collected_facts) == collected_facts

# Generated at 2022-06-13 03:30:51.756175
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_fc = SelinuxFactCollector()
    selinux_facts = selinux_fc.collect()
    selinux_fact_keys = {'selinux', 'selinux_python_present'}

    assert isinstance(selinux_facts, dict)
    assert isinstance(selinux_facts['selinux'], dict)
    assert selinux_fact_keys == set(selinux_facts)
    assert isinstance(selinux_facts['selinux_python_present'], bool)
    assert isinstance(selinux_facts['selinux']['status'], str)
    assert isinstance(selinux_facts['selinux']['policyvers'], str)
    assert isinstance(selinux_facts['selinux']['config_mode'], str)


# Generated at 2022-06-13 03:30:55.733036
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    try:
        module_obj = type('', (object,), {'exit_json': lambda self, vars: None, 'selinux': selinux})()
    except NameError:
        module_obj = None

    src = SelinuxFactCollector(module=module_obj, collected_facts={})
    result = src.collect()

    assert 'selinux_python_present' in result
    assert 'selinux' in result

    if result['selinux_python_present']:
        assert 'status' in result['selinux']

        if result['selinux']['status'] == 'enabled':
            assert 'policyvers' in result['selinux']
            assert 'config_mode' in result['selinux']
            assert 'mode' in result['selinux']

# Generated at 2022-06-13 03:30:56.635852
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    SelinuxFactCollector()


# Generated at 2022-06-13 03:30:58.938952
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_facts = SelinuxFactCollector()
    assert selinux_facts.name == 'selinux'
    assert selinux_facts._fact_ids == {'selinux'}

# Generated at 2022-06-13 03:31:03.542667
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    obj = SelinuxFactCollector()
    assert obj.name == 'selinux'
    assert obj._fact_ids == set()

    with open('/sys/fs/selinux/enforce', 'r') as f:
        mode = f.read().split()[0]

    if mode == '1':
        assert mode == '1'
        assert HAVE_SELINUX
    else:
        assert mode == '0'
        assert not HAVE_SELINUX

# Generated at 2022-06-13 03:31:07.442075
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    """
    Unit test for method collect of class SelinuxFactCollector
    """
    # Create class instance of class SelinuxFactCollector
    selinux_fact_collector = SelinuxFactCollector()
    # Assert method collect returns a dictionary
    assert isinstance(selinux_fact_collector.collect(), dict)

# Generated at 2022-06-13 03:31:09.021553
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_facts = SelinuxFactCollector()
    assert selinux_facts is not None
    assert selinux_facts.name == 'selinux'

# Generated at 2022-06-13 03:31:09.740080
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    SelinuxFactCollector().collect()

# Generated at 2022-06-13 03:31:13.200758
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    fact_collector = SelinuxFactCollector()
    collected_facts = fact_collector.collect()

    assert 'selinux_python_present' in collected_facts
    assert 'selinux' in collected_facts

    status = collected_facts['selinux']['status']
    assert (status == 'enabled' or status == 'disabled' or status == 'Missing selinux Python library')