

# Generated at 2022-06-13 17:28:50.622912
# Unit test for function get_reserved_names
def test_get_reserved_names():

    reserved = get_reserved_names(include_private=False)

    assert 'hosts' in reserved
    assert 'name' in reserved
    assert 'gather_facts' in reserved
    assert 'roles' in reserved
    assert 'tasks' in reserved
    assert 'include' in reserved
    assert 'connection' in reserved
    assert 'remote_user' in reserved
    assert not ('port' in reserved)
    assert not ('private_key_file' in reserved)

# Generated at 2022-06-13 17:28:59.747919
# Unit test for function get_reserved_names
def test_get_reserved_names():
    print("Test reserved names...")

# Generated at 2022-06-13 17:29:01.093376
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved_names = get_reserved_names(include_private=False)
    assert isinstance(reserved_names, set)

# Generated at 2022-06-13 17:29:03.208607
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert _RESERVED_NAMES is not None
    assert len(_RESERVED_NAMES) > 0


# Generated at 2022-06-13 17:29:09.130763
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert get_reserved_names() == frozenset(['post_tasks', 'pre_tasks', 'run_once', 'roles', 'tags', 'tasks', 'register', 'vars', 'environment', 'gather_facts', 'no_log', 'local_action', 'with_', 'ignore_errors', 'action', 'name', 'include', 'when', 'become', 'become_user', 'become_method', 'connection'])

# Generated at 2022-06-13 17:29:16.730266
# Unit test for function get_reserved_names
def test_get_reserved_names():
    print('RESERVED NAMES:', _RESERVED_NAMES)
    assert 'name' in _RESERVED_NAMES
    assert 'roles' in _RESERVED_NAMES
    assert 'hosts' in _RESERVED_NAMES
    assert 'gather_facts' in _RESERVED_NAMES
    assert 'tasks' in _RESERVED_NAMES
    assert 'block' in _RESERVED_NAMES
    assert 'action' in _RESERVED_NAMES
    assert 'local_action' in _RESERVED_NAMES
    assert 'with_' in _RESERVED_NAMES
    assert 'loop' in _RESERVED_NAMES
    assert 'ignore_errors' in _RESERVED_NAMES

# Generated at 2022-06-13 17:29:25.994129
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved = get_reserved_names()
    assert 'pre_tasks' in reserved
    assert 'post_tasks' in reserved
    assert 'roles' in reserved
    assert 'tasks' in reserved
    assert 'block' in reserved
    assert 'action' in reserved
    assert 'include_role' in reserved
    assert 'include_tasks' in reserved
    assert 'tags' in reserved
    assert 'vars' in reserved
    assert 'defaults' in reserved
    assert 'private' not in reserved
    assert 'connection' in reserved
    assert 'become' in reserved
    assert 'become_method' in reserved
    assert 'become_user' in reserved
    assert 'hosts' in reserved
    assert 'gather_facts' in reserved
    assert 'delegate_to' in reserved

# Generated at 2022-06-13 17:29:30.703004
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved_names = get_reserved_names()
    assert isinstance(reserved_names, set)
    assert 'pre_tasks' in reserved_names
    assert 'hosts' in reserved_names


# Generated at 2022-06-13 17:29:37.468262
# Unit test for function get_reserved_names
def test_get_reserved_names():
    result = get_reserved_names(include_private=True)
    assert isinstance(result, set)
    assert len(result) > 1
    assert 'hosts' in result
    assert 'action' in result
    assert 'include' in result

    result = get_reserved_names(include_private=False)
    assert isinstance(result, set)
    assert len(result) > 1
    assert 'hosts' in result
    assert 'action' in result
    assert 'include' in result
    assert not 'prompt' in result



# Generated at 2022-06-13 17:29:40.333746
# Unit test for function get_reserved_names
def test_get_reserved_names():
    try:
        get_reserved_names(include_private=True)
    except:
        assert False



# Generated at 2022-06-13 17:29:58.583320
# Unit test for function get_reserved_names
def test_get_reserved_names():
    '''
    This function is called by test_reserved_names.py
    '''
    reserved = get_reserved_names()

