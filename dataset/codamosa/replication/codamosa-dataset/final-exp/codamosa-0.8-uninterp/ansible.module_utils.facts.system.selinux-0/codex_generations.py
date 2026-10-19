

# Generated at 2022-06-13 03:22:57.283101
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    obj = SelinuxFactCollector()
    assert 'selinux' == obj.name
    assert not obj._fact_ids
    assert obj.collect() == {'selinux': {'status': 'Missing selinux Python library'}, 'selinux_python_present': False}

# Generated at 2022-06-13 03:23:07.436525
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():

    import platform
    import types

    from ansible.module_utils.compat import selinux
    from ansible.module_utils.facts.collector import BaseFactCollector

    def test_getenforce():
        return 1

    def test_selinux_getenforcemode():
        return (0, 1)

    def test_selinux_getpolicytype():
        return (0, 'refpolicy')

    def test_is_selinux_enabled():
        return True

    def test_security_getenforce():
        return 1

    def test_security_policyvers():
        return 28

    def test_selinux_getpolicytype():
        return (0, 'refpolicy')

    def test_security_policyvers():
        return 28

    # Setup a mock selinux module to enable testing

# Generated at 2022-06-13 03:23:12.123782
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # create instance of class SelinuxFactCollector
    selinux_fact_collector = SelinuxFactCollector()
    # call method collect of class SelinuxFactCollector
    collected_facts = selinux_fact_collector.collect()
    # validate collected facts
    assert 'selinux' in collected_facts

# Generated at 2022-06-13 03:23:20.250161
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    # Call the constructor of class SelinuxFactCollector and test its attributes
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.name == 'selinux'
    assert selinux_fact_collector._fact_ids == set()

    # Call the constructor of class SelinuxFactCollector and test its attributes
    selinux_fact_collector_with_args = SelinuxFactCollector(name="selinux", fact_ids=set())
    assert selinux_fact_collector_with_args.name == 'selinux'
    assert selinux_fact_collector_with_args._fact_ids == set()

    # Check the equality of the two above constructors which should be equal
    assert selinux_fact_collector == selinux_fact_collector_with

# Generated at 2022-06-13 03:23:21.532893
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    s = SelinuxFactCollector()
    assert s.name == 'selinux'


# Generated at 2022-06-13 03:23:27.602270
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():

    # Data for asserting the results
    mock_selinux_facts = dict(
        status = 'enabled',
        policyvers = 'unknown',
        config_mode = 'unknown',
        mode = 'unknown',
        type = 'unknown'
    )
    mock_facts_dict = dict(
        selinux_python_present = True,
        selinux = mock_selinux_facts
    )

    # Create a test class
    mock_collector = SelinuxFactCollector()

    # Create mock arguments for collect method
    mock_args = dict()

    # Call the collect method and assert the result
    assert mock_collector.collect(mock_args) == mock_facts_dict

# Generated at 2022-06-13 03:23:32.422191
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    module = DummyModule()
    # Dummy method for setting ansible module args
    def dummy_ansible_get_sub_option(name, fact_name, fact_default):
        if fact_name == 'selinux_python_present':
            if HAVE_SELINUX:
                return True
            else:
                return False
        else:
            return None

    module.ansible_get_sub_option = dummy_ansible_get_sub_option
    facts_dict = SelinuxFactCollector().collect(module)
    assert 'selinux' in facts_dict
    assert 'selinux_python_present' in facts_dict
    assert isinstance(facts_dict['selinux_python_present'], bool)


# Generated at 2022-06-13 03:23:44.532745
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    import os

    import ansible.module_utils.facts.collector
    import ansible.module_utils.facts.system.selinux

    from ansible.module_utils.facts.system.selinux import SelinuxFactCollector

    # We need to mock these two functions so the real library is not called
    os.environ['SELINUX_INIT'] = 'True'
    os.environ['SELINUX_STATE'] = '1'

    def mock_selinux_is_selinux_enabled():
        return True

    def mock_selinux_getenforcemode():
        return (0, 1)

    def mock_selinux_security_getenforce():
        return 1

    def mock_selinux_getpolicytype():
        return (0, 'targeted')

   

