

# Generated at 2022-06-13 05:03:17.657394
# Unit test for method do_comment of class CronTab
def test_CronTab_do_comment():
    ct = CronTab(module="")
    assert ct.do_comment("test") == "#Ansible: test"

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:03:26.737026
# Unit test for method do_add_env of class CronTab
def test_CronTab_do_add_env():
    from ansible_collections.notstdlib.moveitallout.tests.unit import mock_module, mock_command

    crontab = CronTab(module=mock_module)

    crontab.do_add_env(lines=[], decl='Foo=bar')

    assert crontab.lines == ['Foo=bar']

    crontab.do_add_env(lines=[], decl='Bar=baz')

    assert crontab.lines == ['Bar=baz', 'Foo=bar']



# Generated at 2022-06-13 05:03:39.414495
# Unit test for method remove_env of class CronTab
def test_CronTab_remove_env():
    '''
    Unit tests for method remove_env of class CronTab
    '''
    crontab = CronTab(None)
    # test for None
    with pytest.raises(TypeError) as exception_info:
        assert crontab.remove_env(None)
    assert "[remove_env] name argument must be a string" in str(exception_info.value)
    # test for invalid type
    with pytest.raises(TypeError) as exception_info:
        assert crontab.remove_env(True)
    assert "[remove_env] name argument must be a string" in str(exception_info.value)
    # test for empty string
    with pytest.raises(ValueError) as exception_info:
        assert crontab.remove_env("")

# Generated at 2022-06-13 05:03:40.503910
# Unit test for method write of class CronTab
def test_CronTab_write():
    assert True == True


# Generated at 2022-06-13 05:03:46.256534
# Unit test for method add_env of class CronTab
def test_CronTab_add_env():
    """
    add_env([decl, insertafter=None, insertbefore=None])
    """
    item = CronTab('user')

    # test with default arguments
    item.add_env('decl')

    # test with positional arguments
    item.add_env('decl', insertafter='insertafter', insertbefore='insertbefore')



# Generated at 2022-06-13 05:03:51.189681
# Unit test for method read of class CronTab
def test_CronTab_read():
    # Arrange
    module = MagicMock()
    module.get_bin_path.return_value = '/usr/bin/crontab'
    crontab = CronTab(module)

    # Assign
    crontab.lines = None

    # Act
    crontab.read()

    # Assert
    assert crontab.lines == []


# Generated at 2022-06-13 05:04:04.739535
# Unit test for method find_env of class CronTab
def test_CronTab_find_env():
    # Clean environment
    try:
        del os.environ['ANSIBLE_CRONTAB_MODULE_TEST']
    except KeyError:
        pass

    # Test with existing environnement variable
    os.environ['ANSIBLE_CRONTAB_MODULE_TEST'] = 'toto'
    cron_tab = CronTab(module=AnsibleModule(argument_spec={}), user=pwd.getpwuid(os.getuid())[0])

    assert cron_tab.find_env('ANSIBLE_CRONTAB_MODULE_TEST') == [0, 'ANSIBLE_CRONTAB_MODULE_TEST=toto']

    # Test with non existing environnement variable

# Generated at 2022-06-13 05:04:09.081249
# Unit test for method is_empty of class CronTab
def test_CronTab_is_empty():
    ct = CronTab('crontab', 'root')
    if ct.lines == []:
        assert ct.is_empty() == True
    else:
        assert ct.is_empty() == False


# Generated at 2022-06-13 05:04:17.588160
# Unit test for method render of class CronTab
def test_CronTab_render():
    pass
    #TODO: Improve this test

# Generated at 2022-06-13 05:04:21.786297
# Unit test for method remove_job_file of class CronTab
def test_CronTab_remove_job_file():
    # initializing argument values
    name = ''
    job = ''
    special = ''
    disabled = True

    # Create an instance of the "CronTab" class
    cron_tab = CronTab(name,job,special,disabled)
    expected = ''

    # execute function
    result = cron_tab.remove_job_file()

    # assert the output
    assert result is expected, "The expected output does not match the returned output"


# Generated at 2022-06-13 05:05:19.468783
# Unit test for method is_empty of class CronTab
def test_CronTab_is_empty():
    import mock

    class MockModule(object):
        def __init__(self, params):
            self.params = params

        def run_command(self, command, use_unsafe_shell):
            return (0, "", "")

        def get_bin_path(self, executable, required):
            return ""

        def fail_json(self, msg):
            return

        def selinux_enabled(self):
            return False

        def set_default_selinux_context(self, path, recursive):
            return


