

# Generated at 2022-06-13 05:02:41.542201
# Unit test for function get_selections
def test_get_selections():
    from mock import patch
    from ansible.modules.packaging.os import debconf as module

    data = "tzdata tzdata/Areas select Africa"
    rc = 0
    selection = {'tzdata tzdata/Areas': 'Africa'}

    with patch.dict('sys.modules', {'ansible.modules.packaging.os.debconf': module}):
        with patch.object(module, 'run_command', return_value=(rc, data, '')):
            assert module.get_selections('tzdata') == selection


# Generated at 2022-06-13 05:02:44.936128
# Unit test for function main
def test_main():
    # Prepare the parameters
    params = {
        'name': 'locales',
        'question': 'locales/default_environment_locale',
        'vtype': 'select',
        'value': 'fr_FR.UTF-8',
    }
    # Execute the function
    main(params)

# Generated at 2022-06-13 05:02:49.003025
# Unit test for function set_selection
def test_set_selection():
    # pkg, question, vtype, value, unseen
    module = AnsibleModule(argument_spec={})
    rc, msg, e = set_selection(module, "foo", "question", "a_type", "answer", true)
    assert rc == 0, "set_selection should return 0"
    assert e == "", "set_selection should not return an error message"
    assert msg == "", "set_selection should not return a message"


# Unit tests for function get_selections

# Generated at 2022-06-13 05:02:56.107519
# Unit test for function main
def test_main():
    class Args(object):
        def __init__(self, argv=None):
            if argv is None:
                self.args = ['ansible.builtin.debconf', 'ansible.builtin.debconf', '--check', '-vvv']
            else:
                self.args = argv

            self.become = False
            self.become_method = None
            self.become_user = None
            self.listtags = None
            self.listtasks = None
            self.syntax = None
            self.tags = []
            self.verbosity = 3

    import ansible.utils.display
    ansible.utils.display.Verbosity = 0
    import json
    import sys

    args = Args()

# Generated at 2022-06-13 05:03:05.351180
# Unit test for function get_selections
def test_get_selections():
    from ansible.module_utils.basic import AnsibleModule
    import sys

    module = AnsibleModule(
        argument_spec={'name': dict(type='str', required=True, aliases=['pkg'])},
    )

    # set the path for testing
    sys.path.append("..")
    # Monkey patching to avoid calling sys.exit in the module if a required command is not found
    module.get_bin_path = lambda x: x

    # Read the whole output of debconf-show and return it as a dict
    def command_run(module, cmd, data=None):
        if isinstance(cmd, list):
            cmd = " ".join(cmd)


# Generated at 2022-06-13 05:03:18.893230
# Unit test for function main
def test_main():
    # mock module input parameters
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
    module.check_mode = False

# Generated at 2022-06-13 05:03:24.427076
# Unit test for function get_selections
def test_get_selections():
    import os
    import tempfile
    import json

    # Setup

# Generated at 2022-06-13 05:03:36.486301
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

    pkg = "tzdata"
    question = "tzdata/Zones/Africa"
    vtype = "select"
    value

# Generated at 2022-06-13 05:03:49.220447
# Unit test for function main
def test_main():
    import json
    import shutil
    import tempfile

    mk_module = lambda **kwargs: AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', required=True, aliases=['pkg']),
            question=dict(type='str', aliases=['selection', 'setting']),
            vtype=dict(type='str', choices=['boolean', 'error', 'multiselect', 'note', 'password', 'seen', 'select', 'string', 'text', 'title']),
            value=dict(type='str', aliases=['answer']),
            unseen=dict(type='bool', default=False),
        ),
        required_together=(['question', 'vtype', 'value'],),
        supports_check_mode=True,
        **kwargs
    )


