

# Generated at 2022-06-13 03:23:00.091388
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():

    # Setup
    selinux_fact_collector = SelinuxFactCollector()
    selinux_facts = {}
    selinux_facts['status'] = 'enabled'
    selinux_facts['policyvers'] = '24'
    selinux_facts['config_mode'] = 'enforcing'
    selinux_facts['mode'] = 'enforcing'
    selinux_facts['type'] = 'targeted'
    collected_facts = { 'selinux' : selinux_facts }

    # Test
    collected_facts = selinux_fact_collector.collect(collected_facts=collected_facts)

    # Verify
    assert 'selinux' in collected_facts
    assert 'status' in collected_facts['selinux']
    assert 'policyvers' in collected_facts['selinux']

# Generated at 2022-06-13 03:23:05.893641
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():

    selinux_fact = SelinuxFactCollector()

    # check name and _fact_ids.
    assert selinux_fact.name == 'selinux'
    assert selinux_fact._fact_ids == set()

    # check facts
    selinux_facts = selinux_fact.collect()
    assert "selinux" in selinux_facts.keys()
    assert selinux_facts["selinux"] is not None

# Generated at 2022-06-13 03:23:13.878514
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    import sys
    import pytest

    from ansible.module_utils.facts.collector.selinux import SelinuxFactCollector

    selinux_facts = SelinuxFactCollector().collect()
    if HAVE_SELINUX and selinux.is_selinux_enabled():
        assert selinux_facts['selinux']['status'] == 'enabled'
    else:
        assert selinux_facts['selinux']['status'] == 'disabled'

    assert selinux_facts['selinux_python_present'] == True

# Generated at 2022-06-13 03:23:17.642481
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_facts = SelinuxFactCollector()
    result = selinux_facts.collect()
    assert result == {'selinux': {
        'status': 'enabled',
        'config_mode': 'unknown',
        'type': 'unknown',
        'mode': 'unknown',
        'policyvers': 'unknown'},
        'selinux_python_present': True}

# Generated at 2022-06-13 03:23:21.783627
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_fact_collector = SelinuxFactCollector()
    result = selinux_fact_collector.collect()
    assert result['selinux']['status'] == 'Missing selinux Python library'
    assert result['selinux_python_present'] == False

# Generated at 2022-06-13 03:23:23.705155
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    obj = SelinuxFactCollector()
    assert obj.name == 'selinux'
    assert obj.collect() == {'selinux': {}, 'selinux_python_present': False}

# Generated at 2022-06-13 03:23:25.519783
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    module = True
    collected_facts = True
    fact = SelinuxFactCollector()
    fact.collect(module, collected_facts)

# Generated at 2022-06-13 03:23:27.543790
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    assert SelinuxFactCollector.collect() == {'selinux_python_present': True, 'selinux': {'status': 'Missing selinux Python library'}}

# Generated at 2022-06-13 03:23:30.233695
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    from ansible.module_utils.facts.collector.selinux import SelinuxFactCollector
    selinux_fact_collector = SelinuxFactCollector()
    selinux_facts = selinux_fact_collector.collect()
    assert selinux_facts['selinux']['status'] in ('enabled', 'disabled')

# Generated at 2022-06-13 03:23:32.670035
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    input_module = None
    input_collected_facts = None

    selinux_fact_collector = SelinuxFactCollector()
    output = selinux_fact_collector.collect(input_module, input_collected_facts)

    # Test whether the returned value of method collect is a dictionary
    assert(isinstance(output, dict))

# Generated at 2022-06-13 03:23:43.555724
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    obj = SelinuxFactCollector()
    assert obj.name == 'selinux'
    assert obj._fact_ids == set(['selinux', 'selinux_python_present'])

# Generated at 2022-06-13 03:23:54.498821
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    from ansible.module_utils.facts.collector import FactCollector
    from ansible.module_utils.facts.collector.selinux import SelinuxFactCollector

    # Get a list of facts collectors
    m = 'ansible.module_utils.facts.collector'
    fact_collectors = [getattr(__import__(m), n) for n in FactCollector.__subclasses__()]

    # Verify that the Selinux collection is supported
    assert SelinuxFactCollector in fact_collectors

    # Collect facts
    selinux_facts = SelinuxFactCollector().collect()

    # Verify that the selinux facts were collected
    assert 'selinux' in selinux_facts
    assert isinstance(selinux_facts['selinux'], dict)

    # Verify that the boolean for testing

