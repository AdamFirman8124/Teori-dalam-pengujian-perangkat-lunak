

# Generated at 2022-06-13 17:28:53.469645
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved = get_reserved_names()
    assert isinstance(reserved, set)
    assert 'hosts' in reserved
    assert 'with_items' in reserved
    assert 'with_' in reserved
    assert 'local_action' in reserved
    assert len(reserved) == 62

    reserved = get_reserved_names(include_private=False)
    assert 'loop' not in reserved
    assert 'with_' not in reserved
    assert 'local_action' not in reserved
    assert len(reserved) == 30



# Generated at 2022-06-13 17:29:00.710511
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' this function tests the get_reserved_names function '''

    reserved_names = get_reserved_names()

    assert 'hosts' in reserved_names

    assert 'roles' in reserved_names

    assert 'tasks' in reserved_names

    assert 'name' in reserved_names

    assert 'become' in reserved_names

    assert 'vars' in reserved_names

    assert 'include' in reserved_names

    assert 'pre_tasks' in reserved_names

    assert 'post_tasks' in reserved_names

    assert 'include_vars' in reserved_names

    assert 'local_action' in reserved_names

    assert 'tags' in reserved_names

    assert 'with_' in reserved_names

    assert 'when' in reserved_names

    assert 'block' in reserved_names


# Generated at 2022-06-13 17:29:05.944063
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # outcome should be frozenset with 11 or 25 strings
    assert len(get_reserved_names()) == 11
    assert isinstance(get_reserved_names(), frozenset)

    # outcome should be frozenset with 24 strings
    assert len(get_reserved_names(include_private=True)) == 25
    assert isinstance(get_reserved_names(include_private=True), frozenset)

# Generated at 2022-06-13 17:29:13.662940
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' tests the function get_reserved_names() and checks the length of the output '''

    public_reserved = get_reserved_names(include_private=False)
    private_reserved = get_reserved_names(include_private=True)

    # make sure public names are a subset of the private names
    assert public_reserved.issubset(private_reserved)

    # make sure it's not a trivial subset, such as an empty list
    assert len(public_reserved) < len(private_reserved)

    # make sure it doesn't include 'hosts' which is a special name not used in
    # the play/task objects
    assert 'hosts' not in private_reserved

# Generated at 2022-06-13 17:29:23.898380
# Unit test for function get_reserved_names
def test_get_reserved_names():
    if False:
        from ansible.utils.display import Display
        display = Display()

    display.debug('Testing names are correctly returned by get_reserved_names')
    result = get_reserved_names()
    assert type(result) is set
    assert 'hosts' in result
    assert 'roles' in result
    assert 'action' in result
    assert 'any_errors_fatal' in result
    result = get_reserved_names(include_private=False)
    assert type(result) is set
    assert 'hosts' in result
    assert 'roles' in result
    assert 'action' in result
    assert 'any_errors_fatal' in result
    assert 'become_user' not in result
    assert 'with_' in result
    assert 'loop' in result


# Generated at 2022-06-13 17:29:30.415174
# Unit test for function get_reserved_names
def test_get_reserved_names():

    # check for reserved_names that should always be present
    assert('name' in get_reserved_names())
    assert('hosts' in get_reserved_names())

    # check for reserved_names that should only be present when include_private == True
    assert('action' in get_reserved_names(include_private=True))
    # local_action is an implicit attribute of action
    assert('local_action' in get_reserved_names(include_private=True))
    assert('loop' in get_reserved_names(include_private=True))
    assert('with_' in get_reserved_names(include_private=True))

    # check for reserved_names that should only be present when include_private == False
    assert('action' in get_reserved_names(include_private=False))

# Generated at 2022-06-13 17:29:37.755833
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved = get_reserved_names()

    assert 'name' in reserved
    assert 'serial' in reserved
    assert 'user' in reserved
    assert 'delegate_to' in reserved
    assert 'delegate_facts' in reserved
    assert 'connection' in reserved
    assert 'hosts' in reserved
    assert 'gather_facts' in reserved
    assert 'sudo' in reserved
    assert 'sudo_user' in reserved
    assert 'environment' in reserved
    assert 'no_log' in reserved
    assert 'file_roots' in reserved
    assert 'vars_files' in reserved
    assert 'tags' in reserved



