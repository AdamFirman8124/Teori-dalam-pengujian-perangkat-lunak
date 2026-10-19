

# Generated at 2022-06-14 06:14:46.918020
# Unit test for function make_lazy
def test_make_lazy():
    """
    Tests the make_lazy function
    """
    if 'test_make_lazy' in sys.modules:
        del sys.modules['test_make_lazy']

    make_lazy('test_make_lazy')
    assert test_make_lazy
    assert not isinstance(test_make_lazy, _LazyModuleMarker)

    # not lazy modules
    assert not isinstance(make_lazy, _LazyModuleMarker)
    assert not isinstance(sys, _LazyModuleMarker)
    assert not isinstance(NonLocal, _LazyModuleMarker)
    assert not isinstance(_LazyModuleMarker, _LazyModuleMarker)

    lazy_modules = [
        'test_make_lazy'
    ]


# Generated at 2022-06-14 06:14:55.561088
# Unit test for function make_lazy
def test_make_lazy():
    """
    We can't import this module during the tests, as it would break nose.
    Instead, we just compile and exec a little snippet that represents
    what this module does.

    This is a bit of a hack and I would be very open to a better solution.
    """

# Generated at 2022-06-14 06:15:07.331801
# Unit test for function make_lazy
def test_make_lazy():
    # Assert that the module does not exist
    assert 'mylazymodule' not in sys.modules

    # Make the module lazy and assert that it does exist
    make_lazy('mylazymodule')
    assert 'mylazymodule' in sys.modules

    # Assert that it appears to be an instance of a module
    # (but it's not actually)
    assert isinstance(sys.modules['mylazymodule'], _LazyModuleMarker)

    # Assert that you can access an attribute on the module
    # (the module will load itself)
    assert sys.modules['mylazymodule'].__file__


if __name__ == '__main__':
    # Run the unit tests
    test_make_lazy()

# Generated at 2022-06-14 06:15:12.331380
# Unit test for function make_lazy
def test_make_lazy():
    import os
    make_lazy('os')
    isinstance(os, _LazyModuleMarker) == True
    import os
    isinstance(os, _LazyModuleMarker) == False
    isinstance(os, ModuleType) == True

# Generated at 2022-06-14 06:15:25.096056
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    sys.modules.clear()

    import pkg
    assert pkg in sys.modules
    assert isinstance(pkg, ModuleType)

    del sys.modules['pkg']
    make_lazy('pkg')
    assert pkg not in sys.modules
    assert isinstance(pkg, _LazyModuleMarker)

    assert pkg.__name__ == 'pkg'
    assert pkg in sys.modules
    assert isinstance(pkg, ModuleType)
    assert pkg.attr1

    assert sys.modules.get('pkg.mod1') is None
    assert pkg.mod1.__name__ == 'pkg.mod1'
    assert sys.modules.get('pkg.mod1') is not None

# Generated at 2022-06-14 06:15:33.163167
# Unit test for function make_lazy
def test_make_lazy():
    import gc

    class TestClass(object):
        """
        Dummy class for testing `make_lazy`
        """
        pass

    # Test a simple import
    sys.modules['simple_package'] = TestClass()
    make_lazy('simple_package')
    assert isinstance(sys.modules['simple_package'], _LazyModuleMarker)
    assert sys.modules['simple_package'].__class__.__name__ == 'LazyModule'

    # Test a package with submodules
    sys.modules['simple_package.submodule'] = TestClass()
    make_lazy('simple_package.submodule')
    assert isinstance(sys.modules['simple_package.submodule'], _LazyModuleMarker)
    assert sys.modules['simple_package.submodule'].__class__.__name

# Generated at 2022-06-14 06:15:43.886351
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    import os
    sys.path.append("/tmp")

# Generated at 2022-06-14 06:15:56.403344
# Unit test for function make_lazy
def test_make_lazy():
    make_lazy("foo")

    import foo
    assert isinstance(foo, _LazyModuleMarker), type(foo)

    import sys
    from types import ModuleType

    assert 'foo' not in sys.modules
    assert foo.__mro__ == (LazyModule, ModuleType)

    # Even though 'foo' isn't in the sys.modules, this should still work
    # because it's a lazy module.
    foo.bar = 'baz'

    # Now, the module exists in sys.modules
    assert 'foo' in sys.modules
    assert getattr(sys.modules['foo'], 'bar') == 'baz'

    # These should all work the same
    assert foo is sys.modules['foo']
    assert foo.__dict__ is sys.modules['foo'].__dict__

    # Now that the

