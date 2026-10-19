

# Generated at 2022-06-13 21:19:22.031113
# Unit test for function process_data_raw_json_embed_arg
def test_process_data_raw_json_embed_arg():
    value = process_data_raw_json_embed_arg(KeyValueArg('-d', '{ "key": 100 }'))
    assert value['key'] == 100
    print('Value = ', value)

# Generated at 2022-06-13 21:19:26.668968
# Unit test for function load_text_file
def test_load_text_file():
    item = KeyValueArg(None, None, None, None, None, None)
    item.orig = None
    item.value = './httpie_logs/test.txt'
    with open(os.path.expanduser(item.value), 'rb') as f:
        assert f.read().decode() == load_text_file(item)

# Generated at 2022-06-13 21:19:32.501880
# Unit test for function load_text_file
def test_load_text_file():
    path = './tests/data/utf8.txt'
    item = KeyValueArg(key='', sep=SEPARATOR_DATA_EMBED_FILE_CONTENTS, value=path)
    assert load_text_file(item) == '世界\n'



# Generated at 2022-06-13 21:19:45.012024
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    def test_load_json(arg: str, contents: str) -> bool:
        try:
            load_json(arg, contents)
            return True
        except ParseError as e:
            return False

    assert test_load_json("@{}", "{}")
    assert test_load_json("@{}", "{\"a\":1}")
    assert test_load_json("@{}", "{\"b\":true}")
    assert test_load_json("@{}", "{\"c\":\"abc\"}")
    assert test_load_json("@{}", "{\"d\":null}")
    assert test_load_json("@{}", "{\"d\":null, \"e\": [1, \"a\", true]}")

# Generated at 2022-06-13 21:19:51.686060
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    my_dict = {
        "color": "red",
        "value": "#f00",
        "colors":{
            "color": "red",
            "value": "#f00",
        }
    }
    json = json.dumps(my_dict)
    file = open('test_json','w+')
    file.write(json)
    file.close()
    arg = KeyValueArg('test', value='test_json')
    f = process_data_embed_raw_json_file_arg(arg)
    print(f)
    assert f == my_dict

# Generated at 2022-06-13 21:19:58.454279
# Unit test for function process_data_raw_json_embed_arg
def test_process_data_raw_json_embed_arg():
    """This unit test tests function process_data_raw_json_embed_arg()"""
    assert process_data_raw_json_embed_arg(KeyValueArg('-d', '{}')) == {}
    with pytest.raises(ParseError):
        process_data_raw_json_embed_arg(KeyValueArg('-d', '{{'))

# Generated at 2022-06-13 21:19:59.277405
# Unit test for function process_data_raw_json_embed_arg
def test_process_data_raw_json_embed_arg():
    pass

# Generated at 2022-06-13 21:20:07.286166
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    assert (
        process_file_upload_arg(KeyValueArg('avatar', 'image.png',
                      '@')) ==
        ('image.png', open(os.path.expanduser('image.png'), 'rb'), None)
    )

    assert (
        process_file_upload_arg(KeyValueArg('avatar', 'image.png',
                      '@'))[0] == 'image.png'
    )

    assert (
        process_file_upload_arg(KeyValueArg('avatar', 'image.png',
                      '@'))[1] == open(os.path.expanduser('image.png'), 'rb')
    )


# Generated at 2022-06-13 21:20:22.444907
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    ## Test for invalid JSON
    print("Testing for invalid JSON")
    print("=======================")
    try:
        json_value = process_data_embed_raw_json_file_arg(KeyValueArg(orig=KeyValueArg("foo.json"), sep=SEPARATOR_DATA_EMBED_RAW_JSON_FILE, key="data", value=KeyValueArg("foo.json")))
    except ParseError as e:
        print("Expected Exception: " + str(e))
    else:
        raise AssertionError("process_data_embed_raw_json_file_arg did not raise exception as expected")
    
    ## Test for valid JSON without value
    print("Testing for valid JSON without value")
    print("====================================")

