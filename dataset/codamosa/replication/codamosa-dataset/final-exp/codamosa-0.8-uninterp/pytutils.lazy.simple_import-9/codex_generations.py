

# Generated at 2022-06-14 06:14:42.189259
# Unit test for function make_lazy
def test_make_lazy():
    import file_io

    assert file_io.__file__.endswith('file_io.py')
    make_lazy('file_io')
    assert isinstance(file_io, _LazyModuleMarker)
    file_io.find_file()
    assert file_io.__file__.endswith('file_io.pyc')

# Generated at 2022-06-14 06:14:54.101469
# Unit test for function make_lazy
def test_make_lazy():
    module_path = '__lazy_marker_test'
    make_lazy(module_path)

    lazy_module = sys.modules[module_path]

    try:
        from . import __lazy_marker_test
    except ImportError:
        assert False, '__lazy_marker_test module has not been created.'

    assert isinstance(lazy_module, _LazyModuleMarker), \
        'module has been marked as LazyModule'

    # Test that the module hasn't been lazy loaded
    assert sys.modules['__lazy_marker_test'] is lazy_module

    import __lazy_marker_test
    # Test that the module has been loaded
    assert sys.modules['__lazy_marker_test'] is not lazy_module

    del sys.modules[module_path]

# Generated at 2022-06-14 06:15:02.556156
# Unit test for function make_lazy
def test_make_lazy():
    """
    Lazy import for unit test.
    """
    make_lazy("sqlalchemy.sql.type_api")
    assert isinstance(sqlalchemy.sql.type_api, _LazyModuleMarker)
    assert sqlalchemy.sql.type_api.__name__ == "sqlalchemy.sql.type_api"
    assert sqlalchemy.sql.type_api.__class__.__name__ == "LazyModule"



# Generated at 2022-06-14 06:15:11.386581
# Unit test for function make_lazy
def test_make_lazy():
    sys.modules = {}
    module_path = 'test.test_module_imports_a'
    make_lazy(module_path)
    module = sys.modules[module_path]
    assert isinstance(module, _LazyModuleMarker)
    assert not hasattr(module, 'a')
    assert module.a == 'a'
    assert hasattr(module, 'a')


# Mark what packages should be lazy.

# Mark the packages that should be lazy.
make_lazy('test.test_module_imports_a')
make_lazy('test.test_module_imports_b')
make_lazy('test.test_module_imports_c')
make_lazy('test.test_module_imports_d')

# Generated at 2022-06-14 06:15:20.676474
# Unit test for function make_lazy
def test_make_lazy():
    """
    Makes sure the module doesn't get imported until we access it.
    The 'test_module_path' module is in this file.
    """
    def import_test_module():
        import test_module_path

    # This should raise an exception
    assert_raises(ImportError, import_test_module)

    # Mark the `test_module_path` as a lazy module
    make_lazy('test_module_path')

    # This should not raise an exception
    import_test_module()

# Generated at 2022-06-14 06:15:33.537276
# Unit test for function make_lazy
def test_make_lazy():
    test_path = 'test_make_lazy'
    # create a test module
    class TestModule(object):
        var = 0
        def func(self, x):
            return x + 1

    sys_modules = sys.modules # cache in the locals
    sys_modules[test_path] = TestModule()

    make_lazy(test_path)

    # check that the module has been replaced by the lazy version
    import_module(test_path)
    assert isinstance(sys_modules[test_path], _LazyModuleMarker)

    import_module(test_path)
    # check that the module was lazily loaded
    assert sys.modules[test_path].var == 0
    assert sys.modules[test_path].func == TestModule.func

# Generated at 2022-06-14 06:15:44.061662
# Unit test for function make_lazy
def test_make_lazy():
    import datetime
    import threading
    assert datetime.datetime.now() is not None
    make_lazy('datetime')
    assert datetime.datetime.now() is not None  # force lazy load
    assert datetime.datetime.now() is not None  # assert that it doesn't reload
    assert datetime.datetime.now() is not None  # assert that it doesn't reload

    import sys
    assert sys.modules['datetime'] is not None

    # Make sure it doesn't duplicate in sys.modules
    make_lazy('datetime')
    assert sys.modules['datetime'] is not None


# Mark some libraries to be lazy loaded
make_lazy('gevent.select')
make_lazy('gevent.socket')
make_lazy('gevent.core')

