

# Generated at 2022-06-13 03:33:28.326049
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    fact_collector = UserFactCollector()
    fact_collector.collect()
    assert 'user' in fact_collector.collect(), 'user facts not found'
    assert 'user_id' in fact_collector.collect()['user'], 'user_id facts not found'
    assert 'user_uid' in fact_collector.collect()['user'], 'user_uid facts not found'
    assert 'user_gid' in fact_collector.collect()['user'], 'user_gid facts not found'
    assert 'user_gecos' in fact_collector.collect()['user'], 'user_gecos facts not found'
    assert 'user_dir' in fact_collector.collect()['user'], 'user_dir facts not found'
    assert 'user_shell' in fact_collector.collect

# Generated at 2022-06-13 03:33:30.541272
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_fact = UserFactCollector()
    assert type(user_fact.collect()) == dict


# Generated at 2022-06-13 03:33:38.257585
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
   fact_collector = UserFactCollector()
   fact_collector_result = fact_collector.collect()
   assert fact_collector_result.get("user_id") == "root"
   assert fact_collector_result.get("user_uid") == 0
   assert fact_collector_result.get("user_gid") == 0
   assert fact_collector_result.get("user_gecos") == "root"
   assert fact_collector_result.get("user_dir") == "/root"
   assert fact_collector_result.get("user_shell") == "/bin/bash"
   assert fact_collector_result.get("real_user_id") == 0
   assert fact_collector_result.get("effective_user_id") == 0

# Generated at 2022-06-13 03:33:47.902451
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    ufc = UserFactCollector()
    # Test actual user (assume test is being run by default user)
    user = ufc.collect()

    assert 'user_id' in user.keys()
    assert 'user_uid' in user.keys()
    assert 'user_gid' in user.keys()
    assert 'user_gecos' in user.keys()
    assert 'user_dir' in user.keys()
    assert 'user_shell' in user.keys()
    assert 'real_user_id' in user.keys()
    assert 'effective_user_id' in user.keys()
    assert 'real_group_id' in user.keys()
    assert 'effective_group_id' in user.keys()
    assert user['user_id'] == os.getenv('USER')

# Generated at 2022-06-13 03:33:58.008641
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # Create an object
    userfact = UserFactCollector()

    # Create a function to mock the getpwnam call
    def mock_getpwnam(username):
        return pwd.struct_passwd(('test_user',
                                  'test_passwd',
                                  1000,
                                  2000,
                                  'Test user',
                                  '/home/test_user',
                                  '/usr/bin/bash'))

    # Create a function to mock the getpwuid call
    def mock_getpwuid(uid):
        return pwd.struct_passwd(('test_user',
                                  'test_passwd',
                                  1000,
                                  2000,
                                  'Test user',
                                  '/home/test_user',
                                  '/usr/bin/bash'))

    # Mock the get

# Generated at 2022-06-13 03:34:03.281355
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    g_result = { 'real_group_id': 1000, 'user_gid': 1000, 'user_uid': 1000, 'user_id': 'test_user',
                 'effective_user_id': 1000, 'effective_group_id': 1000, 'user_gecos': '', 'user_dir': '/home/test_user',
                 'user_shell': '/bin/bash'}
    test_obj = UserFactCollector()
    assert g_result == test_obj.collect()

# Generated at 2022-06-13 03:34:13.744281
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # Create collector module
    module = type('module', (), {'params': {}})()
    # Create UserFactCollector instance
    user_facts = UserFactCollector(module)

    # Call collect method
    user_facts_output = user_facts.collect()

    # Assert that user_id matches getpass.getuser()
    assert user_facts_output['user_id'] == getpass.getuser()

    # Try to getpwnam user with getpass.getuser()
    try:
        pwent = pwd.getpwnam(getpass.getuser())
    # If unsuccessful, get user details using uid
    except KeyError:
        pwent = pwd.getpwuid(os.getuid())

    # Assert that uid, gid, gecos, dir, shell match output from p

