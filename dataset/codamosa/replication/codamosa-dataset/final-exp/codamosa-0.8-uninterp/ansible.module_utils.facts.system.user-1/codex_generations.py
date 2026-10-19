

# Generated at 2022-06-13 03:33:24.862051
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    ufc = UserFactCollector()

    user_facts = ufc.collect()

    assert user_facts['user_id'] == getpass.getuser()
    assert user_facts['user_uid'] == pwd.getpwuid(os.getuid()).pw_uid
    assert user_facts['user_gid'] == pwd.getpwuid(os.getuid()).pw_gid
    assert user_facts['user_gecos'] == pwd.getpwuid(os.getuid()).pw_gecos
    assert user_facts['user_dir'] == pwd.getpwuid(os.getuid()).pw_dir
    assert user_facts['user_shell'] == pwd.getpwuid(os.getuid()).pw_shell

# Generated at 2022-06-13 03:33:33.638037
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_info_dict = UserFactCollector().collect()
    assert user_info_dict['user_id'] == getpass.getuser()
    assert user_info_dict['user_uid'] == os.getuid()
    assert user_info_dict['user_gid'] == os.getgid()
    assert user_info_dict['real_user_id'] == os.getuid()
    assert user_info_dict['effective_user_id'] == os.geteuid()
    assert user_info_dict['real_group_id'] == os.getgid()
    assert user_info_dict['effective_group_id'] == os.getegid()

# Generated at 2022-06-13 03:33:40.652837
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    userfacts = UserFactCollector()
    facts = userfacts.collect()

    # Some basic sanity check
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

# Generated at 2022-06-13 03:33:50.202961
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    def getpwnam_mock(item):
        pwent = pwd.struct_passwd(('', '', 0, 0, '', '', ''))
        pwent.pw_uid = 1000
        pwent.pw_gid = 1000
        pwent.pw_gecos = 'test user'
        pwent.pw_dir = '/home/test'
        pwent.pw_shell = '/bin/bash'
        return pwent

    def getuid_mock(item):
        return 1000

    def geteuid_mock(item):
        return 1000

    def getgid_mock(item):
        return 1000

    def getegid_mock(item):
        return 1000

    getpass.getuser = lambda : 'test'
    pwd.getpwnam = get

# Generated at 2022-06-13 03:33:59.733544
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # GIVEN
    import os
    import pwd
    from ansible.module_utils.facts.collector import BaseFactCollector

    test_user = 'root'

    # WHEN
    result = UserFactCollector().collect()

    # THEN
    assert result['user_id'] == test_user
    assert result['user_uid'] == 0
    assert result['user_gid'] == 0
    assert result['user_gecos'] == 'root'
    assert result['user_dir'] == '/root'
    assert result['user_shell'] == '/bin/bash'
    assert result['real_user_id'] == 0
    assert result['effective_user_id'] == 0
    assert result['real_group_id'] == 0
    assert result['effective_group_id'] == 0

# Generated at 2022-06-13 03:34:07.929011
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    collector = UserFactCollector()
    facts_dict = collector.collect()
    assert facts_dict['user_id'] == getpass.getuser()
    assert facts_dict['user_uid'] == pwd.getpwuid(os.getuid()).pw_uid
    assert facts_dict['user_gid'] == pwd.getpwuid(os.getuid()).pw_gid
    assert facts_dict['user_gecos'] == pwd.getpwuid(os.getuid()).pw_gecos
    assert facts_dict['user_dir'] == pwd.getpwuid(os.getuid()).pw_dir
    assert facts_dict['user_shell'] == pwd.getpwuid(os.getuid()).pw_shell

# Generated at 2022-06-13 03:34:14.087451
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    class TestModule(object):
        def __init__(self, *args, **kwargs):
            self.params = dict()
    import ansible.module_utils.facts.collector
    ansible.module_utils.facts.collector.BaseFactCollector = object
    collected_facts = dict()
    TestModuleInstance = TestModule()
    TestUserFactCollectorInstance = UserFactCollector()
    TestUserFactCollectorInstance.collect(TestModuleInstance, collected_facts)

