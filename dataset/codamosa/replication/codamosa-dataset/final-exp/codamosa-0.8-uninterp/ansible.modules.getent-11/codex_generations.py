

# Generated at 2022-06-13 05:23:54.560986
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=False),
            service=dict(type='str'),
            split=dict(type='str'),
            fail_key=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )

    colon = ['passwd', 'shadow', 'group', 'gshadow']

    database = module.params['database']
    key = module.params.get('key')
    split = module.params.get('split')
    service = module.params.get('service')
    fail_key = module.params.get('fail_key')

    getent_bin = module.get_bin_path('getent', True)

   

# Generated at 2022-06-13 05:24:02.893170
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=False),
            service=dict(type='str'),
            split=dict(type='str'),
            fail_key=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )
    colon = ['passwd', 'shadow', 'group', 'gshadow']

    database = module.params['database']
    key = module.params.get('key')
    split = module.params.get('split')
    service = module.params.get('service')
    fail_key = module.params.get('fail_key')

    assert key is not None
    assert database == 'passwd'

# Generated at 2022-06-13 05:24:09.709336
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=False),
            service=dict(type='str'),
            split=dict(type='str'),
            fail_key=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )

    assert main() == 1

"""
to run test and get coverage report:

nosetests -v --with-coverage --cover-package=getent
"""

# Generated at 2022-06-13 05:24:19.734083
# Unit test for function main
def test_main():
  fld = "ansible_facts"
  kys = ["getent_shadow", "getent_services", "getent_group", "getent_passwd", "getent_hosts"]
  vals = {'getent_shadow': 'list', 'getent_services': 'list', 'getent_group': 'list', 'getent_passwd': 'list', 'getent_hosts': 'list'}
  res = main()
  assert fld in res
  assert type(res["ansible_facts"]) == dict
  for k in kys:
    assert k in res[fld]
    assert type(res[fld][k]) == vals[k]

# Generated at 2022-06-13 05:24:31.068280
# Unit test for function main
def test_main():
    # Mock module
    module = mock.MagicMock(spec=AnsibleModule)
    # Mock check_mode
    module.check_mode = False
    # Mock params
    params = dict(
        database='passwd',
        key='root',
    )
    module.params = params
    # Mock get_bin_path
    get_bin_path = mock.MagicMock(return_value='/usr/bin/getent')
    module.get_bin_path = get_bin_path
    # Mock run_command
    run_command = mock.MagicMock(return_value=(0, 'root:x:0:0:root:/root:/bin/bash\n'))
    module.run_command = run_command
    # Call the main function
    main()

# Generated at 2022-06-13 05:24:42.591148
# Unit test for function main
def test_main():
    # noinspection PyUnresolvedReferences
    from ansible.module_utils import basic
    # noinspection PyUnresolvedReferences
    from ansible.module_utils._text import to_native

    fake_module = basic.AnsibleModule(argument_spec=dict(
        database='group',
        key='root',
        split=None,
        fail_key=True,
    ),
        supports_check_mode=True,
        check_invalid_arguments=False,
    )
    commands = {
        'getent': 'GETENT',
    }

    # Fake main import
    main_obj = main()

    # Fake run_command
    def run_command(module, cmd):
        if module not in commands:
            raise Exception("Unexpected module")

# Generated at 2022-06-13 05:24:43.242884
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:24:52.352160
# Unit test for function main
def test_main():

    class Mock_module(object):
        def __init__(self, **kwargs):
            self.params = kwargs

        def get_bin_path(self, _, required):
            if required:
                raise Exception("getent_bin not found")
            return 'getent_bin'

        @staticmethod
        def run_command(cmd):
            if cmd[1] == 'passwd':
                return 0, 'root:x:0:0:root:/root:/bin/bash', ''
            else:
                return 2, '', ''

        @staticmethod
        def fail_json(msg, exception=None):
            raise Exception(msg)


# Generated at 2022-06-13 05:25:01.219098
# Unit test for function main
def test_main():
    import sys
    from io import StringIO
    from unittest import mock

    module_args={'database': 'passwd', 'key': 'root'}

    # function get_bin_path is mocked
    with mock.patch('ansible_collections.ansible.community.plugins.modules.getent.get_bin_path') as bin_path, mock.patch.object(sys, 'argv', ['ansible-test', '-m', 'getent.py']):
        bin_path.return_value = 'getent'

