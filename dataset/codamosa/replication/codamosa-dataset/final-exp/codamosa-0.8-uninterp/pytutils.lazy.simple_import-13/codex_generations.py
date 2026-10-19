

# Generated at 2022-06-14 06:14:49.112510
# Unit test for function make_lazy
def test_make_lazy():
    import math
    import os
    # make sure the tests run in the path they were written in
    this_dir = os.path.dirname(os.path.realpath(__file__))
    sys.path.append(this_dir)

    # Test that we don't load the module twice
    lazy_module_count = [0]

    def lazy_module():
        lazy_module_count[0] += 1
        return 1

    # Lazy load a module that is already in sys.modules.
    mod = sys.modules.setdefault('lazy_module', lazy_module)
    make_lazy('lazy_module')

    print(sys.modules)
    print(lazy_module_count)
    assert sys.modules.__contains__('lazy_module')
    assert lazy_module_count[0]

# Generated at 2022-06-14 06:14:53.537972
# Unit test for function make_lazy
def test_make_lazy():
    sys.modules['b'] = None
    make_lazy('b')
    assert isinstance(sys.modules['b'], _LazyModuleMarker)
    assert sys.modules['b'].__name__ == 'b'
    del sys.modules['b']

# Generated at 2022-06-14 06:15:06.725235
# Unit test for function make_lazy
def test_make_lazy():
    import mock

    from splunk_instrumentation.module_utils.loader_lazy import make_lazy
    from splunk_instrumentation.module_utils.loader_lazy import get_lazy_modules

    class Foo(object):
        pass

    @mock.patch('splunk_instrumentation.module_utils.loader_lazy.sys.modules')
    def test(mock_sys_modules):
        module_name = 'foomodule'
        module_path = 'splunk_instrumentation.module_utils.loader_lazy.foomodule'
        mock_sys_modules.__contains__.return_value = False
        make_lazy(module_path)
        mock_sys_modules[module_path]

        lazy_module = mock_sys_modules[module_path]


# Generated at 2022-06-14 06:15:19.590422
# Unit test for function make_lazy
def test_make_lazy():
    """
    Tests the make_lazy method of the lazy_module.py
    """
    try:
        import edx.analytics.tasks.tests.test_utils.lazy_module as lazy_module
    except ImportError:
        sys.stderr.write("Please run the tests from the root folder so the python path is set.")

    lazy_module.make_lazy(
        "edx.analytics.tasks.tests.test_utils.lazy_module.sample_module"
    )
    # pylint: disable=import-outside-toplevel
    from edx.analytics.tasks.tests.test_utils.lazy_module.sample_module import SampleModule
    # pylint: enable=import-outside-toplevel


# Generated at 2022-06-14 06:15:29.023162
# Unit test for function make_lazy
def test_make_lazy():
    """
    Unit test for function make_lazy
    """
    #pylint: disable=no-member
    import sys
    import xbmcgui
    assert 'xbmcgui' in sys.modules
    xbmcgui
    assert 'xbmcgui' in sys.modules
    assert isinstance(sys.modules['xbmcgui'], xbmcgui.__class__)
    import lazytest
    assert 'lazytest' in sys.modules
    assert isinstance(sys.modules['lazytest'], lazytest.__class__)
    lazytest
    assert 'lazytest' in sys.modules
    assert isinstance(sys.modules['lazytest'], lazytest.__class__)
    make_lazy('lazytest')
    assert 'lazytest' in sys.modules

# Generated at 2022-06-14 06:15:33.954394
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    import pytest
    module_path = 'django.conf.urls'
    make_lazy(module_path)
    assert isinstance(sys.modules[module_path], _LazyModuleMarker)

# Generated at 2022-06-14 06:15:44.229836
# Unit test for function make_lazy
def test_make_lazy():
    """
    Unit tests for make_lazy function
    """

    # unload the system module (if loaded)
    import sys
    if 'test_make_lazy' in sys.modules:
        del sys.modules['test_make_lazy']

    # test1: no exception while loading the test module
    try:
        make_lazy('test_make_lazy')
    except:
        assert False

    # test2: module is not loaded to the module list
    assert 'test_make_lazy' not in sys.modules

    # test3: get the module, and check if it's loaded
    import test_make_lazy
    assert 'test_make_lazy' in sys.modules

    # test4: module is loaded, should be able to call functions

# Generated at 2022-06-14 06:15:48.400813
# Unit test for function make_lazy
def test_make_lazy():
    import os
    import pdb

    # Create a test module file

