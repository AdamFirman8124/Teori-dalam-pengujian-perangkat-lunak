

# Generated at 2022-06-13 09:02:59.363345
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    url_as_git_http1 = 'http://git.example.com/repos/repo.git'
    assert RoleRequirement.repo_url_to_role_name(url_as_git_http1) == 'repo'

    url_as_git_http2 = 'http://git.example2.com/repos/repo2.git'
    assert RoleRequirement.repo_url_to_role_name(url_as_git_http2) == 'repo2'

    url_as_git_http3 = 'http://git.example2.com/repos/repo2.git,master'
    assert RoleRequirement.repo_url_to_role_name(url_as_git_http3) == 'repo2'


# Generated at 2022-06-13 09:03:10.346284
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    display.verbosity = 3
    role = dict(role="geerlingguy.java")
    result = RoleRequirement.role_yaml_parse(role)

    assert result['name'] == "geerlingguy.java"
    assert result['src'] == "geerlingguy.java"
    assert result['scm'] == None
    assert result['version'] == ''

    role = dict(role="geerlingguy.jenkins, v1.1.1")
    result = RoleRequirement.role_yaml_parse(role)

    assert result['name'] == "geerlingguy.jenkins"
    assert result['src'] == "geerlingguy.jenkins"
    assert result['scm'] == None
    assert result['version'] == "v1.1.1"


# Generated at 2022-06-13 09:03:20.786980
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name('https://github.com/stevenharris/ansible-galaxy-dustin-test.git') == 'ansible-galaxy-dustin-test'
    assert RoleRequirement.repo_url_to_role_name('git@github.com:stevenharris/ansible-galaxy-dustin-test.git') == 'ansible-galaxy-dustin-test'
    assert RoleRequirement.repo_url_to_role_name('https://github.com/stevenharris/ansible-galaxy-dustin-test.git') == 'ansible-galaxy-dustin-test'

# Generated at 2022-06-13 09:03:30.666252
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    """
    Test for method role_yaml_parse of class RoleRequirement
    """
    # test for string_types
    assert RoleRequirement.role_yaml_parse("http://git.example.com/repos/repo.git") == {'src': 'http://git.example.com/repos/repo.git', 'name': 'repo', 'scm': 'git', 'version': None}
    assert RoleRequirement.role_yaml_parse("http://git.example.com/repos/repo.git,v1.0") == {'src': 'http://git.example.com/repos/repo.git', 'name': 'repo', 'scm': 'git', 'version': 'v1.0'}

# Generated at 2022-06-13 09:03:35.075699
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name("git+https://github.com/username/reponame.git") == "reponame"
    assert RoleRequirement.repo_url_to_role_name("username/reponame") == "reponame"


# Generated at 2022-06-13 09:03:46.842760
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():

    # Testing role name extraction from git repo url
    # http://git.example.com/repos/repo.git" => "repo"
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.git") == "repo"

    # Testing role name extraction from git repo url with .git suffix
    # http://git.example.com/repos/repo" => "repo"
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo") == "repo"

    # Testing role name extraction from git repo url with @
    # git+http://git.example.com/repos/repo.git" => "repo"
    assert RoleRequirement.repo_url_to

# Generated at 2022-06-13 09:03:56.105947
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    assert RoleRequirement.role_yaml_parse('name,version,role_name') == {'name': 'role_name', 'src': 'name', 'scm': None, 'version': 'version'}
    assert RoleRequirement.role_yaml_parse('scm+name,version,role_name') == {'name': 'role_name', 'src': 'name', 'scm': 'scm', 'version': 'version'}
    assert RoleRequirement.role_yaml_parse('name,version') == {'name': 'name', 'src': 'name', 'scm': None, 'version': 'version'}

# Generated at 2022-06-13 09:04:03.346389
# Unit test for method repo_url_to_role_name of class RoleRequirement

# Generated at 2022-06-13 09:04:13.119151
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    # pylint: disable=missing-docstring
    import os
    import sys

    test_repo_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    # If running tests from a checkout add the parent dir to the path,
    # so ansible.galaxy can be found.
    if os.path.exists(os.path.join(test_repo_dir, 'lib', 'ansible')):
        sys.path.insert(1, test_repo_dir)

    from ansible.galaxy import Galaxy
    galaxy = Galaxy()
    galaxy.roles_path = galaxy.roles_paths()

    from ansible.galaxy.role import RoleRequirement