# Generated at 2022-06-13 17:30:07.107948
# Unit test for function get_reserved_names
def test_get_reserved_names():
    expected = ['become',
                'become_method',
                'become_user',
                'block',
                'connection',
                'delegate_to',
                'environment',
                'ignore_errors',
                'name',
                'register',
                'remote_user',
                'sudo',
                'sudo_user',
                'tags',
                'transport',
               ]

    public_names = get_reserved_names(include_private=False)
    assert sorted(expected) == sorted(list(public_names))


# Generated at 2022-06-13 17:30:12.692946
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # Create an example empty play
    pb = Play().load({}, variable_manager={}, loader=None)

    # Make sure the play has correct number of keys
    assert len(pb.__dict__) == len(_RESERVED_NAMES)

    # Check if each key is in reserved names
    for key in pb.__dict__:
        assert key in _RESERVED_NAMES

# Generated at 2022-06-13 17:30:17.802574
# Unit test for function get_reserved_names
def test_get_reserved_names():
    test_data = [("play1", "play1"),
                 ("action1", "action1"),
                 ("local_action", "local_action"),
                 ("with_items", "with_items")]
    for name, expected_reserved_name in test_data:
        assert is_reserved_name(name) == expected_reserved_name

# Generated at 2022-06-13 17:30:25.641898
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:30:28.684126
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' test that get_reserved_names function returns a set of variables '''
    result = get_reserved_names()
    assert isinstance(result, set)

# Generated at 2022-06-13 17:30:34.967434
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved = get_reserved_names()
    # tests for private which are subject to change
    assert 'environment' in reserved
    assert 'when' in reserved
    assert 'roles' in reserved
    assert 'include' in reserved
    assert 'vars_files' in reserved
    assert 'tags' in reserved
    assert 'gather_facts' in reserved
    assert 'roles' in reserved
    assert 'include' in reserved
    assert 'block' in reserved
    assert 'rescue' in reserved
    assert 'always' in reserved
    assert 'notify' in reserved
    assert 'handler' in reserved
    assert 'register' in reserved
    assert 'failed_when' in reserved
    assert 'loop' in reserved
    assert 'with_' in reserved
    assert 'local_action' in reserved
    assert 'connection' in reserved

# Generated at 2022-06-13 17:30:38.044236
# Unit test for function get_reserved_names
def test_get_reserved_names():

    reserved = get_reserved_names()
    assert 'roles' in reserved
    assert 'tasks' in reserved
    assert 'block' in reserved
    assert 'ignore_errors' in reserved

# Generated at 2022-06-13 17:30:47.687657
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:30:49.281764
# Unit test for function get_reserved_names
def test_get_reserved_names():
    result = get_reserved_names()
    assert 'name' in result
    assert 'hosts' in result



# Generated at 2022-06-13 17:31:13.342390
# Unit test for function get_reserved_names
def test_get_reserved_names():
    all_reserved = {'become', 'become_method', 'become_user', 'block', 'connection',
                    'delegate_to', 'environment', 'failed_when', 'gather_facts', 'ignore_errors',
                    'include', 'include_vars', 'local_action', 'loop', 'module_defaults',
                    'name', 'no_log', 'notify', 'parallel', 'pause', 'pre_tasks', 'post_tasks',
                    'remote_user', 'role', 'roles', 'serial', 'tags', 'task', 'tasks',
                    'vars', 'vars_files', 'vars_prompt', 'vault_password_file', 'when'}

# Generated at 2022-06-13 17:31:18.206902
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert 'tags' in get_reserved_names()
    assert 'include' in get_reserved_names()
    assert 'roles' in get_reserved_names(include_private=False)
    assert 'when' in get_reserved_names()

# Generated at 2022-06-13 17:31:21.947478
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved = get_reserved_names()
    assert 'roles' in reserved
    assert 'environment' in reserved
    assert 'vars' in reserved
    assert 'hosts' in reserved
    assert 'when' in reserved


# brute force unit test for is_reserved_name
# FIXME: find a way to 'not hardcode'

