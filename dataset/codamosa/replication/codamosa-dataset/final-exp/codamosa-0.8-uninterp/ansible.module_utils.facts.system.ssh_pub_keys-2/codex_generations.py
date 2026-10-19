

# Generated at 2022-06-13 03:33:29.790567
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    import os
    import tempfile
    import shutil
    import pytest
    from ansible.module_utils.facts.utils import get_file_content

    datadir = "/etc/ssh"
    if not os.path.isdir(datadir):
        datadir = "/etc/openssh"
    if not os.path.isdir(datadir):
        datadir = tempfile.mkdtemp()


# Generated at 2022-06-13 03:33:37.901229
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # Initialize the collector to test with a fake key file
    ssh_pub_key_fact_collector = SshPubKeyFactCollector()
    ssh_pub_key_fact_collector.fact_namespace = 'fake_namespace'

    ssh_pub_key_fact_collector.patches = []
    ssh_pub_key_fact_collector.patches.append(
        {'target': 'os.path.exists', 'mock': lambda _: True})
    ssh_pub_key_fact_collector.patches.append(
        {'target': 'os.access', 'mock': lambda _, __: True})

# Generated at 2022-06-13 03:33:45.332237
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from ansible.module_utils.facts.collector.ssh_pub_key import SshPubKeyFactCollector

    # Create a dictionary with the facts to be collected
    test_facts = {}

    # Instantiate the SshPubKeyFactCollector object
    ssh_pub_key_fact_collector = SshPubKeyFactCollector()

    # Call method collect of the SshPubKeyFactCollector object
    returned_facts = ssh_pub_key_fact_collector.collect(collected_facts=test_facts)

    # Assert if returned facts are what is expected
    assert returned_facts == {}


# Generated at 2022-06-13 03:33:51.492835
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    testmodule = AnsibleModule(argument_spec={'gather_subset': dict(type='list')})
    testmodule.params.update({
        'gather_subset': ['!all', 'network', 'ssh_pub_keys']
    })

    collector = SshPubKeyFactCollector(
        testmodule._name,
        testmodule,
        testmodule.params,
        testmodule.exit_json)
    ssh_pub_key_facts = collector.collect()
    assert ssh_pub_key_facts == {}

# Generated at 2022-06-13 03:33:52.110116
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    pass

# Generated at 2022-06-13 03:34:01.002104
# Unit test for method collect of class SshPubKeyFactCollector

# Generated at 2022-06-13 03:34:03.147790
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    collector = SshPubKeyFactCollector()

    output = collector.collect(collected_facts=[])

    assert isinstance(output, dict)

# Generated at 2022-06-13 03:34:13.626363
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    import os

    # create a temporary directory and cd into it
    import tempfile
    tempdir = tempfile.mkdtemp()
    cwd = os.getcwd()
    os.chdir(tempdir)
    # create a 'test' subdirectory
    testdir = os.path.join(tempdir, 'test')
    os.mkdir(testdir)

    # create some ssh pubkey files in this temporary directory
    algos = ('dsa', 'rsa', 'ecdsa', 'ed25519')

# Generated at 2022-06-13 03:34:24.963410
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from ansible.module_utils.facts.collector import CollectedFact
    import os
    import pytest

    # set up a temp directory to hold keys
    tmpdir = os.path.realpath(pytest.ensuretemp('test_SshPubKeyFactCollector_collect'))
    os.mkdir(tmpdir)

    # create some fake keys
    ssh_host_key_types = {'dsa': 'ssh-dss',
                          'rsa': 'ssh-rsa',
                          'ecdsa': 'ecdsa-sha2-nistp256',
                          'ed25519': 'ssh-ed25519'}

    key_filenames = {}

# Generated at 2022-06-13 03:34:26.529250
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    ssh_pub_key_fact_collector = SshPubKeyFactCollector()
    ssh_pub_key_fact_collector.collect()

# Generated at 2022-06-13 03:34:39.511945
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():

    # Create instance of class ModuleUtils
    ssh_pub_key_fact_collector = SshPubKeyFactCollector()

    # Check that fact_ids is correctly initialized
    assert set(ssh_pub_key_fact_collector.fact_ids()) == set(['ssh_host_pub_keys',
                                                              'ssh_host_key_dsa_public',
                                                              'ssh_host_key_rsa_public',
                                                              'ssh_host_key_ecdsa_public',
                                                              'ssh_host_key_ed25519_public'])

    # Test facts compilation
    facts = ssh_pub_key_fact_collector.collect()

    # Check facts
    assert len(facts) > 0, 'No facts found'

    # Check keys type

