

# Generated at 2022-06-13 03:33:28.337589
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_fact_collector = UserFactCollector()
    test_user_facts = user_fact_collector.collect()
    if len(test_user_facts) == 0:
        raise Exception("Failed to collect user facts")
    elif "user_id" not in test_user_facts:
        raise Exception("Failed to collect user facts")
    elif "user_uid" not in test_user_facts:
        raise Exception("Failed to collect user facts")
    elif "user_gid" not in test_user_facts:
        raise Exception("Failed to collect user facts")
    elif "user_gecos" not in test_user_facts:
        raise Exception("Failed to collect user facts")

# Generated at 2022-06-13 03:33:37.240400
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    userfact = UserFactCollector()
    userfacts = userfact.collect()

    assert userfacts is not None

    assert 'user_id' in userfacts
    assert 'user_uid' in userfacts
    assert 'user_gid' in userfacts
    assert 'user_gecos' in userfacts
    assert 'user_dir' in userfacts
    assert 'user_shell' in userfacts

    assert 'real_user_id' in userfacts
    assert 'effective_user_id' in userfacts
    assert 'real_group_id' in userfacts
    assert 'effective_group_id' in userfacts

    assert userfacts['user_id'] == getpass.getuser()
    assert userfacts['real_user_id'] == os.getuid()
    assert userfacts['effective_user_id'] == os.geteu

# Generated at 2022-06-13 03:33:40.699548
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    fact_collector = UserFactCollector()
    result = fact_collector.collect()
    for fact_id in fact_collector.fact_ids():
        assert(result.get(fact_id, None) != None)



# Generated at 2022-06-13 03:33:50.248454
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # Instantiate a TestUserFactCollector object
    test_user_fact_collector = UserFactCollector()

    # Call method collect() of TestUserFactCollector object
    user_facts = test_user_fact_collector.collect()

    # Assert default user_id returned by collect() of TestUserFactCollector object
    assert user_facts['user_id'] == getpass.getuser()

    # Assert user_uid returned by collect() of TestUserFactCollector object
    assert user_facts['user_uid'] == pwd.getpwuid(os.getuid()).pw_uid

    # Assert user_gid returned by collect() of TestUserFactCollector object
    assert user_facts['user_gid'] == pwd.getpwuid(os.getuid()).pw_gid

   

# Generated at 2022-06-13 03:33:55.836498
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    c = Collector(None)
    c.collect_facts()
    assert c.get_facts()['user_id'] == getpass.getuser()
    assert c.get_facts()['effective_user_id'] == os.geteuid()
    assert c.get_facts()['effective_group_ids'] == [os.getgid()]

# Generated at 2022-06-13 03:33:58.761936
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_fact_collector = UserFactCollector()
    collected_facts = user_fact_collector.collect(None)
    assert user_fact_collector._fact_ids <= collected_facts.keys()


# Generated at 2022-06-13 03:34:04.754719
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_facts = UserFactCollector().collect()
    assert user_facts['user_id']
    assert user_facts['user_uid']
    assert user_facts['user_gid']
    assert user_facts['user_gecos']
    assert user_facts['user_dir']
    assert user_facts['user_shell']
    assert user_facts['real_user_id']
    assert user_facts['effective_user_id']
    assert user_facts['real_group_id']
    assert user_facts['effective_group_id']

# Generated at 2022-06-13 03:34:11.501276
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user = UserFactCollector()
    user_facts = user.collect()
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
    assert user_facts['real_user_id'] == os.get

# Generated at 2022-06-13 03:34:17.822825
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    ufc = UserFactCollector()
    collected_facts = {'gather_subset': [ 'all' ]}
    user_facts = ufc.collect(collected_facts=collected_facts)
    assert user_facts['user_id'] == getpass.getuser()
    assert user_facts['user_uid'] == pwd.getpwnam(getpass.getuser()).pw_uid
    assert user_facts['user_gid'] == pwd.getpwnam(getpass.getuser()).pw_gid
    assert user_facts['user_gecos'] == pwd.getpwnam(getpass.getuser()).pw_gecos
    assert user_facts['user_dir'] == pwd.getpwnam(getpass.getuser()).pw_dir

