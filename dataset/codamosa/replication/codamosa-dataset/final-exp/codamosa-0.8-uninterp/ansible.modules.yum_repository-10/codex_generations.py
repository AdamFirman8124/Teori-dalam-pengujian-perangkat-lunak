

# Generated at 2022-06-13 06:31:24.443053
# Unit test for function main
def test_main():
    pass
if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:31:32.627341
# Unit test for method add of class YumRepo
def test_YumRepo_add():
    '''
    Repo file looks like this before `add` method is called:
    [existing-repo]
    name = existing repo
    exclude = NOT-EXISTS-1 NOT-EXISTS-2

    [myrepo]
    baseurl = baseurl
    protect = 1
    ui_repoid_vars = releasever
    '''

    # Define the repo content
    repo_content = '[existing-repo]\n' \
                   'name = existing repo\n' \
                   'exclude = NOT-EXISTS-1 NOT-EXISTS-2\n\n' \
                   '[myrepo]\n' \
                   'baseurl = baseurl\n' \
                   'protect = 1\n' \
                   'ui_repoid_vars = releasever\n' \



# Generated at 2022-06-13 06:31:40.856513
# Unit test for method add of class YumRepo

# Generated at 2022-06-13 06:31:48.492753
# Unit test for method add of class YumRepo
def test_YumRepo_add():
    # Test add method
    module = AnsibleModule(
        argument_spec={
            "baseurl": {"required": True, "type": "str"},
            "file": {"required": True, "type": "str"},
            "name": {"required": True, "type": "str"},
            "reposdir": {"required": True, "type": "path"},
            "state": {"required": True, "type": "str", "choices": ["present", "absent"]}
        },
        supports_check_mode=True
    )

    yum_repo = YumRepo(module)
    yum_repo.add()



# Generated at 2022-06-13 06:31:53.643586
# Unit test for method save of class YumRepo
def test_YumRepo_save():
    """
    Unit test for method YumRepo.save
    """
    module = AnsibleModule(
        argument_spec=dict(
            repoid="epel",
            dest="/tmp/test_repo",
            gpgcheck=False,
            baseurl="http://example.org",
            enabled=True,
        )
    )
    repo = YumRepo(module)

    # Create a dummy object to test the save method
    repo.repofile = configparser.RawConfigParser()
    repo.repofile.add_section("test")
    repo.repofile.set("test", "gpgcheck", "0")
    repo.repofile.set("test", "baseurl", "http://example.org")
    repo.repofile.set("test", "enabled", "1")

    #

# Generated at 2022-06-13 06:32:04.822429
# Unit test for constructor of class YumRepo
def test_YumRepo():
    '''
    Unit test for constructor of class YumRepo.

    This function is named "test_" to be used with tests/test.py
    '''
    # Parameters

# Generated at 2022-06-13 06:32:15.629448
# Unit test for method dump of class YumRepo
def test_YumRepo_dump():
    # Create class object
    y = YumRepo(None)
    # Read the repo file
    y.repofile.read(os.path.join('files', 'test1.repo'))
    # Dump the repo file
    repo_string = y.dump()
    # Create a file object
    f = open(os.path.join('files', 'test1.repo'), 'r')
    # Get the content of the file
    file_content = f.read()
    f.close()

    if file_content == repo_string:
        return True

    return False



# Generated at 2022-06-13 06:32:29.208145
# Unit test for function main
def test_main():
    with mock.patch('ansible_collections.notmintest.not_a_real_collection.plugins.module_utils.basic.AnsibleModule.exit_json') as exit_json:
        with mock.patch('ansible_collections.notmintest.not_a_real_collection.plugins.module_utils.basic.AnsibleModule.fail_json') as fail_json:
            with mock.patch('os.path.isdir') as isdir:
                isdir.return_value = True
                with mock.patch('os.path.isfile') as isfile:
                    isfile.return_value = False
                    with mock.patch('os.remove') as remove:
                        remove.return_value = True

# Generated at 2022-06-13 06:32:41.322377
# Unit test for function main

