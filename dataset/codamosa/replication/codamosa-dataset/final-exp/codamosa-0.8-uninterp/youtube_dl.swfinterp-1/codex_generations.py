

# Generated at 2022-06-14 18:24:44.073134
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    import io
    import struct
    import unittest

    class FakeAVMClass(object):
        def __init__(self):
            self.method_names = set()
            self.static_properties = {}
            self.method_pyfunctions = {}

        def __getitem__(self, key):
            return self.static_properties[key]

        def __setitem__(self, key, value):
            self.static_properties[key] = value

        def make_object(self):
            return _ScopeDict(self)


# Generated at 2022-06-14 18:24:50.479165
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    assert isinstance(SWFInterpreter.extract_function, MethodType)
    ins = SWFInterpreter()
    func = ins.extract_function
    assert isinstance(func, MethodType)

    class TestClass(object):
        def __init__(self):
            self.multinames = []
            self.constant_strings = []
            self.constant_namespaces = []
            self.constant_namespace_sets = []
            self.constant_multinames = []

    test_ins = TestClass()
    func(test_ins)
    assert isinstance(test_ins.extract_function, MethodType)

    del test_ins.multinames, test_ins.constant_strings

# Generated at 2022-06-14 18:25:00.974638
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    from types import FunctionType
    from .amf import AMFDecoder
    from .tags import parse_swf_tag
    from .swf_tag_data import SWFTagData_doabc as s

    def test_function():
        si = SWFInterpreter()
        si.tags = []

# Generated at 2022-06-14 18:25:12.133713
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    code = '\x60\x00\x01\x0a\x00\x06\x66\x75\x6e\x63\x00\x04\x61\x62\x63\x64\x04\x04\x01\x01\x03\x09\x04\x01\x02\x00\x05\x01\x09\x01\x00\x01\x0a\x00\x00\x00\x01\x0b\x01\x00\x0c\x00\x01\x00\x00\x00\x00\x00\x00\x00'

# Generated at 2022-06-14 18:25:22.225734
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    data = ''.join(['\x04\x00',  # number of bits to encode each byte of
                    '\x00',  # unknown
                    '\x54\x02\x00',  # swf version
                    '\x00\x00',  # file length in bytes
                    '\x00\x00',  # size of the frame
                    '\x95\x00',  # frame rate
                    '\x00\x00',  # number of frames
                    '\x42\x00\x0b',  # SWF file signature
                    ]).encode('ascii')
    # Construct an instance of class SWFInterpreter
    obj = SWFInterpreter(BytesIO(data))
    # Test the __str__ magic method

# Generated at 2022-06-14 18:25:33.651765
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    # test case : all possible values
    assert SWFInterpreter._parse_tag_body(
        '{{{[aa]},1,2,3,4,5},6,7,8,9,10}'.replace(' ', '')) == (
        {'aa': []}, (1, 2, 3, 4, 5), (6, 7, 8, 9, 10))
    # test case : empty string
    assert SWFInterpreter._parse_tag_body('') == (None, None, None)
    # test case : integer
    assert SWFInterpreter._parse_tag_body('1') == (None, (1,), None)
    # test case : tuple
    assert SWFInterpreter._parse_tag_body('(1,2)') == (None, (1, 2), None)
    #

# Generated at 2022-06-14 18:25:43.293461
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    swf = _SWFInterpreter()
    swf.constant_strings = [
        '__swf_add', '__swf_sub', '__swf_mult', '__swf_div',
        '__swf_to_string', '__swf_value_of', '__swf_char_code_at',
        '__swf_init_prop_a', '__swf_init_prop_b', '__swf_init_prop_c',
        '__swf_init_prop_d', '__swf_init_prop_e', '__swf_split',
        '__swf_join', '__swf_slice', '__swf_reverse', '__swf_length',
        '__swf_String', '__swf_undefined',
    ]

