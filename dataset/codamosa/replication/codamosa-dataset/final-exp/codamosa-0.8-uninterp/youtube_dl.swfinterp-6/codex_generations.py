

# Generated at 2022-06-14 18:25:25.647937
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():

    const_str = [
        '', '', '', '',
        'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='
    ]
    si = SWFInterpreter(const_str=const_str)

    si.extract_function(si.StringClass, "fromCharCode")

    code_bytes = compat_chr(0) * 2 + compat_chr(2) + compat_chr(215)
    code_bytes += compat_chr(47) + compat_chr(0) + compat_chr(128) + compat_chr(9)
    code_bytes += compat_chr(39) + compat_chr(0) + compat_chr(4)

# Generated at 2022-06-14 18:25:36.946503
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    import unittest
    test_case = unittest.TestCase()

    class MySWFInterpreter(SWFInterpreter):
        def read_bytes(self, n):
            return b'\x10' * n

    swfi = MySWFInterpreter()
    swfi.constant_strings = ['test_string']
    swfi.constant_namespaces = ['test_namespace']
    swfi.multinames = ['test_name']
    swfi.methods = [[0, 0, 0, 0]]

    def get_method(func_name):
        return {'test_name': [(0, 0)]}[func_name][0]

    class AVMClass(object):
        method_pyfunctions = {}
        method_names = ['test_name']
        variables = {}


# Generated at 2022-06-14 18:25:42.069285
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    interp = SWFInterpreter()
    interp.patch_function(
        'String',
        'fromCharCode',
        [['charCode']],
        '''
        return String.fromCharCode(charCode);
        ''')

    ret = interp.exec_function('String', 'fromCharCode', [65])
    assert ret == 'A'


# Class SWFType

# Generated at 2022-06-14 18:25:54.413106
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    """Tests for SWFInterpreter.extract_function method."""

# Generated at 2022-06-14 18:25:58.113738
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    class T(object):
        pass
    r = SWFInterpreter(None, None)
    t = T()

    def add(args):
        return args[0] + args[1]
    r.patch_function(t, add)

    assert t.add([3, 4]) == 3 + 4
    assert t.add([5, -1]) == 5 - 1



# Generated at 2022-06-14 18:26:03.322502
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2022-06-14 18:26:06.954780
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    sample_swf = TEST_SWF_URL
    # sample_swf = 'http://www.youtube.com/apiplayer?version=3'
    interpreter = SWFInterpreter(sample_swf)
    assert isinstance(interpreter, SWFInterpreter)


# Generated at 2022-06-14 18:26:14.070025
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2022-06-14 18:26:23.930193
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    swf_interpreter = SWFInterpreter()

# Generated at 2022-06-14 18:26:35.187422
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    import sys
    import os
    import os.path
    from selenium.webdriver import compat
    abspath = compat.abspath(__file__)
    faketimetools = os.path.join(os.path.dirname(__file__), 'faketime.py')
    faketimetools_path = os.path.join(os.path.dirname(__file__), 'faketimetools.py')
    env = os.environ.copy()


# Generated at 2022-06-14 18:27:27.311082
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    opcodes = [
        (158, [3, 0]),
        (48, [0]),
        (72, []),
        (67, [0, 0])]
    func = build_function(opcodes)
    interpreter = SWFInterpreter()
    interpreter.patch_function(func, 'test_function')
    res = func()
    assert res == [None, None, None]


# Generated at 2022-06-14 18:27:39.015263
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    # Build a small SWF file containing the following ActionScript code:
    #
    # class test {
    #   public static function get_attr(): int {
    #     return 1;
    #   }
    # }
    # var array:Array = [test,test.get_attr()];
    # return array;

    swf = _SWFInterpreter()
    swf_file = BytesIO()
    writer = SWFWriter(swf_file, 'FWS')
    writer.write_header()
    writer.write_u8(0)
    writer.write_u16(0)
    writer.write_ub(2, 3)
    writer.end_tag()
    writer.flush()
    swf_file.seek(0)
    swf.parse(swf_file)
    sw

