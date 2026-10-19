

# Generated at 2022-06-13 17:28:45.345364
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert len(get_reserved_names()) == 91
    assert len(get_reserved_names(include_private=False)) == 29



# Generated at 2022-06-13 17:28:55.805457
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:29:04.845256
# Unit test for function get_reserved_names
def test_get_reserved_names():

    # check that at least some specific names we expect to be in the list are
    # this also gives us a chance to remove names from the above list that are
    # not actually being used currently. If this test fails, we should update
    # the list of reserved names defined above.
    reserved = _RESERVED_NAMES

    assert 'tasks' in reserved
    assert 'vars' in reserved
    assert 'action' in reserved
    assert 'local_action' in reserved
    assert 'include' in reserved
    assert 'loop' in reserved
    assert 'notify' in reserved
    assert 'async' in reserved

# Generated at 2022-06-13 17:29:13.286329
# Unit test for function get_reserved_names
def test_get_reserved_names():
    import json

    # There are 12 private attributes, so there should be a total of 60 reserved names.
    assert len(get_reserved_names()) == 60

    # A lot of reserved names are not private, so if the private names are excluded we should still have 45 reserved names.
    assert len(get_reserved_names(include_private=False)) == 45

    # Actually make sure that each of the private attributes are removed from the list.
    # We can't just read in a file, since the order of items in a set is not preserved across Python versions.
    with open('lib/ansible/playbook/reserved_names.json') as reserved_names_fp:
        public_reserved_names = json.load(reserved_names_fp)
        public_reserved_names = frozenset(public_reserved_names)

# Generated at 2022-06-13 17:29:23.617576
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert isinstance(get_reserved_names(), set)
    assert isinstance(get_reserved_names(False), set)
    assert is_reserved_name('action')
    assert is_reserved_name('become')
    assert is_reserved_name('block')
    assert is_reserved_name('block:')
    assert is_reserved_name('connection')
    assert is_reserved_name('environment')
    assert is_reserved_name('gather_facts')
    assert is_reserved_name('hosts')
    assert is_reserved_name('hosts:')
    assert is_reserved_name('include')
    assert is_reserved_name('include_tasks')
    assert is_reserved_name('import_playbook')

# Generated at 2022-06-13 17:29:35.151599
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' unit test to check the list of reserved names '''

    # non-privates
    assert 'playbook' in get_reserved_names()
    assert is_reserved_name('playbook')
    assert 'strategy' in get_reserved_names()
    assert is_reserved_name('strategy')
    assert 'hosts' in get_reserved_names()
    assert is_reserved_name('hosts')
    assert 'roles' in get_reserved_names()
    assert is_reserved_name('roles')
    assert 'name' in get_reserved_names()
    assert is_reserved_name('name')
    assert 'tags' in get_reserved_names()
    assert is_reserved_name('tags')
    assert 'loop' in get_reserved_names()

# Generated at 2022-06-13 17:29:41.437936
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved_names = get_reserved_names()
    assert 'name' in reserved_names
    assert 'notify' in reserved_names
    assert 'private' not in reserved_names
    assert 'action' in reserved_names
    assert 'local_action' in reserved_names
    assert 'loop' not in reserved_names
    assert 'with_' in reserved_names

# Generated at 2022-06-13 17:29:50.901682
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' this function tests the function get_reserved_names'''
    global _RESERVED_NAMES
    # Call the method without specifying include_private
    result1 = get_reserved_names()
    # Call the method by specifying include_private to be false
    result2 = get_reserved_names(include_private=False)
    # Build a set of public attributes
    public = set()
    private = set()
    public_ans = set()
    private_ans = set()
    class_list = [Play, Role, Block, Task]

    for aclass in class_list:
        aobj = aclass()
        # build ordered list to loop over and dict with attributes
        for attribute in aobj.__dict__['_attributes']:
            if 'private' in attribute:
                private.add(attribute)

# Generated at 2022-06-13 17:30:00.088373
# Unit test for function get_reserved_names
def test_get_reserved_names():

    expected_public = frozenset(['strategy', 'pre_tasks', 'post_tasks', 'connection', 'sudo', 'sudo_user', 'delegate_to', 'async', 'poll', 'when', 'serial', 'tags', 'any_errors_fatal', 'action', 'local_action', 'with_', 'vars_files', 'with_items', 'environment', 'role_paths', 'roles_path', 'become', 'become_method', 'become_user', 'transport', 'remote_user', 'register', 'ignore_errors', 'always_run', 'notify', 'handlers', 'hosts', 'name', 'include', 'gather_facts', 'gather_subset', 'gather_timeout', 'tasks', 'task_paths', 'ignore_unreachable'])

   

