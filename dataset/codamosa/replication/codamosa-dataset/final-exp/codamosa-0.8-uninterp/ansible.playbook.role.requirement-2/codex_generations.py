

# Generated at 2022-06-13 09:02:52.880952
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    assert RoleRequirement.role_yaml_parse("nginx,1.2.3,nginx_role") == {
        'name': 'nginx_role',
        'src': 'nginx',
        'scm': None,
        'version': '1.2.3'
    }
    assert RoleRequirement.role_yaml_parse("git+nginx,1.2.3,nginx_role") == {
        'name': 'nginx_role',
        'src': 'nginx',
        'scm': 'git',
        'version': '1.2.3'
    }

# Generated at 2022-06-13 09:02:59.795225
# Unit test for method role_yaml_parse of class RoleRequirement

# Generated at 2022-06-13 09:03:08.521686
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    from ansible.playbook.role.definition import RoleDefinition

    # Test case 1: expecting RoleDefinition object with name, src and version filled in
    role = RoleRequirement.role_yaml_parse('git+https://github.com/ansible/ansible-examples.git,v1.0.1,example')
    assert role['name'] == 'example'
    assert role['scm'] == 'git'
    assert role['src'] == 'https://github.com/ansible/ansible-examples.git'
    assert role['version'] == 'v1.0.1'

    # Test case 2: expecting RoleDefinition object with name, src and version filled in

# Generated at 2022-06-13 09:03:19.619274
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    role_yaml = {
        'role': 'geerlingguy.jenkins',
        'version': '1.9.3',
        'some_other_var_in_this_context': 'will be ignored by rolespec.py'
    }
    expected_result = {
        'name': 'geerlingguy.jenkins',
        'src': 'geerlingguy.jenkins',
        'scm': None,
        'version': '1.9.3',
    }
    assert RoleRequirement.role_yaml_parse(role_yaml) == expected_result

    role_string = 'geerlingguy.jenkins,1.9.3'

# Generated at 2022-06-13 09:03:29.624573
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    correct_role = {
        'name': 'test',
        'scm': 'git',
        'src': 'git@github.com:user/test.git',
        'version': 'HEAD'
    }
    assert RoleRequirement.role_yaml_parse('test') == correct_role
    assert RoleRequirement.role_yaml_parse('test.git') == correct_role
    assert RoleRequirement.role_yaml_parse('https://github.com/user/test.git') == correct_role
    assert RoleRequirement.role_yaml_parse('https://github.com/user/test.git,') == correct_role
    assert RoleRequirement.role_yaml_parse('https://github.com/user/test.git,,') == correct_role
    assert RoleRequirement.role_yaml_

# Generated at 2022-06-13 09:03:41.069999
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    url = 'git@github.com:geerlingguy/ansible-role-apache.git'
    role_name = RoleRequirement.repo_url_to_role_name(url)
    assert role_name == 'ansible-role-apache'

    url = 'https://github.com/geerlingguy/ansible-role-apache'
    role_name = RoleRequirement.repo_url_to_role_name(url)
    assert role_name == 'ansible-role-apache'

    url = 'git@github.com:geerlingguy/ansible-role-apache'
    role_name = RoleRequirement.repo_url_to_role_name(url)
    assert role_name == 'ansible-role-apache'