# Generated at 2022-06-13 03:23:55.715404
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    '''
    Unit test for method collect of class SelinuxFactCollector.
    '''
    # Set up patch for selinux.is_selinux_enabled
    mocked_is_selinux_enabled = MagicMock(return_value=False)
    mocked_is_selinux_enabled.side_effect = [True, False]
    selinux.is_selinux_enabled = mocked_is_selinux_enabled

    # Set up patch for selinux.selinux_getenforcemode
    mocked_selinux_getenforcemode = MagicMock(return_value=(0, 0))

# Generated at 2022-06-13 03:23:58.381564
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux = SelinuxFactCollector()
    assert selinux.name == 'selinux'

# Generated at 2022-06-13 03:24:08.502333
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    # Initialize an object of class SelinuxFactCollector
    sef = SelinuxFactCollector()

    # Test that the name of class SelinuxFactCollector is correctly assigned to instance attribute
    assert sef.name == 'selinux'

    # Test that the set of fact names for class SelinuxFactCollector is correctly
    # assigned to instance attribute
    assert sef._fact_ids == set()



# Generated at 2022-06-13 03:24:09.083830
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    pass

# Generated at 2022-06-13 03:24:11.211829
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert isinstance(selinux_fact_collector, SelinuxFactCollector)

# Generated at 2022-06-13 03:24:19.780622
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    collected_facts = dict()
    fake_module = None
    selinux_fact_collector = SelinuxFactCollector()
    ret = selinux_fact_collector.collect(fake_module, collected_facts)
    assert ret['selinux']['status'] == 'disabled'
    assert ret['selinux']['type'] == 'unknown'
    assert ret['selinux']['mode'] == 'unknown'
    assert ret['selinux']['config_mode'] == 'unknown'
    assert ret['selinux']['policyvers'] == 'unknown'
    assert ret['selinux_python_present'] == False

# Generated at 2022-06-13 03:24:22.696995
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_collector = SelinuxFactCollector()
    assert selinux_collector.name == 'selinux'
    assert selinux_collector._fact_ids == set()


# Generated at 2022-06-13 03:24:24.453799
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert isinstance(selinux_fact_collector, SelinuxFactCollector)

# Generated at 2022-06-13 03:24:27.111362
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.collect() == {
        'selinux_python_present': True,
        'selinux': {
            'status': 'Missing selinux Python library'
        }
    }

# Generated at 2022-06-13 03:24:31.554923
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_col = SelinuxFactCollector()
    assert selinux_fact_col.name == 'selinux'
    assert selinux_fact_col._fact_ids == set()

# Generated at 2022-06-13 03:24:40.465211
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    """Test that the SELinux fact collector can read the SELinux status and
    mode correctly.

    When the SELinux library is not installed, the collector should generate
    facts with 'missing selinux Python library' and selinux_python_present
    set to False.

    When the SELinux library is installed, the collector should generate facts
    with the status set to 'disabled' if SELinux is not present on the system,
    and 'enabled' if it is present. When SELinux is enabled, it should generate
    facts with the SELinux mode set to the mode if the mode can be read, and
    'unknown' if it cannot.

    """
    fact_collector = SelinuxFactCollector()
    facts = fact_collector.collect()
    assert 'selinux' in facts

# Generated at 2022-06-13 03:24:42.578669
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector is not None


# Generated at 2022-06-13 03:24:49.924223
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.name == 'selinux'

# Generated at 2022-06-13 03:25:02.206956
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    import sys
    # monkey patch selinux.is_selinux_enabled() to return True
    def is_selinux_enabled(*args, **kwargs):
        return True
    selinux.is_selinux_enabled = is_selinux_enabled
    # monkey patch selinux.security_policyvers() to return 1
    def security_policyvers(*args, **kwargs):
        return 1
    selinux.security_policyvers = security_policyvers
    # monkey patch selinux.selinux_getenforcemode() to return 0 and 1
    def selinux_getenforcemode(*args, **kwargs):
        return 0, 1
    selinux.selinux_getenforcemode = selinux_getenforcemode
    # monkey patch selinux.security_getenforce() to return 1

