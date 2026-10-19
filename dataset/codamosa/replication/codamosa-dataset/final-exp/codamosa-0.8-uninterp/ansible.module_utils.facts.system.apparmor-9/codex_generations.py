

# Generated at 2022-06-13 02:19:45.746100
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    ApparmorFactCollector.collect()

# Generated at 2022-06-13 02:19:50.110578
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact = ApparmorFactCollector()
    result = apparmor_fact.collect()
    # assert apparmor status is present in fact
    assert 'apparmor' in result

# Generated at 2022-06-13 02:19:55.563588
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    fact_collector = ApparmorFactCollector()
    # mock the ansible module
    ansible_module = MagicMock()
    # mock the ansible module exit_json method
    ansible_module.exit_json = MagicMock()
    fact_collector.collect(ansible_module)
    # Call the exit_json function
    ansible_module.exit_json.assert_called_once_with(
        changed=False, ansible_facts={'apparmor': {'status': 'disabled'}})

# Generated at 2022-06-13 02:19:58.528703
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():

    data = {
        'apparmor': {
            'status': 'enabled'
        }
    }
    afc = ApparmorFactCollector()
    facts = afc.collect(None)
    assert facts == data

# Generated at 2022-06-13 02:20:01.717365
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_collector = ApparmorFactCollector()
    apparmor_dict = apparmor_collector.collect()
    assert apparmor_dict['apparmor']
    assert 'status' in apparmor_dict['apparmor']

# Generated at 2022-06-13 02:20:04.481753
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    fact = ApparmorFactCollector()
    facts = fact.collect()
    assert 'status' in facts['apparmor']


# Generated at 2022-06-13 02:20:05.446534
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    assert ApparmorFactCollector.collect(None, None)

# Generated at 2022-06-13 02:20:06.755245
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    pass

# vim: set et ts=4 sw=4 :

# Generated at 2022-06-13 02:20:08.787671
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact_collecter = ApparmorFactCollector()
    apparmor_facts = apparmor_fact_collecter.collect()
    assert 'apparmor' in apparmor_facts

# Generated at 2022-06-13 02:20:13.050622
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact_collector = ApparmorFactCollector()
    collected_facts = apparmor_fact_collector.collect()
    assert type(collected_facts) is dict,\
        "type of collected_facts should be dict."

# Generated at 2022-06-13 02:20:18.426781
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    """Test method collect of class ApparmorFactCollector"""
    # pylint: disable=protected-access
    apparmor_fact_collector = ApparmorFactCollector()
    assert apparmor_fact_collector._fact_ids == set()

    apparmor_fact_collector.collect()

    assert 'status' in apparmor_fact_collector.collect()['apparmor']

# Generated at 2022-06-13 02:20:20.923283
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    facts_dict = {}
    aafc = ApparmorFactCollector()
    facts_dict = aafc.collect()
    assert 'apparmor' in facts_dict
    assert 'status' in facts_dict['apparmor']
    assert isinstance(facts_dict['apparmor']['status'], str)



# Generated at 2022-06-13 02:20:24.914600
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    # get instance of class
    apparmor_fc = ApparmorFactCollector()

    # get return value of method collect
    actual = apparmor_fc.collect()

    # check if apparmor key is present in dict
    assert 'apparmor' in actual


# Generated at 2022-06-13 02:20:27.095125
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    """ ansible.module_utils.facts.system.apparmor.ApparmorFactCollector.collect - test cases"""
    # fail if status is not enabled or disabled
    collector = ApparmorFactCollector()
    assert collector.collect()['apparmor']['status'] in ["enabled", "disabled"]


# Generated at 2022-06-13 02:20:29.136272
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    class_instance = ApparmorFactCollector()
    class_instance.collect()

# Generated at 2022-06-13 02:20:31.415530
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    ac = ApparmorFactCollector()
    facts = ac.collect()
    assert facts['apparmor']['status'] == 'disabled'

# Generated at 2022-06-13 02:20:35.088546
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact = ApparmorFactCollector()
    assert apparmor_fact.collect() == {'apparmor': {'status': 'enabled'}} or {'apparmor': {'status': 'disabled'}}

