

# Generated at 2022-06-13 02:19:45.111136
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    c = ApparmorFactCollector()
    assert not c._fact_ids
    assert c.name == 'apparmor'
    assert isinstance(c.collect(), dict)
    assert isinstance(c.collect()['apparmor'], dict)
    assert c.collect()['apparmor']['status'] == 'disabled'


# Generated at 2022-06-13 02:19:48.725134
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact_collector = ApparmorFactCollector()
    assert(apparmor_fact_collector.collect() == {'apparmor': {'status': 'disabled'}})

# Generated at 2022-06-13 02:19:53.933784
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    mod = ApparmorFactCollector()
    collected_facts = {}
    # Apparmor should be enabled
    facts = mod.collect(collected_facts)
    assert facts['apparmor']['status'] == 'enabled'
    # Apparmor should be disabled
    assert mod.collect(collected_facts)['apparmor']['status'] == 'disabled'

# Generated at 2022-06-13 02:19:55.690236
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_facts = ApparmorFactCollector().collect()
    assert apparmor_facts['apparmor']['status'] == 'enabled'

# Generated at 2022-06-13 02:19:59.992833
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    collector = ApparmorFactCollector()
    apparmor_facts = collector.collect()
    assert(apparmor_facts.values()[0])
    assert(apparmor_facts.values()[0].values()[0])
    assert(apparmor_facts.values()[0]['status'] in ['enabled', 'disabled'])

# Generated at 2022-06-13 02:20:02.538048
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_collector = ApparmorFactCollector()
    apparmor_collector.collect()
    assert apparmor_collector._fact_ids == {'apparmor'}

# Generated at 2022-06-13 02:20:05.351550
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact_collector = ApparmorFactCollector()
    assert 'apparmor' in apparmor_fact_collector.collect()

# Generated at 2022-06-13 02:20:07.267306
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_collector = ApparmorFactCollector()
    # Make sure the class can collect facts
    assert apparmor_collector.collect()

# Generated at 2022-06-13 02:20:09.007829
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_collector = ApparmorFactCollector()
    apparmor_collector.collect()
    assert apparmor_collector._fact_ids is not None

# Generated at 2022-06-13 02:20:12.542928
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_facts = ApparmorFactCollector().collect()
    assert 'apparmor' in apparmor_facts
    assert 'status' in apparmor_facts['apparmor']

# Generated at 2022-06-13 02:20:16.488549
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    """
    Test case for method collect of class ApparmorFactCollector
    """
    fact_collector_obj = ApparmorFactCollector()
    fact_dict = fact_collector_obj.collect()
    assert fact_dict['apparmor']

# Generated at 2022-06-13 02:20:18.651224
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    collector = ApparmorFactCollector()
    _fact_ids = collector.collect()
    assert _fact_ids['apparmor'] == {'status': 'enabled'}

# Generated at 2022-06-13 02:20:23.927196
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    module = MagicMock()
    collected_facts = {}
    facts_dict = {}
    apparmor_facts = {}
    apparmor_facts['status'] = 'enabled'
    facts_dict['apparmor'] = apparmor_facts
    apparmor_fact_collector = ApparmorFactCollector()
    if apparmor_fact_collector.collect(module=module, collected_facts=collected_facts) == facts_dict:
        print('Test for method collect of class ApparmorFactCollector passed')
    else:
        print('Test for method collect of class ApparmorFactCollector failed')

# Generated at 2022-06-13 02:20:26.493588
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    fact_collector = ApparmorFactCollector()
    facts_dict = fact_collector.collect()
    assert (facts_dict == {'apparmor': {'status': 'enabled'}})

# Generated at 2022-06-13 02:20:30.714803
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    fact_collector = ApparmorFactCollector()
    expected = {
            'apparmor': {
                'status': 'disabled',
                }
            }
    returned = fact_collector.collect()
    assert expected == returned

# Generated at 2022-06-13 02:20:36.267507
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    # tested class
    class_name = 'ApparmorFactCollector'

    # Instansiate the tested class
    apparmor_collector = ApparmorFactCollector()
    # Collect facts from the class
    facts_dict = apparmor_collector.collect()
    # Assert if the facts are as expected
    assert(facts_dict == {'apparmor': {'status': 'disabled'}})

# Generated at 2022-06-13 02:20:40.121272
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_facts = ApparmorFactCollector()
    collected_facts = apparmor_facts.collect()
    assert 'apparmor' in collected_facts
    assert 'status' in collected_facts['apparmor']