# Generated at 2022-06-13 03:25:10.226859
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    import sys
    from ansible_collections.ansible.community.tests.unit.compat.mock import MagicMock
    import ansible_collections.ansible.community.plugins.module_utils.facts.fact_collector # noqa: E402

    # Import module without selinux library
    sys.modules['selinux'] = None
    ansible_collections.ansible.community.plugins.module_utils.facts.fact_collector.HAVE_SELINUX = False # noqa: E501

    # Test with selinux not enabled
    selinux = MagicMock()
    selinux.is_selinux_enabled.return_value = False
    sys.modules['selinux'] = selinux
    module = AnsibleModule(argument_spec={})

# Generated at 2022-06-13 03:25:12.871726
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    sfc = SelinuxFactCollector()
    assert isinstance(sfc, SelinuxFactCollector)

# Generated at 2022-06-13 03:25:15.123418
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_collector = SelinuxFactCollector()
    assert selinux_collector.name == 'selinux'


# Generated at 2022-06-13 03:25:18.493390
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    obj_SelinuxFactCollector = SelinuxFactCollector()
    assert obj_SelinuxFactCollector.name == 'selinux'
    assert obj_SelinuxFactCollector._fact_ids == set()


# Generated at 2022-06-13 03:25:19.802174
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    assert SelinuxFactCollector().name == 'selinux'

# Generated at 2022-06-13 03:25:25.658798
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    """Test method collect of class SelinuxFactCollector to make sure it
    returns the correct SELinux facts.
    """
    import pytest
    import os

    # Test to make sure we get the correct facts when the selinux module
    # is available.
    if HAVE_SELINUX:
        test_selinux_facts = SelinuxFactCollector().collect()
        assert test_selinux_facts['selinux_python_present'] is True

        # Test to make sure we get the correct facts when SELinux is
        # disabled on the system.
        test_selinux_facts['selinux']['status'] = 'disabled'
        test_collect_selinux_facts = SelinuxFactCollector().collect()

# Generated at 2022-06-13 03:25:30.214524
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinuxFactCollector = SelinuxFactCollector()
    assert selinuxFactCollector.name == 'selinux'
    assert selinuxFactCollector._fact_ids == set()
    assert len(selinuxFactCollector._fact_ids) == 0


# Generated at 2022-06-13 03:25:40.983616
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    import sys
    import os
    import unittest
    from ansible.module_utils.facts.collectors.selinux import SelinuxFactCollector

    class TestSelinuxFactCollector(unittest.TestCase):
        def test_collect_selinux_disabled(self):
            """
            Test that if selinux.is_selinux_enabled() returns False, then
            selinux['status'] is set to disabled.
            """
            mock_selinux = sys.modules['ansible.module_utils.compat.selinux']
            mock_selinux.is_selinux_enabled = lambda: False
            mock_selinux.security_policyvers = lambda: None
            mock_selinux.selinux_getenforcemode = lambda: None
            mock_selinux.security

# Generated at 2022-06-13 03:25:59.494011
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    from ansible_collections.ansible.community.plugins.module_utils.facts.collectors.selinux import SelinuxFactCollector

    collected_facts = dict()
    selinux_collector = SelinuxFactCollector()
    facts = selinux_collector.collect(collected_facts=collected_facts)

    # In case selinux Python library is not present, only status and the status of the library
    # are present in the dict
    if not HAVE_SELINUX:
        assert 'selinux' not in facts
        assert 'selinux_python_present' not in facts
        assert facts['selinux_python_present'] == False

