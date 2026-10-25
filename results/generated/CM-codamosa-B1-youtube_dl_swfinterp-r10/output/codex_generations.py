

# Generated at 2026-10-25 01:56:39.247582
# Unit test for method __repr__ of class _Multiname
def test__Multiname___repr__():
    multiname = _Multiname(0x1B)
    assert repr(multiname) == '[MULTINAME kind: 0x1b]'

# Generated at 2026-10-25 01:56:41.779554
# Unit test for constructor of class _Undefined

# Generated at 2026-10-25 01:56:44.194784
# Unit test for constructor of class _Undefined

# Generated at 2026-10-25 01:56:50.761016
# Unit test for constructor of class _Undefined
def test__Undefined():obj = _Undefined()

# Generated at 2026-10-25 01:57:01.715814
# Unit test for constructor of class _Multiname
def test__Multiname():
    kind = 0x07
    obj = _Multiname(kind)

    assert isinstance(obj, _Multiname)
    assert obj.kind == kind
    assert repr(obj) == '[MULTINAME kind: 0x%x]' % kind

# Generated at 2026-10-25 01:57:06.058199
# Unit test for method __bool__ of class _Undefined
def test__Undefined___bool__():
    undefined = _Undefined()

    assert undefined.__bool__() is False
    assert bool(undefined) is False

# Generated at 2026-10-25 01:57:12.571515
# Unit test for method __repr__ of class _Undefined
def test__Undefined___repr__():
    u = _Undefined()
    assert repr(u) == 'undefined'
    assert u.__repr__() == 'undefined'
    assert repr(_Undefined()) == 'undefined'
    # __repr__ is bound to __str__
    assert repr(u) == str(u)

# Generated at 2026-10-25 01:57:16.262498
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

# Generated at 2026-10-25 01:57:43.711899
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 01:57:46.129292
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 01:57:48.773359
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 01:57:50.180415
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

# Generated at 2026-10-25 01:57:53.325986
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 01:58:01.825555
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():interpreter = SWFInterpreter.__new__(SWFInterpreter)

# Generated at 2026-10-25 01:58:13.605423
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():import pytest


# Generated at 2026-10-25 01:58:24.335841
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():interpreter = object.__new__(SWFInterpreter)

# Generated at 2026-10-25 01:58:39.102331
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 01:58:41.804382
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 01:58:44.219724
# Unit test for method __repr__ of class _ScopeDict

# Generated at 2026-10-25 01:58:46.636622
# Unit test for method __repr__ of class _ScopeDict

# Generated at 2026-10-25 01:58:49.050618
# Unit test for method __repr__ of class _ScopeDict

# Generated at 2026-10-25 01:58:51.466353
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 01:58:53.879956
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 01:58:56.551977
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 01:58:58.046116
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

# Generated at 2026-10-25 01:59:23.276047
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 01:59:48.117548
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 02:00:07.135221
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():from types import SimpleNamespace


# Generated at 2026-10-25 02:00:10.010113
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 02:00:37.781114
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 02:00:56.930776
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():import sys

# Generated at 2026-10-25 02:01:01.128875
# Unit test for method __repr__ of class _AVMClass_Object
def test__AVMClass_Object___repr__():
    class MockAVMClass(object):
        name = 'TestClass'

    obj = _AVMClass_Object(MockAVMClass())

    assert repr(obj) == 'TestClass#%x' % id(obj)

# Generated at 2026-10-25 02:01:26.421381
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 02:01:41.270007
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 02:02:00.522020
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 02:02:01.955124
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

# Generated at 2026-10-25 02:02:30.291983
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 02:02:32.706421
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 02:02:35.121209
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 02:02:37.537777
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 02:02:39.955626
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 02:02:42.370187
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 02:02:44.910341
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 02:02:47.324554
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 02:02:49.741362
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 02:02:52.155947
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 02:02:54.570348
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 02:02:56.996909
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 02:02:59.410944
# Unit test for method __repr__ of class _AVMClass_Object

# Generated at 2026-10-25 02:03:01.827523
# Unit test for method __repr__ of class _AVMClass_Object

# Generated at 2026-10-25 02:03:17.013617
# Unit test for method __repr__ of class _AVMClass_Object
def test__AVMClass_Object___repr__():fake_avm_class = type('FakeAVMClass', (), {'name': 'MyClass'})()

# Generated at 2026-10-25 02:03:18.337705
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

# Generated at 2026-10-25 02:03:19.782616
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

# Generated at 2026-10-25 02:03:22.544530
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 02:03:48.373092
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():import struct


# Generated at 2026-10-25 02:03:50.798274
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 02:03:53.324163
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 02:03:55.738992
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 02:03:58.286779
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 02:04:00.704169
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 02:04:03.117368
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 02:04:05.532552
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 02:04:08.371704
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 02:04:11.249608
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 02:04:12.602897
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

# Generated at 2026-10-25 02:04:13.975517
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

# Generated at 2026-10-25 02:04:16.727403
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 02:04:38.115697
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():original_extract_tags = _extract_tags

# Generated at 2026-10-25 02:04:40.666387
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 02:04:43.210375
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 02:04:45.625017
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 02:04:48.304270
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 02:04:50.718362
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 02:04:53.133093
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 02:04:55.547882
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 02:04:57.962538
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 02:05:00.377621
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 02:05:02.792496
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 02:05:05.206645
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 02:05:07.621960
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 02:05:10.315462
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 02:05:35.313626
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 02:05:49.087050
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():from types import SimpleNamespace


# Generated at 2026-10-25 02:06:03.006650
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():interpreter = object.__new__(SWFInterpreter)


# Generated at 2026-10-25 02:06:14.372619
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():avm_class = type('DummyAVMClass', (), {
        'method_pyfunctions': {},
        'variables': {},
    })()

# Generated at 2026-10-25 02:06:33.832616
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():interpreter = SWFInterpreter.__new__(SWFInterpreter)
