

# Generated at 2022-06-13 03:22:53.184732
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_facts = SelinuxFactCollector()
    selinux_facts.collect()

# Generated at 2022-06-13 03:22:57.281066
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_facts = SelinuxFactCollector()

    assert selinux_facts.name == 'selinux'
    assert 'selinux' in selinux_facts._fact_ids
    assert 'selinux_python_present' in selinux_facts._fact_ids

# Generated at 2022-06-13 03:23:07.435854
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():

    # Mock out any class methods that collect() relies on in order to use the
    # unit test on systems that don't have the Python library present
    class SelinuxMock(object):
        def __init__(self):
            self.counter = -1
            self.values = ['disabled', 'enabled', 0, 1, -1, 'selinux-python-lib', 'unknown']

        def is_selinux_enabled(self):
            self.counter += 1
            return self.values[self.counter]

        def security_policyvers(self):
            self.counter += 1
            if self.counter < len(self.values):
                return self.values[self.counter]
            else:
                raise OSError

        def selinux_getenforcemode(self):
            self.counter += 1

# Generated at 2022-06-13 03:23:09.942560
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    instance = SelinuxFactCollector()
    assert isinstance(instance, SelinuxFactCollector)
    assert instance.name == 'selinux'
    assert instance.collect()

# Generated at 2022-06-13 03:23:13.630066
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_fact_collector = SelinuxFactCollector()
    selinux_facts = selinux_fact_collector.collect(collected_facts={})
    assert selinux_facts['selinux']['status'] == 'disabled'

# Generated at 2022-06-13 03:23:16.933969
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_fact_obj = SelinuxFactCollector()
    result = selinux_fact_obj.collect()
    assert 'selinux' in result
    assert 'status' in result['selinux']
    assert result['selinux_python_present'] is True

# Generated at 2022-06-13 03:23:24.011291
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    """
    Unit test for method collect of class SelinuxFactCollector
    """
    # Dummy module does not exist and is not needed for this test
    module = None

    # Dummy variable 'collected_facts' does not exist and is not needed for this test
    collected_facts = None

    # Create object of class SelinuxFactCollector
    selinux_collector_obj = SelinuxFactCollector()

    # Test if method collect returns a dictionary
    assert type(selinux_collector_obj.collect(module=module, collected_facts=collected_facts)) == dict

# Generated at 2022-06-13 03:23:24.819633
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    assert isinstance(SelinuxFactCollector, object)

# Generated at 2022-06-13 03:23:27.135785
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_facts = SelinuxFactCollector()
    actual_output = selinux_facts.collect()
    expected_output = {'selinux': {'status': 'enabled'}}
    assert actual_output == expected_output

# Generated at 2022-06-13 03:23:29.028538
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    assert SelinuxFactCollector.name == 'selinux'
    assert SelinuxFactCollector._fact_ids == set()

# Generated at 2022-06-13 03:23:38.869691
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector.selinux import SelinuxFactCollector
    from ansible.module_utils.facts.collector import FactsCollector
    fact_collector = SelinuxFactCollector(BaseFactCollector)
    facts_dict = fact_collector.collect()

    assert 'selinux' in facts_dict.keys()
    # Unit test will fail if the Python library is missing
    assert 'status' in facts_dict['selinux'].keys()
    assert 'mode' in facts_dict['selinux'].keys()
    assert 'policyvers' in facts_dict['selinux'].keys()
    assert 'type' in facts_dict['selinux'].keys()

# Generated at 2022-06-13 03:23:44.764550
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    # Test members of class SelinuxFactCollector()
    assert selinux_fact_collector.name == 'selinux'
    assert selinux_fact_collector._fact_ids == set()

    # Test the size of the set() of the private member _fact_ids
    assert len(selinux_fact_collector._fact_ids) == 0

# Test the method collect() of class SelinuxFactCollector()

# Generated at 2022-06-13 03:23:55.882127
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    """This test case verifies that collect works properly if the Python SELinux
    library is not installed, and if the library is installed.
    """
    # Patch-out the selinux Python library, simulating its absence
    import sys
    # Save a reference to the module so it can be restored later
    original_selinux = sys.modules['ansible.module_utils.compat.selinux']
    sys.modules['ansible.module_utils.compat.selinux'] = None
    # Run the method
    selinux_fact_collector = SelinuxFactCollector()
    result = selinux_fact_collector.collect()
    # Assert that the result is a dictionary with 2 keys
    assert len(result.keys()) == 2, \
        'The result should be a dictionary containing two items'
    # Ass

