

# Generated at 2022-06-14 18:24:46.160202
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    from .compat_urllib_request import urlopen
    from .compat_urllib_parse import urlencode
    from .compat_urllib_error import HTTPError
    interpreter = SWFInterpreter()
    url = 'https://vpaid-get.Tester.com/get-swf'

# Generated at 2022-06-14 18:24:51.100970
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    interpreter = SWFInterpreter()

    code_patches = {
        (3, 2, 1, 'toto'): b'\x03\x02\x01',
    }
    function = interpreter.patch_function(
        b'\x11\x22\x33\x44', code_patches)
    assert function(b'\x11\x22\x33\x44') == b'\x03\x02\x01'

    code_patches = {
        (3, 2): b'\x03\x02\x01',
    }
    function = interpreter.patch_function(
        b'\x11\x22\x33\x44', code_patches)

# Generated at 2022-06-14 18:25:02.178672
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    avm_file = path.join(
        path.dirname(path.abspath(__file__)), 'tests', 'fixtures', 'avm.swf')
    avm_data = open(avm_file, 'rb').read()
    with open(avm_file, 'rb') as avm_file_obj:
        avm = SWFInterpreter(avm_file_obj)
        avm.load()
        avm.patch_function('String.split')
        # Test that avm.play_frame is defined
        assert callable(avm.play_frame)
        # Test that avm.play_frame returns a list of strings
        result = avm.play_frame(avm_data)
        assert isinstance(result, list)

# Generated at 2022-06-14 18:25:13.086685
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    from pyamf.remoting.client import RemotingService
    from .test_remoteservice import echo_function
    from .test_remoteservice import test_Echo_echo

    echo_class = extract_class(Echo, [echo_function])
    service = RemotingService('http://localhost:8080/gateway/',
        amf_version=3, logger=None)
    echo_service = service.getService('echo.Echo')

    assert hasattr(echo_service, 'echo'), 'Missing echo function'
    assert callable(echo_service.echo), 'echo function is not callable'
    assert echo_service.echo != echo_function
    assert echo_service.echo != echo_class.method_pyfunctions['echo']

    res = echo_service.echo('qwerty')

# Generated at 2022-06-14 18:25:22.530731
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    interp = SWFInterpreter(b'\x00' * 0)
    class_ref = pytest.approx(0.7)
    variables = OrderedDict([('a', 1), ('b', 2)])
    method_names = set(['c', 'd'])
    method_bodies = [(1, [], 0, [], [])]
    instance_names = set(['e'])
    super_name = 'Object'
    flags = 0
    class_ = interp.extract_class(class_ref, variables, method_names, method_bodies,
        instance_names, super_name, flags)
    assert type(class_) == _AVMClass
    assert type(class_.ref) == float
    assert class_.ref == class_ref

# Generated at 2022-06-14 18:25:27.383846
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    from io import BytesIO
    with open('test/data/test1.swf', 'rb') as f:
        data = f.read()
    obj = BytesIO(data)
    interpreter = SWFInterpreter(obj)

# Generated at 2022-06-14 18:25:38.989314
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    from io import BytesIO
    from collections import namedtuple

    class ABCFile(object):
        def __init__(self, abc_data):
            self.abc_data = BytesIO(abc_data)

        def read_constant_int(self):
            return self.abc_data.read(4)

        def read_constant_uint(self):
            return self.abc_data.read(4)

        def read_constant_double(self):
            return self.abc_data.read(8)

        def read_constant_utf8(self):
            return self.abc_data.read(4)

        def read_constant_namespace(self):
            return self.abc_data.read(4)

        def read_constant_multiname(self):
            kind = _

# Generated at 2022-06-14 18:25:46.808070
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    s = SWFInterpreter('''
        .bytecode_abc
        "abc"
        21 00 00 00  14  0a  05  73  74  72  69  6e  67  02
        00 05  61  62  63  00 00 00 00 01  06  06  03  00 00
        00  00 04  01 00  00  00  00  05  01 00  00
    ''')
    assert s.constant_strings == ['', 'string', 'abc']

# Generated at 2022-06-14 18:25:56.362051
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    from .flash_constants import AVMConstants
    constants = AVMConstants()

    from .abc_interpreter import build_abcexpressions
    abc_expressions = build_abcexpressions(constants)

    interpreter = SWFInterpreter(constants, abc_expressions)

    from .flash_io import SWFStringReader
    from .swf_tagdata import DoABCData
    from .doabc_interpreter import ABCInterpreter
    abc_interpreter = ABCInterpreter(constants, abc_expressions)
    abc_data = DoABCData(
        name='test',
        unk1=1,
        unk2=2,
        unk3=3,
        abc_string=SWFStringReader('abc.string'),
    )

