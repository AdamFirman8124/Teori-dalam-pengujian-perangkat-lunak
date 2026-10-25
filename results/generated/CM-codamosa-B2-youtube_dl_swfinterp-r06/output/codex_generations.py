

# Generated at 2026-10-24 21:27:07.009951
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-24 21:27:09.560975
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-24 21:27:11.976883
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-24 21:27:14.399821
# Unit test for method __repr__ of class _Multiname

# Generated at 2026-10-24 21:27:16.818317
# Unit test for method __repr__ of class _Multiname

# Generated at 2026-10-24 21:27:19.237751
# Unit test for method __repr__ of class _Multiname

# Generated at 2026-10-24 21:27:21.658368
# Unit test for method make_object of class _AVMClass

# Generated at 2026-10-24 21:27:24.078954
# Unit test for method make_object of class _AVMClass

# Generated at 2026-10-24 21:27:26.497147
# Unit test for method make_object of class _AVMClass

# Generated at 2026-10-24 21:27:28.918824
# Unit test for method __bool__ of class _Undefined

# Generated at 2026-10-24 21:27:31.333973
# Unit test for method __bool__ of class _Undefined

# Generated at 2026-10-24 21:27:33.750577
# Unit test for method __bool__ of class _Undefined

# Generated at 2026-10-24 21:27:36.169503
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-24 21:27:38.585518
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-24 21:27:41.002505
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-24 21:27:44.025809
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:27:46.441284
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:27:48.858578
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:27:51.276263
# Unit test for method make_object of class _AVMClass

# Generated at 2026-10-24 21:27:53.694745
# Unit test for method make_object of class _AVMClass

# Generated at 2026-10-24 21:27:56.110780
# Unit test for method make_object of class _AVMClass

# Generated at 2026-10-24 21:27:58.530531
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:28:00.949358
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:28:03.368327
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:28:05.785847
# Unit test for method make_object of class _AVMClass

# Generated at 2026-10-24 21:28:08.201165
# Unit test for method make_object of class _AVMClass

# Generated at 2026-10-24 21:28:10.621103
# Unit test for method make_object of class _AVMClass

# Generated at 2026-10-24 21:28:27.000532
# Unit test for method __repr__ of class _Multiname
def test__Multiname___repr__():
    assert repr(_Multiname(0x07)) == '[MULTINAME kind: 0x7]'
    assert repr(_Multiname(0x09)) == '[MULTINAME kind: 0x9]'
    assert repr(_Multiname(0x1B)) == '[MULTINAME kind: 0x1b]'
    assert repr(_Multiname(0x00)) == '[MULTINAME kind: 0x0]'
    assert repr(_Multiname(0xFF)) == '[MULTINAME kind: 0xff]'
    assert repr(_Multiname(0x100)) == '[MULTINAME kind: 0x100]'

# Generated at 2026-10-24 21:28:28.334266
# Unit test for method register_methods of class _AVMClass
def test__AVMClass_register_methods():
    cls = _AVMClass(1, 'Test')

    # Empty class: nothing registered yet
    assert cls.method_names == {}
    assert cls.method_idxs == {}

    # Register a single method
    cls.register_methods({'foo': 2})
    assert cls.method_names == {'foo': 2}
    assert cls.method_idxs == {2: 'foo'}

    # Register more methods on the same class
    cls.register_methods({'bar': 3, 'baz': 4})
    assert cls.method_names == {'foo': 2, 'bar': 3, 'baz': 4}
    assert cls.method_idxs == {2: 'foo', 3: 'bar', 4: 'baz'}

    # Later registration overrides an earlier mapping
    cls.register_methods({'foo': 9})
    assert cls.method_names == {'foo': 9, 'bar': 3, 'baz': 4}
    assert cls.method_idxs == {9: 'foo', 3: 'bar', 4: 'baz'}

    # Other attributes untouched
    assert cls.name == 'Test'
    assert cls.name_idx == 1
    assert cls.methods == {}
    assert cls.method_pyfunctions == {}

    print('test__AVMClass_register_methods passed')

# Generated at 2026-10-24 21:28:34.431607
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-24 21:28:55.636700
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():import pytest


# Generated at 2026-10-24 21:28:56.968277
# Unit test for method make_object of class _AVMClass
def test__AVMClass_make_object():
    from unittest import mock

    avm_class = _AVMClass(name_idx=42, name='TestClass', static_properties={'x': 1})
    obj = avm_class.make_object()

    # Returns an object bound to the right class
    assert isinstance(obj, _AVMClass_Object)
    assert obj.avm_class is avm_class

    # repr contains the class name and a hex id
    assert repr(obj).startswith('TestClass#')
    assert repr(obj) == '%s#%x' % (avm_class.name, id(obj))

    # Two calls return distinct objects
    assert avm_class.make_object() is not obj

    # Works on a class with no static properties
    empty = _AVMClass(0, 'Empty')
    assert isinstance(empty.make_object(), _AVMClass_Object)

# Generated at 2026-10-24 21:28:58.295401
# Unit test for method make_object of class _AVMClass
def test__AVMClass_make_object():
    from unittest import mock

    avm_class = _AVMClass(name_idx=42, name='TestClass', static_properties={'x': 1})
    obj = avm_class.make_object()

    # Returns an object bound to the right class
    assert isinstance(obj, _AVMClass_Object)
    assert obj.avm_class is avm_class

    # repr contains the class name and a hex id
    assert repr(obj).startswith('TestClass#')
    assert repr(obj) == '%s#%x' % (avm_class.name, id(obj))

    # Two calls return distinct objects
    assert avm_class.make_object() is not obj

    # Works on a class with no static properties
    empty = _AVMClass(0, 'Empty')
    assert isinstance(empty.make_object(), _AVMClass_Object)

