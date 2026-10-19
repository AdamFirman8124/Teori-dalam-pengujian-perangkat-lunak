

# Generated at 2022-06-13 05:03:15.233463
# Unit test for method add_job of class CronTab
def test_CronTab_add_job():
    assert True



# Generated at 2022-06-13 05:03:19.638751
# Unit test for method do_add_job of class CronTab
def test_CronTab_do_add_job():
    input = ['foo']
    output = CronTab.do_add_job(input, 'bar', 'foobar')
    assert output is None
    assert input == ['foo', 'bar', 'foobar']


# Generated at 2022-06-13 05:03:27.117687
# Unit test for method find_env of class CronTab
def test_CronTab_find_env():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True, type='str'),
            special=dict(required=False, choices=CRON_SPECIAL_TIME),
            minute=dict(required=False, type='str'),
            hour=dict(required=False, type='str'),
            day=dict(required=False, type='str'),
            month=dict(required=False, type='str'),
            weekday=dict(required=False, type='str'),
            job=dict(required=True, type='str'),
        ),
        supports_check_mode=True
    )

    ct = CronTab(module, cron_file='/etc/cron.d/crontest')
    got = ct.find_env('MAILTO')

# Generated at 2022-06-13 05:03:34.346890
# Unit test for method read of class CronTab
def test_CronTab_read():
    class DummyModule(object):
        @staticmethod
        def get_bin_path(binary, required=False):
            return binary

        @staticmethod
        def run_command(args, use_unsafe_shell=False):
            return (1, "", "")

        @staticmethod
        def fail_json(msg):
            return msg

    cron_tab = CronTab(DummyModule(), user=None, cron_file=None)
    assert cron_tab.read() is None

# Generated at 2022-06-13 05:03:45.678190
# Unit test for method is_empty of class CronTab
def test_CronTab_is_empty():
    # Test case for empty list
    crontab = CronTab('', '', '')
    crontab.lines = []
    assert crontab.is_empty() is True

    # Test case for non-empty list
    crontab = CronTab('', '', '')
    crontab.lines = ['#Ansible: test', '60 1 * * * test']
    assert crontab.is_empty() is False

    # Test case for non-empty list with only comments
    crontab = CronTab('', '', '')
    crontab.lines = ['#']
    assert crontab.is_empty() is False


# Generated at 2022-06-13 05:03:51.116389
# Unit test for method update_job of class CronTab
def test_CronTab_update_job():

    module = AnsibleModule({'name': 'foo', 'special_time': 'reboot', 'job': '/bin/bar', 'user': 'root', 'state': 'present'}, check_invalid_arguments=False)
    cron = CronTab(module, user='root')
    cron.update_job('foo', '/bin/bar')

    assert '/bin/bar' in cron.render()



# Generated at 2022-06-13 05:03:55.422357
# Unit test for method update_env of class CronTab
def test_CronTab_update_env():
    cron = CronTab(module)
    cron.lines = [
        'MINUTE=1',
    ]

    cron._update_env('MINUTE', 'MINUTE=5', cron.do_add_env)
    assert cron.lines == ['MINUTE=5'], 'Expected %r == %r' % (['MINUTE=5'], cron.lines)

# Generated at 2022-06-13 05:04:04.371254
# Unit test for method write of class CronTab
def test_CronTab_write():
    module = AnsibleModule(
        argument_spec=dict(
            user=dict(default=None),
            cron_file=dict(default=None),
            backup=dict(default=False, type='bool')
        ),
        supports_check_mode=True
    )
    m = module
    c = CronTab(m)
    c.write()
    res = []
    res.append(m._ansible_sys_executed_command)
    assert res[0] == 'cat ', res


# Generated at 2022-06-13 05:04:14.669832
# Unit test for method do_add_job of class CronTab
def test_CronTab_do_add_job():

    # additional imports for the unittest
    import ansible.utils
    import ansible.utils.template
    from ansible.module_utils.six import PY3

    # Place to store original values of imported modules/functions
    original_utils = None
    original_utils_template = None
    original___builtin__ = None
    original_json = None

    # Unittest class
    class TestCronTab(unittest.TestCase):

        @classmethod
        def setUpClass(cls):
            # Restore the original values of imported modules/functions
            global original_utils
            global original_utils_template
            global original___builtin__
            global original_json

            if original_utils is None:
                original_utils = ansible.utils
            ansible.utils = utils

