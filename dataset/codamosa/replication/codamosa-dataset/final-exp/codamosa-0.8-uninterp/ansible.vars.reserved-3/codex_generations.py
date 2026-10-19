

# Generated at 2022-06-13 17:28:50.736784
# Unit test for function get_reserved_names
def test_get_reserved_names():

    expected = {
        'hosts', 'roles', 'tasks', 'vars', 'handlers',
        'action', 'local_action', 'with_',
        'name', 'block', 'block_var', 'include', 'include_role', 'include_tasks', 'meta',
        'pre_tasks', 'post_tasks',
        'any_errors_fatal', 'changed_when', 'delegate_to', 'failed_when', 'ignore_errors',
        'notify', 'register', 'retries', 'until', 'tags', 'when', 'async', 'poll', 'sudo', 'su',
        'sudo_user', 'connection', 'environment', 'no_log'
    }
    # test get_reserved_names
    assert expected == get_reserved_names(include_private=False)

# Generated at 2022-06-13 17:28:59.742525
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # test public only
    public = set(['name', 'hosts', 'remote_user', 'connection', 'sudo', 'sudo_user', 'environment', 'tags', 'any_errors_fatal',
                  'become', 'become_method', 'become_user', 'check_mode', 'gather_facts', 'serial', 'vars', 'vars_files', 'roles', 'tasks'])

    assert get_reserved_names(include_private=False) == public

    # test private only

# Generated at 2022-06-13 17:29:07.272542
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved = get_reserved_names()
    assert len(reserved) > 12
    assert 'name' in reserved
    assert 'any_errors_fatal' in reserved
    assert 'ignore_errors' in reserved
    assert 'action' in reserved
    assert 'local_action' in reserved
    assert 'loop' not in reserved
    assert 'with_' not in reserved

    reserved = get_reserved_names(False)
    assert len(reserved) > 12
    assert 'name' in reserved
    assert 'any_errors_fatal' in reserved
    assert 'ignore_errors' in reserved
    assert 'action' in reserved
    assert 'local_action' in reserved
    assert 'loop' not in reserved
    assert 'with_' not in reserved

    reserved = get_reserved_names(True)

# Generated at 2022-06-13 17:29:15.595492
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert get_reserved_names() == frozenset([
        'connection',
        'delegate_to',
        'gather_facts',
        'hosts',
        'ignore_errors',
        'local_action',
        'loop',
        'name',
        'register',
        'run_once',
        'serial',
        'sudo',
        'sudo_user',
        'tags',
        'transport',
        'with_',
    ])


# Generated at 2022-06-13 17:29:19.305420
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert 'name' in get_reserved_names(include_private=False)
    assert len(get_reserved_names(include_private=False)) == len(get_reserved_names()) - 2



# Generated at 2022-06-13 17:29:27.665735
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # this is a simple test to ensure the list of reserved names doesn't change
    # without us knowing about it.
    # If this test fails, check if there's a new name in play.yml, and
    # update the list in get_reserved_names.
    reserved_names = get_reserved_names()

# Generated at 2022-06-13 17:29:37.668354
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' test if get_reserved_names() returns expected results '''


# Generated at 2022-06-13 17:29:48.992775
# Unit test for function get_reserved_names
def test_get_reserved_names():
    public = set(['name', 'hosts', 'user', 'remote_user', 'connection', 'sudo', 'sudo_user',
                  'become', 'become_method', 'become_user', 'tags', 'tasks', 'environment', 'delegate_to'])


# Generated at 2022-06-13 17:29:54.067657
# Unit test for function get_reserved_names
def test_get_reserved_names():
    #  _RESERVED_NAMES is frozen set of strings.
    assert isinstance(_RESERVED_NAMES, frozenset)
    assert isinstance(_RESERVED_NAMES.pop(), str)
    assert len(_RESERVED_NAMES) > 100

# Generated at 2022-06-13 17:30:01.686117
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:30:19.218999
# Unit test for function get_reserved_names
def test_get_reserved_names():
    for reserved_name in ['action', 'hosts', 'roles', 'tags', 'tasks', 'local_action', 'delegate_to']:
        assert reserved_name in get_reserved_names()

    for reserved_name in ['ignore_errors', 'block', 'blockinfile', 'become', 'become_user', 'include', 'include_vars', 'loop', 'when']:
        assert reserved_name in get_reserved_names(include_private=True)

    for reserved_name in ['action', 'hosts', 'roles', 'tags', 'tasks', 'local_action', 'delegate_to', 'ignore_errors', 'block', 'blockinfile', 'become', 'become_user', 'include', 'include_vars', 'loop', 'when']:
        assert reserved_name in get

