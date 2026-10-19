

# Generated at 2022-06-13 17:28:50.065635
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:28:51.888819
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert 'vars' in get_reserved_names()
    assert len(get_reserved_names()) > 5
    assert len(get_reserved_names(False)) == 5


# Generated at 2022-06-13 17:28:54.320535
# Unit test for function get_reserved_names
def test_get_reserved_names():
    myset = set(get_reserved_names())

    assert 'hosts' in myset
    assert 'gather_facts' in myset
    assert 'roles' in myset
    assert 'tasks' in myset

    assert 'private_key_file' not in myset
    assert 'private' not in myset

    assert 'with_' in myset
    assert 'local_action' in myset



# Generated at 2022-06-13 17:28:55.491628
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert isinstance(get_reserved_names(), set)


# Generated at 2022-06-13 17:28:59.586114
# Unit test for function get_reserved_names
def test_get_reserved_names():
    '''
    This function test if get_reserved_names returns the good list of reserved names
    we are using these names as variables in our tests
    '''
    test_names = ['hosts', 'roles', 'hosts_list', 'vars_list', 'name', 'roles_list']
    reserved_names = get_reserved_names()
    for name in test_names:
        assert name in reserved_names

# Generated at 2022-06-13 17:29:00.473124
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert get_reserved_names(True) == _RESERVED_NAMES

# Generated at 2022-06-13 17:29:10.297226
# Unit test for function get_reserved_names
def test_get_reserved_names():
    names = get_reserved_names()
    assert 'name' in names
    assert 'become' in names
    assert 'become_user' in names
    assert 'become_method' in names
    assert 'become_flags' in names
    assert 'loop' not in names
    assert 'with_' not in names
    assert 'local_action' not in names
    assert 'delegate_to' not in names
    assert 'delegate_facts' not in names
    assert 'run_once' not in names
    assert 'gather_facts' in names
    assert 'vars_files' in names
    assert 'include' in names
    assert 'include_role' in names
    assert 'include_tasks' in names
    assert 'import_tasks' in names
    assert 'tags' in names

# Generated at 2022-06-13 17:29:17.205840
# Unit test for function get_reserved_names
def test_get_reserved_names():
    '''
    Test function get_reserved_names
    '''

    reserved = set()
    reserved_names = get_reserved_names()

    class_list = [Play, Role, Block, Task]

    for aclass in class_list:
        aobj = aclass()

        # build ordered list to loop over and dict with attributes
        for attribute in aobj.__dict__['_attributes']:
            reserved.add(attribute)

        # local_action is implicit with action
        if 'action' in aobj.__dict__['_attributes']:
            reserved.add('local_action')

        # loop implies with_
        # FIXME: remove after with_ is not only deprecated but removed
        if 'loop' in aobj.__dict__['_attributes']:
            reserved.add('with_')

   

# Generated at 2022-06-13 17:29:18.227310
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert 'connection' in get_reserved_names()

# Generated at 2022-06-13 17:29:26.940945
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:29:49.938232
# Unit test for function get_reserved_names
def test_get_reserved_names():
    public, private = get_reserved_names(include_private=False), get_reserved_names()

    # this is a list of reserved names that are not ok to add to a play
    assert 'roles' not in public
    assert 'roles' not in private

    # to test deprecated options here
    # FIXME: remove after with_ is not only deprecated but removed
    assert 'with_' in private
    assert 'with_' not in public

    # FIXME: remove after action is not only deprecated but removed
    assert 'action' not in public
    assert 'action' in private

    # local_action is implicit with action
    assert 'local_action' in public

    # FIXME: remove after loop is not only deprecated but removed
    assert 'loop' in private
    assert 'loop' not in public

# Generated at 2022-06-13 17:29:52.013643
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved = get_reserved_names()
    assert(len(reserved) > 0)

# Generated at 2022-06-13 17:29:54.787756
# Unit test for function get_reserved_names
def test_get_reserved_names():
    names = get_reserved_names()
    assert 'hosts' in names
    assert 'vars' in names
    assert 'set_fact' in names

