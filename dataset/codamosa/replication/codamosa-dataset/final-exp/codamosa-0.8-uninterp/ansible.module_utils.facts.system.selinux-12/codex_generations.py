

# Generated at 2022-06-13 03:22:55.641249
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    x = SelinuxFactCollector()
    assert x.name == 'selinux'

# Generated at 2022-06-13 03:23:06.345005
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    class MockModuleUtilsCompat(object):
        class MockSelinux(object):
            @staticmethod
            def is_selinux_enabled():
                return True

            @staticmethod
            def security_policyvers():
                return '1.23'

            @staticmethod
            def selinux_getenforcemode():
                return 0, 0

            @staticmethod
            def security_getenforce():
                return 0

            @staticmethod
            def selinux_getpolicytype():
                return 0, 'unknown'

    class MockModuleUtilsCompatMissing(object):
        pass

    # Unit test when selinux library is installed
    mock_module = MockModuleUtilsCompat()
    collected_facts = {}

    obj = SelinuxFactCollector(mock_module, collected_facts)
    facts = obj.collect()

   

# Generated at 2022-06-13 03:23:09.097180
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    obj = SelinuxFactCollector()
    assert obj.name == 'selinux'
    assert obj._fact_ids == set()

# Generated at 2022-06-13 03:23:14.791870
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    """
    This is a unit test for constructor of class SelinuxFactCollector
    """
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.name == 'selinux'
    assert isinstance(selinux_fact_collector.collect(), dict)
    assert 'selinux' in selinux_fact_collector.collect().keys()

# Generated at 2022-06-13 03:23:16.295677
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    x = SelinuxFactCollector()
    assert x.name == 'selinux'
    assert x._fact_ids == set()

# Generated at 2022-06-13 03:23:19.198019
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    myselinux = SelinuxFactCollector()
    assert myselinux.name == 'selinux'
    assert len(myselinux._fact_ids) == 0

# Generated at 2022-06-13 03:23:21.612496
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_module = BaseFactCollector()
    s = SelinuxFactCollector()
    output = s.collect(selinux_module)
    assert type(output) is dict

# Generated at 2022-06-13 03:23:23.021212
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert isinstance(selinux_fact_collector, BaseFactCollector)

# Generated at 2022-06-13 03:23:24.755053
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    assert SelinuxFactCollector.name == 'selinux'
    assert SelinuxFactCollector._fact_ids == set()


# Generated at 2022-06-13 03:23:28.133265
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    selinux_dict = {'status': 'enabled', 'policyvers': 'unknown', 'config_mode': 'unknown', 'mode': 'permissive', 'type': 'unknown'}
    
    assert selinux_dict == selinux_fact_collector.collect(collected_facts=None)

# Generated at 2022-06-13 03:23:44.569264
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # Simulate missing selinux library
    selinux_python_present = False

    selinux_facts = {}
    selinux_facts['status'] = 'disabled'
    selinux_facts['policyvers'] = 'unknown'
    selinux_facts['config_mode'] = 'unknown'
    selinux_facts['mode'] = 'unknown'
    selinux_facts['type'] = 'unknown'

    selinux_facts_dict = {}
    selinux_facts_dict['selinux'] = selinux_facts
    selinux_facts_dict['selinux_python_present'] = selinux_python_present

    # Create object of type SelinuxFactCollector
    selinux_fact_collector = SelinuxFactCollector()

    # Get the facts
    facts_dict = selinux_fact_collector.collect()


# Generated at 2022-06-13 03:23:55.799353
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    import pytest

    # Mock module
    class MockModule():
        def __init__(self):
            self.params = {}

    MockModule.selinux_python_present = False
    MockModule.selinux_status = 'disabled'

    try:
        import selinux
        MockModule.selinux_python_present = True
        if selinux.is_selinux_enabled():
            MockModule.selinux_status = 'enabled'
    except ImportError:
        pass

    mock_module = MockModule()

    # Mock collected_facts
    collected_facts = {}

    # Obtain an instance of class SelinuxFactCollector
    selinux_facts = SelinuxFactCollector()

    # Call method collect of class SelinuxFactCollector