# Generated at 2022-06-13 17:30:21.091889
# Unit test for function get_reserved_names
def test_get_reserved_names():
    for name in _RESERVED_NAMES:
        assert isinstance(name, (str, unicode)), "expected string or unicode"

# Generated at 2022-06-13 17:30:23.685350
# Unit test for function get_reserved_names
def test_get_reserved_names():
    result = get_reserved_names()
    assert result == _RESERVED_NAMES

# Generated at 2022-06-13 17:30:28.339103
# Unit test for function get_reserved_names
def test_get_reserved_names():
    public = set(['name', 'hosts', 'gather_facts', 'any_errors_fatal', 'serial',
                  'max_fail_percentage', 'vars', 'vars_files', 'tags', 'remote_user',
                  'remote_port', 'transport', 'sudo', 'sudo_user', 'sudo_pass', 'become',
                  'become_method', 'become_user', 'become_pass', 'become_exe', 'when',
                  'environment', 'register', 'ignore_errors', 'local_action', 'connection',
                  'run_once', 'delegate_to', 'notify', 'block', 'role_names'])
    private = set(['action', 'loop', 'loop_control', 'with_'])
    assert get_reserved_names(include_private=True)

# Generated at 2022-06-13 17:30:32.757984
# Unit test for function get_reserved_names
def test_get_reserved_names():
    public = get_reserved_names(include_private=False)
    private = get_reserved_names()

    assert 'roles' in public
    assert 'tasks' in public
    assert 'include_role' in public
    assert 'import_role' in private
    assert 'post_tasks' in private

# Generated at 2022-06-13 17:30:43.218416
# Unit test for function get_reserved_names
def test_get_reserved_names():
    expected = frozenset(['action', 'async', 'async_status_timeout', 'become', 'become_flags', 'become_method', 'become_user', 'block', 'delegate_to', 'delegate_facts', 'environment', 'first_available_file', 'hosts', 'ignore_errors', 'include', 'include_tasks', 'include_vars', 'local_action', 'loop', 'meta', 'name', 'notified_by', 'notify', 'register', 'roles', 'run_once', 'sudo', 'sudo_flags', 'sudo_pass', 'sudo_user', 'tags', 'task', 'tasks', 'when', 'with_'])

    assert get_reserved_names() == expected

# Generated at 2022-06-13 17:30:47.250466
# Unit test for function get_reserved_names
def test_get_reserved_names():

    public = get_reserved_names(include_private=False)
    assert 'user' in public
    assert 'loop' not in public

    private = get_reserved_names(include_private=True)
    assert 'user' in private
    assert 'loop' in private

# Generated at 2022-06-13 17:30:53.689820
# Unit test for function get_reserved_names
def test_get_reserved_names():
    public, private = get_reserved_names(include_private=False), get_reserved_names(include_private=True)

    assert type(public) == type(private) == set

    assert 'pre_tasks' in public
    assert 'post_tasks' in public
    assert 'vars' in public
    assert 'roles' in public

    assert 'tags' in private
    assert 'name' in private
    assert 'block' in private



# Generated at 2022-06-13 17:30:57.588658
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' test_get_reserved_names '''
    reserved_names = get_reserved_names()
    assert type(reserved_names) is set
    assert 'hosts' in reserved_names
    assert 'become' in reserved_names
    assert 'loop' not in reserved_names
    assert 'action' in reserved_names


# Generated at 2022-06-13 17:31:00.590134
# Unit test for function get_reserved_names
def test_get_reserved_names():

    assert 'local_action' in get_reserved_names()
    assert 'local_action' not in get_reserved_names(include_private=False)

    assert 'with_' in get_reserved_names()
    assert 'with_' not in get_reserved_names(include_private=False)

# Generated at 2022-06-13 17:31:14.233852
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved = get_reserved_names(False)
    # list of vars which are not in all considered classes
    var_list = ['connection', 'remote_user', 'sudo', 'sudo_user', 'serial', 'gather_facts', 'delegate_to',
                'any_errors_fatal', 'run_once', 'gather_facts', 'environment', 'no_log', 'register', 'ignore_errors']
    for var in var_list:
        assert var not in reserved

