

# Generated at 2022-06-13 05:03:18.825440
# Unit test for method is_empty of class CronTab
def test_CronTab_is_empty():
    m = MagicMock()
    ct = CronTab(m, user=None, cron_file=None)
    out = ct.is_empty()
    assert out == True, "Should be equal"


# Generated at 2022-06-13 05:03:31.981598
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.pycompat24 import get_exception
    #from ansible.module_utils.six import StringIO
    import os
    #import sys
    import tempfile
    import time

# Generated at 2022-06-13 05:03:38.093661
# Unit test for method find_env of class CronTab
def test_CronTab_find_env():
    # Note that this unit test relies on site.py which is not very reliable in
    # Python 2.6
    from crontab import CronTab
    from ansible.module_utils.basic import AnsibleModule

    m = AnsibleModule(argument_spec={})
    test_cron = CronTab(m)
    test_cron.lines = ['abc=def', 'ghi=jkl']
    # Test: find existing variable
    assert test_cron.find_env('abc') == [0, 'abc=def']
    # Test: find non-existent variable
    assert test_cron.find_env('foo') == []



# Generated at 2022-06-13 05:03:38.819087
# Unit test for method render of class CronTab
def test_CronTab_render():
    assert True == True

# Generated at 2022-06-13 05:03:48.438541
# Unit test for method update_job of class CronTab
def test_CronTab_update_job():
    import tempfile

    # Create a temporary file
    fd, path = tempfile.mkstemp()
    os.close(fd)
    crontab = CronTab(None)
    # Create a file
    crontab.write(backup_file=path)

    old_lines = crontab.lines
    crontab.update_job("test", "job")
    assert (len(old_lines) + 2 == len(crontab.lines))
    crontab.update_job("test", "job")
    assert (len(old_lines) + 2 == len(crontab.lines)) == True


# Generated at 2022-06-13 05:03:52.585216
# Unit test for method do_remove_job of class CronTab
def test_CronTab_do_remove_job():
  input=CronTab('module', user=None, cron_file=None)
  input.lines=['abc']
  res=input.do_remove_job(['abc'],'abc','abc')
  assert res is None

test_CronTab_do_remove_job()

# Generated at 2022-06-13 05:04:04.373799
# Unit test for method write of class CronTab
def test_CronTab_write():

    # create temporary directory
    tmpdir = tempfile.mkdtemp()

    # create CronTab object
    crontab = CronTab(tmpdir, False)

    # write the crontab
    crontab.write(False)

    # check the file existence
    assert os.path.isfile(os.path.join(tmpdir, 'crontab'))

    # check the file size
    assert os.stat(os.path.join(tmpdir, 'crontab')).st_size == 0

    # remove the temporary directory
    shutil.rmtree(tmpdir)


if __name__ == '__main__':
    test_CronTab_write()

# Generated at 2022-06-13 05:04:07.028330
# Unit test for method remove_job of class CronTab
def test_CronTab_remove_job():

    # TODO: Make this unit test
    c = CronTab()
    c.read()
    pass

# Generated at 2022-06-13 05:04:10.629043
# Unit test for method write of class CronTab
def test_CronTab_write():
    module = AnsibleModule(
        argument_spec = dict(
            backup = dict(type='bool', required=False),
        ),
        supports_check_mode=False
    )
    ct = CronTab(module=module)
    ct.write()


# Generated at 2022-06-13 05:04:16.252694
# Unit test for method find_job of class CronTab
def test_CronTab_find_job():
    print("Testing method find_job of class CronTab")
    try:
        my = CronTab()
        # my = CronTab(cron_file='/etc/cron.d/test.txt')
        my.read()
    except Exception:
        print("\tEXCEPTION CAUGHT DURING TESTING")
        raise
    else:
        print("\tNO EXCEPTION RAISED")
    print("\tDone testing method find_job of class CronTab")

# Generated at 2022-06-13 05:05:12.602079
# Unit test for method add_env of class CronTab
def test_CronTab_add_env():
    from ansible.module_utils import basic
    module = basic.AnsibleModule(
        argument_spec = dict()
    )
    c = CronTab(module)
    c.add_env('testname=testdecl')
    assert c.lines[0] == 'testname=testdecl'



