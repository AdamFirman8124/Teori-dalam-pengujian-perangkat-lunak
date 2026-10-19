

# Generated at 2022-06-13 05:03:14.849597
# Unit test for method find_job of class CronTab
def test_CronTab_find_job():
    ct = CronTab()
    ct.lines = [
            "#Ansible: test_job",
            "0 0 * * * test_job"
    ]
    job = ct.find_job("test_job", "0 0 * * * test_job")
    assert job == ["#Ansible: test_job", "0 0 * * * test_job"]
    job = ct.find_job("test_job", "0 0 * * * not_job")
    assert job == []
    ct.lines = [
            "0 0 * * * test_job"
    ]
    job = ct.find_job("test_job", "0 0 * * * test_job")
    assert job == ["0 0 * * * test_job", "0 0 * * * test_job", True]



# Generated at 2022-06-13 05:03:20.171763
# Unit test for method get_envnames of class CronTab
def test_CronTab_get_envnames():
    ct = CronTab(module, user, cron_file)
    assert(type(ct.get_envnames()) == list)
    for envname in ct.get_envnames():
        assert(type(envname) == string)


# Generated at 2022-06-13 05:03:31.545862
# Unit test for method get_cron_job of class CronTab
def test_CronTab_get_cron_job():
    f = CronTab.get_cron_job
    assertEquals(f('1', '2', '3', '4', '5', 'job', None, None), '1 2 3 4 5 job')
    assertEquals(f('1', '2', '3', '4', '5', 'job', 'special', None), '@special job')
    assertEquals(f('1', '2', '3', '4', '5', 'job', None, False), '1 2 3 4 5 job')
    assertEquals(f('1', '2', '3', '4', '5', 'job', None, True), '#1 2 3 4 5 job')


# Generated at 2022-06-13 05:03:39.184708
# Unit test for method do_add_env of class CronTab

# Generated at 2022-06-13 05:03:46.185528
# Unit test for method add_env of class CronTab
def test_CronTab_add_env():
    # Create an instance of class CronTab
    cron_tab = CronTab(None, user=None, cron_file=None)

    # Initialize a_variable
    a_variable = ""
    expected_result = []

    # Call method add_env of class CronTab
    result = cron_tab.add_env(a_variable,)

    # Print result or expected result
    assert result == expected_result
    # return result


# Generated at 2022-06-13 05:03:57.922535
# Unit test for method remove_job of class CronTab
def test_CronTab_remove_job():
    module = AnsibleModule(
        argument_spec = dict(
            name = dict(type='str', required=True),
            user = dict(type='str'),
            state = dict(default='present', choices=['present', 'absent']),
        ),
        supports_check_mode=True
    )
    INPUT_DATA = {
        'state': 'absent',
        'name': 'test_job',
        'user': 'root',
    }
    input_data = INPUT_DATA
    c = CronTab(module, user=input_data['user'])
    j = c.find_job(input_data['name'])
    if len(j) == 0:
        to_be_removed = False
    else:
        to_be_removed = True
    removed = c.remove_

# Generated at 2022-06-13 05:04:02.101857
# Unit test for method do_comment of class CronTab
def test_CronTab_do_comment():
    c = CronTab(None)
    assert c.do_comment(None) == "#Ansible:"
    assert c.do_comment("name") == "#Ansible: name"


# Generated at 2022-06-13 05:04:05.432841
# Unit test for method do_remove_job of class CronTab
def test_CronTab_do_remove_job():
    c = CronTab(None)
    lines = ['A', 'B', 'C', 'D']
    assert c.do_remove_job(lines, 'B', 'C') is None
    assert lines == ['A', 'D']

# Generated at 2022-06-13 05:04:11.843601
# Unit test for method add_env of class CronTab
def test_CronTab_add_env():
    args = dict(decl='JAVA_HOME=/opt/jdk', insertafter=None, insertbefore=None)
    ct = CronTab(user=None, cron_file=None)
    ct.lines = ['PATH=/usr/bin:/bin', 'HOME=/home/demouser']
    ct.add_env(**args)
    assert ct.lines[2] == 'JAVA_HOME=/opt/jdk'


