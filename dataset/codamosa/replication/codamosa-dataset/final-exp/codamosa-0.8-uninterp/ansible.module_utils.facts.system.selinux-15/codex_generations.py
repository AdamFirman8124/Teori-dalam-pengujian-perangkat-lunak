

# Generated at 2022-06-13 03:22:55.812908
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    # Assert that instance of SelinuxFactCollector is created
    assert SelinuxFactCollector()

# Generated at 2022-06-13 03:22:58.960453
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    """Unit test for constructor of class SelinuxFactCollector"""
    x = SelinuxFactCollector()
    assert x.name == 'selinux'
    assert x._fact_ids == set()


# Generated at 2022-06-13 03:23:11.193864
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    m = mock.MagicMock()
    m.is_selinux_enabled.return_value = True
    m.security_getenforce.return_value = 1
    m.security_policyvers.return_value = '28'
    m.selinux_getenforcemode.return_value = (0,1)
    m.selinux_getpolicytype.return_value = (0,'targeted')
    selinux.is_selinux_enabled = m.is_selinux_enabled
    selinux.security_getenforce = m.security_getenforce
    selinux.security_policyvers = m.security_policyvers
    selinux.selinux_getenforcemode = m.selinux_getenforcemode
    selinux.selinux_getpolicytype = m.selinux

# Generated at 2022-06-13 03:23:13.232649
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector is not None

# Generated at 2022-06-13 03:23:16.626809
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    obj = SelinuxFactCollector()
    actual_result = obj.collect()
    assert actual_result['selinux']['status'] == 'enabled' \
        or actual_result['selinux']['status'] == 'Missing selinux Python library'

# Generated at 2022-06-13 03:23:18.213388
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux = SelinuxFactCollector()
    selinux.collect()

# Generated at 2022-06-13 03:23:20.490346
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    SelinuxFactCollector = SelinuxFactCollector()
    assert SelinuxFactCollector.name == 'selinux'

# Generated at 2022-06-13 03:23:27.602274
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():

    # Create an instance of SelinuxFactCollector
    selinux_fact_collector = SelinuxFactCollector()

    # Set flag indicating no selinux Python library
    selinux_fact_collector.module_prereqs_installed = False

    # Collect facts
    _facts_dict = selinux_fact_collector.collect()

    # Test properties of selinux fact
    assert 'selinux_python_present' in _facts_dict
    assert _facts_dict['selinux_python_present'] == False

    assert 'selinux' in _facts_dict
    assert 'status' in _facts_dict['selinux']
    assert _facts_dict['selinux']['status'] == 'Missing selinux Python library'

    # Set flag indicating selinux Python library is present
    selinux_fact_collector

# Generated at 2022-06-13 03:23:30.409859
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.name == 'selinux'
    assert selinux_fact_collector._fact_ids == set()


# Generated at 2022-06-13 03:23:32.092723
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    collector = SelinuxFactCollector()
    assert collector.name == "selinux"
    assert collector._fact_ids == set()

# Generated at 2022-06-13 03:23:44.612954
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    fc = SelinuxFactCollector()
    assert fc.name == 'selinux'
    assert fc._fact_ids == set()
    assert fc._platform == 'Generic'
    assert fc._file_paths == []
    assert fc._package_mgr is None

# Generated at 2022-06-13 03:23:47.943807
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
   obj = SelinuxFactCollector()
   assert obj.name == "selinux"
   assert obj._fact_ids == set(['selinux'])

# Generated at 2022-06-13 03:23:50.416719
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    s = SelinuxFactCollector()
    assert s.name == 'selinux'
    assert s._fact_ids is not None

# Generated at 2022-06-13 03:23:53.860869
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector
    assert selinux_fact_collector.name == 'selinux'
    assert selinux_fact_collector._fact_ids == set()

# Generated at 2022-06-13 03:23:55.336620
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    assert SelinuxFactCollector.name == 'selinux'

# Generated at 2022-06-13 03:24:04.282302
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    module = None
    collected_facts = None
    sfc = SelinuxFactCollector()

    facts_dict = sfc.collect(module=module, collected_facts=collected_facts)
    assert 'selinux' in facts_dict
    assert 'status' in facts_dict['selinux']
    assert 'config_mode' in facts_dict['selinux']
    assert 'mode' in facts_dict['selinux']
    assert 'type' in facts_dict['selinux']
    assert 'policyvers' in facts_dict['selinux']
    assert 'selinux_python_present' in facts_dict

