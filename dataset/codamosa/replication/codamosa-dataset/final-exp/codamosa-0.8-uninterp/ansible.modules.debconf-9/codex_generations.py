

# Generated at 2022-06-13 05:02:39.846519
# Unit test for function get_selections
def test_get_selections():
    import os
    from ansible.module_utils.basic import AnsibleModule
    test_module = AnsibleModule(argument_spec={},supports_check_mode=True)
    test_pkg = 'openssh-server'
    select = get_selections(test_module, test_pkg)
    assert(select['ssh/permit-root-login'] == "false")



# Generated at 2022-06-13 05:02:47.970251
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

# Generated at 2022-06-13 05:02:55.566390
# Unit test for function get_selections
def test_get_selections():
    from mock import patch
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={'name': {'type': 'str', 'required': True, 'aliases': ['pkg']}})

# Generated at 2022-06-13 05:03:04.893960
# Unit test for function get_selections

# Generated at 2022-06-13 05:03:18.722503
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
    expected = {"tzdata/Areas": "Europe", "tzdata/Zones/Europe": "London"}

# Generated at 2022-06-13 05:03:19.618983
# Unit test for function main
def test_main():
    print ("Testing main")
    main()

# end of test main

# Generated at 2022-06-13 05:03:25.119516
# Unit test for function set_selection

# Generated at 2022-06-13 05:03:34.090337
# Unit test for function get_selections
def test_get_selections():

    # Create debconf.conf file with single setting:
    f = open("debconf.conf", "w")
    f.write("* shared/accepted-oracle-license-v1-1 boolean true\n")
    f.close()

    # and run test
    m = AnsibleModule(argument_spec={'name': {'type': 'str', 'required': True, 'aliases': ['pkg']}})
    get_selections(m, 'localepurge')
    get_selections(m, 'atop')
    m.fail_json(msg='localepurge above should raise error')


# Generated at 2022-06-13 05:03:47.344964
# Unit test for function get_selections
def test_get_selections():
    # Tested with Ansible 2.9.1
    import os

    test_input = {'name': 'tzdata', 'question': None, 'vtype': None, 'value': None, 'unseen': False}
    module = AnsibleModule(argument_spec=dict(name=dict(type='str', required=True, aliases=['pkg']),
                                              question=dict(type='str', aliases=['selection', 'setting']),
                                              vtype=dict(type='str', choices=['boolean', 'error', 'multiselect', 'note', 'password', 'seen', 'select', 'string', 'text', 'title']),
                                              value=dict(type='str', aliases=['answer']),
                                              unseen=dict(type='bool', default=False)
                                              ))


# Generated at 2022-06-13 05:03:50.322512
# Unit test for function set_selection
def test_set_selection():
    pass


# Generated at 2022-06-13 05:04:10.436438
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
    pkg = "locales"
   

# Generated at 2022-06-13 05:04:14.128440
# Unit test for function main
def test_main():
    args = dict(
        name='vim',
        question='',
        vtype='',
        value='',
    )
    rc, out, err = main(args)

# Generated at 2022-06-13 05:04:21.334733
# Unit test for function set_selection
def test_set_selection():

    import os
    import re
    import debconf
    from ansible.module_utils.basic import AnsibleModule

    # Make sure debconf-set-selections is installed
    module = AnsibleModule(argument_spec={})

    selections = {}

    # Validate the input data
    def validate_data(question, vtype, value):
        supported_types = ['boolean', 'error', 'multiselect', 'note', 'password', 'seen', 'select', 'string', 'text', 'title']
        if vtype not in supported_types:
            return False

        if vtype == 'boolean':
            if value.lower() == 'true':
                value = 'true'
            elif value.lower() == 'false':
                value = 'false'
            else:
                return False

# Generated at 2022-06-13 05:04:21.963913
# Unit test for function set_selection
def test_set_selection():
    assert 4 == 4

# Generated at 2022-06-13 05:04:25.883604
# Unit test for function set_selection
def test_set_selection():
    # determine the number of system calls made
    # import subprocess
    # subprocess.call = count_calls(subprocess.call)
    # set_selection()
    # sys.call_count == 1
    # module.fail_json(msg="Must define unit tests for function set_selection")
    assert False

# Generated at 2022-06-13 05:04:26.523000
# Unit test for function get_selections
def test_get_selections():
    assert False

# Generated at 2022-06-13 05:04:40.282943
# Unit test for function main
def test_main():
    import os
    import tempfile

    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common.process import get_bin_path

