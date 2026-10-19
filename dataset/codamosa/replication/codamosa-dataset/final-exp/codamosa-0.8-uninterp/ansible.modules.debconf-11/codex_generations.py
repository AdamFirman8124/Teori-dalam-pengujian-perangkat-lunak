

# Generated at 2022-06-13 05:02:45.373705
# Unit test for function main
def test_main():
    # Test if we can successfully fake running a command
    def fake_run_command(cmd, data=None):
        if cmd.startswith('debconf-show'):
            return (0, '''tzdata tzdata/Areas select Africa
tzdata tzdata/Zones/Africa select Harare
tzdata tzdata/Zones/Brazil select Sao_Paulo
tzdata tzdata/Zones/Etc select UTC''', '')
        else:
            return (0, '', '')

    def fake_get_bin_path(name, required=False):
        return name

    def fake_fail_json(msg):
        raise Exception(msg)


# Generated at 2022-06-13 05:02:52.945417
# Unit test for function get_selections
def test_get_selections():
    from ansible.module_utils.basic import AnsibleModule
    import sys

    if sys.version_info.major < 3:
        from io import BytesIO as StringIO
    else:
        from io import StringIO

    module = AnsibleModule(
    )


# Generated at 2022-06-13 05:03:03.241568
# Unit test for function set_selection
def test_set_selection():
    import os, tempfile, shutil, re
    temp_dir = tempfile.mkdtemp()

# Generated at 2022-06-13 05:03:10.552375
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', required=True, aliases=['pkg']),
            question=dict(type='str', aliases=['selection', 'setting']),
            vtype=dict(type='str', choices=['boolean', 'error', 'multiselect', 'note', 'password', 'seen', 'select', 'string', 'text', 'title']),
            value=dict(type='str', aliases=['answer']),
            unseen=dict(type='bool', default=False),
        ),
        required_together=(['question', 'vtype', 'value'],),
        supports_check_mode=True,
    )
    module.params["name"] = "locales"

# Generated at 2022-06-13 05:03:15.635140
# Unit test for function main
def test_main():
    """Unit tests for function main"""
    out = mock.MagicMock()
    pkg = 'test'
    question = 'test-question'
    vtype = 'select'
    value = 'test-value'
    main(pkg, question, vtype, value, out)
    assert out.called


# Generated at 2022-06-13 05:03:23.326811
# Unit test for function get_selections
def test_get_selections():
    r_out = "* locales/default_environment_locale select en_US.UTF-8\n"
    r_out += "* locales/locales_to_be_generated multiselect en_US.UTF-8 UTF-8\n"
    r_out += "  tzdata   tzdata/Areas    select  North America\n"
    r_out += "  tzdata   tzdata/Zones/America select Los Angeles\n"
    r_out += "  tzdata   tzdata/Zones/Europe    select  Amsterdam\n"

    target_dict = {}
    target_dict["locales/default_environment_locale"] = "en_US.UTF-8"

# Generated at 2022-06-13 05:03:35.201522
# Unit test for function get_selections
def test_get_selections():
    import sys, os
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__))))
    from ansible.module_utils.ansible_release import __version__ as ANSIBLE_VERSION
    from ansible.module_utils.basic import *
    # Get the path of our module
    ansible_module_path = os.path.dirname(
        os.path.realpath(__file__)
    )
    # Use the built in ansible module to create the module object

# Generated at 2022-06-13 05:03:47.932953
# Unit test for function get_selections

# Generated at 2022-06-13 05:03:57.570193
# Unit test for function set_selection
def test_set_selection():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', required=True, aliases=['pkg']),
            question=dict(type='str', aliases=['selection', 'setting']),
            vtype=dict(type='str', choices=['boolean', 'error', 'multiselect', 'note', 'password', 'seen', 'select', 'string', 'text', 'title']),
            value=dict(type='str', aliases=['answer']),
            unseen=dict(type='bool', default=False),
        ),
        required_together=(['question', 'vtype', 'value'],),
        supports_check_mode=True,
    )

    # question, type, value

