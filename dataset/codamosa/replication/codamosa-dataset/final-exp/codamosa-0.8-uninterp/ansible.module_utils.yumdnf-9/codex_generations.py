

# Generated at 2022-06-13 04:41:40.727203
# Unit test for method wait_for_lock of class YumDnf
def test_YumDnf_wait_for_lock():
    fd, temp_path = tempfile.mkstemp()
    os.write(fd, b'pid')
    os.close(fd)
    module = FakeModule()
    yum_dnf = YumDnf(module)
    yum_dnf.lockfile = temp_path
    yum_dnf.wait_for_lock()
    assert os.path.isfile(temp_path)



# Generated at 2022-06-13 04:41:51.830943
# Unit test for method listify_comma_sep_strings_in_list of class YumDnf
def test_YumDnf_listify_comma_sep_strings_in_list():
    module = MagicMock()
    yum = YumDnf(module)

    # standard case
    input_list = ["foo", "bar", "a, b, c", "d,e,f"]
    expected_list = ['foo', 'bar', 'a', 'b', 'c', 'd', 'e', 'f']
    actual_list = yum.listify_comma_sep_strings_in_list(input_list)
    assert actual_list == expected_list

    # empty list as input
    input_list = []
    expected_list = []
    actual_list = yum.listify_comma_sep_strings_in_list(input_list)
    assert actual_list == expected_list

    # edge cases
    # input element consisting of comma only

# Generated at 2022-06-13 04:42:02.855207
# Unit test for constructor of class YumDnf
def test_YumDnf():
    class YumDnfModule(object):
        def __init__(self):
            self.argument_spec = dict()
            self.params = dict()
        def fail_json(self, msg, results):
            raise Exception(msg)

    class FakeModule(object):
        def __init__(self, params, check_mode=False):
            class FailJsonException(Exception):
                def __init__(self, msg):
                    self.msg = msg
            self.params = params
            self.check_mode = check_mode
            self.fail_json = FailJsonException

    # autoremove alone should result in state=absent if not specified
    params = dict(autoremove=True)
    ydm = YumDnf(FakeModule(params))
    assert ydm.state == "absent"



# Generated at 2022-06-13 04:42:06.137510
# Unit test for method run of class YumDnf
def test_YumDnf_run():
    try:
        test_yumdnf = YumDnf('test_module')
        test_yumdnf.run()
    except NotImplementedError as e:
        print("Method run is not implemented")


# Generated at 2022-06-13 04:42:13.937135
# Unit test for method wait_for_lock of class YumDnf
def test_YumDnf_wait_for_lock():
    """
    Test to make sure that the wait_for_lock method catches a lockfile and fails
    a module run or doesn't catch a lockfile and doesn't fail a module run.
    """
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(
        argument_spec=yumdnf_argument_spec,
        supports_check_mode=True,
    )
    instance = YumDnf(module)

    # Mock wait_for_lock(). We need to wait for _is_lockfile_present()
    # before we can mock it.
    def wait_for_lock(self):
        return self._is_lockfile_present()

    instance.wait_for_lock = wait_for_lock.__get__(instance, YumDnf)

    # Mock _is_lock

# Generated at 2022-06-13 04:42:25.239791
# Unit test for constructor of class YumDnf

# Generated at 2022-06-13 04:42:33.501674
# Unit test for method is_lockfile_pid_valid of class YumDnf
def test_YumDnf_is_lockfile_pid_valid():  # pylint: disable=invalid-name
    """
    Test that the abstract method is_lockfile_pid_valid raises a TypeError
    when called
    """
    yumdnf = YumDnf(None)
    with tempfile.TemporaryFile() as lockfile_handle:
        yumdnf.lockfile = lockfile_handle.name
        try:
            yumdnf.is_lockfile_pid_valid()
        except TypeError:
            pass
        else:
            assert False, "Expected TypeError not raised"

# Generated at 2022-06-13 04:42:40.527784
# Unit test for method is_lockfile_pid_valid of class YumDnf
def test_YumDnf_is_lockfile_pid_valid():
    temp = tempfile.NamedTemporaryFile()

    def try_open_file(self):
        return open(temp.name, 'w')

    class Dummy_module(object):
        def fail_json(self, msg, results):
            raise Exception(msg)

    src = 'ansible.module_utils.yum_dnf.YumDnf'
    name = 'YumDnf'
    bases = (object,)
    dct = {'is_lockfile_pid_valid': lambda self: False}
    Dummy_YumDnf = type(name, bases, dct)
    Dummy_YumDnf.lockfile = temp.name
    obj = Dummy_YumDnf(Dummy_module())
    result = obj.is_lockfile_pid_valid()