# Generated at 2022-06-13 03:34:24.636614
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_fact_collector = UserFactCollector()
    user_facts = user_fact_collector.collect()
    assert user_facts.get('user_id') is not None
    assert user_facts.get('user_uid') is not None
    assert user_facts.get('user_gid') is not None
    assert user_facts.get('user_gecos') is not None
    assert user_facts.get('user_dir') is not None
    assert user_facts.get('user_shell') is not None
    assert user_facts.get('real_user_id') is not None
    assert user_facts.get('effective_user_id') is not None
    assert user_facts.get('effective_group_ids') is not None

# Generated at 2022-06-13 03:34:29.321264
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    import os
    import pwd
    # TODO: Mock getpass.getuser
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector import UserFactCollector

    user_facts = UserFactCollector()

    # Test: User ID has expected value
    fact_id = 'user_id'
    assert fact_id in user_facts._fact_ids, "collect() found fact: " + fact_id
    assert user_facts.collect()[fact_id] == getpass.getuser(), fact_id + " value should be " + getpass.getuser() + " but is " + user_facts.collect()[fact_id]

    # Test: User UID has expected value
    fact_id = 'user_uid'
    assert fact_id in user

# Generated at 2022-06-13 03:34:37.443220
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    import os

    collected_facts = {}
    # Create mocks set
    os_getuid = os.getuid

    # Setup mock
    class osMock:
        @staticmethod
        def getuid():
            return 0
    # Set mock
    os.getuid = osMock.getuid

    user_fact_collector = UserFactCollector()
    # Test
    user_fact_collector.collect(collected_facts=collected_facts)
    # Reset mocks
    os.getuid = os_getuid



# Generated at 2022-06-13 03:34:45.221700
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    a = UserFactCollector()
    response = a.collect()
    assert 'user_id' in response
    assert 'user_uid' in response
    assert 'user_gid' in response
    assert 'user_gecos' in response
    assert 'user_dir' in response
    assert 'user_shell' in response
    assert 'real_user_id' in response
    assert 'effective_user_id' in response
    assert 'real_group_id' in response
    assert 'effective_group_id' in response

# Unit test to validate _fact_ids attribute of class UserFactCollector

# Generated at 2022-06-13 03:34:54.712267
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_fc = UserFactCollector()

    assert isinstance(user_fc.collect(), dict)
    assert user_fc.collect().keys() >= user_fc._fact_ids
    assert isinstance(user_fc.collect()['user_id'], str)
    assert isinstance(user_fc.collect()['user_uid'], int)
    assert isinstance(user_fc.collect()['user_gid'], int)
    assert isinstance(user_fc.collect()['user_gecos'], str)
    assert isinstance(user_fc.collect()['user_dir'], str)
    assert isinstance(user_fc.collect()['user_shell'], str)
    assert isinstance(user_fc.collect()['real_user_id'], int)

# Generated at 2022-06-13 03:34:57.723303
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    import ansible.module_utils.facts.system.user
    ufc = ansible.module_utils.facts.system.user.UserFactCollector()
    assert ufc.collect()['user_id'] == getpass.getuser()

# Generated at 2022-06-13 03:35:00.481787
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # See TESTING.rst / Mocking Objects
    pass

# Generated at 2022-06-13 03:35:10.359412
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    """Test case to validate collect function of UserFactCollector Class"""
    userfactcollector = UserFactCollector()
    user_id = getpass.getuser()
    fact_list = ['user_id', 'user_uid', 'user_gid', 'user_gecos', 'user_dir',
                 'user_shell', 'real_user_id', 'effective_user_id']
    result = {}
    result = userfactcollector.collect()
    assert isinstance(result, dict)
    assert set(result.keys()).intersection(set(fact_list)) == set(fact_list)
    assert set(result['user_id']) == set(user_id)

# Generated at 2022-06-13 03:35:14.806945
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    ufc = UserFactCollector()
    user_facts = ufc.collect()

    assert(user_facts['user_id'] == getpass.getuser())
    assert(user_facts['effective_user_id'] == os.getuid())
    assert(user_facts['user_uid'] == os.getuid())