# Generated at 2022-06-13 03:24:13.634138
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    class MockModule(object):
        def __init__(self):
            self.params = {}

        def fail_json(self, *args, **kwargs):
            assert False, 'fail_json called with {0} and {1}'.format(args, kwargs)

    class MockSelinuxModule(object):
        def __init__(self):
            self.selinux_getenforcemode = Mock(return_value=(0, 0))
            self.selinux_getpolicytype = Mock(return_value=(0, 'targeted'))
            self.security_getenforce = Mock(return_value=0)
            self.is_selinux_enabled = Mock(return_value=True)
            self.security_policyvers = Mock(return_value=20180531)

    selinux_module = Mock

# Generated at 2022-06-13 03:24:23.080802
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    '''Unit test for method collect of class SelinuxFactCollector'''
    # If HAVE_SELINUX is set, check selinux_python_present and check selinux.status
    if HAVE_SELINUX:
        selinux_facts = SelinuxFactCollector().collect()
        assert selinux_facts is not None
        assert 'selinux' in selinux_facts
        assert 'selinux_python_present' in selinux_facts
        assert selinux_facts['selinux_python_present']

        assert 'status' in selinux_facts['selinux']
        if selinux.is_selinux_enabled():
            # If selinux is enabled, check mode, config_mode and type
            assert selinux_facts['selinux']['status'] == 'enabled'
            assert 'mode'

# Generated at 2022-06-13 03:24:24.486076
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_collector = SelinuxFactCollector()
    assert selinux_collector.name == 'selinux'

# Generated at 2022-06-13 03:24:35.557125
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    from ansible.module_utils import basic
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collectors.selinux import SelinuxFactCollector

    selinux_fact_collector = SelinuxFactCollector(BaseFactCollector)

    # Object test
    assert isinstance(selinux_fact_collector, SelinuxFactCollector)
    assert isinstance(selinux_fact_collector, BaseFactCollector)
    assert isinstance(selinux_fact_collector, collector.BaseFactCollector)

    # Testing attributes
    assert hasattr(selinux_fact_collector, 'collect')
    assert hasattr(selinux_fact_collector, 'name')

# Generated at 2022-06-13 03:24:51.052120
# Unit test for method collect of class SelinuxFactCollector

# Generated at 2022-06-13 03:24:52.217934
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    obj = SelinuxFactCollector()
    return obj

# Generated at 2022-06-13 03:25:04.637616
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    '''Unit test method collect of class SelinuxFactCollector'''
    #pylint: disable=protected-access

    # Test the selinux collector with the selinux Python library missing
    # (HAVE_SELINUX = False)
    collector = SelinuxFactCollector()
    collector._collect_from_module = lambda *args, **kwargs: {}   #pylint: disable=protected-access
    collector._collect_from_facts = lambda *args, **kwargs: {}    #pylint: disable=protected-access
    facts_dict = collector.collect()
    assert facts_dict['selinux'] == {'status': 'Missing selinux Python library'}
    assert facts_dict['selinux_python_present'] is False

    #if HAVE_SELINUX:
    #    # TODO:

# Generated at 2022-06-13 03:25:07.994102
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.name == 'selinux'
    assert selinux_fact_collector._fact_ids == set()


# Generated at 2022-06-13 03:25:11.208667
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    doc = SelinuxFactCollector.collect.__doc__
    assert doc == "Collect facts related to selinux"

# Generated at 2022-06-13 03:25:17.365732
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    obj = SelinuxFactCollector()
    assert isinstance(obj, object) == True
    assert isinstance(obj.name, object) == True
    assert isinstance(obj.collect, object) == True
    assert obj.name == 'selinux'
    assert obj.collect()['selinux']['status'] == 'Missing selinux Python library'
    assert obj.collect()['selinux_python_present'] == False


# Generated at 2022-06-13 03:25:18.987617
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_collector = SelinuxFactCollector()
    assert selinux_collector.name == 'selinux'
    assert selinux_collector._fact_ids == set()

# Generated at 2022-06-13 03:25:21.180803
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    collector = SelinuxFactCollector()
    facts = collector.collect()
    assert 'selinux' in facts
    assert 'selinux_python_present' in facts

