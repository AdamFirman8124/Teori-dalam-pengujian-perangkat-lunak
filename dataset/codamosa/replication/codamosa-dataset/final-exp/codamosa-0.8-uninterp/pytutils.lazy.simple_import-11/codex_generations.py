

# Generated at 2022-06-14 06:14:44.519792
# Unit test for function make_lazy
def test_make_lazy():
    from tests.mod import lazy_mod
    assert 'lazy_mod' in sys.modules
    assert not isinstance(lazy_mod, _LazyModuleMarker)

    make_lazy('tests.mod.lazy_mod')
    assert 'tests.mod.lazy_mod' in sys.modules
    assert isinstance(lazy_mod, _LazyModuleMarker)

# Generated at 2022-06-14 06:14:48.368422
# Unit test for function make_lazy

# Generated at 2022-06-14 06:15:01.190866
# Unit test for function make_lazy
def test_make_lazy():
    """
    Test function make_lazy.
    """
    import sys
    import os

    def reset_module():
        """
        Reset test_lazymodule
        """
        if sys.modules.has_key('test_lazymodule'):
            del sys.modules['test_lazymodule']

    def make_module(contents):
        """
        Make a module
        """
        try:
            os.remove('test_lazymodule.py')
        except:
            pass

        with open('test_lazymodule.py', 'w') as f:
            f.write(contents)

    def assertModule(module, expected_module_count, expected_function_count):
        """
        Assert the module is correct.
        """
        assert isinstance(module, _LazyModuleMarker)


# Generated at 2022-06-14 06:15:10.915216
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    import os
    import unittest
    from types import ModuleType
    from tempfile import mkdtemp
    from shutil import rmtree
    from os.path import join

    class TestCase(unittest.TestCase):

        def setUp(self):
            super(TestCase, self).setUp()
            self._old_path = sys.path
            self.test_dir_1 = mkdtemp()
            self.test_dir_2 = mkdtemp()
            sys.path = [self.test_dir_1, self.test_dir_2]

        def tearDown(self):
            sys.path = self._old_path
            rmtree(self.test_dir_1)
            rmtree(self.test_dir_2)
            super(TestCase, self).tear

# Generated at 2022-06-14 06:15:21.541220
# Unit test for function make_lazy
def test_make_lazy():
    import sys

    class FakeModule(object):
        """
        A fake module that does absolutely nothing.
        """
        def __init__(self):
            pass

    make_lazy('fake_module')
    lazy_module = sys.modules['fake_module']
    assert lazy_module is not None
    assert not isinstance(lazy_module, FakeModule)
    assert not isinstance(lazy_module, ModuleType)
    lazy_module.__getattribute__('foo')
    assert isinstance(lazy_module, ModuleType)
    assert isinstance(lazy_module, FakeModule)

# Generated at 2022-06-14 06:15:27.589751
# Unit test for function make_lazy
def test_make_lazy():
    if sys.version_info.major < 3:
        return
    def _assert_lazy():
        try:
            return lambda: isinstance(sys.modules['functools'], _LazyModuleMarker)
        except KeyError:
            return lambda: True
    assert _assert_lazy()()
    assert hashlib.md5
    assert _assert_lazy()()

# Generated at 2022-06-14 06:15:41.363406
# Unit test for function make_lazy
def test_make_lazy():
    import pkgutil
    # We should be able to get a module that hasn't been imported yet
    # without importing it.
    module_name = 'sparkmagic.utils._make_lazy'
    assert module_name not in sys.modules
    make_lazy(module_name)
    # The module should be lazily imported.  Importing it should not work
    # normally, and attempting to import it should raise an error.
    try:
        __import__(module_name)
        assert False, ("Module {0} should not be importable normally "
                       "when lazy".format(module_name))
    except:
        pass
    # When we access an attribute off of the module, it should be importable
    # normally.
    module_obj = pkgutil.get_loader(module_name).load_module()
   

# Generated at 2022-06-14 06:15:46.408366
# Unit test for function make_lazy
def test_make_lazy():
    """
    Make sure make_lazy works as intented.
    """
    # The normal import case
    import sys
    assert sys is not None

    # The lazy module case
    make_lazy("sys")
    import sys  # noqa:F811
    assert sys is not None
    assert isinstance(sys, _LazyModuleMarker)

    # The lazy module with access to an attribute
    import sys  # noqa:F811
    assert sys is not None
    assert isinstance(sys, _LazyModuleMarker)
    assert sys.path is not None

