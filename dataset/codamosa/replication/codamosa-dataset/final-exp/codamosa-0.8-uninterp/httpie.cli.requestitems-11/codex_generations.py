

# Generated at 2022-06-13 21:19:25.257789
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    print(load_json(KeyValueArg(
        'name',
        '',
        'file',
        'value'
    ), '{ "name": "asdf" }'))

# Generated at 2022-06-13 21:19:26.691786
# Unit test for function load_text_file
def test_load_text_file():
    assert load_text_file('hello') == 'hello'

# Generated at 2022-06-13 21:19:34.179428
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    arg = KeyValueArg("filename.txt", "-f,", "filename.txt")
    assert process_file_upload_arg(arg) == ("filename.txt", "filename.txt", None)
    arg = KeyValueArg("filename.txt,text/plain", "-f,", "filename.txt,text/plain")
    assert process_file_upload_arg(arg) == ("filename.txt", "filename.txt", "text/plain")



# Generated at 2022-06-13 21:19:38.994019
# Unit test for function process_data_raw_json_embed_arg
def test_process_data_raw_json_embed_arg():
    json_string = '{"a": "b"}'
    arg = KeyValueArg(sep='=', key=None, value=json_string)
    json_dict_obj = process_data_raw_json_embed_arg(arg)
    assert json_dict_obj["a"] == "b"


# Generated at 2022-06-13 21:19:45.690915
# Unit test for function load_text_file
def test_load_text_file():
    if not os.path.isfile("load_text_file_test.txt"):
        f= open("load_text_file_test.txt","w+")
        f.write("Hello World")
        f.close()
    load_text_file("load_text_file_test.txt")
    os.remove("load_test_file.txt")

# Generated at 2022-06-13 21:19:53.219117
# Unit test for function process_data_raw_json_embed_arg
def test_process_data_raw_json_embed_arg():
    arg = KeyValueArg('','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','')
    arg.key = 'x'
    arg.value = '[1,2]'
    arg.orig = 'x=[1,2]'
    arg.sep = ':'
    arg.orig_sep = ':'
    arg.value_sep = '='
    assert process_data_raw_json_embed_arg(arg) == [1,2]
    arg.key = 'x'
    arg.value = '{"x":1}'

# Generated at 2022-06-13 21:20:04.748239
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    import json
    test_data = {'key': 'value'}
    # save test_data to tmp_file
    tmp_file = open('tmp_file', 'w')
    json.dump(test_data, tmp_file)
    tmp_file.close()
    arg = KeyValueArg(KeyValueArg._make(('data', '@tmp_file', '', '=', '')))
    loaded_data = process_data_embed_raw_json_file_arg(arg)
    print(loaded_data)
    assert loaded_data == test_data
    os.system('rm tmp_file')

# Generated at 2022-06-13 21:20:15.281849
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    a = KeyValueArg("filename.txt;image/jpeg")
    a.value = "filename.txt;image/jpeg"
    a.sep = "="

    b = KeyValueArg("filename.txt")
    b.value = "filename.txt"
    b.sep = "="

    # Test case when mime type is provided
    filename, file_content, mime_type = process_file_upload_arg(a)
    assert filename == "filename.txt"
    assert mime_type == "image/jpeg"
    #Test case when mime type is not provided
    filename, file_content, mime_type =  process_file_upload_arg(b)
    assert filename == "filename.txt"
    assert mime_type == "text/plain; charset=us-ascii"

# Generated at 2022-06-13 21:20:17.616830
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    arg = KeyValueArg(key='', sep=':', orig='', value='')
    assert process_data_embed_raw_json_file_arg(arg) == None

# Generated at 2022-06-13 21:20:25.812430
# Unit test for function load_text_file
def test_load_text_file():
    file_path = "httpie/cli/test.txt"
    test_item = KeyValueArg(
        orig=file_path,
        sep=SEPARATOR_DATA_EMBED_FILE_CONTENTS,
        key='test_file',
        value=file_path
    )
    test_text = load_text_file(test_item)
    assert test_text == 'test text'

# Generated at 2022-06-13 21:20:35.795141
# Unit test for function load_text_file
def test_load_text_file():
    with pytest.raises(ParseError):
        load_text_file('/tmp/test.txt')

