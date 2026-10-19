

# Generated at 2022-06-13 04:41:49.267802
# Unit test for method wait_for_lock of class YumDnf
def test_YumDnf_wait_for_lock():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.basic import AnsibleModule
    import os
    import shutil
    import tempfile

    my_temp_directory = tempfile.mkdtemp()
    my_symlinked_directory = os.path.join(my_temp_directory, "sym")
    my_symlinked_lockfile = os.path.join(my_symlinked_directory, 'yum.pid')
    os.symlink(my_symlinked_directory, my_symlinked_directory)
    os.path.isdir(my_symlinked_directory)


# Generated at 2022-06-13 04:41:57.124189
# Unit test for method wait_for_lock of class YumDnf
def test_YumDnf_wait_for_lock():
    import random, mock

    # no lockfile exists, normal exit
    y = YumDnf(mock.Mock())
    y._is_lockfile_present = mock.Mock(return_value=False)
    y.lock_timeout = 0
    y.wait_for_lock()

    # lockfile exists but timeout is set to 0
    y = YumDnf(mock.Mock())
    y._is_lockfile_present = mock.Mock(return_value=True)
    y.lock_timeout = 0
    y.wait_for_lock()

    # valid lockfile exists and timeout is set to 1 so test should pass
    y = YumDnf(mock.Mock())
    y._is_lockfile_present = mock.Mock(return_value=True)
    y

# Generated at 2022-06-13 04:42:01.894387
# Unit test for method run of class YumDnf
def test_YumDnf_run():
    assert 'object' == type(YumDnf).__name__

    test_class = YumDnf('arg')
    try:
        test_class.run()
        assert False, "Should not reach here"
    except NotImplementedError:
        assert True, "Expected NotImplementedError"


# Generated at 2022-06-13 04:42:10.811412
# Unit test for constructor of class YumDnf

# Generated at 2022-06-13 04:42:21.475292
# Unit test for method run of class YumDnf
def test_YumDnf_run():

    test_is_lockfile_pid_valid = 1

    class TestYumDnf(YumDnf):
        def is_lockfile_pid_valid(self):
            return test_is_lockfile_pid_valid

    test_module = TestYumDnf(dict())

    # test case - lockfile is not present but timeout is zero
    test_lock_timeout = 0
    result, msg = test_module.wait_for_lock()
    assert result is True
    assert msg == ''

    # test case - lockfile is present and timeout is zero
    test_is_lockfile_pid_valid = 0
    result, msg = test_module.wait_for_lock()
    assert result is False
    assert msg == 'yum lockfile is held by another process'

    # test case - lockfile is not

# Generated at 2022-06-13 04:42:30.195050
# Unit test for method is_lockfile_pid_valid of class YumDnf
def test_YumDnf_is_lockfile_pid_valid():
    ''' Unit test of class YumDnf method is_lockfile_pid_valid '''

    # This is a hack to access the method is_lockfile_pid_valid of class YumDnf
    yumdnf = YumDnf(None)

    # Create a temporary file and make it empty
    fd, tmpfilename = tempfile.mkstemp()
    os.close(fd)
    assert os.stat(tmpfilename).st_size == 0


# Generated at 2022-06-13 04:42:38.149013
# Unit test for method listify_comma_sep_strings_in_list of class YumDnf
def test_YumDnf_listify_comma_sep_strings_in_list():
    class MockModule(object):
        def __init__(self):
            class FailJsonException(Exception):
                pass
            self.fail_json = FailJsonException
            self.params = dict()

    class MockYumDnf(YumDnf):
        def __init__(self, module):
            super(MockYumDnf, self).__init__(module)

        def run(self):
            return

    class MockFailJsonException(Exception):
        pass

    module = MockModule()
    module.fail_json = MockFailJsonException
    yum = MockYumDnf(module)

    # Check if method listify_comma_sep_strings_in_list returns correct list when input list has no comma separated elements
    assert yum.listify_comma_sep

# Generated at 2022-06-13 04:42:46.118116
# Unit test for constructor of class YumDnf

