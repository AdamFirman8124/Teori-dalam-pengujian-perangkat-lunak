

# Generated at 2022-06-13 06:21:46.850647
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
  runlevels = module.params['runlevels']
  runlevel_status = {}


# Generated at 2022-06-13 06:21:58.574169
# Unit test for function main
def test_main():
    from ansible import context
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.service import sysv_is_enabled, sysv_exists, get_sysv_script, fail_if_missing
    import sys

    sys.argv = ['ansible-test',
                '--verbose',
                '--tb=short',
                'sysvinit',
                'name="nginx"',
                'enabled=yes'
                ]

    context._init_global_context(ImmutableDict({'ANSIBLE_MODULE_ARGS': {}}))

    # Ensure we have a good service name
    name = "nginx"

    fail_if_missing(module, sysv_exists(name), name)

# Generated at 2022-06-13 06:22:09.632480
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', required=True, aliases=['service']),
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

    name = module.params['name']
    action = module.params['state']

# Generated at 2022-06-13 06:22:20.399288
# Unit test for function main
def test_main():
    """
    @return: none
    """
    from sys import version_info
    if version_info[0] == 2:
        import sys
        import StringIO
        import __builtin__

        input = __builtin__.raw_input
        __builtin__.raw_input = lambda _: None

        output = __builtin__.raw_input
        __builtin__.raw_input = lambda _: "y"

        stdout = sys.stdout
        sys.stdout = buf = StringIO.StringIO()

        main()

        sys.stdout = stdout
        __builtin__.raw_input = input

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:22:31.242900
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

    class ActionBase(object):
        def __init__(self):
            self.run_command

# Generated at 2022-06-13 06:22:42.871847
# Unit test for function main
def test_main():
    import os
    import tempfile
    import shutil
    import sys
    import glob

    # Make test dir and files
    tmpdir = tempfile.mkdtemp(prefix='ansible-test-', suffix='-sysvinit')

    # make etc dir
    etc = os.path.join(tmpdir, 'etc')
    os.makedirs(etc)

    # etc/init.d
    initd = os.path.join(etc, 'init.d')
    os.makedirs(initd)
    shutil.copy('/etc/init.d/crond', initd)

    # etc/rc0.d, etc/rc1.d, etc/rc2.d, etc/rc3.d, etc/rc4.d, etc/rc5.d, etc/rc6.d
    init

# Generated at 2022-06-13 06:22:53.442778
# Unit test for function main
def test_main():
    # module
    module = AnsibleModule(
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

    # fail_if_missing
    fail_if_missing(module, True, 'name')
    fail

# Generated at 2022-06-13 06:23:04.668994
# Unit test for function main
def test_main():
    """
    Function: main()
    """
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



# Generated at 2022-06-13 06:23:12.831159
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    import json

    def exec_code(code, add_under=False, locals=None, globals=None):
        if add_under:
            code = '_ = %s' % code

        py_compile.compile(code, '<string>', 'exec')
        exec(code, globals, locals)

    mod_args = {
        'name': 'application',
        'state': 'started',
        'enabled': True
    }
    mod_args_json = json.dumps(mod_args)
    exec_code('mod = AnsibleModule(%s)' % mod_args_json, add_under=True, globals=globals(), locals=locals())

# Generated at 2022-06-13 06:23:20.370230
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

    # run_command
    m = module

# Generated at 2022-06-13 06:25:03.365677
# Unit test for function main
def test_main():
    # Arguments (name, state, enabled, sleep, pattern, arguments, runlevels, daemonize)
    argv = ['name', 'state', 'enabled', 'sleep', 'pattern', 'arguments', 'runlevels', 'daemonize']
    # Defined options
    opts = {
        'name': 'name'
    }
    # Run the module
    rc = main(argv, **opts)
    # Setting up response
    response = {}
    # Check rc
    if rc == 0:
        # Change the rc, so we don't have an expected failure.
        rc = 1
        # Check results
        if isinstance(results, dict):
            # Update response
            response.update(results)
        # Check rc
        if rc == 1:
            # Update response
            response.update(changed=True)
           