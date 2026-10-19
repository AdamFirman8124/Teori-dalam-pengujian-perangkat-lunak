

# Generated at 2022-06-13 05:02:39.164917
# Unit test for function get_selections
def test_get_selections():
    test_ansible_module = AnsibleModule(argument_spec={'name': {'type': 'str', 'required': True, 'aliases': ['pkg']}},
                                        required_together=(['question', 'vtype', 'value'],),
                                        supports_check_mode=True)
    test_selections = get_selections(test_ansible_module, 'tzdata')
    print(test_selections)

# Generated at 2022-06-13 05:02:46.804001
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils.common.dict_transformations import dict2bytes
    import collections
    import json

    pkg = 'tzdata'


# Generated at 2022-06-13 05:02:51.195329
# Unit test for function get_selections
def test_get_selections():
    module = AnsibleModule(argument_spec=dict())
    assert get_selections(module, 'tzdata') == {
        'tzdata/root_password_crypted': '*',
        'tzdata/Areas': 'Europe',
        'tzdata/Zones/Europe': 'Berlin',
        'tzdata/ZoneInfo/UTC': 'true',
        'tzdata/ZoneInfo/Europe/Berlin': 'true'}



# Generated at 2022-06-13 05:02:51.679902
# Unit test for function set_selection
def test_set_selection():
    pass

# Generated at 2022-06-13 05:02:57.861977
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

# Generated at 2022-06-13 05:02:58.431304
# Unit test for function main
def test_main():
    # Basic function test
    main()


# Generated at 2022-06-13 05:03:04.144900
# Unit test for function get_selections
def test_get_selections():
    assert get_selections("tzdata", "tzdata/Zones/Asia") == {'tzdata/Zones/Asia': 'Japan'}
    assert get_selections("tzdata", "tzdata/Zones/Europe") == {'tzdata/Zones/Europe': 'Amsterdam'}
    assert get_selections("tzdata", "tzdata/Zones/America") == {'tzdata/Zones/America': 'Los_Angeles'}


# Generated at 2022-06-13 05:03:04.826260
# Unit test for function main
def test_main():
    print(main())

# Generated at 2022-06-13 05:03:11.556095
# Unit test for function get_selections
def test_get_selections():
    module = AnsibleModule()
    fqdn = 'test.example.com'
    pkg = 'tzdata'

    tzdata_selections = get_selections(module, pkg)

    assert tzdata_selections['tzdata/Areas'] == 'Etc'


# Generated at 2022-06-13 05:03:22.071141
# Unit test for function get_selections
def test_get_selections():
    import os
    import json
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.module_utils.basic import AnsibleModule

    fixtures_path = os.path.join(os.path.dirname(__file__), 'fixtures')
    fixture_data = {}
    print(fixtures_path)
    for filename in (os.listdir(fixtures_path)):
        if os.path.isdir(os.path.join(fixtures_path, filename)):
            continue
        path = os.path.join(fixtures_path, filename)
        with open(path) as f:
            fixture_data[filename] = f.read()
    fixtures = json.loads(to_text(fixture_data['debconf_show_tzdata_amd64.json']))

# Generated at 2022-06-13 05:03:43.342128
# Unit test for function set_selection
def test_set_selection():
    from ansible.module_utils import basic
    from ansible.module_utils import common_koji
    from ansible.module_utils import common_run
    from ansible.module_utils import common_utils
    from ansible.module_utils import system_details
    from ansible.module_utils import system_info
    from ansible.module_utils import task_queue_manager

    # Mock the module object to be created.

# Generated at 2022-06-13 05:03:44.859735
# Unit test for function main
def test_main():
    # TODO: implement unit test of function main
    # main()
    pass

# Generated at 2022-06-13 05:03:56.691189
# Unit test for function set_selection
def test_set_selection():
    #
    # Function to provide arguments to AnsibleModule
    def get_module_args():
        return dict(
            name='locales',
            question='locales/default_environment_locale',
            vtype='select',
            value='fr_FR.UTF-8',
            unseen=False,
        )

    # Function to provide a clean, blank AnsibleModule
    def get_module_obj():
        from ansible.module_utils.basic import AnsibleModule

# Generated at 2022-06-13 05:04:09.141640
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

    pkg = 'test_package'
    question = 'test_question'
    vtype = 'string'

# Generated at 2022-06-13 05:04:21.263005
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils.common.process import get_bin_path
    from ansible.module_utils._text import to_bytes

    setsel = get_bin_path('debconf-set-selections')
    show = get_bin_path('debconf-show')

    # Test case: initial run

