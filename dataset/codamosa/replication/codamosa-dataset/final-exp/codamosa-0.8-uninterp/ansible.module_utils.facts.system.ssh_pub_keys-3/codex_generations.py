

# Generated at 2022-06-13 03:33:28.559725
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():

    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils._text import to_bytes

    from tempfile import mkdtemp
    from shutil import rmtree
    import os.path

    test_dir = mkdtemp()


# Generated at 2022-06-13 03:33:37.374071
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    import os

    key_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'ssh_host_keys.pub'))
    with open(key_path) as f:
        content = f.read()
    key_data = dict([x.strip('\n').split()[0:2] for x in content.split('\n')])

    class TestModule(object):
        def __init__(self, facts):
            self.params = {'gather_subset': facts}

    class TestCollector(Collector):
        _fact_class = SshPubKeyFactCollector


# Generated at 2022-06-13 03:33:47.195518
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    fact_collector = SshPubKeyFactCollector()
    result = fact_collector.collect()

# Generated at 2022-06-13 03:33:57.319133
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from ansible.module_utils.facts import FactCollector

    # Create a mock class for the module parameter of method collect
    class moduleMock:
        pass

    # Create a mock class for the collected_facts parameter of method collect
    class collected_factsMock:
        pass

    # Instantiate the class under test
    sshPubKeyFactCollector = SshPubKeyFactCollector()
    # Instantiate a new module and collected_facts mock objects
    module = moduleMock()
    collected_facts = collected_factsMock()
    # Populate module.params with valid data
    module.params = dict()
    module.params['gather_subset'] = ["!all", "ssh_pub_keys"]
    # Call the collect method

# Generated at 2022-06-13 03:34:05.977260
# Unit test for method collect of class SshPubKeyFactCollector

# Generated at 2022-06-13 03:34:10.393789
# Unit test for method collect of class SshPubKeyFactCollector

# Generated at 2022-06-13 03:34:17.431249
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from ansible.module_utils.facts.utils import get_file_content as gfc
    from ansible.module_utils.facts.collector import BaseFactCollector
    x = SshPubKeyFactCollector()
    assert x.name == 'ssh_pub_keys'
    assert hasattr(x, 'collect')
    assert x._fact_ids == set(['ssh_host_pub_keys', 'ssh_host_key_dsa_public',
                               'ssh_host_key_rsa_public', 'ssh_host_key_ecdsa_public',
                               'ssh_host_key_ed25519_public'])
    import __builtin__ as builtins
    builtins.open = lambda x, y: x
    gfc_orig = gfc

# Generated at 2022-06-13 03:34:23.214370
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    '''Unit test for method collect of class SshPubKeyFactCollector'''
    from ansible.module_utils.facts.collector import Collector
    collector = Collector()
    ssh_pub_key_collector = SshPubKeyFactCollector(collector)
    collect_result = ssh_pub_key_collector.collect()
    assert type(collect_result) == dict
    print('Result of collect: %s' % collect_result)

# Generated at 2022-06-13 03:34:29.898227
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    import os

    test_data_dir = os.path.join(os.path.dirname(__file__), "unittests/ssh_pub_keys")
    ssh_pub_key_fact_collector = SshPubKeyFactCollector(module=None, collected_facts=None)
    result = ssh_pub_key_fact_collector.collect(module=None, collected_facts=None)

    assert result['ssh_host_key_rsa_public'] is not None
    assert result['ssh_host_key_rsa_public_keytype'] is not None

# Generated at 2022-06-13 03:34:40.910886
# Unit test for method collect of class SshPubKeyFactCollector

# Generated at 2022-06-13 03:34:54.447615
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    class MockModule:
        pass

    class MockCollector(SshPubKeyFactCollector):
        """Mocking get_file_content as we don't want to call it in unit tests"""
        def _get_file_content(self, filepath):
            return 'ssh-rsa AAABBB key1'

    collect_results = MockCollector().collect(MockModule())

    assert collect_results['ssh_host_key_rsa_public'] == 'AAABBB', 'ssh_host_key_rsa_public is incorrect'
    assert collect_results['ssh_host_key_rsa_public_keytype'] == 'ssh-rsa', 'ssh_host_key_rsa_public_keytype is incorrect'

