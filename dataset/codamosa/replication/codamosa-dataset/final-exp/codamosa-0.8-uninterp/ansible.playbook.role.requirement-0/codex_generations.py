

# Generated at 2022-06-13 09:02:51.442594
# Unit test for method repo_url_to_role_name of class RoleRequirement

# Generated at 2022-06-13 09:03:02.291206
# Unit test for method role_yaml_parse of class RoleRequirement

# Generated at 2022-06-13 09:03:12.871018
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    from ansible.playbook.role.definition import RoleDefinition

    # old style
    assert RoleRequirement.role_yaml_parse("role") == {'name': 'role', 'src': 'role', 'scm': None, 'version': None}
    assert RoleRequirement.role_yaml_parse("role,v0.1.0") == {'name': 'role', 'src': 'role', 'scm': None, 'version': 'v0.1.0'}
    assert RoleRequirement.role_yaml_parse("role,v0.1.0,custom_name") == {'name': 'custom_name', 'src': 'role', 'scm': None, 'version': 'v0.1.0'}

    # new style

# Generated at 2022-06-13 09:03:22.102134
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.urls import open_url
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    # Test case 1
    role = "https://github.com/user/repo.git,master,role_name"
    result = dict(name='role_name', scm='git', src='https://github.com/user/repo.git', version='master')
    assert(result == RoleRequirement.role_yaml_parse(role))

    # Test case 2
    role = dict(role='user.repo,master')
    result = dict(name='user.repo', scm=None, src='user.repo', version='master')

# Generated at 2022-06-13 09:03:31.743356
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    # Test 1
    role = RoleRequirement.role_yaml_parse('user.role')
    assert role == { 'name': 'user.role', 'scm': None, 'src': 'user.role', 'version': '' }

    # Test 2
    role = RoleRequirement.role_yaml_parse('user.role,master')
    assert role == { 'name': 'user.role', 'scm': None, 'src': 'user.role', 'version': 'master' }

    # Test 3
    role = RoleRequirement.role_yaml_parse('user.role,master,foobar')
    assert role == { 'name': 'foobar', 'scm': None, 'src': 'user.role', 'version': 'master' }

    # Test 4
    role = RoleRequirement.role_yaml_parse

# Generated at 2022-06-13 09:03:34.561629
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name(
        'https://github.com/user/role') == 'role'



# Generated at 2022-06-13 09:03:46.297114
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    # [1] Test for invalid old style role line:
    # Invalid old style role line (a,b,c), the proper format is 'role_name[,version[,name]]'
    inv_role_line = "a,b,c"
    try:
        RoleRequirement.role_yaml_parse(inv_role_line)
        assert False, "RoleRequirement.role_yaml_parse() should not accept invalid role line: '%s', but it does!" % inv_role_line
    except AnsibleError:
        pass

    # [2] Test for old style role line:
    # Proper format: role_name[,version[,name]]
    # Proper format: role_name,version,name
    # Proper format: role_name,version
    # Proper format: role_name
    # The result should be

# Generated at 2022-06-13 09:03:50.873578
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    EXPECTED_NAME = 'ansible-role-test'
    URL = 'https://github.com/repo/{}.git'.format(EXPECTED_NAME)
    assert RoleRequirement.repo_url_to_role_name(URL) == EXPECTED_NAME

# Generated at 2022-06-13 09:04:05.329754
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    role_requirement_class = RoleRequirement()
    url_without_git_postfix = 'https://github.com/ansible/ansible-galaxy-local'
    git_url = url_without_git_postfix + '.git'
    tar_url = url_without_git_postfix + '.tar.gz'
    tar_url_with_name = tar_url + ',name'
    assert 'ansible-galaxy-local' == role_requirement_class.repo_url_to_role_name(git_url)
    assert 'ansible-galaxy-local' == role_requirement_class.repo_url_to_role_name(tar_url)

# Generated at 2022-06-13 09:04:05.962038
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    pass

# Generated at 2022-06-13 09:04:39.210085
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name("foo") == "foo"
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.git,1.0.0") == "repo"
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.git,1.0.0,bar") == "bar"
    assert RoleRequirement.repo_url_to_role_name("git://git.example.com/repos/repo.git") == "repo"

