

# Generated at 2022-06-13 03:33:29.887424
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from ansible.module_utils.facts import Facts
    from ansible.module_utils.facts.inputs import ssh_host_key_ecdsa_public_keytype
    from ansible.module_utils.facts.inputs import ssh_host_key_ecdsa_public_notes
    from ansible.module_utils.facts.inputs import ssh_host_key_ecdsa_public_version

    module = ''

# Generated at 2022-06-13 03:33:37.981812
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    '''test method SshPubKeyFactCollector.collect'''
    from ansible.module_utils.facts import FactCollector

    # Create an instance of SshPubKeyFactCollector
    fact_collector = FactCollector(
        collectors=[SshPubKeyFactCollector])

    # Call method collect
    facts_dict = fact_collector.collect(module=None, collected_facts=None)

    # Check that the method returned a dictionary
    assert(isinstance(facts_dict, dict))

    # Check that the dictionary contains the expected keys

# Generated at 2022-06-13 03:33:45.084577
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    class EmptyModule(object):
        pass

    # Test with all empty
    ssh_pub_key_facts = SshPubKeyFactCollector.collect(EmptyModule(), {})
    assert ssh_pub_key_facts == {}

    # Test with no ssh_host_key_*_public facts
    collected_facts = {'ssh_host_pub_keys': 'test_ssh_host_pub_keys'}
    ssh_pub_key_facts = SshPubKeyFactCollector.collect(EmptyModule(), collected_facts)
    assert ssh_pub_key_facts == {}

# Generated at 2022-06-13 03:33:48.189375
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # Create an instance of SshPubKeyFactCollector
    collector = SshPubKeyFactCollector()
    # Call method collect of SshPubKeyFactCollector
    result = collector.collect()
    # Checking if result is empty
    assert result == {}

# Generated at 2022-06-13 03:33:58.239047
# Unit test for method collect of class SshPubKeyFactCollector

# Generated at 2022-06-13 03:34:06.661912
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    '''
    This is a functional test for the method collect of class SshPubKeyFactCollector.
    It tests the "happy" path of this method.
    '''
    from ansible.module_utils._text import to_bytes

    # Create a module object to use in the function collect of
    # class SshPubKeyFactCollector
    module = AnsibleModule(argument_spec={})

    # Create a SshPubKeyFactCollector object
    ssh_pub_key_fact_collector = SshPubKeyFactCollector()

    # Create a fact_collector object
    fact_collector = BaseFactCollector()

    # Create a dictionary with empty dictionary as value and
    # as key the name of the class SshPubKeyFactCollector

# Generated at 2022-06-13 03:34:16.120611
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    import sys
    sys.path = ['', '..'] + sys.path[1:]
    from ansible.module_utils.facts import FactCollector
    module = type('MockModule', (), {'params': {'gather_subset': ['!all']}})
    ssh_pub_key_facts = SshPubKeyFactCollector(module).collect()


# Generated at 2022-06-13 03:34:26.067168
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    SshPubKeyFactCollector_obj = SshPubKeyFactCollector()


# Generated at 2022-06-13 03:34:36.728506
# Unit test for method collect of class SshPubKeyFactCollector

# Generated at 2022-06-13 03:34:45.383317
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # fact collection for module parameter gather_subset=['ssh_pub_keys']
    module_params = dict(
        gather_subset=['ssh_pub_keys']
    )
    # expected facts with key of 'ssh_host_key_dsa_public' missing
    # intentionally

# Generated at 2022-06-13 03:34:52.887094
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    module = Mock()
    collected_facts = {"ansible_architecture":"x86_64"}
    ssh_pub_keys_collector = SshPubKeyFactCollector(module=module, collected_facts=collected_facts)
    ssh_pub_keys_collector.collect()

    assert "ssh_host_key_dsa_public" in ssh_pub_keys_collector.collect()


# Generated at 2022-06-13 03:35:01.342121
# Unit test for method collect of class SshPubKeyFactCollector