# Generated at 2022-06-13 03:25:26.640209
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    assert SelinuxFactCollector.name == 'selinux'
    assert SelinuxFactCollector._fact_ids == set()
    assert SelinuxFactCollector.collect(collected_facts=None)['selinux']['status'] == 'disabled'

# Generated at 2022-06-13 03:25:30.321364
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector is not None
    assert selinux_fact_collector.name == 'selinux'

# Generated at 2022-06-13 03:25:52.852142
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():

    sfc = SelinuxFactCollector()
    assert sfc.name == 'selinux'
    assert sfc._fact_ids == set()

    assert sfc._collector_data is None
    assert isinstance(sfc.collect(), dict)

# Generated at 2022-06-13 03:25:54.415460
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    fact = SelinuxFactCollector()
    assert fact


# Generated at 2022-06-13 03:26:02.592078
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    import sys

    # Remove selinux library temporarily so fact collector reports
    # that it is not present
    if 'selinux' in sys.modules:
        del sys.modules['selinux']

    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.name == 'selinux'
    assert len(selinux_fact_collector._fact_ids) == 0

    # Restore selinux library
    if 'selinux' not in sys.modules:
        import selinux

    # Remove selinux library temporarily so fact collector reports
    # that it is not present
    if 'selinux' in sys.modules:
        del sys.modules['selinux']

    selinux_fact_collector.collect()

# Generated at 2022-06-13 03:26:03.719911
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    c = SelinuxFactCollector()
    assert c.name == 'selinux'

# Generated at 2022-06-13 03:26:05.481531
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    sfc = SelinuxFactCollector()
    assert sfc is not None


# Generated at 2022-06-13 03:26:08.515820
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()

    assert selinux_fact_collector.name == 'selinux'
    assert selinux_fact_collector._fact_ids == set()


# Generated at 2022-06-13 03:26:10.388788
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    print("Testing SelinuxFactCollector")


if __name__ == '__main__':
    test_SelinuxFactCollector_collect()

# Generated at 2022-06-13 03:26:11.263843
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    assert SelinuxFactCollector.collect({})

# Generated at 2022-06-13 03:26:13.511462
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():

    collector = SelinuxFactCollector()
    selinux_facts = collector.collect()
    assert selinux_facts['selinux_python_present'] is True

# Generated at 2022-06-13 03:26:21.815279
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes, to_native

    testmodule_path = basic._ANSIBLE_TEST_DATA_ROOT + '/unit/modules/basic.py'
    testmodule_args = 'test=test arg'
    module_name = 'basic'

    facts_dict = SelinuxFactCollector().collect(module_name=module_name,
                                                collected_facts=None)

    assert facts_dict['selinux_python_present'] is True
    assert facts_dict['selinux']['status'] == 'enabled'

# Generated at 2022-06-13 03:27:05.923819
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():

    from ansible.module_utils.facts.collector.selinux import SelinuxFactCollector
    from ansible.module_utils.facts.collector.system import SystemFactCollector

    from ansible.module_utils.facts import timeout

    collected_facts = {}

    # If selinux library is missing, only set the status and selinux_python_present since
    # there is no way to tell if SELinux is enabled or disabled on the system
    # without the library.
    selinux_fact_collector = SelinuxFactCollector(timeout=timeout.Timeout())
    collected_facts = selinux_fact_collector.collect(collected_facts=collected_facts)
    selinux_facts = collected_facts.get('selinux')

    assert selinux_facts['status'] == 'Missing selinux Python library'

# Generated at 2022-06-13 03:27:11.884907
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_collector = SelinuxFactCollector()
    assert selinux_collector.name == 'selinux'
    assert len(selinux_collector.criteria()) == 0
    assert selinux_collector._fact_ids == set()

# Generated at 2022-06-13 03:27:13.661219
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    collector = SelinuxFactCollector()
    facts_dict = collector.collect(collected_facts={})
    selinux_facts = facts_dict.get('selinux', {})
    assert selinux_facts == {'config_mode': 'unknown', 'policyvers': 'unknown', 'mode': 'unknown', 'status': 'enabled', 'type': 'unknown'}

# Generated at 2022-06-13 03:27:15.449674
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact = SelinuxFactCollector()
    assert selinux_fact.name == 'selinux'

