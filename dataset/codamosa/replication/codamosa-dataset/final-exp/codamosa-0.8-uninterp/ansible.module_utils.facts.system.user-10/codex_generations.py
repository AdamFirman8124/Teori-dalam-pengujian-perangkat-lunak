

# Generated at 2022-06-13 03:33:26.142489
# Unit test for method collect of class UserFactCollector

# Generated at 2022-06-13 03:33:35.708717
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():

    from ansible.module_utils.facts import Facts
    from ansible.module_utils.facts.collectors.user import UserFactCollector
    import os

    facts = Facts({})
    fact_collector = UserFactCollector()

    fact_collector.collect(collected_facts=facts)

    try:
        pwent = pwd.getpwnam(getpass.getuser())
    except KeyError:
        pwent = pwd.getpwuid(os.getuid())

    assert facts['user_id'] == getpass.getuser()
    assert facts['user_uid'] == pwent.pw_uid
    assert facts['user_gid'] == pwent.pw_gid
    assert facts['user_gecos'] == pwent.pw_gecos
    assert facts['user_dir']

# Generated at 2022-06-13 03:33:42.830105
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    class FakeModule(object):
        def __init__(self):
            self.ansible_facts = {}
            self.params = {}

    module = FakeModule()
    collector = UserFactCollector()
    collected_facts = collector.collect(module)

    assert set(collected_facts.keys()).issubset(set([
        'user_id', 'user_uid', 'user_gid', 'user_gecos',
        'user_dir', 'user_shell'
    ]))

# Generated at 2022-06-13 03:33:49.253627
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    fc = UserFactCollector()
    result = fc.collect()
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

# Generated at 2022-06-13 03:33:59.054996
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    ufc = UserFactCollector()
    result = ufc.collect()
    assert result['user_id'] == getpass.getuser()
    assert result['user_uid'] == pwd.getpwnam(getpass.getuser()).pw_uid
    assert result['user_gid'] == pwd.getpwnam(getpass.getuser()).pw_gid
    assert result['user_gecos'] == pwd.getpwnam(getpass.getuser()).pw_gecos
    assert result['user_dir'] == pwd.getpwnam(getpass.getuser()).pw_dir
    assert result['user_shell'] == pwd.getpwnam(getpass.getuser()).pw_shell
    assert result['real_user_id'] == os.getuid

# Generated at 2022-06-13 03:34:07.399145
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    from ansible.module_utils.facts.system.user import UserFactCollector
    from ansible.module_utils._text import to_bytes

    user_fact_collector = UserFactCollector()
    result = user_fact_collector.collect()

    assert result['user_id'] == getpass.getuser()
    assert result['user_uid'] == os.getuid()
    assert result['user_gid'] == os.getgid()
    assert result['real_user_id'] == os.getuid()
    assert result['effective_user_id'] == os.geteuid()
    assert result['real_group_id'] == os.getgid()
    assert result['effective_group_id'] == os.getgid()
    assert result['user_gecos'].startswith("root")
   

# Generated at 2022-06-13 03:34:09.349054
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    fact_collector = UserFactCollector()
    fact_collector.collect()

# Generated at 2022-06-13 03:34:16.644691
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    assert UserFactCollector().collect() == {
        'user_id': getpass.getuser(),
        'user_uid': os.getuid(),
        'user_gid': os.getgid(),
        'user_gecos': pwd.getpwuid(os.getuid())[4],
        'user_dir': pwd.getpwuid(os.getuid())[5],
        'user_shell': pwd.getpwuid(os.getuid())[6],
        'real_user_id': os.getuid(),
        'effective_user_id': os.getuid(),
        'real_group_id': os.getgid(),
        'effective_group_id': os.getgid()
    }

