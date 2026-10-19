

# Generated at 2022-06-13 02:19:43.513147
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    """Unit test for method collect of class ApparmorFactCollector"""

    apparmor_fact_collector = ApparmorFactCollector()
    facts = apparmor_fact_collector.collect()
    assert facts['apparmor']['status'] == 'disabled'

# Generated at 2022-06-13 02:19:43.946167
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    pass

# Generated at 2022-06-13 02:19:48.814127
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    # Don't try to load these modules, since we only use them for patching
    import os
    import os.path

    # Don't try to get the filesystems, since we only need os.path.exists
    def mock_os_path_exists(path):
        return False

    # Don't try to read /proc/*/cmdline for each process
    def mock_os_listdir(path):
        return []

    from ansible.module_utils.facts.collector import BaseFactCollector

    test_object = ApparmorFactCollector()

    # Don't try to get the filesystems, since we only need os.path.exists
    os.path.exists = mock_os_path_exists

    collected_facts = test_object.collect()


# Generated at 2022-06-13 02:19:56.682457
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact_collector = ApparmorFactCollector()
    apparmor_fact_collector._module = object()
    apparmor_fact_collector._collect_platform_facts = object()
    apparmor_fact_collector._get_filesystem_mounts = object()
    apparmor_fact_collector._populate_mounts_facts = object()
    apparmor_fact_collector._parse_sys_class_net = object()
    apparmor_fact_collector._get_distribution = object()
    apparmor_fact_collector._get_cmdline = object()
    apparmor_fact_collector._get_all_options = object()
    apparmor_fact_collector._get_dmi_facts = object()
    apparmor_fact_collector._get_pkg_mgr_facts = object()

# Generated at 2022-06-13 02:19:59.031006
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    fact_collector = ApparmorFactCollector()
    collected_facts = fact_collector.collect()
    assert collected_facts['apparmor']['status'] in ['enabled', 'disabled']

# Generated at 2022-06-13 02:20:01.906839
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    my_collector = ApparmorFactCollector()
    collected_result = my_collector.collect()
    assert collected_result[my_collector.name]

# Generated at 2022-06-13 02:20:07.227846
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact_collector = ApparmorFactCollector()

    # Create an empty dict to be used as collected_facts and call the method
    # to test
    facts_dict = apparmor_fact_collector.collect(collected_facts={})

    # Assert if returned facts dict has the value for 'apparmor' key
    assert 'apparmor' in facts_dict

# Generated at 2022-06-13 02:20:08.933900
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_facts = ApparmorFactCollector().collect()
    assert apparmor_facts['apparmor'] == {'status': 'disabled'}

# Generated at 2022-06-13 02:20:10.806091
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    """mock the test"""
    res = {
        'apparmor': {
            'status': 'enabled'
        }
    }
    assert ApparmorFactCollector().collect() == res

# Generated at 2022-06-13 02:20:13.095289
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_facts = ApparmorFactCollector().collect()
    assert 'apparmor' in apparmor_facts

# Generated at 2022-06-13 02:20:17.833467
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    f = ApparmorFactCollector()
    with open('/sys/kernel/security/apparmor', 'w+') as fp:
        assert f.collect() == {'apparmor': {'status': 'enabled'}}
    with open('/sys/kernel/security/apparmor', 'w+') as fp:
        assert f.collect() == {'apparmor': {'status': 'disabled'}}

# Generated at 2022-06-13 02:20:19.438548
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():

    obj = ApparmorFactCollector()
    actual = obj.collect()
    assert actual == {
        'apparmor': {
            'status': 'enabled'
        }
    }

# Test specific to class ApparmorFactCollector

# Generated at 2022-06-13 02:20:22.469482
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    m = ApparmorFactCollector(None)
    res = m.collect()
    assert 'apparmor' in res
    assert 'status' in res['apparmor']
    assert res['apparmor']['status'] in ('enabled', 'disabled')

# Generated at 2022-06-13 02:20:32.226266
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():

    #Create dummy ansible module
    class DummyAnsibleModule():
        def fail_json(self, *args, **kwargs):
            class DummyResult():
                def __init__(self, dummy_msg):
                    self.msg = dummy_msg
                def __getitem__(self, item):
                    return self.msg
            raise Exception(DummyResult(*args, **kwargs))

    dummy_ansible_module = DummyAnsibleModule()

    #Create dummy facts
    collected_facts = {}

    #Create apparmor collector
    apparmor_collector = ApparmorFactCollector()

    #Collect facts, this should pass and return the status of 'apparmor'
    apparmor_collector.collect(DummyAnsibleModule(), collected_facts)