# Generated at 2022-06-13 05:04:22.257008
# Unit test for function main
def test_main():
    # TODO:  Write tests for main
    return None

# Generated at 2022-06-13 05:04:29.600272
# Unit test for function get_selections
def test_get_selections():
  from mock import Mock, MagicMock
  from ansible.module_utils.basic import AnsibleModule
  module = AnsibleModule({'name':'apt'})
  
  module.run_command = MagicMock(return_value=(0, "* apt/trust_new_gpg_key boolean true\n* apt/new_gpg_key_id string 0x1AD3814D\n* apt/use_new_gpg_key select true", ''))
  prev = get_selections(module, "apt")
  assert prev['apt/trust_new_gpg_key'] == 'true'
  assert prev['apt/new_gpg_key_id'] == '0x1AD3814D'
  assert prev['apt/use_new_gpg_key'] == 'true'
  
  module.run

# Generated at 2022-06-13 05:04:30.475793
# Unit test for function set_selection
def test_set_selection():
    # This has been tested in the functional test suite
    return True

# Generated at 2022-06-13 05:04:38.911911
# Unit test for function main
def test_main():
    argument_spec = dict(
        name=dict(type='str', required=True, aliases=['pkg']),
        question=dict(type='str', aliases=['selection', 'setting']),
        vtype=dict(type='str', choices=['boolean', 'error', 'multiselect', 'note', 'password', 'seen', 'select', 'string', 'text', 'title']),
        value=dict(type='str', aliases=['answer']),
        unseen=dict(type='bool', default=False),
    )
    main()

# Generated at 2022-06-13 05:04:42.688543
# Unit test for function get_selections
def test_get_selections():
    module = AnsibleModule(argument_spec={})
    pkg = 'tzdata'
    ret = get_selections(module, pkg)
    assert ret['tzdata/Areas'].startswith('America')

# Generated at 2022-06-13 05:05:06.349119
# Unit test for function get_selections
def test_get_selections():
    pass

# Generated at 2022-06-13 05:05:09.894285
# Unit test for function get_selections
def test_get_selections():
    test_selections = {
        'tzdata/Zones/Europe': 'Berlin',
        'tzdata/Zones/America': 'Argentina/Buenos_Aires'
    }
    assert test_selections == get_selections(module, 'tzdata')

# Generated at 2022-06-13 05:05:17.085785
# Unit test for function set_selection
def test_set_selection():
    """
    Test debconf-set-selections call
    """
    test_module = AnsibleModule({}, check_invalid_arguments=False)
    test_module.fail_json.mock_returns = None
    test_module.exit_json.mock_returns = None

    test_module.run_command.mock_returns = (0, "", "")
    set_selection(test_module, "test_pkg", "test", "test", "test")

    test_module.run_command.mock_returns = (1, "", "")
    set_selection(test_module, "test_pkg", "test", "test", "test")

# Generated at 2022-06-13 05:05:21.022451
# Unit test for function get_selections
def test_get_selections():
    selection = {'default': 'ko_KR.UTF-8', 'locales': 'ko_KR.UTF-8 en_US.UTF-8', 'ko_KR.UTF-8': 'ko_KR.UTF-8', 'en_US.UTF-8': 'ko_KR.UTF-8'}
    assert get_selections('locales') == selection

# Generated at 2022-06-13 05:05:27.621807
# Unit test for function set_selection
def test_set_selection():
    # Setup the module
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

    # Try adding a new value
    pkg = 'test'
    question = 'test-question'
    vtype = 'string'
    value = 'test-value'

# Generated at 2022-06-13 05:05:31.340892
# Unit test for function get_selections
def test_get_selections():
    # Stub out the actual module execution
    # For this stub, we will assume the module is run in non-check mode
    class StubModule(object):
        def __init__(self):
            self.check_mode = False

        def run_command(self, command, data=None):
            if "debconf-show tzdata" in command:
                return 0, out, ""
            else:
                return 1, "", "Error"

        def fail_json(self, msg):
            raise Exception("fail_json was called")

        def get_bin_path(self, executable, required=False):
            return executable

    # Use some fake data

# Generated at 2022-06-13 05:05:42.626060
# Unit test for function set_selection
def test_set_selection():
    import os
    import shutil
    import tempfile

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

    tmpdir = tempfile.mkdtemp()
    old_cwd = os

