

# Generated at 2026-10-25 06:57:07.091151
# Unit test for constructor of class _Multiname
def test__Multiname():
    kind = 0x07
    obj = _Multiname(kind)

    assert isinstance(obj, _Multiname)
    assert obj.kind == kind
    assert repr(obj) == '[MULTINAME kind: 0x%x]' % kind

# Generated at 2026-10-25 06:57:10.057538
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:57:12.997800
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:57:15.847561
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:57:17.270931
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

# Generated at 2026-10-25 06:57:26.149338
# Unit test for method make_object of class _AVMClass
def test__AVMClass_make_object():
    avm_class = _AVMClass(name_idx=1, name='TestClass')
    obj = avm_class.make_object()

    assert isinstance(obj, _AVMClass_Object)
    assert obj.avm_class is avm_class

    # Each call should create a new distinct object
    obj2 = avm_class.make_object()
    assert isinstance(obj2, _AVMClass_Object)
    assert obj2 is not obj
    assert obj2.avm_class is avm_class

# Generated at 2026-10-25 06:57:28.566484
# Unit test for method __repr__ of class _Multiname

# Generated at 2026-10-25 06:57:30.981768
# Unit test for method __repr__ of class _Multiname

# Generated at 2026-10-25 06:57:33.396274
# Unit test for method __repr__ of class _Multiname

# Generated at 2026-10-25 06:57:36.540066
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 06:57:38.954370
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 06:57:41.694456
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 06:57:44.102833
# Unit test for method __repr__ of class _Undefined

# Generated at 2026-10-25 06:57:46.516525
# Unit test for method __repr__ of class _Undefined

# Generated at 2026-10-25 06:57:48.930508
# Unit test for method __repr__ of class _Undefined

# Generated at 2026-10-25 06:57:51.347171
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 06:57:53.758816
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 06:57:56.173447
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 06:57:58.587665
# Unit test for method __hash__ of class _Undefined

# Generated at 2026-10-25 06:58:01.001307
# Unit test for method __hash__ of class _Undefined

# Generated at 2026-10-25 06:58:03.421826
# Unit test for method __hash__ of class _Undefined

# Generated at 2026-10-25 06:58:30.251281
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:58:33.120385
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:58:35.944605
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 06:58:43.463218
# Unit test for method __bool__ of class _Undefined
def test__Undefined___bool__():
    assert bool(_Undefined()) is False
    assert not _Undefined()
    # __nonzero__ is the Python 2 alias; must behave identically
    assert _Undefined().__nonzero__() is False
    # sanity: it is still a real object, not None
    assert _Undefined() is not None

# Generated at 2026-10-25 06:58:44.896575
# Unit test for method __repr__ of class _Undefined
def test__Undefined___repr__():
    u = _Undefined()
    assert repr(u) == 'undefined'
    assert u.__repr__() == 'undefined'
    assert repr(_Undefined()) == 'undefined'
    # __repr__ is bound to __str__
    assert repr(u) == str(u)

# Generated at 2026-10-25 06:58:46.337018
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

# Generated at 2026-10-25 06:58:56.159001
# Unit test for method __repr__ of class _Undefined
def test__Undefined___repr__():
    undef = _Undefined()
    assert repr(undef) == 'undefined'
    assert undef.__repr__() == 'undefined'
    assert undef.__repr__() == str(undef)
    assert _Undefined.__repr__ is _Undefined.__str__

# Generated at 2026-10-25 06:58:58.576749
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 06:59:00.991625
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 06:59:03.406018
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 06:59:28.863596
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 06:59:51.149727
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 06:59:53.793531
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 06:59:56.210470
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 06:59:58.628980
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:00:01.044263
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:00:03.458306
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:00:06.223692
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:00:09.163098
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:00:12.344586
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:00:15.520606
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:00:18.693658
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:00:22.186822
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:00:25.147058
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    from youtube_dl.swfinterp import SWFInterpreter

    assert hasattr(SWFInterpreter, 'patch_function'), (
        'SWFInterpreter.patch_function is not defined in the supplied source: '
        'the fragment ends inside extract_function, whose tail is '
        '"avm_class.method_pyfunctions[func_name] = resfunc; return resfunc". '
        'Supply the real patch_function definition before testing it.')

    assert callable(SWFInterpreter.patch_function)

