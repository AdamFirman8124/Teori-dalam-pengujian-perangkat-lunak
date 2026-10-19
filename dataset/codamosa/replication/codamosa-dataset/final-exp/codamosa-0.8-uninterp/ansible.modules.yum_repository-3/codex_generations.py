

# Generated at 2022-06-13 06:31:32.445991
# Unit test for method add of class YumRepo
def test_YumRepo_add():
    ''' test_YumRepo_add
    Unit test for method add of class YumRepo
    '''
    # Test for input 'add'
    yum_repo_object = YumRepo(module=None)
    yum_repo_object.params = {}
    yum_repo_object.params['repoid'] = "epel"
    yum_repo_object.params['baseurl'] = "https://download.fedoraproject.org/pub/epel/$releasever/$basearch/"
    yum_repo_object.params['reposdir'] = "/etc/yum.repos.d"
    yum_repo_object.params['dest'] = "/etc/yum.repos.d/epel.repo"
    return_value = yum_re

# Generated at 2022-06-13 06:31:40.750253
# Unit test for method add of class YumRepo
def test_YumRepo_add():
    import platform
    import os
    from ansible.module_utils.basic import AnsibleModule

    # Setting up the module
    module = AnsibleModule(
        argument_spec = dict(
            repoid = dict(type='str', required=True),
            file = dict(type='str', required=True),
            name = dict(type='str', required=True),
            baseurl = dict(type='str', required=False),
            metalslink = dict(type='str', required=False),
            mirrorlist = dict(type='str', required=False),
        )
    )

    def create_fake_repofile(repofile_name):
        # Create a fake repo file with a repo section
        repofile = configparser.RawConfigParser()
        repofile.add_section('section1')
        repofile

# Generated at 2022-06-13 06:31:49.818906
# Unit test for method add of class YumRepo
def test_YumRepo_add():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            state=dict(choices=['absent', 'present'], default='present'),
            reposdir=dict(type='path', default='/etc/yum.repos.d'),
            file=dict(default='ansible-test.repo'),
            baseurl=dict(type='str'),
            metalink=dict(type='str'),
            mirrorlist=dict(type='str'),
            gpgcheck=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )

    repo_file = YumRepo(module)
    repo_file.add()
    res = repo_file.dump()


# Generated at 2022-06-13 06:31:56.163380
# Unit test for method remove of class YumRepo
def test_YumRepo_remove():
    from ansible.module_utils import basic
    yumrepo = YumRepo(basic.AnsibleModule(argument_spec={}))
    # Read sample repo file
    yumrepo.repofile.read('/etc/yum.repos.d/CentOS-Base.repo')
    # Change the section name
    yumrepo.section = "CentOS-Debuginfo"
    # Remove section
    yumrepo.remove()
    # Check if the section has been removed correctly
    assert "CentOS-Debuginfo" not in yumrepo.repofile.sections()


# Generated at 2022-06-13 06:32:07.032378
# Unit test for method add of class YumRepo
def test_YumRepo_add():
    """Unit test for method add of class YumRepo"""

    module = AnsibleModule(
        argument_spec={
            'baseurl': dict(required=False, type='str'),
            'file': dict(required=True, type='str'),
            'name': dict(required=True, type='str'),
            'reposdir': dict(required=False, type='path', default='/etc/yum.repos.d'),
        },
        supports_check_mode=False
    )
    yum = YumRepo(module)

    # Remove previous repo and create a new one
    yum.add()

    # Check that parameters are present in the output
    output = yum.dump()
    assert "name = %s" % yum.section in output

# Generated at 2022-06-13 06:32:16.919955
# Unit test for function main
def test_main():
    fixture = ({
        'file': '/etc/yum.repos.d/epel.repo',
        'skip_if_unavailable': False,
        'name': 'EPEL YUM repo',
        'enabled': True,
        'gpgcheck': 1,
        'gpgkey': (
            'file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7\n'
            'file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7-debug-beta'
        ),
        'baseurl': 'https://download.fedoraproject.org/pub/epel/$releasever/$basearch/'
    }, '', None)

# Generated at 2022-06-13 06:32:25.221568
# Unit test for method save of class YumRepo
def test_YumRepo_save():
    import ansible.module_utils.basic
    module = ansible.module_utils.basic.AnsibleModule(
        argument_spec={'reposdir': {'type': 'str'}, 'file': {'type': 'str'}})
    module.params = {
        'dest': '/tmp/test.repo', 'reposdir': '/tmp', 'file': 'test'}

    yr = YumRepo(module)
    yr.add()
    yr.save()