# Generated at 2022-06-13 02:20:39.048392
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    # test when apparmor is enabled
    test_path = '/tmp/test_path/'
    os.makedirs(test_path)
    os.symlink('/sys/kernel/security', test_path + 'apparmor')
    apparmor_fact = ApparmorFactCollector()
    facts_dict = apparmor_fact.collect()
    assert facts_dict['apparmor']['status'] == 'enabled'
    # test when apparmor is disabled
    os.remove(test_path + 'apparmor')
    facts_dict = apparmor_fact.collect()
    assert facts_dict['apparmor']['status'] == 'disabled'
    # cleanup
    os.rmdir(test_path)

# Generated at 2022-06-13 02:20:42.903966
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_facts = ApparmorFactCollector().collect(None, None)
    assert 'apparmor' in apparmor_facts
    assert 'status' in apparmor_facts['apparmor']
    assert apparmor_facts['apparmor']['status'] in ['enabled', 'disabled']

# Generated at 2022-06-13 02:20:46.070229
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact = ApparmorFactCollector()
    assert apparmor_fact.collect() == {'apparmor': {'status': 'enabled'}}

# Generated at 2022-06-13 02:20:47.205658
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    aafc = ApparmorFactCollector()
    assert aafc.collect()

# Generated at 2022-06-13 02:20:49.399408
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    myCollector = ApparmorFactCollector()
    assert myCollector.collect()['apparmor']['status'] in ('enabled', 'disabled')

# Generated at 2022-06-13 02:20:51.949282
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    result = ApparmorFactCollector().collect()
    assert type(result['apparmor']) is dict

# Generated at 2022-06-13 02:21:01.365717
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():

    # create a instance of ApparmorFactCollector and execute collect method
    apparmor_collector = ApparmorFactCollector()
    result = apparmor_collector.collect()
    print(result)

    # check for the final result
    expected_result = {'apparmor': {'status': 'enabled'}}
    assert result == expected_result

if __name__ == '__main__':
    test_ApparmorFactCollector_collect()

# Generated at 2022-06-13 02:21:08.556311
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():

    # Create instance of class ApparmorFactCollector
    apparmor_fact_collector = ApparmorFactCollector()

    # Create instance of class module.params
    module_params = {}

    # Create instance of class facts.dict
    collected_facts = {}

    # Set module.params['apparmor'] to True
    module_params['apparmor'] = True

    # Call method collect of class ApparmorFactCollector
    facts = apparmor_fact_collector.collect(module_params, collected_facts)

    assert facts == {'apparmor': {'status': 'disabled'}}

# Generated at 2022-06-13 02:21:12.614902
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    import json

    apparmor_fact_collector = ApparmorFactCollector()
    apparmor_facts = apparmor_fact_collector.collect() 
    assert json.dumps(apparmor_facts) != ""

# Generated at 2022-06-13 02:21:17.048065
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    """
    This unit test checks if it is possible
    to collect apparmor fact
    """
    from ansible.module_utils.facts.collector import get_collector_instance

    apparmor = get_collector_instance(ApparmorFactCollector)
    apparmor_facts = apparmor.collect({}, {})
    assert apparmor_facts == {'apparmor': {'status': 'enabled'}}

# Generated at 2022-06-13 02:21:19.831299
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    module = None
    collected_facts = {}
    apparmor_fact = ApparmorFactCollector()
    apparmor_fact.collect(module, collected_facts)
    aaf = collected_facts['apparmor']
    if aaf:
        assert 'status' in aaf

# Generated at 2022-06-13 02:21:22.691849
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    if not ApparmorFactCollector.can_run():
        return

    # Init
    apparmor_fact_collector = ApparmorFactCollector()

    # Run
    apparmor_fact_collector.collect()

    # Verify
    assert apparmor_fact_collector.data.get('apparmor') is not None
    assert apparmor_fact_collector.data.get('apparmor').get('status') is not None

# Generated at 2022-06-13 02:21:27.570402
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    """Test if apparmor fact is obtained correctly"""
    x = ApparmorFactCollector()
    results = x.collect()
    assert isinstance(results, dict)
    assert results.get('apparmor', None) is not None
    assert isinstance(results.get('apparmor', None), dict)

# Generated at 2022-06-13 02:21:32.941034
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    # create mock object for module
    module = MagicMock()
    # create mock object for collected facts
    collected_facts = {'kernel': {}}
    # create object for ApparmorFactCollector class
    apparmor_fact_collector = ApparmorFactCollector()
    apparmor_fact_collector.collect(module, collected_facts)

