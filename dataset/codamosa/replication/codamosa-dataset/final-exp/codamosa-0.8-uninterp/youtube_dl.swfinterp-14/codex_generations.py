

# Generated at 2022-06-14 18:25:30.983145
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    obj = SWFInterpreter()
    obj.extract_function()

# Generated at 2022-06-14 18:25:41.482029
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2022-06-14 18:25:49.007320
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    swf = open('tests/resources/swfs/test3.swf', 'rb').read()
    interpreter = SWFInterpreter(swf)
    assert len(interpreter.tags_types) == 62
    assert interpreter.avm_type == 'AVM2'
    assert interpreter.constant_strings[0] == 'str'
    assert interpreter.constant_strings[1] == 'en'
    assert interpreter.constant_strings[2] == 'foo'
    assert interpreter.constant_strings[3] == 'bar'
    assert interpreter.constant_strings[1857] == 'display'
    assert interpreter.constant_ints[0] == -1
    assert interpreter.constant_ints[1] == 0
    assert interpreter.constant_ints[2] == 1
    assert interpreter.constant_

# Generated at 2022-06-14 18:25:57.785672
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    from .bitstream import BitStream
    from .flash_constants import TAG_SCRIPT_LIMITS, TAG_DO_ABC, TAG_DEFINE_BITS_JPEG3
    from .flash_constants import TAG_DEFINE_BITS_LOSSLESS2, TAG_SHOW_FRAME
    from .flash_constants import TAG_END

    swf = BitStream()
    swf.write_bytes(b'FWS')
    swf.write_u8(0)  # Version
    swf.write_uint32(0)  # File size

    swf.write_tag_header(TAG_SCRIPT_LIMITS, 10)
    swf.write_u16(1)  # Max recursion depth
    swf.write_u16(1)  # Script timeout in seconds

    swf

# Generated at 2022-06-14 18:26:08.999726
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    class_name = 'Function'
    coder = compat_io.BytesIO(b'\x01\x00\x0b\x00\x00')
    scopes = []
    # FIXME: Method "patch_function" of class SWFInterpreter
    # is not tested
    swf = SWFInterpreter(None, '', None)
    # FIXME: Method "patch_function" of class SWFInterpreter
    # is not tested
    res = swf.patch_function(
        None, class_name, '', '', coder, scopes)
    assert res is not None


# Class SWF

# Generated at 2022-06-14 18:26:18.446446
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    interpreter = SWFInterpreter()
    interpreter.constant_strings = [
        'some_string', '_level0', '_root', 'length']
    interpreter._register_multiname(
        5,
        _Multiname(is_runtime = True),
        [_Multiname(
            namespaces = [],
            name = '_level0',
            name_type = 'string',
            is_runtime = False),
         _Multiname(
            namespaces = [],
            name = '_root',
            name_type = 'string',
            is_runtime = False)],
        [_Multiname(
            namespaces = [],
            name = 'length',
            name_type = 'string',
            is_runtime = False)])

# Generated at 2022-06-14 18:26:24.885584
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    if not IS_PYTHON2:
        raise SkipTest('Test only runs on Python 2')

    _SWFInterpreter_class_members = [
        'constant_strings', 'multinames', 'method_body_infos']
    with open(test_utils.get_test_file_path('test.swf')) as f:
        data = f.read()
    s = SWFInterpreter(data)
    assert isinstance(s.constant_strings, list)
    assert isinstance(s.multinames, list)
    assert isinstance(s.method_body_infos, list)

# Generated at 2022-06-14 18:26:34.132491
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    from .test_files import swf_files

    swf_info = swf_files['test_hello.swf']
    swf_interpreter = SWFInterpreter(swf_info['file_contents'])
    assert len(swf_interpreter.extract_classes()) == 1
    hello_class = swf_interpreter.extract_classes()[0]
    assert len(hello_class.method_pyfunctions) == 1
    hello = hello_class.method_pyfunctions['hello']
    assert hello() == {'x': 1.0, 'y': 0.5}



