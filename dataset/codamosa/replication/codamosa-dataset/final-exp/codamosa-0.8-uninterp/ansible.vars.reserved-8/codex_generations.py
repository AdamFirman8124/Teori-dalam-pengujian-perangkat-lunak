

# Generated at 2022-06-13 17:28:44.107748
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert 'meta' in get_reserved_names()
    assert 'loop' in get_reserved_names()
    assert 'with_' in get_reserved_names()
    assert 'when' in get_reserved_names()

    assert 'no_log' not in get_reserved_names()
    assert 'private' not in get_reserved_names(include_private=False)



# Generated at 2022-06-13 17:28:46.358195
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert isinstance(get_reserved_names(), set)
    assert len(get_reserved_names()) > 5
    assert len(get_reserved_names(False)) > 5



# Generated at 2022-06-13 17:28:49.719004
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert set(['name', 'action']) == get_reserved_names()
    assert set(['name', 'action', 'private', 'private_role_vars']) == get_reserved_names(include_private=True)



# Generated at 2022-06-13 17:28:56.624181
# Unit test for function get_reserved_names
def test_get_reserved_names():
    public = get_reserved_names(include_private=False)
    private = get_reserved_names(include_private=True)
    # test that 'private' names are a subset of all names
    assert private.difference(public) == set(['delegate_to_localhost', 'any_errors_fatal', 'serial', 'connection', 'local_action'])
    assert public.difference(private) == set([])
    assert private.difference(public).issubset(private)



# Generated at 2022-06-13 17:29:05.896359
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' test get_reserved_names() function '''

    reserved_names = get_reserved_names(include_private=False)
    assert 'roles' in reserved_names
    assert 'action' in reserved_names
    assert 'local_action' not in reserved_names
    assert 'loop' not in reserved_names
    assert 'with_' not in reserved_names

    reserved_names = get_reserved_names(include_private=True)
    assert 'roles' in reserved_names
    assert 'action' in reserved_names
    assert 'local_action' in reserved_names
    assert 'loop' in reserved_names
    assert 'with_' in reserved_names

# Generated at 2022-06-13 17:29:11.176916
# Unit test for function get_reserved_names
def test_get_reserved_names():
    public_names = get_reserved_names(False)
    assert 'hosts' in public_names
    assert 'vars' in public_names
    assert 'block' not in public_names
    assert 'tasks' in public_names

    all_names = get_reserved_names(True)
    assert 'hosts' in all_names
    assert 'block' in all_names
    assert 'tasks' in all_names



# Generated at 2022-06-13 17:29:16.345037
# Unit test for function get_reserved_names
def test_get_reserved_names():

    # check for private vars is de-activated by default
    assert 'private' not in get_reserved_names(False)

    # if check for private vars is activated
    # there should be some private vars
    assert get_reserved_names(True).difference(get_reserved_names(False))

    # check that we have all the attributes that must have been added
    # when we did the update to get the loop implicit dependency
    assert 'loop' in get_reserved_names(False)
    assert 'with_' in get_reserved_names(False)

# Generated at 2022-06-13 17:29:21.245354
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert 'hosts' in get_reserved_names()
    assert 'name' in get_reserved_names()

    assert 'serial' in get_reserved_names()
    assert not is_reserved_name('serial')

    assert not is_reserved_name('gather_facts')
    assert not is_reserved_name('tags')

# Generated at 2022-06-13 17:29:28.900588
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert 'when' in _RESERVED_NAMES
    assert 'async' in _RESERVED_NAMES
    assert 'connection' in _RESERVED_NAMES
    assert 'with_' in _RESERVED_NAMES
    assert 'action' in _RESERVED_NAMES
    assert 'local_action' in _RESERVED_NAMES
    assert 'block' in _RESERVED_NAMES
    assert 'loop' in _RESERVED_NAMES
    assert 'pre_tasks' in _RESERVED_NAMES
    assert 'roles' in _RESERVED_NAMES
    assert 'tags' in _RESERVED_NAMES
    assert 'post_tasks' in _RESERVED_NAMES

# Generated at 2022-06-13 17:29:38.032361
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert 'hosts' in get_reserved_names()
    assert 'hosts' in get_reserved_names(include_private=False)
    assert 'tags' in get_reserved_names()
    assert 'tags' in get_reserved_names(include_private=False)
    assert 'fail_on_missing' in get_reserved_names()
    assert 'fail_on_missing' in get_reserved_names(include_private=False)
    assert 'vars' in get_reserved_names()
    assert 'vars' in get_reserved_names(include_private=False)
    assert 'name' in get_reserved_names()
    assert 'name' in get_reserved_names(include_private=False)
    assert 'delegate_to' in get_reserved_names()


