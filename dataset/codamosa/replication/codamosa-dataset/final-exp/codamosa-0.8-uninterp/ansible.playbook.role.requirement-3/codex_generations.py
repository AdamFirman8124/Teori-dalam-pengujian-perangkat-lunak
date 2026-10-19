

# Generated at 2022-06-13 09:03:06.766234
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    import pytest
    from ansible.playbook.role.requirement import RoleRequirement as RR

    with pytest.raises(AnsibleError):
        role = 'http://git.example.com/repos/repo.git,v1.0.0,foo,bar'
        result = RR.role_yaml_parse(role)

    role = 'http://git.example.com/repos/repo.git,v1.0.0,foo'
    result = RR.role_yaml_parse(role)

    assert(result == dict(name='foo', src='http://git.example.com/repos/repo.git', scm=None, version='v1.0.0'))


# Generated at 2022-06-13 09:03:18.052633
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    # test invocation with simple string
    role_specs = 'mike.dehaan,v1.0'
    role = RoleRequirement.role_yaml_parse(role_specs)
    assert type(role) == dict
    assert role['name'] == 'mike.dehaan'
    assert role['src'] == 'mike.dehaan'
    assert role['version'] == 'v1.0'
    assert role['scm'] is None

    # test invocation with dictionary
    role_specs = {'role': 'mike.dehaan', 'version': 'v1.0'}
    role = RoleRequirement.role_yaml_parse(role_specs)
    assert type(role) == dict
    assert role['name'] == 'mike.dehaan'

# Generated at 2022-06-13 09:03:28.213488
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():

    assert RoleRequirement.repo_url_to_role_name("http://github.com/ansible/ansible-examples/archive/devel.tar.gz") == 'ansible-examples'
    assert RoleRequirement.repo_url_to_role_name("https://github.com/foo/bar") == 'bar'
    assert RoleRequirement.repo_url_to_role_name("https://github.com/foo/bar.git") == 'bar'
    assert RoleRequirement.repo_url_to_role_name("https://github.com/foo/bar,v1.2.3") == 'bar'
    assert RoleRequirement.repo_url_to_role_name("https://github.com/foo/bar,v1.2.3,name") == 'bar'
    assert Role

# Generated at 2022-06-13 09:03:39.547745
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    # For github.com URL
    assert RoleRequirement.repo_url_to_role_name(
        'https://github.com/someuser/somerepo.git') == 'somerepo'
    assert RoleRequirement.repo_url_to_role_name(
        'git+git://github.com/someuser/somerepo.git') == 'somerepo'

    # For gitlab.com URL
    assert RoleRequirement.repo_url_to_role_name(
        'https://gitlab.com/someuser/somerepo.git') == 'somerepo'
    assert RoleRequirement.repo_url_to_role_name(
        'git+git://gitlab.com/someuser/somerepo.git') == 'somerepo'

    # For bitbucket.org

# Generated at 2022-06-13 09:03:52.149386
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    from nose.tools import assert_equal


# Generated at 2022-06-13 09:04:06.698660
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    from ansible.playbook.role.requirement import RoleRequirement

    # test for old style
    errors = 0
    test_yaml = {
        "role":         "myrole",
        "notallowed1":  "foo",
        "notallowed2":  "bar",

    }
    expected_output = {
        "name": "myrole",
        "scm": None,
        "src": None,
        "version": None,
    }
    output = RoleRequirement.role_yaml_parse( test_yaml )
    if output != expected_output:
        print( "expected output: %s" % expected_output )
        print( "got output: %s" % output )
        errors += 1

    # test for new style, single value for src
    errors = 0
    test_yaml

# Generated at 2022-06-13 09:04:15.619151
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.git") == 'repo'
    assert RoleRequirement.repo_url_to_role_name("https://github.com/ansible/ansible-modules-core/tarball/devel") == 'ansible-modules-core'
    assert RoleRequirement.repo_url_to_role_name("https://github.com/ansible/ansible-modules-core/tarball/devel,v1.0") == 'ansible-modules-core'
    assert RoleRequirement.repo_url_to_role_name("https://github.com/ansible/ansible-modules-core/tarball/devel,v1.0,random_name") == 'ansible-modules-core'

# Generated at 2022-06-13 09:04:17.753345
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo.git') == 'repo'


