

# Generated at 2022-06-13 03:23:01.842310
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    collector = SelinuxFactCollector()
    assert collector.name == "selinux"
    assert collector.seclabel_environ_vars == ['ANSIBLE_SELINUX_SPECIAL_FS']
    assert collector.seclabel_environ_regex == r'^(?P<type>[a-z]+)\s+(?P<mls_range>s0)+(?:\s+(?P<context>.+))?$'
    assert collector.seclabel_path_regex == r'^(?P<path>/.+)=(?P<type>[a-z]+)\s+(?P<mls_range>s0)+(?:\s+(?P<context>.+))?$'

# Generated at 2022-06-13 03:23:13.280626
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    from ansible.module_utils.facts.collector import Facts
    from ansible.module_utils.facts.system.selinux import SelinuxFactCollector
    from ansible.module_utils.compat import selinux

    # Arrange
    facts = Facts()
    selinux_fact_collector = SelinuxFactCollector()

    # Act
    selinux_facts = selinux_fact_collector.collect(facts=facts)

    # Assert
    assert selinux_facts['selinux']['status'] == 'Missing selinux Python library'
    assert selinux_facts['selinux_python_present'] is False

    # Arrange
    selinux_fact_collector.HAVE_SELINUX = True

    # Mock selinux API

# Generated at 2022-06-13 03:23:21.038493
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_python_present = True
    test_status = 'enabled'
    test_policyvers = '28'
    test_config_mode = 'enforcing'
    test_mode = 'enforcing'
    test_type = 'targeted'
    test_rc = 0

    class Mock_selinux():

        def is_selinux_enabled(self):
            return True

        def security_policyvers(self):
            return test_policyvers

        def selinux_getenforcemode(self):
            # print("selinux_getenforcemode: {}".format(test_config_mode))
            return (test_rc, test_config_mode)

        def security_getenforce(self):
            # print("security_getenforce: {}".format(test_mode))
            return test_mode

       

# Generated at 2022-06-13 03:23:27.625599
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():

    selinux_collector = SelinuxFactCollector()

    # Test with selinux library imports
    facts_dict = selinux_collector.collect()
    assert len(facts_dict) == 2
    assert facts_dict['selinux_python_present'] == True

    # Test without selinux library imports
    with_selinux = SelinuxFactCollector.HAVE_SELINUX
    SelinuxFactCollector.HAVE_SELINUX = False

    facts_dict = selinux_collector.collect()
    assert len(facts_dict) == 2
    assert facts_dict['selinux_python_present'] == False

    SelinuxFactCollector.HAVE_SELINUX = with_selinux


# Generated at 2022-06-13 03:23:32.579047
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # Stubbed out selinux library in first code block.  Test both code paths.
    try:
        selinux.is_selinux_enabled()
        selinux.security_policyvers()
        selinux.selinux_getpolicytype()
        selinux.selinux_getenforcemode()
        selinux.security_getenforce()
        selinux.security_policyvers()
    except AttributeError:
        FAKE_SELINUX = False
    else:
        FAKE_SELINUX = True
    if FAKE_SELINUX:
        old_is_selinux_enabled = selinux.is_selinux_enabled
        old_security_policyvers = selinux.security_policyvers
        old_selinux_getpolicytype = selinux.selinux_getpolicytype


# Generated at 2022-06-13 03:23:37.226218
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.name == 'selinux'
    assert selinux_fact_collector._fact_ids == set()

# Generated at 2022-06-13 03:23:39.123842
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    SelinuxFactCollector()

# Generated at 2022-06-13 03:23:43.635513
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    ansible_module = AnsibleModule(argument_spec={})
    result = SelinuxFactCollector().collect(ansible_module)
    assert result == dict(
        ansible_module.exit_json(
            changed=False,
            ansible_facts=dict(
                selinux=dict(
                    status='Missing selinux Python library'),
                selinux_python_present=False)))

# Generated at 2022-06-13 03:23:46.016531
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    obj = SelinuxFactCollector()
    assert obj.name == 'selinux'
    assert obj._fact_ids == set(['selinux'])

