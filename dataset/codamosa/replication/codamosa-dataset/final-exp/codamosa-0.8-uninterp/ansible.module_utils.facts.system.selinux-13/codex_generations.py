

# Generated at 2022-06-13 03:22:59.907416
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinuxFact = SelinuxFactCollector()
    assert selinuxFact.name == 'selinux'

    facts_dict = selinuxFact.collect()
    assert 'selinux' in facts_dict
    assert 'selinux_python_present' in facts_dict

    for fact, value in facts_dict['selinux'].items():
        assert fact in ('status', 'mode', 'type', 'config_mode', 'policyvers')

# Generated at 2022-06-13 03:23:01.323349
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    assert isinstance(SelinuxFactCollector(), BaseFactCollector)

# Generated at 2022-06-13 03:23:12.861225
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils import basic
    import os

    selinux_facts = SelinuxFactCollector()
    assert isinstance(selinux_facts, BaseFactCollector)

    # Test the collect method
    if os.geteuid() != 0:
        # Not root, so selinux.is_selinux_enabled() will throw an OSError since
        # the /selinux/enforce file is not readable.
        try:
            selinux_facts.collect()
        except:
            pass
        else:
            assert False, 'Expected OSError not raised'

# Generated at 2022-06-13 03:23:15.765340
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()

    assert selinux_fact_collector.name == 'selinux'
    assert selinux_fact_collector._fact_ids == set()

# Generated at 2022-06-13 03:23:24.896823
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # Create a SelinuxFactCollector object.
    SelinuxFactCollector_obj = SelinuxFactCollector()

    # Create a dictionary that contains fake data for selinux facts.
    fake_selinux_facts = {
        'selinux_python_present': True,
        'selinux': {
            'mode': 'disabled',
            'config_mode': 'disabled',
            'type': 'targeted',
            'status': 'enabled',
            'policyvers': '28'
        }
    }

    # Create a dictionary that contains the fake module argument.
    fake_module_arg = {
        'check_mode': False
    }

    # Save the value of HAVE_SELINUX before we change it.
    prev_HAVE_SELINUX = HAVE_SELINUX

    #

# Generated at 2022-06-13 03:23:26.529125
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    objSelPolCol = SelinuxFactCollector()
    assert isinstance(objSelPolCol, SelinuxFactCollector)


# Generated at 2022-06-13 03:23:32.390055
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    """
    Test the collect method of SelinuxFactCollector.
    """
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.collector.selinux import SelinuxFactCollector

    # Create an instance of the SelinuxFactCollector class.
    selinux_collector = SelinuxFactCollector()

    # Create a "fake" module object
    module = type('module', (object,), {'params': {'gather_subset': ['all']}})()

    # Create an instance of the AnsibleModuleMock class.
    amm = AnsibleModuleMock(module_utils=mock.MagicMock())

    # Mock the Selinux fact collector method

# Generated at 2022-06-13 03:23:35.836684
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    collector = SelinuxFactCollector()
    facts = collector.collect()
    assert 'selinux' in facts

# Generated at 2022-06-13 03:23:45.769623
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():

    # Create a fake module to be used by the facts module
    import ansible.module_utils.facts.collector
    fake_module = ansible.module_utils.facts.collector.AnsibleFakeModule(
        selinux_python_present=True,
        status='enabled',
        mode='enforcing',
        policyvers=28,
        config_mode='enforcing',
        type='targeted'
    )

    # Create an instance of the SelinuxFactCollector class
    selinux_collector = SelinuxFactCollector()

    # Create a dictionary containing the facts collected by the SelinuxFactCollector class
    facts_dict = selinux_collector.collect(module=fake_module, collected_facts={})

    # Check if the values returned by the method match the expected values

# Generated at 2022-06-13 03:23:46.780657
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    SelinuxFactCollector()

# Generated at 2022-06-13 03:24:06.874322
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    from ansible.module_utils.facts import collector
    import ansible.module_utils.facts.collector
    collector.collectors.pop(ansible.module_utils.facts.collector.SelinuxFactCollector.name, None)
    collector.collectors.pop('selinux', None)
    selinux_collector = ansible.module_utils.facts.collector.SelinuxFactCollector('ansible.module_utils.facts.collector')

    # Testing case with selinux Python library present
    selinux_collector.HAVE_SELINUX = True
    import mock