# Generated at 2022-06-13 02:20:48.030803
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    import pytest
    import mock
    import os

    fc = ApparmorFactCollector()

    # Test when apparmor is disabled
    with mock.patch.object(os.path, 'exists', side_effect=[False]):
        assert fc.collect() == {'apparmor': {'status': 'disabled'}}

    # Test when apparmor is enabled
    with mock.patch.object(os.path, 'exists', side_effect=[True]):
        assert fc.collect() == {'apparmor': {'status': 'enabled'}}

# vim: expandtab:tabstop=4:shiftwidth=4

# Generated at 2022-06-13 02:20:51.899549
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
	afc = ApparmorFactCollector()
	print(afc.collect())
	
if __name__ == '__main__':
	test_ApparmorFactCollector_collect()

# Generated at 2022-06-13 02:20:56.649275
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    """
    Return facts related to apparmor
    """
    facts = ApparmorFactCollector()
    if os.path.exists('/sys/kernel/security/apparmor'):
        assert facts.collect() == { 'apparmor' : {'status': 'enabled'} }
    else:
        assert facts.collect() == { 'apparmor' : {'status': 'disabled'} }


# Generated at 2022-06-13 02:21:08.939956
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact = ApparmorFactCollector()

    # Mock the methods
    apparmor_fact.collect(None, {})

    # Test the type of the return
    assert isinstance(apparmor_fact.collect(), dict)

    # Test the return value of function collect
    if os.path.exists('/sys/kernel/security/apparmor'):
        assert 'status' in apparmor_fact.collect()['apparmor']
        assert apparmor_fact.collect()['apparmor']['status'] == 'enabled'
    else:
        assert 'status' in apparmor_fact.collect()['apparmor']
        assert apparmor_fact.collect()['apparmor']['status'] == 'disabled'

# Generated at 2022-06-13 02:21:12.305546
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    # test empty
    obj = ApparmorFactCollector()
    facts = obj.collect()
    assert 'apparmor' in facts

# Generated at 2022-06-13 02:21:14.305198
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact_collector = ApparmorFactCollector()
    apparmor_facts = apparmor_fact_collector.collect()
    assert 'apparmor' in apparmor_facts

# Generated at 2022-06-13 02:21:16.045551
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact = ApparmorFactCollector()
    res = apparmor_fact.collect()
    assert isinstance(res['apparmor'], dict)

# Generated at 2022-06-13 02:21:17.694248
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    f_collector = ApparmorFactCollector()
    assert(f_collector.collect()['apparmor']['status'] == 'enabled')

# Generated at 2022-06-13 02:21:19.356533
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    collector = ApparmorFactCollector()
    facts_dict = collector.collect()
    assert facts_dict['apparmor']['status'] == 'disabled'

# Generated at 2022-06-13 02:21:22.339623
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    a = ApparmorFactCollector()
    assert a.collect()['apparmor']['status'] == 'disabled'

# Generated at 2022-06-13 02:21:23.759724
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact_collector = ApparmorFactCollector()
    apparmor_fact_collector.collect()

# Generated at 2022-06-13 02:21:26.335440
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    afc = ApparmorFactCollector()
    facts = afc.collect()
    assert facts['apparmor']['status'] == 'disabled'

# Generated at 2022-06-13 02:21:33.740058
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    from ansible.module_utils.facts.collector import collect_subset_module_facts
    from ansible.module_utils.facts import FallbackFactCollector

    facts = collect_subset_module_facts(['apparmor'])
    assert facts['apparmor']['status'] in ["enabled", "disabled"]
    # Check that status is the *only* fact that got collected
    assert len(facts['apparmor'].keys()) == 1

# Generated at 2022-06-13 02:21:41.146562
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    fixture = ApparmorFactCollector()
    assert fixture.collect() == {'apparmor': {'status': 'enabled'}}

# Generated at 2022-06-13 02:21:46.324079
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    path = '/sys/kernel/security/apparmor'
    apparmor_collector = ApparmorFactCollector()
    if os.path.exists(path):
        result = apparmor_collector.collect()
        assert result == dict(apparmor=dict(status='enabled'))
    else:
        result = apparmor_collector.collect()
        assert result == dict(apparmor=dict(status='disabled'))

# Generated at 2022-06-13 02:21:49.878930
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    fact_collector = ApparmorFactCollector()
    collected_facts = {}
    fact_collector.collect(collected_facts=collected_facts)
    assert collected_facts['apparmor']['status'] == 'enabled'

