

# Generated at 2022-06-13 05:02:38.808502
# Unit test for function main
def test_main():

    # just test help
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    rc = main()
    assert rc == long(0)

    # check base case

# Generated at 2022-06-13 05:02:46.943359
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

# Generated at 2022-06-13 05:02:54.275748
# Unit test for function main
def test_main():

    # Create a mock module
    from ansible.module_utils.basic import AnsibleModule

    testmodule = AnsibleModule({
        'name': 'tzdata',
        'question': None,
        'vtype': None,
        'value': None,
        'unseen': False
    })

    # Get a list of questions and current values
    selections = get_selections(testmodule, 'tzdata')
    assert selections['tzdata/Areas'] == 'Europe'

    # Set selection
    rc, msg, e = set_selection(testmodule, 'tzdata', 'tzdata/Areas', 'select', 'Canada', False)
    assert rc == 0
    assert msg == ""
    assert e == ""

    # Get a list of questions and current values
    selections = get_selections(testmodule, 'tzdata')
   

# Generated at 2022-06-13 05:02:57.834400
# Unit test for function get_selections
def test_get_selections():
    result = get_selections(None,'tzdata')
    assert result['tzdata/Areas'] == 'America'
    assert result['tzdata/Zones/America'] == 'Argentina Cuba'

# Generated at 2022-06-13 05:02:59.219948
# Unit test for function set_selection
def test_set_selection():
    assert set_selection(module, pkg, name, vtype, value, unseen) == (rc, stdout, stderr)


# Generated at 2022-06-13 05:03:07.901869
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

# Generated at 2022-06-13 05:03:18.089255
# Unit test for function get_selections
def test_get_selections():
    from ansible.module_utils.basic import AnsibleModule
    x = AnsibleModule(
        argument_spec=dict(
        )
    )
    real_stdout, real_stderr = x.run_command("debconf-show vim | grep post | awk '{ print $3 }'")
    real_value = real_stdout.strip()
    pkg = "vim"
    null_value = "None"
    test_value = get_selections(x, pkg)['vim/post-invoke/no-upgrade-warn']
    assert test_value == real_value or real_value == null_value

# Generated at 2022-06-13 05:03:25.459259
# Unit test for function set_selection
def test_set_selection():
    from ansible.module_utils.basic import AnsibleModule
    import sys
    import os

    def test_internal_set_selection(package, question, vtype, value, unseen):
        module = AnsibleModule(argument_spec=dict(
        name=dict(type='str', required=True, aliases=['pkg']),
        question=dict(type='str', aliases=['selection', 'setting']),
        vtype=dict(type='str', choices=['boolean', 'error', 'multiselect', 'note', 'password', 'seen', 'select', 'string', 'text', 'title']),
        value=dict(type='str', aliases=['answer']),
        unseen=dict(type='bool', default=False),
        ),
        )

# Generated at 2022-06-13 05:03:26.322119
# Unit test for function get_selections
def test_get_selections():
    msg = get_selections(module, pkg)
    assert msg == (rc, out, err)

# Generated at 2022-06-13 05:03:30.600657
# Unit test for function get_selections
def test_get_selections():
    '''Unit test for function get_selections'''
    class AttributeDict(object):
        def __init__(self, name, bin_path):
            self.params = {'name': name}
            self.name = name
            self.bin_path = bin_path

    class MockModule:
        def __init__(self, bin_path, fail=False):
            self.params = {'name': 'dummy'}
            self.name = 'dummy'
            self.bin_path = bin_path
            self.fail = fail

        def run_command(self, cmd, data=None):
            if self.fail:
                return (1, '', 'failed')
            else:
                return (0, '', '')


# Generated at 2022-06-13 05:03:50.579022
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', required=True, aliases=['pkg']),
            question=dict(type='str', aliases=['selection', 'setting']),
            vtype=dict(type='str', choices=['boolean', 'error', 'multiselect', 'note', 'password', 'seen', 'select', 'string', 'text', 'title']),
            value=dict(type='str', aliases=['answer']),
        ),
        required_together=(['question', 'vtype', 'value'],),
        supports_check_mode=True,
    )

    # TODO: enable passing array of options and/or debconf file from get-selections dump
    pkg = module.params["name"]
    question = module.params["question"]
    vtype