# Generated at 2022-06-14 06:15:59.343372
# Unit test for function make_lazy
def test_make_lazy():

    make_lazy('logging')
    assert isinstance(logging, _LazyModuleMarker)

    import logging
    assert not isinstance(logging, _LazyModuleMarker)

# Generated at 2022-06-14 06:16:11.376243
# Unit test for function make_lazy
def test_make_lazy():
    # imports may fail, most likely due to circular imports, so suppress
    # the error messages
    import logging
    logging.disable(logging.ERROR)

    # make sure that make_lazy doesn't exist in sys.modules
    # unless we specifically create it
    assert 'make_lazy' not in sys.modules

    # make a module
    module_name = 'make_lazy'
    fake_module_name = 'fake_module'
    module_path = '.'.join((__name__, module_name))
    fake_module_path = '.'.join((__name__, fake_module_name))

    # make a fake module

# Generated at 2022-06-14 06:16:21.828427
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    sys.modules.pop('django.forms.fields', None)

    class MyForm(forms.Form):
        field_one = forms.CharField()
        field_two = forms.CharField()

    make_lazy('django.forms.fields')
    myform = MyForm()
    myform.is_valid()

    assert 'django.forms.fields' in sys.modules
    assert sys.modules['django.forms.fields'].CharField


# Generated at 2022-06-14 06:16:23.914617
# Unit test for function make_lazy
def test_make_lazy():
    make_lazy('sys')
    sys is not None
    make_lazy('re')
    re is not None

# Generated at 2022-06-14 06:16:31.304424
# Unit test for function make_lazy
def test_make_lazy():
    # Make sure that the LazyModule does not exist yet
    assert "test_lazy_module" not in sys.modules
    # Make the module lazy
    make_lazy("test_lazy_module")
    # Verify that the LazyModule is in sys.modules
    assert "test_lazy_module" in sys.modules
    # Try to access test_lazy_module
    import test_lazy_module
    assert test_lazy_module.TEST_VALUE == "success"

# launch the unit tests if the module is the main program
if __name__ == "__main__":
    test_make_lazy()

# Generated at 2022-06-14 06:16:42.079340
# Unit test for function make_lazy
def test_make_lazy():
    # Test module 1
    make_lazy('test_module_1')
    import test_module_1
    # test_module_1 should be lazy, so isinstance(test_module_1, ModuleType)
    # should be false
    assert not isinstance(test_module_1, ModuleType)
    # test_module_1 should be a LazyModule object.
    assert isinstance(test_module_1, _LazyModuleMarker)

    # Test module 2
    make_lazy('test_module_2')
    import test_module_2
    # test_module_2 should be lazy, so isinstance(test_module_2, ModuleType)
    # should be false
    assert not isinstance(test_module_2, ModuleType)
    # test_module_2 should be a LazyModule object.


# Generated at 2022-06-14 06:16:55.613542
# Unit test for function make_lazy
def test_make_lazy():
    """
    test function
    """
    import sys
    import importlib
    from types import ModuleType

    # When `_weblib` is not imported, we expect the `sys.modules` to not have
    # the key `weblib._weblib`.
    # When `_weblib` is imported, we expect the `sys.modules` to have the key
    # `weblib._weblib` and point to a `Module` type.
    # When we import `weblib`, we expect the `sys.modules` to have the key
    # `weblib` point to `weblib._weblib`.
    make_lazy('weblib._weblib')

    # Test that it is a standin module
    assert 'weblib._weblib' in sys.modules
    assert isinstance

# Generated at 2022-06-14 06:17:03.341794
# Unit test for function make_lazy
def test_make_lazy():
    import unittest

    # Create 'dummy' module structure to test imports against
    sys.modules['foo'] = 'This is what you get from importing from foo'
    # Arbitrary module to test against
    sys.modules['arbitrary'] = 'This is what you get from importing arbitrary'

    # our dummy module 'foo' must be the first module that is imported.
    # the 'assertFalse' comes from unittest.
    dummy_module_is_first = False
    try:
        make_lazy('foo')
        import foo
        import arbitrary
        dummy_module_is_first = True
    except:
        pass
    assertFalse(dummy_module_is_first, 'LazyModule is not the first module to be imported!')

    # now we will check to make sure an exception is raised when we try to
   