# Generated at 2022-06-14 06:15:57.464796
# Unit test for function make_lazy
def test_make_lazy():
    """
    Validate that the make_lazy function works
    """
    # Make sure we can do `import a`
    module_path = 'a'
    make_lazy(module_path)
    mod = __import__(module_path, fromlist=['a'])

    assert isinstance(mod, _LazyModuleMarker)
    assert not hasattr(mod, 'a')

    # Try accessing an attribute on the module and importing should succeed.
    mod.a
    assert hasattr(mod, 'a')


if __name__ == '__main__':
    test_make_lazy()

# Generated at 2022-06-14 06:16:09.732265
# Unit test for function make_lazy
def test_make_lazy():
    import time

    class JimBean(object):
        """
        A class that takes a long time to initialize.
        """
        @classmethod
        def init(cls):
            time.sleep(3)
            cls.yes = True


    # First make sure that making it a lazy import doesn't
    # actually import the module.
    make_lazy('tests.test_lazy')

# Generated at 2022-06-14 06:16:19.188086
# Unit test for function make_lazy
def test_make_lazy():
    # A fake module for testing
    assert 'fake_module' not in sys.modules

    class FakeModule(ModuleType):
        pass

    make_lazy('fake_module')
    assert 'fake_module' in sys.modules
    assert isinstance(sys.modules['fake_module'], _LazyModuleMarker)

    # Check that the module is not loaded
    assert not isinstance(sys.modules['fake_module'], ModuleType)

    # Remove the fake module
    del sys.modules['fake_module']



# Generated at 2022-06-14 06:16:23.250167
# Unit test for function make_lazy
def test_make_lazy():
    """
    Unit test for function make_lazy
    """
    make_lazy('test_lazy_module')

    from test_lazy_module import test

    assert isinstance(test, int)
    assert test == 1

# Generated at 2022-06-14 06:16:29.746955
# Unit test for function make_lazy
def test_make_lazy():
    """
    Test that the make_lazy function works.
    """
    mod_name = 'sklearn.utils._testing.lazy_module'
    make_lazy(mod_name)
    mod = sys.modules[mod_name]
    assert isinstance(mod, _LazyModuleMarker)
    # This should not have been imported
    assert hasattr(mod, 'LAZY_MESSAGE')
    assert getattr(mod, 'LAZY_MESSAGE') == 'I am lazy'

# Generated at 2022-06-14 06:16:39.176335
# Unit test for function make_lazy
def test_make_lazy():
    """
    Test to ensure make_lazy works as expected
    """
    import sys

    __name__ = sys._getframe().f_code.co_name

    module_path = __name__ + '_test'
    make_lazy(module_path)
    # The module should not be imported
    assert module_path not in sys.modules

    # when a member is accessed, the module should be imported
    from importlib import import_module
    assert module_path not in sys.modules
    import_module(module_path)
    assert module_path in sys.modules



# Generated at 2022-06-14 06:16:48.555430
# Unit test for function make_lazy
def test_make_lazy():
    """
    Validate that make_lazy generates the correct object.
    """
    import test_lazy  # pylint: disable=import-error, unused-variable
    # This merely needs to import a file in the tests directory, and
    # validate that it doesn't show up in the sys.modules
    from pytest import raises
    with raises(KeyError):
        # If the module is not loaded, we should raise a KeyError.
        sys.modules['test_lazy']
    # import test_lazy
    assert not isinstance(test_lazy, _LazyModuleMarker)
    # We should verify that we are not a normal module.
    assert hasattr(test_lazy, 'test_item')
    # We should actually load the module after a getattr.

# Generated at 2022-06-14 06:16:57.799072
# Unit test for function make_lazy
def test_make_lazy():

    def run_module(unloaded_module):
        module = __import__(unloaded_module)
        assert(not isinstance(module, _LazyModuleMarker))
        instance = module.MyClass()
        assert(instance.mystring == 'lazy')

    def lazy_module(unloaded_module):
        module = __import__(unloaded_module)
        assert(isinstance(module, _LazyModuleMarker))
        instance = module.MyClass()
        assert(instance.mystring == 'lazy')

    # Create a module with a class that defines some variable
    module_path = 'tests.dummy_module'

