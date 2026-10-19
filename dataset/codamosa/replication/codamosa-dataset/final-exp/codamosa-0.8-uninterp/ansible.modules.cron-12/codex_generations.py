

# Generated at 2022-06-13 05:03:08.607130
# Unit test for method get_envnames of class CronTab
def test_CronTab_get_envnames():
    sample_decls = ('MAILTO=mail@example.com', 'PATH=/bin:/sbin:/usr/bin:/usr/sbin:/opt/bin')
    my_crontab = CronTab(dict(), cron_file='test_file')
    my_crontab.lines = sample_decls
    assert sorted(my_crontab.get_envnames()) == sorted(['MAILTO', 'PATH'])
    
    

# Generated at 2022-06-13 05:03:18.882524
# Unit test for method is_empty of class CronTab
def test_CronTab_is_empty():
    cron = CronTab(None)

    cron.lines = []
    assert cron.is_empty() == True
    cron.lines = ['1 2 3 4 5 something', '']
    assert cron.is_empty() == False
    cron.lines = ['1 2 3 4 5 something', '', '', '']
    assert cron.is_empty() == True
    cron.lines = ['1 2 3 4 5 something', '', '', '', '#something']
    assert cron.is_empty() == True


# Generated at 2022-06-13 05:03:22.956987
# Unit test for method add_env of class CronTab
def test_CronTab_add_env():
    table = CronTab()
    table.add_env(decl='TEST=123', insertafter=None, insertbefore=None)
    table.add_job(name='test_job', job='* * * * * test')
    assert table.render() == 'TEST=123\n#Ansible: test_job\n* * * * * test\n'

# Generated at 2022-06-13 05:03:34.347098
# Unit test for method do_remove_job of class CronTab
def test_CronTab_do_remove_job():
    cr = CronTab(None, cron_file='/tmp/testing')
    cr.lines = ['one','two','three','four','five']
    cr.do_remove_job(None,'','foobar')
    assert cr.lines == ['one','two','three','four','five']
    cr.do_remove_job(['one'],'','foobar')
    assert cr.lines == ['one','foobar','three','four','five']
    cr.do_remove_job(['five'],'','foobar')
    assert cr.lines == ['one','foobar','three','four','five']
    cr.do_remove_job(['two'],'','foobar')
    assert cr.lines == ['one','three','four','five']
    cr.do_remove_job(['one'],'','foobar')
    assert cr

# Generated at 2022-06-13 05:03:44.050996
# Unit test for method do_remove_job of class CronTab
def test_CronTab_do_remove_job():
    #
    # remove job
    #
    name='removal_job'
    crontab = CronTab(None)

    crontab.add_job(name, "* * * * * /bin/true")
    assert crontab.find_job(name)
    assert crontab.remove_job(name)
    assert not crontab.find_job(name)
    assert not crontab.remove_job(name)

    #
    # remove job - doesnt exist
    #
    assert not crontab.remove_job(name)


# Generated at 2022-06-13 05:03:46.441646
# Unit test for method do_remove_env of class CronTab
def test_CronTab_do_remove_env():
    ct = CronTab('')
    assert ct.do_remove_env([], '') is None

# Generated at 2022-06-13 05:03:58.372598
# Unit test for method is_empty of class CronTab
def test_CronTab_is_empty():
    os.environ['HOME'] = '/home/user'
    cron = CronTab(AnsibleModule(argument_spec={}))
    if cron.is_empty():
        raise Exception("CronTab.is_empty() fail: Unexpected empty crontab")

    cron = CronTab(AnsibleModule(argument_spec={}))
    cron.lines = ['']
    if not cron.is_empty():
        raise Exception("CronTab.is_empty() fail: Unexpected non-empty crontab")

    cron = CronTab(AnsibleModule(argument_spec={}))
    cron.lines = ['\n']
    if not cron.is_empty():
        raise Exception("CronTab.is_empty() fail: Unexpected non-empty crontab")