# Generated at 2022-06-13 03:34:26.983295
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_fact_collector = UserFactCollector()
    collected_facts = {}
    expected_facts = {
        'user_id': 'root',
        'user_uid': 0,
        'user_gid': 0,
        'user_gecos': 'root',
        'user_dir': '/root',
        'user_shell': '/bin/bash',
        'real_user_id': 0,
        'effective_user_id': 0,
        'real_group_id': 0,
        'effective_group_id': 0
    }
    collected_facts = user_fact_collector.collect(None, collected_facts)
    collected_facts = dict((k, v) for k, v in collected_facts.items() if v is not None)
    assert collected_facts == expected_facts

# Generated at 2022-06-13 03:34:39.466200
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_factCollector = UserFactCollector()

    user_facts = user_factCollector.collect()

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

# Generated at 2022-06-13 03:34:41.034952
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    ufc = UserFactCollector()
    user_facts = ufc.collect()
    assert user_facts is not None

# Generated at 2022-06-13 03:34:47.880838
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_facts = {'effective_group_id': 1000,
                  'effective_user_id': 1000,
                  'real_group_id': 1000,
                  'real_user_id': 1000,
                  'user_dir': '/home/ansible',
                  'user_gid': 1000,
                  'user_gecos': 'None',
                  'user_id': 'ansible',
                  'user_shell': '/bin/bash',
                  'user_uid': 1000}

    user_run = UserFactCollector()
    # noinspection PyProtectedMember
    assert user_run._fact_ids == user_facts.keys()
    assert user_run.collect() == user_facts


if __name__ == '__main__':
    # Unit test
    test_UserFactCollector_collect()

# Generated at 2022-06-13 03:34:56.241034
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # Create instance of UserFactCollector
    user_fact_collector = UserFactCollector()
    outputs = user_fact_collector.collect()
    # Verify that user id is returned.
    assert outputs['user_id']
    # Verify that applied groups id is returned.
    assert outputs['effective_group_id']
    # Verify that real groups id is returned.
    assert outputs['real_group_id']
    # Verify that user id id returned.
    assert outputs['user_id']
    # Verify that real user id is returend.
    assert outputs['real_user_id']
    # Verify that effective user id is returned.
    assert outputs['effective_user_id']

# Generated at 2022-06-13 03:34:57.801310
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    import doctest
    print(doctest.testmod(verbose=True))


# Generated at 2022-06-13 03:35:04.396280
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    """
    Unit test of method collect of class UserFactCollector.
    """

    collector = UserFactCollector()
    # Test method when we are root
    assert os.geteuid() == 0
    facts = collector.collect()
    assert facts is not None
    assert facts['user_id'] == 'root'
    assert facts['user_uid'] == 0
    assert facts['user_gid'] == 0
    assert facts['user_gecos'] == 'root'
    assert facts['user_dir'] == '/root'
    assert facts['user_shell'] == '/bin/bash'
    assert facts['real_user_id'] == 0
    assert facts['real_group_id'] == 0
    assert facts['effective_user_id'] == 0
    assert facts['effective_group_id'] == 0

# Generated at 2022-06-13 03:35:07.375267
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_fact_collector = UserFactCollector()
    user_fact_collector.collect()

# Generated at 2022-06-13 03:35:15.558961
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

# Generated at 2022-06-13 03:35:21.294024
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    UserFactCollector = __import__('ansible.module_utils.facts.user.user_fact_collector', globals(), locals(), ['UserFactCollector'], 0).UserFactCollector

    user_fact_collector = UserFactCollector()

    user_facts = user_fact_collector.collect()

    assert(type(user_facts) == dict)


