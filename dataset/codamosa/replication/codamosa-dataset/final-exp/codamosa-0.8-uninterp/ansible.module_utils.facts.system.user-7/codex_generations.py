

# Generated at 2022-06-13 03:33:27.089535
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user = UserFactCollector()
    user_facts = user.collect()

    expected_keys = ['user_id', 'user_uid', 'user_gid',
                     'user_gecos', 'user_dir', 'user_shell',
                     'real_user_id', 'effective_user_id',
                     'real_group_id', 'effective_group_id']

    assert set(user_facts) == set(expected_keys)
    assert type(user_facts['user_id']) == str
    assert type(user_facts['user_uid']) == int
    assert type(user_facts['user_gid']) == int
    assert type(user_facts['user_gecos']) == str
    assert type(user_facts['user_dir']) == str

# Generated at 2022-06-13 03:33:29.541438
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():

    user_facts = UserFactCollector()
    collected_facts = user_facts.collect()

    assert isinstance(collected_facts,dict)
    for key in user_facts._fact_ids:
        assert key in collected_facts

# Generated at 2022-06-13 03:33:31.690436
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    u = UserFactCollector()
    user_facts = u.collect(collected_facts=None)
    assert isinstance(user_facts, dict)

# Generated at 2022-06-13 03:33:33.209818
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    data = UserFactCollector.collect()
    assert data['user_id'] == getpass.getuser()

# Generated at 2022-06-13 03:33:37.340521
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_fact_collector = UserFactCollector()
    user_facts = user_fact_collector.collect()
    assert isinstance(user_facts, dict)
    assert user_facts['real_user_id'] == os.getuid()
    assert user_facts['effective_user_id'] == os.geteuid()
    assert user_facts['effective_group_id'] == os.getgid()

# Generated at 2022-06-13 03:33:47.195158
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    collector = UserFactCollector()
    collected_facts = collector.collect()

# Generated at 2022-06-13 03:33:54.570902
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # Create an object of UserFactCollector
    user_fact_collector = UserFactCollector()

    # Call method collect
    collected_facts = user_fact_collector.collect()

    # Assert that method collect returned a dictionary
    assert isinstance(collected_facts, dict)

    # Assert that method collect returned the correct facts
    assert collected_facts['user_id'] == getpass.getuser()
    assert collected_facts['real_user_id'] ==  os.getuid()
    assert collected_facts['effective_user_id'] == os.geteuid()

# Generated at 2022-06-13 03:34:00.937923
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # initialize the object, with no parameter
    collector = UserFactCollector()
    # call the method with no parameter, returns the module facts
    result = collector.collect()
    # the returned result should be a dictionary with all the facts of this module
    assert result == { 'effective_user_id': 0, 'user_gecos': 'root', 'effective_group_id': 0, 'user_id': 'root', 'user_uid': 0, 'real_user_id': 0, 'user_dir': '/root', 'user_gid': 0, 'user_shell': '/bin/bash', 'real_group_id': 0 }

# Generated at 2022-06-13 03:34:02.548999
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    new_collection_method = UserFactCollector()
    new_collection_method.collect()


# Generated at 2022-06-13 03:34:13.108157
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():

    class Object(object):
        def __init__(self, **kwargs):
            for k,v in kwargs.items():
                setattr(self, k, v)

    import getpass
    import os
    import pwd
    import pytest

    fc = UserFactCollector()

    username = getpass.getuser()
    uid = os.getuid()
    gid = os.getgid()

    try:
        pwent = pwd.getpwnam(username)
    except KeyError:
        pwent = pwd.getpwuid(os.getuid())

    # collect method should return a dict
    assert isinstance(fc.collect(), dict)
    # the dict should have a 'user_id' key
    assert 'user_id' in fc.collect()
    # the

# Generated at 2022-06-13 03:34:25.118404
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_fact_collector = UserFactCollector()
    user_facts = user_fact_collector.collect()

    assert user_facts['user_id'] is not None
    assert user_facts['user_uid'] == os.getuid()
    assert user_facts['user_gid'] == os.getgid()
    assert user_facts['user_gecos'] is not None
    assert user_facts['user_dir'] is not None
    assert user_facts['user_shell'] is not None
    assert user_facts['real_user_id'] == os.getuid()
    assert user_facts['effective_user_id'] == os.geteuid()


