

# Generated at 2022-06-13 03:33:28.377552
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_test_collector = UserFactCollector()
    facts_collection = user_test_collector.collect()
    assert facts_collection["user_id"] == getpass.getuser()
    assert facts_collection["user_uid"] == pwd.getpwuid(os.getuid()).pw_uid
    assert facts_collection["user_gid"] == pwd.getpwuid(os.getuid()).pw_gid
    assert facts_collection["user_gecos"] == pwd.getpwuid(os.getuid()).pw_gecos
    assert facts_collection["user_dir"] == pwd.getpwuid(os.getuid()).pw_dir
    assert facts_collection["user_shell"] == pwd.getpwuid(os.getuid()).pw_

# Generated at 2022-06-13 03:33:37.274455
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    fact_collector = UserFactCollector()
    user_facts = fact_collector.collect()
    assert set(user_facts.keys()) == fact_collector._fact_ids
    assert user_facts['user_id'] == getpass.getuser()

    assert type(user_facts['user_id']) is str
    assert type(user_facts['user_uid']) is int
    assert type(user_facts['user_gid']) is int
    assert type(user_facts['user_gecos']) is str
    assert type(user_facts['user_dir']) is str
    assert type(user_facts['user_shell']) is str
    assert type(user_facts['real_user_id']) is int
    assert type(user_facts['effective_user_id']) is int

# Generated at 2022-06-13 03:33:43.025064
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    '''
    Test collect() method of class UserFactCollector
    '''
    user_collector = UserFactCollector()
    module = {}
    collected_facts = {}
    user_facts = user_collector.collect(module)
    assert user_facts == user_collector.collect(module, collected_facts)
    assert 'user_id' in user_facts
    assert user_facts['user_id'] == getpass.getuser()

# Generated at 2022-06-13 03:33:53.050614
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_id = 'test_user'
    real_user_id = 'test_user'
    effective_user_id = 'test_user'
    real_group_id = 'test_group'
    effective_group_id = 'test_group'

    user_facts = {}

    user_facts['user_id'] = user_id
    user_facts['user_uid'] = 0
    user_facts['user_gid'] = 0
    user_facts['user_gecos'] = ''
    user_facts['user_dir'] = ''
    user_facts['user_shell'] = ''
    user_facts['real_user_id'] = real_user_id
    user_facts['effective_user_id'] = effective_user_id
    user_facts['real_group_id'] = real_group_id

# Generated at 2022-06-13 03:34:01.615071
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    """
    unit test for facter
    """
    ufc = UserFactCollector()
    test_facts = ufc.collect()

    assert test_facts['user_id'] == getpass.getuser()
    assert test_facts['user_uid'] == pwd.getpwuid(os.getuid()).pw_uid
    assert test_facts['user_gid'] == pwd.getpwuid(os.getuid()).pw_gid
    assert test_facts['user_gecos'] == pwd.getpwuid(os.getuid()).pw_gecos
    assert test_facts['user_dir'] == pwd.getpwuid(os.getuid()).pw_dir

# Generated at 2022-06-13 03:34:04.823124
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_facts = UserFactCollector().collect()

    print(user_facts)

if __name__ == '__main__':
    test_UserFactCollector_collect()

# Generated at 2022-06-13 03:34:06.204120
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_fact_collector = UserFactCollector()
    user_fact_collector.collect()


# Generated at 2022-06-13 03:34:14.009450
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_fact_collector = UserFactCollector()
    user_facts_dict = user_fact_collector.collect()
    assert user_facts_dict['user_id'] == getpass.getuser()
    assert user_facts_dict['real_user_id'] == os.getuid()
    assert user_facts_dict['effective_user_id'] == os.geteuid()
    assert user_facts_dict['real_group_id'] == os.getgid()
    assert user_facts_dict['effective_group_id'] == os.getgid()

# Generated at 2022-06-13 03:34:25.293030
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    from ansible.module_utils.facts.collector import FactsCollector

    def FakeModule(ansible_facts):
        return None

    def FakeCollector(module):
        return { "test_fact": "test_value" }

    user_collector = UserFactCollector()