# Generated at 2022-06-13 06:32:35.212431
# Unit test for constructor of class YumRepo
def test_YumRepo():
    module = AnsibleModule(
        argument_spec=dict(
            description=dict(),
            name=dict(required=True),
            file=dict(default="custom-repo"),
            reposdir=dict(default="/etc/yum.repos.d"),
        )
    )

    # Test init
    repo = YumRepo(module)

    assert repo.params["dest"] == "/etc/yum.repos.d/custom-repo.repo"
    assert not repo.repofile.sections() == None
    assert repo.section == "custom-repo"


# Generated at 2022-06-13 06:32:42.478895
# Unit test for method save of class YumRepo
def test_YumRepo_save():
    module = AnsibleModule(argument_spec={'dest': {'type': 'str'}})
    repofile = configparser.RawConfigParser()
    # Prepare a fake repo file
    repofile.add_section('test')
    repofile.set('test', 'baseurl', 'http://foo.bar')
    repofile.set('test', 'enabled', '0')
    # Try to save it
    obj = YumRepo(module)
    obj.repofile = repofile
    obj.save()



# Generated at 2022-06-13 06:32:50.071568
# Unit test for function main
def test_main():
    # Module import
    from ansible.modules.packaging.os.yum_repository import YumRepo
    from ansible.modules.packaging.os.yum_repository import main

    # Test code here
    # Test cases
    yumrepo = YumRepo('')
    assert main() == ''

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:33:35.020352
# Unit test for constructor of class YumRepo
def test_YumRepo():
    # Create a fake module
    module = AnsibleModule(argument_spec={
        'baseurl': dict(),
        'dest': dict(),
        'file': dict(default='myrepo')
    })

    # Create YumRepo class
    yum_repo = YumRepo(module)

    # Has repo directory
    assert yum_repo.params['dest'] == '/etc/yum.repos.d/myrepo.repo'

    # Check if class variables are correctly set
    assert yum_repo.section == 'myrepo'
    assert yum_repo.repofile.sections() == []

    # Check if default value for parameters are set
    assert yum_repo.params['repoid'] is None

# Generated at 2022-06-13 06:33:41.700618
# Unit test for method dump of class YumRepo
def test_YumRepo_dump():
    # Instantiate YumRepo
    module = AnsibleModule(argument_spec={})
    repofile = YumRepo(module)

    # Create a repo file
    repofile.add()

    # Inside unit tests we have to add the section manually, otherwise
    # the section is added automatically because all parameters are defined
    repofile.repofile.add_section('test')

    # Set test repo parameters
    repofile.repofile.set('test', 'param1', 'test')
    repofile.repofile.set('test', 'param2', 'test2')

    # Dump the repofile
    repo_string = repofile.dump()


# Generated at 2022-06-13 06:33:49.703749
# Unit test for constructor of class YumRepo
def test_YumRepo():
    # Create a YumRepo instance
    yum_repo = YumRepo(AnsibleModule({
        'dest': '/test/test.repo',
        'file': 'test',
        'name': 'test',
        'reposdir': '/test/',
        'state': 'present'}))

    # Check if not repo file was read
    assert len(yum_repo.repofile.sections()) == 0

    # Check if section was set
    assert yum_repo.section == 'test'



# Generated at 2022-06-13 06:34:02.148569
# Unit test for function main
def test_main():
    import os
    import shutil
    import tempfile


# Generated at 2022-06-13 06:34:11.551042
# Unit test for method save of class YumRepo
def test_YumRepo_save():
    class AnsibleModule(object):
        def __init__(self, params):
            self.params = params

    # Create a repo file
    repofile = configparser.RawConfigParser()
    repofile.add_section('epel')
    repofile.set('epel', 'name', 'EPEL')
    repofile.set('epel', 'baseurl', 'https://download.fedoraproject.org/pub/epel/$releasever/$basearch/')
    repofile.set('epel', 'enabled', '1')
    repofile.set('epel', 'gpgcheck', '1')
    repofile.set('epel', 'gpgkey', 'file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7')

    #

