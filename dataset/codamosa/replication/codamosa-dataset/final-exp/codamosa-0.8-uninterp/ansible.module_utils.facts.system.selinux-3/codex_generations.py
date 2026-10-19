

# Generated at 2022-06-13 03:23:02.398468
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    """Test case for :function: `SelinuxFactCollector.collect`."""

    # Create a SelinuxFactCollector object
    selinux_fact_collector = SelinuxFactCollector

    module = None
    collected_facts = None

    # Create mock of module_utils/compat for selinux
    sys.modules['selinux'] = MagicMock()

    # Run the collect method of SelinuxFactCollector
    result = selinux_fact_collector.collect(module, collected_facts)

    # Assert that the method returns the correct dictionary
    assert result == {
        'selinux': {
            'status': 'disabled'
        },
        'selinux_python_present': True
    }

# Generated at 2022-06-13 03:23:08.065767
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    collected_facts = {
        'ansible_selinux': {
            'config_mode': 'Permissive',
            'mode': 'Permissive',
            'status': 'enabled',
            'type': 'targeted'
        }
    }

    module = None
    SelinuxFactCollector_instance = SelinuxFactCollector()
    collected_facts_returned = SelinuxFactCollector_instance.collect(module)
    assert collected_facts == collected_facts_returned

# Generated at 2022-06-13 03:23:10.906064
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    sfc = SelinuxFactCollector()
    assert sfc.name == 'selinux'
    assert len(sfc._fact_ids) == 0


# Generated at 2022-06-13 03:23:18.513593
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # Test with selinux library missing
    import sys
    saved_selinux_path = sys.modules['ansible.module_utils.compat.selinux']
    sys.modules['ansible.module_utils.compat.selinux'] = None

    collector = SelinuxFactCollector()
    facts_dict = collector.collect()

    assert facts_dict == {
        'selinux': {
            'status': 'Missing selinux Python library'
        },
        'selinux_python_present': False
    }

    # Restore selinux library
    sys.modules['ansible.module_utils.compat.selinux'] = saved_selinux_path

# Generated at 2022-06-13 03:23:23.609641
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    collector = SelinuxFactCollector()
    facts = collector.collect()
    assert 'selinux' in facts
    assert 'selinux_python_present' in facts
    assert 'type' in facts['selinux']
    assert 'status' in facts['selinux']
    assert 'mode' in facts['selinux']
    assert 'policyvers' in facts['selinux']
    assert 'config_mode' in facts['selinux']

# Generated at 2022-06-13 03:23:24.408841
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    SelinuxFactCollector()

# Generated at 2022-06-13 03:23:24.933351
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    pass

# Generated at 2022-06-13 03:23:32.742011
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    facts_dict = {}
    selinux_facts = {}

    # If selinux library is missing, only set the status and selinux_python_present since
    # there is no way to tell if SELinux is enabled or disabled on the system
    # without the library.
    if not HAVE_SELINUX:
        selinux_facts['status'] = 'Missing selinux Python library'
        facts_dict['selinux'] = selinux_facts
        facts_dict['selinux_python_present'] = False
        print(facts_dict)
        return facts_dict

    # Set a boolean for testing whether the Python library is present
    facts_dict['selinux_python_present'] = True

    if not selinux.is_selinux_enabled():
        selinux_facts['status'] = 'disabled'

# Generated at 2022-06-13 03:23:36.787911
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_fact_collector = SelinuxFactCollector()
    result = selinux_fact_collector.collect()
    assert result['selinux_python_present'] == True

# Generated at 2022-06-13 03:23:46.261097
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_fact_collector = SelinuxFactCollector()
    # Test when selinux lib is missing
    facts_dict = selinux_fact_collector.collect()
    assert 'selinux_python_present' in facts_dict
    assert 'selinux' in facts_dict
    assert 'status' in facts_dict['selinux']
    assert facts_dict['selinux']['status'] == 'Missing selinux Python library'


# Generated at 2022-06-13 03:23:55.258220
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_facts_collector = SelinuxFactCollector()
    result = selinux_facts_collector.collect()
    expected_result = {'selinux': {'status': 'enabled', 'policyvers': 28, 'config_mode': 'permissive', 'mode': 'permissive', 'type': 'targeted'}, 'selinux_python_present': True}
    assert(result == expected_result)

    selinux_facts_collector = SelinuxFactCollector()
    result = selinux_facts_collector.collect()
    expected_result = {'selinux_python_present': False, 'selinux': {'status': 'Missing selinux Python library'}}
    assert(result == expected_result)