# Generated at 2022-06-13 05:03:58.367136
# Unit test for function set_selection
def test_set_selection():
    module = AnsibleModule(argument_spec=dict(
        name=dict(type='str', required=True, aliases=['pkg']),
        question=dict(type='str', aliases=['selection', 'setting']),
        vtype=dict(type='str', choices=['boolean', 'error', 'multiselect', 'note', 'password', 'seen', 'select', 'string', 'text', 'title']),
        value=dict(type='str', aliases=['answer']),
        unseen=dict(type='bool', default=False),
    ), required_together=(['question', 'vtype', 'value'],),)
    (rc, msg, e) = set_selection(module, 'test_package', 'question', 'boolean', 'true', False)
    assert rc == 0, 'boolean vtype'

# Generated at 2022-06-13 05:03:59.080176
# Unit test for function get_selections
def test_get_selections():
    pass

# Generated at 2022-06-13 05:04:10.601655
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

    class MockModule(object):
        def __init__(self, *args, **kwargs):
            self.params = kwargs



# Generated at 2022-06-13 05:04:18.717911
# Unit test for function set_selection
def test_set_selection():
    import sys
    import ansible.module_utils.ansible_local

# Generated at 2022-06-13 05:04:24.705993
# Unit test for function set_selection
def test_set_selection():
  from ansible.module_utils.six import PY2
  from ansible.errors import AnsibleAction, AnsibleActionFail, AnsibleActionSkip
  from ansible.module_utils.basic import AnsibleModule
  module = AnsibleModule(argument_spec={})
  def run_command(*args, **kwargs):
    if kwargs['data'] == ' '.join(['tzdata', 'tzdata/Areas', 'select', 'Europe']):
      return 0, '', ''
    else:
      return 1, '', ''
  module.run_command = run_command
  rc, msg, e = set_selection(module, 'tzdata', 'tzdata/Areas', 'select', 'Europe', False)
  assert rc == 0


# Generated at 2022-06-13 05:04:30.623021
# Unit test for function set_selection
def test_set_selection():
    module = AnsibleModule(
    argument_spec = dict(
        name = dict(type = 'str', required = True, aliases = ['pkg']),
        question = dict(type = 'str', aliases = ['selection', 'setting']),
        vtype = dict(type = 'str', choices = ['boolean', 'error', 'multiselect', 'note', 'password', 'seen', 'select', 'string', 'text', 'title']),
        value = dict(type = 'str', aliases = ['answer']),
        unseen = dict(type = 'bool', default = False),
        ),
    required_together = (['question', 'vtype', 'value'],),
    supports_check_mode = True,
    )

    pkg = module.params["name"]
    question = module.params["question"]

# Generated at 2022-06-13 05:04:41.956467
# Unit test for function set_selection
def test_set_selection():
    from ansible.module_utils.common.process import get_bin_path
    setsel = get_bin_path('debconf-set-selections', True)

# Generated at 2022-06-13 05:04:47.766006
# Unit test for function main
def test_main():
    # Mock module
    module = AnsibleModule(argument_spec=dict(name=dict(type='str',
        required=True, aliases=['pkg']), question=dict(type='str',
        aliases=['selection', 'setting']), vtype=dict(type='str',
        choices=['boolean', 'error', 'multiselect', 'note', 'password',
        'seen', 'select', 'string', 'text', 'title']), value=dict(type='str',
        aliases=['answer']), unseen=dict(type='bool', default=False)))

    # Mock functions
    def get_selections(module, pkg=None):
        return {'question1': 'value1'}


# Generated at 2022-06-13 05:04:59.395519
# Unit test for function set_selection
def test_set_selection():
    from ansible.module_utils._text import to_text
    from ansible.module_utils.basic import AnsibleModule
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

# Generated at 2022-06-13 05:05:15.704233
# Unit test for function main
def test_main():
    from ansible.module_utils.debconf import DebconfModule
    import sys

    module = DebconfModule(argument_spec={})
    module.name = 'localepurge'
    module.params['pkg'] = module.name
    module.params['question'] = None
    module.params['vtype'] = None
    module.params['value'] = None

    sys.argv = ['ansible-test', 'set_selection', '--name', 'localepurge']
    module.main()

# Generated at 2022-06-13 05:05:24.069262
# Unit test for function get_selections
def test_get_selections():  # noqa
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

# Generated at 2022-06-13 05:05:28.272378
# Unit test for function main
def test_main():
    # Test with a selected question, no vtype or value
    with pytest.raises(AnsibleFailJson):
        module = FakeModule({'name': 'foo', 'question': 'bar', 'vtype': None, 'value': None})
        main()

    # Test with no selected question and no vtype or value
    module = FakeModule({'name': 'foo', 'question': None, 'vtype': None, 'value': None})
    result = main()
    len(result['current']) == 1

    # Test with no selected question and a vtype and value
    with pytest.raises(AnsibleFailJson):
        module = FakeModule({'name': 'foo', 'question': None, 'vtype': 'bar', 'value': 'bar'})
        main()

    # Test with changes