# Generated at 2022-06-13 03:34:25.078943
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_collector = UserFactCollector()
    user_facts = user_collector.collect()
    # Tests that the user_id returns the current username
    assert user_facts['user_id'] == getpass.getuser()
    # Tests that the user_uid returns the current user id
    assert user_facts['user_uid'] == os.getuid()
    # Tests that the user_gid returns the current user id
    assert user_facts['user_gid'] == os.getgid()
    # Tests that user_gecos returns the information in the passwd file for
    # the current user
    assert user_facts['user_gecos'] == pwd.getpwuid(os.getuid()).pw_gecos
    # Tests that user_dir returns the current user home directory

# Generated at 2022-06-13 03:34:26.512863
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_fact_collector = UserFactCollector()
    user_fact_collector.collect()
    print(user_fact_collector.get_facts())


# Generated at 2022-06-13 03:34:30.190234
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    """Check that UserFactCollector.collect() returns expected result.

    """
    # Setup fixture
    import_facts = {}
    collected_facts = {'ansible_local': {'user_facts': {}}}

    # Test one
    # Expected result
    reference_user_facts = {'user_id': 'foo',
                            'user_uid': 1000,
                            'user_gid': 1000,
                            'user_gecos': 'foo,Bar,,',
                            'user_dir': '/home/foo',
                            'user_shell': '/bin/bash',
                            'real_user_id': 1000,
                            'effective_user_id': 1000,
                            'real_group_id': 1000,
                            'effective_group_id': 1000}

    # Run test and check result
   

# Generated at 2022-06-13 03:34:34.214979
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    pass

# Generated at 2022-06-13 03:34:43.876181
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    userFC = UserFactCollector()

    test_facts = userFC.collect()

    assert 'user_id' in test_facts
    assert len(test_facts['user_id']) > 0
    assert isinstance(test_facts['user_id'], str)

    assert 'user_uid' in test_facts
    assert isinstance(test_facts['user_uid'], int)

    assert 'user_gid' in test_facts
    assert isinstance(test_facts['user_gid'], int)

    assert 'user_gecos' in test_facts
    assert len(test_facts['user_gecos']) > 0
    assert isinstance(test_facts['user_gecos'], str)

    assert 'user_dir' in test_facts
    assert len(test_facts['user_dir'])

# Generated at 2022-06-13 03:34:44.492740
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    pass

# Generated at 2022-06-13 03:34:52.881428
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    ufc = UserFactCollector()

    pwent = pwd.getpwnam(getpass.getuser())

    facts = ufc.collect()

    assert facts['user_id'] == getpass.getuser()
    assert facts['user_uid'] == pwent.pw_uid
    assert facts['user_gid'] == pwent.pw_gid
    assert facts['user_gecos'] == pwent.pw_gecos
    assert facts['user_dir'] == pwent.pw_dir
    assert facts['user_shell'] == pwent.pw_shell
    assert facts['effective_user_id'] == os.geteuid()
    assert facts['effective_group_id'] == os.getgid()

# Generated at 2022-06-13 03:34:58.781888
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    from ansible.module_utils.facts.collector import FactsCollector
    import ansible.module_utils.facts.system.user

    FactsCollector._instance = None
    facts = FactsCollector()

    user = ansible.module_utils.facts.system.user.UserFactCollector()
    user_facts = {'user_id': getpass.getuser(), 'user_dir': os.path.expanduser('~')}
    assert user.collect() == user_facts



# Generated at 2022-06-13 03:35:10.884148
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    fact_collector = UserFactCollector()
    user_facts = fact_collector.collect()

    assert user_facts['user_id'] == getpass.getuser()

    pwent = pwd.getpwnam(getpass.getuser())
    assert user_facts['user_uid'] == pwent.pw_uid
    assert user_facts['user_gid'] == pwent.pw_gid
    assert user_facts['user_gecos'] == pwent.pw_gecos
    assert user_facts['user_dir'] == pwent.pw_dir
    assert user_facts['user_shell'] == pwent.pw_shell
    assert user_facts['real_user_id'] == os.getuid()
    assert user_facts['effective_user_id'] == os.geteuid()

