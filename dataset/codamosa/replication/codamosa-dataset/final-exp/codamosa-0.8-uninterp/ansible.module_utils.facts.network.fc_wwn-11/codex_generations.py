

# Generated at 2022-06-13 01:27:43.227149
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    import sys
    sys.modules['ansible'] = type('module', (), {})
    sys.modules['ansible.module_utils'] = type('module', (), {})
    sys.modules['ansible.module_utils.facts'] = type('module', (), {})
    sys.modules['ansible.module_utils.facts.utils'] = type('module', (), {})
    sys.modules['ansible.module_utils.facts.collector'] = type('module', (), {})
    sys.modules['ansible.module_utils.facts.collector'].BaseFactCollector = type('class', (), {})
    if sys.platform.startswith('linux'):
        sys.modules['ansible.module_utils.facts'].get_file_lines = lambda x: ['0x1234567890abcdef']

# Generated at 2022-06-13 01:27:45.870501
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_fact = FcWwnInitiatorFactCollector()
    assert fc_fact is not None


# Generated at 2022-06-13 01:27:47.019012
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    FcWwnInitiatorFactCollector()

# Generated at 2022-06-13 01:27:50.887781
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    try:
        fc_facts = FcWwnInitiatorFactCollector()
        assert fc_facts is not None
    except:
        raise
    assert fc_facts.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:27:55.876464
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():

    from ansible.module_utils.facts import Collector

    #  Create a dummy module instance
    module = type('', (), {
                'run_command': run_command,
                'get_bin_path': get_bin_path,
                })()

    # create a dummy Collector class and register our fact collector to it
    c = Collector(module=module)
    c.register_collector(FcWwnInitiatorFactCollector())

    # Gather facts and return the result
    facts = c.get_facts()
    assert(facts['ansible_facts']['fibre_channel_wwn'] == ['20000001bad1dea1'])

# Dummy method for module run_command

# Generated at 2022-06-13 01:28:01.366276
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fcwwninitiatorfactcollector = FcWwnInitiatorFactCollector()
    assert fcwwninitiatorfactcollector.name ==  "fibre_channel_wwn"
    assert fcwwninitiatorfactcollector._fact_ids == set()

# Generated at 2022-06-13 01:28:06.961265
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    fcinfo = FcWwnInitiatorFactCollector()
    res = fcinfo.collect()
    assert isinstance(res, dict)
    assert isinstance(res['fibre_channel_wwn'], list)
    assert len(res['fibre_channel_wwn']) > 0
    assert len(res['fibre_channel_wwn'][0]) > 0

# Generated at 2022-06-13 01:28:17.734323
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():

    test_platforms = ['Linux', 'SunOS', 'AIX', 'HP-UX']
    test_fcs = [
        {
            'fibre_channel_wwn': ['0x21000014ff52a9bb', '0x21000014ff52bbce']
        },
        {
            'fibre_channel_wwn': ['21000014ff52a9bb', '21000014ff52bbce']
        },
        {
            'fibre_channel_wwn': ['10000090fa1658de']
        },
        {
            'fibre_channel_wwn': ['10000090FA551509']
        },
        {
            'fibre_channel_wwn': ['0x50060b00006975ec']
        }
    ]

    # mock module

# Generated at 2022-06-13 01:28:19.809700
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    collect_fc_facts = FcWwnInitiatorFactCollector()
    assert(type(collect_fc_facts) is FcWwnInitiatorFactCollector)

# Generated at 2022-06-13 01:28:30.548934
# Unit test for method collect of class FcWwnInitiatorFactCollector

# Generated at 2022-06-13 01:28:50.562891
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():

    collector = FcWwnInitiatorFactCollector()
    if sys.platform.startswith('linux'):
        for fcfile in glob.glob('/sys/class/fc_host/*/port_name'):
            with open(fcfile) as f:
                expected_result = f.read().strip('\n')[2:]
                result = collector.collect()
                assert expected_result in result['fibre_channel_wwn']

# Generated at 2022-06-13 01:28:57.557303
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector.fibre_channel_wwn_initiator import FcWwnInitiatorFactCollector
    BaseFactCollector._load_collectors(collector)
    c = FcWwnInitiatorFactCollector()
    assert c.name == 'fibre_channel_wwn'
    assert c._fact_ids == set()
    assert c.collect() == {}

# Generated at 2022-06-13 01:29:00.643243
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    obj = FcWwnInitiatorFactCollector('fibre_channel_wwn', set())
    assert obj.name == 'fibre_channel_wwn'