# Generated at 2022-06-13 03:35:29.900934
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # pylint: disable=protected-access
    user_facts = UserFactCollector().collect()
    assert user_facts['user_id']
    assert user_facts['user_uid']
    assert user_facts['user_gid']
    assert user_facts['user_gecos']
    assert user_facts['user_dir']
    assert user_facts['user_shell']
    assert user_facts['real_user_id']
    assert user_facts['effective_user_id']
    assert user_facts['real_group_id']
    assert user_facts['effective_group_id']
    assert type(user_facts['effective_group_ids']) is list
    assert len(user_facts['effective_group_ids']) > 0

# Generated at 2022-06-13 03:35:45.612821
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():

    import pwd

    from ansible_collections.ansible.community.plugins.module_utils.facts.collector import BaseFactCollector, UserFactCollector
    from ansible_collections.ansible.community.plugins.module_utils.facts.collectors import get_collector_instance

    # Fake user name and user id.
    fake_user_name = 'fake_user_name'
    fake_user_id = 1

    # Class create by UserFactCollector
    class FakeUserFactCollector(UserFactCollector):
        def __init__(self, *args, **kwargs):
            self._user_name = fake_user_name
            super(FakeUserFactCollector, self).__init__(*args, **kwargs)


# Generated at 2022-06-13 03:35:53.917933
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    collector = UserFactCollector()
    # Testing the collect method of UserFactCollector
    collected_facts = collector.collect()
    expected_facts = {'effective_group_id': os.getgid(),
                      'effective_user_id': os.geteuid(),
                      'real_group_id': os.getgid(),
                      'real_user_id': os.getuid()}
    for key, value in expected_facts.items():
        assert collected_facts[key] == value

# Generated at 2022-06-13 03:36:02.312881
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():

    FixtureClass = type('FixtureClass', (object,))
    Fixture = FixtureClass()
    Fixture.user_id = 'test_user_id'
    Fixture.pwent = pwd.struct_passwd((
        b'test_user', b'test_passwd', 1, 2,
        b'test_fullname', b'/home/test_user',
        b'/bin/test_shell'))
    Fixture.user_uid = 1
    Fixture.user_gid = 2
    Fixture.user_gecos = 'test_fullname'
    Fixture.user_dir = '/home/test_user'
    Fixture.user_shell = '/bin/test_shell'
    Fixture.real_user_id = 1
    Fixture.effective_user_id = 2
    F

# Generated at 2022-06-13 03:36:14.069787
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_collector = UserFactCollector()
    collected_facts = {}
    collected_facts = user_collector.collect(collected_facts=collected_facts)
    dict_facts = dict(collected_facts)
    assert dict_facts['ansible_facts']['user_id'] == getpass.getuser()
    pwent = pwd.getpwnam(getpass.getuser())
    assert dict_facts['ansible_facts']['user_uid'] == pwent.pw_uid
    assert dict_facts['ansible_facts']['user_gid'] == pwent.pw_gid
    assert dict_facts['ansible_facts']['user_gecos'] == pwent.pw_gecos

# Generated at 2022-06-13 03:36:19.328094
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    """Unit test for UserFactCollector.collect()"""
    user_facts_collector = UserFactCollector()
    user_facts = user_facts_collector.collect()
    print(user_facts)
    print(user_facts_collector.fact_ids())

if __name__ == '__main__':
    test_UserFactCollector_collect()

# Generated at 2022-06-13 03:36:28.820062
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_facts = UserFactCollector()

    assert 'user_id' in user_facts.collect()
    assert 'user_uid' in user_facts.collect()
    assert 'user_gid' in user_facts.collect()
    assert 'user_gecos' in user_facts.collect()
    assert 'user_dir' in user_facts.collect()
    assert 'user_shell' in user_facts.collect()
    assert 'real_user_id' in user_facts.collect()
    assert 'effective_user_id' in user_facts.collect()
    assert 'real_group_id' in user_facts.collect()
    assert 'effective_group_id' in user_facts.collect()

