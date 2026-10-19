

# Generated at 2022-06-13 04:52:17.961762
# Unit test for function check_command
def test_check_command():
    arglist = ['chown', 'chmod', 'chgrp', 'ln', 'mkdir', 'rmdir', 'rm', 'touch', \
               'curl', 'wget', 'svn', 'service', 'mount', 'rpm', \
               'yum', 'apt-get', 'tar', 'unzip', 'sed', 'dnf', 'zypper']
    for cmd in arglist:
        module = AnsibleModule(argument_spec={'command': {'type': 'str', 'required': True}})
        check_command(module, cmd)
    module = AnsibleModule(argument_spec={'command': {'type': 'str', 'required': True}})
    check_command(module, ['chown', 'test'])

# Generated at 2022-06-13 04:52:19.917520
# Unit test for function main
def test_main():
    assert main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:52:30.211336
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils import common
    from ansible.module_utils._text import to_bytes

    original_basic_run_command = basic.run_command

    def my_run_command(args, executable=None, use_unsafe_shell=False, data=None, binary_data=False):
        if args[0] == 'fail':
            return 1, '', 'FAILED'
        else:
            return 0, 'hello there', ''

    my_module = common.AnsibleModule(argument_spec=dict())
    my_module.run_command = my_run_command


# Generated at 2022-06-13 04:52:42.533646
# Unit test for function check_command
def test_check_command():
    import ansible.module_utils.basic
    import sys
    results = []
    def warn_mock(msg):
        results.append(msg)
    module = ansible.module_utils.basic.AnsibleModule(argument_spec={})
    module.warn = warn_mock
    check_command(module, "rm fakefile")
    assert results[0].startswith("Consider using the file module with ")
    results = []
    check_command(module, "ln -sf fakefile /etc/")
    assert results[0].startswith("Consider using the file module with ")
    results = []
    check_command(module, "chmod 755 fakefile")
    assert results[0].startswith("Consider using the file module with ")
    results = []

# Generated at 2022-06-13 04:52:51.234019
# Unit test for function main
def test_main():
    args = {}
    args['removes'] = ' '
    args['creates'] = ' '
    args['_raw_params'] = ''
    args['argv'] = [' ']
    args['warn'] = False
    args['_uses_shell'] = False

    test_module = AnsibleModule(argument_spec=module.params, supports_check_mode=True)
    main(module=test_module, **args)

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:53:04.185248
# Unit test for function check_command
def test_check_command():
    # This test is run against a specific version of Ansible, so if the
    # version is changed, the test will need to be updated
    assert AnsibleModule.ANSIBLE_VERSION == '2.9.6'

    # Create a fake module used to test the function
    class TestModule(object):
        def __init__(self):
            self.warn_args = []
        def warn(self, msg):
            self.warn_args.append(msg)

    module = TestModule()
    commandline = ['chown', 'fake', '/fake/file']
    check_command(module, commandline)
    assert len(module.warn_args) == 1

# Generated at 2022-06-13 04:53:15.619802
# Unit test for function check_command
def test_check_command():
    module = AnsibleModule(argument_spec={})
    module.warn = mock.MagicMock()
    module.fail_json = mock.MagicMock()

    check_command(module, 'chmod')
    assert module.warn.called and module.warn.call_count == 1
    assert module.warn.call_args == mock.call("Consider using the file module with mode rather than running 'chmod'.  If you need to use 'chmod' because the file module is insufficient you can add 'warn: false' to this command task or set 'command_warnings=False' in the defaults section of ansible.cfg to get rid of this message.")

    check_command(module, 'chown')
    assert module.warn.called and module.warn.call_count == 2

