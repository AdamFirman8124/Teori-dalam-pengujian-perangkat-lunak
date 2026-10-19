

# Generated at 2022-06-13 05:02:39.131822
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

# Generated at 2022-06-13 05:02:42.348675
# Unit test for function get_selections
def test_get_selections():
    result = get_selections(module, pkg)
    result_keys = result.keys()
    if result_keys != 'question':
        module.fail_json(msg="expected {0}, got {1}".format('question', result_keys))


# Generated at 2022-06-13 05:02:52.584279
# Unit test for function set_selection
def test_set_selection():
    import ansible.module_utils.basic
    import ansible.module_utils._text
    import ansible.module_utils.debconf

    test_module = ansible.module_utils.basic.AnsibleModule(argument_spec={
        'name': {
            'required': True,
            'type': 'str'
        },
        'question': {
            'required': True,
            'type': 'str'
        },
        'vtype': {
            'required': True,
            'type': 'str'
        },
        'value': {
            'required': True,
            'type': 'str'
        },
        'unseen': {
            'required': False,
            'type': 'bool'
        },
    })

    pkg = 'test_package'

# Generated at 2022-06-13 05:03:02.869811
# Unit test for function main
def test_main():
    # test with invalid parameters
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
        strict=True
    )

    # test with valid parameters
    # also test different vtypes specified

# Generated at 2022-06-13 05:03:08.713480
# Unit test for function set_selection
def test_set_selection():
    # Prepare for Unit Test
    import sys
    sys.modules['ansible.module_utils.basic'] = sys.modules['ansible.builtin.unit.module_utils.basic']
    sys.modules['ansible.module_utils._text'] = sys.modules['ansible.builtin.unit.module_utils._text']
    from ansible.module_utils.basic import AnsibleModule
    import ansible.builtin.debconf
    import ansible.builtin.unit.module_utils.basic as basic_utils
    import ansible.builtin.unit.module_utils._text as text_utils
    module = AnsibleModule(argument_spec={})
    module.run_command = basic_utils.run_command
    module.run_command_environ_update = basic_utils.run_command_environ_update
   

# Generated at 2022-06-13 05:03:20.892347
# Unit test for function get_selections
def test_get_selections():
    # Define a test module
    class TestModule(object):
        def __init__(self):
            self.fail_json = self.fail_json
            self.run_command = self.run_command
            self.get_bin_path = self.get_bin_path

            self.fail_json_count = 0
            self.run_command_count = 0
            self.get_bin_path_count = 0

        def fail_json(self, **kwargs):
            self.fail_json_count = self.fail_json_count + 1

        def run_command(self, **kwargs):
            self.run_command_count = self.run_command_count + 1
            return(0, '', '')

        def get_bin_path(self, **kwargs):
            self.get_bin_

# Generated at 2022-06-13 05:03:24.060319
# Unit test for function set_selection
def test_set_selection():
    with pytest.raises(TypeError, match='unsupported operand type'):
        set_selection(1, 2, 3, 4, 5, 6)

# Generated at 2022-06-13 05:03:36.070201
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


# Generated at 2022-06-13 05:03:48.897448
# Unit test for function main
def test_main():

    class TestModule(object):
        def __init__(self):
            self.params = dict()
            self.support_check_mode = True
            self.check_mode = False
            self.bin_path = dict()
            self.run_command = dict()

        def get_bin_path(self, executable, required):
            return 'some/path'

        def get_params(self):
            return self.params

        def fail_json(self, msg):
            print(msg)

        def exit_json(self, **kwargs):
            return kwargs

        def run_command(self, cmd, data=None):
            return 0, None, None

        def supports_check_mode(self):
            return self.support_check_mode

        def check_mode(self):
            return self.check_mode

# Generated at 2022-06-13 05:03:57.638636
# Unit test for function set_selection
def test_set_selection():
    import subprocess
    class FakeModule():
        def get_bin_path(self, arg, arg2):
            return arg
    class FakeSubprocess():
        def __init__(self):
            self.returncode = 0
        def run_command(self, command, data=None):
            # test valid command string
            self.command = command
            self.data = data
            return self.returncode, self.command, self.data
    class FakeSubprocessFail():
        def __init__(self):
            self.returncode = 1
        def run_command(self, command, data=None):
            # test valid command string
            self.command = command
            self.data = data
            return self.returncode, self.command, self.data

    pkg = "mypackage"
    question = "myquestion"


# Generated at 2022-06-13 05:04:15.610801
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

# Generated at 2022-06-13 05:04:25.811447
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

