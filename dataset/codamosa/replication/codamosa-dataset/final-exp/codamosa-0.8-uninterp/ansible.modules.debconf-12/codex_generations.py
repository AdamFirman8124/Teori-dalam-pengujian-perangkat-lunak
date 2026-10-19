

# Generated at 2022-06-13 05:02:39.906705
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
    pkg = "debconf-test"
    question = "debconf-test/test-question"
    vtype = "string"
    value = "true"

# Generated at 2022-06-13 05:02:48.038722
# Unit test for function main
def test_main():
    # Importing here for added flexibility to test
    import ansible.module_utils.action._debconf as module

    # What we're testing in these tests
    module.get_selections = lambda m, p: {'question':'existing value'}
    module.set_selection = lambda m, p, q, vt, v, u: (0, "Unit test", "")

    # Test when checking but not changing
    result = module.main(dict(name='test-pkg', check_mode=True))
    assert result['changed'] is False
    assert result['msg'] == "Unit test"
    assert result['current'] == {'question': 'existing value'}

    # Test when not changing
    result = module.main(dict(name='test-pkg'))
    assert result['changed'] is False
    assert result['msg']

# Generated at 2022-06-13 05:02:50.735940
# Unit test for function set_selection
def test_set_selection():
    # Don't do anything
    rc, msg, e = set_selection(module, pkg, question, vtype, value, unseen)

# Generated at 2022-06-13 05:02:57.168327
# Unit test for function get_selections
def test_get_selections():
    pkg = 'tzdata'
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', required=True,  aliases=['pkg']),
            question=dict(type='str', aliases=['selection', 'setting']),
            vtype=dict(type='str',choices=['boolean', 'error', 'multiselect', 'note', 'password', 'seen', 'select', 'string', 'text', 'title']),
            value=dict(type='str', aliases=['answer']),
            unseen=dict(type='bool', default=False),
        ),
        required_together=(['question', 'vtype', 'value'],),
        supports_check_mode=True,
    )
    selections = get_selections(module, pkg)

# Generated at 2022-06-13 05:03:06.399242
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

# Generated at 2022-06-13 05:03:15.640200
# Unit test for function set_selection
def test_set_selection():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule({}, supports_check_mode=True, )
    rc, out, err = set_selection(module, 'locales', 'locales/locales_to_be_generated', 'multiselect', 'en_US.UTF-8 UTF-8, fr_FR.UTF-8 UTF-8', True)
    my_out = ''
    assert my_out == out
    assert rc == 0
    assert err == ''

# Generated at 2022-06-13 05:03:24.737370
# Unit test for function get_selections
def test_get_selections():
    class FakeModule(object):
        def __init__(self):
            self.params = {'name': 'cups-daemon', 'question': None,
                           'vtype': None, 'value': None, 'unseen': False}
            self._ansible_builtin_added_checks = True


# Generated at 2022-06-13 05:03:27.015757
# Unit test for function get_selections
def test_get_selections():
    from ansible.modules.packaging.os.debconf_get_selections import get_selections
    input = {'name' : 'testpkg',
             'question' : 'testpkg/question1',
             'vtype': 'text',
             'value': 'testvalue',
             'unseen': False}
    module = get_selections(input)


# Generated at 2022-06-13 05:03:39.623886
# Unit test for function set_selection
def test_set_selection():
    assert set_selection('pkg', 'question', 'string', 'answer') == "debconf-set-selections", 'pkg question string answer'
    assert set_selection('pkg', 'question', 'boolean', 'answer') == "debconf-set-selections", 'pkg question boolean answer'
    assert set_selection('pkg', 'question', 'string', 'answer', True) == "debconf-set-selections -u", 'pkg question string answer'
    assert set_selection('pkg', 'question', 'boolean', 'answer', True) == "debconf-set-selections -u", 'pkg question boolean answer'
    assert set_selection('pkg', 'question', 'string', 'answer', False) == "debconf-set-selections", 'pkg question string answer'

