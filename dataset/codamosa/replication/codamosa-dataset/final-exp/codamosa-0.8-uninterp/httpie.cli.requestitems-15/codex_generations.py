

# Generated at 2022-06-13 21:19:28.276886
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    filename = 'test.txt'
    mime_type = 'text/plain'
    f = open('/Users/yaluo/Documents/GitHub/20190707/httpie-0.9.9.tar.gz', 'rb')
    value = process_file_upload_arg(KeyValueArg(key='image',
        value=f'{filename}{SEPARATOR_FILE_UPLOAD_TYPE}{mime_type}', sep=SEPARATOR_FILE_UPLOAD))
    assert value == (filename, f, mime_type)


# Generated at 2022-06-13 21:19:35.608551
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    req_item_args = [
        KeyValueArg(
            key="foo",
            sep=SEPARATOR_DATA_EMBED_RAW_JSON_FILE,
            value="bar",
            orig="foo@<bar.json"
        )
    ]
    
    value = RequestItems.from_args(req_item_args).data["foo"]
    assert value == {"bar": "bar", "foo": []}



# Generated at 2022-06-13 21:19:40.069486
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    arg = KeyValueArg('', SEPARATOR_DATA_EMBED_RAW_JSON_FILE, '{"debug":1}')
    result = process_data_embed_raw_json_file_arg(arg)
    assert result == {"debug": 1}



# Generated at 2022-06-13 21:19:48.645327
# Unit test for function process_data_raw_json_embed_arg
def test_process_data_raw_json_embed_arg():
    assert process_data_raw_json_embed_arg(KeyValueArg(
        'data', '{"key1": "val1", "key2": [1, 2]}')) == {"key1": "val1", "key2": [1, 2]}
    try:
        assert process_data_raw_json_embed_arg(KeyValueArg(
            'data', '{"key1": "val1", "key2": [1, 2}')) # invalid json string
        assert False
    except ParseError:
        assert True

# Generated at 2022-06-13 21:19:57.163757
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    #Load a json file which is valid
    actual = process_data_embed_raw_json_file_arg(KeyValueArg('key',r'{"name":"john"}'))
    expected = {"name":"john"}
    assert actual == expected
    #Load a json file which is not valid
    with pytest.raises(ParseError):
        process_data_embed_raw_json_file_arg(KeyValueArg('key',r'{"name":"john"}"'))

# Generated at 2022-06-13 21:19:58.452849
# Unit test for function load_text_file
def test_load_text_file():
    load_text_file("..")


# Generated at 2022-06-13 21:20:07.978595
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    arg = KeyValueArg('--json', '', '', '', '{ "a": "b"}')
    res = process_data_embed_raw_json_file_arg(arg)
    assert res == { "a": "b"}

    arg = KeyValueArg('--json', '', '', '', '{ "a": "c"}')
    res = process_data_embed_raw_json_file_arg(arg)
    assert res == { "a": "c"}

# Generated at 2022-06-13 21:20:12.679777
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    arg = KeyValueArg('--data', value='test.txt:text/plain:test')
    filename, file, mimetype = process_file_upload_arg(arg)
    assert filename == 'test.png'
    assert mimetype == 'text/plain'
    assert file.read() == b'test'


# Generated at 2022-06-13 21:20:18.441345
# Unit test for function process_data_raw_json_embed_arg
def test_process_data_raw_json_embed_arg():
    arg = KeyValueArg(key="", value="a", sep=SEPARATOR_DATA_RAW_JSON)
    assert process_data_raw_json_embed_arg(arg) == "a"

    arg = KeyValueArg(key="", value="a", sep=SEPARATOR_DATA_EMBED_RAW_JSON_FILE)
    with pytest.raises(ParseError):
        process_data_raw_json_embed_arg(arg)

# Generated at 2022-06-13 21:20:25.876515
# Unit test for function load_text_file
def test_load_text_file():
    with open('test.txt', 'w') as f:
        f.write('test')
    try:
        res = load_text_file(KeyValueArg(
            'dummy', 'dummy', '', 'dummy', 'dummy', value='test.txt'),)
        print(res)
    finally:
        os.remove('test.txt')


# Generated at 2022-06-13 21:20:35.803138
# Unit test for function load_text_file
def test_load_text_file():
    testArg = KeyValueArg(orig='hi.txt',
                          key='w',
                          sep='@',
                          value='hi.txt')
    return load_text_file(testArg)


