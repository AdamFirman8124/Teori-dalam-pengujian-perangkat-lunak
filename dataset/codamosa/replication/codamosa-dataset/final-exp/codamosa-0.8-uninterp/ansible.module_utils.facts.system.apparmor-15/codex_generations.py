

# Generated at 2022-06-13 02:19:54.762359
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    assert not os.path.exists('/sys/kernel/security/apparmor'), "The apparmor is enabled in the test system"
    fact_collector = ApparmorFactCollector(None)
    assert fact_collector.collect() is not None, "The result of the apparmor fact collector is none"
    assert 'apparmor' in fact_collector.collect(), "The result of the apparmor fact collector doesn't contain any apparmor fact"
    assert 'status' in fact_collector.collect()['apparmor'], "The result of the apparmor fact collector doesn't contain any apparmor fact"
    assert 'disabled' == fact_collector.collect()['apparmor']['status'], "The result of the apparmor fact collector doesn't contain the correct apparmor fact"

# Generated at 2022-06-13 02:19:56.862650
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact = ApparmorFactCollector()
    facts = apparmor_fact.collect()
    assert 'apparmor' in facts


# Generated at 2022-06-13 02:19:59.571447
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    x = ApparmorFactCollector()
    collected_facts = {}
    aa_facts = x.collect(collected_facts)
    assert aa_facts['apparmor']['status'] in ['enabled', 'disabled']

# Generated at 2022-06-13 02:20:02.679077
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    # Create an instance
    apparmor_collector = ApparmorFactCollector()
    apparmor_collector.collect()
    # Verify the results
    assert isinstance(apparmor_collector.collect(), dict)

# Generated at 2022-06-13 02:20:05.539581
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_collector = ApparmorFactCollector()
    result = apparmor_collector.collect()
    assert result.get("apparmor")

# Generated at 2022-06-13 02:20:12.889811
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils.facts.collector import get_collector_names

    # Create a temporary directory to store facts files
    import tempfile
    tempdir = tempfile.mkdtemp()
    os.mkdir(os.path.join(tempdir, 'ansible_local'))

    # Create a dummy 'apparmor' file to simulate that apparmor is enabled
    apparmor_status_file = os.path.join(tempdir, 'ansible_local', 'apparmor')
    with open(apparmor_status_file, 'w') as af:
        af.write('enabled')

    # Set ansible_local as fact_path
    FactCollector.root_

# Generated at 2022-06-13 02:20:13.257666
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fa

# Generated at 2022-06-13 02:20:14.692587
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_collector = ApparmorFactCollector()
    assert apparmor_collector.collect()['apparmor']['status'] is not None

# Generated at 2022-06-13 02:20:15.846192
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_collector = ApparmorFactCollector
    collected_facts = apparmor_collector.collect(None, None)
    expected_facts = {'apparmor': {'status': 'disabled'}}
    assert collected_facts == expected_facts

# Generated at 2022-06-13 02:20:18.613392
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    import json
    apparmor_fact_collector = ApparmorFactCollector()
    facts = apparmor_fact_collector.collect()

    expected = {'apparmor': {'status': 'enabled'}}
    assert facts == expected

# Generated at 2022-06-13 02:20:25.891581
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    assert ApparmorFactCollector.name == 'apparmor'
    apparmor_fact_collector = ApparmorFactCollector()
    # In case if apparmor not installed apparmor_facts['status'] should be equal to 'disabled'
    assert apparmor_fact_collector.collect()['apparmor']['status'] == 'disabled'

# Generated at 2022-06-13 02:20:34.659546
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact = ApparmorFactCollector()
    # Check status is enabled
    os.path.exists = lambda path: True
    apparmor_facts_dict_enabled = {'apparmor': {'status': 'enabled'}}
    assert apparmor_fact.collect() == apparmor_facts_dict_enabled
    # Check status is disabled
    os.path.exists = lambda path: False
    apparmor_facts_dict_disabled = {'apparmor': {'status': 'disabled'}}
    assert apparmor_fact.collect() == apparmor_facts_dict_disabled

# Generated at 2022-06-13 02:20:36.405560
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    module = AnsibleModule(argument_spec={})
    fc = ApparmorFactCollector()
    fc.collect(module)

# Generated at 2022-06-13 02:20:40.328428
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    fact_collector = ApparmorFactCollector()
    assert issubclass(fact_collector.__class__, BaseFactCollector)
    assert isinstance(fact_collector, BaseFactCollector)

