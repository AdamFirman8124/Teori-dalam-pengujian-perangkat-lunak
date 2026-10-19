

# Generated at 2022-06-13 17:28:56.406440
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # We should get a list of names from get_reserved_names
    names = get_reserved_names()
    assert isinstance(names, set) and names

    # YAML keys for these should be reserved:
    for name in names:
        assert is_reserved_name(name)

    # YAML keys for these should be unreserved:
    for name in ('playbook', 'play', 'role', 'task', 'include', 'block', 'tasks', 'handlers'):
        assert not is_reserved_name(name)



# Generated at 2022-06-13 17:29:05.037898
# Unit test for function get_reserved_names
def test_get_reserved_names():
    test_public = get_reserved_names(include_private=False)
    test_private = get_reserved_names(include_private=True)

    assert 'name' in test_private
    assert 'name' in test_public
    assert 'include_tasks' in test_private
    assert 'include_tasks' in test_public
    assert 'local_action' in test_private
    assert 'local_action' in test_public
    assert 'action' in test_public
    assert 'action' not in test_private
    assert 'with_' in test_private
    assert 'loop' in test_private

# Generated at 2022-06-13 17:29:13.396388
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:29:15.831930
# Unit test for function get_reserved_names
def test_get_reserved_names():

    # for now, just test the actual value of the set
    assert type(get_reserved_names()) == set
    assert len(get_reserved_names()) == 143

# Generated at 2022-06-13 17:29:25.738097
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:29:37.157871
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:29:48.179285
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert get_reserved_names() == frozenset(['gather_facts', 'hosts', 'ignore_errors', 'roles', 'blocks', 'vars', 'tasks', 'name', 'register', 'block', 'error', 'when', 'local_action', 'with_', 'become', 'become_user', 'become_method', 'delegate_to'])
    assert get_reserved_names(include_private=False) == frozenset(['gather_facts', 'hosts', 'ignore_errors', 'roles', 'blocks', 'vars', 'tasks', 'name', 'register', 'block', 'error', 'when', 'local_action', 'become', 'become_user', 'become_method', 'delegate_to'])


# Generated at 2022-06-13 17:29:51.166996
# Unit test for function get_reserved_names
def test_get_reserved_names():

    # Public
    assert 'hosts' in _RESERVED_NAMES

    # Private
    assert 'register' in _RESERVED_NAMES



# Generated at 2022-06-13 17:29:58.440203
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved_names = get_reserved_names()
    assert 'hosts' in reserved_names
    assert 'delegate_to' in reserved_names
    assert 'register' in reserved_names
    assert 'roles' in reserved_names
    assert 'vars' in reserved_names
    assert 'action' in reserved_names
    assert 'local_action' in reserved_names
    assert 'loop' in reserved_names
    assert 'with_' in reserved_names
    assert 'when' in reserved_names
    assert 'meta' in reserved_names



# Generated at 2022-06-13 17:30:04.234685
# Unit test for function get_reserved_names
def test_get_reserved_names():
    p = Play()
    p._load_included_file = True
    p.vars = dict()
    p.post_validate(dict(), dict())

    # Add a variable to a play, it should return a warning
    p.vars = dict(gather_facts=True)
    p.post_validate(dict(), dict())
    assert (len(p._deprecations) == 1)
    assert (p._deprecations[0].deprecated_args[0] == 'gather_facts')

# Generated at 2022-06-13 17:30:14.269176
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert not _RESERVED_NAMES.issuperset(set(['foo', 'bar']))

# Generated at 2022-06-13 17:30:17.733670
# Unit test for function get_reserved_names
def test_get_reserved_names():
    names = get_reserved_names()

    assert 'roles' in names
    assert 'tasks' in names
    assert 'vars' in names
    assert 'private' not in names
    assert 'role_path' not in names
    assert 'connection' not in names
    assert 'any_errors_fatal' in names
    assert 'gather_facts' in names



