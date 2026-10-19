

# Generated at 2022-06-13 05:23:56.442117
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.six import PY2

    class Args(object):
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

    # Arrange
    if PY2:
        import sys
        sys.modules['ansible'] = ImmutableDict(version_info=(2, 11, 0, '', '', '', ''))
    else:
        import sys
        sys.modules['ansible'] = ImmutableDict(version_info=(3, 0, 0, '', '', '', ''))

    monkeypatch = basic.AnsibleModule

# Generated at 2022-06-13 05:24:04.273012
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.compat.argparse import Namespace

    m_args = Namespace()
    m_args.database = 'passwd'
    m_args.key = 'root'
    m_args.fail_key = True

    fake_in = ImmutableDict(ANSIBLE_MODULE_ARGS=m_args.__dict__)

    m_exit = basic.AnsibleModule(argument_spec={},
                                 supports_check_mode=True,
                                 bypass_checks=True)

    orig_run_command = m_exit._run_command


# Generated at 2022-06-13 05:24:13.040371
# Unit test for function main
def test_main():
    print('Testing function main...')

    import sys
    import os
    import shutil
    import tempfile
    import subprocess
    import re

    path_root = os.path.abspath(os.path.realpath(os.path.dirname(os.path.realpath(__file__)) + '/..'))
    sys.path.append(path_root)

    # create a new instance of the module to be tested
    # this will populate the module object with the wrong values
    # but that is ok because we are only testing function main()

# Generated at 2022-06-13 05:24:14.954802
# Unit test for function main
def test_main():
  import sys
  import os
  import shutil
  
  main()


# Generated at 2022-06-13 05:24:23.847346
# Unit test for function main
def test_main():
    module_args = {
        "database": "passwd",
        "key": "root",
        "service": None,
        "split": None,
        "fail_key": True
    }

    # (rc, out, err):
    # rc: return code of the command
    # out: the stdout from running the command
    # err: the stderr from running the command


# Generated at 2022-06-13 05:24:33.997859
# Unit test for function main
def test_main():
    import sys
    argv_orig = sys.argv

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_native
    from ansible_collections.ansible.community.tests.unit.compat.mock import MagicMock, patch

    def get_bin_path(name, required=False):
        return 'getent_bin'

    def run_command(cmd):
        return 0, '', ''

    class FakeModule(object):
        def __init__(self):
            self.params = {}

        def fail_json(self, msg):
            raise AssertionError(msg)

        def exit_json(self, msg):
            pass

    def setup_module_object(module_values):
        module = FakeModule()
        module.run_

# Generated at 2022-06-13 05:24:37.054903
# Unit test for function main
def test_main():
    import imp
    import os
    import sys
    import tempfile

    ansible_module = imp.load_source(os.path.basename(__file__), os.path.abspath(__file__))
    # TODO: replace the next line with the actual test
    assert ansible_module.main() is None


# Generated at 2022-06-13 05:24:45.995011
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
        supports_check_mode=True
    )

    dbtree = 'getent_%s' % database
    result = {dbtree: {}}
    result[dbtree]['somekey'] = ['a', 'b', 'c']
    module.exit_json(ansible_facts=result)


# Generated at 2022-06-13 05:24:54.171800
# Unit test for function main
def test_main():
    data = dict(
        database='passwd',
        key='root',
        service=None,
        split=':',
        fail_key=True,
    )

    module = AnsibleModule(argument_spec={})
    module.params = data

    getent_bin = module.get_bin_path('getent', True)
    rc, out, err = module.run_command([getent_bin, data['database'], data['key']])

    dbtree = 'getent_%s' % data['database']
    results = {dbtree: {}}
    seen = {}
    for line in out.splitlines():
        record = line.split(data['split'])


# Generated at 2022-06-13 05:25:01.968829
# Unit test for function main
def test_main():
    import pytest
    from ansible.module_utils import basic
    from ansible.module_utils.basic import AnsibleModule
    import ansible.module_utils.facts
    import ansible.module_utils.urls
    import os

    def getent_bin(module):
        path = module.get_bin_path('getent', True)
        return path

    module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=False),
            split=dict(type='str'),
            fail_key=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )
    module.get_bin_path = getent_bin
    return main()

