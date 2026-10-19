

# Generated at 2022-06-14 06:14:45.443495
# Unit test for function make_lazy
def test_make_lazy():
    make_lazy('sys')
    assert isinstance(sys, _LazyModuleMarker)
    print(sys.version)
    assert sys.copyright == 'Copyright (c) 2001-2014 Python Software Foundation.\nAll Rights Reserved.\n\nCopyright (c) 2000 BeOpen.com.\nAll Rights Reserved.\n\nCopyright (c) 1995-2001 Corporation for National Research Initiatives.\nAll Rights Reserved.\n\nCopyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.\nAll Rights Reserved.'

# Generated at 2022-06-14 06:14:55.698062
# Unit test for function make_lazy
def test_make_lazy():
    """
    Tests make_lazy() method
    """
    sys.modules.pop('test.lazyload.example', None)


# Generated at 2022-06-14 06:15:02.735134
# Unit test for function make_lazy
def test_make_lazy():
    """
    Test the module is imported when an attribute is looked up
    """
    sys.modules['foo'] = None
    make_lazy('foo')

    # force module to be imported
    result = sys.modules['foo'].test = lambda: 1
    assert sys.modules['foo'].test() == 1
    result()

    # reset module so the next import is possible
    del sys.modules['foo']

# Generated at 2022-06-14 06:15:08.838290
# Unit test for function make_lazy
def test_make_lazy():
    """
    Unit test for the make_lazy function.
    """
    import os
    import tempfile

    module_name = 'tempmodule'
    module_file = tempfile.NamedTemporaryFile(suffix='.py')
    module_file.write('import time')
    module_file.flush()

    module_path = os.path.join('.', module_file.name)

    make_lazy(module_path)

    assert module_name not in sys.modules
    import tempmodule
    assert module_name in sys.modules
    assert module_name in sys.modules

# Generated at 2022-06-14 06:15:20.586818
# Unit test for function make_lazy
def test_make_lazy():
    import pprint
    import sys

    test_mod = sys.modules.pop('test_mod', None)
    if test_mod is not None:
        del test_mod

    lazy_module_path = 'tests.test_lazy_module'

    make_lazy(lazy_module_path)

    test_mod = sys.modules[lazy_module_path]

    assert isinstance(test_mod, _LazyModuleMarker)
    assert test_mod.__name__ == 'tests.test_lazy_module'
    assert test_mod.__module__ == 'tests.test_lazy_module'
    assert test_mod.__file__.endswith('tests/test_lazy_module.py')
    assert isinstance(test_mod.__doc__, str)

# Generated at 2022-06-14 06:15:29.596544
# Unit test for function make_lazy
def test_make_lazy():
    class A(object):
        def foo(self):
            pass

    assert A.foo is not None

    # Make a new module and add A to it
    import new
    new_module = new.module('test_module')
    new_module.A = A

    # Import A from the new module and delete the module
    make_lazy('test_module')
    import test_module as module
    assert module.A.foo is not None
    del sys.modules['test_module']
    assert module.A.foo is None

# Generated at 2022-06-14 06:15:37.987331
# Unit test for function make_lazy
def test_make_lazy():

    if imp is None:
        return  # no imp module in python3

    # We cannot test this in the same process that runs the tests, so we have to
    # fork a new test process. Linux is able to re-use the same address space for
    # the forked process, so the memory is still there and the previous code is
    # still running. MacOS is not able to do this, so it will run the test in a
    # new address space and pass the test.
    if sys.platform.startswith('win'):
        raise unittest.SkipTest("Skipping test_make_lazy() because Windows does not support forking")

# Generated at 2022-06-14 06:15:51.119302
# Unit test for function make_lazy
def test_make_lazy():
    """
    Tests that `mark_lazy` is working.
    """
    mod = 'simple.lazy'
    make_lazy(mod)

    # check that importing module correctly marked module as lazy
    assert isinstance(sys.modules[mod], _LazyModuleMarker)

    # check that after accessing module that it is no longer lazy
    assert sys.modules[mod].a == 42
    assert not isinstance(sys.modules[mod], _LazyModuleMarker)

    # check that deleting module and reaccessing makes it lazy again
    del sys.modules[mod]
    assert isinstance(sys.modules[mod], _LazyModuleMarker)
    assert sys.modules[mod].a == 42
    assert not isinstance(sys.modules[mod], _LazyModuleMarker)

