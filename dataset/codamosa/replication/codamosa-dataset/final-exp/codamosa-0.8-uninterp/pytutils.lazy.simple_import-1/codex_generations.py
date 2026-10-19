

# Generated at 2022-06-14 06:14:48.368558
# Unit test for function make_lazy
def test_make_lazy():
    sys.modules.clear()
    module_path = 'test_lazy_module'
    make_lazy(module_path)
    assert module_path in sys.modules
    assert isinstance(sys.modules[module_path], ModuleType)
    assert isinstance(sys.modules[module_path], _LazyModuleMarker)
    assert module_path not in sys.modules
    assert sys.modules[module_path].a == 1
    assert module_path in sys.modules
    assert isinstance(sys.modules[module_path], ModuleType)
    assert sys.modules[module_path].b == 2
    assert sys.modules[module_path].c == 3


# Reference test module
#
# The following is the module that we are loading lazily.
# The import of this module is delayed until the first
# attribute access is

# Generated at 2022-06-14 06:14:54.102705
# Unit test for function make_lazy
def test_make_lazy():
    from test.pkg.import_test import test_module


# Mark the test package as lazy
make_lazy('test.pkg.import_test')


if __name__ == "__main__":
    test_make_lazy()

# Generated at 2022-06-14 06:15:03.518460
# Unit test for function make_lazy
def test_make_lazy():
    """
    This is a unit test for function make_lazy.
    """
    sys_modules = sys.modules
    assert "my_mod" not in sys_modules

    make_lazy("my_mod")
    assert isinstance(sys_modules["my_mod"], _LazyModuleMarker)
    assert "my_mod" not in sys.modules

    sys_modules["my_mod"].foo = "foo"
    assert sys_modules["my_mod"].foo == "foo"
    assert "my_mod" in sys.modules

# Generated at 2022-06-14 06:15:11.687916
# Unit test for function make_lazy
def test_make_lazy():
    """
    Test that the `make_lazy` function works correctly.
    """

    # Remove the module from sys.modules if it's already there.
    if 'test_make_lazy_module' in sys.modules:
        del sys.modules['test_make_lazy_module']

    import test_make_lazy_module
    assert not isinstance(
        test_make_lazy_module,
        _LazyModuleMarker
    )

    # Ensure that the module has been imported and is
    # available in sys.modules
    assert 'test_make_lazy_module' in sys.modules
    assert test_make_lazy_module.__name__ == 'test_make_lazy_module'

    sys.modules['test_make_lazy_module'] = None


# Generated at 2022-06-14 06:15:24.987714
# Unit test for function make_lazy
def test_make_lazy():
    """
    Test make_lazy works, without the module being imported by mistake.
    """
    old_module = sys.modules.copy()
    make_lazy('totally_lazy_module')

    assert sys.modules['totally_lazy_module'].__class__.__name__ == 'LazyModule'
    # Make sure isinstance works
    assert isinstance(sys.modules['totally_lazy_module'], ModuleType)

    # Make sure the module still hasn't been imported
    assert 'totally_lazy_module' not in old_module
    # And the module's been removed
    assert 'totally_lazy_module' not in sys.modules

    # Now try to access an attribute (which will import it)
    sys.modules['totally_lazy_module'].__mro__
   

# Generated at 2022-06-14 06:15:33.174882
# Unit test for function make_lazy
def test_make_lazy():
    """
    Test that make_lazy works
    """
    import random

    module_path = random.randint(0, 999999)  # generate random module name
    module_path = '%s.%s' % (__name__, module_path)
    make_lazy(module_path)

    import_module(module_path)  # import the lazy module
    assert isinstance(sys.modules[module_path], _LazyModuleMarker)

    # test that the module is actually lazily loaded.
    sys.modules[module_path] = None
    assert not hasattr(sys.modules[module_path], '__mro__')

    # try to import the module again
    import_module(module_path)

    # make sure the module is lazy, and that
    # the module was imported successfully.
   

# Generated at 2022-06-14 06:15:43.889188
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    import threading
    import time
    sys.modules.pop('django.utils.encoding.nonlocal', None)
    make_lazy('django.utils.encoding.nonlocal')