# Generated at 2022-06-13 05:25:42.258304
# Unit test for function main
def test_main():
    getent_bin = module.get_bin_path('getent', True)
    if getent_bin == None:
        msg = "getent executable not found"
        module.fail_json(msg=msg)
    # Example only: test for 'passwd' database
    database = 'passwd'
    # Example only: test for 'root' key
    key = 'root'
    cmd = [getent_bin, database, key]
    rc, out, err = module.run_command(cmd)
    if rc == 0 and out is not None:
        # Test pass
        print(out)
    elif rc == 1:
        msg = "Missing arguments, or database unknown."
        module.fail_json(msg=msg)

# Generated at 2022-06-13 05:25:51.391435
# Unit test for function main
def test_main():
    import platform
    import json
    import copy
    import os
    import stat
    import tempfile

    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.basic import AnsibleModule


# Generated at 2022-06-13 05:26:03.246554
# Unit test for function main
def test_main():
    import sys
    import os

    # Mock the module import
    def AnsibleModule(argument_spec, **kwargs):
        module = MagicMock()
        module.params = params
        module.fail_json.side_effect = Exception
        return module

    # Mock the method run_command
    def run_command(self, cmd, **kwargs):
        stdout = ''
        stderr = ''
        if cmd == ['/usr/bin/getent', 'passwd']:
            stdout = 'root:password:0:0:root:/root:/bin/bash\ngod:password:0:0:god:/root:/bin/bash\nbin:password:1:1:bin:/bin:/bin/sh'
        elif cmd == ['/usr/bin/getent', 'passwd', 'root']:
            std

# Generated at 2022-06-13 05:26:17.724643
# Unit test for function main
def test_main():
    '''
    Ensure all the parameters are valid, or
    that the getent command returns the correct
    results.

    # TODO: Test the actual getent command output
    '''
    from ansible.module_utils.basic import AnsibleModule
    class MockModule(object):
        def __init__(self):
            self.params = {'database': 'foobar',
                           'key': 'bar',
                           'split': ':',
                           'fail_key': True
                          }
            self.run_command = self.mock_run_command

        def mock_run_command(self, *args, **kwargs):
            return 0, '', ''

    module = MockModule()

    main(module)
    module.params['fail_key'] = False
    main(module)
    module.params

# Generated at 2022-06-13 05:26:26.735383
# Unit test for function main
def test_main():
    # Mock the getent module
    getent_mock = MagicMock()
    getent_mock.params = dict(database='passwd',
                              key='root',
                              split=None)

    getent_mock.get_bin_path.return_value = '/bin/getent'

    class RunCommand:
        def __init__(self, rc, out, err):
            self.rc = rc
            self.out = out
            self.err = err

        def __call__(self, *args):
            return (self.rc, self.out, self.err)

    # Test Success
    run_command_mock = RunCommand(0, 'root:x:0:0:root:/root:/bin/bash\n', '')
    getent_mock.run_command = run_command

# Generated at 2022-06-13 05:26:36.266520
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

    args_dict = module.params
    args_dict['database'] = 'group'
    args_dict['key'] = 'wheel'

    module.run_command = MagicMock(return_value=(0, 'wheel:*:0:root,brian\n', ''))
    main()


# Generated at 2022-06-13 05:26:42.480359
# Unit test for function main
def test_main():
    import sys
    import shlex

    class AnsibleModuleMock(object):
        def __init__(self, argument_spec, supports_check_mode):
            self.argument_spec = argument_spec
            self.supports_check_mode = supports_check_mode
            self.result = None

        def get_bin_path(self, path, required):
            return '__BIN_PATH_PLACEHOLDER__'

        def run_command(self, args, check_rc=True):
            args = [x.replace('__BIN_PATH_PLACEHOLDER__', '/usr/bin/getent') for x in args]
            if args[1] == 'group':
                return 0, 'root:x:0:', ''
            else:
                return 1, '', ''