# Generated at 2022-06-14 06:17:03.683268
# Unit test for function make_lazy
def test_make_lazy():
    # Use temp module name to work around cpython issue:
    # http://bugs.python.org/issue18846
    import sys
    import tempfile
    mod_name = next(tempfile._get_candidate_names())
    sys.modules[mod_name] = None
    module = sys.modules[mod_name]
    make_lazy(mod_name)
    assert isinstance(module, _LazyModuleMarker)
    assert module.__name__ == mod_name
    assert module.__doc__ is None
    # This will trigger module to be imported
    assert module.__name__ == mod_name
    del sys.modules[mod_name]



# Generated at 2022-06-14 06:17:11.374759
# Unit test for function make_lazy
def test_make_lazy():
    class TestMod(object):
        a = 'a'

    sys.modules['test_make_lazy'] = TestMod()
    make_lazy('test_make_lazy')

    assert TestMod.a == 'a'  # Make sure we haven't imported yet

    assert sys.modules['test_make_lazy'].a == 'a'  # Now we import
    assert isinstance(sys.modules['test_make_lazy'], type)

# Generated at 2022-06-14 06:17:16.084014
# Unit test for function make_lazy
def test_make_lazy():
    """
    Ensure that the function make_lazy works.
    """
    sys.modules['lazy_module'] = None
    make_lazy('lazy_module')
    import lazy_module
    # The import will fail, if lazy_module is not a lazy module.
    assert isinstance(lazy_module, _LazyModuleMarker)
    del sys.modules['lazy_module']

# Generated at 2022-06-14 06:17:30.300388
# Unit test for function make_lazy
def test_make_lazy():
    if 'test_lazy_module' in sys.modules:
        del sys.modules['test_lazy_module']

    make_lazy('test_lazy_module')
    assert isinstance(sys.modules['test_lazy_module'], ModuleType)
    assert isinstance(sys.modules['test_lazy_module'], _LazyModuleMarker)
    assert not hasattr(sys.modules['test_lazy_module'], 'attribute')
    # Should have been imported at this point
    a = sys.modules['test_lazy_module'].attribute
    assert hasattr(sys.modules['test_lazy_module'], 'attribute')
    assert sys.modules['test_lazy_module'].attribute == a
    import test_lazy_module

# Generated at 2022-06-14 06:17:46.458463
# Unit test for function make_lazy
def test_make_lazy():
    import os
    module_path = 'test.test_lazy_module'
    module_path_not_exists = 'test.test_not_exists'
    assert module_path not in sys.modules
    assert module_path_not_exists not in sys.modules

    assert make_lazy(module_path) is None

    mm = sys.modules[module_path]
    assert isinstance(mm, _LazyModuleMarker)
    mm.__name__ == module_path

    assert make_lazy(module_path_not_exists) is None
    nn = sys.modules[module_path_not_exists]
    assert isinstance(nn, _LazyModuleMarker)
    assert nn.__name__ == module_path_not_exists

    assert mm.__name__ == module

# Generated at 2022-06-14 06:17:54.637281
# Unit test for function make_lazy
def test_make_lazy():
    test_module_path = 'import_lazy_test_module'
    assert test_module_path not in sys.modules
    assert make_lazy(test_module_path)
    assert test_module_path in sys.modules

    test_module = sys.modules[test_module_path]
    assert test_module != None

    assert test_module_path + '.FOO' in sys.modules
    assert sys.modules[test_module_path + '.FOO'] != None

    assert isinstance(test_module, _LazyModuleMarker)
    assert test_module.value == None
    
    assert test_module.FOO.value == None
    assert test_module.FOO.__name__ == test_module_path + '.FOO'
    assert test_module.FOO.BAR == "test"


# Generated at 2022-06-14 06:18:02.050649
# Unit test for function make_lazy
def test_make_lazy():
    mod = 'a'
    sys.modules[mod] = []

    # Put the module into sys.modules so that it can be imported
    make_lazy(mod)

    # Should be a 'LazyModule'
    assert isinstance(sys.modules[mod], _LazyModuleMarker)

    # Get the attribute '__name__' off the module
    assert sys.modules[mod].__name__ == 'a'

# Generated at 2022-06-14 06:18:10.214986
# Unit test for function make_lazy
def test_make_lazy():
    """
    A make_lazy test to ensure functionality.
    """
    class Module(object):
        @staticmethod
        def a():
            """
            Our module's importable subject
            """
            return 1

    test_module_path = 'test_make_lazy_test_import'
    sys.modules[test_module_path] = Module
    make_lazy(test_module_path)

    m = sys.modules[test_module_path]
    assert isinstance(m, _LazyModuleMarker)
    assert m.a() == 1

