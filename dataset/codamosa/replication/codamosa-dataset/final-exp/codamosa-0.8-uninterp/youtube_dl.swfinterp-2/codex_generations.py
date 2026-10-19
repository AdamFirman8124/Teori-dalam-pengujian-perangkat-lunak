

# Generated at 2022-06-14 18:24:53.448162
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    class _MockStringIO(io.BytesIO):
        # Some methods to mock the behavior of BytesIO
        # on Python 3
        def __iter__(self):
            return self
        def __next__(self):
            return self.read(1)
        def readable(self):
            return True
        def seekable(self):
            return True
    assert py3compat.PY3
    # Test constructor
    swf_file = _MockStringIO(b'\x46\x57\x53\x05\x05\x00\x00\x00\x0F\x00\x00\x00')
    reader = lambda *args, **kwargs: swf_file
    swf = SWFInterpreter(reader)

    swf_file.seek(0)
    swf

# Generated at 2022-06-14 18:25:06.700706
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    from .bitstream import BitStream
    from .tags import TagDecoder, TagPlaceObject2

    data = BitStream(bytes=b'')
    obj = SWFInterpreter()

    # Non-tag object
    with pytest.raises(TypeError):
        obj.patch_function(data)

    # Unsupported tag
    class TagDecoderStub(TagDecoder):
        @staticmethod
        def decode(stream):
            return None

    data = BitStream(bytes=b'\x00\x00\x00')
    tag = TagDecoderStub.decode(data)
    tag.type = 0

    with pytest.raises(TypeError):
        obj.patch_function(tag)

    # Type mismatch

# Generated at 2022-06-14 18:25:09.242024
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    swf = SWFInterpreter()
    swf.patch_function('', '', '', '', '', '')

# Generated at 2022-06-14 18:25:17.829001
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    from .rtmp import read_swf
    swf = read_swf(open(path.join(path.dirname(__file__), 'test.swf'), 'rb'))

# Generated at 2022-06-14 18:25:22.852227
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    stream = io.BytesIO(b'')
    ctx = Context(stream)
    ctx.swf_interpreter = SWFInterpreter(ctx)
    ctx.swf_interpreter.method_sizes = {'foo': 2}
    ctx.swf_interpreter.extract_function(
        ctx.swf_interpreter.avm_class, 'foo')

# Class representing the SWF player

# Generated at 2022-06-14 18:25:34.148380
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    class TestInterpreter(SWFInterpreter):
        def __init__(self):
            self.method_names = set()
            self.method_pyfunctions = {}
            self.static_properties = {}

    interp = TestInterpreter()
    interp.constant_strings = [
        'method1',
        'method2',
        'method3',
    ]

# Generated at 2022-06-14 18:25:43.519823
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2022-06-14 18:25:50.768187
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    # ValueError should be raised for empty input
    with pytest.raises(ValueError):
        SWFInterpreter(b'')
    # ValueError should be raised for invalid input
    with pytest.raises(ValueError):
        SWFInterpreter(b'FWS1232')
    # ValueError should be raised for invalid input
    with pytest.raises(ValueError):
        SWFInterpreter(b'CWS1232')


# Generated at 2022-06-14 18:25:58.827608
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    import json
    import io
    import zipfile
    with zipfile.ZipFile(b'a.zip', 'w') as zf:
        zf.writestr(b'a.swf', ''.join(map(chr, range(256))))
    filename = 'a.zip/a.swf'
    with open(filename, 'rb') as f:
        swf = f.read()
    swf = io.BytesIO(swf)
    swf = SWF(swf)
    interpreter = SWFInterpreter(swf)
    f = interpreter.extract_function(interpreter.AVM2, 'dump')
    assert f([1, 2, 3, 4]) == '[1, 2, 3, 4]'