# Generated at 2022-06-13 03:35:25.765616
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    actual_user_facts = UserFactCollector().collect()

    assert actual_user_facts['user_id'] == getpass.getuser()
    assert actual_user_facts['user_uid'] == os.getuid()
    assert actual_user_facts['user_gid'] == os.getgid()
    assert actual_user_facts['user_gecos'] == pwd.getpwuid(os.getuid()).pw_gecos
    assert actual_user_facts['user_dir'] == pwd.getpwuid(os.getuid()).pw_dir
    assert actual_user_facts['user_shell'] == pwd.getpwuid(os.getuid()).pw_shell
    assert actual_user_facts['real_user_id'] == os.getuid()
    assert actual_user

# Generated at 2022-06-13 03:35:33.125063
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_facts = UserFactCollector().collect()

    import getpass
    import pwd
    import os

    assert getpass.getuser() == user_facts['user_id']
    pwent = pwd.getpwnam(getpass.getuser())
    assert pwent.pw_uid == user_facts['user_uid']
    assert pwent.pw_gid == user_facts['user_gid']
    assert pwent.pw_gecos == user_facts['user_gecos']
    assert pwent.pw_dir == user_facts['user_dir']
    assert pwent.pw_shell == user_facts['user_shell']
    assert os.getuid() == user_facts['real_user_id']

# Generated at 2022-06-13 03:35:34.406966
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    pass

# Generated at 2022-06-13 03:35:39.339288
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user = UserFactCollector()
    collected_facts = user.collect()
    assert isinstance(collected_facts, dict)
    assert collected_facts['real_user_id'] == os.getuid()
    assert collected_facts['effective_user_id'] == os.getuid()

# Generated at 2022-06-13 03:35:51.101766
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # Test for different values
    collected_facts = {}
    u_collector = UserFactCollector()
    user_facts = u_collector.collect(collected_facts=collected_facts)
    assert user_facts == {
        'effective_group_id': 1000,
        'effective_user_id': 1000,
        'real_group_id': 1000,
        'real_user_id': 1000,
        'user_dir': '/home/user',
        'user_gid': 1000,
        'user_gecos': 'user gecos',
        'user_id': 'user',
        'user_shell': '/bin/bash',
        'user_uid': 1000
    }

# Generated at 2022-06-13 03:36:01.175791
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # arrange
    user_facts = {}
    test_user_id =  'user_id'
    test_user_uid = 1000
    test_user_gid = 1000
    test_user_gecos = 'test user_gecos'
    test_user_dir = '/home/test'
    test_user_shell = '/bin/bash'
    test_real_user_id = 1000
    test_effective_user_id = 1000
    test_real_group_id = 1000
    test_effective_group_id = 1000
    user_facts['user_id'] = test_user_id
    user_facts['user_uid'] = test_user_uid
    user_facts['user_gid'] = test_user_gid
    user_facts['user_gecos'] = test_user_gecos
   

# Generated at 2022-06-13 03:36:12.366747
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():

    # Simulate the environment
    real_getuser = getpass.getuser
    pwent = pwd.getpwuid(os.getuid())
    real_getpwnam = pwd.getpwnam
    module = None
    collected_facts = None
    getpass.getuser = lambda: 'johndoe'

    pwd.getpwnam = lambda x: pwent

    # Execute UserFactCollector.collect
    ufc = UserFactCollector()

# Generated at 2022-06-13 03:36:22.074857
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    new_FactCollector = UserFactCollector()
    test_facts = new_FactCollector.collect()
    assert isinstance(test_facts, dict)
    assert 'user_id' in test_facts
    assert 'user_uid' in test_facts
    assert 'user_gid' in test_facts
    assert 'user_gecos' in test_facts
    assert 'user_dir' in test_facts
    assert 'user_shell' in test_facts
    assert 'real_user_id' in test_facts
    assert 'effective_user_id' in test_facts
    assert 'real_group_id' in test_facts
    assert 'effective_group_id' in test_facts

