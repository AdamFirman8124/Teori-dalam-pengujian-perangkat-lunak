

# Generated at 2022-06-13 17:28:45.375452
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert len(_RESERVED_NAMES)

# Generated at 2022-06-13 17:28:55.845118
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:28:58.252711
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert False


# Generated at 2022-06-13 17:28:59.609478
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert isinstance(get_reserved_names(), set)


# Generated at 2022-06-13 17:29:07.175373
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved = ['hosts', 'roles', 'vars', 'name', 'action', 'local_action', 'with_', 'block', 'blockinfile', 'blockreplace', 'blockreplacecontent',
                'blockcontent', 'blockfilestart', 'blockfileend', 'blockfilebefore', 'blockfileafter', 'blockfilemarker', 'loop',
                'when', 'delegate_to', 'first_available_file', 'notify', 'poll', 'register', 'retries', 'until', 'attempts',
                'delay', 'tags', 'ignore_errors', 'always_run', 'run_once', 'listen', 'delegate_facts', '_loader', 'meta']
    assert get_reserved_names() == reserved

# Generated at 2022-06-13 17:29:15.595520
# Unit test for function get_reserved_names
def test_get_reserved_names():

    assert 'any_errors_fatal' in get_reserved_names(True)
    assert 'any_errors_fatal' in get_reserved_names(False)
    assert 'action' in get_reserved_names(True)
    assert 'action' in get_reserved_names(False)
    assert 'private_action' in get_reserved_names(True)
    assert 'private_action' not in get_reserved_names(False)
    assert 'handlers' in get_reserved_names(True)
    assert 'handlers' in get_reserved_names(False)
    assert 'loop' in get_reserved_names(True)
    assert 'loop' in get_reserved_names(False)
    assert 'with_' not in get_reserved_names(True)

