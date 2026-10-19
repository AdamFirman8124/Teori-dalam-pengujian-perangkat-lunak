

# Generated at 2022-06-13 05:03:20.668467
# Unit test for method get_jobnames of class CronTab
def test_CronTab_get_jobnames():
    tab = CronTab(None, user=None, cron_file=None)
    tab.lines = ['run something\n', '#Ansible: test\n', '#Ansible: test2\n', 'run something else\n']
    result = tab.get_jobnames()
    assert result == ['test', 'test2']


# Generated at 2022-06-13 05:03:26.900279
# Unit test for constructor of class CronTab
def test_CronTab():
    import os
    import tempfile

    (filed, filename) = tempfile.mkstemp(suffix='.cron.tmp', prefix='ansible-test')
    os.close(filed)

    crontab = CronTab(module=None, cron_file=filename)
    assert crontab.cron_file == filename



# Generated at 2022-06-13 05:03:29.988090
# Unit test for method remove_job_file of class CronTab
def test_CronTab_remove_job_file():
    tab = CronTab(None, None, None)
    # No exception should be raised when removing a job file
    tab.remove_job_file()


# Generated at 2022-06-13 05:03:42.354779
# Unit test for method find_job of class CronTab
def test_CronTab_find_job():
    # Create an instance of class CronTab
    crontab = CronTab(None, None)

    # Test find_job with a comment header, exact match and no header
    crontab.lines = ['#Ansible: TestA', '1 1 * * * TestB', '2 2 2 2 TestC']
    assert crontab.find_job('TestA', '1 1 * * * TestA') == ['TestA', '1 1 * * * TestA', True]
    assert crontab.find_job('TestB', '1 1 * * * TestB') == ['TestB', '1 1 * * * TestB']
    assert crontab.find_job('TestC', '2 2 2 2 TestC') == ['', '2 2 2 2 TestC', True]



# Generated at 2022-06-13 05:03:49.823818
# Unit test for method do_add_env of class CronTab
def test_CronTab_do_add_env():
    module = AnsibleModule(
        argument_spec = dict()
    )
    x = CronTab(module, user="root")
    env_name = "TEST_ENV"
    decl = "%s=test" % env_name

    # Test if return value is None when do_add_env is called
    result = x.do_add_env(x.lines, decl)
    assert result is None

    # Test if a value has been added to the list lines
    assert x.lines[0] == decl



# Generated at 2022-06-13 05:03:57.668445
# Unit test for method update_env of class CronTab
def test_CronTab_update_env():
    module = AnsibleModule(
        argument_spec = dict(
            name = dict(required=True),
            cron_file = dict(),
            user = dict(),
            state = dict(default='present', choices=['present', 'absent']),
        ),
        supports_check_mode=True
    )

    ct = CronTab(module, module.params['user'], module.params['cron_file'])
    crons = [c for c in ct.lines if not c.startswith(ct.ansible)]
    envnames = ct.get_envnames()
    if module.params['name'] not in envnames:
        module.fail_json(msg="Environment variable named '%s' not found." % module.params['name'])



# Generated at 2022-06-13 05:04:04.250252
# Unit test for method render of class CronTab
def test_CronTab_render():
    """
    Basic test of CronTab.render method
    """
    ct = CronTab('root')
    ct.add_job(name='foo', job='(cd ~/; do-something)')

    expected = '\n'.join([
        '#Ansible: foo',
        '(cd ~/; do-something)',
    ])
    assert expected == ct.render()

# Generated at 2022-06-13 05:04:05.646280
# Unit test for method do_comment of class CronTab
def test_CronTab_do_comment():
    assert CronTab.do_comment(self, 'name') == "name"

# Generated at 2022-06-13 05:04:18.002484
# Unit test for method remove_env of class CronTab
def test_CronTab_remove_env():
  import os
  import base64
  if os.getuid() != 0:
    print('skipping test as user is not running as root')
    exit(0)
  # set up cron file and read
  fh = tempfile.NamedTemporaryFile(mode='w+b')
  fh.write(to_bytes(base64.b64decode('Y29tbWVudHMKZGVsZXRlX2Vudj0xCmRlbGV0ZV9lbnY9Mg==')))
  fh.flush()
  os.chmod(fh.name, int('0644', 8))
  crontab = CronTab(user='root', cron_file=fh.name)
  crontab.read()
  # test remove_env