# Generated at 2022-06-13 03:34:26.366448
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    import pwd
    fact_collector = UserFactCollector()
    fact_collector.collect()
    user_facts = fact_collector.collect_facts()
    keys = ['user_id', 'user_uid', 'user_gid', 'user_gecos', 'user_dir', 'user_shell', 'real_user_id', 'effective_user_id', 'real_group_id', 'effective_group_id']
    for key in keys:
        assert key in user_facts
    #check user id
    assert user_facts['user_id'] == os.getlogin()
    #check user uid
    assert user_facts['user_uid'] == pwd.getpwnam(os.getlogin()).pw_uid
    #check user gid

# Generated at 2022-06-13 03:34:37.093785
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    ufc = UserFactCollector()
    collected_facts = ufc.collect()
    test_user = getpass.getuser()
    user_uid = pwd.getpwnam(test_user).pw_uid
    user_gid = pwd.getpwnam(test_user).pw_gid
    user_gecos = pwd.getpwnam(test_user).pw_gecos
    user_dir = pwd.getpwnam(test_user).pw_dir
    user_shell = pwd.getpwnam(test_user).pw_shell
    real_user_id = os.getuid()
    effective_user_id = os.geteuid()
    real_group_id = os.getgid()
    effective_group_id = os.getg

# Generated at 2022-06-13 03:34:47.437602
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_fact_collector = UserFactCollector()
    result = user_fact_collector.collect()

    user_id = result['user_id']
    user_uid = result['user_uid']
    user_gid = result['user_gid']
    user_gecos = result['user_gecos']
    user_dir = result['user_dir']
    user_shell = result['user_shell']
    real_user_id = result['real_user_id']
    effective_user_id = result['effective_user_id']
    real_group_id = result['real_group_id']
    effective_group_id = result['effective_group_id']

    (user_id == "user_id")
    (user_uid == "user_uid")

# Generated at 2022-06-13 03:34:57.334044
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    import os
    import json

    user_fact_collector = UserFactCollector()
    user_facts = user_fact_collector.collect()

    if os.environ.get('HOME') is None :
        user_dir = '/root'
    else :
        user_dir = os.environ.get('HOME')

    assert user_facts['user_gecos'] == 'root'
    assert user_facts['user_id'] == 'root'
    assert user_facts['user_uid'] == 0
    assert user_facts['user_gid'] == 0
    assert user_facts['user_dir'] == user_dir
    assert user_facts['user_shell'] == '/bin/bash'
    assert user_facts['real_user_id'] == os.getuid()

# Generated at 2022-06-13 03:35:10.268534
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    collector = UserFactCollector(None)

    user_facts = collector.collect(None, None)

    user_uid = os.getuid()

    assert user_facts['user_id'] == os.getlogin()
    assert user_facts['user_uid'] == user_uid
    assert user_facts['user_gid'] == pwd.getpwuid(user_uid).pw_gid
    assert user_facts['user_gecos'] == pwd.getpwuid(user_uid).pw_gecos
    assert user_facts['user_dir'] == pwd.getpwuid(user_uid).pw_dir
    assert user_facts['user_shell'] == pwd.getpwuid(user_uid).pw_shell
    assert user_facts['real_user_id'] == user_

# Generated at 2022-06-13 03:35:21.447013
# Unit test for method collect of class UserFactCollector

# Generated at 2022-06-13 03:35:30.571936
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    print("\nExecuting test_UserFactCollector_collect")
    import platform
    import json

    if platform.system() == 'Darwin':
        # test with the current local user
        u = UserFactCollector()
        f = u.collect()
        print("user_id: " + f['user_id'])
        print("user_uid: " + str(f['user_uid']))
        print("user_gid: " + str(f['user_gid']))
        print("user_gecos: " + f['user_gecos'])
        print("user_dir: " + f['user_dir'])
        print("user_shell: " + f['user_shell'])
        print("json.dumps(f): " + json.dumps(f))

        # test with the ans

