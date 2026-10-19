

# Generated at 2022-06-13 04:41:45.289025
# Unit test for method run of class YumDnf
def test_YumDnf_run():
    class TestYumDnf(YumDnf):
        def __init__(self, module):
            self.module = module
            super(TestYumDnf, self).__init__(module)
        def is_lockfile_pid_valid(self):
            return True
  
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(yumdnf_argument_spec)
    yumdnf = TestYumDnf(module)
    yumdnf.run()


# Generated at 2022-06-13 04:41:46.525769
# Unit test for method run of class YumDnf
def test_YumDnf_run():
    module = AnsibleModule(argument_spec=dict())
    y = YumDnf(module)
    rc = y.run()
    assert rc == (False, '', {})


# Generated at 2022-06-13 04:41:54.865792
# Unit test for method listify_comma_sep_strings_in_list of class YumDnf
def test_YumDnf_listify_comma_sep_strings_in_list():
    some_list = [
        'bash-completion, vim-minimal',
        'openssl.x86_64',
        '',
        'rpcbind',
        'dumb-init, util-linux-user',
        'nginx, httpd'
    ]
    expected_list = ['bash-completion', ' vim-minimal', 'openssl.x86_64', 'rpcbind', 'dumb-init', ' util-linux-user', 'nginx', ' httpd']

    yd = YumDnf(None)

    list_after_apply = yd.listify_comma_sep_strings_in_list(some_list)

    assert list_after_apply == expected_list

# Generated at 2022-06-13 04:42:05.746246
# Unit test for method is_lockfile_pid_valid of class YumDnf
def test_YumDnf_is_lockfile_pid_valid():
    from ansible.module_utils.yum_dnf import YumDnf
    from moto import mock_cloudformation
    from ansible.module_utils.ec2 import AnsibleAWSError, HAS_BOTO3, boto3_conn, camel_dict_to_snake_dict
    import traceback
    import os
    print('Test YumDnf_is_lockfile_pid_valid')

# Generated at 2022-06-13 04:42:13.669562
# Unit test for constructor of class YumDnf
def test_YumDnf():
    '''
    Constructor of YumDnf initializes the following variables and makes sure that
    the state is set to absent if the autoremove is set to True.
    It also makes sure that the autoremove is set to False if the state is set to present.

    It also makes sure that the disablerepo and enablerepo are in the form of list if
    the input is in the form of string.

    It also makes sure that the name is a list if the input is a string or a comma separated string.

    It also checks if the lockfile is present and if it is, then it fails the test.
    '''
    import sys
    sys.path.append('/home/ashish/Ansible/ansible-modules-core/cloud/amazon/')

# Generated at 2022-06-13 04:42:19.241285
# Unit test for method listify_comma_sep_strings_in_list of class YumDnf
def test_YumDnf_listify_comma_sep_strings_in_list():
    yd = YumDnf(None)

    # listify_comma_sep_strings_in_list should take a list as a parameter and
    # return a list
    result = yd.listify_comma_sep_strings_in_list([])
    assert isinstance(result, list)

    # It should convert a comma separated string into a list
    result = yd.listify_comma_sep_strings_in_list(['one,two'])
    assert result == ['one', 'two']

    # It should leave a list of strings alone
    result = yd.listify_comma_sep_strings_in_list(['one', 'two'])
    assert result == ['one', 'two']

    # It should remove any strings from the original list that are in the form
    #

# Generated at 2022-06-13 04:42:23.226188
# Unit test for method run of class YumDnf
def test_YumDnf_run():
    obj = YumDnf("")
    try:
        obj.run()
    except NotImplementedError:
        assert True
    else:
        assert False



# Generated at 2022-06-13 04:42:30.917905
# Unit test for constructor of class YumDnf
def test_YumDnf():
    """
    Unit test for constructor of class YumDnf
    """
    import ansible.module_utils.basic as basic
    module = basic.AnsibleModule(argument_spec=yumdnf_argument_spec)
    y = YumDnf(module)
    assert y.allow_downgrade == module.params['allow_downgrade']
    assert y.autoremove == module.params['autoremove']
    assert y.bugfix == module.params['bugfix']
    assert y.cacheonly == module.params['cacheonly']
    assert y.conf_file == module.params['conf_file']
    assert y.disable_excludes == module.params['disable_excludes']
    assert y.disable_gpg_check == module.params['disable_gpg_check']
    assert y.disable_

