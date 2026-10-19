

# Generated at 2022-06-13 09:03:01.148059
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():

    # Test case 1 : repo_url_to_role_name(repo_url) returns role name of repo_url
    assert RoleRequirement.repo_url_to_role_name("https://github.com/example/role.git") == "role"
    
    # Test case 2 : repo_url_to_role_name(role) returns role name of role
    assert RoleRequirement.repo_url_to_role_name("role") == "role"

    # Test case 3 : repo_url_to_role_name(repo_url) returns role name of repo_url
    assert RoleRequirement.repo_url_to_role_name("https://github.com/example/role-1.0.0.tar.gz") == "role"

    # Test case 4 : repo_url_to_role_name

# Generated at 2022-06-13 09:03:09.304979
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    role_requirement = RoleRequirement()
    print("RoleRequirement: test_RoleRequirement_repo_url_to_role_name():")
    print("role_requirement.repo_url_to_role_name('http://git.example.com/repos/repo.git') => %s" % role_requirement.repo_url_to_role_name('http://git.example.com/repos/repo.git'))
    print("role_requirement.repo_url_to_role_name('http@git.example.com/repos/repo.git') => %s" % role_requirement.repo_url_to_role_name('http@git.example.com/repos/repo.git'))

# Generated at 2022-06-13 09:03:15.527578
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    assert RoleRequirement.role_yaml_parse('nginx') == {'name': 'nginx', 'version': None, 'scm': None, 'src': 'nginx'}
    assert RoleRequirement.role_yaml_parse('nginx,v1.0') == {'name': 'nginx', 'version': 'v1.0', 'scm': None, 'src': 'nginx'}
    assert RoleRequirement.role_yaml_parse('nginx,v1.0,httpd') == {'name': 'httpd', 'version': 'v1.0', 'scm': None, 'src': 'nginx'}

