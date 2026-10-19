

# Generated at 2022-06-13 09:03:02.198498
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    result = RoleRequirement.role_yaml_parse('src')
    assert 'name' in result
    assert result['name'] == 'src'
    assert 'src' in result
    assert result['src'] == 'src'

    result = RoleRequirement.role_yaml_parse('src,1.0')
    assert result['name'] == 'src'
    assert result['src'] == 'src'
    assert result['version'] == '1.0'

    result = RoleRequirement.role_yaml_parse('src,1.0,test')
    assert result['name'] == 'test'
    assert result['src'] == 'src'
    assert result['version'] == '1.0'

    result = RoleRequirement.role_yaml_parse('src,1.0,test,invalid')

# Generated at 2022-06-13 09:03:12.767051
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    role_requirement = RoleRequirement()
    # string_types
    #name = 'haolei'
    #scm = 'git'
    #src = 'git@github.com:haolei/ansible-role-tensorflow-tensorboard.git'
    #version = 'HEAD'
    #print(role_requirement.role_yaml_parse((name,scm,src,version)))
    ##dict_types
    #role_dict = {'name': 'haolei', 'scm': 'git', 'src': 'git@github.com:haolei/ansible-role-tensorflow-tensorboard.git', 'version': 'HEAD'}
    #print(role_requirement.role_yaml_parse(role_dict))
    #scm_archive_role_dict = {

# Generated at 2022-06-13 09:03:21.996564
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    assert RoleRequirement.role_yaml_parse("geerlingguy.gitlab") == {'name': 'geerlingguy.gitlab', 'scm': None, 'src': 'geerlingguy.gitlab', 'version': ''}
    assert RoleRequirement.role_yaml_parse("geerlingguy.gitlab,1.0.0") == {'name': 'geerlingguy.gitlab', 'scm': None, 'src': 'geerlingguy.gitlab', 'version': '1.0.0'}

# Generated at 2022-06-13 09:03:31.634065
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    from ansible.utils.role_lookup import RoleLookup
    assert RoleRequirement.repo_url_to_role_name("git+git@github.com:jboss-ansible-roles/my_role.git") == "jboss-ansible-roles.my_role"
    assert RoleRequirement.repo_url_to_role_name("git+https://github.com/jboss-ansible-roles/my_role.git") == "jboss-ansible-roles.my_role"
    assert RoleRequirement.repo_url_to_role_name("git+http://github.com/jboss-ansible-roles/my_role.git") == "jboss-ansible-roles.my_role"
    assert RoleRequirement.repo_url_to_role_

# Generated at 2022-06-13 09:03:42.931622
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    
    ansibleRole = RoleRequirement()
    # Test Old Style Entry
    RoleRequirement_role_yaml_parse_test1_input1_str = "git+git://git.example.com/repos/test.git"
    RoleRequirement_role_yaml_parse_test1_input2_str = ""
    RoleRequirement_role_yaml_parse_test1_exp_output = dict(name="test", src="git://git.example.com/repos/test.git", scm="git", version="")
    RoleRequirement_role_yaml_parse_test1_output = ansibleRole.role_yaml_parse(RoleRequirement_role_yaml_parse_test1_input1_str)
    assert RoleRequirement_role_yaml_parse_test1_output == RoleRequ

# Generated at 2022-06-13 09:03:49.473937
# Unit test for method role_yaml_parse of class RoleRequirement

# Generated at 2022-06-13 09:03:58.212392
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name("separated.git") == 'separated'
    assert RoleRequirement.repo_url_to_role_name("nested,comma,separated") == 'nested'
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.git") == 'repo'
    assert RoleRequirement.repo_url_to_role_name("git@git.example.com:repos/repo.git") == 'repo'
    assert RoleRequirement.repo_url_to_role_name("git://git.example.com/repo.git") == 'repo'

# Generated at 2022-06-13 09:04:03.144035
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    assert 'NameAnsible.stl-network' == RoleRequirement.role_yaml_parse('git+https://github.com/STL-Zabbix/ansible-role-stl-network.git')['name']

# Generated at 2022-06-13 09:04:05.999802
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name('https://github.com/galaxy/ansible-role-foo.git') == 'ansible-role-foo'