# Generated at 2022-06-13 05:05:38.984404
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
    pkg = 'tzdata'
    assert get_selections(module, pkg)

# Generated at 2022-06-13 05:05:49.574581
# Unit test for function get_selections

# Generated at 2022-06-13 05:05:56.085451
# Unit test for function get_selections
def test_get_selections():
    class MockModule(object):
        def __init__(self, rc, out, err):
            self.rc = rc
            self.out = out
            self.err = err

        def run_command(self, _):
            return (self.rc, self.out, self.err)

    # Expect that getting the selections from the locales package should
    # return two selections.
    module = MockModule(
        0,
        'locales/locales_to_be_generated multiselect en_US.UTF-8 UTF-8, fr_FR.UTF-8 UTF-8\n\
locales/default_environment_locale select fr_FR.UTF-8\n',
        ''
    )

    selections = get_selections(module, 'locales')
    assert len(selections) == 2
    assert selections

# Generated at 2022-06-13 05:06:00.615350
# Unit test for function get_selections
def test_get_selections():
    module = AnsibleModule(argument_spec={}, supports_check_mode=False)
    result = get_selections(module, "tzdata")
    assert isinstance(result, dict)
    assert result['tzdata/Areas'] == 'Europe'


# Generated at 2022-06-13 05:06:03.783031
# Unit test for function get_selections
def test_get_selections():
    assert_equal(get_selections(module, pkg), selections)

# Generated at 2022-06-13 05:06:16.918354
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

# Generated at 2022-06-13 05:06:21.791752
# Unit test for function set_selection
def test_set_selection():
    from ansible.module_utils._text import to_native
    from ansible.module_utils.basic import AnsibleModule

    cmd_exists_map.update({'debconf-get-selections': True})
    module_args = dict(
        name='locales',
        question='locales/default_environment_locale',
        vtype='select',
        value='fr_FR.UTF-8',
        unseen=False
    )
    module = AnsibleModule(argument_spec=dict())
    result = set_selection(module, module_args['name'], module_args['question'], module_args['vtype'], module_args['value'], module_args['unseen'])
    assert result[0] != 0

# Generated at 2022-06-13 05:06:53.169634
# Unit test for function set_selection
def test_set_selection():
    mod = AnsibleModule(argument_spec=dict(
        name=dict(type='str', required=True, aliases='pkg'),
        question=dict(type='str', aliases=['selection', 'setting']),
        vtype=dict(type='str', choices=['boolean', 'error', 'multiselect', 'note', 'password', 'seen', 'select', 'string', 'text', 'title']),
        value=dict(type='str', aliases=['answer']),
        unseen=dict(type='bool', default=False),
    ),
                        required_together=(['question', 'vtype', 'value'],),
                        supports_check_mode=True,
                        )

    set_selection(mod, 'debconf', 'debconf/frontend', 'select', 'noninteractive', False)

# Generated at 2022-06-13 05:07:07.012992
# Unit test for function get_selections
def test_get_selections():
    import os
    import tempfile
    import textwrap

    # setup input
    pkg = 'test_package'

    list_input = textwrap.dedent('''
    * test_package/question1: value1
    * test_package/question2: value2
    * test_package/question3: value3
    ''')[1:]

    # setup and run
    test_module = AnsibleModule(argument_spec={})
    test_module.get_bin_path = lambda tool, required=None: 'debconf-show'
    real_run_command = test_module.run_command


# Generated at 2022-06-13 05:07:15.066083
# Unit test for function main
def test_main():
    # pylint: disable=C0103
    data = dict(
        name='locales',
        question='locales/default_environment_locale',
        vtype='select',
        value='fr_FR.UTF-8',
        unseen=False,
    )
    # create a fake module
    fake_module = AnsibleModule(argument_spec={
        'name': dict(type='str', required=True),
        'question': dict(type='str'),
        'vtype': dict(type='str'),
        'value': dict(type='str'),
        'unseen': dict(type='bool', default=False),
    }, required_together=(['question', 'vtype', 'value'],),
        supports_check_mode=True)