# Generated at 2022-06-13 17:29:25.590758
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' This test checks if the list of reserved names for play objects is being generated correctly.
    '''
    private_reserved_names = {'become', 'become_method', 'become_user', 'distribution', 'error_on_undefined_vars', 'gather_facts',
                              'gather_subset', 'handlers', 'included_file', 'inventory', 'loop', 'name', 'no_log', 'os_family',
                              'post_validation', 'pre_validation', 'priority', 'tags', 'tasks', 'vars_files', 'vars_prompt',
                              'vault_password', 'version'}


# Generated at 2022-06-13 17:29:27.174329
# Unit test for function get_reserved_names
def test_get_reserved_names():
    """
    Make sure that the proper number of reserved names are returned
    """
    assert len(get_reserved_names()) == 10



# Generated at 2022-06-13 17:29:37.434323
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:29:48.754623
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:29:56.378221
# Unit test for function get_reserved_names
def test_get_reserved_names():
    pass


# Generated at 2022-06-13 17:30:04.603660
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:30:14.709143
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert get_reserved_names() == frozenset(['tasks', 'vars', 'handlers', 'roles', 'include_role', 'include_tasks', 'block', 'rescue', 'always', 'become', 'become_user', 'become_method', 'delegate_to', 'delegate_facts', 'register', 'vars_prompt', 'vars_files', 'pre_tasks', 'post_tasks', 'error_on_undefined_vars', 'name', 'gather_facts', 'gather_subset', 'gather_timeout', 'local_action', 'action', 'loop', 'when', 'with_', 'hosts'])

# Generated at 2022-06-13 17:30:20.821336
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved_public = ['roles', 'hosts', 'pre_tasks', 'tasks', 'post_tasks', 'any_errors_fatal', 'serial', 'max_fail_percentage', 'delegate_to', 'become', 'tags', 'gather_facts', 'name', 'vars', 'vars_files', 'include', 'import_playbook', 'include_role', 'include_tasks', 'environment', 'no_log', 'register', 'ignore_errors', 'local_action', 'with_']
    reserved_private = ['action', 'loop', 'first_available_file', 'files', 'loop_control', 'block', 'block_var_files', 'dynamic_blocks', 'block_hosts']

    reserved_public = set(reserved_public)

# Generated at 2022-06-13 17:30:32.171764
# Unit test for function get_reserved_names
def test_get_reserved_names():
    private_reserved = get_reserved_names(False)
    print("private_reserved: %s" % private_reserved)
    all_reserved = get_reserved_names(True)
    print("all_reserved: %s" % all_reserved)

    assert len(all_reserved) > len(private_reserved)
    assert 'connection' in private_reserved
    assert 'become_user' in private_reserved
    assert 'environment' in private_reserved
    assert 'roles' in private_reserved
    assert 'tasks' in private_reserved
    assert 'block' in private_reserved
    assert 'pre_tasks' in private_reserved
    assert 'post_tasks' in private_reserved
    assert 'handler_tasks' in private_reserved


# Generated at 2022-06-13 17:30:36.623199
# Unit test for function get_reserved_names
def test_get_reserved_names():
    public = get_reserved_names(include_private=False)

    assert 'register' in public
    assert 'private' not in public

    private = get_reserved_names(include_private=True)

    assert 'private' in private



# Generated at 2022-06-13 17:30:37.446720
# Unit test for function get_reserved_names
def test_get_reserved_names():
    print(get_reserved_names())
    print(get_reserved_names(include_private=False))


# Generated at 2022-06-13 17:30:39.432835
# Unit test for function get_reserved_names
def test_get_reserved_names():
    display.deprecated("Reserved names: %s" % (get_reserved_names()))

# Generated at 2022-06-13 17:30:40.964438
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert len(get_reserved_names(False)) > 0


# Generated at 2022-06-13 17:30:49.583527
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' make sure the reserved names are as expected'''

    # some names that were reserved in earlier versions
    old_reserved = ['sudo_user', 'sudo', 'sudo_pass', 'sudo_exe', 'connection']
    test_dict1 = {}
    test_dict2 = {}
    test_dict3 = {}

    # build test dict from old inventory YAML file as old_reserved
    for item in old_reserved:
        test_dict1[item] = None

    # build test dict from current reserved names
    for item in get_reserved_names():
        test_dict2[item] = None

    # build expected test
    expected_result = test_dict2.copy()
    expected_result.update(test_dict1)

    # test function output

# Generated at 2022-06-13 17:31:11.656041
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert get_reserved_names() == frozenset([
        'any_errors_fatal',
        'become',
        'become_method',
        'become_user',
        'block',
        'connection',
        'delegate_to',
        'gather_facts',
        'handler',
        'hosts',
        'ignore_errors',
        'include',
        'include_tasks',
        'include_role',
        'include_vars',
        'local_action',
        'name',
        'no_log',
        'notify',
        'post_tasks',
        'pre_tasks',
        'roles',
        'serial',
        'tags',
        'tasks',
    ])


# Generated at 2022-06-13 17:31:20.451480
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved = get_reserved_names(False)

    assert isinstance(reserved, set)

    known_reserved = set(['any_errors_fatal', 'connection', 'delegate_to', 'become',
                          'gather_facts', 'ignore_errors', 'sudo', 'sudo_user', 'when'])
    assert not known_reserved.symmetric_difference(reserved)

    reserved = get_reserved_names()

    known_reserved.add('async_status')
    known_reserved.add('become_user')
    known_reserved.add('fail_mode')
    known_reserved.add('first_playbook')
    known_reserved.add('ignore_unavailable_facts')
    known_reserved.add('loop')
    known_reserved.add

# Generated at 2022-06-13 17:31:28.724243
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # Test for default (include_private all)
    reserved_names = get_reserved_names()
    assert ('pause' in reserved_names) is True
    assert ('register' in reserved_names) is True
    assert ('action' in reserved_names) is True
    assert ('pre_tasks' in reserved_names) is True
    assert ('roles' in reserved_names) is True
    assert ('post_tasks' in reserved_names) is True
    assert ('block' in reserved_names) is True
    assert ('tasks' in reserved_names) is True
    assert ('handlers' in reserved_names) is True
    assert ('when' in reserved_names) is True
    assert ('loop' in reserved_names) is True

    # Test for include_private off

