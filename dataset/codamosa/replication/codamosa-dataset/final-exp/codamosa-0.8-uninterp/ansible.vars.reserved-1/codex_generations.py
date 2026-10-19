

# Generated at 2022-06-13 17:29:03.639710
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert 'action' in get_reserved_names()
    assert 'roles' in get_reserved_names()
    assert 'state' in get_reserved_names()
    assert 'vars' in get_reserved_names()
    assert 'block' in get_reserved_names()
    assert 'include' in get_reserved_names()
    assert 'tasks' in get_reserved_names()
    assert 'become' in get_reserved_names()
    assert 'role_path' in get_reserved_names()
    assert 'gather_facts' in get_reserved_names()
    assert 'pre_tasks' in get_reserved_names()
    assert 'post_tasks' in get_reserved_names()

# Generated at 2022-06-13 17:29:10.144982
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert 'become' in get_reserved_names()
    assert 'gather_facts' in get_reserved_names()
    assert 'environment' in get_reserved_names()
    assert 'include' in get_reserved_names()
    assert 'import_role' in get_reserved_names()
    assert 'include_role' in get_reserved_names()
    assert 'private' not in get_reserved_names(False)
    assert 'vars_files' in get_reserved_names()

# Generated at 2022-06-13 17:29:15.865137
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved = get_reserved_names(include_private=False)
    assert 'roles' in reserved
    assert 'tasks' in reserved
    assert 'block' in reserved
    assert 'blockrescue' in reserved
    assert 'blockalways' in reserved
    assert 'prompt' in reserved

    reserved = get_reserved_names(include_private=True)
    assert 'deprecate_as' in reserved
    assert 'import_role' in reserved
    assert 'loop' in reserved

    assert is_reserved_name('roles') is True
    assert is_reserved_name('foobar') is False

# Generated at 2022-06-13 17:29:25.776947
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' function get_reserved_names has a unit test '''

# Generated at 2022-06-13 17:29:29.757679
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert 'action' in get_reserved_names()
    assert 'private' in get_reserved_names(include_private=False)

# Generated at 2022-06-13 17:29:38.487821
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:29:49.264556
# Unit test for function get_reserved_names
def test_get_reserved_names():
    private = get_reserved_names(False)
    private_and_public = get_reserved_names(True)
    private_set = set(private)
    private_and_public_set = set(private_and_public)
    assert 'hosts' in private_set
    assert 'hosts' in private_and_public_set
    assert 'roles' in private_set
    assert 'roles' in private_and_public_set
    assert 'vars' in private_set
    assert 'vars' in private_and_public_set
    assert 'tasks' in private_set
    assert 'tasks' in private_and_public_set
    assert 'block' in private_set
    assert 'block' in private_and_public_set
    assert 'include' in private_set

# Generated at 2022-06-13 17:29:59.418430
# Unit test for function get_reserved_names
def test_get_reserved_names():
    result = get_reserved_names()
    assert isinstance(result, set)
    assert 'connection' in result
    assert 'vars' in result
    assert 'action' in result
    assert 'local_action' in result
    assert 'include' in result
    assert 'include_role' in result
    # FIXME: remove when with_ is removed from core
    assert 'with_' in result
    assert len(result) == 12

    result = get_reserved_names(include_private=False)
    assert isinstance(result, set)
    assert 'connection' in result
    assert 'vars' in result
    assert 'action' in result
    assert 'local_action' in result
    assert 'include' in result
    assert 'include_role' in result
    # FIXME: remove when with_ is removed from core

# Generated at 2022-06-13 17:30:07.726020
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:30:11.731723
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert isinstance(_RESERVED_NAMES, frozenset)
    assert 'roles' in _RESERVED_NAMES
    assert 'roles' in get_reserved_names()
    assert 'geerlingguy.firewall' in get_reserved_names(include_private=True)
    assert 'geerlingguy.firewall' not in get_reserved_names(include_private=False)


