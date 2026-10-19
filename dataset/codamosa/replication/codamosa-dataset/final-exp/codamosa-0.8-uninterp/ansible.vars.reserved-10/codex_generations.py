

# Generated at 2022-06-13 17:28:41.319357
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert 'tasks' in get_reserved_names()

# Generated at 2022-06-13 17:28:44.514472
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # FIXME: not a proper unit test.
    #        should not print to console but return result
    print("Public reserved names: ")
    print(get_reserved_names(False))
    print("Private reserved names: ")
    print(get_reserved_names(True))

# Generated at 2022-06-13 17:28:49.290450
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert isinstance(_RESERVED_NAMES, set)
    assert len(_RESERVED_NAMES) > 0
    assert is_reserved_name('hosts')
    assert is_reserved_name('name')
    assert is_reserved_name('loop')
    assert is_reserved_name('when')
    assert not is_reserved_name('xyz')



# Generated at 2022-06-13 17:28:54.379896
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert get_reserved_names(include_private=False) == set(('action', 'with_', 'tags', 'when', 'name', 'local_action', 'any_errors_fatal', 'max_fail_percentage', 'notify', 'register', 'retries', 'until'))


# Generated at 2022-06-13 17:29:01.352966
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:29:04.599807
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert get_reserved_names() == _RESERVED_NAMES
    assert get_reserved_names(include_private=False) == frozenset(get_reserved_names(include_private=False))


# Generated at 2022-06-13 17:29:13.149295
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' this function tests the functionality of get_reserved_names() '''

    results = get_reserved_names()

# Generated at 2022-06-13 17:29:17.483751
# Unit test for function get_reserved_names
def test_get_reserved_names():
    prompt = 'test_list_reserved_names FAILED'
    assert 'private' not in get_reserved_names(include_private=False), prompt
    assert 'private' in get_reserved_names(include_private=True), prompt



# Generated at 2022-06-13 17:29:23.286119
# Unit test for function get_reserved_names
def test_get_reserved_names():
    public_reserved = get_reserved_names(include_private=False)
    private_reserved = get_reserved_names(include_private=True)

    assert len(private_reserved) > len(public_reserved)
    assert 'with_' in public_reserved
    assert 'with_' not in private_reserved
    assert 'local_action' in public_reserved
    assert 'local_action' not in private_reserved

# Generated at 2022-06-13 17:29:34.704453
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' This function tests the get_reserved_names() function above. '''

    # Test public names
    test_public = set()
    test_private = set()
    test_result = set()

    # FIXME: find a way to 'not hardcode', possibly need role deps/includes
    class_list = [Play, Role, Block, Task]

    for aclass in class_list:
        aobj = aclass()

        # build ordered list to loop over and dict with attributes
        for attribute in aobj.__dict__['_attributes']:
            if 'private' in attribute:
                test_private.add(attribute)
            else:
                test_public.add(attribute)

    # local_action is implicit with action

# Generated at 2022-06-13 17:29:56.895742
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:30:06.836486
# Unit test for function get_reserved_names
def test_get_reserved_names():
    expected_reserved_names = {
        'action', 'become', 'become_user', 'block', 'block_errors',
        'changed_when', 'connection', 'delegate_to', 'environment',
        'failed_when', 'gather_facts', 'ignore_errors', 'include',
        'include_vars', 'local_action', 'meta', 'name', 'no_log',
        'notify', 'other_action', 'pre_tasks', 'post_tasks', 'register',
        'roles', 'run_once', 'sudo', 'sudo_user', 'tags', 'task', 'tasks',
        'transport', 'vars', 'with_', 'when'
    }

    assert expected_reserved_names == get_reserved_names()


# Generated at 2022-06-13 17:30:17.751526
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # Test get_reserved_names with different parameters.
    assert set(get_reserved_names()) == {'become', 'delegate_to', 'delegate_facts', 'environment', 'gather_facts', 'include', 'include_role', 'include_tasks', 'name', 'no_log', 'notify', 'register', 'roles', 'run_once', 'sudo', 'sudo_user', 'tags', 'task', 'tasks', 'vars'}

# Generated at 2022-06-13 17:30:27.173130
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert_reserved = set(['become', 'become_method', 'become_user', 'check_mode', 'connection', 'delegate_to', 'environment', 'environment_file',
                           'group_names', 'inventory_hostname', 'inventory_hostname_short', 'name', 'no_log', 'notify', 'register', 'remote_user',
                           'role_name', 'serial', 'tags', 'task_name', 'until', 'vars', 'when', 'not'])

# Generated at 2022-06-13 17:30:30.358316
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved_names = get_reserved_names()
    assert 'name' in reserved_names
    assert 'block' not in reserved_names
    assert 'private' not in reserved_names



