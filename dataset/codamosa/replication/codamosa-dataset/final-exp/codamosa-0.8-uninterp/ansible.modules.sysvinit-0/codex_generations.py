

# Generated at 2022-06-13 06:21:45.177743
# Unit test for function main
def test_main():
    result = {}
    #result['attempts'] = 0
    result['changed'] = True
    result['name'] = 'apache2'
    result['status'] = {}
    result['status']['enabled'] = {}
    result['status']['enabled']['changed'] = False
    result['status']['enabled']['rc'] = 1
    result['status']['enabled']['stderr'] = 'stderr'
    result['status']['enabled']['stdout'] = 'stdout'
    result['status']['stopped'] = {}
    result['status']['stopped']['changed'] = False
    result['status']['stopped']['rc'] = 0
    result['status']['stopped']['stderr'] = ''

# Generated at 2022-06-13 06:21:50.592372
# Unit test for function main
def test_main():

    test_main_args = dict(
        {}
    )

    test_main_exit_success = dict(
        rc=0
    )

    test_main_exit_fail = dict(
        rc=1
    )
    if __name__ == '__main__':
        module = AnsibleModule(**test_main_args)
        module.exit_json(**test_main_exit_success)


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:22:03.995981
# Unit test for function main

# Generated at 2022-06-13 06:22:16.475357
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
        supports_check_mode=True)

    sysvinit.main()

# include magic from lib/ansible/module_utils/basic.py
#<<INCLUDE_ANSIBLE_MODULE_COMMON

# Generated at 2022-06-13 06:22:22.779137
# Unit test for function main
def test_main():
    rep = {
        'name': 'apache2',
        'changed': True,
        'status': {
            'enabled': {
                'changed': True,
                'rc': 0,
                'stderr': '',
                'stdout': ''
            },
            'stopped': {
                'changed': True,
                'rc': 0,
                'stderr': 'Stopping web server: apache2.\n',
                'stdout': ''
            }
        }
    }
    assert main()==rep


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:22:33.117548
# Unit test for function main
def test_main():

    VALID_ARGUMENTS = dict(
        name = 'sysvinit_name',
        state = 'state_name',
        enabled = True,
        sleep = 1,
        pattern = 'sysvinit_pattern',
        arguments = 'sysvinit_arguments',
        runlevels = ['runlevel_list'],
        daemonize = True,
    )

# Generated at 2022-06-13 06:22:45.434449
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
    module.main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:22:55.828841
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.action._sysvinit import main

# There's a bug in this code that causes it to fail
# for more information please refer to:
# https://github.com/ansible/ansible/issues/44244
#    m = basic.AnsibleModule(
#        argument_spec={
#            'name': {'required': True, 'type': 'str', 'aliases': ['service']},
#            'state': {'choices': ['started', 'stopped', 'restarted', 'reloaded'], 'type': 'str'},
#            'enabled': {'type': 'bool'},
#            'sleep': {'type': 'int', 'default': 1},
#            '

# Generated at 2022-06-13 06:23:07.322136
# Unit test for function main
def test_main():
    test_name = "test.test"
    test_state = "started"
    test_args = "test"
    test_arguments = ""
    test_runlevels = ["1"]
    test_enabled = True
    test_sleep = "1"
    test_pid = "12345"

    test_location = {
        'service': '/usr/bin/service'
    }


# Generated at 2022-06-13 06:23:11.560678
# Unit test for function main
def test_main():
    #import ansible.modules.system.sysvinit as sysvinit
    assert sysvinit.module.get_bin_path('ls').find('ls')
    assert not sysvinit.module.get_bin_path('xyz')
    assert re.sub('p?ed$', '', 'restarted').lower() == 'restart'
    assert re.sub('p?ed$', '', 'started').lower() == 'start'
    assert re.sub('p?ed$', '', 'stopped').lower() == 'stop'
    assert re.sub('p?ed$', '', 'reloaded').lower() == 'reload'

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:24:11.465206
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

# Generated at 2022-06-13 06:24:21.312887
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
    result = main()
    assert result['changed'] == False

# Generated at 2022-06-13 06:24:32.741383
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
    assert main() == None

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:24:41.218636
# Unit test for function main
def test_main():
    # Make sure nothing has changed in the main function
    # Get module args from the args file
    module_args = dict(
        name=dict(required=True, type='str', aliases=['service']),
        state=dict(choices=['started', 'stopped', 'restarted', 'reloaded'], type='str'),
        enabled=dict(type='bool'),
        sleep=dict(type='int', default=1),
        pattern=dict(type='str'),
        arguments=dict(type='str', aliases=['args']),
        runlevels=dict(type='list', elements='str'),
        daemonize=dict(type='bool', default=False),
    )
    # Create a mock module
    module = AnsibleModule(argument_spec=module_args)
    def sysv_exists(name):
        return True

# Generated at 2022-06-13 06:24:53.035768
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

    # set up the test environment

# Generated at 2022-06-13 06:24:54.798461
# Unit test for function main
def test_main():
    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:25:02.766151
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