# Generated at 2022-06-13 04:42:47.422004
# Unit test for method listify_comma_sep_strings_in_list of class YumDnf
def test_YumDnf_listify_comma_sep_strings_in_list():
    yd = YumDnf(None)
    assert yd.listify_comma_sep_strings_in_list(["foo"]) == ["foo"]
    assert yd.listify_comma_sep_strings_in_list(["foo,bar"]) == ["foo", "bar"]
    assert yd.listify_comma_sep_strings_in_list(["foo,bar","baz"]) == ["foo", "bar", "baz"]
    assert yd.listify_comma_sep_strings_in_list(["foo, bar"]) == ["foo", "bar"]
    assert yd.listify_comma_sep_strings_in_list(["foo", "bar,baz"]) == ["foo", "bar", "baz"]



# Generated at 2022-06-13 04:42:56.283891
# Unit test for method listify_comma_sep_strings_in_list of class YumDnf
def test_YumDnf_listify_comma_sep_strings_in_list():
    # create an empty module and instantiate YumDnf(module) object
    import module_utils.basic
    module = module_utils.basic.AnsibleModule(
        argument_spec=dict()
    )
    yumdnf = YumDnf(module)

    # test with mixed commas and spaces in comma separated list
    yumdnf.names = ["abc,pqr, xyz"]
    yumdnf.listify_comma_sep_strings_in_list(yumdnf.names)
    assert yumdnf.names == ["abc", "pqr", "xyz"]

    # test with comma separated list
    yumdnf.names = ["abc,pqr"]

# Generated at 2022-06-13 04:43:21.816141
# Unit test for method listify_comma_sep_strings_in_list of class YumDnf
def test_YumDnf_listify_comma_sep_strings_in_list():
    yumdnf = YumDnf(None)

    assert yumdnf.listify_comma_sep_strings_in_list(['a', 'b']) == ['a', 'b']
    assert yumdnf.listify_comma_sep_strings_in_list(['a,b']) == ['a', 'b']
    assert yumdnf.listify_comma_sep_strings_in_list(['a , b']) == ['a', 'b']
    assert yumdnf.listify_comma_sep_strings_in_list(['a', 'b', 'c,d']) == ['a', 'b', 'c', 'd']

# Generated at 2022-06-13 04:43:25.094430
# Unit test for method listify_comma_sep_strings_in_list of class YumDnf
def test_YumDnf_listify_comma_sep_strings_in_list():
    yum_dnf = YumDnf('')
    original_list = ['httpd', 'vim,git', 'gvim', '']
    expected_list = ['httpd', 'vim', 'git', 'gvim']
    output_list = yum_dnf.listify_comma_sep_strings_in_list(original_list)
    assert sorted(output_list) == sorted(expected_list)

# Generated at 2022-06-13 04:43:35.758056
# Unit test for method wait_for_lock of class YumDnf
def test_YumDnf_wait_for_lock():
    from ansible.module_utils.common.process import get_bin_path
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.rpm_utils import is_yum_lockfile_valid, is_dnf_lockfile_valid
    import yum
    import dnf

    # We want to test an existing lockfile scenario. The lockfile is a lockfile
    # validation where the pid is valid.
    # We also need a __str__() method to be defined on both the yum and dnf
    # classes.
    # The __str__() method was added to yum in the yum v3.4.3 release and dnf
    # in the dnf v2.2.0 release.
    # We cannot test against a lower release.
    # We can override the

# Generated at 2022-06-13 04:43:43.272662
# Unit test for method is_lockfile_pid_valid of class YumDnf
def test_YumDnf_is_lockfile_pid_valid():
    class YumDnfMock():
        def __init__(self):
            pass

    y = YumDnf(YumDnfMock())

    try:
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        y.lockfile = temp_file.name
        with open(temp_file.name, 'w') as f:
            f.write("1234")
        assert y.is_lockfile_pid_valid()
    finally:
        try:
            os.remove(temp_file.name)
        except OSError:
            pass