# Generated at 2022-06-13 17:30:40.514075
# Unit test for function get_reserved_names
def test_get_reserved_names():

    reserved = get_reserved_names(False)
    assert 'action' in reserved
    assert 'local_action' in reserved
    if 'loop' in reserved:
        assert 'with_' in reserved
    assert 'hosts' in reserved
    assert 'name' in reserved
    assert 'register' in reserved
    assert 'transport' in reserved

    assert 'ignore_errors' not in reserved
    assert 'roles' not in reserved
    assert 'tags' not in reserved
    assert 'tasks' not in reserved

    reserved = get_reserved_names(True)
    for name in ('name', 'ignore_errors', 'roles'):
        assert name in reserved
    assert 'name' in reserved

# Generated at 2022-06-13 17:30:49.313720
# Unit test for function get_reserved_names
def test_get_reserved_names():
    public = frozenset(['become', 'connection', 'delegate_to', 'environment', 'gather_facts', 'name', 'no_log', 'remote_user', 'sudo', 'sudo_user', 'tags', 'tasks', 'vars', 'vars_prompt', 'vars_files'])

# Generated at 2022-06-13 17:30:58.344010
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert get_reserved_names() == get_reserved_names(True)

# Generated at 2022-06-13 17:31:03.122240
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert 'action' in get_reserved_names()
    assert 'local_action' in get_reserved_names()
    assert 'hosts' in get_reserved_names()
    assert 'name' in get_reserved_names()
    assert 'roles' in get_reserved_names()
    assert 'connection' in get_reserved_names()
    assert 'remote_user' in get_reserved_names()
    assert 'any_errors_fatal' in get_reserved_names(include_private=True)
    assert 'with_' in get_reserved_names(include_private=True)

# Generated at 2022-06-13 17:31:06.207090
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert set(get_reserved_names()) == _RESERVED_NAMES
    assert set(get_reserved_names(include_private=False)) == _RESERVED_NAMES - get_reserved_names()


# Generated at 2022-06-13 17:31:31.670757
# Unit test for function get_reserved_names
def test_get_reserved_names():
    names = get_reserved_names()
    assert len(names) > 0
    assert isinstance(names, set)

# Generated at 2022-06-13 17:31:32.644597
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert isinstance(get_reserved_names(), frozenset)



# Generated at 2022-06-13 17:31:34.009056
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ret = get_reserved_names()
    assert 'name' in ret
    assert 'delegate_to' in ret

# Generated at 2022-06-13 17:31:35.369037
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved_names = get_reserved_names()

    assert isinstance(reserved_names, set)

# Generated at 2022-06-13 17:31:39.058529
# Unit test for function get_reserved_names
def test_get_reserved_names():
    print("Checking internal reserved names\n")
    definition = get_reserved_names()

    if definition is not None:
        if isinstance(definition, set):
            print("set of reserved names: %s\n" % definition)
        else:
            print("Error, get_reserved_names expected set")
    else:
        print("Error, get_reserved_names returned None")


# Generated at 2022-06-13 17:31:41.385018
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved_names = get_reserved_names()
    assert isinstance(reserved_names, set)
    assert 'hosts' in reserved_names
    assert 'roles' in reserved_names


# Generated at 2022-06-13 17:31:49.202825
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert set(get_reserved_names(include_private=False)) == \
        set(['hosts', 'gather_facts', 'roles', 'vars', 'vars_files', 'tags', 'action',
             'register', 'ignore_errors', 'delegate_to', 'notify', 'delegate_facts', 'local_action',
             'when', 'with_', 'remote_user', 'sudo', 'sudo_user', 'async', 'poll', 'module_defaults'])


# Generated at 2022-06-13 17:32:00.569378
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' test function get_reserved_names '''

    public_reserved_names = get_reserved_names(include_private=False)
    assert len(public_reserved_names) == 39
    assert isinstance(public_reserved_names, set)

    private_reserved_names = get_reserved_names(include_private=True)
    assert len(private_reserved_names) == 40
    assert isinstance(private_reserved_names, set)

    assert public_reserved_names.isdisjoint(private_reserved_names)

    all_reserved_names = get_reserved_names()
    assert all_reserved_names == private_reserved_names
    assert all_reserved_names == public_reserved_names.union(private_reserved_names)

# Unit

# Generated at 2022-06-13 17:32:02.108654
# Unit test for function get_reserved_names
def test_get_reserved_names():
    for reserved_name in _RESERVED_NAMES:
        assert is_reserved_name(reserved_name)

# Generated at 2022-06-13 17:32:08.062450
# Unit test for function get_reserved_names
def test_get_reserved_names():
    display.verbosity = 4
    from ansible.playbook.play_context import PlayContext

    assert 'hosts' in get_reserved_names()
    assert 'name' in get_reserved_names()
    assert 'roles' in get_reserved_names()
    assert 'gather_facts' in get_reserved_names()
    assert 'host_vars' in get_reserved_names()
    assert PlayContext.CLIARGS in get_reserved_names()

