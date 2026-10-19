

# Generated at 2022-06-13 09:03:10.432962
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():

    assert 'role_name' == RoleRequirement.repo_url_to_role_name('role_name')
    assert 'role_name' == RoleRequirement.repo_url_to_role_name('git+http://git.example.com/repos/role_name.git')
    assert 'role_name' == RoleRequirement.repo_url_to_role_name('git+https://git.example.com/repos/role_name.git')
    assert 'role_name' == RoleRequirement.repo_url_to_role_name('git+ssh://git.example.com/repos/role_name.git')
    assert 'role_name' == RoleRequirement.repo_url_to_role_name('git+git@git.example.com:repos/role_name.git')

# Generated at 2022-06-13 09:03:16.464693
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    role_requirement = RoleRequirement()
    # Test with urls that have '.git' extension
    assert role_requirement.repo_url_to_role_name(None) == None
    assert role_requirement.repo_url_to_role_name("") == ""
    assert role_requirement.repo_url_to_role_name("ansible") == "ansible"
    assert role_requirement.repo_url_to_role_name("https://github.com/ansible/ansible-modules-core.git") == "ansible-modules-core"
    assert role_requirement.repo_url_to_role_name("git@github.com:ansible/ansible-modules-core.git") == "ansible-modules-core"

    # Test with urls that does not have '.

# Generated at 2022-06-13 09:03:26.862365
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():

    assert RoleRequirement.repo_url_to_role_name("https://github.com/example/ansible-role-foo.git") == "ansible-role-foo"
    assert RoleRequirement.repo_url_to_role_name("https://github.com/example/ansible-role-foo") == "ansible-role-foo"
    assert RoleRequirement.repo_url_to_role_name("https://github.com/example/ansible-role-foo.git,v1.2.3") == "ansible-role-foo"
    assert RoleRequirement.repo_url_to_role_name("https://github.com/example/ansible-role-foo.git,v1.2.3,test_role") == "test_role"
    assert RoleRequirement.repo_url

# Generated at 2022-06-13 09:03:37.944227
# Unit test for method role_yaml_parse of class RoleRequirement

# Generated at 2022-06-13 09:03:49.047054
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    # GIVEN
    role_requirement = RoleRequirement()
    repo_url = "git+git://git.example.com/repos/repo.git"
    # WHEN
    name = role_requirement.repo_url_to_role_name(repo_url)
    # THEN
    assert name == "repo"
    # GIVEN
    repo_url = "http://git.example.com/repos/repo.git"
    # WHEN
    name = role_requirement.repo_url_to_role_name(repo_url)
    # THEN
    assert name == "repo"
    # GIVEN
    repo_url = "https://git.example.com/repos/repo.git"
    # WHEN
    name = role_requirement.repo_

