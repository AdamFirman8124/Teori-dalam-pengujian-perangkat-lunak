

# Generated at 2022-06-13 03:33:21.583013
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    test_facts = UserFactCollector.collect()
    for f in test_facts:
        assert type(test_facts[f]) is int, 'user.py: wrong type'

# Generated at 2022-06-13 03:33:32.522553
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    import os
    import pwd
    import pytest
    from ansible.module_utils.facts.collector import BaseFactCollector

    class MockUserFactCollector(BaseFactCollector):
        def collect(self, module=None, collected_facts=None):
            import os
            import pwd
            user_facts = {}
            user_facts['user_id'] = getpass.getuser()
            user_facts['user_uid'] = os.getuid()
            user_facts['user_gid'] = os.getgid()
            user_facts['user_dir'] = os.getcwd()
            user_facts['user_shell'] = os.getenv('SHELL')
            user_facts['real_user_id'] = os.getuid()

# Generated at 2022-06-13 03:33:38.981726
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    from ansible.module_utils.facts.collectors import all_collectors

    user_collector = UserFactCollector()

    # all_collectors returns a dictionary, where the keys are the names
    # of the collectors and the values are the collector classes
    assert 'UserFactCollector' in all_collectors

    # test whether the vault password file is created and removed
    with open('.VaultTestFile', 'w') as vault_test_file:
        pass
    user_collector.collect()
    assert not os.path.isfile('.VaultTestFile')

# Generated at 2022-06-13 03:33:39.920464
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    fact_collector = UserFactCollector()
    user_facts = fact_collector.collect()
    assert user_facts, 'Empty user facts'

# Generated at 2022-06-13 03:33:42.447269
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    module = None
    collected_facts = {}
    userfact_obj = UserFactCollector()
    res = userfact_obj.collect()
    print(res)

# Generated at 2022-06-13 03:33:43.066535
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    assert True

# Generated at 2022-06-13 03:33:49.945139
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    """Unit test class UserFactCollector.

    This is a testing stub for unit testing the module UserFactCollector.
    This will be replaced with a proper unit test framework.
    """

    # Initialize the test object
    user_collector = UserFactCollector()

    # Unit test the method
    collected_facts = user_collector.collect()

    # Assert on the fact collection
    assert collected_facts['user_id'] == getpass.getuser()


# Generated at 2022-06-13 03:33:56.375150
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    collector = UserFactCollector()
    result = collector.collect()
    assert 'user_id' in result
    assert 'user_uid' in result
    assert 'user_gid' in result
    assert 'user_gecos' in result
    assert 'user_dir' in result
    assert 'user_shell' in result
    assert 'real_user_id' in result
    assert 'effective_user_id' in result
    assert 'effective_group_ids' in result

# Generated at 2022-06-13 03:34:03.452992
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user = UserFactCollector()
    user_facts = user.collect()

    assert user_facts['user_id'] == getpass.getuser()
    assert user_facts['user_uid'] == os.getuid()
    assert user_facts['user_gid'] == os.getgid()
    assert user_facts['real_user_id'] == os.getuid()
    assert user_facts['effective_user_id'] == os.geteuid()
    assert user_facts['real_group_id'] == os.getgid()
    assert user_facts['effective_group_id'] == os.getgid()

# Generated at 2022-06-13 03:34:10.587576
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # test environment
    os.environ["HOME"] = "/home/user"
    os.environ["USER"] = "user"

    # test class attributes
    user_fact_collector = UserFactCollector()
    user_fact_collector._fact_ids = None

    # test method attributes
    expected_result = {'user_id': 'user',
                       'user_uid': 1000,
                       'user_gid': 1000,
                       'user_gecos': 'user,,,',
                       'user_dir': '/home/user',
                       'user_shell': '/bin/bash',
                       'real_user_id': 1000,
                       'effective_user_id': 1000,
                       'real_group_id': 1000,
                       'effective_group_id': 1000}

    assert user_fact_collector.collect()