# Generated at 2022-06-13 17:33:02.047558
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:33:05.157399
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # get_reserved_names should be deterministic
    assert set(get_reserved_names()) == _RESERVED_NAMES

# Generated at 2022-06-13 17:33:06.854066
# Unit test for function get_reserved_names
def test_get_reserved_names():
    result = get_reserved_names(False)
    # Verify that deprecated 'with_' is not returned
    assert not result & {'with_'}

# Generated at 2022-06-13 17:33:09.704103
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved = get_reserved_names()
    assert len(reserved) > 0
    assert 'hosts' in reserved

# Generated at 2022-06-13 17:33:18.064944
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # Check version of functions and class
    assert(Play._version == 2)
    assert(Task._version == 2)
    assert(Role._version == 2)
    assert(Block._version == 2)

    # Check that we return the correct reserved names
    assert('include_tasks' in get_reserved_names())
    assert('register' in get_reserved_names())
    assert('loop' in get_reserved_names())
    assert('local_action' in get_reserved_names())
    assert('with_' in get_reserved_names())
    assert('hosts' in get_reserved_names())
    assert('name' in get_reserved_names())
    assert('ignore_errors' in get_reserved_names())

    # Check that private names are returned

# Generated at 2022-06-13 17:33:30.334073
# Unit test for function get_reserved_names
def test_get_reserved_names():
    from collections import namedtuple

    ReservedNames = namedtuple('ReservedNames', ('public', 'private', 'all'))

    assert_equals = lambda a,b: reserved_names_assert_equals(a, b, ReservedNames)


# Generated at 2022-06-13 17:33:33.755703
# Unit test for function get_reserved_names
def test_get_reserved_names():
    r = get_reserved_names()
    assert 'name' in r
    assert 'hosts' in r

    r = get_reserved_names(False)
    assert 'delegate_to' not in r
    r = get_reserved_names(True)
    assert 'delegate_to' in r

# Generated at 2022-06-13 17:33:43.565486
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert get_reserved_names() == get_reserved_names(include_private=True)
    reserved_names = get_reserved_names()

    # check default
    assert 'hosts' in reserved_names
    assert 'roles' in reserved_names
    assert 'action' in reserved_names
    assert 'tags' in reserved_names
    assert 'local_action' in reserved_names
    assert 'with_' in reserved_names

    # check private
    assert 'loop' in reserved_names
    assert 'when' in reserved_names
    assert 'rescue' in reserved_names
    assert 'always' in reserved_names
    assert 'delegate_to' in reserved_names
    assert 'delegate_facts' in reserved_names
    assert 'include' in reserved_names
    assert 'import_playbook' in reserved

# Generated at 2022-06-13 17:33:47.747894
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' Unit test for AnsibleModule.get_reserved_names '''

    # FIXME: add test for plugin imports
    # FIXME: add test for plugin imports with a plugin_dir set

    # this is a simple syntax test that the list is created properly
    assert 'action' in get_reserved_names()



# Generated at 2022-06-13 17:33:55.600304
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved = get_reserved_names(include_private=False)

    assert 'tasks' in reserved
    assert 'gather_facts' in reserved
    assert 'loop' in reserved

    # name is private attribute of Play, not public
    assert 'name' not in reserved

    # roles is only public in role include, not play or task
    assert 'roles' not in reserved

    # register is only public in task, not play or role
    assert 'register' not in reserved

    # tags is only public in task, not play or role
    assert 'tags' not in reserved



# Generated at 2022-06-13 17:35:28.253046
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved = get_reserved_names(include_private=False)
    assert 'roles' in reserved
    assert 'action' in reserved
    assert 'user' in reserved
    assert 'group' in reserved
    assert 'namespace' in reserved
    assert 'local_action' in reserved
    assert 'with_' in reserved
    assert 'tags' in reserved
    assert 'block' in reserved
    assert 'register' in reserved
    assert 'unless' in reserved
    assert 'when' in reserved
    assert 'become' in reserved



# Generated at 2022-06-13 17:35:37.797352
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' returns a list of reserved names associated with play objects '''


# Generated at 2022-06-13 17:35:42.347624
# Unit test for function get_reserved_names
def test_get_reserved_names():
    private = get_reserved_names(include_private=True)
    assert 'private' in private
    assert '_private' in private
    assert 'private_var' not in private

    public = get_reserved_names(include_private=False)
    assert 'private' not in public
    assert '_private' not in public
    assert 'private_var' not in public


# Generated at 2022-06-13 17:35:47.943007
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved = get_reserved_names()

    if isinstance(reserved, set):
        reserved = frozenset(reserved)

    assert isinstance(reserved, frozenset)

    # check that the list is non-empty
    assert reserved

    # all members of reserved should be strings
    assert set(map(lambda x: isinstance(x, str), reserved)) == set([True])


