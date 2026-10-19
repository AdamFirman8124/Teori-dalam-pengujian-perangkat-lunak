

# Generated at 2022-06-13 17:28:54.824043
# Unit test for function get_reserved_names
def test_get_reserved_names():
    '''
    test to ensure that reserved names are returned as expected
    '''

    # public only
    result = get_reserved_names(include_private=False)
    assert len(result) > 1
    assert 'name' in result
    assert 'include_role' in result
    assert 'action' in result
    assert 'local_action' in result
    for name in result:
        assert not name.startswith('_')

    # public and private
    result = get_reserved_names(include_private=True)
    assert len(result) > 1
    assert 'name' in result
    assert '_role_name' in result
    assert '_playbook_dir' in result
    assert 'action' in result
    assert 'local_action' in result

# Generated at 2022-06-13 17:29:05.234356
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert 'debug' in get_reserved_names()
    assert 'tags' in get_reserved_names()
    assert 'name' in get_reserved_names()
    assert 'with_' in get_reserved_names()
    assert 'local_action' in get_reserved_names()
    assert 'vars' in get_reserved_names()
    assert 'gather_facts' in get_reserved_names(include_private=False)
    assert 'action' not in get_reserved_names(include_private=False)
    assert '_role_name' in get_reserved_names()
    assert get_reserved_names() != get_reserved_names(include_private=False)


# Generated at 2022-06-13 17:29:09.486634
# Unit test for function get_reserved_names
def test_get_reserved_names():
    result = set(get_reserved_names())
    assert(len(result) == 83)
    assert('name' in result)
    assert('action' in result)
    assert('when' in result)
    assert('loop' in result)
    assert('_raw_params' in result)

# Generated at 2022-06-13 17:29:16.845254
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert isinstance(_RESERVED_NAMES, frozenset)
    assert _RESERVED_NAMES is not get_reserved_names()


# Generated at 2022-06-13 17:29:24.809305
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved_names = get_reserved_names(include_private=False)
    reserved_names_private = get_reserved_names(include_private=True)
    assert(len(reserved_names) < len(reserved_names_private))
    assert('action' in reserved_names)
    assert('tasks' in reserved_names)
    assert('post_tasks' in reserved_names)
    assert('handlers' in reserved_names)
    assert('hosts' in reserved_names)
    assert(len(reserved_names) > 10)
    assert('tags' in reserved_names)
    assert('delegate_to' in reserved_names)



# Generated at 2022-06-13 17:29:30.615116
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert 'hosts' in get_reserved_names()
    assert 'role_name' in get_reserved_names()
    assert 'name' in get_reserved_names(False)
    assert 'name' not in get_reserved_names(True)


# Unit tests for function warn_if_reserved


# Generated at 2022-06-13 17:29:38.927013
# Unit test for function get_reserved_names
def test_get_reserved_names():
    print(_RESERVED_NAMES)
    assert 'vars' in _RESERVED_NAMES
    assert 'name' in _RESERVED_NAMES
    assert 'action' in _RESERVED_NAMES
    assert 'loop' in _RESERVED_NAMES
    assert 'loop_control' in _RESERVED_NAMES
    assert 'private' not in _RESERVED_NAMES
    assert 'private_key_file' in _RESERVED_NAMES
    assert 'local_action' in _RESERVED_NAMES
    assert 'with_' in _RESERVED_NAMES
    assert 'with_fileglob' in _RESERVED_NAMES

# Generated at 2022-06-13 17:29:43.728155
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved_names = get_reserved_names()
    private_reserved_names = get_reserved_names(include_private=True)

    assert 'gather_facts' in reserved_names
    assert 'private' in private_reserved_names



# Generated at 2022-06-13 17:29:46.697330
# Unit test for function get_reserved_names
def test_get_reserved_names():
    result = get_reserved_names()
    assert set(['roles', 'tasks', 'handlers', 'pre_tasks', 'post_tasks', 'role_path']) <= result