# Generated at 2022-06-13 09:03:26.529689
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("https://bitbucket.org/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("https://example.com/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("git@github.com:example/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("https://github.com/example/repo.git") == "repo"

# Generated at 2022-06-13 09:03:37.194584
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name('https://github.com/user/repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('git+https://github.com/user/repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('git://git.example.com/repos/repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('github.com/user/repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_

# Generated at 2022-06-13 09:03:46.634667
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    # Valid single parameter
    assert RoleRequirement.role_yaml_parse('http://github.com/foo/bar') == dict(name='bar',
                                                                                src='http://github.com/foo/bar', 
                                                                                scm=None,
                                                                                version='')
    assert RoleRequirement.role_yaml_parse('http://github.com/foo/bar,v1.0') == dict(name='bar',
                                                                                      src='http://github.com/foo/bar', 
                                                                                      scm=None,
                                                                                      version='v1.0')

# Generated at 2022-06-13 09:03:55.985455
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    rr = RoleRequirement()
    result = rr.role_yaml_parse('travis-ci.org/ansible/ansible-spec,devel,spec')
    assert result == {'name': 'spec', 'src': 'travis-ci.org/ansible/ansible-spec', 'scm': None, 'version': 'devel'}
    result = rr.role_yaml_parse('travis-ci.org/ansible/ansible-spec+git')
    assert result == {'name': 'ansible-spec', 'src': 'travis-ci.org/ansible/ansible-spec', 'scm': 'git', 'version': None}

# Generated at 2022-06-13 09:04:03.272328
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    # Test for invalid role requirement
    try:
        role_requirement = RoleRequirement()
        role = role_requirement.role_yaml_parse('foo,bar,baz,foobar')
        assert False
    except AnsibleError as e:
        assert "Invalid role line (foo,bar,baz,foobar)" in e.message

    # Test for valid requirement with too many parameters
    role_requirement = RoleRequirement()
    role = role_requirement.role_yaml_parse('foo,bar,baz')
    assert role['name'] == 'baz'
    assert role['version'] == 'bar'
    assert role['src'] == 'foo'

    # Test for valid requirement with too many parameters
    role_requirement = RoleRequirement()
    role = role_requirement.role_yaml_parse

# Generated at 2022-06-13 09:04:13.077279
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    # test with complete scm urls
    assert RoleRequirement.repo_url_to_role_name("http://github.com/cliffano/ansible-roles.git") == "ansible-roles"
    assert RoleRequirement.repo_url_to_role_name("https://github.com/cliffano/ansible-roles.git") == "ansible-roles"
    assert RoleRequirement.repo_url_to_role_name("git@github.com:cliffano/ansible-roles.git") == "ansible-roles"

    # test with ssh scm urls
    assert RoleRequirement.repo_url_to_role_name("cliffano@github.com:cliffano/ansible-roles.git") == "ansible-roles"
   

# Generated at 2022-06-13 09:04:23.128105
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    role = dict(role='test')
    assert RoleRequirement.role_yaml_parse(role) == dict(name='test')

    role = 'test'
    assert RoleRequirement.role_yaml_parse(role) == dict(name='test')

    role = 'test,master'
    assert RoleRequirement.role_yaml_parse(role) == dict(name='test', version='master')

    role = 'test,master,newtest'
    assert RoleRequirement.role_yaml_parse(role) == dict(name='newtest', src='test', version='master')

    role = 'git@github.com:nagui/ansible.git'

# Generated at 2022-06-13 09:04:38.352914
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    """
    Unit test for method role_yaml_parse of class RoleRequirement
    """

    # test for a valid role
    valid_role = RoleRequirement.role_yaml_parse('geerlingguy.pip')
    assert valid_role
    assert valid_role['name'] == 'geerlingguy.pip'
    assert valid_role['version'] == ''
    assert valid_role['src'] == 'https://github.com/geerlingguy/ansible-role-pip'
    assert valid_role['scm'] == 'git'

    # test for invalid role syntax
    invalid_role = None

# Generated at 2022-06-13 09:04:49.039631
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    valid_role_specs = [
        "angstwad.foobar",
        "role_name,other,1.0",
        "http://git.example.com/repos/repo.git,tag",
        "git+https://github.com/user/repo,tag",
        "https://github.com/user/repo.git,tag",
        "git+https://github.com/user/repo.git,tag",
        "git+https://github.com/user/repo.git,tag,name",
        "git+git@github.com:user/repo.git"
    ]


# Generated at 2022-06-13 09:04:59.035003
# Unit test for method repo_url_to_role_name of class RoleRequirement

# Generated at 2022-06-13 09:05:10.076469
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    print("test_RoleRequirement_role_code_parse")

    result1 = RoleRequirement.role_yaml_parse(role='geerlingguy.mysql')
    if result1['src'] != 'geerlingguy.mysql':
        raise Exception("Fail: test 1 of role_yaml_parse")
    if result1['name'] != 'geerlingguy.mysql':
        raise Exception("Fail: test 2 of role_yaml_parse")
    if result1['scm'] is not None:
        raise Exception("Fail: test 3 of role_yaml_parse")
    if result1['version'] != '':
        raise Exception("Fail: test 4 of role_yaml_parse")


# Generated at 2022-06-13 09:05:19.535892
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    role_spec = "http://git.example.com/repos/repo.git,1.0,my_role"
    role = RoleRequirement.role_yaml_parse(role_spec)
    assert role is not None
    assert role['name'] == 'my_role'
    assert role['version'] == '1.0'
    assert role['scm'] is None
    assert role['src'] == 'http://git.example.com/repos/repo.git'

    role_spec = "http://git.example.com/repos/repo.git,1.0"
    role = RoleRequirement.role_yaml_parse(role_spec)
    assert role is not None
    assert role['name'] == 'repo'
    assert role['version'] == '1.0'
    assert role

# Generated at 2022-06-13 09:05:28.667965
# Unit test for method repo_url_to_role_name of class RoleRequirement

# Generated at 2022-06-13 09:05:40.346631
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/example.git') == 'example'
    assert RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/example.tar.gz') == 'example'
    assert RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/example,v1.tar.gz') == 'example'
    assert RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/example,v1') == 'example'
    assert RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/example,v1,name') == 'example'
    assert Role

# Generated at 2022-06-13 09:05:46.118007
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('git@git.example.com/repos/repo.git') == 'repo'


# Generated at 2022-06-13 09:05:53.796615
# Unit test for method repo_url_to_role_name of class RoleRequirement

# Generated at 2022-06-13 09:06:05.711840
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    assert RoleRequirement.role_yaml_parse("my.github.repo,v1.0") == { 'name': 'my.github.repo', 'src': 'my.github.repo', 'scm': None, 'version': 'v1.0' }
    assert RoleRequirement.role_yaml_parse("my.github.repo,v1.0") == { 'name': 'my.github.repo', 'src': 'my.github.repo', 'scm': None, 'version': 'v1.0' }
    assert RoleRequirement.role_yaml_parse("my.github.repo,v1.0,new_name") == { 'name': 'new_name', 'src': 'my.github.repo', 'scm': None, 'version': 'v1.0' }


# Generated at 2022-06-13 09:06:22.683164
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    # Case: default
    role = 'foo'
    r = RoleRequirement.role_yaml_parse(role)
    assert r['name'] == 'foo'
    assert r['src'] == 'foo'
    assert r['scm'] == None
    assert r['version'] == None

    # Case: scm + src + version
    role = 'git+https://github.com/myuser/myrole.git,0.9.6'
    r = RoleRequirement.role_yaml_parse(role)
    assert r['name'] == 'myrole'
    assert r['src'] == 'https://github.com/myuser/myrole.git'
    assert r['scm'] == 'git'
    assert r['version'] == '0.9.6'

    # Case: scm + src
    role

# Generated at 2022-06-13 09:06:35.419191
# Unit test for method role_yaml_parse of class RoleRequirement

# Generated at 2022-06-13 09:06:44.875813
# Unit test for method role_yaml_parse of class RoleRequirement

# Generated at 2022-06-13 09:06:50.390864
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    repo_url = "git@github.com:foo/bar.git"
    result = RoleRequirement.repo_url_to_role_name(repo_url)
    assert result == "bar"

    repo_url = "https://github.com/foo/bar.git"
    result = RoleRequirement.repo_url_to_role_name(repo_url)
    assert result == "bar"

    repo_url = "https://github.com/foo/bar.tar.gz"
    result = RoleRequirement.repo_url_to_role_name(repo_url)
    assert result == "bar"

    repo_url = "https://github.com/foo/bar,v1.2.3.tar.gz"
    result = RoleRequirement.repo_url_to_role_

# Generated at 2022-06-13 09:07:01.447623
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    role1 = {u'role': u'foo'}
    result = RoleRequirement.role_yaml_parse(role1)
    assert result == {u'name': u'foo', 'version': None, 'src': None, 'scm': None}

    role2 = {u'role': u'foo,1.0'}
    result = RoleRequirement.role_yaml_parse(role2)
    assert result == {u'name': u'foo', 'version': u'1.0', 'src': None, 'scm': None}

    role3 = {u'role': u'foo,baz,1.0'}
    try:
        result = RoleRequirement.role_yaml_parse(role3)
        assert False
    except AnsibleError:
        assert True


# Generated at 2022-06-13 09:07:06.084239
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    role_name = RoleRequirement.repo_url_to_role_name("https://github.com/ros-planning/moveit.git")
    assert role_name == "moveit"
    role_name = RoleRequirement.repo_url_to_role_name("https://github.com/ros-planning/moveit_robots.git")
    assert role_name == "moveit_robots"
    role_name = RoleRequirement.repo_url_to_role_name("https://github.com/ros-planning/moveit_robots.git,master")
    assert role_name == "moveit_robots"

# Generated at 2022-06-13 09:07:16.488774
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    from ansible.module_utils.six import PY3

    import types
    # The PY2 / PY3 distinction is made because
    # The dicts returned by dict() are not order preserving
    if PY3:
        assert (type(RoleRequirement.role_yaml_parse("role,1.2.3,name")) is dict)
        assert (type(RoleRequirement.role_yaml_parse("role,1.2.3")) is dict)
        assert (type(RoleRequirement.role_yaml_parse("role,v1.2.3")) is dict)
        assert (type(RoleRequirement.role_yaml_parse("role,1.2.3,")) is dict)
        assert (type(RoleRequirement.role_yaml_parse("role")) is dict)

# Generated at 2022-06-13 09:07:27.749033
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name("role") == "role"
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("https://github.com/user/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("git://git.example.com/repos/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("git@github.com:user/repo.git") == "repo"

# Generated at 2022-06-13 09:07:36.408136
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    repo_url = 'git@github.com:jdauphant/ansible-role-nginx.git'
    assert RoleRequirement.repo_url_to_role_name(repo_url) == 'ansible-role-nginx'
    repo_url = 'https://github.com/jdauphant/ansible-role-nginx.git'
    assert RoleRequirement.repo_url_to_role_name(repo_url) == 'ansible-role-nginx'
    repo_url = 'https://github.com/jdauphant/ansible-role-nginx,v1.0.0,jdauphant.nginx'
    assert RoleRequirement.repo_url_to_role_name(repo_url) == 'ansible-role-nginx'
    repo_

# Generated at 2022-06-13 09:07:46.797769
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    # single line role string
    print("TEST: role_yaml_parse - single line role string")
    role = "geerlingguy.apache,v2.2.3"
    result = RoleRequirement.role_yaml_parse(role)
    assert result == {'name': 'geerlingguy.apache', 'src': 'geerlingguy.apache', 'scm': None, 'version': 'v2.2.3'}

    # role dictionary without role key
    print("TEST: role_yaml_parse - role dictionary without role key")
    role = {"src": "git+https://github.com/geerlingguy/ansible-role-apache.git", "name": "apache", "scm": "git", "version": "v2.2.3"}
    result = RoleRequirement.role_

# Generated at 2022-06-13 09:08:02.007236
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    correct_result = dict(name='foo', src='https://github.com/foo/foo.git', scm='git', version='')
    assert RoleRequirement.role_yaml_parse('foo') == correct_result
    assert RoleRequirement.role_yaml_parse('foo,udated') == dict(correct_result, version='udated')
    assert RoleRequirement.role_yaml_parse('foo,udated,foo') == dict(correct_result, version='udated')
    assert RoleRequirement.role_yaml_parse('foo,udated,foo,bar') == dict(correct_result, version='udated,foo')
    assert RoleRequirement.role_yaml_parse('foo,udated,foo,bar,baz') == dict(correct_result, version='udated,foo')
    assert Role

# Generated at 2022-06-13 09:08:12.592825
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    require = RoleRequirement()

    # Test correct values

# Generated at 2022-06-13 09:08:26.984209
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    assert RoleRequirement.role_yaml_parse('https://github.com/hongqn/ansible-role-ansible.git,v1.0,ansible') == {
        'name': 'ansible',
        'src': 'https://github.com/hongqn/ansible-role-ansible.git',
        'scm': 'git',
        'version': 'v1.0'
    }

# Generated at 2022-06-13 09:08:40.239135
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    rr = RoleRequirement()

    # test with a string type argument
    str_test_arg = '''
    - src: https://github.com/jdauphant/ansible-role-nginx
      version: v1.0 # Version is optional
    '''
    ans = {'scm': 'git', 'src': 'https://github.com/jdauphant/ansible-role-nginx',
           'version': 'v1.0', 'name': 'ansible-role-nginx'}
    assert ans == rr.role_yaml_parse(str_test_arg)

    # test with a string and a name

# Generated at 2022-06-13 09:08:51.123222
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    role_str1 = "git+https://github.com/so1/so2"
    role_str2 = "git+https://github.com/so1/so2,master"
    role_str3 = "git+https://github.com/so1/so2,master,role_name_1"
    role_str4 = "https://github.com/so1/so2,role_name_1,master"
    role_str5 = "https://github.com/so1/so2"
    role_str6 = "https://github.com/so1/so2,master"
    role_str7 = "git+git@github.com:so1/so2,master,role_name_1"

# Generated at 2022-06-13 09:09:03.273109
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    # confirm simple name extraction from URL
    assert RoleRequirement.repo_url_to_role_name("https://github.com/foo/bar") == "bar"
    # confirm simple name extraction from URL, `.git` suffix removal
    assert RoleRequirement.repo_url_to_role_name("https://github.com/foo/bar.git") == "bar"
    # confirm simple name extraction from URL, `.tar.gz` suffix removal
    assert RoleRequirement.repo_url_to_role_name("https://github.com/foo/bar.tar.gz") == "bar"
    # confirm simple name extraction from URL, `.tar.gz` suffix removal, `.git` suffix removal

# Generated at 2022-06-13 09:09:15.214110
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    assert RoleRequirement.role_yaml_parse("geerlingguy.nginx,1.2.3") == {'name': u'geerlingguy.nginx', 'src': u'geerlingguy.nginx', 'scm': None, 'version': u'1.2.3'}
    assert RoleRequirement.role_yaml_parse("geerlingguy.nginx,1.2.3,test_name") == {'name': u'test_name', 'src': u'geerlingguy.nginx', 'scm': None, 'version': u'1.2.3'}

# Generated at 2022-06-13 09:09:24.302880
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    # Test for:
    # - src is a galaxy role
    # - name is not specified in string
    # - scm and version are not specified in string
    # - version is not specified in hash
    # - name is not specified in hash
    # - scm and src are specified in hash
    assert RoleRequirement.role_yaml_parse('example.role') == dict(
        name='example.role',
        src='example.role',
        scm=None,
        version='')

    assert RoleRequirement.role_yaml_parse(dict(src='example.role')) == dict(
        name='example.role',
        src='example.role',
        scm=None,
        version='')


# Generated at 2022-06-13 09:09:36.263965
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    '''test for repo_url_to_role_name method'''


# Generated at 2022-06-13 09:09:47.261405
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    from pprint import pprint


# Generated at 2022-06-13 09:10:04.632692
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    '''Test for method role_yaml_parse for class RoleRequirement'''
    role_requirement = RoleRequirement()
    # Case 1: Case with string as argument
    args = 'galaxy.role,version,name'
    expected_resuls = {'name': 'name', 'src': 'galaxy.role', 'scm': None, 'version': 'version'}
    assert(role_requirement.role_yaml_parse(args) == expected_resuls)

    # Case 2: Case with dictionary as argument
    args = {'role': 'galaxy.role,version,name'}
    expected_resuls = {'name': 'name', 'src': 'galaxy.role', 'scm': None, 'version': 'version'}

# Generated at 2022-06-13 09:10:13.032974
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    # Check function raises error on invalid role
    try:
        RoleRequirement.role_yaml_parse("invalid")
    except Exception:
        pass
    
    # Check function raises error on invalid role
    try:
        RoleRequirement.role_yaml_parse("invalid,invalid,invalid")
    except Exception:
        pass
    
    # Check function raises error on invalid role
    try:
        RoleRequirement.role_yaml_parse("invalid,invalid,invalid,invalid")
    except Exception:
        pass

    # Check function raises error on invalid role
    try:
        RoleRequirement.role_yaml_parse("invalid,invalid,invalid,invalid,invalid")
    except Exception:
        pass

    # Check function raises error on invalid role

# Generated at 2022-06-13 09:10:25.467360
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    assert RoleRequirement.role_yaml_parse('some_role') == {'name': 'some_role', 'version': '', 'src': 'some_role', 'scm': None}
    assert RoleRequirement.role_yaml_parse('some_role,v1.0') == {'name': 'some_role', 'version': 'v1.0', 'src': 'some_role', 'scm': None}
    assert RoleRequirement.role_yaml_parse('some_role,v1.0,other_name') == {'name': 'other_name', 'version': 'v1.0', 'src': 'some_role', 'scm': None}

# Generated at 2022-06-13 09:10:29.704193
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name('http://git.example.com/repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('git@git.example.com:repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('repo') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('repo.git.tar.gz') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('repo.tar.gz') == 'repo'
    assert RoleRequirement.repo_url_

# Generated at 2022-06-13 09:10:37.634397
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    from ansible.playbook.role.requirement import RoleRequirement
    parsed = RoleRequirement.role_yaml_parse('geerlingguy.jenkins,1.6.1')
    assert parsed['name'] == 'geerlingguy.jenkins'
    assert parsed['version'] == '1.6.1'
    assert parsed['scm'] is None
    assert parsed['src'] == 'geerlingguy.jenkins'

    parsed = RoleRequirement.role_yaml_parse('geerlingguy.jenkins')
    assert parsed['name'] == 'geerlingguy.jenkins'
    assert parsed['version'] == ''
    assert parsed['scm'] is None
    assert parsed['src'] == 'geerlingguy.jenkins'


# Generated at 2022-06-13 09:10:48.835628
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    import ansible.playbook.role.definition

# Generated at 2022-06-13 09:10:57.807141
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    role = "foo"
    role_dict = RoleRequirement.role_yaml_parse(role)
    assert role_dict['name'] == 'foo'
    assert role_dict['src'] == 'foo'
    assert role_dict['scm'] is None
    assert role_dict['version'] is None

    role = "foo, master"
    role_dict = RoleRequirement.role_yaml_parse(role)
    assert role_dict['name'] == 'foo'
    assert role_dict['src'] == 'foo'
    assert role_dict['scm'] is None
    assert role_dict['version'] == 'master'

    role = "git+https://foo, master"
    role_dict = RoleRequirement.role_yaml_parse(role)
    assert role_dict['name'] == 'foo'


# Generated at 2022-06-13 09:11:05.654320
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    tests = [
        ('repo', 'repo'),
        ('http://git.example.com/repos/repo.git', 'repo'),
        ('http://git.example.com/repos/repo,1.0.git', 'repo,1.0'),
        ('https://github.com/user/repo.git', 'repo'),
        ('git@github.com:user/repo.git', 'repo'),
        ('user@ssh.example.com:repo.git', 'repo'),
    ]

    for test, result in tests:
        actual = RoleRequirement.repo_url_to_role_name(test)

# Generated at 2022-06-13 09:11:15.560683
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
   assert RoleRequirement.repo_url_to_role_name('git@github.com:user-name/ansible-role.git') == 'ansible-role'
   assert RoleRequirement.repo_url_to_role_name('https://github.com/user-name/ansible-role.git') == 'ansible-role'
   assert RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo.git') == 'repo'
   assert RoleRequirement.repo_url_to_role_name('https://user-name@github.com/user-name/ansible-role.git') == 'ansible-role'

# Generated at 2022-06-13 09:11:24.621174
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    role_req = RoleRequirement()

    # Use cases for new style role requirements in role requirement files
    # test case 1: 'role_name,version,name' where name is optional
    # test case 2: 'src: "galaxy.role,version,name", other_vars: "here"' where name is optional

    # Test case 1: role_name,version,name
    data = 'my-role,1.0.0,RoleName'
    expected_result = {'name': 'RoleName', 'src': 'my-role', 'scm': None, 'version': '1.0.0'}

    result = role_req.role_yaml_parse(data)
    assert result == expected_result, "Expected %s but got %s" % (expected_result, result)


# Generated at 2022-06-13 09:11:47.612010
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    assert RoleRequirement.role_yaml_parse('geerlingguy.apache') == {'name': 'geerlingguy.apache', 'src': 'geerlingguy.apache', 'version': '', 'scm': None}
    assert RoleRequirement.role_yaml_parse('geerlingguy.apache,1.2.3') == {'name': 'geerlingguy.apache', 'src': 'geerlingguy.apache', 'version': '1.2.3', 'scm': None}
    assert RoleRequirement.role_yaml_parse('geerlingguy.apache,1.2.3,apache') == {'name': 'apache', 'src': 'geerlingguy.apache', 'version': '1.2.3', 'scm': None}
    assert RoleRequirement.role_yaml_parse

# Generated at 2022-06-13 09:12:01.128700
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    roleRequirement = RoleRequirement()

# Generated at 2022-06-13 09:12:08.023334
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    """
    Test role_yaml_parse method

    :return:
    """

    def _print(str_):
        print(str_)

    def _assert(func, expected, msg=''):
        try:
            assert func == expected
            _print("{0}: OK".format(msg))
        except AssertionError:
            _print("{0}: FAILED".format(msg))


    _assert(RoleRequirement.role_yaml_parse('git+https://github.com/jdauphant/ansible-role-nginx.git'),
            {'name': 'ansible-role-nginx', 'src': 'https://github.com/jdauphant/ansible-role-nginx.git', 'scm': 'git', 'version': ''},
            'basic entry')
    _

# Generated at 2022-06-13 09:12:19.955296
# Unit test for method role_yaml_parse of class RoleRequirement

# Generated at 2022-06-13 09:12:26.495506
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name('foo') == 'foo'
    assert RoleRequirement.repo_url_to_role_name('git+git://git.example.net/repos/repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('https://github.com/geerlingguy/ansible-role-apache') == 'ansible-role-apache'
    assert RoleRequirement.repo_url_to_role_name('https://github.com/geerlingguy/ansible-role-apache.git') == 'ansible-role-apache'

# Generated at 2022-06-13 09:12:35.737832
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    """Define a method to unit test role_yaml_parse function"""
    from ansible.utils.display import Display
    from ansible.utils import plugin_docs
    from ansible.plugins.doc_fragments import DOCUMENTABLE_PLUGIN_KINDS
    from ansible.module_utils.common import ANSIBLE_TEST_DATA_ROOT
    from ansible.utils.plugin_docs import read_docstub
    import os
    import yaml
    display = Display()

    # If a docstub contains metadata, the sections of the
    # docstub are guaranteed to be in the same order as DOCUMENTABLE_PLUGIN_KINDS.
    # As a result, we can iterate through the docstub sections and produce
    # a dict that maps strings of plugin kind to each docstub section