# Generated at 2022-06-13 06:34:23.288003
# Unit test for method add of class YumRepo
def test_YumRepo_add():
    import os
    import shutil

    class FakeModule(object):
        def __init__(self, params):
            self.params = params
            self.fail_json = lambda x: self.fail(x)

        def fail(self, msg):
            raise AssertionError(msg)

        def exit_json(self, **kwargs):
            raise NotImplementedError()

    module = FakeModule({
        'name': 'epel',
        'state': 'present',
        'reposdir': '/tmp',
        'file': 'test_add.repo'})

    # Define file
    repofile = '/tmp/test_add.repo'

    # Create repos dir
    os.makedirs('/tmp')

    # Create repo object
    repo = YumRepo(module)

   

# Generated at 2022-06-13 06:34:36.871104
# Unit test for method save of class YumRepo
def test_YumRepo_save():
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat import unittest
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat.mock import patch
    from ansible_collections.notstdlib.moveitallout.plugins.modules import yum_repository

    # Create a mock for the open function
    mock_class = unittest.mock.mock_open()

    # Create a fake file-like object
    fake_file = unittest.mock.MagicMock(spec=file)

    # Create a mock for the os.remove function
    mock_remove = unittest.mock.MagicMock()

    # Create a mock for the module

# Generated at 2022-06-13 06:34:44.918363
# Unit test for method add of class YumRepo
def test_YumRepo_add():
    module = AnsibleModule(argument_spec={
        'file': {'type': 'str', 'default': 'external_repos'},
        'name': {'type': 'str'},
        'reposdir': {'type': 'str', 'default': '/etc/yum.repos.d'},
        'baseurl': {'type': 'str', 'default': 'https://example.com/epel'},
        'dest': {'type': 'str'},
        'state': {'type': 'str', 'default': 'present'}})

    repo = YumRepo(module)
    repo.add()
    assert repo.repofile.get('example', 'baseurl') == 'https://example.com/epel'

# Generated at 2022-06-13 06:34:53.726920
# Unit test for method save of class YumRepo
def test_YumRepo_save():
    module = AnsibleModule({'dest': 'dest'})
    repo = YumRepo(module)
    repo.repofile = configparser.RawConfigParser()
    repo.repofile.add_section('test')
    repo.repofile.set('test', 'key1', 'value1')
    repo.repofile.set('test', 'key2', 'value2')
    repo.save()
    assert os.path.isfile('dest') is True
    os.remove('dest')
    assert os.path.isfile('dest') is False



# Generated at 2022-06-13 06:35:04.587730
# Unit test for method add of class YumRepo
def test_YumRepo_add():
    # pylint: disable=protected-access

    repo_file = configparser.RawConfigParser()

    repoid = 'epel'
    params = {
        'baseurl': 'https://download.fedoraproject.org/pub/epel/7/$basearch',
        'description': 'Extra Packages for Enterprise Linux 7 - $basearch',
        'enabled': 1,
        'file': 'external_repos',
        'gpgcheck': 0,
        'gpgkey': 'file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7',
        'name': 'Extra Packages for Enterprise Linux 7 - $basearch',
        'reposdir': '/etc/yum.repos.d',
    }

    yumrepo = YumRepo(None)

# Generated at 2022-06-13 06:35:46.161492
# Unit test for method add of class YumRepo
def test_YumRepo_add():
    module = AnsibleModule({
        'action': 'present',
        'baseurl': 'http://localhost/',
        'name': 'example',
        'reposdir': 'tests/files/repos/',
        'state': 'present',
    })
    repo = YumRepo(module)
    repo.add()
    result = repo.dump()
    assert result == '[example]\nbaseurl = http://localhost/\nname = example\nstate = present\n\n'


# Generated at 2022-06-13 06:35:59.166725
# Unit test for constructor of class YumRepo

# Generated at 2022-06-13 06:36:03.945665
# Unit test for method save of class YumRepo
def test_YumRepo_save():
    # Prepare the mocks
    yum_repository = YumRepo()
    #yum_repository.params['dest'] = '/home/user/test.repo'
    #yum_repository.repofile = ['/home/user/test.repo']
    yum_repository.save()
    return False


# Generated at 2022-06-13 06:36:04.839239
# Unit test for constructor of class YumRepo
def test_YumRepo():
    assert YumRepo(None)


