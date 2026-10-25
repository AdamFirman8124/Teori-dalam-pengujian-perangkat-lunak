

# Generated at 2026-10-25 05:26:19.910107
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

# Generated at 2026-10-25 05:26:37.956991
# Unit test for constructor of class _ScopeDict

# Generated at 2026-10-25 05:26:39.372411
# Unit test for constructor of class _ScopeDict

# Generated at 2026-10-25 05:26:40.737881
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

# Generated at 2026-10-25 05:26:42.237858
# Unit test for constructor of class _Multiname
def test__Multiname():
    kind = 0x07
    obj = _Multiname(kind)

    assert isinstance(obj, _Multiname)
    assert obj.kind == kind
    assert repr(obj) == '[MULTINAME kind: 0x%x]' % kind

# Generated at 2026-10-25 05:26:45.026630
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 05:26:47.651673
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 05:26:50.368553
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 05:26:52.788536
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 05:26:55.376017
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 05:26:57.796459
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 05:27:03.348963
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 05:27:05.767692
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 05:27:08.186998
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 05:27:10.605415
# Unit test for method __repr__ of class _Undefined

# Generated at 2026-10-25 05:27:13.024081
# Unit test for method __repr__ of class _Undefined

# Generated at 2026-10-25 05:27:15.445264
# Unit test for method __repr__ of class _Undefined

# Generated at 2026-10-25 05:27:17.862222
# Unit test for method __repr__ of class _Undefined

# Generated at 2026-10-25 05:27:20.282969
# Unit test for method __repr__ of class _Undefined

# Generated at 2026-10-25 05:27:22.701173
# Unit test for method __repr__ of class _Undefined

# Generated at 2026-10-25 05:27:25.119796
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 05:27:27.540151
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 05:27:47.262044
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():interpreter = object.__new__(SWFInterpreter)

# Generated at 2026-10-25 05:27:49.966258
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 05:27:52.396942
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 05:27:54.807870
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 05:27:57.227576
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 05:27:59.646891
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 05:28:02.207000
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 05:28:04.624598
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 05:28:07.042280
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 05:28:09.461230
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 05:28:11.879964
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 05:28:14.299984
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 05:28:16.719291
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 05:28:19.136872
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 05:28:21.557021
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 05:28:23.975519
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 05:28:26.393967
# Unit test for method __repr__ of class _Undefined

# Generated at 2026-10-25 05:28:28.812007
# Unit test for method __repr__ of class _Undefined

# Generated at 2026-10-25 05:28:31.232716
# Unit test for method __repr__ of class _Undefined

# Generated at 2026-10-25 05:28:35.047992
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 05:28:37.466903
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 05:28:39.884893
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 05:28:42.301997
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 05:28:44.719793
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 05:28:47.140126
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 05:28:49.559254
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 05:28:51.975217
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 05:28:54.394094
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 05:28:56.813075
# Unit test for method register_methods of class _AVMClass

# Generated at 2026-10-25 05:28:59.229826
# Unit test for method register_methods of class _AVMClass

# Generated at 2026-10-25 05:29:01.647774
# Unit test for method register_methods of class _AVMClass

# Generated at 2026-10-25 05:29:04.066218
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 05:29:06.484814
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 05:29:08.906800
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 05:29:11.326768
# Unit test for method register_methods of class _AVMClass

# Generated at 2026-10-25 05:29:13.745101
# Unit test for method register_methods of class _AVMClass

# Generated at 2026-10-25 05:29:16.163157
# Unit test for method register_methods of class _AVMClass

# Generated at 2026-10-25 05:29:18.583044
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 05:29:21.001776
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 05:29:23.420453
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 05:29:25.841257
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 05:29:41.523051
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():method = type('Method', (), {
        'code': bytes([36, 42, 72]),
        'local_count': 1,
    })()

# Generated at 2026-10-25 05:29:44.515335
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 05:30:12.238791
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 05:30:40.012862
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 05:30:50.469939
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():interpreter = SWFInterpreter.__new__(SWFInterpreter)


# Generated at 2026-10-25 05:31:37.058531
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():from types import SimpleNamespace


# Generated at 2026-10-25 05:31:39.606502
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

# Generated at 2026-10-25 05:32:25.487160
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():interpreter = SWFInterpreter.__new__(SWFInterpreter)

# Generated at 2026-10-25 05:32:53.823375
# Unit test for method extract_function of class SWFInterpreter