# Generated at 2022-06-14 06:15:55.583793
# Unit test for function make_lazy
def test_make_lazy():
    make_lazy('sentry.lazy_tests.foo')
    assert 'sentry.lazy_tests.foo' not in sys.modules
    from sentry.lazy_tests import foo
    assert 'sentry.lazy_tests.foo' in sys.modules
    assert isinstance(foo, _LazyModuleMarker)
    assert isinstance(foo, ModuleType)
    assert hasattr(foo, 'answer')
    assert foo.answer == 42

# Generated at 2022-06-14 06:16:01.209144
# Unit test for function make_lazy
def test_make_lazy():
    make_lazy('mock_module')
    assert isinstance(sys.modules['mock_module'], _LazyModuleMarker)
    assert 'loaded' not in sys.modules
    assert sys.modules['mock_module'].loaded == 'loaded'
    assert 'loaded' in sys.modules

# Generated at 2022-06-14 06:16:14.104951
# Unit test for function make_lazy
def test_make_lazy():
    """
    Test make_lazy function
    """
    # Clean up sys.modules to make it a clean slate.
    sys.modules = {}

    # Check that it's empty
    assert len(sys.modules) == 0

    def try_import_test():
        """
        Try to import the module test
        """
        # Make sure that the test module is not already loaded.
        assert not hasattr(sys.modules, 'test')

        # Call make_lazy
        make_lazy('test')

        # Check that the module is not in sys.modules
        assert 'test' not in sys.modules
        # Check that it's in the dict
        assert sys.modules['test'][0] == '_'
    try_import_test()

    # Check that the module has not been loaded.
    from test import test_

# Generated at 2022-06-14 06:16:24.956700
# Unit test for function make_lazy
def test_make_lazy():
    import os
    import collections

    from sphinx import util
    from sphinx.util import _LazyModuleMarker

    module_path = 'collections'

    # Make sure collection is not lazy and does not exist
    assert module_path not in sys.modules

    # Make sure the module is not an instance of the LazyModuleMarker
    assert not isinstance(util.rst, _LazyModuleMarker)

    # Get the collections module
    cur_collection = collections

    # Make sure it is in sys.modules
    assert module_path in sys.modules

    # Make collections a LazyModule
    make_lazy(module_path)

    # Make sure collection is now a LazyModule
    assert isinstance(collections, _LazyModuleMarker)

    # Make sure it is still in sys.modules

# Generated at 2022-06-14 06:16:38.339890
# Unit test for function make_lazy
def test_make_lazy():
    """
    Make a package name and then check if the package is in the
    system modules, this tests that importing a lazy module with
    make_lazy doesn't actually import the module.
    """
    # This module name shouldn't exist, so we can test if make_lazy works
    # by checking if it is in the sys.modules dictionary
    module_name = 'test_make_lazy.{0}'.format(uuid.uuid4())

    assert module_name not in sys.modules

    make_lazy(module_name)

    assert isinstance(sys.modules[module_name], _LazyModuleMarker)
    assert module_name in sys.modules

    assert hasattr(sys.modules[module_name], 'uniform')

    assert isinstance(sys.modules[module_name], ModuleType)
    assert module

# Generated at 2022-06-14 06:16:43.458102
# Unit test for function make_lazy
def test_make_lazy():
    sys_modules = sys.modules
    if 'test_make_lazy' in sys_modules:
        # Prevent the original name of this function from
        # being in the sys.modules, it will be replaced
        # by the LazyModule created here.
        del sys_modules['test_make_lazy']

    make_lazy('make_lazy.test_make_lazy')

    # Import the module we just made lazy, this will
    # force the lazy module to be loaded.
    from make_lazy.test_make_lazy import test

    assert(test() == 'foo')

# Generated at 2022-06-14 06:16:48.954862
# Unit test for function make_lazy
def test_make_lazy():
    import os
    make_lazy('os')
    assert not hasattr(os, 'name')

    os.path.split('/foo/bar')
    assert hasattr(os, 'name')

    assert isinstance(os, _LazyModuleMarker)
    assert os.name == 'posix'

# Generated at 2022-06-14 06:17:00.681234
# Unit test for function make_lazy
def test_make_lazy():
    not_lazy_module = sys.modules['config.module_loading']
    assert not isinstance(not_lazy_module, _LazyModuleMarker)
    assert 'make_lazy' in not_lazy_module.__dict__

    lazy_module_path = 'config.module_loading.dummy'
    make_lazy(lazy_module_path)
    assert lazy_module_path not in sys.modules

    lazy_module = sys.modules['config.module_loading.dummy']
    assert isinstance(lazy_module, _LazyModuleMarker)
    assert not hasattr(lazy_module, '__dict__')
    assert not hasattr(lazy_module, '__file__')
    assert hasattr(lazy_module, 'is_lazy')


