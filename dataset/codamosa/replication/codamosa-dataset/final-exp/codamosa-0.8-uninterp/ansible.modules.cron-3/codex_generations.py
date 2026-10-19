

# Generated at 2022-06-13 05:03:24.120384
# Unit test for method find_job of class CronTab
def test_CronTab_find_job():
    cronit = CronTab()
    cronit.lines = ['#Ansible: test-job', '0 0 * * * /usr/bin/test']

    found = cronit.find_job('test-job')
    assert found == ['#Ansible: test-job', '0 0 * * * /usr/bin/test']

    found = cronit.find_job('test-job', '0 0 * * * /usr/bin/test')
    assert found == ['#Ansible: test-job', '0 0 * * * /usr/bin/test']

    found = cronit.find_job('not-there')
    assert found == []

    found = cronit.find_job('not-there', '1 1 * * * /usr/bin/test')
    assert found == []



# Generated at 2022-06-13 05:03:36.176722
# Unit test for function main
def test_main():
    """  Test the main function  """

    def _get_script(filename):
        return ''.join(open(
            os.path.join(os.path.dirname(__file__), 'modules/extras/cron/test/%s' % filename),
            'r').readlines())


# Generated at 2022-06-13 05:03:48.989214
# Unit test for method do_add_env of class CronTab
def test_CronTab_do_add_env():
    # Create an instance of a class
    crontab = CronTab(module=None)

    # Add a variable as the top variable
    decl = "OPT=1"
    lines = []
    crontab.do_add_env(lines, decl)
    assert lines[0] == decl

    # Add a variable after a variable named 'ANSIBLE' is defined.
    # And, the variable 'ANSIBLE' is not a variable at all.
    insertafter = 'ANSIBLE'
    decl = "OPT=2"
    lines = ["#AA"]
    crontab.do_add_env(lines, decl, insertafter=insertafter)
    assert lines[0] == "#AA"
    assert lines[1] == decl

    # Add a variable after a variable named 'ANSIBLE' is defined.
    # And, the variable

# Generated at 2022-06-13 05:04:01.368881
# Unit test for constructor of class CronTab
def test_CronTab():
    # create instance of class without parameters
    module = Mock()
    crontab = CronTab(module)
    assert crontab
    assert isinstance(crontab, CronTab)
    assert crontab.lines is None
    assert crontab.n_existing == ''
    assert crontab.root is True

    # create instance of class with parameters
    crontab = CronTab(module, 'root', '/etc/cron.d/snapshot')
    assert crontab
    assert isinstance(crontab, CronTab)
    assert crontab.lines == []
    assert crontab.n_existing == '#Ansible: snapshot\n'
    assert crontab.ansible == '#Ansible: '
    assert crontab.user == 'root'
    assert crontab.cron_

# Generated at 2022-06-13 05:04:09.122874
# Unit test for method do_add_job of class CronTab
def test_CronTab_do_add_job():
    from ansible.module_utils.basic import AnsibleModule
    m = AnsibleModule
    obj = CronTab('user', m, 'cron_file')
    lines = ['#Ansible: test_job', '0 0 1 1 0 test_job']
    name = '0 0 1 1 0 test_job'
    job = 'job'
    obj.do_add_job(lines, name, job)
    assert lines == ['#Ansible: test_job', '0 0 1 1 0 test_job']



# Generated at 2022-06-13 05:04:10.832065
# Unit test for method write of class CronTab
def test_CronTab_write():
    assert True


if __name__ == '__main__':
    test_CronTab_write()

# Generated at 2022-06-13 05:04:15.675093
# Unit test for method is_empty of class CronTab
def test_CronTab_is_empty():
    module = AnsibleModule(
        argument_spec = dict()
    )
    crontab = CronTab(module, user='nobody')
    result = crontab.is_empty()
    if result != True:
        module.fail_json(msg="Test for CronTab.is_empty() failed.", actual=result, expected=True)
    module.exit_json(changed=False)


# Generated at 2022-06-13 05:04:17.897564
# Unit test for method do_remove_job of class CronTab
def test_CronTab_do_remove_job():
    ct = CronTab(None)
    lines = []
    comment = ''
    job = ''
    assert ct.do_remove_job(lines, comment, job) == None


# Generated at 2022-06-13 05:04:24.346468
# Unit test for method remove_job of class CronTab
def test_CronTab_remove_job():
    ct = CronTab(None, None)
    ct.lines = ["1 2 3 4 5 /tmp/true", "#ansible: foo", "1 2 3 4 5 /tmp/false", "#ansible: bar", "1 2 3 4 5 /tmp/true"]
    ct.remove_job("foo")
    assert ct.lines == ["1 2 3 4 5 /tmp/true", "1 2 3 4 5 /tmp/false", "#ansible: bar", "1 2 3 4 5 /tmp/true"]
    ct.remove_job("bar")
    assert ct.lines == ["1 2 3 4 5 /tmp/true", "1 2 3 4 5 /tmp/false", "1 2 3 4 5 /tmp/true"]
    ct.remove_job("baz")