# Generated at 2022-06-13 03:35:20.141889
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
    assert 'real_group_id' in user_facts
    assert 'effective_group_id' in user_facts


# Generated at 2022-06-13 03:35:21.750361
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    method = UserFactCollector()
    assert method.collect()

# Generated at 2022-06-13 03:35:26.707834
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    collector = UserFactCollector()
    result = collector.collect()
    assert(result['real_user_id'] == os.getuid())
    assert(result['effective_user_id'] == os.geteuid())
    assert(result['real_group_id'] == os.getgid())
    assert(result['effective_group_id'] == os.getegid())

# Generated at 2022-06-13 03:35:33.601559
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
    assert 'real_group_id' in user_facts
    assert 'effective_group_id' in user_facts

    assert user_facts['user_id'] == getpass.getuser()
    assert user_facts['user_uid'] == pwd.getpwuid(os.getuid()).pw_uid

# Generated at 2022-06-13 03:35:49.180881
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():

    # Call collected methods
    user_facts = UserFactCollector().collect()

    # assertions
    assert('user_id' in user_facts)
    assert(user_facts['user_id'] == getpass.getuser())

    try:
        pwent = pwd.getpwnam(getpass.getuser())
    except KeyError:
        pwent = pwd.getpwuid(os.getuid())

    assert('user_uid' in user_facts)
    assert(user_facts['user_uid'] == pwent.pw_uid)

    assert('user_gid' in user_facts)
    assert(user_facts['user_gid'] == pwent.pw_gid)

    assert('user_gecos' in user_facts)

# Generated at 2022-06-13 03:35:52.300270
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_fact_collector = UserFactCollector()
    user_fact_collector.collect()
    assert(text_type(user_fact_collector) == text_type(user_fact_collector.collect()))

# Generated at 2022-06-13 03:35:55.142112
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    ufc = UserFactCollector()
    assert ufc.collect()['user_id'] == getpass.getuser()

# Generated at 2022-06-13 03:35:57.100856
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    userfactcollector = UserFactCollector()
    result = userfactcollector.collect()
    print(result)


# Generated at 2022-06-13 03:36:02.735262
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
    assert 'real_group_id' in user_facts
    assert 'effective_group_id' in user_facts

# Generated at 2022-06-13 03:36:13.383854
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_fact_collector = UserFactCollector()
    user_facts = user_fact_collector.collect()
    assert isinstance(user_facts, dict)
    assert 'user_id' in user_facts
    assert 'user_uid' in user_facts
    assert 'user_gid' in user_facts
    assert 'user_gecos' in user_facts
    assert 'user_dir' in user_facts
    assert 'user_shell' in user_facts
    assert 'real_user_id' in user_facts
    assert 'effective_user_id' in user_facts
    assert 'real_group_id' in user_facts
    assert 'effective_group_id' in user_facts

# Generated at 2022-06-13 03:36:15.108983
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_fact_collector = UserFactCollector()
    user_fact_collector.collect()

# Generated at 2022-06-13 03:36:17.351527
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # Initialize the collector
    user_fact_collector = UserFactCollector()
    user_fact_collector.collect()



# Generated at 2022-06-13 03:36:28.467589
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():

    user_collector = UserFactCollector()
    collected_facts = user_collector.collect(module=None, collected_facts=None)

    assert collected_facts.get('user_id') is not None
    assert collected_facts.get('user_uid') is not None
    assert collected_facts.get('user_gid') is not None
    assert collected_facts.get('user_gecos') is not None
    assert collected_facts.get('user_dir') is not None
    assert collected_facts.get('user_shell') is not None
    assert collected_facts.get('real_user_id') is not None
    assert collected_facts.get('effective_user_id') is not None
    assert collected_facts.get('real_group_id') is not None

# Generated at 2022-06-13 03:36:30.000888
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    test_user = UserFactCollector()
    test_user.collect()