# Generated at 2022-06-14 06:15:55.642639
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    import os.path
    module_path = os.path.realpath(__file__)
    sys.modules['test_make_lazy'] = sys_modules_temp = {}
    make_lazy(module_path)
    assert isinstance(sys.modules['test_make_lazy'], _LazyModuleMarker)
    assert sys.modules['test_make_lazy'] is not None
    from .test_lazymodule import test_make_lazy
    assert test_make_lazy is not None
    assert test_make_lazy.test_make_lazy is not None
    assert sys.modules['test_make_lazy'] is not sys_modules_temp
    assert test_make_lazy is sys.modules['test_make_lazy']

# Generated at 2022-06-14 06:16:03.489241
# Unit test for function make_lazy
def test_make_lazy():
    import sys_modules

    make_lazy('sys_modules')

    # Make sure no modifications to the module path
    assert sys_modules.__name__ == 'sys_modules'

    # Make sure we are lazy
    assert isinstance(sys_modules, _LazyModuleMarker)

    # Make sure the actual attribute is accessible
    assert sys_modules.HEY == 'there'

    # Make sure we are not lazy
    assert not isinstance(sys_modules, _LazyModuleMarker)


# Testing data for module 'sys_modules'
HEY = 'there'

# Generated at 2022-06-14 06:16:14.278492
# Unit test for function make_lazy
def test_make_lazy():
    sys_modules = sys.modules  # cache in the locals

    def _is_lazy_module(mod):
        "Helper function to check if the module is lazy"
        return isinstance(mod, _LazyModuleMarker)

    # test make_lazy function
    # 1. a new module: mod
    mod = 'foo.bar'
    make_lazy(mod)
    assert mod in sys_modules
    assert _is_lazy_module(sys_modules[mod])

    # 2. existing module
    mod_path = 'sys'
    mod = sys.modules[mod_path]
    make_lazy(mod_path)
    assert mod_path in sys_modules
    assert sys_modules[mod_path] is mod
    assert not _is_lazy_module(mod)

    # 3. existing

# Generated at 2022-06-14 06:16:25.031857
# Unit test for function make_lazy
def test_make_lazy():
    import sys

    before = "before"
    after = "after"

    # create a module
    mod = sys.modules.setdefault("test_make_lazy", types.ModuleType("test_make_lazy"))
    mod.__file__ = "test"

    # Add an attribute to the module
    mod.before = before

    # Lazy module
    make_lazy("test_make_lazy")

    assert not hasattr(mod, "after"), "Lazy module doesn't have attribute before lazyness"

    # add an attribute to the module
    mod.after = after

    assert hasattr(mod, "after"), "Lazy module has attribute after lazyness"

    assert "after" in dir(mod), "Lazy module has attribute after lazyness in dir"

    del sys.modules["test_make_lazy"]

# Generated at 2022-06-14 06:16:30.601002
# Unit test for function make_lazy
def test_make_lazy():
    import sys

    make_lazy('foo')
    assert isinstance(sys.modules['foo'], _LazyModuleMarker)
    assert sys.modules['foo'].__class__.__mro__ == (sys.modules['foo'].__class__, ModuleType)



# Generated at 2022-06-14 06:16:37.134868
# Unit test for function make_lazy
def test_make_lazy():
    import imp

    # Hack to load a module into our test space.
    mod = imp.new_module('mod')
    mod.foo = 'bar'
    sys.modules['mod'] = mod

    make_lazy('mod')
    assert isinstance(mod, _LazyModuleMarker)
    assert mod.foo == 'bar'
    assert not isinstance(mod, _LazyModuleMarker)



# Generated at 2022-06-14 06:16:47.985415
# Unit test for function make_lazy
def test_make_lazy():
    import django
    make_lazy('django')  # 1) Django not imported
    assert isinstance(django, _LazyModuleMarker)
    assert not hasattr(django, 'VERSION')  # 2) AttributeError
    assert hasattr(django, 'VERSION')  # 3) Django imported

