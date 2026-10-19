

# Generated at 2022-06-13 03:33:16.295819
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    ufc = UserFactCollector()
    assert ufc != None

    test_facts = ufc.collect()

    assert len(test_facts) > 0

# Generated at 2022-06-13 03:33:27.612653
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # Testing for getuser
    user_facts_1 = UserFactCollector().collect(None, None)
    assert user_facts_1['user_id'] == getpass.getuser()

    # Testing for getuid
    user_facts_2 = UserFactCollector().collect(None, None)
    assert user_facts_2['user_uid'] == pwd.getpwuid(os.getuid()).pw_uid

    # Testing for getgid
    user_facts_3 = UserFactCollector().collect(None, None)
    assert user_facts_3['user_gid'] == pwd.getpwuid(os.getuid()).pw_gid

    # Testing for pw_gecos
    user_facts_4 = UserFactCollector().collect(None, None)
    assert user_facts

# Generated at 2022-06-13 03:33:28.189479
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    pass

# Generated at 2022-06-13 03:33:31.173743
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    fact_collector = UserFactCollector()
    fact_collector.collect()
    assert fact_collector.collect()['user_id'] == getpass.getuser()

# Generated at 2022-06-13 03:33:40.231068
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():

    from ansible.module_utils.facts import collector

    collector.collectors['user'] = UserFactCollector()


# Generated at 2022-06-13 03:33:49.000250
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_facts = UserFactCollector().collect()

    user_id = user_facts['user_id']
    user_uid = user_facts['user_uid']
    user_gid = user_facts['user_gid']
    user_dir = user_facts['user_dir']
    user_shell = user_facts['user_shell']

    assert isinstance(user_id, str)
    assert ' ' not in user_id

    assert isinstance(user_uid, int)
    assert isinstance(user_gid, int)
    assert isinstance(user_dir, str)
    assert ' ' not in user_dir

    assert isinstance(user_shell, str)
    assert ' ' not in user_shell

# Generated at 2022-06-13 03:33:50.423595
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    fact_collector = UserFactCollector()
    fact_collector.collect()

# Generated at 2022-06-13 03:33:59.869981
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # Case 1: getpass is mocked and returns dummy values
    # pr-ansible/ansible#57436
    import mock
    import tempfile
    module = mock.Mock(spec=dict)
    collected_facts = mock.Mock(spec=dict)
    mock_getpass = mock.Mock(return_value="dummy", specs=["getuser"])
    mock_pwd = mock.Mock(spec=dict)
    mock_pwd.getpwnam.return_value = pwd.struct_passwd(("name","passwd","uid","gid","gecos","dir","shell"))
    mock_pwd.getpwuid.return_value = pwd.struct_passwd(("name","passwd","uid","gid","gecos","dir","shell"))

# Generated at 2022-06-13 03:34:09.398270
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    """Unit test for method UserFactCollector.collect."""
    
    # Create a UserFactCollector object as it would be created by FactsCollector
    fact_collector = UserFactCollector()

    # Run method collect of UserFactCollector
    user_facts = fact_collector.collect()

    # Assert that user_id contains a (login-)name
    assert isinstance(user_facts['user_id'], str)
    assert len(user_facts['user_id']) > 0

    # Assert that user_uid contains a number
    assert isinstance(user_facts['user_uid'], int)

    # Assert that user_gid contains a number
    assert isinstance(user_facts['user_gid'], int)

    # Assert that user_gecos contains a string

# Generated at 2022-06-13 03:34:12.159702
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    fact_collector = UserFactCollector()
    fact_collector.collect()
    assert fact_collector._collected_facts['user_id'] == getpass.getuser()

# Generated at 2022-06-13 03:34:22.512832
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():

    m_facts = UserFactCollector()

    assert m_facts.collect(
    ) == {'effective_group_id': 1000,
          'effective_user_id': 1000,
          'real_group_id': 1000,
          'real_user_id': 1000,
          'user_dir': '/home/test',
          'user_gid': 1000,
          'user_gecos': 'test',
          'user_id': 'test',
          'user_shell': '/bin/bash',
          'user_uid': 1000}