# Generated at 2022-06-13 17:29:47.545187
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved = get_reserved_names()
    if 'name' not in reserved:
        raise AssertionError('name not in list of reserved names')

# Generated at 2022-06-13 17:29:56.022077
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert 'hosts' in _RESERVED_NAMES
    assert 'name' in _RESERVED_NAMES
    assert 'roles' in _RESERVED_NAMES
    assert 'vars' in _RESERVED_NAMES
    assert 'args' in _RESERVED_NAMES
    assert 'local_action' in _RESERVED_NAMES
    assert 'loop' in _RESERVED_NAMES
    assert 'with_' in _RESERVED_NAMES



# Generated at 2022-06-13 17:30:01.863341
# Unit test for function get_reserved_names
def test_get_reserved_names():
    public = get_reserved_names(include_private=False)
    assert len(public) == 4
    assert 'roles' in public
    assert 'tasks' in public
    assert 'vars' in public
    assert 'action' in public

    private = get_reserved_names(include_private=True)
    assert len(private) == 8
    assert 'roles' in private
    assert 'tasks' in private
    assert 'vars' in private
    assert 'action' in private
    assert 'loop' in private
    assert 'include' in private
    assert 'dep_chain' in private
    assert 'local_action' in private

# Generated at 2022-06-13 17:30:04.031304
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert isinstance(get_reserved_names(), frozenset)
    assert isinstance(get_reserved_names(include_private=False), frozenset)



# Generated at 2022-06-13 17:30:08.184951
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert get_reserved_names() == get_reserved_names(include_private=False)

    reserved_names = get_reserved_names()
    assert 'private' in reserved_names
    assert 'private' not in get_reserved_names(include_private=False)



# Generated at 2022-06-13 17:30:14.489989
# Unit test for function get_reserved_names
def test_get_reserved_names():
    raw_reserved_names = get_reserved_names()
    reserved_names = set()

    # raw_reserved_names is actually a set of tuples.
    #  This is because the dict used to build it has tuples as keys.
    #  The list of tuples comes from AnsibleUnsafeText, which has 3 tuples
    #  for each entry (name, description, safe).
    for item in raw_reserved_names:
        reserved_names.add(item[0])

    # Assert that we get the same items when we use the function we're testing
    # as when we use the frozen set created from the function.
    assert len(reserved_names) == len(_RESERVED_NAMES)
    assert reserved_names == _RESERVED_NAMES

# Generated at 2022-06-13 17:30:18.969534
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved_names = get_reserved_names()
    assert 'pre_tasks' in reserved_names
    assert 'with_items' in reserved_names
    assert 'tags' in reserved_names
    assert 'roles' in reserved_names
    assert 'include' in reserved_names


# Generated at 2022-06-13 17:30:24.375012
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' this function tests the get_reserved_names function '''

    class TestClass():
        myattribute = 'testvalue'
        _private_attribute = 'testvalue'
        _attributes = ['myattribute', '_private_attribute']

    testobj = TestClass()

    assert isinstance(get_reserved_names(), frozenset)
    assert not get_reserved_names().intersection(set(testobj._attributes))
    assert get_reserved_names().intersection(set(testobj._attributes), True)



# Generated at 2022-06-13 17:30:27.275535
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved = get_reserved_names()
    assert 'task' in reserved
    assert 'tasks' in reserved
    assert 'play' in reserved
    assert 'block' in reserved

# Generated at 2022-06-13 17:30:31.247825
# Unit test for function get_reserved_names
def test_get_reserved_names():
    if _RESERVED_NAMES:
        display.vvvv('Reserved names: %s' % _RESERVED_NAMES)
        assert Play.vars_prompt.startswith(tuple(_RESERVED_NAMES))
    else:
        assert False

# Generated at 2022-06-13 17:30:53.781608
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # first, test public names
    public_names = get_reserved_names(include_private=False)
    assert 'tasks' in public_names
    assert 'delegate_to' in public_names
    assert 'notify' in public_names

    # next, test private names
    private_names = get_reserved_names(include_private=True)
    assert 'action' in private_names
    assert 'local_action' in private_names
    assert 'with_' in private_names

    # now test a combination of public and private names
    both_names = get_reserved_names(include_private=True)
    both_names.add('test_name')
    assert 'test_name' in both_names

    # test cases with a few reserved names

