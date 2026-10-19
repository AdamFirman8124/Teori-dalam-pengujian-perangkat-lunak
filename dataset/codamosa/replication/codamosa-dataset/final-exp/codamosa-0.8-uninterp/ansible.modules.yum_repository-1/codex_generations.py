

# Generated at 2022-06-13 06:31:31.870936
# Unit test for method dump of class YumRepo
def test_YumRepo_dump():

    import tempfile
    import shutil
    import os


# Generated at 2022-06-13 06:31:40.463865
# Unit test for method save of class YumRepo
def test_YumRepo_save():
    resp = None
    dest_tmp = '/tmp/yum_repository_test.repo'
    module = AnsibleModule(argument_spec=dict(
            file='yum_repository_test',
            state='present',
            reposdir='/tmp/',
            name='test',
            params=dict(
                baseurl='http://download.fedoraproject.org/pub/epel/7/x86_64/',
                enabled=False
            ),
            dest=dest_tmp
        ),
        check_invalid_arguments=False,
        supports_check_mode=True,
        bypass_checks=True
    )

# Generated at 2022-06-13 06:31:41.542880
# Unit test for method save of class YumRepo
def test_YumRepo_save():
    pass


# Generated at 2022-06-13 06:31:47.740890
# Unit test for constructor of class YumRepo
def test_YumRepo():
    module = AnsibleModule(argument_spec={
        "baseurl": {"required": False, "type": "str"},
        "file": {"default": "__testrepo__", "type": "str"},
        "repoid": {"default": "testrepo", "type": "str"},
        "reposdir": {"required": True, "type": "path"},
    })

    test = YumRepo(module)

    module.exit_json(changed=False, repo=test, state='present')


# Generated at 2022-06-13 06:31:49.013103
# Unit test for constructor of class YumRepo
def test_YumRepo():
    """Basic class instantiation test."""
    module = AnsibleModule(argument_spec={})
    repo = YumRepo(module)


# Generated at 2022-06-13 06:31:53.789856
# Unit test for function main

# Generated at 2022-06-13 06:32:04.206036
# Unit test for method dump of class YumRepo
def test_YumRepo_dump():
    repofile = configparser.RawConfigParser()
    repofile.add_section('foo')
    repofile.set('foo', 'bar', 'foo')
    repofile.set('foo', 'baz', 'foo1')
    repofile.add_section('bar')
    repofile.set('bar', 'asd', 'foo2')
    repofile.set('bar', 'what', 'foo3')

    y = YumRepo(None)
    y.repofile = repofile

    assert y.dump() == '[bar]\nasd = foo2\nwhat = foo3\n\n[foo]\nbar = foo\nbaz = foo1\n\n'



# Generated at 2022-06-13 06:32:10.273319
# Unit test for method add of class YumRepo
def test_YumRepo_add():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec={
        'repoid': {'type': 'str'},
        'includepkgs': {'type': 'list'}
    })
    repo = YumRepo(module)
    repo.params['repoid'] = 'repo1'
    repo.params['includepkgs'] = ['pkg1', 'pkg2', 'pkg3*']
    repo.add()
    assert repo.repofile.get('repo1', 'includepkgs') == 'pkg1 pkg2 pkg3*'



# Generated at 2022-06-13 06:32:23.988085
# Unit test for method save of class YumRepo
def test_YumRepo_save():
    class MyModule(object):
        def __init__(self):
            self.params = {'reposdir': 'tests/repo/', 'file': 'test_yum_repo_save'}
            self.fail_json = lambda **kwargs: None

    class MyConfigParser(object):
        def __init__(self):
            self.sections = []

        def has_section(self, section):
            return True if section in self.sections else False

        def remove_section(self, section):
            self.sections.remove(section)

        def add_section(self, section):
            self.sections.append(section)

        def write(self):
            repo_string = ""

            # Compose the repo file