# Generated at 2022-06-13 03:34:30.552272
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_collector = UserFactCollector()
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
    user_facts

# Generated at 2022-06-13 03:34:39.321636
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    collector = UserFactCollector()
    result = collector.collect()

    # Check the result got from user fact collector
    assert result['user_id'] == getpass.getuser()
    assert result['user_uid'] == os.getuid()
    assert result['user_gid'] == os.getgid()
    assert result['real_user_id'] == os.getuid()
    assert result['effective_user_id'] == os.geteuid()
    assert result['real_group_id'] == os.getgid()
    assert result['effective_group_id'] == os.getgid()

# Generated at 2022-06-13 03:34:46.154875
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
	# Create an instance of UserFactCollector with default values
	user_fact_collector = UserFactCollector()

	# Return a dict of user facts for the current user
	user_facts = user_fact_collector.collect()

	# Assert all of the facts are found
	for user_fact in user_fact_collector._fact_ids:
		assert user_fact in user_facts, \
			'User fact "{}" not found in user_facts'.format(user_fact)
		assert user_fact not in user_facts.values(), \
			'User fact "{}" is incorrect in user_facts'.format(user_fact)


# Generated at 2022-06-13 03:34:55.883823
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    from ansible.module_utils.facts.collectors import UserFactCollector
    from ansible.module_utils.facts.collector import FactsCollector
    import ansible.module_utils.facts.collectors as collectors
    ufc = UserFactCollector()
    fc = FactsCollector()
    fc.add_collection(ufc)
    collected_facts = fc.collect(module=None, collected_facts=None)
    if collected_facts['user'] is None:
        raise AssertionError
    print("user_id: " + collected_facts['user']['user_id'])
    print("user_uid: " + str(collected_facts['user']['user_uid']))

# Generated at 2022-06-13 03:34:57.490934
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    ufc = UserFactCollector()
    assert set(ufc.collect().keys()) == ufc._fact_ids

# Generated at 2022-06-13 03:35:06.731891
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    U = UserFactCollector

    # before verifying that actual user is not root,
    # we'll make sure that UserFactCollector.collect
    # works on root as well.
    assert U().collect()['real_user_id'] == 0

    if getpass.getuser() != 'root':
        # real
        assert U().collect()['real_user_id'] == os.getuid()

        # effective
        try:
            os.seteuid(0)
            assert U().collect()['effective_user_id'] == 0
        except OSError:
            pass

# Generated at 2022-06-13 03:35:09.444976
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    ufc = UserFactCollector()
    # TODO: add test cases


# Generated at 2022-06-13 03:35:13.815799
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_collector = UserFactCollector()
    result = user_collector.collect()
    assert result is not None
    assert sorted(result.keys()) == ['effective_group_id', 'effective_user_id', 'real_group_id', 'real_user_id', 'user_dir', 'user_gecos', 'user_gid', 'user_id', 'user_shell', 'user_uid']

# Generated at 2022-06-13 03:35:23.331707
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    from ansible.module_utils.facts import collector

    collector.collectors['user'] = UserFactCollector()

    results = collector._collect_all_facts(dict(user={}))

    assert results['user_id'] == getpass.getuser()
    assert results['user_uid'] == os.getuid()
    assert results['user_gid'] == os.getgid()
    assert results['real_user_id'] == os.getuid()
    assert results['effective_user_id'] == os.geteuid()
    assert results['real_group_id'] == os.getgid()
    assert results['effective_group_id'] == os.getegid()

# Generated at 2022-06-13 03:35:41.934824
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

# Generated at 2022-06-13 03:35:45.250810
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    UserFactCollector = UserFactCollector()
    collected_facts = UserFactCollector.collect()
    assert collected_facts['user_id'] == getpass.getuser()


# Generated at 2022-06-13 03:35:50.413512
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_coll = UserFactCollector()
    user_facts = user_coll.collect()
    assert user_facts['user_id'] == getpass.getuser()
    assert user_facts['user_uid'] == os.getuid()

# Run the unit tests
if __name__ == '__main__':
    test_UserFactCollector_collect()

# Generated at 2022-06-13 03:36:00.729356
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    module = None
    collected_facts = None
    user_facts = {}
    user_facts['user_id'] = getpass.getuser()
    user_facts['user_uid'] = None
    user_facts['user_gid'] = None
    user_facts['user_gecos'] = None
    user_facts['user_dir'] = None
    user_facts['user_shell'] = None
    user_facts['real_user_id'] = None
    user_facts['effective_user_id'] = None
    user_facts['real_group_id'] = None
    user_facts['effective_group_id'] = None


