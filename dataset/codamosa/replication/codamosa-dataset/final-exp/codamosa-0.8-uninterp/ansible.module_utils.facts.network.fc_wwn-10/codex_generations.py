

# Generated at 2022-06-13 01:27:31.556738
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts import fact_collector

    # read fact collector and set module and collected facts
    fact_collector.read_collection_directory('')
    fc_facts = {}

    # collect facts and check results
    fact_collector.collect(module=None, collected_facts=fc_facts)
    assert 'fibre_channel_wwn' in fc_facts

# Generated at 2022-06-13 01:27:35.333622
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    module = AnsibleModuleMock()
    collected_facts = {}
    fc = FcWwnInitiatorFactCollector()
    new_facts = fc.collect(module, collected_facts)
    assert isinstance(new_facts, dict)

# Generated at 2022-06-13 01:27:36.847221
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    test_obj = FcWwnInitiatorFactCollector()
    assert test_obj

# Generated at 2022-06-13 01:27:41.330187
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """
    Function to unit test method collect of class FcWwnInitiatorFactCollector
    """
    # create an object of class FcWwnInitiatorFactCollector
    fact_collector = FcWwnInitiatorFactCollector()
    facts_list = fact_collector.collect()
    assert facts_list is not None
    assert 'fibre_channel_wwn' in facts_list

# Generated at 2022-06-13 01:27:44.924130
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_facts = FcWwnInitiatorFactCollector()
    assert fc_facts.name == 'fibre_channel_wwn'
    assert len(fc_facts._fact_ids) == 0



# Generated at 2022-06-13 01:27:47.608268
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fcwwnfc = FcWwnInitiatorFactCollector()
    assert "fibre_channel_wwn" == fcwwnfc.name

# Generated at 2022-06-13 01:27:56.588782
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    def test_object_constructor():
        # create object instance of FcWwnInitiatorFactCollector class
        o_FcWwnInitiatorFactCollector = FcWwnInitiatorFactCollector()
        # get attributes of object
        print("o_FcWwnInitiatorFactCollector.name", o_FcWwnInitiatorFactCollector.name)
        assert o_FcWwnInitiatorFactCollector.name == "fibre_channel_wwn"
        print("o_FcWwnInitiatorFactCollector._fact_ids", o_FcWwnInitiatorFactCollector._fact_ids)
        assert o_FcWwnInitiatorFactCollector._fact_ids == set()

# Generated at 2022-06-13 01:27:58.708534
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fcWwnInitiatorFactCollector = FcWwnInitiatorFactCollector()
    assert isinstance(fcWwnInitiatorFactCollector, FcWwnInitiatorFactCollector)

# Unit test that fc_facts are collected on Linux system

# Generated at 2022-06-13 01:27:59.780941
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    collector = FcWwnInitiatorFactCollector()
    assert collector.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:28:04.013642
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    fc_facts = FcWwnInitiatorFactCollector().collect()
    assert(len(fc_facts['fibre_channel_wwn']) > 0)

if __name__ == '__main__':
    test_FcWwnInitiatorFactCollector_collect()

# Generated at 2022-06-13 01:28:28.124826
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fw = FcWwnInitiatorFactCollector()
    assert fw.name == 'fibre_channel_wwn'
    assert fw._fact_ids == set()

# Generated at 2022-06-13 01:28:34.939419
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    class mock_module:
        pass
    class mock_get_bin_path:
        def return_value(self,cmd, opt_dirs=None):
            return cmd + " path"
    fc = FcWwnInitiatorFactCollector()
    assert fc
    module = mock_module()
    module.get_bin_path = mock_get_bin_path()
    fc_facts = fc.collect(module)
    assert not fc_facts

