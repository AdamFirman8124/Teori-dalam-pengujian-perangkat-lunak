

# Generated at 2022-06-13 09:02:58.439678
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    src = "https://github.com/ansible/ansible-examples.git"
    version = "master"
    name = "ansible/ansible-examples"

    role = RoleRequirement.role_yaml_parse("%s,%s,%s" % (src, version, name))

    assert role["src"] == src
    assert role["scm"] == 'git'
    assert role["version"] == version
    assert role["name"] == name
    assert role["keep_scm_meta"] == False

    verify_role = {}
    verify_role['src'] = src
    verify_role['version'] = version
    verify_role['name'] = name
    verify_role['scm'] = 'git'
    verify_role['keep_scm_meta'] = False


# Generated at 2022-06-13 09:03:07.601669
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    role_1 = "galaxy.ansible.com/bertwag/ansible-role-tomcat"
    role_1_exp = dict(name='ansible-role-tomcat', src='galaxy.ansible.com/bertwag/ansible-role-tomcat', scm=None, version='')

    role_2 = "galaxy.ansible.com/bertwag/ansible-role-tomcat,v1.0"
    role_2_exp = dict(name='ansible-role-tomcat', src='galaxy.ansible.com/bertwag/ansible-role-tomcat', scm=None, version='v1.0')

    role_3 = "galaxy.ansible.com/bertwag/ansible-role-tomcat,v1.0,tomcat"


# Generated at 2022-06-13 09:03:18.463998
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    test_tuple = [
        ("https://github.com/geerlingguy/test.git", "test"),
        ("http://github.com/geerlingguy/test.git", "test"),
        ("github.com/geerlingguy/test.git", "test"),
        ("github.com:geerlingguy/test.git", "test"),
        ("github.com/geerlingguy/test.git,", "test"),
    ]
    for (src, name) in test_tuple:
        assert RoleRequirement.repo_url_to_role_name(src) == name, "Wrong role name '%s' for source '%s'" % (RoleRequirement.repo_url_to_role_name(src), src)


# Generated at 2022-06-13 09:03:28.650818
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    # 1st test, specify the role name only
    role = dict(role='nginx')
    res = RoleRequirement.role_yaml_parse(role)

    # Verify the result
    assert res == {'name': 'nginx', 'src': None, 'scm': None, 'version': None}

    # 2nd test, specify the role name and version
    role = dict(role='nginx,1.0.0')
    res = RoleRequirement.role_yaml_parse(role)

    # Verify the result
    assert res == {'name': 'nginx', 'src': None, 'scm': None, 'version': '1.0.0'}

    # 3rd test, specify the role name, version and name
    role = dict(role='nginx,1.0.0,test')
    res