# Generated at 2022-06-13 04:42:55.863923
# Unit test for constructor of class YumDnf
def test_YumDnf():
    """
    Test cases for constructor of class YumDnf
    """
    # Import test module
    from ansible.module_utils import basic

    # Import ansible module_utils
    from ansible.module_util.basic import AnsibleModule

    # Define test module
    module_args = {
        "name": "vim",
        "state": None,
        "autoremove": True,
        "lock_timeout": 30,
    }
    module = AnsibleModule(argument_spec=yumdnf_argument_spec, module_args=module_args)
    # Define test yum class
    class TestYum(YumDnf):
        def __init__(self, module):
            self.module = module
            self.pkg_mgr_name = "Yum"

# Generated at 2022-06-13 04:43:06.295433
# Unit test for constructor of class YumDnf
def test_YumDnf():
    import ansible.module_utils.yum as yum_module_util

    # empty set of module parameters
    params = {}
    args = {'params': params}
    module = yum_module_util.AnsibleYumModule(down_to_class=True, **args)
    yum_dnf = YumDnf(module)
    assert len(yum_dnf.names) == 0
    assert yum_dnf.disablerepo == []
    assert yum_dnf.enablerepo == []
    assert yum_dnf.exclude == []
    assert yum_dnf.state == None
    assert yum_dnf.autoremove == False
    assert not yum_dnf._is_lockfile_present()

    # set allow_downgrade=True

# Generated at 2022-06-13 04:43:27.587399
# Unit test for constructor of class YumDnf

# Generated at 2022-06-13 04:43:33.181577
# Unit test for method run of class YumDnf
def test_YumDnf_run():
    module = MockModule({})
    try:
        YumDnf.run(MockYumDnf({}))
    except NotImplementedError:
        assert True, \
            'Expected NotImplementedError'
    else:
        assert False, \
            'Expected NotImplementedError - got: ' + str(result)


# Generated at 2022-06-13 04:43:34.846845
# Unit test for method run of class YumDnf
def test_YumDnf_run():
    assert True


# Generated at 2022-06-13 04:43:36.521787
# Unit test for method is_lockfile_pid_valid of class YumDnf
def test_YumDnf_is_lockfile_pid_valid():
    pass  # No need to define this method for test since it is an abstract method



# Generated at 2022-06-13 04:43:45.071226
# Unit test for method listify_comma_sep_strings_in_list of class YumDnf
def test_YumDnf_listify_comma_sep_strings_in_list():
    result = YumDnf.listify_comma_sep_strings_in_list(["foo", "bar", "baz"])
    assert result == ["foo", "bar", "baz"]

    result = YumDnf.listify_comma_sep_strings_in_list(["foo", "bar", "baz, qux"])
    assert result == ["foo", "bar", "baz", "qux"]

    result = YumDnf.listify_comma_sep_strings_in_list(["foo", "bar", "baz,qux"])
    assert result == ["foo", "bar", "baz", "qux"]


# Generated at 2022-06-13 04:43:53.133560
# Unit test for method listify_comma_sep_strings_in_list of class YumDnf
def test_YumDnf_listify_comma_sep_strings_in_list():
    import unittest
    from ansible.module_utils.six import StringIO
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six.moves import builtins

    class MockAnsibleModule():
        pass

    # setup the test cases

    # test case 1
    # a list with a comma separated element
    test_case = [
        "foo",
        "bar",
        "abc, def, ghi"
    ]
    expected_result = [
        "foo",
        "bar",
        "abc",
        "def",
        "ghi"
    ]

    # test case 2
    # a list with a comma separated element with a space in it

# Generated at 2022-06-13 04:43:56.179590
# Unit test for method is_lockfile_pid_valid of class YumDnf
def test_YumDnf_is_lockfile_pid_valid():
    """
    unit test to test method is_lockfile_pid_valid of class YumDnf
    """
    import ansible.module_utils.yum
    import ansible.module_utils.dnf
    for module_utils in [ansible.module_utils.yum, ansible.module_utils.dnf]:
        with tempfile.NamedTemporaryFile() as tmp:
            yum = module_utils.YumDnf(tmp.name)
            yum.lockfile = tmp.name
            yum.is_lockfile_pid_valid()

