

# Generated at 2022-06-13 06:21:44.678758
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec={
            'name': dict(required=True, type='str', aliases=['service']),
            'state': dict(choices=['started', 'stopped', 'restarted', 'reloaded'], type='str'),
            'enabled': dict(type='bool'),
            'sleep': dict(type='int', default=1),
            'pattern': dict(type='str'),
            'arguments': dict(type='str', aliases=['args']),
            'runlevels': dict(type='list', elements='str'),
            'daemonize': dict(type='bool', default=False),
        },
        supports_check_mode=True,
        required_one_of=[['state', 'enabled']],
    )
    module.exit_json(something='somevalue')



# Generated at 2022-06-13 06:21:54.270976
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

    name = module.params['name']
    action = module.params['state']

# Generated at 2022-06-13 06:22:06.730884
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils import service
    import sys
    import os
    import pytest
    from unittest.mock import patch, MagicMock, Mock, mock_open
    from ansible.module_utils._text import to_bytes
    import ansible_collections.notstdlib.moveitallout.plugins.module_utils.sysvinit as sysv

    m_args = MagicMock(name='args')
    m_args.daemonize = False

    m_service = MagicMock(name='service')
    m_service.script = 'a/b/c/d'
    m_service.name = 'named'

    m_module = MagicMock(name='module', spec=AnsibleModule, arguments=m_args)
    m_module

# Generated at 2022-06-13 06:22:18.397325
# Unit test for function main
def test_main():

    import os
    import shutil
    import tempfile

    tmpdir = tempfile.mkdtemp()
    print("running test in tmpdir=%s" % tmpdir)

    service_name = 'mock_service'
    service_script = os.path.join(tmpdir, service_name)
    service_script_status = os.path.join(tmpdir, service_name) + '-status'


# Generated at 2022-06-13 06:22:29.737422
# Unit test for function main
def test_main():
    argument_spec = dict(
        name=dict(required=True, type='str', aliases=['service']),
        state=dict(choices=['started', 'stopped', 'restarted', 'reloaded'], type='str'),
        enabled=dict(type='bool'),
        sleep=dict(type='int', default=1),
        pattern=dict(type='str'),
        arguments=dict(type='str', aliases=['args']),
        runlevels=dict(type='list', elements='str'),
        daemonize=dict(type='bool', default=False),
    )
    module = AnsibleModule(argument_spec=argument_spec)
    main()


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:22:36.854029
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
    name = module.params['name']
    action = module.params['state']

# Generated at 2022-06-13 06:22:47.400314
# Unit test for function main
def test_main():
    import json
    import sys

    from ansible.module_utils.basic import AnsibleModule

    from ansible.module_utils.ansible_release import __version__ as release_version

    if not sys.version_info >= (3, 0):
        # if we can't use json.loads() on the result data, we will get TypeError
        # in AnsibleModule.exit_json() and the result will be not properly
        # sent to the Ansible controller
        json_loads = lambda x: x
    else:
        json_loads = json.loads


# Generated at 2022-06-13 06:22:49.017930
# Unit test for function main
def test_main():

    res = main()
    print(res)
# Run unit test first
test_main()

# Generated at 2022-06-13 06:23:00.435479
# Unit test for function main
def test_main():
    import os
    import tempfile
    import shutil
    import mock

    # Create a temporary directory
    tmpdir = tempfile.mkdtemp()

    module = mock.MagicMock(check_mode=False)
    module.exit_json = mock.MagicMock(return_value=None)
    module.fail_json = mock.MagicMock(return_value=[""])
    module.params = dict()
    module.run_command = mock.MagicMock(return_value=[0, "", ""])
    module.get_bin_path = mock.MagicMock(return_value=True)
    module.warn = mock.MagicMock(return_value=None)

    result = dict()

    # Should fail if no valid params
    try:
        main()
    except SystemExit:
        pass