# Generated at 2022-06-13 06:32:53.813379
# Unit test for method remove of class YumRepo
def test_YumRepo_remove():
    # Prepare environment
    module = AnsibleModule(argument_spec={
        'repoid': {
            'default' : "epel",
            'type' : 'str'
        },
        'file': {
            'default': "external_repos",
            'type': 'str'
        },
        'reposdir': {
            'default': "/etc/yum.repos.d",
            'type': 'str'
        }
    })
    params = module.params

    # Set repo file
    repofile = ModuleStub()
    repofile.sections = ["epel"]
    repofile.items = {"epel": {"gpgcheck": "1"}}
    repofile.remove_section = stub_remove_section

    # Add class stubs and prepare class instance
    YumRepo

# Generated at 2022-06-13 06:33:18.076955
# Unit test for method dump of class YumRepo
def test_YumRepo_dump():
    import tempfile
    import ansible.utils as utils
    import ansible.runner
    import ansible.json
    import ansible.constants
    import ansible.errors
    import ansible.inventory
    import ansible.filedepot
    import ansible.playbook

    test_module = AnsibleModule(
        argument_spec=dict(
            repoid='epel',
            state='present',
            baseurl='https://download.fedoraproject.org/pub/epel/$releasever/$basearch/',
            file='external_repos',
            gpgcheck='no',
            reposdir='/etc/yum.repos.d'
        ),
    )

    # Create a temp file
    (fd, temp_path) = tempfile.mkstemp()


# Generated at 2022-06-13 06:33:26.282486
# Unit test for method save of class YumRepo
def test_YumRepo_save():
    m = AnsibleModule(
        argument_spec={
            'baseurl': dict(type='str'),
            'file': dict(type='str', default=''),
            'name': dict(type='str', default='ansible'),
            'reposdir': dict(type='str', default='/etc/yum.repos.d')
        }
    )
    y = YumRepo(m)
    y.add()
    y.save()




# Generated at 2022-06-13 06:33:33.969441
# Unit test for method add of class YumRepo
def test_YumRepo_add():
    test_module = AnsibleModule(
        argument_spec=dict(
            repoid='epel',
            description='EPEL YUM repo',
            file='epel.repo',
            baseurl='http://download.fedoraproject.org/pub/epel/7/$basearch',
            enabled=True,
            gpgcheck=True,
            gpgkey='https://dl.fedoraproject.org/pub/epel/RPM-GPG-KEY-EPEL-7',
            reposdir='/etc/yum.repos.d'),
        check_invalid_arguments=False)

    test_YumRepo = YumRepo(module=test_module)

    repofile_example = configparser.RawConfigParser()

# Generated at 2022-06-13 06:33:40.840849
# Unit test for method save of class YumRepo
def test_YumRepo_save():
    module = AnsibleModule({'dest': None}, check_invalid_arguments=False)
    yum_repo_object = YumRepo(module)
    yum_repo_object.repofile = configparser.RawConfigParser()

    # Write empty config to file
    yum_repo_object.save()

    # Check if the file was written
    assert os.path.exists(yum_repo_object.params['dest'])

    # Remove the file
    os.remove(yum_repo_object.params['dest'])

    # Add section
    yum_repo_object.repofile.add_section('test')

    # Write config with single section to file
    yum_repo_object.save()

    # Check if the file was written
    assert os.path

# Generated at 2022-06-13 06:33:48.649165
# Unit test for method add of class YumRepo

# Generated at 2022-06-13 06:33:55.935568
# Unit test for method remove of class YumRepo
def test_YumRepo_remove():
    # Initialize the class
    myYumRepo = YumRepo(None)

    # Setup the repository to be present in the list
    myYumRepo.repofile.add_section("test")
    myYumRepo.section = "test"

    # Now remove the repository from the list
    myYumRepo.remove()

    assert not myYumRepo.repofile.has_section("test"), \
        "YumRepo class remove() method does not work"


# Generated at 2022-06-13 06:34:08.747707
# Unit test for method remove of class YumRepo
def test_YumRepo_remove():
    '''
    Unit test for method remove of class YumRepo.
    '''

    # Create a mock module
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_native

    # Create the repository file in memory
    from ansible.module_utils.six.moves import configparser
    text_file = configparser.RawConfigParser()
    text_file.add_section('epel')
    text_file.add_section('rpmforge')
    text_file.add_section('epel-testing')

    # Create the test module