# Generated at 2022-06-13 02:21:50.650420
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    ApparmorFactCollector()

# Generated at 2022-06-13 02:21:52.029385
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    result = ApparmorFactCollector().collect()
    assert result == {'apparmor': {'status': 'enabled'}}

# Generated at 2022-06-13 02:21:52.940042
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    assert ApparmorFactCollector().collect()

# Generated at 2022-06-13 02:21:53.811116
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    assert ApparmorFactCollector().collect() is not None

# Generated at 2022-06-13 02:21:58.216185
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    test_collector = ApparmorFactCollector()
    apparmor_facts = test_collector.collect()
    assert set(apparmor_facts.keys()) == set(('apparmor',))
    assert set(apparmor_facts['apparmor'].keys()) == set(('status',))
    assert apparmor_facts['apparmor']['status'].startswith(('disabled', 'enabled'))

# Generated at 2022-06-13 02:22:02.842841
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():

    class MockModule(object):
        pass

    class MockModuleUtils(object):
        pass

    class MockFactsCollector(object):
        pass

    class MockApparmorFactCollector(ApparmorFactCollector):

        def __init__(self, module):
            self.__module = module

        @property
        def module(self):
            return self.__module

        def _exec(self, command, check_rc=False, enforce_diff=True, data=''):
            return ""

    apparmor_status = ApparmorFactCollector._exec(['/bin/grep', 'apparmor /proc/self/status'])

    module = MockModule()
    module.get_bin_path = MockModuleUtils()
    module.run_command = MockModuleUtils()
    module.exit_json = MockModuleUt

# Generated at 2022-06-13 02:22:10.969494
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    # Create a Apparmor fact collector
    fact_collector = ApparmorFactCollector()

    # Call collect method
    facts = fact_collector.collect()

    # Test apparmor facts key present in facts, then test is not empty.
    assert 'apparmor' in facts
    assert facts['apparmor'] != {}
    assert 'status' in facts['apparmor']

# Load the collect method of the apparmor fact collector
collect = ApparmorFactCollector().collect
# Load the collect method of the apparmor fact collector
# (For unit test purpose)
test_collect = ApparmorFactCollector().collect

# Generated at 2022-06-13 02:22:23.397811
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    collector = ApparmorFactCollector()
    facts_dict = collector.collect()
    assert 'fact_ids' in facts_dict
    assert facts_dict['fact_ids'] == set()

# Generated at 2022-06-13 02:22:24.454895
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    a = ApparmorFactCollector
    # TODO: Add tests related to class collect method


# Generated at 2022-06-13 02:22:25.398316
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fc = ApparmorFactCollector()
    apparmor_fc.collect()

# Generated at 2022-06-13 02:22:32.752535
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    module_mock = type('module', (object,), {})()
    collected_facts_mock = type('collected_facts', (object,), {})()
    apparmor_facter = ApparmorFactCollector()
    # Case 1: When /sys/kernel/security/apparmor does not exists
    os.path.exists = lambda x: False
    assert apparmor_facter.collect(module_mock, collected_facts_mock) == {'apparmor': {'status': 'disabled'}}

    # Case 2: When /sys/kernel/security/apparmor exists
    # Will be covered as part of other unit test
    # as os.path.exists is mocked to False

# Generated at 2022-06-13 02:22:34.306400
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact = ApparmorFactCollector()
    assert apparmor_fact.collect() == {'apparmor': {'status': 'disabled'}}

# Generated at 2022-06-13 02:22:37.071465
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    collector = ApparmorFactCollector()
    facts_dict = collector.collect()
    assert 'apparmor' in facts_dict.keys()
    assert 'status' in facts_dict['apparmor'].keys()
    assert facts_dict['apparmor']['status'] in ['enabled', 'disabled']


# Generated at 2022-06-13 02:22:38.544735
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact_collector = ApparmorFactCollector()
    apparmor_fact_collector.collect()

# Generated at 2022-06-13 02:22:40.279347
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    ApparmorFactCollector._fact_ids = set()

    ApparmorFactCollector().collect()

# Generated at 2022-06-13 02:22:42.753066
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_facts = ApparmorFactCollector().collect()
    assert 'apparmor' in apparmor_facts
    assert 'status' in apparmor_facts['apparmor']