# Generated at 2022-06-13 06:36:08.081416
# Unit test for method remove of class YumRepo
def test_YumRepo_remove():
    # Create class object
    y = YumRepo(None)
    # Set class variable repofile
    y.repofile = configparser.RawConfigParser()
    # Call method remove
    y.remove()



# Generated at 2022-06-13 06:36:11.623275
# Unit test for method add of class YumRepo
def test_YumRepo_add():
    # pylint: disable=R0903
    class _module(object):
        params = None
        fail_json = None
    module = _module()
    yum_repo = YumRepo(module)
    yum_repo.add()


# Generated at 2022-06-13 06:36:21.342883
# Unit test for constructor of class YumRepo
def test_YumRepo():
    class FakeModule(object):
        params = {}

    class FakeAnsibleModule(object):
        fail_json = FakeModule
        _diff = False
        _ansible_verbosity = 0
        _ansible_no_log = False

    module = FakeModule()

# Generated at 2022-06-13 06:36:28.292662
# Unit test for method dump of class YumRepo
def test_YumRepo_dump():
    module = AnsibleModule({})
    yum = YumRepo(module)
    yum.repofile = configparser.RawConfigParser()
    yum.repofile.add_section('repo_one')
    yum.repofile.set('repo_one', 'name', 'repo_one')
    yum.repofile.set('repo_one', 'priority', 99)
    yum.repofile.add_section('repo_two')
    yum.repofile.set('repo_two', 'name', 'repo_two')
    yum.repofile.set('repo_two', 'priority', 1)

# Generated at 2022-06-13 06:36:35.746083
# Unit test for method remove of class YumRepo
def test_YumRepo_remove():
    module = AnsibleModule(argument_spec={})
    yum_repo_instance = YumRepo(module)
    test_object = configparser.RawConfigParser()
    test_object.add_section('test_section')
    test_object.set('test_section', 'test_param', 'test_value')
    yum_repo_instance.repofile = test_object
    yum_repo_instance.section = 'test_section'
    yum_repo_instance.remove()
    assert yum_repo_instance.repofile.has_section('test_section') == False


# Generated at 2022-06-13 06:36:47.440698
# Unit test for method save of class YumRepo
def test_YumRepo_save():
    module = AnsibleModule({
        'reposdir': '/tmp/repos',
        'file': 'test',
        'repoid': 'myrepoid',
        'baseurl': 'https://my.repo.com'
    })

    # Create a repo instance
    yum_repository = YumRepo(module)
    yum_repository.add()
    yum_repository.save()

    # Check if repo file was created
    assert os.path.isfile('/tmp/repos/test.repo')

    # Remove repo file
    os.remove('/tmp/repos/test.repo')


# Generated at 2022-06-13 06:38:00.434527
# Unit test for method add of class YumRepo
def test_YumRepo_add():
    yum_repo_module_args = dict(
        name='epel',
        description='EPEL YUM repo',
        baseurl='https://download.fedoraproject.org/pub/epel/$releasever/$basearch/',
        gpgcheck=True,
        gpgkey='https://dl.fedoraproject.org/pub/epel/RPM-GPG-KEY-EPEL-7'
    )

    m = AnsibleModule(
        argument_spec=yum_repo_module_args,
        supports_check_mode=True
    )

    yum_repo = YumRepo(m)
    yum_repo.add()

    # Check data

# Generated at 2022-06-13 06:38:12.801672
# Unit test for method dump of class YumRepo
def test_YumRepo_dump():
    repofile_ini = configparser.RawConfigParser()
    repofile_ini.add_section('epel')
    repofile_ini.add_section('base')
    repofile_ini.set('epel', 'name', 'EPEL YUM repo')
    repofile_ini.set('base', 'name', 'Base YUM repo')

    expected = ("[base]\nname = Base YUM repo\n\n"
                "[epel]\nname = EPEL YUM repo\n\n")

    yum_repo = YumRepo(None)
    yum_repo.repofile = repofile_ini
    assert yum_repo.dump() == expected


# Generated at 2022-06-13 06:38:18.732654
# Unit test for method dump of class YumRepo
def test_YumRepo_dump():
    module = AnsibleModule({})
    yum_repo = YumRepo(module)

    yum_repo.repofile.read("tests/unit/modules/yum_repository_test.conf")