# Generated at 2022-06-13 09:03:57.912088
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('git.example.com/repos/repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('git.example.com/repos/repo') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('git@git.example.com:group/repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_

# Generated at 2022-06-13 09:04:04.324164
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    assert RoleRequirement.role_yaml_parse("example.com,v1.0,name") == dict(name='name', src='example.com', scm=None, version='v1.0')
    assert RoleRequirement.role_yaml_parse("example.com,v1.0") == dict(name='example.com', src='example.com', scm=None, version='v1.0')
    assert RoleRequirement.role_yaml_parse("example.com") == dict(name='example.com', src='example.com', scm=None, version='')

    # Test logic for automatic 'name' detection from URL

# Generated at 2022-06-13 09:04:14.055278
# Unit test for method role_yaml_parse of class RoleRequirement

# Generated at 2022-06-13 09:04:23.894620
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    from ansible.utils.py2_compat import is_py3

    # Test if fully qualified URLs are converted correctly
    assert RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('https://git.example.com/repos/repo.git') == 'repo'

    # Test if the repo name is extracted correctly if the URL contains a port number

# Generated at 2022-06-13 09:04:35.693202
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    # Test scenario 1
    name = "new"
    src = "git+https://github.com/user/new"
    scm = "git"
    version = "HEAD"
    my_role1 = RoleRequirement.role_yaml_parse({"name":name, "src":src, "scm":scm, "version":version})
    if (name == my_role1["name"] and src == my_role1["src"] and scm == my_role1["scm"] and version == my_role1["version"]):
        print("Successfully tested RoleRequirement: role_yaml_parse with scenario 1")
    else:
        print("Failed to test RoleRequirement: role_yaml_parse with scenario 1")

    # Test scenario 2
    name = "new"

# Generated at 2022-06-13 09:04:55.091173
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    actual = RoleRequirement.role_yaml_parse("git+https://github.com/jshapirogit/ansible-network-curses.git,v0.1")
    expected = dict(name='ansible-network-curses', src='https://github.com/jshapirogit/ansible-network-curses.git', scm='git', version='v0.1')
    assert actual == expected
    actual = RoleRequirement.role_yaml_parse("git+https://github.com/jshapirogit/ansible-network-curses.git")
    expected = dict(name='ansible-network-curses', src='https://github.com/jshapirogit/ansible-network-curses.git', scm='git', version='')
    assert actual == expected

# Generated at 2022-06-13 09:05:02.423195
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    ''' Test method role_yaml_parse of class RoleRequirement '''

    role = 'foo.git'
    output = RoleRequirement.role_yaml_parse(role)
    assert 'name' in output
    assert output['name'] == 'foo'
    assert 'src' in output
    assert output['src'] == 'foo.git'
    assert 'scm' in output
    assert output['scm'] == None
    assert 'version' in output
    assert output['version'] == None

    role = 'foo.git,v1.0'
    output = RoleRequirement.role_yaml_parse(role)
    assert 'name' in output
    assert output['name'] == 'foo'
    assert 'src' in output
    assert output['src'] == 'foo.git'

# Generated at 2022-06-13 09:05:05.371131
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.git") == "repo"


# Generated at 2022-06-13 09:05:17.995676
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    # Testcase 1
    expected = dict (role='foo', bar='baz')
    result = RoleRequirement.role_yaml_parse(expected)
    assert result == expected
    # Testcase 2
    expected = dict (name='foo', src='git+https://github.com/username/foo.git', scm='git', version='1.2.3', other='thing')
    result = RoleRequirement.role_yaml_parse(expected)
    assert result == expected
    # Testcase 3 - role name and version only
    expected = dict (name='foo', src='foo', scm=None, version='1.2.3')
    result = RoleRequirement.role_yaml_parse('foo,1.2.3')
    assert result == expected
    # Testcase 4 - role name and version only with spaces
   

# Generated at 2022-06-13 09:05:27.530052
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name("user@git.example.com:user/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("https://git.example.com/user/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("https://git.example.com/user/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("https://git.example.com/user/repo.git,bar") == "repo"
    assert RoleRequirement.repo_url_to_role_name("https://git.example.com/user/repo.git,bar,foo") == "repo"
    assert Role

# Generated at 2022-06-13 09:05:34.861703
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    # test old-style role line
    name = 'example.role'
    parsed_name = RoleRequirement.role_yaml_parse(name)
    assert parsed_name == dict(name=name, src=name, scm=None, version=None)

    # test old-style line with version
    name = 'example.role, 1.23'
    parsed_name = RoleRequirement.role_yaml_parse(name)
    assert parsed_name == dict(name=name, src=name, scm=None, version=None)

    # test new-style line with dictionary and name key
    name = 'example.role'
    parsed_name = RoleRequirement.role_yaml_parse(dict(name=name, ignore_errors=True))

# Generated at 2022-06-13 09:05:41.689143
# Unit test for method role_yaml_parse of class RoleRequirement

# Generated at 2022-06-13 09:05:51.814267
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo") == "repo"
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.tar.gz") == "repo.tar"
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo,v1.0") == "repo"

# Generated at 2022-06-13 09:06:04.014342
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    # Test a git style role name with the prefix git+
    role_name = RoleRequirement.repo_url_to_role_name("git+https://github.com/ansible-qe/ansible-role-ipa.git")
    assert role_name == "ansible-role-ipa"

    # Test a pypi style role name
    role_name = RoleRequirement.repo_url_to_role_name("ansible-role-ipa")
    assert role_name == "ansible-role-ipa"

    # Test a full scm url without the prefix
    role_name = RoleRequirement.repo_url_to_role_name("https://github.com/ansible-qe/ansible-role-ipa.git")

# Generated at 2022-06-13 09:06:11.767332
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo.tar.gz') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo.tar.gz,v0.0.1') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo') == 'repo'

# Generated at 2022-06-13 09:06:25.237378
# Unit test for method repo_url_to_role_name of class RoleRequirement

# Generated at 2022-06-13 09:06:39.188125
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    assert RoleRequirement.role_yaml_parse('role_name') == {'name': 'role_name', 'scm': None, 'src': 'role_name', 'version': ''}
    assert RoleRequirement.role_yaml_parse('role_name,version') == {'name': 'role_name', 'scm': None, 'src': 'role_name', 'version': 'version'}
    assert RoleRequirement.role_yaml_parse('role_name,version,name') == {'name': 'name', 'scm': None, 'src': 'role_name', 'version': 'version'}

# Generated at 2022-06-13 09:06:50.874800
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    rreq = RoleRequirement()
    parsed_role = rreq.role_yaml_parse('../foo')
    assert parsed_role == dict(name='../foo', scm=None, src='../foo', version='')
    parsed_role = rreq.role_yaml_parse('../foo,v1')
    assert parsed_role == dict(name='../foo', scm=None, src='../foo', version='v1')
    parsed_role = rreq.role_yaml_parse('../foo,v1,bar')
    assert parsed_role == dict(name='bar', scm=None, src='../foo', version='v1')
    parsed_role = rreq.role_yaml_parse('../foo,v1,bar,bam')

# Generated at 2022-06-13 09:06:54.508943
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert (RoleRequirement.repo_url_to_role_name('git@github.com:ansible/ansible-for-devops.git') ==
            'ansible-for-devops')


# Generated at 2022-06-13 09:07:05.467513
# Unit test for method role_yaml_parse of class RoleRequirement

# Generated at 2022-06-13 09:07:15.969461
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    role = RoleRequirement()
    print(role.role_yaml_parse('src is a string'))
    print(role.role_yaml_parse({'role': 'src is a string'}))
    print(role.role_yaml_parse({'src': 'src is a string'}))
    print(role.role_yaml_parse('src is a string'))
    print(role.role_yaml_parse('src is a string'))
    print(role.role_yaml_parse('src is a string'))
    print(role.role_yaml_parse('src is a string'))
    print(role.role_yaml_parse('src is a string'))
    print(role.role_yaml_parse('src is a string'))

# Generated at 2022-06-13 09:07:27.021504
# Unit test for method role_yaml_parse of class RoleRequirement

# Generated at 2022-06-13 09:07:35.994315
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    import sys

# Generated at 2022-06-13 09:07:46.435571
# Unit test for method repo_url_to_role_name of class RoleRequirement

# Generated at 2022-06-13 09:07:56.328201
# Unit test for method role_yaml_parse of class RoleRequirement

# Generated at 2022-06-13 09:08:11.470421
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    roles_yaml_parse = RoleRequirement.role_yaml_parse

    role = roles_yaml_parse('foo.bar')
    assert role['scm'] is None
    assert role['name'] == 'foo.bar'
    assert role['src'] == 'foo.bar'
    assert role['version'] is None

    role = roles_yaml_parse('git+https://github.com/foo/bar')
    assert role['scm'] == 'git'
    assert role['name'] == 'bar'
    assert role['src'] == 'https://github.com/foo/bar'
    assert role['version'] is None

    role = roles_yaml_parse('git+https://github.com/foo/bar,baz')
    assert role['scm'] == 'git'

# Generated at 2022-06-13 09:08:25.834393
# Unit test for method role_yaml_parse of class RoleRequirement

# Generated at 2022-06-13 09:08:38.732577
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    test_role = "role_name,version"
    expected_role = {'name': 'role_name', 'version': 'version', 'scm': None, 'src': None}
    assert RoleRequirement.role_yaml_parse(test_role) == expected_role

    test_role = {'role': 'role_name'}
    expected_role = {'name': 'role_name', 'version': '', 'scm': None, 'src': None}
    assert RoleRequirement.role_yaml_parse(test_role) == expected_role

    test_role = {'role': 'role_name', 'other': 'other_value'}
    expected_role = {'name': 'role_name', 'version': '', 'scm': None, 'src': None}
    assert RoleRequirement.role_

# Generated at 2022-06-13 09:08:50.224129
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    error_msg = "Invalid role line (%s). Proper format is 'role_name[,version[,name]]'"

    # Test role specification according to
    # https://galaxy.ansible.com/intro#installing-multiple-roles-from-a-file
    # {
    #   "role" : "username.rolename",
    #   "role" : "https://github.com/username/rolename",
    #   "role" : "https://github.com/username/rolename,v1.2",
    #   "role" : "https://github.com/username/rolename,v1.2,rolename"
    # }
    #
    # Test role specification according to
    # https://github.com/ansible/galaxy/blob/devel/docs/api.md#install-

# Generated at 2022-06-13 09:09:01.990521
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    test_dict = dict(role='test_role', src='http://github.com/ansible/test_role.git', scm='git', version='v1.0')
    test_str = 'http://github.com/ansible/test_role.git,v1.0,test_role'
    test_str2 = 'http://github.com/ansible/test_role.git,v1.0'
    test_str3 = 'http://github.com/ansible/test_role.git'
    test_str4 = 'git+http://github.com/ansible/test_role.git,v1.0,test_role'
    test_str5 = 'git+http://github.com/ansible/test_role.git,v1.0'

# Generated at 2022-06-13 09:09:10.189032
# Unit test for method role_yaml_parse of class RoleRequirement

# Generated at 2022-06-13 09:09:19.459728
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name("git://git.example.com/someuser/somerepo.git") == "somerepo"
    assert RoleRequirement.repo_url_to_role_name("git@git.example.com:someuser/somerepo.git") == "somerepo"
    assert RoleRequirement.repo_url_to_role_name("https://git.example.com/someuser/somerepo.git") == "somerepo"
    assert RoleRequirement.repo_url_to_role_name("https://git.example.com/someuser/somerepo") == "somerepo"

# Generated at 2022-06-13 09:09:23.477877
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():

    role_name = RoleRequirement.repo_url_to_role_name("https://github.com/foo/bar.git")
    assert role_name == "bar"

    role_name = RoleRequirement.repo_url_to_role_name("@git+ssh://git@github.com/foo/bar.git,v1.0")
    assert role_name == "bar"


# Generated at 2022-06-13 09:09:29.866000
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    if __name__ == '__main__':
        import os
        import sys

        test = RoleRequirement()
        test_result = test.role_yaml_parse('galaxy.role,version,name')
        assert test_result['name'] == 'name'
        assert test_result['scm'] == 'git'
        assert test_result['src'] == 'galaxy.role'
        assert test_result['version'] == 'version'

        test_result = test.role_yaml_parse('galaxy.role,version')
        assert test_result['name'] == 'galaxy.role'
        assert test_result['scm'] == 'git'
        assert test_result['src'] == 'galaxy.role'
        assert test_result['version'] == 'version'

        test_result = test.role_y

# Generated at 2022-06-13 09:09:39.883029
# Unit test for method repo_url_to_role_name of class RoleRequirement

# Generated at 2022-06-13 09:09:59.677882
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    obj = RoleRequirement()
    assert obj.repo_url_to_role_name("http://git.example.com/repos/repo.git") == "repo"
    assert obj.repo_url_to_role_name("http://git.example.com/repos/repo,version123.git") == "repo"
    assert obj.repo_url_to_role_name("http://git.example.com/repos/repo-name.git") == "repo-name"
    assert obj.repo_url_to_role_name("git://git.example.com/repos/repo-name.git") == "repo-name"

# Generated at 2022-06-13 09:10:07.437361
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    display.display(' ')
    display.display('<<< role_name (from url): ')
    display.display(' ')
    role_name = RoleRequirement.repo_url_to_role_name('')
    display.display('empty      : %s' % role_name)
    assert role_name == ''
    role_name = RoleRequirement.repo_url_to_role_name('test')
    display.display('test       : %s' % role_name)
    assert role_name == 'test'
    role_name = RoleRequirement.repo_url_to_role_name('test.git')
    display.display('test.git   : %s' % role_name)
    assert role_name == 'test'
    role_name = RoleRequirement.repo_url_

# Generated at 2022-06-13 09:10:19.288094
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('git@git.example.com:repos/repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('file://home/user/repos/repo.tar.gz') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo.tar.gz') == 'repo'

# Generated at 2022-06-13 09:10:30.855442
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    # Test for role
    role = RoleRequirement.role_yaml_parse("role_name")
    assert role['name'] == 'role_name'
    assert role['version'] == ''
    assert role['scm'] is None
    assert role['src'] == 'role_name'

    # Test for role,version
    role = RoleRequirement.role_yaml_parse("role_name,version")
    assert role['name'] == 'role_name'
    assert role['version'] == 'version'
    assert role['scm'] is None
    assert role['src'] == 'role_name'

    # Test for role,version,name
    role = RoleRequirement.role_yaml_parse("role_name,version,name")
    assert role['name'] == 'name'

# Generated at 2022-06-13 09:10:39.675788
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    role_req = RoleRequirement()

    # Test for valid role string
    role = "foo"
    res1 = role_req.role_yaml_parse(role)
    assert res1["name"] == "foo"
    assert res1["src"] == "foo"
    assert res1["scm"] == None
    assert res1["version"] == ""

    # Test for valid role string with version
    role = "foo,1.0"
    res1 = role_req.role_yaml_parse(role)
    assert res1["name"] == "foo"
    assert res1["src"] == "foo"
    assert res1["scm"] == None
    assert res1["version"] == "1.0"

    # Test for valid role string with version and name

# Generated at 2022-06-13 09:10:47.330238
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert 'ansible' == RoleRequirement.repo_url_to_role_name('https://github.com/ansible/ansible')
    assert 'ansible' == RoleRequirement.repo_url_to_role_name('git@github.com:ansible/ansible.git')
    assert 'ansible' == RoleRequirement.repo_url_to_role_name('git@github.com:ansible/ansible')
    assert 'ansible' == RoleRequirement.repo_url_to_role_name('git://github.com/ansible/ansible.git')
    assert 'ansible' == RoleRequirement.repo_url_to_role_name('http://github.com/ansible/ansible.git')
    assert 'ansible' == RoleRequirement.repo_url_to_

# Generated at 2022-06-13 09:10:56.372440
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("git@github.com/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("https://github.com/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.git,v2.0") == "repo"
    assert RoleRequirement.repo_url_to_role_name("git@github.com/repo.git,v2.0") == "repo"
    assert RoleRequirement.repo_

# Generated at 2022-06-13 09:11:11.211901
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert(RoleRequirement.repo_url_to_role_name("https://github.com/username/repo.git") == "repo")
    assert(RoleRequirement.repo_url_to_role_name("https://github.com/username/repo.git,v1.0") == "repo")
    assert(RoleRequirement.repo_url_to_role_name("https://github.com/username/repo.git,v1.0,myname") == "repo")
    assert(RoleRequirement.repo_url_to_role_name("https://github.com/username/repo,v1.0,myname") == "repo")

# Generated at 2022-06-13 09:11:19.876011
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    import ansible.galaxy.role


# Generated at 2022-06-13 09:11:30.814803
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():

    repo_url = RoleRequirement.repo_url_to_role_name("https://github.com/AnsibleShipyard/ansible-git.git")
    assert repo_url == "ansible-git"

    repo_url2 = RoleRequirement.repo_url_to_role_name("https://github.com/AnsibleShipyard/ansible-git.git,version,name")
    assert repo_url2 == "ansible-git"

    repo_url3 = RoleRequirement.repo_url_to_role_name("https://github.com/AnsibleShipyard/ansible-git.git,version,name,one_more")
    assert repo_url3 == "ansible-git"


# Generated at 2022-06-13 09:12:01.773190
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():

    assert RoleRequirement().repo_url_to_role_name('http://git.example.com/repos/repo.git') == 'repo'
    assert RoleRequirement().repo_url_to_role_name('https://github.com/octocat/Hello-World') == 'Hello-World'
    assert RoleRequirement().repo_url_to_role_name('git@github.com:octocat/Hello-World.git') == 'Hello-World'
    assert RoleRequirement().repo_url_to_role_name('http://bitbucket.org/user/repo') == 'repo'
    assert RoleRequirement().repo_url_to_role_name('http://bitbucket.org/user/repo/') == 'repo'
    assert RoleRequirement().repo_

# Generated at 2022-06-13 09:12:08.449135
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert "roles/winlib" == RoleRequirement.repo_url_to_role_name("roles/winlib")
    assert "role" == RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/role.git")
    assert "role" == RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/role.tar.gz")
    assert "role" == RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/role,v1.0.0")
    assert "role" == RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/role,v1.0.0,new_name")

# Generated at 2022-06-13 09:12:20.167104
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():

    assert RoleRequirement.repo_url_to_role_name("git@git.example.com:user/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/user/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("git+http://git.example.com/user/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("git+http://git.example.com/user/repo.git,v1.0") == "repo"

# Generated at 2022-06-13 09:12:26.663416
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():

    role_requirement = RoleRequirement()

    assert(role_requirement.repo_url_to_role_name("git://git.example.com/repos/repo.git") == "repo")
    assert(role_requirement.repo_url_to_role_name("git@git.example.com:repos/repo.git") == "repo")
    assert(role_requirement.repo_url_to_role_name("http://git.example.com/repos/repo.git") == "repo")
    assert(role_requirement.repo_url_to_role_name("https://git.example.com/repos/repo.git") == "repo")


# Generated at 2022-06-13 09:12:35.832694
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    print("Unit test for method role_yaml_parse of class RoleRequirement")
    test_role = {}
    test_role['name'] = "role_name"
    test_role['src'] = "src"
    test_role['scm'] = None
    test_role['version'] = ""
    test_role['role'] = "role_name"
    assert RoleRequirement.role_yaml_parse(test_role) == {'name': 'role_name', 'src': 'src', 'scm': None, 'version': ""}

    test_role['name'] = "role_name"
    test_role['src'] = "src,version"
    test_role['scm'] = None
    test_role['version'] = "version"
    test_role['role'] = "role_name"
   