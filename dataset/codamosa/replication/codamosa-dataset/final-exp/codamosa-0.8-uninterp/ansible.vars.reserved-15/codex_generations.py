

# Generated at 2022-06-13 17:28:56.258516
# Unit test for function get_reserved_names
def test_get_reserved_names():
    expected = frozenset([u'hosts', u'method', u'tasks', u'include', u'block', u'blocks', u'tags', u'register', u'remote_user', u'vars', u'environment', u'name', u'roles', u'serial', u'local_action', u'with_items', u'delegate_to', u'handler_name', u'connection', u'when', u'notify', u'poll', u'tags', u'changed_when', u'failed_when', u'include_role', u'import_playbook', u'include_tasks', u'local_action', u'ignore_errors', u'with_', u'check_mode', u'local_action'])
    result = get_reserved_names()
    assert expected == result

# Generated at 2022-06-13 17:29:07.312874
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' this function tests that get_reserved_names() returns what we expect '''


# Generated at 2022-06-13 17:29:08.451964
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert len(get_reserved_names(include_private=False)) > len(get_reserved_names(include_private=True))



# Generated at 2022-06-13 17:29:16.293500
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # Objects that match these should have no extra attributes.
    expected_no_attribs = (
        'name', 'connection', 'sudo', 'sudo_user', 'environment', 'register', 'ignore_errors',
        'any_errors_fatal', 'delegate_to', 'local_action', 'transport', 'remote_user',
        'run_once', 'connection_user', 'no_log', 'su', 'su_user', 'when', 'changed_when',
        'failed_when', 'tags', 'check_mode', 'block', 'always_run', 'serial', 'post_tasks',
        'pre_tasks', 'notify', 'handlers', 'meta', 'vars', 'hosts', 'roles', 'tasks',
    )

    # Objects that match these should have no additional public attributes.
   

# Generated at 2022-06-13 17:29:22.736740
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' test that the list of reserved names is not empty '''
    assert len(get_reserved_names()) > 0
    assert 'action' in get_reserved_names()
    assert 'local_action' not in get_reserved_names()
    assert 'with_' not in get_reserved_names()
    assert 'private' not in get_reserved_names()
    assert 'private' in get_reserved_names(include_private=True)


# Generated at 2022-06-13 17:29:29.733393
# Unit test for function get_reserved_names
def test_get_reserved_names():
    import sys
    import os

    if os.path.exists(__file__):
        # We're running as a unit test, so we can assume Ansible is on the PYTHONPATH
        import ansible
        f = os.path.dirname(ansible.__file__) + '/playbook/__init__.py'
    else:
        # Assume the unit tests are being run directly in the top-level directory
        f = 'lib/ansible/playbook/__init__.py'

    for line in open(f, 'r').readlines():
        if line.startswith('__version__'):
            version = line.split('=')[1].strip().replace('"', '')
            break

# Generated at 2022-06-13 17:29:38.488435
# Unit test for function get_reserved_names
def test_get_reserved_names():
    public = frozenset(['name', 'hosts', 'connection', 'gather_facts', 'any_errors_fatal', 'serial', 'sudo', 'sudo_user', 'tags', 'environment', 'when', 'notify', 'async', 'poll', 'register', 'ignore_errors', 'always_run', 'local_action', 'transport', 'vars_prompt', 'vars_files', 'vars_prompt', 'any_errors_fatal', 'asserts', 'delegate_to', 'run_once', 'first_available_file'])

# Generated at 2022-06-13 17:29:49.264469
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:29:58.873578
# Unit test for function get_reserved_names
def test_get_reserved_names():

    assert 'action' in get_reserved_names()
    assert 'block' in get_reserved_names()
    assert 'hosts' in get_reserved_names()
    assert 'pre_tasks' in get_reserved_names()
    assert 'post_tasks' in get_reserved_names()
    assert 'name' in get_reserved_names()
    assert 'roles' in get_reserved_names()
    assert 'tasks' in get_reserved_names()
    assert 'with_' in get_reserved_names()

    assert 'private' in get_reserved_names(include_private=True)
    assert 'private' not in get_reserved_names(include_private=False)



