

# Generated at 2022-06-13 17:28:55.994968
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:29:07.233176
# Unit test for function get_reserved_names
def test_get_reserved_names():
    public = set()
    private = set()
    public.add('name')
    public.add('connection')
    public.add('delegate_to')
    public.add('become')
    public.add('become_user')
    public.add('check_mode')
    public.add('gather_facts')
    public.add('hosts')
    public.add('roles')
    public.add('serial')
    public.add('tasks')
    public.add('vars')

    private.add('any_errors_fatal')
    private.add('force_handlers')
    private.add('ignore_errors')
    private.add('no_log')
    private.add('post_tasks')
    private.add('pre_tasks')


# Generated at 2022-06-13 17:29:15.595909
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:29:25.589186
# Unit test for function get_reserved_names
def test_get_reserved_names():
    public = frozenset(['vars', 'name', 'hosts', 'user', 'connection', 'gather_facts', 'become', 'become_method', 'become_user', 'tags', 'any_errors_fatal', 'delegate_to', 'serial', 'run_once', 'remote_user', 'ignore_errors', 'force_handlers', 'roles', 'tasks', 'block', 'handlers', 'post_tasks', 'pre_tasks', 'include', 'include_role', 'dependencies', 'register', 'environment', 'no_log', 'check_mode', 'force_debug', 'ignore_warnings', 'changed_when', 'failed_when', 'always_run', 'local_action', 'with_'])

# Generated at 2022-06-13 17:29:36.976309
# Unit test for function get_reserved_names
def test_get_reserved_names():
    got = get_reserved_names()
    assert type(got) == set
    assert len(got) > 2
    assert 'hosts' in got
    assert is_reserved_name('hosts')
    assert 'action' in got
    assert is_reserved_name('action')
    assert not is_reserved_name('whatever')
    assert 'connection' in got
    assert is_reserved_name('connection')
    assert 'role_name' in got
    assert 'become' in got
    assert is_reserved_name('become')
    assert 'tags' in got
    assert is_reserved_name('tags')
    assert 'ignore_errors' in got
    assert is_reserved_name('ignore_errors')
    assert 'delegate_to' in got
    assert is_reserved_name

# Generated at 2022-06-13 17:29:40.221376
# Unit test for function get_reserved_names
def test_get_reserved_names():

    assert Play.RESERVED in get_reserved_names()
    assert 'roles' in get_reserved_names()
    assert 'tags' in get_reserved_names()

# Generated at 2022-06-13 17:29:46.788065
# Unit test for function get_reserved_names
def test_get_reserved_names():
    private = get_reserved_names(include_private=False)
    public = get_reserved_names(include_private=True)

    assert(type(private) is set)
    assert(type(public) is set)

    assert(len(private) > 0)
    assert(len(public) > 0)

    assert(len(private) < len(public))
    assert(public.issuperset(private))



# Generated at 2022-06-13 17:29:53.046448
# Unit test for function get_reserved_names
def test_get_reserved_names():

    aa = get_reserved_names(include_private=True)
    assert aa
    assert len(aa) > 20

    ab = get_reserved_names(include_private=False)
    assert ab
    assert len(ab) > 20
    assert len(ab) < len(aa)
    assert ab.issubset(aa)

# Generated at 2022-06-13 17:30:00.874321
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:30:05.406830
# Unit test for function get_reserved_names
def test_get_reserved_names():

    reserved_names = get_reserved_names()

    # Reserved names
    assert 'name' in reserved_names
    assert 'tags' in reserved_names
    assert 'any_errors_fatal' in reserved_names
    assert 'action' in reserved_names
    assert 'local_action' in reserved_names
    assert 'with_' in reserved_names

# Generated at 2022-06-13 17:30:23.270646
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert get_reserved_names() == _RESERVED_NAMES