# Generated at 2022-06-13 06:32:37.031431
# Unit test for function main
def test_main():
    # Put here a json output example of the yum_repository module
    result = {'changed': True,
                    'comment': 'Some comment',
                    'failed': False,
                    'name': 'username',
                    'repo': 'my_repo',
                    'state': 'present'}
    # Put here a description of what the function does
    module = AnsibleModule({'reposdir':['arg1', 'arg2'],
                            'name': ['arg1', 'arg2'],
                            'state': ['arg1', 'arg2'],
                            'file':['arg1', 'arg2'],
                            })

    # Update the result with an example of the function's output
    result.update({'comment': 'Some other comment'})

# Generated at 2022-06-13 06:33:01.960394
# Unit test for method add of class YumRepo
def test_YumRepo_add():
    module = AnsibleModule(argument_spec={
        "repoid": {"required": True},
        "description": {"required": False},
        "state": {"default": "present", "choices": ["present", "absent"]},
        "file": {"required": False, "default": "test"},
    })
    result = dict(
        changed=True,
        msg="",
    )
    yum_repo = YumRepo(module)

    yum_repo.add()

    result['msg'] = yum_repo.dump()

    module.exit_json(**result)



# Generated at 2022-06-13 06:33:15.675677
# Unit test for method add of class YumRepo
def test_YumRepo_add():
    from ansible.module_utils.six import StringIO
    from ansible.module_utils.basic import AnsibleModule

    class AnsibleModuleFake(AnsibleModule):
        # Public dictionary of parameters passed to the module
        params = {}


# Generated at 2022-06-13 06:33:30.638199
# Unit test for constructor of class YumRepo
def test_YumRepo():
    module_args = {
        'repoid': 'test_repoid',
        'file': 'test_repofile',
        'baseurl': 'test_baseurl',
        'name': 'test_name'
    }

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)
    yrepo = YumRepo(module)

    assert yrepo.section == 'test_repoid'
    assert yrepo.params['repoid'] == 'test_repoid'
    assert yrepo.params['file'] == 'test_repofile'
    assert yrepo.params['baseurl'] == 'test_baseurl'
    assert yrepo.params['name'] == 'test_name'

    # We have to remove the created /tmp/test_repofile.

# Generated at 2022-06-13 06:33:36.899954
# Unit test for method save of class YumRepo
def test_YumRepo_save():
    import tempfile
    import os
    import shutil
    # Create temporary directory
    tmp = tempfile.mkdtemp()
    # Create repository
    y = YumRepo(AnsibleModule({'reposdir': tmp}))
    # Add repository
    y.add()
    # Save repository
    y.save()
    # Check if file exists
    assert os.path.isfile(os.path.join(tmp, 'yumrepo-test.repo'))
    # Remove temporary directory
    shutil.rmtree(tmp)

# Generated at 2022-06-13 06:33:38.694956
# Unit test for method save of class YumRepo
def test_YumRepo_save():
    assert False


# Generated at 2022-06-13 06:33:47.448892
# Unit test for method add of class YumRepo

# Generated at 2022-06-13 06:33:58.011522
# Unit test for function main
def test_main():
    # Test for simple present repo
    set_module_args({
        'name': 'ansible-test',
        'baseurl': 'http://example.com/centos/$releasever/$basearch/',
        'enabled': True,
        'gpgcheck': True,
        'gpgkey': ['http://example.com/pub/RPM-GPG-KEY'],
    })
    result = main()
    assert result['changed']
    assert result['repo'] == 'ansible-test'
    assert result['state'] == 'present'

    # Test for simple absent repo

# Generated at 2022-06-13 06:34:09.575409
# Unit test for method save of class YumRepo
def test_YumRepo_save():
  """
  This unit test is written when there is no implementation of the method.
  It is used to write the implementation.
  The implementation of the method is written only when it is executed,
  and not when it is imported.
  This allows to perform the coverage of the implementation
  """
  from ansible.module_utils.basic import AnsibleModule
  from ansible.module_utils._text import to_native
  m = AnsibleModule(argument_spec=dict(
    params = dict()
  ))
  y = YumRepo(m)