# Generated at 2022-06-13 01:28:36.947250
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    my_object = FcWwnInitiatorFactCollector()
    assert my_object.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:28:41.008373
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    facts_module = FcWwnInitiatorFactCollector()
    # fact_id should be 'fibre_channel_wwn'
    assert facts_module.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:28:52.972102
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    '''
    test method collect of FcWwnInitiatorFactCollector
    '''
    # open a file containing some sample data
    lines = open('./fixture/test_FcWwnInitiatorFactCollector_collect', 'r')

    # create an object of class FcWwnInitiatorFactCollector and assign the fixture
    # file to its mock command module
    my_obj = FcWwnInitiatorFactCollector()
    my_obj.module.run_command = lambda *cmd, **kwargs: (0, lines, "")

    # run the collect method of object my_obj and get a dictionary
    ansible_facts = my_obj.collect()

    # assertions to make sure everything went well
    assert 'fibre_channel_wwn' in ansible_facts
    assert ansible

# Generated at 2022-06-13 01:29:01.352980
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    import os
    module = MagicMock()
    fcwwn_collector = FcWwnInitiatorFactCollector()
    facts_dict = {}
    # test on linux system
    facts_dict['kernel'] = 'Linux'
    if (facts_dict['kernel'] == 'Linux'):
        def mock_run_command(cmd, **kwargs):
            """
            fake helper for run_command
            """
            cmd_return  = "HBA Port WWN: 10000090fa1658e1\n"
            cmd_return += "HBA Port WWN: 10000090fa1658d2\n"
            cmd_return += "HBA Port WWN: 10000090fa1658d3\n"
            cmd_return += "HBA Port WWN: 10000090fa1658d4\n"

# Generated at 2022-06-13 01:29:03.517719
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_facts = FcWwnInitiatorFactCollector()
    assert fc_facts.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:29:07.511795
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    fc_facts = FcWwnInitiatorFactCollector().collect()
    if 'fibre_channel_wwn' in fc_facts:
        assert type(fc_facts['fibre_channel_wwn']) is list

# Generated at 2022-06-13 01:29:10.036333
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    from ansible.module_utils.facts.collector import Collector
    collector = FcWwnInitiatorFactCollector()
    assert isinstance(collector, Collector)

# Generated at 2022-06-13 01:29:18.430238
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    # set up a stub Module
    from ansible.module_utils.facts.collector import BaseFactCollector
    class ModuleStub():
        def __init__(self, platform_stub, run_command_stub, get_bin_path_stub):
            self.platform = platform_stub
            self.run_command = run_command_stub
            self.get_bin_path = get_bin_path_stub
            self.params = {}
            self._fail_json = lambda msg, **kwargs: dict(msg=msg, **kwargs)
            self.exit_json = lambda **kwargs: dict(**kwargs)
    # set up a stub BaseFactCollector

# Generated at 2022-06-13 01:29:41.856261
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fci = FcWwnInitiatorFactCollector()


# Generated at 2022-06-13 01:29:46.549379
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    # create test object of class FcWwnInitiatorFactCollector
    testobj = FcWwnInitiatorFactCollector()

    # test its name
    assert testobj.name == 'fibre_channel_wwn'

    # test its fact_ids
    assert testobj._fact_ids == set()

# Generated at 2022-06-13 01:29:52.344985
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    # import module snippets
    module = AnsibleModule(argument_spec=dict())
    fc = FcWwnInitiatorFactCollector()
    
    # execute method collect and check returned dictionary
    result = fc.collect(module)
    assert result['fibre_channel_wwn'] != None
    assert result['fibre_channel_wwn'] == ['21000014ff52a9bb']


# Import module snippets
from ansible.module_utils.basic import AnsibleModule
if __name__ == '__main__':
    main()

# Generated at 2022-06-13 01:29:54.795285
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    mm = FcWwnInitiatorFactCollector()
    assert mm.name == 'fibre_channel_wwn'



# Generated at 2022-06-13 01:30:01.615513
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    try:
        FcWwnInitiatorFactCollector()
    except NameError:
        print("NameError: name 'FcWwnInitiatorFactCollector' is not defined")
        sys.exit(1)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        sys.exit(1)
    else:
        print("Tested constructor of class FcWwnInitiatorFactCollector")
        sys.exit(0)


