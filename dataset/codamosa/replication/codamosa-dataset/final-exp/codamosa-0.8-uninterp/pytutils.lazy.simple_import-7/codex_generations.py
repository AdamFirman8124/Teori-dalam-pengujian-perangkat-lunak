

# Generated at 2022-06-14 06:14:46.044219
# Unit test for function make_lazy
def test_make_lazy():
    # import package to be lazy-loaded
    pkg_name = 'entropy.client.misc'
    make_lazy(pkg_name)

    # check if package is _LazyModuleMarker instance
    pkg = sys.modules[pkg_name]
    assert isinstance(pkg, _LazyModuleMarker)

    # check if we can import attributes without full import
    from entropy.client.misc import entropy_uri_to_package_id

    # check if the attribute is actually imported
    assert callable(entropy_uri_to_package_id)

    # remove pkg from sys.modules
    del sys.modules[pkg_name]
    # remove entro

# Generated at 2022-06-14 06:14:55.739613
# Unit test for function make_lazy
def test_make_lazy():
    test_mod = "sentry.test.test_lazy"
    module = sys.modules.get(test_mod)
    if module is not None:
        del sys.modules[test_mod]

    make_lazy(test_mod)

    assert sys.modules.get(test_mod) is not None
    assert isinstance(sys.modules[test_mod], _LazyModuleMarker)
    assert not hasattr(sys.modules[test_mod], "baz")

    import sentry.test.test_lazy
    assert isinstance(sys.modules[test_mod], ModuleType)
    assert hasattr(sentry.test.test_lazy, "baz")


if __name__ == "__main__":
    test_make_lazy()

# Generated at 2022-06-14 06:15:08.313287
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    import tempfile
    import shutil
    import os
    from types import ModuleType

    from nose.tools import assert_true, assert_false
    from nose.tools import assert_in, assert_not_in

    def _assert_isinstance_lazymodule(mod):
        """
        Check that 'mod' is not a LazyModule by directly comparing the mro of
        the instance.
        """
        assert_false(isinstance(mod, _LazyModuleMarker),
                     "Expected `isinstance` to fail.")
        assert_in(LazyModule, mod.__mro__(),
                  "Expected to find LazyModule in mro")


# Generated at 2022-06-14 06:15:14.615917
# Unit test for function make_lazy
def test_make_lazy():
    import random

    try:
        make_lazy('random')
        import random
    except ImportError:
        assert False, 'ImportError occurred. make_lazy is not working'
    else:
        assert isinstance(random, _LazyModuleMarker), 'random is not a lazy module.'
        assert random.random() == random.random()

# Generated at 2022-06-14 06:15:20.676004
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    from importlib import import_module
    from types import ModuleType

    make_lazy('six')

    assert isinstance(sys.modules['six'], ModuleType)
    assert not isinstance(sys.modules['six'], ImportError)

    six = import_module('six')
    assert isinstance(sys.modules['six'], six.LazyModule)

# Generated at 2022-06-14 06:15:33.471499
# Unit test for function make_lazy
def test_make_lazy():
    # test setup code
    # --------------

    module_path = "some.module"
    mock_module = MagicMock()
    mock_module.some_function.return_value = "some_result"
    mock_import = MagicMock()
    mock_import.return_value = mock_module
    with patch("__builtin__.__import__", mock_import):
        make_lazy(module_path)

    def get_module():
        return sys.modules[module_path]

    def get_some_function():
        return get_module().some_function()

    # tests
    # -----

    # lazy module is created
    assert isinstance(get_module(), _LazyModuleMarker)
    assert not mock_import.called  # lazy module not imported

    # accessing module attr triggers import

# Generated at 2022-06-14 06:15:37.818060
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    sys.modules['dummy'] = None
    make_lazy('dummy')
    assert isinstance(sys.modules['dummy'], _LazyModuleMarker)
    del sys.modules['dummy']


# Generated at 2022-06-14 06:15:48.872560
# Unit test for function make_lazy
def test_make_lazy():
    import random as _random  # import this so we know it exists.
    import sys

    def get_random():
        make_lazy('random')
        import random  # this should be a lazy import.
        return random

    random = get_random()
    assert sys.modules['random'] is not _random
    assert isinstance(random, ModuleType)

    # Now call a function off of random.
    # This should trigger the module to import itself.
    rand_int = random.randint(5, 10000)
    assert sys.modules['random'] is _random
    assert type(rand_int) is int

