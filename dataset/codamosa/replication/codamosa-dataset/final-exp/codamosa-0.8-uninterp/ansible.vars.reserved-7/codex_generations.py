

# Generated at 2022-06-13 17:28:50.499430
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert_msg = "Failed the test of reserved names"

    reserved = get_reserved_names()


# Generated at 2022-06-13 17:28:55.765807
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' this function tests the get_reserved_names function '''

    # for now, we are only testing for the size
    assert len(get_reserved_names()) == 140    # FIXME: should not be hard coded
    assert len(get_reserved_names(False)) == 76    # FIXME: should not be hard coded

# Generated at 2022-06-13 17:29:02.321972
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' this test verifies that the play object names are being found in reserved names'''

    play_names = frozenset(get_reserved_names())

    # confirm all reserved names are reflected
    attribute_list = [
        'name',
        'hosts',
        'roles',
        'connection',
        'gather_facts',
        'max_fail_percentage',
        'any_errors_fatal',
        'serial',
        'vars',
        'tags',
        'skip_tags',
        'post_tasks',
        'pre_tasks',
        'notify',
        'handlers',
        'error_handler',
        'block',
    ]

    for name in attribute_list:
        assert name in play_names

    # confirm nothing else is included

# Generated at 2022-06-13 17:29:08.168062
# Unit test for function get_reserved_names
def test_get_reserved_names():

    # Test if private attributes are included and excluded
    private_included = get_reserved_names()
    private_excluded = get_reserved_names(False)
    private_names = set(get_reserved_names(True)).difference(get_reserved_names(False))

    print(private_names)
    for name in private_names:
        print(name)
        assert name in private_included
        assert name not in private_excluded

# Generated at 2022-06-13 17:29:09.979203
# Unit test for function get_reserved_names
def test_get_reserved_names():
    names = get_reserved_names()
    assert frozenset(names) == _RESERVED_NAMES

# Generated at 2022-06-13 17:29:13.552541
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' this is a unit test for the get_reserved_names function '''

    for name in get_reserved_names(include_private=True):
        assert is_reserved_name(name)

    for name in get_reserved_names(include_private=False):
        assert is_reserved_name(name)

# Generated at 2022-06-13 17:29:17.042985
# Unit test for function get_reserved_names
def test_get_reserved_names():
    result = _RESERVED_NAMES
    assert 'hosts' in result
    assert 'roles' in result
    assert 'tags' in result
    assert 'hosts' not in result



# Generated at 2022-06-13 17:29:19.633904
# Unit test for function get_reserved_names
def test_get_reserved_names():
    result = get_reserved_names()

    assert isinstance(result, set)
    assert 'tasks' in result
    assert 'roles' in result



# Generated at 2022-06-13 17:29:24.409146
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' test get_reserved_names'''
    import os
    import sys
    import pytest
    import ansible.playbook

    dir_path = os.path.dirname(os.path.realpath(__file__))

    sys.path.append(dir_path)

    playbook_reserved = ansible.playbook.get_reserved_names()

    assert playbook_reserved



# Generated at 2022-06-13 17:29:35.685962
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:29:51.445370
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert 'hosts' in get_reserved_names()
    assert 'roles' in get_reserved_names()
    assert 'action' in get_reserved_names()
    assert 'environment' in get_reserved_names()
    assert 'when' in get_reserved_names()
    assert 'delegate_to' in get_reserved_names()
    assert 'gather_facts' in get_reserved_names()
    assert 'force_handlers' in get_reserved_names()
    assert 'ignore_errors' in get_reserved_names()
    assert 'first_available_file' in get_reserved_names()
    assert 'any_errors_fatal' in get_reserved_names()
    assert 'serial' in get_reserved_names()
    assert 'sudo' in get_res