# Generated at 2022-06-13 21:20:43.302333
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    path = 'unit_test/httpie_file_test.json'
    item = KeyValueArg('a', '@', path, None)
    expect_result = {
        "code": 200,
        "error_code": 0,
        "message": "success",
        "data": {
            "name": "meow",
            "age": 2,
            "diseases": ["dalmatian", "lion", "tiger"],
            "meow": {"meow": "meow", "meow meow": "meow meow"}
        },
        "error_message": ""
    }
    assert expect_result == process_data_embed_raw_json_file_arg(item)


# Generated at 2022-06-13 21:20:44.918415
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    arg = KeyValueArg("label@path/to/file.json")
    assert isinstance(process_data_embed_raw_json_file_arg(arg), dict)


# Generated at 2022-06-13 21:20:49.345791
# Unit test for function load_text_file
def test_load_text_file():
    import tempfile
    path = tempfile.mktemp()
    text = "Foo"
    with open(path,'w') as f:
        f.write(text)
    f.closed
    assert load_text_file(KeyValueArg(key=None,sep='',value=path,orig=path)) == text
    print(path)

# Generated at 2022-06-13 21:20:52.447371
# Unit test for function load_text_file
def test_load_text_file():
    item = KeyValueArg('test.txt', '-O', 'test.txt')
    assert(load_text_file(item) == 'Hello world!')


# Generated at 2022-06-13 21:20:56.185402
# Unit test for function load_text_file
def test_load_text_file():
    item = KeyValueArg('a', 'b', SEPARATOR_DATA_EMBED_FILE_CONTENTS)
    assert load_text_file(item) == 'b'

# Generated at 2022-06-13 21:20:59.692568
# Unit test for function load_text_file
def test_load_text_file():
    item = KeyValueArg(orig = "textfile", sep = "=", key = "", value = "./test_load_text_file.txt")
    contents = load_text_file(item)
    print(contents)


# Generated at 2022-06-13 21:21:01.661289
# Unit test for function load_text_file
def test_load_text_file():
    arg = KeyValueArg("test_header", "test_value", "test_orig")
    assert load_text_file(arg) == "test_value"

# Generated at 2022-06-13 21:21:09.535782
# Unit test for function load_text_file
def test_load_text_file():

    with open(os.path.expanduser('~/Desktop/temp.txt'), 'a') as file:
        file.write('This is a test')
    keyValueArg = KeyValueArg(value=os.path.expanduser('~/Desktop/temp.txt'))
    x = load_text_file(keyValueArg)
    print(x)
    os.remove(os.path.expanduser('~/Desktop/temp.txt'))

# Generated at 2022-06-13 21:21:22.152902
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    test_file_path = 'C:\\httpie\\test_process_data_embed_raw_json_file_arg.json'
    test_KeyValueArg = KeyValueArg('key_name', 'test')
    t = RequestItems()
    if os.path.exists(test_file_path):
        os.remove(test_file_path)
    test_file = open(test_file_path, 'x')
    test_file.write('{"name": "test_name", "age": 0, "gender": "male"}')
    test_file.close()
    print(t.process_data_embed_raw_json_file_arg(test_KeyValueArg))
    if os.path.exists(test_file_path):
        os.remove(test_file_path)


# Generated at 2022-06-13 21:21:41.320376
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    # Test for basic usage
    filename = "https://httpbin.org/get"
    mime_type = "Test"
    test_arg1 = KeyValueArg(name="", key=SEPARATOR_FILE_UPLOAD,
                            value=filename + SEPARATOR_FILE_UPLOAD_TYPE + mime_type + ";", orig="", sep="", type=None)
    assert process_file_upload_arg(test_arg1) == ("get", "", "Test")
    # Test for empty filename usage
    filename = ""
    test_arg2 = KeyValueArg(name="", key=SEPARATOR_FILE_UPLOAD, value=filename, orig="", sep="", type=None)
    assert process_file_upload_arg(test_arg2) == ("", "", "")
    # Test for

# Generated at 2022-06-13 21:21:49.466351
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    full_path = os.getcwd() + "/testFile.json"
    full_path_1 = os.getcwd() + "/testFile1.json"
    arg = KeyValueArg("testKey","@" + full_path)
    arg1 = KeyValueArg("testKey", "@" + full_path_1)
    assert process_data_embed_raw_json_file_arg(arg) == {"testKey":"testValue"}
    assert process_data_embed_raw_json_file_arg(arg1) == {"testKey1":"testValue1"}

# Generated at 2022-06-13 21:21:53.369877
# Unit test for function load_text_file
def test_load_text_file():
    item = KeyValueArg("data-binary", "xueqiao.txt")
    file_data = load_text_file(item)
    print(file_data)
    
test_load_text_file()