# Generated at 2022-06-13 05:07:27.252556
# Unit test for function set_selection
def test_set_selection():
    class Module(object):
        def __init__(self, name, get_bin_path_return, run_command_return,
                           run_command_rc, run_command_stdout, run_command_stderr):
            self.name = name
            self.get_bin_path_return = get_bin_path_return
            self.run_command_return = run_command_return
            self.run_command_rc = run_command_rc
            self.run_command_stdout = run_command_stdout
            self.run_command_stderr = run_command_stderr

        def get_bin_path(self, cmd, required):
            return self.get_bin_path_return


# Generated at 2022-06-13 05:07:38.172663
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

# Generated at 2022-06-13 05:07:49.389078
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

# Generated at 2022-06-13 05:07:57.505465
# Unit test for function set_selection
def test_set_selection():
    import os
    from ansible.module_utils.debconf import set_selection
    fh = open("ts.txt", "w")
    fh.write("test\n")
    fh.close()

    if os.path.isfile("ts.txt"):
        os.system("rm -f ts.txt")
        os.system("rm -f ts.txt")
    rc, msg, e = set_selection(module=None, pkg="test", question="test", vtype="boolean", value="true", unseen=False)
    assert rc == 0
    assert msg == ""
    assert e == ""
    assert os.path.isfile("ts.txt")