# Generated at 2022-06-13 17:30:30.930788
# Unit test for function get_reserved_names
def test_get_reserved_names():

    assert len(_RESERVED_NAMES) == 13
    assert 'name' in _RESERVED_NAMES
    assert 'action' in _RESERVED_NAMES
    assert 'hosts' in _RESERVED_NAMES
    assert 'tags' in _RESERVED_NAMES
    assert 'local_action' in _RESERVED_NAMES
    assert 'register' in _RESERVED_NAMES
    assert 'error_on_undefined_vars' in _RESERVED_NAMES



# Generated at 2022-06-13 17:30:42.423256
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # determine the expected set of reserved names for public/private
    expected = set()
    for attrs in Play()._attributes:
        if 'private' in attrs:
            expected.add(attrs)
        elif attrs == 'action':
            expected.add('action')
            expected.add('local_action')
        elif attrs == 'loop':
            expected.add('loop')
            expected.add('with_')
        else:
            expected.add(attrs)
    for attrs in Role()._attributes:
        if 'private' in attrs:
            expected.add(attrs)
        elif attrs == 'action':
            expected.add('action')
            expected.add('local_action')
        elif attrs == 'loop':
            expected.add('loop')

# Generated at 2022-06-13 17:30:49.434456
# Unit test for function get_reserved_names
def test_get_reserved_names():

    display.deprecated('Test function test_get_reserved_names is a deprecated function and will be removed in future versions.')

    # test getting just public names
    public = get_reserved_names(include_private=False)
    assert 'roles' not in public
    assert 'loop' not in public
    assert 'action' in public
    assert 'local_action' in public

    # test getting all names
    all_names = get_reserved_names(include_private=True)
    assert 'roles' in all_names
    assert 'loop' in all_names
    assert 'action' in all_names
    assert 'local_action' in all_names



# Generated at 2022-06-13 17:30:51.136221
# Unit test for function get_reserved_names
def test_get_reserved_names():
    p = Play()
    print(p.__dict__)
    print(get_reserved_names())

# Generated at 2022-06-13 17:30:59.780462
# Unit test for function get_reserved_names
def test_get_reserved_names():
    failed = False

    # Playbook
    # reserved: connection, gather_facts, name, remote_user, serial, strategy, sudo, sudo_user, 
    #           tags, when
    # private:  become, become_user, hosts, any_errors_fatal, blocks, delegate_to, error_on_undefined_vars, 
    #           environment, ignore_errors, max_fail_pct, no_log, play_hosts, post_tasks, pre_tasks, roles, 
    #           register, handlers, tasks, vars_files, vars_prompt, vars, vars_plugins 
    public = ['connection', 'gather_facts', 'name', 'remote_user', 'serial', 'strategy', 'sudo',
              'sudo_user', 'tags', 'when']

# Generated at 2022-06-13 17:31:04.089845
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # Test if the reserved set contains a reserved name
    assert 'action' in get_reserved_names(include_private=True)

    # Test if the reserved set doesn't contain a non-reserved name
    assert 'book' not in get_reserved_names()

    # Test if the non-private reserved set contains a non-private reserved name
    assert 'vars_files' in get_reserved_names(include_private=False)

    # Test if the non-private reserved set doesn't contain a private reserved name
    assert 'inventory' not in get_reserved_name

# Generated at 2022-06-13 17:31:13.695675
# Unit test for function get_reserved_names
def test_get_reserved_names():
    public = frozenset(['hosts', 'roles', 'tasks', 'vars', 'name', 'environment', 'tags', 'gather_facts', 'ignore_errors', 'port', 'serial', 'transport', 'accelerate', 'setup_cache_timeout', 'remote_user', 'connection', 'su', 'su_user', 'sudo', 'sudo_user', 'su_flags', 'sudo_flags', 'no_log', 'run_once', 'any_errors_fatal', 'poll', 'action', 'local_action', 'with_', 'delegate_to', 'delegate_facts', 'notify', 'listen', 'register'])

