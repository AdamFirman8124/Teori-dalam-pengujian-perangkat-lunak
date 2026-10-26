

# Generated at 2026-10-25 07:14:54.222316
# Unit test for constructor of class _Multiname
def test__Multiname():
    kind = 0x07
    obj = _Multiname(kind)

    assert isinstance(obj, _Multiname)
    assert obj.kind == kind
    assert repr(obj) == '[MULTINAME kind: 0x%x]' % kind

# Generated at 2026-10-25 07:15:30.369835
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:15:32.790946
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:15:35.207898
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:15:37.627668
# Unit test for constructor of class _AVMClass

# Generated at 2026-10-25 07:15:40.041482
# Unit test for constructor of class _AVMClass

# Generated at 2026-10-25 07:15:42.456904
# Unit test for constructor of class _AVMClass

# Generated at 2026-10-25 07:15:44.873078
# Unit test for constructor of class _Undefined

# Generated at 2026-10-25 07:15:47.290361
# Unit test for constructor of class _Undefined

# Generated at 2026-10-25 07:15:49.704941
# Unit test for constructor of class _Undefined

# Generated at 2026-10-25 07:15:52.120713
# Unit test for constructor of class _AVMClass_Object

# Generated at 2026-10-25 07:16:07.129501
# Unit test for constructor of class _AVMClass_Object

# Generated at 2026-10-25 07:16:18.691218
# Unit test for constructor of class _AVMClass_Object
def test__AVMClass_Object():mock_avm_class = type('FakeAVMClass', (), {'name': 'TestClass'})()

# Generated at 2026-10-25 07:16:38.024852
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:16:40.442730
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:16:42.856856
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:16:45.272461
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:16:47.687029
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:16:50.102460
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:16:52.516309
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:16:55.363691
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:16:58.238331
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:16:59.662424
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

# Generated at 2026-10-25 07:17:01.013331
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

# Generated at 2026-10-25 07:17:03.949813
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:17:07.138582
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    from youtube_dl.swfinterp import SWFInterpreter

    assert hasattr(SWFInterpreter, 'patch_function'), (
        'SWFInterpreter.patch_function is not defined in the supplied source: '
        'the fragment ends inside extract_function, whose tail is '
        '"avm_class.method_pyfunctions[func_name] = resfunc; return resfunc". '
        'Supply the real patch_function definition before testing it.')

    assert callable(SWFInterpreter.patch_function)

# Generated at 2026-10-25 07:17:08.499541
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

# Generated at 2026-10-25 07:17:09.861085
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

# Generated at 2026-10-25 07:17:12.850670
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:17:15.782213
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:17:18.462657
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:17:20.877306
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:17:23.296240
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:17:25.710597
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:17:28.126250
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:17:30.544870
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:17:32.960396
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:17:35.411282
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:17:37.828487
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:17:40.241318
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:17:42.808058
# Unit test for method register_methods of class _AVMClass

# Generated at 2026-10-25 07:17:45.219010
# Unit test for method register_methods of class _AVMClass

# Generated at 2026-10-25 07:17:47.633599
# Unit test for method register_methods of class _AVMClass

# Generated at 2026-10-25 07:17:50.048416
# Unit test for method register_methods of class _AVMClass

# Generated at 2026-10-25 07:17:52.463155
# Unit test for method register_methods of class _AVMClass

# Generated at 2026-10-25 07:17:54.880640
# Unit test for method register_methods of class _AVMClass

# Generated at 2026-10-25 07:17:57.293608
# Unit test for method register_methods of class _AVMClass

# Generated at 2026-10-25 07:17:59.712046
# Unit test for method register_methods of class _AVMClass

# Generated at 2026-10-25 07:18:02.128230
# Unit test for method register_methods of class _AVMClass

# Generated at 2026-10-25 07:18:04.541376
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:18:06.955992
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:18:09.372329
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:18:11.787257
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:18:14.201794
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:18:16.616073
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:18:19.029372
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:18:21.442875
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:18:23.856426
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:18:26.273174
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:18:28.738462
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:18:31.147996
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:18:33.562950
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:18:35.976244
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:18:38.391144
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:18:40.804854
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:18:43.217860
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:18:45.634287
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:18:48.051474
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:18:50.465777
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:18:52.880448
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:18:55.295162
# Unit test for method register_methods of class _AVMClass

# Generated at 2026-10-25 07:18:57.711088
# Unit test for method register_methods of class _AVMClass

# Generated at 2026-10-25 07:19:00.160073
# Unit test for method register_methods of class _AVMClass

# Generated at 2026-10-25 07:19:02.571806
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:19:04.982909
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:19:07.398638
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:19:09.818627
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:19:12.236071
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:19:14.653317
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:19:17.069426
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:19:19.487368
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:19:21.902243
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:19:24.320555
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:19:26.737614
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:19:29.152611
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:19:31.568899
# Unit test for method register_methods of class _AVMClass

