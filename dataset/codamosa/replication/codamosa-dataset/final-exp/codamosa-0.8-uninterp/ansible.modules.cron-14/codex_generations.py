

# Generated at 2022-06-13 05:03:09.811904
# Unit test for method find_env of class CronTab
def test_CronTab_find_env():
  assert 1 == 1


# Generated at 2022-06-13 05:03:22.562177
# Unit test for method is_empty of class CronTab
def test_CronTab_is_empty():
    cron = CronTab(None, user=None, cron_file=None)
    cron.lines = []
    assert cron.is_empty()
    cron.lines = ['']
    assert cron.is_empty()
    cron.lines = ['# foo']
    assert not cron.is_empty()
    cron.lines = ['', '# foo']
    assert not cron.is_empty()
    cron.lines = ['# foo', '']
    assert cron.is_empty()
    cron.lines = ['', '', '# foo']
    assert cron.is_empty()
    cron.lines = ['', '# foo', '']
    assert not cron.is_empty()
    cron.lines = ['', '', '# foo', '']

# Generated at 2022-06-13 05:03:33.982940
# Unit test for method get_cron_job of class CronTab
def test_CronTab_get_cron_job():
    class Module(object):
        pass
    module = Module()
    cron_tab = CronTab(module)

    assert cron_tab.get_cron_job(minute='*', hour='*', day='*', month='*', weekday='*', job='ansible-thing do something', special=None, disabled=True) == "#* * * * * ansible-thing do something"
    assert cron_tab.get_cron_job(minute='*', hour='*', day='*', month='*', weekday='*', job='ansible-thing do something', special=None, disabled=False) == "* * * * * ansible-thing do something"

# Generated at 2022-06-13 05:03:38.322044
# Unit test for method get_jobnames of class CronTab
def test_CronTab_get_jobnames():
    assert CronTab.get_jobnames(['#Ansible: hola', '* * * * * /usr/bin/command']) == ['hola']

# Generated at 2022-06-13 05:03:49.998600
# Unit test for method is_empty of class CronTab
def test_CronTab_is_empty():
    class MockModule:
        pass

    module = MockModule()

    tab = CronTab(module)
    assert tab.is_empty() == True

    lines = ["* * * * * foo", "#Ansible: test1", "#Ansible: test2", "* * * * * bar", "", "#Ansible: test3"]
    tab.lines = lines
    assert tab.is_empty() == False

    lines = ["* * * * * foo", "#Ansible: test1", "#Ansible: test2", "* * * * * bar", "    #Ansible: test3"]
    tab.lines = lines
    assert tab.is_empty() == False

    lines = ["#Ansible: test1", "", "", "    #Ansible: test2"]
    tab.lines = lines
   

# Generated at 2022-06-13 05:03:54.094192
# Unit test for method write of class CronTab
def test_CronTab_write():
    wrong_instance = pwd.getpwnam('root')[2]
    wrong_instance.write(path='/home/test/cronjob', backup_file=None)

    instance = CronTab(module='', user='', cron_file='')
    assert isinstance(instance, CronTab)
    instance.write(backup_file=None)

# Generated at 2022-06-13 05:04:05.521361
# Unit test for constructor of class CronTab
def test_CronTab():
    """
    >>> c = CronTab(None)
    >>> c.user
    >>> c.cron_file
    >>> c.lines
    ''''
    >>> c = CronTab(None, 'dummyuser')
    >>> c.user
    'dummyuser'
    >>> c.cron_file
    >>> c.lines
    ''''
    >>> c = CronTab(None, 'dummyuser', '/etc/cron.d/dummycron')
    >>> c.user
    'dummyuser'
    >>> c.cron_file
    '/etc/cron.d/dummycron'
    >>> c.lines
    ''''
    """
    pass


# Generated at 2022-06-13 05:04:15.573713
# Unit test for method write of class CronTab
def test_CronTab_write():
    class MockModule(object):
        def __init__(self):
            self.params = dict()
            self.params['backup'] = True

        def fail_json(self, *args, **kwargs):
            raise Exception('fail_json')

        def get_bin_path(self, *args, **kwargs):
            return '/usr/bin/crontab'

        def selinux_enabled(self):
            return False

        def set_default_selinux_context(self, *args, **kwargs):
            pass

        def run_command(self, *args, **kwargs):
            return (0, '', '')

    mock_module = MockModule()
    cron_tab = CronTab(mock_module, user=None)

# Generated at 2022-06-13 05:04:19.175265
# Unit test for method is_empty of class CronTab
def test_CronTab_is_empty():
    module = AnsibleModule(
        argument_spec = dict()
    )
    module.params = {}
    cron = CronTab(module)
    cron.lines = []

    assert cron.is_empty() == True

    cron.lines = ['#Ansible: test']
    assert cron.is_empty() == False


# Generated at 2022-06-13 05:04:23.651307
# Unit test for function main