# Generated at 2022-06-13 03:36:23.548533
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user = UserFactCollector()

    assert isinstance(user.collect(), dict)

# Generated at 2022-06-13 03:36:29.631973
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    """UserFactCollector - collect facts
    """
    user_facts = UserFactCollector().collect()
    assert user_facts['user_id'] == 'root'
    assert user_facts['user_uid'] == 0
    assert user_facts['user_dir'] == '/root'
    assert user_facts['real_group_id'] == 0
    assert user_facts['effective_group_id'] == 0


# Generated at 2022-06-13 03:36:38.371953
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_id = getpass.getuser()
    user_uid = pwd.getpwnam(getpass.getuser()).pw_uid
    user_gid = pwd.getpwnam(getpass.getuser()).pw_gid
    user_gecos = pwd.getpwnam(getpass.getuser()).pw_gecos
    user_dir = pwd.getpwnam(getpass.getuser()).pw_dir
    user_shell =pwd.getpwnam(getpass.getuser()).pw_shell
    real_user_id = os.getuid()
    effective_user_id = os.geteuid()
    real_group_id = os.getgid()
    effective_group_id = os.getgid()

    user_

# Generated at 2022-06-13 03:36:41.776053
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_facts = {'user_id': 'qthk', 'user_uid': 1001, 'user_gid': 1001, 'user_gecos': 'qthk,,,', 'user_dir': '/home/qthk', 'user_shell': '/bin/bash', 'real_user_id': 1001, 'effective_user_id': 1001, 'real_group_id': 1001, 'effective_group_id': 1001}
    assert UserFactCollector.collect() == user_facts

# Generated at 2022-06-13 03:36:51.367300
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # Dummy class for testing
    class Dummy:
        def __init__(self):
            self.ansible_facts = {}

    m = Dummy()

    u = UserFactCollector()
    u.collect(module=m)

    try:
        pwent = pwd.getpwnam(getpass.getuser())
    except KeyError:
        pwent = pwd.getpwuid(os.getuid())


# Generated at 2022-06-13 03:37:00.650058
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    userfc = UserFactCollector()
    user_facts = userfc.collect()
    assert user_facts['user_id'] == getpass.getuser()
    if os.getuid() == 0 and pwd.getpwuid(os.getuid())[0] == 'root':
        assert user_facts['real_user_id'] == user_facts['effective_user_id'] == 0
        assert user_facts['real_group_id'] == user_facts['effective_group_id'] == 0
    else:
        assert user_facts['real_user_id'] != user_facts['effective_user_id']
        assert user_facts['effective_user_id'] == 0
        assert user_facts['real_group_id'] != user_facts['effective_group_id']

# Generated at 2022-06-13 03:37:07.817968
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_id = pwd.getpwuid(os.getuid()).pw_name
    user_fact_collector = UserFactCollector()
    user_facts = user_fact_collector.collect()
    assert type(user_facts) == dict
    assert user_facts['user_id']
    assert user_facts['user_id'] == user_id
    assert user_facts['user_uid']
    assert user_facts['user_uid'] == os.getuid()
    assert user_facts['user_gid']
    assert user_facts['user_gid'] == os.getgid()
    assert user_facts['user_gecos']
    assert user_facts['user_gecos'] == pwd.getpwuid(os.getuid()).pw_gecos

# Generated at 2022-06-13 03:37:11.882619
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # Initialize an object of class UserFactCollector
    user_fact_collector_obj = UserFactCollector()

    # Assert the returned data of method collect
    assert user_fact_collector_obj.collect() == {'effective_group_id': 1000, 'effective_user_id': 1000, 'real_group_id': 1000, 'real_user_id': 1000, 'user_dir': '/home/vagrant', 'user_gecos': 'Vagrant', 'user_gid': 1000, 'user_id': 'vagrant', 'user_shell': '/bin/bash', 'user_uid': 1000}