# Generated at 2022-06-14 06:15:56.409048
# Unit test for function make_lazy
def test_make_lazy():
    """Test make_lazy and the lazy module implementation"""
    import sys
    import threading

    module_path = '__test_lazy__'
    del sys.modules[module_path]


# Generated at 2022-06-14 06:16:03.440184
# Unit test for function make_lazy
def test_make_lazy():
    sys.modules['parent'] = parent = types.ModuleType('parent')
    sys.modules['parent.child'] = child = types.ModuleType('parent.child')
    parent.init = True
    parent.child.val = 'yo'

    make_lazy('parent.child')
    assert isinstance(parent.child, _LazyModuleMarker)
    assert not hasattr(parent.child, 'init')
    assert hasattr(parent.child, 'val')
    assert parent.child.val == 'yo'

# Generated at 2022-06-14 06:16:11.031799
# Unit test for function make_lazy
def test_make_lazy():
    import shutil
    module_path = 'shutil'

    # Make a module lazy, then delete it from sys.modules.
    make_lazy(module_path)
    assert isinstance(shutil, _LazyModuleMarker)
    assert 'shutil' not in sys.modules

    # Access an attribute on the lazy module.
    assert shutil.which('python') is not None
    assert isinstance(shutil, ModuleType)
    assert 'shutil' in sys.modules

# Generated at 2022-06-14 06:16:23.805057
# Unit test for function make_lazy
def test_make_lazy():

    def testcase(to_import):
        """
        Execute the given statements and check for a RuntimeError
        """
        try:
            exec(to_import)
        except RuntimeError as e:
            assert 'Attempt to load a lazy module without access' in str(e), 'Got unexpcted exception: {}'.format(e)
        else:
            assert False, 'Should have seen RuntimeError'

    def testcase2(to_import, value):
        assert value == eval(to_import)

    make_lazy('os.path')

    testcase('os.path==None')
    testcase('isinstance(os.path, _LazyModuleMarker)')

    # Test accessing a value.
    #
    # Note that it is not required that the lazy module be removed from
    # sys.modules before importing. 

# Generated at 2022-06-14 06:16:32.478453
# Unit test for function make_lazy
def test_make_lazy():
    import test_lazy_module
    make_lazy('test_lazy_module')
    reload(test_lazy_module)


if __name__ == '__main__':
    import unittest
    import test_lazy_module
    make_lazy('test_lazy_module')

    class LazyModuleTests(unittest.TestCase):
        def test_module_is_lazy(self):
            """
            The module should be lazy
            """
            import test_lazy_module
            self.assert_(isinstance(test_lazy_module, _LazyModuleMarker))

        def test_module_attrs_are_available(self):
            """
            The module's attributes should be available
            """
            import test_lazy_module

# Generated at 2022-06-14 06:16:42.479317
# Unit test for function make_lazy
def test_make_lazy():
    import foo

    # Ensure we have not imported foo
    assert 'foo' not in sys.modules

    # Get a module lazy version of the foo module
    make_lazy('foo')

    # Ensure we still have not imported foo
    assert 'foo' not in sys.modules

    # Get an object from foo
    thing = foo.thing()

    # Ensure we have imported foo now
    assert 'foo' in sys.modules

    # Ensure we now have access to the thing object
    assert isinstance(thing, foo.Thing)

    # Ensure we can get other attributes off of the module
    assert foo.__package__ is not None


# Ensure we were not imported by a LazyModule standin.
assert not isinstance(sys.modules[__name__], _LazyModuleMarker)

# Indicate that this module should be lazy-loaded

# Generated at 2022-06-14 06:16:56.007940
# Unit test for function make_lazy
def test_make_lazy():
    # Create a test module to import
    import tempfile
    import os

    MOD_NAME = 'test_make_lazy'
    FILE_NAME = 'test_make_lazy.py'

    test_file = tempfile.mkstemp(suffix=FILE_NAME)[1]
    test_mod = 'import sys\n' \
               'FOO = sys.platform\n'

    with open(test_file, 'w') as f:
        f.write(test_mod)

    sys.path.append(os.path.dirname(test_file))
    make_lazy(MOD_NAME)

    import test_make_lazy

    # Lazy loaded modules are are instances of
    # _LazyModuleMarker
    assert isinstance(test_make_lazy, _LazyModuleMarker)