# Generated at 2022-06-13 05:04:09.186677
# Unit test for function set_selection
def test_set_selection():
    import StringIO
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', required=True, aliases=['pkg']),
            question=dict(type='str', aliases=['selection', 'setting']),
            vtype=dict(type='str', choices=['boolean', 'error', 'multiselect', 'note', 'password', 'seen', 'select', 'string', 'text', 'title']),
            value=dict(type='str', aliases=['answer']),
            unseen=dict(type='bool', default=False),
        ),
        required_together=(['question', 'vtype', 'value'],),
        supports_check_mode=True,
    )
    sio = StringIO.StringIO()

# Generated at 2022-06-13 05:04:27.687549
# Unit test for function get_selections
def test_get_selections():
    class DummyModule():
        def __init__(self):
            self.run_command_calls = []

        def run_command(self, commands, data=None):
            self.run_command_calls.append(commands)
            self.run_command_calls.append(data)
            return (0, "", "")

    obj = DummyModule()
    assert get_selections(obj, "tzdata") == {
        'tzdata/Areas': 'Etc',
        'tzdata/Zones/Etc': 'UTC'
    }
    assert obj.run_command_calls == [
        ['debconf-show', 'tzdata'],
        None
    ]



# Generated at 2022-06-13 05:04:40.571112
# Unit test for function set_selection
def test_set_selection():
    import os
    import tempfile
    import uuid

    # Create temporary folder
    module_test_folder = tempfile.mkdtemp()

    # Create temporary folder
    test_folder = os.path.join(module_test_folder, str(uuid.uuid4()))
    os.mkdir(test_folder)

    # Create temporary file
    test_file = os.path.join(test_folder, str(uuid.uuid4()))
    with open(test_file, 'w') as f:
        f.write("tests")

    # Create AnsibleModule for use in set_selection

# Generated at 2022-06-13 05:04:45.215993
# Unit test for function set_selection
def test_set_selection():
    class AnsMod:
        def get_bin_path(self, bin, required):
            return '/usr/bin/'+bin
        def run_command(self, cmd, data=None):
            return 0, '', ''
    mod = AnsMod()
    pkg = 'tzdata'
    question = 'tzdata/Areas'
    vtype = 'select'
    value = 'Etc'
    set_selection(mod, pkg, question, vtype, value, unseen=False)

# Generated at 2022-06-13 05:04:57.868186
# Unit test for function main
def test_main():
    import json
    import os
    import subprocess
    from ansible.module_utils.basic import AnsibleModule

    if not os.path.exists("debconf-show"):
        print("SKIP: debconf-show not found")
        return
    if not os.path.exists("debconf-set-selections"):
        print("SKIP: debconf-set-selections not found")
        return

    subprocess.check_call("apt-get install -y tzdata", shell=True)

    # Get previous values for test with tzdata
    prev = {}
    process = subprocess.Popen(
        ["debconf-show", "tzdata"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE
    )
    stdout_value, stderr

# Generated at 2022-06-13 05:05:09.003018
# Unit test for function set_selection
def test_set_selection():
    with patch('ansible.module_utils.basic.AnsibleModule.run_command') as run_mock:
        run_mock.side_effect = [
            (None, "", ""),
            (None, "", ""),
            (None, "", ""),
        ]


# Generated at 2022-06-13 05:05:10.571593
# Unit test for function get_selections
def test_get_selections():
    """
    get_selections() function should return boolean type.
    """
    assert isinstance(False, bool)

# Generated at 2022-06-13 05:05:19.126936
# Unit test for function main
def test_main():
    import sys

    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', required=True, aliases=['pkg']),
            question=dict(type='str', aliases=['selection', 'setting']),
            vtype=dict(type='str', choices=['boolean', 'error', 'multiselect', 'note', 'password', 'seen', 'select', 'string', 'text', 'title']),
            value=dict(type='str', aliases=['answer']),
            unseen=dict(type='bool', default=False),
        ),
        required_together=(['question', 'vtype', 'value'],),
        supports_check_mode=True,
    )
    pkg = module.params["name"]
    question = module.params["question"]

# Generated at 2022-06-13 05:05:21.024537
# Unit test for function main
def test_main():
    # Example to add test function here...
    # Tests here should pass when the module is run directly and fail when
    # the module is imported
    pass