# Generated at 2022-06-13 21:22:05.456425
# Unit test for function process_data_raw_json_embed_arg
def test_process_data_raw_json_embed_arg():
    test_item = KeyValueArg(key=None, sep="=", value="q=httpie&foo=bar", orig="q=httpie&foo=bar")
    assert process_data_raw_json_embed_arg(test_item) == {"q": "httpie", "foo": "bar"}
    test_item = KeyValueArg(key=None, sep="=", value="{}", orig="{}")
    assert process_data_raw_json_embed_arg(test_item) == {}
    test_item = KeyValueArg(key=None, sep="=", value='{"q":"httpie","foo":"bar"}', orig='{"q":"httpie","foo":"bar"}')
    assert process_data_raw_json_embed_arg(test_item) == {"q": "httpie", "foo": "bar"}


# Generated at 2022-06-13 21:22:07.792997
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    arg = KeyValueArg(key='foo', sep='@', value='file.txt')
    f, mime = process_file_upload_arg(arg)
    print(f)
    print(mime)


if __name__ == '__main__':
    test_process_file_upload_arg()

# Generated at 2022-06-13 21:22:13.927914
# Unit test for function process_data_raw_json_embed_arg
def test_process_data_raw_json_embed_arg():
    arg = KeyValueArg(sep="-d", key="abcd", value="{\"abc\":[1,2,3]}")
    value = process_data_raw_json_embed_arg(arg)
    assert(value == {"abc":[1,2,3]})
if __name__ == "__main__":
    test_process_data_raw_json_embed_arg()

# Generated at 2022-06-13 21:22:18.686113
# Unit test for function load_text_file
def test_load_text_file():
    my_path = "my_path"
    my_orig = "my_orig"
    assert load_text_file(KeyValueArg(key=None, value=my_path, sep=None, orig=my_orig)) == my_path

# Generated at 2022-06-13 21:22:28.323518
# Unit test for function process_data_raw_json_embed_arg

# Generated at 2022-06-13 21:22:30.977630
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    try:
        process_file_upload_arg(KeyValueArg('a', 'b'))
    except ParseError:
        pass
    f = 'C:\\Users\\yicheng\\Desktop\\test.txt'
    assert process_file_upload_arg(KeyValueArg('a', f)) == ('test.txt', open(f, 'rb'), 'text/plain')

# Generated at 2022-06-13 21:22:41.535929
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    from httpie.cli.argtypes import KeyValueArg
    from httpie.cli.dicts import RequestDataDict, RequestJSONDataDict, RequestFilesDict
    class MockRequestItems(KeyValueArg):
        def __init__(self):
            self.headers = RequestJSONDataDict()
            self.data = RequestJSONDataDict()
            self.files = RequestFilesDict()
            self.params = RequestDataDict()
            self.multipart_data = RequestDataDict()

        @classmethod
        def from_args(
            cls,
            request_item_args: List[KeyValueArg],
            as_form=False,
        ) -> 'RequestItems':
            instance = cls()

# Generated at 2022-06-13 21:23:15.670115
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    path = "../httpie/tests/data/keyvals.json"
    item = KeyValueArg('--data', '@' + path)
    # Call assert if not working inside a test case
    data = process_data_embed_raw_json_file_arg(item)
    assert len(data) == 1
    assert data['key'] == 'value'
    path = "../httpie/tests/data/empty-object.json"
    item = KeyValueArg('--data', '@' + path)
    # Call assert if not working inside a test case
    data = process_data_embed_raw_json_file_arg(item)
    assert len(data) == 0

# TODO add more test cases, like file that does exist but cannot be read

# Generated at 2022-06-13 21:23:21.311546
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    input_file_path = os.path.abspath(os.path.dirname(__file__)+'/../test_data/request_items.json')
    f = open(input_file_path, 'r')
    contents = f.read()
    kv = KeyValueArg()
    kv.value = contents
    data = process_data_embed_raw_json_file_arg(kv)
    print(data)


# Generated at 2022-06-13 21:23:28.052091
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    arg = KeyValueArg("@b.txt", "b.txt", "@", "b.txt", "")
    #print("test_process_file_upload_arg:", process_file_upload_arg(arg))

    arg = KeyValueArg("@b.txt;type=.xlsx", "b.txt", "@", "b.txt", "type=.xlsx")
    #print("test_process_file_upload_arg:", process_file_upload_arg(arg))



# Generated at 2022-06-13 21:23:31.095242
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    print(process_file_upload_arg(KeyValueArg(key="", sep="@@", value="./file.txt")))

