

# Generated at 2022-06-13 05:03:22.655170
# Unit test for method get_cron_job of class CronTab
def test_CronTab_get_cron_job():
    class MockModule:
        class MockParams:
            def __init__(self):
                self.name   = 'tomcat'
                self.minute = '0'
                self.hour   = '0'
                self.day    = '*'
                self.month  = '*'
                self.weekday = '*'
                self.job    = '/root/tomcat_restart.sh'
                self.state  = 'present'
                self.special_time  = 'reboot'
                self.cron_file  = '/etc/cron.d/tomcat'
                self.disabled    = True

        def __init__(self):
            self.fail_json = print
            self.params = self.MockParams()


    ct = CronTab(MockModule())

# Generated at 2022-06-13 05:03:26.574346
# Unit test for method update_env of class CronTab
def test_CronTab_update_env():
    ct = CronTab('/etc/cron.d')
    ct.update_env('PATH', 'PATH=/usr/bin')
    assert ct.lines == ['PATH=/usr/bin'], ct.lines


# Generated at 2022-06-13 05:03:39.254886
# Unit test for method find_job of class CronTab
def test_CronTab_find_job():
    # Testing string to create the crontab object
    cron_string = """
#Ansible: test_job
* * * * * ls -a

#Ansible: test_job_2
* * * * * ls -b



#Ansible: test_job_3
* * * * * ls -c


"""
    # Create CronTab object from string
    cron_obj = CronTab(module=None, user=None, cron_file=None)
    cron_obj.lines = cron_string.splitlines()

    # Testing the find_job for Ansible: test_job
    result = cron_obj.find_job('test_job', None)
    assert result == ['#Ansible: test_job', '* * * * * ls -a']

    # Testing the find

# Generated at 2022-06-13 05:03:39.903990
# Unit test for method remove_job_file of class CronTab
def test_CronTab_remove_job_file():
    CronTab('/foo')


# Generated at 2022-06-13 05:03:51.155694
# Unit test for method find_job of class CronTab
def test_CronTab_find_job():
    module = AnsibleModule(
        argument_spec = dict(
            hour        = dict(default='0'),
            minute      = dict(default='0'),
            job         = dict(default='ls'),
            name        = dict(default=None),
            special     = dict(default=None),
            state       = dict(default='present'),
        )
    )

    # test find_job with name and no job
    cron = CronTab(module)
    r_job = cron.find_job("ls")
    assert r_job == []

    # test find_job with job and no name
    cron = CronTab(module, cron_file='ansible_test')
    module.write_file(cron.cron_file, "* * * * * ls")
    cron.read()
    r_

# Generated at 2022-06-13 05:03:53.640604
# Unit test for method do_remove_env of class CronTab
def test_CronTab_do_remove_env():
    ct = CronTab(None, None)
    decl = 'a=1'
    lines = ['a=1']
    assert ct.do_remove_env(lines, decl) == None



# Generated at 2022-06-13 05:03:58.608620
# Unit test for method is_empty of class CronTab
def test_CronTab_is_empty():
    ct = CronTab(None)
    assert ct.is_empty()
    ct.lines.append('test')
    assert not ct.is_empty()
    ct.lines.append('   ')
    assert not ct.is_empty()



# Generated at 2022-06-13 05:03:59.998314
# Unit test for method add_job of class CronTab
def test_CronTab_add_job():
    assert False


# Generated at 2022-06-13 05:04:04.731391
# Unit test for method do_comment of class CronTab
def test_CronTab_do_comment():
    test_module = AnsibleModule(argument_spec={})

    expected_result = '#Ansible: test_job'
    result = CronTab(test_module, 'ansible', None).do_comment('test_job')

    assert result == expected_result


# Generated at 2022-06-13 05:04:09.776701
# Unit test for method get_envnames of class CronTab
def test_CronTab_get_envnames():
    crontab = CronTab(None)
    """
        Tests for get_envnames()
    """
    lines = ['#Ansible', 'PATH=path:path']
    crontab.lines = lines
    assert crontab.get_envnames() == ['PATH']


# Generated at 2022-06-13 05:05:07.708168
# Unit test for method find_job of class CronTab
def test_CronTab_find_job():
    v = CronTab(None)
    v.lines = [
        '#Ansible: foo',
        '* * * * * root echo hello',
        '* * * * * root echo bar',
        '#Ansible: bar',
        '* * * * * root echo hello',
    ]
    assert v.find_job('foo', '* * * * * root echo hello') == ['foo', '* * * * * root echo hello']
    assert v.find_job('foo', '* * * * * root echo bar') == []
    assert v.find_job('bar', '* * * * * root echo hello') == ['bar', '* * * * * root echo hello']
    assert v.find_job('bar', '* * * * * root echo bar') == []

