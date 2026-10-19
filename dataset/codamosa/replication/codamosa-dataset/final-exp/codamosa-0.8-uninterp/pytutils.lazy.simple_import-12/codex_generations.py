

# Generated at 2022-06-14 06:14:49.112499
# Unit test for function make_lazy
def test_make_lazy():
    # This example is a silly one, where we try to use make_lazy() to prevent
    # the time module from being imported.
    import time
    assert hasattr(time, 'time')

    # First, remove the time module from sys.modules
    del sys.modules['time']

    # Create a fake time module
    class FakeTimeModule(object):
        time = 1
        __metaclass__ = type

    sys.modules['time'] = FakeTimeModule()
    assert sys.modules['time'].time == 1

    # Now, import the real time module, lazily
    make_lazy('time')
    assert sys.modules['time'].time == 1, 'This import should be non-lazy'
    assert sys.modules['time'].time != time.time, 'Modules are different'

    # Now, use

# Generated at 2022-06-14 06:14:58.478741
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    mod_name = 'my_mod'

    sys.modules[mod_name] = 'my_mod_value'
    make_lazy(mod_name)
    assert isinstance(sys.modules[mod_name], _LazyModuleMarker)
    assert sys.modules[mod_name].__name__ == 'my_mod'

    from my_mod import __name__
    assert __name__ == 'my_mod'

    # Ensure it's still lazy
    assert isinstance(sys.modules[mod_name], _LazyModuleMarker)

# Generated at 2022-06-14 06:15:08.271800
# Unit test for function make_lazy
def test_make_lazy():
    make_lazy("django.apps")
    make_lazy("sorl.thumbnail.conf")
    import django.apps
    import sorl.thumbnail.conf
    from django.conf import global_settings
    print("django.apps", django.apps.__name__)
    print("sorl.thumbnail.conf", sorl.thumbnail.conf.__name__)
    print("django.apps", django.apps.get_app_config.__name__)
    print("sorl.thumbnail.conf", sorl.thumbnail.conf.get_module_name.__name__)

if __name__ == '__main__':
    test_make_lazy()

# Generated at 2022-06-14 06:15:19.072168
# Unit test for function make_lazy
def test_make_lazy():
    # patch sys modules
    sys_modules = sys.modules
    sys.modules = {}

    # __import__ returns a module in the global scope
    # we only want to test the functionality of make_lazy()
    make_lazy('test_module')

    mod = sys.modules['test_module']

    assert isinstance(mod, _LazyModuleMarker)
    assert not hasattr(mod, '__file__')

    mod.__file__ = 'foobar'

    assert not isinstance(mod, _LazyModuleMarker)
    assert hasattr(mod, '__file__')

    # return patched sys modules
    sys.modules = sys_modules

# Generated at 2022-06-14 06:15:28.760388
# Unit test for function make_lazy
def test_make_lazy():
    """
    Tests make_lazy.
    """
    module_path = 'test_module'
    lazy = make_lazy(module_path)
    assert lazy is None
    assert sys.modules[module_path] is not None
    assert isinstance(sys.modules[module_path], _LazyModuleMarker)
    # Module was not yet loaded
    assert not hasattr(sys.modules[module_path], 'test_attribute')
    # Import the module by accessing an attribute on it.
    sys.modules[module_path].test_attribute
    # Module was loaded
    assert hasattr(sys.modules[module_path], 'test_attribute')
    # Make sure we're now using the actual module
    assert sys.modules[module_path] is not _LazyModuleMarker
    # Module wasn't reloaded when importing again

# Generated at 2022-06-14 06:15:41.746149
# Unit test for function make_lazy
def test_make_lazy():
    # Create a mock module, module_path and sys.modules
    module_path = 'mod.sub.mod'
    module = ModuleType('mod.sub.mod')
    module.attr = 'attr'
    modules = {
        'mod': ModuleType('mod'),
    }
    modules['mod'].sub = ModuleType('mod.sub')
    modules['mod'].sub.mod = module

    # Set the mock module to sys.modules
    sys.modules = modules

    # Make the module lazy
    make_lazy(module_path)

    # Test that the module is not loaded
    assert module_path not in sys.modules
    assert 'mod.sub' in sys.modules

    # Test that its attributes can be fetched
    assert sys.modules[module_path].attr is module.attr

    # Test that isinstance works

# Generated at 2022-06-14 06:15:47.303020
# Unit test for function make_lazy
def test_make_lazy():
    module_path = "foo"
    make_lazy(module_path)
    assert sys.modules[module_path]
    assert module_path in sys.modules
    assert isinstance(sys.modules[module_path], _LazyModuleMarker)
    sys.modules.pop(module_path)



