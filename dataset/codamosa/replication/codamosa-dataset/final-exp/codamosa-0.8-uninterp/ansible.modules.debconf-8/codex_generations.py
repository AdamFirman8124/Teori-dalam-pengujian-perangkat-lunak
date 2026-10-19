

# Generated at 2022-06-13 05:02:39.646856
# Unit test for function set_selection
def test_set_selection():
    import sys
    import os
    test_file = open('/tmp/unit_tests_debconf', 'w')
    test_file.write("this is a test file")
    test_file.close()
    test_args = {'name': 'fake_package_name',
                 'question': 'fake_setting_name',
                 'vtype': 'fake_setting_type',
                 'value': 'fake_setting_value',
                 'unseen': 'unset'}
    sys.argv = [__file__,
                '-vvv',
                '-i',
                '%s,' % os.path.join(os.path.dirname(__file__), 'test_ansible_module_debconf.py'),
                '--',
                'fake_file']

# Generated at 2022-06-13 05:02:47.793297
# Unit test for function main
def test_main():
    module = AnsibleModule(argument_spec={
        'name': dict(type='str', required=True, aliases=['pkg']),
        'question': dict(type='str', aliases=['selection', 'setting']),
        'vtype': dict(type='str',
                      choices=['boolean', 'error', 'multiselect', 'note', 'password', 'seen', 'select', 'string',
                               'text', 'title']),
        'value': dict(type='str', aliases=['answer']),
        'unseen': dict(type='bool', default=False)
    }, required_together=(['question', 'vtype', 'value'],), supports_check_mode=True)

    assert module.params["name"] is not None
    result = get_selections(module, module.params["name"])

# Generated at 2022-06-13 05:02:55.516414
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

    pkg = 'ansible'
    question = 'ansible/something'
    vtype = 'something'

# Generated at 2022-06-13 05:02:56.196626
# Unit test for function get_selections
def test_get_selections():
    assert True

# Generated at 2022-06-13 05:03:05.433058
# Unit test for function main
def test_main():
    import ansible.module_utils.basic as basic
    import tempfile
    import os
    import shutil
    import sys

    class Args(object):
        pass

    class Module(object):
        def __init__(self):
            self.args = Args()
            self.params = {}
            self.run_command_called = 0
            self.run_command_rc = 0
            self.run_command_msg = ""
            self.run_command_err = ""
        def run_command(self, cmd, data=None):
            self.run_command_called += 1
            return self.run_command_rc, self.run_command_msg, self.run_command_err
        def get_bin_path(self, cmd, required, opt_dirs=[]):
            return cmd

# Generated at 2022-06-13 05:03:18.944867
# Unit test for function main
def test_main():
    # Unit test for function main
    def test_main():
        # Dummy input
        request = {}
        request['name'] = 'locales'
        request['question'] = 'locales/default_environment_locale'
        request['vtype'] = 'select'
        request['value'] = 'fr_FR.UTF-8'
        request['unseen'] = 'False'

        module_msg = {}
        module_msg['name'] = request['name']
        module_msg['question'] = request['question']
        module_msg['vtype'] = request['vtype']
        module_msg['value'] = request['value']
        module_msg['unseen'] = request['unseen']

        msg = {}
        msg['changed'] = True

# Generated at 2022-06-13 05:03:24.472555
# Unit test for function get_selections
def test_get_selections():
    import unittest

    class MockModule(object):
        # This class is used to mock the return code and out/err
        # of AnsibleModule
        class MockRunCommand(object):
            def __init__(self, rc, out, err):
                self.rc = rc
                self.out = out
                self.err = err

            def __call__(self, cmd, data=None):
                return self.rc, self.out, self.err

        def __init__(self, rc, out, err):
            self.run_command = self.MockRunCommand(rc, out, err)


# Generated at 2022-06-13 05:03:28.128434
# Unit test for function get_selections
def test_get_selections():
    expected = {'tzdata/Areas': 'Europe', 'tzdata/Zones/Europe': 'Amsterdam'}

    assert get_selections(None, 'tzdata') == expected


# Generated at 2022-06-13 05:03:40.705448
# Unit test for function main
def test_main():
    import os
    import sys
    import io
    import os.path
    import pytest
    from . import debconf

    # Build path to test data
    current_dir = os.path.dirname(os.path.realpath(__file__))
    data_dir = os.path.join(current_dir, 'data')
    procenv_debconf_output = os.path.join(data_dir, 'procenv_debconf_output')
    procenv_debconf_output_changed = os.path.join(data_dir, 'procenv_debconf_output_changed')

    # Setup functions for mocking
    def mock_run_command(cmd, data):
        return 0, "mock_command_ran", ""

    # Build mock module