# Generated at 2022-06-14 06:16:58.993178
# Unit test for function make_lazy
def test_make_lazy():
    def abc_test():
        try:
            from abc import ABCMeta
            return True
        except ImportError:
            return False
    # First import, from abc module
    make_lazy('abc')
    assert abc_test()
    # Reimport, from abc module.
    make_lazy('abc')
    assert abc_test()
    # Reimport, from six.moves module.
    make_lazy('six.moves')
    assert abc_test()
    # Reimport, from six.moves.builtins module.
    make_lazy('six.moves.builtins')
    assert abc_test()


if PY3:
    raise_from = raise_from

# Generated at 2022-06-14 06:17:04.538787
# Unit test for function make_lazy
def test_make_lazy():
    prefix = 'test_make_lazy'
    make_lazy(prefix)
    import test_make_lazy
    assert prefix in sys.modules
    assert isinstance(sys.modules[prefix], _LazyModuleMarker)
    del sys.modules[prefix]



# Generated at 2022-06-14 06:17:15.446722
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    if sys.modules.has_key('frozendict'):
        del sys.modules['frozendict']

    import frozendict

    # tests that the module was imported normally
    assert isinstance(frozendict, ModuleType)
    assert frozendict.__name__ == "frozendict"

    # make the frozen dict lazy
    make_lazy('frozendict')

    from frozendict import frozendict

    # tests that the module was made lazy
    assert frozendict.__name__ == "frozendict"
    assert isinstance(frozendict, _LazyModuleMarker)

    # tests that frozendict still works

# Generated at 2022-06-14 06:17:29.714567
# Unit test for function make_lazy
def test_make_lazy():
    """
    Make sure that `make_lazy` actually works.
    """
    try:
        import os.path
    except ImportError:
        return

    # Hack in a global, so that we can check if it is properly loaded
    os.path._TEST_VAR = False

    make_lazy('os.path')
    assert sys.modules['os.path'] is not None
    assert not sys.modules['os.path']._TEST_VAR
    assert sys.modules['os.path'].__mro__ == (sys.modules['os.path'], ModuleType)

    os.path._TEST_VAR = True
    os.path.sep
    assert sys.modules['os.path']._TEST_VAR

# Generated at 2022-06-14 06:17:36.966365
# Unit test for function make_lazy
def test_make_lazy():
    mod = __import__('make_lazy')

    assert isinstance(mod, _LazyModuleMarker)

    reload = getattr(mod, 'reload')

    assert not isinstance(reload, _LazyModuleMarker)

    assert reload(mod) is mod

    assert type(reload(mod)) is ModuleType


test_make_lazy()

# Generated at 2022-06-14 06:17:46.262886
# Unit test for function make_lazy
def test_make_lazy():
    import math
    import os.path
    make_lazy("os.path")
    assert not isinstance(os.path, _LazyModuleMarker)
    assert not isinstance(math, _LazyModuleMarker)
    abspath = os.path.abspath
    abspath("")
    assert isinstance(os.path, _LazyModuleMarker)
    assert not isinstance(math, _LazyModuleMarker)

# Generated at 2022-06-14 06:17:54.568079
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    import uuid
    import mock
    module_name = str(uuid.uuid1())
    make_lazy(module_name)
    assert module_name in sys.modules
    assert isinstance(sys.modules[module_name], _LazyModuleMarker)
    import_method = mock.MagicMock()
    getattr_method = mock.MagicMock()
    with mock.patch('__builtin__.__import__', import_method):
        with mock.patch('__builtin__.getattr', getattr_method):
            sys.modules[module_name].test()
    import_method.assert_called_once_with(module_name)
    getattr_method.assert_called_once_with(
        import_method.return_value,
        'test',
    )

# Generated at 2022-06-14 06:18:02.246565
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    import os
    import shutil

    # Make a test dir
    test_dir = 'my_test_dir'
    if not os.path.isdir(test_dir):
        os.makedirs(test_dir)

    # Create a test python file
    module_name = 'my_test_module'
    with open('{}/{}.py'.format(test_dir, module_name), 'w') as f:
        f.write('hello_string = "Hello World!"')
    sys.path.append(test_dir)

    # Test case 1.
    # Run `import my_test_module` before `make_lazy` is called
    make_lazy(module_name)
    # Now, the actual module is loaded

