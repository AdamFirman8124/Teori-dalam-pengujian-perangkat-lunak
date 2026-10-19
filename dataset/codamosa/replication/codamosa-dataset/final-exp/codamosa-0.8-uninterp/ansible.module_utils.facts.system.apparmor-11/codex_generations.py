

# Generated at 2022-06-13 02:19:48.293857
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    """ Check if all expected facts are returned on Ubuntu, Debian and FreeBSD """
    facts = {}
    aaf = ApparmorFactCollector()

    # Run collect and check if the returned facts are as expected
    # Ubuntu and Debian
    facts['distribution'] = 'Ubuntu'
    facts['distribution_version'] = '16.04'
    facts['os_family'] = 'Debian'
    collected_facts = aaf.collect(collected_facts=facts)
    assert collected_facts == { 'apparmor': { 'status': 'enabled' }}, "Incorrect facts returned in Ubuntu"
    facts['distribution'] = 'Debian'
    facts['distribution_version'] = '8'
    collected_facts = aaf.collect(collected_facts=facts)

# Generated at 2022-06-13 02:19:56.545671
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    import pytest
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collectors.apparmor.apparmor import ApparmorFactCollector
    base_fact_collector = BaseFactCollector()
    base_fact_collector.collect = lambda: {'kernel': {'name': 'Linux'}}
    apparmor_fact_collector = ApparmorFactCollector()
    apparmor_fact_collector.collect = pytest.MagicMock(return_value={'status': 'disabled'})
    apparmor_fact_collector._collect_from_fact_file = pytest.MagicMock()
    ansible_facts = {}
    apparmor_fact_collector.collect(ansible_facts=ansible_facts)
    assert apparmor_fact_collector

# Generated at 2022-06-13 02:20:00.364743
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_collector = ApparmorFactCollector()
    apparmor_fact = apparmor_collector.collect()
    assert apparmor_fact
    print("Apparmor collect works")

if __name__ == '__main__':
    test_ApparmorFactCollector_collect()

# Generated at 2022-06-13 02:20:02.806510
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact_collector = ApparmorFactCollector()
    apparmor_fact_collector.collect({}, {})
# Tests ends here.



# Generated at 2022-06-13 02:20:06.755044
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    module = Mock(return_value=dict())
    collected_facts = dict()

    apparmor_collector = ApparmorFactCollector()

    apparmor_collector.collect(module=module, collected_facts=collected_facts)


# Generated at 2022-06-13 02:20:10.249787
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    class TestClass(object):
        def __init__(self):
            self.path = '/sys/kernel/security/apparmor'
        def exists(self, path):
            return self.path == path
    test_object = TestClass()
    assert ApparmorFactCollector().collect(module=None, collected_facts=None) == {'apparmor':{'status':'enabled'}}
    test_object.path = ''
    assert ApparmorFactCollector().collect(module=None, collected_facts=None) == {'apparmor':{'status':'disabled'}}

# Generated at 2022-06-13 02:20:13.189085
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    aac = ApparmorFactCollector()
    fake_module = None
    fake_collected_facts = None
    aac.collect(fake_module, fake_collected_facts)

# Generated at 2022-06-13 02:20:14.930697
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_facts = ApparmorFactCollector().collect()
    assert apparmor_facts['apparmor']['status'] == 'disabled'

# Generated at 2022-06-13 02:20:18.363208
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():

    apparmor_fact_collector = ApparmorFactCollector()
    os.environ['APPARMOR_STATUS'] = "enabled"
    assert apparmor_fact_collector.collect() == {'ansible_apparmor': {'status': 'enabled'}}
    os.environ['APPARMOR_STATUS'] = "disabled"
    assert apparmor_fact_collector.collect() == {'apparmor': {'status': 'disabled'}}

# Generated at 2022-06-13 02:20:19.702213
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    '''
    Test collect method of class ApparmorFactCollector
    '''
    test_instance = ApparmorFactCollector()
    test_instance.collect()

# Generated at 2022-06-13 02:20:24.114608
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmorFC = ApparmorFactCollector()
    facts_dict = apparmorFC.collect()
    assert isinstance(facts_dict, dict)

# Generated at 2022-06-13 02:20:28.383436
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    factCollector = ApparmorFactCollector()
    factCollector._module = Mock()
    factCollector._module.run_command.return_value = (0, 'enabled', '')
    assert factCollector.collect() == {'apparmor': {'status': 'disabled'}}

