

# Generated at 2022-06-13 05:03:15.360332
# Unit test for method get_jobnames of class CronTab
def test_CronTab_get_jobnames():
    module = AnsibleModule(argument_spec={}, supports_check_mode=False)
    cron = CronTab(module, user='root', cron_file='/tmp/test_cron_file')
    cron.lines = ["#Ansible: \"job name 1\"", "* * * * * job 1", "#Ansible: \"job name 2\"", "* * * * * job 2"]
    assert cron.get_jobnames() == ["job name 1", "job name 2"]


# Generated at 2022-06-13 05:03:20.841431
# Unit test for method get_envnames of class CronTab
def test_CronTab_get_envnames():
    crontab = CronTab(None, None, '/tests/var/ansible_test_cron.txt')
    envnames = crontab.get_envnames()
    assert envnames == ['TEST1', 'TEST2', 'TEST3', 'TEST4']


# Generated at 2022-06-13 05:03:33.079085
# Unit test for method do_add_env of class CronTab
def test_CronTab_do_add_env():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.pycompat24 import get_exception
    module = AnsibleModule(
        argument_spec = dict(
            a = dict(type='str'),
        ),
        supports_check_mode=True
    )

    # set up all inputs
    a = 'b'

    # create cron object
    cron = CronTab(module)

    # call function do_add_env on object cron

# Generated at 2022-06-13 05:03:37.121032
# Unit test for method get_envnames of class CronTab
def test_CronTab_get_envnames():
    test_module = AnsibleModule(argument_spec={})
    test_ctab = CronTab(test_module)
    result = test_ctab.get_envnames()
    assert type(result) is list



# Generated at 2022-06-13 05:03:46.505631
# Unit test for method find_job of class CronTab
def test_CronTab_find_job():
    v_CronTab = CronTab(module, user=None, cron_file=None)
    v_CronTab.lines = [
        '#Ansible: test_job',
        '#Ansible: no_job',
        '*/1 * * * * echo "wow"',
        ''
    ]
    assert v_CronTab.find_job('test_job') == ['#Ansible: test_job', '*/1 * * * * echo "wow"']
    assert v_CronTab.find_job('no_job') == []


# Generated at 2022-06-13 05:03:48.437876
# Unit test for method is_empty of class CronTab
def test_CronTab_is_empty():
    test_obj = CronTab('', '', '')
    assert test_obj.is_empty()

# Generated at 2022-06-13 05:03:51.053772
# Unit test for method get_jobnames of class CronTab
def test_CronTab_get_jobnames():
    c = CronTab({'absent':None,'minute': None,'hour': None,'day': None,'month': None,'weekday': None,'user': None,'name': None,'disabled': None,'job': None,'special_time': None},user="root",cron_file="/etc/cron.d/ansible")


# Generated at 2022-06-13 05:03:58.697631
# Unit test for method update_env of class CronTab
def test_CronTab_update_env():
    # This test is specific to AIX
    if platform.system() != 'AIX':
        raise Exception("System is not AIX")
    cron = CronTab(module=None, cron_file="/etc/cron.d/mycron")
    cron.lines = ["#Ansible: mycron", "FOO=foo", "#Ansible: mycron2", "FOO=foo"]
    env_name = "FOO"
    decl = "FOO=baz"
    temp_file = "/tmp/foo"
    cron.write(temp_file)

# Generated at 2022-06-13 05:04:00.290384
# Unit test for method render of class CronTab
def test_CronTab_render():
    results = CronTab('module', 'root').render()
    assert results == None

# Generated at 2022-06-13 05:04:04.416677
# Unit test for method update_env of class CronTab
def test_CronTab_update_env():
    c = CronTab(None)
    c.lines = ['test=test']
    c._update_env('test', 'test', c.do_add_env)

    assert c.lines == []



# Generated at 2022-06-13 05:05:47.312220
# Unit test for method do_remove_env of class CronTab
def test_CronTab_do_remove_env():
    from ansible.module_utils.basic import AnsibleModule

    # prepare module
    test_module = AnsibleModule({})
    test_module.exit_json = mock.MagicMock()

    # prepare module args
    lines = []
    decl = 'VAR=VAL'

    # prepare object
    mycron = CronTab(test_module)
    actual = mycron.do_remove_env(lines, decl)

    # verify results
    assert actual is None
    assert lines == []