# Generated at 2022-06-14 06:15:58.306831
# Unit test for function make_lazy
def test_make_lazy():
    mod_path = 'mytestmodule.mytestmodule'

    # sanity test.
    assert mod_path in sys.modules

    # unload the module.
    del sys.modules[mod_path]

    # the module should be unloaded.
    assert mod_path not in sys.modules

    # mark the module to be lazy loaded.
    make_lazy(mod_path)

    # the module should be lazy again.
    assert mod_path in sys.modules

    # the module should be of type LazyModule
    assert isinstance(sys.modules[mod_path], _LazyModuleMarker)

    # the module should not be imported yet.
    assert sys.modules[mod_path].value is None

    # import the module
    __import__(mod_path)

    # the module should be imported
    assert sys.modules

# Generated at 2022-06-14 06:16:07.278039
# Unit test for function make_lazy
def test_make_lazy():
    class Mod:
        def __init__(self):
            self.x = "a"

    try:
        sys.modules["a"] = Mod()
        make_lazy("a")

        import a
        assert(isinstance(a, _LazyModuleMarker))
        assert("a" == a.x)

    finally:
        del sys.modules["a"]

make_lazy("confluent_kafka.cimpl")

from confluent_kafka import cimpl

__all__ = cimpl.__all__

# Generated at 2022-06-14 06:16:11.942796
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    module_path = 'tests.lazy_module'
    lazy_module = sys.modules[module_path]
    assert isinstance(lazy_module, _LazyModuleMarker)
    assert not hasattr(lazy_module, 'TEST_VAR')
    assert lazy_module.TEST_VAR == 'TEST'

# Generated at 2022-06-14 06:16:25.781514
# Unit test for function make_lazy
def test_make_lazy():
    """
    Tests that the module is not imported until the 'mark_used' function is called.
    """
    import sys
    import os
    import imp

    # Create a test package to import...
    import tempfile
    from types import ModuleType
    tempdir = tempfile.mkdtemp(dir='.')
    sys.path.insert(0, tempdir)
    test_pkg = os.path.join(tempdir, 'test_pkg')
    os.mkdir(test_pkg)
    test_file = os.path.join(test_pkg, 'test_file.py')
    open(test_file, 'a').close()
    test_file_init = os.path.join(test_pkg, '__init__.py')
    open(test_file_init, 'a').close()

# Generated at 2022-06-14 06:16:39.288109
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    import os
    import tempfile
    import logging

    mod = ("lazy_mod", """def hello():
            return "world"
        """)

    mod_path = os.path.join(tempfile.mkdtemp(),
                            "{0}.py".format(mod[0]))

    with open(mod_path, "w") as f:
        f.write(mod[1])

    sys.path.insert(0, os.path.dirname(mod_path))
    make_lazy(mod[0])

    import lazy_mod
    assert not isinstance(lazy_mod, _LazyModuleMarker)
    assert lazy_mod.hello() == "world"

    sys.path.remove(os.path.dirname(mod_path))
    logging.info(sys.path)


# Generated at 2022-06-14 06:16:46.411158
# Unit test for function make_lazy
def test_make_lazy():
    del sys.modules['foo.bar']
    import foo.bar

    assert foo.bar
    assert hasattr(foo.bar, 'baz')

    del sys.modules['foo.bar']

    make_lazy('foo.bar')

    assert isinstance(foo.bar, _LazyModuleMarker)
    assert not hasattr(foo.bar, 'baz')

    assert foo.bar.baz
    assert hasattr(foo.bar, 'baz')
    assert isinstance(foo.bar, _LazyModuleMarker) is False

# Generated at 2022-06-14 06:16:58.616447
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    import os
    import tempfile

    # Helper function to create a package with a module
    def create_package(package_name, module_name, module_data):
        package_path = tempfile.mkdtemp()

        # Create __init__.py
        init_path = os.path.join(package_path, "__init__.py")
        file(init_path, "w").close()

        # Create module
        module_path = os.path.join(package_path, module_name + ".py")
        with open(module_path, 'w') as f:
            f.write(module_data)
        return (package_path, module_name)

    # Create a package with a module

# Generated at 2022-06-14 06:17:04.235104
# Unit test for function make_lazy
def test_make_lazy():
    import imutils
    assert(isinstance(imutils, _LazyModuleMarker))
    print(dir(imutils))
    print(imutils.__doc__)
    print(imutils.version)
    assert(imutils.version != '1.2.0')