# Generated at 2022-06-13 04:53:20.766988
# Unit test for function main
def test_main():
    return '''
- name: Execute a command returns a non-zero return code
  ansible.builtin.command: id -grp non-existent-group
  register: result

- name: Fail when execution returns an error
  assert:
    that: result.rc != 0

- name: Fail when execution output contains specific text
  assert:
    that: result.stderr.find('non-existent-group') != -1

- name: Fail when execution output does not contain specific text
  assert:
    that: result.stderr.find('non-existent-group') == -1
'''
if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:53:33.025852
# Unit test for function main
def test_main():
    f = open("test.py", "w")
    f.write("")
    f.close()
    command = "/usr/bin/python test.py"

# Generated at 2022-06-13 04:53:39.859752
# Unit test for function check_command
def test_check_command():
    mod = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    check_command(mod, ['foo'])
    check_command(mod, 'foo')
    check_command(mod, ['curl', 'http://example.com'])
    check_command(mod, 'curl http://example.com')
    check_command(mod, 'chown 123:456 /path/to/file')
    check_command(mod, 'chmod 0644 /path/to/file')



# Generated at 2022-06-13 04:53:52.215181
# Unit test for function check_command
def test_check_command():
    module = AnsibleModule({}, {})
    module.warn = MagicMock()
    with patch.object(builtins, 'open', mock_open()) as mock_file, patch('os.path.isfile') as mock_isfile:
        mock_isfile.return_value = True
        command = "/usr/bin/foo"
        check_command(module, command)

# ===========================================
# Main control flow


# Generated at 2022-06-13 04:54:02.941413
# Unit test for function main

# Generated at 2022-06-13 04:54:14.982104
# Unit test for function check_command
def test_check_command():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.common.text.converters import to_text
    from io import BytesIO
    from ansible.playbook.play_context import PlayContext
    from ansible.module_utils.helpers import ModuleDeprecationWarning
    import ansible.module_utils.basic
    from ansible.module_utils.connection import Connection
    from ansible.module_utils.remote_management import exec_command
    import ansible.module_utils.common.warnings
    import ansible.module_utils.common.text.converters
    import ansible.module_utils.six.moves.urllib.parse


# Generated at 2022-06-13 04:54:21.019248
# Unit test for function check_command
def test_check_command():
    from ansible.module_utils.basic import AnsibleModule
    m = AnsibleModule(argument_spec=dict())
    # test the things that generate a warning
    check_command(m, 'chown')
    check_command(m, 'chmod')
    check_command(m, 'chgrp')
    check_command(m, 'ln')
    check_command(m, 'mkdir')
    check_command(m, 'rmdir')
    check_command(m, 'rm')
    check_command(m, 'touch')
    check_command(m, 'curl')
    check_command(m, 'wget')
    check_command(m, 'svn')
    check_command(m, 'service')
    check_command(m, 'mount')

# Generated at 2022-06-13 04:54:30.383977
# Unit test for function main
def test_main():
    m = AnsibleModule(argument_spec={
        '_raw_params': {},
        'warn': {'type': 'bool', 'default': False}
    })
    r = {'changed': False, 'stdout': '', 'stderr': ''}
    r['cmd'] = '/bin/false'
    r['rc'] = 1
    r['msg'] = 'non-zero return code'
    try:
        main(m)
    except SystemExit:
        pass
    assert r == m.exit_json.call_args[0][0]


# Generated at 2022-06-13 04:54:39.561425
# Unit test for function main

# Generated at 2022-06-13 04:54:47.679308
# Unit test for function main

# Generated at 2022-06-13 04:55:00.975548
# Unit test for function check_command
def test_check_command():
    from ansible.module_utils import basic
    module = basic.AnsibleModule(
        argument_spec=dict()
    )

# Generated at 2022-06-13 04:55:10.755990
# Unit test for function check_command
def test_check_command():
    module = AnsibleModule({}, check_mode=True)
    check_command(module, '/bin/chown')
    assert module.deprecations == [
        "Consider using the file module with chown rather than running 'chown'.  If you need to use 'chown' because the file module is insufficient you can add 'warn: false' to this command task or set 'command_warnings=False' in the defaults section of ansible.cfg to get rid of this message.",
        "Consider using 'become', 'become_method', and 'become_user' rather than running chown"
    ]
    check_command(module, '/bin/chmod')