# Generated at 2022-06-13 06:23:10.546652
# Unit test for function main
def test_main():
    module = AnsibleModule(argument_spec = dict(
        name = dict(required = True, type = 'str', aliases = ['service']),
        state = dict(choices = ['started', 'stopped', 'restarted', 'reloaded'], type = 'str'),
        enabled = dict(type = 'bool'),
        sleep = dict(type = 'int', default = 1),
        pattern = dict(type = 'str'),
        arguments = dict(type = 'str', aliases = ['args']),
        runlevels = dict(type = 'list', elements = 'str'),
        daemonize = dict(type = 'bool', default = False),
    ), supports_check_mode = True, required_one_of = [['state', 'enabled']])
    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:24:03.150916
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

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:24:04.485496
# Unit test for function main
def test_main():
    print("test_main")


# Generated at 2022-06-13 06:24:14.610336
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True, type='str'),
            state=dict(choices=['started', 'stopped', 'restarted', 'reloaded'], type='str'),
            enabled=dict(type='bool'),
            sleep=dict(type='int', default=1),
            pattern=dict(type='str'),
            arguments=dict(type='str', aliases=['args']),
            runlevels=dict(type='list', elements='str'),
            daemonize=dict(type='bool', default=False)
        ),
        supports_check_mode=True,
        required_one_of=[['state', 'enabled']]
    )
    assert main() == None

# Generated at 2022-06-13 06:24:23.469920
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

    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:24:32.250349
# Unit test for function main
def test_main():
    '''sysvinit unit test'''
    import sys
    import json

    sys.argv = [
        'sysvinit',
        '-s',
        'start',
        '-n',
        'service1'
    ]
    print(main())

    sys.argv = [
        'sysvinit',
        '-s',
        'start',
        '-n',
        'service1'
    ]
    print(main())

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:24:39.843782
# Unit test for function main
def test_main():
    # Mock ansible module to catch the results
    mod = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True, type='str', aliases=['service']),
            enabled=dict(type='bool', default=None),
            state=dict(choices=['started', 'stopped', 'restarted', 'reloaded'], type='str'),
            sleep=dict(type='int', default=1),
            pattern=dict(type='str'),
            arguments=dict(type='str', aliases=['args']),
            runlevels=dict(type='list', elements='str'),
            daemonize=dict(type='bool', default=False),
        ),
        supports_check_mode=True,
        required_one_of=[['state', 'enabled']],
    )


# Generated at 2022-06-13 06:24:42.614592
# Unit test for function main
def test_main():
    if __name__ == '__main__':
        main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:24:48.999114
# Unit test for function main
def test_main():

    module_args = dict(
        name='httpd',
        enabled=True,
        daemonize=True,
    )
    module = AnsibleModule(argument_spec=module_args)
    i = 5
    while i > 0:
        i -= 1
        result = main()
        assert result['status']['enabled']['rc'] in [0, None]
test_main()

# Generated at 2022-06-13 06:24:57.085207
# Unit test for function main
def test_main():
    # Mock module
    module = AnsibleModule({
        'name': 'foo',
        'state': 'started',
        'enabled': True,
    })

    # Mock code
    class Foo(object):
        def __init__(self):
            pass

    module.get_bin_path = Foo
    module.run_command = Foo
    module.warn = Foo
    module.fail_json = Foo
    module.exit_json = Foo
    # Action
    main()


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:24:58.465133
# Unit test for function main
def test_main():
    pass


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:25:57.511775
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    import re

    # is_started
    is_started = False
    worked = False
    paths = ['/sbin', '/usr/sbin', '/bin', '/usr/bin']

    binaries = ['chkconfig', 'update-rc.d', 'insserv', 'service']
    location = {}
    for binary in binaries:
        location[binary] = '/bin/%s' % binary

    module = AnsibleModule('service', 'name=test')
    module.run_command = lambda x: (0, '', '')
    module.exit_json = lambda x: None
    module.fail_json = lambda x: None
    module.get_bin_path = lambda x, y: '/bin/%s' % x

    # Test for existing pattern
   

# Generated at 2022-06-13 06:26:00.862811
# Unit test for function main
def test_main():
    filename = 'tmp.py'
    args = dict(
        name='apache2',
        state='started',
        enabled=True,
        pattern=None,
        sleep='1',
        arguments=None,
        runlevels='3',
    )
    main(**args)

if __name__ == '__main__':
    main()