# Generated at 2022-06-13 03:24:07.240680
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    import os
    import sys
    import unittest.mock as mock
    from sys import version_info

    # Set the environment variable used by selinux.is_selinux_enabled()
    os.environ['SELINUX_INIT'] = '1'

    with mock.patch('ansible.module_utils.facts.collector.BaseFactCollector.collect') as base_collect:
        selinux_collector = SelinuxFactCollector()
        base_collect.return_value = {}

        # Test the case where selinux library is not present.
        # This will make the selinux library unavailable, so that
        # if the module is imported, the following code blocks in
        # the library will throw an import exception.
        if version_info[0] == 2:
            sys.modules['selinux'] = None

# Generated at 2022-06-13 03:24:16.134294
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    ''' Unit test for method collect of class SelinuxFactCollector '''
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector.selinux import SelinuxFactCollector
    from ansible.module_utils.compat import selinux

    BaseFactCollector.collectors = []
    collector = SelinuxFactCollector(module=None, collected_facts=None)
    collected_facts = collector.collect()
    assert collected_facts.get('selinux').get('mode') == 'unknown'
    assert collected_facts.get('selinux').get('status') == 'disabled'
    assert isinstance(collected_facts.get('selinux'), dict)
    assert collected_facts.get('selinux_python_present') is False

# Generated at 2022-06-13 03:24:18.237174
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    obj = SelinuxFactCollector()
    assert obj.name == 'selinux'
    assert obj._fact_ids == set()

# Generated at 2022-06-13 03:24:22.288131
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    """Test if the facts dictionary is generated properly"""
    # Unit test for method collect of class SelinuxFactCollector
    # pylint: disable=protected-access,unsubscriptable-object
    selinux_facts = {
        'status': 'enabled',
        'policyvers': '1',
        'config_mode': 'enforcing',
        'mode': 'enforcing',
        'type': 'targeted',
    }
    collector = SelinuxFactCollector()
    facts = collector._collect()
    if HAVE_SELINUX:
        assert 'selinux' in facts
        assert facts['selinux'] == selinux_facts
    else:
        assert 'selinux' not in facts
        assert facts['selinux_python_present'] == False

# Generated at 2022-06-13 03:24:24.420133
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_facts = SelinuxFactCollector().collect()
    assert 'selinux' in selinux_facts
    assert 'selinux_python_present' in selinux_facts

# Generated at 2022-06-13 03:24:27.809617
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_collector = SelinuxFactCollector()
    assert 'selinux' == selinux_collector.name
    assert 'selinux_python_present' in selinux_collector._fact_ids
    assert 'selinux' in selinux_collector._fact_ids
    assert 'selinux' in selinux_collector.fact_namespace_lookups

# Generated at 2022-06-13 03:24:37.912836
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    class MockModule(object):
        def get_bin_path(self, exe, opt_dirs=[]):
            return 'test_path', None

        def run_command(self, cmd, check_rc=False, close_fds=True, executable=None, data=None, binary_data=False, path_prefix=None, cwd=None, use_unsafe_shell=False, prompt_regex=None, environ_update=None, umask=None):
            return 0, '0\n', ''

    collected_facts = {}
    current_collector = SelinuxFactCollector()
    results = current_collector.collect(MockModule(), collected_facts=collected_facts)
    assert 'selinux' in results
    assert results['selinux']['status'] == 'enabled'
   

# Generated at 2022-06-13 03:24:44.751419
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    from ansible.module_utils import basic

    # Ensure selinux library is not present
    basic.remove_module('selinux')

    test_obj = SelinuxFactCollector()
    result = test_obj.collect()
    # The result should be a dictionary
    assert isinstance(result, dict)

    # Ensure that the expected keys are present even though
    # the selinux library was not present
    assert result['selinux_python_present'] == False
    assert result['selinux']
    assert result['selinux']['status'] == 'Missing selinux Python library'