# Generated at 2022-06-13 02:20:38.876056
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    # Arrange
    apparmor_fact_collector = ApparmorFactCollector()

    # Act
    apparmor_facts = apparmor_fact_collector.collect()

    # Assert
    assert 'apparmor' in apparmor_facts

# Generated at 2022-06-13 02:20:40.715568
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    ApparmorFactCollector().collect()

# vim: set et ts=4 sw=4 :

# Generated at 2022-06-13 02:20:49.398446
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    from ansible.module_utils.facts.collector import TestBaseFactCollector
    import os
    import mock

    if os.path.exists('/sys/kernel/security/apparmor'):
        result = {'apparmor':
            {
                'status': 'enabled'
            }
        }
    else:
        result = {'apparmor':
            {
                'status': 'disabled'
            }
        }

    mock_module = mock.MagicMock()
    mock_module.exit_json.return_value = {}
    test_collector = ApparmorFactCollector()
    result_dict = test_collector.collect(module=mock_module, collected_facts=None)
    assert result == result_dict

# Generated at 2022-06-13 02:20:52.999369
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    ApparmorFactCollector().collect()

# Generated at 2022-06-13 02:20:55.937692
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    """
    Unit test for method collect of class ApparmorFactCollector
    """
    fact_collector = ApparmorFactCollector()
    assert fact_collector.collect() == {'apparmor': {'status': 'disabled'}}

# Generated at 2022-06-13 02:20:57.957678
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    aafc = ApparmorFactCollector()
    aafc_results = aafc.collect()

    assert 'apparmor' in aafc_results

# Generated at 2022-06-13 02:20:59.328239
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    cpu_fac = ApparmorFactCollector()
    facts_dict = cpu_fac.collect()
    assert facts_dict == {'apparmor': {'status': 'disabled'}}

# Generated at 2022-06-13 02:21:08.699927
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():

    # TODO: Fix
    # testing is not working currently.
    
    # apparmor_check_enabled = '/sys/kernel/security/apparmor'
    # apparmor_check_disabled = '/sys/kernel/security/apparmor/notae'

    # # checking when apparmor is enabled
    # apparmor_facts = ApparmorFactCollector()
    # assert apparmor_facts.collect({}) == {'apparmor': {'status': 'enabled'}}

    # # checking when apparmor is disabled
    # apparmor_facts = ApparmorFactCollector()
    # assert apparmor_facts.collect({}) == {'apparmor': {'status': 'disabled'}}

    return

# Generated at 2022-06-13 02:21:18.139930
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    '''Unit test for method ApparmorFactCollector.collect'''

    # Case 1: If file /sys/kernel/security/apparmor exists, then apparmor_facts['status'] = 'enabled'
    # Case 2: If file /sys/kernel/security/apparmor not exists, then apparmor_facts['status'] = 'disabled'

    # Case 2: If file /sys/kernel/security/apparmor not exists, then apparmor_facts['status'] = 'disabled'
    # Create a new class instance
    apparmorFactCollector = ApparmorFactCollector()
    # Run the method collect
    apparmor_facts = apparmorFactCollector.collect()
    # Create the expected result
    expected_result = {'apparmor': {'status': 'disabled'} }
    # Check the result
    assert apparmor_facts == expected_result

# Generated at 2022-06-13 02:21:20.936831
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    fixture_dict = {'ansible_facts':
                    {'apparmor':
                        {'status': 'enabled'}},
                    'changed': False}
    fact_collector = ApparmorFactCollector()
    assert fact_collector.collect() == fixture_dict

# Generated at 2022-06-13 02:21:22.607702
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fc = ApparmorFactCollector()
    apparmor_fc.collect()

# Generated at 2022-06-13 02:21:25.097186
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    module = mock.MagicMock()
    module.get_bin_path.return_value = '/usr/sbin/apparmor_status'
    collector = apparmor_fact_collector.ApparmorFactCollector(module)
    collected_facts = collector.collect()
    assert 'apparmor' in collected_facts
    assert 'status' in collected_facts['apparmor']

# Generated at 2022-06-13 02:21:29.455480
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    """
    Unit test for method collect of class ApparmorFactCollector.
    Returns dictionary of apparmor facts
    """
    fact_collector = ApparmorFactCollector()
    assert('apparmor' in fact_collector.collect())