# Generated at 2022-06-13 21:20:28.118450
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    arg = KeyValueArg(SEPARATOR_DATA_EMBED_RAW_JSON_FILE, "", "C:\\Users\\123.json")
    val = process_data_embed_raw_json_file_arg(arg)
    assert val == ""

    arg = KeyValueArg(SEPARATOR_DATA_EMBED_RAW_JSON_FILE, "", "")
    try:
        process_data_embed_raw_json_file_arg(arg)
        assert False
    except ParseError:
        assert True

# Generated at 2022-06-13 21:20:49.154951
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    file_name = "test_output.txt"
    file = open(file_name, "w")
    file.close()

    request_item_args = [
        ("", "-F", "test_output.txt")
    ]
    result = process_file_upload_arg(request_item_args)

    assert (result == (os.path.basename(file_name), file, get_content_type(file_name)))

    os.remove(file_name)

# Generated at 2022-06-13 21:20:57.277806
# Unit test for function load_text_file
def test_load_text_file():
    datadir = os.path.dirname(os.path.abspath(__file__))
    datadir = os.path.join(datadir, "data")
    item = KeyValueArg("request_item_args", "-d", "embed@"+os.path.join(datadir, "test_file.txt"))
    content = load_text_file(item)
    assert content == "test\n", "content not same as test"


# Generated at 2022-06-13 21:21:04.604384
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    command = ["--form", "upload=test.txt"]
    parser = ArgParser()
    args = parser.parse_args(args=command)
    assert len(args.items) == 1
    assert isinstance(args.items[0], KeyValueArg)
    assert args.items[0].key == 'upload'
    assert args.items[0].sep == '='
    assert args.items[0].value == "test.txt"



# Generated at 2022-06-13 21:21:15.685921
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    # Create a KeyValueArg Object with a separator starting with '@'
    # key: file_name.json, value: {'firstName':'Vincent','surname':'Vega'}
    test_arg = KeyValueArg('@', 'file_name.json', "{'firstName':'Vincent','surname':'Vega'}")
    # Create a JSON Object for the comparison
    test_json = {'firstName':'Vincent','surname':'Vega'}
    # call the function
    test_result = process_data_embed_raw_json_file_arg(test_arg)
    # check the type of the result if it is a dictionary
    assert type(test_result) is dict
    # check that all the keys of the result is the same with the comparison JSON

# Generated at 2022-06-13 21:21:27.249190
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    from httpie import input

    def parse_arg(value: str) -> KeyValueArg:
        return input.KeyValueArg(value)

    def input_arg(value: str) -> KeyValueArg:
        arg = parse_arg(value)
        process_data_embed_raw_json_file_arg(arg)
        return arg

    assert input_arg('~/test_file_1').value == load_json_preserve_order(
        load_text_file(parse_arg('~/test_file_1')))
    assert input_arg('/test_file_2').value == load_json_preserve_order(
        load_text_file(parse_arg('/test_file_2')))

# Generated at 2022-06-13 21:21:34.105286
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    arg = KeyValueArg('type : C:/Users/james/Desktop/123.pptx')
    # No mime type
    process_file_upload_arg(arg)
    arg_type = KeyValueArg('type : C:/Users/james/Desktop/123.pptx; application/vnd.openxmlformats-officedocument.presentationml.presentation')
    # With mime type
    process_file_upload_arg(arg_type)

# Generated at 2022-06-13 21:21:37.941790
# Unit test for function load_text_file
def test_load_text_file():
    abc = "tests/files/abcd.txt"
    assert load_text_file(KeyValueArg("key", abc, "embed", "key=:" + abc)) == "abcd\n"


# Generated at 2022-06-13 21:21:45.359620
# Unit test for function load_text_file
def test_load_text_file():
    print("Success")
    with open("input.txt", "a") as f:
        f.write("Hello, World!")
    assert (load_text_file(KeyValueArg("input.txt")) == "Hello, World!")
    os.remove("input.txt")

