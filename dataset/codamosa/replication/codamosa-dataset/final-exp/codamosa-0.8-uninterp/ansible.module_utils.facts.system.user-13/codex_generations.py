

# Generated at 2022-06-13 03:33:28.512217
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # instantiate the UserFactCollector class
    userFactCollector = UserFactCollector()

    # invoke the collect method
    user_facts = userFactCollector.collect()

    # assert that the user id is not None
    assert(user_facts['user_id'] is not None)
    # assert that the user uid is not None
    assert(user_facts['user_uid'] is not None)
    # assert that the user gid is not None
    assert(user_facts['user_gid'] is not None)
    # assert that the user gecos is not None
    assert(user_facts['user_gecos'] is not None)
    # assert that the user dir is not None
    assert(user_facts['user_dir'] is not None)
    # assert that the user shell is not None

# Generated at 2022-06-13 03:33:36.201263
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    userFactCollector = UserFactCollector()
    collected_facts = {}
    user_facts = userFactCollector.collect(collected_facts=collected_facts)

    assert user_facts['user_id']
    assert user_facts['user_gid']
    assert user_facts['user_uid']
    assert user_facts['user_gecos']
    assert user_facts['user_dir']
    assert user_facts['user_shell']
    assert user_facts['real_user_id']
    assert user_facts['real_group_id']
    assert user_facts['effective_user_id']
    assert user_facts['effective_group_id']

# Generated at 2022-06-13 03:33:43.511820
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

# Generated at 2022-06-13 03:33:53.147774
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_fact_collector = UserFactCollector()

    assert 'user_id' in user_fact_collector.collect().keys()
    assert 'user_uid' in user_fact_collector.collect().keys()
    assert 'user_gid' in user_fact_collector.collect().keys()
    assert 'user_gecos' in user_fact_collector.collect().keys()
    assert 'user_dir' in user_fact_collector.collect().keys()
    assert 'user_shell' in user_fact_collector.collect().keys()
    assert 'real_user_id' in user_fact_collector.collect().keys()
    assert 'effective_user_id' in user_fact_collector.collect().keys()

# Generated at 2022-06-13 03:33:59.555822
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_collector = UserFactCollector()
    user_facts = user_collector.collect()
    assert user_facts.keys() == set([u'user_id',
                                     u'user_uid',
                                     u'user_gid',
                                     u'user_gecos',
                                     u'user_dir',
                                     u'user_shell',
                                     u'real_user_id',
                                     u'effective_user_id',
                                     u'real_group_id',
                                     u'effective_group_id'])

# Generated at 2022-06-13 03:34:03.911323
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():

    # Create an instance
    user_fact_collector = UserFactCollector()

    # Create a mock class
    class MockModule:
        pass
    mock_module = MockModule()

    # Collect facts
    collected_facts = user_fact_collector.collect(mock_module)

    # Assert that collected facts are not empty
    assert collected_facts


# Generated at 2022-06-13 03:34:09.721067
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    fact_collector = UserFactCollector()
    test_facts = fact_collector.collect()
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

# Generated at 2022-06-13 03:34:17.179604
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():

    ufc = UserFactCollector()
    facts = ufc.collect()

    assert facts['user_id'] == getpass.getuser()
    assert facts['user_uid'] == pwd.getpwnam(getpass.getuser()).pw_uid
    assert facts['user_uid'] == os.getuid()
    assert facts['user_gid'] == pwd.getpwnam(getpass.getuser()).pw_gid
    assert facts['user_gid'] == os.getgid()
    assert facts['user_gecos'] == pwd.getpwnam(getpass.getuser()).pw_gecos
    assert facts['user_dir'] == pwd.getpwnam(getpass.getuser()).pw_dir

# Generated at 2022-06-13 03:34:26.525387
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    mock_module = type('', (), {})()
    mock_module.params = {}

    real_user_id = os.getuid()
    real_group_id = os.getgid()
    user = getpass.getuser()

    user_facts = UserFactCollector().collect(mock_module)

    assert user_facts['real_user_id'] == real_user_id
    assert user_facts['effective_user_id'] == real_user_id
    assert user_facts['real_group_id'] == real_group_id
    assert user_facts['effective_group_id'] == real_group_id

    assert type(user_facts['effective_group_ids']) is list
    assert len(user_facts['effective_group_ids']) > 0

    assert user_facts['user_id']