# Generated at 2022-06-13 05:04:22.742557
# Unit test for function main
def test_main():
    """
    main function unit test
    :return:
    """
    # Check module args https://docs.ansible.com/ansible/devel/dev_guide/developing_modules_documenting.html#common-module-arguments
    # https://docs.ansible.com/ansible/devel/dev_guide/developing_modules_general.html#module-utilities

# Generated at 2022-06-13 05:05:26.731884
# Unit test for method get_cron_job of class CronTab
def test_CronTab_get_cron_job():
    c = CronTab(None, 'root')
    c.get_cron_job('*/2', '*', '*', '*', '*', '/bin/true', None, False)
    c.get_cron_job('*/2', '*', '*', '*', '*', '/bin/true', None, True)
    c.get_cron_job('*/2', '*', '*', '*', '*', '/bin/true', 'reboots', False)
    c.get_cron_job('*/2', '*', '*', '*', '*', '/bin/true', 'reboots', True)
    c.get_cron_job('*/2', '*', '*', '*', '*', '/bin/true', '@reboot', False)
    c.get_

# Generated at 2022-06-13 05:05:30.151482
# Unit test for method remove_job_file of class CronTab
def test_CronTab_remove_job_file():
    # TODO: write a unit test for method remove_job_file of class CronTab
    pass

# Generated at 2022-06-13 05:05:41.339419
# Unit test for method add_job of class CronTab
def test_CronTab_add_job():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str'),
            special_time=dict(type='str'),
            job=dict(type='str'),
            state=dict(default='present', choices=['present', 'absent', 'latest']),
            user=dict(type='str'),
            cron_file=dict(type='str'),
            minute=dict(type='str'),
            hour=dict(type='str'),
            day=dict(type='str'),
            month=dict(type='str'),
            weekday=dict(type='str'),
            disabled=dict(type='bool'),
            backup=dict(type='bool', default=False),
            backup_name=dict(type='str', default=None)
        ),
        supports_check_mode=True
    )


# Generated at 2022-06-13 05:05:46.863079
# Unit test for method write of class CronTab
def test_CronTab_write():
    cur_user = getpass.getuser()
    t = CronTab(None, user=cur_user)
    t.write('/tmp/test-crontab.txt')
    f = open('/tmp/test-crontab.txt', 'w')
    f.write(t.render())
    f.close()
    os.remove('/tmp/test-crontab.txt')



# Generated at 2022-06-13 05:05:55.452918
# Unit test for method find_env of class CronTab
def test_CronTab_find_env():
    module = AnsibleModule(
        argument_spec = dict(
            name = dict(required=True, type='str'),
        )
    ) 
    name = module.params['name']
    myobject = CronTab(module)
    myresult = myobject.find_env(name)
    mymodule = AnsibleModule(
        argument_spec = dict(
            name = dict(required=True, type='str'),
        ),
        supports_check_mode=True
    )
    if module.check_mode:
        mymodule.exit_json(changed=True)
    else:
        mymodule.exit_json(changed=False, meta=myresult)


# Generated at 2022-06-13 05:06:05.110608
# Unit test for method render of class CronTab

# Generated at 2022-06-13 05:06:18.151759
# Unit test for method remove_env of class CronTab

# Generated at 2022-06-13 05:06:27.213414
# Unit test for method update_job of class CronTab
def test_CronTab_update_job():
    class ModuleStub:
        pass

    module = ModuleStub()

    class CronTabStub:
        def find_job(self, name, job=None):
            if name == 'foo':
                return ['#Ansible: foo', '* * * * * echo foo']
            elif name == 'bar':
                return []
            else:
                assert False, 'Unexpected call to find_job: %s %s' % (name, job)

        def do_remove_job(self, lines, comment, job):
            if comment == '#Ansible: foo':
                return None
            else:
                assert False, 'Unexpected call to do_remove_job: %s %s' % (comment, job)


# Generated at 2022-06-13 05:06:34.158048
# Unit test for method do_remove_job of class CronTab
def test_CronTab_do_remove_job():
    ct = CronTab(module=MagicMock(), user=None, cron_file=None)
    lines = MagicMock()
    comment = MagicMock()
    job = MagicMock()
    ct.do_remove_job(lines, comment, job)
    with pytest.raises(SystemExit):
        ct.do_remove_job(lines, comment, job)


# Generated at 2022-06-13 05:06:37.850251
# Unit test for method update_job of class CronTab
def test_CronTab_update_job():
    module = MockAnsibleModule()
    ct = CronTab(module, user='testuser')
    assert ct.update_job('testname', 'testjob') == True
    assert ct.update_job('testname', 'testjob') == False