# Generated at 2022-06-13 03:36:35.048310
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # Test with low-uid user (nobody)
    ufc = UserFactCollector()
    results = ufc.collect()
    assert results['user_uid'] == 65534
    assert results['user_id'] == 'nobody'
    assert results['real_user_id'] == 65534
    assert results['effective_user_id'] == 65534
    assert results['real_group_id'] == 65534
    assert results['effective_group_id'] == 65534

# Generated at 2022-06-13 03:36:41.069384
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    test = UserFactCollector()
    res = test.collect()

    assert('effective_group_ids' in res)
    assert('user_id' in res)
    assert('user_uid' in res)
    assert('user_gecos' in res)
    assert('user_dir' in res)
    assert('user_shell' in res)
    assert('real_user_id' in res)
    assert('effective_user_id' in res)

# Generated at 2022-06-13 03:36:43.609866
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_facts_collector = UserFactCollector()
    user_facts = user_facts_collector.collect()
    assert type(user_facts) is dict
    assert len(user_facts) > 0

# Generated at 2022-06-13 03:36:44.409080
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    pass

# Generated at 2022-06-13 03:36:58.339105
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():

    # Initializing UserFactCollector object
    userf = UserFactCollector()

    # Collecting all the user facts
    data = userf.collect()

    # Asserting collected facts
    assert data['user_id'] == getpass.getuser()
    assert data['user_uid'] == pwd.getpwnam(getpass.getuser()).pw_uid
    assert data['user_gid'] == pwd.getpwnam(getpass.getuser()).pw_gid
    assert data['user_gecos'] == pwd.getpwnam(getpass.getuser()).pw_gecos
    assert data['user_dir'] == pwd.getpwnam(getpass.getuser()).pw_dir

# Generated at 2022-06-13 03:37:09.032493
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    ###################################################################
    # Mock the dependencies for test_UserFactCollector_collect.
    ###################################################################
    import os
    import getpass
    import pwd

    # create the mock file system
    from ansible_collections.ansible.community.plugins.module_utils.facts import user

    class MockUser:
        def getuid():
            return 1707
        def geteuid():
            return 1707
        def getgid():
            return 500
        def getegid():
            return 500
        def getpwuid(uid):
            return pwd.struct_passwd(('eric', 'x', 1707, 500, 'Eric Kavanagh', '/home/eric', '/bin/bash'))

# Generated at 2022-06-13 03:37:13.092262
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    class TestModule(object):
        def __init__(self):
            self.params = {}

    module = TestModule()
    fact_collector = UserFactCollector()

    fact_collector.collect(module=module)

# Generated at 2022-06-13 03:37:22.493435
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_facts = UserFactCollector().collect()
    assert isinstance(user_facts['user_id'], str)
    assert isinstance(user_facts['user_uid'], int)
    assert isinstance(user_facts['user_gid'], int)
    assert isinstance(user_facts['user_gecos'], str)
    assert isinstance(user_facts['user_dir'], str)
    assert isinstance(user_facts['user_shell'], str)
    assert isinstance(user_facts['real_user_id'], int)
    assert isinstance(user_facts['effective_user_id'], int)
    assert isinstance(user_facts['real_group_id'], int)
    assert isinstance(user_facts['effective_group_id'], int)

# Generated at 2022-06-13 03:37:27.046286
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_fact_collector_class = UserFactCollector()
    user_fact_collector = user_fact_collector_class.collect()
    print(user_fact_collector)


# Generated at 2022-06-13 03:37:30.454972
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    from ansible.module_utils.facts import user
    from ansible.module_utils import facts

    c = user.UserFactCollector()
    assert c.collect() == facts.user.collect()