# Generated at 2026-10-24 21:28:59.617336
# Unit test for method make_object of class _AVMClass
def test__AVMClass_make_object():
    from unittest import mock

    avm_class = _AVMClass(name_idx=42, name='TestClass', static_properties={'x': 1})
    obj = avm_class.make_object()

    # Returns an object bound to the right class
    assert isinstance(obj, _AVMClass_Object)
    assert obj.avm_class is avm_class

    # repr contains the class name and a hex id
    assert repr(obj).startswith('TestClass#')
    assert repr(obj) == '%s#%x' % (avm_class.name, id(obj))

    # Two calls return distinct objects
    assert avm_class.make_object() is not obj

    # Works on a class with no static properties
    empty = _AVMClass(0, 'Empty')
    assert isinstance(empty.make_object(), _AVMClass_Object)

# Generated at 2026-10-24 21:29:04.410015
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-24 21:29:32.492933
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():import io

# Generated at 2026-10-24 21:29:35.037156
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-24 21:29:37.455636
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-24 21:29:39.876696
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-24 21:29:42.293073
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:29:44.710829
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:29:47.128064
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:29:49.546906
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-24 21:29:51.961155
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-24 21:29:54.381136
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-24 21:29:57.208766
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:30:16.038729
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():from types import SimpleNamespace


# Generated at 2026-10-24 21:30:19.989256
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-24 21:30:48.860739
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-24 21:31:17.147750
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-24 21:31:18.580481
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():import os
import unittest

from yt_dlp.swfinterpreter import SWFInterpreter

_SWF_DIR = os.path.join(os.path.dirname(__file__), 'swftests')


class TestSWFInterpreter(unittest.TestCase):
    def test_extract_class(self):
        swf_path = os.path.join(_SWF_DIR, 'Assigned_stage_video_display_object.swf')
        with open(swf_path, 'rb') as f:
            swf = f.read()

        interp = SWFInterpreter(swf)
        classes = interp.extract_classes()  # <-- confirm entry point + return shape

        self.assertTrue(classes, 'extract_classes returned nothing')
        for name, cls in classes.items():
            self.assertTrue(name, 'class with empty name')
            self.assertIsNotNone(cls.method_names)

# Generated at 2026-10-24 21:31:21.548690
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:31:33.735571
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:31:51.151768
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():interpreter = SWFInterpreter.__new__(SWFInterpreter)

# Generated at 2026-10-24 21:32:09.408424
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():interpreter = SWFInterpreter.__new__(SWFInterpreter)


# Generated at 2026-10-24 21:32:28.502327
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():method = type('Method', (), {
        'code': bytes((36, 7, 72)),
        'local_count': 1,
    })()

# Generated at 2026-10-24 21:32:43.064323
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():interpreter = SWFInterpreter.__new__(SWFInterpreter)


# Generated at 2026-10-24 21:32:45.487251
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-24 21:32:47.904896
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-24 21:32:50.322304
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-24 21:33:01.371178
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():interpreter = SWFInterpreter.__new__(SWFInterpreter)

# Generated at 2026-10-24 21:33:21.606059
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-24 21:33:24.362842
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:33:52.181940
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:34:12.294203
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:34:16.961353
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-24 21:34:46.116965
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-24 21:34:48.790043
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-24 21:34:51.206927
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:35:06.615863
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():from types import SimpleNamespace


# Generated at 2026-10-24 21:35:08.062349
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():import os
import unittest

from yt_dlp.swfinterpreter import SWFInterpreter

_SWF_DIR = os.path.join(os.path.dirname(__file__), 'swftests')


class TestSWFInterpreter(unittest.TestCase):
    def test_extract_class(self):
        swf_path = os.path.join(_SWF_DIR, 'Assigned_stage_video_display_object.swf')
        with open(swf_path, 'rb') as f:
            swf = f.read()

        interp = SWFInterpreter(swf)
        classes = interp.extract_classes()  # <-- confirm entry point + return shape

        self.assertTrue(classes, 'extract_classes returned nothing')
        for name, cls in classes.items():
            self.assertTrue(name, 'class with empty name')
            self.assertIsNotNone(cls.method_names)

# Generated at 2026-10-24 21:35:12.462481
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-24 21:35:36.015077
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():import struct


# Generated at 2026-10-24 21:35:38.680084
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-24 21:35:41.098811
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-24 21:35:43.515060
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-24 21:35:45.933752
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-24 21:35:48.358323
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-24 21:35:50.771020
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-24 21:35:53.188456
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-24 21:35:55.606255
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-24 21:35:58.023285
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-24 21:36:00.438162
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:36:02.855778
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:36:05.274295
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:36:09.767047
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-24 21:36:12.185529
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-24 21:36:14.605469
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-24 21:36:17.022993
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:36:19.441424
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:36:21.862670
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:36:45.241003
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():interpreter = object.__new__(SWFInterpreter)

# Generated at 2026-10-24 21:36:57.735622
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():interpreter = object.__new__(SWFInterpreter)

# Generated at 2026-10-24 21:37:06.128120
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():interpreter = SWFInterpreter.__new__(SWFInterpreter)