# Generated at 2022-06-13 17:30:24.794221
# Unit test for function get_reserved_names
def test_get_reserved_names():
    private = get_reserved_names(include_private=True)
    public = get_reserved_names(include_private=False)

    assert 'hosts' in public
    assert 'hosts' in private
    assert 'action' in public
    assert 'action' in private
    assert 'local_action' in private
    assert 'local_action' in private
    assert 'loop' in private
    assert 'loop' not in public
    assert 'with_' in private
    assert 'with_' not in public

    # we've added local_action to hosts
    assert 'local_action' in private

    # we've added with_ to loop
    assert 'with_' in private



# Generated at 2022-06-13 17:30:31.099031
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' test function get_reserved_names '''

    # make sure we get a set
    result = get_reserved_names()
    assert isinstance(result, set) is True

    # make sure no names are repeated
    temp = set()
    for key in result:
        if key in temp:
            assert False
        else:
            temp.add(key)


# unit test for function warn_if_reserved

# Generated at 2022-06-13 17:30:42.560304
# Unit test for function get_reserved_names
def test_get_reserved_names():

    # Test set of reserved names
    reserved_names = get_reserved_names()
    assert 'hosts' in reserved_names
    assert 'vars' in reserved_names
    assert 'roles' in reserved_names
    assert 'block' in reserved_names
    assert 'rescue' in reserved_names
    assert 'always' in reserved_names
    assert 'local_action' in reserved_names
    assert 'action' in reserved_names
    assert 'loop' in reserved_names
    assert 'with_' in reserved_names

    # Test set of reserved private names
    reserved_names = get_reserved_names(include_private=True)
    assert '[]' in reserved_names
    assert 'register' in reserved_names
    assert 'ignore_errors' in reserved_names


# unit test for function warn_if_res

# Generated at 2022-06-13 17:30:46.645608
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # assert that names are all unique across public and private
    public_names = set(get_reserved_names(include_private=False))
    private_names = set(get_reserved_names(include_private=True)) - public_names
    assert len(public_names.intersection(private_names)) == 0



# Generated at 2022-06-13 17:30:56.680823
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert 'hosts' in get_reserved_names()
    assert 'roles' in get_reserved_names()
    assert 'tasks' in get_reserved_names()
    assert 'pre_tasks' in get_reserved_names()
    assert 'post_tasks' in get_reserved_names()
    assert 'block' in get_reserved_names()
    assert 'include' in get_reserved_names()
    assert 'vars' in get_reserved_names()
    assert 'vars_files' in get_reserved_names()
    assert 'vars_prompt' in get_reserved_names()
    assert 'name' in get_reserved_names()
    assert 'debug' in get_reserved_names(include_private=False)
    assert 'notify' in get

# Generated at 2022-06-13 17:31:06.088865
# Unit test for function get_reserved_names
def test_get_reserved_names():

    result = get_reserved_names(include_private=False)

    assert 'action' in result
    assert 'local_action' in result
    assert 'loop' in result
    assert 'with_' in result
    assert 'roles' in result
    assert 'tasks' in result
    assert 'handlers' in result
    assert 'block' in result
    assert 'block' in result
    assert 'when' in result
    assert 'always' in result
    assert 'changed_when' in result
    assert 'failed_when' in result
    assert 'include' in result
    assert 'include_role' in result
    assert 'meta' in result
    assert 'name' in result
    assert 'register' in result
    assert 'tags' in result
    assert 'vars' in result

# Generated at 2022-06-13 17:31:10.795726
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert _RESERVED_NAMES.__class__ is frozenset
    assert u'block' in _RESERVED_NAMES
    assert u'block' in _RESERVED_NAMES
    assert u'roles' in _RESERVED_NAMES
    assert u'private' not in _RESERVED_NAMES

# Generated at 2022-06-13 17:31:12.331998
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ansible_reserved_names = get_reserved_names()
    assert ansible_reserved_names is not None
    assert isinstance(ansible_reserved_names, set)
    assert (len(ansible_reserved_names) > 0)

