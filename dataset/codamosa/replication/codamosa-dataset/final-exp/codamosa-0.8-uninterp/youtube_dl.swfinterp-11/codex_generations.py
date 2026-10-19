

# Generated at 2022-06-14 18:25:31.191876
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    assert isinstance(SWFInterpreter(1, 2), SWFInterpreter)

if __name__ == '__main__':
    from sys import argv
    test_SWFInterpreter()

    for filename in argv[1:]:
        print('Processing %r' % filename)
        # Test reading simple Actionscript 3
        with open(filename, 'rb') as fp:
            swf = SWFParser(fp)
            print('SWF version:', swf.signature)
            tag = swf.read_tag()
            while tag is not None:
                if tag.code == 82:
                    print('Processing ActionScript3: %r' % tag)
                    # Process ActionScript3
                    interpreter = SWFInterpreter()

# Generated at 2022-06-14 18:25:41.703634
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    from .swftags import DoABC
    from .avm2 import ABCFile
    from .parser import SWFParser
    from .parser import SWFStream
    from cStringIO import StringIO
    from nose.tools import ok_
    from sys import stderr

# Generated at 2022-06-14 18:25:54.458371
# Unit test for constructor of class SWFInterpreter

# Generated at 2022-06-14 18:25:55.659859
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    assert True

# Generated at 2022-06-14 18:26:03.062051
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    class SWFInterpreterSub(SWFInterpreter):
        def __init__(self):
            self.constant_strings = []

    inter = SWFInterpreterSub()

# Generated at 2022-06-14 18:26:09.688622
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    class Test(SWFInterpreter):
        def __init__(self, method_info, body_info, method_names):
            self.method_info = method_info
            self.body_info = body_info
            self.method_names = method_names

        def build_method(self, method_name, avm_class):
            return self.extract_function(avm_class, method_name)

    class AVMClass:
        def __init__(self, variables, method_names):
            self.variables = variables
            self.method_names = method_names
            self.static_properties = {}

    # Test 1
    x = {
        'abc': undefined,
        'xyz': 5,
        'v': [],
    }

# Generated at 2022-06-14 18:26:19.046943
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2022-06-14 18:26:21.976110
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    assert SWFInterpreter([], [], [], [], [], [], [], [])._init_ok
    assert not SWFInterpreter([], [], [], [], [], [], [], []).has_loaded_classes


# Generated at 2022-06-14 18:26:33.845727
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    class AVMClass:
        def __init__(self, base_class, static_properties, method_names):
            self.base_class = base_class
            self.static_properties = static_properties
            self.method_names = method_names
            self.method_pyfunctions = {}
        def make_object(self):
            return 'a_new'

    interpreter = SWFInterpreter(
        AVMClass, [],
        {'multinames': [], 'constant_strings': []})
    assert isinstance(interpreter.swf_class, AVMClass)
    assert isinstance(interpreter.avm_class, AVMClass)

# Generated at 2022-06-14 18:26:45.514133
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
  from .AVMClass import AVMClass
  from .ABCFile import ABCFile
  from .Multiname import Multiname
  from .MethodBody import MethodBody
  from .ABCConstantPool import ABCConstantPool
  from .ABCMethod import ABCMethod

  abc_constant_pool = ABCConstantPool()
  abc_constant_pool.add_int(10)
  abc_constant_pool.add_multiname(Multiname(name=b'length'))
  abc_constant_pool.add_multiname(Multiname(name=b'Array'))
  abc_constant_pool.add_multiname(Multiname(name=b'join'))

  abc_method_body = MethodBody(initializer=True)

# Generated at 2022-06-14 18:28:21.491142
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    filename = 'tests/swfs/SWFTEST_AVM2.swf'
    fp = open(filename, 'rb')
    swf = compat_ET.parse(fp)
    fp.close()

    avm = SWFInterpreter(swf)
    avm.extract_class('AVM2')

    assert avm.classes['AVM2'].variables['PI'] == 3.141592653589793

    # print(avm.classes['AVM2'].variables['PI'])

# Generated at 2022-06-14 18:28:30.493314
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    import binascii

# Generated at 2022-06-14 18:28:36.933328
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    from os.path import join, dirname
    interp = SWFInterpreter(join(dirname(__file__), 'test.swf'))
    interp.extract_class('_level0', 'MovieClip')
    
    assert isinstance(_level0.method_pyfunctions, dict)
    assert isinstance(_level0.variables, dict)
    assert isinstance(_level0.static_properties, dict)
    assert isinstance(_level0.method_names, list)
    assert isinstance(_level0.make_object(), _ScopeDict)

# Generated at 2022-06-14 18:28:47.937908
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    swf = SWFInterpreter()
    swf.extract_function(swf.avm_class, 'escapeString')
    swf.extract_function(swf.avm_class, 'construct_UrlLoader')
    swf.extract_function(swf.avm_class, 'construct_NetStream')
    swf.extract_function(swf.avm_class, 'construct_Sound')
    swf.extract_function(swf.avm_class, 'construct_LoaderInfo')
    swf.extract_function(swf.avm_class, 'construct_Stage')
    function = swf.extract_function(swf.avm_class, 'construct_Capabilities')
    res = function([])
    assert isinstance(res, _AVMClass_Object)


# Generated at 2022-06-14 18:28:52.191071
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    interp = SWFInterpreter()
    avm_class = interp.extract_class(
        AVMMethodBody(
            method_name=None,
            max_stack=4,
            local_count=4,
            init_scope_depth=1,
            max_scope_depth=1,
            code=b'\x13\x00\x02\x00\x00\x00\x00',
            exception_info=[
                AVMExceptionInfo(
                    from_pos=0,
                    to_pos=0,
                    target=0,
                    exc_type=0,
                    var_name=0),
            ],
            traits=[]))
    assert avm_class.variables['__AS3__.vec']['length'] == 0