# Generated at 2022-06-13 03:36:11.910624
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # Expected results
    expected_user_id = getpass.getuser()
    try:
        pwent = pwd.getpwnam(getpass.getuser())
    except KeyError:
        pwent = pwd.getpwuid(os.getuid())
    expected_user_uid = pwent.pw_uid
    expected_user_gid = pwent.pw_gid
    expected_user_gecos = pwent.pw_gecos
    expected_user_dir = pwent.pw_dir
    expected_user_shell = pwent.pw_shell
    expected_real_user_id = os.getuid()
    expected_effective_user_id = os.geteuid()
    expected_real_group_id = os.getgid()
    expected_effective_group

# Generated at 2022-06-13 03:36:22.944566
# Unit test for method collect of class UserFactCollector

# Generated at 2022-06-13 03:36:33.747372
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    """
    Unit test for UserFactCollector.collect()
    """

    upw = pwd.getpwuid(os.getuid())

    user_fact_collector = UserFactCollector()
    result = user_fact_collector.collect()

# Generated at 2022-06-13 03:36:36.451198
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    """Unit test for method collect of class UserFactCollector
    """
    # Define a class instance
    obj = UserFactCollector()

    # Check type of output
    assert isinstance(obj.collect(), dict)


# Generated at 2022-06-13 03:36:39.324304
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # Setup
    test_obj = UserFactCollector()

    # Exercise
    result = test_obj.collect()

    # Verify
    assert isinstance(result, dict)

# Generated at 2022-06-13 03:36:47.338704
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    collector = UserFactCollector()
    result = collector.collect()


# Generated at 2022-06-13 03:37:11.603357
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    import tempfile
    import shutil
    import os

    # Create a temporary directory
    tmpdir = tempfile.mkdtemp()

    # Create a test ansible.cfg config file
    path = os.path.join(tmpdir, "ansible.cfg")
    with open(path, 'w') as f:
        f.write('[defaults]\n')

    # Set the ANSIBLE_CONFIG env variable to point to the test ansilbe.cfg config file
    os.environ['ANSIBLE_CONFIG'] = path

    # Create a UserFactCollector instance
    ufc = UserFactCollector()

    # Create an empty collected_facts
    collected_facts = {}

    # Test the collect method
    ufc.collect(collected_facts=collected_facts)

    # Test that collected_facts is correct

# Generated at 2022-06-13 03:37:21.676576
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    import os
    import pwd
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collectors.system.user import UserFactCollector
    user_id = pwd.getpwuid(os.getuid()).pw_name
    user_uid = pwd.getpwuid(os.getuid()).pw_uid
    user_gid = pwd.getpwuid(os.getuid()).pw_gid
    user_gecos = pwd.getpwuid(os.getuid()).pw_gecos
    user_dir = pwd.getpwuid(os.getuid()).pw_dir
    user_shell = pwd.getpwuid(os.getuid()).pw_shell


# Generated at 2022-06-13 03:37:31.652862
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    expected_keys = ['user_id', 'user_uid', 'user_gid', 'user_gecos',
                     'user_dir', 'user_shell', 'real_user_id',
                     'effective_user_id', 'real_group_id',
                     'effective_group_id']

    dummy_module = None
    dummy_collected_facts = None

    fact_collector = UserFactCollector(dummy_module, dummy_collected_facts)
    fact_collector._collect()

    # verify the collected facts
    assert fact_collector.collected_facts.keys() == expected_keys


# Generated at 2022-06-13 03:37:34.965809
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_facts = UserFactCollector().collect()
    assert type(user_facts) == dict
    assert user_facts['user_id'] == getpass.getuser()
    assert user_facts['user_uid'] == pwd.getpwuid(os.getuid()).pw_uid
    assert user_facts['user_gid'] == pwd.getpwuid(os.getuid()).pw_gid
    assert user_facts['user_gecos'] == pwd.getpwuid(os.getuid()).pw_gecos
    assert user_facts['user_dir'] == pwd.getpwuid(os.getuid()).pw_dir
    assert user_facts['user_shell'] == pwd.getpwuid(os.getuid()).pw_shell
    assert user