# Generated at 2022-06-14 06:17:03.467492
# Unit test for function make_lazy
def test_make_lazy():
    import tempfile
    from sys import modules

    import os
    import time
    import shutil

    def sub_test(module_name, attr):
        """
        Ensure that the module is not imported until we ask for some attribute
        """
        mtime = time.time()
        # Python 3.2 has this as os.path.mtime
        if hasattr(os.path, 'getmtime'):
            getmtime = os.path.getmtime
        else:
            getmtime = lambda path: os.stat(path)[8]

        # Create a temporary directory
        dir_name = tempfile.mkdtemp()

        # Create a dummy module in that directory
        pkg_name = 'mymod'

# Generated at 2022-06-14 06:17:15.004128
# Unit test for function make_lazy
def test_make_lazy():
    import test.test_math
    try:
        from math import fabs
    except ImportError:
        if sys.platform.startswith("java"):
            raise unittest.SkipTest("The math module is missing")
        else:
            raise
    make_lazy("math")

    # Clean up any existing references to math before we start.
    import gc
    gc.collect()

    # Check that the math module is still not loaded.
    self.assertTrue("math" not in sys.modules)

    # Check that we can get something off of math.
    self.assertEqual(fabs(-1), 1)

    # Check that the math module is now loaded.
    self.assertTrue("math" in sys.modules)

    # Check that math is actually the math module, not LazyModule.

# Generated at 2022-06-14 06:17:23.310258
# Unit test for function make_lazy
def test_make_lazy():
    import __main__
    import imp
    ll_assert_equal(type(__main__.Lazy).__name__, 'LazyModule')
    make_lazy('Lazy')
    assert isinstance(__main__.Lazy, ModuleType)
    ll_assert_equal(type(__main__.Lazy).__name__, 'module')
    ll_assert_equal(__main__.Lazy.__name__, 'Lazy')

# Generated at 2022-06-14 06:17:28.423235
# Unit test for function make_lazy
def test_make_lazy():
    import test_make_lazy as mod

    make_lazy('test_make_lazy')

    # Test that we can call functions on this module
    assert mod.__name__ == 'test_make_lazy'

    # Test that we can instantiate an object in this module
    instance = mod.TestMakeLazyInstance()
    assert isinstance(instance, mod.TestMakeLazyInstance)

    # Test that we can subclass an object in this module
    class NewInstance(mod.TestMakeLazyInstance):
        pass

    instance = NewInstance()
    assert isinstance(instance, NewInstance)

# Generated at 2022-06-14 06:17:34.491416
# Unit test for function make_lazy
def test_make_lazy():
    import test_make_lazy_module
    assert not isinstance(test_make_lazy_module, _LazyModuleMarker)
    make_lazy('test_make_lazy_module')
    assert isinstance(test_make_lazy_module, _LazyModuleMarker)



# Generated at 2022-06-14 06:17:41.920428
# Unit test for function make_lazy
def test_make_lazy():
    """
    Test if make_lazy imports the module correctly
    """
    try:
        import tests.test_make_lazy
    except ImportError:
        pass

    make_lazy('tests.test_make_lazy')

    # Make sure that the module attribute was imported correctly
    assert sys.modules['tests.test_make_lazy'].test_attribute == 'success'



# Generated at 2022-06-14 06:17:51.545173
# Unit test for function make_lazy
def test_make_lazy():
    # return a fresh module path
    from importlib import import_module
    from random import randint
    from sys import modules, executable
    from tempfile import mkdtemp
    from uuid import uuid1
    from shutil import rmtree

    # make a temp dir
    temp_dir = mkdtemp()

    def make_path():
        # make a random path to use as a test
        return '%s.%s' % (str(randint(1, 100000)), str(uuid1()))

    # make a path that's not really in sys.modules
    module_path = make_path()
    while module_path in modules:
        module_path = make_path()

    # make a path that's not really in our temp dir

