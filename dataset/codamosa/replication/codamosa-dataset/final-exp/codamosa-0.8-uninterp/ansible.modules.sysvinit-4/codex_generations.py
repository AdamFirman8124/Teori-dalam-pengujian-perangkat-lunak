

# Generated at 2022-06-13 06:21:43.936152
# Unit test for function main
def test_main():
    import sys
    import os
    import pytest
    sys.path.append(os.path.join(os.environ["TEST_DIR"], ".."))
    from ansible.module_utils.common.process import get_bin_path
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.service import get_sysv_script
    from ansible.module_utils.sysvinit import sysv_is_enabled
    from ansible.module_utils.basic import AnsibleModule

# Generated at 2022-06-13 06:21:51.918951
# Unit test for function main

# Generated at 2022-06-13 06:22:05.124232
# Unit test for function main

# Generated at 2022-06-13 06:22:16.750896
# Unit test for function main
def test_main():
    import json
    import subprocess
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils._text import to_bytes

    def get_result(cmd):
        return subprocess.check_output(cmd, stderr=subprocess.STDOUT)

    def get_module_args(changed=False):
        return {
            'name': 'foo',
            'state': 'stopped',
            '_ansible_check_mode': False,
            '_ansible_verbosity': 2,
            '_ansible_no_log': False,
            'changed': changed
        }


# Generated at 2022-06-13 06:22:24.056297
# Unit test for function main
def test_main():
    name = "apache2"
    state = "stopped"
    enabled = "False"
    sleep = "1"
    pattern = "apache2"
    arguments = "args"
    runlevels = ['3', '5']
    daemonize = "False"
    check_mode = "True"
    action = "start"
    is_started = "True"
    worked = "False"
    cmd = "chkconfig --level 35 apache2 on"

    # location = {
    #     "chkconfig" : "chkconfig",
    #     "update-rc.d" : "update-rc.d"
    #     }
    location = {}
    for binary in binaries:
        location.update(binary)

    # runlevel_status = {
    #     "3" : "True",
    #

# Generated at 2022-06-13 06:22:34.199359
# Unit test for function main
def test_main():
    class FakeModule(object):
        def __init__(self, params):
            self.params = params
            self.fail_json = lambda msg: msg
            self.run_command = lambda cmd: [0, '', '']
            self.run_init_script = lambda name, cmd: [0, '', '']
        
    def fake_get_bin_path(name, opt_dirs=[]):
        return '/path/to/' + name
        
    fake_module = FakeModule({
        'name': 'nginx',
        'state': 'started',
        'enabled': True,
        'runlevels': ['3', '5'],
        'arguments': '',
        'daemonize': False
    })
    fake_module.get_bin_path = fake_get_bin_path

# Generated at 2022-06-13 06:22:36.125452
# Unit test for function main
def test_main():
    main()

# import module snippets
main()

# Generated at 2022-06-13 06:22:46.957115
# Unit test for function main
def test_main():
    ''' test_main is a unit testing function to test function main '''
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

    # Mock input arguments

# Generated at 2022-06-13 06:22:55.899904
# Unit test for function main
def test_main():
    import ConfigParser
    import StringIO

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.service import sysv_is_enabled, get_sysv_script, sysv_exists, fail_if_missing, get_ps, daemonize

    #  set system daemons for unit testing
    config = ConfigParser.ConfigParser()
    buf = StringIO.StringIO()
    buf.write('[Unit]\n')
    buf.write('Description=Dummy service\n')
    buf.write('After=syslog.target\n')
    buf.write('[Service]\n')
    buf.write('Type=forking\n')
    buf.write('PIDFile=/var/run/dummy.pid\n')

# Generated at 2022-06-13 06:22:59.486042
# Unit test for function main
def test_main():    
    # Mock function call
    def run_command(module, cmd):
        return ('', '', '')
        
    pass


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:23:51.158753
# Unit test for function main
def test_main():
    with pytest.raises(FailJsonException) as excinfo:
        main()
    assert 'required one of' in str(excinfo.value)


# Generated at 2022-06-13 06:23:58.701227
# Unit test for function main
def test_main():

    from ansible.module_utils import basic
    from ansible.module_utils.service import sysv_exists
    from ansible.module_utils.service import sysv_is_enabled
    from ansible.module_utils.service import get_sysv_script
    from ansible.module_utils.service import fail_if_missing
    from ansible.module_utils.service import get_ps

    from ansible.module_utils.basic import AnsibleModule


# Generated at 2022-06-13 06:24:07.213546
# Unit test for function main
def test_main():
    module = AnsibleModule
    module.get_bin_path = lambda x, y, z: True
    module.run_command = lambda x, y, z: (0, '', '')
    setattr(module, 'check_mode', False)
    setattr(module, '_sysv_is_enabled', lambda x, y: True)
    setattr(module, '_get_sysv_script', lambda x: 'script')
    result = main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:24:17.448883
# Unit test for function main
def test_main():
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

    rc = 1
    out = err = ''