# Generated at 2022-06-13 05:03:47.835924
# Unit test for function main
def test_main():
    module_args = {
        "name": "tzdata",
        "question": None,
        "vtype": None,
        "value": None,
        "unseen": False
    }

    module = AnsibleModule(argument_spec=module_args)

    selections = main()

    assert(selections['msg'] == '')
    assert(selections['changed'] == False)
    assert(selections['current'] is not None)

# Generated at 2022-06-13 05:04:08.753597
# Unit test for function get_selections
def test_get_selections():
    test_input = [
        "locales/default_environment_locale: fr_FR.UTF-8",
        "locales/locales_to_be_generated: en_US.UTF-8 UTF-8, fr_FR.UTF-8 UTF-8",
        "shared/accepted-oracle-license-v1-1: true"
    ]

    test_output = {
        "locales/default_environment_locale": "fr_FR.UTF-8",
        "locales/locales_to_be_generated": "en_US.UTF-8 UTF-8, fr_FR.UTF-8 UTF-8",
        "shared/accepted-oracle-license-v1-1": "true"
    }

    assert test_output == get_selections(test_input)

# Generated at 2022-06-13 05:04:20.324483
# Unit test for function main
def test_main():
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

    # test_module is a AnsibleModule Object
    test_module.check_mode = False
    # run_command will be mocked

# Generated at 2022-06-13 05:04:22.652737
# Unit test for function get_selections
def test_get_selections():
    selections = get_selections(module, 'tzdata')
    assert selections['tzdata/Zones/Etc'] == 'UTC'


# Generated at 2022-06-13 05:04:29.760133
# Unit test for function set_selection
def test_set_selection():
    import json
    import os

    test_data_dir = os.path.join(os.path.dirname(__file__), 'test_data')
    test_input_data = os.path.join(test_data_dir, 'test_ansible_module_input.json')
    test_input_data_json = open(test_input_data, 'rb').read()

    module_args = json.loads(test_input_data_json)

    pkg = module_args["name"]
    question = module_args["question"]
    vtype = module_args["vtype"]
    value = module_args["value"]
    unseen = module_args["unseen"]

# Generated at 2022-06-13 05:04:34.415526
# Unit test for function main
def test_main():

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

    pkg = "locales"
    question = "locales/default_environment_locale"

# Generated at 2022-06-13 05:04:44.122439
# Unit test for function set_selection
def test_set_selection():
    import os
    import tempfile
    tmpfile = tempfile.mkstemp()[1]
    # create a fake module and params to test set_selection
    set_module = AnsibleModule(argument_spec=dict())
    set_module.params = {'value': 'test', 'vtype': 'note', 'pkg': 'testpkg', 'unseen': 'false'}
    rc, msg, e = set_selection(set_module, 'testpkg', 'testquestion', 'note', 'test', 'false')
    assert rc == 0
    assert_msg = 'stdout:wrote testpkg testquestion note test'
    assert msg == assert_msg
    assert e == ''
    os.remove(tmpfile)

    # create a fake module and params to test set_selection

# Generated at 2022-06-13 05:04:45.079957
# Unit test for function get_selections
def test_get_selections():
    pass

# Generated at 2022-06-13 05:04:57.685010
# Unit test for function get_selections
def test_get_selections():
    class ModuleFailException(Exception):
        pass
    class AnsibleModule(object):
        def __init__(self):
            pass
        class FailJsonException(Exception):
            pass
        def get_bin_path(self, command, required=False, opt_dirs=None):
            if command == 'debconf-show':
                return '/usr/bin/debconf-show'
            if command == 'debconf-utils':
                return '/usr/bin/debconf-get-selections'
            return None #fail if not found

# Generated at 2022-06-13 05:05:02.233555
# Unit test for function set_selection
def test_set_selection():
    import tempfile
    import os
    import shutil

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

    pkg = "testpackage123"
    question = "testquestion456"


# Generated at 2022-06-13 05:05:13.184799
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

# Generated at 2022-06-13 05:05:40.392292
# Unit test for function get_selections
def test_get_selections():
    import os
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

# Generated at 2022-06-13 05:05:47.313343
# Unit test for function get_selections
def test_get_selections():
    from ansible_collections.ansible.builtin.modules.plugins.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', required=True, aliases=['pkg'])
        ),
        supports_check_mode=True
    )

    result = get_selections(module, "debconf")

    assert(isinstance(result, dict))
    assert("debconf/frontend" in result)