# Generated at 2022-06-13 17:31:29.419300
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved_names = get_reserved_names()
    assert 'name' in reserved_names
    assert 'hosts' in reserved_names
    assert 'user' in reserved_names
    assert 'host_pattern' in reserved_names
    assert 'vars' in reserved_names
    assert 'tags' in reserved_names
    assert 'when' in reserved_names
    assert 'gather_facts' in reserved_names
    assert 'delegate_to' in reserved_names
    assert 'sudo' in reserved_names
    assert 'action' in reserved_names
    assert 'local_action' in reserved_names
    assert 'with_' in reserved_names
    assert 'with_items' in reserved_names
    assert 'with_fileglob' in reserved_names
    assert 'with_first_found' in reserved_names

# Generated at 2022-06-13 17:31:30.720746
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert ('hosts' in get_reserved_names())

# Generated at 2022-06-13 17:31:35.151396
# Unit test for function get_reserved_names
def test_get_reserved_names():
    all_reserved_names = get_reserved_names(True)
    assert 'name' in all_reserved_names
    assert 'private' in all_reserved_names
    assert all_reserved_names == _RESERVED_NAMES

    public_reserved_names = get_reserved_names(False)
    assert 'name' in public_reserved_names
    assert 'private' not in public_reserved_names



# Generated at 2022-06-13 17:31:41.613462
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:31:49.304311
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:31:58.645211
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' This function tests a list of reserved names in play objects'''

    reserved_names = get_reserved_names()
    assert 'hosts' in reserved_names

    reserved_names = get_reserved_names(False)
    assert 'hosts' in reserved_names

    try:
        reserved_names = get_reserved_names(include_private=1)
    except TypeError:
        assert True
    else:
        assert False

    try:
        reserved_names = get_reserved_names(include_private='true')
    except TypeError:
        assert True
    else:
        assert False

# Generated at 2022-06-13 17:32:07.874190
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:32:44.258933
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert 'hosts' in _RESERVED_NAMES
    assert 'roles' in _RESERVED_NAMES
    assert 'tasks' in _RESERVED_NAMES
    assert 'action' in _RESERVED_NAMES
    assert 'local_action' in _RESERVED_NAMES
    assert 'with_' in _RESERVED_NAMES
    assert 'when' in _RESERVED_NAMES
    assert 'name' in _RESERVED_NAMES
    assert 'include' in _RESERVED_NAMES
    assert 'block' in _RESERVED_NAMES
    assert 'block' in _RESERVED_NAMES
    assert 'delegate_to' in _RESERVED_NAMES
    assert 'delegate_facts' in _

# Generated at 2022-06-13 17:32:53.303946
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert get_reserved_names(include_private=False) == frozenset(['gather_facts', 'hosts', 'name', 'serial', 'remote_user', 'sudo', 'sudo_user', 'vars', 'vars_files', 'include', 'roles', 'role_names', 'tasks', 'tags', 'task_tags', 'post_tasks', 'any_errors_fatal', 'always_run', 'connection', 'environment', 'no_log', 'poll', 'local_action', 'with_'])

# Generated at 2022-06-13 17:32:56.485356
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert 'connection' in get_reserved_names()
    assert 'sudo' in get_reserved_names()
    assert 'delegate_to' in get_reserved_names()



# Generated at 2022-06-13 17:32:58.758869
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved_names = get_reserved_names()
    assert isinstance(reserved_names, set)
    assert len(reserved_names) > 0



# Generated at 2022-06-13 17:33:00.613691
# Unit test for function get_reserved_names
def test_get_reserved_names():
    names = get_reserved_names()
    assert isinstance(names, set)
    assert 'loop' in names
    assert 'with_' in names

# Generated at 2022-06-13 17:33:04.987546
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # Calls function get_reserved_names and returns a set of reserved names
    # 1. Verify that no private names is included in reserved names
    # 2. Verify that 'hosts' is included in list of reserved names

    res_names = get_reserved_names(include_private=False)
    assert 'hosts' in res_names
    assert res_names.isdisjoint(get_reserved_names(include_private=True))

# Generated at 2022-06-13 17:33:12.252256
# Unit test for function get_reserved_names
def test_get_reserved_names():
    names = get_reserved_names()

    assert(names == frozenset({'action', 'local_action', 'with_', 'loop',
                              'name', 'block', 'include', 'vars', 'connection', 'gather_facts',
                              'delegate_to', 'run_once', 'ignore_errors', 'roles', 'tags', 'when',
                              'register', 'sudo', 'sudo_user', 'remote_user', 'environment',
                              'no_log', 'deprecated', 'delegate_facts', 'notify', 'async',
                              'poll', 'become', 'become_user', 'become_method'}))


