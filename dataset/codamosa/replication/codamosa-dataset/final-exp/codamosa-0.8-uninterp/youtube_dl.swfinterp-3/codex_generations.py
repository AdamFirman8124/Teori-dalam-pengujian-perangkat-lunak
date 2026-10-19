

# Generated at 2022-06-14 18:25:13.367738
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    subtitles = [
        {'script': 'function f(x) {\n'
                   '  return x;\n'
                   '}\n'
                   'var y = f(5);\n',
         'script_type': 'AS1',
         'start': 2.0,
         'style': 'Style1',
         'text': 'TEST1'},
        {'script': 'function g(x) {\n'
                   '  return x+1;\n'
                   '}\n'
                   'var z = g(11);\n',
         'script_type': 'AS1',
         'start': 3.0,
         'style': 'Style1',
         'text': 'TEST2'}]
    swf = SWFInterpreter(None, subtitles)
    avm_classes = swf

# Generated at 2022-06-14 18:25:16.841794
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    interp = SWFInterpreter(SWF(open('../test.swf', 'rb')))
    # TODO check the returned values
    interp.extract_class('__Packages.test')
    interp.extract_class('__Packages.test.test2')

# Generated at 2022-06-14 18:25:23.717484
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    fileobj = io.BytesIO(b'')
    swf = swftags.SWF(fileobj)
    swf.version = 8

    swf.tags.append(swftags.DoABC(
        flags=0, name='', data=b''))
    swf.tags.append(swftags.FileAttributes(
        has_metadata=False, use_network=False))

    interpreter = SWFInterpreter(swf)
    avm_classes = interpreter.extract_classes()
    assert len(avm_classes) == 1

    interpreter.avm_classes = avm_classes
    interpreter.extract_all_functions()

# Generated at 2022-06-14 18:25:35.128249
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2022-06-14 18:25:44.890179
# Unit test for constructor of class SWFInterpreter

# Generated at 2022-06-14 18:25:47.538382
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    interp = SWFInterpreter("file.swf")
    classobj = interp.build_single_class("test")
    assert interp.extract_function(classobj, "test")(None) == 1

# Generated at 2022-06-14 18:25:56.833794
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    i = SWFInterpreter()

# Generated at 2022-06-14 18:25:58.132510
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    # With a dummy argument this function can't be triggered
    pass


# Generated at 2022-06-14 18:26:10.910652
# Unit test for constructor of class SWFInterpreter

# Generated at 2022-06-14 18:26:17.057208
# Unit test for method register_methods of class _AVMClass
def test__AVMClass_register_methods():
    obj = _AVMClass(1, 'test1')
    obj.register_methods({'method1': 2})
    assert obj.method_names == {'method1': 2}
    assert obj.method_idxs == {2: 'method1'}
    obj.register_methods({'method2': 3})
    assert obj.method_names == {'method1': 2, 'method2': 3}
    assert obj.method_idxs == {2: 'method1', 3: 'method2'}



# Generated at 2022-06-14 18:27:40.467107
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    class AVMClass(object):
        def __init__(self):
            self.method_pyfunctions = {}

    my_class = AVMClass()
    si = SWFInterpreter(avm_class=my_class)


# Generated at 2022-06-14 18:27:48.415122
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    si = SWFInterpreter(io.BytesIO(test_vars['c-simple']))
    res = si.extract_class('C')
    assert res.static_properties['b'] == 1
    assert callable(res.static_properties['f'])
    assert res.static_properties['f']([1]) == 2
    assert res.static_properties['f']([2]) == 3
    assert res.static_properties['f']([3]) == 4

# Generated at 2022-06-14 18:27:56.851275
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    from .swfdecompiler import SWFDecompiler
    s = SWFDecompiler(open(os.path.join(
        test_dir, '....swf')))
    interpreter = SWFInterpreter(s)

    avm_class = _AVMClass(interpreter)
    avm_class.variables['Math'] = MathClass
    avm_class.variables['String'] = StringClass

    interpreter.patch_function(
        avm_class, '....', '....',
        program_counter=-1, registers=[],
        stack=[], scopes=[])

    assert False