# Generated at 2022-06-13 05:25:07.199279
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=False),
            service=dict(type='str'),
            split=dict(type='str'),
            fail_key=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )

    colon = ['passwd', 'shadow', 'group', 'gshadow']

    database = module.params['database']
    key = module.params.get('key')
    split = module.params.get('split')
    service = module.params.get('service')
    fail_key = module.params.get('fail_key')

    getent_bin = module.get_bin_path('getent', True)

   

# Generated at 2022-06-13 05:25:22.147913
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:25:33.158253
# Unit test for function main
def test_main():
    import json
    import sys
    import os
    import uuid
    from ansible.module_utils.facts import Facts
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common.collections import is_iterable

    current_path = os.path.dirname(os.path.realpath(__file__))

    with open(current_path+'/getent.json') as json_data:
        test_data = json.load(json_data)
        json_data.close()


# Generated at 2022-06-13 05:25:45.549849
# Unit test for function main
def test_main():
    import sys
    import tempfile
    import textwrap
    import shutil
    import os

    (fd, tmppath) = tempfile.mkstemp()
    os.close(fd)

    shutil.copy('/etc/passwd', tmppath)

    # quick edit to /tmp/passwd
    with open(tmppath, 'r+') as file_:
        content = file_.read()
        file_.seek(0)
        content_new = content.replace('nobody:x:99:99:Nobody:/:/sbin/nologin',
                                      'nobody:x:99:99:Nobody:new:/sbin/nologin')
        file_.write(content_new)
        file_.truncate()


# Generated at 2022-06-13 05:25:59.493740
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule

    def run_main(module, method):
        getent_bin = module.get_bin_path('getent', True)
        if getent_bin is None:
            module.fail_json(msg="Unable to locate binary")
        getent_bin = getent_bin + ' '

        if method == 'pass':
            module.run_command = lambda cmd: (0, getent_bin + cmd)
        elif method == 'fail_with_key':
            module.run_command = lambda cmd: (2, getent_bin + cmd)
        elif method == 'fail_without_key':
            module.run_command = lambda cmd: (1, getent_bin + cmd)

# Generated at 2022-06-13 05:26:01.760447
# Unit test for function main
def test_main():
    from ansible.module_utils.facts.system.getent import main
    result = main()
    print(result)
    assert result == 'foo'

# Generated at 2022-06-13 05:26:10.429152
# Unit test for function main
def test_main():
    '''
    ansible_facts:
      contains:
        getent_<database>:
          description:
            - A list of results or a single result as a list of the fields the db provides
            - The list elements depend on the database queried, see getent man page for the structure
            - Starting at 2.11 it now returns multiple duplicate entries, previouslly it only returned the last one
          returned: always
          type: list
    '''
    pass

# Generated at 2022-06-13 05:26:21.820555
# Unit test for function main
def test_main():
    import mock
    import json

    # Use request mock to return a summary of the topic
    request_mock = mock.Mock(side_effect=[
        ('127.0.0.1', 1, 'localhost'),
        ('127.0.0.1', 1, 'localhost'),
        ('127.0.0.1', 1, 'localhost'),
        ('127.0.0.1', 1, 'localhost'),
        ('127.0.0.1', 1, 'localhost'),
        ('127.0.0.1', 1, 'localhost'),
    ])


# Generated at 2022-06-13 05:26:34.815096
# Unit test for function main
def test_main():
    import time
    import json
    import os

    # the following imports make sure the mocked functions get loaded before any real function is called
    import ansible.module_utils.basic
    import ansible.module_utils._text
    from ansible.module_utils import action
    from ansible.module_utils.common.collections import ImmutableDict

    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.action.getent_module import process_output

    ACTIVE_MODULE_ARGS = dict(
        database='passwd',
        key='root',
        split=':',
    )


# Generated at 2022-06-13 05:26:41.169610
# Unit test for function main
def test_main():
    getent_bin = '/usr/bin/getent'

    def remove(str1):
        return str1.remove('\n')

    rc, out, err = module.run_command([getent_bin, 'passwd', 'root'])
    out = out.split(':')
    assert rc == 0
    assert out.remove('\n') == ['root', 'x', '0', '0', 'root', '/root', '/bin/bash']
    assert out[1] == 'x'
    assert out[2] == '0'
    assert out[3] == '0'
    assert out[4] == 'root'
    assert out[5] == '/root'
    assert out[6] == '/bin/bash'

