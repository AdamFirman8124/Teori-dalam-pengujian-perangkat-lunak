

# Generated at 2022-06-13 06:21:31.409786
# Unit test for function main
def test_main():
    # TODO: Replace this with meaningful unit test
    assert True

test_main()

# Generated at 2022-06-13 06:21:43.473545
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True, type='str', aliases=['service']),
            state=dict(choices=['started', 'stopped', 'restarted', 'reloaded'], type='str'),
            enabled=dict(type='bool'),
            sleep=dict(type='int', default=1),
            pattern=dict(type='str'),
            arguments=dict(type='str', aliases=['args']),
            runlevels=dict(type='list', elements='str'),
            daemonize=dict(type='bool', default=False),
        ),
        supports_check_mode=True,
        required_one_of=[['state', 'enabled']],
    )

    module.run_command = lambda *args, **kwargs: (0, None, None)


# Generated at 2022-06-13 06:21:51.664099
# Unit test for function main
def test_main():
    data = """
        state: started
        enabled: yes
        sleep: 1
        pattern: crap
        arguments: blap
        runlevels:
          - 3
          - 5
    """
    data = yaml.safe_load(data)

# Generated at 2022-06-13 06:22:04.988579
# Unit test for function main
def test_main():
    import sys

    def ansible_module_run():
        sys.argv.append('-m')
        sys.argv.append('sysvinit')
        sys.argv.append('-a')
        sys.argv.append('name=ansible')
        sys.argv.append('state=started')
        sys.argv.append('-e')
        sys.argv.append('host_key_checking=False')
        sys.argv.append('-vvvv')
        sys.argv.append('-c')
        sys.argv.append('local')
        sys.argv.append('-T')
        sys.argv.append('1')

        from ansible.module_utils.basic import AnsibleModule
        return AnsibleModule(check_invalid_arguments=False)

   

# Generated at 2022-06-13 06:22:16.612456
# Unit test for function main
def test_main():
    exit_args = {
        'rc': 0,
        'warnings': [],
        'stdout_lines': [],
        'stderr_lines': [],
        'changed': False,
        'failed': False,
        'msg': ''
    }

# Generated at 2022-06-13 06:22:28.734361
# Unit test for function main
def test_main():
    from ansible.module_utils import arguments
    from ansible.module_utils.basic import AnsibleModule
    from collections import namedtuple

    def run_command_mock(self, cmd):
        # FIXME: this is fragile, use better mocking
        # check if enabling/disabling, not just cmd and fail if bad input
        if "enable" in cmd:
            return (0, "Enabled", "")
        elif "disable" in cmd:
            return (0, "Disabled", "")
        elif "restart" in cmd:
            return (0, "Restarted", "")
        elif "start" in cmd:
            return (0, "Started", "")
        elif "stop" in cmd:
            return (0, "Stopped", "")

# Generated at 2022-06-13 06:22:30.893405
# Unit test for function main
def test_main():
    print('hello')
    main()


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:22:37.456325
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True, type='str', aliases=['service']),
            state=dict(choices=['started', 'stopped', 'restarted', 'reloaded'], type='str'),
            enabled=dict(type='bool'),
            sleep=dict(type='int', default=1),
            pattern=dict(type='str'),
            arguments=dict(type='str', aliases=['args']),
            runlevels=dict(type='list', elements='str'),
            daemonize=dict(type='bool', default=False),
        ),
        supports_check_mode=True,
        required_one_of=[['state', 'enabled']],
    )

    module.exit_json(rc=0)

# Generated at 2022-06-13 06:22:38.153408
# Unit test for function main
def test_main():
    print('main')

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:22:47.862566
# Unit test for function main
def test_main():
    import tempfile
    fd, temp_path = tempfile.mkstemp()
    output = open(temp_path, 'w')
    output.write('''#!/bin/bash\n
    # chkconfig: 345 99 01
    # description: Some description
    # processname: Some name\n''')
    output.write('case "$1" in\n')
    output.write('start)\n')
    output.write('    exit 0\n')
    output.write('    ;;\n')
    output.write('stop)\n')
    output.write('    exit 0\n')
    output.write('    ;;\n')
    output.write('restart)\n')
    output.write('    exit 0\n')
    output.write('    ;;\n')