# Generated at 2022-06-13 17:31:17.423638
# Unit test for function get_reserved_names
def test_get_reserved_names():
    result = get_reserved_names()
    assert len(result) > 1
    assert 'hosts' in result
    assert 'name' in result

# Generated at 2022-06-13 17:31:25.450578
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # Get public reserved names
    __reserved_names = get_reserved_names(False)
    assert 'name' in __reserved_names
    assert 'gather_facts' in __reserved_names
    assert 'register' in __reserved_names
    assert 'tags' in __reserved_names
    assert 'connection' in __reserved_names
    assert 'any_errors_fatal' in __reserved_names
    assert 'serial' in __reserved_names
    assert 'max_fail_percentage' in __reserved_names
    assert 'local_action' in __reserved_names
    # Get private reserved names
    __reserved_names = get_reserved_names()
    assert 'when' in __reserved_names
    assert 'with_' in __reserved_names

# Generated at 2022-06-13 17:32:03.608605
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' return list of reserved names'''
    reserved = get_reserved_names()
    assert isinstance(reserved, set)
    assert 'hosts' in reserved
    assert 'tasks' in reserved
    assert 'playbook' in reserved
    # assert 'block' in reserved
    assert 'action' in reserved
    assert 'ignore_errors' in reserved
    assert 'any_errors_fatal' in reserved

# Generated at 2022-06-13 17:32:09.962630
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' check if the reserved names are as documented '''
    # test1: check if this list is up-to-date
    assert len(get_reserved_names()) > 60
    assert 'hosts' in get_reserved_names()
    assert 'roles' in get_reserved_names()
    assert 'tasks' in get_reserved_names()
    assert 'vars' in get_reserved_names()
    assert 'name' in get_reserved_names()
    assert 'environment' in get_reserved_names()
    assert 'block' in get_reserved_names()
    assert 'when' in get_reserved_names()
    assert 'action' in get_reserved_names()
    assert 'tags' in get_reserved_names()
    assert 'always_run' in get_res

# Generated at 2022-06-13 17:32:16.959259
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:32:26.361591
# Unit test for function get_reserved_names
def test_get_reserved_names():
    from ansible.vars import VariableManager
    from collections import namedtuple

    myvars = VariableManager()

    def get_reserved_name_set(include_private=True):
        result = get_reserved_names(include_private)
        return set(result)

    # FIXME: add more basic tests, to make sure that we're handling cases correctly
    test_case = namedtuple('test_case', 'name_set, include_private, expected_result')

# Generated at 2022-06-13 17:32:30.181586
# Unit test for function get_reserved_names
def test_get_reserved_names():
    result = get_reserved_names(include_private=True)
    assert 'ignore_errors' in result
    # this is not a reserved name:
    assert 'foo' not in result


# Generated at 2022-06-13 17:32:39.042955
# Unit test for function get_reserved_names
def test_get_reserved_names():

    # dicts to compare reserved names against
    reserved_public = {
        'action',
        'async',
        'become',
        'become_user',
        'block',
        'connection',
        'delegate_to',
        'delegate_facts',
        'environment',
        'group_by',
        'hosts',
        'ignore_errors',
        'include_vars',
        'loops',
        'local_action',
        'name',
        'no_log',
        'notify',
        'notified_by',
        'post_tasks',
        'pre_tasks',
        'roles',
        'run_once',
        'serial',
        'tasks',
        'tags',
        'vars',
    }

    reserved_public_

# Generated at 2022-06-13 17:32:40.723055
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # The 'vars' name is not a reserved name.
    assert 'vars' not in _RESERVED_NAMES


# Generated at 2022-06-13 17:32:44.743403
# Unit test for function get_reserved_names
def test_get_reserved_names():
    class_name = 'TestVar'
    obj = eval(class_name)()
    if set(obj.__dict__['_attributes']) != _RESERVED_NAMES:
        raise AssertionError("Reserved names differ from actual names")