# Generated at 2022-06-13 01:30:09.705376
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = FcWwnInitiatorFactCollector()

    # Set property of parent class BaseFactCollector
    class _module_dummy:
        def __init__(self, path="", rc=0, err="", out=""):
            self.path = path
            self.rc = rc
            self.err = err
            self.out = out

        def run_command(self, cmd):
            return self.rc, self.out, self.err

        def get_bin_path(self, cmd, required=True, opt_dirs=[]):
            return self.path

    class _base_fact_collector_dummy:
        def __init__(self, module=None):
            self.module = module

    collector._base_

# Generated at 2022-06-13 01:30:10.688495
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    FcWwnInitiatorFactCollector()

# Generated at 2022-06-13 01:30:13.296858
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():

    fc_collector = FcWwnInitiatorFactCollector()
    assert fc_collector.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:30:14.657172
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    mytest = FcWwnInitiatorFactCollector()
    mytest.collect()

# Generated at 2022-06-13 01:30:20.476598
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts import munch
    from ansible.module_utils.facts import ansible_collector

    ansible_collector.collector._collected_facts = munch.Munch()
    fc_facts_collector = FcWwnInitiatorFactCollector()
    result = fc_facts_collector.collect()
    assert isinstance(result, dict)

# Generated at 2022-06-13 01:31:07.229428
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    a = FcWwnInitiatorFactCollector()
    assert a.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:31:09.653698
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_fact_collector = FcWwnInitiatorFactCollector()
    assert fc_fact_collector is not None


# Generated at 2022-06-13 01:31:17.592599
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    # Create a Mock of the AnsibleModule object
    import ansible.module_utils.facts.facts
    testmodule = ansible.module_utils.facts.facts.AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )
    # Test a linux system
    from ansible.module_utils.facts.platform.linux.fc_wwn_initiator import FcWwnInitiatorFactCollector
    fc_facts = FcWwnInitiatorFactCollector().collect(module=testmodule)
    assert len(fc_facts['fibre_channel_wwn']) >= 2
    # Test an AIX system
    from ansible.module_utils.facts.platform.aix.fc_wwn_initiator import FcWwnInitiatorFactCollector
    f

# Generated at 2022-06-13 01:31:19.724692
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc = FcWwnInitiatorFactCollector()
    assert fc.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:31:28.266483
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    # Test case: no FC device
    test_cases = [
        {'platform': 'linux2', 'lsdev_out': '', 'expected_result': []},
        {'platform': 'solaris', 'lsdev_out': '', 'expected_result': []},
        {'platform': 'aix', 'lsdev_out': '', 'expected_result': []},
        {'platform': 'hp-ux', 'lsdev_out': '', 'expected_result': []},
    ]
    for test_case in test_cases:
        test_obj = FcWwnInitiatorFactCollector()
        test_obj.module = MagicMock()
        test_obj.module().run_command.return_value = (0, test_case['lsdev_out'], '')

# Generated at 2022-06-13 01:31:40.012497
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.collectors import network
    from ansible.module_utils.facts.collectors.fc_wwn_initiator import FcWwnInitiatorFactCollector
    from ansible.module_utils.facts.utils import get_file_lines

    # set up module argument spec
    module_args = dict()
    module_args['_ansible_syslog_facility'] = 'LOG_USER'
    module_args['_ansible_socket'] = '/path/to/ansible/mock'
    module_args['_ansible_shell_executable'] = '/bin/sh'

    # set up module

# Generated at 2022-06-13 01:31:46.395256
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_wwn_initiator_fact_collector = FcWwnInitiatorFactCollector()
    assert fc_wwn_initiator_fact_collector.name == 'fibre_channel_wwn'
    assert len(fc_wwn_initiator_fact_collector._fact_ids) == 0
    assert fc_wwn_initiator_fact_collector.collect() == {}

# Generated at 2022-06-13 01:31:47.495340
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    FcWwnInitiatorFactCollector()

