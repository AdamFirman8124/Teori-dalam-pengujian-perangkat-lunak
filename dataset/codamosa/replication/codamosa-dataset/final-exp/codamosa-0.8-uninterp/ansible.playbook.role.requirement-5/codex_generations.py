

# Generated at 2022-06-13 09:02:52.606833
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    from ansible.playbook.role.definition import _ROLE_CACHE
    test_role = "rolename,testversion,testname"
    test_role_result = {'name': 'testname', 'version': 'testversion', 'scm': None, 'src': 'rolename'}
    test_role_result_git = "git+https://github.com/rolename,testversion,testname"
    test_role_result_git_result = {'name': 'testname', 'version': 'testversion', 'scm': 'git', 'src': 'https://github.com/rolename'}
    test_role_result_tar = "https://github.com/rolename/archive/master.tar.gz,testversion,testname"

# Generated at 2022-06-13 09:02:59.490080
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    from ansible.utils.display import Display
    display = Display()

    display.verbosity = 3
    display.deprecated('This is deprecated')
    assert RoleRequirement.role_yaml_parse('foo') == \
        {'name': 'foo', 'scm': None, 'src': 'foo', 'version': None}
    assert RoleRequirement.role_yaml_parse('foo,v2') == \
        {'name': 'foo', 'scm': None, 'src': 'foo', 'version': 'v2'}
    assert RoleRequirement.role_yaml_parse('foo,v2,bob') == \
        {'name': 'bob', 'scm': None, 'src': 'foo', 'version': 'v2'}

# Generated at 2022-06-13 09:03:04.389274
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    repo_url = "https://github.com/michaelrigart/ansible-role-devtools.git"
    test = RoleRequirement.repo_url_to_role_name(repo_url)
    assert test == "ansible-role-devtools"


# Generated at 2022-06-13 09:03:15.596265
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    role_requirement = RoleRequirement()
    assert role_requirement.repo_url_to_role_name('http://git.example.com/repos/repo.git') == 'repo'
    assert role_requirement.repo_url_to_role_name('https://git.example.com/repos/repo.git') == 'repo'
    assert role_requirement.repo_url_to_role_name('http://git.example.com/repos/repo.tar.gz') == 'repo'
    assert role_requirement.repo_url_to_role_name('http://git.example.com/repos/repo') == 'repo'

# Generated at 2022-06-13 09:03:26.570249
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    test_string_1 = "src"
    test_string_2 = "name,src"
    test_string_3 = "version,src,name"
    test_hash_1 = {'src': 'src'}
    test_hash_2 = {'name': 'name', 'src': 'src'}
    test_hash_3 = {'version': 'version', 'src': 'src', 'name': 'name'}
    assert RoleRequirement.role_yaml_parse(test_string_1) == test_hash_1
    assert RoleRequirement.role_yaml_parse(test_string_2) == test_hash_2
    assert RoleRequirement.role_yaml_parse(test_string_3) == test_hash_3

# Generated at 2022-06-13 09:03:37.254251
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    role = "geerlingguy.memcached"
    output = RoleRequirement.role_yaml_parse(role)
    assert output == {'name': 'geerlingguy.memcached', 'scm': None, 'src': 'geerlingguy.memcached', 'version': None}

    role = "geerlingguy.memcached,1.2"
    output = RoleRequirement.role_yaml_parse(role)
    assert output == {'name': 'geerlingguy.memcached', 'scm': None, 'src': 'geerlingguy.memcached', 'version': '1.2'}

    role = "geerlingguy.memcached,1.2,foo"
    output = RoleRequirement.role_yaml_parse(role)

# Generated at 2022-06-13 09:03:46.634178
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    from ansible.utils.color import ANSIBLE_COLOR, stringc
    ANSIBLE_COLOR['color'] = False
    assert RoleRequirement.role_yaml_parse('foo') == {'name': 'foo', 'scm': None, 'src': 'foo', 'version': ''}
    assert RoleRequirement.role_yaml_parse('git+https://github.com/foo/bar') == {'name': 'bar', 'scm': 'git', 'src': 'https://github.com/foo/bar', 'version': ''}