# Generated at 2022-06-13 03:26:06.677546
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_fact_collector = SelinuxFactCollector()
    ret = selinux_fact_collector.collect()

    assert 'selinux' in ret
    assert isinstance(ret['selinux'], dict)
    assert 'config_mode' in ret['selinux']
    assert 'mode' in ret['selinux']
    assert 'status' in ret['selinux']
    assert 'type' in ret['selinux']
    assert 'policyvers' in ret['selinux']
    assert 'selinux_python_present' in ret

# Generated at 2022-06-13 03:26:14.210831
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    # If selinux library is missing
    if not HAVE_SELINUX:
        selinux_fact_collector = SelinuxFactCollector()
        fact_dict = {}
        selinux_fact_collector.collect(collected_facts=fact_dict)
        # Check to see if fact_dict returns the correct data
        assert fact_dict['selinux_python_present'] == False
        assert fact_dict['selinux']['status'] == 'Missing selinux Python library'
    # If selinux library is present
    else:
        selinux_fact_collector = SelinuxFactCollector()
        fact_dict = {}
        selinux_fact_collector.collect(collected_facts=fact_dict)
        # Check to see if fact_dict returns the correct data

# Generated at 2022-06-13 03:26:16.198882
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    sfc = SelinuxFactCollector()
    assert sfc
    assert sfc.name == 'selinux'

# Generated at 2022-06-13 03:26:24.009645
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    fc = SelinuxFactCollector()
    collected_facts = {}
    fc.collect(collected_facts=collected_facts)
    assert collected_facts['selinux']['type'] == 'unknown'
    assert collected_facts['selinux']['mode'] == 'unknown'
    assert collected_facts['selinux']['config_mode'] == 'unknown'
    assert collected_facts['selinux']['status'] == 'Missing selinux Python library'
    assert collected_facts['selinux_python_present'] is False
    assert collected_facts['ansible_facts']['selinux'] == collected_facts['selinux']

# Generated at 2022-06-13 03:26:32.962686
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_collector = SelinuxFactCollector()

    selinux_facts = selinux_collector.collect()

    assert selinux_facts['selinux_python_present'] is True
    assert selinux_facts['selinux']['status'] == 'enabled'
    assert selinux_facts['selinux']['type'] == 'unknown'
    assert selinux_facts['selinux']['mode'] == 'unknown'
    assert selinux_facts['selinux']['config_mode'] == 'unknown'

# Generated at 2022-06-13 03:26:34.966716
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    collect = SelinuxFactCollector()
    assert isinstance(collect, SelinuxFactCollector)

# Generated at 2022-06-13 03:26:46.416873
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():

    class FakeModule(object):
        def __init__(self, params):
            self.params = params


    class FakeSelinux(object):
        def __init__(self, is_selinux_enabled=True,
                     security_policyvers=None,
                     selinux_getenforcemode=None,
                     security_getenforce=None,
                     selinux_getpolicytype=None):
            self.is_selinux_enabled = is_selinux_enabled
            self.security_policyvers = security_policyvers
            self.selinux_getenforcemode = selinux_getenforcemode
            self.security_getenforce = security_getenforce
            self.selinux_getpolicytype = selinux_getpolicytype

        def is_selinux_enabled(self):
            return self

# Generated at 2022-06-13 03:26:47.918531
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    obj = SelinuxFactCollector()
    assert obj.name == 'selinux'

# Generated at 2022-06-13 03:26:49.467863
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    x = SelinuxFactCollector()
    assert x.name == 'selinux'


# Generated at 2022-06-13 03:27:12.688861
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.name == 'selinux'
    assert selinux_fact_collector._fact_ids == set()

# Generated at 2022-06-13 03:27:23.686110
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector.selinux import SelinuxFactCollector

    # pseudo collector subclass for testing
    class TestCollector(BaseFactCollector):
        name = 'testcollector'
        _fact_ids = set()

        def __init__(self, module=None, collected_facts=None):
            self.test_dict = {}
            self.test_dict['test'] = 'test_fact'

        def collect(self, module=None, collected_facts=None):
            return self.test_dict

    # Instantiate test class
    test_collector = TestCollector()

    # Store original instance of TestCollector in facts collector to simulate
    #

