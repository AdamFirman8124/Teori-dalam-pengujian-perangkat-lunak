

# Generated at 2022-06-14 18:25:12.429471
# Unit test for method __repr__ of class _ScopeDict
def test__ScopeDict___repr__():
    def mock_avm_class_name(this):
        return 'mock_avm_class_name'
    _ScopeDict._ScopeDict__avm_class_name = mock_avm_class_name
    assert repr(_ScopeDict(None)) == 'mock_avm_class_name__Scope({})'



# Generated at 2022-06-14 18:25:20.317851
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    from .tag import TagImportAssets2
    from .tag import TagDoABC

    import_assets_tag = TagImportAssets2([
        (
            'net.wonderbit.videoeditor.Clip',
            [
                'Clip',
                'cutClip',
                'cutAllClips',
                'getTotalTime',
                'getTimeUnit',
                'getTime',
                'getColor',
                'getSticker',
                'getTransition',
                'getTransitionIn',
                'getTransitionOut',
                'getTransitionTime',
            ],
        ),
    ])
    avmcode_tag = TagDoABC()
    avmcode_tag.code = '\x10\x00\x2e\x00'

# Generated at 2022-06-14 18:25:31.993671
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2022-06-14 18:25:38.255554
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    from .compat import compat_struct_pack
    from .swf.swftags import SWFDefineBinaryDataTag

    s = SWFInterpreter()
    # We need to add at least one class, otherwise the SWF class won't contain
    # any functions
    s.read_class_swf(SWFDefineBinaryDataTag('', b"\x00", ''))


# Test building a simple class

# Generated at 2022-06-14 18:25:46.288884
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2022-06-14 18:25:56.039970
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    def test_interpreter(si_):
        assert si_.extract_function([1, 2, 3]) == 6
        assert si_.extract_function([1]) == 1

    import zlib
    from io import BytesIO


# Generated at 2022-06-14 18:26:07.499487
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    def docreate(self):
        obj = {}
        obj['this'] = obj
        obj['a'] = 1
        obj['b'] = 12
        obj['c'] = 'ok'
        return obj

    def dosum():
        return this.a + this.b

    def dosum2():
        return a + b
        
    def dosum3():
        return this.a + this.b + this.c
        
    def dosum4(c):
        return this.a + this.b + c + this.c
        
    def _test_method_patch(src_func, expected_res):
        swfi = SWFInterpreter(docreate, dosum, dosum2, dosum3, dosum4)

# Generated at 2022-06-14 18:26:17.274295
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    from .swf import SWF
    with open('test/swfs/as2-ActionScript2_0.swf', 'rb') as f:
        swf = SWF(f)
    with open('test/swfs/as2-ActionScript2_0.abc', 'rb') as f:
        abcs = find_abc_blocks(f)
    avm_classes = set()
    for abc in abcs:
        avm_class = SWFInterpreter.parse_abc(abc)
        avm_classes.add(avm_class)
    interp = SWFInterpreter(avm_classes, swf)

    class_obj = interp.parse_class('com.longtailvideo.jwplayer.view::View')
    class_obj.extract_methods()

# Generated at 2022-06-14 18:26:25.285085
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    from swftools.abce.actions import ActionPush
    from swftools.abce.actions import ActionPushRegister
    from swftools.abce.actions import ActionPushConst
    from swftools.abce.actions import ActionPushString
    from swftools.abce.actions import ActionPushBoolean
    from swftools.abce.actions import ActionPushNull
    from swftools.abce.actions import ActionCoerce
    from swftools.abce.actions import ActionAdd
    from swftools.abce.actions import ActionSubtract
    from swftools.abce.actions import ActionMultiply
    from swftools.abce.actions import ActionDivide
    from swftools.abce.actions import ActionModulo
    from swftools.abce.actions import ActionAnd

# Generated at 2022-06-14 18:26:35.558282
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    swf_interpreter = SWFInterpreter(
        'http://localhost:80', b'\x00' * 1024,
        ['A', 'B', 'C', 'D', 'E'])
    assert swf_interpreter.swf_url == 'http://localhost:80'
    assert swf_interpreter.swf_bytes == b'\x00' * 1024
    assert swf_interpreter.host_str == 'A'
    assert swf_interpreter.host_exe == 'B'
    assert swf_interpreter.host_version == 'C'
    assert swf_interpreter.version == 'D'
    assert swf_interpreter.autoplay == 'E'