# Generated at 2022-06-14 06:17:13.320581
# Unit test for function make_lazy
def test_make_lazy():
    """
    Test that the make_lazy function works.
    """
    module_path = '__test_make_lazy__'

    if module_path in sys.modules:
        del sys.modules[module_path]

    class Module(object):
        a = 1

    def decorate(f):
        def function(*args, **kwargs):
            return f(*args, **kwargs)
        return function

    # Create the test module
    sys.modules[module_path] = Module()

    # Create a Function that depends on the test module.
    @decorate
    def f():
        return Module.a

    # Ensure that the Function can access the test module.
    assert f() == 1

    # Apply the make_lazy function.
    make_lazy(module_path)

    # Ensure that the Function

# Generated at 2022-06-14 06:17:24.187951
# Unit test for function make_lazy
def test_make_lazy():
    import inspect
    # unit test for function make_lazy
    import unittest
    import sys

    class TestMakeLazy(unittest.TestCase):
        def test__mro__(self):
            # check that module is instance of ModuleType.
            sys.modules[__name__] = None
            make_lazy(__name__)
            lazy_module = sys.modules[__name__]
            self.assertTrue(isinstance(lazy_module, ModuleType))

        def test_real_import(self):
            # check that lazy module imports appropriately
            sys.modules[__name__] = None
            make_lazy(__name__)
            lazy_module = sys.modules[__name__]
            self.assertEqual(lazy_module.__file__, inspect.getfile(inspect))

# Generated at 2022-06-14 06:17:30.108734
# Unit test for function make_lazy
def test_make_lazy():
    # Remove 'tests.lazy' from sys.modules
    if 'tests.lazy' in sys.modules:
        del sys.modules['tests.lazy']

    # Make tests.lazy a lazy module
    make_lazy('tests.lazy')

    # Assert that tests.lazy module is not in sys.modules dictionary
    assert 'tests.lazy' not in sys.modules

    # Assert that the module is a LazyModule
    assert isinstance(sys.modules['tests.lazy'], _LazyModuleMarker)

    # Get the attribute from the lazy module
    assert sys.modules['tests.lazy'].__name__ == 'tests.lazy'

    # Assert that tests.lazy module is in sys.modules dictionary
    assert 'tests.lazy' in sys.modules

# Generated at 2022-06-14 06:17:41.978563
# Unit test for function make_lazy
def test_make_lazy():
    # Test case where the module is not found
    module_name = 'non_existant_module'
    make_lazy(module_name)
    assert module_name not in sys.modules
    try:
        # We don't care whether this raises a KeyError or an ImportError, we
        # just care that it raises an error.
        sys.modules[module_name]
    except Exception:
        pass
    else:
        assert False, "Should have raised an exception"

    # Test case where the module is found.
    module_name = 'datetime'
    make_lazy(module_name)
    try:
        dt = sys.modules[module_name]
    except ImportError:
        assert False, "Should not have thrown an error."
    assert dt
    assert dt.date
    assert dt

# Generated at 2022-06-14 06:17:51.465088
# Unit test for function make_lazy
def test_make_lazy():
    """
    Test utility make_lazy.
    """
    import finch_test_package.module_a

    assert isinstance(finch_test_package.module_a, _LazyModuleMarker)
    assert hasattr(finch_test_package.module_a, 'something') == False

    finch_test_package.module_a.something
    assert isinstance(finch_test_package.module_a, ModuleType) == True


# Generated at 2022-06-14 06:17:57.168424
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    import test_lazy_module
    print(test_lazy_module.__file__)
    make_lazy('test_lazy_module')
    sys.modules['test_lazy_module'].__file__

if __name__ == '__main__':
    test_make_lazy()

# Generated at 2022-06-14 06:18:08.903107
# Unit test for function make_lazy
def test_make_lazy():
    """
    This test is done in the unit tests
    """
    class TestModule(object):
        """
        A test module
        """
        def test_attr(self):
            """
            A test attribute
            """
            return 1

    sys.modules['test_module'] = TestModule()
    test_module = sys.modules['test_module']
    assert isinstance(test_module, TestModule)
    assert test_module.test_attr() == 1

# Generated at 2022-06-14 06:18:21.522226
# Unit test for function make_lazy
def test_make_lazy():
    # Note: This test must be executed before unittest import
    # to guarantee that unittest was not imported yet
    make_lazy('unittest')
    import unittest

    assert isinstance(unittest, _LazyModuleMarker)
    assert not isinstance(unittest, unittest.TestCase)


