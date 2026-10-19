

# Generated at 2022-06-13 03:33:25.982532
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    module = None
    collected_facts = None

    testobj = SshPubKeyFactCollector()
    result = testobj.collect(module, collected_facts)

    assert result.keys() == set(['ssh_host_key_dsa_public',
                                 'ssh_host_key_rsa_public',
                                 'ssh_host_key_ecdsa_public',
                                 'ssh_host_key_ed25519_public'])

# Generated at 2022-06-13 03:33:35.594615
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    """ returns ssh keys read from file /etc/ssh/ssh_host_<algo>_key.pub """
    # Define fake ssh key files with empty key
    import tempfile
    import os.path

    (fd, keydir) = tempfile.mkdtemp()
    algos = ('dsa', 'rsa', 'ecdsa', 'ed25519')

    for algo in algos:
        key_filename = os.path.join(keydir, 'ssh_host_%s_key.pub' % algo)

# Generated at 2022-06-13 03:33:45.912478
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils._text import to_bytes
    import os, sys

    # create fake host key files
    os.mkdir("ssh")
    os.mkdir("ssh/ssh_host_dsa_key.pub")
    os.mkdir("ssh/ssh_host_rsa_key.pub")
    os.mkdir("ssh/ssh_host_ecdsa_key.pub")
    os.mkdir("ssh/ssh_host_ed25519_key.pub")
    os.mkdir("ssh/ssh_host_dsa_key")
    os.mkdir("ssh/ssh_host_rsa_key")
    os.mkdir("ssh/ssh_host_ecdsa_key")

# Generated at 2022-06-13 03:33:46.697914
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    pass

# Generated at 2022-06-13 03:33:49.395590
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    collector = SshPubKeyFactCollector()

    results = collector.collect()
    assert ['ansible_ssh_host_key_ecdsa_public'] == list(results.keys())

# Generated at 2022-06-13 03:33:57.360514
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    """
    Basic functional test of the method collect of class SshPubKeyCollector
    """
    mock_module = type('module', (object, ), {'params': {}})
    mock_collected_facts = {}
    ssh_pub_keys_collector = SshPubKeyFactCollector()
    ssh_pub_key_facts = ssh_pub_keys_collector.collect(mock_module, mock_collected_facts)

    # make sure the basic facts are present
    for fact_id in ssh_pub_keys_collector._fact_ids:
        assert fact_id in ssh_pub_key_facts

# Generated at 2022-06-13 03:33:58.967103
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    fact_collector_class = SshPubKeyFactCollector
    fact_collector_class.collect()

# Generated at 2022-06-13 03:34:04.315579
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    collected_facts = {}
    mock_module = type('MockModule', (), {'exit_json': lambda self, **kwargs: kwargs})
    mock_module_instance = mock_module()
    spam_fact_collector = SshPubKeyFactCollector()
    spam_fact_collector.collect(module=mock_module_instance, collected_facts=collected_facts)
    assert collected_facts['ssh_host_key_rsa_public'] is not None

# Generated at 2022-06-13 03:34:14.228859
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    class Mock(object):
        pass

    module_opts = {
        'mode': 0o600,
        'encoding': None,
        'errors': 'strict',
    }


# Generated at 2022-06-13 03:34:25.329580
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    class MockModule:
        def __init__(self):
            self.params = {'gather_subset': ['all']}

    mock_module = MockModule()
    collected_facts = {'ansible_local': {'ssh_pub_keys': None}}
    # Mock the get_file_content() method of module_utils.facts.utils
    import ansible.module_utils.facts.utils
    original_get_file_content = ansible.module_utils.facts.utils.get_file_content

# Generated at 2022-06-13 03:34:28.704139
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # Test with empty variables - no keys found
    ssh_pub_key_facts = SshPubKeyFactCollector().collect()
    assert ssh_pub_key_facts == {}

# Generated at 2022-06-13 03:34:39.651607
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    class MockModule:
        def __init__(self, facts=None):
            self.params = {}
            self.facts = facts

        def get_bin_path(self, executable, required=True):
            pass

    # Should handle empty /etc/ssh dir
    test_facts = {}
    test_module = MockModule(facts=test_facts)
    test_collector = SshPubKeyFactCollector()
    result = test_collector.collect(module=test_module, collected_facts=test_facts)
    assert result == {}

    # Should handle empty /etc/openssh dir
    test_facts = {}
    test_module = MockModule(facts=test_facts)
    test_collector = SshPubKeyFactCollector()

