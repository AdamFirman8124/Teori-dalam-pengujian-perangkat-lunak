

# Generated at 2022-06-13 05:02:39.887033
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

# Generated at 2022-06-13 05:02:48.218711
# Unit test for function get_selections
def test_get_selections():

    from ansible.module_utils.basic import AnsibleModule

    test_module = AnsibleModule(argument_spec={'name': {'type': 'str'}}, supports_check_mode=True)

    # Test if get_selections method returns a dictionary
    # Test if get_selections returns 'seen'
    assert isinstance(get_selections(test_module, 'tzdata'), dict), 'get_selections should return a dictionary'
    assert get_selections(test_module, 'tzdata').has_key('tzdata/Areas'), 'get_selections should return dictionary with tzdata/Areas'
    assert get_selections(test_module, 'tzdata')['tzdata/Areas'] == '', 'get_selections should return array with tzdata/Areas = ""'

# Generated at 2022-06-13 05:02:48.808719
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-13 05:02:50.057780
# Unit test for function set_selection
def test_set_selection():
    set_selection(module, pkg, question, vtype, value, unseen)

# Generated at 2022-06-13 05:02:56.553552
# Unit test for function set_selection
def test_set_selection():
    # Test when vtype is boolean and value is true
    module = AnsibleModule(argument_spec={})
    rc, msg, e = set_selection(module, 'locales', 'locales/default_environment_locale', 'boolean', 'true', False)
    assert rc == 0
    assert e == ''
    assert msg == ''

    # Test when vtype is boolean and value is false
    module = AnsibleModule(argument_spec={})
    rc, msg, e = set_selection(module, 'locales', 'locales/default_environment_locale', 'boolean', 'false', False)
    assert rc == 0
    assert e == ''
    assert msg == ''

    # Test when vtype is boolean and value is True
    module = AnsibleModule(argument_spec={})
    rc, msg, e = set_

# Generated at 2022-06-13 05:02:57.425766
# Unit test for function get_selections
def test_get_selections():
    get_selections(name='tzdata')

# Generated at 2022-06-13 05:02:58.024042
# Unit test for function set_selection
def test_set_selection():
    pass

# Generated at 2022-06-13 05:02:59.063306
# Unit test for function main
def test_main():
    assert main() is None


# Generated at 2022-06-13 05:03:07.806989
# Unit test for function set_selection
def test_set_selection():
    module = AnsibleModule()
    module.get_bin_path = lambda bin_name, warn=False: bin_name
    module.run_command = lambda cmd: (0, '', '')
    pkg = 'foo'
    question = 'bar'
    vtype = 'baz'
    value = 'quux'
    unseen = False
    rc, stdout, stderr = set_selection(module, pkg, question, vtype, value, unseen)
    assert 'debconf-set-selections -u' not in stdout
    assert 'foo bar baz quux' in stdout
    unseen = True
    rc, stdout, stderr = set_selection(module, pkg, question, vtype, value, unseen)
    assert 'debconf-set-selections -u' in stdout

# Generated at 2022-06-13 05:03:10.761593
# Unit test for function set_selection
def test_set_selection():
    set_selection("postgresql-common", "postgresql-common/start_confirm", 'boolean', 'true', False)

# Generated at 2022-06-13 05:03:22.190511
# Unit test for function set_selection
def test_set_selection():
    from ansible_collections.ansible.community.plugins.module_utils.module_common import AnsibleModule
    my_module = AnsibleModule({})
    results = set_selection(my_module, 'package', 'question', 'string', 'value', False)
    assert results[0] == 0

# Generated at 2022-06-13 05:03:33.771755
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


# Generated at 2022-06-13 05:03:41.056135
# Unit test for function main
def test_main():
    import pytest
    import ansible.module_utils.debconf
    import ansible.modules.extras.packaging.os.debconf as debconf

    # Run without any arguments and fail
    with pytest.raises(SystemExit) as excinfo:
        main()

    # Check exception's exit code
    assert excinfo.type == SystemExit
    assert excinfo.value.code == 1

# Generated at 2022-06-13 05:03:49.406557
# Unit test for function get_selections
def test_get_selections():
    '''
    Read the following debconf-show output and verify the function returns an
    expected dictionary.
    tzdata/Areas: America
    tzdata/Zones/America: Chicago
    '''
    test_output = '''
    tzdata/Areas: America
    tzdata/Zones/America: Chicago
    '''
    module = AnsibleModule(argument_spec={})
    selections = get_selections(module, None)
    assert selections['tzdata/Zones/America'] == 'Chicago'

# Generated at 2022-06-13 05:03:51.586752
# Unit test for function set_selection
def test_set_selection():
    import debconf
    testInput = 'hello'
    testOutput = set_selection(testInput)
    assert testInput in testOutput

# Generated at 2022-06-13 05:03:58.962059
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
    pkg = "ansible-test"

# Generated at 2022-06-13 05:04:10.518501
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

# Generated at 2022-06-13 05:04:23.112157
# Unit test for function get_selections
def test_get_selections():
    import os
    from ansible.module_utils.basic import AnsibleModule

    if not os.path.exists('data'):
        os.makedirs('data')