# Generated at 2022-06-13 17:30:02.184599
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' test module get_reserved_names '''
    public_names = get_reserved_names()
    private_names = get_reserved_names(include_private=False)
    assert 'hosts' in public_names
    assert 'roles' in public_names
    assert 'tasks' in public_names
    assert 'include_vars' in public_names
    assert 'include_role' in public_names
    assert 'pre_tasks' in public_names
    assert 'post_tasks' in public_names
    assert 'handlers' in public_names
    assert 'register' in public_names
    assert 'local_action' in public_names
    assert 'action' in private_names
    assert 'delegate_to' in private_names
    assert 'delegate_facts' in private_names


# Generated at 2022-06-13 17:30:10.066222
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # test when include_private = False
    # Play: action, connection, environment, gather_facts, hosts, name, serial, sudo, sudo_user, tags, tasks
    # Role: role_name, role_path
    # Block: delegate_to, rescue, always, block, vars
    # Task: any_errors_fatal, async_poll, async_seconds, become, become_flags, become_method, become_user, delegate_to, ignore_errors, remote_user, register, retries, tags, until, warn
    reserved_no_private = get_reserved_names(include_private=False)

# Generated at 2022-06-13 17:30:18.207529
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert get_reserved_names() == frozenset(['post_tasks', 'import_tasks', 'vars', 'block', 'roles', 'hosts', 'handlers', 'pre_tasks', 'tasks', 'register', 'notify', 'name', 'action', 'local_action', 'with_', 'loop', 'include', 'any_errors_fatal', 'delegate_to', 'until', 'failed_when', 'listen', 'when', 'become', 'become_user', 'become_method', 'serial', 'async', 'poll'])

# Generated at 2022-06-13 17:30:28.414072
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert 'name' in get_reserved_names()
    assert 'include' in get_reserved_names()
    assert 'action' in get_reserved_names()
    assert 'become' in get_reserved_names()
    assert 'delegate_to' in get_reserved_names()

     # assert 'local_action' in get_reserved_names()
    assert 'any_errors_fatal' in get_reserved_names()
    assert 'delegate_facts' in get_reserved_names()

    assert 'notify' not in get_reserved_names()
    assert 'handlers' not in get_reserved_names()
    assert 'roles' not in get_reserved_names()
    assert 'tags' not in get_reserved_names()
    # assert 'block' not in get

# Generated at 2022-06-13 17:30:35.553201
# Unit test for function get_reserved_names
def test_get_reserved_names():
    result = get_reserved_names()
    assert not any(name in result for name in ('action', 'roles', 'include_variables', 'include_role'))
    assert all(name in result for name in ('delegate_to'))

    result = get_reserved_names(include_private=False)
    assert not any(name in result for name in ('delegate_to', 'tags', 'gather_facts'))
    assert all(name in result for name in ('action', 'roles'))

# Generated at 2022-06-13 17:30:46.278471
# Unit test for function get_reserved_names
def test_get_reserved_names():
    public = frozenset(['gather_facts', 'hosts', 'name', 'roles', 'become', 'become_method', 'connection', 'any_errors_fatal', 'async', 'delegate_to', 'remote_user', 'become_user', 'become_ask_pass', 'become_flags', 'register', 'ignore_errors', 'check_mode'])

# Generated at 2022-06-13 17:30:56.398385
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved = get_reserved_names(include_private=False)

    assert 'vars' in reserved
    assert 'roles' in reserved
    assert 'locals' in reserved
    assert 'become' not in reserved
    assert 'run_once' not in reserved
    assert 'environment' not in reserved
    assert 'register' not in reserved
    assert 'ignore_errors' not in reserved
    assert 'become_user' not in reserved
    assert 'tags' not in reserved
    assert 'delegate_to' not in reserved
    assert 'sudo' not in reserved
    assert 'sudo_user' not in reserved
    assert 'environment' not in reserved

    # reserved public and private options
    reserved = get_reserved_names(include_private=True)

    assert 'environment' in reserved
    assert 'register' in reserved