# Generated at 2022-06-13 03:35:39.190942
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    infos = UserFactCollector().collect()
    assert 'user_id' in infos
    assert 'user_uid' in infos
    assert 'user_gid' in infos
    assert 'user_gecos' in infos
    assert 'user_dir' in infos
    assert 'user_shell' in infos
    assert 'real_user_id' in infos
    assert 'effective_user_id' in infos
    assert 'real_group_id' in infos
    assert 'effective_group_id' in infos

# Generated at 2022-06-13 03:35:50.457373
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    import os
    import pwd
    import getpass
    import platform

    user_facts = {}

    user_facts['user_id'] = getpass.getuser()

    try:
        pwent = pwd.getpwnam(getpass.getuser())
    except KeyError:
        if platform.system() == 'Darwin':
            # https://stackoverflow.com/a/9508469
            pwent = pwd.getpwuid(-2)
        else:
            pwent = pwd.getpwuid(os.getuid())

    user_facts['user_uid'] = pwent.pw_uid
    user_facts['user_gid'] = pwent.pw_gid
    user_facts['user_gecos'] = pwent.pw_gecos

# Generated at 2022-06-13 03:36:00.729087
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    userFact = UserFactCollector();
    result = userFact.collect();
    assert(type(result) == dict)
    assert('user_id' in result)
    assert(type(result['user_id']) == str)
    assert('user_uid' in result)
    assert(type(result['user_uid']) == int)
    assert('user_gid' in result)
    assert(type(result['user_gid']) == int)
    assert('user_gecos' in result)
    assert(type(result['user_gecos']) == str)
    assert('user_dir' in result)
    assert(type(result['user_dir']) == str)
    assert('user_shell' in result)
    assert(type(result['user_shell']) == str)

# Generated at 2022-06-13 03:36:02.928118
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # Arrange
    collector = UserFactCollector()

    # Act
    result = collector.collect()

    # Assert
    assert result.keys() == collector._fact_ids

# Generated at 2022-06-13 03:36:06.588679
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    print("\nTesting AnsibleFacts UserFactCollector")
    um = UserFactCollector()
    result = um.collect()
    print("\nResult of collect is {}".format(result))

# Generated at 2022-06-13 03:36:23.952353
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_facts = UserFactCollector().collect()
    assert isinstance(user_facts, dict)
    assert isinstance(user_facts['user_id'], str)
    assert isinstance(user_facts['user_uid'], int)
    assert isinstance(user_facts['user_gid'], int)
    assert isinstance(user_facts['user_gecos'], str)
    assert isinstance(user_facts['user_dir'], str)
    assert isinstance(user_facts['user_shell'], str)
    assert isinstance(user_facts['real_user_id'], int)
    assert isinstance(user_facts['effective_user_id'], int)
    assert isinstance(user_facts['real_group_id'], int)

# Generated at 2022-06-13 03:36:33.142006
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    collector = UserFactCollector()
    returned_facts = collector.collect()
    assert returned_facts == {'user_id': 'default',
                              'user_uid': 0,
                              'user_gid': 0,
                              'user_gecos': 'Default User',
                              'user_dir': '/var/lib/juju/agents/unit-0',
                              'user_shell': '/bin/bash',
                              'real_user_id': 0,
                              'effective_user_id': 0,
                              'real_group_id': 0,
                              'effective_group_id': 0}


test_UserFactCollector_collect()

# Generated at 2022-06-13 03:36:33.750759
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    pass

# Generated at 2022-06-13 03:36:34.247605
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
  pass

# Generated at 2022-06-13 03:36:43.366893
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts import OmnibusFacts

    def fake_getpass_getuser(self):
        return 'test_ansible_user'
    getpass.getuser = fake_getpass_getuser

    def fake_getpwnam(test_ansible_user):
        class FakeUser:
            def __init__(self):
                self.pw_uid = 100
                self.pw_gid = 200
                self.pw_gecos = 'Test Ansible User'
                self.pw_dir = '/home/test_ansible_user'
                self.pw_shell = '/bin/bash'
        return FakeUser()
    pwd.getpwnam = fake_getpwnam