# Generated at 2022-06-14 06:18:00.090594
# Unit test for function make_lazy
def test_make_lazy():
    assert 'make_lazy' in sys.modules
    assert 'make_lazy' not in vars()
    assert make_lazy.__file__.endswith('/make_lazy.py')

    # should also work with dotted modules
    make_lazy('make_lazy.make_lazy')
    assert 'make_lazy.make_lazy' in sys.modules
    assert 'make_lazy.make_lazy' not in vars()
    assert not isinstance(make_lazy.make_lazy, _LazyModuleMarker)
    assert make_lazy.make_lazy.__file__.endswith('/make_lazy.py')

# Generated at 2022-06-14 06:18:08.820622
# Unit test for function make_lazy
def test_make_lazy():
    """
    We need to make sure that calling make_lazy works as expected (sys.modules
    points to a lazy module and then can be imported later by a consumer).
    """
    module_name = 'django.utils.lazy_tests'
    sys.modules[module_name] = None
    make_lazy(module_name)

    assert isinstance(sys.modules[module_name], _LazyModuleMarker)
    import django.utils.lazy_tests
    assert isinstance(sys.modules[module_name], ModuleType)
    assert isinstance(django.utils.lazy_tests, ModuleType)



# Generated at 2022-06-14 06:18:21.395807
# Unit test for function make_lazy
def test_make_lazy():
    """
    Unit test for function make_lazy
    """
    import sys
    import os

    import site

    import brew
    import pytest

    from .environment import Environment
    from .util import get_executable_path
    from .file import File

    test_dir = os.path.dirname(brew.__file__)
    executable_dir = os.path.dirname(get_executable_path())
    this_brew_file = File(__file__).to_node()
    test_brew_file = File(test_dir).to_node()
    executable_brew_file = File(executable_dir).to_node()
    tool_brew_file = File(os.path.join(executable_dir, 'tools')).to_node()

    # Make sure brew.py is not already imported
   

# Generated at 2022-06-14 06:18:26.510070
# Unit test for function make_lazy
def test_make_lazy():
    # Mock the sys.modules
    sys.modules = {}
    make_lazy('mod')
    from mod import x
    assert x == True
    assert 'mod' in sys.modules
    assert isinstance(sys.modules['mod'], _LazyModuleMarker)
    # Tear down the mocked sys.modules
    del sys.modules['mod']
    del sys.modules

# Generated at 2022-06-14 06:18:40.012011
# Unit test for function make_lazy
def test_make_lazy():
    """
    A unit test for the make_lazy function.

    If this test fails, please check the following:
        * The directory structure is correct.
        * The test_module module exists in `dulwich/tests/`
    """
    module_name = 'dulwich.tests.test_module'
    import dulwich
    import dulwich.tests

    # module shouldn't be loaded yet
    assert not hasattr(dulwich, 'tests')
    assert not hasattr(dulwich, 'tests')

    # lazy module shouldn't be loaded yet
    assert not hasattr(dulwich.tests, 'test_module')
    assert not hasattr(dulwich.tests, 'test_module')

    make_lazy(module_name)

    # lazy module shouldn't be loaded yet

# Generated at 2022-06-14 06:18:53.064990
# Unit test for function make_lazy
def test_make_lazy():
    # Test simple case
    make_lazy('my_package.my_module')
    # check that the module has been created
    assert 'my_package.my_module' in sys.modules
    # Check that the module is a LazyModule
    assert isinstance(sys.modules['my_package.my_module'], _LazyModuleMarker)
    # The system should not contain this module
    assert 'my_package.my_module.my_child' not in sys.modules

    # Make sure the system can still handle this module normally.

# Generated at 2022-06-14 06:19:02.239219
# Unit test for function make_lazy
def test_make_lazy():
    try:
        from StringIO import StringIO
    except ImportError:
        from io import StringIO

    output = StringIO()

    def is_lazy(module_path):
        """
        Returns True if the module is lazy
        """
        return isinstance(sys.modules[module_path], _LazyModuleMarker)

    def del_module(module_path):
        """
        Delete the module
        """
        del sys.modules[module_path]

    def dummy_print(s):
        """
        Prints a string with a newline
        """
        output.write('%s\n' % s)

    lazy_module_path = 'test_make_lazy_module'
    make_lazy(lazy_module_path)

    assert is_lazy(lazy_module_path)


