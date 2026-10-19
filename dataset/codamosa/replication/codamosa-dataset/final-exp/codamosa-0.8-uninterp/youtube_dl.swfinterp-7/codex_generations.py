

# Generated at 2022-06-14 18:25:19.350672
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    # No need to test, this method is already tested indirectly by
    # test_SWF and test_SWFInterpreter
    pass


# Functions extracted from extracted/ndf/embed.as of
# https://github.com/rg3/youtube-dl/issues/1371, see
# https://github.com/rg3/youtube-dl/issues/1371#issuecomment-46866473 for
# the command-line to extract all the code.
# Basically, embed.as must be the same as Main.as, but without the last
# line (the return statement)

# Generated at 2022-06-14 18:25:25.846794
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    interpreter = SWFInterpreter()

# Generated at 2022-06-14 18:25:35.832808
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    swf_interp = SWFInterpreter(b'')
    assert(swf_interp.extract_class(0) == StringClass)
    assert(
        swf_interp.extract_class(
            0x0A,
            [
                _AVMClass(
                    0x0A,
                    {'SomeClass': None}),
                _AVMClass(
                    0x0B,
                    {'SomeClass': None,
                     'ParentClass': 0x0A}),
            ],
            []) == _AVMClass(
            0x0B,
            {'SomeClass': None,
             'ParentClass': 0x0A}))


# Generated at 2022-06-14 18:25:44.256984
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    import io
    import zipfile
    from collections import defaultdict

    from .swftags import DoABC
    from .swftags import Tag

    with io.open('test/test-swf.zip', 'rb') as f:
        test_zip = zipfile.ZipFile(f)
        swf_data = test_zip.read('test.swf')
        swf_file = io.BytesIO(swf_data)
        swf = SWF(swf_file)

        swf_interpreter = SWFInterpreter(swf)
        for tag in swf.tags:
            if not isinstance(tag, DoABC):
                continue
            abc = tag.abc
            for c_idx, aclass in enumerate(abc.classes):
                assert aclass.name not in swf_

# Generated at 2022-06-14 18:25:54.687370
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    # Test data
    code_string = compat_struct_pack('<H', 1) + \
        b'\x1f\x06\x00\x10\x00\x00\x00\x61\x00\x00' + \
        compat_struct_pack('<H', 1) + \
        b'\x0b\x06\x00\x0c\x00\x00\x00\x63\x00\x00' + \
        compat_struct_pack('<H', 1) + \
        b'\x0b\x06\x00\x06\x00\x00\x00\x65\x00\x00' + \
        b'\x1c\x00\x00\x00\x00'

    # Setup
    interpreter = SWF

# Generated at 2022-06-14 18:25:57.379033
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    swf = SWFInterpreter(open('../testcases/Asset.swf', 'rb'))
    swf.extract_class('com.adobe.serialization.json.JSON')
    print('ok')

# Generated at 2022-06-14 18:26:10.046708
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    """
    Test functionality of :py:method:`SWFInterpreter.extract_function`.
    """
    import io
    import sys

    from .swfobj import SWF, TAG_SHOWFRAME, TAG_END
    from .swfobj import TAG_DOACTION, TAG_DOABC

    from .swftags import ActionPush

    interpreter_cls = SWFInterpreter

    # Define a test class
    swf = SWF()
    swf.header.frame_size.x_min = swf.header.frame_size.y_min = 0
    swf.header.frame_size.x_max = swf.header.frame_size.y_max = 5000

    if sys.version_info < (3, 0):
        coder = io.BytesIO()

# Generated at 2022-06-14 18:26:15.073793
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    assert SWFInterpreter.version_id == 46, \
        'Your version of SWFInterpreter should be 46'
    assert (SWFInterpreter.build_date
            == '2013-08-23 08:30:07 -0400 (Fri, 23 Aug 2013)'), \
        'Your build date of SWFInterpreter is incorrect'


if __name__ == '__main__':
    sys.exit(unittest.main())

# Generated at 2022-06-14 18:26:19.451917
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    with open(os.path.join(
        os.path.dirname(__file__),
        'fixtures', 'sample.swf'
    ), 'rb') as f:
        swf = SWFInterpreter(f)
    assert isinstance(swf, SWFInterpreter)


# Generated at 2022-06-14 18:26:26.367526
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    # create a sample AVMFile to make tests on
    avm_file = AVMFile()
    # print(avm_file)

    # init swfInterpreter
    swf_interpreter = SWFInterpreter(avm_file)

    # extract a random class
    avm_class = swf_interpreter.extract_class('ae500d')
    # print(avm_class)

    # extract the same class again
    avm_class = swf_interpreter.extract_class('ae500d')
    # print(avm_class)

    # extract a non-existing class
    avm_class = swf_interpreter.extract_class('ae5d')
    assert avm_class is None