# Generated at 2022-06-13 17:33:13.953488
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert isinstance(get_reserved_names(), set)
    assert isinstance(get_reserved_names(include_private=False), set)



# Generated at 2022-06-13 17:33:20.572761
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # Set the list of reserved name
    RESERVED = frozenset(get_reserved_names(include_private=True))
    PUBLIC = frozenset(get_reserved_names(include_private=False))

    # Test presence of essential public reserved names
    assert 'name' in PUBLIC
    assert 'roles' in PUBLIC
    assert 'tasks' in PUBLIC
    assert 'vars' in PUBLIC
    assert 'hosts' in PUBLIC

    # Test presence of essential private reserved names
    assert 'become' in RESERVED
    assert 'gather_facts' in RESERVED
    assert 'tags' in RESERVED

    # Test presence of public names in private names
    assert PUBLIC.issubset(RESERVED)

    # Test presence of some special names in private names
    assert 'action' in RES

# Generated at 2022-06-13 17:33:25.603700
# Unit test for function get_reserved_names
def test_get_reserved_names():
    '''
    Make sure key words are not added or removed.
    '''
    current_reserved_names = get_reserved_names()
    assert _RESERVED_NAMES == current_reserved_names

# Generated at 2022-06-13 17:33:56.297388
# Unit test for function get_reserved_names
def test_get_reserved_names():
    names = get_reserved_names()
    assert len(names) > 0
    assert 'name' in names

# Generated at 2022-06-13 17:34:05.050682
# Unit test for function get_reserved_names
def test_get_reserved_names():

    # test for no private vars
    public_only = frozenset([u'any_errors_fatal', u'async', u'become', u'become_flags', u'become_method', u'become_user', u'block', u'block_errors', u'connection', u'environment', u'failed_when', u'gather_facts', u'global_vars', u'handlers', u'hosts', u'max_fail_percentage', u'meta', u'name', u'no_log', u'post_tasks', u'pre_tasks', u'roles', u'serial', u'start_at_task', u'strategy', u'stats', u'tasks', u'timeout', u'transport', u'vars'])

    # test for all vars

# Generated at 2022-06-13 17:34:08.620703
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' returns a list of reserved names and checks length'''

    reserved_names = get_reserved_names()
    assert(len(reserved_names) > 50)
    assert(type(reserved_names) == set)


# Generated at 2022-06-13 17:34:18.335476
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert('action' in _RESERVED_NAMES)
    assert('block' in _RESERVED_NAMES)
    assert('handlers' in _RESERVED_NAMES)
    assert('roles' in _RESERVED_NAMES)
    assert('tasks' in _RESERVED_NAMES)
    assert('vars' in _RESERVED_NAMES)
    assert('any_errors_fatal' in _RESERVED_NAMES)
    assert('block' in _RESERVED_NAMES)
    assert('connection' in _RESERVED_NAMES)
    assert('delegate_to' in _RESERVED_NAMES)
    assert('gather_facts' in _RESERVED_NAMES)

# Generated at 2022-06-13 17:34:21.646829
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert isinstance(get_reserved_names(), frozenset)
    assert get_reserved_names() == _RESERVED_NAMES


# Generated at 2022-06-13 17:34:28.879026
# Unit test for function get_reserved_names
def test_get_reserved_names():
    expected = set([
        "tags", "ignore_errors", "any_errors_fatal", "always_run",
        "register", "vars", "vars_files", "block", "blockinfile",
        "when", "notify", "delegate_to", "local_action", "transport",
        "connection", "remote_user", "become", "become_user",
        "become_method", "become_flags", "failed_when", "environment",
        "args", "sudo", "sudo_user", "sudo_flags", "with_", "loop",
        "ignore_errors", "no_log", "always_run", "changed_when",
        "until", "retries", "delay", "poll", "first_available_file",
        "name",
    ])
    result = get

# Generated at 2022-06-13 17:34:32.674996
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved = get_reserved_names()
    # reserved should not be empty
    assert reserved is not None
    # loop implies with_
    assert 'with_' in reserved
    # local_action is implicit with action
    assert 'local_action' in reserved