# Generated at 2022-06-14 18:25:54.461024
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    from .swftags import TagDefineSprite, TagDoABC, TagPlaceObject2, TagEnd
    from .abc import ABCFile

    assert _builtin_classes['Array'] == list

    def iter_tag_objects(tag_bytes):
        stream = io.BytesIO(tag_bytes)
        tag_parser = SWFTagParser(stream)
        for tag_id, tag_data in tag_parser:
            tag_cls = SWF_TAGS.get(tag_id)
            if tag_cls is None:
                yield tag_id, tag_data
            else:
                tag_object = tag_cls(tag_data, tag_parser)
                yield tag_object, tag_data


# Generated at 2022-06-14 18:26:02.258229
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2022-06-14 18:26:06.120013
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    swf = open(os.path.join(os.path.dirname(__file__), 'test.swf'), 'rb').read()
    swf = BytesIO(swf)

    swf = SWF(swf)
    interpreter = SWFInterpreter(swf)



# Generated at 2022-06-14 18:27:06.133219
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    """
    This function test SWFInterpreter.extract_class against the parsing
    of SWF files.
    """

    from .data import string_swf_files, int_swf_files, list_swf_files
    import io
    import zlib
    from os.path import join
    from .data import swf_files_dir

    def get_swf_content(fname):
        with io.open(join(swf_files_dir, fname), 'rb') as f:
            data = f.read()
            if data.startswith(b'CWS'):
                data = zlib.decompress(data[8:])
            # Ignore header size
            reader = SWFReader(io.BytesIO(data[8:]))
            assert reader.read_u8() == 9


# Generated at 2022-06-14 18:27:15.365793
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    s = compat_urllib_request.urlopen(
        'http://yts.re/torrent/download/3A507DFC4BD4F4A9E8F13CFD4A4E547AFC79F5BB'
        ).read()
    swf = _parse_swf(s)
    interp = SWFInterpreter(swf)

    def print_function(args):
        print(args)

    interp.patch_function('ytsre', 'print', print_function)
    interp.run()

# Generated at 2022-06-14 18:27:24.718774
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    from .swfdecompiler import SWFDecompiler
    from .abcfile import ABCFile
    from .tags import DoABCTag


# Generated at 2022-06-14 18:27:33.002202
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    from .swf_extract import SWFInterpreter
    from .compat import BytesIO

    for swf_id, swf in sorted(SWF_FILES.items()):
        if not swf_id.startswith('_'):
            continue
        fobj = BytesIO(swf)
        try:
            swf_interpreter = SWFInterpreter(fobj)
        except NotImplementedError:
            break
        for avm_class in swf_interpreter.avm_classes:
            for func_name in avm_class.method_names:
                func = swf_interpreter.extract_function(avm_class, func_name)
                args = avm_class.method_args[func_name]

# Generated at 2022-06-14 18:27:42.445137
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    m = SWFInterpreter()


# Generated at 2022-06-14 18:27:54.165932
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    _test_SWFInterpreter_patch_function_fixture(
        {
        },
        "",
        'import flash.external.ExternalInterface;  if (callFunction == "FSCommand:quit", "quit", "" )')


# Generated at 2022-06-14 18:28:07.493787
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2022-06-14 18:28:18.230578
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    swf = open(os.path.join(RESOURCES_PATH, 'metadata1.swf'), 'rb').read()
    assert len(swf) == 49487, 'len(swf): %d' % len(swf)

    interpreter = SWFInterpreter(swf)
    assert len(interpreter.constant_strings) == 13, \
        'len(interpreter.constant_strings): %d' % len(interpreter.constant_strings)

    assert len(interpreter.multinames) == 52, \
        'len(interpreter.multinames): %d' % len(interpreter.multinames)

# Generated at 2022-06-14 18:28:30.857246
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2022-06-14 18:28:32.754448
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    swfi = SWFInterpreter
    # TODO add unit test method

# Class SWFReader