# Generated at 2022-06-13 02:20:32.710581
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    afc = ApparmorFactCollector()
    apparmor_facts = afc.collect()
    assert 'status' in apparmor_facts['apparmor']
    assert 'enabled' == apparmor_facts['apparmor']['status'] or 'disabled' == apparmor_facts['apparmor']['status']

# Generated at 2022-06-13 02:20:37.954203
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    try:
        import os
        os.stat('/sys/kernel/security/apparmor')
        apparmor_enabled = True
    except OSError:
        apparmor_enabled = False
    collected_facts = { 'apparmor': { 'status': 'disabled' } }
    fc = ApparmorFactCollector()
    result = fc.collect(collected_facts = collected_facts)
    assert result == { 'apparmor': { 'status': 'enabled' } }

# Generated at 2022-06-13 02:20:40.758324
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_facts = ApparmorFactCollector()
    assert apparmor_facts.collect() == {'apparmor': {'status': 'enabled'}}

# Generated at 2022-06-13 02:20:49.838635
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    # mock tests
    try:
        from ansible.modules.system import apparmor as apparmor_module
    except ImportError:
        module = None  # noqa
        print("module ApparmorFactCollector was not found. Skipping test for method collect.")
        return

    mock_module = apparmor_module.AnsibleModule(
        argument_spec={},
        supports_check_mode=False,
    )

    mock_module.run_command.side_effect = [
        (1, "/sys/kernel/security/apparmor", ""),
        ]
    mock_module.exit_json.side_effect = SystemExit

    # define global variables for apparmor module
    global facts, ApparmorFactCollector

    # initialize
    facts = dict()
    ApparmorFactCollector = ApparmorFactCollector()

    # collect

# Generated at 2022-06-13 02:20:54.966282
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    awf = ApparmorFactCollector()
    aaa_path = '/sys/kernel/security/apparmor'
    os.unlink(aaa_path)
    assert awf.collect()["apparmor"]["status"] == 'disabled'
    os.mkdir(aaa_path)
    assert awf.collect()["apparmor"]["status"] == 'enabled'

# Generated at 2022-06-13 02:20:58.709495
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact_collector = ApparmorFactCollector()
    assert apparmor_fact_collector.collect() == {'apparmor': {'status': 'enabled'}} or apparmor_fact_collector.collect() == {'apparmor': {'status': 'disabled'}}

# Generated at 2022-06-13 02:21:04.634039
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    """Unit test for method collect."""

    apparmorfactcollector = ApparmorFactCollector()
    facts = {}
    apparmorfactcollector.collect(collected_facts=facts)
    assert 'apparmor' in facts
    assert 'status' in facts['apparmor']
    assert facts['apparmor']['status'] in ('disabled', 'enabled')

# Generated at 2022-06-13 02:21:08.669475
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    """ Unit test for method collect of class ApparmorFactCollector """
    assert ApparmorFactCollector().fact_type is None
    assert ApparmorFactCollector().name == 'apparmor'
    assert ApparmorFactCollector().priority == 100
    assert ApparmorFactCollector()._fact_ids == set()
    assert ApparmorFactCollector().platform_facts is None
    assert ApparmorFactCollector().platform is None
    assert ApparmorFactCollector().required_legacy_facts is None
    assert ApparmorFactCollector().required_system_facts is None
    assert ApparmorFactCollector().collect() != {}
    assert ApparmorFactCollector().collect()['apparmor'] != {}

# Generated at 2022-06-13 02:21:15.982124
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    fact_test = {
        'apparmor': {'status': 'enabled'}
    }
    apparmor = ApparmorFactCollector()
    assert fact_test == apparmor.collect()

# Generated at 2022-06-13 02:21:20.793632
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact_collector = ApparmorFactCollector()
    # Testcase
    os.path.exists = lambda x: True
    facts = apparmor_fact_collector.collect(collected_facts={})
    assert facts['apparmor']['status'] == 'enabled'
    # Testcase
    os.path.exists = lambda x: False
    facts = apparmor_fact_collector.collect(collected_facts={})
    assert facts['apparmor']['status'] == 'disabled'

# Generated at 2022-06-13 02:21:23.375535
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    am = ApparmorFactCollector()
    am_facts = am.collect()
    assert am_facts['apparmor'] is not None, "Apparmor facts collection is missing"