# Generated at 2022-06-13 03:34:47.048080
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # Make sure we can collect facts for openssh and ssh are the same
    ssh_pub_key_facts = SshPubKeyFactCollector().collect()
    assert 'ssh_host_key_dsa_public' in ssh_pub_key_facts
    assert 'ssh_host_key_dsa_public_keytype' in ssh_pub_key_facts
    assert 'ssh_host_key_rsa_public' in ssh_pub_key_facts
    assert 'ssh_host_key_rsa_public_keytype' in ssh_pub_key_facts
    assert 'ssh_host_key_ecdsa_public' in ssh_pub_key_facts
    assert 'ssh_host_key_ecdsa_public_keytype' in ssh_pub_key_facts

# Generated at 2022-06-13 03:34:57.048432
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # create the instance
    SshPubKeyFactCollector = SshPubKeyFactCollector()

    # create the return values for the get_file_content method
    keydata = 'ssh-rsa abcdef'

    SshPubKeyFactCollector.get_file_content = lambda x: keydata \
        if 'ssh_host_rsa_key.pub' in x else None

    # run the collect method
    facts = SshPubKeyFactCollector.collect()

    # basic assertions
    assert 'ssh_host_key_rsa_public' in facts
    assert 'ssh_host_key_rsa_public_keytype' in facts
    assert facts['ssh_host_key_rsa_public'] == 'abcdef'

# Generated at 2022-06-13 03:35:10.176272
# Unit test for method collect of class SshPubKeyFactCollector

# Generated at 2022-06-13 03:35:16.265354
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    keys_found = {
        'ssh_host_key_dsa_public': 'dsa',
        'ssh_host_key_rsa_public': 'rsa',
        'ssh_host_key_ecdsa_public': 'ecdsa',
        'ssh_host_key_ed25519_public': 'ed25519'
    }

    for key,algo in keys_found.items():
        ssh_pub_key_facts = {}
        ssh_pub_key_facts[key] = '%s ssh-public-key' % algo
        collector = SshPubKeyFactCollector(module=None, collected_facts=ssh_pub_key_facts)
        facts = collector.collect()
        assert key in facts

# Generated at 2022-06-13 03:35:27.038124
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    import tempfile
    import shutil

    # Create a temporary directory
    tmpdir = tempfile.mkdtemp()

    # Create a temporary directory of ssh keys
    keydir = tmpdir+"/etc/ssh"
    shutil.copytree("tests/unit/module_utils/facts/ssh_keys_dir", keydir)

    # Create a temporary module
    class MockModule():
        pass
    tmp_module = MockModule()

    collected_facts = SshPubKeyFactCollector()

    tmp_module.params = {}
    collected_facts.collect(tmp_module, collected_facts)


# Generated at 2022-06-13 03:35:36.609580
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    class DummyModule(object):
        b_type = 'not_a_file'
        def __init__(self):
            return

    class DummyCollector(object):
        def __init__(self):
            return

    algos = ('dsa', 'rsa', 'ecdsa', 'ed25519')

    test_collector = SshPubKeyFactCollector()
    test_module = DummyModule()
    test_collector.collect(module=test_module)

    assert isinstance(test_collector.collect(module=test_module), dict)

    # keys exist, so the results should not be empty
    test_collector = SshPubKeyFactCollector()
    test_module = DummyModule()
    ssh_key_facts = test_collector.collect(module=test_module)

# Generated at 2022-06-13 03:35:45.054520
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # Working ssh keys
    for algo in ('dsa', 'rsa', 'ecdsa', 'ed25519'):
        factname = 'ssh_host_key_%s_public' % algo
        f = SshPubKeyFactCollector()
        f.collect()
        assert(factname in f.collect())

    # Non-working ssh keys
    f = SshPubKeyFactCollector()
    f.collect()
    assert('ssh_host_key_dsa_public_keytype' not in f.collect())

# Generated at 2022-06-13 03:35:49.026715
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    module = None
    collected_facts = None

    collector = SshPubKeyFactCollector()
    ssh_facts = collector.collect(module, collected_facts)

    assert ssh_facts is not None
    assert len(ssh_facts) > 0