# Generated at 2022-06-13 05:05:54.840187
# Unit test for function get_selections
def test_get_selections():
    fake_module = AnsibleModule(
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

# Generated at 2022-06-13 05:06:04.762257
# Unit test for function get_selections
def test_get_selections():
    selections = {
        'localepurge/quickndirtycalc': 'true',
        'localepurge/use-dpkg-feature': 'false',
        'golang-github-gorilla-websocket/install': '',
        'locales/locales_to_be_generated': '',
        'localepurge/quickndirtycalc': '',
        'localepurge/verbose': '',
    }

    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True,
    )

    # inject a test implementation for module.run_command
    def fake_run_command(cmd, data=None):
        return 0, '', ''

    module.run_command = fake_run_command

# Generated at 2022-06-13 05:06:06.674567
# Unit test for function get_selections
def test_get_selections():
    assert get_selections('tzdata') is not None


# Generated at 2022-06-13 05:06:17.926216
# Unit test for function get_selections
def test_get_selections():
    test_data = '''
* apt-daily/upgrade-packages:
  <No value set>
* apt-daily/upgrade-error-is-fatal:
  <No value set>
* apt-daily/upgrade-error:
  <No value set>
* apt-daily/upgrade-autoclean:
  <No value set>
* apt-daily/upgrade-autoremovable:
  <No value set>
* tzdata/Areas:
  Etc
* tzdata/Zones/Etc:
  UTC

'''

# Generated at 2022-06-13 05:06:19.817228
# Unit test for function get_selections
def test_get_selections():
    pkg = "tzdata"
    get_selections(None, pkg)


# Generated at 2022-06-13 05:06:20.379694
# Unit test for function set_selection
def test_set_selection():
    pass

# Generated at 2022-06-13 05:06:33.584636
# Unit test for function get_selections
def test_get_selections():
    module = AnsibleModule(argument_spec={})
    module.get_bin_path = lambda x, y: x
    module.run_command = lambda x: (0, "* bash/bashrc-sys:\n* bash/readline-enabled:\n* bash/umask:\n* debconf/priority:\n* dash/sh:\n* locales/default_environment_locale: fr_FR.UTF-8\n* locales/locales_to_be_generated: \n", "")

# Generated at 2022-06-13 05:06:34.747696
# Unit test for function set_selection
def test_set_selection():
    assert(set_selection(pkg, question, vtype, value, unseen) == (False, 'Successful', ''))

# Generated at 2022-06-13 05:07:28.762472
# Unit test for function set_selection
def test_set_selection():
    import tempfile
    import shutil
    import os
    import subprocess
    import select

    def _exec_set_selection(question, vtype, value):
        debconf_dir = tempfile.mkdtemp()
        debconf_socket = os.path.join(debconf_dir, 'socket')
        os.mkdir(os.path.join(debconf_dir, 'conf'))

        cmd = ['debconf-communicate', '-fnoninteractive', '-o', 'Dsocket='+debconf_socket]
        new_env = os.environ.copy()
        new_env['DEBIAN_PRIORITY'] = 'critical'
        new_env['DEBCONF_DIR'] = debconf_dir

# Generated at 2022-06-13 05:07:40.431379
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils import action
    from ansible.module_utils import debconf

    # Tests for function get_selections
    module = basic.AnsibleModule()
    module.run_command = action.run_command
    module.fail_json = action.fail_json
    module.get_bin_path = action.get_bin_path

    # test for error
    pkg = 'vim'
    rc = 1
    out = ''
    err = 'foo'
    module.run_command = action.run_command
    action.run_command = lambda cmd, data=None, check_rc=False: (rc, out, err)

    result = debconf.get_selections(module, pkg)
    assert result == {}
    assert module.fail_

# Generated at 2022-06-13 05:07:41.124886
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-13 05:07:44.474725
# Unit test for function get_selections
def test_get_selections():
    pkg = "tzdata"
    selections = get_selections(module, pkg)
    assert selections is not None
    assert len(selections) > 0
    assert selections[u'clock-setup/utc'] == 'true'


# Generated at 2022-06-13 05:07:47.782253
# Unit test for function get_selections
def test_get_selections():
    module = AnsibleModule(argument_spec=[])
    result = get_selections(module, "tzdata")
    assert result
    assert type(result) is dict
    assert "tzdata/Zones/Etc" in result

# Generated at 2022-06-13 05:07:51.244842
# Unit test for function set_selection

# Generated at 2022-06-13 05:07:53.673393
# Unit test for function get_selections
def test_get_selections():
    assert get_selections(['tzdata', 'tzdata/Areas', 'select', 'Europe']) == ['tzdata', 'tzdata/Areas', 'select', 'Europe']

