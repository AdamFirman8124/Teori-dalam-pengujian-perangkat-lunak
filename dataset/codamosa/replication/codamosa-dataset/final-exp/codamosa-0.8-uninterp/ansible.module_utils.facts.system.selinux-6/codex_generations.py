

# Generated at 2022-06-13 03:22:58.999398
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    facts_dict = dict()
    selinux_facts = dict()
    selinux_facts['status'] = 'Missing selinux Python library'
    facts_dict['selinux'] = selinux_facts
    facts_dict['selinux_python_present'] = False

    sfc = SelinuxFactCollector()
    assert sfc.collect() == facts_dict
    assert sfc.name == 'selinux'

# Generated at 2022-06-13 03:23:00.156062
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    mySelinux = SelinuxFactCollector()
    assert mySelinux.name == 'selinux'

# Generated at 2022-06-13 03:23:09.675088
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # If a library is available, collect() should return a dict
    # containing status, mode, type and config_mode.
    selinux_instance = SelinuxFactCollector()
    if HAVE_SELINUX:
        facts_dict = selinux_instance.collect()
        assert isinstance(facts_dict, dict), 'facts_dict should be a dict'
        assert 'selinux' in facts_dict, 'facts_dict should have a selinux key'
        for key in ['status', 'mode', 'type', 'config_mode']:
            assert key in facts_dict['selinux'], 'facts should have a {} key'.format(key)

# Generated at 2022-06-13 03:23:15.604160
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_facts = {
        'status': 'enabled',
        'policyvers': 'unknown',
        'config_mode': 'unknown',
        'mode': 'unknown',
        'type': 'unknown'
    }

    facts_dict = SelinuxFactCollector().collect()
    assert facts_dict['selinux'] == {'status': 'Missing selinux Python library'}
    assert facts_dict['selinux_python_present'] is False

# Generated at 2022-06-13 03:23:17.359601
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.name == 'selinux'

# Generated at 2022-06-13 03:23:22.858935
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    import sys
    sys.modules['selinux'] = MockSelinuxModule()
    c = SelinuxFactCollector()
    assert c.collect() == { 'selinux': { 'status': 'enabled', 'mode': 'disabled',
                                         'policyvers': '42', 'config_mode': 'permissive' },
                            'selinux_python_present': True }


# Generated at 2022-06-13 03:23:24.545383
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    obj = SelinuxFactCollector()
    assert obj.name == 'selinux'
    assert obj._fact_ids == set()


# Generated at 2022-06-13 03:23:31.100894
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    try:
        import selinux
        selinux_available = True
    except ImportError:
        selinux_available = False

    selinux_present = 'selinux_python_present'
    selinux_facts = 'selinux'
    selinux_disabled = 'disabled'
    selinux_enabled = 'enabled'
    selinux_unknown = 'unknown'

    # Using a proxy object to prevent a selinux.is_selinux_enabled() call
    class SELinux:
        def __init__(self, selinux=False):
            self.selinux = selinux

        def is_selinux_enabled(self):
            return self.selinux

        def set_selinux_enabled(self, enabled):
            self.selinux = enabled

    # Check the facts returned when selinux is enabled

# Generated at 2022-06-13 03:23:44.015421
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    from ansible.module_utils.facts import collector

    # Create a mock selinux module
    selinux = collector.__import__('ansible.module_utils.compat.selinux')

    # Create a mock module
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={})

    # Create a mock AnsibleModule.selinux method

# Generated at 2022-06-13 03:23:46.823233
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    # test idempotency
    selinux_collector = SelinuxFactCollector()
    selinux_collector2 = SelinuxFactCollector()
    assert selinux_collector == selinux_collector2

# Generated at 2022-06-13 03:23:58.295531
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert 'selinux' == selinux_fact_collector.name
    assert set() == selinux_fact_collector._fact_ids