# Generated at 2022-06-13 03:37:41.776555
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    facts_module = __import__('ansible.module_utils.facts.system.user', fromlist=['UserFactCollector'])

    user_facts = facts_module.UserFactCollector()

    results = user_facts.collect()
    assert results.has_key('user_id')
    assert results['user_id'] == getpass.getuser()
    assert results.has_key('user_uid')
    assert results.has_key('user_gid')
    assert results.has_key('user_gecos')
    assert results.has_key('user_dir')
    assert results.has_key('user_shell')
    assert results.has_key('real_user_id')
    assert results['real_user_id'] == os.getuid()

# Generated at 2022-06-13 03:37:46.960108
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_fact_collector = UserFactCollector()
    user_facts = user_fact_collector.collect()

    assert user_facts['user_id'] == getpass.getuser()
    assert user_facts['user_gecos'] is not None
    assert user_facts['user_shell'] is not None


# Generated at 2022-06-13 03:37:50.791273
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    """Test collection of facts related to user"""
    user_fact_collector = UserFactCollector()
    facts = user_fact_collector.collect()
    expected_keys = user_fact_collector._fact_ids
    assert set(facts.keys()) == expected_keys

# Generated at 2022-06-13 03:38:01.320742
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    """Unit test for method collect of class UserFactCollector"""

    # When the user is root, we expect to be able to collect all facts
    def set_getpwuid_mock_data(getpwuid):
        class PwUid(object):
            """Mock class for pwent"""
            pw_uid = 0
            pw_gid = 0
            pw_gecos = 'user_gecos'
            pw_dir = 'user_dir'
            pw_shell = 'user_shell'
        getpwuid.return_value = PwUid()

    def set_geteuid_mock_data(geteuid):
        geteuid.return_value = 0


# Generated at 2022-06-13 03:38:15.049203
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # Initialize a UserFactCollector instance
    user_fact_collector = UserFactCollector()

    # Collect facts
    collected_facts = user_fact_collector.collect()

    # Check the collected facts

# Generated at 2022-06-13 03:38:23.557542
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user = UserFactCollector()

    facts = user.collect()
    assert isinstance(facts, dict)
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

# Generated at 2022-06-13 03:38:28.826837
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_c = UserFactCollector()

    user_facts = user_c.collect()

    assert user_facts['user_id'] == getpass.getuser()
    assert user_facts['user_uid'] == pwd.getpwnam(getpass.getuser()).pw_uid
    assert user_facts['user_gid'] == pwd.getpwnam(getpass.getuser()).pw_gid
    assert user_facts['user_gecos'] == pwd.getpwnam(getpass.getuser()).pw_gecos
    assert user_facts['user_dir'] == pwd.getpwnam(getpass.getuser()).pw_dir
    assert user_facts['user_shell'] == pwd.getpwnam(getpass.getuser()).pw_shell

# Generated at 2022-06-13 03:38:35.590885
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    test_data = {'user_id': 'root', 'user_uid': 0, 'user_gid': 0, 'user_gecos': 'root',
                 'user_home': '/root', 'user_shell': '/bin/bash',
                 'real_user_id': 0, 'effective_user_id': 0, 'real_group_id': 0,
                 'effective_group_id': 0}
    user_fact_collector = UserFactCollector()
    user_facts = user_fact_collector.collect()
    assert user_facts == test_data

# Generated at 2022-06-13 03:38:47.317939
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    import pwd
    fact_collector = UserFactCollector()
    collected_facts = fact_collector.collect()
    assert collected_facts['user_id'] == getpass.getuser()
    pwent = pwd.getpwnam(getpass.getuser())
    assert collected_facts['user_uid'] == pwent.pw_uid
    assert collected_facts['user_gid'] == pwent.pw_gid
    assert collected_facts['user_gecos'] == pwent.pw_gecos
    assert collected_facts['user_dir'] == pwent.pw_dir
    assert collected_facts['user_shell'] == pwent.pw_shell
    assert collected_facts['real_user_id'] == os.getuid()
    assert collected_facts['effective_user_id'] == os

