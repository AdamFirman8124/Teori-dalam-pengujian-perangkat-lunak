

# Generated at 2022-06-13 05:02:37.203047
# Unit test for function set_selection
def test_set_selection():
    with tempfile.NamedTemporaryFile() as f:
        # Create config file
        f.write(b'debconf debconf/frontend select noninteractive\n')
        f.flush()
        # Append test for the set_selection function
        cmd = [setsel]
        if unseen:
            cmd.append('-u')
        data = ' '.join([pkg, question, vtype, value])
        rc, out, err = module.run_command(cmd, data=data)
        assert rc, err
        assert out, err


# Generated at 2022-06-13 05:02:45.486880
# Unit test for function main
def test_main():
    test_name = 'gitlab-ce'
    test_question = 'gitlab-ce/external-url'
    test_vtype = 'string'
    test_value = 'http://gitlab.example.com'
    test_unseen = 'False'

    # Create a module instance

# Generated at 2022-06-13 05:02:46.014030
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:02:51.884600
# Unit test for function set_selection
def test_set_selection():
    """
    Test output of:
    debconf-set-selections <(echo 'postfix postfix/main_mailer_type string "Internet Site"')
    """
    setsel = "/usr/bin/debconf-set-selections"
    cmd = [setsel]
    pkg = 'postfix'
    question = 'postfix/main_mailer_type'
    vtype = 'select'
    value = 'Internet Site'
    data = ' '.join((pkg, question, vtype, value))
    rc = set_selection('', cmd, data)

    assert rc == 0



# Generated at 2022-06-13 05:02:57.809014
# Unit test for function get_selections
def test_get_selections():
    test_module = AnsibleModule(argument_spec={}, check_invalid_arguments=False)
    test_module.get_bin_path=lambda path, required=True: path
    test_module.run_command=lambda cmd, data=None: (0, "key1: value1\nkey2: value2", '')
    assert get_selections(test_module, 'pkg') == {'key1': 'value1', 'key2': 'value2'}
    test_module.run_command = lambda cmd, data=None: (1, '', 'error')
    test_module.fail_json = lambda msg: 'debconf-show failed with error'
    assert get_selections(test_module, 'pkg') == 'debconf-show failed with error'

# Generated at 2022-06-13 05:03:06.959304
# Unit test for function main
def test_main():
    import sys
    import os
    import re
    import subprocess
    import shutil
    import tempfile

    def set_selection(pkg, question, vtype, value):
        setsel = ['debconf-set-selections']
        if vtype == 'boolean':
            if value == 'True':
                value = 'true'
            elif value == 'False':
                value = 'false'
        data = ' '.join([pkg, question, vtype, value])

        rc, msg, e = module.run_command(setsel, data=data)
        if rc:
            module.fail_json(msg=e)

        return msg

    def get_selections_data(pkg):
        cmd = ['debconf-show', pkg]

# Generated at 2022-06-13 05:03:19.833056
# Unit test for function set_selection
def test_set_selection():

    def fake_run_command(cmd, data=None):
        assert cmd == [setsel, "-u"]
        assert data == "fakepkg fakequestion faketype fakevalue"
        return (0, "", "")

    fake_module = AnsibleModule(argument_spec=dict(), supports_check_mode=True, check_invalid_arguments=True)
    fake_module.run_command = fake_run_command
    fake_module.get_bin_path = lambda x: x

    setsel = 'debconf-set-selections'
    pkg = 'fakepkg'
    question = 'fakequestion'
    vtype = 'faketype'
    value = 'fakevalue'
    unseen = True


# Generated at 2022-06-13 05:03:25.313306
# Unit test for function set_selection
def test_set_selection():
    class MockModule(object):
        def __init__(self, msg, changed):
            self._changed = changed
            self._msg = msg
            self._return_value = (1, '', 'stub')

        def run_command(self, cmd, data=''):
            if self._msg and not self._changed:
                return (0, '', self._msg)
            else:
                return self._return_value

        def get_bin_path(self, cmd, required=False):
            return cmd

        def fail_json(self, msg):
            self._return_value = (1, '', msg)

        def check_mode(self):
            return self._changed

    pkg = "ansible-debconf-test-pkg"
    question = "ansible-debconf-test-question"