# Generated at 2022-06-13 06:34:22.613707
# Unit test for method add of class YumRepo
def test_YumRepo_add():
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(
                default='present',
                choices=['present', 'absent']),
            reposdir=dict(
                default='/etc/yum.repos.d'),
            file=dict(
                default='test_yum_repo.repo'),
            baseurl=dict(),
            gpgkey=dict(),
        )
    )
    repo = YumRepo(module=module)
    repo.add()
    repo_string = repo.dump()

    assert 'test_yum_repo.repo' in repo_string
    assert '[test_yum_repo]' in repo_string
    assert 'baseurl = None' in repo_string
    assert 'gpgkey = None' in repo_string


# Generated at 2022-06-13 06:34:32.454877
# Unit test for method dump of class YumRepo
def test_YumRepo_dump():
    module = AnsibleModule(name='repository', argument_spec={})
    obj_YumRepo = YumRepo(module)

    obj_YumRepo.repofile.add_section("test_section")
    obj_YumRepo.repofile.set("test_section", "test_key", "test_value")

    assert obj_YumRepo.dump() == "[test_section]\n\ntest_key = test_value\n\n\n"



# Generated at 2022-06-13 06:35:12.315703
# Unit test for method dump of class YumRepo
def test_YumRepo_dump():
    class MockModule(object):
        def __init__(self, params):
            self.params = params

    class MockConfigParser(object):
        def __init__(self, data):
            self.sections = [s for s in data]
            self.items = lambda x: data[x].items()

    # Section names should be ordered alphabetically
    data = {
        'first': {'a': 'b', 'c': 'd'},
        'second': {'f': 'g', 'h': 'i'}
    }

    configparser_obj = MockConfigParser(data)
    yum_repo = YumRepo(MockModule({'file': 'test_file'}))
    yum_repo.repofile = configparser_obj

# Generated at 2022-06-13 06:35:27.626921
# Unit test for method save of class YumRepo
def test_YumRepo_save():
    import pytest

    from ansible.modules.packaging.os.yum_repository import YumRepo

    repofile = configparser.RawConfigParser()
    repofile.add_section('test')
    repofile.set('test', 'foo', 'bar')

    yumrepo = YumRepo(module=None)
    yumrepo.repofile = repofile
    yumrepo.params = {'dest': '/dev/null'}

    # Add data
    save_repofile = configparser.RawConfigParser()
    save_repofile.read(yumrepo.params['dest'])
    assert save_repofile.sections() == []

    # Save
    yumrepo.save()

    # Check if the method added data
    save_repof

# Generated at 2022-06-13 06:35:32.747029
# Unit test for method dump of class YumRepo
def test_YumRepo_dump():
    module = AnsibleModule(argument_spec={})

    yumrepo = YumRepo(module)

    # Add a section
    yumrepo.repofile.add_section('test')
    # Add a parameter
    yumrepo.repofile.set('test', 'testparam', 'testvalue')

    # Get the dump
    output = yumrepo.dump()

    # Check the output
    assert output == '[test]\ntestparam = testvalue\n\n'



# Generated at 2022-06-13 06:35:35.365906
# Unit test for constructor of class YumRepo
def test_YumRepo():
    module = AnsibleModule({'file': 'test_file'}, check_invalid_arguments=False)
    repo = YumRepo(module)
    assert repo.repofile
    assert repo.repofile.sections() == []



# Generated at 2022-06-13 06:35:48.689333
# Unit test for method save of class YumRepo
def test_YumRepo_save():
    import base64
    import tempfile

    file_path = tempfile.mkstemp()[1]


# Generated at 2022-06-13 06:35:49.300550
# Unit test for method remove of class YumRepo
def test_YumRepo_remove():
    pass