# Generated at 2022-06-13 05:08:07.261594
# Unit test for function main
def test_main():
    mod = AnsibleModule(
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
    mod.run_command = lambda args, data: (0, 'test', '')

    question = 'test'

# Generated at 2022-06-13 05:08:17.152972
# Unit test for function get_selections
def test_get_selections():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.ansible_release import __version__ as ansible_version
    import sys

    if sys.version_info[0] < 3:
        input_spec = {
            "name": {"type": "str", "required": True, "aliases": ["pkg"]}
        }
    else:
        input_spec = {
            "name": {"type": "str", "required": True, "aliases": ["pkg"]}
        }

    module = AnsibleModule(
        argument_spec=input_spec,
        required_together=[["question", "vtype", "value"]],
    )

    pkg = 'tzdata'

    result = get_selections(module, pkg)
    # assert False

# Generated at 2022-06-13 05:08:27.809256
# Unit test for function get_selections
def test_get_selections():
    import debconf
    debconf.run("set debconf/priority critical")
    debconf.run("set debconf/frontend critical")
    debconf.set("test-debconf-module/foo", "bar")
    debconf.set("test-debconf-module/bar", "baz")
    debconf.set("test-debconf-module/baz", "qux")
    debconf.set("test-debconf-module/qux", "quux")
    debconf.run("set debconf/priority critical")
    debconf.run("set debconf/frontend critical")

    mock_module = MockModule()

    input = dict(name="test-debconf-module")

    selections = dict(foo="bar", bar="baz", baz="qux", qux="quux")


# Generated at 2022-06-13 05:09:15.424798
# Unit test for function main
def test_main():
    import filecmp
    import os
    import shutil
    import subprocess
    import tempfile
    import yaml

    import ansible.utils

    module_name = 'ansible.builtin.debconf'
    module = __import__(module_name)
    module = getattr(module, module_name)

    with tempfile.TemporaryDirectory() as tmpdir:
        fn = tmpdir + '/test_main.yaml'
        fp = open(fn, 'w')

        fp.write('---\n')
        fp.write('- hosts: localhost\n')
        fp.write('  tasks:\n')
        fp.write('    - name: Test main\n')

# Generated at 2022-06-13 05:09:26.017497
# Unit test for function set_selection

# Generated at 2022-06-13 05:09:31.400060
# Unit test for function main
def test_main():
    args = dict(pkg='tzdata', question='tzdata/Areas', vtype='select', value='America')
    result = {}
    module = MagicMock()
    module.params = dict(pkg=args['pkg'])
    module.check_mode = False
    module._diff = False
    module.run_command = run_command
    module.get_bin_path = get_bin_path
    module.fail_json = fail_json
    module.exit_json = exit_json
    module.fail_json = fail_json
    module.exit_json = exit_json

    main()

    # Test if debconf-show is called
    module.run_command.assert_called()

    # Test if debconf-set-selections is called
    module.run_command.assert_called()

# Generated at 2022-06-13 05:09:34.443710
# Unit test for function get_selections
def test_get_selections():
    testAnsibleModule = AnsibleModule(argument_spec={})
    selections = get_selections(testAnsibleModule, "")
    assert selections == {}

# Generated at 2022-06-13 05:09:37.149466
# Unit test for function set_selection
def test_set_selection():
    assert set_selection(pkg, question, vtype, value, unseen) == rc, "Error in set_selection function"


# Generated at 2022-06-13 05:09:40.990171
# Unit test for function set_selection
def test_set_selection():
    module = AnsibleModule()
    rc, msg, e = set_selection(module, "locales", "locales/default_environment_locale", "select", "fr_FR.UTF-8", False)
    assert rc == 0

# Generated at 2022-06-13 05:09:47.744365
# Unit test for function main
def test_main():
    import sys
    import json
    import os.path
    from ansible.module_utils import basic

    if not os.path.isfile('/usr/bin/debconf-show'):
        sys.exit(0)


# Generated at 2022-06-13 05:09:54.224366
# Unit test for function set_selection
def test_set_selection():
    # set_selection(module, pkg, question, vtype, value, unseen):

    # Test case 1:
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

# Generated at 2022-06-13 05:10:03.168992
# Unit test for function set_selection
def test_set_selection():
    from ansible.module_utils import basic
    import os
    from ansible.module_utils.six import StringIO
    from ansible.module_utils._text import to_bytes
    import shutil

    tmpdir = "/tmp/ansible_%s" % os.getpid()
    os.environ['DEBIAN_FRONTEND'] = 'noninteractive'
    module = basic.AnsibleModule(argument_spec={})
    module.CHECK_MODE = False
    module.no_log = True
    module._diff = True
    setsel = "/tmp/setsel"
    os.makedirs(tmpdir)
    with open(setsel, "w") as f:
        f.write("#! /bin/sh\n")
        f.write("set -ex\n")

# Generated at 2022-06-13 05:10:09.460496
# Unit test for function get_selections
def test_get_selections():
    try:
      import unittest2 as unittest
    except ImportError:
      import unittest
    import ansible.module_utils.debconf as dc
    module = unittest.mock.Mock()

    # Mock module.run_command
    module.run_command = unittest.mock.Mock()

# Generated at 2022-06-13 05:12:00.836621
# Unit test for function main
def test_main():
    import sys
    import json
    import os
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common import get_platform
    from ansible.module_utils.urls import urllib_request
    from ansible.module_utils import action_common_attributes
    from ansible.module_utils import debconf
    from mock import patch, Mock

    # Get the function we are testing
    main = debconf.main

    # Save the original value of sys.modules
    orig_sys_modules = sys.modules.copy()

    # Create a temporary testing directory and copy the resource file to it.
    temp_dir = tempfile.mkdtemp

# Generated at 2022-06-13 05:12:05.304456
# Unit test for function set_selection
def test_set_selection():
    module = AnsibleModule(argument_spec=dict(question=dict(type='str'),
                                              vtype=dict(type='str', choices=['boolean', 'error', 'multiselect', 'note', 'password', 'seen', 'select', 'string', 'text', 'title']),
                                              value=dict(type='str'),
                                              unseen=dict(type='bool', default=False),))
    pkg = 'test_package'
    question = 'test_question'
    vtype = 'string'
    value = 'test_value'
    unseen = False
    if unseen:
        cmd = ['/usr/bin/debconf-set-selections', '-u']
    else:
        cmd = ['/usr/bin/debconf-set-selections']


# Generated at 2022-06-13 05:12:15.193196
# Unit test for function set_selection
def test_set_selection():

    class Mock_Run_Command:
        def __init__(self, rc, out, err):
            self.rc = rc
            self.out = out
            self.err = err

        def run_command(self, cmd, data=None):
            return (self.rc, self.out, self.err)

    rc = 0
    out = "success"
    err = "error"
    cmd = ['debconf-set-selection', 'pkg', 'question', 'vtype', 'value']

    # Test with rc = 0
    run_command = Mock_Run_Command(rc, out, err)
    assert set_selection(run_command, 'pkg', 'question', 'vtype', 'value', False) == (rc, out, err)

    # Test with rc = 1
    rc = 1

# Generated at 2022-06-13 05:12:21.729183
# Unit test for function set_selection
def test_set_selection():
    f = set_selection('main.set_selection')
    data = Data('True')
    rc, out, err = f(pkg='tzdata', question='tzdata/Zonenames', value=data, vtype='boolean', unseen=True)
    assert rc == 0
    assert out == ''
    assert err == ''
    data = Data('False')
    rc, out, err = f(pkg='tzdata', question='tzdata/Zonenames', value=data, vtype='boolean', unseen=True)
    assert rc == 0
    assert out == ''
    assert err == ''
    data = Data('foo')
    rc, out, err = f(pkg='tzdata', question='tzdata/Zonenames', value=data, vtype='boolean', unseen=True)
    assert rc != 0
    assert out == ''