# Generated at 2022-06-13 17:32:53.598235
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:33:00.573335
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved_names = get_reserved_names()
    assert 'hosts' in reserved_names
    assert 'roles' in reserved_names
    assert 'name' in reserved_names
    assert 'name' in reserved_names
    assert 'connection' in reserved_names
    assert 'gather_facts' in reserved_names
    assert 'tags' in reserved_names
    assert 'failed_when' in reserved_names
    assert 'ignore_errors' in reserved_names
    assert 'always_run' in reserved_names
    assert 'when' in reserved_names
    assert 'local_action' in reserved_names

# Generated at 2022-06-13 17:33:39.709580
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert get_reserved_names(include_private=True) == _RESERVED_NAMES
    assert get_reserved_names(include_private=False) == frozenset([
        'gather_facts', 'tasks', 'handlers', 'pre_tasks', 'post_tasks', 'notify', 'roles', 'tags', 'vars_files', 'vars_prompt',
        'vars_files_encoding', 'name', 'action', 'local_action', 'with_', 'block', 'rescue', 'always', 'delegate_to', 'become'
    ])

# Generated at 2022-06-13 17:33:41.470903
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert 'include' in get_reserved_names()
    assert 'include_tasks' in get_reserved_names()
    assert 'include_role' in get_reserved_names(include_private=False)
    assert 'include_role' not in get_reserved_names()

# Generated at 2022-06-13 17:33:48.802272
# Unit test for function get_reserved_names
def test_get_reserved_names():
    p = get_reserved_names(include_private=False)
    a = frozenset(['roles', 'hosts', 'connection', 'vars', 'any_errors_fatal',
                   'delegate_to', 'gather_facts', 'environment', 'remote_user',
                   'sudo_user', 'sudo', 'sudo_flags', 'no_log', 'no_target_syslog',
                   'register', 'ignore_errors', 'until', 'retries', 'delay',
                   'poll', 'tags', 'env', 'block', 'when', 'local_action', 'with_'])
    assert p == a
    p = get_reserved_names(include_private=True)

# Generated at 2022-06-13 17:33:50.751228
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert len(get_reserved_names()) == 25



# Generated at 2022-06-13 17:34:00.886068
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved = sorted(get_reserved_names(False))

    assert len(reserved) > 0
    assert 'any_errors_fatal' in reserved
    assert 'async' in reserved
    assert 'become_user' in reserved
    assert 'become' in reserved
    assert 'block' in reserved
    assert 'delegate_to' in reserved
    assert 'delimiter' in reserved
    assert 'first_available_file' in reserved
    assert 'group' in reserved
    assert 'ignore_errors' in reserved
    assert 'include' in reserved
    assert 'include_role' in reserved
    assert 'include_vars' in reserved
    assert 'local_action' in reserved
    assert 'loop' in reserved
    assert 'loop_control' in reserved
    assert 'name' in reserved
    assert 'notify' in reserved

# Generated at 2022-06-13 17:34:07.609959
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:34:17.514120
# Unit test for function get_reserved_names
def test_get_reserved_names():

    class TestPlay(Play):
        def __init__(self):
            self.hosts = 'hosts'
            self.roles = 'roles'
            super(Play,self).__init__()

    test_class_list = [TestPlay, Role, Block, Task]
    test_reserved_names = get_reserved_names()

    # check that all reserved_names are in class attribute lists
    for aclass in test_class_list:
        assert all(attr in aclass().__dict__.keys() for attr in test_reserved_names)

    # check that all class attribute lists are in reserved_names
    for aclass in test_class_list:
        assert all(attr in test_reserved_names for attr in aclass().__dict__.keys())



# Generated at 2022-06-13 17:34:23.551782
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert _RESERVED_NAMES == frozenset(('block', 'block', 'connection', 'with_', 'gather_facts', 'ignore_errors',
                                         'no_log', 'notify', 'register', 'remote_user', 'roles', 'serial', 'sudo',
                                         'sudo_user', 'tasks', 'transport', 'vars_files', 'vars_prompt', 'tags',
                                         'when'))