# Generated at 2022-06-14 06:15:59.021506
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    import test_make_lazy_module

    assert "test_make_lazy_module" not in sys.modules
    assert test_make_lazy_module.__name__ == "test_make_lazy_module"

    make_lazy("test_make_lazy_module")

    assert "test_make_lazy_module" in sys.modules
    mod = sys.modules['test_make_lazy_module']

    assert isinstance(mod, _LazyModuleMarker)
    assert mod.__name__ == "test_make_lazy_module"
    assert hasattr(mod, "VALUE")

    try:
        mod.NOT_LOADED
        assert False, "Should have thrown AttributeError"
    except AttributeError:
        pass  # Expected


# Generated at 2022-06-14 06:16:11.083983
# Unit test for function make_lazy
def test_make_lazy():
    _global = None

    def get_global():
        make_lazy('make_lazy_test_module')

        import make_lazy_test_module
        return make_lazy_test_module

    assert not isinstance(sys.modules['make_lazy_test_module'], NonLocal)

    # Check that we did not import immediately
    assert isinstance(sys.modules['make_lazy_test_module'], _LazyModuleMarker)

    _global = get_global()
    assert _global is sys.modules['make_lazy_test_module']

    assert 'my_var' in _global.__dict__
    assert 'my_var' in sys.modules['make_lazy_test_module'].__dict__

    # Check that the object is no longer a LazyModule

# Generated at 2022-06-14 06:16:25.559084
# Unit test for function make_lazy
def test_make_lazy():
    import os

    old_os = sys.modules['os']
    assert old_os is not None
    make_lazy('os')
    assert 'os' in sys.modules
    assert sys.modules['os'] is not old_os
    assert isinstance(sys.modules['os'], ModuleType)
    assert sys.modules['os'] is not None
    assert isinstance(sys.modules['os'], _LazyModuleMarker)

    # The module should be loaded when an attribute is accessed
    assert sys.modules['os'].curdir != ''
    assert sys.modules['os'] is old_os
    assert old_os.curdir != ''

    # Since the module was already loaded, reloading it should return it.
    make_lazy('os')
    assert sys.modules['os'] is old_os

   

# Generated at 2022-06-14 06:16:38.621442
# Unit test for function make_lazy
def test_make_lazy():
    """
    Test our lazy module loader.
    """
    import os

    # Remove our test module from sys.modules to simulate that it was never imported.
    try:
        sys.modules.pop('test_module')
    except KeyError:
        pass

    # Import the module and mark it as lazy.
    import test_module
    make_lazy('test_module')

    # Verify the module is not imported yet.
    assert os.path.basename(test_module.__file__) is None

    # Verify one of the attributes is a function.
    assert isinstance(test_module.fn, types.FunctionType)

    # Verify that it imported.
    assert os.path.basename(test_module.__file__) == 'test_module.py'

# Generated at 2022-06-14 06:16:48.381245
# Unit test for function make_lazy
def test_make_lazy():
    class Importer(object):
        """
        This class will keep track of what is imported.
        """
        _imported = []
        def find_module(self, fullname, path):
            """
            Keep track of what modules are attempted to be imported.
            """
            self._imported.append(fullname)
            return None

    importer = Importer()
    sys.meta_path.insert(0, importer)

    import mock
    import json
    assert importer._imported == ['mock', 'json']

    make_lazy('oh_no')
    import oh_no
    assert importer._imported == ['mock', 'json', 'oh_no']

    import oh_no2

# Generated at 2022-06-14 06:16:59.035983
# Unit test for function make_lazy
def test_make_lazy():
    """
    Testing the make_lazy function
    """
    # Test to make sure it sets something in sys.modules
    sys_module_list = ['sys_module_list', 'for_test_only']
    sys_module_list_lazy = 'sys_module_list_lazy'

    sys.modules[sys_module_list] = ['a', 'b', 'c']
    make_lazy(sys_module_list_lazy)

    assert sys_module_list in sys.modules

    # Test to make sure it sets a lazy class in sys.modules
    assert isinstance(sys.modules[sys_module_list_lazy], _LazyModuleMarker)

    # Test to make sure an attribute can be gotten from the lazy class
    lazy_module = sys.modules[sys_module_list_lazy]