# Generated at 2022-06-14 06:17:14.951712
# Unit test for function make_lazy
def test_make_lazy():
    """
    Test function make_lazy
    """
    sys.modules['examples.lazy_import'] = None
    assert 'examples.lazy_import' not in sys.modules
    make_lazy('examples.lazy_import')
    assert 'examples.lazy_import' in sys.modules
    assert isinstance(sys.modules['examples.lazy_import'], _LazyModuleMarker)
    assert sys.modules['examples.lazy_import'].foobar is 'foobar'
    assert sys.modules['examples.lazy_import'].foo is 'foo'
    assert sys.modules['examples.lazy_import'] is sys.modules['examples.lazy_import']
    assert sys.modules['examples.lazy_import'].bar is 'bar'

# Generated at 2022-06-14 06:17:29.237830
# Unit test for function make_lazy
def test_make_lazy():
    """
    This test is for the make_lazy module

    1. Modified the sys.modules to store the lazy module in the test_module
    2. Loaded test_module dynamically using importlib module
    3. Checked if the test_module is lazy module and not actual module
    4. Checked if actual module is imported when accessing the properties
    """

# Generated at 2022-06-14 06:17:35.128947
# Unit test for function make_lazy
def test_make_lazy():
    os = __import__('os')
    make_lazy('os')
    assert not hasattr(os, 'curdir')
    assert getattr(os, 'curdir') == '.'
    assert hasattr(os, 'curdir')



# Generated at 2022-06-14 06:17:49.091760
# Unit test for function make_lazy
def test_make_lazy():
    import os, sys
    import types

    # This unit test only works in Python 2.x
    if sys.version_info[0] != 2:
        return

    class TestModule(object):
        def __init__(self):
            self.import_count = 0
            self.import_count_ov = 0

        def checked_import(self):
            self.import_count += 1

        def checked_import_ov(self):
            if self.import_count_ov > 0:
                raise Exception("Overimport detected")

            self.import_count_ov += 1

    mod = types.ModuleType('test_module')
    mod.checked_import = TestModule().checked_import
    sys.modules['test_module'] = mod

    def check_and_make_lazy(path):
        import test_module
       

# Generated at 2022-06-14 06:18:04.729001
# Unit test for function make_lazy
def test_make_lazy():
    """
    This function will run make_lazy and simulate a user accessing the
    module that is marked as lazy.
    """
    import sys
    old_modules = sys.modules.copy()
    try:
        make_lazy("datetime")
        # this would fail without make_lazy because the datetime module would
        # be imported earlier
        assert "datetime" not in sys.modules
        # simulate someone doing "import datetime"
        import datetime
        assert datetime
        assert "datetime" in sys.modules
        # simulate someone doing "from datetime import date"
        from datetime import date
        assert date
        assert "datetime" in sys.modules
        assert "datetime.date" in sys.modules
    finally:
        sys.modules = old_modules

# Generated at 2022-06-14 06:18:12.976456
# Unit test for function make_lazy
def test_make_lazy():
    """
    Test function make_lazy
    """
    from common.python.__test__.unit.pythond_test import (
        EXT_MODULES, TEST_MODULES, _TEST_MODULE_NAME)

    # Check test modules is present
    assert _TEST_MODULE_NAME in sys.modules

    # Check that test modules are present in EXT_MODULES
    assert set(EXT_MODULES) == set(TEST_MODULES)

    _TEST_MODULE_NAME2 = _TEST_MODULE_NAME+"2"

    # Check that test module is not present
    assert _TEST_MODULE_NAME2 not in sys.modules

    # Make test module2 lazy
    make_lazy(_TEST_MODULE_NAME2)

    # Check that the value in sys