# Generated at 2022-06-13 21:23:36.534566
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    value = process_data_embed_raw_json_file_arg('["tomorrow", "today", "yesterday"]')
    print(value)
    print(type(value))
    print(len(value))


# Generated at 2022-06-13 21:23:42.368525
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    from httpie.cli import args
    from httpie.cli.parser import parse_items
    request_items = parse_items([
        args.KeyValueArg(None, 'user', 'json', '{"username": "x"}')
    ])
    assert request_items.data == {"user": {"username": "x"}}

# Generated at 2022-06-13 21:23:51.308011
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    # test original valid.json file from original test
    item = KeyValueArg(sep=SEPARATOR_DATA_EMBED_RAW_JSON_FILE,
                       key=None,
                       value='~/.httpie/tests/data_files/valid.json')
    test_valid = process_data_embed_raw_json_file_arg(item)
    # test original valid.json file from new unit test
    test_file = open('data_files/valid.json', 'r')
    expected_valid = test_file.read()
    test_file.close()
    assert(test_valid == json.loads(expected_valid))



# Generated at 2022-06-13 21:23:55.453853
# Unit test for function load_text_file
def test_load_text_file():
    test_arg = KeyValueArg("-d","abc.txt")
    expected = "123"
    actual = load_text_file(test_arg)
    assert(expected == actual)
    

# Generated at 2022-06-13 21:23:59.839301
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    arg = KeyValueArg('', '', None, 'data@a.json')
    json_dic = load_json(arg, '{"a":1,"b":3,"c":4}')
    assert json_dic['a'] == 1
    assert json_dic['b'] == 3
    assert json_dic['c'] == 4

# Generated at 2022-06-13 21:24:03.820605
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    filename = 'foo.txt'
    mime_type = 'text/plain'
    try:
        f = open(os.path.expanduser(filename), 'rb')
    except IOError as e:
        raise ParseError('"%s": %s' % (filename, e))
    return (
        os.path.basename(filename),
        f,
        mime_type or get_content_type(filename),
    )


# Generated at 2022-06-13 21:24:48.210266
# Unit test for function load_text_file
def test_load_text_file():
    # Arrange
    dummy_text_file_name = 'afile.txt'
    contents = "somestring"
    dummy_item = KeyValueArg("item", dummy_text_file_name, ";")

    # Act
    with patch("builtins.open", mock_open(read_data=contents)) as m:
        result = load_text_file(dummy_item)

    # Assert
    assert result == contents
    assert m.called

# Generated at 2022-06-13 21:24:53.554545
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    f = process_file_upload_arg(KeyValueArg('test', 'test.json'))
    assert(f[0] == 'test.json')
    assert(f[2] == 'application/json')
    assert(f[1].closed == False)
    f[1].close()

# Generated at 2022-06-13 21:24:59.777532
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    # Only test the functionality of the function (no exception is thrown)
    process_data_embed_raw_json_file_arg(None)
    process_data_embed_raw_json_file_arg(None)
    process_data_embed_raw_json_file_arg(None)
    process_data_embed_raw_json_file_arg(None)
    process_data_embed_raw_json_file_arg(None)

# Generated at 2022-06-13 21:25:08.220064
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    # Input
    test_arg = KeyValueArg("file=report.xlsx","file",SEPARATOR_FILE_UPLOAD,"report.xlsx")

    # Expected output
    expected_return = ('report.xlsx',open('report.xlsx', 'rb'),get_content_type('report.xlsx'))

    # Unit test
    assert expected_return == process_file_upload_arg(test_arg)

    # Cleanup
    os.remove("report.xlsx")


# Generated at 2022-06-13 21:25:16.410313
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg(): 
    arg1 = KeyValueArg(key=None, value=None, sep=':', orig='order_id:2')
    arg2 = KeyValueArg(key=None, value=None, sep='@', orig='order_id:2')
    result = process_data_embed_raw_json_file_arg(arg1)
    print(result)
    result = process_data_embed_raw_json_file_arg(arg2)
    print(result)
    assert result == 'order_id'


# Generated at 2022-06-13 21:25:27.202725
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    json_file_path = "test_json_file.json"
    key = '"key"'
    json_value = '"value"'
    json_value_with_quotes = '"\"quoted value\""'
    json_int_value = "123"
    json_boolean_value = "true"
    json_list_value = "[\"list1\",\"list2\"]"

    # create the test file
    f = open(json_file_path, 'w')
    f.write("{" + key + ":" + json_value + "}")
    f.close()

    # do the test
    value = process_data_embed_raw_json_file_arg(KeyValueArg(key, json_file_path, SEPARATOR_DATA_EMBED_RAW_JSON_FILE))