# Generated at 2022-06-13 17:30:57.841725
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert len(_RESERVED_NAMES) == 40
    assert 'action' in _RESERVED_NAMES
    assert 'local_action' in _RESERVED_NAMES
    assert 'loop' in _RESERVED_NAMES
    assert 'with_' in _RESERVED_NAMES
    assert 'debug' in _RESERVED_NAMES
    assert 'vars' not in _RESERVED_NAMES

# Generated at 2022-06-13 17:31:08.144848
# Unit test for function get_reserved_names
def test_get_reserved_names():
    import re
    import unittest

    result = get_reserved_names(True)
    all_lower = [w for w in result if re.search('^[a-z_]+$', w)]
    all_alphanum = [w for w in result if re.search('^[a-z0-9_]+$', w)]

    class TestPlaybook(unittest.TestCase):
        ''' unit test class to test reserved names '''

        def setUp(self):
            self.reserved = get_reserved_names()

        def test_reserved(self):
            ''' test case for reserved names'''
            for attr in self.reserved:
                self.assertTrue(hasattr(Play(), attr))

        def test_lower(self):
            ''' test case for underscore '''


# Generated at 2022-06-13 17:31:14.004662
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' this function tests the return value of get_reserved_names by asserting a few elements of the return set '''

    reserved_names = get_reserved_names()
    reserved_names_as_list = list(reserved_names)

    assert 'tasks' in reserved_names_as_list
    assert 'include' in reserved_names_as_list
    assert 'local_action' in reserved_names_as_list
    assert 'with_' in reserved_names_as_list

# Generated at 2022-06-13 17:31:24.591306
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert type(get_reserved_names()) is set
    assert len(get_reserved_names()) > 20
    assert len(get_reserved_names(False)) < len(get_reserved_names())
    assert 'hosts' in get_reserved_names()
    assert 'hosts' in get_reserved_names(True)
    assert 'hosts' in get_reserved_names(False)
    assert 'action' in get_reserved_names()
    assert 'action' in get_reserved_names(True)
    assert 'action' in get_reserved_names(False)
    assert 'local_action' not in get_reserved_names()
    assert 'local_action' in get_reserved_names(True)

# Generated at 2022-06-13 17:31:27.422722
# Unit test for function get_reserved_names
def test_get_reserved_names():
    import pytest
    with pytest.raises(AssertionError):
        get_reserved_names(include_private=False)
    assert isinstance(get_reserved_names(include_private=True), frozenset)
    assert len(get_reserved_names()) > 0


# Generated at 2022-06-13 17:31:36.545666
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # FIXME: find a way to 'not hardcode', possibly need role deps/includes
    class_list = [Play, Role, Block, Task]

    for aclass in class_list:
        aobj = aclass()

        # build ordered list to loop over and dict with attributes
        for attribute in aobj.__dict__['_attributes']:
            if 'private' in attribute:
                assert (attribute in get_reserved_names(True)), "private attribute: %s not found in get_reserved_names" % attribute
            else:
                assert (attribute in get_reserved_names()), "public attribute: %s not found in get_reserved_names" % attribute

# Generated at 2022-06-13 17:31:37.657730
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert frozenset(get_reserved_names()) == _RESERVED_NAMES

# Generated at 2022-06-13 17:31:45.780268
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved_names = set(get_reserved_names())
    assert 'hosts' in reserved_names
    assert 'vars' in reserved_names
    assert 'action' in reserved_names
    assert 'local_action' in reserved_names
    assert 'loop' in reserved_names
    assert 'with_' in reserved_names
    assert 'name' in reserved_names
    assert 'any_errors_fatal' in reserved_names
    assert 'max_fail_percentage' in reserved_names
    assert 'serial' in reserved_names
    assert 'sudo' in reserved_names
    assert 'sudo_user' in reserved_names
    assert 'connection' in reserved_names
    assert 'when' in reserved_names
    assert 'become' in reserved_names
    assert 'become_user' in reserved_names

# Generated at 2022-06-13 17:31:53.609403
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' this function verifies that get_reserved_names() returns expected '''

    assert get_reserved_names(include_private=False) == frozenset([
        'any_errors_fatal', 'any_errors_fatal', 'become', 'become_method', 'become_user', 'connection', 'delegate_to', 'environment',
        'gather_facts', 'hosts', 'no_log', 'remote_user', 'serial', 'tags', 'ignore_unreachable', 'vars', 'vars_prompt', 'vars_files',
        'vault_password_files', 'when', 'with_'
        ])

    assert _RESERVED_NAMES.issubset(get_reserved_names(include_private=False))


