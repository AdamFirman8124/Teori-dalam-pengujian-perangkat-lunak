

# Generated at 2022-06-13 03:33:27.846578
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    ssh_pub_key_facts = SshPubKeyFactCollector().collect()
    assert 'ssh_host_key_dsa_public' in ssh_pub_key_facts
    assert 'ssh_host_key_rsa_public' in ssh_pub_key_facts
    assert 'ssh_host_key_ecdsa_public' in ssh_pub_key_facts
    assert 'ssh_host_key_ed25519_public' in ssh_pub_key_facts
    assert 'ssh_host_key_dsa_public_keytype' in ssh_pub_key_facts
    assert 'ssh_host_key_rsa_public_keytype' in ssh_pub_key_facts
    assert 'ssh_host_key_ecdsa_public_keytype' in ssh_pub_key_facts

# Generated at 2022-06-13 03:33:36.889364
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    import os
    from ansible.module_utils.facts.utils import FactsFilesCollectorFactory
    from ansible_collections.ansible.community.tests.unit.modules.utils import AnsibleFailJson, AnsibleExitJson, ModuleTestCase
    module = ModuleTestCase.fake_module

    if not os.path.exists('/etc/ssh/ssh_host_rsa_key.pub'):
        raise Exception('Cannot find test file')

    # set up a fake module used in AnsibleModule
    def fake_get_bin_path(module, executable, required=False):
        return executable
    module.get_bin_path = fake_get_bin_path

    fffc = FactsFilesCollectorFactory(module)
    ffc = fffc.create_collector('SshPubKeyFactCollector')


# Generated at 2022-06-13 03:33:46.738576
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    import os
    import tempfile
    import shutil
    from ansible.module_utils.facts.collector import Facts
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector import BaseFileCacheCollector
    from ansible.module_utils.facts.utils import get_file_content

    # mock Facts class since it is a singleton
    class MockFacts(Facts):
        def __init__(self):
            pass

        def get_facts(self):
            return {'foo': 'bar'}

    # mock the BaseFactCollector._collect_from_filesystem method
    # so we can test the collect method of our collector

# Generated at 2022-06-13 03:33:56.828302
# Unit test for method collect of class SshPubKeyFactCollector

# Generated at 2022-06-13 03:34:05.519595
# Unit test for method collect of class SshPubKeyFactCollector

# Generated at 2022-06-13 03:34:13.934593
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    ssh_pub_keys_fact_collector = SshPubKeyFactCollector()
    module = {}
    collected_facts = {}
    ssh_pub_keys = ssh_pub_keys_fact_collector.collect(module=module, collected_facts=collected_facts)
    assert 'ssh_host_key_rsa_public' in ssh_pub_keys
    assert 'ssh_host_key_rsa_public' in ssh_pub_keys
    assert 'ssh_host_key_ecdsa_public' in ssh_pub_keys
    assert 'ssh_host_key_ed25519_public' in ssh_pub_keys

# Generated at 2022-06-13 03:34:25.292568
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    import tempfile
    import os

    keydir = tempfile.mkdtemp()
    keyfiles = {}
    fake_facts = {}
    key_algos = ('dsa', 'rsa', 'ecdsa', 'ed25519')
    key_formats = ('base64', 'hex')

    # generate some test keys
    for key_algo in key_algos:
        for key_format in key_formats:
            cmd = 'ssh-keygen -q -b 1024 -t %s -f %s/test_ssh_host_%s_key ' \
                  '-N "" -E %s' % (key_algo, keydir, key_algo, key_format)
            os.system(cmd)

# Generated at 2022-06-13 03:34:35.564287
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():

    # Test when ssh key files do not exist
    def get_file_content_mock_none():
        return None

    collector = SshPubKeyFactCollector()
    collector.get_file_content = get_file_content_mock_none
    facts = collector.collect()
    assert facts is not None
    assert len(facts) == 0

    # Test when ssh key files exist