# Generated at 2022-06-14 18:28:14.050827
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    swf = SWFInterpreter()

    # class C1

# Generated at 2022-06-14 18:28:20.738467
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    from .tag_types import PARSER_METADATA_ATTRIBUTE_TYPE_CONSTANT_8
    from .parser import TagParser
    tag_parser = TagParser(PARSER_METADATA_ATTRIBUTE_TYPE_CONSTANT_8)
    tag_parser.read(b'\x11\x12\x13\x14')
    assert tag_parser.attribute_type == 0x11
    assert tag_parser.attribute_name == b'\x12\x13\x14'



# Generated at 2022-06-14 18:28:29.121231
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    from .util import bin_to_hexstr
    from .abc import parse_abc_file

    # The following binary file is from a ABC block of
    # http://cp7733.com/file/swf/denglu.swf

# Generated at 2022-06-14 18:28:37.699263
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    s = SWFInterpreter()
    avm_class = s.make_class()

    def test_function(name, code, expected, func_args=[]):
        func = cStringIO.StringIO(code)
        s.extract_function(avm_class, name, '', func, None, func_args)
        func = avm_class.method_pyfunctions[name]
        assert func() == expected

    test_function('func', '\x03\x00\x00\x00\x2a\x00\x00\x00\x55\x00\x00\x00\x47\x00\x00\x00\x3f\x00\x00\x00', True)

# Generated at 2022-06-14 18:28:48.847616
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    filename = os.path.join(os.path.dirname(__file__), 'test.swf')
    with open(filename, 'rb') as f:
        swf = f.read()

    interpreter = SWFInterpreter(swf)
    assert len(interpreter.constant_strings) == 33

# Generated at 2022-06-14 18:28:55.875957
# Unit test for method __repr__ of class _ScopeDict
def test__ScopeDict___repr__():
    scope_dict = _ScopeDict(object)
    scope_dict[b'result'] = b'result of method'
    scope_dict[b'var'] = 42
    assert repr(scope_dict) == 'object__Scope({\'result\': \'result of method\', \'var\': 42})'

# Generated at 2022-06-14 18:28:58.466663
# Unit test for method __repr__ of class _ScopeDict
def test__ScopeDict___repr__():
    sd = _ScopeDict(None)
    sd['k'] = 'v'
    assert repr(sd) == 'None__Scope({\'k\': \'v\'})'



# Generated at 2022-06-14 18:29:01.168938
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    contents = open('tests/swfbytes', 'rb').read()
    assert SWFInterpreter(contents, raise_on_error=True), \
        'Cannot parse the swf file'


# Generated at 2022-06-14 18:29:02.221747
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2022-06-14 18:29:11.014520
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2022-06-14 18:31:40.905932
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    # SWFInterpreter_func_patch
    pass



# Generated at 2022-06-14 18:31:51.281100
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    import io

# Generated at 2022-06-14 18:32:02.018585
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2022-06-14 18:32:09.998911
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    from .parse_swf import SWFParser
    from .make_avm import AVMClass
    from .utils import SWF
    from .bytearray_io import BytearrayIOWrapper

    swfparser = SWFParser()
    s = '6F00530053002E00610076006D002E004400610074006100440065006300680061006E006E006100540065006300680061006E006E00650072002E00650072006F003200'
    s = s.decode('hex')
    f = BytearrayIOWrapper(s)
    swf = swfparser.parse_swf(f, None)
    swf = SWF(swf)

# Generated at 2022-06-14 18:32:18.385165
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2022-06-14 18:32:20.147988
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    # TODO
    pass

# Generated at 2022-06-14 18:32:32.199161
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2022-06-14 18:32:41.332895
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2022-06-14 18:32:51.201919
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    # Test extract_function of class SWFInterpreter class
    interpreter = SWFInterpreter()
    name = 'doSomething'
    type_name = 'Foo'
    code = ''.join(['%02x' % b for b in range(256)])
    interpreter.define_function(name, type_name, code)
    res = interpreter.extract_function(interpreter.classes[type_name], name)
    assert res(['foo']) == 'foo'


# Extract an AVM2 constant pool from a full SWF file path or file-like object

# Generated at 2022-06-14 18:32:53.323752
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    # TODO: Implement test
    raise NotImplementedError()