# Generated at 2022-06-13 03:35:57.450239
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    """ Validate that if we have ssh_host_key_<algo>_public, we
    have ssh_host_key_<algo>_public_keytype too, and vice versa
    """
    c = SshPubKeyFactCollector()
    c.collect()
    algos = ('dsa', 'rsa', 'ecdsa', 'ed25519')
    # These facts should exist
    for algo in algos:
        factname = 'ssh_host_key_%s_public' % algo
        assert c.collect_func(factname) is not None
        factname = 'ssh_host_key_%s_public_keytype' % algo
        assert c.collect_func(factname) is not None

# Generated at 2022-06-13 03:36:04.161918
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from ansible.module_utils.facts.collector import FactCollector
    from ansible.module_utils.facts.utils import get_file_content

    def get_file_facts(keydir, keyfile, keydata):
        def get_file(filename):
            if filename == '%s/%s' % (keydir, keyfile):
                return keydata
            else:
                return None
        return get_file

    # "Nominal" case, all keys are present
    facts = {}
    keydir = '/etc'
    keydata = "ssh-rsa ....."
    keyfile = 'ssh_host_rsa_key.pub'
    facts['ssh_host_key_rsa_public'] = keydata.split()[1]

# Generated at 2022-06-13 03:36:15.258767
# Unit test for method collect of class SshPubKeyFactCollector

# Generated at 2022-06-13 03:36:17.111903
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    """Test method ``collect`` of module ``sshpubkey_facts``."""
    # not implemented
    pass

# Generated at 2022-06-13 03:36:27.983969
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from ansible.module_utils.facts import FactCollector, \
        collect_facts, get_collector_names

    def mock_module_params(module_name, module_args, became=None,
                           diff=False, ansible_facts={}, ansible_version=None):
        if 'filename' in module_args:
            key_filename = module_args['filename']

# Generated at 2022-06-13 03:36:37.452343
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    mock_module = type('module', (object, ), {})
    mock_module.params = {}

    fact_collector = SshPubKeyFactCollector()
    collected_facts = fact_collector.collect(mock_module, {})

    # Test collected facts
    assert 'ssh_host_key_dsa_public' in collected_facts
    assert 'ssh_host_key_ecdsa_public' in collected_facts
    assert 'ssh_host_key_rsa_public' in collected_facts
    assert 'ssh_host_key_ed25519_public' in collected_facts
    assert 'ssh_host_key_dsa_public_keytype' in collected_facts
    assert 'ssh_host_key_ecdsa_public_keytype' in collected_facts

# Generated at 2022-06-13 03:36:42.493401
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    class TestModule():
        def __init__(self):
            self.tmpdir = '/tmp/'
    class TestModuleAnsibleFacts():
        def __init__(self):
            self.module = TestModule()
    testobj = SshPubKeyFactCollector(TestModuleAnsibleFacts())
    testobj.collect()


# Generated at 2022-06-13 03:36:53.390715
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():

    class FakeSshPubKeyFactCollector(SshPubKeyFactCollector):

        def __init__(self):
            self.ssh_host_key_rsa_public_content = ''
            self.ssh_host_key_dsa_public_content = ''
            self.ssh_host_key_ecdsa_public_content = ''
            self.ssh_host_key_ed25519_public_content = ''

        def get_file_content(self, filename):
            if filename == '/etc/ssh/ssh_host_rsa_key.pub':
                return self.ssh_host_key_rsa_public_content
            elif filename == '/etc/ssh/ssh_host_dsa_key.pub':
                return self.ssh_host_key_dsa_public_content

# Generated at 2022-06-13 03:36:54.005834
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    pass

# Generated at 2022-06-13 03:37:02.146394
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from ansible.module_utils.facts.collector import FactCollector
    from ansible.module_utils.facts.utils import get_file_content
    from ansible.module_utils._text import to_bytes

    new_ssh_pub_key_method = SshPubKeyFactCollector()
    FactCollector._fact_collectors['ssh_pub_keys'] = new_ssh_pub_key_method

    # pretend that /etc/ssh/ssh_host_dsa_key.pub exists and has content
    module = object()
    # fake-file /etc/ssh/ssh_host_dsa_key.pub -> "dsa AAAABBB...666\n"
    fake_file_context_manager = to_bytes("dsa AAAABBB...666\n")