# Generated at 2022-06-13 17:29:49.596405
# Unit test for function get_reserved_names
def test_get_reserved_names():
    p = Play()
    for prop in p.__dict__['_attributes']:
        if prop.get('name') == 'vars':
            continue
        assert prop.get('name') in get_reserved_names()



# Generated at 2022-06-13 17:30:15.414322
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert 'gather_facts' in get_reserved_names()
    assert 'roles' in get_reserved_names()

    assert 'when' in get_reserved_names()
    assert 'notify' in get_reserved_names()

    assert 'local_action' in get_reserved_names()
    assert 'action' in get_reserved_names()

    assert 'with_' in get_reserved_names()
    assert 'loop' in get_reserved_names()

    assert 'always_run' in get_reserved_names()
    assert 'first_available_file' in get_reserved_names()
    assert 'vars_prompt' in get_reserved_names()
    assert 'tags' in get_reserved_names()

    assert 'vars_files' in get_reserved

# Generated at 2022-06-13 17:30:17.378376
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert frozenset(get_reserved_names()) == _RESERVED_NAMES

# Generated at 2022-06-13 17:30:20.976616
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert set(['name', 'roles', 'tasks', 'hosts', 'action', 'block', 'local_action', 'with_', 'connection', 'vars', 'environment', 'register', 'ignore_errors', 'delegate_to']).issubset(get_reserved_names())


# Generated at 2022-06-13 17:30:25.516388
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # This is kind of a fragile test, but hard to do better, so it'll do.
    assert 'action' in get_reserved_names()
    assert 'applied_tasks' in get_reserved_names()
    assert 'hosts' in get_reserved_names()
    assert 'roles' in get_reserved_names(include_private=True)
    assert 'roles' not in get_reserved_names(include_private=False)

# Generated at 2022-06-13 17:30:28.683382
# Unit test for function get_reserved_names
def test_get_reserved_names():
    names = get_reserved_names()
    assert len(names) > 0
    assert 'name' in names
    assert 'local_action' in names



# Generated at 2022-06-13 17:30:40.150594
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # Simple test, just make sure that this function works as expected
    reserved_names = get_reserved_names(include_private=True)
    public_names = get_reserved_names(include_private=False)
    assert 'roles' in reserved_names and 'roles' in public_names
    assert 'block' in reserved_names and 'block' in public_names
    # 'tags' is a special case, it is a private attribute for Block but also
    # a public attribute for Role and Play
    assert 'tags' in reserved_names and 'tags' not in public_names
    assert 'become' in reserved_names and 'become' in public_names
    assert 'action' in reserved_names and 'action' in public_names
    assert 'local_action' in reserved_names and 'local_action' in public_names

# Generated at 2022-06-13 17:30:41.055691
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert get_reserved_names()



# Generated at 2022-06-13 17:30:49.638723
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' test get_reserved_names_n module '''

    # FIXME: find a way to 'not hardcode', possibly need role deps/includes
    public = ['name', 'gather_facts', 'delegate_to', 'remote_user', 'transport', 'tags', 'register',
              'vars', 'vars_files', 'notify', 'roles', 'include_vars', 'pre_tasks', 'post_tasks',
              'block', 'any_errors_fatal', 'action', 'local_action']

    public.sort()
    result = get_reserved_names(include_private=False)
    result = list(result)
    result.sort()
    assert result == public


# Generated at 2022-06-13 17:30:58.632520
# Unit test for function get_reserved_names
def test_get_reserved_names():
    for name in ('hosts', 'name', 'vars', 'vars_prompt', 'vars_files', 'gather_facts',
                 'roles', 'pre_tasks', 'post_tasks', 'tasks', 'when', 'tags', 'become',
                 'become_user', 'become_method', 'any_errors_fatal', 'remote_user',
                 'connection', 'sudo', 'sudo_user', 'transport', 'ignore_errors'):
        assert(name in _RESERVED_NAMES)

    for name in ('action', 'local_action', 'with_'):
        assert(name in _RESERVED_NAMES)