# Generated at 2022-06-13 09:04:50.008294
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    # Test string case
    assert RoleRequirement.role_yaml_parse('http://github.com/myorg/myrole,1.0.0').__eq__({'name': 'myrole', 'version': '1.0.0', 'src': 'http://github.com/myorg/myrole', 'scm': None})
    assert RoleRequirement.role_yaml_parse('https://github.com/myorg/myrole,1.0.0').__eq__({'name': 'myrole', 'version': '1.0.0', 'src': 'https://github.com/myorg/myrole', 'scm': None})

# Generated at 2022-06-13 09:04:59.744364
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    # Import Ansible's testing framework
    import pytest

    # Check for expected exception when more than two commas in role
    # specification
    with pytest.raises(AnsibleError) as excinfo:
        role = RoleRequirement.role_yaml_parse("role,version,name,another-name")
    assert 'Invalid role line' in str(excinfo.value)

    # Check for expected exception when role specification doesn't contain
    # a comma
    with pytest.raises(AnsibleError) as excinfo:
        role = RoleRequirement.role_yaml_parse("http://git.example.com/repos/repo.git")
    assert 'Invalid role line' in str(excinfo.value)

    # Check for expected exception when role specification is a list

# Generated at 2022-06-13 09:05:13.295899
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    # Test URL without suffix
    src1 = "http://git.example.com/repos/repo"
    assert RoleRequirement.repo_url_to_role_name(src1) == "repo"

    # Test URL with suffix ".git"
    src2 = "http://git.example.com/repos/repo.git"
    assert RoleRequirement.repo_url_to_role_name(src2) == "repo"

    # Test URL with suffix ".tar.gz"
    src3 = "http://git.example.com/repos/repo.tar.gz"
    assert RoleRequirement.repo_url_to_role_name(src3) == "repo"

    # Test URL that contains a file name

# Generated at 2022-06-13 09:05:23.064545
# Unit test for method role_yaml_parse of class RoleRequirement