# Generated at 2022-06-13 03:24:15.844277
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_collector = SelinuxFactCollector()

    # Test with no library loaded, so no selinux_python_present fact
    # and status set to Missing selinux Python library
    selinux_facts = selinux_collector.collect(collected_facts=dict())
    assert not selinux_facts['selinux_python_present']
    assert selinux_facts['selinux']['status'] == 'Missing selinux Python library'

    # Test with library loaded, so set selinux_python_present fact
    # and status set to enabled and other related facts
    selinux_facts = selinux_collector.collect(collected_facts=dict())
    assert selinux_facts['selinux_python_present']
    assert selinux_facts['selinux']['status'] == 'enabled'
    assert selinux

# Generated at 2022-06-13 03:24:22.918140
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    initial_object_length = len(SelinuxFactCollector().collect())

    selinux_fact_collector = SelinuxFactCollector()
    result = selinux_fact_collector.collect()

    assert len(result) == initial_object_length + 2
    assert 'selinux' in result
    assert result['selinux']['config_mode'] == 'enforcing'
    assert result['selinux']['mode'] == 'enforcing'
    assert result['selinux']['status'] == 'enabled'
    assert result['selinux']['type'] == 'targeted'

# Generated at 2022-06-13 03:24:24.496989
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux = SelinuxFactCollector()
    assert selinux
    assert selinux.name == 'selinux'

# Generated at 2022-06-13 03:24:26.660509
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fc = SelinuxFactCollector()
    assert selinux_fc.name == 'selinux'
    assert selinux_fc._fact_ids is not None

# Generated at 2022-06-13 03:24:37.550270
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():

    # If the selinux library is not present, the only facts in the dictionary should be status
    # and selinux_python_present
    selinux_fact_collector = SelinuxFactCollector(None)
    if not HAVE_SELINUX:
        assert selinux_fact_collector.collect().keys() == {'selinux', 'selinux_python_present'}
        assert selinux_fact_collector.collect()['selinux'].keys() == {'status'}
    else:
        assert selenium_fact_collector.collect().keys() == {'selinux', 'selinux_python_present'}
        assert selenium_fact_collector.collect()['selinux'].keys() == {'status', 'policyvers', 'mode', 'config_mode', 'type'}

# Generated at 2022-06-13 03:24:47.083095
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_module_mock = type('selinux', (), {
        'is_selinux_enabled': lambda: True,
        'security_policyvers': lambda: 1,
        'selinux_getenforcemode': lambda: (0,1),
        'security_getenforce': lambda: 1,
        'selinux_getpolicytype': lambda: (0,'policy')
    })
    selinux_mock = type('selinux', (), { 'selinux': selinux_module_mock })
    collector = SelinuxFactCollector()
    collected_facts = collector.collect(selinux=selinux_mock)
    # Check the facts

# Generated at 2022-06-13 03:24:49.908452
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # Set expected values
    expected_result = {
        'selinux': {
            'status': 'disabled'
        },
        'selinux_python_present': False
    }
    fact_collector = SelinuxFactCollector()
    facts_dict = fact_collector.collect()
    assert facts_dict == expected_result

# Generated at 2022-06-13 03:25:02.212286
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    Sel = SelinuxFactCollector()
    selinux_facts = Sel.collect()
    # selinux_facts will contain selinux_python_present and will have
    # value true if selinux python library is present.
    if selinux_facts['selinux_python_present']:
        assert 'status' in selinux_facts['selinux']
        assert 'policyvers' in selinux_facts['selinux']
        assert 'config_mode' in selinux_facts['selinux']
        assert 'type' in selinux_facts['selinux']
        assert 'mode' in selinux_facts['selinux']
    else:
        assert 'status' in selinux_facts['selinux']
        assert selinux_facts['selinux'] == 'Missing selinux python library'

# Generated at 2022-06-13 03:25:04.110828
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    """Test SelinuxFactCollector.collect()
    """
    # Placeholder for testing method collect of class SelinuxFactCollector

# Generated at 2022-06-13 03:25:13.524083
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    pass

