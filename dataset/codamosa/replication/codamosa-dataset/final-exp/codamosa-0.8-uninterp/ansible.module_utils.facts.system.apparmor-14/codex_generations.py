

# Generated at 2022-06-13 02:19:43.765891
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    ac = ApparmorFactCollector()
    ac.collect()

# Generated at 2022-06-13 02:19:45.622921
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    """
    Tests for status of apparmor.
    Returns dict like:
        {'apparmor': {'status': 'enabled'}}
    """
    a = ApparmorFactCollector()
    assert a.collect()

# Generated at 2022-06-13 02:19:49.894730
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_collector = ApparmorFactCollector()
    # Expecting fact dict with key 'apparmor'
    assert 'apparmor' in apparmor_collector.collect()

# Generated at 2022-06-13 02:19:54.762275
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmorFact = ApparmorFactCollector()
    res = apparmorFact.collect()
    assert res is not None
    assert res['apparmor'] is not None
    if os.path.exists('/sys/kernel/security/apparmor'):
        assert res['apparmor']['status'] == 'enabled'
    else:
        assert res['apparmor']['status'] == 'disabled'

# Generated at 2022-06-13 02:20:00.456808
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():

    from ansible.module_utils.facts.collector import FactCollector

    ansible_class = module_args = dict()
    apparmor_collector = ApparmorFactCollector(ansible_class,module_args)
    facts_dict = dict()
    collected_facts = dict()
    facts_dict = apparmor_collector.collect(collected_facts)

    assert facts_dict['apparmor']['status'] == 'enabled'

# Generated at 2022-06-13 02:20:05.157189
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    collector = ApparmorFactCollector()
    # create a mock module object for the collect() method to use
    class MockModule(object):
        def __init__(self):
            self.module_name = 'mock_module'
    module = MockModule()
    assert collector.collect(module)

# Generated at 2022-06-13 02:20:09.259020
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    """Test method collect of class ApparmorFactCollector."""
    # Instantiate ApparmorFactCollector without any params
    apparmor_facts = ApparmorFactCollector()
    # Collect apparmor facts
    facts_dict = apparmor_facts.collect()

    # Assert if method collect the apparmor facts
    assert facts_dict == {'apparmor': {'status': 'disabled'}}

# Generated at 2022-06-13 02:20:18.794621
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    import os

    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector import BaseFileEntropyCollector
    from ansible.module_utils.facts.collector import BaseHardwareCollector
    from ansible.module_utils.facts.collector import BaseNetworkCollector
    from ansible.module_utils.facts.collector import BasePlatformFactCollector
    from ansible.module_utils.facts.collector import BaseSysctlCollector
    from ansible.module_utils.facts.collector import BaseVirtualCollector
    from ansible.module_utils.facts.collector import Cache
    from ansible.module_utils.facts.collector import NetworkCollector
    from ansible.module_utils.facts.collector import VirtualCollector

    FileEntropyCollector

# Generated at 2022-06-13 02:20:21.688250
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    
    apparmor_facts_collector = ApparmorFactCollector()
    facts = apparmor_facts_collector.collect()
    assert (facts['apparmor']['status'] == 'enabled') or (facts['apparmor']['status'] == 'disabled')

# Generated at 2022-06-13 02:20:32.182028
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    # initializing instance of class ApparmorFactCollector
    fact_collector = ApparmorFactCollector()
    # initializing os.path.exists to return true
    os.path.exists = MagicMock(return_value=True)
    # calling method collect
    fact_dict = fact_collector.collect()
    # check if fact_dict is non empty
    assert fact_dict
    # check apparmor Status
    assert 'enabled' == fact_dict['apparmor']['status']

    # initializing os.path.exists to return False
    os.path.exists = MagicMock(return_value=False)
    # calling method collect
    fact_dict = fact_collector.collect()
    # check if fact_dict is non empty
    assert fact_dict
    # check apparmor Status

# Generated at 2022-06-13 02:20:36.070935
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmorFactCollector = ApparmorFactCollector()
    assert apparmorFactCollecto

# Generated at 2022-06-13 02:20:41.528925
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    """
    Test method collect returns correct data structure
    """
    module = object()
    collected_facts = object()
    apparmor_fact_collector = ApparmorFactCollector(module, collected_facts)
    assert apparmor_fact_collector.collect() == {'apparmor': {'status': 'disabled'}}