# Generated at 2022-06-13 03:36:45.465641
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    collector = UserFactCollector()
    res = collector.collect()
    print(res)


if __name__ == '__main__':
    test_UserFactCollector_collect()

# Generated at 2022-06-13 03:36:50.762997
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector
    import pwd
    passwd_file = open("/etc/passwd")
    for line in passwd_file:
        if line.startswith('_ansible:'):
            user_ansible = line.split(':')[0]
            break
    passwd_file.close()
    ufc = UserFactCollector()
    collected_facts = {}

# Generated at 2022-06-13 03:36:58.802365
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    from ansible.module_utils.facts import facts
    from ansible.module_utils.facts.collector import Collector

    collector = UserFactCollector()

    module = facts.AnsibleModuleMock()
    output = collector.collect(module)
    expected_keys = set(['user_id', 'user_uid',
                         'user_gid', 'user_dir',
                         'user_gecos', 'user_shell',
                         'real_user_id', 'effective_user_id'])

    assert isinstance(collector, Collector)
    assert set(output.keys()) == expected_keys

# Generated at 2022-06-13 03:37:04.575401
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    import ansible.module_utils.facts.collectors.user
    import sys

    # Get a UserFactCollector
    fact_collector = ansible.module_utils.facts.collectors.user.UserFactCollector()

    # Collect the facts
    facts = fact_collector.collect()

    # Ensure that the facts are expected
    assert sys.version_info >= (3, 0)
    assert facts['user_id'] == getpass.getuser()
    assert facts['user_uid'] == pwd.getpwnam(getpass.getuser()).pw_uid
    assert facts['user_gid'] == pwd.getpwnam(getpass.getuser()).pw_gid
    assert facts['user_gecos'] == pwd.getpwnam(getpass.getuser()).pw_

# Generated at 2022-06-13 03:37:11.496654
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_fact_collector = UserFactCollector()
    user_facts = user_fact_collector.collect()
    assert user_facts['user_id'] == getpass.getuser()
    assert user_facts['real_user_id'] == os.getuid()
    assert user_facts['effective_user_id'] == os.geteuid()
    assert user_facts['real_group_id'] == os.getgid()
    assert user_facts['effective_group_id'] == os.getgid()

# Generated at 2022-06-13 03:37:28.250793
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    """
    Ensure collect works as expected
    """

    module = None
    collected_facts = None
    ufc = UserFactCollector()
    user_facts = ufc.collect(module, collected_facts)
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

# Generated at 2022-06-13 03:37:32.494506
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_fact_collector = UserFactCollector()

    collected_facts = user_fact_collector.collect()

    assert collected_facts['user_id'] == getpass.getuser()
    assert type(collected_facts['user_id']) is str

# Generated at 2022-06-13 03:37:41.486600
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_facts = UserFactCollector().collect()

    assert user_facts['user_id'] is not None
    assert user_facts['user_uid'] is not None
    assert user_facts['user_gid'] is not None
    assert user_facts['user_gecos'] is not None
    assert user_facts['user_dir'] is not None
    assert user_facts['user_shell'] is not None
    assert user_facts['real_user_id'] is not None
    assert user_facts['effective_user_id'] is not None
    assert user_facts['effective_group_ids'] is None

# Generated at 2022-06-13 03:37:50.673328
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    import os
    user_facts = UserFactCollector().collect()
    assert user_facts['user_id'] == os.environ['USER']
    
    assert user_facts['user_uid'] == os.getuid()
    assert user_facts['user_gid'] == os.getgid()

    assert user_facts['real_user_id'] == os.getuid()
    assert user_facts['effective_user_id'] == os.geteuid()
    assert user_facts['real_group_id'] == os.getgid()
    assert user_facts['effective_group_id'] == os.getgid()

    assert user_facts['user_shell'] == os.environ['SHELL']