# Generated at 2022-06-13 03:34:35.348926
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user = UserFactCollector()
    collected_facts = user.collect()

    assert collected_facts['user_id'] == getpass.getuser()
    assert collected_facts['user_uid'] == pwd.getpwuid(os.getuid()).pw_uid
    assert collected_facts['user_gid'] == pwd.getpwuid(os.getuid()).pw_gid
    assert collected_facts['user_gecos'] == pwd.getpwuid(os.getuid()).pw_gecos
    assert collected_facts['user_dir'] == pwd.getpwuid(os.getuid()).pw_dir
    assert collected_facts['user_shell'] == pwd.getpwuid(os.getuid()).pw_shell

# Generated at 2022-06-13 03:34:40.582354
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user = UserFactCollector()
    assert user.collect()['effective_user_id'] == os.geteuid()

# Generated at 2022-06-13 03:34:44.515371
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_collector = UserFactCollector()
    user_facts = user_collector.collect()
    assert isinstance(user_facts, dict)
    # At least we need user_id and user_uid to be string and int
    assert isinstance(user_facts['user_id'], str)
    assert isinstance(user_facts['user_uid'], int)

# Generated at 2022-06-13 03:34:44.976385
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    pass

# Generated at 2022-06-13 03:34:52.790800
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    """
    test the UserFactCollector collect method
    """
    user_fact = UserFactCollector()
    result = user_fact.collect()
    assert result['user_dir'] is not None
    assert result['user_gid'] is not None
    assert result['user_gecos'] is not None
    assert result['user_id'] is not None
    assert result['user_shell'] is not None
    assert result['user_uid'] is not None
    assert result['real_user_id'] is not None
    assert result['effective_user_id'] is not None
    assert result['effective_group_ids'] is not None
    assert result['real_group_id'] is not None

# Generated at 2022-06-13 03:35:01.278111
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    ufc = UserFactCollector()
    assert isinstance(ufc, BaseFactCollector)
    assert ufc.name == 'user'
    assert ufc._fact_ids == \
        set(['user_id', 'user_uid', 'user_gid',
             'user_gecos', 'user_dir', 'user_shell',
             'real_user_id', 'effective_user_id',
             'effective_group_ids'])
    user_facts = ufc.collect()
    assert isinstance(user_facts, dict)
    assert 'user_id' in user_facts
    assert user_facts['user_id']
    assert 'user_uid' in user_facts
    assert user_facts['user_uid']
    assert 'user_gid' in user_facts

# Generated at 2022-06-13 03:35:10.269143
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_facts = {
        'user_id': 'test_user',
        'user_uid': 1,
        'user_gid': 2,
        'user_gecos': 'Test User',
        'user_dir': '/home/test_user',
        'user_shell': '/bin/bash',
        'real_user_id': 1,
        'effective_user_id': 1,
        'real_group_id': 2,
        'effective_group_id': 2,
    }
    ufc = UserFactCollector()
    assert ufc.collect() == user_facts

# Generated at 2022-06-13 03:35:21.447555
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # mock
    import os

    class Mock_os(object):
        @staticmethod
        def getuid():
            return 1000

        @staticmethod
        def geteuid():
            return 1000

        @staticmethod
        def getgid():
            return 1000

    os_mock = Mock_os()

    # Act
    fact = UserFactCollector(module=None, collected_facts={})
    result = fact.collect(module=None, collected_facts={})

    # Asserts
    assert result['user_uid'] == os_mock.getuid()
    assert result['user_gid'] == os_mock.getgid()
    assert result['user_id'] == 'root'
    assert result['user_shell'] == '/bin/bash'
    assert result['real_user_id'] == os_

# Generated at 2022-06-13 03:35:25.667886
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():

    user_collector = UserFactCollector()

    # Collect facts.
    user_facts = user_collector.collect()

    # Verify facts.
    assert type(user_facts) is dict
    for fact_id in user_collector._fact_ids:
        assert fact_id in user_facts

# Generated at 2022-06-13 03:35:26.617685
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    assert UserFactCollector().collect() is not None

# Generated at 2022-06-13 03:35:33.579226
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    """Unit test for method collect of class UserFactCollector"""
    user_fact_collector = UserFactCollector()
    user_facts = user_fact_collector.collect()
    assert user_facts['user_id'] == getpass.getuser()
    assert user_facts['user_uid'] == pwd.getpwuid(os.getuid()).pw_uid
    assert user_facts['user_gid'] == pwd.getpwuid(os.getuid()).pw_gid
    assert user_facts['user_gecos'] == pwd.getpwuid(os.getuid()).pw_gecos
    assert user_facts['user_dir'] == pwd.getpwuid(os.getuid()).pw_dir
    assert user_facts['user_shell'] == pwd