# Generated at 2022-06-13 05:04:04.792471
# Unit test for method do_add_env of class CronTab
def test_CronTab_do_add_env():
    test_object = CronTab(None, None)

    # Test default behavior
    assert test_object.do_add_env(['1\n'], '2\n') == ['1\n', '2\n']

    # Test exception behavior
    with pytest.raises(Exception):
        assert test_object.do_add_env(None)



# Generated at 2022-06-13 05:04:15.119780
# Unit test for method add_env of class CronTab
def test_CronTab_add_env():
  c = CronTab()
  c.lines = ["PATH=/foo", "MAILTO=me@example.com", "HOME=/home/%(user)s"]

  c.add_env("MYVAR=foobar", insertafter="MAILTO")
  assert c.lines == ["PATH=/foo", "MAILTO=me@example.com", "MYVAR=foobar", "HOME=/home/%(user)s"]

  c.lines = ["PATH=/foo", "MAILTO=me@example.com", "HOME=/home/%(user)s"]
  c.add_env("MYVAR=foobar", insertbefore="MAILTO")

# Generated at 2022-06-13 05:04:20.083246
# Unit test for method add_env of class CronTab
def test_CronTab_add_env():
    # Check that exception is raised if object is not initialized
    obj = CronTab()
    obj.module = MagicMock()
    with pytest.raises(Exception) as excinfo:
        obj.add_env("var_name=var_value")
    assert "Object not initialized" in str(excinfo)

    # Check that no exception is raised
    obj1 = CronTab()
    obj1.module = MagicMock()
    obj1.lines = []
    obj1.add_env("var_name=var_value")



# Generated at 2022-06-13 05:05:56.016552
# Unit test for method read of class CronTab
def test_CronTab_read():
    name = 'test_cron'
    module = AnsibleModule(argument_spec={'name': dict(type='str')})
    crontab = CronTab(module)
    assert crontab != None


# Generated at 2022-06-13 05:06:00.917610
# Unit test for method is_empty of class CronTab
def test_CronTab_is_empty():
    crontab = CronTab(module, user=None, cron_file=None)
    if crontab. is_empty() != True:
        print("Method is_empty() of class CronTab does not return expected value")
        exit(1)
    exit(0)


# Generated at 2022-06-13 05:06:12.455855
# Unit test for constructor of class CronTab
def test_CronTab():
    c = CronTab(None, user="root")
    assert c.user == 'root'
    assert c.cron_cmd == '/usr/bin/crontab'
    assert c.n_existing == ''

    c = CronTab(None, user="root", cron_file="/etc/cron.d/crontest")
    assert c.user == 'root'
    assert c.cron_file == '/etc/cron.d/crontest'
    assert c.b_cron_file == b'/etc/cron.d/crontest'
    assert c.n_existing == ''


# Generated at 2022-06-13 05:06:14.874772
# Unit test for method is_empty of class CronTab
def test_CronTab_is_empty():
    # Test if a crontab with no rows is considered empty
    module = AnsibleModule(argument_spec={})
    crontab = CronTab(module)

    crontab.read()
    crontab.lines = []
    assert crontab.is_empty() == True


# Generated at 2022-06-13 05:06:23.189706
# Unit test for method get_envnames of class CronTab
def test_CronTab_get_envnames():
    tab = CronTab(None, None, "test_cronfile")
    tab.lines = [
        'name=value',
        'name =value',
        'name= value',
        'name = value',
        'name2=value2',
        '   name3 = value3',
        '\tname4=value4',
        '\tname5 = value5',
        'name6',
    ]

    assert(tab.get_envnames() == ['name', 'name2', 'name3', 'name4', 'name5'])

# Generated at 2022-06-13 05:06:29.321980
# Unit test for method render of class CronTab
def test_CronTab_render():
    cron = CronTab()
    cron.lines.append("minute hour day month weekday command")
    cron.lines.append("#Ansible: job1")
    cron.lines.append("job2")
    cron.lines.append("#Ansible: job3")
    cron.lines.append("job4")
    cron.lines.append("job5")

    expected = """\
job1
job2
job3
job4
job5
"""

    actual = cron.render()
    assert actual == expected, "\nGot:\n%s\n\nExpected:\n%s" % (actual, expected)