# Generated at 2022-06-13 03:34:23.307209
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():

    # This test works on the assumption that the user executing this module
    # is in /etc/passwd. This should be a safe assumption.

    user = UserFactCollector()

    # Add all the identifiers in _fact_ids to dict
    user_facts = dict.fromkeys(user._fact_ids)

    user_facts = user.collect(collected_facts=user_facts)

    assert getpass.getuser() == user_facts['user_id']
    assert os.getuid() == user_facts['real_user_id']
    assert os.getgid() == user_facts['real_group_id']
    assert user_facts['user_uid'] == user_facts['real_user_id']

# Generated at 2022-06-13 03:34:29.936508
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    import sys
    import tempfile
    from ansible.module_utils.facts.collector import FactsCollector

    if sys.version_info[0] < 3:
        from cStringIO import StringIO
    else:
        from io import StringIO

    collector = FactsCollector()
    collector.collect(module_file=tempfile.mkstemp()[1])
    # Create an instance of UserFactCollector
    user_collector = UserFactCollector()

    # Wrap the stdout
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()

    user_collector.collect(module=None, collected_facts=None)

    user_facts = {}
    # Get the facts collected
    user_facts = mystdout.getvalue()

    # Reset redirect.

# Generated at 2022-06-13 03:34:34.007409
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user = UserFactCollector()
    # Using this method, it is not possible to check that facts are correctly
    # collected in Ansible.
    # Thus we only check that the returned value is a dict.
    assert isinstance(user.collect(), dict)

# Generated at 2022-06-13 03:34:34.535521
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    pass

# Generated at 2022-06-13 03:34:44.198597
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_collector = UserFactCollector()
    d = user_collector.collect()
    assert d.get('user_id') is not None
    assert d.get('user_uid') is not None
    assert d.get('user_uid') == os.getuid()
    assert d.get('user_gid') == os.getgid()
    assert d.get('user_gecos') is not None
    assert d.get('user_dir') is not None
    assert d.get('user_shell') is not None
    assert d.get('real_user_id') == os.getuid()
    assert d.get('effective_user_id') == os.geteuid()
    assert d.get('real_group_id') == os.getgid()

# Generated at 2022-06-13 03:34:50.113067
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    uid = os.getuid()
    euid = os.geteuid()
    gid = os.getgid()
    egid = os.getegid()

    user_fact = UserFactCollector()
    user_facts = user_fact.collect()

    assert uid == user_facts['real_user_id']
    assert euid == user_facts['effective_user_id']
    assert gid == user_facts['real_group_id']
    assert egid == user_facts['effective_group_id']

# Generated at 2022-06-13 03:34:51.397423
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    ufc = UserFactCollector()
    assert ufc.collect() is not None

# Generated at 2022-06-13 03:34:58.294879
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    result = UserFactCollector.collect()
    # This method is not supposed to return any facts, just the names of available facts
    assert result == {'user_id': 'root',
                      'user_uid': 0,
                      'user_gid': 0,
                      'user_gecos': 'root',
                      'user_dir': '/root',
                      'user_shell': '/bin/bash',
                      'real_user_id': 0,
                      'effective_user_id': 0,
                      'real_group_id': 0,
                      'effective_group_id': 0}

# Generated at 2022-06-13 03:35:09.151579
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_facts = UserFactCollector()
    subsystem_facts = user_facts.collect()

    assert len(user_facts._fact_ids) >= len(subsystem_facts)
    assert 'user_id' in subsystem_facts
    assert 'user_uid' in subsystem_facts
    assert 'user_gid' in subsystem_facts
    assert 'user_gecos' in subsystem_facts
    assert 'user_dir' in subsystem_facts
    assert 'user_shell' in subsystem_facts
    assert 'real_user_id' in subsystem_facts
    assert 'effective_user_id' in subsystem_facts
    assert 'effective_group_ids' in subsystem_facts


# Generated at 2022-06-13 03:35:16.190736
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_collector = UserFactCollector()
    user_collector_facts = user_collector.collect(None, None)
    assert user_collector_facts['user_id'] == getpass.getuser()
    assert user_collector_facts['user_uid'] == pwd.getpwnam(getpass.getuser()).pw_uid
    assert user_collector_facts['user_gecos'] == pwd.getpwnam(getpass.getuser()).pw_gecos
    assert user_collector_facts['user_gid'] == pwd.getpwnam(getpass.getuser()).pw_gid
    assert user_collector_facts['user_dir'] == pwd.getpwnam(getpass.getuser()).pw_dir
    assert user_collector