# Generated at 2022-06-13 17:30:36.895105
# Unit test for function get_reserved_names
def test_get_reserved_names():
    from nose.tools import assert_equal

    # This will return a set of names
    reserved_names = get_reserved_names()

    # We know all the attributes on the top level Play object
    public = ['playbook', 'connection', 'strategy', 'remote_user',
              'any_errors_fatal', 'poll', 'sudo', 'sudo_user', 'transport',
              'vars_prompt', 'vars_files', 'vars_prompt_once', 'gather_facts',
              'gather_subset', 'gather_timeout', 'environment', 'no_log',
              'roles', 'post_tasks', 'pre_tasks', 'handlers', 'tags', 'flush_cache',
              'sudo_flags']
    # Private are all attributes not in the public list

# Generated at 2022-06-13 17:30:47.005471
# Unit test for function get_reserved_names
def test_get_reserved_names():
    from ansible.parsing.yaml.objects import AnsibleUnicode

    test_private = get_reserved_names(include_private=True)
    test_public = get_reserved_names(include_private=False)

    # test_private and test_public should be type set
    assert isinstance(test_private, set)
    assert isinstance(test_public, set)

    # ensure that test_private has more elements than test_public
    assert len(test_private) > len(test_public)

    # test_private and test_public should be composed of only type AnsibleUnicode
    for t in test_private:
        assert isinstance(t, AnsibleUnicode)
    for t in test_public:
        assert isinstance(t, AnsibleUnicode)

    # test_private

# Generated at 2022-06-13 17:30:56.844531
# Unit test for function get_reserved_names
def test_get_reserved_names():

    # test 1, simple compare
    standard = get_reserved_names()
    modified = get_reserved_names(include_private=False)
    if len(modified) >= len(standard):
        raise AssertionError("Expected modified list to contain less elements than standard, got %d <= %d" % (len(modified), len(standard)))

    # test 2, string compare
    if str(modified) == str(standard):
        raise AssertionError("Expected modified list to differ from standard, got '%s' == '%s'" % (modified, standard))

    # test 3, is_reserved_name function

# Generated at 2022-06-13 17:31:06.364268
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:31:08.053482
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved = get_reserved_names()
    assert 'name' in reserved



# Generated at 2022-06-13 17:31:10.129618
# Unit test for function get_reserved_names
def test_get_reserved_names():
    print(get_reserved_names())
    print(get_reserved_names(include_private=False))


# Generated at 2022-06-13 17:31:19.508340
# Unit test for function get_reserved_names
def test_get_reserved_names():
    class CheckReservedNames:
        def __init__(self):
            self.reserved_play = ['playbook', 'play', 'hosts', 'remote_user', 'connection', 'port', 'become',
                                  'become_method', 'become_user', 'become_ask_pass', 'gather_facts', 'vars_prompt',
                                  'vars_files', 'vault_password_files', 'tags', 'skip_tags', 'check', 'any_errors_fatal',
                                  'max_fail_percentage', 'roles', 'tasks', 'post_tasks', 'pre_tasks',
                                  'handlers', 'meta', 'module_defaults', 'include', 'include_role', 'name',
                                  'blocks', 'block']

# Generated at 2022-06-13 17:31:21.986606
# Unit test for function get_reserved_names
def test_get_reserved_names():
    # pylint: disable=unused-variable
    assert isinstance(get_reserved_names(), set)
    assert 'roles' in get_reserved_names()


# Generated at 2022-06-13 17:31:29.759593
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert set(get_reserved_names()) == set(get_reserved_names(include_private=False)) == set(['any_errors_fatal', 'connection', 'gather_facts', 'delegate_to', 'environment', 'post_tasks', 'register', 'roles', 'hosts', 'tasks', 'sudo', 'sudo_user', 'vars_files', 'vars_prompt', 'vars', 'when', 'become', 'become_user', 'extra_vars', 'tags', 'pre_tasks', 'run_once', 'include', 'no_log', 'serial', 'failed_when', 'ignore_errors', 'deprecated', 'until', 'retries', 'delay', 'poll', 'notify', 'local_action', 'action'])

# Generated at 2022-06-13 17:31:32.302215
# Unit test for function get_reserved_names
def test_get_reserved_names():

    assert 'local_action' in _RESERVED_NAMES
    assert 'with_' in _RESERVED_NAMES

# Generated at 2022-06-13 17:31:48.454316
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert set(('roles', 'tasks', 'handlers', 'vars', 'meta', 'block', 'pre_tasks', 'post_tasks')) == get_reserved_names(False)

