

# Generated at 2022-06-13 03:33:24.187989
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    fact_collector = UserFactCollector(None)

    user_facts = fact_collector.collect()

    assert user_facts['user_id'] == getpass.getuser()
    assert user_facts['user_uid'] == os.getuid()
    assert user_facts['user_gid'] == os.getgid()
    assert user_facts['real_user_id'] == os.getuid()
    assert user_facts['real_group_id'] == os.getgid()
    assert user_facts['effective_user_id'] == os.geteuid()
    assert user_facts['effective_group_id'] == os.getegid()

# Generated at 2022-06-13 03:33:28.373413
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # unit_test start
    user = UserFactCollector()
    user_facts = user.collect()
    print(user_facts)
    # unit_test stop

# When run as a script
if __name__ == '__main__':
    test_UserFactCollector_collect()

# Generated at 2022-06-13 03:33:37.273626
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_collector = UserFactCollector()
    user_facts = user_collector.collect()
    assert user_facts['user_id'] == getpass.getuser()
    assert user_facts['user_uid'] == pwd.getpwnam(getpass.getuser()).pw_uid
    assert user_facts['user_gid'] == pwd.getpwnam(getpass.getuser()).pw_gid
    assert user_facts['user_gecos'] == pwd.getpwnam(getpass.getuser()).pw_gecos
    assert user_facts['user_dir'] == pwd.getpwnam(getpass.getuser()).pw_dir
    assert user_facts['user_shell'] == pwd.getpwnam(getpass.getuser()).pw

# Generated at 2022-06-13 03:33:47.111808
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_facts = UserFactCollector()
    user_facts_collected = user_facts.collect()

    assert user_facts_collected['user_id'] == getpass.getuser()
    assert user_facts_collected['user_uid'] == pwd.getpwuid(os.getuid()).pw_uid
    assert user_facts_collected['user_gid'] == pwd.getpwuid(os.getuid()).pw_gid
    assert user_facts_collected['user_gecos'] == pwd.getpwuid(os.getuid()).pw_gecos
    assert user_facts_collected['user_dir'] == pwd.getpwuid(os.getuid()).pw_dir
    assert user_facts_collected['user_shell'] == pwd

# Generated at 2022-06-13 03:33:57.237342
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    import collections

    Fact = collections.namedtuple('Fact', ['name', 'type'])
    facts = [
        Fact(name='user_id', type='string'),
        Fact(name='user_uid', type='int'),
        Fact(name='user_gid', type='int'),
        Fact(name='user_gecos', type='string'),
        Fact(name='user_dir', type='string'),
        Fact(name='user_shell', type='string'),
        Fact(name='real_user_id', type='int'),
        Fact(name='effective_user_id', type='int'),
        Fact(name='real_group_id', type='int'),
        Fact(name='effective_group_id', type='int')
    ]

    user_fact_collector = UserFactCollector()

    assert user_

# Generated at 2022-06-13 03:34:01.903363
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_fact_collector = UserFactCollector()
    user_facts = user_fact_collector.collect()
    assert user_facts['user_id'] == getpass.getuser()
    assert user_facts['real_user_id'] == os.getuid()
    assert user_facts['effective_user_id'] == os.geteuid()
    assert user_facts['real_group_id'] == os.getgid()
    assert user_facts['effective_group_id'] == os.getgid()

# Generated at 2022-06-13 03:34:13.077790
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_facts = UserFactCollector().collect()
    assert user_facts['user_id'] == getpass.getuser()
    assert isinstance(user_facts['user_uid'], int)
    assert isinstance(user_facts['user_gid'], int)
    assert isinstance(user_facts['user_gecos'], str)
    assert isinstance(user_facts['user_dir'], str)
    assert isinstance(user_facts['user_shell'], str)
    assert isinstance(user_facts['real_user_id'], int)
    assert isinstance(user_facts['effective_user_id'], int)
    assert isinstance(user_facts['real_group_id'], int)
    assert isinstance(user_facts['effective_group_id'], int)

