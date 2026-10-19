

# Generated at 2022-06-13 04:52:12.356768
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    import mock

    def run_command(args, executable, use_unsafe_shell, stdin_add_newline=True, binary_data=False):
        stdout = 'hello'
        stderr = 'world'
        rc = 0
        return rc, stdout, stderr

    m = mock.MagicMock()
    m.run_command.side_effect = run_command
    m.params = dict()
    m.check_mode = False
    m.params['strip_empty_ends'] = True
    m.params['argv'] = ['echo', 'hello']
    m.params['chdir'] = './'
    m.params['executable'] = None

# Generated at 2022-06-13 04:52:24.407352
# Unit test for function main
def test_main():
    from ansible.module_utils.ansible_release import __version__
    from ansible.module_utils.basic import AnsibleModule

    # Prepare argument spec
    argument_spec = dict()
    argument_spec['_raw_params'] = dict(type='str')
    argument_spec['_uses_shell'] = dict(type='bool', default='False')
    argument_spec['argv'] = dict(type='list', elements='str')
    argument_spec['chdir'] = dict(type='path')
    argument_spec['executable'] = dict()
    argument_spec['creates'] = dict(type='path')
    argument_spec['removes'] = dict(type='path')

# Generated at 2022-06-13 04:52:33.148825
# Unit test for function main
def test_main():
    args = dict(
        _raw_params = '/usr/bin/env',
        argv = ['/usr/bin/env'],
        chdir = '',
        executable = '',
        creates = '',
        removes = '',
        warn = False,
        stdin = '',
        stdin_add_newline = True,
        strip_empty_ends = True,
        )

# Generated at 2022-06-13 04:52:41.414268
# Unit test for function main

# Generated at 2022-06-13 04:52:44.084124
# Unit test for function check_command
def test_check_command():
    args = dict(command='/usr/bin/make_database.sh db_user db_name', creates='/path/to/database')
    module = AnsibleModule(argument_spec=args)
    check_command(module, args['command'])


# Generated at 2022-06-13 04:52:51.844768
# Unit test for function main

# Generated at 2022-06-13 04:53:02.566278
# Unit test for function main
def test_main():
    args = dict(
        _uses_shell=False,
        executable=None,
        _raw_params=None,
        argv=['echo', 'hello'],
        chdir='/tmp',
        creates='/path/to/database',
        warn=False,
        stdin=None,
        stdin_add_newline=True,
        strip_empty_ends=True,
    )
    r = dict(
        changed=False,
        failed=True,
        _ansible_verbose_always=True,
        _ansible_no_log=False
    )
    module = AnsibleModule(**args)
    main()

# Generated at 2022-06-13 04:53:10.761199
# Unit test for function main

# Generated at 2022-06-13 04:53:14.845875
# Unit test for function check_command
def test_check_command():
    import ansible.module_utils.basic
    import ansible.module_utils.common.collections

    args = dict(
        check_mode=False,
        diff_mode=False,
        no_log=False,
        _ansible_check_mode=False,
        _ansible_diff=False,
        _ansible_module_name='command'
    )

    m = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True,
        bypass_checks=False,
        no_log=False
    )

    setattr(m, '_shared_loader_obj', ansible.module_utils.basic._AnsibleModuleLoader())
    setattr(m, '_shared_loader_obj._aliases', dict())
    setattr(m, 'check_mode', False)

# Generated at 2022-06-13 04:53:27.142582
# Unit test for function main

# Generated at 2022-06-13 04:53:50.184400
# Unit test for function main
def test_main():
    args = dict(
        _raw_params='whoami',
        _uses_shell='false',
        executable='None',
        creates='None',
        removes='None',
        warn='True',
        stdin='None',
        stdin_add_newline='True',
        strip_empty_ends='True'
    )

    r = dict(
        changed='False',
        stdout='Bobby',
        stderr='',
        rc='0',
        cmd='whoami',
        start='None',
        end='None',
        delta='None',
        msg=''
    )