# Generated at 2022-06-14 06:18:07.797876
# Unit test for function make_lazy
def test_make_lazy():
    import os

# Generated at 2022-06-14 06:18:18.919628
# Unit test for function make_lazy
def test_make_lazy():
    """
    Test make_lazy to see if it marks a module to be lazy.
    """
    lazy_module_name = '__lazy__'
    module_name = '__non_lazy__'

    make_lazy(lazy_module_name)
    sys.modules[module_name] = ModuleType(__name__)

    # check if a module is lazily loaded
    assert isinstance(sys.modules[lazy_module_name], _LazyModuleMarker)

    # check for a non-lazy module
    assert not isinstance(sys.modules[module_name], _LazyModuleMarker)

if __name__ == '__main__':
    test_make_lazy()

# Generated at 2022-06-14 06:18:26.795317
# Unit test for function make_lazy
def test_make_lazy():
    sys.modules['django.utils.importlib'] = utils = ModuleType('django.utils.importlib', 'Dummy doc')
    utils.__file__ = '/django/utils/importlib.py'
    make_lazy('django.utils.importlib')
    assert isinstance(importlib, _LazyModuleMarker)
    assert importlib.__name__ == 'django.utils.importlib'
    assert importlib.__doc__ == 'Dummy doc'
    assert importlib.__file__ == '/django/utils/importlib.py'

# Generated at 2022-06-14 06:18:33.255223
# Unit test for function make_lazy
def test_make_lazy():
    import types

    assert sys.modules == {}
    make_lazy('os')

    assert sys.modules['os'].__class__ == types.ModuleType

    # Import the module
    import os

    # Should be the same as the one above
    assert sys.modules['os'] is os
    assert sys.modules['os'].__class__ == types.ModuleType

# Generated at 2022-06-14 06:18:36.092398
# Unit test for function make_lazy
def test_make_lazy():
    make_lazy('pytest')
    assert isinstance(pytest, _LazyModuleMarker)

# Generated at 2022-06-14 06:18:40.761680
# Unit test for function make_lazy
def test_make_lazy():
    assert 'make_lazy_test' not in sys.modules
    make_lazy('make_lazy_test')
    assert 'make_lazy_test' in sys.modules
    assert type(sys.modules['make_lazy_test']) == _LazyModuleMarker

# Generated at 2022-06-14 06:18:44.691514
# Unit test for function make_lazy
def test_make_lazy():
    """
    Test function make_lazy
    """
    try:
        make_lazy('test_lazy')
        import test_lazy
    except ImportError:
        assert False

# Generated at 2022-06-14 06:18:59.306320
# Unit test for function make_lazy
def test_make_lazy():
    import os
    import sys
    import tempfile

    def create_dummy_module(module_name, path, init_code):
        with tempfile.NamedTemporaryFile(
            prefix=module_name + '.py',
            suffix='.tmp',
            mode='w',
            delete=False,
            dir=path,
        ) as fp:
            fp.write(init_code)

        return fp

    root = tempfile.mkdtemp()
    mpath = os.path.realpath(os.path.join(root, os.path.dirname(__file__)))
    sys.path.insert(0, mpath)

    # Create a dummy module to test with.

# Generated at 2022-06-14 06:19:12.895220
# Unit test for function make_lazy
def test_make_lazy():
    # Test the basics of make_lazy and make sure it works appropriately
    # with __import__.

    # We're going to do some evil things here, hence the pylint disable.
    # pylint: disable=W0212
    sys_modules = sys.modules  # cache in the locals
    sys_modules['foo'] = 'bar'

    make_lazy('foo')

    # Make sure we can import foo and that it's the right type.
    assert 'foo' not in sys.modules
    assert sys_modules['foo'] == 'bar'
    foo = __import__('foo')

    assert isinstance(foo, _LazyModuleMarker)
    assert 'foo' not in sys_modules

    # Make sure we can't get at foo.bar directly.

# Generated at 2022-06-14 06:19:25.870719
# Unit test for function make_lazy
def test_make_lazy():
    # get the function make_lazy
    import inspect
    code = inspect.getsource(make_lazy)
    code = textwrap.dedent(code).replace('NonLocal(None)', 'None')

    locals_ = locals()
    exec(code, globals(), locals_)
    make_lazy = locals_['make_lazy']

    # import the real module lazily
    make_lazy('time')
    import sys

    # check __class__
    assert sys.modules['time'].__class__.__name__ == 'LazyModule'
    # check __getattribute__
    assert sys.modules['time'].__getattribute__('time')
    # check that the module is moved from LazyModule
    assert 'time' not in sys.modules
    # check that the module is in sys.modules
   