# Generated at 2022-06-13 02:21:35.475141
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_collector = ApparmorFactCollector()
    assert apparmor_collector.collect() == {'apparmor': {'status': 'disabled'}}


# Generated at 2022-06-13 02:21:37.352671
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    fact_collector = ApparmorFactCollector()
    ans = fact_collector.collect()
    assert ans['apparmor']['status'] == 'enabled'

# Generated at 2022-06-13 02:21:45.245464
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    aaf_collector = ApparmorFactCollector()
    assert aaf_collector != None

    facts_dict = aaf_collector.collect()
    assert facts_dict != None

# Generated at 2022-06-13 02:21:50.208839
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    mock_module = type('module', (object, ), {})()
    mock_module.params = { 'gather_subset': [ 'all' ] }
    mock_module.get_bin_path = lambda executable: ''
    mock_module.run_command = lambda _, check_rc=True: ''

    apparmor_facts = ApparmorFactCollector()
    result = apparmor_facts.collect(module=mock_module)
    assert result == {}

# Generated at 2022-06-13 02:21:52.498313
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    aafc = ApparmorFactCollector()
    aafc._module = 'apparmor'
    aafc._collect_subset = [ 'all' ]
    aafc.collect()

# Generated at 2022-06-13 02:21:54.428589
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmorFactCollector = ApparmorFactCollector()
    assert apparmorFactCollector.collect() == {'apparmor': {'status': 'disabled'}}

# Generated at 2022-06-13 02:21:55.660893
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    a = ApparmorFactCollector()
    a.collect()


# Generated at 2022-06-13 02:21:57.256247
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    import pytest
    from ansible.module_utils.facts.collector.apparmor import ApparmorFactCollector
    apparmor_obj = ApparmorFactCollector()
    apparmor_obj.collect()

# Generated at 2022-06-13 02:21:58.374765
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    pass

# vim: set et ts=4 sw=4 :

# Generated at 2022-06-13 02:22:00.752937
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact_collector = ApparmorFactCollector()
    result = apparmor_fact_collector.collect(module=None, collected_facts=None)
    assert result['apparmor']['status'] in ['enabled', 'disabled']

# Generated at 2022-06-13 02:22:02.243470
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_facts = ApparmorFactCollector()
    facts_dict = apparmor_facts.collect()
    assert 'apparmor' in facts_dict

# Generated at 2022-06-13 02:22:02.932581
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    ApparmorFactCollector().collect()

# Generated at 2022-06-13 02:22:17.131737
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    test_collector = ApparmorFactCollector(None)
    test_collector.collect()
    assert test_collector.fact_subset == ['apparmor']

# Generated at 2022-06-13 02:22:19.055174
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    collector = ApparmorFactCollector()
    assert len(collector.collect()) == 1
    assert set([collector.name]) == collector.collect().keys()

# Generated at 2022-06-13 02:22:21.180451
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    collect_method = ApparmorFactCollector().collect
    assert collect_method.__name__ == 'collect'

# Generated at 2022-06-13 02:22:29.764168
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    from ansible_collections.notstdlib.moveitallout.tests.unit.modules.facts import test_apparmor_fact_collector
    fs = test_apparmor_fact_collector.Fs()

    def exists_mock(path):
        if path == '/sys/kernel/security/apparmor':
            return True
        return False
    fs.exists_orig = os.path.exists
    os.path.exists = exists_mock
    fact_collector = ApparmorFactCollector()
    result = fact_collector.collect(None, None)
    assert result['apparmor']['status'] == 'enabled'
    os.path.exists = fs.exists_orig

# Generated at 2022-06-13 02:22:31.761101
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    fact_collector = ApparmorFactCollector()
    facts = fact_collector.collect(module=None, collected_facts=None)
    assert 'apparmor' in facts

# Generated at 2022-06-13 02:22:33.398822
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact = ApparmorFactCollector()
    assert apparmor_fact.collect()['apparmor']['status'] == 'enabled'

# Generated at 2022-06-13 02:22:35.478240
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    fact_collector = ApparmorFactCollector()
    assert isinstance(fact_collector.collect(), dict)

# Generated at 2022-06-13 02:22:36.879144
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_collector = ApparmorFactCollector()
    apparmor_collector.collect()

# Generated at 2022-06-13 02:22:40.196317
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    fact = ApparmorFactCollector()
    facts = fact.collect()

    assert fact.name == fact.name
    assert 'apparmor' in facts
    assert 'status' in facts['apparmor']
    assert facts['apparmor']['status'] == 'enabled'