# Generated at 2022-06-13 03:34:44.889284
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    import os
    import tempfile
    from ansible.utils.path import unfrackpath
    from ansible.module_utils.facts import ModuleDataConsumer

    sshdir = tempfile.mkdtemp()

    for algo in ('dsa', 'rsa', 'ecdsa', 'ed25519'):
        keyfile_name = "ssh_host_%s_key.pub" % algo
        keyfile = os.path.join(sshdir, keyfile_name)

# Generated at 2022-06-13 03:34:48.685378
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # Create a new instance of SshPubKeyFactCollector class
    sshpubkey_fact = SshPubKeyFactCollector()
    try:
        # Check the method collect of the class SshPubKeyFactCollector
        # doesn't return None
        assert sshpubkey_fact.collect() is not None
    except:
        assert False

# Generated at 2022-06-13 03:34:59.817709
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collectors.ssh_pub_keys import SshPubKeyFactCollector


# Generated at 2022-06-13 03:35:11.436260
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from ansible.module_utils.facts import FactCollector

    def collect(self, module=None, collected_facts=None):
        fact_collector = SshPubKeyFactCollector(
            module=None,
            collected_facts=None)
        return fact_collector.collect()

    FactCollector.collect = collect
    fact_collector = FactCollector(
        module=None,
        collected_facts=None)
    fact_collector.collect()
    collected_facts = fact_collector.get_facts()
    assert collected_facts['ssh_host_key_dsa_public_keytype'] == 'ssh-dss'
    assert collected_facts['ssh_host_key_rsa_public_keytype'] == 'ssh-rsa'

# Generated at 2022-06-13 03:35:22.724852
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    ssh_pub_key_collector = SshPubKeyFactCollector()
    ssh_pub_key_facts = ssh_pub_key_collector.collect()

# Generated at 2022-06-13 03:35:31.365869
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    #mocking
    import os
    os.path = MagicMock()
    os.path.exists = MagicMock()

# Generated at 2022-06-13 03:35:41.496899
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    fact_collector = SshPubKeyFactCollector()
    facts_dict = fact_collector.collect()
    assert isinstance(facts_dict, dict)
    assert facts_dict.get('ssh_host_pub_keys') is not None
    assert facts_dict.get('ssh_host_key_dsa_public') is not None
    assert facts_dict.get('ssh_host_key_rsa_public') is not None
    assert facts_dict.get('ssh_host_key_ecdsa_public') is not None
    assert facts_dict.get('ssh_host_key_ed25519_public') is not None

# Generated at 2022-06-13 03:35:53.538998
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # This test creates an instance of SshPubKeyFactCollector,
    # calls method collect on that class,
    # and check the results
    keys_to_check=['ssh_host_dsa_key', 'ssh_host_rsa_key',
                   'ssh_host_ecdsa_key', 'ssh_host_ed25519_key']
    algos_to_check=['ssh_host_key_dsa_public', 'ssh_host_key_rsa_public',
                    'ssh_host_key_ecdsa_public', 'ssh_host_key_ed25519_public']
    keytype_to_check=['ssh-dss', 'ssh-rsa', 'ecdsa-sha2-nistp256', 'ssh-ed25519']
    ssh_pub_key_fact = S

# Generated at 2022-06-13 03:36:02.195129
# Unit test for method collect of class SshPubKeyFactCollector

# Generated at 2022-06-13 03:36:13.931546
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes

    # create a fake file system
    moduledir = '/tmp/ssh_test_module_dir'

# Generated at 2022-06-13 03:36:24.636132
# Unit test for method collect of class SshPubKeyFactCollector

# Generated at 2022-06-13 03:36:35.122976
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    ssh_pub_key_facts = {}
    algos = ('dsa', 'rsa', 'ecdsa', 'ed25519')
    keydirs = ['/etc/ssh', '/etc/openssh', '/etc']

    for keydir in keydirs:
        for algo in algos:
            factname = 'ssh_host_key_%s_public' % algo
            if factname in ssh_pub_key_facts:
                # a previous keydir was already successful, stop looking
                #for keys
                return ssh_pub_key_facts
            key_filename = '%s/ssh_host_%s_key.pub' % (keydir, algo)
            keydata = get_file_content(key_filename)
            if keydata != None:
                (keytype, key) = key