# Generated at 2022-06-13 01:29:01.619923
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    assert FcWwnInitiatorFactCollector()

# Generated at 2022-06-13 01:29:13.026003
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.collectors.network import NetworkCollector
    from ansible.module_utils.facts.collectors.hardware.fc_wwn_initiator import FcWwnInitiatorFactCollector
    import platform
    import sys

    # create a mock module object
    mock_module = type('AnsibleModule', (), {})()
    mock_module.get_bin_path = lambda *args, **kwargs: 'mock_path'

    mock_module.run_command = lambda *args, **kwargs: (0, "", "")

# Generated at 2022-06-13 01:29:21.992014
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fact_collector = FcWwnInitiatorFactCollector()
    facts = fact_collector.collect()
    print(facts)
    assert 'fibre_channel_wwn' in facts
    assert type(facts['fibre_channel_wwn']) is list
    for wwn in facts['fibre_channel_wwn']:
        # 16 characters (8byte for vpci and 8byte for vnpi)
        assert len(wwn) == 16

if __name__ == '__main__':
    test_FcWwnInitiatorFactCollector()

# Generated at 2022-06-13 01:29:26.282039
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    fcwwnfc = FcWwnInitiatorFactCollector()
    # Method collect must return dict type object
    assert isinstance(fcwwnfc.collect(), dict)

if __name__ == '__main__':
    test_FcWwnInitiatorFactCollector_collect()

# Generated at 2022-06-13 01:29:29.996532
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    facts_collector = FcWwnInitiatorFactCollector()
    assert facts_collector.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:29:42.227884
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    class TestModule(object):
        def get_bin_path(self, name, opt_dirs=[]):
            return name
    testmodule = TestModule()

    class TestFactCollector(FcWwnInitiatorFactCollector):
        def collect(self, collected_facts=None):
            return self.get_fq_class_name()

    class TestCollectedFacts(object):
        def __init__(self):
            self._dict = {'fibre_channel_wwn': ['210000144c90b826', '210000144c90b828']}

    testfacts = TestCollectedFacts()

    class TestAnsibleModule(object):
        def __init__(self, args):
            self.args = args


# Generated at 2022-06-13 01:29:49.043216
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_collector = FcWwnInitiatorFactCollector()
    assert fc_collector.name == 'fibre_channel_wwn', 'Expected name "fibre_channel_wwn", but got %s' % fc_collector.name
    assert 'fibre_channel_wwn' in fc_collector._fact_ids, 'Expected _fact_ids to contain "fibre_channel_wwn", but got %s' % fc_collector._fact_ids

# Generated at 2022-06-13 01:30:21.705738
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts import ModuleFacts, MOCK_LINUX, MOCK_SOLARIS10, MOCK_SOLARIS11, MOCK_AIX, MOCK_HPUX
    from ansible.module_utils.facts.modules.fibre_channel_wwn import FactsCollector
    module_facts = ModuleFacts(FactsCollector, [FcWwnInitiatorFactCollector])
    # run collect from FcWwnInitiatorFactCollector
    result = FcWwnInitiatorFactCollector().collect(module=module_facts.module, collected_facts=module_facts.collected_facts)

# Generated at 2022-06-13 01:30:23.303412
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    assert isinstance(FcWwnInitiatorFactCollector(), FcWwnInitiatorFactCollector)

# Generated at 2022-06-13 01:30:25.604749
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():

    test_collector = FcWwnInitiatorFactCollector()
    assert test_collector.name == 'fibre_channel_wwn'
    assert test_collector.collect()

# Generated at 2022-06-13 01:30:28.356383
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_wwn_obj = FcWwnInitiatorFactCollector()
    assert fc_wwn_obj.name == 'fibre_channel_wwn'


# Generated at 2022-06-13 01:30:29.748326
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    FcWwnInitiatorFactCollector()


# Generated at 2022-06-13 01:30:40.639211
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """
    The fc_facts are collected.
    """

    # Create a fake module
    import ansible.module_utils.facts.collector
    moduleUtils = ansible.module_utils.facts.collector
    import ansible.module_utils.facts.collector
    class FakeModule(object):
        def get_bin_path(self, exe, opt_dirs=[]):
            if exe == 'fcinfo':
                return '/usr/sbin/fcinfo'
            elif exe == 'lsdev':
                return '/usr/sbin/lsdev'
            elif exe == 'lscfg':
                return '/usr/sbin/lscfg'
            else:
                return None


