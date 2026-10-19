

# Generated at 2022-06-13 06:31:30.369491
# Unit test for method remove of class YumRepo
def test_YumRepo_remove():
    b = YumRepo()
    with open('/home/travis/build/ansible/ansible/test/units/modules/files/yum_repository/epel.repo', 'r') as f:
        b.repofile = configparser.RawConfigParser()
        b.repofile.read_file(f)

    b.remove()
    with open('/home/travis/build/ansible/ansible/test/units/modules/files/yum_repository/epel.repo', 'r') as f:
        a = YumRepo()
        a.repofile = configparser.RawConfigParser()
        a.repofile.read_file(f)
        assert a.repofile.sections() == b.repofile.sections()

# Generated at 2022-06-13 06:31:39.891863
# Unit test for method dump of class YumRepo
def test_YumRepo_dump():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.six import StringIO

    # Test cases
    y = YumRepo(basic.AnsibleModule(
        argument_spec={},
        supports_check_mode=True))
    y.repofile = configparser.RawConfigParser()

    y.repofile.add_section('test')
    y.repofile.set('test', 'foo', 'bar')
    y.repofile.set('test', 'foo2', 'bar2')
    y.repofile.add_section('test2')
    y.repofile.set('test2', 'foo', 'bar')
    y.repofile.set('test2', 'foo2', 'bar2')

# Generated at 2022-06-13 06:31:49.530000
# Unit test for method dump of class YumRepo
def test_YumRepo_dump():
    reposdir = tempfile.mkdtemp()
    repo_file = os.path.join(reposdir, "test.repo")
    repo_data = "[test]\n" \
                "baseurl = baseurl\n" \
                "mirrorlist = mirrorlist\n" \
                "\n" \
                "[test2]\n" \
                "baseurl = baseurl2\n" \
                "mirrorlist = mirrorlist2\n"


# Generated at 2022-06-13 06:32:04.477352
# Unit test for function main
def test_main():
    # Import module and instantiate the class
    module, yumrepo = get_module_and_class()

    # Read test file
    yumrepo.repofile.read(os.path.join(os.path.dirname(__file__), 'test.repo'))

    # Repository exists
    yumrepo.section = 'base'
    assert yumrepo.repofile.has_section(yumrepo.section)
    # Dump repo file
    repo_dump = yumrepo.dump()
    # Remove the repository
    yumrepo.remove()
    # Repository has been removed
    assert not yumrepo.repofile.has_section(yumrepo.section)
    # Dump repo file
    repo_dump_changed = yumrepo.dump()

# Generated at 2022-06-13 06:32:11.613863
# Unit test for method add of class YumRepo

# Generated at 2022-06-13 06:32:25.210389
# Unit test for method dump of class YumRepo
def test_YumRepo_dump():
    module = AnsibleModule(argument_spec={})
    repo = YumRepo(module)

    # Create the repo config object
    repofile = configparser.RawConfigParser()
    repofile.add_section('epel')
    repofile.set('epel', 'baseurl', 'https://download.fedoraproject.org/pub/epel/$releasever/$basearch/')
    repofile.add_section('updates')
    repofile.set('updates', 'baseurl', 'https://example.com/repo/centos/$releasever/$basearch/updates/')
    repofile.set('updates', 'enabled', '0')
    repo.repofile = repofile

    # Test
    result = repo.dump()


# Generated at 2022-06-13 06:32:37.903256
# Unit test for method dump of class YumRepo
def test_YumRepo_dump():
    """Test module for YumRepo.dump"""
    import os
    import tempfile

    test_data = "[epel]\nbaseurl=http://download.fedoraproject.org/pub/epel/7/$basearch\nenabled=1\ngpgcheck=1\n"

    tempfd, tempname = tempfile.mkstemp()
    f = open(tempname, 'w+')
    os.chmod(tempname, 0o644)
    f.write(test_data)
    f.close()

    module_args = {
        'name': 'epel',
        'reposdir': tempfile.gettempdir(),
        'file': 'epel.repo',
        'state': 'present',
    }


# Generated at 2022-06-13 06:32:50.116293
# Unit test for method add of class YumRepo
def test_YumRepo_add():
    module = AnsibleModule(
        argument_spec={
            'name': {'required': True},
            'file': {'default': 'testing'},
            'reposdir': {'default': os.path.join('.', 'tmp')},
            'dest': {'required': True},
        }
    )
    set_module_args(module,
        name='epel',
        baseurl='https://download.fedoraproject.org/pub/epel/$releasever/$basearch/',
        gpgcheck=False,
        enabled=False,
        protect=True,
        sslverify=False,
    )
    yum_repo = YumRepo(module)
    yum_repo.add()