# Generated at 2022-06-13 03:24:54.634899
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    mock_module = type('MockModule', (object,), {'_short_params': {}, 'params': {}, 'run_command': type('MockRunCommand', (), {'return_value': ['enforcing']})})

# Generated at 2022-06-13 03:24:58.974477
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_col = SelinuxFactCollector()
    assert selinux_fact_col is not None
    assert selinux_fact_col.name == 'selinux'
    assert len(selinux_fact_col._fact_ids) == 0


# Generated at 2022-06-13 03:25:01.818422
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    sfc = SelinuxFactCollector()
    assert sfc.name == 'selinux'
    assert 'selinux' in sfc._fact_ids



# Generated at 2022-06-13 03:25:04.225935
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_collector = SelinuxFactCollector()
    assert (selinux_collector.name == 'selinux')

# Generated at 2022-06-13 03:25:07.157753
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector is not None
    assert hasattr(selinux_fact_collector, 'collect')

# Generated at 2022-06-13 03:25:19.008463
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # Create a mock object
    class mock_module_util_selinux(object):
        def __init__(self, *args, **kwargs):
            # Avoid calling selinux.is_selinux_enabled()
            raise Exception

    SELINUX_MODE = {1: 'enforcing', 0: 'permissive', -1: 'disabled'}

    # Mock is_selinux_enabled
    selinux.is_selinux_enabled = lambda : True

    # Mock selinux_getenforcemode and security_getenforce
    selinux.selinux_getenforcemode = lambda : (0, 1)
    selinux.security_getenforce = lambda : 0

    # Mock selinux_getpolicytype
    selinux.selinux_getpolicytype = lambda : (0, 'mcs')

   

# Generated at 2022-06-13 03:25:21.770788
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_facts = SelinuxFactCollector()
    assert selinux_facts.name == 'selinux'
    assert selinux_facts._fact_ids == set(['selinux', 'selinux_python_present'])

# Generated at 2022-06-13 03:25:33.968540
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # Mock method collect of class SelinuxFactCollector
    selinux_fact_collector = SelinuxFactCollector()

    # Mock selinux.is_selinux_enabled(), return true
    selinux_fact_collector.is_selinux_enabled = Mock(return_value=True)

    # Mock selinux.security_policyvers(), return '1.2.3'
    selinux_fact_collector.security_policyvers = Mock(return_value='1.2.3')

    # Mock selinux.selinux_getenforcemode(), return (0, 1)
    selinux_fact_collector.selinux_getenforcemode = Mock(return_value=(0, 1))

    # Mock selinux.security_getenforce(), return 1
    selinux_fact_collector.security_get

# Generated at 2022-06-13 03:25:34.911930
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    SelinuxFactCollector()

# Generated at 2022-06-13 03:25:36.800619
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    s = SelinuxFactCollector()
    assert s.name == 'selinux'
    assert s._fact_ids == set()


# Generated at 2022-06-13 03:25:55.293171
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts.collector.system import SystemFactCollector
    from ansible.module_utils.facts.collector.virtual import VirtualFactCollector
    from ansible.module_utils.facts.collector.network import NetworkFactCollector

    # Create an instance of structure required for the unit test
    # It won't contain a correct ansible_module_args
    # In order to not have to patch all get_all_facts()'s instances,
    # patching the whole get_all_facts() method is done
    module = {'ansible_module_args': ''}
    # Create an instance of SystemFactCollector. This instance will
    # contain a "module" attribute with

# Generated at 2022-06-13 03:25:58.876597
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    # Test for the insertion of arguments in the constructor of class SelinuxFactCollector
    selinux_collector = SelinuxFactCollector()

    # Assert that the length of the fact_ids list is 0
    assert len(selinux_collector._fact_ids) == 0

# Generated at 2022-06-13 03:26:02.745695
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_collector = SelinuxFactCollector()
    assert 'selinux' == selinux_collector.name
    assert 'selinux_python_present' in selinux_collector._fact_ids

# Generated at 2022-06-13 03:26:05.086021
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinuxfc = SelinuxFactCollector()

    assert selinuxfc.name == 'selinux'
    assert selinuxfc._fact_ids == set()


