

# Generated at 2022-06-13 03:33:23.113225
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    module = AnsibleModuleMock()
    result = {}
    result['changed'] = False
    
    c = SshPubKeyFactCollector()
    c.collect(module=module, collected_facts=result)

    assert('ssh_host_pub_keys' in result)
    assert('ssh_host_key_rsa_public' in result)



# Generated at 2022-06-13 03:33:33.521482
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts import ansible_collections
    from ansible.module_utils.facts.collector import get_collector_instance

    fake_module = ansible_collections.__file__
    fake_module = fake_module[:fake_module.rfind("/")]
    keydir = fake_module + '/test/unit/module_utils/facts/files/sshkey'

    ssh_pub_key_facts = get_collector_instance(SshPubKeyFactCollector).collect(fake_module)


# Generated at 2022-06-13 03:33:39.796570
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    import pytest

    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.ssh_pub_keys import SshPubKeyFactCollector
    from ansible.module_utils._text import to_bytes

    from ansible.module_utils.facts.utils import get_file_content

    @pytest.fixture
    def keydata():
        return to_bytes(
            "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIMiUYfmZU6ecgm4/tzp4cLDOvDgyp0XpyX9i8WLMq0z test_ed25519\n"
        )


# Generated at 2022-06-13 03:33:44.949699
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    ssh_pub_key_facts = SshPubKeyFactCollector().collect()
    assert 'ssh_host_key_rsa_public' in ssh_pub_key_facts
    assert 'ssh-rsa' in ssh_pub_key_facts['ssh_host_key_rsa_public']
    assert 'ssh_host_key_rsa_public_keytype' in ssh_pub_key_facts

# Generated at 2022-06-13 03:33:53.852810
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    mod_args = {'module_name': 'test_module',
                'module_args': {},
                'module_complex_args': None,
                'module_class': None}
    mod_facts = {'ansible_module_args': '{"test": "args"}',
                 'ansible_module_name': 'test_module',
                 'ansible_version': 'version'}


# Generated at 2022-06-13 03:34:01.987342
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # create mock module and mock facts
    class MockModule:
        def __init__(self):
            self.params = {}

    class MockFacts:
        def __init__(self):
            self.ssh_host_pub_keys = None
            self.ssh_host_key_dsa_public = None
            self.ssh_host_key_rsa_public = None
            self.ssh_host_key_ecdsa_public = None
            self.ssh_host_key_ed25519_public = None

    class MockAlgo:
        def __init__(self):
            self.algo = None
            self.keytype = None


    # This is the correct keydata to be returned by get_file_content()
    # when certain keys are found

# Generated at 2022-06-13 03:34:13.066134
# Unit test for method collect of class SshPubKeyFactCollector

# Generated at 2022-06-13 03:34:20.467757
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # Create a new instance of SshPubKeyFactCollector
    provider = SshPubKeyFactCollector()
    # Check method collect - return one element
    assert(len(provider.collect()) == 1)
    # Check method collect.rsa_public - return expected string
    assert(provider.collect().get("ssh_host_key_rsa_public") == 'AAAAB3NzaC1yc2EAAAABIwAAAQEA.....')

# Generated at 2022-06-13 03:34:28.569013
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # Create an instance of a helper class used by the fact collection
    # mechanism of Ansible, whose sole purpose is to provide constants
    # and utility functions used by fact collection, such as a list of
    # directories to search for ssh public keys
    TestAnsibleModule = type('TestAnsibleModule', (object,), dict(
        ANSIBLE_MODULE_UTILS=dict(
            MODULE_UTILS_PATH = ['ansible/module_utils'],
        ),
    ))

    # Create an instance of the SshPubKeyFactCollector to be tested
    test_collector = SshPubKeyFactCollector(module=TestAnsibleModule)

    # Pretend the keys exist in the key directories specified in the
    # SshPubKeyFactCollector and also in a directory not listed there

# Generated at 2022-06-13 03:34:29.379302
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    pass