# Generated at 2022-06-14 18:26:45.721397
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    class _Clip(object):
        def _init_fields_(self):
            pass
    clip = _Clip()
    clip.ncid = 14
    clip.ncname = 'test'

    class _AVM(object):
        def call_method(self, methodname, arg):
            return methodname, arg

        def get_field(self, fieldname):
            if fieldname is None:
                fieldname = 'None'
            return fieldname

        def set_field(self, fieldname, value):
            return (fieldname, value)

        def get_property(self, propname, obj):
            if obj is None:
                obj = 'None'
            return propname, obj

        def set_property(self, propname, obj, value):
            if obj is None:
                obj = 'None'


# Generated at 2022-06-14 18:26:49.254493
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    with open('../../test/swf/as3.swf', 'rb') as f:
        swf = SWF(f)
    swf_interpreter = SWFInterpreter(swf)

if __name__ == '__main__':
    test_SWFInterpreter()

# Generated at 2022-06-14 18:27:58.705476
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    swf_interpreter = SWFInterpreter()
    swf_interpreter.version = 14
    swf_interpreter.method_count = 1
    swf_interpreter.class_count = 0
    swf_interpreter.classes = []

# Generated at 2022-06-14 18:28:09.425479
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    from avm_utils import SWFInterpreter
    from avm_utils import _AVMClass_Object
    from avm_utils import _AVMClass
    from avm_utils import _ScopeDict
    from avm_utils import _Multiname
    from avm_utils import _Undefined
    from avm_utils import StringClass
    from avm_utils import _builtin_classes

    with open('tests/swf/swf_int_extract_class.swf', 'rb') as f:
        assert f.read(3) == b'CWS'
        coder = BytesIO(f.read())
    interpreter = SWFInterpreter(coder, extract_classes=False)
    interpreter.extract_class(0)

    # Test the extracted classes
    assert interpreter.constant_strings

# Generated at 2022-06-14 18:28:19.516634
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    from yxdswf.swftags import SWFTagDoABC

    with open('test/test-swfs/bug-decode.swf', 'rb') as stream:
        swf = SWF(stream)
    swf_intrprtr = SWFInterpreter(swf)
    abc_tags = [t for t in swf.tags if isinstance(t, SWFTagDoABC)]
    assert len(abc_tags) == 1
    swf_intrprtr.extract_class(abc_tags[0].abc)

    for name, cls in swf_intrprtr.builtin_classes.items():
        if not isinstance(cls, _AVMClass):
            continue
        assert hasattr(cls, '__name__'), 'Class %r has no name' % cls

# Generated at 2022-06-14 18:28:28.028394
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    from .parse import Tag_DoABC, Tag_DoInitAction, Tag_DoABC_Flags
    from .tags import Tag_SymbolClass
    from .swf import SWF

    DOABC_FLAGS = Tag_DoABC_Flags(
        AS3=1, has_abc_data=1,
    )
    DOABC = Tag_DoABC(
        flags=DOABC_FLAGS,
        name='main',
        abc=b'',
    )

    DOINITACTION = Tag_DoInitAction(
        sprite_id=0,
        actions=[],
    )

    SYMCLASS = Tag_SymbolClass(
        objects=[],
    )


# Generated at 2022-06-14 18:28:38.351022
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    # test for code with variable length encoding (vle).
    tag1 = SWFTag()

# Generated at 2022-06-14 18:28:49.390572
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    from .tags import Tag
    from .abcfile import ABCFile
    from .debug import add_debug_info
    from .bits import read_u30

    t = Tag(b'\x00\x00\x00\x00\x00\x00\x00')
    abcfile = ABCFile(0)
    add_debug_info(t, abcfile)
    interpreter = SWFInterpreter(t, abcfile)

    # Attributes

    # constant_strings
    assert interpreter.constant_strings == []

    # multinames
    assert interpreter.multinames == []

    # methods
    assert interpreter.methods == {}

    # method_pyfunctions
    assert interpreter.method_pyfunctions == {}

    # class_names
    assert interpreter.class_names == []

    # classes
   

# Generated at 2022-06-14 18:29:00.277459
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    interp = SWFInterpreter()

    constant_strings = [
        '_global',
    ]
    methods = []
    multinames = [
        None,
        _Multiname(['_global'], [0]),
    ]
    body = io.BytesIO(compat_chr(12))

    method = _Method(0, 0, 2, 0, 2, body)

    methods.append(method)

    avm_class = interp.make_avm_class('_global', methods, multinames,
                                      constant_strings)

    resfunc = interp.extract_function(avm_class, 'f')
    assert resfunc([]) == None