# Generated at 2022-06-13 03:35:29.360765
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user = UserFactCollector()
    user_result = user.collect()
    assert user_result['user_id'] == getpass.getuser()
    assert user_result['effective_user_id'] == os.geteuid()
    assert user_result['user_uid'] == pwd.getpwnam(getpass.getuser()).pw_uid
    assert user_result['user_gid'] == pwd.getpwnam(getpass.getuser()).pw_gid
    assert user_result['user_gecos'] == pwd.getpwnam(getpass.getuser()).pw_gecos
    assert user_result['user_dir'] == pwd.getpwnam(getpass.getuser()).pw_dir

# Generated at 2022-06-13 03:35:32.200431
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    ufc = UserFactCollector()
    facts = ufc.collect()

    assert facts is not None
    assert isinstance(facts, dict)
    assert set(facts.keys()) == ufc._fact_ids

# Generated at 2022-06-13 03:35:44.668640
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    import os
    import pwd

    user_fact_collector = UserFactCollector()
    user_facts = user_fact_collector.collect()

    assert user_facts['user_id'] == getpass.getuser()

    try:
        pwent = pwd.getpwnam(getpass.getuser())
    except KeyError:
        pwent = pwd.getpwuid(os.getuid())

    assert user_facts['user_uid'] == pwent.pw_uid
    assert user_facts['user_gid'] == pwent.pw_gid
    assert user_facts['user_gecos'] == pwent.pw_gecos
    assert user_facts['user_dir'] == pwent.pw_dir
    assert user_facts['user_shell'] == pwent.pw

# Generated at 2022-06-13 03:35:47.795037
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    """
    Test case for collect method of class UserFactCollector
    """
    user_fact_collector = UserFactCollector()
    user_fact_collector.collect()

# Generated at 2022-06-13 03:35:57.572455
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    '''
    Unit test for method collect of class UserFactCollector
    '''

    user_1 = UserFactCollector()
    user_2 = UserFactCollector()

    # positive test case
    results = user_1.collect()
    assert results['real_user_id'] == user_2.collect()['real_user_id']
    assert results['effective_user_id'] == user_2.collect()['effective_user_id']

    # negative test case
    results = user_1.collect()
    assert results['real_user_id'] != user_2.collect()['real_user_id']
    assert results['effective_user_id'] != user_2.collect()['effective_user_id']

# Generated at 2022-06-13 03:36:02.597681
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    ufc = UserFactCollector()
    facts = ufc.collect()
    assert('user_id' in facts)
    assert('user_uid' in facts)
    assert('user_gid' in facts)
    assert('user_gecos' in facts)
    assert('user_dir' in facts)
    assert('user_shell' in facts)
    assert('real_user_id' in facts)
    assert('effective_user_id' in facts)
    assert('effective_group_ids' in facts)

# Generated at 2022-06-13 03:36:14.400043
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_fact_collector = UserFactCollector()
    user_facts = user_fact_collector.collect()
    assert user_facts['user_id'] == getpass.getuser()
    assert user_facts['user_uid'] == os.getuid()
    assert user_facts['user_gid'] == os.getgid()
    assert user_facts['user_gecos'] == pwd.getpwuid(os.getuid()).pw_gecos
    assert user_facts['user_dir'] == pwd.getpwuid(os.getuid()).pw_dir
    assert user_facts['user_shell'] == pwd.getpwuid(os.getuid()).pw_shell
    assert user_facts['real_user_id'] == os.getuid()
    assert user_facts

# Generated at 2022-06-13 03:36:16.993631
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user = UserFactCollector()
    facts = user.collect()
    user_id = getpass.getuser()
    assert user_id == facts['user_id']