# Generated at 2022-06-13 09:04:23.167617
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    role_requirement = RoleRequirement()


# Generated at 2022-06-13 09:04:57.751426
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    test_datas = {}
    test_datas[0] = ["", ""]
    test_datas[1] = ["http://git.example.com/repos/repo.git", "repo"]
    test_datas[2] = ["https://git.example.com/repos/repo.git", "repo"]
    test_datas[3] = ["git@git.example.com:repos/repo.git", "repo"]
    test_datas[4] = ["repo.git", "repo"]
    test_datas[5] = ["repo.tar.gz", "repo"]
    test_datas[6] = ["repo1,repo2", "repo1"]

# Generated at 2022-06-13 09:05:05.250537
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    role_req = RoleRequirement()
    with open('test/unit/galaxy/test_data/role_requirement.yml', 'r') as f:
        test_role = yaml.safe_load(f)
    for test_spec in test_role:
        # Skip the test_spec in the test data yet not handled
        if test_spec['expected_return'] is None:
            continue
        # Parse the role using the role_yaml_parse method
        test_case = role_req.role_yaml_parse(test_spec['role'])
        # Test the parsed role against the expected_return
        assert test_case==test_spec['expected_return']

# Generated at 2022-06-13 09:05:17.917907
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    role = RoleRequirement.role_yaml_parse("role_name")
    assert (role['name'] == "role_name")

    role = RoleRequirement.role_yaml_parse("role_name,1.0")
    assert (role['name'] == "role_name")
    assert (role['version'] == "1.0")

    role = RoleRequirement.role_yaml_parse("rolename,v1")
    assert (role['name'] == "rolename")
    assert (role['version'] == "v1")

    role = RoleRequirement.role_yaml_parse("role_name,v1,name")
    assert (role['name'] == "name")
    assert (role['version'] == "v1")


# Generated at 2022-06-13 09:05:27.442749
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    # Test new style
    assert RoleRequirement.role_yaml_parse(dict(role = 'testrole,1.0')) == dict(name = 'testrole', version = '1.0')
    assert RoleRequirement.role_yaml_parse(dict(src='testrole,1.0')) == dict(name = 'testrole', version = '1.0')
    assert RoleRequirement.role_yaml_parse(dict(src='testrole,1.0,newname')) == dict(name = 'newname', version = '1.0')
    assert RoleRequirement.role_yaml_parse(dict(src='git+git://github.com/user1/testrole.git,1.0,newname')) == dict(name = 'newname', version = '1.0', scm = 'git')

# Generated at 2022-06-13 09:05:31.239600
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    from ansible.utils.display import Display
    display = Display()

    role_url = "http://git.example.com/path/to/role.git"
    role_name = RoleRequirement().repo_url_to_role_name(role_url)

    assert role_name == "role"
    display.display("Test passed")

# Generated at 2022-06-13 09:05:43.339077
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    # Tests for specs with a non dict value.
    assert (RoleRequirement.role_yaml_parse('git+https://github.com/cloudalchemy/ansible-role-cassandra.git') ==
            {'name': 'ansible-role-cassandra', 'src': 'https://github.com/cloudalchemy/ansible-role-cassandra.git', 'scm': 'git', 'version': ''})
    assert (RoleRequirement.role_yaml_parse('https://github.com/cloudalchemy/ansible-role-cassandra') ==
            {'name': 'ansible-role-cassandra', 'src': 'https://github.com/cloudalchemy/ansible-role-cassandra', 'scm': None, 'version': ''})

    # Tests for specs with a dict value.

# Generated at 2022-06-13 09:05:52.708701
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    from ansible.utils.display import Display
    from ansible.parsing.yaml.objects import AnsibleMapping
    from collections import OrderedDict

    display = Display()
    # invalid specification
    input_value = 'foo,1.0,bar'
    try:
        result = RoleRequirement.role_yaml_parse(input_value)
    except:
        display.display('RoleRequirement.role_yaml_parse key error: %s' % input_value)
    # valid specification: scm, src, version
    display.display('RoleRequirement.role_yaml_parse: %s' % input_value)
    assert RoleRequirement.role_yaml_parse(input_value) == {'scm': 'foo', 'src': '1.0', 'name': 'bar'}
   