# Generated at 2022-06-13 04:43:52.409497
# Unit test for constructor of class YumDnf
def test_YumDnf():
    # Initialize module object
    module = AnsibleModule(yumdnf_argument_spec)

    # Initialize class object
    yumdnf = YumDnf(module)

    # Test constructor of class YumDnf
    assert yumdnf.allow_downgrade == module.params['allow_downgrade']
    assert yumdnf.autoremove == module.params['autoremove']
    assert yumdnf.bugfix == module.params['bugfix']
    assert yumdnf.cacheonly == module.params['cacheonly']
    assert yumdnf.conf_file == module.params['conf_file']
    assert yumdnf.disable_excludes == module.params['disable_excludes']

# Generated at 2022-06-13 04:43:59.871102
# Unit test for method is_lockfile_pid_valid of class YumDnf
def test_YumDnf_is_lockfile_pid_valid():
    class fake_module(object):
        class fail_json(object):
            def __call__(self, **kwargs):
                return

        params = {}

    class fake_yum_dnf(YumDnf):
        pass

    module = fake_module()
    yum_dnf_obj = fake_yum_dnf(module)

    test_name = 'test_YumDnf_is_lockfile_pid_valid'

    # Non existent pid
    yum_dnf_obj.lockfile = tempfile.mktemp(dir='/tmp', prefix='test_YumDnf_is_lockfile_pid_valid_')
    open(yum_dnf_obj.lockfile, 'w').write('9999')
    assert not yum_dnf_obj.is_lockfile

# Generated at 2022-06-13 04:44:08.088431
# Unit test for constructor of class YumDnf
def test_YumDnf():
    import mock
    test_module = mock.MagicMock()

# Generated at 2022-06-13 04:44:17.149934
# Unit test for constructor of class YumDnf
def test_YumDnf():
    mod = ModuleMock()
    mod.params = yumdnf_argument_spec['argument_spec']
    yumdnf = YumDnf(mod)
    assert yumdnf.allow_downgrade == False
    assert yumdnf.autoremove == False
    assert yumdnf.bugfix == False
    assert yumdnf.cacheonly == False
    assert yumdnf.conf_file == None
    assert yumdnf.disable_excludes == None
    assert yumdnf.disable_gpg_check == False
    assert yumdnf.disable_plugin == []
    assert yumdnf.disablerepo == []
    assert yumdnf.download_only == False
    assert yumdnf.download_dir == None

# Generated at 2022-06-13 04:44:24.185723
# Unit test for method listify_comma_sep_strings_in_list of class YumDnf
def test_YumDnf_listify_comma_sep_strings_in_list():

    class YumDnf_test(YumDnf):
        def is_lockfile_pid_valid(self):
            return True

        def run(self):
            return

    yum_test = YumDnf_test(None)

    # test 1
    names = ['name1, name2', 'name3', 'name4, name5, name6', 'name7', 'name8, name9']
    yum_test.names = names
    expected_list = ['name1', 'name2', 'name3', 'name4', 'name5', 'name6', 'name7', 'name8', 'name9']
    new_list = yum_test.listify_comma_sep_strings_in_list(yum_test.names)

# Generated at 2022-06-13 04:44:34.445148
# Unit test for constructor of class YumDnf
def test_YumDnf():
    params = yumdnf_argument_spec['argument_spec']
    params['name'] = 'foo-package, bar-package'
    params['disablerepo'] = 'foo, bar'
    params['enablerepo'] = 'foo, bar'
    params['exclude'] = 'foo, bar'
    params['list'] = 'installed'
    params['lock_timeout'] = 3
    params['update_cache'] = True

    class Struct:
        def __init__(self, **entries):
            self.__dict__.update(entries)

    class FakeModule(object):
        def __init__(self):
            self.params = Struct(**params)
            self.fail_json = lambda **kwargs: None

    obj = YumDnf(FakeModule())


# Generated at 2022-06-13 04:45:01.752541
# Unit test for method wait_for_lock of class YumDnf
def test_YumDnf_wait_for_lock():
    import time
    import os

    class YumDnfMock(YumDnf):
        def __init__(self, module):
            self.module = module
            self.lock_timeout = module.params['lock_timeout']
        def is_lockfile_pid_valid(self):
            return True

    # Test if lockfile exists
    class AnsibleModuleMock():
        def __init__(self, lock_timeout):
            self.params = dict()
            self.params['lock_timeout'] = lock_timeout
        def fail_json(self, msg):
            print('Test failed: ' + msg)

    module = AnsibleModuleMock(lock_timeout=0)
    yumdnf_mock = YumDnfMock(module)