# Generated at 2022-06-13 05:04:27.920864
# Unit test for function get_selections
def test_get_selections():
    module = AnsibleModule(
        argument_spec=dict(
        )
    )
    pkg = 'tzdata'
    result = {'tzdata/Zones/Europe': 'Amsterdam',
              'tzdata/Zones/America': 'Denver',
              'tzdata/Zone/Etc': 'UTC',
              'tzdata/Areas': 'Europe',
              'tzdata/Zones/Etc': 'UTC'}
    assert(result == get_selections(module, pkg))

# Generated at 2022-06-13 05:04:33.523238
# Unit test for function get_selections
def test_get_selections():
    import os
    os.environ['PYTHONPATH'] = '/home/ubuntu/workspace/ansible'
    import ansible.module_utils.debconf as debconf_utils
    # test_case 1: test from debconf-set-selections
    test_case1 = {'*urlpath':'', '*default-selection':'', '*priority':'critical', '*http_proxy':'', '*url':'http://security.debian.org', '*codename':'jessie/updates', '*suite':'jessie-updates', '*release':'', '*components':''}
    # test_case 2: test from debconf-show

# Generated at 2022-06-13 05:04:58.551267
# Unit test for function set_selection
def test_set_selection():
    setsel = __import__('ansible.module_utils.basic').get_bin_path('debconf-set-selections', True)
    out = os.system(setsel + " -u - <<EOF\npackage question vtype value\nEOF\n")
    assert out == 0
    assert os.path.isfile("/var/cache/debconf/config.dat")

# Generated at 2022-06-13 05:04:59.908179
# Unit test for function set_selection
def test_set_selection():
    assert set_selection() == "OK"

# Generated at 2022-06-13 05:05:09.116130
# Unit test for function main
def test_main():
    testdict = {'name': 'locales', 'question': 'locales/locales_to_be_generated', 'vtype': 'multiselect', 'value': 'en_US.UTF-8 UTF-8, fr_FR.UTF-8 UTF-8'}
    result = main(testdict)
    assert result == {'changed': True, 'current': {'locales/locales_to_be_generated': 'en_US.UTF-8 UTF-8, fr_FR.UTF-8 UTF-8'}, 'previous': {'locales/locales_to_be_generated': ''}, 'result': True, 'returncode': 0}

# Generated at 2022-06-13 05:05:13.517988
# Unit test for function get_selections
def test_get_selections():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', required=True, aliases=['pkg']),
        ),
        supports_check_mode=True,
    )
    pkg = module.params["name"]
    selections = get_selections(module, pkg)
    module.exit_json(changed=False, msg="", current=selections)

# Generated at 2022-06-13 05:05:17.210905
# Unit test for function set_selection
def test_set_selection():
    module = set_selection(module, pkg, question, vtype, value, unseen)
    pkg = test
    question = True
    vtype = test
    value = test
    unseen = test
    setsel = set_selection(module, pkg, question, vtype, value, unseen)

# Generated at 2022-06-13 05:05:25.121928
# Unit test for function get_selections
def test_get_selections():
    """
    [Unit test for function get_selections]

    [Test all cases of get_selections]
    """
    import sys
    import os
    import types

    # append module path
    MODULE_PATH = 'package/module/path'
    sys.path.append(MODULE_PATH)
    from ansible.module_utils.basic import AnsibleModule


# Generated at 2022-06-13 05:05:28.311920
# Unit test for function set_selection
def test_set_selection():
    set_selection(module, pkg, question, vtype, value, unseen)


# Generated at 2022-06-13 05:05:39.341926
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

# Generated at 2022-06-13 05:05:40.920596
# Unit test for function get_selections
def test_get_selections():
    module = AnsibleModule()
    # running this with an empty dict will return None which is OK
    result = get_selections(module, {})
    assert result is None


# Generated at 2022-06-13 05:05:50.660019
# Unit test for function main

# Generated at 2022-06-13 05:06:36.627741
# Unit test for function set_selection
def test_set_selection():
    module = AnsibleModule(argument_spec=dict(
        name=dict(type='str', required=True, aliases=['pkg']),
        question=dict(type='str', aliases=['selection', 'setting']),
        vtype=dict(type='str', choices=['boolean', 'error', 'multiselect', 'note', 'password', 'seen', 'select', 'string', 'text', 'title']),
        value=dict(type='str', aliases=['answer']),
        unseen=dict(type='bool', default=False),
        ))

    module.set_bin_path('/usr/bin/printf')
    pkg = "mypackage"
    question = "myquestion"
    vtype = "select"
    value = "myvalue"
    unseen = False
    
    rc, stdout, stderr

# Generated at 2022-06-13 05:06:50.814730
# Unit test for function main
def test_main():
    # test with required args
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

    # test for missing required args
    with pytest.raises(SystemExit):
        module = AnsibleModule

# Generated at 2022-06-13 05:07:00.126210
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
        # We don't want to exit with an error when the module runs in check mode
        supports_check_mode=True,
    )
    pkg = 'locales'