# Generated at 2022-06-13 03:34:41.408035
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # Create class instance
    oTestClass = SshPubKeyFactCollector()

    # Create mocks for modules to be used
    oMockModule = mock.MagicMock()
    oMockCollectedFacts = mock.MagicMock()

    # Call method collect and check returned result
    returned_result = oTestClass.collect(oMockModule, oMockCollectedFacts)

# Generated at 2022-06-13 03:34:47.902104
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    '''
    test_SshPubKeyFactCollector_collect method, it creates a SshPubKeyFactCollector
    class object and checks proper working of collect method.
    '''

    collector_obj = SshPubKeyFactCollector()
    collected_facts = {}
    test_collected_facts = {'ssh_host_key_ed25519_public': 'ssh-ed25519', 'ssh_host_key_ecdsa_public': 'ecdsa', 'ssh_host_key_rsa_public': 'ssh-rsa', 'ssh_host_key_dsa_public': 'ssh-dss'}
    collected_facts = collector_obj.collect(collected_facts=collected_facts)

    assert collected_facts == test_collected_facts

# Generated at 2022-06-13 03:34:57.607550
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    import os

    collector = SshPubKeyFactCollector()

    facts = {}
    tmpdir = '%s/ansible_test' % os.environ['CWD']

    os.mkdir(tmpdir)
    tmpfile = '%s/ssh_host_dsa_key' % tmpdir

# Generated at 2022-06-13 03:34:59.584346
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    SshPubKeyFactCollector.collect()

# Generated at 2022-06-13 03:35:11.311115
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # test for two sshd_config formats
    for line in ['HostKey /etc/ssh/ssh_host_rsa_key.pub',
                 'HostKey /etc/ssh/ssh_host_rsa_key']:
        ssh_host_sshd_config_content = '\n'.join(['#',
                                                  line,
                                                  '#HostKey /etc/ssh/ssh_host_dsa_key.pub',
                                                  '#HostKey /etc/ssh/ssh_host_ed25519_key.pub',
                                                  '#HostKey /etc/ssh/ssh_host_ecdsa_key.pub',
                                                  ''])


# Generated at 2022-06-13 03:35:22.573916
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    keys = SshPubKeyFactCollector(None, None).collect()
    assert keys.get('ssh_host_key_rsa_public') is not None
    assert keys.get('ssh_host_key_rsa_public_keytype') is not None
    assert keys.get('ssh_host_key_dsa_public') is not None
    assert keys.get('ssh_host_key_dsa_public_keytype') is not None
    assert keys.get('ssh_host_key_ecdsa_public') is not None
    assert keys.get('ssh_host_key_ecdsa_public_keytype') is not None
    assert keys.get('ssh_host_key_ed25519_public') is not None

# Generated at 2022-06-13 03:35:31.297001
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    """
    Test the ssh_pub_keys method of SshPubKeyFactCollector.
    """
    # Create a SshPubKeyFactCollector instance.
    ssh_pub_key_fact_collector = SshPubKeyFactCollector()

    # Mock the ssh_pub_keys method, so we do not actually
    # collect any facts and can test the collect method.
    def mock_ssh_pub_keys(module=None, collected_facts=None):
        return {}

    # Mock the get_file_content method.
    def mock_get_file_content(filename):
        keydata = None

# Generated at 2022-06-13 03:35:43.663169
# Unit test for method collect of class SshPubKeyFactCollector

# Generated at 2022-06-13 03:35:55.713128
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # test ssh_pub_key_facts for directory /etc
    input = {}

# Generated at 2022-06-13 03:35:56.285344
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    pass