# Generated at 2022-06-13 03:34:58.708361
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # Initialize the fact collector
    ssh_pub_key_fact_collector_obj = SshPubKeyFactCollector()

    # Initialize the collected_facts parameter
    collected_facts = {}

    # Return a dictionary of ssh_pub_key facts
    return ssh_pub_key_fact_collector_obj.collect(collected_facts=collected_facts)

# Generated at 2022-06-13 03:35:04.964665
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes


# Generated at 2022-06-13 03:35:05.950480
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    SshPubKeyFactCollector().collect()

# Generated at 2022-06-13 03:35:13.174022
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    keydirs = ['/etc/ssh', '/etc/openssh', '/etc']
    for keydir in keydirs:
        collector = SshPubKeyFactCollector()
        collection = collector.collect()
        assert collection.keys() == {'ssh_host_pub_keys',
                                     'ssh_host_key_dsa_public',
                                     'ssh_host_key_rsa_public',
                                     'ssh_host_key_ecdsa_public',
                                     'ssh_host_key_ed25519_public'}

# Generated at 2022-06-13 03:35:24.398013
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # given
    test_collector = SshPubKeyFactCollector()
    test_module = None
    test_facts_dict = None
    # when
    actual_facts_dict = test_collector.collect(test_module, test_facts_dict)
    # then
    assert actual_facts_dict['ssh_host_key_rsa_public_keytype'] is not None
    assert actual_facts_dict['ssh_host_key_rsa_public'] is not None
    assert actual_facts_dict['ssh_host_key_dsa_public_keytype'] is not None
    assert actual_facts_dict['ssh_host_key_dsa_public'] is not None
    assert actual_facts_dict['ssh_host_key_ecdsa_public_keytype'] is not None
    assert actual_

# Generated at 2022-06-13 03:35:32.446871
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    """
    SshPubKeyFactCollector.collect(module=None, collected_fact=None)
    method should return a dict with facts about ssh-host-keys available on
    the system
    """
    from ansible.module_utils.facts import FactCollector

    new_fact_collector = FactCollector()
    ssh_pub_keys = SshPubKeyFactCollector(new_fact_collector)

    res = ssh_pub_keys.collect()

    # run some assertion tests to make sure that we got a dict as expected
    assert isinstance(res, dict)

    # check that we have the expected keys in the returned facts
    assert 'ssh_host_key_dsa_public' in res.keys()
    assert 'ssh_host_key_rsa_public' in res.keys()

# Generated at 2022-06-13 03:35:41.739857
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from . import tmp_ssh_keys
    try:
        ssh_pub_key_facts = SshPubKeyFactCollector().collect()
        assert 'ssh_host_key_dsa_public' in ssh_pub_key_facts
        assert 'ssh_host_key_rsa_public' in ssh_pub_key_facts
        assert 'ssh_host_key_ecdsa_public' in ssh_pub_key_facts
        assert 'ssh_host_key_ed25519_public' in ssh_pub_key_facts
    finally:
        tmp_ssh_keys.cleanup()

# Generated at 2022-06-13 03:35:54.016686
# Unit test for method collect of class SshPubKeyFactCollector

# Generated at 2022-06-13 03:36:02.374231
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from ansible.module_utils.facts.utils import get_file_content, get_file_lines
    from ansible.module_utils.facts.collector import BaseFactCollector
    file_content_mock = get_file_content
    file_line_mock = get_file_lines

    class FileContent(object):
        def __init__(self, file_content):
            self.file_content = file_content

        def read(self):
            return self.file_content

        def close(self):
            pass

    def mock_file_content(file_path):
        return FileContent(file_path)

    get_file_content = mock_file_content

    class FileLine(object):
        def __init__(self, file_content):
            self.file_content = file_content.splitlines