# Generated at 2022-06-14 06:18:25.607723
# Unit test for function make_lazy
def test_make_lazy():
    # Create a test package with two modules inside
    test_package = tempfile.mkdtemp()
    test_package_first_mod_path = os.path.join(test_package, 'first.py')
    test_package_second_mod_path = os.path.join(test_package, 'second.py')
    with open(test_package_first_mod_path, 'w') as f:
        f.write(textwrap.dedent("""
            a = 1
            """))
    with open(test_package_second_mod_path, 'w') as f:
        f.write(textwrap.dedent("""
            b = 2
            """))

    sys.path.append(test_package)

# Generated at 2022-06-14 06:18:36.225899
# Unit test for function make_lazy
def test_make_lazy():
    import ldap
    assert isinstance(ldap, _LazyModuleMarker)
    make_lazy('ldap')
    assert isinstance(ldap, _LazyModuleMarker)
    import ldap
    assert not isinstance(ldap, _LazyModuleMarker)
    assert ldap.__name__ == 'ldap'
    make_lazy('ldap')
    assert isinstance(ldap, _LazyModuleMarker)
    import ldap
    assert not isinstance(ldap, _LazyModuleMarker)
    assert ldap.__name__ == 'ldap'

# Generated at 2022-06-14 06:18:40.877352
# Unit test for function make_lazy
def test_make_lazy():
    make_lazy('a')
    from a import b
    assert b == 1
    make_lazy('a.b')
    from a import c
    assert c == 2


# Importing for side-effect of make_lazy calls
from a import b, c

# Generated at 2022-06-14 06:18:54.064034
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    sys.modules["test.a.b.c"] = 0
    make_lazy("test.a.b.c")
    mm = sys.modules["test.a.b.c"]
    assert isinstance(mm, _LazyModuleMarker), mm
    assert mm not in sys.modules.values(), mm
    assert mm.__mro__() == (mm.__class__, ModuleType)
    a = mm.a
    assert isinstance(a, ModuleType), a
    assert a in sys.modules.values(), a
    assert a.__name__ == "test.a.b.c.a", a.__name__
    del a
    b = mm.b
    assert isinstance(b, ModuleType), b
    assert b in sys.modules.values(), b
    assert b.__name__

# Generated at 2022-06-14 06:19:05.846186
# Unit test for function make_lazy
def test_make_lazy():
    # Go through the module loader gyrations so we can mess with __dict__
    from .test_lazy_module import os
    os.__dict__ = os.__dict__.copy()

    # Remove os from sys.modules so we can test it as a regular module
    module_path = 'celery.tests.test_lazy_module.os'
    sys.modules.pop(module_path)

    # Make sure that it doesn't have os loaded
    assert not hasattr(os, 'name')
    assert not (os.__class__.__mro__[-1] is sys.modules['os'])

    # Mark test_lazy_module.os as lazy
    make_lazy(module_path)

    # Make sure the os class hasn't changed
    assert ModuleType in os.__class__.__mro

# Generated at 2022-06-14 06:19:12.201754
# Unit test for function make_lazy
def test_make_lazy():
    module = 'test_lazy'
    make_lazy(module)

    from . import test_lazy
    assert isinstance(test_lazy, _LazyModuleMarker)

    old_value = test_lazy.VALUE
    test_lazy.VALUE = 100
    assert test_lazy.VALUE == 100
    test_lazy.VALUE = old_value


if __name__ == '__main__':
    test_make_lazy()

# Generated at 2022-06-14 06:19:19.931549
# Unit test for function make_lazy
def test_make_lazy():
    make_lazy('foo')

    foo = sys.modules['foo']
    assert foo
    assert isinstance(foo, _LazyModuleMarker)
    assert 'foo' not in sys.modules

    # accessing attributes will 'activate' the module
    assert foo.__name__ == 'foo'
    assert foo
    assert isinstance(foo, ModuleType)
    assert 'foo' in sys.modules

# Generated at 2022-06-14 06:19:33.156419
# Unit test for function make_lazy
def test_make_lazy():
    """
    Unit test to make sure make_lazy is working as expected.
    """
    import os
    import sys
    import shutil
    import tempfile
    import textwrap

    # NOTE: This module is not setup with the standard
    # setup.py/setup.cfg setup because it is only a unittest
    # and is not part of the source distribution.

    # Create a temporary directory to work in
    temp_dir = tempfile.mkdtemp()

    # Create a sample module
    module_dir = os.path.join(temp_dir, 'sample_module')
    module_file = os.path.join(module_dir, '__init__.py')


