

# Generated at 2022-06-13 03:22:53.865854
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.name == 'selinux'
    assert len(selinux_fact_collector._fact_ids) == 0
    assert selinux_fact_collector._fact_ids == set()

# Generated at 2022-06-13 03:22:55.772053
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    my_object = SelinuxFactCollector()
    my_object.collect()

# Generated at 2022-06-13 03:22:56.908571
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    SelinuxFactCollector()

# Generated at 2022-06-13 03:22:59.110546
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    assert SelinuxFactCollector.name == 'selinux'
    assert SelinuxFactCollector._fact_ids == set()



# Generated at 2022-06-13 03:23:00.195951
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    collector = SelinuxFactCollector()
    assert collector.name == 'selinux'
    assert collector._fact_ids == set()

# Generated at 2022-06-13 03:23:01.230715
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    SelinuxFactCollector.collect()

# Generated at 2022-06-13 03:23:08.089887
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    # Unit tests returns a empty list of collected facts,
    # when status of SELinux is enabled.
    # As there is no way to enabled SELinux on a running system,
    # this test will always return a empty list.
    assert selinux_fact_collector.collect() == {}
    assert selinux_fact_collector.name == 'selinux'

# Generated at 2022-06-13 03:23:14.395925
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    collected_facts = dict()
    selinux_fact_collector = SelinuxFactCollector()
    selinux_facts = selinux_fact_collector.collect(None, collected_facts)
    assert 'selinux' in selinux_facts
    assert 'status' in selinux_facts['selinux']
    assert selinux_facts['selinux']['status'] == 'Missing selinux Python library'
    assert 'selinux_python_present' in selinux_facts
    assert selinux_facts['selinux_python_present'] == False

# Generated at 2022-06-13 03:23:17.215273
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # Can only unit-test with Python selinux library present
    if not HAVE_SELINUX:
        return

    selinux_facts = SelinuxFactCollector().collect()

    # Verify that there is at least one entry in selinux_facts
    assert selinux_facts != {}

# Generated at 2022-06-13 03:23:19.500968
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector is not None

# Generated at 2022-06-13 03:23:26.261917
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_collector = SelinuxFactCollector()
    selinux_facts = selinux_collector.collect()
    assert selinux_facts['selinux_python_present'] == True

# Generated at 2022-06-13 03:23:33.935404
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    module = None
    collected_facts = {}

    # Call the method
    facts_dict = SelinuxFactCollector().collect(module, collected_facts)
    # Check the returned result
    assert 'selinux' in facts_dict
    assert 'selinux_python_present' in facts_dict

    # Check that the selinux dict has the right keys.
    assert isinstance(facts_dict['selinux'], dict)
    keys = ('config_mode', 'mode', 'policyvers', 'status', 'type')
    if 'status' not in facts_dict['selinux'].keys():
        assert sorted(keys) == sorted(facts_dict['selinux'].keys())

    # Check the value of selinux_python_present
    # This variable is set to True or False because of the import of the selinux library

# Generated at 2022-06-13 03:23:42.381721
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    module_mock = dict()
    collected_facts_mock = dict()

    selinux_facts = dict()
    selinux_facts['status'] = 'Missing selinux Python library'
    selinux_facts['selinux_python_present'] = False

    collected_facts_mock = dict()
    collected_facts_mock['ansible_selinux'] = selinux_facts

    fact_collector = SelinuxFactCollector()
    result = fact_collector.collect(module_mock, collected_facts_mock)

    assert result == collected_facts_mock

# Generated at 2022-06-13 03:23:44.068627
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    assert SelinuxFactCollector().name == 'selinux'


# Generated at 2022-06-13 03:23:55.073237
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    import os
    collector = SelinuxFactCollector()

    # Mock selinux module to be present (HAVE_SELINUX is True)
    collector.selinux = mock.MagicMock()
    facts_dict = collector.collect()
    assert facts_dict['selinux_python_present']
    assert 'selinux' in facts_dict

    # Mock selinux.is_selinux_enabled() to return False
    collector.selinux.is_selinux_enabled.return_value = False
    facts_dict = collector.collect()
    assert facts_dict['selinux_python_present']
    assert facts_dict['selinux']['status'] == 'disabled'

    # Mock selinux.is_selinux_enabled() to return True
    collector.selinux.is_selin

# Generated at 2022-06-13 03:23:56.305324
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    m = SelinuxFactCollector()
    fact = m.collect()
    assert fact.get('selinux')
    assert fact.get('selinux_python_present')