# Generated at 2022-06-13 03:23:57.098116
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    my_obj = SelinuxFactCollector()
    results = my_obj.collect(module=None, collected_facts={})
    assert(results['selinux_python_present'] == True)

# Generated at 2022-06-13 03:24:03.881265
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_dict = {
        'status': 'enabled',
        'policyvers': '29',
        'config_mode': 'permissive',
        'mode': 'permissive',
        'type': 'targeted'
    }

    # Mocked module
    module = AnsibleModuleMock(
        params={}
    )

    # Mocked selinux library
    class MockedSelinux:
        def __init__(self):
            self.SELINUX_ENFORCE = 0
            self.SELINUX_PERMISSIVE = 1
            self.SELINUX_DISABLED = -1

        def is_selinux_enabled(self):
            return True

        def security_policyvers(self):
            return '29'

        def selinux_getenforcemode(self):
            return

# Generated at 2022-06-13 03:24:04.649854
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    assert SelinuxFactCollector._fact_ids == set()

# Generated at 2022-06-13 03:24:13.283165
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():

    # Create a SelinuxFactCollector object
    s = SelinuxFactCollector()

    # Create a test facts dictionary
    test_facts_dict = dict()

    # Create a test results dictionary
    test_results_dict = dict()

    # Call method collect of SelinuxFactCollector object
    result = s.collect(collected_facts=test_facts_dict)
    test_results_dict['selinux'] = {
        'config_mode': 'unknown',
        'mode': 'unknown',
        'policyvers': 'unknown',
        'status': 'enabled',
        'type': 'unknown'}
    test_results_dict['selinux_python_present'] = True
    assert result == test_results_dict

# Generated at 2022-06-13 03:24:22.789017
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    facts_dict = {}
    test = SelinuxFactCollector()

    # Run collect method when HAVE_SELINUX is False to test
    # it sets the 'status' field to 'Missing selinux Python library'
    # and 'selinux_python_present' field to False
    HAVE_SELINUX = False
    facts_dict = test.collect()
    assert 'status' in facts_dict['selinux']
    assert 'selinux_python_present' in facts_dict
    assert facts_dict['selinux']['status'] == 'Missing selinux Python library'
    assert facts_dict['selinux_python_present'] == False

    # Mock the selinux.is_selinux_enabled() method to return False
    selinux.is_selinux_enabled = lambda: False

    # Run

# Generated at 2022-06-13 03:24:33.205648
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector.selinux import SelinuxFactCollector

    selinux_fact_collector = SelinuxFactCollector()
    result = selinux_fact_collector.collect()

    assert result is not None
    assert isinstance(result, dict)
    assert 'selinux' in result
    assert isinstance(result['selinux'], dict)
    assert result['selinux_python_present'] is not None
    assert isinstance(result['selinux_python_present'], bool)


# Generated at 2022-06-13 03:24:36.151879
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_collector = SelinuxFactCollector()
    assert selinux_collector.name == 'selinux'
    assert selinux_collector._fact_ids == set()


# Generated at 2022-06-13 03:24:45.328919
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    """Test method SelinuxFactCollector.collect()
    """
    # Test collect function when a non-SELinux system is tested
    shell_mock = {
        'selinuxenabled': 0,
        'selinux_status': "disabled",
        'selinux_policyvers': '',
        'selinux_config_mode': '',
        'selinux_mode': '',
        'selinux_policytype': ''
    }
    with patch.dict(SelinuxFactCollector.__salt__, shell_mock):
        collected_facts = SelinuxFactCollector.collect(module=None, collected_facts=None)
        assert collected_facts['ansible_facts']['selinux']['status'] == 'disabled'

# Generated at 2022-06-13 03:24:55.900681
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    obj = SelinuxFactCollector()
    assert obj.name == 'selinux'