# Generated at 2022-06-13 04:55:23.505944
# Unit test for function main
def test_main():
    import pytest
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils._text import to_text
    from ansible.module_utils.common.collections import is_iterable
    from ansible.module_utils.common.collections import to_native
    from ansible.module_utils.common.collections import to_text

    # the command module is the one ansible module that does not take key=value args
    # hence don't copy this one if you are looking to build others!
    # NOTE: ensure splitter.py is kept in sync for exceptions

# Generated at 2022-06-13 04:55:45.432270
# Unit test for function main

# Generated at 2022-06-13 04:55:53.793549
# Unit test for function check_command
def test_check_command():
    module = AnsibleModule(argument_spec={})
    module.warn = lambda x: x
    check_command(module, "/bin/chown foo")
    assert module.warnings == ["Consider using the file module with owner rather than running 'chown'.  "
                               "If you need to use 'chown' because the file module is insufficient you can add "
                               "'warn: false' to this command task or set 'command_warnings=False' in "
                               "the defaults section of ansible.cfg to get rid of this message."]



# Generated at 2022-06-13 04:56:05.621189
# Unit test for function check_command
def test_check_command():
    module = AnsibleModule(argument_spec = dict())
    check_command(module, ['chown', 'owner'])
    check_command(module, ['chmod', 'mode'])
    check_command(module, ['chgrp', 'group'])
    check_command(module, ['ln', 'state=link'])
    check_command(module, ['mkdir', 'state=directory'])
    check_command(module, ['rmdir', 'state=absent'])
    check_command(module, ['rm', 'state=absent'])
    check_command(module, ['touch', 'state=touch'])

    check_command(module, ['curl', 'get_url'])
    check_command(module, ['wget', 'get_url'])

# Generated at 2022-06-13 04:56:08.228677
# Unit test for function main
def test_main():
  # function main is of type <class 'function'>
  assert callable(main)
  assert isinstance(main, function)


# Generated at 2022-06-13 04:56:14.119803
# Unit test for function check_command
def test_check_command():
    m = AnsibleModule(
        argument_spec={},
    )
    check_command(m, '/usr/bin/chown root /etc/passwd')
    assert m._result['warnings'] == [
        "Consider using the file module with owner rather than running 'chown'.  If you need to use 'chown' because the file module is insufficient you can add 'warn: false' to this command task or set 'command_warnings=False' in the defaults section of ansible.cfg to get rid of this message."
    ]



# Generated at 2022-06-13 04:56:16.121039
# Unit test for function check_command
def test_check_command():
    pass  # FIXME



# Generated at 2022-06-13 04:56:27.143740
# Unit test for function check_command
def test_check_command():
    from ansible.module_utils.common.warnings import AnsibleFilterDeprecationWarning
    try:
        from unittest.mock import patch
    except:
        from mock import patch
    with patch('ansible.module_utils.basic.AnsibleModule') as mock_module:
        # Parameter 'warn' with value 'no' disables warning
        command = 'ls'
        args = dict(warn=False)
        mock_module.params = args
        mock_module.get_bin_path.return_value = command
        mock_module.check_mode = False
        command_module = AnsibleModule(argument_spec={})
        check_command(command_module, command)
        assert mock_module.warn.called == False
        # Parameter 'warn' with value 'yes' enables warning

# Generated at 2022-06-13 04:56:36.630009
# Unit test for function main
def test_main():
    args = dict(
        _raw_params='uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu'
        )