# Generated at 2022-06-14 06:17:08.969226
# Unit test for function make_lazy
def test_make_lazy():
    lazy_module_path = 'src.lazy_import'
    make_lazy(lazy_module_path)
    assert lazy_import.x == 1
    assert isinstance(sys.modules[lazy_module_path], _LazyModuleMarker)

# Generated at 2022-06-14 06:17:16.828378
# Unit test for function make_lazy
def test_make_lazy():
    """
    Test the make_lazy function.
    """

# Generated at 2022-06-14 06:17:24.995793
# Unit test for function make_lazy
def test_make_lazy():
    make_lazy('lazy')

    # verify module is lazy
    assert sys.modules['lazy'] is not None

    # make sure it's not imported until it's needed
    assert 'lazy.test' not in sys.modules

    # now import it
    import lazy.test
    assert isinstance(lazy.test, ModuleType)

    # make sure we can see an attribute
    assert lazy.test.__name__ == 'lazy.test'

# Generated at 2022-06-14 06:17:33.691670
# Unit test for function make_lazy
def test_make_lazy():
    """
    A basic test for the function make_lazy.
    """
    from types import ModuleType

    module_path = 'my_module'

    assert not hasattr(sys.modules, module_path)
    assert not isinstance(sys.modules.get(module_path), ModuleType)
    assert not isinstance(sys.modules.get(module_path), _LazyModuleMarker)

    make_lazy(module_path)

    assert hasattr(sys.modules, module_path)
    assert isinstance(sys.modules.get(module_path), _LazyModuleMarker)
    assert not isinstance(sys.modules.get(module_path), ModuleType)



# Generated at 2022-06-14 06:17:43.691965
# Unit test for function make_lazy
def test_make_lazy():
    """
    Unit test for `make_lazy`
    """
    # Test setting nonlocal variables from nested scope
    nonlocal_value = NonLocal(0)

    # Test that our `__mro__` method is working
    assert issubclass(LazyModule, ModuleType) is False

    def test_module_importing():
        """
        Test if the module imports correctly.
        """
        # Test that we can do a simple import without mucking with sys.modules
        assert import_module('make_lazy') is not None

        # Test that we can override a normal module in sys.modules and
        # cause correct import behavior
        sys.modules['make_lazy'] = ModuleType('make_lazy')

# Generated at 2022-06-14 06:17:48.165692
# Unit test for function make_lazy
def test_make_lazy():
    module_name = 'my_module'
    try:
        make_lazy(module_name)
        sys.modules[module_name].__name__ == module_name
        sys.modules[module_name].__file__ == '<lazy:%s>' % module_name
    finally:
        del sys.modules[module_name]

# Generated at 2022-06-14 06:17:55.354267
# Unit test for function make_lazy
def test_make_lazy():
    import random
    assert sys.modules['random'] == random
    make_lazy('random')
    assert 'random' in sys.modules
    assert sys.modules['random'].__class__.__name__ == 'LazyModule'
    assert 'randint' not in sys.modules['random'].__dict__
    assert sys.modules['random'].randint
    assert 'randint' in sys.modules['random'].__dict__

# Generated at 2022-06-14 06:17:57.589921
# Unit test for function make_lazy
def test_make_lazy():
    import lib_test_lazy

    lib_test_lazy.x = "test"  # make sure we can set an attribute on the module



# Generated at 2022-06-14 06:18:01.572585
# Unit test for function make_lazy
def test_make_lazy():
    from . import mock_make_lazy
    assert mock_make_lazy.var  # noqa
    assert mock_make_lazy.func() == 1
    assert mock_make_lazy.cls().method() == 2



# Generated at 2022-06-14 06:18:09.833109
# Unit test for function make_lazy
def test_make_lazy():
    from tests import lazy_test
    # Verify that the module is not yet loaded.
    if lazy_test.made_it:
        raise AssertionError("Lazy module was not lazy!")

    # Verify that accessing an attribute loads the module.
    lazy_test.made_it = True
    import tests.lazy_test
    if not tests.lazy_test.made_it:
        raise AssertionError("Lazy module was not loaded on access!")


if __name__ == '__main__':
    test_make_lazy()