# Generated at 2022-06-13 03:27:27.500221
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_collector = SelinuxFactCollector()
    assert isinstance(selinux_collector, SelinuxFactCollector)


# Generated at 2022-06-13 03:27:37.482300
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    import pytest
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.collector.selinux import SelinuxFactCollector

    # Create the Collector object with a mock module
    test_collector = Collector()
    test_collector.module = pytest.Mock()
    test_collector.module.params = {}

    # Create the SelinuxFactCollector
    test_SelinuxFactCollector = SelinuxFactCollector()

    # Test if module selinux is not present
    test_SelinuxFactCollector.HAVE_SELINUX = False

    result = test_SelinuxFactCollector._collect(test_collector)
    assert result['selinux'] == {'status': 'Missing selinux Python library'}

# Generated at 2022-06-13 03:27:39.163629
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector is not None

# Generated at 2022-06-13 03:27:42.739521
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    obj = SelinuxFactCollector()
    assert obj.name == 'selinux'
    expected_fact_ids = set()
    assert obj._fact_ids == expected_fact_ids



# Generated at 2022-06-13 03:27:49.183483
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():

    # Test execution without parameters
    obj = SelinuxFactCollector()
    assert obj.name == 'selinux', \
        "The name of the object should be 'selinux', but it is %s" % obj.name

    # Test execution with parameters
    obj = SelinuxFactCollector(name="foo")
    assert obj.name == 'selinux', \
        "The name of the object should be 'selinux', but it is %s" % obj.name


# Generated at 2022-06-13 03:27:53.086253
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():

    c = SelinuxFactCollector()
    assert c.name == 'selinux'

    c = SelinuxFactCollector()
    results = c.collect()

    # Test that status is equal to "disabled" because selinux
    # module is not available in python
    assert results['selinux_python_present'] == False
    assert results['selinux']['status'] == 'Missing selinux Python library'

# Generated at 2022-06-13 03:28:04.467729
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():

    # Data for testing
    class MockModule(object):
        """ Mocking module class for testing """
        def __init__(self):
            pass

    class MockCollectedFacts(object):
        """ Mocking CollectedFacts class for testing """
        def __init__(self):
            pass

    # Mocking the selinux library
    class MockSelinux(object):
        """ Mocking selinux class for testing """
        def __init__(self):
            pass

        def is_selinux_enabled(self):
            return True

        def selinux_getenforcemode(self):
            return (1, 1)

        def selinux_getpolicytype(self):
            return (1, 'targeted')

        def security_getenforce(self):
            return 1


# Generated at 2022-06-13 03:28:05.483102
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    collector = SelinuxFactCollector()
    assert collector.name == 'selinux'

# Generated at 2022-06-13 03:29:00.364755
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinuxFactCollector = SelinuxFactCollector(None)
    assert selinuxFactCollector.name == 'selinux'
    assert selinuxFactCollector._fact_ids == set()

# Generated at 2022-06-13 03:29:04.615186
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    module = 'mock_module'
    collected_facts = 'collected_facts'
    testobj = SelinuxFactCollector(module, collected_facts)
    assert testobj.name == 'selinux'
    assert testobj.collect.__annotations__ == {'return': dict, 'module': type(None), 'collected_facts': dict}


# Generated at 2022-06-13 03:29:06.755041
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.name == 'selinux'
    assert selinux_fact_collector._fact_ids == set()

# Unit test selinux module present

# Generated at 2022-06-13 03:29:09.814411
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux = SelinuxFactCollector()
    assert selinux.name == 'selinux'
    assert selinux.collect() == {}

# Generated at 2022-06-13 03:29:11.162746
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    collector = SelinuxFactCollector()
    assert collector.name == 'selinux'

