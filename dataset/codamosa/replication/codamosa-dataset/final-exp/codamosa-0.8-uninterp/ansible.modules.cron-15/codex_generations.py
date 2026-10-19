

# Generated at 2022-06-13 05:03:18.712261
# Unit test for method find_job of class CronTab
def test_CronTab_find_job():
    ct = CronTab(None, user='jdoe')
    # Comment but no job
    assert ct.find_job('job1') == []

    # No comment, Job
    ct.lines.append('* * * * * command1')
    assert ct.find_job('job1') == []

    # Comment, no job
    ct.lines.insert(0, ct.do_comment('job1'))
    assert ct.find_job('job1') == []

    # Comment, Job
    ct.lines.append('* * * * * command1')
    assert ct.find_job('job1') == ['job1', '* * * * * command1']

    # No comment, no job
    ct.lines = []
    assert ct.find_job('job1')

# Generated at 2022-06-13 05:03:24.762900
# Unit test for method render of class CronTab
def test_CronTab_render():
    c = CronTab(None)
    c.cron_cmd = 'crontab'
    c.lines = ['#Ansible: foo', 'bar', '#Ansible: meh', 'baz']
    assert c.render() == '#Ansible: foo\nbar\n#Ansible: meh\nbaz'
    c.lines = ['#Ansible: foo', 'bar']
    assert c.render() == '#Ansible: foo\nbar'
    c.lines = ['#Ansible: foo']
    assert c.render() == '#Ansible: foo'



# Generated at 2022-06-13 05:03:25.394366
# Unit test for method get_cron_job of class CronTab
def test_CronTab_get_cron_job():
    ct = CronTab(None)


# Generated at 2022-06-13 05:03:35.746610
# Unit test for method get_envnames of class CronTab
def test_CronTab_get_envnames():
    module = MagicMock()
    module.get_bin_path = MagicMock(return_value = '/path/to/crontab')
    module.run_command = MagicMock(return_value = (0,'#Ansible: a\n#Ansible: b\n\n#Ansible: c'))
    module.selinux_enabled = MagicMock(return_value = False)
    module.set_default_selinux_context = MagicMock(return_value = True)
    module.fail_json = MagicMock(return_value = True)
    crontab = CronTab(module, user = None, cron_file = None)

    assert crontab.get_envnames() == ['a', 'b', 'c']

# Generated at 2022-06-13 05:03:48.437858
# Unit test for method render of class CronTab
def test_CronTab_render():
    ct = CronTab(user='root')

    ct.add_job('test1', '* * * * * /bin/foo')
    result = ct.render()
    assert result == '#Ansible: test1\n* * * * * /bin/foo\n'

    assert ct.remove_job('test1') == True
    result = ct.render()
    assert result == ''

    ct.add_job('test1', '* * * * * /bin/foo')
    ct.add_job('test2', '* * * * * /bin/foo')
    result = ct.render()

# Generated at 2022-06-13 05:03:57.602395
# Unit test for method is_empty of class CronTab
def test_CronTab_is_empty():
	print("Testing is_empty")
	cron_empty = CronTab(user=None, cron_file=None)
	assert cron_empty.is_empty() == True, "Test case is_empty failed"
	cron_job = CronTab(user=None, cron_file=None)
	cron_job.lines = [' ',' ',' ']
	assert cron_job.is_empty() == False, "Test case is_empty failed"
	cron_job.lines = [' ',' ','job']
	assert cron_job.is_empty() == False, "Test case is_empty failed"
	cron_job.lines = ['job',' ','job']
	assert cron_job.is_empty() == False, "Test case is_empty failed"


# Generated at 2022-06-13 05:04:02.341711
# Unit test for method do_comment of class CronTab
def test_CronTab_do_comment():
    # Arrange
    crontab = CronTab(None)

    # Act
    result = crontab.do_comment('name')

    # Assert
    assert result == '#Ansible: name'



# Generated at 2022-06-13 05:04:12.037287
# Unit test for function main