# Generated at 2022-06-13 05:26:48.917868
# Unit test for function main
def test_main():
    # Test module import
    from ansible.modules.extras.linux.getent import main

    # Test module return values
    args = dict(
        database='passwd',
        key='root',
    )

    rc, out, err = main(args)
    assert rc == 0
    assert out is not None

    # TODO: Test module execution when the database is not supported
    # TODO: Test module execution when we run in check mode

# Generated at 2022-06-13 05:27:19.372679
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=True),
        )
    )
    results = main()
    assert results['ansible_facts']

# Generated at 2022-06-13 05:27:29.399788
# Unit test for function main

# Generated at 2022-06-13 05:27:34.105668
# Unit test for function main
def test_main():
    test_module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=False),
            key=dict(type='str', no_log=False),
            split=dict(type='str'),
            fail_key=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )
    test_module.params['database'] = 'passwd'
    test_module.params['key'] = 'test_user'
    test_module.params['split'] = ':'

    test_main()

# Generated at 2022-06-13 05:27:39.659095
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule

    def getent_run_command_fail(module, cmd):
        return 0, "some line", "some error"

    def getent_run_command_success(module, cmd):
        return 0, "root:x:0:0:root:/root:/bin/bash\n" \
                  "bin:x:1:1:bin:/bin:/sbin/nologin\n" \
                  "nobody:x:65534:65534:nobody:/nonexistent:/sbin/nologin", ""

    def getent_run_command_error(module, cmd):
        return 1, None, ""

    def getent_run_command_notfound(module, cmd):
        return 2, None, ""


# Generated at 2022-06-13 05:27:48.789224
# Unit test for function main
def test_main():
    import sys
    import re
    module = AnsibleModule(argument_spec={'database': dict(type='str', required=True)}, supports_check_mode=True)

    check_mode = module.check_mode
    diff_mode = module.params['diff_mode']
    facts_mode = module.params['facts']
    platform = module.params['platform']

    # Setup environment vars needed by getent
    sys.environ["LANG"] = "C"
    sys.environ["LC_ALL"] = "C"

    try:
        from ansible.module_utils.getent import getent
    except Exception as e:
        module.exit_json(msg=to_native(e), exception=traceback.format_exc())
        #module.fail_json(msg="failed to import getent module: %s

# Generated at 2022-06-13 05:27:51.167967
# Unit test for function main
def test_main():
    pass

'''
TO DO
  - check getent and what it returns
  - implement action ?
'''

# Generated at 2022-06-13 05:28:02.130241
# Unit test for function main
def test_main():
    import tempfile
    import os
    from ansible.module_utils.common.collections import ImmutableDict
    from collections import namedtuple
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_native


# Generated at 2022-06-13 05:28:03.564353
# Unit test for function main
def test_main():
    with pytest.raises(SystemExit):
        main()

# Generated at 2022-06-13 05:28:11.029479
# Unit test for function main
def test_main():
    import os
    import tempfile
    import pytest
    import json
    import subprocess
    import textwrap

    # When getent is not installed, ansible should fail with msg and fail_json
    def test_missing_getent():
        m = ansible.module_utils.basic.AnsibleModule(
            argument_spec=dict(
                database=dict(type='str', required=True),
                key=dict(type='str', no_log=False),
                service=dict(type='str'),
                split=dict(type='str'),
                fail_key=dict(type='bool', default=True),
            ),
            supports_check_mode=True,
        )
        m.get_bin_path = lambda x, y: None
        m.run_command = lambda x: (1, None, None)

# Generated at 2022-06-13 05:28:21.014870
# Unit test for function main
def test_main():

    import sys
    import os
    import subprocess
    import datetime
    import pytz
    import random
    import json
    import time

    from ansible.module_utils.basic import *

    print("Running unittest for  main")

    # define facts to save (will be used as arguments)
    facts = {}

    # Save arguments into facts
    facts["database"] = "passwd"
    facts["key"] = "root"

    # Set up environment
    os.environ['ANSIBLE_MODULE_ARGS'] = json.dumps(facts)


# Generated at 2022-06-13 05:29:39.839091
# Unit test for function main
def test_main():
    import pytest

    # Unit tests do not automatically get the main() function's arguments.
    # You must pass them in as named arguments.
    #
    # You can also access the main function's attributes.
    #
    # The main function returns a dict of the form:
    # {'ansible_facts': {'<database>': <data>}}


    # Unit test the main function using pytest.

    # Mock the module class.
    # This will allow you to set return values, side_effect functions, etc.
    # See https://docs.pytest.org/en/latest/reference.html for more info.

    # To get the module's arguments, you need to get the class instance.
    # The module instance is called 'cls'.

