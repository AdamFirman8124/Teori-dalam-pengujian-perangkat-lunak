

# Generated at 2022-06-13 01:27:32.821470
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_collector = FcWwnInitiatorFactCollector()
    assert fc_collector.name == 'fibre_channel_wwn'
    assert fc_collector._fact_ids == set()

# Generated at 2022-06-13 01:27:36.406546
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fact_collector = FcWwnInitiatorFactCollector()
    assert fact_collector.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:27:42.656677
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_facts = FcWwnInitiatorFactCollector()
    expected = FcWwnInitiatorFactCollector.name
    assert fc_facts.name == expected
    assert sorted(fc_facts.collect().keys()) == sorted(['fibre_channel_wwn'])

if __name__ == '__main__':
    print(FcWwnInitiatorFactCollector().collect())


from ansible.module_utils.facts.utils import get_file_lines
from ansible.module_utils.facts.collector import BaseFactCollector



# Generated at 2022-06-13 01:27:53.600252
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """This is a unit test for method collect of class FcWwnInitiatorFactCollector."""
    # create an instance of class FcWwnInitiatorFactCollector
    fc_collector = FcWwnInitiatorFactCollector()

    # create a mock module object
    fake_module = type('module', (object,), {'run_command': mock_run_command,
                                             'get_bin_path': mock_get_bin_path})

    # perform the test
    result_array = fc_collector.collect(fake_module)

    # check if the wwn's are collected correctly
    assert 'ansible-test1-wwn' in result_array['fibre_channel_wwn']

# Generated at 2022-06-13 01:28:02.406875
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    import sys
    sys.modules['ansible'] = __import__('mock')
    fc_facts = FcWwnInitiatorFactCollector()
    fc_info = fc_facts.collect()
    print("fc_info: {0}".format(fc_info))
    assert 'fibre_channel_wwn' in fc_info

if __name__ == '__main__':
    test_FcWwnInitiatorFactCollector_collect()

# Generated at 2022-06-13 01:28:06.608311
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    FcWwnInitiatorFactCollector = FcWwnInitiatorFactCollector()
    assert FcWwnInitiatorFactCollector.collect() == {
        'fibre_channel_wwn': [
            '21000014FF52A9BB',
        ]
    }

# Generated at 2022-06-13 01:28:09.153257
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fw = FcWwnInitiatorFactCollector()
    assert fw.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:28:12.575967
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    """ construct an instance (in memory) of class FcWwnInitiatorFactCollector """
    instance = FcWwnInitiatorFactCollector()
    assert instance


# Generated at 2022-06-13 01:28:16.491085
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
  fc_wwn = FcWwnInitiatorFactCollector()
  facts = {'ansible_facts': {}}
  fc_wwn.collect(module=None, collected_facts=facts)
  assert facts['ansible_facts']['fibre_channel_wwn'] == []

# Generated at 2022-06-13 01:28:20.748862
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    x = FcWwnInitiatorFactCollector()
    assert x.name == 'fibre_channel_wwn'
    assert x._fact_ids == set()


# Generated at 2022-06-13 01:28:44.854958
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    pass

# Generated at 2022-06-13 01:28:49.995105
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_wwn_fact_collector = FcWwnInitiatorFactCollector()
    assert fc_wwn_fact_collector.name == 'fibre_channel_wwn'
    assert fc_wwn_fact_collector._fact_ids == set()

# Generated at 2022-06-13 01:28:54.586508
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    # create instance of FcWwnInitiatorFactCollector
    fc_sut = FcWwnInitiatorFactCollector()
    # perform the test (TBD)
    res = fc_sut.collect()
    # check the result
    assert len(res['fibre_channel_wwn']) > 0

# Generated at 2022-06-13 01:28:55.214311
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    pass

# Generated at 2022-06-13 01:28:57.667229
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    fwinit_fc = FcWwnInitiatorFactCollector()
    assert fwinit_fc.collect() == {'fibre_channel_wwn': ['21000014ff52a9bb']}