test_make_lazy()


# The rest of this file is the actual lazy modules.
# Each of these modules has some imports that are only used within
# a function or class. Since these submodules are unlikely to be used,
# we don't want to import all of that code until we need it.

make_lazy('django.apps')
make_lazy('django.conf')
make_lazy('django.core.mail')

# Generated at 2022-06-14 06:18:29.312924
# Unit test for function make_lazy
def test_make_lazy():
    import sys

    sys.modules['lazy_test'] = None

    lazy_test = __import__('lazy_test')

    make_lazy('lazy_test')

    try:
        assert(isinstance(lazy_test, _LazyModuleMarker))
        assert(lazy_test.__name__ == 'lazy_test')
        assert(lazy_test.__doc__ is None)

        # The really cool part. The test file has a function called `doit`.
        # Calling it from the lazy module will actually have the side effect
        # of importing the module.
        assert(lazy_test.doit() == 'did it')
        assert(isinstance(lazy_test, ModuleType))

    finally:
        del sys.modules['lazy_test']

# Generated at 2022-06-14 06:18:33.380324
# Unit test for function make_lazy
def test_make_lazy():
    module_path = "make_lazy"
    make_lazy(module_path)

    assert not isinstance(sys.modules[module_path], ModuleType)
    assert make_lazy == _LazyModuleMarker

# Generated at 2022-06-14 06:18:45.480542
# Unit test for function make_lazy
def test_make_lazy():
    # first use a normal module
    test_module = dict((k, v) for k, v in globals().items()
                       if k.startswith('test_make_lazy_') and callable(v))

    # test with make_lazy
    test_module_lazy = dict((k, v) for k, v in globals().items()
                            if k.startswith('test_make_lazy_') and callable(v))

    test_module_lazy = dict((k, v) for k, v in globals().items()
                            if k.startswith('test_make_lazy_') and callable(v))

    # use 'test_module_lazy' as the module_path
    make_lazy(__name__)

# Generated at 2022-06-14 06:18:47.919356
# Unit test for function make_lazy
def test_make_lazy():
    assert make_lazy('fake_path')
    fake_module = sys.modules['fake_path']
    assert isinstance(fake_module, _LazyModuleMarker)



# Generated at 2022-06-14 06:18:59.698913
# Unit test for function make_lazy
def test_make_lazy():
    # Skip this test if we don't have the _testcapi extension
    try:
        from _testcapi import ute_get_startup_trace
    except ImportError:
        import unittest
        raise unittest.SkipTest("Needs _testcapi module")

    # Make sure that importing _testcapi added this to the startup_imports list
    startup_imports = ute_get_startup_trace()
    assert '_testcapi' in startup_imports

    # Now we mark the module as lazy, and then try to import it.
    make_lazy("_testcapi")
    assert '_testcapi' not in startup_imports

    # Importing _testcapi again should now import it, and add it to the
    # startup_imports list

# Generated at 2022-06-14 06:19:13.147313
# Unit test for function make_lazy
def test_make_lazy():
    """
    This test will fail if the function make_lazy(...) does not do the job.
    """
    # To make a module lazy, you can use the function make_lazy(...)
    # Here is an example:
    make_lazy("time")

    # Now the module time is not in sys.modules yet
    assert "time" not in sys.modules

    # However, you can still use it as if it has been imported
    from time import time

    # Now the module time has been loaded
    assert "time" in sys.modules

    # You can also use any other attributes of time module
    # for example:
    assert time() >= 1473143271

    # NOTE: if you still want to load the module, use:
    # from time import time
    # or
    # from time import time as time_var

   

# Generated at 2022-06-14 06:19:23.215487
# Unit test for function make_lazy
def test_make_lazy():
    import os, tempfile, sys

    try:
        make_lazy('sys')
        sys.lazy_module = True
        assert sys.platform == 'lazy_module'
    finally:
        del sys.lazy_module
        del sys.modules['sys']
        del sys.modules['sys.lazy_module']

# Generated at 2022-06-14 06:19:29.905231
# Unit test for function make_lazy
def test_make_lazy():
    make_lazy(module_path)
    from . import test_lazy
    from . import test_lazy as test_lazy_alias

    assert test_lazy is test_lazy_alias
    assert type(test_lazy) is type(test_lazy_alias)
    assert isinstance(test_lazy, _LazyModuleMarker)