# Generated at 2022-06-13 06:23:43.219588
# Unit test for function main
def test_main():
    from ansible.module_utils.service import sysv_exists, sysv_is_enabled, get_sysv_script, get_ps
    import os, tempfile
    tempdir = tempfile.mkdtemp()
    service_file = "%s/myservice" % tempdir
    runlevel_file = "%s/myservice.conf" % tempdir
    f_handle = open(service_file, 'w')
    f_handle.write("#!/bin/sh\n\n# This is a sysv init script\n\n# chkconfig: 123 45 67\n# description: My Service\n\nMy service")
    f_handle.close()
    f_handle = open(runlevel_file, 'w')

# Generated at 2022-06-13 06:23:44.708392
# Unit test for function main
def test_main():
    assert 1 == 1

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:23:46.319473
# Unit test for function main
def test_main():
    main()

if __name__ == "__main__":
    main()

# Generated at 2022-06-13 06:23:55.598200
# Unit test for function main
def test_main():
    test = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True, type='str'),
            state=dict(choices=['started', 'stopped', 'restarted', 'reloaded'], type='str'),
            enabled=dict(type='bool'),
            sleep=dict(type='int', default=1),
            pattern=dict(type='str'),
            arguments=dict(type='str', aliases=['args']),
            runlevels=dict(type='list', elements='str'),
            daemonize=dict(type='bool', default=False),
        ),
        supports_check_mode=True,
        required_one_of=[['state', 'enabled']],
    )
    test.get_bin_path = lambda x, opt=None: '/bin/' + x
    test.run_command

# Generated at 2022-06-13 06:23:57.402641
# Unit test for function main
def test_main():
    with pytest.raises(FailJsonException) as excinfo:
        main()
    assert 'required one of the following' in str(excinfo)



# Generated at 2022-06-13 06:24:02.930699
# Unit test for function main
def test_main():

    failed = False

    with open('tests/test_sysvinit_a', 'r') as content_file:
        test_str = content_file.read()
    try:
        import json
        test_dict = json.loads(test_str)
    except ValueError:
        test_dict = yaml.load(test_str)

    check_mode = test_dict['ansible_check_mode']
    daemonize = test_dict['ansible_daemonize']
    enabled = test_dict['ansible_enabled']
    name = test_dict['ansible_name']
    script = test_dict['ansible_script']
    sleep = test_dict['ansible_sleep']
    state = test_dict['ansible_state']
    arguments = test_dict['ansible_arguments']

# Generated at 2022-06-13 06:24:10.167626
# Unit test for function main

# Generated at 2022-06-13 06:24:20.084015
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True, type='str', aliases=['service']),
            state=dict(choices=['started', 'stopped', 'restarted', 'reloaded'], type='str'),
            enabled=dict(type='bool'),
            sleep=dict(type='int', default=1),
            pattern=dict(type='str'),
            arguments=dict(type='str', aliases=['args']),
            runlevels=dict(type='list', elements='str'),
        ),
        supports_check_mode=True,
        required_one_of=[['state', 'enabled']],
    )

    # Mock need things from module
    module._ansible_verbosity = 3
    module.run_command = mock.MagicMock()
    module.get_

# Generated at 2022-06-13 06:24:30.793851
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True, type='str', aliases=['service']),
            state=dict(choices=['started', 'stopped', 'restarted', 'reloaded'], type='str'),
            enabled=dict(type='bool'),
            sleep=dict(type='int', default=1),
            pattern=dict(type='str'),
            arguments=dict(type='str', aliases=['args']),
            runlevels=dict(type='list', elements='str'),
            daemonize=dict(type='bool', default=False),
        ),
        supports_check_mode=True,
        required_one_of=[['state', 'enabled']],
    )
    import os
    import sys
    import tempfile


# Generated at 2022-06-13 06:24:40.792390
# Unit test for function main
def test_main():
  with open('test_data/test_sysvinit.json') as f:
    module = AnsibleModule(
      argument_spec=dict(
            name=dict(required=True, type='str', aliases=['service']),
            state=dict(choices=['started', 'stopped', 'restarted', 'reloaded'], type='str'),
            enabled=dict(type='bool'),
            sleep=dict(type='int', default=1),
            pattern=dict(type='str'),
            arguments=dict(type='str', aliases=['args']),
            runlevels=dict(type='list', elements='str'),
            daemonize=dict(type='bool', default=False),
        ),
        required_one_of=[['state', 'enabled']],
    )
    module.params = json.load(f)
   

