

# Generated at 2026-10-25 02:22:28.115853
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

# Generated at 2026-10-25 02:22:35.074597
# Unit test for constructor of class _ScopeDict
def test__ScopeDict():
    class DummyAVMClass(object):
        name = 'TestClass'

    avm_class = DummyAVMClass()
    scope = _ScopeDict(avm_class)

    assert isinstance(scope, dict)
    assert scope == {}
    assert scope.avm_class is avm_class

# Generated at 2026-10-25 02:22:42.230708
# Unit test for method __repr__ of class _Multiname
def test__Multiname___repr__():
    multiname = _Multiname(0x1A)
    assert repr(multiname) == '[MULTINAME kind: 0x1a]'

# Generated at 2026-10-25 02:22:43.662216
# Unit test for constructor of class _Multiname
def test__Multiname():
    kind = 0x07
    obj = _Multiname(kind)

    assert isinstance(obj, _Multiname)
    assert obj.kind == kind
    assert repr(obj) == '[MULTINAME kind: 0x%x]' % kind

# Generated at 2026-10-25 02:22:49.192363
# Unit test for constructor of class _ScopeDict
def test__ScopeDict():
    class DummyAVMClass(object):
        name = 'DummyClass'

    avm_class = DummyAVMClass()
    scope = _ScopeDict(avm_class)

    assert isinstance(scope, dict)
    assert scope == {}
    assert scope.avm_class is avm_class

# Generated at 2026-10-25 02:22:52.458177
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 02:22:54.870911
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 02:22:57.286161
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 02:22:59.702835
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 02:23:02.241969
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 02:23:04.657172
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 02:23:07.071318
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 02:23:09.491718
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 02:23:38.098842
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 02:23:58.725324
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    interpreter = object.__new__(SWFInterpreter)

    sentinel_result = object()

    def cached_function(args):
        assert args == [1, 2]
        return sentinel_result

    avm_class = type('FakeAVMClass', (), {
        'method_pyfunctions': {'testMethod': cached_function},
    })()

    extracted = interpreter.extract_function(avm_class, 'testMethod')

    assert extracted is cached_function
    assert extracted([1, 2]) is sentinel_result

# Generated at 2026-10-25 02:24:01.142317
# Unit test for method register_methods of class _AVMClass

# Generated at 2026-10-25 02:24:03.558247
# Unit test for method register_methods of class _AVMClass

# Generated at 2026-10-25 02:24:05.973954
# Unit test for method register_methods of class _AVMClass

# Generated at 2026-10-25 02:24:08.390054
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 02:24:10.804351
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 02:24:13.220590
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 02:24:16.132410
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 02:24:43.587782
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 02:24:46.018101
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 02:24:48.550359
# Unit test for method register_methods of class _AVMClass

# Generated at 2026-10-25 02:24:50.967692
# Unit test for method register_methods of class _AVMClass

# Generated at 2026-10-25 02:24:53.380525
# Unit test for method register_methods of class _AVMClass

# Generated at 2026-10-25 02:24:55.795747
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 02:24:58.211546
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 02:25:00.866039
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 02:25:03.282690
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 02:25:05.701477
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 02:25:08.114690
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 02:25:10.529121
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 02:25:12.944818
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 02:25:15.901338
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 02:25:17.257256
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

# Generated at 2026-10-25 02:25:42.953192
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 02:25:57.416112
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 02:25:59.822578
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 02:26:02.246920
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 02:26:04.662415
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 02:26:07.078052
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 02:26:09.497342
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 02:26:11.910422
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 02:26:14.324974
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 02:26:16.739526
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 02:26:19.154801
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 02:26:21.570128
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 02:26:23.985385
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 02:26:26.400518
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 02:26:28.815527
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 02:26:31.232091
# Unit test for method register_methods of class _AVMClass

# Generated at 2026-10-25 02:26:33.646897
# Unit test for method register_methods of class _AVMClass

# Generated at 2026-10-25 02:26:36.063747
# Unit test for method register_methods of class _AVMClass

# Generated at 2026-10-25 02:26:38.481978
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 02:26:40.897667
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 02:26:43.314095
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 02:26:45.727698
# Unit test for method register_methods of class _AVMClass

# Generated at 2026-10-25 02:26:50.553169
# Unit test for method register_methods of class _AVMClass
def test__AVMClass_register_methods():avm_class = _AVMClass(1, 'Example')

# Generated at 2026-10-25 02:26:53.417000
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 02:27:18.710524
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():import importlib

# Generated at 2026-10-25 02:27:39.204169
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    """extract_function should return an already compiled function unchanged."""
    interpreter = object.__new__(SWFInterpreter)

    def cached_function(args):
        return args[0] + args[1]

    avm_class = SimpleNamespace(
        method_pyfunctions={'add': cached_function},
    )

    extracted = interpreter.extract_function(avm_class, 'add')

    assert extracted is cached_function
    assert extracted([2, 3]) == 5

# Generated at 2026-10-25 02:27:41.649814
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 02:27:44.583291
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 02:27:47.332063
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 02:27:50.147706
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 02:28:17.743888
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 02:28:31.501066
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():import pytest


# Generated at 2026-10-25 02:28:34.043562
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 02:28:36.459992
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 02:28:38.885825
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 02:28:41.301136
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 02:28:43.716130
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 02:29:08.793225
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 02:29:32.139577
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 02:29:34.560733
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 02:29:36.976830
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 02:29:39.392519
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 02:29:41.808075
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 02:29:44.235052
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 02:29:46.661348
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 02:29:49.077257
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 02:29:51.506263
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 02:29:53.921168
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 02:29:56.339350
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 02:29:58.764114
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 02:30:01.734026
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 02:30:30.817415
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 02:30:33.354843
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 02:30:35.776228
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 02:30:38.185718
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 02:30:40.602350
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 02:30:43.192580
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 02:30:45.606498
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 02:30:48.020438
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 02:30:50.435633
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 02:30:53.024645
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 02:30:55.454906
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 02:30:57.868561
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 02:31:00.280948
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 02:31:02.697914
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 02:31:05.110187
# Unit test for method register_methods of class _AVMClass

# Generated at 2026-10-25 02:31:07.523280
# Unit test for method register_methods of class _AVMClass

# Generated at 2026-10-25 02:31:09.939233
# Unit test for method register_methods of class _AVMClass

# Generated at 2026-10-25 02:31:12.353476
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 02:31:14.768295
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 02:31:17.184075
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 02:31:19.598199
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 02:31:22.012680
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 02:31:24.427080
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 02:31:26.854020
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 02:31:29.268988
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 02:31:31.684828
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 02:31:34.101865
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 02:31:36.753396
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 02:32:02.053336
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 02:32:30.117508
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 02:32:32.532653
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 02:32:34.948792
# Unit test for method extract_function of class SWFInterpreter