# Generated at 2022-06-13 05:03:49.977895
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

    return module


# Generated at 2022-06-13 05:04:08.623740
# Unit test for function set_selection
def test_set_selection():
    module = type('', (), {})()
    module.run_command = lambda *args, **kwargs: (0, '', '')

    pkg = 'foo'
    question = 'bar'
    vtype = 'string'
    value = 'baz'

    # Test with no arguments
    rc, msg, err = set_selection(module, pkg, question, vtype, value, False)
    assert rc == 0, 'Return code must be 0 when no error occurs'
    assert len(msg) == 0, 'Stdout must be empty when no error occurs'
    assert len(err) == 0, 'Stderr must be empty when no error occurs'

# Generated at 2022-06-13 05:04:20.174250
# Unit test for function set_selection
def test_set_selection():
    from ansible.module_utils.basic import AnsibleModule
    import os
    import shutil
    from tempfile import mkdtemp

    def setUpModule():
        self.tempdir = mkdtemp()
        self.addCleanup(shutil.rmtree, self.tempdir)

    setUpModule()
    # dummy AnsibleModule
    module = AnsibleModule(argument_spec={})
    module.params['name'] = 'debconf_selections'
    module.params['question'] = 'foo'
    module.params['value'] = 'bar'
    module.params['vtype'] = 'string'

    # dummy bin directory
    bin_dir = os.path.join(self.tempdir, 'bin')
    os.mkdir(bin_dir)

# Generated at 2022-06-13 05:04:27.731397
# Unit test for function set_selection
def test_set_selection():

    setsel = set_selection('debconf-set-selections', True)
    pkg = 'locales'
    question = 'locales/default_environment_locale'
    vtype = 'select'
    value = 'fr_FR.UTF-8'
    unseen = False
    cmd = [setsel]
    if unseen:
        cmd.append('-u')

    if vtype == 'boolean':
        if value == 'True':
            value = 'true'
        elif value == 'False':
            value = 'false'
    data = ' '.join([pkg, question, vtype, value])

    return module.run_command(cmd, data=data)

    assert True


# Generated at 2022-06-13 05:04:41.082493
# Unit test for function set_selection
def test_set_selection():
    from ansible.module_utils.basic import AnsibleModule as BAModule
    import ansible.module_utils.debconf as DebconfModule
    import os
    import tempfile

    def fake_module_run_command(self, cmd, data='', check_rc=True):
        if cmd == ['/usr/bin/debconf-show', 'tzdata']:
            self.exit_json(rc=0, stdout='', stderr='')
            return self.rc, self.stdout, self.stderr

        if cmd == ['/usr/bin/debconf-set-selections', '-u']:
            self.exit_json(rc=0, stdout='', stderr='')
            return self.rc, self.stdout, self.stderr


# Generated at 2022-06-13 05:04:45.302379
# Unit test for function get_selections
def test_get_selections():
    print('Test get_selections')
    import sys
    import tempfile
    tmp = tempfile.NamedTemporaryFile()
    tmp.write('* tzdata/Areas: Europe\n')
    tmp.flush()
    sys.argv = ['debconf.py', '--name', 'tzdata', '--areas', 'Europe']
    selections = get_selections(tmp.name)
    assert selections == {'tzdata/Areas': 'Europe'}

# Generated at 2022-06-13 05:04:57.927934
# Unit test for function main
def test_main():
    module = AnsibleModule(
      argument_spec={
        'name': {'required': True, 'type': 'str'},
        'question': {'required': False, 'type': 'str'},
        'vtype': {'required': False, 'type': 'str'},
        'value': {'required': False, 'type': 'str'},
        'unseen': {'required': False, 'type': 'bool'},
      }
    )

    # TODO: Add test here
    # module.expect_failure(test_func, args, test_kwargs, msg)
    # module.exit_json(changed=changed, msg=msg, meta=meta)
    # module.fail_json(msg=msg, **kwargs)
    # module.run_command(cmd, check_rc=False)

