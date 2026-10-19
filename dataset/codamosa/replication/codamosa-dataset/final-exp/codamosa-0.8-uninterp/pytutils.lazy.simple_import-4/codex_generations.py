

# Generated at 2022-06-14 06:14:36.146960
# Unit test for function make_lazy
def test_make_lazy():
    """
    Unit test for the make_lazy function
    """
    import startproject

# Generated at 2022-06-14 06:14:49.064482
# Unit test for function make_lazy
def test_make_lazy():
    # clear out the sys.modules cache.

    sys.modules['z'] = None
    z = sys.modules['z']
    assert z is None

    def module_side_effect():
        return 2
    module_side_effect()

    # Tests if the module is not being preloaded via the `sys.modules` cache
    make_lazy('z')
    assert module_side_effect() == 1

    # The `z` module will have been preloaded now --
    # Test that we can now reference the module directly.
    z = sys.modules['z']
    assert isinstance(z, _LazyModuleMarker)
    assert z.attribute_of_z == 7
    assert module_side_effect() == 2
    assert sys.modules['z'].attribute_of_z == 7

# Generated at 2022-06-14 06:14:56.810903
# Unit test for function make_lazy
def test_make_lazy():
    import os
    import tempfile
    import shutil

    tempdir = None

# Generated at 2022-06-14 06:15:09.057233
# Unit test for function make_lazy
def test_make_lazy():
    """
    This is a unit test for function make_lazy
    """

    # Save state of sys.modules
    modules = sys.modules.copy()

    # Add test module to sys.modules
    test_name = 'lazy_test'
    sys.modules[test_name] = None

    # Call make_lazy on test_name
    make_lazy(test_name)

    # Check that sys.modules[test_name] is a LazyModule
    assert test_name in sys.modules and \
           isinstance(sys.modules[test_name], _LazyModuleMarker)

    # Check that sys.modules[test_name] is a LazyModule
    # This should be true because of the __mro__ override
    assert isinstance(sys.modules[test_name], ModuleType)

    # Restore state

# Generated at 2022-06-14 06:15:18.503182
# Unit test for function make_lazy
def test_make_lazy():
    test_module = "test_make_lazy"
    assert test_module not in sys.modules
    make_lazy(test_module)
    assert isinstance(sys.modules[test_module], _LazyModuleMarker)
    from test_make_lazy import test_attr
    assert sys.modules[test_module].test_attr is test_attr
    assert test_attr() == 0
    assert sys.modules[test_module].test_attr() == 0


MAKE_LAZY_FUNC = make_lazy

# Generated at 2022-06-14 06:15:28.461611
# Unit test for function make_lazy
def test_make_lazy():
    import types
    module = types.ModuleType('test_make_lazy')

    module.__dict__['__file__'] = 'foo'
    module.__dict__['x'] = 'abc'

    sys.modules[module.__name__] = module

    make_lazy(module.__name__)
    del sys.modules[module.__name__]

    test_module = __import__(module.__name__)
    assert test_module.x == 'abc'

    # Test reloading
    module.__dict__['x'] = '123'
    reload(test_module)
    assert test_module.x == '123'

    for key in list(sys.modules):
        if key.startswith('test_make_lazy'):
            del sys.modules[key]

# Generated at 2022-06-14 06:15:40.252127
# Unit test for function make_lazy
def test_make_lazy():
    mod = make_lazy("django.utils.lazy_module_tests.foo")
    assert mod is not None
    assert isinstance(mod, ModuleType)
    assert isinstance(mod, _LazyModuleMarker)
    assert getattr(mod, 'foo') == 'foo'
    assert getattr(mod, 'bar') == 'bar'

    mod = make_lazy("django.utils.lazy_module_tests.bar")
    assert mod is not None
    assert isinstance(mod, ModuleType)
    assert isinstance(mod, _LazyModuleMarker)
    assert getattr(mod, 'foo') == 'foo'
    assert getattr(mod, 'bar') == 'bar'



# Generated at 2022-06-14 06:15:51.604261
# Unit test for function make_lazy
def test_make_lazy():
    """
    Tests that the make_lazy decorator actually works.
    """
    def test_module_is_lazy(module_path, sys_modules=sys.modules):
        """
        Tests that a module is lazy.
        """
        assert isinstance(sys_modules[module_path], _LazyModuleMarker)
        assert not sys_modules.get(module_path + '.testmodule', False)
        assert hasattr(sys_modules[module_path], 'testmodule')

    def test_module_is_no_longer_lazy(module_path, sys_modules=sys.modules):
        """
        Tests that a module is no longer lazy.
        """
        assert not isinstance(sys_modules[module_path], _LazyModuleMarker)