# Generated at 2022-06-13 09:04:26.170881
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    from ansible.module_utils.six import PY2

    # Test case: role_yaml_parse(role="http://github.com/foobar/ansible-myapp,v1.0")
    #   -> {"name": "ansible-myapp", "scm": "git", "src": "http://github.com/foobar/ansible-myapp,v1.0", "version": "v1.0"}
    rr = RoleRequirement()

# Generated at 2022-06-13 09:04:37.418665
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():

    s = {}
    s["http://git.example.com/repos/repo.git"] = "repo"
    s["https://jumpserver.int.example.com/repos/play.git"] = "play"
    s["jumpserver.int.example.com/repos/play.git"] = "play"
    s["git@github.com:jumpserver/play.git"] = "play"
    s["git://jumpserver.example.com/repos/play.git"] = "play"
    s["ansible-galaxy install -r requirements.yml --roles-path ./roles"] = "ansible-galaxy"
    s["git+git@git.example.com:repos/play.git"] = "play"

# Generated at 2022-06-13 09:04:59.201763
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    role_spec = RoleRequirement.role_yaml_parse("https://github.com/geerlingguy/ansible-role-apache.git")
    assert role_spec['name'] == 'ansible-role-apache'
    assert role_spec['scm'] == 'git'
    assert role_spec['src'] == 'https://github.com/geerlingguy/ansible-role-apache.git'

    role_spec = RoleRequirement.role_yaml_parse("https://github.com/geerlingguy/ansible-role-apache,v1.0")
    assert role_spec['name'] == 'ansible-role-apache'
    assert role_spec['scm'] == 'git'

# Generated at 2022-06-13 09:05:10.126850
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    # We define two roles, one with a name and one without a name
    role_with_name = {'role': 'test-role'}
    role_without_name = {'role': 'test-role,master'}

    # We define a new style role, with a 'src' keyword and with a 'src' keyword containing the name
    new_style_role = {'src': 'test-role,master'}
    new_style_role_with_custom_name = {'src': 'test-role,master,test-role-custom-name'}

    # We test the method role_yaml_parse with a role defined with and without a name
    result_with_name = RoleRequirement.role_yaml_parse(role_with_name)
    result_without_name = RoleRequirement.role_yaml_parse

# Generated at 2022-06-13 09:05:20.424397
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    role = "kubernetes,0.3.3,russmckendrick.kubernetes"
    rsp = RoleRequirement.role_yaml_parse(role)
    assert rsp['name'] == 'russmckendrick.kubernetes'

    role = "galaxy.role,version,name"
    rsp = RoleRequirement.role_yaml_parse(role)
    assert rsp['name'] == 'name'

    role = dict(role="galaxy.role")
    rsp = RoleRequirement.role_yaml_parse(role)
    assert rsp['name'] == 'galaxy.role'

    role = dict(src="galaxy.role")
    rsp = RoleRequirement.role_yaml_parse(role)

# Generated at 2022-06-13 09:05:29.386382
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    role_requirement = RoleRequirement()

    # valid SSH-style git url
    repo_url = "git+ssh://git@git.example.com/repos/repo.git"
    role_name = role_requirement.repo_url_to_role_name(repo_url)
    assert role_name == "repo"

    # valid HTTP-style git url
    repo_url = "git+http://git.example.com/repos/repo.git"
    role_name = role_requirement.repo_url_to_role_name(repo_url)
    assert role_name == "repo"

    # invalid url
    repo_url = "git+httpss://git.example.com/repos/repo.git"
    role_name = role_requirement.re

# Generated at 2022-06-13 09:05:41.461886
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    import os

# Generated at 2022-06-13 09:05:51.650535
# Unit test for method repo_url_to_role_name of class RoleRequirement

# Generated at 2022-06-13 09:06:04.814009
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    from ansible.playbook.role.requirement import RoleRequirement

    # test 1
    role2 = RoleRequirement.role_yaml_parse('src')
    assert role2['src'] == 'src'
    assert role2['scm'] is None
    assert role2['name'] == 'src'
    assert role2['version'] is None

    # test 2
    role3 = RoleRequirement.role_yaml_parse('src,version')
    assert role3['src'] == 'src'
    assert role3['scm'] is None
    assert role3['name'] == 'src'
    assert role3['version'] == 'version'

    # test 3
    role4 = RoleRequirement.role_yaml_parse('src,version,name')
    assert role4['src'] == 'src'
    assert role