# Generated at 2022-06-13 17:31:23.437283
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert not _RESERVED_NAMES.difference(
        {'action', 'any_errors_fatal', 'async', 'async_timeout', 'changed_when',
         'connection', 'delegate_to', 'environment', 'first_available_file', 'ignore_errors',
         'local_action', 'loop', 'notify', 'register', 'remote_user', 'roles', 'serial',
         'sudo_user', 'sudo_pass', 'sudo', 'su', 'su_user', 'su_pass', 'tags', 'transport',
         'vars', 'when', 'with_', 'with_items'})

# Generated at 2022-06-13 17:31:31.745044
# Unit test for function get_reserved_names
def test_get_reserved_names():

    reserved = set(get_reserved_names())

    # Compare the set of names with hardcoded valid names

# Generated at 2022-06-13 17:31:32.725187
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert type(get_reserved_names()) is frozenset

# Generated at 2022-06-13 17:31:39.726598
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # note that we have to do some property sets here to make sure the comparison
    # is fair and that we don't assume the get_reserved_names() function returns
    # a list which is in any particular order

    # test basic functionality with Role since that's a class which sets up a lot of properties
    role_obj = Role()
    role_dict = role_obj.__dict__['_attributes']
    role_private_objs = [x for x in role_dict.items() if 'private' in x[0]]
    role_public_objs = [x for x in role_dict.items() if 'private' not in x[0]]
    obj_names = [x[0] for x in role_private_objs + role_public_objs]

    reserved = get_reserved_names(include_private=False)

# Generated at 2022-06-13 17:31:40.905966
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved = get_reserved_names()
    assert 'hosts' in reserved

# Generated at 2022-06-13 17:31:45.921371
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert len(get_reserved_names()) > 70

    public = get_reserved_names(include_private=False)
    assert 'any_errors_fatal' in public
    assert 'private' not in public
    assert 'vars_files' in public

# Generated at 2022-06-13 17:31:48.384083
# Unit test for function get_reserved_names
def test_get_reserved_names():
    public = get_reserved_names(False)
    private = get_reserved_names()
    difference = private.difference(public)
    assert difference == {'with_', 'local_action'}

# Generated at 2022-06-13 17:31:52.530144
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved_names = get_reserved_names(include_private=True)
    assert isinstance(reserved_names, frozenset)

    # make sure we have some
    assert len(reserved_names) > 20

    # make sure we have some that are in v2 and some deprecated
    assert 'name' in reserved_names
    assert 'ignored_tags' in reserved_names



# Generated at 2022-06-13 17:32:01.925483
# Unit test for function get_reserved_names
def test_get_reserved_names():
    r = get_reserved_names()

# Generated at 2022-06-13 17:32:23.974255
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' test for get_reserved_names() '''

    assert 'role' in get_reserved_names()
    assert 'var' in get_reserved_names()
    assert 'action' in get_reserved_names()
    assert 'local_action' in get_reserved_names()
    assert 'with_' in get_reserved_names()
    assert 'loop' in get_reserved_names()
    assert 'tags' in get_reserved_names()
    assert 'connection' in get_reserved_names()

# Generated at 2022-06-13 17:32:25.902400
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert len(get_reserved_names()) > 2

if __name__ == '__main__':
    # Test get_reserved_names()
    test_get_reserved_names()

# Generated at 2022-06-13 17:32:36.673314
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert isinstance(_RESERVED_NAMES, frozenset), "get_reserved_names must return a frozenset"
    assert len(_RESERVED_NAMES) >= 39, "The list of reserved names must contain at least 39 words"
    assert isinstance(_RESERVED_NAMES.pop(), str), "The list of reserved names must contain strings"
    assert 'vars'  in _RESERVED_NAMES, "The list of reserved names must include variable 'vars'"
    assert 'private' not in _RESERVED_NAMES, "The list of reserved names must not include variable 'private'"
    assert 'private' in get_reserved_names(True), "The list including private must include variable 'private'"

# Generated at 2022-06-13 17:32:47.457090
# Unit test for function get_reserved_names
def test_get_reserved_names():
    private = get_reserved_names()
    public = get_reserved_names(include_private=False)
    assert(private != public)

    # Private should not be empty
    assert(private)

    # Private should be superset of public
    assert(public < private)

    # Private should not contain action
    assert('action' not in private)

    # Public should contain action
    assert('action' in public)

    # Private should contain local_action
    assert('local_action' in private)

    # Public should not contain local_action
    assert('local_action' not in public)

    # Private should not contain with_
    assert('with_' not in private)

    # Private should contain with_
    assert('with_' in public)

    # Private should not contain loop
    assert('loop' not in private)