# Generated at 2022-06-13 17:31:37.503395
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # FIXME: move to test/unit/playbook/test_utils.py
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task

    class_list = [Play, Role, Block, Task]

    result = get_reserved_names()

    assert isinstance(result, frozenset)

    for aclass in class_list:
        aobj = aclass()

        # build ordered list to loop over and dict with attributes
        for attribute in aobj.__dict__['_attributes']:
            assert attribute in result


# Generated at 2022-06-13 17:31:40.741745
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert get_reserved_names() == _RESERVED_NAMES
    assert len(get_reserved_names(True)) > len(get_reserved_names(False))
    assert get_reserved_names(True) != get_reserved_names(False)


# Generated at 2022-06-13 17:31:48.628828
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # Only run from parent directory
    if __file__.startswith('.'):
        return
    import os
    import sys
    import pytest
    try:
        mydir = os.path.dirname(os.path.realpath(__file__))
    except NameError:
        mydir = os.getcwd()
    # On some systems __file__ is not defined.
    # Running tests from the source distribution fails.
    # If we cannot find the source, just skip the test.
    else:
        if mydir.endswith('contrib/inventory/test_reserved_names') and 'site-packages' in mydir:
            rootdir = os.path.join(mydir, '../..')
            sys.path.insert(0, rootdir)
        else:
            return


# Generated at 2022-06-13 17:31:55.286794
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' this function unit tests reserved names that are used in plays '''

    # list of public names
    public = set(['hosts', 'name', 'gather_facts', 'any_errors_fatal', 'serial', 'max_fail_percentage', 'remote_user', 'sudo', 'sudo_user', 'sudo_pass', 'tags', 'skip_tags', 'force_handlers', 'connection', 'port', 'environment', 'vars', 'vars_files', 'vars_prompt', 'vault_id', 'tags', 'delegate_to', 'transport', 'when'])

    # list of private names

# Generated at 2022-06-13 17:31:57.769525
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ret = get_reserved_names(include_private=False)
    assert len(ret) > 0

    ret = get_reserved_names(include_private=True)
    assert len(ret) > 0



# Generated at 2022-06-13 17:32:07.055883
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert isinstance(_RESERVED_NAMES, frozenset)

# Generated at 2022-06-13 17:32:09.307740
# Unit test for function get_reserved_names
def test_get_reserved_names():
    result = get_reserved_names(include_private=False)
    assert 'name' in result

    result = get_reserved_names(include_private=True)
    assert 'name' in result
    assert '_remote_user' in result



# Generated at 2022-06-13 17:32:41.743927
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' This unit test ensures the list of reserved names is correct.
    '''

    # Check reserved name list without private names

# Generated at 2022-06-13 17:32:45.662328
# Unit test for function get_reserved_names
def test_get_reserved_names():

    # Get reserved attribute names
    reserved = get_reserved_names()
    assert len(reserved) == 134

    # Get reserved attribute names, excluding private names
    reserved = get_reserved_names(include_private=False)
    assert len(reserved) == 128

# Generated at 2022-06-13 17:32:50.509352
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' test reserved names '''

    reserved = set(get_reserved_names())

    assert len(reserved) > 0

    assert 'hosts' in reserved
    assert 'name' in reserved
    assert 'gather_facts' in reserved
    assert 'any_errors_fatal' in reserved
    assert 'serial' in reserved
    assert 'action' in reserved
    assert 'remote_user' in reserved

# Generated at 2022-06-13 17:32:55.940082
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert len(get_reserved_names()) > 0
    assert len(get_reserved_names(include_private=False)) > 0
    assert len(get_reserved_names(include_private=True)) > len(get_reserved_names(include_private=False))