# Generated at 2022-06-13 03:36:11.166885
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from ansible.module_utils.facts.collector import collector_mgr
    from ansible.module_utils.facts import collector
    collectorobj = SshPubKeyFactCollector
    collector_mgr.collectors[collectorobj.name] = collectorobj
    test_dict = collectorobj.collect(collected_facts=dict())
    assert isinstance(test_dict, dict)
    assert 'ssh_host_key_rsa_public' in test_dict
    assert test_dict['ssh_host_key_rsa_public']
    assert 'ssh_host_key_rsa_public_keytype' in test_dict
    assert test_dict['ssh_host_key_rsa_public_keytype']
    assert 'ssh_host_key_dsa_public' in test_dict

# Generated at 2022-06-13 03:36:11.738745
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    pass

# Generated at 2022-06-13 03:36:16.125262
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    collector = SshPubKeyFactCollector()
    facts = collector.collect()
    assert isinstance(facts, dict)
    assert 'ssh_host_key_dsa_public' in facts
    assert_equal(facts['ssh_host_key_dsa_public'], '1.2.3.4')

# Generated at 2022-06-13 03:36:27.055268
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # test for case when file exists
    testMod = SshPubKeyFactCollector

# Generated at 2022-06-13 03:36:36.801883
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    '''Create an instance, then call its collect() method to see if
    it returns a dictionary of ssh key information.
    '''

# Generated at 2022-06-13 03:36:45.974236
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    """
    Method collect returns keys and types of different algorithm
    """

    # create a mock class instead of using BaseFactCollector as parent
    class Mock(object):
        pass

    Mock.name = 'ssh_pub_keys'
    Mock._fact_ids = set(['ssh_host_pub_keys',
                          'ssh_host_key_dsa_public',
                          'ssh_host_key_rsa_public',
                          'ssh_host_key_ecdsa_public',
                          'ssh_host_key_ed25519_public'])

    ssh_pub_key_facts = {}
    algos = ('dsa', 'rsa', 'ecdsa', 'ed25519')

    # list of directories to check for ssh keys
    # used in the order listed here, the first one with keys is

# Generated at 2022-06-13 03:36:56.609729
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from ansible.module_utils import basic
    from ansible.module_utils.facts.utils import get_file_content
    # create mock module object
    module = basic.AnsibleModule(argument_spec=dict())
    module.params = {}

    # create mock facts and add them to module
    collected_facts = {}
    module.exit_json = lambda data: False
    module.fail_json = lambda *args, **kwargs: None

    # create mock SshPubKeyFactCollector and add it to collected facts
    ssh_pub_key_fact_collector = SshPubKeyFactCollector()
    collected_facts['ssh_pub_key_fact_collector'] = ssh_pub_key_fact_collector

    # execute test method collect of SshPubKeyFactCollector
    ssh_pub_key_fact_

# Generated at 2022-06-13 03:37:01.386882
# Unit test for method collect of class SshPubKeyFactCollector

# Generated at 2022-06-13 03:37:04.290147
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    ssh_pub_key_facts = SshPubKeyFactCollector()
    assert ssh_pub_key_facts.collect().has_key('ssh_host_key_dsa_public')

# Generated at 2022-06-13 03:37:05.854891
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    """
    Here we test the method collect of the class SshPubKeyFactCollector
    """
    # initialize object
    obj = SshPubKeyFactCollector()
    # create a fake module
    module = object()

    # test the code
    res = obj.collect(module)

# Generated at 2022-06-13 03:37:16.875327
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    fc = SshPubKeyFactCollector('ssh_pub_keys')
    module = 'module'
    collected_facts = 'collected_facts'
    assert fc.collect(module, collected_facts) == {}

# Generated at 2022-06-13 03:37:24.269765
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils.facts.collectors.network.ssh.ssh_pub_key import SshPubKeyFactCollector

    for fact_name in ['ssh_host_key_rsa_public',
                      'ssh_host_key_dsa_public',
                      'ssh_host_key_ecdsa_public',
                      'ssh_host_key_ed25519_public']:
        fact_collector = FactCollector(collectors=[SshPubKeyFactCollector()])
        host_facts = fact_collector.collect(module=None, collected_facts=None)