if __name__ == "__main__":
    test_load_text_file()

# Generated at 2022-06-13 21:21:51.369663
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    """
    Test the function process_data_embed_raw_json_file_arg()
    """
    from httpie.cli.argtypes import KeyValueArg
    arg = KeyValueArg(
        'sep',
        'data',
        None,
        '@'
    )
    arg.value = 'tests/data/raw_json.json'
    process_data_embed_raw_json_file_arg(arg)

# Generated at 2022-06-13 21:21:55.202849
# Unit test for function load_text_file
def test_load_text_file():
    keyvaluearg = KeyValueArg("myfile","/home/fz/d/file.txt")
    assert load_text_file(keyvaluearg) == 'www.baidu.com\n'

# Generated at 2022-06-13 21:22:12.093002
# Unit test for function load_text_file
def test_load_text_file():
    c = load_text_file('test.txt')
    print(c)



# Generated at 2022-06-13 21:22:14.319583
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    arg = KeyValueArg('q', '/home/yoyo/test/test.jpg', '=', '@')
    process_file_upload_arg(arg)

# Generated at 2022-06-13 21:22:20.993437
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    import json
    with open('/tmp/test.json','w') as f:
        json.dump({'test':'test'}, f)
    item = KeyValueArg(orig='test',value='/tmp/test.json',sep='=')
    value = process_data_embed_raw_json_file_arg(item)
    print(value)

# Generated at 2022-06-13 21:22:29.443585
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    assert isinstance(process_data_embed_raw_json_file_arg,
                      Callable), "Function is not callable."
    arg = KeyValueArg()
    arg.orig = 'orig'
    arg.key = 'key'
    arg.value = 'value'
    arg.sep = ';'
    # Testing for input type str
    assert isinstance(process_data_embed_raw_json_file_arg(arg),
                      JSONType), "Input of type str failed"
    # Testing for input type int
    arg.value = 123
    # Testing for input type float
    arg.value = 12.3
    assert isinstance(process_data_embed_raw_json_file_arg(arg),
                      JSONType), "Input of type float failed"
    # Testing for input type str and list
    arg.value

# Generated at 2022-06-13 21:22:32.715093
# Unit test for function load_text_file
def test_load_text_file():
    try:
        s = load_text_file("./lex.py")
        print(s)
    except ParseError as e:
        print(e)

test_load_text_file()

# Generated at 2022-06-13 21:22:44.739791
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    content_without_mimetype = process_file_upload_arg(KeyValueArg(
        'upload', "~/Test_photo.jpg"))
    assert isinstance(content_without_mimetype, tuple)
    assert isinstance(content_without_mimetype[2], str)
    assert (content_without_mimetype[2] == 'image/jpeg')

    content_with_mimetype = process_file_upload_arg(KeyValueArg(
        'upload', "~/Test_photo.jpg'application/json"))
    assert isinstance(content_with_mimetype, tuple)
    assert isinstance(content_with_mimetype[2], str)
    assert (content_with_mimetype[2] == 'application/json')

# Generated at 2022-06-13 21:22:56.393234
# Unit test for function load_text_file
def test_load_text_file():
    path = "C:\\Users\\TranTung\\PycharmProjects\\httpie\\httpie\\cli\\args.py"
    try:
        with open(os.path.expanduser(path), 'rb') as f:
            return f.read().decode()
    except IOError as e:
        raise ParseError('"%s": %s' % (item.orig, e))
    except UnicodeDecodeError:
        raise ParseError(
            '"%s": cannot embed the content of "%s",'
            ' not a UTF8 or ASCII-encoded text file'
            % (item.orig, item.value)
        )

test_load_text_file()

# Generated at 2022-06-13 21:23:00.303899
# Unit test for function load_text_file
def test_load_text_file():
    try:
        path = "test-data/test_data_string.txt"
        print('test_load_text_file: '+load_text_file(path))
    except ParseError as e:
        print('test_load_text_file: exception: '+str(e))
        