# Generated at 2022-06-13 17:31:55.170307
# Unit test for function get_reserved_names
def test_get_reserved_names():
    names = frozenset(get_reserved_names(include_private=False))

# Generated at 2022-06-13 17:32:01.074547
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert isinstance(get_reserved_names(), set)
    assert isinstance(get_reserved_names(include_private=False), set)

    private = set(['any_errors_fatal', 'become', 'become_method', 'become_user', 'connection', 'delegate_to', 'first_available_file', 'local_action', 'loop', 'name', 'others', 'pause', 'run_once', 'serial'])

# Generated at 2022-06-13 17:32:04.652426
# Unit test for function get_reserved_names
def test_get_reserved_names():
    result = get_reserved_names()
    assert len(result) == 35
    assert 'name' in result

    result = get_reserved_names(include_private=False)
    assert len(result) == 28
    assert 'name' in result

# Generated at 2022-06-13 17:32:06.526951
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' this function tests the safe_eval.get_reserved_names function '''

    testclass = get_reserved_names()

    assert 'hosts' in testclass

# Generated at 2022-06-13 17:32:07.211497
# Unit test for function get_reserved_names
def test_get_reserved_names():
   assert get_reserved_names() == _RESERVED_NAMES

# Generated at 2022-06-13 17:32:08.253005
# Unit test for function get_reserved_names
def test_get_reserved_names():
    get_reserved_names(include_private=True).difference(get_reserved_names(include_private=False))



# Generated at 2022-06-13 17:32:11.704168
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert 'name' in get_reserved_names(include_private=False)
    assert 'any_errors_fatal' in get_reserved_names(include_private=False)
    assert 'run_once' in get_reserved_names(include_private=False)

    assert 'action' in get_reserved_names()
    assert 'delegate_to' in get_reserved_names()
    assert 'local_action' in get_reserved_names()
    assert 'loop' in get_reserved_names()
    assert 'name' in get_reserved_names()



# Generated at 2022-06-13 17:32:20.003386
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved_names = set(get_reserved_names())
    # list of reserved names returned should be greater than 0 (obviously)
    assert len(reserved_names) > 0

    # action is explicitly added to reserved names
    assert 'action' in reserved_names

    # implicitly added with_ and local_action should be in reserved names
    assert 'with_' in reserved_names
    assert 'local_action' in reserved_names

    # test that a private attribute is defined in reserved names
    assert 'loop' in reserved_names


# Generated at 2022-06-13 17:32:27.860433
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:33:03.108131
# Unit test for function get_reserved_names
def test_get_reserved_names():

    reserved_names_public_only = ['any_errors_fatal',
                                  'become',
                                  'become_method',
                                  'become_user',
                                  'connection',
                                  'delegate_to',
                                  'gather_facts',
                                  'gather_subset',
                                  'groups',
                                  'hosts',
                                  'ignore_errors',
                                  'include',
                                  'include_role',
                                  'include_tasks',
                                  'no_log',
                                  'notify',
                                  'sudo',
                                  'sudo_user',
                                  'tags',
                                  'tasks',
                                  'vars',
                                  'vars_files']


# Generated at 2022-06-13 17:33:07.932371
# Unit test for function get_reserved_names
def test_get_reserved_names():
    names = get_reserved_names()

    # action is a required attribute of a task
    assert 'action' in names
    # private attributes are included by default
    assert '_role_name' in names

    names = get_reserved_names(include_private=False)
    # private attributes are not included
    assert '_role_name' not in names
    # action is a required attribute of a task
    assert 'action' in names



# Generated at 2022-06-13 17:33:10.318807
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved_names = get_reserved_names()
    assert 'name' in reserved_names
    assert 'action' in reserved_names

# Generated at 2022-06-13 17:33:11.851006
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved_names = get_reserved_names()
    assert 'action' in reserved_names



# Generated at 2022-06-13 17:33:19.531227
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:33:27.512360
# Unit test for function get_reserved_names
def test_get_reserved_names():
    res = get_reserved_names()
    assert 'name' in res
    assert 'action' in res
    assert 'local_action' in res
    assert 'loop' in res
    assert 'with_' in res
    assert 'include_role' in res
    assert 'include' in res
    assert 'register' in res
    assert 'roles' in res

    assert 'private' not in res