# Generated at 2022-06-13 05:05:23.300683
# Unit test for method get_envnames of class CronTab
def test_CronTab_get_envnames():
    module = AnsibleModule(argument_spec={})
    module.params['name'] = "HOME"
    module.params['value'] = "/home/testuser"
    module.params['state'] = "present"

    cron_tab = CronTab(module, 'testuser', '/etc/cron.d/test_cron_tab')

    cron_tab.add_env("%s=%s" % (module.params['name'], module.params['value']))

    if "HOME" not in cron_tab.get_envnames():
        raise Exception("Failed to find environment variable 'HOME'")

    # Success
    module.exit_json(changed=False)



# Generated at 2022-06-13 05:05:32.360133
# Unit test for method update_job of class CronTab
def test_CronTab_update_job():
    # Setup
    ct = CronTab(
        module=dict(),
        user='root',
        cron_file=''
    )
    name = 'cron_test'
    job = 'echo "Test Cron Job" >> /tmp/cron.test'

    # Expected Result
    should_result = False

    # Creating a parameter for method to be tested
    args = [name, job]

    # Recording and Asserting Results
    actual_result = ct.update_job(*args)
    assert actual_result == should_result


# Generated at 2022-06-13 05:05:43.747732
# Unit test for method get_envnames of class CronTab
def test_CronTab_get_envnames():
    class MockModule(object):
        def __init__(self):
            self.params = {}
            self.result = {}

    class MockOS(object):
        def __init__(self, uid):
            self.uid = uid

        def getuid(self):
            return self.uid

    c = CronTab(MockModule())

    c.lines = []
    assert c.get_envnames() == []

    os = MockOS(0)
    c.lines = []
    c.lines = ['#Ansible: test_cron_job', '42 0 * * * myuser mycommand']
    assert c.get_envnames() == []


# Generated at 2022-06-13 05:05:48.123665
# Unit test for method do_comment of class CronTab
def test_CronTab_do_comment():
    crontab = CronTab(resource, user='my_user', cron_file='/my_file')
    crontab.ansible = 'Ansible: '
    if crontab.do_comment('command') != 'Ansible: command':
        raise AssertionError()


# Generated at 2022-06-13 05:05:55.356537
# Unit test for method render of class CronTab
def test_CronTab_render():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict(
            minute=dict(default='*'),
            hour=dict(default='*'),
            day=dict(default='*'),
            month=dict(default='*'),
            weekday=dict(default='*'),
            job=dict(),
            special_time=dict(),
            disabled=dict(type='bool', default=False),
            name=dict(required=True),
            state=dict(choices=['present', 'absent'], default='present'),
            cron_file=dict(default="")
        )
    )

    cron = CronTab(module)

    minute = module.params['minute']
    hour = module.params['hour']
    day = module.params['day']
   

# Generated at 2022-06-13 05:06:00.481539
# Unit test for method do_add_env of class CronTab
def test_CronTab_do_add_env():
    crontab = CronTab(self.module, user="root")
    decl = "PATH=/my/path"
    index = 2
    lines = [1, 2, 3]

    crontab.do_add_env(lines, decl)
    assert lines[index] == decl


# Generated at 2022-06-13 05:06:09.860923
# Unit test for method write of class CronTab
def test_CronTab_write():
    module = AnsibleModule
    module.get_bin_path = MagicMock(return_value='/bin/crontab')
    module.run_command = MagicMock(return_value=0)

    cron = CronTab(module)
    cron.lines = ['Test content', '']
    cron.write()
    module.run_command.assert_called_with('/bin/crontab', use_unsafe_shell=True)


# Generated at 2022-06-13 05:06:21.399178
# Unit test for method get_envnames of class CronTab
def test_CronTab_get_envnames():
    crontab = CronTab(None)
    assert crontab.lines == []
    crontab = CronTab(None, cron_file='ansible-crontab')
    crontab.lines = ['']
    assert crontab.get_envnames() == []
    crontab.lines = ['PATH=/usr/bin']
    assert crontab.get_envnames() == ['PATH']
    crontab.lines = ['PATH=/usr/bin', 'PATH=/usr/bin', 'OTHER=/usr/bin']
    assert crontab.get_envnames() == ['PATH', 'PATH', 'OTHER']
    crontab.lines = ['PATH=/usr/bin', 'OTHER=/usr/bin']
    assert crontab.get_envnames() == ['PATH', 'OTHER']

# Generated at 2022-06-13 05:06:29.109897
# Unit test for method add_job of class CronTab
def test_CronTab_add_job():
    global _module
    # setup a tmpdir for our test
    tempdir = tempfile.mkdtemp(prefix='ansible_cron_')

    my_cron = CronTab("""
#Ansible: test1
30 01 02 03 04 /bin/test1
#Ansible: test2
""")

    my_cron.add_job("test3", "30 01 02 03 04 /bin/test3")
    my_cron.write(tempdir + "/test_add_job")

    result = None
    with open(tempdir + "/test_add_job", 'r') as f:
        result = f.read()


