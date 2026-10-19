

# Generated at 2022-06-13 17:28:44.883746
# Unit test for function warn_if_reserved
def test_warn_if_reserved():
    # Use a copy to test the function on
    myvars = _RESERVED_NAMES.copy()
    myvars.add('vars')
    myvars.add('foo')
    warn_if_reserved(myvars)



# Generated at 2022-06-13 17:28:47.145892
# Unit test for function warn_if_reserved
def test_warn_if_reserved():
    assert warn_if_reserved(['action', 'delegate_to', 'environment'], ['foo', 'bar']), "Should return True"


# Generated at 2022-06-13 17:28:50.665944
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved = get_reserved_names()
    assert reserved
    assert len(reserved) > 15  # checking that we have at least a few
    assert 'name' in reserved
    assert 'roles' in reserved
    assert 'action' in reserved



# Generated at 2022-06-13 17:28:53.242797
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert isinstance(get_reserved_names(), set)


# Generated at 2022-06-13 17:28:57.721656
# Unit test for function warn_if_reserved
def test_warn_if_reserved():

    # assert no error
    warn_if_reserved({},)
    warn_if_reserved({'var': 'foo'},)

    # assert throw error
    import pytest
    with pytest.raises(Exception) as excinfo:
        warn_if_reserved({'meta': 'foo'},)
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "Found variable using reserved name: meta"

# Generated at 2022-06-13 17:29:01.345409
# Unit test for function warn_if_reserved
def test_warn_if_reserved():
    warn_if_reserved(set(['vars']))
    warn_if_reserved(set(['vars', 'connection']))
    warn_if_reserved(set(['vars', 'name', 'action', 'loop']))
    warn_if_reserved(set(['vars', 'name', 'action', 'loop']), additional=[])

# Generated at 2022-06-13 17:29:03.045114
# Unit test for function warn_if_reserved
def test_warn_if_reserved():
    warn_if_reserved(('hosts', 'become', 'become_user'))

# Generated at 2022-06-13 17:29:12.162995
# Unit test for function warn_if_reserved
def test_warn_if_reserved():
    warn_if_reserved({'hosts': ['foo']})
    warn_if_reserved({'hosts': ['foo'], 'roles': 'bar'})  # roles is not a reserved name
    warn_if_reserved({'hosts': ['foo'], 'action': 'bar'})  # action is a reserved name
    warn_if_reserved({'hosts': ['foo'], 'local_action': 'bar'})  # local_action is a reserved name
    warn_if_reserved({'hosts': ['foo'], 'with_': 'bar'})  # with_ is a reserved name
    warn_if_reserved({'hosts': ['foo'], 'loop': 'bar'})  # with_ is a reserved name
    warn_if_reserved({'playbook': ['foo']})  #

# Generated at 2022-06-13 17:29:14.680826
# Unit test for function warn_if_reserved
def test_warn_if_reserved():
    ''' Return True if test is ok, False if there is a problem '''
    mydict = {}
    mydict['foo'] = 'bar'
    mydict['debug'] = False

    warn_if_reserved(mydict)

    return True

# Generated at 2022-06-13 17:29:24.811942
# Unit test for function get_reserved_names
def test_get_reserved_names():

    reserved_names = get_reserved_names()

# Generated at 2022-06-13 17:29:30.471364
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved_names = get_reserved_names()
    assert 'serial' in reserved_names
    assert 'strategy' in reserved_names

# Generated at 2022-06-13 17:29:34.516340
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert get_reserved_names(include_private=True) == _RESERVED_NAMES
    assert get_reserved_names(include_private=False) == _RESERVED_NAMES.difference(dict(private=None))


# Generated at 2022-06-13 17:29:36.630874
# Unit test for function get_reserved_names
def test_get_reserved_names():

    assert isinstance(get_reserved_names(), set)



# Generated at 2022-06-13 17:29:43.824632
# Unit test for function get_reserved_names
def test_get_reserved_names():

    # private names should be returned
    assert 'action' in get_reserved_names(include_private=True)

    # reserved public names
    assert 'hosts' in get_reserved_names()
    assert 'roles' in get_reserved_names()

    # non-reserved non-private names
    assert 'name' not in get_reserved_names()
    assert 'tags' not in get_reserved_names()

# Generated at 2022-06-13 17:29:45.566357
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert get_reserved_names()
    assert get_reserved_names(include_private=False)