# Generated at 2022-06-13 17:31:25.510538
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved_set = frozenset(get_reserved_names())
    assert len(reserved_set) > 0
    assert isinstance(reserved_set, frozenset)
    assert 'name' in reserved_set
    assert 'any_errors_fatal' in reserved_set
    assert 'with_items' in reserved_set
    assert 'environment' in reserved_set
    assert 'no_log' in reserved_set

# Generated at 2022-06-13 17:31:26.327950
# Unit test for function get_reserved_names
def test_get_reserved_names():
    result = get_reserved_names()
    print(result)


# Generated at 2022-06-13 17:31:36.703084
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:31:39.069749
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # FIXME: this test will fail when we have a new reserved name
    assert(len(get_reserved_names()) == 24)
    assert(len(get_reserved_names(include_private=False)) == 21)

# Generated at 2022-06-13 17:31:40.663151
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved_names = get_reserved_names()
    assert len(reserved_names) > 0
    assert 'hosts' in reserved_names



# Generated at 2022-06-13 17:31:45.097938
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert isinstance(get_reserved_names(), set)
    assert len(get_reserved_names()) > 1
    assert isinstance(get_reserved_names(include_private=False), set)
    assert len(get_reserved_names(include_private=False)) > 1
    assert len(get_reserved_names()) > len(get_reserved_names(include_private=False))


# Generated at 2022-06-13 17:31:55.121086
# Unit test for function get_reserved_names
def test_get_reserved_names():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    public_names = get_reserved_names(False)
    private_names = get_reserved_names()

    # Test private names was subtracted from public
    assert public_names.issubset(private_names)

    # Test we can look up all names simply
    assert 'tasks' in public_names
    assert 'role_path' in public_names
    assert 'gather_facts' in public_names
    assert 'tags' in private_names
    assert 'private' in private_names

    # Test we can use them in conjunction with ansible and it works still
    p = Play()
    r = Role()
    for name in public_names:
        setattr(p, name, 'test')

# Generated at 2022-06-13 17:32:01.052206
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:32:08.231247
# Unit test for function get_reserved_names
def test_get_reserved_names():
    '''This function tests the get_reserved_names function'''

    # All reserved names

# Generated at 2022-06-13 17:32:09.588463
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert isinstance(_RESERVED_NAMES, frozenset)
    assert set(_RESERVED_NAMES)

# Generated at 2022-06-13 17:32:38.631173
# Unit test for function get_reserved_names
def test_get_reserved_names():
    test = get_reserved_names()

    assert type(test) == set
    assert 'roles' in test
    assert 'private' not in test
    assert 'no_log' not in test
    assert 'name' in test
    assert 'handler' in test
    assert 'block' in test

# Generated at 2022-06-13 17:32:44.809375
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert 'action' in get_reserved_names(include_private=True)
    assert 'action' in get_reserved_names(include_private=False)
    assert 'tags' in get_reserved_names(include_private=True)
    assert 'tags' in get_reserved_names(include_private=False)
    assert 'connection' in get_reserved_names(include_private=True)
    assert 'connection' not in get_reserved_names(include_private=False)
    assert 'local_action' in get_reserved_names(include_private=True)
    assert 'local_action' not in get_reserved_names(include_private=False)
    assert 'vars' in get_reserved_names(include_private=True)
    assert 'vars' in get_reserved_

# Generated at 2022-06-13 17:32:53.649019
# Unit test for function get_reserved_names
def test_get_reserved_names():
    result = get_reserved_names()

    assert 'name' in result
    assert 'action' in result
    assert 'hosts' in result
    assert 'any_errors_fatal' in result
    assert 'serial' in result
    assert 'become' in result
    assert 'become_user' in result
    assert 'connection' in result
    assert 'sudo_user' in result
    assert 'sudo' in result
    assert 'run_once' in result
    assert 'when' in result
    assert 'async_poll_interval' in result

    assert 'vars' in result
    assert 'roles' in result
    assert 'tasks' in result
    assert 'block' in result
    assert 'includes' in result
    assert 'tags' in result
    assert 'register' in result

    assert 'setup'

# Generated at 2022-06-13 17:32:55.810203
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert isinstance(get_reserved_names(), set)
    assert isinstance(get_reserved_names(False), set)