# Generated at 2022-06-14 06:15:57.821389
# Unit test for function make_lazy
def test_make_lazy():
    """
    Unit Tests for function make_lazy
    """
    import os
    import sys

    make_lazy('os')
    assert sys.modules['os'] is not os

    make_lazy('sys')
    assert sys.modules['os'] is os
    assert sys.modules['sys'] is not sys

    make_lazy('foo_bar')
    assert sys.modules['foo_bar'] is not None

# Generated at 2022-06-14 06:16:00.972437
# Unit test for function make_lazy
def test_make_lazy():
    def squared(x):
        return x * x
    make_lazy(__name__)
    assert squared(2) == 4

# Generated at 2022-06-14 06:16:13.989420
# Unit test for function make_lazy
def test_make_lazy():
    # todo: add more tests
    import sys
    import tempfile
    import shutil
    import pytest

    module_name = 'lazy_foo'
    module_path = 'lazy_bar'

    # create a new directory in test_dir
    test_dir = tempfile.mkdtemp()
    make_lazy(module_path)

    # make sure that make_lazy() works as expected
    with pytest.raises(AttributeError):
        sys.modules[module_path].foo()

    # create a new directory for lazy_foo
    os.makedirs(os.path.join(test_dir, module_path))

    # make sure that the directory is created
    assert os.path.isdir(os.path.join(test_dir, module_path))

    # create a new file __

# Generated at 2022-06-14 06:16:23.901625
# Unit test for function make_lazy
def test_make_lazy():
    import sys as modsys
    import importlib

    sys_modules = modsys.modules
    module_path = 'test_module'

    # Mark this module as lazy
    make_lazy(module_path)

    # Ensure module was added to sys.modules
    assert module_path in sys_modules

    # Ensure it was added as a LazyModule
    mod = sys_modules[module_path]
    assert isinstance(mod, _LazyModuleMarker)

    # Ensure we can still import it
    importlib.import_module(module_path)

    # Ensure it was added as a LazyModule
    mod = sys_modules[module_path]
    assert not isinstance(mod, _LazyModuleMarker)

# Generated at 2022-06-14 06:16:32.532600
# Unit test for function make_lazy
def test_make_lazy():
    # Test when the module is not in sys.modules
    assert "test_make_lazy" not in sys.modules
    make_lazy("test_make_lazy")
    assert "test_make_lazy" in sys.modules
    assert isinstance(sys.modules["test_make_lazy"], ModuleType)
    assert isinstance(sys.modules["test_make_lazy"], _LazyModuleMarker)
    assert not hasattr(sys.modules["test_make_lazy"], "__mro__")
    assert not hasattr(sys.modules["test_make_lazy"], "__getattribute__")
    assert not hasattr(sys.modules["test_make_lazy"], "__name__")
    assert not hasattr(sys.modules["test_make_lazy"], "__file__")

    # Test

# Generated at 2022-06-14 06:16:41.307473
# Unit test for function make_lazy
def test_make_lazy():
    mod = NonLocal(None)
    def fake_import(name):
        mod.value = name

    orig_import = __import__
    try:
        __import__ = fake_import
        make_lazy("foo")

        assert mod.value is None
        assert sys.modules["foo"] is not None

        # Trigger the import
        from foo import bar  # noqa

        assert mod.value == "foo"

        # make sure we don't import again:
        from foo import baz  # noqa

        assert mod.value == "foo"
    finally:
        __import__ = orig_import

# Generated at 2022-06-14 06:16:54.627242
# Unit test for function make_lazy
def test_make_lazy():
    import atexit
    import sys
    from django.utils._os import npath

    module_path = "django.utils.unittest.util"
    make_lazy(module_path)

    util = sys.modules[module_path]
    assert isinstance(util, _LazyModuleMarker)

    with npath("django/utils/unittest/util.py"):
        assert util.__file__ == "<non-existing-file>"

    # Make sure that our module is not actually imported.
    import django.utils.unittest
    assert module_path not in sys.modules

    # Now trigger the import of our module
    sys.modules[module_path].NON_EXISTENT_ATTRIBUTE

    # Make sure our module is imported now
    assert module_path in sys.modules