# Generated at 2022-06-13 17:33:04.214659
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:33:06.403191
# Unit test for function get_reserved_names
def test_get_reserved_names():
    result = get_reserved_names()
    assert isinstance(result, set)
    assert len(result) > 0

# Generated at 2022-06-13 17:33:16.467067
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:33:28.386767
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved_names = get_reserved_names()

# Generated at 2022-06-13 17:33:36.000456
# Unit test for function get_reserved_names
def test_get_reserved_names():

    public = set(['hosts', 'name', 'gather_facts', 'connection', 'vars', 'vars_files', 'roles', 'include', 'include_vars'])
    private = set(['pre_tasks', 'tasks', 'post_tasks', 'handlers', 'delegate_to', 'notify', 'listen', 'serial', 'any_errors_fatal', 'max_fail_percentage'])

    result = get_reserved_names()

    assert result == public.union(private)
    assert result.issuperset(public)
    assert result.issuperset(private)

# Generated at 2022-06-13 17:33:45.514996
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # test with default
    assert 'roles' in get_reserved_names(include_private=True)

    # test without private names
    assert 'roles' in get_reserved_names(include_private=False)
    assert 'vars_prompt' not in get_reserved_names(include_private=False)
    assert 'any_errors_fatal' not in get_reserved_names(include_private=False)
    assert 'become_user' not in get_reserved_names(include_private=False)

    # test loop and with_
    assert 'with_' in get_reserved_names(include_private=True) # deprecated
    assert 'loop' not in get_reserved_names(include_private=True) # deprecated

# Generated at 2022-06-13 17:34:36.864449
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved = set(["name", "hosts", "roles", "tasks", "handlers"])
    assert get_reserved_names() == reserved



# Generated at 2022-06-13 17:34:41.615271
# Unit test for function get_reserved_names
def test_get_reserved_names():
    public = get_reserved_names(include_private=False)
    assert len(public) == 22
    assert 'role_path' in public

    private = get_reserved_names(include_private=True)
    assert len(private) == 34
    assert 'loop' in private

# Generated at 2022-06-13 17:34:44.855027
# Unit test for function get_reserved_names
def test_get_reserved_names():

    names = get_reserved_names()
    assert names is not None
    assert 'connection' in names

    names = get_reserved_names(False)
    assert names is not None
    assert 'connection' in names
    assert 'any_errors_fatal' not in names

# Generated at 2022-06-13 17:34:49.629127
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved = get_reserved_names()
    # Test private names not default in result
    assert 'private' not in reserved
    # Test local_action present when action is present
    assert 'local_action' in reserved
    # Test with_ present when loop is present
    assert 'with_' in reserved

# Generated at 2022-06-13 17:34:54.339178
# Unit test for function get_reserved_names
def test_get_reserved_names():
    names = get_reserved_names()
    assert 'hosts' in names
    assert 'pre_tasks' in names
    assert 'roles' in names
    assert 'tasks' in names
    assert 'post_tasks' in names


# unit tests for warn_if_reserved

# Generated at 2022-06-13 17:34:56.184483
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved_attributes = get_reserved_names()
    assert 'hosts' in reserved_attributes


# Generated at 2022-06-13 17:34:58.262173
# Unit test for function get_reserved_names
def test_get_reserved_names():
    result = get_reserved_names()
    assert type(result) is set
    assert result.__contains__('name') is True

# Generated at 2022-06-13 17:35:03.682633
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # This test case can go away once it passes
    # We should never have this happen
    # assert 'name' in get_reserved_names()
    # This test is dependent on the current state of fact gathering.
    # We don't want to be constantly changing this so it's not in the list
    assert 'ansible_local' in get_reserved_names(include_private=False)