# Generated at 2022-06-13 17:30:03.586532
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # verify that all reserved names are listed in _RESERVED_NAMES
    result = set()
    for _ in get_reserved_names(include_private=False), get_reserved_names(include_private=True):
        result.update(_)
    assert _RESERVED_NAMES == result

# Generated at 2022-06-13 17:30:25.357529
# Unit test for function get_reserved_names
def test_get_reserved_names():

    expected_public = frozenset([
        'connection', 'any_errors_fatal', 'any_errors_fatal_continue', 'become', 'become_flags', 'become_method', 'become_user',
        'check_mode', 'delegate_to', 'environment', 'groups', 'hosts', 'inventory_hostname', 'inventory_hostname_short', 'no_log',
        'notify', 'name', 'remote_user', 'serial', 'tags', 'vars', 'when', 'with_items', 'with_subelements', 'with_sequence',
        'when', 'roles'
    ])


# Generated at 2022-06-13 17:30:28.884021
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved_names = get_reserved_names()
    assert 'name' in reserved_names
    assert 'loop' in reserved_names
    assert 'with_items' in reserved_names

# Generated at 2022-06-13 17:30:40.333925
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:30:44.111757
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved_names = get_reserved_names()
    assert 'tasks' in reserved_names
    assert 'hosts' in reserved_names
    assert 'action' in reserved_names
    assert 'loop' in reserved_names
    assert 'local_action' in reserved_names

# Generated at 2022-06-13 17:30:46.726470
# Unit test for function get_reserved_names
def test_get_reserved_names():
    result = get_reserved_names()
    assert result == _RESERVED_NAMES

    result = get_reserved_names(include_private=False)
    assert result != _RESERVED_NAMES

# Generated at 2022-06-13 17:30:51.979512
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved_names = get_reserved_names()
    # check contents
    assert 'name' in reserved_names
    assert 'roles' in reserved_names
    # check that reserved names are not added
    assert 'silly_name' not in reserved_names
    # and that the private ones are not included in the public list
    assert 'connection' not in reserved_names


# Generated at 2022-06-13 17:30:56.923879
# Unit test for function get_reserved_names
def test_get_reserved_names():

    reserved = get_reserved_names()
    assert 'hosts' in reserved
    assert 'with_' in reserved
    assert 'loop' in reserved
    assert 'register' in reserved

    reserved = get_reserved_names(include_private=False)
    assert 'hosts' in reserved
    assert 'with_' in reserved
    assert 'loop' not in reserved
    assert 'register' not in reserved

# Generated at 2022-06-13 17:31:00.200871
# Unit test for function get_reserved_names
def test_get_reserved_names():
    test_names = ['vars_files', 'remote_user', 'roles', 'tags']
    reserved_names = get_reserved_names()
    for name in test_names:
        assert name in reserved_names, \
            "test_get_reserved_names: name %s not in reserved_names" % name

# Generated at 2022-06-13 17:31:10.407616
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:31:18.031518
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved = get_reserved_names()
    assert 'name' in reserved
    assert 'hosts' in reserved
    assert 'roles' in reserved
    assert 'tasks' in reserved
    assert 'vars' in reserved

    reserved = get_reserved_names(include_private=False)
    assert 'name' in reserved
    assert 'hosts' in reserved
    assert 'roles' in reserved
    assert 'tasks' in reserved
    assert 'vars' in reserved
    assert 'action' in reserved
    assert 'local_action' in reserved
    assert 'with_' in reserved
    assert 'loop' not in reserved



# Generated at 2022-06-13 17:31:50.391162
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:31:54.424378
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert not set(['hosts', 'name']) - _RESERVED_NAMES
    assert _RESERVED_NAMES - set(['hosts', 'name'])



# Generated at 2022-06-13 17:31:56.618178
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert len(get_reserved_names(False)) > 0
    assert len(get_reserved_names(True)) > 0

# Generated at 2022-06-13 17:32:05.823316
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:32:11.378232
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:32:17.942697
# Unit test for function get_reserved_names
def test_get_reserved_names():
    from ansible.playbook.play_context import PlayContext

    assert 'action' in get_reserved_names()
    assert 'connection' in get_reserved_names()
    assert 'distribution' in get_reserved_names()
    assert 'error_on_undefined_vars' in get_reserved_names()
    assert 'host_list' in get_reserved_names()
    assert 'hosts' in get_reserved_names(False)
    assert 'ignore_unreachable' in get_reserved_names()
    assert 'name' in get_reserved_names()
    assert 'name' in get_reserved_names(False)
    assert 'no_log' in get_reserved_names()
    assert 'no_log' in get_reserved_names(False)