# Generated at 2022-06-14 06:19:43.105742
# Unit test for function make_lazy
def test_make_lazy():
    from backports.functools_lru_cache.make_lazy import make_lazy, sys

    make_lazy('os')

    assert 'os' not in sys.modules

    assert isinstance(sys.modules['os'], _LazyModuleMarker)

    assert 'path' not in sys.modules

    path = sys.modules['os'].path

    assert id(path) == id(sys.modules['os.path'])

    assert 'path' in sys.modules

# Generated at 2022-06-14 06:19:51.986468
# Unit test for function make_lazy
def test_make_lazy():
    import sys
    import os

    # Make sure the testing module is not in the sys.modules
    test_mod = "test_module"
    if test_mod in sys.modules:
        del sys.modules[test_mod]

    # Create a module with a variable called "lazy_var"
    # and add it to sys.modules as a named module
    test_str = "lazy_var = 'not lazy'"
    test_file = open("test_module.py", "w")
    test_file.write(test_str)
    test_file.close()

    # Add a lazy module to the sys.modules
    make_lazy(test_mod)

    # Check that the module has not been imported
    assert test_mod not in globals()

    # Check that it can be imported after the fact
    import test

# Generated at 2022-06-14 06:20:01.319516
# Unit test for function make_lazy
def test_make_lazy():
    """
    Makes sure the functionality of make_lazy works as expected.
    """
    make_lazy('temp_mod')

    import temp_mod  # pylint: disable=import-outside-toplevel, import-error
    temp_mod.var = 'Something'

    # We need to use isinstance to make sure it passes the mro checks.
    assert isinstance(temp_mod, _LazyModuleMarker)  # pylint: disable=undefined-variable

    import temp_mod  # pylint: disable=import-outside-toplevel, import-error
    assert temp_mod.var == 'Something'

# Generated at 2022-06-14 06:20:12.363272
# Unit test for function make_lazy
def test_make_lazy():
    """
    Simple unit test for make_lazy.
    """
    make_lazy('gstudio.urls')
    from gstudio.urls import urls


# Generated at 2022-06-14 06:20:22.733412
# Unit test for function make_lazy
def test_make_lazy():
    class TestClass(object):
        def test_it(self, assert_):
            assert_(hasattr(sys, 'modules'))
            module_path='os'
            assert_(module_path not in sys.modules)
            make_lazy(module_path)
            assert_(module_path in sys.modules)
            assert_(sys.modules[module_path])
            assert_(isinstance(sys.modules[module_path], _LazyModuleMarker))
            assert_(not isinstance(sys.modules[module_path], ModuleType))
            assert_(hasattr(sys.modules[module_path], 'path'))
            assert_(hasattr(sys.modules[module_path], 'system'))
            assert_('os' not in sys.modules)

# Generated at 2022-06-14 06:20:35.930117
# Unit test for function make_lazy
def test_make_lazy():
    import test_lazy
    # in test_lazy.py, we have a value 'test_value = "test"'
    # we use this value to test lazy module.
    # On initialization, test_lazy.py hasn't been loaded.
    # The __getattribute__ of LazyModule object will be called
    # when we try to access attribute of test_lazy.
    # Inside __getattribute__ function, test_lazy.py will be loaded.
    # With the loaded test_lazy module, we can access its attribute
    # test_value.
    # All those things happen in one line, so we don't need to
    # import test_lazy, and test_lazy.py won't be loaded.
    assert test_lazy.test_value == 'test'
    import os
    # In python implementation, every module

# Generated at 2022-06-14 06:20:42.314321
# Unit test for function make_lazy
def test_make_lazy():
    import re

    assert isinstance(re, _LazyModuleMarker) is False
    assert isinstance(sys.modules['re'], _LazyModuleMarker) is False

    reload(lazy)
    lazy.make_lazy('re')

    assert isinstance(re, _LazyModuleMarker) is True
    assert isinstance(sys.modules['re'], _LazyModuleMarker) is True