# Generated at 2022-06-13 05:05:25.782080
# Unit test for method get_envnames of class CronTab
def test_CronTab_get_envnames():
    from ansible.module_utils import basic

    f1 = tempfile.NamedTemporaryFile()
    f1name = f1.name

    f1.write(b'''SHELL=/bin/bash
PATH=/sbin:/bin:/usr/sbin:/usr/bin
MAILTO=root
HOME=/

''')

    f1.seek(0)

    ct = CronTab(f1name,user=None,cron_file=None)
    ct.lines = f1.readlines()
    f1.close()

    assert ct.get_envnames() == ['SHELL', 'PATH', 'MAILTO', 'HOME']


# Generated at 2022-06-13 05:05:30.953053
# Unit test for method do_remove_job of class CronTab
def test_CronTab_do_remove_job():
    ct = CronTab()
    lines = []
    comment = "test comment"
    job = "test job"
    result = ct.do_remove_job(lines, comment, job)

    assert(result==None)


# Generated at 2022-06-13 05:05:39.938260
# Unit test for method update_env of class CronTab
def test_CronTab_update_env():
    ct = CronTab()
    ct.lines = ['VAR1=VALUE1']
    assert ct.update_env('VAR1', 'NEW')

    ct.lines = ['VAR1=VALUE1', 'VAR2=VALUE2', 'VAR3=VALUE3']
    assert ct.update_env('VAR1', 'NEW')

    ct.lines = ['VAR1=VALUE1', 'VAR2=VALUE2', 'VAR3=VALUE3']
    assert ct.update_env('VAR4', 'NEW')

    ct.lines = []
    assert ct.update_env('VAR1', 'NEW')


# Generated at 2022-06-13 05:05:49.061319
# Unit test for method render of class CronTab
def test_CronTab_render():
    lines = ['#Ansible: name1', '1 * * * * *', '#Ansible: name2', '2 * * * * *', '#Ansible: name3', '3 * * * * *',
             '#Ansible: name4', '4 * * * * *']
    obj = CronTab('', '')
    obj.lines = lines
    obj.ansible = '#Ansible: '
    expected_result = "\n".join(lines)
    render_result = obj.render()
    assert render_result == expected_result, 'render should return %s, got %s' % (expected_result, render_result)



# Generated at 2022-06-13 05:05:55.872379
# Unit test for method read of class CronTab
def test_CronTab_read():
    # Creation of a new object
    crontab = CronTab(None, 'bob')

    # Creation of the data file
    f = open('/tmp/test_cron', 'w')
    f.write("test line 1\ntest line 2\n")
    f.close()
    os.chmod('/tmp/test_cron', int('0600', 8))

    # Test normal output
    crontab.cron_file = '/tmp/test_cron'
    crontab.read()
    lines = crontab.n_existing
    assert len(crontab.lines) == 2
    assert crontab.lines[0] == "test line 1"
    assert crontab.lines[1] == "test line 2"
    os.unlink('/tmp/test_cron')


# Generated at 2022-06-13 05:06:05.270585
# Unit test for method find_job of class CronTab
def test_CronTab_find_job():
    class ModuleMock(object):
        pass

    module = ModuleMock()

    obj = CronTab(module, cron_file='/etc/cron.d/holland')

    obj.lines = [
        '#Ansible: holland_backup_all_databases',
        '0 0 * * * root /usr/libexec/holland/backup.sh mysqldump -all --lock-tables=false',
    ]

    name = 'holland_backup_all_databases'
    job = '0 0 * * * root /usr/libexec/holland/backup.sh mysqldump -all --lock-tables=false'
    output = obj.find_job(name, job)

# Generated at 2022-06-13 05:06:17.395376
# Unit test for method do_remove_job of class CronTab
def test_CronTab_do_remove_job():
    """
    Test that do_remove_job of class CronTab
    """
    ct = CronTab(None, None)

    lines = [
        '#Ansible: aaa',
        '* * * * * /tmp/aaa',
        '#Ansible: bbb',
        '* * * * * /tmp/bbb',
    ]
    comment = '#Ansible: aaa'
    job = '* * * * * /tmp/aaa'
    assert ct.do_remove_job(lines, comment, job) is None
    assert lines == [
        '#Ansible: bbb',
        '* * * * * /tmp/bbb',
    ]


# Generated at 2022-06-13 05:06:21.710623
# Unit test for method remove_env of class CronTab
def test_CronTab_remove_env():
    """Tests remove_env method"""

    cron = CronTab(None)
    cron.lines = ['MY_ENV=foo', 'MY_ENV2=bar', 'another_env=baz']
    cron.remove_env('MY_ENV')
    assert cron.lines == ['MY_ENV2=bar', 'another_env=baz']


# Generated at 2022-06-13 05:06:24.555008
# Unit test for function main
def test_main():
    print("in test_main")

