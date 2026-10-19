

# Generated at 2022-06-13 17:28:57.896738
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # Verify the returned list only contains public names
    assert get_reserved_names(include_private=False) == set([
            'name', 'connection', 'remote_user', 'gather_facts', 'vars_prompt', 'vars_files', 'include', 'when',
            'environment', 'ignore_errors', 'serial', 'sudo_user', 'sudo', 'sudo_pass', 'tags', 'register',
            'no_log', 'other', 'local_action', 'with_'])

    # Verify the returned list contains both public and private names

# Generated at 2022-06-13 17:29:03.530101
# Unit test for function get_reserved_names
def test_get_reserved_names():
    private_names = frozenset(get_reserved_names(include_private=True))
    assert 'name' in private_names
    assert 'action' in private_names
    assert 'local_action' in private_names
    assert 'loop' in private_names
    public_names = frozenset(get_reserved_names(include_private=False))
    assert public_names.isdisjoint(private_names)

# Generated at 2022-06-13 17:29:05.892856
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert get_reserved_names() == _RESERVED_NAMES
    assert 'name' in _RESERVED_NAMES


# Generated at 2022-06-13 17:29:12.196372
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved = get_reserved_names()
    public = get_reserved_names(include_private=False)
    assert 'name' in reserved
    assert 'name' in public
    assert 'action' in reserved
    assert 'action' in public
    assert 'local_action' in reserved
    assert 'local_action' not in public
    assert 'loop' in reserved
    assert 'loop' not in public
    assert 'with_' in reserved
    assert 'with_' not in public
    assert 'with_items' in reserved
    assert 'with_items' in public


# Generated at 2022-06-13 17:29:14.781858
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert 'name' in get_reserved_names()
    assert 'private' in get_reserved_names(True)
    assert not 'private' in get_reserved_names(False)

# Generated at 2022-06-13 17:29:18.498225
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert isinstance(_RESERVED_NAMES, frozenset)
    assert isinstance(get_reserved_names(), set)
    assert isinstance(get_reserved_names(include_private=False), set)

# Generated at 2022-06-13 17:29:20.552744
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved = get_reserved_names()
    assert isinstance(reserved, set)
    assert 'name' in reserved



# Generated at 2022-06-13 17:29:28.459090
# Unit test for function get_reserved_names
def test_get_reserved_names():
    result = sorted(get_reserved_names())