# Generated at 2022-06-13 03:34:21.257230
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    fc = UserFactCollector()
    assert fc.collect() == {'user_id': 'vagrant', 'user_uid': 1000,
                            'user_gid': 1000, 'user_gecos': 'vagrant,,,',
                            'user_dir': '/home/vagrant', 'user_shell': '/bin/bash',
                            'real_user_id': 1000, 'effective_user_id': 1000,
                            'real_group_id': 1000, 'effective_group_id': 1000}


# Generated at 2022-06-13 03:34:29.030213
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    ufc = UserFactCollector()
    res = ufc.collect()
    assert 'user_id' in res
    assert isinstance(res['user_id'], str)
    assert 'user_uid' in res
    assert isinstance(res['user_uid'], int)
    assert 'user_gid' in res
    assert isinstance(res['user_gid'], int)
    assert 'user_gecos' in res
    assert isinstance(res['user_gecos'], str)
    assert 'user_dir' in res
    assert isinstance(res['user_dir'], str)
    assert 'user_shell' in res
    assert isinstance(res['user_shell'], str)
    assert 'real_user_id' in res

# Generated at 2022-06-13 03:34:40.039372
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_facts_collector = UserFactCollector()
    user_facts = {}

    user_facts_collector.collect(user_facts)

    assert user_facts['user_id'] == getpass.getuser()

    try:
        pwent = pwd.getpwnam(getpass.getuser())
    except KeyError:
        pwent = pwd.getpwuid(os.getuid())

    assert user_facts['user_uid'] == pwent.pw_uid
    assert user_facts['user_gid'] == pwent.pw_gid
    assert user_facts['user_gecos'] == pwent.pw_gecos
    assert user_facts['user_dir'] == pwent.pw_dir
    assert user_facts['user_shell'] == pwent.pw_shell

# Generated at 2022-06-13 03:34:48.983333
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    ufc = UserFactCollector()

# Generated at 2022-06-13 03:34:51.936563
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    userFactCol = UserFactCollector()
    # Call the collect method and assert it got the right set og _fact_ids
    assert (userFactCol.collect() == userFactCol._fact_ids)

# Generated at 2022-06-13 03:35:00.746552
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    def mock_getpwnam(name):
        mock_pwent = getpwnam_mock()
        mock_pwent.pw_name = name
        return mock_pwent

    def mock_geteuid():
        return 1000

    def mock_getegid():
        return 1000

    # set up mock objects for testing and stub out the functions that are called
    pwd_mock = pwd_mock_class()
    getpwnam_mock = pwd_mock_class()
    os_mock = os_mock_class()
    ansible_mock = ansible_mock_class()
    user_collector = UserFactCollector()

    # find the result for the test user defined below
    base_pwent = pwd.getpwnam("root")

    # test standard

# Generated at 2022-06-13 03:35:11.974751
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    '''
    Unit test for method collect of class UserFactCollector
    '''
    userFactCollector = UserFactCollector()
    user_facts = userFactCollector.collect(None, None)
    assert len(user_facts) > 0
    assert 'user_id' in user_facts
    assert user_facts['user_id'] == getpass.getuser()
    assert 'user_uid' in user_facts
    assert 'user_gid' in user_facts
    assert 'user_gecos' in user_facts
    assert 'user_dir' in user_facts
    assert 'user_shell' in user_facts
    assert 'real_user_id' in user_facts
    assert 'effective_user_id' in user_facts
    assert 'real_group_id' in user_facts

# Generated at 2022-06-13 03:35:23.018193
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    module = None
    collected_facts = {}

    userfact = UserFactCollector()
    userfact.collect(module, collected_facts)

    assert 'effective_group_ids' in collected_facts
    assert 'effective_user_id' in collected_facts
    assert 'real_user_id' in collected_facts
    assert 'real_group_id' in collected_facts
    assert 'user_shell' in collected_facts
    assert 'user_dir' in collected_facts
    assert 'user_gecos' in collected_facts
    assert 'user_gid' in collected_facts
    assert 'user_uid' in collected_facts
    assert 'user_id' in collected_facts