# Generated at 2022-06-14 06:17:12.504009
# Unit test for function make_lazy
def test_make_lazy():
    def test_module_1():
        make_lazy('test_module_1')
        import test_module_1
        test_module_1.__name__
        test_module_1.__doc__
        assert isinstance(test_module_1, _LazyModuleMarker)

    def test_module_2():
        make_lazy('test_module_2')
        import test_module_2
        test_module_2.__name__
        test_module_2.__doc__
        assert isinstance(test_module_2, _LazyModuleMarker)

    def test_module_3():
        # Test the module is imported if not present in sys.modules
        make_lazy('test_module_3')
        sys.modules.pop('test_module_3')
        import test_module_

# Generated at 2022-06-14 06:17:23.739457
# Unit test for function make_lazy
def test_make_lazy():
    # Test with 'thread'
    thread = sys.modules['thread']
    thread_is_lazy = isinstance(thread, _LazyModuleMarker)
    assert not thread_is_lazy, \
        'before lazy loading, thread module is not lazy'
    # thread module will be removed from sys.modules and will be reloaded
    make_lazy('thread')
    thread = sys.modules['thread']
    thread_is_lazy = isinstance(thread, _LazyModuleMarker)
    assert thread_is_lazy, \
        'thread module is now lazy'
    # If a function is invoked lazily, it should be reloaded
    assert getattr(thread, 'Lock')
    thread_is_lazy = isinstance(thread, _LazyModuleMarker)

# Generated at 2022-06-14 06:17:32.414928
# Unit test for function make_lazy
def test_make_lazy():
    # Create a temporary module
    import tempfile
    module_path = tempfile.mkdtemp()
    mod_file = os.path.join(module_path, '__init__.py')
    with open(mod_file, 'w') as f:
        f.write("test_var = 'test'")
        f.flush()

    # Test with package name
    import_path = module_path.split(os.path.sep)[-1]
    make_lazy(import_path)
    import import_path

    import_path_mod = import_path.__dict__
    assert import_path_mod.get('test_var') == 'test'
    assert import_path_mod.get('__file__') == mod_file

    # Test with relative path
    import_path = module_path.split

# Generated at 2022-06-14 06:17:37.322662
# Unit test for function make_lazy
def test_make_lazy():
    import materialized.lazy
    import materialized
    # Check if `materialized.lazy` is lazy
    assert not hasattr(materialized, 'lazy')
    # This should trigger the lazy import
    assert hasattr(materialized.lazy, 'hmm')

# Generated at 2022-06-14 06:17:41.523144
# Unit test for function make_lazy
def test_make_lazy():
    make_lazy('test_module')
    sys.modules['test_module'].TEST = 'TEST'
    assert isinstance(sys.modules['test_module'], _LazyModuleMarker)
    assert sys.modules['test_module'].TEST == 'TEST'



# Generated at 2022-06-14 06:17:52.708166
# Unit test for function make_lazy
def test_make_lazy():
    # We need to manually add an entry to sys.modules, because
    # the import machinery will not pick up our LazyModule entry
    # as a valid module
    sys_modules_before = sys.modules.copy()

    module_path = 'test.test_module'
    make_lazy(module_path)

    assert sys_modules_before != sys.modules, \
                    'sys.modules has not changed after calling make_lazy'

    lazy_module = sys.modules['test.test_module']
    assert isinstance(lazy_module, _LazyModuleMarker), \
                    'sys.modules[%s] is not a LazyModule' % module_path
    assert isinstance(lazy_module, ModuleType), \
                    'sys.modules[%s] is not a ModuleType' % module_path

    #

# Generated at 2022-06-14 06:18:03.237153
# Unit test for function make_lazy
def test_make_lazy():
    # Test basic functionality
    make_lazy('foo')
    import foo
    assert foo
    assert foo.__name__ == 'foo'

    # Test lazy import
    make_lazy('foo.bar')
    assert foo
    assert foo.bar

    # Test isinstance
    assert isinstance(foo.bar, ModuleType)
    assert isinstance(foo.bar, _LazyModuleMarker)



# Generated at 2022-06-14 06:18:10.928196
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    # Find a module to use.
    module_name = 'os'
    module = sys.modules[module_name]

    # Make sure it's not already a lazy module.
    assert not isinstance(module, _LazyModuleMarker)

    # Make it lazy.
    make_lazy(module_name)

    # Make sure we get a module back when we import it.
    import os
    assert isinstance(os, ModuleType)

    # Make sure we can get an attribute back.
    assert os.path is not None

    # Make sure we can call a function on the module.
    assert os.getcwd() is not None