# Generated at 2022-06-13 03:34:29.562013
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    u = UserFactCollector()
    testinfo = dict()
    testinfo['user_id'] = 'this.is.username'
    testinfo['user_uid'] = 0
    testinfo['user_gid'] = 0
    testinfo['user_gecos'] = 'user_gecos'
    testinfo['user_dir'] = 'user_dir'
    testinfo['user_shell'] = 'user_shell'
    testinfo['real_user_id'] = 0
    testinfo['effective_user_id'] = 0
    testinfo['real_group_id'] = 0
    testinfo['effective_group_id'] = 0

# Generated at 2022-06-13 03:34:33.024991
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    '''
    Unit test for method UserFactCollector.collect
    '''
    userFactCollector = UserFactCollector()
    userFactCollector.collect()

# Generated at 2022-06-13 03:34:41.487905
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    """Test collect method of UserFactCollector.
    """
    user_collector = UserFactCollector()
    collected_facts = user_collector.collect()
    assert len(collected_facts) == len(user_collector._fact_ids)
    assert 'user_id' in collected_facts
    assert 'user_uid' in collected_facts
    assert 'user_gid' in collected_facts
    assert 'user_gecos' in collected_facts
    assert 'user_dir' in collected_facts
    assert 'user_shell' in collected_facts
    assert 'real_user_id' in collected_facts
    assert 'effective_user_id' in collected_facts

# Generated at 2022-06-13 03:34:47.390604
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    fact_collector = UserFactCollector()
    ansible_facts = {}

    fact_collector.collect(collected_facts=ansible_facts)
    assert 'user_id' in ansible_facts
    assert 'user_uid' in ansible_facts
    assert 'user_gid' in ansible_facts
    assert 'user_gecos' in ansible_facts
    assert 'user_dir' in ansible_facts
    assert 'user_shell' in ansible_facts
    assert 'real_user_id' in ansible_facts
    assert 'effective_user_id' in ansible_facts
    assert 'effective_group_id' in ansible_facts

# Generated at 2022-06-13 03:34:57.294071
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # Create a mock module
    module = MockModule()
    # Create an instance of UserFactCollector
    fact_collector = UserFactCollector()
    collected_facts = fact_collector.collect(module=module)

# Generated at 2022-06-13 03:35:02.183009
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_facts = UserFactCollector()
    collected_facts = {}
    user_facts_dict = user_facts.collect(collected_facts)
    assert user_facts_dict['user_id'] == getpass.getuser()

# Generated at 2022-06-13 03:35:13.002332
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    import sys

    # Create a UserFactCollector object
    user_fc = UserFactCollector()

    # Check the name attribute of the object
    assert user_fc.name == 'user'

    # Check the _fact_ids attribute of the object
    assert 'user_id' in user_fc._fact_ids
    assert 'user_uid' in user_fc._fact_ids
    assert 'user_gid' in user_fc._fact_ids
    assert 'user_gecos' in user_fc._fact_ids
    assert 'user_dir' in user_fc._fact_ids
    assert 'user_shell' in user_fc._fact_ids
    assert 'real_user_id' in user_fc._fact_ids
    assert 'effective_user_id' in user_fc._fact_ids

# Generated at 2022-06-13 03:35:21.887753
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_fc = UserFactCollector()
    result = user_fc.collect()
    result.has_key('user_id')
    result.has_key('user_uid')
    result.has_key('user_gid')
    result.has_key('user_gecos')
    result.has_key('user_dir')
    result.has_key('user_shell')
    result.has_key('real_user_id')
    result.has_key('effective_user_id')
    result.has_key('real_group_id')
    result.has_key('effective_group_id')

# Generated at 2022-06-13 03:35:26.810726
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_fact = UserFactCollector()
    user_fact.collect()
    print(user_fact.collect())
    #print(user_fact.collect().keys())
    #print(user_fact.collect().values())
    assert user_fact.collect() != {}