# Generated at 2022-06-13 05:05:51.943666
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

    pkg = "pkg"
    question = "question"
    vtype = "string"
    value = "value"

# Generated at 2022-06-13 05:06:03.037406
# Unit test for function get_selections
def test_get_selections():
    # NOTE: Requires module to be installed to test!
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
    print(get_selections(module, "tzdata"))

# Generated at 2022-06-13 05:06:16.177229
# Unit test for function main
def test_main():
    print("")
    print("============================")
    print(" Debconf Module Test")
    print("============================")

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

    test_

# Generated at 2022-06-13 05:06:55.492009
# Unit test for function get_selections
def test_get_selections():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec=dict())
    prev = get_selections(module, 'tzdata')
    assert prev['tzdata/Areas'] == 'Europe'
    assert prev['tzdata/Zones/Europe'] == 'Berlin'

# Generated at 2022-06-13 05:07:02.076931
# Unit test for function get_selections
def test_get_selections():
    ansible = collections.namedtuple('AnsibleModule', ['run_command', 'fail_json'])
    module = ansible(run_command=run_command_get_selections, fail_json=fail_json)
    result = get_selections(module, 'tzdata')
    assert result['Map'] == 'Europe/Dublin'

# Generated at 2022-06-13 05:07:11.553016
# Unit test for function main
def test_main():

    # Test case for debconf module with no question supplied

    def test(args, result_expected):

        class Args(object):
            pass

        class Module(object):
            def __init__(self):
                self.exit_json = lambda **kwargs: None
                self.fail_json = lambda **kwargs: None
                self.params = args

            def get_bin_path(self, arg1, arg2):
                return 'path'

            def run_command(self, cmd, data=None):
                if cmd == 'path debconf-show path':
                    return 0, '*some line\na question:a value', 'nothing'
                elif cmd == 'path debconf-set-selections':
                    return 0, '', ''

# Generated at 2022-06-13 05:07:18.203125
# Unit test for function main
def test_main():
    import tempfile
    pkg = "test_pkg"
    question = "test_question"
    vtype = "test_vtype"
    value = "test_value"
    unseen = True
    (f, tmppath) = tempfile.mkstemp()
    def cleanup():
        os.close(f)
        os.remove(tmppath)
    cleanup()
    with patch('ansible.module_utils.basic.AnsibleModule') as mock_am:
        mock_module = Mock()
        mock_module.params = {
            "name": pkg,
            "question": question,
            "vtype": vtype,
            "value": value,
            "unseen": True,
        }
        mock_module.check_mode = True
        mock_module._diff = False
        mock

# Generated at 2022-06-13 05:07:22.411815
# Unit test for function get_selections
def test_get_selections():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True, type='str', aliases=['pkg']),
            question=dict(type='str', aliases=['selection', 'setting']),
            vtype=dict(type='str', choices=['boolean', 'error', 'multiselect', 'note', 'password', 'seen', 'select', 'string', 'text', 'title']),
            value=dict(type='str', aliases=['answer']),
        ),
        required_together=(['question', 'vtype', 'value'],),
    )

    pkg = 'tzdata'

# Generated at 2022-06-13 05:07:34.037302
# Unit test for function get_selections
def test_get_selections():
    # Test exists
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

    # Test doesn't exist

# Generated at 2022-06-13 05:07:45.476298
# Unit test for function main
def test_main():
    from ansible.modules.packaging.os import debconf
    from ansible.module_utils.six import StringIO
    from ansible.module_utils.ansible_release import __version__ as ansible_version
    import sys
    module = debconf.__dict__['_AnsibleModule']
    setattr(module, 'run_command', lambda args, data=None, check_rc=True, close_fds=True, executable=None, binary_data=False: (0, '', '') )
    setattr(module, 'get_bin_path', lambda module, required=False, opt_dirs=[] : '/usr/bin/%s' % module )
    setattr(module, 'exit_json', lambda changed=False, msg='', **kwargs : print(kwargs))

# Generated at 2022-06-13 05:07:55.780262
# Unit test for function get_selections
def test_get_selections():
    import os
    import sys
    import copy
    import tempfile
    import subprocess
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.pycompat24 import get_exception
    from ansible_collections.ansible.common.tests.unit.compat.mock import patch, Mock
    from ansible_collections.ansible.common.plugins.modules import debconf

    class APIParameters(object):

        def __getitem__(self, arg):
            return getattr(self, arg)

        def __contains__(self, arg):
            return hasattr(self, arg) and getattr(self, arg)