# Generated at 2022-06-13 04:56:44.204942
# Unit test for function main
def test_main():
    source = {
        "check_mode": True,
        "params": {
            "argv": None,
            "chdir": None,
            "creates": None,
            "executable": None,
            "removes": None,
            "stdin": None,
            "strip_empty_ends": True,
            "warn": False,
        }
    }
    module = AnsibleModule(**source)
    r = main()
    assert r["msg"] == "Command would have run if not in check mode", "Failed to run command"


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:56:56.080079
# Unit test for function main
def test_main():
    args = dict(
        _raw_params='test.sh',
        _uses_shell=True,
        argv=None,
        chdir=None,
        executable='/bin/bash',
        creates=None,
        removes=None,
        warn=False,
        stdin=None,
        stdin_add_newline=True,
        strip_empty_ends=True
    )
    r = dict(
        changed=False,
        stdout='',
        stderr='',
        rc=None,
        cmd=None,
        start=None,
        end=None,
        delta=None,
        msg=''
    )

# Generated at 2022-06-13 04:57:31.870992
# Unit test for function main
def test_main():
  args = {
    "warn": False,
    "_raw_params": "ls -l /home/ansible",
    "_uses_shell": False,
  }

# Generated at 2022-06-13 04:57:44.224176
# Unit test for function main

# Generated at 2022-06-13 04:57:54.408884
# Unit test for function main

# Generated at 2022-06-13 04:57:56.279895
# Unit test for function main
def test_main():
  pass

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:58:07.951493
# Unit test for function main
def test_main():
    module_arguments = dict(
        _raw_params='ls -l',
        _uses_shell=False,
        argv=dict(type='list', elements='str'),
        chdir=dict(type='path'),
        executable=dict(),
        creates=dict(type='path'),
        removes=dict(type='path'),
        warn=dict(type='bool', default=False, removed_in_version='2.14', removed_from_collection='ansible.builtin'),
        stdin=dict(required=False),
        stdin_add_newline=dict(type='bool', default=True),
        strip_empty_ends=dict(type='bool', default=True),
    )
    module_dynamic_args = {}

# Generated at 2022-06-13 04:58:14.857315
# Unit test for function main
def test_main():
    arg_spec = dict(
        _raw_params=dict(),
        _uses_shell=dict(type='bool', default=False),
        argv=dict(type='list', elements='str'),
        chdir=dict(type='path'),
        executable=dict(),
        creates=dict(type='path'),
        removes=dict(type='path'),
        # The default for this really comes from the action plugin
        warn=dict(type='bool', default=False, removed_in_version='2.14', removed_from_collection='ansible.builtin'),
        stdin=dict(required=False),
        stdin_add_newline=dict(type='bool', default=True),
        strip_empty_ends=dict(type='bool', default=True),
    )

# Generated at 2022-06-13 04:58:26.871420
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    import json
    import sys
    import tempfile

    myenv = os.environ.copy()
    myenv['ANSIBLE_MODULE_ARGS'] = json.dumps({
        '_raw_params': '/usr/bin/env',
        '_uses_shell': True,
        'argv': None,
        'chdir': None,
        'warn': False
    })


# Generated at 2022-06-13 04:58:37.954925
# Unit test for function main
def test_main():
  args = dict(
    _raw_params="uptime",
  )
  r = {"changed": False,
       "delta": None,
       "end": None,
       "rc": None,
       "start": None,
       "cmd": None,
       "stderr": "",
       "msg": "",
       "stdout": ""}

# Generated at 2022-06-13 04:58:47.757464
# Unit test for function main
def test_main():
	from ansible.module_utils.basic import AnsibleModule
	from ansible.module_utils._text import to_bytes
	from ansible.module_utils.common.collections import is_iterable
	import sys
	import random
	import string
	import sqlite3 as lite
	import os
	import os.path
	import base64
	import getpass
	import json

	con = ''
	con = lite.connect('ansible_command.db')
	cur = con.cursor()