# Generated at 2022-06-13 21:20:44.012770
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    arg = KeyValueArg(
        key = 'key1',
        sep = SEPARATOR_DATA_EMBED_RAW_JSON_FILE,
        orig = 'key1:=@data.json',
        value = 'data.json'
    )
    try:
        value = process_data_embed_raw_json_file_arg(arg)
        assert isinstance(value, dict)
    except Exception as e:
        assert False, 'Should not raise the exception'



# Generated at 2022-06-13 21:20:47.215755
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    item = KeyValueArg(key=None, sep=SEPARATOR_DATA_EMBED_RAW_JSON_FILE, value=None)
    process_data_embed_raw_json_file_arg(item)

# Generated at 2022-06-13 21:20:51.163965
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    arg = KeyValueArg('filename', None, 'filename')
    filename, f, mime_type = process_file_upload_arg(arg)

# Generated at 2022-06-13 21:20:54.953329
# Unit test for function load_text_file
def test_load_text_file():
    try:
        assert load_text_file(arg) == 'Hello, World!'
    except ParseError as e:
        print(e)
    

# Generated at 2022-06-13 21:21:02.879272
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    print('test_process_file_upload_arg')
    import sys
    import pdb
    pdb.Pdb(stdout=sys.__stdout__).set_trace()
    import io
    try:
        f = open(os.path.expanduser('~/Downloads/Untitled.png'), 'rb')
    except Exception as e:
        raise ParseError('"%s": %s' % ('test', e))

    print(f)

if __name__ == '__main__':
    print('hello')
    test_process_file_upload_arg()

# Generated at 2022-06-13 21:21:14.277424
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    data_embed_raw_json_file_arg = KeyValueArg('data1', 'file=./test_data.json')
    answer = {
        "firstName": "John",
        "lastName": "Smith",
        "age": 25,
        "address": {
            "streetAddress": "21 2nd Street",
            "city": "New York",
            "state": "NY",
            "postalCode": "10021"
        },
        "phoneNumber": [
            {
                "type": "home",
                "number": "212 555-1234"
            },
            {
                "type": "fax",
                "number": "646 555-4567"
            }
        ]
    }

# Generated at 2022-06-13 21:21:21.213249
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    file_upload_arg = "test_file.txt:/home/username/test_file.txt:image/jpeg"
    import types
    assert isinstance(process_file_upload_arg(KeyValueArg(":", None, file_upload_arg)), types.GeneratorType)


# Generated at 2022-06-13 21:21:25.522613
# Unit test for function load_text_file
def test_load_text_file():
    assert load_text_file(KeyValueArg(orig="bob.txt", sep=";", key="", value="bob.txt")) == "bob\n"
    assert load_text_file(KeyValueArg(orig="dave.txt", sep=";", key="", value="dave.txt")) == "dave\n"



# Generated at 2022-06-13 21:21:28.162969
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    item=KeyValueArg(orig='b.txt',key='b',sep='',value='b.txt')
    assert process_data_embed_raw_json_file_arg(item) == '{}'

# Generated at 2022-06-13 21:21:38.490639
# Unit test for function load_text_file
def test_load_text_file():
    # given
    file_path = '.'
    key_value_arg = KeyValueArg(None, '.', '.')
    # when
    i = load_text_file(key_value_arg)
    # then
    assert isinstance(i, str)

# Generated at 2022-06-13 21:21:43.414059
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
	arg = KeyValueArg(
            '-F',
       	    '-F',
            'file=./test/test_file.txt',
            'file',
            './test/test_file.txt',
            ';',
            False
        )
	test_case = process_file_upload_arg(arg)
	assert test_case == ('test_file.txt', open('./test/test_file.txt', 'rb'), 'text/plain')

# Generated at 2022-06-13 21:21:51.151322
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    # Arrange
    test_arg = KeyValueArg('file', SEPARATOR_FILE_UPLOAD, 'test', orig='test')
    test_arg2 = KeyValueArg('file', SEPARATOR_FILE_UPLOAD, 'test:test', orig='test:test')

    # Act
    f = process_file_upload_arg(test_arg)
    f2 = process_file_upload_arg(test_arg2)

    # Assert
    assert f == ('test', f, None)
    assert f2 == ('test', f, 'test')

# Generated at 2022-06-13 21:21:56.621845
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    arg = KeyValueArg('data_raw_json_embed_arg', ';', '{"a": "b"}', None)
    result = process_data_embed_raw_json_file_arg(arg)
    assert (isinstance(result, dict)) == True
    assert result["a"] == "b"