# Generated at 2022-06-13 02:20:43.331273
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    collector = ApparmorFactCollector()
    facts_dict = collector.collect()


# Generated at 2022-06-13 02:20:47.819536
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    """Test if collect method returns correct dictionary"""
    import os
    import tempfile
    import shutil

    def create_temp_dir(tmp_dir):
        """Create temporary directory tree with apparmor directory"""
        if not os.path.exists(tmp_dir):
            os.makedirs(tmp_dir)
        apparmor_path = os.path.join(tmp_dir, 'sys/kernel/security/apparmor')
        if not os.path.exists(apparmor_path):
            os.makedirs(apparmor_path)
        return tmp_dir

    import pytest

    test_dir = tempfile.mkdtemp()

# Generated at 2022-06-13 02:20:48.291574
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    pass

# Generated at 2022-06-13 02:20:51.812175
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    fact_collector = ApparmorFactCollector()
    facts = fact_collector.collect()
    assert 'apparmor' in facts

# Generated at 2022-06-13 02:20:57.294611
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    fact_collector = ApparmorFactCollector()
    facts = dict()
    facts = fact_collector.collect(collected_facts=facts)
    assert facts.get('apparmor')
    apparmor = facts.get('apparmor')
    if os.path.exists('/sys/kernel/security/apparmor'):
        assert apparmor.get('status') == 'enabled'
    else:
        assert apparmor.get('status') == 'disabled'

# Generated at 2022-06-13 02:21:02.309489
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    fact_collector = ApparmorFactCollector()
    test_apparmor_facts = fact_collector.collect()
    assert 'apparmor' in test_apparmor_facts
    assert test_apparmor_facts['apparmor']['status'] == 'enabled'


# Generated at 2022-06-13 02:21:05.497952
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_facts = {'status': 'disabled'}
    collected_facts = {'apparmor': apparmor_facts}

    assert ApparmorFactCollector().collect(collected_facts) == collected_facts

# Generated at 2022-06-13 02:21:06.068530
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    pass

# Generated at 2022-06-13 02:21:12.508199
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact_collector = ApparmorFactCollector()
    assert apparmor_fact_collector.collect() == {'apparmor': {'status': 'disabled'}}

# Generated at 2022-06-13 02:21:19.236337
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    print('Test type: {}'.format(os.path.basename(__file__)))

    if os.path.exists('/sys/kernel/security/apparmor'):
        print('Apparmor status: enabled')
    else:
        print('Apparmor status: disabled')

    print('Test method collect of class ApparmorFactCollector')

    # test case 1
    fact_collector  = ApparmorFactCollector()
    apparmor_dict = fact_collector.collect()
    print(apparmor_dict)

    # test case 2
    apparmor_dict = ApparmorFactCollector().collect()
    print(apparmor_dict)

# test case 1
test_ApparmorFactCollector_collect()

# Generated at 2022-06-13 02:21:22.532627
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    fact_collector = ApparmorFactCollector()
    apparmor = fact_collector.collect()
    assert apparmor == {'apparmor':{ 'status': 'disabled' }}

# Generated at 2022-06-13 02:21:25.995789
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    from ansible.module_utils.facts.collector.apparmor import ApparmorFactCollector
    apparmor_fact = ApparmorFactCollector()
    assert apparmor_fact.collect() == {'apparmor': {'status': 'disabled'}}

# Generated at 2022-06-13 02:21:31.870895
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_dict = {}
    apparmor_dict['status'] = 'enabled'
    apparmor_dict['some_other_key'] = 'some_other_value'
    expected_dict = {}
    expected_dict['apparmor'] = apparmor_dict
    fact_collector = ApparmorFactCollector()
    assert fact_collector.collect() == expected_dict

# Generated at 2022-06-13 02:21:35.007404
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    fact_collector = ApparmorFactCollector()
    facts = fact_collector.collect()
    assert facts['apparmor']['status'] == 'enabled'

# Generated at 2022-06-13 02:21:35.607423
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
	pass

# Generated at 2022-06-13 02:21:40.732087
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    fact_collector = ApparmorFactCollector()
    facts_dict = fact_collector.collect(collected_facts=None)
    if os.path.exists('/sys/kernel/security/apparmor'):
        assert facts_dict['apparmor']['status'] == 'enabled'
    else:
        assert facts_dict['apparmor']['status'] == 'disabled'

# Generated at 2022-06-13 02:21:43.183783
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    a = ApparmorFactCollector()
    result = a.collect()
    assert result['apparmor'] == {
        'status': 'enabled'
    }