# Generated at 2022-06-13 17:29:37.812575
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' this test function checks if any new attributes have been added and if these have been added
        to the list of reserved names.
    '''
    reserved_names = get_reserved_names()
    assert 'action' in reserved_names, 'action is a reserved name'
    assert 'private' in reserved_names, 'private is a reserved name'
    assert 'local_action' in reserved_names, 'local_action is a reserved name'
    assert 'loop' in reserved_names, 'loop is a reserved name'
    assert 'vars' not in reserved_names, 'vars is not a reserved name'
    assert 'not_defined_attribute' not in reserved_names, 'not_defined_attribute is not a reserved name'
    assert 'name' not in reserved_names, 'name is not a reserved name'

# Generated at 2022-06-13 17:29:49.157913
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:30:10.714876
# Unit test for function get_reserved_names
def test_get_reserved_names():

    # Should not contain include_vars
    assert "include_vars" not in get_reserved_names(include_private=False)

    # Should contain include_vars
    assert "include_vars" in get_reserved_names(include_private=True)

# Generated at 2022-06-13 17:30:12.158746
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved = get_reserved_names()
    assert isinstance(reserved, set)
    assert 'connection' in reserved



# Generated at 2022-06-13 17:30:18.443097
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:30:28.932217
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:30:40.380086
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

# Generated at 2022-06-13 17:30:49.217996
# Unit test for function get_reserved_names
def test_get_reserved_names():
    '''
    This function unit tests function get_reserved_names.
    '''
    result = get_reserved_names(include_private=True)

# Generated at 2022-06-13 17:30:53.952265
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # Test inclusion of private names
    assert isinstance(get_reserved_names(), frozenset)
    assert len(get_reserved_names()) > 0
    assert len(get_reserved_names(True)) > len(get_reserved_names(False))
    # Test exclusion of 'vars' from reserved names
    assert 'vars' not in _RESERVED_NAMES

# Generated at 2022-06-13 17:31:00.859259
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # Set of reserved names should be frozen
    assert isinstance(_RESERVED_NAMES, frozenset)

    for k in _RESERVED_NAMES:
        assert k in get_reserved_names()

    assert is_reserved_name('action')
    assert is_reserved_name('loop')
    assert is_reserved_name('include')
    assert is_reserved_name('include_role')
    assert is_reserved_name('when')

    # private attributes should not be returned by default
    assert 'meta' not in get_reserved_names()
    assert 'async' not in get_reserved_names()

    assert 'meta' in get_reserved_names(include_private=True)
    assert 'async' in get_reserved_names(include_private=True)



# Generated at 2022-06-13 17:31:04.376256
# Unit test for function get_reserved_names
def test_get_reserved_names():
    public = get_reserved_names(False)
    assert 'vars' not in public
    assert 'roles' not in public
    private = get_reserved_names(True)
    assert 'roles' in private

# Generated at 2022-06-13 17:31:07.590010
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:31:46.772244
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert frozenset(get_reserved_names(True)) == _RESERVED_NAMES

# Generated at 2022-06-13 17:31:58.183963
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:32:07.450737
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:32:14.590559
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved_names = get_reserved_names()

    # First, test that all public names are in the class

# Generated at 2022-06-13 17:32:19.952759
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert 'name' in get_reserved_names()
    assert 'hosts' in get_reserved_names()
    assert 'action' in get_reserved_names()
    assert 'local_action' in get_reserved_names()
    assert 'local_action' not in get_reserved_names(include_private=False)


# Generated at 2022-06-13 17:32:27.855754
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert(_RESERVED_NAMES == frozenset(get_reserved_names()))


# Static list generated by test_get_reserved_names()

# Generated at 2022-06-13 17:32:36.429488
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # Test if reserved names are retrieved properly
    reserved_names = get_reserved_names()
    assert 'hosts' in reserved_names
    assert 'roles' in reserved_names
    assert 'pre_tasks' in reserved_names

    # Test if private names are retrieved properly
    private_names = get_reserved_names(include_private=False)
    assert 'hosts' in private_names
    assert 'roles' in private_names
    assert 'pre_tasks' in private_names
    assert 'register' in private_names
    assert 'changed_when' not in private_names
    assert 'with_items' not in private_names

# Generated at 2022-06-13 17:32:39.736069
# Unit test for function get_reserved_names
def test_get_reserved_names():
    import time
    import doctest
    now = time.time()
    doctest.testmod(verbose=False)
    elapsed = time.time() - now
    print("%d examples, %.3f seconds" % (doctest.master.summarize(True)[0], elapsed))



# Generated at 2022-06-13 17:32:50.255759
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:32:53.922702
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert get_reserved_names(include_private=True) == frozenset(['block', 'connection', 'delegate_to', 'environment', 'become', 'gather_facts', 'hosts',
                                                                 'no_log', 'notify', 'anything_else_which_does_not_actually_exist_but_the_key_is_the_value',
                                                                 'post_validate', 'pre_validate', 'roles', 'serial', 'tasks', 'when', 'with_', 'local_action',
                                                                 'failed_when', 'register', 'ignore_errors', 'loop'])


# Generated at 2022-06-13 17:34:05.027141
# Unit test for function get_reserved_names
def test_get_reserved_names():
    result = frozenset(get_reserved_names(include_private=False))
    assert result == _RESERVED_NAMES, result

# Generated at 2022-06-13 17:34:11.336083
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved_names = get_reserved_names(True)
    assert 'delegate_to' in reserved_names
    assert 'item' in reserved_names
    assert 'loop' in reserved_names
    assert 'name' in reserved_names
    assert 'private' in reserved_names
    assert 'server' in reserved_names
    assert 'tags' in reserved_names
    assert 'when' in reserved_names
    assert 'with_' not in reserved_names


# Generated at 2022-06-13 17:34:17.396633
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' This function tests the function get_reserved_names() '''

    names = get_reserved_names()
    # test for length
    assert len(names) == 50
    # test for a few known names
    assert 'vars' in names
    assert 'block' in names
    assert 'notify' in names
    assert 'register' in names
    assert 'run_once' in names
    assert 'import_tasks' in names


# Generated at 2022-06-13 17:34:26.152255
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:34:35.305761
# Unit test for function get_reserved_names
def test_get_reserved_names():
    public = ['hosts', 'name', 'register', 'connection', 'remote_user', 'sudo', 'sudo_user', 'transport', 'any_errors_fatal', 'delegate_to', 'action', 'local_action', 'with_', 'ignore_errors', 'gather_facts', 'tags', 'vars']
    private = ['become', 'become_method', 'become_user', 'check_mode', 'no_log', 'environment', 'when', 'async', 'poll']

    reserved = get_reserved_names()
    public_reserved = get_reserved_names(include_private=False)

    # order doesn't matter, use sets
    assert reserved >= set(public)
    assert reserved >= set(private)

    # check private items are excluded when asked

# Generated at 2022-06-13 17:34:45.789150
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ansible = get_reserved_names(include_private=False)

    assert 'name' in ansible
    assert 'action' in ansible
    assert 'delegate_to' in ansible
    assert 'delegate_facts' in ansible
    assert 'environment' in ansible
    assert 'tags' in ansible
    assert 'register' in ansible

    assert 'local_action' in ansible
    assert 'with_' in ansible

    assert 'when' not in ansible
    assert 'loop' not in ansible
    assert 'vars' not in ansible

    all = get_reserved_names(include_private=True)

    assert 'name' in all
    assert 'action' in all
    assert 'delegate_to' in all
    assert 'delegate_facts' in all
    assert 'environment'