# Generated at 2022-06-13 03:34:27.327195
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    obj = UserFactCollector()

    assert isinstance(obj.collect(), dict)

# Generated at 2022-06-13 03:34:34.868704
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    import json
    import pytest

    user_facts_collector = UserFactCollector()

    user_facts = user_facts_collector.collect()

    assert type(user_facts) is dict
    assert 'user_id' in user_facts
    assert type(user_facts['user_id']) is str
    assert 'user_gecos' in user_facts
    assert type(user_facts['user_gecos']) is str
    assert 'real_user_id' in user_facts
    assert type(user_facts['real_user_id']) is int
    assert 'effective_user_id' in user_facts
    assert type(user_facts['effective_user_id']) is int
    assert 'real_group_id' in user_facts

# Generated at 2022-06-13 03:34:44.410448
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    """
    Unit test for method collect of class UserFactCollector
    """
    # Instantiate UserFactCollector object
    U = UserFactCollector()
    # Collect fact user_id
    fact_user_id = U.collect(collected_facts=None)['user_id']
    # Via getpass module
    via_getpass_module = getpass.getuser()
    assert fact_user_id == via_getpass_module

    # Collect fact user_uid
    fact_user_uid = U.collect(collected_facts=None)['user_uid']
    # Via getpass module
    via_getpass_module = pwd.getpwuid(os.getuid()).pw_uid
    assert fact_user_uid == via_getpass_module

    # Collect fact user_gid
    fact

# Generated at 2022-06-13 03:34:53.471759
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # Test case when getpass.getuser() raises an Exception in
    # UserFactCollector.__init__()
    user_fact_collector = UserFactCollector()
    user_fact_collector.get_user = lambda : None
    user_fact_collector.get_user_uid = lambda : 1
    user_fact_collector.get_getpwnam = lambda : (1,1,1,1,1,1,1)
    
    result = user_fact_collector.collect()
        

# Generated at 2022-06-13 03:35:01.474368
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # Instantiate an instance
    instance = UserFactCollector()
    response = instance.collect()

    # Verify that the method returns a dictionary
    assert isinstance(response, dict)

    # Verify that the response has the expected values
    assert len(response.keys()) == 9
    assert response['user_id'] == getpass.getuser()
    assert response['real_user_id'] == os.getuid()
    assert response['effective_user_id'] == os.geteuid()

    # Verify that the response doesn't have invalid values
    assert 'invalid_fact_id_1' not in response.keys()
    assert 'invalid_fact_id_2' not in response.keys()
    assert 'invalid_fact_id_3' not in response.keys()

# Generated at 2022-06-13 03:35:12.445467
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    pwd_ob = None
    keys_present = ['user_shell','user_dir','user_gecos','user_uid','user_gid','user_id',
                    'effective_group_id','real_group_id','effective_user_id','real_user_id']
    try:
        user_name = getpass.getuser()
        pwd_ob = pwd.getpwnam(user_name)
    except KeyError:
        pass

    user_facts = {}
    ufc = UserFactCollector()
    user_facts = ufc.collect()

    if pwd_ob is not None:
        assert type(user_facts) == dict
        assert set(user_facts.keys()) == set(keys_present)
        assert user_facts['user_uid'] == pwd_ob.pw_