# Generated at 2022-06-13 17:34:44.418163
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert get_reserved_names() == frozenset(['name', 'gather_facts', 'roles', 'vars', 'vars_prompt', 'vars_files', 'vars_prompt', 'when', 'include_role', 'include', 'hosts', 'pre_tasks', 'post_tasks', 'tasks', 'handlers', 'block', 'any_errors_fatal', 'become', 'become_user', 'become_method', 'tags', 'register', 'ignore_errors', 'local_action', 'connection', 'port', 'remote_user', 'environment', 'no_log', 'sudo', 'sudo_user', 'transport', 'delegate_to', 'with_', 'run_once', 'loop', 'until', 'listen', 'listen_task'])

# Generated at 2022-06-13 17:34:55.740042
# Unit test for function get_reserved_names
def test_get_reserved_names():
    '''
    unit test that validates a known set of reserved names for play
    objects. It does not validate the existence of the reserved name,
    rather the list of known reserved names.
    '''

    plays = (
        Play(),
        Role(),
        Block(),
        Task()
    )

    # list of known reserved names

# Generated at 2022-06-13 17:34:59.263186
# Unit test for function get_reserved_names
def test_get_reserved_names():

    reserved = list(get_reserved_names())
    assert len(reserved) > 0, "No reserved words returned from get_reserved_names"
    for attribute in reserved:
        assert isinstance(attribute, str), "Reserved name is not a string"

# Generated at 2022-06-13 17:36:08.705467
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert 'become' in _RESERVED_NAMES
    assert 'hosts' in _RESERVED_NAMES
    assert 'name' in _RESERVED_NAMES
    assert 'with_' in _RESERVED_NAMES
    assert 'block' not in _RESERVED_NAMES
    assert 'changed_when' not in _RESERVED_NAMES



# Generated at 2022-06-13 17:36:10.223220
# Unit test for function get_reserved_names
def test_get_reserved_names():

    assert isinstance(get_reserved_names(), set)


# Generated at 2022-06-13 17:36:11.947291
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert get_reserved_names() == _RESERVED_NAMES

# Generated at 2022-06-13 17:36:21.535876
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:36:31.162297
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:36:37.432206
# Unit test for function get_reserved_names
def test_get_reserved_names():

    reserved = get_reserved_names()
    assert 'name' in reserved
    assert 'hosts' in reserved
    assert 'roles' in reserved
    assert 'tasks' in reserved
    assert 'vars' in reserved
    assert 'roles' in reserved
    assert 'block' in reserved
    assert 'action' in reserved
    assert 'private' in reserved
    assert 'private' not in get_reserved_names(False)
    assert 'local_action' in get_reserved_names(False)

# Generated at 2022-06-13 17:36:45.579483
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert 'roles' in get_reserved_names()

    # if 'limit' is not in reserved names, this fails
    # as we have an assertion in the Play class
    assert 'limit' in get_reserved_names()

    # add a dummy attribute
    class_list = [Play, Role, Block, Task]
    for aclass in class_list:
        aobj = aclass()
        aobj._attributes = {'dummy': None}
    assert 'dummy' in get_reserved_names()

    # limit should be in the public attributes
    public = set()
    private = set()
    class_list = [Play, Role, Block, Task]
    for aclass in class_list:
        aobj = aclass()

# Generated at 2022-06-13 17:36:51.691965
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved = get_reserved_names()
    assert len(reserved) > 0
    assert isinstance(reserved, set)
    assert is_reserved_name('hosts')
    assert is_reserved_name('connection')
    assert is_reserved_name('vars')
    assert not is_reserved_name('fred')

# Generated at 2022-06-13 17:36:56.650262
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert(set(get_reserved_names(include_private=False)).issuperset(['name', 'hosts', 'roles', 'tasks', 'connection']))
    assert(set(get_reserved_names(include_private=True)).issuperset(['name', 'hosts', 'roles', 'tasks', 'connection', 'with_', 'local_action', 'loop', 'delegate_to', 'register']))

# Generated at 2022-06-13 17:37:00.479491
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' test the get_reserved_names function '''
    result = get_reserved_names(include_private=False)

    assert isinstance(result, set)
    assert 'action' in result
    assert 'local_action' in result
    assert 'with_' in result
    assert 'loop' not in result