# Generated at 2022-06-13 01:29:08.425855
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    import ansible.module_utils.facts.collectors.fibre_channel_wwn as test_obj

    # Set up test environment
    fc_facts = {'fibre_channel_wwn': ['21000014ff52a9bb']}

    # Test1: execute collect
    # Rearrange
    module = object
    collector = test_obj.FcWwnInitiatorFactCollector()
    # Act
    hostvars = collector.collect()
    # Assert
    assert hostvars == fc_facts

    # Test2: execute collect on platform other than linux
    # Rearrange
    module = object
    collector = test_obj.FcWwnInitiatorFactCollector()
    # Act
    hostvars = collector.collect()
    # Assert
    assert hostvars == {}

# Generated at 2022-06-13 01:29:15.741410
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    class MockModule():
        def __init__(self):
            pass
        def get_bin_path(self, arg, opt_dirs=None):
            return arg
    class MockCollector():
        def __init__(self):
            pass
    test_input = MockModule()
    test_collector = MockCollector()
    test_obj = FcWwnInitiatorFactCollector(test_input, test_collector)
    assert(test_obj.name == "fibre_channel_wwn")
    assert(test_obj.collect() == {})

# Generated at 2022-06-13 01:29:25.760211
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    import sys
    import tempfile
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode=True
    )
    tmp_dir = tempfile.gettempdir()
    sys.path.append(tmp_dir)
    # fake sys.platform for different systems
    sys.platform = 'linux'
    fc_collector = FcWwnInitiatorFactCollector()
    fc_collector.collect(module=module)
    # create fake file with fc data
    open(tmp_dir+'/sys/class/fc_host/host0/port_name', 'a').close()
    open(tmp_dir+'/sys/class/fc_host/host1/port_name', 'a').close()

# Generated at 2022-06-13 01:29:29.901236
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    # TODO need to add unit test for this
    fcfact = FcWwnInitiatorFactCollector()
    fcfact.collect()


# Generated at 2022-06-13 01:29:42.124124
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts.collector import FactsCollector
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector import FactsParseException
    from ansible.module_utils.facts import timeout
    import ansible.module_utils.facts.timeout
    import ansible.module_utils.facts.timeout.FcWwnInitiatorFactCollector
    import sys
    import mock


# Generated at 2022-06-13 01:30:16.044742
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """
    Unit test for method ansible.module_utils.facts.collectors.fibre_channel_wwn.FcWwnInitiatorFactCollector.collect
    """
    test_cases = ()
    from ansible.module_utils.facts.collectors.fibre_channel_wwn import FcWwnInitiatorFactCollector
    for test_case in test_cases:
        collected_facts = FcWwnInitiatorFactCollector.collect(test_case[0])
        if collected_facts != test_case[1]:
            print("Expected result %s but got %s" % (test_case[1], collected_facts))
            return False
    return True

# Generated at 2022-06-13 01:30:18.211561
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    collector = FcWwnInitiatorFactCollector()
    result = collector.collect()
    assert 'fibre_channel_wwn' in result

# Generated at 2022-06-13 01:30:22.371233
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    # Create a FcWwnInitiatorFactCollector instance
    obj = FcWwnInitiatorFactCollector()
    rc = obj.collect()
    print (rc)

if __name__ == "__main__":
    test_FcWwnInitiatorFactCollector_collect()

# Generated at 2022-06-13 01:30:25.713230
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_collector = FcWwnInitiatorFactCollector()
    assert fc_collector.name == "fibre_channel_wwn"
    assert fc_collector._fact_ids == set(['fibre_channel_wwn'])

# Generated at 2022-06-13 01:30:27.491287
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    f = FcWwnInitiatorFactCollector()
    assert f.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:30:32.733561
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts.collector import get_collectors_facts_for
    fcwwn_facts_dict = get_collectors_facts_for('fibre_channel_wwn')
    print(fcwwn_facts_dict)
    assert fcwwn_facts_dict.get('fibre_channel_wwn') is not None


if __name__ == '__main__':
    test_FcWwnInitiatorFactCollector_collect()

# Generated at 2022-06-13 01:30:41.176788
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    """
    This test is only for class FcWwnInitiatorFactCollector
    """
    from ansible.module_utils.facts.collector import collector_registry
    from ansible.module_utils.facts.collector import BaseFactCollector
    my_obj = FcWwnInitiatorFactCollector()
    assert isinstance(my_obj, BaseFactCollector)
    assert 'fibre_channel_wwn' == my_obj.name
    assert my_obj in collector_registry._fact_collectors