# Generated at 2022-06-13 21:23:07.945203
# Unit test for function load_text_file
def test_load_text_file():
    # Test case 1: use file which is not json, but is text
    try:
        value = load_text_file(KeyValueArg(key="", sep="", value="common/test_files/data/key-values.txt"))
        assert '1\tOne\n' in value
        assert '2\tTwo\n' in value
        assert '3\tThree\n' in value
    except ParseError as e:
        assert False

    # Test case 2: use file which is not text
    try:
        value = load_text_file(KeyValueArg(key="", sep="", value="common/test_files/data/numbers.json"))
        assert False
    except ParseError:
        assert True

    # Test case 3: use a text file but not utf-8 encoded

# Generated at 2022-06-13 21:23:15.274397
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    arg = KeyValueArg(key='test', sep=SEPARATOR_FILE_UPLOAD, value='test_file.abcd')
    process_file_upload_arg(arg)

    # TODO: find a better way to handle this test with exception
    # arg = KeyValueArg(key='test', sep=SEPARATOR_FILE_UPLOAD, value='test_file.abcd')
    # try:
    #     process_file_upload_arg(arg)
    # except ParseError:
    #     pass

# Generated at 2022-06-13 21:24:08.777675
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    from httpie.cli.dicts import (
    RequestHeadersDict, RequestDataDict, RequestFilesDict, RequestQueryParamsDict, RequestJSONDataDict,
    MultipartRequestDataDict,
    )
    from httpie.cli.argtypes import KeyValueArg

# Generated at 2022-06-13 21:24:12.258784
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    arg = KeyValueArg('data', ':', '~/data.json', '')
    result = process_data_embed_raw_json_file_arg(arg)
    assert type(result) == dict

# Generated at 2022-06-13 21:24:18.436169
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    filename, f, mime_type = process_file_upload_arg(
        KeyValueArg(key=None, sep=SEPARATOR_FILE_UPLOAD, orig='test.txt', value='test.txt')
    )
    assert filename == 'test.txt'
    assert mime_type == 'text/plain'
    f.close()

# Generated at 2022-06-13 21:24:23.444883
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    arg = KeyValueArg("@","/home/harshad/Downloads/Python/httpie-partial-json-output/tests/file.json")
    print(process_data_embed_raw_json_file_arg(arg))

# Generated at 2022-06-13 21:24:26.663444
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    arg = KeyValueArg(key='test', value='test.txt', sep=SEPARATOR_FILE_UPLOAD)
    assert(process_file_upload_arg(arg)[0] == 'test.txt')

# Generated at 2022-06-13 21:24:32.183704
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    input_file = open('data.txt', 'w')
    input_file.write('{"hello": "world"}')
    input_file.close()
    arg = KeyValueArg('data.txt#@', 'data.txt', '#@')
    assert load_json(arg, '{"hello": "world"}') == {'hello': 'world'}


# Generated at 2022-06-13 21:24:35.381808
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    try:
        process_file_upload_arg(KeyValueArg('', '', 'filename.txt'))
    except ParseError:
        assert True
    else:
        assert False


# Generated at 2022-06-13 21:24:42.527541
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    # Test 1
    arg = KeyValueArg('', '', '', 'text.txt', '')
    result = process_file_upload_arg(arg)
    assert result == ('text.txt', 'text.txt', 'text/plain')
    # Test 2
    arg = KeyValueArg('', '', '', 'text.txt;application/json', '')
    result = process_file_upload_arg(arg)
    assert result == ('text.txt', 'text.txt', 'application/json')