# Generated at 2022-06-13 03:37:27.651703
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    ssh_pub_key_facts = SshPubKeyFactCollector().collect()
    assert ssh_pub_key_facts['ssh_host_key_dsa_public_keytype'] == 'ssh-dss'
    assert ssh_pub_key_facts['ssh_host_key_rsa_public_keytype'] == 'ssh-rsa'
    assert ssh_pub_key_facts['ssh_host_key_ecdsa_public_keytype'] == 'ecdsa-sha2-nistp256'
    assert ssh_pub_key_facts['ssh_host_key_ed25519_public_keytype'] == 'ssh-ed25519'

# Generated at 2022-06-13 03:37:38.586547
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():

    # creating a mock object for the module
    module = type('module', (object,), {'params': {}, '_debug': True})

    # creating a mock object for the BaseFactCollector
    base_fact_collector = type('base_fact_collector', (object,), {'collect': lambda self, module=None, collected_facts=None: None})

    # creating a mock object for the SshPubKeyFactCollector class

# Generated at 2022-06-13 03:37:47.594312
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    keydirs = ['/etc/ssh', '/etc/openssh', '/etc']
    algos = ('dsa', 'rsa', 'ecdsa', 'ed25519')
    for keydir in keydirs:
        for algo in algos:
            key_filename = '%s/ssh_host_%s_key.pub' % (keydir, algo)

            collector = SshPubKeyFactCollector()
            ssh_pub_key_facts = collector.collect(key_filename)
            assert ssh_pub_key_facts['ssh_host_key_%s_public' % algo]

# Generated at 2022-06-13 03:37:48.815141
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    collector = SshPubKeyFactCollector()
    result = collector.collect()
    assert isinstance(result, dict)

# Generated at 2022-06-13 03:37:52.525979
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
  #initialize class module
  collector = SshPubKeyFactCollector()
  #invoke collect method
  result = collector.collect()
  print (result)

# Generated at 2022-06-13 03:38:02.324442
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    module = None
    collected_facts = None
    mock_keydir = '/etc/mockkeydir'
    mock_algo = 'mockalgo'
    mock_keyfile = 'ssh_host_mockalgo_key.pub'

# Generated at 2022-06-13 03:38:05.095707
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    class ModuleFake():
        def __init__(self, params=None):
            self.params = params

    module = ModuleFake({'gather_subset': ['all'], 'gather_timeout': 10})
    SshPubKeyFactCollector().collect(module)

# Generated at 2022-06-13 03:38:12.458038
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    assert SshPubKeyFactCollector.collect({}, {}) == {
        'ssh_host_pub_keys': '/etc/ssh/ssh_host_ed25519_key.pub',
        'ssh_host_key_dsa_public': None,
        'ssh_host_key_rsa_public': None,
        'ssh_host_key_ecdsa_public': None,
        'ssh_host_key_ed25519_public': 'AAAAC3NzaC1lZDI1NTE5AAAAIMwI1ZlkRiRp6UdKARfzX9jI+YeRp0pK51fYwYHsN/Tq'
    }

# Generated at 2022-06-13 03:38:35.083442
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # mock module object
    module = Mock()

    # mock collected_facts object
    collected_facts = dict()

    # Initialize fact collector
    fact_collector = SshPubKeyFactCollector(module=module,
                                            collected_facts=collected_facts)

    # Run method under test: collect
    res = fact_collector.collect()

    # Assert results
    assert isinstance(res, dict)
    assert len(res) > 0
    assert 'ssh_host_key_rsa_public' in res
    assert 'ssh_host_key_rsa_public_keytype' in res


# Generated at 2022-06-13 03:38:39.324980
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    collector = SshPubKeyFactCollector()

    collected_facts = collector.collect()
    assert collected_facts is not None
    for key in collected_facts.keys():
        print("%s: %s" % (key, collected_facts[key]))