# Generated at 2022-06-14 18:29:10.646137
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    '''
    Test for swfdec.SWFInterpreter.
    '''
    from .swftags import TagDefineBinaryData
    from .swfdec import SWFInterpreter
    from .utils import BytesIO


# Generated at 2022-06-14 18:29:12.710358
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    swf = SWFInterpreter()
    swf._code_cacher = {'code1': None}  # Override to prevent IO
    swf.extract_function(None, 'code1')



# Generated at 2022-06-14 18:29:16.359005
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    swf_file = open(get_testfile_path('youtube.swf'), 'rb')
    swf = SWF(swf_file)
    interpreter = SWFInterpreter(swf)
    interpreter.extract_class(swf.tags[0].avm2)



# Generated at 2022-06-14 18:30:31.345766
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    from .test_swfdecompiler import (
        TEST_SWF_DECOMPILER, read_test_swf)
    with open(TEST_SWF_DECOMPILER, 'rb') as f:
        swf = read_test_swf(f)
    assert swf.header['Version'] == 10
    assert swf.tags[0].__class__.__name__ == 'FileAttributesTag'
    assert swf.tags[1].__class__.__name__ == 'SetBackgroundColorTag'
    assert swf.tags[2].__class__.__name__ == 'DefineShapeTag'
    assert swf.tags[3].__class__.__name__ == 'DefineShapeTag'

# Generated at 2022-06-14 18:30:40.659294
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():

    class AVMClass(object):
        def __init__(self, variables):
            self.variables = variables
            self.static_properties = {
                'Array': _builtin_classes['Array'],
                'String': _builtin_classes['String'],
                'Number': _builtin_classes['Number'],
                'StringTools': _builtin_classes['StringTools'],
            }

        def make_object(self):
            return _ScopeDict(self)

    def func_test(args):
        assert len(args) == 1
        return args[0]

    interp = SWFInterpreter()
    avm_class = AVMClass({})
    interp.patch_function(avm_class, 'test', func_test)
    func = avm_class.method_pyfunctions

# Generated at 2022-06-14 18:30:50.405236
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    swftools_cmd = find_executable('swfdump')
    assert swftools_cmd

    output = subprocess.check_output([
        swftools_cmd, '-a',
        os.path.join(DATA_DIR, 'avm2.swf'),
    ]).decode('utf-8')

    p = SWFInterpreter(output)

    class_ = p.extract_class('flash.utils.Proxy')

    assert (
        class_.method_pyfunctions['$construct']([]) ==
        _AVMClass_Object({
            'flash$utils$flash$utils$Proxy': ProxyClass,
        }))



# Generated at 2022-06-14 18:30:59.899273
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2022-06-14 18:31:06.342371
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    swf = SWFInterpreter('test/test-swfdec.swf')
    codeblock = swf.action_blocks[0].bytecode
    avm_class = swf._avmclasses[-1]
    swf.extract_function(avm_class, 'main')
    swf.avm_classes[0].method_pyfunctions['main']([])



# Generated at 2022-06-14 18:31:14.046740
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    import io
    import struct
    import unittest
    import zlib
    from svtplay_dl.utils.flash_proxy_python import SWFInterpreter

    class TestSWFInterpreter(unittest.TestCase):
        def setUp(self):
            self.si = SWFInterpreter()

            # 0 getlocal_0
            # 1 pushscope
            # 2 findpropstrict String
            # 3 pushstring 'f1'
            # 4 constructprop String (1)
            # 5 setproperty __PYTHON__ (0)
            # 6 getlex String
            # 7 pushstring 'f1'
            # 8 callpropvoid String (1)
            # 9 returnvoid

# Generated at 2022-06-14 18:31:19.494168
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    si = SWFInterpreter()
    si.constant_strings = [
        'abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz']

    multinames = [
        _Multiname('abc'), _Multiname('def'), _Multiname('ghi'),
        _Multiname('jkl'), _Multiname('mno'), _Multiname('pqr'),
        _Multiname('stu')]
    si.multinames = multinames

    coder = compat_BytesIO()
    def w_u30(n):
        coder.write(struct.pack('!I', n)[1:])
    def w_byte(n):
        coder.write(struct.pack('!B', n))