# Generated at 2022-06-13 05:07:56.610399
# Unit test for method is_empty of class CronTab
def test_CronTab_is_empty():
    ct = CronTab('root', cron_file = 'test.txt')

    ct.lines = []
    if ct.is_empty() != True:
        exit(1)

    ct.lines = ['\n']
    if ct.is_empty() != True:
        exit(2)

    ct.lines = ['#Ansible: test_CronTab_is_empty', '* * * * * test_CronTab_is_empty']
    if ct.is_empty() != False:
        exit(3)


# Generated at 2022-06-13 05:08:03.302532
# Unit test for method find_env of class CronTab
def test_CronTab_find_env():
    # Method arguments
    name = name
    decl = decl
    self = CronTab
    # Add any additional arguments
    # No additional arguments
    # Build the expected value
    # Build the actual value
    cron = CronTab(None)
    cron.add_env("frank=monster")
    cron.add_env("george=animal")
    cron.add_env("bob=animal")
    cron.add_env("fred=monster")
    cron.add_env("george=human")
    cron.add_env("alice=person")
    cron.add_env("fred=human")
    cron.add_env("bob=monster")
    actual = cron.find_env("bob")

    # The assertion
    assert actual == expected

# Generated at 2022-06-13 05:08:09.264542
# Unit test for method get_envnames of class CronTab
def test_CronTab_get_envnames():
    # Create a new instance of the class under test
    c = CronTab()
    c.lines = ['#Ansible: foo']

    # Insert code here to set the appropriate object attributes
    # and/or invoke the class's lifecycle callbacks.

    # Run the method under test
    result = c.get_envnames()

    # Use this syntax for asserting equality
    assert result == []


# Generated at 2022-06-13 05:08:18.151496
# Unit test for method do_remove_env of class CronTab
def test_CronTab_do_remove_env():
    c = CronTab(None)

    # test for deleting env
    c.lines = [
            'HOME = /home/abc',
            'SHELL=/bin/bash',
            'PATH =/bin:/usr/bin',
            '* */2 * * *  /home/abc/cron_job.sh'
        ]

    c.do_remove_env(c.lines, 'PATH')

    assert(c.lines == ['HOME = /home/abc', 'SHELL=/bin/bash', '* */2 * * *  /home/abc/cron_job.sh'])

    # test for deleting non existing env
    c.do_remove_env(c.lines, 'LANG')


# Generated at 2022-06-13 05:08:27.060830
# Unit test for method get_jobnames of class CronTab
def test_CronTab_get_jobnames():
    ct = CronTab(None)

    ct.lines = ['#Ansible: junk', '* * * * * /bin/false', '', '#Ansible: foobar']
    assert ct.get_jobnames() == ['junk', 'foobar']

    ct.lines = ['#Ansible: junk', '', '', '#Ansible: foobar']
    assert ct.get_jobnames() == ['junk', 'foobar']

    ct.lines = []
    assert ct.get_jobnames() == []



# Generated at 2022-06-13 05:08:31.906472
# Unit test for method remove_job of class CronTab
def test_CronTab_remove_job():

	# A rough test for remove_job for now
	cron = CronTab(module=None, user=None, cron_file=None)

	cron.lines = ['#Ansible: test_job1', '0,30 * * * * test_job1 command', '#Ansible: test_job2', '0,30 * * * * test_job2 command']
	cron.remove_job('test_job2')
	assert cron.lines == ['#Ansible: test_job1', '0,30 * * * * test_job1 command']


# Generated at 2022-06-13 05:08:43.837007
# Unit test for method write of class CronTab
def test_CronTab_write():
    class MockArgs(object):
        def __init__(self, **kwargs):
            self.user = kwargs.get('user')
            self.cron_file = kwargs.get('cron_file')
            self.special = kwargs.get('special')
            self.minute = kwargs.get('minute')
            self.hour = kwargs.get('hour')
            self.day = kwargs.get('day')
            self.month = kwargs.get('month')
            self.weekday = kwargs.get('weekday')
            self.job = kwargs.get('job')
            self.state = kwargs.get('state')
            self.disabled = kwargs.get('disabled')
            self.backup = kwargs.get('backup')