# Generated at 2022-06-14 06:18:23.000789
# Unit test for function make_lazy
def test_make_lazy():
    # The module that we will use in the tests.
    module_path = 'test_lazy_module'
    module_name = 'test_lazy_module.lazy_mod'

    # Create the module.
    tmp_dir = tempfile.mkdtemp()
    module_file = os.path.join(tmp_dir, '__init__.py')

    with open(module_file, 'w') as fp:
        fp.write('attr = 1')

    sys.path.append(tmp_dir)

    # Our lazy module should actually be a LazyModule.
    assert isinstance(sys.modules[module_path], _LazyModuleMarker)

    # Should not be able to import the module.
    with pytest.raises(ImportError):
        __import__(module_name)

    #

# Generated at 2022-06-14 06:18:28.866290
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    sys.modules['lazy_test'] = True  # `test_make_lazy` may have already been imported
    make_lazy('lazy_test')
    lazy_test = sys.modules['lazy_test']
    assert lazy_test.__class__.__name__ == 'LazyModule'
    assert isinstance(lazy_test, _LazyModuleMarker)
    assert 'VERSION' not in sys.modules
    assert lazy_test.VERSION == '0.0.1'
    assert 'VERSION' in sys.modules
    del sys.modules['lazy_test']



# Generated at 2022-06-14 06:18:42.142414
# Unit test for function make_lazy
def test_make_lazy():
    """
    Tests that make_lazy() works as expected.
    """
    import os
    assert not hasattr(os, 'is_there_god')

    # Mark os as lazy such that everything in os will be imported lazily.
    make_lazy('os')
    assert isinstance(os, _LazyModuleMarker)

    # Force import the tempfile module to make sure os module is truly lazy.
    import tempfile

    # But os.path should now exist, so we should be able to do the following.
    import os.path

    # Even though we haven't access the os module, we are able to access the os.path
    # object directly. This should be fine.
    assert isinstance(os.path, ModuleType)

    # But when we access other objects in the os module, it will be loaded at that time.


# Generated at 2022-06-14 06:18:55.246171
# Unit test for function make_lazy
def test_make_lazy():
    _loaded = False
    make_lazy("my_module")

    class MyTestModule(object):
        def __init__(self):
            global _loaded
            _loaded = True

        @property
        def property_one(self):
            return True

        @property
        def property_two(self):
            return "string"

    sys.modules["my_module"] = MyTestModule()

    my_module = __import__("my_module")

    assert isinstance(my_module, _LazyModuleMarker)
    assert not _loaded

    assert my_module.property_one

    # Lazy module gets replaced with real module
    assert isinstance(my_module, MyTestModule)
    assert _loaded

    assert my_module.property_two == "string"

    sys.modules.pop("my_module")

# Generated at 2022-06-14 06:19:03.282527
# Unit test for function make_lazy
def test_make_lazy():
    # Simulate what would run when a new module is installed
    module_path = 'new_module'
    make_lazy(module_path)
    assert module_path not in sys.modules

    # Check if the new_module is in the sys.modules now
    new_module = sys.modules[module_path]
    assert isinstance(sys.modules[module_path], _LazyModuleMarker)

    # Check if the new_module attribute is in the sys.modules now
    new_module.attr = 'attr'
    assert new_module.attr == 'attr'
    assert sys.modules[module_path].__name__ == module_path


# Make all modules in `discovery.lazy_modules` lazy
for module_path in discovery.lazy_modules:
    make_lazy(module_path)

# Generated at 2022-06-14 06:19:13.407847
# Unit test for function make_lazy
def test_make_lazy():
    import imp

    class DummyModule:
        pass

    # testing non-lazy
    sys.modules['foo'] = DummyModule()
    sys.modules['foo'].foo = 'foo'

    module = imp.load_module('foo', *imp.find_module('foo'))
    assert module.foo == 'foo'

    # testing lazy
    make_lazy('foo')
    assert not isinstance(sys.modules['foo'], DummyModule)

    module = imp.load_module('foo', *imp.find_module('foo'))
    assert module.foo == 'foo'