# Generated at 2022-06-13 03:37:16.787295
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    '''
    Unit test for method collect of class SshPubKeyFactCollector
    :return:
    '''
    # Create a test SshPubKeyFactCollector object
    sshPubKeyFactCollector = SshPubKeyFactCollector()
    ret_facts = sshPubKeyFactCollector.collect()
    # assert the return value is a dict type
    assert isinstance(ret_facts, dict)

# Generated at 2022-06-13 03:37:21.183933
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():

    # Create instance of class SshPubKeyFactCollector
    ssh_pub_key_fact_collector = SshPubKeyFactCollector()

    # Check method collect
    ssh_host_pub_keys = ssh_pub_key_fact_collector.collect().get('ssh_host_pub_keys', None)
    assert ssh_host_pub_keys is not None

# Generated at 2022-06-13 03:37:26.460712
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():

    class MockModule(object):
        def __init__(self):
            self.system = 'Linux'

    class MockCollectFacts(object):
        def __init__(self):
            self.system = 'Linux'
            self.file_exists = {'ssh_host_key_ecdsa_public': 1}

# Generated at 2022-06-13 03:37:37.228030
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    ssh_pub_key_collector = SshPubKeyFactCollector()
    # test with all keys in /etc/ssh
    ssh_pub_key_facts = ssh_pub_key_collector.collect(collected_facts={'ssh_pub_keys_dir': '/etc/ssh'})

# Generated at 2022-06-13 03:37:48.581611
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # Test when no ssh keys are found
    module_mock = Mock()
    module_mock.facts = dict()
    ssh_pub_key_facts = SshPubKeyFactCollector().collect(module_mock, module_mock.facts)
    assert ssh_pub_key_facts == dict()

    # Test when ssh keys are found in /etc/ssh
    module_mock = Mock()
    module_mock.facts = dict()

# Generated at 2022-06-13 03:37:54.181236
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    ssh_pub_key_facts = SshPubKeyFactCollector().collect(module=None, collected_facts=None)
    assert ssh_pub_key_facts is not None
    for factname in SshPubKeyFactCollector._fact_ids:
        assert factname in ssh_pub_key_facts

# Generated at 2022-06-13 03:37:58.861616
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    fact_data_mock = {'ssh_host_key_dsa_public': 'ssh-dss testdata',
                      'ssh_host_key_rsa_public': 'ssh-rsa testdata',
                      'ssh_host_key_ecdsa_public': 'ecdsa-sha2-nistp256 testdata',
                      'ssh_host_key_ed25519_public': 'ssh-ed25519 testdata'}
    module_mock = type('module', (object,), {})
    module_mock.params = {}
    module_mock.params['gather_subset'] = ['!all', 'network']
    collected_facts_mock = type('collected_facts', (object,), {})
    collected_facts_mock.data = {}

# Generated at 2022-06-13 03:38:06.773640
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    collector = SshPubKeyFactCollector()
    facts = {}
    facts = collector.collect(module=None, collected_facts=None)
    assert type(facts['ssh_host_key_dsa_public']) is str
    assert type(facts['ssh_host_key_rsa_public']) is str
    assert type(facts['ssh_host_key_ecdsa_public']) is str
    assert type(facts['ssh_host_key_ed25519_public']) is str
    assert type(facts['ssh_host_key_dsa_public_keytype']) is str
    assert type(facts['ssh_host_key_rsa_public_keytype']) is str
    assert type(facts['ssh_host_key_ecdsa_public_keytype']) is str

# Generated at 2022-06-13 03:38:08.789770
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    arg_spec = {}
    module = MockModule(arg_spec=arg_spec)

    SshPubKeyFactCollector(module=module).collect(module=module)

# Generated at 2022-06-13 03:38:14.028520
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # GIVEN a SshPubKeyFactCollector instance, inject the expected output
    # for get_file_content into it
    ssh_pub_key_facts_collector = SshPubKeyFactCollector()

# Generated at 2022-06-13 03:38:32.503065
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    keys = SshPubKeyFactCollector().collect()
    assert len(keys) > 0