# Generated at 2022-06-13 03:36:47.097487
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from ansible.module_utils.facts.collectors.ssh_pub_keys import SshPubKeyFactCollector
    # initialize SshPubKeyFactCollector class
    SshPubKeyFactCollector = SshPubKeyFactCollector()
    # call method collect
    result = SshPubKeyFactCollector.collect()

# Generated at 2022-06-13 03:36:57.818949
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    ssh_pub_key_facts = {}
    # test_mock_fact_collection_dir can be used as collection dir
    # for SshPubKeyFactCollector. It contains files created from ssh keys:
    # ssh_host_ecdsa_key.pub, ssh_host_ed25519_key.pub, ssh_host_rsa_key.pub
    # and ssh_host_dsa_key.pub. The files contained in this directory are
    # used in test_SshPubKeyFactCollector_collect.
    test_mock_fact_collection_dir = 'test/unit/module_utils/facts/ssh_pub_keys'

    ssh_pub_key_fact_collector = SshPubKeyFactCollector()

# Generated at 2022-06-13 03:37:02.172955
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    c = SshPubKeyFactCollector()
    c.collect()
    assert c.name == 'ssh_pub_keys'
    assert c._fact_ids == set(['ssh_host_pub_keys',
                               'ssh_host_key_dsa_public',
                               'ssh_host_key_rsa_public',
                               'ssh_host_key_ecdsa_public',
                               'ssh_host_key_ed25519_public'])

# Generated at 2022-06-13 03:37:13.388873
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    mock_module = MagicMock()
    mock_collected_facts = {}

    # If there are present pub key files, should return a dict with
    # corresponding key and key type factors
    key_files = [('ssh_host_dsa_key.pub', 'ssh_host_key_dsa_public'),
                 ('ssh_host_rsa_key.pub', 'ssh_host_key_rsa_public'),
                 ('ssh_host_ecdsa_key.pub', 'ssh_host_key_ecdsa_public'),
                 ('ssh_host_ed25519_key.pub', 'ssh_host_key_ed25519_public')]
    expected_pub_key_facts = {}
    for (key_file, pub_key_fact) in key_files:
        key_filename = os.path.join

# Generated at 2022-06-13 03:37:22.628805
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    import os
    import stat
    import tempfile
    import textwrap

    # Create test key files
    tmpdir = tempfile.mkdtemp()
    os.mkdir(os.path.join(tmpdir, 'etc'))
    os.mkdir(os.path.join(tmpdir, 'etc', 'ssh'))
    os.mkdir(os.path.join(tmpdir, 'etc', 'openssh'))
    os.mkdir(os.path.join(tmpdir, 'etc', 'openssh', 'keys'))
    os.mkdir(os.path.join(tmpdir, 'etc', 'openssh', 'ssh2'))

# Generated at 2022-06-13 03:37:25.709408
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    test_obj = SshPubKeyFactCollector()
    assert test_obj.collect() == {}



# Generated at 2022-06-13 03:37:29.982590
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    module = {}
    facts = {}

    collector = SshPubKeyFactCollector()
    collected_facts = collector.collect(module, facts)

    assert isinstance(collected_facts, dict)
    assert isinstance(collected_facts[collector.name], dict)

# Generated at 2022-06-13 03:37:40.576764
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # Get the instance of the SshPubKeyFactCollector class
    sshPubKeyCollector = SshPubKeyFactCollector()

    # Create collected_facts
    collected_facts = {}

    # Invoke the collect method of SshPubKeyFactCollector
    collected_facts = sshPubKeyCollector.collect(
        module=None,
        collected_facts=collected_facts)

    # Assert the fact names are present
    assert sshPubKeyCollector.name in collected_facts

    ssh_pub_key_facts = collected_facts[sshPubKeyCollector.name]

    # Assert atleast one of the fact names is present
    assert (set(ssh_pub_key_facts.keys()) & sshPubKeyCollector._fact_ids)