# Generated at 2022-06-13 17:30:01.241174
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # print get_reserved_names()
    assert isinstance(get_reserved_names(), set)
    assert get_reserved_names().__len__() > 0



# Generated at 2022-06-13 17:30:20.782639
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert len(get_reserved_names()) == len(get_reserved_names(False)) + 3, 'A reserved name was added without updating tests'

    assert 'pre_tasks' in get_reserved_names(), 'pre_tasks is a reserved name'
    assert 'post_tasks' in get_reserved_names(), 'post_tasks is a reserved name'
    assert 'vars' in get_reserved_names(), 'vars is a reserved name'
    assert 'register' in get_reserved_names(), 'register is a reserved name'
    assert 'no_log' in get_reserved_names(), 'no_log is a reserved name'
    assert 'action' in get_reserved_names(), 'action is a reserved name'

# Generated at 2022-06-13 17:30:27.334866
# Unit test for function get_reserved_names
def test_get_reserved_names():
    names = get_reserved_names()
    expected = frozenset(['private', 'vars', 'register', 'roles', 'gather_facts', 'hosts', 'serial', 'include', 'tasks', 'action', 'any_errors_fatal', 'become', 'block', 'connection', 'delegate_to', 'environment', 'first_available_file', 'ignore_errors', 'local_action', 'max_fail_percentage', 'name', 'notify', 'other_errors_fatal', 'pause', 'pre_tasks', 'post_tasks', 'roles_path', 'run_once', 'serial', 'sudo', 'sudo_user', 'sudo_password', 'tags', 'transport', 'when', 'with_', 'handler', 'environment', 'no_log', 'always_run'])
    assert expected

# Generated at 2022-06-13 17:30:32.663328
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # test reserved with minimal set of possible attributes
    class Ob(object):
        _attributes = {'role_name': {'private': True}, 'name': {}}

    assert get_reserved_names() == frozenset(['name', 'role_name'])
    assert get_reserved_names(include_private=False) == frozenset(['name'])

# Generated at 2022-06-13 17:30:36.015585
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert(_RESERVED_NAMES.issubset(get_reserved_names()))
    assert(get_reserved_names(include_private=False).issubset(_RESERVED_NAMES))

# Generated at 2022-06-13 17:30:37.207885
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert isinstance(get_reserved_names(), set)

# Generated at 2022-06-13 17:30:41.464344
# Unit test for function get_reserved_names
def test_get_reserved_names():
    result = get_reserved_names(include_private=False)
    assert isinstance(result, set)
    assert len(result) == 16
    assert 'roles' in result
    assert 'pre_tasks' in result
    assert 'post_tasks' in result
    assert 'tasks' in result
    assert 'vars' in result
    assert 'handlers' in result



# Generated at 2022-06-13 17:30:51.892215
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved = get_reserved_names(include_private=False)
    assert 'vars' in reserved
    assert 'environment' in reserved
    assert 'others' in reserved
    assert 'sudo' in reserved
    assert 'sudo_user' in reserved
    assert 'su' in reserved
    assert 'su_user' in reserved

    reserved = get_reserved_names(include_private=True)
    assert 'vars' in reserved
    assert 'environment' in reserved
    assert 'others' in reserved
    assert 'sudo' in reserved
    assert 'sudo_user' in reserved
    assert 'su' in reserved
    assert 'su_user' in reserved
    assert 'gather_facts' in reserved
    assert 'tags' in reserved
    assert 'ignore_errors' in reserved
    assert 'delegate_to' in reserved
   