# Generated at 2022-06-13 03:25:16.636665
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_collector = SelinuxFactCollector()
    assert 'selinux' == selinux_collector.name
    assert 'selinux_python_present' in selinux_collector._fact_ids

# Generated at 2022-06-13 03:25:25.923859
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_fact_collector = SelinuxFactCollector()
    # If the selinux Python library is missing, collect should return True
    if not HAVE_SELINUX:
        result = selinux_fact_collector.collect()
    else:
        result = selinux_fact_collector.collect()
    assert result
    assert 'selinux' in result

    selinux = result['selinux']
    assert 'status' in selinux
    assert 'python_present' in result
    assert selinux['python_present'] == False

    if selinux['status'] == 'enabled':
        assert 'policyvers' in selinux
        assert 'config_mode' in selinux
        assert 'mode' in selinux
        assert 'type' in selinux

# Generated at 2022-06-13 03:25:29.592203
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    """ Test case to validate the constructor of class SelinuxFactCollector """
    assert SelinuxFactCollector.name == 'selinux'
    assert len(SelinuxFactCollector._fact_ids) == 0

# Generated at 2022-06-13 03:25:37.155059
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    # Proper instantiation
    selinux_col = SelinuxFactCollector()
    assert selinux_col.name == 'selinux'
    assert selinux_col._fact_ids == set()

    # Selinux library is missing, set the status field to 'Missing selinux Python library'
    selinux_col._HAVE_SELINUX = False
    assert selinux_col.collect()['selinux']['status'] == 'Missing selinux Python library'
    assert selinux_col.collect()['selinux_python_present'] == False
    selinux_col._HAVE_SELINUX = True

# Generated at 2022-06-13 03:25:47.999696
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    """
    Test for SelinuxFactCollector.collect
    """
    import os
    import sys

    # Mock the system under test
    from ansible.module_utils.facts.collector import BaseFactCollector
    base = BaseFactCollector

    # Initialize the Test object
    test_obj = SelinuxFactCollector()

    # Test the failure case
    if sys.version_info[0] > 2:
        # mock selinux library
        module_mock = mock.MagicMock()
        selinux_mock = mock.MagicMock()
        selinux_mock.is_selinux_enabled.return_value = False
        module_mock.selinux = selinux_mock
        test_obj.collect(module_mock)

# Generated at 2022-06-13 03:25:52.394620
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_fact = SelinuxFactCollector()
    selinux_fact.collect()
    assert 'selinux' in selinux_fact.get_facts()

# Generated at 2022-06-13 03:26:01.582234
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    try:
        import selinux
        HAVE_SELINUX = True
    except ImportError:
        HAVE_SELINUX = False

    # Mock the module
    class MockModule(object):
        pass

    TEST_COLLECTED_FACTS = {'selinux': {'status': 'disabled'}}
    TEST_COLLECTED_FACTS_WITH_SELINUX = {'selinux': {'status': 'enabled', 'policyvers': 'testing',
                                                     'config_mode': 'testing', 'mode': 'testing',
                                                     'type': 'testing'}}
    TEST_COLLECTED_FACTS_WITH_SELINUX_PYTHON_PRESENT = {'selinux_python_present': True}
    TEST_COLLECTED_FACTS_W

# Generated at 2022-06-13 03:26:04.928066
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    collector = SelinuxFactCollector()
    assert(collector.name == 'selinux')
    assert(set(collector._fact_ids) == set(['selinux', 'selinux_python_present']))

# Generated at 2022-06-13 03:26:07.920910
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():

    fact_collector = SelinuxFactCollector()
    selinux_fact = fact_collector.collect()

    assert 'selinux' in selinux_fact
    assert 'status' in selinux_fact['selinux']

# Generated at 2022-06-13 03:26:25.283173
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # Disable selinux for unit testing
    selinux.is_selinux_enabled = lambda: False
    # Create a SelinuxFactCollector instance
    selinux_collector = SelinuxFactCollector()
    # Test collect method
    selinux_facts = selinux_collector.collect()
    assert selinux_facts['selinux'] == {'status': 'disabled'}

    # Enable selinux for unit testing
    selinux.is_selinux_enabled = lambda: True
    # Set mocks for the selinux functions
    selinux.security_policyvers = lambda : '3'
    selinux.selinux_getenforcemode = lambda : (0, 1)
    selinux.security_getenforce = lambda : 1