# Generated at 2022-06-13 05:04:19.858297
# Unit test for method update_env of class CronTab
def test_CronTab_update_env():
    # create a dummy module and an instance of CronTab
    module = AnsibleModule(argument_spec=dict())
    ct = CronTab(module, user='testuser')
    ct.lines = [
                '# comment',
                '#Ansible: testjob1',
                '* * * * * echo "this is a test"',
                '#Ansible: testjob2',
                '* * * * * echo "this is a test"',
                '#Ansible: testjob3',
                '* * * * * echo "this is a test"',
               ]

    # make sure the method fails when requested variable isn't present
    module.fail_json = MagicMock()
    result = ct.update_env('TESTENV', 'TESTENV=testvalue')
    assert result is False

# Generated at 2022-06-13 05:04:25.153823
# Unit test for method find_job of class CronTab
def test_CronTab_find_job():
    test_obj = CronTab(None)
    test_obj.lines = []
    name = "test_name"
    job = "test_job"
    test_obj.lines.append("#Ansible: " + name)
    test_obj.lines.append(job)
    test_obj.lines.append("")
    assert test_obj.find_job(name) == ["#Ansible: " + name, job]


# Generated at 2022-06-13 05:05:50.058995
# Unit test for method write of class CronTab
def test_CronTab_write():
    cron = CronTab(module, user=None, cron_file='cronfile.txt')
    cron.write(backup_file=None)


# Generated at 2022-06-13 05:05:53.884852
# Unit test for method get_envnames of class CronTab
def test_CronTab_get_envnames():
    crontab = CronTab(None, user="mark")
    crontab.lines = ["LOGNAME=mark", "SHELL=/bin/bash", "HOME=/home/mark"]
    crontab.cron_file = "/etc/cron.d/mycron"
    assert crontab.get_envnames() == ['LOGNAME', 'SHELL', 'HOME']



# Generated at 2022-06-13 05:06:04.187166
# Unit test for method get_envnames of class CronTab
def test_CronTab_get_envnames():
    if not pythonbin_subject:
        raise Exception(
            'Python binary {0} does not exist.'.format(pythonbin_subject))
    if not test_module_path:
        raise Exception('Test module {0} does not exist.'.format(test_module_path))
    command = [pythonbin_subject, test_module_path, 'crontab', 'get_envnames']
    p = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    p.wait()
    (stdout, stderr) = p.communicate()

# Generated at 2022-06-13 05:06:09.162902
# Unit test for method remove_env of class CronTab
def test_CronTab_remove_env():
    module = AnsibleModule(
        argument_spec = dict()
    )
    ct = CronTab(module)

    assert ct.remove_env('TEST') is False, "The remove_env() method return wrong value"


# Generated at 2022-06-13 05:06:16.677327
# Unit test for method get_cron_job of class CronTab
def test_CronTab_get_cron_job():
    class module_mock:
        def get_bin_path(self, arg, required):
            return True

    cron = CronTab(module_mock, user=None, cron_file=None)
    assert cron.get_cron_job("*", "*", "*", "*", "*", "/bin/false", "", False) == "* * * * * /bin/false"


# Generated at 2022-06-13 05:06:18.476545
# Unit test for method is_empty of class CronTab
def test_CronTab_is_empty():
    m = MagicMock()
    m.get_bin_path.return_value = '/usr/bin/crontab'
    c = CronTab(m)
    assert c.is_empty()




# Generated at 2022-06-13 05:06:20.327871
# Unit test for method find_job of class CronTab
def test_CronTab_find_job():
    ct = CronTab(None)
    assert [] == ct.find_job('test_name')



# Generated at 2022-06-13 05:06:28.556347
# Unit test for method remove_job of class CronTab
def test_CronTab_remove_job():
    cron_file = to_bytes('/etc/cron.d/ansible-cron.file', errors='surrogate_or_strict')
    module = MagicMock(spec=AnsibleModule, type='AnsibleModule')
    cron = CronTab(module=module, cron_file='ansible-cron.file')
    cron.lines = [
        b'#Ansible: test_job_1',
        b'* * * * * rm /tmp/test_job_1',
        b'#Ansible: test_job_2',
        b'* * * * * rm /tmp/test_job_2',
        b'#Ansible: test_job_3',
        b'* * * * * rm /tmp/test_job_3'
    ]
   