# Generated at 2022-06-13 17:31:00.334769
# Unit test for function get_reserved_names
def test_get_reserved_names():
    public_names = get_reserved_names(include_private=False)
    private_names = get_reserved_names(include_private=True)

    # All private names should also be public
    assert set(private_names).issuperset(set(public_names))

    assert 'name' in public_names
    assert 'any_errors_fatal' in public_names
    assert 'connection' in public_names
    assert 'with_' in public_names
    assert 'with_dict' in private_names
    assert 'with_first_found' in private_names
    assert 'with_items' in public_names
    assert 'with_nested' in private_names
    assert 'with_subelements' in private_names
    assert 'with_together' in private_names

# Generated at 2022-06-13 17:31:07.849325
# Unit test for function get_reserved_names
def test_get_reserved_names():
    '''
    This unittest is to test the get_reserved_names utility function
    '''

    # FIXME: it is an anti-pattern to test private functions. The function tested
    # can be part of the public API
    for aclass in [Play, Role, Block, Task]:
        # ensure all the public names are in the returned list
        reserved_names = get_reserved_names()
        aobj = aclass()
        for attribute in aobj.__dict__['_attributes']:
            if 'private' not in attribute:
                assert attribute in reserved_names

# Generated at 2022-06-13 17:31:11.475730
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert('name' in get_reserved_names())
    assert('hosts' in get_reserved_names())

    assert(len(get_reserved_names()) > len(get_reserved_names(include_private=False)))



# Generated at 2022-06-13 17:31:38.124169
# Unit test for function get_reserved_names
def test_get_reserved_names():
    public = {'hosts', 'roles', 'name', 'vars', 'tags', 'gather_facts', 'any_errors_fatal', 'max_fail_percentage', 'serial', 'remote_user',
              'sudo', 'sudo_user', 'become', 'become_user', 'environment', 'no_log', 'connection', 'port', 'remote_addr', 'local_action',
              'with_', 'ignore_errors'}


# Generated at 2022-06-13 17:31:43.938008
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:31:47.161954
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert 'roles' in get_reserved_names(True)
    assert 'roles' in get_reserved_names(False)
    assert 'private' not in get_reserved_names(False)
    assert 'private' in get_reserved_names(True)


# Generated at 2022-06-13 17:31:55.341036
# Unit test for function get_reserved_names
def test_get_reserved_names():
    '''unit test for function get_reserved_names'''


# Generated at 2022-06-13 17:32:02.608602
# Unit test for function get_reserved_names
def test_get_reserved_names():
    test = get_reserved_names(include_private=False)
    assert 'hosts' in test
    assert 'roles' in test
    assert 'action' in test
    assert 'local_action' in test
    assert 'with_' in test
    assert 'when' in test
    assert 'name' in test
    assert 'tags' in test
    assert 'gather_facts' in test
    assert 'serial' in test
    assert 'register' in test
    assert 'ignore_errors' in test
    assert 'delegate_to' in test
    assert 'loop' not in test
    assert 'private' not in test
    assert 'transport' not in test

# Generated at 2022-06-13 17:32:05.363843
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert 'vars' in _RESERVED_NAMES
    assert 'hosts' in _RESERVED_NAMES
    assert 'action' in _RESERVED_NAMES