# Generated at 2022-06-13 05:05:00.100535
# Unit test for function main
def test_main():
    assert main({
        "name" : "test-pkg"
    }, None) == (False, {}, {}, {}, None)

# Generated at 2022-06-13 05:05:10.249964
# Unit test for function get_selections
def test_get_selections():
    from ansible_collections.ansible.debian.tests.unit.compat.mock import patch
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes

    def mocked_run_command(*args):
        return 0, to_bytes('name: value\n*name: value\n'), ''

    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', required=True, aliases=['pkg'])
        )
    )

    with patch.object(module, 'run_command', mocked_run_command):
        selections = get_selections(module, 'pkg')

    assert selections == {'name': 'value'}

# Generated at 2022-06-13 05:05:18.096776
# Unit test for function main
def test_main():
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

  # TODO: write test for function main
  assert False

# Generated at 2022-06-13 05:05:25.782402
# Unit test for function set_selection
def test_set_selection():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_text
    import subprocess

    module = AnsibleModule(argument_spec={}, supports_check_mode=True)

    # Exit with no error (True == 0)
    assert set_selection(module, 'ansible-test-pkg', 'ansible/question', 'string', 'test answer', False)[0] == 0

    # Check that question was set
    assert subprocess.check_output(['debconf-get-selections', '|', 'grep', 'ansible/question']).strip() == 'ansible-test-pkg\tansible/question\tstring\tansible-test-pkg/question\ttest answer'

    # Check that question was unset

# Generated at 2022-06-13 05:05:51.382647
# Unit test for function set_selection
def test_set_selection():
    debconf_set_selections_executable = '/usr/bin/debconf-set-selections'
    pkg = 'testpkg'
    question = 'testquestion'
    vtype = 'testtype'
    value = 'testvalue'
    unseen = True
    
    assert set_selection(debconf_set_selections_executable, pkg, question, vtype, value, unseen) == '/usr/bin/debconf-set-selections -u testpkg testquestion testtype testvalue'
    assert set_selection(debconf_set_selections_executable, pkg, question, vtype, value, False) == '/usr/bin/debconf-set-selections testpkg testquestion testtype testvalue'

# Generated at 2022-06-13 05:06:03.009792
# Unit test for function main
def test_main():
    # Get function parameters
    main()
    # Get module parameters
    pkg = module.params["name"]
    question = module.params["question"]
    vtype = module.params["vtype"]
    value = module.params["value"]
    unseen = module.params["unseen"]

    # Get function parameters
    prev = get_selections(module, pkg)

    # Get module parameters
    changed = False
    msg = ""

    if question is not None:
        if vtype is None or value is None:
            module.fail_json(msg="when supplying a question you must supply a valid vtype and value")

        # if question doesn't exist, value cannot match
        if question not in prev:
            changed = True
        else:

            existing = prev[question]

            # ensure we compare booleans supplied to the way

# Generated at 2022-06-13 05:06:05.794752
# Unit test for function main
def test_main():
  # the test would have failed if the data section was not defined in the module
  # parameters
  assert True

# Generated at 2022-06-13 05:06:17.557217
# Unit test for function set_selection
def test_set_selection():
    pkg = 'tzdata'
    question = 'tzdata/Zones/Europe'
    vtype = 'select'
    value = 'Paris'
    unseen = False

    # Create a dummy module

# Generated at 2022-06-13 05:06:25.277295
# Unit test for function set_selection
def test_set_selection():
    import tempfile
    import os
    # prepare tmp file to avoid writing to real debconf database
    tmp_file = tempfile.NamedTemporaryFile(mode='a', delete=False)
    orig_debconf_file = os.environ.get('DEBIAN_FRONTEND')
    os.environ['DEBIAN_FRONTEND'] = 'Noninteractive'
    os.environ['DEBCONF_DB_FILE'] = tmp_file.name

    from ansible.module_utils import debconf as mdebconf
    from ansible.module_utils import basic
    from ansible.module_utils import action
    from ansible.module_utils import module_utils_common