# Generated at 2022-06-13 04:54:02.888579
# Unit test for function main
def test_main():
    cwd = os.path.dirname(os.path.realpath(__file__)) + "/data/"
    test_cmd = [cwd + "test.sh", "one", "two", "three"]
    test_exec = "bash"
    test_creates = cwd + "one"
    test_removes = cwd + "/two"

    #dictionary of results - returned

# Generated at 2022-06-13 04:54:11.969121
# Unit test for function main
def test_main():
    import sys
    import StringIO
    import tempfile
    import os
    import subprocess
    import textwrap


# Generated at 2022-06-13 04:54:18.727292
# Unit test for function main

# Generated at 2022-06-13 04:54:26.109174
# Unit test for function check_command

# Generated at 2022-06-13 04:54:36.850851
# Unit test for function main

# Generated at 2022-06-13 04:54:38.407367
# Unit test for function check_command
def test_check_command():
    module = AnsibleModule(argument_spec={})
    check_command(module, ['touch', 'file'])
    check_command(module, ['sed', '-e', 's/a/b/'])


# Generated at 2022-06-13 04:54:46.876675
# Unit test for function main
def test_main():
    with pytest.raises(AnsibleExitJson) as result:
        main()
    assert result.value.args[0]['changed']
    assert result.value.args[0]['msg']
    assert result.value.args[0]['rc']
    assert result.value.args[0]['cmd']
    assert result.value.args[0]['start']
    assert result.value.args[0]['end']
    assert result.value.args[0]['delta']
    assert result.value.args[0]['stdout']
    assert result.value.args[0]['stderr']


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:55:00.171922
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
            warn=dict(type='bool', default=False),
            stdin=dict(required=False),
            stdin_add_newline=dict(type='bool', default=True),
            strip_empty_ends=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )
    check_command(module, "echo")
    print(module.params)

# Generated at 2022-06-13 04:55:01.952577
# Unit test for function check_command
def test_check_command():

    module = AnsibleModule(argument_spec={})
    check_command(module, 'wget')
    pass



# Generated at 2022-06-13 04:55:28.368882
# Unit test for function main
def test_main():
    args = dict(
        _raw_params='echo hi',
        _uses_shell=False,
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
    main(None, args)

# import module snippets

# Generated at 2022-06-13 04:55:41.686949
# Unit test for function check_command
def test_check_command():
    from ansible.module_utils.basic import AnsibleModule
    m = AnsibleModule(
    )
    check_command(m, 'sudo apt-get install ansible')
    check_command(m, ['sudo', 'apt-get', 'install', 'ansible'])
    check_command(m, 'chmod +x /etc/ansible')
    check_command(m, 'chown root:root /etc/ansible')
    check_command(m, 'chgrp root /etc/ansible')
    check_command(m, 'ln -s /etc/ansible_old /etc/ansible')
    check_command(m, 'su - ansible_old -c /etc/ansible')
    check_command(m, 'mount /dev/sda1 /mnt')

# Generated at 2022-06-13 04:55:43.945277
# Unit test for function main
def test_main():
    assert main() is None # no exception raised

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:55:56.497013
# Unit test for function main
def test_main():
    """ Unit test for function main function """
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.loader import action_loader, lookup_loader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.utils.vars import load_extra_vars
    from ansible.utils.vars import load_options_vars
    source, destination = "/etc/hosts", "/etc/hosts.copy"
    # Init
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='localhost,')


# Generated at 2022-06-13 04:56:04.766838
# Unit test for function main
def test_main():
    src = """
- name: Run command if /path/to/database does not exist (without 'args')
  ansible.builtin.command: /usr/bin/make_database.sh db_user db_name creates=/path/to/database
"""
    module = get_module_mock(src)
    module.warn = MagicMock()
    module.run_command = MagicMock(return_value=(0, "out", "err"))
    from ansible.module_utils.common.collections import is_iterable
    def is_iterable_mock(arg, include_strings=False):
        return False
    is_iterable.side_effect = is_iterable_mock