# Generated at 2022-06-13 03:24:08.006541
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # Remove selinux from sys.modules so module is reloaded
    if 'selinux' in sys.modules:
        del sys.modules['selinux']

    # Create a basic mocked selinux module that will return specific values
    # when testing
    class MockSelinux:
        def __init__(self):
            self.is_selinux_enabled_called = 0
            self.security_policyvers_called = 0
            self.selinux_getenforcemode_called = 0
            self.security_getenforce_called = 0
            self.selinux_getpolicytype_called = 0

        def is_selinux_enabled(self):
            self.is_selinux_enabled_called += 1

            if self.is_selinux_enabled_called == 1:
                return True

# Generated at 2022-06-13 03:24:10.819883
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    s = SelinuxFactCollector()
    # SELinux is not enabled on this system, so only status should be returned
    assert s.collect()['selinux']['status'] == 'disabled'

# Generated at 2022-06-13 03:24:13.709113
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux = SelinuxFactCollector()
    assert selinux.name == "selinux"
    assert selinux.collect_fn_name == "selinux.collect"
    assert selinux._fact_ids == set()

# Generated at 2022-06-13 03:24:23.160868
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # Test with selinux library present
    test_object = SelinuxFactCollector()

    test_object.HAVE_SELINUX = True
    test_object.selinux = selinux

    returned_facts = test_object.collect()
    assert returned_facts['selinux_python_present']
    assert 'selinux' in returned_facts.keys()
    assert 'status' in returned_facts['selinux'].keys()
    assert 'policyvers' in returned_facts['selinux'].keys()
    assert 'config_mode' in returned_facts['selinux'].keys()
    assert 'mode' in returned_facts['selinux'].keys()
    assert 'type' in returned_facts['selinux'].keys()

    # Test with selinux library missing
    test_object = Sel

# Generated at 2022-06-13 03:24:30.206150
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    Selinux = SelinuxFactCollector()
    assert Selinux.name == 'selinux'

# Generated at 2022-06-13 03:24:33.253469
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    """Test SelinuxFactCollector"""
    selinux_collector = SelinuxFactCollector()
    assert selinux_collector is not None
    assert selinux_collector.name == 'selinux'

# Generated at 2022-06-13 03:24:35.557403
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.name == 'selinux'

# Generated at 2022-06-13 03:24:39.139890
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_facts = SelinuxFactCollector()

    assert selinux_facts.name == 'selinux'
    assert selinux_facts.collect() == {'selinux': {'status': 'Missing selinux Python library'}, 'selinux_python_present': False}

# Generated at 2022-06-13 03:24:48.019071
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector

    def test_check_available_values(available_fact_names, fact_names):
        for fact_name in available_fact_names:
            assert fact_name in fact_names

    def mock_getenforcemode(self):
        return (0, 1)

    def mock_security_getenforce(self):
        return 1

    def mock_selinux_getpolicytype(self):
        return (0, 'targeted')

    def mock_selinux_getenforcemode_error(self):
        return (-1, None)

    def mock_security_getenforce_error(self):
        return -1

    def mock_selinux_getpolicytype_error(self):
        return (-1, None)


# Generated at 2022-06-13 03:24:56.312466
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # unit tests for __init__ and collect are
    # combined because we need initialized SelinuxFactCollector
    # to test collect. This is how Ansible handles it.
    selinuxfc = SelinuxFactCollector()

    collected_facts = dict()
    selinux_facts = selinuxfc.collect(collected_facts=collected_facts)
    assert 'selinux_python_present' in selinux_facts
    assert 'selinux' in selinux_facts

# Generated at 2022-06-13 03:25:06.620272
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    """
    Test the collect method of SelinuxFactCollector.
    """
    # Initialize and set a mock for the is_selinux_enabled and selinux_getpolicytype methods
    # of AnsibleModuleUtils.selinux module
    import ansible.module_utils.selinux

    module = type('module', (), {'is_selinux_enabled': lambda: True})

    selinux_getpolicytype_mock = lambda: ('policytype', 0)
    ansible.module_utils.selinux.selinux_getpolicytype = selinux_getpolicytype_mock

    # Initialize a SelinuxFactCollector
    selinux_fact_collector = SelinuxFactCollector()

    # Set a mock for the security_policyvers and security_getenforce methods

# Generated at 2022-06-13 03:25:11.158689
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_fact_collector = SelinuxFactCollector()
    test_result = selinux_fact_collector.collect()
    assert type(test_result) is dict


