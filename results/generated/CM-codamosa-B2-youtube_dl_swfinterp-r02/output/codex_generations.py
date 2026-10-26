

# Generated at 2026-10-25 06:05:11.257373
# Unit test for constructor of class _ScopeDict
def test__ScopeDict():
    class FakeAVMClass(object):
        def __init__(self, name='TestClass'):
            self.name = name

    fake_class = FakeAVMClass()

    scope = _ScopeDict(fake_class)

    # is a dict, initialized empty
    assert isinstance(scope, dict)
    assert isinstance(scope, _ScopeDict)
    assert len(scope) == 0
    assert dict(scope) == {}
    assert list(scope.keys()) == []

    # stores class reference
    assert scope.avm_class is fake_class

    # dict behavior still works and is instance-local
    scope['x'] = 1
    assert scope['x'] == 1
    other = _ScopeDict(fake_class)
    assert other == {}
    assert 'x' not in other

# Generated at 2026-10-25 06:05:12.648082
# Unit test for constructor of class _ScopeDict

# Generated at 2026-10-25 06:05:13.998047
# Unit test for constructor of class _ScopeDict

# Generated at 2026-10-25 06:05:15.480866
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

# Generated at 2026-10-25 06:05:16.919794
# Unit test for constructor of class _Multiname
def test__Multiname():
    kind = 0x07
    obj = _Multiname(kind)

    assert isinstance(obj, _Multiname)
    assert obj.kind == kind
    assert repr(obj) == '[MULTINAME kind: 0x%x]' % kind

# Generated at 2026-10-25 06:05:19.747517
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 06:05:42.587109
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 06:05:46.267749
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 06:05:49.107763
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:06:12.471524
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:06:14.889477
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:06:17.309664
# Unit test for method __repr__ of class _AVMClass

# Generated at 2026-10-25 06:06:19.726338
# Unit test for method __repr__ of class _AVMClass

# Generated at 2026-10-25 06:06:22.145427
# Unit test for method __repr__ of class _AVMClass

# Generated at 2026-10-25 06:06:32.413309
# Unit test for method __repr__ of class _AVMClass_Object

# Generated at 2026-10-25 06:06:39.033923
# Unit test for method __repr__ of class _AVMClass_Object

# Generated at 2026-10-25 06:06:40.449367
# Unit test for method __repr__ of class _AVMClass_Object

# Generated at 2026-10-25 06:06:41.876220
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

# Generated at 2026-10-25 06:06:43.229947
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

# Generated at 2026-10-25 06:06:50.172773
# Unit test for method __repr__ of class _AVMClass
def test__AVMClass___repr__():
    avm_class = _AVMClass(123, 'SomeClass')
    assert repr(avm_class) == '_AVMClass(SomeClass)', repr(avm_class)

    # repr depends only on name, not name_idx or registered methods
    avm_class.register_methods({'someMethod': 456})
    assert repr(avm_class) == '_AVMClass(SomeClass)', repr(avm_class)

    # name is embedded verbatim
    avm_class2 = _AVMClass(1, 'flash.display::Sprite')
    assert repr(avm_class2) == '_AVMClass(flash.display::Sprite)', repr(avm_class2)

    print('test__AVMClass___repr__ passed')

# Generated at 2026-10-25 06:06:52.591282
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:06:55.010598
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:06:57.427853
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:06:59.846014
# Unit test for method make_object of class _AVMClass

# Generated at 2026-10-25 06:07:02.262150
# Unit test for method make_object of class _AVMClass

# Generated at 2026-10-25 06:07:05.000054
# Unit test for method make_object of class _AVMClass

# Generated at 2026-10-25 06:07:07.415273
# Unit test for constructor of class _AVMClass_Object

# Generated at 2026-10-25 06:07:09.832176
# Unit test for constructor of class _AVMClass_Object

# Generated at 2026-10-25 06:07:12.251148
# Unit test for constructor of class _AVMClass_Object

# Generated at 2026-10-25 06:07:14.688072
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:07:17.102756
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:07:19.521155
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:07:22.164315
# Unit test for method __repr__ of class _AVMClass

# Generated at 2026-10-25 06:07:24.585135
# Unit test for method __repr__ of class _AVMClass

# Generated at 2026-10-25 06:07:27.005192
# Unit test for method __repr__ of class _AVMClass

# Generated at 2026-10-25 06:07:29.421631
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 06:07:31.847627
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 06:07:34.363814
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 06:07:36.778966
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 06:07:39.410198
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 06:07:42.489494
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 06:07:45.723951
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 06:07:48.748188
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 06:07:51.735706
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 06:07:53.151150
# Unit test for method __repr__ of class _AVMClass_Object

# Generated at 2026-10-25 06:07:54.626376
# Unit test for method __repr__ of class _AVMClass_Object

# Generated at 2026-10-25 06:07:56.018892
# Unit test for method __repr__ of class _AVMClass_Object