# Generated at 2022-06-13 02:20:48.160823
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact_collector = ApparmorFactCollector()
    apparmor_facts_dict = apparmor_fact_collector.collect()
    # Verify collect method returns a dictionary
    assert type(apparmor_facts_dict) == dict
    # Verify collect method returns expected keys
    expected_keys = ['apparmor']
    assert set(apparmor_facts_dict.keys()) == set(expected_keys)
    # Verify all keys in 'apparmor' dictionary have expected values
    expected_values = ['enabled', 'disabled']
    assert set(apparmor_facts_dict['apparmor']['status'] in expected_values)

# Generated at 2022-06-13 02:20:52.763303
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    fact_collector = ApparmorFactCollector()
    collected_facts = fact_collector.collect()
    apparmor_facts = collected_facts["apparmor"]
    assert apparmor_facts["status"] == "enabled"

# Generated at 2022-06-13 02:21:03.648899
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    import os
    import tempfile
    import shutil
    import pytest
    from mock import Mock, patch

    class Args(object):
        def __init__(self):
            self.gather_subset = ['all']
            self.gather_timeout = 10

    module = Mock()
    module.params = Args()
    collected_facts = {}
    tmpdir = tempfile.mkdtemp()

    # Create fake /sys/kernel/security/apparmor
    os.makedirs(os.path.join(tmpdir, 'sys/kernel/security'))
    os.makedirs(os.path.join(tmpdir, 'sys/kernel/security/apparmor'))

    # Fake /sys/kernel/security/apparmor exist
    module.get_bin_path.return_value = tmpdir
   

# Generated at 2022-06-13 02:21:07.447809
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    # Unit tests for collect method
    apparmor_obj = ApparmorFactCollector()

    test_apparmor_status_dict = {'apparmor': {'status': 'enabled'}}
    assert apparmor_obj.collect() == test_apparmor_status_dict


# Generated at 2022-06-13 02:21:09.151826
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    collector = ApparmorFactCollector()
    result = collector.collect()
    assert result
    assert 'apparmor' in result

# Generated at 2022-06-13 02:21:13.966686
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    # Create instance of class FileSystemFactCollector
    apparmor_fact_collector_obj = ApparmorFactCollector()

    # Call method collect of class FileSystemFactCollector
    apparmor_facts = apparmor_fact_collector_obj.collect()

    assert isinstance(apparmor_facts, dict)

# Generated at 2022-06-13 02:21:25.869587
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor = ApparmorFactCollector()
    facts = apparmor.collect()
    assert type(facts) is dict
    assert type(facts['apparmor']) is dict
    if os.path.exists('/sys/kernel/security/apparmor'):
        assert facts['apparmor']['status'] == 'enabled'
    else:
        assert facts['apparmor']['status'] == 'disabled'

# Generated at 2022-06-13 02:21:29.160638
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_facts = ApparmorFactCollector().collect()
    assert apparmor_facts['apparmor']['status'] in ['disabled', 'enabled']

# Generated at 2022-06-13 02:21:34.047044
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    # fake the filesystem to return something we can test against
    class fakefs(dict):
        def __init__(self):
            pass

        def get(self, key, default=None):
            if key == '/sys/kernel/security/apparmor':
                return True
            return default

        def __contains__(self, key):
            if key == '/sys/kernel/security/apparmor':
                return True
            return False
    fakeos = fakefs()

    apparmor_fact_collector = ApparmorFactCollector(fakeos)
    result = apparmor_fact_collector.collect()

    assert result['apparmor']['status'] == 'enabled'

# Generated at 2022-06-13 02:21:39.800083
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():

    # import and instantiate the class to tested
    from ansible.module_utils.facts.system.apparmor import ApparmorFactCollector
    apparmorfc = ApparmorFactCollector()

    # create a mock module to use in calling the collect method
    class MockModule(object):
        def __init__(self, params):
            self.params = params

    # the test facts to use
    test_facts = {
        'apparmor': {
            'status': 'enabled'
        }
    }

    # test the method using the actual return value
    assert test_facts == apparmorfc.collect(MockModule(params={}))

# Generated at 2022-06-13 02:21:43.907882
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor = ApparmorFactCollector()

    # mock
    apparmor._read_file_on_disk = True

    # test
    results = apparmor.collect()

    # assert
    assert results['apparmor']['status'] == 'enabled'

# Generated at 2022-06-13 02:21:48.453697
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():

    class Module(object):
        def __init__(self, file_exists_list):
            self.file_exists_list = file_exists_list
            self.index = 0

        def get_bin_path(self, executable, required=False, opt_dirs=[]):
            return

        def file_exists(self, path):
            return self.file_exists_list[self.index]

    module = Module([False, True])

    apparmor_fact_collector = ApparmorFactCollector()
    result = apparmor_fact_collector.collect(module)

    assert result['apparmor']['status'] == 'disabled'

    module.index = 1
    result = apparmor_fact_collector.collect(module)

    assert result['apparmor']['status'] == 'enabled'

