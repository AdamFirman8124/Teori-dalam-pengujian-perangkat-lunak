

# Generated at 2022-06-13 05:02:38.949497
# Unit test for function main
def test_main():
    # Test 1
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

    # Set argument's value to a valid value
    pkg = 'locales'

# Generated at 2022-06-13 05:02:47.080261
# Unit test for function set_selection
def test_set_selection():

    class FakeModule(object):
        def __init__(self, pkg, question, vtype, value, unseen):
            self.params = {"name": pkg, "question": question, "vtype": vtype, "value": value, "unseen": unseen}

        def get_bin_path(self, name, required=False):
            return 'fake'

        def run_command(self, command, data=None):
            return [1, None, None]

    # TODO: add more testcases
    module = FakeModule("fake_pkg", 'fake/answer', 'fake_vtype', 'fake_value', 'fake_unseen')
    question = module.params["question"]
    vtype = module.params["vtype"]
    value = module.params["value"]

# Generated at 2022-06-13 05:02:54.389697
# Unit test for function set_selection
def test_set_selection():
    from ansible.module_utils.basic import AnsibleModule
    import json

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


# Generated at 2022-06-13 05:03:03.611338
# Unit test for function get_selections
def test_get_selections():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', aliases=['pkg']),
            question=dict(type='str', aliases=['selection', 'setting']),
            vtype=dict(type='str', choices=['boolean', 'error', 'multiselect', 'note', 'password', 'seen', 'select', 'string', 'text', 'title']),
            value=dict(type='str', aliases=['answer']),
            unseen=dict(type='bool', default=False),
        ),
        required_together=(['question', 'vtype', 'value'],),
        supports_check_mode=True,
    )
    get_selections(module, 'tzdata')

# Generated at 2022-06-13 05:03:10.822275
# Unit test for function get_selections
def test_get_selections():
    import sys
    import os
    sys.path.append(os.getcwd())
    from debconf import get_selections
    my_dict = {"tzdata/Zones/Asia":"Asia/Kolkata","tzdata/Zones/Africa":"Africa/Harare"}
    # def get_selections(module, pkg):
    #     cmd = [module.get_bin_path('debconf-show', True)]
    #     rc, out, err = module.run_command(' '.join(cmd))
    #     selections = {}
    #     for line in out.splitlines():
    #         (key, value) = line.split(':', 1)
    #         selections[key.strip('*').strip()] = value.strip()
    #     return selections

# Generated at 2022-06-13 05:03:14.100618
# Unit test for function main

# Generated at 2022-06-13 05:03:20.387132
# Unit test for function main
def test_main():
    import os
    import json
    import sys
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.module_utils.python import DictDiffer

    def _load_json(file):
        with open(file, 'rb') as f:
            return json.load(f)

    def _dump_json(file, data):
        with open(file, 'wb') as f:
            json.dump(data, f, indent=2)

    def _fail(module, msg):
        sys.stderr.write(msg)
        sys.stderr.write('\n')
        sys.exit(1)


# Generated at 2022-06-13 05:03:24.060928
# Unit test for function set_selection
def test_set_selection():
    rc, out, err = set_selection(module, pkg, question, vtype, value, unseen)
    assert rc == 0


# Generated at 2022-06-13 05:03:36.070267
# Unit test for function get_selections
def test_get_selections():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common.collections import Mapping
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
    get_selections(module, None)


# Generated at 2022-06-13 05:03:48.851071
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


# Generated at 2022-06-13 05:03:58.671026
# Unit test for function get_selections
def test_get_selections():
    assert get_selections(unseen) == unseen

# Generated at 2022-06-13 05:04:09.648932
# Unit test for function get_selections
def test_get_selections():
    # type: () -> None
    """
    Unit test function main()
    """
    # Set up argument spec
    module_args = dict(
        name=dict(type='str', required=True, aliases=['pkg']),
        question=dict(type='str', aliases=['selection', 'setting']),
        vtype=dict(type='str', choices=['boolean', 'error', 'multiselect', 'note', 'password', 'seen', 'select', 'string', 'text', 'title']),
        value=dict(type='str', aliases=['answer']),
        unseen=dict(type='bool', default=False),
    )

    # Create instance of AnsibleModule

# Generated at 2022-06-13 05:04:21.958501
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