if __name__ == '__main__':
    test_UserFactCollector_collect()

# Generated at 2022-06-13 03:35:31.692020
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    fact_collector = UserFactCollector()
    collected_facts = fact_collector.collect()
    assert collected_facts['user_id'] == getpass.getuser()

# Generated at 2022-06-13 03:35:38.937444
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    ufc = UserFactCollector()
    user_facts = ufc.collect()

    assert user_facts['user_id'] == getpass.getuser()
    assert user_facts['user_uid'] == os.getuid()
    assert user_facts['user_shell'] == os.getenv('SHELL')
    assert user_facts['user_dir'] == os.path.expanduser('~')


# Generated at 2022-06-13 03:35:39.539254
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    pass

# Generated at 2022-06-13 03:35:41.011156
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    result = collect()
    assert result
    assert result['user_id']

# Generated at 2022-06-13 03:35:44.474402
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_facts = UserFactCollector().collect()

    assert (user_facts['real_user_id'] == os.getuid())
    assert (user_facts['user_id'] == getpass.getuser())

# Generated at 2022-06-13 03:35:50.413459
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():

    from ansible.module_utils.facts.collector import UserFactCollector
    import getpass

    if getpass.getuser() != 'travis':
        test_user_fact_collector = UserFactCollector()
        test_user_collect_result = test_user_fact_collector.collect()

        test_user_collect_result['user_id'].should.equal(getpass.getuser())

# Generated at 2022-06-13 03:36:00.728498
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():

    # prepare system facts
    system_facts = {'test_fact_1': 'test_value_1', 'test_fact_2': 'test_value_2'}
    # prepare distro facts
    distro_facts = {'test_fact_3': 'test_value_3', 'test_fact_4': 'test_value_4'}
    # prepare collected facts
    collected_facts = {'system': system_facts, 'distribution': distro_facts}
    # prepare mock of getuser() method
    def mock_getuser():
        return 'test_user_id'

    # prepare mock of getpwnam/getpwuid() method

# Generated at 2022-06-13 03:36:05.303637
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    collector = UserFactCollector()
    user_facts = collector.collect(module=None, collected_facts=None)
    assert user_facts['user_id'] == getpass.getuser()
    assert 'real_group_id' in user_facts
    assert 'effective_group_id' in user_facts

# Generated at 2022-06-13 03:36:10.239235
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    import sys
    if sys.version_info[:2] < (2, 7):
        import unittest2 as unittest
    else:
        import unittest

    class TestUserFactCollector(unittest.TestCase):
        def test_collect(self):
            pass

    unittest.main()

# Generated at 2022-06-13 03:36:12.710016
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    ufc = UserFactCollector()
    results = ufc.collect()
    assert results['user_id'] == getpass.getuser()



# Generated at 2022-06-13 03:36:21.828412
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():

    user_fact_collector = UserFactCollector()
    user_fact_collector.collect()
    assert(user_fact_collector.collect() is not None)

# Generated at 2022-06-13 03:36:32.673732
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    import sys
    import user_utils
    user_utils.HAS_PWD = True

    import pwd
    class MockPwd(object):
        class struct_passwd:
            pw_uid = 0
            pw_gid = 0
            pw_gecos = 0
            pw_dir = 0
            pw_shell = 0
        def getpwnam(self, name):
            return self.struct_passwd()
        def getpwuid(self, uid):
            return self.struct_passwd()
    pwd = MockPwd()

    module = type('', (), {})()
    sys.modules['ansible.module_utils.facts.user_utils'] = user_utils
    sys.modules['pwd'] = pwd


# Generated at 2022-06-13 03:36:39.089528
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_fact_collector = UserFactCollector()
    user_facts = user_fact_collector.collect()

    assert user_facts['user_id'] == getpass.getuser()
    assert user_facts['user_uid'] == os.getuid()
    assert user_facts['user_gid'] == os.getgid()
    assert user_facts['real_user_id'] == os.getuid()
    assert user_facts['effective_user_id'] == os.geteuid()
    assert user_facts['real_group_id'] == os.getgid()
    assert user_facts['effective_group_id'] == os.getegid()