# Generated at 2022-06-14 18:26:03.830590
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    SWFInterpreter = _SWFInterpreter
    assert_raises(ValueError, SWFInterpreter, b'\x00\x00\x00')
    assert_raises(ValueError, SWFInterpreter, b'\x00\x00\x00F')
    assert_raises(ValueError, SWFInterpreter, b'\x00\x00\x00F\x00')
    assert_raises(ValueError, SWFInterpreter, b'\x00\x00\x00F\x00\x00')
    assert_raises(ValueError, SWFInterpreter, b'\x00\x00\x00F\x00\x00\x00')

# Generated at 2022-06-14 18:27:07.588620
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    interpreter = SWFInterpreter(None)

    running_version = util.running_version

    def _check_extract_function(version):
        # Here we have to wrap a function in a class, otherwise it won't be
        # found during method lookup
        class Class_0:
            def methodspec_2(self, arg1=None):
                return arg1

            def methodspec_3(self, arg1=None, arg2=None):
                return arg1, arg2

        if version <= (10, 0):
            func = interpreter.extract_function(Class_0, 'methodspec_2')
            assert func(['a']) == 'a'  # AssertionError on Python 3
            func = interpreter.extract_function(Class_0, 'methodspec_3')

# Generated at 2022-06-14 18:27:19.534281
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    import io
    from .tagreader import AS3Reader
    from .swftags import EndTag, SymbolClassTag, DoABCTag, SWFTag

    class DummyTag(object):
        def __init__(self, data):
            self.data = data

    # For SWF14 and above, ABC methods have flags, which we cannot set yet
    # For now we just use doabc1 to avoid the flags.
    flags = b'\x00\x00\x00\x00\x0A\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    data = bytearray(b'\x06\x00\x00\x00')
    data.extend(flags)

# Generated at 2022-06-14 18:27:27.658658
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    avm_interpreter = SWFInterpreter()
    class AvmFile(object):
        def __init__(self):
            self.methods = {}
    avm_file = AvmFile()


# Generated at 2022-06-14 18:27:39.219338
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2022-06-14 18:27:45.992007
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2022-06-14 18:27:56.893345
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    import zlib
    from io import BytesIO

    from .test_helper import TestCase

    def open_swf(name):
        return BytesIO(zlib.decompress(getattr(test_helper, name)))

    class TestInterpreter(TestCase):
        def test_SWFInterpreter_extract_function_basics(self):
            si = SWFInterpreter(open_swf('hello_world_button.swf'))
            button_class = si.avm_class
            button_prototype = button_class.make_object()
            button_prototype.init_prototype(button_class)
            button_class.method_pyfunctions['draw'] = lambda x: None
            button_class.method_pyfunctions['updateAfterEvent'] = lambda x: None
            button_class

# Generated at 2022-06-14 18:28:02.061829
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    def testfunc(args):
        if args:
            return args[0]

    interpreter = SWFInterpreter(None, None)
    interpreter.patch_function(testfunc)

    assert testfunc([1]) == 1
    assert testfunc(['hello']) == 'hello'
    assert testfunc([]) == undefined


# Generated at 2022-06-14 18:28:12.907872
# Unit test for method __repr__ of class _ScopeDict
def test__ScopeDict___repr__():
    class _MockAVMClass(object):
        name = 'dummy_class_name'
    scope_dict = _ScopeDict(
        _MockAVMClass())
    if not isinstance(
            scope_dict.__repr__(),
            compat_str):
        raise AssertionError
    if scope_dict.__repr__() != 'dummy_class_name__Scope({})':
        raise AssertionError
    scope_dict['x'] = 123
    if scope_dict.__repr__() != "dummy_class_name__Scope({'x': 123})":
        raise AssertionError
    scope_dict['y'] = ['a', 'b', 'c']

# Generated at 2022-06-14 18:28:18.677242
# Unit test for method __repr__ of class _ScopeDict
def test__ScopeDict___repr__():
    class AVMClass(object):
        @classmethod
        def class_name(cls, object_id):
            return 'AVMClass'
    sd = _ScopeDict(AVMClass)
    sd['a'] = 'b'
    sd.update({'c': 'd'})
    assert sd.__repr__() == "AVMClass__Scope({'a': 'b', 'c': 'd'})"