# Generated at 2022-06-13 03:24:08.689838
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    if HAVE_SELINUX:
        # Enable SELinux if disabled
        if selinux.is_selinux_enabled() == 0:
            selinux.selinux_setenforce(1)

        test_fact = SelinuxFactCollector()
        facts = test_fact.collect()

        assert 'selinux' in facts.keys()
        assert isinstance(facts['selinux'], dict)
        assert 'status' in facts['selinux'].keys()
        assert isinstance(facts['selinux']['status'], str)
        assert 'type' in facts['selinux'].keys()
        assert isinstance(facts['selinux']['type'], str)
        assert 'mode' in facts['selinux'].keys()

# Generated at 2022-06-13 03:24:17.068100
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    AnsibleModule = {}
    AnsibleModule['selinux_python_present'] = False

    AnsibleModule['selinux'] = {}
    AnsibleModule['selinux']['status'] = 'Unable to determine selinux status'
    AnsibleModule['selinux']['config_mode'] = 'Unknown'
    AnsibleModule['selinux']['mode'] = 'Unknown'
    AnsibleModule['selinux']['type'] = 'Unknown'
    AnsibleModule['selinux']['policyvers'] = 'Unknown'

    testCollector = SelinuxFactCollector()

    testCollector.collect(AnsibleModule)

    assert AnsibleModule['selinux_python_present'] == False

# Generated at 2022-06-13 03:24:19.845671
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    assert SelinuxFactCollector.name == 'selinux'
    x = SelinuxFactCollector()
    x.collect()

# vim: set expandtab shiftwidth=4:

# Generated at 2022-06-13 03:24:20.700565
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_facts = SelinuxFactCollector()
    assert selinux_facts.name == 'selinux'

# Generated at 2022-06-13 03:24:22.547614
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_facts = SelinuxFactCollector()
    assert selinux_facts is not None

# Generated at 2022-06-13 03:24:23.400265
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    SelinuxFactCollector().collect()

# Generated at 2022-06-13 03:24:29.735246
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    import pytest
    from ansible.module_utils.facts.collector import get_collector_instance
    # Setup testing object attributes
    obj = get_collector_instance('SelinuxFactCollector')
    obj._fact_ids = set()
    # Testing with selinux library present
    # Testing with selinux disabled in the system
    HAVE_SELINUX = True
    selinux.is_selinux_enabled = lambda : False
    selinux.selinux_getenforcemode = lambda : (0, -1)
    selinux.security_getenforce = lambda : -1
    selinux.selinux_getpolicytype = lambda : (0, 'unknown')
    selinux.security_policyvers = lambda : 'unknown'

# Generated at 2022-06-13 03:24:38.413667
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    fact_collector = SelinuxFactCollector()
    collected_facts = fact_collector.collect()
    assert fact_collector.name == 'selinux'
    assert 'selinux' in collected_facts
    assert 'selinux_python_present' in collected_facts
    # If selinux library is not present, just test whether selinux_python_present is set False
    if collected_facts.get('selinux_python_present', True):
        assert 'status' in collected_facts['selinux']
        assert 'policyvers' in collected_facts['selinux']
        assert 'config_mode' in collected_facts['selinux']
        assert 'mode' in collected_facts['selinux']
        assert 'type' in collected_facts['selinux']

# Generated at 2022-06-13 03:24:47.740754
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    '''Unit test for method collect of class SelinuxFactCollector'''

    # test_SelinuxFactCollector_collect_1: 'selinux' shall not be in the base class's _fact_ids
    assert 'selinux' not in SelinuxFactCollector._fact_ids

    # test_SelinuxFactCollector_collect_2: 'selinux' shall be in the class's _fact_ids
    assert 'selinux' in SelinuxFactCollector._fact_ids

    # test_SelinuxFactCollector_collect_3: False shall be returned if there is no selinux Python library
    collector = SelinuxFactCollector()
    assert collector.collect()['selinux_python_present'] is False

    # test_SelinuxFactCollector_collect_4: True shall be returned if

# Generated at 2022-06-13 03:25:06.837404
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    obj = SelinuxFactCollector()
    assert obj.name == 'selinux'
    assert obj._fact_ids == set()


# Generated at 2022-06-13 03:25:12.794665
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_obj = SelinuxFactCollector()
    selinux_facts = selinux_obj.collect()
    assert selinux_facts['selinux']['config_mode'] == 'unknown'
    assert selinux_facts['selinux_python_present'] == True