# Generated at 2022-06-13 02:21:48.290027
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    class Test():
        pass

    module = Test()
    module.params = 'not used'
    module.exit_json = 'not used'
    module.ansible_facts = dict()
    module.run_command = 'not used'

    c = ApparmorFactCollector()
    result = c.collect(module=module, collected_facts=None)
    assert result['apparmor']['status'] in ['enabled', 'disabled']

# Generated at 2022-06-13 02:21:54.989311
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    factCollector = ApparmorFactCollector()
    factCollector.collect()

# Generated at 2022-06-13 02:21:57.147457
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact_collector = ApparmorFactCollector()
    assert(apparmor_fact_collector.collect() == {'apparmor': {'status': 'disabled'}})

# Generated at 2022-06-13 02:21:58.829810
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():

    assert_equal(ApparmorFactCollector.collect(), {
        'apparmor': {
            'status': 'disabled'
        }
    })

# Generated at 2022-06-13 02:22:02.374124
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_collector = ApparmorFactCollector()
    apparmor_mocked_ansible_module = MockAnsibleModule()
    apparmor_collector.collect(module=apparmor_mocked_ansible_module)
    ansible_output = apparmor_mocked_ansible_module.exit_json()
    assert 'apparmor' in ansible_output['ansible_facts']
    assert 'status' in ansible_output['ansible_facts']['apparmor']

# Unit test class

# Generated at 2022-06-13 02:22:06.062315
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor = ApparmorFactCollector()
    apparmor_facts = apparmor.collect()
    assert apparmor_facts['apparmor']['status'] == 'disabled'

# Generated at 2022-06-13 02:22:12.409365
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    from ansible.module_utils.facts.collectors.apparmor import ApparmorFactCollector
    from ansible.module_utils.facts.collectors.apparmor import BaseFactCollector
    # BaseFactCollector is abstract
    assert BaseFactCollector is not None
    apparmor_instance = ApparmorFactCollector()
    # _fact_ids must be overwritten by subclasses
    assert len(apparmor_instance._fact_ids) == 0
    assert len(apparmor_instance.collect()) > 0

# Generated at 2022-06-13 02:22:13.801495
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    test_obj = ApparmorFactCollector()
    res = test_obj.collect()


# Generated at 2022-06-13 02:22:17.617837
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_facts = ApparmorFactCollector().collect()
    assert apparmor_facts['apparmor']['status'] == 'disabled'

# Generated at 2022-06-13 02:22:19.449050
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact_obj = ApparmorFactCollector()
    assert apparmor_fact_obj.collect()['apparmor']['status'] == 'disabled'

# Generated at 2022-06-13 02:22:21.714970
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_collector = ApparmorFactCollector()
    result = apparmor_collector.collect()
    assert isinstance(result, dict)

# Generated at 2022-06-13 02:22:34.461341
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
  obj = ApparmorFactCollector()
  facts = obj.collect()
  assert isinstance(facts, dict)
  assert 'apparmor' in facts

# Generated at 2022-06-13 02:22:38.956176
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
  # Create instance of ApparmorFactCollector
  apparmorfactcollector = ApparmorFactCollector()

  # Call collect method of ApparmorFactCollector
  apparmorfactcollector.collect()

  # Check if instance of ApparmorFactCollector has 'apparmor' key
  if 'apparmor' in apparmorfactcollector.collect():
    return True
  return False

# Generated at 2022-06-13 02:22:40.965662
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    asc = ApparmorFactCollector()
    facts = asc.collect()
    assert type(facts['apparmor']['status']) == str

# Generated at 2022-06-13 02:22:46.039790
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    """
    Assumptions:
    - The file /sys/kernel/security/apparmor does exist.
    """
    apparmor_fact_collector = ApparmorFactCollector()
    facts = apparmor_fact_collector.collect({})
    assert facts['apparmor']['status'] == 'enabled'

# Generated at 2022-06-13 02:22:47.626671
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact_collector = ApparmorFactCollector()
    apparmor_fact_collector.collect()

# Generated at 2022-06-13 02:22:48.454918
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    ApparmorFactCollector.collect()

# Generated at 2022-06-13 02:22:52.317780
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    collector = ApparmorFactCollector()
    results = collector.collect()
    assert isinstance(results['apparmor'], dict)
    assert isinstance(results['apparmor']['status'], str)
    assert results['apparmor']['status'] in ('enabled', 'disabled')