# Generated at 2022-06-13 21:22:03.554298
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    from httpie.cli.argtypes import KeyValueArg
    from httpie.cli.dicts import RequestFilesDict
    from httpie.cli.exceptions import ParseError
    from httpie.cli.requestitems import process_file_upload_arg
    from httpie.cli.requestitems import RequestItems
    from httpie.streams import RawRequestBodyStream
    import os

    # Case 1: File does not exist
    filename = "a"
    request_item_args = [
        KeyValueArg(
            key=filename,
            value=filename,
            orig="upload=" + filename,
            sep=SEPARATOR_FILE_UPLOAD
        )
    ]
    try:
        r = RequestItems.from_args(request_item_args)
    except ParseError as e:
        print(e)


# Generated at 2022-06-13 21:22:09.945042
# Unit test for function load_text_file
def test_load_text_file():

    # Test for file with absolute path
    test_file_path = '/path/to/file'
    test_file = 'data to embed'
    test_data = 'data;' + test_file_path
    test_arg = KeyValueArg(0,0,0,0,0,0,0,0,0,0, test_data,0,0,0,0)
    temp_file = open(test_file_path, 'w')
    temp_file.write(test_file)
    temp_file.close()
    assert load_text_file(test_arg) == test_file
    os.remove(test_file_path)

    # Test for file with relative path
    test_file_path = 'path/to/file'
    test_file = 'data to embed'

# Generated at 2022-06-13 21:22:14.202455
# Unit test for function load_text_file
def test_load_text_file():
    path = "abc.txt"
    line = "hello"
    file = open(path, 'w')
    file.write(line)
    file.close()
    print(load_text_file(path))
    os.remove(path)


# Generated at 2022-06-13 21:22:16.263027
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    raw_json_string = 'raw json string'
    json_data = process_data_embed_raw_json_file_arg(KeyValueArg(value=raw_json_string))
    assert json_data == raw_json_string

# Generated at 2022-06-13 21:22:19.876647
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    sample = ("a", "./sample.json")
    assert isinstance(process_data_embed_raw_json_file_arg(sample), dict)



# Generated at 2022-06-13 21:22:28.977779
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    arg1 = KeyValueArg(
        '',
        '',
        'httpbin.org/post',
        'data',
        'RawJsonFile@/home/chris/data.json',
        'arg1',
        '',
        'raw-json-file',
        '@',
        '',
        'file',
        '/home/chris/data.json',
    )
    process_data_embed_raw_json_file_arg(arg1)

# Generated at 2022-06-13 21:22:44.553664
# Unit test for function load_text_file
def test_load_text_file():
    import os
    import tempfile
    from pytest import raises

    with tempfile.NamedTemporaryFile(mode='w+') as f:
        test_string = "test_string"
        f.write(test_string)
        f.flush()
        assert load_text_file(KeyValueArg("", "", "", f.name)) == test_string
    assert raises(ParseError, load_text_file, KeyValueArg("", "", "", "/path/to/file/that/does/not/exists"))

# Generated at 2022-06-13 21:22:52.174465
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    test_file = 'C:\\Users\\jb\\Desktop\\test.txt'
    with open(test_file, 'wb+') as wf:
        wf.write(b'aaa')
    wf.close()

    arg = KeyValueArg('file', test_file, 'file@')
    filename, f, mime_type = process_file_upload_arg(arg)

    assert filename == 'test.txt'
    assert f.read() == b'aaa'
    assert mime_type == 'text/plain'
    f.close()

    os.remove(test_file)

# Generated at 2022-06-13 21:22:54.460521
# Unit test for function load_text_file
def test_load_text_file():
    request_item = KeyValueArg(
        key='test',
        sep='=',
        orig='test=test',
        value='test',
    )
    assert load_text_file(request_item) == 'test'

# Generated at 2022-06-13 21:22:57.450341
# Unit test for function load_text_file
def test_load_text_file():
    item = KeyValueArg(
        key='test_key',
        value='test_value',
        sep=';'
    )
    assert load_text_file(item) == 'test_value'

# Generated at 2022-06-13 21:23:04.227374
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    from httpie.cli.argtypes import KeyValueArg
    from httpie.cli.parse import process_file_upload_arg
    from httpie.cli.constants import SEPARATOR_FILE_UPLOAD_TYPE    

    # test regular file upload
    arg = KeyValueArg(sep = SEPARATOR_FILE_UPLOAD, key = "a", value = "~/test.bin")
    assert process_file_upload_arg(arg) == ('test.bin', open('~/test.bin', 'rb'), None)

    # test file upload with MIME type specified
    arg = KeyValueArg(sep = SEPARATOR_FILE_UPLOAD, key = "a", value = "~/test.bin" + SEPARATOR_FILE_UPLOAD_TYPE + "audio/mpeg")
    assert process_file_upload