# Generated at 2022-06-13 17:29:49.071661
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:29:54.296430
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # Ensure we are returning all values
    assert len(get_reserved_names()) > 10

    # Ensure we are returning the correct values
    assert 'name' in get_reserved_names()
    assert 'role' not in get_reserved_names(include_private=False)

# Generated at 2022-06-13 17:30:01.828910
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' this function unit tests get_reserved_names '''

    test_case = get_reserved_names()

    # check the size of the set is not 0
    # we currently have 33 reserved names
    assert len(test_case) > 0, "get_reserved_names does not " \
    "contain any reserved names"

    for aclass in [Play, Role, Task, Block]:
        aobj = aclass()

        # walk over attributes and make sure they are in the list of reserved names
        for attribute in aobj.__dict__['_attributes']:

            if attribute in test_case: # pragma: no cover
                continue

            # local_acton is an implicit attribute with action

# Generated at 2022-06-13 17:30:18.412863
# Unit test for function get_reserved_names
def test_get_reserved_names():

    # test for public names
    result = get_reserved_names(include_private=False)
    assert 'roles' in result
    assert 'tags' in result

    # test for private names
    result = get_reserved_names(include_private=True)
    assert 'when' in result
    assert 'name' in result

    assert len(result) > 10

# Generated at 2022-06-13 17:30:21.875893
# Unit test for function get_reserved_names
def test_get_reserved_names():
    expected = frozenset(('any_errors_fatal', 'become', 'become_method', 'become_user', 'connection', 'delegate_to', 'environment', 'gather_facts', 'hosts', 'name', 'no_log', 'notify', 'notify_handler', 'post_tasks', 'pre_tasks', 'roles', 'serial', 'tags', 'tasks', 'transport', 'vars', 'vars_prompt'))
    assert expected == _RESERVED_NAMES

# Generated at 2022-06-13 17:30:32.615988
# Unit test for function get_reserved_names
def test_get_reserved_names():
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

    # local_action is implicit with action
    if 'action' in public:
        public.add('local_action')

    # loop implies with_
    # FIXME: remove after with_ is not only deprecated but removed

# Generated at 2022-06-13 17:30:38.887256
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert 'roles' in get_reserved_names()
    assert 'tasks' in get_reserved_names()
    assert 'handlers' in get_reserved_names()
    assert 'vars_files' in get_reserved_names()
    assert 'pre_tasks' in get_reserved_names()
    assert 'post_tasks' in get_reserved_names()

# Generated at 2022-06-13 17:30:41.047612
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved = get_reserved_names(include_private=True)
    assert isinstance(reserved, set)
    assert 'block' in reserved
    assert 'hosts' in reserved

    reserved = get_reserved_names(include_private=False)
    assert isinstance(reserved, set)
    assert 'block' in reserved
    assert 'hosts' in reserved



# Generated at 2022-06-13 17:30:49.637024
# Unit test for function get_reserved_names
def test_get_reserved_names():
    '''Test the reserved attributes'''
    assert get_reserved_names() == frozenset(['serial', 'tasks', 'name', 'b_vars', 'environment', 'any_errors_fatal', 'roles', 'gather_facts', 'tags', 'connection', 'post_tasks', 'another_option', 'with_', 'block', 'tasks_from', 'include', 'action', 'playbook', 'register', 'handlers', 'when', 'pre_tasks', 'vars', 'local_action', 'delegate_facts', 'vars_files', 'notify', 'hosts', 'roles_path', 'block_hosts', 'become', 'become_method', 'become_flags', 'become_user', 'become_ask_pass'])

# Generated at 2022-06-13 17:30:57.741122
# Unit test for function get_reserved_names
def test_get_reserved_names():

    result = get_reserved_names(include_private=False)
    expected = set(['any_errors_fatal', 'become', 'become_method', 'become_user', 'block', 'connection', 'delegate_to',
                    'environment', 'failed_when', 'gather_facts', 'ignore_errors', 'import_playbook', 'include',
                    'include_role', 'include_tasks', 'no_log', 'notify', 'post_tasks', 'pre_tasks', 'redirect',
                    'remote_user', 'roles', 'serial', 'tasks', 'tags', 'transport', 'when', 'with_', 'local_action'])

    assert result == expected