# Generated at 2022-06-13 03:37:59.437888
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    collector = UserFactCollector()
    collected_facts = collector.collect()
    print("collected facts : ")
    print(collected_facts)
    assert collected_facts['user_id'] == getpass.getuser()
    assert collected_facts['real_user_id'] == os.getuid()
    assert collected_facts['effective_user_id'] == os.geteuid()
    assert collected_facts['real_group_id'] == os.getgid()
    assert collected_facts['effective_group_id'] == os.getgid()
    
if __name__ == '__main__':
    test_UserFactCollector_collect()

# Generated at 2022-06-13 03:38:07.190029
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    """Tests the collect method of class UserFactCollector
    """
    import pwd
    import os
    # Create a UserFactCollector
    collector = UserFactCollector()

    # Test method with default values
    fact_list = collector.collect()
    assert len(fact_list) == 10
    assert fact_list['user_id'] == 'root'
    assert fact_list['user_uid'] == 0
    assert fact_list['user_gid'] == 0
    assert fact_list['user_gecos'] == ',,,'
    assert fact_list['user_dir'] == '/root'
    assert fact_list['user_shell'] == '/bin/bash'
    assert fact_list['real_user_id'] == 0
    assert fact_list['effective_user_id'] == 0

# Generated at 2022-06-13 03:38:11.820184
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():

    # create an instance of the class under test
    user_fact_collector = UserFactCollector()

    user_facts = user_fact_collector.collect(None, None)

    # The class under test returns dictionnary
    assert(isinstance(user_facts, dict))

    # Check that the dictionnary contains the right keys
    assert(set(user_facts.keys()) == user_fact_collector._fact_ids)

# Generated at 2022-06-13 03:38:16.156185
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_fc = UserFactCollector()
    user_facts = user_fc.collect()
    assert user_facts['user_id'] == getpass.getuser()
    assert user_facts['user_uid'] == os.getuid()
    assert user_facts['user_dir'] == os.path.expanduser('~')

# Generated at 2022-06-13 03:38:17.515621
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    ufc = UserFactCollector()
    ufc.collect()


# Generated at 2022-06-13 03:38:26.415604
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    fact_collector = UserFactCollector()
    result = fact_collector.collect()

    expected_result = {'effective_group_id': 1001,
                       'effective_user_id': 1001,
                       'real_group_id': 1001,
                       'real_user_id': 1001,
                       'user_dir': '/home/sho',
                       'user_gid': 1001,
                       'user_gecos': 'Test User,,,',
                       'user_id': 'sho',
                       'user_shell': '/bin/bash',
                       'user_uid': 1001}

    assert result == expected_result

# Generated at 2022-06-13 03:38:48.024938
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    from ansible.module_utils.facts.collector import FactCollector
    from ansible.module_utils.facts import get_collectors_from_names

    # get the module_utils functions mocked
    get_collectors_from_names_mock = get_collectors_from_names
    get_collectors_from_names_mock.return_value = []

    # test default values
    f = FactCollector()
    assert f.get_collection_string() == ""

    # test 'user' collection method
    f = FactCollector()
    f.collect(['user'])

    assert f.get_collection_string() == "user"

# Generated at 2022-06-13 03:38:58.458883
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_facts = {}

    user_facts['user_id'] = getpass.getuser()

    pwent = pwd.getpwnam(getpass.getuser())

    user_facts['user_uid'] = pwent.pw_uid
    user_facts['user_gid'] = pwent.pw_gid
    user_facts['user_gecos'] = pwent.pw_gecos
    user_facts['user_dir'] = pwent.pw_dir
    user_facts['user_shell'] = pwent.pw_shell
    user_facts['real_user_id'] = os.getuid()
    user_facts['effective_user_id'] = os.geteuid()
    user_facts['real_group_id'] = os.getgid()

# Generated at 2022-06-13 03:39:03.528904
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    '''
    Returns a dict with the following keys: user_id, user_uid, user_gid,
    user_gecos, user_dir, user_shell, real_user_id, effective_user_id,
    real_group_id, effective_group_id.
    '''

    assert UserFactCollector().collect(module=None, collected_facts=None)