# Generated at 2022-06-13 06:33:00.483950
# Unit test for method dump of class YumRepo
def test_YumRepo_dump():
    repofile = configparser.RawConfigParser()
    repofile.add_section('first')
    repofile.add_section('second')
    repofile.set('first', 'a', 'b')
    repofile.set('first', 'c', 'd')
    repofile.set('second', 'e', 'f')
    repofile.set('second', 'g', 'h')

    repo = YumRepo(AnsibleModule({}))
    repo.repofile = repofile

    assert repo.dump() == '[first]\na = b\nc = d\n\n[second]\ne = f\ng = h\n\n'



# Generated at 2022-06-13 06:33:08.864615
# Unit test for constructor of class YumRepo
def test_YumRepo():
    y = YumRepo(None)

    # Repo file dir
    assert y.reposdir == "/etc/yum.repos.d"
    assert y.params['dest'] == "/etc/yum.repos.d/external_repos.repo"

    # Allowed parameters

# Generated at 2022-06-13 06:33:33.277402
# Unit test for method add of class YumRepo
def test_YumRepo_add():
    params = {
        'name': 'epel',
        'baseurl': 'https://download.fedoraproject.org/pub/epel/$releasever/$basearch/',
        'gpgcheck': False,
        'gpgkey': 'file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-$releasever',
        'reposdir': '/tmp/yum.repos.d',
        'file': 'epel.repo',
        'state': 'present',
        'dest': '/tmp/yum.repos.d/epel.repo'}
    module = AnsibleModule(argument_spec={})

    m_YumRepo = YumRepo(module)
    m_YumRepo.parameters = params
    m_YumRepo

# Generated at 2022-06-13 06:33:39.187084
# Unit test for method dump of class YumRepo
def test_YumRepo_dump():
    # https://github.com/ansible/ansible/issues/8556
    # Please note that this test is not intended to be ran with unit test suite
    # directly.
    # This is just an example which shows how to use the helper method dump().
    module = AnsibleModule(argument_spec={})
    yumrepo = YumRepo(module)
    section = 'foobar'
    parameters = {
        'name': 'foobar',
        'baseurl': 'http://example.com/repo',
        'mirrorlist': 'http://example.com/mirror',
        'metalink': 'http://example.com/metalink',
    }
    yumrepo.repofile = configparser.RawConfigParser()
    yumrepo.repofile.add_section(section)
    yum

# Generated at 2022-06-13 06:33:47.643747
# Unit test for method save of class YumRepo
def test_YumRepo_save():
    import base64

    # Set the module arguments
    module_args = dict(
        name="test_repository",
        baseurl="http://example.org")

    # Set the module instantiation
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True)

    # Instantiate the helper module object
    repo = YumRepo(module)
    repo.add()
    repo.save()

    # Check if the repo file was created
    repo_file = repo.params['dest']
    assert(os.path.isfile(repo_file))

    # Check if the repo file contains the repo configuration
    repo_file_content = ""
    with open(repo_file, 'r') as repo_file_fd:
        repo_file_content = repo_file_

# Generated at 2022-06-13 06:33:56.410024
# Unit test for method add of class YumRepo

# Generated at 2022-06-13 06:34:08.828169
# Unit test for function main
def test_main():
    import os

    # Remove repo file if exists
    repo_file = "/tmp/ansible_yum_repository_unit_test.repo"
    if os.path.isfile(repo_file):
        os.remove(repo_file)

    # Create module

# Generated at 2022-06-13 06:34:22.445724
# Unit test for method save of class YumRepo
def test_YumRepo_save():
    import os
    import shutil
    import sys
    import tempfile

    try:
        import yum

        if sys.version_info[0] == 2:
            import urlparse
        elif sys.version_info[0] == 3:
            import urllib.parse as urlparse

    except ImportError:
        yum_found = False
    else:
        yum_found = True


    def cleanup():
        """Cleanup created directory and files"""
        shutil.rmtree(temp_dir, ignore_errors=True)


    # Create and save a repo file
    def create_file(repo_file, repo_string):
        """Create repo file with content"""
        with open(repo_file, 'w') as fd:
            fd.write(repo_string)


   

# Generated at 2022-06-13 06:34:36.383288
# Unit test for method add of class YumRepo