# Generated at 2022-06-14 06:18:22.854414
# Unit test for function make_lazy
def test_make_lazy():
    from lazmod import make_lazy
    from types import ModuleType
    import sys

    module_path = 'lazmod.tests'

    __import__(module_path)
    assert isinstance(sys.modules[module_path], ModuleType)

    sys.modules[module_path] = 'foo'
    make_lazy(module_path)
    assert sys.modules[module_path] != 'foo'
    assert isinstance(sys.modules[module_path], ModuleType)

    #module has not been imported yet
    assert len(sys.modules) == 1

    #module has now been imported
    sys.modules[module_path].test_import
    assert len(sys.modules) == 2

    #module has already been imported
    sys.modules[module_path].test_import
    assert len(sys.modules)

# Generated at 2022-06-14 06:18:28.608122
# Unit test for function make_lazy
def test_make_lazy():
    module_name = 'test_lazy_module'

    import sys
    sys.modules[module_name] = __import__(module_name)
    assert module_name in sys.modules

    make_lazy(module_name)
    assert module_name in sys.modules
    assert isinstance(sys.modules[module_name], _LazyModuleMarker)

    # Make sure that the module is properly imported when necessary.
    assert sys.modules[module_name].imported is True


if __name__ == '__main__':
    test_make_lazy()

# Generated at 2022-06-14 06:18:41.987757
# Unit test for function make_lazy
def test_make_lazy():
    '''
    Test our lazy load function.  Note that this function will
    make a special module called lazy_test_mod.  Make sure to clean
    up.
    '''

    import sys
    import os
    import shutil
    import tempfile
    import functools

    def run_test(test_method):
        import sys
        orig_exception_hook = sys.excepthook

        # our exception hook will throw an error if it is called
        sys.excepthook = lambda exc_type, exc_value, exc_traceback: None

        # create the directory structure
        temp_dir = tempfile.mkdtemp()
        os.mkdir(os.path.join(temp_dir, 'lazy'))

# Generated at 2022-06-14 06:18:55.190879
# Unit test for function make_lazy
def test_make_lazy():
    __test__ = {}
    import sys
    import os
    import shutil
    import glob
    import stat
    import random

    TEMP_DIRECTORY = 'tempdir'
    sys.path.insert(0, TEMP_DIRECTORY)

    # A few random names to reduce collisions in /tmp
    TEMP_PREFIX_MODULE = 'LazyTestModule' + str(random.randrange(0, 10**7))
    TEMP_PREFIX_MODULE2 = 'LazyTestModule' + str(random.randrange(0, 10**7))
    TEMP_DIRECTORY = 'tempdir'
    REPLACEMENT = 'from lazy_import import make_lazy\n'

# Generated at 2022-06-14 06:18:58.944104
# Unit test for function make_lazy
def test_make_lazy():
    import socket
    make_lazy('socket')
    assert 'socket' not in globals()
    assert isinstance(socket, _LazyModuleMarker)
    assert socket is sys.modules['socket']
    assert socket.socket is socket._socketobject

# Generated at 2022-06-14 06:19:12.437591
# Unit test for function make_lazy
def test_make_lazy():
    """
    Create a temporary module, mark it as lazy and assert that it is lazy.
    """
    import tempfile
    import os.path

    # Create a fake module
    handle, module_path = tempfile.mkstemp()
    os.close(handle)  # Close the file descriptor
    f = open(module_path, 'w')
    f.write('a = 1')
    f.close()

    # Import the module for the first time and make sure it is not lazy
    mod = __import__(os.path.splitext(os.path.basename(module_path))[0])
    assert isinstance(mod, ModuleType)
    assert not isinstance(mod, _LazyModuleMarker)

    # Mark the module as lazy and make sure if it is really lazy

# Generated at 2022-06-14 06:19:16.257804
# Unit test for function make_lazy
def test_make_lazy():
    import gevent
    mod = make_lazy('gevent')
    assert isinstance(gevent, _LazyModuleMarker)
    gevent.spawn(lambda: 42)

# Generated at 2022-06-14 06:19:30.604043
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    import test_lazymodule  # Actual test code for LazyModule is in test_lazymodule.py

    assert sys.modules['test_lazymodule'] is None  # Ensure test_lazymodule is not imported
    assert 'version' not in test_lazymodule.__dict__

    # Access the attribute 'version' of test_lazymodule
    assert test_lazymodule.version == "v2"
    assert 'version' in test_lazymodule.__dict__

    # Ensure test_lazymodule.version is not lazy
    assert isinstance(sys.modules['test_lazymodule'].version, str)

    # Ensure test_lazymodule is not lazy
    assert isinstance(sys.modules['test_lazymodule'], ModuleType)

    # Cleanup