# Generated at 2022-06-14 18:29:02.114232
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    from .tag_data import tag_data
    from .tag_def import TAG_DEFINITION_CLASSES
    from .swf import read_swf, SWF
    from .movie import Movie

    s = read_swf(io.BytesIO(tag_data))
    assert isinstance(s, SWF)
    s.validate()

    m = Movie.read_tags(s.tags)
    assert isinstance(m, Movie)
    # m.validate()  # TODO should not be necessary

    interp = SWFInterpreter(s.tags, m)
    assert isinstance(interp, SWFInterpreter)

    interp.extract_function(interp.avm_classes['init__'], 'init')


# ---- ABC code ----


# In the ABC file format, multinames

# Generated at 2022-06-14 18:29:10.988879
# Unit test for method register_methods of class _AVMClass
def test__AVMClass_register_methods():
    from .simple_vm import (
        simple_vm_exec,
        simple_vm_push_const,
        simple_vm_push_context,
    )

    c = _AVMClass('SomeClass', 0)
    assert c.name == 'SomeClass'
    assert c.name_idx == 0
    assert not c.static_properties
    assert not c.method_names
    assert not c.methods

    c.register_methods({
        'method_1': 1,
        'method_2': 2,
        'method_3': 3,
    })
    assert c.method_names == {
        'method_1': 1,
        'method_2': 2,
        'method_3': 3,
    }

# Generated at 2022-06-14 18:29:21.586241
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2022-06-14 18:29:26.562646
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    with open(
            os.path.join(os.path.dirname(__file__),
                         'test_swfinterp_extract_class.swf'), 'rb') as f:
        data = f.read()
    interp = SWFInterpreter()
    interp.extract_class(data, 'test')


# Generated at 2022-06-14 18:29:27.271008
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    pass

# Generated at 2022-06-14 18:30:35.667780
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    with open(
            os.path.join(os.path.dirname(__file__),
                         'flash_strings_test.swf'), 'rb') as f:
        data = f.read()
        interpreter = SWFInterpreter(data)
        # Test access to a class variable
        assert interpreter.extract_variable(
            interpreter.avm_classes[0], 'flash_strings_test_AVM_txt') == 'Hello, world!'

if __name__ == '__main__':
    test_SWFInterpreter()

# Generated at 2022-06-14 18:30:38.541210
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    assert SWFInterpreter("http://example.com")


# Generated at 2022-06-14 18:30:48.811588
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    from flash_extractors.swf_extractor import SWFInterpreter
    from flash_extractors.swf_extractor import SWFExtractor
    se = SWFExtractor({
        '-a': None,
        '--get-url': None,
    })
    si = SWFInterpreter([], se)

# Generated at 2022-06-14 18:30:58.879733
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2022-06-14 18:31:07.462700
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    from os.path import join, dirname
    fname = join(dirname(__file__), 'mandelbrot.swf')
    with open(fname, 'rb') as f:
        interp = SWFInterpreter(f.read())
    classes = interp.extract_classes()
    assert len(classes) == 1
    assert classes.keys() == {
        'flash.display.Sprite',
    }
    assert isinstance(classes[classes.keys()[0]], _AVMClass)



# Generated at 2022-06-14 18:31:20.570802
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    from io import BytesIO
    from .swftags import _SWF_METHOD_CODE_CONSTANTS
    from .swftags import _SWFTAG_CLASSES_MAP


# Generated at 2022-06-14 18:31:33.134373
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    swf_interpreter = SWFInterpreter()
    swf_interpreter.avm_classes = {}
    swf_interpreter.constant_strings = ['String', 'length', 'charCodeAt']
    swf_interpreter.multinames = [
        _Multiname('String', ['packet']),
        'packet',
        'length',
        'charCodeAt'
    ]

# Generated at 2022-06-14 18:31:41.163803
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    interp = SWFInterpreter()
    abc_data = compat_bytes(open(TEST_FILE_NAME, 'rb').read())
    interp.load(abc_data)
    abc_data = abc_data[8:]

    extract_func = interp.extract_function
    func = extract_func(interp.classes['navigationCode'], 'toString')
    assert func([], []) == '[object navigationCode]'

    func = extract_func(interp.classes['flashproxy'], 'getProperty')
    assert func([0], []) == 'http://www.youtube.com/apiplayer?video_id=ywmpjyAOiKo&version=3'

    func = extract_func(interp.classes['flashproxy'], 'setProperty')

# Generated at 2022-06-14 18:31:51.520426
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    from .swf import make_swf_constructor, SWFReader
    from .avm2 import AVM2Interpreter
    from .swfmetadata import SWFMetadata
    swf_data = open(get_test_data_file_path(
        'test_SWFInterpreter_extract_function_01.swf'),
        'rb').read()
    swf_tags = SWFReader(swf_data).read_tags()
    SWFMetadata(swf_data, swf_tags).extract_metadata()
    avm2_interpreter = AVM2Interpreter(SWFInterpreter(swf_tags), swf_tags)
    test_function = avm2_interpreter.extract_function(
        'TestClass', 'testFunction')
    assert test_

# Generated at 2022-06-14 18:32:02.223074
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    def _test(file_content):
        # file_content is the content of a .swf file
        if file_content:
            with open('/tmp/test.swf', 'wb') as outf:
                outf.write(file_content)
            swf = SWF('/tmp/test.swf')
            si = SWFInterpreter(swf)
            for avm_class in swf.class2avm:
                for func_name in sorted(avm_class.method_pyfunctions):
                    func = si.patch_function(
                        avm_class, func_name, avm_class.method_pyfunctions[func_name]())
                    func()