# Generated at 2022-06-13 03:36:25.915498
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # test with non-default values
    test_dict = {'user_id': 'testuser', 'user_uid': '1245', 'user_gid': '5678', 'user_gecos': 'Test User',
                 'user_dir': 'test/dir', 'user_shell': 'test/shell', 'real_user_id': os.getuid(),
                 'effective_user_id': os.geteuid(), 'real_group_id': os.getgid(),
                 'effective_group_id': os.getgid()}

    ufc = UserFactCollector()
    assert ufc.collect() == test_dict

# Generated at 2022-06-13 03:36:35.980738
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

# Generated at 2022-06-13 03:36:53.024476
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    collectFacts = UserFactCollector()

# Generated at 2022-06-13 03:37:01.561678
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_mod = UserFactCollector()
    user_facts = user_mod.collect()
    assert user_facts['user_id'] == getpass.getuser()
    assert user_facts['user_uid'] == pwd.getpwnam(getpass.getuser()).pw_uid
    assert user_facts['user_gid'] == pwd.getpwnam(getpass.getuser()).pw_gid
    assert user_facts['user_gecos'] == pwd.getpwnam(getpass.getuser()).pw_gecos
    assert user_facts['user_dir'] == pwd.getpwnam(getpass.getuser()).pw_dir
    assert user_facts['user_shell'] == pwd.getpwnam(getpass.getuser()).pw_shell

# Generated at 2022-06-13 03:37:03.253982
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_facts = UserFactCollector().collect()
    assert isinstance(user_facts, dict)

# Generated at 2022-06-13 03:37:14.861506
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    collector = UserFactCollector()
    facts = collector.collect()

# Generated at 2022-06-13 03:37:22.134095
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    """Test UserFactCollector"""
    collector = UserFactCollector()
    facts = collector.collect()
    assert facts['user_id'] == 'root'
    assert facts['user_uid'] == 0
    assert facts['user_gid'] == 0
    assert facts['user_gecos'] == 'root'
    assert facts['user_dir'] == '/root'
    assert facts['user_shell'] == '/bin/bash'
    assert facts['real_user_id'] == 0
    assert facts['effective_user_id'] == 0
    assert facts['real_group_id'] == 0
    assert facts['effective_group_id'] == 0

# Generated at 2022-06-13 03:37:31.313979
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    c = UserFactCollector()
    r = c.collect()
    assert r['user_id'] != ''
    assert r['user_uid'] != ''
    assert r['user_gid'] != ''
    assert r['user_gecos'] != ''
    assert r['user_dir'] != ''
    assert r['user_shell'] != ''
    assert r['real_user_id'] != ''
    assert r['effective_user_id'] != ''
    assert r['real_group_id'] != ''
    assert r['effective_group_id'] != ''

# Generated at 2022-06-13 03:37:42.620410
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils.facts.collector import Cache
    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils.facts.collector.user import UserFactCollector

    cache = Cache()
    cache = get_collector_instance(UserFactCollector).collect(cache=cache)

    assert cache.get('user_id') == getpass.getuser()
    assert cache.get('user_uid') == pwd.getpwnam(getpass.getuser()).pw_uid
    assert cache.get('user_gid') == pwd.getpwnam(getpass.getuser()).pw_gid
    assert cache.get('user_gecos') == pwd.get

# Generated at 2022-06-13 03:37:51.071670
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_fact_collector = UserFactCollector()
    user_facts = user_fact_collector.collect()
    assert user_facts is not None
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


# Generated at 2022-06-13 03:37:53.382927
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    fact_collector = UserFactCollector()
    fact_collector.collect()


# Generated at 2022-06-13 03:38:02.960541
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    from ansible.module_utils.facts.collectors import UserFactCollector
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.system import DefaultCollector
    import os

    uid = os.getuid()
    euid = os.geteuid()
    gid = os.getgid()
    egid = os.getegid()

# Generated at 2022-06-13 03:38:26.864882
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    my_user_id = 'ansible'
    my_user_uid = pwd.getpwnam(my_user_id).pw_uid
    my_user_gid = pwd.getpwnam(my_user_id).pw_gid
    my_user_gecos = pwd.getpwnam(my_user_id).pw_gecos
    my_user_dir = pwd.getpwnam(my_user_id).pw_dir
    my_user_shell = pwd.getpwnam(my_user_id).pw_shell
    my_real_user_id = os.getuid()
    my_effective_user_id = os.geteuid()
    my_real_group_id = os.getgid()
    my_effective_group