# Generated at 2022-06-13 09:06:19.361084
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    # Test 1 :
    # With role =  role_name,role_verion,role_src
    # Expected : Name = role_name, Version = role_version, Source = role_src
    obj = RoleRequirement()
    role = "role_name,role_verion,role_src"
    role = obj.role_yaml_parse(role)
    assert role['name'] == "role_name", "Name is wrong, should be role_name"
    assert role['version'] == "role_verion", "Version is wrong, should be role_verion"
    assert role['src'] == "role_src", "Source is wrong, should be role_src"

    # Test 2:
    # With role = role_name
    # Expected : Name = role_name, Version = None, Source = role_name


# Generated at 2022-06-13 09:06:27.588163
# Unit test for method role_yaml_parse of class RoleRequirement

# Generated at 2022-06-13 09:06:40.526656
# Unit test for method repo_url_to_role_name of class RoleRequirement

# Generated at 2022-06-13 09:07:07.451690
# Unit test for method role_yaml_parse of class RoleRequirement

# Generated at 2022-06-13 09:07:17.539576
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    url_form1 = "http://git.example.com/repos/repo.git"
    assert RoleRequirement.repo_url_to_role_name(url_form1) == 'repo'

    url_form2 = "http://git.example.com/repos/repo.tar.gz"
    assert RoleRequirement.repo_url_to_role_name(url_form2) == 'repo'

    url_form3 = "http://git.example.com/repos/repo.tar.gz,v0.0.1"
    assert RoleRequirement.repo_url_to_role_name(url_form3) == 'repo'


# Generated at 2022-06-13 09:07:28.471863
# Unit test for method repo_url_to_role_name of class RoleRequirement

# Generated at 2022-06-13 09:07:36.851687
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    print('\n>>>>>>>>>> Testing RoleRequirement class - repo_url_to_role_name method')

    # input

# Generated at 2022-06-13 09:07:47.324043
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    assert RoleRequirement.role_yaml_parse('mysql') == {'name': 'mysql', 'src': 'mysql', 'scm': None, 'version': ''}
    assert RoleRequirement.role_yaml_parse('mysql,1.0.x') == {'name': 'mysql', 'src': 'mysql', 'scm': None, 'version': '1.0.x'}
    assert RoleRequirement.role_yaml_parse('mysql,1.0.x,awesome_db') == {'name': 'awesome_db', 'src': 'mysql', 'scm': None, 'version': '1.0.x'}

# Generated at 2022-06-13 09:07:56.903459
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    role = { "role": "geerlingguy.apache" }
    assert RoleRequirement.role_yaml_parse(role) == dict(name="geerlingguy.apache", src=None, scm=None, version=None)

    role = { "role": "geerlingguy.apache,v1.0.0" }
    assert RoleRequirement.role_yaml_parse(role) == dict(name="geerlingguy.apache", src=None, scm=None, version="v1.0.0")

    role = { "role": "git+git://github.com/geerlingguy/ansible-role-apache.git,v1.0.0" }

# Generated at 2022-06-13 09:08:09.252271
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name("http://abc.com/ansible-role-test.git") == "ansible-role-test"
    assert RoleRequirement.repo_url_to_role_name("http://abc.com/ansible-role-test-2.0.tar.gz") == "ansible-role-test-2.0"
    assert RoleRequirement.repo_url_to_role_name("git+https://github.com/ansible/ansible-modules-extras.git,devel") == "ansible-modules-extras"
    assert RoleRequirement.repo_url_to_role_name("git+https://github.com/ansible/ansible-modules-extras,devel") == "ansible-modules-extras"
    assert Role

# Generated at 2022-06-13 09:08:15.749182
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    good_values = [
        ('scm+https://github.com/foo/bar', dict(name='bar', scm='scm', src='https://github.com/foo/bar', version=None)),
        ('https://github.com/foo/bar,v1.2', dict(name='bar', scm=None, src='https://github.com/foo/bar', version='v1.2')),
        ('https://github.com/foo/bar,v1.2,fred', dict(name='fred', scm=None, src='https://github.com/foo/bar', version='v1.2')),
    ]

# Generated at 2022-06-13 09:08:29.429393
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    role_hash = { \
        'role': 'jdauphant.nginx', \
        'somevar': 'somevalue' \
    }
    role = RoleRequirement.role_yaml_parse(role_hash)
    assert role['name'] == 'jdauphant.nginx'
    assert role['src'] == 'jdauphant.nginx'
    assert role['scm'] == None
    assert role['version'] == ''
    assert role.has_key('somevar') == False
    assert role.has_key('role') == False

    role_hash = { \
        'role': 'jdauphant.nginx,v1.0', \
        'somevar': 'somevalue' \
    }
    role = RoleRequirement.role_yaml_parse(role_hash)