if __name__ == '__main__':
    test_UserFactCollector_collect()

# Generated at 2022-06-13 03:35:31.562885
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_collector = UserFactCollector()
    user_facts = user_collector.collect()

    assert 'user_id' in user_facts, "user_facts['user_id'] should in user_facts"
    assert 'user_uid' in user_facts, "user_facts['user_uid'] should in user_facts"
    assert 'user_gid' in user_facts, "user_facts['user_gid'] should in user_facts"
    assert 'user_gecos' in user_facts, "user_facts['user_gecos'] should in user_facts"
    assert 'user_dir' in user_facts, "user_facts['user_dir'] should in user_facts"
    assert 'user_shell' in user_facts, "user_facts['user_shell'] should in user_facts"

# Generated at 2022-06-13 03:35:40.514182
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

# Generated at 2022-06-13 03:35:51.881088
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    import pwd

    # Create a UserFactCollector instance
    fact_collector = UserFactCollector()

    # Test collect method
    collected_facts = fact_collector.collect()

    # Test collected_facts is a dict
    assert isinstance(collected_facts, dict)

    # Test collect method produces expected facts
    try:
        pwent = pwd.getpwnam(getpass.getuser())
    except KeyError:
        pwent = pwd.getpwuid(os.getuid())
    assert collected_facts['user_id'] == getpass.getuser()
    assert collected_facts['user_uid'] == pwent.pw_uid
    assert collected_facts['user_gid'] == pwent.pw_gid
    assert collected_facts['user_gecos'] == pwent.p

# Generated at 2022-06-13 03:36:01.650176
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    '''
    Unit test for method collect of class UserFactCollector.
    '''
    user_fact_collector_obj = UserFactCollector()
    user_fact_list = user_fact_collector_obj.collect()
    assert user_fact_list.get('user_id')
    assert user_fact_list.get('user_uid')
    assert user_fact_list.get('user_gid')
    assert user_fact_list.get('user_gecos')
    assert user_fact_list.get('user_dir')
    assert user_fact_list.get('user_shell')
    assert user_fact_list.get('real_user_id')
    assert user_fact_list.get('effective_user_id')
    assert user_fact_list.get('real_group_id')

# Generated at 2022-06-13 03:36:13.030370
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_facts = UserFactCollector().collect()
    assert user_facts['user_id'] == getpass.getuser()
    assert user_facts['real_user_id'] == os.getuid()
    assert user_facts['effective_user_id'] == os.geteuid()
    assert user_facts['real_group_id'] == os.getgid()
    assert user_facts['effective_group_id'] == os.getgid()
    try:
        pwent = pwd.getpwnam(getpass.getuser())
    except KeyError:
        pwent = pwd.getpwuid(os.getuid())
    assert user_facts['user_uid'] == pwent.pw_uid
    assert user_facts['user_gid'] == pwent.pw_gid

# Generated at 2022-06-13 03:36:24.951745
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # Test passing in a module
    collector = UserFactCollector()
    test_facts = collector.collect()

    assert test_facts['user_id'], "user_id value from UserFactCollector.collect() is empty"
    assert test_facts['user_uid'], "user_uid value from UserFactCollector.collect() is empty"
    assert test_facts['user_gid'], "user_gid value from UserFactCollector.collect() is empty"
    assert test_facts['user_gecos'], "user_gecos value from UserFactCollector.collect() is empty"
    assert test_facts['user_dir'], "user_dir value from UserFactCollector.collect() is empty"
    assert test_facts['user_shell'], "user_shell value from UserFactCollector.collect() is empty"


# Generated at 2022-06-13 03:36:26.913726
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    fact_collector = UserFactCollector()
    fact_collector.collect()
    assert True


# Generated at 2022-06-13 03:36:29.346186
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    ufc = UserFactCollector()
    user_facts = ufc.collect()

# vim: expandtab:ts=4:sw=4