# Generated at 2022-06-13 02:22:46.240240
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    fixture = ApparmorFactCollector()
    res = fixture.collect()
    assert 'apparmor' in res
    assert res['apparmor']['status'] == 'enabled'

# Generated at 2022-06-13 02:23:11.128693
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_facts = ApparmorFactCollector()
    facts = apparmor_facts.collect()

    assert isinstance(facts, dict)
    assert isinstance(facts['apparmor'], dict)
    assert facts['apparmor']['status'] in ('enabled', 'disabled')

# Generated at 2022-06-13 02:23:16.414577
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    # Note: there is not current way to mock the existence of /sys/kernel/security/apparmor at the moment, but that is
    # not really an important thing to test
    afc = ApparmorFactCollector()
    assert afc.collect() == {'apparmor': {'status': 'disabled'}}

# Generated at 2022-06-13 02:23:17.146190
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    collector = ApparmorFactCollector()
    result = collector.collect()
    assert 'apparmor' in result

# Generated at 2022-06-13 02:23:23.100857
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    def mock_os_open(path):
        if path == '/sys/kernel/security/apparmor':
            return True
        else:
            return False

    def mock_os_path_exists(path):
        if path == '/sys/kernel/security/apparmor':
            return True
        else:
            return False

    apparmor_collector = ApparmorFactCollector()
    apparmor_collector.collect = mock_os_open
    apparmor_collector._exists = mock_os_path_exists
    assert apparmor_collector.collect() == {'apparmor': {'status': 'enabled'}}

# Generated at 2022-06-13 02:23:25.014468
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fc = ApparmorFactCollector()
    assert apparmor_fc.collect()

# Generated at 2022-06-13 02:23:32.896524
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    collector = ApparmorFactCollector()

    # given test data
    def test_data(path):
        return (
            (
                True,
                {
                    'apparmor': {
                        'status': 'enabled'
                    }
                }
            ),
            (
                False,
                {
                    'apparmor': {
                        'status': 'disabled'
                    }
                }
            )
        )

    for os.path.exists in test_data(path='/sys/kernel/security/apparmor'):
        assert collector.collect() == test_data
        assert collector.collect() == test_data

# Generated at 2022-06-13 02:23:35.425444
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    aa_fact_collector = ApparmorFactCollector()
    collected_facts = aa_fact_collector.collect()
    assert collected_facts['apparmor']['status'] == 'disabled'


# Generated at 2022-06-13 02:23:38.947477
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector

    collector = Collector()
    collector.collect_custom_facts = lambda x: {'custom_facts': {'fact1': 'value1'}}
    result = ApparmorFactCollector(collector).collect()
    assert result is not None
    assert 'custom_facts' in result
    assert 'apparmor' in result

# Generated at 2022-06-13 02:23:39.575484
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    pass
#    ApparmorFactCollector().collect()

# Generated at 2022-06-13 02:23:44.396864
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    from ansible.module_utils.facts.collector.apparmor import ApparmorFactCollector
    import json
    import os

    orig_path = os.path.isfile

# Generated at 2022-06-13 02:24:12.038793
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    if os.path.exists('/sys/kernel/security/apparmor'):
        exp_apparmor_facts = {'status': 'enabled'}
    else:
        exp_apparmor_facts = {'status': 'disabled'}

    apparmor_fact_collector = ApparmorFactCollector()
    apparmor_facts = apparmor_fact_collector.collect()
    apparmor_facts_dict = apparmor_facts['ansible_facts']
    assert apparmor_facts_dict.get('apparmor') == exp_apparmor_facts

# Generated at 2022-06-13 02:24:15.775533
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    with open('/sys/kernel/security/apparmor', 'w') as file_content:
        file_content.write('apparmor filesystem is mounted at /sys/kernel/security/apparmor')
        apparmor_results = ApparmorFactCollector().collect()
        assert apparmor_results['apparmor']['status'] == 'enabled'

    os.remove('/sys/kernel/security/apparmor')
    apparmor_results = ApparmorFactCollector().collect()
    assert apparmor_results['apparmor']['status'] == 'disabled'

# Generated at 2022-06-13 02:24:20.019939
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    module = None
    collected_facts = None
    apparmor_fact_collector = ApparmorFactCollector()
    result = apparmor_fact_collector.collect(module, collected_facts)
    assert result is not None and result['apparmor'] is not None

# Generated at 2022-06-13 02:24:22.465928
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_collector = ApparmorFactCollector()
    apparmor_collector._module = ''
    apparmor_collector._collected_facts = ''
    apparmor_collector.collect()