# Generated at 2022-06-14 18:27:25.376243
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    def _load_swf(path):
        with open(join(__SWFS_PATH__, path), 'rb') as f:
            swf = f.read()
        return swf

    with open(join(__SWFS_PATH__, 'swfdec_devil.swf'), 'rb') as f:
        swfdec_devil_swf = f.read()
    tags = _swf_tags(io.BytesIO(swfdec_devil_swf))

    swf = _load_swf('abcs/abc_empty.swf')
    inter = SWFInterpreter(swf)

    swf = _load_swf('abcs/abc_add.swf')
    inter = SWFInterpreter(swf)


# Generated at 2022-06-14 18:27:33.390790
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    import sys
    assert sys.version_info[:2] >= (2, 7)
    swf = SWFInterpreter('test/swfdecomp_test_verify.swf')

    # Ensure that certain classes are defined
    assert 'TestClass' in swf.classes
    assert 'TestSubClass' in swf.classes
    assert swf.classes['TestClass'] is not swf.classes['TestSubClass']
    assert 'Object' in swf.classes
    assert 'TestClass' not in swf.classes['Object']
    assert '__name' in swf.classes['Object']
    assert 'String' in swf.classes

    avm_class = swf.classes['TestClass']
    assert '__name' in avm_class.static_properties
    assert '__name' in avm_class

# Generated at 2022-06-14 18:27:42.715475
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    swf = io.BytesIO(base64.b64decode(TEST_SWF_EXTRACT_CLASS))
    avm = SWFInterpreter(swf)

    avm_class = avm.extract_class('MyClass')
    assert avm_class.static_properties == {
        'foo': 'bar',
        'my_property': 0,
        'variable': 'value',
        'baz': {
            'foo': 'bar',
        },
        'obj': {
            'x': 10,
        },
    }
    assert avm_class.method_pyfunctions['my_method']() == 'Hello'
    assert avm_class.method_pyfunctions['my_method'](
        'myString') == 'myString'
    assert avm_class.method_

# Generated at 2022-06-14 18:27:54.407126
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():

    def _get_fake_MethodBody(code):
        class FakeMethodBody(object):
            def __init__(self):
                self.code = [o for o in bytearray(code)]
        return FakeMethodBody

    def _get_fake_Method(return_type_name, param_type_names, body):
        class FakeMethod(object):
            def __init__(self):
                self.return_type_name = return_type_name
                self.param_type_names = param_type_names
            def get_body(self):
                return body
        return FakeMethod

    class FakeClass(object):
        def __init__(self):
            self.multinames = {}
            self.constant_strings = []
            self.methods = []


# Generated at 2022-06-14 18:28:07.495251
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    swf = SWFInterpreter()
    class_name = 'MyClass'

# Generated at 2022-06-14 18:28:18.263996
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    si = SWFInterpreter()

    # Test for simple function returning a constant
    @si.registered_function
    def test_SWFInterpreter_extract_function_decorated(self, *args):
        return 42
    avm_class = _AVMClass(name='test_SWFInterpreter_extract_function_decorated')
    func_name = 'test_SWFInterpreter_extract_function_decorated'
    resfunc = si.extract_function(avm_class, func_name)
    assert resfunc(arg=[]) == 42

    # Test for simple function with input argument
    @si.registered_function
    def test_SWFInterpreter_extract_function_decorated(self, *args):
        [input] = args
        return 42 + input

# Generated at 2022-06-14 18:28:30.900138
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    # read in the test file
    with open(test_filepath('test.swf'), 'rb') as f:
        swf = SWF(f)
    # check the magic number in the header
    assert swf.header.signature == b'FWS'
    # check the minor version
    assert swf.header.version == 12
    # check the file length
    assert swf.header.file_length == 20
    # check the frame size
    assert swf.header.frame_size == {
        'Nbits': 17,
        'Xmin': 0,
        'Xmax': 20,
        'Ymin': 0,
        'Ymax': 20
    }
    # check the frame rate
    assert swf.header.frame_rate == 12.0
    # check the number of frames
    assert swf

# Generated at 2022-06-14 18:28:38.809772
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    from flash_actionscript import common as flash_common
    action_script = """
        this.loaderInfo.uncaughtErrorEvents.addEventListener(
            'uncaughtError', uncaughtErrorHandler);
        function uncaughtErrorHandler(event:uncaughtErrorEvent):void {
            var errorMsg:String;
            if (event.error is Error) {
                errorMsg = 'Error: ' + event.error.message;
            }
            else if (event.error is ErrorEvent) {
                errorMsg = 'ErrorEvent: ' + event.error.text;
            }
            else {
                errorMsg = 'Unknown error: ' + event.toString();
            }
            trace(errorMsg);
        }
        stop();
    """
    avm1_byte_array = flash_common.flash_embed_script_with_actionscript