# Generated at 2022-06-13 05:04:28.479100
# Unit test for constructor of class CronTab
def test_CronTab():
    # Test basic constructor
    c = CronTab(None, 'root', 'ansible_crontab')
    assert c.user == 'root'
    assert c.root == True
    assert c.cron_file == '/etc/cron.d/ansible_crontab'


# Generated at 2022-06-13 05:05:29.811295
# Unit test for method do_remove_env of class CronTab
def test_CronTab_do_remove_env():
    m = MagicMock()
    crontab = CronTab(m)
    lines = [ 'job' ]
    decl = 'decl'
    assert crontab.do_remove_env(lines, decl) == None


# Generated at 2022-06-13 05:05:41.076241
# Unit test for method add_env of class CronTab
def test_CronTab_add_env():
    module = AnsibleModule(
        argument_spec = dict(
            insertafter  = dict(type='str'),
            insertbefore  = dict(type='str'),
            ),
        supports_check_mode=True
        )
    m_cron = CronTab(module)
    m_cron.add_env('test_CronTab_add_env')
    m_cron.write('/tmp/test')
    f = open('/tmp/test', 'rb')
    result = to_native(f.read(), errors='surrogate_or_strict').strip('\n')
    f.close()
    assert result == 'test_CronTab_add_env'


# Generated at 2022-06-13 05:05:45.081004
# Unit test for method add_job of class CronTab
def test_CronTab_add_job():
    c = CronTab()
    c.add_job('test_comment', '12 1 * * * /bin/foo')
    assert c.render() == '#Ansible: test_comment\n12 1 * * * /bin/foo\n'



# Generated at 2022-06-13 05:05:53.480231
# Unit test for method update_env of class CronTab
def test_CronTab_update_env():
    # Test if variable named 'HOME' can be updated
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.pycompat24 import get_exception
    module = AnsibleModule(argument_spec={})
    ct = CronTab()
    ct.add_env('HOME=/home/ansible')
    ct.add_env('HOME=/home/ansible/')
    ct.add_env('HOME=/home/ansible//')
    ct.add_env('HOME=/home/ansible///')
    assert 'HOME=/home/ansible' in ct.lines
    assert 'HOME=/home/ansible/' in ct.lines
    assert 'HOME=/home/ansible//' in ct.lines
    assert 'HOME=/home/ansible///' in ct