# Generated at 2022-06-13 03:35:09.148682
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    class MockModule():
        def __init__(self):
            self.params = { 'gather_subset' : ['all'] }

    class MockCollector():
        def collect(self):
            return { 'fact_name' : 'fact value'}

    collector = SshPubKeyFactCollector(MockModule())
    collector.collectors = [MockCollector()]
    returned = collector.collect()
    assert 'fact_name' in returned.keys(), 'fact_name must be in returned'

# Generated at 2022-06-13 03:35:16.156117
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # Set up test data
    ssh_pub_key_facts = {
        'ssh_host_key_dsa_public': 'DSAKEY',
        'ssh_host_key_dsa_public_keytype': 'ssh-dss',
        'ssh_host_key_rsa_public': 'RSAKEY',
        'ssh_host_key_rsa_public_keytype': 'ssh-rsa',
        'ssh_host_key_ecdsa_public': 'ECKEY',
        'ssh_host_key_ecdsa_public_keytype': 'ecdsa-sha2-nistp256',
        'ssh_host_key_ed25519_public': '25519KEY',
        'ssh_host_key_ed25519_public_keytype': 'ssh-ed25519',
    }

# Generated at 2022-06-13 03:35:20.032586
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    import pytest
    from ansible.module_utils.facts import FactCollector
    test_collector = FactCollector(['ssh_pub_keys'], [__name__])
    test_collector.collect(None, None)

# Generated at 2022-06-13 03:35:24.491247
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from ansible.module_utils.facts.collector import collect_subset
    from ansible.module_utils.facts.collector import inherit_facts_from_file

    SshPubKeyFactCollector.collect()

    inherit_facts_from_file()

    collect_subset()

    return(None)

# Generated at 2022-06-13 03:35:32.471241
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from ansible.module_utils.facts.utils import get_file_content
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.linux.ssh_pub_keys import SshPubKeyFactCollector
    from ansible.module_utils._text import to_text
    import os
    import shutil
    import tempfile

    # backup os.environ
    old_environ = {}
    for k in os.environ:
        old_environ[k] = os.environ[k]
    old_get_file_content = get_file_content

    get_file_content = lambda x: None
    # create a dir to store some test ssh key files
    tempdir = tempfile.mkdtemp()

    # store some test key files in the temp

# Generated at 2022-06-13 03:35:34.895344
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    results = SshPubKeyFactCollector().collect()

# vim: set expandtab: ts=4:sw=4

# Generated at 2022-06-13 03:35:46.808830
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    """Test SshPubKeyFactCollector.collect returns the expected ssh public keys."""
    #
    # Create an instance of SshPubKeyFactCollector
    #
    collector = SshPubKeyFactCollector()

    #
    # Create a fake list of ssh public keys and inject it into the fake filesystem
    #

# Generated at 2022-06-13 03:35:51.487082
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    collector = SshPubKeyFactCollector()
    ssh_pub_key_facts = collector.collect()
    assert isinstance(ssh_pub_key_facts, dict), '%s should be dict, but is %s' % (ssh_pub_key_facts, type(ssh_pub_key_facts))

# Generated at 2022-06-13 03:35:59.414299
# Unit test for method collect of class SshPubKeyFactCollector

# Generated at 2022-06-13 03:36:10.411217
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    pub_key_collector = SshPubKeyFactCollector()


# Generated at 2022-06-13 03:36:21.250495
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    import os
    import tempfile
    from ansible.module_utils.facts.utils import get_file_content, set_file_content

    FAKE_DATA_DIR = tempfile.mkdtemp()

    # list of directories to check for ssh keys
    # used in the order listed here, the first one with keys is used
    keydirs = ['/etc/ssh', '/etc/openssh', '/etc']

    algos = ('dsa', 'rsa', 'ecdsa', 'ed25519')


# Generated at 2022-06-13 03:36:31.899617
# Unit test for method collect of class SshPubKeyFactCollector

# Generated at 2022-06-13 03:36:39.584201
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    import os
    import tempfile
    import sys

    # Create a temporary directory
    tmpdir = tempfile.mkdtemp()

    # Create a temporary file that we'll write to
    fd, old_sys_modules = tempfile.mkstemp()
    fh = os.fdopen(fd, 'wb')
    fh.close()
    # Create the file
    open(old_sys_modules, 'a').close()

    # Write something to the file
    with open(old_sys_modules, 'w') as fh:
        fh.write('This is a test for SshPubKeyFactCollector')

    # Initialize the collector
    ssh_pub_key_fact_collector = SshPubKeyFactCollector(module=None, collected_facts=None)

    # Add content to system_profiler