# Generated at 2022-06-13 17:31:33.845351
# Unit test for function get_reserved_names
def test_get_reserved_names():

    assert 'any_errors_fatal' in get_reserved_names()
    assert 'with_' in get_reserved_names()
    assert 'private' not in get_reserved_names()
    assert 'private' in get_reserved_names(include_private=True)



# Generated at 2022-06-13 17:31:42.716786
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # This test uses private attributes for checking reserved names, but
    # those attributes and structure may change in the future.
    assert "vars" in get_reserved_names()
    assert "vars" in get_reserved_names(include_private=True)
    assert "vars_files" in get_reserved_names()
    assert "vars_files" in get_reserved_names(include_private=True)
    assert "no_log" in get_reserved_names()
    assert "no_log" in get_reserved_names(include_private=True)
    assert "hosts" in get_reserved_names()
    assert "hosts" in get_reserved_names(include_private=True)
    assert "gather_facts" in get_reserved_names()

# Generated at 2022-06-13 17:31:50.125950
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:31:55.950367
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert 'any_errors_fatal' in get_reserved_names()
    assert 'roles' in get_reserved_names()
    assert 'block' in get_reserved_names()
    assert 'hosts' in get_reserved_names()
    assert 'when' in get_reserved_names()



# Generated at 2022-06-13 17:32:01.562687
# Unit test for function get_reserved_names
def test_get_reserved_names():
    result = get_reserved_names(True)

    assert 'roles' in result
    assert 'run_once' in result
    assert 'become' in result
    assert 'gather_facts' in result
    assert 'vars' in result

    result = get_reserved_names(False)

    assert 'roles' in result
    assert 'run_once' in result
    assert 'become' in result
    assert 'gather_facts' in result
    assert 'vars' in result

    assert 'name' in result
    assert 'task_vars' in result
    assert 'delegate_to' in result
    assert 'local_action' in result
    assert 'register' in result

    assert 'block' not in result
    assert 'rescue' not in result
    assert 'always' not in result
   

# Generated at 2022-06-13 17:32:07.531198
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert('hosts' in get_reserved_names())
    assert('roles' in get_reserved_names())
    assert('vars' in get_reserved_names())
    assert('gather_facts' in get_reserved_names())
    assert('private' in get_reserved_names(include_private=False))
    assert('private' not in get_reserved_names())

    # FIXME: other tests could be added for Task/Block, etc

# Generated at 2022-06-13 17:32:12.035884
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved = set(get_reserved_names(include_private=True))

# Generated at 2022-06-13 17:32:23.385968
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:32:29.888107
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:32:35.714930
# Unit test for function get_reserved_names
def test_get_reserved_names():
    func = get_reserved_names
    assert func()


# Generated at 2022-06-13 17:33:17.566303
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:33:29.893672
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:33:31.656421
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' testing get_reserved_names function '''
    assert isinstance(get_reserved_names(False), set)



# Generated at 2022-06-13 17:33:41.319667
# Unit test for function get_reserved_names
def test_get_reserved_names():
    public_names = frozenset('''
    authority
    ignore_errors
    no_log
    roles
    tasks
    tags
    when
    ''').split()
    public_names.extend('connection delegate_to remote_tmp run_once sudo_user')
    # collect the private vars
    private_names = frozenset('''
    _role
    ''').split()
    private_names.extend('_%s' % name for name in public_names)
    public_names.extend('''
    action
    block
    delegate_facts
    hostvars
    inventory_hostname
    inventory_hostname_short
    play_hosts
    ''')

# Generated at 2022-06-13 17:33:48.740937
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' this function tests if the reserved names are what expected '''

    # hard coded list of reserved names