# Generated at 2022-06-13 03:36:15.108993
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # create a test class object
    test_class = SshPubKeyFactCollector()

    # class method collect should return a dictionary
    results = test_class.collect()
    assert results is not None
    assert isinstance(results, dict)

    # test to make sure that at least one ssh_host ssh_host_key_public_* was
    # returned in the results
    found = False
    for key in results.keys():
        if key.startswith('ssh_host_key_') and key.endswith('_public'):
            found = True
            break

    assert found is True

# Generated at 2022-06-13 03:36:20.799142
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    """
    Test ssh public key fact collection.
    """
    collector_mock = SshPubKeyFactCollector()
    result = collector_mock.collect()
    assert result is not None
    assert result['ssh_host_key_dsa_public'] is not None
    assert result['ssh_host_key_rsa_public'] is not None
    assert result['ssh_host_key_ecdsa_public'] is not None
    assert result['ssh_host_key_ed25519_public'] is not None
    assert result['ssh_host_key_dsa_public_keytype'] is not None
    assert result['ssh_host_key_rsa_public_keytype'] is not None
    assert result['ssh_host_key_ecdsa_public_keytype'] is not None

# Generated at 2022-06-13 03:36:31.464166
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    module = DummyModule()
    fact_collecter = SshPubKeyFactCollector()

    # Test that collect works properly with no ssh public keys in the /etc directory
    assert fact_collecter.collect(module) == {}

    # Test that collect works properly with with ssh public keys in the /etc/ssh
    # directory
    setattr(module, '_ssh_key_files', ['ssh_host_rsa_key.pub'])
    setattr(module, '_ssh_key_dir', '/etc/ssh')

# Generated at 2022-06-13 03:36:38.429044
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    class obj:
        def __init__(self,  ssh_host_key_rsa_public='ssh-rsa AAAAB3Nz'):
            self.facts = {'ssh_host_key_rsa_public': ssh_host_key_rsa_public}

    sshpubkey_facts = SshPubKeyFactCollector()
    ssh_pub_key_facts = sshpubkey_facts.collect(obj ,None)

    assert ssh_pub_key_facts == {'ssh_host_key_rsa_public_keytype': 'ssh-rsa', 'ssh_host_key_rsa_public': 'ssh-rsa AAAAB3Nz'}

# Generated at 2022-06-13 03:36:43.492413
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from ansible.module_utils.facts.collectors.ssh_pub_keys import SshPubKeyFactCollector

    collected_facts = {}

    keydirs = ['/etc/ssh', '/etc/openssh', '/etc']

# Generated at 2022-06-13 03:36:45.645463
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    ssh_pub_key_facts = SshPubKeyFactCollector().collect()
    assert (len(ssh_pub_key_facts) > 0)

# Generated at 2022-06-13 03:36:53.390042
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    """ test_SshPubKeyFactCollector_collect method """
    import os

    collected_facts = {}
    collected_facts['system'] = 'Linux'
    pub_key = SshPubKeyFactCollector(None, None, collected_facts)
    #call method collect of class SshPubKeyFactCollector
    pub_key_collect = pub_key.collect()
    pub_key_collect.update(collected_facts)
    #assign expected result for test case
    expected_result = get_expected_result()
    assert pub_key_collect == expected_result


# Generated at 2022-06-13 03:37:01.800688
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    import sys
    from ansible.module_utils.facts.collector import Collector

    # create a ssh_pub_keys collector instance
    myssh_pub_keys = SshPubKeyFactCollector()

    # create a Collector instance for holding results
    mycollector = Collector()

    # execute method collect on the ssh_pub_keys instance
    result = myssh_pub_keys.collect(sys.modules[__name__], mycollector)

    # assert the result