# Generated at 2022-06-14 06:19:38.162521
# Unit test for function make_lazy
def test_make_lazy():
    class ModuleTest(object):
        """
        A test class for the make_lazy function.
        """
        def __getattribute__(self, attr):
            """
            ModuleTest is a fake module, just to test make_lazy
            """

# Generated at 2022-06-14 06:19:47.745199
# Unit test for function make_lazy
def test_make_lazy():
    module_path = 'os'

    def reset():
        sys.modules[module_path].__dict__.clear()

        del sys.modules[module_path]

        make_lazy(module_path)

    reset()

    # Check that we can import it again
    import os

    # os should be a LazyModule
    assert isinstance(os, _LazyModuleMarker)
    assert os.name == 'posix'

    reset()

    # Check that we can import from a subpackage
    from os import path

    # os should be a LazyModule
    assert isinstance(os, _LazyModuleMarker)
    assert os.name == 'posix'
    assert os.path is path

# Generated at 2022-06-14 06:20:01.054122
# Unit test for function make_lazy
def test_make_lazy():
    import signal
    import os
    import sys

    make_lazy('signal')
    assert isinstance(signal, _LazyModuleMarker)
    assert hasattr(signal, 'SIGINT')
    try:
        assert hasattr(signal, 'alarm')
    except AttributeError:
        assert 'alarm' not in signal.__dict__
    if os.name == 'posix':
        signal.alarm(1)

    # os should not be lazy
    assert not isinstance(os, _LazyModuleMarker)

    # sys should not be lazy
    assert not isinstance(sys, _LazyModuleMarker)

    # test for __mro__.
    assert isinstance(signal, ModuleType)

    # test for __del__.
    # This test case is not necessary, because

# Generated at 2022-06-14 06:20:10.692985
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    import time

    # create some dummy module to use.
    class Foo():
        def bar(self):
            pass

    def foo():
        pass

    def run_test():
        def f():
            # If a module is lazily imported, it doesn't appear in sys.modules
            # until a member is imported from it
            assert baz not in sys.modules

            # accessing a member of the module forces it to import its dependencies
            module.foo()
            assert baz in sys.modules

            # module is not imported until we access a member
            start = time.time()
            module.baz.Bar()
            end = time.time()
            assert end-start > 1

        baz = "test_lazy_module"
        module = make_lazy(baz)


# Generated at 2022-06-14 06:20:18.693121
# Unit test for function make_lazy
def test_make_lazy():
    make_lazy('test')

    assert isinstance(test, _LazyModuleMarker)

    import test
    assert isinstance(test, ModuleType)
    test.test = 3

    reload(test)
    assert isinstance(test, ModuleType)
    assert test.test == 3

    del sys.modules['test']

    make_lazy('test')
    assert isinstance(test, _LazyModuleMarker)

    import test
    assert isinstance(test, ModuleType)
    assert test.test == 3

# Generated at 2022-06-14 06:20:24.043493
# Unit test for function make_lazy
def test_make_lazy():
    import random
    import sys

    def test_module(name, *keys):
        keys = keys or ['__name__', 'random']
        module = sys.modules[name]
        assert module is not None
        assert isinstance(module, _LazyModuleMarker)
        for key in keys:
            assert getattr(module, key) is not None

    module_path = 'tests.utils.test_lazy_module'
    test_module(module_path)
    make_lazy(module_path)
    test_module(module_path)
    assert sys.modules[module_path].random is random

# Generated at 2022-06-14 06:20:28.677977
# Unit test for function make_lazy
def test_make_lazy():
    assert "foo" not in sys.modules
    make_lazy("foo")
    assert "foo" in sys.modules
    assert isinstance(sys.modules["foo"], _LazyModuleMarker)

# Unit tests for class LazyModule

# Generated at 2022-06-14 06:20:44.339228
# Unit test for function make_lazy
def test_make_lazy():
    """
    Unit test function to make sure that, when the lazy module is imported,
    it has the properties that we expect.
    """

    # This unit test function will run before the `make_lazy` function
    # is loaded.  Therefore, we load it in the unit test.
    # Note: putting this code outside this function would cause an import error
    import tests.lazy as lazy_module

    class DummyModule(object):
        """
        A dummy module to be inserted into the `sys.modules` dict.
        """
        pass

    class DummyClass(object):
        """
        A dummy class to be inserted into the DummyModule.
        """
        pass

    # Insert our dummy module in to the `sys.modules` dict
    sys.modules['tests.lazy'] = DummyModule()

    # Put our dummy