# Generated at 2022-06-13 03:34:46.995014
# Unit test for method collect of class SshPubKeyFactCollector

# Generated at 2022-06-13 03:34:56.967259
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    '''Unit test for method collect of class SshPubKeyFactCollector'''
    SUT = SshPubKeyFactCollector()

# Generated at 2022-06-13 03:35:10.081704
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # add ssh_host_key_dsa_public fact to collected_facts
    collected_facts = {'ssh_host_key_dsa_public': 'test_ssh_host_key_dsa_public'}
    # add ssh_host_key_rsa_public fact to collected_facts
    collected_facts = {'ssh_host_key_rsa_public': 'test_ssh_host_key_rsa_public'}
    # add ssh_host_key_ecdsa_public fact to collected_facts
    collected_facts = {'ssh_host_key_ecdsa_public': 'test_ssh_host_key_ecdsa_public'}
    # add ssh_host_key_ed25519_public fact to collected_facts

# Generated at 2022-06-13 03:35:16.547246
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    """
    Check that collect method of SshPubKeyFactCollector class works
    as expected.
    """
    # Construct a SshPubKeyFactCollector object
    collect_obj = SshPubKeyFactCollector()

    # Check that the ssh_pub_key_facts dictionary returned by the collect
    # method of the SshPubKeyFactCollector object is well-formed with
    # the expected keys and values.
    ssh_pub_key_facts = collect_obj.collect()
    assert isinstance(ssh_pub_key_facts, dict)
    for factname in collect_obj._fact_ids:
        expected_value = None
        assert factname in ssh_pub_key_facts

# Generated at 2022-06-13 03:35:27.169711
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    import os
    import tempfile

    # Create a temporary directory
    tmpdir = tempfile.mkdtemp()

    # Create a temporary file that is empty
    tmpfile1 = tempfile.mkstemp(dir=tmpdir)
    os.close(tmpfile1[0])

    # Create an SSH key for testing
    tmpfile2 = tempfile.mkstemp(dir=tmpdir, suffix=".pub")
    os.write(tmpfile2[0],
             "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGh+ZaY7W8EIVJhT7Tjb1DpBt+S8LXJl1VzLqCPYq7W ohai")
    os.close(tmpfile2[0])

    # Create a second temporary file that is

# Generated at 2022-06-13 03:35:37.002805
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    import platform
    import tempfile
    import shutil

    # Create temp directory to work in
    tmpdir = tempfile.mkdtemp()

    # We need to use the same OS as the tested class
    if platform.system() == 'Linux':
        pubkeytype = 'ssh-ed25519'
        pubkey_filename = 'ssh_host_ed25519_key.pub'
    else:
        pubkeytype = 'ssh-rsa'
        pubkey_filename = 'ssh_host_rsa_key.pub'

    # Generate public and private keys
    os.system("ssh-keygen -N '' -f %s/ssh_host_ed25519_key" % tmpdir)
    # Rename public key

# Generated at 2022-06-13 03:35:49.180873
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    import json
    import os

    from ansible.module_utils.facts.utils import get_file_content

    # Creating fake tempfile for ssh_host_rsa_key.pub

# Generated at 2022-06-13 03:35:59.801180
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    import os
    import mock
    import ansible.utils.path


# Generated at 2022-06-13 03:36:10.507719
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    mock_module = MagicMock()
    mock_collected_facts = dict()
    sshpubkey_fact_collector = SshPubKeyFactCollector()
    sshpubkey_fact_collector.collect(module=mock_module, 
         collected_facts=mock_collected_facts)
    print("\nUnit test for method collect of class SshPubKeyFactCollector\n")
    print("Able to collect SSH Pub Key Facts: %s" % 
           (mock_collected_facts is not None))
    ssh_pub_keys = mock_collected_facts.get("ssh_host_pub_keys")
    print("Able to collect SSH Pub Key Facts: %s" % 
           (ssh_pub_keys is not None))

# Generated at 2022-06-13 03:36:25.522332
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    algos = ('dsa', 'rsa', 'ecdsa', 'ed25519')
    keydirs = ['/etc/ssh', '/etc/openssh', '/etc']