# Generated at 2022-06-13 09:04:15.033937
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    url = "https://github.com/ansible/ansible-examples.git"
    assert "ansible-examples" == RoleRequirement.repo_url_to_role_name(url)

    url = "https://github.com/ansible/ansible-examples.git,"
    assert "ansible-examples" == RoleRequirement.repo_url_to_role_name(url)

    url = "https://github.com/ansible/ansible-examples.git, "
    assert "ansible-examples" == RoleRequirement.repo_url_to_role_name(url)

    url = "https://github.com/ansible/ansible-examples.git,master"
    assert "ansible-examples" == RoleRequirement.repo_url_to_role_name

# Generated at 2022-06-13 09:04:28.147506
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    role = RoleRequirement()

    assert role.role_yaml_parse("geerlingguy.apache") == {
        "name": "geerlingguy.apache",
        "src": "https://galaxy.ansible.com/geerlingguy/apache",
        "scm": None,
        "version": "",
    }

    assert role.role_yaml_parse("https://github.com/geerlingguy/ansible-role-apache.git") == {
        "name": "ansible-role-apache",
        "src": "https://github.com/geerlingguy/ansible-role-apache.git",
        "scm": None,
        "version": "",
    }


# Generated at 2022-06-13 09:04:38.730004
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    import os

    for _ in [
        'git+https://github.com/davidk/ansible-role-vim.git,v1.1',
        'davidk.vim,v1.1',
        'https://github.com/davidk/ansible-role-vim.git,v1.1',
        'https://github.com/davidk/ansible-role-vim.git,v1.1,davidk.vim',
        'git+https://github.com/davidk/ansible-role-vim.git,v1.1,davidk.vim',
        'davidk.vim'
    ]:
        role = RoleRequirement.role_yaml_parse(_)
        assert role
        assert role['name']
        assert role['src']

# Generated at 2022-06-13 09:04:49.573559
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    rr = RoleRequirement()
    assert rr.repo_url_to_role_name('repo_name') == 'repo_name'
    assert rr.repo_url_to_role_name('https://git.example.com/repos/repo.git') == 'repo'
    assert rr.repo_url_to_role_name('git://git@git.example.com/repos/repo.git') == 'repo'
    assert rr.repo_url_to_role_name('http://git.example.com/repos/repo,v1.1') == 'repo'

# Generated at 2022-06-13 09:04:57.038387
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert 'repo' == RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo.git')
    assert 'repo-tar.gz' == RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo-tar.gz')
    assert 'repo-tar.gz' == RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo-tar.gz.tar.gz')
    assert 'repo-tar.gz' == RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo-tar.gz.git')
    assert 'repo-tar.gz' == RoleRequirement.repo_url

# Generated at 2022-06-13 09:05:06.430249
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.git#ref") == "repo"
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.git,branch") == "repo"
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.git#ref,branch") == "repo"

# Generated at 2022-06-13 09:05:18.591858
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():

    role_requirement = RoleRequirement() 

    # Test url that end with .git
    url = "https://github.com/ansible/role-couchdb.git"
    assert role_requirement.repo_url_to_role_name(url) == "role-couchdb"
    url = "git@github.com:ansible/role-couchdb.git"
    assert role_requirement.repo_url_to_role_name(url) == "role-couchdb"

    # Test url that end with .tar.gz
    url = "https://github.com/ansible/role-couchdb/archive/master.tar.gz"
    assert role_requirement.repo_url_to_role_name(url) == "role-couchdb"

# Generated at 2022-06-13 09:05:28.073384
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    import unittest2 as unittest


# Generated at 2022-06-13 09:05:34.592145
# Unit test for method repo_url_to_role_name of class RoleRequirement