# Generated at 2022-06-13 05:03:37.586194
# Unit test for function get_selections
def test_get_selections():
    def run_module(*args, **kwargs):
        module_args = kwargs.copy()
        if 'module_defaults' in module_args:
            del module_args['module_defaults']


# Generated at 2022-06-13 05:03:49.549870
# Unit test for function get_selections
def test_get_selections():
    out = ('* locales/default_environment_locale   select  en_GB.UTF-8',
           'locales/locales_to_be_generated         multiselect  en_GB.UTF-8 UTF-8')
    assert(get_selections(None, "locales") == {'locales/locales_to_be_generated': 'en_GB.UTF-8 UTF-8',
                                               'locales/default_environment_locale': 'en_GB.UTF-8'})

# Generated at 2022-06-13 05:04:03.326026
# Unit test for function main
def test_main():
    module_args = {
        "name": "tzdata",
        "question": "tzdata/Areas",
        "vtype": "multiselect",
        "value": "Europe",
        "unseen": True
    }
    module = AnsibleModule(argument_spec=module_args)
    assert main() is not None

# Generated at 2022-06-13 05:04:13.723169
# Unit test for function main
def test_main():

    test_values = {
        "question": "rootpw",
        "vtype": "password",
        "value": "test",
        "unseen": "false"
    }

# Generated at 2022-06-13 05:04:15.722764
# Unit test for function get_selections
def test_get_selections():
    list_test = get_selections("tzdata")
    assert "tzdata/Areas" in list_test

# Generated at 2022-06-13 05:04:25.880508
# Unit test for function main
def test_main():
    import sys

    class ExitJsonException(Exception):
        pass
    class FailJsonException(Exception):
        pass

    class ModuleExitJson(object):
        def __init__(self, module, **kwargs):
            self.kwargs = kwargs
            self.module = module
        def exit_json(self, **kwargs):
            self.module.exit_json(**kwargs)

        def exit_json(self, *args, **kwargs):
            if 'changed' not in kwargs:
                kwargs['changed'] = False
            raise ExitJsonException(kwargs)

        def fail_json(self, *args, **kwargs):
            kwargs['failed'] = True
            raise FailJsonException(kwargs)

    # we show a message when something happens

# Generated at 2022-06-13 05:04:39.514908
# Unit test for function set_selection
def test_set_selection():
    # Python 3 test cases
    selection_data = 'test_package setting string test_value'
    data = selection_data.encode('utf-8')
    test_module = MockModule()
    test_module._ansible_version = '3.3.0'
    test_module.run_command = Mock(return_value=(0, '', ''))
    rc, msg, e = set_selection(test_module, 'test_package', 'setting', 'string', 'test_value', False)
    assert rc == 0
    test_module.run_command.assert_called_once_with(['/usr/bin/debconf-set-selections'], data=data)
    # Python 2 test cases
    selection_data = 'test_package setting string test_value'

# Generated at 2022-06-13 05:04:41.805170
# Unit test for function main
def test_main():
    module = importlib.import_module('library.debconf')
    module.main()


# Generated at 2022-06-13 05:04:47.695784
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

# Generated at 2022-06-13 05:04:57.314514
# Unit test for function main
def test_main():
    try:
        import importlib
        importlib.reload(get_selections)
        importlib.reload(set_selection)
    except:
        import imp
        globals()['get_selections'] = imp.load_source('get_selections', 'get_selections')
        globals()['set_selection'] = imp.load_source('set_selection', 'set_selection')
    args = dict(
        name="tzdata",
        question="clock",
        vtype="select",
        value="America/New_York",
        unseen=False,
    )
    main()

# Generated at 2022-06-13 05:05:00.439618
# Unit test for function set_selection
def test_set_selection():
    import os

    os.system("./ansible-config dump --only-changed")
    set_selection(AnsibleModule, "tad", "tad", "tad", "tad", True)