# Generated at 2022-06-13 17:29:49.124347
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' this function tests the get_reserved_names function

    This is just a simple test to make sure the get_reserved_names function works as expected.
    '''

    reserved_names = get_reserved_names()
    assert 'vars' in reserved_names
    assert 'register' in reserved_names
    assert 'become' in reserved_names



# Generated at 2022-06-13 17:29:59.255912
# Unit test for function get_reserved_names
def test_get_reserved_names():

    # quick test to make sure we get the right number of public/private before we delve into them
    assert len(get_reserved_names(include_private=True)) > len(get_reserved_names(include_private=False))

    # quick test that we have the 'formal' reserved names as well
    assert len(_RESERVED_NAMES) > len(get_reserved_names(include_private=False))

    # basic test to make sure all names returned are 'valid'
    # FIXME: the names become invalid if there are 'dupe' names in the class (ie task and block)
    for name in get_reserved_names(include_private=True):
        assert hasattr(Task(), name) or hasattr(Play(), name) or hasattr(Block(), name) or hasattr(Role(), name)

# Generated at 2022-06-13 17:30:07.622987
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:30:13.310073
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # basic smoke test
    assert len(get_reserved_names()) > 0
    # check for known attribute that is not private
    assert 'name' in get_reserved_names()
    assert 'name' in get_reserved_names(include_private=False)
    # check for known attribute that is private
    assert 'become_user' in get_reserved_names()
    assert 'become_user' not in get_reserved_names(include_private=False)
    # check for known attribute that is private
    assert 'with_items' in get_reserved_names()
    assert 'with_items' not in get_reserved_names(include_private=False)

# Generated at 2022-06-13 17:30:19.570303
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:30:37.054457
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:30:39.130685
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert 'name' in get_reserved_names()
    assert 'register' in get_reserved_names(False)

# Generated at 2022-06-13 17:30:41.442343
# Unit test for function get_reserved_names
def test_get_reserved_names():

    # Test that all reserved names are present in the dict returned
    assert set(get_reserved_names()) >= _RESERVED_NAMES

# Generated at 2022-06-13 17:30:47.042305
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved = set(get_reserved_names(include_private=True))
    reserved_no_private = set(get_reserved_names(include_private=False))

    # with private
    assert 'name' in reserved
    assert 'vars' in reserved
    assert 'private' in reserved
    assert 'private' not in reserved_no_private

    # w/o private
    assert 'private' in reserved
    assert 'private' not in reserved_no_private

# Generated at 2022-06-13 17:30:48.953273
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert 'playbook' in get_reserved_names()



# Generated at 2022-06-13 17:30:52.967997
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert len(get_reserved_names()) == 36
    assert len(get_reserved_names(False)) == 25
    assert isinstance(get_reserved_names(), set)
    for r in get_reserved_names():
        assert isinstance(r, str)



# Generated at 2022-06-13 17:31:00.937277
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' this function tests the get_reserved_names function'''

    result = len(get_reserved_names())
    assert result > 20
    assert 'hosts' in get_reserved_names()
    assert 'roles' in get_reserved_names()

    public = get_reserved_names(include_private=False)
    assert 'hosts' in public
    assert 'roles' in public
    assert 'free_form' not in public
    assert 'delegate_to' in public
    assert 'condition' in public
    assert 'notify' in public

    private = get_reserved_names(include_private=True)
    assert 'hosts' in private
    assert 'roles' in private
    assert 'free_form' in private
    assert 'delegate_to' in private

# Generated at 2022-06-13 17:31:03.112577
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert isinstance(get_reserved_names(include_private=True), frozenset)

# Generated at 2022-06-13 17:31:04.996731
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert isinstance(_RESERVED_NAMES, frozenset)
    assert _RESERVED_NAMES != set()

# Generated at 2022-06-13 17:31:07.842288
# Unit test for function get_reserved_names
def test_get_reserved_names():
    result = get_reserved_names()
    # Check for 'hosts' as part of test
    assert 'hosts' in result
    assert isinstance(result, set)


# Generated at 2022-06-13 17:31:24.289843
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert isinstance(get_reserved_names(include_private=False), set)
    assert isinstance(get_reserved_names(include_private=True), set)
    assert 'hosts' in get_reserved_names(include_private=True)
    assert 'hosts' in get_reserved_names(include_private=False)
    assert 'become' in get_reserved_names(include_private=True)
    assert 'become' in get_reserved_names(include_private=False)
    assert 'gather_facts' in get_reserved_names(include_private=True)
    assert 'gather_facts' in get_reserved_names(include_private=False)
    assert 'vars' not in get_reserved_names(include_private=True)