# Generated at 2022-06-13 02:21:51.197136
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact = ApparmorFactCollector()
    module = {}
    collected_facts = {}
    apparmor_facts = apparmor_fact.collect(module, collected_facts)
    assert apparmor_facts['apparmor']['status'] == 'disabled'

# Generated at 2022-06-13 02:21:53.028867
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_collector = ApparmorFactCollector()
    result = apparmor_collector.collect()
    assert 'apparmor' in result

# Generated at 2022-06-13 02:21:57.826439
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    mock_collector = ApparmorFactCollector()
    mock_collector._module = None
    mock_collector._collected_facts = {}
    mock_facts = mock_collector.collect()
    if os.path.exists('/sys/kernel/security/apparmor'):
        assert mock_facts['apparmor']['status'] == 'enabled'
    else:
        assert mock_facts['apparmor']['status'] == 'disabled'

# Generated at 2022-06-13 02:22:00.507069
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    factCollector = ApparmorFactCollector()
    assert factCollector.collect()['apparmor']['status'] == 'disabled'
    assert factCollector.collect()['apparmor'] != {}

# Generated at 2022-06-13 02:22:14.168303
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_facts_collector = ApparmorFactCollector()
    assert apparmor_facts_collector.collect() == {'apparmor': {'status': 'enabled'}}


# Generated at 2022-06-13 02:22:19.622759
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    fact_collector = ApparmorFactCollector()
    facts = fact_collector.collect()
    assert isinstance(facts, dict)
    assert 'apparmor' in facts
    assert isinstance(facts['apparmor'], dict)
    assert 'status' in facts['apparmor']
    assert isinstance(facts['apparmor']['status'], str)

# Generated at 2022-06-13 02:22:22.251459
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    collector = ApparmorFactCollector()
    facts = collector.collect()
    assert facts['apparmor']['status'] == 'enabled' or facts['apparmor']['status'] == 'disabled'

# Generated at 2022-06-13 02:22:24.101104
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    fact_collector = ApparmorFactCollector()
    facts = fact_collector.collect()
    assert type(facts['apparmor']) is dict
    assert len(facts['apparmor']) > 0

# Generated at 2022-06-13 02:22:26.511899
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fc = ApparmorFactCollector()
    facts_dict = apparmor_fc.collect()

    # Assert that the object is ApparmorFactCollector
    assert isinstance(apparmor_fc, ApparmorFactCollector)

    # Assert that the return value is expected
    assert facts_dict == {'apparmor': {'status': 'disabled'}}

# Generated at 2022-06-13 02:22:27.965325
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    collector = ApparmorFactCollector()
    res = collector.collect()
    assert isinstance(res, dict)

# Generated at 2022-06-13 02:22:29.667001
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    collector = ApparmorFactCollector()
    facts = collector.collect()
    assert 'apparmor' in facts
    assert isinstance(facts['apparmor'], dict)
    assert 'status' in facts['apparmor']
    assert isinstance(facts['apparmor']['status'], str)

# Generated at 2022-06-13 02:22:31.686548
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    # Initialize class
    apparmor_collector = ApparmorFactCollector()

    # Check return data
    assert isinstance(apparmor_collector.collect(), dict)

# Generated at 2022-06-13 02:22:33.330838
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    collector = ApparmorFactCollector()
    facts = collector.collect()
    assert facts['apparmor']['status'] == 'enabled'

# Generated at 2022-06-13 02:22:35.134949
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    fact_collector = ApparmorFactCollector()
    facts_dict = fact_collector.collect()
    assert facts_dict['apparmor']['status'] is not None

# Generated at 2022-06-13 02:23:02.455520
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact = ApparmorFactCollector()
    os.path.exists = lambda x: True
    result = apparmor_fact.collect()
    assert result == {'apparmor': {'status': 'enabled'}}
    os.path.exists = lambda x: False
    result = apparmor_fact.collect()
    assert result == {'apparmor': {'status': 'disabled'}}

# Generated at 2022-06-13 02:23:11.251190
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    os_system = 'Linux'
    os_release = '4.4.0-135-generic'
    os_distribution = 'Ubuntu'
    os_version = '16.04'
    os_subversion = 'LTS'