# Generated at 2022-06-13 04:45:12.585214
# Unit test for constructor of class YumDnf

# Generated at 2022-06-13 04:45:26.003694
# Unit test for method is_lockfile_pid_valid of class YumDnf
def test_YumDnf_is_lockfile_pid_valid():
    assert not os.path.isfile("./test_yumdnf_is_lockfile_pid_valid")
    assert len(glob.glob("./test_yumdnf_is_lockfile_pid_valid")) == 0


# Generated at 2022-06-13 04:45:31.284690
# Unit test for method is_lockfile_pid_valid of class YumDnf
def test_YumDnf_is_lockfile_pid_valid():
    class YumDnfMock(YumDnf):
        def __init__(self):
            pass

        def is_lockfile_pid_valid(self):
            return True
    yumdnf = YumDnfMock()
    assert yumdnf.is_lockfile_pid_valid() is True


# Generated at 2022-06-13 04:45:32.723346
# Unit test for method is_lockfile_pid_valid of class YumDnf
def test_YumDnf_is_lockfile_pid_valid():
    pass


# Generated at 2022-06-13 04:45:46.722871
# Unit test for method wait_for_lock of class YumDnf
def test_YumDnf_wait_for_lock():
    """
    Test the method wait_for_lock of class YumDnf
    """
    from ansible.module_utils import common
    import ansible.module_utils.yum
    import ansible.module_utils.dnf
    import ansible.module_utils.yum_dnf_common as YumDnfCommon

    class TestModule(object):
        def __init__(self, params):
            self.params = params
            self.fail_json = common.fail_json
            self.exit_json = common.exit_json

    class TestYumDnf(YumDnfCommon.YumDnf):
        def __init__(self, module):
            super(TestYumDnf, self).__init__(module)


# Generated at 2022-06-13 04:45:54.863850
# Unit test for constructor of class YumDnf
def test_YumDnf():

    # create a mock module to pass to object
    # returning_value_of_run is value to be returned by method 'run'
    test_module = MockAnsibleModule(
        argument_spec=yumdnf_argument_spec,
        returning_value_of_run=[],
    )

    # create a YumDnf object by passing mock module
    y = YumDnf(test_module)
    assert y.lock_timeout == 30, 'default value of lock_timeout should be 30.'
    assert y.names == test_module.params['name'], 'y.names should be same as in test_module.params["name"]'
    assert y.conf_file == test_module.params['conf_file'], 'y.conf_file should be same as in test_module.params["conf_file"]'


# Generated at 2022-06-13 04:46:04.098818
# Unit test for method wait_for_lock of class YumDnf
def test_YumDnf_wait_for_lock():

    with tempfile.NamedTemporaryFile() as tmpfile:
        # Mock class Yum
        class Yum(YumDnf):
            def is_lockfile_pid_valid(self):
                return True

        m = Yum(None)
        m.lockfile = tmpfile.name
        assert m._is_lockfile_present()
        # wait_for_lock() does not raise exception, so YumDnf is correctly mocked
        m.wait_for_lock()

    with tempfile.NamedTemporaryFile(dir="/var/run") as tmpfile:
        # Mock class Dnf
        class Dnf(YumDnf):
            def is_lockfile_pid_valid(self):
                return True

        m = Dnf(None)
        m.lockfile = tmpfile.name

# Generated at 2022-06-13 04:46:15.343596
# Unit test for method listify_comma_sep_strings_in_list of class YumDnf
def test_YumDnf_listify_comma_sep_strings_in_list():
    # create temp file to be used as a fake YumDnf module
    t = tempfile.NamedTemporaryFile()
    module_path = t.name

    # create fake module object to replace imported module for unit testing
    class tmp():
        def __init__(self, module_path):
            self.module_path = module_path

        def fail_json(self, *args, **kwargs):
            kwargs['failed'] = True
            with open(self.module_path, 'w') as f:
               f.write(to_native(repr(kwargs)))

        class params():
            name = ['test_pkg1', 'test_pkg2', 'test_pkg3']

    class tmp_YumDnf(YumDnf):
        def run(self):
            pass

    fake_