# Generated at 2022-06-13 17:31:04.571579
# Unit test for function get_reserved_names
def test_get_reserved_names():
    '''
    test_get_reserved_names
    :return:
    '''
    public_vars = [
        'name', 'hosts', 'roles', 'tasks', 'handlers', 'block', 'block',
        'pre_tasks', 'post_tasks', 'any_errors_fatal',
        'notify', 'listen', 'vars', 'vars_prompt', 'vars_files', 'tags',
        'gather_facts', 'serial', 'any_errors_fatal', 'remote_user',
        'connection', 'sudo', 'sudo_user', 'become', 'become_method',
        'become_user', 'environment', 'no_log',
        'no_target_syslog'
    ]


# Generated at 2022-06-13 17:31:24.358416
# Unit test for function get_reserved_names
def test_get_reserved_names():
    r_names = get_reserved_names(include_private=False)
    assert 'action' in r_names
    r_names = get_reserved_names(include_private=True)
    assert 'become_user' in r_names
    assert 'action' in r_names



# Generated at 2022-06-13 17:31:27.337578
# Unit test for function get_reserved_names
def test_get_reserved_names():

    reserved_names = get_reserved_names()

    assert type(reserved_names) is set
    assert 'name' in reserved_names
    assert 'action' in reserved_names
    assert 'local_action' in reserved_names
    assert 'with_' in reserved_names



# Generated at 2022-06-13 17:31:32.983577
# Unit test for function get_reserved_names
def test_get_reserved_names():
    public = get_reserved_names(include_private=False)
    private = get_reserved_names(include_private=True)

    assert public.issubset(private)
    assert 'hosts' in public
    assert 'hosts' in private

    assert 'roles' in public
    assert 'roles' in private

    assert 'private' in private
    assert 'private' not in public



# Generated at 2022-06-13 17:31:33.793049
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert isinstance(get_reserved_names(), set)

# Generated at 2022-06-13 17:31:36.737847
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert len(get_reserved_names(False)) > 5
    assert len(get_reserved_names()) > len(get_reserved_names(False))



# Generated at 2022-06-13 17:31:37.844440
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert 'vars' in get_reserved_names()
    assert 'include' in get_reserved_names()
    assert 'include_tasks' in get_reserved_names()

# Generated at 2022-06-13 17:31:48.711108
# Unit test for function get_reserved_names
def test_get_reserved_names():

    # We expect these to be the same.  If they are not, then we have
    # added or removed a reserved name and need to update the assert
    assert sorted(_RESERVED_NAMES) == sorted(get_reserved_names())


# Generated at 2022-06-13 17:32:00.351994
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # check the function returns something
    assert get_reserved_names()
    assert isinstance(get_reserved_names(), set)

    # check we can get both public and private
    assert len(get_reserved_names(include_private=False)) < len(get_reserved_names(include_private=True))

    # check we get a sane list of names
    assert 'name' in get_reserved_names()
    assert 'roles' in get_reserved_names()
    assert 'hosts' in get_reserved_names()
    assert 'private_key_file' in get_reserved_names(include_private=True)
    assert 'private_key_file' not in get_reserved_names(include_private=False)
    assert 'action' in get_reserved_names()

# Generated at 2022-06-13 17:32:07.728342
# Unit test for function get_reserved_names
def test_get_reserved_names():
    '''
    unit test for get_reserved_names()
    '''
    # create list of reserved names and make all lower case
    reserved_name_list = list(get_reserved_names())
    reserved_name_lower = [x.lower() for x in reserved_name_list]

    # test reserved names are all lowercase
    assert not [name for name in reserved_name_list if name not in reserved_name_lower]

    # test get_reserved_names returns once instance of each name
    assert len(reserved_name_list) == len(reserved_name_lower)

    # test get_reserved_names with exclude_private False
    private_names = get_reserved_names(include_private=False)
    # test all private_names are in reserved_name_list

# Generated at 2022-06-13 17:32:19.018784
# Unit test for function get_reserved_names
def test_get_reserved_names():

    reserved = get_reserved_names()