# Generated at 2022-06-13 02:21:29.356817
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    """
    Unit test for collect method.
    """
    module = None
    collected_facts = None
    apparmor_test_obj = ApparmorFactCollector()
    data = apparmor_test_obj.collect(module, collected_facts)
    assert data['apparmor'] == {'status': 'disabled'}


# Generated at 2022-06-13 02:21:32.437458
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact_collector = ApparmorFactCollector()
    apparmor_fact_collector.collect()
    assert(apparmor_fact_collector.fact_ids() == ['apparmor'])

# Generated at 2022-06-13 02:21:40.049849
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact_collector = ApparmorFactCollector()

    # When /sys/kernel/security/apparmor exists, status is enabled
    apparmor_fact_collector._exists = lambda x: True
    result_dict = apparmor_fact_collector.collect()
    assert result_dict == {'apparmor': {'status': 'enabled'}}, \
        'status should be enabled when /sys/kernel/security/apparmor exists'

    # When /sys/kernel/security/apparmor does not exist, status is disabled
    apparmor_fact_collector._exists = lambda x: False
    result_dict = apparmor_fact_collector.collect()

# Generated at 2022-06-13 02:21:48.330781
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    # Test with AppArmor disabled
    apparmor_path = '/sys/kernel/security/apparmor'
    if os.path.exists(apparmor_path):
        os.rmdir(apparmor_path)
    apparmor_fact_collector = ApparmorFactCollector()
    facts_dict = apparmor_fact_collector.collect()
    assert facts_dict == {'apparmor': {'status': 'disabled'}}

    # Test with AppArmor enabled
    os.makedirs(apparmor_path)
    facts_dict = apparmor_fact_collector.collect()
    assert facts_dict == {'apparmor': {'status': 'enabled'}}

# Generated at 2022-06-13 02:21:49.983910
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_facts = {'apparmor': {'status': 'disabled'}}
    assert ApparmorFactCollector().collect() == apparmor_facts

# Generated at 2022-06-13 02:21:58.125975
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector.network import NetworkFactCollector
    from ansible.module_utils.facts.collector.apparmor import ApparmorFactCollector
    import os

    # Assert ApparmorFactCollector is subclass of BaseFactCollector
    assert issubclass(ApparmorFactCollector, BaseFactCollector)

    # Create an instance of ApparmorFactCollector
    apparmor_fact_collector = ApparmorFactCollector()

    # Try to collect without apparmor enabled
    backup_path = '/sys/kernel/security/apparmor'
    if os.path.exists(backup_path):
        os.unlink(backup_path)

# Generated at 2022-06-13 02:22:03.681232
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
  fact_collector = ApparmorFactCollector()

  if os.path.exists('/sys/kernel/security/apparmor'):
    expected_apparmor_facts = {'status': 'enabled'}
  else:
    expected_apparmor_facts = {'status': 'disabled'}

  expected_facts = {'apparmor': expected_apparmor_facts}

  # mock os.path.exists - this will be checked by ApparmorFactCollector
  os_mock = os.path
  os_mock.exists = lambda path: path == '/sys/kernel/security/apparmor'

  assert fact_collector.collect() == expected_facts

# Generated at 2022-06-13 02:22:21.287841
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    # Arrange
    # Create a fact collector object
    fact_collector_obj = ApparmorFactCollector()

    # Act
    # Collect the facts using above object
    fact = fact_collector_obj.collect()

    # Assert
    # Check if it is the right type
    if not isinstance(fact, dict):
        raise AssertionError('Unexpected type. Expected dict got {0}'.format(type(fact)))
    # Check if the method returns empty fact
    if fact:
        raise AssertionError('Unexpected data. Expected empty dict got {0}'.format(fact))

# Generated at 2022-06-13 02:22:22.019585
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    pass


# Generated at 2022-06-13 02:22:25.831396
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    files = {}
    files['/sys/kernel/security/apparmor'] = 'text'

    obj = ApparmorFactCollector()
    result = obj.collect(collected_facts={}, module=None)
    assert result['apparmor']['status'] == 'enabled'
    obj = ApparmorFactCollector()
    result = obj.collect(collected_facts={}, module=None, file_exists_dict=files)
    assert result['apparmor']['status'] == 'disabled'

# Generated at 2022-06-13 02:22:27.206463
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    ApparmorFactCollector_object = ApparmorFactCollector()
    assert ApparmorFactCollector_object.collect() == {'apparmor': {'status': 'disabled'}}