# Generated at 2022-06-13 06:34:44.794060
# Unit test for method add of class YumRepo
def test_YumRepo_add():
    # Unit test input parameters
    module = AnsibleModule(argument_spec={})
    params = {
        'repoid': 'epel',
        'description': 'EPEL YUM repo',
        'baseurl': 'https://download.fedoraproject.org/pub/epel/$releasever/$basearch/',
        'enabled': '1',
        'gpgcheck': '0',
        'reposdir': '/path/to/repos/dir',
        'file': 'test_repo.repo'
    }

    # Input for method add
    module.params = params
    repo = YumRepo(module)
    repo.add()

    # Output from method add
    output = repo.repofile

    # Expected output
    expected = configparser.RawConfigParser()
    expected.add_

# Generated at 2022-06-13 06:34:51.314471
# Unit test for method dump of class YumRepo
def test_YumRepo_dump():
    ''' Test dump method of class YumRepo using a fake repo file '''
    # Import the class to test
    from ansible.modules.packaging.os.yum_repository import YumRepo

    # Creating a fake module
    module = AnsibleModule({'reposdir': '/test/repos'})

    # Init the class with the module
    repo = YumRepo(module)

    # Let's start to create the fake repo file
    repo.repofile.add_section('myrepo')
    repo.repofile.set('myrepo', 'baseurl', 'http://example.com')
    repo.repofile.set('myrepo', 'priority', '1')

# Generated at 2022-06-13 06:35:03.550769
# Unit test for function main

# Generated at 2022-06-13 06:35:27.080282
# Unit test for method add of class YumRepo

# Generated at 2022-06-13 06:35:31.802285
# Unit test for method remove of class YumRepo
def test_YumRepo_remove():
    module = AnsibleModule({'name': 'repo_test_1'})
    repo = YumRepo(module)

    repo.repofile.add_section('repo_test_1')
    repo.repofile.set('repo_test_1', 'baseurl', 'http://example.com/')

    repo.remove()

    assert repo.repofile.sections() == []

# Generated at 2022-06-13 06:35:36.203097
# Unit test for method save of class YumRepo
def test_YumRepo_save():
    module = AnsibleModule({})
    y = YumRepo(module)
    y.params['dest'] = '/tmp/test.file'
    y.repofile.add_section(y.section)

    assert y.save() is None
    assert os.path.isfile(y.params['dest'])

    y.save()
    os.remove(y.params['dest'])


# Generated at 2022-06-13 06:35:49.206888
# Unit test for function main
def test_main():
    try:
        from ansible.modules.system.yum_repository import main
    except ImportError:
        from ansible.modules.system.yum_repository import __main__ as main

    from ansible.module_utils.six.moves import StringIO
    import contextlib
    import shutil
    import tempfile
    import pytest
    import os

    @pytest.fixture(autouse=True)
    def setup_tmpdir(request):
        tmpdir = tempfile.mkdtemp()
        #tmpdir = '/tmp/ansible-tmp-50344-zTODTrnVY1sW'
        request.addfinalizer(lambda: shutil.rmtree(tmpdir))
        request.cls.tmpdir = tmpdir


# Generated at 2022-06-13 06:35:57.769334
# Unit test for function main
def test_main():
    from ansible.modules.packaging.os.yum_repository import *
    import ansible.modules.packaging.os.yum_repository
    yum_repository = ansible.modules.packaging.os.yum_repository
    module = ansible.modules.packaging.os.yum_repository.module
    yum_repository.main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:36:07.845197
# Unit test for constructor of class YumRepo

# Generated at 2022-06-13 06:36:18.448533
# Unit test for method dump of class YumRepo
def test_YumRepo_dump():
    import tempfile
    import os

    def create_tmpfile(data):
        tmpfd, tmpfile = tempfile.mkstemp()
        with open(tmpfd, 'w') as fd:
            fd.write(data)
        os.close(tmpfd)
        return tmpfile

    module = AnsibleModule(argument_spec={
        'params': {'type': 'dict'},
        'dest': {'type': 'path'},
        'state': {'type': 'str', 'choices': ['present', 'absent']},
    })
    test_YumRepo_dump.input_repo = create_tmpfile("""\
[foo]
baseurl = http://bar

[baz]
baseurl = http://quux
""")
    test_YumRepo_dump.output

# Generated at 2022-06-13 06:36:27.173741
# Unit test for method save of class YumRepo
def test_YumRepo_save():
    import os
    import tempfile
    module = AnsibleModule(argument_spec=dict(
        name=dict(type='str'),
        dest=dict(type='str'),
        reposdir=dict(type='str', default='/etc/yum.repos.d'),
    ))

    # Create a temporary directory
    test_dir = tempfile.mkdtemp()
    # Set the reposdir parameter to the temporary directory
    module.params['reposdir'] = test_dir

    # Add a repo
    repofile = YumRepo(module)

    # Repo information
    repofile.section = "test"
    repofile.repofile.add_section(repofile.section)

    # Set options