# Generated at 2022-06-14 06:15:52.371554
# Unit test for function make_lazy
def test_make_lazy():
    """
    Tests that make_lazy is working as expected.
    """
    # Test before mark.
    assert __import__('imp').find_module('os')[3] is True

    # Test mark.
    try:
        make_lazy('os')
        assert __import__('imp').find_module('os')[3] is False
    finally:
        del sys.modules['os']

    # Test after mark.
    assert __import__('imp').find_module('os')[3] is True

# Generated at 2022-06-14 06:16:02.040383
# Unit test for function make_lazy
def test_make_lazy():
    sys.modules[__name__ + '.test_module'] = None
    make_lazy(__name__ + '.test_module')

    assert __name__ + '.test_module' in sys.modules
    import test_module
    assert isinstance(test_module, _LazyModuleMarker)

    # This should load the module, and replace the lazy with a real module
    assert sys.modules[__name__ + '.test_module'] is not None
    assert isinstance(sys.modules[__name__ + '.test_module'], ModuleType)

# Generated at 2022-06-14 06:16:11.059443
# Unit test for function make_lazy
def test_make_lazy():
    """
    Test make_lazy functionality
    """
    class C(object):
        def __init__(self, message):
            self.message = message

        def __str__(self):
            return self.message

    class D(object):
        def __init__(self, message):
            self.message = message

        def __str__(self):
            return self.message

    file_name = 'a/b/c'
    try:
        os.makedirs(os.path.dirname(file_name))
    except OSError:
        pass

    with open(file_name + '.py', 'w') as f:
        f.write('c = C("this is c")\n')

    with open(file_name + '_d.py', 'w') as f:
        f

# Generated at 2022-06-14 06:16:23.949847
# Unit test for function make_lazy
def test_make_lazy():
    """
    Tests that the function 'make_lazy' works as expected.
    """
    import sys
    # Stores the initial state of sys.modules
    sys_modules = sys.modules.copy()

    # Create a test module
    class TestModule(object):
        """
        A test module to test with
        """
        TEST_ATTRIBUTE = "Test attribute"

    # Store a reference to this module for the sake of later unloading the module
    sys_modules["_test_make_lazy"] = TestModule

    # Make the test module lazy
    make_lazy("_test_make_lazy")

    # Check that the module was made lazy
    assert isinstance(sys.modules["_test_make_lazy"], _LazyModuleMarker)

    # Check that we can get the attribute off of the module
   

# Generated at 2022-06-14 06:16:26.390623
# Unit test for function make_lazy
def test_make_lazy():
    """
    Test that calling `make_lazy` causes no errors.
    """
    make_lazy('_non_existant_module_')

# Generated at 2022-06-14 06:16:35.503044
# Unit test for function make_lazy
def test_make_lazy():
    import imp_unittest.mock_module
    try:
        assert(isinstance(imp_unittest.mock_module, _LazyModuleMarker))
        assert(not hasattr(imp_unittest, 'mock_module'))
        assert(type(imp_unittest.mock_module) == ModuleType)
        assert(imp_unittest.mock_module != imp_unittest)
    finally:
        del sys.modules['imp_unittest.mock_module']

# Generated at 2022-06-14 06:16:43.441494
# Unit test for function make_lazy
def test_make_lazy():
    from unittest import TestCase
    import sys

    class LazyModuleTest(TestCase):
        def _assertIsLazy(self, module):
            self.assertTrue(isinstance(module, _LazyModuleMarker))

            # We want to make sure our module will not
            # be imported when we check for the module's __mro__
            with self.assertRaises(KeyError):
                sys.modules.pop(module.__name__)

            # Make sure isinstance will return True
            # but not import a module because of __mro__
            self.assertTrue(isinstance(module, _LazyModuleMarker))

        def _assertIsNotLazy(self, module):
            self.assertFalse(isinstance(module, _LazyModuleMarker))


# Generated at 2022-06-14 06:16:57.002123
# Unit test for function make_lazy
def test_make_lazy():
    import sys, os

    mod_path = 'lazy_import.tests.fixtures.lazy_module'

    # Make sure original module is not loaded
    try:
        import fixtures.lazy_module
    except ImportError:
        pass
    else:
        assert False, "Fixtures lazy_module should not be loaded"

    # Make sure module is originally not in sys.modules
    assert not mod_path in sys.modules, "Module should not be in sys.modules"

    # Add fake module to sys.modules
    fake_module = ModuleType(mod_path)
    sys.modules[mod_path] = fake_module

    # Make lazy
    make_lazy(mod_path)
    reload(sys)

    # Make sure original module is not loaded