# Generated at 2022-06-13 17:32:52.044226
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved_names_public  = get_reserved_names(include_private=False)
    reserved_names_private = get_reserved_names(include_private=True)
    assert(set(reserved_names_public).issubset(set(reserved_names_private)))
    assert(len(reserved_names_private) > len(reserved_names_public))


# Generated at 2022-06-13 17:32:59.670038
# Unit test for function get_reserved_names
def test_get_reserved_names():
    public = get_reserved_names(include_private=False)
    private = get_reserved_names(include_private=True)

    assert len(private) > len(public)
    assert 'vars' in public
    assert 'vars' not in private
    assert 'action' in public
    assert 'action' in private
    assert 'local_action' in private and 'local_action' not in public
    assert 'with_' in private and 'with_' not in public
    assert 'loop' not in private and 'loop' not in public

# Generated at 2022-06-13 17:33:09.893022
# Unit test for function get_reserved_names
def test_get_reserved_names():
    def assert_reserved_names(public, private, include_private):
        result = get_reserved_names(include_private=include_private)
        assert result == (private.union(public) if include_private else public)


# Generated at 2022-06-13 17:33:18.201433
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert set(['roles', 'gather_facts', 'hosts', 'name', 'vars',
                'vars_files', 'roles_path', 'hosts', 'action', 'local_action',
                'with_', 'when', 'environment', 'delegate_to',
                'serial', 'run_once']) == get_reserved_names(False)
    assert set(['roles', 'private', 'gather_facts', 'hosts', 'name', 'vars',
                'vars_files', 'roles_path', 'hosts', 'action', 'local_action',
                'loop', 'with_', 'when', 'environment', 'delegate_to',
                'serial', 'run_once']) == get_reserved_names(True)


# Generated at 2022-06-13 17:33:30.451461
# Unit test for function get_reserved_names
def test_get_reserved_names():
    hostname = 'localhost'
    task = {'include': 'test',
            'name': 'test',
            'register': 'test',
            'args': {},
            'environment': {},
            'with_items': [],
            'with_file': [],
            'when': []}

    print('Play Reserved Names:')
    print('-' * 20)
    for key in Play().__dict__['_attributes']:
        if 'private' in key:
            print('  %s: PRIVATE' % key)
        else:
            print('  %s' % key)
    print('')

    print('Role Reserved Names:')
    print('-' * 20)

# Generated at 2022-06-13 17:33:39.303067
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' unit test for function get_reserved_names '''


# Generated at 2022-06-13 17:33:56.337551
# Unit test for function get_reserved_names
def test_get_reserved_names():
    names = get_reserved_names(include_private=False)
    assert 'become' in names
    assert 'become_user' in names

# Generated at 2022-06-13 17:34:05.082117
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # legacy-playbook-roles-inclusion variable is deprecated
    assert 'legacy_playbook_roles_inclusion' in get_reserved_names()
    assert 'gather_facts' in get_reserved_names()
    assert 'gather_subset' in get_reserved_names()
    # gather_timeout is deprecated
    assert 'gather_timeout' in get_reserved_names()
    assert 'tags' in get_reserved_names()
    assert 'name' in get_reserved_names()
    assert 'author' in get_reserved_names()
    assert 'description' in get_reserved_names()
    assert 'vars' in get_reserved_names()
    assert 'default_vars' in get_reserved_names()
    assert 'vars_files' in get_

# Generated at 2022-06-13 17:34:13.859083
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert 'action' in _RESERVED_NAMES
    assert 'local_action' in _RESERVED_NAMES
    assert 'name' in _RESERVED_NAMES
    assert 'gather_facts' in _RESERVED_NAMES
    assert 'include_' in _RESERVED_NAMES
    assert 'with_' in _RESERVED_NAMES

    # These should not be in _RESERVED_NAMES
    assert 'ignore_errors' not in _RESERVED_NAMES
    assert 'pre_tasks' not in _RESERVED_NAMES
    assert 'post_tasks' not in _RESERVED_NAMES