# Generated at 2022-06-13 04:44:03.867896
# Unit test for method listify_comma_sep_strings_in_list of class YumDnf
def test_YumDnf_listify_comma_sep_strings_in_list():
    from ansible.module_utils.yum import YumDnf
    yum = YumDnf(object())
    assert yum.listify_comma_sep_strings_in_list(["one", "two,three", "four"]) == ['one', 'two', 'three', 'four']
    assert yum.listify_comma_sep_strings_in_list(["one"]) == ['one']
    assert yum.listify_comma_sep_strings_in_list([""]) == []
    assert yum.listify_comma_sep_strings_in_list(["one,two"]) == ['one', 'two']

# Generated at 2022-06-13 04:44:06.339451
# Unit test for method run of class YumDnf
def test_YumDnf_run():
    yd = YumDnf()
    try:
        yd.run()
    except NotImplementedError:
        pass



# Generated at 2022-06-13 04:44:16.224039
# Unit test for method wait_for_lock of class YumDnf
def test_YumDnf_wait_for_lock():
    '''
    Test method wait_for_lock of class YumDnf.
    For that the method _is_lockfile_present() needs to be mocked.
    '''
    import mock
    import time
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule()
    yumdnf_mock = YumDnf(module)

    # Set up mock.
    yumdnf_mock._is_lockfile_present = mock.MagicMock(return_value=False)

    # No need to wait for lock, return immediately.
    yumdnf_mock.wait_for_lock()
    assert yumdnf_mock._is_lockfile_present.call_count == 1
    yumdnf_mock._is_lockfile_present.assert_

# Generated at 2022-06-13 04:44:49.491488
# Unit test for method is_lockfile_pid_valid of class YumDnf
def test_YumDnf_is_lockfile_pid_valid():

    # dummy class inheriting YumDnf
    class DummyYumDnf(YumDnf):
        pkg_mgr_name = 'dummy_pkg_mgr'

        def is_lockfile_pid_valid(self):
            return False

    # create an instance of dummy class
    dummy_yum_dnf = DummyYumDnf('dummy_module')
    # test cases
    test_cases = [
        # case1: lockfile exist but its pid is invalid
        dict(
            lock_timeout=1,
            is_lockfile_present=True,
            expected_msg='dummy_pkg_mgr lockfile is held by another process'
        )
    ]

    # run the test
    for test_case in test_cases:
        dummy_yum_dnf

# Generated at 2022-06-13 04:44:55.125752
# Unit test for method listify_comma_sep_strings_in_list of class YumDnf
def test_YumDnf_listify_comma_sep_strings_in_list():
    """
    Check if method listify comma separated strings in list is working correctly
    """
    sample_list = ["A,C", "B,", "D", "E", "F,G,H"]
    yum_dnf_object = YumDnf('')
    new_list = yum_dnf_object.listify_comma_sep_strings_in_list(sample_list)
    if new_list != ["A", "C", "B", "D", "E", "F", "G", "H"]:
        raise AssertionError("Method listify_comma_sep_strings_in_list failed")


# Generated at 2022-06-13 04:45:03.199936
# Unit test for method run of class YumDnf
def test_YumDnf_run():
    from ansible.module_utils.yum import YumDnfModule
    class dummy(YumDnf):
        def __init__(self, module):
            super(dummy, self).__init__(module)
            self.pkg_mgr_name = 'yum'

        def is_lockfile_pid_valid(self):
            return True

    module = YumDnfModule(
        argument_spec=dict(),
        supports_check_mode=True,
        bypass_checks=True,
    )
    mgr = dummy(module)

    assert mgr.listify_comma_sep_strings_in_list(['a,b,c']) == ['a', 'b', 'c']

# Generated at 2022-06-13 04:45:04.047097
# Unit test for method is_lockfile_pid_valid of class YumDnf
def test_YumDnf_is_lockfile_pid_valid():
    pass



# Generated at 2022-06-13 04:45:13.801847
# Unit test for method run of class YumDnf
def test_YumDnf_run():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.modules.package.yum import YumModule
    args = dict(
        state=dict(type='str', default=None, choices=['absent', 'installed', 'latest', 'present', 'removed']),
    )
    yum_dnf = YumDnf(YumModule(
        argument_spec=dict(
            state=dict(type='str', default=None, choices=['absent', 'installed', 'latest', 'present', 'removed']),
        ),
        mutually_exclusive=[],
        supports_check_mode=True,
        required_one_of=[],
    ))
    try:
        yum_dnf.run()
    except NotImplementedError:
        pass