# Generated at 2022-06-14 06:17:04.087002
# Unit test for function make_lazy
def test_make_lazy():
    import os
    import tempfile
    import shutil
    import time
    import sys

    def test(target_file, module_path, expected_time):
        path = tempfile.mkdtemp()
        sys.path.insert(0, path)
        with open(os.path.join(path, target_file), 'w') as fd:
            fd.write('import time\ntime.sleep(2)')
        time_before = time.time()
        make_lazy(module_path)
        __import__(module_path)
        sys.path.remove(path)
        shutil.rmtree(path)
        time_after = time.time()
        assert (time_after - time_before) < expected_time

    test('test.py', 'test', 0)

# vim:

# Generated at 2022-06-14 06:17:12.350686
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    make_lazy('test_make_lazy')

    # If this module is NOT lazy, then the following line will fail.
    assert sys.modules['test_make_lazy'].__mro__() == (
        sys.modules['test_make_lazy'], ModuleType)

    # If this module is NOT lazy, then the following line will fail.
    assert isinstance(sys.modules['test_make_lazy'], _LazyModuleMarker)

# Generated at 2022-06-14 06:17:22.382291
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    import os
    import tempfile
    import shutil
    import ipdb

    tmpdir = tempfile.mkdtemp()
    modulename = 'temp'
    modulefile = os.path.join(tmpdir, modulename + '.py')
    code = 'A = 1'
    with open(modulefile, 'w') as f:
        f.write(code)

    # ipdb.set_trace()
    make_lazy(modulename)
    assert not isinstance(sys.modules[modulename], ModuleType)
    assert sys.modules[modulename].A == 1
    shutil.rmtree(tmpdir)

# Generated at 2022-06-14 06:17:33.449449
# Unit test for function make_lazy
def test_make_lazy():
    mod = 'lazy_load.make_lazy'

    # remove if we've already imported it,
    # and make sure it doesn't exist in sys.modules
    if mod in sys.modules:
        del sys.modules[mod]

    assert mod not in sys.modules

    make_lazy(mod)

    # make sure it's not loaded yet
    assert mod in sys.modules
    assert isinstance(sys.modules[mod], _LazyModuleMarker)

    # make sure it's accessible
    assert sys.modules[mod].__file__.endswith('make_lazy.pyc')
    assert sys.modules[mod] is not None

    # make sure we can access it via import
    __import__(mod)
    assert mod in sys.modules
    assert sys.modules[mod].__file__.endsw

# Generated at 2022-06-14 06:17:41.475499
# Unit test for function make_lazy
def test_make_lazy():
    try:
        import make_lazy
    except ImportError:
        import make_lazy as module

    assert make_lazy.module is None
    # The module is still lazy so make_lazy.module is still None
    assert make_lazy.module is None
    # The module has loaded because we accessed it so the module is not None
    assert make_lazy.module is not None
    # The module is not lazy anymore
    import make_lazy
    # The module is not lazy anymore
    assert make_lazy is not None

test_make_lazy()

# Generated at 2022-06-14 06:17:44.523723
# Unit test for function make_lazy
def test_make_lazy():
    make_lazy("lazy_test")
    from lazy_test import HELLO

# Generated at 2022-06-14 06:17:51.990003
# Unit test for function make_lazy
def test_make_lazy():
    mod = 'tests.unit.test_lazy'
    class FakeSys(object):
        modules = dict()
    sys = FakeSys()
    make_lazy(mod)
    assert sys.modules[mod].__class__.__name__ == 'LazyModule'
    # Access the module to see if it's lazy
    assert sys.modules[mod].test_attribute == 'foo'
    # Access a module that doesn't exist
    with pytest.raises(KeyError):
        sys.modules['foo']


# Generated at 2022-06-14 06:18:01.298757
# Unit test for function make_lazy
def test_make_lazy():
    """
    Test that make_lazy works as intended.
    """
    # Set up mocks
    class MockModule(object):
        """
        A mock module
        """

    class MockSys(object):
        """
        A mock sys module
        """
        modules = {}

    orig_sys = sys
    modules = MockSys.modules
    orig_modules = sys.modules

    sys = MockSys()

    # Test that the Lazy module is returned
    make_lazy('my_module')
    module = sys.modules['my_module']

    assert isinstance(module, _LazyModuleMarker)
    assert module._lazy_path == 'my_module'
    assert module._lazy_module is None

    # Test that a real module is returned after calling on module
    module.some_attribute = 'value'

# Generated at 2022-06-14 06:18:08.775369
# Unit test for function make_lazy
def test_make_lazy():
    try:
        made_lazy = make_lazy('pkg.test_lazy_module')
        print(made_lazy)
    except ImportError:
        # Make sure no actual module is created during the test
        assertTrue(sys.modules.get('pkg.test_lazy_module') is None)