# Generated at 2022-06-13 03:36:35.432182
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from ansible.module_utils.facts.collector.ssh_pub_key import SshPubKeyFactCollector

    # no keys found
    ssh_pub_key_facts = SshPubKeyFactCollector({}).collect()
    assert ssh_pub_key_facts == {}

    # keys found
    ssh_pub_key_facts = SshPubKeyFactCollector({'open_mock': True}).collect()
    assert len(ssh_pub_key_facts) >= 4

    # when only one key is present
    ansible_facts = {'open_mock': True, '__tmpdir': '/tmp'}
    ssh_pub_key_facts = SshPubKeyFactCollector(ansible_facts).collect()
    assert len(ssh_pub_key_facts) == 1

# Generated at 2022-06-13 03:36:44.671759
# Unit test for method collect of class SshPubKeyFactCollector

# Generated at 2022-06-13 03:36:50.746480
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    ssh_pub_key_facts = {'ssh_host_key_dsa_public': 'ssh-dss ABBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB= '}
    module = None
    collected_facts = None
    collector = SshPubKeyFactCollector()
    result = collector.collect(module, collected_facts)
    assert result == ssh_pub_key_facts

# Generated at 2022-06-13 03:36:59.981154
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():

    module = None
    collected_facts = None
    ssh_pub_key_facts = ['ssh_host_pub_keys', 'ssh_host_key_dsa_public', 'ssh_host_key_rsa_public', 'ssh_host_key_ecdsa_public', 'ssh_host_key_ed25519_public']
    for key in ssh_pub_key_facts:
        ssh_pub_key_facts = key

    def test_file_content(path):
        return True
    setattr(SshPubKeyFactCollector, '_get_file_content', test_file_content)

    result = SshPubKeyFactCollector().collect(module, collected_facts)
    assert result == ssh_pub_key_facts

# Generated at 2022-06-13 03:37:01.599108
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    test = SshPubKeyFactCollector()
    print(test.collect())

# Generated at 2022-06-13 03:37:12.566865
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    """ Test all the collect method scenarios. """
    class MockAnsibleModule(object):
        def __init__(self, **kwargs):
            self.params = kwargs

    SshPubKeyFactCollector.COLLECT_DATA = {}
    ssh_pub_key_facts = SshPubKeyFactCollector().collect(
        MockAnsibleModule(gather_subset=SshPubKeyFactCollector()._fact_ids))
    assert 'ssh_host_key_dsa_public' in ssh_pub_key_facts
    assert 'ssh_host_key_rsa_public' in ssh_pub_key_facts
    assert 'ssh_host_key_ecdsa_public' in ssh_pub_key_facts
    assert 'ssh_host_key_ed25519_public' in ssh_pub_key_

# Generated at 2022-06-13 03:37:22.230358
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from ansible.module_utils.facts.utils import AnsibleFactCollector
    from ansible.module_utils.facts.collector import FactCollector

    module = None
    fact_collector = FactCollector()
    ansible_fact_collector = AnsibleFactCollector(fact_collector=fact_collector)
    fact_collector.populate_fact_cache(ansible_fact_collector=ansible_fact_collector)

    ssh_pub_key_facts = SshPubKeyFactCollector().collect(module=module, collected_facts=ansible_fact_collector.collected_facts)
    ssh_pub_key_fact_names = ssh_pub_key_facts.keys()
    # The test keys are generated using ssh-keygen -t <type>
    # The following tests fails if their names

# Generated at 2022-06-13 03:37:34.451521
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # get the insance of the SshPubKeyFactCollector class
    ssh_pub_key_collector = SshPubKeyFactCollector()

    # create a dict for collected_facts, this is the dict that
    # SshPubKeyFactCollector.collect method will add its facts to
    # also, add some extra facts to test if they are not deleted
    collected_facts = dict(
        ansible_cmdline=dict(
            chdir='/home/stack',
        ),
        dummy_fact='dummy_fact_value',
        ansible_test='test value',
        ansible_test2=dict(
            key1='value1',
            key2='value2',
            key3='value3',
        )
    )

    # call the collect method of SshPubKeyFactCollector
    ssh_pub

# Generated at 2022-06-13 03:37:46.223382
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    import os
    import tempfile
    import shutil
    import ansible.module_utils.facts.collector

    # create a temporary directory
    keydir = tempfile.mkdtemp()
    keyfiles_expected = {}
    keyfiles_expected['dsa'] = '%s/ssh_host_dsa_key.pub' % keydir
    keyfiles_expected['rsa'] = '%s/ssh_host_rsa_key.pub' % keydir
    keyfiles_expected['ecdsa'] = '%s/ssh_host_ecdsa_key.pub' % keydir
    keyfiles_expected['ed25519'] = '%s/ssh_host_ed25519_key.pub' % keydir
    keyfile_unexpected = '%s/ssh_host_key.pub' % keydir

   