# Generated at 2022-06-13 03:36:37.939677
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    fact_collector = UserFactCollector()

    user_facts = fact_collector.collect()

    assert(user_facts['user_id'] != '')
    assert(user_facts['user_uid'] != '')
    assert(user_facts['user_gid'] != '')
    assert(user_facts['user_gecos'] != '')
    assert(user_facts['user_dir'] != '')
    assert(user_facts['user_shell'] != '')
    assert(user_facts['real_user_id'] != '')
    assert(user_facts['effective_user_id'] != '')
    assert(user_facts['real_group_id'] != '')
    assert(user_facts['effective_group_id'] != '')

# Generated at 2022-06-13 03:36:44.281756
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    collector = UserFactCollector()
    ansible_facts = collector.collect()
    assert ansible_facts['user_id'] == getpass.getuser()
    assert ansible_facts['real_user_id'] == os.getuid()
    assert ansible_facts['effective_user_id'] == os.geteuid()
    assert ansible_facts['real_group_id'] == os.getgid()
    assert ansible_facts['effective_group_id'] == os.getgid()

# Generated at 2022-06-13 03:36:46.434496
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    test_collector = UserFactCollector()
    test_result = test_collector.collect()
    assert test_result['user_id'] == 'root'

# Generated at 2022-06-13 03:36:51.358060
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_fact_collector = UserFactCollector()

    user_facts = user_fact_collector.collect()

    # name property
    assert user_fact_collector.name == 'user'

    # _fact_ids property
    assert user_fact_collector._fact_ids == set(['user_id', 'user_uid',
                                                 'user_gid', 'user_gecos',
                                                 'user_dir', 'user_shell',
                                                 'real_user_id',
                                                 'effective_user_id',
                                                 'effective_group_ids'])

    # user_id
    assert user_facts['user_id'] == getpass.getuser()

    # user_uid

# Generated at 2022-06-13 03:36:58.913779
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    d = {}
    ufc = UserFactCollector()
    ufc.collect(d)
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
    assert 'effective_group_ids' in d

# Generated at 2022-06-13 03:37:07.239629
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    #Check if method collect of class UserFactCollector is working
    user_collector = UserFactCollector()

    collected_facts = user_collector.collect(collected_facts=None)

    assert 'user_id' in collected_facts
    assert 'user_uid' in collected_facts
    assert 'user_gid' in collected_facts
    assert 'user_gecos' in collected_facts
    assert 'user_dir' in collected_facts
    assert 'user_shell' in collected_facts
    assert 'real_user_id' in collected_facts
    assert 'effective_user_id' in collected_facts

# Generated at 2022-06-13 03:37:18.288533
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # pylint: disable=undefined-variable
    # pylint: disable=global-variable-not-assigned
    global collected_facts  # collected_facts is used in BaseFactCollector
    global module  # module is used in BaseFactCollector
    module = None
    collected_facts = {'hostname': 'hostname'}

    # Now test the method with success
    collect_results = UserFactCollector.collect()

    assert collect_results['user_id']
    assert collect_results['user_uid']
    assert collect_results['user_gid']
    assert collect_results['user_gecos']
    assert collect_results['user_dir']
    assert collect_results['user_shell']
    assert collect_results['real_user_id']
    assert collect_results['effective_user_id']


# Generated at 2022-06-13 03:37:41.331049
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_fc = UserFactCollector(None)
    v = user_fc.collect()
    assert 'user_id' in v
    assert 'user_uid' in v
    assert 'user_gid' in v
    assert 'user_gecos' in v
    assert 'user_dir' in v
    assert 'user_shell' in v
    assert 'real_user_id' in v
    assert 'real_group_id' in v
    assert 'effective_user_id' in v
    assert 'effective_group_id' in v
    assert 'effective_group_ids' in v
    
if __name__ == '__main__':
    test_UserFactCollector_collect()

# Generated at 2022-06-13 03:37:50.594461
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_facts_collector = UserFactCollector()

    assert user_facts_collector.collect()['user_id'] == getpass.getuser()
    assert user_facts_collector.collect()['user_uid'] == pwd.getpwuid(os.getuid()).pw_uid
    assert user_facts_collector.collect()['user_gid'] == pwd.getpwuid(os.getuid()).pw_gid
    assert user_facts_collector.collect()['user_gecos'] == pwd.getpwuid(os.getuid()).pw_gecos
    assert user_facts_collector.collect()['user_dir'] == pwd.getpwuid(os.getuid()).pw_dir