# Generated at 2022-06-13 03:37:21.841469
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    '''
    This function test the collect method of class UserFactCollector.
    '''
    # Prepare parameters for UserFactCollector.collect
    module = None
    collected_facts = {}

    # Make UserFactCollector.collect return a valid fact
    def pwd_getpwnam_func(username):
        '''
        This function is used to mock pwd.getpwnam with the username provided
        by getpass.getuser.
        '''
        pwent = {'pw_uid': 1000, 'pw_gid': 1000, 'pw_gecos': '', 'pw_dir': '/home/username',
                 'pw_shell': '/bin/bash'}
        return pwent


# Generated at 2022-06-13 03:37:33.942697
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_fact_collector = UserFactCollector()
    user_facts = user_fact_collector.collect()
    assert user_facts['user_id'] == getpass.getuser()
    assert 'user_uid' in user_facts.keys()
    assert 'user_gid' in user_facts.keys()
    assert 'user_gecos' in user_facts.keys()
    assert 'user_dir' in user_facts.keys()
    assert 'user_shell' in user_facts.keys()
    assert 'real_user_id' in user_facts.keys()
    assert 'effective_user_id' in user_facts.keys()
    assert 'real_group_id' in user_facts.keys()
    assert 'effective_group_id' in user_facts.keys()

# Generated at 2022-06-13 03:37:37.875731
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    ufc = UserFactCollector()
    ret = ufc.collect()
    assert ret['user_id'] == getpass.getuser()
    assert ret['user_shell'] == pwd.getpwnam(getpass.getuser()).pw_shell

# Generated at 2022-06-13 03:37:40.359511
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    test_UserFactCollector = UserFactCollector()
    ans = test_UserFactCollector.collect()
    keys = ans.keys()
    assert 'user_id' in keys
    assert 'user_uid' in keys
    assert 'user_gid' in keys
    assert 'user_gecos' in keys
    assert 'user_dir' in keys
    assert 'user_shell' in keys
    assert 'real_user_id' in keys
    assert 'effective_user_id' in keys
    assert 'effective_group_ids' in keys

# Generated at 2022-06-13 03:37:41.391384
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    UserFactCollector().collect()

# Generated at 2022-06-13 03:37:48.296589
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # If a normal user facts is expected
    # 
    # 

    # If a user facts is expected
    # 
    # When a user ID is provided and is a normal user account
    # 
    # Then UserFactCollector.collect is expected to return a valid user facts

    # If a user facts is expected
    # 
    # When a user ID is provided and is not a normal user account
    # 
    # Then UserFactCollector.collect is expected to return an empty user facts
    pass

# Generated at 2022-06-13 03:37:52.525371
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # We can't rely on the exact contents of vars() being repeated, but
    # we can make sure they're not empty.
    x = UserFactCollector()
    assert x.collect() == {}

# Generated at 2022-06-13 03:37:57.145664
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():

    # Create an instance of UserFactCollector
    t = UserFactCollector()

    # Call method collect of the instance and
    # check that the result is not None.
    result = t.collect()
    assert result is not None

    # Check that the result is a dictionary.
    assert isinstance(result, dict)


# Generated at 2022-06-13 03:38:11.936565
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_facts = UserFactCollector()
    collected_facts = user_facts.collect()
    assert collected_facts['user_id'] == getpass.getuser()
    assert collected_facts['user_uid'] == pwd.getpwuid(os.getuid()).pw_uid
    assert collected_facts['user_gid'] == pwd.getpwuid(os.getuid()).pw_gid
    assert collected_facts['user_gecos'] == pwd.getpwuid(os.getuid()).pw_gecos
    assert collected_facts['user_dir'] == pwd.getpwuid(os.getuid()).pw_dir
    assert collected_facts['user_shell'] == pwd.getpwuid(os.getuid()).pw_shell
    assert collected_

# Generated at 2022-06-13 03:38:22.722317
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():

    collector = UserFactCollector()
    user_facts = collector.collect()

    print("user_facts: ", user_facts)

    assert type(user_facts) == dict
    assert user_facts['user_id'] == getpass.getuser()
    assert type(user_facts['user_uid']) == int
    assert type(user_facts['user_gid']) == int
    assert type(user_facts['user_gecos']) == str
    assert type(user_facts['user_dir']) == str
    assert type(user_facts['user_shell']) == str
    assert user_facts['real_user_id'] == os.getuid()
    assert user_facts['effective_user_id'] == os.geteuid()
    assert user_facts['real_group_id'] == os.getg