# Generated at 2022-06-14 06:20:47.058785
# Unit test for function make_lazy
def test_make_lazy():
    import types
    import sys

    class Module(object):
        pass

    sys.modules['lazy_module'] = Module()

    make_lazy('lazy_module')

    assert isinstance(sys.modules['lazy_module'], types.ModuleType)

# Generated at 2022-06-14 06:20:48.614920
# Unit test for function make_lazy
def test_make_lazy():
    import doctest
    doctest.testmod()


# Generated at 2022-06-14 06:20:56.282011
# Unit test for function make_lazy
def test_make_lazy():
    module_name = 'time'
    module_path = module_name
    sys_modules = sys.modules  # cache in the locals
    make_lazy(module_path)
    # make sure module does not exist in sys.modules
    # make_lazy mocked the module for lazy loading
    assert module_path not in sys_modules
    # check that lazy module is an instance of LazyModule
    assert isinstance(sys_modules[module_path], _LazyModuleMarker)
    # check that isinstance correctly identifies LazyModule
    # as ModuleType
    assert issubclass(type(sys_modules[module_path]), ModuleType)
    # check that LazyModule stays an instance of LazyModule
    # after getattr is called
    sys_modules[module_path].time

# Generated at 2022-06-14 06:21:10.694636
# Unit test for function make_lazy
def test_make_lazy():
    def reset_sys_modules():
        sys_modules = sys.modules  # cache in the locals
        sys_modules.pop('foo.bar', None)
        sys_modules['foo'] = __import__('foo')

    reset_sys_modules()
    foo = sys.modules['foo']

    # just peeking into the module should cause the import of bar
    bar = foo.bar

    # assert that everything worked as expected
    assert sys.modules['foo.bar'].__class__.__name__ == 'LazyModule'
    assert sys.modules['foo'].bar.__class__.__name__ == 'Bar'
    assert sys.modules['foo'].foo == foo

    # clean up
    reset_sys_modules()



# Generated at 2022-06-14 06:21:19.759811
# Unit test for function make_lazy
def test_make_lazy():
    def do_test_make_lazy():
        for mod_name in ('some.loadable.package',
                         'some.loadable.module'):
            import_time = time.time()
            make_lazy(mod_name)
            import_time = time.time() - import_time

            import_func = lambda: __import__(mod_name)
            load_time = timeit.timeit(import_func, number=100)
            load_time_with_lazy = timeit.timeit(import_func, number=100)

            assert import_time < load_time
            assert import_time > load_time_with_lazy, 'Lazy module not faster'

    do_test_make_lazy()



# Generated at 2022-06-14 06:21:32.502747
# Unit test for function make_lazy
def test_make_lazy():
    test_m = __import__('test_make_lazy')
    assert isinstance(test_m, ModuleType)
    assert test_m.__name__ == 'test_make_lazy'

    del sys.modules['test_make_lazy']
    make_lazy('test_make_lazy')
    test_m = __import__('test_make_lazy')
    assert isinstance(test_m, _LazyModuleMarker)
    assert test_m.__name__ == 'test_make_lazy'
    assert test_m.__class__.__name__ == 'LazyModule'
    assert test_m.__doc__ == '\n        A standin for a module to prevent it from being imported\n        '

# Generated at 2022-06-14 06:21:40.503473
# Unit test for function make_lazy
def test_make_lazy():
    """
    Test that the function actually works.
    """
    import os
    import tempfile
    import sys

    # make a temporary directory for the test
    temp_directory = tempfile.mkdtemp()

    # create a temporary module that is a little expensive to load
    tmpfilename = os.path.join(temp_directory, 'lazymodule.py')

# Generated at 2022-06-14 06:21:52.151542
# Unit test for function make_lazy
def test_make_lazy():
    import os
    import tempfile
    from types import ModuleType

    # Create a fake module in a temporary directory
    module_path = os.path.join(tempfile.mkdtemp(), 'fake_module.py')
    with open(module_path, 'w') as f:
        f.write("module_var = 'Hello'")

    # Try that it works as a normal import
    import fake_module
    assert fake_module.module_var == 'Hello'

    # Mark it as lazy
    make_lazy(module_path)
    import fake_module
    assert isinstance(fake_module, ModuleType)
    assert isinstance(fake_module, _LazyModuleMarker)
    assert not hasattr(fake_module, 'module_var')

    # Accessing it loads the real module