# Generated at 2022-06-13 06:34:20.796011
# Unit test for method dump of class YumRepo
def test_YumRepo_dump():
    from ansible.module_utils.pycompat24 import StringIO

    module = AnsibleModule({
        'file': 'epel',
        'reposdir': '.',
    })
    yum = YumRepo(module)
    yum.repofile = configparser.RawConfigParser()
    yum.repofile.readfp(StringIO(u"""[epel]
name=epel
baseurl=https://url.example.com/
gpgcheck=1
"""))

    expected = u"""[epel]
baseurl = https://url.example.com/
gpgcheck = 1
name = epel

"""

    assert yum.dump() == expected


# Generated at 2022-06-13 06:34:30.603724
# Unit test for constructor of class YumRepo
def test_YumRepo():
    class AnsibleModuleMock(object):
        def __init__(self, **kwargs):
            self.params = kwargs

        def fail_json(self, msg):
            raise Exception(msg)

    # Create instance and check if the repo file is empty
    repo = YumRepo(AnsibleModuleMock(reposdir='/tmp', file='unittest'))
    assert len(repo.repofile.sections()) == 0


# Generated at 2022-06-13 06:34:42.014287
# Unit test for method dump of class YumRepo
def test_YumRepo_dump():
    module = AnsibleModule(argument_spec={
        'file': {'required': True, 'type': 'str'},
        'state': {'default': 'present', 'type': 'str'},
        'repoid': {'required': True, 'type': 'str'},
        'baseurl': {'required': False, 'type': 'str'},
        'mirrorlist': {'required': False, 'type': 'str'},
        'reposdir': {'required': False, 'type': 'str'},
    })
    file = module.params['file']
    repoid = module.params['repoid']
    baseurl = module.params['baseurl']
    mirrorlist = module.params['mirrorlist']
    reposdir = module.params['reposdir']

# Generated at 2022-06-13 06:35:22.564771
# Unit test for constructor of class YumRepo
def test_YumRepo():
    module = AnsibleModule({
        'repoid': 'epel',
        'file': 'external_repos',
        'reposdir': '/tmp'})

    repo = YumRepo(module)
    assert repo.section == 'epel'
    assert repo.params['file'] == 'external_repos'
    assert repo.params['reposdir'] == '/tmp'


# Generated at 2022-06-13 06:35:28.516371
# Unit test for method add of class YumRepo
def test_YumRepo_add():
    import tempfile
    # Create temporary file
    temp_fd, temp_path = tempfile.mkstemp()
    # Example module argument spec

# Generated at 2022-06-13 06:35:38.612910
# Unit test for constructor of class YumRepo
def test_YumRepo():
    # Constructor of class AnsibleModule
    module = AnsibleModule(
        argument_spec={
            'name': {'type': 'str'},
            'file': {'type': 'str'},
            'reposdir': {'type': 'path'},
            'dest': {'type': 'path'},
            'params': {'type': 'dict'},
            'state': {
                'choices': ['absent', 'present'],
                'default': 'present'},
        },
    )

    # Proper init of YumRepo class
    yum_repo = YumRepo(module)
    assert module == yum_repo.module
    assert module.params == yum_repo.params
    assert module.params['name'] == yum_repo.section

# Generated at 2022-06-13 06:35:50.451774
# Unit test for method save of class YumRepo
def test_YumRepo_save():
    from ansible.module_utils import basic
    from timeout_decorator import timeout

    class MockModule(object):
        def __init__(self):
            self._repo = YumRepo(self)

        def fail_json(self, **kwargs):
            return kwargs

        @property
        def params(self):
            return {'dest': '/tmp/test.repo'}

        @property
        def repo(self):
            return self._repo

    class MockConfigParser(object):
        def __init__(self):
            self._objects = {}

        def sections(self):
            return self._objects.keys()

        def items(self, section):
            return self._objects[section].items()