# Generated at 2022-06-13 04:45:24.975989
# Unit test for method run of class YumDnf
def test_YumDnf_run():
    modl = AnsibleModule(yumdnf_argument_spec, supports_check_mode=True)
    try:
        YumDnf(modl).run()
    except NotImplementedError:
        # We've written a test for base class, the run method is not
        # implemented there. We want to know if someone removes it from the
        # subclass. This line will be executed if the method run is not
        # implemented in the subclass.
        assert False
    except Exception:
        assert False
    else:
        # The method run is implemented in the subclass, we need to think about
        # it's unit testing.
        assert True



# Generated at 2022-06-13 04:45:33.249807
# Unit test for constructor of class YumDnf

# Generated at 2022-06-13 04:45:38.090989
# Unit test for method is_lockfile_pid_valid of class YumDnf
def test_YumDnf_is_lockfile_pid_valid():
    class TestYumDnf(YumDnf):
        def test_is_lockfile_pid_valid(self):
            return True

        def run(self):
            raise NotImplementedError
    assert TestYumDnf(dict).is_lockfile_pid_valid()


# Generated at 2022-06-13 04:45:50.756752
# Unit test for method listify_comma_sep_strings_in_list of class YumDnf
def test_YumDnf_listify_comma_sep_strings_in_list():
    # Create a YumDnf instance for testing
    class FakeModule(object):
        def __init__(self):
            self.params = {}

        def fail_json(self, msg):
            raise Exception(msg)

    fake_module = FakeModule()
    yum_dnf = YumDnf(fake_module)

    assert yum_dnf.listify_comma_sep_strings_in_list(["one, two, three"]) == ["one", "two", "three"]
    assert yum_dnf.listify_comma_sep_strings_in_list(["one, two, three", "four", "five"]) == ["one", "two", "three", "four", "five"]
    assert yum_dnf.listify_comma_sep_strings_in_

# Generated at 2022-06-13 04:46:01.900415
# Unit test for method listify_comma_sep_strings_in_list of class YumDnf
def test_YumDnf_listify_comma_sep_strings_in_list():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.yumdnf.yumdnf import YumDnf

    yumdnf_module = AnsibleModule(
        argument_spec={},
        required_one_of=[],
        mutually_exclusive=[],
        supports_check_mode=True,
        required_together=[],
    )

    yumdnf_instance = YumDnf(module=yumdnf_module)
    # Test with valid input
    yumdnf_instance.listify_comma_sep_strings_in_list(['a,b,c', 'a', 'b,c', 'a,b']) == ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b']

    #

# Generated at 2022-06-13 04:46:42.218755
# Unit test for method listify_comma_sep_strings_in_list of class YumDnf
def test_YumDnf_listify_comma_sep_strings_in_list():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.yumdnf import YumDnf

    module = AnsibleModule({'the_list': ['a,b', 'c', 'd,e,f']})
    setattr(module, 'fail_json', lambda a, msg: msg)

    yumdnf_obj = YumDnf(module)

    ret = yumdnf_obj.listify_comma_sep_strings_in_list(module.params['the_list'])
    assert ret == ['a', 'b', 'c', 'd', 'e', 'f']

    module.params['the_list'] = ['a,b', 'c,']
    ret = yumdnf_obj.listify_comma_sep_strings_

# Generated at 2022-06-13 04:46:47.469364
# Unit test for constructor of class YumDnf
def test_YumDnf():
    class TestModule(object):
        def __init__(self, **kwargs):
            self.params = kwargs.copy()


# Generated at 2022-06-13 04:46:54.638684
# Unit test for method wait_for_lock of class YumDnf
def test_YumDnf_wait_for_lock():
    module = FakeAnsibleModule()
    yumdnf = YumDnf(module)

    # Create the lockfile
    lockfile_handle, lockfile = tempfile.mkstemp()
    os.close(lockfile_handle)

    # Test with lockfile present
    yumdnf.lockfile = lockfile
    yumdnf.lock_timeout = 10
    yumdnf._is_lockfile_present = lambda: True
    yumdnf.is_lockfile_pid_valid = lambda: True
    with yumdnf._handle_exceptions():
        yumdnf.wait_for_lock()

    # Test with lockfile present and timeout 0
    yumdnf.lock_timeout = 0
    yumdnf._is_lockfile_present = lambda: True