# Generated at 2022-06-13 09:06:05.340637
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo") == "repo"
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.tar.gz") == "repo"
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo,v1.0.0") == "repo"
    assert RoleRequirement.repo_url_to_role_name("repo") == "repo"
    assert RoleRequirement.repo_url_to

# Generated at 2022-06-13 09:06:19.920851
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    from ansible.utils.color import stringc

    role_yaml_parse = RoleRequirement.role_yaml_parse

    dots = u'\u25CC' * 4

    display.info(u'%s %s %s' % (dots, stringc(u'RoleRequirement.role_yaml_parse()', 'blue'), dots))
    display.display(u'Trying to parse "%s".' % stringc('foobar', 'cyan'))
    display.display(u'Expected: %s' % stringc(dict(src=u'foobar', name=u'foobar', scm=None, version=None), 'cyan'))
    display.display(u'Result: %s' % stringc(role_yaml_parse('foobar'), 'green'))


# Generated at 2022-06-13 09:06:24.736620
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    # Testing with string
    test_role = "test_role"
    test_role_result = RoleRequirement.role_yaml_parse(test_role)
    assert test_role_result['name'] == "test_role"
    assert test_role_result['scm'] == None
    assert test_role_result['src'] == "test_role"
    assert test_role_result['version'] == None

    test_role = "test_role,1.0.0"
    test_role_result = RoleRequirement.role_yaml_parse(test_role)
    assert test_role_result['name'] == "test_role"
    assert test_role_result['scm'] == None
    assert test_role_result['src'] == "test_role"
    assert test_role_result['version']

# Generated at 2022-06-13 09:06:43.234414
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name('git+git@github.com:geerlingguy/ansible-role-apache.git') == 'ansible-role-apache'
    assert RoleRequirement.repo_url_to_role_name('git://github.com/geerlingguy/ansible-role-apache.git') == 'ansible-role-apache'
    assert RoleRequirement.repo_url_to_role_name('git://github.com/geerlingguy/ansible-role-apache') == 'ansible-role-apache'
    assert RoleRequirement.repo_url_to_role_name('http://github.com/geerlingguy/ansible-role-apache') == 'ansible-role-apache'
    assert RoleRequirement.repo_url_to_

# Generated at 2022-06-13 09:06:48.912032
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    from ansible.module_utils.six import string_types


# Generated at 2022-06-13 09:06:56.669232
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    required_role = {'name': 'myrole', 'src': 'git+http://github.com/user/myrole.git', 'version': '1.0'}
    yaml_str = 'git+http://github.com/user/myrole.git,1.0,myrole'
    new_required_role = RoleRequirement.role_yaml_parse(yaml_str)
    assert new_required_role == required_role

    required_role = {'name': 'myrole', 'src': 'git+http://github.com/user/myrole.git', 'version': 'master'}
    yaml_str = 'myrole.tar.gz'
    new_required_role = RoleRequirement.role_yaml_parse(yaml_str)
    assert new_required_role == required_role



# Generated at 2022-06-13 09:07:07.265671
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    # Test for role_yaml_parse(role)
    role = RoleRequirement.role_yaml_parse('http://github.com/user/repo.git@master')
    assert {'name': 'repo', 'src': 'http://github.com/user/repo.git', 'scm': 'http', 'version': 'master'} == role
    role = RoleRequirement.role_yaml_parse('https://github.com/user/repo.git@master')
    assert {'name': 'repo', 'src': 'https://github.com/user/repo.git', 'scm': 'https', 'version': 'master'} == role
    role = RoleRequirement.role_yaml_parse('https://github.com/user/repo,v1.0.0')

# Generated at 2022-06-13 09:07:17.425079
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo,1.0.0.tar.gz') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo@1.0.0.tar.gz') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('github.com/user/repo') == 'repo'

# Generated at 2022-06-13 09:07:20.466628
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name("https://github.com/mrlesmithjr/ansible-etc-hosts.git") == "ansible-etc-hosts"


# Generated at 2022-06-13 09:07:31.583237
# Unit test for method repo_url_to_role_name of class RoleRequirement

# Generated at 2022-06-13 09:07:41.572060
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name(
            "http://git.example.com/repos/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name(
            "http://git.example.com/repos/repo.git,v1.0.0") == "repo"
    assert RoleRequirement.repo_url_to_role_name(
            "http://git.example.com/repos/repo.git,v1.0.0,first_name") == "repo"