# Generated at 2022-06-13 03:25:22.073172
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # Create a test collector object
    test_col = SelinuxFactCollector()

    # Create a test dict to pass in as collected_facts (module_utils.facts.collector.BaseFactCollector)
    test_collected_facts = {}

    # Call the collect method
    test_collected_facts = test_col.collect()

    # Assert that the collect method returned a dict
    assert type(test_collected_facts) is dict

    # Assert that the collect method returned a dict containing the key 'selinux'
    assert test_collected_facts.has_key('selinux') is True

    # Assert that the collect method returned a dict containing the key 'selinux', which is itself a dict
    assert type(test_collected_facts['selinux']) is dict


# Generated at 2022-06-13 03:25:25.430763
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    fact_collector = SelinuxFactCollector()
    assert fact_collector.name == 'selinux'
    assert 'selinux' in fact_collector._fact_ids

# Generated at 2022-06-13 03:25:27.616794
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_collector = SelinuxFactCollector()

    selinux_collector.collect()

# Generated at 2022-06-13 03:25:37.805904
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    test_object = SelinuxFactCollector()
    # Create a test selinux module to use
    selinux_module = __import__('selinux')

    # Test with no selinux module.  Should return
    #   {'selinux_python_present': False, 'selinux': {'status': 'Missing selinux Python library'}}
    result = test_object.collect(selinux_module)
    assert({'selinux_python_present': False, 'selinux': {'status': 'Missing selinux Python library'}} == result)

    # Test with no SELinux enabled.  Should return
    #   {'selinux_python_present': True, 'selinux': {'mode': 'disabled', 'config_mode': 'disabled'}}
    selinux_module.is_selinux

# Generated at 2022-06-13 03:25:40.375119
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinuxfacts = SelinuxFactCollector()
    assert selinuxfacts is not None

# Generated at 2022-06-13 03:25:44.957844
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    # Dummy collected_facts
    collected_facts = {}
    # Dummy module
    module = None
    fact_collector = SelinuxFactCollector()
    assert fact_collector.name == 'selinux'
    assert fact_collector._fact_ids == set()
    fact_collector.collect(module, collected_facts)

# Generated at 2022-06-13 03:25:48.361004
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    collected_facts = dict()
    obj = SelinuxFactCollector()
    obj.collect(collected_facts=collected_facts)
    selinux = collected_facts['selinux']
    assert selinux['status'] == 'Missing selinux Python library'

# Generated at 2022-06-13 03:25:53.000711
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.name == 'selinux'
    assert selinux_fact_collector._fact_ids == set()

# Generated at 2022-06-13 03:26:29.625652
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_facts_collector = SelinuxFactCollector()
    selinux_facts = selinux_facts_collector.collect()
    assert selinux_facts['selinux']['status'] is not None

# Generated at 2022-06-13 03:26:32.756334
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    collector = SelinuxFactCollector()
    assert collector.name == 'selinux'
    assert collector._fact_ids == set()


# Generated at 2022-06-13 03:26:33.474639
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    pass


# Generated at 2022-06-13 03:26:38.997005
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # set up the object
    selinux_fact_collector = SelinuxFactCollector()

    # ensure that the object collects facts correctly
    assert selinux_fact_collector.collect() == {
        'selinux': {'status': 'enabled'},
        'selinux_python_present': True
    }

# Generated at 2022-06-13 03:26:47.256663
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    from ansible.module_utils.facts import (
        get_collector_instance,
        get_collector_fact_ids,
    )
    from ansible.module_utils.facts.collectors.selinux import SelinuxFactCollector

    # collect facts
    collector = get_collector_instance(SelinuxFactCollector)
    facts = collector.collect()

    # test that fact name and all fact ids are present in facts
    assert 'selinux' in facts
    assert set(get_collector_fact_ids(SelinuxFactCollector)) == set(facts.keys())