# Generated at 2022-06-13 03:25:14.030761
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    # Test whether the constructor sets the correct name
    my_collector = SelinuxFactCollector()
    assert my_collector.name == 'selinux'



# Generated at 2022-06-13 03:25:21.567808
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_facts = {}
    selinux_facts['status'] = 'enabled'
    selinux_facts['policyvers'] = '28'
    selinux_facts['config_mode'] = 'permissive'
    selinux_facts['mode'] = 'permissive'
    selinux_facts['type'] = 'targeted'
    facts_dict = {}
    facts_dict['selinux'] = selinux_facts
    facts_dict['selinux_python_present'] = True
    obj = SelinuxFactCollector()
    result = obj.collect(collected_facts=None)
    assert result == facts_dict

# Generated at 2022-06-13 03:25:31.268822
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    test_subject = SelinuxFactCollector()

    test_output = {'selinux': {'status': 'Missing selinux Python library', 'config_mode': 'unknown',
                               'mode': 'unknown', 'type': 'unknown'},
                   'selinux_python_present': False}

    assert test_subject.collect() == test_output

# Generated at 2022-06-13 03:25:41.926028
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    """Unit test for SelinuxFacctCollector._collect_selinux method
    """
    selinux_facts = {}
    selinux_facts['status'] = 'enabled'

    selinux_facts['policyvers'] = '68'

    selinux_facts['config_mode'] = 'permissive'
    selinux_facts['mode'] = 'permissive'
    selinux_facts['type'] = 'targeted'

    # Mock class object of class SelinuxFactCollector
    class SelinuxFactCollectorMock(SelinuxFactCollector):
        def __init__(self):
            from ansible.module_utils.facts.collector import BaseFactCollector
            BaseFactCollector.__init__(self)
            self.__name__ = 'SelinuxFactCollector'


# Generated at 2022-06-13 03:25:44.366912
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    module = None
    collected_facts = {}
    c = SelinuxFactCollector()
    c.collect(module, collected_facts)

# Generated at 2022-06-13 03:25:45.304586
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    SelinuxFactCollector().collect(None)

# Generated at 2022-06-13 03:25:46.615293
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    assert SelinuxFactCollector.name == 'selinux'

# Generated at 2022-06-13 03:25:51.933177
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    collector = SelinuxFactCollector()
    facts_dict = collector.collect()
    assert 'selinux' in facts_dict
    assert 'status' in facts_dict['selinux']
    assert facts_dict['selinux_python_present'] is True
    assert 'policyvers' in facts_dict['selinux']
    assert 'config_mode' in facts_dict['selinux']
    assert 'mode' in facts_dict['selinux']
    assert 'type' in facts_dict['selinux']

# Generated at 2022-06-13 03:25:53.591940
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    obj = SelinuxFactCollector()
    assert isinstance(obj.collect(), dict)

# Generated at 2022-06-13 03:26:02.147090
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    import sys
    sys.modules['selinux'] = __import__('ansible.module_utils.facts.collector.selinux.SELINUX_DUMMY', fromlist=["SELINUX_DUMMY"])
    sys.modules['selinux.security_getenforce'] = selinux.security_getenforce

    fact_collector = SelinuxFactCollector()
    results = fact_collector.collect(module=None, collected_facts={})

    assert results == {
        'selinux_python_present': True,
        'selinux': {
            'config_mode': 'disabled',
            'policyvers': '1.0',
            'mode': 'disabled',
            'status': 'disabled',
            'type': 'dummy'
        }
    }

# Generated at 2022-06-13 03:26:10.928314
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    from ansible.module_utils.facts.collector import FactsCollector

    # Create a mock of an AnsibleModule object
    mock_module = MockAnsibleModule()
    mock_module.params = {}

    # Create the AnsibleModule object
    fc = FactsCollector(mock_module)

    # Validate the fact collector
    selinux_fc = fc.get_fact_collector('selinux')
    assert isinstance(selinux_fc, SelinuxFactCollector)

    # Invoke the collect method of the fact collector
    facts_collector_ret = selinux_fc.collect()

    # Validate fact collector return
    selinux_ret = facts_collector_ret.get('selinux')
    assert selinux_ret is not None

    # Validate that the Python selinux library was

# Generated at 2022-06-13 03:26:14.596393
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    # Construct class with no parameters and verify data
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector._fact_ids == set()
    assert selinux_fact_collector.name == 'selinux'