# Generated at 2022-06-13 03:36:42.949708
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # Create an instance of class UserFactCollector
    user_fct_collector = UserFactCollector()

    # Call method collect from class UserFactCollector
    user_facts = user_fct_collector.collect()

    # Test the result
    # Test if the number of key created is correct
    assert len(user_facts) == 9
    # Test that each key is in list of fact_ids
    for key in user_facts:
        assert key in user_fct_collector._fact_ids

# Generated at 2022-06-13 03:36:52.334375
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_facts = UserFactCollector().collect()
    assert user_facts['user_id'] is not None
    assert user_facts['user_uid'] > 0
    assert user_facts['user_gid'] > 0
    assert user_facts['user_gecos'] is not None
    assert user_facts['user_dir'] is not None
    assert user_facts['user_shell'] is not None
    assert user_facts['real_user_id'] > 0
    assert user_facts['effective_user_id'] > 0
    assert user_facts['real_group_id'] > 0
    assert user_facts['effective_group_id'] > 0

# Generated at 2022-06-13 03:36:59.306789
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    ufc = UserFactCollector()
    collected_facts = ufc.collect()
    assert collected_facts['user_id'] == getpass.getuser()
    assert isinstance(collected_facts['user_uid'], int)
    assert isinstance(collected_facts['user_gid'], int)
    assert isinstance(collected_facts['user_gecos'], str)
    assert isinstance(collected_facts['user_dir'], str)
    assert isinstance(collected_facts['user_shell'], str)
    assert isinstance(collected_facts['real_user_id'], int)
    assert isinstance(collected_facts['effective_user_id'], int)
    assert isinstance(collected_facts['real_group_id'], int)

# Generated at 2022-06-13 03:37:06.947562
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    test_case = {'user_id':'ansible', 'user_uid':1000, 'user_gid':1000,
                 'user_gecos':'Ansible', 'user_dir':'/home/ansible',
                 'user_shell':'/bin/bash', 'real_user_id':1000,
                 'effective_user_id':1000, 'real_group_id':1000,
                 'effective_group_id':1000}
    ufc = UserFactCollector()
    assert ufc.collect() == test_case

# Generated at 2022-06-13 03:37:12.925322
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    fact_collector = UserFactCollector()
    fact_collector.collect()

    test_id = getpass.getuser()
    test_uid = os.getuid()
    test_gid = os.getgid()

    assert test_id in fact_collector.get_facts()
    assert test_uid in fact_collector.get_facts()
    assert test_gid in fact_collector.get_facts()

# Generated at 2022-06-13 03:37:22.420506
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_facts = {}
    user_facts['user_id'] = getpass.getuser()
    try:
        pwent = pwd.getpwnam(getpass.getuser())
    except KeyError:
        pwent = pwd.getpwuid(os.getuid())
    user_facts['user_uid'] = pwent.pw_uid
    user_facts['user_gid'] = pwent.pw_gid
    user_facts['user_gecos'] = pwent.pw_gecos
    user_facts['user_dir'] = pwent.pw_dir
    user_facts['user_shell'] = pwent.pw_shell
    user_facts['real_user_id'] = os.getuid()
    user_facts['effective_user_id'] = os.geteu

# Generated at 2022-06-13 03:37:34.625369
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # create a UserFactCollector
    ufc = UserFactCollector()
    # call method collect of class UserFactCollector
    user_facts = ufc.collect()
    # check that user_facts is of type dict
    assert isinstance(user_facts, dict)
    # check that user_facts contains keys user_id, user_uid, user_gid, user_gecos,
    # user_dir, user_shell, real_user_id, effective_user_id, real_group_id and effective_group_id

# Generated at 2022-06-13 03:37:35.169272
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    pass

# Generated at 2022-06-13 03:37:44.598528
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user = UserFactCollector()
    user_facts = user.collect()

    assert 'user_id' in user_facts
    assert 'user_uid' in user_facts
    assert 'user_gid' in user_facts
    assert 'user_gecos' in user_facts
    assert 'user_dir' in user_facts
    assert 'user_shell' in user_facts
    assert 'real_user_id' in user_facts
    assert 'effective_user_id' in user_facts
    assert 'real_group_id' in user_facts
    assert 'effective_group_id' in user_facts