# Generated at 2022-06-13 05:08:06.453098
# Unit test for function set_selection
def test_set_selection():
    import subprocess

    pkg = 'ansible-test-debconf'
    question = 'ansible-test-debconf/test'
    vtype = 'string'
    value = 'example-setting'
    unseen = False

    (rc, out, err) = set_selection(module, pkg, question, vtype, value, unseen)

    (rc, out, err) = subprocess.getstatusoutput(' '.join(['debconf-show', pkg]))

    assert out == 'ansible-test-debconf/test: example-setting', 'Expected example-setting but got %s' % out

    # Cleanup

# Generated at 2022-06-13 05:08:16.471254
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
    command = [module.get_bin_path('debconf-set-selections', True)]

# Generated at 2022-06-13 05:09:47.069496
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
    assert get_selections(module, 'tzdata')['tzdata/Zones/Europe'] == 'Amsterdam'



# Generated at 2022-06-13 05:09:53.652477
# Unit test for function main
def test_main():
    # Set up mock input
    test_module = AnsibleModule({
        'name': 'test-module',
        'question': 'test-question',
        'vtype': 'string',
        'value': 'test-value',
        'unseen': False,
    })

    # Mock set_selection()
    def mock_set_selection(module, pkg, question, vtype, value, unseen):
        return False, '', ''

    # Mock get_selections()
    def mock_get_selections(module, pkg):
        return {'test-question': 'test-value'}

    # Instantiate module and set up dependencies
    module = AnsibleModule({})
    module.get_bin_path = lambda x, y: 'module-path'
    module.run_command = mock_set_selection
    module

# Generated at 2022-06-13 05:09:54.145994
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:09:55.390108
# Unit test for function get_selections
def test_get_selections():
    assert get_selections({}, "tzdata") is not None

# Generated at 2022-06-13 05:10:04.075739
# Unit test for function main
def test_main():
    # Values for this test
    test_name= 'docker-ce'      # The name of the package to configure
    test_question= None         # The debconf configuration setting to change
    test_vtype= None            # The type of the value supplied
    test_value= None            # The value to set the configuration to
    test_unseen= False          # Do not set 'seen' flag when pre-seeding

    # module = AnsibleModule(
    #     argument_spec=dict(
    #         name=dict(type='str', required=True, aliases=['pkg']),
    #         question=dict(type='str', aliases=['selection', 'setting']),
    #         vtype=dict(type='str', choices=['boolean', 'error', 'multiselect', 'note', 'password', 'seen', 'select', 'string

# Generated at 2022-06-13 05:10:10.121945
# Unit test for function set_selection
def test_set_selection():
  import os
  import shutil
  path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tmp')

# Generated at 2022-06-13 05:10:18.315105
# Unit test for function set_selection
def test_set_selection():
    module = AnsibleModule()
    assert set_selection(module, "test_pkg", "test_qustion", "test_vtype", "test_value", False)
    assert set_selection(module, "test_pkg", "test_qustion", "boolean", "True", False)
    assert set_selection(module, "test_pkg", "test_qustion", "boolean", "False", False)
    assert set_selection(module, "test_pkg", "test_qustion", "boolean", "true", False)
    assert set_selection(module, "test_pkg", "test_qustion", "boolean", "false", False)
    assert set_selection(module, "test_pkg", "test_qustion", "test_vtype", "test_value", True)

# Unit

# Generated at 2022-06-13 05:10:30.634277
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


# Generated at 2022-06-13 05:10:37.321185
# Unit test for function set_selection
def test_set_selection():
    from ansible.module_utils.ansible_release import __version__
    import re
    import sys
    import os.path
    sys.path = ["./lib"] + sys.path

    import debconf_utils
    import debconf_parser
    import ansible.module_utils.debconf

    ansible.module_utils.debconf.os.path.isdir = lambda path: path == "/etc/debconf-test-selections"
    debconf_utils.mkdir = lambda path: None
    debconf_utils.chmod = lambda path, mode: None
    debconf_utils.save_selection = lambda pkg, question, vtype, value, unseen, filepath: None

    fn = os.path.dirname(__file__) + '/test/fixtures/files/debconf_test'

# Generated at 2022-06-13 05:10:40.241069
# Unit test for function get_selections
def test_get_selections():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_text
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    pkg = 'fcron'
    selections = get_selections(module, pkg)
    assert selections['fcron/purge_old_nologins'] == 'true'
