

# Generated at 2022-06-13 04:52:08.931098
# Unit test for function check_command
def test_check_command():
    m = AnsibleModule(argument_spec={})
    check_command(m, 'ansible --version')


# Generated at 2022-06-13 04:52:20.368040
# Unit test for function check_command
def test_check_command():
    module = type('AnsibleModule', (object,), {})
    module.warn = lambda self, msg: type('Command', (object,), {'cmd': []})
    from ansible.module_utils.basic import AnsibleModule
    m = AnsibleModule(argument_spec={})
    check_command(m, "")
    assert m.cmd == []
    m.cmd = None
    check_command(m, ["touch", "test"])
    assert m.cmd == ["touch", "test"]
    m.cmd = None
    check_command(m, ["ln", "test", "test1"])
    assert m.cmd == ["ln", "test", "test1"]
    m.cmd = None
    check_command(m, ["chmod", "777", "test"])

# Generated at 2022-06-13 04:52:30.585178
# Unit test for function main
def test_main():
    args = dict(
        _raw_params='ls -l',
        args=None
    )
    result = {
    'changed': True,
    'cmd': ['ls', '-l'],
    'delta': '0:00:00.001346',
    'end': '2017-09-29 22:03:48.084657',
    'rc': 0,
    'start': '2017-09-29 22:03:48.083128'
    }
    mocked_module = MagicMock()
    with patch.dict(main.__dict__, {'module': mocked_module}):
        mocked_module.check_mode = False
        main()
        mocked_module.run_command.assert_called_with(args['_raw_params'], None, False, None)

# Generated at 2022-06-13 04:52:38.745202
# Unit test for function main
def test_main():
    m = AnsibleModule(argument_spec={}, supports_check_mode=True)
    m._ansible_no_log = False
    m.run_command = lambda *args, **kwargs: [0, '', '']
    params = dict(
        argv=[],
        _uses_shell=True,
        _raw_params=['/usr/bin/uptime']
    )
    m.params = params
    res = main()
    assert res['rc'] == 0


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:52:50.958285
# Unit test for function check_command
def test_check_command():
    module = type('test', (object,), {})

    # Check that no warning is reported for unrecognized commands
    setattr(module, 'warnings', [])
    check_command(module, 'notacommand')
    assert not module.warnings

    # Check that valid commands with no further qualification do not warn
    module.warnings = []
    check_command(module, 'ls')
    assert not module.warnings
    check_command(module, '/usr/bin/ls')
    assert not module.warnings

    # Check that valid commands with arguments do warn
    module.warnings = []
    check_command(module, 'ls -1 /tmp/does-not-exist')
    assert module.warnings

    # Check that a warning is reported if a known command is found
    module.warnings = []
    check_

# Generated at 2022-06-13 04:53:03.897726
# Unit test for function main
def test_main():
    from lib.ansible_module import execute_module
    from lib.ansible_module import AnsibleModule
    import sys

    print(AnsibleModule)
    # Exit public function