# Generated at 2022-06-13 03:26:24.297644
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.name == 'selinux'

# Generated at 2022-06-13 03:26:35.343192
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_fact_collector = SelinuxFactCollector()
    facts_dict = selinux_fact_collector.collect()
    assert 'selinux_python_present' in facts_dict
    assert 'selinux' in facts_dict
    assert 'status' in facts_dict['selinux']
    assert facts_dict['selinux']['status'] in ('enabled', 'disabled', 'Missing selinux Python library')

    if facts_dict['selinux']['status'] == 'enabled':
        assert 'policyvers' in facts_dict['selinux']
        assert 'config_mode' in facts_dict['selinux']
        assert facts_dict['selinux']['config_mode'] in ('enforcing', 'permissive', 'disabled', 'unknown')

# Generated at 2022-06-13 03:26:45.761806
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # Need to mock the selinux module
    import sys
    sys.modules['selinux'] = MockSel()
    module = MockModule('selinux')
    fact_collector = SelinuxFactCollector(module)
    facts = fact_collector.collect()
    assert facts['selinux_python_present'] is True
    assert facts['selinux']['policyvers'] == '28'
    assert facts['selinux']['config_mode'] == 'enforcing'
    assert facts['selinux']['mode'] == 'enforcing'
    assert facts['selinux']['type'] == 'targeted'
    assert facts['selinux']['status'] == 'enabled'


# Generated at 2022-06-13 03:26:48.560492
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.name == 'selinux'
    assert selinux_fact_collector._fact_ids is not None

# Generated at 2022-06-13 03:26:53.355206
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # Create mock objects
    module = type('', (), {})()
    collected_facts = {}

    # Create the objects
    sfc = SelinuxFactCollector(module)

    # Call the method actually being tested
    fact_dict = sfc.collect(module,collected_facts)

    # Check the results
    assert fact_dict == {
        'selinux': {'status': 'Missing selinux Python library'},
        'selinux_python_present': False
    }

# Generated at 2022-06-13 03:26:55.392369
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.name == 'selinux'


# Generated at 2022-06-13 03:27:05.879722
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    
    class MockModule(object):
        pass

    class MockSelinsux(object):
        def __init__(self):
            self.selinux_enabled = True
            self.policyvers = 20
            self.selinux_getenforcemode = lambda : (0, 1)
            self.security_getenforce = lambda: 0
            self.selinux_getpolicytype = lambda : (0, 'unknown')

        def is_selinux_enabled(self):
            return self.selinux_enabled

        def security_policyvers(self):
            return self.policyvers

        def selinux_getenforcemode(self):
            return self.selinux_getenforcemode()

        def security_getenforce(self):
            return self.security_getenforce()


# Generated at 2022-06-13 03:27:11.495863
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_fact_collector = SelinuxFactCollector()
    selinux_facts_dict = selinux_fact_collector.collect()
    assert type(selinux_facts_dict) is dict

# Generated at 2022-06-13 03:27:22.628843
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():

    collector = SelinuxFactCollector()
    results = collector.collect()

    # The result should have selinux.
    assert('selinux' in results)

    # The selinux should have 4 key/value pairs <status>, <policyvers>, <config_mode>, <mode>, <type>,
    # and <status> should match the expected result.
    selinux_facts = results['selinux']
    assert(len(selinux_facts) == 6)
    assert('status' in selinux_facts)
    if selinux_facts['status'] == 'enabled':
        assert('policyvers' in selinux_facts)
        assert('config_mode' in selinux_facts)
        assert('mode' in selinux_facts)
        assert('type' in selinux_facts)

# Generated at 2022-06-13 03:27:25.041258
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_facts = SelinuxFactCollector()
    assert selinux_facts.collect().get('selinux').get('status') == 'disabled'

# Generated at 2022-06-13 03:27:45.285036
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    fact_collector = SelinuxFactCollector()
    assert fact_collector.name == 'selinux'
    assert fact_collector._fact_ids == set()

# Unit test function collect()

# Generated at 2022-06-13 03:27:53.522953
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    import sys

    # Add the test directory to import path
    testdir = os.path.dirname(__file__)
    sys.path.insert(0, testdir)

    # Create a fake selinux module with hard-coded values for testing
    class selinux:
        @staticmethod
        def is_selinux_enabled():
            return False
        @staticmethod
        def security_policyvers():
            return None


# Generated at 2022-06-13 03:27:56.551124
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    # check attributes
    assert selinux_fact_collector.name == 'selinux'
    assert 'selinux' in selinux_fact_collector._fact_ids