# Generated at 2022-06-13 05:06:37.413860
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

# Generated at 2022-06-13 05:06:51.456414
# Unit test for function main
def test_main():
    """ mocks the module and attempts to run the main function without fail
    """
    import os
    import stat
    import contextlib
    from ansible.module_utils.basic import AnsibleModule

    # import module under test
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'library', 'debconf.py')
    with open(path) as f:
        module = imp.load_module('ansible.module_utils.debconf', f, path, ('.py', 'r', imp.PY_SOURCE))

    # stub the module for test

# Generated at 2022-06-13 05:06:53.206972
# Unit test for function main
def test_main():
    # If a function has a non -1 exit code, then fail the unit test
    assert main() == 0


# Generated at 2022-06-13 05:07:07.012581
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

    pkg = 'test'
    question = 'test'
    vtype = 'test'
    value = 'test'

    rc,

# Generated at 2022-06-13 05:07:12.124863
# Unit test for function set_selection
def test_set_selection():
    module = AnsibleModule(argument_spec=dict(
            name=dict(type='str', required=True, aliases=['pkg']),
            question=dict(type='str', aliases=['selection', 'setting']),
            vtype=dict(type='str', choices=['boolean', 'error', 'multiselect', 'note', 'password', 'seen', 'select', 'string', 'text', 'title']),
            value=dict(type='str', aliases=['answer']),
            unseen=dict(type='bool', default=False),
        ),
        required_together=(['question', 'vtype', 'value'],),
        supports_check_mode=True,
    )

    set_selection(module, 'locales', 'locales/locales_to_be_generated', 'boolean', 'true', False)

   

# Generated at 2022-06-13 05:08:09.656246
# Unit test for function get_selections
def test_get_selections():
    from ansible.module_utils.basic import AnsibleModule
    result = get_selections(AnsibleModule, 'locales')
    assert 'locales/default_environment_locale' in result
    assert 'locales/locales_to_be_generated' in result

# Generated at 2022-06-13 05:08:18.405086
# Unit test for function get_selections

# Generated at 2022-06-13 05:08:25.877628
# Unit test for function main
def test_main():
    my_dict = {"name": "tzdata", "question": None, "value": None, "vtype": None, "unseen": False }
    fields = my_dict.keys()
    data = my_dict.values()
    args = dict(zip(fields, data))
    import ansible.utils.module_docs
    ansible.utils.module_docs.ANSIBLE_MODULE_INSTALL_PATH = "/home/shafi/lib/python2.7/site-packages/ansible/modules/"
    main()


# Generated at 2022-06-13 05:08:33.130861
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
    pkg = "test_pkg"
    question = "test_question"
    vtype = "test_type"
    value = "test_value"

# Generated at 2022-06-13 05:08:45.326657
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

# Generated at 2022-06-13 05:08:53.534587
# Unit test for function main
def test_main():
    def run_command(self, args, data=None, check_rc=True):
        if args == ['debconf-get-selections']:
            output = ' oracle-java7-installer   shared/accepted-oracle-license-v1-1    boolean    true\n'
            return (0, output, '')
        elif args == ['debconf-show', 'oracle-java7-installer']:
            output = ''
            return (0, output, '')
        elif args == ['/usr/bin/debconf-set-selections']:
            print('Test function called!')
            return (0, '', '')
        elif args == ['/usr/bin/debconf-set-selections', '-u']:
            print('Test function called!')

# Generated at 2022-06-13 05:09:03.849766
# Unit test for function get_selections
def test_get_selections():
    module = AnsibleModule(
        argument_spec=dict(name=dict(type='str', required=True, aliases=['pkg']))
    )
    msg = ""
    prev = get_selections(module, 'tzdata')

# Generated at 2022-06-13 05:09:05.538636
# Unit test for function get_selections
def test_get_selections():
    assert get_selections('tzdata') is not None
    assert len(get_selections('tzdata')) > 0

