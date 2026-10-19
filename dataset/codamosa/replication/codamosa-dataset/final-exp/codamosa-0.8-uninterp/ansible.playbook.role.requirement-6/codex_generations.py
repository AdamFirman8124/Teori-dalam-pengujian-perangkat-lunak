

# Generated at 2022-06-13 09:03:02.481581
# Unit test for method repo_url_to_role_name of class RoleRequirement

# Generated at 2022-06-13 09:03:13.160715
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    rr = RoleRequirement()

    # Test that a string is parsed properly
    test1 = rr.role_yaml_parse("foo,bar,baz")
    assert test1['name'] == "baz"
    assert test1['src'] == "foo"
    assert test1['version'] == "bar"

    # Test that an old style line is parsed properly, with a branch
    test2 = rr.role_yaml_parse("my_role,")
    assert test2['name'] == "my_role"
    assert test2['src'] == None
    assert test2['version'] == ''

    # Test that an old style line is parsed properly, without a branch
    test3 = rr.role_yaml_parse("my_role")
    assert test3['name'] == "my_role"

# Generated at 2022-06-13 09:03:22.227167
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    # Setup
    data = { 'role': 'role' }
    role = RoleRequirement.role_yaml_parse(data)
    assert role['name'] == 'role'

    # Setup
    data = { 'role': 'role,v1,name' }
    role = RoleRequirement.role_yaml_parse(data)
    assert role['name'] == 'name'

    # Setup
    data = { 'role': 'role,v1,name-with-dashes' }
    role = RoleRequirement.role_yaml_parse(data)
    assert role['name'] == 'name-with-dashes'

    # Setup
    data = { 'role': 'https://github.com/user/repo.git' }
    role = RoleRequirement.role_yaml_parse(data)
    assert role

# Generated at 2022-06-13 09:03:31.818758
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    # Test for strings
    role_name = 'foo'
    assert RoleRequirement.role_yaml_parse(role_name) == {'name': 'foo', 'src': 'foo', 'scm': None, 'version': None}

    role_name_with_version = 'foo,bar'
    assert RoleRequirement.role_yaml_parse(role_name_with_version) == {'name': 'foo', 'src': 'foo', 'scm': None, 'version': 'bar'}

    role_name_with_version_and_name = 'foo,bar,baz'
    assert RoleRequirement.role_yaml_parse(role_name_with_version_and_name) == {'name': 'baz', 'src': 'foo', 'scm': None, 'version': 'bar'}

   