# Generated at 2022-06-13 03:25:00.869475
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # If selinux Python library is missing, return empty dictionary
    if not HAVE_SELINUX:
        assert SelinuxFactCollector.collect() == { 'selinux' : {}, 'selinux_python_present' : False }
    else:
        try:
            assert SelinuxFactCollector.collect() == {
                'selinux': {
                    'status': 'enabled',
                    'policyvers': 'unknown',
                    'config_mode': 'unknown',
                    'mode': 'unknown',
                    'type': 'unknown'
                },
                'selinux_python_present' : True
            }
        except ImportError:
            assert SelinuxFactCollector.collect() == { 'selinux' : {}, 'selinux_python_present' : False }

# Generated at 2022-06-13 03:25:05.327634
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    # Create a SelinuxFactCollector object
    selinux_fact_collector = SelinuxFactCollector()

    # Check the name of the object
    assert selinux_fact_collector.name == 'selinux'
    assert isinstance(selinux_fact_collector, BaseFactCollector)

# Generated at 2022-06-13 03:25:07.623276
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    val = SelinuxFactCollector()
    facts = val.collect()
    assert 'status' in facts['selinux']

# Generated at 2022-06-13 03:25:19.404528
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.compat import selinux
    import types

    # Create a fake selinux module to work with
    module = types.ModuleType('selinux')

    # Create the two functions that we need
    def fake_is_selinux_enabled():
        return False

    def fake_is_selinux_enabled_true():
        return True

    # Monkey patch the functions onto the fake module
    module.is_selinux_enabled = fake_is_selinux_enabled
    module.is_selinux_enabled_true = fake_is_selinux_enabled

# Generated at 2022-06-13 03:25:20.612595
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    c = SelinuxFactCollector()
    assert c.name == 'selinux'

# Generated at 2022-06-13 03:25:28.152399
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_info = {'selinux': {'status': 'enabled',
                                'policyvers': 'unknown',
                                'config_mode': 'unknown',
                                'mode': 'enforcing',
                                'type': 'unknown'},
                    'selinux_python_present': True}

    result = SelinuxFactCollector().collect()

    assert result == selinux_info

# Generated at 2022-06-13 03:25:30.668325
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.name == 'selinux'

# Generated at 2022-06-13 03:25:33.061217
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    s = SelinuxFactCollector()
    assert s.name == 'selinux'
    assert s._fact_ids == set()


# Generated at 2022-06-13 03:25:37.765640
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    module = AnsibleModuleMock()
    collected_facts = AnsibleFactsCollector()

    sfc = SelinuxFactCollector(module=module, collected_facts=collected_facts)
    facts = sfc.collect()
    assert facts == {
        'selinux': {'status': 'disabled'},
        'selinux_python_present': True
    }


# Generated at 2022-06-13 03:25:56.551773
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    collected_facts = dict()
    SelinuxFactCollector().collect(module=None, collected_facts=collected_facts)


# Generated at 2022-06-13 03:25:59.819601
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    testobj = SelinuxFactCollector()
    assert testobj.name == 'selinux'
    # SELinux facts are not platform dependent
    assert testobj.platform == ''
    # SELinux facts are not distribution dependent
    assert testobj.distribution == ''

# Generated at 2022-06-13 03:26:02.187369
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    obj = SelinuxFactCollector()
    assert obj.name == 'selinux'
    assert obj._fact_ids == set()


# Generated at 2022-06-13 03:26:05.164569
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.name == 'selinux'
    assert selinux_fact_collector._fact_ids == set()


# Generated at 2022-06-13 03:26:10.849847
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    from ansible.module_utils.facts import gathering

    content = gathering.get_ansible_facts(gathering.__file__, 'setup')
    result = SelinuxFactCollector().collect(None, content)
    assert result.get('selinux') == {'status': 'enabled', 'policyvers': '28', 'config_mode': 'enforcing', 'mode': 'enforcing', 'type': 'targeted'}
    assert result.get('selinux_python_present') == True



