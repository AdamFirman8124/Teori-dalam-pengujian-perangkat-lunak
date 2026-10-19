

# Generated at 2022-06-13 03:22:53.865985
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    mock_module = object()
    mock_collected_facts = object()
    selinux_fact_collector = SelinuxFactCollector(mock_module, mock_collected_facts)
    assert selinux_fact_collector.name == 'selinux'
    assert selinux_fact_collector._fact_ids == set()


# Generated at 2022-06-13 03:23:05.317274
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # We expect these dictionaries as return values
    # If the status is disabled
    facts_dict_disabled = {
        'selinux': {'status': 'disabled'},
        'selinux_python_present': True
    }

    # If SELinux is enabled
    facts_dict_enabled = {
        'selinux': {
            'policyvers': '24',
            'type': 'targeted',
            'config_mode': 'enforcing',
            'mode': 'enforcing',
            'status': 'enabled'
        },
        'selinux_python_present': True
    }


    import sys
    old_modules = sys.modules.copy()

# Generated at 2022-06-13 03:23:10.165926
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_collector = SelinuxFactCollector()
    assert selinux_collector.name == 'selinux'
    assert selinux_collector.collect() == {'selinux': {'status': 'Missing selinux Python library'}, 'selinux_python_present': False}

# Generated at 2022-06-13 03:23:12.960395
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector.selinux import SelinuxFactCollector

    SelinuxFactCollector.collect(None, None)

# Generated at 2022-06-13 03:23:15.520690
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    sl_facts = SelinuxFactCollector()
    assert sl_facts.name == 'selinux'
    assert sl_facts._fact_ids == set()


# Generated at 2022-06-13 03:23:18.635113
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_facts = SelinuxFactCollector().collect()
    assert selinux_facts.get('selinux') is not None
    assert selinux_facts.get('selinux_python_present') is not None

# Generated at 2022-06-13 03:23:20.357355
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # selinux = SelinuxFactCollector()
    # print selinux.collect()
    pass

# Generated at 2022-06-13 03:23:27.793724
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # We don't want to fail the selinux module because of the selinux library being missing.
    # This would cause all selinux facts to be missing. Instead, we want to inform the user
    # that the library is missing and then only try to gather information that is available.
    # The first test checks that the missing library results in a disabled status and library
    # not present. The second part tests whether this method can gather the
    # expected facts for a system with selinux enabled.

    # Mock out the selinux library
    def mock_import_selinux(*args, **kwargs):
        return None

    selinux_collector = SelinuxFactCollector()
    # Test first case where library not loaded
    selinux_collector.__class__.selinux = mock_import_selinux
    result = selinux_collector.collect

# Generated at 2022-06-13 03:23:35.146374
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # Create a test class
    class TestClass(object):
        def __init__(self):
            self.python_version = 2.7
            global HAVE_SELINUX
            HAVE_SELINUX = True
            self.is_selinux_enabled = False
            self.security_policyvers = '24'
            self.selinux_getenforcemode = lambda: (0, 1)
            self.security_getenforce = lambda: 0
            self.selinux_getpolicytype = lambda: (0, 'targeted')

    # Create an instance of the test class
    test_instance = TestClass()
    # Create a test module
    class TestModule(object):
        def __init__(self):
            self.params = dict()
            self.selinux = test_instance

    selinux_

# Generated at 2022-06-13 03:23:36.217453
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    SelinuxFactCollector()

# Generated at 2022-06-13 03:23:50.417166
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():

    # Setup the class
    selinux_fact_collector = SelinuxFactCollector()

    # Test when selinux module is not present
    selinux_fact_collector.HAVE_SELINUX = False
    selinux_facts = selinux_fact_collector.collect()
    assert selinux_facts['selinux'] == {'status': 'Missing selinux Python library'}
    assert selinux_facts['selinux_python_present'] == False

    # Test when selinux is disabled
    selinux_fact_collector.HAVE_SELINUX = True
    selinux_fact_collector.selinux.is_selinux_enabled = lambda: False
    selinux_facts = selinux_fact_collector.collect()

# Generated at 2022-06-13 03:23:55.467821
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    """Unit test for constructor of class SelinuxFactCollector.
    """
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.name == 'selinux'
    assert isinstance(selinux_fact_collector._fact_ids, set)
    assert not selinux_fact_collector._fact_ids

# Generated at 2022-06-13 03:23:56.674721
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    collector = SelinuxFactCollector()
    assert collector.name == 'selinux'