# Generated at 2022-06-13 02:23:22.293095
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    """
    Test if the method collect of class ApparmorFactCollector
    returns a dictionary with the right content.
    """
    # Create object ApparmorFactCollector
    apparmor_collector = ApparmorFactCollector()

    # Remove file /sys/kernel/security/apparmor if it exists,
    # and create it if it doesn't exist
    if os.path.exists('/sys/kernel/security/apparmor'):
        os.remove('/sys/kernel/security/apparmor')
    else:
        os.mkdir('/sys/kernel/security/apparmor')

    # Get the facts from the method collect of class ApparmorFactCollector
    apparmor_facts_disabled = apparmor_collector.collect(collected_facts={})

    # Remove file /sys/kernel/security/apparmor if it exists
   

# Generated at 2022-06-13 02:23:28.727096
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    ansible_module = None
    ansible_facts = None
    aafc = ApparmorFactCollector()
    apparmor_facts = aafc.collect(ansible_module, ansible_facts)
    assert isinstance(apparmor_facts, dict)
    assert 'apparmor' in apparmor_facts
    assert 'status' in apparmor_facts['apparmor']
    assert apparmor_facts['apparmor']['status'] in ['disabled', 'enabled']

# Generated at 2022-06-13 02:23:30.747021
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    ApparmorFactCollector1 = ApparmorFactCollector()
    ApparmorFactCollector1.collect()
    #assert(True)

# Generated at 2022-06-13 02:23:33.359306
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    afc = ApparmorFactCollector()
    assert afc.collect() == {'apparmor': {'status': 'disabled'}}

# Generated at 2022-06-13 02:23:36.253886
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    fact_collector = ApparmorFactCollector()
    _facts = fact_collector.collect(None, None)
    _expected_facts = {'apparmor': {'status': 'disabled'}}
    assert _facts == _expected_facts

# Generated at 2022-06-13 02:23:37.554610
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_obj = ApparmorFactCollector()

    print(apparmor_obj.collect())

# Generated at 2022-06-13 02:23:38.917920
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    ans_module = None
    ans_facts = None
    ans = ApparmorFactCollector()
    ans.collect(ans_module, ans_facts)

# Generated at 2022-06-13 02:23:43.936953
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    """Unit test for method collect of class ApparmorFactCollector."""
    # backup sys.modules
    saved_sys_modules = sys.modules.copy()
    # set sys.modules to fake it
    sys.modules = {
        'ansible.module_utils.facts.collector.base': mock.MagicMock(),
        'os': mock.MagicMock(),
    }
    # create the object
    apparmor_collector = ApparmorFactCollector()

    # testing when file /sys/kernel/security/apparmor is not found
    with mock.patch('os.path.exists') as mock_exists:
        mock_exists.return_value = False
        facts_dict = apparmor_collector.collect()

        assert facts_dict['apparmor']['status'] == 'disabled'

    # testing when file

# Generated at 2022-06-13 02:24:36.048855
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    # Unit tests requires the following globals
    #  - module : AnsibleModule type
    #  - ansible_facts : dictionary
    module = None
    ansible_facts = dict()

    collector = ApparmorFactCollector()

    # Call the collector
    collector.collect(module=module, collected_facts=ansible_facts)

    # Check the apparmor facts
    if 'apparmor' in ansible_facts:
        apparmor_facts = ansible_facts['apparmor']
        if 'status' in apparmor_facts:
            assert apparmor_facts['status'] == 'disabled' or apparmor_facts['status'] == 'enabled'

# Generated at 2022-06-13 02:24:39.834032
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact_collector = ApparmorFactCollector()
    result = apparmor_fact_collector.collect()
    assert 'apparmor' in result
    assert 'status' in result['apparmor']
    assert result['apparmor']['status'] in ['enabled', 'disabled']

# Generated at 2022-06-13 02:24:42.041278
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    assert ApparmorFactCollector().collect() == {'apparmor': {'status': 'disabled'}}

# Generated at 2022-06-13 02:24:44.642197
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    # Create instance of class ApparmorFactCollector
    apparmor_collector = ApparmorFactCollector()

    # Test method collect of class ApparmorFactCollector
    apparmor_collector.collect()

# Generated at 2022-06-13 02:24:50.728379
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    ApparmorFactCollector_obj = ApparmorFactCollector()

    apparmor_facts = {'status': 'enabled'}

    returned_facts_dict = ApparmorFactCollector_obj.collect(module=None, collected_facts=None)
    # Test returns correct keys
    assert set(returned_facts_dict.keys()) == set(['apparmor'])
    # Test returns apparmor facts
    assert set(returned_facts_dict['apparmor'].keys()) == set(apparmor_facts.keys())