# Generated at 2022-06-13 05:04:32.050659
# Unit test for function main
def test_main():
    test = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', required=True, aliases=['pkg']),
            question=dict(type='str', aliases=['selection', 'setting']),
            vtype=dict(type='str', choices=['boolean', 'error', 'multiselect', 'note', 'password', 'seen', 'select', 'string', 'text', 'title']),
            value=dict(type='str', aliases=['answer']),
        ),
        required_together=(['question', 'vtype', 'value'],),
        supports_check_mode=True,
    )
    main()
    #test.exit_json(msg='test')

# Generated at 2022-06-13 05:04:33.711420
# Unit test for function main
def test_main():
    # TODO: Implement unit test for function main
    assert True == True

# Generated at 2022-06-13 05:04:43.888523
# Unit test for function main
def test_main():
    import json
    import sys

    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', required=True, aliases=['pkg']),
            question=dict(type='str', aliases=['selection', 'setting']),
            vtype=dict(type='str', choices=['boolean', 'error', 'multiselect', 'note', 'password', 'seen', 'select', 'string', 'text', 'title']),
            value=dict(type='str', aliases=['answer']),
            unseen=dict(type='bool', default=False),
        )
    )

    # we need to do this since the json encoder will fail on unserializable values (like booleans)

# Generated at 2022-06-13 05:04:50.157652
# Unit test for function set_selection
def test_set_selection():
    class module:
        @staticmethod
        def get_bin_path(cmd, required):
            return 'debconf-set-selections'
        @staticmethod
        def run_command(cmd, data):
            return (0, '', '')
    assert set_selection(module, 'foo', 'bar', 'boolean', 'false', False) == (0, '', '')

# Generated at 2022-06-13 05:05:00.886210
# Unit test for function get_selections
def test_get_selections():

    # import the module, blank out the parameters
    module = AnsibleModule(argument_spec={})

    # create a fake module with the correct name
    class FakeModule(object):
        def __init__(self, path, name):
            self.path = path
            self.name = name

        @classmethod
        def get_bin_path(self, name, required):
            return self.path

    # create a fake module with the correct name
    class FakeRC(object):
        def __init__(self, rc, out, err):
            self.rc = rc
            self.out = out
            self.err = err

    # create a fake module with the correct rc and output
    class FakeModuleRun(object):
        def __init__(self, rc, out, err):
            self.rc = rc
            self.out

# Generated at 2022-06-13 05:05:01.504164
# Unit test for function get_selections
def test_get_selections():
    return main()

# Generated at 2022-06-13 05:05:12.082976
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

    pkg = module.params["name"]
    test_selections = get_selections(module, pkg)
    

# Generated at 2022-06-13 05:05:31.641095
# Unit test for function get_selections
def test_get_selections():
    invalid_question = get_selections('test')
    assert invalid_question is None
    valid_question = get_selections(module, pkg)
    assert valid_question is not None

# Generated at 2022-06-13 05:05:32.951886
# Unit test for function get_selections
def test_get_selections():
    assert(get_selections('tzdata') is not None)

# Generated at 2022-06-13 05:05:37.198210
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

# Generated at 2022-06-13 05:05:48.316414
# Unit test for function set_selection
def test_set_selection():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.basic import get_exception
    from ansible.module_utils.six import PY2
    from ansible.module_utils._text import to_bytes, to_text
    import sys
    import os

    cur_dir = os.path.dirname(__file__)
    libraries_path = cur_dir + "/../../../lib/"

    # ansible is not installed, do the manual path manipulation
    if libraries_path not in sys.path:
        sys.path.append(libraries_path)

# Generated at 2022-06-13 05:05:59.112796
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


# Generated at 2022-06-13 05:05:59.507699
# Unit test for function set_selection
def test_set_selection():
    pass

# Generated at 2022-06-13 05:06:03.845527
# Unit test for function get_selections
def test_get_selections():
    r = get_selections(None, "glpi")
    assert r["glpi/db_admin_pass"] == ""
    assert r["glpi/default_language"] == "en_GB"
    assert r["glpi/db_type"] == "mysql"
    assert r["glpi/db_type_autoconf"] == "true"
    assert r["glpi/db_user"] == "root"
    assert r["glpi/db_host"] == "localhost"
    assert r["glpi/reconfigure-webserver"] == "apache2"