# Generated at 2022-06-13 03:37:12.827201
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector, \
            SshPubKeyFactCollector, BaseFactCollector
    from ansible.module_utils.facts.utils import get_file_content
    import os

    # Setup a mocked file system
    os.chdir('/')
    os.environ['PATH'] = '/usr/bin:/bin'
    os.mkdir('test')
    os.chdir('test')

    os.mkdir('etc')
    os.chdir('etc')
    os.mkdir('ssh')
    os.chdir('ssh')

# Generated at 2022-06-13 03:37:20.433656
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    facts_module = type('FactsModule', (object,), {})
    ssh_pub_keys_fact_collector = SshPubKeyFactCollector(facts_module)
    module_facts = ssh_pub_keys_fact_collector.collect(
        collected_facts=dict(os_family='Linux'),
        module=dict(params=dict(gather_subset=['all'])))
    assert('ssh_host_key_dsa_public' in module_facts)
    assert('ssh_host_key_rsa_public' in module_facts)


# Generated at 2022-06-13 03:37:40.273155
# Unit test for method collect of class SshPubKeyFactCollector

# Generated at 2022-06-13 03:37:49.963474
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    """Unit test for method collect of class SshPubKeyFactCollector"""

    # Create a dummy class for which we can mock collect facts
    class DummyClass(object):
        def __init__(self):
            self.ssh_pub_key_facts = [
                "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOsTl8iFANXy+" + \
                "1dxU6ShhUZ1q3rleLc6QHW8omASB"
            ]

    # Instantiate the class
    cls = DummyClass()

    # Create a new SshPubKeyFactCollector
    collector = SshPubKeyFactCollector()

    # Try to collect the facts
    facts = collector.collect(module=None, collected_facts=cls)

   

# Generated at 2022-06-13 03:38:00.908737
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    fact_collector = SshPubKeyFactCollector()

# Generated at 2022-06-13 03:38:08.070260
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # the following dict will contain the module parameters
    module_args = dict()

    # instantiate a dummy ansible module object
    mock_module = type('AnsibleModule')
    mock_module.params = module_args
    mock_module.check_mode = False

    # instantiate SshPubKeyFactCollector object
    sshpubkey_collector = SshPubKeyFactCollector()

    # execute the collect method
    facts = sshpubkey_collector.collect(module=mock_module)

    # now check that the facts that are collected are the ones we expect
    expected_facts = dict()

# Generated at 2022-06-13 03:38:15.159089
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    module = None
    collected_facts = {
        'distribution': 'Ubuntu',
        'distribution_release': 'precise',
        'virtualization_type': None,
        'gather_subset': ['all'],
        'os_family': 'Debian'
    }
    # import needed for unit test to compile
    from ansible.module_utils.facts.collector.ssh_pub_key import SshPubKeyFactCollector
    ssh_pub_key_facts = SshPubKeyFactCollector.collect(module=module, collected_facts=collected_facts)

# Generated at 2022-06-13 03:38:26.374969
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    testobj = SshPubKeyFactCollector()
    assert testobj

    import tempfile
    import os

    tempdir = tempfile.mkdtemp(prefix='ansible-test-ssh_pub_keys')
    os.mkdir(os.path.join(tempdir, 'ssh'))
    os.mkdir(os.path.join(tempdir, 'openssh'))
    os.mkdir(os.path.join(tempdir, 'ssh', 'ssh_host_dsa_key.pub'))
    os.mkdir(os.path.join(tempdir, 'openssh', 'ssh_host_rsa_key.pub'))
    os.mkdir(os.path.join(tempdir, 'ssh_host_ecdsa_key.pub'))

# Generated at 2022-06-13 03:38:31.943502
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    collector = SshPubKeyFactCollector()
    actual = collector.collect()
    assert 'ssh_host_key_ed25519_public' in actual
    assert 'ssh_host_key_rsa_public' in actual
    assert 'ssh_host_key_dsa_public' in actual
    assert 'ssh_host_key_ecdsa_public' in actual

# Generated at 2022-06-13 03:38:43.710825
# Unit test for method collect of class SshPubKeyFactCollector