# Generated at 2022-06-13 17:33:02.046777
# Unit test for function get_reserved_names
def test_get_reserved_names():
    '''
    This function tests get_reserved_names and returns true if the test passes
    and false if the test fails.
    '''
    reserved_names = list(get_reserved_names())
    test_result = ('action' in reserved_names and 'pre_tasks' in reserved_names)

    print ("\n***RESULT***\n")
    if test_result:
        print ("TEST PASSED")
    else:
        print ("TEST FAILED")

    print ("\n***END***\n")

    return test_result


# Generated at 2022-06-13 17:33:06.372168
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert 'action' in get_reserved_names()
    assert 'local_action' in get_reserved_names()
    assert 'loop' in get_reserved_names(include_private=True)
    assert 'with_' in get_reserved_names(include_private=True)

# Generated at 2022-06-13 17:33:16.431588
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:33:28.341527
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved = set(get_reserved_names())
    reserved_priv = set(get_reserved_names(include_private=True))
    assert reserved == set(['name', 'hosts', 'gather_facts', 'remote_user', 'connection', 'sudo', 'sudo_user', 'when', 'delegate_to', 'any_errors_fatal', 'serial', 'environment', 'no_log', 'check_mode', 'tags', 'failed_when', 'notify', 'register', 'vars', 'vars_files', 'vars_prompt', 'vault_password_files', 'transport', 'become', 'become_method', 'become_user', 'become_flags', 'ignore_errors'])

# Generated at 2022-06-13 17:33:30.961703
# Unit test for function get_reserved_names
def test_get_reserved_names():
    result = get_reserved_names()
    assert type(result) is frozenset
    assert result == _RESERVED_NAMES

# Generated at 2022-06-13 17:33:39.819288
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:34:37.649572
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:34:40.759589
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved = get_reserved_names()

    # assert isinstance(reserved, set)
    assert 'name' in reserved
    assert 'gather_facts' in reserved

# Generated at 2022-06-13 17:34:47.989240
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert(('when' in get_reserved_names()))
    assert(('private' not in get_reserved_names()))
    assert(('private' in get_reserved_names(include_private=True)))
    assert(('local_action' in get_reserved_names(include_private=True)))
    assert(('with_' in get_reserved_names()))
    assert(('with_' in get_reserved_names(include_private=True)))
    assert(('loop' not in get_reserved_names()))
    assert(('loop' in get_reserved_names(include_private=True)))

# Generated at 2022-06-13 17:34:49.272912
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved = get_reserved_names()
    assert 'roles' in reserved
    assert 'roles' in reserved

# Generated at 2022-06-13 17:34:58.677761
# Unit test for function get_reserved_names
def test_get_reserved_names():
    public_names = set(['name', 'hosts', 'connection', 'sudo', 'sudo_user', 'remote_user', 'gather_facts', 'any_errors_fatal', 'serial', 'max_fail_percentage', 'ignore_errors', 'block', 'notify', 'handlers', 'register', 'vars', 'vars_files', 'action', 'local_action', 'with_', 'tags'])
    private_names = set(['action', 'loop', 'when'])

    result = get_reserved_names()
    assert result == public_names.union(private_names)

    result = get_reserved_names(include_private=False)
    assert result == public_names



# Generated at 2022-06-13 17:35:07.628829
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:35:15.230634
# Unit test for function get_reserved_names
def test_get_reserved_names():

    reserved = get_reserved_names(include_private=False)

    # all expected vars are in reserved
    assert('name' in reserved )
    assert('vars' in reserved )
    assert('tags' in reserved )
    assert('when' in reserved )

    # local_action is implicit with action
    assert('local_action' in reserved )

    # loop implies with_
    assert('with_' in reserved )

    # some not expected vars are in reserved
    assert('private' not in reserved )
    assert('action' not in reserved )
    assert('loop' not in reserved )

    # local_action is not there when private vars are not included
    assert('private' not in reserved )