# Generated at 2022-06-13 17:31:02.441188
# Unit test for function get_reserved_names
def test_get_reserved_names():
    names = get_reserved_names()
    assert 'tags' in names
    assert 'when' in names
    assert 'with_' in names
    assert 'local_action' in names
    assert 'run_once' in names
    assert 'environment' in names
    assert 'loop' in names

# Generated at 2022-06-13 17:31:12.241156
# Unit test for function get_reserved_names
def test_get_reserved_names():
    public = get_reserved_names(False)
    private = get_reserved_names(True)
    assert 'name' in public
    assert 'name' in private
    assert 'private' in private
    assert 'private' not in public
    assert 'private' not in private
    assert 'public' not in public
    assert 'public' not in private
    assert 'tags' in public
    assert 'tags' in private
    assert 'gather_facts' in public
    assert 'gather_facts' in private
    assert 'roles' in public
    assert 'roles' in private
    assert 'vars_files' in public
    assert 'vars_files' in private
    assert 'vars_prompt' in public
    assert 'vars_prompt' in private
    assert 'task_filters' in private


# Generated at 2022-06-13 17:31:21.079092
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:32:00.001148
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # the class names are all lowercase
    assert 'pre_tasks' in get_reserved_names()
    assert 'post_tasks' in get_reserved_names()
    assert 'pre_task' in get_reserved_names()
    assert 'post_task' in get_reserved_names()
    assert 'pre_role' in get_reserved_names()
    assert 'post_role' in get_reserved_names()
    assert 'name' in get_reserved_names()
    assert 'roles' in get_reserved_names()
    assert 'handlers' in get_reserved_names()
    assert 'hosts' in get_reserved_names()
    assert 'meta' in get_reserved_names()
    assert 'connection' in get_reserved_names()

# Generated at 2022-06-13 17:32:04.459159
# Unit test for function get_reserved_names
def test_get_reserved_names():

    # should include private and public
    assert 'become' in get_reserved_names(include_private=True)
    assert 'no_log' in get_reserved_names(include_private=True)

    # should NOT include private, but should include public
    assert 'become' in get_reserved_names(include_private=False)
    assert 'no_log' not in get_reserved_names(include_private=False)

# Generated at 2022-06-13 17:32:12.486382
# Unit test for function get_reserved_names
def test_get_reserved_names():
    actual_private = get_reserved_names(include_private=False)
    actual_public = get_reserved_names(include_private=True)


# Generated at 2022-06-13 17:32:20.128994
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert 'roles' in get_reserved_names()
    assert 'role_paths' in get_reserved_names(False)
    assert 'include_role' in get_reserved_names(False)
    assert 'post_tasks' in get_reserved_names(False)
    assert 'pre_tasks' in get_reserved_names(False)
    assert 'vars_files' in get_reserved_names(False)
    assert 'playbook' in get_reserved_names(False)

# Generated at 2022-06-13 17:32:27.857929
# Unit test for function get_reserved_names
def test_get_reserved_names():

    # Test private vs. public names
    assert 'private' not in get_reserved_names(include_private=False)
    assert 'private' in get_reserved_names(include_private=True)

    # Test canonical names, when they are public or private
    assert 'include_tasks' in get_reserved_names(include_private=True)
    assert 'include_tasks' in get_reserved_names(include_private=False)
    assert 'include_role' in get_reserved_names(include_private=True)
    assert 'include_role' not in get_reserved_names(include_private=False)

    # Test implicit names
    assert 'local_action' in get_reserved_names(include_private=True)

# Generated at 2022-06-13 17:32:37.960217
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:32:41.396473
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved = get_reserved_names()
    print(reserved)
    assert 'hosts' in reserved
    assert 'hosts' in reserved
    assert 'roles' in reserved
    assert 'any_errors_fatal' in reserved
    assert 'action' in reserved
    assert 'gather_facts' in reserved

    assert 'loops' not in reserved

# Generated at 2022-06-13 17:32:51.284485
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' unit tests for get_reserved_names'''

    class TestClass:

        _attributes = dict(
            action=dict(default='foo', inherit=True, priority=1),
            a=dict(default='bar', inherit=True, private=True),
            b=dict(default='foobar', inherit=True, private=True),
            c=dict(default='bar', inherit=True, private=True),
            d=dict(default='foobar', inherit=True, private=True),
            e=dict(),
        )

    t = TestClass()
    assert get_reserved_names(include_private=True) == set(['a', 'b', 'c', 'd', 'e', 'action', 'local_action', 'loop', 'with_'])