# Generated at 2022-06-13 05:04:39.388683
# Unit test for function set_selection
def test_set_selection():
  class Module():
    pass
  class AnsibleModule():
    def __init__(self, argument_spec=None, required_together=None, supports_check_mode=None):
      self.argument_spec = argument_spec
      self.required_together = required_together
      self.supports_check_mode = supports_check_mode
      self.params = Module()
    def fail_json(self, msg=None):
      assert False, msg
    def run_command(self, cmd=None, data=None):
      assert cmd is not None
      assert data is not None
      return None, None, None

# Generated at 2022-06-13 05:04:40.761863
# Unit test for function main
def test_main():
    assert main()

# Generated at 2022-06-13 05:04:47.131219
# Unit test for function get_selections
def test_get_selections():
    test_obj = AnsibleModule(
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
    test_obj.run_command = MagicMock(return_value=(0, 'foo: bar\n', ''))
    test

# Generated at 2022-06-13 05:04:58.580169
# Unit test for function set_selection
def test_set_selection():
    from ansible.module_utils.common.process import get_bin_path

    class FakeModule(object):
        def __init__(self):
            self.fake_setsel = get_bin_path('debconf-set-selections')

        def get_bin_path(self, bin, required=False, opt_dirs=[]):
            return self.fake_setsel

        def run_command(self, cmd, data=None):
            return 0, '%s: %s' % (cmd, data), None

    class FakeSelection(object):
        def __init__(self, pkg='hello-world', question='test_question', vtype='multiselect', value='A, B, C', unseen=False):
            self.pkg = pkg
            self.question = question
            self.vtype = vtype

# Generated at 2022-06-13 05:05:04.528913
# Unit test for function get_selections
def test_get_selections():
    assert get_selections('ansible.builtin.debconf', 'locales') == {'debconf_selections_backend': 'Pipe',\
                                                                    'debconf_selections_path': '/var/cache/debconf/passive',\
                                                                    'locales/default_environment_locale': 'fr_FR.UTF-8'}


# Generated at 2022-06-13 05:05:07.396776
# Unit test for function main
def test_main():
#    f = StringIO()
#    main(f)
#    assert f.getvalue() == 'Hello World!\n'
    pass

# Generated at 2022-06-13 05:05:15.695179
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

    main_func = lambda: main()
    returncode, out, err = run_module_as_main(module, main_func)


# Generated at 2022-06-13 05:05:24.103225
# Unit test for function main
def test_main():
    __salt__ = {}
    __opts__ = {}
    __utils__ = {}
    __pillar__ = {}

    try:
        import salt.utils.timed_subprocess as M
    except:
        import lib.salt.utils.timed_subprocess as M
    M.TimedProc = TimedProc
    M.TimedProc.return_value.pid=1
    M.TimedProc.return_value.returncode=0
    M.TimedProc.return_value.stdout.read.return_value=""
    M.TimedProc.return_value.stderr.read.return_value=""


# Generated at 2022-06-13 05:05:50.379176
# Unit test for function main
def test_main():
    import ansible.module_utils
    args = dict(
        name = "tzdata",
    )


# Generated at 2022-06-13 05:06:02.456894
# Unit test for function main
def test_main():
    # given
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', required=True, aliases=['pkg']),
            question=dict(type='str', aliases=['selection', 'setting']),
            vtype=dict(type='str', choices=['boolean', 'error', 'multiselect', 'note', 'password', 'seen', 'select',
                                            'string', 'text', 'title']),
            value=dict(type='str', aliases=['answer']),
            unseen=dict(type='bool', default=False),
        ),
        required_together=(['question', 'vtype', 'value'],),
        supports_check_mode=True,
    )

    # when
    main()

# vim: set expandtab:ts=4:sw=4

# Generated at 2022-06-13 05:06:04.495352
# Unit test for function set_selection
def test_set_selection():
    set_selection(module,pkg,question,vtype,value,unseen)

# Generated at 2022-06-13 05:06:07.340777
# Unit test for function get_selections
def test_get_selections():
    assert get_selections(None, "base-files") is not None
    assert get_selections(None, "doesntexist") == {}

# Generated at 2022-06-13 05:06:13.643949
# Unit test for function set_selection
def test_set_selection():
    module = AnsibleModule(argument_spec={})

    # nothing should fail here
    module.run_command([module.get_bin_path('debconf-set-selections', True)], 'foo bar string foobar')
    module.run_command([module.get_bin_path('debconf-set-selections', True), '-u'], 'foo bar string foobar')

# Generated at 2022-06-13 05:06:24.598084
# Unit test for function set_selection
def test_set_selection():
    class module:
        def __init__(self):
            self.run_command_return = 0
            self.run_command_msg = ''

        def get_bin_path(self, prog, required):
            return 'prog'

        def run_command(self, cmd, data=None):
            self.run_command_cmd = cmd
            self.run_command_data = data
            return self.run_command_return, '', self.run_command_msg

    test_module = module()
    test_module.run_command_return = 0
    test_module.run_command_msg = ''
    pkg = 'test-package'
    question = 'test-question'
    vtype = 'string'
    value = 'test-value'
    unseen = False
    rc, msg, e = set_