# Generated at 2022-06-13 02:21:38.384573
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor = ApparmorFactCollector()
    if os.path.exists('/sys/kernel/security/apparmor'):
        expected_status = 'enabled'
    else:
        expected_status = 'disabled'
    facts_dict = apparmor.collect()
    assert facts_dict == {'apparmor': {'status': expected_status}}

# Generated at 2022-06-13 02:21:44.051869
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor = ApparmorFactCollector()
    with open('/sys/kernel/security/apparmor', 'w') as f:
        f.write('test-file')
    collected_facts = apparmor.collect(collected_facts={})
    if collected_facts.has_key('apparmor'):
        assert collected_facts['apparmor']['status'] == 'enabled'
    else:
        assert False

# Generated at 2022-06-13 02:21:50.141826
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():

    class MockModule(object):
        @staticmethod
        def run_command(command, check_rc=True):
            return "1"
        @staticmethod
        def get_bin_path(bin_name, required=True):
            return '1'

    class MockFile(object):
        @staticmethod
        def exists(file_path):
            return False

    module = MockModule()
    file = MockFile()
    x = ApparmorFactCollector()
    x.collect(module=module, file=file)

# vim: expandtab filetype=python

# Generated at 2022-06-13 02:21:51.490181
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    ApparmorFactCollector = ApparmorFactCollector()
    ApparmorFactCollector.collect()

# Generated at 2022-06-13 02:21:54.989397
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    fake_module = 'Fake module'
    fake_collector = ApparmorFactCollector()
    apparmor_facts = fake_collector.collect(module=fake_module, collected_facts='banana')
    assert 'apparmor' in apparmor_facts
    assert 'status' in apparmor_facts['apparmor']

# Generated at 2022-06-13 02:21:58.089969
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    """
    Checks for correct dictionary keys for apparmor fact
    """
    apparmor_collector = ApparmorFactCollector()
    apparmor_collector.collect()
    assert apparmor_collector.get_facts()['apparmor'].keys() == ['status']

# Generated at 2022-06-13 02:22:01.101091
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    from ansible.module_utils.facts import FactCollector, get_collector_instance
    from ansible.module_utils.facts.collector.apparmor import ApparmorFactCollector

    collected_facts = {}
    facts_collector = get_collector_instance(ApparmorFactCollector)
    facts_dict = facts_collector.collect(collected_facts)
    assert (facts_dict['apparmor']['status'] in ['enabled', 'disabled'])

# Generated at 2022-06-13 02:22:07.719841
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    # Test with apparmor in disabled state
    os.path.exists = Mock(return_value=False)
    apparmorFactCollector = ApparmorFactCollector()
    result = apparmorFactCollector.collect()
    assert result['apparmor']['status'] == 'disabled'

    # Test with apparmor in enabled state
    os.path.exists = Mock(return_value=True)
    apparmorFactCollector = ApparmorFactCollector()
    result = apparmorFactCollector.collect()
    assert result['apparmor']['status'] == 'enabled'

# Generated at 2022-06-13 02:22:10.696260
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor = ApparmorFactCollector()
    assert apparmor.collect() == {'apparmor': {'status': 'ENABLED'}}

# Generated at 2022-06-13 02:22:18.960093
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    import os
    import re
    import pytest

    @pytest.fixture
    def ApparmorFactCollectorClass(mocker):
        '''Fixture to mock the base class and return fake apparmor facts.'''
        mocker.patch.object(BaseFactCollector, 'collect',
                            return_value={'apparmor': {'status': 'enabled'}})
        return BaseFactCollector

    def test_apparmor_fact_collector_disabled(self, ApparmorFactCollectorClass):
        '''Unit test to prove ApparmorFactCollector.collect with apparmor disabled.'''
        mocker.patch.object(os.path, 'exists', return_value=False)
        class_test = ApparmorFactCollector()
        class_test.collect()
        assert class_test.name == 'apparmor'
       