# Generated at 2022-06-13 02:24:24.693645
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    fact_collector = ApparmorFactCollector()
    facts = fact_collector.collect()
    assert facts['apparmor']['status'] == 'disabled'

# Generated at 2022-06-13 02:24:29.671749
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact_collector = ApparmorFactCollector()
    result = apparmor_fact_collector.collect()

    assert 'apparmor' in result
    assert type(result['apparmor']) == dict
    assert len(result['apparmor']) == 1
    assert 'status' in result['apparmor']
    assert type(result['apparmor']['status']) == str

# Generated at 2022-06-13 02:24:36.921453
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    from ansible.module_utils.facts.collector import FactsCollector
    from ansible.module_utils.facts.system.apparmor import ApparmorFactCollector
    from ansible.module_utils.facts import FAKE_3_MODULE_UTILS_PATH

    module_utils_importers = [FAKE_3_MODULE_UTILS_PATH]

    ApparmorFactCollector.collect()

    facts_collector = FactsCollector(module_utils_importers=module_utils_importers)

    facts_collector.collect(module=None, collected_facts=None)

    # FactsCollector.populate() is only called from FactsCache.get_facts(),
    # but the latter is not a public API and therefore not mocked.
    #
    # However, FactsCollector.populate() is indirectly tested by

# Generated at 2022-06-13 02:24:40.156849
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    aafc_obj = ApparmorFactCollector()
    return_dict = aafc_obj.collect()
    assert return_dict.get('apparmor') == {'status': 'enabled'}

# Generated at 2022-06-13 02:24:43.551780
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact_collector = ApparmorFactCollector()
    result = apparmor_fact_collector.collect()
    assert result.get('apparmor') == {'status': 'disabled'}

# Generated at 2022-06-13 02:24:46.526052
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    facts_collector = ApparmorFactCollector()
    facts_dict = facts_collector.collect()
    assert facts_dict['apparmor']['status'] == 'enabled'

# Generated at 2022-06-13 02:25:38.112869
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    collector = ApparmorFactCollector()
    data = collector.collect()
    assert data['apparmor']['status'] == 'disabled'

# Generated at 2022-06-13 02:25:43.601817
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact_collector = ApparmorFactCollector()
    assert apparmor_fact_collector.collect() == {'apparmor': {'status': 'enabled'}}
    apparmor_fact_collector._module.params = {'gather_subset': ['!all', 'apparmor']}
    assert apparmor_fact_collector.collect() == {}

# Generated at 2022-06-13 02:25:51.325507
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    # results reference
    result = {'apparmor':
                      {'status': 'enabled'}}

    # Init module object
    module = None

    # Init collected_facts
    collected_facts = {
        "filesystems": [],
        "dns": {},
        "mounts": [],
        "ansible_proc_uptime": {},
        "devices": {},
        "distribution": None,
        "distribution_release": None,
        "distribution_version": None,
        "virtualization_type": None,
        "virtualization_role": None
    }

    # Test
    result = ApparmorFactCollector.collect(module, collected_facts)
    assert result == {'apparmor': {'status': 'enabled'}}

# Generated at 2022-06-13 02:25:54.098842
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    fact_collector = ApparmorFactCollector()
    facts = fact_collector.collect()
    assert 'apparmor' in facts.keys()
    assert 'status' in facts['apparmor'].keys()
    assert facts['apparmor']['status'] in ['enabled', 'disabled']

# Generated at 2022-06-13 02:26:00.410096
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    # creating object
    c = ApparmorFactCollector()
    # calling method
    result = c.collect()
    assert result != {}
    # test returned data
    if os.path.exists('/sys/kernel/security/apparmor'):
        assert result['apparmor']['status'] == 'enabled'
    else:
        assert result['apparmor']['status'] == 'disabled'

# Generated at 2022-06-13 02:26:02.695869
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_facts = ApparmorFactCollector()
    result = apparmor_facts.collect({}, {})
    assert result['apparmor']['status'] == 'disabled'

# Generated at 2022-06-13 02:26:04.028379
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_facts = ApparmorFactCollector()
    apparmor_facts.collect()

# Generated at 2022-06-13 02:26:06.632148
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    #get facts instance
    apparmor = ApparmorFactCollector()
    #get facts
    apparmor_facts = apparmor.collect()
    #test facts
    assert {'apparmor': {'status': 'enabled'}} == apparmor_facts

