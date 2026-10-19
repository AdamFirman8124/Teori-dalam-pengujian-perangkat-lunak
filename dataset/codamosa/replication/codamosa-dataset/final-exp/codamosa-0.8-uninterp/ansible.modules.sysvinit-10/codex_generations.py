

# Generated at 2022-06-13 06:21:33.123733
# Unit test for function main
def test_main():
    ansible_module_main(YAML_SYNTAX, YAML_SIDE_EFFECTS, YAML_DRY_RUN, YAML_CHECK_MODE, YAML_ARGS )

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:21:44.952823
# Unit test for function main
def test_main():
    """Unit test for function main."""
    # We have 4 tests here:
    # 1. Name None
    # 2. Name not found
    # 3. Module.params['state'] is not 'stopped', 'started' or 'restarted'
    # 4. All tests passed
    #
    # We try to test the function itself and not the functions it calls. We
    # mock all of these functions.
    #
    # Function we try to mock:
    # module.run_command


# Generated at 2022-06-13 06:21:47.672518
# Unit test for function main

# Generated at 2022-06-13 06:21:59.426390
# Unit test for function main
def test_main():

    # Test command parameter to be able to run the module directly from command line
    if __name__ == "__main__":

        # Set up Argument parser
        parser = argparse.ArgumentParser(description='ansible module for sysvinit')
        parser.add_argument('--name', required=True, default=None)
        parser.add_argument('--state', default=None)
        parser.add_argument('--enabled', default=None)
        parser.add_argument('--sleep', default=None)
        parser.add_argument('--pattern', default=None)
        parser.add_argument('--arguments', default=None)
        parser.add_argument('--runlevels', default=None)
        parser.add_argument('--daemonize', default=None)

        # Get module parameters
        args = parser.parse_args

# Generated at 2022-06-13 06:22:03.871949
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    import os
    import sys
    this_dir = os.path.dirname(os.path.realpath(__file__))
    name = 'sysvinit'
    args = ['-c', '-m', this_dir + os.sep + name + '.py', '-a', 'name=apache2', '-a', 'state=started']
    args.append('-a')
    args.append('sleep=1')
    args.append('-a')
    args.append('runlevels=["1", "2", "3", "4", "5"]')
    args.append('-a')
    args.append('enabled=yes')
    module = AnsibleModule(argument_spec={})

# Generated at 2022-06-13 06:22:16.426948
# Unit test for function main
def test_main():
    import json
    import sys
    class AnsibleModuleFake:
        _ansible_module_generated_id = "something"
        _ansible_module_generated_version = "2.4"
        _ansible_module_generated_version_tuple = tuple([int(x) for x in "2.4".split(".")])
        __name__ = "AnsibleModule"

# Generated at 2022-06-13 06:22:23.903318
# Unit test for function main
def test_main():
    old_run_command = AnsibleModule.run_command

    ###########################################################################
    # Mocks
    def run_command(self, args, check_rc=True, close_fds=True, executable=None, data=None, binary_data=False):
        if executable:
            if executable.endswith('update-rc.d'):
                return (0, "", "")
            elif executable.endswith('chkconfig'):
                return (0, "", "")
            elif executable.endswith('service'):
                return (0, "", "")
            elif executable.endswith('insserv'):
                return (0, "", "")
        return (0, "", "")
    AnsibleModule.run_command = run_command


# Generated at 2022-06-13 06:22:34.070453
# Unit test for function main
def test_main():
    module = AnsibleModule(argument_spec={'name': {'type': 'str', 'required': True}, 'state': {'choices': ['started', 'stopped', 'restarted', 'reloaded'], 'type': 'str'}, 'enabled': {'type': 'bool'}, 'sleep': {'type': 'int', 'default': 1}, 'pattern': {'type': 'str'}, 'arguments': {'type': 'str', 'aliases': ['args']}, 'runlevels': {'type': 'list', 'elements': 'str'}, 'daemonize': {'type': 'bool', 'default': False}}, required_one_of=[['state', 'enabled']], supports_check_mode=True)
    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:22:41.054578
# Unit test for function main
def test_main():
    f = open('test_sysvinit.py', 'a')
    f.write('def main():')
    f.close()

# import module snippets
from ansible.module_utils.basic import *

# import unit test modules
import sysvinit_common_tests
from sysvinit_common_tests import *

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:22:51.648420
# Unit test for function main
def test_main():
  from ansible.module_utils.basic import AnsibleModule
  from ansible.module_utils.service import sysv_is_enabled, get_sysv_script, sysv_exists, fail_if_missing, get_ps, daemonize

# Generated at 2022-06-13 06:23:44.100146
# Unit test for function main
def test_main():
    print('Test suite for function main')

    args = dict(
        name='apache2',
        state='stopped',
        enabled=True,
        sleep=1,
        pattern='',
        arguments='',
        runlevels=['3', '5', '2'],
    )

    print(args)