# Generated at 2022-06-13 17:32:25.209543
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert get_reserved_names() == frozenset(['connection', 'delegate_to', 'become',
                                              'vars', 'roles', 'task', 'role', 'include',
                                              'include_role', 'block', 'register', 'include_tasks',
                                              'action', 'async', 'poll', 'local_action', 'when',
                                              'sudo', 'sudo_user', 'any_errors_fatal',
                                              'listen', 'listen_parents', 'with_', 'loop'])

# Generated at 2022-06-13 17:32:27.924423
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # FIXME: get this into a test case
    assert 'name' in get_reserved_names()



# Generated at 2022-06-13 17:32:31.377344
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved_names = get_reserved_names()
    assert reserved_names is not None
    assert isinstance(reserved_names, set)
    assert len(reserved_names) > 100

# Generated at 2022-06-13 17:32:37.885479
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert len(get_reserved_names()) != 0
    assert 'tasks' in get_reserved_names()
    assert 'roles' in get_reserved_names()
    assert 'vars' in get_reserved_names()
    assert 'register' in get_reserved_names()
    assert 'with_' in get_reserved_names()
    assert 'keyed_groups' in get_reserved_names()
    assert 'private' in get_reserved_names()
    assert 'include_role' not in get_reserved_names()


# Generated at 2022-06-13 17:32:41.562207
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # get current set of reserved names
    reserved = get_reserved_names()

    # should contain some values
    assert len(reserved) > 50

    # loop implies with_
    # FIXME: remove after with_ is not only deprecated but removed
    assert 'with_' in reserved

    # local_action is implicit with action
    assert 'local_action' in reserved

# Generated at 2022-06-13 17:32:51.284484
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:32:58.508038
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved_names = get_reserved_names(include_private=False)
    assert isinstance(reserved_names, set)
    assert len(reserved_names) > 0
    assert 'delegate_to' in reserved_names

    reserved_names = get_reserved_names(include_private=True)
    assert isinstance(reserved_names, set)
    assert len(reserved_names) > 0
    assert 'delegate_to' in reserved_names


# Generated at 2022-06-13 17:33:09.188935
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert get_reserved_names(include_private=False) == frozenset([
        'hosts', 'roles', 'gather_facts', 'any_errors_fatal', 'force_handlers', 'no_log', 'name', 'serial', 'remote_user',
        'remote_port', 'connection', 'timeout', 'sudo', 'sudo_user', 'sudo_pass', 'become', 'become_user', 'become_pass',
        'become_method', 'ignore_errors', 'tags', 'skip_tags', 'start_at_task', 'environment', 'directory', 'user',
        'host_vars', 'group_vars', 'role_vars', 'vars_files', 'action', 'local_action', 'with_', 'tags'
    ])


# Generated at 2022-06-13 17:33:17.668851
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:33:30.015908
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:34:22.975358
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:34:30.696980
# Unit test for function get_reserved_names
def test_get_reserved_names():
    display.vv('Testing get_reserved_names')
    reserved_names = get_reserved_names()
    assert 'vars' in reserved_names
    assert 'action' in reserved_names
    assert 'any_errors_fatal' in reserved_names
    assert 'block' in reserved_names
    assert 'hosts' in reserved_names
    assert 'name' in reserved_names
    assert 'roles' in reserved_names
    assert 'tasks' in reserved_names
    assert 'meta' in reserved_names

# Generated at 2022-06-13 17:34:34.618022
# Unit test for function get_reserved_names
def test_get_reserved_names():
    r_names = get_reserved_names()
    assert r_names.intersection(['roles', 'hosts', 'name', 'vars', 'block'])

    r_names = get_reserved_names(include_private=False)
    assert not r_names.intersection(['loop', 'action', 'local_action', 'when'])


# Generated at 2022-06-13 17:34:42.263887
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # check that we can get the list of reserved names
    rs = get_reserved_names()
    assert(rs != None)
    # check that the list is not empty
    assert(len(rs) > 0)
    # check that we can get the list of reserved names including private attributes
    rs = get_reserved_names(True)
    assert(rs != None)
    # check that the list is not empty
    assert(len(rs) > 0)



# Generated at 2022-06-13 17:34:51.240986
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:34:56.307532
# Unit test for function get_reserved_names
def test_get_reserved_names():

    # We don't know the values for reserved names, so just test with a few examples
    assert 'any_errors_fatal' in get_reserved_names()
    assert 'loop_control' in get_reserved_names()
    assert 'name' in get_reserved_names()
    assert 'private' in get_reserved_names()