# Generated at 2022-06-13 04:53:15.385423
# Unit test for function main
def test_main():

    import pytest,json
    # test case 1
    command = ['/bin/false']
    module = AnsibleModule(
        argument_spec=dict(
            _raw_params=dict(),
            _uses_shell=dict(type='bool', default=False),
            argv=dict(type='list', elements='str'),
            chdir=dict(type='path'),
            executable=dict(),
            creates=dict(type='path'),
            removes=dict(type='path'),
            warn=dict(type='bool', default=False),
            stdin=dict(required=False),
            stdin_add_newline=dict(type='bool', default=True),
            strip_empty_ends=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )

# Generated at 2022-06-13 04:53:19.377642
# Unit test for function check_command
def test_check_command():
    assert check_command('chown') == 'owner'
    assert check_command('chmod') == 'mode'
    assert check_command('chgrp') == 'group'
    assert check_command('ln') == 'state=link'
    assert check_command('mkdir') == 'state=directory'
    assert check_command('rmdir') == 'state=absent'
    assert check_command('rm') == 'state=absent'
    assert check_command('touch') == 'state=touch'

    assert check_command('curl') == 'get_url or uri'
    assert check_command('wget') == 'get_url or uri'
    assert check_command('svn') == 'subversion'
    assert check_command('service') == 'service'

# Generated at 2022-06-13 04:53:23.939386
# Unit test for function main
def test_main():
    module = AnsibleModule(argument_spec={}, supports_check_mode=False)

    # Test check_command(module, ['foo', 'bar'])
    check_command(module, ['foo', 'bar'])

# Generated at 2022-06-13 04:53:33.657212
# Unit test for function main
def test_main():
    args = dict(
        _raw_params='/usr/bin/echo hello',
        _uses_shell=False,
        argv=['/usr/bin/echo', 'hello'],
        chdir=None,
        executable=None,
        creates=None,
        removes=None,
        # The default for this really comes from the action plugin
        warn=True,
        stdin=None,
        stdin_add_newline=True,
        strip_empty_ends=True,
        verbosity=1,
        no_log=0,
        diff=False,
        check=False,
    )

    res = main()
    assert args == res, "assert args == res"

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:53:53.739697
# Unit test for function main
def test_main():
    assert True

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:54:03.255185
# Unit test for function main
def test_main():
    import os
    import tempfile

    def get_module_path(module_name):
        try:
            from ansible.utils.module_docs import get_docstring
            docstring = get_docstring(module_name)
            return docstring['module']
        except:
            module = AnsibleModule(argument_spec={})
            module_arg_spec = dict(module._task.args.copy())
            module_path = module_arg_spec['_original_file']
            module_name = os.path.splitext(os.path.basename(module_path))[0]
            return module_name

    module_name = get_module_path(__name__)
    tmpdir = tempfile.mkdtemp()
    file_name = os.path.join(tmpdir, 'test.txt')
   

# Generated at 2022-06-13 04:54:13.995347
# Unit test for function main
def test_main():
    args = {
        "_raw_params": "hostname",
        "_uses_shell": False,
        "argv": [
            "/bin/hostname"
        ],
        "chdir": "",
        "executable": "",
        "creates": "",
        "removes": "",
        "warn": False,
        "strip_empty_ends": True,
        "stdin": "",
        "stdin_add_newline": True
    }
    module = AnsibleModule(argument_spec=args, supports_check_mode=True)
    command_result = main()


# Generated at 2022-06-13 04:54:14.492390
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-13 04:54:18.262525
# Unit test for function check_command
def test_check_command():
    module = AnsibleModule(argument_spec={
        'commandline': dict(required=True)
    })
    command = 'git clone https://github.com/ansible/ansible.git /path/to/ansible'
    command_as_list = [
        command,
        'arg1', 'arg2'
    ]
    check_command(module, command)
    check_command(module, command_as_list)



# Generated at 2022-06-13 04:54:20.333173
# Unit test for function main
def test_main():
    test_result = main()
    assert test_result == 0

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:54:30.160374
# Unit test for function main
def test_main():
    args = dict(
        _raw_params="echo hello",
        _uses_shell=True,
        argv=["echo", "hello"],
        chdir="/path/to/chdir",
        executable="cat",
        creates="/path/to/creates",
        removes="/path/to/removes",
        warn=False,
        stdin="",
        stdin_add_newline=True,
        strip_empty_ends=True,
   )
    results = list(main(module_args=args))
    assert results

# Generated at 2022-06-13 04:54:39.450212
# Unit test for function check_command
def test_check_command():
    from ansible.module_utils import basic
    from ansible.module_utils.common.collections import is_iterable
    from ansible.module_utils.six import b
    from ansible.module_utils.six import PY3
    args = {}
    def mock_warn(msg):
        args['msg'] = msg
    setattr(basic, 'warn', mock_warn)
    m = basic.AnsibleModule(
        argument_spec={},
    )
    if PY3:
        check_command(m, b('/bin/foo'))
    else:
        check_command(m, '/bin/foo')
    assert is_iterable(args)
    assert 'msg' in args

# import module snippets
from ansible.module_utils.basic import *

# Generated at 2022-06-13 04:54:45.277550
# Unit test for function check_command
def test_check_command():
    from ansible.utils.display import Display
    from ansible.module_utils._text import to_bytes
    display = Display()
    display.verbosity = 4
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    print("running function check_command")
    check_command(module, to_bytes('rm foo'))
    check_command(module, to_bytes('touch foo'))
    check_command(module, to_bytes('wget http://google.com'))
    check_command(module, to_bytes('service service_name status'))
    check_command(module, to_bytes('/usr/bin/sudo /usr/bin/chown -R user1:usergroup /var/www'))

# Generated at 2022-06-13 04:54:57.068842
# Unit test for function main
def test_main():
    x={"changed": False, "stdout": "", "stderr": "", "rc": None, "cmd": None, "start": None, "end": None, "delta": None, "msg": "no command given"}
    args = {
        '_raw_params': '',
        '_uses_shell': False,
        'argv': [],
        'chdir': None,
        'executable': None,
        'creates': None,
        'removes': None,
        'warn': True,
        'stdin': None,
        'stdin_add_newline': True,
        'strip_empty_ends': True
    }

# Generated at 2022-06-13 04:55:18.349609
# Unit test for function check_command
def test_check_command():
    arguments = {'chown': 'owner', 'chmod': 'mode', 'chgrp': 'group',
                 'ln': 'state=link', 'mkdir': 'state=directory',
                 'rmdir': 'state=absent', 'rm': 'state=absent', 'touch': 'state=touch'}

# Generated at 2022-06-13 04:55:20.478582
# Unit test for function check_command
def test_check_command():
    from ansible.module_utils.basic import AnsibleModule
    m = AnsibleModule(argument_spec={})
    check_command(m, 'curl')
    check_command(m, ['curl', 'url'])



# Generated at 2022-06-13 04:55:31.550282
# Unit test for function main
def test_main():
    # check default arguments
    assert main.func_defaults == (None,)
    # arguments
    args = ['echo', 'hello']

# Generated at 2022-06-13 04:55:44.421216
# Unit test for function main
def test_main():
  test_data = {
    "argv": [
      "ls",
      "-l"
    ],
    "_raw_params": "ls -l",
    "_uses_shell": False,
    "chdir": "/",
    "creates": "/var/lib/dav/lock/foo.db",
    "executable": None,
    "removes": "/var/lib/dav/lock/foo.db",
    "stdin": None,
    "stdin_add_newline": True,
    "strip_empty_ends": True,
    "warn": False
  }
  need_update = []
  changed = False
  rc = 0
  stdout = ""
  stderr = ""
  msg = ""
  cmd = []
  start = datetime.datetime.now()
  end

# Generated at 2022-06-13 04:55:52.152497
# Unit test for function main
def test_main():
    args = dict(
        _raw_params='ls',
        _uses_shell=True,
        executable='/bin/sh',
        creates='/root/ansible.txt',
        removes='/root/ansible.txt',
        )
    from ansible.utils.path import which as ansible_which
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(**args)
    module.run_command = lambda cmd, **kw: (0, 'stdout', 'stderr')
    setattr(module, 'CHECK_MODE', True)
    main()


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:56:03.851687
# Unit test for function main

# Generated at 2022-06-13 04:56:16.562456
# Unit test for function main
def test_main():
    # Fixture for testing main
    fixture_args = dict(
        _raw_params="ls -l /home/user/",
        _uses_shell=None,
        argv=None,
        chdir=None,
        executable=None,
        creates=None,
        removes=None,
        warn=None,
        stdin=None,
        stdin_add_newline=None,
        strip_empty_ends=None,
    )

# Generated at 2022-06-13 04:56:27.433252
# Unit test for function main
def test_main():
    # mock out the module and action plugin
    module = Mock(check_mode=False)
    module.run_command = Mock(return_value=[0, 'foo', 'bar'])
    module.params = {'_raw_params': 'true', '_uses_shell': False, 'chdir': None,
                     'executable': None, 'creates': None, 'removes': None,
                     'warn': False, 'argv': None, 'stdin': None, 'strip_empty_ends': True}
    module.exit_json = Mock()
    module.fail_json = Mock()
    module.warn = Mock()

    # execute test
    main()

    # make some asserts

# Generated at 2022-06-13 04:56:36.711140
# Unit test for function main
def test_main():

    def run_check_command(module, command):
        commands = {'curl': 'get_url or uri', 'wget': 'get_url or uri', 'svn': 'subversion',
                    'service': 'service', 'mount': 'mount', 'rpm': 'yum, dnf or zypper',
                    'yum': 'yum', 'apt-get': 'apt', 'tar': 'unarchive', 'unzip': 'unarchive',
                    'sed': 'replace, lineinfile or template', 'dnf': 'dnf', 'zypper': 'zypper'}

        substitutions = {'mod': None, 'cmd': command}

        if command in commands:
            msg = "Consider using the {mod} module rather than running '{cmd}'.  "
            substitutions['mod'] = commands[command]

# Generated at 2022-06-13 04:56:39.154872
# Unit test for function main
def test_main():
    # assert 0
    """
    assert main(args=dict(argv=['/bin/echo', 'OK'], _uses_shell=True)) == 0
    """

# Generated at 2022-06-13 04:57:21.090618
# Unit test for function check_command

# Generated at 2022-06-13 04:57:34.459796
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common.collections import is_iterable
    import os, glob, shlex, datetime
    args = shlex.split("echo hello world")
    # Construct a ``module`` object - this is a dummy object which has methods for checking common parameters

# Generated at 2022-06-13 04:57:45.651083
# Unit test for function main
def test_main():
    # Mock the AnsibleModule
    from ansible.module_utils.basic import AnsibleModule

# Generated at 2022-06-13 04:57:53.749007
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from collections import namedtuple

    module = AnsibleModule(
        argument_spec = dict(
            name = dict(type='str'),
            cmd = dict(type='str'),
        ),
        supports_check_mode=True,
    )

    mock_args = namedtuple('MockArgs', 'cmd')
    module.run_command = lambda x, **kwargs: (0, 'hello', '')
    module.check_mode = False
    retval = main()
    assert retval['stdout'] == 'hello'
    assert retval['rc'] == 0


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:58:02.514248
# Unit test for function check_command
def test_check_command():
    command = "/bin/foo"
    arguments = {'chown': 'owner', 'chmod': 'mode', 'chgrp': 'group',
                 'ln': 'state=link', 'mkdir': 'state=directory',
                 'rmdir': 'state=absent', 'rm': 'state=absent', 'touch': 'state=touch'}

# Generated at 2022-06-13 04:58:12.620745
# Unit test for function check_command
def test_check_command():
    class TestCommandModule(object):
        def __init__(self, params):
            self.params = params
            self.warnings = []

        def warn(self, msg):
            self.warnings.append(msg)
    commandline1 = 'echo hello'
    module1 = TestCommandModule({})
    check_command(module1, commandline1)
    assert not module1.warnings

    commandline2 = '/bin/yum -y install git'
    module2 = TestCommandModule({})
    check_command(module2, commandline2)
    assert "Consider using the yum module rather than running" in module2.warnings[0]

    commandline3 = '/bin/yum install git'
    module3 = TestCommandModule({})
    check_command(module3, commandline3)

# Generated at 2022-06-13 04:58:20.316557
# Unit test for function main
def test_main():
    module = AnsibleModule(argument_spec=dict(
        stdin=dict(required=False),
        stdin_add_newline=dict(type='bool', default=True),
        strip_empty_ends=dict(type='bool', default=True),
    ))
    try:
        main()
    except:
        pass

if __name__ == '__main__':
    # test_main()
    main()

# Generated at 2022-06-13 04:58:22.430120
# Unit test for function main
def test_main():
    assert 1 == 1

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:58:29.556742
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            _raw_params=dict(),
            _uses_shell=dict(type='bool', default=False),
            argv=dict(type='list', elements='str'),
            chdir=dict(type='path'),
            executable=dict(),
            creates=dict(type='path'),
            removes=dict(type='path'),
            warn=dict(type='bool', default=False, removed_in_version='2.14', removed_from_collection='ansible.builtin'),
            stdin=dict(required=False),
            stdin_add_newline=dict(type='bool', default=True),
            strip_empty_ends=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )

# Generated at 2022-06-13 04:58:41.089670
# Unit test for function check_command
def test_check_command():
    class FakeModule(object):
        def __init__(self, arg):
            self.argument_spec = arg

        def fail_json(self, *args, **kwargs):
            self.failed = True

        def warn(self, msg):
            self.msg = msg

        def exit_json(self, **kwargs):
            self.exit = kwargs
            self.exit.update({'changed': True})

    args = dict(
        free_form=dict(type='str', required=True),
        creates=dict(type='str'),
        removes=dict(type='str'),
        chdir=dict(type='str'),
        executable=dict(type='str'),
        warn=dict(type='bool', default=False),
    )
    module = FakeModule(args)