# Generated at 2022-06-14 06:17:03.202846
# Unit test for function make_lazy
def test_make_lazy():
    # test non-existing file
    assert not os.path.exists('test_lazy.py')
    make_lazy('test_lazy')
    assert 'test_lazy' in sys.modules

    # A 'LazyModule' object should be created.
    assert isinstance(sys.modules['test_lazy'], _LazyModuleMarker)

    # test existing file
    assert os.path.exists('test_make_lazy.py')
    make_lazy('test_make_lazy')
    assert 'test_make_lazy' in sys.modules

    # A 'LazyModule' object should be created.
    assert isinstance(sys.modules['test_make_lazy'], _LazyModuleMarker)

    # Now test if attributes are handled correcly
    import test_lazy

# Generated at 2022-06-14 06:17:05.434366
# Unit test for function make_lazy
def test_make_lazy():
    make_lazy('inspect')
    assert isinstance(inspect, _LazyModuleMarker)

# Generated at 2022-06-14 06:17:12.557811
# Unit test for function make_lazy
def test_make_lazy():
    sys.modules['test_make_lazy'] = None
    make_lazy('test_make_lazy')
    mod = sys.modules['test_make_lazy']

    assert isinstance(mod, _LazyModuleMarker)
    assert mod.__name__ == 'test_make_lazy'
    assert mod.__file__.endswith('test_make_lazy')

    del sys.modules['test_make_lazy']

# Generated at 2022-06-14 06:17:21.344579
# Unit test for function make_lazy
def test_make_lazy():
    try:
        make_lazy("tests.test_lazy.mod")

        # test that our module is loaded
        import tests  # noqa

        assert tests.test_lazy.mod.hello() == "hello"

        # test that our module is lazy
        assert isinstance(tests.test_lazy.mod, _LazyModuleMarker)

    finally:
        # cleanup
        del sys.modules['tests.test_lazy.mod']
        del sys.modules['tests.test_lazy']
        del sys.modules['tests']



# Generated at 2022-06-14 06:17:26.010661
# Unit test for function make_lazy
def test_make_lazy():
    import os
    import sys

    make_lazy('os')
    assert os.__name__ == 'os'

    loaded = False

    def _os():
        global loaded
        loaded = True

# Generated at 2022-06-14 06:17:35.302978
# Unit test for function make_lazy
def test_make_lazy():
    try:
        from jupyter_server.version import gen_version
    except ImportError:
        return

    gen_version_copy = gen_version
    make_lazy('jupyter_server.version')
    assert gen_version_copy is not gen_version



# Generated at 2022-06-14 06:17:42.189373
# Unit test for function make_lazy
def test_make_lazy():
    """
    Test the make_lazy utility function
    """
    # Make sure that it works in a function
    def add_lazy_module():
        make_lazy('path.to.module')
    add_lazy_module()

    # Make sure that we can access the module
    import path.to.module as mod
    assert 'mod' == mod.mod_name

# Generated at 2022-06-14 06:17:53.017346
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    import itertools

    module = 'itertools'
    make_lazy(module)
    assert module not in sys.modules
    assert isinstance(itertools, _LazyModuleMarker)
    assert module in sys.modules

    # Evaluate the lazy module and check that it completes successfully
    import itertools
    assert isinstance(itertools, ModuleType)


if __name__ == '__main__':
    import sys
    import itertools

    # Exercise the function directly
    test_make_lazy()

    # Exercise the function from the command line
    make_lazy('sys')
    make_lazy('itertools')
    assert 'sys' not in sys.modules
    assert 'itertools' not in sys.modules

# Generated at 2022-06-14 06:17:58.942680
# Unit test for function make_lazy
def test_make_lazy():
    module_path = "os.path"
    make_lazy(module_path)
    if not isinstance(sys.modules[module_path], _LazyModuleMarker):
        raise AssertionError("make_lazy: The named module '%s' is not lazy" % module_path)

# Generated at 2022-06-14 06:18:10.480949
# Unit test for function make_lazy
def test_make_lazy():
    # Mock the sys module
    sys.modules = {}
    # This is the module path that's used by the code in _taskmanager_utils
    # and we will assume it's the same for the test.
    module_path = "pyVmomi.VmomiSupport.Vmodl"

    # We haven't imported anything yet so the module should be
    # set to None
    assert sys.modules.get(module_path) is None

    # Make the module lazy
    make_lazy(module_path)
    # Check that it's now of type LazyModule
    assert isinstance(sys.modules.get(module_path), _LazyModuleMarker)

    # Call the function, which should return true since we've mocked it
    response = LazyModule.Fault()
    assert response

    # Now check that the module is still