# Generated at 2026-10-25 07:00:28.202893
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:00:31.302184
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:00:34.244753
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:00:37.035260
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:00:39.448757
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:00:42.235818
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:00:44.650909
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:00:47.269381
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:00:49.865857
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:00:52.278781
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:00:54.692030
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:00:57.105410
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:00:59.519757
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:01:01.945549
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:01:04.354594
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:01:07.204627
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:01:09.665344
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:01:12.073778
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:01:14.488308
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:01:16.904100
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:01:19.319214
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:01:21.735413
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:01:24.153965
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:01:26.692522
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:01:29.099507
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:01:32.527369
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:01:35.600394
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:01:38.567148
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:01:41.541458
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    from youtube_dl.swfinterp import SWFInterpreter

    assert hasattr(SWFInterpreter, 'patch_function'), (
        'SWFInterpreter.patch_function is not defined in the supplied source: '
        'the fragment ends inside extract_function, whose tail is '
        '"avm_class.method_pyfunctions[func_name] = resfunc; return resfunc". '
        'Supply the real patch_function definition before testing it.')

    assert callable(SWFInterpreter.patch_function)

# Generated at 2026-10-25 07:01:59.563321
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:02:02.511568
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:02:05.499830
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:02:08.142439
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:02:10.912820
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:02:13.328823
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:02:15.747158
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:02:18.502637
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:02:20.932090
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:02:23.596553
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:02:26.009096
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:02:28.426273
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:02:31.149897
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:02:34.001335
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    from youtube_dl.swfinterp import SWFInterpreter

    assert hasattr(SWFInterpreter, 'patch_function'), (
        'SWFInterpreter.patch_function is not defined in the supplied source: '
        'the fragment ends inside extract_function, whose tail is '
        '"avm_class.method_pyfunctions[func_name] = resfunc; return resfunc". '
        'Supply the real patch_function definition before testing it.')

    assert callable(SWFInterpreter.patch_function)

# Generated at 2026-10-25 07:02:39.279316
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:02:42.174112
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    from youtube_dl.swfinterp import SWFInterpreter

    assert hasattr(SWFInterpreter, 'patch_function'), (
        'SWFInterpreter.patch_function is not defined in the supplied source: '
        'the fragment ends inside extract_function, whose tail is '
        '"avm_class.method_pyfunctions[func_name] = resfunc; return resfunc". '
        'Supply the real patch_function definition before testing it.')

    assert callable(SWFInterpreter.patch_function)

# Generated at 2026-10-25 07:03:00.282506
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:03:03.032443
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:03:05.911273
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:03:08.580759
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:03:10.996941
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:03:13.444404
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:03:15.833707
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:03:18.462044
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:03:20.873235
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:03:23.292940
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:03:25.710489
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:03:28.124461
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:03:30.614489
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:03:33.029520
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:03:35.446442
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:03:37.866143
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:03:40.278458
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:03:42.691463
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:03:45.105849
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:03:47.520681
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:03:49.942455
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:03:52.357306
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:03:54.775599
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:03:57.290099
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:03:59.706390
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:04:02.123936
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:04:04.539671
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:04:12.775362
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:04:15.189032
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:04:17.607306
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:04:20.019218
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:04:22.435867
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:04:24.850395
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:04:27.265187
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:04:29.678820
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:04:32.093752
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:04:34.506499
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:04:36.919604
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:04:39.334721
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:04:41.750605
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:04:44.165772
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:04:46.580026
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:04:49.013737
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:04:51.427921
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:04:53.841422
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:04:56.256116
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:04:58.669355
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:05:01.084483
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:05:03.498504
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:05:05.912678
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:05:08.327760
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:05:10.742715
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:05:13.156710
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:05:15.569725
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:05:17.982168
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:05:20.397928
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:05:22.808727
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:05:38.287310
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:05:41.257681
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    from youtube_dl.swfinterp import SWFInterpreter

    assert hasattr(SWFInterpreter, 'patch_function'), (
        'SWFInterpreter.patch_function is not defined in the supplied source: '
        'the fragment ends inside extract_function, whose tail is '
        '"avm_class.method_pyfunctions[func_name] = resfunc; return resfunc". '
        'Supply the real patch_function definition before testing it.')

    assert callable(SWFInterpreter.patch_function)

# Generated at 2026-10-25 07:05:42.693112
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

# Generated at 2026-10-25 07:05:46.172578
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:05:49.246699
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:05:51.663639
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:05:54.260570
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:05:56.804609
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:05:59.390937
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:06:01.804165
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:06:04.217143
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:06:06.633143
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:06:09.048873
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:06:11.462603
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:06:13.878040
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 07:06:16.292398
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:06:18.706040
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:06:21.122352
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:06:23.538484
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:06:26.159289
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:06:28.574078
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 07:06:31.001955
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:06:33.403461
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:06:35.817279
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:06:38.232330
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:06:40.648996
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:06:43.063832
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:06:55.861735
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:06:58.275926
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:07:00.693966
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 07:07:03.106481
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:07:05.521380
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 07:07:07.939435
# Unit test for method extract_function of class SWFInterpreter