# Generated at 2022-06-13 01:30:45.657793
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    # create instance
    FcWwnInitiatorFactCollector = FcWwnInitiatorFactCollector()
    # create output
    output = FcWwnInitiatorFactCollector.collect()
    # assert output is not empty
    assert output['fibre_channel_wwn']

# Generated at 2022-06-13 01:30:49.050741
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc = FcWwnInitiatorFactCollector()
    assert fc.name == 'fibre_channel_wwn'
    assert fc._fact_ids == set()

# Generated at 2022-06-13 01:30:58.692842
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    import platform
    import pytest
    import os

    if platform.system() == 'Linux':
        executor = os.environ.get('ANSIBLE_TEST_EXECUTOR', 'local')
        if executor == 'local':
            pytest.skip("Test is not applicable for local executor")

        __import__('ansible_collections.notmintest.not_a_real_collection.plugins.module_utils.facts.collectors.network.fc_wwn')

        module = FakeModule('TEST_MODULE')
        fc = FcWwnInitiatorFactCollector()

        assert fc.collect(module) == {'fibre_channel_wwn': ['21000014ff52a9bb']}



# Generated at 2022-06-13 01:31:51.379953
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    import sys
    import platform

    fcwwnfc = FcWwnInitiatorFactCollector()
    assert fcwwnfc.name == 'fibre_channel_wwn'
    assert 'fibre_channel_wwn' in fcwwnfc.collect()


if __name__ == '__main__':
    test_FcWwnInitiatorFactCollector()

# Generated at 2022-06-13 01:31:54.574455
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fact_collector = FcWwnInitiatorFactCollector()
    assert fact_collector.name == 'fibre_channel_wwn'
    assert fact_collector._fact_ids == set()


# Generated at 2022-06-13 01:31:59.138889
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    # WIP
    print('test_FcWwnInitiatorFactCollector_collect not implemented')
    assert True

# Generated at 2022-06-13 01:32:05.496358
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    from ansible.module_utils.facts import collector

    collected_facts = collector.collector.get_collection_list()
    fc_coll = FcWwnInitiatorFactCollector()
    assert isinstance(fc_coll, FcWwnInitiatorFactCollector)
    assert fc_coll.name == "fibre_channel_wwn"

# Generated at 2022-06-13 01:32:07.698435
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    f = FcWwnInitiatorFactCollector()
    assert f.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:32:17.004371
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    class MockModule(object):
        def get_bin_path(self, arg1, arg2=None):
            if arg1 == 'fcinfo':
                return "/usr/sbin/fcinfo"
            elif arg1 == 'lsdev' and arg2 is None:
                return "/usr/sbin/lsdev"
            elif arg1 == 'lscfg' and arg2 is None:
                return "/usr/sbin/lscfg"
            elif arg1 == 'ioscan' and arg2 is None:
                return "/usr/sbin/ioscan"
            elif arg1 == 'fcmsutil' and arg2 == ['/opt/fcms/bin']:
                return "/opt/fcms/bin/fcmsutil"


# Generated at 2022-06-13 01:32:24.850130
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    from ansible.module_utils.facts.collectors.network.fibre_channel import FcWwnInitiatorFactCollector
    from ansible.module_utils.facts.utils.fake import FakeModule
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.utils import get_file_lines
    import glob

    # Create dummy module
    module = FakeModule({})
    k = FcWwnInitiatorFactCollector()

    # Test common base class calls
    assert (k.name == 'fibre_channel_wwn')
    assert Collector.CACHEFILE_NAME not in k._cache
    assert k.can_run(module) == 'kernel'
    k.collect(module=module)
    assert Collector.CACHEFILE_NAME in k._

# Generated at 2022-06-13 01:32:32.536071
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.collector import BaseFactCollector

    fc_obj = FcWwnInitiatorFactCollector()
    # test for attributes of class FcWwnInitiatorFactCollector
    assert fc_obj.name == 'fibre_channel_wwn'
    assert fc_obj._fact_ids == set()
    assert isinstance(fc_obj, Collector)
    assert isinstance(fc_obj, BaseFactCollector)

    # test for overridden methods
    assert callable(fc_obj.collect)

# Generated at 2022-06-13 01:32:36.556318
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    """
    Unit test of class constructor FcWwnInitiatorFactCollector()
    :return:
    """
    fc_collector = FcWwnInitiatorFactCollector()
    assert(fc_collector.name == 'fibre_channel_wwn')