# Generated at 2022-06-13 17:32:11.183843
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' this function tests get_reserved_names() by asserting that certain strings are
        in the reserved names, and that certain strings are not '''

    assert 'include_tasks' in get_reserved_names()
    assert 'private_role_vars' in get_reserved_names()
    assert 'not_reserved' not in get_reserved_names()
    assert 'not_reserved' in get_reserved_names(include_private=True)
    assert 'private_role_vars' not in get_reserved_names(include_private=False)



# Generated at 2022-06-13 17:32:17.795777
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:32:26.821979
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:32:32.728982
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # Test that no private names are in get_reserved_names(False)
    public_names = get_reserved_names(include_private=False)
    private_names = get_reserved_names(include_private=True).difference(public_names)
    assert len(private_names) == 0, 'Found private names in public reserved name list'

# Generated at 2022-06-13 17:32:52.692412
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert get_reserved_names(include_private=False) == frozenset(['any_errors_fatal', 'become', 'connection', 'delegate_to', 'gather_facts', 'hosts', 'ignore_errors', 'roles', 'serial', 'tags', 'task_action', 'task_args', 'task_delegate_to', 'task_tags', 'tasks', 'when', 'vars', 'with_'])

# Generated at 2022-06-13 17:32:58.507349
# Unit test for function get_reserved_names
def test_get_reserved_names():
    res = get_reserved_names(include_private=True)
    assert isinstance(res, set)
    assert len(res) > 20
    assert 'action' in res
    assert 'hosts' in res
    assert 'gather_facts' in res
    assert 'include_vars' in res  # private, so it must be there
    assert 'include_role' in res



# Generated at 2022-06-13 17:33:03.143960
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved = get_reserved_names()
    assert isinstance(reserved, set)
    assert 'hosts' in reserved

    # assert that local_action is implicitly in reserved names list
    assert 'local_action' in reserved

    # assert that with_ is implicitly in reserved names list
    assert 'with_' in reserved

    # assert that all reserved names are included
    assert len(_RESERVED_NAMES) == len(reserved)



# Generated at 2022-06-13 17:33:09.660177
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' test_get_reserved_names '''
    assert 'action' in _RESERVED_NAMES
    assert 'become' in _RESERVED_NAMES
    assert 'with_' in _RESERVED_NAMES
    assert 'local_action' in _RESERVED_NAMES
    assert 'loop' in _RESERVED_NAMES
    assert 'action' in _RESERVED_NAMES
    assert 'block' in _RESERVED_NAMES
    assert 'with_items' in _RESERVED_NAMES



# Generated at 2022-06-13 17:33:16.234346
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert isinstance(get_reserved_names(), frozenset)
    assert len(get_reserved_names()) > 1
    assert isinstance(get_reserved_names(include_private=False), frozenset)
    assert len(get_reserved_names(include_private=False)) > 1
    assert get_reserved_names().issuperset(['hosts'])
    assert get_reserved_names(include_private=False).issuperset(['hosts'])
    assert get_reserved_names(include_private=False).issubset(get_reserved_names())

# Generated at 2022-06-13 17:33:18.319013
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # Make sure we have names that don't conflict with class attributes
    assert set(['action', 'private', 'with_', 'delegate_to',
                'run_once', 'become_user', 'connection', 'async']) == get_reserved_names(include_private=True)

# Generated at 2022-06-13 17:33:30.562983
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved = get_reserved_names()

    assert 'action' in reserved
    assert 'local_action' in reserved
    assert 'when' in reserved
    assert 'async' in reserved
    assert 'block' in reserved
    assert 'notify' in reserved
    assert 'become_user' in reserved
    assert 'become' in reserved
    assert 'connection' in reserved
    assert 'any_errors_fatal' in reserved
    assert 'changed_when' in reserved
    assert 'delegate_to' in reserved
    assert 'first_available_file' in reserved
    assert 'failed_when' in reserved
    assert 'gather_facts' in reserved
    assert 'ignore_errors' in reserved
    assert 'register' in reserved
    assert 'retries' in reserved
    assert 'until' in reserved

# Generated at 2022-06-13 17:33:39.501464
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # known values
    assert 'name' in _RESERVED_NAMES
    assert 'hosts' in _RESERVED_NAMES
    assert 'action' in _RESERVED_NAMES
    assert 'local_action' in _RESERVED_NAMES
    assert 'loop' in _RESERVED_NAMES
    assert 'with_' in _RESERVED_NAMES

    # expected length
    # FIXME: not a hard number, depends on the reserved names
    assert len(_RESERVED_NAMES) <= 22

    # check if private names are included
    assert 'vars_prompt' in _RESERVED_NAMES
    assert 'run_once' in _RESERVED_NAMES

    # check if private names are excluded

# Generated at 2022-06-13 17:33:43.872706
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved_names = get_reserved_names()
    assert 'vars' in reserved_names
    assert 'include_vars' in reserved_names
    assert 'import_tasks' in reserved_names
    assert 'handlers' in reserved_names
    assert 'block' in reserved_names


