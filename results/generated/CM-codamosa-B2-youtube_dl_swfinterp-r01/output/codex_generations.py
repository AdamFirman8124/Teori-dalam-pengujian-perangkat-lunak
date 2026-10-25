

# Generated at 2026-10-25 00:05:14.184045
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():interpreter = SWFInterpreter.__new__(SWFInterpreter)

# Generated at 2026-10-25 00:05:40.806376
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 00:05:54.627332
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():interpreter = SWFInterpreter.__new__(SWFInterpreter)

# Generated at 2026-10-25 00:05:55.972661
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

# Generated at 2026-10-25 00:06:15.214612
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

# Generated at 2026-10-25 00:06:17.637733
# Unit test for constructor of class _ScopeDict

# Generated at 2026-10-25 00:06:20.070441
# Unit test for constructor of class _ScopeDict

# Generated at 2026-10-25 00:06:22.496904
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 00:06:24.920217
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 00:06:27.342978
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 00:06:29.760751
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 00:06:32.183523
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 00:06:34.612455
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 00:06:37.029191
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 00:06:39.456794
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 00:06:42.654539
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 00:06:45.368749
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 00:07:11.490664
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 00:07:13.919930
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 00:07:16.340484
# Unit test for method __repr__ of class _AVMClass_Object

# Generated at 2026-10-25 00:07:18.768395
# Unit test for method __repr__ of class _AVMClass_Object

# Generated at 2026-10-25 00:07:21.196291
# Unit test for method __repr__ of class _AVMClass_Object

# Generated at 2026-10-25 00:07:23.635257
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 00:07:26.055157
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 00:07:28.471520
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 00:07:30.895858
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 00:07:33.500784
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 00:07:35.938437
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 00:07:38.351007
# Unit test for method __repr__ of class _ScopeDict

# Generated at 2026-10-25 00:07:40.769697
# Unit test for method __repr__ of class _ScopeDict

# Generated at 2026-10-25 00:07:43.191589
# Unit test for method __repr__ of class _ScopeDict

# Generated at 2026-10-25 00:07:45.610322
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 00:07:48.030482
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 00:07:50.450417
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 00:08:16.560959
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 00:08:19.281719
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 00:08:22.086630
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 00:08:23.453083
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

# Generated at 2026-10-25 00:08:24.853355
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

# Generated at 2026-10-25 00:08:43.259949
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    interpreter = object.__new__(SWFInterpreter)

    # Required constant-pool attributes for bytecode execution.
    interpreter.constant_strings = ['']
    interpreter.multinames = ['']

    avm_class = _AVMClass(0, 'TestClass')
    avm_class.method_names['add'] = 0

    # Adapt these containers if method_infos/method_bodies use named objects
    # rather than dictionaries in your parser.
    interpreter.method_infos = [{
        'param_count': 2,
    }]
    interpreter.method_bodies = [{
        'method_idx': 0,
        'local_count': 3,  # this + two arguments
        'code': bytes((
            209,  # getlocal_1
            210,  # getlocal_2
            160,  # add
            72,   # returnvalue
        )),
    }]

    func = interpreter.extract_function(avm_class, 'add')

    assert func([20, 22]) == 42
    assert func([-5, 2]) == -3

    # extract_function should cache the generated Python function.
    assert interpreter.extract_function(avm_class, 'add') is func
    assert avm_class.method_pyfunctions['add'] is func

# Generated at 2026-10-25 00:08:45.815907
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 00:08:48.368349
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 00:08:50.926745
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 00:08:53.340200
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 00:08:55.760867
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 00:08:58.438857
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 00:09:25.292372
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 00:09:39.973481
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():from types import SimpleNamespace


# Generated at 2026-10-25 00:09:42.394776
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 00:09:44.812241
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 00:09:47.232308
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 00:09:49.651735
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 00:09:52.063836
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 00:09:54.482680
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-25 00:09:56.899133
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 00:09:59.315544
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 00:10:01.732621
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 00:10:04.148343
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 00:10:06.562985
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 00:10:08.985452
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 00:10:11.399484
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-25 00:10:26.396965
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():interpreter = SWFInterpreter.__new__(SWFInterpreter)

# Generated at 2026-10-25 00:10:44.838011
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():interpreter = SWFInterpreter.__new__(SWFInterpreter)

# Generated at 2026-10-25 00:10:47.696218
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 00:11:09.511425
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():import struct

abc = struct.pack('<HH', 16, 46) + b'\x01' * 7 + b'\x00' * 5
doabc = b'\x00\x00\x00\x00\x00' + abc
tag_header = struct.pack('<H', (82 << 6) | len(doabc))
body = (
    b'\x08\x00'
    + b'\x00\x0c'
    + b'\x01\x00'
    + tag_header
    + doabc
    + b'\x00\x00'
)
swf = b'FWS' + b'\x09' + struct.pack('<I', 8 + len(body)) + body

interpreter = SWFInterpreter(swf)
assert interpreter.constant_strings == ['']

# Generated at 2026-10-25 00:11:36.951433
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 00:11:53.729939
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():interpreter = SWFInterpreter.__new__(SWFInterpreter)


# Generated at 2026-10-25 00:12:14.023816
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():from types import SimpleNamespace


# Generated at 2026-10-25 00:12:15.453813
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

# Generated at 2026-10-25 00:12:35.271136
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    class DummyAVMClass:
        pass

    interpreter = object.__new__(SWFInterpreter)

    avm_class = DummyAVMClass()
    avm_class.variables = {}
    avm_class.method_names = {'add_one': 0}
    avm_class.method_pyfunctions = {}

    # getlocal_1
    # pushbyte 1
    # add
    # returnvalue
    avm_class.methods = {
        0: bytes((209, 36, 1, 160, 72)),
    }

    func = interpreter.extract_function(avm_class, 'add_one')

    assert callable(func)
    assert func([41]) == 42

    # The extracted function should be cached and reused.
    assert interpreter.extract_function(avm_class, 'add_one') is func
    assert avm_class.method_pyfunctions['add_one'] is func

# Generated at 2026-10-25 00:12:38.083665
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 00:13:05.169846
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 00:13:32.363347
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-25 00:13:33.710417
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

# Generated at 2026-10-25 00:13:47.411166
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():interpreter = SWFInterpreter.__new__(SWFInterpreter)


# Generated at 2026-10-25 00:14:11.267667
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 00:14:37.279745
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2026-10-25 00:14:38.639128
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

# Generated at 2026-10-25 00:14:57.452747
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    class MethodBody:
        local_count = 3
        # getlocal_1, getlocal_2, add, returnvalue
        code = b'\xd1\xd2\xa0\x48'

    class AVMClass:
        variables = {}
        method_names = {'add': 0}
        methods = {}
        method_pyfunctions = {}

    # Avoid parsing an actual SWF; provide only the state required by
    # extract_function.
    interpreter = SWFInterpreter.__new__(SWFInterpreter)
    interpreter.method_infos = {0: object()}
    interpreter.method_bodies = {0: MethodBody()}

    avm_class = AVMClass()

    add = interpreter.extract_function(avm_class, 'add')

    assert add([2, 3]) == 5
    assert add([-4, 10]) == 6

    # The extracted Python function should be cached on the AVM class.
    assert avm_class.method_pyfunctions['add'] is add
    assert interpreter.extract_function(avm_class, 'add') is add

# Generated at 2026-10-25 00:15:00.423596
# Unit test for constructor of class SWFInterpreter