# Generated at 2022-06-13 17:34:29.859623
# Unit test for function get_reserved_names
def test_get_reserved_names():
    RESERVED_NAMES = get_reserved_names()
    assert isinstance(RESERVED_NAMES, set), "get_reserved_names() must return a set"
    assert len(RESERVED_NAMES) > 0, "get_reserved_names() must return a set with length > 0"
    assert 'hosts' in RESERVED_NAMES, "hosts is a reserved name and should be in the reserved set"
    assert 'roles' in RESERVED_NAMES, "roles is a reserved name and should be in the reserved set"
    assert 'tasks' in RESERVED_NAMES, "tasks is a reserved name and should be in the reserved set"

# Generated at 2022-06-13 17:34:37.516669
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' unit test for get_reserved_names function '''

    assert set(get_reserved_names()) == get_reserved_names()  # test for consistent return
    assert 'name' in get_reserved_names()  # should be a standard attribute found
    assert 'vars' in get_reserved_names()  # should be a standard attribute found
    assert 'private' not in get_reserved_names(include_private=False)  # should be private attribute found
    assert 'private' in get_reserved_names()  # should be private attribute found
    assert 'action' in get_reserved_names()  # action is an explicit attr, but local_action is not
    assert 'local_action' in get_reserved_names()  # action is an explicit attr, but local_action is not

# Generated at 2022-06-13 17:35:45.847706
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert type(get_reserved_names()) is frozenset
    assert type(get_reserved_names()) is set

# Generated at 2022-06-13 17:35:53.934694
# Unit test for function get_reserved_names
def test_get_reserved_names():
    public = get_reserved_names(False) or set()

# Generated at 2022-06-13 17:36:02.043463
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:36:10.225245
# Unit test for function get_reserved_names
def test_get_reserved_names():
    """
    This function tests get_reserved_names function
    """

    #test reserved public names consist only of public names
    reserved_public = get_reserved_names(False)
    reserved_private = get_reserved_names(True)

    #test private names are filtered from public names
    assert not (reserved_public & get_reserved_names(True))

    #test public and private names are filtered from reserved names
    assert not reserved_public.difference(get_reserved_names(True))
    assert not reserved_private.difference(get_reserved_names(True))

# Generated at 2022-06-13 17:36:16.283663
# Unit test for function get_reserved_names
def test_get_reserved_names():
    '''This function tests the function get_reserved_names, for correctness '''
    import pprint
    assert isinstance(get_reserved_names(), set)
    assert isinstance(get_reserved_names(include_private=False), set)
    assert get_reserved_names(include_private=True) == get_reserved_names(include_private=False).union(set(['hosts', 'name', 'serial']))

# Generated at 2022-06-13 17:36:19.274246
# Unit test for function get_reserved_names
def test_get_reserved_names():
    test_result = get_reserved_names()
    assert 'hosts' in test_result
    assert 'tasks' in test_result
    assert 'name' in test_result


# Generated at 2022-06-13 17:36:22.620256
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # simplified test for non-blank reserved names
    assert get_reserved_names() != set()

    # test that loop implies with_
    # FIXME: remove after with_ is not only deprecated but removed
    assert 'loop' in get_reserved_names()
    assert 'with_' in get_reserved_names()

# Generated at 2022-06-13 17:36:33.218682
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:36:44.044631
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:36:47.908950
# Unit test for function get_reserved_names
def test_get_reserved_names():
    expected = set(['any_errors_fatal', 'become', 'become_method', 'become_user', 'block', 'connection', 'delegate_to',
                    'environment', 'ignore_errors', 'local_action', 'loop', 'name', 'other_action', 'pause', 'role',
                    'serial', 'with_', 'when', 'with_items', 'with_subelements', 'with_fileglob', 'with_filetree'])
    result = get_reserved_names()
    assert result == expected