# Generated at 2022-06-13 02:22:54.401629
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    c = ApparmorFactCollector()
    facts = c.collect()
    assert 'apparmor' in facts
    assert 'status' in facts['apparmor']

# Generated at 2022-06-13 02:22:56.562416
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    pass

# Generated at 2022-06-13 02:22:58.439022
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    fact = ApparmorFactCollector()
    assert type(fact.collect()) is dict


# Generated at 2022-06-13 02:23:22.011189
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    TestFacts = ApparmorFactCollector()
    result = TestFacts.collect()
    assert result['apparmor']['status'] != 'disabled'

# Generated at 2022-06-13 02:23:25.313423
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    fact_collector = ApparmorFactCollector()
    facts_dict = fact_collector.collect()
    assert facts_dict['apparmor']['status'] == 'disabled'


# Generated at 2022-06-13 02:23:27.947944
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    fact_collector = ApparmorFactCollector()
    result = fact_collector.collect()
    assert result == {'apparmor' : {'status' : 'disabled'}}

# Generated at 2022-06-13 02:23:31.325899
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    # create instance of class
    input_obj = ApparmorFactCollector()
    # call method collect
    result = input_obj.collect()
    # assert the return and the result
    assert result is not None
    assert result['apparmor']['status'] == 'enabled'

# Generated at 2022-06-13 02:23:35.809232
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    with open('/sys/kernel/security/apparmor') as f:
        pass
    system = ApparmorFactCollector()
    assert system.collect() == {'apparmor': {'status': 'enabled'}}
    system = ApparmorFactCollector()
    assert system.collect() == {'apparmor': {'status': 'disabled'}}

# Generated at 2022-06-13 02:23:37.882014
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact_collector = ApparmorFactCollector()
    apparmor_fact_collector.collect()
    assert apparmor_fact_collector.name == 'apparmor'

# Generated at 2022-06-13 02:23:47.413626
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    '''Unit test for method collect of class ApparmorFactCollector'''
    # Create an instance of ApparmorFactCollector
    apparmor_fact_collector = ApparmorFactCollector()
    # Create a fake modules and facts
    modules = []
    facts = {}

# Generated at 2022-06-13 02:23:49.112279
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact_collector = ApparmorFactCollector()
    print(apparmor_fact_collector.collect())


# Generated at 2022-06-13 02:23:54.579635
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    # Create a fact collector
    fact_collector = ApparmorFactCollector()

    # Collect facts
    collected_facts = fact_collector.collect()

    # Test that the result is correct
    assert 'apparmor' in collected_facts
    assert collected_facts['apparmor']['status'] == 'enabled' or collected_facts['apparmor']['status'] == 'disabled'

# Generated at 2022-06-13 02:23:58.848695
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact = ApparmorFactCollector()
    facts = apparmor_fact.collect()
    assert isinstance(facts, dict)
    assert isinstance(facts['apparmor'], dict)
    assert 'status' in facts['apparmor']
    assert isinstance(facts['apparmor']['status'], str)

# Generated at 2022-06-13 02:24:51.175677
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts.collector import Collector
    import os
    import os.path

    class FakeCollector(Collector):

        def __init__(self):
            self.name = 'apparmor'
            self._fact_ids = set()

        def collect(self, module=None, collected_facts=None):
            facts_dict = {}
            apparmor_facts = {}
            if os.path.exists('/sys/kernel/security/apparmor'):
                apparmor_facts['status'] = 'enabled'
            else:
                apparmor_facts['status'] = 'disabled'

            facts_dict['apparmor'] = apparmor_facts
            return facts_dict


# Generated at 2022-06-13 02:24:53.005664
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_status = {'apparmor': {'status': 'enabled'}}
    a = ApparmorFactCollector()
    assert apparmor_status == a.collect()

# Generated at 2022-06-13 02:24:55.841525
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    collector = ApparmorFactCollector()
    collectors = {'Apparmor' : ApparmorFactCollector()}
    ansible_facts = collector.collect(None)
    assert 'apparmor' in ansible_facts

# Generated at 2022-06-13 02:24:57.715531
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    ApparmorFactCollector()

# Generated at 2022-06-13 02:24:59.230218
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    AF = ApparmorFactCollector()
    assert AF.collect() == {}
    assert AF._fact_ids == set()