# Generated at 2022-06-14 06:19:27.463253
# Unit test for function make_lazy
def test_make_lazy():
    # Make sure we don't import something
    old_sys_modules = sys.modules
    sys.modules = {}

    # Imported module
    real_mod = NonLocal(None)
    def real_import(mod_name, *args, **kwargs):
        if not real_mod.value:
            real_mod.value = ModuleType(mod_name)
        return real_mod.value

    # Mock the import function
    with mock.patch('__builtin__.__import__', new=real_import):
        # Run make_lazy to get the new module
        import_path = 'test_make_lazy'
        make_lazy(import_path)
        lazy_mod = sys.modules['test_make_lazy']

        # Make sure we don't import anything
        assert real_mod.value is None

# Generated at 2022-06-14 06:19:40.603533
# Unit test for function make_lazy
def test_make_lazy():
    import math
    import threading

    math_bytes = marshal.dumps(math.__dict__)

    def do_import():
        __import__("math")

    def do_make_lazy():
        make_lazy("math")
        __import__("math")

    # import math normally
    t1 = timeit.Timer(do_import)
    t2 = timeit.Timer(do_make_lazy)

    print("math imported normally: %s" % t1.timeit())
    print("math imported lazily: %s" % t2.timeit())

    # make sure math.pi is still usable
    print("math.pi is %s" % math.pi)

    # make sure math imported lazily is the real math

# Generated at 2022-06-14 06:19:45.523237
# Unit test for function make_lazy
def test_make_lazy():
    import test_lazy_module

    make_lazy('test_lazy_module')
    import test_lazy_module

    assert isinstance(test_lazy_module, _LazyModuleMarker)
    with pytest.raises(AttributeError):
        getattr(test_lazy_module, 'a')

# Generated at 2022-06-14 06:19:57.259854
# Unit test for function make_lazy
def test_make_lazy():
    try:
        import json
    except ImportError:
        pass  # no json, skip.
    else:
        @make_lazy("test.test_make_lazy.json")
        def newjson():
            return json

        old_json = newjson
        newjson = None
        assert old_json is json


# patch in place for json support for Python 2.4
if sys.version_info[:2] == (2, 4):
    import simplejson
    make_lazy("json")
    import json
    sys.modules["json"] = simplejson
    json.loads = simplejson.loads
    json.dumps = simplejson.dumps

# Generated at 2022-06-14 06:20:03.821508
# Unit test for function make_lazy
def test_make_lazy():
    import socket

    assert 'socket' in sys.modules
    assert isinstance(socket, ModuleType)
    assert not isinstance(socket, _LazyModuleMarker)

    sys.modules['socket'] = None
    make_lazy('socket')

    assert 'socket' in sys.modules
    assert sys.modules['socket'] is not None
    assert isinstance(socket, _LazyModuleMarker)

    socket.socket()
    assert isinstance(socket, ModuleType)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 06:20:10.693346
# Unit test for function make_lazy
def test_make_lazy():
    import sys

    assert 'test_module' not in sys.modules

    make_lazy('test_module')

    assert sys.modules['test_module']

    assert isinstance(sys.modules['test_module'], _LazyModuleMarker)

    assert not hasattr(sys.modules['test_module'], '__all__')

    from test_module import test_function

    assert test_function() == 1

    assert isinstance(sys.modules['test_module'], ModuleType)

    assert 'test_function' in sys.modules['test_module'].__all__


# vim: ts=4:sts=4:sw=4:et:fdm=indent

# Generated at 2022-06-14 06:20:21.257386
# Unit test for function make_lazy
def test_make_lazy():
    from sys import modules
    import bokeh.plotting

    for name in list(modules):
        if name.startswith('bkcharts'):
            del modules[name]

    assert 'bkcharts' not in modules
    assert 'bokeh.charts' not in modules
    assert bokeh.plotting.figure
    assert 'bokeh.charts' not in modules
    assert 'bkcharts' not in modules
    import bokeh.charts
    assert 'bokeh.charts' in modules
    assert 'bkcharts' in modules
    import bokeh.charts
    assert 'bokeh.charts' in modules
    assert 'bkcharts' in modules

# Generated at 2022-06-14 06:20:34.704674
# Unit test for function make_lazy
def test_make_lazy():
    lazy_modules = [
        'django.utils',
        'django.utils.translation',
        'django.utils.translation.trans_real'
    ]

    m = __import__('django.utils.translation')
    assert not isinstance(m, _LazyModuleMarker)


    # Ensure all our modules are imported.
    for module_path in lazy_modules:
        __import__(module_path)
        m = sys.modules[module_path]
        assert not isinstance(m, _LazyModuleMarker)


    # Make things lazy
    for module_path in lazy_modules:
        make_lazy(module_path)
        m = sys.modules[module_path]
        assert isinstance(m, _LazyModuleMarker)


    # `gettext` should only import