# Generated at 2022-06-13 06:25:04.160590
# Unit test for function main
def test_main():
    module = AnsibleModule(argument_spec={})
    print(main())


# Generated at 2022-06-13 06:25:12.725544
# Unit test for function main
def test_main():
    """
    Test function main
    """

    # Test module arguments
    module_args = { "name": "exp1", "state": "exp2", "sleep": 10, "pattern": "exp3", "enabled": False, "arguments": "exp4", "runlevels": "exp5", "daemonize": False, }
    # Construct incomplete module
    module = AnsibleModule(**module_args)

    # Mock module input parameters
    class args:
        def __init__(self):
            self.name = "exp1"
            self.state = "exp2"
            self.sleep = 10
            self.pattern = "exp3"
            self.enabled = False
            self.arguments = "exp4"
            self.runlevels = "exp5"
            self.daemonize = False

# Generated at 2022-06-13 06:25:23.005368
# Unit test for function main
def test_main():
    from ansible.module_utils.common._collections_compat import Mapping

# Generated at 2022-06-13 06:27:23.354356
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule

# Generated at 2022-06-13 06:27:25.041772
# Unit test for function main
def test_main():
    module = AnsibleModule(argument_spec={})
    assert module.exit_json.called

# Generated at 2022-06-13 06:27:35.462237
# Unit test for function main
def test_main():
    from ansible.module_utils.service import *
    import os
    import pytest
    import json
    names = os.environ['SERVICE_NAMES'].split(',')
    data = {}
    for name in names:
        # TODO: Add more tests
        if name == 'apache2':
            pass
        else:
            data[name] = {}
            data[name]['name'] = name
            data[name]['state'] = "started"
            data[name]['enabled'] = True
            data[name]['pattern'] = 'blank'
            data[name]['runlevels'] = []

    for script in data.keys():
        action = data[script]
        service_name = action['name']
        if action['state'] == 'started':
            action['state'] = 'stopped'

# Generated at 2022-06-13 06:27:50.959185
# Unit test for function main
def test_main():
    src = {
        'UPDATE_RC_D': '/usr/sbin/update-rc.d',
        'CHKCONFIG': '/usr/sbin/chkconfig',
        'SERVICE': '/usr/bin/service',
        'INSERVICE': '/usr/sbin/insserv',
    }
    dest = {}
    results = {}


# Generated at 2022-06-13 06:28:00.041821
# Unit test for function main
def test_main():
    module = AnsibleModule(argument_spec={
            'name' : dict(required=True, type='str', aliases=['service']),
            'state' : dict(choices=['started', 'stopped', 'restarted', 'reloaded'], type='str'),
            'enabled' : dict(type='bool'),
            'sleep' : dict(type='int', default=1),
            'pattern' : dict(type='str'),
            'arguments' : dict(type='str', aliases=['args']),
            'runlevels' : dict(type='list', elements='str'),
            'daemonize' : dict(type='bool', default=False),
        })
    sysvinit = __import__('sysvinit')
    sysvinit.main()

# Generated at 2022-06-13 06:28:12.678785
# Unit test for function main
def test_main():

    # setup test object
    class fakeModule:

        def __init__(self, i):

            self.params = {
                    'name': 'test',
                    'state': 'started',
                    'enabled': 'yes',
                    'runlevels': ['3', '5'],
                    'daemonize': False,
                    'sleep': 1,
            }

            self.check_mode = False
            self.called_commands = []
            self.warnings = []

        def run_command(self, cmd, tmp_path, su_user='root', su_exe='/bin/su'):
            self.called_commands.append(cmd)
            return 0, '', ''

        def get_bin_path(self, binary, opt_dirs=tuple()):
            return "fake %s" % binary


# Generated at 2022-06-13 06:28:23.677264
# Unit test for function main
def test_main():
    module = AnsibleModule(argument_spec={
        "name": {"required": True, "type": "str"},
        "state": {"type": "str", "choices": ['started', 'stopped', 'restarted', 'reloaded']},
        "enabled": {"type": "bool"},
        "sleep": {"type": "int", "default": 1},
        "pattern": {"type": "str"},
        "arguments": {"type": "str", "aliases": ['args']},
        "runlevels": {"type": "list", "elements": 'str'},
        "daemonize": {"type": "bool", "default": False},
    })
    module.main()
# import module snippets
from ansible.module_utils.basic import *
from ansible.module_utils.service import sysv_exists, sysv

# Generated at 2022-06-13 06:28:33.377063
# Unit test for function main
def test_main():
    module = AnsibleModule(name='test', argument_spec=dict(
        name=dict(required=True, type='str', aliases=['service']),
        state=dict(choices=['started', 'stopped', 'restarted', 'reloaded'], type='str'),
        enabled=dict(type='bool'),
        sleep=dict(type='int', default=1),
        pattern=dict(type='str'),
        arguments=dict(type='str', aliases=['args']),
        runlevels=dict(type='list', elements='str'),
        daemonize=dict(type='bool', default=False),
    ))
    assert main() == module.fail_json


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:28:46.224019
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

    name = BINDIR + '/touched.sh'
    is_enabled = False

# Generated at 2022-06-13 06:28:53.355781
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