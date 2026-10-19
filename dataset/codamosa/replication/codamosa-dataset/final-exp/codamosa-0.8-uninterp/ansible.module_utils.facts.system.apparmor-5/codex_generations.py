

# Generated at 2022-06-13 02:19:44.761685
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    aafc = ApparmorFactCollector()
    aafc.collect()
    assert aafc.name == 'apparmor'

# Generated at 2022-06-13 02:19:50.900242
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_facts_collector_obj=ApparmorFactCollector()
    actual_apparmor_facts_result = apparmor_facts_collector_obj.collect()
    expected_apparmor_facts_result = {'apparmor': {'status': 'disabled'}}
    assert actual_apparmor_facts_result==expected_apparmor_facts_result

# Generated at 2022-06-13 02:19:53.036202
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact_collector = ApparmorFactCollector()
    expected_result = {
                       'apparmor':{
                                   'status':'enabled'
                                  }
                       }
    result = apparmor_fact_collector.collect()
    assert result == expected_result


# Generated at 2022-06-13 02:19:55.260025
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact = ApparmorFactCollector()
    apparmor_fact_list = apparmor_fact.collect()
    print(apparmor_fact_list)

# Generated at 2022-06-13 02:20:05.967457
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    before = {"apparmor": {"status": "enabled"}}
    def fake_os_path_exists(path):
        return True

    def fake_module_utils_get_module_path():
        return '/usr/local/lib/python2.7/dist-packages/ansible/module_utils/'

    import sys
    import __builtin__
    __builtin__.__dict__['os'] = __import__('os')
    import os
    import __builtin__
    os.path.exists = fake_os_path_exists

    import __builtin__
    __builtin__.__dict__['module_utils'] = __import__('module_utils')
    import module_utils
    module_utils.module_utils_get_module_path = fake_module_utils_get_module_path

   

# Generated at 2022-06-13 02:20:09.018084
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    collector = ApparmorFactCollector()
    results = collector.collect()

    assert 'apparmor' in results
    assert 'status' in results.get('apparmor')
    assert results.get('apparmor').get('status') == 'disabled'


# Generated at 2022-06-13 02:20:10.896616
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
  assert("apparmor" in ApparmorFactCollector().collect())

# Generated at 2022-06-13 02:20:12.848562
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    aafc = ApparmorFactCollector()
    aafc.collect()

# Generated at 2022-06-13 02:20:14.345857
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmorFactCollector = ApparmorFactCollector()
    apparmorFactCollector.collect()



# Generated at 2022-06-13 02:20:15.679627
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_collector = ApparmorFactCollector()
    assert not apparmor_collector.collect()


# Generated at 2022-06-13 02:20:20.245209
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    # Setup
    module = None
    apparmor_fact_collector = ApparmorFactCollector()

    # Run
    results = apparmor_fact_collector.collect(module)

    # Test
    assert 'apparmor' in results

    # Cleanup

# Generated at 2022-06-13 02:20:22.679998
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    aafc = ApparmorFactCollector()
    facts_dict = aafc.collect()
    assert isinstance(facts_dict, dict)
    assert 'apparmor' in facts_dict
    assert isinstance(facts_dict['apparmor'], dict)

# Generated at 2022-06-13 02:20:24.376457
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    aafc = ApparmorFactCollector()
    aafc.collect()
    assert aafc.collect() == {'apparmor': {'status': 'disabled'}}

# Generated at 2022-06-13 02:20:25.862610
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    my_obj = ApparmorFactCollector()
    my_vars = my_obj.collect()
    assert my_vars['apparmor']['status'] in ['enabled', 'disabled']

# Generated at 2022-06-13 02:20:36.194615
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact_collector = ApparmorFactCollector()
    # Initialize ansible-module-utils/facts/collectors/apparmor.py
    # Test case 1:
    # Test if Apparmor is enbaled
    # Expected result: 'apparmor': {'status': 'enabled'}
    assert apparmor_fact_collector.collect() == {'apparmor': {'status': 'enabled'}}
    # Test case 2:
    # Test if Apparmor is enbaled
    # Expected result: 'apparmor': {'status': 'enabled'}
    apparmor_fact_collector.name = 'apparmor'
    assert apparmor_fact_collector.collect() == {'apparmor': {'status': 'enabled'}}