# Generated at 2022-06-13 03:37:46.789301
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    #mock_module = MagicMock()
    #mock_module.params = {}
    #mock_module.params['gather_subset'] = []
    #mock_module.params['gather_timeout'] = 10
    collected_facts = {}

    #uc = UserFactCollector(module=mock_module, collected_facts=collected_facts)

    # expected_facts = {'effective_group_id': 1000,
    #                   'effective_group_ids': [1000],
    #                   'effective_user_id': 1000,
    #                   'real_user_id': 1000, 'user_dir': '/home/xxxx',
    #                   'user_gecos': 'test user', 'user_gid': 1000,
    #                   'user_id': 'xxxx', 'user_shell': '/bin/

# Generated at 2022-06-13 03:37:57.473829
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():

    # Create an instance of class UserFactCollector
    user_collector = UserFactCollector()

    # Get required data from class
    user_uid = user_collector.get_required_data('user_uid')
    user_gid = user_collector.get_required_data('user_gid')
    user_gecos = user_collector.get_required_data('user_gecos')
    user_dir = user_collector.get_required_data('user_dir')
    user_shell = user_collector.get_required_data('user_shell')
    real_user_id = user_collector.get_required_data('real_user_id')
    effective_user_id = user_collector.get_required_data('effective_user_id')
    real_group_id = user

# Generated at 2022-06-13 03:38:02.996906
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    ufc = UserFactCollector()
    output = ufc.collect()
    assert isinstance(output, dict)
    assert 'user_id' in output
    assert 'user_uid' in output
    assert 'user_gid' in output
    assert 'user_gecos' in output
    assert 'user_dir' in output
    assert 'user_shell' in output
    assert 'real_user_id' in output
    assert 'effective_user_id' in output

# Generated at 2022-06-13 03:38:04.881615
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # For coverage, call method collect of class UserFactCollector
    UserFactCollector().collect()

if __name__ == '__main__':
    test_UserFactCollector_collect()

# Generated at 2022-06-13 03:38:10.338377
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    """
    Unit test for the method collect of the class UserFactCollector
    """
    obj = UserFactCollector()
    result = obj.collect()
    assert isinstance(result, dict), 'Should return a dict'

    # Ensure we have the expected keys
    keys = ['user_id', 'user_uid', 'user_gid', 'user_gecos',
            'user_dir', 'user_shell', 'real_user_id', 'effective_user_id',
            'real_group_id', 'effective_group_id']
    for key in keys:
        assert key in result, 'Result should contain %s' % key

    # Ensure we have the same user_id, effective_user_id, real_user_id

# Generated at 2022-06-13 03:38:15.657391
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_facts = UserFactCollector().collect()
    assert user_facts['user_id'] != ''
    assert user_facts['user_uid'] != ''
    assert user_facts['user_gid'] != ''
    assert user_facts['user_gecos'] != ''
    assert user_facts['user_dir'] != ''
    assert user_facts['user_shell'] != ''
    assert user_facts['real_user_id'] != ''
    assert user_facts['effective_user_id'] != ''
    assert user_facts['real_group_id'] != ''
    assert user_facts['effective_group_id'] != ''

# Generated at 2022-06-13 03:38:54.775296
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # Create an instance of class UserFactCollector
    userFactCollector = UserFactCollector()
    # Call the collect method
    user_facts = userFactCollector.collect()
    # Assert that the type of the return value is a dictionary
    assert isinstance(user_facts, dict)
    # Assert that each fact is in the dictionary
    assert 'user_id' in user_facts
    assert 'user_uid' in user_facts
    assert 'user_gid' in user_facts
    assert 'user_gecos' in user_facts
    assert 'user_dir' in user_facts
    assert 'user_shell' in user_facts
    assert 'real_user_id' in user_facts
    assert 'effective_user_id' in user_facts
    assert 'effective_group_id' in user_facts


# Generated at 2022-06-13 03:39:02.313957
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_facts = UserFactCollector().collect()

    assert user_facts['user_id'] == getpass.getuser()
    assert user_facts['user_uid'] == os.getuid()
    assert user_facts['user_gid'] == os.getgid()
    assert user_facts['user_shell'] is not None
    assert user_facts['user_dir'] is not None
    assert user_facts['user_gecos'] is not None
    assert user_facts['real_user_id'] == os.getuid()
    assert user_facts['real_group_id'] == os.getgid()
    assert user_facts['effective_user_id'] == os.geteuid()
    assert user_facts['effective_group_id'] == os.getegid()