# Generated at 2022-06-13 17:31:33.273229
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:31:42.299183
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert set(get_reserved_names(include_private=False)) == set(['gather_facts', 'name', 'roles', 'vars', 'any_errors_fatal', 'delegate_to', 'delegate_facts', 'register', 'ignore_errors', 'vars_prompt', 'vars_files', 'vars_prompt', 'action', 'local_action', 'with_'])

# Generated at 2022-06-13 17:31:49.848862
# Unit test for function get_reserved_names
def test_get_reserved_names():

    # Check that the function returns a set
    reserved = get_reserved_names()
    assert isinstance(reserved, set)

    # Check that the function returns a set of strings
    for name in reserved:
        assert isinstance(name, str), 'Found non-string in reserved name: %s' % name

    # Check that some specific values are included
    assert 'roles' in reserved
    assert 'tasks' in reserved
    assert 'action' in reserved
    assert 'with_items' in reserved
    assert 'with_dict' in reserved
    assert 'with_fileglob' in reserved
    assert 'with_first_found' in reserved
    assert 'with_lines' in reserved
    assert 'with_sequence' in reserved
    assert 'with_random_choice' in reserved
    assert 'with_nested' in reserved
   

# Generated at 2022-06-13 17:32:00.613761
# Unit test for function get_reserved_names
def test_get_reserved_names():
    expected_public = frozenset(['vars_files', u'environment', 'connection', 'gather_facts', 'name', 'hosts', 'remote_user', 'become',
                                 u'policies', 'become_user', 'vars_prompt', 'any_errors_fatal', 'any_unreachable_fatal', 'serial', 'local_action',
                                 'handlers', 'tags', 'roles', 'post_tasks', 'pre_tasks', 'blocks', 'tasks', 'meta', 'when', 'with_', 'notify',
                                 u'ignore_errors', 'register', 'connection', 'environment', 'become'])

# Generated at 2022-06-13 17:32:03.672005
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert 'action' in get_reserved_names()
    assert 'pre_tasks' in get_reserved_names()
    assert 'post_tasks' in get_reserved_names(include_private=False)



# Generated at 2022-06-13 17:32:09.553148
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # Test private names
    # FIXME: should this be a warning?
    for item in _RESERVED_NAMES:
        if '_' in item:
            assert not item in _RESERVED_NAMES

    public = get_reserved_names(include_private=False)
    private = get_reserved_names(include_private=True)
    assert public.issubset(private)
    assert private.issubset(_RESERVED_NAMES)



# Generated at 2022-06-13 17:32:15.186072
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' this function tests the get_reserved_names function'''

    # verify that we can get the reserved names both with and without private names
    public_only = get_reserved_names(include_private=False)
    with_private = get_reserved_names(include_private=True)

    # verify that public names is a subset of all names with private
    assert(public_only.issubset(with_private))

    # verify that there are no duplicates in all names
    assert(len(public_only) + len(with_private) == len(with_private.union(public_only)))



# Generated at 2022-06-13 17:32:25.321303
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:32:33.254913
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' Unit test for function get_reserved_names '''

    assert(isinstance(_RESERVED_NAMES, frozenset))

    # NOTE: uncomment below to verify that the function is still current and there are no duplicates etc.

    #reserved_names = get_reserved_names()
    #print sorted(list(reserved_names))
    #for x in reserved_names:
    #    assert(is_reserved_name(x))

# Generated at 2022-06-13 17:32:50.468399
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' test that the reserved name list is accurate and up to date '''

    # order is not important in this test
    result = get_reserved_names()
    expected_result = frozenset(['ignore_errors', 'pre_tasks', 'hosts', 'roles', 'tasks', 'vars', 'notify', 'post_tasks', 'handlers',
                                 'any_errors_fatal', 'remote_user', 'always_run', 'serial', 'block', 'block_errors', 'become',
                                 'become_user', 'connection', 'delegate_to', 'ignore_unreachable', 'meta', 'vars_prompt', 'vars_files',
                                 'vault_password_file', 'when', 'delay', 'changed_when', 'register', 'fail_when'])

   