# Generated at 2022-06-14 18:26:00.941048
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    swf = SWFInterpreter(None, ['tests/data/SWFInterpreter.swf'])
    swf.parse()
    swf.patch_function('tests/data/SWFInterpreter.swf', 'Main', 'get_func', swf.get_func)
    assert swf.call_function('tests/data/SWFInterpreter.swf', 'Main', 'test_call_func') is True


# Generated at 2022-06-14 18:27:03.380188
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    swfint = SWFInterpreter()
    swfint.load(os.path.join(test_dir, 'cbsnews.swf'))
    player_init = swfint.extract_function('com.cbs.news.Player', 'init')
    player = player_init()
    assert player.is_ready == True

# Class for representing a Magic Swf

# Generated at 2022-06-14 18:27:10.260748
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    interpreter = SWFInterpreter()
    interpreter.load_swf(BytesIO(b'\x53\x57\x46\x57'))
    interpreter.patch_function(None, 'Array', 'join', lambda x: [])
    interpreter.patch_function(None, 'String', 'split', lambda x: [])

# Generated at 2022-06-14 18:27:21.563086
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    swfi = SWFInterpreter()

    # Test empty function
    swfi.scp_header.nConstantPool.set(2)
    swfi.scp_header.StackSize.set(4)
    assert len(swfi.constant_pool) == 2
    assert len(swfi.multinames) == 0
    coder = compat_io.BytesIO()
    coder.write(b'\x03\x00\x00')
    swfi.scp_header.methods.append(coder.getvalue())
    coder.seek(0)
    swfi.extract_function(None, 'dummy')
    assert swfi.scp_header.StackSize.get() == 4
    assert len(swfi.multinames) == 0

# Generated at 2022-06-14 18:27:32.363496
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    with open('test.swf', 'rb') as f:
        data = f.read()
    swf_file = swf.SWF(BytesIO(data), is_bytes_io=True)

    interp = SWFInterpreter(swf_file)
    assert interp.constant_strings[1] == 'root1'
    assert interp.constant_strings[2] == 'root2'
    assert interp.constant_strings[3] == '_level0'
    assert interp.constant_strings[4] == '_level0.loader_mc'
    assert interp.constant_strings[5] == '_level0.loader_mc.test_mc'
    assert interp.constant_strings[6] == '_root'

# Generated at 2022-06-14 18:27:34.234757
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    assert SWFInterpreter('\x00\x00\x00\x00')


# Generated at 2022-06-14 18:27:43.279543
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2022-06-14 18:27:54.882156
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    test_abc = open(
        os.path.join(os.path.dirname(__file__),
                     'test_avm1_abc.abc'), 'rb').read()
    with NamedTemporaryFile('wb', delete=False) as f:
        f.write(test_abc)
    ptr = SWFParser.parse(f.name)
    os.unlink(f.name)
    ptr.pretty_print()

# Generated at 2022-06-14 18:28:07.538367
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    swf = read_swf('test.swf')
    interp = SWFInterpreter(swf, {'trace_enabled': False})
    res = interp.extract_function(interp.avm_class, 'get_ytplayer_config')

# Generated at 2022-06-14 18:28:18.296204
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    from .test_utils import make_test_resource_path
    path = make_test_resource_path('python-soundcloud.swf')
    interpreter = SWFInterpreter(path)

    class_1 = interpreter.extract_class(0)

# Generated at 2022-06-14 18:28:30.899569
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    def _test(f):
        f = open(f, 'rb')
        tag_reader = SWFTagReader(f)
        interpreter = SWFInterpreter(tag_reader)
        assert interpreter.doactions_tag == tag_reader.doactions_tag
        assert interpreter.swf_header == tag_reader.swf_header
        assert interpreter.tag_reader == tag_reader
        assert interpreter.tag_index == 0
        assert interpreter.tag_pos == tag_reader.tag_pos
        assert interpreter.method_pyfunctions == {}
        assert interpreter.next_tag_type == tag_reader.next_tag_type
        assert interpreter.next_tag_data == tag_reader.next_tag_data
        assert interpreter.next_tag_pos == tag_reader.next_tag_pos