# Generated at 2022-06-14 06:20:56.185908
# Unit test for function make_lazy
def test_make_lazy():
    import sys

    class X:
        pass

    # Mock the modules hash table in sys.
    sys.modules = {
        'test_module': X()
    }

    make_lazy('test_module')

    assert 'test_module' not in sys.modules

    # Get the attribute 'test_module'. This will cause it
    # to be imported, since sys.modules['test_module'] is
    # now a LazyModule instance.
    testmodule = sys.modules['test_module']

    assert 'test_module' in sys.modules

    # Check that the value in sys.modules['test_module'] is
    # the correct one, and not the LazyModule.
    assert sys.modules['test_module'] is testmodule

    # Test isinstance on the module.
    assert isinstance(testmodule, X)



# Generated at 2022-06-14 06:21:05.830659
# Unit test for function make_lazy
def test_make_lazy():
    from django.utils import six
    import sys

    if six.PY3:
        # This test won't work on Python 3, because `sys.modules` is no longer
        # writable.
        return

    make_lazy('django.utils.six')

    # Now that we've make the module `lazy`, we should be able to get the
    # module, but not any of its attributes.
    six = sys.modules['django.utils.six']
    assert not hasattr(six, 'PY3')
    assert isinstance(six, _LazyModuleMarker)
    assert six.PY3 == 3

    # We shouldn't be able to import the actual module.
    from django.utils import six as sixx
    assert six is not sixx
    assert sixx == sixx

# Generated at 2022-06-14 06:21:16.984882
# Unit test for function make_lazy
def test_make_lazy():
    # create a testing module
    sys.modules['test_module'] = sys.modules[__name__]
    # mark it as lazy
    make_lazy('test_module')

    #make sure it is an instance of LazyModule
    assert isinstance(sys.modules['test_module'], _LazyModuleMarker)
    # import another module to make sure test_module is not loaded
    __import__('os')

    # make sure the module is now loaded
    assert isinstance(sys.modules['test_module'], ModuleType)

    # make sure we can access objects as expected
    assert sys.modules['test_module'] == __import__('test_module')

# Generated at 2022-06-14 06:21:22.994018
# Unit test for function make_lazy
def test_make_lazy():
    import tempfile
    import os

    from common.testing_helpers import generate_test_function

    def _func():
        make_lazy('os')
        assert os.name == 'nt'

    generate_test_function(_func, 'test_make_lazy')


if __name__ == '__main__':
    test_make_lazy()

# Generated at 2022-06-14 06:21:30.335028
# Unit test for function make_lazy
def test_make_lazy():
    class MyModule(object):
        def my_method(self):
            return "Hello"
    sys.modules['my_module'] = MyModule()
    module = sys.modules['my_module']
    make_lazy('my_module')

    assert isinstance(module, _LazyModuleMarker)
    assert not isinstance(module, MyModule)
    assert module.my_method() == "Hello"
    assert isinstance(module, MyModule)
    assert isinstance(module, _LazyModuleMarker)

# Generated at 2022-06-14 06:21:42.967894
# Unit test for function make_lazy
def test_make_lazy():
    """
    Test that we can import a lazy module and it will be imported
    lazily.
    """

    class TestModule(object):
        """
        Module that we will use to test the laziness
        """

        CONST = 'test'

    TEST_MODULE_NAME = 'test_module'

    # Create the module and import it
    sys.modules[TEST_MODULE_NAME] = TestModule

    make_lazy(TEST_MODULE_NAME)


# Generated at 2022-06-14 06:21:53.093491
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    import os
    import os.path

    lazy_test_file_contents = """\
import sys

test_int = 5
test_string = "test string"
test_list = [test_int, test_string]
test_dict = dict(zip(test_list, test_list))

"""

    # Test setup
    directory = os.path.dirname(__file__)
    full_path = os.path.join(directory, "lazy_test_file.py")
    lazy_path = "lazy_test_file"
    f = open(full_path, 'w')
    f.write(lazy_test_file_contents)
    f.close()

    sys.path.append(directory)
    make_lazy(lazy_path)

    import lazy_

# Generated at 2022-06-14 06:22:06.744597
# Unit test for function make_lazy
def test_make_lazy():
    """
    Test the make_lazy function.
    """
    import sys
    import random
    import string
    from contextlib import contextmanager

    def make_temp_module():
        """
        A function that makes a temporary module that contains a variable 'test_value'
        which is a string of a random set of letters.
        """
        # Create a temporary module
        my_module = sys.modules.setdefault(
            ''.join(random.choice(string.ascii_letters) for _ in range(5)),
            types.ModuleType('my_module'))
    
        # Create the variable test_value in the module
        my_module.test_value = ''.join(random.choice(string.ascii_letters) for _ in range(10))
    
        return my_module