# Generated at 2022-06-13 02:22:28.073515
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    colec = ApparmorFactCollector()
    assert type(colec.collect()) == dict

# Generated at 2022-06-13 02:22:28.485733
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    pass

# Generated at 2022-06-13 02:22:30.063410
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    my_collector = ApparmorFactCollector()

    assert my_collector.collect() == {}

# Generated at 2022-06-13 02:22:33.231619
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    test_module = 'ansible.module_utils.'
    apparmor_collector = ApparmorFactCollector(module=test_module)
    apparmor_facts = apparmor_collector.collect()
    assert apparmor_facts['apparmor'] != None
    assert apparmor_facts['apparmor']['status'] != None

# Generated at 2022-06-13 02:22:34.767813
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    test_class = ApparmorFactCollector()
    facts_dict = test_class.collect()
    assert 'apparmor' in facts_dict

# Generated at 2022-06-13 02:22:37.809040
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    # Create an instance of the ApparmorFactCollector class
    apparmor_fact_collector_instance = ApparmorFactCollector()
    # Invoke the collect method
    apparmor_facts = apparmor_fact_collector_instance.collect()
    # Assert that the facts collected are as expected
    assert apparmor_facts['apparmor']['status'] == 'disabled'

# Generated at 2022-06-13 02:22:50.351026
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    collector = ApparmorFactCollector()
    collector.collect()
    assert isinstance(collector.collect(), dict)

# Generated at 2022-06-13 02:22:52.525512
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact_collector = ApparmorFactCollector()
    assert not apparmor_fact_collector.collect()['apparmor']['status']

# Generated at 2022-06-13 02:22:58.589349
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_collector = ApparmorFactCollector()
    if os.path.exists('/sys/kernel/security/apparmor'):
        assert apparmor_collector.collect() == {'apparmor': {'status': 'enabled'}}, \
            "test_ApparmorFactCollector_collect: collect method of class ApparmorFactCollector doesn't return \
            expected dictionary"
    else:
        assert apparmor_collector.collect() == {'apparmor': {'status': 'disabled'}}, \
            "test_ApparmorFactCollector_collect: collect method of class ApparmorFactCollector doesn't return \
            expected dictionary"

# Generated at 2022-06-13 02:23:08.105348
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    """
    Test collect() by mocking open() to read in a file.
    """
    import mock
    import __builtin__
    # mock open() of file /sys/kernel/security/apparmor to read in a file
    mock_open = mock.mock_open(read_data="some data")
    mock_cache_dir = 'some/dir'

# Generated at 2022-06-13 02:23:09.699509
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    assert ApparmorFactCollector().collect() == {'apparmor': {'status': 'disabled'}}

# Generated at 2022-06-13 02:23:12.049382
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    module = None
    collected_facts = None
    apparmor_collector = ApparmorFactCollector(module, collected_facts)
    assert apparmor_collector.collect() == { 'apparmor': {'status': 'disabled'} }

# Generated at 2022-06-13 02:23:15.675451
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    collector = ApparmorFactCollector()
    facts = collector.collect({}, {})
    assert 'apparmor' in facts

# Generated at 2022-06-13 02:23:21.166383
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():

    # Create a fake module object for test
    module = object()
    # Create an instance of ApparmorFactCollector and call method collect
    apparmor_fact_collector = ApparmorFactCollector()
    facts_dict = apparmor_fact_collector.collect(module)
    # Verify return value
    assert sorted(facts_dict.keys()) == ['apparmor']
    assert sorted(facts_dict['apparmor'].keys()) == ['status']

# Generated at 2022-06-13 02:23:23.631838
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact_collector = ApparmorFactCollector()
    assert(apparmor_fact_collector.collect() ==
            {'apparmor': {'status': 'disabled'}})

# Generated at 2022-06-13 02:23:27.948396
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    # Create a new object of class ApparmorFactCollector
    apparmor = ApparmorFactCollector()
    # Acquire collect() method of the object
    c = apparmor.collect()
    # Verify if the collect() method returns the expected type
    assert isinstance(c, dict)

# Generated at 2022-06-13 02:23:54.337379
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact_collector = ApparmorFactCollector()

    apparmor_facts = apparmor_fact_collector.collect()['apparmor']

    assert apparmor_facts['status'] == 'disabled'