# Generated at 2022-06-13 21:25:36.601047
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    file_item_arg_1=KeyValueArg('Content-Disposition','form-data; name="userfile"; filename="test.txt"')
    file_item_arg_2 = KeyValueArg('Content-Disposition', 'form-data; name="userfile"; filename="test.txt"; type="text/html"')

    try:
        items= process_file_upload_arg(file_item_arg_1)
    except ParseError:
        print('error')

    print('{0},{1},{2}'.format(items[0],items[1],items[2]))

    try:
        items = process_file_upload_arg(file_item_arg_2)
    except ParseError:
        print('error')


# Generated at 2022-06-13 21:25:42.865347
# Unit test for function load_text_file
def test_load_text_file():
    try:
        f = open(os.path.expanduser('c:\\httpie\\http\\request.py'), 'rb')
    except IOError as e:
        raise ParseError('"%s": %s' % (str(), e))
    return f.read().decode()


if __name__ == '__main__':
    print(test_load_text_file())

# Generated at 2022-06-13 21:25:51.258419
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    arg = KeyValueArg(key=None, sep="=", orig="filename", value="filename")
    filename, f, mime_type = process_file_upload_arg(arg)
    assert filename == "filename"
    assert mime_type == None
    arg = KeyValueArg(key=None, sep="=", orig="filename;content-type", value="filename;content-type")
    filename, f, mime_type = process_file_upload_arg(arg)
    assert filename == "filename"
    assert mime_type == "content-type"

# Generated at 2022-06-13 21:26:04.353833
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    arg = KeyValueArg(
        orig="test_file@test_data/test.txt",
        key="test_file",
        sep=SEPARATOR_FILE_UPLOAD,
        value="test_data/test.txt",
    )
    assert process_file_upload_arg(arg) == (
        "test.txt",
        open("./test_data/test.txt", "rb"),
        "text/plain"
    )

    arg = KeyValueArg(
        orig="test_file@test_data/test.txt;text/plain",
        key="test_file",
        sep=SEPARATOR_FILE_UPLOAD,
        value="test_data/test.txt;text/plain",
    )

# Generated at 2022-06-13 21:26:37.538293
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    # Test csv data file
    item = process_file_upload_arg(KeyValueArg(
        sep=SEPARATOR_FILE_UPLOAD,
        key='csv',
        value='test_data/csv_test_data.csv',
        orig='test_data/csv_test_data.csv:test_data/csv_test_data.csv'))
    assert item[0] == 'csv_test_data.csv'
    assert item[1].__class__.__name__ == 'FileIO'
    assert item[2] == 'text/csv'

    # Test excel data file

# Generated at 2022-06-13 21:26:44.650370
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    test_file_name = 'test_file.json'
    test_file_path = './tests/test_files/test_file.json'
    with open(test_file_path,'rt') as f:
        line = f.readline()
        expected = json.loads(line)
    assert expected == process_data_embed_raw_json_file_arg(KeyValueArg(test_file_name,test_file_path))

# Generated at 2022-06-13 21:26:49.792083
# Unit test for function load_text_file
def test_load_text_file():
        assert(load_text_file("abc.TXT") == "abc.TXT\n")
        assert(load_text_file("abc.txt") == "abc.txt\n")
        assert(load_text_file("ab.txt") == "ab.txt\n")
        assert(load_text_file("a.txt") == "a.txt\n")


# Generated at 2022-06-13 21:26:53.692099
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    assert process_data_embed_raw_json_file_arg(KeyValueArg("a", "b", "a:<b")) == "b"

# Generated at 2022-06-13 21:26:58.840970
# Unit test for function load_text_file
def test_load_text_file():
    path = "./httpie/cli/argtypes.py"
    contents = load_text_file(KeyValueArg("name", "value"))
    assert contents[:10] == "#!/usr/bin"

# Generated at 2022-06-13 21:27:07.967613
# Unit test for function load_text_file
def test_load_text_file():
    with open('http.txt', 'w') as f:
        f.write('hello world')
    parser = argparse.ArgumentParser()
    parser.add_argument('--request-items', type=KeyValueArg, action='append')
    args = parser.parse_args(['--request-items', '@http.txt'])
    print(args.request_items)
    assert process_data_item_arg(args.request_items[0]) == 'hello world'
    os.remove('http.txt')