# Generated at 2022-06-13 17:34:22.302886
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert get_reserved_names() == get_reserved_names(True)
    assert get_reserved_names(include_private=False) == set(
        ['name', 'user', 'sudo', 'sudo_user', 'connection', 'any_errors_fatal', 'serial', 'gather_facts', 'hosts', 'force_handlers', 'roles',
         'tasks', 'handlers', 'vars', 'vars_files', 'pre_tasks', 'post_tasks', 'tags', 'block', 'block_errors', 'when', 'local_action', 'with_'])

# Generated at 2022-06-13 17:34:28.091418
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:34:33.210820
# Unit test for function get_reserved_names
def test_get_reserved_names():
    public_names = set()
    public_names.add('hosts')
    public_names.add('gather_facts')
    public_names.add('roles')
    public_names.add('tasks')
    public_names.add('vars')
    public_names.add('action')
    public_names.add('local_action')

    assert _RESERVED_NAMES == public_names

# Generated at 2022-06-13 17:34:44.581071
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:34:48.406237
# Unit test for function get_reserved_names
def test_get_reserved_names():
    result = get_reserved_names()
    assert len(result) > 0
    assert 'name' in result
    assert 'private' not in result
    assert 'no_log' not in result

# Generated at 2022-06-13 17:34:58.016920
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved_names = frozenset(get_reserved_names(include_private=False))
    for name in ['name', 'hosts', 'remote_user', 'tasks', 'roles', 'block',
                 'action', 'local_action', 'vars', 'any_errors_fatal', 'failed_when', 'failed_results_json',
                 'failed_when_result', 'include', 'pre_tasks', 'post_tasks', 'vars_prompt', 'vars_files',
                 'no_log', 'ignore_errors', 'loop', 'with_', 'tags', 'when', 'gather_facts', 'delegate_to',
                 'run_once', 'register']:
        assert name in reserved_names

# Generated at 2022-06-13 17:35:07.298053
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' we want to make sure get_reserved_names returns the expected names '''
    expected_names = set([u'roles', u'tasks', u'action', u'post_tasks', u'handlers', u'name', u'block', u'include', u'vars', u'any_errors_fatal', u'depth', u'block', u'become', u'become_user', u'become_method', u'async', u'hosts', u'connection', u'ignore_errors', u'gather_facts', u'transport', u'serial', u'environment', u'no_log', u'poll', u'local_action', u'loop', u'tags'])

    # use set comparison to test

# Generated at 2022-06-13 17:35:47.366320
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' functions get_reserved_names and warn_if_reserved '''
    # We want to ensure that all reserved names are in the set
    reserved = get_reserved_names()
    # Values in varnames will be missing from the list of reserved names
    varnames = ['connection',
                'gather_facts',
                'hosts',
                'name',
                'notify',
                'roles',
                'slurp',
                'sudo',
                'sudo_user']

    for name in varnames:
        if name in reserved:
            continue
        raise Exception("name %s not in reserved names" % name)

    # We expect the warning for reserved name
    varnames.append('action')
    warn_if_reserved(varnames)

# Generated at 2022-06-13 17:35:52.111000
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert 'name' in get_reserved_names()
    assert 'hosts' in get_reserved_names()
    assert 'roles' in get_reserved_names()
    assert 'loop' in get_reserved_names(include_private=False)
    assert 'with_' not in get_reserved_names(include_private=False)
    assert 'with_' in get_reserved_names(include_private=True)

# Generated at 2022-06-13 17:35:58.018356
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:36:04.849224
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:36:16.336250
# Unit test for function get_reserved_names
def test_get_reserved_names():

    private = set([
        'become', 'become_method', 'become_user',
        'changed_when', 'check_mode', 'connection',
        'gather_facts', 'ignore_errors', 'loop',
        'name', 'no_log', 'notify', 'poll',
        'register', 'retries', 'run_once',
        'sudo', 'sudo_user', 'tags',
        'when', 'with_',
    ])


# Generated at 2022-06-13 17:36:23.781197
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert 'hosts' in get_reserved_names()
    assert 'action' in get_reserved_names()
    assert 'name' in get_reserved_names()

    assert 'become' in get_reserved_names()
    assert 'become_user' in get_reserved_names()
    assert 'delegate_to' in get_reserved_names()
    assert 'gather_facts' in get_reserved_names()
    assert 'ignore_errors' in get_reserved_names()
    assert 'no_log' in get_reserved_names()

    assert 'include' not in get_reserved_names(False)
    assert 'include' in get_reserved_names(True)

# Generated at 2022-06-13 17:36:26.782620
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert get_reserved_names(include_private=True) == get_reserved_names(include_private=False).union(('when',))