test_set_selection()

# Generated at 2022-06-13 05:05:11.133042
# Unit test for function get_selections
def test_get_selections():
    import os
    from ansible.module_utils.basic import AnsibleModule

    # stub our module
    test_module = AnsibleModule(argument_spec={'name': {'type': 'str', 'required': True, 'aliases': ['pkg']}})

    # stub only the run_command function and give it some return values that we expect debconf-show to return

# Generated at 2022-06-13 05:05:39.118555
# Unit test for function get_selections
def test_get_selections():
    import os
    import sys
    import re
    import pytest
    from mock import Mock, call
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes, to_text
    sys.modules['debconf'] = Mock()
    sys.modules['debconf_utils'] = Mock()

    mymodule = imp.load_source('ansible.module_utils.debconf', '../../action_plugins/modules/debconf.py')


# Generated at 2022-06-13 05:05:42.823606
# Unit test for function get_selections
def test_get_selections():
    import mock

    # Mock module parameters
    module = mock.Mock()
    module.run_command.return_value = 0, "mock output", ""

    # Mock module parameters
    module.params = {}
    module.params['name'] = "mock_package"

    # Call function get_selections()
    result = get_selections(module, module.params['name'])

    # Validate values
    assert(result == {'mock_selection': 'mock_value'})

# Generated at 2022-06-13 05:05:45.176774
# Unit test for function set_selection
def test_set_selection():
    assert set_selection('debconf', 'pkg', 'question', 'string', 'value', False) == [pkg, question, string, value]

# Generated at 2022-06-13 05:05:53.574775
# Unit test for function main
def test_main():
    import sys
    import inspect
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.basic import AnsibleModule

    module = basic.AnsibleModule(name='debconf', argument_spec=dict(name=dict(type='str', required=True, aliases=['pkg']),question=dict(type='str', aliases=['selection', 'setting']),vtype=dict(type='str', choices=['boolean', 'error', 'multiselect', 'note', 'password', 'seen', 'select', 'string', 'text', 'title']),value=dict(type='str', aliases=['answer']),unseen=dict(type='bool', default=False)))
    setattr(module, '_ansible_no_log', True)
    setattr

# Generated at 2022-06-13 05:06:03.914313
# Unit test for function set_selection
def test_set_selection():
    '''set_selection function test'''
    from ansible.module_utils.basic import AnsibleModule
    import os
    import re

    # Create module object
    module = AnsibleModule(argument_spec={})

    # Get random package name
    pkg = re.sub('[^A-Za-z0-9]+', '', os.urandom(10).encode('hex'))

    # Example debconf-set-selection
    debconf_command = 'debconf-set-selections'
    debconf_command_data = pkg + ' bogus-package/bogus-setting select bogus-value'

    # Test missing parameter values
    rc, msg, e = set_selection(module, pkg, 'bogus-package/bogus-setting', None, None, False)

# Generated at 2022-06-13 05:06:16.051004
# Unit test for function get_selections
def test_get_selections():
    from ansible.module_utils.basic import AnsibleModule
    mod = AnsibleModule(argument_spec=dict(
        name=dict(type='str', required=True, aliases=['pkg']),
        question=dict(type='str', aliases=['selection', 'setting']),
        vtype=dict(type='str', choices=['boolean', 'error', 'multiselect', 'note', 'password', 'select', 'string', 'text', 'title']),
        value=dict(type='str', aliases=['answer']),
    ))
    selections = get_selections(mod, 'locales')
    assert len(dict) == 4
    assert selections['locales/default_environment_locale'] == 'en_US.UTF-8'

# Generated at 2022-06-13 05:06:23.936401
# Unit test for function get_selections
def test_get_selections():
    import mock

    test_module = mock.Mock()

    test_module.run_command.return_value = (0,
        '* tzdata/Areas: Europe\n'
        '* tzdata/Zones/Europe: Madrid\n',
        '')

    expected = {
        'tzdata/Areas': 'Europe',
        'tzdata/Zones/Europe': 'Madrid',
    }
    result = get_selections(test_module, 'tzdata')
    assert expected == result