# Generated at 2022-06-13 09:03:51.570956
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("https://git.example.com/repos/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("git+git@git.example.com:repos/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("git+http://git.example.com:repos/repo.git") == "repo"

# Generated at 2022-06-13 09:04:06.067970
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    assert RoleRequirement.role_yaml_parse("some.scm,0.9") == {'scm': 'some.scm', 'src': '', 'name': '', 'version': '0.9'}
    assert RoleRequirement.role_yaml_parse("some.scm,0.9,testing") == {'scm': 'some.scm', 'src': '', 'name': 'testing', 'version': '0.9'}
    assert RoleRequirement.role_yaml_parse("http://some.scm,0.9,testing") == {'scm': 'http', 'src': '//some.scm', 'name': 'testing', 'version': '0.9'}

# Generated at 2022-06-13 09:04:15.108888
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    assert RoleRequirement.role_yaml_parse("src") == {
        "name": "src",
        "scm": None,
        "src": "src",
        "version": None,
    }

    assert RoleRequirement.role_yaml_parse("src,") == {
        "name": "src",
        "scm": None,
        "src": "src",
        "version": "",
    }

    assert RoleRequirement.role_yaml_parse("src, ") == {
        "name": "src",
        "scm": None,
        "src": "src",
        "version": "",
    }


# Generated at 2022-06-13 09:04:24.676240
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    """
    Unit test for method role_yaml_parse of class RoleRequirement
    """

# Generated at 2022-06-13 09:04:49.561969
# Unit test for method role_yaml_parse of class RoleRequirement

# Generated at 2022-06-13 09:04:59.397558
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    # test old style:
    r = RoleRequirement.role_yaml_parse('git+https://github.com/username/repo.git,v1.0')
    assert r == {'name': 'repo', 'scm': 'git', 'src': 'https://github.com/username/repo.git', 'version': 'v1.0'}

    # test old style:
    r = RoleRequirement.role_yaml_parse('https://github.com/username/repo,v1.0')
    assert r == {'name': 'repo', 'scm': None, 'src': 'https://github.com/username/repo', 'version': 'v1.0'}

    # test old style with an invalid role line.

# Generated at 2022-06-13 09:05:10.271430
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    from ansible.utils.role_builder import RoleBuilder

    builder = RoleBuilder("test", "test_RoleRequirement_role_yaml_parse")
    builder.set_metadata("test_RoleRequirement_role_yaml_parse.yml")

    role_yaml_dict = builder.role_metadata.role_yaml_parse("role_name,version,name")
    assert role_yaml_dict['name'] == 'role_name'
    assert role_yaml_dict['src'] == 'role_name'
    assert role_yaml_dict['version'] == 'version'

    role_yaml_dict = builder.role_metadata.role_yaml_parse("scm+src,version,name")
    assert role_yaml_dict['name'] == 'name'

# Generated at 2022-06-13 09:05:14.890109
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    repo_url = "https://git.openstack.org/openstack/ansible-hardening.git"
    assert RoleRequirement.repo_url_to_role_name(repo_url) == 'ansible-hardening'


# Generated at 2022-06-13 09:05:22.756383
# Unit test for method role_yaml_parse of class RoleRequirement

# Generated at 2022-06-13 09:05:31.531225
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name('git+git@github.com:geerlingguy/ansible-role-apache.git') == 'ansible-role-apache'
    assert RoleRequirement.repo_url_to_role_name('git+https://github.com/geerlingguy/ansible-role-apache.git') == 'ansible-role-apache'
    assert RoleRequirement.repo_url_to_role_name('git+git@github.com:geerlingguy/ansible-role-apache.git,1.0.0') == 'ansible-role-apache'

# Generated at 2022-06-13 09:05:37.553103
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    # git@github.com:ansible/test.git => test
    assert RoleRequirement.repo_url_to_role_name('git@github.com:ansible/test.git') == 'test'

    # http://github.com/ansible/test.git => test
    assert RoleRequirement.repo_url_to_role_name('http://github.com/ansible/test.git') == 'test'

    # github.com/ansible/test.git => test
    assert RoleRequirement.repo_url_to_role_name('github.com/ansible/test.git') == 'test'

    # github.com/ansible/test.git/ => test

# Generated at 2022-06-13 09:05:49.120491
# Unit test for method repo_url_to_role_name of class RoleRequirement

# Generated at 2022-06-13 09:06:02.851470
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():

    # Test git repo URL's
    assert RoleRequirement.repo_url_to_role_name("http://example.org/roles/example.git") == "example"
    assert RoleRequirement.repo_url_to_role_name("git@example.org:roles/example.git") == "example"
    assert RoleRequirement.repo_url_to_role_name("https://github.com/ansible/ansible-examples.git") == "ansible-examples"
    assert RoleRequirement.repo_url_to_role_name("git://github.com/ansible/ansible-examples.git") == "ansible-examples"

    # Test tarball URL's

# Generated at 2022-06-13 09:06:10.426186
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    assert RoleRequirement.role_yaml_parse('/tmp/foo/bar') == {'name': 'bar', 'scm': None, 'src': '/tmp/foo/bar', 'version': None}
    assert RoleRequirement.role_yaml_parse('git+https://redacted:x-oauth-basic@github.com/ansible/ansible.git') == {'name': 'ansible', 'scm': 'git', 'src': 'https://redacted:x-oauth-basic@github.com/ansible/ansible.git', 'version': None}

# Generated at 2022-06-13 09:06:25.027867
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name('foo') == 'foo'
    assert RoleRequirement.repo_url_to_role_name('git+git://github.com/foo/bar.git') == 'bar'
    assert RoleRequirement.repo_url_to_role_name('git+git://github.com/foo/bar,v2.3') == 'bar'
    assert RoleRequirement.repo_url_to_role_name('http://github.com/foo/bar.git') == 'bar'
    # test url with username
    assert RoleRequirement.repo_url_to_role_name('https://foo@vault.example.com/baz.git') == 'baz'
    # test with an argument that is the wrong type

# Generated at 2022-06-13 09:06:38.995308
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    """
    Format of repo URL:
    (1) Git: git@git.example.com:repos/repo.git
    (2) Hg: http://git.example.com/repos/repo
    (3) Svn: https://git.example.com/repos/repo
    (4) Other: https://git.example.com/repos/repo.tar.gz

    RoleRequirement.repo_url_to_role_name returns the "short name" of the role
    repo_url_to_role_name(...) should return "repo" given the above repo URLs
    """


# Generated at 2022-06-13 09:06:50.685655
# Unit test for method repo_url_to_role_name of class RoleRequirement

# Generated at 2022-06-13 09:06:53.304829
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name("https://github.com/ansible/ansible-examples.git") \
        == "ansible-examples"

# Generated at 2022-06-13 09:07:04.855025
# Unit test for method role_yaml_parse of class RoleRequirement

# Generated at 2022-06-13 09:07:15.637528
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    # Test 1: name, src and scm from string
    test1_role = dict(role="git+https://github.com/lucee/lucee-ansible-role.git,2.9.6")
    test1_correct_result = dict(scm='git', src='https://github.com/lucee/lucee-ansible-role.git',
                                    version='2.9.6', name='lucee-ansible-role')
    test1_result = RoleRequirement.role_yaml_parse(test1_role)
    assert test1_result == test1_correct_result, "Test1 failed: role_name %s != %s" % \
                                                  (test1_result, test1_correct_result)

    # Test 2: name, src and scm from dict

# Generated at 2022-06-13 09:07:20.678142
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    display.verbosity = 4

    def assert_values(line_input, expected_dict):
        r = RoleRequirement()
        actual_dict = r.role_yaml_parse(line_input)
        assert (actual_dict == expected_dict), "Expected '%s' but got '%s'" % (expected_dict, actual_dict)



# Generated at 2022-06-13 09:07:31.705899
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    rr = RoleRequirement()

    # Given a string in YAML, parse it in role YAML format
    role = dict(name = 'test-role', src = 'http://example.com/test-role.git', scm = 'git', version = '0.1.1')

    # String in YAML
    role_str = 'src=http://example.com/test-role.git,version=0.1.1,scm=git,name=test-role'

    assert(role == rr.role_yaml_parse(role_str))

    # Given a JSON in YAML, parse it in role YAML format

# Generated at 2022-06-13 09:07:41.378781
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo.git,v0.0.1') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('repo') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('repo,v0.0.1') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('repo,v0.0.1,foobar') == 'repo'


# Generated at 2022-06-13 09:07:43.124114
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    repo_url = "http://git.example.com/repos/repo.git"
    print(RoleRequirement.repo_url_to_role_name(repo_url))


# Generated at 2022-06-13 09:07:58.414318
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    assert RoleRequirement.role_yaml_parse("role_name") == dict(name="role_name", src=None)
    assert RoleRequirement.role_yaml_parse("role_name,1.2.3") == dict(name="role_name", version="1.2.3", src=None)
    assert RoleRequirement.role_yaml_parse("role_name,1.2.3,fork") == dict(name="fork", version="1.2.3", src=None)
    assert RoleRequirement.role_yaml_parse("git+https://github.com/user/repo,v1.2.3") == dict(name=None, version="v1.2.3", src="https://github.com/user/repo", scm="git")
    assert RoleRequirement.role_yaml

# Generated at 2022-06-13 09:08:09.632420
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    test_role = "my.org,development,cool_role"
    expected_dict = {"name": "cool_role", "src": "my.org", "version": "development"}
    actual_dict = RoleRequirement.role_yaml_parse(test_role)
    assert actual_dict == expected_dict

    test_role = "my.org,development"
    expected_dict = {"name": "my.org", "src": "my.org", "version": "development"}
    actual_dict = RoleRequirement.role_yaml_parse(test_role)
    assert actual_dict == expected_dict

    test_role = "my.org"
    expected_dict = {"name": "my.org", "src": "my.org"}

# Generated at 2022-06-13 09:08:16.867825
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    from ansible.playbook.role.requirement import RoleRequirement

    def verify_dict(role_name, d):
        assert d['name'] == role_name
        assert 'scm' not in d
        assert 'src' not in d
        assert d['version'] == None

    verify_dict('simple_role', RoleRequirement.role_yaml_parse('simple_role'))

    def verify_dict2(role_name, src, d):
        assert d['name'] == role_name
        assert 'scm' not in d
        assert d['src'] == src
        assert d['version'] == None


# Generated at 2022-06-13 09:08:21.925919
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    assert RoleRequirement.role_yaml_parse("foobar") == {'name': 'foobar', 'scm': None, 'src': 'foobar', 'version': None}
    assert RoleRequirement.role_yaml_parse("foobar,1.2.3") == {'name': 'foobar', 'scm': None, 'src': 'foobar', 'version': '1.2.3'}
    assert RoleRequirement.role_yaml_parse("foobar,1.2.3,baz") == {'name': 'baz', 'scm': None, 'src': 'foobar', 'version': '1.2.3'}

# Generated at 2022-06-13 09:08:27.789628
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    rr = RoleRequirement()
    role = rr.role_yaml_parse('role')
    assert role == {'name': 'role', 'src': 'role', 'scm': None, 'version': None}

    role = rr.role_yaml_parse('git+git@gitlab.com:team/role.git')
    assert role == {'name': 'role', 'src': 'git@gitlab.com:team/role.git', 'scm': 'git', 'version': None}

    role = rr.role_yaml_parse('role,[branch]')
    assert role == {'name': 'role', 'src': 'role', 'scm': None, 'version': '[branch]'}


# Generated at 2022-06-13 09:08:41.271911
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    from ansible.utils.unicode import to_unicode


# Generated at 2022-06-13 09:08:51.738604
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    # Test for a valid role line
    role = 'geerlingguy.java,1.8'
    assert(RoleRequirement.role_yaml_parse(role) == {'version': '1.8', 'name': 'geerlingguy.java', 'scm': None, 'src': 'geerlingguy.java'})
    role = 'geerlingguy.java,1.8,jdk'
    assert(RoleRequirement.role_yaml_parse(role) == {'version': '1.8', 'name': 'jdk', 'scm': None, 'src': 'geerlingguy.java'})
    role = 'https://github.com/geerlingguy/ansible-role-java.git,1.8,jdk'

# Generated at 2022-06-13 09:09:03.719469
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    from ansible.module_utils._text import to_text

# Generated at 2022-06-13 09:09:10.959421
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    role_data = {'name': 'A_Testing_Role', 'scm': 'git', 'src': 'http://github.com/ansible/ansible-testing-role.git'}
    assert RoleRequirement.role_yaml_parse('http://github.com/ansible/ansible-testing-role.git') == role_data
    assert RoleRequirement.role_yaml_parse('http://github.com/ansible/ansible-testing-role.git,v9.9.9') == role_data
    assert RoleRequirement.role_yaml_parse('http://github.com/ansible/ansible-testing-role.git,v9.9.9,bar') == role_data

# Generated at 2022-06-13 09:09:19.768749
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    role_obj = RoleRequirement()
    if role_obj.repo_url_to_role_name('http://git.example.com/repos/repo.git') != 'repo':
        raise AssertionError()
    if role_obj.repo_url_to_role_name('git+git.example.com/repos/repo.git') != 'repo':
        raise AssertionError()
    if role_obj.repo_url_to_role_name('https://github.com/x/x') != 'x':
        raise AssertionError()
    if role_obj.repo_url_to_role_name(
            'https://github.com/x/x,v1.0.0') != 'https://github.com/x/x':
        raise Assertion

# Generated at 2022-06-13 09:09:39.963696
# Unit test for method role_yaml_parse of class RoleRequirement

# Generated at 2022-06-13 09:09:51.765702
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    role_requirement = RoleRequirement()
    assert role_requirement.repo_url_to_role_name('http://git.example.com/repos/repo.git') == 'repo'
    assert role_requirement.repo_url_to_role_name('http://git.example.com/repos/repo,v1.0.0.tar.gz') == 'repo'
    assert role_requirement.repo_url_to_role_name('repo,v1.0.0,package_name') == 'repo'
    assert role_requirement.repo_url_to_role_name('https://github.com/org/repo.git,v1.0.0,package_name') == 'repo'
    assert role_requirement.repo_url_to

# Generated at 2022-06-13 09:10:01.515596
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    role_requirement = RoleRequirement()
    assert role_requirement.repo_url_to_role_name("http://git.example.com/repos/repo.git") == "repo"
    assert role_requirement.repo_url_to_role_name("http://git.example.com/repos/repo.tar.gz") == "repo"
    assert role_requirement.repo_url_to_role_name("http://git.example.com/repos/repo,1.0") == "repo"
    assert role_requirement.repo_url_to_role_name("http://git.example.com/repos/repo,1.0,foobar") == "repo"

# Generated at 2022-06-13 09:10:11.113949
# Unit test for method role_yaml_parse of class RoleRequirement

# Generated at 2022-06-13 09:10:24.466964
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    role_requirement = RoleRequirement()

# Generated at 2022-06-13 09:10:35.787560
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    """
    Method role_yaml_parse of class RoleRequirement should handle all requirements
    specified in meta/main.yml and requirements.yml files.
    """
    rr = RoleRequirement()
    assert rr.role_yaml_parse('role1') == {'name': 'role1', 'scm': None, 'src': 'role1', 'version': ''}
    assert rr.role_yaml_parse('role1,v2') == {'name': 'role1', 'scm': None, 'src': 'role1', 'version': 'v2'}
    assert rr.role_yaml_parse('role4, v3,role4') == {'name': 'role4', 'scm': None, 'src': 'role4', 'version': 'v3'}

# Generated at 2022-06-13 09:10:47.538106
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    role_requirement = RoleRequirement
    assert role_requirement.role_yaml_parse('geerlingguy.apache') == {'src': 'geerlingguy.apache', 'name': 'geerlingguy.apache', 'version': None, 'scm': None}
    assert role_requirement.role_yaml_parse('geerlingguy.apache,v1.0.3') == {'src': 'geerlingguy.apache', 'name': 'geerlingguy.apache', 'version': 'v1.0.3', 'scm': None}

# Generated at 2022-06-13 09:10:56.515799
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    role_requirement = RoleRequirement()
    a = role_requirement.role_yaml_parse("geerlingguy.apache")
    assert a == {'name': 'geerlingguy.apache', 'src': 'geerlingguy.apache', 'scm': None, 'version': None}
    a = role_requirement.role_yaml_parse("geerlingguy.apache,v1.8.x")
    assert a == {'name': 'geerlingguy.apache', 'src': 'geerlingguy.apache', 'scm': None, 'version': 'v1.8.x'}
    a = role_requirement.role_yaml_parse("geerlingguy.apache,v1.8.x,Apache")

# Generated at 2022-06-13 09:11:11.353344
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    print(RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo.git'), 'repo')
    print(RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo.git,v1.0'), 'repo')
    print(RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo.git,v1.0.tar.gz'), 'repo')
    print(RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo.git,v1.0.zip'), 'repo')

# Generated at 2022-06-13 09:11:20.016172
# Unit test for method repo_url_to_role_name of class RoleRequirement

# Generated at 2022-06-13 09:11:39.751843
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    assert RoleRequirement.role_yaml_parse('rolename') == dict(name='rolename', src=None, scm=None, version=None)
    assert RoleRequirement.role_yaml_parse('rolename,version') == dict(name='rolename', src=None, scm=None, version='version')
    assert RoleRequirement.role_yaml_parse('rolename,version,name') == dict(name='name', src=None, scm=None, version='version')
    assert RoleRequirement.role_yaml_parse('rolename,version,name,scm') == dict(name='name', src=None, scm='scm', version='version')


# Generated at 2022-06-13 09:11:46.685918
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    def test_role(role, expected, invalid_syntax=False):
        try:
            result = RoleRequirement.role_yaml_parse(role)
            assert result == expected, "result:%s != expected:%s" % (result, expected)
            assert invalid_syntax==False, "Invalid role line (%s). Proper format is 'role_name[,version[,name]]'" % role
        except AnsibleError:
            assert invalid_syntax
            pass

    test_role("http://server/foo.git", {'name': 'foo', 'src': 'http://server/foo.git', 'version': '', 'scm': None})

# Generated at 2022-06-13 09:12:00.412365
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    from ansible.utils.path import unfrackpath

    import os
    import tempfile


# Generated at 2022-06-13 09:12:07.554076
# Unit test for method role_yaml_parse of class RoleRequirement

# Generated at 2022-06-13 09:12:19.736026
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    assert RoleRequirement.role_yaml_parse("git+https://github.com/mivok/ansible-module-pip.git") == {
        'name': u'ansible-module-pip',
        'scm': u'git',
        'src': u'https://github.com/mivok/ansible-module-pip.git',
        'version': None,
    }

# Generated at 2022-06-13 09:12:26.234337
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    def _check_role_yaml_parse(input_str, input_dict, expected_dict):
        print("input:      %s" % (input_str))
        print("input_dict: %s" % (input_dict))
        print("expected:   %s" % (expected_dict))
        if input_dict is None:
            parsed_dict = RoleRequirement.role_yaml_parse(input_str)
        else:
            parsed_dict = RoleRequirement.role_yaml_parse(input_dict)
        assert parsed_dict == expected_dict

    # name, src and version must not be specified in the same line

# Generated at 2022-06-13 09:12:35.604005
# Unit test for method repo_url_to_role_name of class RoleRequirement