# Generated at 2022-06-13 06:23:54.212171
# Unit test for function main
def test_main():

    class TestModule(object):
        def __init__(self, **kwargs):
            self.params = kwargs
            self.fail_json = kwargs['fail_json']
            self.run_command = kwargs['run_command']

        def get_bin_path(self, **kwargs):
            return get_bin_path(self, **kwargs)

    # Unit test function main
    # TODO: Figure out why it is not finding the binaries.
    def get_bin_path(self, **kwargs):
        # Does not actually test
        return 'fakebinary'

    def fail_json(self, **kwargs):
        # May not actually test
        print("Failing with: {0}".format(kwargs))

    # Cannot test:
    # sysv_is_enabled
    # get

# Generated at 2022-06-13 06:23:55.306803
# Unit test for function main
def test_main():
    pass


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:24:02.034270
# Unit test for function main
def test_main():

    action = 'stop'

    module_args = {
        u'name': u'aide',
        u'state': action,
        u'pattern': None,
        u'enabled': u'yes',
        u'arguments': None,
        u'daemonize': False
    }

    from ansible.module_utils import basic 
    from ansible.module_utils._text import to_bytes

    # Mock what basic.py does inside a module.
    old_basic_ANSIBLE_ARGS = basic.ANSIBLE_ARGS
    basic.ANSIBLE_ARGS = to_bytes(u'ansible')
    basic._ANSIBLE_ARGS = to_bytes(u'ansible')
    module = AnsibleModule(**module_args)
    basic.ANSIBLE_ARGS = old_basic_ANSIBLE_

# Generated at 2022-06-13 06:24:11.236890
# Unit test for function main
def test_main():
    schema = 'ansible.local.sysvinit'
    model = 'sysvinit.yml'
    mock_module = AnsibleModule(argument_spec={})
    mock_module.params = {
            'name': 'sysvinit.yml',
            'state': 'started',
            'enabled': 'yes',
            'sleep': '1',
            'pattern': 'sysvinit.yml',
            'arguments': 'sysvinit.yml',
            'runlevels': ['3'],
            'daemonize': 'False',
    }
    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:24:16.677089
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
    module.run_command = MagicMock(return_value=(0, '', ''))
   

# Generated at 2022-06-13 06:24:24.890322
# Unit test for function main
def test_main():
    mock_run_command = MagicMock(return_value=(0, "", ""))
    mock_get_bin_path = MagicMock(return_value="/bin")

    module_args = {
      "name": "apache",
      "state": "started",
      "enabled": True,
      "sleep": "1",
      "pattern": "apache",
      "arguments": "",
      "runlevels": [
        "3",
        "5"
      ],
      "daemonize": False
    }


# Generated at 2022-06-13 06:24:32.092235
# Unit test for function main
def test_main():

    class Options(object):
        def __init__(self):
            self.name = 'apache2'
            self.state = 'started'
            self.enabled = 'yes'
            self.runlevels = [3,5]

    module = Options()

    if main():
        exit(0)
    else:
        exit(1)

if __name__ == '__main__':

    # test_main()

    main()

# Generated at 2022-06-13 06:24:39.163712
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

# Generated at 2022-06-13 06:24:51.151454
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

# Generated at 2022-06-13 06:26:54.127608
# Unit test for function main
def test_main():
    # Mock module
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

    # Mock name that exists
    name = 'fakeService1'
    script

# Generated at 2022-06-13 06:27:02.238154
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

# Generated at 2022-06-13 06:27:05.238966
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec=dict())
    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:27:16.178087
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.service import sysv_is_enabled, get_sysv_script, sysv_exists, fail_if_missing, get_ps

# Generated at 2022-06-13 06:27:20.279867
# Unit test for function main
def test_main():
    """
    Test that main() returns the correct JSON.
    """
    from ansible.module_utils import basic
    import inspect

# Generated at 2022-06-13 06:27:26.140680
# Unit test for function main
def test_main():
    # This is just a test description to simulate arguments_spec
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

    name = "service002"
   

# Generated at 2022-06-13 06:27:27.816089
# Unit test for function main
def test_main():
    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:27:36.351397
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule

# Generated at 2022-06-13 06:27:51.962149
# Unit test for function main
def test_main():
    test_spec = dict(
        name=dict(required=True, type='str', aliases=['service']),
        state=dict(choices=['started', 'stopped', 'restarted', 'reloaded'], type='str'),
        enabled=dict(type='bool'),
        sleep=dict(type='int', default=1),
        pattern=dict(type='str'),
        arguments=dict(type='str', aliases=['args']),
        runlevels=dict(type='list', elements='str'),
        daemonize=dict(type='bool', default=False),
    )

    test_module = AnsibleModule(
        argument_spec=test_spec,
        supports_check_mode=True,
        required_one_of=[['state', 'enabled']],
    )
    test_module.exit_json = exit_

# Generated at 2022-06-13 06:27:56.601048
# Unit test for function main
def test_main():
    module = AnsibleModule({"name":"apache","pattern":"apache"})
    result = main()
    assert result['pattern'] is not None

# import module snippets
#from ansible.module_utils.basic import *
#if __name__ == '__main__':
#    main()