# Generated at 2022-06-13 03:35:49.517844
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    collector = UserFactCollector()

    def do_test(name, expected_values=None, module_arg=None, collected_facts=None):
        user_facts = collector.collect(module_arg, collected_facts)

        if expected_values is None:
            expected_values = {}

        for item in expected_values:
            if expected_values[item] is None:
                assert item not in user_facts
            else:
                assert user_facts[item] == expected_values[item]

    # Just check that user_facts['user_id'] is set
    do_test('user_id')

    # Just check that user_facts['user_id'] is set
    do_test('user_id')

    # Check that user_facts[id] is unset for an invalid user

# Generated at 2022-06-13 03:36:00.079283
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    collector = UserFactCollector()
    user_facts = collector.collect()

    assert 'user_id' in user_facts
    assert 'user_uid' in user_facts
    assert 'user_gid' in user_facts
    assert 'user_gecos' in user_facts
    assert 'user_dir' in user_facts
    assert 'user_shell' in user_facts
    assert 'real_user_id' in user_facts
    assert 'effective_user_id' in user_facts
    assert 'effective_group_ids' in user_facts

    assert user_facts['user_id'] == getpass.getuser()
    assert isinstance(user_facts['user_uid'], int)
    assert isinstance(user_facts['user_gid'], int)

# Generated at 2022-06-13 03:36:11.255182
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    """
    Test for return value of method collect of class UserFactCollector
    """
    user_fact_collector = UserFactCollector()
    collected_facts = {}
    
    collected_facts = user_fact_collector.collect()
    assert type(collected_facts['user_id']) is str
    assert type(collected_facts['user_uid']) is int
    assert type(collected_facts['user_gid']) is int
    assert type(collected_facts['user_gecos']) is str
    assert type(collected_facts['user_dir']) is str
    assert type(collected_facts['user_shell']) is str
    assert type(collected_facts['real_user_id']) is int

# Generated at 2022-06-13 03:36:20.206927
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_facts_collector = UserFactCollector()

    facts = user_facts_collector.collect()

    assert facts == {'user_id': getpass.getuser(),
                     'user_uid': os.getuid(),
                     'user_gid': os.getgid(),
                     'user_gecos': None,
                     'user_dir': None,
                     'user_shell': None,
                     'real_user_id': os.getuid(),
                     'effective_user_id': os.geteuid(),
                     'real_group_id': os.getgid(),
                     'effective_group_id': os.getgid()}

# Generated at 2022-06-13 03:36:30.891840
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    import os
    import pwd
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector.user import UserFactCollector

    # Create a fake module and a similarly fake BaseFactCollector instance
    module = BaseFactCollector()
    instance = UserFactCollector()

    # Unit test
    all_facts = instance.collect(module=module, collected_facts=None)
    assert all_facts['user_id'] == getpass.getuser()
    assert all_facts['user_uid'] == pwd.getpwnam(getpass.getuser()).pw_uid
    assert all_facts['user_gid'] == pwd.getpwnam(getpass.getuser()).pw_gid

# Generated at 2022-06-13 03:36:39.015639
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_collector_instance = UserFactCollector()
    user_facts = user_collector_instance.collect()
    assert 'user_id' in user_facts
    assert user_facts['user_id'] == getpass.getuser()
    assert 'user_uid' in user_facts
    assert 'user_gid' in user_facts
    assert 'user_gecos' in user_facts
    assert 'user_dir' in user_facts
    assert 'user_shell' in user_facts
    assert 'real_user_id' in user_facts
    assert user_facts['real_user_id'] == os.getuid()
    assert 'effective_user_id' in user_facts
    assert user_facts['effective_user_id'] == os.geteuid()
    assert 'real_group_id' in user