# Generated at 2022-06-13 03:38:58.092797
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    module = None
    collected_facts = None
    collector = UserFactCollector()
    output = collector.collect(module, collected_facts)

    assert type(output) is dict
    assert 'user_id' in output
    assert 'user_uid' in output
    assert 'user_gid' in output
    assert 'user_dir' in output
    assert 'user_shell' in output
    assert 'real_user_id' in output
    assert 'effective_user_id' in output
    assert 'real_group_id' in output
    assert 'effective_group_id' in output
    assert output['user_id'] == getpass.getuser()
    assert output['user_uid'] == pwd.getpwnam(getpass.getuser()).pw_uid

# Generated at 2022-06-13 03:39:01.264058
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_facts = UserFactCollector().collect()
    assert user_facts is not None
    assert isinstance(user_facts, dict)
    for fact in UserFactCollector._fact_ids:
        assert fact in user_facts
    #assert 'real_group_id' in user_facts

# Generated at 2022-06-13 03:39:04.684951
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    test_instance = UserFactCollector()
    test_data = test_instance.collect()
    # Test for the user_id fact
    assert 'user_id' in test_data


# Generated at 2022-06-13 03:39:15.841051
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    uid = os.getuid()
    pwent = pwd.getpwuid(uid)
    egid = os.getegid()
    gids = os.getgroups() + [egid]
    user_facts = UserFactCollector().collect()
    assert user_facts['user_id'] == pwent.pw_name
    assert user_facts['user_uid'] == uid
    assert user_facts['user_gid'] == pwent.pw_gid
    assert user_facts['user_gecos'] == pwent.pw_gecos
    assert user_facts['user_dir'] == pwent.pw_dir
    assert user_facts['user_shell'] == pwent.pw_shell
    assert user_facts['real_user_id'] == uid

# Generated at 2022-06-13 03:39:16.478215
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    pass

# Generated at 2022-06-13 03:39:32.338465
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    os.environ['USER'] = "my_user"
    UserFactCollector().collect()
    assert os.getenv('USER') == 'my_user'

# Generated at 2022-06-13 03:39:37.358354
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_fact_collector = UserFactCollector()
    ansible_facts = user_fact_collector.collect()
    # If a user has a User Fact defined in the set _fact_ids
    # then the user fact is collected
    assert 'user_id' in ansible_facts
    assert 'user_uid' in ansible_facts

# Generated at 2022-06-13 03:39:43.958875
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_facts = UserFactCollector().collect()
    assert isinstance(user_facts, dict)
    assert user_facts['user_id'] != None
    assert user_facts['user_uid'] != None
    assert user_facts['user_gid'] != None
    assert user_facts['user_gecos'] != None
    assert user_facts['user_dir'] != None
    assert user_facts['user_shell'] != None
    assert user_facts['real_user_id'] != None
    assert user_facts['effective_user_id'] != None
    assert user_facts['real_group_id'] != None
    assert user_facts['effective_group_id'] != None

# Generated at 2022-06-13 03:39:48.618475
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    import sys

    # Create a UserFactCollector object
    user_collector = UserFactCollector()

    # Get the facts from the collector object
    user_facts = user_collector.collect()

    # Check the collected facts
    if sys.platform.lower() == "win32":
        assert(user_facts['user_id'] == getpass.getuser())
        assert(user_facts['user_uid'] == 0)
        assert(user_facts['user_gid'] == 0)
        assert(user_facts['user_gecos'] == "")
        assert(user_facts['user_dir'] == os.path.expanduser("~"))
        assert(user_facts['user_shell'] == "")
        assert(user_facts['real_user_id'] == os.getuid())

