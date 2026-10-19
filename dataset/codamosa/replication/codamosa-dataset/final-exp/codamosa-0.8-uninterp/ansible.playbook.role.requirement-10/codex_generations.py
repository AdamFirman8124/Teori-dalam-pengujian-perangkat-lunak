

# Generated at 2022-06-13 09:03:02.944137
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    from ansible.parsing.yaml.objects import AnsibleMapping

    # Test: minimum requirement
    input_yaml = {'src': 'https://github.com/ansible/role_example.git'}
    output_yaml = RoleRequirement.role_yaml_parse(input_yaml)
    expected_output_yaml = AnsibleMapping(dict(
        name='role_example',
        src='https://github.com/ansible/role_example.git',
        version='',
        scm=None
    ))
    assert output_yaml == expected_output_yaml

    # Test: maximum requirement
    input_yaml = {'scm': 'hg', 'src': 'https://bitbucket.org/ansible/role_example,myversion,myname'}
    output

# Generated at 2022-06-13 09:03:10.443676
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    role_requirement = RoleRequirement()

    # Testing with default/correct format of yaml
    yaml_content = dict(
        name='ansible-role-nginx',
        src='https://github.com/jdauphant/ansible-role-nginx.git',
        scm='git',
        version='v1.0'
    )
    expected_results = dict(
        name='ansible-role-nginx',
        src='https://github.com/jdauphant/ansible-role-nginx.git',
        scm='git',
        version='v1.0'
    )
    results = role_requirement.role_yaml_parse(yaml_content)

    assert results == expected_results, "Default format of yaml parsing not working"

    # Testing with different format of

# Generated at 2022-06-13 09:03:16.486316
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    test_values = [
        # (
        #     expected_name,
        #     expected_version,
        #     expected_scm,
        #     expected_src,
        #     role
        # )
        (
            'foo_role',
            None,
            'git',
            'foo.role.git',
            'git+foo.role.git'
        ),
        (
            'bar_role',
            None,
            'git',
            'bar.role.git',
            'git+git://bar.role.git'
        ),
        (
            'baz_role',
            'master',
            'git',
            'baz.role.git',
            {'src': 'git+baz.role.git,master'}
        ),
    ]


# Generated at 2022-06-13 09:03:26.883221
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    # Test normal cases
    test_str1 = 'git://git@gitlab.some.com/some/repo.git'
    assert RoleRequirement.repo_url_to_role_name(test_str1) == 'repo'

    test_str2 = 'git@gitlab.some.com/some/repo.git'
    assert RoleRequirement.repo_url_to_role_name(test_str2) == 'repo'

    test_str3 = 'https://gitlab.some.com/some/repo.git'
    assert RoleRequirement.repo_url_to_role_name(test_str3) == 'repo'

    test_str4 = 'http://gitlab.some.com/some/repo.git'
    assert RoleRequirement.repo_url_

# Generated at 2022-06-13 09:03:38.003401
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name("git@gitlab.example.com:foo/bar.git") == "bar"
    assert RoleRequirement.repo_url_to_role_name("git@gitlab.example.com:foo/bar.git,v2.0") == "bar"
    assert RoleRequirement.repo_url_to_role_name("git@gitlab.example.com:foo/bar.git,v2.0,myname") == "bar"
    assert RoleRequirement.repo_url_to_role_name("https://gitlab.com/foo/bar.git") == "bar"
    assert RoleRequirement.repo_url_to_role_name("git+https://gitlab.com/foo/bar.tar.gz") == "bar"
   

# Generated at 2022-06-13 09:03:49.090339
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("ssh://git@git.example.com/repos/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo") == "repo"
    assert RoleRequirement.repo_url_to_role_name("git@git.example.com/repos/repo") == "repo"
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.git,v1.0") == "repo"
   

# Generated at 2022-06-13 09:03:57.911335
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    """Unit test for method role_yaml_parse of class RoleRequirement"""

    results = dict()
    results = RoleRequirement.role_yaml_parse("role_name")
    if not results['name'] == 'role_name' and not results['scm'] is None and not results['src'] is None and not results['version'] is None:
        raise AssertionError("role_yaml_parse parsing 'role_name' failed")

    results = RoleRequirement.role_yaml_parse("https://github.com/someuser/somerepo.git,myversion")