# Generated at 2022-06-14 06:20:47.004562
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    import os

    # Make sure that the module we want to mock is not already in sys.modules
    # Do not mock "os" module. It may cause bugs
    if "os" in sys.modules:
        pass

    make_lazy("os")
    path = os.path
    assert sys.modules["os"]


# We want to make sure that all common modules are loaded lazily

# Generated at 2022-06-14 06:20:55.833979
# Unit test for function make_lazy
def test_make_lazy():
    """
    Tests that make_lazy does not import the module until the attribute is
    used.
    """
    # We need to use two functions to make sure the module is actually
    # imported this function.
    def im_here():
        """
        Make sure we are here.
        """
        assert False

    def mark_as_here():
        """
        Make sure mark_as_here is marked as here.
        """
        assert False

        mark_as_here.here = True

    import django.core
    django.core.im_here = im_here
    django.core.mark_as_here = mark_as_here

    mark_as_here.here = False

    make_lazy('django.core')

    # Should not have been imported yet.
    assert not mark_as_here

# Generated at 2022-06-14 06:21:11.898072
# Unit test for function make_lazy
def test_make_lazy():
    try:
        import os
        def testfunc():
            # This is to check for certain variable that might be set during
            # `import os`.
            os.environ  # will raise an AttributeError if os is not imported

            assert os is sys.modules['os']
            assert isinstance(os, ModuleType)

        del sys.modules['os']

        make_lazy('os')
        assert isinstance(os, _LazyModuleMarker)

        # This should fail because os is not yet imported.
        with pytest.raises(AttributeError):
            os.environ

        testfunc()

        # This should work because `testfunc` imports `os`
        os.environ

    finally:
        # Cleanup.
        if 'os' in sys.modules:
            del sys.modules['os']

# Generated at 2022-06-14 06:21:19.422469
# Unit test for function make_lazy
def test_make_lazy():
    mod_name = 'silly_name'
    make_lazy(mod_name)
    assert isinstance(sys.modules[mod_name], _LazyModuleMarker), 'make_lazy does not create a _LazyModuleMarker as a placeholder for module'
    assert sys.modules[mod_name].__getattribute__('asdf') == None, 'accessing an attribute after importing the module failed'

# Generated at 2022-06-14 06:21:22.443174
# Unit test for function make_lazy
def test_make_lazy():
    import time
    import numpy as np
    make_lazy('numpy')
    time.sleep(0.1)
    np.zeros(5)

# Generated at 2022-06-14 06:21:33.917871
# Unit test for function make_lazy
def test_make_lazy():
    """
    Unit test for function make_lazy
    """
    import os
    import sys
    import tempfile
    import imp
    import threading
    import time

    # Make some temp code we can import.
    _, tmp_file_name = tempfile.mkstemp()
    with open(tmp_file_name, 'w') as fobj:
        fobj.write('# this is temp python code')

    # Import the temp code, will cause exception if it doesn't import.
    module_path = os.path.splitext(os.path.split(tmp_file_name)[1])[0]
    test_mod = imp.load_source(module_path, tmp_file_name)
    del test_mod

    # Mark our temp module as lazy.
    make_lazy(module_path)



# Generated at 2022-06-14 06:21:41.164652
# Unit test for function make_lazy
def test_make_lazy():
    import os, sys, ctypes
    ctypes_dir = os.path.dirname(ctypes.__file__)
    ctypes_macho_dir = os.path.join(ctypes_dir, 'macholib')
    make_lazy(ctypes_macho_dir)
    import ctypes.macholib
    ctypes.macholib.__file__.startswith(ctypes_macho_dir)

    # Verify that importing an attribute from the dummy LazyModule
    # will import the real module

    import ctypes.macholib.dyld
    isinstance(ctypes_macho_dir, _LazyModuleMarker)

# Generated at 2022-06-14 06:21:52.382356
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    import os
    import tempfile
    import shutil

    def true(_):
        return True

    def false(_):
        return False

    def _create_module(name, path, lines=[]):
        """
        Create a temporary python module.
        """
        with open(path, 'w') as outfile:
            outfile.write(os.linesep.join(lines))

    def _create_package(name):
        """
        Create a temporary package.
        """
        path = os.path.join(master_dir, name)

        os.mkdir(path)
        package_path = os.path.join(path, '__init__.py')
        _create_module(name, package_path)

        return path, package_path