# Generated at 2022-06-13 03:36:47.154298
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_facts = UserFactCollector().collect()
    assert isinstance(user_facts['user_id'], str)
    assert isinstance(user_facts['user_uid'], int)
    assert isinstance(user_facts['user_gid'], int)
    assert isinstance(user_facts['user_shell'], str)
    assert isinstance(user_facts['user_dir'], str)
    assert isinstance(user_facts['user_gecos'], str)
    assert isinstance(user_facts['real_user_id'], int)
    assert isinstance(user_facts['effective_user_id'], int)
    assert isinstance(user_facts['real_group_id'], int)
    assert isinstance(user_facts['effective_group_id'], int)

# Generated at 2022-06-13 03:36:57.903859
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    usrfc = UserFactCollector()
    usrfc_facts = usrfc.collect()
    assert 'user_id' in usrfc_facts
    assert 'user_uid' in usrfc_facts
    assert 'user_gid' in usrfc_facts
    assert 'user_gecos' in usrfc_facts
    assert 'user_dir' in usrfc_facts
    assert 'user_shell' in usrfc_facts
    assert 'real_user_id' in usrfc_facts
    assert 'effective_user_id' in usrfc_facts
    assert 'real_group_id' in usrfc_facts
    assert 'effective_group_id' in usrfc_facts
    assert usrfc_facts['user_id'] == getpass.getuser()
    assert usr

# Generated at 2022-06-13 03:37:08.728280
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    facter = UserFactCollector()
    facts = facter.collect()
    assert facts['user_id'] == getpass.getuser()
    assert facts['user_uid'] == os.geteuid()
    assert facts['user_gid'] == os.getegid()
    # TODO: Add a better test
    #assert facts['user_gecos'] == pwent.pw_gecos
    assert facts['user_dir'] == pwd.getpwuid(os.getuid()).pw_dir
    assert facts['user_shell'] == pwd.getpwuid(os.getuid()).pw_shell
    assert facts['real_user_id'] == os.getuid()
    assert facts['effective_user_id'] == os.geteuid()
    assert facts['effective_group_ids']

# Generated at 2022-06-13 03:37:10.321556
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():

    user_facts = UserFactCollector().collect()
    assert user_facts['user_gecos'] is not None

# Generated at 2022-06-13 03:37:18.680168
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # TODO: implement unit tests
    pass

# Generated at 2022-06-13 03:37:24.383271
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    real_user_facts = UserFactCollector().collect()
    assert 'user_id' in real_user_facts
    assert 'user_uid' in real_user_facts
    assert 'user_gid' in real_user_facts
    assert 'user_gecos' in real_user_facts
    assert 'user_dir' in real_user_facts
    assert 'user_shell' in real_user_facts
    assert 'real_user_id' in real_user_facts
    assert 'effective_user_id' in real_user_facts
    assert 'real_group_id' in real_user_facts
    assert 'effective_group_id' in real_user_facts

# Generated at 2022-06-13 03:37:35.699352
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    import os
    import pwd
    user_id = getpass.getuser()
    # Setup user and group ids.
    os.setuid(0)
    pw = pwd.getpwnam(user_id)
    os.setuid(pw.pw_uid)
    uf = UserFactCollector()
    user_facts = uf.collect()

    assert user_facts['user_id'] == user_id
    assert user_facts['user_uid'] == pw.pw_uid
    assert user_facts['user_gid'] == pw.pw_gid
    assert user_facts['user_gecos'] == pw.pw_gecos
    assert user_facts['user_dir'] == pw.pw_dir

# Generated at 2022-06-13 03:37:44.698642
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
    assert 'effective_group_id' in user_facts

# Generated at 2022-06-13 03:37:46.918971
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user = UserFactCollector()
    result = user.collect()
    assert (result['user_id'] == getpass.getuser())

# Generated at 2022-06-13 03:37:57.666986
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

# Generated at 2022-06-13 03:37:59.101187
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    fact_collector = UserFactCollector()
    fact_collector.collect()

# Generated at 2022-06-13 03:38:06.933949
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # For more information on testing facts collectors, see the documentation:
    #   https://docs.ansible.com/ansible/dev_guide/testing_strategy.html#unit-tests-for-facts-collectors
    user_collector = UserFactCollector()
    collected_facts = {}

    new_facts = user_collector.collect(collected_facts=collected_facts)

    assert isinstance(new_facts, dict)
    assert 'user_id' in new_facts
    assert 'user_uid' in new_facts
    assert 'user_gid' in new_facts
    assert 'user_gecos' in new_facts
    assert 'user_dir' in new_facts
    assert 'user_shell' in new_facts
    assert 'real_user_id' in new_facts