# Generated at 2022-06-13 21:24:52.992253
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    text = process_file_upload_arg(KeyValueArg(
        key=b'', value=b'/path/file.txt', sep=b'@', orig=b'@/path/file.txt'))
    assert text == ('file.txt', open('/path/file.txt', 'rb'), 'text/plain')

    text = process_file_upload_arg(KeyValueArg(
        key=b'', value=b'/path/file.txt;text/html', sep=b'@',
        orig=b'@/path/file.txt;text/html'))
    assert text == ('file.txt', open('/path/file.txt', 'rb'), 'text/html')

# Generated at 2022-06-13 21:24:57.212303
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    class TestArg:
        orig: str
        value: str

    item = TestArg()
    item.orig = "test data"
    item.value = "filename.json"
    assert process_data_embed_raw_json_file_arg(item) == {}


# Generated at 2022-06-13 21:25:31.342045
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    arg = KeyValueArg(
        'Data_embed_raw_json_file',
        '',
        '',
        False,
        False,
        '',
        '',
        '',
        ''
    )
    assert process_data_embed_raw_json_file_arg(arg) == ''

# Generated at 2022-06-13 21:25:38.240446
# Unit test for function load_text_file
def test_load_text_file():
    item = KeyValueArg(
        key='name',
        value='./test_load_text_file.txt',
        sep=SEPARATOR_DATA_EMBED_FILE_CONTENTS
    )
    contents = load_text_file(item)
    assert contents == 'foo'


# Generated at 2022-06-13 21:25:39.048905
# Unit test for function load_text_file
def test_load_text_file():
    print(load_text_file(KeyValueArg(key='name', sep=':')))

# Generated at 2022-06-13 21:25:40.528987
# Unit test for function load_text_file
def test_load_text_file():
    assert load_text_file("dummy.txt") == True


# Generated at 2022-06-13 21:25:45.828188
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    """Example file in tests/fixtures/files/data.json
    """
    arg = KeyValueArg('key', 'value', ';@')
    # Value key which is a path to a file
    value = load_text_file(arg)
    result = load_json(arg, value)

    assert result['employee'] == {
        'name': 'John',
        'salary': 2000,
        'married': True
    }



# Generated at 2022-06-13 21:25:55.236190
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    data = {'bat': 'man'}
    req = RequestItems()
    req.data.update(data)
    req.params.update(data)
    req.files.update({'bat': 'man'})
    req.multipart_data.update({'bat': 'man'})
    req.headers.update({'bat': 'man'})

    req_arg = KeyValueArg(
        key=None,
        value='{"bat": "man"}',
        sep=SEPARATOR_DATA_EMBED_RAW_JSON_FILE,
        orig='$json'
    )
    print(process_data_embed_raw_json_file_arg(req_arg))
    print(req.data)
    print(req.params)
    print(req.files)

# Generated at 2022-06-13 21:25:57.076797
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    file_upload_arg = KeyValueArg('test.jpg', SEPARATOR_FILE_UPLOAD)
    assert process_file_upload_arg(file_upload_arg) == ('test.jpg', 'rb', 'image/jpeg')



# Generated at 2022-06-13 21:26:03.680069
# Unit test for function load_text_file
def test_load_text_file():
    data = '''
---
- url: http://www.github.com
  method: GET
  header:
      content-type: application/json
  multipart_data:
      content-type: image/png
'''
    request_item_args = RequestItems.from_args(
        [arg for arg in KeyValueArg.parse(data)],
        as_form=True,
    )
    print(request_item_args.multipart_data)

# Generated at 2022-06-13 21:26:12.393245
# Unit test for function load_text_file
def test_load_text_file():
    request_item_args = [
        KeyValueArg(
            'file',
            './file_load_text',
            '@',
        )
    ]
    item = request_item_args[0]
    path = item.value
    try:
        with open(os.path.expanduser(path), 'rb') as f:
            return f.read().decode()
    except IOError as e:
        raise ParseError('"%s": %s' % (item.orig, e))
    except UnicodeDecodeError:
        raise ParseError(
            '"%s": cannot embed the content of "%s",'
            ' not a UTF8 or ASCII-encoded text file'
            % (item.orig, item.value)
        )