# Generated at 2022-06-14 06:22:06.048928
# Unit test for function make_lazy
def test_make_lazy():
    """
    Unit test for the make_lazy function
    """

    # Make sure the lazy module doesn't exist
    assert '_test_make_lazy' not in sys.modules
    make_lazy('_test_make_lazy')

    # Make sure the lazy module does exist
    assert '_test_make_lazy' in sys.modules

    # Make sure the module is not loaded
    assert '_test_make_lazy' not in sys.modules
    # Make sure isinstance(module, _LazyModuleMarker) is True
    assert isinstance(sys.modules['_test_make_lazy'], _LazyModuleMarker)

    # Now import the module
    sys.modules['_test_make_lazy'].__class__

    # Make sure the module is loaded and that it has the correct attribute


# Generated at 2022-06-14 06:22:17.677061
# Unit test for function make_lazy
def test_make_lazy():
    # import this now, we will remove it later
    import some.really.deep.module  # NOQA

    # remove the module so we can test this
    del sys.modules["some.really.deep.module"]

    # define a function to test
    def some_test():
        try:
            import some.really.deep.module  # NOQA
        except ImportError:
            return False
        else:
            return True

    # ensure the module does not exist
    assert not some_test()
    # let's make the module lazy
    make_lazy("some.really.deep.module")
    # and ensure it's still not loaded
    assert not some_test()

    # now, let's grab some attribute off of it
    import some.really.deep.module.MyClass
    # check to make sure module is loaded

# Generated at 2022-06-14 06:22:26.298294
# Unit test for function make_lazy
def test_make_lazy():
    import os
    import sys

    def analyze_module(module):
        # There should not be a pyspark.testmod object in sys.modules
        assert module not in sys.modules
        make_lazy('pyspark.testmod')

        # There should be a pyspark.testmod object in sys.modules
        assert module in sys.modules
        assert isinstance(sys.modules[module], _LazyModuleMarker)

        # There should not be an os.path object in sys.modules
        assert 'os.path' not in sys.modules
        # Try to access attribute 'curdir' from pyspark.testmod
        assert sys.modules[module].curdir == os.path.curdir

        # There should be an os.path object in sys.modules
        assert 'os.path' in sys.modules


# Generated at 2022-06-14 06:22:37.211097
# Unit test for function make_lazy
def test_make_lazy():
    """
    Test that the LazyModule behaves correctly.
    """
    # just pretend that time is a module that we know exists.
    make_lazy('time')

    # We confirmed that time is lazy, so it doesn't exist yet.

# Generated at 2022-06-14 06:22:52.310889
# Unit test for function make_lazy
def test_make_lazy():
    """
    Test for make_lazy.
    """
    sys.modules.pop('mymodule', None)
    make_lazy('mymodule')
    import mymodule

    assert isinstance(mymodule, _LazyModuleMarker)
    assert not hasattr(mymodule, '__file__')
    assert hasattr(mymodule, 'x')
    assert hasattr(mymodule, 'y')

    import mymodule
    assert isinstance(mymodule, _LazyModuleMarker)
    assert not hasattr(mymodule, '__file__')
    assert hasattr(mymodule, 'x')
    assert hasattr(mymodule, 'y')

# Generated at 2022-06-14 06:22:55.100609
# Unit test for function make_lazy
def test_make_lazy():
    import os

    assert os.path.sep != '\\'
    make_lazy('os.path')

    # Behaviour before assigning a value
    try:
        os.path
        assert False
    except AttributeError:
        pass

    # Behaviour of assigning a value
    os.path.sep = '\\'
    assert os.path.sep == '\\'

# Generated at 2022-06-14 06:23:05.849618
# Unit test for function make_lazy
def test_make_lazy():
    from importlib import import_module
    import os, sys

    # os.path is a builtin module, so this should raise an ImportError
    # if it tries to import it
    try:
        make_lazy('os.path')
    except ImportError:
        pass
    else:
        assert False, 'Failed to properly initialize os.path'

    # Make sure we can retrieve functions from our faked module
    from os.path import join
    join('test', 'dir') == 'test/dir' if os.name == 'posix' else \
                                      'test\\dir'

    # Change the faked module to be a real one
    sys.modules['os.path'] = import_module('os.path')

    # Make sure we can still retrieve functions from our module
    from os.path import join