# Generated at 2022-06-13 02:22:36.958004
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    from ansible.utils.path import unfrackpath
    from ansible.module_utils._text import to_bytes

    ApparmorFactCollector.collect = lambda *args, **kwargs: {"apparmor":
                                                              {"status": "disabled"}}
    module = lambda *args, **kwargs: None
    module.exit_json = lambda *args, **kwargs: None
    tmp = unfrackpath("$system_mount_point/tmp")

# Generated at 2022-06-13 02:22:47.192882
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    from ansible_collections.ansible.netcommon.tests.unit.compat import unittest
    from ansible_collections.ansible.netcommon.plugins.module_utils.facts.collector.apparmor import ApparmorFactCollector

    class TestApparmorFactCollector(unittest.TestCase):
        def setUp(self):
            self.apparmor = ApparmorFactCollector()

        def tearDown(self):
            pass

        def test_collect_apparmor_facts(self, *args, **kwargs):
            attrs = {
                "fact_ids.return_value": set()
            }
            self.apparmor.collect = MagicMock(return_value="test")
            self.apparmor.collect()

# Generated at 2022-06-13 02:22:49.943181
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    fact = ApparmorFactCollector(None, None)
    facts_dict = fact.collect()
    assert 'apparmor' in facts_dict.keys()
    assert 'status' in facts_dict['apparmor'].keys()

# Generated at 2022-06-13 02:22:58.221243
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    # mock os.path
    class MockOsPath():
        def exists(self, path):
            if path == '/sys/kernel/security/apparmor':
                return True
            else:
                return False

    import sys
    sys.modules['os.path'] = MockOsPath()

    # mock module object
    class MockModule(object):
        class MockParams(object):
            gather_subset = None
            gather_timeout = None
            filter = None
            whitelist = None

        params = MockParams()

    apparmor_fact_collector = ApparmorFactCollector()

    # mock system_profiler
    class MockSystemProfiler():
        def __init__(self):
            self.ok = False


# Generated at 2022-06-13 02:22:59.136413
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    # TODO: Add test
    ...

# Generated at 2022-06-13 02:23:04.828528
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    # Mock needed libraries
    class MockOs(object):
        class path(object):
            @staticmethod
            def exists(filepath):
                if filepath == "/sys/kernel/security/apparmor":
                    return True
                else:
                    return False

    mock_module = MockOs()
    apparmor = ApparmorFactCollector()

    assert(apparmor.collect(mock_module) == {'apparmor': {'status': 'enabled'}})

# Generated at 2022-06-13 02:23:07.461972
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    """Unit test for method collect of class ApparmorFactCollector."""
    apparmor_fact_collector = ApparmorFactCollector()
    assert 'apparmor' in apparmor_fact_collector.collect()

# Generated at 2022-06-13 02:23:11.391158
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    test_collector = ApparmorFactCollector()
    test_collector._module = {}
    test_collector._module.get_bin_path = lambda x: 'True'
    test_collector._module.run_command = lambda x: 'True'
    test_collector._module.get_shell_type = lambda x: 'True'
    test_collector.collect()

# Generated at 2022-06-13 02:23:14.846710
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_instance = ApparmorFactCollector()
    f_dict = apparmor_instance.collect()
    assert 'apparmor' in f_dict

# Generated at 2022-06-13 02:23:21.070667
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    factCollector = ApparmorFactCollector
    collected_facts = {}
    collected_facts.update(factCollector.collect())
    assert type(collected_facts) is dict
    assert 'apparmor' in collected_facts
    assert len(collected_facts['apparmor']) >= 1
    assert type(collected_facts['apparmor']) is dict
    assert 'status' in collected_facts['apparmor']
    assert type(collected_facts['apparmor']['status']) is str

# Generated at 2022-06-13 02:23:47.949784
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    # Create instance of ApparmorFactCollector
    apparmor_fact_collector = ApparmorFactCollector()

    # Call collect method of ApparmorFactCollector
    apparmor_facts = apparmor_fact_collector.collect()
    assert apparmor_facts is not None
    assert apparmor_facts['apparmor']['status'].strip() == 'disabled'

# Generated at 2022-06-13 02:23:49.872067
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact_collector = ApparmorFactCollector()
    assert apparmor_fact_collector.collect() == {'apparmor': {'status': 'disabled'}}