# Generated at 2022-06-13 17:33:01.772792
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:33:10.443093
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert get_reserved_names(include_private=False) == frozenset(['tags', 'environment', 'delegate_to', 'hosts', 'name', 'connection', 'any_errors_fatal', 'serial', 'local_action', 'tasks', 'post_tasks',
        'pre_tasks', 'notify', 'vars', 'when', 'roles', 'gather_facts', 'gather_subset', 'run_once', 'become', 'become_user', 'become_method', 'remote_user', 'sudo', 'sudo_user', 'sudo_pass', 'register', 'delegate_facts', 'with_'])

# Generated at 2022-06-13 17:34:14.942256
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # Display to stderr (not stdout)
    display.verbosity = 3

    # Check that some reserved names are present
    assert 'gather_facts' in get_reserved_names()
    assert 'tags' in get_reserved_names()
    assert 'tasks' in get_reserved_names()
    assert 'add_host' in get_reserved_names(include_private=False)
    assert 'vars' in get_reserved_names(include_private=False)

    # Check that some reserved names are not present (private)
    assert 'sudo_user' not in get_reserved_names()
    assert 'connection' not in get_reserved_names()

    # Check that some reserved names are present (private)

# Generated at 2022-06-13 17:34:22.569394
# Unit test for function get_reserved_names
def test_get_reserved_names():
    public = [ 'become', 'become_method', 'become_user', 'connection', 'environment',
               'gather_facts', 'hosts', 'max_fail_percentage', 'name', 'no_log', 'serial',
               'strategy', 'sudo', 'sudo_user', 'tags', 'tasks', 'type', 'vars', 'vars_prompt',
               'vault_password_file' ]


# Generated at 2022-06-13 17:34:29.356643
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:34:36.567138
# Unit test for function get_reserved_names
def test_get_reserved_names():
    test_set = get_reserved_names()
    correct_set = frozenset(['remote_user', 'register', 'ignore_errors', 'when', 'connection', 'serial', 'sudo', 'delegate_to', 'tags', 'any_errors_fatal', 'notify', 'roles',
                             'vars', 'block', 'tasks', 'name', 'pre_tasks', 'post_tasks', 'include', 'playbook_vars', 'playbook_dirs', 'action', 'local_action', 'loop', 'with_', 'include_role', 'run_once', 'strategy'])
    assert test_set == correct_set, "reserved names not correctly returned"

# Generated at 2022-06-13 17:34:41.322272
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert get_reserved_names() == _RESERVED_NAMES
    assert get_reserved_names(include_private=False) == _RESERVED_NAMES.difference(set(['vars', 'omit', 'loop', 'delegate_to']))

# Generated at 2022-06-13 17:34:44.302107
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # assert the number of reserved names is what we expect it to be
    assert len(get_reserved_names(include_private=True)) == 76
    assert len(get_reserved_names(include_private=False)) == 67

# Generated at 2022-06-13 17:34:45.362376
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert get_reserved_names() == _RESERVED_NAMES

# Generated at 2022-06-13 17:34:48.245572
# Unit test for function get_reserved_names
def test_get_reserved_names():
    '''make sure that we have the expected number of reserved names'''
    reserved_names = get_reserved_names()
    assert(len(reserved_names) == 46)

# Generated at 2022-06-13 17:34:53.968184
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert 'become' in get_reserved_names(), 'become missing from reserved names'
    assert 'vars' not in get_reserved_names(), 'vars should not be in reserved names'
    # FIXME: this should be removed from private but not removed from public
    assert 'loop' not in get_reserved_names(include_private=False), 'loop should not be in public reserved names'



# Generated at 2022-06-13 17:34:58.917041
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert get_reserved_names(include_private=False) == {
        'action',
        'any_errors_fatal',
        'async',
        'become',
        'become_flags',
        'become_method',
        'become_user',
        'block',
        'connection',
        'gather_facts',
        'hosts',
        'ignore_errors',
        'local_action',
        'max_fail_percentage',
        'name',
        'notify',
        'register',
        'remote_user',
        'roles',
        'serial',
        'tags',
        'tasks',
        'transport',
        'vars',
        'with_',
    }