# Generated at 2022-06-13 04:47:06.778748
# Unit test for method listify_comma_sep_strings_in_list of class YumDnf
def test_YumDnf_listify_comma_sep_strings_in_list():
    class MockModule:
        def __init__(self):
            self.params = {
                'name': ['', 'foo'],
                'disablerepo': ['', 'bar', 'foo,baz'],
                'enablerepo': ['', 'x', 'y,z'],
                'exclude': ['', 'quux'],
            }

    class YumDnfSubclass(YumDnf):
        def __init__(self, module):
            YumDnf.__init__(self, module)

    result = {'name': ['foo', 'foo', 'baz'],
              'disablerepo': ['bar', 'foo,baz'],
              'enablerepo': ['x', 'y,z', 'y', 'z'],
              'exclude': ['quux']}


# Generated at 2022-06-13 04:47:18.547480
# Unit test for method wait_for_lock of class YumDnf
def test_YumDnf_wait_for_lock():
    module = object
    module.fail_json = lambda msg: exit(msg)
    module.params = dict(lock_timeout=10)
    yum_dnf_obj = YumDnf(module)
    # Lock file not available
    yum_dnf_obj.lockfile = tempfile.mkstemp()[1]
    yum_dnf_obj.is_lockfile_pid_valid = lambda: True
    # Lock file available
    yum_dnf_obj.wait_for_lock()
    # Lock file available and timeout 0
    module.params.update(dict(lock_timeout=0))
    yum_dnf_obj.wait_for_lock()

    # Test case fails if wait_for_lock did not quit in test_yum_dnf_wait_for_lock_fail
   

# Generated at 2022-06-13 04:47:19.567965
# Unit test for method listify_comma_sep_strings_in_list of class YumDnf
def test_YumDnf_listify_comma_sep_strings_in_list():
    # This method is tested by the yum module`s test_yum.py
    pass

# Generated at 2022-06-13 04:47:31.657858
# Unit test for method run of class YumDnf

# Generated at 2022-06-13 04:47:42.506229
# Unit test for constructor of class YumDnf
def test_YumDnf():
    module = (os.path.dirname(os.path.realpath(__file__)) +
              '/../../lib/ansible/modules/packaging/os/yum.py')
    module = to_native(module)

# Generated at 2022-06-13 04:47:55.444373
# Unit test for method listify_comma_sep_strings_in_list of class YumDnf
def test_YumDnf_listify_comma_sep_strings_in_list():
    yum = YumDnf(ansible_module)
    yum.listify_comma_sep_strings_in_list(["a,b,c"]) == ["a", "b", "c"]
    yum.listify_comma_sep_strings_in_list(["a,b", "c"]) == ["a", "b", "c"]
    yum.listify_comma_sep_strings_in_list(["abc", "d", "f,g,h", "i, j, k"]) == ["abc", "d", "f", "g", "h", "i", "j", "k"]
    yum.listify_comma_sep_strings_in_list([]) == []
    yum.listify_comma_sep_strings_in_

# Generated at 2022-06-13 04:48:08.342103
# Unit test for method wait_for_lock of class YumDnf

# Generated at 2022-06-13 04:49:30.685242
# Unit test for method is_lockfile_pid_valid of class YumDnf
def test_YumDnf_is_lockfile_pid_valid():

    class MockModule(object):
        def fail_json(self, **kwargs):
            pass

        def get_bin_path(self, executable, required=False, opt_dirs=[]):
            return '/bin/' + executable

    class MockYumDnf(YumDnf):
        def __init__(self):
            self.module = MockModule()

    yumdnf = MockYumDnf()

    # PID is a valid number
    with tempfile.NamedTemporaryFile(mode='w', prefix='yum.pid.', delete=False) as pid_file:
        pid_file.write('12345')
    assert yumdnf.is_lockfile_pid_valid() == True
    os.unlink(pid_file.name)

    # PID is not a number