# Generated at 2022-06-13 04:46:24.783180
# Unit test for method is_lockfile_pid_valid of class YumDnf
def test_YumDnf_is_lockfile_pid_valid():
    os.chdir("..")
    from ansible.modules.package.yum import Yum

    yum = Yum({"name": "git"})
    fd, some_file = tempfile.mkstemp()

    with open(some_file, "w+") as f:
        f.write("12345678\n{}".format(os.getpid()))

    yum.lockfile = some_file
    yum.is_lockfile_pid_valid()
    os.close(fd)

    with open(some_file, "w+") as f:
        f.write("{}".format(os.getpid()))

    yum.lockfile = some_file
    yum.is_lockfile_pid_valid()
    os.close(fd)


# Generated at 2022-06-13 04:46:48.993525
# Unit test for method run of class YumDnf
def test_YumDnf_run():
    try:
        YumDnf(None).run()
    except NotImplementedError:
        pass

# Generated at 2022-06-13 04:46:55.211347
# Unit test for method wait_for_lock of class YumDnf
def test_YumDnf_wait_for_lock():
    class MockModule(object): # use __new__ to enable static methods
        @staticmethod
        def fail_json(msg):
            raise RuntimeError(msg)

    with tempfile.NamedTemporaryFile(prefix='ansible', suffix='.pid') as tmp:
        lockfile = tmp.name

    with open(lockfile, 'w') as fh:
        fh.write(str(os.getpid()))

    mock_class = type('MockClass', (YumDnf,), {}) # create empty MockClass for mocking of _is_lockfile_present
    mock_class.lockfile = lockfile

    mock_class._is_lockfile_present = lambda self: True
    # lockfile exists, is_lockfile_pid_valid returns True

# Generated at 2022-06-13 04:47:06.547182
# Unit test for method run of class YumDnf
def test_YumDnf_run():
    from ansible.modules.package.yum import Yum
    from ansible.module_utils.facts.system.distribution import Distribution
    from ansible.module_utils.facts.system.platform import Platform
    import sys

    with tempfile.TemporaryModule(sys.modules[__name__]) as dg_module:
        # construct the Yum class with a module_utils.facts.system.distribution.Distribution
        dg_module.YumDnf = YumDnf
        dg_module.Distribution = Distribution
        dg_module.Platform = Platform
        dg_module.Yum = Yum
        try:
            dg_class = dg_module.Yum(dg_module)
        except NotImplementedError:
            pass

# Generated at 2022-06-13 04:47:18.546377
# Unit test for method listify_comma_sep_strings_in_list of class YumDnf
def test_YumDnf_listify_comma_sep_strings_in_list():
    yumdnf = YumDnf(None)
    assert yumdnf.listify_comma_sep_strings_in_list(['first', 'second', 'third']) == ['first', 'second', 'third']
    assert yumdnf.listify_comma_sep_strings_in_list(['first, second, third']) == ['first', 'second', 'third']
    assert yumdnf.listify_comma_sep_strings_in_list(['first, second, third', 'fourth, fifth']) == ['first', 'second', 'third', 'fourth', 'fifth']

# Generated at 2022-06-13 04:47:23.164374
# Unit test for method is_lockfile_pid_valid of class YumDnf
def test_YumDnf_is_lockfile_pid_valid():
    pkg_mgr_name = 'dnf'
    lockfile = '/var/run/dnf.pid'
    p = YumDnf(module)

    def fake_is_lockfile_pid_valid(self):
        return True

    YumDnf.is_lockfile_pid_valid = fake_is_lockfile_pid_valid

    assert p.is_lockfile_pid_valid() is true


# unit test for method _is_lockfile_present of class YumDnf

# Generated at 2022-06-13 04:47:24.180981
# Unit test for method run of class YumDnf
def test_YumDnf_run():
    assert issubclass(YumDnf, object)



# Generated at 2022-06-13 04:47:30.388001
# Unit test for method wait_for_lock of class YumDnf
def test_YumDnf_wait_for_lock():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.module_utils.facts.system.distribution.yumdnf import YumDnf
    from ansible.module_utils.facts.system.distribution.yumdnf import yumdnf_argument_spec
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes, to_native

    from ansible.module_utils.six.moves import builtins

    _tempfile = tempfile.NamedTemporaryFile()
    _tempfile.write(to_bytes(u'#!/usr/bin/python\nimport time\ntime.sleep(5)\n', errors='surrogate_or_strict'))
    _tempfile.flush()
    _temp

