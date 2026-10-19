

# Generated at 2022-06-13 03:22:53.515003
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
  def test_selinux_python_present_is_false():
      selinux_fact_collector = SelinuxFactCollector()

      assert selinux_fact_collector.name == 'selinux'

# Generated at 2022-06-13 03:22:59.000734
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector is not None
    facts_dict = selinux_fact_collector.collect()
    assert 'selinux' in facts_dict
    assert 'status' in facts_dict['selinux']
    assert 'selinux_python_present' in facts_dict

# Generated at 2022-06-13 03:23:00.733190
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_facts = SelinuxFactCollector()
    # Asserts for class instantiation
    assert selinux_facts is not None
    assert selinux_facts.name == 'selinux'
    assert 'selinux' in selinux_facts._fact_ids

# Generated at 2022-06-13 03:23:10.002159
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    from ansible.module_utils.facts.collector import module_cache
    from ansible.module_utils.facts.collector import FactsCache
    from ansible.module_utils.facts.collector import get_file_content
    from ansible.module_utils.facts.collector import cache_valid
    from ansible.module_utils.facts.collector import BaseFactCollector

    import os
    import sys

    class MockModuleCache(FactsCache):
        """
        Mock class to replace module_cache class
        """
        def __init__(self, module_name, timeout, cache=True, module_path=None):
            self._module_name = module_name
            self._module_path = module_path
            self._timeout = timeout


# Generated at 2022-06-13 03:23:19.034657
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    """
    Test method collect of class SelinuxFactCollector - it should return
    a dictionary with facts related to selinux.
    """
    selinux_dict = {'config_mode': 'permissive',
                    'mode': 'permissive',
                    'policyvers': 28,
                    'status': 'enabled',
                    'type': 'targeted'}

    # Set up the import of selinux to return the test selinux_dict
    # Also set up the import of is_selinux_enabled to return True
    import ansible.module_utils.facts.system.selinux as selinux
    def mock_is_selinux_enabled():
        return True
    selinux.is_selinux_enabled = mock_is_selinux_enabled


# Generated at 2022-06-13 03:23:27.016179
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_module = SelinuxFactCollector()

    # If selinux library is missing, only set the status and selinux_python_present since
    # there is no way to tell if SELinux is enabled or disabled on the system
    # without the library.
    if not HAVE_SELINUX:
        assert selinux_module.collect() == {"selinux": {"status": "Missing selinux Python library"}, "selinux_python_present": False}

    # Set a boolean for testing whether the Python library is present
    assert selinux_module.collect()["selinux_python_present"] == True

    # use selinux library to get selinux facts

# Generated at 2022-06-13 03:23:34.587761
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    import sys
    sys.modules['selinux'] = __import__('ansible.module_utils.compat.mock.selinux')
    from ansible.module_utils.compat.mock.selinux import (is_selinux_enabled, selinux_getenforcemode,
                                                          selinux_getpolicytype, security_policyvers,
                                                          security_getenforce)

    fact_collector = SelinuxFactCollector()

    is_selinux_enabled.return_value = True
    selinux_getenforcemode.return_value = (0, 1)
    selinux_getpolicytype.return_value = (0, 'targeted')
    security_policyvers.return_value = 29
    security_getenforce.return_value = 1

    # Test case:

# Generated at 2022-06-13 03:23:36.170421
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    obj = SelinuxFactCollector()
    assert obj.name == 'selinux'

# Generated at 2022-06-13 03:23:37.226308
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    SelinuxFactCollector()

# Generated at 2022-06-13 03:23:39.481394
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    x = SelinuxFactCollector()
    assert x


# Generated at 2022-06-13 03:23:45.564717
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    se = SelinuxFactCollector()
    assert se.name == 'selinux'

# Generated at 2022-06-13 03:23:56.486352
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():

    # Declare a mock for the function selinux.is_selinux_enabled
    def mock(self):
        return True

    # Declare a mock for the function selinux.security_policyvers
    def mock_policyvers(self):
        return '1'

    # Declare a mock for the function selinux.selinux_getenforcemode
    def mock_enforcemode(self):
        return (0, 1)

    # Declare a mock for the function selinux.security_getenforce
    def mock_enforce(self):
        return 1

    # Declare a mock for the function selinux.selinux_getpolicytype
    def mock_policytype(self):
        return (0, 'targeted')

    # Create a SelinuxFactCollector object
    x = SelinuxFactCollector()



# Generated at 2022-06-13 03:24:06.024101
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    import os
    import tempfile
    try:
        facts_dir = tempfile.mkdtemp(dir='/tmp',prefix="ansible_test_facts")
        facts_file = os.path.join(facts_dir, 'facts.d')
        fact = SelinuxFactCollector(facts_file)
        assert fact.name == 'selinux'
        assert fact._fact_ids == set()
        assert fact.collect() == {'selinux':{'status': 'Missing selinux Python library'}, 'selinux_python_present': False}
    finally:
        os.rmdir(facts_dir)