# Generated at 2022-06-13 02:20:42.113865
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():

    # Create a test instance of ApparmorFactCollector
    apparmor_collector = ApparmorFactCollector()
    # Test output
    apparmor_fact = apparmor_collector.collect()
    # Assert the output in the test
    assert apparmor_fact['apparmor']['status'] == 'disabled', \
        'Test Failed: Invalid apparmor status after collect.'


# Generated at 2022-06-13 02:20:46.775879
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    # Create instance of ApparmorFactCollector class
    apparmor_fact_collector = ApparmorFactCollector()
    # Execute the method collect of the class ApparmorFactCollector
    apparmor_fact_collector.collect()
    # Check if the method collect successfully executed
    assert apparmor_fact_collector is not None

# Generated at 2022-06-13 02:20:53.470455
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    module = BaseFactCollector()
    collected_facts = {}
    apparmor_fact = ApparmorFactCollector()
    apparmor_dict = apparmor_fact.collect(module, collected_facts)
    assert apparmor_dict is not None
    apparmor_dict = apparmor_dict['apparmor']
    assert apparmor_dict is not None
    assert apparmor_dict['status'] is not None
    assert 'apparmor' in collected_facts
    assert collected_facts['apparmor']['status'] is not None

# Generated at 2022-06-13 02:20:54.361221
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    ApparmorFactCollector().collect()

# Generated at 2022-06-13 02:20:57.473556
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    import os
    apparmor_fact_collector = ApparmorFactCollector()
    os.path.exists = lambda x: True
    results = apparmor_fact_collector.collect()

    assert results['apparmor']['status'] == 'enabled'

# Generated at 2022-06-13 02:21:07.076601
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():

    # Initialize mock test data
    collected_facts = {}

    # Executing module and comparing results
    apparmorFactCollector = ApparmorFactCollector()
    results = apparmorFactCollector.collect(None, collected_facts)

    assert results == {'apparmor': {'status': 'disabled'}}

# Generated at 2022-06-13 02:21:12.086565
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact_collector = ApparmorFactCollector()
    fact_data = apparmor_fact_collector.collect()
    assert 'apparmor' in fact_data
    assert 'status' in fact_data['apparmor']


# vim: set et ts=4 sw=4 :

# Generated at 2022-06-13 02:21:15.372349
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact_collector = ApparmorFactCollector()

    # Test - When status of apparmor is disabled, then apparmor status should be set to disabled
    apparmor_fact_collector.collect()
    assert apparmor_fact_collector.fact_subset['apparmor']['status'] == 'disabled'

# Generated at 2022-06-13 02:21:17.265400
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    test_ApparmorFactCollector = ApparmorFactCollector()
    facts_dict = test_ApparmorFactCollector.collect()
    assert facts_dict.get('apparmor') is not None

# Generated at 2022-06-13 02:21:18.575368
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    arr = {'apparmor': {'status': 'enabled'}}
    assert arr == ApparmorFactCollector().collect()

# Generated at 2022-06-13 02:21:23.611517
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():

    fact_module_name = 'ansible.module_utils.facts.system.apparmor.ApparmorFactCollector'
    fact_module = __import__(fact_module_name)
    # Collects two facts - apparmor status and Apparmor library version
    apparmor_fact_collector = getattr(fact_module, 'ApparmorFactCollector')
    apparmor_facts = apparmor_fact_collector()
    # Extracts apparmor facts only
    apparmor_facts = apparmor_facts.collect()['apparmor']

    assert apparmor_facts['status'] in ('enabled', 'disabled')

# Generated at 2022-06-13 02:21:25.483176
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    a = ApparmorFactCollector()
    a.collect()