# Generated at 2022-06-13 05:03:57.668566
# Unit test for function get_selections
def test_get_selections():
    # Test 1. pkg = locales
    pkg = 'locales'
    expected_value = {'locales/locales_to_be_generated': 'en_US.UTF-8 UTF-8 fr_FR.UTF-8 UTF-8', 'locales/default_environment_locale': 'fr_FR.UTF-8', 'locales/locales_to_be_generated_template': '\n'}
    actual_value = get_selections(pkg)
    assert expected_value == actual_value

    # Test 2. pkg = tzdata
    pkg = 'tzdata'
    expected_value = {'tzdata/Zones/Asia': 'Asia/Tokyo', 'tzdata/Zones/Europe': 'Europe/Paris'}
    actual_value = get_selections(pkg)
    assert expected

# Generated at 2022-06-13 05:04:18.384324
# Unit test for function set_selection
def test_set_selection():
    # Use dict to store previous selections
    prev = dict()

    # Try to set a selection that has never been made before
    assert set_selection(prev, 'tzdata', 'tzdata/Areas', 'select', 'Europe', False) == 1
    # Check if change was made
    assert prev['tzdata/Areas'] == 'Europe'

    # Try to set a selection again, with a different value
    assert set_selection(prev, 'tzdata', 'tzdata/Areas', 'select', 'Africa', False) == 0
    # Check if change was made
    assert prev['tzdata/Areas'] == 'Africa'

    # Try to set a selection again, with a different value, and the default unseen-flag
    # NOTE: This is the same code as before, but with the flag in question

# Generated at 2022-06-13 05:04:18.862755
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:04:24.979906
# Unit test for function main

# Generated at 2022-06-13 05:04:30.762340
# Unit test for function get_selections
def test_get_selections():
    module = AnsibleModule({}, {})
    pkg = "tzdata"
    actual = get_selections(module, pkg)

# Generated at 2022-06-13 05:04:32.107503
# Unit test for function get_selections
def test_get_selections():
    assert(get_selections('1') == '1')

# Generated at 2022-06-13 05:04:42.896539
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

    module.run_command = MagicMock(return_value=(0, "success", ""))


# Generated at 2022-06-13 05:04:44.543014
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:04:45.246139
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:04:57.542834
# Unit test for function main
def test_main():

    module_args={
        'name': 'locales',
        'question': 'locales/locales_to_be_generated',
        'vtype': 'multiselect',
        'value': 'en_US.UTF-8 UTF-8, fr_FR.UTF-8 UTF-8',
        'unseen': False
    }
    module_args['name'] = 'locales'
    module_args['question'] = 'locales/locales_to_be_generated'
    module_args['vtype'] = 'multiselect'
    module_args['value'] = 'en_US.UTF-8 UTF-8, fr_FR.UTF-8 UTF-8'
    module_args['unseen'] = False

# Generated at 2022-06-13 05:04:58.050547
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-13 05:05:22.562673
# Unit test for function get_selections
def test_get_selections():
    # Data needed for test
    curr_data = {
        'tzdata/Areas': 'America',
        'tzdata/Zones/America': 'Chicago'
    }

    # Mock module to get debconf-show
    class MockModule(object):
        def __init__(self, pkg):
            self.pkg = pkg

        def run_command(self, cmd, data=None):
            self.cmd = cmd
            self.data = data
            out = ""
            for k, v in curr_data.items():
                out += k + ": " + v + "\n"
            out = out.encode()
            err = ""
            return 0, out, err

    module = MockModule(pkg="tzdata")

    # Mock get_selections function for test

# Generated at 2022-06-13 05:05:28.027468
# Unit test for function set_selection
def test_set_selection():
    class test_module:
        def __init__(self):
            self.fail_json = lambda rc, msg: msg
            self.run_command = lambda cmd, data=None: [0, None, None]
            self.check_mode = False
            self.get_bin_path = lambda bin, required=False: bin
            self._diff = False

    tm = test_module()
    try:
        rc, msg, e = set_selection(tm, 'locales', 'locales/locales_to_be_generated', 'multiselect', 'en_US.UTF-8 UTF-8, fr_FR.UTF-8 UTF-8', False)
        assert rc is False
    except:
        assert False