# Generated at 2022-06-13 03:24:03.546489
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    fact = SelinuxFactCollector()
    result = fact.collect(collected_facts={})
    assert result['selinux_python_present'] == True
    assert 'status' in result['selinux']
    assert 'mode' in result['selinux']
    assert 'type' in result['selinux']
    assert 'policyvers' in result['selinux']
    assert 'config_mode' in result['selinux']


# Generated at 2022-06-13 03:24:13.006112
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    from ansible.module_utils.facts import ansible_selinux
    from ansible.module_utils.compat import selinux
    from ansible.module_utils.facts import ansible_selinux_python_present

    fake_module = None
    fake_collector = SelinuxFactCollector()
    fake_collected_facts = None
    result = fake_collector.collect(module=fake_module, collected_facts=fake_collected_facts)
    assert ansible_selinux == result['selinux']
    assert ansible_selinux_python_present == result['selinux_python_present']

    assert ansible_selinux_python_present == True
    assert ansible_selinux['status'] == 'enabled'
    assert ansible_selinux['policyvers'] == se

# Generated at 2022-06-13 03:24:15.313272
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    sfc = SelinuxFactCollector()
    assert sfc.name == 'selinux'
    assert sfc._fact_ids == set()

# Generated at 2022-06-13 03:24:20.350927
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    from ansible.module_utils.facts.collector import FactsCollector

    FC = FactsCollector()
    SF = SelinuxFactCollector()

    # Test when selinux Python library is not present
    facts = {}
    SF.collect(collected_facts=facts)  # Set 'selinux_python_present' to False

    # Test when selinux Python library is present but selinux is disabled
    facts = {
        'selinux_python_present' : True
    }
    SF.collect(collected_facts=facts)

    # Test when selinux Python library is present and selinux is enabled
    facts = {
        'selinux_python_present' : True
    }
    SF.collect(collected_facts=facts)

# Generated at 2022-06-13 03:24:22.631119
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    obj = SelinuxFactCollector()
    assert obj.name == 'selinux'
    assert len(obj._fact_ids) == 2

# Generated at 2022-06-13 03:24:32.962841
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_fact_collector = SelinuxFactCollector()
    test_module = 'testmodule'
    test_collected_facts = {}
    facts_dict = selinux_fact_collector.collect(module=test_module, collected_facts=test_collected_facts)

    assert len(facts_dict) == 2
    assert 'selinux' in facts_dict
    assert 'selinux_python_present' in facts_dict
    selinux_facts = facts_dict['selinux']

    assert len(selinux_facts) == 5
    assert 'status' in selinux_facts
    assert 'policyvers' in selinux_facts
    assert 'config_mode' in selinux_facts
    assert 'mode' in selinux_facts
    assert 'type' in selinux_facts

# Unit test

# Generated at 2022-06-13 03:24:37.197102
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # Check if facts collection is successful with missing selinux Python library
    selinux_instance = SelinuxFactCollector()
    selinux_instance.HAVE_SELINUX = False
    facts = selinux_instance.collect()
    assert 'status' in facts['selinux']
    assert facts['selinux_python_present'] is False

# Generated at 2022-06-13 03:24:47.929690
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_obj = SelinuxFactCollector()
    assert selinux_obj.name == 'selinux'
    assert selinux_obj._fact_ids == set()

# Generated at 2022-06-13 03:24:49.241527
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector is not None

# Generated at 2022-06-13 03:25:01.210676
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    test_cases = [
        {
            'description': 'Test constructor of class SelinuxFactCollector when selinux library is not present',
            'mock_selinux_import': False,
            'expected_result': {'selinux': {'status': 'Missing selinux Python library'}, 'selinux_python_present': False},
        },
        {
            'description': 'Test constructor of class SelinuxFactCollector when selinux library is present',
            'mock_selinux_import': True,
            'expected_result': {'selinux': {'status': 'disabled'}, 'selinux_python_present': True},
        }
    ]

    for test_case in test_cases:
        if test_case['mock_selinux_import'] is True:
            selinux_