# Generated at 2022-06-14 06:18:22.548724
# Unit test for function make_lazy
def test_make_lazy():
    import test_lazy_module
    test_lazy_module.__lazy__ = True
    module_path = test_lazy_module.__name__

    make_lazy(module_path)

    sys_modules = sys.modules
    assert not sys_modules[module_path].__lazy__
    assert sys_modules[module_path].__name__ == 'test_lazy_module'

    # Verify our lazy module 'isinstance' of ModuleType
    assert isinstance(sys_modules[module_path], ModuleType)

    # Verify our lazy module is now 'isinstance' of _LazyModuleMarker
    assert isinstance(sys_modules[module_path], _LazyModuleMarker)

    del sys.modules[module_path]

# Generated at 2022-06-14 06:18:29.714077
# Unit test for function make_lazy
def test_make_lazy():
    """
    Test making a module lazy.
    """
    make_lazy('foo.bar')

    # We have to have a reference to the module here in order
    # to force it to be cached locally to pass the isinstance check.
    # Otherwise, we would just be testing against `LazyModule`
    # rather than `foo.bar`.
    import foo.bar

    # make sure it doesn't do an import
    # This should fail without `make_lazy`
    assert not hasattr(foo, 'baz')

    # Make sure it does work correctly, and that we can access the attributes.
    assert isinstance(foo.bar, _LazyModuleMarker)

    # Make sure we can do an import
    from foo.bar import baz

    assert foo.bar.baz == baz



# Generated at 2022-06-14 06:18:36.346296
# Unit test for function make_lazy
def test_make_lazy():
    make_lazy('socket')
    import socket
    assert isinstance(socket, _LazyModuleMarker)
    assert socket.gethostname() == 'localhost', 'should be able to use like normal after it has been touched'
    assert not isinstance(socket, _LazyModuleMarker), 'should no longer be a lazy module'

# Generated at 2022-06-14 06:18:45.950430
# Unit test for function make_lazy
def test_make_lazy():
    # Make sure it works for 1 level deep.
    make_lazy('dynamic_import.non_virtual')
    import dynamic_import.non_virtual

    assert 'virtual' in dir(dynamic_import.non_virtual)

    make_lazy('dynamic_import.non_virtual.virtual')
    import dynamic_import.non_virtual.virtual

    assert 'virtual' in dir(dynamic_import.non_virtual.virtual)

    assert isinstance(dynamic_import.non_virtual, _LazyModuleMarker)
    assert not isinstance(dynamic_import.non_virtual.virtual, _LazyModuleMarker)

if __name__ == '__main__':
    test_make_lazy()

# Generated at 2022-06-14 06:18:50.278142
# Unit test for function make_lazy
def test_make_lazy():
    """
    Tests make_lazy functionality
    """
    import select

    assert select.poll is not None

    make_lazy('select')

    assert isinstance(select, _LazyModuleMarker)
    assert select.poll is not None

# Generated at 2022-06-14 06:18:59.018068
# Unit test for function make_lazy
def test_make_lazy():
    sys.modules["mock_module"] = None
    make_lazy("mock_module")

    assert type(sys.modules["mock_module"]) == _LazyModuleMarker
    assert not hasattr(sys.modules["mock_module"], "__mro__")

    mock_module = sys.modules["mock_module"]
    assert mock_module is not None

    assert hasattr(mock_module, "__mro__")
    assert isinstance(mock_module, ModuleType)

    del sys.modules["mock_module"]



# Generated at 2022-06-14 06:19:12.684105
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    import os

    foo = NonLocal(None)

    class MyModule(object):
        """
        A fake module.
        """
        def __getattribute__(self, attr):
            if foo.value is None:
                foo.value = True
            else:
                foo.value = False

            return getattr(os, attr)

    # Stash the original module
    orig_sys_modules = sys.modules.copy()

    # "import" our fake os module
    sys.modules = {
        'os': MyModule()
    }

    # "import" the fake os module
    import os

    assert(foo.value is None), 'We should have not invoked __getattribute__ on the module yet'

    # "import" the fake os module
    import os


# Generated at 2022-06-14 06:19:24.476195
# Unit test for function make_lazy
def test_make_lazy():
    make_lazy('foo.bar')
    import foo.bar
    assert isinstance(foo.bar, _LazyModuleMarker)