# Generated at 2022-06-13 05:08:52.480446
# Unit test for method remove_env of class CronTab
def test_CronTab_remove_env():
    def do_remove_env_default(self,lines,decl):
        return None

    # Note: this class only has one method 'remove_env'
    # All other methods are mocked out.
    class MockModule(object):
        def __init__(self):
            self.params = {
                           'name': 'foo',
                           'minute': '0',
                           'hour': '*',
                           'day': '*',
                           'month': '*',
                           'weekday': '*',
                           'job': '/path/to/job.sh',
                           'special_time': '',
                           'disabled': 'no',
                           'variable': '',
                           'insertafter': '',
                           'insertbefore': '',
                           'state': 'present',
                           }



# Generated at 2022-06-13 05:09:00.206886
# Unit test for method get_cron_job of class CronTab
def test_CronTab_get_cron_job():
    ct = CronTab(None)
    if ct.get_cron_job('0', '1', '*', '*', '*', 'ls', None, False) != '0 1 * * * ls':
        return False
    if ct.get_cron_job('0', '1', '*', '*', '*', 'ls', None, True) != '#0 1 * * * ls':
        return False
    if ct.get_cron_job('0', '1', '*', '*', '*', 'ls', 'reboot', False) != '@reboot ls':
        return False
    if ct.get_cron_job('0', '1', '*', '*', '*', 'ls', 'reboot', True) != '#@reboot ls':
        return False

# Generated at 2022-06-13 05:09:05.104576
# Unit test for method do_remove_job of class CronTab
def test_CronTab_do_remove_job():
    args = dict(
        lines = "",
        comment = "",
        job = ""
    )

    ct = CronTab(args)
    ct.do_remove_job(args['lines'], args['comment'], args['job'])

# Generated at 2022-06-13 05:11:39.868493
# Unit test for function main
def test_main():
    """ Test module """
#    import ansible.modules

# Generated at 2022-06-13 05:11:52.831512
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes

    class AnsibleExitJson(Exception):
        """Exception class to be raised by module.exit_json and caught to exit from module"""
        pass

    class AnsibleFailJson(Exception):
        """Exception class to be raised by module.fail_json and caught by the test case"""
        pass

    def exit_json(*args, **kwargs):
        """function to patch over exit_json; package return data into an exception"""
        if 'changed' not in kwargs:
            kwargs['changed'] = False
        raise AnsibleExitJson(kwargs)

    def fail_json(*args, **kwargs):
        """function to patch over fail_json; package return data into an exception"""
        kwargs['failed']

# Generated at 2022-06-13 05:11:59.569402
# Unit test for method remove_job_file of class CronTab
def test_CronTab_remove_job_file():
    import os
    import tempfile
    fd, path = tempfile.mkstemp()
    fileh = os.fdopen(fd, 'wb')
    fileh.close()
    crontab = CronTab(user='root', cron_file=path)
    crontab.cron_file = path
    try:
        crontab.remove_job_file()
        # If we get here, there was no exception
        assert True
    except CronTabError:
        assert False
    finally:
        os.unlink(path)



# Generated at 2022-06-13 05:12:03.167554
# Unit test for method do_remove_job of class CronTab
def test_CronTab_do_remove_job():
    import doctest
    failure_count, test_count = doctest.testmod(verbose=True)
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec=dict())
    if failure_count:
        module.fail_json(msg='%s of %s doxygen tests failed' % (failure_count, test_count))



# Generated at 2022-06-13 05:12:13.682490
# Unit test for method add_env of class CronTab

# Generated at 2022-06-13 05:12:15.934356
# Unit test for method do_add_env of class CronTab
def test_CronTab_do_add_env():
    crontab_writer = CronTab(module, user, cron_file)
    crontab_writer.do_add_env(lines, decl)


# Generated at 2022-06-13 05:12:18.643701
# Unit test for method remove_job_file of class CronTab
def test_CronTab_remove_job_file():
    fake_module = type('HASoH', (object,), dict(exit_json=lambda k,v: None, fail_json=lambda k,v: None))
    c = CronTab(fake_module)
    assert c.remove_job_file() == False


# Generated at 2022-06-13 05:12:29.117333
# Unit test for function main
def test_main():
    # Mock of arguments
    class MockArgs(object):
        def __init__(self):
            self.name = None
            self.user = None
            self.job = None
            self.cron_file = None
            self.state = 'present'
            self.backup = False
            self.minute = '*'
            self.hour = '*'
            self.day = '*'
            self.month = '*'
            self.weekday = '*'
            self.special_time = None
            self.disabled = False
            self.env = False
            self.insertafter = None
            self.insertbefore = None
            
    # Create the mock
    mock_args = MockArgs()
    mock_args.name = 'test'

    # Run the function with the mock
    main()