# Generated at 2022-06-13 03:26:26.776534
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    my_obj = SelinuxFactCollector()
    assert my_obj.name == 'selinux'
    assert not my_obj._fact_ids

# Generated at 2022-06-13 03:26:32.922249
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # In this unit test, we can't test the functionality of the
    # collect() method since we need the selinux Python library
    # installed to test it. Here we just test that the fact
    # collector class is successfully created and that the
    # collect() method does not raise an exception.
    selinux_fact_collector = SelinuxFactCollector()
    selinux_fact_collector.collect()

# Generated at 2022-06-13 03:26:37.333492
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    unit_test = {}
    module_collector = SelinuxFactCollector()
    unit_test['name'] = "selinux"
    unit_test['collected_facts'] = module_collector.collect()
    return unit_test

# Generated at 2022-06-13 03:26:39.685664
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    fact_collector = SelinuxFactCollector()
    assert fact_collector.name == 'selinux'



# Generated at 2022-06-13 03:26:42.681019
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    c = SelinuxFactCollector()
    assert c.collect() == {
        "selinux": {
            "status": "Missing selinux Python library"
        }
    }

# Generated at 2022-06-13 03:26:43.998699
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    obj = SelinuxFactCollector()
    assert obj

# Generated at 2022-06-13 03:26:51.985167
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    fact_collector = SelinuxFactCollector()
    facts = fact_collector.collect()
    assert 'selinux' in facts
    assert 'status' in facts['selinux']
    assert facts['selinux_python_present'] == HAVE_SELINUX
    if facts['selinux_python_present']:
        assert facts['selinux']['status'] == 'disabled' or facts['selinux']['status'] == 'enabled'
        assert 'policyvers' in facts['selinux']
        assert 'config_mode' in facts['selinux']
        assert 'mode' in facts['selinux']
        assert 'type' in facts['selinux']

# Generated at 2022-06-13 03:26:53.510294
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    se = SelinuxFactCollector()
    assert se.name == 'selinux'
    assert len(se._fact_ids) == 0

# Generated at 2022-06-13 03:27:04.045870
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    def mock_selinux_getenforcemode():
        return 0, 0
    selinux.selinux_getenforcemode = mock_selinux_getenforcemode

    def mock_selinux_getpolicytype():
        return 0, 'MLS'
    selinux.selinux_getpolicytype = mock_selinux_getpolicytype

    fake_selinux_fact_collector = SelinuxFactCollector()

    def mock_call_module_func(module, *args, **kwargs):
        return {"stderr": "", "rc": 0}
    fake_selinux_fact_collector._call_module_func = mock_call_module_func


# Generated at 2022-06-13 03:27:25.219913
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinuxcollector = SelinuxFactCollector()
    assert selinuxcollector.collect() == {'selinux': {'status': 'Missing selinux Python library'}, 'selinux_python_present': False}

# Generated at 2022-06-13 03:27:27.448390
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    """Test the collect method of the SelinuxFactCollector."""

    pass

# Generated at 2022-06-13 03:27:29.581916
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    module = AnsibleModuleMock()
    fact_collector = SelinuxFactCollector()
    assert fact_collector.name == "selinux"
    assert fact_collector.collect(module) is not None


# Generated at 2022-06-13 03:27:33.411111
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact = SelinuxFactCollector()
    assert selinux_fact.name == 'selinux'
    assert 'selinux' in selinux_fact._fact_ids

# Generated at 2022-06-13 03:27:40.249076
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    # Test with selinux module present
    globals()['HAVE_SELINUX'] = True
    assert SelinuxFactCollector._fact_ids == set()
    sfc = SelinuxFactCollector()
    sfc_fact_ids = set(sfc._fact_ids)
    assert sfc_fact_ids == set(['selinux', 'selinux_python_present'])
    assert len(sfc_fact_ids) == 2
    assert sfc.name == 'selinux'


# Generated at 2022-06-13 03:27:43.720162
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    """Test that we correctly return a dictionary containing the
       selinux facts
    """
    set_module_args({})
    result = SelinuxFactCollector().collect()
    assert 'selinux' in result