# Generated at 2022-06-13 01:32:43.419454
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """
    Test case class FcWwnInitiatorFactCollector: method collect

    """
    print("\ntest_FcWwnInitiatorFactCollector_collect")

    # test module class
    class AnsibleModuleFake:
        @staticmethod
        def get_bin_path(arg1, opt_dirs=None):
            testdata = {
                '/bin/lsdev': 'lsdev',
                '/bin/lscfg': 'lscfg',
                '/bin/ioscan': 'ioscan',
                '/opt/fcms/bin/fcmsutil': 'fcmsutil',
                '/usr/sbin/fcinfo': 'fcinfo',
            }
            return testdata[arg1]


# Generated at 2022-06-13 01:34:16.956773
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fcwwni = FcWwnInitiatorFactCollector()
    assert fcwwni != None

# Generated at 2022-06-13 01:34:25.683181
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    class module:
        def __init__(self, *args, **kwargs):
            pass
        def get_bin_path(self, module):
            if module == 'fcinfo':
                return 'fcinfo'
            elif module == 'lsdev':
                return 'lsdev'
            elif module == 'lscfg':
                return 'lscfg'
            elif module == 'ioscan':
                return 'ioscan'
            elif module == 'fcmsutil':
                return 'fcmsutil'
            return None
        def run_command(self, cmd):
            if cmd == "fcinfo hba-port":
                return (0,
                '''HBA Port WWN: 10000090fa1658de''',
                '')

# Generated at 2022-06-13 01:34:26.928798
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    FcWwnInitiatorFactCollector()

# Generated at 2022-06-13 01:34:29.060616
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_collector = FcWwnInitiatorFactCollector()
    assert fc_collector.name == 'fibre_channel_wwn'


# Generated at 2022-06-13 01:34:33.013125
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    f = FcWwnInitiatorFactCollector()
    assert f.name == 'fibre_channel_wwn'
    assert f.collect() == {'fibre_channel_wwn': []}

# Generated at 2022-06-13 01:34:41.477095
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    mock_module = MagicMock()
    mock_module.get_bin_path.side_effect = lambda x, opt_dirs: x
    mock_module.run_command.return_value = (0, '''
# fcinfo hba-port  | grep "Port WWN"
HBA Port WWN: 10000090fa1658de

''', '')
    # run the test
    fact_collector = FcWwnInitiatorFactCollector()
    facts = fact_collector.collect(module=mock_module)
    assert facts['fibre_channel_wwn'] == ['10000090fa1658de']

# Generated at 2022-06-13 01:34:51.418165
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.collectors import get_collector_names
    from ansible.module_utils.facts.collectors import get_collectors

    collector = Collector()
    collector.populate()
    names = get_collector_names()
    assert 'fibre_channel_wwn' in names
    assert collector.get_fact_names() == names
    for name in names:
        assert name in collector.get_fact_names()
    c_names = get_collector_names(collector_class=FcWwnInitiatorFactCollector)
    assert 'fibre_channel_wwn' in c_names
    assert len(c_names) == 1

# Generated at 2022-06-13 01:34:57.134191
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector

    # Create a Collector instance
    fc_collector = Collector.fetch_collector('fibre_channel_wwn')

    # Create a dummy module object instance
    class DummyModule:
        def __init__(self):
            self.params = dict()

        def get_bin_path(self, app, opt_dirs=[]):
            if app == 'fcinfo':
                return '/usr/sbin/fcinfo'
            if app == 'fcmsutil':
                return '/opt/fcms/bin/fcmsutil'
            if app == 'ioscan':
                return '/usr/sbin/ioscan'
            if app == 'lsdev':
                return '/usr/sbin/lsdev'

# Generated at 2022-06-13 01:35:02.409507
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts.collector.fc_wwn import FcWwnInitiatorFactCollector
    from ansible.module_utils.facts.utils import mock_module

    collector = FcWwnInitiatorFactCollector()
    module = mock_module()
    collected_facts = {}
    collector.collect(module, collected_facts)
    assert collected_facts == {}

# Generated at 2022-06-13 01:35:04.572990
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fcwwns = FcWwnInitiatorFactCollector()
    assert fcwwns.name == 'fibre_channel_wwn'