# Generated at 2022-06-13 17:33:32.769040
# Unit test for function get_reserved_names
def test_get_reserved_names():
    '''
    This function tests the get_reserved_names function.
    '''

    test_list = ["any_errors_fatal", "connection", "delegate_to", "gather_facts", "ignore_errors", "local_actions",
                 "notify", "register", "remote_user", "roles", "serial", "tags"]
    assert set(get_reserved_names()) == set(test_list)


# Generated at 2022-06-13 17:33:35.342304
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved = get_reserved_names()
    print(reserved)
    assert type(reserved) == set
    assert 'roles' in reserved
    assert 'when' in reserved


# Generated at 2022-06-13 17:33:39.561651
# Unit test for function get_reserved_names
def test_get_reserved_names():

    for reserved in _RESERVED_NAMES:
        assert reserved in get_reserved_names(include_private=False), \
            "%s not in public reserved names list" % reserved
        assert reserved in get_reserved_names(include_private=True), \
            "%s not in public+private reserved names list" % reserved

# Generated at 2022-06-13 17:33:41.997894
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert 'include' in get_reserved_names()
    assert 'include_role' in get_reserved_names()

# Generated at 2022-06-13 17:34:45.329803
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert len(_RESERVED_NAMES) > 20
    assert 'name' in _RESERVED_NAMES
    assert 'roles' in _RESERVED_NAMES
    assert 'dependencies' in _RESERVED_NAMES     # private
    assert 'vars_files' in _RESERVED_NAMES
    assert 'gather_facts' in _RESERVED_NAMES
    assert 'connection' in _RESERVED_NAMES
    assert 'remote_user' in _RESERVED_NAMES
    assert 'sudo' in _RESERVED_NAMES
    assert 'sudo_user' in _RESERVED_NAMES
    assert 'become' in _RESERVED_NAMES
    assert 'become_user' in _RESERVED_NAMES


# Generated at 2022-06-13 17:34:47.528908
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert isinstance(get_reserved_names(), set)
    assert isinstance(get_reserved_names(include_private=True), set)

# Generated at 2022-06-13 17:34:58.211295
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:35:07.381941
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved_names = get_reserved_names(include_private=True)

# Generated at 2022-06-13 17:35:16.051105
# Unit test for function get_reserved_names
def test_get_reserved_names():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.parsing.yaml.loader import AnsibleLoader
    from io import StringIO
    from ansible.compat.tests import unittest

    class TestPlay(unittest.TestCase):
        def setUp(self):
            # clear Ansible defaults
            RoleDefinition._defaults = {}
            Play.load = {}

            self.loader = AnsibleLoader

            # init loader with YAML
            self.playbook_yaml = """
            - hosts: all
              roles:
                - role: foobar
                  bar: "{{ foo }}"
                  foo: "{{ bar }}"
              tasks:
                - debug: msg="{{ foo }}"
                - debug: msg="{{ bar }}"
            """
            self.playbook = StringIO

# Generated at 2022-06-13 17:35:20.829536
# Unit test for function get_reserved_names
def test_get_reserved_names():
    privates = get_reserved_names(include_private=False)
    publics = get_reserved_names(include_private=True)
    assert('roles' in publics)
    assert('connection' in publics)
    assert('roles' in privates)
    assert('connection' in privates)
    assert(len(publics) < len(privates))

# Generated at 2022-06-13 17:35:28.310252
# Unit test for function get_reserved_names

# Generated at 2022-06-13 17:35:35.537780
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved_names = get_reserved_names()

    # Check that some common names are included
    assert 'vars' in reserved_names
    assert 'roles' in reserved_names

    # Check that some uncommon names are included
    assert 'raw' in reserved_names
    assert 'block' in reserved_names
    assert 'deprecate' in reserved_names

    # Check that some uncommon names are NOT included
    assert 'async' not in reserved_names
    assert 'sudo' not in reserved_names
    assert 'environment' not in reserved_names


# Generated at 2022-06-13 17:35:45.181402
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reverse_order = list(reversed(get_reserved_names()))