# Generated at 2022-06-13 03:38:14.082696
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_facts = BaseFactCollector().collect_facts(module=None, collected_facts=None,
                                                   fact_class=UserFactCollector,
                                                   fact_subset=UserFactCollector._fact_ids)
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

# Generated at 2022-06-13 03:38:22.841374
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    ufc = UserFactCollector()
    facts = ufc.collect()
    assert facts['user_id'] == getpass.getuser()
    assert facts['user_uid'] == os.getuid()
    assert facts['user_gid'] == os.getgid()
    assert facts['real_user_id'] == os.getuid()
    assert facts['effective_user_id'] == os.geteuid()
    assert facts['real_group_id'] == os.getgid()
    assert facts['effective_group_id'] == os.getegid()

# Generated at 2022-06-13 03:38:48.347946
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_fact_collector = UserFactCollector()

# Generated at 2022-06-13 03:38:58.697116
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_facts = UserFactCollector().collect()
    assert user_facts['user_id'] == getpass.getuser()
    assert user_facts['user_uid'] == pwd.getpwnam(getpass.getuser()).pw_uid
    assert user_facts['user_gid'] == pwd.getpwnam(getpass.getuser()).pw_gid
    assert user_facts['user_gecos'] == pwd.getpwnam(getpass.getuser()).pw_gecos
    assert user_facts['user_dir'] == pwd.getpwnam(getpass.getuser()).pw_dir
    assert user_facts['user_shell'] == pwd.getpwnam(getpass.getuser()).pw_shell

# Generated at 2022-06-13 03:39:09.471411
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    collect = UserFactCollector().collect()

    assert 'user_id' in collect.keys()
    assert 'user_uid' in collect.keys()
    assert 'user_gid' in collect.keys()
    assert 'user_gecos' in collect.keys()
    assert 'user_dir' in collect.keys()
    assert 'user_shell' in collect.keys()
    assert 'real_user_id' in collect.keys()
    assert 'effective_user_id' in collect.keys()

    assert isinstance(collect['user_id'], str)
    assert isinstance(collect['user_uid'], int)
    assert isinstance(collect['user_gid'], int)
    assert isinstance(collect['user_gecos'], str)
    assert isinstance(collect['user_dir'], str)
   

# Generated at 2022-06-13 03:39:20.421603
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    import os

    user_facts = {}

    user_facts["user_id"] = getpass.getuser()

    try:
        pwent = pwd.getpwnam(getpass.getuser())
    except KeyError:
        pwent = pwd.getpwuid(os.getuid())

    user_facts["user_uid"] = pwent.pw_uid
    user_facts["user_gid"] = pwent.pw_gid
    user_facts["user_gecos"] = pwent.pw_gecos
    user_facts["user_dir"] = pwent.pw_dir
    user_facts["user_shell"] = pwent.pw_shell

    user_facts["real_user_id"] = os.getuid()

# Generated at 2022-06-13 03:39:28.092661
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_fact = UserFactCollector()
    user_facts_dict = user_fact.collect()

    expected_user_facts_dict = {
        'user_id': getpass.getuser(),
        'user_uid': os.getuid(),
        'user_gid': os.getgid(),
        'user_gecos': pwd.getpwuid(os.getuid()).pw_gecos,
        'user_dir': pwd.getpwuid(os.getuid()).pw_dir,
        'user_shell': pwd.getpwuid(os.getuid()).pw_shell,
        'effective_user_id': os.geteuid(),
        'effective_group_id': os.getegid(),
    }

    assert user_facts_dict == expected_user

# Generated at 2022-06-13 03:39:29.117147
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    obj = UserFactCollector()
    obj.collect()

# Generated at 2022-06-13 03:39:36.326370
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    ufc = UserFactCollector()
    result = ufc.collect()
    assert 'user_id' in result
    assert 'user_uid' in result
    assert 'user_gid' in result
    assert 'user_gecos' in result
    assert 'user_dir' in result
    assert 'user_shell' in result
    assert 'real_user_id' in result
    assert 'effective_user_id' in result
    assert 'effective_group_id' in result

