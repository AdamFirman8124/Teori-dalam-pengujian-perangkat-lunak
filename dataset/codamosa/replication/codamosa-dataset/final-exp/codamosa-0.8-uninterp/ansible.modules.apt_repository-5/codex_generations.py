

# Generated at 2022-06-13 04:52:35.456144
# Unit test for method __iter__ of class SourcesList
def test_SourcesList___iter__():
    from ansible_collections.community.general.tests.unit.compat import mock

    def check_params(module):
        assert module.params['state'] == 'present'
        assert module.params['repo'] == 'deb http://archive.canonical.com/ubuntu hardy partner'
        assert module.params['filename'] is None


# Generated at 2022-06-13 04:52:41.127541
# Unit test for function get_add_ppa_signing_key_callback
def test_get_add_ppa_signing_key_callback():
    module= AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )
    assert isinstance(get_add_ppa_signing_key_callback(module), types.FunctionType)
    assert get_add_ppa_signing_key_callback(module) is None
    module.check_mode = False
    assert isinstance(get_add_ppa_signing_key_callback(module), types.FunctionType)
    assert get_add_ppa_signing_key_callback(module).__name__ == "_run_command"


# Generated at 2022-06-13 04:52:54.691659
# Unit test for function revert_sources_list
def test_revert_sources_list():
    sources_before = {'/etc/apt/sources.list.d/file1.list': 'Line 1\nLine 2\nLine 3\n',
                      '/etc/apt/sources.list.d/file2.list': 'Line 4\nLine 5\nLine 6\n',
                      '/etc/apt/sources.list.d/file3.list': 'Line 7\nLine 8\nLine 9\n'}

# Generated at 2022-06-13 04:53:01.673201
# Unit test for method __iter__ of class SourcesList
def test_SourcesList___iter__():
    obj = SourcesList()
    obj.files['file1'] = [('n1', 'valid1', 'enabled1', 'source1', 'comment1'),
                          ('n2', None, None, None, None),
                          ('n3', 'valid3', 'enabled3', 'source3', 'comment3'),
                          ('n4', 'valid4', 'enabled4', 'source4', 'comment4')]
    obj.files['file2'] = [('n1', 'valid1', 'enabled1', 'source1', 'comment1'),
                          ('n2', None, None, None, None),
                          ('n3', 'valid3', 'enabled3', 'source3', 'comment3'),
                          ('n4', 'valid4', 'enabled4', 'source4', 'comment4')]

# Generated at 2022-06-13 04:53:12.176127
# Unit test for method __iter__ of class SourcesList
def test_SourcesList___iter__():
    import os
    import aptsources.distro
    import ansible.module_utils.six.moves.builtins as __builtin__

    old_environ = copy.deepcopy(os.environ)

    aptsources.distro = type(
        'aptsources.distro',
        (), dict(
            get_distro=lambda: type(
                'aptsources.distro.Ubuntu',
                (), dict(
                    id=lambda: 'Ubuntu',
                    get_sources=lambda: []
                )
            )
        )
    )


# Generated at 2022-06-13 04:53:19.779400
# Unit test for function get_add_ppa_signing_key_callback
def test_get_add_ppa_signing_key_callback():
    def fake_module():
        return MagicMock(**{'run_command.side_effect': Exception})
    module = fake_module()
    result = get_add_ppa_signing_key_callback(module)
    assert result is None
    result = get_add_ppa_signing_key_callback(module)
    assert call(['apt-key', 'adv', '--recv-keys', '--no-tty', '--keyserver', 'hkp://keyserver.ubuntu.com:80', 'test']) in module.run_command.mock_calls



# Generated at 2022-06-13 04:53:22.369518
# Unit test for method dump of class SourcesList
def test_SourcesList_dump():
    assert SourcesList(None).dump() == {}



# Generated at 2022-06-13 04:53:23.146865
# Unit test for function install_python_apt
def test_install_python_apt():
    pass