# Generated at 2022-06-13 05:06:38.968777
# Unit test for method update_env of class CronTab
def test_CronTab_update_env():
    # setup
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            user=dict(default=None),
            cron_file=dict(default=None),
            decl=dict(required=True),
            insertafter=dict(default=None),
            insertbefore=dict(default=None),
            state=dict(choices=['set', 'unset'], default='set')
        ),
        supports_check_mode=True
    )
    name = module.params['name']
    user = module.params['user']
    cron_file = module.params['cron_file']
    decl = module.params['decl']
    insertafter = module.params['insertafter']
    insertbefore = module.params['insertbefore']

# Generated at 2022-06-13 05:06:44.612927
# Unit test for method do_remove_env of class CronTab
def test_CronTab_do_remove_env():
    '''Test method in class CronTab'''

    test_instance = CronTab()

    # Invalid input type
    with pytest.raises(TypeError):
        assert test_instance.do_remove_env(1, 2)

# Generated at 2022-06-13 05:09:56.964495
# Unit test for method update_job of class CronTab
def test_CronTab_update_job():
    module = AnsibleModule(argument_spec={})
    x = CronTab(module, user=None, cron_file=None)
    x.lines = []
    x.lines.append('* * * * * echo "Hello World"')
    assert x.update_job("test_jobname", "test_jobcontent") == False
    assert x.lines == ['* * * * * echo "Hello World"']
    assert x.is_empty() == False


# Generated at 2022-06-13 05:09:59.483847
# Unit test for method remove_job of class CronTab
def test_CronTab_remove_job():
    c = CronTab('/bin/echo', 'root', '/etc/cron.d/test')
    assert '#Ansible: test' in c.remove_job('test')

# Generated at 2022-06-13 05:10:06.848415
# Unit test for method is_empty of class CronTab
def test_CronTab_is_empty():
    from ansible.module_utils.basic import AnsibleModule
    cron = CronTab(AnsibleModule, cron_file='crontab')
    cron.lines = ['#Ansible: foo', '1', '2', '3', '4', '5', 'foo', '#Ansible: bar']
    assert cron.is_empty() == False
    cron.lines = ['#Ansible: ', '1', '2', '3', '4', '5', 'foo', '#Ansible: ', '1', '2', '3', '4', '5', 'foo']
    assert cron.is_empty() == True
    cron.lines = None
    assert cron.is_empty() == True


# Generated at 2022-06-13 05:10:07.812070
# Unit test for method read of class CronTab
def test_CronTab_read():
    pass


# Generated at 2022-06-13 05:10:16.739418
# Unit test for method get_jobnames of class CronTab
def test_CronTab_get_jobnames():
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode=True
    )

    if not HAS_CRONITER:
        module.fail_json(msg=missing_required_lib('python-croniter'), exception=CRONITER_IMP_ERR)

    c = CronTab(module)


# Generated at 2022-06-13 05:10:20.443630
# Unit test for method remove_job_file of class CronTab
def test_CronTab_remove_job_file():
    cron_file_path = ''
    obj = CronTab(module=MockModule())
    try:
        obj.remove_job_file()
    except SystemExit:
        pass
    assert True


# Generated at 2022-06-13 05:10:32.509251
# Unit test for method update_env of class CronTab
def test_CronTab_update_env():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    if not HAS_CRONTAB:
        module.fail_json(msg='The python module crontab is required')

    content = '''#Ansible: job1
* * * * * root echo job1

#Ansible: job2
* * * * * root echo job2

#Ansible: job3
* * * * * root echo job3'''

    c = CronTab(module, user='root', cron_file='test_update_env', content=content)

    env = {}
    env['name'] = 'TEST'
    env['value'] = 'test'


# Generated at 2022-06-13 05:10:37.122744
# Unit test for method remove_job of class CronTab
def test_CronTab_remove_job():
  cron_tab = CronTab(module, cron_file='test_cron_file')
  assert(cron_tab.remove_job('test_job') is None)


# Generated at 2022-06-13 05:10:42.730851
# Unit test for method remove_job_file of class CronTab
def test_CronTab_remove_job_file():
    # Set up
    user = 'root'
    cron_file = '/etc/cron.d/test_cron.d'
    c = CronTab(user, cron_file)

    # Test remove_job_file method
    c.remove_job_file()


# Generated at 2022-06-13 05:10:45.379919
# Unit test for method remove_job_file of class CronTab
def test_CronTab_remove_job_file():
    """
    Unit test for method CronTab::remove_job_file of class CronTab
    """
    # FIXME:
    pass