# Generated at 2022-06-13 17:33:58.854174
# Unit test for function get_reserved_names
def test_get_reserved_names():
    r = get_reserved_names(include_private=False)
    assert isinstance(r, set)
    assert 'vars' in r
    assert 'name' in r
    assert 'block' in r
    assert 'include_role' in r
    assert 'include_tasks' in r
    assert 'include' not in r
    assert 'pre_tasks' in r
    assert 'post_tasks' in r
    assert 'handler_tasks' in r
    assert 'tasks' in r
    assert 'role_paths' in r
    assert 'collections' in r

    r = get_reserved_names(include_private=True)
    assert isinstance(r, set)
    assert 'vars' in r
    assert 'name' in r
    assert 'block' in r

# Generated at 2022-06-13 17:34:01.465844
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert isinstance(get_reserved_names(), frozenset)
    assert get_reserved_names() == _RESERVED_NAMES

# Generated at 2022-06-13 17:34:03.225176
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert isinstance(_RESERVED_NAMES, frozenset)
    assert len(_RESERVED_NAMES) == 27



# Generated at 2022-06-13 17:34:07.513595
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert get_reserved_names() == get_reserved_names(include_private=True)
    assert get_reserved_names(include_private=False) < get_reserved_names(include_private=True)
    assert len(get_reserved_names()) > 40

# Generated at 2022-06-13 17:34:17.434215
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:35:29.416151
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved = get_reserved_names()
    reserved_private = get_reserved_names(include_private=True)

# Generated at 2022-06-13 17:35:36.468889
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert get_reserved_names() == _RESERVED_NAMES, \
        "Returned reserved names do not match expected"
    assert "hosts" in get_reserved_names(), \
        "hosts should be a reserved name"
    assert "roles" in get_reserved_names(), \
        "roles should be a reserved name"
    assert "name" in get_reserved_names(), \
        "name should be a reserved name"

# Generated at 2022-06-13 17:35:44.358168
# Unit test for function get_reserved_names
def test_get_reserved_names():

    # Check against known list of public names
    public_names = ['roles', 'tasks', 'name', 'vars', 'pre_tasks', 'post_tasks',\
                    'handlers', 'tags', 'register', 'connection', 'vars_files',\
                    'include_vars', 'any_errors_fatal', 'max_fail_percentage', \
                    'gather_facts', 'remote_user', 'sudo', 'sudo_user', 'transport',\
                    'notify', 'changed_when' ]

    assert(sorted(_RESERVED_NAMES.intersection(public_names)) == sorted(public_names))

# Generated at 2022-06-13 17:35:52.313367
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:36:00.865089
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:36:12.333168
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:36:14.538175
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert isinstance(get_reserved_names(), set)
    assert len(get_reserved_names()) > 10



# Generated at 2022-06-13 17:36:19.833012
# Unit test for function get_reserved_names
def test_get_reserved_names():
    names = get_reserved_names()
    assert 'hosts' in names
    assert 'name' in names
    assert 'gather_facts' in names
    assert 'vars' in names
    assert 'block' in names
    assert 'connection' in names
    assert 'local_action' in names
    assert 'register' not in names
    assert 'with_' in names



# Generated at 2022-06-13 17:36:26.439407
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # print(get_reserved_names())
    reserved = get_reserved_names()
    assert "name" in reserved
    assert "action" in reserved
    assert "local_action" in reserved
    assert "delegate_to" in reserved
    assert "become" in reserved
    assert "become_user" in reserved
    assert "become_method" in reserved
    assert "vars_files" in reserved
    assert "vars_prompt" in reserved
    assert "vars" in reserved
    assert "include" not in reserved
    assert "register" in reserved
    assert "connection" in reserved
    assert "gather_facts" in reserved
    assert "environment" in reserved
    assert "pre_tasks" in reserved
    assert "post_tasks" in reserved
    assert "tasks" in reserved
   

# Generated at 2022-06-13 17:36:33.217371
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert set(get_reserved_names()) == _RESERVED_NAMES
    assert set(get_reserved_names(True)) == _RESERVED_NAMES
    assert set(get_reserved_names(False)) == \
        _RESERVED_NAMES.difference(set(('vars', 'tags')))
    assert set(get_reserved_names(False)).isdisjoint(_RESERVED_NAMES)