# Generated at 2022-06-13 02:23:57.524827
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact_collector = ApparmorFactCollector()
    assert 'apparmor' == apparmor_fact_collector.name
    facts_dict = apparmor_fact_collector.collect()
    assert 'apparmor' in facts_dict

# Generated at 2022-06-13 02:24:03.838637
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_enabled_facts = {'apparmor': {'status': 'enabled'}}
    apparmor_disabled_facts = {'apparmor': {'status': 'disabled'}}

    # Enable Apparmor for testing
    apparmor_enabled = os.system('apparmor_status > /dev/null 2>&1')
    if apparmor_enabled != 0:
        os.system('service apparmor start')
    collector = ApparmorFactCollector()
    assert collector.collect() == apparmor_enabled_facts
    # Disable Apparmor for testing
    if apparmor_enabled != 0:
        os.system('service apparmor stop')
    collector = ApparmorFactCollector()
    assert collector.collect() == apparmor_disabled_facts

# Generated at 2022-06-13 02:24:08.639966
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact = ApparmorFactCollector()
    os.path.exists = lambda x: True
    apparmor_fact.collect()
    assert 'apparmor' in apparmor_fact.collect()
    assert 'status' in apparmor_fact.collect().get('apparmor')
    assert apparmor_fact.collect().get('apparmor').get('status') == 'enabled'

# Generated at 2022-06-13 02:24:12.643203
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    # create an object of class ApparmorFactCollector
    facts_object = ApparmorFactCollector()
    # create facts dictionary related to apparmor
    apparmor_facts_dict = facts_object.collect()
    # assert that the key apparmor on the dictionary is not empty
    assert 'apparmor' in apparmor_facts_dict
    # assert that the key apparmor on the dictionary is not None
    assert apparmor_facts_dict['apparmor'] is not None

# Generated at 2022-06-13 02:24:17.905800
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    aa = ApparmorFactCollector()
    ret = aa.collect()
    if os.path.exists('/sys/kernel/security/apparmor'):
        assert ret['apparmor']['status'] == 'enabled'
    else:
        assert ret['apparmor']['status'] == 'disabled'

# Generated at 2022-06-13 02:24:19.240433
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    obj = ApparmorFactCollector()
    obj.collect()

# Generated at 2022-06-13 02:24:21.221086
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmorTest = ApparmorFactCollector()
    apparmorTest._module = object()
    apparmorTest.collect()

# Generated at 2022-06-13 02:24:23.270822
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    """Test ApparmorFactCollector.collect()"""
    apparmor_collector = ApparmorFactCollector()
    apparmor_fact = apparmor_collector.collect()
    assert apparmor_fact is not None

# Generated at 2022-06-13 02:24:30.367045
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_collector = ApparmorFactCollector()
    ansible_facts = {}
    collected_facts = apparmor_collector.collect(None, ansible_facts)
    assert collected_facts['apparmor']

    # if /sys/kernel/security/apparmor is not available,
    # status should be disabled
    if os.path.exists('/sys/kernel/security/apparmor'):
        assert collected_facts['apparmor']['status'] == 'enabled'
    else:
        assert collected_facts['apparmor']['status'] == 'disabled'

# Generated at 2022-06-13 02:25:24.405201
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_collector = ApparmorFactCollector()
    apparmor_facts = apparmor_collector.collect()
    assert apparmor_facts['apparmor']['status'] in ['enabled', 'disabled']

# Generated at 2022-06-13 02:25:29.398859
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    from ansible.module_utils.facts.collector.apparmor import ApparmorFactCollector
    fact_collector = ApparmorFactCollector()
    if os.path.exists('/sys/kernel/security/apparmor'):
        assert {'apparmor':{'status':'enabled'}} == fact_collector.collect()
    else:
        assert {'apparmor':{'status':'disabled'}} == fact_collector.collect()

# Generated at 2022-06-13 02:25:34.904995
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    fact_collector = ApparmorFactCollector()
    facts = fact_collector.collect(module=None, collected_fact=None)
    assert facts['apparmor']['status'] == 'disabled'
    # Unit test for method get_fact_ids of class ApparmorFactCollector
    fact_collector = ApparmorFactCollector()
    fact_ids = fact_collector.get_fact_ids()
    assert fact_ids == set(['apparmor_status'])
    # Unit test for method get_fact_name of class ApparmorFactCollector
    fact_collector = ApparmorFactCollector()
    fact_ids = fact_collector.get_fact_name('apparmor_dummy')
    assert fact_ids == None