# Generated at 2022-06-13 03:39:44.209513
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    import os
    import pwd

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

    pwd_entry = pwd.getpwnam(getpass.getuser())

    assert user_facts['user_id'] == getpass.getuser()

# Generated at 2022-06-13 03:39:52.144738
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    userfc = UserFactCollector()
    user_facts = userfc.collect()
    assert 'user_id' in user_facts
    assert 'user_uid' in user_facts
    assert 'user_gid' in user_facts
    assert 'user_gecos' in user_facts
    assert 'user_dir' in user_facts
    assert 'user_shell' in user_facts
    assert 'effective_user_id' in user_facts
    assert 'effective_group_id' in user_facts



# Generated at 2022-06-13 03:40:00.816422
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

# Generated at 2022-06-13 03:40:38.018153
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    """
    Unit test for method collect of class UserFactCollector
    """
    def fake_getpwnam(user_name):
        pwent = pwd.struct_passwd
        pwent.pw_uid = 1000
        pwent.pw_gid = 1000
        pwent.pw_gecos = "gecos"
        pwent.pw_dir = "/home/dir"
        pwent.pw_shell = "/bin/bash"
        return pwent

    def _fake_getuid():
        return 1000
    def _fake_geteuid():
        return 1000
    def _fake_getgid():
        return 1000

    fact_collector = UserFactCollector()
    module = {}
    collected_facts = {}

# Generated at 2022-06-13 03:40:47.676721
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    from ansible.module_utils.facts import FactsCollector
    facts_collector = FactsCollector()
    user_fact_collector = UserFactCollector(facts_collector)
    user_fact_collector.collect()
    assert user_fact_collector.collected_facts["user_id"] == "alice"
    assert user_fact_collector.collected_facts["user_uid"] == 500
    assert user_fact_collector.collected_facts["user_gid"] == 500
    assert user_fact_collector.collected_facts["user_gecos"] == "Alice"
    assert user_fact_collector.collected_facts["user_dir"] == "/home/alice"
    assert user_fact_collector.collected_facts["user_shell"] == "bash"
    assert user

# Generated at 2022-06-13 03:40:51.166833
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    ufc = UserFactCollector()
    result = ufc.collect()
    assert isinstance(result, dict)

if __name__ == '__main__':
    test_UserFactCollector_collect()

# Generated at 2022-06-13 03:40:59.353228
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    """
    When invoked without parameters `UserFactCollector.collect` should
    return a dictionary having entries:
        user_id
        user_uid
        user_gid
        real_user_id
        effective_user_id
        real_group_id
        effective_group_id
    """
    user_id = getpass.getuser()
    pwent = pwd.getpwnam(user_id)
    user_facts = UserFactCollector.collect()
    assert user_facts['user_id'] == user_id
    assert user_facts['user_uid'] == pwent.pw_uid
    assert user_facts['user_gid'] == pwent.pw_gid
    assert user_facts['real_user_id'] == os.getuid()

# Generated at 2022-06-13 03:41:10.443450
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    import pwd
    from ansible.module_utils.facts import collector

    # Set up an instance
    fact_collector = collector.get_collector('UserFactCollector')

    # Set up mock user data
    mock_user_data = {}
    mock_user_data['user_id'] = 'test'
    mock_user_data['user_uid'] = pwd.getpwnam('test').pw_uid
    mock_user_data['user_gid'] = pwd.getpwnam('test').pw_gid
    mock_user_data['user_gecos'] = pwd.getpwnam('test').pw_gecos
    mock_user_data['user_dir'] = pwd.getpwnam('test').pw_dir

# Generated at 2022-06-13 03:41:13.285790
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_facts = UserFactCollector().collect()
    assert user_facts['real_user_id'] == os.getuid()
    assert user_facts['effective_group_id'] == os.getgid()

# Generated at 2022-06-13 03:41:19.437952
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # Create an instance of UserFactCollector
    user_collector = UserFactCollector()

    # Call the method collect of class UserFactCollector instance
    collected_facts = user_collector.collect()

    # Test if the method collect of class UserFactCollector instance
    # return a dictionary
    assert isinstance(collected_facts, dict) is True

    # Test if the method collect of class UserFactCollector instance
    # return good data
    assert collected_facts['user_id'] == 'travis'
    assert isinstance(collected_facts['user_uid'], int) is True
    assert collected_facts['user_uid'] == 2000