# Generated at 2022-06-13 02:21:29.498270
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    test = ApparmorFactCollector()
    assert test.collect() == {
        'apparmor': {
            'status': 'disabled'
        }
    }
    assert test.collect() == {}

# Generated at 2022-06-13 02:21:33.684263
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact_collector = ApparmorFactCollector()
    facts_dict = apparmor_fact_collector.collect()
    assert facts_dict['apparmor']['status'] == 'disabled'
    assert sorted(facts_dict.keys()) == ['apparmor']

# Generated at 2022-06-13 02:21:36.394211
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmorFactCollector = ApparmorFactCollector()
    apparmor_facts = apparmorFactCollector.collect()
    assert apparmor_facts['apparmor']['status'] in ['enabled','disabled']

# Generated at 2022-06-13 02:21:52.343002
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    import json
    import os

    open('/sys/kernel/security/apparmor', 'w').close()
    try:
        collector = ApparmorFactCollector()
        test_facts = collector.collect()
        assert test_facts == {'apparmor': {'status': 'enabled'}}

        os.remove('/sys/kernel/security/apparmor')
        test_facts = collector.collect()
        assert test_facts == {'apparmor': {'status': 'disabled'}}
    finally:
        try:
            os.remove('/sys/kernel/security/apparmor')
        except IOError:
            pass

# Generated at 2022-06-13 02:21:54.910011
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact_collector_obj = ApparmorFactCollector()

# Generated at 2022-06-13 02:21:57.701497
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    collector = ApparmorFactCollector()
    facts = collector.collect()
    assert 'apparmor' in facts
    assert 'status' in facts['apparmor']
    assert facts['apparmor']['status'] == 'disabled' or 'enabled'

# Generated at 2022-06-13 02:22:01.079140
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    # Create instance of ApparmorFactCollector
    ApparmorFactCollectorInstance = ApparmorFactCollector()
    # Execute method collect of ApparmorFactCollectorInstance
    result = ApparmorFactCollectorInstance.collect()
    assert result.get('apparmor').get('status') in ['enabled', 'disabled']

# Generated at 2022-06-13 02:22:02.461293
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact_collector = ApparmorFactCollector()
    assert apparmor_fact_collector.collect() == {'apparmor': {'status': 'disabled'}}

# Generated at 2022-06-13 02:22:05.758052
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_collector = ApparmorFactCollector()
    assert 'apparmor' in apparmor_collector.collect().keys()

# Generated at 2022-06-13 02:22:06.552189
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    ApparmorFactCollector().collect()


# Generated at 2022-06-13 02:22:09.798404
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_instance = ApparmorFactCollector()
    apparmor_facts = apparmor_instance.collect()
    assert apparmor_facts['apparmor']['status'] == 'enabled'

# Generated at 2022-06-13 02:22:17.468052
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    """Unit test for method 'collect' of class ApparmorFactCollector
    """

    # create an instance of ApparmorFactCollector
    apparmor_collector_ins = ApparmorFactCollector()

    # call method collect - enabled
    if os.path.exists('/sys/kernel/security/apparmor'):
        results = apparmor_collector_ins.collect()
        assert results['apparmor']['status'] == 'enabled'

    # call method collect - disabled
    if not os.path.exists('/sys/kernel/security/apparmor'):
        results = apparmor_collector_ins.collect()
        assert results['apparmor']['status'] == 'disabled'

# Generated at 2022-06-13 02:22:18.398591
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    ApparmorFactCollector.collect()

# Generated at 2022-06-13 02:22:42.973210
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    collector = ApparmorFactCollector()
    results = collector.collect()
    assert len(results) == 1
    assert 'apparmor' in results['apparmor']
    assert results['apparmor']['apparmor'] in ('enabled', 'disabled')

# Generated at 2022-06-13 02:22:46.090270
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    collector = ApparmorFactCollector()
    result = collector.collect()
    assert result['apparmor']['status'] == 'disabled'