# Generated at 2022-06-14 18:27:45.883217
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    from io import BytesIO

    interpreter = SWFInterpreter()
    interpreter.add_binary_data(BytesIO(compat_struct_pack('>H', 123)))
    parser = SWFParser(interpreter)
    parser.parse(BytesIO(compat_struct_pack('>H', 456)))

    assert len(interpreter.constant_strings) == 0

    # Patch the test method

# Generated at 2022-06-14 18:27:50.059952
# Unit test for method __repr__ of class _ScopeDict
def test__ScopeDict___repr__():
    scope = _ScopeDict(dummy_class)
    scope['a'] = 1
    scope['z'] = 2
    assert repr(scope) == 'dummy_class__Scope({\'a\': 1, \'z\': 2})'



# Generated at 2022-06-14 18:27:59.720184
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():

    swfi = SWFInterpreter(b'mytestswf')

    with open(os.path.join(SWF_DATA_DIR, 'test.swf'), 'rb') as f:
        swf = SWF(f)
    tag = swf.read_tag()
    assert isinstance(tag, DoABCOp)
    assert tag.flags == 0
    assert tag.name == '!test'
    assert tag.data == b'<abc>\n'

    swfi.extract_function(tag.data)

    tag = swf.read_tag()
    assert isinstance(tag, DoABCOp)
    assert tag.flags == 1
    assert tag.name == 'TestCase'
    assert tag.data == b'<abc>\n'

    # TestCase.test_string_access
    generated

# Generated at 2022-06-14 18:28:10.324401
# Unit test for constructor of class SWFInterpreter

# Generated at 2022-06-14 18:28:19.966469
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    with open('test/swf_interpreter/Test.swf', 'rb') as f:
        swf_data = f.read()
    swf = SWF(swf_data)
    intf = swf.swf_interpreter
    cls = intf.avm_classes['Test']
    intf.patch_function(cls, 'test_string')
    print(cls.test_string)
    (test_string_coder, test_string_stack,
    test_string_registers, test_string_scope) = cls.test_string

    intf.patch_function(cls, 'test_concat')
    print(cls.test_concat)

# Generated at 2022-06-14 18:28:25.528463
# Unit test for method register_methods of class _AVMClass
def test__AVMClass_register_methods():
    class_obj = _AVMClass(0, 'Foo')
    class_obj.register_methods({
        'bar': 0x100,
        'baz': 0x104,
    })
    assert class_obj.method_names == {
        'bar': 0x100,
        'baz': 0x104,
    }
    assert class_obj.method_idxs == {
        0x100: 'bar',
        0x104: 'baz',
    }



# Generated at 2022-06-14 18:28:27.379420
# Unit test for method __repr__ of class _ScopeDict
def test__ScopeDict___repr__():
    t = _ScopeDict(_AVMClass({'name': 't'}))
    assert repr(t) == "t__Scope({})"



# Generated at 2022-06-14 18:28:37.515838
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2022-06-14 18:29:39.444459
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    # Get the abc tag, which is always the last tag
    abc_tag = None
    with open('test.swf', 'rb') as f:
        f.seek(8)  # Skip the header
        while True:
            code = ord(f.read(1))
            if code == 0:  # End tag
                break
            length = struct.unpack('<I', f.read(4))[0]
            f.seek(length, 1)  # Jump to the next tag
            if code == 82:  # abc tag
                abc_tag = f.read(length)

    abc = SWFInterpreter(abc_tag)
    abc.run()

if __name__ == '__main__':
    test_SWFInterpreter()