try:
    from django.core.management.commands.runserver import naiveip_re
except ImportError:
    # We are running Django 1.2.x, so we can't use
    # django.core.management.commands.runserver.naiveip_re.
    # So copy/paste the logic into this module.
    naiveip_re = re.compile('^(\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3})$')



# Generated at 2022-06-14 06:19:35.221658
# Unit test for function make_lazy
def test_make_lazy():
    import math

    make_lazy('math')
    assert isinstance(math, _LazyModuleMarker)
    assert hasattr(math, 'sin')
    assert type(math).__name__ == 'module'
    assert math.isnan(math.sin(float('inf')))
    assert math.pi == 3.141592653589793



# Generated at 2022-06-14 06:19:46.354132
# Unit test for function make_lazy
def test_make_lazy():
    import os
    import sys
    try:
        del sys.modules['testmakelazy']
    except:
        pass
    import testmakelazy
    assert isinstance(testmakelazy, (ModuleType, _LazyModuleMarker))
    try:
        variable = testmakelazy.test_variable
    except:
        pass

    assert variable == 'test variable value'
    assert isinstance(testmakelazy, (ModuleType, _LazyModuleMarker))
    sys.modules.pop('testmakelazy')
    import testmakelazy
    assert isinstance(testmakelazy, _LazyModuleMarker)
    try:
        variable = testmakelazy.test_variable
    except:
        pass

    assert variable == 'test variable value'

# Generated at 2022-06-14 06:19:53.932403
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    import os
    make_lazy('os')
    assert(isinstance(sys.modules['os'], _LazyModuleMarker))
    assert(sys.modules['os'] is not os)
    assert(sys.modules['os'].path is os.path)
    assert(isinstance(sys.modules['os'].path, _LazyModuleMarker))

# Generated at 2022-06-14 06:20:04.669668
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    make_lazy('sys')
    a = sys
    assert not hasattr(sys.modules['sys'], 'modules')

    # Assert that sys is now our LazyModule type
    assert type(sys.modules['sys']) == type(sys.modules['lazy'])

    make_lazy('abc')
    assert not hasattr(sys.modules['abc'], 'modules')

    assert type(sys.modules['sys']) == type(sys.modules['lazy'])

    # Try getting an attribute off of sys.
    sys.version

    assert hasattr(sys.modules['sys'], 'version')
    assert type(sys.modules['sys']) != type(sys.modules['lazy'])

    # Try with a module that doesn't exist.
    make_lazy('sdasdf')


# Generated at 2022-06-14 06:20:18.064622
# Unit test for function make_lazy
def test_make_lazy():
    module_path = 'make_lazy_test_'
    make_lazy(module_path)

    lazy_module = sys.modules[module_path]

    assert isinstance(lazy_module, _LazyModuleMarker)
    assert not hasattr(lazy_module, 'a')

    class InnerClass(object):
        pass

    InnerClass.a = 5
    setattr(sys.modules[module_path], 'InnerClass', InnerClass)

    assert hasattr(lazy_module, 'a')
    assert lazy_module.a == 5
    assert lazy_module.InnerClass.a == 5

    del sys.modules[module_path]

    make_lazy(module_path)

    lazy_module = sys.modules[module_path]


# Generated at 2022-06-14 06:20:29.331127
# Unit test for function make_lazy
def test_make_lazy():

    def does_not_exist():
        """
        This is a function that does not exist in the global namespace.
        """
        pass

    # Make sure that the function does not exist
    try:
        does_not_exist()
        raise ValueError("Expected error trying to call undefined function.")
    except NameError:
        pass

    # Use make_lazy to create a lazy module
    make_lazy(__name__)

    # Now it should still not exist
    try:
        does_not_exist()
        raise ValueError("Expected error trying to call undefined function.")
    except NameError:
        pass

    # But now it should import the module
    does_not_exist()

# Generated at 2022-06-14 06:20:39.665166
# Unit test for function make_lazy
def test_make_lazy():
    """
    Test that the make_lazy function properly lazily loads a module.
    """
    test_module_path = 'tests.test_extras.test_lazy_module'

    # Verify that the module does not exist in `sys.modules`
    assert test_module_path not in sys.modules

    # Now make the module be lazy
    make_lazy(test_module_path)

    # Verify that the module does exist in `sys.modules` but is our
    # LazyModule instance
    assert isinstance(sys.modules[test_module_path], _LazyModuleMarker)

    # Verify that we can do an import of the module
    import tests.test_extras.test_lazy_module
    assert tests.test_extras.test_lazy_module is not None

    # Verify that the module