# Generated at 2022-06-13 03:38:39.841662
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    fixture = SshPubKeyFactCollector()
    ssh_pub_key_facts = fixture.collect()
    assert 'ssh_host_key_dsa_public' in ssh_pub_key_facts
    assert 'ssh_host_key_rsa_public' in ssh_pub_key_facts
    assert 'ssh_host_key_ecdsa_public' in ssh_pub_key_facts
    assert 'ssh_host_key_ed25519_public' in ssh_pub_key_facts

# Generated at 2022-06-13 03:38:45.400351
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # test if returns empty dictionary when no key files are present
    from ansible.module_utils.facts import Collector
    facts_collector = Collector()
    ssh_pub_keys = facts_collector.collect(collector_class=SshPubKeyFactCollector)
    assert ssh_pub_keys == {}

    # TODO: add test for case when keys are present in the system

# Generated at 2022-06-13 03:38:57.011809
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    ssh_pub_key_facts = SshPubKeyFactCollector.collect()

    assert 'ssh_host_key_dsa_public' in ssh_pub_key_facts

# Generated at 2022-06-13 03:39:07.423628
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # Run tests for the method collect of class SshPubKeyFactCollector
    import shutil
    import tempfile

    ssh_pub_key_fact_collector = SshPubKeyFactCollector()
    ssh_pub_key_fact_collector._fact_ids = set(['ssh_host_key_rsa_public'])

    # run collect without any ssh keys
    collected_facts = ssh_pub_key_fact_collector.collect()
    assert collected_facts == {}

    # run collect with an ssh key
    tmp_keydir = tempfile.mkdtemp()
    tmp_key = tmp_keydir + '/ssh_host_rsa_key.pub'
    shutil.copyfile('./unit/modules/utils/facts/files/ssh_host_rsa_key.pub',
                    tmp_key)

# Generated at 2022-06-13 03:39:17.267452
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from ansible.module_utils.facts.utils import FactsCollector

    collected_facts = {'default': {}}
    module = None
    sshpubkey_fact = SshPubKeyFactCollector()

    sshpubkey_fact.collect(module, collected_facts)
    assert collected_facts['ansible_ssh_host_key_dsa_public'] is not None
    assert collected_facts['ansible_ssh_host_key_rsa_public'] is not None
    assert collected_facts['ansible_ssh_host_key_ecdsa_public'] is not None
    assert collected_facts['ansible_ssh_host_key_ed25519_public'] is not None

    # Cleanup
    FactsCollector._fact_collectors.clear()

# Generated at 2022-06-13 03:39:26.568464
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    """
    When the ssh_host_key_dsa_public and ssh_host_key_rsa_public
    facts are read, the expected result is returned.
    """

# Generated at 2022-06-13 03:39:34.782066
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    class TestModule(object):
        def __init__(self):
            self.params = {
                'ssh_public_key_files': None
            }
            self.ansible_ssh_common_args = None

    collector = SshPubKeyFactCollector()
    module = TestModule()
    ssh_pub_key_facts_0 = collector.collect(module=module)
    assert len(ssh_pub_key_facts_0) > 0

if __name__ == '__main__':
    test_SshPubKeyFactCollector_collect()

# Generated at 2022-06-13 03:39:43.177945
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from ansible.module_utils.facts import VirtualFilesystem


# Generated at 2022-06-13 03:39:44.353753
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    #TODO
    # Test with various files in different locations
    pass

# Generated at 2022-06-13 03:40:26.173824
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    """Test class SshPubKeyFactCollector"""
    facts = {}

    # populate facts with values that we know should match
    # the values we expect to find in the ssh keys under /etc/ssh
    # on a test system
    facts['ssh_host_key_dsa_public'] = 'ssh-dss AAAAB3NzaC1kc3MAAACBAP4Nw4sB/yN/gFk/YT97T/H/0tZgyg7/u0MYmOc7VuKm8'

# Generated at 2022-06-13 03:40:35.553951
# Unit test for method collect of class SshPubKeyFactCollector

# Generated at 2022-06-13 03:40:46.681298
# Unit test for method collect of class SshPubKeyFactCollector

# Generated at 2022-06-13 03:40:56.290127
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    """ Unit test to ensure collect() method returns expected ssh_pub_key facts """