# Generated at 2022-06-14 06:19:12.808490
# Unit test for function make_lazy
def test_make_lazy():
    make_lazy('generic.Lazy')
    from generic.Lazy import deep
    from generic.Lazy.deep import nested
    from generic.Lazy.deep import nested as n
    assert deep.nested is nested
    assert deep.nested is n

    # After usage, we are no longer lazy
    import generic.Lazy
    assert not isinstance(generic.Lazy, _LazyModuleMarker)
    # but our sub module should still be lazy
    assert isinstance(generic.Lazy.deep, _LazyModuleMarker)


# We should import this module right away
import generic.Immediate

make_lazy('generic.Lazy')
make_lazy('generic.Lazy.deep')
make_lazy('generic.Lazy.deep.nested')

# Generated at 2022-06-14 06:19:23.760798
# Unit test for function make_lazy
def test_make_lazy():
    """
    Unit test function for make_lazy function
    """
    module_name = 'lazy_module'

    print('\nRunning test')
    print('----------------')

    print('\nTesting module is not loaded when created')
    make_lazy(module_name)
    assert lazy_module.lazy_loaded == False
    print('SUCCESS: lazy_module not loaded when created')

    print('\nTesting module is loaded when an attribute is accessed')
    print(lazy_module.__dict__)
    assert lazy_module.lazy_loaded == True
    print('SUCCESS: lazy_module loaded when attribute is accessed')

# Generated at 2022-06-14 06:19:42.633694
# Unit test for function make_lazy
def test_make_lazy():
    # Make sure that module doesn't exist in sys.modules
    assert 'make_lazy_test' not in sys.modules
    # Make sure that we can import the module normally
    import make_lazy_test
    assert make_lazy_test.a == 1
    assert make_lazy_test.b == 2

    # make the module lazy
    make_lazy('make_lazy_test')

    # Make sure that the module is now in sys.modules, but is a LazyModule
    assert 'make_lazy_test' in sys.modules
    assert isinstance(sys.modules['make_lazy_test'], _LazyModuleMarker)

    # This won't be imported until we do a sys.modules.pop
    from make_lazy_test import a
    assert a == 1

# Generated at 2022-06-14 06:19:51.679977
# Unit test for function make_lazy
def test_make_lazy():
    # This is just an example, cannot run test on the module itself.

    import inspect
    import sys
    from types import ModuleType

    # this test is a bit tricky since we can't do anything without
    # importing the module. So we 'load' our module definition
    # using `import` and then 'register' the definition using
    # `sys.modules`.

    definition = inspect.getsource(make_lazy)
    definition = 'def test_make_lazy():\n' + definition

# Generated at 2022-06-14 06:20:02.926064
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    m = sys.modules
    module_path = 'a_fake_module_for_testing'

    make_lazy(module_path)

    assert module_path in m
    fake_mod = m[module_path]

    # check that the module is not imported
    assert fake_mod.__class__.__name__ == 'LazyModule'
    assert fake_mod.__name__ == module_path

    # check that isinstance works
    assert not isinstance(fake_mod, object)
    assert isinstance(fake_mod, ModuleType)

    # check that the module is imported on first request
    assert fake_mod.__name__ == module_path
    assert fake_mod.__class__.__name__ == 'module'
    assert m[module_path] is not fake_mod



# Generated at 2022-06-14 06:20:11.192284
# Unit test for function make_lazy
def test_make_lazy():
    pytest.importorskip("django")
    import django
    old_value = django.__version__
    try:
        # make sure `django` module exists in sys.modules
        assert "django" in sys.modules
        # make sure django.__version__ is accessible
        assert old_value
        # make it lazy
        make_lazy("django")
        assert "django" in sys.modules
        # assert that django.__version__ is None, since it wasn't loaded
        with pytest.raises(AttributeError):
            assert django.__version__
        # assert that django.VERSION is now accessible
        assert django.VERSION
    finally:
        del sys.modules["django"]
        # make sure sys.modules was restored to its original state
        assert "django"

# Generated at 2022-06-14 06:20:17.737502
# Unit test for function make_lazy
def test_make_lazy():
    try:
        make_lazy('zope.interface')
        from zope import interface
        assert isinstance(interface, _LazyModuleMarker)
        from zope.interface import Interface
        assert Interface.__module__ == 'zope.interface'
        assert Interface.__name__ == 'Interface'
    except Exception:
        import traceback
        traceback.print_exc()