# Generated at 2022-06-13 03:23:58.168716
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    obj = SelinuxFactCollector()
    assert obj.name == 'selinux'
    assert obj._fact_ids == set()
    assert obj.collect() == {'selinux': {'status': 'Missing selinux Python library'}, 'selinux_python_present': False}

# Generated at 2022-06-13 03:24:08.546808
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():

    # AnsibleModule.exit_json() will be called
    class AnsibleModule:
        def __init__(self, **kwargs):
            self.facts = {}
        def exit_json(self, **kwargs):
            self.facts = kwargs['ansible_facts']

    # AnsibleModule.run_command() will be called
    class Selinux:

        class policy:
            SECURITY_POLICY_VERSION = 1

        def security_policyvers(self):
            return self.policy.SECURITY_POLICY_VERSION

        def is_selinux_enabled(self):
            return True

        def selinux_getenforcemode(self):
            return 0, 0

        def security_getenforce(self):
            return 1

        def selinux_getpolicytype(self):
            return

# Generated at 2022-06-13 03:24:10.638542
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.name == 'selinux'

# Generated at 2022-06-13 03:24:11.960174
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    ob = SelinuxFactCollector()
    assert ob is not None

# Generated at 2022-06-13 03:24:16.425812
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    result = SelinuxFactCollector()
    assert isinstance(result, SelinuxFactCollector)
    assert result.name == 'selinux'
    assert isinstance(result._fact_ids, set)
    assert len(result._fact_ids) == 0

# Generated at 2022-06-13 03:24:18.795114
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_facts = SelinuxFactCollector()
    assert selinux_facts.name == 'selinux'
    assert selinux_facts._fact_ids == set()

# Generated at 2022-06-13 03:24:28.928816
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # Create a class object
    selinux_facts = SelinuxFactCollector()
    selinux_facts._module = {}

    # Disable selinux on system
    selinux.is_selinux_enabled = lambda: False

    # Call the collect method of class SelinuxFactCollector
    selinux_facts.collect()

    # Assert the status of selinux on system is disabled
    assert selinux_facts.data['selinux']['status'] == 'disabled'

    # Enable selinux on system
    selinux.is_selinux_enabled = lambda: True
    selinux.security_policyvers = lambda: 'abc'
    selinux.selinux_getenforcemode = lambda: (0, 1)
    selinux.security_getenforce = lambda: 1
    selinux.selinux_getpolicy

# Generated at 2022-06-13 03:24:36.847703
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    collector = SelinuxFactCollector()
    facts_dict = collector.collect(None, None)

    assert 'selinux' in facts_dict
    assert isinstance(facts_dict['selinux'], dict)
    assert facts_dict['selinux_python_present'] == True
    assert 'status' in facts_dict['selinux']
    assert 'policyvers' in facts_dict['selinux']
    assert 'config_mode' in facts_dict['selinux']
    assert 'mode' in facts_dict['selinux']
    assert 'type' in facts_dict['selinux']



# Generated at 2022-06-13 03:24:46.449694
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.collector.selinux import SelinuxFactCollector

    # Create a test Collector instance
    test_collector = Collector()
    test_collector.module = None
    test_collector.collected_facts = {}

    # If the selinux python library is not available, collect will return the
    # expected dictionary if it has been
    # imported with the following code and not with import selinux.
    try:
        from ansible.module_utils.compat import selinux
        HAVE_SELINUX = True
    except ImportError:
        HAVE_SELINUX = False

    # Create a test SelinuxFactCollector instance
    test_SelinuxFactCollector = SelinuxFactCollector()

   

# Generated at 2022-06-13 03:24:58.515965
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    slx_cl = SelinuxFactCollector()
    assert slx_cl.name == 'selinux'
    assert slx_cl._fact_ids == set()


# Generated at 2022-06-13 03:25:02.599411
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector

    collector = Collector()
    collector.collect_facts = lambda: {}

    my_collector = SelinuxFactCollector(collector)

    assert isinstance(my_collector.collect(), dict)