# Generated at 2022-06-13 05:05:57.768195
# Unit test for method remove_job of class CronTab
def test_CronTab_remove_job():
    module = AnsibleModule(argument_spec={})
    crontab = CronTab(module)
    crontab.read()
    test_crontab = """# (test_file.cron installed on Wed Jun 24 17:31:43 2020)
# (Cron version -- $Id: crontab.c,v 2.13 1994/01/17 03:20:37 vixie Exp $)
1 2 3 4 5 user command

#Ansible: test_job
* 3 4 5 6 7 user command
"""
    crontab.lines = test_crontab.split('\n')
    crontab.remove_job('test_job')
    output = crontab.render()

# Generated at 2022-06-13 05:06:05.565577
# Unit test for method do_add_env of class CronTab
def test_CronTab_do_add_env():
    assert CronTab.do_add_env(["abc", "def"], "MYVAR=hello") == ["abc", "def", "MYVAR=hello"]
    assert CronTab.do_add_env(["abc", "def"], "MYVAR2=goodbye") == ["abc", "def", "MYVAR2=goodbye"]
    assert CronTab.do_add_env([], "MYVAR=hello") == ["MYVAR=hello"]
    assert CronTab.do_add_env([], "MYVAR2=goodbye") == ["MYVAR2=goodbye"]
    assert CronTab.do_add_env(["abc", "def"], "") == ["abc", "def"]



# Generated at 2022-06-13 05:06:13.624937
# Unit test for method is_empty of class CronTab
def test_CronTab_is_empty():
    # Arrange
    from ansible.module_utils.basic import AnsibleModule
    from ansible_collections.community.general.plugins.module_utils.cron import CronModule, CronTab
    a = AnsibleModule({})
    ct = CronTab(a)

    # Act
    result = ct.is_empty()

    # Assert
    assert result == True



# Generated at 2022-06-13 05:06:20.327558
# Unit test for method get_envnames of class CronTab
def test_CronTab_get_envnames():
    ct = CronTab(None)
    ct.lines = [
        '#Ansible: job',
        '@daily foo bar',
        'foo = bar',
        'baz = qux',
        '#Ansible: job2',
        '@daily foo bar',
    ]
    assert ct.get_envnames() == ['foo', 'baz']


# Generated at 2022-06-13 05:06:31.267371
# Unit test for method get_envnames of class CronTab
def test_CronTab_get_envnames():
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    crontab = CronTab(module)
    crontab.lines = [
        "#Ansible:ENVNAME1",
        "ENVNAME1=value1",
        "#Ansible:ENVNAME2",
        "ENVNAME2=value2",
        ]
    expectedoutput = ["ENVNAME1",
                      "ENVNAME2"]
    output = crontab.get_envnames()
    assert output == expectedoutput, \
        "expected %s, got %s" % (expectedoutput, output)


# Generated at 2022-06-13 05:06:41.022824
# Unit test for method do_remove_job of class CronTab
def test_CronTab_do_remove_job():
    def do_remove_job(lines, comment, job):
        return None

    ct = CronTab()
    ct.lines = [
        "#Ansible: TestJobName",
        "1 2 3 4 5 testjob.sh"
    ]

    ct.do_remove_job(ct.lines, "#Ansible: TestJobName", "1 2 3 4 5 testjob.sh")
    assert len(ct.lines) == 0

    ct.lines = [
        "1 2 3 4 5 testjob.sh",
        "1 2 3 4 5 testjob.sh"
    ]

    ct.do_remove_job(ct.lines, "#Ansible: TestJobName", "1 2 3 4 5 testjob.sh")
    assert len(ct.lines) == 2

    return



# Generated at 2022-06-13 05:06:51.111441
# Unit test for method add_job of class CronTab
def test_CronTab_add_job():
    # This is a python unit test for the method add_job of class CronTab.
    #
    # We make an instance of the class CronTab and add a new cronjob.
    # Then we check if the cronjob is correctly added to the lines list
    # of the instance.

    cron1 = CronTab(module, user='root', cron_file='/tmp/deleteme')
    cron1.add_job('TEST_NAME', '* * * * * /bin/true')
    assert cron1.lines[-1] == '*/1 * * * * /bin/true'