# Generated at 2022-06-14 18:28:07.967457
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    from .amf0 import _Undefined

    class SWFInterpreter:
        def __init__(self):
            self.constant_strings = ['abc', 'def']
            self.constant_ints = [1, 2, 3]
            self.constant_uints = [4, 5, 6]
            self.constant_doubles = [1., 2., 3.]
            self.multinames = ['$a', '$b', 1, '$c', '$d', '$e']

# Generated at 2022-06-14 18:28:18.576324
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    from tests import DataTestCase
    from . import patch_function


# Generated at 2022-06-14 18:28:31.022217
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2022-06-14 18:28:38.012662
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    from . import __file__ as avconv_path
    from .version import __version__

    class_builder = _AVMClass_Builder()

    avm_class = class_builder.make_class('Test')
    avm_class.variables['env'] = {}

    interpreter = SWFInterpreter(
        avm_class,
        '',
        {
            'avconv': avconv_path,
            'version': __version__,
            'arguments': '-i {infile} -acodec copy -f flv -'.split(),
        })

    assert interpreter.extract_function(avm_class, 'Test') is not None



# Generated at 2022-06-14 18:28:49.185650
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    def t(name):
        return {
            'length': 8,
            'slice': (2, 3),
        }[name]

    interpreter = SWFInterpreter()
    avm_class = _AVMClass()

    func_name = 'func_name'

# Generated at 2022-06-14 18:29:00.162208
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    """
    This unit test extracts the class Object from the SWF file `test/test.swf`
    and executes it
    """
    interpreter = SWFInterpreter('test/test.swf')
    interpreter.extract_class('Object')
    for method in ['toString', 'valueOf']:
        interpreter.extract_function_from_class('Object', method)
    for method in ['trace']:
        interpreter.extract_function_from_class('AS2_Builtin', method)

    obj = _AVMClasses['Object'].make_object()
    obj['mytuple'] = 'mytuple'
    obj['myint'] = 3
    assert obj['mytuple'] == 'mytuple'
    assert obj['myint'] == 3


# Generated at 2022-06-14 18:29:10.646768
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    si = SWFInterpreter()
    avm_class = si.avm_classes['com.longtailvideo.jwplayer.player::Player']
    avm_class.static_properties['utils'] = utils_mock

    func_name = 'resolve'
    args = ['this']
    func = avm_class.method_pyfunctions[func_name]
    def func_wrapper(self, args):
        res = func(self.variables, args)
        return res

    resfunc = si.patch_function(avm_class, func_name, args, func_wrapper)
    res = resfunc({'this': 'somethis'}, ['somearg'])

# Generated at 2022-06-14 18:30:53.298164
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    import io
    from .util import lzma_decompress, concat_bytes


    def make_swf_data(op0, *ops):
        from .abc_parser import ABCParser
        abc_parser = ABCParser(kind=ABCParser.Kind.both)
        abc_parser.add_bytes(op0)
        for op in ops:
            abc_parser.add_bytes(op)
        abc_bytes = abc_parser.serialize()


# Generated at 2022-06-14 18:31:04.705143
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    import io
    import struct

    from io import BytesIO
    from pprint import pformat  # noqa
    from typing import Any, Dict, List, Optional

    def write_u8(self, val):
        self.write(struct.pack('B', val))

    def write_u30(self, val):
        val = int(val)
        assert val >= 0
        s = b''
        while True:
            if val < 128:
                s += compat_chr(val)
                break
            else:
                s += compat_chr(128 | (val & 0x7f))
                val >>= 7
        self.write(s)

    f = BytesIO()
    f.write_u8 = write_u8.__get__(f)
    f.write_u30 = write