# Generated at 2022-06-13 01:30:44.160515
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc = FcWwnInitiatorFactCollector()
    assert fc.name == 'fibre_channel_wwn'
    assert 'fibre_channel_wwn' in fc._fact_ids

# Generated at 2022-06-13 01:30:46.025335
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    # Unit test - check if class is created properly
    x = FcWwnInitiatorFactCollector()
    assert x is not None

# Generated at 2022-06-13 01:30:53.483089
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    # initialize instance of class FcWwnInitiatorFactCollector
    fc_wwn_initiator_fact_collector = FcWwnInitiatorFactCollector()
    assert fc_wwn_initiator_fact_collector.name == 'fibre_channel_wwn'
    assert fc_wwn_initiator_fact_collector._fact_ids == set()

    # test method collect
    # todo: mock the calls to run_command

# Generated at 2022-06-13 01:30:55.473398
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    test_facts = {}
    result = FcWwnInitiatorFactCollector.collect(collected_facts=test_facts)
    assert isinstance(result, dict)
    assert 'fibre_channel_wwn' in result

# Generated at 2022-06-13 01:31:27.224691
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """ Test method collect """
    fc_facts = FcWwnInitiatorFactCollector().collect(module, collected_facts)
    print("##########")
    print("fibre_channel_wwn: %s" % fc_facts['fibre_channel_wwn'])
    assert fc_facts['fibre_channel_wwn'] is not None
    assert len(fc_facts['fibre_channel_wwn']) == 0

if __name__ == '__main__':
    # just run unit test
    if len(sys.argv) > 1 and sys.argv[1] == 'unit_test':
        test_FcWwnInitiatorFactCollector_collect()

# Generated at 2022-06-13 01:31:39.189310
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():

    # initialize class object
    fc_wwn_initiator_module = FcWwnInitiatorFactCollector()
    # mock module class, including methods is_system_platform_solaris and run_command
    class MockModule(object):
        def __init__(self):
            self.params = {}
            self.facts = {}

        def run_command(self, module):
            return(0, 'Mock Command output', None)

        def get_bin_path(self, command):
            return '/usr/bin/ls'

    # mock module object that can be called inside of the method
    module = MockModule()
    # run the collect method
    facts = fc_wwn_initiator_module.collect(module)

    assert facts['fibre_channel_wwn'] == []

# Unit

# Generated at 2022-06-13 01:31:47.168616
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():

    # create a mock module object
    class MockModule():
        def get_bin_path(self, arg, **kwargs):
            if 'lscfg' in arg:
                return '/usr/sbin/lscfg'
            if 'ioscan' in arg:
                return '/usr/sbin/ioscan'
            if 'fcmsutil' in arg:
                return '/opt/fcms/bin/fcmsutil'
            if 'fcinfo' in arg:
                return '/usr/sbin/fcinfo'

# Generated at 2022-06-13 01:31:54.617003
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    # set up
    FcWwnInitiatorFactCollector._fact_ids.clear()
    fcwwn_fc = FcWwnInitiatorFactCollector()
    fcwwn_fc._module = FakeModule()
    # test
    result = fcwwn_fc.collect()
    # verify
    assert set(FcWwnInitiatorFactCollector._fact_ids) == set([])
    assert result == {
        'ansible_fibre_channel_wwn': ['1262390000000123', '1262390000001234']
    }


# Generated at 2022-06-13 01:32:06.806037
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts.hardware.fibre_channel_wwn import FcWwnInitiatorFactCollector
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils._text import to_text
    from ansible.module_utils.basic import AnsibleModule

    class MockModule(object):
        def __init__(self, params):
            self.params = params
            self._ansible_module = None

        def get_bin_path(self, arg, opt_dirs=[]):
            return ':memory:'


# Generated at 2022-06-13 01:32:08.692513
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """
    Unit test for method collect of class FcWwnInitiatorFactCollector
    """

    pass

# Generated at 2022-06-13 01:32:11.854847
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc = FcWwnInitiatorFactCollector()
    assert fc.name == 'fibre_channel_wwn'
    assert fc.collect() == {}


# Generated at 2022-06-13 01:32:13.097988
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    FcWwnInitiatorFactCollector()

# Generated at 2022-06-13 01:32:15.679954
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fake_module = type('module', (), {})
    collector = FcWwnInitiatorFactCollector(fake_module)
    assert collector.name == 'fibre_channel_wwn'
    assert collector._fact_ids == set()