# Generated at 2022-06-13 17:33:01.334646
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:33:11.161324
# Unit test for function get_reserved_names
def test_get_reserved_names():
    myvars = dict()
    myvars['name'] = 'test'
    myvars['hosts'] = 'localhost'
    myvars['action'] = 'ping'
    myvars['with_items'] = 'foo'
    myvars['register'] = 'bar'
    myvars['connection'] = 'smart'
    myvars['remote_user'] = 'jdoe'
    myvars['gather_facts'] = True
    myvars['sudo'] = True
    myvars['sudo_user'] = 'jdoe'
    myvars['sudo_pass'] = '12345'
    myvars['when'] = 'always'
    myvars['delegate_to'] = 'localhost'
    myvars['async'] = '1'

# Generated at 2022-06-13 17:33:14.410858
# Unit test for function get_reserved_names
def test_get_reserved_names():

    reserved = get_reserved_names()

    assert 'name' in reserved
    assert 'roles' in reserved
    assert 'include' in reserved

    assert 'vars' not in reserved
    assert 'tasks' not in reserved
    assert 'variables' not in reserved


# Generated at 2022-06-13 17:33:19.706412
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' function tests get_reserved_names() return values '''

    test = get_reserved_names()

    assert 'action' in test
    assert 'delegate_to' in test
    assert 'name' in test
    assert 'hosts' in test
    assert 'roles' in test
    assert 'tasks' in test
    assert 'block' in test
    assert 'meta' in test
    assert 'pre_tasks' in test
    assert 'post_tasks' in test
    assert 'vars_files' in test
    assert 'vars_prompt' in test
    assert 'vars' in test
    assert 'when' in test

    # loop implies with_
    # FIXME: remove after with_ is not only deprecated but removed
    assert 'with_' in test
    assert 'loop' in test

# Generated at 2022-06-13 17:33:26.567608
# Unit test for function get_reserved_names
def test_get_reserved_names():

    reserved_names = get_reserved_names()
    assert 'hosts' in reserved_names
    assert 'hosts' in reserved_names
    assert 'roles' in reserved_names
    assert 'tasks' in reserved_names
    assert 'environment' in reserved_names



# Generated at 2022-06-13 17:33:34.792453
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' Unit test for function get_reserved_names '''

    from ansible.playbook.test.test_attribute import TestAttribute
    test_obj = TestAttribute()

    # Fixed set of reserved variables
    reserved = get_reserved_names()

# Generated at 2022-06-13 17:33:36.502527
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' this function runs the reserved names unit tests '''
    assert 'hosts' in get_reserved_names()

# Generated at 2022-06-13 17:33:38.485914
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert isinstance(get_reserved_names(), set)
    assert isinstance(get_reserved_names(False), set)



# Generated at 2022-06-13 17:33:47.375071
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:34:03.403550
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:34:06.060111
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert 'name' in get_reserved_names()
    assert get_reserved_names(include_private=False) != get_reserved_names()

# Generated at 2022-06-13 17:34:16.333343
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # Test the public names
    play_obj = Play()
    public_names = get_reserved_names(include_private=False)
    for name in public_names:
        assert hasattr(play_obj, name) is not None

    # Test the private names
    play_obj = Play()
    private_names = get_reserved_names(include_private=True)
    for name in private_names:
        assert hasattr(play_obj, name) is not None

    # Test if 'vars' is in public or private names, and remove it from private names
    assert 'vars' not in public_names
    assert 'vars' in private_names
    private_names.remove('vars')

    # Test if the len of private names is higher than the len of public names

# Generated at 2022-06-13 17:34:17.384703
# Unit test for function get_reserved_names
def test_get_reserved_names():
   assert 'hosts' in get_reserved_names()
   assert isinstance(get_reserved_names(), set)

# Generated at 2022-06-13 17:34:20.022897
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # This test will fail if the inventory_hostname is a reserved name.
    # There is no way to savely test the function without executing it.
    assert 'inventory_hostname' not in get_reserved_names()



# Generated at 2022-06-13 17:34:22.397100
# Unit test for function get_reserved_names
def test_get_reserved_names():
    tmp = get_reserved_names()
    assert isinstance(tmp, set)
    assert 'role' in tmp
    assert 'action' in tmp
    assert 'roles' in tmp
    assert 'action' in tmp



# Generated at 2022-06-13 17:34:29.282986
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:34:30.314362
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert len(get_reserved_names()) > 0