# Generated at 2022-06-13 05:05:25.738533
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils import ansible_module_runner
    from ansible.module_utils.common._collections_compat import UserDict
    import ansible.module_utils.debconf
    # Sample values to be passed to ansible.module_utils.debconf.main
    # If you want to test these params check the file ansible.module_utils.debconf
    # to check how these values are used.
    #
    # values = {
    #     'params': {
    #         '_ansible_diff': False,
    #         '_ansible_module': 'debconf',
    #         '_ansible_module_name': 'ansible.module_utils.debconf',
    #         '_ansible_no_log': False,
    #

# Generated at 2022-06-13 05:05:36.037897
# Unit test for function get_selections
def test_get_selections():
    module = AnsibleModule(argument_spec=dict())
    module.run_command = MagicMock(return_value=('0', 'test_key: test_value', ''))
    test_return = get_selections(module, 'test_pkg')
    assert test_return == {'test_key': 'test_value'}
    module.fail_json = MagicMock()
    module.run_command = MagicMock(return_value=('1', '', 'test msg'))
    test_return = get_selections(module, 'test_pkg')
    module.fail_json.assert_called_with(msg='test msg')


# Generated at 2022-06-13 05:06:03.541782
# Unit test for function main
def test_main():
    import os
    import shutil
    import tempfile

    # create temporary directory
    tempdir = tempfile.mkdtemp()

    # copy debconf-get-selections to temporary directory
    shutil.copy('tests/files/test_debconf-get-selections', os.path.join(tempdir, 'test_debconf-get-selections'))

    # change to temporary directory
    os.chdir(tempdir)

    # create a fake ansible module
    class FakeModule(object):
        def __init__(self, params):
            self.params = params

        def get_bin_path(self, path, required):
            return os.path.join(tempdir, path)

        def run_command(self, command, data=None):
            command_string = ' '.join(command)

# Generated at 2022-06-13 05:06:16.732824
# Unit test for function set_selection
def test_set_selection():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', required=True, aliases=['pkg']),
            question=dict(type='str', aliases=['selection', 'setting']),
            vtype=dict(type='str', choices=['boolean', 'error', 'multiselect', 'note', 'password', 'seen', 'select', 'string', 'text', 'title']),
            value=dict(type='str', aliases=['answer']),
            unseen=dict(type='bool', default=False),
        ),
        required_together=(['question', 'vtype', 'value'],),
        supports_check_mode=True,
    )
    pkg = 'tzdata'
    id = 'tzdata/Areas'
    value = 'America'

# Generated at 2022-06-13 05:06:19.523423
# Unit test for function get_selections
def test_get_selections():
    # run a get_selections for a package that doesn't have any debconf selections
    assert get_selections(AnsibleModule, "lsb-release") == {}
    # run a get_selections for a package that definitely has debconf selections
    assert "locales/locales_to_be_generated" in get_selections(AnsibleModule, "locales")

# Generated at 2022-06-13 05:06:28.040888
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', required=True, aliases=['pkg']),
            question=dict(type='str', aliases=['selection', 'setting']),
            vtype=dict(type='str', choices=['boolean', 'error', 'multiselect', 'note', 'password', 'seen', 'select', 'string', 'text', 'title']),
            value=dict(type='str', aliases=['answer']),
            unseen=dict(type='bool', default=False),
        ),
        required_together=(['question', 'vtype', 'value'],),
        supports_check_mode=True,
    )

    # TODO: enable passing array of options and/or debconf file from get-selections dump
    pkg = module.params["name"]

# Generated at 2022-06-13 05:06:38.490094
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    if not basic._ANSIBLE_ARGS:
        args = sys.argv[:]
        basic._ANSIBLE_ARGS = basic.AnsibleParser(args, usage='{argv[0]} [options]',
                desc="Configure a .deb package using debconf-set-selections",
                default_vars=dict(
                    question='locales/locales_to_be_generated',
                    vtype='select',
                    value='en_US.UTF-8 UTF-8, fr_FR.UTF-8 UTF-8',
                ),
        ).parse_args()

    p = os.path.dirname(os.path.realpath(__file__))
    sys.path.append(p)

    main()