# Generated at 2022-06-13 03:38:03.431806
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    '''Test ssh_pub_key facts with appropriate data.'''

    # Set up the module params.
    module = {}

    # Set up the collector object with the required args.
    fake_collected_facts = {}
    collector = SshPubKeyFactCollector(
                    module=module,
                    collected_facts=fake_collected_facts)

    # Execute the collect method with the required args.
    returned_facts = collector.collect(module=module,
                                       collected_facts=fake_collected_facts)

    # Assert that facts collect method returns a non-empty dict.
    assert isinstance(returned_facts, dict)
    assert returned_facts

    # Assert that the collect method has set the values correctly.

# Generated at 2022-06-13 03:38:09.502238
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    keydirs = ['/etc/ssh', '/etc/openssh', '/etc']
    algos = ('dsa', 'rsa', 'ecdsa', 'ed25519')

    for keydir in keydirs:
        for algo in algos:
            key_filename = '%s/ssh_host_%s_key.pub' % (keydir, algo)
            keydata = get_file_content(key_filename)
            if keydata is not None:
                (keytype, key) = keydata.split()[0:2]
                factname = 'ssh_host_key_%s_public' % algo
                fact_val = {
                    factname : key,
                    factname + '_keytype' : keytype
                }

# Generated at 2022-06-13 03:38:13.458634
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    """Validate that the collect method executes properly"""
    ssh_pub_keys_collector = SshPubKeyFactCollector()
    results = ssh_pub_keys_collector.collect()

    assert results is not None
    assert isinstance(results, dict)
    assert "ssh_host_key_rsa_public" in results
    assert "ssh_host_key_rsa_public_keytype" in results
    assert ssh_pub_keys_collector.name in results
    assert isinstance(results[ssh_pub_keys_collector.name], list)



# Generated at 2022-06-13 03:38:24.381304
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    factCollector = SshPubKeyFactCollector()
    # User for testing, get_file_content must be monkey patched in
    # order to test this
    from ansible.module_utils.facts import utils
    utils.get_file_content = lambda filename: None
    assert factCollector.collect() == {}
    utils.get_file_content = lambda filename: "ssh-rsa AAAA == AAAA"
    assert factCollector.collect() == {
        'ssh_host_key_rsa_public': 'AAAA',
        'ssh_host_key_rsa_public_keytype': 'ssh-rsa'
    }
    utils.get_file_content = lambda filename: None
    assert factCollector.collect() == {}

# Generated at 2022-06-13 03:38:34.217166
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    collector = SshPubKeyFactCollector({})
    facts = collector.collect()

    assert 'ssh_host_key_dsa_public' in facts
    assert 'ssh_host_key_rsa_public' in facts
    assert 'ssh_host_key_ecdsa_public' in facts
    assert 'ssh_host_key_ed25519_public' in facts
    assert 'ssh_host_key_dsa_public_keytype' in facts
    assert 'ssh_host_key_rsa_public_keytype' in facts
    assert 'ssh_host_key_ecdsa_public_keytype' in facts
    assert 'ssh_host_key_ed25519_public_keytype' in facts
    assert 'ssh_host_pub_keys' not in facts

# Generated at 2022-06-13 03:38:40.210587
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # Create an instance of SshPubKeyFactCollector class
    m = SshPubKeyFactCollector()
    # Check dict returned by method collect
    ssh_pub_keys_facts = m.collect()
    # Check if 'ssh_host_rsa_public' is in dict returned by method collect
    assert 'ssh_host_rsa_public' in ssh_pub_keys_facts

# Generated at 2022-06-13 03:38:47.566034
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    sshPubKeyFactCollector = SshPubKeyFactCollector()
    res = sshPubKeyFactCollector.collect()
    assert 'ssh_host_key_ecdsa_public' in res.keys(), res
    assert 'ssh_host_key_ecdsa_public_keytype' in res.keys(), res
    assert 'ssh_host_key_rsa_public' in res.keys(), res
    assert 'ssh_host_key_rsa_public_keytype' in res.keys(), res



# Generated at 2022-06-13 03:38:58.255349
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # instantiate the class
    ssh_pub_key_facts_collector = SshPubKeyFactCollector('/etc/ssh/keys')

    # set mocked return values of methods to avoid file system access

# Generated at 2022-06-13 03:39:08.878433
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():

    # Prepare
    import os
    import tempfile
    workdir = tempfile.mkdtemp()