# Generated at 2022-06-14 18:31:16.335478
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    test_file = '''
    var a = "a";
    var b = "b";
    var c = "c";
    var d = "d";
    function f(arg1, arg2) {
      var e = "e";
      var f = "f";
      return arg1 + arg2 + a + b + c + d + e + f;
    }
    return f("1", "2");
    '''

    interpreter = SWFInterpreter()
    avm_class = interpreter.make_avm_class(test_file)

    f = avm_class.method_pyfunctions['f']
    res = f(['1', '2'])

    assert res == '12abcdef', res


# Generated at 2022-06-14 18:31:23.123536
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    swf = SWFInterpreter('tests/swf/test.swf')
    assert swf.header.has_audio == 0
    assert swf.header.frame_rate == 24
    assert swf.header.frame_count == 1
    assert swf.header.width == 320
    assert swf.header.height == 240
    assert swf.header.version == 9
    assert swf.header.file_length == 2551


if __name__ == '__main__':
    test_SWFInterpreter()

# Generated at 2022-06-14 18:31:34.761192
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    def test():
        import os
        from .downloader import MockYDL
        f = SWFFile(
            ydl=MockYDL({
                'url': 'http://afp.com',
                'info_dict': {
                    'url': 'http://afp.com',
                },
            }),
            f='tests/resources/swfextract.swf',
            video_url='http://afp.com'
        )
        assert f.original_url == 'http://afp.com'
        assert f.file_size == os.path.getsize('tests/resources/swfextract.swf')
        assert f.duration == 1.0

        f.extract_classes()

# Generated at 2022-06-14 18:31:42.641677
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    from . import testdata
    from . import amfdata

    interp = SWFInterpreter(encoding='utf8')
    amf = amfdata.AMF3DataFile(testdata.get_path('_test4.swf'))
    amf.load()
    assert len(amf.actionscript_list) == 2
    assert isinstance(amf.actionscript_list[0], list)
    assert isinstance(amf.actionscript_list[0][0], amfdata.AMF3Class)
    assert amf.actionscript_list[0][0].name == 'Object3'
    assert amf.actionscript_list[1][0].name == 'Object2'
    assert amf.actionscript_list[1][1].name == 'Object1'

# Generated at 2022-06-14 18:31:52.946849
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    from .read_swf import read_swf
    from .utils import SWFError

    def _assert_raises_swferror(func, *args, **kwargs):
        try:
            func(*args, **kwargs)
        except SWFError:
            pass
        else:
            raise AssertionError('Excepted to raise SWFError')

    swf = read_swf('tests/swfs/avm2_flash_player10_rc2.swf')
    swf.validate()
    assert swf.tagtype == 43
    assert swf.abcdata

    sh = swf.abcdata
    interpreter = SWFInterpreter(sh)
    assert interpreter.swf.tagtype == 43
    assert interpreter.swf.abcdata


# Generated at 2022-06-14 18:32:03.477275
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    class M(object):

        @staticmethod
        def func(arg):
            return arg

    m = M()
    m.func = M.func

    # }}}

    si = SWFInterpreter()

    si.classes['test'] = m

    si.extract_function(m, 'func')
    m.func(42)

    # }}}

    class M(object):

        @staticmethod
        def func(arg=None):
            return arg

    m = M()
    m.func = M.func

    # }}}

    si = SWFInterpreter()

    si.classes['test'] = m

    si.extract_function(m, 'func')

    assert m.func() == None

    # }}}


# Generated at 2022-06-14 18:32:05.294292
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    # SWFInterpreter.patch_function(self, avm_class, func_name)
    assert True # TODO: implement your test here


# Generated at 2022-06-14 18:32:17.081425
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    si = SWFInterpreter()

    avm_class = _AVMClass()

    def declare_method(name, arg_count, addr, code):
        method = _AVMMethod()
        method.name = name
        method.arg_count = arg_count
        method.addr = addr
        method.code = code
        avm_class.methods.append(method)
        avm_class.method_names.append(name)

    def extract_function(name):
        si.extract_function(avm_class, name)

    def build_function_code(minfo, code_bytes, args, **kwargs):
        code = SWFCode(minfo, code_bytes, args, **kwargs)
        return code.to_bytes()

    # Declare a function with one argument
    # function