# Generated at 2022-06-14 06:21:56.376612
# Unit test for function make_lazy
def test_make_lazy():
    """
    Test function make_lazy
    """
    d = sys.modules.copy()
    make_lazy('os')
    assert sys.modules['os'] is not d['os']

# Unit Test for function test_make_lazy

# Generated at 2022-06-14 06:22:04.399931
# Unit test for function make_lazy
def test_make_lazy():
    module_path = 'my_fake_module'

    # set up module and make lazy
    sys.modules[module_path] = FakeModule()
    make_lazy(module_path)

    mod = sys.modules[module_path]

    assert isinstance(mod, _LazyModuleMarker)
    assert not hasattr(mod, 'attribute')

    mod.attribute = 'test'
    assert mod.attribute == 'test'

    del sys.modules[module_path]
    del mod



# Generated at 2022-06-14 06:22:17.173573
# Unit test for function make_lazy
def test_make_lazy():
    import sys

    module_path = 'mock.lazy_module'

    # NonLocal to allow Python 2 to have similar usage as Python 3.
    module = NonLocal(None)
    sys_modules = sys.modules

    class LazyModule(_LazyModuleMarker):
        def __mro__(self):
            return (LazyModule, ModuleType)

        def __getattribute__(self, attr):
            if module.value is None:
                del sys_modules[module_path]
                module.value = __import__(module_path)

                sys_modules[module_path] = __import__(module_path)

            return getattr(module.value, attr)

    make_lazy(module_path)

    if sys_modules[module_path].__class__ != LazyModule:
        raise

# Generated at 2022-06-14 06:22:26.077062
# Unit test for function make_lazy
def test_make_lazy():
    orig_sys_modules = sys.modules.copy()


# Generated at 2022-06-14 06:22:37.834027
# Unit test for function make_lazy
def test_make_lazy():
    """
    Test the module-level function make_lazy
    """
    import sys
    import types
    import django.conf

    # noinspection PyUnresolvedReferences
    import django.core.exceptions
    # noinspection PyUnresolvedReferences
    import django.conf.urls
    # noinspection PyUnresolvedReferences
    import django.contrib
    # noinspection PyUnresolvedReferences
    from django.contrib.auth.models import User
    # noinspection PyUnresolvedReferences
    from django.contrib.auth.hashers import BCryptPasswordHasher

    # Make sure the `sys.modules` cache is empty.
    mod_name_ls = list(sys.modules.keys())

# Generated at 2022-06-14 06:22:55.214111
# Unit test for function make_lazy
def test_make_lazy():
    """
    Test that make_lazy is working properly.
    """
    from sys import modules
    # check that module is not in cache
    assert 'tests.lazy_loader' not in modules
    # check that our custom class is in place
    assert modules['tests.lazy_loader']
    # check that our module is being returned
    assert isinstance(modules['tests.lazy_loader'], _LazyModuleMarker)
    # check that the module is loaded
    assert isinstance(modules['tests.lazy_loader'].test_make_lazy, types.FunctionType)
    # check that our custom class is not longer in place
    assert not isinstance(modules['tests.lazy_loader'], _LazyModuleMarker)
    # check that module is in cache
    assert 'tests.lazy_loader' in modules

# Generated at 2022-06-14 06:23:05.902974
# Unit test for function make_lazy
def test_make_lazy():
    from types import ModuleType

    import lazy_module

    # Make sure that even when a module is marked as lazy, we can still
    # import arbitrary modules.
    import os

    # Validate that the lazy module looks like a normal module,
    # but that when an attribute is actually accessed, we load
    # the module
    assert isinstance(lazy_module, ModuleType)
    assert not hasattr(lazy_module, '__file__')
    assert hasattr(os, '__file__')
    # Make sure that we can access attributes off of the module
    # and that it actually gets imported.
    assert lazy_module.test_attr == 'foo'
    # Make sure that the module is a real module
    assert hasattr(lazy_module, '__file__')
    # Make sure that we can still access other modules
   