# Generated at 2022-06-13 05:06:35.168147
# Unit test for method is_empty of class CronTab
def test_CronTab_is_empty():
    print("TESTING IS_EMPTY")
    cron = CronTab(None)
    cron.lines = ['', '', '', '']
    assert(cron.is_empty())

    cron = CronTab(None)
    cron.lines = ['', '     ', '#Ansible: Hello', '']
    assert(not cron.is_empty())

    cron = CronTab(None)
    cron.lines = ['', '     ', '', '', '', '#Ansible: Hello', '']
    assert(not cron.is_empty())

    cron = CronTab(None)
    cron.lines = ['', '     ', '#Ansible: ', '']
    assert(not cron.is_empty())


# Generated at 2022-06-13 05:06:41.424909
# Unit test for method get_envnames of class CronTab
def test_CronTab_get_envnames():
    ct = CronTab(None, user=None, cron_file=None)
    ct.lines = [
        '#Ansible: env1',
        '* * * * * /path/to/command',
        '#Ansible: env2',
        '* * * * * /path/to/command',
        '#Ansible: env3',
        '* * * * * /path/to/command'
    ]
    assert ct.get_envnames() == ['env1', 'env2', 'env3']



# Generated at 2022-06-13 05:06:45.582261
# Unit test for method add_job of class CronTab
def test_CronTab_add_job():
    lines = []
    name = None
    job = None
    annotate = CronTab.do_comment
    annotate(lines,name,job)
    assert lines == [None]



# Generated at 2022-06-13 05:06:55.894902
# Unit test for method remove_job of class CronTab
def test_CronTab_remove_job():
    try:
        # test '/etc/cron.d' functionality
        ct = CronTab(module, user=None, cron_file='ansible-crontab.test')
        ct.write()
        ct.remove_job_file()
        # test 'user' functionality
        ct = CronTab(module, user='root', cron_file=None)
        ct.write()
        ct.remove_job('ansible-test-job')
        ct.write()
        ct.remove_job_file()
        # test '/etc/cron.d' functionality
        ct = CronTab(module, user=None, cron_file='ansible-crontab.test')
        ct.write()
        ct.remove_job_file()
    except Exception:
        pass

# Generated at 2022-06-13 05:11:12.049893
# Unit test for method render of class CronTab
def test_CronTab_render():
    ct = CronTab(None, None, None)
    for p in [c.strip() for c in """# DO NOT EDIT THIS FILE - edit the master and reinstall.
    # (/tmp/crontab.XXXX3AvZa9 installed on Thu Nov 26 10:41:58 2015)
    # (Cron version -- $Id: crontab.c,v 2.13 1994/01/17 03:20:37 vixie Exp $)
    #Ansible: test1
    0 2 * 1 * /tmp/ansible
    #Ansible: test2
    0 2 * 1 * /tmp/ansible2
    """.split('\n')]:
        if len(p) > 0:
            ct.lines.append(p)
    ct.lines.append('')

# Generated at 2022-06-13 05:11:23.904400
# Unit test for method do_add_job of class CronTab
def test_CronTab_do_add_job():
    module = AnsibleModule(
        argument_spec = dict()
    )

    cront = CronTab(module)
    do_add_job = cront.do_add_job

    # Test 1.1:
    # Test with no lines, name, and job
    lines = []
    name = "* * * * * root echo 'hello world'"
    job = "* * * * * root echo 'hello world'"
    add_job = do_add_job(lines, name, job)
    assert lines == ["* * * * * root echo 'hello world'", "* * * * * root echo 'hello world'"]

    # Test 1.2:
    # Test with lines, name, and job
    lines = ["* * * * * root echo 'hello world'", "* * * * * root echo 'hello world'"]

# Generated at 2022-06-13 05:11:32.733110
# Unit test for method add_env of class CronTab
def test_CronTab_add_env():
    module = AnsibleModule(
        argument_spec = dict(
            special_time=dict(type='str'),
            state=dict(default='present', choices=['absent', 'present']),
            job=dict(required=False),
            name=dict(required=True),
            disabled=dict(type='bool', default=False),
        ),
        supports_check_mode=True
    )

    job = CronTab(module)
    job.add_job('name', '')
    job.add_env('XYZ=1')

    return job.get_jobnames()