# Generated at 2022-06-13 09:04:10.858153
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    name = "name"
    src = "src"
    scm = "scm"
    version = "version"
    out = dict(name=name, src=src, scm=scm, version=version)

    role = "%s,%s,%s" % (src, version, name)
    assert RoleRequirement.role_yaml_parse(role) == out

    role = "scm+%s" % src
    out["scm"] = "git"
    assert RoleRequirement.role_yaml_parse(role) == out

    role = "%s,%s" % (src, version)
    out["name"] = RoleRequirement.repo_url_to_role_name(src)
    del out["scm"]

# Generated at 2022-06-13 09:04:20.944535
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    assert RoleRequirement.role_yaml_parse('foo') == {'name': 'foo', 'scm': None, 'src': 'foo', 'version': None}
    assert RoleRequirement.role_yaml_parse('foo,1.2') == {'name': 'foo', 'scm': None, 'src': 'foo', 'version': '1.2'}
    assert RoleRequirement.role_yaml_parse('foo,1.2,foofoo') == {'name': 'foofoo', 'scm': None, 'src': 'foo', 'version': '1.2'}

# Generated at 2022-06-13 09:04:28.085108
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name('https://github.com/erasme/ansible-role-ovirt') == 'ansible-role-ovirt'
    assert RoleRequirement.repo_url_to_role_name('https://github.com/erasme/ansible-role-ovirt.git') == 'ansible-role-ovirt'
    assert RoleRequirement.repo_url_to_role_name('git+https://github.com/erasme/ansible-role-ovirt') == 'ansible-role-ovirt'
    assert RoleRequirement.repo_url_to_role_name('git+https://github.com/erasme/ansible-role-ovirt.git') == 'ansible-role-ovirt'
    assert RoleRequirement.re

# Generated at 2022-06-13 09:04:56.084618
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    display.vvvv('test_RoleRequirement_repo_url_to_role_name')
    assert RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo.git,v1,me') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo.tar.gz,v1,me') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('git://git.example.com/repos/repo.git,v1,me') == 'repo'

# Generated at 2022-06-13 09:05:05.727632
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    result = RoleRequirement.repo_url_to_role_name("git://git.example.com/repos/repo.git")
    assert result == "repo"

    result = RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.git")
    assert result == "repo"

    result = RoleRequirement.repo_url_to_role_name("https://git.example.com/repos/repo.git")
    assert result == "repo"

    result = RoleRequirement.repo_url_to_role_name("ssh://git@git.example.com/repos/repo.git")
    assert result == "repo"


# Generated at 2022-06-13 09:05:18.233451
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    from ansible.utils.unicode import to_unicode


# Generated at 2022-06-13 09:05:27.780836
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    display.debug("role: test_RoleRequirement_repo_url_to_role_name")

    repo_url = "https://github.com/geerlingguy/ansible-role-security.git"
    role = RoleRequirement()
    assert role.repo_url_to_role_name(repo_url) == "ansible-role-security"

    repo_url = "https://github.com/geerlingguy/ansible-role-security"
    assert role.repo_url_to_role_name(repo_url) == "ansible-role-security"

    repo_url = "git@github.com:geerlingguy/ansible-role-security"
    assert role.repo_url_to_role_name(repo_url) == "ansible-role-security"

# Generated at 2022-06-13 09:05:34.419378
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    """
    Unit testing of method repo_url_to_role_name as per contract in ../README.md.

    :return: None
    """

    if RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.git") != "repo":
        print("ERROR: RoleRequirement.repo_url_to_role_name failed for http://git.example.com/repos/repo.git")
        exit(1)