# Generated at 2022-06-13 09:05:31.817756
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('git://git.example.com/repos/repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('git@git.example.com:repos/repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('some-user-some-repo.git') == 'some-user-some-repo'
    assert RoleRequirement.repo_url_to_role_name('some-user-some-repo') == 'some-user-some-repo'
    assert RoleRequ

# Generated at 2022-06-13 09:05:37.830675
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    role_str_1 = 'geerlingguy.apache'
    role_str_2 = 'geerlingguy.apache,v1.2.3'
    role_str_3 = 'geerlingguy.apache,v1.2.3,apache'
    #role_str_4 = 'http://github.com/geerlingguy/ansible-role-apache.git,v1.2.3,apache'
    role_str_4 = 'git+https://github.com/geerlingguy/ansible-role-apache.git,v1.2.3,apache'
    role_str_5 = 'apache,v1.2.3,apache'
    role_str_6 = 'apache,v1.2.3'

# Generated at 2022-06-13 09:05:49.202453
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name(None) is None
    assert RoleRequirement.repo_url_to_role_name('') is None
    assert RoleRequirement.repo_url_to_role_name('http://www.example.com') is None
    assert RoleRequirement.repo_url_to_role_name('http://www.example.com/a') == 'a'
    assert RoleRequirement.repo_url_to_role_name('http://www.example.com/a+b') == 'a'
    assert RoleRequirement.repo_url_to_role_name('http://www.example.com/a/b') == 'b'

# Generated at 2022-06-13 09:06:02.380780
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    # The parameters to the function are:
    function_name = 'repo_url_to_role_name'

# Generated at 2022-06-13 09:06:10.292479
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('https://github.com/repo/repo.git,v0.9.6') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('git@github.com:repo/repo.git,v0.9.6') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('git@github.com:repo/repo.git,v0.9.6,ansible-role-zabbix-repo') == 'repo'
    assert RoleRequirement.repo_url_to_role_name

# Generated at 2022-06-13 09:06:39.574689
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name('https://github.com/ansible/ansible-examples.git') == 'ansible-examples'
    assert RoleRequirement.repo_url_to_role_name('git@github.com:ansible/ansible-examples.git') == 'ansible-examples'
    assert RoleRequirement.repo_url_to_role_name('ansible-examples') == 'ansible-examples'
    assert RoleRequirement.repo_url_to_role_name('ansible-examples.git') == 'ansible-examples'
    assert RoleRequirement.repo_url_to_role_name('git+https://github.com/ansible/ansible-examples.git') == 'ansible-examples'

# Generated at 2022-06-13 09:06:51.196630
# Unit test for method repo_url_to_role_name of class RoleRequirement

# Generated at 2022-06-13 09:07:02.315286
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    #1) Test the wrong input type
    try: 
        RoleRequirement.role_yaml_parse(dict())
    except AnsibleError as e:
        assert(str(e) == 'Role definition must be a string, got <type \'dict\'>')
    #2) Test the role with name (without scm and version)
    result = RoleRequirement.role_yaml_parse("name")
    assert(result['name'] == 'name')
    #3) Test the role with name, version (without scm)
    result = RoleRequirement.role_yaml_parse("name,version")
    assert(result['name'] == 'name')
    assert(result['version'] == 'version')
    #4) Test the role with name, version, src

# Generated at 2022-06-13 09:07:11.190026
# Unit test for method role_yaml_parse of class RoleRequirement

# Generated at 2022-06-13 09:07:16.387976
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    import sys
    import os
    import json
    from ansible.module_utils.common.collections import is_sequence
    from ansible.module_utils.six import string_types

    display = Display()
    display.verbosity = 4

    rr = RoleRequirement()

    assert rr.role_yaml_parse("foo") == { 'name': 'foo', 'scm': None, 'src': 'foo', 'version': '' }
    assert rr.role_yaml_parse("foo,bar") == { 'name': 'foo', 'scm': None, 'src': 'foo', 'version': 'bar' }

# Generated at 2022-06-13 09:07:27.595429
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    print ("\n##### Testing RoleRequirement.role_yaml_parse #####")
    role = 'scm+http://git.example.com/repos/repo.git,3.3'
    expected_dict = {'name': 'repo', 'src': 'http://git.example.com/repos/repo.git', 'scm': 'scm', 'version': '3.3'}
    actual_dict = RoleRequirement.role_yaml_parse(role)
    assert expected_dict == actual_dict

    role = {"role":'scm+http://git.example.com/repos/repo.git,3.3'}

# Generated at 2022-06-13 09:07:37.691793
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    assert RoleRequirement.role_yaml_parse("git+https://github.com/geerlingguy/ansible-role-ntp.git") == \
           dict(name=RoleRequirement.repo_url_to_role_name("git+https://github.com/geerlingguy/ansible-role-ntp.git"),
                src="https://github.com/geerlingguy/ansible-role-ntp.git",
                scm="git", version=None)

# Generated at 2022-06-13 09:07:48.325906
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    role_defn = RoleRequirement()
    role_string = 'Username.name,1.2.3,myname'
    role_details = role_defn.role_yaml_parse(role_string)
    assert dict(role=role_string) == {'role' : role_string}
    assert dict(name=role_details.get('name'), src=role_details.get('src'), scm=role_details.get('scm'), version=role_details.get('version')) == dict(name='myname', src='Username.name', scm=None, version='1.2.3')
    role_string = 'Username.name,1.2.3'
    role_details = role_defn.role_yaml_parse(role_string)

# Generated at 2022-06-13 09:07:57.752582
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    role1 = "http://git.example.com/repos/repo.git"
    role2 = "http://git.example.com/repos/repo.tar.gz"
    role3 = "https://github.com/username/repo.git"
    role4 = "https://github.com/username/repo.tar.gz"
    role5 = "https://github.com/username/repo,v1.0.0"
    role6 = "git+https://github.com/username/repo.git,v1.0.0"
    role7 = "git+https://github.com/username/repo.git,v1.0.0,some_name"
    role8 = "github.com/username/repo.git"

# Generated at 2022-06-13 09:08:04.040206
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    from ansible.errors import AnsibleError
    from ansible.module_utils._text import to_native


# Generated at 2022-06-13 09:09:15.413533
# Unit test for method repo_url_to_role_name of class RoleRequirement

# Generated at 2022-06-13 09:09:24.437018
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('https://git.example.com/repos/role1.git') == 'role1'
    assert RoleRequirement.repo_url_to_role_name('git@git.example.com:repos/role2.git') == 'role2'
    assert RoleRequirement.repo_url_to_role_name('https://git.example.com/repos/role3,v1.2.3') == 'role3'
    assert RoleRequirement.repo_url_to_role_name('git@git.example.com:repos/role4,v1.2.3')

# Generated at 2022-06-13 09:09:30.630804
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    assert RoleRequirement.role_yaml_parse("geerlingguy.apache") == {'name': 'geerlingguy.apache', 'src': 'geerlingguy.apache', 'scm': None, 'version': ''}
    assert RoleRequirement.role_yaml_parse("geerlingguy.apache,1.0.0") == {'name': 'geerlingguy.apache', 'src': 'geerlingguy.apache', 'scm': None, 'version': '1.0.0'}
    assert RoleRequirement.role_yaml_parse("geerlingguy.apache,1.0.0,bar") == {'name': 'bar', 'src': 'geerlingguy.apache', 'scm': None, 'version': '1.0.0'}
    assert RoleRequirement.role_yaml

# Generated at 2022-06-13 09:09:40.083163
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    assert(RoleRequirement.role_yaml_parse("http://git.example.com/repos/repo.git") == {
        'name': 'repo',
        'src': 'http://git.example.com/repos/repo.git',
        'scm': 'git',
        'version': None
        })

    assert(RoleRequirement.role_yaml_parse("http://git.example.com/repos/repo.git,v1.2") == {
        'name': 'repo',
        'src': 'http://git.example.com/repos/repo.git',
        'scm': 'git',
        'version': 'v1.2'
        })


# Generated at 2022-06-13 09:09:51.854244
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo.tar.gz') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo,v0.1') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('git@git.example.com/repos/repo.git') == 'repo'