# Generated at 2022-06-13 17:34:36.376098
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved = set(['action', 'block', 'block_tasks', 'connection'])

    public = get_reserved_names(include_private=False)
    private = get_reserved_names(include_private=True)

    assert public.difference(reserved) == set()
    assert reserved.difference(public) == set()
    assert not public.difference(private)
    assert not private.difference(public)
    assert private.difference(reserved) == set(['hosts', 'local_action', 'loop', 'with_'])
    assert reserved.difference(private) == set()

# Generated at 2022-06-13 17:34:46.550258
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved_names = get_reserved_names()

    assert 'vars' in reserved_names
    assert 'hosts' in reserved_names
    assert 'roles' in reserved_names
    assert 'name' in reserved_names
    assert 'import_role' in reserved_names
    assert 'import_tasks' in reserved_names
    assert 'import_playbook' in reserved_names

    assert 'action' in reserved_names
    assert 'local_action' in reserved_names

    assert 'loop' in reserved_names
    assert 'with_' in reserved_names

    assert 'include' in reserved_names
    assert 'tags' in reserved_names
    assert 'when' in reserved_names
    assert 'register' in reserved_names
    assert 'delegate_to' in reserved_names
    assert 'notify' in reserved_

# Generated at 2022-06-13 17:35:08.262023
# Unit test for function get_reserved_names
def test_get_reserved_names():
    class TestPlay:
        _role = None
        _dependencies = []

        name = None
        hosts = None
        connection = None
        gather_facts = None
        any_errors_fatal = None
        serial = None
        max_fail_percentage = None
        force_handlers = None
        sudo = None
        sudo_user = None
        remote_user = None
        become = None
        become_method = None
        become_user = None
        become_ask_pass = None
        module_defaults = None
        inventory = None
        strategy = None
        vars = []
        vars_files = []
        vars_prompt = []
        handler_tasks = []
        default_vars = None
        pre_tasks = None
        post_tasks = None
        roles = None


# Generated at 2022-06-13 17:35:16.950681
# Unit test for function get_reserved_names
def test_get_reserved_names():
    data = get_reserved_names()
    assert len(data) > 0
    assert 'name' in data
    assert 'roles' in data
    assert 'tasks' in data
    assert 'action' in data
    assert 'include' in data
    assert 'connection' in data
    assert 'sudo' in data
    assert 'sudo_user' in data
    assert 'sudo_pass' in data
    assert 'environment' in data
    assert 'delegate_to' in data
    assert 'run_once' in data
    assert 'register' in data
    assert 'ignore_errors' in data

    data = get_reserved_names(include_private=False)
    assert len(data) > 0
    assert 'when' not in data
    assert 'local_action' not in data

# Generated at 2022-06-13 17:35:23.367311
# Unit test for function get_reserved_names
def test_get_reserved_names():
    play_obj = Play()
    role_obj = Role()
    block_obj = Block()
    task_obj = Task()

    assert set(play_obj.__dict__['_attributes']) == get_reserved_names()
    assert set(role_obj.__dict__['_attributes']) == get_reserved_names()
    assert set(block_obj.__dict__['_attributes']) == get_reserved_names()
    assert set(task_obj.__dict__['_attributes']) == get_reserved_names()

# Generated at 2022-06-13 17:35:29.976800
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved = get_reserved_names()
    for name in ['name', 'hosts', 'any_errors_fatal']:
        assert name in reserved

    # assert local_action is in reserved names because action is and
    # local_action is marked as private, so we include it by default.
    assert 'local_action' in reserved

    # assert with_ is in reserved names because loop is and
    # with_ is marked as private, so we include it by default.
    # FIXME: remove after with_ is not only deprecated but removed
    assert 'with_' in reserved

    # assert local_action is in public names because action is
    # local_action is marked as private, so we exclude it by default.
    assert 'local_action' not in get_reserved_names(False)

    # assert with_ is in public names because loop

# Generated at 2022-06-13 17:35:35.704432
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert isinstance(get_reserved_names(), frozenset)
    assert len(get_reserved_names()) > 0
    assert isinstance(get_reserved_names(False), frozenset)
    assert len(get_reserved_names(False)) > 0
    assert get_reserved_names() == get_reserved_names(True)
    assert len(get_reserved_names()) > len(get_reserved_names(False))



# Generated at 2022-06-13 17:35:38.548171
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved_names = get_reserved_names(include_private=True)
    assert 'action' in reserved_names
    assert 'local_action' in reserved_names
    assert 'loop' in reserved_names
    assert 'with_' in reserved_names