# Generated at 2022-06-13 02:22:41.681797
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact_collector = ApparmorFactCollector()
    apparmor_fact_collector.collect() is not None

# Generated at 2022-06-13 02:23:09.467170
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    aafc = ApparmorFactCollector()
    results = aafc.collect(None, None)
    assert results['apparmor']['status'] == 'disabled'
    # Run tests to ensure that the status is correct for each.
    # enabled
    aafc._file_exists['/sys/kernel/security/apparmor'] = True
    results = aafc.collect(None, None)
    assert results['apparmor']['status'] == 'enabled'
    # disabled
    aafc._file_exists['/sys/kernel/security/apparmor'] = False
    results = aafc.collect(None, None)
    assert results['apparmor']['status'] == 'disabled'

# vim: set et ts=4 sw=4 :

# Generated at 2022-06-13 02:23:11.872794
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor = ApparmorFactCollector()
    assert apparmor.collect()['apparmor'] == {'status': 'enabled'}
    assert ApparmorFactCollector().collect()['apparmor'] == {'status': 'enabled'}



# Generated at 2022-06-13 02:23:15.878258
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    aafc = ApparmorFactCollector()
    facts_dict=aafc.collect()
    assert facts_dict['apparmor']['status'] in ['enabled','disabled']

# Generated at 2022-06-13 02:23:18.314781
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_facts = ApparmorFactCollector().collect()
    assert 'apparmor' in apparmor_facts
    assert 'status' in apparmor_facts['apparmor']

# Generated at 2022-06-13 02:23:22.676203
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    mod = {'path':  os.path}
    fact_collector = ApparmorFactCollector()
    facts = fact_collector.collect(mod, {})
    assert 'apparmor' in facts
    assert facts['apparmor']['status'] == 'enabled' or facts['apparmor']['status'] == 'disabled'

# Generated at 2022-06-13 02:23:26.342227
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor = ApparmorFactCollector(None)
    collected_facts = {}
    assert apparmor.collect(None, collected_facts) == {'apparmor': 
                                                        {'status': 'enabled'}}

# Generated at 2022-06-13 02:23:27.946824
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    test_collector = ApparmorFactCollector()
    test_collector.collect()


# Generated at 2022-06-13 02:23:35.393082
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
  # Test for non-existing directory
  os.path.isdir = Mock(side_effect=[True, False])
  apparmorfactcollector = ApparmorFactCollector()
  fact_list = apparmorfactcollector.collect()
  assert fact_list == {'apparmor': {'status': 'disabled'}}

  # Test for existing directory
  os.path.isdir = Mock(return_value=True)
  apparmorfactcollector = ApparmorFactCollector()
  fact_list = apparmorfactcollector.collect()
  assert fact_list == {'apparmor': {'status': 'enabled'}}

# Generated at 2022-06-13 02:23:37.192947
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor = ApparmorFactCollector()
    facts = apparmor.collect()
    assert facts == {'apparmor': {'status': 'disabled'}}

# Generated at 2022-06-13 02:23:44.974069
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    # Set up class and method to test.
    from ansible.module_utils.facts.collectors.apparmor.apparmor import ApparmorFactCollector
    collect_method = ApparmorFactCollector.collect
    # Set up object to use.
    collector_object = ApparmorFactCollector()
    # Set up expected results.
    # Here we verify that the method collects the same data as the
    # ApparmorFactCollector class definition.
    expected_results = ApparmorFactCollector._fact_ids
    # Verify results of method.
    assert collector_object.collect() == expected_results

# Generated at 2022-06-13 02:24:32.105269
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    fact_collector = ApparmorFactCollector()
    assert fact_collector.collect() == {
        'apparmor': {
            'status': 'disabled'
        }
    }



# Generated at 2022-06-13 02:24:33.474340
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    aa = ApparmorFactCollector()
    facts = aa.collect()
    assert 'apparmor' in facts

# Generated at 2022-06-13 02:24:36.369618
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    fact = ApparmorFactCollector()
    if os.path.exists('/sys/kernel/security/apparmor'):
        assert fact.collect() == {'apparmor': {'status': 'enabled'}}
    else:
        assert fact.collect() == {'apparmor': {'status': 'disabled'}}

# Generated at 2022-06-13 02:24:37.515262
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    collector = ApparmorFactCollector()
    assert collector.collect() == {'apparmor': {'status': 'disabled'}}