# Generated at 2022-06-13 21:23:11.807001
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    file_arg = KeyValueArg('name', 'file', ':')
    assert ('file', open(os.path.expanduser('file')), None) == process_file_upload_arg(file_arg)

    file_arg_with_type = KeyValueArg('name', 'file/txt', ':')
    assert ('file', open(os.path.expanduser('file')), 'txt') == process_file_upload_arg(file_arg_with_type)

# Generated at 2022-06-13 21:23:18.591441
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    from httpie.cli.argtypes import KeyValueArg
    from httpie.cli.dicts import RequestJSONDataDict
    testjson = process_data_embed_raw_json_file_arg(KeyValueArg(key='test', sep='=#', value='test.json'))
    testdict = RequestJSONDataDict()
    testdict['test'] = load_json_preserve_order('{"test": "value"}')
    assert testjson == testdict['test']



# Generated at 2022-06-13 21:23:21.645037
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    arg = KeyValueArg('file: /example.txt')
    print(process_file_upload_arg(arg))


# Generated at 2022-06-13 21:23:26.617080
# Unit test for function load_text_file
def test_load_text_file():
    arg = KeyValueArg(orig='--data=@/Users/guanwenxue/Desktop/data.txt', key='', value='/Users/guanwenxue/Desktop/data.txt', sep='=',
                      orig_separator='=')
    data = load_text_file(arg)
    print(data)

# Generated at 2022-06-13 21:23:36.028475
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    # Check if the output of the function is correct if the mime_type is not present.
    content = 'file.txt'
    arg = KeyValueArg('file', 'file.txt', SEPARATOR_FILE_UPLOAD)
    (filename, file, mime_type) = process_file_upload_arg(arg)
    assert file.name == content
    assert mime_type == 'text/plain'

    # Check if the output of the function is correct if the mime_type is present.
    content = 'file.txt'
    arg = KeyValueArg('file', 'file.txt;text/html', SEPARATOR_FILE_UPLOAD)
    (filename, file, mime_type) = process_file_upload_arg(arg)
    assert file.name == content

# Generated at 2022-06-13 21:23:56.074193
# Unit test for function load_text_file
def test_load_text_file():

    with open('httpie/cli/parser_test.txt', 'r') as f:
        expected_result = f.read()

    result = load_text_file(KeyValueArg('', '', '', ''))

    assert result == expected_result

# Generated at 2022-06-13 21:23:59.578473
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    file_name = '/Users/louis/Desktop/httpie/httpie/auth.py'
    arg = KeyValueArg('-F', '', 'name=@' + file_name)
    print(process_file_upload_arg(arg))

# Generated at 2022-06-13 21:24:06.156797
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    arg = KeyValueArg(orig = "json@data.json", sep = SEPARATOR_DATA_EMBED_RAW_JSON_FILE, key = "json", value = "data.json")
    assert process_data_embed_raw_json_file_arg(arg) == {'a': 1, 'b': 3.14, 'c': 'foo', 'd': True, 'e': None, 'f': [1, 2, 3], 'g': {'k1':10, 'k2':20}}

# Generated at 2022-06-13 21:24:14.230534
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    filename="a.txt"
    mime_type="txt"
    s=filename+":"+mime_type
    arg=KeyValueArg(SEPARATOR_FILE_UPLOAD,filename,s)
    a,b,c=process_file_upload_arg(arg)
    assert a=="a.txt"
    assert b.mode=="rb"
    assert c=="txt"
    filename2 = "a.txt"
    s2 = filename2
    arg2 = KeyValueArg(SEPARATOR_FILE_UPLOAD, filename2, s2)
    a2, b2, c2 = process_file_upload_arg(arg2)
    assert a2 == "a.txt"
    assert b2.mode == "rb"
    assert c2=="text/plain"



# Generated at 2022-06-13 21:24:25.101169
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    f = open(os.path.expanduser('file.png'), 'rb')
    mime_type = 'application/octet-stream'
    file_name = 'file.png'
    arg = KeyValueArg(key='', value='file.png', sep=SEPARATOR_FILE_UPLOAD)
    filename, f, mime_type = process_file_upload_arg(arg)
    assert(filename == file_name)
    assert(f == f)
    assert(mime_type == mime_type)