# Generated at 2022-06-13 03:23:56.598411
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # Test without selinux module
    global HAVE_SELINUX
    HAVE_SELINUX = False

    obj = SelinuxFactCollector()
    facts_dict = obj.collect()

    assert facts_dict['selinux']['status'] == 'Missing selinux Python library'
    assert facts_dict['selinux_python_present'] == False

    # Test with selinux module
    HAVE_SELINUX = True

    obj = SelinuxFactCollector()
    facts_dict = obj.collect()

    assert facts_dict['selinux']['status'] == 'enabled'
    assert facts_dict['selinux_python_present'] == True
    assert facts_dict['selinux']['mode'] == 'enforcing'


# Generated at 2022-06-13 03:24:08.187994
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    module = None
    collected_facts = None
    SelinuxFactCollector(module, collected_facts)


# Generated at 2022-06-13 03:24:09.855377
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    """Unit test for constructor of class SelinuxFactCollector."""
    SelinuxFactCollector()

# Generated at 2022-06-13 03:24:10.496235
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    pass

# Generated at 2022-06-13 03:24:16.561588
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # If the selinux module is not present, then the selinux information returned should be minimal
    # and only provide information about the selinux Python library
    fact_collector = SelinuxFactCollector()
    selinux = fact_collector.collect()['selinux']
    assert selinux['status'] == 'Missing selinux Python library'
    assert selinux['mode'] is None
    assert selinux['policyvers'] is None
    assert selinux['type'] is None
    assert selinux['config_mode'] is None
    assert selinux['python_present'] is False

# Generated at 2022-06-13 03:24:18.873004
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    a = SelinuxFactCollector()
    assert a.name == 'selinux'
    assert len(a._fact_ids) == 0, 'expected no facts'


# Generated at 2022-06-13 03:24:21.397258
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector is not None
    assert selinux_fact_collector.name == 'selinux'

# Generated at 2022-06-13 03:24:22.254435
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    pass

# Generated at 2022-06-13 03:24:24.097763
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    collector = SelinuxFactCollector()
    assert collector.name == 'selinux'
    assert not collector._fact_ids

# Generated at 2022-06-13 03:24:26.828438
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect(): 
    module = None
    collected_facts = {}
    s = SelinuxFactCollector()
    facts_dict = s.collect(module, collected_facts)
    assert 'selinux' in facts_dict    
    assert 'selinux_python_present' in facts_dict

# Generated at 2022-06-13 03:24:29.637150
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()

# Generated at 2022-06-13 03:24:41.218813
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinuxfactcollector = SelinuxFactCollector()
    assert selinuxfactcollector.name == 'selinux'
    assert selinuxfactcollector._fact_ids == set()



# Generated at 2022-06-13 03:24:49.703796
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    import sys
    if sys.version_info[0] >= 3:
        from unittest.mock import patch
    else:
        from mock import patch

    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils.facts.collector import get_collector_config
    from ansible.module_utils.facts.collector import get_collector_instance_config_data
    from ansible.module_utils.facts.collector import get_collector_names
    from ansible.module_utils.facts.collector import list_collectors


# Generated at 2022-06-13 03:24:51.599388
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_obj = SelinuxFactCollector()
    assert selinux_obj is not None


# Generated at 2022-06-13 03:25:02.207041
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.collector import BaseFactCollector

    # Set up the class to be unit tested
    selinux_fact_collector = SelinuxFactCollector()

    #Check that the class is a subclass of BaseFactCollector
    assert issubclass(selinux_fact_collector.__class__, BaseFactCollector)

    #Check that the name of the class is correct
    assert selinux_fact_collector.name == 'selinux'

    #Check that the class has the correct fact_ids set
    assert selinux_fact_collector._fact_ids == set()

# Generated at 2022-06-13 03:25:05.284936
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    """Test constructor of class SelinuxFactCollector
    """
    facts_collector = SelinuxFactCollector()
    assert facts_collector.name == 'selinux'