# Generated at 2022-06-14 18:30:14.049820
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    interpreter = SWFInterpreter()

# Utility function to run SWFInterpreter.extract_function
# and return the result

# Generated at 2022-06-14 18:30:22.287324
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    # Testcase generated by the following commands:
    # swfc -o tmp.swf rect.as
    # tdump --disassemble tmp.swf > tmp.txt
    # python -c 'from avm2 import *; s = SWFInterpreter(open(
    #             "tmp.txt", "rb"))' > tmp.py
    s = SWFInterpreter(open(
        os.path.join(os.path.dirname(__file__), 'swfdecompiler.txt'), 'rb'))

    assert s.script_name == 'Script'
    assert len(s.constant_strings) == 14

    assert s.constant_strings[0] == 'flash.display::Sprite'

# Generated at 2022-06-14 18:30:34.311800
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    from io import BytesIO

    # Example from #3869

# Generated at 2022-06-14 18:30:42.557965
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    avm_class = _AVMClass(
        variables={'q': 1},
        static_properties={'x': None},
        method_names={'nofun'},
    )

    interp = SWFInterpreter()

    def _read_byte(coder):
        return coder.read_u8()

    interp.patch_function(avm_class, _read_byte, 'fun')

    # Dummy function that does not actually parse bytecode
    bytecode_parser = lambda bytecode, coder: bytecode

    def _parse_bytecode(bytecode):
        class FakeCoder(object):
            def __init__(self, bytecode):
                self._bytecode = bytecode
                self._offset = 0

            def tell(self):
                return self._offset


# Generated at 2022-06-14 18:30:51.474587
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    input = open('tests/adobe_flashplayer_11.1.102.63_linux_sa.jar', 'rb')
    swf = input.read()
    input.close()
    interpreter = SWFInterpreter(swf)

    def assert_multinames(ms):
        # We define our own assert because we don't want assertion failure to
        # break other test cases
        for mn in ms:
            assert isinstance(mn, _Multiname), ('%r is not _Multiname' % mn)

    assert_multinames(interpreter.multinames)
    assert_multinames(interpreter.multinames_string)
    assert_multinames(interpreter.multinames_int)
    assert_multinames(interpreter.multinames_uint)

# Generated at 2022-06-14 18:31:00.736517
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    filename = os.path.join(os.path.dirname(__file__),
                            '..', 'tests', 'swfs', 'playerProductInstall.swf')
    with open(filename, 'rb') as f:
        swf_data = compat_str(f.read())
    swf = SWFInterpreter(swf_data)

    assert isinstance(swf.avm2_types, dict)
    for i, avm_class in enumerate(swf.avm2_types.values()):
        assert isinstance(avm_class, _AVMClass)
        assert avm_class.name in avm_class.static_properties
        if avm_class.private_namespace is not None:
            assert avm_class.private_namespace in avm_class.static_properties


# Generated at 2022-06-14 18:31:02.495537
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    INTERPRETER.extract_class(AVM_CLASSES[INTERPRETER.main_class])

# Generated at 2022-06-14 18:31:05.692577
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    swf_interpreter_class = _SWFInterpreter()
    assert swf_interpreter_class.constant_strings == []



# Generated at 2022-06-14 18:31:13.972566
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    import umsgpack
    import struct

    class _AVMClass(object):
        method_pyfunctions = {}
    avm_class = _AVMClass()

    interpreter = SWFInterpreter()
    avm_class.method_names = set(interpreter.method_names)

# Generated at 2022-06-14 18:31:23.293547
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    swf_data = compat_urllib_request.urlopen(
        'https://github.com/rg3/youtube-dl/raw/master/test/swf/'
        'int_class.swf').read()
    swf = SWFInterpreter(swf_data)
    assert sorted(swf.avm_classes.keys()) == [
        'Complex', 'Complex$1', 'Complex$2', 'Complex$3', 'Complex$4']

    cls = swf.avm_classes['Complex']