# Generated at 2022-06-14 06:19:36.253273
# Unit test for function make_lazy
def test_make_lazy():
    """
    Test function that tests the make_lazy function.
    """
    test_module = 'unittest.make_lazy.test_module'
    sys.modules[test_module] = None
    make_lazy(test_module)

    # Assert that we are in the same list.
    assert sys.modules[test_module] == test_module

    # Assert that we were able to get the sys.modules key/value pair
    assert sys.modules[test_module] is not None

    # Assert that we were able to get the module
    assert isinstance(sys.modules[test_module], _LazyModuleMarker) is True

    # Assert that we were able to get the module attributes
    assert sys.modules[test_module].__name__ is test_module

    # Assert that we were able

# Generated at 2022-06-14 06:19:44.787327
# Unit test for function make_lazy
def test_make_lazy():
    """
    Simple unit test for make_lazy
    """
    assert_raises_regexp(ImportError, "no module named foo", __import__, "foo")
    make_lazy("foo")
    assert_raises_regexp(AttributeError, "foo has no attribute bar",
                         getattr, sys.modules["foo"], "bar")


# Functions to mark lazy import modules
make_lazy("sentinel")
make_lazy("faker")
make_lazy("pygeoip")

# Generated at 2022-06-14 06:19:46.681766
# Unit test for function make_lazy
def test_make_lazy():
    make_lazy('foo')
    assert isinstance(sys.modules['foo'], _LazyModuleMarker)



# Generated at 2022-06-14 06:20:00.269792
# Unit test for function make_lazy
def test_make_lazy():
    # removing sys.modules[__name__] from sys.modules
    # as it is automatically added during import
    # and it will be required for the test to function properly
    del sys.modules[__name__]
    make_lazy("framework.custom.lazy")
    # importing the lazily loaded module
    from framework.custom.lazy import make_lazy
    # importing this module again because we are trying to access
    # a lazy module from a lazy module and it may potentially cause a
    # recursion exception
    from framework.custom.lazy import make_lazy
    # making sure the module is correctly loaded
    import framework.custom.lazy
    # making sure the module is correctly loaded
    import framework.custom.lazy
    # making sure the function works
    make_lazy("framework.custom.lazy")

# Generated at 2022-06-14 06:20:06.446809
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    sys.modules["foo"] = None
    make_lazy("foo")
    assert isinstance(sys.modules["foo"], _LazyModuleMarker)
    assert "foo" in sys.modules
    import foo
    assert isinstance(foo, ModuleType)
    assert sys.modules["foo"] is foo
    del sys.modules["foo"]

# Generated at 2022-06-14 06:20:13.494765
# Unit test for function make_lazy
def test_make_lazy():
    from six.moves import reload_module
    import os
    import tests

    module_path = os.getcwd() + '/tests.py'
    make_lazy(module_path)

    assert(isinstance(tests, _LazyModuleMarker))
    reload_module(tests)
    assert(not isinstance(tests, _LazyModuleMarker))

# Generated at 2022-06-14 06:20:18.898045
# Unit test for function make_lazy
def test_make_lazy():
    import os

    module_path = 'os'
    make_lazy(module_path)
    mod = sys.modules[module_path]
    assert isinstance(mod, _LazyModuleMarker)
    assert not hasattr(mod, 'path')
    assert os.path is sys.modules[module_path].path


# Generated at 2022-06-14 06:20:31.227076
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    import os
    import stat
    import importlib
    import tempfile

    # Create a temp directory and chdir to it
    tmpdir = tempfile.mkdtemp()
    os.chdir(tmpdir)

    # Create a module and add to sys.path