# Generated at 2022-06-13 03:39:14.551084
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    module = None
    collected_facts = None
    fact_collector = UserFactCollector()
    
    user_facts = fact_collector.collect(module, collected_facts)
    assert(user_facts['user_id'] == getpass.getuser())
    assert(user_facts['user_uid'] == pwd.getpwnam(getpass.getuser()).pw_uid)
    assert(user_facts['user_gid'] == pwd.getpwnam(getpass.getuser()).pw_gid)
    assert(user_facts['user_gecos'] == pwd.getpwnam(getpass.getuser()).pw_gecos)
    assert(user_facts['user_dir'] == pwd.getpwnam(getpass.getuser()).pw_dir)

# Generated at 2022-06-13 03:39:24.593255
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    import pytest
    user_facts = {
            "user_id" : "test",
            "user_uid": 2000,
            "user_gid": 2000,
            "user_gecos": "test",
            "user_dir": "/home/test",
            "user_shell": "/bin/bash",
            "real_user_id": 2000,
            "effective_user_id": 2000,
            "real_group_id": 2000,
            "effective_group_id": 2000,
            "effective_group_ids" : []
            }

    UF = UserFactCollector()
    mock_getpass = pytest.Mock(return_value = "test")

# Generated at 2022-06-13 03:39:31.605173
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



# Generated at 2022-06-13 03:39:36.285350
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    facts = UserFactCollector().collect()

    assert 'user_id' in facts
    assert 'user_uid' in facts
    assert 'user_gid' in facts
    assert 'user_gecos' in facts
    assert 'user_dir' in facts
    assert 'user_shell' in facts

# Generated at 2022-06-13 03:39:44.181028
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    fs = UserFactCollector()
    fs.collect()
    assert fs.name == 'user'
    assert fs._fact_ids == set(['user_id', 'user_uid', 'user_gid', 'user_gecos',
                                'user_dir', 'user_shell','real_user_id',
                                'effective_user_id','effective_group_ids'])
    assert getpass.getuser()
    assert pwd.getpwuid(os.getuid())
    assert pwd.getpwuid(os.getuid())[0] == os.getuid()
    assert pwd.getpwuid(os.getuid())[2] == os.getgid()
    assert pwd.getpwuid(os.getuid())[3]

# Generated at 2022-06-13 03:39:55.272231
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user = UserFactCollector()
    facts = {'default_ipv4': {'address': '10.10.10.10',
                              'aliases': ['eth0.1'], 'interface': 'eth0'}}

    user_facts = user.collect(None, facts)
    assert user_facts['user_id'] == getpass.getuser()
    assert user_facts['user_uid'] == pwd.getpwnam(getpass.getuser()).pw_uid
    assert user_facts['user_gid'] == pwd.getpwnam(getpass.getuser()).pw_gid
    assert user_facts['user_gecos'] == pwd.getpwnam(getpass.getuser()).pw_gecos

# Generated at 2022-06-13 03:40:02.675094
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    ufc = UserFactCollector()
    facts = ufc.collect()

    assert type(facts['user_id']) == type("")
    assert type(facts['user_uid']) == type(0)
    assert type(facts['user_gid']) == type(0)
    assert type(facts['user_gecos']) == type("")
    assert type(facts['user_dir']) == type("")
    assert type(facts['user_shell']) == type("")
    assert type(facts['real_user_id']) == type(0)
    assert type(facts['effective_user_id']) == type(0)
    assert type(facts['real_group_id']) == type(0)
    assert type(facts['effective_group_id']) == type(0)

# Generated at 2022-06-13 03:40:31.050441
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_fact_collector = UserFactCollector()
    ret = user_fact_collector.collect()
    assert type(ret) == dict
    assert 'user_id' in ret
    assert 'user_uid' in ret