# Generated at 2022-06-13 06:38:31.784162
# Unit test for method remove of class YumRepo
def test_YumRepo_remove():
    yumrepo = YumRepo(None)
    yumrepo.repofile.add_section('repo_test')
    yumrepo.repofile.set('repo_test', 'a', 'b')
    yumrepo.repofile.set('repo_test', 'c', 'd')

    yumrepo.repofile.add_section('repo_test_2')
    yumrepo.repofile.set('repo_test_2', 'a', 'b')
    yumrepo.repofile.set('repo_test_2', 'c', 'd')

    yumrepo.repofile.add_section('repo_test_3')

# Generated at 2022-06-13 06:38:41.769394
# Unit test for method dump of class YumRepo
def test_YumRepo_dump():
    sample_input = '''
[test-section]
a = 1
b = 2
c = 3

[test-section2]
c = 3
b = 2
a = 1
'''

    sample_output = '''
[test-section]
a = 1
b = 2
c = 3

[test-section2]
a = 1
b = 2
c = 3
'''

    module = AnsibleModule(argument_spec={
        'dest': {'type': 'path'},
        'reposdir': {'type': 'path'},
    })
    obj = YumRepo(module)
    obj.repofile.read_string(sample_input)

    assert obj.dump() == sample_output



# Generated at 2022-06-13 06:38:47.781231
# Unit test for method add of class YumRepo
def test_YumRepo_add():
    yrepo = YumRepo()

    yrepo.params = {
        'repoid': 'epel',
        'baseurl': 'https://download.fedoraproject.org/pub/epel/$releasever/$basearch/',
        'gpgcheck': False,
        'dest': './',
        'name': 'EPEL YUM repo'}
    yrepo.repofile.add_section('other-repo')
    yrepo.repofile.set('other-repo', 'name', "Other YUM repo")
    yrepo.repofile.set('other-repo', 'baseurl', "http://example.com/repo/")

    # Add new repo to the list
    yrepo.add()

    assert not yrepo.repofile.has_section

# Generated at 2022-06-13 06:39:00.033947
# Unit test for constructor of class YumRepo
def test_YumRepo():
    # Check the repo directory does not exist
    check = YumRepo(AnsibleModule(
        argument_spec=dict(
            repoid='test-repoid',
            baseurl='https://some.url/for/$releasever',
            reposdir='/test/path')))
    assert check.module.fail_json.called_once
    # Check the repo file does not exist
    check = YumRepo(AnsibleModule(
        argument_spec=dict(
            repoid='test-repoid',
            baseurl='https://some.url/for/$releasever',
            file='test-repoid-file',
            reposdir='/etc/yum.repos.d')))
    assert not check.repofile.sections()



# Generated at 2022-06-13 06:39:07.307303
# Unit test for method remove of class YumRepo
def test_YumRepo_remove():
    module = AnsibleModule(
        argument_spec={
            'name': dict(type='str', required=True)
        }
    )

    # class variable module
    YumRepo.module = module

    # class variable repofile
    YumRepo.repofile = configparser.RawConfigParser()

    # Read the repo file if it exists
    YumRepo.repofile.read(['tests/test.repo'])

    # Initialization
    yum_repo = YumRepo(module)

    # Returned value
    ret = 0

    # Remove repo
    yum_repo.remove()

    # Create returned values
    results = {}
    results['changed'] = 1
    results['repo'] = yum_repo.section
    results['state'] = 'absent'

# Generated at 2022-06-13 06:39:15.294643
# Unit test for method dump of class YumRepo
def test_YumRepo_dump():
    yum_repo_instance = YumRepo("mocked_module")

    yum_repo_instance.repofile.add_section("section1")
    yum_repo_instance.repofile.set("section1", "key1", "value1")
    yum_repo_instance.repofile.set("section1", "key2", "value2")

    yum_repo_instance.repofile.add_section("section2")
    yum_repo_instance.repofile.set("section2", "key1", "value1")
    yum_repo_instance.repofile.set("section2", "key2", "value2")


# Generated at 2022-06-13 06:39:21.817052
# Unit test for method save of class YumRepo
def test_YumRepo_save():
  import tempfile
  import os

  filename = os.path.join(tempfile.mkdtemp(), 'test.repo')
  assert(not os.path.isfile(filename))

  params = dict(path=None, state='present', file='test', repoid='test')
  # Create an empty object
  obj = YumRepo(None)
  obj.params = params
  # Now create the file
  obj.save()

  assert(os.path.isfile(filename))

  # Remove the file
  os.remove(filename)