# Generated at 2022-06-13 05:08:23.751341
# Unit test for method get_cron_job of class CronTab
def test_CronTab_get_cron_job():
    test_module = AnsibleModule(argument_spec={})
    test_class = CronTab(test_module)
    # TODO: Fix this test
    # result = test_class.get_cron_job('*', '*', '*', '*', '*', 'test1', '@daily', False)
    # assert result == "* * * * * test1"
    # result = test_class.get_cron_job('*', '*', '*', '*', '*', 'test2', '@reboot', True)
    # assert result == "#@reboot test2"
    # result = test_class.get_cron_job('*', '*', '*', '*', '*', 'test3', 'test4', False)
    # assert result == "* * * * * test3

# Generated at 2022-06-13 05:08:28.393748
# Unit test for method add_job of class CronTab
def test_CronTab_add_job():
    from ansible.module_utils.six import StringIO

    stdout = StringIO()
    sys.stdout = stdout

    user = "testuser"
    crontab = CronTab(user=user)

    crontab.add_job("test", "*/5 * * * * /bin/test")

    assert len(crontab.lines) == 2, "expected two lines in cron file"


# Generated at 2022-06-13 05:08:34.118111
# Unit test for method render of class CronTab
def test_CronTab_render():
    crontab = CronTab(None)
    crontab.lines = ['0', '1', '2']

    # Test render with no comments
    if crontab.render() != '0\n1\n2\n':
        raise ValueError("CronTab.render() test failed")

    # Test render with comments
    crontab.lines = ['# Ansible: 0', '0', '# Ansible: 1', '1', '2']
    if crontab.render() != '# Ansible: 0\n0\n# Ansible: 1\n1\n2\n':
        raise ValueError("CronTab.render() test failed")

    # Test render with comments

# Generated at 2022-06-13 05:08:40.995844
# Unit test for method add_job of class CronTab
def test_CronTab_add_job():
    crontab = CronTab()
    crontab.lines = [""]
    crontab.add_job( "test", "* * * * * /usr/bin/foo")
    assert crontab.lines == ["", "#Ansible: test", "* * * * * /usr/bin/foo"]


# Generated at 2022-06-13 05:08:44.414640
# Unit test for method write of class CronTab
def test_CronTab_write():
    # test 1
    user = None
    cron_file = None
    ct = CronTab(user, cron_file)
    assert 'crontab' == ct.cron_cmd


# Generated at 2022-06-13 05:08:46.691254
# Unit test for method do_add_env of class CronTab
def test_CronTab_do_add_env():
    crontab = CronTab()
    assert crontab.do_add_env([], "a") == None, 'dont do anything'


# Generated at 2022-06-13 05:08:54.608879
# Unit test for method render of class CronTab
def test_CronTab_render():
    from ansible.compat.tests import unittest

    class TestCronTabRender(unittest.TestCase):

        def test_render_with_job(self):
            cron_tab = CronTab(None)
            cron_tab.lines = [
                '#Ansible: job1',
                '* * * * * /usr/bin/foo',
                '#Ansible: job2',
                '* * * * * /usr/bin/bar'
            ]
            self.assertEqual("""#Ansible: job1
* * * * * /usr/bin/foo
#Ansible: job2
* * * * * /usr/bin/bar
""", cron_tab.render())

        def test_render_without_job(self):
            cron_tab = CronTab

# Generated at 2022-06-13 05:09:05.222011
# Unit test for method update_job of class CronTab
def test_CronTab_update_job():
    c = CronTab()
    c.lines = [
        'line 1',
        'line 2',
        'line 3',
        'line 4'
    ]

    # This should return true and have no effect
    assert c.update_job('foo', 'test1') == True
    assert c.lines == [
        'line 1',
        'line 2',
        'line 3',
        'line 4'
    ]

    c.lines = [
        '#Ansible: foo',
        'line 1',
        'line 2',
        'line 3',
        'line 4'
    ]

    # This should return true and remove the comment and job
    assert c.remove_job('foo') == True

# Generated at 2022-06-13 05:09:07.248528
# Unit test for method do_add_job of class CronTab
def test_CronTab_do_add_job():
    my_CronTab = CronTab(module, user, cron_file)
    my_CronTab.do_add_job(lines, comment, job)


# Generated at 2022-06-13 05:09:15.424651
# Unit test for method update_job of class CronTab
def test_CronTab_update_job():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.compat.tests import unittest

    class FakeModule(AnsibleModule):

        def _get_bin_path(self, arg, required=True):
            return "/bin/crontab"

        def get_bin_path(self, arg, required=True):
            return self._get_bin_path(arg, required)


    class FakeRunCommand(object):

        def __init__(self, rc, out, err):
            self.rc = rc
            self.out = out
            self.err = err

        def __call__(self, arg, use_unsafe_shell=True):
            return (self.rc, self.out, self.err)