# Generated at 2022-06-13 05:06:52.383217
# Unit test for function set_selection
def test_set_selection():
    from ansible.module_utils.basic import AnsibleModule
    def run_command(cmd, data=None):
        if cmd[-1] == '/bin/debconf-set-selections' and data == 'tzdata tzdata/Areas select':
            return 123, 'out', 'err'
        return 0, 'out', 'err'

    module = AnsibleModule(
            argument_spec=dict(
                cmd=dict(type='str', required=True),
                data=dict(type='str')
            )
    )
    module.run_command = run_command

    rc, msg, e = set_selection(module, 'tzdata', 'tzdata/Areas', 'select', '', False)
    assert rc == 123
    assert msg == 'out'
    assert e == 'err'

# Generated at 2022-06-13 05:07:01.526022
# Unit test for function set_selection
def test_set_selection():
    from ansible.module_utils.six import b
    from ansible.module_utils.six.moves import StringIO
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils import common_koji
    from ansible.module_utils.debconf import set_selection


# Generated at 2022-06-13 05:07:07.949841
# Unit test for function get_selections
def test_get_selections():
    mock_module = MagicMock()
    mock_module.run_command.return_value = 0, '', ''
    mock_module.get_bin_path.return_value = '/usr/bin/debconf-show'
    mock_module.params = {'name': 'libc6'}

    assert get_selections(mock_module, 'libc6') == {}


# Generated at 2022-06-13 05:07:15.543066
# Unit test for function get_selections
def test_get_selections():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', required=True, aliases=['pkg']),
            question=dict(type='str', aliases=['selection', 'setting']),
            vtype=dict(type='str', choices=['boolean', 'error', 'multiselect', 'note', 'password', 'seen', 'select', 'string', 'text', 'title']),
            value=dict(type='str', aliases=['answer']),
            unseen=dict(type='bool', default=False),
        ),
        required_together=(['question', 'vtype', 'value'],),
        supports_check_mode=True,
    )

    # Test shell checking for locales (with different version)
    # sudo debconf-show locales
    # # Creo que la variable de

# Generated at 2022-06-13 05:07:27.640686
# Unit test for function set_selection
def test_set_selection():

    test_values = {
        'boolean': 'true',
        'error': 'This is a test error',
        'multiselect': 'a b',
        'note': 'This is a note',
        'password': 'This is a password',
        'select': 'a',
        'string': 'This is a string',
        'text': 'This is some text',
        'title': 'This is a title',
    }

    for key, value in test_values.items():
        rc, msg, e = set_selection(None, 'test', 'question', key, value, False)
        assert rc == 0
        assert e is None
        assert msg == b''

        rc, msg, e = set_selection(None, 'test', 'question', key, value, True)
        assert rc == 0

# Generated at 2022-06-13 05:08:25.697002
# Unit test for function set_selection
def test_set_selection():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', required=True, aliases=['pkg']),
            question=dict(type='str', aliases=['selection', 'setting']),
            vtype=dict(type='str', choices=['boolean', 'error', 'multiselect', 'note', 'password', 'seen', 'select', 'string', 'text', 'title']),
            value=dict(type='str', aliases=['answer']),
            unseen=dict(type='bool', default=False),
        ),
        required_together=(['question', 'vtype', 'value'],),
        supports_check_mode=True
    )

    def myruncommand(cmd, data=None):
        return (0, cmd+' '+data, '')

    module.run_command

# Generated at 2022-06-13 05:08:33.002197
# Unit test for function set_selection
def test_set_selection():
    import os
    import shutil

    test_root = tempfile.mkdtemp()
    test_bin_path = os.path.join(test_root, 'bin')
    test_lib_path = os.path.join(test_root, 'lib')
    test_debconf_path = '/usr/bin/debconf-utils'
    test_question = 'test-question'
    test_vtype = 'test-vtype'
    test_value = 'test-value'
    test_seen = False
    test_module = AnsibleModule(Check=True)
    # Create test debconf-set-selections
    os.makedirs(test_bin_path)
    test_debconf_set_selections_path = os.path.join(test_bin_path, 'debconf-set-selections')