# Generated at 2022-06-13 04:53:34.648162
# Unit test for method save of class SourcesList
def test_SourcesList_save():
    def write_random_file(d, *args):
        fn = os.path.join(d, *args)
        #f = open(fn, 'w')
        #f.write(str(random.random()))


    def remove_random_file(d, *args):
        fn = os.path.join(d, *args)
        os.remove(fn)


    def list_files(d, *args):
        fn = os.path.join(d, *args)
        return os.listdir(fn)

    d = tempfile.TemporaryDirectory()

# Generated at 2022-06-13 04:53:38.646155
# Unit test for constructor of class SourcesList
def test_SourcesList():
    sl = SourcesList()
    assert 'aptsources.sourceslist.SourcesList' == sl.__class__.__name__



# Generated at 2022-06-13 04:54:20.666616
# Unit test for method add_source of class UbuntuSourcesList
def test_UbuntuSourcesList_add_source():
    module = AnsibleModule(argument_spec={})
    module.params['codename'] = 'trusty'
    UbuntuSourcesListMock.module = module

    sl = UbuntuSourcesList(module)
    assert not sl.repos_urls

    sl.add_source('ppa:owner/ppa')
    assert 'deb http://ppa.launchpad.net/owner/ppa/ubuntu trusty main' in sl.repos_urls

    sl.add_source('ppa:owner/ppa', file='my-sources.list')
    assert 'deb http://ppa.launchpad.net/owner/ppa/ubuntu trusty main' in sl.repos_urls

    sl.add_source('ppa:owner/ppa', file='/etc/apt/sources.list')

# Generated at 2022-06-13 04:54:30.045945
# Unit test for function install_python_apt
def test_install_python_apt():
    from ansible.module_utils.basic import AnsibleModule
    m = AnsibleModule(argument_spec={'install_python_apt': {'type': 'bool', 'default': True}})
    m.params['_ansible_check_mode'] = False
    m.params['_ansible_diff'] = True
    m.params['_ansible_verbosity'] = 3
    m.fail_json = lambda this, msg: sys.stderr.write(this['msg'] + '\n')
    install_python_apt(m, 'python-apt')



# Generated at 2022-06-13 04:54:42.739380
# Unit test for method dump of class SourcesList
def test_SourcesList_dump():
    module = AnsibleModule({})
    from ansible.module_utils.six import StringIO
    f = StringIO(u"""# deb cdrom:[Ubuntu-Server 14.04.1 LTS _Trusty Tahr_ - Release amd64 (20140722.3)]/ trusty main restricted
deb http://archive.ubuntu.com/ubuntu trusty main restricted multiverse universe

""")
    sl = SourcesList(module)
    sl.files = {'file': [(0, False, False, '', 'cdrom:'), (1, True, True, 'deb http://archive.ubuntu.com/ubuntu trusty main restricted multiverse universe', '')]}

# Generated at 2022-06-13 04:54:56.356279
# Unit test for method modify of class SourcesList
def test_SourcesList_modify():
    module = AnsibleModule({})
    sl = SourcesList(module)
    sl.files = {
        'testfile1': [
            (0, True, True, 'deb http://archive.ubuntu.com/ubuntu xenial main', 'comment'),
            (1, True, True, 'deb http://archive.ubuntu.com/ubuntu xenial universe', '')
        ],
        'testfile2': [
            (0, True, True, 'deb http://archive.ubuntu.com/ubuntu trusty main', 'comment'),
            (1, True, True, 'deb http://archive.ubuntu.com/ubuntu trusty universe', '')
        ],

    }
    sl.modify('testfile1', 0, source='deb http://archive.ubuntu.com/ubuntu xenial main2')

# Generated at 2022-06-13 04:55:05.510123
# Unit test for method dump of class SourcesList
def test_SourcesList_dump():
    test_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_data.json')
    with open(test_data) as test_data_file:
        test_data = json.load(test_data_file)
        for sources in test_data['sources']:
            expected_sources_list_dump = sources['expected_sources_list_dump']
            test_sources_list = SourcesList(None)
            for source in sources['sources']:
                test_sources_list.add_source(source)
            assert test_sources_list.dump() == expected_sources_list_dump, "The dump of the SourcesList is not correct"



# Generated at 2022-06-13 04:55:08.485628
# Unit test for function install_python_apt
def test_install_python_apt():

    if not HAVE_PYTHON_APT:
        install_python_apt(module, apt_pkg_name)