# Generated at 2022-06-13 03:37:59.391273
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_facts = UserFactCollector().collect()

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

# Generated at 2022-06-13 03:38:07.159969
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():

    with patch('getpass.getuser') as mock_getuser:
        with patch('os.getuid') as mock_getuid:
            with patch('pwd.getpwnam') as mock_getpwnam:
                with patch('pwd.getpwuid') as mock_getpwuid:
                    with patch('os.getgid') as mock_getgid:
                        with patch('os.getegid') as mock_getegid:
                            with patch('os.geteuid') as mock_geteuid:
                                mock_getuser.return_value = 'user'
                                mock_getuid.return_value = 1
                                mock_getpwnam.return_value = [1,1,1,'gecos','dir','shell']

# Generated at 2022-06-13 03:38:12.731159
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():

    user_collector = UserFactCollector()

    result = user_collector.collect()
    assert result.get('user_id')
    assert result.get('user_uid')
    assert result.get('user_gid')
    assert result.get('user_gecos')
    assert result.get('user_dir')
    assert result.get('user_shell')
    assert result.get('real_user_id')
    assert result.get('effective_user_id')
    assert result.get('real_group_id')
    assert result.get('effective_group_id')

# Generated at 2022-06-13 03:38:15.870160
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    ufc = UserFactCollector()
    collected_facts = {}
    collected_facts = ufc.collect(collected_facts=collected_facts)
    assert isinstance(collected_facts, dict)

# Generated at 2022-06-13 03:38:26.248131
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_fact_collector = UserFactCollector()
    user_facts = user_fact_collector.collect()
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

# Generated at 2022-06-13 03:38:30.068929
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    ufc = UserFactCollector()
    ansible_facts = {}
    ansible_facts = ufc.collect(ansible_facts) 
    #we have to have all properties in ansible_facts
    assert len(ufc._fact_ids & set(ansible_facts)) == len(ufc._fact_ids)

# Generated at 2022-06-13 03:38:37.738697
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():

    # Set up mock of getpwnam
    def mock_getpwnam(username):
        if username == 'user_id':
            return pwd.struct_passwd(('user_id', '*', 123, 456, 'user_gecos', '/home/user_id', '/bin/user_shell'))
        else:
            raise KeyError

    # Set up mock of getpwuid
    def mock_getpwuid(uid):
        return pwd.struct_passwd(('user_id', '*', 123, 456, 'user_gecos', '/home/user_id', '/bin/user_shell'))

    # Set up mocks
    pwd.getpwnam = mock_getpwnam
    pwd.getpwuid = mock_getpwuid
    oldgeteuid

# Generated at 2022-06-13 03:38:42.324908
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    test_object = UserFactCollector()
    user_dict = test_object.collect()
    assert user_dict['effective_user_id'] == os.geteuid()
    assert user_dict['user_id'] == getpass.getuser()

# Generated at 2022-06-13 03:39:18.849681
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    #
    # unit test with mocked pwd.getpwuid.
    #
    import pwd
    from types import ModuleType
    from ansible.module_utils.facts.collector import UserFactCollector

    module_name = 'ansible.module_utils.facts.collector'
    getpwuid_return_values = [('a', 'b', 'uid', 'gid', 'gecos', 'home', '/bin/bash')]

    def mocked_getpwuid(arg):
        return getpwuid_return_values.pop()

    pwd_module_mock = ModuleType(module_name)
    pwd_module_mock.getpwuid = mocked_getpwuid
    pwd_module_mock.getpwnam = mocked_getpwuid

    user_fact_