# Generated at 2022-06-13 17:35:22.118778
# Unit test for function get_reserved_names
def test_get_reserved_names():
    public = get_reserved_names(include_private=False)
    private = get_reserved_names(include_private=True)

    assert 'with_items' in private
    assert 'remote_user' in public
    assert 'any_errors_fatal' in private

    assert 'loop' in private
    assert 'with_' in private

    assert 'action' in public
    assert 'local_action' in public

    assert 'included_tasks' not in public
    assert 'included_tasks' not in private

# Generated at 2022-06-13 17:35:29.114599
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:35:29.949000
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert get_reserved_names(True) == _RESERVED_NAMES

# Generated at 2022-06-13 17:37:17.140601
# Unit test for function get_reserved_names
def test_get_reserved_names():

    public, private = get_reserved_names(False), get_reserved_names(True)

    assert 'action' in public
    assert 'local_action' in private
    assert 'action' in private

    assert 'loop' in private
    assert 'with_' in private

# Generated at 2022-06-13 17:37:24.607615
# Unit test for function get_reserved_names
def test_get_reserved_names():
    names = get_reserved_names()
    assert isinstance(names, set), "get_reserved_names() did not return a set"
    assert len(names) > 10, "get_reserved_names() did not return more than 10 items"

    names = get_reserved_names(include_private=False)
    assert isinstance(names, set), "get_reserved_names(include_private=False) did not return a set"
    assert len(names) > 5, "get_reserved_names(include_private=False) did not return more than 5 items"



# Generated at 2022-06-13 17:37:32.835279
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved = get_reserved_names()
    assert 'name' in reserved
    assert 'delegate_to' in reserved
    assert 'ignore_errors' in reserved
    assert 'block' in reserved
    assert 'tasks' in reserved
    assert 'handlers' in reserved
    assert 'pre_tasks' in reserved
    assert 'post_tasks' in reserved
    assert 'when' in reserved
    assert 'async' in reserved
    assert 'async_status_timeout' in reserved
    assert 'notify' in reserved
    assert 'register' in reserved
    assert 'poll' in reserved
    assert 'ignore_errors' in reserved
    assert 'tags' in reserved
    assert 'any_errors_fatal' in reserved
    assert 'run_once' in reserved
    assert 'connection' in reserved

# Generated at 2022-06-13 17:37:37.808871
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert isinstance(get_reserved_names(False), set)
    assert isinstance(get_reserved_names(True), set)
    assert len(get_reserved_names(False)) > 0
    assert len(get_reserved_names(True)) > 0
    assert len(get_reserved_names(False)) < len(get_reserved_names(True))


# Generated at 2022-06-13 17:37:41.678290
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved_private = 'hosts'
    reserved_public = 'action'

    actual = get_reserved_names()

    assert reserved_private in actual, '%s missing in reserved vars' % reserved_private

    assert reserved_public in actual, '%s missing in reserved vars' % reserved_public

# Generated at 2022-06-13 17:37:48.726308
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:37:57.751290
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # public is a superset of private
    public = get_reserved_names(include_private=False)
    private = get_reserved_names(include_private=True)

    assert public.issubset(private)


# Generated at 2022-06-13 17:38:01.010943
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' unit test for the get_reserved_names() function '''

    assert 'hosts' in get_reserved_names(), 'hosts is a reserved name and should be in the list of returned names'
    assert 'action' in get_reserved_names(), 'action is a reserved name and should be in the list of returned names'
    assert 'private' not in get_reserved_names(include_private=False), 'private is not part of the public methods'
    assert 'private' in get_reserved_names(include_private=True), 'private is a private method and should be in returned names'

# Generated at 2022-06-13 17:38:11.090697
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' This function tests if we get reserved names correctly '''

    names = get_reserved_names(False)
    assert len(names) == 18
    assert names.issuperset(set(['name', 'hosts', 'roles', 'tasks', 'action', 'local_action', 'with_']))

    names = get_reserved_names(True)
    assert len(names) == 21
    assert names.issuperset(set(['name', 'hosts', 'roles', 'tasks', 'action', 'local_action', 'with_']))

    names = get_reserved_names(False)
    assert len(names) == 18

# Generated at 2022-06-13 17:38:12.836132
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' test the get_reserved_names function '''

    assert 'name' in _RESERVED_NAMES