# Generated at 2022-06-13 03:37:51.807011
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    pwd.getpwnam = lambda x: {'pw_name': 'testuser', 'pw_uid': 1001, 'pw_gid': 1002,
                              'pw_gecos': 'User test', 'pw_dir': '/home/test/',
                              'pw_shell': '/bin/bash'}
    os.getuid = lambda: 1001
    os.geteuid = lambda: 1003
    os.getgid = lambda: 1004
    os.getegid = lambda: 1004
    getpass.getuser = lambda: 'testuser'

# Generated at 2022-06-13 03:38:13.365078
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    '''
    Test the collect method of the UserFactCollector.  This involves
    readding a python module and patching os.geteuid() and os.getuid()
    so that we can test that the UserFactCollector gets the user_id
    information correctly.
    '''
    import ansible.module_utils.facts.collectors.user
    from unittest import mock

    user_id = "test_user"
    uid = 1001
    gid = 1002
    gecos = "Test User"
    shell = "/bin/bash"
    homedir = "/home/test_user"


# Generated at 2022-06-13 03:38:23.558720
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    import pytest
    from ansible.module_utils.facts.collector import get_collector_instance
    user_fact_collector = get_collector_instance(UserFactCollector)
    user_fact = {'user_gecos': 'Git Fusion', 'effective_group_ids': [1000, 31, 6, 15], 'user_dir': '/home/git', 'real_user_id': 1000, 'effective_user_id': 1000,
     'real_group_id': 1000, 'user_gid': 1000, 'effective_group_id': 1000, 'user_id': 'git', 'user_uid': 1000, 'user_shell': '/bin/bash'}
    assert user_fact == user_fact_collector.collect()

# Generated at 2022-06-13 03:38:24.840929
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    mycollector = UserFactCollector()
    myuser_facts = mycollector.collect()
    assert 'user_id' in myuser_facts, \
        "expected 'user_id' in user_facts, but not found"

# Generated at 2022-06-13 03:38:29.380525
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    un = UserFactCollector()
    assert sorted(un.collect().keys()) == ['effective_group_id', 'effective_user_id', 'real_group_id', 'real_user_id', 'user_dir', 'user_gid', 'user_gecos', 'user_id', 'user_shell', 'user_uid']



# Generated at 2022-06-13 03:38:37.405367
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():

    def mock_getpwuid(uid):
        return (
            u'foo',
            '*',
            100,
            100,
            'Foo Bar, the first',
            '/Users/foo',
            '/bin/bash'
        )

    def mock_getgid():
        return 100

    def mock_getuid():
        return 100

    def mock_geteuid():
        return 100

    import __builtin__

    # Arrange
    mock_pwd = __import__('pwd')
    mock_pwd.getpwuid = mock_getpwuid

    mock_os = __import__('os')
    mock_os.getgid = mock_getgid
    mock_os.getuid = mock_getuid
    mock_os.geteuid = mock_geteuid



# Generated at 2022-06-13 03:38:40.315819
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_fact_collector = UserFactCollector()
    user_facts = user_fact_collector.collect()

    assert user_facts['user_id'] == getpass.getuser()

# Generated at 2022-06-13 03:38:49.343509
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    os_obj = UserFactCollector()
    user_facts = os_obj.collect()
    assert True == isinstance(user_facts, dict)
    assert True == isinstance(user_facts['user_id'], str)
    assert True == isinstance(user_facts['user_uid'], int)
    assert True == isinstance(user_facts['user_gid'], int)
    assert True == isinstance(user_facts['user_gecos'], str)
    assert True == isinstance(user_facts['user_dir'], str)
    assert True == isinstance(user_facts['user_shell'], str)
    assert True == isinstance(user_facts['real_user_id'], int)
    assert True == isinstance(user_facts['effective_user_id'], int)