# Generated at 2022-06-13 03:40:37.722473
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # Setup
    module = None; collected_facts = None
    instance = UserFactCollector()
    expected = {'user_id': 'myname', 'user_uid': 1000, 'user_gid': 1000, 'user_gecos': 'gecos', 'user_dir': '/home/myname', 'user_shell': '/bin/bash', 'real_user_id': 1000, 'effective_user_id': 1000, 'real_group_id': 1000, 'effective_group_id': 1000}

    # Mock functions
    def mock_getpass_getuser():
        return 'myname'


# Generated at 2022-06-13 03:40:47.569813
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    fact_collector = UserFactCollector()
    user_facts = fact_collector.collect()

    assert isinstance(user_facts['user_id'], str)
    assert isinstance(user_facts['user_uid'], int)
    assert isinstance(user_facts['user_gid'], int)
    assert isinstance(user_facts['user_gecos'], str)
    assert isinstance(user_facts['user_dir'], str)
    assert isinstance(user_facts['user_shell'], str)
    assert isinstance(user_facts['real_user_id'], int)
    assert isinstance(user_facts['effective_user_id'], int)
    assert isinstance(user_facts['real_group_id'], int)

# Generated at 2022-06-13 03:40:53.667170
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_facts = UserFactCollector().collect()
    assert user_facts['user_id'] == getpass.getuser()
    assert user_facts['real_user_id'] == os.getuid()
    assert user_facts['effective_user_id'] == os.geteuid()
    assert user_facts['real_group_id'] == os.getgid()
    assert user_facts['effective_group_id'] == os.getgid()

# Generated at 2022-06-13 03:41:01.191621
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user = UserFactCollector()
    collected_facts = {}
    user_facts = user.collect(collected_facts=collected_facts)
    assert isinstance(user_facts, dict)
    assert isinstance(user_facts['user_id'], basestring)
    assert isinstance(user_facts['user_uid'], int)
    assert isinstance(user_facts['user_gid'], int)
    assert isinstance(user_facts['user_gecos'], basestring)
    assert isinstance(user_facts['user_dir'], basestring)
    assert isinstance(user_facts['user_shell'], basestring)
    assert isinstance(user_facts['real_user_id'], int)
    assert isinstance(user_facts['effective_user_id'], int)
   

# Generated at 2022-06-13 03:41:06.472331
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # Instantiating object
    userFactCollectorObject = UserFactCollector()

    # Testing method collect
    # This will return the facts along with the keys ['user_id', 'user_uid', 'user_gid', 'user_gecos', 'user_dir', 'user_shell', 'real_user_id', 'effective_user_id', 'effective_group_ids']
    collected_facts = userFactCollectorObject.collect()
    assert bool(collected_facts) == True
    assert bool(userFactCollectorObject._fact_ids.issubset(collected_facts)) == True

# Generated at 2022-06-13 03:41:15.888337
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    ufc = UserFactCollector()
    module = None
    collected_facts = None
    user_facts = ufc.collect(module, collected_facts)

    assert isinstance(user_facts, dict)
    assert 'user_id' in user_facts.keys()
    assert 'user_uid' in user_facts.keys()
    assert 'user_gid' in user_facts.keys()
    assert 'user_gecos' in user_facts.keys()
    assert 'user_dir' in user_facts.keys()
    assert 'user_shell' in user_facts.keys()
    assert 'real_user_id' in user_facts.keys()
    assert 'effective_user_id' in user_facts.keys()
    assert 'effective_group_ids' in user_facts.keys()

# Generated at 2022-06-13 03:41:20.328069
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    ufc = UserFactCollector()
    res = ufc.collect()
    expected_keys = set(['user_id', 'user_uid', 'user_gid',
                         'user_gecos', 'user_dir', 'user_shell',
                         'real_user_id', 'effective_user_id',
                         'real_group_id', 'effective_group_id'])
    assert res.keys() == expected_keys
    assert isinstance(res['user_uid'], int)
    assert isinstance(res['user_gid'], int)
    assert isinstance(res['user_gecos'], basestring)
    assert isinstance(res['user_dir'], basestring)
    assert isinstance(res['user_shell'], basestring)