# Generated at 2022-06-13 03:38:44.149700
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    ssh_pub_key_facts = SshPubKeyFactCollector().collect()

    # Check that all the keys that were registered were collected
    for fact_id in SshPubKeyFactCollector._fact_ids:
        assert fact_id in ssh_pub_key_facts

# Generated at 2022-06-13 03:38:49.335222
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    ssh_pub_key_facts = SshPubKeyFactCollector().collect()

    assert ssh_pub_key_facts
    assert 'ssh_host_key_rsa_public' in ssh_pub_key_facts



# Generated at 2022-06-13 03:38:59.348490
# Unit test for method collect of class SshPubKeyFactCollector

# Generated at 2022-06-13 03:39:04.724690
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():

    # create a mock module
    module = FakeAnsibleModule()

    # create a mock facts collection and load it with both desired and undesired
    # facts.  We can then test if the desired facts are returned and the
    # undesired ones are not.

# Generated at 2022-06-13 03:39:15.919851
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from ansible.module_utils.facts.utils import FactsCollector
    from ansible.module_utils.facts.collectors.system import SshPubKeyFactCollector
    from ansible.module_utils.facts import get_all_facts
    import os

    # change current working directory to one where we can create files and
    # directories without affecting the environment
    previous_cwd = os.getcwd()
    os.chdir('/tmp')

    # create a dummy directory to look for ssh keys
    key_dir = os.path.join('/tmp', 'ssh_pub_key_facts')
    os.makedirs(key_dir)

    # generate a key pair
    # return code is not checked here since we are mocking FactsCollector class
    # and mocking a class using a decorator does not seem to work properly
    #

# Generated at 2022-06-13 03:39:25.663856
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from ansible.module_utils.facts.collector import FactsCollector
    from ansible.module_utils.facts.system.ssh_pub_keys import SshPubKeyFactCollector


# Generated at 2022-06-13 03:39:28.371772
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    test_obj = SshPubKeyFactCollector()
    result = test_obj.collect()
    assert isinstance(result, dict), "result is of type %s" % type(result)

# Generated at 2022-06-13 03:39:38.897349
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # define collected_facts, using fixture data
    collected_facts = {
        'ansible_distribution': 'CentOS',
        'ansible_distribution_file_parsed': True,
        'ansible_distribution_file_path': '/etc/redhat-release',
        'ansible_distribution_file_variety': 'RedHat',
        'ansible_distribution_major_version': '6',
        'ansible_distribution_release': 'Final',
        'ansible_distribution_version': '6.9',
    }

    # Create an instance of SshPubKeyFactCollector
    inst = SshPubKeyFactCollector(module=None)

    # create a testfile (ssh_host_rsa_key.pub) and return its path
    # Use the basename of the module,

# Generated at 2022-06-13 03:40:18.558341
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from ansible.module_utils.facts.utils import get_file_content
    get_file_content_orig = get_file_content

# Generated at 2022-06-13 03:40:26.305150
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    cls = SshPubKeyFactCollector()

    # List of ssh public keys read from the system
    # ssh-rsa

# Generated at 2022-06-13 03:40:35.677421
# Unit test for method collect of class SshPubKeyFactCollector

# Generated at 2022-06-13 03:40:46.811321
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    import os as _os
    import tempfile as _tempfile
    import shutil as _shutil
    import textwrap as _textwrap
    import os.path as _path
    import sys as _sys
    import pytest as _pytest

    class ModuleStub(object):
        def __init__(self, params):
            self.params = params
            self.args = dict(params)

        def fail_json(self, *args, **kwargs):
            self.exit_args = args
            self.exit_kwargs = kwargs
            _sys.exit(1)

    def get_platform():
        return _os.uname()[0]

    class AnsibleFactsCollectorStub(object):
        def __init__(self, facts_dict):
            self.facts = facts_dict


# Generated at 2022-06-13 03:40:56.401126
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.utils import get_file_content

    # set keys for the test