# Generated at 2022-06-14 06:19:35.726580
# Unit test for function make_lazy
def test_make_lazy():
    import __pkginfo__
    make_lazy('__pkginfo__')
    assert isinstance(__pkginfo__, _LazyModuleMarker)
    assert __pkginfo__.__version__ == '0.4.1'
    import __pkginfo__
    assert isinstance(__pkginfo__, ModuleType)
    assert __pkginfo__.__version__ == '0.4.1'


# Generated at 2022-06-14 06:19:47.094064
# Unit test for function make_lazy
def test_make_lazy():
    module_name = 'lazy_module'

    # Setup a fake module that we can check gets imported
    class FakeModule(object):
        def __init__(self):
            self.attr = None
            self.attr_attr = None

        def set_attr(self, attr):
            self.attr = attr

        def set_attr_attr(self, attr, attr_attr):
            self.attr = attr
            self.attr_attr = attr_attr

    fake_module = FakeModule()
    sys.modules[module_name] = fake_module

    # A module should not be imported when we mark it lazy
    make_lazy(module_name)
    assert sys.modules[module_name] is not fake_module

    # It should be imported after an attribute is called on it
    sys.modules

# Generated at 2022-06-14 06:19:59.743136
# Unit test for function make_lazy
def test_make_lazy():
    class FakeModule(object):
        def __init__(self, module_name):
            self.__name__ = module_name

    make_lazy("fake_module")
    mod = sys.modules['fake_module']
    assert type(mod) == NonLocal
    assert mod.value == None

    mod.value = FakeModule("fake_module")
    assert sys.modules['fake_module'].__name__ == "fake_module"
    assert sys.modules['fake_module'].__mro__() == (LazyModule, ModuleType)
    assert sys.modules['fake_module'].__class__.__mro__[1] == ModuleType

if __name__ == '__main__':
    test_make_lazy()

# Generated at 2022-06-14 06:20:07.002276
# Unit test for function make_lazy
def test_make_lazy():
    """
    Test make_lazy by using make_lazy on an object and
    trying to import it.
    """
    import tests.unit.lib.haikunator.lazy_module

    assert tests.unit.lib.haikunator.lazy_module.__name__ == 'tests.unit.lib.haikunator.lazy_module'
    assert not isinstance(tests.unit.lib.haikunator.lazy_module, _LazyModuleMarker)

    make_lazy('tests.unit.lib.haikunator.lazy_module')

    assert isinstance(tests.unit.lib.haikunator.lazy_module, _LazyModuleMarker)

    from tests.unit.lib.haikunator.lazy_module import foo
    assert foo() == 'bar'

# Generated at 2022-06-14 06:20:20.084030
# Unit test for function make_lazy
def test_make_lazy():
    import os
    import sys
    from types import ModuleType
    from threading import Thread
    from time import sleep

    os.environ['MODULE_IMPORT_WATCHER_TEST'] = 'y'
    sys.modules.pop('module_import_watcher_tests', None)

    make_lazy('module_import_watcher_tests')
    assert not 'module_import_watcher_tests' in sys.modules

    # test lazy property
    assert isinstance(sys.modules['module_import_watcher_tests'], ModuleType)

    import module_import_watcher_tests
    assert module_import_watcher_tests.__name__ == "module_import_watcher_tests"
    assert os.environ.get('MODULE_IMPORT_WATCHER_TEST', None) is None

    # test

# Generated at 2022-06-14 06:20:25.935264
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    import os.path
    import tempfile

    # Create a temporary directory for the module
    lazy_mod_dir = tempfile.mkdtemp()
    lazy_mod_path = os.path.join(lazy_mod_dir, 'lazy.py')

    # Create a module in the temporary directory
    fh = open(lazy_mod_path, 'w')
    try:
        fh.write('x = 1')
    finally:
        fh.close()

    # Add the temporary directory to the path
    sys.path.append(lazy_mod_dir)

    # Lazy load the module
    make_lazy('lazy')

    # Get a reference to the module
    m = sys.modules['lazy']
    # Get a reference to the module path

# Generated at 2022-06-14 06:20:37.602510
# Unit test for function make_lazy
def test_make_lazy():
    """
    foobar.py looks like

    class Foo:
        pass

    class Bar:
        pass
    """
    import os
    import sys
    import tempfile

    # create a file
    with tempfile.NamedTemporaryFile('w', suffix='.py', delete=False) as f:
        f.write('''
        class Foo:
            pass

        class Bar:
            pass
        ''')

    # Path and file name
    module_path = os.path.splitext(f.name)[0]

    # Get module name, not the path
    module_name = os.path.basename(module_path)

    make_lazy(module_name)

    # Call __import__ to get the module, but this will not
    # import the module, and instead only return a LazyModule