# Generated at 2022-06-13 03:37:50.176240
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():

    class TestModule(object):
        def run_command(self, *args, **kwargs):
            return (0, '', '')

    class TestAnsibleModule(object):
        def __init__(self, *args, **kwargs):
            self.run_command = TestModule.run_command


# Generated at 2022-06-13 03:38:00.950187
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # pylint: disable=protected-access
    # create and instance of the fact collector
    fact = SshPubKeyFactCollector()

    collected_facts = {}

    file_content = 'ssh-rsa IAmFake= datasethatdoesnotmatter'
    collected_facts['ssh_pub_keys'] = file_content

    file_content = 'ssh-dss IAmFake= datasethatdoesnotmatter'
    collected_facts['ssh_host_key_dsa_public'] = file_content

    file_content = 'ssh-rsa IAmFake= datasethatdoesnotmatter'
    collected_facts['ssh_host_key_rsa_public'] = file_content

    file_content = 'ecdsa-sha2-nistp256 IAmFake= datasethatdoesnotmatter'

# Generated at 2022-06-13 03:38:14.013454
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from ansible.module_utils.facts import Facts
    from ansible.module_utils.facts.collectors.ssh.pub_key import SshPubKeyFactCollector
    from ansible.module_utils.facts.collectors.base import FactCollector

    # Mock Facts base class and its config member which
    # is utilized by SshPubKeyFactCollector
    config = {'gather_subset': '!all,!min', 'gather_timeout': 5}
    facts_base_mock = Facts(config)
    facts_base_mock.collector.collectors[FactCollector.name] = FactCollector()
    facts_base_mock.collector.collectors[SshPubKeyFactCollector.name] = SshPubKeyFactCollector()

    # Get ssh_pub_key facts for all the algorithms

# Generated at 2022-06-13 03:38:25.126597
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # IMPORTANT NOTE: The tests in this file are skipped by default because they
    # are dependent on system file/directories.
    # Test1: check collecting of keys
    # Test2: check collecting of keys when keydirs don't exist
    # Test3: check collecting of keys when keydirs don't exist and
    #        ssh_pub_key_facts contains some data
    test_collector = SshPubKeyFactCollector()
    ssh_pub_key_facts = test_collector.collect()
    assert 'ssh_host_key_rsa_public' in ssh_pub_key_facts
    assert 'ssh_host_key_rsa_public_keytype' in ssh_pub_key_facts
    assert 'ssh_host_key_dsa_public' in ssh_pub_key_facts

# Generated at 2022-06-13 03:38:30.708810
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():

    ssh_collector = SshPubKeyFactCollector()
    ssh_pub_key_facts = ssh_collector.collect()
    assert(ssh_pub_key_facts['ssh_host_key_dsa_public'].startswith('AAAAB3Nza'))
    assert(ssh_pub_key_facts['ssh_host_key_rsa_public'].startswith('AAAAB3Nza'))
    assert(ssh_pub_key_facts['ssh_host_key_ecdsa_public'].startswith('AAAAE2VjZ'))
    assert(ssh_pub_key_facts['ssh_host_key_ed25519_public'].startswith('AAAAE2VjZ'))


# Generated at 2022-06-13 03:38:36.685137
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    algos = ('dsa', 'rsa', 'ecdsa', 'ed25519')

    # When no keys exist, the collect method should return an empty dict
    collector = SshPubKeyFactCollector()
    facts = collector.collect()
    assert '' == ''

    # When some keys exist, the collect method should return dict
    # with entries for each of the keys
    for algo in algos:
        factname = 'ssh_host_key_%s_public' % algo
        assert factname in facts
        assert facts[factname] == '%s_key' % algo

# Generated at 2022-06-13 03:38:47.816865
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    ssh_pub_key_collector = SshPubKeyFactCollector()
    factdata = ssh_pub_key_collector.collect()

    # check that the collected facts have the keys we expect
    ssh_pub_key_fact_names = factdata.keys()
    assert 'ssh_host_pub_keys' in ssh_pub_key_fact_names
    assert 'ssh_host_key_rsa_public' in ssh_pub_key_fact_names
    assert 'ssh_host_key_ecdsa_public' in ssh_pub_key_fact_names
    assert 'ssh_host_key_ed25519_public' in ssh_pub_key_fact_names

    # check that the collected facts have data we expect
    rsa_pub_key = factdata['ssh_host_key_rsa_public']


