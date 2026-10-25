

# Generated at 2026-10-25 04:08:53.589179
# Unit test for method __hash__ of class _Undefined
def test__Undefined___hash__():
    # __hash__ is a constant 0 for every instance
    assert hash(_Undefined()) == 0
    assert isinstance(hash(_Undefined()), int)

    # stable across repeated calls on the same instance
    u = _Undefined()
    assert hash(u) == hash(u) == 0

    # same instance is still usable as a dict key
    assert {u: 'x'}[u] == 'x'

# Generated at 2026-10-25 04:08:55.019635
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

# Generated at 2026-10-25 04:09:12.530972
# Unit test for method __repr__ of class _ScopeDict
def test__ScopeDict___repr__():
    class FakeAVMClass(object):
        def __init__(self, name):
            self.name = name

    # empty dict
    scope = _ScopeDict(FakeAVMClass('Foo'))
    assert repr(scope) == 'Foo__Scope({})'

    # non-empty dict uses dict.__repr__ for inner part
    scope['a'] = 1
    assert repr(scope) == "Foo__Scope({'a': 1})"

# Generated at 2026-10-25 04:09:15.071096
# Unit test for method __repr__ of class _Undefined

# Generated at 2026-10-25 04:09:17.487110
# Unit test for method __repr__ of class _Undefined

# Generated at 2026-10-25 04:09:19.903619
# Unit test for method __repr__ of class _Undefined

# Generated at 2026-10-25 04:09:22.318355
# Unit test for constructor of class _Multiname

# Generated at 2026-10-25 04:09:24.733498
# Unit test for constructor of class _Multiname

# Generated at 2026-10-25 04:09:31.293316
# Unit test for constructor of class _Multiname
def test__Multiname():from youtube_dl.swf import _Multiname


# Generated at 2026-10-25 04:09:41.919921
# Unit test for method register_methods of class _AVMClass
def test__AVMClass_register_methods():avm_class = _AVMClass(name_idx=1, name='TestClass')

# Generated at 2026-10-25 04:09:54.105136
# Unit test for method __bool__ of class _Undefined
def test__Undefined___bool__():
    u = _Undefined()
    # direct call returns False boolean
    assert u.__bool__() is False
    assert isinstance(u.__bool__(), bool)

    # bool() integration
    assert bool(u) is False

    # falsy in conditionals
    assert not u
    assert (u if u else 'fallback') == 'fallback'

    # Python 2 alias preserved
    assert _Undefined.__nonzero__ is _Undefined.__bool__
    assert u.__nonzero__() is False

# Generated at 2026-10-25 04:09:55.551348
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

# Generated at 2026-10-25 04:09:56.922204
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

# Generated at 2026-10-25 04:09:59.350227
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 04:10:01.767112
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 04:10:04.183772
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 04:10:06.609150
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 04:10:09.227701
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 04:10:11.643557
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 04:10:14.062538
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 04:10:16.474351
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 04:10:18.889941
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 04:10:21.308518
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 04:10:23.723310
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 04:10:26.140767
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 04:10:28.762124
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 04:10:57.388368
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 04:11:24.814667
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 04:11:26.250434
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

# Generated at 2026-10-25 04:11:27.686767
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

# Generated at 2026-10-25 04:11:29.134295
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

# Generated at 2026-10-25 04:11:30.567237
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

# Generated at 2026-10-25 04:11:33.367640
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 04:12:02.022271
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 04:12:26.998606
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 04:12:28.427384
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

# Generated at 2026-10-25 04:12:29.959990
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

# Generated at 2026-10-25 04:12:52.999796
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():interpreter = SWFInterpreter.__new__(SWFInterpreter)


# Generated at 2026-10-25 04:13:17.971603
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 04:13:20.384158
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 04:13:22.798994
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 04:13:25.413100
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 04:13:27.828551
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 04:13:30.244169
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 04:13:32.661233
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 04:13:35.076073
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 04:13:37.490588
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 04:13:39.906146
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 04:13:42.320888
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 04:13:45.591438
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 04:13:48.007164
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 04:13:50.422629
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 04:13:52.837501
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 04:13:55.251710
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 04:14:15.060975
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():interpreter = object.__new__(SWFInterpreter)

# Generated at 2026-10-25 04:14:40.413179
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 04:14:42.829764
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 04:14:45.249019
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 04:14:47.664549
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 04:14:50.082381
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 04:14:52.497922
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 04:14:54.914697
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 04:14:57.328604
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 04:14:59.743549
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 04:15:02.158416
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 04:15:04.575680
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 04:15:06.989300
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 04:15:09.405602
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 04:15:11.819749
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 04:15:14.250825
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 04:15:16.657821
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 04:15:19.072855
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 04:15:21.862838
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 04:15:23.265422
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

# Generated at 2026-10-25 04:15:46.955269
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 04:16:13.214885
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 04:16:15.630180
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 04:16:23.303091
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 04:16:25.717766
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 04:16:28.132691
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 04:16:54.462654
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 04:17:09.306984
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 04:17:11.725517
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 04:17:14.139848
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 04:17:16.554286
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 04:17:18.971067
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 04:17:21.384735
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 04:17:23.810522
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 04:17:26.224966
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 04:17:28.639168
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 04:17:31.054248
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 04:17:33.468986
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 04:17:35.885783
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 04:18:01.224737
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 04:18:22.321000
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():from types import SimpleNamespace


# Generated at 2026-10-25 04:18:24.738854
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 04:18:27.181384
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 04:18:29.612591
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 04:18:32.026361
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 04:18:34.442404
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 04:18:36.859869
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 04:18:39.272560
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 04:18:41.689346
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 04:18:44.115816
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 04:18:46.542587
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 04:18:48.957702
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 04:18:51.374386
# Unit test for method extract_class of class SWFInterpreter