# Generated at 2022-06-14 18:28:49.564350
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    from SWF.avm import AVM
    swfinterpreter = AVM()
    swfinterpreter.constant_strings = ['String', 'join']
    Multiname = swfinterpreter.Multiname
    mname = Multiname('String', [Multiname('join', [])])
    swfinterpreter.multinames = [mname]
    swfinterpreter.method_signatures = [
        {
            'name': 'String',
            'return_type': 'String',
            'param_types': ['*'],
        },
    ]
    swfinterpreter.method_names = ['String']
    swfinterpreter.method_default = {
        0: (
            'String',
            ('returnString',),
        ),
    }
    swf

# Generated at 2022-06-14 18:28:54.738681
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    from swfextract.amf import SWFReader
    from io import BytesIO

    def test_method_patching(swf_file, function_name, new_function):
        with open(swf_file, 'rb') as f:
            swf = SWFReader(f, parse_tags=False)
            swf.swf_data.seek(0)
            interpreter = SWFInterpreter(swf.swf_data)
            interpreter.patch_function(function_name, new_function)

    def swf_invoke(coder, s, args=None, interpreter=None):
        from swfextract.amf import AMF0
        from swfextract import constants

        header = s.read(16)
        assert header == b'swfinvoke'


# Generated at 2022-06-14 18:30:39.893166
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    with open(
        os.path.join(os.path.dirname(__file__), 'test', 'test.swf'),
        'rb') as f:
        swf = SWF(f)
    interpreter = SWFInterpreter(swf)
    assert len(interpreter.constant_strings) == 8
    assert len(interpreter.avm2_classes) == 14
    # TODO test that all AVM2 classes have all functions, etc.


# Generated at 2022-06-14 18:30:49.608723
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    interpreter = _SWFInterpreter()
    avm_class = _AVMClass('MyClass', [])

# Generated at 2022-06-14 18:30:59.223060
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    from .avm2 import avm2
    from .abc import ABCFile

    sl = '''
        class A extends Object {
            public function A() {
                this['c'] = 2;
                this['a'] = 1;
            }
            public function sum() {
                return this['a'] + this['c'] + this['d'];
            }
        }
        class B extends A {
            public function B() {
                this['d'] = 3;
                super();
            }
        }
        function test() {
            return new B();
        }
    '''

    # Get a SWFInterpreter for test
    abc_file = ABCFile.load_script(sl)
    avm2_interpreter = avm2.AVM2(abc_file)
    swf_interpre

# Generated at 2022-06-14 18:31:07.254790
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    import io
    with io.open('tests/swf/test.abc', 'rb') as f:
        s = f.read()
    intpr = SWFInterpreter()
    intpr.load_action_bytecode(s)
    intpr.extract_function(intpr.avm_classes['test'], 'test')
    pyfunc = intpr.avm_classes['test'].method_pyfunctions['test']
    assert pyfunc([]) == 1

# Generated at 2022-06-14 18:31:14.596991
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    import amf
    amf1 = amf.load_amf(open('../../test/swfverification/swfdata'))
    #print(amf1)

    coder = BitPackingDecoder(amf1[b'DoABC'][0][b'code'])
    #print([coder.remaining_bits()])
    swf = SWFInterpreter(coder)
    #print(swf)

    # Assert all constant strings are valid, then print them
    for s in swf.constant_strings:
        assert isinstance(s, compat_str)
    print(swf.constant_strings)
    # Assert all method names are valid, then print them
    for s in swf.method_names:
        assert isinstance(s, compat_str)
    print

# Generated at 2022-06-14 18:31:24.230207
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2022-06-14 18:31:33.602597
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    interpreter = SWFInterpreter(test_data.test_flash_vars['SWFInterpreter'])
    clazz = interpreter.extract_class(
        'com.wimpyplayer.player.WimpyButtonSolo',
        interpreter.abc_tags[0].abc_file)
    assert clazz.class_name == 'com/wimpyplayer/player/WimpyButtonSolo'
    assert clazz.method_names == set([
        'WimpyButtonSolo', 'com/wimpyplayer/player/WimpyButtonSolo',
        'setPlayerSize', 'onClick', 'setButtonSize', 'setClipNo'])



# Generated at 2022-06-14 18:31:41.403831
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    interpreter = SWFInterpreter()
    swf_bytes = get_test_data('swf/test.swf')
    swf_file = io.BytesIO(swf_bytes)
    interpreter.load(swf_file)
    assert len(interpreter.constant_strings) == 12
    assert interpreter.constant_strings[0] == 'file:///C:/Users/Sebastian/Desktop/Videos/Making a Video Game in 48 Hours/video-week2.flv'
    assert interpreter.constant_strings[1] == 'video'
    assert interpreter.constant_strings[2] == '3.0.0'
    assert interpreter.constant_strings[3] == 'A video player for YouTube'

# Generated at 2022-06-14 18:31:51.671372
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2022-06-14 18:32:02.421100
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    interp = SWFInterpreter()
    
    func_name = 'testfunc'
    #                                                 0   5  10  15  20  25  30  35  40  45  50  55  60  65  70  75  80  85  90  95 100 105 110 115 120 125