# Generated at 2022-06-14 06:23:16.381597
# Unit test for function make_lazy
def test_make_lazy():
    """
    Ensure that make_lazy works
    """

    # A module to use for testing
    class _TestModule(object):
        def __init__(self):
            self.a = 1
            self.b = 2
            self.c = 3

    # Make sure the module isn't in sys.modules
    module_path = 'testpath'
    sys.modules.pop(module_path, None)

    make_lazy(module_path)

    # Make sure it can be imported
    try:
        module = __import__(module_path)
    except ImportError:
        assert False, "Make lazy prevents importing module"

    # Make sure types are correct
    assert isinstance(module, _LazyModuleMarker)

    # Make sure we did not import the module

# Generated at 2022-06-14 06:23:20.169200
# Unit test for function make_lazy
def test_make_lazy():
    mod = make_lazy('lazy')
    assert isinstance(mod, _LazyModuleMarker)
    assert getattr(mod, '__name__') == 'lazy'
    assert getattr(mod, '__path__') == 0

# Generated at 2022-06-14 06:23:27.526577
# Unit test for function make_lazy
def test_make_lazy():
    sys.modules["test_make_lazy"] = None
    make_lazy('test_make_lazy')
    if "test_make_lazy" in sys.modules:
        assert isinstance(sys.modules["test_make_lazy"], _LazyModuleMarker)
    else:
        assert False
    try:
        test_make_lazy.func_name
    except Exception:
        assert False
    finally:
        make_lazy('test_make_lazy')

# Generated at 2022-06-14 06:23:36.716502
# Unit test for function make_lazy
def test_make_lazy():
    """
    Tests the function make_lazy.

    Raises:
        AssertionError if the test fails.
    """
    make_lazy('foo.bar')

    # Check that the module is marked as lazy loading
    assert isinstance(sys.modules['foo.bar'], _LazyModuleMarker)

    # Check that we don't fail when the lazy module is called
    import foo.bar

    assert foo.bar is sys.modules['foo.bar']

    # Check that the module was loaded
    assert hasattr(foo.bar, '__file__')



# Generated at 2022-06-14 06:23:49.587155
# Unit test for function make_lazy
def test_make_lazy():
    module_path = 'utils.test_make_lazy_helper'
    import sys
    sys.path.append(os.path.dirname(__file__))

# Generated at 2022-06-14 06:24:00.432235
# Unit test for function make_lazy
def test_make_lazy():
    import some_module

    assert not isinstance(sys.modules["some_module"], _LazyModuleMarker)
    assert "foo" in dir(some_module)
    assert "foo" in dir(sys.modules["some_module"])
    del sys.modules["some_module"]

    make_lazy("some_module")

    assert isinstance(sys.modules["some_module"], _LazyModuleMarker)
    assert "foo" not in dir(sys.modules["some_module"])
    assert "foo" not in dir(some_module)

    assert "foo" in dir(some_module)
    assert "foo" in dir(sys.modules["some_module"])

    print("Success")

# Generated at 2022-06-14 06:24:13.229370
# Unit test for function make_lazy
def test_make_lazy():
    try:
        # Setup
        module_path = 'code_without_side_effects'
        make_lazy(module_path)
        import code_without_side_effects
        orig_module_types = tuple(code_without_side_effects.__mro__)
        # Do not execute any code from the module

        # Test
        code_without_side_effects.x = 1
        assert code_without_side_effects.x == 1

        # Cleanup
        del code_without_side_effects
        del sys.modules[module_path]
    finally:
        # Make sure that this function does not affect any other modules
        assert 'code_without_side_effects' not in sys.modules
        assert 'code_without_side_effects' not in globals().keys()


# Generated at 2022-06-14 06:24:23.676106
# Unit test for function make_lazy
def test_make_lazy():
    try:
        import tempfile
    except ImportError:
        # the unittest will skip this test
        raise Exception()

    # Set up the files and imports we need.
    _, module_path = tempfile.mkstemp()
    sys.modules[module_path] = object()
    import_path = module_path.replace(os.path.sep, '.')

    def module_test():
        import import_path
        assert isinstance(import_path, _LazyModuleMarker)

    # Force importing the path
    module_test()

    # Now test that the module really gets lazy loaded.
    make_lazy(import_path)

    # Import again.
    module_test()

    # Now import a submodule.