# Generated at 2022-06-13 03:39:03.818299
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    ufc = UserFactCollector()
    assert ufc.collect()

# Generated at 2022-06-13 03:39:11.651370
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    collector = UserFactCollector()
    assert collector.collect() == {
        'user_id': 'vagrant',
        'user_uid': 1000,
        'user_gid': 1000,
        'user_gecos': 'vagrant,,,',
        'user_dir': '/home/vagrant',
        'user_shell': '/bin/bash',
        'real_user_id': 1000,
        'effective_user_id': 1000,
        'real_group_id': 1000,
        'effective_group_id': 1000}


# Generated at 2022-06-13 03:39:22.622388
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    from unit.modules.utils import set_module_args
    from ansible.module_utils.facts import ansible_facts
    user_info = ansible_facts['ansible_user_id']
    module = FakeModule()
    set_module_args(module)
    fact_collector = UserFactCollector()
    fact_collector.collect(module=module, collected_facts=ansible_facts)
    current_user = getpass.getuser()
    assert type(ansible_facts['ansible_user_id']) is dict
    assert type(ansible_facts['ansible_user_id']) is not None
    assert ansible_facts['ansible_user_id']['user_id'] == user_info['user_id']

# Generated at 2022-06-13 03:39:29.258404
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    '''
    Unit test for method collect of class UserFactCollector
    '''
    from ansible.module_utils.facts import processor
    from ansible.module_utils.facts.processor import FactsCollector
    from ansible.module_utils.facts.collector import add_collector

    user_collector = UserFactCollector()
    add_collector(user_collector)

    facts_collector = FactsCollector()
    facts_collector.collect(module=None, collected_facts={})

    facts = facts_collector.read_facts()
    assert isinstance(facts, dict)
    assert 'user_id' in facts.keys()
    assert 'user_uid' in facts.keys()
    assert 'user_gid' in facts.keys()
    assert 'user_gecos' in facts.keys()

# Generated at 2022-06-13 03:39:39.627219
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # Arrange
    import unittest.mock as mock

    expected_result = {
        'user_id': 'test',
        'user_uid': 0,
        'user_gid': 0,
        'user_gecos': 'gecos',
        'user_dir': '/home/test',
        'user_shell': '/bin/sh',
        'real_user_id': 0,
        'effective_user_id': 0,
        'real_group_id': 0,
        'effective_group_id': 0
    }

    # Mock pwd.getpwnam and pwd.getpwuid
    mock_user = mock.MagicMock(**expected_result)
    mock_pwd = mock.MagicMock()
    mock_pwd.getpwnam.return_value = mock

# Generated at 2022-06-13 03:39:44.845024
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    # Test real user
    collector = UserFactCollector()
    user_facts = collector.collect()
    assert user_facts['user_id'] == getpass.getuser()
    assert user_facts['user_uid'] == os.getuid()
    assert user_facts['user_gid'] == os.getgid()
    assert user_facts['user_gecos'] == pwd.getpwuid(os.getuid()).pw_gecos
    assert user_facts['user_dir'] == pwd.getpwuid(os.getuid()).pw_dir
    assert user_facts['user_shell'] == pwd.getpwuid(os.getuid()).pw_shell
    assert user_facts['real_user_id'] == os.getuid()

# Generated at 2022-06-13 03:39:52.945658
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():

    user_facts = {
        'user_id': 'ansible',
        'user_uid': 911,
        'user_gid': 911,
        'user_gecos': 'User &',
        'user_dir': '/home/user',
        'user_shell': '/bin/sh',
        'real_user_id': 911,
        'effective_user_id': 911,
        'real_group_id': 911,
        'effective_group_id': 911
    }

    assert user_facts == UserFactCollector().collect()

# Generated at 2022-06-13 03:39:58.968143
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    test_module = UserFactCollector()
    result = test_module.collect()
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

# Generated at 2022-06-13 03:41:03.697960
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():

    result = UserFactCollector().collect()
    assert 'user_id' in result
    assert isinstance(result['user_id'], str)
    assert 'user_uid' in result
    assert isinstance(result['user_uid'], int)
    assert 'user_gid' in result
    assert isinstance(result['user_gid'], int)
    assert 'real_user_id' in result
    assert isinstance(result['real_user_id'], int)
    assert 'effective_user_id' in result
    assert isinstance(result['effective_user_id'], int)
    assert 'real_group_id' in result
    assert isinstance(result['real_group_id'], int)
    assert 'effective_group_id' in result