if __name__ == '__main__':
    test_make_lazy()

# Generated at 2022-06-14 06:18:16.812913
# Unit test for function make_lazy
def test_make_lazy():
    import os
    module_path_name = 'test.test_lazy_module.test_module'
    module_path = module_path_name.replace('.', os.sep) + '.py'
    make_lazy(module_path_name)
    assert sys.modules[module_path_name] is not None
    from test.test_lazy_module import test_module
    assert sys.modules[module_path_name] is test_module

# Generated at 2022-06-14 06:18:27.523722
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    import tempfile
    import os

    try:
        sys.modules['rotate_image']
    except KeyError:
        sys.modules['rotate_image'] = None

    assert 'rotate_image' not in sys.modules, \
        """
        Ensure that the module rotate_image is not present in sys.modules
        """

    mod_path = os.path.join(tempfile.gettempdir(), 'rotate_image.py')

# Generated at 2022-06-14 06:18:40.935510
# Unit test for function make_lazy
def test_make_lazy():
    import unit_testing.lazy_loading.test_lazy

    from unit_testing.lazy_loading import test_lazy

    make_lazy('unit_testing.lazy_loading.test_lazy')

    assert(isinstance(unit_testing.lazy_loading.test_lazy, _LazyModuleMarker))
    assert(isinstance(test_lazy, _LazyModuleMarker))

    assert(unit_testing.lazy_loading.test_lazy.DATA == [1, 2])
    assert(test_lazy.DATA == [1, 2])

    assert(not isinstance(unit_testing.lazy_loading.test_lazy, _LazyModuleMarker))
    assert(not isinstance(test_lazy, _LazyModuleMarker))

    import unit_testing.lazy_

# Generated at 2022-06-14 06:18:54.125344
# Unit test for function make_lazy
def test_make_lazy():
    class FooException(Exception):
        pass

    def test_module():
        from . import lazy_module
        return lazy_module

    def test_module_2():
        from . import lazy_module_2
        return lazy_module_2

    make_lazy('.lazy_module')


# Generated at 2022-06-14 06:19:05.896702
# Unit test for function make_lazy
def test_make_lazy():
    # Create a fake module and put it in sys.modules.
    sys.modules['fake_module'] = ModuleType('fake_module')
    fake = sys.modules['fake_module']
    fake.__file__ = __file__
    fake.HELLO = 'hello'

    # Test set up is OK
    assert isinstance(fake, ModuleType)
    assert hasattr(fake, 'HELLO')
    assert fake.HELLO == 'hello'
    assert fake.__file__ == __file__

    # Test that make_lazy is lazy and that it marks the module as lazy.
    make_lazy('fake_module')
    assert isinstance(fake, _LazyModuleMarker)  # Lazy
    assert not hasattr(fake, 'HELLO')  # Lazy

# Generated at 2022-06-14 06:19:14.921853
# Unit test for function make_lazy
def test_make_lazy():
    assert 'test_lazy_module' not in sys.modules

    class Foo(object):
        def __init__(self):
            self.foo = False

        def set_foo(self, val):
            self.foo = val

    # Make sure the module is not already loaded into sys.modules
    assert 'test_lazy_module' not in sys.modules

    # Lazy load a module
    make_lazy('test_lazy_module')

    # Imports should not actually run yet...
    assert not sys.modules['test_lazy_module'].foo

    # Importing should mark the module as loaded
    from test_lazy_module import Foo
    assert isinstance(Foo(), Foo)

    # The module is now loaded, so this should run the import script
    from test_lazy_module import foo
   

# Generated at 2022-06-14 06:19:22.764631
# Unit test for function make_lazy
def test_make_lazy():
    import django.conf.global_settings as settings

    # This should be the settings module
    assert isinstance(settings, ModuleType)
    assert hasattr(settings, 'DEBUG')

    # This is a lazy module
    assert isinstance(sys.modules['django.conf.global_settings'], _LazyModuleMarker)

# Generated at 2022-06-14 06:19:34.913019
# Unit test for function make_lazy
def test_make_lazy():
    test_module = 'hyperkitty.tests.importer.TestLazyImport'
    def has_imported_module(module_name):
        # A function to test whether the module has been imported
        return importlib.import_module(module_name) is not None

    # test_module is not imported yet
    assert not has_imported_module(test_module)
    # Mark test_module as lazy
    make_lazy(test_module)
    # Make sure the module import has not been triggered yet
    assert not has_imported_module(test_module)
    # Access a variable in the module, to trigger the import
    importlib.import_module(test_module).value
    # Make sure the module import has been triggered now
    assert has_imported_module(test_module)
    # Make sure that the module