# Generated at 2022-06-13 03:36:47.181896
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():

    # Fake execution of method getuser
    def fake_getuser(self):
        return 'fake_user'

    # Fake execution of method getpwnam
    def fake_getpwnam(self, username):
        class FakePwdEntry:
            pass

        fake_entry = FakePwdEntry()
        fake_entry.pw_uid = 1
        fake_entry.pw_gid = 1
        fake_entry.pw_gecos = 'fake_gecos'
        fake_entry.pw_dir = '/home/fake_user'
        fake_entry.pw_shell = '/bin/bash'
        return fake_entry

    # Fake execution of method getuid
    def fake_getuid(self):
        return 1

    # Fake execution of method geteuid

# Generated at 2022-06-13 03:36:50.634479
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # Test if the fact collectore return a value for real_user_id
    collector = UserFactCollector()
    facts = collector.collect()
    assert facts.get('real_user_id') is not None


# Generated at 2022-06-13 03:37:00.445248
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_fact_collector = UserFactCollector()
    user_facts = user_fact_collector.collect()

    assert user_facts['user_id'] == getpass.getuser()
    assert user_facts['user_uid'] == pwd.getpwuid(os.getuid()).pw_uid
    assert user_facts['user_gid'] == pwd.getpwuid(os.getuid()).pw_gid
    assert user_facts['user_gecos'] == pwd.getpwuid(os.getuid()).pw_gecos
    assert user_facts['user_dir'] == pwd.getpwuid(os.getuid()).pw_dir
    assert user_facts['user_shell'] == pwd.getpwuid(os.getuid()).pw_

# Generated at 2022-06-13 03:37:11.276343
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    """Unit test for UserFactCollector.collect."""

    # Create instance
    ufc = UserFactCollector()

    # Execute method and test results
    results = ufc.collect()

    # Check that the results have all the expected keys
    expected_keys = ['user_id', 'user_uid', 'user_gid',
                     'user_gecos', 'user_dir', 'user_shell',
                     'real_user_id', 'effective_user_id',
                     'real_group_id', 'effective_group_id']
    for k in expected_keys:
        assert k in results, "key {} should be in results".format(k)

    # Check that the user_id is not blank
    user_id = results['user_id']

# Generated at 2022-06-13 03:37:20.025385
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    collector = UserFactCollector()
    result = collector.collect()
    assert result['user_id'] == 'ansible'
    assert result['user_uid'] == 500
    assert result['user_gid'] == 500
    assert result['user_gecos'] == 'User Name'
    assert result['user_dir'] == '/home/ansible'
    assert result['user_shell'] == '/bin/bash'
    assert result['real_user_id'] == 500
    assert result['effective_user_id'] == 500
    assert result['real_group_id'] == 500
    assert result['effective_group_id'] == 500

# Generated at 2022-06-13 03:37:31.897871
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    '''
    Unit test for the method collect of class UserFactCollector

    :return: True
    '''
    user_collector = UserFactCollector()
    user_facts = user_collector.collect()
    assert isinstance(user_facts, dict)
    assert 'user_id' in user_facts
    assert isinstance(user_facts['user_id'], str)
    assert user_facts['user_id'] == getpass.getuser()
    assert 'user_uid' in user_facts
    assert isinstance(user_facts['user_uid'], int)
    assert 'user_gid' in user_facts
    assert isinstance(user_facts['user_gid'], int)
    assert 'user_shell' in user_facts