# Generated at 2022-06-13 05:05:36.268845
# Unit test for function get_selections
def test_get_selections():
    """ Verify return value of get_selections. """
    import sys
    from ansible.module_utils.basic import AnsibleModule

    ret = get_selections(AnsibleModule(argument_spec={}), "tzdata")
    assert isinstance(ret, dict)

    assert ret['tzdata/Areas'] == ''.join(sorted(['America', 'Europe']))
    assert ret['tzdata/Zones/Europe'] == ''.join(sorted(['Helsinki', 'Zurich']))
    assert 'question 5' not in ret
    assert 'question 6' not in ret

# Generated at 2022-06-13 05:05:47.629873
# Unit test for function set_selection
def test_set_selection():
    import os
    import tempfile
    from . import debconf
    from . import module_utils
    from . import ActionModule
    from . import utils
    #
    # Mock the _get_bin_path method
    # In our test all the commands we need are found on the PATH
    #
    if not hasattr(module_utils, '_get_bin_path_shell'):
        module_utils._get_bin_path_shell = module_utils._get_bin_path
    module_utils._get_bin_path = lambda x, y: x

    #
    # Mock the environment variables
    #
    os.environ['LANGUAGE'] = 'C'
    os.environ['LANG'] = 'C'
    os.environ['LC_ALL'] = 'C'

# Generated at 2022-06-13 05:05:55.035891
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
    result = get_selections(module, pkg)

# Generated at 2022-06-13 05:06:04.855735
# Unit test for function get_selections
def test_get_selections():
    """
    Test the get_selections function
    """
    expected = {'tzdata/Areas': 'Africa', 'tzdata/Zones/Africa': 'Algiers', 'tzdata/Zones/America': 'New_York',
                'tzdata/Zones/Asia': 'Hong_Kong', 'tzdata/Zones/Atlantic': 'Azores', 'tzdata/Zones/Australia': 'Sydney',
                'tzdata/Zones/Europe': 'Vienna', 'tzdata/Zones/Indian': 'Maldives', 'tzdata/Zones/Pacific': 'Auckland',
                'tzdata/Zones/US': 'Eastern'}

    # Add the test data
    # Note: tzdata must be installed!
    pkg = 'tzdata'

    # Get the data
    actual = get

# Generated at 2022-06-13 05:06:17.869751
# Unit test for function set_selection
def test_set_selection():
    import tempfile, os

    # Create temporary file and temporary directory with it
    fd, tmp_filename = tempfile.mkstemp()
    tmp_dirname = os.path.dirname(tmp_filename)

    # Create test file and set its permissions
    test_filename = '/tmp/file_exists_test'
    open(test_filename, 'w')
    os.chmod(test_filename, 0o600)

    # Test function with valid parameters
    rc, msg, e = set_selection('pkg', 'question', 'vtype', 'value')
    assert rc == 0
    assert msg == ''
    assert e == ''

    # Test function with invalid parameters
    rc, msg, e = set_selection('pkg', 'question', 'vtype', 'value')
    assert rc == 1
    assert msg == ''
   

# Generated at 2022-06-13 05:06:23.853955
# Unit test for function set_selection
def test_set_selection():
    setsel = module.get_bin_path('debconf-set-selections', True)
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

# Generated at 2022-06-13 05:06:34.446293
# Unit test for function set_selection
def test_set_selection():
    # simple case of setting a string that should not already be set
    module = AnsibleModule(argument_spec={}, check_mode=True)
    pkg = 'units'
    question = 'units/string'
    vtype = 'string'
    value = 'value'
    unseen = False
    (rc, msg, e) = set_selection(module, pkg, question, vtype, value, unseen)
    assert rc == 0
    assert msg == ''
    assert e == ''

    # should fail because the string is already set
    (rc, msg, e) = set_selection(module, pkg, question, vtype, value, unseen)
    assert rc != 0
    assert msg == ''
    assert e != ''

    # yes/no should fail because the boolean is already set
    question = 'units/boolean'
   