# Generated at 2022-06-13 21:24:29.277068
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    result = process_file_upload_arg(
        KeyValueArg('name', 'data/sample.json')
    )

# Generated at 2022-06-13 21:24:37.565857
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    data = process_file_upload_arg(KeyValueArg(
        "content-disposition: form-data; name=\"file\"; filename=\"/home/tesseract/tt/a.txt\"",
        "content-type: application/x-www-form-urlencoded"))
    assert data == ('a.txt', open('/home/tesseract/tt/a.txt', 'rb'), 'application/x-www-form-urlencoded')
    data = process_file_upload_arg(KeyValueArg(
        "content-disposition: form-data; name=\"file\"; filename=\"/home/tesseract/tt/a.txt\"",
        None))
    print(data)

# Generated at 2022-06-13 21:24:46.077775
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    result = process_file_upload_arg(KeyValueArg('@', 'file', 'test.txt'))
    assert result[0] == 'test.txt'
    assert result[2] == 'text/plain'
    result = process_file_upload_arg(KeyValueArg('@', 'file', 'test.txt;image'))
    assert result[0] == 'test.txt'
    assert result[2] == 'image'


# Generated at 2022-06-13 21:24:54.333582
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    arg = KeyValueArg('name', './tests/fixtures.py')
    assert isinstance(process_file_upload_arg(arg), tuple)
    arg = KeyValueArg('name', './tests/fixtures.py;text/html')
    assert isinstance(process_file_upload_arg(arg), tuple)
    try:
        arg = KeyValueArg('name', './tests/fixtures;text/html')
        process_file_upload_arg(arg)
        assert False
    except ParseError:
        pass

# Generated at 2022-06-13 21:24:59.731773
# Unit test for function load_text_file
def test_load_text_file():
    data = 'A test file.\n'
    with tempfile.NamedTemporaryFile("w+") as f:
        f.write(data)
        f.seek(0)
        path = f.name
        print(f"file {path} created.")
        value = load_text_file(path)
        print(value)
        assert value == data

# Generated at 2022-06-13 21:25:38.356599
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    from httpie.cli.dicts import RequestJSONDataDict
    process_data_embed_raw_json_file_arg(KeyValueArg(0, '-d', '{}'))
    process_data_embed_raw_json_file_arg(KeyValueArg(0, '-d@', '{}'))

# Generated at 2022-06-13 21:25:50.716717
# Unit test for function process_data_embed_raw_json_file_arg

# Generated at 2022-06-13 21:26:00.782149
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    arg = KeyValueArg(key='test', sep=SEPARATOR_FILE_UPLOAD, value='./test.txt')
    fup_arg = process_file_upload_arg(arg)
    assert(fup_arg[0] == 'test.txt')
    with open(os.path.expanduser('./test.txt'), 'rb') as f:
        assert(fup_arg[1] == f)
    assert(fup_arg[2] == 'text/plain')


# Generated at 2022-06-13 21:26:04.177269
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    file = process_file_upload_arg(KeyValueArg("f;foo/bar;/tmp/test.txt"))

    if file == ("test.txt", open("/tmp/test.txt", 'rb'), "foo/bar"):
        return True
    
    return False

# Generated at 2022-06-13 21:26:19.959581
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    filename = 'httpie/__init__.py'
    mime_type = 'text/plain'
    f = open(filename, 'rb')
    value = SEPARATOR_FILE_UPLOAD + SEPARATOR_FILE_UPLOAD_TYPE + mime_type
    arg = KeyValueArg(SEPARATOR_FILE_UPLOAD, "file", value, value)
    file_name, f_, mime_type_ = process_file_upload_arg(arg)
    print(file_name)
    print(f_.read())
    print(mime_type_)
    assert file_name == os.path.basename(filename)
    assert f_.read().decode() == f.read().decode()
    assert mime_type_ == mime_type

# Generated at 2022-06-13 21:26:29.931689
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    arg = KeyValueArg("Basic", "file=C:\\Users\\User\\Pictures\\test2.png")
    expected = ("test2.png", open("C:\\Users\\User\\Pictures\\test2.png", "rb"), None)
    actual = process_file_upload_arg(arg)
    assert expected[0] == actual[0]
    assert expected[2] == actual[2]
    assert (expected[1].read() == actual[1].read())