# Generated at 2022-06-13 03:27:27.551525
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    """Test SelinuxFactCollector.collect()"""
    # Test with selinux_python_present == True and selinux == 'enabled'
    #
    # starting with selinux_python_present == True
    selinux_python_present = True

    # selinux is 'enabled'
    selinux_enabled = True

    m = mock.mock_module.MockModule()
    m.is_selinux_enabled.return_value = selinux_enabled
    m.security_policyvers.return_value = '29'
    m.selinux_getenforcemode.return_value = (0, 1)
    m.security_getenforce.return_value = 1
    m.selinux_getpolicytype.return_value = (0, 'targeted')

# Generated at 2022-06-13 03:27:30.801965
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_fact_collector_instance = SelinuxFactCollector()
    test_module = None
    test_collected_facts = None
    test_facts_dict = selinux_fact_collector_instance.collect(test_module, test_collected_facts)
    assert test_facts_dict

# Generated at 2022-06-13 03:27:34.865714
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector is not None
    assert selinux_fact_collector.name == 'selinux'

# Generated at 2022-06-13 03:27:36.147004
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    actual_result = SelinuxFactCollector()
    assert actual_result != None

# Generated at 2022-06-13 03:27:46.555141
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():

    # Test when the selinux library is not present

    module = mock.Mock()
    ansible_module = mock.Mock()

    # ImportError will be raised when trying to import selinux
    selinux = mock.Mock()
    selinux.side_effect = ImportError
    # Since the selinux library is missing, is_selinux_enabled will always return False
    selinux.is_selinux_enabled.return_value = False
    selinux.security_policyvers.return_value = '3.12.1'

    sys.modules['selinux'] = selinux

    collected_facts = {}
    selinux_fact_collector = SelinuxFactCollector()
    result = selinux_fact_collector.collect()


# Generated at 2022-06-13 03:27:51.208414
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    assert not HAS_SELINUX
    obj = SelinuxFactCollector()
    assert obj is not None
    assert obj.name == 'selinux'
    assert obj._fact_ids == set()
    assert set(obj.collect().keys()) == set(['selinux', 'selinux_python_present'])
    assert 'status' in obj.collect()['selinux']


# Generated at 2022-06-13 03:29:27.673758
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector

# Generated at 2022-06-13 03:29:30.240262
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    collector = SelinuxFactCollector()
    assert collector.name == 'selinux'
    assert collector.collect() == {'selinux':
                                   {'status': 'Missing selinux Python library'},
                                   'selinux_python_present': False}

# Generated at 2022-06-13 03:29:31.805220
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    g = SelinuxFactCollector()
    assert g.name == 'selinux'

# Generated at 2022-06-13 03:29:35.021649
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.name == 'selinux'


# Generated at 2022-06-13 03:29:36.441907
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    assert(SelinuxFactCollector.name == 'selinux')

# Generated at 2022-06-13 03:29:46.981239
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # For testing purpose, we will mock camelCase method to lowercase.
    # https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect
    def mock_is_selinux_enabled():
        return True

    # The mocked methods
    selinux.is_selinux_enabled = mock_is_selinux_enabled

    selinux_collector = SelinuxFactCollector()

    # Collected facts should be a hash
    assert isinstance(selinux_collector.collect(), dict)

    # Collected facts should have a selinux sub hash
    assert isinstance(selinux_collector.collect().get('selinux'), dict)

    # Collected facts should have a boolean

# Generated at 2022-06-13 03:29:48.354979
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    r = SelinuxFactCollector()
    assert r.name == 'selinux'

# Generated at 2022-06-13 03:29:50.320671
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_collector = SelinuxFactCollector()
    assert(selinux_collector.name == 'selinux')

# Generated at 2022-06-13 03:29:52.114252
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_output = SelinuxFactCollector()
    assert 'selinux' in selinux_output.get_facts()

# Generated at 2022-06-13 03:30:04.252630
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():

    # selinux.is_selinux_enabled() returns False if SELinux is not enabled or
    # config mode is disabled. This test tests the collection when
    # selinux.is_selinux_enabled() returns False.
    selinux.is_selinux_enabled = lambda: False
    selinux_fact_collector = SelinuxFactCollector()
    selinux_facts = selinux_fact_collector.collect()
    assert selinux_facts == {
        'selinux': {
            'status': 'disabled'
        },
        'selinux_python_present': True
    }

    # selinux.is_selinux_enabled() returns True if SELinux is enabled. This test
    # tests the collection when selinux.is_selinux_enabled() returns True.
    selinux