# Generated at 2022-06-13 03:41:03.583464
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # executed from tests/unit/module_utils/facts/test_collections.py
    mock_module = type('MockAnsibleModule', (object,), {'params': {}})
    mock_module_utils = type('MockModuleUtils', (object,), {'get_file_content': get_file_content})

    # mock_module.params = {}
    fact_collector = SshPubKeyFactCollector()
    fact_collector.collect(module=mock_module, module_utils=mock_module_utils)
    # print(json.dumps(fact_collector.collect(module=mock_module, module_utils=mock_module_utils), indent=4, sort_keys=True))

# Generated at 2022-06-13 03:41:06.843943
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    ssh_pub_key_facts = SshPubKeyFactCollector()
    results = ssh_pub_key_facts.collect()
    assert isinstance(results, dict)

# Generated at 2022-06-13 03:41:16.215959
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():

    class TestAnsibleModule(object):
        def __init__(self):
            self.params = {}
            self.exit_json = None
            self.fail_json = None

    class TestModuleUtils(object):
        def __init__(self):
            self.get_file_content = None

    ansible_module = TestAnsibleModule()
    ansible_module_utils = TestModuleUtils()

# Generated at 2022-06-13 03:41:18.141625
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    ssh_pub_key_facts = SshPubKeyFactCollector.collect()
    assert any(map(lambda x: 'ssh_host_key_rsa_public' in x, ssh_pub_key_facts))

# Generated at 2022-06-13 03:41:19.376176
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    keyboard_interrupt = False
    assert SshPubKeyFactCollector.collect(keyboard_interrupt)

# Generated at 2022-06-13 03:41:22.430931
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():

    # instantiate the class
    sshpubkey_collector = SshPubKeyFactCollector()
    result = sshpubkey_collector.collect()
    assert result == {}

# Generated at 2022-06-13 03:42:38.157455
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # Test 1
    result = SshPubKeyFactCollector().collect()
    assert result is not None

# Generated at 2022-06-13 03:42:44.780661
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    import os
    import pytest
    from ansible.module_utils.facts.collectors import collector_module
    from ansible.module_utils.facts.utils import get_file_content

    # create ssh_host_key_dsa_public file
    ssh_host_key_dsa_public = "/etc/ssh/ssh_host_dsa_key.pub"

# Generated at 2022-06-13 03:42:52.156064
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    """
    Test if all the facts are collected
    """
    class MockModule(object):
        def __init__(self, **kwargs):
            self.params = {
                'gather_subset': ['!all', 'network']
            }
            self.params.update(**kwargs)

        def get_bin_path(self, executable):
            return

    ssh_pub_key_facts = SshPubKeyFactCollector()
    # Use the fact collector with GatherSubset with network and other facts
    mock_module = MockModule()
    result = ssh_pub_key_facts.collect(module=mock_module)
    assert result['ssh_pub_key_facts']['ssh_host_pub_keys']

# Generated at 2022-06-13 03:42:57.215441
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    module = None

    keydirs = ['/etc/ssh']

    for keydir in keydirs:
        key_filename = '%s/ssh_host_rsa_key.pub' % keydir
        keydata = get_file_content(key_filename)
        if keydata is not None:
            (keytype, key) = keydata.split()[0:2]


# Generated at 2022-06-13 03:43:07.737572
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    ssh_pub_key_facts = {}

    algos = ('rsa', 'dsa', 'ecdsa', 'ed25519')

    keydirs = ['/etc/ssh', '/etc/openssh', '/etc']

    for keydir in keydirs:
        for algo in algos:
            factname = 'ssh_host_key_%s_public' % algo
            if factname in ssh_pub_key_facts:
                # a previous keydir was already successful, stop looking
                # for keys
                return ssh_pub_key_facts
            key_filename = '%s/ssh_host_%s_key.pub' % (keydir, algo)
            keydata = get_file_content(key_filename)

# Generated at 2022-06-13 03:43:08.225407
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    assert SshPubKeyFactCollector().collect() == {}

# Generated at 2022-06-13 03:43:13.890144
# Unit test for method collect of class SshPubKeyFactCollector

# Generated at 2022-06-13 03:43:23.522805
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    import tempfile
    import os

    # Create temporary directory
    tmpdir = tempfile.mkdtemp(prefix='ansible_test_ssh_collector')

    # Construct keys