# Generated at 2022-06-13 06:36:02.412425
# Unit test for function main
def test_main():
    import json
    import os
    from ansible.module_utils.six.moves.mock import mock_open, patch

    yumrepo_instance = YumRepo({})
    yumrepo_instance.repofile = configparser.RawConfigParser()
    yumrepo_instance.repofile.add_section('epel')
    yumrepo_instance.repofile.add_section('testing')
    yumrepo_instance.repofile.add_section('other')
    yumrepo_instance.repofile.add_section('ansible')

    yumrepo_instance.repofile.set('epel', 'name', 'name')
    yumrepo_instance.repofile.set('epel', 'baseurl', 'https..')
    yumrepo

# Generated at 2022-06-13 06:36:11.665669
# Unit test for constructor of class YumRepo
def test_YumRepo():
    # Create module and set params
    mod = AnsibleModule(
        argument_spec=dict(
            state=dict(
                choices=['present', 'absent'],
                default="present"
            ),
            name=dict(type='str'),
            file=dict(default='ansible.repo'),
            reposdir=dict(default='/etc/yum.repos.d'),
            description=dict(type='str'),
            enabled=dict(default=1, type='bool'),
            gpgcheck=dict(default=1, type='bool'),
            baseurl=dict(type='list'),
            metalink=dict(type='str'),
            mirrorlist=dict(type='str'),
        )
    )

    # Create constructor
    repo = YumRepo(mod)

    # Check whether the constructor sets the

# Generated at 2022-06-13 06:36:16.498575
# Unit test for method remove of class YumRepo
def test_YumRepo_remove():
    module = AnsibleModule(argument_spec={})
    # fake args
    module.params = {
        'repoid': 'test'
    }
    yumRepo = YumRepo(module)
    yumRepo.repofile.add_section('test')
    yumRepo.remove()
    assert yumRepo.repofile.has_section('test') == False


# Generated at 2022-06-13 06:36:24.059295
# Unit test for method add of class YumRepo
def test_YumRepo_add():
    import tempfile
    import shutil

    params = dict(
        file='test',
        repoid='test',
        baseurl='https://example.com',
    )

    # Create a temp directory where the repo file will be stored
    temp_dir = tempfile.mkdtemp()

    # Create module object with params
    module = AnsibleModule(argument_spec=dict(
        baseurl=dict(required=False, default=params['baseurl']),
        file=dict(default=params['file'], required=False),
        repoid=dict(default=params['repoid'], required=True),
        reposdir=dict(default=temp_dir),
    ))

    # Set standard module variables
    module.fail_json = lambda **kwargs: kwargs

# Generated at 2022-06-13 06:37:35.596940
# Unit test for method add of class YumRepo
def test_YumRepo_add():
    module = AnsibleModule(argument_spec={
        'baseurl': {'required': False, 'type': 'str'},
        'file': {"required": False, 'type': 'str'},
        'name': {"required": False, 'type': 'str'},
        'reposdir': {"required": False, 'type': 'path'}
    })
    yum_repo = YumRepo(module)
    yum_repo.params = {
        'baseurl': 'https://download.fedoraproject.org/pub/epel/$releasever/$basearch/',
        'file': 'external_repos',
        'name': 'epel',
        'reposdir': '/tmp'
    }
    yum_repo.add()
    yum_repo.save()

# Generated at 2022-06-13 06:37:44.465450
# Unit test for method add of class YumRepo
def test_YumRepo_add():
    new_repo = YumRepo(None)

    new_repo.repofile.add_section('test')
    new_repo.repofile.set('test', 'async', '0')
    new_repo.repofile.set('test', 'skip_if_unavailable', '1')
    new_repo.repofile.set('test', 'bandwidth', '2048')
    new_repo.repofile.set('test', 'baseurl', 'https://example.com')
    new_repo.repofile.set('test', 'cost', '14')
    new_repo.repofile.set('test', 'deltarpm_metadata_percentage', '100')