# Generated at 2022-06-14 06:19:43.904986
# Unit test for function make_lazy
def test_make_lazy():
    """
    Unit test for function make_lazy
    """
    def test_module():
        """
        Mock module for testing
        """
        print("Hello World!")

    # Import test_module
    print("Import test_module")
    import test_module

    # Make test_module lazy
    print("Make test_module lazy")
    make_lazy("test_module")
    assert isinstance(test_module, _LazyModuleMarker)

    # Test lazy load test_module
    print("Test lazy load test_module")
    test_module.test_module()

test_make_lazy()

# Generated at 2022-06-14 06:19:51.638861
# Unit test for function make_lazy
def test_make_lazy():
    module_path = 'lazy_import.test_lazy_module'

    try:
        del sys.modules[module_path]
    except KeyError:
        pass

    assert module_path not in sys.modules

    make_lazy(module_path)
    assert module_path in sys.modules
    assert sys.modules[module_path].__name__ == module_path
    assert not isinstance(sys.modules[module_path], ModuleType)

    assert module_path in dir(sys.modules[module_path])
    assert sys.modules[module_path].lazy_module_func() == 1

    try:
        del sys.modules[module_path]
    except KeyError:
        pass



# Generated at 2022-06-14 06:20:02.878739
# Unit test for function make_lazy
def test_make_lazy():
    '''
    The decorator wraps the returned function and module in callable
    objects that raise RuntimeError if called.
    '''
    import sys

    def get_module(module_name):
        '''
        Return the module object with the specified name.
        '''
        return sys.modules[module_name]

    # Remove any old version of the module
    try:
        del sys.modules['test_lazy_module']
    except KeyError:
        pass

    import test_lazy_module
    module = test_lazy_module.module

    # Check that the module not loaded at all yet
    assert get_module('test_lazy_module').__name__ == 'test_lazy_module'
    assert isinstance(module, _LazyModuleMarker)

    # Check __mro__ results in correct behavior

# Generated at 2022-06-14 06:20:08.568679
# Unit test for function make_lazy
def test_make_lazy():
    sys.modules['mod.a'] = None

    # The module should not have been imported
    make_lazy('mod.a')
    assert 'mod.a' in sys.modules
    assert not hasattr(sys.modules['mod.a'], 'mod')
    assert 'mod.a' not in sys.modules['mod.a'].__dict__

    # The module should now be loaded
    mod = sys.modules['mod.a']
    assert hasattr(mod, 'mod')

# Generated at 2022-06-14 06:20:16.204505
# Unit test for function make_lazy
def test_make_lazy():
    import os
    assert os is sys.modules['os']
    make_lazy('os')
    assert 'os' not in sys.modules
    try:
        assert 'os' not in sys.modules
        assert simplejson is not sys.modules['simplejson']
        assert os is sys.modules['os']
    finally:
        del sys.modules['simplejson']
        del sys.modules['os']
    sys.modules['os'] = os

# Generated at 2022-06-14 06:20:24.824842
# Unit test for function make_lazy
def test_make_lazy():
    sys.modules.pop('lazy_module', None)
    make_lazy('lazy_module')
    assert not hasattr(sys.modules['lazy_module'], 'attr'), ("Module should not be loaded yet")
    sys.modules['lazy_module'].attr = 'value'
    assert hasattr(sys.modules['lazy_module'], 'attr'), ("Module should now be loaded")
    assert sys.modules['lazy_module'].attr == 'value', ("Value is wrong")

# Generated at 2022-06-14 06:20:34.941774
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    import os

    # Clean up sys.modules for our test module
    try:
        del sys.modules['test_lazy']
    except KeyError:
        pass

    # Make our module lazy
    make_lazy('test_lazy')
    module = sys.modules['test_lazy']

    # Make sure module wasn't imported
    assert not hasattr(module, '__file__')

    # Reading an attribute forces import
    assert module.__file__ == __file__
    assert hasattr(module, '__file__')
    assert module.__file__ == __file__

# Generated at 2022-06-14 06:20:47.223469
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    import test_mod1
    import test_mod2
    import test_mod3

    # Note that we import these modules before make_lazy
    assert(sys.modules.has_key('test_mod1'))
    assert(sys.modules.has_key('test_mod2'))
    assert(sys.modules.has_key('test_mod3'))

    import test_mod3.mod3_1

    make_lazy('test_mod1')
    make_lazy('test_mod2')
    make_lazy('test_mod3')

    # Make sure that we have a lazy module here
    assert(isinstance(sys.modules['test_mod1'], _LazyModuleMarker))