# Generated at 2022-06-13 05:06:29.205344
# Unit test for function get_selections
def test_get_selections():
    import debconf
    db = debconf.Debconf()
    db.set('debconf.test.selections', 'debconf.test.selections', 'boolean', 'true')
    selections = get_selections(db, 'debconf.test.selections')
    assert selections['debconf.test.selections'] == 'true'

# Generated at 2022-06-13 05:06:34.609653
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
    main()

# Generated at 2022-06-13 05:06:42.753335
# Unit test for function set_selection
def test_set_selection():
    import os
    import tempfile
    from subprocess import PIPE
    from ansible.module_utils.basic import AnsibleModule

    def test_failure(in_data=None, rc=1, stderr=''):
        tmp = tempfile.NamedTemporaryFile()
        tmp.write(in_data)
        tmp.seek(0)
        module = AnsibleModule(argument_spec={})
        module.params = { 'data': tmp.name }
        test = set_selection(module, 'test_package', 'test_question', 'test_type', 'test_value', False)
        tmp.close()
        assert test[0] == rc
        assert test[2] == stderr
        if rc == 0:
            assert test[1] == ''


# Generated at 2022-06-13 05:07:21.474750
# Unit test for function set_selection
def test_set_selection():
    return 0

# Generated at 2022-06-13 05:07:32.932076
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

# Generated at 2022-06-13 05:07:41.038047
# Unit test for function set_selection
def test_set_selection():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={'question':dict(), 'vtype':dict(), 'value':dict()})
    rc, msg, e = set_selection(module, None, None, None, None, True)
    assert rc == 0, "incorrect exit code"
    assert not e, "error message returned"
    assert msg, "no output returned"
    assert 'debconf-set-selections' in msg, "incorrect command used"

# Generated at 2022-06-13 05:07:52.683037
# Unit test for function main
def test_main():
    # run_command, main
    sub_mock = Mock()
    sub_mock.run_command = MagicMock()
    sub_mock.run_command.return_value = (0, '', '')

    main_mock = Mock()
    main_mock.get_bin_path = MagicMock()
    main_mock.get_bin_path.return_value = '/usr/bin/debconf-show'

    set_selection_mock = MagicMock()
    set_selection_mock.return_value = (0, '', '')

    get_selections_mock = MagicMock()
    get_selections_mock.return_value = {'foo': 'bar'}



# Generated at 2022-06-13 05:08:03.471294
# Unit test for function main
def test_main():
    # Importing module
    module_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../', 'library', 'debconf.py')
    module_args = {}
    set_module_args(module_args)
    sys.path.append(module_path)