# Generated at 2022-06-13 17:29:58.441036
# Unit test for function get_reserved_names
def test_get_reserved_names():
    class Fake(object):
        _attributes = dict(
            x1=dict(),
            x2=dict(private=True),
            x3=dict(private=True),
            x4=dict(private=True),
        )
    class_list = [Play, Role, Fake]
    assert frozenset(get_reserved_names()) == frozenset(['x1', 'x2', 'x3', 'x4'])
    assert frozenset(get_reserved_names(include_private=False)) == frozenset(['x1'])

# Generated at 2022-06-13 17:30:02.246035
# Unit test for function get_reserved_names
def test_get_reserved_names():

    # this test just checks if a few specific names are found in the reserved list
    names = ['roles', 'tasks']

    for name in names:
        if name not in get_reserved_names():
            raise AssertionError("%s is a reserved keyword but not found in the list" % name)

# Generated at 2022-06-13 17:30:10.133133
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:30:19.633803
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # TypeError given because no arg is passed to the function
    try:
        get_reserved_names()
    except TypeError:
        pass

    # check if set is not empty
    assert get_reserved_names()

    # reserved names with private names
    reserved_with_private = get_reserved_names(include_private=True)

    # reserved names without private names
    reserved_without_private = get_reserved_names(include_private=False)

    # reserved without private should be a subset of reserved with private
    assert reserved_without_private.issubset(reserved_with_private)
    assert not reserved_without_private.issuperset(reserved_with_private)



# Generated at 2022-06-13 17:30:23.094222
# Unit test for function get_reserved_names
def test_get_reserved_names():
    '''
        Unit tests Reserved names list.
        Tests that public and private reserved names are both returned
        Tests that public and private reserved names are added to public list.
    '''
    aclass = Play()
    # Tests public reserved names
    assert aclass._attributes.keys() == get_reserved_names(include_private=False)
    # Tests public and private reserved names
    assert aclass.__dict__['_attributes'].keys() == get_reserved_names(include_private=True)



# Generated at 2022-06-13 17:30:34.045561
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved_names = get_reserved_names ()
    assert 'hosts' in reserved_names
    assert 'pre_tasks' in reserved_names
    assert 'roles' in reserved_names
    assert 'include_vars' in reserved_names
    assert 'include_tasks' in reserved_names
    assert 'tags' in reserved_names
    assert 'gather_facts' in reserved_names
    assert 'tags' in reserved_names
    assert 'roles' in reserved_names
    assert 'no_log' in reserved_names
    assert 'meta' in reserved_names
    assert 'any_errors_fatal' in reserved_names
    assert 'hosts' in reserved_names
    assert 'always_run' in reserved_names
    assert 'action' in reserved_names
    assert 'name' in reserved_names
   

# Generated at 2022-06-13 17:30:39.809348
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' Test get_reserved_names() returns a list of reserved names '''

    test_list = get_reserved_names()
    assert isinstance(test_list, set)

    # get_reserved_names should be returning a list of strings
    assert all (isinstance(name, basestring) for name in test_list)

test_get_reserved_names()

# Generated at 2022-06-13 17:30:45.689361
# Unit test for function get_reserved_names
def test_get_reserved_names():
    my_reserved_names = get_reserved_names()

    # test number of reserved names
    assert len(my_reserved_names) >= 145

    # test a few known values
    assert 'name' in my_reserved_names
    assert 'hosts' in my_reserved_names
    assert 'vars' in my_reserved_names
    assert 'private' in my_reserved_names
    assert 'include_role' in my_reserved_names



# Generated at 2022-06-13 17:30:55.717493
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' test the functionality of get_reserved_names function'''
    reserved = get_reserved_names(False)

    print(reserved)
    print(len(reserved))

    assert len(reserved) == 16
    assert 'action' in reserved
    assert 'compose' in reserved
    assert 'when' in reserved
    assert 'roles' in reserved
    assert 'gather_facts' in reserved
    assert 'vars' in reserved
    assert 'pre_tasks' in reserved
    assert 'post_tasks' in reserved
    assert 'vars_files' in reserved
    assert 'tasks' in reserved
    assert 'handlers' in reserved
    assert 'become' in reserved
    assert 'become_user' in reserved
    assert 'name' in reserved
    assert 'imports' in reserved
   