# Generated at 2022-06-13 17:36:50.236893
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' make sure we get the reserved names by default '''

    assert 'hosts' in get_reserved_names()
    assert 'roles' in get_reserved_names()
    assert 'connection' not in get_reserved_names(include_private=False)

# Generated at 2022-06-13 17:36:57.489532
# Unit test for function get_reserved_names
def test_get_reserved_names():
    test_public = set(['name', 'connection', 'user', 'fail_on_missing_handler', 'any_errors_fatal', 'gather_facts', 'delegate_to', 'serial', 'sudo_user', 'sudo', 'force_handlers'])
    test_private = set(['hosts', 'roles', 'vars_files', 'register', 'ignore_errors', 'when', 'environment', 'run_once', 'tags', 'tasks', 'notify'])

    reserved_names = get_reserved_names()

    assert reserved_names == test_public.union(test_private)

# Generated at 2022-06-13 17:36:58.406643
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert 'hosts' in get_reserved_names()

# Generated at 2022-06-13 17:36:59.560114
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert isinstance(_RESERVED_NAMES, set)



# Generated at 2022-06-13 17:37:03.604838
# Unit test for function get_reserved_names
def test_get_reserved_names():
    expected = set(['connection', 'delegate_to', 'environment', 'no_log', 'remote_user', 'sudo', 'sudo_user', 'tags', 'transport', 'vars', 'become', 'become_user'])
    result = get_reserved_names(include_private=False)
    assert result == expected



# Generated at 2022-06-13 17:37:10.163078
# Unit test for function get_reserved_names
def test_get_reserved_names():
    expected = ['any_errors_fatal', 'async_timeout', 'become', 'become_method',
                'become_user', 'block', 'connection', 'delegate_to', 'affected_tasks',
                'environment', 'first_available_file', 'ignore_errors', 'local_action',
                'loop', 'max_fail_percentage', 'meta', 'no_log', 'notify', 'poll',
                'register', 'retries', 'roles', 'serial', 'tags', 'until', 'when']
    assert get_reserved_names() == frozenset(expected)
    assert is_reserved_name('tags')
    assert not is_reserved_name('foo')

# Generated at 2022-06-13 17:37:20.019700
# Unit test for function get_reserved_names
def test_get_reserved_names():
    result = get_reserved_names()
    assert 'hosts' in result
    assert 'action' in result
    assert 'local_action' in result
    assert 'gather_facts' in result
    assert 'vars' in result
    assert 'vars_prompt' in result
    assert 'vars_files' in result
    assert 'include' in result
    assert 'pre_tasks' in result
    assert 'post_tasks' in result
    assert 'tasks' in result
    assert 'handlers' in result
    assert 'roles' in result
    assert 'role_path' in result
    # Options that should not show up in public
    assert 'any_errors_fatal' in result
    assert 'max_fail_percentage' in result
    assert 'serial' in result

# Generated at 2022-06-13 17:37:27.438849
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' This function tests our ability to correctly identify reserved names
    for play objects '''

    # create sets of reserved names for private and public testing
    public = set()
    private = set()
    for attribute in Play()._attributes:
        if 'private' in attribute:
            private.add(attribute)
        else:
            public.add(attribute)

    # test the public names
    public_result = set(get_reserved_names(include_private=False))
    assert public_result == public

    # test the private names
    private_result = set(get_reserved_names(include_private=True)).difference(public)
    assert private_result == private

# Generated at 2022-06-13 17:37:34.754537
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert 'name' in get_reserved_names()
    assert 'vars' in get_reserved_names()
    assert 'roles' in get_reserved_names()
    assert 'tasks' in get_reserved_names()
    assert 'block' in get_reserved_names()
    assert 'block' in get_reserved_names()
    assert 'notify' in get_reserved_names()
    assert 'handler' in get_reserved_names()
    assert 'meta' in get_reserved_names()
    assert 'tags' in get_reserved_names()
    assert 'gather_facts' in get_reserved_names()
    assert 'ignore_errors' in get_reserved_names()
    assert 'always_run' in get_reserved_names()

# Generated at 2022-06-13 17:37:43.671231
# Unit test for function get_reserved_names