# Generated at 2022-06-13 03:26:18.139067
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_collector = SelinuxFactCollector()
    facts_dict = selinux_collector.collect()
    facts_dict2 = {}
    if 'selinux' in facts_dict:
        facts_dict2['selinux'] = facts_dict['selinux']
    if 'selinux_python_present' in facts_dict:
        facts_dict2['selinux_python_present'] = facts_dict['selinux_python_present']
    assert facts_dict2 == selinux_collector.collect()

# Generated at 2022-06-13 03:26:21.344053
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()

    assert 'selinux' == selinux_fact_collector.name
    assert set() == selinux_fact_collector._fact_ids


# Generated at 2022-06-13 03:26:23.197980
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    fact_collector = SelinuxFactCollector()
    assert fact_collector.name == 'selinux'

# Generated at 2022-06-13 03:26:27.919394
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    c = SelinuxFactCollector()
    facts = c.collect()
    assert 'selinux' in facts
    assert facts['selinux_python_present'] == True
    assert facts['selinux']['type'] == 'unknown'
    assert facts['selinux']['config_mode'] == 'unknown'
    assert facts['selinux']['status'] == 'enabled'
    assert facts['selinux']['mode'] == 'unknown'
    assert facts['selinux']['policyvers'] == 'unknown'

# Generated at 2022-06-13 03:26:34.348476
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    assert SelinuxFactCollector()
    with patch('ansible.module_utils.compat.selinux.is_selinux_enabled') as mock_is_selinux_enabled:
        mock_is_selinux_enabled.return_value = False
        selinux_facts = SelinuxFactCollector()
        selinux_facts._collect()
        assert 'selinux_python_present' in selinux_facts.collect()


# Generated at 2022-06-13 03:27:11.346755
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    fake_module = object()
    fake_collector = SelinuxFactCollector(fake_module)
    fake_collector._module = fake_module
    fake_collector.collect()

# Generated at 2022-06-13 03:27:12.793378
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    result = SelinuxFactCollector()
    assert result.name == 'selinux'

# Generated at 2022-06-13 03:27:23.806799
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
#   Facts Collected by this class
#
#   This class does not collect any facts. It only tests whether selinux
#   library is available or not and sets some boolean values accordingly
#   to indicate if selinux is available.
#
#   Facts are collected by the setup module and by the selinux modules.

    # selinux variables
    selinux_status = "enabled"
    selinux_mode = "enforcing"
    selinux_policyvers = 1
    selinux_config_mode = "enforcing"
    selinux_type = "selinux"

    # Gather facts
    collected_facts = {}
    facts = SelinuxFactCollector(collected_facts, None)
    facts.collect()
    fact_dict = facts.get_facts()

    # Test values of fact_dict

# Generated at 2022-06-13 03:27:25.546591
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    obj = SelinuxFactCollector()
    assert obj.name == 'selinux'

# Generated at 2022-06-13 03:27:28.770015
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinuxFact = SelinuxFactCollector()
    assert 'selinux' == selinuxFact.name and isinstance(selinuxFact, BaseFactCollector)

# Generated at 2022-06-13 03:27:39.421182
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()

    # Test the name and _fact_ids property of class SelinuxFactCollector
    assert (selinux_fact_collector.name == 'selinux' and
            selinux_fact_collector._fact_ids == set())

    if HAVE_SELINUX:
        import os

        # Test the collect function (SELinux is enabled,
        # selinux.is_selinux_enabled() returns True)
        os.environ['SELINUX'] = '1'
        collected_facts = selinux_fact_collector.collect()

# Generated at 2022-06-13 03:27:47.761019
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # Verify that trying to collect facts without the selinux Python library
    # available results in the expected data being set.
    global HAVE_SELINUX
    HAVE_SELINUX = False
    fc = SelinuxFactCollector()
    facts = fc.collect()
    assert 'selinux_python_present' in facts
    assert 'selinux' in facts
    assert facts['selinux_python_present'] is False
    assert facts['selinux']['status'] == 'Missing selinux Python library'
    # Re-enable selinux Python library for other tests.
    HAVE_SELINUX = True