# Generated at 2022-06-14 06:20:50.323898
# Unit test for function make_lazy
def test_make_lazy():
    """
    Python has a framework for unit testing where you can run the
    module itself to execute all the tests in the file.
    """
    module_name = "tests.lazy_test_module"

    module = __import__(module_name)
    assert module.loaded is True, "Module should have been imported"

    del sys.modules[module_name]

    make_lazy(module_name)
    assert module_name in sys.modules, ("Module should have been replaced"
                                        " with the lazy proxy")

    lazy_module = sys.modules[module_name]

    assert isinstance(lazy_module, _LazyModuleMarker), ("Make sure our"
                                                        " __mro__ works")


# Generated at 2022-06-14 06:21:04.208799
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    from types import ModuleType
    from functools import wraps

    lazy = 'tests.lazy'
    trigger = 'tests.lazy.trigger'

    def check_lazy():
        assert lazy not in sys.modules
        assert isinstance(sys.modules[trigger], ModuleType)

    def check_loaded():
        assert isinstance(sys.modules[lazy], ModuleType)
        assert not isinstance(sys.modules[trigger], ModuleType)

    try:
        import tests.lazy  # noqa
    except:
        pass

    old_lazy_modules = sys.modules.copy()

    make_lazy(lazy)
    check_lazy()
    import tests.lazy  # noqa

    check_loaded()

    def import_trigger():
        import tests.lazy.trigger 

# Generated at 2022-06-14 06:21:12.734201
# Unit test for function make_lazy
def test_make_lazy():
    import sys

    assert 'test_make_lazy' not in sys.modules
    make_lazy('test_make_lazy')
    assert 'test_make_lazy' in sys.modules

    test_mod = sys.modules['test_make_lazy']
    assert isinstance(test_mod, _LazyModuleMarker)
    assert not isinstance(test_mod, ModuleType)

    assert not hasattr(test_mod, '__implemented__')
    assert hasattr(test_mod, '__implemented__')
    assert test_mod.__implemented__ is True
    del sys.modules['test_make_lazy']



# Generated at 2022-06-14 06:21:26.210308
# Unit test for function make_lazy
def test_make_lazy():
    import os
    import tempfile
    import imp

    temp_dir = tempfile.mkdtemp()
    init_file = os.path.join(temp_dir, '__init__.py')
    f = open(init_file, 'w')
    f.write('test_str = "hello world"')
    f.close()
    module_name = os.path.join(temp_dir, 'test_mod')
    f = open(module_name + '.py', 'w')
    f.write('test_str = "hello world"')
    f.close()
    sys.path.append(temp_dir)
    tmp_mod = None

# Generated at 2022-06-14 06:21:36.851057
# Unit test for function make_lazy
def test_make_lazy():
    """
    Test the make_lazy function.
    """
    # Put a test module in sys.modules.
    # We assume it was not there before this test was run.
    module_path = 'test_module'
    sys.modules[module_path] = 'test'

    # Make sure that the test module has been set.
    assert sys.modules[module_path] == 'test'

    # Make sure that the test module is a LazyModule, not just a string.
    make_lazy(module_path)
    assert isinstance(sys.modules[module_path], _LazyModuleMarker)

    # Prove that our LazyModule fools the isinstance statement.
    assert isinstance(sys.modules[module_path], ModuleType)

    # Prove that our LazyModule doesn't fool the type statement.
   

# Generated at 2022-06-14 06:21:43.403518
# Unit test for function make_lazy
def test_make_lazy():
    import my_module
    assert not isinstance(my_module, _LazyModuleMarker)
    assert isinstance(my_module, ModuleType)
    assert my_module.__name__ == "my_module"
    assert my_module.a_value == "A VALUE"


# Generated at 2022-06-14 06:21:53.257287
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    sys.modules.pop('redis_cluster', None)
    assert 'redis_cluster' not in sys.modules
    make_lazy('redis_cluster')

    import redis_cluster
    assert isinstance(redis_cluster, _LazyModuleMarker)

    sys.modules.pop('redis_cluster', None)
    assert 'redis_cluster' not in sys.modules

    # Ensure that the module is cached after import
    make_lazy('redis_cluster')

    import redis_cluster
    assert isinstance(redis_cluster, _LazyModuleMarker)
    assert 'redis_cluster' in sys.modules
    assert 'redis_cluster' not in sys.modules['redis_cluster']