# Generated at 2022-06-13 01:32:18.359158
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc = FcWwnInitiatorFactCollector()
    assert fc.name == 'fibre_channel_wwn'
    assert fc._fact_ids == set(['fibre_channel_wwn'])

# Generated at 2022-06-13 01:32:43.881828
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc = FcWwnInitiatorFactCollector()
    assert fc.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:32:51.232361
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils.facts.collector import BaseFactCollector

    global fc_facts
    class FakeModule:
        def __init__(self):
            pass
        def get_bin_path(self):
            return "/usr/bin/fakebin"
        def run_command(self):
            return 0, "fakecmd output", "fakecmd error"

    # instantiate class to be tested
    fc_fact_collector = get_collector_instance(FcWwnInitiatorFactCollector)
    # check type
    assert isinstance(fc_fact_collector, BaseFactCollector)
    # run the collection
    fake_module = FakeModule()
    fc_facts = fc_fact_collector

# Generated at 2022-06-13 01:32:58.148578
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    test_module = AnsibleModule(argument_spec={})
    # Create a new isntance of FcWwnInitiatorFactCollector
    test_object = FcWwnInitiatorFactCollector()
    # create test facts dict
    test_facts = {}
    # Call the method collect of the class FcWwnInitiatorFactCollector
    result = test_object.collect(None, test_facts)
    # Test if the returned facts dict matches what is expected
    assert result == {'fibre_channel_wwn': []}


# Generated at 2022-06-13 01:33:02.514990
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    # Code that instantiates the class to be tested
    fc_facts = FcWwnInitiatorFactCollector()
    # If your code instantiates the class properly.
    # The if statement passes.
    assert isinstance(fc_facts, FcWwnInitiatorFactCollector)
    # If your code instantiates the class with the wrong Parameter.
    # The except statement passes.
    try:
        fc_facts = FcWwnInitiatorFactCollector('xxx')
    except TypeError:
        assert True

# Generated at 2022-06-13 01:33:12.535931
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """Unit test for method FcWwnInitiatorFactCollector.collect"""

    # Create a class instance.
    fc_wwn_initiator_fc = FcWwnInitiatorFactCollector()
    # Define a dummy module.
    module = type('', (), {})()
    # Define the get_bin_path method of the dummy module. This is required in
    # case of sunos.
    def get_bin_path(self, exe, opt_dirs=[]):
        if exe == 'fcinfo':
            return 'dummy_fcinfo'
        else:
            return None
    module.get_bin_path = get_bin_path
    # Define the run_command method of the dummy module. This is required in
    # case of sunos.

# Generated at 2022-06-13 01:33:18.730206
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    # prepare mocks for module and facts
    mock_module = Mock(function=['run_command', 'get_bin_path'])
    mock_facts = dict()

    # mock run_command to return fcinfo -a output as if running on solaris 10 or later
    mock_module.run_command.return_value = (0, "HBA Port WWN: 10000090fa1658de\n", "")

    # define fcinfo command
    mock_module.get_bin_path.return_value = "/usr/sbin/fcinfo"

    # instantiate fact class
    fcwwn = FcWwnInitiatorFactCollector()

    # retrieve facts
    fcwwn.collect(module=mock_module, collected_facts=mock_facts)

    # make sure the fact 'fibre

# Generated at 2022-06-13 01:33:22.898783
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """
    Unit test for method collect of class FcWwnInitiatorFactCollector
    """
    data = {}
    data['ansible_module_loaded'] = True
    test_object = FcWwnInitiatorFactCollector(None, data, None)
    test_result_dict = test_object.collect()
    assert 'fibre_channel_wwn' in test_result_dict
    assert isinstance(test_result_dict['fibre_channel_wwn'], list)

if __name__ == "__main__":
    test_FcWwnInitiatorFactCollector_collect()

# Generated at 2022-06-13 01:33:29.277968
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    from ansible.module_utils import basic
    from ansible.module_utils.facts import collector

    def _get_mock_module():
        mock_module = basic.AnsibleModule(
            argument_spec=dict()
        )
        return mock_module

    fc = FcWwnInitiatorFactCollector(_get_mock_module(), {})
    assert fc.name == 'fibre_channel_wwn'