# Generated at 2022-06-13 03:36:46.006773
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from ansible.module_utils.facts.collector import FactCollector
    from ansible.module_utils.facts import gather_facts

    # Mock fact collection (this is normally done by gather_facts)
    facts = {}
    for f in FactCollector.fact_classes:
        fact_class = FactCollector.fact_classes[f]
        fact = fact_class(gather_facts.__loader__)
        fact_dict = fact.collect(module=None, collected_facts=None)
        facts.update(fact_dict)

    assert 'ssh_host_key_rsa_public' in facts

# Generated at 2022-06-13 03:36:47.505167
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    x = SshPubKeyFactCollector()
    x.collect()
    assert isinstance(x.collect(),dict)

# Generated at 2022-06-13 03:36:58.222316
# Unit test for method collect of class SshPubKeyFactCollector

# Generated at 2022-06-13 03:37:04.257729
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from ansible.module_utils.facts import ansible_collections
    from ansible.module_utils.facts.collector import collect_facts
    import os

    # reset the ansible_collections to be empty
    ansible_collections[:] = []

    # create the ssh keys for testing
    dirpath = '/tmp/ssh_pub_key_facts_ut'
    os.makedirs(dirpath)

# Generated at 2022-06-13 03:37:15.583784
# Unit test for method collect of class SshPubKeyFactCollector

# Generated at 2022-06-13 03:37:28.570414
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    import os
    import tempfile
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.utils import get_file_content
    BaseFactCollector.collectors = []
    BaseFactCollector._collectors_cache = None
    m = SshPubKeyFactCollector()
    fd, test_facts_file = tempfile.mkstemp()
    os.close(fd)
    fd, test_facts_file2 = tempfile.mkstemp()
    os.close(fd)

# Generated at 2022-06-13 03:37:40.390378
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from ansible.module_utils.facts import TestModule
    collected_facts = dict()
    mp = TestModule(collect_fixture)
    SshPubKeyFactCollector().collect(mp, collected_facts)
    SshPubKeyFactCollector().populate_fact_cache(mp, collected_facts)

# Generated at 2022-06-13 03:37:50.027620
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from ansible.module_utils.facts.collector import FactsCollector
    from ansible.module_utils.facts.collectors.ssh_pub_key_fact_collector import SshPubKeyFactCollector
    from ansible.module_utils.facts.utils import mock_ansible_module
    from ansible.module_utils._text import to_bytes

    module = mock_ansible_module()

    collector = FactsCollector(module=module, collectors=[SshPubKeyFactCollector()])
    collector.collect()

    keys = module.params['ansible_facts']['ssh_host_pub_keys']
    assert module.params['ansible_facts']['ssh_host_key_dsa_public'] == keys['dsa']

# Generated at 2022-06-13 03:37:59.063158
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    ssh_key_facts = {}
    algos = ('rsa', 'dsa', 'ecdsa', 'ed25519')
    for algo in algos:
        factname = 'ssh_host_key_%s_public' % algo
        ssh_key_facts[factname] = "test"

    collector = SshPubKeyFactCollector()
    assert collector.collect(collected_facts=ssh_key_facts) is None
    collector._fact_ids.add('not_existing_fact')
    assert collector.collect(collected_facts=ssh_key_facts) is not None



# Generated at 2022-06-13 03:38:06.934633
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():

    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.utils import FactsFiles
    from ansible.module_utils.facts.collector import Collector
    import os

    tmpdir = "/tmp/ansible_test_collector_facts"
    os.environ['ANSIBLE_COLLECTORS_PATH'] = tmpdir
    os.makedirs(tmpdir)

    # create files

# Generated at 2022-06-13 03:38:14.337213
# Unit test for method collect of class SshPubKeyFactCollector

