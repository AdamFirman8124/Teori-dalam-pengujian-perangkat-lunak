

# Generated at 2022-06-13 01:27:28.587833
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    print("TODO")



# Generated at 2022-06-13 01:27:31.746239
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
        fc_instance = FcWwnInitiatorFactCollector()
        assert fc_instance.name == 'fibre_channel_wwn'
        assert 'linux' in fc_instance.platforms
        assert 'sunos' in fc_instance.platforms
        assert 'aix' in fc_instance.platforms
        assert 'hp-ux' in fc_instance.platforms

# Generated at 2022-06-13 01:27:36.499910
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    plugin = FcWwnInitiatorFactCollector()
    facts = {}
    facts['ansible_facts'] = {}
    plugin.collect(collected_facts=facts)
    for k, v in facts['ansible_facts'].items():
        print("%s => %s" % (k, v))

# Generated at 2022-06-13 01:27:42.700063
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    import mock
    installed_mock = mock.Mock()
    installed_mock.return_value = True
    class_constructor = mock.Mock(return_value=installed_mock)
    with mock.patch.dict('sys.modules', {'fcmsutil': class_constructor}):
        fc_wwn_initiator = FcWwnInitiatorFactCollector()
    assert fc_wwn_initiator.name == 'fibre_channel_wwn'
    assert fc_wwn_initiator._fact_ids == set()

# Generated at 2022-06-13 01:27:46.180816
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    facts_collected = {}
    c = FcWwnInitiatorFactCollector()
    facts_collected = c.collect()
    print(facts_collected)


# Generated at 2022-06-13 01:27:50.562104
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """
    Class FcWwnInitiatorFactCollector collect method unit test.
    """
    test_class = FcWwnInitiatorFactCollector()
    facts_dict = test_class.collect()
    assert 'fibre_channel_wwn' in facts_dict

# Generated at 2022-06-13 01:27:58.629151
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    class test_module(object):
        def __init__(self):
            self.run_command_calls = []
            self.run_command_return_values = []
            self.run_command_side_effects = []

        def run_command(self, cmd, check_rc=True):
            self.run_command_calls.append(cmd)
            try:
                return self.run_command_return_values.pop(0)
            except IndexError:
                exception = self.run_command_side_effects.pop(0)
                if isinstance(exception, Exception):
                    raise exception
                return exception

        def get_bin_path(self, name, opt_dirs=[]):
            if name == 'fcinfo':
                return '/usr/sbin/fcinfo'

# Generated at 2022-06-13 01:28:01.686496
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    """
    Unit test for class FcWwnInitiatorFactCollector
    """
    assert FcWwnInitiatorFactCollector().name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:28:04.628339
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():

    # Create an instance of the class
    fc_collector = FcWwnInitiatorFactCollector()

    # Test the results of the constructor
    assert fc_collector.name == 'fibre_channel_wwn'
    assert fc_collector._fact_ids == set()


# Generated at 2022-06-13 01:28:15.694966
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """ this test case covers few scenarios based on platform
        1. on linux it should return a dictionary with key 'fibre_channel_wwn'
           and value having a list of WWNs
        2. on solaris 10 or solaris 11 it should return a dictionary with key
           'fibre_channel_wwn' and value having a list of WWNs
        3. on solaris 9 it should return an empty dictionary as fcinfo is
           not available on solaris 9
        4. on aix (ibm power) it should return a dictionary with key
           'fibre_channel_wwn' and value having a list of WWNs
        5. on hp-ux (ia64) it should return a dictionary with key
           'fibre_channel_wwn' and value having a list of WWNs
    """
    import sys

# Generated at 2022-06-13 01:28:29.468397
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    FcWwnInitiatorFactCollector()

# Generated at 2022-06-13 01:28:36.811236
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():

    class TestModule:
        def __init__(self, rc, out, err):
            self.rc = rc
            self.stdout = out
            self.stderr = err

        def run_command(self, cmd):
            return self.rc, self.stdout, self.stderr

        def get_bin_path(self, filename, opt_dirs=[]):
            return filename