# Generated at 2022-06-13 02:22:47.351167
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    aafc = ApparmorFactCollector()
    aafc.collect()

# Generated at 2022-06-13 02:22:50.136628
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_facts_dict = ApparmorFactCollector().collect()

    # check that the correct dict is returned
    assert apparmor_facts_dict == {'apparmor': {'status': 'disabled'}}

# Generated at 2022-06-13 02:22:52.655437
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    collector = ApparmorFactCollector()
    assert collector.collect() == {
        'apparmor': {
            'status': 'disabled'
        }
    }

# Generated at 2022-06-13 02:22:59.709587
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    '''Unit test for method collect of class ApparmorFactCollector'''
    apparmor_fact_collector = ApparmorFactCollector()

    real_returned_facts = apparmor_fact_collector.collect()

    # Create a mock for the method collect
    patcher_collect = mock.patch.object(ApparmorFactCollector, 'collect')
    # Start mocking the method collect
    mocked_collect = patcher_collect.start()
    # Mock the method collect to return the test fact
    mocked_collect.return_value = {'apparmor': {'status': 'enabled'}}
    # Run the method collect
    collect_returned_facts = apparmor_fact_collector.collect()
    # Stop mocking the method collect
    patcher_collect.stop()

    assert real_returned_facts == collect_returned_facts

# Generated at 2022-06-13 02:23:01.530278
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact = ApparmorFactCollector()
    assert 'apparmor' in apparmor_fact.collect()

# Generated at 2022-06-13 02:23:04.578167
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_facts = ApparmorFactCollector().collect()
    assert 'apparmor' in apparmor_facts.keys()
    assert 'status' in apparmor_facts['apparmor'].keys()

# Generated at 2022-06-13 02:23:06.912659
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmorCollector = ApparmorFactCollector()
    facts_dict = apparmorCollector.collect()
    assert facts_dict['apparmor'] == {'status': 'disabled'}

# Generated at 2022-06-13 02:23:12.579106
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    # create object
    apparmor_fact_collector = ApparmorFactCollector()
    # call method collect
    apparmor_facts = apparmor_fact_collector.collect()
    # create data for test
    if os.path.exists('/sys/kernel/security/apparmor'):
        apparmor_facts_expected = {'apparmor': {'status': 'enabled'}}
    else:
        apparmor_facts_expected = {'apparmor': {'status': 'disabled'}}
    # compare data
    assert apparmor_facts == apparmor_facts_expected

# Generated at 2022-06-13 02:23:58.787423
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    aafc = ApparmorFactCollector()
    # The method collect should return a dict
    assert isinstance(aafc.collect(), dict)

# Generated at 2022-06-13 02:23:59.849311
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    assert 'status' in ApparmorFactCollector().collect()['apparmor']

# Generated at 2022-06-13 02:24:02.479772
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    status = os.path.exists('/sys/kernel/security/apparmor')
    result = {
        'apparmor': {
            'status': 'enabled' if status else 'disabled'
        }
    }
    assert ApparmorFactCollector().collect() == result

# Generated at 2022-06-13 02:24:10.642395
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    import platform
    import os
    import tempfile

    def fake_platform_linux_distribution(distname='', version='', id='', supported_dists='arch,centos,debian,fedora,mandrake,mandriva,meego,redhat,suse,opensuse,ubuntu'):
        return '', '', ''

    def fake_os_path_exists(path='/sys/kernel/security/apparmor'):
        return True

    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True,
    )

    platform.linux_distribution = fake_platform_linux_distribution
    os.path.exists = fake_os_path_exists

    file, path = tempfile.mkstemp()


# Generated at 2022-06-13 02:24:11.366699
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    ApparmorFactCollector().collect()

# Generated at 2022-06-13 02:24:19.283895
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    def get_module_mock(params):
        return True

    def get_mk_temp_path_mock(path):
        return True

    import ansible.module_utils.facts.collector
    ansible.module_utils.facts.collector.get_module = get_module_mock
    ansible.module_utils.facts.collector.get_mk_temp_path = get_mk_temp_path_mock

    apps = ApparmorFactCollector()
    assert apps.collect() == {'apparmor': {'status': 'disabled'}}