# Generated at 2022-06-13 04:42:38.583355
# Unit test for method run of class YumDnf
def test_YumDnf_run():
    import unittest
    import ansible.module_utils.yum as yum_module_utils
    import ansible.module_utils.basic as basic_module_utils
    from ansible.module_utils.pycompat24 import get_exception
    from ansible.module_utils import six
    if six.PY2:
        module_utils = yum_module_utils
    else:
        module_utils = yum_module_utils.dnf_module_utils
    class TestException(Exception):
        '''Exception for testing module error exit'''
        pass

    class TestModule(object):
        '''Class used to mock the module parameter passed to run method in class YumDnf'''
        def __init__(self):
            self.params = {}
            self.check_mode = False

# Generated at 2022-06-13 04:42:39.460813
# Unit test for method run of class YumDnf
def test_YumDnf_run():
    assert True  # TODO



# Generated at 2022-06-13 04:43:04.921430
# Unit test for method run of class YumDnf
def test_YumDnf_run():
    """
    Test to check if the method run of class YumDnf throws
    NotImplementedError.
    """
    from ansible_collections.community.general.plugins.module_utils.package.yum import YumDnf
    yumdnf_obj = YumDnf()
    try:
        yumdnf_obj.run()
    except NotImplementedError:
        pass
    else:
        assert False, "YumDnf.run should raise NotImplementedError"


# Generated at 2022-06-13 04:43:09.081173
# Unit test for method listify_comma_sep_strings_in_list of class YumDnf
def test_YumDnf_listify_comma_sep_strings_in_list():
    test = ['a', 'b,c', 'd', 'e,f,g', 'h']
    expected = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    yum = YumDnf(None)
    actual = yum.listify_comma_sep_strings_in_list(test)
    assert expected == actual


# Generated at 2022-06-13 04:43:18.022733
# Unit test for method run of class YumDnf
def test_YumDnf_run():
    from ansible.module_utils.yum_dnf import YumDnf
    from ansible.module_utils.basic import AnsibleModule

    class MockModule(AnsibleModule):
        def __init__(self):
            self.params = {}
            self.fail_json = Mock()
            self.warn = Mock()

    module = MockModule()

    # Unit tests need to mock the abstract method run of class YumDnf.
    # Using the mock decorator from the Python unittest module to do that.
    @patch.object(YumDnf, 'run', return_value=None)
    def test_YumDnf_run(mock_YumDnf_run):
        yumdnf = YumDnf(module)
        yumdnf.run()
        mock

# Generated at 2022-06-13 04:43:25.030920
# Unit test for method listify_comma_sep_strings_in_list of class YumDnf
def test_YumDnf_listify_comma_sep_strings_in_list():
    some_list = ['a,b,c', 'c,b,a', 'a', 'b', 'c', 'c,b,a', 'a,b,c']
    expected_list = ['a', 'c', 'c', 'a', 'b', 'b', 'c', 'c', 'b', 'a', 'a', 'b', 'c', 'c', 'b', 'a', 'a', 'b', 'c']
    yum_dnf = YumDnf(None)
    new_list = yum_dnf.listify_comma_sep_strings_in_list(some_list)
    assert new_list == expected_list

# Generated at 2022-06-13 04:43:30.037750
# Unit test for method wait_for_lock of class YumDnf
def test_YumDnf_wait_for_lock():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.basic import AnsibleModule
    from ansible.modules.package.yum import YumModule
    from ansible.modules.package.dnf import DnfModule
    from ansible.module_utils.six.moves.urllib.parse import urlparse
    import tempfile

    # 1st: Create tempfile as a lockfile and create a class
    #  instance by calling the YumDnf class.
    lockfile = tempfile.mktemp()
    with open(lockfile, 'w'):
        pass