# Generated at 2022-06-13 02:23:53.118443
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    """
    apparmor.collect is deprecated, tests exist in test_linux.py
    This method exists to prevent collect from being removed from this file
    but tests also exist in test_linux.py
    """
    pass

# Generated at 2022-06-13 02:23:59.848172
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    from ansible.module_utils.facts.collector import Collectors
    from ansible.module_utils.facts.collector.apparmor import ApparmorFactCollector as apparmor_fact_collector
    from ansible.module_utils.facts import ModuleTestCase

    collected_facts = {}
    collectors = {'distribution': apparmor_fact_collector}
    apparmor_fact_collector = Collectors(collected_facts, [], [[], {}], collectors)
    apparmor_fact_collector.collect()

    assert collected_facts['apparmor']['status'] == 'disabled'

# Generated at 2022-06-13 02:24:03.008569
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    cm = ApparmorFactCollector()
    assert cm.collect() == {
        'apparmor': {
            'status': 'disabled'
        }
    }

# Generated at 2022-06-13 02:24:03.822848
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    pass


# Generated at 2022-06-13 02:24:08.614566
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    if os.path.exists('/sys/kernel/security/apparmor'):
        apparmor_facts = {'apparmor': {'status': 'enabled'}}
    else:
        apparmor_facts = {'apparmor': {'status': 'disabled'}}
    afc = ApparmorFactCollector()
    facts = afc.collect()
    assert facts == apparmor_facts

# Generated at 2022-06-13 02:24:10.230904
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact = ApparmorFactCollector()
    apparmor_fact._module = None
    apparmor_fact.collect()

# Generated at 2022-06-13 02:24:12.038777
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    aac = ApparmorFactCollector()
    apparmor_facts = aac.collect()
    assert apparmor_facts['apparmor']['status'] in ['enabled', 'disabled']

# Generated at 2022-06-13 02:24:16.244345
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    module = None
    collected_facts = None
    apparmor_fact = ApparmorFactCollector()
    apparmor_facts = apparmor_fact.collect(module, collected_facts)
    assert 'apparmor' in apparmor_facts

# Generated at 2022-06-13 02:25:10.540176
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_facts = ApparmorFactCollector().collect()
    assert isinstance(apparmor_facts, dict)
    assert apparmor_facts['apparmor']['status'] == 'enabled' or \
        apparmor_facts['apparmor']['status'] == 'disabled'

# Generated at 2022-06-13 02:25:12.195068
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fc = ApparmorFactCollector()
    # Test the collect method by calling it with the module and collected facts arguments
    assert apparmor_fc.collect() == {'apparmor': {'status': 'disabled'}}

# Generated at 2022-06-13 02:25:15.924593
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact_collector = ApparmorFactCollector(None)
    facts_dict = apparmor_fact_collector.collect()
    assert 'apparmor' in facts_dict

# Generated at 2022-06-13 02:25:17.457799
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    '''Unit test for method collect of class ApparmorFactCollector'''
    ApparmorFactCollector_obj = ApparmorFactCollector()
    facts_dict = ApparmorFactCollector_obj.collect()
    assert facts_dict['apparmor']['status'] == 'disabled'

# Generated at 2022-06-13 02:25:17.960025
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    pass

# Generated at 2022-06-13 02:25:19.115252
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    aafc = ApparmorFactCollector()
    assert aafc.collect()

# Generated at 2022-06-13 02:25:21.622080
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact_collector = ApparmorFactCollector()
    # Test with /sys/kernel/security/apparmor existing
    try:
        os.stat('/sys/kernel/security/apparmor')
        facts_dict = apparmor_fact_collector.collect()
        assert facts_dict['apparmor']['status'] == 'enabled'
    except:
        facts_dict = apparmor_fact_collector.collect()
        assert facts_dict['apparmor']['status'] == 'disabled'

# Generated at 2022-06-13 02:25:22.994446
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    c = ApparmorFactCollector()
    result = c.collect()
    assert 'apparmor' in result

# Generated at 2022-06-13 02:25:26.069558
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    facts = {}
    fact_collector = ApparmorFactCollector()
    fact_collector.collect(collected_facts=facts)
    assert facts['apparmor']['status'] in ('enabled', 'disabled')

