

# Generated at 2022-06-14 18:24:49.126915
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    interpreter = SWFInterpreter()
    class_ = _AVMClass()
    interpreter.extract_class(class_)


# Generated at 2022-06-14 18:24:57.746872
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    swf = SWFInterpreter('tests/swf/a.swf')
    assert swf.extract_function(swf.classes['Main'], 'foo') is not None
    assert swf.extract_function(swf.classes['Main'], 'i') is not None
    assert swf.extract_function(swf.classes['Main'], 'j') is not None
    assert swf.extract_function(swf.classes['Main'], 'k') is not None
    assert swf.extract_function(swf.classes['Main'], 'l') is not None
    assert swf.extract_function(swf.classes['Main'], 'm') is not None
    assert swf.extract_function(swf.classes['Main'], 'n') is not None
    assert sw

# Generated at 2022-06-14 18:25:09.541677
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    import xml.etree.ElementTree as ET
    interpreter = SWFInterpreter()
    tests_dir = os.path.normpath(os.path.join(__file__, '..', 'tests'))
    test_file_name = os.path.join(tests_dir, 'LA_Times_Player.swf')
    with open(test_file_name, 'rb') as f:
        parser = SWFParser(io.BytesIO(f.read()))
        for tag in parser.iter_tags():
            tag_type = tag[0]
            if tag_type == 69:
                data = tag[1]
                # Find action script code (AbcFile) in DefineSprite tag
                abc_file = data[3]

# Generated at 2022-06-14 18:25:15.854961
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    avm_interpreter = SWFInterpreter()
    avm_interpreter.parse(
        os.path.join(os.path.dirname(__file__), 'test.swf'))
    avm_interpreter.build()
    res = avm_interpreter.execute(
        'Main', 'main', [10, 20])
    assert res == [30, 50, 'undefined']

if __name__ == '__main__':
    test_SWFInterpreter()


# vim:set ts=4 sw=4 et:

# Generated at 2022-06-14 18:25:24.038506
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    decoder = SWFInterpreter('tests/test.swf', 'tests/test.py')
    assert len(decoder.constant_strings) == 10
    assert len(decoder.multinames) == 12
    assert decoder.constant_strings[1] == 'URLFetchVariables'
    assert decoder.constant_strings[2] == 'A'
    assert decoder.constant_strings[3] == 'B'
    assert decoder.constant_strings[4] == 'C'
    assert decoder.constant_strings[5] == 'D'
    assert decoder.constant_strings[6] == 'E'
    assert decoder.constant_strings[7] == 'F'
    assert decoder.constant_strings[8] == 'G'

# Generated at 2022-06-14 18:25:35.503135
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    import base64

# Generated at 2022-06-14 18:25:42.941746
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    class _AVMClass(dict):
        pass
    avm_class = _AVMClass()
    avm_class.variables = {}

    self = SWFInterpreter()
    func_name = 'f'
    with io.BytesIO(b'\x10\x00\x2A\x00j\x00\x02\x00\x00\x00\x00j\x01\x02\x00\x00\x00\x00') as coder:
        resfunc = self.extract_function(avm_class, func_name, coder)
        assert resfunc() == 20

# Generated at 2022-06-14 18:25:50.297039
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    import unittest
    from StringIO import StringIO

# Generated at 2022-06-14 18:25:58.561255
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    interp = _SWFInterpreter()

# Generated at 2022-06-14 18:26:10.911215
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():

    class DummyAVMClass(object):
        def __init__(self):
            self.method_names = []
            self.static_properties = {}
            self.method_pyfunctions = {}
    avm_class = DummyAVMClass()

    class DummySWF(object):
        def __init__(self):
            self.constant_strings = ['abc']
            self.multinames = []
    swf = DummySWF()

    def test_method(stack):
        assert stack[-1] == 'abc'
        stack[-1] = 'def'
        return undefined

    interp = SWFInterpreter()
    interp._wrap_class_method(
        test_method, swf, avm_class, 'test_method')