# Generated at 2022-06-13 03:38:25.540697
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils.facts.utils import get_file_content

    # mock keys in test keys dir
    testdir = '/tmp/ansible_test_keys'
    get_file_content.side_effect = lambda x: 'testkey1' if x == testdir + '/ssh_host_dsa_key.pub' else x
    fc = FactCollector(None, None)
    fc.collectors = [SshPubKeyFactCollector()]
    fc.collectors[0].fact_path = testdir
    facts = fc.collect(None, None)
    assert facts['ssh_host_key_dsa_public'] == 'testkey1'
    assert 'ssh_host_key_ecdsa_public' not in facts


# Generated at 2022-06-13 03:38:35.278294
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    keydata = """ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIEg2QmQ9XW/ZJjhgByesE3q5o5i5IR541zbwNt5Yn1Mb9
"""

# Generated at 2022-06-13 03:38:38.970527
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    result = SshPubKeyFactCollector().collect()
    assert len(result) >= 1
    assert result['ssh_host_key_dsa_public'] == result['ssh_host_pub_keys']['dsa']

# Generated at 2022-06-13 03:38:48.912682
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    class Module(object):
        pass
    collect_facts = SshPubKeyFactCollector()
    module = Module()
    result = collect_facts.collect(module, None)
    assert len(result.keys()) == 5
    assert 'ssh_host_key_dsa_public' in result.keys()
    assert 'ssh_host_key_rsa_public' in result.keys()
    assert 'ssh_host_key_ecdsa_public' in result.keys()
    assert 'ssh_host_key_ed25519_public' in result.keys()
    assert 'ssh_host_pub_keys' in result.keys()

# Generated at 2022-06-13 03:38:58.657360
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # test no keys
    ssh_pub_key_collector = SshPubKeyFactCollector()
    ssh_pub_key_facts = ssh_pub_key_collector.collect(collected_facts=None)
    assert 'ssh_host_key_dsa_public' not in ssh_pub_key_facts
    assert 'ssh_host_key_rsa_public' not in ssh_pub_key_facts
    assert 'ssh_host_key_ecdsa_public' not in ssh_pub_key_facts
    assert 'ssh_host_key_ed25519_public' not in ssh_pub_key_facts

# Generated at 2022-06-13 03:38:59.691126
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    f = SshPubKeyFactCollector()
    assert f.collect() is None

# Generated at 2022-06-13 03:39:04.327770
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():

    testcollected_facts = {
                            'ssh_host_rsa_public': 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQAB'
                          }

    expected_sshpubkey_facts = {
                            'ssh_host_rsa_public': 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQAB',
                            'ssh_host_rsa_public_keytype': 'ssh-rsa'
                          }

    testobj = SshPubKeyFactCollector()

    assert testobj.collect(collected_facts=testcollected_facts) == expected_sshpubkey_facts

# Generated at 2022-06-13 03:39:15.483322
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    ssh_pub_key_facts = dict()

# Generated at 2022-06-13 03:39:22.783504
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    module = None
    collected_facts = {'ansible_system': 'Linux'}
    c = SshPubKeyFactCollector()
    c.collect(module, collected_facts)
    assert 'ssh_host_key_dsa_public' in collected_facts
    assert 'ssh_host_key_rsa_public' in collected_facts
    assert 'ssh_host_key_ecdsa_public' in collected_facts
    assert 'ssh_host_key_ed25519_public' in collected_facts


# Generated at 2022-06-13 03:39:29.320749
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # Create a new instance of SshPubKeyFactCollector
    test_instance = SshPubKeyFactCollector()

    # Create a new instance of AnsibleModule
    test_module = AnsibleModule(argument_spec={})

    # Create a new instance of collected_facts
    test_collected_facts = {}

    # Call the method collect of class SshPubKeyFactCollector
    result = test_instance.collect(module=test_module, collected_facts=test_collected_facts)

    # Check if the result is as expected
    assert isinstance(result, dict)
    assert 'ssh_host_key_dsa_public' in result
    assert 'ssh_host_key_rsa_public' in result
    assert 'ssh_host_key_ecdsa_public' in result

# Generated at 2022-06-13 03:39:31.420596
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    test_collector_instance = SshPubKeyFactCollector()

    assert test_collector_instance.collect().has_key('ssh_host_key_rsa_public')
    assert test_collector_instance.collect().has_key('ssh_host_key_rsa_public_keytype')