# Generated at 2022-06-13 05:06:42.665312
# Unit test for function main
def test_main():
    '''
    Main function unit test.
    '''
    import argparse
    from ansible_collections.ansible.builtin.plugins.module_utils.basic import AnsibleModule
    import ansible_collections.ansible.builtin.plugins.modules.debconf as debconf
    import os

    # redirecting stdout and stderr to devnull
    with open(os.devnull, 'w') as f:
        # saving old stdout, stderr to restore
        stdout_=sys.stdout
        stderr_=sys.stderr
        # redirecting
        sys.stdout=f
        sys.stderr=f

        # arguments
        opt = argparse.Namespace()

        # setting argument values
        opt.check = True

        # function call

# Generated at 2022-06-13 05:07:37.314048
# Unit test for function main
def test_main():
    import sys
    import os
    import subprocess

    # Function "run_command" return a tuple (rc, out, err)
    def run_command(cmd, data=None):
        out = subprocess.check_output(cmd, input=data)
        return (0, out, '')

    # Function "get_bin_path" always return a string '/usr/bin'
    def get_bin_path(cmd, required=True):
        return '/usr/bin'

    # Function "fail_json" returns an exception
    def fail_json(msg=None):
        raise Exception('Call failed with message: ' + msg)

    # Function "exit_json" returns an exit
    def exit_json(changed=False, msg=None, current=None, previous=None, diff=None):
        sys.exit(0)



# Generated at 2022-06-13 05:07:40.784672
# Unit test for function get_selections
def test_get_selections():
    assert get_selections(
        module=None,
        pkg='tzdata') == {'tzdata/Zones/Etc': 'UTC'}

# Generated at 2022-06-13 05:07:52.433073
# Unit test for function main
def test_main():
    import os.path
    import shutil
    import tempfile
    import subprocess
    import json
    import sys
    import ansible
    import ansible.module_utils.basic

    # Load ansible module
    this_file = os.path.normpath(
        os.path.dirname(os.path.abspath(__file__)) + '/../../modules/extras/debconf.py')
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Generated at 2022-06-13 05:07:58.635809
# Unit test for function get_selections
def test_get_selections():
    module = mock.MagicMock()
    module.run_command.return_value = 0, '*linux-image-extra-3.13.0-29-generic:amd64:FOO:word\n', ''
    assert get_selections(module, '') == {
        'linux-image-extra-3.13.0-29-generic:amd64': 'FOO:word'
    }

# Generated at 2022-06-13 05:08:09.056966
# Unit test for function set_selection
def test_set_selection():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.pycompat24 import get_exception
    import json
    import sys

    # Removing all environment variables which might interfere with the unittest
    myenviron = os.environ.copy()
    for key in myenviron.keys():
      if key.startswith('ANSIBLE_'):
          del os.environ[key]

    # Adding our own debconf_set_selections binary which will return the correct values for our test
    test_debconf_set_selections = os.path.join(os.path.dirname(__file__), 'test-bin-debconf-set-selections.sh')
    os.environ['PATH'] = test_debconf_set_selections + ':' + os.environ

# Generated at 2022-06-13 05:08:09.614627
# Unit test for function set_selection
def test_set_selection():
    pass

# Generated at 2022-06-13 05:08:13.141613
# Unit test for function main
def test_main():
    # TODO: finish this
    params = {"name":"localepurge", "question":"localepurge/no_purge_libc", "vtype":"select", "value":"True"}

    print(set_selection(main, **params))

# Generated at 2022-06-13 05:08:18.533933
# Unit test for function get_selections
def test_get_selections():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', required=True, aliases=['pkg'])
        )
    )
    pkg = module.params["name"]
    selections = get_selections(module, pkg)
    assert selections == {}


# Generated at 2022-06-13 05:08:19.829029
# Unit test for function set_selection
def test_set_selection():
    # TODO: Create unit tests for function set_selection
    return True

# Generated at 2022-06-13 05:08:23.979795
# Unit test for function set_selection
def test_set_selection():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec={})
    rc, msg, e = set_selection(module, 'pkg', 'question', 'string', 'value', True)
    assert rc == 0
    assert msg == ""
    assert e == ""