# Generated at 2022-06-13 09:08:42.070236
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    import pytest
    # Setup

# Generated at 2022-06-13 09:09:07.738415
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    result = RoleRequirement.role_yaml_parse("git+https://github.com/ansible/ansible-examples,devel")
    assert result['name'] == 'ansible-examples'
    assert result['scm'] == 'git'
    assert result['src'] == 'https://github.com/ansible/ansible-examples'
    assert result['version'] == 'devel'
    result = RoleRequirement.role_yaml_parse("git+https://github.com/ansible/ansible-examples")
    assert result['name'] == 'ansible-examples'
    assert result['scm'] == 'git'
    assert result['src'] == 'https://github.com/ansible/ansible-examples'
    assert result['version'] == ''
    result = RoleRequirement.role_

# Generated at 2022-06-13 09:09:18.132267
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    assert RoleRequirement().role_yaml_parse("http://git.example.com/repos/repo.git") == {'name': 'repo'}
    assert RoleRequirement().role_yaml_parse("http://git.example.com/repos/repo.git,v1") == {'name': 'repo', 'version': 'v1'}
    assert RoleRequirement().role_yaml_parse("http://git.example.com/repos/repo.git,v1,epel") == {'name': 'epel', 'version': 'v1'}
    assert RoleRequirement().role_yaml_parse("https://github.com/ansible/ansible-examples,devel,my_debian") == {'name': 'my_debian', 'version': 'devel'}

# Generated at 2022-06-13 09:09:25.525730
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    class Test_role_yaml_parse():
        def __init__(self, name, expected_result):
            self.name = name
            self.expected_result = expected_result

    # list of dictionaries that contain input and expected output {input, expected_output}

# Generated at 2022-06-13 09:09:35.479442
# Unit test for method repo_url_to_role_name of class RoleRequirement

# Generated at 2022-06-13 09:09:43.238139
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name('https://github.com/foo/bar') == 'bar'
    assert RoleRequirement.repo_url_to_role_name('https://github.com/foo/bar.git') == 'bar'
    assert RoleRequirement.repo_url_to_role_name('https://github.com/foo/bar.tar.gz') == 'bar'
    assert RoleRequirement.repo_url_to_role_name('https://github.com/foo/bar.tar.gz,v1.0') == 'bar'
    assert RoleRequirement.repo_url_to_role_name('https://github.com/foo/bar.tar.gz,v1.0,myrole') == 'myrole'
    assert RoleRequirement.repo_url_

# Generated at 2022-06-13 09:09:54.784730
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name("https://github.com/ansible/ansible-examples.git") == "ansible-examples"
    assert RoleRequirement.repo_url_to_role_name("http://github.com/ansible/ansible-examples.git") == "ansible-examples"
    assert RoleRequirement.repo_url_to_role_name("git+https://github.com/ansible/ansible-examples.git") == "ansible-examples"
    assert RoleRequirement.repo_url_to_role_name("git+http://github.com/ansible/ansible-examples.git") == "ansible-examples"

# Generated at 2022-06-13 09:10:03.933211
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    # Conditional use of python 2/3 library unittest
    try:
        import unittest2 as unittest
    except ImportError:
        import unittest

    # Class to test the constructor and method RoleRequirement.role_yaml_parse
    class TestRoleRequirement(unittest.TestCase):

        # Set up the object and data to be used in the tests
        def setUp(self):
            self.requirement = RoleRequirement()

# Generated at 2022-06-13 09:10:12.722136
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    import pprint
    pp = pprint.PrettyPrinter(indent=4)


# Generated at 2022-06-13 09:10:15.578348
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    role = RoleRequirement()
    print(role.repo_url_to_role_name('http://github.com/galaxy_role.git'))


# Generated at 2022-06-13 09:10:26.553628
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():

    # Test case 1
    # "http://git.example.com/repos/repo.git" => "repo"

    expected_value = "repo"
    actual_value = RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.git")
    if actual_value != expected_value:
        raise AssertionError()

    # Test case 2
    # "http://git.example.com/repos/repo-1.0.0.tar.gz" => "repo-1.0.0"

    expected_value = "repo-1.0.0"