# Generated at 2022-06-13 03:25:09.842470
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    import sys
    from unittest.mock import Mock, patch

    # Prepare arguments
    test_module = 'ansible.module_utils.facts.system.selinux.se_status'
    test_collected_facts = {}

    # Set up context
    selinux_fact_collector = SelinuxFactCollector()
    selinux_fact_collector.__module__ = 'ansible.module_utils.facts.system.selinux'


    # Replace the module, class, and method we want to test.
    # Also patch the selinux library to be our Mock.

# Generated at 2022-06-13 03:25:20.702389
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():

    # Create an empty module object
    module = {}

    # Create an empty return value object
    collected_facts = {}

    # Create an instance of class SelinuxFactCollector
    obj = SelinuxFactCollector()

    # Try to collect facts without selinux Python library and check that selinux
    # is present in the collected facts
    obj.HAVE_SELINUX = False
    obj.collect(module, collected_facts)
    assert len(collected_facts) == 2
    assert collected_facts['selinux_python_present'] == False
    assert collected_facts['selinux']['status'] == 'Missing selinux Python library'

    # Try to collect facts with selinux Python library and check that selinux is
    # present in the collected facts
    obj.HAVE_SELINUX = True

# Generated at 2022-06-13 03:25:33.610786
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    """
    The method collect() of class SelinuxFactCollector is a testing stub.
    """
    selinux_facts = {}

    # If selinux library is missing, only set the status and selinux_python_present since
    # there is no way to tell if SELinux is enabled or disabled on the system
    # without the library.
    if not HAVE_SELINUX:
        selinux_facts['status'] = 'Missing selinux Python library'
        facts_dict['selinux'] = selinux_facts
        facts_dict['selinux_python_present'] = False
        return facts_dict

    # Set a boolean for testing whether the Python library is present
    facts_dict['selinux_python_present'] = True


# Generated at 2022-06-13 03:25:37.925294
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # Create a class object for testing purposes
    selinux_fact_collector = SelinuxFactCollector()

    # Check if the fact_ids list is empty
    assert selinux_fact_collector.fact_ids == set()

    # Check if the returned list of facts is a dictionary
    assert isinstance(selinux_fact_collector.collect(), dict)

# Generated at 2022-06-13 03:25:44.520209
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_fact_collector = SelinuxFactCollector()
    result = selinux_fact_collector.collect({})
    expected_result = {'selinux': {'type': 'unknown', 'status': 'unknown', 'mode': 'unknown', 'policyvers': 'unknown', 'config_mode': 'unknown'}, 'selinux_python_present': True}
    assert result == expected_result

# Generated at 2022-06-13 03:25:52.544008
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():

    class MockModule():
        pass

    class MockCollector():
        pass

    class MockSelinux():
        def __init__(self):
            self.is_selinux_enabled_retval = True

        def is_selinux_enabled(self):
            return self.is_selinux_enabled_retval

    class ModuleStub():
        def __init__(self, *args, **kwargs):
            self.params = kwargs

    class CollectorStub():
        def __init__(self, *args, **kwargs):
            pass

    class SelinuxStub():
        def __init__(self, *args, **kwargs):
            pass

    module = MockModule()
    collector = MockCollector()
    selinux_obj = MockSelinux()

    old_module = Sel

# Generated at 2022-06-13 03:25:53.787031
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    SelinuxFactCollector()



# Generated at 2022-06-13 03:26:13.515634
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_obj = SelinuxFactCollector()
    assert selinux_obj is not None


# Generated at 2022-06-13 03:26:16.942370
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_facts = SelinuxFactCollector()
    assert selinux_facts.name == 'selinux'
    assert selinux_facts._fact_ids == set()

# Generated at 2022-06-13 03:26:25.650329
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils._text import to_bytes
    import json
    import os

    # Create the Collector object with the module_path of the directory containing
    # the collector plugins.
    collector = Collector(module_path=[os.path.dirname(os.path.abspath(__file__))])

    # Load the available collectors and cache
    collector.collect()

    # Create the SelinuxFactCollector object
    selinux_fact_collector = SelinuxFactCollector()

    # Collect the facts and return a dict
    facts_dict = selinux_fact_collector.collect()

    # Return the JSON representation of the facts
    facts = json.dumps(facts_dict)

    # Encode the facts for Python 3 compatibility