# Generated at 2022-06-14 06:20:51.979626
# Unit test for function make_lazy
def test_make_lazy():
    make_lazy(__name__ + '.test_mod1')
    mod = sys.modules[__name__ + '.test_mod1']
    assert_true(isinstance(mod, _LazyModuleMarker))

    # The module should not have been imported yet
    assert_true('test_mod1' not in sys.modules)

    # Trigger the import by accessing an attribute
    assert_equal(mod.a, 'a')
    assert_true('test_mod1' in sys.modules)


from test_mod1 import a, b, c  # noqa
make_lazy(__name__ + '.test_mod2')
from test_mod2 import d, e, f  # noqa


# Generated at 2022-06-14 06:21:02.920090
# Unit test for function make_lazy
def test_make_lazy():
    # Test case: make_lazy('test_make_lazy')
    make_lazy('test_make_lazy')
    import test_make_lazy
    assert isinstance(test_make_lazy, _LazyModuleMarker)

    # Test case: test_make_lazy.foo
    assert hasattr(test_make_lazy, 'foo')
    assert test_make_lazy.foo == "foo"

    # Test case: test_make_lazy.bar
    assert hasattr(test_make_lazy, 'bar')
    assert test_make_lazy.bar == "bar"

    # We should be able to call un-explored functions
    assert test_make_lazy.call_other_function() == "other"

# Generated at 2022-06-14 06:21:06.711513
# Unit test for function make_lazy
def test_make_lazy():
    import django
    django.__name__ = 'django'
    make_lazy('django')
    assert isinstance(django, _LazyModuleMarker)
    django.__getattribute__('OK')
    assert not isinstance(django, _LazyModuleMarker)
    assert django.VERSION[0] == 1
    django.__getattribute__('OK')
    assert django.VERSION[0] == 1

# Generated at 2022-06-14 06:21:22.933255
# Unit test for function make_lazy
def test_make_lazy():
    try:
        sys.modules.pop('foo')
    except KeyError:
        pass

    make_lazy('foo')
    assert 'foo' not in sys.modules

    m = __import__('foo')
    assert 'foo' in sys.modules

# Generated at 2022-06-14 06:21:34.157449
# Unit test for function make_lazy
def test_make_lazy():
    """
    Unit test for function make_lazy
    """
    import sys
    import os
    import tempfile
    dir_path = tempfile.mkdtemp()
    try:
        with open(os.path.join(dir_path, 'test.py'), 'w') as f:
            f.write("a = 1; b = 2; c = 3; d = 4; e = 5; f = 6; g = 7;")
        sys.path.append(dir_path)
        
        import test
        make_lazy('test')
        assert test.f == 6, "test.f should be 6"
        assert 'make_lazy' in dir(test), "make_lazy should be imported in test"
    finally:
        sys.path.remove(dir_path)
        shutil.rmtree

# Generated at 2022-06-14 06:21:42.733954
# Unit test for function make_lazy
def test_make_lazy():
    import os, sys
    from types import ModuleType

    test_mod = 'lazy_test'
    sys.modules[test_mod] = 'Test module'
    make_lazy(test_mod)


# Generated at 2022-06-14 06:21:50.057919
# Unit test for function make_lazy
def test_make_lazy():
    """
    Test the lazy module loading.
    """
    original_sys_modules = sys.modules.copy()  # copy to snapshot
    try:
        make_lazy('six')
        sys_six = sys.modules['six']
        sys_six.add_metaclass  # trigger the import
        assert isinstance(sys.modules['six'], ModuleType)
    finally:
        # restore sys.modules
        sys.modules = original_sys_modules

# Generated at 2022-06-14 06:21:58.944945
# Unit test for function make_lazy
def test_make_lazy():
    import os

    make_lazy('os')

    assert isinstance(os, _LazyModuleMarker)
    assert isinstance(os, ModuleType)

    try:
        import os.path
    except ImportError:
        pass
    else:
        raise AssertionError('os.path was not imported')

    os.path.join('a', 'b', 'c')
    import os.path

    assert isinstance(os.path, ModuleType)
    assert not isinstance(os.path, _LazyModuleMarker)