# Generated at 2022-06-13 01:31:53.304830
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    module = AnsibleModuleMock()
    FcWwnInitiatorFactCollector.collect(module=module)
    module.run_command.assert_called()

# Generated at 2022-06-13 01:31:55.268692
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_facts = FcWwnInitiatorFactCollector()
    assert fc_facts.name == 'fibre_channel_wwn'
    assert fc_facts._fact_ids == set()


# Generated at 2022-06-13 01:33:26.255840
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    # Create an instance of the FcWwnInitiatorFactCollector
    fcwwn_facts_obj = FcWwnInitiatorFactCollector()

    # Check that the class name is set correctly
    assert fcwwn_facts_obj.name == 'fibre_channel_wwn'


# Generated at 2022-06-13 01:33:33.046676
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """
    Unit test for method collect of class FcWwnInitiatorFactCollector
    :return: 
    """
    c = FcWwnInitiatorFactCollector()
    result = c.collect()
    assert 'fibre_channel_wwn' in result
    assert isinstance(result['fibre_channel_wwn'], list)
    assert len(result['fibre_channel_wwn']) > 0

# Generated at 2022-06-13 01:33:35.998652
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    obj = FcWwnInitiatorFactCollector()
    assert obj.name == 'fibre_channel_wwn'
    assert obj._fact_ids == set()

# Generated at 2022-06-13 01:33:38.576445
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    collector = FcWwnInitiatorFactCollector()
    assert collector.name == 'fibre_channel_wwn'
    assert collector._fact_ids == set()


# Generated at 2022-06-13 01:33:41.820599
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """Unit test for method collect of class FcWwnInitiatorFactCollector
    """
    module = AnsibleModuleMock()
    fact_collector = FcWwnInitiatorFactCollector()
    facts = fact_collector.collect(module=module)
    assert facts['fibre_channel_wwn'] is not None

# Generated at 2022-06-13 01:33:47.006185
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    import platform
    import unittest

    class FcWwnInitiatorFactCollectorTestCase(unittest.TestCase):
        def setUp(self):
            self.collector = FcWwnInitiatorFactCollector()

        def tearDown(self):
            pass

        def test_constructor(self):
            self.assertEqual(self.collector.name, 'fibre_channel_wwn')
            self.assertTrue(isinstance(self.collector._fact_ids, set))
            self.assertEqual(len(self.collector._fact_ids), 0)

        # TODO: add test case method test_collect()

    unittest.main()

# Generated at 2022-06-13 01:33:49.079613
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    obj = FcWwnInitiatorFactCollector(None)
    assert obj.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:33:56.836371
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    fc_facts = {}
    fc_facts['fibre_channel_wwn'] = []
    fc_facts['fibre_channel_wwn'].append('50060b00006975ec')
    test_mock_ansible_module = lambda: None
    test_mock_ansible_module.run_command = lambda self, cmd, check_rc=True: (0, '', '')
    test_mock_ansible_module.get_bin_path = lambda self, arg: '/usr/sbin/fcmsutil'
    setattr(test_mock_ansible_module, '_ansible_no_log', False)
    test_collector = FcWwnInitiatorFactCollector()


# Generated at 2022-06-13 01:34:07.215438
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.utils import get_file_lines
    from ansible.module_utils.facts.collector.fibre_channel_wwn import FcWwnInitiatorFactCollector

    from ansible.module_utils.six import b
    from ansible.module_utils.six.moves import reload_module

    # override system platform for testing
    __builtins__['platform'] = 'linux'

    # prepare test files
    fakefact_file_1 = '/sys/class/fc_host/hba__fc_class_0/port_name'
    open(fakefact_file_1, 'a').close()
    with open(fakefact_file_1, "wb") as myfile:
        myfile

# Generated at 2022-06-13 01:34:12.989985
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():

    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict(),
    )

    col_fact = FcWwnInitiatorFactCollector()

    fc_facts = col_fact.collect(module=module)

    assert fc_facts['fibre_channel_wwn']