# Generated at 2022-06-13 05:07:05.295318
# Unit test for function main
def test_main():
    test_mod = AnsibleModule({
        "name": "local",
        "question": "locales/default_environment_locale",
        "vtype": "select",
        "value": "fr_FR.UTF-8"
    }, check_invalid_arg=False)

    main(test_mod)

# Generated at 2022-06-13 05:07:12.588852
# Unit test for function main
def test_main():
    import os
    import sys
    import pytest
    from tempfile import mkstemp
    from ansible.module_utils._text import to_bytes
    import ansible.module_utils.basic
    fd, temp = mkstemp()
    os.close(fd)

# Generated at 2022-06-13 05:07:18.790391
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

# Generated at 2022-06-13 05:07:30.042706
# Unit test for function get_selections
def test_get_selections():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import StringIO

    mocked_response = """locales/locales_to_be_generated: en_US.UTF-8 UTF-8, fr_FR.UTF-8 UTF-8
locales/default_environment_locale: en_US.UTF-8
locales/locales_to_be_generated: en_US.UTF-8 UTF-8, fr_FR.UTF-8 UTF-8"""

    # Mock module method run_command
    def run_command_mocked(self, cmd, data=None, check_rc=True):
        return (0, StringIO(mocked_response), StringIO())

    AnsibleModule.run_command = run_command_mocked

    # Execute function get_selections with mocked

# Generated at 2022-06-13 05:07:41.669926
# Unit test for function get_selections
def test_get_selections():
    from ansible.module_utils import basic
    import copy

    module_data = {}
    module = basic.AnsibleModule(argument_spec={}, supports_check_mode=True)
    module.run_command = lambda *args, **kwargs: copy.deepcopy(module_data)
    module.get_bin_path = lambda *args, **kwargs: '/usr/bin/debconf-show'

    # Test with no data, should return empty dictionary
    module_data['rc'] = 0
    module_data['out'] = ''
    module_data['err'] = ''
    assert get_selections(module, 'foo') == {}

    # Test with data, should return dictionary with data
    module_data['rc'] = 0

# Generated at 2022-06-13 05:07:53.344707
# Unit test for function get_selections
def test_get_selections():
    from ansible.module_utils.six import StringIO
    from ansible.module_utils import basic
    module = basic.AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', required=True, aliases=['pkg']),
        ),
        supports_check_mode=True,
    )

    pkg='tzdata'

# Generated at 2022-06-13 05:08:04.065808
# Unit test for function main
def test_main():
    import ansible.modules.debconf as debconf
    import ansible.module_utils.common.process as process
    import ansible.module_utils.six as six
    import sys, os
    import datetime, time


# Generated at 2022-06-13 05:09:28.165875
# Unit test for function main
def test_main():
    import os
    import sys
    import tempfile

    from ansible.module_utils.basic import AnsibleModule

    DIR = os.path.dirname(os.path.abspath(__file__))
    BIN = os.path.join(DIR, '../../../bin/')
    sys.path.insert(0, BIN)
    TEST_PATH = os.path.join(DIR, '../../../..')
    if TEST_PATH not in sys.path:
        sys.path.append(TEST_PATH)
    from units.modules.utils import set_module_args, exit_json, fail_json, AnsibleExitJson

    d = tempfile.mkdtemp()

# Generated at 2022-06-13 05:09:33.678652
# Unit test for function main

# Generated at 2022-06-13 05:09:44.737557
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

# Generated at 2022-06-13 05:09:52.833484
# Unit test for function set_selection
def test_set_selection():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_text
    from ansible.module_utils.common.collections import ImmutableDict

# Generated at 2022-06-13 05:10:01.914401
# Unit test for function get_selections

# Generated at 2022-06-13 05:10:06.498726
# Unit test for function set_selection
def test_set_selection():
    module = AnsibleModule(argument_spec=dict(name='localepurge', question='localepurge/nopurge',
                                              vtype='multiselect', value='en_US.UTF-8'),
                           supports_check_mode=True)

    rc, out, err = set_selection(module, module.params['name'], module.params['question'],
                                 module.params['vtype'], module.params['value'], unseen=False)
    assert(rc == 0)



# Generated at 2022-06-13 05:10:13.759416
# Unit test for function set_selection
def test_set_selection():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )

    # Test without question/vtype/value
    result = set_selection(module, 'test', None, None, None, False)
    assert result == (None, None)

    # Test with valid question/vtype/value
    result = set_selection(module, 'test', 'myquestion', 'mytype', 'myvalue', False)
    assert result == (None, None)

# Generated at 2022-06-13 05:10:14.262959
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:10:20.363246
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

# Generated at 2022-06-13 05:10:28.810888
# Unit test for function set_selection
def test_set_selection():
    module = AnsibleModule(argument_spec={})
    name = "locales"
    question = "locales/default_environment_locale"
    vtype = "select"
    value = "fr_FR.UTF-8"
    unseen = False
    rc, msg, e = set_selection(module, name, question, vtype, value, unseen)
    if rc:
        module.fail_json(msg=e)
    assert msg == "", "msg should be blank"
    assert e == None, "e should be blank"