# Generated at 2022-06-13 01:33:40.015928
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    import sys
    import os
    import platform
    import pytest

    # sys module is patched in conftest.py
    if sys.platform.startswith('linux'):
        sys.platform = 'linux'
    else:
        sys.platform = 'sunos'

    module = pytest.fixtures.create_module()
    module.get_bin_path = lambda *args, **kwargs: 'cmd'
    config = {'custom_class': 'FcWwnInitiatorFactCollector'}
    fcfc = FcWwnInitiatorFactCollector(config)
    fcfc.collect(module=module)
    res = fcfc.collect(module=module)
    assert res['fibre_channel_wwn'] == ['21000014ff52a9bb']

# Generated at 2022-06-13 01:33:44.299179
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    FcWwnInitiatorFactCollector = FcWwnInitiatorFactCollector()
    assert FcWwnInitiatorFactCollector.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:34:35.569743
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_wwn_initiator_fact_collector_obj = FcWwnInitiatorFactCollector()
    assert fc_wwn_initiator_fact_collector_obj.name == "fibre_channel_wwn"
    assert fc_wwn_initiator_fact_collector_obj.collect() == {}

# Generated at 2022-06-13 01:34:44.640494
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    # Create an instance of class FcWwnInitiatorFactCollector
    collector = FcWwnInitiatorFactCollector()

    # Generate a dummy module
    module = DummyModule()

    # Generate a dummy collected_facts
    collected_facts = {}

    # Call method collect of class FcWwnInitiatorFactCollector
    facts = collector.collect(module, collected_facts)

    # Verify content of facts
    assert 'fibre_channel_wwn' in facts
    if sys.platform.startswith('linux'):
        assert len(facts['fibre_channel_wwn']) == 2
    elif sys.platform.startswith('sunos'):
        assert len(facts['fibre_channel_wwn']) == 1

# Generated at 2022-06-13 01:34:52.949285
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.collector.fibre_channel_wwn_initiator import FcWwnInitiatorFactCollector

    # We need to register the collector for the FactCache to work!
    collector.register(FcWwnInitiatorFactCollector)

    # I think we can 'mock' the facts collector here.
    fc_fact_collector = FcWwnInitiatorFactCollector()

    fc_facts_dict = fc_fact_collector.collect()

    # Default should be empty!
    assert fc_facts_dict['fibre_channel_wwn'] == []

# Generated at 2022-06-13 01:34:55.543937
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    class_object = FcWwnInitiatorFactCollector()
    assert class_object is not None
    assert class_object.name == 'fibre_channel_wwn'


# Generated at 2022-06-13 01:35:00.187740
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_facts = FcWwnInitiatorFactCollector()
    assert fc_facts.name == 'fibre_channel_wwn'
    assert fc_facts._fact_ids == set()


# Generated at 2022-06-13 01:35:04.187465
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_facts = FcWwnInitiatorFactCollector()
    assert fc_facts.name == 'fibre_channel_wwn', "name is %s" % fc_facts.name
    assert len(fc_facts._fact_ids) == 0, "Fact ids is %s" % fc_facts._fact_ids

# Generated at 2022-06-13 01:35:07.664261
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fact_collector = FcWwnInitiatorFactCollector()
    assert fact_collector.name == 'fibre_channel_wwn'
    assert fact_collector._fact_ids == set()


# Generated at 2022-06-13 01:35:09.792371
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc = FcWwnInitiatorFactCollector()
    assert fc.name == 'fibre_channel_wwn'
    assert fc._fact_ids == set()

# Generated at 2022-06-13 01:35:13.112836
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    fc_facts = {}
    fc_facts['fibre_channel_wwn'] = [
        '21000014ff52a9bb',
        '10000090fa1658de',
        '10000090FA551509',
        '50060b00006975ec'
    ]
    collector = FcWwnInitiatorFactCollector()
    facts = collector.collect()
    assert facts == fc_facts


# Generated at 2022-06-13 01:35:19.842260
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    # test class attribute name
    assert FcWwnInitiatorFactCollector.name == 'fibre_channel_wwn'

    # test class attribute _fact_ids
    assert FcWwnInitiatorFactCollector._fact_ids == set()

    # call method collect of class FcWwnInitiatorFactCollector
    # Note: use fake module for testing
    ansible_module = AnsibleFakeModule(collect_facts=False)
    fc_facts = FcWwnInitiatorFactCollector.collect(ansible_module)
    output = {}
    if sys.platform.startswith('linux'):
        output = {'fibre_channel_wwn':['21000014ff52a9bb']}