# Generated at 2022-06-14 06:21:02.037211
# Unit test for function make_lazy
def test_make_lazy():
    import os
    import sys
    import test_make_lazy as test_make_lazy_mod
    module_path = os.path.dirname(test_make_lazy_mod.__file__) + '/test_make_lazy_data.py'
    sys.modules['test_make_lazy_data'] = test_make_lazy_mod

    make_lazy('test_make_lazy_data')
    import test_make_lazy_data
    assert isinstance(test_make_lazy_data, _LazyModuleMarker)
    assert test_make_lazy_data.val == 2



# Generated at 2022-06-14 06:21:06.845419
# Unit test for function make_lazy
def test_make_lazy():
    import platform

    make_lazy('os')
    assert isinstance(sys.modules['os'], _LazyModuleMarker)
    assert 'os' not in sys.modules

    assert sys.modules['os'].path == platform.path
    assert sys.modules['os'].path.abspath('foo') == platform.path.abspath('foo')
    assert sys.modules['os'].path.abspath('foo') == '/foo'
    assert not isinstance(sys.modules['os'], _LazyModuleMarker)



# Generated at 2022-06-14 06:21:19.187562
# Unit test for function make_lazy
def test_make_lazy():
    """
    Test make_lazy function.
    """
    module_path = 'a.b.c'
    sys.modules[module_path] = import_module(module_path)
    module = import_module(module_path)
    assert module is sys.modules[module_path]
    assert not isinstance(module, _LazyModuleMarker)

    make_lazy(module_path)
    module = import_module(module_path)
    assert isinstance(module, _LazyModuleMarker)
    assert module is sys.modules[module_path]

    # Trigger lazy import
    getattr(module, '__name__')
    module = import_module(module_path)
    assert not isinstance(module, _LazyModuleMarker)

# Generated at 2022-06-14 06:21:30.851413
# Unit test for function make_lazy
def test_make_lazy():
    """Test make_lazy"""
    import doctest
    m = doctest.register_optionflag('LazyModuleMarker')
    d = doctest.DocTestParser().get_doctest(make_lazy,
                                            mflags=doctest.NORMALIZE_WHITESPACE | m,
                                            name='make_lazy',
                                            globs={},
                                            filename=None,
                                            docstring=make_lazy.__doc__)
    runner = doctest.DebugRunner(verbose=False, optionflags=doctest.NORMALIZE_WHITESPACE | m)
    f, t = runner.rundoc(d)


# Generated at 2022-06-14 06:21:43.665703
# Unit test for function make_lazy
def test_make_lazy():
    # set up the environmenmt
    import sys
    import os
    import shutil
    import glob

    tempdir = os.path.realpath('.test_make_lazy_temp')
    mod_dir = os.path.join(tempdir, 'a')
    sys.path.insert(0, tempdir)
    os.makedirs(mod_dir)

    # make a test module
    with open(os.path.join(mod_dir, 'a.py'), 'w') as f:
        f.write("""
b = 'test123'
c = 'test456'
print('Imported a')
""")

    # 'emulate' a certain environment

# Generated at 2022-06-14 06:21:49.385944
# Unit test for function make_lazy
def test_make_lazy():
    """
    Test that a lazy module is actually, you know, lazy.
    """
    sys.modules['test_lazy'] = None
    make_lazy('test_lazy')
    sys_modules = sys.modules
    assert 'test_lazy' in sys_modules
    sys_modules['test_lazy'].foo
    assert sys_modules['test_lazy'] is not None
    assert isinstance(sys_modules['test_lazy'], _LazyModuleMarker)
    del sys.modules['test_lazy']
    del sys_modules['test_lazy']

# Generated at 2022-06-14 06:21:56.377053
# Unit test for function make_lazy
def test_make_lazy():
    """
    Test make_lazy()
    """
    import sys
    test_path = 'foo.bar.baz'
    make_lazy(test_path)

    # We should not have a module in sys.modules
    assert test_path not in sys.modules

    # Upon using the object, we should have
    # a module in sys.modules
    assert test_path in sys.modules



# Generated at 2022-06-14 06:22:08.445264
# Unit test for function make_lazy
def test_make_lazy():
    # Define a module
    import os
    module_path = os.path.join(os.path.dirname(__file__), 'lazy_module.py')
    sys.path = [os.path.dirname(os.path.dirname(__file__))]
    mod = __import__('lazy_module')

    # Attribute of the module
    attr = mod.VALUE

    # If we mark the module as lazy, then it is not imported
    # until we get an attribute from the module (like mod.VALUE).
    make_lazy('lazy_module')
    mod = __import__('lazy_module')
    attr = mod.VALUE