# Generated at 2022-06-13 03:26:35.517225
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    """
    This test is needed as the SELinux libraries involved in facts collection is
    using a dict to store the fact values which is not ordered. This makes
    testing of facts collection tricky and as such, this unit test is needed to
    verify that the facts are actually getting collected properly.
    """

    from . import SelinuxFactCollector
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts import cached

    class MockedBaseFactCollector(BaseFactCollector):
        name = 'MockedBaseFactCollector'
        _fact_ids = set()

    # Define a mocked method to return a mocked fact
    def mock_collect():
        return {'MockedBaseFactCollector': {'MockedBaseFactCollector': 'Mocked'}}

    # Mock the

# Generated at 2022-06-13 03:26:36.764337
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    fc = SelinuxFactCollector()
    assert fc.name == 'selinux'
    assert fc._fact_ids == set()
    assert fc._collect_count == 0


# Generated at 2022-06-13 03:26:38.998320
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.name == 'selinux'

# Generated at 2022-06-13 03:26:44.463741
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.name == 'selinux'
    assert len(selinux_fact_collector.collect()) == 2
    assert 'selinux_python_present' in selinux_fact_collector.collect()
    assert 'selinux' in selinux_fact_collector.collect()

# Generated at 2022-06-13 03:26:47.094082
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinuxfc = SelinuxFactCollector()
    assert selinuxfc.name == 'selinux'
    assert selinuxfc._fact_ids == set()

# Generated at 2022-06-13 03:26:50.307405
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    collector = SelinuxFactCollector()

    assert isinstance(collector, SelinuxFactCollector)
    assert isinstance(collector.name, str)
    assert isinstance(collector.collect(), dict)
    assert collector.collect().get('selinux', None)

# Generated at 2022-06-13 03:26:53.647842
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # Instantiating SelinuxFactCollector
    module = AnsibleModule(argument_spec={})
    selinux_fact_collector = SelinuxFactCollector(module=module)

    # Testing the collection method
    result = selinux_fact_collector.collect()

    # Asserting that the result is not empty
    assert result is not None

# Generated at 2022-06-13 03:27:29.237028
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    sfc = SelinuxFactCollector()
    sfc.collect()

# Generated at 2022-06-13 03:27:30.260884
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    SelinuxFactCollector()

# Generated at 2022-06-13 03:27:37.799733
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_fact_collector = SelinuxFactCollector()
    selinux_facts = selinux_fact_collector.collect()

    assert isinstance(selinux_facts, dict)
    assert "selinux" in selinux_facts
    assert isinstance(selinux_facts['selinux'], dict)
    # The test will pass if selinux module is present.
    # If not, it is still valid.
    assert 'selinux_python_present' in selinux_facts


# Generated at 2022-06-13 03:27:48.390820
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():

    # Assumptions
    facts_dict = dict()
    selinux_facts = dict()

    # Mock selinux library
    mock_selinux = MagicMock()
    mock_selinux.is_selinux_enabled = Mock(return_value = True)
    mock_selinux.security_getenforce = Mock(return_value = 1)
    mock_selinux.security_policyvers = Mock(return_value = 'foo')
    mock_selinux.selinux_getenforcemode = Mock(return_value = (0, 1))
    mock_selinux.selinux_getpolicytype = Mock(return_value = (0, 'bar'))
    sys.modules['selinux'] = mock_selinux

    # Test
    selinux_collector = SelinuxFactCollect

# Generated at 2022-06-13 03:27:50.458281
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_collector = SelinuxFactCollector()
    assert selinux_collector.name == 'selinux'
    assert selinux_collector._fact_ids == set()

# Generated at 2022-06-13 03:27:53.962336
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector(None)

    assert selinux_fact_collector.name == 'selinux'
    assert not selinux_fact_collector._fact_ids