# Generated at 2022-06-13 04:58:55.675789
# Unit test for function main
def test_main():
    # Mock module mock_module
    mock_module = MagicMock()
    mock_module.params = {
        '_uses_shell': False,
        'argv': [
            'echo',
            'hello',
        ],
        'chdir': None,
        'creates': None,
        'removes': None,
        '_raw_params': '',
        'executable': None,
        'strip_empty_ends': True,
        'warn': False,
        'stdin': None,
        'stdin_add_newline': True,
    }
    mock_module.check_mode = False
    mock_module.run_command.return_value = (0, '', '')
    mock_module.fail_json.side_effect = fail_json

# Generated at 2022-06-13 05:00:00.881860
# Unit test for function check_command
def test_check_command():
    assert check_command(1,1) == None  # How do we test this?


# Generated at 2022-06-13 05:00:13.410626
# Unit test for function main

# Generated at 2022-06-13 05:00:15.124408
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-13 05:00:28.432569
# Unit test for function check_command
def test_check_command():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(
        argument_spec=dict(
            command=dict(type='str'),
        )
    )
    check_command(module, 'sudo echo hi')
    assert module.warnings == ["Consider using 'become', 'become_method', and 'become_user' rather than running sudo"]
    check_command(module, 'svn up')

# Generated at 2022-06-13 05:00:34.090719
# Unit test for function main
def test_main():
    # Capture values returned from main()
    result = {
        'changed': True,
        'end': '2010-03-28T15:56:21.438Z',
        'failed': False,
        'rc': 256,
        'start': '2010-03-28T15:56:21.438Z',
        'stderr': 'ls cannot access foo: No such file or directory',
        'stderr_lines': [
            'ls cannot access foo: No such file or directory',
            'ls: cannot access bar: No such file or directory'
        ],
        'stdout': 'Clustering node rabbit@slave1 with rabbit@master …',
        'stdout_lines': [
            'Clustering node rabbit@slave1 with rabbit@master …'
        ]
    }
    # unittest
    test

# Generated at 2022-06-13 05:00:44.728466
# Unit test for function main
def test_main():
    args = dict(
        _raw_params='mycommand arg1 arg2 arg3 arg4 arg5 arg6 arg7 arg8 arg9',
        _uses_shell=True,
        executable='/usr/bin/python',
        creates='/root/myfile',
        removes='/root/myfile',
        warn=True,
        stdin='Some data for stdin',
        stdin_add_newline=True,
        strip_empty_ends=False,
    )
    os.chdir('/root')
    rc, out, err = main([], args)

    assert rc == 0
    assert out == ''
    assert err == ''

# Generated at 2022-06-13 05:00:46.556500
# Unit test for function main
def test_main():
    res = main()
    return res

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:00:53.999937
# Unit test for function main
def test_main():
    import tempfile
    (osf, fpath) = tempfile.mkstemp()
    os.write(osf, "Hello\n")
    os.close(osf)
    os.chmod(fpath, 0o0644)
    os.chown(fpath, 0, 0)
    assert os.stat(fpath).st_uid == 0
    assert os.stat(fpath).st_gid == 0


# Generated at 2022-06-13 05:01:00.818594
# Unit test for function main
def test_main():
    test_args = [
        "command_module.py"
    ]
    if not PY3:
        test_args.append(u'bob')
    else:
        test_args.append('bob')
    with patch.object(sys, 'argv', test_args):
        with patch.object(ansible.module_utils.basic, 'AnsibleModule') as mock_module:
            # TODO: not actually testing anything else
            main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:01:11.713828
# Unit test for function main
def test_main():
    """
    This is the unit test for the main function.
    """
    print("Running test_main()...")
    import sys
    sys.modules['ansible.module_utils.basic'] = MagicMock()
    sys.modules['ansible.module_utils.basic'].AnsibleModule = MagicMock()
    sys.modules['ansible.module_utils.basic'].AnsibleModule.return_value = MagicMock()
    sys.modules['ansible.module_utils.common.collections'] = MagicMock()
    sys.modules['ansible.module_utils.common.collections'].is_iterable = MagicMock()
    sys.modules['ansible.module_utils.common.collections'].is_iterable.return_value = True