# Generated at 2022-06-13 06:24:26.317073
# Unit test for function main
def test_main():
    '''
    Unit test for function main
    '''
    module = AnsibleModule(argument_spec=dict())
    # stub sysvinit function
    def service(name):
        '''
        Stub function to stub out sysvinit.service
        '''
        return (True, [name])

    module.sysvinit = service
    # Stub AnsibleModule.run_command function
    def run_command(self, cmd):
        '''
        Stubs out the AnsibleModule.run_command function
        '''
        return (0, "", "")

    module.run_command = run_command
    # Stub AnsibleModule.get_bin_path function
    def get_bin_path(self, arg):
        '''
        Stubs the the AnsibleModule.get_bin_path function
        '''


# Generated at 2022-06-13 06:24:37.846783
# Unit test for function main
def test_main():
    # Mock setup
    import sys
    sys.modules['ansible'] = __import__('ansible')
    sys.modules['ansible.utils'] = __import__('ansible.utils')
    sys.modules['ansible.module_utils'] = __import__('ansible.module_utils')
    sys.modules['ansible.module_utils.basic'] = __import__('ansible.module_utils.basic')
    sys.modules['ansible.module_utils.basic.AnsibleModule'] = __import__('ansible.module_utils.basic').AnsibleModule
    sys.modules['ansible.module_utils.basic.AnsibleModule.run_command'] = __import__('ansible.module_utils.basic').AnsibleModule.run_command
    sys.modules['ansible.module_utils.action']

# Generated at 2022-06-13 06:24:50.178269
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec = dict(
            name = dict(required = True, type = str, aliases = ['service']),
            state = dict(
                choices = ['started', 'stopped', 'restarted', 'reloaded'],
                type = str
            ),
            enabled = dict(type = 'bool'),
            sleep = dict(type = int, default = 1),
            pattern = dict(type = str),
            arguments = dict(type = str, aliases = ['args']),
            runlevels = dict(type = list, elements = 'str'),
            daemonize = dict(type = 'bool', default = False)
        ),
        # supports_check_mode = True,
        # required_one_of = [['state', 'enabled']]
    )

    main()


# Generated at 2022-06-13 06:24:52.160977
# Unit test for function main
def test_main():
    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:25:01.459692
# Unit test for function main
def test_main():
    '''
    Unit tests for function main
    '''
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

    name = module.params['name']
    action = module.params['state']

# Generated at 2022-06-13 06:25:10.988223
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

# Generated at 2022-06-13 06:27:09.995818
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

    # Set up test data

    # Get the module parameters
    params = module.params

    #

# Generated at 2022-06-13 06:27:19.780300
# Unit test for function main
def test_main():
    test_str_out = """
{
    "name": "apache2",
    "changed": false,
    "status": {
        "started": {
            "changed": false
        }
    }
}
"""
    fields = {
        "name": "apache2",
        "state": "started",
        "enabled": "yes",
        "runlevels": "3 5",
        "sleep": "1",
        "pattern": "",
        "arguments": ""
    }


# Generated at 2022-06-13 06:27:25.778952
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
    rc = 0
    out = err = ''

# Generated at 2022-06-13 06:27:35.525683
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            state=dict(choices=['started', 'stopped', 'restarted', 'reloaded'], default=None),
            enabled=dict(type='bool', default=None),
            sleep=dict(type='int', default=1),
            pattern=dict(type='str', default=None),
            arguments=dict(type='str', default=None),
            daemonize=dict(type='bool', default=False),
        ),
        supports_check_mode=True,
        required_one_of=[['state', 'enabled']],
    )
    # mock the run_command and get_bin_path methods
    module.run_command = mock.Mock()
    module.get_bin_path = mock.Mock()

# Generated at 2022-06-13 06:27:51.031348
# Unit test for function main
def test_main():
    import ansible.module_utils
    import ansible.module_utils.basic
    import ansible.module_utils.service
    import ansible.module_utils.common
    import sys

    # AnsibleModule unit test:
    # code under test is called from the main() method of the AnsibleModule object,
    # this mock object and it's methods allow the code under test to be called, and
    # for the return values to be captured for the unit test

# Generated at 2022-06-13 06:28:00.327807
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
    # test with good parameters 
    # test common case

# Generated at 2022-06-13 06:28:03.290417
# Unit test for function main
def test_main():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:28:14.975454
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

# Generated at 2022-06-13 06:28:19.103440
# Unit test for function main
def test_main():
    data = {"name": "foo"}
    module = AnsibleModule(argument_spec=data)
    assert main() == "success"

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:28:24.058549
# Unit test for function main
def test_main():
    'Test module: basic'
    module = AnsibleModule(
        argument_spec={})
    module.exit_json = lambda x:None
    sysvinit = imp.load_source('main', os.path.join(os.path.dirname(__file__), 'main.py'))

# import module snippets
from ansible.module_utils.basic import *
if __name__ == '__main__':
    main()