# Generated at 2022-06-13 03:26:05.993630
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    SelinuxFactCollector()

# Generated at 2022-06-13 03:26:13.831824
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    mock_module = object()

    mocked_is_selinux_enabled = {
        'return_value': True
    }

    mocked_security_policyvers = {
        'return_value': '28'
    }

    mocked_selinux_getenforcemode = {
        'return_value': (0, 0)
    }

    mocked_security_getenforce = {
        'return_value': int(-1)
    }

    mocked_selinux_getpolicytype = {
        'return_value': (0, 'targeted')
    }


# Generated at 2022-06-13 03:26:23.772836
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    from ansible.module_utils.facts import default_collectors # pylint: disable=E0611

    # Create a fact collector object for SELinux facts
    fc = SelinuxFactCollector()

    # Create a set of module_utils.facts.fact.Collector objects
    collectors = set()
    for collector in default_collectors:
        collectors.add(collector())

    # Create a module_utils.facts.legacy.Facts object
    result = {'local': {'gather_subset': ['all'], 'gather_timeout': 10, 'filter': ['ansible_python_version', 'ansible_selinux']},
              'ansible_python_version': '2.7'}
    facts = {'ansible_python_version': '2.7'}

    # Set the

# Generated at 2022-06-13 03:26:27.203748
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.name == 'selinux'

# Generated at 2022-06-13 03:26:32.921689
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    """
    Tests which collect facts without selinux python library
    """
    selinux_fact_collector = SelinuxFactCollector()
    collected_facts = selinux_fact_collector.collect()
    assert collected_facts['selinux_python_present'] is False
    assert collected_facts['selinux']['status'] == 'Missing selinux Python library'

# Generated at 2022-06-13 03:26:44.626966
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    """
    SelinuxFactCollector.collect() returns a dict of selinux facts
    """
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector.selinux import SelinuxFactCollector

    # Save original imported libraries for later restoring
    OriginalBaseFactCollector = BaseFactCollector
    OriginalSelinuxFactCollector = SelinuxFactCollector

    MockBaseFactCollector = None
    MockSelinuxFactCollector = None
    MockSelinux = None

    # Replace imported libraries with Mock objects
    def setUpModule():
        global OriginalBaseFactCollector
        global OriginalSelinuxFactCollector
        global MockBaseFactCollector
        global MockSelinuxFactCollector


# Generated at 2022-06-13 03:27:03.638340
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.name == 'selinux'
    assert selinux_fact_collector._fact_ids == set()


# Generated at 2022-06-13 03:27:08.538544
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    mock_module = Mock()
    mock_module.params = {}
    mock_se_module = Mock()

    # Testing scenario when python selinux module is present
    selinux.security_policyvers = Mock()
    selinux.is_selinux_enabled = Mock()
    selinux.selinux_getenforcemode = Mock()
    selinux.security_getenforce = Mock()
    selinux.selinux_getpolicytype = Mock()
    selinux.security_policyvers.return_value = 123
    selinux_getenforcemode_return = [0, 1]
    selinux.selinux_getenforcemode.return_value = selinux_getenforcemode_return
    selinux_security_getenforce_return = 1
    selinux.security_getenforce.return_value = selinux

# Generated at 2022-06-13 03:27:11.835096
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_fact_collector = SelinuxFactCollector()
    assert isinstance(selinux_fact_collector, SelinuxFactCollector)

# Generated at 2022-06-13 03:27:12.885471
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    assert type(SelinuxFactCollector)

# Generated at 2022-06-13 03:27:14.724051
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_collector = SelinuxFactCollector()
    assert selinux_collector.collect()

# Generated at 2022-06-13 03:27:21.442589
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    example_selinux_dict = {
        'selinux': {
            'config_mode': 'permissive',
            'mode': 'permissive',
            'status': 'enabled',
            'type': 'targeted'
        },
        'selinux_python_present': True
    }
    fact_collector = SelinuxFactCollector()
    selinux_facts = fact_collector.collect()
    assert(selinux_facts != example_selinux_dict)