# Generated at 2022-06-13 05:09:10.994422
# Unit test for function main
def test_main():
    pkg = 'tzdata'

    # Get all selections: returns a dict of all selections
    def get_selections(module, pkg):
        all = {'tzconfig/popcon_participation': 'participate',
               'tzconfig/tzdata_valid': 'true',
               'tzdata/System/UTC': 'true',
               'tzdata/Zones/Etc': 'UTC'
               }
        return all

    # If no question is specified, return all selections for a package
    if question is None:
        all = get_selections(module, pkg)
        module.exit_json(changed=False, msg="", current=all)

    # If question is specified, verify selected value matches
    module.params['name'] = pkg
    module.params['question'] = 'tzdata/Zones/Etc'

# Generated at 2022-06-13 05:09:17.607549
# Unit test for function set_selection
def test_set_selection():
  from debconf import Debconf
  from debconf import DebconfCommunicator
  from debconf import DebconfCommunicatorSubprocess
  import subprocess
  import os
  import sys

  test_msg = "test"
  test_question = "test"
  dc = DebconfCommunicator(DebconfCommunicatorSubprocess(subprocess.PIPE, logfd=sys.stdout.fileno()))
  dc.set_progress_data(test_msg)
  pkg = "test"
  vtype = "test"
  value = "test"
  unseen = True
  mode_command = os.path.join(os.path.dirname(os.path.realpath(__file__)), "set_selection.py")

# Generated at 2022-06-13 05:11:06.896689
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
    pkg = module.params["name"]
    question = module.params["question"]
    vtype = module.params["vtype"]
    value = module.params["value"]


# Generated at 2022-06-13 05:11:12.811705
# Unit test for function main
def test_main():

    mock_module = Mock(params={'name': 'tzdata', 'question': None, 'vtype': None, 'value': None, 'unseen': False})
    get_selections_mock = Mock(return_value={'tzdata/Zones/America': 'US,America/New_York'})
    from debconf import main
    main.get_selections = get_selections_mock

    main.main(mock_module)
    mock_module._result['current'] == {'tzdata/Zones/America': 'US,America/New_York'}

# Generated at 2022-06-13 05:11:24.051084
# Unit test for function get_selections
def test_get_selections():

    test_pkg = 'tzdata'

# Generated at 2022-06-13 05:11:35.514016
# Unit test for function set_selection
def test_set_selection():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common._collections_compat import Mapping, Sequence

    # Taken from module_utils.basic.py

# Generated at 2022-06-13 05:11:37.756148
# Unit test for function get_selections
def test_get_selections():
    test = "package1 package2"
    module = AnsibleModule(True, None)
    assert (get_selections(module, test) == dict())



# Generated at 2022-06-13 05:11:51.674364
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

# Generated at 2022-06-13 05:11:52.958733
# Unit test for function get_selections
def test_get_selections():
    result = get_selections(None, 'tzdata')
    assert result is not None


# Generated at 2022-06-13 05:12:01.815441
# Unit test for function get_selections
def test_get_selections():
    # Define module parameters
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

    # Define module parameters
    pkg = module.params["name"]

# Generated at 2022-06-13 05:12:04.793634
# Unit test for function get_selections
def test_get_selections():
    assert get_selections(pkg='tzdata') == "{'tzdata/Areas': 'Europe', 'tzdata/Zones/Europe': 'Helsinki'}"

# Generated at 2022-06-13 05:12:14.891152
# Unit test for function get_selections
def test_get_selections():
    from ansible.module_utils.ansible_release import __version__
    from ansible.module_utils.basic import AnsibleModule, DeprecationWarning
    from ansible.module_utils._text import to_bytes
    import pytest
    import warnings

    warnings.simplefilter('once', DeprecationWarning)
    warnings.warn('test_get_selections is deprecated and will be removed', DeprecationWarning)

    # This test case is actually completely redundant with the make test-module-utils, but it is kept here
    # for documentation purposes.
    def get_selections_check(module, pkg):
        module.run_command = fake_run_command
        selections = get_selections(module, pkg)