# Unit tests for function collect

# Generated at 2022-06-13 03:25:17.365907
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # Set up the test class
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.collectors import get_collector_class
    Collector._collectors_classes['selinux'] = SelinuxFactCollector
    get_collector_class('ansible.module_utils.facts.collectors.system.selinux')

    # Return values for mocked functions
    ret_selinux_is_selinux_enable = True

    # Test that if selinux lib is not available the status is set to "Missing selinux Python library"
    with patch('ansible.module_utils.facts.collectors.system.selinux.HAVE_SELINUX', new=False):
        sfc = SelinuxFactCollector()
        ret = sfc.collect()

# Generated at 2022-06-13 03:25:28.619460
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # Test data
    collected_facts = dict()
    # Instantiate the class
    selinux_fact_collector = SelinuxFactCollector()
    # Mock the methods
    mocked_methods = dict()

    with patch.multiple(selinux_fact_collector,
                        _get_config_mode=DEFAULT,
                        _get_mode=DEFAULT,
                        _get_policyvers=DEFAULT,
                        _get_type=DEFAULT,
                        is_selinux_enabled=DEFAULT,
                        autospec=True,
                        **mocked_methods) as mocks:

        mocks['is_selinux_enabled'].return_value = False
        selinux_fact_collector.collect()

        # Check if the methods were called
        mocks['is_selinux_enabled'].assert_

# Generated at 2022-06-13 03:25:39.821947
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    if not HAVE_SELINUX:
        return

    obj = SelinuxFactCollector('dummy', True)
    assert obj.name == 'selinux'
    assert obj._fact_ids == set(['selinux', 'selinux_python_present'])

    # Check expected return value with missing selinux Python library
    obj = SelinuxFactCollector('dummy', False)
    result = obj.collect()
    assert result['selinux']['status'] == 'Missing selinux Python library'
    assert result['selinux_python_present'] is False

    # Check expected return value with SELinux enabled
    obj = SelinuxFactCollector('dummy', True)
    result = obj.collect()

    assert result['selinux']['status'] == 'enabled'

# Generated at 2022-06-13 03:25:43.616843
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.name == "selinux"
    assert selinux_fact_collector._fact_ids == set(["selinux", "selinux_python_present"])

# Generated at 2022-06-13 03:25:45.301217
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    x = SelinuxFactCollector()
    assert isinstance(x,BaseFactCollector)

# Generated at 2022-06-13 03:26:08.771514
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # Test if selinux Python library is missing
    if not HAVE_SELINUX:
        instance_collector = SelinuxFactCollector()
        result = instance_collector.collect()
        assert result['selinux_python_present'] == False
        assert result['selinux']
        assert result['selinux']['status'] == 'Missing selinux Python library'
    return



# Generated at 2022-06-13 03:26:11.919365
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    fake_module = type('module', (object,), {})()
    collector = SelinuxFactCollector(fake_module, '127.0.0.1')
    assert collector.name == 'selinux'
    assert collector._fact_ids == set()


# Generated at 2022-06-13 03:26:22.334369
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    import sys
    class dummymodule:
        def __init__(self):
            self.params = dict()
            self.params['gather_subset'] = '!all'

    module = dummymodule()
    collected_facts = dict()
    result = dict()
    result['ansible_selinux_python_present'] = False
    result['ansible_selinux'] = dict()
    result['ansible_selinux']['status'] = 'Missing selinux Python library'

    obj = SelinuxFactCollector()


# Generated at 2022-06-13 03:26:25.043222
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    obj = SelinuxFactCollector()
    assert obj.name == 'selinux'
    assert obj.collect() == { 'selinux': { 'status': 'enabled' }, 'selinux_python_present': True }

# Generated at 2022-06-13 03:26:28.423894
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    collector = SelinuxFactCollector()
    result = collector.collect()
    assert 'selinux' in result
    assert result['selinux']['status'] == 'disabled'