# Generated at 2022-06-13 03:41:03.658692
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    k = SshPubKeyFactCollector()
    # test_collect function is in test_utils.py
    # test_utils.py is not a direct child of lib/ansible/module_utils/facts
    # and so is not imported automatically
    import sys, os
    parent_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # add ../lib/ansible/module_utils/facts to search path for unit testing
    sys.path.insert(0, os.path.join(parent_dir, "..", "lib", "ansible", "module_utils", "facts"))
    import test_utils
    test_utils.test_collect(k)

# Generated at 2022-06-13 03:41:14.095970
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():

    #import pdb; pdb.set_trace()

    m = MagicMock()

# Generated at 2022-06-13 03:41:21.136551
# Unit test for method collect of class SshPubKeyFactCollector

# Generated at 2022-06-13 03:41:32.144431
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    SshPubKeyFactCollector = SshPubKeyFactCollector()
    actual = SshPubKeyFactCollector.collect()

    # This is a fragile test, as it depends on the order of /etc/ssh/ssh_host_* keys

    expected_fact_keys = set(['ssh_host_key_dsa_public',
                              'ssh_host_key_dsa_public_keytype',
                              'ssh_host_key_rsa_public',
                              'ssh_host_key_rsa_public_keytype',
                              'ssh_host_key_ecdsa_public',
                              'ssh_host_key_ecdsa_public_keytype'])
    assert set(actual.keys()) == expected_fact_keys

# Generated at 2022-06-13 03:41:34.629982
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    """Test for method collect of class SshPubKeyFactCollector"""
    ssh_pub_key_facts = SshPubKeyFactCollector().collect()
    assert not ssh_pub_key_facts

# Generated at 2022-06-13 03:42:49.871008
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # create a test class for SshPubKeyFactCollector
    class TestSshPubKeyFactCollector(SshPubKeyFactCollector):
        def __init__(self):
            self.name = 'ssh_pub_keys'
            self._fact_ids = set(['ssh_host_pub_keys',
                                  'ssh_host_key_dsa_public',
                                  'ssh_host_key_rsa_public',
                                  'ssh_host_key_ecdsa_public',
                                  'ssh_host_key_ed25519_public'])

        # this method is required by BaseFactCollector
        def get_fact_id(self, key):
            return key

        # this method is a copy of the collect method in SshPubKeyFactCollector
        # with logging added

# Generated at 2022-06-13 03:42:56.047796
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    # Mock module used in the method collect of class SshPubKeyFactCollector
    # to return a predefined result
    class Module:
        def __init__(self):
            pass

        def get_bin_path(self, executable, required=False, opt_dirs=[]):
            return "/usr/bin/" + executable

    class Facts:
        def __init__(self):
            self.data = {}

        def add(self, fact, value):
            self.data[fact] = value

    module = Module()
    facts = Facts()

# Generated at 2022-06-13 03:43:03.222120
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():

    test_SshPubKeyFactCollector = SshPubKeyFactCollector()
    output = test_SshPubKeyFactCollector.collect()

    assert 'ssh_host_key_dsa_public' in output
    assert 'ssh_host_key_rsa_public' in output
    assert 'ssh_host_key_ecdsa_public' in output
    assert 'ssh_host_key_ed25519_public' in output

# Generated at 2022-06-13 03:43:11.269504
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

# Generated at 2022-06-13 03:43:22.256932
# Unit test for method collect of class SshPubKeyFactCollector
def test_SshPubKeyFactCollector_collect():
    """
    Unit test method collect of class SshPubKeyFactCollector.
    """
    from ansible_collections.ansible.community.tests.unit.module_utils.facts.test_ssh_pub_keys import (
        key_facts_file,
        key_facts_file_data,
        key_facts_expected_result
    )
    # set up mock environment
    import os
    os.environ = {'PATH': '/usr/local/bin:/usr/bin:/bin'}
    os.path = {'exists': lambda x: x == key_facts_file}
    open_name = "ansible_collections.ansible.community.plugins.module_utils.facts.ssh_pub_keys.open"