# Generated at 2022-06-13 03:26:54.865836
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    import pytest

    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.compat import selinux

    # Setup a mock for the selinux library
    # There is no way to disable SELinux in the test environment since the
    # the library is always present. A better approach would be to use a
    # shared library that both the fact module and the test can use.
    original_selinux_module_getenforce = selinux.getenforce

    # Example of how to create a Mock object to return a fixed value.
    #selinux_mock = Mock()
    #selinux_mock.return_value = 'permissive'
    #selinux.getenforce = selinux_mock

    # Example of how to create a Mock object to return a dynamic value.


# Generated at 2022-06-13 03:27:05.395991
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    """Test that collect returns correct data"""
    from ansible.module_utils.facts.collector import Collector

    # Make sure that collecting facts is callable
    sc = SelinuxFactCollector()
    fact_list = sc.collect()
    assert 'selinux' in fact_list

    # Make sure that collecting facts is called only once
    # by passing a previously collected fact to a new collector
    sc = SelinuxFactCollector(fact_list)
    fact_list = sc.collect()
    assert 'selinux' in fact_list

    # Verify that collect() produces the same results as
    # the collect_function defined in the collector class
    sc = SelinuxFactCollector(fact_list)
    func_fact_list = sc.collect_function()
    assert func_fact_list == fact_list

# Generated at 2022-06-13 03:27:09.097948
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux = SelinuxFactCollector()
    assert selinux.name == 'selinux'
    assert selinux._fact_ids == set()

# Generated at 2022-06-13 03:27:13.963279
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_instance = SelinuxFactCollector()
    assert selinux_fact_instance.name == 'selinux'
    # Since we aren't running on an actual system, assert set is empty
    assert not selinux_fact_instance._fact_ids

# Generated at 2022-06-13 03:27:24.824270
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # Test with Python selinux library not present
    setattr(selinux, '__file__', '/does_not_exist')
    collector = SelinuxFactCollector()
    facts_dict = collector.collect()

    assert facts_dict['selinux']['status'] == 'Missing selinux Python library'
    assert facts_dict['selinux_python_present'] == False

    # Test with Python selinux library present
    setattr(selinux, '__file__', '/usr/lib/python2.7/site-packages/ansible/module_utils/compat/selinux.py')
    collector = SelinuxFactCollector()
    facts_dict = collector.collect()

    assert facts_dict['selinux_python_present'] == True

# Generated at 2022-06-13 03:28:00.729891
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    import pytest

    obj = SelinuxFactCollector()
    assert obj.name == 'selinux'


# Generated at 2022-06-13 03:28:02.184603
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    assert isinstance(SelinuxFactCollector(), SelinuxFactCollector)

# Generated at 2022-06-13 03:28:03.897495
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    obj = SelinuxFactCollector()
    assert obj.name == "selinux"
    assert isinstance(obj._fact_ids, set)
    assert obj._fact_ids == set()

# Generated at 2022-06-13 03:28:05.757946
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_collector = SelinuxFactCollector()
    assert selinux_collector.name == 'selinux'
    assert len(selinux_collector._fact_ids) == 0

# Generated at 2022-06-13 03:28:07.618029
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fc = SelinuxFactCollector()
    assert selinux_fc.name == 'selinux'

# Generated at 2022-06-13 03:28:08.666657
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    col = SelinuxFactCollector()
    print(col.collect())

# Generated at 2022-06-13 03:28:14.175820
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_facts = SelinuxFactCollector.collect()
    assert selinux_facts['selinux']['status'] == 'disabled'
    assert selinux_facts['selinux']['config_mode'] == 'unknown'
    assert selinux_facts['selinux']['mode'] == 'unknown'
    assert selinux_facts['selinux']['type'] == 'unknown'
    assert selinux_facts['selinux']['policyvers'] == 'unknown'
    assert selinux_facts['selinux_python_present'] == False

# Generated at 2022-06-13 03:28:16.747229
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    my_mock = SelinuxFactCollector()
    my_mock.collect()

# Generated at 2022-06-13 03:28:20.385157
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    x = SelinuxFactCollector()
    assert x.name == 'selinux'
    assert not x._fact_ids
    assert x.collect() == {'selinux': {'status': 'Missing selinux Python library'}, 'selinux_python_present': False}