#    run_command = AnsibleModule.run_command

    # create a selection dump file
    module = AnsibleModule(argument_spec={})
    fd, path = tempfile.mkstemp()
    os.close(fd)
    fd = open(path, 'w')
    stdout = to_bytes('question1 error value1\n')
    fd.write(stdout)
    fd.close()



# Generated at 2022-06-13 05:04:41.264854
# Unit test for function main
def test_main():
    # unit tests go here
    assert True

# Generated at 2022-06-13 05:04:47.408605
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
    pkg = 'tzdata'
   

# Generated at 2022-06-13 05:04:54.165520
# Unit test for function set_selection
def test_set_selection():
    (rc, msg, e) = set_selection(module, 'scribus', 'scribus/install-desktop-files', 'boolean', 'true', False)
    if rc:
        fail('command failed with return code {0} and error {1}'.format(rc, e))
    else:
        module.exit_json(changed=True, msg=msg, current=curr, previous=prev, diff=diff_dict)

# Generated at 2022-06-13 05:05:21.621231
# Unit test for function set_selection

# Generated at 2022-06-13 05:05:27.983853
# Unit test for function main
def test_main():
    # Create the module object
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', required='True', aliases=['pkg']),
            question=dict(type='str', aliases=['selection', 'setting']),
            vtype=dict(type='str', choices=['boolean', 'error', 'multiselect', 'note', 'password', 'seen', 'select', 'string', 'text', 'title']),
            value=dict(type='str', aliases=['answer']),
            unseen=dict(type='bool', default=False),
        ),
        required_together=(['question', 'vtype', 'value'],),
        supports_check_mode=True,
    )

    # Set params

# Generated at 2022-06-13 05:05:39.161223
# Unit test for function set_selection
def test_set_selection():
    import unittest2
    from ansible.module_utils.six import StringIO

    # Syntax 1, bare function call
    module = DummyModule(
        argument_spec=dict(
            name=dict(type='str', required=True, aliases=['pkg']),
            question=dict(type='str', aliases=['selection', 'setting']),
            vtype=dict(type='str', choices=['boolean', 'error', 'multiselect', 'note', 'password', 'seen', 'select', 'string', 'text', 'title']),
            value=dict(type='str', aliases=['answer']),
            unseen=dict(type='bool', default=False),
        ),
        required_together=(['question', 'vtype', 'value'],),
    )

# Generated at 2022-06-13 05:05:41.446533
# Unit test for function main
def test_main():
    # test get_selections
    assert get_selections(AnsibleModule, 'tzdata') is not None

    # test set_selection
    assert set_selection(AnsibleModule, 'tzdata', 'selections/country', 'string', 'US', True) is not None

# Generated at 2022-06-13 05:05:47.405276
# Unit test for function get_selections
def test_get_selections():
  module = AnsibleModule(argument_spec=dict( name=dict(type='str', required=True, aliases=['pkg']) ), supports_check_mode=True )
  pkg = "locales"
  result = get_selections(module, pkg)
  assert result["locales/locales_to_be_generated"] != None
  assert result["locales/default_environment_locale"] != None


# Generated at 2022-06-13 05:05:48.346770
# Unit test for function get_selections
def test_get_selections():
    assert 0 == 0



# Generated at 2022-06-13 05:06:00.259674
# Unit test for function get_selections
def test_get_selections():
    class TestModule:
        def __init__(self):
            self.run_command_results = [
                (0, 'locales/default_environment_locale: fr_FR.UTF-8\nlocales/locales_to_be_generated: en_US.UTF-8 UTF-8, fr_FR.UTF-8 UTF-8\n\n', ''),
                (0, 'locales/default_environment_locale: en_US.UTF-8\nlocales/locales_to_be_generated: en_US.UTF-8 UTF-8, en_GB.UTF-8 UTF-8, fr_FR.UTF-8 UTF-8\n\n', '')
            ]
            self.run_command_calls = 0


# Generated at 2022-06-13 05:06:03.518570
# Unit test for function set_selection
def test_set_selection():
    assert set_selection(module, pkg, question, vtype, value, unseen) == True

# Generated at 2022-06-13 05:06:16.677183
# Unit test for function set_selection
def test_set_selection():
    # Create a mock module to test the function.
    module = AnsibleModule(argument_spec={})
    module.params = {
        'unseen': False,
        'pkg': 'foo',
        'question': 'greeting',
        'vtype': 'string',
        'value': 'hello'
    }
    module.check_mode = False

    # Create a mock run_command method.

# Generated at 2022-06-13 05:06:24.311434
# Unit test for function get_selections
def test_get_selections():
    selection_list = ['tzdata tzdata/Areas select Africa',
                      'tzdata tzdata/Zones/Africa select Casablanca',
                      'tzdata tzdata/Zones/Africa select Freetown',
                      'tzdata tzdata/Zones/Africa select Nouakchott']
    assert( get_selections(selection_list) == { 'tzdata/Areas' : 'Africa',
                                                'tzdata/Zones/Africa' : 'Casablanca' } )