# Generated at 2022-06-13 03:38:55.747335
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():

    class ModuleMock:
        def __init__(self, argument_spec):
            self.argument_spec = argument_spec

    class CollectorMock:
        name = 'ssh_pub_keys'
        _fact_ids =  set(['ssh_host_pub_keys',
                          'ssh_host_key_dsa_public',
                          'ssh_host_key_rsa_public',
                          'ssh_host_key_ecdsa_public',
                          'ssh_host_key_ed25519_public'])

        def __init__(self, module=None, collected_facts=None):
            self.module = module
            self.collected_facts = collected_facts

        def collect(self, module=None, collected_facts=None):
            self.module = module
            self.collected_

# Generated at 2022-06-13 03:39:02.937377
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    import platform
    class_under_test = SshPubKeyFactCollector()

# Generated at 2022-06-13 03:39:27.530489
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    module = None
    collected_facts = None
    ssh_pub_key_facts = SshPubKeyFactCollector().collect(module, collected_facts)

# Generated at 2022-06-13 03:39:38.437246
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    testobj = SshPubKeyFactCollector()
    facts = testobj.collect()

# Generated at 2022-06-13 03:39:43.818812
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():

    def mock_get_file_content(filename):

        if filename == '/etc/ssh/ssh_host_dsa_key.pub':
            return 'ssh-dss AAAABbbb...== user@host'
        elif filename == '/etc/openssh/ssh_host_ecdsa_key.pub':
            return 'ecdsa-sha2-nistp256 AAAA...== user@host'
        elif filename == '/etc/ssh/ssh_host_ed25519_key.pub':
            return 'ssh-ed25519 AAAA...== user@host'
        elif filename == '/etc/ssh_host_rsa_key.pub':
            return 'ssh-rsa AAAA...= user@host'
        else:
            return None

    ssh_pub_key_facts = SshPubKeyFactCollector

# Generated at 2022-06-13 03:39:54.620595
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():

    class MockModule(object):
        def __init__(self):
            self._ansible_module = MockModule

    class MockFile(object):
        def __init__(self, content):
            self.content = content

    class MockFs(object):
        def __init__(self, files):
            self.files = files

        def open(self, path, mode):
            return MockFile(self.files[path])

    def my_get_file_content(filename):
        for path, contents in MockFs.files.items():
            if path.endswith(filename):
                return contents
        return None

    class MockOs(object):
        def __init__(self, fs):
            self.fs = fs


# Generated at 2022-06-13 03:40:02.428750
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    class FakeModule:
        pass
        
    sut = SshPubKeyFactCollector()
    result = sut.collect(FakeModule)

# Generated at 2022-06-13 03:40:09.937702
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    collector = SshPubKeyFactCollector()
    collected_facts = collector.collect()

    assert isinstance(collected_facts, dict)
    assert 'ssh_host_pub_keys' in collected_facts
    assert 'ssh_host_key_dsa_public' in collected_facts
    assert 'ssh_host_key_rsa_public' in collected_facts
    assert 'ssh_host_key_ecdsa_public' in collected_facts
    assert 'ssh_host_key_ed25519_public' in collected_facts

# Generated at 2022-06-13 03:40:19.896296
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from ansible.module_utils.facts.collector import FactCollector
    from ansible.module_utils.facts.utils import get_file_content
    from ansible.module_utils.facts.system.ssh_pub_key import SshPubKeyFactCollector


# Generated at 2022-06-13 03:40:27.225410
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    x = SshPubKeyFactCollector()
    ssh_pub_key_facts = x.collect()
    assert ssh_pub_key_facts is not None

# Generated at 2022-06-13 03:40:36.192760
# Unit test for method collect of class SshPubKeyFactCollector

# Generated at 2022-06-13 03:40:45.756916
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    host_keys = SshPubKeyFactCollector()
    ssh_pub_keys = host_keys.collect()
    assert ssh_pub_keys.get('ssh_host_key_dsa_public_keytype') == 'ssh-dss'
    assert ssh_pub_keys.get('ssh_host_key_ecdsa_public_keytype') == 'ecdsa-sha2-nistp256'
    assert ssh_pub_keys.get('ssh_host_key_ed25519_public_keytype') == 'ssh-ed25519'
    assert ssh_pub_keys.get('ssh_host_key_rsa_public_keytype') == 'ssh-rsa'