# Generated at 2022-06-13 03:39:41.261555
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # Test for an existing key pair with the ssh keys in a standard OpenSSH
    # key directory
    ssh_pub_key_facts = SshPubKeyFactCollector().collect()

    assert 'ssh_host_key_rsa_public' in ssh_pub_key_facts
    assert 'ssh_host_key_rsa_public_keytype' in ssh_pub_key_facts

# Generated at 2022-06-13 03:39:50.420998
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    import modules.sshpubkeyfactcollector_sshpubkeyfactcollector
    module = modules.sshpubkeyfactcollector_sshpubkeyfactcollector.SshPubKeyFactCollector()
    facts = module.collect()
    assert facts is not None
    assert 'ssh_host_key_ed25519_public' in facts
    assert 'ssh_host_key_rsa_public' in facts
    assert 'ssh_host_key_ecdsa_public' in facts
    assert 'ssh_host_key_ed25519_public_keytype' in facts
    assert 'ssh_host_key_rsa_public_keytype' in facts
    assert 'ssh_host_key_ecdsa_public_keytype' in facts

# Generated at 2022-06-13 03:39:59.979437
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from ansible.module_utils.facts import FactsCollector
    from ansible.module_utils.facts.collector import collect_subset
    from ansible.module_utils.facts.collectors import SshPubKeyFactCollector
    from ansible.module_utils.facts.utils import get_file_content

    class FakeModule:
        def __init__(self, ansible_facts):
            self.ansible_facts = ansible_facts

    class FakeFactsCollector(FactsCollector):
        def __init__(self, module):
            self.module = module
            self.fact_collectors = [SshPubKeyFactCollector()]

    class FakeUtilsModule(object):
        def __init__(self):
            self.file_exists = Mock(return_value=False)


# Generated at 2022-06-13 03:40:11.858627
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from ansible.module_utils.facts.ssh_pub_key import SshPubKeyFactCollector

    module = 'testmodule'
    test_collector = SshPubKeyFactCollector()
    # test with all keys present
    ssh_host_key_rsa_public_filename = '/etc/ssh/ssh_host_rsa_key.pub'

# Generated at 2022-06-13 03:40:21.501517
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    import os
    import tempfile
    import ansible.module_utils.facts.collectors.ssh_pub_keys as ssh_pub_keys
    import ansible.module_utils.facts.utils as facts_utils
    import ansible.module_utils.facts.collectors.base as base_collector
    import ansible.modules.system.facts as facts

    #
    # test with no ssh keys present
    #
    collect = ssh_pub_keys.SshPubKeyFactCollector().collect()
    assert 'ssh_host_key_dsa_public' not in collect
    assert 'ssh_host_key_rsa_public' not in collect
    assert 'ssh_host_key_ecdsa_public' not in collect
    assert 'ssh_host_key_ed25519_public' not in collect

    #
   

# Generated at 2022-06-13 03:40:31.929328
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():

    def ssh_host_key_dsa_public():
        ssh_host_key_dsa_public = 'ssh-dss AAAAAAA'
        return ssh_host_key_dsa_public

    def ssh_host_key_rsa_public():
        ssh_host_key_rsa_public = 'ssh-rsa BBBBBBB'
        return ssh_host_key_rsa_public

    def ssh_host_key_ecdsa_public():
        ssh_host_key_ecdsa_public = 'ssh-ecdsa CCCCCCC'
        return ssh_host_key_ecdsa_public

    def ssh_host_key_ed25519_public():
        ssh_host_key_ed25519_public = 'ssh-ed25519 DDDDDDD'
        return ssh_host_

# Generated at 2022-06-13 03:40:36.909351
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector
    import tempfile
    from ansible.module_utils.facts.utils import get_file_content
    from os.path import exists

    bfc = BaseFactCollector()
    spkfc = SshPubKeyFactCollector()

    with tempfile.TemporaryDirectory() as tmpdirname:
        dsa_key_filename = '%s/ssh_host_dsa_key.pub' % tmpdirname