# Generated at 2022-06-14 06:18:20.301304
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    import copy
    def test_imports():
        """Function to test make_lazy function"""
        # import ssl
        make_lazy("ssl")

    test_imports()
    assert isinstance(sys.modules["ssl"], _LazyModuleMarker)
    assert sys.modules["ssl"] is not None
    assert sys.modules["ssl"]
    assert ssl
    assert isinstance(sys.modules["ssl"].socket, object)
    assert isinstance(sys.modules["ssl"].SSLContext, object)
    assert sys.modules["ssl"] is not copy.deepcopy(sys.modules["ssl"])

# Generated at 2022-06-14 06:18:26.993857
# Unit test for function make_lazy
def test_make_lazy():
    def _t():
        mod = sys.modules['lazy_module']
        assert isinstance(mod, _LazyModuleMarker)
        assert not hasattr(mod, 'attr')
        mod.attr
        assert hasattr(mod, 'attr')

    sys.modules['lazy_module'] = _LazyModuleMarker()
    try:
        make_lazy('lazy_module')
        _t()
    finally:
        del sys.modules['lazy_module']



# Generated at 2022-06-14 06:18:40.484917
# Unit test for function make_lazy
def test_make_lazy():
    """
    Verify that make_lazy function works.
    """
    import sys
    import unittest
    import time

    class MakeLazyTestCase(unittest.TestCase):
        """
        Validate module loading is delayed.
        """
        def setUp(self):
            self._mod_name = 'make_lazy_test_case'
            self._module = sys.modules[self._mod_name]

        def test_module_is_instance_of_lazymodule(self):
            """
            Verify that the module is an instance of LazyModule.
            """
            self.assertTrue(isinstance(self._module, _LazyModuleMarker))

        def test_module_is_not_loaded(self):
            """
            Verify that the module hasn't been loaded yet.
            """
            self

# Generated at 2022-06-14 06:18:53.514773
# Unit test for function make_lazy
def test_make_lazy():
    """
    Tests method make_lazy.
    """
    import tempfile
    import shutil

    for _ in xrange(10):
        dirname = tempfile.mkdtemp(prefix='tmp_lazy_import')


# Generated at 2022-06-14 06:19:00.353731
# Unit test for function make_lazy
def test_make_lazy():
    """
    Unit tests for Make lazy module
    """
    import sys
    module_path = 'settings'
    make_lazy(module_path)
    assert sys.modules[module_path].__class__.__name__ == 'LazyModule'

    #When a attribute is called, module imports all modules
    assert sys.modules[module_path].__class__.__name__ == 'module'
    assert sys.modules[module_path].__name__ == 'settings'



# Generated at 2022-06-14 06:19:13.814503
# Unit test for function make_lazy
def test_make_lazy():
    """
    Ensure we can mark a module as lazy and invoke it.
    """
    # We are going to import 'django.db.backends.util' and make it lazy.
    module_path = 'django.db.backends.util'
    module = __import__(module_path, [], [], [module_path.split('.')[-1]])
    assert isinstance(module, ModuleType)

    # Make the module lazy
    make_lazy(module_path)
    # Check to make sure it is lazy
    assert not isinstance(module, ModuleType)
    assert isinstance(module, _LazyModuleMarker)

    # The next import should complete
    module = __import__(module_path, [], [], [module_path.split('.')[-1]])

# Generated at 2022-06-14 06:19:20.898098
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    make_lazy('temp_module')
    assert isinstance(sys.modules['temp_module'], _LazyModuleMarker), "Incorrect Type"
    assert sys.modules['temp_module'].__mro__ == (sys.modules['temp_module'].__class__, ModuleType), "Incorrect MRO"