# Generated at 2022-06-13 03:24:07.147803
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    o = SelinuxFactCollector()

# Generated at 2022-06-13 03:24:08.410033
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    x = SelinuxFactCollector()
    assert x.name == 'selinux'

# Generated at 2022-06-13 03:24:12.596446
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    collector = SelinuxFactCollector()
    facts = collector.collect()
    assert isinstance(facts, dict)
    assert 'selinux' in facts and isinstance(facts['selinux'], dict)
    for key in ['type', 'mode', 'policyvers', 'status']:
        assert key in facts['selinux']

# Generated at 2022-06-13 03:24:21.968394
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # Create a set to trigger the if statement in collect
    selinux_fact_ids = set()
    selinux_fact_ids.add('selinux')
    selinux_fact_ids.add('selinux_python_present')

    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector._fact_ids == selinux_fact_ids
    # Simulate a missing selinux Python library
    selinux_fact_collector.__dict__['HAVE_SELINUX'] = False
    selinux_facts = selinux_fact_collector.collect()
    assert selinux_facts['selinux']['status'] == 'Missing selinux Python library'
    assert selinux_facts['selinux_python_present'] == False

# Generated at 2022-06-13 03:24:24.784534
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    collected_facts = {}
    fact_collector = SelinuxFactCollector(None, collected_facts)
    assert fact_collector.name == 'selinux'
    assert fact_collector._fact_ids == set()


# Generated at 2022-06-13 03:24:26.924776
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    test_obj = SelinuxFactCollector(None)
    assert test_obj.name == 'selinux'
    assert len(test_obj._fact_ids) == 1

# Generated at 2022-06-13 03:24:31.092116
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact = SelinuxFactCollector()
    assert selinux_fact.name == 'selinux'
    assert selinux_fact._fact_ids == set()

# Generated at 2022-06-13 03:24:44.092271
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # create instance of class SelinuxFactCollector
    selinux_fact_collector = SelinuxFactCollector()

    # call collect method of class SelinuxFactCollector
    selinux_facts = selinux_fact_collector.collect()

    # print selinux_facts
    print(selinux_facts)



# Generated at 2022-06-13 03:24:47.331396
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.name == 'selinux'
    assert len(selinux_fact_collector._fact_ids) == 0


# Generated at 2022-06-13 03:24:58.975690
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    """
    Given a SelinuxFactCollector and the library selinux (which all the methods
    of SelinuxFactCollector are dependent on) when testing collect method of
    SelinuxFactCollector, then the selinux Python library is detected,
    the mode and type of selinux should be reported accordingly.
    For example,
    mode: enforcing
    type: targeted
    """

    # Create a dummy module object
    module = type('Module', (object,), {})

    # Mock out the selinux.is_selinux_enabled() method to return True
    selinux.is_selinux_enabled = lambda: True
    selinux.security_policyvers = lambda: "1.2.3.4"
    selinux.selinux_getenforcemode = lambda: (0, 1)
    selinux.security_get

# Generated at 2022-06-13 03:24:59.616723
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    instance = SelinuxFactCollector()
    assert instance.name == 'selinux'

# Generated at 2022-06-13 03:25:07.522282
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # Test collecting facts
    import ansible.module_utils.facts.collector

    # Instantiate the collector
    selinux_fc = SelinuxFactCollector()

    # Mock function selinux.is_selinux_enabled
    class mock_selinux():
        @staticmethod
        def is_selinux_enabled():
            return True

        @staticmethod
        def security_policyvers():
            return 2

        @staticmethod
        def selinux_getenforcemode():
            return 0,1

        @staticmethod
        def security_getenforce():
            return 1

        @staticmethod
        def selinux_getpolicytype():
            return 0, 'targeted'

    ansible.module_utils.facts.collector.selinux = mock_selinux

    # Collect the facts
    facts_dict

# Generated at 2022-06-13 03:25:11.564369
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    obj = SelinuxFactCollector()
    assert obj.name == 'selinux'
    assert list(obj._fact_ids) == []


# Generated at 2022-06-13 03:25:21.395872
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # Initialize a SelinuxFactCollector object
    selinux_facts = SelinuxFactCollector()
    # Collect facts
    facts = selinux_facts.collect()

    # Assert the required facts selinux_python_present and selinux are present
    assert isinstance(facts, dict)
    assert 'selinux_python_present' in facts
    assert 'selinux' in facts
    assert isinstance(facts['selinux'], dict)

    # Assert that if selinux Python library is missing, then only selinux_python_present
    # is present and status of selinux is set to 'Missing selinux Python library'
    selinux_facts._have_selinux = False
    facts = selinux_facts.collect()
    assert 'selinux_python_present' in facts
    assert 'selinux'