# Generated at 2022-06-13 05:06:03.589874
# Unit test for method do_add_env of class CronTab
def test_CronTab_do_add_env():
    module_args = dict(
        name='TEST_ENV', value='TEST', state='present',
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    cron = CronTab(module)
    cron.lines = ['PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin']
    cron.do_add_env(cron.lines, 'TEST_ENV=TEST')

    assert cron.lines == ['PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin', 'TEST_ENV=TEST']


# Generated at 2022-06-13 05:06:16.738613
# Unit test for method write of class CronTab
def test_CronTab_write():
    fixture = CronTab()
    fixture.write()
    assert os.path
    assert os.path.join
    assert os.path.isabs
    assert os.path.join('/etc/cron.d', cron_file)
    assert os.path.join(b'/etc/cron.d', to_bytes(cron_file, errors='surrogate_or_strict'))
    assert f
    assert f.close()
    assert rc != 0
    assert rc != 1
    assert not re.match(r'# DO NOT EDIT THIS FILE - edit the master and reinstall.', l)
    assert not re.match(r'# \(/tmp/.*installed on.*\)', l)
    assert not re.match(r'# \(.*version.*\)', l)
    assert lines
    assert count > 2


# Generated at 2022-06-13 05:06:23.353050
# Unit test for method add_env of class CronTab
def test_CronTab_add_env():
    with tempfile.NamedTemporaryFile() as tmp_file:
        with pytest.raises(CronTabError):
            ct = CronTab(None, None, tmp_file.name)
        # TODO: This test may need to be refactored once we have a non-None module
        if False:
            assert ct.add_env('test=test') == None
        else:
            pass


# Generated at 2022-06-13 05:06:27.853677
# Unit test for method remove_job_file of class CronTab
def test_CronTab_remove_job_file():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(
        argument_spec=dict(
            user=dict(required=False, type='str'),
            cron_file=dict(required=False, type='str'),
        ),
        supports_check_mode=True
    )
    ct_temp = CronTab(module)
    ct_temp.remove_job_file()


# Generated at 2022-06-13 05:06:34.968623
# Unit test for method read of class CronTab
def test_CronTab_read():
    from ansible.module_utils.basic import AnsibleModule
    class TestModule(object):
        def __init__(self):
            self.params = {}
        def get_bin_path(self, executable, required=False):
            if executable == 'crontab':
                return 'crontab'
    testmodule = TestModule()
    testcron = CronTab(testmodule, cron_file = 'cron.test')


# Generated at 2022-06-13 05:06:39.097139
# Unit test for method get_envnames of class CronTab
def test_CronTab_get_envnames():
    lines = ['FOO=bar', 'FOO=baz']
    ct = CronTab()
    ct.lines = lines
    ct_expected = set(['FOO'])
    assert ct_expected == set(ct.get_envnames())
    assert ['FOO'] == ct.get_envnames()

# Generated at 2022-06-13 05:08:46.652839
# Unit test for function main
def test_main():
    # Patch AnsibleModule
    mock_module = MagicMock()
    mock_module.params = {'name': 'test', 'job': 'test', 'state': 'present', 'backup': True}
    mock_module.check_mode = False
    mock_module._diff = False

    # Create a crontab
    crontab = CronTab()

    # Add a line to the crontab
    crontab.add_line('test')

    # Patch CronTab to return our test crontab

# Generated at 2022-06-13 05:08:50.005538
# Unit test for method is_empty of class CronTab
def test_CronTab_is_empty():
    ct = CronTab("", "", None)
    ct.lines = []
    assert True == ct.is_empty()

if __name__ == '__main__':
    test_CronTab_is_empty()

# Generated at 2022-06-13 05:08:54.197078
# Unit test for method write of class CronTab
def test_CronTab_write():

    # Create the object
    cron_object = cron.CronTab(user='root', cron_file='test.cron')

    # FIXME: Add more tests here.

    # Write notes to a file
    cron_object.write()


# Generated at 2022-06-13 05:08:56.338603
# Unit test for method render of class CronTab
def test_CronTab_render():
    cron = CronTab()
    cron.lines = ["a", "b", "c"]
    assert cron.render() == "a\nb\nc"

# Generated at 2022-06-13 05:09:05.104750
# Unit test for method add_env of class CronTab
def test_CronTab_add_env():
    import mock
    A = mock.MagicMock()
    A.ansible = 'xxx'
    A.do_comment = mock.MagicMock(return_value='xxx')
    A.lines = ['1']
    A.insertafter = ''
    A.insertbefore = ''
    A.decl = '1'
    A.find_env = mock.MagicMock(return_value=None)
    A.module = mock.MagicMock()
    A.module.fail_json = mock.MagicMock()
    cron_tab.CronTab.add_env(A)
    assert A.lines == ['1', '1']



# Generated at 2022-06-13 05:09:14.291291
# Unit test for method update_env of class CronTab
def test_CronTab_update_env():
    module = DummyModule()
    ctab = CronTab(module)
    assert ctab.update_env('aaa','bbb') == False
    assert ctab.update_env('aaa','aaa=bbb') == False
    assert ctab.update_env('aaa','bbb') == False
    assert ctab.update_env('aaa','aaa=bbb') == False
    assert ctab.remove_env('aaa') == False
    assert ctab.update_env('aaa','aaa=bbb') == False
    assert ctab.remove_env('aaa') == False
    assert ctab.update_env('aaa','aaa=bbb') == False
    assert ctab.remove_env('aaa') == False
    assert ctab.update_env('aaa','aaa=bbb') == False

# Generated at 2022-06-13 05:09:24.010798
# Unit test for method write of class CronTab
def test_CronTab_write():
    module = AnsibleModule(
        argument_spec = dict(
            backup      = dict(default='no', type='bool'),
            cron_file   = dict(default=None),
            state       = dict(default='present', choices=['absent', 'present']),
            jobs        = dict(type='list'),
            user        = dict(default=None),
            vars        = dict(type='dict'),
        ),
        supports_check_mode = True
    )

    module.exit_json(changed=False)


"""
Mock replacement for 'cron' module
"""

try:
    from ansible.module_utils.basic import AnsibleModule
except ImportError:
    pass


# Generated at 2022-06-13 05:09:28.858735
# Unit test for method get_envnames of class CronTab
def test_CronTab_get_envnames():
    args = dict(
        name='FOO',
        path='/path/to/file',
    )
    ct = CronTab(**args)

    assert(ct.get_envnames() == [])

    ct.lines.append('FOO=BAR')
    assert(ct.get_envnames() == ['FOO'])

    ct.lines.append('BAR=FOO')
    assert(ct.get_envnames() == ['FOO', 'BAR'])


# Generated at 2022-06-13 05:09:42.003017
# Unit test for method update_job of class CronTab
def test_CronTab_update_job():
    '''
    Unit test for method update_job of class CronTab
    '''
    m = AnsibleModule(
        argument_spec=dict(
            minute=dict(type='str', required=False),
            user=dict(type='str', required=False),
            job=dict(type='str', required=False),
        ),
        supports_check_mode=False,
    )

    ctab = CronTab(m)
    ctab.add_job("myjob", "* * * * * ping 127.0.0.1")
    ctab.update_job("myjob2", "* * * * * ping 127.0.0.1")
    ctab_render = ctab.render()

    fileh = open("file.txt", "w")

# Generated at 2022-06-13 05:09:48.528770
# Unit test for method add_env of class CronTab
def test_CronTab_add_env():
    import tempfile
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec={})

    filepath = tempfile.mktemp()
    c = CronTab(module, user=None, cron_file=filepath)
    c.add_env('foo=bar')
    c.add_env('bar=baz')
    c.add_env('apple=orange', insertbefore='foo')
    c.add_env('pear=grape', insertafter='bar')

    assert c.lines == ['apple=orange', 'foo=bar', 'bar=baz', 'pear=grape']
    # Test fails on this line