# Generated at 2022-06-13 05:04:20.756740
# Unit test for method get_cron_job of class CronTab
def test_CronTab_get_cron_job():
    # Initialize required variable for calling get_cron_job
    minute = '0'
    hour = '1'
    day = '2'
    month = '3'
    weekday = '4'
    job = 'foo'
    special = 'reboot'
    disabled = True

    # Test
    crontabobj = CronTab()
    cronjob = crontabobj.get_cron_job(minute, hour, day, month, weekday, job, special, disabled)

    # Test assertion
    assert cronjob == '@reboot foo' or cronjob == '#@reboot foo' or cronjob == '# @reboot foo'

# Generated at 2022-06-13 05:05:25.626337
# Unit test for method do_add_job of class CronTab

# Generated at 2022-06-13 05:05:34.456145
# Unit test for method remove_job_file of class CronTab
def test_CronTab_remove_job_file():
    from ansible.module_utils import basic

    module = basic.AnsibleModule(
        argument_spec={
            'backup': {'type': 'bool', 'default': False},
            'cron_file': {'type': 'path'},
            'user': {'type': 'str'}
        },
        supports_check_mode=True
    )

    crontab_mo = CronTab(module, user=None, cron_file=None)

    assert crontab_mo.remove_job_file() == False



# Generated at 2022-06-13 05:05:39.209365
# Unit test for method do_comment of class CronTab
def test_CronTab_do_comment():
    filename = '/tmp/crontab'
    if os.path.exists(filename):
        os.remove(filename)

    tempfh, path = tempfile.mkstemp()
    f = os.fdopen(tempfh, 'wb')
    f.write(to_bytes("@daily test\n"))
    f.close()

    ct = CronTab(None, cron_file=filename)
    ct.n_existing = ct.render()
    ct.lines = ct.render().splitlines()
    name = 'test'
    job = 'test'

    ct.add_job(name, job)

    assert ct.do_comment(name) == '#Ansible: ' + name
    assert ct.lines[0] == '#Ansible: ' + name


# Generated at 2022-06-13 05:05:43.400446
# Unit test for method do_comment of class CronTab
def test_CronTab_do_comment():
    ct = CronTab(None)
    assert ct.do_comment("hello") == "#Ansible: hello"
    assert ct.do_comment("hello") != "#Ansible hello"
    assert ct.do_comment("hello") != "Ansible: hello"
    assert ct.do_comment("hello") != "#Ansible: hello\n"
    assert ct.do_comment("hello") != "# Ansible: hello"
    assert ct.do_comment("hello") != "#Ansible:  hello"



# Generated at 2022-06-13 05:05:45.580753
# Unit test for method get_jobnames of class CronTab
def test_CronTab_get_jobnames():
    cron = CronTab("user")
    assert cron.get_jobnames() == []
    cron = CronTab("user", cron_file="/tmp/ansible_cron")
    assert cron.get_jobnames() == []


# Generated at 2022-06-13 05:05:49.383091
# Unit test for method get_envnames of class CronTab
def test_CronTab_get_envnames():
    c = CronTab(module, user="root")
    assert_equals(c.get_envnames(), [])
    c.add_env("JOB=test", insertafter="MAILTO=")
    assert_equals(len(c.get_envnames()), 2)
    assert_equals(c.get_envnames(), ["MAILTO", "JOB"])
    c.remove_env("JOB")
    assert_equals(c.get_envnames(), ["MAILTO"])


# Generated at 2022-06-13 05:05:57.145184
# Unit test for method update_job of class CronTab
def test_CronTab_update_job():
    cron_tab = CronTab()
    assert cron_tab.lines == []
    cron_tab.lines = ['# test', '* * * * * ansible']
    assert cron_tab.lines == ['# test', '* * * * * ansible']
    cron_tab.update_job('test', '* * * * * ansible2')
    assert cron_tab.lines == ['# test', '* * * * * ansible2']


# Generated at 2022-06-13 05:06:02.456793
# Unit test for method remove_job_file of class CronTab
def test_CronTab_remove_job_file():
    my_crontab = CronTab(use_sudo=True, user='root')
    assert len(my_crontab.lines) != 0

    my_crontab.remove_job_file()

    my_crontab = CronTab(use_sudo=True, user='root')
    assert len(my_crontab.lines) == 0


# Generated at 2022-06-13 05:06:04.511489
# Unit test for method render of class CronTab
def test_CronTab_render():
    ct = CronTab()
    ct.lines = ['a', 'b']
    assert ct.render() == 'a\nb\n'