# Generated at 2022-06-13 03:38:29.293954
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():

    # create instance of UserFactCollector
    ofc = UserFactCollector()
    # call method collect of class UserFactCollector
    ofc.collect()
    

# Generated at 2022-06-13 03:38:37.360191
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # Prepare a mock module object
    class MockModule:
        pass
    mock_module = MockModule()

    # Create an instance of UserFactCollector
    user_fact_collector = UserFactCollector()

    # Retrieve facts
    user_facts = user_fact_collector.collect(mock_module)

    # Check that the facts are as expected
    assert user_facts['user_id'] == getpass.getuser()
    assert user_facts['user_uid'] == pwd.getpwnam(user_facts['user_id']).pw_uid
    assert user_facts['user_gid'] == pwd.getpwnam(user_facts['user_id']).pw_gid

# Generated at 2022-06-13 03:38:44.922676
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    result1 = UserFactCollector().collect()

    assert result1['user_id']
    assert result1['user_uid']
    assert result1['user_gid']
    assert result1['user_gecos']
    assert result1['user_dir']
    assert result1['user_shell']
    assert result1['real_user_id']
    assert result1['effective_user_id']
    assert result1['real_group_id']
    assert result1['effective_group_id']

# Generated at 2022-06-13 03:38:47.455334
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    fact_collector = UserFactCollector()
    fact_collector.collect()

# Generated at 2022-06-13 03:38:48.815574
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    UserFactCollector().collect()

# Generated at 2022-06-13 03:38:50.244470
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    usrclt = UserFactCollector()
    usrclt.collect()

# Generated at 2022-06-13 03:38:59.909274
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    test_UserFactCollector = UserFactCollector()
    result_user_facts = test_UserFactCollector.collect()
    assert (result_user_facts['user_id'] is not None)
    assert (result_user_facts['user_uid'] is not None)
    assert (result_user_facts['user_gid'] is not None)
    assert (result_user_facts['user_gecos'] is not None)
    assert (result_user_facts['user_dir'] is not None)
    assert (result_user_facts['user_shell'] is not None)
    assert (result_user_facts['real_user_id'] is not None)
    assert (result_user_facts['effective_user_id'] is not None)

# Generated at 2022-06-13 03:39:10.379062
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    
    # Arrange
    fact_output = {
        "user_id": "ansible",
        "user_gecos": "ansible",
        "user_uid": 1000,
        "user_shell": "/bin/bash",
        "user_dir": "/home/ansible",
        "user_gid": 1000,
        "effective_user_id": 1000,
        "effective_group_id": 1000,
        "real_user_id": 1000,
        "real_group_id": 1000
    }
    
    # Act
    user_fact_collector = UserFactCollector()
    fact_output = user_fact_collector.collect()
    
    # Assert
    assert fact_output == fact_output

# Generated at 2022-06-13 03:39:12.995140
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_collector = UserFactCollector()

    user_facts_dict = user_collector.collect()

    assert type(user_facts_dict) is dict

# Generated at 2022-06-13 03:39:43.553983
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    ufc = UserFactCollector()
    assert ufc.collect() == {'user_id': 'ctm-test',
                             'user_uid': 0,
                             'user_gid': 0,
                             'user_gecos': 'Citrix Test',
                             'user_dir': '/root',
                             'user_shell': '/bin/bash',
                             'real_user_id': 0,
                             'effective_user_id': 0,
                             'real_group_id': 0,
                             'effective_group_id': 0}

# Generated at 2022-06-13 03:39:54.348984
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    ufc = UserFactCollector()

    # current user information
    fake_user_id = 'fake_user_id'
    fake_user_uid = 'fake_user_uid'
    fake_user_gid = 'fake_user_gid'
    fake_user_gecos = 'fake_user_gecos'
    fake_user_dir = 'fake_user_dir'
    fake_user_shell = 'fake_user_shell'
    fake_real_user_id = 'fake_real_user_id'
    fake_effective_user_id = 'fake_effective_user_id'
    fake_effective_group_ids = 'fake_effective_group_ids'

    def pwd_getpwnam(getuser):
        if getuser==fake_user_id:
            return MockPwdStruct