# Generated at 2022-06-13 05:05:16.361920
# Unit test for method get_jobnames of class CronTab
def test_CronTab_get_jobnames():
    test_lines = [
        '#Ansible: test1',
        '0       1       2       3       4       5       alias awk basename cat chgrp chmod',
        '#Ansible: test2',
        '0       1       2       3       4       5       alias awk basename cat chgrp chmod',
        '#Ansible: test3',
        '0       1       2       3       4       5       alias awk basename cat chgrp chmod'
    ]
    ct = CronTab(module=FakeModule(), user='', cron_file='')
    ct.lines = test_lines
    result = ct.get_jobnames()
    assert result == ['test1', 'test2', 'test3']

# Generated at 2022-06-13 05:05:22.876965
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule

    ansible_args = dict(
        name="my job",
        user="someuser",
        job="/some/dir/job.sh",
        state="present",
        backup=False,
        minute="8",
        hour="5",
        day="2",
        month="*",
        weekday="*",
        special_time="reboot",
        disabled=False,
        env=False,
        insertafter=None,
        insertbefore=None,
    )

    test_args = dict(
        ANSIBLE_MODULE_ARGS=ansible_args
    )

    module = AnsibleModule(test_args)
    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:05:34.457796
# Unit test for method remove_job of class CronTab
def test_CronTab_remove_job():
    # Test import fail
    try:
        import crontab
    except ImportError:
        try:
            import cron
        except ImportError:
            import croniter
        else:
            import cron
    else:
        import crontab


# Generated at 2022-06-13 05:05:39.161020
# Unit test for method remove_env of class CronTab
def test_CronTab_remove_env():
    class ModuleStub(object):
        pass
    module = ModuleStub()

    class RunCommandStub():
        def __init__(self):
            self.rc = 0
            self.out = ""
            self.err = ""

        def __call__(self, args, use_unsafe_shell=False):
            return (self.rc, self.out, self.err)

    module.run_command = RunCommandStub()
    module.get_bin_path = lambda path: path
    cron = CronTab(module)

    cron.lines = ["#Ansible: env-var-name", "env-var-name=var-value", "not-an-env-var=value"]
    cron.remove_env("env-var-name")

# Generated at 2022-06-13 05:05:40.571572
# Unit test for method find_env of class CronTab
def test_CronTab_find_env():
    with pytest.raises(CronTabError):
        c = CronTab(None)
        c.find_env("TEST")

# Generated at 2022-06-13 05:05:42.302679
# Unit test for method remove_job_file of class CronTab
def test_CronTab_remove_job_file():
    module = AnsibleModule(
        argument_spec = dict()
    )
    crontab_obj = CronTab(module)

    assert crontab_obj.remove_job_file() == False


# Generated at 2022-06-13 05:05:51.159168
# Unit test for method get_jobnames of class CronTab
def test_CronTab_get_jobnames():

    # Setup test CronTab object
    module = mock.MagicMock()

    module.get_bin_path.return_value = '/usr/bin/crontab'
    m = mock.mock_open(read_data='42 2 * * * root echo pong')
    module.run_command.return_value = (0, None, None)
    module.selinux_enabled.return_value = False
    with mock.patch('ansible.module_utils.six.moves.builtins.open', m):
        cron = CronTab(module, 'root')

    # Run method to be tested
    jobnames = cron.get_jobnames()

    # Assertions
    assert jobnames == []



# Generated at 2022-06-13 05:06:02.958895
# Unit test for method find_job of class CronTab
def test_CronTab_find_job():
    f = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_crontab_file"), mode='r')
    ct = CronTab(None, cron_file=f)
    f.close()
    job = ct.find_job("test")
    print("test_CronTab_find_job: test1=%s" % job)
    assert job[0] == "#Ansible: test"
    assert job[1] == "0,20,40 * * * 1-5 /usr/bin/echo 'test' > /tmp/test.txt"
    job = ct.find_job("test", "0,20,40 * * * 1-5 /usr/bin/echo 'test' > /tmp/test.txt")

# Unit

# Generated at 2022-06-13 05:06:12.132639
# Unit test for method update_env of class CronTab
def test_CronTab_update_env():
    mymock = Mock(return_value=None)
    with patch.object(CronTab, '_update_env', mymock):
        crontab = CronTab()
        crontab.update_env('name', 'declaration')
        assert mymock.call_args[0][0] == 'name'
        assert mymock.call_args[0][1] == 'declaration'
        assert mymock.call_args[0][2].__name__ == 'do_add_env'