if __name__ == '__main__':
    from z3 import *
    from z3util_base import *

    test_make_lazy

# Generated at 2022-06-14 06:22:19.372037
# Unit test for function make_lazy
def test_make_lazy():
    key = 'lazymodule'
    make_lazy(key)
    # Lazy module
    assert key in sys.modules
    assert sys.modules[key]

    lazy_mod = sys.modules[key]
    assert lazy_mod is sys.modules[key]

    assert isinstance(lazy_mod, _LazyModuleMarker)
    assert isinstance(lazy_mod, ModuleType)
    assert not isinstance(lazy_mod, object)

    # Check for existence of attribute
    assert hasattr(lazy_mod, '__mro__')

    # Check if value will only be initialized once
    lazy_mod.x = 1
    assert hasattr(lazy_mod, 'x')
    assert lazy_mod.x == 1

    make_lazy(key)
    # This time value will not be in

# Generated at 2022-06-14 06:22:24.153706
# Unit test for function make_lazy
def test_make_lazy():
    class FakeModule(object):
        pass

    mod = FakeModule()
    mod.a = 1

    make_lazy('mod')

    m = sys.modules['mod']

    assert(not isinstance(m, FakeModule))
    assert(isinstance(m, _LazyModuleMarker))
    assert(m.a == 1)

# Generated at 2022-06-14 06:22:37.452381
# Unit test for function make_lazy
def test_make_lazy():
    """
    Tests that the module is not imported when just marked as lazy.
    """
    a_module_path = 'a_module'
    sys.modules.pop(a_module_path, None)

    make_lazy(a_module_path)
    assert isinstance(sys.modules[a_module_path], _LazyModuleMarker)

    # A module is marked to be lazy, but it is not imported yet
    assert sys.modules[a_module_path] not in sys.modules.values()



# Generated at 2022-06-14 06:22:41.045416
# Unit test for function make_lazy
def test_make_lazy():
    import django
    make_lazy('django')
    assert sys.modules['django'] != django
    assert isinstance(sys.modules['django'], _LazyModuleMarker)
    import django
    assert sys.modules['django'] == django

# Generated at 2022-06-14 06:22:52.753877
# Unit test for function make_lazy
def test_make_lazy():
    """
    Test for make_lazy
    """
    import django

    assert not isinstance(django, _LazyModuleMarker)
    make_lazy('django')
    assert isinstance(django, _LazyModuleMarker)

    # Now that we've accessed the module, it should import
    assert django.VERSION

    # This should be imported already
    assert not isinstance(django.conf, _LazyModuleMarker)

    make_lazy('django.conf')
    assert isinstance(django.conf, _LazyModuleMarker)

    # Now that we've accessed the module, it should import
    assert django.conf.settings



# Generated at 2022-06-14 06:23:01.124161
# Unit test for function make_lazy
def test_make_lazy():
    # A module that has a dependency on 'os'.
    module_path = 'test_module'
    with mock.patch('test_module.os', autospec=True) as mock_os:
        # Make sure module is not imported on creation (mocked out above)
        make_lazy(module_path)
        assert mock_os.system.call_count == 0

        # Ensure that the module gets imported on first access.
        sys.modules[module_path].foo()
        assert mock_os.system.call_count == 1

# Generated at 2022-06-14 06:23:11.924536
# Unit test for function make_lazy
def test_make_lazy():
    """
    Tests that make_lazy actually makes the module lazy
    """
    import time
    import time_lazy

    before = time.time()

    # Check to make sure that time is actually imported
    getattr(time_lazy, 'time')

    after = time.time()

    assert(before < after)

    # Check that the module is actually lazy
    before = time.time()

    # Check to make sure that time is not imported
    getattr(time_lazy, 'sleep')

    after = time.time()

    assert(before == after)

# Generated at 2022-06-14 06:23:20.027892
# Unit test for function make_lazy
def test_make_lazy():
    """
    Test that the module is not fetched until the first import.
    """
    assert not hasattr(sys.modules, '_lazy_module')
    make_lazy('_lazy_module')
    assert isinstance(sys.modules['_lazy_module'], _LazyModuleMarker)
    assert not hasattr(sys.modules, '_lazy_module')
    import _lazy_module
    assert hasattr(sys.modules, '_lazy_module')