# Generated at 2022-06-13 05:06:05.367088
# Unit test for method get_cron_job of class CronTab
def test_CronTab_get_cron_job():
    pass

# Generated at 2022-06-13 05:08:09.348543
# Unit test for method do_comment of class CronTab
def test_CronTab_do_comment():
    ct = CronTab(Module(), 'root')
    assert ct.do_comment('test') == '#Ansible: test'



# Generated at 2022-06-13 05:08:15.632791
# Unit test for constructor of class CronTab
def test_CronTab():
    c = CronTab(None, 'h', 'f')
    assert c.user == 'h'
    assert c.cron_file == '/etc/cron.d/f'
    assert c.root

    c = CronTab(None, 'h')
    assert c.user == 'h'
    assert not c.cron_file
    assert c.root

    c = CronTab(None)
    assert c.user is None
    assert not c.cron_file
    assert c.root



# Generated at 2022-06-13 05:08:24.178776
# Unit test for method render of class CronTab
def test_CronTab_render():
    module = AnsibleModule(argument_spec=dict())

    cron_tab = CronTab(module)
    cron_tab.lines.append('* * * * * *')
    cron_tab.lines.append('*/20 * * * * *')
    cron_tab.lines.append('@reboot foo')
    cron_tab.lines.append('')

    assert cron_tab.render() == "* * * * * *\n*/20 * * * * *\n@reboot foo\n"


# Generated at 2022-06-13 05:08:31.342057
# Unit test for method add_env of class CronTab
def test_CronTab_add_env():
    ct = CronTab()

    ct.lines = [
        "SHELL=/bin/sh",
        "PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin",
        "LANG=en_US.UTF-8",
        "MAILTO=",
        "HOME=/root",
        "* * * * * root echo \"Hello world\""]
    ct.add_env("EDITOR=vi")
    assert ct.lines[0] == "EDITOR=vi"
    assert ct.lines[1] == "SHELL=/bin/sh"
    assert ct.lines[2] == "PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin"
    assert ct.lines

# Generated at 2022-06-13 05:08:35.556157
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes

    import stat
    import shutil
    import tempfile

    # get the comment and jobs defined in cron_file
    cron_file = "/tmp/crontab.jason"
    crontab = CronTab(None, None, cron_file)
    # print crontab.render()
    # /usr/bin/who
    # /usr/bin/foo
    crontab.lines = ['* * * * * /usr/bin/who', '# Ansible: /usr/bin/foo']
    crontab.write()

    # set all the needed module args, the normal stuff

# Generated at 2022-06-13 05:08:41.818482
# Unit test for method render of class CronTab
def test_CronTab_render():
    lines = ['#Ansible: 1', '0 1 2 3 4 /bin/true']

    # init crontab
    ct = CronTab(user='test')

    # set lines
    ct.lines = lines

    # render
    result = ct.render()

    # test render
    assert result == '\n'.join(lines) + '\n'

# Generated at 2022-06-13 05:08:43.958587
# Unit test for method remove_job_file of class CronTab
def test_CronTab_remove_job_file():
    ct = CronTab(1, "test_user", None)
    assert ct.remove_job_file() == False

# Generated at 2022-06-13 05:08:47.561198
# Unit test for method get_envnames of class CronTab
def test_CronTab_get_envnames():
    obj = create_CronTab()
    obj.lines = [ to_bytes(u'PATH=/bin:/sbin:/usr/bin:/usr/sbin'),
                  to_bytes(u'TESTVAR=value') ]
    assert obj.get_envnames() == ['PATH', 'TESTVAR']

# Generated at 2022-06-13 05:08:55.196485
# Unit test for method do_remove_env of class CronTab
def test_CronTab_do_remove_env():
  b_cron_file = os.path.join(b'/etc/cron.d', to_bytes('cron_file.txt', errors='surrogate_or_strict'))
  module = Mock()
  module.run_command = Mock(return_value=0)
  module.get_bin_path = Mock(return_value='/usr/bin/crontab')
  module.selinux_enabled = Mock()
  module.set_default_selinux_context = Mock(return_value=0)
  cron = CronTab(module, user='user', cron_file='cron_file.txt')
  lines = []
  decl = 'my_var=some_value'
  cron.do_remove_env(lines, decl)
  assert lines == []


# Generated at 2022-06-13 05:08:57.224974
# Unit test for method get_envnames of class CronTab
def test_CronTab_get_envnames():
    try:
        crontab = CronTab(None)
    except NameError:
        crontab = object
    assert crontab.get_envnames() == []