# Generated at 2022-06-13 04:43:40.580594
# Unit test for method listify_comma_sep_strings_in_list of class YumDnf
def test_YumDnf_listify_comma_sep_strings_in_list():
    '''
    Unit test for method listify_comma_sep_strings_in_list of class YumDnf
    '''
    
    yumdnf = YumDnf(None)
    assert yumdnf.listify_comma_sep_strings_in_list(['a,b,c']) == ['a', 'b', 'c']
    assert yumdnf.listify_comma_sep_strings_in_list(['a', 'b', 'c']) == ['a', 'b', 'c']
    assert yumdnf.listify_comma_sep_strings_in_list(['a,b,c', 'b', 'c', 'd']) == ['a', 'b', 'c', 'b', 'c', 'd']
    assert yum

# Generated at 2022-06-13 04:43:44.833197
# Unit test for method run of class YumDnf
def test_YumDnf_run():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict()
    )

    yumdnf = MyYumDnf(module)

    result = yumdnf.run()

    assert result == dict(
        changed=False,
        results=[],
        msg="Not implemented, you should implement this in your concrete class"
    )



# Generated at 2022-06-13 04:43:53.010162
# Unit test for method listify_comma_sep_strings_in_list of class YumDnf
def test_YumDnf_listify_comma_sep_strings_in_list():
    yum_dnf = YumDnf(None)
    results = yum_dnf.listify_comma_sep_strings_in_list([])
    assert results == []

    results = yum_dnf.listify_comma_sep_strings_in_list(['aaa'])
    assert results == ['aaa']

    results = yum_dnf.listify_comma_sep_strings_in_list(['aaa', 'bbb'])
    assert results == ['aaa', 'bbb']

    results = yum_dnf.listify_comma_sep_strings_in_list(['aaa', 'bbb,ccc'])
    assert results == ['aaa', 'bbb', 'ccc']

    results = yum_dnf.listify_comma_sep

# Generated at 2022-06-13 04:44:01.892397
# Unit test for method wait_for_lock of class YumDnf
def test_YumDnf_wait_for_lock():
    class YumDnfFakeTest(YumDnf):
        def is_lockfile_pid_valid(self):
            return True

        def pkg_mgr_name(self):
            return "dnf"

    class FakeModule(object):
        params = {
            'lock_timeout': 30,
            'pkg_mgr_name': 'dnf',
        }
        fail_json = lambda self, msg: msg
        changed = False

        def get_bin_path(self, *args, **kwargs):
            return '/bin/dnf'


    def mock_isfile(filename):
        return True

    def mock_can_access(filename):
        if filename == '/bin/dnf':
            return True
        return False

    # Create temporary lockfile

# Generated at 2022-06-13 04:44:03.830152
# Unit test for method run of class YumDnf
def test_YumDnf_run():
    with pytest.raises(NotImplementedError):
        p = YumDnf(module=None)
        p.run()


# Generated at 2022-06-13 04:44:39.674174
# Unit test for method wait_for_lock of class YumDnf
def test_YumDnf_wait_for_lock():
    class MyYumDnf(YumDnf):
        pkg_mgr_name = 'mockyum'

    mock_module = get_mock_module()

    yum = MyYumDnf(mock_module)

    temp_dir = tempfile.mkdtemp()
    temp_dir_in_usage = os.path.join(temp_dir, 'in-usage')
    os.mkdir(temp_dir_in_usage)

    yum.lockfile = os.path.join(temp_dir_in_usage, 'yum.pid')
    yum.lock_timeout = 0

    # check lockfile is present and return
    yum._is_lockfile_present = MagicMock()
    yum._is_lockfile_present.return_value = True
    yum

# Generated at 2022-06-13 04:44:46.710316
# Unit test for constructor of class YumDnf
def test_YumDnf():
    module_args = dict(
        name='cowsay',
        state='present'
    )
    module = MockModule(argument_spec=yumdnf_argument_spec, **module_args)
    yum = YumDnf(module)
    assert yum.names == ['cowsay']
    assert yum.state == 'present'
    assert yum.lockfile == '/var/run/yum.pid'

    module = MockModule(argument_spec=yumdnf_argument_spec, **dict(
        name=['cowsay', 'httpd'],
        state='present'
    ))
    yum = YumDnf(module)
    assert yum.names == ['cowsay', 'httpd']