# Generated at 2022-06-13 06:36:03.282804
# Unit test for method dump of class YumRepo
def test_YumRepo_dump():
    """Unit test for method dump of class YumRepo"""
    # Test module
    module = AnsibleModule({
        'state': 'present',
        'params': {
            'name': 'epel',
            'file': 'external_repos',
            'reposdir': 'test_data',
            'baseurl': 'https://download.fedoraproject.org/pub/epel/$releasever/$basearch/'},
        'reposdir': 'test_data'})
    # Test class instance
    repo = YumRepo(module)
    # Test section
    repo.section = 'epel'
    # Test data
    repo.repofile.add_section('epel')
    repo.repofile.set('epel', 'name', 'epel')
    repo.repofile.set

# Generated at 2022-06-13 06:36:10.826298
# Unit test for method remove of class YumRepo
def test_YumRepo_remove():
    module = AnsibleModule(argument_spec=dict(
        repoid=dict(required=True),
        state=dict(default='absent', choices=['absent', 'present']),
        file=dict(required=False, default='ansible'),
        reposdir=dict(required=False, default='/etc/yum.repos.d'),
        ))
    repo = YumRepo(module)
    # Add the repo
    repo.add()
    # Remove the repo
    repo.remove()
    # Save the repo
    repo.save()
    # Dump the repo
    output = repo.dump()
    assert not output


# Generated at 2022-06-13 06:36:20.715501
# Unit test for method dump of class YumRepo
def test_YumRepo_dump():
    src_string = """\
[epel]
name = EPEL YUM repo
baseurl = http://download.fedoraproject.org/pub/epel/6/$basearch
enabled = 0
gpgcheck = 1

[rpmforge]
name = RPMforge YUM repo
baseurl = http://apt.sw.be/redhat/el7/en/$basearch/rpmforge
mirrorlist = http://mirrorlist.repoforge.org/el7/mirrors-rpmforge
enabled = 1
gpgcheck = 1
"""

    repo_file = configparser.RawConfigParser()
    repo_file.read_string(src_string)

    y = YumRepo(None)
    y.repofile = repo_file

    assert y.dump() == src_string



# Generated at 2022-06-13 06:36:28.050794
# Unit test for method add of class YumRepo
def test_YumRepo_add():
    class test_module():
        def __init__(self, params):
            self.params = params

    class test_params():
        def __init__(self, **kwargs):
            for key, value in sorted(kwargs.items()):
                self.__dict__[key] = value

    # Create an object with this module
    module = test_module(None)

    # Define some test parameters

# Generated at 2022-06-13 06:36:36.816897
# Unit test for method remove of class YumRepo
def test_YumRepo_remove():
    import io
    module = AnsibleModule(argument_spec=dict(), supports_check_mode=True)
    fake_in = io.StringIO()
    fake_in.write('[test-repo]\n')
    fake_in.write('baseurl = http://example.com/mirror\n')
    fake_in.write('gpgcheck = no\n')
    fake_in.write('[another-repo]\n')
    fake_in.write('baseurl = http://another.example.com/mirror\n')
    fake_in.write('gpgcheck = yes\n')
    fake_in.write('[example-repo]\n')
    fake_in.write('baseurl = https://yum.example.com/mirror\n')

# Generated at 2022-06-13 06:36:45.383263
# Unit test for method dump of class YumRepo
def test_YumRepo_dump():
    import tempfile
    import shutil

    class Module(object):
        """Constructor for class Module for unit testing YumRepo class."""
        def __init__(self, params):
            self.params = params

    class AnsibleModule(object):
        FAIL_JSON = Exception

        def __init__(self, *args, **kwargs):
            self.params = kwargs.get('params', {})

        def fail_json(self, *args, **kwargs):
            self.exit_args = kwargs
            self.exit_args['failed'] = True
            raise AnsibleModule.FAIL_JSON(kwargs['msg'])

    def test_dump_returns_repo_string():
        tmp_dir = tempfile.mkdtemp()