# Generated at 2022-06-13 03:41:30.923798
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    ufc = UserFactCollector()
    import_user = __import__('user')
    collected_facts = {}

    ufc.collect(module = import_user, collected_facts = collected_facts)

    assert 'user_id' in collected_facts
    assert 'user_uid' in collected_facts
    assert 'user_gid' in collected_facts
    assert 'user_gecos' in collected_facts
    assert 'user_dir' in collected_facts
    assert 'user_shell' in collected_facts
    assert 'real_user_id' in collected_facts
    assert 'effective_user_id' in collected_facts
    assert 'real_group_id' in collected_facts
    assert 'effective_group_id' in collected_facts

# Generated at 2022-06-13 03:41:31.766126
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    pass

# Generated at 2022-06-13 03:41:36.147053
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    ufc = UserFactCollector()
    user_id = getpass.getuser()
    output = ufc.collect()
    assert(user_id == output['user_id'])
    assert(os.getuid() == output['real_user_id'])
    assert(os.geteuid() == output['effective_user_id'])
    assert(os.getgid() == output['real_group_id'])
    assert(os.getegid() == output['effective_group_id'])

# Generated at 2022-06-13 03:42:49.624689
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_collector = UserFactCollector()
    collected_facts = {}
    test_facts = {'user_uid': 1000,
                  'user_shell': '/bin/bash',
                  'user_gid': 1000,
                  'effective_user_id': 1000,
                  'user_id': 'vagrant',
                  'user_dir': '/home/vagrant',
                  'real_user_id': 1000,
                  'effective_group_id': 1000,
                  'real_group_id': 1000,
                  'user_gecos': 'vagrant'}
    collected_facts = user_collector.collect(collected_facts=collected_facts)
    assert collected_facts == test_facts

# Generated at 2022-06-13 03:42:54.158737
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    """
    Test UserFactCollector.collect
    """
    module = None
    collected_facts = None
    collector = UserFactCollector()
    user_facts = collector.collect(module, collected_facts)

    assert isinstance(user_facts['real_user_id'], int)
    assert isinstance(user_facts['effective_user_id'], int)
    assert isinstance(user_facts['real_group_id'], int)
    assert isinstance(user_facts['effective_group_id'], int)

# Generated at 2022-06-13 03:42:57.362987
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    myTestCollector = UserFactCollector()
    myTestCollector.collect()
    assert isinstance(myTestCollector.collect(), dict)
    assert myTestCollector.collect()['user_id'] == getpass.getuser()

# Generated at 2022-06-13 03:43:00.832529
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    """
    Test the method UserFactCollector.collect
    """
    ufc = UserFactCollector()
    assert 'user_id' in ufc.collect()


# Generated at 2022-06-13 03:43:01.752256
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # TODO: Implement unit test
    pass

# Generated at 2022-06-13 03:43:10.648218
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    """
    Test UserFactCollector collect method
    """
    user_facts = UserFactCollector().collect()

    assert user_facts['user_id'] == getpass.getuser()
    assert user_facts['user_uid'] == pwd.getpwnam(getpass.getuser()).pw_uid
    assert user_facts['user_gid'] == pwd.getpwnam(getpass.getuser()).pw_gid
    assert user_facts['user_gecos'] == pwd.getpwnam(getpass.getuser()).pw_gecos
    assert user_facts['user_dir'] == pwd.getpwnam(getpass.getuser()).pw_dir

# Generated at 2022-06-13 03:43:22.077042
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    """This function test collect method of UserFactCollector class.
    """
    #######################################################################
    # Initializing parameters
    #######################################################################
    output = {
        'user_id': getpass.getuser(),
        'user_uid': os.getuid(),
        'user_gid': os.getgid(),
        'user_gecos': '',
        'user_dir': os.getcwd(),
        'user_shell': '/bin/sh',
        'real_user_id': os.getuid(),
        'effective_user_id': os.getuid(),
        'effective_group_ids': os.getgroups(),
        'real_group_id': os.getgid(),
    }
    #######################################################################
    # Testing
    #######################################################################
    # Instantiate