# Generated at 2022-06-13 05:06:16.952621
# Unit test for function main
def test_main():
    from ansible.module_utils import argspec

    argspec.get_default_argspec = lambda self: argspec.RawTextArgumentSpec(no_log=True)


# Generated at 2022-06-13 05:06:22.157469
# Unit test for function main
def test_main():
    import json
    import subprocess
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.debconf import get_selections, set_selection

    # Load test data
    data = json.loads('''
        {"version": 2,
        "params": {"name": "tzdata",
        "question": "tzdata/Zones/US",
        "vtype": "select",
        "value": "America/New_York",
        "unseen": true}}
        ''')

    # Set common properties
    module = basic.AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True,
    )
    module.params = data["params"]
    module.exit_json = basic.Ansible

# Generated at 2022-06-13 05:06:34.249211
# Unit test for function set_selection
def test_set_selection():
    import subprocess
    import os
    import unittest

    class TestShellCmd(unittest.TestCase):
        """test shell command"""
        def setUp(self):
            """create tmp file"""
            fd = os.open('/etc/hosts', os.O_RDWR|os.O_CREAT)
            os.close(fd)
            os.chmod('/etc/hosts', 0o600)

        def tearDown(self):
            """remove tmp file"""
            os.remove('/etc/hosts')

        def test_get_shell_cmd(self):
            """test if get_shell_cmd is returning the correct output"""
            cmd = 'touch /etc/hosts'

# Generated at 2022-06-13 05:07:17.514382
# Unit test for function get_selections
def test_get_selections():
    '''
    make sure argument_spec exists, if not throw an error
    '''
    assert get_selections, 'argument_spec is missing'

# Generated at 2022-06-13 05:07:23.798345
# Unit test for function set_selection
def test_set_selection():
    assert set_selection(module, "nginx", "nginx/http_port", "string", "80") == (0, '', '')
    assert set_selection(module, "nginx", "nginx/http_port", "string", "8080") == (0, '', '')
    assert set_selection(module, "nginx", "nginx/http_port", "string", "808080") == (1, '', 'errormsg')

# Generated at 2022-06-13 05:07:25.705165
# Unit test for function main
def test_main():
    assert main()



# Generated at 2022-06-13 05:07:32.306218
# Unit test for function set_selection
def test_set_selection():
    # test hashbang
    assert set_selection('/usr/local/bin/python3.7', 'pgsql', 'postgresql-common/install-error-allow-peer', 'boolean', 'true', False)
    # test tuple of cmd and data
    assert set_selection(['/usr/local/bin/python3.7', '-u'], 'pgsql', 'postgresql-common/install-error-allow-peer', 'boolean', 'true', True)


# Generated at 2022-06-13 05:07:43.810729
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
    question = 'question'
    vtype = 'vtype'
    value = 'value'
    unseen = 'unseen'
    rc

# Generated at 2022-06-13 05:07:54.799581
# Unit test for function get_selections
def test_get_selections():
    from ansible.module_utils.basic import AnsibleModule

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

    from ansible.module_utils.debconf import get_selections

# Generated at 2022-06-13 05:08:05.704356
# Unit test for function get_selections

# Generated at 2022-06-13 05:08:15.788421
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
    results = get_selections(module, "tzdata")

# Generated at 2022-06-13 05:08:20.425186
# Unit test for function get_selections
def test_get_selections():
    module_args=dict(
        name='tzdata'
    )
    output=get_selections(module_args, pkg)

    assert output == {'tzdata/Areas': '', 'tzdata/Zones/Africa': ''}


# Generated at 2022-06-13 05:08:29.002778
# Unit test for function get_selections
def test_get_selections():
    '''
    Test function get_selections
    '''

    # Following test use the following command to return:
    # debconf-show locales
    # locales/default_environment_locale: fr_FR.UTF-8
    # locales/locales_to_be_generated: en_US.UTF-8 UTF-8, fr_FR.UTF-8 UTF-8

    # Initialize the module object
    module = AnsibleModule(argument_spec={})
    pkg = 'locales'

    # Set the run_command return code and output