# Generated at 2022-06-13 17:34:57.762746
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved_play_names = get_reserved_names()

    assert 'name' in r

# Generated at 2022-06-13 17:35:07.180676
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' This function tests the get_reserved_names function in order to make sure it continues to work as expected '''
    from ansible.playbook import Play
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role

    class_list = [Play, Role, Block, Task]

    for myclass in class_list:
        get_class_reserved = get_reserved_names()
        myclass = myclass()
        myclass_reserved = set()
        for attribute in myclass.__dict__['_attributes']:
            if 'private' in attribute:
                myclass_reserved.add(attribute)
            else:
                myclass_reserved.add(attribute)
        myclass_reserved.add('with_')

# Generated at 2022-06-13 17:35:09.261724
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert isinstance(get_reserved_names(), set)
    assert len(get_reserved_names()) > 0


# Generated at 2022-06-13 17:35:13.607918
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:36:49.216021
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:36:58.726865
# Unit test for function get_reserved_names
def test_get_reserved_names():

    # Create a set of public reserved names
    public = set()
    for name in get_reserved_names(include_private=False):
        if name.startswith("_"):
            continue
        public.add(name)


# Generated at 2022-06-13 17:37:06.689829
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert get_reserved_names() == {'become', 'become_user', 'connection', 'delegate_to', 'environment',
                                    'ignore_errors', 'local_action', 'name', 'notify', 'poll', 'role_names',
                                    'serial', 'sudo', 'sudo_user', 'task_action', 'task_name', 'tags',
                                    'task_vars', 'vars', 'with_', 'with_items'}

# Generated at 2022-06-13 17:37:08.010246
# Unit test for function get_reserved_names
def test_get_reserved_names():

    assert get_reserved_names() == get_reserved_names(include_private=False)

    assert 'name' in get_reserved_names()

# Generated at 2022-06-13 17:37:14.642569
# Unit test for function get_reserved_names
def test_get_reserved_names():
    public_names = get_reserved_names(include_private=False)
    assert isinstance(public_names, set)
    assert 'name' in public_names
    assert 'remote_user' in public_names
    assert 'sudo_user' in public_names
    assert 'connection' in public_names

    private_names = get_reserved_names(include_private=True)
    assert isinstance(private_names, set)
    assert 'gather_facts' in private_names
    assert 'hosts' in private_names
    assert 'no_log' in private_names

    public_private_names = get_reserved_names(include_private=True)
    assert len(public_private_names) > len(public_names)


# Generated at 2022-06-13 17:37:24.163436
# Unit test for function get_reserved_names
def test_get_reserved_names():
    '''
    Test the functionality of get_reserved_names
    '''
    reserved_names = get_reserved_names()

# Generated at 2022-06-13 17:37:32.540783
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert 'name' in get_reserved_names()
    assert 'vars' in get_reserved_names()
    assert 'include' in get_reserved_names(include_private=False)
    assert 'include' in get_reserved_names(include_private=True)
    assert 'any_errors_fatal' in get_reserved_names(include_private=False)
    assert 'any_errors_fatal' in get_reserved_names(include_private=True)
    assert 'sudo' in get_reserved_names(include_private=False)
    assert 'sudo' not in get_reserved_names(include_private=True)
    assert 'sudo_user' not in get_reserved_names(include_private=False)

# Generated at 2022-06-13 17:37:34.792534
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved_names = get_reserved_names()
    assert len(reserved_names) == len(set(reserved_names))

# Generated at 2022-06-13 17:37:43.671710
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved_names = get_reserved_names()

    assert 'tags' in reserved_names
    assert 'ignore_errors' in reserved_names

    assert 'become' in reserved_names
    assert 'become_method' in reserved_names
    assert 'become_user' in reserved_names

    assert 'connection' in reserved_names
    assert 'environment' in reserved_names
    assert 'gather_facts' in reserved_names
    assert 'name' in reserved_names
    assert 'vars' in reserved_names
    assert 'vars_prompt' in reserved_names
    assert 'vars_files' in reserved_names
    assert 'delegate_to' in reserved_names

    assert 'pre_tasks' in reserved_names
    assert 'roles' in reserved_names
    assert 'tasks' in reserved_

# Generated at 2022-06-13 17:37:47.559102
# Unit test for function get_reserved_names
def test_get_reserved_names():
    name_set = {'hosts', 'vars'}
    reserved = get_reserved_names()
    # Make sure reserved is superset of name_set
    assert name_set.issubset(reserved)