# Generated at 2022-06-13 03:25:05.908664
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.name == 'selinux'
    assert selinux_fact_collector._fact_ids == set()


# Generated at 2022-06-13 03:25:07.476669
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    c = SelinuxFactCollector()
    assert c.name == 'selinux'

# Generated at 2022-06-13 03:25:19.270399
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # Throw exception if there is not selinux Python library available
    def test_selinux_import_error(self):
        pass

    # Raise exception if there is selinux Python library available
    def test_selinux_import_error_no_raise(self):
        pass

    # Return false if selinux is not enabled on the system
    def is_selinux_enabled(self):
        return False

    # Return false if selinux is enabled on the system
    def is_selinux_enabled_true(self):
        return True

    # Return 1 if selinux is enforcing, 0 if permissive and -1 if disabled
    def security_getenforce(self):
        return 1

    # Return 1 if selinux is enforcing, 0 if permissive and -1 if disabled

# Generated at 2022-06-13 03:25:31.875315
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():

    class MockModule(object):
        pass

    mock_module = MockModule()

    # No selinux library is installed
    facts_dict = {}
    selinux_facts = {}

    selinux_facts['status'] = 'Missing selinux Python library'
    facts_dict['selinux'] = selinux_facts
    facts_dict['selinux_python_present'] = False

    selinux_facts_collector = SelinuxFactCollector()
    assert selinux_facts_collector.collect(mock_module) == facts_dict

    # selinux library is installed
    facts_dict = {}
    selinux_facts = {}

    selinux_facts['status'] = 'enabled'
    selinux_facts['policyvers'] = '28'
    selinux_facts['config_mode'] = 'enforcing'
    se

# Generated at 2022-06-13 03:25:35.238571
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_fact_collector = SelinuxFactCollector()
    facts_dict = selinux_fact_collector.collect()

    assert 'selinux' not in facts_dict
    assert 'selinux_python_present' not in facts_dict

# Generated at 2022-06-13 03:25:40.476535
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    module = AnsibleModuleMock()
    collected_facts = {}
    sfc = SelinuxFactCollector(module=module, collected_facts=collected_facts)
    assert sfc.name == 'selinux'
    assert sfc.module == module
    assert sfc._fact_ids == set()


# Generated at 2022-06-13 03:25:46.329505
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    import unittest
    from mock import patch

    # Collect facts
    def test_SelinuxFactCollector_collect(self):
        ansible_local = AnsibleLocalFactCollector()
        facts = ansible_local.collect()

        # Verify if SELinux is present in the facts
        self.assertIn('selinux', facts)

    if __name__ == '__main__':
        unittest.main()

# Generated at 2022-06-13 03:25:49.108352
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    assert(SelinuxFactCollector.name == "selinux")
    assert(SelinuxFactCollector._fact_ids is not None)
    assert(len(SelinuxFactCollector._fact_ids) == 2)


# Generated at 2022-06-13 03:26:11.302770
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_collector = SelinuxFactCollector()
    facts_dict = selinux_collector.collect()
    assert len(facts_dict) == 2
    assert 'selinux' in facts_dict
    assert 'selinux_python_present' in facts_dict
    assert not facts_dict['selinux_python_present'] and facts_dict['selinux']['status'] == 'Missing selinux Python library'

# Generated at 2022-06-13 03:26:14.689498
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()

    assert selinux_fact_collector is not None
    assert selinux_fact_collector.name == 'selinux'

# Generated at 2022-06-13 03:26:18.625047
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.name == 'selinux'
    assert selinux_fact_collector.priority == 80
    assert selinux_fact_collector._fact_ids == set()


# Generated at 2022-06-13 03:26:19.713050
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    SelinuxFactCollector.collect()

# Generated at 2022-06-13 03:26:27.394267
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    facts_dict = {}
    selinux_facts = {}

    # If selinux library is missing, only set the status and selinux_python_present since
    # there is no way to tell if SELinux is enabled or disabled on the system
    # without the library.
    if not HAVE_SELINUX:
        selinux_facts['status'] = 'Missing selinux Python library'
        facts_dict['selinux'] = selinux_facts
        facts_dict['selinux_python_present'] = False
        assert facts_dict == SelinuxFactCollector.collect()

    # Set a boolean for testing whether the Python library is present
    facts_dict['selinux_python_present'] = True

    if not selinux.is_selinux_enabled():
        selinux_facts['status'] = 'disabled'
   