# Generated at 2022-06-13 06:36:36.518710
# Unit test for method save of class YumRepo
def test_YumRepo_save():
    module = AnsibleModule(argument_spec={
        'name': {'required': True},
        'baseurl': {'required': False},
        'file': {'required': False, 'default': 'ansible_test'},
        'reposdir': {'required': True, 'default': '.'}
    })
    yumrepo = YumRepo(module)
    yumrepo.section = 'section'
    yumrepo.repofile.add_section('section')
    yumrepo.repofile.set('section', 'key', 'value')
    yumrepo.save()

    with open('%s.repo' % yumrepo.params['file'], 'r') as fd:
        assert fd.read() == "[section]\nkey = value\n"

# Generated at 2022-06-13 06:36:44.354088
# Unit test for method save of class YumRepo
def test_YumRepo_save():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            baseurl=dict(required=False),
            gpgcheck=dict(type='bool', default=False),
            enabled=dict(type='bool', default=True),
            dest=dict(),
            diff_mode=dict(type='bool', default=False),
            state=dict(default='present', choices=['absent', 'present']),
        ),
    )

    # Prepare for action
    repo = YumRepo(module)

    # Set the repo
    repo.add()

    # Save the repo
    repo.save()



# Generated at 2022-06-13 06:37:04.398571
# Unit test for function main
def test_main():
    result = main()
    assert result == "", "main should return \"\""


# Generated at 2022-06-13 06:37:04.855482
# Unit test for method remove of class YumRepo
def test_YumRepo_remove():
    pass

# Generated at 2022-06-13 06:37:06.757305
# Unit test for function main
def test_main():
    main()


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:37:12.130732
# Unit test for function main

# Generated at 2022-06-13 06:37:17.494296
# Unit test for method add of class YumRepo
def test_YumRepo_add():
    param = dict(
        name='epel',
        description='EPEL YUM repo',
        baseurl='https://download.fedoraproject.org/pub/epel/$releasever/$basearch/',
        gpgcheck=False,
        reposdir='/etc/yum.repos.d/',
        file='epel.repo',
    )
    repo = YumRepo(AnsibleModule(argument_spec={}, supports_check_mode=True))
    repo.params = param

    assert(not repo.repofile.has_section('epel'))
    repo.add()
    assert(repo.repofile.has_section('epel'))

# Generated at 2022-06-13 06:37:24.052506
# Unit test for method remove of class YumRepo
def test_YumRepo_remove():
    module = AnsibleModule({'repoid': 'nameofrepo'})
    repofile = configparser.RawConfigParser()
    repofile.add_section('nameofrepo')
    repofile.set('nameofrepo', 'baseurl', 'http://example.com')
    yumrepo = YumRepo(module)
    yumrepo.repofile = repofile
    yumrepo.remove()
    assert not yumrepo.repofile.has_section('nameofrepo')


# Generated at 2022-06-13 06:37:30.063103
# Unit test for method save of class YumRepo
def test_YumRepo_save():
    # Construct a module fake object and a YumRepo object
    module = AnsibleModule(argument_spec={})
    yum_repo_object = YumRepo(module)

    # When the YumRepo object has no section, the method save should remove
    # the file. Hence, we create a fake file and check if it exists after the
    # method.
    with open("foo.txt", "w") as foo_file:
        foo_file.write("Foo")

    assert os.path.isfile("foo.txt")

    yum_repo_object.module.params['dest'] = "foo.txt"
    yum_repo_object.save()

    assert not os.path.isfile("foo.txt")

    # When the YumRepo object has one section and one option, the method save

# Generated at 2022-06-13 06:37:38.260547
# Unit test for method add of class YumRepo
def test_YumRepo_add():
    """
    This test checks the behaviour of method add of the class YumRepo.
    class YumRepo is a helper class to handle yum repository files.

    :return: Nothing
    """

    # Create a YumRepo instance
    yum_repo = YumRepo()

    # Define an empty yum repository file
    yum_repo.repofile = configparser.RawConfigParser()

    # Add a new repo
    yum_repo.add()

    # Check if the repo was added
    assert yum_repo.repofile.has_section('epel') == True

    # Check the output of method dump

# Generated at 2022-06-13 06:37:53.926002
# Unit test for function main

# Generated at 2022-06-13 06:38:03.429188
# Unit test for method save of class YumRepo