# Generated at 2022-06-13 05:04:19.727970
# Unit test for method render of class CronTab

# Generated at 2022-06-13 05:06:14.044177
# Unit test for method find_job of class CronTab
def test_CronTab_find_job():
    job = '* * * * * /bin/echo hello'
    crontab = CronTab(None, "root", None)
    crontab.lines = ['#Ansible: testjob', job]
    assert crontab.find_job("testjob", job) == ["testjob", job]
    assert crontab.find_job("testjob") == ["testjob", job]
    assert crontab.find_job("not_a_job", job) == []
    assert crontab.find_job("not_a_job") == []

# Generated at 2022-06-13 05:06:15.048605
# Unit test for method update_job of class CronTab
def test_CronTab_update_job():
	pass

# Generated at 2022-06-13 05:06:25.423277
# Unit test for method find_env of class CronTab
def test_CronTab_find_env():
    # Create a class instance
    cron_tab = CronTab(module=None)

    # Nones are special case, return None
    assert cron_tab.find_env(None) == [], 'Nones are special case, return None'

    # Empty list
    assert cron_tab.find_env('') == [], 'Empty list'

    # Empty list
    cron_tab.lines = ["VAR1=1", "VAR2=2", "VAR3=3"]
    assert cron_tab.find_env('VAR1') == [0, 'VAR1=1'], 'Empty list'

    # Empty list
    cron_tab.lines = ["VAR1=1", "VAR2=2", "VAR3=3"]

# Generated at 2022-06-13 05:06:31.207233
# Unit test for method add_job of class CronTab
def test_CronTab_add_job():
    ct = CronTab()
    ct.add_job('test_name', 'test_job')
    assert ct.lines[0] == "#Ansible: test_name"
    assert ct.lines[1] == "test_job"



# Generated at 2022-06-13 05:06:36.979296
# Unit test for method get_jobnames of class CronTab
def test_CronTab_get_jobnames():
    #pass
    c = CronTab(None, None, None)
    c.lines = [u'#ansible: test1', u'DUMMY', u'#ansible: test2', u'DUMMY', u'# test3', u'DUMMY']
    assert c.get_jobnames() == ['test1', 'test2']



# Generated at 2022-06-13 05:06:51.112301
# Unit test for function main

# Generated at 2022-06-13 05:06:53.257499
# Unit test for method get_envnames of class CronTab
def test_CronTab_get_envnames():
    os.environ['TZ'] = 'UTC'
    time.tzset()
    CronTab()
    pass


# Generated at 2022-06-13 05:06:53.939673
# Unit test for method do_add_env of class CronTab
def test_CronTab_do_add_env():
    assert True

# Generated at 2022-06-13 05:07:03.111132
# Unit test for function main
def test_main():
    try:
        backend = Basic('test')
        data = dict()
        data['test'] = 'test'
        data['test2'] = {'test23': 'test234'}
        data['test3'] = [1, 2, 3, 4]
        pprint(backend._serialize(data))
        pprint(backend._deserialize(backend._serialize(data)))
    except Exception as err:
        pprint(err)
        raise


# Generated at 2022-06-13 05:07:05.536106
# Unit test for method remove_job of class CronTab
def test_CronTab_remove_job():
    ct = CronTab()
    ct.lines = ['#Ansible dummy', '* * * * * echo "hello"']
    ct.remove_job('dummy')
    assert ct.lines == []


# Generated at 2022-06-13 05:09:13.263559
# Unit test for method do_add_env of class CronTab
def test_CronTab_do_add_env():
    """
    test the method do_add_env of class CronTab
    """
    #################################################################
    # test when lines is an empty list
    #################################################################
    time = time.asctime(time.localtime())
    print("Now is:", time)
    lines = []
    decl = "decl"
    new_line = "new_line"
    crontab = CronTab(module,user=None,cron_file=None)
    lines = crontab.do_add_env(lines, decl)
    assert lines[0] == new_line
    print("do_add_env() of class CronTab works as expected")
    return