# Generated at 2022-06-14 06:20:30.735656
# Unit test for function make_lazy
def test_make_lazy():
    """
    Tests the functionality of the make_lazy function.
    """
    import sys

    def _test_lazy_loads_module():
        """
        Tests that the module doesn't load till it has to.
        """
        assert sys.modules['test_helper_lazy_module'] is not None

        try:
            sys.modules['test_helper_lazy_module'] = None
            __import__('test_helper_lazy_module')
        except KeyError:
            pass
        else:
            assert False, 'Module should not be loaded yet.'

    def _test_lazy_loads_module_on_use():
        """
        Tests that the module loads when an attribute is used.
        """
        import test_helper_lazy_module


# Generated at 2022-06-14 06:20:39.896855
# Unit test for function make_lazy
def test_make_lazy():
    import imp
    import os.path
    import sys

    test_module_name = 'test'
    test_module_full_path = os.path.join(os.path.dirname(__file__), 'test_module.py')

    if test_module_name in sys.modules:
        del sys.modules[test_module_name]

    assert test_module_name not in sys.modules
    mod = imp.load_source(test_module_name, test_module_full_path)
    assert test_module_name in sys.modules

    del sys.modules[test_module_name]
    assert test_module_name not in sys.modules

    make_lazy(test_module_name)
    assert test_module_name in sys.modules
    mod = sys.modules[test_module_name]


# Generated at 2022-06-14 06:20:53.461560
# Unit test for function make_lazy
def test_make_lazy():
    from django.utils.module_loading import import_string
    import sys
    import unittest

    try:
        del sys.modules['tests.lazy_module']
    except KeyError:
        pass
    sys.modules['tests.lazy_module'] = None

    lazy_module = import_string('tests.lazy_module')
    if hasattr(lazy_module, 'LazyTestModel'):
        raise ValueError('Lazy module was imported immediately!')

    lazy_module_impl = import_string('tests.lazy_module.impl')
    if not hasattr(lazy_module_impl, 'LazyTestModel'):
        raise ValueError('Lazy module implememtation was not imported!')


# Generated at 2022-06-14 06:20:59.771379
# Unit test for function make_lazy
def test_make_lazy():
    module_path = 'six.moves'

    # Test that the module is not already loaded
    assert module_path not in sys.modules
    make_lazy(module_path)
    assert isinstance(sys.modules[module_path], _LazyModuleMarker)

    # Test that the module is loaded after the first access
    assert module_path in sys.modules
    assert isinstance(sys.modules[module_path], ModuleType)



# Generated at 2022-06-14 06:21:05.223871
# Unit test for function make_lazy
def test_make_lazy():
    import datetime
    global datetime # pylint: disable=global-statement

    assert type(datetime) is ModuleType

    make_lazy('datetime')
    assert not isinstance(datetime, ModuleType)

    assert datetime.date
    assert isinstance(datetime, ModuleType)

# Generated at 2022-06-14 06:21:25.983890
# Unit test for function make_lazy
def test_make_lazy():
    from default_settings.default_settings import settings

    make_lazy('default_settings.default_settings')
    settings.add_config_location('default_settings/test.settings')

    class MyClass(object):
        settings = settings

    my_obj = MyClass()
    with pytest.raises(AttributeError):
        my_obj.settings.set_default('test_lazy_module', 'test')

    my_obj.settings.test_lazy_module
    assert my_obj.settings.test_lazy_module == 'test'

# Generated at 2022-06-14 06:21:35.235120
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    import os

    module_name = 'foo'
    module_path = module_name + '.py'
    module_content = "test = 1\n"

    f = open(module_path, 'w')
    f.write(module_content)
    f.close()

    assert not module_name in sys.modules
    make_lazy(module_name)
    assert isinstance(sys.modules[module_name], _LazyModuleMarker)
    assert sys.modules[module_name].test == 1

    os.remove(module_path)
    del sys.modules[module_name]

test_make_lazy()

# Generated at 2022-06-14 06:21:40.825058
# Unit test for function make_lazy
def test_make_lazy():
    """
    Tests function make_lazy
    """
    import this

    make_lazy('this')
    if not isinstance(this, _LazyModuleMarker):
        raise AssertionError("make_lazy did not make module lazy")

    if not this.c == 'confidence':
        raise AssertionError("module attributes could not be accessed")