# Generated at 2022-06-14 06:19:33.915536
# Unit test for function make_lazy
def test_make_lazy():
    import pylint.testutils.pylint_plugins as test_pylint_plugins
    import pylint.testutils.functional as test_functional
    assert not isinstance(test_pylint_plugins, _LazyModuleMarker)
    assert not isinstance(test_functional, _LazyModuleMarker)

    make_lazy('pylint.testutils.functional')
    make_lazy('pylint.testutils.pylint_plugins')

    import pylint.testutils.functional as test_functional
    import pylint.testutils.pylint_plugins as test_pylint_plugins

    assert isinstance(test_pylint_plugins, _LazyModuleMarker)
    assert not isinstance(pylint.testutils.pylint_plugins, _LazyModuleMarker)

# Generated at 2022-06-14 06:19:45.264970
# Unit test for function make_lazy
def test_make_lazy():
    try:
        import importlib

        make_lazy('importlib')
        if not isinstance(importlib, _LazyModuleMarker):
            raise Exception()
        make_lazy('importlib.util')
        if not isinstance(importlib.util, _LazyModuleMarker):
            raise Exception()
        util = importlib.util
        # We do not want to make circular imports but we have a lazy version
        importlib.util = None
        make_lazy('importlib.util')
        if util != importlib.util:
            raise Exception()
        t = util.__name__
        if t != 'importlib.util':
            raise Exception()
    except:
        import traceback
        traceback.print_exc()
        return 1


# Generated at 2022-06-14 06:19:58.844705
# Unit test for function make_lazy
def test_make_lazy():
    # Simple case
    sys.modules = {}
    make_lazy('django.contrib.auth')
    assert isinstance(sys.modules['django.contrib.auth'],
                      _LazyModuleMarker)
    # Check if the module has not been imported yet
    assert not hasattr(sys.modules['django.contrib.auth'], 'models')
    # Try to import an attribute
    from django.contrib.auth import models
    assert sys.modules.get('django.contrib.auth.models') is models
    # Check if the module has been imported now
    assert hasattr(sys.modules['django.contrib.auth'], 'models')
    # Check if the module reference has been updated
    assert sys.modules['django.contrib.auth'] is models.__module__

    # Insert

# Generated at 2022-06-14 06:20:09.463493
# Unit test for function make_lazy
def test_make_lazy():
    module_path = 'mymodule'

    # import the module so it is 'not' our LazyModule
    import mymodule

    # make the module lazy
    make_lazy(module_path)

    # get the module out of sys.modules
    mod = sys.modules[module_path]

    # assert that the module still exists
    assert mod is not None

    # assert that the module is a LazyModule
    assert isinstance(mod, _LazyModuleMarker)

    # assert that it is a LazyModule
    assert mod.__class__.__name__ == 'LazyModule'

    # assert that we can retrieve a value off the module
    assert mod.foo == 'foo'

    # assert that the module is not still a 'LazyModule'
    assert not isinstance(mod, _LazyModuleMarker)



# Generated at 2022-06-14 06:20:21.358414
# Unit test for function make_lazy
def test_make_lazy():
    is_not_lazy = "import sys\nsys.modules['foo'] = LazyModule()\n"
    is_no_longer_lazy = "import sys\ndel sys.modules['foo']\n"
    is_not_a_module = "import sys; del sys.modules['foo']\n"
    is_not_a_lazy_module = "import sys\nclass NotLazy(): pass\nsys.modules['foo'] = NotLazy()\n"
    is_still_lazy = "import sys\nassert sys.modules['foo'].__class__.__name__ == 'LazyModule'\n"

# Generated at 2022-06-14 06:20:29.638943
# Unit test for function make_lazy
def test_make_lazy():
    module_path = '__test_module_path__'

    make_lazy(module_path)
    assert module_path in sys.modules
    assert isinstance(sys.modules[module_path], _LazyModuleMarker)

    sys.modules[module_path].value = 'test value'

    # Check that the module is replaced with the real module
    assert sys.modules[module_path] is module.value

    del sys.modules[module_path]

# Generated at 2022-06-14 06:20:36.313817
# Unit test for function make_lazy
def test_make_lazy():
    """
    Unit tests for the make_lazy function.
    """
    import django
    make_lazy('django')

    from django.test.testcases import settings
    assert settings.USE_TZ

    from django.sessions.models import Session
    assert Session.DoesNotExist

    from django.test.testcases import settings
    assert settings.USE_TZ