# Generated at 2022-06-13 03:26:34.804140
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    import ansible.module_utils.facts.collector as facts_collector
    def get_mock_selinux_collector():
        mock_selinux_collector = facts_collector.BaseFactCollector()
        mock_selinux_collector.name = 'selinux'
        mock_selinux_collector._fact_ids = set()
        return mock_selinux_collector
    fact_collector = SelinuxFactCollector(get_mock_selinux_collector())
    fact_collector.collect()

# Generated at 2022-06-13 03:26:38.659182
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.name == 'selinux'
    assert selinux_fact_collector._fact_ids == set()

# Generated at 2022-06-13 03:26:43.123173
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    module = mock.MagicMock()
    fact = SelinuxFactCollector(module)
    collected_facts = {}
    fact.collect(module=module, collected_facts=collected_facts)
    assert collected_facts['selinux_python_present']

# Generated at 2022-06-13 03:26:45.142959
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.name == 'selinux'

# Generated at 2022-06-13 03:26:48.961068
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    fc = SelinuxFactCollector()
    collected_facts = {'selinux_python_present': False, 'selinux': {'status': 'disabled'}}
    fc.collect(collected_facts)
    assert collected_facts.get('selinux').get('status') == 'disabled'

# Generated at 2022-06-13 03:27:28.808614
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.name == 'selinux'
    assert selinux_fact_collector._fact_ids == set()


if __name__ == '__main__':
    test_SelinuxFactCollector()

# Generated at 2022-06-13 03:27:33.032233
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_col = SelinuxFactCollector()
    assert selinux_col.name == 'selinux'
    assert selinux_col.collect() is not None
    assert 'selinux' in selinux_col.collect()

# Generated at 2022-06-13 03:27:43.423873
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_dict = {
        'status': 'disabled',
        'config_mode': 'unknown',
        'mode': 'unknown',
        'type': 'unknown'
    }
    selinux_fact_collector = SelinuxFactCollector()
    
    # Test with selinux library present
    selinux_fact_collector.HAVE_SELINUX = True
    selinux_fact_collector.selinux = lambda: None
    selinux_fact_collector.selinux.is_selinux_enabled = lambda: False
    actual_dict = selinux_fact_collector.collect()

    assert actual_dict['selinux_python_present'] == True
    assert actual_dict['selinux'] == selinux_dict

    # Test with selinux library not present
    selinux_fact_

# Generated at 2022-06-13 03:27:46.865999
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.name == 'selinux'
    assert selinux_fact_collector._fact_ids == set()


# Generated at 2022-06-13 03:27:49.306239
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # pylint: disable=protected-access
    srv = SelinuxFactCollector()
    assert srv._fact_ids == set()
    assert not HAVE_SELINUX

# Generated at 2022-06-13 03:27:55.849323
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    facts_dict = SelinuxFactCollector().collect()
    assert 'selinux' in facts_dict
    assert facts_dict['selinux_python_present'] == HAVE_SELINUX

if HAVE_SELINUX:
    # Unit test for function collect()
    def test_collect():
        facts_dict = SelinuxFactCollector().collect()
        assert 'selinux' in facts_dict
        assert facts_dict['selinux_python_present'] == HAVE_SELINUX
        assert 'status' in facts_dict['selinux']
        assert facts_dict['selinux']['status'] == 'enabled' or 'disabled'
        assert 'mode' in facts_dict['selinux']
        assert 'type' in facts_dict['selinux']

# Generated at 2022-06-13 03:28:07.358729
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():

    # The arguments in the following mock_module_args object are not used, since they are just
    # placeholders. This object is passed to the AnsibleModule constructor in
    # the TestAnsibleModule class below.
    mock_module_args = dict(
        # These are dummy arguments:
        a=dict(required=True, type='str'),
        b=dict(required=False, default='c', type='str')
    )

    # The following class is used as an AnsibleModule mock, as in
    # https://docs.ansible.com/ansible/dev_guide/developing_modules_general.html#testing-modules
    class TestAnsibleModule(object):
        def __init__(self, **kwargs):
            self.params = kwargs