# Generated at 2022-06-14 06:22:09.819406
# Unit test for function make_lazy
def test_make_lazy():
    """
    Check the simple use case of make_lazy
    """
    import sys
    import os

    old_path = list(sys.path)
    old_modules = sys.modules.copy()


# Generated at 2022-06-14 06:22:20.564929
# Unit test for function make_lazy
def test_make_lazy():
    def test_module_a():
        assert sys.modules['lazy_module.module_a'] is None

        import lazy_module.module_a

        assert 'module_a' in sys.modules
        assert sys.modules['lazy_module.module_a'] is not None

    def test_module_b():
        assert sys.modules['lazy_module.module_b'] is None

        import lazy_module.module_b

        assert 'module_b' in sys.modules
        assert sys.modules['lazy_module.module_b'] is not None

    def test_module_c():
        assert sys.modules['lazy_module.module_c'] is None

        import lazy_module.module_c

        assert 'module_c' in sys.modules

# Generated at 2022-06-14 06:22:30.953949
# Unit test for function make_lazy
def test_make_lazy():
    mod = LazyModule()
    mod.__name__ = 'lazy_module'
    mod.__package__ = 'lazy_package'
    make_lazy(mod.__name__)
    lazy_module = sys.modules[mod.__name__]
    assert isinstance(lazy_module, LazyModule)
    assert lazy_module.__package__ == mod.__package__
    assert lazy_module.__name__ == mod.__name__
    # Force import of the real module and make sure it is present in sys.modules
    lazy_module.new_attribute = 'test attribute'
    lazy_module = sys.modules[mod.__name__]
    assert not isinstance(lazy_module, LazyModule)
    assert hasattr(lazy_module, 'new_attribute')

# Import lazy modules by

# Generated at 2022-06-14 06:22:37.161529
# Unit test for function make_lazy
def test_make_lazy():
    make_lazy('test.lazy_opt')

    import test.lazy_opt
    assert isinstance(test.lazy_opt, _LazyModuleMarker)
    assert not hasattr(test.lazy_opt, 'x')

    assert test.lazy_opt.x == 2
    assert isinstance(test.lazy_opt, _LazyModuleMarker)
    assert hasattr(test.lazy_opt, 'x')

# Generated at 2022-06-14 06:22:41.334509
# Unit test for function make_lazy
def test_make_lazy():
    import json

    make_lazy('json')
    assert isinstance(json, _LazyModuleMarker)
    try:
        assert json.dumps('test string') == '"test string"'
        assert isinstance(json, ModuleType)
    except AttributeError:
        pytest.fail('AttributeError thrown because Module is lazy')



# Generated at 2022-06-14 06:22:58.268215
# Unit test for function make_lazy
def test_make_lazy():
    """
    Simple unit test.
    """
    module = 'make_lazy'
    make_lazy(module)

    # The module should not be loaded yet.
    assert module in sys.modules
    assert isinstance(sys.modules[module], _LazyModuleMarker)

    # Lets import it again to ensure it doesn't get loaded twice.
    import_module(module)

    # The module should be loaded now.
    assert isinstance(sys.modules[module], ModuleType)

# Generated at 2022-06-14 06:23:01.928920
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    import os

    make_lazy('os')

    assert isinstance(sys.modules['os'], _LazyModuleMarker)

    assert sys.modules['os'] is not os

# Generated at 2022-06-14 06:23:06.962352
# Unit test for function make_lazy
def test_make_lazy():
    import tempfile
    temp_dir = tempfile.gettempdir()
    filename = tempfile.mkstemp(
        prefix="test_make_lazy", suffix=".py", dir=temp_dir)[1]
    f = open(filename, 'w')

# Generated at 2022-06-14 06:23:16.981419
# Unit test for function make_lazy
def test_make_lazy():
    # Check that the module doesn't get imported if we don't try to see any of
    # it's variables.
    # Modules can't be added after they've been removed from the sys.modules
    # dictionary, so we must define the test module in another file.
    test_mod_file = 'foo/bar.py'
    test_mod_path = 'foo.bar'
    with open(test_mod_file, 'w') as f:
        f.write('def test():\n')
        f.write('  assert False')
    try:
        make_lazy(test_mod_path)
        import sys
        assert test_mod_path not in sys.modules
    finally:
        os.unlink(test_mod_file)
    # Bias the system to look at the test module's definition.
    # This