# Generated at 2022-06-14 18:28:24.596493
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    interpreter = SWFInterpreter({})
    assert interpreter.constant_strings == []
    assert interpreter.constant_namespaces == []
    assert interpreter.multinames == []
    assert interpreter.methods == []
    assert interpreter.classes == {}
    assert interpreter.classes_by_name == {}
    assert interpreter.method_pyfunctions == {}


# Generated at 2022-06-14 18:29:53.879858
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    from .tag import DoAction, DoInitAction
    from .actions import ActionPush, ActionGetURL
    from .abcfile import ABCFile
    from .abc import ABCMethodInfo, ABCMultinameInfo, ABCClassInfo
    abc = ABCFile()
    multiname_obj = ABCMultinameInfo(
        name_index=None,
        namespace_indices=[0],
        namespace_set_index=0)
    idx_obj = abc.add_multiname(multiname_obj)

    multiname_array = ABCMultinameInfo(
        name_index=None,
        namespace_indices=[0],
        namespace_set_index=0)
    idx_array = abc.add_multiname(multiname_array)

    multiname_undefined = ABCMultinameInfo

# Generated at 2022-06-14 18:30:02.253035
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    with open(os.path.join(os.path.dirname(__file__), 'test.swf'), 'rb') as f:
        swf = SWF(f)
    avm_interpreter = SWFInterpreter(swf)
    assert len(avm_interpreter.constant_strings) == 7
    assert avm_interpreter.constant_strings[0] == ''
    assert avm_interpreter.constant_strings[1] == 'testMethod'
    assert avm_interpreter.constant_strings[2] == 'testName'
    assert avm_interpreter.constant_strings[3] == 'testArg'
    assert avm_interpreter.constant_strings[4] == 'testName'
    assert avm_interpreter.constant

# Generated at 2022-06-14 18:30:10.602741
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2022-06-14 18:30:16.707910
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    text = """
    <abc>
        <b>
        <c>
    """
    interp = SWFInterpreter(text)
    assert interp.extract_class("_lex_toplevel")
    assert interp.extract_class("_lex_toplevel_1")
    assert interp.extract_class("_lex_toplevel_2")
    assert not interp.extract_class("_lex_toplevel_3")

# Generated at 2022-06-14 18:30:29.171594
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():

    def test_func(args):
        return args[0] + args[1]

    class PinoClass:
        def __init__(self, x):
            self.x = x

        def num(self):
            return 1

        def str(self):
            return '2'

        def bool(self):
            return False

        def undef(self):
            return undefined

        def obj(self):
            return PinoClass(3)

    def test_func2(args):
        return args[0] + args[1]

    class PinoClass2:
        def __init__(self, x):
            self.x = x

        def num(self):
            return 1

        def str(self):
            return '2'

        def bool(self):
            return False


# Generated at 2022-06-14 18:30:39.283279
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    class A:
        def __init__(self):
            self.x = 3
            self.y = 5
    a = A()

# Generated at 2022-06-14 18:30:40.441302
# Unit test for method __repr__ of class _ScopeDict
def test__ScopeDict___repr__():
    import doctest
    doctest.testmod()



# Generated at 2022-06-14 18:30:48.205531
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    import io
    #SwfFile = io.BytesIO(open('c:/Users/Hao/Desktop/a.swf', 'rb').read())
    SwfFile = io.BytesIO(open('temp/main.swf', 'rb').read())
    si = SWFInterpreter(SwfFile)
    si.extract_function(si.AVMClasses[1], 'iframeLoadedHandler')


# Generated at 2022-06-14 18:30:54.313996
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    from .swfdecompiler import SWFInterpreter
    from .swfdom import SWF


