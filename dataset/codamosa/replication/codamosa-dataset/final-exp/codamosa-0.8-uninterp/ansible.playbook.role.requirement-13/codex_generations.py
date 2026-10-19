

# Generated at 2022-06-13 09:03:02.425786
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    role_name = "geerlingguy.composer"
    role_spec = RoleRequirement.role_yaml_parse(role_name)

    assert "name" in role_spec.keys()
    assert "src" in role_spec.keys()
    assert "scm" in role_spec.keys()
    assert "version" in role_spec.keys()

    assert role_spec["name"] == role_name
    assert role_spec["src"] == role_name
    assert role_spec["scm"] == None
    assert role_spec["version"] == ''

    role_name = "geerlingguy.composer,0.3.0"
    role_spec = RoleRequirement.role_yaml_parse(role_name)

    assert "name" in role_spec.keys()

# Generated at 2022-06-13 09:03:13.009606
# Unit test for method role_yaml_parse of class RoleRequirement

# Generated at 2022-06-13 09:03:22.131984
# Unit test for method role_yaml_parse of class RoleRequirement

# Generated at 2022-06-13 09:03:31.744725
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    assert RoleRequirement().role_yaml_parse('geerlingguy.apache') == dict(name='apache', scm=None, src='geerlingguy.apache', version='')
    assert RoleRequirement().role_yaml_parse('geerlingguy.apache,v1.0') == dict(name='apache', scm=None, src='geerlingguy.apache', version='v1.0')
    assert RoleRequirement().role_yaml_parse('geerlingguy.apache,v1.0,') == dict(name='', scm=None, src='geerlingguy.apache', version='v1.0')

# Generated at 2022-06-13 09:03:37.195251
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    role_name = 'ansible-role-simple-role'
    repo_url = 'git+https://github.com/michaelrigart/'+role_name+'.git,v1.0.0,michaelrigart.'+role_name
    assert RoleRequirement.repo_url_to_role_name(repo_url) == role_name