# Generated at 2022-06-13 04:44:51.348851
# Unit test for method listify_comma_sep_strings_in_list of class YumDnf
def test_YumDnf_listify_comma_sep_strings_in_list():
    from ansible.module_utils.basic import AnsibleModule
    yumdnf_module = YumDnf(AnsibleModule({}))
    test_list = ['test', 'test1,test2,test3', 'test4,test5', 'test6']
    expected_list = ['test', 'test1', 'test2', 'test3', 'test4', 'test5', 'test6']
    assert yumdnf_module.listify_comma_sep_strings_in_list(test_list) == expected_list
    # test_list = ['', '', ''] doesn't work as expected because current code
    # doesn't check if some string doesn't contain ","
    test_list = ["", "", ""]
    expected_list = []
    assert yumdnf_module.listify_

# Generated at 2022-06-13 04:44:57.649271
# Unit test for method run of class YumDnf
def test_YumDnf_run():
    with tempfile.TemporaryDirectory() as temp_dir:
        os.chdir(temp_dir)
        try:
            YumDnf(None).run()
        except NotImplementedError:
            pass
        except Exception as e:
            raise AssertionError('Exception raised: %s' % to_native(e))
        else:
            raise AssertionError('No exception raised')

# Generated at 2022-06-13 04:45:03.260440
# Unit test for method wait_for_lock of class YumDnf
def test_YumDnf_wait_for_lock():
    mock_module = FakeAnsibleModule(
        argument_spec=dict(
            lock_timeout=dict(type='int', default=30)
        )
    )
    yum = YumDnf(mock_module)

    yum.wait_for_lock()
    assert yum.lock_timeout == 30


# Generated at 2022-06-13 04:45:08.143325
# Unit test for constructor of class YumDnf
def test_YumDnf():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec=yumdnf_argument_spec,
                           supports_check_mode=True)
    ym = YumDnf(module)
    assert ym.allow_downgrade is False
    assert ym.autoremove is False
    assert ym.bugfix is False
    assert ym.cacheonly is False
    assert ym.conf_file is None
    assert ym.disable_excludes is None
    assert ym.disable_gpg_check is False
    assert ym.disable_plugin == []
    assert ym.disablerepo == []
    assert ym.download_only is False
    assert ym.download_dir is None
    assert ym.enable_plugin == []
    assert ym

# Generated at 2022-06-13 04:45:18.722613
# Unit test for method listify_comma_sep_strings_in_list of class YumDnf
def test_YumDnf_listify_comma_sep_strings_in_list():
    """
    unit test for method listify_comma_sep_strings_in_list of class YumDnf
    """
    from ansible import context
    from ansible.module_utils.yumdndf import YumDnf

    class TestModule:
        def fail_json(self, **args):
            pass

    ansible_contexts = context.CLIContext()

    test_YumDnf = YumDnf(TestModule())

    assert test_YumDnf.listify_comma_sep_strings_in_list([]) == []
    assert test_YumDnf.listify_comma_sep_strings_in_list(['']) == []
    assert test_YumDnf.listify_comma_sep_strings_in_list

# Generated at 2022-06-13 04:45:27.313856
# Unit test for method wait_for_lock of class YumDnf
def test_YumDnf_wait_for_lock():
    yd = YumDnf(dict())
    yd.lockfile = tempfile.NamedTemporaryFile(mode='w')
    yd.lock_timeout = 5
    
    # Method _is_lockfile_present should return True as the lockfile is present
    assert yd._is_lockfile_present() == True
    yd.wait_for_lock()
    # After waiting for 5 seconds, the lockfile should be gone 
    assert yd._is_lockfile_present() != True

    

# Generated at 2022-06-13 04:45:39.621327
# Unit test for method wait_for_lock of class YumDnf
def test_YumDnf_wait_for_lock():
    class MockModule:
        def fail_json(self, msg, results):
            pass

    class FakeLockFile:
        def __init__(self, file_exists=True):
            self.file_exists = file_exists

        def __enter__(self):
            pass

        def __exit__(self, type, value, traceback):
            pass

        def is_lockfile_pid_valid(self):
            return self.file_exists

        def is_lockfile_present(self):
            return self.file_exists

    class FakeYumDnf(YumDnf):
        def __init__(self, module, is_lockfile_present=None):
            self.module = module
            self.lockfile = tempfile.mktemp()
            self.is_lockfile_pid_