# Generated at 2022-06-13 05:08:45.109817
# Unit test for function get_selections
def test_get_selections():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.debconf import get_selections
    import json
    import os
    filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data', 'debconf_selections.txt')

    # Debconf returns multiple lines:
    # * key: value
    # so we need to process it to simulate real life
    selections = {}
    with open(filepath, 'r') as f:
        for line in f.readlines():
            (key, value) = line.split(': ', 1)
            selections[key.strip('*').strip()] = value.strip()


# Generated at 2022-06-13 05:08:48.803562
# Unit test for function get_selections
def test_get_selections():
    selection = get_selections(module, 'tzdata')
    assert selection['tzdata/Areas'] == 'Europe'
    assert selection['tzdata/Zones/Europe'] == 'Berlin'
    assert selection['tzdata/Zones/UTC'] == 'true'

# Generated at 2022-06-13 05:08:53.762508
# Unit test for function get_selections
def test_get_selections():
    fake_module = AnsibleModule(argument_spec=dict())
    fake_module.get_bin_path = lambda x: x
    fake_module.run_command = lambda x: (0, "tzdata tzdata/Areas select Africa\ntzdata tzdata/Zones/Africa select Abidjan", "")
    assert get_selections(fake_module, "tzdata") == {u'tzdata/Zones/Africa': u'Abidjan', u'tzdata/Areas': u'Africa'}


# Generated at 2022-06-13 05:09:00.509042
# Unit test for function set_selection
def test_set_selection():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', required=True, aliases=['pkg']),
            question=dict(type='str', aliases=['selection', 'setting']),
            vtype=dict(type='str', choices=['boolean', 'error', 'multiselect', 'note', 'password', 'seen', 'select', 'string', 'text', 'title']),
            value=dict(type='str', aliases=['answer']),
            unseen=dict(type='bool', default=False),
        ),
        required_together=(['question', 'vtype', 'value'],),
        supports_check_mode=True,
    )

    pkg = 'locales'
    question = 'locales/default_environment_locale'
    vtype = 'select'
   

# Generated at 2022-06-13 05:09:11.360189
# Unit test for function set_selection
def test_set_selection():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', required=True, aliases=['pkg']),
            question=dict(type='str', aliases=['selection', 'setting']),
            vtype=dict(type='str', choices=['boolean', 'error', 'multiselect', 'note', 'password', 'seen', 'select', 'string', 'text', 'title']),
            value=dict(type='str', aliases=['answer']),
            unseen=dict(type='bool', default=False),
        ),
        required_together=(['question', 'vtype', 'value'],),
        supports_check_mode=True,
    )

    # Set selection with the TRUE value

# Generated at 2022-06-13 05:09:17.839987
# Unit test for function get_selections
def test_get_selections():
    import tempfile

    class FakeModule(object):
        def __init__(self):
            self.params = {}
            self._ansible_diff = False
            self.check_mode = True
            self.exit_json = self.exit_json_no_diff
            self.fail_json = self.fail_json_no_diff

        def exit_json_no_diff(self, **kwargs):
            self.kwargs = kwargs
            return None

        def fail_json_no_diff(self, **kwargs):
            self.fail = kwargs

        def run_command(self, cmd, data=None):
            self.rc = 0
            self.data = data
            self.cmd = cmd

# Generated at 2022-06-13 05:09:28.201140
# Unit test for function get_selections
def test_get_selections():
    import os
    from ansible.module_utils.basic import _load_params
    from ansible.module_utils.basic import _load_ansible_module
    from ansible.module_utils.basic import AnsibleFallbackNotFound
    module = _load_ansible_module('debconf', os.path.join(os.path.dirname(__file__), '../lib/ansible/modules/packaging/os/debconf.py'))
    params = _load_params(os.path.join(os.path.dirname(__file__), '../lib/ansible/modules/packaging/os/debconf.py'), ignore_params=['CHECKMODE', 'DIFFMODE', 'PLATFORM'])
    params.update(dict(name="locales"))

# Generated at 2022-06-13 05:09:29.094685
# Unit test for function get_selections
def test_get_selections():
    # Must be implemented
    return