# Generated at 2022-06-13 05:09:14.967433
# Unit test for method write of class CronTab
def test_CronTab_write():
    assert CronTab._write_execute("/tmp") == "crontab -l -u root /tmp"



# Generated at 2022-06-13 05:09:23.192243
# Unit test for method get_jobnames of class CronTab
def test_CronTab_get_jobnames():
    c = CronTab()
    c.lines = ['#Ansible: John', '0 0 * * * /usr/bin/run_me_ daily', '#Ansible: Paul', '0 0 * * 7 /usr/bin/run_me_ weekly', '#Ansible: George', '0 0 1 * * /usr/bin/run_me_ monthly', '#Ansible: Ringo', '0 0 1 1 * /usr/bin/run_me_ yearly']
    assert c.get_jobnames() == ['John', 'Paul', 'George', 'Ringo']



# Generated at 2022-06-13 05:09:30.209049
# Unit test for method get_cron_job of class CronTab
def test_CronTab_get_cron_job():
    import pprint

# Generated at 2022-06-13 05:09:36.349528
# Unit test for method get_envnames of class CronTab
def test_CronTab_get_envnames():
    lines = ['#Ansible: env1', '#Ansible: env2']
    obj = CronTab(module=None, user=None, cron_file=None)
    obj.lines = lines
    expected = ['env1', 'env2']
    result = obj.get_envnames()
    assert result == expected

# Generated at 2022-06-13 05:09:47.493091
# Unit test for method get_cron_job of class CronTab
def test_CronTab_get_cron_job():
    module = MagicMock()
    module.run_command.return_value = (0, '', '')
    module.get_bin_path.return_value = "/usr/bin/crontab"
    def mock_selinux_enabled():
        return True
    module.selinux_enabled.side_effect = mock_selinux_enabled
    
    # NOTE: set the user name your system uses for the crontab
    test_user = "root"

    ct = CronTab(module, test_user)
    assert ct.get_cron_job("12", "", "", "", "", "/bin/date", "", False).startswith("12")
    assert ct.get_cron_job("12", "", "", "", "", "/bin/date", "", True).startsw

# Generated at 2022-06-13 05:09:52.084393
# Unit test for method add_env of class CronTab
def test_CronTab_add_env():
    global module
    module = AnsibleModule(argument_spec={'user': {}, 'minute': {}, 'hour': {}, 'day': {}, 'month': {}, 'weekday': {}, 'job': {}, 'name': {}, 'special_time': {}, 'disabled': {}, 'insertafter': {}, 'insertbefore': {}, 'decl': {}})
    c = CronTab(module)
    c.add_env("TEST=bla", insertafter="PATH")


# Generated at 2022-06-13 05:10:00.584152
# Unit test for method find_env of class CronTab
def test_CronTab_find_env():
    with tempfile.NamedTemporaryFile() as cronfile:
        cronfile.write(to_bytes("* * * * * echo 'test'\n"))
        cronfile.write(to_bytes("Myvar=myvalue\n"))
        cronfile.write(to_bytes("Myvar2=myvalue2\n"))
        cronfile.flush()

        cron = CronTab(None, cron_file=cronfile.name)
        assert cron.find_env('Myvar') == [1, 'Myvar=myvalue']
        assert cron.find_env('Myvar2') == [2, 'Myvar2=myvalue2']
        assert cron.find_env('OtherVar') == []

        assert cron.remove_job_file() == True



# Generated at 2022-06-13 05:10:08.229485
# Unit test for function main

# Generated at 2022-06-13 05:10:10.815699
# Unit test for method remove_job of class CronTab
def test_CronTab_remove_job():
    user = ""
    cron_file = ""
    crontab = CronTab(user, cron_file)
    name = ""
    assert crontab.remove_job(name) == False