# Generated at 2022-06-14 06:21:48.947111
# Unit test for function make_lazy
def test_make_lazy():
    """
    Check to see if the function make_lazy creates a lazy module.
    """
    # Setup
    module_path = 'make_lazy_test'
    sys_modules = sys.modules

    if module_path in sys_modules:
        del sys_modules[module_path]

    # Test
    make_lazy(module_path)
    lazy_module = sys_modules[module_path]
    # Just verify that the module is in the sys path and it's a subclass of ModuleType
    assert isinstance(lazy_module, ModuleType), 'lazy_module is not a subclass of ModuleType'

    # Teardown
    del sys_modules[module_path]

# Generated at 2022-06-14 06:21:57.420424
# Unit test for function make_lazy
def test_make_lazy():
    make_lazy("my_module")
    import my_module as m
    import my_module
    assert isinstance(m, _LazyModuleMarker)
    m.x = 0
    assert isinstance(m, _LazyModuleMarker)
    assert isinstance(m, ModuleType)
    assert m.x == my_module.x
    import my_module
    assert m == my_module


if __name__ == '__main__':
    test_make_lazy()

# Generated at 2022-06-14 06:22:00.461575
# Unit test for function make_lazy
def test_make_lazy():
    sys.modules["lazydummy"] = None
    make_lazy("lazydummy")

    assert isinstance(sys.modules["lazydummy"], _LazyModuleMarker)

# Generated at 2022-06-14 06:22:10.808854
# Unit test for function make_lazy
def test_make_lazy():
    """
    Make sure make_lazy doesn't import anything until it's needed.
    """
    # Create a mock package and a dummy module
    module_path = 'test_package.dummy_module'
    module_name = 'dummy_module'

    # Create the dummy module with a dummy variable
    dummy_val = 'dummy variable'
    with open(os.path.join(module_path.split('.')[0], module_name + '.py'), 'w') as f:
        f.write("{} = '{}'".format(module_name, dummy_val))

    assert module_path not in sys.modules
    make_lazy(module_path)

    # Test that the module exists, but wasn't imported
    assert module_path in sys.modules

# Generated at 2022-06-14 06:22:21.736582
# Unit test for function make_lazy
def test_make_lazy():
    # Import modules
    import os
    import errno
    import sys
    import django
    import django.utils.unittest.suite

    # Make sure the modules are not lazy
    assert not isinstance(os, _LazyModuleMarker)
    assert not isinstance(errno, _LazyModuleMarker)
    assert not isinstance(sys, _LazyModuleMarker)
    assert not isinstance(django, _LazyModuleMarker)
    assert not isinstance(django.utils.unittest.suite, _LazyModuleMarker)

    # Make the modules lazy
    make_lazy('os')
    make_lazy('errno')
    make_lazy('sys')
    make_lazy('django')

# Generated at 2022-06-14 06:22:26.911666
# Unit test for function make_lazy
def test_make_lazy():
    module_path = 'test.test_lazy_module'

    module = sys.modules[module_path]
    assert module.value == 2

    del sys.modules[module_path]
    make_lazy(module_path)

    module = sys.modules[module_path]
    assert not isinstance(module, ModuleType)

    assert module.value == 2

# Generated at 2022-06-14 06:22:38.333737
# Unit test for function make_lazy
def test_make_lazy():
    import unittest

    class TestMakeLazy(unittest.TestCase):
        def test_make_lazy(self):
            lazy_module_name = 'make_lazy_test'

            class LazyModule:
                pass

            def get_lazy_module():
                return LazyModule

            def set_lazy_module(value):
                global LazyModule
                LazyModule = value

            sys.modules[lazy_module_name] = get_lazy_module()

            # Shouldn't be lazy yet
            self.assertIs(sys.modules[lazy_module_name], get_lazy_module())
            self.assertNotIn(lazy_module_name, sys.modules)

            # Lazy it up!
            make_lazy(lazy_module_name)

# Generated at 2022-06-14 06:23:07.690824
# Unit test for function make_lazy
def test_make_lazy():
    module_path = "_test_make_lazy_mod"

    # force module reload
    if module_path in sys.modules:
        del sys.modules[module_path]

    # define a test module
    # it should set a global and define a function when imported