# Generated at 2022-06-13 05:11:07.939976
# Unit test for function main
def test_main():
    class AnsibleModule:
        def __init__(self, some_dict):
            self.params = some_dict
            self.check_mode = False
            self._diff = False
            self.exit_json = lambda a, b: print("exit_json: a={}, b={}".format(a, b))
            self.fail_json = lambda msg: print("fail_json: {}".format(msg))

        def run_command(self, cmd, data=None):
            print("run cmd={}, data={}".format(cmd, data))
            if cmd == self.get_bin_path('debconf-show', True) + " foo":
                return 0, "foo bar", ""

# Generated at 2022-06-13 05:11:13.135109
# Unit test for function main
def test_main():
    # Check for no questions being returned for a package
    # Arrage
    class ModuleMock(object):
        def get_bin_path(self, path, opt_dirs=[]):
            return "/bin/bash"

        def run_command(self, cmd, data=None):
            return 0, "", ""
    module = ModuleMock()

    # Act
    prev = get_selections(module, "tzdata")

    # Assert
    assert prev == {}


# Generated at 2022-06-13 05:11:17.083801
# Unit test for function get_selections
def test_get_selections():
    import module_utils.debconf

    prev = module_utils.debconf.get_selections(None, 'tzdata')
    assert 'tzdata/Areas' in prev
    assert 'tzdata/Zones/Europe' in prev

# Generated at 2022-06-13 05:11:19.994674
# Unit test for function main
def test_main():
    # Test for main with idempotent operation
    # Test for main with non-idempotent operation
    pass

# Generated at 2022-06-13 05:11:27.080904
# Unit test for function set_selection
def test_set_selection():

    # Test with 'debconf-get-selections'
    def run_command(cmd, data=None):

        if cmd == ['debconf-get-selections']:
            return 0, "MySQL-server mysql-server/root_password password abc123", None

        elif cmd == ['debconf-get-selections', '-u']:
            return 0, "MySQL-server mysql-server/root_password seen false", None

        elif cmd == ['debconf-set-selections']:
            return 0, "", None

        elif cmd == ['debconf-set-selections', '-u']:
            return 0, "", None

        else:
            return 1, "", "Failed to run: %s" % cmd

    def fail_json(msg):
        raise Exception("Ansible module failed")

# Generated at 2022-06-13 05:11:37.309972
# Unit test for function main
def test_main():

    options = {'check_mode': False, 'diff': False}
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', required=True, aliases=['pkg']),
            question=dict(type='str', aliases=['selection', 'setting']),
            vtype=dict(type='str', choices=['boolean', 'error', 'multiselect', 'note', 'password', 'seen', 'select', 'string', 'text', 'title']),
            value=dict(type='str', aliases=['answer']),
            unseen=dict(type='bool'),
        ),
        supports_check_mode=True,
    )

# Generated at 2022-06-13 05:11:51.328520
# Unit test for function main
def test_main():
    args = dict(
        name='ntp',
        question='ntp/ntpservers',
        vtype='string',
        value='10.0.1.1'
    )

    module = AnsibleModule(argument_spec=args, supports_check_mode=True)

    set_selection = module.get_bin_path('debconf-set-selections', True)
    module.run_command = MagicMock(name="run_command")
    module.run_command.return_value = (0, '', '')

    rc, out, err = main()

    assert not rc
    # make sure we run a debconf-set-selections command with proper parameters

# Generated at 2022-06-13 05:11:51.658358
# Unit test for function get_selections
def test_get_selections():
    pass

# Generated at 2022-06-13 05:12:00.191946
# Unit test for function main
def test_main():
    import inspect
    import sys
    import os
    import json
    import mock

    argv = ['--force', '--diff', '--check']

# Generated at 2022-06-13 05:12:06.167602
# Unit test for function set_selection
def test_set_selection():
    # Create a mock module
    test_module = MagicMock()
    # Create a mock command
    test_cmd = [ 'debconf-set-selections' ]
    # Create a mock data to execute in the command
    test_data = 'locales locales/default_environment_locale select fr_FR.UTF-8'
    # Create a mock function to execute the command
    test_run = MagicMock()
    test_module.run_command = test_run
    # Create a mock return code
    test_rc = 0
    # Create a mock error message
    test_err = 'No error'
    # Create a mock output message
    test_out = 'No output'
    # Create a mock return value
    test_retval = ( test_rc, test_out, test_err )