# Generated at 2022-06-14 18:27:17.827710
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    from os.path import dirname, join
    from .utils import _swf_path

    f = open(join(dirname(__file__), _swf_path(
        'edit_event-2.swf')), 'rb')
    swf = f.read()
    f.close()

    interpreter = SWFInterpreter(swf)

    assert len(interpreter.constant_arrays) > 0
    interpreter.extract_class({}, None, 0)

    assert len(interpreter.constant_arrays) > 0
    assert len(interpreter.constant_strings) > 0
    assert len(interpreter.constant_namespaces) > 0
    assert len(interpreter.constant_multinames) > 0


# Generated at 2022-06-14 18:27:23.092407
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2022-06-14 18:27:32.456154
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2022-06-14 18:27:38.631857
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    from avm2lib.parser import Parser
    from avm2lib.actions import ActionGetURL2

    swf_interpreter = SWFInterpreter(Parser())
    swf_interpreter.register_class('Array', [], [('push', ['*'])])
    class_ = swf_interpreter.register_class('Main', [], [('main', [])])

    func = swf_interpreter.extract_function(
        class_, 'main', [
            8,  # Go back to beginning
            0x43, 0, 0,  # newfunction
            0x24, 0,  # pushscope 0
            0x41, 0,  # callfunction 0
            0x1d,  # returnvoid
        ])

    res = func()
    assert res is undefined


# Generated at 2022-06-14 18:27:45.697843
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    from . import _fixtures as f
    from . import _read_fixture_data
    swfi = SWFInterpreter()

    class1 = swfi.get_class(_read_fixture_data('GimmeSomeCookie.class1'))
    assert class1.package_name == 'gimmesomecookie'
    assert class1.class_name == 'Class1'
    class1.make_object()
    assert class1.variables == {
        'cookie': '...'
    }

    class2 = swfi.get_class(_read_fixture_data('GimmeSomeCookie.class2'))
    assert class2.package_name == ''
    assert class2.class_name == 'Class2'
    class2.make_object()


# Generated at 2022-06-14 18:27:56.723047
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    print('Testing SWFInterpreter()')
    # The data was generated from the SWF file
    # of the video "https://youtu.be/pEbV7L-qoHg"
    # by the commands:
    #   $ swfdump pEbV7L-qoHg.swf
    #   $ swfdump -a pEbV7L-qoHg.swf

# Generated at 2022-06-14 18:28:07.822873
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    # Create an SWFInterpreter object
    swf_file = SWFInterpreter("../lib/uwsc.swf")
    swf_file.parse_header()

    # Test if the property ``self.version`` is an integer
    assert isinstance(swf_file.version, int)
    assert swf_file.version == 11

    # Test if the property ``self.file_length`` is an integer, and correct
    assert isinstance(swf_file.file_length, int)
    assert swf_file.file_length == 965824

    # Test if the property ``self.frame_size`` is a dictionary, and correct
    assert isinstance(swf_file.frame_size, dict)
    assert swf_file.frame_size['nbits'] == 17

# Generated at 2022-06-14 18:28:18.495194
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    swf_filename = '../test/data/test_constructor.swf'
    swf_interpreter = SWFInterpreter(swf_filename)

    assert len(swf_interpreter.constant_strings) == 3
    assert swf_interpreter.constant_strings[0] == 'undefined'
    assert swf_interpreter.constant_strings[1] == 'Class'
    assert swf_interpreter.constant_strings[2] == 'prototype'

    assert len(swf_interpreter.multinames) == 20

# Generated at 2022-06-14 18:28:31.020760
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2022-06-14 18:28:38.876208
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    import os
    import tempfile
    from subprocess import Popen, PIPE, check_call
    from io import BytesIO
    import pytest

    test_directory = os.path.dirname(os.path.abspath(__file__))