# Generated at 2022-06-13 17:34:50.272874
# Unit test for function get_reserved_names
def test_get_reserved_names():
    """Test that all the attributes in a Play object are returned by
    get_reserved_names"""
    play = Play()
    reserved_names = set()
    for attr in play.__dict__['_attributes']:
        reserved_names.add(attr)

    assert reserved_names == _RESERVED_NAMES

# Generated at 2022-06-13 17:35:01.532247
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert_msg = "Expected '{0}' to be in reserved names: {1}"

# Generated at 2022-06-13 17:35:07.698170
# Unit test for function get_reserved_names
def test_get_reserved_names():
    from ansible.playbook.role.includes import _included_filenames
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject

    reserved = get_reserved_names(include_private=False).union(_included_filenames)
    reserved = reserved.union(AnsibleBaseYAMLObject.defined_tags)
    assert reserved == _RESERVED_NAMES

# Generated at 2022-06-13 17:35:16.291401
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:36:39.596194
# Unit test for function get_reserved_names
def test_get_reserved_names():

    # This function will return a set of strings, therefore this cannot be a simple == test
    # We'll need to convert the set returned from the function to a list to compare
    public = sorted(list(get_reserved_names(include_private=False)))
    private = sorted(list(get_reserved_names(include_private=True)))


# Generated at 2022-06-13 17:36:44.180047
# Unit test for function get_reserved_names
def test_get_reserved_names():
    global _RESERVED_NAMES

    # _RESERVED_NAMES is filled at module load. Because of the way things are
    # loaded, the unit test will be run after _RESERVED_NAMES is set. So we
    # just need to declare a new nameset to compare against

    reserved_by_class = get_reserved_names()

    assert _RESERVED_NAMES == reserved_by_class

# Generated at 2022-06-13 17:36:49.434538
# Unit test for function get_reserved_names
def test_get_reserved_names():
    public_names = get_reserved_names(False)
    private_names = get_reserved_names(True)

    # Test public names
    assert 'hosts' in public_names
    assert 'name' in public_names
    assert 'roles' in public_names
    assert 'tasks' in public_names
    assert 'when' in public_names
    assert len(public_names) == 8

    # Test private names
    assert 'action' in private_names
    assert 'block' in private_names
    assert 'include_tasks' in private_names
    assert 'include_vars' in private_names
    assert 'loop' in private_names
    assert 'tags' in private_names
    assert 'vars' in private_names
    assert len(private_names) == 32

# Generated at 2022-06-13 17:36:58.881590
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:37:06.809175
# Unit test for function get_reserved_names
def test_get_reserved_names():

    # reference variables
    play_vars = frozenset(['name', 'hosts', 'gather_facts', 'pre_tasks', 'roles', 'tasks', 'post_tasks', 'any_errors_fatal',
                           'serial', 'max_fail_percentage', 'vars_prompt', 'vars_files', 'tags', 'handlers'])

    role_vars = frozenset(['dependencies', 'default_vars', 'vars', 'handlers', 'pre_tasks', 'post_tasks', 'tasks',
                           'tasks_from', 'meta', 'file_dependencies', 'role_path', 'prerequisites', 'always_run'])


# Generated at 2022-06-13 17:37:08.148219
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert 'gather_facts' in get_reserved_names()
    assert 'roles' in get_reserved_names()



# Generated at 2022-06-13 17:37:14.772047
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:37:17.458010
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved_names = get_reserved_names()
    assert isinstance(reserved_names, set)
    assert 'tasks' in reserved_names
    assert 'hosts' in reserved_names

# Generated at 2022-06-13 17:37:24.938651
# Unit test for function get_reserved_names
def test_get_reserved_names():
    all_names = get_reserved_names()
    private_names = get_reserved_names(include_private=False)
    private_names.discard('action')  # action includes local_action
    private_names.discard('loop')  # loop implies with_

    assert 'action' in all_names
    assert 'local_action' in all_names
    assert 'local_action' not in private_names

    assert 'loop' in all_names
    assert 'loop' in private_names
    assert 'with_' in all_names
    assert 'with_' not in private_names

# Generated at 2022-06-13 17:37:28.185442
# Unit test for function get_reserved_names
def test_get_reserved_names():

    # Test that public and private reserved names are returned
    assert 'hosts' in get_reserved_names()
    assert 'local_action' in get_reserved_names()
    assert 'become' in get_reserved_names()
    assert 'connection' in get_reserved_names()

    # Test that private reserved names are not returned when include_private=False
    assert 'become' in get_reserved_names(include_private=False)
    assert 'connection' not in get_reserved_names(include_private=False)