# Generated at 2022-06-13 06:26:20.587793
# Unit test for function main
def test_main():
    print("Nothing to test")

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:26:28.788149
# Unit test for function main
def test_main():
    # called as module, so we need to set up the args ourselves
    module = AnsibleModule(argument_spec=dict(
        name=dict(required=True, type='str', aliases=['service']),
        state=dict(choices=['started', 'stopped', 'restarted', 'reloaded'], type='str'),
        enabled=dict(type='bool'),
        sleep=dict(type='int', default=1),
        pattern=dict(type='str'),
        arguments=dict(type='str', aliases=['args']),
        runlevels=dict(type='list', elements='str'),
        daemonize=dict(type='bool', default=False),
        ),
        supports_check_mode=True,
        required_one_of=[['state', 'enabled']],
    )
    main()


# Generated at 2022-06-13 06:26:31.554624
# Unit test for function main
def test_main():
    # test module
    a = AnsibleModule( 'sysvinit',
                    name = 'httpd',
                    state = 'started',
                    enabled = 'yes',
                    daemonize = 'no' )
    # run module
    main()

if __name__ == "__main__":
    main()

# Generated at 2022-06-13 06:26:33.304440
# Unit test for function main
def test_main():
    # FIXME: Test this!
    pass

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:26:46.194197
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils.service import sysv_is_enabled, get_sysv_script, sysv_exists, fail_if_missing, get_ps, daemonize

# Generated at 2022-06-13 06:26:55.372202
# Unit test for function main
def test_main():
    from ansible.module_utils.service import get_ps
    from ansible.module_utils.six import PY3
    from ansible.module_utils.six import text_type
    import sys
    import re

    mock_config = {
        'name': 'apache2',
        'sleep': 1,
        'arguments': '',
        'enabled': False,
        'action': '',
        'script': 'apache2ctl',
        'pattern': '',
        'runlevels': ''
    }


# Generated at 2022-06-13 06:27:06.373764
# Unit test for function main
def test_main():

    ##
    ## SYSCFG:
    ## core_syscfg_get_tuple: function: locals = <dict object at 0xb62350>, key_value_tuple = ('name', 'apache2')
    ##
    mock_ansible_module = MagicMock(name='sysvinit mock module')
    mock_ansible_module.params = {
        'name': 'apache2',
        'state': 'started',
        'enabled': True,
        'sleep': 1,
        'pattern': '',
        'arguments': '',
        'runlevels': [],
        'daemonize': False,
    }
    mock_ansible_module.check_mode = False
    mock_ansible_module.get_bin_path.side_effect = lambda n,a: n


# Generated at 2022-06-13 06:27:16.290882
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.basic import AnsibleModule
    """
    Test to make sure all parameters work together.

    :param self: Self reference for the class
    :return: None
    """
    #
    # set up
    #
    module = AnsibleModule({
        'enabled': True,
        'pattern': None,
        'runlevels': None,
        'state': None,
        'name': 'apache2',
        'sleep': 1
    })

    #
    # call test main
    #
    main()

# Import module snippets
from ansible.module_utils.basic import *
if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:27:22.911933
# Unit test for function main
def test_main():
    import json
    
    module = AnsibleModule(argument_spec=dict(
        enabled=dict(type='bool'),
        runlevels=dict(type='list', elements='str'),
        name=dict(required=True, type='str', aliases=['service']),
        arguments=dict(type='str', aliases=['args']),
        state=dict(choices=['started', 'stopped', 'restarted', 'reloaded'], type='str'),
        sleep=dict(type='int', default=1),
        pattern=dict(type='str'),
        daemonize=dict(type='bool', default=False),
    ), required_one_of=[['state', 'enabled']])
    
    if module.params['enabled'] is not None or module.params.get('state') is not None:
        is_enabled = sy

# Generated at 2022-06-13 06:27:34.201677
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils.service import sysv_is_enabled, get_sysv_script, sysv_exists, fail_if_missing, get_ps, daemonize
    import sys