# Generated at 2022-06-13 05:26:51.112633
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
    rc = main()
    assert rc == 1
    assert module.check_mode is True



# Generated at 2022-06-13 05:27:01.571404
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=False),
            split=dict(type='str'),
            fail_key=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )

    databases = ['passwd', 'shadow', 'group', 'gshadow']

    for database in databases:
        key = None
        split = None
        return_values = {}

        if database == 'passwd':
            key = 'root'
            split = ':'

# Generated at 2022-06-13 05:27:12.315150
# Unit test for function main
def test_main():
  # Test with key
  test_main_1 = {
        'database': 'passwd',
        'key': 'root',
        'split': ':',
        'service': '',
        'fail_key': True
    }
  assert main(test_main_1) == 0

  # Test with no key
  test_main_2 = {
        'database': 'hosts',
        'key': '',
        'split': '',
        'service': '',
        'fail_key': False
    }
  assert main(test_main_2) == 0

  # Test with fail_key
  test_main_3 = {
        'database': 'passwd',
        'key': '',
        'split': ':',
        'service': '',
        'fail_key': True
    }

# Generated at 2022-06-13 05:27:42.787635
# Unit test for function main
def test_main():
    sys.path.append(os.path.dirname(__file__))
    from test_data import data
    __builtins__['__salt__'] = {}
    __builtins__['__opts__'] = {}
    __builtins__['__grains__'] = {}
    ansible_module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=False),
            service=dict(type='str'),
            split=dict(type='str'),
            fail_key=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )
    ansible_module.get_bin_path = data['get_bin_path']
    ansible_module.run_

# Generated at 2022-06-13 05:27:43.356425
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:27:44.924548
# Unit test for function main
def test_main():
    os.system("pytest --capture=sys --verbose")

# Generated at 2022-06-13 05:27:54.992840
# Unit test for function main
def test_main():
    import os
    os.system("mv action_plugins/getent.py action_plugins/getent.orig")
    os.system("ln -s ../../action_plugins/action_plugins/getent.py action_plugins")
    os.system("ansible-playbook -i inventory.txt test.yml --connection=local")
    os.system("rm action_plugins/getent.py")
    os.system("mv action_plugins/getent.orig action_plugins/getent.py")

# Generated at 2022-06-13 05:27:55.714009
# Unit test for function main
def test_main():
    assert 2 == 2

# Generated at 2022-06-13 05:27:56.367226
# Unit test for function main
def test_main():
    assert main() is None

# Generated at 2022-06-13 05:28:06.667691
# Unit test for function main
def test_main():
    # import modules needed by our function
    import json
    import sys

    # import module we want to test
    import module_utils.getent_module as utils

    # the tested function
    main()

    # define needed variables
    module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str'),
            split=dict(type='str'),
            fail_key=dict(type='bool', default=True),
        )
    )

    # prepare arguments
    args = dict(
        database='passwd',
        key='root',
        split=None,
        fail_key=True,
    )

    # run the code

# Generated at 2022-06-13 05:28:17.503071
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

   

# Generated at 2022-06-13 05:28:23.779414
# Unit test for function main
def test_main():
    class MockModule(object):
        def run_command(self, command, **kwargs):
            if command == ['getent', 'passwd', 'root']:
                return 0, "root:x:0:0:root:/root:/bin/bash", ""
            elif command == ['getent', 'passwd']:
                return 0, "root:x:0:0:root:/root:/bin/bash", ""
            else:
                return 1, "", ""
    module = MockModule()
    results = main()
    assert type(results['ansible_facts']['getent_passwd']) is dict

# Generated at 2022-06-13 05:28:29.014790
# Unit test for function main
def test_main():
    from ansible.module_utils.ansible_release import __version__ as ansible_version

    # Ansible 2.10 does not keep duplicate entires
    if ansible_version < '2.11':
        if True:
            pass
    else:
        if False:
            pass


# from ansible.module_utils.facts import *

# Load config and populate ansible facts