# Generated at 2022-06-13 04:45:43.054304
# Unit test for method run of class YumDnf
def test_YumDnf_run():
    y = YumDnf('module')
    with pytest.raises(NotImplementedError):
        y.run()


# Generated at 2022-06-13 04:46:33.655792
# Unit test for method wait_for_lock of class YumDnf
def test_YumDnf_wait_for_lock():

    class MockModule(object):
        def fail_json(self, results, msg):
            raise Exception(msg)

    class MockOsPathIsFile(object):
        def __init__(self, path):
            self.path = path

        def __call__(self, path):
            if path == self.path:
                return True
            else:
                return False

    class MockGlob(object):
        def __call__(self, path):
            return [path]

    def is_lockfile_valid():
        return True

    def is_lockfile_invalid():
        return False

    # Test if we raise upon timeout
    YumDnfInstance = YumDnf(MockModule())
    YumDnfInstance.lockfile = tmp_lockfile
    YumDnfInstance.lock_timeout

# Generated at 2022-06-13 04:46:42.603149
# Unit test for constructor of class YumDnf
def test_YumDnf():
    import ansible.modules.packaging.os.yum as yum
    import ansible.module_utils.yum as yum_module_utils
    import ansible.module_utils.basic as basic

    module = yum.Yum(
        basic.AnsibleModule(
            argument_spec=yumdnf_argument_spec,
            supports_check_mode=True
        )
    )
    assert module.module.check_mode is True
    assert module.module.params['bugfix'] is False
    assert module.module.params['disable_gpg_check'] is False
    assert module.module.params['update_only'] is False

    # Modify arguments and test again
    module.module.params['bugfix'] = True
    module.module.params['disable_gpg_check'] = True
    module

# Generated at 2022-06-13 04:46:53.230433
# Unit test for constructor of class YumDnf
def test_YumDnf():
    # Positive test
    module = object()

# Generated at 2022-06-13 04:47:05.961737
# Unit test for method wait_for_lock of class YumDnf
def test_YumDnf_wait_for_lock():
    # !/usr/bin/python
    import shutil
    import os
    import time
    import pytest
    import ansible.module_utils.yum
    lockfile = ['/var/run/yum.pid']
    lock_timeout = 2

    def _is_lockfile_present():
        return (os.path.isfile(lockfile[0]) or glob.glob(lockfile[0]))
    # Create lockfile and check wait_for_lock works with timeout 0
    # and the lockfile is alive
    f = open(lockfile[0], 'w')
    assert _is_lockfile_present()
    ansible.module_utils.yum.YumDnf._is_lockfile_present = _is_lockfile_present
    ansible.module_utils.yum.YumD

# Generated at 2022-06-13 04:47:18.330802
# Unit test for method listify_comma_sep_strings_in_list of class YumDnf
def test_YumDnf_listify_comma_sep_strings_in_list():
    yumdnf_object = YumDnf(None) # instance of the class with None parameter
    assert yumdnf_object.listify_comma_sep_strings_in_list(['a', 'b', 'c,d']) == ['a', 'b', 'c', 'd']
    assert yumdnf_object.listify_comma_sep_strings_in_list(['a', 'b', 'c,d,e,f']) == ['a', 'b', 'c', 'd', 'e', 'f']
    assert yumdnf_object.listify_comma_sep_strings_in_list(['a', 'b', 'c,d,e,f,g']) == ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# Generated at 2022-06-13 04:47:24.841030
# Unit test for method listify_comma_sep_strings_in_list of class YumDnf
def test_YumDnf_listify_comma_sep_strings_in_list():
    # test with a list of strings that don't need modification
    yd = YumDnf(None)
    mylist = yd.listify_comma_sep_strings_in_list(['abc', 'def'])
    assert mylist == ['abc', 'def']
    # test with a list that has a comma separated string in it
    mylist = yd.listify_comma_sep_strings_in_list(['abc', 'def,ghi,jkl'])
    assert mylist == ['abc', 'def', 'ghi', 'jkl']
    # test with a list that has two comma separated strings in it
    mylist = yd.listify_comma_sep_strings_in_list(['abc', 'def,ghi', 'jkl,mno'])
    assert mylist