test_get_reserved_names()

# Generated at 2022-06-13 17:35:51.747455
# Unit test for function get_reserved_names
def test_get_reserved_names():
    fields = get_reserved_names()
    assert isinstance(fields, set)
    assert 'name' in fields

    fields = get_reserved_names(include_private=False)
    assert isinstance(fields, set)
    assert 'name' in fields
    assert '_role_name' not in fields



# Generated at 2022-06-13 17:35:53.934503
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved = get_reserved_names(include_private=False)
    assert 'vars' in reserved

    reserved = get_reserved_names(include_private=True)
    assert 'name' in reserved

# Generated at 2022-06-13 17:35:56.644879
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert isinstance(get_reserved_names(False), set)
    assert len(get_reserved_names(False)) > 100
    assert len(get_reserved_names(True)) > 100

# Generated at 2022-06-13 17:36:03.909196
# Unit test for function get_reserved_names
def test_get_reserved_names():
    '''
    Unit test for function get_reserved_names() to ensure it is returning the correct reserved names.
    '''

    # All reserved variables regardless of scope
    public = set([u'any_errors_fatal', u'become', u'become_method', u'become_user', u'connection', u'delegate_facts',
                  u'environment', u'gather_facts', u'ignore_unreachable', u'no_log', u'post_tasks', u'pre_tasks',
                  u'roles', u'serial', u'strategy', u'tasks', u'vars_files', u'with_', u'action', u'local_action'])
    private = set([u'deps', u'handler', u'loop', u'register', u'notify'])
   

# Generated at 2022-06-13 17:36:07.768525
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved_names = get_reserved_names()

    assert 'hosts' in reserved_names
    assert 'roles' in reserved_names
    assert 'private' not in reserved_names


# Generated at 2022-06-13 17:36:11.442115
# Unit test for function get_reserved_names
def test_get_reserved_names():
    result = get_reserved_names()
    assert('tags' in result)
    assert('block' in result)
    assert('any_errors_fatal' in result)
    assert('private' in result)



# Generated at 2022-06-13 17:37:58.831123
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:38:03.311939
# Unit test for function get_reserved_names
def test_get_reserved_names():
    public = set()
    private = set()
    result = get_reserved_names()
    class_list = [Play, Role, Block, Task]

    for aclass in class_list:
        aobj = aclass()
        # build ordered list to loop over and dict with attributes
        for attribute in aobj.__dict__['_attributes']:
            if 'private' in attribute:
                private.add(attribute)
            else:
                public.add(attribute)

    assert len(result) == len(public.union(private))

# Generated at 2022-06-13 17:38:06.179238
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert len(_RESERVED_NAMES) == 79
    assert 'hosts' in _RESERVED_NAMES
    assert 'name' in _RESERVED_NAMES
    assert 'vars' in _RESERVED_NAMES

# Generated at 2022-06-13 17:38:12.755953
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # Basic test to validate no reserved names are missing
    assert len(get_reserved_names(include_private=False) & _RESERVED_NAMES) == len(_RESERVED_NAMES)

    # Basic test to validate no reserved names are missing
    assert len(get_reserved_names(include_private=True) & _RESERVED_NAMES) == len(_RESERVED_NAMES)

    # Test without private included
    assert get_reserved_names(include_private=False) == _RESERVED_NAMES



# Generated at 2022-06-13 17:38:20.171060
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # module is in both private and public
    assert isinstance(get_reserved_names(), set)
    assert 'module' in get_reserved_names()
    assert 'action' in get_reserved_names()
    assert 'local_action' in get_reserved_names()
    assert 'vars' in get_reserved_names()

    # connection is private only
    assert 'connection' in get_reserved_names(True)
    assert not 'connection' in get_reserved_names(False)

    # role_name is public only
    assert 'role_name' in get_reserved_names(True)
    assert 'role_name' in get_reserved_names(False)



# Generated at 2022-06-13 17:38:21.486488
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved_names = get_reserved_names()
    assert 'roles' in reserved_names

# Generated at 2022-06-13 17:38:24.738570
# Unit test for function get_reserved_names
def test_get_reserved_names():
    all_names = get_reserved_names()
    public_names = get_reserved_names(include_private=False)

    assert 'private' not in all_names

# Generated at 2022-06-13 17:38:25.945685
# Unit test for function get_reserved_names
def test_get_reserved_names():

    reserved_names = get_reserved_names()
    assert 'name' in reserved_names

# Generated at 2022-06-13 17:38:34.785367
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved_names = {'become', 'become_user', 'connection', 'delegate_to', 'gather_facts', 'hosts', 'name', 'port',
                      'roles', 'serial', 'serial_failure_criteria', 'strategy', 'tasks', 'vars'}