# Generated at 2022-06-13 06:38:37.641876
# Unit test for method save of class YumRepo
def test_YumRepo_save():
    assert True == True

# Generated at 2022-06-13 06:38:45.425637
# Unit test for method save of class YumRepo
def test_YumRepo_save():
    from ansible.utils.path import unfrackpath
    from tempfile import mkstemp

    workdir = unfrackpath("/tmp")
    repo_file_name = "foo.repo"
    repodir = os.path.join(workdir, repo_file_name)

    fd, tmpfile = mkstemp(dir=workdir)
    os.write(fd, "# Comment line\n".encode())
    os.close(fd)

    m = AnsibleModule(
        argument_spec=dict(
            file=dict(default=repo_file_name, type='str'),
            params=dict(default=dict(), type='dict'),
            reposdir=dict(default=workdir, type='str'),
            dest=dict(default=repodir, type='str'),
        )
    )


# Generated at 2022-06-13 06:38:51.076876
# Unit test for method save of class YumRepo
def test_YumRepo_save():
    YumRepo_obj = YumRepo()
    YumRepo_obj.params['dest'] = 'dest'
    YumRepo_obj.repofile.add_section('section')
    YumRepo_obj.repofile.set('section', 'key', 'value')

    # Create the file
    YumRepo_obj.save()

    # Check that the dest file exists now
    if not os.path.isfile(YumRepo_obj.params['dest']):
        raise AssertionError("The dest file was not created")

    # Remove the file
    os.remove(YumRepo_obj.params['dest'])

    # Check that is removed

# Generated at 2022-06-13 06:39:00.534063
# Unit test for method remove of class YumRepo
def test_YumRepo_remove():
    module = AnsibleModule(
        argument_spec={
            'repoid': {'type': 'str', 'required': False, 'default': 'epel'},
            'state': {'type': 'str', 'required': False, 'default': 'absent'}
        },
        supports_check_mode=True
    )

    repofile = configparser.RawConfigParser()
    repofile.read("repofiles/repofile")

    y = YumRepo(module)
    y.repofile = repofile
    y.section = "repoid"

    assert repofile.has_section("repoid")

    y.remove()

    assert not repofile.has_section("repoid")



# Generated at 2022-06-13 06:39:06.237712
# Unit test for method dump of class YumRepo
def test_YumRepo_dump():
    module = type('', (), {'params': {}, 'fail_json': None})()
    setattr(module, 'params', {'dest': "tests/rpmforge.repo"})
    repo = YumRepo(module)

    # Compare the strings
    assert repo.dump() == "[base]\n\n[custom]\nbaseurl = http://example.com/repo\n\n[epel]\nbaseurl = http://example.com/repo\n\n[rpmforge]\nbaseurl = http://example.com/repo\n\n"



# Generated at 2022-06-13 06:39:14.236643
# Unit test for constructor of class YumRepo

# Generated at 2022-06-13 06:39:22.893476
# Unit test for method add of class YumRepo

# Generated at 2022-06-13 06:39:31.677885
# Unit test for method remove of class YumRepo
def test_YumRepo_remove():
    # Prepare the parameters
    module = AnsibleModule(argument_spec={})
    params = {
        'baseurl': 'http://test',
        'dest': 'test_dest',
        'file': 'test',
        'name': 'test_name',
        'reposdir': 'test_repos_dir',
        'repoid': 'test_repoid'}

    # Initialize the object
    test_object = YumRepo(module=module)
    test_object.params = params

    # Prepare the repo file
    test_object.repofile.add_section('test_repoid')
    test_object.repofile.add_section('test_repoid_2')
    test_object.repofile.set('test_repoid', 'name', 'test_name')

# Generated at 2022-06-13 06:39:32.840404
# Unit test for method remove of class YumRepo
def test_YumRepo_remove():
    return



# Generated at 2022-06-13 06:39:48.083736
# Unit test for method save of class YumRepo
def test_YumRepo_save():
    import tempfile
    filename = tempfile.NamedTemporaryFile(delete=False)
    filename.close()

    # Init the module
    module = AnsibleModule(
        argument_spec=dict(
            repoid=dict(required=True),
            state=dict(choices=['absent', 'present'], default='present'),
            dest=dict(default=filename.name),
        ),
    )

    repofile = configparser.RawConfigParser()
    repofile.add_section('test')
    repofile.set('test', 'value', 1)

    # Init the class
    yum = YumRepo(module=module)
    yum.repofile = repofile
    yum.save()

    os.unlink(filename.name)