# Generated at 2022-06-14 06:20:49.426564
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    sys.modules.pop("__main__")
    sys.modules.pop("test_lazy_module")
    sys.modules.pop("test_lazy_module.test_module")

    import test_lazy_module

    assert "__main__" in sys.modules
    assert "test_lazy_module" in sys.modules
    assert "test_lazy_module.test_module" not in sys.modules
    assert isinstance(test_lazy_module.submodule, _LazyModuleMarker)

    test_lazy_module.submodule.foo
    assert "test_lazy_module.test_module" in sys.modules
    assert isinstance(test_lazy_module.submodule, ModuleType)

# Generated at 2022-06-14 06:21:09.996872
# Unit test for function make_lazy
def test_make_lazy():
    module_path = 'my_module'

    sys_modules = sys.modules  # cache in the locals

    # store our 'instance' data in the closure.
    module = NonLocal(None)

    class LazyModule(_LazyModuleMarker):
        def __mro__(self):
            return (LazyModule, ModuleType)

        def __getattribute__(self, attr):
            if module.value is None:
                del sys_modules[module_path]
                module.value = __import__(module_path)

                sys_modules[module_path] = __import__(module_path)

            return getattr(module.value, attr)

    sys_modules[module_path] = LazyModule()

    test = isinstance(sys_modules[module_path], _LazyModuleMarker)
   

# Generated at 2022-06-14 06:21:19.134031
# Unit test for function make_lazy
def test_make_lazy():
    reload(sys)
    original_sys = sys

    module_name = '__test_make_lazy'
    module = types.ModuleType(module_name)
    sys.modules[module_name] = module

    make_lazy(module_name)

    assert module is not sys.modules[module_name]
    assert isinstance(sys.modules[module_name], _LazyModuleMarker)
    assert isinstance(sys.modules[module_name], types.ModuleType)

    del sys.modules[module_name]

    sys = original_sys


if __name__ == '__main__':
    test_make_lazy()

# Generated at 2022-06-14 06:21:28.581518
# Unit test for function make_lazy
def test_make_lazy():
    import os
    from types import ModuleType
    make_lazy('email.mime')
    module = __import__('email.mime')
    assert isinstance(module, ModuleType)
    assert isinstance(module, _LazyModuleMarker)
    assert hasattr(module, '_LazyModuleMarker')
    # The following does not work on LazyModule
    #assert os.path.isfile(module.__file__)
    #import email.mime.multipart
    #assert os.path.isfile(email.mime.multipart.__file__)

# Generated at 2022-06-14 06:21:34.405511
# Unit test for function make_lazy
def test_make_lazy():
    import os

    assert 'os' not in sys.modules
    os_mod = make_lazy('os')
    assert isinstance(os_mod, _LazyModuleMarker)
    assert isinstance(os_mod, ModuleType)
    assert 'os' in sys.modules
    assert os_mod.path is os.path
    assert os_mod.name is os.name



# Generated at 2022-06-14 06:21:46.597977
# Unit test for function make_lazy
def test_make_lazy():
    # Create a test module with function foo
    import os
    f = open('test_lazy_module.py', 'w')
    f.write('def foo():\n    pass')
    f.close()

    # Importing the test module should not load the file yet
    sys.modules['test_lazy_module'] = make_lazy('test_lazy_module')
    module = sys.modules['test_lazy_module']

    assert module.foo is None
    assert os.path.exists('test_lazy_module.pyc') is False

    # Now calling any function should load things up
    module.foo()
    assert module.foo is not None
    assert os.path.exists('test_lazy_module.pyc')

    # Now delete the module, so we can easily remove it

# Generated at 2022-06-14 06:21:52.466318
# Unit test for function make_lazy
def test_make_lazy():
    sys.modules['a.b.c'] = None

    make_lazy('a.b.c')

    assert isinstance(sys.modules['a.b.c'], _LazyModuleMarker)

    del sys.modules['a.b.c']



# Generated at 2022-06-14 06:22:01.712330
# Unit test for function make_lazy
def test_make_lazy():
    import sys

    modules = sys.modules
    mod = modules['sortedcollections.laziermodule']

    assert isinstance(mod, _LazyModuleMarker)
    assert mod.__getattribute__('__name__') == 'sortedcollections.laziermodule'
    assert mod.__getattribute__('__file__') == os.path.abspath(
        os.path.join(os.path.dirname(__file__),
                     'laziermodule.py'))