# Generated at 2022-06-13 17:33:50.441780
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:34:29.518838
# Unit test for function get_reserved_names
def test_get_reserved_names():
    names = get_reserved_names(include_private=False)
    assert 'gather_facts' in names
    assert 'name' in names
    assert 'hosts' in names
    assert 'roles' in names
    assert 'vars' in names
    assert 'any_errors_fatal' in names
    assert 'no_log' in names
    assert '_raw_params' not in names
    names = get_reserved_names()
    assert '_raw_params' in names
    assert 'connection' in names
    assert 'sudo_user' in names
    assert 'sudo' in names
    assert 'sudo_flags' in names
    assert 'become' in names
    assert 'become_user' in names
    assert 'become_method' in names

# Generated at 2022-06-13 17:34:37.332026
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert set(get_reserved_names(include_private=False)) == set(
        ['name', 'hosts', 'roles', 'vars', 'vars_files', 'action', 'delegate_to', 'register', 'ignore_errors', 'local_action']
    )

# Generated at 2022-06-13 17:34:40.582922
# Unit test for function get_reserved_names
def test_get_reserved_names():
    result = get_reserved_names()
    assert 'action' in result
    assert 'local_action' in result
    assert 'loop' in result
    assert 'with_' in result

# Generated at 2022-06-13 17:34:49.239566
# Unit test for function get_reserved_names
def test_get_reserved_names():
    '''test against a hardcoded list'''

# Generated at 2022-06-13 17:34:55.413299
# Unit test for function get_reserved_names
def test_get_reserved_names():
    from ansible.playbook import Play

    public = set(get_reserved_names(include_private=False))
    private = set(get_reserved_names(include_private=True))

    # get public names associated with the Play() class
    aobj = Play()
    aobj_public = set()
    for attribute in aobj.__dict__['_attributes']:
        if 'private' not in attribute:
            aobj_public.add(attribute)

    assert aobj_public == public, 'public names have changed'
    assert len(aobj_public.union(private)) == len(private), 'private names have changed'



# Generated at 2022-06-13 17:35:05.412183
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # This is a test of get_reserved_names
    # we define this class so we can manipulate/define attributes
    # then we can look at the attributes and see if certain words are
    # in the set, to test get_reserved_names
    class TheClass(object):
        def __init__(self):
            i = 0

    # initialize set of known reserved names
    known_reserved_names = set()
    known_reserved_names.add('name')
    known_reserved_names.add('hosts')
    known_reserved_names.add('action')
    known_reserved_names.add('others')
    known_reserved_names.add('vars')
    known_reserved_names.add('roles')
    known_reserved_names.add('tasks')
    known

# Generated at 2022-06-13 17:35:08.834197
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # Check both private and public result to make sure our reserved names are for real
    assert get_reserved_names(include_private=True)
    assert get_reserved_names(include_private=False)

# Generated at 2022-06-13 17:35:17.415351
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # C0111(missing-docstring) pylint: disable=C0111

    public = get_reserved_names(include_private=False)
    private = get_reserved_names(include_private=True)
    all_local = get_reserved_names(include_private=False).union(get_reserved_names(include_private=True))

    assert len(all_local) > len(public)

    # make sure all private names are in the all list
    assert len(private.difference(all_local)) == 0

    # local_action is implicit with action
    assert 'local_action' in public

    # loop implies with_
    # FIXME: remove after with_ is not only deprecated but removed
    assert 'with_' in public

    # loop is deprecated, but still private
    assert 'loop'

# Generated at 2022-06-13 17:35:25.562373
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:35:36.273828
# Unit test for function get_reserved_names
def test_get_reserved_names():
    from ansible.plugins.loader import action_loader, filter_loader

    def _get_filter_plugins():
        from ansible.constants import DEFAULT_FILTER_PLUGIN_PATH
        f = set()
        for p in filter_loader._find_plugins(DEFAULT_FILTER_PLUGIN_PATH):
            f.add(p.name)
        return f

    filter_plugins = _get_filter_plugins()

    # these keywords aren't actually reserved, but they are also not compiled into
    # the action plugin dictionary and are thus also reserved
    # FIXME: they should be compiled into the action plugin dictionary