# Generated at 2022-06-14 18:30:17.714672
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    import zlib
    import base64
    import re

# Generated at 2022-06-14 18:30:19.286536
# Unit test for method __repr__ of class _ScopeDict
def test__ScopeDict___repr__():
    _ScopeDict(1).__repr__()



# Generated at 2022-06-14 18:30:31.501244
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    swfobj = _TestSwfObject()
    sp = SWFInterpreter(swfobj)
    cls1 = sp.extract_class(0)
    cls2 = sp.extract_class(0)
    assert cls1 is cls2, 'Classes must be cached'

    cls3 = sp.extract_class(1)
    assert cls3 is not cls1, 'Class must be extracted with different id'

    assert cls1.name == 'Main'
    assert cls1.superclass == ObjectClass
    assert cls1.constructor_name == 'Main'

    assert cls1.variables['x'] == 0
    assert cls1.variables['y'] == 0
    assert cls1.variables['value'] is undefined
    assert cls1.variables

# Generated at 2022-06-14 18:30:40.518282
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():

    @staticmethod
    def _dummy_function(args):
        # Dummy function for testing
        return args[0] + args[1]

    @staticmethod
    def _do_decode(code):
        class DummySWFClass:
            @staticmethod
            def get_action(version, code):
                return code

        class DummySWFMethod:
            name = 'dummy'

        # Mock objects
        interpreter = DummySWFInterpreter()
        swf_class = DummySWFClass()
        swf_method = DummySWFMethod()
        interpreter.extract_script = lambda x: x
        interpreter.patch_script = lambda x: x

        return interpreter.patch_function(
            swf_class, swf_method, 'dummy', code)

    # No params, return

# Generated at 2022-06-14 18:30:51.316569
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    with open(os.path.join(os.path.dirname(__file__), 'test.swf'), 'rb') as f:
        swf = SWF(f)
        avm_class = SWFInterpreter().extract_class(swf, 0)

    assert avm_class.static_properties['parseInt'] == parseInt
    assert avm_class.static_properties['parseFloat'] == parseFloat
    assert avm_class.static_properties['isFinite'] == isFinite
    assert avm_class.static_properties['decodeURI'] == decodeURI
    assert avm_class.static_properties['encodeURI'] == encodeURI
    assert avm_class.static_properties['Date'].static_properties['UTC'] == UTC

# Generated at 2022-06-14 18:30:57.049199
# Unit test for method __repr__ of class _ScopeDict
def test__ScopeDict___repr__():
    from .utils import FakeAVMClass
    scope = _ScopeDict(FakeAVMClass('Foo'))
    scope['abc'] = [1, 2, 3]
    scope['def'] = 'ghi'
    scope['jkl'] = (4, 5, 6, 7)
    assert repr(scope) == "Foo__Scope({'abc': [1, 2, 3], 'def': 'ghi', 'jkl': (4, 5, 6, 7)})"



# Generated at 2022-06-14 18:31:05.204366
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    swf = '3gABAAQADQAXABsA'
    interp = SWFInterpreter(io.BytesIO(base64.b64decode(swf)), 0)
    interp.extract_classes()
    class_data = interp.class_data
    assert len(class_data['Test'].method_pyfunctions) == 1
    assert 'checkA' in class_data['Test'].method_pyfunctions
    assert class_data['Test'].static_properties['a'] == 0x123
    assert class_data['Test'].static_properties['b'] == 0x456
    assert class_data['Test'].static_properties['c'] == 0x789
    assert class_data['Test'].static_properties['d'] == 'abc'
    assert class_data['Test'].static

# Generated at 2022-06-14 18:31:17.795267
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    with open(os.path.join(os.path.dirname(__file__),
                           'testdata/buzztard_tests/class.swf'), 'rb') as fp:
        swf = SWF(fp)
    swf.parse()
    inter = SWFInterpreter(swf)
    inter.extract_classes()
    assert len(inter.classes) == 1
    cls = list(inter.classes.values())[0]
    assert cls.name == 'Test'
    assert len(cls.static_properties) == 3
    assert cls.static_properties['S1'] == 'test'
    assert cls.static_properties['S2'] == 3
    assert cls.static_properties['S3'] == 5.5

    assert len(cls.method_names)

# Generated at 2022-06-14 18:31:26.279073
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2022-06-14 18:31:36.652595
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    interpreter = SWFInterpreter()  # type: SWFInterpreter