# Generated at 2022-06-13 03:26:36.988665
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():

    # Test with missing selinux library
    # Should return the selinux dictionary with status and the selinux_python_present boolean
    def test_with_missing_selinux_library(monkeypatch):
        monkeypatch.setattr(
            'ansible.module_utils.compat.selinux',
            None
        )
        collector = SelinuxFactCollector()
        result = collector.collect()

        assert result['selinux_python_present'] == False
        assert result['selinux']['status'] == 'Missing selinux Python library'

    # Test that SELinux enabled facts are gathered
    # Enable SELinux for the duration of the test by monkeypatching
    # the selinux.is_selinux_enabled method.
    def test_enable_selinux_facts(monkeypatch):
        monkeypatch

# Generated at 2022-06-13 03:26:44.505445
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    """Unit test for method collect of class SelinuxFactCollector."""
    faked_module = None
    faked_collector = SelinuxFactCollector()
    faked_facts_dict = {'selinux_python_present': True, 'selinux': {'config_mode': 'permissive', 'mode': 'permissive', 'status': 'enabled', 'type': 'targeted', 'policyvers': 'unknown'}}
    assert faked_collector.collect(faked_module) == faked_facts_dict


# Generated at 2022-06-13 03:26:49.553380
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():

    # unit test execution without selinux Python library
    with_selinux = SelinuxFactCollector()
    with_selinux_data = with_selinux.collect()
    assert isinstance(with_selinux_data, dict)
    assert 'selinux' in with_selinux_data
    assert with_selinux_data['selinux_python_present'] == False

# Generated at 2022-06-13 03:26:52.270933
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    '''Unit test constructor of class SelinuxFactCollector.'''
    selinuxCollector = SelinuxFactCollector()
    assert selinuxCollector.name == 'selinux'
    assert selinuxCollector._fact_ids == set()

# Generated at 2022-06-13 03:26:55.391263
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    SelinuxFactCollector_collect = SelinuxFactCollector()
    facts_dict = SelinuxFactCollector_collect.collect()
    assert facts_dict['selinux']['status'] == 'enabled'
    assert facts_dict['selinux']['mode'] == 'enforcing'

# Generated at 2022-06-13 03:27:39.072923
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    s = SelinuxFactCollector()
    f = s.collect()
    assert s.name == 'selinux'
    assert 'selinux' in f
    assert 'selinux_python_present' in f
    assert 'status' in f['selinux']
    assert 'policyvers' in f['selinux']
    assert 'config_mode' in f['selinux']
    assert 'mode' in f['selinux']
    assert 'type' in f['selinux']

# Generated at 2022-06-13 03:27:44.973438
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.name == 'selinux'
    assert selinux_fact_collector.priority == BaseFactCollector.DEFAULT_PRIORITY + 3
    assert selinux_fact_collector._fact_ids == set(['selinux', 'selinux_python_present'])


# Generated at 2022-06-13 03:27:53.375196
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    collector = SelinuxFactCollector()
    facts_dict = collector.collect()
    assert 'selinux' in facts_dict
    assert 'selinux_python_present' in facts_dict
    assert 'status' in facts_dict['selinux']
    assert 'mode' in facts_dict['selinux']
    assert 'type' in facts_dict['selinux']
    assert 'config_mode' in facts_dict['selinux']
    assert 'policyvers' in facts_dict['selinux']
    assert facts_dict['selinux_python_present'] == False or facts_dict['selinux_python_present'] == True
    assert facts_dict['selinux']['status'] in ['disabled', 'enabled']

# Generated at 2022-06-13 03:27:57.426096
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.name == 'selinux'
    assert selinux_fact_collector.collect() == {'selinux': {'status': 'Missing selinux Python library'}, 'selinux_python_present': False}

# Generated at 2022-06-13 03:28:08.352056
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    fake_selinux_status = {
        'status': 'Missing selinux Python library',
        'selinux_python_present': False
    }

    fake_selinux_enabled_status = {
        'config_mode': 'enforcing',
        'status': 'enabled',
        'mode': 'permissive',
        'policyvers': '28',
        'type': 'targeted',
        'selinux_python_present': True
    }

    selinux_collector = SelinuxFactCollector()
    selinux_status = selinux_collector.collect()

    assert selinux_status == fake_selinux_status

    selinux.is_selinux_enabled = lambda : True
    selinux.selinux_getenforcemode = lambda : (0,1)
    selinux.security