# Generated at 2022-06-13 05:06:34.552676
# Unit test for method get_jobnames of class CronTab
def test_CronTab_get_jobnames():
    fd, path = tempfile.mkstemp(prefix='crontab')
    os.close(fd)
    with open(path, 'w') as f:
        f.write(textwrap.dedent('''\
            #Ansible: job1
            * * * * * echo "job1"

            #Ansible: job2
            * * * * * echo "job2"
            '''))

    cron = CronTab(None, None, path)
    jobnames = cron.get_jobnames()

    assert len(jobnames) == 2
    assert 'job1' in jobnames
    assert 'job2' in jobnames

    os.unlink(path)



# Generated at 2022-06-13 05:08:26.404499
# Unit test for method do_add_job of class CronTab
def test_CronTab_do_add_job():
    crontab = CronTab()
    crontab.do_add_job(["a"], "b", "c")
    assert crontab.lines == ["a", "b", "c"]
    return True



# Generated at 2022-06-13 05:08:28.405603
# Unit test for method get_envnames of class CronTab
def test_CronTab_get_envnames():
    crontab = CronTab()
    names = crontab.get_envnames()
    assert isinstance(names, list)
    assert len(names) > 0


# Generated at 2022-06-13 05:08:31.455118
# Unit test for method remove_job of class CronTab
def test_CronTab_remove_job():
    crontab = CronTab('', '', '')
    crontab.lines = [u'#Ansible: foo', u'* * * * * /bin/bar']
    actual = crontab.remove_job('foo')
    expected = False
    assert actual == expected


# Generated at 2022-06-13 05:08:43.386126
# Unit test for method update_job of class CronTab
def test_CronTab_update_job():
    ct = CronTab(None, cron_file='/test/test.txt')

    f = open(ct.b_cron_file, 'w')
    f.write("* * * * * /test/test1.sh\n")
    f.write("* * * * * /test/test2.sh\n")
    f.close()

    ct.append(CronItem(':', '* 12 * * *', '/path/to/script_1', 'my_jobname_1'))
    ct.write()

    f = open(ct.b_cron_file, 'r')
    lines = f.readlines()
    f.close()

    assert lines[-1].strip() == "#Ansible: my_jobname_1\n"
    assert lines[-2].strip

# Generated at 2022-06-13 05:08:49.140588
# Unit test for method add_job of class CronTab
def test_CronTab_add_job():
    """
    Unit test for method 'add_job' of class 'CronTab'
    """
    mycron = CronTab('test_user', None)
    mycron.add_job("test_job", "0,30 * * * 1-5 /bin/true")
    assert "0,30 * * * 1-5 /bin/true" in mycron.render()
    assert "#Ansible: test_job" in mycron.render()



# Generated at 2022-06-13 05:08:52.120247
# Unit test for method do_comment of class CronTab
def test_CronTab_do_comment():
    temp_instance = CronTab(module=Mock(), user='', cron_file='')
    temp_instance.ansible = Mock()
    test_name = 'foo'
    assert temp_instance.do_comment(test_name) == 'foo'

# Generated at 2022-06-13 05:08:56.522658
# Unit test for method get_cron_job of class CronTab
def test_CronTab_get_cron_job():
    # Initialize empty class for testing
    crontab = CronTab(None, user='testuser', cron_file='testfile')
    assert crontab.get_cron_job('*', '*', '*', '*', '*', '/bin/touch test', None, False) == '* * * * * testuser /bin/touch test'

# Generated at 2022-06-13 05:08:58.632385
# Unit test for function main
def test_main():
    module = AnsibleModule({}, {}, {})
    # Main should never return anything other than 0 or 1
    assert main(module) in [0, 1]


# Generated at 2022-06-13 05:09:09.909291
# Unit test for method do_remove_job of class CronTab
def test_CronTab_do_remove_job():
    # check 1
    test_CronTab = CronTab(None)
    test_CronTab.lines = [
        '#Ansible: testjob',
        '0  2 * * * sh /tmp/testjob.sh',
        '#Ansible: testjob2',
        '0  3 * * * sh /tmp/testjob2.sh'
    ]
    test_name = 'testjob'
    test_job = ''
    test_CronTab.do_remove_job(test_CronTab.lines, test_name, test_job)
    assert test_CronTab.lines == ['0  3 * * * sh /tmp/testjob2.sh'], test_CronTab.lines

    # check 2
    test_CronTab = CronTab(None)
    test_CronTab

# Generated at 2022-06-13 05:09:16.952648
# Unit test for method remove_job of class CronTab
def test_CronTab_remove_job():
    tests = [{'name': 'test1', 'job': '* * * * * echo test1', 'expected': False},
             {'name': 'test1', 'job': None, 'expected': True},
             {'name': None, 'job': '* * * * * echo test1', 'expected': False},
             {'name': '', 'job': '* * * * * echo test1', 'expected': True}]

    for test in tests:
        crontab = CronTab(None)
        crontab.add_job(name=test['name'], job=test['job'])
        assert crontab.remove_job(test['name']) == test['expected']