# Generated at 2022-06-13 05:08:06.630418
# Unit test for method update_job of class CronTab
def test_CronTab_update_job():
    # All needed imports
    from ansible_collections.notstdlib.moveitallout.tests.units.compat import unittest

    def do_add_job(self, lines, comment, job):
        lines.append(comment)

        lines.append("%s" % (job))

    with unittest.mock.patch('ansible_collections.notstdlib.moveitallout.plugins.modules.crontab.CronTab.do_add_job') as mock_do_add_job:
        # Make the test
        ct = CronTab(None, None, None)
        ct.do_add_job = do_add_job.__get__(ct, CronTab)

# Generated at 2022-06-13 05:08:14.439361
# Unit test for method remove_env of class CronTab
def test_CronTab_remove_env():
    # test 1
    ct = CronTab(None, cron_file = '/etc/mytab')
    cron_entry = CronSlices('@hourly echo hello',['@','','','','','','','','', 'echo hello'])
    jobname = 'myjob'
    ct.find_job(jobname, cron_entry.raw)
    ct.remove_env('test_env')
    assert len(ct.find_env('test_env')) == 0
    assert len(ct.find_job(jobname)) == 0


# Generated at 2022-06-13 05:08:18.224374
# Unit test for method update_env of class CronTab
def test_CronTab_update_env():
    for item in update_env_data:
        yield check_update_env, item['name'], item['decl'], item['insertafter'], item['insertbefore'], item['expected']


# Generated at 2022-06-13 05:08:28.076484
# Unit test for method update_env of class CronTab
def test_CronTab_update_env():
    import tempfile
    import shutil
    import tempfile
    import os
    import os.path
    import subprocess
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes, to_native
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.parsing.convert_bool import BOOLEAN_TRUE_STRINGS, BOOLEAN_FALSE_STRINGS, boolean
    from ansible.module_utils.urls import open_url, fetch_url
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.six.moves.urllib.parse import urlencode

# Generated at 2022-06-13 05:08:34.900216
# Unit test for method add_job of class CronTab
def test_CronTab_add_job():
    """
    Test method add_job of class CronTab
    """
    module = ansible_module_cron()
    # Add a job
    ct = CronTab(module)
    ct.add_job('test', 'echo "TEST"')
    assert len(ct.lines) == 2
    assert ct.lines[0] == ct.do_comment('test')
    assert ct.lines[1] == 'echo "TEST"'
    # Add another job
    ct = CronTab(module)
    ct.add_job('test', 'echo "TEST"')
    ct.add_job('test2', 'echo "TEST2"')
    assert len(ct.lines) == 4
    assert ct.lines[0] == ct.do_comment('test')
    assert c

# Generated at 2022-06-13 05:08:40.077454
# Unit test for method remove_env of class CronTab
def test_CronTab_remove_env():
    args = dict(
        name='test',
    )
    obj = CronTab(module=AnsibleModule(argument_spec={}), cron_file='test.crontab')
    obj.remove_env(**args)
    assert True



# Generated at 2022-06-13 05:08:44.490404
# Unit test for method do_add_env of class CronTab
def test_CronTab_do_add_env():
    args = dict(
        lines = ['LINE1'],
        decl = 'LINE2',
        )
    expected = ['LINE1', 'LINE2']
    current = CronTab.do_add_env(**args)
    assert current == expected


# Generated at 2022-06-13 05:08:46.162802
# Unit test for method do_add_env of class CronTab
def test_CronTab_do_add_env():
    assert CronTab(None, None, None).do_add_env([], "") == None


# Generated at 2022-06-13 05:08:53.220746
# Unit test for method find_env of class CronTab
def test_CronTab_find_env():
    crontab = CronTab(None, 'root')
    last_env = crontab.lines[-1]
    last_env_name = last_env.split('=')[0]
    last_env_value = last_env.split('=')[1]
    last_index = len(crontab.lines) - 1
    env_found = crontab.find_env(last_env_name)
    assert env_found[0] == last_index
    assert env_found[1] == last_env
    assert crontab.find_env('NON_EXISTING_ENVIRONMENT_VARIABLE') == []


# Generated at 2022-06-13 05:08:56.040760
# Unit test for method do_add_env of class CronTab
def test_CronTab_do_add_env():
    cron_tab = CronTab()
    lines = []
    decl = 'foo=bar'
    cron_tab.do_add_env(lines, decl)
    assert lines == ['foo=bar']