# Generated at 2022-06-13 05:29:52.625064
# Unit test for function main
def test_main():
    import os
    import sys
    import inspect
    import mock

    # set up imports
    # import module snippets
    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    parentdir = os.path.dirname(currentdir)
    sys.path.insert(0, parentdir)
    import ansible.module_utils.basic  as basic
    import ansible.module_utils._text  as text
    import ansible.module_utils.action as action
    import ansible.modules.system  as system
    import plugins.modules.getent as getent

    getent.AnsibleModule = mock.Mock()
    getent.AnsibleModule.params = {
        'database': 'passwd'
    }
    getent.An

# Generated at 2022-06-13 05:29:53.161008
# Unit test for function main
def test_main():
    test_main()

# Generated at 2022-06-13 05:29:54.022373
# Unit test for function main
def test_main():
    main()


# Generated at 2022-06-13 05:30:00.047348
# Unit test for function main
def test_main():

    class mock_module:
        def __init__(self, key, database, split=None, service=None, fail_key=True):
            self.params = {
                'key': key,
                'database': database,
                'split': split,
                'service': service,
                'fail_key': fail_key
            }

        def get_bin_path(self, name, true):
            return '/bin/getent'

        def run_command(self, cmd):
            self.cmd = cmd

            if database == "services":
                if key == "ssh":
                    return (0, 'ssh\t22/tcp', '')
                else:
                    return (2, '', '')

# Generated at 2022-06-13 05:30:10.824292
# Unit test for function main
def test_main():
    import subprocess
    import datetime
    import json

    # Test with no parameters
    p = subprocess.Popen(['ansible-playbook', 'test_getent.yml', '-v',
                          '-e', 'getent_database=passwd',
                          '-e', 'getent_key=root'],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    if p.returncode != 0:
        print('STDOUT:', out)
        print('STDERR:', err)
        raise RuntimeError('test failed')

    # Parse the facts
    facts = json.loads(out)
    passwd = facts['ansible_facts']['getent_passwd']['root']

# Generated at 2022-06-13 05:30:21.801109
# Unit test for function main
def test_main():
    with patch("ansible_collections.ansible.community.plugins.modules.getent.AnsibleModule", MockAnsibleModule):
        obj = getent()
        x = "someval"
        obj.run_command = MagicMock(return_value=(0, "", ""))
        obj.get_bin_path = MagicMock(return_value="/usr/bin/getent")
        obj.main()
        args, kwargs = obj.run_command.call_args
        assert "/usr/bin/getent hosts {}".format(x) in args

# Generated at 2022-06-13 05:30:31.332361
# Unit test for function main
def test_main():
    import tempfile
    import os
    import shutil

    tmp = os.path.join(tempfile.gettempdir(), 'getent')
    os.makedirs(tmp)
    shutil.copy(__file__, os.path.join(tmp, 'ansible.module_utils.getent.py'))
    shutil.copy(__file__, os.path.join(tmp, 'ansible'))

    module_args = dict(database='test', split=':')
    module_args['testdb'] = """v1:1\nv2:2\nv3:3\nv3:3\nv3:3\nv4"""


# Generated at 2022-06-13 05:30:44.214825
# Unit test for function main
def test_main():
    # Test with no split, passwd, and key
    testdata1 = {
        "database": "passwd",
        "key": "vagrant"
    }
    # Test with split and key
    testdata2 = {
        "database": "group",
        "key": "vagrant",
        "split": ":"
    }
    # Test with no split, hosts and no key
    testdata3 = {
        "database": "hosts"
    }
    # Test with split, hosts and no key
    testdata4 = {
        "database": "hosts",
        "split": ":"
    }
    # Test with no split and no key
    testdata5 = {
        "database": "passwd"
    }
    # Test with no split, service and key

# Generated at 2022-06-13 05:30:57.292619
# Unit test for function main
def test_main():
    ''' test getent module '''
    test_spec1 = dict(database='passwd', key='root', split=':')
    test_spec2 = dict(database='group', key='root', split=':')
    test_spec3 = dict(database='hosts', key='localhost', split='\t')
    test_spec4 = dict(database='services', key='http', split='\t')
    test_spec5 = dict(database='shadow', key='root', split=':')
    test_specs = [test_spec1, test_spec2, test_spec3, test_spec4, test_spec5]