# Generated at 2022-06-13 09:05:47.196585
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('git://git.example.com/repos/repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('https://git.example.com/repos/repo/') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('git@git.example.com:repos/repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('http://user@git.example.com/repos/repo.git') == 'repo'
    assert Role

# Generated at 2022-06-13 09:06:00.655695
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    role = RoleRequirement.role_yaml_parse("src")
    assert role["name"] == "src"
    assert role["src"] == "src"
    assert role["scm"] is None
    assert role["version"] == ""

    role = RoleRequirement.role_yaml_parse("src,version")
    assert role["name"] == "src"
    assert role["src"] == "src"
    assert role["scm"] is None
    assert role["version"] == "version"

    role = RoleRequirement.role_yaml_parse("src,version,name")
    assert role["name"] == "name"
    assert role["src"] == "src"
    assert role["scm"] is None
    assert role["version"] == "version"


# Generated at 2022-06-13 09:06:08.432509
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    assert RoleRequirement.role_yaml_parse('geerlingguy.nginx') == {'name': 'geerlingguy.nginx', 'src': 'geerlingguy.nginx', 'scm': None, 'version': ''}
    assert RoleRequirement.role_yaml_parse('git+https://github.com/geerlingguy/ansible-role-virtualbox,v4.0.0,geerlingguy.virtualbox') == {'name': 'geerlingguy.virtualbox', 'src': 'https://github.com/geerlingguy/ansible-role-virtualbox,v4.0.0', 'scm': 'git', 'version': ''}

# Generated at 2022-06-13 09:06:16.964378
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    '''
    repo_url_to_role_name of class RoleRequirement for testing:
    '''
    # Test the method
    test = RoleRequirement()
    # case1: url with '@' and suffix with '.tar'
    url_01 = 'http://git.example.com/repos/foo.tar'
    assert test.repo_url_to_role_name(url_01) == 'foo'
    # case2: url with '@' and suffix with '.tar.gz'
    url_02 = 'http://git.example.com/repos/foo.tar.gz'
    assert test.repo_url_to_role_name(url_02) == 'foo'
    # case3: url with '://' and suffix with '.git'

# Generated at 2022-06-13 09:06:25.773423
# Unit test for method repo_url_to_role_name of class RoleRequirement

# Generated at 2022-06-13 09:06:42.059022
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    # Test new style role definition
    role_definition = dict(src='git+https://github.com/my_name/my_repo.git')
    role = RoleRequirement.role_yaml_parse(role_definition)
    assert role['name'] == 'my_repo'
    assert role['scm'] == 'git'
    assert role['src'] == 'https://github.com/my_name/my_repo.git'
    assert role['version'] == ''

    role_definition = dict(src='git+file:///path/to/repo.git')
    role = RoleRequirement.role_yaml_parse(role_definition)
    assert role['name'] == 'repo'
    assert role['scm'] == 'git'

# Generated at 2022-06-13 09:06:52.995373
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    from ansible.playbook.role.requirement import RoleRequirement
    from ansible.errors import AnsibleError

    # Test case should pass

# Generated at 2022-06-13 09:07:04.407890
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    assert RoleRequirement.role_yaml_parse({'role': 'foo'}) == {'name': 'foo'}
    assert RoleRequirement.role_yaml_parse({'src': 'foo'}) == {'name': 'foo', 'src': 'foo', 'scm': None, 'version': ''}
    assert RoleRequirement.role_yaml_parse({'src': 'git+foo'}) == {'name': 'foo', 'src': 'foo', 'scm': 'git', 'version': ''}
    assert RoleRequirement.role_yaml_parse({'src': 'foo,v1'}) == {'name': 'foo', 'src': 'foo', 'scm': None, 'version': 'v1'}

# Generated at 2022-06-13 09:07:12.414420
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    role = 'geerlingguy.nginx'
    assert RoleRequirement.role_yaml_parse(role) == {
        'name': 'geerlingguy.nginx',
        'role': 'geerlingguy.nginx',
        'scm': None,
        'src': None,
        'version': None,
    }

    role = {'role': 'geerlingguy.nginx'}
    assert RoleRequirement.role_yaml_parse(role) == {
        'name': 'geerlingguy.nginx',
        'role': 'geerlingguy.nginx',
        'scm': None,
        'src': None,
        'version': None,
    }

    role = 'galaxy.role,v0.1.0'
    assert RoleRequirement.role_y

# Generated at 2022-06-13 09:07:15.497656
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    # TODO: Add unit tests
    pass


# Generated at 2022-06-13 09:07:26.165774
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    from ansible.utils.collection_loader._collection_finder import get_role_definition_from_role_yml


# Generated at 2022-06-13 09:07:35.013816
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    from nose.tools import assert_true, assert_false, assert_equals

    assert_equals(RoleRequirement.role_yaml_parse('geerlingguy.apache'),
                  {'name': 'geerlingguy.apache', 'src': 'geerlingguy.apache', 'scm': None, 'version': ''})
    assert_equals(RoleRequirement.role_yaml_parse('https://github.com/geerlingguy/ansible-role-apache'),
                  {'name': 'ansible-role-apache', 'src': 'https://github.com/geerlingguy/ansible-role-apache', 'scm': None, 'version': ''})

# Generated at 2022-06-13 09:07:45.555586
# Unit test for method role_yaml_parse of class RoleRequirement

# Generated at 2022-06-13 09:07:55.583291
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    from ansible.module_utils.six import string_types

# Generated at 2022-06-13 09:07:59.702656
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    repo_url = "https://github.com/ght/role_name.git"
    expected = "role_name"
    assert RoleRequirement.repo_url_to_role_name(repo_url) == expected

# Generated at 2022-06-13 09:08:24.141754
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    print("Test RoleRequirement.role_yaml_parse method")

    def parse(role_line, role_name=None, version=None, src=None, scm=None):
        print("Role line: ", role_line)
        role = RoleRequirement.role_yaml_parse(role_line)

        assert role["name"] == role_name
        assert role["src"] == src
        assert role["version"] == version
        assert role["scm"] == scm

    print("Test for old inline style roles")
    parse("http://github.com/user/repo",
          "repo", None, "http://github.com/user/repo", None)

# Generated at 2022-06-13 09:08:36.919020
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    # github.com
    role = 'https://github.com/galaxyproject/ansible-galaxy.git,v1.0'
    assert RoleRequirement.role_yaml_parse(role) == dict(name='ansible-galaxy', src='https://github.com/galaxyproject/ansible-galaxy.git', scm='git', version='v1.0')

    # bitbucket.org
    role = 'https://bitbucket.org/ansible/ansible-modules-core.git,v2.0'
    assert RoleRequirement.role_yaml_parse(role) == dict(name='ansible-modules-core', src='https://bitbucket.org/ansible/ansible-modules-core.git', scm='git', version='v2.0')

    # gitlab.com

# Generated at 2022-06-13 09:08:49.252537
# Unit test for method role_yaml_parse of class RoleRequirement

# Generated at 2022-06-13 09:09:01.636051
# Unit test for method role_yaml_parse of class RoleRequirement

# Generated at 2022-06-13 09:09:09.951469
# Unit test for method role_yaml_parse of class RoleRequirement

# Generated at 2022-06-13 09:09:19.374661
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('https://github.com/rgl/ansible-role-rgl-base.git') == 'ansible-role-rgl-base'
    assert RoleRequirement.repo_url_to_role_name('git+ssh://user@git.example.com/repos/repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('git@github.com:rgl/ansible-role-rgl-base.git') == 'ansible-role-rgl-base'
    assert RoleRequirement.repo_url_to_role_

# Generated at 2022-06-13 09:09:26.533233
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    # Test for cases with different spec of role_name
    assert RoleRequirement.role_yaml_parse("src") == {'name': 'src', 'scm': None, 'src': 'src', 'version': ''}
    assert RoleRequirement.role_yaml_parse("src,version") == {'name': 'src', 'scm': None, 'src': 'src', 'version': 'version'}
    assert RoleRequirement.role_yaml_parse("scm+src") == {'name': 'src', 'scm': 'scm', 'src': 'src', 'version': ''}
    assert RoleRequirement.role_yaml_parse("scm+src,version") == {'name': 'src', 'scm': 'scm', 'src': 'src', 'version': 'version'}
    assert RoleRequ

# Generated at 2022-06-13 09:09:36.800316
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():

    # init
    role_requirement = RoleRequirement()

    # GIT HTTP
    repo_url = "http://git.example.com/repos/repo.git"
    role_name = role_requirement.repo_url_to_role_name(repo_url)
    assert role_name == "repo"

    # GIT SSH
    repo_url = "git@git.example.com:repos/repo.git"
    role_name = role_requirement.repo_url_to_role_name(repo_url)
    assert role_name == "repo"

    # GIT HTTPS
    repo_url = "https://git.example.com/repos/repo.git"

# Generated at 2022-06-13 09:09:48.201754
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    print("Testing RoleRequirement().role_yaml_parse")

    rr = RoleRequirement()
    result = rr.role_yaml_parse('geerlingguy.jenkins,1.0.2,version')

    assert result['name'] == 'version'
    assert result['src'] == 'geerlingguy.jenkins'
    assert result['version'] == '1.0.2'
    assert result['scm'] == None

    result = rr.role_yaml_parse(dict(role='geerlingguy.jenkins,1.0.2'))

    assert result['name'] == 'geerlingguy.jenkins'
    assert result['src'] == None
    assert result['version'] == '1.0.2'
    assert result['scm'] == None

    result = rr.role

# Generated at 2022-06-13 09:09:59.076311
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    from ansible.utils.path import unfrackpath
    import os

    # test for handle role requirement without version
    role_dict = RoleRequirement.role_yaml_parse('https://github.com/ikus060/ansible-role-test')
    assert role_dict["name"] == "ansible-role-test"
    assert role_dict["src"] == "https://github.com/ikus060/ansible-role-test"
    assert role_dict["scm"] == "git"
    assert role_dict["version"] == None

    # test for handle role requirement with version
    role_dict = RoleRequirement.role_yaml_parse('https://github.com/ikus060/ansible-role-test,v0.0.1')

# Generated at 2022-06-13 09:11:05.061716
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    ret = RoleRequirement.role_yaml_parse("foo.bar,0.1.1")
    assert ret == dict(name='foo.bar', src='foo.bar', scm=None, version='0.1.1')

    ret = RoleRequirement.role_yaml_parse("foo.bar,1.0.0,ansible-role-foo")
    assert ret == dict(name='ansible-role-foo', src='foo.bar', scm=None, version='1.0.0')

    ret = RoleRequirement.role_yaml_parse("foo.bar,v2,ansible-role-foo")
    assert ret == dict(name='ansible-role-foo', src='foo.bar', scm=None, version='v2')


# Generated at 2022-06-13 09:11:15.001111
# Unit test for method repo_url_to_role_name of class RoleRequirement

# Generated at 2022-06-13 09:11:24.592000
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
  # Test for simple case
  ret = RoleRequirement.role_yaml_parse('foo')
  assert ret == {'name': 'foo', 'src': 'foo', 'scm': None, 'version': None}
  # Test for simple case with version
  ret = RoleRequirement.role_yaml_parse('foo,0.1')
  assert ret == {'name': 'foo', 'src': 'foo', 'scm': None, 'version': '0.1'}
  # Test for complex case
  ret = RoleRequirement.role_yaml_parse('https://github.com/ansible/ansible-examples.git,v1.6,ansible.examples')

# Generated at 2022-06-13 09:11:29.791692
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    # string
    role = 'test.role'
    role_dict = RoleRequirement.role_yaml_parse(role)
    assert role_dict == {'name': 'test', 'src': role, 'scm': None, 'version': ''}

    # dict - old style
    role_dict = {'role': 'test.role'}
    test_role_dict = RoleRequirement.role_yaml_parse(role_dict)
    assert test_role_dict == {'name': 'test', 'src': 'test.role', 'scm': None, 'version': ''}

    # dict - new style
    role_dict = {'src': role_dict['role']}
    test_role_dict = RoleRequirement.role_yaml_parse(role_dict)

# Generated at 2022-06-13 09:11:38.533021
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    display.warning("TESTING:  test_RoleRequirement_repo_url_to_role_name (please ignore message above)")
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.git") == 'repo'
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo,master") == 'repo'
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.tar.gz") == 'repo'
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo,master,alternate_name") == 'repo'

#

# Generated at 2022-06-13 09:11:46.023097
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('git@git.example.com:repository') == 'repository'
    assert RoleRequirement.repo_url_to_role_name('https://github.com/user/repository.git') == 'repository'
    assert RoleRequirement.repo_url_to_role_name('git://git.example.com/repos/repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('svn://svn.example.com/repos/repo') == 'repo'
    assert RoleRequirement.repo

# Generated at 2022-06-13 09:11:59.774212
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name('rolem1') == 'rolem1', 'test1 failed'
    assert RoleRequirement.repo_url_to_role_name('http://server.com/rolem1') == 'rolem1', 'test2 failed'
    assert RoleRequirement.repo_url_to_role_name('rolem1.git') == 'rolem1', 'test3 failed'
    assert RoleRequirement.repo_url_to_role_name('http://server.com/rolem1.git') == 'rolem1', 'test4 failed'
    assert RoleRequirement.repo_url_to_role_name('rolem1.tar.gz') == 'rolem1', 'test5 failed'
    assert RoleRequirement.repo_url_to_role

# Generated at 2022-06-13 09:12:07.244870
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    # Role name without version: http://git.example.com/repos/repo.git => "repo"
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo") == "repo"

    # Role name with version: http://git.example.com/repos/repo,v1.0.0 => "repo"
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo,v1.0.0") == "repo"

    # Role name with version and name: http://git.example.com/re

# Generated at 2022-06-13 09:12:19.586900
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    dummy_class = RoleRequirement()
    assert dummy_class.role_yaml_parse('role_1') == {'name': 'role_1', 'src': 'role_1', 'scm': None, 'version': ''}
    assert dummy_class.role_yaml_parse('role_2,v2') == {'name': 'role_2', 'src': 'role_2', 'scm': None, 'version': 'v2'}
    assert dummy_class.role_yaml_parse('role_3,v3,name_3') == {'name': 'name_3', 'src': 'role_3', 'scm': None, 'version': 'v3'}

# Generated at 2022-06-13 09:12:26.054765
# Unit test for method role_yaml_parse of class RoleRequirement