# Generated at 2022-06-13 17:31:20.623201
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:31:29.010897
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' This is a simple unit test, more info in test/playbook/test_play_name_variables.py '''

    # Set of all variables with the playbook, task and block objects
    public_reserved_names = frozenset(['any_errors_fatal', 'become', 'become_method', 'become_user', 'connection',
                                       'delegate_to', 'environment', 'gather_facts', 'hosts', 'ignore_errors',
                                       'name', 'roles', 'serial', 'sudo', 'sudo_user', 'tags', 'tasks', 'when'])

    # Set of all variables with the task and block objects

# Generated at 2022-06-13 17:31:34.118455
# Unit test for function get_reserved_names
def test_get_reserved_names():
    a = frozenset(['name', 'serial', 'hosts', 'gather_facts'])
    b = frozenset(['role_name', 'run_once', 'tasks', 'pre_tasks', 'post_tasks', 'pre_host_tasks', 'post_host_tasks', 'delegate_to', 'delegate_facts'])
    assert frozenset(get_reserved_names(False)) == a
    assert frozenset(get_reserved_names(True)) == a.union(b)



# Generated at 2022-06-13 17:31:35.711618
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert isinstance(_RESERVED_NAMES, frozenset)


# Generated at 2022-06-13 17:31:38.141333
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert isinstance(get_reserved_names(), set)
    assert len(get_reserved_names()) > 10
    assert 'name' in get_reserved_names()
    assert 'roles' in get_reserved_names()

# Generated at 2022-06-13 17:31:45.612570
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved_names = get_reserved_names()
    assert isinstance(reserved_names, set)
    reserved_names_only_public = get_reserved_names(include_private=False)
    assert 'connection' in reserved_names_only_public
    assert 'any_errors_fatal' in reserved_names_only_public
    assert 'async' in reserved_names_only_public



# Generated at 2022-06-13 17:31:56.619150
# Unit test for function get_reserved_names
def test_get_reserved_names():

    public = set(['pre_tasks', 'name', 'post_tasks', 'roles', 'tags', 'max_fail_percentage', 'serial', 'connection', 'gather_facts', 'notify', 'sudo', 'sudo_user', 'environment', 'delegate_to', 'become', 'remote_user', 'ignore_errors', 'check_mode', 'any_errors_fatal', 'no_log', 'deprecations', 'compile_roles_flags', 'role_compile', 'always_run', 'hosts', 'block', 'action', 'tasks', 'else_tasks', 'with_', 'register', 'when', 'async_poll', 'async_status_timeout', 'local_action'])

# Generated at 2022-06-13 17:32:00.788111
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # Currently this test is a NOP because the function is hardcoded and nothing changed in the code
    reserved = get_reserved_names()
    assert reserved == _RESERVED_NAMES
    reserved = get_reserved_names(include_private=False)
    assert reserved == _RESERVED_NAMES.difference(set(('state', 'with_')))

# Generated at 2022-06-13 17:32:08.032906
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' unit test for function get_reserved_names '''

    # FIXME: add a test for role dependencies/includes

    reserved = _RESERVED_NAMES
    assert len(reserved) > 0

    public = set()
    private = set()
    result = set()

    # FIXME: find a way to 'not hardcode', possibly need role deps/includes
    class_list = [Play, Role, Block, Task]

    for aclass in class_list:
        aobj = aclass()

        # build ordered list to loop over and dict with attributes
        for attribute in aobj.__dict__['_attributes']:
            if 'private' in attribute:
                private.add(attribute)
            else:
                public.add(attribute)


# Generated at 2022-06-13 17:32:19.019806
# Unit test for function get_reserved_names
def test_get_reserved_names():
    '''
    Test get_reserved_names, including private attributes
    '''

    reserved_public = frozenset(['gather_facts', 'delegate_to', 'name', 'any_errors_fatal', 'become', 'become_method', 'become_user', 'tags', 'register', 'ignore_errors', 'force_handlers', 'environment', 'action', 'local_action', 'remote_user'])