# Generated at 2022-06-14 18:31:25.590573
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    with open('test.swf', 'rb') as f:
        contents = f.read()
    interpreter = SWFInterpreter(contents)

    res = interpreter.extract_class('NetStream')
    check_result(res, {
        'extract_symbol_class':
            "<class 'youtube_dl.extractor.flashmedia.SWFInterpreter.SWFInterpreter._AVMClass'>",
    })
    assert res.extract_symbol_class

# Generated at 2022-06-14 18:31:34.639472
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    interpreter = SWFInterpreter(open('test1.swf', 'rb'))

    def t(func, *args):
        return interpreter.extract_pyfunction(func, *args)

    assert t('asGetPublicProperty', 'e', 'd') == 'public'
    assert t('asGetPrivateProperty', 'e', 'd') == 'private'
    assert t('asGetGlobalProperty', 'd') == 'global'
    assert t('asGetGlobalProperty') == 99
    assert t('asGetGlobalProperty', 'e') == undefined
    assert t('asGetStaticProperty', 'e', 'd') == 'static'

test_SWFInterpreter()

# Generated at 2022-06-14 18:31:38.255199
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    with open(os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'fixture', '2.swf'), 'rb') as f:
        swf = SWF(f, strict=False)

    swf.extract_function
import json

# Generated at 2022-06-14 18:32:56.608796
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    import os
    import subprocess
    from pyasn1.compat.octets import *

    file_name = '/tmp/test.swf'

    tag_file = open(file_name, 'wb')
    tag_file.write(hex2bytes(
        '43 01 00 00 00 00 00 00 01 00 00 00 01 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'))
    tag_file.write(b'\x00\x00\x00\x00')
    tag_file.write(hex2bytes(
        '00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'))
    tag_file.write(b'\x00\x00\x00\x00')
    tag

# Generated at 2022-06-14 18:33:07.786582
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    from .test_swf_interpreter import fixture  # noqa
    swf_interpreter = SWFInterpreter(fixture)
    swf_interpreter.extract_function(
        swf_interpreter.avm_classes['com.jeroenwijering.parsers::RtmpParser'],
        'parseUrl')


if __name__ == '__main__':
    import sys
    import unittest
    if sys.argv[-1] == '-v':
        unittest.TestCase.maxDiff = None
        del sys.argv[-1]
    unittest.main()

# Generated at 2022-06-14 18:33:17.474456
# Unit test for constructor of class SWFInterpreter

# Generated at 2022-06-14 18:33:22.338240
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    swf_interpreter = SWFInterpreter('test_interpreter.swf')
    assert swf_interpreter.constant_strings == \
        ['MainTimeline', 'onLoad', 'main', 'loaderInfo', 'backgroundColor']
    assert isinstance(swf_interpreter.classes['MainTimeline'], _AVMClass)



# Generated at 2022-06-14 18:33:28.248191
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    with open(os.path.join(
            os.path.dirname(__file__),
            'tests/swfs/dummy.swf'), 'rb') as f:
        swf = _read_swf(f)
    swf.patch_function('checkString', lambda x: False)

    assert swf.main_class.method_pyfunctions['checkString']('foobar') is False

# Generated at 2022-06-14 18:33:40.136237
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2022-06-14 18:33:49.667842
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    # This test case checks for the patches
    # for classes in the SWF file 'YouTube HTML5 embed as of 2014.11.01.swf'
    test_cases = []
    base_dir = os.path.dirname(os.path.abspath(__file__))
    swf_file_path = os.path.join(base_dir, 'tests', 'test_patches.swf')
    swf = open(swf_file_path, 'rb').read()
    swf_id = swf_file_path.encode()

    # The SWF file 'YouTube HTML5 embed as of 2014.11.01.swf'
    # contains a VideoPlayer class and a YouTubeVideoPlayer class.
    # The class VideoPlayer has a method called 'toString'
    # and the class YouTubeVideoPlayer extends the class

# Generated at 2022-06-14 18:33:50.993720
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    # FIXME test this
    pass

# Generated at 2022-06-14 18:33:59.972735
# Unit test for constructor of class SWFInterpreter