# Generated at 2022-06-13 05:06:36.929680
# Unit test for function main
def test_main():
    try:
        from debconf import Debconf, DebconfError
    except ImportError:
        raise AssertionError("debconf is not available")

    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six.moves import StringIO

    def run_command(module, cmd, data):
        if cmd[0] == 'debconf-show':
            if cmd[1] == '-t' and cmd[2] == 'neutron-common':
                return 0, None, None
            if cmd[1] == 'neutron-common':
                temp = '''
* debconf: falling back to frontend: Dialog
%s: %s: seen: false
'''

# Generated at 2022-06-13 05:06:37.651240
# Unit test for function set_selection
def test_set_selection():
    assert True

# Generated at 2022-06-13 05:06:38.910575
# Unit test for function get_selections

# Generated at 2022-06-13 05:06:52.579825
# Unit test for function set_selection
def test_set_selection():
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
    where = '/usr/bin/debconf-set-selections'

# Generated at 2022-06-13 05:07:46.920519
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils.common.process import get_bin_path

    module = basic.AnsibleModule(argument_spec={'name': {'type': 'str', 'required': True, 'aliases': ['pkg']}, 'question': {'type': 'str', 'aliases': ['selection', 'setting']}, 'vtype': {'type': 'str', 'choices': ['boolean', 'error', 'multiselect', 'note', 'password', 'seen', 'select', 'string', 'text', 'title']}, 'value': {'type': 'str', 'aliases': ['answer']}, 'unseen': {'type': 'bool', 'default': False}}, required_together=([['question', 'vtype', 'value']]), supports_check_mode=True)
   

# Generated at 2022-06-13 05:07:56.610888
# Unit test for function set_selection
def test_set_selection():
    # Arrange
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

    # Act
    m.run_command = lambda cmd, data=None: (0, data, None)
    rc

# Generated at 2022-06-13 05:08:06.539277
# Unit test for function main
def test_main():
    args = {
        'name': 'test',
        'question': 'test',
        'vtype': 'string',
        'value': 'test',
        'unseen': False,
    }

    check_mode = False


# Generated at 2022-06-13 05:08:16.547635
# Unit test for function get_selections
def test_get_selections():
    test_module = AnsibleModule(argument_spec = dict(name = dict(type = 'str', required = True, aliases = ['pkg']),
                                                     question = dict(type = 'str', aliases = ['selection', 'setting']),
                                                     vtype = dict(type = 'str',
                                                                  choices=['boolean', 'error', 'multiselect', 'note', 'password', 'seen', 'select', 'string',
                                                                           'text', 'title']),
                                                     value = dict(type = 'str', aliases = ['answer']),
                                                     unseen = dict(type='bool', default=False)
                                                     ))
    test_question = "tzdata/Zones/Etc"
    test_value = "UTC"
    test_pkg = "tzdata"

# Generated at 2022-06-13 05:08:21.055020
# Unit test for function main
def test_main():
    from ansible.module_utils import debconf

    # Test choices
    #
    # Test Call
    #
    assert len(debconf.get_selections(module, 'tzdata')) > 0

# Generated at 2022-06-13 05:08:29.368509
# Unit test for function set_selection
def test_set_selection():
    args = {
        '_ansible_check_mode': True,
        '_ansible_diff': False,
        '_ansible_module_name': 'debconf',
        '_ansible_no_log': False,
        '_ansible_verbosity': 0,
        'name': 'tripwire',
        'question': 'tripwire/site-passphrase',
        'vtype': 'password',
        'value': 'verysecret',
        'unseen': True
    }

# Generated at 2022-06-13 05:08:33.941824
# Unit test for function get_selections
def test_get_selections():
    from ansible.errors import AnsibleModuleExit
    import os
    import sys
    import pytest
    sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
    from units.modules.utils import AnsibleExitJson, AnsibleFailJson, ModuleTestCase, set_module_args

    # the results should be the same, but sorted
    pkg = "locales"
    result_expected = {'locales/locales_to_be_generated': 'en_US.UTF-8 UTF-8', 'locales/default_environment_locale': 'en_US.UTF-8'}
    selections = get_selections(ModuleTestCase(module=AnsibleModule(argument_spec={})), pkg)

    assert len(result_expected) == len