# Generated at 2022-06-13 21:26:36.488897
# Unit test for function load_text_file
def test_load_text_file():
    test_data = [
        ('a', 'a'),
        ('a.txt', 'a')
    ]
    for value, expect in test_data:
        file_path = 'httpie/cli/test/data/json/{}'.format(value)
        item = KeyValueArg(
            'a',
            file_path,
            '',
            '',
            '',
            ''
        )
        result = load_text_file(item)
        assert result == expect, 'load_text_file {} {}'.format(
            value, result
        )


# Generated at 2022-06-13 21:26:41.561864
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    arg = KeyValueArg(key='test', sep=SEPARATOR_HEADER, value='')
    print(process_data_embed_raw_json_file_arg(arg))


if __name__ == "__main__":
    test_process_data_embed_raw_json_file_arg()

# Generated at 2022-06-13 21:26:45.029374
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    arg = KeyValueArg('path/to/file')
    assert 'file' == process_file_upload_arg(arg)[0]

# Generated at 2022-06-13 21:26:51.804093
# Unit test for function load_text_file
def test_load_text_file():
    item = KeyValueArg(value='-d', orig='-d')
    with open('test.txt', 'w') as f:
        f.write('hello this is test file')
    assert load_text_file(item) == 'hello this is test file'
    os.remove('test.txt')

# Generated at 2022-06-13 21:27:34.256405
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():

    import sys
    from pathlib import Path
    current_path = Path(__file__).resolve()
    print("Current path: " + str(current_path))
    sys_path = str(current_path.parent.parent.parent)
    print("Adding " + str(sys_path))
    sys.path.append(sys_path)

    from httpie.cli.argtypes import KeyValueArg

    arg = KeyValueArg("data@./data/test_data.json")
    value = process_data_embed_raw_json_file_arg(arg)
    print("Value: " + str(value))
    assert False

# Generated at 2022-06-13 21:27:42.311002
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    args=["CreatePost", "http://localhost/posts", "Authorization:Basic YWRtaW46YWRtaW4=", "title=MyTest&body=This is a new post", "Content-Type:application/json", "--debug"]
    request_item_args = [KeyValueArg(arg) for arg in args]
    request_items = RequestItems.from_args(request_item_args)
    assert request_items.params.get("Authorization")=="Basic YWRtaW46YWRtaW4="

# Generated at 2022-06-13 21:27:46.997692
# Unit test for function load_text_file
def test_load_text_file():
    assert load_text_file("a.txt") == "a"



# Generated at 2022-06-13 21:27:55.201330
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    class KeyValueArg:
        def __init__(self, sep='', key='', value=''):
            self.sep = sep
            self.key = key
            self.value = value
            self.orig = ''
    arg = KeyValueArg(sep=SEPARATOR_DATA_EMBED_RAW_JSON_FILE, key='test', value='test.json')
    value = process_data_embed_raw_json_file_arg(arg)
    print(value)

# Generated at 2022-06-13 21:27:59.713504
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    from httpie.cli.argtypes import KeyValueArg
    file_upload_arg = KeyValueArg.from_str('data@file_upload;text/plain;filename=a.txt')
    tuple = process_file_upload_arg(file_upload_arg)
    assert tuple[0] == 'a.txt'
    assert tuple[2] == 'text/plain'

# Generated at 2022-06-13 21:28:00.852696
# Unit test for function load_text_file
def test_load_text_file():
    assert load_text_file(KeyValueArg("test", "", "")) == ""

# Generated at 2022-06-13 21:28:12.922420
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    # Dict of JSON objects
    test_case = "./test_files/test_json_dict.json"

# Generated at 2022-06-13 21:28:15.557789
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    print(process_data_embed_raw_json_file_arg(arg='process_data_embed_raw_json_file_arg'))


# Generated at 2022-06-13 21:28:32.070966
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    # valid json file
    key_value_arg1 = KeyValueArg('-d', '@', 'valid.json')
    data1 = process_data_embed_raw_json_file_arg(key_value_arg1)
    assert data1 == [1, 2, 3]

    # invalid json file
    key_value_arg2 = KeyValueArg('-d', '@', 'invalid.json')
    try:
        data2 = process_data_embed_raw_json_file_arg(key_value_arg2)
    except ParseError as e:
        assert str(e) == '"-d @invalid.json": Expecting value: line 1 column' \
                         ' 1 (char 0)'


# Generated at 2022-06-13 21:28:34.561261
# Unit test for function load_text_file
def test_load_text_file():
    arg = KeyValueArg('Header', 'example.txt')
    result = load_text_file(arg)
    assert result == '1234567890'