# Generated at 2022-06-13 03:28:07.942153
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_props = {
        'status': 'enabled',
        'policyvers': 42,
        'config_mode': 'enforcing',
        'mode': 'permissive',
        'type': 'targeted'
    }

    selinux_fact_collector = SelinuxFactCollector()

    def is_selinux_enabled_side_effect(*args, **kwargs):
        return True

    def selinux_getenforcemode_side_effect(*args, **kwargs):
        return (0, 0)

    def security_getenforce_side_effect(*args, **kwargs):
        return 1

    def selinux_getpolicytype_side_effect(*args, **kwargs):
        return (0, 'targeted')


# Generated at 2022-06-13 03:28:15.331267
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    import tempfile
    import shutil
    import os

    # Make a temporary directory to be used as a temp storage location
    backup_dir = tempfile.mkdtemp()

    # Get a backup copy of the min selinux module if it exists
    file_to_backup = '/usr/lib/python2.6/site-packages/ansible/module_utils/selinux.py'
    if os.path.isfile(file_to_backup):
        shutil.copy(file_to_backup, backup_dir)

    # Remove the min selinux module from the python path so we can test
    # the fact that the selinux python library is missing
    os.remove(file_to_backup)

    # Instantiate the Selinux Fact Collector Class
    selinux_fact_collector = SelinuxFactCollector

# Generated at 2022-06-13 03:28:24.390549
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # Create  SelinuxFactCollector object
    selinux_fact_collector = SelinuxFactCollector()

    # Create variables for testing
    status_key = 'status'
    disabled_value = 'disabled'
    config_mode_key = 'config_mode'
    permissive_value = 'permissive'
    mode_key = 'mode'
    enforcing_value = 'enforcing'
    type_key = 'type'
    mls_value = 'MLS'
    policyvers_key = 'policyvers'
    policyvers_value = '28'

    # Generate test data
    selinux_facts_disabled = {}
    selinux_facts_disabled[status_key] = disabled_value
    selinux_facts_disabled[config_mode_key] = permissive_value
    selinux_facts_disabled

# Generated at 2022-06-13 03:28:34.655658
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    import sys
    import tempfile
    import os
    old_sys_modules = sys.modules.copy()
    fact_collector = SelinuxFactCollector()

# Generated at 2022-06-13 03:28:35.750744
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_facts = SelinuxFactCollector()
    assert selinux_facts.name == 'selinux'
    assert 'selinux' in selinux_facts._fact_ids

# Generated at 2022-06-13 03:28:36.824407
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    my_selinux_instance = SelinuxFactCollector()
    assert my_selinux_instance is not None

# Unit test to check the collector name

# Generated at 2022-06-13 03:28:38.646577
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    """
    If selinux library is available, the constructor should set selinux_python_present to True.
    If not, it should set the value to False.
    """
    selinux_collector = SelinuxFactCollector()
    assert selinux_collector.collect()['selinux_python_present'] == HAVE_SELINUX

# Generated at 2022-06-13 03:29:36.476650
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    c = SelinuxFactCollector()
    # set up the expected results
    expected_results = {
        "selinux_python_present": True,
        "selinux": {
            "config_mode": "enforcing",
            "mode": "enforcing",
            "status": "enabled",
            "type": "targeted"
        }
    }

    # set up the selinux library to return our prearranged answers
    def selinux_is_selinux_enabled():
        return True
    def selinux_security_policyvers():
        return 28
    def selinux_selinux_getenforcemode():
        return (0, 1)
    def selinux_security_getenforce():
        return 1

# Generated at 2022-06-13 03:29:39.197655
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector is not None


# Generated at 2022-06-13 03:29:42.442534
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    src = SelinuxFactCollector()
    fact_dict = src.collect()
    assert 'selinux' in fact_dict
    assert 'selinux_python_present' in fact_dict
    assert 'status' in fact_dict['selinux']

# Generated at 2022-06-13 03:29:49.072065
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    #  Get the class object for SelinuxFactCollector class
    obj_SelinuxFactCollector = SelinuxFactCollector()
    #  Call the collect method of SelinuxFactCollector class
    #  Because Module class is not imported, this will fail with exception which
    #  will be handled and will return None
    assert obj_SelinuxFactCollector.collect() is None

#  Unit test for method name of class SelinuxFactCollector