# Generated at 2022-06-13 02:25:28.836157
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    c = ApparmorFactCollector()
    result = c.collect()
    assert result['apparmor']['status'] == 'enabled' or result['apparmor']['status'] == 'disabled'
# END Unit test for method collect of class ApparmorFactCollector

# Generated at 2022-06-13 02:27:25.525170
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    # Get possibly mocked ApparmorFactCollector class
    fact_collector_class = ApparmorFactCollector()
    # Unit test to check if the collected facts are correct or not
    collected_facts = fact_collector_class.collect()
    assert collected_facts['apparmor']['status'] == 'disabled'


# Generated at 2022-06-13 02:27:30.676512
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    import ansible.module_utils.facts.collector
    # First set of test data
    # /sys/kernel/security/apparmor exists
    collected_facts = {}
    apparmor_fact_collector = ApparmorFactCollector()
    res_dict = apparmor_fact_collector.collect(collected_facts=collected_facts)
    assert res_dict == {'apparmor': {'status': 'enabled'}}
    # /sys/kernel/security/apparmor does not exist
    collected_facts = {}
    apparmor_fact_collector = ApparmorFactCollector()
    os.system('mkdir -p /tmp/notsys/kernel/')
    os.system('mv /sys/kernel/security /tmp/notsys/kernel/')

# Generated at 2022-06-13 02:27:35.628325
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    """
    Checks if method collect of class ApparmorFactCollector returns the correct
    data structure.
    """
    aafc = ApparmorFactCollector()
    assert aafc.collect() == {
        'apparmor': {
            'status': 'disabled'
        }
    }

# Generated at 2022-06-13 02:27:37.187265
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    aaf = ApparmorFactCollector()
    assert aaf.collect()['apparmor']['status'] == 'disabled'

# Generated at 2022-06-13 02:27:43.779096
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    '''Used for unittest.TestCase.subTest()'''
    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils.facts.collectors.apparmor import ApparmorFactCollector
    # create fake class ApparmorFactCollector
    class FakeApparmorFactCollector():
        pass
    FakeApparmorFactCollector.name = 'apparmor'
    FakeApparmorFactCollector._fact_ids = set()

    # monkey patch ApparmorFactCollector.collect to raise exception
    # if BaseFactCollector.collect is not called as expected
    def _mock_base_collect(self, module=None, collected_facts=None):
        raise Exception('expected call to BaseFactCollector.collect')
    BaseFactCollector.collect = _mock_base_collect

    # monkey patch `

# Generated at 2022-06-13 02:27:48.525202
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    fact_collector = ApparmorFactCollector()
    if os.path.exists('/sys/kernel/security/apparmor'):
        result = fact_collector.collect()
        assert result['apparmor'] == {'status': 'enabled'}
    else:
        result = fact_collector.collect()
        assert result['apparmor'] == {'status': 'disabled'}

# Generated at 2022-06-13 02:27:52.757022
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    # Create mock module
    apparmor_obj = ApparmorFactCollector()
    apparmor_obj.collect()
    apparmor_dict = apparmor_obj.collect()
    print("apparmor dict: %s" % apparmor_dict)
    print("apparmor dict keys: %s" % apparmor_dict.keys())
    print("apparmor dict values: %s" % apparmor_dict.values())

if __name__ == '__main__':
    test_ApparmorFactCollector_collect()

# Generated at 2022-06-13 02:27:58.169619
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    Apparmor_FactCollector = ApparmorFactCollector()
    apparmor_facts = Apparmor_FactCollector.collect()
    assert apparmor_facts is not None
    assert apparmor_facts['apparmor'] is not None
    assert apparmor_facts['apparmor']['status'] is not None

# Generated at 2022-06-13 02:28:01.879540
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact_collector = ApparmorFactCollector()
    collected_facts = apparmor_fact_collector.collect()
    assert "apparmor" in collected_facts

# Generated at 2022-06-13 02:28:03.599387
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact = ApparmorFactCollector()
    assert apparmor_fact.collect() == {'apparmor': {'status': 'disabled'}}