# Generated at 2022-06-13 17:32:58.254850
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # test for reserved names, including private
    assert isinstance(get_reserved_names(), set)
    assert 'vars' in get_reserved_names()

    # test for reserved names, not including private
    assert 'post_tasks' not in get_reserved_names()
    assert 'pre_tasks' not in get_reserved_names()
    assert 'block' not in get_reserved_names()
    assert 'delegate_to' not in get_reserved_names()


# Generated at 2022-06-13 17:33:03.038242
# Unit test for function get_reserved_names
def test_get_reserved_names():
    public = set(['name', 'hosts', 'roles', 'block', 'pre_tasks', 'post_tasks', 'tasks', 'handlers', 'any_errors_fatal',
                  'max_fail_percentage', 'sudo', 'sudo_user', 'gather_facts', 'tags', 'tasks', 'vars', 'vars_prompt',
                  'vars_files', 'local_action', 'with_', 'local_action', 'connection', 'run_once', 'any_errors_fatal',
                  'always_run', 'delegate_to', 'delegate_facts', 'action', 'register'])

    private = set(['_block', '_play', '_task', '_role'])
    result = get_reserved_names(include_private=False)
    assert result == public

# Generated at 2022-06-13 17:33:07.330434
# Unit test for function get_reserved_names
def test_get_reserved_names():

    reserved = get_reserved_names()
    assert reserved

    public = get_reserved_names(include_private=False)
    assert public

    assert reserved != public
    assert public.issubset(reserved)

    # make sure it does not change over time
    global _RESERVED_NAMES
    assert _RESERVED_NAMES == reserved

# Generated at 2022-06-13 17:33:11.094552
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved_names = get_reserved_names()
    assert 'hosts' in reserved_names
    assert 'with_' in reserved_names
    assert 'private' not in reserved_names
    assert 'gather_facts' in reserved_names

# Generated at 2022-06-13 17:33:19.056256
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:33:27.374513
# Unit test for function get_reserved_names
def test_get_reserved_names():
    good_names = ['action', 'name', 'vars', 'local_action']
    bad_names = ['meta', 'private']

    reserved_names = get_reserved_names(include_private=True)

    assert len(good_names) + len(bad_names) == len(reserved_names)

    for name in good_names:
        assert name in reserved_names

    for name in bad_names:
        assert name not in reserved_names

# Generated at 2022-06-13 17:33:35.294651
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:33:40.970843
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' unit test for function get_reserved_names '''

    assert 'pre_tasks' in _RESERVED_NAMES
    assert 'notify' in _RESERVED_NAMES
    assert 'handlers' in _RESERVED_NAMES
    assert 'loop' in _RESERVED_NAMES
    assert 'with_' in _RESERVED_NAMES



# Generated at 2022-06-13 17:33:45.125134
# Unit test for function get_reserved_names
def test_get_reserved_names():
    '''
    >>> test_vars = get_reserved_names()
    >>> assert test_vars
    >>> assert 'hosts' in test_vars
    >>> assert 'become' in test_vars
    >>> assert 'become_user' in test_vars
    >>> assert 'private' not in test_vars
    '''

# Generated at 2022-06-13 17:33:47.783897
# Unit test for function get_reserved_names
def test_get_reserved_names():
    public = get_reserved_names(False)
    private = get_reserved_names(True)
    assert isinstance(public, set)
    assert isinstance(private, set)
    assert len(public) > 0
    assert len(private) > 0



# Generated at 2022-06-13 17:34:55.826427
# Unit test for function get_reserved_names
def test_get_reserved_names():
    public = get_reserved_names(include_private=False)
    private = get_reserved_names(include_private=True)

    # ensure that they are not the same
    assert public != private

    # make sure some private things are actually in both
    assert 'role_name' in public
    assert 'role_name' in private

    # make sure some public things are only in the public
    assert 'become' in public
    assert 'become' not in private

    # make sure some things are only in private
    assert 'private' in private
    assert 'private' not in public