# Generated at 2022-06-13 04:56:06.154101
# Unit test for function main
def test_main():
    pass

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:56:12.289994
# Unit test for function check_command
def test_check_command():
    module = AnsibleModule(argument_spec={})
    for test in [["tar", "unarchive"], ["foo", None]]:
        check_command(module, test[0])
        assert module.warn.called == (test[1] is not None)
        module.warn.called = False
        check_command(module, [test[0], "bar"])
        assert module.warn.called == (test[1] is not None)



# Generated at 2022-06-13 04:56:14.550803
# Unit test for function check_command
def test_check_command():
    commandline = 'chgrp'
    module = AnsibleModule(argument_spec={})
    module.check_command(module, commandline)



# Generated at 2022-06-13 04:56:21.363080
# Unit test for function check_command
def test_check_command():
    module = AnsibleModule({'command': 'command', 'warn': True}, check_mode=False)

    check_command(module, "echo hello")
    check_command(module, "echo hello")
    check_command(module, "echo hello")
    check_command(module, "echo hello")
    check_command(module, "echo hello")



# Generated at 2022-06-13 04:56:25.852247
# Unit test for function check_command
def test_check_command():
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )
    check_command(module, '/bin/chgrp')
    assert 'chgrp' in module._warnings[0]
    assert 'file' in module._warnings[0]



# Generated at 2022-06-13 04:57:00.832467
# Unit test for function check_command
def test_check_command():
    # pylint: disable=redefined-outer-name
    module = AnsibleModule(argument_spec=dict())
    for command in ('curl', 'foo', 'ln', 'rm', 'rpm'):
        check_command(module, [command] + ['argument']*module.params['_checks'])
        assert module.called == 1, "Command '{0}' should have emitted a warning".format(command)



# Generated at 2022-06-13 04:57:07.467960
# Unit test for function check_command
def test_check_command():
    class FakeModule(object):
        def __init__(self):
            self.warns = []
        def warn(self, warning):
            self.warns.append(warning)
    for command in ['chown', 'chmod', 'chgrp', 'ln', 'mkdir', 'rmdir', 'rm', 'touch',
                    'curl', 'wget', 'svn', 'service', 'mount', 'rpm', 'yum', 'apt-get',
                    'tar', 'unzip', 'sed', 'dnf', 'zypper']:
        fake_module = FakeModule()
        check_command(fake_module, [command, 'foo'])
        assert len(fake_module.warns) > 0
        for warn in fake_module.warns:
            assert command in warn

# Generated at 2022-06-13 04:57:08.107240
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-13 04:57:14.923942
# Unit test for function main

# Generated at 2022-06-13 04:57:20.242917
# Unit test for function main
def test_main():
    from ansible import context
    from ansible.utils.path import unfrackpath

    context.CLIARGS = {} # avoid any sideeffects

    # needs some work to work in a unit test
    command = unfrackpath('/bin/echo')
    args = "Hello World!"
    assert main() == True


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:57:29.103288
# Unit test for function check_command
def test_check_command():

    class TestModule(object):
        def __init__(self, params=None, args=None):
            pass

        def exit_json(self, **kwargs):
            pass

        def fail_json(self, **kwargs):
            pass

        def warn(self, msg):
            pass

    class AnsibleModule(TestModule):
        def __init__(self, **kwargs):
            pass

    m = AnsibleModule()
    check_command(m, ['/usr/bin/wget'])



# Generated at 2022-06-13 04:57:33.954664
# Unit test for function main
def test_main():
    args = dict(
        argv=[u'/bin/echo', u'hello'],
        warn=False,
        strip_empty_ends=True
    )
    result = dict(
        delta=None,
        stdout=u'hello',
        stderr=u'',
        msg='',
        start=None,
        end=None,
        changed=False,
        cmd=['/bin/echo', 'hello'],
        rc=0
    )
    module = AnsibleModule(argument_spec={})
    module.params = args
    r = main()
    assert r['rc'] == result['rc']
    assert r['stdout'] == result['stdout']
    assert r['cmd'] == result['cmd']
    assert r['rc'] == result['rc']
    assert r['changed'] == result