# Generated at 2022-06-13 17:32:51.769915
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # List of reserved names from class Play, Block and Task
    play_reserved_names = set(['connection', 'delegate_to', 'gather_facts', 'hosts', 'name', 'no_log', 'roles', 'serial', 'sudo', 'sudo_user', 'tags', 'tasks', 'transport', 'vars_files'])
    block_reserved_names = set(['block', 'block', 'rescue', 'always', 'any_errors_fatal'])

# Generated at 2022-06-13 17:32:57.747027
# Unit test for function get_reserved_names
def test_get_reserved_names():
    public = frozenset(['name', 'hosts'])
    private = frozenset(['serial', 'remote_user', 'roles', 'become_user'])
    result = get_reserved_names()
    assert result == public.union(private)

    result = get_reserved_names(include_private=False)
    assert result == public

# Generated at 2022-06-13 17:33:06.540793
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:33:16.586108
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' need to run this after importing the module containing the classes to test '''

    name_set = get_reserved_names()
    assert 'action' in name_set
    assert 'first_available_file' in name_set
    assert 'name' in name_set
    assert 'include_role' in name_set
    assert 'environment' in name_set
    assert 'notify' in name_set
    assert 'become' in name_set
    assert 'pre_tasks' in name_set
    assert 'connection' in name_set
    assert 'until' in name_set
    assert 'delegate_to' in name_set
    assert 'any_errors_fatal' in name_set
    assert 'when' in name_set
    assert 'post_tasks' in name_set
    assert 'tags'

# Generated at 2022-06-13 17:33:17.601707
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert get_reserved_names() == _RESERVED_NAMES

# Generated at 2022-06-13 17:33:29.934961
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' test_get_reserved_names - this function tests that the get_reserved_names function returns a proper list of reserved play names '''

    # it's hard to assert that this list is correct, but we can at least make sure to get a list
    # and that it grows/shrinks as we add/remove attributes
    reserved_names = get_reserved_names()
    assert isinstance(reserved_names, set)
    assert len(reserved_names) > 0

    # assert that items are added and removed as expected
    old_len = len(reserved_names)
    new_set = reserved_names.copy()
    new_set.add('test_attribute')
    new_len = len(new_set)
    assert new_len > old_len

    new_set.remove('test_attribute')
    new

# Generated at 2022-06-13 17:33:30.764572
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert len(get_reserved_names()) > 0

# Generated at 2022-06-13 17:33:39.636419
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:33:48.151606
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:33:58.239211
# Unit test for function get_reserved_names
def test_get_reserved_names():

    # gather all available reserved names for the play objects
    all_reserved = get_reserved_names(include_private=True)
    # gather the public reserved names for the play objects
    public_reserved = get_reserved_names(include_private=False)

    # list of all the reserved names
    all_reserved_list = sorted(list(all_reserved))
    public_reserved_list = sorted(list(public_reserved.difference(public_reserved.difference(all_reserved))))

    # helper variables for tests
    assert len(all_reserved) > len(public_reserved)
    assert sorted(all_reserved_list) == sorted(public_reserved_list + ['local_action', 'with_'])

    # assert that the 'local_action' is only included in the all_

# Generated at 2022-06-13 17:34:59.635162
# Unit test for function get_reserved_names
def test_get_reserved_names():
    result = get_reserved_names()
    assert 'hosts' in result
    assert 'name' in result
    assert 'action' in result


# Generated at 2022-06-13 17:35:08.161189
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:35:15.471394
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' helper function for unit test used in task_include.py '''
    assert get_reserved_names() == get_reserved_names(False)
    assert get_reserved_names(True) == get_reserved_names(False).union({'hosts', 'any_errors_fatal', 'delegate_to', 'run_once', 'no_log', 'first_available_file', 'tags', 'when', 'register', 'ignore_errors', 'become', 'become_method', 'become_user', 'when', 'changed_when', 'failed_when', 'environment', 'roles', 'block', 'blockinfile', 'blockinfile_'})