# Generated at 2022-06-13 09:07:52.677691
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    # TODO: add more test cases for different formats of role spec
    role_spec = dict(name='test', scm='git', src='http://github.com/test/test.git', version='1.0.0')
    role_spec2 = dict()
    role_spec2['src'] = 'git+https://github.com/ansible/ansible-examples.git,v1.4.1'
    role_spec2['name'] = 'ansible-examples'
    role_spec2['version'] = 'v1.4.1'

    assert role_spec2 == RoleRequirement.role_yaml_parse(role_spec2)

    role_spec['role'] = 'test,1.0.0,my-test'

# Generated at 2022-06-13 09:08:00.635713
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    """
    RoleRequirement.role_yaml_parse method unit test
    """

    # Passes
    assert RoleRequirement.role_yaml_parse("http://git.example.com/repos/repo.git") == {'name': 'repo', 'scm': 'git', 'src': 'http://git.example.com/repos/repo.git', 'version': ''}
    assert RoleRequirement.role_yaml_parse("http://git.example.com/repos/repo.git,v1") == {'name': 'repo', 'scm': 'git', 'src': 'http://git.example.com/repos/repo.git', 'version': 'v1'}

# Generated at 2022-06-13 09:08:19.320781
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    test_func = RoleRequirement.repo_url_to_role_name
    assert test_func("https://github.com/geerlingguy/ansible-role-apache.git") == "geerlingguy.apache"
    assert test_func("https://github.com/geerlingguy/ansible-role-apache.git,") == "geerlingguy.apache"
    assert test_func("https://github.com/geerlingguy/ansible-role-apache.git,1.9.0") == "geerlingguy.apache"
    assert test_func("https://github.com/geerlingguy/ansible-role-apache.git,1.9.0,") == "geerlingguy.apache"

# Generated at 2022-06-13 09:08:26.585965
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    # test for string_types(old-style role line) case
    assert {'name': 'git-user', 'version': 'v0.2.0', 'src': 'git+https://github.com/randomuser/ansible-role-git-user', 'scm': 'git'} == RoleRequirement.role_yaml_parse('git+https://github.com/randomuser/ansible-role-git-user,v0.2.0')
    assert {'name': 'git-user', 'version': '', 'src': 'git+https://github.com/randomuser/ansible-role-git-user', 'scm': 'git'} == RoleRequirement.role_yaml_parse('git+https://github.com/randomuser/ansible-role-git-user')

# Generated at 2022-06-13 09:08:39.897083
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    rr = RoleRequirement()
    assert rr.repo_url_to_role_name("anything") == "anything"
    assert rr.repo_url_to_role_name("git@github.com:user/role.git") == "role"
    assert rr.repo_url_to_role_name("http://git.example.com/repos/repo.git") == "repo"
    assert rr.repo_url_to_role_name("http://git.example.com/repos/repo,ver.git") == "repo"
    assert rr.repo_url_to_role_name("http://git.example.com/repos/repo,ver.tar.gz") == "repo"
    assert rr.repo_url_to_role_

# Generated at 2022-06-13 09:08:50.901520
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    role = RoleRequirement()
    role_src = "https://github.com/jboss-fuse/fis-ansible-roles.git"

    # Test with 'role_name[,version[,name]]' pattern
    case1 = role.role_yaml_parse(role_src+',1.0,fuse-camel')
    assert case1.get('name') == 'fuse-camel'
    assert case1.get('src') == role_src
    assert case1.get('scm') == None
    assert case1.get('version') == '1.0'

    # Test with 'role_name[,version]' pattern
    case2 = role.role_yaml_parse(role_src+',2.0')

# Generated at 2022-06-13 09:09:03.038962
# Unit test for method repo_url_to_role_name of class RoleRequirement

# Generated at 2022-06-13 09:09:14.663330
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    # Test dict with out role
    role = {'src': 'https://github.com/jdauphant/ansible-role-nginx.git'}
    result = RoleRequirement.role_yaml_parse(role)
    assert result['name'] == 'ansible-role-nginx'
    assert result['src'] == 'https://github.com/jdauphant/ansible-role-nginx.git'
    assert result['scm'] == None
    assert result['version'] == ''

    # Test dict with role and version
    role = {'role': 'https://github.com/jdauphant/ansible-role-nginx.git,v1.0.0'}
    result = RoleRequirement.role_yaml_parse(role)