if __name__ == '__main__':
    test_get_reserved_names()

# Generated at 2022-06-13 17:36:31.810838
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # we should get a set
    assert isinstance(get_reserved_names(), set)

    # each item should be a string
    for item in get_reserved_names():
        assert isinstance(item, str)

    # we should not get a None type variable
    assert get_reserved_names() is not None



# Generated at 2022-06-13 17:36:36.321465
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert isinstance(get_reserved_names(), set)
    assert isinstance(get_reserved_names(include_private=False), set)

# Generated at 2022-06-13 17:36:44.911785
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:37:59.633202
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # Note: the following tests assume that get_reserved_names() is called once
    # to build _RESERVED_NAMES, otherwise the test will fail

    # Test reserved names with private attributes excluded
    reserved = get_reserved_names(include_private=False)
    assert len(reserved) == 24
    assert 'name' in reserved
    assert 'sudo_user' in reserved
    assert 'sudo' in reserved
    assert 'sudo_password' not in reserved
    assert 'local_action' not in reserved

    # Test reserved names with private attributes included
    reserved = get_reserved_names(include_private=True)
    assert len(reserved) == 43
    assert 'name' in reserved
    assert 'sudo_user' in reserved
    assert 'sudo' in reserved
    assert 'sudo_password' in reserved

# Generated at 2022-06-13 17:38:03.342148
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert 'hosts' in get_reserved_names()
    assert 'name' in get_reserved_names()
    assert 'local_action' in get_reserved_names()
    assert 'action' in get_reserved_names()
    assert 'notify' in get_reserved_names()
    assert 'vars' in get_reserved_names()
    assert 'loop' not in get_reserved_names()



# Generated at 2022-06-13 17:38:09.376511
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert 'roles' in get_reserved_names(include_private=False)
    assert 'roles' in get_reserved_names(include_private=True)
    assert 'tasks' in get_reserved_names(include_private=False)
    assert 'tasks' in get_reserved_names(include_private=True)
    assert 'vars' in get_reserved_names(include_private=False)
    assert 'vars' in get_reserved_names(include_private=True)

    assert 'connection' in get_reserved_names(include_private=False)
    assert 'connection' in get_reserved_names(include_private=True)
    assert 'become' in get_reserved_names(include_private=False)
    assert 'become' in get_reserved_

# Generated at 2022-06-13 17:38:17.617622
# Unit test for function get_reserved_names
def test_get_reserved_names():
    from ansible.playbook import Play
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.task import Task

    # Setup the classes
    classes = [Play, Block, Role, Task]

    # Get the reserved names
    reserved = get_reserved_names()

    # Check if all classes attributes are in the reserved names
    for aclass in classes:
        my_obj = aclass()
        for attr in my_obj.__dict__['_attributes']:
            assert attr in reserved

    # Check there is no missing attributes
    assert len(reserved) == 51

    # Check there is no duplicates
    assert len(set(reserved)) == 51

# Generated at 2022-06-13 17:38:20.879402
# Unit test for function get_reserved_names
def test_get_reserved_names():
    test_list = ["name", "private", "only_if", "tags"]
    reserved_list = get_reserved_names(include_private=True)

    assert(reserved_list.intersection(set(test_list)) == set(test_list))

# Generated at 2022-06-13 17:38:30.388636
# Unit test for function get_reserved_names
def test_get_reserved_names():
    public = frozenset([
        'connection',
        'gather_facts',
        'hosts',
        'name',
        'roles',
        'strategy',
        'sudo',
        'sudo_user',
        'tags',
        'tasks',
        'when',
    ])
    private = frozenset([
        'action',
        'delegate_to',
        'delegate_facts',
        'environment',
        'ignore_errors',
        'local_action',
        'loop',
        'name',
        'notify',
        'notified_by',
        'register',
        'retries',
        'until',
        'wait_for',
        'with_',
    ])

# Generated at 2022-06-13 17:38:35.735434
# Unit test for function get_reserved_names
def test_get_reserved_names():
    pub_r1 = frozenset(['hosts', 'roles'])
    priv_r1 = frozenset(['gather_facts', 'name', 'register', 'vars_files'])
    assert get_reserved_names(include_private=False) == pub_r1
    assert get_reserved_names(include_private=True) == pub_r1.union(priv_r1)


__all__ = ['is_reserved_name', 'warn_if_reserved']