# Generated at 2022-06-13 02:24:53.393112
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor = ApparmorFactCollector()
    apparmor._module = {}
    apparmor.collect()
    assert isinstance(apparmor.collect(), dict) and apparmor.collect() != {}
    apparmor._module = {'check_mode': True}
    apparmor.collect()
    assert isinstance(apparmor.collect(), dict) and apparmor.collect() == {}




# Generated at 2022-06-13 02:24:55.173786
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact_collector = ApparmorFactCollector()
    apparmor_fact_collector.collect()
    apparmor_facts = apparmor_fact_collector.collect()
    assert apparmor_facts['apparmor']['status'] == 'enabled'

# Generated at 2022-06-13 02:25:03.831210
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    _ApparmorFactCollector = ApparmorFactCollector()
    # Create a mock for os.path.exists
    _os_path_exists = os.path.exists
    os.path.exists = lambda x: True
    assert _ApparmorFactCollector.collect() == {'apparmor': {'status': 'enabled'}}
    os.path.exists = lambda x: False
    assert _ApparmorFactCollector.collect() == {'apparmor': {'status': 'disabled'}}
    # Restore the original path.exists
    os.path.exists = _os_path_exists

# Generated at 2022-06-13 02:25:07.115605
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmorFactCollector = ApparmorFactCollector()
    apparmor_dict = apparmorFactCollector.collect()
    assert sorted(apparmor_dict.keys()) == ['apparmor']
    assert sorted(apparmor_dict['apparmor'].keys()) == ['status']

# Generated at 2022-06-13 02:25:10.513244
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    def mock_os_path_exists(path):
        return True

    ApparmorFactCollector.__bases__[0].os.path.exists = mock_os_path_exists
    apparmor_fc = ApparmorFactCollector()
    apparmor_facts = apparmor_fc.collect()
    assert apparmor_facts['apparmor']['status'] == 'enabled'

# Generated at 2022-06-13 02:27:00.039341
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    fact = ApparmorFactCollector()
    assert fact.collect() == {'apparmor': {'status': 'disabled'}}

# Generated at 2022-06-13 02:27:01.810721
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    results = ApparmorFactCollector().collect()
    assert "apparmor" in results
    assert "status" in results['apparmor']

# Generated at 2022-06-13 02:27:05.883298
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_facts_collector = ApparmorFactCollector()
    facts = apparmor_facts_collector.collect()
    assert 'apparmor' in facts
    assert 'status' in facts['apparmor']

# Generated at 2022-06-13 02:27:10.486812
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    test_object = ApparmorFactCollector()
    apparmor_facts = test_object.collect()
    apparmor_status = apparmor_facts['apparmor']['status']

    if os.path.exists('/sys/kernel/security/apparmor'):
        assert apparmor_status == 'enabled'
    else:
        assert apparmor_status == 'disabled'

# Generated at 2022-06-13 02:27:13.296712
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    aafc = ApparmorFactCollector()
    result = aafc.collect()
    assert result['apparmor']['status'] == 'disabled' or result['apparmor']['status'] == 'enabled'

# Generated at 2022-06-13 02:27:15.460539
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    fc = ApparmorFactCollector()
    fc.collect(module=None, collected_facts=None)


# Generated at 2022-06-13 02:27:18.330422
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    ApparmorFactCollector_obj = ApparmorFactCollector()
    assert(isinstance(ApparmorFactCollector_obj.collect(), dict))

# Generated at 2022-06-13 02:27:23.334109
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    class MockModule(object):
        def __init__(self):
            self.params = {}

    class MockCollectedFacts(object):
        def __init__(self):
            self.facts = {}

    module = MockModule()
    collected_facts = MockCollectedFacts()

    apparmor_fc = ApparmorFactCollector()
    apparmor_fc.collect(module, collected_facts)

    assert 'apparmor' in collected_facts.facts

# Generated at 2022-06-13 02:27:29.298548
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    # This test makes sure that collect method of class ApparmorFactCollector
    # works with both enabled and disabled apparmor, and apparmor is being
    # picked up as a fact.
    import mock
    from ansible.module_utils.facts.collector import FactsCollector
    from ansible.module_utils import basic
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.collector import get_collector_instance
    collected_facts = FactsCollector()
    class MockFactsCollector(FactsCollector):
        def __init__(instance):
            instance._collectors = []
            instance._collected_facts = {'all': {}}
    mock_collector = MockFactsCollector()
    mock_collector.collect_apparmor_facts = ApparmorFactCollector.collect

# Generated at 2022-06-13 02:27:31.765957
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    collector = ApparmorFactCollector()
    collected_facts = {}
    result = collector.collect(collected_facts)
    assert result['ansible_local']['apparmor']['status'] == 'disabled'