# Generated at 2022-06-13 05:05:19.654522
# Unit test for method add_env of class CronTab
def test_CronTab_add_env():
    """
    Test CronTab.add_env()
    """
    #unit test for add_env

# Generated at 2022-06-13 05:05:22.122562
# Unit test for method get_jobnames of class CronTab
def test_CronTab_get_jobnames():
    ct = CronTab('', cron_file='test_cron_file')

    assert ct.get_jobnames() == ['test_jobname_1', 'test_jobname_2']



# Generated at 2022-06-13 05:05:32.915841
# Unit test for method remove_env of class CronTab
def test_CronTab_remove_env():
    # crontab, to be removed
    test_crontab = CronTab(module=None, cron_file='cron_remove')

    # environment variable
    env_name = 'MYVAR'
    env_value = 'MYVAL'
    env_decl = '%s=%s' % (env_name, env_value)

    # add environment variable
    test_crontab.add_env(env_decl)

    # remove environment variable
    test_crontab.remove_env(env_name)

    # assert that environment variable is removed
    env_names = test_crontab.get_envnames()
    assert env_name not in env_names



# Generated at 2022-06-13 05:05:44.336459
# Unit test for method find_env of class CronTab
def test_CronTab_find_env():
    '''
    Unit test for method find_env of class CronTab
    '''

    module = MagicMock()
    module.selinux_enabled.return_value = True

    crontab = CronTab(module)

# Generated at 2022-06-13 05:05:48.258878
# Unit test for method read of class CronTab
def test_CronTab_read():
    module = AnsibleModule(
        argument_spec = dict(
            user     = dict(default=None),
            cron_file= dict(default=None),
         ),
    )
    cron = CronTab(module)
    cron.read()

# Generated at 2022-06-13 05:05:55.222294
# Unit test for method write of class CronTab
def test_CronTab_write():
    out = sys.stdout
    err = sys.stderr
    try:
        content = read_file('unit_test_cron_tab_write.json')
        sys.stdout = open('/dev/null', 'w')
        sys.stderr = open('/dev/null', 'w')
        module_args = json.loads(content)
        c = CronTab(module_args)
        c.write()
        sys.stdout.flush()
        sys.stderr.flush()
    finally:
        sys.stdout = out
        sys.stderr = err
        try:
            os.remove('/tmp/tmphc5njrzr.cron')
        except OSError:
            pass


# Generated at 2022-06-13 05:06:00.703432
# Unit test for method is_empty of class CronTab
def test_CronTab_is_empty():
    c = CronTab(None)
    if len(c.lines) == 0:
        assert c.is_empty() == True
    else:
        for line in c.lines:
            if not line.strip():
                assert c.is_empty() == True
            else:
                assert c.is_empty() == False


# Generated at 2022-06-13 05:06:15.288241
# Unit test for method add_job of class CronTab

# Generated at 2022-06-13 05:06:23.228940
# Unit test for method render of class CronTab
def test_CronTab_render():
    import json

    with open("./cron_test.json", "r") as f:
        test_cases = json.load(f)

    for test_case in test_cases:
        ct = CronTab(None)
        ct.lines = test_case["input"].split("\n")
        output = ct.render()
        result = output == test_case["output"]
        if test_case.get("expected", True) and not result:
            print("Test case %s failed" % test_case["name"])



# Generated at 2022-06-13 05:08:24.101382
# Unit test for method remove_job_file of class CronTab
def test_CronTab_remove_job_file():
    cr = CronTab()
    ret = cr.remove_job_file()
    assert True == ret
    cr.module.fail_json(msg='Must provide existence of a file already in memory to remove')


# Generated at 2022-06-13 05:08:29.457079
# Unit test for constructor of class CronTab
def test_CronTab():
    obj_CronTab = CronTab(module=None, user='wendy', cron_file=None)
    assert obj_CronTab.cron_cmd.endswith('crontab')
    assert obj_CronTab.user == 'wendy'
    assert obj_CronTab.lines is None
    assert obj_CronTab.ansible == '#Ansible: '
    assert obj_CronTab.n_existing == ''
    assert not obj_CronTab.cron_file