# Generated at 2022-06-13 03:27:31.177807
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    fake_selinux = selinux
    fake_selinux.is_selinux_enabled = lambda: True
    fake_selinux.security_policyvers = lambda: 1
    fake_selinux.selinux_getenforcemode = lambda: (0, 1)
    fake_selinux.security_getenforce = lambda: 1
    fake_selinux.selinux_getpolicytype = lambda: (0, "targeted")

    selinuxfp = SelinuxFactCollector()
    result = selinuxfp.collect()
    assert result['selinux']['type'] == 'targeted' and result['selinux']['config_mode'] == 'enforcing' and result['selinux']['mode'] == 'enforcing' and result['selinux']['policyvers'] == 1

# Generated at 2022-06-13 03:27:34.533346
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    x = SelinuxFactCollector()
    assert x.name == 'selinux'
    assert x._fact_ids == set()


# Generated at 2022-06-13 03:27:36.235953
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_collector = SelinuxFactCollector()
    assert selinux_collector.name == 'selinux'

# Generated at 2022-06-13 03:27:39.333275
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    from ansible.module_utils.facts.collector import Collector
    c = SelinuxFactCollector()
    assert c.name == 'selinux'
    assert isinstance(c, Collector)
    assert isinstance(c.collect(), dict)

# Generated at 2022-06-13 03:28:18.960558
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_facts = SelinuxFactCollector()
    assert selinux_facts.name == 'selinux'
    assert selinux_facts._fact_ids == set()

# Generated at 2022-06-13 03:28:22.851840
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    collector = SelinuxFactCollector()

    assert collector.name == 'selinux'
    assert not collector.device
    assert not collector.device_serial
    assert collector.collector == 'selinux'
    assert collector.sysname_factor == 'selinux'
    assert collector._fact_ids == set(['selinux', 'selinux_python_present'])

# Generated at 2022-06-13 03:28:23.878548
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    s = SelinuxFactCollector()
    assert s.name == 'selinux'

# Generated at 2022-06-13 03:28:25.580453
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    assert SelinuxFactCollector().name == 'selinux'
    obj = SelinuxFactCollector()
    assert obj.name == 'selinux'


# Generated at 2022-06-13 03:28:36.478924
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():

    # Initialize instances of module_utils.selinux.selinux and fact class
    module_selinux = selinux
    fact_collector = SelinuxFactCollector()

    # Initialize the collected_facts dict
    collected_facts = dict()

    # Set value of the is_selinux_enabled function of the selinux module
    module_selinux.is_selinux_enabled = lambda: True

    # Set the value of the security_getenforce function of the selinux module
    module_selinux.security_getenforce = lambda: 1

    # Set the value of the security_policyvers function of the selinux module
    module_selinux.security_policyvers = lambda: '28'

    # Set the output of the selinux_getpolicytype function of the selinux module
    module_selin

# Generated at 2022-06-13 03:28:42.433011
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_facts = SelinuxFactCollector().collect()

    # Check if selinux_python_present is True as the selinux library is
    # mocked and installed.
    assert selinux_facts['selinux_python_present'] == True

    # Check if selinux library is present and working.
    if HAVE_SELINUX:
        assert selinux_facts['selinux']['mode'] in SELINUX_MODE_DICT.values()
        assert selinux_facts['selinux']['config_mode'] in SELINUX_MODE_DICT.values()
        assert selinux_facts['selinux']['status'] == 'disabled' or selinux_facts['selinux']['status'] == 'enabled'

# Generated at 2022-06-13 03:28:45.678971
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux_collector = SelinuxFactCollector()
    assert selinux_collector.name == 'selinux'
    assert selinux_collector._fact_ids == set([''])

# Generated at 2022-06-13 03:28:48.219227
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():

    selinux_fact_collector = SelinuxFactCollector()
    assert selinux_fact_collector.name == "selinux"
    assert selinux_fact_collector.collect() is not None