# Generated at 2022-06-13 01:28:48.519746
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """
    Unit test collects facts and checks validity of the facts
    """
    class MockModule(object):
        def __init__(self, params=None):
            self.params = params

        def run_command(self, cmd):
            return (0, "", "")

        def get_bin_path(self, arg, opt_dirs=None, required=False):
            return "/usr/bin/%s" % arg

    # 0. create instance of the class under test
    test_instance = FcWwnInitiatorFactCollector()
    # 1. call method collect
    test_result = test_instance.collect(MockModule(), {})
    # 2. test result is not empty
    assert test_result != {}

# Generated at 2022-06-13 01:28:50.706221
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    '''
    returns a dict with a list of wwns or an empty dict.
    '''
    pass

# Generated at 2022-06-13 01:28:52.698963
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fact_collector = FcWwnInitiatorFactCollector()
    assert fact_collector != None


# Generated at 2022-06-13 01:28:54.732683
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    assert FcWwnInitiatorFactCollector.name == 'fibre_channel_wwn'
    assert FcWwnInitiatorFactCollector.collect() == {}

# Generated at 2022-06-13 01:28:57.107547
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """
    Unit test for method collect of class FcWwnInitiatorFactCollector
    """
    FcWwnInitiatorFactCollector().collect()

# Generated at 2022-06-13 01:29:07.873728
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():

    class MockModule(object):
        def __init__(self):
            self.params = {}

        def run_command(self, cmd):
            """
            This function imitates module.run_command function behaviour.
            """
            if ('lsdev -Cc adapter -l fcs*' in cmd) and ('Available' in cmd):
                return 0, 'fcs0 Available 02-08-08 10/10/0  PCI 1000v FCoE Adapter', ''
            elif 'lscfg -vpl fcs0' in cmd:
                return 0, 'Network Address.............10000090FA551509', ''
            elif 'ioscan -fnC FC' in cmd:
                return 0, '/dev/fcd0    /dev/fcd1    /dev/fcd2', ''

# Generated at 2022-06-13 01:29:17.209698
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collectors import FcWwnInitiatorFactCollector
    from ansible.module_utils.six import StringIO
    import sys
    import stat

    FcWwnInitiatorFactCollector.collect(None, {})
    file_mode = None
    try:
        mode = stat.S_IMODE(os.lstat('/sys/class/fc_host/host0/port_name').st_mode)
        file_mode = oct(mode)
    except Exception:
        file_mode = None
    if file_mode is not None:
        sys.stdout = StringIO()

# Generated at 2022-06-13 01:29:27.845927
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():

    test_os_facts = {
        "os_facts": {},
        "fibre_channel_wwn": []
    }

    fc_wwn_fact_collector = FcWwnInitiatorFactCollector()
    # on linux
    if sys.platform.startswith('linux'):
        for fcfile in glob.glob('/sys/class/fc_host/*/port_name'):
            for line in open(fcfile, 'r'):
                test_os_facts['fibre_channel_wwn'].append(line.rstrip()[2:])
        result = fc_wwn_fact_collector.collect(collected_facts=test_os_facts)
        assert result == test_os_facts
    # on solaris 10 or solaris 11 should use `fc

# Generated at 2022-06-13 01:29:54.728218
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fact_collector = FcWwnInitiatorFactCollector()
    assert fact_collector.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:29:57.950120
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():

    fci = FcWwnInitiatorFactCollector()
    assert fci.name == 'fibre_channel_wwn'
    assert 'fibre_channel_wwn' in fci._fact_ids

# Generated at 2022-06-13 01:30:05.116143
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """Unit test for method collect of class FcWwnInitiatorFactCollector"""

    # Collect facts
    fcwwn_fc = FcWwnInitiatorFactCollector()
    fc_facts = fcwwn_fc.collect()
    assert fc_facts['fibre_channel_wwn']

    # Test whether all collected WWNs are strings starting with 0x
    for wwn in fc_facts['fibre_channel_wwn']:
        assert isinstance(wwn, str)
        assert wwn.startswith('0x')

# Generated at 2022-06-13 01:30:12.931047
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_collector = FcWwnInitiatorFactCollector()
    assert fc_collector.name == 'fibre_channel_wwn', "fc_collector.name returns incorrect value"
    assert fc_collector._fact_ids == set(), "fc_collector._fact_ids returns incorrect value"
    assert repr(fc_collector) == '<FcWwnInitiatorFactCollector(fibre_channel_wwn)>'