# Generated at 2022-06-13 03:38:59.384542
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    passwd_mock = {
        'user_id': 'foo',
        'user_uid': 1000,
        'user_gid': 1000,
        'user_gecos': 'foo',
        'user_dir': '/home/foo',
        'user_shell': '/bin/bash',
        'real_user_id': 1000,
        'effective_user_id': 1000,
        'effective_group_ids': 1000,
    }

    class fake_pwd:
        def getpwnam(self, name):
            passwd_mock['user_id'] = name
            return passwd_mock

        def getpwuid(self, uid):
            passwd_mock['user_uid'] = uid
            return passwd_mock

    pwd.getpwnam = fake_p

# Generated at 2022-06-13 03:39:00.568526
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    ufc = UserFactCollector()
    ufc.collect()

# Generated at 2022-06-13 03:39:08.164239
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    from . import TestAnsibleModule

    result = dict(changed=False, ansible_facts=dict(user=dict()))
    module = TestAnsibleModule(argument_spec=dict(), supports_check_mode=True)

    user_fact_collector = UserFactCollector()

    user_facts = user_fact_collector.collect(module)
    result['ansible_facts']['user'] = user_facts
    module.exit_json(**result)


# Generated at 2022-06-13 03:39:38.265340
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user = UserFactCollector()
    assert 'user_shell' in user.collect()
    assert 'user_uid' in user.collect()

# Generated at 2022-06-13 03:39:45.307394
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    gid = os.getgid()
    uid = os.getuid()

    collector = UserFactCollector()
    r = collector.collect()
    assert r['real_group_id'] == gid
    assert r['real_user_id'] == uid
    assert r['effective_group_id'] == gid
    assert r['effective_user_id'] == uid
    assert r['user_id'] == getpass.getuser()
    assert r['user_uid'] == uid
    assert r['user_gid'] == gid
    assert r['user_gecos'] == pwd.getpwuid(uid).pw_gecos
    assert r['user_dir'] == pwd.getpwuid(uid).pw_dir
    assert r['user_shell'] == pwd.getp

# Generated at 2022-06-13 03:39:55.820916
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    ufc = UserFactCollector()
    facts = ufc.collect()
    assert facts['user_id'] is not None
    assert facts['user_uid'] == os.getuid()
    assert facts['user_gid'] == os.getgid()
    assert facts['user_dir'] == os.getenv('HOME')
    assert facts['user_shell'] == os.getenv('SHELL')
    assert facts['real_user_id'] == os.getuid()
    assert facts['effective_user_id'] == os.geteuid()
    assert facts['real_group_id'] == os.getgid()
    assert facts['effective_group_id'] == os.getegid()
    assert type(facts['effective_group_ids']) == list

# Generated at 2022-06-13 03:40:02.959587
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    module_mock = mock.MagicMock()
    collected_facts_mock = mock.MagicMock()
    collector = UserFactCollector()

    returned_facts = collector.collect(module_mock, collected_facts_mock)

    assert returned_facts['user_id'] == 'username'
    assert returned_facts['user_uid'] == 1234
    assert returned_facts['user_gid'] == 4321
    assert returned_facts['user_gecos'] == 'gecos'
    assert returned_facts['user_dir'] == '/home/username'
    assert returned_facts['user_shell'] == '/bin/bash'
    assert returned_facts['real_user_id'] == 1234
    assert returned_facts['effective_user_id'] == 1234

# Generated at 2022-06-13 03:40:12.019543
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_fact_collector = UserFactCollector()
    user_facts = user_fact_collector.collect()
    assert(user_facts['user_id'] == getpass.getuser())
    pwent = pwd.getpwnam(getpass.getuser())
    assert(user_facts['user_uid'] == pwent.pw_uid)
    assert(user_facts['user_gid'] == pwent.pw_gid)
    assert(user_facts['user_gecos'] == pwent.pw_gecos)
    assert(user_facts['user_dir'] == pwent.pw_dir)
    assert(user_facts['user_shell'] == pwent.pw_shell)
    assert(user_facts['real_user_id'] == os.getuid())