# Generated at 2022-06-13 03:37:43.167805
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    userFacts = UserFactCollector()
    result = userFacts.collect()
    assert result['user_id'] == getpass.getuser()
    assert result['user_uid'] == pwd.getpwuid(os.getuid()).pw_uid
    assert result['user_gid'] == pwd.getpwuid(os.getuid()).pw_gid
    assert result['user_gecos'] == pwd.getpwuid(os.getuid()).pw_gecos
    assert result['user_dir'] == pwd.getpwuid(os.getuid()).pw_dir
    assert result['user_shell'] == pwd.getpwuid(os.getuid()).pw_shell
    assert result['real_user_id'] == os.getuid()
   

# Generated at 2022-06-13 03:38:02.208520
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    from ansible.module_utils.facts import facts

    fact = None
    collected_facts = None

    base = UserFactCollector()

    result = base.collect(fact, collected_facts)

    assert result['user_id']
    assert result['user_uid']
    assert result['user_gid']
    assert result['user_gecos']
    assert result['user_dir']
    assert result['user_shell']
    assert result['real_user_id']
    assert result['effective_user_id']
    assert result['real_group_id']
    assert result['effective_group_id']

# Generated at 2022-06-13 03:38:08.815365
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_fact_collector = UserFactCollector()
    user_id_fact = {'user_id': getpass.getuser()}
    user_uid_fact = {'user_uid': os.getuid()}
    user_gid_fact = {'user_gid': os.getgid()}
    user_gecos_fact = {'user_gecos': pwd.getpwuid(os.getuid()).pw_gecos}
    user_dir_fact = {'user_dir': pwd.getpwuid(os.getuid()).pw_dir}
    user_shell_fact = {'user_shell': pwd.getpwuid(os.getuid()).pw_shell}

# Generated at 2022-06-13 03:38:13.937943
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    ufc = UserFactCollector()
    collected_facts = ufc.collect()

    assert 'user_id' in collected_facts.keys()
    assert 'user_uid' in collected_facts.keys()
    assert 'user_gid' in collected_facts.keys()
    assert 'user_gecos' in collected_facts.keys()
    assert 'user_dir' in collected_facts.keys()
    assert 'user_shell' in collected_facts.keys()
    assert 'real_user_id' in collected_facts.keys()
    assert 'effective_user_id' in collected_facts.keys()
    assert 'real_group_id' in collected_facts.keys()
    assert 'effective_group_id' in collected_facts.keys()


# Generated at 2022-06-13 03:38:25.042334
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    collector = UserFactCollector()
    user_facts = collector.collect()
    assert user_facts['user_id'] == getpass.getuser()
    assert user_facts['user_uid'] == pwd.getpwuid(os.getuid()).pw_uid
    assert user_facts['user_gid'] == pwd.getpwuid(os.getuid()).pw_gid
    assert user_facts['user_gecos'] == pwd.getpwuid(os.getuid()).pw_gecos
    assert user_facts['user_dir'] == pwd.getpwuid(os.getuid()).pw_dir
    assert user_facts['user_shell'] == pwd.getpwuid(os.getuid()).pw_shell

# Generated at 2022-06-13 03:38:34.460385
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():

    collector = UserFactCollector()
    user_facts = collector.collect()

    assert user_facts.has_key('user_id')
    assert user_facts.has_key('user_uid')
    assert user_facts.has_key('user_gid')
    assert user_facts.has_key('user_gecos')
    assert user_facts.has_key('user_dir')
    assert user_facts.has_key('user_shell')
    assert user_facts.has_key('real_user_id')
    assert user_facts.has_key('effective_user_id')
    assert user_facts.has_key('real_group_id')
    assert user_facts.has_key('effective_group_id')

# Generated at 2022-06-13 03:38:37.817577
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    module = None
    collected_facts = None
    ufc = UserFactCollector()
    ufc.collect(module, collected_facts)



# Generated at 2022-06-13 03:38:48.442740
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # Assign
    module = None
    collected_facts = None
    user_fact_collector = UserFactCollector()

    # Act
    result = user_fact_collector.collect(module, collected_facts)

    # Assert
    assert isinstance(result, dict)
    assert 'user_id' in result
    assert isinstance(result['user_id'], str)
    assert 'user_uid' in result
    assert isinstance(result['user_uid'], int)
    assert 'user_gid' in result
    assert isinstance(result['user_gid'], int)
    assert 'user_gecos' in result
    assert isinstance(result['user_gecos'], str)
    assert 'user_dir' in result
    assert isinstance(result['user_dir'], str)
   