# Generated at 2022-06-13 05:07:00.446072
# Unit test for method read of class CronTab

# Generated at 2022-06-13 05:07:03.189162
# Unit test for method render of class CronTab
def test_CronTab_render():
    obj = CronTab()
    obj.lines = ['# test', '@hourly', '0 2 * * *']
    assert obj.render() == '# test\n@hourly\n0 2 * * *'



# Generated at 2022-06-13 05:11:06.014879
# Unit test for method do_add_env of class CronTab
def test_CronTab_do_add_env():
    # Simple test case
    c = CronTab(None)
    newlines = []
    l = "SOME_VAR=SOME_VALUE"
    c.do_add_env(newlines, l)
    assert newlines == [l]
    

# Generated at 2022-06-13 05:11:14.083842
# Unit test for method do_remove_env of class CronTab

# Generated at 2022-06-13 05:11:20.986807
# Unit test for method do_add_job of class CronTab
def test_CronTab_do_add_job():
    ct = CronTab(None, None)
    new_lines = []
    comment = 'comment'
    job = 'job'
    ct.do_add_job(new_lines, comment, job)
    assert(len(new_lines) == 2)
    assert(new_lines[0] == comment)
    assert(new_lines[1] == 'job')

# Generated at 2022-06-13 05:11:33.403664
# Unit test for method update_env of class CronTab
def test_CronTab_update_env():
    import tempfile

    try:
        fd, tmp_file = tempfile.mkstemp(prefix='crontab')

        os.write(fd, b"""\
PATH=/bin:/sbin:/usr/bin:/usr/sbin
#*/5 * * * * root /sbin/cleanup.sh
""")
        os.close(fd)

        cron = CronTab(user='root', cron_file=tmp_file)

        cron.update_env('PATH', 'PATH=/bin:/sbin:/usr/bin')

        expected = """\
PATH=/bin:/sbin:/usr/bin
#*/5 * * * * root /sbin/cleanup.sh
"""

        assert cron.render() == expected
    finally:
        os.unlink(tmp_file)


# Generated at 2022-06-13 05:11:38.000152
# Unit test for method remove_job of class CronTab
def test_CronTab_remove_job():
    module = AnsibleModule(argument_spec={})
    ct = CronTab(module)
    ct.lines=[u'minute hour day month weekday    command']
    ct.n_existing=u'minute hour day month weekday    command'
    name = u''
    assert(ct.remove_job(name) == False)


# Generated at 2022-06-13 05:11:49.840150
# Unit test for method get_jobnames of class CronTab
def test_CronTab_get_jobnames():
    ct = CronTab('')

    # test 1
    ct.lines.append('#')
    ct.lines.append('#Ansible: name1')
    ct.lines.append('#')
    ct.lines.append('#Ansible: name2')
    ct.lines.append('#')
    ct.lines.append('#Ansible: name3')
    ct.lines.append('#')
    ct.lines.append('#Ansible: name4')

    assert ct.get_jobnames() == ['name1', 'name2', 'name3', 'name4']



# Generated at 2022-06-13 05:11:53.424318
# Unit test for method get_cron_job of class CronTab
def test_CronTab_get_cron_job():
    cron_tab = CronTab()
    assert cron_tab.get_cron_job('*', '*', '*', '*', '*', 'ls -la', '', 'False') == '* * * * * ls -la'


# Generated at 2022-06-13 05:12:02.410319
# Unit test for method write of class CronTab
def test_CronTab_write():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.basic import AnsibleModule


# Generated at 2022-06-13 05:12:13.112909
# Unit test for method get_cron_job of class CronTab
def test_CronTab_get_cron_job():
    # create a MockAnsibleModule
    mm = MockAnsibleModule()

    # Initialize a CronTab object
    ct = CronTab(mm, 'root', 'test')

    # test that cron_file is initialized to None
    assert ct.cron_file is None

    # test that get_cron_job returns a enabled cronjob
    result = ct.get_cron_job("*", "*", "*", "*", "*", "/bin/foo", "", False)
    assert result == "* * * * * /bin/foo"

    # test that get_cron_job returns a disabled cronjob and that the disabled
    # cronjob is the same for both normal crontabs and crond.d files
    ct.cron_file = "test"
    result = c

# Generated at 2022-06-13 05:12:19.111873
# Unit test for method add_env of class CronTab