# Generated at 2022-06-13 05:07:12.596687
# Unit test for function get_selections
def test_get_selections():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', required=True, aliases=['pkg'])
        )
    )
    module.run_command = MagicMock(return_value=(0, '* tzdata/Zones/Etc: Etc/UTC\n', ''))
    assert get_selections(module, 'tzdata') == {'tzdata/Zones/Etc': 'Etc/UTC'}
    module.run_command = MagicMock(return_value=(1, '', ''))
    try:
        get_selections(module, 'tzdata')
        assert False, 'this statement should not be reached'
    except AnsibleFailJson as e:
        assert True



# Generated at 2022-06-13 05:07:14.725747
# Unit test for function main
def test_main():
    pkg = 'ntp'
    question = 'ntp/ntpservers'
    vtype = 'string'
    value ='ntp.example.com'
    unseen = False
    changed = True

# Generated at 2022-06-13 05:07:26.805921
# Unit test for function set_selection
def test_set_selection():
    to_text = module.to_text
    run_command = module.run_command
    get_bin_path = module.get_bin_path
    module.to_text = lambda x: x
    module.run_command = lambda x, data='': (0, '', '')
    module.get_bin_path = lambda x, true: x

# Generated at 2022-06-13 05:07:37.456711
# Unit test for function get_selections
def test_get_selections():
    from ansible.module_utils.basic import AnsibleModule
    import debconf
    test_selections = {}
    test_selections['tzdata tzdata/Areas select'] = 'America'
    test_selections['tzdata tzdata/Zones/America select'] = 'New_York'
    test_selections['tzdata tzdata/Zones/America seen'] = 'true'
    test_selections['tzdata tzdata/Areas seen'] = 'true'
    test_selections['tzdata tzdata/Zones/America multiselect'] = 'America/Indiana/Vincennes'

    module = AnsibleModule(
    	argument_spec=dict(
    		name=dict(type='str', aliases=['pkg'])
    	)
    )

# Generated at 2022-06-13 05:07:48.695330
# Unit test for function get_selections
def test_get_selections():
    import json
    import sys
    import os
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils._text import to_text
    from ansible.module_utils.common.command import AnsibleCmd

    # Force an import error on _selinux to ensure we don't break action plugins
    # that do not depend on it.
    sys.modules["selinux"] = None

    # Store the result
    result = None

    class TestModule:

        def __init__(self, *args, **kwargs):
            self.params = kwargs
            self.check_mode = False

        def fail_json(self, *args, **kwargs):
            raise AssertionError(kwargs['msg'])


# Generated at 2022-06-13 05:07:57.389384
# Unit test for function get_selections
def test_get_selections():
    # Test 1: Test for a non existing package
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
    # Test for a package that does not exist

# Generated at 2022-06-13 05:08:07.178913
# Unit test for function get_selections
def test_get_selections():
    import os
    import platform
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common.collections import ImmutableDict

    class TestModule(object):
        def __init__(self, **kwargs):
            self.params = kwargs
            self.verbose = True

        def exit_json(self, **kwargs):
            self.exit_args = kwargs

        def fail_json(self, **kwargs):
            self.fail_args = kwargs

        def run_command(self, args, data=None):
            self.command_executed = args
            if data:
                file_name = to_bytes(self.params['name'])
                self.tmp_file_handler = open(file_name, 'wb+')
                self.tmp

# Generated at 2022-06-13 05:08:11.828132
# Unit test for function main
def test_main():
    # Test for missing vtype and value
    set_module_args({'question': 'question'})
    with pytest.raises(AnsibleFailJson) as exc:
        main()
    assert 'when supplying a question you must supply a valid vtype and value' in str(exc.value)


# Generated at 2022-06-13 05:08:25.583239
# Unit test for function set_selection
def test_set_selection():
    mock_module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', required=True, aliases=['pkg']),
            question=dict(type='str', aliases=['selection', 'setting']),
            vtype=dict(type='str', choices=['boolean', 'error', 'multiselect', 'note', 'password', 'seen', 'select', 'string', 'text', 'title']),
            value=dict(type='str', aliases=['answer']),
            unseen=dict(type='bool', default=False),
        ),
        required_together=(['question', 'vtype', 'value'],),
    )

    # check that set_selection returns rc, msg, e