# Generated at 2022-06-13 04:47:34.883138
# Unit test for method listify_comma_sep_strings_in_list of class YumDnf
def test_YumDnf_listify_comma_sep_strings_in_list():
    module = AnsibleModule({})
    yum_dnf_obj = YumDnf(module)

    # Test for basic functionality
    assert yum_dnf_obj.listify_comma_sep_strings_in_list(['test1,test2']) == [
        'test1', 'test2']

    # Test for no comma separated entries
    assert yum_dnf_obj.listify_comma_sep_strings_in_list(['test1']) == ['test1']

    # Test for blank entry
    assert yum_dnf_obj.listify_comma_sep_strings_in_list(['']) == []

    # Test for empty list
    assert yum_dnf_obj.listify_comma_sep_strings_in_list([]) == []

   

# Generated at 2022-06-13 04:47:43.222367
# Unit test for method listify_comma_sep_strings_in_list of class YumDnf
def test_YumDnf_listify_comma_sep_strings_in_list():
    # Test 1
    # original list: ['yum', 'yaml-devel,python-jinja2,python-psutil']
    # expected list: ['yum', 'yaml-devel', 'python-jinja2', 'python-psutil']
    list1 = ['yum', 'yaml-devel,python-jinja2,python-psutil']
    yum_dnf = YumDnf(None)
    assert yum_dnf.listify_comma_sep_strings_in_list(list1) == ['yum', 'yaml-devel', 'python-jinja2', 'python-psutil'], yum_dnf.listify_comma_sep_strings_in_list(list1)

    # Test 2
    # original list: ['yum', 'y

# Generated at 2022-06-13 04:47:56.040966
# Unit test for method is_lockfile_pid_valid of class YumDnf
def test_YumDnf_is_lockfile_pid_valid():
    tmp_dir = tempfile.mkdtemp()
    lockfile = os.path.join(tmp_dir, 'lock-file')
    pidfile = os.path.join(tmp_dir, 'pid-file')
    open(lockfile, 'w').close()

    def is_lockfile_pid_valid():
        return True

    y = YumDnf(None)
    y.lockfile = lockfile

    assert y._is_lockfile_present() is True

    os.remove(lockfile)

    y.lockfile = pidfile
    open(pidfile, 'w').close()

    assert y._is_lockfile_present() is True
    os.remove(pidfile)

    y.lockfile = None
    y.is_lockfile_pid_valid = is_lockfile_pid_valid
   

# Generated at 2022-06-13 04:48:09.100672
# Unit test for method wait_for_lock of class YumDnf
def test_YumDnf_wait_for_lock():
    import unittest
    import sys

    # Fake classes to test wait_for_lock()
    class module_fake(object):

        def __init__(self, name=None, **kwargs):
            self.params = self._load_params(name, **kwargs)

        def _load_params(self, name, **kwargs):
            params = dict(
                list=None,
                lock_timeout=30,
            )
            params.update(kwargs)
            return params

        def fail_json(self, msg, results=None):
            raise Exception(msg)

    class YumDnf_fake(YumDnf):

        def __init__(self, module):
            self.module = module
            self.lockfile = '/var/run/yum.pid'
            self.lock_timeout

# Generated at 2022-06-13 04:49:51.432987
# Unit test for method run of class YumDnf
def test_YumDnf_run():
    """
    Make sure method .run() throws an exception
    """
    module = AnsibleModule({}, check_invalid_arguments=False)
    yum_dnf = YumDnf(module)
    with pytest.raises(NotImplementedError):
        yum_dnf.run()



# Generated at 2022-06-13 04:50:00.571763
# Unit test for method wait_for_lock of class YumDnf
def test_YumDnf_wait_for_lock():
    setattr(YumDnf, '_is_lockfile_present', lambda self: False)

    module = dict()
    module['params'] = dict()
    module['params']['lock_timeout'] = 0
    module['fail_json'] = lambda self, msg: msg
    setattr(YumDnf, 'module', module)

    yumdnf_obj = YumDnf(module)
    result_msg = yumdnf_obj.wait_for_lock()
    assert result_msg is None

    setattr(YumDnf, '_is_lockfile_present', lambda self: True)

    module = dict()
    module['params'] = dict()
    module['params']['lock_timeout'] = 1
    setattr(YumDnf, 'module', module)