# Generated at 2022-06-14 06:22:18.187162
# Unit test for function make_lazy
def test_make_lazy():
    import django.conf
    import django.db
    # Test that make_lazy does not make conf lazy
    conf = __import__('django.conf')
    assert not isinstance(conf, _LazyModuleMarker)
    # Test that make_lazy does make db lazy
    db = __import__('django.db')
    assert isinstance(db, _LazyModuleMarker)
    # Test that make_lazy does import submodule of lazy module but does not
    # make submodule lazy
    db = __import__('django.db.models')
    assert not isinstance(db, _LazyModuleMarker)
    # Test that an attribute on a lazy module imports the entire module
    db = __import__('django.db.models')

# Generated at 2022-06-14 06:22:36.330754
# Unit test for function make_lazy
def test_make_lazy():
    """
    Check if unit test is running by checking if stdout has write method.
    If not then we are not running unit test and we return.
    """

    import os
    import sys
    mod_name = "make_lazy_test_mod"
    mod_file = "make_lazy_test_mod.py"

    if not hasattr(sys.stdout, 'write'):
        return


# Generated at 2022-06-14 06:22:48.364883
# Unit test for function make_lazy
def test_make_lazy():
    # XXX: We will break this test if we ever change the name of our
    #      'LazyModule' type.
    import imp
    import random
    import sys
    import types

    # create a random name for our module
    mod_name = "lazy_test_module_" + "".join(chr(random.randint(ord('a'), ord('z'))) for x in range(10))
    sys.modules["lazy_test_module_" + mod_name] = None

    # Add a random name to `sys.modules`
    make_lazy(mod_name)

    # Make sure we really have a lazy module
    assert isinstance(sys.modules[mod_name], _LazyModuleMarker)


# Generated at 2022-06-14 06:22:55.364570
# Unit test for function make_lazy
def test_make_lazy():

    def import_test():
        from .test_app_1 import models  # noqa

    def import_test_lazy():
        from .test_app_lazy_1 import models  # noqa

    sys.modules['test_app_1'] = None
    sys.modules['test_app_lazy_1'] = None

    # assert that the original import has no side effects
    eq_(models, None)

    with patch('django_addons.utils.lazy_module.settings') as settings:
        settings.INSTALLED_APPS = []
        assert_raises(ImportError, import_test)

    # assert that a lazy import doesn't have side effects
    eq_(models, None)

    with patch('django_addons.utils.lazy_module.settings') as settings:
        settings.INSTALLED_

# Generated at 2022-06-14 06:23:08.293332
# Unit test for function make_lazy
def test_make_lazy():
    # The test module here should have a really long import time!
    # Otherwise, by the time we query `test_mod.__mro__`, the import has
    # already been finished and the test is not very effective.

    make_lazy('test_mod')

    import test_mod
    import time

    start = time.time()

    # This should take very little time because we haven't actually imported
    # test_mod.
    assert isinstance(sys.modules['test_mod'], _LazyModuleMarker)

    # If our module hasn't been imported yet, it should take a really long time
    # to get `__mro__`, because it will trigger an import.
    assert isinstance(test_mod, _LazyModuleMarker)

    # By the time we check the time, the import should have finished, so we
   

# Generated at 2022-06-14 06:23:12.167203
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    make_lazy('string')
    assert 'string' in sys.modules
    assert isinstance(sys.modules['string'], _LazyModuleMarker)
    assert hasattr(sys.modules['string'], 'ascii_lowercase')
    assert 'string' in sys.modules
    assert isinstance(sys.modules['string'], ModuleType)
    import string
    assert isinstance(sys.modules['string'], ModuleType)
    assert string is sys.modules['string']

# Generated at 2022-06-14 06:23:19.580311
# Unit test for function make_lazy
def test_make_lazy():
    """
    Test function make_lazy.
    """
    import sys
    import types
    sys.modules['lazy_test_module'] = None

    make_lazy('lazy_test_module')

    assert isinstance(sys.modules['lazy_test_module'], _LazyModuleMarker)
    assert not isinstance(sys.modules['lazy_test_module'], types.ModuleType)