# Generated at 2022-06-13 09:05:47.251918
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com:8080/repos/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("user@git.example.com/repos/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("git@git.example.com/repos/repo.git") == "repo"
   

# Generated at 2022-06-13 09:06:00.723071
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    rr = RoleRequirement()
    assert rr.role_yaml_parse({}) == {}
    assert rr.role_yaml_parse({'role': 'test'}) == {'name': 'test'}
    assert rr.role_yaml_parse({'role': 'test', 'version': '1.0.0'}) == {'name': 'test', 'version': '1.0.0'}

    assert rr.role_yaml_parse('test') == {'name': 'test', 'scm': None, 'src': None, 'version': None}
    assert rr.role_yaml_parse('test,1.0.0') == {'name': 'test', 'scm': None, 'src': None, 'version': '1.0.0'}
    assert rr.role

# Generated at 2022-06-13 09:06:20.887003
# Unit test for method repo_url_to_role_name of class RoleRequirement

# Generated at 2022-06-13 09:06:33.401575
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name("git://git.example.com/repos/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("git://github.com/user/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("git://github.com/user/repo.git?somearg") == "repo"
    assert RoleRequirement.repo_url_to_role_name("git@github.com:user/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("git@github.com:user/repo.git?some-arg") == "repo"
    assert RoleRequirement.re

# Generated at 2022-06-13 09:06:43.057805
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    print ('\nTesting repo_url_to_role_name...')

    #test RoleRequirement.repo_url_to_role_name
    role_name = RoleRequirement.repo_url_to_role_name("git+https://github.com/ansible/ansible-example-role-nginx.git")
    assert role_name == 'ansible-example-role-nginx'

    role_name = RoleRequirement.repo_url_to_role_name("https://github.com/ansible/ansible-example-role-nginx.git")
    assert role_name == 'ansible-example-role-nginx'

    role_name = RoleRequirement.repo_url_to_role_name("git+http://git.example.com/repos/repo.git")

# Generated at 2022-06-13 09:06:53.468519
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    assert RoleRequirement.role_yaml_parse('foo') == {'name': 'foo', 'src': 'foo', 'version': '', 'scm': None}
    assert RoleRequirement.role_yaml_parse('foo,v2') == {'name': 'foo', 'src': 'foo', 'version': 'v2', 'scm': None}
    assert RoleRequirement.role_yaml_parse('foo,v2,bar') == {'name': 'bar', 'src': 'foo', 'version': 'v2', 'scm': None}
    assert RoleRequirement.role_yaml_parse({'role': 'foo'}) == {'name': 'foo', 'src': 'foo', 'version': '', 'scm': None}
    assert RoleRequirement.role_yaml_par

# Generated at 2022-06-13 09:07:05.003371
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    # Tests if the method properly extracts the role name from the given repository URL
    # Repository URL: http://git.example.com/repos/repo.git
    # Role Name: repo
    role_name = RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.git")
    assert role_name == "repo", "The extracted role name is not equal to the expected one (repo)"

    # Tests, if the method properly extracts the role name from another given repository URL
    # Repository URL: git@github.com:user/role.git
    # Role Name: role
    role_name = RoleRequirement.repo_url_to_role_name("git@github.com:user/role.git")

# Generated at 2022-06-13 09:07:12.726073
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    # test the normal case
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.git") == "repo"

    # test the case of the trailing ".git" should be stripped
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.git") == "repo"

    # test the case of the trailing ".tar.gz" should be stripped
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.tar.gz") == "repo"

    # test the case of the trailing .tar.gz and ",version" should be stripped

# Generated at 2022-06-13 09:07:20.354657
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    # testing http://git.example.com/repos/repo.git
    repo_url = "http://git.example.com/repos/repo.git"
    expected_return_value = "repo"
    actual_return_value = RoleRequirement.repo_url_to_role_name(repo_url)
    assert actual_return_value == expected_return_value, "got %s" % actual_return_value

    # testing git+http://git.example.com/repos/repo.git
    repo_url = "git+http://git.example.com/repos/repo.git"
    expected_return_value = "repo"
    actual_return_value = RoleRequirement.repo_url_to_role_name(repo_url)
    assert actual_return

# Generated at 2022-06-13 09:07:31.473727
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    # Test repo_url_to_role_name() of class RoleRequirement
    # with good input
    assert RoleRequirement.repo_url_to_role_name('http://github.com/user/repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('https://github.com/user/repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('git@github.com:user/repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('git@github.com/user/repo.git') == 'repo'
    # with bad input: no valid URL

# Generated at 2022-06-13 09:07:41.495262
# Unit test for method role_yaml_parse of class RoleRequirement

# Generated at 2022-06-13 09:07:52.591316
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    # Given
    role_requirement = RoleRequirement()

    # When
    result_01 = role_requirement.role_yaml_parse('nginx')
    result_02 = role_requirement.role_yaml_parse('jdauphant.nginx')
    result_03 = role_requirement.role_yaml_parse('jdauphant.nginx,v1.0.0')
    result_04 = role_requirement.role_yaml_parse('jdauphant.nginx,v1.0.0,role_01')
    result_05 = role_requirement.role_yaml_parse('nginx,v1.0.0,role_01')

    # Then

# Generated at 2022-06-13 09:08:12.145694
# Unit test for method role_yaml_parse of class RoleRequirement

# Generated at 2022-06-13 09:08:26.520063
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    assert RoleRequirement.role_yaml_parse("galaxy.role") == {'name': 'galaxy.role', 'scm': None, 'src': 'galaxy.role', 'version': None}
    assert RoleRequirement.role_yaml_parse("galaxy.role,v1") == {'name': 'galaxy.role', 'scm': None, 'src': 'galaxy.role', 'version': 'v1'}
    assert RoleRequirement.role_yaml_parse("https://github.com/galaxy.role,v1,my.galaxy.role") == {'name': 'my.galaxy.role', 'scm': None, 'src': 'https://github.com/galaxy.role', 'version': 'v1'}

# Generated at 2022-06-13 09:08:39.782390
# Unit test for method role_yaml_parse of class RoleRequirement

# Generated at 2022-06-13 09:08:50.822486
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    # case 1

    tasks = """
    - name: test1
      hosts: localhost
      roles:
          - role: ansible-role-repo1,v1.0.0,repo1
    """

    role = RoleRequirement.role_yaml_parse(tasks)
    assert role == {'name': 'repo1', 'scm': None, 'src': 'ansible-role-repo1', 'version': 'v1.0.0'}

    # case 2

    tasks = """
    - name: test2
      hosts: localhost
      roles:
          - {role: ansible-role-repo2, version: v1.0.0, name: repo2}
    """

    role = RoleRequirement.role_yaml_parse(tasks)

# Generated at 2022-06-13 09:08:55.230426
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    """RoleRequirement.role_yaml_parse() unit test"""

    from __main__ import display

    # test role with old style "src=some_url"
    old_style = dict(src='http://some_url.tar.gz')
    r = RoleRequirement.role_yaml_parse(old_style)
    assert r['src'] == 'http://some_url.tar.gz', "Old style role %s is not parsed correctly. src=%s" % (old_style, r['src'])
    assert r['scm'] == None, "Old style role %s is not parsed correctly. scm=%s" % (old_style, r['scm'])

# Generated at 2022-06-13 09:09:06.248512
# Unit test for method role_yaml_parse of class RoleRequirement

# Generated at 2022-06-13 09:09:17.540409
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.git")=='repo'
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.git,0.1")=='repo'
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.git,0.1,myrepo")=='myrepo'
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.git,0.1,myrepo,0.2")=='myrepo'

# Generated at 2022-06-13 09:09:30.535277
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    
    # Example data of Galaxy for test specifically
    #https://github.com/jtyr/ansible-mysql.git
    #https://github.com/jtyr/ansible-mysql/archive/1.0.tar.gz
    #https://github.com/jtyr/ansible-mysql/archive/1.0.zip

    # Test typical case
    assert RoleRequirement.repo_url_to_role_name("https://github.com/jtyr/ansible-mysql.git")=="ansible-mysql"
    assert RoleRequirement.repo_url_to_role_name("https://github.com/jtyr/ansible-mysql/archive/1.0.tar.gz")=="ansible-mysql"
    assert RoleRequirement.repo_url_

# Generated at 2022-06-13 09:09:40.043681
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    role = "geerlingguy.java,1.8.0"
    assert RoleRequirement.role_yaml_parse(role) == {'name': 'geerlingguy.java', 'src': 'geerlingguy.java', 'scm': None, 'version': '1.8.0'}
    role = "geerlingguy.java,1.8.0,some_custom_name"
    assert RoleRequirement.role_yaml_parse(role) == {'name': 'some_custom_name', 'src': 'geerlingguy.java', 'scm': None, 'version': '1.8.0'}
    role = "geerlingguy.java"

# Generated at 2022-06-13 09:09:51.759874
# Unit test for method role_yaml_parse of class RoleRequirement

# Generated at 2022-06-13 09:10:37.898269
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    display.display("--- test_RoleRequirement_role_yaml_parse ---")

    # ---------------------------
    display.display("Test with an invalid role line")

    try:
        role = 'geerlingguy.apache-php,1.0.0,var=val'
        RoleRequirement.role_yaml_parse(role)
        assert False
    except AnsibleError:
        display.display("-> OK")

    # ---------------------------
    display.display("Test with a valid role line")

    role      = 'geerlingguy.apache-php,1.0.0,php'
    result    = { 'name': 'php',
                  'role': 'geerlingguy.apache-php',
                  'src': 'geerlingguy.apache-php',
                  'version': '1.0.0' }

# Generated at 2022-06-13 09:10:49.073500
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    print("\nWARN: test suite for class RoleRequirement not implemented yet, only class docstring tested\n")

    assert isinstance(RoleRequirement(), RoleRequirement)


# Generated at 2022-06-13 09:11:00.426878
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    repo_url_to_role_name_testcases = []
    repo_url_to_role_name_testcases.append(('https://github.com/geerlingguy/ansible-role-security.git', None, 'ansible-role-security'))
    repo_url_to_role_name_testcases.append(('https://github.com/geerlingguy/ansible-role-security', None, 'ansible-role-security'))
    repo_url_to_role_name_testcases.append(('https://github.com/geerlingguy/ansible-role-security.git,3.0.0', None, 'ansible-role-security'))

# Generated at 2022-06-13 09:11:06.580886
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    # Given a github HTTPS URL "https://github.com/mvisonneau/ansible-role-test-1.git"
    url = "https://github.com/mvisonneau/ansible-role-test-1.git"
    # When calling to the method with this URL
    result = RoleRequirement.repo_url_to_role_name(url)
    # Then it should match the role name
    assert "ansible-role-test-1" == result

    # Given a github SSH URL "git+ssh://git@github.com/mvisonneau/ansible-role-test-1.git"
    url = "git+ssh://git@github.com/mvisonneau/ansible-role-test-1.git"
    # When calling to the method with this URL

# Generated at 2022-06-13 09:11:16.091878
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    # Simple role testing
    role_src = dict(name='test', version='1.0', src='http://github.com/galaxy/role.git', scm=None)
    role_src_string = 'http://github.com/galaxy/role.git,1.0'
    assert(RoleRequirement.role_yaml_parse(role_src) == RoleRequirement.role_yaml_parse(role_src_string))

    # Role with name
    role_src = dict(name='test-name', version='1.0', src='http://github.com/galaxy/role.git', scm=None)
    role_src_string = 'http://github.com/galaxy/role.git,1.0,test-name'

# Generated at 2022-06-13 09:11:24.852584
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    from ansible.module_utils.six import PY3

    # Old style role definition without name
    role = 'galaxy.role,version'
    val = RoleRequirement.role_yaml_parse(role)
    assert val['name'] == 'galaxy.role'
    assert val['version'] == 'version'
    assert val['src'] == 'galaxy.role'
    assert val['scm'] == None

    # Old style role definition with name
    role = 'galaxy.role,version,name'
    val = RoleRequirement.role_yaml_parse(role)
    assert val['name'] == 'name'
    assert val['version'] == 'version'
    assert val['src'] == 'galaxy.role'
    assert val['scm'] == None

    # New style role definition with src and version but

# Generated at 2022-06-13 09:11:34.982007
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    from ansible.errors import AnsibleError
    from ansible.utils.display import Display
    display = Display()


# Generated at 2022-06-13 09:11:44.442808
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    assert RoleRequirement.role_yaml_parse('role_name,v0.0.1,blah') == dict(name='role_name', scm=None, src='blah', version='v0.0.1')
    assert RoleRequirement.role_yaml_parse('role_name,v0.0.1') == dict(name='role_name', scm=None, src='role_name', version='v0.0.1')
    assert RoleRequirement.role_yaml_parse('role_name,blah') == dict(name='role_name', scm=None, src='blah', version='')
    assert RoleRequirement.role_yaml_parse('role_name') == dict(name='role_name', scm=None, src='role_name', version='')

# Unit

# Generated at 2022-06-13 09:11:58.033902
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():

    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo") == "repo"
    assert RoleRequirement.repo_url_to_role_name("git+ssh://git@github.com/ansible/ansible-examples.git") == "ansible-examples"
    assert RoleRequirement.repo_url_to_role_name("git@example.com:user/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("user/repo") == "repo"
    assert RoleRequirement.repo_url_to

# Generated at 2022-06-13 09:12:01.649663
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    url = "https://github.com/ansible/ansible-modules-extra.git"
    assert RoleRequirement.repo_url_to_role_name(url) == 'ansible-modules-extra'

# Generated at 2022-06-13 09:12:47.230791
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    result = RoleRequirement.role_yaml_parse('/path/to/repo.git')
    assert result == dict(name='repo', src='/path/to/repo.git', scm=None, version=None)
    result = RoleRequirement.role_yaml_parse('https://github.com/user/ansible-role-repo')
    assert result == dict(name='ansible-role-repo', src='https://github.com/user/ansible-role-repo', scm=None, version=None)
    result = RoleRequirement.role_yaml_parse('https://github.com/user/ansible-role-repo.git')