# Generated at 2022-06-13 09:10:02.242203
# Unit test for method role_yaml_parse of class RoleRequirement

# Generated at 2022-06-13 09:10:11.376082
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.git,v1.0") == "repo"
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.git,v1.0,other_role_name") == "repo"
    assert RoleRequirement.repo_url_to_role_name("https://gitlab.com/gitlab-org/gitlab-ce.git,v11.3.0") == "gitlab-ce"
    assert RoleRequirement.repo_url_to_role_

# Generated at 2022-06-13 09:10:15.581647
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    url = "http://git.example.com/repos/repo.git"
    role_name = RoleRequirement.repo_url_to_role_name(url)
    assert role_name == "repo"

# Generated at 2022-06-13 09:10:22.218305
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name("role_name[,version[,name]]") == "role_name[,version[,name]]"
    assert RoleRequirement.repo_url_to_role_name("../galaxy_role_name[,version[,name]]") == "galaxy_role_name[,version[,name]]"
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("git@git.example.com:repos/repo.git") == "repo"

# Generated at 2022-06-13 09:10:33.898424
# Unit test for method repo_url_to_role_name of class RoleRequirement

# Generated at 2022-06-13 09:11:13.905148
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    def _parse_role(role):
        return RoleRequirement.role_yaml_parse(role)

    assert _parse_role('user.role') == {'name': 'user.role', 'scm': None, 'src': 'user.role', 'version': ''}
    assert _parse_role('user.role.') == {'name': 'user.role.', 'scm': None, 'src': 'user.role.', 'version': ''}
    assert _parse_role('user.role,1.0') == {'name': 'user.role', 'scm': None, 'src': 'user.role', 'version': '1.0'}

# Generated at 2022-06-13 09:11:24.411799
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    '''
    Test class RoleRequirement's role_yaml_parse method
    '''
    # Test 1: Test with only role name
    role = RoleRequirement.role_yaml_parse('role1')
    assertion1 = role['name'] == 'role1'
    assertion2 = role['src'] == 'role1'
    assertion3 = role['scm'] is None
    assertion4 = role['version'] == ''
    assertion5 = len(role) == 4
    assert assertion1 and assertion2 and assertion3 and assertion4 and assertion5

    # Test 2: Test old style with comma
    role = RoleRequirement.role_yaml_parse('role1,v1')
    assertion1 = role['name'] == 'role1'
    assertion2 = role['src'] == 'role1'

# Generated at 2022-06-13 09:11:34.592118
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    # Test case 1: { src: 'galaxy.role,version,name', other_vars: "here" }
    role = { 'src': 'galaxy.role,version,name', 'other_vars': "here" }
    rr = RoleRequirement()
    role_dict = rr.role_yaml_parse(role)
    assert role_dict['scm'] == None
    assert role_dict['src'] == 'galaxy.role'
    assert role_dict['version'] == 'version'
    assert role_dict['name'] == 'name'

    # Test case 2: 'galaxy.role,version,name'
    role = 'galaxy.role,version,name'
    rr = RoleRequirement()
    role_dict = rr.role_yaml_parse(role)
    assert role