# Generated at 2022-06-13 01:30:23.050588
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    sys_module = [
        'linux',
        'solaris',
        'aix',
        'hp-ux'
    ]
    from ansible.module_utils.facts.collector import ModuleDepFactsCollector

    for platform in sys_module:
        sys.platform = platform
        fc = FcWwnInitiatorFactCollector()
        fc_facts = fc.collect()
        if not fc_facts:
            continue
        assert 'fibre_channel_wwn' in fc_facts
        if fc_facts['fibre_channel_wwn']:
            print("fc_facts['fibre_channel_wwn'] => %s" % fc_facts['fibre_channel_wwn'])

# Generated at 2022-06-13 01:30:24.065855
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    FcWwnInitiatorFactCollector()

# Generated at 2022-06-13 01:30:26.101309
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    assert len(FcWwnInitiatorFactCollector.__doc__) > 0

# Generated at 2022-06-13 01:30:28.035166
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    ff = FcWwnInitiatorFactCollector()
    assert ff.name == 'fibre_channel_wwn'
    assert ff._fact_ids == set()



# Generated at 2022-06-13 01:30:36.145590
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    import platform
    import os
    import tempfile
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.utils import get_file_lines
    if platform.system().lower() == 'linux':
        class FakeModule:
            def get_bin_path(self, args, opt_dirs=()):
                return args
            def run_command(self, cmd):
                if cmd == 'lsdev -Cc adapter -l fcs*':
                    return 0, '/dev/fcs0 Available 04-08-02 IBM 16Gb FC Single Port Adapter (df1000f807)', None
                    # return 0, '/dev/fcs0 Defined       04-08-02 IBM 16Gb FC Single Port Adapter (df1000f807)', None


# Generated at 2022-06-13 01:30:38.633081
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_facts = FcWwnInitiatorFactCollector()
    assert fc_facts is not None

if __name__ == '__main__':
    test_FcWwnInitiatorFactCollector()

# Generated at 2022-06-13 01:31:32.265212
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    import os
    import sys
    import unittest

    # creating an instance
    obj = FcWwnInitiatorFactCollector()

    # testing name attribute
    assert obj.name == 'fibre_channel_wwn'

    # testing collect function
    obj.collect(collected_facts=None)

# Generated at 2022-06-13 01:31:43.350236
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts.utils import mock_module

    fc1 = '0x21000014ff52a9bb'
    fc2 = '0x21000014ff52a9ac'
    # create a dict that simulates the contents /sys/class/fc_host/host*/port_name
    mock_fc_port_name = {}
    mock_fc_port_name['ansible_facts'] = { 'filesystem': {
        '/sys/class/fc_host/host0/port_name': { 'content': fc1 },
        '/sys/class/fc_host/host1/port_name': { 'content': fc2 },
    }}
    # create a mock object for the ansible module
    module = mock_module()
    # pass the mock object and the dict as arguments to the

# Generated at 2022-06-13 01:31:45.589513
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc = FcWwnInitiatorFactCollector()

# Generated at 2022-06-13 01:31:47.200663
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    collector = FcWwnInitiatorFactCollector()
    assert collector.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:31:56.860939
# Unit test for method collect of class FcWwnInitiatorFactCollector

# Generated at 2022-06-13 01:31:59.493613
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc = FcWwnInitiatorFactCollector()
    assert fc.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:32:00.709934
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    FcWwnInitiatorFactCollector()


# Generated at 2022-06-13 01:32:10.311904
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """ Test FcWwnInitiatorFactCollector.collect()
        Return facts regarding fibre_channel_wwn.
    """

    from ansible.module_utils.facts.collector.fibre_channel import FcWwnInitiatorFactCollector
    from ansible.module_utils.facts.utils import FactsCollectionError

    class TestModule(object):
        def __init__(self):
            self.params = {}
            self.fail_json = False
            self.run_command_environ_update = None

    class TestModuleFail(object):
        def __init__(self):
            self.params = {}
            self.fail_json = True
            self.run_command_environ_update = None

    # On Linux
    factcol = FcWwnInitiatorFactCollector()