# Generated at 2022-06-13 03:41:30.515876
# Unit test for method collect of class SshPubKeyFactCollector

# Generated at 2022-06-13 03:41:32.432206
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    collector = SshPubKeyFactCollector()
    facts = collector.collect()
    assert isinstance(facts, dict)

# Generated at 2022-06-13 03:41:42.872253
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # In the test case, ssh_host_rsa_key.pub is not found, although
    # ssh_host_dsa_key.pub, ssh_host_ecdsa_key.pub, and ssh_host_ed25519_key.pub
    # are found.
    # Also, the test case is used to test the keytype is correctly parsed and
    # returned.
    ssh_key_facts = SshPubKeyFactCollector().collect()

    assert ssh_key_facts is not None
    assert len(ssh_key_facts) == 5

    assert 'ssh_host_key_dsa_public' in ssh_key_facts
    assert ssh_key_facts['ssh_host_key_dsa_public_keytype'] == 'ssh-dss'

# Generated at 2022-06-13 03:41:52.411590
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    """
    Check if SshPubKeyFactCollector.collect() works as expected.
    """
    import os.path
    import sys
    import tempfile


# Generated at 2022-06-13 03:41:59.121576
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # Arrange
    fake_module = object()
    expected_ssh_pub_key_facts = {
        'ssh_host_key_ed25519_public': 'AAAAC3NzaC1lZDI1NTE5AAAAIELLiBcYhfEX0cUZjV4xm6u2MD6UOHvjyO/W8X0b/h7/g',
        'ssh_host_key_ed25519_public_keytype': 'ssh-ed25519'
    }

# Generated at 2022-06-13 03:42:06.454954
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    module = None
    collected_facts = {}

    collector = SshPubKeyFactCollector()
    ssh_pub_key_facts = collector.collect(module, collected_facts)

    assert isinstance(ssh_pub_key_facts, dict)
    assert 'ssh_host_key_rsa_public' in ssh_pub_key_facts.keys()

# Generated at 2022-06-13 03:42:16.816070
# Unit test for method collect of class SshPubKeyFactCollector

# Generated at 2022-06-13 03:42:24.557399
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from ansible.module_utils.facts.utils import get_file_content
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collectors import SshPubKeyFactCollector

    """ unit test for method collect of class SshPubKeyFactCollector """
    class MockModule():
        def __init__(self):
            pass

    class MockData():
        def __init__(self):
            self.dir = '/etc/ssh/'
            

# Generated at 2022-06-13 03:42:35.430030
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # find out where we are running
    import os
    curr_dir = os.path.dirname(os.path.realpath(__file__))
    tc_base_dir = os.path.dirname(curr_dir)

    # collect the required facts
    mod_utils_dir = os.path.join(tc_base_dir, 'module_utils')
    facts_dir = os.path.join(tc_base_dir, 'unit_tests', 'test_data', 'facts')
    test_facts = SshPubKeyFactCollector(module_utils_path=mod_utils_dir,
                                        facts_dir=facts_dir)
    test_collected_facts = test_facts.collect()

    # compare the collected facts with the results we expect

# Generated at 2022-06-13 03:42:43.494522
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    import pytest
    fake_module = {'get_file_content': get_file_content}
    pub_key_collector = SshPubKeyFactCollector()

    # test for case when dsa key can be read from etc/openssh/ssh_host_dsa_key.pub
    # file
    fake_module['get_file_content'] = lambda x: "dsa-keytype fake_dsa_key" if x == "/etc/openssh/ssh_host_dsa_key.pub" else None
    pub_key_facts = pub_key_collector.collect(fake_module, None)
    assert pub_key_facts['ssh_host_key_dsa_public'] == "fake_dsa_key"