# Generated at 2022-06-13 03:38:33.068632
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.collector import Collector
    import pwd

    def mock_getpwnam(username):
        return pwd.struct_passwd((username, '*', 1000, 1000, 'User 1',
                                  '/home/user1', '/bin/bash'))

    def mock_getpwuid(uid):
        return pwd.struct_passwd(('user2', '*', uid, 1001, 'User 2',
                                  '/home/user2', '/bin/bash'))

    monkeypatch.setattr(pwd, 'getpwnam', mock_getpwnam)
    monkeypatch.setattr(pwd, 'getpwuid', mock_getpwuid)


# Generated at 2022-06-13 03:38:44.844473
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():

    def mock_get_user(self):
        return 'test_user'

    def mock_getpwnam(name):
        pwent = pwd.struct_passwd(('test_user', '', 0, 0, 'Test User',
                                   '/home/test_user', '/bin/bash'))
        return pwent

    def mock_getuid():
        return 0

    def mock_geteuid():
        return 0

    def mock_getgid():
        return 0

    def mock_getegid():
        return 0

    def mock_getgroups():
        return [100, 10]

    user_facts = {}

    user_collector = UserFactCollector()

    user_collector.get_user = mock_get_user
    pwd.getpwnam = mock_getpwnam
   

# Generated at 2022-06-13 03:38:47.455013
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    fact_collector = UserFactCollector()
    fact_collector.collect()

# Generated at 2022-06-13 03:38:49.627802
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    User_test = UserFactCollector()
    assert User_test.user_id == 'user_id'

# Generated at 2022-06-13 03:38:53.632654
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # Instantiate object of class UserFactCollector
    collector = UserFactCollector()

    # Invoke method collect
    collector.collect()

    assert collector is not None
    assert os.getuid() == collector.fact_values['effective_user_id']


# Generated at 2022-06-13 03:39:01.901644
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    um_obj = UserFactCollector()
    collected_facts = um_obj.collect()
    assert collected_facts['user_id'] == getpass.getuser()
    assert collected_facts['user_uid'] == pwd.getpwnam(getpass.getuser()).pw_uid
    assert collected_facts['user_gid'] == pwd.getpwnam(getpass.getuser()).pw_gid
    assert collected_facts['user_gecos'] == pwd.getpwnam(getpass.getuser()).pw_gecos
    assert collected_facts['user_dir'] == pwd.getpwnam(getpass.getuser()).pw_dir
    assert collected_facts['user_shell'] == pwd.getpwnam(getpass.getuser()).pw_shell

# Generated at 2022-06-13 03:39:13.341302
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    import mock
    gecos_value = "gecos_value"
    mock_pwent = mock.MagicMock(pw_gecos=gecos_value)
    mock_getpwnam = mock.MagicMock(return_value =
                                   mock_pwent)
    mock_getpwuid = mock.MagicMock(return_value =
                                   mock_pwent)

    with mock.patch("ansible.module_utils.facts.collector.UserFactCollector.pwd",
                    autospec=True) as mock_pwd:
        mock_pwd.getpwnam = mock_getpwnam
        mock_pwd.getpwuid = mock_getpwuid
        ufc = UserFactCollector()
        res = ufc.collect()

# Generated at 2022-06-13 03:39:23.680572
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    from ansible.module_utils.facts import ModuleFacts, FactManager
    from ansible.module_utils.facts.collector import get_collector_instance

    fm = FactManager(None, None)

    # Build facts
    facts = {
        'fact_id': 'value'
    }
    module_facts = ModuleFacts(None, '', module_name='collector', facts=facts)

    # Test that module_facts.facts is returned as is
    fact_collector = get_collector_instance('UserFactCollector', module_facts, fm)
    result = fact_collector.collect()
    assert result is module_facts.facts

    # Test with empty facts
    module_facts = ModuleFacts(None, '', module_name='collector', facts={})