# Generated at 2022-06-14 18:29:47.002515
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    testdata_url = 'https://github.com/rg3/youtube-dl/raw/master/test/data/'
    expected_url = testdata_url + 'adobepass_test_vevo.txt'
    encoded_url = testdata_url + 'adobepass_test_vevo.swf'
    expected_data = compat_urllib_request.urlopen(expected_url).read().decode('utf-8')
    encoded_data = compat_urllib_request.urlopen(encoded_url).read()
    swf = SWFInterpreter(encoded_data)
    assert swf.extract_class() == expected_data

# Tests for _AVMClass_Object


# Generated at 2022-06-14 18:29:56.617658
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    data = open('test/test_data/classTest.swf', 'rb').read()
    assert isinstance(data, bytes)
    swf = SWF(BytesIO(data), parse_header=False)
    interpreter = SWFInterpreter(swf)
    interpreter.extract_classes()
    assert len(interpreter.classes) == 1
    assert len(list(interpreter.classes)) == 1
    assert isinstance(list(interpreter.classes)[0], _AVMClass)
    assert list(interpreter.classes)[0].name == 'classTest'
    assert 'constructor' in list(interpreter.classes)[0].static_properties
    assert 'length' in list(interpreter.classes)[0].static_properties

# Generated at 2022-06-14 18:30:05.606608
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    swf = open(os.path.join(os.path.dirname(__file__),
                            'swf-example1.swf'), 'rb').read()
    avm = SWFInterpreter(swf)
    assert len(avm.strings_map) == 0
    assert len(avm.constant_strings) == 2
    arr = avm.constant_strings
    assert isinstance(arr[1], compat_str)

# Test the SWFInterpreter.find_main routine

# Generated at 2022-06-14 18:30:09.846314
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    # Check that constructor does not raise errors
    # for file test.swf
    avm = SWFInterpreter('test.swf')


# Generated at 2022-06-14 18:30:20.418796
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    class AVMInterpreterTest(AVMInterpreter):
        def __init__(self):
            AVMInterpreter.__init__(self)
            self.constant_strings = ['a', 'b']
            self.constant_names = ['', '']
        def extract_function(self, avm_class, name):
            if name == 'get_a':
                return lambda args: avm_class.static_properties['a']
            elif name == 'set_a':
                return lambda args: avm_class.static_properties.__setitem__('a', args[0])
            elif name == 'identity':
                return lambda args: args[0]
            elif name == 'f':
                return lambda args: None
            elif name == 'x':
                return lambda args: avm

# Generated at 2022-06-14 18:30:28.039620
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    swf = SWFInterpreter()
    f = TestCase().swf_data('rtmp.swf')
    with open(f, 'rb') as inf:
        swf.parse_header(inf.read(8))
        data = inf.read()

    swf.parse_body(data)
    assert swf.version != -1
    assert swf.frame_size is not None
    assert len(swf.tags) > 0


# Generated at 2022-06-14 18:30:38.193567
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2022-06-14 18:30:41.286057
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    swf = SWFInterpreter()
    swf.parse_bytes(b'ZWS')
    assert swf.file_version == 9
    assert swf.file_length == 0


# Code of SWFPlayer

# Generated at 2022-06-14 18:30:48.204076
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    from . import _tests_data
    from .abc import ABCFile
    abc_file = ABCFile.load(
        open(_tests_data.get_path_for_data_file('sample.abc'), 'rb'))
    avm_class = SWFInterpreter.extract_class(abc_file)
    return avm_class


# Generated at 2022-06-14 18:32:44.206071
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    interp = SWFInterpreter()
    interp.constant_strings = ['zzz']
    interp.multinames = [123]
    interp.methods = [
        #   0: GetLocal0
        #   1: PushString zzz
        #   3: SetLocal0
        #   4: GetLocal0
        #   5: PushString 123
        #   7: SetProperty
        #   8: ReturnVoid
        [0, 1, 0, 3, 0, 4, 1, 3, 5, 7, 8],
    ]

# Generated at 2022-06-14 18:32:48.726129
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    from .util import make_swf_interpreter
    avm = make_swf_interpreter()
    avm.extract_class(
        avm.constant_classes[avm.constant_multinames[1].idx])