# Generated at 2022-06-13 03:25:24.279055
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact = SelinuxFactCollector()
    assert selinux_fact.name == 'selinux'

# Generated at 2022-06-13 03:25:28.837668
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_collector = SelinuxFactCollector()
    assert selinux_collector.name == 'selinux'
    assert set(selinux_collector._fact_ids) == set(['selinux', 'selinux_python_present'])

# Generated at 2022-06-13 03:25:31.003740
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    fact = SelinuxFactCollector()
    result = fact.collect()
    assert result != {}

# Generated at 2022-06-13 03:25:59.643258
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    class _module(object):
        def get_bin_path(self, module, opt_dirs=[]):
            return 'semanage'

        def get_distribution(self):
            return 'CentOS'

    facts_dict = SelinuxFactCollector(_module()).collect()

    assert isinstance(facts_dict, dict) and 'selinux' in facts_dict
    assert 'status' in facts_dict['selinux']
    assert 'selinux_python_present' in facts_dict
    assert 'policyvers' in facts_dict['selinux']
    assert 'config_mode' in facts_dict['selinux']
    assert 'mode' in facts_dict['selinux']
    assert 'type' in facts_dict['selinux']

# Generated at 2022-06-13 03:26:09.105754
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    module = None
    collected_facts = None
    selinux_fact_collector = SelinuxFactCollector()
    # Test with the selinux module not present.
    facts_dict = selinux_fact_collector.collect(module, collected_facts)
    assert facts_dict['selinux_python_present'] == False
    assert facts_dict['selinux'] == {'status': 'Missing selinux Python library'}

    # Test with the selinux module present
    selinux_fact_collector._collect_from_file = lambda x: True
    facts_dict = selinux_fact_collector.collect(module, collected_facts)
    assert facts_dict['selinux_python_present'] == True

# Generated at 2022-06-13 03:26:15.590540
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    from ansible.module_utils.facts.collector import Collectors
    collector = Collectors['ansible.module_utils.selinux_python'].collector
    # Return values for selinux (mocked)
    def security_policyvers():
        return '20180325'

    def is_selinux_enabled():
        return True

    def selinux_getpolicytype():
        return (0, 'mock')

    def selinux_getenforcemode():
        return (0, 1)

    def security_getenforce():
        return 1

    # Patch selinux
    mocker = Mocker()
    selinux = mocker.replace("ansible.module_utils.selinux_python")
    selinux.is_selinux_enabled = is_selinux_enabled
    selinux.security_policy

# Generated at 2022-06-13 03:26:17.091736
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    '''No way to test this module except mocking the selinux binary
    '''
    pass

# Generated at 2022-06-13 03:26:21.058451
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    collector = SelinuxFactCollector()
    facts = collector.collect(module=None, collected_facts=None)['selinux']

    assert 'status' in facts
    assert 'mode' in facts
    assert 'policyvers' in facts
    assert 'type' in facts
    assert 'config_mode' in facts

# Generated at 2022-06-13 03:26:22.576098
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_collector = SelinuxFactCollector()
    assert selinux_collector.name == 'selinux'

# Generated at 2022-06-13 03:26:24.424188
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    assert SelinuxFactCollector().collect() == {'selinux': {'status': 'disabled'}, 'selinux_python_present': True}

# Generated at 2022-06-13 03:26:26.503583
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    x = SelinuxFactCollector()
    assert x.name == 'selinux'
    assert x._fact_ids == {'selinux', 'selinux_python_present'}

# Generated at 2022-06-13 03:26:28.595158
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact = SelinuxFactCollector()
    assert selinux_fact.name == 'selinux'

# Generated at 2022-06-13 03:26:37.086173
# Unit test for method collect of class SelinuxFactCollector

# Generated at 2022-06-13 03:27:23.474600
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    from ansible.module_utils.facts.collector import fetch_file_if_needed
    from ansible.module_utils.facts.hardware.selinux import SelinuxFactCollector
    # create a fact collector object
    c = SelinuxFactCollector()

    # mock the selinux module
    import sys
    if sys.version_info[0] < 3:
        built_in_module = '__builtin__'
    else:
        built_in_module = 'builtins'
    import mock
    selinux_mock = mock.MagicMock()
    sys.modules['selinux'] = selinux_mock
    sys.modules[built_in_module].__import__.return_value = selinux_mock
    # mock selinux.is_selinux_enabled()
    selinux

# Generated at 2022-06-13 03:27:25.219130
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    assert SelinuxFactCollector.name == 'selinux'