# Generated at 2022-06-13 03:27:45.861113
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    collector = SelinuxFactCollector()
    assert collector._fact_ids == set()
    assert collector.name == 'selinux'

# Generated at 2022-06-13 03:27:53.893991
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    def mock_is_selinux_enabled(*args, **kwargs):
        return True

    def mock_selinux_getenforcemode(*args, **kwargs):
        return (0, 1)

    def mock_selinux_getpolicytype(*args, **kwargs):
        return (0, 'targeted')

    if not HAVE_SELINUX:
        # The only selinux info that can be collected in this instance is the
        # status and whether the Python library is present
        expected_selinux = {'status': 'Missing selinux Python library'}
        expected_python = False
    else:
        # The "selinux_python_present" value is always true in this instance
        # because it is the real Python library being used.
        expected_python = True


# Generated at 2022-06-13 03:28:05.246045
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # Create a mock class for moduleutils.compat.selinux
    class MockSelinux:
        class security_context:
            def __init__(self):
                return

        class selinux_config:
            def __init__(self):
                return

        @staticmethod
        def is_selinux_enabled():
            return True

        @staticmethod
        def security_policyvers():
            return 42

        @staticmethod
        def selinux_getenforcemode():
            return (0, 0)

        @staticmethod
        def security_getenforce():
            return 1

        @staticmethod
        def selinux_getpolicytype():
            return (0, "targeted")

    # Create a mock class for facts.module_utils.module_loading

# Generated at 2022-06-13 03:28:08.015020
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_collector = SelinuxFactCollector()
    collected_facts = dict()

    # No exceptions should be thrown.
    selinux_collector.collect(collected_facts=collected_facts)

# Generated at 2022-06-13 03:28:59.532780
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector is not None

# Generated at 2022-06-13 03:29:04.714049
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    fact_collector = SelinuxFactCollector()
    facts = fact_collector.collect()
    assert facts['selinux']['status'] == 'disabled'
    assert facts['selinux']['config_mode'] == 'disabled'
    assert facts['selinux']['mode'] == 'disabled'
    assert facts['selinux']['type'] == 'unknown'
    assert facts['selinux']['policyvers'] == 'unknown'

# Generated at 2022-06-13 03:29:13.081482
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    import pytest
    from ansible.module_utils.facts.collector import BaseFactCollector

    _collector = SelinuxFactCollector()

    with pytest.raises(AttributeError):
        _collector.collect()

    _base_collector = BaseFactCollector()
    _base_collector.collect = BaseFactCollector.collect

    with pytest.raises(AttributeError):
        _base_collector.collect(None, None)

    del _collector
    del _base_collector

# Generated at 2022-06-13 03:29:14.836172
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.name == 'selinux'

# Generated at 2022-06-13 03:29:17.085938
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    sc = SelinuxFactCollector()
    assert sc.name == 'selinux'
    assert sc._fact_ids == set()
    assert type(sc) == SelinuxFactCollector


# Generated at 2022-06-13 03:29:23.626790
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_fact_collector = SelinuxFactCollector()  # create instance of class with name SelinuxFactCollector
    result = selinux_fact_collector.collect()   # collecting facts
    keys = result.keys()  # key in the dictionary

    assert 'selinux' in keys
    assert 'selinux_python_present' in keys
    assert result['selinux_python_present'] == True
    # selinux_facts = result['selinux']
    assert 'mode' in result['selinux']
    assert 'type' in result['selinux']
    assert 'status' in result['selinux']
    assert 'config_mode' in result['selinux']
    assert 'policyvers' in result['selinux']

# Generated at 2022-06-13 03:29:25.548833
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    collector = SelinuxFactCollector()
    assert isinstance(collector, SelinuxFactCollector)
    assert collector.name == 'selinux'

# Generated at 2022-06-13 03:29:32.407262
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():

    # Test with selinux Python library present
    fake_module_util = dict()
    fake_module_util['is_selinux_enabled'] = lambda : True
    fake_module_util['security_getenforce'] = lambda : 0
    fake_module_util['selinux_getpolicytype'] = lambda : (0, 'targeted')
    fake_module_util['selinux_getenforcemode'] = lambda : (0, 1)
    fake_module_util['security_policyvers'] = lambda : 24
    fake_selinux = type('module', (), fake_module_util)
    module = type('module', (), dict(selinux=fake_selinux))

    fact_collector = SelinuxFactCollector(module=module)
    facts = fact_collector.collect()