# Generated at 2022-06-13 09:11:44.134631
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    #case1: test string
    role_string = "tomcat"
    expect_result = {'name': "tomcat", 'src': "tomcat", 'scm': None, 'version': None}
    result = RoleRequirement.role_yaml_parse(role_string)
    assert expect_result == result

    #case2: test dictionary
    role_dic = {'role': "tomcat", 'version': "2.0.0"}
    expect_result = {'name': "tomcat", 'src': "tomcat", 'scm': None, 'version': "2.0.0"}
    result = RoleRequirement.role_yaml_parse(role_dic)
    assert expect_result == result

    #case3: test dictionary about src and version

# Generated at 2022-06-13 09:11:55.520719
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    assert RoleRequirement.role_yaml_parse("kickstart-centos") == {
        'name': 'kickstart-centos',
        'role': None,
        'scm': None,
        'src': None,
        'version': None
    }

    assert RoleRequirement.role_yaml_parse("git+https://github.com/fubarhouse/ansible-role-yum") == {
        'name': 'ansible-role-yum',
        'role': None,
        'scm': 'git',
        'src': 'https://github.com/fubarhouse/ansible-role-yum',
        'version': None
    }


# Generated at 2022-06-13 09:12:04.302558
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    # Test if the URL has no protocol and no @
    test1 = "git.example.com/repos/repo.git"
    assert RoleRequirement.repo_url_to_role_name(test1) == "repo"

    # Test if the URL has a protocol
    test2 = "https://github.com/Neilpang/ansible-ssh-hardening.git"
    assert RoleRequirement.repo_url_to_role_name(test2) == "ansible-ssh-hardening"

    # Test if the URL contains @
    test3 = "git@github.com:Neilpang/ansible-ssh-hardening.git"
    assert RoleRequirement.repo_url_to_role_name(test3) == "ansible-ssh-hardening"

    # Test if the URL has

# Generated at 2022-06-13 09:12:10.509643
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    assert RoleRequirement.role_yaml_parse("foo") == dict(
        name='foo', src=None, version='', scm=None
    )
    assert RoleRequirement.role_yaml_parse("foobar") == dict(
        name='foobar', src=None, version='', scm=None
    )
    assert RoleRequirement.role_yaml_parse("foo,1.0") == dict(
        name='foo', src=None, version='1.0', scm=None
    )
    assert RoleRequirement.role_yaml_parse("git+git://foo.git") == dict(
        name='foo', src=None, version='', scm='git'
    )
    assert RoleRequirement.role_yaml_parse("git+git://foo.git,2.0") == dict

# Generated at 2022-06-13 09:12:21.008423
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    role_name = 'test'
    # legacy style
    legacy_style = RoleRequirement.role_yaml_parse(role='ansible-galaxy:%s' % role_name)
    assert legacy_style['name'] == role_name and legacy_style['src'] == role_name
    # new style
    new_style = RoleRequirement.role_yaml_parse(role=dict(src='ansible-galaxy:%s' % role_name))
    assert new_style['name'] == role_name and new_style['src'] == role_name

    # legacy style with version
    legacy_style = RoleRequirement.role_yaml_parse(role='ansible-galaxy:%s,version=%s' % (role_name, 'v0.3.2'))

# Generated at 2022-06-13 09:12:27.395668
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    assert RoleRequirement.role_yaml_parse("geerlingguy.nginx") == {'scm': None, 'src': 'geerlingguy.nginx', 'version': None, 'name': 'nginx'}
    assert RoleRequirement.role_yaml_parse("geerlingguy.nginx,2.8.1") == {'scm': None, 'src': 'geerlingguy.nginx', 'version': '2.8.1', 'name': 'nginx'}

# Generated at 2022-06-13 09:12:36.238653
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    role = 'cobbler,1.2.3,name'
    assert dict(name='name', src='cobbler', scm=None, version='1.2.3') == RoleRequirement.role_yaml_parse(role)

    role = 'cobbler+http://git.example.com/repos/repo.git,1.2.3,name'
    assert dict(name='name', src='http://git.example.com/repos/repo.git', scm='cobbler', version='1.2.3') == RoleRequirement.role_yaml_parse(role)

    role = 'http://git.example.com/repos/repo.git,1.2.3,name'