# Generated at 2022-06-13 03:39:58.380296
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    fact_collection = UserFactCollector()
    collected_facts = fact_collection.collect()

    # assert user_id
    assert collected_facts['user_id'] == getpass.getuser()

    # assert user_uid
    assert collected_facts['user_uid'] == pwd.getpwuid(os.getuid()).pw_uid

    # assert user_gid
    assert collected_facts['user_gid'] == pwd.getpwuid(os.getuid()).pw_gid

    # assert user_gecos
    assert collected_facts['user_gecos'] == pwd.getpwuid(os.getuid()).pw_gecos

    # assert user_dir
    assert collected_facts['user_dir'] == pwd.getpwuid(os.getuid()).pw

# Generated at 2022-06-13 03:40:04.240915
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    fact = UserFactCollector()
    f = fact.collect(None, None)
    assert f['user_id'] == getpass.getuser()
    assert f['user_uid'] == pwd.getpwnam(getpass.getuser()).pw_uid
    assert f['user_gid'] == pwd.getpwnam(getpass.getuser()).pw_gid
    assert f['user_gecos'] == pwd.getpwnam(getpass.getuser()).pw_gecos
    assert f['user_dir'] == pwd.getpwnam(getpass.getuser()).pw_dir
    assert f['user_shell'] == pwd.getpwnam(getpass.getuser()).pw_shell

# Generated at 2022-06-13 03:40:12.446202
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    from ansible.module_utils.facts.collector import FactsCollector

    facts_collector = FactsCollector()
    for fact in facts_collector.get_facts():
        fact_collector = fact.get('ansible_facts')
        fact_dict = fact.get('ansible_facts').get('user')
        user_id = fact_dict.get('user_id')
        user_uid = fact_dict.get('user_uid')
        user_gid = fact_dict.get('user_gid')
        user_gecos = fact_dict.get('user_gecos')
        user_dir = fact_dict.get('user_dir')
        user_shell = fact_dict.get('user_shell')
        real_user_id = fact_dict.get('real_user_id')
       

# Generated at 2022-06-13 03:40:14.704116
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    collector = UserFactCollector()
    assert collector.collect(None, None) is not None

# Generated at 2022-06-13 03:40:16.302385
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    fact_collector = UserFactCollector()
    fact_collector.collect()

# Generated at 2022-06-13 03:40:24.439466
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    fact_collector = UserFactCollector()
    fact_collector._module = type('', (object,), {})
    fact_collector._module.params = dict()
    fact_collector._module._debug = False
    collected_facts = dict()


# Generated at 2022-06-13 03:40:58.381457
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    from ansible.module_utils.facts.collector import FactCollector
    fact_collector = FactCollector(collectors=['user'], module=None)
    collected_facts = fact_collector.collect()
    assert 'user_id' in collected_facts
    assert 'user_uid' in collected_facts
    assert 'user_gid' in collected_facts
    assert 'user_shell' in collected_facts
    assert 'user_dir' in collected_facts
    assert 'user_gecos' in collected_facts
    assert 'real_user_id' in collected_facts
    assert 'effective_user_id' in collected_facts
    assert 'effective_group_ids' in collected_facts

# Generated at 2022-06-13 03:41:05.139271
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    import pwd

    cf = {}

    # create the instance under test
    ufc = UserFactCollector(cf)

    # run the method and assert the result is correct
    result = ufc.collect(cf)

# Generated at 2022-06-13 03:41:07.314667
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_fact_collector = UserFactCollector()
    response = user_fact_collector.collect(None)

    assert response['user_id'] == getpass.getuser()
    assert response['user_uid'] != 0
    assert response['user_gid'] != 0
    assert response['user_dir'] is not None
    assert response['user_shell'] is not None

# Generated at 2022-06-13 03:41:16.578494
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    try:
        uid_name = getpass.getuser()
    except Exception:
        uid_name = pwd.getpwuid(os.getuid())[0]
    uid_number = pwd.getpwnam(uid_name)[2]
    gid_number = pwd.getpwnam(uid_name)[3]
    gecos = pwd.getpwnam(uid_name)[4]
    homedir = pwd.getpwnam(uid_name)[5]
    usershell = pwd.getpwnam(uid_name)[6]
    test_UserFactCollector = UserFactCollector()
    user_facts = test_UserFactCollector.collect()
    assert(user_facts['user_id'] == uid_name)