# Generated at 2022-06-13 17:32:26.907944
# Unit test for function get_reserved_names
def test_get_reserved_names():
    expected_reserved_names = frozenset(['hosts', 'pre_tasks', 'tasks', 'roles', 'post_tasks', 'block', 'handlers', 'action', 'any_errors_fatal', 'any_unreachable_fatal', 'always_run', 'become', 'become_method', 'become_user', 'connection', 'delegate_to', 'deprecate_tags', 'gather_facts', 'local_action', 'name', 'notify', 'register', 'serial', 'serial_failure_threshold', 'vars', 'vars_files', 'vars_prompt', 'vault_password_files'])
    actual_reserved_names = frozenset(get_reserved_names())

# Generated at 2022-06-13 17:32:31.130111
# Unit test for function get_reserved_names
def test_get_reserved_names():
    
    assert 'pre_tasks' in get_reserved_names()
    assert 'roles' in get_reserved_names()
    assert 'private_roles' in get_reserved_names()



# Generated at 2022-06-13 17:32:39.809380
# Unit test for function get_reserved_names
def test_get_reserved_names():

    # we need to use a set to compare since order can change
    assert set(get_reserved_names(include_private=False)) == {'roles', 'tasks', 'name', 'action', 'any_errors_fatal', 'connection', 'delegate_to', 'delegate_facts', 'gather_facts', 'ignore_errors', 'listen', 'local_action', 'max_fail_percentage', 'no_log', 'notify', 'post_tasks', 'pre_tasks', 'remote_user', 'serial', 'sudo', 'sudo_user', 'vars', 'vars_files', 'with_', 'with_file'}

# Generated at 2022-06-13 17:32:50.341346
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved = get_reserved_names()

    # Expected reserved words for all types
    common = [
        'block',
        'delegate_to',
        'gather_facts',
        'hosts',
        'name',
        'roles',
        'serial',
    ]
    # Expected reserved words for all types except Play
    non_play = [
        'action',
        'handler',
        'notify',
        'register',
        'tags',
        'when',
    ]

    for word in common:
        assert word in reserved

    for word in non_play:
        assert word in reserved

    for word in non_play + ['vars']:
        assert 'with_' + word not in reserved


# Generated at 2022-06-13 17:33:47.515694
# Unit test for function get_reserved_names
def test_get_reserved_names():
    """
    This function tests the get_reserved_names function.
    """

    pub_names = get_reserved_names(include_private=False)
    priv_names = get_reserved_names(include_private=True)

    assert isinstance(pub_names, set)
    assert isinstance(priv_names, set)

    assert pub_names.issubset(priv_names)
    assert not pub_names == priv_names

# Generated at 2022-06-13 17:33:51.225780
# Unit test for function get_reserved_names
def test_get_reserved_names():
    names = get_reserved_names()
    assert 'action' in names
    assert 'local_action' in names
    assert 'tags' in names
    assert 'delegate_to' in names
    assert 'with_' in names

# Generated at 2022-06-13 17:33:53.717666
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert isinstance(get_reserved_names(), set)
    assert set() != get_reserved_names()



# Generated at 2022-06-13 17:34:03.117000
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:34:13.327693
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' test function get_reserved_names() '''

    public_reserved_names = {'vars_files', 'name', 'register', 'action', 'when', 'local_action',
                             'with_', 'connection', 'remote_user', 'sudo', 'sudo_user', 'async', 'poll',
                             'become', 'become_user', 'become_method', 'environment', 'tags', 'any_errors_fatal',
                             'failed_when', 'ignore_errors', 'max_fail_percentage'}

    private_reserved_names = {'block', 'block_type', 'attributes', 'load_role', 'dep_chain', 'handler',
                              'play', 'post_validate', 'reset_connection', 'tags', '_role', 'transport'}

    actual

# Generated at 2022-06-13 17:34:17.353516
# Unit test for function get_reserved_names
def test_get_reserved_names():

    result = get_reserved_names(include_private=True)
    assert 'action' in result
    assert 'local_action' in result

    result = get_reserved_names(include_private=False)
    assert 'action' in result
    assert 'local_action' not in result