# Generated at 2022-06-14 06:23:17.819729
# Unit test for function make_lazy
def test_make_lazy():
    import timeit
    import os

    # Break the import statement and make a file that we can write to.
    # The contents of the file will be system-dependent.
    module_path = 'lazy_module_for_testing'
    module_file_path = '{}.py'.format(module_path)
    test_module_import_text = u'import time\n'
    with open(module_file_path, 'w') as f:
        f.write(test_module_import_text)

    # Check to make sure the module doesn't exist.
    try:
        import lazy_module_for_testing
    except ImportError:
        pass
    else:
        raise AssertionError(u'Module exists before adding it to sys.modules.')

    # Add the module to sys.modules and make it a Lazy

# Generated at 2022-06-14 06:23:29.932450
# Unit test for function make_lazy
def test_make_lazy():
    from test_lazy_import import module_to_import

    # Make sure the module is really loaded before we start the test.
    assert hasattr(module_to_import, 'foo')

    # Undefine the module
    del sys.modules['test_lazy_import.module_to_import']

    make_lazy('test_lazy_import.module_to_import')

    # LazyModule is a subclass of ModuleType
    assert isinstance(module_to_import, ModuleType)

    # Fails before we access `foo`
    try:
        assert module_to_import.bar is None
    except AttributeError:
        pass
    else:
        assert False, "AttributeError should have been raised"

    # Now that we access `foo`, the module should be loaded
    assert module_to_import.foo

# Generated at 2022-06-14 06:23:41.146367
# Unit test for function make_lazy
def test_make_lazy():
    import sys

    # Test that we can call make_lazy on a module
    sys.modules['test_make_lazy'] = None
    make_lazy('test_make_lazy')
    assert isinstance(sys.modules['test_make_lazy'], _LazyModuleMarker)
    assert not isinstance(sys.modules['test_make_lazy'], ModuleType)
    assert sys.modules['test_make_lazy'].__name__ == 'test_make_lazy'
    del sys.modules['test_make_lazy']

    # Test that we can call make_lazy on a module with a package.
    # This is a common pattern since we use this in the __init__.py files
    sys.modules['django.test_make_lazy'] = None

# Generated at 2022-06-14 06:23:44.759632
# Unit test for function make_lazy
def test_make_lazy():
    import os
    make_lazy('os')
    assert(isinstance(os, _LazyModuleMarker))
    assert(not hasattr(os, 'name'))
    assert(os.name == 'posix')

# Generated at 2022-06-14 06:23:54.904482
# Unit test for function make_lazy
def test_make_lazy():
    mod1 = NonLocal(None)
    def foo(x):
        mod1.value = x

    make_lazy('test')

    try:
        import test
        assert isinstance(test, _LazyModuleMarker)
        assert mod1.value is None
        assert test.foo == foo
        assert mod1.value is foo
    except ImportError:
        raise ImportError('Skipped Testing')
    finally:
        sys.modules.pop('test')


if __name__ == '__main__':
    test_make_lazy()

# Generated at 2022-06-14 06:24:06.952754
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    from types import ModuleType

    # Test that the module is not loaded upon creation of fake module
    def fk(s):
        def side_effect(*args, **kwargs):
            return 'fake.%s' % attr
        return side_effect

    make_lazy('fake')

    # Test to see if the module is loaded
    # once you access an attribute on it
    # make sure to delete the module so we can run the test
    # multiple times
    if 'fake' in sys.modules:
        del sys.modules['fake']

    make_lazy('fake')
    sys.modules['fake'].__str__ = fk('__str__')
    module = sys.modules['fake']
    assert 'fake.__str__' == sys.modules['fake'].__str__()

# Generated at 2022-06-14 06:24:20.252837
# Unit test for function make_lazy
def test_make_lazy():
    d = {}
    exec("""if 1:
        def a():
            raise Exception
    """, d)

    import sys
    import types
    assert types.ModuleType in d['a'].__class__.__mro__

    # Scenario: import a module, then get an attribute off of it.
    # python ./lazy_modules.py
    # python -J-ea ./lazy_modules.py

    mod_name = 'lazy_modules.test_make_lazy.a'
    make_lazy(mod_name)

    # Make sure that the module is made lazy.
    assert mod_name in sys.modules

    # Make sure that we make the module lazy
    assert isinstance(sys.modules[mod_name], _LazyModuleMarker)

    # Make sure that accessing an attribute causes the module to