# Generated at 2022-06-13 09:03:55.944786
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    dict = RoleRequirement.role_yaml_parse('git+https://github.com/geerlingguy/ansible-role-apache.git')
    assert dict['name'] == 'ansible-role-apache'
    assert dict['scm'] == 'git'
    assert dict['src'] == 'https://github.com/geerlingguy/ansible-role-apache.git'
    assert dict['version'] == ''
    dict = RoleRequirement.role_yaml_parse('git+git://git.example.com/repos/repo.git')
    assert dict['name'] == 'repo'
    assert dict['scm'] == 'git'
    assert dict['src'] == 'git://git.example.com/repos/repo.git'
    assert dict['version'] == ''
    dict = RoleRequ

# Generated at 2022-06-13 09:04:03.247183
# Unit test for method repo_url_to_role_name of class RoleRequirement

# Generated at 2022-06-13 09:04:13.035209
# Unit test for method repo_url_to_role_name of class RoleRequirement

# Generated at 2022-06-13 09:04:26.550980
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    print("###############################")
    print("##### Unit test for RoleRequirement.role_yaml_parse(...)")
    print("##### - role_yaml_parse('role_name')")
    role_1 = RoleRequirement.role_yaml_parse("role_name")
    assert role_1['name'] == 'role_name'
    print("##### - role_yaml_parse('role_name,1.1.1')")
    role_2 = RoleRequirement.role_yaml_parse("role_name,1.1.1")
    assert role_2['name'] == 'role_name'
    assert role_2['version'] == '1.1.1'
    print("##### - role_yaml_parse('role_name,1.1.1,other_name')")


# Generated at 2022-06-13 09:04:37.802089
# Unit test for method role_yaml_parse of class RoleRequirement

# Generated at 2022-06-13 09:04:40.771255
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    role = RoleRequirement()
    assert role.repo_url_to_role_name('http://github.com/awesomelib/awesome.git') == 'awesome'


# Generated at 2022-06-13 09:04:55.591395
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    assert RoleRequirement.role_yaml_parse({
        'role': 'role_name'
    }) == {
        'name': 'role_name',
        'src': 'role_name',
        'scm': None,
        'version': '',
    }

    assert RoleRequirement.role_yaml_parse({
        'role': 'role_name,version'
    }) == {
        'name': 'role_name',
        'src': 'role_name',
        'scm': None,
        'version': 'version',
    }


# Generated at 2022-06-13 09:05:02.748264
# Unit test for method role_yaml_parse of class RoleRequirement

# Generated at 2022-06-13 09:05:16.055601
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    assert RoleRequirement.role_yaml_parse("git+https://github.com/geerlingguy/ansible-role-security,1.2.0,geerlingguy.security") == {'name': 'geerlingguy.security', 'scm': 'git', 'src': 'https://github.com/geerlingguy/ansible-role-security', 'version': '1.2.0'}
    assert RoleRequirement.role_yaml_parse("galaxy.role_name,version,name") == {'name': 'name', 'scm': None, 'src': 'galaxy.role_name', 'version': 'version'}

# Generated at 2022-06-13 09:05:26.619694
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    import ansible.module_utils.common.collections as collections

    # Test valid string
    role = RoleRequirement.role_yaml_parse('geerlingguy.java,1.7')
    assert role == dict(name='geerlingguy.java', src=None, scm=None, version='1.7')

    # Test valid dict
    role = RoleRequirement.role_yaml_parse(dict(name='geerlingguy.java', src=None, scm='git', version='1.7'))
    assert role == dict(name='geerlingguy.java', src=None, scm='git', version='1.7')

    # Test invalid format

# Generated at 2022-06-13 09:05:33.739893
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/some-repo,v1.0.4") == "some-repo"
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/a-role,v1.0.4,myname") == "myname"
    assert RoleRequirement.repo_url_to_role_name("git+http://git.example.com/repos/repo.git,v1.0.4,myname") == "myname"
    assert RoleRequirement.repo_url_to_

# Generated at 2022-06-13 09:05:45.897109
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():

    # Test with valid url
    url = 'http://git.example.com/repos/repo.git'
    name = RoleRequirement.repo_url_to_role_name(url)
    assert name == 'repo'

    # Test with valid url that ends with .tar.gz
    url = 'http://git.example.com/repos/repo.tar.gz'
    name = RoleRequirement.repo_url_to_role_name(url)
    assert name == 'repo'

    # Test with valid url that ends with .git
    url = 'http://git.example.com/repos/repo.git'
    name = RoleRequirement.repo_url_to_role_name(url)
    assert name == 'repo'