# Generated at 2022-06-13 03:39:24.109516
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.collector.user import UserFactCollector

    collector = Collector()
    fact_collector = UserFactCollector()

    fact_collector.collect(None, collector)

    assert 'user' in collector.collector
    assert isinstance(collector.collector['user'], dict)

    assert 'user_id' in collector.collector['user']
    assert isinstance(collector.collector['user']['user_id'], str)

    assert 'user_uid' in collector.collector['user']
    assert isinstance(collector.collector['user']['user_uid'], int)

    assert 'user_gid' in collector.collector['user']

# Generated at 2022-06-13 03:39:30.756089
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_facts = UserFactCollector().collect()
    assert('user_id' in user_facts)
    assert('user_uid' in user_facts)
    assert('user_gid' in user_facts)
    assert('user_gecos' in user_facts)
    assert('user_dir' in user_facts)
    assert('user_shell' in user_facts)
    assert('real_user_id' in user_facts)
    assert('effective_user_id' in user_facts)
    assert('effective_group_ids' in user_facts)

# Generated at 2022-06-13 03:39:40.724275
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    """Unit test for method collect of class UserFactCollector"""

    # create a UserFactCollector instance
    fact_collector = UserFactCollector()

    # invoke method collect of the UserFactCollector instance and validate
    # the result

# Generated at 2022-06-13 03:39:44.945386
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # Set up mock class
    class Module(object):
        pass

    module = Module()
    module.params = {}

    collector = UserFactCollector()

    result = collector.collect(module=module)

    assert 'user_id' in result
    assert 'user_uid' in result
    assert 'user_gid' in result
    assert 'user_gecos' in result
    assert 'user_dir' in result
    assert 'user_shell' in result
    assert 'real_user_id' in result
    assert 'effective_user_id' in result
    assert 'real_group_id' in result
    assert 'effective_group_id' in result

# Generated at 2022-06-13 03:39:56.180056
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    import platform
    from ansible.module_utils.facts import collector
    user_fact_collector = UserFactCollector()
    user_fact_collector.collect()
    if platform.system() == 'Windows':
        assert user_fact_collector.name == None
        assert user_fact_collector._fact_ids == set()
        assert collector.FactsCollector._fact_collectors == []
    else:
        assert user_fact_collector.name == 'user'
        assert user_fact_collector._fact_ids == set(['user_id', 'user_uid', 'user_gid',
                                                     'user_gecos', 'user_dir', 'user_shell',
                                                     'real_user_id', 'effective_user_id',
                                                     'effective_group_ids'])

# Generated at 2022-06-13 03:39:58.062878
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    userfact = UserFactCollector()
    user_facts = userfact.collect()
    assert type(user_facts) is dict

# Generated at 2022-06-13 03:39:59.483246
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    fact_collector = UserFactCollector()
    fact_collector.collect()


# Generated at 2022-06-13 03:40:10.634111
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_collector = UserFactCollector()
    test_user_facts = user_collector.collect()
    assert test_user_facts['user_id'] == getpass.getuser()
    assert isinstance(test_user_facts['user_uid'], int)
    assert isinstance(test_user_facts['user_gid'], int)
    assert isinstance(test_user_facts['user_gecos'], str)
    assert isinstance(test_user_facts['user_dir'], str)
    assert isinstance(test_user_facts['user_shell'], str)
    assert isinstance(test_user_facts['real_user_id'], int)
    assert isinstance(test_user_facts['effective_user_id'], int)

# Generated at 2022-06-13 03:40:20.341999
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    from ansible.module_utils.facts.collectors.user import UserFactCollector
    collector = UserFactCollector()
    result = collector.collect()
    assert result['user_id'] == getpass.getuser()
    assert result['user_uid'] == pwd.getpwuid(os.getuid()).pw_uid
    assert result['user_gid'] == pwd.getpwuid(os.getuid()).pw_gid
    assert result['user_gecos'] == pwd.getpwuid(os.getuid()).pw_gecos
    assert result['user_dir'] == pwd.getpwuid(os.getuid()).pw_dir
    assert result['user_shell'] == pwd.getpwuid(os.getuid()).pw_shell

# Generated at 2022-06-13 03:41:21.471856
# Unit test for method collect of class UserFactCollector

