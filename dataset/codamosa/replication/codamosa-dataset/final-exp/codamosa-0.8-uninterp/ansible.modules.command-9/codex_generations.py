

# Generated at 2022-06-13 04:52:14.863492
# Unit test for function main

# Generated at 2022-06-13 04:52:16.899634
# Unit test for function main
def test_main():

    result = main()
    assert result == 'Command would have run if not in check mode'

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:52:28.760989
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common.collections import is_iterable
    from ansible.module_utils._text import to_bytes, to_native
    import datetime
    import glob
    import os
    import shlex

# Generated at 2022-06-13 04:52:32.612295
# Unit test for function main
def test_main():
    module = AnsibleModule({'_raw_params': 'ls -l /root'}, check_mode=False)
    assert main() is None

# Generated at 2022-06-13 04:52:34.932399
# Unit test for function check_command
def test_check_command():
    assert check_command(module=None, commandline="ansible.builtin.command cat /etc/motd")



# Generated at 2022-06-13 04:52:43.971596
# Unit test for function main

# Generated at 2022-06-13 04:52:53.854889
# Unit test for function main
def test_main():
    r = dict()
    r['changed'] = False
    r['stdout'] = ''
    r['stderr'] = ''
    r['rc'] = None
    r['cmd'] = None
    r['start'] = None
    r['end'] = None
    r['delta'] = None
    r['msg'] = ''

    # Test running command without passing args/argv
    r['rc'] = 256
    r['msg'] = "no command given"
    assert r == main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:53:06.253824
# Unit test for function main
def test_main():
    command_string = "ls -l"
    module_args = {}
    module_args.update({"_raw_params" : command_string})


# Generated at 2022-06-13 04:53:10.982174
# Unit test for function main
def test_main():
    test_module = AnsibleModule(argument_spec={})
    test_module.params['_raw_params'] = 'This is a test'
    test_main_test = main()
    assert test_main

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:53:11.995825
# Unit test for function main
def test_main():
    arguments = {}
    returned = main()

# Generated at 2022-06-13 04:53:34.561427
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_text
    from ansible.module_utils.common.collections import is_iterable
    from ansible.module_utils import common as common_utils
    # Setting up mock environment for basic AnsibleModule

# Generated at 2022-06-13 04:53:42.323268
# Unit test for function main
def test_main():
    args = {"_raw_params": "ls -al /etc", "_uses_shell": True, "argv": [], "chdir": "", "executable": None,
            "creates": "", "removes": "", "warn": False, "stdin": None, "stdin_add_newline": False,
            "strip_empty_ends": True}


# Generated at 2022-06-13 04:53:56.106780
# Unit test for function main
def test_main():
    class AnsibleFailJsonMock(object):
        def __init__(self, **kwargs):
            self.kwargs = kwargs

        def fail_json(self, **kwargs):
            self.kwargs.update(kwargs)
    class ModuleMock(object):
        def __init__(self, params):
            self.params = params
            self.run_command_result = [0, 'stdout', 'stderr']

        def run_command(self, args, **kwargs):
            self.args = args
            self.kwargs = kwargs
            return self.run_command_result

        def warn(self, msg):
            self.warn_msg = msg

        def exit_json(self, **kwargs):
            self.exit_kwargs = kwargs
            self.exit

# Generated at 2022-06-13 04:54:05.900348
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            _raw_params=dict(default='ls -al'),
            _uses_shell=dict(type='bool', default=False),
            argv=dict(type='list', elements='str'),
            chdir=dict(type='path'),
            executable=dict(),
            creates=dict(type='path'),
            removes=dict(type='path'),
            warn=dict(type='bool', default=False, removed_in_version='2.14', removed_from_collection='ansible.builtin'),
            stdin=dict(),
            stdin_add_newline=dict(type='bool', default=True),
            strip_empty_ends=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )
    main

# Generated at 2022-06-13 04:54:18.792916
# Unit test for function main
def test_main():
    print('Test main: start')


# Generated at 2022-06-13 04:54:26.134056
# Unit test for function main

# Generated at 2022-06-13 04:54:26.815038
# Unit test for function main
def test_main():
    pass


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:54:28.108269
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-13 04:54:37.880561
# Unit test for function main
def test_main():
    import os
    import psutil
    import signal
    import tempfile
    import time
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common.json import AnsibleJSONEncoder
    from ansible.module_utils._text import to_bytes
    from collections import namedtuple


# Generated at 2022-06-13 04:54:44.413842
# Unit test for function main
def test_main():
    # Check if fails with no command argument
    c = dict(
        args = 'echo hello world',
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
            ))

   

# Generated at 2022-06-13 04:55:14.257380
# Unit test for function check_command
def test_check_command():
    m = AnsibleModule(argument_spec=dict())
    check_command(m, '/bin/chown')
    check_command(m, '/bin/chmod')
    check_command(m, '/bin/chgrp')
    check_command(m, '/bin/ln')
    check_command(m, '/bin/mkdir')
    check_command(m, '/bin/rmdir')
    check_command(m, '/bin/rm')
    check_command(m, '/bin/rpm')
    check_command(m, '/bin/svn')
    check_command(m, '/bin/tar')
    check_command(m, '/bin/curl')
    check_command(m, '/bin/wget')
    check_command(m, '/bin/service')

# Generated at 2022-06-13 04:55:22.635557
# Unit test for function main
def test_main():
    args = {'_raw_params': 'mjpg_streamer -i "/usr/local/lib/input_uvc.so -d /dev/video0 -r 320x240 -f 15" -o "/usr/local/lib/output_http.so -w /usr/local/www -p 8080"', '_uses_shell': False, 'warn': False, 'creates': '', 'removes': '', 'strip_empty_ends': True}

# Generated at 2022-06-13 04:55:34.354395
# Unit test for function main

# Generated at 2022-06-13 04:55:46.460161
# Unit test for function main
def test_main():
    """ Function main() """

# Generated at 2022-06-13 04:55:58.934178
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common.collections import is_iterable
    from ansible.module_utils.parsing.convert_bool import boolean
    import ansible.module_utils.basic
    import ansible.module_utils._text
    import os
    import datetime
    import sys
    import json
    import pytest
    import shutil
    import py

    # We are running inside a py.test
    if boolean(os.environ.get('PYTEST_XDIST_WORKER', '0')):
        # We are running inside a py.test
        pytest.skip('skipping test under xdist', allow_module_level=True)

# Generated at 2022-06-13 04:56:10.272297
# Unit test for function main
def test_main():
    _args = {
        '_raw_params': 'echo hello',
        '_uses_shell': False,
        'argv': None,
        'chdir': None,
        'executable': None,
        'creates': None,
        'removes': None,
        'warn': False,
        'stdin': None,
        'stdin_add_newline': True,
        'strip_empty_ends': True,
    }
    with pytest.raises(SystemExit):
        main(**_args)


if __name__ == '__main__':
    main()