# Generated at 2022-06-13 03:28:14.845461
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    """ unit testing for method SelinuxFactCollector.collect """
    fake_module = "fake module"
    fake_collected_facts = "fake collected_facts"

    # If selinux library is missing, only set the status and selinux_python_present since
    # there is no way to tell if SELinux is enabled or disabled on the system
    # without the library.
    if not HAVE_SELINUX:
        expected_facts = {
            'selinux_python_present': False,
            'selinux': {
                'status': 'Missing selinux Python library',
            }
        }
        collected_facts = SelinuxFactCollector().collect(fake_module, fake_collected_facts)
        assert collected_facts == expected_facts
        return

    # Set a boolean for testing whether the Python library is

# Generated at 2022-06-13 03:28:21.359089
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # Initialize SelinuxFactCollector()
    se = SelinuxFactCollector()
    facts_dict = {}
    selinux_facts = {}
    selinux_facts['status'] = 'Missing selinux Python library'
    facts_dict['selinux'] = selinux_facts
    facts_dict['selinux_python_present'] = False

    # Call method collect
    result = se.collect()

    # Check if result equals facts_dict
    assert result == facts_dict

# Generated at 2022-06-13 03:28:28.048267
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    from ansible.module_utils.facts.collector.selinux import SelinuxFactCollector
    from ansible.module_utils.facts.collector.base import BaseFactCollector
    import sys

    class FakeModule(object):
        def __init__(self, params):
            self.params = params

        def get_bin_path(self, name, required, opt_dirs=None):
            return None

        def get_module_path(self):
            return '/path/to/lib'


# Generated at 2022-06-13 03:29:59.260716
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    obj = SelinuxFactCollector()
    assert isinstance(obj, SelinuxFactCollector)
    assert obj.name == 'selinux'
    assert obj._fact_ids == set()

# Generated at 2022-06-13 03:30:02.804867
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_facts = SelinuxFactCollector()
    assert selinux_facts.name == 'selinux'
    assert selinux_facts.collect() == {
        'selinux': {'status': 'disabled'},
        'selinux_python_present': False
    }

# Generated at 2022-06-13 03:30:04.319916
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinuxfactcollector = SelinuxFactCollector()
    assert selinuxfactcollector.name == 'selinux'
    assert 'selinux' in selinuxfactcollector.collect()


# Generated at 2022-06-13 03:30:11.092676
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    import sys
    import os.path
    sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
    from modules.selinux import SelinuxFactCollector
    fact_collector = SelinuxFactCollector()
    fact_collector.collect()
    print ('test')

# Generated at 2022-06-13 03:30:13.364554
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.name == 'selinux'

# Generated at 2022-06-13 03:30:14.715825
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    result = SelinuxFactCollector()
    assert result is not None

# Generated at 2022-06-13 03:30:15.885113
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    collector = SelinuxFactCollector()
    assert collector.name == "selinux"

# Generated at 2022-06-13 03:30:26.920681
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
  import mock
  selinux_facts_dict = {'config_mode': 'permissive', 'mode': 'permissive', 'status': 'enabled', 'type': 'targeted'}

  # Create a mock for the selinux library
  selinux_mock = mock.Mock()
  selinux_mock.is_selinux_enabled = mock.MagicMock(return_value = True)
  selinux_mock.security_getenforce = mock.MagicMock(return_value = 0)
  selinux_mock.selinux_getpolicytype = mock.MagicMock(return_value = (0, "targeted"))
  selinux_mock.selinux_getenforcemode = mock.MagicMock(return_value = (0, 0))

  # Build the return dictionary for the collect function
 

# Generated at 2022-06-13 03:30:28.610689
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    assert SelinuxFactCollector()

# Generated at 2022-06-13 03:30:35.840125
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():

    # Mock selinux
    import mock
    import selinux
    selinux_obj = selinux.__dict__
    selinux_obj['is_selinux_enabled'] = mock.MagicMock(return_value=True)
    selinux_obj['security_getenforce'] = mock.MagicMock(return_value=1)
    selinux_obj['security_policyvers'] = '21'
    selinux_obj['selinux_getenforcemode'] = mock.MagicMock(return_value=(0, 1))
    selinux_obj['selinux_getpolicytype'] = mock.MagicMock(return_value=(0, 'targeted'))

    # Test
    sfc = SelinuxFactCollector()
    test_facts = sfc.collect()