# Generated at 2022-06-13 02:25:35.470190
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    pass

# Generated at 2022-06-13 02:25:43.360351
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    fact_collector = ApparmorFactCollector()

    # status is enabled when /sys/kernel/security/apparmor exists and is
    # a directory.
    apparmor = {'status': 'enabled'}
    if os.path.isdir('/sys/kernel/security/apparmor'):
        collected_facts = fact_collector.collect()
        assert collected_facts['apparmor'] == apparmor
    else:
        apparmor['status'] = 'disabled'
        collected_facts = fact_collector.collect()
        assert collected_facts['apparmor'] == apparmor

# Generated at 2022-06-13 02:25:45.570278
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    fact_class = ApparmorFactCollector()
    fact_class.collect()
    fact_class._fact_ids
    assert(fact_class.name == 'apparmor')

# Generated at 2022-06-13 02:25:47.935881
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    ApparmorFactCollector._fact_ids = set()
    module = None
    facts_dict = ApparmorFactCollector().collect(module)
    assert facts_dict['apparmor']['status'] == 'enabled'

# Generated at 2022-06-13 02:25:48.455151
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    assert True

# Generated at 2022-06-13 02:25:50.508042
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact_collector = ApparmorFactCollector()
    assert apparmor_fact_collector.collect() == {'apparmor': {'status': 'disabled'}}

# Generated at 2022-06-13 02:25:52.575050
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    """
    Test collect method of class ApparmorFactCollector
    """
    test_obj = ApparmorFactCollector()
    result = test_obj.collect()
    assert result == 'Test-data'

# Generated at 2022-06-13 02:27:47.014676
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact = ApparmorFactCollector()
    apparmor_facts = apparmor_fact.collect()
    assert 'apparmor' in apparmor_facts

# Generated at 2022-06-13 02:27:52.086363
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact_collector = ApparmorFactCollector(None)

    with open('/sys/kernel/security/apparmor', 'w') as apparmor_file:
        apparmor_file.write('')
    assert apparmor_fact_collector.collect() == {
        'apparmor': {
            'status': 'enabled'
        }
    }
    os.remove('/sys/kernel/security/apparmor')

    assert apparmor_fact_collector.collect() == {
        'apparmor': {
            'status': 'disabled'
        }
    }

# Generated at 2022-06-13 02:28:00.430937
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    # Arrange
    # By faking the existence of /sys/kernel/security/apparmor
    # we mock a system that has apparmor enabled.
    exists_mock = mock.MagicMock(return_value=True)
    exists_mock.return_value = True
    with mock.patch.object(os.path, 'exists', exists_mock):
        # Act
        apparmor_collector = ApparmorFactCollector()
        apparmor_facts = apparmor_collector.collect()
        # Assert
        assert apparmor_facts['apparmor'] == {'status': 'enabled'}

# Generated at 2022-06-13 02:28:02.071941
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_collector = ApparmorFactCollector()
    apparmor_collector.collect()

# Generated at 2022-06-13 02:28:03.796990
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    app_apparmor = ApparmorFactCollector()
    result = app_apparmor.collect()
    assert ('apparmor' in result)

# Generated at 2022-06-13 02:28:05.972908
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    assert ApparmorFactCollector().collect() == {'apparmor': {'status': 'enabled'}}

# Generated at 2022-06-13 02:28:07.879400
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_facts = ApparmorFactCollector.collect()

    assert apparmor_facts['apparmor']['status'] == 'enabled'


# Generated at 2022-06-13 02:28:10.618968
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    fact_collector = ApparmorFactCollector()

    facts_dict = fact_collector.collect(None, None)
    assert type(facts_dict['apparmor']) is dict
    assert 'apparmor' in facts_dict
    assert 'status' in facts_dict['apparmor']

# Generated at 2022-06-13 02:28:17.368414
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact_collector = ApparmorFactCollector()
    assert isinstance(apparmor_fact_collector, ApparmorFactCollector)
    assert apparmor_fact_collector.name == 'apparmor'
    assert apparmor_fact_collector._fact_ids == set()
    assert isinstance(apparmor_fact_collector.collect(module=None, collected_facts={}), dict) == True

# Generated at 2022-06-13 02:28:19.406794
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    fixture = ApparmorFactCollector()
    assert fixture.collect() == {
        'apparmor': {
            'status': 'disabled'
        }
    }