# Generated at 2022-06-13 17:34:23.662011
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' unit test for get_reserved_names function '''

    result = get_reserved_names()
    assert 'action' in result

    # for coverage, test private is only in private results
    result = get_reserved_names(include_private=False)
    assert 'action' in result
    assert 'private' not in result

    # make sure loop is included as with_
    result = get_reserved_names()

    assert 'loop' in result
    assert 'with_' in result

# Generated at 2022-06-13 17:34:30.830831
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # no public should be returned if include_private is not set
    assert not get_reserved_names(False)

    assert 'block' in get_reserved_names()
    assert 'vars' in get_reserved_names()
    assert 'action' in get_reserved_names()
    assert 'local_action' in get_reserved_names()
    assert 'loop' in get_reserved_names()



# Generated at 2022-06-13 17:34:32.675504
# Unit test for function get_reserved_names
def test_get_reserved_names():
    for name in _RESERVED_NAMES:
        # assert name starts with '_'
        assert name.startswith("_")

# Generated at 2022-06-13 17:34:44.417713
# Unit test for function get_reserved_names
def test_get_reserved_names():
    from ansible.playbook import Play
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.task import Task

    class MyTest(object):
        pass

    attribute_list = []
    attribute_list.extend(Play()._attributes)
    attribute_list.extend(Role()._attributes)
    attribute_list.extend(Block()._attributes)
    attribute_list.extend(Task()._attributes)

    a = MyTest()
    a.attribute_list = attribute_list
    a.public = []
    a.private = []
    a.result = []

    for attribute in a.attribute_list:
        if 'private' in attribute:
            a.private.append(attribute)
        else:
            a

# Generated at 2022-06-13 17:36:33.274505
# Unit test for function get_reserved_names
def test_get_reserved_names():
    names = frozenset(get_reserved_names())
    assert("vars" in names)
    assert("action" in names)
    assert("local_action" in names)
    assert("loop" in names)
    assert("with_" in names)

# Generated at 2022-06-13 17:36:41.193069
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved = get_reserved_names()
    assert isinstance(reserved, set)
    assert 'roles' in reserved
    assert 'tasks' in reserved
    assert 'hosts' in reserved
    assert 'vars_files' in reserved
    assert 'loop' not in reserved
    assert 'with_' not in reserved

    reserved = get_reserved_names(include_private=True)
    assert 'loop' in reserved
    assert 'with_' in reserved

# Generated at 2022-06-13 17:36:46.630860
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # unit test, 1: verify the function can be called and returns a set,
    # including the name 'vars'
    assert 'vars' in get_reserved_names()

    # unit test, 2: verify that if private names are not included (exclude_private=False)
    # that the 'loop' name is not in the set
    assert 'loop' not in get_reserved_names(include_private=False)

    # unit test, 3: verify that if private names are included (include_private=True)
    # that the 'loop' name is in the set
    assert 'loop' in get_reserved_names(include_private=True)



# Generated at 2022-06-13 17:36:56.689034
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:37:05.164912
# Unit test for function get_reserved_names
def test_get_reserved_names():
    all_reserved_names = set()
    all_reserved_names.add("action")
    all_reserved_names.add("any_errors_fatal")
    all_reserved_names.add("become")
    all_reserved_names.add("become_user")
    all_reserved_names.add("block")
    all_reserved_names.add("block_list")
    all_reserved_names.add("changed_when")
    all_reserved_names.add("connection")
    all_reserved_names.add("delegate_to")
    all_reserved_names.add("delegate_facts")
    all_reserved_names.add("environment")
    all_reserved_names.add("failed_when")

# Generated at 2022-06-13 17:37:05.949859
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert ('roles' in get_reserved_names())



# Generated at 2022-06-13 17:37:11.385694
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved_public = set(get_reserved_names(include_private=False))
    assert 'action' in reserved_public
    assert 'register' in reserved_public
    assert 'with_' in reserved_public
    assert 'with_items' not in reserved_public
    assert 'local_action' not in reserved_public
    reserved = set(get_reserved_names(include_private=True))
    assert 'action' in reserved
    assert 'register' in reserved
    assert 'with_' in reserved
    assert 'with_items' in reserved
    assert 'local_action' in reserved



# Generated at 2022-06-13 17:37:13.478884
# Unit test for function get_reserved_names
def test_get_reserved_names():
    public = get_reserved_names(include_private=False)
    private = get_reserved_names(include_private=True)

    assert len(public) == len(private)

# Generated at 2022-06-13 17:37:23.377556
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:37:25.976483
# Unit test for function get_reserved_names
def test_get_reserved_names():
    pub, priv = get_reserved_names()
    assert 'hosts' in pub
    assert 'action' in pub
    assert 'local_action' in pub

    assert priv