# Generated at 2022-06-14 06:22:08.738106
# Unit test for function make_lazy
def test_make_lazy():
    """
    unit tests that the function make_lazy works as expected.
    """
    module = make_lazy('random')
    import random
    import types
    # make sure the module is not loaded
    eq_(isinstance(random, types.ModuleType), True)
    # make sure module is imported
    eq_(isinstance(random.random(), float), True)
    # make sure that the module has been imported
    eq_(isinstance(random, types.ModuleType), True)

# Generated at 2022-06-14 06:22:20.553027
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    from mock import patch

    module_name = 'mock.test'

    if module_name in sys.modules:
        del sys.modules[module_name]

    # We patch out the import to confirm it never gets called.
    with patch('__builtin__.__import__') as import_mock:
        make_lazy(module_name)

        import_mock.assert_not_called()

        # Load the module, check it loaded and call again.
        sys.modules[module_name] = __import__ = object()

# Generated at 2022-06-14 06:22:28.959108
# Unit test for function make_lazy
def test_make_lazy():
    class MyException(Exception):
        pass

    try:
        make_lazy(__name__)
    except:
        pass
    else:
        raise MyException("make_lazy should not be run on the module it is defined in")

    try:
        make_lazy("foo")
        import foo
    except ImportError:
        pass
    else:
        raise MyException("Expected the module to not be imported")

    make_lazy("sys")
    assert isinstance(sys, _LazyModuleMarker)

    # This call should import the module
    sys.exit()

    assert not isinstance(sys, _LazyModuleMarker)

# Generated at 2022-06-14 06:22:46.238297
# Unit test for function make_lazy
def test_make_lazy():
    # Create a dummy module and import it.
    module_path = 'test_make_lazy'
    import_path = 'tests.test_lazy_module.%s' % module_path
    with open(os.path.join(os.path.dirname(__file__), module_path + '.py'), 'w') as f:
        f.write('a = 1')
    importlib.import_module(import_path)

    make_lazy(import_path)
    assert import_path in sys.modules
    assert 'a' not in sys.modules[import_path].__dict__

    # Load a value from the module.
    from . import test_make_lazy
    assert test_make_lazy.a == 1
    # It should now be in the module.

# Generated at 2022-06-14 06:22:53.844377
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    sys.modules['module'] = None
    module = sys.modules['module']
    assert module is None
    make_lazy('module')
    module = sys.modules['module']
    assert isinstance(module, _LazyModuleMarker)
    try:
        module.a
    except AttributeError:
        pass
    else:
        raise AssertionError('should have raised AttributeError')
    sys.modules['module'] = None
    del sys.modules['module']

# Generated at 2022-06-14 06:23:06.373619
# Unit test for function make_lazy
def test_make_lazy():
    global make_lazy

    class _VerifyLazyModule(object):
        def __init__(self):
            self.module = None

        def __call__(self, module_path):
            self.module = sys.modules[module_path]
            assert isinstance(self.module, _LazyModuleMarker)
            assert isinstance(self.module, ModuleType)
            make_lazy = None
            del self.module

    verify_lazy_module = _VerifyLazyModule()
    make_lazy = verify_lazy_module

    lazy_module = make_lazy('any_module')
    verify_lazy_module.module = lazy_module
    assert isinstance(lazy_module, _LazyModuleMarker)
    assert isinstance(lazy_module, ModuleType)

    del lazy

# Generated at 2022-06-14 06:23:16.381566
# Unit test for function make_lazy
def test_make_lazy():
    def _test_lazy(module_name):
        mod = __import__(module_name)
        make_lazy(module_name)
        assert mod is sys.modules[module_name]
        assert isinstance(sys.modules[module_name], _LazyModuleMarker)

        # `reload` has a check for object identity, so this is to check that
        # we don't accidentally break that behavior.
        reload(mod)

        # A simple check that the module was imported
        assert getattr(sys.modules[module_name], '__file__', None) is not None

    # Test 3 different modules to ensure we don't break reloading a module.
    _test_lazy('os')
    _test_lazy('threading')
    _test_lazy('random')

# Generated at 2022-06-14 06:23:24.303782
# Unit test for function make_lazy
def test_make_lazy():
    import os

    make_lazy('os')
    # Make sure we can access a value directly on the module
    assert os.pathsep == os.pathsep
    # Make sure the module is a lazy module
    assert isinstance(os, _LazyModuleMarker)
    # Make sure stuff that is not defined on the module raises
    # an AttributeError
    try:
        getattr(os, 'NOT_DEFINED')
    except AttributeError:
        pass
    # Make sure we can still access stuff directly on the module
    assert os.pathsep == os.pathsep
    # Make sure that the module's type is the same as the original
    # type of the module
    assert type(os) == ModuleType