# Generated at 2022-06-13 05:08:30.945234
# Unit test for method remove_job of class CronTab
def test_CronTab_remove_job():
    ct = CronTab(user=None, cron_file=None )
    assert ct.remove_job(name="name") is None

# Generated at 2022-06-13 05:08:42.523843
# Unit test for method read of class CronTab
def test_CronTab_read():
    m = mock.MagicMock(spec=AnsibleModule)
    t = CronTab(m)

    # empty
    t.lines = None
    t.n_existing = ''
    m.run_command.return_value = ('0', 'hello', '')
    t.read()
    assert t.lines == ['hello']
    # non-empty existing
    t.lines = None
    t.n_existing = 'hello\nworld'
    t.read()
    assert t.lines == ['hello', 'world']
    # try a real file
    t.cron_file = '/bogusfile.dat'
    t.b_cron_file = to_bytes(t.cron_file)
    t.lines = None
    t.n_existing = ''
    t.read()

# Generated at 2022-06-13 05:08:47.520473
# Unit test for method get_envnames of class CronTab
def test_CronTab_get_envnames():
    x = CronTab(DummyUser())
    test_lines = [
        '#Ansible: a',
        '42 * * * * foo bar',
        'TESTING=hello world',
        'MORE_TESTING=hello world'
    ]
    x.lines = test_lines
    env_names = x.get_envnames()
    assert env_names == ['TESTING', 'MORE_TESTING']


# Generated at 2022-06-13 05:08:54.091351
# Unit test for method get_jobnames of class CronTab
def test_CronTab_get_jobnames():
   c = CronTab('', None, None)
   c.lines = ['#Ansible: my_job_1', '* * * * * echo "Hello World!"',
              '* * * * * echo "Goodbye World!"', '#Ansible: my_job_2',
              '0 12 * * * echo "Goodbye World!"', '#Ansible: my_job_3',
              '0 12 * * * echo "Goodbye World!"']

   # Successful test
   jobnames = c.get_jobnames()
   assert jobnames == ['my_job_1', 'my_job_2', 'my_job_3']



# Generated at 2022-06-13 05:08:59.318864
# Unit test for method remove_job_file of class CronTab
def test_CronTab_remove_job_file():
    # prep test
    # initialize the module, passing through any keyword arguments
    module = AnsibleModule(argument_spec={})
    path = '/tmp/cron.d/file'
    if os.path.exists(path):
        os.unlink(path)
    f = open(path, 'w')
    f.write('jobs')
    f.close()
    ct = CronTab(module=module, cron_file=path)
    # test
    assert ct.remove_job_file()
    assert not os.path.exists(path)



# Generated at 2022-06-13 05:09:10.560785
# Unit test for method find_job of class CronTab
def test_CronTab_find_job():
    ct = CronTab(None, None, None)
    ct.lines = ['', '', '#Ansible:\n', '#Ansible:\n', '#Ansible:\n', '#Ansible:\n', '#Ansible: first\n', '* * * * * ls']
    assert ct.find_job('first', '* * * * * ls') == ['#Ansible: first', '* * * * * ls']
    assert ct.find_job('first') == []
    assert ct.find_job('second', '* * * * * ls') == []
    assert ct.find_job(None, '* * * * * ls') == []
    assert ct.find_job('first', '* * * * * ls -l') == []

# Generated at 2022-06-13 05:09:15.861776
# Unit test for method do_add_job of class CronTab
def test_CronTab_do_add_job():
    module = AnsibleModule(
        argument_spec = dict(
            name = dict(required=True, type='str'),
            job = dict(required=True, type='str'),
        ),
    )
    c = CronTab(module, user=None, cron_file=None)
    c.module = module
    c.do_add_job(c.lines, "test_name", "test_job")
    assert not c.lines
    assert c.do_comment("test_name") == "#Ansible: test_name"


# Generated at 2022-06-13 05:09:17.837326
# Unit test for method remove_job_file of class CronTab
def test_CronTab_remove_job_file():
    c = CronTab('/etc/cron.d/test')
    c.remove_job_file()
    assert c.remove_job_file() == True