# Generated at 2022-06-13 05:08:46.272057
# Unit test for function main
def test_main():
    global module

    def setUp():
        global module
        module = AnsibleModule(
            argument_spec=dict(
                name=dict(type='str', required=True, aliases=['pkg']),
                question=dict(type='str', aliases=['selection', 'setting']),
                vtype=dict(type='str', choices=['boolean', 'error', 'multiselect', 'note', 'password', 'seen', 'select', 'string', 'text', 'title']),
                value=dict(type='str', aliases=['answer']),
                unseen=dict(type='bool', default=False),
            ),
            supports_check_mode=True,
        )

    def test_get_selections():
        global module
        pkg = "ansible_test_pkg"
        setsel = module.get_bin_

# Generated at 2022-06-13 05:08:49.596834
# Unit test for function get_selections
def test_get_selections():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.debconf import get_selections
    module = AnsibleModule(argument_spec={})
    selections = get_selections(module, 'git')
    assert selections

# Generated at 2022-06-13 05:08:50.727153
# Unit test for function set_selection
def test_set_selection():
    assert set_selection('pkg', 'key', 'type', 'value') == 'debconf-set-selections -u pkg key type value'

# Generated at 2022-06-13 05:10:19.445041
# Unit test for function main
def test_main():
    import inspect
    import os
    import re
    import sys
    # import unittest.mock as mock

    # use patched ansible module
    if sys.version_info[0] < 3:
        import __builtin__ as builtins
    else:
        import builtins
    builtins.__ansible_module_mock_1__ = inspect.getmodule(lambda: None)
    import ansible.module_utils.basic
    real_import = builtins.__import__
    def my_import(name, *args):
        if name == 'ansible.module_utils.basic':
            return builtins.__ansible_module_mock_1__
        else:
            return real_import(name, *args)
    builtins.__import__ = my_import


# Generated at 2022-06-13 05:10:21.629115
# Unit test for function set_selection
def test_set_selection():
    set_selection(module, 'tzdata', 'selections/variant', 'select', 'none')


# Generated at 2022-06-13 05:10:31.492762
# Unit test for function set_selection
def test_set_selection():
    class FakeModule(object):
        def fail_json(self, *args, **kwargs):
            raise AssertionError('test failed')
        def run_command(self, cmd, data=None):
            return 0, '', 'success'
        def get_bin_path(self, name, required):
            return "/usr/bin/%s" % name

    pkg = "tzdata"
    question = "tzdata/Areas"
    vtype = "select"
    value = "Europe"
    unseen = False

    module = FakeModule()
    rc, _, _ = set_selection(module, pkg, question, vtype, value, unseen)

    module.assertEqual(rc, 0)

# Generated at 2022-06-13 05:10:33.162257
# Unit test for function get_selections
def test_get_selections():
    assert get_selections(module, pkg) == selections


# Generated at 2022-06-13 05:10:46.780055
# Unit test for function main
def test_main():
    test_params = {
        'name': 'local_setting',
        'question': 'question_setting',
        'vtype': 'vtype_setting',
        'value': 'value_setting',
        'unseen': False
    }

    def run_command_mock(module, cmd, data=None):
        return 0, "", ""

    def get_selections_mock(module, pkg):
        return {test_params['question']: test_params['value']}


# Generated at 2022-06-13 05:10:54.660212
# Unit test for function main
def test_main():
    # Mock the options and arguments we pass to the module, and
    # return values that would normally come from the ansible utils
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

    # Mock

# Generated at 2022-06-13 05:11:00.465282
# Unit test for function get_selections

# Generated at 2022-06-13 05:11:10.156454
# Unit test for function main
def test_main():
    import json
    import os
    import tempfile

    # This sets up the test environment appropriately
    # Run in a git checkout
    # run in a tempdir
    # set PYTHONPATH to include the module
    # Create a fake ansible modules dir
    #
    module_dir = tempfile.mkdtemp()
    module_name = 'debconf'
    module_file = module_name + '.py'

    cwd = os.getcwd()
    os.chdir(module_dir)
    os.environ['PYTHONPATH'] = module_dir
    os.environ['ANSIBLE_MODULE_UTILS'] = module_dir

    # Create the fake module
    with open(module_file, 'w') as f:
        f.write('from ansible.module_utils.basic import *')

# Generated at 2022-06-13 05:11:17.842506
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

    import doctest

    doctest.testmod()

# Hint: ansible-doc -t test -m ansible.builtin.

# Generated at 2022-06-13 05:11:25.519703
# Unit test for function set_selection
def test_set_selection():
    setsel = "/usr/bin/debconf-set-selections"
    cmd = [setsel]
    pkg = "openssh-server"
    question = "openssh-server/permit-root-login"
    vtype = "boolean"
    value = value = 'true'
    unseen = False
    data = ' '.join([pkg, question, vtype, value])

    rc, out, err = set_selection(module, pkg, question, vtype, value, unseen)
    if rc != 0:
        module.fail_json(msg=e)
    else:
        return True
