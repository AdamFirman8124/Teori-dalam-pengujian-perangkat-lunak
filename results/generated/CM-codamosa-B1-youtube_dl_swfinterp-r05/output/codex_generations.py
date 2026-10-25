

# Generated at 2026-10-24 21:14:44.780902
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:14:47.199370
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:14:49.613848
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:14:52.032471
# Unit test for method __repr__ of class _Undefined

# Generated at 2026-10-24 21:14:53.406225
# Unit test for method __repr__ of class _Undefined
def test__Undefined___repr__():
    u = _Undefined()
    assert repr(u) == 'undefined'
    assert u.__repr__() == 'undefined'
    assert repr(_Undefined()) == 'undefined'
    assert str(u) == 'undefined'

# Generated at 2026-10-24 21:14:54.812217
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

# Generated at 2026-10-24 21:15:00.548128
# Unit test for constructor of class _AVMClass_Object
def test__AVMClass_Object():
    avm_class = type('MockAVMClass', (object,), {'name': 'TestClass'})()

    obj = _AVMClass_Object(avm_class)

    assert obj.avm_class is avm_class
    assert repr(obj) == 'TestClass#%x' % id(obj)

# Generated at 2026-10-24 21:15:27.792351
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-24 21:15:30.213117
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-24 21:15:32.633219
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-24 21:15:36.617057
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-24 21:15:39.032402
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-24 21:15:41.453284
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-24 21:15:43.870691
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:15:46.288528
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:15:48.707991
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:15:51.125978
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-24 21:15:53.543439
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-24 21:15:55.963626
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-24 21:15:58.379558
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-24 21:16:00.798970
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-24 21:16:03.217763
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-24 21:16:06.026545
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:16:21.964907
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():interpreter = object.__new__(SWFInterpreter)


# Generated at 2026-10-24 21:16:32.612520
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():interpreter = object.__new__(SWFInterpreter)

# Generated at 2026-10-24 21:16:43.226832
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    interpreter = SWFInterpreter.__new__(SWFInterpreter)

    original = lambda args: 'original'
    replacement = lambda args: 'replacement'
    unrelated = lambda args: 'unrelated'

    avm_class = type('MockAVMClass', (), {})()
    avm_class.method_pyfunctions = {
        'target': original,
        'other': unrelated,
    }

    result = interpreter.patch_function(avm_class, 'target', replacement)

    assert result is None
    assert avm_class.method_pyfunctions['target'] is replacement
    assert avm_class.method_pyfunctions['target']([]) == 'replacement'
    assert avm_class.method_pyfunctions['other'] is unrelated

# Generated at 2026-10-24 21:16:45.646872
# Unit test for method make_object of class _AVMClass

# Generated at 2026-10-24 21:16:48.062642
# Unit test for method make_object of class _AVMClass

# Generated at 2026-10-24 21:16:50.595654
# Unit test for method make_object of class _AVMClass

# Generated at 2026-10-24 21:16:53.013847
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-24 21:16:55.431033
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-24 21:16:57.848604
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-24 21:17:00.266599
# Unit test for method make_object of class _AVMClass

# Generated at 2026-10-24 21:17:02.684654
# Unit test for method make_object of class _AVMClass

# Generated at 2026-10-24 21:17:05.103279
# Unit test for method make_object of class _AVMClass

# Generated at 2026-10-24 21:17:12.751634
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

# Generated at 2026-10-24 21:17:15.529036
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:17:30.365499
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():interpreter = SWFInterpreter.__new__(SWFInterpreter)

# Generated at 2026-10-24 21:17:32.787965
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:17:35.204826
# Unit test for method register_methods of class _AVMClass

# Generated at 2026-10-24 21:17:37.631308
# Unit test for method register_methods of class _AVMClass

# Generated at 2026-10-24 21:17:40.153534
# Unit test for method register_methods of class _AVMClass

# Generated at 2026-10-24 21:17:42.569898
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:17:44.987395
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:17:47.405077
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:17:49.821911
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:17:52.243480
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:17:54.665542
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:17:57.085739
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-24 21:17:59.501875
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-24 21:18:01.918066
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-24 21:18:04.335790
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-24 21:18:06.752569
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-24 21:18:09.167845
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-24 21:18:11.966309
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:18:26.811730
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():interpreter = SWFInterpreter.__new__(SWFInterpreter)

# Generated at 2026-10-24 21:18:41.638645
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():interpreter = SWFInterpreter.__new__(SWFInterpreter)

# Generated at 2026-10-24 21:18:44.197208
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-24 21:18:46.754758
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-24 21:18:49.172017
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-24 21:18:51.591424
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:18:54.013626
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:18:56.429895
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:18:58.847119
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-24 21:19:01.265394
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-24 21:19:03.683823
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-24 21:19:07.216482
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-24 21:19:09.635297
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-24 21:19:12.051663
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-24 21:19:14.469993
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-24 21:19:16.887007
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-24 21:19:19.306474
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-24 21:19:21.720887
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-24 21:19:24.137312
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-24 21:19:26.555239
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-24 21:19:27.912931
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

# Generated at 2026-10-24 21:19:30.698438
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:19:44.820221
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:19:56.489880
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():interpreter = object.__new__(SWFInterpreter)

# Generated at 2026-10-24 21:19:58.910687
# Unit test for method register_methods of class _AVMClass

# Generated at 2026-10-24 21:20:01.328112
# Unit test for method register_methods of class _AVMClass

# Generated at 2026-10-24 21:20:03.748350
# Unit test for method register_methods of class _AVMClass

# Generated at 2026-10-24 21:20:06.166855
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-24 21:20:08.777879
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-24 21:20:11.166598
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-24 21:20:13.585347
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-24 21:20:16.005099
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-24 21:20:18.426777
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-24 21:20:20.844908
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:20:23.265512
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:20:25.688198
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:20:28.337343
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:20:40.967235
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():from types import SimpleNamespace


# Generated at 2026-10-24 21:20:45.310004
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-24 21:21:16.567292
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-24 21:21:18.988699
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-24 21:21:21.583818
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:21:24.001626
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:21:26.421980
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:21:28.837625
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-24 21:21:31.255050
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-24 21:21:33.671580
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-24 21:21:36.091875
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:21:38.507716
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:21:40.922839
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:21:43.340117
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-24 21:21:45.757252
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-24 21:21:48.175252
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-24 21:21:50.597825
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-24 21:21:53.016349
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-24 21:22:03.472703
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():interpreter = SWFInterpreter.__new__(SWFInterpreter)

# Generated at 2026-10-24 21:22:09.143956
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-24 21:22:37.056583
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-24 21:22:39.627646
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-24 21:22:42.044699
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-24 21:22:44.461745
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-24 21:22:46.880640
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-24 21:22:49.298194
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-24 21:22:51.717979
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-24 21:22:54.131005
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-24 21:22:56.549525
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:22:58.968168
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:23:01.386360
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:23:33.378906
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():interpreter = SWFInterpreter.__new__(SWFInterpreter)


# Generated at 2026-10-24 21:23:58.448246
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-24 21:24:00.864150
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-24 21:24:03.282419
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:24:05.703312
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:24:23.300995
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 21:24:50.686858
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-24 21:24:53.106022
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-24 21:24:55.522147
# Unit test for method patch_function of class SWFInterpreter