# Generated at 2022-06-13 02:24:23.327314
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    module = None
    fc = ApparmorFactCollector(module)
    collected_facts = {}
    apparmor_facts = {}
    apparmor_facts['status'] = 'enabled'
    facts_dict = {}
    facts_dict['apparmor'] = apparmor_facts

    assert fc.collect(module, collected_facts) == facts_dict

# Generated at 2022-06-13 02:24:25.013634
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_collector = ApparmorFactCollector()
    apparmor_collector.collect()

# Generated at 2022-06-13 02:24:30.548849
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    """Unit test for method collect of class ApparmorFactCollector"""

    facts_dict = {}
    apparmor_facts = {}
    if os.path.exists('/sys/kernel/security/apparmor'):
        apparmor_facts['status'] = 'enabled'
    else:
        apparmor_facts['status'] = 'disabled'

    facts_dict['apparmor'] = apparmor_facts
    assert ApparmorFactCollector().collect() == facts_dict

# Generated at 2022-06-13 02:24:32.567456
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact_collector = ApparmorFactCollector(None, None)

    apparmor_facts = apparmor_fact_collector.collect()
    assert apparmor_facts is not None

# Generated at 2022-06-13 02:26:23.085655
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    # Test for os.path.exists(/sys/kernel/security/apparmor) is True
    apparmor_status_enabled = ApparmorFactCollector()
    test_facts = {'apparmor': {'status': 'enabled'}}
    apparmor_status_enabled.collect()
    assert test_facts == apparmor_status_enabled.collect()

    # Test for os.path.exists(/sys/kernel/security/apparmor) is False
    apparmor_status_disabled = ApparmorFactCollector()
    test_facts = {'apparmor': {'status': 'disabled'}}
    apparmor_status_disabled.collect()
    assert test_facts == apparmor_status_disabled.collect()

# Generated at 2022-06-13 02:26:24.759525
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact_collector = ApparmorFactCollector()
    assert apparmor_fact_collector.collect().keys() == set(['apparmor'])

# Generated at 2022-06-13 02:26:28.739337
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    if os.path.exists('/sys/kernel/security/apparmor'):
        status = 'enabled'
    else:
        status = 'disabled'

    assert(ApparmorFactCollector.collect() == {'apparmor': {'status': status}})

# Generated at 2022-06-13 02:26:30.743464
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    print("test_ApparmorFactCollector_collect")
    apparmor_collector = ApparmorFactCollector()
    apparmor_collector.collect()

# Generated at 2022-06-13 02:26:33.257041
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    collector = ApparmorFactCollector()
    facts = collector.collect()
    assert facts['apparmor']['status'] == 'enabled'

# Generated at 2022-06-13 02:26:36.228284
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():

    apparmor_fact_collector = ApparmorFactCollector()
    facts_dict = apparmor_fact_collector.collect()

    assert 'apparmor' in facts_dict.keys()
    assert 'status' in facts_dict['apparmor'].keys()

# Generated at 2022-06-13 02:26:37.987532
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact_collector_obj = ApparmorFactCollector()

    assert apparmor_fact_collector_obj.collect() == {}

# Generated at 2022-06-13 02:26:40.221396
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    fact = ApparmorFactCollector()
    collected_facts = fact.collect()
    assert collected_facts['apparmor']['status'] == 'disabled'

# Generated at 2022-06-13 02:26:44.494455
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    """
    Unit test for ApparmorFactCollector.collect
    """
    fake_collected_facts = {}
    fact_collector = ApparmorFactCollector()
    result = fact_collector.collect(collected_facts=fake_collected_facts)
    assert 'apparmor' in result

# Generated at 2022-06-13 02:26:47.322881
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor = ApparmorFactCollector()
    facts = apparmor.collect(None, {})

    assert facts['apparmor']['status'] == 'disabled'