# Generated at 2022-06-13 03:38:58.736861
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_facts = UserFactCollector().collect(module=None, collected_facts=None)
    assert type(user_facts) is dict
    assert set(user_facts.keys()) == set(['user_id', 'user_uid', 'user_gid',
                     'user_gecos', 'user_dir', 'user_shell',
                     'real_user_id', 'effective_user_id',
                     'real_group_id', 'effective_group_id'])
    assert type(user_facts['user_id']) is str
    assert type(user_facts['user_uid']) is int
    assert type(user_facts['user_gid']) is int
    assert type(user_facts['user_gecos']) is str
    assert type(user_facts['user_dir']) is str

# Generated at 2022-06-13 03:39:01.678083
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    print("Running test_UserFactCollector_collect")

    ufc = UserFactCollector()
    results = ufc.collect()
    print("Got these results:")
    print(results)
    assert(type(results).__name__ == "dict")

# Generated at 2022-06-13 03:39:10.622169
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_fact_collector = UserFactCollector()

    user_facts = user_fact_collector.collect()
    assert 'user_id' in user_facts
    assert 'user_uid' in user_facts
    assert 'user_gid' in user_facts
    assert 'user_gecos' in user_facts
    assert 'user_dir' in user_facts
    assert 'user_shell' in user_facts
    assert 'real_user_id' in user_facts
    assert 'effective_user_id' in user_facts
    assert 'effective_group_id' in user_facts

# Generated at 2022-06-13 03:39:43.456908
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # Create a new instance of the UserFactCollector
    uc = UserFactCollector()

    # Create a new instance of the AnsibleModule
    am = AnsibleModuleMock()
    am.params = {}
    am.exit_json = exit_json
    am.fail_json = fail_json

    # Call the collect method and save the results to a fact_subset
    fact_subset = uc.collect(module=am, collected_facts=None)

    # Assert that fact_subset is not None
    assert fact_subset is not None

    # Assert that the expected facts are present in fact_subset
    assert 'user_id' in fact_subset
    assert 'user_uid' in fact_subset
    assert 'user_gid' in fact_subset

# Generated at 2022-06-13 03:39:54.229006
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_collector = UserFactCollector()
    collected_facts = {}
    user_facts = user_collector.collect(collected_facts=collected_facts)
    assert user_facts['user_id'] == getpass.getuser()
    assert user_facts.get('user_uid') is not None
    assert user_facts.get('user_gid') is not None
    assert user_facts.get('user_gecos') is not None
    assert user_facts.get('user_dir') is not None
    assert user_facts.get('user_shell') is not None
    assert user_facts.get('real_user_id') is not None
    assert user_facts.get('effective_user_id') is not None
    assert user_facts.get('real_group_id') is not None
    assert user

# Generated at 2022-06-13 03:40:02.217075
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    from ansible.module_utils import basic
    from ansible.module_utils.facts import collector

    collected_facts = dict()
    getpass_mock = mock.MagicMock(return_value='johndoe')
    getuid_mock = mock.MagicMock(return_value=123)
    geteuid_mock = mock.MagicMock(return_value=123)
    getgid_mock = mock.MagicMock(return_value=123)

# Generated at 2022-06-13 03:40:11.860560
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    import re
    import pwd
    from ansible.module_utils.facts.collector import BaseFactCollector

    # Create an object of class UserFactCollector
    user_fact_collector_obj = UserFactCollector()
    # Get the user facts
    user_facts = user_fact_collector_obj.collect()
    # Get the user id
    user_id = user_facts['user_id']
    # Get the user information using the pwd command
    user_pwd = pwd.getpwnam(user_id)
    # Sanity check
    assert(user_id == user_pwd[0])
    # Sanity check
    assert(user_facts['user_uid'] == user_pwd[2])
    # Sanity check