# Generated at 2022-06-13 09:05:53.685613
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    def assert_role_yaml_parse(line, expected_name=None, expected_scm=None, expected_src=None, expected_version=None):
        display.vvv("Testing role line '%s'" % line)
        role = RoleRequirement.role_yaml_parse(line)
        assert role['name'] == expected_name, 'name: found %s, expecting %s' % (role['name'], expected_name)
        assert role['scm'] == expected_scm, 'scm: found %s, expecting %s' % (role['scm'], expected_scm)
        assert role['src'] == expected_src, 'src: found %s, expecting %s' % (role['src'], expected_src)

# Generated at 2022-06-13 09:06:09.155257
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    # test with urls
    assert RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('https://git.example.com/repos/repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('git@git.example.com:repos/repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('git@git.example.com:/repos/repo.git') == 'repo'

# Generated at 2022-06-13 09:06:17.341986
# Unit test for method repo_url_to_role_name of class RoleRequirement

# Generated at 2022-06-13 09:06:26.169966
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    tests = (
        ('http://git.example.com/repos/repo.git', 'repo'),
        ('git@git.example.com:repos/repo.git', 'repo'),
        ('git@git.example.com:/repos/repo.git', 'repo'),
        ('git@git.example.com:repos/repo', 'repo'),
        ('git@git.example.com:/repos/repo', 'repo'),
        ('/repos/repo', 'repo'),
        ('repos/repo', 'repo'),
        ('repo', 'repo'),
    )
    for (test, result) in tests:
        assert RoleRequirement.repo_url_to_role_name(test) == result


# Generated at 2022-06-13 09:06:39.760367
# Unit test for method role_yaml_parse of class RoleRequirement

# Generated at 2022-06-13 09:06:51.329705
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    from ansible.playbook.role.requirement import RoleRequirement
    assert RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('https://github.com/geerlingguy/ansible-role-apache.git') == 'ansible-role-apache'
    assert RoleRequirement.repo_url_to_role_name('https://github.com/myorg/ansible-role-foobar,release-100') == 'ansible-role-foobar'

# Generated at 2022-06-13 09:07:02.459616
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    # Input data
    # (#1)
    role = 'src-role, v1.0.0, role'
    # (#2)
    role2 = 'src-role, v1.0.0'
    # (#3)
    role3 = 'src-role,role'
    # (#4)
    role4 = 'src-role'
    # (#5)
    role5 = 'src-role, v1.0.0, role, v1.0.0'
    # (#6)
    role6 = 'git+https://git.site.com/repo.git'
    # (#7)
    role7 = 'https://git.site.com/repo.git'
    # (#8)
    role8 = {'role': 'role, v1.0.0'}
    # (#

# Generated at 2022-06-13 09:07:11.304388
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    req = RoleRequirement()
    assert req.repo_url_to_role_name('https://github.com/user/role.git') == 'role'
    assert req.repo_url_to_role_name('https://github.com/user/role') == 'role'
    assert req.repo_url_to_role_name('https://github.com/user/role.git,') == 'role'
    assert req.repo_url_to_role_name('https://github.com/user/role,') == 'role'
    assert req.repo_url_to_role_name('https://github.com/user/role.tar.gz') == 'role'

# Generated at 2022-06-13 09:07:19.623614
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    assert RoleRequirement.role_yaml_parse('test') == {'name': 'test', 'src': 'test', 'scm': None, 'version': ''}
    assert RoleRequirement.role_yaml_parse('test,') == {'name': 'test', 'src': 'test', 'scm': None, 'version': ''}
    assert RoleRequirement.role_yaml_parse('test,1.0') == {'name': 'test', 'src': 'test', 'scm': None, 'version': '1.0'}
    assert RoleRequirement.role_yaml_parse('test,1.0,') == {'name': 'test', 'src': 'test', 'scm': None, 'version': '1.0'}

# Generated at 2022-06-13 09:07:30.851139
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    # Test 1
    # ------
    tests_list = [
        "name",
        "name,version",
        "name,version,name",
        "scm+https://www.google.com/x,refs=1,name"
    ]
    for test_string in tests_list:
        role = RoleRequirement.role_yaml_parse(test_string)
        assert role["name"] == "name"

    # Test 2
    # ------
    test_dict_list = [
        {"role": "name"},
        {"role": "name,version"},
        {"role": "name,version,name"},
        {"role": "scm+https://www.google.com/x,refs=1,name"}
    ]
    for test_dict in test_dict_list:
        role = RoleRequ

# Generated at 2022-06-13 09:07:41.054293
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name('https://github.com/user/role.git') == 'role'
    assert RoleRequirement.repo_url_to_role_name('git@github.com:user/role.git') == 'role'
    assert RoleRequirement.repo_url_to_role_name('https://github.com/user/role.git,v1.0') == 'role'
    assert RoleRequirement.repo_url_to_role_name('https://github.com/user/role.git,v1.0,name') == 'role'
    assert RoleRequirement.repo_url_to_role_name('https://github.com/user/role.git,v1.0,name,someother') == 'role'


# Generated at 2022-06-13 09:07:56.471288
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    
    assert(RoleRequirement.repo_url_to_role_name("git://git.example.com/repos/repo.git") == "repo")
    assert(RoleRequirement.repo_url_to_role_name("git@git.example.com:repos/repo.git") == "repo")
    assert(RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.git") == "repo")
    assert(RoleRequirement.repo_url_to_role_name("https://git.example.com/repos/repo.git") == "repo")

# Generated at 2022-06-13 09:08:09.076777
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    print('Testing RoleRequirement.role_yaml_parse')

    import sys
    from textwrap import dedent
    from six import PY3

    class TestException(Exception):
        pass

    def _test(test_case):
        try:
            result = RoleRequirement.role_yaml_parse(test_case[0])
        except TestException as e:
            if test_case[1]:
                raise
            if PY3:
                if str(e) == test_case[2]:
                    return
            else:
                if unicode(e) == test_case[2]:
                    return

# Generated at 2022-06-13 09:08:16.523199
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    def _role_yaml_parse_test(input, expected):
        result = RoleRequirement.role_yaml_parse(input)
        assert result == expected, \
            "Expected result: %s, but got %s" % (expected, result)
        # print("Expected result: %s, but got %s" % (expected, result))

    # test string inputs
    _role_yaml_parse_test(input="git+https://github.com/geerlingguy/ansible-role-jenkins.git,v1.0",
                          expected=dict(name="ansible-role-jenkins", src="https://github.com/geerlingguy/ansible-role-jenkins.git", scm="git", version="v1.0"))


# Generated at 2022-06-13 09:08:22.667068
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    # test parsing dict
    result = RoleRequirement.role_yaml_parse({'role': 'some-role'})
    assert result == {'name': 'some-role'}

    # test parsing dict with some options
    result = RoleRequirement.role_yaml_parse({
        'role': 'some-role',
        'src': 'some-src',
        'version': 'some-version',
        'scm': 'some-scm',
        'foo': 'some-foo',
        'bar': 'some-bar'
    })
    assert result == {
        'name': 'some-role',
        'src': 'some-src',
        'version': 'some-version',
        'scm': 'some-scm',
    }

    # test parsing string
    result = RoleRequirement.role

# Generated at 2022-06-13 09:08:36.626664
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    import os.path
    import pytest
    # test git url
    assert RoleRequirement.repo_url_to_role_name("git://example.com/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("ssh://example.com/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("https://example.com/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("git@example.com:repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("git@example.com:/repo.git") == "repo"
    assert RoleRequirement.repo_url_to

# Generated at 2022-06-13 09:08:49.118920
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo.tar.gz') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('https://github.com/ansible/ansible-examples.git,v2.0') == 'ansible-examples'
    assert RoleRequirement.repo_url_to_role_name('git+https://github.com/ansible/ansible-examples.git,v2.0') == 'ansible-examples'

# Generated at 2022-06-13 09:08:58.290057
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name('https://github.com/ansible/ansible-examples.git') == 'ansible-examples'
    assert RoleRequirement.repo_url_to_role_name('https://github.com/ansible/ansible-examples.git,v1.0') == 'ansible-examples'
    assert RoleRequirement.repo_url_to_role_name('https://github.com/ansible/ansible-examples.git,v1.0,myrole') == 'ansible-examples'


# Generated at 2022-06-13 09:09:08.275929
# Unit test for method repo_url_to_role_name of class RoleRequirement

# Generated at 2022-06-13 09:09:18.385131
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    # Test case for positive and negative scenario for method RoleRequirement.role_yaml_parse
    # Positive and negative scenario for method RoleRequirement.role_yaml_parse

    # Positive scenario for method RoleRequirement.role_yaml_parse
    test_one_output = RoleRequirement.role_yaml_parse('galaxy.role_name')
    if test_one_output == {'name': 'role_name', 'src': 'galaxy.role_name', 'scm': None, 'version': ''}:
        test_one_result = 'PASSED'
    else:
        test_one_result = 'FAILED'
    print('Test one scenario one is %s' % test_one_result)


# Generated at 2022-06-13 09:09:32.504278
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    def check_role(str_input, expected_output):
        assert RoleRequirement.role_yaml_parse(str_input) == expected_output, "role_yaml_parse works as expected for '%s'" % str_input

    check_role('', {'name': None, 'src': None, 'scm': None, 'version': None})
    check_role('a.b', {'name': 'a.b', 'src': 'a.b', 'scm': None, 'version': None})
    check_role('http://git.example.com/repos/repo.git', {'name': 'repo', 'src': 'http://git.example.com/repos/repo.git', 'scm': None, 'version': None})

# Generated at 2022-06-13 09:09:59.456227
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    assert RoleRequirement.role_yaml_parse("geerlingguy.java") == {
        'scm': None,
        'src': 'geerlingguy.java',
        'version': None,
        'name': 'geerlingguy.java',
    }
    assert RoleRequirement.role_yaml_parse("geerlingguy.java,1.6") == {
        'scm': None,
        'src': 'geerlingguy.java',
        'version': '1.6',
        'name': 'geerlingguy.java',
    }

# Generated at 2022-06-13 09:10:07.195480
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    def t(role, expected):
        result = RoleRequirement.role_yaml_parse(role)
        assert result == expected, "not equal: result=%s != %s=expected" % (result, expected)

    t("geerlingguy.jenkins", dict(name="geerlingguy.jenkins", src="geerlingguy.jenkins", scm=None, version=''))
    t("geerlingguy.jenkins,1.0.1", dict(name="geerlingguy.jenkins", src="geerlingguy.jenkins", scm=None, version='1.0.1'))
    t("geerlingguy.jenkins,1.0.1,foo", dict(name="foo", src="geerlingguy.jenkins", scm=None, version='1.0.1'))

# Generated at 2022-06-13 09:10:21.731548
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    result = RoleRequirement.role_yaml_parse("geerlingguy.test")
    assert result == {'name': 'test', 'scm': None, 'src': 'geerlingguy.test', 'version': None}
    result = RoleRequirement.role_yaml_parse("git+https://github.com/geerlingguy/ansible-role-test.git")
    assert result == {'name': 'test', 'scm': 'git', 'src': 'https://github.com/geerlingguy/ansible-role-test.git', 'version': None}
    result = RoleRequirement.role_yaml_parse("git+https://github.com/geerlingguy/ansible-role-test.git,v1.0")

# Generated at 2022-06-13 09:10:33.343980
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    from ansible.errors import AnsibleError

    # test no errors
    name = "name"
    src = "src"
    scm = "scm"
    version = "version"
    role = dict(name=name, src=src, scm=scm, version=version)
    result = RoleRequirement.role_yaml_parse(role)
    assert result == role

    # test src
    src = "src"
    role = src
    result = RoleRequirement.role_yaml_parse(role)
    assert result == dict(name=src, src=src, scm=None, version=None)

    src = "src,version,name"
    role = src
    result = RoleRequirement.role_yaml_parse(role)

# Generated at 2022-06-13 09:10:44.503022
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    # Test 1: An invalid line should raise an exception
    invalid_line = 'role,git+https://github.com/mode/roles/tree/devel,1.0.0'
    try:
        RoleRequirement.role_yaml_parse(invalid_line)
    except AnsibleError as e:
        print('Test 1: Invalid role spec: ' + str(e))

    # Test 2: A valid role in string should be translated to dict
    valid_role_line = 'git+https://github.com/mode/roles/tree/devel,master,role'
    valid_role_dict = RoleRequirement.role_yaml_parse(valid_role_line)

# Generated at 2022-06-13 09:10:52.744019
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    role = RoleRequirement()
    assert role.repo_url_to_role_name('http://git.example.com/repos/repo.git') == 'repo'
    assert role.repo_url_to_role_name('git@git.example.com/repos/repo.git') == 'repo'
    assert role.repo_url_to_role_name('https://git.example.com/repos/repo.git') == 'repo'
    assert role.repo_url_to_role_name('https://git.example.com/repos/test_repo.git') == 'test_repo'
    assert role.repo_url_to_role_name('https://git.example.com/repos/repo.tar.gz') == 'repo'


# Generated at 2022-06-13 09:11:03.263417
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name('a') == 'a'
    assert RoleRequirement.repo_url_to_role_name('a,0.0.1') == 'a'
    assert RoleRequirement.repo_url_to_role_name('a,0.0.1,b') == 'a'
    assert RoleRequirement.repo_url_to_role_name('a/b') == 'b'
    assert RoleRequirement.repo_url_to_role_name('a/b,0.0.1') == 'b'
    assert RoleRequirement.repo_url_to_role_name('a/b,0.0.1,c') == 'b'

# Generated at 2022-06-13 09:11:07.532055
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name('https://github.com/paulosuzart/ansible-role-google-compute-engine-docker-host.git') == 'ansible-role-google-compute-engine-docker-host'


# Generated at 2022-06-13 09:11:16.472958
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert 'role' == RoleRequirement.repo_url_to_role_name('git@git.example.com:role.git')
    assert 'role' == RoleRequirement.repo_url_to_role_name('git@git.example.com:role')
    assert 'role' == RoleRequirement.repo_url_to_role_name('http://git.example.com:role')
    assert 'role' == RoleRequirement.repo_url_to_role_name('https://git.example.com/role')
    assert 'role' == RoleRequirement.repo_url_to_role_name('https://git.example.com/role.git')
    assert 'role' == RoleRequirement.repo_url_to_role_name('https://git.example.com/role.tar.gz')

# Generated at 2022-06-13 09:11:25.086700
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo.tar.gz') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('git@github.com:user/repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo.git,1.1') == 'repo'

# Generated at 2022-06-13 09:11:57.906155
# Unit test for method role_yaml_parse of class RoleRequirement

# Generated at 2022-06-13 09:12:06.165905
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    def run_test(role, expect):
        res = RoleRequirement.role_yaml_parse(role)
        assert res == expect

    # Test with different git repositories
    run_test('https://github.com/galaxyproject/ansible-role-sysctl.git',
             {'name': 'ansible-role-sysctl', 'src': 'https://github.com/galaxyproject/ansible-role-sysctl.git', 'scm': 'git', 'version': None})

# Generated at 2022-06-13 09:12:11.410981
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name("git@github.com:jimi-c/ansible-test-role.git") == "ansible-test-role"
    assert RoleRequirement.repo_url_to_role_name("git@github.com:jimi-c/ansible-test-role") == "ansible-test-role"
    assert RoleRequirement.repo_url_to_role_name("https://github.com/jimi-c/ansible-test-role") == "ansible-test-role"
    assert RoleRequirement.repo_url_to_role_name("https://github.com/jimi-c/ansible-test-role.git") == "ansible-test-role"
    assert RoleRequirement.repo_url_to_role_

# Generated at 2022-06-13 09:12:21.268799
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    # test with new style requirements
    obj = RoleRequirement.role_yaml_parse({'src': 'my_galaxy_role', 'path': '/my/roles/my_galaxy_role'})
    assert obj == {'name': 'my_galaxy_role', 'src': 'my_galaxy_role', 'scm': None, 'version': ''}
    obj = RoleRequirement.role_yaml_parse({'src': 'my_galaxy_role,v2', 'path': '/my/roles/my_galaxy_role'})
    assert obj == {'name': 'my_galaxy_role', 'src': 'my_galaxy_role', 'scm': None, 'version': 'v2'}

    # test with old style requirements
    obj = RoleRequirement.role_yaml_parse

# Generated at 2022-06-13 09:12:27.586310
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    # In this test we check if parsing is done correctly.

    # Test case: The role is specified in old style.
    #            src = role, version = None and name = None
    role = {'role': 'apache'}
    output = RoleRequirement.role_yaml_parse(role)
    assert isinstance(output, dict)
    assert output['version'] == ''
    assert output['src'] == 'apache'
    assert output['name'] == 'apache'
    assert 'scm' not in output

    # Test case: The role is specified in old style.
    #            src = role, version = version and name = None
    role = {'role': 'apache,1.0'}
    output = RoleRequirement.role_yaml_parse(role)
    assert isinstance(output, dict)

# Generated at 2022-06-13 09:12:36.360350
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    repo_url = 'git://git.example.com/ansible.git'
    assert 'ansible' == RoleRequirement.repo_url_to_role_name(repo_url)
    repo_url = 'git@git.example.com:ansible.git'
    assert 'ansible' == RoleRequirement.repo_url_to_role_name(repo_url)
    repo_url = 'git@git.example.com:ansible/foobar.git'
    assert 'foobar' == RoleRequirement.repo_url_to_role_name(repo_url)
    repo_url = '/usr/local/src/ansible.git'
    assert 'ansible' == RoleRequirement.repo_url_to_role_name(repo_url)