# Generated at 2022-06-13 03:28:57.599472
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # Save the selinux.is_selinux_enabled method in order
    # to be restored after the test
    saved_is_selinux_enabled = selinux.is_selinux_enabled

    # Mock the selinux.is_selinux_enabled method to always return
    # True (selinux enabled)
    def mock_is_selinux_enabled():
        return True

    selinux.is_selinux_enabled = mock_is_selinux_enabled

    # Save the selinux.security_policyvers method in order
    # to be restored after the test
    saved_security_policyvers = selinux.security_policyvers

    # Mock the selinux.security_policyvers method to always return
    # 2 in order to emulate a modern selinux policy
    def mock_security_policyvers():
        return 2

# Generated at 2022-06-13 03:28:58.541148
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    x = SelinuxFactCollector()
    assert x

# Generated at 2022-06-13 03:30:26.922981
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    selinux_facts_list = {
        'selinux': {
            'config_mode': 'disabled',
            'mode': 'disabled',
            'policyvers': '26',
            'status': 'enabled',
            'type': 'targeted'
        },
        'selinux_python_present': True
    }

    # Mock selinux
    selinux.is_selinux_enabled = MagicMock(return_value=True)
    selinux.selinux_getenforcemode = MagicMock(return_value=(0, 1))
    selinux.selinux_getpolicytype = MagicMock(return_value=(0, 'targeted'))
    selinux.security_getenforce = MagicMock(return_value=1)

# Generated at 2022-06-13 03:30:30.155616
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    """
    Test to make sure the constructor for the class works
    """
    obj = SelinuxFactCollector()
    assert isinstance(obj, SelinuxFactCollector)

# Generated at 2022-06-13 03:30:31.642528
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    o = SelinuxFactCollector()
    assert o.name == 'selinux'
    assert 'selinux' in o._fact_ids

# Generated at 2022-06-13 03:30:32.018412
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    pass

# Generated at 2022-06-13 03:30:36.364025
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    mock_module = Mock()
    selinux_fact_collector = SelinuxFactCollector()

    # set missing selinux library
    selinux_fact_collector.collect(mock_module, None)
    assert selinux_fact_collector.collect(mock_module, None) == {
        'selinux_python_present': False,
        'selinux': {'status': 'Missing selinux Python library'}}

    # set selinux library
    selinux_fact_collector.collect(mock_module, None)

# Generated at 2022-06-13 03:30:45.720476
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    fact_collector = SelinuxFactCollector()

# Generated at 2022-06-13 03:30:46.818731
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    # verify that the class can be instantiated
    SelinuxFactCollector()

# Generated at 2022-06-13 03:30:49.314185
# Unit test for constructor of class SelinuxFactCollector
def test_SelinuxFactCollector():
    selinux = SelinuxFactCollector()
    assert selinux.name == 'selinux'

# Generated at 2022-06-13 03:30:57.209874
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    # Note: For unit test to work, execute tests under the directory containing this file
    #       e.g. ansible/test/units/module_utils/facts/collectors/network/ipv4.py
    #
    # When tests are run in isolation, the Ansible module_utils directory is not added
    # to the pythonpath and python interpreter is unable to load the module and therefore
    # throws import error.
    #
    # By executing unit tests under the directory containing this file, python interpreter
    # will be able to import module_utils.compat.selinux
    fact_collector = SelinuxFactCollector()
    collected_facts = fact_collector.collect()
    assert collected_facts['selinux_python_present']
    assert collected_facts['selinux']['status']

# Generated at 2022-06-13 03:31:01.919516
# Unit test for method collect of class SelinuxFactCollector
def test_SelinuxFactCollector_collect():
    mock_module = 'module'
    mock_collected_facts = {}
    selinux_facts = {'status': 'enabled',
                     'config_mode': 'enforcing',
                     'mode': 'enforcing',
                     'type': 'targeted',
                     'policyvers': '28',
                     }

    SELinuxFactCollector.collect(mock_module, mock_collected_facts)

    assert mock_collected_facts['selinux_python_present']
    assert mock_collected_facts['selinux'] == selinux_facts