# Generated at 2022-06-13 03:39:15.788284
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    """
    Test the collect method of SshPubKeyFactCollector class
    """
    mock_module = 'ansible_collected_facts'
    mock_facts = {}
    ssh_pub_key_facts = {'ssh_host_key_rsa_public': 'key', 'ssh_host_key_rsa_public_keytype': 'keytype'}

    collector = SshPubKeyFactCollector()
    assert ssh_pub_key_facts == collector.collect(mock_module, mock_facts)

# Generated at 2022-06-13 03:39:41.772529
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    ssh_pub_key_facts = {}

    # Testing w/o ssh_host_key files
    test_obj = SshPubKeyFactCollector()
    ssh_pub_key_facts = test_obj.collect()
    assert len(ssh_pub_key_facts) == 0

    # Testing with ssh_host_key files
    # Create the ssh_host_key files
    import os
    tempdir = os.path.abspath('./test_tempdir')
    sshdir = os.path.join(tempdir, 'etc', 'ssh')

# Generated at 2022-06-13 03:39:47.985097
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # Create an instance of class SshPubKeyFactCollector
    ssh_pub_key_fact_collector = SshPubKeyFactCollector()

    # Create a fact collection object
    collected_facts = dict()
    collected_facts = ssh_pub_key_fact_collector.collect(
        collected_facts=collected_facts)

    # Assert if the collected facts has 'ssh_host_pub_keys' fact
    assert 'ssh_host_pub_keys' in collected_facts

# Generated at 2022-06-13 03:39:57.827304
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    '''
    Unit test function for method collect of class SshPubKeyFactCollector
    '''
    from ansible.module_utils.facts.collector import FactCollector
    from ansible.module_utils.facts.collectors.network.ssh_pub_key import SshPubKeyFactCollector

    # Create a new SshPubKeyFactCollector instance
    obj = SshPubKeyFactCollector()

    # First, test for a case where the key files are not present
    facts = {}
    module = None
    provided_fact_names = None
    fact_cache = None
    obj.collect(module, facts)

    # Now test for a case where all key files are present, nothing to do

# Generated at 2022-06-13 03:40:03.985136
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # create an instance
    c = SshPubKeyFactCollector(dict(), dict())

    # test single key, no type check
    keys = c.collect(
        collected_facts={
            'sysctl_facts': { 'kernel.random.entropy_avail': 1000 }
            }
        )

# Generated at 2022-06-13 03:40:12.340276
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from tempfile import mkdtemp
    from shutil import rmtree
    from textwrap import dedent
    sshkey_tmpdir = mkdtemp()

# Generated at 2022-06-13 03:40:15.716401
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # Put together a mock module and call the collect
    module = None
    collected_facts = {}
    SshPubKeyFactCollector().collect(module, collected_facts)


# Generated at 2022-06-13 03:40:17.617489
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    sc = SshPubKeyFactCollector()
    res = sc.collect()
    assert type(res) is dict
    assert len(res) >= 5

# Generated at 2022-06-13 03:40:25.542751
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    fact_collector = SshPubKeyFactCollector()
    collected_facts = {}

# Generated at 2022-06-13 03:40:35.055711
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.collectors.base import BaseFactCollector

    collector = Collector()
    collector.add_collection(SshPubKeyFactCollector())
    facts = collector.collect()

    # expected output data
    ecdsa_public_key_filename = '/etc/ssh/ssh_host_ecdsa_key.pub'

# Generated at 2022-06-13 03:40:44.742124
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    '''Unit test for method collect of class SshPubKeyFactCollector'''
    SshPubKeyFactCollector = SshPubKeyFactCollector()
    ssh_pub_key_facts = SshPubKeyFactCollector.collect()
    assert 'ssh_host_key_dsa_public' in ssh_pub_key_facts
    assert 'ssh_host_key_rsa_public' in ssh_pub_key_facts
    assert 'ssh_host_key_ecdsa_public' in ssh_pub_key_facts
    assert 'ssh_host_key_ed25519_public' in ssh_pub_key_facts


# Generated at 2022-06-13 03:41:28.753450
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    ssh_pub_key_collector = SshPubKeyFactCollector()
    facts = ssh_pub_key_collector.collect()
    assert facts is not None
    assert 'ssh_host_pub_keys' not in facts
    assert 'ssh_host_key_dsa_public' in facts
    assert 'ssh_host_key_rsa_public' in facts
    assert 'ssh_host_key_ecdsa_public' in facts
    assert 'ssh_host_key_ed25519_public' in facts
    assert 'ssh_host_key_dsa_public_keytype' in facts
    assert 'ssh_host_key_rsa_public_keytype' in facts
    assert 'ssh_host_key_ecdsa_public_keytype' in facts