# Generated at 2022-06-13 09:09:18.613267
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():

    roleRequirement = RoleRequirement()
    assert roleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo.git') == 'repo'

# Generated at 2022-06-13 09:09:32.779310
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    # Test 1:
    # case 1: role: "repo,version,name"
    # return: {'src': 'repo', 'version': 'version', 'name': 'name'}
    result = RoleRequirement.role_yaml_parse("repo,version,name")
    assert result == {'src': 'repo', 'version': 'version', 'name': 'name'}

    # Test 2:
    # case 1: role: "repo,version"
    # return: {'src': 'repo', 'version': 'version', 'name': 'repo'}
    result = RoleRequirement.role_yaml_parse("repo,version")
    assert result == {'src': 'repo', 'version': 'version', 'name': 'repo'}

    # Test 3:
    # case

# Generated at 2022-06-13 09:09:41.336850
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name('https://github.com/username/ansible-role-foo') == 'ansible-role-foo'
    assert RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('git+ssh://git.example.com/repos/repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('git+ssh://git.example.com/repos/repo.tar.gz') == 'repo'

# Generated at 2022-06-13 09:09:52.901876
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    try:
        invalid_role = "role_name1,version1,name1,name2"
        role = RoleRequirement.role_yaml_parse(invalid_role)
        assert False, "AnsibleError not raised with invalid role: %s" % invalid_role
    except AnsibleError as e:
        pass

    try:
        invalid_role = "role_name1,version1,,name1"
        role = RoleRequirement.role_yaml_parse(invalid_role)
        assert False, "AnsibleError not raised with invalid role: %s" % invalid_role
    except AnsibleError as e:
        pass

    role = RoleRequirement.role_yaml_parse("role,version")

# Generated at 2022-06-13 09:10:11.290711
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name('https://github.com/') == 'github.com'
    assert RoleRequirement.repo_url_to_role_name('https://github.com/orgname/') == 'github.com'
    assert RoleRequirement.repo_url_to_role_name('https://github.com/orgname/repo') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('https://github.com/orgname/repo,') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('https://github.com/orgname/repo,') == 'repo'

# Generated at 2022-06-13 09:10:15.512048
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    role_name = RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo.git')
    assert role_name == 'repo'


# Generated at 2022-06-13 09:10:26.529594
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    """
    Tests for method role_yaml_parse.
    :return:
    """
    result_1 = RoleRequirement.role_yaml_parse('test,1.2.3,test_name')
    assert result_1['version'] == '1.2.3'
    result_2 = RoleRequirement.role_yaml_parse('test,test_name')
    assert result_2['name'] == 'test_name'
    result_3 = RoleRequirement.role_yaml_parse('test,v1.2.3,test_name')
    assert result_3['version'] == 'v1.2.3'
    result_4 = RoleRequirement.role_yaml_parse('test')
    assert result_4['version'] == ''
    result_5 = RoleRequirement.role_yaml_

# Generated at 2022-06-13 09:10:37.256544
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    result = RoleRequirement.role_yaml_parse('role_name')
    assert result == {'name': 'role_name', 'src': 'role_name', 'scm': None, 'version': None}

    result = RoleRequirement.role_yaml_parse('role_name,version')
    assert result == {'name': 'role_name', 'src': 'role_name', 'scm': None, 'version': 'version'}

    result = RoleRequirement.role_yaml_parse('role_name,version,name')
    assert result == {'name': 'name', 'src': 'role_name', 'scm': None, 'version': 'version'}

    result = RoleRequirement.role_yaml_parse('role_name,name,version')

# Generated at 2022-06-13 09:10:48.500957
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    from ansible.playbook.role.requirement import RoleRequirement


# Generated at 2022-06-13 09:10:57.488422
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    import pytest

    role_requirement = RoleRequirement()

    role_input = dict(role='my_role')
    role_expected = dict(role='my_role', name='my_role', src='my_role', scm=None, version='')
    assert role_requirement.role_yaml_parse(role_input) == role_expected

    role_input = dict(role='my_role,1.0')
    role_expected = dict(role='my_role,1.0', name='my_role', src='my_role,1.0', scm=None, version='1.0')
    assert role_requirement.role_yaml_parse(role_input) == role_expected

    role_input = dict(role='my_role,1.0,new_name')
    role_

# Generated at 2022-06-13 09:11:02.312750
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name('https://github.com/ansible/ansible-examples.git') == 'ansible-examples'
    assert RoleRequirement.repo_url_to_role_name('git@github.com:ansible/ansible-examples.git') == 'ansible-examples'


# Generated at 2022-06-13 09:11:14.553065
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    assert RoleRequirement.role_yaml_parse("git+http://git.example.com/repos/repo.git") == {'src': 'http://git.example.com/repos/repo.git', 'scm': 'git', 'version': '', 'name': 'repo'}
    assert RoleRequirement.role_yaml_parse("http://git.example.com/repos/repo.git") == {'src': 'http://git.example.com/repos/repo.git', 'scm': None, 'version': '', 'name': 'repo'}

# Generated at 2022-06-13 09:11:24.561094
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    from ansible.playbook.role.meta import RoleMeta

    meta = RoleMeta()
    meta.role_name = 'foo'
    meta.version = '1.1'
    role = {}
    role['role'] = 'bar'
    meta.dependencies.append(role)
    # New style: { src: 'galaxy.role,version,name', other_vars: "here" }
    role = {}
    role['src'] = 'test_role'
    meta.dependencies.append(role)
    role = {}
    role['src'] = 'test_role,1.0.0'
    meta.dependencies.append(role)
    role = {}
    role['src'] = 'test_role,1.0.0,test_name'
    meta.dependencies.append(role)
   

# Generated at 2022-06-13 09:11:34.762488
# Unit test for method repo_url_to_role_name of class RoleRequirement

# Generated at 2022-06-13 09:12:03.812508
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    # Test for old style role requirement (name only)
    role_line = 'role_name'
    role_spec = RoleRequirement.role_yaml_parse(role_line)
    assert role_spec['name'] == 'role_name'
    assert role_spec['src'] is None
    assert role_spec['scm'] is None
    assert role_spec['version'] is None

    # Test for new style role requirement (dict)
    role_spec = RoleRequirement.role_yaml_parse({'role': 'role_name', 'foobar': 'foobar'})
    assert role_spec['name'] == 'role_name'
    assert role_spec['src'] is None
    assert role_spec['scm'] is None
    assert role_spec['version'] is None

    # Test for new style role requirement (name

# Generated at 2022-06-13 09:12:10.204598
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    # Test whether an error is raised when no dictionary is given.
    try:
        RoleRequirement.role_yaml_parse("http://git.example.com/repos/repo.git")
    except AnsibleError as e:
        display.display("Error raised: %s" % e.message)
        assert False == False

    # Test whether an error is raised when an invalid role line was given.
    try:
        RoleRequirement.role_yaml_parse("http://git.example.com/repos/repo.git,master,name,invalid")
    except AnsibleError as e:
        display.display("Error raised: %s" % e.message)
        assert False == False

    # Test whether a valid role entry was parsed correctly.

# Generated at 2022-06-13 09:12:20.863228
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    import unittest

    class RoleRequirementTest(unittest.TestCase):

        def test_role_yaml_parse(self):
            z = RoleRequirement.role_yaml_parse('role_name,v1.2,name')
            self.assertEquals(z['name'], 'name')

            z = RoleRequirement.role_yaml_parse('name,v1.2,name')
            self.assertEquals(z['name'], 'name')

            z = RoleRequirement.role_yaml_parse('name,v1.2')
            self.assertEquals(z['name'], 'name')

            z = RoleRequirement.role_yaml_parse('name')
            self.assertEquals(z['name'], 'name')

            z = RoleRequirement.role_yaml

# Generated at 2022-06-13 09:12:31.484508
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    def test_yaml_parse(role, expected_role):
        result_role = RoleRequirement.role_yaml_parse(role)
        msg = "yaml parse: %s" % role
        assert expected_role == result_role, msg

    # src, version, name as string
    test_yaml_parse(
        "https://github.com/example/repo.git,v1.0.0",
        dict(name="repo", src="https://github.com/example/repo.git", scm="git", version="v1.0.0")
    )
    # src, version, name as dict