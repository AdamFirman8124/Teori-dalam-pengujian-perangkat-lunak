

# Generated at 2022-06-13 05:02:44.224539
# Unit test for function get_selections
def test_get_selections():
    mock = MagicMock()
    #mocked = Mock(return_value={"locales/locales_to_be_generated": "en_US.UTF-8 UTF-8"})
    #mock.debconf_show = mocked
    expected = {"locales/default_environment_locale": "fr_FR.UTF-8",
                "locales/locales_to_be_generated": "en_US.UTF-8 UTF-8"}

# Generated at 2022-06-13 05:02:51.988961
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
    question = module.params["question"]
    vtype = module.params["vtype"]
    value

# Generated at 2022-06-13 05:02:58.068918
# Unit test for function main
def test_main():
    from ansible.module_utils import basic

    pkg = 'locales'
    question = 'locales/default_environment_locale'
    vtype = 'select'
    value = 'fr_FR.UTF-8'

    mod_params = {
        'name': pkg,
        'question': question,
        'vtype': vtype,
        'value': value,
        'unseen': False
    }

    mock_ansible_module = basic.AnsibleModule(**mod_params)

    if not hasattr(mock_ansible_module, 'exit_json'):
        mock_ansible_module.exit_json = basic.AnsibleModule.exit_json

    mock_ansible_module.run_command = basic.AnsibleModule.run_command