# Generated at 2022-06-13 04:55:18.731238
# Unit test for function install_python_apt
def test_install_python_apt():

    class TestModule(object):
        def __init__(self):
            self.run_command_results = []
            self.run_command_calls = []

        def get_bin_path(self, executable, required=False):
            return '/usr/bin/apt-get'

        def run_command(self, cmd, check_rc=False, close_fds=True, executable=None, data=None, binary_data=False, path_prefix=None, cwd=None,
                        use_unsafe_shell=False, prompt_regex=None, environ_update=None, umask=None, encoding=None, errors='surrogate_then_replace',
                        expand_user_and_vars=True):
            result = copy.deepcopy(self.run_command_results)
            self.run_command_

# Generated at 2022-06-13 04:55:25.286492
# Unit test for method modify of class SourcesList
def test_SourcesList_modify():
    module = AnsibleModule({})
    apt = apt_repository(module)
    apt.sources.files = { 'apt.list' : [( 0, True, True, 'deb http://archive.canonical.com/ubuntu trusty partner', '' ),
                                      ( 1, True, True, 'deb http://dl.google.com/linux/chrome/deb/ trusty main', '' ),
                                      ( 2, True, True, 'deb-src http://archive.canonical.com/ubuntu trusty partner', '' ),
                                      ( 3, True, False, 'deb http://archive.canonical.com/ubuntu hardy partner', '' ),
                                      ( 4, True, True, 'deb-src http://archive.canonical.com/ubuntu trusty partner', '' )]
                            }

# Generated at 2022-06-13 04:55:38.402016
# Unit test for method remove_source of class SourcesList
def test_SourcesList_remove_source():
    line = 'deb https://download.docker.com/linux/ubuntu bionic stable'
    line2 = 'deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable'
    line3 = 'deb-src https://download.docker.com/linux/ubuntu bionic stable'
    line4 = 'deb-src https://download.docker.com/linux/ubuntu bionic stable'
    files = {}
    files[line] = [(0, True, True, line, ''), (1, True, False, line2, ''),
                   (2, True, True, line3, ''), (3, True, True, line4, '')]
    module = AnsibleModule(argument_spec=dict(
        line=dict(type='str'),
    ))

    lines = SourcesList(module)

# Generated at 2022-06-13 04:55:48.746775
# Unit test for method modify of class SourcesList
def test_SourcesList_modify():
    module = AnsibleModule({})
    instance = SourcesList(module)
    temp_file = tempfile.NamedTemporaryFile(delete=False)

# Generated at 2022-06-13 04:56:58.044413
# Unit test for method __deepcopy__ of class UbuntuSourcesList
def test_UbuntuSourcesList___deepcopy__():
    import copy
    from ansible.module_utils.basic import AnsibleModule
    argument_spec = dict(codename=dict())
    module = AnsibleModule(argument_spec=argument_spec)
    original = UbuntuSourcesList(module)
    original.codename = 'foo'
    copy = copy.deepcopy(original)
    assert copy.codename == original.codename, 'Copy should be independent'
    original.codename = 'bar'
    assert copy.codename == 'foo', 'Original should not be affected'



# Generated at 2022-06-13 04:57:05.348857
# Unit test for method remove_source of class SourcesList

# Generated at 2022-06-13 04:57:13.684072
# Unit test for method __iter__ of class SourcesList
def test_SourcesList___iter__():
    module = AnsibleModule({'sources_dir': '.'})
    sources = SourcesList(module)

    # Create files in sources.list.d
    test_file = 'foo.list'
    test_entry = 'deb http://localhost/foo/bar/ baz'
    test_comment = 'This is a multiline\ncomment\n'
    test_full_entry = '# %s %s\n' % (test_entry, test_comment)

    with open(test_file, 'w') as f:
        f.write(test_full_entry)

    with open(test_file, 'r') as f:
        sources.load(test_file)

    for file, n, enabled, source, comment in sources:
        assert file == './%s' % test_file
        assert enabled is False