# Generated at 2022-06-13 03:29:39.043985
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_collector = SelinuxFactCollector
    assert isinstance(selinux_collector.name, str)
    assert len(selinux_collector._fact_ids) > 0
    assert "selinux" in selinux_collector._fact_ids
    assert "selinux_python_present" in selinux_collector._fact_ids
    assert selinux_collector.name == "selinux"

# Generated at 2022-06-13 03:29:49.029961
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    try:
        from ansible.module_utils.compat import selinux
        HAVE_SELINUX = True
    except ImportError:
        HAVE_SELINUX = False

    if HAVE_SELINUX:
        SELinux_avcstats = selinux.selinux_avc_stats
        SELinux_enabled = selinux.is_selinux_enabled
        SELinux_getenforce = selinux.security_getenforce
        SELinux_getenforcemode = selinux.selinux_getenforcemode
        SELinux_getpolicytype = selinux.selinux_getpolicytype
        SELinux_policyvers = selinux.security_policyvers

    # If selinux Python library is not present, only create a stub class
    # which returns None for

# Generated at 2022-06-13 03:31:12.850093
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux = SelinuxFactCollector()
    assert selinux.name == 'selinux'
    assert selinux._fact_ids == set()

# Generated at 2022-06-13 03:31:18.117417
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():

    # create instance of class SelinuxFactCollector
    selinux_fc = SelinuxFactCollector()

    # create a fake module object with attributes from selinux library
    class FakeModule:
        def __init__(self):
            self.selinux_enabled = 1
            self.policyvers = '29'
            self.getenforcemode = (0, '1')
            self.getenforce = '1'
            self.getpolicytype = (0, 'targeted')

    # create instance of class FakeModule
    fake_module = FakeModule()

    # test selinux_fc.collect()
    facts = selinux_fc.collect(fake_module)
    assert facts['selinux']['status'] == 'enabled'
    assert facts['selinux']['policyvers'] == '29'

# Generated at 2022-06-13 03:31:19.628849
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    SELinux_collector = SelinuxFactCollector()
    SELinux_collector.collect()

# Generated at 2022-06-13 03:31:21.070707
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_collector = SelinuxFactCollector()
    selinux_collector.collect()

# Generated at 2022-06-13 03:31:25.525956
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():

    selinux_fact_collector = SelinuxFactCollector()
    (collected_facts, additional_facts) = selinux_fact_collector.collect()
    assert type(collected_facts) == dict
    assert collected_facts['selinux'] is not None
    assert collected_facts['selinux_python_present'] is not None
    assert len(collected_facts) == 2

# Generated at 2022-06-13 03:31:29.180267
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.name == 'selinux'
    assert 'selinux' in selinux_fact_collector.collect()

# Generated at 2022-06-13 03:31:29.858633
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
  pass

# Generated at 2022-06-13 03:31:33.823232
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    """
    Unit Test for SelinuxFactCollector()
    """
    selinux_collector = SelinuxFactCollector()
    assert selinux_collector.name == 'selinux'
    assert selinux_collector._fact_ids == set()



# Generated at 2022-06-13 03:31:36.215090
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux = SelinuxFactCollector()
    assert len(selinux.collect()) == 2
    assert 'selinux' in selinux.collect()
    assert 'selinux_python_present' in selinux.collect()



# Generated at 2022-06-13 03:31:46.210108
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():

    # Create a SelinuxFactCollector
    selinux_fact_collector = SelinuxFactCollector()

    # Create a test facts_dict
    test_facts_dict = {}

    # Module is not available, so the selinux Python library is
    # missing.
    test_facts_dict['selinux_python_present'] = False
    test_facts_dict['selinux'] = {'status': 'Missing selinux Python library'}
    assert selinux_fact_collector.collect(collected_facts=test_facts_dict) == test_facts_dict

    # Module is available, so the selinux Python library is
    # present.
    test_facts_dict['selinux_python_present'] = True

    # SELinux is disabled.