# Generated at 2022-06-14 06:23:22.033215
# Unit test for function make_lazy
def test_make_lazy():
    make_lazy('test.test_make_lazy')
    from test import test_make_lazy as mod
    # Note that we are using the lazy version
    assert isinstance(mod, _LazyModuleMarker), "%s is not a lazy module" % mod
    assert mod.__name__ is 'test.test_make_lazy'
    assert mod.__file__.endswith('test_make_lazy.pyc')



# Generated at 2022-06-14 06:23:30.431145
# Unit test for function make_lazy
def test_make_lazy():
    """
    Tests the make_lazy function.
    """
    import os

    # Test that lazy loading works in the first place
    make_lazy('os')
    assert isinstance(os, _LazyModuleMarker)

    # Test that lazy loading works for submodules
    make_lazy('os.path')
    assert isinstance(os.path, _LazyModuleMarker)

    # Test that lazy loading works for a module which requires arguments
    import struct
    make_lazy('struct')
    assert isinstance(struct, _LazyModuleMarker)
    struct.pack('i', 5)

# Generated at 2022-06-14 06:23:38.773319
# Unit test for function make_lazy
def test_make_lazy():
    from configparser import SafeConfigParser

    # We won't actually use the SafeConfigParser module
    # so we can import it safely
    make_lazy('configparser')

    # We should be able to import the module safely
    import configparser

    # The module should not have been imported yet
    assert isinstance(configparser, _LazyModuleMarker)

    # Loading the module's attributes should work
    assert configparser.version == SafeConfigParser.__version__

    # The module should have been imported
    assert not isinstance(configparser, _LazyModuleMarker)

# Generated at 2022-06-14 06:23:43.709380
# Unit test for function make_lazy
def test_make_lazy():
    module_path = 'weighted_trie.tests'
    make_lazy(module_path)
    assert module_path in sys.modules
    assert isinstance(sys.modules[module_path], _LazyModuleMarker)
    assert 'tests' not in sys.modules

# Generated at 2022-06-14 06:23:57.448416
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    import os
    import tempfile
    from types import ModuleType
    from cluster_pack.utils.lazy_module import make_lazy, _LazyModuleMarker

    # create a temp module to work with
    fd, path = tempfile.mkstemp(suffix='.py',
                                prefix='clusterpack_lazymodule_',
                                dir=tempfile.gettempdir(),
                                text=True)

    # define the test module
    f = os.fdopen(fd, 'w')
    f.write('foo = "bar"')
    f.flush()
    f.close()

    # make it lazy
    make_lazy(path)

    # test that it's lazy
    sys_modules = sys.modules
    test_module = sys_modules[path]

# Generated at 2022-06-14 06:24:07.894381
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    import os
    import tempfile
    import unittest

    class TestLazy(unittest.TestCase):
        def test_make_lazy(self):
            sys.modules.pop('make_lazy.test_module', None)

            # Create temporary file
            test_file = tempfile.NamedTemporaryFile(delete=False)
            test_file.close()

            # Create test file with attr "test"
            with open(test_file.name, 'w') as tf:
                tf.write("test = 'test'")

            module_name = 'test_module'
            module_path = os.path.join(test_file.name)
            module = sys.modules.get(module_path)

            # Test lazy importation
            make_lazy(module_path)


# Generated at 2022-06-14 06:24:30.861226
# Unit test for function make_lazy
def test_make_lazy():
    """
    We have a basic module that we can test against, look at the
    test_mod.py file.
    """
    # Make sure that our module isn't imported
    import test_mod
    assert isinstance(test_mod, _LazyModuleMarker)

    # Make sure our module has the attribute we want
    assert test_mod.A == 5

    # Make sure it doesn't really exist
    assert not hasattr(sys.modules[__name__], 'test_mod')

    # Make sure that if we try to access one of the attributes
    # it will import the module
    assert hasattr(sys.modules['test_mod'], 'A')


if __name__ == "__main__":
    # If we run this file we will run the test
    test_make_lazy()

# Generated at 2022-06-14 06:24:37.781307
# Unit test for function make_lazy
def test_make_lazy():
    mod_path = 'test_module'

    @make_lazy(mod_path)
    def test_module():
        import math
        return math.pi

    assert sys.modules[mod_path] is not None
    assert sys.modules[mod_path].pi == test_module.pi


if __name__ == '__main__':
    test_make_lazy()