# Generated at 2022-06-13 03:39:44.714557
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():

    # Arrange
    getuser_mock = MockGetuser()
    getpwnam_mock = MockGetpwnam()
    getpwuid_mock = MockGetpwuid()
    getuid_mock = MockGetuid()
    geteuid_mock = MockGeteuid()
    getgid_mock = MockGetgid()

    # Arrange
    collector = UserFactCollector()
    collector.__getuser__ = getuser_mock.getuser
    collector.__getpwnam__ = getpwnam_mock.getpwnam
    collector.__getpwuid__ = getpwuid_mock.getpwuid
    collector.__getuid__ = getuid_mock.getuid

# Generated at 2022-06-13 03:39:52.397868
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_fact_collector = UserFactCollector()
    user_facts = user_fact_collector.collect()
    assert user_facts['user_id'] == getpass.getuser()
    assert user_facts['real_user_id'] == os.getuid()
    assert user_facts['effective_user_id'] == os.geteuid()
    assert user_facts['real_group_id'] == os.getgid()
    assert user_facts['effective_group_id'] == os.getgid()

# Generated at 2022-06-13 03:39:58.774213
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


# Generated at 2022-06-13 03:40:01.645149
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():

    test_user_collector = UserFactCollector()

    # Test if method collect does not return a empty dict
    test_result = test_user_collector.collect()
    assert test_result != {}

# Generated at 2022-06-13 03:40:11.805818
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    test_obj = UserFactCollector()
    gid = os.getgid()
    uid = os.getuid()
    username = getpass.getuser()
    output = {'user_id': username,
              'user_gid': gid,
              'user_uid': uid,
              'user_gecos': pwd.getpwuid(uid)[4],
              'user_dir': pwd.getpwuid(uid)[5],
              'user_shell': pwd.getpwuid(uid)[6],
              'real_user_id': uid,
              'effective_user_id': uid,
              'real_group_id': gid,
              'effective_group_id': gid}
    assert test_obj.collect() == output

# Generated at 2022-06-13 03:40:18.191718
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    obj = UserFactCollector()
    res = obj.collect()

    assert "user_uid" in res
    assert "user_gid" in res
    assert "user_gecos" in res
    assert "user_dir" in res
    assert "user_shell" in res
    assert "real_user_id" in res
    assert "effective_user_id" in res
    assert "real_group_id" in res
    assert "effective_group_id" in res

# Generated at 2022-06-13 03:40:21.305606
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    result = {}
    userFactCollector = UserFactCollector()
    fact_ids = userFactCollector._fact_ids
    for fact_id in fact_ids:
        result[fact_id] = fact_id
    assert(result == userFactCollector.collect())

# Generated at 2022-06-13 03:40:23.843658
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    test_UserFactCollector = UserFactCollector()
    user_facts = test_UserFactCollector.collect()
    assert user_facts['user_id'] == getpass.getuser()


# Generated at 2022-06-13 03:40:33.955083
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():

    collector = UserFactCollector()
    result = collector.collect()

    assert result['user_id'] == getpass.getuser()
    assert result['real_user_id'] == os.getuid()
    assert result['effective_user_id'] == os.geteuid()
    assert result['real_group_id'] == os.getgid()
    assert result['effective_group_id'] == os.getgid()

    pwent = pwd.getpwnam(getpass.getuser())
    assert result['user_uid'] == pwent.pw_uid
    assert result['user_gid'] == pwent.pw_gid
    assert result['user_gecos'] == pwent.pw_gecos
    assert result['user_dir'] == pwent.pw_dir

# Generated at 2022-06-13 03:40:42.504709
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    """
    Unit test for UserFactCollector's collect method
    """
    results = UserFactCollector().collect()

    assert isinstance(results, dict)
    assert results['user_id']
    assert results['user_uid']
    assert results['user_gid']
    assert results['user_dir']
    assert results['user_shell']
    assert results['real_user_id']
    assert results['effective_user_id']
    assert results['real_group_id']
    assert results['effective_group_id']