# Generated at 2022-06-13 04:57:23.192601
# Unit test for method dump of class SourcesList
def test_SourcesList_dump():
    from ansible.module_utils.six import StringIO
    from ansible.module_utils._text import to_bytes
    orig_stdout = sys.stdout
    stdout = sys.stdout = StringIO()
    list = SourcesList(AnsibleModule(argument_spec={}))
    list.load('tests/ansible/testdata/apt_repository/sources-list-test-1')
    list.load('tests/ansible/testdata/apt_repository/sources-list-test-2')
    result = list.dump()
    sys.stdout = orig_stdout
    output = stdout.getvalue()
    if output:
        # to make pylint happy
        assert output

# Generated at 2022-06-13 04:57:28.984270
# Unit test for method modify of class SourcesList
def test_SourcesList_modify():
    file = 'test_filename'
    n = 0
    enabled = None
    source = None
    comment = None
    valid = True
    enabled_old = False
    source_old = 'test_source_old'
    comment_old = 'test_comment_old'
    obj = {
        file: [(n, valid, enabled_old, source_old, comment_old)]
    }
    expected_result = {
        file: [(n, valid, enabled_old, source_old, comment_old)]
    }
    sources_list = SourcesList('this-is-the-module')
    sources_list.files = copy.deepcopy(obj)
    sources_list.modify(file, n, enabled, source, comment)
    assert sources_list.files == expected_result

# Generated at 2022-06-13 04:57:32.366955
# Unit test for method __deepcopy__ of class UbuntuSourcesList
def test_UbuntuSourcesList___deepcopy__():
    sources = UbuntuSourcesList(module, add_ppa_signing_keys_callback=None)
    assert sources != sources.__deepcopy__()


# Generated at 2022-06-13 04:57:44.448768
# Unit test for method remove_source of class SourcesList
def test_SourcesList_remove_source():
    sources = SourcesList(None)
    sources.files = {'/a/b/c.list':[(1, True, True, 'deb http://a b c', ''),
                                    (2, True, True, 'deb http://b c d', '')],
                     '/d/e/f.list':[(2, True, True, 'deb http://c b d', ''),
                                    (3, True, True, 'deb http://d e f', '')]}
    sources.remove_source('deb http://c b d')

# Generated at 2022-06-13 04:57:54.435994
# Unit test for method add_source of class SourcesList
def test_SourcesList_add_source():
    '''
    Unit test for method add_source of class SourcesList
    '''
    test_sources_list = SourcesList(AnsibleModule(argument_spec={}))
    test_sources_list.add_source('deb-src http://archive.canonical.com/ubuntu hardy partner')
    test_sources_list.add_source('deb-src http://noroot.com/ubuntu hardy partner')
    test_sources_list.add_source('deb-src http://no-existing.com/ubuntu hardy partner')
    test_sources_list.add_source('deb-src http://archive.canonical.com/ubuntu hardy partner')

# Generated at 2022-06-13 04:58:02.927699
# Unit test for constructor of class UbuntuSourcesList
def test_UbuntuSourcesList():
    module = object()
    module.params = {
        'codename': 'default_codename',
        'filename': None
    }
    module.run_command = lambda cmd: (0, '', '')
    module.fail_json = lambda msg: None
    module.warn = lambda msg: None

    # Mock distro
    distro.codename = 'some_codename'

    # Mock read_file

# Generated at 2022-06-13 04:58:12.936462
# Unit test for method remove_source of class UbuntuSourcesList
def test_UbuntuSourcesList_remove_source():
    module = AnsibleModule(argument_spec={'codename' : {'type': 'str', 'default': 'xenial'}})
    sources_file1 = '''
deb http://us.archive.ubuntu.com/ubuntu/ trusty-updates main restricted
# deb-src http://us.archive.ubuntu.com/ubuntu/ trusty-updates main restricted

ppa:ansible/ansible
ppa:ansible/ansible
'''
    sources_file2 = '''
deb http://us.archive.ubuntu.com/ubuntu/ trusty-updates main restricted
# deb-src http://us.archive.ubuntu.com/ubuntu/ trusty-updates main restricted

ppa:ansible/ansible
'''
    sourceslist = UbuntuSourcesList(module)