# Generated at 2022-06-13 04:47:39.952013
# Unit test for method run of class YumDnf
def test_YumDnf_run():
    with tempfile.NamedTemporaryFile(suffix='.py') as temp_file:
        temp_file.write(b"")
        temp_file.flush()

        yd = YumDnf("test")
        try:
            yd.run()
        except NotImplementedError as e:
            if str(e) == "YumDnf.run has not implemented by subclasses":
                pass
            else:
                raise
        yd._is_lockfile_present()
        yd.wait_for_lock()



# Generated at 2022-06-13 04:47:53.417697
# Unit test for method wait_for_lock of class YumDnf
def test_YumDnf_wait_for_lock():

    class ModMock(object):
        params = dict(lockfile='/var/run/yum.pid', lock_timeout=30)
        fail_json_called = False
        fail_json_msg = None

        def fail_json(self, msg):
            self.fail_json_called = True
            self.fail_json_msg = msg

    class DnfMock(YumDnf):
        pkg_mgr_name = 'dnf'

        def __init__(self, module):
            YumDnf.__init__(self, module)

        def is_lockfile_pid_valid(self):
            return True

        def run(self):
            return

    # lock file msg
    mod = ModMock()
    mod.params['lockfile'] = tempfile.NamedTemporary

# Generated at 2022-06-13 04:48:02.179274
# Unit test for constructor of class YumDnf

# Generated at 2022-06-13 04:48:51.984793
# Unit test for constructor of class YumDnf
def test_YumDnf():
    module = MagicMock()

# Generated at 2022-06-13 04:49:03.038586
# Unit test for method is_lockfile_pid_valid of class YumDnf
def test_YumDnf_is_lockfile_pid_valid():
    from ansible.module_utils import yum, dnf
    import os
    import tempfile
    import pytest
    import ansible.constants as C
    import ansible.module_utils.six as six

    # Create test modules
    if six.PY3:
        _yum = yum
        _dnf = dnf
    else:
        _yum = yum.YumDnfModule
        _dnf = dnf.YumDnfModule

    # Create fake lockfile
    with tempfile.NamedTemporaryFile(delete=False) as lockfile:
        os.chmod(lockfile.name, 0o600)
        lockfile.write(b'1234')
        lockfile.flush()
        lockfile_pid = lockfile.name

    # Create test modules with

# Generated at 2022-06-13 04:49:05.373637
# Unit test for constructor of class YumDnf
def test_YumDnf():
    y = YumDnf(module=None)
    assert isinstance(y, YumDnf)



# Generated at 2022-06-13 04:49:16.774529
# Unit test for constructor of class YumDnf

# Generated at 2022-06-13 04:49:28.964261
# Unit test for method is_lockfile_pid_valid of class YumDnf

# Generated at 2022-06-13 04:49:37.293329
# Unit test for method is_lockfile_pid_valid of class YumDnf
def test_YumDnf_is_lockfile_pid_valid():
    test_lockfile_pid = os.getpid()
    lockfile_pid = open(tempfile.gettempdir() + '/yum.pid', 'w')
    lockfile_pid.write(str(test_lockfile_pid))
    lockfile_pid.close()

    module = AnsibleModule(yumdnf_argument_spec)
    module.params['lock_timeout'] = '10'

    yum_dnf = YumDnf(module)
    yum_dnf.lockfile = tempfile.gettempdir() + '/yum.pid'

    yum_dnf.is_lockfile_pid_valid()
    assert True

    # unlink yum.pid file
    os.remove(tempfile.gettempdir() + '/yum.pid')



# Generated at 2022-06-13 04:49:46.955243
# Unit test for constructor of class YumDnf

# Generated at 2022-06-13 04:49:57.099176
# Unit test for method wait_for_lock of class YumDnf
def test_YumDnf_wait_for_lock():
    """Test wait_for_lock method of class YumDnf"""
    from ansible.module_utils import basic
    from ansible.module_utils.common.text.converters import to_text

    from ansible_collections.ansible.community.plugins.module_utils.yum_utils import YumDnf

    from mock import Mock

    class MockYumDnf(YumDnf, object):
        def __init__(self, module):
            super(MockYumDnf, self).__init__(module)
            self.lockfile = None

        def is_lockfile_pid_valid(self):
            return True

        def listify_comma_sep_strings_in_list(self, strlist):
            return strlist


# Generated at 2022-06-13 04:50:03.917092
# Unit test for method run of class YumDnf
def test_YumDnf_run():
    from ansible.modules.packaging.os import yum


# Generated at 2022-06-13 04:50:10.765140
# Unit test for method run of class YumDnf