# Generated at 2022-06-13 05:09:43.961284
# Unit test for function get_selections
def test_get_selections():
    question = 'tzdata/Areas'
    vtype = 'select'
    value = 'America'
    unseen = False

    response = str(get_selections(question, vtype, value, unseen))
    assert 'Etc' in response


# Generated at 2022-06-13 05:09:48.835484
# Unit test for function get_selections
def test_get_selections():

    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True,
    )

    results = get_selections(module, 'localepurge')
    assert isinstance(results, dict)
    assert "localepurge/nopurge" in results
    assert results["localepurge/nopurge"] == "eo"

# Generated at 2022-06-13 05:09:58.193190
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
        supports_check_mode=False,
    )

    # TODO: enable passing array of options and/or debconf file from get-selections dump
    pkg = "tzdata"
   

# Generated at 2022-06-13 05:10:06.371078
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

# Generated at 2022-06-13 05:10:07.520162
# Unit test for function get_selections
def test_get_selections():
    assert True

# Generated at 2022-06-13 05:10:12.070627
# Unit test for function get_selections
def test_get_selections():
    module = AnsibleModule(argument_spec=dict())
    assert get_selections(module, "locales") == {'local/postrm_purge_mo': 'true', 'local/default_environment_locale': 'en_US.UTF-8', 'local/postinst_upgrade_mo': 'true', 'local/supported_locales': 'fr_FR.UTF-8 UTF-8 en_US.UTF-8 UTF-8', 'local/configure_locale_failed': 'true', 'local/upgrade_locales': 'true', 'local/locale_gen': '# File generated by update-locale'}
    assert get_selections(module, "unknown") == {}


# Generated at 2022-06-13 05:10:20.117768
# Unit test for function main
def test_main():
    with patch.object(AnsibleModule, 'run_command') as run_command:
        with patch.object(AnsibleModule, 'get_bin_path') as get_bin_path:
            get_bin_path.return_value = '/usr/bin'
            run_command.return_value = 0, '\n'.join(
                ['tzdata tzdata/Areas select Africa',
                 'tzdata tzdata/Zones/Africa select Abidjan',
                 'tzdata tzdata/Zones/America select Bogota',
                 'tzdata tzdata/Zones/Canada select America/Regina',
                 'tzdata tzdata/Zones/Europe select Istanbul',
                 'tzdata tzdata/Zones/GB select Africa/Monrovia']), ''
            main()
            main()
           

# Generated at 2022-06-13 05:10:32.331360
# Unit test for function main
def test_main():
    # test with all three options
    p = dict(
        name='debconf_test_1',
        question='debconf_test_1/question_1',
        vtype='boolean',
        value='true',
        unseen=False,
    )

# Generated at 2022-06-13 05:10:38.561148
# Unit test for function set_selection
def test_set_selection():
    # Note: true/false values expected in set_selection need to be wrapped in quotes.
    assert set_selection(pkg='locales', question='locales/locales_to_be_generated', vtype='multiselect', value='en_US.UTF-8 UTF-8, fr_FR.UTF-8 UTF-8') == [0, 'debconf-set-selections: locales/locales_to_be_generated: multiselect en_US.UTF-8 UTF-8, fr_FR.UTF-8 UTF-8\n']

# Generated at 2022-06-13 05:10:50.195925
# Unit test for function get_selections
def test_get_selections():
    class Return:
        def __init__(self, rc, out, err=''):
            self.rc = rc
            self.out = out
            self.err = err

    class Module:
        def __init__(self):
            self.run_command_args = []
            self.run_command_kwargs = []
            self.run_command_return = Return(0, '''* locales/locales_to_be_generated multiselect
* locales/default_environment_locale select fr_FR.UTF-8
''')

        def run_command(self, args):
            self.run_command_args.append(args)
            self.run_command_kwargs.append(kwargs)
            return self.run_command_return

    module = Module()

    pkg = 'locales'