# Generated at 2022-06-13 03:40:42.830992
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # Init a SshPubKeyFactCollector object
    ssh_pub_key = SshPubKeyFactCollector()

    # Call method collect
    result = ssh_pub_key.collect()
    assert 'ssh_host_key_dsa_public' in result
    assert 'ssh_host_key_rsa_public' in result


# Generated at 2022-06-13 03:40:48.911886
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    module_mock = DummyModule()
    collected_facts = {}
    fact_collector = SshPubKeyFactCollector()
    collected_facts = fact_collector.collect(module=module_mock,
                                             collected_facts=collected_facts)
    # check if the ssh_pub_key facts are collected

# Generated at 2022-06-13 03:40:58.123480
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    collector = SshPubKeyFactCollector()
    facts = {}

    # given
    ssh_pub_key_facts = collector.collect()

    # then
    assert ssh_pub_key_facts['ssh_host_key_rsa_public'] == 'AAAAB3NzaC1yc2EAAAABIwAAAQEAklOUpkDHrfHY17SbrmTIpNLTGK9Tjom/BWDSU'
    assert ssh_pub_key_facts['ssh_host_key_rsa_public_keytype'] == 'ssh-rsa'

# Generated at 2022-06-13 03:41:04.940028
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    module = None
    collected_facts = {}

    # define expected values based on installed ssh keys
    expected_values = {'factname': 'ssh_host_key_%s_public',
                       'facttype': 'string',
                       'facttypenull': False,
                       'factabsent': False}

    # define expected dictionary of values based on installed ssh keys
    expected_results = dict()

# Generated at 2022-06-13 03:41:14.985970
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    # Collectors is a private instance of FactCollector

    mingw = ("name='Microsoft Windows' "
             "pretty_name='Windows 10 Enterprise' "
             "ansi_color_support=True "
             "ansible_facts={'ansible_distribution': 'Microsoft', "
             "'ansible_distribution_major_version': '10', "
             "'ansible_distribution_version': 'Enterprise', "
             "'ansible_distribution_release': '2016 LTSB'}")

    facts_dict = {'kernel': 'Windows', 'ansible_system': mingw}

    sshpubkeyfact = SshPubKeyFactCollector()
    collectors = Collector()
    collectors._collect(sshpubkeyfact, facts_dict)


# Generated at 2022-06-13 03:41:21.632241
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    class mock_module(object):
        def __init__(self):
            pass

    class mock_collected_facts(object):
        def __init__(self):
            self.facts = {'whitelisted_collected_facts': ['foo']}

    mock_module_obj = mock_module()
    mock_collected_facts_obj = mock_collected_facts()

    ssh_pub_key_collector = SshPubKeyFactCollector(module=mock_module_obj,
                                                   collected_facts=mock_collected_facts_obj)

    assert 'foo' in mock_collected_facts_obj.facts['whitelisted_collected_facts']
    assert 'ssh_host_pub_keys' not in mock_collected_facts_obj.facts

    ssh_pub_key_

# Generated at 2022-06-13 03:41:35.299509
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    with open("/etc/ssh/ssh_host_rsa_key.pub", "w") as f:
        f.write("ssh-rsa key")
    with open("/etc/ssh/ssh_host_dsa_key.pub", "w") as f:
        f.write("ssh-dsa key")
    with open("/etc/ssh/ssh_host_ecdsa_key.pub", "w") as f:
        f.write("ecdsa-sha2-nistp256 key")
    with open("/etc/ssh/ssh_host_ed25519_key.pub", "w") as f:
        f.write("ssh-ed25519 key")

# Generated at 2022-06-13 03:41:43.825220
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    """
    The test case is executed by setting the environment
    variable SSH_KNOWN_HOSTS_FILE.
    """
    collector = SshPubKeyFactCollector()
    keys = collector.collect()
    assert keys.get('ssh_host_key_rsa_public_keytype') == "ssh-rsa"

# Generated at 2022-06-13 03:41:53.265378
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    c = SshPubKeyFactCollector()