if __name__ == '__main__':
    test_make_lazy()

# Generated at 2022-06-14 06:23:33.917734
# Unit test for function make_lazy
def test_make_lazy():
    # Create a dummy module within the 'test_lazy_loader' namespace to test.
    dummy_module = ModuleType('dummy_test_module')
    # Add something on the module.
    dummy_module.something = 1
    # Create a new module in the cache
    sys.modules['test_lazy_loader.dummy_test_module'] = dummy_module
    # Call make_lazy on it
    make_lazy('test_lazy_loader.dummy_test_module')
    # Should have Module for module.
    assert isinstance(sys.modules['test_lazy_loader.dummy_test_module'],
                      LazyModule)

# Generated at 2022-06-14 06:23:47.991875
# Unit test for function make_lazy
def test_make_lazy():

    def assert_lazy(path, mocked_value):
        # make a new scope
        result = NonLocal(None)

        make_lazy(path)

# Generated at 2022-06-14 06:23:59.771277
# Unit test for function make_lazy
def test_make_lazy():
    """
    Unit test to verify that make_lazy works.
    """

    def import_explicit_test():
        """
        Import a module and access an attribute so that it gets loaded.
        """
        make_lazy('tests.test_lazy')
        # The following importing should force the loading of the module
        assert isinstance(sys.modules['tests.test_lazy'], _LazyModuleMarker)
        assert not isinstance(sys.modules['tests.test_lazy'], ModuleType)
        sys.modules['tests.test_lazy'].test_make_lazy
        assert isinstance(sys.modules['tests.test_lazy'], ModuleType)

    def import_implicit_test():
        """
        Import a module
        """
        make_lazy('tests.test_lazy')

# Generated at 2022-06-14 06:24:09.050513
# Unit test for function make_lazy
def test_make_lazy():
    import pytest

    def test():
        from sentry.utils.imports import make_lazy

        make_lazy('django.conf')
        with pytest.raises(KeyError):
            from django.conf import settings

        from django.conf import __path__

        assert __path__

    test.__name__ = 'test'
    import sys
    test.__module__ = sys._getframe().f_globals.get('__name__')

    globals().pop('test')

# Generated at 2022-06-14 06:24:11.161355
# Unit test for function make_lazy
def test_make_lazy():
    make_lazy('test')

    import test
    assert isinstance(test, _LazyModuleMarker)

# Generated at 2022-06-14 06:24:19.825700
# Unit test for function make_lazy
def test_make_lazy():
    sys.modules['lazy_module'] = 'lazy_module'
    make_lazy('lazy_module')
    assert sys.modules['lazy_module'] is not None
    assert isinstance(sys.modules['lazy_module'], _LazyModuleMarker)
    assert not hasattr(sys.modules['lazy_module'], '__mro__')
    assert sys.modules['lazy_module'].__mro__ is not None
    assert hasattr(sys.modules['lazy_module'], '__getattribute__')
    assert getattr(sys.modules['lazy_module'], '__getattribute__') is not None
    assert not hasattr(sys.modules['lazy_module'], '__path__')
    assert sys.modules['lazy_module'].__path__ is not None



# Generated at 2022-06-14 06:24:26.122964
# Unit test for function make_lazy
def test_make_lazy():
    """
    Tests the function make_lazy
    """
    import sys
    sys.modules['a.b'] = object()
    make_lazy('a.b')
    from a.b import func1
    func1()
    make_lazy('a.b.c')
    from a.b.c import func2
    func2()



# Generated at 2022-06-14 06:24:33.970671
# Unit test for function make_lazy
def test_make_lazy():
    def _test_module(module_path):
        make_lazy(module_path)
        assert sys.modules[module_path] is not None
        assert isinstance(sys.modules[module_path], _LazyModuleMarker)
        return sys.modules[module_path]

    def _test_lazying(module_path, attr):
        mod = _test_module(module_path)

        with pytest.raises(AttributeError) as excinfo:
            getattr(mod, attr)
        assert 'has no attribute' in str(excinfo.value)

        with pytest.raises(AttributeError) as excinfo:
            getattr(mod, attr)
        assert 'has no attribute' in str(excinfo.value)

        assert sys.modules[module_path] is not None