# Generated at 2022-06-13 03:41:27.589259
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    ustring = ':'.join([str(os.getuid()), str(os.getgid())])

    if os.geteuid() != os.getuid():
        ustring += ':' + str(os.geteuid())

    for gid in os.getgroups():
        if gid != os.getgid():
            ustring += ',' + str(gid)

    u = UserFactCollector()

# Generated at 2022-06-13 03:41:35.726892
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():

    expected_values = {'user_id': 'test_user',
                      'user_uid': 1000,
                      'user_gid': 1000,
                      'user_gecos': 'Test User,,,',
                      'user_dir': '/home/test_user',
                      'user_shell': '/bin/bash',
                      'real_user_id': 1000,
                      'effective_user_id': 1000,
                      'real_group_id': 1000,
                      'effective_group_id': 1000,
                      'effective_group_ids': [1000, 0]}

    user_facts = UserFactCollector()
    collected_facts = user_facts.collect()

    for key, value in expected_values.items():
        assert collected_facts[key] == value


# Generated at 2022-06-13 03:41:42.422156
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    from ansible.module_utils.facts import FactCollector
    user_fact_collector = UserFactCollector()
    user_collector_facts = user_fact_collector.collect()

    expected_keys = [u'user_id', u'user_gid', u'user_gecos', u'user_shell',
                     u'effective_user_id', u'user_dir', u'user_uid', u'real_user_id']

    assert isinstance(user_collector_facts, dict)
    assert set(user_collector_facts.keys()) == set(expected_keys)

# Generated at 2022-06-13 03:41:48.196176
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_fact_collector = UserFactCollector()
    facts = user_fact_collector.collect()
    assert facts['user_id'] == getpass.getuser()
    assert facts['real_user_id'] == os.getuid()
    assert facts['effective_user_id'] == os.geteuid()
    assert facts['real_group_id'] == os.getgid()
    assert facts['effective_group_id'] == os.getgid()

# Generated at 2022-06-13 03:41:55.658110
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

# vim: set expandtab:ts=4:sw=4:

# Generated at 2022-06-13 03:41:57.359774
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    ufc = UserFactCollector()
    user_facts = ufc.collect(collected_facts=None)
    assert user_facts is not None


# Generated at 2022-06-13 03:43:08.232358
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():

    tf = UserFactCollector()

    # test user_id and user_uid
    assert tf.collect()['user_id'] == getpass.getuser()
    assert tf.collect()['user_uid'] == pwd.getpwnam(getpass.getuser()).pw_uid

    # test user_gid and user_gecos
    assert tf.collect()['user_gid'] == pwd.getpwnam(getpass.getuser()).pw_gid
    assert tf.collect()['user_gecos'] == pwd.getpwnam(getpass.getuser()).pw_gecos

    # test gids
    assert tf.collect()['real_group_id'] == os.getgid()
    assert tf.collect()['effective_group_id'] == os.getegid()

# Generated at 2022-06-13 03:43:09.679475
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_fact_collector_obj = UserFactCollector()
    user_fact_collector_obj.collect()

# Generated at 2022-06-13 03:43:20.439238
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():

    user_uid = os.getuid()
    user_gid = os.getgid()
    user = getpass.getuser()
    user_dir = os.path.expanduser("~")

    ufc = UserFactCollector()
    facts = ufc.collect()

    assert facts['user_id'] == user
    assert facts['user_uid'] == user_uid
    assert facts['user_gid'] == user_gid
    assert facts['user_dir'] == user_dir
    assert facts['real_user_id'] == user_uid
    assert facts['effective_user_id'] == user_uid
    assert facts['real_group_id'] == user_gid
    assert facts['effective_group_id'] == user_gid