# Generated at 2022-06-13 05:08:14.094057
# Unit test for function main
def test_main():
    m = AnsibleModule(
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
    m.params["name"] = "local"
    m.params["question"] = "locales/default_environment_locale"
   

# Generated at 2022-06-13 05:08:26.496379
# Unit test for function main
def test_main():

    from ansible.module_utils.basic import AnsibleModule

    def assertModuleFail(params, msg=None):
        '''Assert that the module fails with an error message containing the given string.'''

# Generated at 2022-06-13 05:08:27.599589
# Unit test for function get_selections
def test_get_selections():
    assert get_selections("tzdata")


# Generated at 2022-06-13 05:08:34.494263
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

    pkg = "dummy_pkg"
    question = "dummy_question"
    vtype = "boolean"

# Generated at 2022-06-13 05:08:45.153004
# Unit test for function set_selection
def test_set_selection():
    module = AnsibleModule(argument_spec=None, supports_check_mode=True)
    pkg = "tzdata"
    question = "tzdata/Areas"
    vtype = "multiselect"
    value = "Europe"
    unseen = False
    rc, msg, error = set_selection(module, pkg, question, vtype, value, unseen)
    assert rc == 0
    assert error is None
    assert msg == ''
    # Since we run debconf-set-selections this should return 'ok', otherwise something is wrong
    assert to_text(module.run_command([module.get_bin_path('debconf-show', True), pkg])) == 'ok'

# Generated at 2022-06-13 05:10:17.618733
# Unit test for function set_selection
def test_set_selection():
    import subprocess
    import shlex
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
    v

# Generated at 2022-06-13 05:10:29.806127
# Unit test for function get_selections
def test_get_selections():
    import sys
    import os
    import json
    import pytest
    from collections import namedtuple

    # Import the Ansible module to be tested.
    from ansible.modules.system import debconf as debconf_module

    # AnsibleModule object
    from ansible.module_utils.basic import AnsibleModule

    # This module requires the command line debconf tools.
    pkg = 'debconf-utils'

    TestCase = namedtuple('TestCase', ['module', 'result'])


# Generated at 2022-06-13 05:10:38.083928
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
    pkg = module.params["name"]
    question = module.params["question"]
    vtype = module.params["vtype"]


# Generated at 2022-06-13 05:10:41.000884
# Unit test for function main
def test_main():
    module = AnsibleModule(argument_spec=dict())
    module.exit_json = exit_json
    main()


# Generated at 2022-06-13 05:10:51.234297
# Unit test for function get_selections
def test_get_selections():
    def get_selections_mock(module, pkg):
        return {'setting1': 'value1', 'setting2': 'value2'}

    module = AnsibleModule(argument_spec={})
    prev_run = globals().get('run_command')
    globals()['run_command'] = module.run_command
    prev_get_bin_path = globals().get('get_bin_path')
    globals()['get_bin_path'] = module.get_bin_path
    prev_selections = globals().get('get_selections')
    globals()['get_selections'] = get_selections_mock

# Generated at 2022-06-13 05:10:53.756160
# Unit test for function set_selection
def test_set_selection():
    setsel = set_selection(module, "module", "question", "vtype", "value", "unseen")
    assert 1 == 1

# Generated at 2022-06-13 05:10:59.835248
# Unit test for function set_selection
def test_set_selection():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils import basic
    from ansible.module_utils.debconf import set_selection

    def run_command(cmd, data, check_rc=False):
        return (0, str(cmd) + " " + data, "")

    m = AnsibleModule(argument_spec=dict())
    m.get_bin_path = lambda x, y: x
    m.run_command = run_command

    test_question = 'test_question'
    test_vtype = 'test_vtype'
    test_value = 'test_value'

    set_selection(m, 'test_pkg', test_question, test_vtype, test_value, False)


# Generated at 2022-06-13 05:11:09.682634
# Unit test for function set_selection
def test_set_selection():
    from ansible.module_utils.ansible_release import __version__
    from ansible.module_utils._text import to_bytes
    mod = AnsibleModule(argument_spec={}, supports_check_mode=True)
    mod.params["name"] = "tzdata"
    mod.params["question"] = "tzdata/SystemTimezone"
    mod.params["vtype"] = "select"
    mod.params["value"] = "America/Los_Angeles"
    mod.params["unseen"] = False
    mod.params["check_mode"] = True
    rc, msg, err = set_selection(mod, mod.params["name"], mod.params["question"], mod.params["vtype"], mod.params["value"], mod.params["unseen"])

# Generated at 2022-06-13 05:11:17.465664
# Unit test for function get_selections
def test_get_selections():
    ''' get_selections should return a dictionary with the questions and values '''

    # arguments
    class Args(object):
        def __init__(self, name):
            self.name = name

    # mock class for module
    class Module(object):
        def __init__(self, name):
            self.params = Args(name)

        def run_command(self, cmd, data=None):
            ''' return a fake list of questions and values '''
            out = '''
* locales/default_environment_locale: en_US.UTF-8
* locales/locales_to_be_generated: en_US.UTF-8 UTF-8, fr_FR.UTF-8 UTF-8
'''
            return 0, out, None

    # get a list of selection

# Generated at 2022-06-13 05:11:26.413810
# Unit test for function set_selection
def test_set_selection():
    """
    Test function set_selection
    """
    # Given
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
    pkg = "test"
    question = "test"
   