# Generated at 2022-06-14 06:20:43.862183
# Unit test for function make_lazy
def test_make_lazy():
    lazy_module_name = 'test_lazy_module'
    # Simulate the importation of a module inside a package
    sys.modules[".%s" % lazy_module_name] = True
    import_path = '%s.%s' % (__name__, lazy_module_name)

    old_lazy = sys.modules.get(import_path)

    make_lazy(import_path)

    new_lazy = sys.modules[import_path]

    assert old_lazy is None
    assert isinstance(new_lazy, _LazyModuleMarker)
    assert new_lazy.__name__ == import_path
    assert new_lazy.__class__.__name__ == 'LazyModule'

    lazy_module = __import__(import_path)

    assert lazy_module

# Generated at 2022-06-14 06:20:50.577547
# Unit test for function make_lazy
def test_make_lazy():
    module = 'test_make_lazy'

    assert module not in sys.modules

    make_lazy(module)

    assert isinstance(sys.modules[module], _LazyModuleMarker)
    assert sys.modules[module].__file__.endswith('__init__.py')

    sys.modules[module].foo = 1

    assert sys.modules[module].foo == 1

# Generated at 2022-06-14 06:20:56.685588
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    make_lazy('mock_lazy_module')
    assert sys.modules['mock_lazy_module'].__class__.__module__ == 'tests.common.lazy_loader'
    assert isinstance(sys.modules['mock_lazy_module'], _LazyModuleMarker)
# end of unit test

# Generated at 2022-06-14 06:21:08.348460
# Unit test for function make_lazy
def test_make_lazy():
    import test_make_lazy
    assert isinstance(test_make_lazy, _LazyModuleMarker)
    assert test_make_lazy.__name__ == 'test_make_lazy'
    assert test_make_lazy.__getattribute__('__name__') == 'test_make_lazy'
    assert test_make_lazy.__getattribute__('__name__') is test_make_lazy.__name__
    assert test_make_lazy.__getattribute__('__mro__') != test_make_lazy.__mro__
    assert isinstance(test_make_lazy, ModuleType)



# Generated at 2022-06-14 06:21:19.243051
# Unit test for function make_lazy
def test_make_lazy():
    import unittest

    class A(object):
        def __init__(self, x):
            self.x = x

    class A(object):
        def __init__(self, x):
            self.x = x

        def f(self):
            return self.x

    class B(object):
        def __init__(self, x):
            self.x = x

        def f(self):
            return self.x

    class C(object):
        def __init__(self, x):
            self.x = x

        def f(self):
            return self.x

    class D(object):
        def __init__(self, x):
            self.x = x

        def f(self):
            return self.x


# Generated at 2022-06-14 06:21:32.190273
# Unit test for function make_lazy
def test_make_lazy():
    """ Unit test for make lazy"""

    # ../../test_module.py
    #   test_module.a = 2
    #   test_module.b = "asdf"

    test_module_path = "nltk.internals.test_module"

    make_lazy(test_module_path)

    # ../../test_module2.py
    #   test_module2.a = 4
    #   test_module2.c = "qwer"

    test_module2_path = "nltk.internals.test_module2"

    make_lazy(test_module2_path)

    # test_module.a  and  test_module2.a
    # -> should not equal
    # -> should not raise any import error

    # test_module.a  !=  test_

# Generated at 2022-06-14 06:21:39.314511
# Unit test for function make_lazy
def test_make_lazy():
    make_lazy('foo')

    # check that foo is a LazyModule
    import foo
    assert isinstance(foo, _LazyModuleMarker)

    # check that foo.x is not a LazyModule
    foo.x = 1
    assert foo.x == 1
    assert not isinstance(foo.x, _LazyModuleMarker)


if __name__ == '__main__':
    test_make_lazy()

# Generated at 2022-06-14 06:21:51.626249
# Unit test for function make_lazy
def test_make_lazy():
    try:
        import foo.bar.baz
    except ImportError:
        pass
    else:
        raise AssertionError('import foo.bar.baz should fail as it is not a valid module')

    make_lazy('foo.bar.baz')
    import foo.bar.baz
    assert isinstance(foo.bar.baz, _LazyModuleMarker)

    # This import should fail as the module isn't loaded yet.
    try:
        import foo.bar.baz.test
    except ImportError:
        pass
    else:
        raise AssertionError('foo.bar.baz.test should not be accessible')

    # Now import a submodule and make sure it's still a LazyModule
    from foo.bar.baz import test  # pylint: disable=unused-variable