# Generated at 2022-06-13 04:50:04.870312
# Unit test for method is_lockfile_pid_valid of class YumDnf
def test_YumDnf_is_lockfile_pid_valid():
    try:
        result = YumDnf.is_lockfile_pid_valid()
    except NotImplementedError:
        pass
    else:
        raise Exception("test failed")



# Generated at 2022-06-13 04:50:11.307939
# Unit test for constructor of class YumDnf
def test_YumDnf():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec=yumdnf_argument_spec)
    ydf = YumDnf(module)
    assert ydf.allow_downgrade is False
    assert ydf.autoremove is False
    assert ydf.bugfix is False
    assert ydf.cacheonly is False
    assert ydf.conf_file is None
    assert ydf.disable_excludes is None
    assert ydf.disable_gpg_check is False
    assert ydf.disable_plugin == []
    assert ydf.disablerepo == []
    assert ydf.download_only is False
    assert ydf.download_dir is None
    assert ydf.enable_plugin == []
    assert ydf.enablerepo == []
    assert ydf

# Generated at 2022-06-13 04:50:21.960739
# Unit test for method listify_comma_sep_strings_in_list of class YumDnf
def test_YumDnf_listify_comma_sep_strings_in_list():
    class TestYumDnf(YumDnf):
        def is_lockfile_pid_valid(self):
            pass

    test_obj = TestYumDnf(None)
    list_to_test = ['string1', 'string2', 'string3']
    assert test_obj.listify_comma_sep_strings_in_list(list_to_test) == ['string1', 'string2', 'string3']
    list_to_test = ['string1,string2', 'string3']
    assert test_obj.listify_comma_sep_strings_in_list(list_to_test) == ['string1', 'string2', 'string3']
    assert test_obj.listify_comma_sep_strings_in_list([""]) == []
    list_

# Generated at 2022-06-13 04:50:29.315542
# Unit test for method wait_for_lock of class YumDnf
def test_YumDnf_wait_for_lock():
    class DummyModule(object):
        def __init__(self, **kwargs):
            self.params = kwargs

    def is_lockfile_valid(foo):
        return True

    def is_lockfile_pid_valid(foo):
        return True

    class DummyYumDnf(YumDnf):
        def __init__(self, module):
            super(DummyYumDnf, self).__init__(module)
            self.lockfile = 'foo'
            self.pkg_mgr_name = 'dummy_pkg_mgr'

        def is_lockfile_pid_valid(self):
            return is_lockfile_pid_valid(self)

        def run(self):
            return


# Generated at 2022-06-13 04:50:38.324767
# Unit test for method listify_comma_sep_strings_in_list of class YumDnf
def test_YumDnf_listify_comma_sep_strings_in_list():
    import sys
    import traceback
    import io
    import os
    import unittest

    class TestYumDnfParseHelper(YumDnf):
        def __init__(self, module):
            super(TestYumDnfParseHelper, self).__init__(module)

        def is_lockfile_pid_valid(self):
            return False

    class TestYumDnf(unittest.TestCase):
        def setUp(self):
            self.module = type('module', (object,), {})
            self.module.params = {}
            self.module.fail_json = lambda **kwargs: sys.exit(1)

            self.test_obj = TestYumDnfParseHelper(self.module)


# Generated at 2022-06-13 04:50:49.306146
# Unit test for constructor of class YumDnf
def test_YumDnf():
    from ansible.module_utils.basic import AnsibleModule

# Generated at 2022-06-13 04:51:00.241751
# Unit test for method listify_comma_sep_strings_in_list of class YumDnf
def test_YumDnf_listify_comma_sep_strings_in_list():
    #test_list = ["foo", "bar", "baz"]
    y = YumDnf(None)
    assert y.listify_comma_sep_strings_in_list(["foo", "bar", "baz"]) == ["foo", "bar", "baz"]      # 1
    assert y.listify_comma_sep_strings_in_list(["foo,bar,baz"]) == ["foo", "bar", "baz"]            # 2
    assert y.listify_comma_sep_strings_in_list(["foo, bar, baz"]) == ["foo", "bar", "baz"]         # 3

# Generated at 2022-06-13 04:51:10.255019
# Unit test for constructor of class YumDnf