# Generated at 2022-06-13 06:38:01.968035
# Unit test for method add of class YumRepo
def test_YumRepo_add():
    class _module(object):
        params = dict(
            repo_name='test_repo',
            description='Test repo',
            baseurl='http://example.org',
            exclude='foo bar',
            gpgcheck=True,
            metalink='http://localhost/metalink.xml',
            mirrorlist_expire='10',
            name='test_repo',
            proxy_password='secret',
            proxy_username='user',
            s3_enabled=False,
            sslclientcert='/etc/pki/client-cert.pem',
            sslclientkey='/etc/pki/client-key.pem',
        )
    module = _module()

    yum_repo = YumRepo(module)
    yum_repo.add()

    # Test for parameters

# Generated at 2022-06-13 06:38:08.572862
# Unit test for method remove of class YumRepo
def test_YumRepo_remove():
    module = AnsibleModule({'file': 'test.repo', 'name': 'test'})
    repo = YumRepo(module)

    repo.repofile.add_section('test')
    repo.remove()

    if repo.repofile.has_section('test'):
        assert False, "Remove method is broken."
    else:
        assert True



# Generated at 2022-06-13 06:38:21.041853
# Unit test for method save of class YumRepo
def test_YumRepo_save():

    import shutil
    import tempfile

    tmp_dir = tempfile.mkdtemp()


# Generated at 2022-06-13 06:38:29.959985
# Unit test for constructor of class YumRepo
def test_YumRepo():
    # Import needed so this test can be exectuted as __main__
    from ansible.module_utils.basic import AnsibleModule
    # Fake module class
    class FakeModule():
        def fail_json(self, *_):
            return

    # Fake params
    params = { 'repoid': 'test' }

    # Test the constructor
    repo = YumRepo(FakeModule())
    assert repo.module
    assert repo.params
    assert repo.section == params['repoid']
    assert repo.repofile


# Generated at 2022-06-13 06:38:33.198866
# Unit test for constructor of class YumRepo
def test_YumRepo():
    module = AnsibleModule({
        'file': 'epel',
        'reposdir': '/etc/yum.repos.d',
        'repoid': 'epel'})

    assert YumRepo(module)


# Generated at 2022-06-13 06:38:36.336389
# Unit test for constructor of class YumRepo
def test_YumRepo():
    module = AnsibleModule(argument_spec={})
    yumrepo = YumRepo(module)

    assert yumrepo.section == {}



# Generated at 2022-06-13 06:38:40.451614
# Unit test for method save of class YumRepo
def test_YumRepo_save():

    # Tests are kept in separate files so that you can use the IDE autocomplete
    # and typehints
    import tests.unit.modules.yum_repository_test

    tests.unit.modules.yum_repository_test.test_YumRepo_save()


# Generated at 2022-06-13 06:38:47.370437
# Unit test for function main

# Generated at 2022-06-13 06:39:00.168891
# Unit test for method save of class YumRepo
def test_YumRepo_save():
    import os
    import shutil
    import tempfile

    module = AnsibleModule(
        argument_spec={
            "file": {"required": True, "default": "myrepo", "type": "str"},
            "reposdir": {"required": True, "default": "/tmp", "type": "str"},
        }
    )

    # We need to create a temporary directory for the unit test
    tmp_dir = tempfile.mkdtemp()

    # Create the parameters
    params = {
        "file": "myrepo",
        "reposdir": tmp_dir,
        "baseurl": None,
        "metalink": None,
        "mirrorlist": None,
    }

    # Create a new object
    repo = YumRepo(module)

    # Testcase 1: no section in the repo file

# Generated at 2022-06-13 06:39:07.430227
# Unit test for method remove of class YumRepo
def test_YumRepo_remove():
    module = AnsibleModule(argument_spec={
        'baseurl': dict(default=None, type='str'),
        'dest': dict(default='/etc/yum.repos.d/file.repo', type='str'),
        'file': dict(default='file', type='str'),
        'reposdir': dict(default='/etc/yum.repos.d', type='str'),
        'repoid': dict(default='repo', type='str'),
        'state': dict(default='absent', type='str'),
        'metalink': dict(default=None, type='str'),
        'mirrorlist': dict(default=None, type='str')
    })