# Generated at 2022-06-13 01:32:15.843131
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    """
    test_FcWwnInitiatorFactCollector: test constructor of class FcWwnInitiatorFactCollector
    """
    fc_wwn_collector = FcWwnInitiatorFactCollector()
    assert type(fc_wwn_collector) == FcWwnInitiatorFactCollector
    assert fc_wwn_collector.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:32:20.762656
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():

    fc_facts = {}
    fc_facts['fibre_channel_wwn'] = []

    # expected result 
    fibre_channel_wwn = ['21000014ff52a9bb']
    
    fc_facts['fibre_channel_wwn'] = fibre_channel_wwn

    fcwwn_fc = FcWwnInitiatorFactCollector()
    assert fcwwn_fc.collect() == fc_facts



# Generated at 2022-06-13 01:34:03.332924
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    obj1 = FcWwnInitiatorFactCollector()
    assert obj1
    assert obj1.name == 'fibre_channel_wwn'
    assert obj1._fact_ids == set()


# Generated at 2022-06-13 01:34:14.007241
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible_collections.misc.not_a_real_collection.plugins.module_utils.facts.collectors.network import FcWwnInitiatorFactCollector
    from ansible_collections.misc.not_a_real_collection.plugins.module_utils.facts.utils import get_file_lines
    fc_facts = {}
    fc_facts['fibre_channel_wwn'] = []
    fc_collector = FcWwnInitiatorFactCollector()

# Generated at 2022-06-13 01:34:23.486318
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    FC_WWN = '0x21000014ff52a9bb'
    TO_FILE = 'to_file'
    module = MockModule()
    fc_wwn = FcWwnInitiatorFactCollector()
    sys.platform = 'linux2'
    fc_wwn.collect(module=module)
    assert module.args == [TO_FILE, 'r']
    sys.platform = 'sunos5'
    fc_wwn.collect(module=module)
    assert module.args == [TO_FILE, 'r']
    sys.platform = 'aix6'
    fc_wwn.collect(module=module)
    assert module.args == [TO_FILE, 'r']
    sys.platform = 'hp-ux11'

# Generated at 2022-06-13 01:34:32.130499
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """
    Unit test for the method collect of the class FcWwnInitiatorFactCollector.
    """

    def module_mock(**kwargs):
        """
        Mock function module.run_command.
        """
        return {
            'rc': kwargs.pop('rc', 0),
            'stdout': kwargs.pop('stdout', ''),
            'stderr': kwargs.pop('stderr', '')
        }

    EFFECTIVE_PLATFORM = sys.platform
    FACTS_COLLECTED = {}

    def platform_mock(name='', **kwargs):
        """
        Mock for platform module.
        """
        if name == 'linux_distribution':
            return 'RedHat', '7.1', ''

# Generated at 2022-06-13 01:34:35.479181
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    # Create object of FcWwnInitiatorFactCollector class
    fci = FcWwnInitiatorFactCollector(None)
    # Test method name()
    assert fci.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:34:38.884845
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc = FcWwnInitiatorFactCollector()
    assert fc.name == 'fibre_channel_wwn'
    assert not fc._fact_ids

# Generated at 2022-06-13 01:34:42.177235
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    from ansible.module_utils.facts.collector import FactCollector

    fc_wwn_facts_collector = FactCollector(FcWwnInitiatorFactCollector, __file__)

# Generated at 2022-06-13 01:34:46.784776
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    class MockModule(object):
        def __init__(self, params=None):
            self.params = params

    assert FcWwnInitiatorFactCollector().name == 'fibre_channel_wwn'
    assert FcWwnInitiatorFactCollector(MockModule()).name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:34:55.015910
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    import platform
    os_platform = platform.system()
    if os_platform == 'Linux':
        from ansible_collections.misc.not_a_real_collection.tests.unit.compat.mock import patch
        path = 'ansible_collections.misc.not_a_real_collection.plugins.module_utils.facts.fibre_channels.fc_wwn_initiator'
        with patch(path + '.get_file_lines') as mock_get_file_lines:
            mock_get_file_lines.return_value = """0x21000014ff52a9bb
0x21000014ff52a9bd"""
            result = FcWwnInitiatorFactCollector().collect()

# Generated at 2022-06-13 01:34:58.847774
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc = FcWwnInitiatorFactCollector()
    assert fc.name == 'fibre_channel_wwn'
# Unit test end