# Generated at 2022-06-13 03:41:36.276251
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    ssh_pub_key_facts = SshPubKeyFactCollector().collect()
    assert isinstance(ssh_pub_key_facts, dict)
    assert 'ssh_host_key_ecdsa_public' in ssh_pub_key_facts
    assert 'ssh_host_key_ecdsa_public_keytype' in ssh_pub_key_facts
    assert 'ssh_host_key_ed25519_public' in ssh_pub_key_facts
    assert 'ssh_host_key_ed25519_public_keytype' in ssh_pub_key_facts
    assert 'ssh_host_key_rsa_public' in ssh_pub_key_facts
    assert 'ssh_host_key_rsa_public_keytype' in ssh_pub_key_facts

# Generated at 2022-06-13 03:41:44.038787
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    ssh_pub_key_facts = {}
    algos = ('dsa', 'rsa', 'ecdsa', 'ed25519')
    # list of directories to check for ssh keys
    # used in the order listed here, the first one with keys is used
    keydirs = ['/etc/ssh', '/etc/openssh', '/etc']
    for keydir in keydirs:
        for algo in algos:
            factname = 'ssh_host_key_%s_public' % algo
            if factname in ssh_pub_key_facts:
                # a previous keydir was already successful, stop looking
                # for keys
                print(ssh_pub_key_facts)

if __name__ == '__main__':
    test_SshPubKeyFactCollector_collect()

# Generated at 2022-06-13 03:41:50.093942
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    ssh_pub_key_facts = SshPubKeyFactCollector().collect()
    assert 'ssh_host_key_rsa_public' in ssh_pub_key_facts
    assert 'ssh_host_key_rsa_public_keytype' in ssh_pub_key_facts
    assert 'ssh_host_key_ecdsa_public' not in ssh_pub_key_facts
    assert 'ssh_host_key_ecdsa_public_keytype' not in ssh_pub_key_facts

# Generated at 2022-06-13 03:41:57.222215
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    module_mock = type("module",(object,),{"params":{},"fail_json":None})()
    ssh_pub_key_fact_collector = SshPubKeyFactCollector()
    ssh_pub_key_facts = ssh_pub_key_fact_collector.collect(module=module_mock, collected_facts=None)
    assert isinstance(ssh_pub_key_facts, dict)
    assert 'ssh_host_pub_keys' in ssh_pub_key_facts
    assert 'ssh_host_key_rsa_public' in ssh_pub_key_facts
    assert 'ssh_host_key_rsa_public_keytype' in ssh_pub_key_facts

# Generated at 2022-06-13 03:42:01.446344
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    ssh_pub_key_facts = SshPubKeyFactCollector.collect(None, None)
    assert ssh_pub_key_facts['ssh_host_key_rsa_public']
    assert ssh_pub_key_facts['ssh_host_key_rsa_public_keytype']

# Generated at 2022-06-13 03:42:10.864653
# Unit test for method collect of class SshPubKeyFactCollector

# Generated at 2022-06-13 03:42:20.429892
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    mock_module = { }
    mock_collected_facts = { }
    fact_collector = SshPubKeyFactCollector()

    # Check no ssh host keys are found without any keys present
    SSH_HOST_KEYS = {}
    result = fact_collector.collect(mock_module, mock_collected_facts)
    assert result == {}

    # Check all algos of ssh host keys are found when all keys are present

# Generated at 2022-06-13 03:42:27.117744
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    keydirs = ['/etc/ssh', '/etc/openssh', '/etc']
    keydir = keydirs[1]
    algos = ['rsa', 'ecdsa', 'ed25519']
    algo = algos[1]
    factname = 'ssh_host_key_%s_public' % algo
    key_filename = '%s/ssh_host_%s_key.pub' % (keydir, algo)


# Generated at 2022-06-13 03:42:38.047979
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    """
    check that the method collect returns the expected structure,
    """
    import os
    import pytest
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collectors.ssh_pub_key import SshPubKeyFactCollector

    # files must be in lower case as this is the format we will use to
    # parse them
    keynames = ['dsa', 'rsa', 'ecdsa', 'ed25519']
    ssh_data = {}
    ssh_data['openssh'] = {}
    ssh_data['openssh']['firstkey'] = {}
    ssh_data['openbsd'] = {}
    ssh_data['openbsd']['firstkey'] = {}