# Generated at 2022-06-13 03:40:18.067824
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    collector = UserFactCollector()
    result = collector.collect()
    assert result == {'user_id': 'test', 'user_uid': 1000, 'user_gid': 1000, 'user_gecos': 'test,,,', 'user_dir': '/home/test', 'user_shell': '/bin/bash', 'effective_user_id': 1000, 'effective_group_ids': [1000], 'real_user_id': 1000}

# Generated at 2022-06-13 03:40:25.911509
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    test_object = UserFactCollector()
    user_facts = test_object.collect()
    #assert(user_facts['user_id'] == 'mae')
    assert(user_facts['user_uid'] == os.getuid())
    assert(user_facts['user_gid'] == os.getgid())
    assert(user_facts['user_gecos'] != '')
    assert(user_facts['user_dir'] != '')
    assert(user_facts['user_shell'] != '')
    assert(user_facts['real_user_id'] == os.getuid())
    assert(user_facts['effective_user_id'] == os.geteuid())
    assert(user_facts['real_group_id'] == os.getgid())

# Generated at 2022-06-13 03:40:35.356711
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # empty dictionary
    facts = {}

    # initialize UserFactCollector
    user = UserFactCollector(module=None, collected_facts=facts)

    # test UserFactCollector.collect method

# Generated at 2022-06-13 03:40:40.722157
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    ufc = UserFactCollector()
    facts = ufc.collect()
    assert facts['user_id'] == getpass.getuser()
    assert facts['user_uid'] == pwd.getpwnam(getpass.getuser()).pw_uid


# Generated at 2022-06-13 03:40:48.291148
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    __import__('ansible.module_utils.facts.collector.user')
    import ansible.module_utils.facts.collector.user

    # Get the `UserFactCollector` class object.
    collector = ansible.module_utils.facts.collector.user.UserFactCollector

    # Get the ansible module object.
    ansible_module = AnsibleModule()

    # Call the collect method of the object and get the result.
    result = collector.collect(ansible_module)

    # Fetch important factors few of them as follows.
    username = result["user_id"]
    uid = result["user_uid"]
    gid = result["user_gid"]
    gecos = result["user_gecos"]
    dir = result["user_dir"]
    shell = result["user_shell"]

# Generated at 2022-06-13 03:41:54.994320
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    uf = UserFactCollector()
    uf_facts = uf.collect()
    assert len(uf_facts) == 9
    assert uf_facts['user_id'] == getpass.getuser()
    assert uf_facts['user_uid'] == pwd.getpwnam(getpass.getuser()).pw_uid
    assert uf_facts['user_gid'] == pwd.getpwnam(getpass.getuser()).pw_gid
    assert uf_facts['user_gecos'] == pwd.getpwnam(getpass.getuser()).pw_gecos
    assert uf_facts['user_dir'] == pwd.getpwnam(getpass.getuser()).pw_dir

# Generated at 2022-06-13 03:42:03.989641
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_collector_facts = UserFactCollector()
    user_facts = user_collector_facts.collect()
    # Check if user_id and user_uid are not None
    assert user_facts['user_id'] is not None
    assert user_facts['user_uid'] is not None
    # Check if real_user_id is not None
    assert user_facts['real_user_id'] is not None
    # Check if effective_user_id is not None
    assert user_facts['effective_user_id'] is not None
    # Check if effective_group_ids is not None
    assert user_facts['effective_group_ids'] is not None

# Generated at 2022-06-13 03:42:14.012876
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    c = UserFactCollector()
    d = c.collect()

    assert len(d) > 0

    assert 'user_id' in d
    assert 'user_uid' in d
    assert 'user_gid' in d
    assert 'user_gecos' in d
    assert 'user_dir' in d
    assert 'user_shell' in d
    assert 'real_user_id' in d
    assert 'effective_user_id' in d
    assert 'real_group_id' in d
    assert 'effective_group_id' in d

    assert len(d['user_id']) > 0

    assert d['user_uid'] >= 0
    assert d['user_gid'] >= 0
    assert d['user_gecos'] is not None
    assert d['user_dir'] is not None
   