# Generated at 2022-06-13 04:57:37.384147
# Unit test for function check_command
def test_check_command():
    m = AnsibleModule(argument_spec={'command': {'default': ['pwd']},
                                     'warn': {'default': True, 'type': 'bool'}})
    check_command(m, m.params['command'])
    assert 'file' in m._result['warnings'][0]
    assert 'pwd' in m._result['warnings'][0]


# Generated at 2022-06-13 04:57:40.759348
# Unit test for function check_command
def test_check_command():
    result = check_command('echo')
    print("This is check_command:", result)


# Generated at 2022-06-13 04:57:49.746912
# Unit test for function check_command
def test_check_command():
    # Test commands with file module arguments
    module = magic_mock()
    check_command(module, 'chown john /tmp/file')
    module.warn.assert_called_with("Consider using the file module with owner=john rather than running 'chown'.  If you need to use 'chown' because the file module is insufficient you can add 'warn: false' to this command task or set 'command_warnings=False' in the defaults section of ansible.cfg to get rid of this message.")

    module = magic_mock()
    check_command(module, 'chmod 600 /tmp/file')

# Generated at 2022-06-13 04:59:02.109574
# Unit test for function main

# Generated at 2022-06-13 04:59:12.490637
# Unit test for function main
def test_main():
    import os
    import tempfile
    import json
    import shutil
    importsys
    if sys.version_info < (2, 7):
        import unittest2 as unittest
    else:
        import unittest

    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes, to_text

    # make sure we consider os.path.samefile on python version < 2.7
    # this is because we cover that feature in the unit test
    if sys.version_info < (2, 7):
        from ansible.module_utils._text import samefile


# Generated at 2022-06-13 04:59:14.569628
# Unit test for function check_command
def test_check_command():
    test_module = AnsibleModule(argument_spec={})
    check_command(test_module, "command")



# Generated at 2022-06-13 04:59:25.277897
# Unit test for function main
def test_main():
    import platform
    import shlex
    argument_spec = dict(
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

# Generated at 2022-06-13 04:59:36.882829
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_text
    import json
    import pytest
    import shlex


# Generated at 2022-06-13 04:59:37.780293
# Unit test for function main
def test_main():
    assert not main(None, None, None)

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:59:48.772696
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common.collections import is_iterable
    from ansible.module_utils._text import to_native, to_bytes, to_text
    import json
    import os
    import shlex
    import sys


# Generated at 2022-06-13 04:59:55.695719
# Unit test for function check_command
def test_check_command():
    # Dummy module for testing
    class DummyModule(object):
        def __init__(self):
            self.warn_msg = None
        def warn(self, msg):
            self.warn_msg = msg

    test_commands = {
        'sudo':
            "Consider using 'become', 'become_method', and 'become_user' rather than running sudo",
        '/usr/bin/chmod':
            "Consider using the file module with mode rather than running '/usr/bin/chmod'",
        'cp':
            "Consider using the copy module or the ansible.builtin.template module rather than running cp",
        'curl':
            "Consider using the get_url or uri module rather than running 'curl'",
    }
    module = DummyModule()

# Generated at 2022-06-13 05:00:09.693224
# Unit test for function main

# Generated at 2022-06-13 05:00:19.520553
# Unit test for function main
def test_main():

    def fail_json(*args, **kwargs):
        raise Exception("Failed")

    def exit_json(*args, **kwargs):
        return 0

    def run_command(*args, **kwargs):
        raise Exception("run_command not implemented")

    def warn(*args, **kwargs):
        return 0

    def check_command(*args, **kwargs):
        return 0

    module = type("module", (), {})()
    module.warn = warn
    module.fail_json = fail_json
    module.exit_json = exit_json
    module.run_command = run_command
    module.check_command = check_command
    module.check_mode = False