# Generated at 2022-06-13 03:27:58.896812
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    fact_collector = SelinuxFactCollector()
    collected_facts = fact_collector.collect()
    assert collected_facts['selinux_python_present'] is False
    assert collected_facts['selinux']['status'] == 'Missing selinux Python library'


# Generated at 2022-06-13 03:28:01.489053
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    s = SelinuxFactCollector()
    assert isinstance(s, SelinuxFactCollector)
    assert isinstance(s, BaseFactCollector)


# Generated at 2022-06-13 03:28:03.272807
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_facts_collector = SelinuxFactCollector()
    assert selinux_facts_collector.name == 'selinux'
    assert selinux_facts_collector._fact_ids == set()



# Generated at 2022-06-13 03:28:08.990806
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    ansible_module = DummyAnsibleModule()

    # - If selinux library is missing, only set the status and selinux_python_present since
    #   there is no way to tell if SELinux is enabled or disabled on the system
    #   without the library.
    # - Set a boolean for testing whether the Python library is present
    facts_dict = {'selinux': {'status': 'Missing selinux Python library'}, 'selinux_python_present': False}
    SelinuxCollector = SelinuxFactCollector(ansible_module)
    assert facts_dict == SelinuxCollector.collect()

    # - If SELinux is not enabled on the system, only set the status to 'disabled'
    # - Set a boolean for testing whether the Python library is present
    selinux_enabled = False



# Generated at 2022-06-13 03:29:42.975772
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.name == 'selinux'

# Generated at 2022-06-13 03:29:52.690050
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    import platform
    import pytest
    from copy import deepcopy

    from ansible.module_utils.facts import FactCollector

    from ansible.module_utils.facts.collectors.selinux import SelinuxFactCollector
    from ansible.module_utils.facts.collectors.selinux import HAVE_SELINUX

    from ansible.module_utils.facts.collectors.system import SystemFactCollector
    from ansible.module_utils.facts.collectors.distribution import DistributionFactCollector
    from ansible.module_utils.facts.collectors.platform import PlatformFactCollector
    from ansible.module_utils.facts.collectors.pkg_mgr import PkgMgrFactCollector

    platform_fact_collector = PlatformFactCollector()
    pkg_mgr_fact_collector = P

# Generated at 2022-06-13 03:29:54.067007
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    pass

# Generated at 2022-06-13 03:30:02.294053
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    params = {
        'hostvars': {},
        'facts': {},
        'ansible_facts': {}
    }

    selinux_fact_collector = SelinuxFactCollector(module=params)
    selinux_facts = selinux_fact_collector.collect(collected_facts={})

    assert 'selinux' in selinux_facts
    assert 'status' in selinux_facts['selinux']
    assert 'selinux_python_present' in selinux_facts
    assert selinux_facts['selinux_python_present'] is True

# Generated at 2022-06-13 03:30:03.611819
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    facts_dict = SelinuxFactCollector()
    assert facts_dict.name == 'selinux'
    assert facts_dict._fact_ids == set()

# Generated at 2022-06-13 03:30:15.886061
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_collector = SelinuxFactCollector()
    collected_facts = dict()
    expected_facts = dict()
    expected_facts['selinux_python_present'] = True

    # Since selinux is not present, only the selinux_python_present fact
    # should be set.
    facts_dict = selinux_collector.collect(collected_facts=collected_facts)
    selinux_facts = facts_dict.get('selinux', dict())
    assert set(facts_dict.keys()) == set(expected_facts.keys())
    assert set(selinux_facts.keys()) == set(['status'])
    assert facts_dict.get('selinux_python_present') == expected_facts.get('selinux_python_present')

# Generated at 2022-06-13 03:30:17.778919
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    pass

# Generated at 2022-06-13 03:30:19.032252
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    assert isinstance(SelinuxFactCollector.collect(), dict)


# Generated at 2022-06-13 03:30:23.519208
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_facts = {
        'config_mode': 'unknown',
        'mode': 'unknown',
        'policyvers': 'unknown',
        'status': 'enabled',
        'type': 'unknown'
    }

    assert SelinuxFactCollector().collect() == {'selinux': selinux_facts}

# Generated at 2022-06-13 03:30:25.107157
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux = SelinuxFactCollector()
    assert selinux
    assert selinux.name == 'selinux'