# Generated at 2022-06-13 03:40:19.855555
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # Given
    mocked_module = None
    mocked_collected_facts = None
    fact = UserFactCollector()

    # When
    result = fact.collect(mocked_module, mocked_collected_facts)

    # Then
    assert result['user_id']
    assert result['user_uid']
    assert result['user_gid']
    assert result['user_gecos']
    assert result['user_dir']
    assert result['user_shell']
    assert result['real_user_id']
    assert result['effective_user_id']
    assert result['real_group_id']
    assert result['effective_group_id']

# Generated at 2022-06-13 03:40:27.200921
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # Setup mock facts
    collected_facts = {}

    # Setup mock collector
    collector = UserFactCollector()

    # Call method collect of class UserFactCollector
    user_facts = collector.collect(collected_facts=collected_facts)

    # Assert user_id
    assert user_facts['user_id']

    # Assert user_uid
    assert user_facts['user_uid']

    # Assert user_gid
    assert user_facts['user_gid']

    # Assert user_gecos
    assert user_facts['user_gecos']

    # Assert user_dir
    assert user_facts['user_dir']

    # Assert user_shell
    assert user_facts['user_shell']

    # Assert real_user_id

# Generated at 2022-06-13 03:40:27.849898
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    pass

# Generated at 2022-06-13 03:40:35.883700
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    mock_module = None
    mock_collected_facts = {}

    ufc = UserFactCollector()
    got = ufc.collect(mock_module, mock_collected_facts)

    assert isinstance(got, dict)
    assert 'user_id' in got
    assert 'user_uid' in got
    assert 'user_gid' in got
    assert 'user_gecos' in got
    assert 'user_dir' in got
    assert 'user_shell' in got
    assert 'real_user_id' in got
    assert 'effective_user_id' in got
    assert 'real_group_id' in got
    assert 'effective_group_id' in got


# Generated at 2022-06-13 03:40:38.153137
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    u = UserFactCollector()
    u_facts = u.collect()
    print(u_facts)

# Generated at 2022-06-13 03:40:47.718565
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    '''ansible.module_utils.facts.system.user.UserFactCollector.collect'''
    # Collect facts using method collect of UserFactCollector
    collected_facts = UserFactCollector().collect()

    # Check collected facts
    assert type(collected_facts) is dict
    assert len(collected_facts) == 8

    assert 'user_id' in collected_facts
    assert type(collected_facts['user_id']) is str

    assert 'user_uid' in collected_facts
    assert type(collected_facts['user_uid']) is int

    assert 'user_gid' in collected_facts
    assert type(collected_facts['user_gid']) is int

    assert 'user_gecos' in collected_facts

# Generated at 2022-06-13 03:41:48.237464
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    result = UserFactCollector().collect()
    assert result['user_id'] is not None
    assert result['user_uid'] is not None
    assert result['user_gid'] is not None
    assert result['user_gecos'] is not None
    assert result['user_dir'] is not None
    assert result['user_shell'] is not None
    assert result['real_user_id'] is not None
    assert result['effective_user_id'] is not None
    assert result['real_group_id'] is not None
    assert result['effective_group_id'] is not None


# Generated at 2022-06-13 03:41:54.567371
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_facts = UserFactCollector().collect()
    assert 'user_id' in user_facts
    assert 'user_uid' in user_facts
    assert 'user_gid' in user_facts
    assert 'user_gecos' in user_facts
    assert 'user_dir' in user_facts
    assert 'user_shell' in user_facts
    assert 'real_user_id' in user_facts
    assert 'effective_user_id' in user_facts
    assert 'effective_group_ids' in user_facts

# Generated at 2022-06-13 03:41:55.887155
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    ufc = UserFactCollector()
    assert ufc.collect()['user_id'] == getpass.getuser()

# Generated at 2022-06-13 03:41:59.987055
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    test_UserFactCollector = UserFactCollector()
    result = test_UserFactCollector.collect()
    assert result
    assert type(result) is dict