# Generated at 2022-06-13 03:41:32.626728
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    ufc = UserFactCollector()
    ret = ufc.collect()

    assert(ret['user_id'] == getpass.getuser())
    assert(ret['user_uid'] == os.getuid())
    assert(ret['user_gid'] == os.getgid())
    assert(ret['user_dir'] == os.getcwd())
    assert(ret['user_shell'] == os.getenv('SHELL'))
    assert(ret['real_user_id'] == os.getuid())
    assert(ret['effective_user_id'] == os.getuid())
    assert(ret['real_group_id'] == os.getgid())
    assert(ret['effective_group_id'] == os.getgid())

# Generated at 2022-06-13 03:41:39.995240
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    print("Testing method collect of class UserFactCollector")

    # Testing uid and username
    user_fact_collector = UserFactCollector()
    user_facts = user_fact_collector.collect()
    assert user_facts['user_id'] == getpass.getuser()
    assert user_facts['user_uid'] == os.getuid()

    # Testing gid and username
    assert user_facts['user_gid'] == os.getgid()
    assert user_facts['effective_user_id'] == os.geteuid()

# Generated at 2022-06-13 03:41:46.032313
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    import doctest
    results = doctest.testmod(UserFactCollector)

    if results.failed == 0:
        print('SUCCESS: %s' % __file__)
    else:
        print('FAILURE: %s' % __file__)

if __name__ == '__main__':
    test_UserFactCollector_collect()

# Generated at 2022-06-13 03:41:55.174577
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
	observed = UserFactCollector().collect()
	assert observed['user_id'] is not None, 'user_id should not be empty'
	assert observed['user_uid'] is not None, 'user_uid should not be empty'
	assert observed['user_gid'] is not None, 'user_gid should not be empty'
	assert observed['user_gecos'] is not None, 'user_gecos should not be empty'
	assert observed['user_dir'] is not None, 'user_dir should not be empty'
	assert observed['user_shell'] is not None, 'user_shell should not be empty'
	assert observed['real_user_id'] is not None, 'real_user_id should not be empty'
	assert observed['effective_user_id'] is not None, 'effective_user_id should not be empty'

# Generated at 2022-06-13 03:41:59.784928
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_fact_collector = UserFactCollector()
    user_fact_collector.collect()
    print(user_fact_collector.collect())
    print(user_fact_collector._fact_ids)


# Generated at 2022-06-13 03:42:01.284610
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # Test collect(module=None, collected_facts=None)
    collector = UserFactCollector()
    assert collector.collect() is not None


# Generated at 2022-06-13 03:42:04.628894
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user = UserFactCollector()
    collected_facts = user.collect()
    assert type(collected_facts) is dict
    assert collected_facts['user_id'] == getpass.getuser()
    assert collected_facts['effective_user_id'] == os.geteuid()
    assert collected_facts['effective_group_id'] == os.getegid()

# Generated at 2022-06-13 03:42:14.724072
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    f = UserFactCollector()
    res = f.collect()
    # info to be printed
    print("")
    print("UserFacts:")
    print("  OS User:", res['user_id'])
    print("  OS User UID:", res['user_uid'])
    print("  OS User GID:", res['user_gid'])
    print("  OS User GECOS:", res['user_gecos'])
    print("  OS User Dir:", res['user_dir'])
    print("  OS User Shell:", res['user_shell'])
    print("  Effective User ID:", res['real_user_id'])
    print("  Effective User ID:", res['effective_user_id'])

# Generated at 2022-06-13 03:42:22.963327
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    """
    Tests UserFactCollector.collect function when called with
    username 'test'.
    """
    import pwd

    def getpwnam_test(name):
        test_pwent = pwd.struct_passwd(('test', # pw_name
                                        'x',    # pw_passwd
                                        1000,   # pw_uid
                                        1000,   # pw_gid
                                        '',     # pw_gecos
                                        '/tmp', # pw_dir
                                        '/bin/true')) # pw_shell
        return test_pwent

    pwd.getpwnam = getpwnam_test

    user_fc = UserFactCollector()
    user_facts = user_fc.collect()

    assert user_facts['user_id'] == 'test'