# Generated at 2022-06-13 05:08:32.874466
# Unit test for function main
def test_main():
    import sys
    import StringIO
    if sys.version_info[0] >= 3:
        module_io = StringIO.StringIO()
    else:
        module_io = StringIO.StringIO()

    def run_command(*args, **kwargs):
        return 0, '', ''

    # Test with good args
    params = {'name': 'foo', 'vtype': 'boolean', 'value': 'False', 'question': 'foo/bar'}

# Generated at 2022-06-13 05:09:53.280123
# Unit test for function set_selection
def test_set_selection():
    assert set_selection(module, test_package, test_question, test_type, test_value, false) == 0

# Generated at 2022-06-13 05:10:02.276229
# Unit test for function set_selection
def test_set_selection():
    import os
    import shutil
    import tempfile
    import subprocess
    from ansible.module_utils._text import to_text

    tmp_dir = tempfile.mkdtemp()
    fname = os.path.join(tmp_dir, 'test_debconf_settings')
    result = subprocess.check_output(['debconf-get-selections'], universal_newlines=True)

    # TODO: find/use actual archive.debconf.org password
    # FIXME: this test can only run in a debian or derivative
    # test setting password and testing with check_output('debconf-get-selections') for expected password

# Generated at 2022-06-13 05:10:08.858812
# Unit test for function set_selection
def test_set_selection():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', required=True, aliases=['pkg']),
            question=dict(type='str', aliases=['selection', 'setting']),
            vtype=dict(type='str', choices=['boolean', 'error', 'multiselect', 'note', 'password', 'seen', 'select', 'string', 'text', 'title']),
            value=dict(type='str', aliases=['answer']),
            unseen=dict(type='bool', default=False),
        ),
    )
    assert set_selection(module, 'tzdata', 'tzdata/Zones/US', 'select', 'America/Chicago', False) == (0, '', '')

# Generated at 2022-06-13 05:10:17.441602
# Unit test for function set_selection
def test_set_selection():
    set_selection(module=AnsibleModule(
      argument_spec=dict(
        name=dict(type='str', required=True, aliases=['pkg']),
        question=dict(type='str', aliases=['selection', 'setting']),
        vtype=dict(type='str', choices=['boolean', 'error', 'multiselect', 'note', 'password', 'seen', 'select', 'string', 'text', 'title']),
        value=dict(type='str', aliases=['answer']),
        unseen=dict(type='bool', default=False),
      ),
      required_together=(['question', 'vtype', 'value'],),
      supports_check_mode=True,
    ), pkg='test', question='test_question', vtype='string', value="test string", unseen=False)

# Generated at 2022-06-13 05:10:28.634795
# Unit test for function set_selection
def test_set_selection():
    module = AnsibleModule(argument_spec=dict(
        name=dict(type='str', required=True, aliases=[]),
        question=dict(type='str', aliases=[]),
        vtype=dict(type='str', aliases=[]),
        value=dict(type='str', aliases=[]),
        unseen=dict(type='bool', aliases=[]),
    ),
        required_together=(['question', 'vtype', 'value'],),
        supports_check_mode=True,
    )
    rc, msg, e = set_selection(module, 'test_module', 'my_question', 'test_type', 'test_value', False)
    print(rc)
    print(msg)
    print(e)

# Generated at 2022-06-13 05:10:31.848583
# Unit test for function main
def test_main():
    assert main(['-c', 'test/test.cfg', '', 'foo.bar']) == 0

if __name__ == "__main__":
    test_main()

# Generated at 2022-06-13 05:10:34.243823
# Unit test for function get_selections
def test_get_selections():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', required=True, aliases=['pkg'])
        )
    )

    pkg = module.params["name"]

    if pkg is not None:
        prev = get_selections(module, pkg)
        print("Selections: %s" % prev)


# Generated at 2022-06-13 05:10:47.933554
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


# Generated at 2022-06-13 05:10:52.868780
# Unit test for function set_selection
def test_set_selection():
    setsel = '/usr/bin/debconf-set-selections'
    pkg = 'tzdata'
    question = 'tzdata/Areas'
    vtype = 'select'
    value = 'America'
    unseen = False
    cmd = [setsel, '-u']
    data = ' '.join([pkg, question, vtype, value])
    set_selection(cmd, data)

# Generated at 2022-06-13 05:10:56.996960
# Unit test for function get_selections
def test_get_selections():
    module_mock = AnsibleModule({})
    module_mock.run_command = run_command_mock
    selections = get_selections(module_mock, 'nsd')
    assert selections is not None
    assert len(selections) == 2
    assert selections['nsd/trustanchor-import-check'] == 'false'
    assert selections['nsd/trust-anchor-file'] == '/usr/share/dnssec-tools/root.key'