# Generated at 2022-06-14 06:23:29.979907
# Unit test for function make_lazy
def test_make_lazy():
    module_path = 'django.db._backends'

    # module should not have already been imported
    assert module_path not in sys.modules

    make_lazy(module_path)

    # module should have been "imported" now
    assert module_path in sys.modules

    # Check that we can get attributes off of the module
    # and that the module is still lazy
    mod = sys.modules[module_path]

    assert 'BaseDatabaseFeatures' in dir(mod)
    assert isinstance(mod, _LazyModuleMarker)

    # If we access the attribute, the module should no longer be lazy
    mod.BaseDatabaseFeatures

    assert isinstance(mod, ModuleType)

# Generated at 2022-06-14 06:23:31.132621
# Unit test for function make_lazy
def test_make_lazy():
    make_lazy('lazy.module')

# Generated at 2022-06-14 06:23:40.188512
# Unit test for function make_lazy
def test_make_lazy():
    def _creatures():
        make_lazy('animals')
        import animals
        import plants
        return (animals.animal, plants.animal)

    # result of _creatures()
    (animal, plant) = _creatures()

    # check the result
    assert isinstance(animal, _LazyModuleMarker)
    assert isinstance(plant, _LazyModuleMarker)
    assert animal.__mro__() == (LazyModule, ModuleType)
    assert plant.__mro__() == (LazyModule, ModuleType)
    assert animal.fish is animals.animal.fish
    assert plant.fish is plants.animal.fish

# Generated at 2022-06-14 06:23:43.699736
# Unit test for function make_lazy
def test_make_lazy():
    import os
    import sys

    make_lazy('os')
    assert hasattr(os, 'getcwd')
    assert isinstance(os, _LazyModuleMarker)
    assert os.getcwd() == os.path.abspath('.')

    # remove os from the global sys.modules
    del sys.modules['os']
    # this should import os, and not raise an error
    assert isinstance(os, _LazyModuleMarker)

# Generated at 2022-06-14 06:24:07.283561
# Unit test for function make_lazy
def test_make_lazy():
    """
    Test that we can import modules marked as lazy
    """
    # First, try a basic test
    make_lazy('test_module')
    # import it
    import test_module
    # and make sure it works.
    assert test_module.foo == 'bar'

    # Now import some nested modules.
    # The `importlib` module we want to import is also lazy,
    # so this should work
    import sys
    import imp
    sys.modules['importlib'] = imp.new_module('importlib')
    make_lazy('tests.imports.import_from_importlib')

    from tests.imports.import_from_importlib import ModuleSpec
    assert isinstance(ModuleSpec, type)

    # Now, try a module with a '.' in it.
    # Modules with a '.'

# Generated at 2022-06-14 06:24:17.544100
# Unit test for function make_lazy
def test_make_lazy():
    """
    Test that make_lazy functions as expected
    """
    import tests.lazy_module  # NOQA - this is just for a test to work
    del sys.modules['tests.lazy_module']
    make_lazy('tests.lazy_module')
    tests.lazy_module.fake_attr = 100
    assert tests.lazy_module.fake_attr == 100
    assert isinstance(tests.lazy_module, _LazyModuleMarker)
    assert 'fake_attr' not in sys.modules['tests.lazy_module'].__dict__

# Generated at 2022-06-14 06:24:30.811382
# Unit test for function make_lazy
def test_make_lazy():
    sys.modules['test_make_lazy'] = None

    # Ensure that no module is loaded at the start of this test.
    assert 'test_make_lazy' not in sys.modules

    # Ensure that the module is loaded after an attribute has been requested
    # from it.
    make_lazy('test_make_lazy')
    assert isinstance(sys.modules['test_make_lazy'], _LazyModuleMarker)

    assert sys.modules['test_make_lazy'].__name__ == "test_make_lazy"

    # Ensure that the module is not loaded before an attribute is requested
    # from it.
    del sys.modules['test_make_lazy']
    assert 'test_make_lazy' not in sys.modules

    make_lazy('test_make_lazy')


# Generated at 2022-06-14 06:24:41.296484
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    import tests.lazy
    from tests.modules import lazy_module

    lazy_module_path = 'tests.modules.lazy_module'

    #Make sure module was imported
    assert lazy_module_path in sys.modules
    #Make sure the actual module is not yet loaded
    #and instead a LazyModule is in its place
    assert isinstance(sys.modules[lazy_module_path], _LazyModuleMarker)
    #Make sure the LazyModule can be used like the real module
    assert lazy_module.__name__ == 'tests.modules.lazy_module'
    assert lazy_module.TEST_ATTR == 123