# Generated at 2022-06-13 17:35:05.802457
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:35:14.972997
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' these are the reserved names that should be returned by get_reserved_names '''

# Generated at 2022-06-13 17:35:24.381652
# Unit test for function get_reserved_names
def test_get_reserved_names():
    from ansible.playbook.play_context import PlayContext
    assert get_reserved_names().__contains__('type')
    assert get_reserved_names().__contains__('action')
    assert get_reserved_names().__contains__('become_method')
    assert get_reserved_names().__contains__('tags')
    assert get_reserved_names().__contains__('when')
    assert get_reserved_names().__contains__('become_user')
    assert get_reserved_names().__contains__('hosts')
    assert get_reserved_names().__contains__('name')
    assert get_reserved_names().__contains__('roles')
    assert get_reserved_names().__contains__('connection')
    assert get_reserved

# Generated at 2022-06-13 17:35:31.604439
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved = get_reserved_names(False)
    assert 'gather_facts' in reserved
    assert 'environment' in reserved
    assert 'hosts' in reserved
    assert 'roles' in reserved
    assert 'name' in reserved

    reserved = get_reserved_names(True)
    assert 'roles' in reserved
    assert 'vars_files' in reserved
    assert 'delegate_to' in reserved

# Generated at 2022-06-13 17:35:35.247013
# Unit test for function get_reserved_names
def test_get_reserved_names():
    names = get_reserved_names()
    assert 'pre_tasks' in names
    assert '_role_name' in names
    assert 'any_errors_fatal' in names
    assert not is_reserved_name('iamnotreserved')


# Generated at 2022-06-13 17:35:44.922665
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' this function unit tests the function get_reserved_names'''

# Generated at 2022-06-13 17:35:51.957659
# Unit test for function get_reserved_names
def test_get_reserved_names():

    # test for presence of all reserved names for class play
    # and all attributes with private set to True
    play_obj = Play()
    play_obj_names = play_obj.__dict__['_attributes']

    reserved_names = get_reserved_names()

    # make sure all reserved names are in Play class
    assert play_obj_names.issubset(set(reserved_names))

    # test for no presence of all attributes non private
    # in reserved names
    play_obj_names_no_private = [attr for attr in play_obj_names if 'private' not in attr]
    assert not set(play_obj_names_no_private).difference(set(reserved_names))

    # test for the presence of all attributes with 'private' set to True
    # in reserved names
    play_

# Generated at 2022-06-13 17:35:57.701537
# Unit test for function get_reserved_names
def test_get_reserved_names():
    def assert_contains(a, b):
        assert a in b, '%s not in %s' % (a, b)

    # assert private reserved names
    private = get_reserved_names(include_private=True)
    assert_contains('tags', private)
    assert_contains('roles', private)

    # assert public reserved names
    public = get_reserved_names(include_private=False)
    assert_contains('action', public)
    assert_contains('handlers', public)

# Generated at 2022-06-13 17:36:01.430397
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # make sure local action is reported as reserved
    assert 'local_action' in get_reserved_names()

    # make sure loop implies with_ is reserved
    assert 'with_' in get_reserved_names()

    # make sure loop is not exposed in public
    assert 'loop' in get_reserved_names(include_private=False)

    # make sure local_action is exposed as public
    assert 'local_action' in get_reserved_names(include_private=False)

    # make sure loop is exposed in private
    assert 'loop' in get_reserved_names(include_private=True)

# Generated at 2022-06-13 17:38:22.723978
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:38:32.481101
# Unit test for function get_reserved_names
def test_get_reserved_names():
    result = [
        'any_errors_fatal',
        'become',
        'become_method',
        'become_user',
        'connection',
        'delegate_to',
        'hosts',
        'import_role',
        'import_tasks',
        'include',
        'include_role',
        'include_tasks',
        'local_action',
        'meta',
        'name',
        'notify',
        'pre_tasks',
        'post_tasks',
        'roles',
        'serial',
        'tasks',
        'when',
        'vars'
    ]

    assert set(result) == get_reserved_names()