# Generated at 2022-06-13 03:40:01.145059
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    expected_real_user_id = os.getuid()
    expected_effective_user_id = os.geteuid()

    user_facts = UserFactCollector().collect()

    assert(user_facts['user_id'] == getpass.getuser())
    assert(user_facts['user_uid'] == user_facts['real_user_id'])
    assert(user_facts['user_uid'] == user_facts['effective_user_id'])
    assert(user_facts['user_uid'] == expected_real_user_id)
    assert(user_facts['user_uid'] == expected_effective_user_id)

# Generated at 2022-06-13 03:40:11.556873
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    module = MagicMock(params={})
    collected_facts = {}
    real_user_id = os.getuid()
    effective_user_id = os.geteuid()
    real_group_id = os.getgid()
    effective_group_id = os.getgid()

    a_user_fact_collector = UserFactCollector(module=module, collected_facts=collected_facts)
    user_facts = a_user_fact_collector.collect()

    assert(user_facts['user_id'] == getpass.getuser())
    assert(user_facts['user_uid'] == pwent.pw_uid)
    assert(user_facts['user_gid'] == pwent.pw_gid)

# Generated at 2022-06-13 03:40:20.219094
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():

    # Setup
    user_fact_collector = UserFactCollector()
    user_fact_collector_result = {
        'user_gecos': 'mzachmann,,,',
        'user_id': 'mzachmann',
        'user_gid': 1000,
        'user_shell': '/bin/bash',
        'user_uid': 1000,
        'real_user_id': 1000,
        'user_dir': '/home/mzachmann',
        'effective_user_id': 1000
    }

    # Test
    user_facts = user_fact_collector.collect()

    # Verify
    assert user_facts == user_fact_collector_result, 'Wrong results'

# Generated at 2022-06-13 03:40:27.423567
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    c = UserFactCollector()
    results = c.collect()

    assert 'ansible_facts' in results
    assert 'user_id' in results['ansible_facts']
    assert 'user_uid' in results['ansible_facts']
    assert 'user_gid' in results['ansible_facts']
    assert 'user_gecos' in results['ansible_facts']
    assert 'user_dir' in results['ansible_facts']
    assert 'user_shell' in results['ansible_facts']
    assert 'real_user_id' in results['ansible_facts']
    assert 'effective_user_id' in results['ansible_facts']
    assert 'real_group_id' in results['ansible_facts']
    assert 'effective_group_id' in results['ansible_facts']

   

# Generated at 2022-06-13 03:40:36.328289
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():

    # Path to file "test_facts_user.py"
    path_file = os.path.realpath(__file__)
    # Directory where is file "test_facts_user.py"
    dir_file = os.path.dirname(path_file)

    # Create a instance of class UserFactCollector
    user_facts = UserFactCollector()
    # Create a dict with all variables in this class
    user_facts.collect()

    # Use a dict to compare with the dict with all variables in class UserFactCollector

# Generated at 2022-06-13 03:40:46.869966
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    from ansible.module_utils.facts import Facts

    collector = UserFactCollector()
    collected_facts = Facts()
    collected_facts.ansible_facts = {}
    assert not hasattr(collected_facts, 'user')
    collected_facts = collector.collect(collected_facts=collected_facts)

    assert hasattr(collected_facts, 'ansible_facts')
    assert 'user' in collected_facts.ansible_facts
    assert len(collected_facts.ansible_facts['user']) >= 6

    assert 'user_id' in collected_facts.ansible_facts['user']
    assert 'user_uid' in collected_facts.ansible_facts['user']
    assert 'user_gid' in collected_facts.ansible_facts['user']

# Generated at 2022-06-13 03:40:48.536076
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_fact_collector = UserFactCollector()

    user_fact_collector.collect()