# Generated at 2022-06-13 03:38:58.416681
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():

    ssh_pub_key_facts = SshPubKeyFactCollector().collect()
    assert 'ssh_host_key_rsa_public' in ssh_pub_key_facts
    assert 'ssh_host_key_rsa_public_keytype' in ssh_pub_key_facts
    assert 'ssh_host_key_dsa_public' in ssh_pub_key_facts
    assert 'ssh_host_key_dsa_public_keytype' in ssh_pub_key_facts
    assert 'ssh_host_key_ecdsa_public' in ssh_pub_key_facts
    assert 'ssh_host_key_ecdsa_public_keytype' in ssh_pub_key_facts
    assert 'ssh_host_key_ed25519_public' in ssh_pub_key_facts

# Generated at 2022-06-13 03:39:07.015702
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    '''Unit test for method collect of class SshPubKeyFactCollector'''

    # Create a class object of class SshPubKeyFactCollector
    ssh_pub_key = SshPubKeyFactCollector()

    # Create a test ansible module
    from ansible.module_utils.facts.collector import AnsibleModule
    test_module = AnsibleModule()

    # Create a test list of collected facts
    collected_facts = {}

    # Call method collect of SshPubKeyFactCollector
    result = ssh_pub_key.collect(test_module, collected_facts)

    # Check if result is not None
    assert result is not None

# Generated at 2022-06-13 03:39:17.958743
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from ansible.module_utils.facts import collector
    import textwrap

    for key in collector.fact_collector_classes[SshPubKeyFactCollector.name]._fact_ids:
        assert key in SshPubKeyFactCollector().collect().keys()


# Generated at 2022-06-13 03:39:26.862722
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from ansible.module_utils.facts import fact_collector

    # Create reference for test

# Generated at 2022-06-13 03:39:37.751713
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    import pytest
    from ansible.module_utils.facts.utils import get_file_content
    from ansible.module_utils.facts import collect
    module = pytest.Mock()

    get_file_content.default = None

# Generated at 2022-06-13 03:40:01.909394
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    """
    Unit test for method collect of class SshPubKeyFactCollector
    """
    from ansible.module_utils.facts import Facts
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.collector.ssh_pub_key import SshPubKeyFactCollector

    # prepare collector & collect some facts
    my_collector = Collector()
    my_collector.collect(module=None, collected_facts=Facts())

    # try to get the ssh_pub_key facts using the method
    collected_facts = my_collector.get_facts('ssh_pub_key')

    # check the expected result
    assert isinstance(collected_facts, dict)
    assert len(collected_facts) >= 1

# Generated at 2022-06-13 03:40:10.695993
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    c = Collector()
    c.collect_fact = lambda x, y=None: None # stub out collect_fact
    c.add_fact = lambda x, y, z=None: x.__setitem__(y, z)
    c.populate()
    assert c.facts['ssh_host_key_rsa_public'] is not None
    assert c.facts['ssh_host_key_rsa_public_keytype'] is not None
    assert c.facts.get('ssh_host_key_dsa_public') is None # most systems do not have dsa keys

# Generated at 2022-06-13 03:40:17.782297
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    ssh_pub_key_facts = SshPubKeyFactCollector()
    # Dummy facts
    collected_facts = {}
    fact_data = ssh_pub_key_facts.collect(collected_facts)
    assert 'ssh_host_key_dsa_public' in fact_data
    assert 'ssh_host_key_rsa_public' in fact_data
    assert 'ssh_host_key_ecdsa_public' in fact_data
    assert 'ssh_host_key_ed25519_public' in fact_data

# Generated at 2022-06-13 03:40:18.638119
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # TODO: Full implementation
    return