# Generated at 2022-06-13 03:29:51.028721
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    obj = SelinuxFactCollector()
    assert obj.name == 'selinux'
    assert obj._fact_ids == set()



# Generated at 2022-06-13 03:30:04.185579
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts import get_collector_instance
    from ansible.module_utils._text import to_bytes

    selinux_fake = SelinuxFactCollector()
    selinux_fake.collect = lambda x=None, y=None: {'selinux': {'status': 'disabled'}}

    collector_mock = Collector()
    collector_mock.get_collector = lambda x: selinux_fake

    tmp_result = get_collector_instance().get_fact(to_bytes('selinux'))
    assert tmp_result['status'] == 'disabled'

    tmp_result = get_collector_instance().get_fact(to_bytes('selinux_python_present'))
    assert not tmp_result



# Generated at 2022-06-13 03:30:06.915580
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    assert isinstance(SelinuxFactCollector(), SelinuxFactCollector)


# Generated at 2022-06-13 03:30:10.835341
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    assert SelinuxFactCollector.name == 'selinux'
    assert len(SelinuxFactCollector._fact_ids) == 0


# Generated at 2022-06-13 03:30:14.294635
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    """Unit test class constructor of SelinuxFactCollector
    """
    fact_collector = SelinuxFactCollector()
    assert fact_collector.name == 'selinux'
    assert fact_collector._fact_ids == set()

# Generated at 2022-06-13 03:30:18.576730
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.name == "selinux"
    assert selinux_fact_collector._fact_ids == set()

# Generated at 2022-06-13 03:31:59.292720
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    """Test SelinuxFactCollector
    """
    seinfo = SelinuxFactCollector()

    assert seinfo.name == 'selinux'
    keys = set
    assert seinfo._fact_ids == keys([])
    assert seinfo.collect() == {}

# Generated at 2022-06-13 03:32:04.480699
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    import ansible.module_utils.facts.collectors.selinux as module_collector

    module_collector.HAVE_SELINUX = False
    module_collector.selinux = None
    selinux_facts = {}
    selinux_facts['status'] = 'Missing selinux Python library'
    selinux_facts['selinux_python_present'] = False
    facts_dict = module_collector.SelinuxFactCollector().collect()
    assert facts_dict['selinux'] == selinux_facts
    assert facts_dict['selinux_python_present'] == False

# Generated at 2022-06-13 03:32:07.326204
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    import sys
    import os
    sys.modules['selinux'] = os.stat_result
    selinux_fact_collector = SelinuxFactCollector()
    test_response = selinux_fact_collector.collect()
    assert test_response['selinux']['status'] == 'Missing selinux Python library'
    assert test_response['selinux_python_present'] == False

# Generated at 2022-06-13 03:32:10.893004
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_collector = SelinuxFactCollector()
    test_result = selinux_collector.collect()

    assert set(test_result.keys()) == {
        'selinux',
        'selinux_python_present'
    }

    assert set(test_result['selinux'].keys()) == {
        'config_mode',
        'mode',
        'policyvers',
        'status',
        'type'
    } or set(test_result['selinux'].keys()) == {
        'status',
    }

# Generated at 2022-06-13 03:32:11.753632
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinuxFactCollector = SelinuxFactCollector()
    selinuxFactCollector.collect() # returns dict

# Generated at 2022-06-13 03:32:14.858384
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    """Check instantiating SelinuxFactCollector works as expected."""
    collector = SelinuxFactCollector()

    assert collector.name == 'selinux'

# Generated at 2022-06-13 03:32:16.430809
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    obj = SelinuxFactCollector()
    assert obj.name == 'selinux'
    assert obj._fact_ids == set([])

# Generated at 2022-06-13 03:32:24.826482
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    py_version = sys.version_info[0]
    if py_version == 2:
        mock_selinux_base = [
            "security_policyvers",
            "selinux_getenforcemode",
            "security_getenforce",
            "selinux_getpolicytype"
        ]
        mock_selinux = MagicMock()
        sys.modules['selinux'] = mock_selinux
        # python 2.7
        if sys.version_info[1] == 7:
            mock_selinux_base.extend([
                "is_selinux_enabled",
            ])
        # python 2.6

# Generated at 2022-06-13 03:32:26.675496
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_fact_collector = SelinuxFactCollector()
    selinux_facts = selinux_fact_collector.collect()
    assert isinstance(selinux_facts, dict)

# Generated at 2022-06-13 03:32:27.948642
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    fc = SelinuxFactCollector()
    assert fc.name == 'selinux'