# Generated at 2022-06-13 03:41:32.382622
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_facts = UserFactCollector().collect()

    assert isinstance(user_facts, dict), "User facts are not a dict"
    assert 'user_id' in user_facts, "User facts did not contains user id"
    assert 'user_gid' in user_facts, "User facts did not contains user gid"
    assert 'user_gecos' in user_facts, "User facts did not contains user gecos"
    assert 'user_dir' in user_facts, "User facts did not contains user dir"
    assert 'user_shell' in user_facts, "User facts did not contains user shell"
    assert 'real_user_id' in user_facts, "User facts did not contains real user id"
    assert 'effective_user_id' in user_facts, "User facts did not contains effective user id"
   

# Generated at 2022-06-13 03:41:39.966124
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    instance = UserFactCollector()
    assert instance.collect() == {
        'user_id': 'vagrant',
        'user_uid': 1000,
        'user_gid': 1000,
        'user_gecos': 'Vagrant',
        'user_dir': '/home/vagrant',
        'user_shell': '/bin/bash',
        'real_user_id': 1000,
        'effective_user_id': 1000,
        'real_group_id': 1000,
        'effective_group_id': 1000,
    }

# Generated at 2022-06-13 03:42:44.801558
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_facts = UserFactCollector().collect()

    assert user_facts['user_id'] == getpass.getuser()
    assert user_facts['user_uid'] == pwd.getpwnam(getpass.getuser()).pw_uid
    assert user_facts['user_gid'] == pwd.getpwnam(getpass.getuser()).pw_gid
    assert user_facts['user_gecos'] == pwd.getpwnam(getpass.getuser()).pw_gecos
    assert user_facts['user_dir'] == pwd.getpwnam(getpass.getuser()).pw_dir
    assert user_facts['user_shell'] == pwd.getpwnam(getpass.getuser()).pw_shell

# Generated at 2022-06-13 03:42:45.335831
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    pass

# Generated at 2022-06-13 03:42:51.818714
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    users = UserFactCollector()
    result = users.collect()

    # verify return object is dict
    assert isinstance(result, dict)

    # verify return object contains required keys
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

# Generated at 2022-06-13 03:42:57.194315
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    module = DummyModule()
    user_fact_collector = UserFactCollector()
    user_fact_collector.collect(module)
    assert module.exit_args['failed'] == False
    assert isinstance(module.exit_args['ansible_facts'],dict)
    assert 'user_id' in module.exit_args['ansible_facts']
    assert 'user_uid' in module.exit_args['ansible_facts']
    assert 'user_gid' in module.exit_args['ansible_facts']
    assert 'user_gecos' in module.exit_args['ansible_facts']
    assert 'user_dir' in module.exit_args['ansible_facts']
    assert 'user_shell' in module.exit_args['ansible_facts']
    assert 'real_user_id'

# Generated at 2022-06-13 03:43:05.007954
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_fact = UserFactCollector()
    ansible_facts = {}
    user_fact.collect(collected_facts=ansible_facts)

if __name__ == '__main__':
    print('# Unit test for method collect of class UserFactCollector')
    print('# Above code is executed only when this file is run as script')
    print('# Below code is executed only when this file is imported')
    print('# No code is executed when this file is called by other file')
    test_UserFactCollector_collect()

# Generated at 2022-06-13 03:43:09.472856
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    fct_col = UserFactCollector()
    user_facts = fct_col.collect()
    assert user_facts is not None
    assert type(user_facts) is dict
    for f in UserFactCollector._fact_ids:
        if f == 'effective_group_ids':
            assert type(user_facts[f]) is list
        else:
            assert type(user_facts[f]) is int or type(user_facts[f]) is str

# Generated at 2022-06-13 03:43:12.365987
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_fac_col = UserFactCollector()
    user_fac_col.collect()