# Generated at 2022-06-13 03:40:26.368016
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    '''
    This method test the collect method of SshPubKeyFactCollector.
    '''

    ###################
    # Testing collect #
    ###################

    # Initialize a SshPubKeyFactCollector object
    ssh_pub_key_fact_collector = SshPubKeyFactCollector()

    # The collect method of SshPubKeyFactCollector
    # should return a dictionary containing the
    # key 'ssh_host_key_{algo}_public'.
    # Parameters:
    #    - module:  the module variable is an object of AnsibleModule class
    #    - collected_facts: a dictionary of collected facts
    # Return:
    #    - return_facts: a dictionary of facts to add to ansible_facts
    #                    in the calling module.
    return_facts = ssh_pub_key_

# Generated at 2022-06-13 03:40:35.710539
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from ansible.module_utils.facts import Facts
    from ansible.module_utils.facts.collector import FactsCollector

    file_mocker = {}

# Generated at 2022-06-13 03:40:46.811321
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    module = None
    collected_facts = None
    keydirs = ['/etc/ssh', '/etc/openssh', '/etc']
    algos = ('dsa', 'rsa', 'ecdsa', 'ed25519')
    ssh_pub_key_facts = []

    for keydir in keydirs:
        for algo in algos:
            key_filename = '%s/ssh_host_%s_key.pub' % (keydir, algo)
            keydata = get_file_content(key_filename)
            if keydata is not None:
                (keytype, key) = keydata.split()[0:2]
                ssh_pub_key_facts.append(key)
                ssh_pub_key_facts.append(keytype)


# Generated at 2022-06-13 03:40:53.299978
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    ssh_pub_key_facts = SshPubKeyFactCollector().collect()

    assert('ssh_host_key_dsa_public' in ssh_pub_key_facts)
    assert('ssh_host_key_rsa_public' in ssh_pub_key_facts)
    assert('ssh_host_key_ecdsa_public' in ssh_pub_key_facts)
    assert('ssh_host_key_ed25519_public' in ssh_pub_key_facts)

# Generated at 2022-06-13 03:41:00.836237
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from ansible.module_utils.facts.collector import FactsCollector

    test_collector = FactsCollector()
    test_collector.collectors = [SshPubKeyFactCollector()]

    # add the collector to this module's namespace
    globals()['SshPubKeyFactCollector'] = SshPubKeyFactCollector()

    # test one key exists but is empty
    # the method should not be called
    def mock_get_file_content(filename):
        expected_filename = '/etc/ssh/ssh_host_dsa_key.pub'
        assert filename == expected_filename
        return ''

    import __builtin__
    __builtin__.__import__ = lambda x: None

    import sys
    del sys.modules['ansible.module_utils.facts.utils']

    test_module = Mock

# Generated at 2022-06-13 03:41:03.853993
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    ssh_pub_key_facts = SshPubKeyFactCollector().collect()
    assert(ssh_pub_key_facts['ssh_host_key_rsa_public'].find(":") > 0)
    assert(ssh_pub_key_facts['ssh_host_key_ecdsa_public'].find(":") > 0)

# Generated at 2022-06-13 03:41:44.263969
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.facts.collectors.ssh_pub_keys import SshPubKeyFactCollector
    SshPubKeyFactCollector_instance = SshPubKeyFactCollector()
    collected_facts = SshPubKeyFactCollector_instance.collect()
    assert len(collected_facts) == 0

# Generated at 2022-06-13 03:41:53.703620
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # Test with ssh_host_ed25519_key.pub file that only contains a key
    key = 'AAAAC3NzaC1lZDI1NTE5AAAAIH1+yk0aJdG8HrRU6JwUg7elu6vH8Y4JSM5XxfqB3RLny'
    ssh_host_ed25519_key_pub_path = 'tests/unit/module_utils/facts/ssh_host_ed25519_key.pub'
    result = SshPubKeyFactCollector().collect(None, {}, ssh_host_ed25519_key_pub_path)
    assert result['ssh_host_key_ed25519_public'] == key
    assert result['ssh_host_key_ed25519_public_keytype'] == 'ssh-ed25519'