# Generated at 2022-06-13 09:10:41.382784
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    repo_url = "http://git.example.com/repos/repo.git"
    assert RoleRequirement.repo_url_to_role_name(repo_url) == "repo"

# Generated at 2022-06-13 09:10:51.993021
# Unit test for method role_yaml_parse of class RoleRequirement

# Generated at 2022-06-13 09:10:56.848761
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name("git+git://git@git.example.com/repos/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("git+http://git.example.com/repos/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("https://git.example.com/repos/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("https://git.example.com/repos/repo.git") == "repo"

# Generated at 2022-06-13 09:11:05.259431
# Unit test for method role_yaml_parse of class RoleRequirement

# Generated at 2022-06-13 09:11:15.161064
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("https://git.example.com/repos/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("git@git.example.com/repos/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("svn+ssh://git.example.com/repos/repo.git") == "repo"

# Generated at 2022-06-13 09:11:22.421229
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():

    r = RoleRequirement
    test_cases = [
        # repo_url, role_name
        ("https://github.com/geerlingguy/ansible-role-redis.git", "geerlingguy.redis"),
        ("git@github.com:geerlingguy/ansible-role-redis.git", "geerlingguy.redis"),
        ("git+https://github.com/geerlingguy/ansible-role-redis.git", "geerlingguy.redis"),
        ("geerlingguy.redis", "geerlingguy.redis"),
    ]

    for (repo_url, role_name) in test_cases:
        test_case = r.repo_url_to_role_name(repo_url)
        assert test_case == role_name

# Generated at 2022-06-13 09:11:32.906956
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    assert RoleRequirement.role_yaml_parse('geerlingguy.apache') == {'name': 'geerlingguy.apache', 'src': 'geerlingguy.apache', 'scm': None, 'version': ''}
    assert RoleRequirement.role_yaml_parse('https://github.com/geerlingguy/ansible-role-apache') == {'name': 'ansible-role-apache', 'src': 'https://github.com/geerlingguy/ansible-role-apache', 'scm': None, 'version': ''}

# Generated at 2022-06-13 09:11:40.338662
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    role_requirement = RoleRequirement()

    repo_url = 'http://git.example.com/repos/repo.git'
    assert role_requirement.repo_url_to_role_name(repo_url) == 'repo'
    repo_url = 'http://git.example.com/repos/galaxy_role.git'
    assert role_requirement.repo_url_to_role_name(repo_url) == 'galaxy_role'
    repo_url = 'http://git.example.com/repos/galaxy_role.tar.gz'
    assert role_requirement.repo_url_to_role_name(repo_url) == 'galaxy_role'

# Generated at 2022-06-13 09:11:46.930276
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    rr = RoleRequirement()
    assert rr.role_yaml_parse("role_name") == {'name': 'role_name', 'scm': None, 'src': 'role_name', 'version': None}
    assert rr.role_yaml_parse("role_name,1.0") == {'name': 'role_name', 'scm': None, 'src': 'role_name', 'version': '1.0'}
    assert rr.role_yaml_parse("role_name,1.0,another_name") == {'name': 'another_name', 'scm': None, 'src': 'role_name', 'version': '1.0'}

# Generated at 2022-06-13 09:12:00.608829
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert 'role' == RoleRequirement.repo_url_to_role_name('git+git@git.example.com/role.git')
    assert 'role' == RoleRequirement.repo_url_to_role_name('git+https://git.example.com/role.git')
    assert 'role' == RoleRequirement.repo_url_to_role_name('git+https://git.example.com/role,v1.0')
    assert 'role' == RoleRequirement.repo_url_to_role_name('git+https://git.example.com/role,v1.0,role_name')
    assert 'role' == RoleRequirement.repo_url_to_role_name('git+https://git.example.com/role.git')
    assert 'role' == RoleRequirement

# Generated at 2022-06-13 09:12:22.073515
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    print('Testing function: RoleRequirement.role_yaml_parse')

# Generated at 2022-06-13 09:12:32.554409
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    assert RoleRequirement.role_yaml_parse('myrole') == dict(name='myrole', src='myrole', scm=None, version='')
    assert RoleRequirement.role_yaml_parse('user.myrole') == dict(name='user.myrole', src='user.myrole', scm=None, version='')
    assert RoleRequirement.role_yaml_parse('https://github.com/username/myrole') == dict(name='myrole', src='https://github.com/username/myrole', scm=None, version='')