# Generated at 2022-06-13 03:24:03.527442
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    m = """

- hosts: ansible-test-01
  vars:
    ansible_user: /bin/foo
  tasks:
    - name: test facts
      debug:
        msg: "{{ ansible_selinux }}"
    - name: test facts
      debug:
        msg: "{{ ansible_selinux_python_present }}"
"""
    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils.facts.collector import BaseFactCollector, ModuleCollector


    fake_module = type('AnsibleModuleFake', (), {'run_command': (lambda *args, **kwargs: (0, '', ''))})

    ####################################################################
    # Case 1: selinux library is available and selinux is disabled
    #

# Generated at 2022-06-13 03:24:05.612676
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    x = SelinuxFactCollector()
    assert x.name == 'selinux'
    assert isinstance(x, SelinuxFactCollector)

# Generated at 2022-06-13 03:24:08.547054
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    x = SelinuxFactCollector()
    assert x.name == 'selinux'
    assert isinstance(x._fact_ids, set)
    assert len(x._fact_ids) == 0

# Generated at 2022-06-13 03:24:16.990073
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # Library missing
    selinux_missing = SelinuxFactCollector()
    selinux_missing_facts = selinux_missing.collect()
    assert selinux_missing_facts['selinux']['status'] == 'Missing selinux Python library'
    assert selinux_missing_facts['selinux_python_present'] == False

    # Library present
    selinux_present = SelinuxFactCollector()
    selinux_present_facts = selinux_present.collect()
    assert selinux_present_facts['selinux_python_present'] == True
    assert selinux_present_facts['selinux']['config_mode'] in ['enforcing', 'permissive', 'disabled', 'unknown']
    assert selinux_present_facts['selinux']['status'] in ['enabled', 'disabled']
    assert se

# Generated at 2022-06-13 03:24:19.850114
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector is not None
    assert selinux_fact_collector.name == 'selinux'


# Generated at 2022-06-13 03:24:30.163667
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    def selinux_is_selinux_enabled_mock(self):
        return True

    selinux.is_selinux_enabled = selinux_is_selinux_enabled_mock

    def selinux_selinux_getenforcemode_mock(self):
        return (0, 1)

    selinux.selinux_getenforcemode = selinux_selinux_getenforcemode_mock

    def selinux_security_policyvers_mock(self):
        return 23

    selinux.security_policyvers = selinux_security_policyvers_mock

    def selinux_security_getenforce_mock(self):
        return 1

    selinux.security_getenforce = selinux_security_getenforce_mock


# Generated at 2022-06-13 03:24:33.205398
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    t = SelinuxFactCollector()
    assert t.name == 'selinux'
    assert t._fact_ids == set(['selinux', 'selinux_python_present'])

# Generated at 2022-06-13 03:24:44.858209
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    collector = SelinuxFactCollector()
    assert 'selinux' == collector.name

# Generated at 2022-06-13 03:24:51.102926
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    # fake data
    class fake_ansible_module(object):
        def __init__(self, selinux_module=None):
            self.selinux = selinux_module

    # fake import if selinux is not present
    if not HAVE_SELINUX:
        class fake_selinux(object):
            class selinux(object):
                @staticmethod
                def security_getenforce():
                    pass

                @staticmethod
                def selinux_getenforcemode():
                    pass

                @staticmethod
                def security_policyvers():
                    pass

                @staticmethod
                def selinux_getpolicytype():
                    pass

                @staticmethod
                def is_selinux_enabled():
                    pass

    # test
   

# Generated at 2022-06-13 03:24:56.642183
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.name == 'selinux'
    assert selinux_fact_collector.fact_ids == ['selinux_python_present', 'selinux']


# Generated at 2022-06-13 03:25:05.987023
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():

    # Create instance of class SelinuxFactCollector
    selinux_fact_collector = SelinuxFactCollector()

    # If a selinux library does not exist, the following should be
    # added to the facts dictionary.
    expected_dict = {
        'selinux': {
            'status': 'Missing selinux Python library',
        },
        'selinux_python_present': False
    }

    # Call method collect of class SelinuxFactCollector
    actual_dict = selinux_fact_collector.collect()

    # Verify expected dictionary is the same as actual dictionary
    assert actual_dict == expected_dict, "Expected: %s  Actual: %s" % (expected_dict, actual_dict)

# Generated at 2022-06-13 03:25:18.189455
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_fact_collector = SelinuxFactCollector()
    returned_facts = selinux_fact_collector.collect()
    if 'selinux' in returned_facts:
        selinux_facts = returned_facts['selinux']
    else:
        selinux_facts = {}

    if not HAVE_SELINUX:
        assert selinux_facts['status'] == 'Missing selinux Python library'
    else:
        if not selinux.is_selinux_enabled():
            assert selinux_facts['status'] == 'disabled'
        else:
            assert selinux_facts['status'] == 'enabled'
            assert selinux_facts['config_mode'] in ('enforcing', 'disabled', 'permissive', 'unknown')