if __name__ == '__main__':
    test_load_text_file()

# Generated at 2022-06-13 21:27:15.747520
# Unit test for function load_text_file
def test_load_text_file():
    def mockopen(value, f):
        return True

    text = 'foo'
    with patch('httpie.cli.argtypes.open', new=mockopen) as mo:
        assert process_data_item_arg(KeyValueArg('', ':', 'foo')) == text
        assert process_data_embed_file_contents_arg(KeyValueArg('', '~~', 'foo')) == text
        assert process_data_raw_json_embed_arg(KeyValueArg('', '=', 'foo')) == text



# Generated at 2022-06-13 21:27:25.557692
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    # pylint: disable=unused-variable
    arg1 = KeyValueArg('key=@test/test_data/test.json', 'key', '=@test/test_data/test.json', '@test/test_data/test.json', '=')
    arg2 = KeyValueArg('key=@test/test_data/rawjson.json', 'key', '=@test/test_data/rawjson.json', '@test/test_data/rawjson.json', '=')
    result1 = process_data_embed_raw_json_file_arg(arg1)
    result2 = process_data_embed_raw_json_file_arg(arg2)
    assert result1 == {'a': 1, 'b': {'c': 'd'}}

# Generated at 2022-06-13 21:27:31.699290
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    file_path = "test.json"
    target_json = {}
    with open(os.path.expanduser(file_path), 'r') as file:
        target_json = json.loads(file.read())
    arg = KeyValueArg(key=None, sep=None, orig=None, value=file_path)
    print(process_data_embed_raw_json_file_arg(arg) == target_json)


# Generated at 2022-06-13 21:27:43.658661
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    from httpie.cli.argtypes import KeyValueArg
    arg = KeyValueArg(sep=SEPARATOR_FILE_UPLOAD,
                      key='file',
                      orig='file@~/test.txt',
                      value='~/test.txt')
    assert process_file_upload_arg(arg)[0] == 'test.txt'
    assert process_file_upload_arg(arg)[2] == 'text/plain'
    arg = KeyValueArg(sep=SEPARATOR_FILE_UPLOAD,
                      key='file',
                      orig='file@~/test.txt:image/jpeg',
                      value='~/test.txt:image/jpeg')
    assert process_file_upload_arg(arg)[2] == 'image/jpeg'

# Generated at 2022-06-13 21:28:47.968985
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    from httpie.cli.argtypes import KeyValueArg

    arg = KeyValueArg(
        orig='filename.jpg' + SEPARATOR_FILE_UPLOAD + 'image/jpeg',
        sep=SEPARATOR_FILE_UPLOAD,
        key='filename.jpg',
        value='image/jpeg')

    assert process_file_upload_arg(arg) == ('filename.jpg', open(os.path.expanduser(arg.value)), 'image/jpeg')

# Generated at 2022-06-13 21:28:54.701138
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    import json
    # test paraemter passing
    value = process_data_embed_raw_json_file_arg(KeyValueArg("test", "test"))
    with open("test.json", 'w') as json_file:
        json.dump({"key": "value"}, json_file)
    value = process_data_embed_raw_json_file_arg(KeyValueArg("test", "test.json"))
    assert value == {"key": "value"}
    return


# Generated at 2022-06-13 21:29:06.662599
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    # Tests for load_json
    arg_sample = KeyValueArg(key=None, value='geojson.json', orig="<PATH>", sep=":")
    contents = load_text_file(arg_sample)
    value = load_json(arg_sample, contents)
    assert(value == {'type': 'Point', 'coordinates': [0, 0]})


# Generated at 2022-06-13 21:29:08.870403
# Unit test for function load_text_file
def test_load_text_file():
    item = KeyValueArg('label', '1.txt', None)
    contents = load_text_file(item)
    print(contents)

# Generated at 2022-06-13 21:29:14.893959
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    arg1 = '--form file@~/Desktop/myfile.txt'
    arg2 = '--form file@~/myfile.txt;text/plain'
    arg3 = '--form file@~/myfile.txt;'
    arg4 = '--form file@~/myfile.txt'

    assert process_file_upload_arg(arg1) == ('myfile.txt', "/Users/dip/Desktop/myfile.txt", 'text/plain')
    assert process_file_upload_arg(arg2) == ('myfile.txt', "/Users/dip/myfile.txt", 'text/plain')
    assert process_file_upload_arg(arg3) == ('myfile.txt', "/Users/dip/myfile.txt", 'text/plain')