# Generated at 2022-06-13 17:36:49.435243
# Unit test for function get_reserved_names
def test_get_reserved_names():
    expected_public = set(['any_errors_fatal', 'become', 'become_user', 'remote_user',
                           'name', 'gather_facts', 'roles', 'roles_path', 'vars',
                           'blocks', 'handlers', 'block', 'include', 'include_vars',
                           'include_tasks', 'pre_tasks', 'post_tasks', 'tasks',
                           'action', 'local_action', 'with_items', 'with_dict',
                           'with_fileglob', 'with_first_found', 'with_nested', 'with_sequence',
                           'with_struc', 'with_together', 'with_weirdo', 'delegate_to', 'delegate_facts'])

# Generated at 2022-06-13 17:36:55.755367
# Unit test for function get_reserved_names
def test_get_reserved_names():
    def compare_results(result):
        assert isinstance(result, set)
        assert 'name' in result
        assert 'hosts' in result
        assert 'roles' in result
        assert 'block' in result
        assert 'ignore_errors' in result
        assert 'action' in result
        assert 'local_action' in result
        assert 'with_' in result
        assert 'loop' in result

    all_results = get_reserved_names()
    compare_results(all_results)



# Generated at 2022-06-13 17:37:04.470445
# Unit test for function get_reserved_names
def test_get_reserved_names():
    class Test:
        _private = set()
        _public = set()


# Generated at 2022-06-13 17:37:10.887588
# Unit test for function get_reserved_names
def test_get_reserved_names():
    r = get_reserved_names()
    assert frozenset(['name', 'action', 'local_action', 'block', 'rescue', 'always', 'delegate_to',
                      'delegate_facts', 'with_items', 'tags', 'when', 'notify', 'first_available_file',
                      'vars', 'vars_files', 'static', 'include', 'role_names', 'roles', 'tasks', 'handlers']) <= r

    r = get_reserved_names(include_private=False)

# Generated at 2022-06-13 17:37:16.014010
# Unit test for function get_reserved_names
def test_get_reserved_names():
    names_public = ['name', 'hosts', 'user', 'connection', 'delegate_to', 'gather_facts']
    names_private = ['serial', 'sudo']
    names_all = names_public + names_private

    names = get_reserved_names(True)
    assert set(names) == set(names_all)

    names = get_reserved_names(False)
    assert set(names) == set(names_public)

# Generated at 2022-06-13 17:37:24.730863
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert 'hosts' in get_reserved_names()
    assert 'roles' in get_reserved_names()
    assert 'tasks' in get_reserved_names()

    assert 'handlers' in get_reserved_names()
    assert 'block' in get_reserved_names()
    assert 'task' in get_reserved_names()

    assert 'when' in get_reserved_names()
    assert 'become' in get_reserved_names()
    assert 'delegate_to' in get_reserved_names()

    assert len(get_reserved_names(include_private=False)) > len(get_reserved_names(include_private=True))

# Generated at 2022-06-13 17:37:32.948413
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' test function get_reserved_names '''


# Generated at 2022-06-13 17:37:37.291677
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert("tasks" in get_reserved_names())
    assert("roles" in get_reserved_names())
    assert("strategy" in get_reserved_names())
    assert("loop" not in get_reserved_names())
    assert("_loop" in get_reserved_names(include_private=True))



# Generated at 2022-06-13 17:37:42.862064
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert(get_reserved_names(False) == get_reserved_names(True))
    assert('name' in get_reserved_names())
    assert('tags' in get_reserved_names())
    assert('when' in get_reserved_names())
    assert('loop' in get_reserved_names(True))
    assert('with_' in get_reserved_names(True))
    assert('local_action' in get_reserved_names(True))

# Generated at 2022-06-13 17:37:49.616317
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert get_reserved_names() == _RESERVED_NAMES