# Generated at 2022-06-13 09:03:40.116669
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('git://git.example.com/repos/repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('git@git.example.com/repos/repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('git.example.com/repos/repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('repo.git') == 'repo'

# Generated at 2022-06-13 09:03:52.357826
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name('https://github.com/geerlingguy/ansible-role-apache.git') == 'ansible-role-apache'
    assert RoleRequirement.repo_url_to_role_name('git@git.example.com:repos/repo.git,1.0.0') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('git@git.example.com:repos/repo.git,1.0.0,foo') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('git@git.example.com:repos/repo.git') == 'repo'

# Generated at 2022-06-13 09:04:06.907477
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    assert RoleRequirement.role_yaml_parse(role="test.test,test_version") == \
        {
            'name': 'test.test',
            'scm': None,
            'src': 'test.test',
            'version': 'test_version',
        }

    assert RoleRequirement.role_yaml_parse(role=dict(role="test,test_version")) == \
        {
            'name': 'test',
            'scm': None,
            'src': 'test',
            'version': 'test_version',
        }


# Generated at 2022-06-13 09:04:15.770623
# Unit test for method repo_url_to_role_name of class RoleRequirement

# Generated at 2022-06-13 09:04:25.061009
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():

    # test case 1: https://github.com/x/y.git
    repo_url = 'https://github.com/x/y.git'
    role_name = RoleRequirement.repo_url_to_role_name(repo_url)
    assert role_name == 'y'

    # test case 2: https://github.com/x/y.git,v1.0
    repo_url = 'https://github.com/x/y.git,v1.0'
    role_name = RoleRequirement.repo_url_to_role_name(repo_url)
    assert role_name == 'y'

    # test case 3: git+https://github.com/x/y.git
    repo_url = 'git+https://github.com/x/y.git'
    role

# Generated at 2022-06-13 09:04:36.492019
# Unit test for method role_yaml_parse of class RoleRequirement

# Generated at 2022-06-13 09:04:58.546462
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    v = RoleRequirement()
    assert {} == v.role_yaml_parse('')
    assert {} == v.role_yaml_parse(' ')
    assert {'name': 'a', 'scm': None, 'src': 'a', 'version': None} == v.role_yaml_parse('a')
    assert {'name': 'a', 'scm': None, 'src': 'a', 'version': None} == v.role_yaml_parse({'role': 'a'})
    assert {'name': '', 'scm': None, 'src': 'a', 'version': None} == v.role_yaml_parse('a,')

# Generated at 2022-06-13 09:05:09.061201
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    role_yaml = RoleRequirement.role_yaml_parse('git+git@github.com:alexeguzman/ansible_hello.git,d1b1a8e8a0f20e9f0e9b9a2f8d79b0be1d1a78c2,alexeguzman.hello')
    assert role_yaml['name'] == 'alexeguzman.hello'
    assert role_yaml['scm'] == 'git'
    assert role_yaml['src'] == 'git@github.com:alexeguzman/ansible_hello.git'
    assert role_yaml['version'] == 'd1b1a8e8a0f20e9f0e9b9a2f8d79b0be1d1a78c2'



# Generated at 2022-06-13 09:05:19.462709
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    from ansible.module_utils._text import to_text
    test_url1 = b'git+https://gitlab.company.com/ansible/my_role.git'
    test_url2 = b'git+ssh://git@gitlab.company.com:10022/ansible/my_role.git'
    test_url3 = b'git+https://github.com/username/my_role.git'
    test_url4 = b'git+https://github.com/username/my_role'
    test_url5 = b'https://github.com/username/my_role'
    test_url6 = b'git+https://github.com/username/my_role.git,v1.2.3,my_role'

# Generated at 2022-06-13 09:05:28.590525
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    assert RoleRequirement.role_yaml_parse('geerlingguy.java') == {'name': 'geerlingguy.java', 'src': 'geerlingguy.java', 'scm': None, 'version': ''}
    assert RoleRequirement.role_yaml_parse('geerlingguy.java,1.6') == {'name': 'geerlingguy.java', 'src': 'geerlingguy.java', 'scm': None, 'version': '1.6'}
    assert RoleRequirement.role_yaml_parse('geerlingguy.java,1.6,java') == {'name': 'java', 'src': 'geerlingguy.java', 'scm': None, 'version': '1.6'}

# Generated at 2022-06-13 09:05:35.469763
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    url = '../roles/test_role'
    assert RoleRequirement.repo_url_to_role_name(url) == 'test_role'

    url = 'http://git.example.com/repos/test_role.git'
    assert RoleRequirement.repo_url_to_role_name(url) == 'test_role'

    url = 'https://github.com/someuser/test_role.git'
    assert RoleRequirement.repo_url_to_role_name(url) == 'test_role'

    url = 'git@example.git/someuser/test_role.git'
    assert RoleRequirement.repo_url_to_role_name(url) == 'test_role'


# Generated at 2022-06-13 09:05:47.456933
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name("foo/bar") == "bar"
    assert RoleRequirement.repo_url_to_role_name("git@github.com:foo/bar.git") == "bar"
    assert RoleRequirement.repo_url_to_role_name("git@github.com:foo/bar.git,v1.2.3") == "bar"
    assert RoleRequirement.repo_url_to_role_name("https://github.com/foo/bar.git") == "bar"
    assert RoleRequirement.repo_url_to_role_name("https://github.com/foo/bar.git,v1.2.3") == "bar"

# Generated at 2022-06-13 09:06:00.449680
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    from ansible.playbook.role.requirement import RoleRequirement
    from ansible.errors import AnsibleError
    from ansible.utils.display import Display
    from ansible.utils.galaxy import scm_to_pip_scm

    display = Display()
    role = 'test'
    role_err = 'test,'
    role_err2 = 'test,v1,v2'

    # Check if it is a string
    assert isinstance(role, string_types)

    # Check if method return a dict
    result = RoleRequirement.role_yaml_parse(role)
    role_result = dict(name='test', src=None, scm=None, version=None)
    assert result == role_result

    # Check Error Exception

# Generated at 2022-06-13 09:06:08.361641
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    assert len(RoleRequirement.role_yaml_parse("galaxy.role")) == 4
    assert RoleRequirement.role_yaml_parse("galaxy.role")["scm"] == None
    assert RoleRequirement.role_yaml_parse("galaxy.role")["version"] == None

    assert len(RoleRequirement.role_yaml_parse("git+git@github.com:user/galaxy.role,v1.0")) == 4
    assert RoleRequirement.role_yaml_parse("git+git@github.com:user/galaxy.role,v1.0")["scm"] == "git"
    assert RoleRequirement.role_yaml_parse("git+git@github.com:user/galaxy.role,v1.0")["version"] == "v1.0"

    assert len

# Generated at 2022-06-13 09:06:18.885186
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    test_case_data = {
        'http://github.com/geerlingguy/ansible-role-jenkins.git': 'ansible-role-jenkins',
        './../my-role': 'my-role',
        '../my-role': 'my-role',
        'my-role': 'my-role',
    }
    for test_input, expected_output in test_case_data.items():
        actual_output = RoleRequirement.repo_url_to_role_name(test_input)
        assert expected_output == actual_output

# Generated at 2022-06-13 09:06:27.285028
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    role = {
        'role': 'my_role',
        'scm': 'git',
        'src': 'https://github.com/ansible/ansible-examples',
        'version': '1.0'
    }

    new_role = RoleRequirement.role_yaml_parse(role)

    assert new_role['name'] == role['role']
    assert new_role['scm'] == role['scm']
    assert new_role['src'] == role['src']
    assert new_role['version'] == role['version']

    src0 = 'http://github.com/example.com/repo.git'
    src2 = 'git+http://github.com/example.com/repo.git'

# Generated at 2022-06-13 09:06:42.442635
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    from ansible.utils.display import Display
    global_display = Display()


# Generated at 2022-06-13 09:06:46.743559
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    # Test Git urls
    result = RoleRequirement.repo_url_to_role_name('https://github.com/example-username/example-repo-name.git')
    assert result == 'example-repo-name'

    result = RoleRequirement.repo_url_to_role_name('git@github.com:example-username/example-repo-name.git')
    assert result == 'example-repo-name'

    result = RoleRequirement.repo_url_to_role_name('git@github.com:example-username/example-repo-name')
    assert result == 'example-repo-name'

    result = RoleRequirement.repo_url_to_role_name('http://github.com/example-username/example-repo-name.git')
    assert result

# Generated at 2022-06-13 09:06:51.490450
# Unit test for method role_yaml_parse of class RoleRequirement

# Generated at 2022-06-13 09:07:02.635212
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    # Test case with minimum requirement
    result = RoleRequirement.role_yaml_parse('geerlingguy.apache')
    assert result['name'] == 'geerlingguy.apache'
    assert result['src'] == 'https://github.com/geerlingguy/ansible-role-apache.git'
    assert result['scm'] == 'git'
    assert result['version'] == ''

    # Test Case with explicit version
    result = RoleRequirement.role_yaml_parse('geerlingguy.apache,v1.2.3')
    assert result['name'] == 'geerlingguy.apache'
    assert result['src'] == 'https://github.com/geerlingguy/ansible-role-apache.git'
    assert result['scm'] == 'git'

# Generated at 2022-06-13 09:07:11.417316
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    role_yaml = {
        'name': 'apache',
        'role': 'geerlingguy.apache',
        'version': 'v0.1.0'
    }

    # first with name in role
    role = RoleRequirement.role_yaml_parse(role_yaml)
    assert role == {'name': 'geerlingguy.apache', 'version': 'v0.1.0', 'scm': None, 'src': None}

    # now with name in root
    role_yaml['name'] = 'geerlingguy.apache'
    del role_yaml['role']
    role = RoleRequirement.role_yaml_parse(role_yaml)

# Generated at 2022-06-13 09:07:16.557006
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    """
    Case 1:
    Input: "geerlingguy.jenkins,1.4.0"
    Expected: { 'name': 'geerlingguy.jenkins', 'src': 'geerlingguy.jenkins', 'scm': None, 'version': '1.4.0' }
    """
    assert RoleRequirement.role_yaml_parse("geerlingguy.jenkins,1.4.0") == {'name': 'geerlingguy.jenkins', 'src': 'geerlingguy.jenkins', 'scm': None, 'version': '1.4.0'}

# Generated at 2022-06-13 09:07:21.605385
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    test_urls = [('http://github.com/foo/bar.git', 'bar'), ('http://github.com/foo/bar,v1.0', 'bar')]
    for (url, expected) in test_urls:
        assert RoleRequirement.repo_url_to_role_name(url) == expected

# Generated at 2022-06-13 09:07:32.345749
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    print("Testing method 'role_yaml_parse' of class RoleRequirement ...")

    # Proper format: 'role_name[,version[,name]]'
    role = RoleRequirement.role_yaml_parse("role_name,version,name")
    assert role["name"] == "name"
    assert role["src"] == "role_name"
    assert role["version"] == "version"
    assert "scm" not in role

    role = RoleRequirement.role_yaml_parse("role_name,version")
    assert role["name"] == "role_name"
    assert role["src"] == "role_name"
    assert role["version"] == "version"
    assert "scm" not in role

    role = RoleRequirement.role_yaml_parse("role_name")

# Generated at 2022-06-13 09:07:42.256569
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    """
    unit test for method repo_url_to_role_name of class RoleRequirement
    """
    url_test_data = (
        ('http://git.example.com/repos/repo.git', 'repo'),
        ('http://git.example.com/repos/repo', 'repo'),
        ('git@git.example.com:repos/repo.git', 'repo'),
        ('git@git.example.com:repos/repo', 'repo'),
        ('repo', 'repo'),
    )
    sample_obj = RoleRequirement()
    for url_test in url_test_data:
        assert sample_obj.repo_url_to_role_name(url_test[0]) == url_test[1]


# Generated at 2022-06-13 09:07:53.537510
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    from ansible.parsing.yaml.objects import AnsibleUnicode

# Generated at 2022-06-13 09:08:09.500906
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name('ssh://git.example.com/repos/repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('git@git.example.com:repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('https://git.example.com/repos/repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('git://git.example.com/repos/repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('github.com/user/repo.git') == 'repo'
    assert RoleRequirement.repo_url_to

# Generated at 2022-06-13 09:08:16.807740
# Unit test for method role_yaml_parse of class RoleRequirement

# Generated at 2022-06-13 09:08:17.725207
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    # TODO: write unit tests
    pass

# Generated at 2022-06-13 09:08:25.685056
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    assert RoleRequirement.role_yaml_parse('geerlingguy.apache') == dict(name='apache', src='geerlingguy.apache', scm=None, version=None)
    assert RoleRequirement.role_yaml_parse('geerlingguy.apache,v1.0') == dict(name='apache', src='geerlingguy.apache', scm=None, version='v1.0')
    assert RoleRequirement.role_yaml_parse('geerlingguy.apache,v1.0,myrole') == dict(name='myrole', src='geerlingguy.apache', scm=None, version='v1.0')
    assert RoleRequirement.role_yaml_parse('git+http://github.com/geerlingguy/ansible-role-apache,v1.0,myrole')

# Generated at 2022-06-13 09:08:38.614852
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    from ansible.utils.display import Display
    display = Display()


# Generated at 2022-06-13 09:08:50.142249
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():

    def check(repo_url, expected):
        role_name = RoleRequirement.repo_url_to_role_name(repo_url)
        assert role_name == expected, 'Expected %s, got %s' % (expected, role_name)

    check('https://github.com/ansible/ansible-examples.git', 'ansible-examples')
    check('foo/bar.git', 'bar')
    check('foo/bar', 'bar')
    check('git@github.com:ansible/ansible-examples.git', 'ansible-examples')
    check('git+https://github.com/ansible/ansible-examples.git', 'ansible-examples')

# Generated at 2022-06-13 09:09:01.890758
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    display.warning("\ntest_RoleRequirement_repo_url_to_role_name()\n")
    role_requirement = RoleRequirement()
    assert role_requirement.repo_url_to_role_name("http://git.example.com/repos/repo.git") == "repo"
    assert role_requirement.repo_url_to_role_name("https://git.example.com/repos/repo.git") == "repo"
    assert role_requirement.repo_url_to_role_name("git@git.example.com:repos/repo.git") == "repo"

# Generated at 2022-06-13 09:09:10.130759
# Unit test for method role_yaml_parse of class RoleRequirement

# Generated at 2022-06-13 09:09:19.432107
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    # test with a http repo url
    http_repo_url = "http://git.example.com/repos/repo.git"
    assert RoleRequirement.repo_url_to_role_name(http_repo_url) == "repo"
    # test with a https repo url
    https_repo_url = "https://git.example.com/repos/repo.git"
    assert RoleRequirement.repo_url_to_role_name(https_repo_url) == "repo"
    # test with a ssh repo url
    ssh_repo_url = "git@git.example.com:repos/repo.git"
    assert RoleRequirement.repo_url_to_role_name(ssh_repo_url) == "repo"
    # test with

# Generated at 2022-06-13 09:09:26.597311
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    role_name = RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/foo.git')
    assert role_name == 'foo'

    role_name = RoleRequirement.repo_url_to_role_name('git@git.example.com:repos/foo.git')
    assert role_name == 'foo'

    role_name = RoleRequirement.repo_url_to_role_name('foo.tar.gz')
    assert role_name == 'foo'

    role_name = RoleRequirement.repo_url_to_role_name('foo,bar.tar.gz')
    assert role_name == 'foo'

    role_name = RoleRequirement.repo_url_to_role_name('bar')

# Generated at 2022-06-13 09:09:42.015028
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name("http://example.org/foo") == 'foo'
    assert RoleRequirement.repo_url_to_role_name("http://example.org/foo.git") == 'foo'
    assert RoleRequirement.repo_url_to_role_name("http://example.org/foo,bar.git") == 'foo,bar'
    assert RoleRequirement.repo_url_to_role_name("http://example.org/foo.git,baz") == 'foo'
    assert RoleRequirement.repo_url_to_role_name("http://example.org/foo,bar.git,baz") == 'foo,bar'

# Generated at 2022-06-13 09:09:53.676647
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    # Test case 1
    test_1_role_input = 'role_name'
    test_1_expected_role_output = {
        'name': 'role_name',
        'role': 'role_name',
        'scm': None,
        'src': 'role_name',
        'version': None
    }
    test_1_actual_role_output = RoleRequirement.role_yaml_parse(test_1_role_input)
    assert test_1_expected_role_output == test_1_actual_role_output

    # Test case 2
    test_2_role_input = 'role_name,1.2.3'

# Generated at 2022-06-13 09:10:03.399243
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name('https://github.com/geerlingguy/ansible-role-apache.git') == 'ansible-role-apache'
    assert RoleRequirement.repo_url_to_role_name('https://github.com/geerlingguy/ansible-role-apache.git,v1.0.1') == 'ansible-role-apache,v1.0.1'
    assert RoleRequirement.repo_url_to_role_name('https://github.com/geerlingguy/ansible-role-apache.git,v1.0.1,httpd') == 'ansible-role-apache,v1.0.1,httpd'

# Generated at 2022-06-13 09:10:12.268677
# Unit test for method role_yaml_parse of class RoleRequirement

# Generated at 2022-06-13 09:10:25.002072
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    # Test the wrong format
    try:
        RoleRequirement.role_yaml_parse('3debian')
        assert(False)
    except AnsibleError:
        pass

    # Test the old format
    role = RoleRequirement.role_yaml_parse('role[,version[,name]]')
    print(role)
    assert(role['name'] == 'role')
    assert(role['version'] == '')
    assert(role['scm'] is None)

    # Test the new format
    role = RoleRequirement.role_yaml_parse(dict(src='git+https://github.com/eprintsug/ansible-role-hiera'))
    print(role)
    assert(role['name'] == 'ansible-role-hiera')
    assert(role['version'] == '')
   

# Generated at 2022-06-13 09:10:36.121156
# Unit test for method role_yaml_parse of class RoleRequirement

# Generated at 2022-06-13 09:10:47.590653
# Unit test for method role_yaml_parse of class RoleRequirement

# Generated at 2022-06-13 09:10:56.550279
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    result = RoleRequirement.role_yaml_parse('http://git.example.com/repos/repo.git')
    assert result == {'name': 'repo', 'scm': 'git', 'src': 'http://git.example.com/repos/repo.git', 'version': None}, result

    result = RoleRequirement.role_yaml_parse('git+https://git.example.com/repos/repo.git')
    assert result == {'name': 'repo', 'scm': 'git', 'src': 'https://git.example.com/repos/repo.git', 'version': None}, result

    result = RoleRequirement.role_yaml_parse('https://git.example.com/repos/repo.git')

# Generated at 2022-06-13 09:11:11.426862
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    # import pdb; pdb.set_trace()
    # initialize a RoleRequirement class
    role_requirement = RoleRequirement()

    # Test case when role is a string "username.role_name"
    role_name = "username.role_name"
    role = role_requirement.role_yaml_parse(role_name)
    assert role['name'] == role_name

    # Test case when role is a string "username.role_name,version"
    role_name = "username.role_name,version"
    role = role_requirement.role_yaml_parse(role_name)
    assert role['name'] == "username.role_name"
    assert role['version'] == "version"

    # Test case when role is a string "username.role_name,version,role_name"
   

# Generated at 2022-06-13 09:11:20.046300
# Unit test for method role_yaml_parse of class RoleRequirement

# Generated at 2022-06-13 09:11:46.987778
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():

    # test GitHub
    assert RoleRequirement.repo_url_to_role_name('https://github.com/ansible/ansible-examples.git') == 'ansible-examples'
    assert RoleRequirement.repo_url_to_role_name('https://github.com/ansible/ansible-examples,v1.0.0') == 'ansible-examples'
    assert RoleRequirement.repo_url_to_role_name('https://github.com/ansible/ansible-examples,v1.0.0,geerlingguy.repo-epel') == 'geerlingguy.repo-epel'

    # test GitLab

# Generated at 2022-06-13 09:12:00.674212
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():

    import os

    # 1) test that the method returns the proper role name for different types of URLs
    # a) test URLs with a protocol prefix
    test_url = "http://git.example.com/repos/repo.git"
    result_name = RoleRequirement.repo_url_to_role_name(test_url)
    assert result_name == 'repo'

    test_url = "https://git.example.com/repos/repo.git"
    result_name = RoleRequirement.repo_url_to_role_name(test_url)
    assert result_name == 'repo'

    test_url = "git@git.example.com/repos/repo.git"
    result_name = RoleRequirement.repo_url_to_role_name(test_url)

# Generated at 2022-06-13 09:12:07.740556
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    from ansible.playbook.role.requirement import RoleRequirement
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/.git") == 'repos'
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/") == 'repos'
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos") == 'repos'
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/.git/") == 'repos'
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/.git/name") == 'repos'

# Generated at 2022-06-13 09:12:13.468164
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():

    repo_url = 'http://git.example.com/repos/repo.git'
    role_name = RoleRequirement.repo_url_to_role_name(repo_url)

    assert role_name == 'repo'


# Generated at 2022-06-13 09:12:17.244716
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    role_requirement = RoleRequirement()
    src_role_name = role_requirement.repo_url_to_role_name('git+https://git.example.com/repos/repo.git')
    assert src_role_name == 'repo'

# Generated at 2022-06-13 09:12:23.775792
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    expected_role_name = 'michaelrichardson'
    url_git_tar = 'http://git.example.com/michaelrichardson.git'
    url_git_tar_gz = 'http://git.example.com/michaelrichardson.tar.gz'
    url_https_tar_gz = 'https://git.example.com/michaelrichardson.tar.gz'
    url_http_tar_gz = 'http://git.example.com/michaelrichardson.tar.gz'
    url_ssh_tar_gz = 'git@git.example.com/michaelrichardson.tar.gz'
    url_http_tar = 'http://git.example.com/michaelrichardson.tar'

    role_name = RoleRequirement.repo_url_to_role_

# Generated at 2022-06-13 09:12:33.901001
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/example.git") == "example"
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/example.git, x.y") == "example"
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/example.git, x.y, name") == "example"
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/example.tar.gz") == "example"