# Generated at 2022-06-14 06:22:06.796652
# Unit test for function make_lazy
def test_make_lazy():
    # Make sure the module can be imported without raising errors
    try:
        make_lazy("tests.unit.test_lazymodule")
    except:
        raise Exception("Error importing lazy module.")

    # Make sure the module appears not imported
    if "tests.unit.test_lazymodule" in sys.modules:
        raise Exception("Lazy module is already in sys.modules.")
    if "lazymodule" in sys.modules:
        raise Exception("Lazy module is already in sys.modules.")

    # Make sure the module's class is ModuleType
    if type(sys.modules["tests.unit.test_lazymodule"]) != ModuleType:
        raise Exception("Lazy module does not have class ModuleType.")

    # Make sure the module's class is not __builtin__.object

# Generated at 2022-06-14 06:22:17.858938
# Unit test for function make_lazy
def test_make_lazy():
    # it's a hard thing to test as we don't have a
    # handle to the actual LazyModule
    # let's just ensure we can import a module
    # without actually importing the module.
    make_lazy('make_lazy_test')

    # patch in the sys.modules to test this module.
    # this is really just
    # `from make_lazy_test import x`
    # but we are using the low level api to verify it's working.
    sys.modules['make_lazy_test'] = __import__('make_lazy_test')

    import make_lazy_test

    assert make_lazy_test.test_attribute == 'hello'


if __name__ == '__main__':
    test_make_lazy()

# Generated at 2022-06-14 06:22:22.646815
# Unit test for function make_lazy
def test_make_lazy():

    import ctypes

    ctypes.string_at.__module__ = 'ctypes'

    make_lazy('ctypes')

    assert 'ctypes' not in sys.modules
    assert ctypes.string_at is not None

    assert sys.modules['ctypes'] is ctypes



# Generated at 2022-06-14 06:22:32.471536
# Unit test for function make_lazy
def test_make_lazy():
    import types
    import sys
    # make sure not in sys.modules because we are a lazy import
    assert 'test_module' not in sys.modules
    assert isinstance(test_module, types.ModuleType)
    # reassign the module so the parent module doesn't hold a reference
    # to the old value
    test_module = sys.modules['test_module']
    assert test_module.test_value == 'test'
    # make sure we re-imported it and that the module is the same
    assert id(test_module) == id(sys.modules['test_module'])

# Generated at 2022-06-14 06:22:40.122898
# Unit test for function make_lazy
def test_make_lazy():
    make_lazy('inspect')
    assert isinstance(sys.modules['inspect'], _LazyModuleMarker)
    import inspect
    assert inspect.getsourcefile(make_lazy)
    assert inspect.getsourcefile(test_make_lazy)



# Generated at 2022-06-14 06:22:53.637716
# Unit test for function make_lazy
def test_make_lazy():
    """
    Tests for the make_lazy function.
    """
    make_lazy('test_me')
    import test_me
    assert isinstance(test_me, _LazyModuleMarker)

    # Make sure the import works
    assert test_me.__name__ == 'test_me'
  
# This is called from the import hook to make the modules lazy.

# Generated at 2022-06-14 06:23:04.703081
# Unit test for function make_lazy
def test_make_lazy():
    """
    Make sure the module returns the correct type.
    """
    # Create a temp file for testing
    fd, temp = tempfile.mkstemp()

    # Write standard header
    header = """
    import sys
    import os

    class LazyClass(object):
        def __init__(self):
            self.loaded = True

    sys.modules["__main__"] = LazyClass()"""
    os.write(fd, header)
    os.close(fd)

    # Make the module lazy
    make_lazy(temp)

    # Make sure the module returns a LazyModule
    assert isinstance(sys.modules[temp], _LazyModuleMarker)

    # Remove file when we're done
    os.remove(temp)

# Generated at 2022-06-14 06:23:15.375436
# Unit test for function make_lazy
def test_make_lazy():
    """
    Tests the make_lazy function.
    """
    module_path = 'test_module'

    def test_func():
        """
        Tests that an imported module is imported lazily.
        """
        make_lazy(module_path)
        from test_module import TEST_CONST
        assert TEST_CONST == 'Lazy module'

    # Mock a test module.
    testmod = types.ModuleType(module_path)
    testmod.TEST_CONST = 'Normal module'

    # Insert the test module into sys.modules
    try:
        sys.modules[module_path] = testmod

        test_func()
    finally:
        # Cleanup the test module.
        del sys.modules[module_path]
        del testmod