# Generated at 2026-10-25 07:19:33.987551
# Unit test for method register_methods of class _AVMClass

# Generated at 2026-10-25 07:19:36.405968
# Unit test for method register_methods of class _AVMClass

# Generated at 2026-10-25 07:19:38.816375
# Unit test for method __repr__ of class _AVMClass

# Generated at 2026-10-25 07:19:41.231987
# Unit test for method __repr__ of class _AVMClass

# Generated at 2026-10-25 07:19:43.655080
# Unit test for method __repr__ of class _AVMClass

# Generated at 2026-10-25 07:19:46.070365
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:19:48.486316
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:19:50.906221
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:19:53.830098
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:19:56.248821
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:19:58.664308
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:20:01.079747
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:20:03.496247
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:20:05.913675
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:20:08.331507
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:20:10.745203
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:20:13.163446
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:20:15.575330
# Unit test for method __repr__ of class _AVMClass

# Generated at 2026-10-25 07:20:17.993524
# Unit test for method __repr__ of class _AVMClass

# Generated at 2026-10-25 07:20:20.404341
# Unit test for method __repr__ of class _AVMClass

# Generated at 2026-10-25 07:20:22.818226
# Unit test for method register_methods of class _AVMClass

# Generated at 2026-10-25 07:20:25.233131
# Unit test for method register_methods of class _AVMClass

# Generated at 2026-10-25 07:20:27.651268
# Unit test for method register_methods of class _AVMClass

# Generated at 2026-10-25 07:20:30.070005
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:20:32.484794
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:20:34.902095
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:20:37.321249
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:20:39.737155
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:20:42.153826
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:20:44.568774
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:20:46.983203
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:20:49.397506
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:20:51.815923
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:20:54.234159
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:20:56.646686
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:20:59.066956
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:21:01.483916
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:21:03.898183
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:21:11.747878
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:21:14.165566
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:21:16.583007
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:21:19.075439
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:21:21.480033
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:21:23.897447
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:21:26.314027
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:21:28.727252
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:21:31.134307
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:21:33.551143
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:21:35.985261
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:21:38.398194
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:21:40.812563
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:21:43.226508
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:21:45.640051
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:21:48.055115
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:21:50.497972
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:21:52.891077
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:21:55.303850
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:21:57.716897
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:22:00.723458
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    from youtube_dl.swfinterp import SWFInterpreter

    assert hasattr(SWFInterpreter, 'patch_function'), (
        'SWFInterpreter.patch_function is not defined in the supplied source: '
        'the fragment ends inside extract_function, whose tail is '
        '"avm_class.method_pyfunctions[func_name] = resfunc; return resfunc". '
        'Supply the real patch_function definition before testing it.')

    assert callable(SWFInterpreter.patch_function)

# Generated at 2026-10-25 07:22:02.257874
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

# Generated at 2026-10-25 07:22:03.689728
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

# Generated at 2026-10-25 07:22:05.083426
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

# Generated at 2026-10-25 07:22:12.160568
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:22:15.073462
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    from youtube_dl.swfinterp import SWFInterpreter

    assert hasattr(SWFInterpreter, 'patch_function'), (
        'SWFInterpreter.patch_function is not defined in the supplied source: '
        'the fragment ends inside extract_function, whose tail is '
        '"avm_class.method_pyfunctions[func_name] = resfunc; return resfunc". '
        'Supply the real patch_function definition before testing it.')

    assert callable(SWFInterpreter.patch_function)

# Generated at 2026-10-25 07:22:17.819918
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:22:20.379415
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:22:22.795230
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:22:25.215823
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:22:27.628300
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:22:30.426012
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:22:32.841809
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:22:35.255549
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:22:37.668534
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:22:40.084708
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:22:42.557061
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:22:44.975179
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:22:47.388866
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:22:49.806880
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:22:52.218759
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:22:54.635623
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:22:57.050629
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:22:59.468151
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:23:01.882738
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:23:04.295654
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:23:06.709740
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:23:09.129349
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:23:11.544999
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:23:14.015400
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:23:16.424537
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:23:18.839716
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:23:21.260276
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:23:26.950620
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:23:29.364638
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:23:31.778956
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:23:34.193295
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:23:36.608224
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:23:39.024361
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:23:41.440607
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:23:43.851073
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:23:46.266319
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:23:48.681226
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:23:51.447857
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:23:54.483194
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:24:12.406947
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:24:14.827408
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:24:17.246645
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:24:19.659547
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:24:22.078697
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:24:24.493335
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:24:26.908729
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:24:29.326485
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:24:31.741765
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:24:34.155013
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:24:36.572449
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:24:38.991665
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:24:41.405078
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:24:43.821992
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:24:46.239554
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:24:48.655948
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:24:51.069898
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:24:53.487707
# Unit test for method extract_class of class SWFInterpreter