# Generated at 2022-06-13 04:49:38.146512
# Unit test for method wait_for_lock of class YumDnf
def test_YumDnf_wait_for_lock():

    class MockYumDnf(YumDnf):
        lockfile = tempfile.NamedTemporaryFile(delete=False)

        def is_lockfile_pid_valid(self):
            return os.path.isfile(self.lockfile.name)

    MockYumDnf.lockfile.write(b"")
    MockYumDnf.lockfile.close()

    instance = MockYumDnf(None)

    # Testing the normal scenario
    instance.wait_for_lock()

    # Testing the scenario when the pid in the lockfile is not valid
    with open(instance.lockfile.name, "w") as f:
        f.write("pid=99999\n")


# Generated at 2022-06-13 04:49:45.517074
# Unit test for method listify_comma_sep_strings_in_list of class YumDnf
def test_YumDnf_listify_comma_sep_strings_in_list():
    yumdnf = YumDnf(object)
    some_list = ["one,two", "three, four, five", "six, seven, eight, nine, ten", "eleven", "", "twelve, thirteen, fourteen,"]
    assert yumdnf.listify_comma_sep_strings_in_list(some_list) == ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen']

# Generated at 2022-06-13 04:49:48.658508
# Unit test for method run of class YumDnf
def test_YumDnf_run():
    module = MockModule()
    yum = YumDnf(module)
    with pytest.raises(NotImplementedError):
        yum.run()



# Generated at 2022-06-13 04:49:58.463537
# Unit test for method is_lockfile_pid_valid of class YumDnf
def test_YumDnf_is_lockfile_pid_valid():

    from ansible.module_utils.six import PY3, PY2

    from ansible.module_utils import package_common
    from ansible.module_utils.package_common import YumDnfBase

    from ansible.modules.packaging.os import yum_repository

    from ansible.module_utils.six import BytesIO

    class FakePopen(object):

        def __init__(self, cmd, stdout=None):
            self.stdout = stdout or BytesIO()
            self.cmd = cmd

        def __call__(self, *args, **kwargs):
            return self

        def communicate(self):
            if self.cmd[1] == '-q':
                pid = self.cmd[2]

# Generated at 2022-06-13 04:50:06.884311
# Unit test for method wait_for_lock of class YumDnf
def test_YumDnf_wait_for_lock():
    module = MockModule()
    mock_os = MockOS()
    module.params = dict(state='latest', name='foo')
    module.check_mode = False
    ModuleUtilsMock.FAKE_MODULE_UTILS_PATH = True
    yum = YumDnf(module)
    yum.is_lockfile_pid_valid = Mock(return_value=True)
    yum.wait_for_lock()
    assert not yum.module.fail_json.called


# Generated at 2022-06-13 04:50:18.288765
# Unit test for constructor of class YumDnf

# Generated at 2022-06-13 04:50:28.083110
# Unit test for method listify_comma_sep_strings_in_list of class YumDnf
def test_YumDnf_listify_comma_sep_strings_in_list():
    class FakeModule():
        def fail_json(self, msg, results=[]):
            print(msg)
            assert False, "FAIL"

    fm = FakeModule()
    class FakeYumDnf(YumDnf):
        def run(self):
            raise NotImplementedError

    fyd = FakeYumDnf(fm)
    assert fyd.listify_comma_sep_strings_in_list(["a"]) == ["a"]
    assert fyd.listify_comma_sep_strings_in_list([]) == []
    assert fyd.listify_comma_sep_strings_in_list(["a,b,c"]) == ["a", "b", "c"]
    assert fyd.listify_comma_sep_strings_in_

# Generated at 2022-06-13 04:50:37.962262
# Unit test for method wait_for_lock of class YumDnf
def test_YumDnf_wait_for_lock():

    # Create a temporary directory
    tmp_dir = tempfile.mkdtemp()


# Generated at 2022-06-13 04:50:42.670949
# Unit test for method run of class YumDnf
def test_YumDnf_run():
    """
    Validate the method run of class YumDnf
    """
    module = MockModule()
    with pytest.raises(NotImplementedError):
        n = YumDnf(module)
        n.run()