# Generated at 2022-06-13 17:35:45.955244
# Unit test for function get_reserved_names
def test_get_reserved_names():
    result = get_reserved_names()
    assert result

# Generated at 2022-06-13 17:37:36.306291
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved = get_reserved_names()
    assert 'name' in reserved


# Generated at 2022-06-13 17:37:40.111618
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved = get_reserved_names()
    assert type(reserved) is set
    assert len(reserved) > 0
    assert 'action' in reserved
    assert 'local_action' in reserved  # implicit with action
    assert 'loop' not in reserved  # deprecated in favor of with_
    assert 'with_' in reserved

# Generated at 2022-06-13 17:37:41.634210
# Unit test for function get_reserved_names
def test_get_reserved_names():
    result = get_reserved_names()
    assert isinstance(result, set)

# Generated at 2022-06-13 17:37:48.726231
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

# Generated at 2022-06-13 17:37:57.750350
# Unit test for function get_reserved_names
def test_get_reserved_names():

    # checks if a list of names are in the list of reserved names from the function
    def _check_reserved_names(names):
        for name in names:
            assert(name in _RESERVED_NAMES)

    # list of names to test
    test_names = [
        'hosts',
        'name',
        'gather_facts',
        'connection',
        'serial',
        'sudo',
    ]

    # list of names that must not be found in reserved names as they are private
    private_exp_names = [
        '_load_name',
        '_role_name',
        '_role_path',
        '_parent',
        '_elements',
        '_block',
        '_role',
    ]

    # test that all names from the 'test_names' list

# Generated at 2022-06-13 17:38:07.193052
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved = get_reserved_names()
    assert 'name' in reserved
    assert 'any_errors_fatal' in reserved
    assert 'any_errors_fatal' in reserved
    assert 'ignore_errors' in reserved
    assert 'listen' in reserved
    assert 'hosts' in reserved
    assert 'gather_facts' in reserved
    assert 'roles' in reserved
    assert 'vars' in reserved
    assert 'vars_files' in reserved
    assert 'tasks' in reserved
    assert 'post_tasks' in reserved
    assert 'pre_tasks' in reserved
    assert 'handlers' in reserved
    assert 'tags' in reserved
    assert 'when' in reserved
    assert 'defaults_file' in reserved
    assert 'connection' in reserved
    assert 'remote_user' in reserved
   

# Generated at 2022-06-13 17:38:09.428561
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved = get_reserved_names()
    assert isinstance(reserved, set)
    assert 'hosts' in reserved
    assert 'tasks' in reserved



# Generated at 2022-06-13 17:38:18.594880
# Unit test for function get_reserved_names
def test_get_reserved_names():
    ''' parametrize this function to return the set of reserved names
        by default it will return the publically facing ones '''


# Generated at 2022-06-13 17:38:28.008031
# Unit test for function get_reserved_names
def test_get_reserved_names():
    assert (frozenset(['name']).issubset(get_reserved_names()))
    assert (frozenset(['static']).issubset(get_reserved_names()))
    assert (frozenset(['roles']).issubset(get_reserved_names()))
    assert (frozenset(['gather_facts']).issubset(get_reserved_names()))
    assert (frozenset(['any_errors_fatal']).issubset(get_reserved_names()))
    assert (frozenset(['run_once']).issubset(get_reserved_names()))
    assert (frozenset(['hosts']).issubset(get_reserved_names()))



# Generated at 2022-06-13 17:38:36.840569
# Unit test for function get_reserved_names
def test_get_reserved_names():
    reserved_names = get_reserved_names()
    assert 'playbook' in reserved_names
    assert 'roles' in reserved_names
    assert 'private_role_vars' in reserved_names
    assert 'become' in reserved_names
    assert 'become_method' in reserved_names
    assert 'become_user' in reserved_names
    assert 'connection' in reserved_names
    assert 'user' in reserved_names
    assert 'delegate_to' in reserved_names
    assert 'environment' in reserved_names
    assert 'force_handlers' in reserved_names
    assert 'gather_facts' in reserved_names
    assert 'priority' in reserved_names
    assert 'remote_user' in reserved_names
    assert 'serial' in reserved_names
    assert 'su' in reserved_names
   