# Generated at 2022-06-14 06:23:13.963091
# Unit test for function make_lazy
def test_make_lazy():
    import test_module
    make_lazy('test_module')

    assert '__name__' not in dir(test_module)
    assert '__name__' in dir(test_module.sub_module)
    assert '__name__' in dir(test_module.sub_module.sub_sub_module)

    assert test_module.sub_module.sub_sub_module.func() == 'test'

# Generated at 2022-06-14 06:23:23.169701
# Unit test for function make_lazy
def test_make_lazy():
    import os
    make_lazy('os')
    # os module should be lazy now.
    assert isinstance(os, _LazyModuleMarker)
    # We lazy load the path attribute on os.
    os.getcwd()
    assert not isinstance(os, _LazyModuleMarker)
    # The `path` attribute should be available but not the `sys` attribute.
    assert hasattr(os, 'getcwd')
    assert not hasattr(os, 'sys')
    # After being accessed, the standard `os` module should be available.
    assert os == __import__('os')

# Generated at 2022-06-14 06:23:27.980640
# Unit test for function make_lazy
def test_make_lazy():
    '''
    Test function make_lazy.
    '''
    sys.modules['foo.bar'] = None
    make_lazy('foo.bar')
    assert sys.modules['foo.bar'] is not None
    assert sys.modules['foo.bar'] is not 'foo/__init__.py'

# Generated at 2022-06-14 06:23:40.139853
# Unit test for function make_lazy
def test_make_lazy():
    mod_name = 'test_lazy_module'
    # TODO(msolo): This module should be accessible in a more standard way.
    import test_lazy_module

    # Verify that the module is already loaded.
    assert mod_name in sys.modules

    # Verify that the module can be imported again
    assert __import__(mod_name) is sys.modules[mod_name]

    # Mark the module as lazy
    make_lazy(mod_name)

    # Verify that the module was reloaded.
    # The test module should have a global variable `count` that tracks
    # the number of times it has been loaded.
    assert sys.modules[mod_name].count == 2

    # Verify that the module is an instance of LazyModule

# Generated at 2022-06-14 06:23:44.447074
# Unit test for function make_lazy
def test_make_lazy():
    import os
    import sys

    sys.modules['test_lazy_mod'] = None
    sys.modules['test_lazy_mod.testmod'] = None

    make_lazy('test_lazy_mod.testmod')
    assert isinstance(sys.modules['test_lazy_mod.testmod'], _LazyModuleMarker)

    from test_lazy_mod import testmod
    assert isinstance(sys.modules['test_lazy_mod.testmod'], ModuleType)

    x = testmod.modvar
    assert x == "hullabaloo"


# Generated at 2022-06-14 06:23:49.451218
# Unit test for function make_lazy
def test_make_lazy():
    """
    Unit test for function make_lazy
    """
    path = '__main__.lazy_mod'
    make_lazy(path)
    sys.modules[path].x = 1
    assert sys.modules[path].x == 1

# Generated at 2022-06-14 06:23:53.276230
# Unit test for function make_lazy
def test_make_lazy():
    make_lazy('test')
    assert 'test' in sys.modules

    import test
    assert sys.modules['test'] is test
    assert 'test' in sys.modules



# Generated at 2022-06-14 06:24:06.213232
# Unit test for function make_lazy
def test_make_lazy():
    """
    Test to make sure that `make_lazy` works.
    """

# Generated at 2022-06-14 06:24:19.446864
# Unit test for function make_lazy
def test_make_lazy():

    import os
    import nose
    import nose.tools

    def test_that_module_does_not_exist_in_sys_modules():
        nose.tools.assert_false(module_path in sys.modules)

    def test_that_module_does_exist_in_sys_modules():
        nose.tools.assert_true(module_path in sys.modules)

    def test_that_module_is_lazy():
        nose.tools.assert_false(module.__module__ in sys.modules)
        module.foo = 1
        nose.tools.assert_true(module.__module__ in sys.modules)

    module_path = '_test_module'
    make_lazy(module_path)
    module = __import__(module_path)

    # Our module does not really exist.
    test_