# Generated at 2022-06-13 03:29:13.500205
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    collector = SelinuxFactCollector()
    assert collector.name == 'selinux'
    assert collector._fact_ids is not None

# Generated at 2022-06-13 03:29:14.669660
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    obj = SelinuxFactCollector()
    assert obj is not None

# Generated at 2022-06-13 03:29:15.750363
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    x = SelinuxFactCollector()
    assert x is not None

# Generated at 2022-06-13 03:29:18.546299
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    '''
    This method unit tests method collect of class SelinuxFactCollector
    '''
    selinux_facts = SelinuxFactCollector()
    selinux_facts.collect()
    # Print all the values collected
    selinux_facts.get_facts()

# Generated at 2022-06-13 03:29:20.329125
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    collector = SelinuxFactCollector()
    assert collector.name == 'selinux'
    assert collector._fact_ids == set()

# Generated at 2022-06-13 03:30:46.986699
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinuxObj = SelinuxFactCollector()
    assert selinuxObj != None
    assert selinuxObj.name == 'selinux'
    assert isinstance(selinuxObj._fact_ids, set)

# Generated at 2022-06-13 03:30:49.440317
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinuxFactCollector = SelinuxFactCollector()
    assert selinuxFactCollector.name == 'selinux'

# Generated at 2022-06-13 03:30:52.517178
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.name == 'selinux'
    assert len(selinux_fact_collector._fact_ids) == 0


# Generated at 2022-06-13 03:30:59.645108
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    """
    Unit test for method collect of class SelinuxFactCollector
    """
    # Disable Selinux for this unit test
    selinux.selinux_setenforce(0)

    # Create an instance of SelinuxFactCollector
    selinux_collector = SelinuxFactCollector()

    # Call collect method
    selinux_facts_dict = selinux_collector.collect()

    assert selinux_facts_dict['selinux_python_present'] is True
    assert selinux_facts_dict['selinux']['status'] == 'enabled'
    assert selinux_facts_dict['selinux']['mode'] == 'permissive'

    # Re-enable selinux
    selinux.selinux_setenforce(1)

# Generated at 2022-06-13 03:31:06.617723
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # Run the collect method of the SelinuxFactCollector class
    # and check whether the method returned the expected result.
    #
    # Make sure selinux Python library is missing
    selinux = None
    try:
        from ansible.module_utils.compat import selinux
        HAVE_SELINUX = True
    except ImportError:
        HAVE_SELINUX = False

    module = None
    collected_facts = None

    selinux_fact_collector = SelinuxFactCollector()
    facts_dict = selinux_fact_collector.collect(module, collected_facts)
    assert 'selinux' in facts_dict
    assert 'selinux_python_present' in facts_dict

    if HAVE_SELINUX:
        assert facts_dict['selinux_python_present'] is True

# Generated at 2022-06-13 03:31:08.565516
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    fact = SelinuxFactCollector()
    assert fact.name == 'selinux'
    assert fact.fact_ids == set()

# Generated at 2022-06-13 03:31:10.091699
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    collector = SelinuxFactCollector()

    assert collector.name == 'selinux'
    assert collector._fact_ids == set()

# Generated at 2022-06-13 03:31:15.890296
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    try:
        from ansible.module_utils.compat import selinux
        HAVE_SELINUX = True
    except ImportError:
        HAVE_SELINUX = False

    if HAVE_SELINUX == False:
        facts_dict = {'selinux_python_present': False,
                      'selinux': {'status': 'Missing selinux Python library'}}
    else:
        facts_dict = {'selinux_python_present': True}

    obj = SelinuxFactCollector()
    assert isinstance(obj, BaseFactCollector)
    assert obj.name == 'selinux'
    assert obj._fact_ids == set()
    result = obj.collect()
    assert result == facts_dict


# Generated at 2022-06-13 03:31:17.612205
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_fact_collector = SelinuxFactCollector()
    result = selinux_fact_collector.collect()
    assert result

# Generated at 2022-06-13 03:31:18.595558
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    assert SelinuxFactCollector().collect()