# Generated at 2022-06-13 05:07:58.369348
# Unit test for function set_selection
def test_set_selection():
    changed = False
    msg = ""
    print("Unit test for function set_selection")
    rc, msg, e = set_selection()

    if rc:
        print("Unit test fail for function set_selection")
    else:
        print("Unit test success for function set_selection")

# Generated at 2022-06-13 05:07:58.939498
# Unit test for function get_selections
def test_get_selections():
    pass # TODO

# Generated at 2022-06-13 05:07:59.457853
# Unit test for function set_selection
def test_set_selection():
    pass

# Generated at 2022-06-13 05:09:13.440828
# Unit test for function get_selections
def test_get_selections():
    # Some basic imports
    import sys
    import os
    # Importing class
    from ansible.module_utils.basic import AnsibleModule
    # Assigning argument dictionary
    module_args = {}
    module_args['name'] = 'tzdata'
    module_args['question'] = None
    module_args['vtype'] = None
    module_args['value'] = None
    module_args['unseen'] = False
    # Setting up object

# Generated at 2022-06-13 05:09:24.129886
# Unit test for function set_selection
def test_set_selection():
    import subprocess
    from ansible.module_utils.basic import AnsibleModule

    def run_command(cmd, data=None, check_rc=True, close_fds=True, executable=None, data_encoding='UTF-8', path_prefix=None, cwd=None):
        p = subprocess.Popen(
            cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=close_fds, executable=executable, cwd=cwd
        )
        if data is not None:
            data = to_bytes(data, errors=data_encoding)
            rc = p.communicate(data)[0]
            if check_rc and p.returncode != 0:
                raise Exception("")

# Generated at 2022-06-13 05:09:32.166628
# Unit test for function set_selection
def test_set_selection():
    import os
    from ansible.module_utils.basic import AnsibleModule


# Generated at 2022-06-13 05:09:37.504271
# Unit test for function get_selections
def test_get_selections():
    from .module_utils.debconf import get_selections
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec={})
    pkg = "dummy-package"
    results = get_selections(module, pkg)
    assert results == {"dummy": "example"}

# Generated at 2022-06-13 05:09:48.322928
# Unit test for function set_selection
def test_set_selection():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', required=False, aliases=['pkg']),
            question=dict(type='str', aliases=['selection', 'setting']),
            vtype=dict(type='str', choices=['boolean', 'error', 'multiselect', 'note', 'password', 'seen', 'select', 'string', 'text', 'title']),
            value=dict(type='str', aliases=['answer']),
            unseen=dict(type='bool', default=False),
        ),
        required_together=(['question', 'vtype', 'value'],),
        supports_check_mode=True,
    )
    pkg = 'ansible'
    question = 'ansible/foo'
    vtype = 'string'
    value = 'bar'

# Generated at 2022-06-13 05:09:54.586515
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
    mock_pkg = 'dummy-package'
    mock_question = 'dummy-question'
    mock_vtype = 'string'

# Generated at 2022-06-13 05:09:58.788812
# Unit test for function get_selections
def test_get_selections():
    try:
        from ansible.module_utils.basic import AnsibleModule
    except ImportError:
        print("ansible is not installed")

    module = AnsibleModule(argument_spec={})
    pkg = 'tzdata'
    selections = get_selections(module, pkg)
    assert selections['tzdata/Areas'] == 'Europe'



# Generated at 2022-06-13 05:10:06.849882
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

# Generated at 2022-06-13 05:10:15.864048
# Unit test for function get_selections
def test_get_selections():
    # set up module object
    set_module_args(dict(name="tzdata", question="tzdata/Zones/Etc", vtype="string", value="UTC"))
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', required=True, aliases=['pkg']),
            question=dict(type='str', aliases=['selection', 'setting']),
            vtype=dict(type='str', choices=['boolean', 'error', 'multiselect', 'note', 'password', 'seen', 'select', 'string', 'text', 'title']),
            value=dict(type='str', aliases=['answer']),
        ),
        required_together=(['question', 'vtype', 'value'],),
        supports_check_mode=False,
    )
    pkg = module

# Generated at 2022-06-13 05:10:28.871255
# Unit test for function set_selection
def test_set_selection():
    import unittest
    import os
    import io
    import sys
    import json

    class TestDebconfModule(unittest.TestCase):
        def setUp(self):
            self.package = 'fortesting'
            self.question = 'bool_question'
            self.vtype = 'boolean'
            self.value = 'true'
            self.unseen = False
            self.selections = {
                    "bool_question": "false",
                    "int_question": "9929",
                    "multiselect_question": "b,c,d,f",
                    "password_question": "password_set",
                    "select_question": "a",
                    "string_question": "select_a",
                    "text_question": "this is text",
                    "title_question": "title"
            }