# Generated at 2022-06-13 05:29:51.358003
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=False),
            service=dict(type='str'),
            fail_key=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )

    database = module.params['database']
    key = module.params.get('key')
    service = module.params.get('service')
    fail_key = module.params.get('fail_key')

    getent_bin = module.get_bin_path('getent', True)

    if key is not None:
        cmd = [getent_bin, database, key]
    else:
        cmd = [getent_bin, database]


# Generated at 2022-06-13 05:29:58.126073
# Unit test for function main
def test_main():
    # Placeholder for construction of unit test case
    # test_module = AnsibleModule(
    #     argument_spec=dict(
    #         database=dict(type='str', required=True),
    #         key=dict(type='str', no_log=False),
    #         service=dict(type='str'),
    #         split=dict(type='str')
    #     ),
    #     supports_check_mode=True,
    # )

    # test_module.params['database'] = ''
    # test_module.params['key'] = ''
    # test_module.params['service'] = ''
    # test_module.params['split'] = ''

    print("Hello World!")

# Generated at 2022-06-13 05:30:03.346524
# Unit test for function main
def test_main():
    import os
    import json
    import pytest
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common.collections import is_sequence
    from ansible.module_utils.six import PY3
    from ansible.module_utils._text import to_text



# Generated at 2022-06-13 05:30:10.623547
# Unit test for function main
def test_main():
  module = AnsibleModule(
    argument_spec=dict(
      database=dict(type='str'),
      key=dict(type='str')
    ),
    supports_check_mode=True,
  )
  rc, out, err = module.run_command(['getent', 'passwd'])
  results = {'getent_passwd':{}}
  lines = out.splitlines()
  for line in lines:
    record = line.split(':')
    results['getent_passwd'][record[0]] = record[1:]

  assert rc == 0

# Generated at 2022-06-13 05:30:21.711943
# Unit test for function main
def test_main():
    import json

    module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=False),
            split=dict(type='str'),
            fail_key=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )

    colon = ['passwd', 'shadow', 'group', 'gshadow']

    database = 'hosts'
    key = module.params.get('key')
    split = module.params.get('split')
    fail_key = module.params.get('fail_key')

    getent_bin = module.get_bin_path('getent', True)

    if key is not None:
        cmd = [getent_bin, database, key]

# Generated at 2022-06-13 05:30:28.727894
# Unit test for function main
def test_main():
    test = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=False),
            service=dict(type='str'),
            split=dict(type='str'),
            fail_key=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )
    test_main.getent_bin = test.get_bin_path('getent', True)
    test_main.split = ':'



# Generated at 2022-06-13 05:30:31.561731
# Unit test for function main
def test_main():
    module = AnsibleModule({
        'database': 'services',
        'key': 'ssh',
        'split': ':',
    })
    assert getent_bin is not None

# Generated at 2022-06-13 05:30:38.675730
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.basic import AnsibleModule

    # class TestModule(unittest.TestCase):

    module = AnsibleModule(argument_spec=dict(
        database=dict(type='str', required=True),
        key=dict(type='str', no_log=False),
        service=dict(type='str'),
        split=dict(type='str'),
        fail_key=dict(type='bool', default=True),
    ))

    main()
    # if __name__ == '__main__':
    #     unittest.main()

# Generated at 2022-06-13 05:30:53.848668
# Unit test for function main
def test_main():
    import json

    module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=False),
            split=dict(type='str'),
            fail_key=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )

    colon = ['passwd', 'shadow', 'group', 'gshadow']

    database = module.params['database']
    key = module.params.get('key')
    split = module.params.get('split')
    fail_key = module.params.get('fail_key')

    getent_bin = module.get_bin_path('getent', True)


# Generated at 2022-06-13 05:31:04.138791
# Unit test for function main
def test_main():
    getent_bin = 'getent'
    database = 'passwd'
    key = 'root'
    rc = 0
    out = 'root:x:0:0:root:/root:/bin/bash'
    err = ''
    module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=False),
        ),
        supports_check_mode=True,
    )
    getent_bin = module.get_bin_path(getent_bin, True)

    cmd = [getent_bin, database, key]