# Generated at 2022-06-14 18:30:31.611067
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    swf = SWFStream(_TEST_SWF)
    swf.read_tags()
    assert swf.version == 11
    assert swf.file_length == _TEST_SWF_LEN

    swf.swf_interpreter = SWFInterpreter(swf)
    assert swf.swf_interpreter.constant_strings == [
        '', 'abcdefg', 'abcdefg', 'abcdefg',
        'abcdefg', 'abcdefg', 'abcdefg', 'abcdefg',
        'abcdefg', 'abcdefg', 'abcdefg', 'abcdefg',
        '', '', '', '', '', '']

    assert swf.swf_interpreter.constant_ints == [0]


# Generated at 2022-06-14 18:30:39.313869
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    with compat_urlopen(AMF_SWF_URL) as f:
        swf_file = f.read()

    with io.BytesIO(swf_file) as f:
        interpreter = SWFInterpreter(f)

    assert 'NetConnection' in interpreter.avm2_classes
    assert 'Object' in interpreter.avm2_classes
    assert 'flash.text.TextField' in interpreter.avm2_classes
    assert 'send' in interpreter.avm2_classes['NetConnection'].method_names



# Generated at 2022-06-14 18:30:47.862980
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    from .test_swf_classes import test_swf_with_method_swf
    from .test_avm2_classes_wiki import test_avm2_with_method_wiki
    for swf in [test_swf_with_method_swf, test_avm2_with_method_wiki]:
        si = SWFInterpreter(swf)
        sx = si.extract_method(0, 'swf')
        assert sx([1]) == 0
    sx = si.extract_method(0, 'wiki')
    assert sx([1]) == 2

# Generated at 2022-06-14 18:30:58.197972
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    class _AVMClass(object):
        variables = {
            'qqq': 'qqq',
        }
        constants = {
        }
        static_properties = {
        }
        static_methods = {
        }
        method_pyfunctions = {
        }
        method_names = {
        }
        make_object = None

    class _AVMClass_Object(object):
        def __init__(self, avm_class):
            self.avm_class = avm_class
            self.variables = {
                'qqq': 'qqq',
            }
            self.methods = {
            }

        def call_method(self, method_name, args):
            return self.methods[method_name](args)

    interp = SWFInterpreter(None)



# Generated at 2022-06-14 18:31:06.294196
# Unit test for constructor of class SWFInterpreter

# Generated at 2022-06-14 18:31:13.997303
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    from ..tag import TagDefineBinaryData, TagDoABC
    from ..abc import ABCFile

# Generated at 2022-06-14 18:31:19.467203
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    swf = io.BytesIO()
    swf.write(b"FWS")
    swf.write(b'\x09')
    swf.write(b'\x00\x00\x00')
    swf.write(b'\x00\x00\x00\x00')
    swf.write(b'\x20')
    swf.write(
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    # empty tag (a bit more than minimum length)
    swf.write(b'\x00\x00\x00\x00\x00\x00\x00')

# Generated at 2022-06-14 18:31:27.594959
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    import codecs
    import re

    assert hasattr(SWFInterpreter, 'extract_function'),\
        'SWFInterpreter must have a method extract_function()'

    # copied from https://github.com/rg3/youtube-dl/blob/master/youtube_dl/utils.py
    def compat_chr(i):
        return chr(i) if isinstance(i, int) else i

    def hex_xor(s1, s2):
        xored = ''.join([compat_chr(ord(x) ^ ord(y)) for x, y in zip(s1, s2)])
        assert len(xored) == len(s1), '%r != %r' % (len(xored), len(s1))

# Generated at 2022-06-14 18:31:37.564430
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    with open('test2.swf', 'rb') as f:
        data = f.read()
    data = bytearray(data)

    with open('test3.swf', 'rb') as f:
        data2 = f.read()
    data2 = bytearray(data2)

    with open('test4.swf', 'rb') as f:
        data3 = f.read()
    data3 = bytearray(data3)

    interpreter = SWFInterpreter()
    interpreter.extract_class(data)
    interpreter.extract_class(data2)
    interpreter.extract_class(data3)
    return interpreter


# Generated at 2022-06-14 18:31:49.770124
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    from .swftags import DoActionTag
    si = SWFInterpreter()
    da_tag = DoActionTag()