# Generated at 2022-06-13 03:25:21.430333
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector
    assert selinux_fact_collector.name == 'selinux'
    assert selinux_fact_collector._fact_ids == set()


# Generated at 2022-06-13 03:25:31.781635
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # side effect of setting HAVE_SELINUX to True
    # would be to change the test result by detecting
    # the selinux library, so set HAVE_SELINUX to False
    # to avoid the side effect
    global HAVE_SELINUX
    HAVE_SELINUX = False

    objTest = SelinuxFactCollector()

    expected = {'selinux_python_present': False, 'selinux': {'status': 'Missing selinux Python library'}}
    actual = objTest.collect(None, None)

    assert set(expected) == set(actual)
    assert isinstance(actual['selinux'], dict)

# Generated at 2022-06-13 03:25:38.693605
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    # Test instantiation of class SelinuxFactCollector
    selinux_facter = SelinuxFactCollector()

    # Test method collect()
    selinux_facts = selinux_facter.collect()
    assert 'selinux' in selinux_facts
    assert 'status' in selinux_facts['selinux']
    assert 'mode' in selinux_facts['selinux']
    assert 'type' in selinux_facts['selinux']
    assert 'config_mode' in selinux_facts['selinux']

# Generated at 2022-06-13 03:25:40.773887
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    obj = SelinuxFactCollector()
    assert obj


# Generated at 2022-06-13 03:25:42.652951
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_fact = SelinuxFactCollector()
    assert selinux_fact.collect() is not None

# Generated at 2022-06-13 03:26:03.208857
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    x = SelinuxFactCollector()
    assert x.name == 'selinux'

# Generated at 2022-06-13 03:26:04.440427
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fc = SelinuxFactCollector()
    assert selinux_fc

# Generated at 2022-06-13 03:26:07.190682
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():

    # Test constructor with argument passed
    selinux_fact_collector_with_arg = SelinuxFactCollector({})
    assert not selinux_fact_collector_with_arg is None



# Generated at 2022-06-13 03:26:11.740638
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # Setup the test
    selinux_collector = SelinuxFactCollector()
    selinux_collector.collect()

    # Test assumes selinux module is not present
    # and therefore selinux facts should be unknown
    assert selinux_collector.collector['selinux_python_present'] == False
    assert selinux_collector.collector['selinux']['status'] == 'Missing selinux Python library'

# Generated at 2022-06-13 03:26:17.854191
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    assert 'selinux' == SelinuxFactCollector.name
    assert 'selinux' in SelinuxFactCollector._fact_ids
    assert BaseFactCollector in SelinuxFactCollector.__bases__
    selinux_obj = SelinuxFactCollector()
    assert 'selinux' == selinux_obj.name
    assert 'selinux' in selinux_obj._fact_ids

# Generated at 2022-06-13 03:26:18.844058
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    assert SelinuxFactCollector()

# Generated at 2022-06-13 03:26:26.892519
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    """
    Test the method collect of class SelinuxFactCollector.
    """
    # pylint: disable=protected-access, missing-docstring, no-self-use
    def _getenforcemode(run_method=True):
        if run_method:
            return (0, 0)
        else:
            return (-1, -1)

    def _is_selinux_enabled():
        return False

    class MockSelinux:
        def __init__(self):
            self.is_selinux_enabled = _is_selinux_enabled
            self.selinux_getpolicytype = lambda: (0, 'targeted')
            self.selinux_getenforcemode = _getenforcemode
            self.security_getenforce = lambda: 1

    mocked_module = MockS

# Generated at 2022-06-13 03:26:32.659051
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_collector = SelinuxFactCollector()
    assert selinux_collector.name == 'selinux'
    # _fact_ids is a set so order of elements is not guaranteed
    assert 'selinux' in selinux_collector._fact_ids
    assert 'selinux_python_present' in selinux_collector._fact_ids

# Generated at 2022-06-13 03:26:34.613322
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    SelinuxCollector = SelinuxFactCollector()
    assert SelinuxCollector.name == 'selinux'

# Generated at 2022-06-13 03:26:41.444174
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.name == 'selinux', \
        'name=%r instead of \'selinux\'' % selinux_fact_collector.name
    assert selinux_fact_collector._fact_ids == set(), \
        '_fact_ids=%r instead of set()' % selinux_fact_collector._fact_ids

# Generated at 2022-06-13 03:27:28.848689
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    """
    Tests the return of SelinuxFactCollector.collect() against a known
    facts file.
    """
    testfile = os.path.join(os.path.dirname(__file__), 'unit', 'modules', 'test_data',
                            'FactsCollector', 'selinux_facts.json')

    with open(testfile, 'r') as f:
        try:
            fc = SelinuxFactCollector()
            results = fc.collect()
            test_results = json.load(f)
            assert results == test_results
        except:
            assert False