# Generated at 2022-06-13 03:28:10.038136
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.name == 'selinux'

# Generated at 2022-06-13 03:28:11.145061
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    test_obj = SelinuxFactCollector()
    test_obj.collect()

# Generated at 2022-06-13 03:28:12.748682
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    obj = SelinuxFactCollector()
    assert obj.name == "selinux"
    assert obj._fact_ids == set()

# Generated at 2022-06-13 03:28:13.515813
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    SelinuxFactCollector()

# Generated at 2022-06-13 03:28:18.081622
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    import doctest
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts import collector

    SelinuxCollector = collector.get_collector('SelinuxFactCollector')

    assert SelinuxCollector is not None, 'Could not load SELinuxFactCollector'

    print("Testing basic collection")
    c = SelinuxCollector()
    assert isinstance(c, BaseFactCollector)

    # Basic test;
    # Skipped as we do not want to expose the complete fact list to be public
    # assert c.collect() == {'selinux':  }


# Generated at 2022-06-13 03:30:04.874237
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector.selinux import SelinuxFactCollector
    import mock
    import selinux

    selinux.is_selinux_enabled = mock.MagicMock()
    selinux.is_selinux_enabled.return_value = True
    selinux.security_policyvers = mock.MagicMock()
    selinux.security_policyvers.return_value = 17
    selinux.selinux_getenforcemode = mock.MagicMock()
    selinux.selinux_getenforcemode.return_value = (0, 0)
    selinux.security_getenforce = mock.MagicMock()
    selinux.security_getenforce.return_value = 0
    se

# Generated at 2022-06-13 03:30:07.956524
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_facts = SelinuxFactCollector()
    assert selinux_facts != None
    assert selinux_facts.name == 'selinux'

# Generated at 2022-06-13 03:30:11.482792
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_obj = SelinuxFactCollector()
    assert selinux_obj.name == 'selinux'
    assert type(selinux_obj._fact_ids) == set

# Generated at 2022-06-13 03:30:15.833898
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.collector.selinux import SelinuxFactCollector
    from ansible.module_utils.facts.collector.generic import GenericFactCollector

    # Initialize all available collectors
    collectors = [SelinuxFactCollector()]

    # Initialize Collector object
    fact_collector = Collector(collectors)

    # Call collect method of Collector
    all_facts = fact_collector.collect(module=None, collected_facts=None)

    # Test if all available collectors were called
    assert len(all_facts) == 1

    # Test if all facts were collected
    assert 'selinux' in all_facts

    # Test if all selinux facts were collected

# Generated at 2022-06-13 03:30:19.901614
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    facts_dict = dict()
    obj = SelinuxFactCollector(facts_dict)
    assert obj.name == 'selinux'
    assert obj._fact_ids == set(['selinux'])

# Generated at 2022-06-13 03:30:22.282913
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_facts = SelinuxFactCollector()
    assert selinux_facts
    assert selinux_facts.name == 'selinux'

# Generated at 2022-06-13 03:30:25.404728
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    """
    Constructor of SelinuxFactCollector should create an instance of SelinuxFactCollector
    """
    selinux_collector = SelinuxFactCollector()
    assert isinstance(selinux_collector, SelinuxFactCollector)

# Generated at 2022-06-13 03:30:27.416009
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_facts = SelinuxFactCollector()
    assert selinux_facts.name == 'selinux'
    assert selinux_facts._fact_ids == set()


# Generated at 2022-06-13 03:30:29.304140
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_collector = SelinuxFactCollector()
    assert selinux_collector.name == 'selinux'
    assert selinux_collector._fact_ids == set()

# Generated at 2022-06-13 03:30:31.192195
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.name == 'selinux'