# Generated at 2022-06-13 05:11:38.029485
# Unit test for method find_env of class CronTab
def test_CronTab_find_env():
    c = CronTab('module', None)
    c.lines = [
        'TEST=test',
        'TEST2=test',
        'TEST3=test',
    ]
    assert c.find_env('TEST') == [0, 'TEST=test']
    assert c.find_env('TEST2') == [1, 'TEST2=test']
    assert c.find_env('TEST3') == [2, 'TEST3=test']


# Generated at 2022-06-13 05:11:47.396999
# Unit test for constructor of class CronTab
def test_CronTab():
    module = AnsibleModule(argument_spec={})

    # Testing no arguments
    c = CronTab(module)
    assert c.cron_cmd == '/usr/bin/crontab'
    assert c.user is None
    assert c.root
    assert c.lines == []
    assert c.cron_file is None
    assert c._read_user_execute() == '/usr/bin/crontab  -l'
    assert c._write_execute('/path') == '/usr/bin/crontab  /path'
    assert c.render() == ''
    assert c.find_job('job') == []
    assert c.get_jobnames() == []
    assert c.get_envnames() == []

    # Testing user argument
    c = CronTab(module, user='test')
    assert c.c

# Generated at 2022-06-13 05:11:58.337600
# Unit test for method find_job of class CronTab
def test_CronTab_find_job():
    # Initialise a CronTab object
    crontab = CronTab(module, user=None, cron_file=None)
    crontab.n_existing = 'a newline here\n#Ansible: A comment\nsome important job\n#Ansible: Another comment\n'
    crontab.lines = crontab.n_existing.splitlines()
    # Find job with ansible header
    result = crontab.find_job("A comment", job=None)
    # Result should equal to: [u'#Ansible: A comment', u'some important job']
    assert result == ['#Ansible: A comment', 'some important job']
    # Find job without ansible header and exact match
    result = crontab.find_job("A comment", job='some important job')
    # Result

# Generated at 2022-06-13 05:11:59.908382
# Unit test for method remove_job of class CronTab
def test_CronTab_remove_job():
  cron = CronTab(module, user='testuser')
  assert cron.remove_job('testname') == True

# Generated at 2022-06-13 05:12:06.022391
# Unit test for method do_add_env of class CronTab
def test_CronTab_do_add_env():
    '''
    Unit test for method do_add_env

    Test that proper order is preserved and that env var is added.
    '''
    my_lines = [("PATH=blah"), ("LD_LIBRARY_PATH=foo"), ("MAILTO=root")]
    my_name = "NEW_VAR"
    my_decl = "NEW_VAR=foo"
    my_expected_lines = [("PATH=blah"), ("LD_LIBRARY_PATH=foo"), ("MAILTO=root"), ("NEW_VAR=foo")]
    my_task = CronTab(my_lines)
    my_task.do_add_env(my_lines, my_decl)
    assert my_expected_lines == my_lines, "do_add_env doesn't add new env var to end of list"
    my

# Generated at 2022-06-13 05:12:12.372048
# Unit test for method get_jobnames of class CronTab
def test_CronTab_get_jobnames():
    ct = CronTab(None)
    ct.lines = [
        '#Ansible: job1',
        '#Ansible: job2',
        '* * * * * echo "job3"',
        '#Ansible: job4',
        '#Ansible: job5',
    ]

    assert ct.get_jobnames() == ['job1', 'job2', 'job4', 'job5']

# Generated at 2022-06-13 05:12:15.077671
# Unit test for function main
def test_main():
    # Too many arguments, should raise an error
    with pytest.raises(SystemExit) as err:
        main(["one", "two", "three"])
    assert err.value.code == 2

    # Missing required argument, should raise an error
    with pytest.raises(SystemExit) as err:
        main(["--state=present"])
    assert err.value.code == 2