# Generated at 2022-06-13 02:26:12.045565
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():

    # Create instance of ApparmorFactCollector
    apparmor_fact_collector = ApparmorFactCollector()
    apparmor_fact_collector._module = None

    # Create apparmor keys
    apparmor_keys = set()
    apparmor_keys.add('status')

    # Create apparmor values
    apparmor_values = dict()

    # Create expected dict
    expected_dict = dict()
    expected_dict['apparmor'] = dict()
    expected_dict['apparmor']['status'] = 'enabled'

    # Unit test
    apparmor_fact_collector._fact_ids = apparmor_keys
    apparmor_fact_collector._collected_facts = apparmor_values
    ret_dict = apparmor_fact_collector.collect()

    # Check the compare variable
    assert ret_dict == expected_

# Generated at 2022-06-13 02:26:13.455929
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    collect = ApparmorFactCollector()
    assert collect.collect()['apparmor']

# Generated at 2022-06-13 02:28:12.558751
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    # Create ApparmorFactCollector object and
    # mock assertTrue and assertFalse in order to
    # fake the existence of /sys/kernel/security/apparmor
    apparmor_fact_collector = ApparmorFactCollector()
    def fake_assertTrue(expr):
        apparmor_fact_collector.assertTrue = lambda x: None
        assert expr
    def fake_assertFalse(expr):
        apparmor_fact_collector.assertFalse = lambda x: None
        assert not expr

    # Fake the existence of /sys/kernel/security/apparmor
    apparmor_fact_collector.assertTrue = lambda x: fake_assertTrue(x)
    apparmor_fact_collector.assertFalse = lambda x: fake_assertFalse(x)
    facts_dict = apparmor_fact_collector.collect()
    assert facts

# Generated at 2022-06-13 02:28:13.579413
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    pass

# Generated at 2022-06-13 02:28:17.929717
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    # Setup
    apparmor_module = ApparmorFactCollector()
    apparmor_facts = {}

    # Act
    apparmor_facts = apparmor_module.collect()

    # Assert
    assert apparmor_facts['apparmor']['status'] == 'enabled'

# Generated at 2022-06-13 02:28:19.914291
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_collector = ApparmorFactCollector()
    apparmor_facts = apparmor_collector.collect()

    assert 'apparmor' in apparmor_facts

# Generated at 2022-06-13 02:28:23.348083
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    os.path.exists = lambda path: path == '/sys/kernel/security/apparmor'
    apparmor_fact_collector = ApparmorFactCollector()

    assert apparmor_fact_collector.collect() == \
        {'apparmor': {'status': 'enabled'}}

# Generated at 2022-06-13 02:28:27.721461
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    obj = ApparmorFactCollector()
    assert obj.name == 'apparmor'
    assert obj._fact_ids == set()
    assert obj.collect() == {'apparmor': {'status': 'disabled'}}
    assert obj.collect() == {'apparmor': {'status': 'disabled'}}

# Generated at 2022-06-13 02:28:31.999970
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    test_collector = ApparmorFactCollector()
    facts = test_collector.collect()
    status = facts['apparmor']['status']
    if status != 'enabled' and status != 'disabled':
        raise ValueError("status value %s is not valid" % status) 

if __name__ == '__main__':
    test_ApparmorFactCollector_collect()

# Generated at 2022-06-13 02:28:39.049318
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes

    # Create mock module
    mock_module = basic.AnsibleModule(argument_spec={})

    # Create mock facts
    mock_facts = {}

    # Create and initialize ApparmorFactCollector object
    apparmor_fact_collector = ApparmorFactCollector(mock_module)
    apparmor_fact_collector.collect(module=mock_module, collected_facts=mock_facts)

    assert mock_facts == {to_bytes('apparmor'): to_bytes('enabled')}

# Generated at 2022-06-13 02:28:41.129892
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor = ApparmorFactCollector()
    test_apparmor = {
        'apparmor': {
            'status': 'enabled'
        }
    }
    assert apparmor.collect() == test_apparmor

# Generated at 2022-06-13 02:28:44.482188
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    module_exits_mock = {'ansible_facts': {'apparmor': {'status': 'enabled'}}}
    module_not_exits_mock = {'ansible_facts': {'apparmor': {'status': 'disabled'}}}
    collector = ApparmorFactCollector()
    collector._exists = lambda path: True
    assert collector.collect() == module_exits_mock
    collector._exists = lambda path: False
    assert collector.collect() == module_not_exits_mock