# Generated at 2022-06-14 06:23:23.041207
# Unit test for function make_lazy
def test_make_lazy():
    module_path = 'time'

    make_lazy(module_path)

    assert module_path not in sys.modules
    assert module_path in sys.modules
    assert isinstance(sys.modules[module_path], _LazyModuleMarker)

# Generated at 2022-06-14 06:23:30.514865
# Unit test for function make_lazy
def test_make_lazy():
    """
    Test make_lazy function.
    """
    import testmodule
    assert not isinstance(testmodule, _LazyModuleMarker)

    make_lazy("testmodule")
    assert isinstance(testmodule, _LazyModuleMarker)

    # Make sure we lazy-import the module.
    assert testmodule.test_attribute == "a test attribute"
    assert not isinstance(testmodule, _LazyModuleMarker)

if __name__ == "__main__":
    test_make_lazy()

# Generated at 2022-06-14 06:23:33.560930
# Unit test for function make_lazy
def test_make_lazy():
    import os as _os  # Importing inside the function so no pep8 error
    make_lazy('os')
    assert isinstance(_os, _LazyModuleMarker)

# Generated at 2022-06-14 06:23:39.434662
# Unit test for function make_lazy
def test_make_lazy():
    make_lazy('lazy_test')
    module = sys.modules['lazy_test']

    assert isinstance(module, _LazyModuleMarker)
    assert str(module.__class__).endswith('LazyModule')
    assert module.__getattribute__.__self__ is module

    assert 'lazy_test' in sys.modules
    assert sys.modules['lazy_test'] is module

# Generated at 2022-06-14 06:23:57.288424
# Unit test for function make_lazy
def test_make_lazy():
    def foo():
        import inspect

    import inspect
    inspect.stack()
    make_lazy('inspect')

    assert 'inspect' in sys.modules
    assert sys.modules['inspect']

    assert not isinstance(sys.modules['inspect'], ModuleType)

    foo()

    assert isinstance(sys.modules['inspect'], ModuleType)



# Generated at 2022-06-14 06:24:06.300819
# Unit test for function make_lazy
def test_make_lazy():
    import import_from_dotted_path.test_lazy_modules
    import_from_dotted_path.test_lazy_modules.foo
    assert import_from_dotted_path.test_lazy_modules.foo == 'bar'

    make_lazy('import_from_dotted_path.test_lazy_modules')
    import_from_dotted_path.test_lazy_modules.foo
    assert import_from_dotted_path.test_lazy_modules.foo == 'bar'



# Generated at 2022-06-14 06:24:19.506420
# Unit test for function make_lazy
def test_make_lazy():
    """
    Tests the make_lazy import deferral
    NOTE: if this test fails, it's going to blow up hard

    Usage:
        python -m edx_django_utils.test_make_lazy
    """

    # Avoid recursion
    try:
        from .test_make_lazy import foo
    except ImportError:
        pass
    else:
        raise Exception("Test case failed to prevent recursion")

    import os
    import glob
    import shutil
    import tempfile
    from uuid import uuid4

    # Create a temporary directory
    TEST_DIR = tempfile.mkdtemp()
    __builtins__["TEST_DIR"] = TEST_DIR
    TEMP_DIR = os.path.join(TEST_DIR, "tmp")
    __builtins__["TEMP_DIR"]

# Generated at 2022-06-14 06:24:30.861589
# Unit test for function make_lazy
def test_make_lazy():
    """
    Make sure we can properly delay a module's import.
    """
    module_path = 'import_module_tests.module_with_expensive_import'
    assert module_path in sys.modules, 'could not find module in sys.modules prior to patching'

    make_lazy(module_path)

    assert module_path in sys.modules, 'failed to find the module instance in sys.modules after patching'
    assert isinstance(sys.modules[module_path], _LazyModuleMarker), 'fail to delay module loading'

    with patch(module_path + '.expensive_import') as expensive_import:
        # check that the function is not called until needed.
        assert expensive_import.call_count == 0

  

# Generated at 2022-06-14 06:24:42.725009
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    import random
    import test_module

    try:
        # delete our module from sys.modules to have a clean start
        del sys.modules['test_module']
    except KeyError:
        pass
    assert 'test_module' not in sys.modules
    assert 'test_module_attr' not in sys.modules['test_module']

    # Call make_lazy
    make_lazy('test_module')

    # Confirm the module is not yet loaded
    assert 'test_module' in sys.modules
    assert 'test_module_attr' not in sys.modules['test_module']

    # Confirm a call to the attr in the module will import the module
    assert not test_module.test_module_attr

    # Confirm the module is now loaded