# Generated at 2022-06-13 03:40:57.787875
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    module = MagicMock()
    collected_facts = dict()
    ufc = UserFactCollector()
    user_facts = ufc.collect(module=module, collected_facts=collected_facts)

    assert user_facts['user_id'].split('-')[0] == getpass.getuser().split('-')[0]

    pwent = pwd.getpwnam(getpass.getuser())
    assert user_facts['user_uid'] == pwent.pw_uid
    assert user_facts['user_gid'] == pwent.pw_gid
    assert user_facts['user_gecos'] == pwent.pw_gecos
    assert user_facts['user_dir'] == pwent.pw_dir
    assert user_facts['user_shell'] == pwent.pw_

# Generated at 2022-06-13 03:42:00.388766
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():

    user_fact_collector = UserFactCollector()
    user_facts = user_fact_collector.collect()

    # All basic facts should be available
    for user_fact in user_fact_collector._fact_ids:
        assert user_fact in user_facts
        assert user_facts[user_fact] is not None

# Generated at 2022-06-13 03:42:07.179845
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    expected_facts = { "user_shell": "/bin/sh",
                        "user_uid": 1000,
                        "user_id": "test",
                        "user_dir": "/home/test",
                        "effective_user_id": 1000,
                        "user_gecos": "test,,,",
                        "effective_group_id": 1000,
                        "real_user_id": 1000,
                        "user_gid": 1000,
                        "real_group_id": 1000}

    collector = UserFactCollector()
    collected_facts = collector.collect()

    assert collected_facts == expected_facts

# Generated at 2022-06-13 03:42:16.369512
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_facts_collector = UserFactCollector()

    user_facts = user_facts_collector.collect()

    assert type(user_facts) is dict
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

# Generated at 2022-06-13 03:42:22.578386
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    collector = UserFactCollector()
    collected_facts = collector.collect()
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

# Generated at 2022-06-13 03:42:23.615926
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_facts = UserFactCollector().collect()
    assert user_facts is not None

# Generated at 2022-06-13 03:42:29.060440
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():

    m_module = Mock(params={})
    m_collector = Mock(spec=UserFactCollector)
    m_collector._fact_ids = set(['user_id', 'user_uid', 'user_gid',
                                 'user_gecos', 'user_dir', 'user_shell',
                                 'real_user_id', 'effective_user_id',
                                 'effective_group_ids'])
    m_pwent = Mock()
    m_pwent.pw_uid = 42
    m_pwent.pw_gid = 42
    m_pwent.pw_gecos = 'bob'
    m_pwent.pw_dir = '/home/bob'
    m_pwent.pw_shell = '/bin/bash'

    # Testing return with uid and

# Generated at 2022-06-13 03:42:38.565017
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    ufc = UserFactCollector()
    data = ufc.collect()
    assert isinstance(data['user_id'], str)
    assert isinstance(data['user_uid'], int)
    assert isinstance(data['user_gid'], int)
    assert isinstance(data['user_gecos'], str)
    assert isinstance(data['user_dir'], str)
    assert isinstance(data['user_shell'], str)
    assert isinstance(data['real_user_id'], int)
    assert isinstance(data['effective_user_id'], int)
    assert isinstance(data['effective_group_ids'], list)

# Generated at 2022-06-13 03:42:44.977705
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_fact_collector = UserFactCollector()
    user_facts = user_fact_collector.collect()
    assert user_facts['user_id'] == getpass.getuser()
    assert user_facts['user_uid'] == pwd.getpwnam(getpass.getuser()).pw_uid
    assert user_facts['user_gid'] == pwd.getpwnam(getpass.getuser()).pw_gid
    assert user_facts['user_gecos'] == pwd.getpwnam(getpass.getuser()).pw_gecos
    assert user_facts['user_dir'] == pwd.getpwnam(getpass.getuser()).pw_dir

# Generated at 2022-06-13 03:42:52.850534
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    '''
    This will test the UserFactCollector collect method and assert that all values are as expected
    '''
    # Create a dictionary of expected facts

# Generated at 2022-06-13 03:42:55.195376
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_facts = UserFactCollector().collect()
    assert isinstance(user_facts, dict)
    assert type(user_facts) == dict
    assert user_facts['user_id'].lower() == getpass.getuser().lower()
    assert user_facts['real_user_id'] == os.getuid()