# Generated at 2022-06-13 03:27:54.861253
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():

    def mock_selinux_is_selinux_enabled(self):
        return True

    def mock_selinux_security_getenforce(self):
        return 0

    def mock_selinux_security_policyvers(self):
        return 25

    def mock_selinux_selinux_getenforcemode(self):
        return (0,1)

    def mock_selinux_selinux_getpolicytype(self):
        return (0, 'targeted')

    selinux.selinux_is_selinux_enabled = mock_selinux_is_selinux_enabled
    selinux.security_getenforce = mock_selinux_security_getenforce
    selinux.security_policyvers = mock_selinux_security_policyvers
    selinux.selin

# Generated at 2022-06-13 03:28:06.042831
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # Create an instance of the SelinuxFactCollector class
    selinux_fact_collector = SelinuxFactCollector()
    # Create a fake AnsibleModule object
    module = AnsibleModuleMock()
    # Create a mock context manager
    context_manager = MagicMock()
    # Create a fake module temporary directory
    module_tmp_dir = tempfile.mkdtemp()
    context_manager.__enter__.return_value = module_tmp_dir
    # Create a fake temporary directory
    tmp_dir = tempfile.mkdtemp()
    # Create a fake selinux config file
    selinux_config_file = os.path.join(tmp_dir, 'selinux')
    # Write fake selinux config to file
    with open(selinux_config_file, 'w') as f:
        f

# Generated at 2022-06-13 03:28:08.049616
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    sfc = SelinuxFactCollector()
    assert sfc.HAVE_SELINUX == True
    return sfc


# Generated at 2022-06-13 03:29:46.244928
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinuxfacts = SelinuxFactCollector()
    output = selinuxfacts.collect(None, None)
    assert "selinux" in output.keys(), "The value for the key selinux should exist"
    assert "missing" not in output["selinux"]["status"], "The value for the key status should not be missing"

# Generated at 2022-06-13 03:29:49.072226
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():

    selinux_collector = SelinuxFactCollector()
    assert selinux_collector.name == 'selinux'
    assert selinux_collector._fact_ids == set()


# Generated at 2022-06-13 03:29:49.587024
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    SelinuxFactCollector()


# Generated at 2022-06-13 03:29:51.151775
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
  selinuxfactcollector = SelinuxFactCollector()
  assert selinuxfactcollector.name == 'selinux'

# Generated at 2022-06-13 03:29:56.833088
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    x = SelinuxFactCollector()
    assert x.name == 'selinux'
    assert x._fact_ids == set()

# check collect() when selinux module is not present

# Generated at 2022-06-13 03:29:59.429884
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    x = SelinuxFactCollector()
    assert x is not None
    assert 'selinux' == x.name


# Generated at 2022-06-13 03:30:06.593923
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # Create a new instance of the collector to call collect
    selinux_fact_collector = SelinuxFactCollector()
    selinux_facts = selinux_fact_collector.collect()

    if HAVE_SELINUX:
        # Check the facts selinux_python_present and status are correct if selinux is installed
        assert selinux_facts['selinux_python_present'] == True
        assert selinux_facts['selinux']['status'] == 'enabled'
    else:
        # Check the facts selinux_python_present and status are correct if selinux is not installed
        assert selinux_facts['selinux_python_present'] == False
        assert selinux_facts['selinux']['status'] == 'Missing selinux Python library'

# Generated at 2022-06-13 03:30:13.904646
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # Create instance of class SelinuxFactCollector
    selinux_fc = SelinuxFactCollector()
    # Invoke method collect
    facts_dict = selinux_fc.collect()
    assert 'selinux' in facts_dict
    assert 'status' in facts_dict['selinux']
    assert facts_dict['selinux_python_present'] == True or facts_dict['selinux_python_present'] == False


# Generated at 2022-06-13 03:30:16.326724
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    # Initialize instance of class SelinuxFactCollector
    selinux_collector = SelinuxFactCollector()

    # Assert that name attribute is set to selinux
    assert selinux_collector.name == 'selinux'

    # Assert that the instance of class CollectModule has the attribute set to selinux
    assert getattr(selinux_collector, 'collected_facts') == 'selinux'



# Generated at 2022-06-13 03:30:18.466620
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    assert SelinuxFactCollector().name == "selinux"