# Generated at 2022-06-13 09:03:48.700618
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert (RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo.git') == 'repo')
    assert (RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo,1.0.1.tar.gz') == 'repo')
    assert (RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo.tar.gz') == 'repo')
    assert (RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo,1.0.1.tar.gz,role_name') == 'repo')

# Generated at 2022-06-13 09:03:57.556301
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert "repo" == RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.git")
    assert "repo" == RoleRequirement.repo_url_to_role_name("https://github.com/user/repo.git")
    assert "user/repo" == RoleRequirement.repo_url_to_role_name("git@github.com:user/repo.git")
    assert "repo" == RoleRequirement.repo_url_to_role_name("git@github.com:user/repo,1.0.1")
    assert "repo" == RoleRequirement.repo_url_to_role_name("git@github.com:user/repo,1.0.1,specific_name")

# Generated at 2022-06-13 09:04:10.733477
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    """
    RoleRequirement: role_yaml_parse method unit test stub
    """

    url = "git+https://github.com/ehelms/ansible-role-nfs.git,v1.0.0,nfs"
    role = RoleRequirement.role_yaml_parse(url)
    assert role["name"] == "nfs"
    assert role["scm"] == "git"
    assert role["src"] == "https://github.com/ehelms/ansible-role-nfs.git"
    assert role["version"] == "v1.0.0"

    assert RoleRequirement.repo_url_to_role_name("git+https://github.com/ehelms/ansible-role-nfs.git,v1.0.0,nfs") == "nfs"

# Generated at 2022-06-13 09:04:15.541338
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name("https://github.com/username/myrole.git") == 'myrole'
    assert RoleRequirement.repo_url_to_role_name("/home/myusername/myrepo") == 'myrepo'
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.git") == 'repo'

# Generated at 2022-06-13 09:04:20.798236
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    # string_types = basestring
    role_1 = 'git+https://github.com/Yelp/ansible-role-requirements.git,v1'
    role_2 = 'git+https://github.com/Yelp/ansible-role-requirements.git,v1,requirement'
    role_3 = 'https://github.com/Yelp/ansible-role-requirements.git,v1'
    role_4 = 'https://github.com/Yelp/ansible-role-requirements.git,v1,requirement'

    role_5 = 'git+https://github.com/Yelp/ansible-role-requirements.git'
    role_6 = 'https://github.com/Yelp/ansible-role-requirements.git'
    #role

# Generated at 2022-06-13 09:04:48.080456
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    # TODO
    assert False

# Generated at 2022-06-13 09:05:01.102920
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    # Test invalid format
    try:
        RoleRequirement.role_yaml_parse('hoge,fuga,foo,bar')
    except AnsibleError as e:
        assert e.message == "Invalid role line (hoge,fuga,foo,bar). Proper format is 'role_name[,version[,name]]'"
    else:
        assert False

    # Test invalid format
    try:
        RoleRequirement.role_yaml_parse('hoge,fuga,foo,')
    except AnsibleError as e:
        assert e.message == "Invalid role line (hoge,fuga,foo,). Proper format is 'role_name[,version[,name]]'"
    else:
        assert False

    # Test invalid format

# Generated at 2022-06-13 09:05:14.472821
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    # Testing with a string input
    role_complete = 'git+https://github.com/apolloclark/ansible-role-nginx,v1.0.0,nginx'
    role_parse = dict(name='nginx', scm='git', src='https://github.com/apolloclark/ansible-role-nginx', version='v1.0.0')
    assert (RoleRequirement.role_yaml_parse(role_complete) == role_parse)

    role_noversion = 'git+https://github.com/apolloclark/ansible-role-nginx,nginx'
    role_parse = dict(name='nginx', scm='git', src='https://github.com/apolloclark/ansible-role-nginx', version='')

# Generated at 2022-06-13 09:05:22.580742
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    from ansible.module_utils._text import to_text

    t_dict = lambda l: dict((to_text(k), to_text(v)) for k, v in l)
    print("")
    print("# Testing RoleRequirement.role_yaml_parse")
    print("")

    print("## Only role name")
    errors = []
    role_name = './tests/data/ansible-role-test/meta/main.yml'
    result = RoleRequirement.role_yaml_parse(role_name)
    expect = t_dict([
        ('name', 'test'),
        ('src', './tests/data/ansible-role-test'),
        ('scm', 'git'),
        ('version', ''),
    ])

# Generated at 2022-06-13 09:05:31.052223
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    r = RoleRequirement()

    assert r.role_yaml_parse('geerlingguy.java,1.7.0') == dict(name='geerlingguy.java', src='geerlingguy.java', version='1.7.0')
    assert r.role_yaml_parse('http://git.example.com/repos/myrepo.git') == dict(name='myrepo', src='http://git.example.com/repos/myrepo.git', scm=None, version=None)

# Generated at 2022-06-13 09:05:43.080724
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    str_role_1 = 'example.com,1.2,role_name'
    str_role_2 = 'example.com'
    str_role_3 = 'git+git@example.com,1.2'
    str_role_4 = 'git+git@example.com'
    str_role_5 = 'git+git://example.com'
    str_role_6 = 'git+https://example.com'
    str_role_7 = 'git+https://example.com,1.2,'
    str_role_8 = 'git+https://example.com,1.2,role_name'
    str_role_9 = 'git+https://example.com,role_name'


# Generated at 2022-06-13 09:05:52.567201
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    r = RoleRequirement()
    assert r.role_yaml_parse('https://github.com/geerlingguy/ansible-role-apache,v1.0,geerlingguy.apache') == {'name': 'geerlingguy.apache',
                                                                                                              'src': 'https://github.com/geerlingguy/ansible-role-apache',
                                                                                                              'scm': None,
                                                                                                              'version': 'v1.0'}


# Generated at 2022-06-13 09:06:05.397857
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    print("Name %s" % RoleRequirement.repo_url_to_role_name("git+https://github.com/test.git"))
    assert(RoleRequirement.repo_url_to_role_name("https://github.com/test.git") == "test")
    assert(RoleRequirement.repo_url_to_role_name("http://github.com/test.git") == "test")
    assert(RoleRequirement.repo_url_to_role_name("git+ssh://github.com/test.git") == "test")
    assert(RoleRequirement.repo_url_to_role_name("git+ssh://github.com/test-test.git") == "test-test")

# Generated at 2022-06-13 09:06:19.920154
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    # Tests that a valid input string is correctly parsed
    test_string = RoleRequirement.role_yaml_parse('geerlingguy.composer,1.0.0')
    assert test_string['name'] == 'geerlingguy.composer'
    assert test_string['version'] == '1.0.0'
    assert test_string['src'] == 'geerlingguy.composer'
    assert test_string['scm'] == None
    # Tests that a valid input dictionary is correctly parsed
    test_dict = RoleRequirement.role_yaml_parse({'geerlingguy.composer': '1.0.0'})
    assert test_dict['name'] == 'geerlingguy.composer'
    assert test_dict['version'] == '1.0.0'

# Generated at 2022-06-13 09:06:27.851198
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo") == "repo"
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo,v0.1.0") == "repo"
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo,v0.1.0,renamed") == "repo"
    assert RoleRequirement.repo_url_to_role_name("repo") == "repo"

# Generated at 2022-06-13 09:06:40.911177
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    role_requirement = RoleRequirement()
    results = role_requirement.role_yaml_parse('galaxy.role,1')
    expected_dict = { 'src': 'galaxy.role', 'scm': None, 'version': '1', 'name': 'galaxy.role'}
    assert results == expected_dict

# Generated at 2022-06-13 09:06:50.374144
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    """
    Note: is not a real test, but illustrates the use of method test_RoleRequirement_role_yaml_parse
    :return: Dictionary with role data
    """
    role = 'https://github.com/mjhea0/ansible-lamp'
    result = RoleRequirement.role_yaml_parse(role)
    print(result)
    assert result['name'] == 'ansible-lamp'
    assert result['scm'] == 'git'
    assert result['src'] == 'https://github.com/mjhea0/ansible-lamp'
    assert result['version'] == ''
    return result



# Generated at 2022-06-13 09:07:01.447574
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    # Test 1: input a repo url without version and return the role name
    status = 1
    role_name = "role_repo"
    url = "http://git.example.com/repos/role_repo.git"
    if RoleRequirement.repo_url_to_role_name(url) == role_name:
        status = 0
    assert not status

    # Test 2: input a repo url with version and return the role name
    status = 1
    role_name = "role_repo"
    url = "http://git.example.com/repos/role_repo.git,v1.0.0"
    if RoleRequirement.repo_url_to_role_name(url) == role_name:
        status = 0
    assert not status

    # Test 3: input a repo

# Generated at 2022-06-13 09:07:06.063673
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    import unittest

    class TestRoleRequirementRoleYamlParse(unittest.TestCase):
        """ Test class for RoleRequirement.role_yaml_parse """

        def test_version_with_name(self):
            """ Test that version and name are correctly parsed from the role string
            """

            test_role = 'git+https://github.com/everpeace/ansible-role-mecab.git,v1.0.1,myrole'
            result = RoleRequirement.role_yaml_parse(test_role)

# Generated at 2022-06-13 09:07:16.447856
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    # Parse a string
    role_yaml = 'https://github.com/some_user/some_repository.git'
    rr = RoleRequirement.role_yaml_parse(role_yaml)
    assert rr['name'] == 'some_repository'
    assert rr['scm'] == 'git'
    assert rr['src'] == 'https://github.com/some_user/some_repository.git'
    assert rr['version'] == ''

    # Parse a string with a version
    role_yaml = 'https://github.com/some_user/some_repository.git,v2.0'
    rr = RoleRequirement.role_yaml_parse(role_yaml)
    assert rr['name'] == 'some_repository'


# Generated at 2022-06-13 09:07:27.649168
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    # Test the old style
    role = 'git+https://github.com/ansible/awx.git,develop,awx'
    parsed = RoleRequirement.role_yaml_parse(role)
    expected_result = {'name': 'awx', 'src': 'https://github.com/ansible/awx.git', 'scm': 'git', 'version': 'develop'}
    assert parsed == expected_result

    # Test the new style
    role = {'role': 'awx,develop'}
    parsed = RoleRequirement.role_yaml_parse(role)
    expected_result = {'name': 'awx', 'src': None, 'scm': None, 'version': 'develop'}
    assert parsed == expected_result


# Generated at 2022-06-13 09:07:37.776643
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    assert RoleRequirement.role_yaml_parse("http://www.github.com/username/repo.git") == {'version': None, 'name': 'repo', 'src': 'http://www.github.com/username/repo.git', 'scm': None}
    assert RoleRequirement.role_yaml_parse("git+http://www.github.com/username/repo.git") == {'version': None, 'name': 'repo', 'src': 'http://www.github.com/username/repo.git', 'scm': 'git'}

# Generated at 2022-06-13 09:07:48.414783
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    from collections import OrderedDict

    print("\n# Testing role_yaml_parse of class RoleRequirement")

    role_tests = OrderedDict()

    role_tests[
        {'role': 'geerlingguy.java',
         'ansible_galaxy.info': 'role_galaxy_info',
         'ansible_galaxy.meta': 'role_galaxy_meta'},
        {'name': 'geerlingguy.java', 'src': 'geerlingguy.java', 'scm': 'git', 'version': ''}
    ]


# Generated at 2022-06-13 09:07:57.822981
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    role_requirement = RoleRequirement()

# Generated at 2022-06-13 09:08:09.547333
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name("ssh://git@g.example.com/repos/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("ssh://git@g.example.com/repos/repo.git,1.0.0") == "repo"
    assert RoleRequirement.repo_url_to_role_name("git@g.example.com/repos/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("git@g.example.com/repos/repo.git,1.0.0") == "repo"

# Generated at 2022-06-13 09:08:38.058601
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    # Old style
    assert RoleRequirement.role_yaml_parse({'role': 'role1'}) == dict(name='role1', src=None, scm=None, version=None)

    assert RoleRequirement.role_yaml_parse({'role': 'role1,v1'}) == dict(name='role1', src=None, scm=None, version='v1')

    assert RoleRequirement.role_yaml_parse({'role': 'role1,v1,name1'}) == dict(name='name1', src=None, scm=None, version='v1')


# Generated at 2022-06-13 09:08:49.770992
# Unit test for method repo_url_to_role_name of class RoleRequirement

# Generated at 2022-06-13 09:09:01.791549
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    role_req = RoleRequirement()

    assert role_req.repo_url_to_role_name("https://github.com/example/example.git") == "example.git"
    assert role_req.repo_url_to_role_name("https://github.com/example/example.git,1.0") == "example.git"
    assert role_req.repo_url_to_role_name("https://github.com/example/example.git,1.0,example") == "example.git"
    assert role_req.repo_url_to_role_name("https://github.com/example/example.tar.gz") == "example.tar.gz"

# Generated at 2022-06-13 09:09:10.045411
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    #
    # Test role name with one argument: git url
    #

    role_definition = "https://github.com/username/rolename"
    assert RoleRequirement.role_yaml_parse(role_definition)["name"] == "rolename"
    assert RoleRequirement.role_yaml_parse(role_definition)["src"] == "https://github.com/username/rolename"

    role_definition = "git+git://git.myproject.org/MyProject"
    assert RoleRequirement.role_yaml_parse(role_definition)["src"] == "git://git.myproject.org/MyProject"
    assert RoleRequirement.role_yaml_parse(role_definition)["scm"] == "git"

    role_definition = "http://github.com/someuser/someproject"

# Generated at 2022-06-13 09:09:19.403660
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name("http://github.com/geerlingguy/ansible-role-apache") == "ansible-role-apache"
    assert RoleRequirement.repo_url_to_role_name("http://github.com/FooBar/ansible-role-apache") == "ansible-role-apache"
    assert RoleRequirement.repo_url_to_role_name("https://github.com/FooBar/ansible-role-apache") == "ansible-role-apache"
    assert RoleRequirement.repo_url_to_role_name("https://github.com/geerlingguy/ansible-role-apache") == "ansible-role-apache"

# Generated at 2022-06-13 09:09:31.803678
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    # test check no src
    role = {}
    result = RoleRequirement.role_yaml_parse(role)
    assert result["name"] == ""
    assert result["scm"] is None
    assert result["src"] == ""
    assert result["version"] == ""

    # test check no name, with version
    role = {}
    role["role"] = "," + "1.0"
    result = RoleRequirement.role_yaml_parse(role)
    assert result["name"] == ""
    assert result["scm"] is None
    assert result["src"].strip() == ""
    assert result["version"] == "1.0"

    # test check with name, no version
    role = {}
    role["role"] = "foo"
    result = RoleRequirement.role_yaml_parse(role)


# Generated at 2022-06-13 09:09:40.981070
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    f = RoleRequirement.role_yaml_parse

    # src
    assert f("git@github.com:apache/cassandra.git") == dict(name="cassandra", src="git@github.com:apache/cassandra.git", scm=None, version=None)
    assert f("https://github.com/apache/cassandra/archive/cassandra-2.0.6.tar.gz") == dict(name="cassandra", src="https://github.com/apache/cassandra/archive/cassandra-2.0.6.tar.gz", scm=None, version=None)
    assert f("apache.cassandra,1.2.3") == dict(name="cassandra", src="apache.cassandra", scm=None, version="1.2.3")


# Generated at 2022-06-13 09:09:52.478111
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    # The method is static, hence the way it is tested here
    # with the class name just to make it readable,
    # and one can clearly see the tested class.

    # No comma, just the role name
    role = 'role_name'
    assert RoleRequirement.role_yaml_parse(role) == dict(name='role_name', src=None, scm=None, version=None)

    # Simple case, src with a version
    role = 'role_name,1.0'
    assert RoleRequirement.role_yaml_parse(role) == dict(name='role_name', src=None, scm=None, version='1.0')

    # src case, name with a version
    role = 'role_name,1.0,some_name'
    assert RoleRequirement.role_yaml_parse

# Generated at 2022-06-13 09:10:01.104403
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    role = 'git+https://github.com/coveooss/ansible-coveo.git,1.0.3,coveo.ansible'
    r = RoleRequirement.role_yaml_parse(role)
    assert r['name'] == 'coveo.ansible'
    assert r['scm'] == 'git'
    assert r['src'] == 'https://github.com/coveooss/ansible-coveo.git'
    assert r['version'] == '1.0.3'

if __name__ == '__main__':
    test_RoleRequirement_role_yaml_parse()

# Generated at 2022-06-13 09:10:10.876067
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    role = RoleRequirement.role_yaml_parse('http://github.com/user/name,v1.0,foobar')
    assert role['scm'] == 'git'
    assert role['version'] == 'v1.0'
    assert role['name'] == 'foobar'
    assert role['src'] == 'http://github.com/user/name'

    role = RoleRequirement.role_yaml_parse('http://github.com/user/name,foobar')
    assert role['scm'] == 'git'
    assert role['version'] == ''
    assert role['name'] == 'foobar'
    assert role['src'] == 'http://github.com/user/name'

    role = RoleRequirement.role_yaml_parse('http://github.com/user/name,foobar')
   

# Generated at 2022-06-13 09:10:30.070475
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    assert RoleRequirement.role_yaml_parse('http://github.com/user/test,test-version') == dict(name='test', version='test-version', src='http://github.com/user/test', scm=None), 'incorrect role requirements parsing'

# Generated at 2022-06-13 09:10:39.220843
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    # Does the function handle string input
    assert(RoleRequirement.role_yaml_parse('my_role') == dict(name='my_role', src='my_role', version='', scm=None),
        RoleRequirement.role_yaml_parse('my_role'))

    # Does the function handle old style input with 'role'
    assert(RoleRequirement.role_yaml_parse(dict(role='my_role')) == dict(name='my_role', src='my_role', version='', scm=None),
        RoleRequirement.role_yaml_parse(dict(role='my_role')))

    # Does the function handle new style input with 'role'

# Generated at 2022-06-13 09:10:50.160335
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    # test for normal flow
    assert RoleRequirement.role_yaml_parse('geerlingguy.java,1.6.0') == {'name': 'geerlingguy.java', 'scm': None, 'src': 'geerlingguy.java', 'version': '1.6.0'}
    assert RoleRequirement.role_yaml_parse('geerlingguy.java') == {'name': 'geerlingguy.java', 'scm': None, 'src': 'geerlingguy.java', 'version': ''}
    assert RoleRequirement.role_yaml_parse('robertdebock.bootstrap') == {'name': 'robertdebock.bootstrap', 'scm': None, 'src': 'robertdebock.bootstrap', 'version': ''}
    assert RoleRequirement.role_y

# Generated at 2022-06-13 09:10:53.471231
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    role_name = RoleRequirement.repo_url_to_role_name('role_name')
    assert role_name == 'role_name'


# Generated at 2022-06-13 09:11:03.383842
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():

    from ansible.utils.path import unfrackpath


# Generated at 2022-06-13 09:11:12.967960
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.tar.gz") == "repo"
    assert RoleRequirement.repo_url_to_role_name("git+http://git.example.com/repos/repo.git,v1.0") == "repo"

# Generated at 2022-06-13 09:11:21.024301
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    display.verbosity = 4

    # Old style galaxy use
    role = "geerlingguy.redis"
    role_yaml_parse_output = RoleRequirement.role_yaml_parse(role)
    assert role_yaml_parse_output == dict(name='geerlingguy.redis', src='geerlingguy.redis', scm=None, version=None), role_yaml_parse_output

    # Old style galaxy use, with version specified
    role = "geerlingguy.redis,1.0"
    role_yaml_parse_output = RoleRequirement.role_yaml_parse(role)

# Generated at 2022-06-13 09:11:31.433961
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():

    repo_urls = {
        'http://git.example.com/repos/repo.git' : 'repo',
        'http://git.example.com/repos/repo.git,' : 'repo',
        'http://git.example.com/repos/repo.git,1.0' : 'repo',
        'http://git.example.com/repos/repo.git,1.0,name' : 'repo',
    }

    for repo_url in repo_urls.keys():
        name = RoleRequirement.repo_url_to_role_name(repo_url)
        print(repo_url, name)
        assert name == repo_urls[repo_url]


# Generated at 2022-06-13 09:11:35.855798
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    repo_url = "http://git.example.com/repos/repo.git"
    print("role_name == ", RoleRequirement.repo_url_to_role_name(repo_url))
    assert RoleRequirement.repo_url_to_role_name(repo_url) == "repo"


# Generated at 2022-06-13 09:11:44.907628
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    # test simple name only
    role = RoleRequirement.role_yaml_parse('testrole-for-ansible')
    assert role == {'name': 'testrole-for-ansible', 'src': None, 'scm': None, 'version': None}

    # test name and version only
    role = RoleRequirement.role_yaml_parse('testrole-for-ansible,1.1.1')
    assert role == {'name': 'testrole-for-ansible', 'src': None, 'scm': None, 'version': '1.1.1'}

    # test name, version, and src
    role = RoleRequirement.role_yaml_parse('git+https://github.com/testrole-for-ansible,1.1.1,testrole-for-ansible')
    assert role

# Generated at 2022-06-13 09:12:35.567533
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    print("test_RoleRequirement_role_yaml_parse")

    role1 = "http://github.com/bennojoy/nginx"
    res1 = RoleRequirement.role_yaml_parse(role1)
    print(res1)
    assert res1['name'] == 'nginx'
    assert res1['src'] == 'http://github.com/bennojoy/nginx'
    assert res1['scm'] is None
    assert res1['version'] is None

    role2 = "git+http://github.com/bennojoy/nginx"
    res2 = RoleRequirement.role_yaml_parse(role2)
    print(res2)
    assert res2['name'] == 'nginx'