# Generated at 2022-06-13 05:03:07.098515
# Unit test for function main
def test_main():
    from ansible.module_utils import basic

    module = basic.AnsibleModule(
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

    # TODO: enable passing array of options and/or debconf file from get-

# Generated at 2022-06-13 05:03:13.338219
# Unit test for function get_selections
def test_get_selections():
    test_module = AnsibleModule(
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

# Generated at 2022-06-13 05:03:22.655476
# Unit test for function main

# Generated at 2022-06-13 05:03:34.034907
# Unit test for function set_selection
def test_set_selection():
    import os

    os.environ['LANG'] = 'en_US.UTF-8'


# Generated at 2022-06-13 05:03:47.289908
# Unit test for function set_selection
def test_set_selection():
    module = AnsibleModule(
        argument_spec=dict(
            pkg=dict(type='str', required=True, aliases=['pkg']),
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

# Generated at 2022-06-13 05:03:54.946780
# Unit test for function get_selections
def test_get_selections():
    test_pkg='locales'
    selections = get_selections(module, test_pkg)
    assert('locales/locales_to_be_generated' in selections)
    assert('locales/default_environment_locale' in selections)
    assert('locales/default_environment_locale' in selections)
    test_pkg='tzdata'
    selections = get_selections(module, test_pkg)
    assert('tzdata/Areas' in selections)
    assert('tzdata/Zones/Etc' in selections)

# Generated at 2022-06-13 05:03:59.842397
# Unit test for function set_selection
def test_set_selection():
    import os
    from ansible.module_utils.basic import AnsibleModule
    from ansible_collections.ansible.builtin.plugins.module_utils.debconf import set_selection

    setsel = '/usr/bin/debconf-set-selections'

    if os.path.exists(setsel):
        rc, out, err = set_selection(AnsibleModule, 'test', 'test', 'test', 'test')
        print(rc)
        print(out)
        print(err)
    else:
        print('skipping test, debconf-set-selections not found')

# Generated at 2022-06-13 05:04:22.181549
# Unit test for function set_selection
def test_set_selection():
    # Setting argument spec
    module_args=dict(
            name='locales',
            question='locales/default_environment_locale',
            vtype='select',
            value='fr_FR.UTF-8',
            unseen=False
            )

    # Setting up a new module object
    module = AnsibleModule(module_args)

    rc, _msg, _e = set_selection(module, 'locales', 'locales/default_environment_locale', 'select', 'fr_FR.UTF-8', False)
    assert rc == 0

    # Test with unseen=True
    # Setting argument spec

# Generated at 2022-06-13 05:04:29.576296
# Unit test for function get_selections
def test_get_selections():
    """
    Test function get_selections

    This function does not return anything, it instead modifies the
    'module' object it receives as argument and fails it if the debconf
    command fails.

    Ideally, we would mock the module.run_command calls, but the mock
    library (and python-unittest in general) doesn't allow mocking
    __builtins__ (which includes 'file'), so we have to mock the whole
    module and play with its internals.

    This means that this is not 100% unit-tested, and that the result
    of the function can be different if the 'module' object has changed.
    """

    # We can't just import the module, as it would mess with the actual
    # module's globals
    mod = types.ModuleType("ansible")
    mod.__file__ = "ansible"
   

# Generated at 2022-06-13 05:04:41.387840
# Unit test for function set_selection
def test_set_selection():
    # Mocks
    import ansible.module_utils.basic
    import ansible.module_utils.common

    m_module = ansible.module_utils.basic.AnsibleModule(argument_spec={})

    def run_command(cmd, data, check_rc):
        assert cmd == ['debconf-set-selections']
        assert data == 'package_name question_name vtype value'
        assert check_rc == True
        return 0, '', ''

    m_module.run_command = run_command

    # Run code to test
    rc, msg, err = set_selection(m_module, 'package_name', 'question_name', 'vtype', 'value', False)
    assert rc == 0
    assert msg == ''
    assert err == ''

# Generated at 2022-06-13 05:04:47.470477
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

    pkg = module.params["name"]
    question = module.params["question"]
    vtype = module.params["vtype"]


# Generated at 2022-06-13 05:04:53.888194
# Unit test for function get_selections
def test_get_selections():
    import mock

    module = mock.Mock()
    module.run_command.return_value = (0, "preseed db_type select ", "")
    module.get_bin_path.return_value = "/usr/bin/debconf-show"

    result = get_selections(module, "debconf")

    assert result == {'db_type': 'select '}

# Generated at 2022-06-13 05:05:02.147099
# Unit test for function get_selections
def test_get_selections():
    def test_get_selections_sub(text):
        from ansible.module_utils.basic import AnsibleModule
        from ansible.module_utils._text import to_text
        from ansible.module_utils.debconf import get_selections

        class TestModule(object):
            def __init__(self):
                self.run_command_calls = []

            def run_command(self, cmd, data=None):
                self.run_command_calls.append((cmd, data))
                if text.startswith('RunCommandrc=0'):
                    return (0, '\n'.join(text[len('RunCommandrc=0:'):].split('\n')), '')
                return (1, '', text)

            def get_bin_path(self, name, required):
                return name



# Generated at 2022-06-13 05:05:11.417334
# Unit test for function set_selection
def test_set_selection():
    # Test normal execution
    rc, msg, err = set_selection(module, pkg, question, vtype, value, unseen)
    assert rc == 0
    
    # Test failure due lack of value
    vtype = None
    value = None
    module.fail_json(msg="when supplying a question you must supply a valid vtype and value")

    # Test failure due to bad executable
    module = AnsibleModule(
        argument_spec=dict(
            executable=dict(type='str', default=''),
        ),
        supports_check_mode=True,
    )
    executable = 'executable'
    module.fail_json(msg="invalid executable specified '%s'" % executable)

# Generated at 2022-06-13 05:05:20.125674
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    # Create a dummy module
    module = basic.AnsibleModule(argument_spec={'name': {'default': True, 'type': 'str'}, 'question': {'default': True, 'type': 'str'}, 'vtype': {'default': True, 'type': 'str', 'choices': ['boolean', 'error', 'multiselect', 'note', 'password', 'seen', 'select', 'string', 'text', 'title']}, 'value': {'default': True, 'type': 'str'}, 'unseen': {'default': False, 'type': 'bool'}}, required_together=[['question', 'vtype', 'value']], supports_check_mode=True)
    module.check_mode = False

# Generated at 2022-06-13 05:05:32.314865
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

    # TODO: enable passing array of options and/or debconf file from get-selections dump
    pkg = module.params["name"]

# Generated at 2022-06-13 05:05:32.912500
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:05:55.779707
# Unit test for function get_selections
def test_get_selections():
    import mock
    import os

    import get_selections

    test_data = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'debconf-show_tzdata')

    with mock.patch('ansible.module_utils.basic.AnsibleModule') as mock_module:
        with mock.patch('ansible.module_utils.basic.AnsibleModule.run_command') as mock_run_command:
            mock_run_command.return_value = (0, open(test_data, 'rb').read(), '')
            get_selections.get_selections(mock_module)

# Generated at 2022-06-13 05:06:05.218044
# Unit test for function get_selections
def test_get_selections():
    pkg = "tzdata"
    rc = 0

# Generated at 2022-06-13 05:06:06.037451
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-13 05:06:18.519615
# Unit test for function main
def test_main():
    import datetime
    from ansible.modules.system.debconf import main
    from ansible.module_utils.common._collections_compat import Mapping
    module = AnsibleModule(argument_spec={
            'name':{'type': 'str','required': True},
            'question':{'type': 'str','aliases': ['selection','setting']},
            'vtype':{'type': 'str','choices': ['boolean','error','multiselect','note','password','seen','select','string','text','title']},
            'value':{'type': 'str','aliases': ['answer']},
            'unseen':{'type': 'bool','default':False}
        },
        required_together=({'question','vtype','value'}),
        supports_check_mode=True
    )

# Generated at 2022-06-13 05:06:26.218415
# Unit test for function set_selection
def test_set_selection():
    args = {
        'name': 'tzdata',
        'question': 'tzdata/Areas',
        'value': 'Europe',
        'vtype': 'select'
    }
    m = AnsibleModule(argument_spec=args)
    m.run_command = mock_run_command
    set_selection(m, 'tzdata', 'tzdata/Areas', 'select', 'Europe', False)

# Generated at 2022-06-13 05:06:36.969841
# Unit test for function main
def test_main():
  sample_input = {
    "name": "locales",
    "question": "locales/default_environment_locale",
    "vtype": "select",
    "value": "fr_FR.UTF-8",
  }
  sample_output = {
    "current": {
      "locales/default_environment_locale": "fr_FR.UTF-8"
    },
    "changed": True,
    "msg": ""
  }
  with mock.patch("ansible.module_utils.debconf.module", autospec=True) as mock_module:
    mock_module.params = sample_input
    mock_module.return_value = sample_output
    assert main() == sample_output

# Generated at 2022-06-13 05:06:50.091258
# Unit test for function set_selection
def test_set_selection():
    with mock.patch('debconf_mod.os.environ', new_callable=dict):
        with mock.patch('debconf_mod.run_command', return_value=(0, '', '')), mock.patch('debconf_mod.AnsibleModule'):
            mock_module = mock.MagicMock(name='AnsibleModule')
            mock_module.check_mode = False
            set_selection(mock_module, 'tzdata', 'tzdata/Zones/Europe', 'string', 'Bucharest', False)
            mock_module.run_command.assert_called_once_with(['/usr/bin/debconf-set-selections'], data='tzdata tzdata/Zones/Europe string Bucharest')

# Generated at 2022-06-13 05:06:59.683288
# Unit test for function main
def test_main():
    import os
    import json
    import pytest
    import ansible.module_utils.basic as ansible_module
    import ansible.module_utils.action as ansible_action
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils._text import to_text

    current_path = os.path.dirname(__file__)
    module_args = dict(
        name="tzdata",
        question=None,
        vtype=None,
        value=None,
        unseen=False
    )


# Generated at 2022-06-13 05:07:10.687663
# Unit test for function get_selections
def test_get_selections():
    # Create the module object
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

    # Initialise test input
    pkg = 'locales'

    # Call the function
    selections = get

# Generated at 2022-06-13 05:07:17.638695
# Unit test for function main
def test_main():
    import sys
    import os
    import json
    import subprocess

    #capture output
    oldout, olderr = sys.stdout, sys.stderr
    sys.stdout, sys.stderr = StringIO(), StringIO()
    os.environ['ANSIBLE_MODULE_ARGS'] = json.dumps(dict(
        name='tzdata',
        question='tzdata/Zone',
        vtype='select',
        value='Asia/Kolkata',
        unseen='false',
        diff='true',
        log_path='/tmp/test.log',
    ))
    try:
        main()
        result = json.loads(sys.stdout.getvalue())
        assert result['changed']
    finally:
        # restore output
        sys.stdout, sys.stderr = oldout

# Generated at 2022-06-13 05:08:09.360780
# Unit test for function main
def test_main():

    # Example of how to capture the stdout of a function:
    # https://stackoverflow.com/a/42748974/699831
    from io import StringIO
    from unittest.mock import patch

    # Capture module.fail_json(msg)
    with patch('ansible.module_utils.basic.AnsibleModule.fail_json') as mock_fail_json:

        # First time we try to set a value, it will not have been set before
        pkg = "test_package"
        question = "test_question"
        vtype = "string"
        value = "test_value"
        unseen = False
        check_mode = False

        # Output of the function will be stored in result

# Generated at 2022-06-13 05:08:16.802134
# Unit test for function set_selection
def test_set_selection():
    def run_command(cmd, data=None):
        if cmd[1] == '-u':
            cmd.pop(1)
        if cmd[-2:] == '-f -':
            cmd.pop()
            cmd.pop()
        if data != None:
            cmd.append(data)
        return 0, '', ''
    module = AnsibleModule(argument_spec=dict())
    module.run_command = run_command
    rc, out, err = set_selection(module, 'locales', 'locales/default_environment_locale', 'string', 'fr_FR.UTF-8', False)
    assert rc == 0

# Generated at 2022-06-13 05:08:27.586952
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

    # TODO: enable passing array of options and/or debconf file from get-selections dump
    pkg = module.params["name"]

# Generated at 2022-06-13 05:08:33.473880
# Unit test for function get_selections
def test_get_selections():
    class FakeModule(object):
        def __init__(self):
            self.run_command_called = False
            self.run_command_params = None
            self.run_command_calls = 0

        def get_bin_path(self, what, required):
            return what
        def run_command(self, params, data=None):
            self.run_command_called = True
            self.run_command_params = params
            self.run_command_calls += 1
            if self.run_command_calls == 1:
                return 0, "", ""
            return 0, "abc: 123\nxyz: 456", ""
    module = FakeModule()
    selections = get_selections(module, "wibble")
    assert module.run_command_called
    assert module.run_command_

# Generated at 2022-06-13 05:08:45.697413
# Unit test for function set_selection
def test_set_selection():
    # mocking module class
    class MockModule:
        def __init__(self):
            self.exit_json = mock.Mock()
            self.fail_json = mock.Mock()
            self.params = {
                'unseen': True
            }
            self.run_command = mock.Mock(return_value=(0, '', ''))
            self.get_bin_path = mock.Mock(return_value='/bin/debconf-set-selections')

    # mocking module
    module = MockModule()
    set_selection(module, 'foo', 'bar', 'baz', 'bax', unseen=True)
    module.run_command.assert_called_with(['/bin/debconf-set-selections', '-u'], data='foo bar baz bax')
    module.exit

# Generated at 2022-06-13 05:08:53.789144
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
    )
    pkg = 'fake_pkg'
    question = 'fake_question'
    vtype = 'select'
    value = 'fake_value'
    unseen = False
    rc

# Generated at 2022-06-13 05:08:54.348523
# Unit test for function set_selection
def test_set_selection():
    set_selection()

# Generated at 2022-06-13 05:08:58.044845
# Unit test for function set_selection
def test_set_selection():
    # Test to check if a value is set correctly and return code is zero
    assert set_selection('locales', 'locales/locales_to_be_generated', 'multiselect', 'en_US.UTF-8 UTF-8, fr_FR.UTF-8 UTF-8') == 0

    # Test to check if an invalid type is set correctly and return code is non-zero
    asser

# Generated at 2022-06-13 05:09:08.837182
# Unit test for function set_selection
def test_set_selection():
    def mockrun_command(module, cmd, data=None, check_rc=True, close_fds=True, executable=None,
                        data_encoding=None, binary=False, path_prefix=None, cwd=None):
        assert module is not None
        assert cmd is not None
        assert data is None
        assert check_rc is not None
        assert close_fds is not None
        assert executable is not None
        assert data_encoding is None
        assert binary is not None
        assert path_prefix is None
        assert cwd is None

        cmd[0] = '/bin/echo'
        return 0, 'test', 'errtest'

    def mockget_bin_path(module, name, required=True):
        assert module is not None
        assert name is not None
        assert required is not None

        return

# Generated at 2022-06-13 05:09:16.395700
# Unit test for function main
def test_main():
    # run the module with defaults
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
    module.exit_json = print
    #main(module)


# Generated at 2022-06-13 05:10:59.377237
# Unit test for function get_selections
def test_get_selections():
    ''' Returns list of questions and values for package '''
    import os
    import tempfile

    # create an empty debconf config file
    debconf_file = tempfile.NamedTemporaryFile(delete=False)
    debconf_file.close()

    # create a debconf setting in the file
    os.system('echo "locales locales/locales_to_be_generated multiselect en_US.UTF-8 UTF-8, fr_FR.UTF-8 UTF-8" > %s' % debconf_file.name)

    # create a fake module
    module = AnsibleModule(argument_spec={'name': {'required': True}}, supports_check_mode=False)

    # run the function
    selections = get_selections(module, 'locales')

    # test values

# Generated at 2022-06-13 05:11:05.428239
# Unit test for function get_selections
def test_get_selections():
    module = AnsibleModule(
        argument_spec=dict())
    module.run_command = MagicMock(return_value=(0, 'tzdata tzdata/Areas select Europe\ntzdata tzdata/Zones/Europe select Paris\n', ''))
    package = 'tzdata'

    selections = get_selections(module, package)

    assert selections == {u'tzdata/Zones/Europe': u'Paris', u'tzdata/Areas': u'Europe'}

# Generated at 2022-06-13 05:11:13.664722
# Unit test for function set_selection
def test_set_selection():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.basic import AnsibleModule
    import os

    def test_module(module_args, expected_result):
        def run_command(cmd, data):
            if cmd == ['debconf-set-selections', '-u']:
                return 0, data, ''
            elif cmd[1] == 'reconfigure':
                return 0, '', ''
            else:
                raise ValueError("Unexpected command")


# Generated at 2022-06-13 05:11:15.781771
# Unit test for function get_selections
def test_get_selections():
    get_selections(ansible.builtin.debconf, 'tzdata')
    assert True

# Generated at 2022-06-13 05:11:18.578000
# Unit test for function get_selections
def test_get_selections():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True,
        )
    selections = get_selections(module, 'tzdata')
    assert "Time zone?" in selections
    assert "GeoClue2" in selections

# Generated at 2022-06-13 05:11:26.671551
# Unit test for function get_selections
def test_get_selections():
    x = get_selections(AnsibleModule, "tzdata")

# Generated at 2022-06-13 05:11:27.406510
# Unit test for function set_selection
def test_set_selection():
    return 0

# Generated at 2022-06-13 05:11:35.676434
# Unit test for function main
def test_main():
    module.exit_json = MagicMock()
    module.run_command = MagicMock(return_value=(0, "", ""))
    module.fail_json = MagicMock()
    module.get_bin_path = MagicMock(return_value=True)

    def set_selections(module, pkg, question, vtype, value, unseen):
        return (0, "", "")

    get_selections(module, "pkg")
    set_selection(module, pkg, question, vtype, value, unseen)
    main()

# Generated at 2022-06-13 05:11:44.617380
# Unit test for function main
def test_main():
    # Tests for function main
    class TestArgs(object):
        """ Empty class to use as a test namespace """
        pass

    test_args = TestArgs()

    test_args.name = 'tzdata'
    test_args.question = None
    test_args.vtype = None
    test_args.value = None


# Generated at 2022-06-13 05:11:45.402705
# Unit test for function main
def test_main():
    assert True