# Generated at 2022-06-13 03:41:59.701139
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    """
    Test method collect
    """
    # pylint: disable=protected-access, missing-docstring
    fact_collector = SshPubKeyFactCollector()
    # Test collecting facts from missing files
    collected_facts = fact_collector.collect()
    assert collected_facts == {}

    # Test collecting facts from existing files
    collected_facts = fact_collector.collect(collected_facts)
    assert collected_facts is not None

# Generated at 2022-06-13 03:42:09.314085
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    import pytest
    from ansible.module_utils.facts import Facts
    from ansible.module_utils.facts import default_collectors

    # create temporary files to simulate the ssh pub keys
    # in typical locations

# Generated at 2022-06-13 03:42:11.068553
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    collector = SshPubKeyFactCollector()
    facts = collector.collect()
    assert 'ssh_host_pub_keys' in facts

# Generated at 2022-06-13 03:42:13.223702
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    assert SshPubKeyFactCollector.collect(None, {}) == {}

# Generated at 2022-06-13 03:42:17.382992
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    module = None
    fact_collector = SshPubKeyFactCollector()
    ssh_pub_key_facts = fact_collector.collect(module)
    assert ssh_pub_key_facts['ssh_host_key_ecdsa_public'] == ssh_pub_key_facts['ssh_host_key_ed25519_public']

# Generated at 2022-06-13 03:42:24.947023
# Unit test for method collect of class SshPubKeyFactCollector

# Generated at 2022-06-13 03:42:28.484680
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    module = None
    collected_facts = None
    SshPubKeyFactCollectorObj = SshPubKeyFactCollector()
    facts = SshPubKeyFactCollectorObj.collect(module, collected_facts)
    assert facts['ssh_host_key_dsa_public'] != None

# Generated at 2022-06-13 03:42:44.641253
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    import os
    import tempfile
    from ansible.module_utils.facts.collector import collected_facts
    from ansible.module_utils.facts.collectors.network.ssh_pub_keys import SshPubKeyFactCollector

    # local variables
    olddir = os.getcwd()
    algos = ('dsa', 'rsa', 'ecdsa', 'ed25519')
    expected_facts = {}

# Generated at 2022-06-13 03:42:52.557727
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    import inspect
    import os
    import shutil
    import tempfile

    class RawArgsMock(object):
        def __init__(self):
            # fixed static values for testing
            self.spooldir = '/var/lib/ansible'
            self.remote_tmp = '/tmp/.ansible/tmp'
            self.module_name = 'setup'

    class AnsibleModuleMock(object):
        def __init__(self):
            self.params = {}

    params = RawArgsMock()
    module = AnsibleModuleMock()

    # Test for empty key directories
    tmp_keydir = tempfile.mkdtemp(prefix = 'ansible_test_ssh_pub_keys_')

    collector = SshPubKeyFactCollector(module=module, params=params)
    facts_dict = collector._

# Generated at 2022-06-13 03:43:01.994218
# Unit test for method collect of class SshPubKeyFactCollector

# Generated at 2022-06-13 03:43:10.807613
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():

    # arrange
    import os
    import sys
    import tempfile

    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector import collect

    from ansible.module_utils.facts.utils import get_file_content
    from ansible.module_utils.facts.utils import get_file_lines

    from ansible.module_utils.facts.collectors.ssh_pub_key import SshPubKeyFactCollector

    fake_module = {'run_command': lambda x: [0, '', '']}

    _ssh_keys = {}
    _ssh_keys['rsa'] = '''ssh-rsa foo_rsa_key'''
    _ssh_keys['dsa'] = '''ssh-dss foo_dsa_key'''
   

# Generated at 2022-06-13 03:43:11.490399
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    """Test method collect of class SshPubKeyFactCollector."""
    pass

# Generated at 2022-06-13 03:43:20.118468
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # ssh_host_key_dsa_public not found but
    # ssh_host_key_rsa_public and ssh_host_key_ed25519_public are found
    # there are no other key to find
    collector = SshPubKeyFactCollector()
    facts = collector.collect(None, {})
    assert sorted(facts.keys()) == sorted(['ssh_host_key_rsa_public',
                                           'ssh_host_key_rsa_public_keytype',
                                           'ssh_host_key_ed25519_public',
                                           'ssh_host_key_ed25519_public_keytype'])