# Generated at 2022-06-13 21:26:16.157365
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    # Arrange
    arg = KeyValueArg('sep', 'key', 'value')
    # Act
    result = process_file_upload_arg(arg)
    # Assert
    # TODO: Write a better test
    assert result is not None

# Generated at 2022-06-13 21:27:09.513987
# Unit test for function load_text_file
def test_load_text_file():
    assert load_text_file('test.txt') == 'test'


# Generated at 2022-06-13 21:27:17.949697
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    class KeyValueArg_test:
        def __init__(self, orig, value):
            self.orig = orig
            self.value = value
            self.sep = SEPARATOR_DATA_EMBED_RAW_JSON_FILE

    kva = KeyValueArg_test("'@'", '"/Users/cgj/Documents/httpie-1.0.2/examples/test.json"')
    print("keyValueArg: ", kva.orig, kva.value, kva.sep)
    res = process_data_embed_raw_json_file_arg(kva)
    print("res: ", res)
    print("res_type: ", type(res))



# Generated at 2022-06-13 21:27:26.789764
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    arg = KeyValueArg(
            key=None,
            sep=None,
            orig=None,
            value=None
    )
    arg.sep = SEPARATOR_DATA_EMBED_RAW_JSON_FILE
    arg.value = 'json'
    instance = load_json(arg, '{"foo": "bar"}')
    assert isinstance(instance, dict) is True
    assert instance.get("foo") == "bar"
    arg.value = 'json'
    instance = load_json(arg, '["foo", "bar"]')
    assert isinstance(instance, list) is True
    assert instance[0] == "foo"
    arg.value = 'json'
    instance = load_json(arg, '[{"foo": "bar"}]')
    assert isinstance(instance, list) is True
   

# Generated at 2022-06-13 21:27:28.799595
# Unit test for function load_text_file
def test_load_text_file():
    assert load_text_file(KeyValueArg('h', 'testdata/hello')) == 'hello, world!'
    try:
        load_text_file(KeyValueArg('h', 'testdata/binary'))
    except ParseError as e:
        pass


# Generated at 2022-06-13 21:27:35.301342
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    arg = KeyValueArg(key=None, sep=SEPARATOR_DATA_EMBED_RAW_JSON_FILE, value="~/Desktop/blah.json", orig=None)
    result = process_data_embed_raw_json_file_arg(arg)
    print(result)


# Generated at 2022-06-13 21:27:41.961029
# Unit test for function load_text_file
def test_load_text_file():
    f = open("test_request_item.txt", 'w')
    f.write("Hello World")
    f.close()

    f = open("test_request_item.txt", 'r')
    rf = RequestItems.load_text_file(f.read())
    assert rf == "Hello World"


if __name__ == "__main__":
    test_load_text_file()

# Generated at 2022-06-13 21:27:50.886966
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    arg = KeyValueArg(orig='@users.json', key='file', value='users.json', sep='@', index=0)
    # file users.json not exits
    assert process_data_embed_raw_json_file_arg(arg) == None

# Generated at 2022-06-13 21:27:54.423572
# Unit test for function load_text_file
def test_load_text_file():
    file = load_text_file('fruits.txt')
    assert type(file) is str
    assert file == 'apple\norange\ntomato\n'


# Generated at 2022-06-13 21:28:02.722743
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    import os
    from httpie.cli.argtypes import KeyValueArg
    from httpie.cli.dicts import RequestJSONDataDict
    from httpie.cli.items import process_data_embed_raw_json_file_arg

    data = (
        '[{"username": "user1", "password": "pwd1"}, '
        '{"username": "user2", "password": "pwd2"}]'
    )
    fd, path = tempfile.mkstemp()

# Generated at 2022-06-13 21:28:04.837691
# Unit test for function load_text_file
def test_load_text_file():
    filename = "README.rst"
    contents = load_text_file(filename)
    assert contents != None