# Generated at 2022-06-14 06:22:00.997958
# Unit test for function make_lazy
def test_make_lazy():
    # this will fail if the module is not lazy
    try:
        make_lazy('importlib_metadata')
        import importlib_metadata
        assert isinstance(importlib_metadata, _LazyModuleMarker)
    except ImportError:
        pass

    try:
        make_lazy('importlib_metadata.version')
        import importlib_metadata
        importlib_metadata.version
    except ImportError:
        pass
    else:
        raise AssertionError('importlib_metadata.version import should have failed')

# Generated at 2022-06-14 06:22:21.116433
# Unit test for function make_lazy
def test_make_lazy():
    import inspect
    import sys

    class Module(object):
        pass

    test_module_path = 'test_module'

    module = Module()
    module.__name__ = test_module_path

    sys.modules[test_module_path] = module

    make_lazy(test_module_path)

    try:
        assert sys.modules[test_module_path] is not module
        assert isinstance(sys.modules[test_module_path], _LazyModuleMarker)

        # check that we can get an attribute off our lazy module.
        sys.modules[test_module_path].IDENTIFIER
    finally:
        del sys.modules[test_module_path]



# Generated at 2022-06-14 06:22:31.541883
# Unit test for function make_lazy
def test_make_lazy():
    import os

    sys.modules['test'] = None

    make_lazy('test')

    assert ('test' in sys.modules) is True

    assert isinstance(sys.modules['test'], _LazyModuleMarker) is True

    assert hasattr(sys.modules['test'], '__repr__') is False

    assert hasattr(sys.modules['test'], '__file__') is False

    assert hasattr(sys.modules['test'], '__loader__') is False

    assert hasattr(sys.modules['test'], '__package__') is False

    # Just ensure that we don't accidentally call __import__
    sys.modules['os'] = None

    assert ('os' in sys.modules) is True

    assert hasattr(os, '__repr__') is False


# Generated at 2022-06-14 06:22:41.115499
# Unit test for function make_lazy
def test_make_lazy():
    """
    Test that make lazy works for the most basic case.
    """

    import os
    import sys
    import types

    mod = types.ModuleType('test_make_lazy')
    mod.__package__ = 'test_make_lazy'
    mod.__loader__ = None
    mod.__name__ = 'test_make_lazy'

    make_lazy('os')
    make_lazy('test_make_lazy')
    assert sys.modules['os'] is not os
    assert sys.modules['test_make_lazy'] is not mod
    assert 'test_make_lazy' not in sys.modules
    sys.modules['test_make_lazy'] = mod
    assert 'test_make_lazy' in sys.modules

    sys.modules['os'] is os  # importing from

# Generated at 2022-06-14 06:22:54.545939
# Unit test for function make_lazy
def test_make_lazy():
    # Installed packages
    assert sys.modules["sys"] is sys

    assert isinstance(sys, ModuleType)
    make_lazy("sys")
    assert isinstance(sys, _LazyModuleMarker)
    assert isinstance(sys, ModuleType)
    assert sys.__name__ == "sys"

    # Uninstalled packages
    assert "tst" not in sys.modules
    assert isinstance(tst, ModuleType)
    make_lazy("tst")
    assert isinstance(tst, _LazyModuleMarker)
    assert isinstance(tst, ModuleType)
    assert tst.__name__ == "tst"

    # Lazy attributes
    assert tst.test.__name__ == "tst.test"
    assert tst.test.test_int == 815
    assert tst

# Generated at 2022-06-14 06:23:01.158187
# Unit test for function make_lazy
def test_make_lazy():
    __import__('__future__').print_function

    make_lazy('__future__')
    assert isinstance(__future__, _LazyModuleMarker)

    # make sure that accessing attributes loads the module
    print_function = __future__.print_function
    assert print_function is not _LazyModuleMarker
    assert print_function is not __future__
    assert isinstance(__future__, ModuleType)

# Generated at 2022-06-14 06:23:10.588509
# Unit test for function make_lazy
def test_make_lazy():
    """
    Test function make_lazy
    """
    import sys
    sys.modules.pop('kio.lazy_module_test', None)
    sys.modules.pop('kio.tests.test_lazy_module', None)

    make_lazy('kio.lazy_module_test')

    from kio.lazy_module_test import lazy_module_test

    assert isinstance(lazy_module_test, _LazyModuleMarker)