# Generated at 2022-06-13 03:35:21.294044
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    collector = UserFactCollector(None, None)

    # test_1
    expected = {
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
    actual = collector.collect()
    assert actual == expected

# Generated at 2022-06-13 03:35:30.186189
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_facts_collector = UserFactCollector()
    user_facts = user_facts_collector.collect()
    print("user_facts: %s" % user_facts)
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

# Test for class UserFactCollector

# Generated at 2022-06-13 03:35:32.942611
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    u = UserFactCollector()
    uf = u.collect()
    assert isinstance(uf, dict)
    for k in u._fact_ids:
        assert k in uf


# Generated at 2022-06-13 03:35:45.469737
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():

    import ansible.module_utils.facts.collector as collector

    # Testing of class UserFactCollector without a module
    user_obj = collector.UserFactCollector()

    user_id = getpass.getuser()
    pwent = pwd.getpwnam(getpass.getuser())

    user_facts = user_obj.collect()

    assert user_facts['user_id'] == user_id, \
        "user_id expected: %s, actual: %s" % (user_id, user_facts['user_id'])
    assert user_facts['user_uid'] == pwent.pw_uid, \
        "user_uid expected: %s, actual: %s" % (pwent.pw_uid, user_facts['user_uid'])

# Generated at 2022-06-13 03:35:54.958810
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    import sys
    import os
    import unittest

    class TestFactsModule(object):
        def __init__(self, **kwargs):
            self.params = kwargs

    class TestAnsibleModule(object):
        def __init__(self):
            self.params = {}
            self.exit_json = lambda **kwargs: True

    class TestUserFactCollector(object):
        def __init__(self):
            self.facts_module = TestFactsModule()

    user = UserFactCollector()
    user.collect()
    assert len(user.result) != 0

# Generated at 2022-06-13 03:36:10.876957
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # Creating instance of UserFactCollector class
    ufc = UserFactCollector()

    # Testing for method collect with default value of parameter module and collected_facts
    assert ufc.collect() == {
        'user_id': 'user',
        'user_uid': 1000,
        'user_gid': 1000,
        'user_gecos': 'User,,,',
        'user_dir': '/home/user',
        'user_shell': '/bin/bash',
        'real_user_id': 1000,
        'effective_user_id': 1000,
        'real_group_id': 1000,
        'effective_group_id': 1000
    }

# Generated at 2022-06-13 03:36:21.684054
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_fact_collector = UserFactCollector()
    assert user_fact_collector.collect(collected_facts={})['user_gid'] == pwd.getpwnam(getpass.getuser()).pw_gid
    assert user_fact_collector.collect(collected_facts={})['user_uid'] == pwd.getpwnam(getpass.getuser()).pw_uid
    assert user_fact_collector.collect(collected_facts={})['user_gecos'] == pwd.getpwnam(getpass.getuser()).pw_gecos
    assert user_fact_collector.collect(collected_facts={})['user_dir'] == pwd.getpwnam(getpass.getuser()).pw_dir

# Generated at 2022-06-13 03:36:32.522574
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():

    import time
    import datetime

    os.environ['USER_ID'] = 'my_user'
    os.environ['USER_UID'] = '21'
    os.environ['USER_GID'] = '10'
    os.environ['USER_GECOS'] = 'System User,,,system@localhost'
    os.environ['USER_DIR'] = '/home/system'
    os.environ['USER_SHELL'] = '/bin/bash'
    os.environ['REAL_USER_ID'] = '21'
    os.environ['EFFECTIVE_USER_ID'] = '21'
    os.environ['REAL_GROUP_ID'] = '10'
    os.environ['EFFECTIVE_GROUP_ID'] = '10'


# Generated at 2022-06-13 03:36:37.216605
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # Create an instance of UserFactCollector
    user_collector = UserFactCollector()
    # Collect facts from UserFactCollector
    user_facts = user_collector.collect()
    # Assert if the method collect returned a dict as expected
    assert isinstance(user_facts, dict)
    # Assert if the method collected the expected facts
    for fact in user_collector._fact_ids:
        assert fact in user_facts

# Generated at 2022-06-13 03:36:45.168204
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_facts = UserFactCollector()
    collected_facts = {}
    expected_result = {'effective_group_id': 1000,
                       'effective_user_id': 1000,
                       'real_group_id': 1000,
                       'real_user_id': 1000,
                       'user_dir': '/home/wczech',
                       'user_gid': 1000,
                       'user_gecos': 'wczech,,,',
                       'user_id': 'wczech',
                       'user_shell': '/bin/bash',
                       'user_uid': 1000}
    result = user_facts.collect(collected_facts)
    assert expected_result == result

# Generated at 2022-06-13 03:36:55.742692
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    gecos = pwd.getpwnam(getpass.getuser()).pw_gecos
    userdir = pwd.getpwnam(getpass.getuser()).pw_dir
    usershell = pwd.getpwnam(getpass.getuser()).pw_shell
    uid = os.getuid()
    euid = os.geteuid()
    gid = os.getgid()
    egid = os.getgid()
    user_id = getpass.getuser()
    real_user_id = os.getuid()

    # test
    ansible_user = UserFactCollector()
    result_user = ansible_user.collect()

    assert result_user['user_id'] == user_id

# Generated at 2022-06-13 03:37:02.998226
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # Patch pwd.getpwnam method
    import mock
    import pwd
    def getpwnam(user):
        return type('pwent', (object,), {'pw_uid': 1000,
                                         'pw_gid': 1000,
                                         'pw_gecos': 'gecos value',
                                         'pw_dir': '/home/user',
                                         'pw_shell': '/bin/bash'})()
    pwd.getpwnam = mock.MagicMock(side_effect=getpwnam)

    # Patch pwd.getpwuid method

# Generated at 2022-06-13 03:37:14.379084
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # Initialize the instance of the class UserFactCollector
    u = UserFactCollector()

    # Collect facts
    facts = u.collect()

    # Assert user_id is a string
    assert isinstance(facts['user_id'], str)

    # Assert user_uid is integer
    assert isinstance(facts['user_uid'], int)

    # Assert user_gid is integer
    assert isinstance(facts['user_gid'], int)

    # Assert user_gecos is a string
    assert isinstance(facts['user_gecos'], str)

    # Assert user_dir is a string
    assert isinstance(facts['user_dir'], str)

    # Assert user_shell is a string
    assert isinstance(facts['user_shell'], str)

    # Assert real

# Generated at 2022-06-13 03:37:17.226751
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    userfactcollector = UserFactCollector()
    user_facts = userfactcollector.collect()
    assert user_facts['user_id'] == getpass.getuser()

# Generated at 2022-06-13 03:37:23.816521
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    ufc = UserFactCollector()
    collected_facts = {}

    collected_facts = ufc.collect(collected_facts=collected_facts)

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

# Generated at 2022-06-13 03:37:47.806196
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_facts = UserFactCollector()
    facts = user_facts.collect()
    assert facts['user_id'] == getpass.getuser()
    assert facts['user_uid'] == pwd.getpwuid(os.getuid()).pw_uid
    assert facts['user_gid'] == pwd.getpwuid(os.getuid()).pw_gid
    assert facts['user_gecos'] == pwd.getpwuid(os.getuid()).pw_gecos
    assert facts['user_dir'] == pwd.getpwuid(os.getuid()).pw_dir
    assert facts['user_shell'] == pwd.getpwuid(os.getuid()).pw_shell
    assert facts['real_user_id'] == os.getuid()
   

# Generated at 2022-06-13 03:37:58.162877
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    userObj = UserFactCollector()
    user_facts = userObj.collect()
    assert(user_facts.get('user_id'))
    assert(user_facts.get('user_uid'))
    assert(user_facts.get('user_gid'))
    assert(user_facts.get('user_gecos'))
    assert(user_facts.get('user_dir'))
    assert(user_facts.get('user_shell'))
    assert(user_facts.get('real_user_id'))
    assert(user_facts.get('effective_user_id'))
    assert(user_facts.get('real_group_id'))
    assert(user_facts.get('effective_group_id'))

# Generated at 2022-06-13 03:38:06.307936
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():

    # This is a simple unit test using the test fixture.
    # We could test the real_user_id and effective_user_id, but
    # that's not a good idea, because people may run the tests
    # as root. We are just making sure that the keys are in the
    # result.

    result = UserFactCollector().collect()

    assert(result['user_id'] != None)
    assert(result['user_uid'] != None)
    assert(result['user_gid'] != None)
    assert(result['user_gecos'] != None)
    assert(result['user_dir'] != None)
    assert(result['user_shell'] != None)
    assert(result['real_user_id'] != None)
    assert(result['effective_user_id'] != None)

# Generated at 2022-06-13 03:38:07.628440
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_facts = UserFactCollector().collect()
    assert 'ansible_facts' in user_facts

# Generated at 2022-06-13 03:38:14.365523
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # Setting up
    user_fact_collector = UserFactCollector()
    user_fact_collector.name = 'user'
    user_fact_collector._fact_ids = set(['user_id', 'user_uid', 'user_gid',
                                         'user_gecos', 'user_dir', 'user_shell'])

    # Testing
    user_facts = user_fact_collector.collect()

    # Validations
    assert user_facts['user_id']
    assert user_facts['user_uid']
    assert user_facts['user_gid']
    assert user_facts['user_gecos']
    assert user_facts['user_shell']
    assert user_facts['user_dir']

# Generated at 2022-06-13 03:38:21.730662
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    x = UserFactCollector()
    facts = x.collect()
    assert facts['user_id'] == getpass.getuser()
    assert facts['user_gid'] == os.getgid()
    assert facts['user_gecos'] == pwd.getpwuid(os.getuid()).pw_gecos
    assert facts['user_shell'] == pwd.getpwuid(os.getuid()).pw_shell

# Generated at 2022-06-13 03:38:32.236483
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():

    # Create a instance of UserFactCollector class
    u = UserFactCollector()

    # Create a dictionary with minimal collected_facts
    collected_facts = {}

    # Call method collect of UserFactCollector class
    result = u.collect(collected_facts=collected_facts)

    # Assert if the result is not None
    assert result is not None

    # Assert if the result is a dictionary
    assert isinstance(result, dict)

    # Assert if the result is as expected with user_id
    assert result['user_id'] == collected_facts['user_id']

    # Assert if the result is as expected with user_uid
    assert result['user_uid'] == collected_facts['user_uid']

    # Assert if the result is as expected with user_gid
    assert result['user_gid']

# Generated at 2022-06-13 03:38:34.526966
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    collect_facts = UserFactCollector()
    ansible_facts = collect_facts.collect()
    assert ansible_facts['user_id'] == 'root'

# Generated at 2022-06-13 03:38:37.483976
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # Create an instance of UserFactCollector
    ufc = UserFactCollector()

    # Call method collect
    ufc.collect()

# Generated at 2022-06-13 03:38:48.298205
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # Reference data for test
    reference_keys = set(['user_id', 'user_uid', 'user_gid',
                          'user_gecos', 'user_dir', 'user_shell',
                          'real_user_id', 'effective_user_id',
                          'real_group_id', 'effective_group_id'])

    user_facts = UserFactCollector().collect()
    assert len(user_facts.keys()) == len(reference_keys)
    assert user_facts['user_id']
    assert user_facts['user_uid']
    assert user_facts['user_gid']
    assert user_facts['user_gecos']
    assert user_facts['user_dir']
    assert user_facts['user_shell']
    assert user_facts['real_user_id']

# Generated at 2022-06-13 03:39:15.656864
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    fact_collector = UserFactCollector()
    fact_collector.collect()
    assert set(fact_collector.get_facts().keys()) == fact_collector._fact_ids

# Generated at 2022-06-13 03:39:18.981575
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    fact_collector = UserFactCollector()
    fact_collector.collect()
    assert isinstance(fact_collector._fact_data, dict)
    assert len(fact_collector._fact_data) == 8

# Generated at 2022-06-13 03:39:19.837616
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    assert False

# Generated at 2022-06-13 03:39:27.186998
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_fact_collector = UserFactCollector()
    user_facts = user_fact_collector.collect()
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


# Generated at 2022-06-13 03:39:34.826168
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():

    # Create UserFactCollector instance
    user_fc = UserFactCollector()
    
    # The actual collect function is tested in the test/units/plugins/facts/test_user.py script.
    # So we just make sure that it's called and gets the module variable.
    def fake_collect(module=None, collected_facts=None):
        assert module == "Module variable"
        return {}

    user_fc.collect = fake_collect

    assert user_fc.collect("Module variable") == {}

# Generated at 2022-06-13 03:39:41.556848
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_facts = UserFactCollector().collect()

    assert user_facts['user_id'] is not None
    assert user_facts['user_uid'] is not None
    assert user_facts['user_gid'] is not None
    assert user_facts['user_dir'] is not None
    assert user_facts['user_shell'] is not None
    assert user_facts['real_user_id'] is not None
    assert user_facts['effective_user_id'] is not None
    assert user_facts['real_group_id'] is not None
    assert user_facts['effective_group_id'] is not None

# Generated at 2022-06-13 03:39:42.318031
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    UserFactCollector().collect()

# Generated at 2022-06-13 03:39:52.861506
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    import subprocess
    import sys

    # get UID of default non-root user
    default_user = subprocess.check_output('whoami', shell=True).strip()
    default_uid = subprocess.check_output("id -u %s" % default_user, shell=True).strip()
    default_gid = subprocess.check_output("id -g %s" % default_user, shell=True).strip()
    default_gecos = subprocess.check_output("getent passwd %s | cut -d: -f5" % default_user, shell=True).strip()
    default_dir = subprocess.check_output("getent passwd %s | cut -d: -f6" % default_user, shell=True).strip()

# Generated at 2022-06-13 03:40:00.321410
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_facts = UserFactCollector.collect()
    assert(type(user_facts['user_id']) == str)
    assert(type(user_facts['user_uid']) == int)
    assert(type(user_facts['user_gid']) == int)
    assert(type(user_facts['user_gecos']) == str)
    assert(type(user_facts['user_dir']) == str)
    assert(type(user_facts['user_shell']) == str)
    assert(type(user_facts['real_user_id']) == int)
    assert(type(user_facts['effective_user_id']) == int)

# Generated at 2022-06-13 03:40:09.590116
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():

    user_facts = {'user_id': 'testuser', 'user_uid': 1000, 'user_gid': 1000,
                  'user_gecos': 'Test User,,,', 'user_dir': '/home/testuser',
                  'user_shell': '/bin/bash', 'real_user_id': 1000,
                  'effective_user_id': 1000, 'effective_group_ids': [1000],
                  'real_group_id': 1000}

    test_collector = UserFactCollector()
    result = test_collector.collect()
    assert result == user_facts

# Generated at 2022-06-13 03:40:36.547100
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    pass

# Generated at 2022-06-13 03:40:38.007934
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
  ufc = UserFactCollector()
  ufc.collect()

# Generated at 2022-06-13 03:40:46.354418
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    test_obj = UserFactCollector('system')
    result = test_obj.collect()
    assert Set(result.keys()) == test_obj._fact_ids
    assert result['user_id'] == getpass.getuser()
    assert result['real_user_id'] == os.getuid()
    assert result['effective_user_id'] == os.geteuid()
    assert result['real_group_id'] == os.getgid()
    assert result['effective_group_id'] == os.getgid()
    print('Result Test: {}'.format(result))


# Generated at 2022-06-13 03:40:47.517663
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    fact_collector = UserFactCollector()
    fact_collector.collect()

# Generated at 2022-06-13 03:40:53.625134
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_facts = UserFactCollector().collect()
    assert user_facts['user_id'] == getpass.getuser()
    assert user_facts['effective_user_id'] == os.geteuid()
    assert user_facts['real_user_id'] == os.getuid()
    assert user_facts['effective_group_id'] == os.getgid()
    assert user_facts['real_group_id'] == os.getgid()

# Generated at 2022-06-13 03:40:54.459706
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    c = UserFactCollector()
    c.collect()

# Generated at 2022-06-13 03:40:56.760463
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_fact_collector = UserFactCollector()
    user_facts = user_fact_collector.collect()
    assert(user_facts['user_id'] == getpass.getuser())

# Generated at 2022-06-13 03:41:02.185873
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    userf = UserFactCollector()
    assert(userf.collect()['user_id'] == getpass.getuser())
    assert(userf.collect()['user_uid'] == os.getuid())
    assert(userf.collect()['user_gid'] == os.getgid())
    assert(userf.collect()['user_gecos'] == pwd.getpwnam(userf.collect()['user_id']).pw_gecos)
    assert(userf.collect()['user_dir'] == pwd.getpwnam(userf.collect()['user_id']).pw_dir)
    assert(userf.collect()['user_shell'] == pwd.getpwnam(userf.collect()['user_id']).pw_shell)

# Generated at 2022-06-13 03:41:12.834586
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_info = {
        'user_id': 'wangy',
        'user_uid': 1001,
        'user_gid': 1001,
        'user_gecos': 'wangy',
        'user_dir': '/home/wangy',
        'user_shell': '/bin/bash',
        'real_user_id': 1001,
        'effective_user_id': 1001,
        'effective_group_ids': [1001,1002],
    }

    class mockModule:
        def __init__(self):
            self.params = {}

    class mockFacts:
        pass

    user_fact_check = UserFactCollector()
    user_fact_check.collect(mockModule(), mockFacts)
    current_user_info = user_fact_check.collect_fn()



# Generated at 2022-06-13 03:41:18.049892
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    collector = UserFactCollector()
    result = collector.collect()
    assert result
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


# Generated at 2022-06-13 03:42:20.947215
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_fact_collector = UserFactCollector()
    res_facts = user_fact_collector.collect()
    assert res_facts['user_id'] == getpass.getuser()
    assert res_facts['user_uid'] == pwd.getpwuid(os.getuid()).pw_uid
    assert res_facts['user_gid'] == pwd.getpwuid(os.getuid()).pw_gid
    assert res_facts['user_gecos'] == pwd.getpwuid(os.getuid()).pw_gecos
    assert res_facts['user_dir'] == pwd.getpwuid(os.getuid()).pw_dir
    assert res_facts['user_shell'] == pwd.getpwuid(os.getuid()).pw_

# Generated at 2022-06-13 03:42:22.053038
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    obj = UserFactCollector()
    obj.collect()
    return True

# Generated at 2022-06-13 03:42:26.170524
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_facts = {}
    try:
        ufc = UserFactCollector()
        user_facts = ufc.collect()
    except Exception as e:
        print('Unable to collect facts for user, error raised: ' + str(e))
    finally:
        for fact_id in ufc._fact_ids:
            print('Collecting user fact ' + fact_id + ' with value ' + str(user_facts.get(fact_id)))

# Generated at 2022-06-13 03:42:27.740328
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user = UserFactCollector()
    user_facts = user.collect()
    print(user_facts)

if __name__ == '__main__':
    test_UserFactCollector_collect()

# Generated at 2022-06-13 03:42:28.312426
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    pass

# Generated at 2022-06-13 03:42:39.175751
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_facts_collector = UserFactCollector()
    user_facts = user_facts_collector.collect()
    assert isinstance(user_facts, dict)
    assert 'user_id' in user_facts
    assert isinstance(user_facts['user_id'], basestring)
    assert 'user_uid' in user_facts
    assert isinstance(user_facts['user_uid'], int)
    assert 'user_gid' in user_facts
    assert isinstance(user_facts['user_gid'], int)
    assert 'user_gecos' in user_facts
    assert isinstance(user_facts['user_gecos'], basestring)
    assert 'user_dir' in user_facts
    assert isinstance(user_facts['user_dir'], basestring)

# Generated at 2022-06-13 03:42:43.671473
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    ufc = UserFactCollector()
    assert ufc.name == 'user'
    assert len(ufc._fact_ids) == 10
    ufc2 = UserFactCollector()
    assert ufc._fact_ids == ufc2._fact_ids

# Generated at 2022-06-13 03:42:49.976095
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_facts = {
        'effective_group_id': 1000,
        'effective_user_id': 1000,
        'user_dir': '/home/example_user',
        'user_gecos': 'example_user',
        'user_gid': 1000,
        'user_id': 'example_user',
        'user_shell': '/bin/zsh',
        'user_uid': 1000,
        'real_group_id': 1000,
        'real_user_id': 1000
    }

    collector = UserFactCollector()
    result = collector.collect()

    assert result == user_facts

# Generated at 2022-06-13 03:42:51.277289
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    ufc = UserFactCollector()
    assert ufc.collect()['user_id'] == getpass.getuser()

# Generated at 2022-06-13 03:42:56.315531
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    test_user_fact_collector = UserFactCollector()
    test_collected_facts = {'some_fact': 'some_value'}
    result = test_user_fact_collector.collect(collected_facts=test_collected_facts)
    for key in test_user_fact_collector._fact_ids:
        if key == "real_user_id":
            assert os.getuid() == result[key]
        elif key == "effective_user_id":
            assert os.geteuid() == result[key]
        elif key == "real_group_id":
            assert os.getgid() == result[key]
        elif key == "effective_group_id":
            assert os.getegid() == result[key]
        else:
            assert key in result
   