# Generated at 2022-06-13 05:09:52.019026
# Unit test for function set_selection
def test_set_selection():
    setsel = module.get_bin_path('debconf-set-selections', True)
    cmd = [setsel]
    if unseen:
        cmd.append('-u')
    data = ' '.join([pkg, question, vtype, value])
    return module.run_command(cmd, data=data)

# Generated at 2022-06-13 05:09:59.627516
# Unit test for function set_selection
def test_set_selection():
    args = dict(
        question="localepurge/use-dpkg",
        vtype="boolean",
        value="true",
        unseen="False",
    )
    # AnsibleModule takes care of the input arguments
    module = AnsibleModule(argument_spec=dict(
        question     = dict(required=True),
        vtype        = dict(required=True),
        value        = dict(required=True),
        unseen       = dict(required=True),
    ), **args)
    # Call module
    rc, msg, out = set_selection(module,"localepurge","localepurge/use-dpkg","boolean","true","False")
    return msg, rc


# Generated at 2022-06-13 05:10:06.660457
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

# Generated at 2022-06-13 05:10:11.940932
# Unit test for function set_selection
def test_set_selection():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    # Test success with Boolean
    assert set_selection(module, 'test-package', 'question', 'boolean', 'true', False) is None

    # Test success with string
    assert set_selection(module, 'test-package', 'question', 'string', 'test_string', False) is None


# Generated at 2022-06-13 05:10:19.016832
# Unit test for function get_selections
def test_get_selections():
    import subprocess
    import os

    test_package = "tzdata"
    debconf_show = [os.environ["PATH"].split(":")[0] + "/debconf-show", test_package]

    rc, out, err = subprocess.Popen(debconf_show, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    rc = int(rc)
    assert(rc == 0)

    selections = {}

    for line in out.splitlines():
        (key, value) = line.split(':', 1)
        selections[key.strip('*').strip()] = value.strip()

    assert(get_selections(test_package) == selections)

# Generated at 2022-06-13 05:10:31.399416
# Unit test for function main
def test_main():
    import os
    import sys
    import tempfile

    # language=Python
    # Mock input args and create temp directory for answers file
    package = 'my-package'
    question = 'my-question'
    vtype = 'my-type'
    value = 'my-value'
    unseen = False

    tmpdir = tempfile.mkdtemp()
    answers_tmpfile = os.path.join(tmpdir, 'answers')

    # Write args to answers file in temp directory
    with open(answers_tmpfile, 'w') as f:
        f.write('\n'.join([package, question, vtype, value]))

    # Mock sys.argv

# Generated at 2022-06-13 05:10:34.622476
# Unit test for function get_selections
def test_get_selections():
    module = AnsibleModule(argument_spec = dict())

    selections = get_selections(module, 'nail')
    assert 'nail/mailto' in selections
    assert 'nail/copies' in selections
    assert 'nail/headerfrom' in selections


# Generated at 2022-06-13 05:10:35.776963
# Unit test for function set_selection
def test_set_selection():
    main()

# Generated at 2022-06-13 05:10:48.443140
# Unit test for function set_selection
def test_set_selection():
    class DummyModule:
        def __init__(self):
            self.params = dict(
                name = "dummypkg",
                question = "dummyquestion",
                vtype = "string",
                value = "dummyvalue",
                unseen = False
            )

        def get_bin_path(self, *args, **kwargs):
            return "debconf-set-selections"

        def run_command(self, *args, **kwargs):
            return 0, "", ""

    module = DummyModule()
    rc, msg, err = set_selection(module, "dummypkg", "dummyquestion", "string", "dummyvalue", False)
    assert rc == 0
    assert msg == ""
    assert err == ""


# Generated at 2022-06-13 05:10:55.208701
# Unit test for function set_selection
def test_set_selection():
    """
    Test set_selection function.
    """
    import sys
    import os
    import unittest
    import tempfile
    
    class TestDebconfModule(unittest.TestCase):
        """
        Unit test for TestDebconfModule.
        """

        def setUp(self):
            """
            Setup test fixture.
            """
            self.old_path = sys.path[:]
            sys.path.append(os.path.join(os.path.dirname(__file__), '../../lib'))
            self.temp_file = tempfile.NamedTemporaryFile()
            self.temp_file.write(b'fake debconf-set-selections results')
            self.temp_file.seek(0)
        