# Generated at 2022-06-13 03:41:14.254068
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_facts = UserFactCollector().collect()

    assert user_facts['user_id']
    assert user_facts['user_uid']
    assert user_facts['user_gid']
    assert user_facts['user_gecos']
    assert user_facts['user_dir']
    assert user_facts['user_shell']

# Generated at 2022-06-13 03:41:21.236409
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    import os
    import getpass

    # Create an instance of UserFactCollector
    c = UserFactCollector()

    # Call method collect
    facts = c.collect()

    # Verify that the returned data structure is what we expect
    assert facts['user_id'] == getpass.getuser()
    assert facts['user_uid'] == os.getuid()
    assert facts['real_user_id'] == os.getuid()
    assert facts['effective_user_id'] == os.geteuid()
    assert facts['user_gid'] == os.getgid()
    assert facts['real_group_id'] == os.getgid()
    assert facts['effective_group_id'] == os.getegid()
    assert facts['user_dir'] == os.getcwd()

# Generated at 2022-06-13 03:41:33.112758
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    """
    Create an instance of UserFactCollector and invoke
    method collect of class UserFactCollector.
    """
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

# Generated at 2022-06-13 03:41:42.964992
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():

    user_facts = UserFactCollector().collect()
    assert(user_facts['user_id'] == getpass.getuser())
    assert(user_facts['user_uid'] == os.getuid())
    assert(user_facts['user_gid'] == os.getgid())
    assert(user_facts['user_shell'] == pwd.getpwuid(os.getuid()).pw_shell)
    assert(user_facts['user_gecos'] == pwd.getpwuid(os.getuid()).pw_gecos)
    assert(user_facts['user_dir'] == pwd.getpwuid(os.getuid()).pw_dir)
    assert(user_facts['real_user_id'] == os.getuid())

# Generated at 2022-06-13 03:41:48.851493
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    assert UserFactCollector().collect() == {u'user_id': u'ansible', u'user_uid': 501, u'user_gid': 20, u'user_gecos': u'Ansible Local User,,,', u'user_dir': u'/Users/ansible', u'user_shell': u'/bin/bash', u'real_user_id': 501, u'effective_user_id': 501, u'real_group_id': 20, u'effective_group_id': 20}

# Generated at 2022-06-13 03:41:57.192719
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # Instantiate a UserFactCollector object
    user_fact_collector = UserFactCollector()

    # Call the method collect of UserFactCollector
    user_facts = user_fact_collector.collect()

    # Assert the collected facts
    assert(user_facts['user_id'] == getpass.getuser())
    pwent = pwd.getpwnam(getpass.getuser())
    assert(user_facts['user_uid'] == pwent.pw_uid)
    assert(user_facts['user_gid'] == pwent.pw_gid)
    assert(user_facts['user_gecos'] == pwent.pw_gecos)
    assert(user_facts['user_dir'] == pwent.pw_dir)

# Generated at 2022-06-13 03:42:02.321799
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_collector = UserFactCollector()
    collected_facts = user_collector.collect()
    assert(collected_facts['user_id'] == getpass.getuser())
    assert(collected_facts['user_gid'] == pwd.getpwuid(os.getuid()).pw_gid)

# Generated at 2022-06-13 03:42:04.353035
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    '''Test UserFactCollector.collect()'''
    fact_collector = UserFactCollector()
    fact_collector.collect()

# Generated at 2022-06-13 03:42:13.727076
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    cf = UserFactCollector()
    collected_facts = cf.collect()
    assert collected_facts['user_id'] == getpass.getuser()
    assert collected_facts['user_uid'] == pwd.getpwuid(os.getuid()).pw_uid
    assert collected_facts['user_gid'] == pwd.getpwuid(os.getuid()).pw_gid
    assert collected_facts['real_user_id'] == os.getuid()
    assert collected_facts['effective_user_id'] == os.geteuid()
    assert collected_facts['real_group_id'] == os.getgid()
    assert collected_facts['effective_group_id'] == os.getgid()

# Generated at 2022-06-13 03:42:14.277868
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    pass