# Generated at 2022-06-13 17:35:13.752978
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:35:17.778829
# Unit test for function get_reserved_names
def test_get_reserved_names():
    results = get_reserved_names()
    assert 'block' in results

    results = get_reserved_names(False)
    assert results == get_reserved_names()
    assert 'vars' in results
    assert 'block' in results
    assert 'any_errors_fatal' in results



# Generated at 2022-06-13 17:37:06.504496
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # list of reserved names - these are internal to ansible
    reserved = set(get_reserved_names())

    # list of public names, these are not internal
    public = set(['roles', 'hosts', 'gather_facts', 'connection', 'sudo', 'sudo_user',
                  'remote_user', 'environment', 'no_log', 'vars', 'vars_prompt',
                  'vars_files', 'tags', 'transport', 'when', 'post_tasks', 'pre_tasks',
                  'handlers'])

    # list of private names, these are not internal

# Generated at 2022-06-13 17:37:13.848095
# Unit test for function get_reserved_names
def test_get_reserved_names():
    public_expected = set(['action', 'any_errors_fatal', 'any_errors_fatal', 'continue_on_error', 'connection',
                           'delegate_to', 'gather_facts', 'gather_subset', 'hosts', 'ignore_errors',
                           'ignore_unreachable', 'when', 'local_action', 'max_fail_percentage', 'meta', 'no_log',
                           'notify', 'post_tasks', 'pre_tasks', 'role_name', 'register', 'remote_user',
                           'serial', 'strategy', 'sudo', 'sudo_user', 'tags', 'tasks', 'transport', 'vars_files',
                           'vars_prompt', 'vault_password_files', 'with_'])


# Generated at 2022-06-13 17:37:23.851247
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved_names = get_reserved_names()

    assert 'hosts' in reserved_names
    assert 'hosts' in reserved_names
    assert 'any_errors_fatal' in reserved_names
    assert 'remote_user' in reserved_names
    assert 'sudo' in reserved_names
    assert 'sudo_user' in reserved_names
    assert 'connection' in reserved_names
    assert 'gather_facts' in reserved_names
    assert 'gather_subset' in reserved_names
    assert 'no_log' in reserved_names
    assert 'serial' in reserved_names
    assert 'force_handlers' in reserved_names
    assert 'environment' in reserved_names
    assert 'tags' in reserved_names
    assert 'ignore_errors' in reserved_names
    assert 'roles' in reserved_names


# Generated at 2022-06-13 17:37:32.273971
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:37:40.489410
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # Test for empty result
    assert len(get_reserved_names(include_private=False)) == 0
    # Test order
    assert get_reserved_names()[0] > get_reserved_names()[1]
    # Test for results
    assert get_reserved_names(include_private=False)[-1] == 'vars'
    assert get_reserved_names(include_private=False)[-2] == 'task'
    assert get_reserved_names(include_private=False)[-3] == 'hosts'
    assert get_reserved_names(include_private=False)[-4] == 'name'
    assert get_reserved_names(include_private=False)[-5] == 'dynamic'

# Generated at 2022-06-13 17:37:48.082688
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:37:53.020670
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert 'tasks' in get_reserved_names()

    # local_action is implied by action
    assert 'local_action' in get_reserved_names()
    assert 'action' in get_reserved_names()

    # with_ is implied by loop
    assert 'with_' in get_reserved_names()
    assert 'loop' in get_reserved_names()



# Generated at 2022-06-13 17:38:00.655210
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:38:07.404783
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # Testing with_ not in private attributes
    # FIXME: remove after with_ is not only deprecated but removed
    aobj = Task()
    aobj.__dict__['_attributes'].append({'name': 'loop'})
    result = get_reserved_names()
    assert 'with_' in result
    del aobj.__dict__['_attributes'][2]

    # Testing only public attributes
    result = get_reserved_names(include_private=False)

# Generated at 2022-06-13 17:38:09.026808
# Unit test for function get_reserved_names
def test_get_reserved_names():
    for attr in _RESERVED_NAMES:
        assert attr.startswith('_')