# Generated at 2022-06-13 03:27:29.584427
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    x = SelinuxFactCollector()
    assert x

# Generated at 2022-06-13 03:27:33.874496
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinuxFactCollector = SelinuxFactCollector()
    assert selinuxFactCollector.name == 'selinux'
    assert len(selinuxFactCollector._fact_ids) == 0


# Generated at 2022-06-13 03:27:37.568093
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    import sys
    from ansible.module_utils.facts.collector import FactsCollector
    from ansible.module_utils.facts import BaseFactModule

    # Backup the selinux library so we can restore it after mocking it
    sys.modules['_ansible_selinux'] = selinux

# Generated at 2022-06-13 03:27:39.246064
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    obj = SelinuxFactCollector()
    assert obj.name == 'selinux'


# Generated at 2022-06-13 03:27:41.074049
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux = SelinuxFactCollector()
    assert selinux.name == 'selinux'

# Generated at 2022-06-13 03:27:51.104684
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # Test if selinux Python library is present
    if HAVE_SELINUX:
        fact_class_collector_test = SelinuxFactCollector()
        result = fact_class_collector_test.collect()
        assert isinstance(result, dict)
        assert 'selinux' in result
        assert 'selinux_python_present' in result
        assert isinstance(result['selinux'], dict)
        assert 'status' in result['selinux']
        assert result['selinux_python_present'] == True

    # Test if selinux Python library is missing
    else:
        fact_class_collector_test = SelinuxFactCollector()
        result = fact_class_collector_test.collect()
        assert isinstance(result, dict)
        assert 'selinux' in result


# Generated at 2022-06-13 03:27:54.439684
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinuxfc = SelinuxFactCollector()
    facts_dict = selinuxfc.collect()
    assert 'selinux' in facts_dict
    assert 'selinux_python_present' in facts_dict

# Generated at 2022-06-13 03:27:58.561239
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_collector = SelinuxFactCollector()
    facts = selinux_collector.collect()
    print(facts)

if __name__ == '__main__':
    test_SelinuxFactCollector_collect()

# Generated at 2022-06-13 03:28:00.602988
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector_obj = SelinuxFactCollector()
    assert selinux_fact_collector_obj.name == 'selinux'

# Generated at 2022-06-13 03:29:46.895325
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    facts_dict = SelinuxFactCollector.collect()
    assert 'selinux' in facts_dict
    assert 'status' in facts_dict['selinux']
    assert 'selinux_python_present' in facts_dict
    assert facts_dict['selinux_python_present'] is False

# Generated at 2022-06-13 03:29:49.747693
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    SELINUX_FACT_COLLECTOR = SelinuxFactCollector()
    # test the name is set correctly
    assert SELINUX_FACT_COLLECTOR.name == 'selinux'

# Generated at 2022-06-13 03:29:51.627880
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.name == 'selinux'

# Generated at 2022-06-13 03:29:55.116480
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    assert(SelinuxFactCollector.name == 'selinux')

# Generated at 2022-06-13 03:29:57.870056
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    collector = SelinuxFactCollector
    facts = collector.collect()
    assert 'selinux' in facts
    assert 'status' in facts['selinux']

# Generated at 2022-06-13 03:30:00.100224
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    obj = SelinuxFactCollector()
    assert obj.name == 'selinux'


# Generated at 2022-06-13 03:30:01.030716
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    SelinuxFactCollector().collect()

# Generated at 2022-06-13 03:30:05.699628
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    module = None
    collected_facts = {'kernel':'linux'}
    if not HAVE_SELINUX:
        selinux_facts = {'status': 'Missing selinux Python library'}
        selinux_python_present = False
    else:
        selinux_facts = {
            'status': 'disabled',
            'config_mode': 'unknown',
            'mode': 'unknown',
            'policyvers': 'unknown',
            'type': 'unknown'
        }
        selinux_python_present = True
    facts_dict = {'selinux': selinux_facts, 'selinux_python_present': selinux_python_present}
    expected_facts_dict = {'selinux':selinux_facts, 'selinux_python_present': selinux_python_present}

# Generated at 2022-06-13 03:30:12.082841
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    """
    Unit test for method collect of class SelinuxFactCollector
    """
    fact_collector = SelinuxFactCollector()
    facts_dict = fact_collector.collect()
    assert facts_dict['selinux'] is not None
    assert facts_dict['selinux']['status'] is not None

# Generated at 2022-06-13 03:30:15.615531
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector is not None
    assert selinux_fact_collector.name == 'selinux'
    assert selinux_fact_collector._fact_ids == set()