# Generated at 2022-06-13 17:35:47.906981
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' test that names associated with play objects are all returned by get_reserved_names '''
    allvars = get_reserved_names()
    cls_vars = get_reserved_names(include_private=False)


# Generated at 2022-06-13 17:35:50.642170
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved = get_reserved_names()
    assert 'block' in reserved
    assert 'name' in reserved

    exclusions = frozenset(['hosts', 'roles'])
    assert not (reserved & exclusions)

# Generated at 2022-06-13 17:35:52.205637
# Unit test for function get_reserved_names
def test_get_reserved_names():
    print("\nreserved names: %s" % get_reserved_names())



# Generated at 2022-06-13 17:35:56.764512
# Unit test for function get_reserved_names
def test_get_reserved_names():
    wrong = False
    for aclass in [Play, Role, Block, Task]:
        aobj = aclass()
        for attribute in aobj.__dict__['_attributes']:
            if attribute not in _RESERVED_NAMES and 'private' not in attribute:
                wrong = True
                print(attribute + ' is not in reserved_names')
    assert wrong == False

# Generated at 2022-06-13 17:36:26.466757
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' this function tests the get_reserved_names function'''
    result = get_reserved_names()
    assert len(result) > 0
    result = get_reserved_names(include_private=False)
    assert len(result) > 0


# Generated at 2022-06-13 17:36:30.478124
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert get_reserved_names() == _RESERVED_NAMES
    assert get_reserved_names(include_private=False) == frozenset(get_reserved_names()) - frozenset(_RESERVED_NAMES)



# Generated at 2022-06-13 17:36:34.580063
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert len(_RESERVED_NAMES) != 0
    assert isinstance(_RESERVED_NAMES, frozenset)
    assert is_reserved_name('name') == True
    assert is_reserved_name('not_name') == False



# Generated at 2022-06-13 17:36:42.280575
# Unit test for function get_reserved_names
def test_get_reserved_names():
    rnames = get_reserved_names()
    assert 'name' in rnames
    assert 'task' in rnames
    assert 'debug' in rnames
    assert 'vars' in rnames
    assert 'private' in rnames
    assert 'pre_tasks' in rnames
    assert 'post_tasks' in rnames
    assert 'action' in rnames
    assert 'local_action' not in rnames
    assert 'loop' not in rnames
    assert 'with_' not in rnames



# Generated at 2022-06-13 17:36:45.216204
# Unit test for function get_reserved_names
def test_get_reserved_names():
    '''Test that get_reserved_names returns the right values'''

    # Not very well tested, but better than nothing
    result = get_reserved_names()
    assert 'hosts' in result
    assert 'action' in result
    assert 'local_action' in result
    assert 'with_' in result

    assert isinstance(result, set)

# Generated at 2022-06-13 17:36:56.348383
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:37:04.904777
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' Unit test for function get_reserved_names() '''

    reserved = get_reserved_names()

    # check that reserved names are assigned to the right class
    for name in reserved:
        if name in Play._attributes:
            continue
        elif name in Role._attributes:
            continue
        elif name in Block._attributes:
            continue
        elif name in Task._attributes:
            continue
        else:
            raise Exception("%s is not assigned to a class" % name)

    # check that no 'private' attribute is listed as reserved
    for name in reserved:
        if 'private' in name:
            raise Exception("%s should not be listed as reserved" % name)

    # check that all Play._attributes is reserved
    # FIXME: remove after with_ is not only deprecated but removed


# Generated at 2022-06-13 17:37:11.719432
# Unit test for function get_reserved_names
def test_get_reserved_names():
    result = get_reserved_names()

# Generated at 2022-06-13 17:37:21.561309
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:37:30.067252
# Unit test for function get_reserved_names
def test_get_reserved_names():

    # Empty set
    assert len(get_reserved_names(include_private=False)) == 0

    public = get_reserved_names(include_private=False)
    private = get_reserved_names(include_private=True)

    # Check public reserved names set
    assert 'action' in public
    assert 'block' in public
    assert 'connection' in public
    assert 'environment' in public
    assert 'gather_facts' in public
    assert 'handlers' in public
    assert 'hosts' in public
    assert 'roles' in public
    assert 'tags' in public
    assert 'tasks' in public
    assert 'vars' in public

    # Check private reserved names set
    assert 'any_errors_fatal' in private
    assert 'always_run' in private
    assert 'block'