# Generated at 2022-06-14 18:32:52.586022
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    class_obj = _AVMClass({}, {})
    interp = SWFInterpreter({}, {}, {}, {}, class_obj)
    def f(x):
        return x + 1
    resfunc = interp.extract_function(class_obj, 'f')
    assert resfunc(5) == f(5)



# Generated at 2022-06-14 18:33:01.959294
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2022-06-14 18:33:10.692093
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    from .consts import SWF_MAGIC
    f = io.BytesIO()
    f.write(SWF_MAGIC)
    f.write(b'\x87\x00\x00\x00')
    f.write(b'\x00\x00\x00\x00')
    f.write(b'\x00\x00\x00\x00')
    f.write(b'\x00\x00')
    f.write(b'\x00\x00\x00\x00')
    f.write(b'\x00\x00\x00\x00')
    f.write(b'\x00\x00\x00\x00')
    f.write(b'\x00\x00\x00\x00')
    f.write

# Generated at 2022-06-14 18:33:18.852383
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    from .flash_proxy import make_flash_class  # pylint: disable=import-error
    from . import avm1_handler  # pylint: disable=import-error
    from . import utils  # pylint: disable=import-error
    swfi = SWFInterpreter()

    class AVM1_Class(object):
        make_object = lambda self: None
        variables = {}
        static_methods = {}
        static_properties = {}
        __name__ = 'AVM1_Class'

    avm1_handler.AVM1_Class = AVM1_Class
    action_handler = utils.ActionHandler(dict(MouseEvent=AVM1_Class))

# Generated at 2022-06-14 18:33:29.408117
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    from .swf_utils import Tag, TAG_DoABC, ABCFile
    from .swf_tag_data import TAG_DATA_ABC_TYPE
    name = TAG_DATA_ABC_TYPE[TAG_DoABC]

    si = SWFInterpreter()
    t = Tag(TAG_DoABC, name)
    # t.raw_data = raw_data

    # fake ABC file
    abc = ABCFile()
    si.abc_files.append(abc)
    si.abc_file = abc
    si.extract_function(si, 'test1')
    si.extract_function(si, 'test2')
    si.extract_function(si, 'test3')
    si.extract_function(si, 'test4')

    t.process(si)

#------------------------------------------------------------------------------#
#

# Generated at 2022-06-14 18:33:36.055465
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    interpreter = SWF('tests/swf/shapes.swf', True)
    interpreter.extract_function('Shape', 'addShape', ['shapeId', 'shape'])


_builtin_classes = {
    'Array': list,
    'String': compat_str,
    'Boolean': bool,
}



# Generated at 2022-06-14 18:33:44.391841
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    import io
    import collections
    import os.path

    # patch_function function to be unit tested
    def patch_function(self, swf_parser, avm_class, func_name):
        def resfunc(*args, **kwargs):
            raise AssertionError(
                'Function %s should have been patched' % func_name)

        assert func_name in avm_class.method_names
        assert func_name not in avm_class.method_pyfunctions

        # Compute a string to be used as cache key
        # md5_module is used as reference implementation
        # https://hg.python.org/cpython/file/3.6/Lib/hashlib.py#l297
        hasher = swf_parser.hash_module.md5()

# Generated at 2022-06-14 18:33:51.704558
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():

    def to_run(obj):
        return obj['toString']()

    interpreter = SWFInterpreter()
    interpreter.extract_class(_builtin_classes['Object'])
    interpreter.constant_strings = [
        'toString', 'asfunction', 'Number', '$Bgcolor', '$Bheight', '$Bwidth',
        '$B_alpha', '$Bx', '$By', '$Brotation', 'Boolean', 'true', 'false',
        'Array', 'toString', 'slice', 'join', 'String', 'split', 'charCodeAt',
        'NaN'
    ]