# Generated at 2026-10-25 06:07:58.797847
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:08:01.854950
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:08:04.394047
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:08:06.808808
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 06:08:09.223711
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 06:08:11.967412
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 06:08:14.384137
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 06:08:16.802212
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 06:08:19.219540
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 06:08:21.883897
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 06:08:24.298855
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 06:08:26.713895
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 06:08:29.130384
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 06:08:31.662265
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 06:08:33.996220
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 06:08:36.411954
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:08:39.108772
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:08:41.860278
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:08:44.769131
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 06:08:47.628095
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 06:08:50.495797
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 06:09:05.853365
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 06:09:08.218261
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 06:09:10.634858
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 06:09:13.124711
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 06:09:15.717668
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 06:09:18.134522
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 06:09:20.551357
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 06:09:22.969136
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 06:09:25.383120
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 06:09:27.807520
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 06:09:30.217899
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 06:09:32.630192
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 06:09:35.044677
# Unit test for method __repr__ of class _AVMClass_Object

# Generated at 2026-10-25 06:09:37.457545
# Unit test for method __repr__ of class _AVMClass_Object

# Generated at 2026-10-25 06:09:39.872172
# Unit test for method __repr__ of class _AVMClass_Object

# Generated at 2026-10-25 06:09:42.287735
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:09:44.703379
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:09:47.117200
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:09:49.531605
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 06:09:51.948416
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 06:09:54.365468
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 06:09:56.862803
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 06:09:59.611359
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 06:10:02.498009
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 06:10:03.906905
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

# Generated at 2026-10-25 06:10:25.326539
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 06:10:27.742213
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 06:10:30.557508
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 06:10:32.975339
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 06:10:35.390591
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 06:10:37.808253
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 06:10:40.221764
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 06:10:42.637892
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 06:10:45.054143
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 06:10:47.467996
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 06:10:49.884024
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 06:10:52.298682
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 06:10:54.712840
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 06:10:57.129056
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 06:10:59.679222
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 06:11:02.020194
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:11:04.438312
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:11:06.854077
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:11:09.269387
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 06:11:11.684569
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 06:11:14.101584
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 06:11:16.611056
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 06:11:19.028940
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 06:11:35.370689
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    from youtube_dl.swfinterp import SWFInterpreter

    assert hasattr(SWFInterpreter, 'patch_function'), (
        'SWFInterpreter.patch_function is not defined in the supplied source: '
        'the fragment ends inside extract_function, whose tail is '
        '"avm_class.method_pyfunctions[func_name] = resfunc; return resfunc". '
        'Supply the real patch_function definition before testing it.')

    assert callable(SWFInterpreter.patch_function)

# Generated at 2026-10-25 06:11:38.155178
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 06:11:41.109785
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 06:11:43.972287
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 06:11:46.596000
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:11:49.011167
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:11:51.429068
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:11:55.497480
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:11:57.988107
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:12:00.403445
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:12:02.818328
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:12:05.235963
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:12:07.652414
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:12:10.516786
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:12:13.668036
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:12:16.637794
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:12:18.174410
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

# Generated at 2026-10-25 06:12:21.243974
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 06:12:24.213515
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 06:12:27.348289
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 06:12:30.027101
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 06:12:32.682320
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 06:12:35.097034
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 06:12:37.512478
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:12:39.928457
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:12:42.346427
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:12:44.945341
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:12:47.364492
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:12:49.782973
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:12:52.199900
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:12:54.614301
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:12:57.029925
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:12:59.444222
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 06:13:01.860388
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 06:13:04.272850
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 06:13:11.925571
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 06:13:14.345417
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 06:13:16.762196
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 06:13:19.904446
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:13:22.789225
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:13:25.757820
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:13:27.192952
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

# Generated at 2026-10-25 06:13:30.042648
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 06:13:52.621078
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 06:13:55.294740
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 06:13:57.710625
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:14:00.127561
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:14:02.556465
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:14:04.973546
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 06:14:07.387775
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 06:14:09.802989
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 06:14:12.220022
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 06:14:14.634531
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 06:14:17.047846
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 06:14:19.464985
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 06:14:21.879239
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 06:14:24.296248
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 06:14:26.708959
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 06:14:29.128038
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 06:14:31.543001
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 06:14:33.959196
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:14:36.373658
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:14:38.937237
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:14:46.835889
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

# Generated at 2026-10-25 06:14:49.634013
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 06:14:52.418893
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    from youtube_dl.swfinterp import SWFInterpreter

    assert hasattr(SWFInterpreter, 'patch_function'), (
        'SWFInterpreter.patch_function is not defined in the supplied source: '
        'the fragment ends inside extract_function, whose tail is '
        '"avm_class.method_pyfunctions[func_name] = resfunc; return resfunc". '
        'Supply the real patch_function definition before testing it.')

    assert callable(SWFInterpreter.patch_function)

# Generated at 2026-10-25 06:14:55.256517
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:14:58.129115
# Unit test for method extract_function of class SWFInterpreter