# Generated at 2022-06-13 06:37:49.917955
# Unit test for method dump of class YumRepo
def test_YumRepo_dump():
    # Test simple repo definition
    module = AnsibleModule({
        'name': 'epel',
        'file': 'test1',
        'reposdir': './test/rhel7_repo/',
        'baseurl': 'https://download.fedoraproject.org/pub/epel/$releasever/$basearch/',
        'enabled': '1'
    })
    repo = YumRepo(module)
    repo.add()
    assert repo.dump() == """[epel]
baseurl = https://download.fedoraproject.org/pub/epel/$releasever/$basearch/
enabled = 1
"""


# Generated at 2022-06-13 06:38:00.426916
# Unit test for method save of class YumRepo
def test_YumRepo_save():
    """
    Test for method save() of class YumRepo
    """
    from ansible.module_utils import basic
    from ansible.module_utils.basic import AnsibleModule
    from ansible_collections.ansible.community.tests.unit.compat import unittest
    from ansible_collections.ansible.community.tests.unit.compat.mock import patch

    response_d = {}
    response_d['section'] = 'section'
    response_d['baseurl'] = "http://baseurl"

    test_module = type('object', (object,), {'params': {'state': 'present', 'reposdir': '/tmp', 'dest': '/tmp/test.repo', 'file': 'test', 'baseurl': 'http://baseurl'}})

    fake_module = AnsibleModule

# Generated at 2022-06-13 06:38:06.763289
# Unit test for function main

# Generated at 2022-06-13 06:38:19.721498
# Unit test for constructor of class YumRepo
def test_YumRepo():
    # generate params to be used
    p = {}
    p['reposdir'] = "/tmp/ansible-test/yum-repos/reposdir"
    p['file'] = "testfile"
    p['repoid'] = "testrepoid"
    p['metalink'] = "http://www.example.com"

    # create a module
    m = AnsibleModule({
        'baseurl': '',
        'file': p['file'],
        'reposdir': p['reposdir'],
        'repoid': p['repoid'],
        'metalink': p['metalink'],
        'state': 'present'})

    # create the YumRepo() object
    my_yum_repo = YumRepo(m)

    assert my_yum_repo.section

# Generated at 2022-06-13 06:38:32.296828
# Unit test for method remove of class YumRepo
def test_YumRepo_remove():
    """
    Unit test for method remove of class YumRepo
    """
    module = AnsibleModule({})
    repofile = configparser.RawConfigParser()

    # Add section
    repofile.add_section("repo1")

    # Set options
    repofile.set("repo1", 'name', "repo1")
    repofile.set("repo1", 'baseurl', "https://download.fedoraproject.org/pub/epel/$releasever/$basearch/")

    # Add section
    repofile.add_section("repo2")

    # Set options
    repofile.set("repo2", 'name', "repo2")

# Generated at 2022-06-13 06:38:40.151626
# Unit test for constructor of class YumRepo
def test_YumRepo():
    mod = AnsibleModule({
        'name': 'epel',
        'file': 'testing',
        'reposdir': '/tmp/',
        'state': 'present',
        'baseurl': 'http://example.com/repo'
    })

    yumrepo = YumRepo(mod)

    assert yumrepo.params['dest'] == '/tmp/testing.repo'
    assert yumrepo.section == 'epel'
    assert not yumrepo.repofile.sections()



# Generated at 2022-06-13 06:38:46.910959
# Unit test for method add of class YumRepo
def test_YumRepo_add():

    from ansible.module_utils import basic
    from ansible.module_utils import six
    from ansible.module_utils._text import to_bytes


    class MockModule(object):

        def __init__(self, **kwargs):
            self.params = kwargs

        def fail_json(self, *args, **kwargs):
            self.exit_args = args
            self.exit_kwargs = kwargs
            raise Exception('FAIL')

    # Initialize mock module

# Generated at 2022-06-13 06:38:52.257001
# Unit test for constructor of class YumRepo
def test_YumRepo():
    set_module_args({
        'baseurl': 'http://localhost/repo',
        'name': 'repo-name',
        'state': 'present',
        'reposdir': 'tests/files/yum_repository',
        'file': 'file-name'})