# Generated at 2022-06-14 06:23:19.873981
# Unit test for function make_lazy
def test_make_lazy():
    class A(object):
        pass
    class B(object):
        pass

    with patch('sys.modules') as mocked_sys_modules:
        mocked_sys_modules['foo'] = A()
        make_lazy('foo')

        assert isinstance(mocked_sys_modules['foo'], LazyModule)

        with patch('__builtin__.__import__') as mocked_import:
            mocked_import.side_effect = lambda x: B()
            # Accessing attribute 'bar' should cause import
            assert 'bar' in dir(mocked_sys_modules['foo'])
            assert not isinstance(mocked_sys_modules['foo'], LazyModule)
            assert isinsta

# Generated at 2022-06-14 06:23:30.715185
# Unit test for function make_lazy
def test_make_lazy():
    # Emulate the Bazel behavior.
    import sys
    sys.modules.pop('lazy_loader')

    make_lazy('lazy_loader')
    import lazy_loader
    assert isinstance(lazy_loader, _LazyModuleMarker)
    assert lazy_loader.__name__ == 'lazy_loader'
    assert lazy_loader.__path__ == ['lazy_loader']

    # Test that module is not imported until an attribute is needed.
    try:
        module_import_fail
    except NameError:
        pass
    else:
        assert False, "Module was imported when it shouldn't have been."

    lazy_loader.module_import_ok = True
    import lazy_loader
    lazy_loader.module_import_fail

# Generated at 2022-06-14 06:23:35.826124
# Unit test for function make_lazy
def test_make_lazy():
    assert sys.modules.get('test_make_lazy') == None

    make_lazy('test_make_lazy')

    assert isinstance(sys.modules['test_make_lazy'], _LazyModuleMarker)
    assert sys.modules['test_make_lazy'].__mro__() == (None, None)

    import test_make_lazy
    assert sys.modules['test_make_lazy'] == test_make_lazy
    assert test_make_lazy.__mro__() == (None, None)

# Generated at 2022-06-14 06:23:49.354589
# Unit test for function make_lazy
def test_make_lazy():
    module_name = 'djblets.tests.test_lazy_load'
    file_name = __file__.replace('.pyc', '.py')

    def reset_sys_modules():
        # Mock sys.modules for testing
        sys.modules = dict((k, v) for k, v in sys.modules.items()
                           if not k.startswith('djblets.tests.'))

    reset_sys_modules()

    # djblets.tests.test_lazy_load should not have been imported yet
    try:
        import djblets.tests.test_lazy_load
    except ImportError:
        pass
    else:
        raise Exception('djblets.tests.test_lazy_load was already imported')

    # Make djblets.tests.test_lazy_load lazy
    make

# Generated at 2022-06-14 06:24:18.612498
# Unit test for function make_lazy
def test_make_lazy():

    # Create a temporary module for testing
    import tempfile
    import os
    fd, path = tempfile.mkstemp(suffix='.py')

    module_name = 'test_lazy'
    module_path = module_name

    # Write some code to the module
    os.write(fd, 'test_var = "test"')
    os.close(fd)

    make_lazy(module_path)

    import test_lazy

    assert not hasattr(test_lazy, 'test_var')

    test_lazy.test_var

    assert hasattr(test_lazy, 'test_var')

# Generated at 2022-06-14 06:24:23.972609
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    import getpass
    make_lazy("getpass")
    assert sys.modules['getpass'] is not None
    assert isinstance(sys.modules['getpass'], _LazyModuleMarker)
    sys.modules['getpass'].getuser()

# Generated at 2022-06-14 06:24:37.661479
# Unit test for function make_lazy
def test_make_lazy():
    import inspect

    assert 'make_lazy' not in sys.modules

    make_lazy('make_lazy')

    assert 'make_lazy' in sys.modules
    assert 'test_make_lazy' not in sys.modules['make_lazy']

    sys.modules['make_lazy'].test_make_lazy()

    assert 'test_make_lazy' in sys.modules['make_lazy']
    assert 'inspect' not in sys.modules, \
        "make_lazy should only load needed modules"

    assert isinstance(
        sys.modules['make_lazy'],
        _LazyModuleMarker
    ), "make_lazy should return a LazyModule"

    mod = sys.modules['make_lazy']