# Generated at 2022-06-13 03:42:04.313653
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():

    # Import required modules
    from ansible.module_utils import basic

    # Create a mocked out file for the test
    mocked_file = '{"/etc/ssh": {"ssh_host_rsa_key.pub": "ssh-rsa AAAAB1"}}'

    # Create and instantiate an instance of the SshPubKeyFactCollector
    fact_collector = SshPubKeyFactCollector()

    # Create a mocked out AnsibleModule
    module = basic.AnsibleModule(argument_spec={},
                                 supports_check_mode=True)

    # Mock the get_file_content function
    fact_collector.get_file_content = basic.AnsibleModule.get_file_contents

    # Set the mocked out file contents
    module.mock_file = mocked_file

    # Run the collect method


# Generated at 2022-06-13 03:42:13.687317
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # get this module to use for testing
    module = __import__('ansible.module_utils.facts.system.ssh_pub_key',
                        globals(), locals(), ['SshPubKeyFactCollector'], -1)
    ssh_pub_key_fact_collector = module.SshPubKeyFactCollector()

    # create a fake module object
    _module = type('AnsibleModule', (object,),
            {'params': {'gather_subset': ssh_pub_key_fact_collector.name},
             'get_bin_path': lambda x, y, opt_dirs=None: None})

    # unit test the method collect of this class
    assert ssh_pub_key_fact_collector.collect(_module) == {}

# Generated at 2022-06-13 03:42:22.078069
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    module = AnsibleModuleMock()
    collector = SshPubKeyFactCollector(module)

    # set up return values for mocked get_file_content
    # using ssh keys from testcases/units/module_utils/facts/collector/test_SshPubKeyFactCollector.ssh

# Generated at 2022-06-13 03:42:26.241081
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    import tempfile
    import shutil
    import os

    from ansible.module_utils.facts.collector import BaseFactCollector

    class BaseTest(object):
        def __init__(self):
            self.tempdir = None

        def setup(self):
            self.tempdir = tempfile.mkdtemp()
            os.mkdir(os.path.join(self.tempdir, 'ssh'))
            os.mkdir(os.path.join(self.tempdir, 'openssh'))
            os.mkdir(os.path.join(self.tempdir, 'ssh2'))
            os.mkdir(os.path.join(self.tempdir, 'ansible'))

        def teardown(self):
            shutil.rmtree(self.tempdir)


# Generated at 2022-06-13 03:42:37.049143
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True)

    mock_get_file_content = MagicMock(side_effect=["dsa AAA",
                                                   "asd",
                                                   "rsa  AAAA"])

    with patch("ansible.module_utils.facts.utils.get_file_content",
               mock_get_file_content):
        # Test dsa key
        ssh_pub_key_facts = SshPubKeyFactCollector.collect(module)
        expected = {
            'ssh_host_key_dsa_public': 'AAA',
            'ssh_host_key_dsa_public_keytype': 'dsa',
        }
        assert_true(ssh_pub_key_facts == expected)

        # Test rsa key


# Generated at 2022-06-13 03:42:39.872970
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    module = None
    collected_facts = None
    ssh_pub_key_facts = SshPubKeyFactCollector().collect(module, collected_facts)
    assert 'ssh_host_key_dsa_public' in ssh_pub_key_facts

# Generated at 2022-06-13 03:42:46.058338
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # create a class instance
    instance = SshPubKeyFactCollector()
    # call method collect and get the ssh pub key facts
    result = instance.collect()
    assert 'ssh_host_key_dsa_public' in result
    assert 'ssh_host_key_rsa_public' in result
    assert 'ssh_host_key_ecdsa_public' in result
    assert 'ssh_host_key_ed25519_public' in result

# Generated at 2022-06-13 03:42:50.453419
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    fact_collector = SshPubKeyFactCollector()
    collected_facts = {}
    ssh_pub_key_facts = fact_collector.collect(collected_facts=collected_facts)

    # check for the presence of a commonly found public ssh key type
    assert(ssh_pub_key_facts['ssh_host_key_rsa_public'].startswith('ssh-rsa'))