# Generated at 2022-06-14 18:30:57.809275
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    swf = SWFInterpreter(b'\x00\x00\x00\x00\x00\x00\x00\x00')
    assert len(swf.method_pyfunctions) == 0

# Common code for all tests

# Generated at 2022-06-14 18:32:56.971146
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    from io import BytesIO
    from collections import namedtuple
    from struct import pack
    AVMClass = namedtuple('AVMClass', 'name variables methods traits')

    class _SWFInterpreterTest(object):
        def __init__(self, action_data):
            self.code = BytesIO(action_data)
            self.methods = []
            self.multinames = []
            self.method_pyfunctions = {}

        def seek(self, offset):
            return self.code.seek(offset)

        def tell(self):
            return self.code.tell()

        def read(self, size):
            return self.code.read(size)

    def _test(action_data, expected_source):
        interp = _SWFInterpreterTest(action_data)
        patch

# Generated at 2022-06-14 18:33:09.203516
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    def _test(class_name, args, expected_output):
        with io.open(class_name + '.swf', 'rb') as inp:
            data = inp.read()
        with namedTemporaryFile() as out:
            with io.open(out.name, 'wb') as outf:
                outf.write(data)
            interpreter = SWFInterpreter(out.name)
        class_ = interpreter.avm_classes[class_name]
        function_ = class_.method_pyfunctions['main']
        res = function_(args)
        assert res == expected_output
    _test('Minimal', [], None)
    _test('MinimalInit', [], None)
    _test('MinimalMath', [], None)
    _test('MinimalArray', [], None)
    _

# Generated at 2022-06-14 18:33:19.810398
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    swf = pkgutil.get_data('youtube_dl.extractor', 'test/data/test.swf')

    swf_interpreter = SWFInterpreter()
    swf_interpreter.read_swf(swf)
    assert swf_interpreter.header == b'FWS'
    assert swf_interpreter.version == 3
    assert swf_interpreter.file_length == 751
    assert swf_interpreter.frame_size == (800, 600)
    assert swf_interpreter.frame_rate == 24.0
    assert swf_interpreter.tag_code_length == 1

    assert swf_interpreter.tags[0].tag_type == 69
    assert swf_interpreter.tags[1].tag_type == 75


# Generated at 2022-06-14 18:33:30.093660
# Unit test for constructor of class SWFInterpreter

# Generated at 2022-06-14 18:33:36.505888
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    with open(os.path.join('tests', 'as3', 'Test.swf'), 'rb') as f:
        s = f.read()
    i = SWFInterpreter(s)
    cls = i.extract_class('Test')
    cls.make_object(1)

# Generated at 2022-06-14 18:33:44.649348
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    global StringClass
    StringClass = _builtin_classes['String']

    global String_asclass
    String_asclass = StringClass.make_object()


# Generated at 2022-06-14 18:33:50.258252
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    interpreter = SWFInterpreter(b'foo.swf')

    def test_method(args):
        assert len(args) == 1
        assert args[0] == 'abc'
        return 'abc'

    interpreter.avm_class.method_names.add('test_method')
    interpreter.avm_class.static_properties['test_method'] = test_method

    interpreter.extract_function(interpreter.avm_class, 'test_method')
    res = interpreter.extract_function(
        interpreter.avm_class, 'test_method')(['abc'])

    assert res == 'abc'


# Generated at 2022-06-14 18:33:59.200840
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    def check(code, expected_result):
        interpreter = SWFInterpreter()
        func = interpreter.extract_function(
            avm_class=None, func_name='', code=code)
        result = func()
        assert result == expected_result, repr((result, expected_result))

    check(
        '\n'.join((
            '3',
            '0 pushbyte 23',
            '2 pushbyte 42',
            '4 add',
            '5 returnvalue',
        )),
        65)

    check(
        '\n'.join((
            '1',
            '0 pushnull',
            '1 returnvalue',
        )),
        None)