# Generated at 2022-06-13 17:35:24.646801
# Unit test for function get_reserved_names
def test_get_reserved_names():
    public = frozenset(['name', 'hosts', 'gather_facts', 'connection', 'sudo', 'sudo_user', 'become',
                        'become_method', 'become_user', 'remote_user', 'vars_files', 'roles', 'tasks',
                        'vars', 'handlers', 'any_errors_fatal', 'changed_when', 'failed_when', 'block',
                        'tags', 'ignore_errors', 'notify', 'when', 'register', 'environment', 'action',
                        'local_action', 'with_'])

# Generated at 2022-06-13 17:35:29.845433
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert isinstance(get_reserved_names(), set)
    assert len(get_reserved_names()) > 0
    assert 'roles' in get_reserved_names()


# Unit tests for function warn_if_reserved

# Generated at 2022-06-13 17:35:37.294566
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # test default
    reserved = get_reserved_names(include_private=True)
    assert isinstance(reserved, set)
    assert len(reserved) > 0
    assert 'when' in reserved

    # test include_private=False
    public = get_reserved_names(include_private=False)
    assert isinstance(public, set)
    assert len(public) > 0
    assert 'when' in public

    # test difference
    assert len(reserved.difference(public)) > 0
    assert 'tags' in reserved.difference(public)
    assert len(public.difference(reserved)) == 0

# Generated at 2022-06-13 17:35:45.154289
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved_names = get_reserved_names()
    assert isinstance(reserved_names, set), 'get_reserved_names returned a non-set'

    assert 'action' in reserved_names, 'action should be in reserved names'
    assert 'local_action' in reserved_names, 'local_action should be in reserved names'
    assert 'with_' in reserved_names, 'with_ should be in reserved names'
    assert 'roles' in reserved_names, 'roles should be in reserved names'
    assert 'tasks' in reserved_names, 'tasks should be in reserved names'
    assert 'block' in reserved_names, 'block should be in reserved names'

    assert 'vars_prompt' not in reserved_names, 'vars_prompt should NOT be in reserved names'

# Generated at 2022-06-13 17:35:53.245178
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert get_reserved_names() == get_reserved_names(include_private=True)
    assert 'name' in get_reserved_names()
    assert 'force_handlers' in get_reserved_names()
    assert 'gather_facts' in get_reserved_names()
    assert 'gather_subset' in get_reserved_names()
    assert 'hosts' in get_reserved_names()
    assert 'serial' in get_reserved_names()
    assert 'remote_user' in get_reserved_names()
    assert 'remote_port' in get_reserved_names()
    assert 'remote_pass' in get_reserved_names()
    assert 'remote_transport' in get_reserved_names()
    assert 'environment' in get_reserved_names()
   

# Generated at 2022-06-13 17:36:01.752469
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:36:12.843786
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # Testing public reserved names
    assert 'hosts' in get_reserved_names(include_private=False)
    assert 'name' in get_reserved_names(include_private=False)
    assert 'tasks' in get_reserved_names(include_private=False)
    assert 'action' in get_reserved_names(include_private=False)
    assert 'local_action' in get_reserved_names(include_private=False)
    assert 'with_' in get_reserved_names(include_private=False)

    # Testing private reserved names
    assert 'vars' in get_reserved_names(include_private=True)
    assert 'block' in get_reserved_names(include_private=True)

# Generated at 2022-06-13 17:38:29.840865
# Unit test for function get_reserved_names
def test_get_reserved_names():
    public = get_reserved_names(include_private=False)
    private = get_reserved_names(include_private=True)
    reduce_private = [x for x in private if x not in public]
    assert len(public & private) == len (public), "set intersection should be equal to public set"
    assert len(reduce_private) == 1, "set difference should be 1"
    assert 'vars' in reduce_private, "set difference should be 'vars'"

# Generated at 2022-06-13 17:38:33.296832
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert isinstance(get_reserved_names(), set)
    assert len(get_reserved_names()) > 0
    assert get_reserved_names(include_private=False) < get_reserved_names()