# Generated at 2022-06-13 09:03:43.128866
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():

    assert(RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.git") == "repo")
    assert(RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.git,v1") == "repo")
    assert(RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.git,v1,name") == "repo")
    assert(RoleRequirement.repo_url_to_role_name("https://github.com/example/repo.git") == "repo")
    assert(RoleRequirement.repo_url_to_role_name("repo") == "repo")

# Generated at 2022-06-13 09:03:53.844094
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    # If the first argument is a string
    # Input value: "src,version,name"
    # Output value: dict(name='name', src='src', scm=None, version='version')
    test_value = RoleRequirement.role_yaml_parse('src,version,name')
    assert test_value['name'] == 'name'
    assert test_value['src'] == 'src'
    assert test_value['scm'] is None
    assert test_value['version'] == 'version'

    # If the first argument is a string
    # Input value: "src"
    # Output value: dict(name=None, src='src', scm=None, version=None)
    test_value = RoleRequirement.role_yaml_parse('src')
    assert test_value['name'] is None
    assert test

# Generated at 2022-06-13 09:04:08.544052
# Unit test for method role_yaml_parse of class RoleRequirement

# Generated at 2022-06-13 09:04:16.829437
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    assert RoleRequirement.role_yaml_parse("myorg.myrole") == {'name': 'myorg.myrole', 'scm': None, 'src': 'myorg.myrole', 'version': None}
    assert RoleRequirement.role_yaml_parse("https://github.com/myorg/myrole") == {'name': 'myorg.myrole', 'scm': 'git', 'src': 'https://github.com/myorg/myrole', 'version': None}
    assert RoleRequirement.role_yaml_parse("https://github.com/myorg/myrole,v2") == {'name': 'myorg.myrole', 'scm': 'git', 'src': 'https://github.com/myorg/myrole', 'version': 'v2'}
    assert RoleRequirement.role_

# Generated at 2022-06-13 09:04:25.705901
# Unit test for method repo_url_to_role_name of class RoleRequirement

# Generated at 2022-06-13 09:04:37.127911
# Unit test for method repo_url_to_role_name of class RoleRequirement

# Generated at 2022-06-13 09:04:59.620085
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("git+git@git.example.com:repos/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("https://github.com/ansible/ansible-examples.git") == "ansible-examples"
    assert RoleRequirement.repo_url_to_role_name("https://github.com/ansible/ansible-examples/releases/download/v0.2/ansible-examples-0.2.tar.gz") == "ansible-examples"
    assert RoleRequirement.repo_url_

# Generated at 2022-06-13 09:05:13.295859
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    print('---')
    print('test_RoleRequirement_repo_url_to_role_name method of RoleRequirement class')
    print('---')
    test_role_string_1 = 'http://git.example.com/repos/repo.git'
    test_role_string_2 = 'git://git.example.com/repos/repo.git,v2.0'
    test_role_string_3 = 'git+git://git.example.com/repos/repo.git'
    test_role_string_4 = 'https://github.com/ansible/ansible-modules-extras.git'
    test_role_string_5 = 'https://github.com/ansible/ansible-modules-extras.git,v2.1'
    test_role_string_

# Generated at 2022-06-13 09:05:22.758235
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    # returns the role name out of a repo like
    # http://git.example.com/repos/repo.git" => "repo"
    url = "http://git.example.com/repos/repo.git"
    role_name = RoleRequirement.repo_url_to_role_name(url)
    assert role_name == "repo"

    # returns the role name out of a repo like
    # http://git.example.com/repos/repo.git" => "repo"
    url = "git@git.example.com:repos/repo.git"
    role_name = RoleRequirement.repo_url_to_role_name(url)
    assert role_name == "repo"


# Generated at 2022-06-13 09:05:31.530249
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name("http://github.com/geerlingguy/ansible-role-apache") == 'ansible-role-apache'
    assert RoleRequirement.repo_url_to_role_name("https://github.com/geerlingguy/ansible-role-apache") == 'ansible-role-apache'
    assert RoleRequirement.repo_url_to_role_name("https://github.com/geerlingguy/ansible-role-apache.git") == 'ansible-role-apache'
    assert RoleRequirement.repo_url_to_role_name("http://github.com/geerlingguy/ansible-role-apache.git") == 'ansible-role-apache'
    assert RoleRequirement.repo_url_to_role_

# Generated at 2022-06-13 09:05:41.511903
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():

    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.tar.gz") == "repo"
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/other,repo.tar.gz") == "other"
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo") == "repo"

# Generated at 2022-06-13 09:05:51.683301
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    # Test "name" key
    role_req = 'role: role1'
    role_dict = RoleRequirement.role_yaml_parse(role_req)
    assert len(role_dict) == 1 and 'name' in role_dict.keys() and role_dict['name'] == 'role1'

    # Test "name" and "version" keys
    role_req = 'role1,1.0.0'
    role_dict = RoleRequirement.role_yaml_parse(role_req)
    assert role_dict['name'] == 'role1' and role_dict['version'] == '1.0.0'

    # Test "name", "version" and "src" keys
    role_req = 'role1,1.0.0,https://github.com/role1'
    role_dict = Role

# Generated at 2022-06-13 09:06:04.846830
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('git@git.example.com:repos/repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo.git,v2.0') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('git@git.example.com:repos/repo.git,v2.0') == 'repo'

# Generated at 2022-06-13 09:06:14.064200
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert('foo_bar' == RoleRequirement.repo_url_to_role_name("git@git.example.com:repos/foo_bar.git"))
    assert('foo_bar' == RoleRequirement.repo_url_to_role_name("https://github.com/foo/bar"))
    assert('foo_bar' == RoleRequirement.repo_url_to_role_name("https://github.com/foo/bar.git"))
    assert('foo_bar  ' == RoleRequirement.repo_url_to_role_name("https://github.com/foo/bar.git "))
    assert('foo_bar  ' == RoleRequirement.repo_url_to_role_name("https://github.com/foo/bar.git  "))

# Generated at 2022-06-13 09:06:22.770915
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    # Old style: 'galaxy.role,version,name'
    assert RoleRequirement.role_yaml_parse('geerlingguy.apache,1.1.1,my_apache') == dict(name='my_apache', src='geerlingguy.apache', scm=None, version='1.1.1')
    assert RoleRequirement.role_yaml_parse('geerlingguy.apache') == dict(name='geerlingguy.apache', src='geerlingguy.apache', scm=None, version=None)
    assert RoleRequirement.role_yaml_parse('geerlingguy.apache,1.1.1') == dict(name='geerlingguy.apache', src='geerlingguy.apache', scm=None, version='1.1.1')

    # Old style: 'scm+

# Generated at 2022-06-13 09:06:35.604566
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name("https://github.com/user/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("https://github.com:80/user/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("https://github.com:80/user/repo.git#1.0") == "repo"
    assert RoleRequirement.repo_url_to_role_name("https://github.com/user/repo.git#1.0") == "repo"
    assert RoleRequirement.repo_url_to_role_name("https://github.com/user/repo.git,v1.1") == "repo"

# Generated at 2022-06-13 09:06:51.151516
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    role = RoleRequirement()

    # NEED TO TEST
    # 1. 'name' and 'src' and 'role' both provided
    # 2. 'name' and 'src' both provided
    # 3. 'src' and 'role' both provided
    # 4. 'name' and 'role' both provided
    # 5. 'name' provided
    # 6. 'src' provided
    # 7. 'role' provided
    # 8. None provided

    print("Test case #1")
    input_role = dict(name='geerlingguy.java', src='https://github.com/geerlingguy/ansible-role-java.git')
    validated_role = RoleRequirement.role_yaml_parse(input_role)
    assert validated_role['name'] == 'geerlingguy.java'
    assert validated_

# Generated at 2022-06-13 09:07:02.265782
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    if RoleRequirement.role_yaml_parse('geerlingguy.ntp') != {'name': 'geerlingguy.ntp', 'scm': None, 'src': 'geerlingguy.ntp', 'version': ''}:
        raise Exception('Test 1 of RoleRequirement.role_yaml_parse failed!')

    if RoleRequirement.role_yaml_parse('geerlingguy.ntp,0.2.0') != {'name': 'geerlingguy.ntp', 'scm': None, 'src': 'geerlingguy.ntp', 'version': '0.2.0'}:
        raise Exception('Test 2 of RoleRequirement.role_yaml_parse failed!')


# Generated at 2022-06-13 09:07:11.188050
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    assert RoleRequirement.role_yaml_parse("foo") == {'name': 'foo', 'src': 'foo', 'version': None, 'scm': None}
    assert RoleRequirement.role_yaml_parse("foo,bar") == {'name': 'foo', 'src': 'foo,bar', 'version': 'bar', 'scm': None}
    assert RoleRequirement.role_yaml_parse("foo,bar,baz") == {'name': 'baz', 'src': 'foo,bar,baz', 'version': 'bar', 'scm': None}

# Generated at 2022-06-13 09:07:19.307514
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    """
    Tests if role_yaml_parse matches expected output.
    """

    import json
    import yaml

    with open("../tests/lib/ansible/galaxy/meta_data_sample.yaml") as f:
        meta_data_sample = yaml.load(f)

    expected = {
        'name': 'Myappnet.myapp',
        'src': 'git+https://github.com/ansible/ansible-examples',
        'version': 'v1.0'
    }

    # I used json.dumps to get a string representation of the dict that was easier to compare
    assert json.dumps(RoleRequirement.role_yaml_parse(meta_data_sample)) == json.dumps(expected)



# Generated at 2022-06-13 09:07:30.480011
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    assert RoleRequirement.role_yaml_parse('http://git.example.com/repos/repo.git,v1.0') == {'src': 'http://git.example.com/repos/repo.git', 'version': 'v1.0', 'name': 'repo', 'scm': None}
    assert RoleRequirement.role_yaml_parse('http://git.example.com/repos/repo.git,v1.0,name') == {'src': 'http://git.example.com/repos/repo.git', 'version': 'v1.0', 'name': 'name', 'scm': None}

# Generated at 2022-06-13 09:07:40.724216
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():

    info = RoleRequirement()

    # Test with invalid arguments
    assert info.repo_url_to_role_name('') is None
    assert info.repo_url_to_role_name('http://git.example.com/repos/repo.git') == 'repo'
    assert info.repo_url_to_role_name('http://git.example.com/repos/repo.git,master') == 'repo.git'
    assert info.repo_url_to_role_name('http://git.example.com/repos/repo.git,master,acme.role') == 'repo.git'
    assert info.repo_url_to_role_name('git+http://git.example.com/repos/repo.git') == 'repo'
   

# Generated at 2022-06-13 09:07:51.720072
# Unit test for method role_yaml_parse of class RoleRequirement

# Generated at 2022-06-13 09:07:59.997231
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    result = RoleRequirement.role_yaml_parse('role_name,version,name')
    assert result['name'] == 'name'
    assert result['scm'] is None
    assert result['src'] == 'role_name'
    assert result['version'] == 'version'

    result = RoleRequirement.role_yaml_parse('scm+role_name,version,name')
    assert result['name'] == 'name'
    assert result['scm'] == 'scm'
    assert result['src'] == 'role_name'
    assert result['version'] == 'version'

    result = RoleRequirement.role_yaml_parse('https://github.com/geerlingguy/ansible-role-drupal.git,1.2.3,drupal')
    assert result['name'] == 'drupal'


# Generated at 2022-06-13 09:08:10.917040
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.git") == "repo"
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo") == "repo"
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo.tar.gz") == "repo"
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo,1.0.0") == "repo"
    assert RoleRequirement.repo_url_to_role_name("http://git.example.com/repos/repo,1.0.0,name")

# Generated at 2022-06-13 09:08:25.340867
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():

    rr = RoleRequirement()
    assert rr.repo_url_to_role_name("git@git.example.com:repos/repo.git") == "repo"
    assert rr.repo_url_to_role_name("http://git.example.com/repos/repo.git") == "repo"
    assert rr.repo_url_to_role_name("http://git.example.com/repos/repo.git,1.0") == "repo"
    assert rr.repo_url_to_role_name("http://git.example.com/repos/repo.git,1.0,roles/repo") == "roles/repo"

# Generated at 2022-06-13 09:08:46.285014
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    print("Start unit test for method role_yaml_parse of class RoleRequirement")

    # Case 1
    # Args:
    #     role = "my_role"
    # Expected:
    #     result = { 'name': 'my_role', 'src': 'my_role', 'scm': None, 'version': None }
    role = "my_role"
    result = RoleRequirement.role_yaml_parse(role)
    expect = { 'name': 'my_role', 'src': 'my_role', 'scm': None, 'version': '' }
    if result != expect:
        print("Case 1 Failed: Result: {}, Expect: {}".format(result, expect))

    # Case 2
    # Args:
    #     role = { 'src': 'my_role'}
    #

# Generated at 2022-06-13 09:08:56.873989
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    from ansible.playbook.role.requirement import RoleRequirement
    from ansible import constants as C

    src = 'https://github.com/example/example.git'
    scm = 'git'
    name = 'example'
    version = 'HEAD'
    keep_scm_meta = False

    assert RoleRequirement.role_yaml_parse(src) == dict(name=name, src=src, scm=scm, version=version)
    assert RoleRequirement.role_yaml_parse('%s,%s' % (src, version)) == dict(name=name, src=src, scm=scm, version=version)

# Generated at 2022-06-13 09:09:07.379692
# Unit test for method role_yaml_parse of class RoleRequirement

# Generated at 2022-06-13 09:09:17.927666
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    display.vvv("Testing ansible.galaxy.requirement.RoleRequirement.role_yaml_parse()")
    assert RoleRequirement.role_yaml_parse("geerlingguy.nodejs") == {'name': 'geerlingguy.nodejs', 'src': 'geerlingguy.nodejs', 'scm': None, 'version': None}
    assert RoleRequirement.role_yaml_parse("geerlingguy.nodejs,1.2") == {'name': 'geerlingguy.nodejs', 'src': 'geerlingguy.nodejs', 'scm': None, 'version': '1.2'}

# Generated at 2022-06-13 09:09:25.405502
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name('https://github.com/wayneeseguin/rvm/') == 'rvm'
    assert RoleRequirement.repo_url_to_role_name('https://github.com/wayneeseguin/rvm') == 'rvm'
    assert RoleRequirement.repo_url_to_role_name('https://github.com/wayneeseguin/rvm.git') == 'rvm'
    assert RoleRequirement.repo_url_to_role_name('https://github.com/wayneeseguin/rvm.git/') == 'rvm'
    assert RoleRequirement.repo_url_to_role_name('https://github.com/wayneeseguin/rvm,v1.0.0') == 'rvm'
   

# Generated at 2022-06-13 09:09:35.385347
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    import os
    import tempfile
    from ansible.parsing.yaml.dumper import AnsibleDumper

    # test with a string single role
    role = RoleRequirement.role_yaml_parse('geerlingguy.apache')
    assert role == dict(name='geerlingguy.apache', src='geerlingguy.apache', scm=None, version=None)

    # test with a string single role with a version
    role = RoleRequirement.role_yaml_parse('geerlingguy.apache,1.0.0')
    assert role == dict(name='geerlingguy.apache', src='geerlingguy.apache', scm=None, version='1.0.0')

    # test with a string single role with a version and a name
    role = RoleRequirement.role_yaml_

# Generated at 2022-06-13 09:09:43.207880
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    print()
    display.display("testing RoleRequirement.role_yaml_parse...")
    assert RoleRequirement.role_yaml_parse("git+https://github.com/geerlingguy/ansible-role-apache.git,v1.9.1,geerlingguy.apache") == {
        "name": "geerlingguy.apache",
        "scm": "git",
        "src": "https://github.com/geerlingguy/ansible-role-apache.git",
        "version": "v1.9.1",
    }, "Error parsing role with role name with version."

# Generated at 2022-06-13 09:09:54.780715
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    # The method repo_url_to_role_name should handle various url patterns
    url = "http://git.example.com/repos/repo.git"
    role_name = RoleRequirement.repo_url_to_role_name(url)
    assert role_name == "repo"

    url = "https://git.example.com/repos/repo.git"
    role_name = RoleRequirement.repo_url_to_role_name(url)
    assert role_name == "repo"

    url = "user@git.example.com:repos/repo.git"
    role_name = RoleRequirement.repo_url_to_role_name(url)
    assert role_name == "repo"


# Generated at 2022-06-13 09:10:03.932759
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    import string, random
    chars = string.ascii_lowercase + string.digits

    def random_string(size):
        return ''.join(random.choice(chars) for _ in range(size))

    # Test case 1: { src: 'galaxy.role,version,name', other_vars: "here" }
    test_data = {
        "src": "{0},{1}".format(random_string(5), random_string(5)),
        "name": None,
        "version": random_string(5),
        "scm": "git"
    }
    expected_data = test_data.copy()
    expected_data['src'] = "{0}+{1}".format(test_data['scm'], test_data['src'])
    result = RoleRequirement.role

# Generated at 2022-06-13 09:10:12.721431
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    ''' role_yaml_parse should parse role definition string and return a dict. '''

    # old style, which should be parsed as name and src
    assert RoleRequirement.role_yaml_parse('geerlingguy.git') == {'name': u'geerlingguy.git', 'scm': None, 'src': u'geerlingguy.git', 'version': u''}
    assert RoleRequirement.role_yaml_parse(u'geerlingguy.git') == {'name': u'geerlingguy.git', 'scm': None, 'src': u'geerlingguy.git', 'version': u''}

    # old style with version, which should be parsed as name, src and version

# Generated at 2022-06-13 09:10:38.251570
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name("git+https://github.com/someusername/somerepo") == "somerepo"
    assert RoleRequirement.repo_url_to_role_name("https://github.com/someusername/somerepo") == "somerepo"
    assert RoleRequirement.repo_url_to_role_name("git+https://someusername@github.com/someusername/somerepo.git") == "somerepo"
    assert RoleRequirement.repo_url_to_role_name("https://someusername@github.com/someusername/somerepo.git") == "somerepo"

# Generated at 2022-06-13 09:10:49.311090
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    assert RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('git+http://git.example.com/repos/repo.git') == 'repo'
    assert RoleRequirement.repo_url_to_role_name('https://github.com/ansible/ansible-modules-extras.git') == 'ansible-modules-extras'
    assert RoleRequirement.repo_url_to_role_name('git+https://github.com/ansible/ansible-modules-extras.git') == 'ansible-modules-extras'

# Generated at 2022-06-13 09:10:58.493477
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    # Make sure deprecation warning is given
    role_requirement = RoleRequirement()
    role_yaml_result = role_requirement.role_yaml_parse("src='https://github.com/user/repo.git', version='v1.0'")
    assert role_yaml_result['src'] == "https://github.com/user/repo.git"
    assert role_yaml_result['name'] == "repo"
    assert role_yaml_result['version'] == "v1.0"

    role_yaml_result = role_requirement.role_yaml_parse("{ src: 'https://github.com/user/repo.git', version: 'v1.0'}")

# Generated at 2022-06-13 09:11:05.956302
# Unit test for method role_yaml_parse of class RoleRequirement

# Generated at 2022-06-13 09:11:15.872585
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    role_def = RoleRequirement()

    # Check parsing of line w/ no version or name
    assert role_def.role_yaml_parse("https://github.com/7bits/ansible-role-user.git") == \
        dict(name='ansible-role-user', scm='git', src='https://github.com/7bits/ansible-role-user.git', version=''), \
        "Failed to correctly parse line w/ no version or name"

    # Check parsing of line w/ only version and no name

# Generated at 2022-06-13 09:11:24.739976
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    role = RoleRequirement()

    # test case: src is only string
    src = "string"
    parsed_role = role.role_yaml_parse(src)
    assert src == parsed_role["src"]
    assert parsed_role["name"] == "string"
    assert parsed_role["version"] == ""
    assert "scm" not in parsed_role

    # test case: src is string with one comma and without version and name
    src = "string, "
    parsed_role = role.role_yaml_parse(src)
    assert src == parsed_role["src"]
    assert parsed_role["name"] == "string"
    assert parsed_role["version"] == ""
    assert "scm" not in parsed_role

    # test case: src is string with one comma and version

# Generated at 2022-06-13 09:11:34.933354
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    def check_parse(a,b,c,d):
        result = RoleRequirement.role_yaml_parse(a)
        role = dict(name=b, src=c, scm=d, version=None)
        assert result == role

    check_parse('git+http://git.example.com/repos/repo.git', 'repo', 'http://git.example.com/repos/repo.git', 'git')
    check_parse('https://github.com/username/repository.git', 'repository', 'https://github.com/username/repository.git', 'git')

# Generated at 2022-06-13 09:11:44.396916
# Unit test for method repo_url_to_role_name of class RoleRequirement
def test_RoleRequirement_repo_url_to_role_name():
    """
    Test if RoleRequirement.repo_url_to_role_name returns expected results
    """
# Input tests
# Expect to return the same string if no scm has been specifed
    repo_url = "git@git.example.com/roles/repo.git"
    expected = "repo"
    result = RoleRequirement.repo_url_to_role_name(repo_url)
    assert result == expected, 'Expected: %s, got: %s' % (expected, result)

    repo_url = "https://git.example.com/roles/repo.git"
    expected = "repo"
    result = RoleRequirement.repo_url_to_role_name(repo_url)

# Generated at 2022-06-13 09:11:55.767302
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    yaml_string1 = "role1"
    yaml_dict1 = {'name': 'role1', 'src': 'role1', 'scm': None, 'version': None}

    yaml_string2 = "role2,v0.1"
    yaml_dict2 = {'name': 'role2', 'src': 'role2', 'scm': None, 'version': 'v0.1'}

    yaml_string3 = "role3,v0.1,rolename"
    yaml_dict3 = {'name': 'rolename', 'src': 'role3', 'scm': None, 'version': 'v0.1'}

    yaml_string4 = "git+https://github.com/1234/role4.git"

# Generated at 2022-06-13 09:12:04.163174
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():

    # setup
    rr = RoleRequirement()

    # print("\nStack Trace\n##########")
    # traceback.print_stack()

    # Test 1:
    test_dict = rr.role_yaml_parse("geerlingguy.apache")
    assert(test_dict['name'] == 'geerlingguy.apache')
    assert(test_dict['scm'] == None)
    assert(test_dict['src'] == 'geerlingguy.apache')
    assert(test_dict['version'] == '')

    # Test 2:
    test_dict = rr.role_yaml_parse("geerlingguy.apache,v2.0.0")
    assert(test_dict['name'] == 'geerlingguy.apache')
    assert(test_dict['scm'] == None)

# Generated at 2022-06-13 09:12:33.070973
# Unit test for method role_yaml_parse of class RoleRequirement
def test_RoleRequirement_role_yaml_parse():
    from os import path
    from tempfile import gettempdir
    from ansible.galaxy import Galaxy

    repo_path = path.join(gettempdir(), 'UnitTestGALAXY')