# Generated at 2022-06-13 03:42:19.113944
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    fact = UserFactCollector()
    result = fact.collect()
    assert result['user_id'] == getpass.getuser()
    assert result['real_user_id'] == os.getuid()
    assert result['effective_user_id'] == os.geteuid()
    assert result['real_group_id'] == os.getgid()
    assert result['effective_group_id'] == os.getgid()

# Generated at 2022-06-13 03:42:25.270264
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():

    # Simple test for method collect of class UserFactCollector
    insight_facts = {'user_id': 'ansible01', 'user_uid': 1000,
                     'user_gid': 1000, 'user_gecos': 'Ansible User',
                     'user_dir': '/home/ansible01',
                     'user_shell': '/bin/bash',
                     'real_user_id': 1000, 'effective_user_id': 1000,
                     'real_group_id': 1000, 'effective_group_id': 1000}

    user_fact_collector = UserFactCollector()
    user_facts = user_fact_collector.collect()

    assert user_facts == insight_facts

# Generated at 2022-06-13 03:42:35.810550
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():

    import sys
    from ansible.module_utils.facts.collector import (
        UserFactCollector, BaseFactCollector)

    class MockPwd:

        class Pwent:
            pw_uid = 10000
            pw_gid = 10000
            pw_gecos = "gecos"
            pw_dir = "/home/ansible"
            pw_shell = "/usr/bin/bash"

        user_id = "ansible"
        pwent = Pwent()

        @staticmethod
        def getpwnam(user):
            return MockPwd.pwent

        @staticmethod
        def getpwuid(uid):
            return MockPwd.pwent

    class MockOS:
        @staticmethod
        def getuid():
            return MockOS.uid


# Generated at 2022-06-13 03:42:43.763546
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    uid = os.getuid()
    euid = os.geteuid()
    gid = os.getgid()
    egid = os.getegid()


    assert UserFactCollector().collect() == {
        'user_id': getpass.getuser(),
        'user_uid': uid,
        'user_gid': gid,
        'user_gecos': pwd.getpwuid(uid)[4],
        'user_dir': pwd.getpwuid(uid)[5],
        'user_shell': pwd.getpwuid(uid)[6],
        'real_user_id': uid,
        'effective_user_id': euid,
        'real_group_id': gid,
        'effective_group_id': egid,
    }

# Generated at 2022-06-13 03:42:48.704265
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    c = UserFactCollector()

    attributes_to_check = ['user_id', 'user_uid', 'user_gid',
                           'user_gecos', 'user_dir', 'user_shell',
                           'real_user_id', 'effective_user_id',
                           'real_group_id', 'effective_group_id']
    results = c.collect()
    for attribute_to_check in attributes_to_check:
        assert attribute_to_check in results

# Generated at 2022-06-13 03:42:55.352080
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    import platform
    import pwd
    tmp = UserFactCollector()
    res = tmp.collect()
    assert res['user_id'] == pwd.getpwuid(os.geteuid())[0]
    assert res['effective_user_id'] == os.geteuid()
    assert res['effective_group_id'] == os.getgid()
    assert res['real_user_id'] == os.getuid()
    assert res['real_group_id'] == os.getgid()
    # Make sure that, even on Windows, the results have all the expected keys.

# Generated at 2022-06-13 03:43:06.824249
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    import os

    test_collector = Collector.fetch_collector("UserFactCollector")
    facts = test_collector.collect()

    assert facts['user_id'] == getpass.getuser()
    assert facts['user_uid'] > 0
    assert facts['user_gid'] > 0
    assert facts['user_gecos'] != ""
    assert facts['user_dir'] != ""
    assert facts['user_shell'] != ""
    assert facts['real_user_id'] == os.getuid()
    assert facts['effective_user_id'] == os.geteuid()
    assert facts['real_group_id'] == os.getgid()
    assert facts['effective_group_id'] == os.getgid()