# Generated at 2022-06-13 02:24:39.201253
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    aafc = ApparmorFactCollector()

    apparmor_facts = aafc.collect()
    assert 'apparmor' in apparmor_facts
    assert 'status' in apparmor_facts['apparmor']

# Generated at 2022-06-13 02:24:42.685034
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    #This test cases are executed only on Linux
    if os.name != 'posix':
        return

    facts = ApparmorFactCollector().collect()
    assert 'apparmor' in facts
    assert 'status' in facts['apparmor']

# Generated at 2022-06-13 02:24:48.955371
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    expected_facts = {'apparmor': {'status': 'disabled'}}

    # Assign path to dummy file
    path = '/sys/kernel/security/apparmor_dummy'

    # Create dummy file
    open(path, 'a').close()

    # Check if file exists
    if os.path.exists(path):
        ApparmorFactCollector().collect()
        assert ApparmorFactCollector().collect() == expected_facts

    # Remove dummy file
    os.remove(path)

# Generated at 2022-06-13 02:24:50.387511
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact_collector = ApparmorFactCollector()
    assert apparmor_fact_collector.collect() == {}

# Generated at 2022-06-13 02:24:52.349704
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():

    facts = {}

    ApparmorFactCollector(None, facts=facts, name=None).collect()

    assert facts['apparmor'] == {'status': 'disabled'}

# Generated at 2022-06-13 02:24:53.985227
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact_collector = ApparmorFactCollector()
    result = apparmor_fact_collector.collect()
    assert 'apparmor' in result
    assert isinstance(result['apparmor'], dict)

# Generated at 2022-06-13 02:26:40.358753
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    assert isinstance(ApparmorFactCollector.collect(None), dict)

# Generated at 2022-06-13 02:26:43.780522
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    fact_collector = ApparmorFactCollector()
    result = fact_collector.collect()
    assert result['apparmor']
    assert result['apparmor']['status'] in ['enabled','disabled']


# Generated at 2022-06-13 02:26:48.202907
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    import os.path

    def os_path_exists(path):
        return True

    apparmorfactcollector = ApparmorFactCollector()
    apparmorfactcollector.collect()
    # Test if collect method has 'return' statement
    os.path.exists = os_path_exists
    apparmorfactcollector.collect()

# Generated at 2022-06-13 02:26:49.586164
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    mod = ApparmorFactCollector()
    assert mod.collect()

# Generated at 2022-06-13 02:26:55.467713
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    import re

    mocked_module = type("MockedModule", (), {})
    mocked_module.exit_json = lambda x: None

    collector = ApparmorFactCollector(MockedModule())
    result = collector.collect(mocked_module)

    assert re.match("^(enabled|disabled)$", result["apparmor"]["status"]) is not None

if __name__ == "__main__":
    test_ApparmorFactCollector_collect()

# Generated at 2022-06-13 02:27:03.632492
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():

    # Define expected return dictionary
    expected_return_dict={'apparmor': {'status': 'enabled'}}

    # Test with fake "facts" directory
    fake_facts_dir = '/tmp/fake_facts_dir'
    os.mkdir(fake_facts_dir)
    os.mkdir('%s/apparmor' % fake_facts_dir)
    module=None
    collected_facts={}
    apparmor_fact_collector = ApparmorFactCollector(module=module, collected_facts=collected_facts)
    apparmor_fact_collector.set_root_dir(root_dir=fake_facts_dir)
    returned_dict = apparmor_fact_collector.collect()

    # Verify return dictionary has correct content
    assert returned_dict == expected_return_dict
    # Delete fake "facts"

# Generated at 2022-06-13 02:27:08.793100
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    # We use this test to check Py3 compatibility
    if os.path.exists('/sys/kernel/security/apparmor'):
        assert ApparmorFactCollector().collect()['apparmor']['status'] == 'enabled' 
    else:
        assert ApparmorFactCollector().collect()['apparmor']['status'] == 'disabled'

# Generated at 2022-06-13 02:27:11.610730
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_dict = {}
    apparmor_dict['status'] = 'enabled'
    if os.path.exists('/sys/kernel/security/apparmor'):
        apparmor_dict['status'] = 'enabled'
    else:
        apparmor_dict['status'] = 'disabled'
    assert ApparmorFactCollector().collect()['apparmor'] == apparmor_dict

# Generated at 2022-06-13 02:27:13.164200
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    assert ApparmorFactCollector.collect()['apparmor']['status'] is not None

# Generated at 2022-06-13 02:27:15.855093
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_collector = ApparmorFactCollector()
    apparmor_collector.collect()
    os.path.exists('/sys/kernel/security/apparmor')