# Generated at 2022-06-13 03:42:09.593792
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    collector = UserFactCollector()
    user_facts = collector.collect()

    assert 'ansible_user_id' in user_facts
    assert 'ansible_user_uid' in user_facts
    assert 'ansible_user_gid' in user_facts
    assert 'ansible_user_gecos' in user_facts
    assert 'ansible_user_dir' in user_facts
    assert 'ansible_user_shell' in user_facts
    assert 'ansible_real_user_id' in user_facts
    assert 'ansible_effective_user_id' in user_facts
    assert 'ansible_effective_group_ids' in user_facts

    assert 'user_id' not in user_facts
    assert 'user_uid' not in user_facts
    assert 'user_gid' not in user

# Generated at 2022-06-13 03:42:18.877736
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    '''
    This test will check if the function collect from
    UserFactCollector does return a user fact
    '''
    result = {}
    collected_facts = UserFactCollector()
    result = collected_facts.collect()
    assert result['user_id'] is not None
    assert result['user_uid'] is not None
    assert result['user_gid'] is not None
    assert result['user_gecos'] is not None
    assert result['user_dir'] is not None
    assert result['user_shell'] is not None
    assert result['real_user_id'] is not None
    assert result['effective_user_id'] is not None
    assert result['real_group_id'] is not None
    assert result['effective_group_id'] is not None

# Generated at 2022-06-13 03:42:26.002149
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    import platform
    import multiprocessing
    user_facts = UserFactCollector().collect()
    user_facts_keys = set(user_facts.keys())
    current_user = getpass.getuser()
    current_pwuid = pwd.getpwnam(current_user)

    assert user_facts_keys == UserFactCollector._fact_ids
    assert user_facts['user_id'] == current_user
    assert user_facts['user_uid'] == current_pwuid.pw_uid
    assert user_facts['user_gid'] == current_pwuid.pw_gid
    assert user_facts['user_gecos'] == current_pwuid.pw_gecos
    assert user_facts['user_dir'] == current_pwuid.pw_dir
    assert user

# Generated at 2022-06-13 03:42:33.649590
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    fact_collector = UserFactCollector()
    facts = {}
    fact_collector.collect(collected_facts=facts)
    assert 'user_id' in facts
    assert 'user_uid' in facts
    assert 'user_gid' in facts
    assert 'user_gecos' in facts
    assert 'user_dir' in facts
    assert 'user_shell' in facts
    assert 'real_user_id' in facts
    assert 'effective_user_id' in facts
    assert 'real_group_id' in facts
    assert 'effective_group_id' in facts

# Generated at 2022-06-13 03:42:42.395132
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_collector = UserFactCollector()
    collected_facts = {}
    user_collector.collect(collected_facts=collected_facts)
    assert collected_facts['user_id'] == getpass.getuser()
    assert collected_facts['user_uid'] == os.getuid()
    assert collected_facts['user_gid'] == os.getgid()
    assert collected_facts['user_gecos'] == pwd.getpwuid(os.getuid()).pw_gecos
    assert collected_facts['user_dir'] == pwd.getpwuid(os.getuid()).pw_dir
    assert collected_facts['user_shell'] == pwd.getpwuid(os.getuid()).pw_shell

# Generated at 2022-06-13 03:42:50.420250
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():

    # Initial state
    # Setup test objects
    test_obj = UserFactCollector()
    test_obj.collect()

    # Assertion that user_id is not empty
    assert test_obj.collect()['user_id'] != None
    # Assertion that user_uid is an integer
    assert type(test_obj.collect()['user_uid']) == int
    # Assertion that user_gid is an integer
    assert type(test_obj.collect()['user_gid']) == int
    # Assertion that user_gecos is not empty
    assert test_obj.collect()['user_gecos'] != None
    # Assertion that user_dir is not empty
    assert test_obj.collect()['user_dir'] != None
    # Assertion that user_shell is not empty
   