# Generated at 2022-06-13 03:41:06.471758
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    ModuleUtilsTest = type('ModuleUtilsTest', (object,), {})
    collector = UserFactCollector()
    result = collector.collect(ModuleUtilsTest())
    assert result['effective_user_id'] == getpass.getuser()

# Generated at 2022-06-13 03:41:15.888288
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    fact_collector = UserFactCollector()

    # Test if collect() return a dictionary
    assert isinstance(fact_collector.collect(), dict)

    # Test if the number of keys in the dictionary is not equal to 0
    assert len(fact_collector.collect()) > 0

    # Test if the key 'user_id' in the dictionary is not equal to ''
    assert fact_collector.collect()['user_id'] != ''

    # Test if the key 'user_uid' in the dictionary is not equal to ''
    assert fact_collector.collect()['user_uid'] != ''

    # Test if the key 'user_gid' in the dictionary is not equal to ''
    assert fact_collector.collect()['user_gid'] != ''

    # Test if the key 'user_gecos' in the dictionary is not equal

# Generated at 2022-06-13 03:41:22.025854
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_facts_collector = UserFactCollector()

    collected_facts = {}
    user_facts = user_facts_collector.collect(collected_facts=collected_facts)

    assert isinstance(user_facts, dict)
    assert user_facts['user_id'] == getpass.getuser()
    assert isinstance(user_facts['user_id'], str)
    assert user_facts['user_uid'] == pwd.getpwuid(os.getuid()).pw_uid
    assert isinstance(user_facts['user_uid'], int)
    assert user_facts['user_gid'] == pwd.getpwuid(os.getuid()).pw_gid
    assert isinstance(user_facts['user_gid'], int)

# Generated at 2022-06-13 03:41:33.831178
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():

    # Declare UserFactCollector object
    class test_user_facts:
        def __init__(self):
            self.user = getpass.getuser()
    test_user = test_user_facts()

    # Declare UserFactCollector object
    class test_user_facts_uid:
        def __init__(self):
            self.uid = os.getuid()
    test_uid = test_user_facts_uid()

    # Declare UserFactCollector object
    class test_user_facts_gid:
        def __init__(self):
            self.gid = os.getgid()
    test_gid = test_user_facts_gid()

    # Declare UserFactCollector object

# Generated at 2022-06-13 03:41:37.535802
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():

    user_fc = UserFactCollector()
    user_facts = user_fc.collect(module=None, collected_facts=None)

    assert user_facts['user_id'] == getpass.getuser()

# Generated at 2022-06-13 03:41:45.444046
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_fact_collector = UserFactCollector()
    result = user_fact_collector.collect()

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

# Generated at 2022-06-13 03:41:48.893550
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    from ansible_collections.misc.not_a_real_collection.plugins.module_utils.facts.collectors.user import UserFactCollector
    module = UserFactCollector()
    print("module.collect() : ")
    print(module.collect())

# Generated at 2022-06-13 03:41:56.718083
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    collecter = UserFactCollector()
    collected_facts = {'user_id': 'user1',
                           'user_uid': '1234',
                           'user_gid': '5678',
                           'user_gecos': 'user1',
                           'user_dir': '/home/user1',
                           'user_shell': '/bin/bash',
                           'real_user_id': '1234',
                           'effective_user_id': '1234',
                           'real_group_id': '5678',
                           'effective_group_id': '5678'}

    if collecter.collect() == collected_facts:
        return True
    else:
        return False


# Generated at 2022-06-13 03:42:05.002802
# Unit test for method collect of class UserFactCollector
def test_UserFactCollector_collect():
    user_fact_collector = UserFactCollector()
    user_facts = user_fact_collector.collect()
    assert(user_facts['user_id'] == getpass.getuser())
    assert(user_facts['user_uid'] == os.getuid())
    assert(user_facts['real_user_id'] == os.getuid())
    assert(user_facts['effective_user_id'] == os.geteuid())
    assert(user_facts['real_group_id'] == os.getgid())
    assert(user_facts['effective_group_id'] == os.getgid())