# Generated at 2022-06-13 03:27:30.090215
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    collected_facts = {'selinux_python_present': True}
    selinux_fact_collector = SelinuxFactCollector(None)
    selinux_facts = selinux_fact_collector.collect(collected_facts)
    assert isinstance(selinux_facts, dict)
    assert selinux_facts['selinux_python_present']

# Generated at 2022-06-13 03:27:39.072622
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    """Unit test for method collect of class SelinuxFactCollector

    """
    # Create an instance of the class we want to test
    test_obj = SelinuxFactCollector()

    # Get facts
    ansible_facts = test_obj.collect()

    # The following checks assume the selinux module is not installed
    assert 'selinux' in ansible_facts
    assert 'status' in ansible_facts['selinux']
    assert ansible_facts['selinux']['status'] == 'Missing selinux Python library'
    assert ansible_facts['selinux_python_present'] == False



# Generated at 2022-06-13 03:27:40.900608
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_facts = SelinuxFactCollector()
    assert selinux_facts.name == 'selinux'

# Generated at 2022-06-13 03:27:44.821009
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.name == 'selinux'
    assert selinux_fact_collector._fact_ids == set()


# Generated at 2022-06-13 03:27:46.634373
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinuxFactCollector = SelinuxFactCollector()
    selinuxFactCollector.collect()

# Generated at 2022-06-13 03:27:47.807455
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    SelinuxFactCollector()

# Generated at 2022-06-13 03:27:49.021163
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    mod = SelinuxFactCollector()
    assert mod.name == 'selinux'

# Generated at 2022-06-13 03:27:50.426338
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    my_obj = SelinuxFactCollector()
    assert my_obj.name == 'selinux'

# Generated at 2022-06-13 03:29:26.322050
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()

    assert selinux_fact_collector
    assert selinux_fact_collector.name == 'selinux'

# Generated at 2022-06-13 03:29:30.924153
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_fact_collector = SelinuxFactCollector()
    # selinux facts exist
    selinux_fact_collector.collect = lambda: None
    assert selinux_fact_collector.collect() is None
    # selinux facts don't exist
    selinux_fact_collector.collect = lambda: {'selinux': {'status': 'disabled'}}
    assert selinux_fact_collector.collect() == {'selinux': {'status': 'disabled'}}

# Generated at 2022-06-13 03:29:31.535549
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    SelinuxFactCollector()

# Generated at 2022-06-13 03:29:33.773317
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    assert isinstance(SelinuxFactCollector(), SelinuxFactCollector)

# Generated at 2022-06-13 03:29:44.059261
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector, Collector
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts import timeout

    collector._set_timeout = timeout.set_fact_collector_timeout

    tested_object = SelinuxFactCollector()

    def mock_is_selinux_enabled():
        return True
    selinux.is_selinux_enabled = mock_is_selinux_enabled

    def mock_security_policyvers():
        return 0
    selinux.security_policyvers = mock_security_policyvers

    def mock_selinux_getenforcemode():
        return (0, 1)
    selinux.selinux_getenforcemode = mock_selinux_getenforcemode


# Generated at 2022-06-13 03:29:46.023971
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    sfc = SelinuxFactCollector()
    assert sfc._fact_ids == set(['selinux'])

# Generated at 2022-06-13 03:29:49.917353
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinuxfact_collector = SelinuxFactCollector()
    assert selinuxfact_collector.name == 'selinux'
    assert isinstance(selinuxfact_collector._fact_ids, set)
    assert selinuxfact_collector._fact_ids == set()


# Generated at 2022-06-13 03:29:54.161893
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    module = type('', (), {})
    collected_facts = None
    expected_dict = {'selinux': {'status': 'Missing selinux Python library'},
                     'selinux_python_present': False}
    selinux_fact_collector = SelinuxFactCollector()
    actual_dict = selinux_fact_collector.collect(module, collected_facts)
    assert actual_dict == expected_dict


# Generated at 2022-06-13 03:29:55.437703
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    x = SelinuxFactCollector()
    assert x
    assert x.name == 'selinux'
    assert x._fact_ids == set()

# Generated at 2022-06-13 03:30:05.155663
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # Test for selinux python library present and selinux enabled
    mod = DictModule()
    mod.fail_json = DictFailJson()
    selinux_facts = SelinuxFactCollector().collect(module=mod, collected_facts={})
    assert 'selinux_python_present' in selinux_facts
    assert 'selinux' in selinux_facts
    assert selinux_facts['selinux_python_present']

    # Test for selinux python library present but selinux not enabled
    mod.IS_SELINUX_ENABLED = False
    selinux_facts = SelinuxFactCollector().collect(module=mod, collected_facts={})
    assert 'selinux_python_present' in selinux_facts
    assert 'selinux' in selinux_facts
    assert selinux_facts