# Generated at 2022-06-13 03:28:24.357177
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # Selinux library is not present. 
    # Only selinux_python_present boolean and selinux status should be set.
    collector = SelinuxFactCollector()
    collected_facts = collector.collect()
    assert collected_facts == {'selinux': {'status': 'Missing selinux Python library'}, 'selinux_python_present': False}


test_SelinuxFactCollector_collect()

# Generated at 2022-06-13 03:30:04.280980
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():

    # Initialize module object
    module = AnsibleModuleMock()

    # Initialize fact collector
    selinux_collector = SelinuxFactCollector(module=module)

    # Switching the value of HAVE_SELINUX variable to True
    global HAVE_SELINUX
    HAVE_SELINUX = True

    # Testing for the return value of collect method
    result = selinux_collector.collect()
    assert result['selinux']['mode'] == 'unknown'
    assert result['selinux_python_present'] == True

    # Switching the value of HAVE_SELINUX variable to False
    HAVE_SELINUX = False

    # Testing for the return value of collect method
    result = selinux_collector.collect()

# Generated at 2022-06-13 03:30:08.662305
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_facts = SelinuxFactCollector().collect()
    assert selinux_facts is not None
    assert 'status' in selinux_facts['selinux']
    assert 'python_present' in selinux_facts

# Generated at 2022-06-13 03:30:12.507570
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_facts = SelinuxFactCollector()
    assert selinux_facts.name == 'selinux'
    assert selinux_facts._fact_ids == set()



# Generated at 2022-06-13 03:30:15.655775
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.name == 'selinux'
    assert selinux_fact_collector._fact_ids == set()


# Generated at 2022-06-13 03:30:18.793066
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_collector = SelinuxFactCollector()
    assert selinux_collector.name == 'selinux'

# Generated at 2022-06-13 03:30:28.620261
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    assert have_selinux_library, 'This module needs selinux library.'
    selinux_facts = SelinuxFactCollector().collect()['selinux']

    assert selinux_facts['mode'] == selinux.security_getenforce()
    assert selinux_facts['policyvers'] == selinux.security_policyvers()

    rc, configmode = selinux.selinux_getenforcemode()
    assert selinux_facts['config_mode'] == configmode

    rc, policytype = selinux.selinux_getpolicytype()
    assert selinux_facts['type'] == policytype

    if not selinux.is_selinux_enabled():
        assert selinux_facts['status'] == 'disabled'



# Generated at 2022-06-13 03:30:29.769205
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # Not tested because the selinux module is not mocked
    pass

# Generated at 2022-06-13 03:30:39.428783
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # Create an empty SelinuxFactCollector object
    fact_collector = SelinuxFactCollector()

    # Create a local dict to temporarily hold the collected facts
    collected_facts = {}

    # Call SelinuxFactCollector.collect()
    collected_facts = fact_collector.collect()

    # Check the returned dict
    assert collected_facts.get('selinux_python_present')

    # Check that 'selinux' is in the returned dict
    assert 'selinux' in collected_facts

    # Check that 'selinux' is populated
    assert collected_facts['selinux']

    # Check that 'selinux' has expected keys
    assert 'status' in collected_facts['selinux']
    assert 'config_mode' in collected_facts['selinux']
    assert 'mode' in collected

# Generated at 2022-06-13 03:30:40.880618
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_collector = SelinuxFactCollector()
    assert selinux_collector.name == 'selinux'

# Generated at 2022-06-13 03:30:48.771943
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # Disabling the Selinux library will make is_selinux_enabled() always return False
    selinux.is_selinux_enabled = lambda: False

    # Run the collect() method
    facts_dict = SelinuxFactCollector().collect()

    # Check that the output is correct
    assert 'selinux_python_present' in facts_dict
    assert 'selinux' in facts_dict
    selinux_facts = facts_dict['selinux']
    assert 'status' in selinux_facts
    assert selinux_facts['status'] == 'disabled'
    assert len(selinux_facts.keys()) == 1