# Generated at 2022-06-13 02:25:02.495949
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    """Unit test for method collect of class ApparmorFactCollector
    """
    apparmor_fc = ApparmorFactCollector()
    result = apparmor_fc.collect()
    assert 'apparmor' in result

# Generated at 2022-06-13 02:25:06.467345
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    import sys
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    mod_apparmor_facts = ApparmorFactCollector()
    mod_apparmor_facts.collect(module=module)
    assert mod_apparmor_facts.fact_ids() == set(['apparmor'])

# Generated at 2022-06-13 02:25:12.757105
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    import os
    import shutil
    import tempfile

    tempdir = tempfile.mkdtemp()
    os.mkdir(os.path.join(tempdir, 'sys'))
    os.mkdir(os.path.join(tempdir, 'sys', 'kernel'))
    os.mkdir(os.path.join(tempdir, 'sys', 'kernel', 'security'))
    os.mkdir(os.path.join(tempdir, 'sys', 'kernel', 'security', 'apparmor'))

    fact_collector = ApparmorFactCollector()
    collected_facts = fact_collector.collect()
    assert collected_facts['apparmor']['status'] == 'enabled'

    shutil.rmtree(tempdir)
    collected_facts = fact_collector.collect()
    assert collected_facts

# Generated at 2022-06-13 02:25:17.800916
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmorFactCollector = ApparmorFactCollector()
    apparmorFactCollector._module = object()
    apparmorFactCollector._collect_platform_subset(object())
    apparmorFactCollector._collect_command_outputs(object())

# vim: set et ts=4 sw=4 :

# Generated at 2022-06-13 02:25:24.441937
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_mock = ApparmorFactCollector()

    # Case test for enabled apparmor
    apparmor_mock.collect()
    assert apparmor_mock.name == 'apparmor'
    assert apparmor_mock._fact_ids == set()
    assert apparmor_mock.collect().get('apparmor').get('status') == 'enabled'

    # Case test for disabled apparmor
    apparmor_mock._os.path.exists.return_value = False
    assert apparmor_mock.collect().get('apparmor').get('status') == 'disabled'

# Generated at 2022-06-13 02:27:18.216276
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    assert ApparmorFactCollector().collect() == {
        'apparmor': {
            'status': 'disabled'
        }
    }

# Generated at 2022-06-13 02:27:22.064319
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact_collector = ApparmorFactCollector()
    facts_dict = apparmor_fact_collector.collect()
    assert apparmor_fact_collector.name in facts_dict
    assert len(apparmor_fact_collector._fact_ids) == 0

# Generated at 2022-06-13 02:27:23.102586
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    aafc = ApparmorFactCollector()
    aafc.collect()

# Generated at 2022-06-13 02:27:25.134472
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_facts = {'status': 'enabled'}
    test_obj = ApparmorFactCollector()
    facts = test_obj.collect()['ansible_facts']
    assert facts['apparmor'] == apparmor_facts

# Generated at 2022-06-13 02:27:26.284025
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact_collector = ApparmorFactCollector()
    assert apparmor_fact_collector.collect() != {}

# Generated at 2022-06-13 02:27:28.244086
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():

    # Create a new ApparmorFactCollector object
    apt = ApparmorFactCollector()

    # Collect apparmor facts
    apt.collect()

    # Test if apparmor facts were collected
    assert 'apparmor' in apt.collect()


# Generated at 2022-06-13 02:27:30.118648
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact = ApparmorFactCollector()
    apparmor_fact.collect()
    output = apparmor_fact.get_facts()
    assert "enabled" in output['apparmor']['status']
    assert "disabled" in output['apparmor']['status']

# Generated at 2022-06-13 02:27:32.278722
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    apparmor_fact_collector = ApparmorFactCollector()
    assert isinstance(apparmor_fact_collector, BaseFactCollector)
    assert apparmor_fact_collector.name == 'apparmor'
    result = apparmor_fact_collector.collect(collected_facts=None)
    assert 'apparmor' in result
    assert 'disabled' in result['apparmor']['status']

# Generated at 2022-06-13 02:27:36.095454
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    afc = ApparmorFactCollector()
    result = afc.collect()
    assert result['apparmor']['status'] == 'disabled'


# Generated at 2022-06-13 02:27:38.434002
# Unit test for method collect of class ApparmorFactCollector
def test_ApparmorFactCollector_collect():
    collector = ApparmorFactCollector()
    collection = collector.collect()

    assert collection == {'apparmor': {'status': 'disabled'}}