# Generated at 2022-06-14 06:23:26.990462
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    sys.modules['test:test_make_lazy'] = None
    make_lazy('test:test_make_lazy')
    module = sys.modules['test:test_make_lazy']
    assert module is not None
    assert isinstance(module, _LazyModuleMarker)
    assert hasattr(module, '__mro__')
    assert isinstance(module, ModuleType)
    module.__mro__  # Used to raise an exception
    module.__getattribute__  # Used to raise an exception

import django.core.exceptions

# Add the signature of each exception class to it.
# This is specially useful for DRF's api_view functions
for name in dir(django.core.exceptions):
    obj = getattr(django.core.exceptions, name)


# Generated at 2022-06-14 06:23:35.528309
# Unit test for function make_lazy
def test_make_lazy():
    """
    Test that make_lazy is behaving as intended
    """
    mod = 'test_make_lazy_mod'
    try:
        import test_make_lazy_mod
    except ImportError:
        pass
    else:
        del sys.modules['test_make_lazy_mod']

    make_lazy('test_make_lazy_mod')
    found_lazy = False
    for key, val in sys.modules.items():
        if key == 'test_make_lazy_mod':
            if isinstance(val, _LazyModuleMarker):
                found_lazy = True

    assert found_lazy

    import test_make_lazy_mod

    assert sys.modules[mod].foo == 'foo'

# Generated at 2022-06-14 06:23:49.163883
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    import types
    import sys_module
    # Create a dummy module.
    sys.modules.pop('sys_module')
    sys_module.__name__ = 'sys_module'
    sys_module.__file__ = __file__
    sys_module.__loader__ = None
    sys_module.__package__ = None
    sys_module.__spec__ = None
    # Mark it lazy.
    make_lazy('sys_module')
    # Make sure our standin module is in sys.modules.
    assert 'sys_module' in sys.modules
    # Make sure our standin module is lazy.
    assert isinstance(sys.modules['sys_module'], _LazyModuleMarker)
    # Make sure our standin module was deleted.

# Generated at 2022-06-14 06:24:00.262550
# Unit test for function make_lazy
def test_make_lazy():
    from importlib import import_module
    from sonosco.common import lazy
    import os
    import sys

    test_path = os.path.abspath(os.path.dirname(__file__))
    test_file = os.path.join(test_path, 'test_module.py')
    test_module_path = os.path.splitext(test_file)[0].replace(os.sep, '.')

    # Test if it is not loaded
    module = None
    try:
        module = import_module(test_module_path)
    except ImportError:
        pass

    assert module is None
    # Test the case of nonlocal keyword
    module_path = test_module_path
    module = NonLocal(None)
    test_module = __import__(module_path)
   

# Generated at 2022-06-14 06:24:08.942029
# Unit test for function make_lazy
def test_make_lazy():
    make_lazy('email.message')

    # Check that it works for pylint.  The following line should not throw an
    # import error.
    import email.message
    # Check that it works for pyflakes
    email.message.Message()
    # Check that it works for class instances
    assert isinstance(email.message, _LazyModuleMarker)
    # Check that it works for class types
    assert issubclass(email.message.Message, email.message.Message)

# Generated at 2022-06-14 06:24:19.722357
# Unit test for function make_lazy
def test_make_lazy():
    class ModuleUnderTest(ModuleType):
        __file__ = 'foo'

    sys.modules['test.lazy'] = ModuleUnderTest('test.lazy')

    testlazy = sys.modules['test.lazy']
    assert testlazy.__file__ == 'foo'

    # now lazy it.
    make_lazy('test.lazy')
    assert isinstance(sys.modules['test.lazy'], _LazyModuleMarker)

    # access the module
    testlazy = sys.modules['test.lazy']

    # assert we get our module back
    assert testlazy == ModuleUnderTest('test.lazy')
    assert isinstance(testlazy, ModuleType)

# Generated at 2022-06-14 06:24:27.558411
# Unit test for function make_lazy
def test_make_lazy():
    make_lazy("os")   # A normal module
    make_lazy("sys")  # A module with a __mro__
    make_lazy("distutils.tests.support")  # A module with a __mro__
    # A module to be imported that does not exist
    lazy_module = make_lazy("does.not.exist")

# Generated at 2022-06-14 06:24:32.437832
# Unit test for function make_lazy
def test_make_lazy():
    """
    Test function make_lazy.

    The function is tested by creating a module marked as lazy,
    and then importing it.
    """
    # The module to be marked as lazy.
    # It has a function that returns a string

# Generated at 2022-06-14 06:24:43.436285
# Unit test for function make_lazy