

# Generated at 2022-06-13 21:19:38.351958
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    # type: () -> None

    from httpie.cli.argtypes import KeyValueArg
    from httpie.cli.dicts import RequestFilesDict
    from httpie.cli.items import RequestItems, process_file_upload_arg

    def test_process_file_upload_arg(
            # type: () -> None
            arg,  # type: KeyValueArg
            expected_value  # type: Tuple[str, IO, str]
    ):
        # type: (...) -> None
        actual_value = process_file_upload_arg(arg)
        assert actual_value == expected_value

    items = RequestItems()
    filename = os.path.join(os.path.dirname(__file__), '../requests/test/test_files/test.json')

# Generated at 2022-06-13 21:19:41.256772
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    try:
        process_data_embed_raw_json_file_arg("arg.value")
    except ParseError as e:
        return e


# Generated at 2022-06-13 21:19:44.568939
# Unit test for function load_text_file
def test_load_text_file():
    test_arg = KeyValueArg("test", "hi", ":")
    print(load_text_file(test_arg))


# Generated at 2022-06-13 21:19:49.015935
# Unit test for function load_text_file
def test_load_text_file():
    item = KeyValueArg(SEPARATOR_DATA_EMBED_FILE_CONTENTS, 'a', './test_load_text_file.txt')
    result = load_text_file(item)
    expected_result = 'success\n'
    assert result == expected_result


# Generated at 2022-06-13 21:19:53.670380
# Unit test for function load_text_file
def test_load_text_file():
    path = "/Users/yuexinlin/Downloads/hw7/hw7.py"
    item = KeyValueArg('test', path, '%s' %path, None)
    load_text_file(item)
    

# Generated at 2022-06-13 21:20:05.486277
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    data = "test.txt"
    arg = KeyValueArg(None, SEPARATOR_FILE_UPLOAD, "filename", data)
    filename, f, mime_type = process_file_upload_arg(arg)
    import pdb; pdb.set_trace()
    assert filename == "test.txt"
    assert f is not None
    assert mime_type == "text/plain"

    data = "test.txt; image/jpg"
    arg = KeyValueArg(None, SEPARATOR_FILE_UPLOAD, "filename", data)
    filename, f, mime_type = process_file_upload_arg(arg)
    assert filename == "test.txt"
    assert f is not None
    assert mime_type == "image/jpg"

# Generated at 2022-06-13 21:20:11.382789
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    path = 'test_data.json'
    item = KeyValueArg(None, '@' + path, '', '')
    assert process_data_embed_raw_json_file_arg(item) == {'1': '1', '2': '2', '3': '3'}

test_process_data_embed_raw_json_file_arg()

# Generated at 2022-06-13 21:20:20.034890
# Unit test for function process_data_raw_json_embed_arg
def test_process_data_raw_json_embed_arg():
    print("Testing function process_data_raw_json_embed_arg")
    test_dict = {"key1": "value1"}

    # request_items.py
    # process_data_embed_raw_json_file_arg(arg: KeyValueArg) -> JSONType:
    # process_data_raw_json_embed_arg(arg: KeyValueArg) -> JSONType:
    # def load_json(arg: KeyValueArg, contents: str) -> JSONType:
    # def load_text_file(item: KeyValueArg) -> str:

    test_arg = KeyValueArg(orig='key1:value1', key='key1', sep=':', value='value1')
    result = process_data_raw_json_embed_arg(test_arg)
    print(result)
    assert result == test_dict


# Generated at 2022-06-13 21:20:22.092805
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    assert process_data_embed_raw_json_file_arg(KeyValueArg("", "", "", "{\"name\": \"value\"}")) == {"name": "value"}

# Generated at 2022-06-13 21:20:29.734965
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg(): 
    testData = ['test_data.json','test_data2.json','test_data3.json','test_data4.json']
    testValues = ['{"hello": "world"}','{"time": "05:00", "temp": "80f"}','{"hello": "world"}','{"temp": "80f", "time": "05:00"}']
    for i in range(0, len(testData)):
        testValue = testValues[i]
        class testArg(object):
            orig = testData[i]
            value = testData[i]
        testDataArg = testArg()
        result = process_data_embed_raw_json_file_arg(testDataArg)
        # print("arg from test_data.json:  %s" % result)

# Generated at 2022-06-13 21:20:39.891563
# Unit test for function load_text_file
def test_load_text_file():
    path = os.path.abspath('../../../requirements.txt')
    item = KeyValueArg('embed-file-contents', '', '', '', '', path)
    content = load_text_file(item)
    # Contents of requirements file is not empty, so
    assert content != ""

# Generated at 2022-06-13 21:20:51.068388
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    import json
    import unittest
    from httpie.cli.argtypes import KeyValueArg

    data: str = '''
    {
        "name": "王小虎",
        "age": 18
    }
    '''
    arg: KeyValueArg = KeyValueArg('name=data.json;')
    arg.value = 'data.json'
    with open('data.json', 'w') as f:
        f.write(data)

    value = process_data_embed_raw_json_file_arg(arg)
    got = json.dumps(value, ensure_ascii=False)
    expect = data
    assert got == expect


if __name__ == "__main__":
    test_process_data_embed_raw_json_file_arg()

# Generated at 2022-06-13 21:21:03.044148
# Unit test for function process_data_raw_json_embed_arg
def test_process_data_raw_json_embed_arg():
    # Simple dict
    assert (process_data_raw_json_embed_arg(KeyValueArg('key', 'val')) == {'key': 'val'})

    # Dict with nested dict
    assert (process_data_raw_json_embed_arg(KeyValueArg('key', '{\"nested\": \"val\"}')) == {'key': {'nested': 'val'}})

    # List containing a tuple
    assert (process_data_raw_json_embed_arg(KeyValueArg('key', '[[1, 2], [3, 4]]')) == {'key': [[1, 2], [3, 4]]})

    # None Type
    assert (process_data_raw_json_embed_arg(KeyValueArg('key', 'null')) == {'key': None})

    # Boolean Type
   

# Generated at 2022-06-13 21:21:14.468418
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    # test filename and mime1
    test_arg = KeyValueArg(
        orig="filename;mime",
        key="filename",
        sep=";",
        value="test.txt;text/plain"
    )
    result = process_file_upload_arg(test_arg)
    assert(result[0] == "test.txt")
    assert(result[1].name == "test.txt")
    assert(result[2] == "text/plain")

    # test filename and mime2
    test_arg = KeyValueArg(
        orig="filename",
        key="filename",
        sep=";",
        value="test.txt"
    )
    result = process_file_upload_arg(test_arg)

    # test mime2
    assert(result[0] == "test.txt")


# Generated at 2022-06-13 21:21:27.551019
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    separator_file_upload_type = ';type='
    def check_func(arg, filename, content_type):
        if arg.value.find(separator_file_upload_type) != -1:
            return process_file_upload_arg(arg)
        else:
            arg.value = arg.value + separator_file_upload_type + content_type
            return process_file_upload_arg(arg)

    def check_func_no_type(arg, filename):
        if arg.value.find(separator_file_upload_type) != -1:
            return process_file_upload_arg(arg)
        else:
            arg.value = arg.value + separator_file_upload_type
            return process_file_upload_arg(arg)


# Generated at 2022-06-13 21:21:31.655310
# Unit test for function load_text_file
def test_load_text_file():
   try:
       obj = load_text_file(KeyValueArg("name", "httpie.txt"))
       assert obj==open("./httpie.txt").read()
   except IOError as e:
       print("\nIO error occured")



# Generated at 2022-06-13 21:21:44.327463
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    arg = KeyValueArg(
        option_strings=[],
        dest='key',
        nargs=1,
        const=None,
        default=None,
        type=None,
        choices=None,
        required=False,
        help=None,
        metavar=None,
        key='key',
        sep='<',
        orig='key<file.txt',
        value='file.txt',
    )

    filename, f, mime_type = process_file_upload_arg(arg)
    assert filename == "file.txt"
    assert mime_type == get_content_type('file.txt')
    assert f.name == 'file.txt'

# Generated at 2022-06-13 21:21:53.460109
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    # To test the upload file, we try to process the file in data/test.mp4,
    # and get the file name and mime type.
    arg = KeyValueArg('test.mp4', "html")
    # Note: here is the test.mp4 path, you need to change it according to your
    # file path.
    arg.value = "catdata/test.mp4"
    filename, f, mime_type = process_file_upload_arg(arg)
    # Here we check if the file name and mime-type are correct.
    assert filename == "test.mp4"
    assert mime_type == "html"

if __name__ == "__main__":
    test_process_file_upload_arg()

# Generated at 2022-06-13 21:21:55.203345
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    # TODO
    pass

# Generated at 2022-06-13 21:22:06.345020
# Unit test for function process_data_raw_json_embed_arg
def test_process_data_raw_json_embed_arg():
    sample_data = []
    sample_data.append(['{"a":1}', {'a': 1}])
    sample_data.append(['{"a": 1}', {'a': 1}])
    sample_data.append(['["a",1]', ['a', 1]])
    sample_data.append(['[ "a",1]', ['a', 1]])
    sample_data.append(['["a"     ,1]', ['a', 1]])
    sample_data.append(['[ "a"     ,1]', ['a', 1]])
    sample_data.append(['[ "a" ,  1]', ['a', 1]])
    sample_data.append(['[ "ab" , "cd"]', ['ab', 'cd']])

# Generated at 2022-06-13 21:22:19.459086
# Unit test for function load_text_file
def test_load_text_file():
    item = KeyValueArg(
        sep=SEPARATOR_DATA_EMBED_FILE_CONTENTS,
        key=None,
        orig="@file.txt",
        value="file.txt"
    )

    text = load_text_file(item)
    assert text == "Hello World"


# Generated at 2022-06-13 21:22:24.469460
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    function_input = '~/Documents/file_to_upload'
    expected_output = ('file_to_upload', 
                       open('/Users/dwyane/Documents/file_to_upload', 'rb'),
                       'application/octet-stream')
    assert process_file_upload_arg(function_input) == expected_output

# Generated at 2022-06-13 21:22:35.476693
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    sep = SEPARATOR_FILE_UPLOAD
    filename = "file1.txt"
    result1 = process_file_upload_arg(KeyValueArg("", sep, filename))
    assert result1[0] == os.path.basename(filename)
    assert result1[2] == get_content_type(filename)
    assert result1[1].read() == b"file1\n"

    result2 = process_file_upload_arg(KeyValueArg("", sep, "/tmp/file2.txt"))
    assert result2[0] == os.path.basename("/tmp/file2.txt")
    assert result2[2] == get_content_type("/tmp/file2.txt")
    assert result2[1].read() == b"file2\n"

    sep = SEPARATOR_FILE

# Generated at 2022-06-13 21:22:47.642509
# Unit test for function load_text_file
def test_load_text_file():
    assert load_text_file(KeyValueArg("name", "./tests/data/colors.json")) == ('[{"color": "red", "value": "#f00"}, {"color": "green", "value": "#0f0"}, {"color": "blue", "value": "#00f"}, {"color": "cyan", "value": "#0ff"}, {"color": "magenta", "value": "#f0f"}, {"color": "yellow", "value": "#ff0"}, {"color": "black", "value": "#000"}]\n')
    assert load_text_file(KeyValueArg("name", "./tests/data/colors.txt")) == ('[red]\n[green]\n[blue]\n[cyan]\n[magenta]\n[yellow]\n[black]\n')

# Generated at 2022-06-13 21:22:59.997459
# Unit test for function load_text_file
def test_load_text_file():
    # Case 1: Existent file
    arg = argparse.Namespace()
    arg.key = "test1"
    arg.val = "test.txt"
    arg.sep = ":"
    arg.orig = "test1:" + '"' + "test.txt" + '"'
    assert (process_data_embed_file_contents_arg(arg) == 'test\n')
    # Case 2: Nonexistent file
    arg = argparse.Namespace()
    arg.key = "test2"
    arg.val = "nonexistent.txt"
    arg.sep = ":"
    arg.orig = "test2:" + '"' + "nonexistent.txt" + '"'

# Generated at 2022-06-13 21:23:03.747402
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    a = RequestItems()
    value = process_data_embed_raw_json_file_arg(KeyValueArg(key='', value='', sep=';;#'))
    assert value == {}
    assert a.data == {}
    assert a.multipart_data == {'': {}}



# Generated at 2022-06-13 21:23:08.023355
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    args = KeyValueArg('key', 'value')
    try:
        process_file_upload_arg(args)
        assert(true)
    except ParseError:
        assert(false)

# Generated at 2022-06-13 21:23:18.135302
# Unit test for function load_text_file
def test_load_text_file():
    test_cases = [
        # simple case
        {
            "item": KeyValueArg(key='', sep='', value=''),
            "path": './resources/test.txt'
        },
        # exception case 1 - IOError
        {
            "item": KeyValueArg(key='', sep='', value=''),
            "path": './resources/test_not_exist.txt'
        },
        # exception case 2 - UnicodeDecodeError
        {
            "item": KeyValueArg(key='', sep='', value=''),
            "path": './resources/test_non_utf8.txt'
        },
    ]
    for i, test_case in enumerate(test_cases):
        print(i, test_case)

# Generated at 2022-06-13 21:23:25.772989
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    arg = KeyValueArg(
        key='test_key',
        sep=SEPARATOR_DATA_EMBED_RAW_JSON_FILE,
        orig='test_key@test.json',
        value='test.json'
    )
    assert process_data_embed_raw_json_file_arg(arg) == {'test_key': 'test_value'}

# Generated at 2022-06-13 21:23:27.932837
# Unit test for function load_text_file
def test_load_text_file():
    load_text_file(KeyValueArg(orig="", key="", value="./tests/data/big_file", sep="", quoted=False))

# Generated at 2022-06-13 21:23:47.297411
# Unit test for function load_text_file
def test_load_text_file():
    import tempfile
    import os

    # Create a temporary text file
    with tempfile.TemporaryDirectory() as directory:
        path = os.path.join(directory, 'temp.txt')
        with open(path, 'w') as file:
            file.write('This is a text file')
        item = KeyValueArg('TEST', 'TEST', 'TEST', path)
        value = load_text_file(item)
        assert value == 'This is a text file'

    # Test error
    item = KeyValueArg('TEST', 'TEST', 'TEST', 'NON_EXISTENT_FILE.txt')
    try:
        load_text_file(item)
    except ParseError:
        pass

# Generated at 2022-06-13 21:23:50.996667
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    filename = "cc"
    mime_type = "json"
    f = open(os.path.expanduser(filename), 'rb')
    result = process_file_upload_arg(filename, f, mime_type)
    assert result

# Generated at 2022-06-13 21:24:01.536567
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    separator = '@'
    separator_type = ':type='

    text = '''
        D相对路径:
        !@../a.txt

        D绝对路径:
        !@/home/ivy/a.txt

        D带类型:
        !@a.txt:type=image/png

        D带类型:
        !@../a.txt:type=image/png

        D带类型:
        !@/home/ivy/a.txt:type=image/png
    '''

    lines = text.splitlines()
    args = []
    for line in lines:
        line = line.strip()

# Generated at 2022-06-13 21:24:04.798629
# Unit test for function process_data_raw_json_embed_arg
def test_process_data_raw_json_embed_arg():
    arg = KeyValueArg('json', '{"a":1}', 'json;{"a":1}')
    value = process_data_raw_json_embed_arg(arg)
    assert value == {"a":1}


# Generated at 2022-06-13 21:24:06.652705
# Unit test for function load_text_file
def test_load_text_file():
    assert load_text_file("1.txt") == "hello world\n"

# Generated at 2022-06-13 21:24:10.242821
# Unit test for function load_text_file
def test_load_text_file():
    item = [KeyValueArg('-H', 'filename.txt', '-H', 'filename.txt')]
    assert load_text_file(item) == 'filename.txt'


# Generated at 2022-06-13 21:24:17.007068
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    filename = r'C:\Users\BCD\Desktop\httpie\requirements.txt'
    item = KeyValueArg(filename, SEPARATOR_FILE_UPLOAD)
    name, f, mime_type = process_file_upload_arg(item)
    assert name == 'requirements.txt'
    assert mime_type == 'text/plain'
    f.close()

# Generated at 2022-06-13 21:24:26.985874
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    import tempfile
    fh, fpath = tempfile.mkstemp()
    with os.fdopen(fh, 'w') as tmp:
        tmp.write("test data")

    key, file, mime = process_file_upload_arg(
        KeyValueArg(SEPARATOR_FILE_UPLOAD, 'a', '{}'.format(fpath))
    )
    assert key == os.path.basename(fpath)
    assert mime == 'application/octet-stream'
    assert file.read() == b"test data"
    os.remove(fpath)


# Generated at 2022-06-13 21:24:30.186166
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    arg='fname.jpg'
    key=SEPARATOR_FILE_UPLOAD
    process_file_upload_arg(arg)

# Generated at 2022-06-13 21:24:42.375755
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    raw_json_file_content = {'a':1,'b':2}
    # create a file with name raw_json_file.json and content raw_json_file_content
    with open('raw_json_file.json', 'w') as raw_json_f:
        json.dump(raw_json_file_content, raw_json_f)
    # create a key-value request item, here key is 'body' and value is the filename which contains raw data
    raw_json_file_arg = KeyValueArg('body', 'raw_json_file.json')
    raw_json_file_content_loaded = process_data_embed_raw_json_file_arg(raw_json_file_arg)
    assert raw_json_file_content == raw_json_file_content_loaded


# Generated at 2022-06-13 21:25:00.987768
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    # Valid data
    # Float
    assert process_data_embed_raw_json_file_arg(KeyValueArg('key', 'float', separator='=')) == 2.0
    # Int
    assert process_data_embed_raw_json_file_arg(KeyValueArg('key', 'int', separator='=')) == 1
    # String
    assert process_data_embed_raw_json_file_arg(KeyValueArg('key', 'str', separator='=')) == 'string_1'
    # Boolean
    assert process_data_embed_raw_json_file_arg(KeyValueArg('key', 'bool', separator='=')) == True

    # Invalid data

# Generated at 2022-06-13 21:25:05.813978
# Unit test for function load_text_file
def test_load_text_file():
    test_item = KeyValueArg(key=None,
                            value='/home/craig/Desktop/testing.txt',
                            orig=None,
                            sep=None)
    print(load_text_file(test_item))


# Generated at 2022-06-13 21:25:13.228654
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    txtfile_path = 'test.txt'
    txtfile = open(txtfile_path, 'w')
    txtfile.write('{\"status\": \"pass\"}')
    txtfile.close()
    arg = KeyValueArg(
        sep=SEPARATOR_DATA_EMBED_RAW_JSON_FILE,
        key='',
        value=txtfile_path,
        orig='')
    value = process_data_embed_raw_json_file_arg(arg)
    assert not isinstance(value, str) and value['status'] == 'pass'
    os.remove(txtfile_path)

# Generated at 2022-06-13 21:25:17.700587
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    """
    >>> process_file_upload_arg(KeyValueArg('key', 'val'))
    Traceback (most recent call last):
    ...
    httpie.cli.exceptions.ParseError: Invalid item 'key val', must be 'key:=file' or 'key:=file;type'
    """
    return process_file_upload_arg(KeyValueArg('key', 'val'))

# Generated at 2022-06-13 21:25:26.445748
# Unit test for function load_text_file
def test_load_text_file():
    input_file = 'data/file1.txt'
    expected_output = 'hello world!'
    res = load_text_file(KeyValueArg('file', input_file))
    assert res == expected_output
    input_file = 'data/file2.txt'
    expected_output = 'hello world!\n'
    res = load_text_file(KeyValueArg('file', input_file))
    assert res == expected_output
    input_file = 'data/file3.txt'
    expected_output = 'hello world!\n'
    res = load_text_file(KeyValueArg('file', input_file))
    assert res == expected_output

# Generated at 2022-06-13 21:25:36.278320
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    arg = KeyValueArg("file", SEPARATOR_FILE_UPLOAD, "sample.jpg")
    assert os.path.basename('sample.jpg') == process_file_upload_arg(arg)[0]
    arg = KeyValueArg("file", SEPARATOR_FILE_UPLOAD, "sample.jpg:image/jpeg")
    assert 'image/jpeg' == process_file_upload_arg(arg)[2]
    arg = KeyValueArg("file", SEPARATOR_FILE_UPLOAD, "sample.jpg:image/svg+xml")
    assert 'image/svg+xml' == process_file_upload_arg(arg)[2]
    # bad mime type
    arg = KeyValueArg("file", SEPARATOR_FILE_UPLOAD, "sample.jpg:image/svg++xml")


# Generated at 2022-06-13 21:25:48.932820
# Unit test for function process_data_raw_json_embed_arg
def test_process_data_raw_json_embed_arg():
    arg = KeyValueArg("data", "animal", "dog", None, None)
    assert(process_data_raw_json_embed_arg(arg) == "dog")
    arg = KeyValueArg("data", "animal", "\"dog\"", None, None)
    assert(process_data_raw_json_embed_arg(arg) == "dog")
    arg = KeyValueArg("data", "animal", "\"cat\"", None, None)
    assert (process_data_raw_json_embed_arg(arg) == "cat")
    arg = KeyValueArg("data", "animal", "\"mouse\"", None, None)
    assert (process_data_raw_json_embed_arg(arg) == "mouse")
    arg = KeyValueArg("data", "animal", "\"dog\"", None, None)

# Generated at 2022-06-13 21:25:52.717581
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    arg = KeyValueArg(None, "--form", "file=test.txt;image/png", "")
    assert process_file_upload_arg(arg) == ('test.txt', open('C:/Users/Administrator/PycharmProjects/PyHttp/httpie/test.txt', 'rb'), 'image/png')


# Generated at 2022-06-13 21:25:57.290749
# Unit test for function load_text_file
def test_load_text_file():
    assert load_text_file(KeyValueArg(orig='A.txt', sep=';', key='text', value='A.txt')) == 'a.txt'

# Generated at 2022-06-13 21:26:03.171177
# Unit test for function load_text_file
def test_load_text_file():
    arg = KeyValueArg('d', '~/Documents/test.txt')
    assert load_text_file(arg) == ('This is a test file.\n', 'utf-8')

    arg = KeyValueArg('d', '~/Documents/test.txt:text/plain')
    assert load_text_file(arg) == ('This is a test file.\n', 'utf-8')

# Generated at 2022-06-13 21:26:17.279720
# Unit test for function load_text_file
def test_load_text_file():
    text_file = "../../config/testdata/http_client/httpie.cfg"
    process_data_embed_file_contents_arg(KeyValueArg("", ""))
    load_text_file(KeyValueArg("", text_file))

# Generated at 2022-06-13 21:26:31.349849
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    test_folder = './inputs/'
    test_inputs = [os.path.join(test_folder, f) for f in
                   os.listdir(test_folder) if os.path.isfile(os.path.join(test_folder, f))]
    for filename in test_inputs:
        with open(filename, 'r', encoding='utf-8') as f:
            input_content = f.read()
            kv_arg = KeyValueArg(sep='<!@json!>', key='', value='', orig='')
            kv_arg.value = input_content
            kv_arg.orig = input_content
            process_data_embed_raw_json_file_arg(kv_arg)

# Generated at 2022-06-13 21:26:33.614912
# Unit test for function load_text_file
def test_load_text_file():
    _ = load_text_file(KeyValueArg('a.txt'))

# Generated at 2022-06-13 21:26:41.393933
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    arg = KeyValueArg(key=None, sep=SEPARATOR_DATA_EMBED_RAW_JSON_FILE, value="../test-data/test_data.json")
    value = process_data_embed_raw_json_file_arg(arg)

    # Check the type of returned value and value of key-value
    assert type(value) is dict and value['str'] == 'str'


# Generated at 2022-06-13 21:26:44.031976
# Unit test for function load_text_file
def test_load_text_file():
    contents = load_text_file(KeyValueArg('json;@test.json', 'json;', '@test.json'))
    assert isinstance(contents, str)


# Generated at 2022-06-13 21:26:48.648831
# Unit test for function load_text_file
def test_load_text_file():
    fileName = "./httpie/cli/items.py"
    with open(fileName, 'rb') as f:
        filecontent = f.read().decode()
        print(filecontent)

if __name__ == '__main__':
    test_load_text_file()

# Generated at 2022-06-13 21:26:52.213455
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    process_data_embed_raw_json_file_arg(KeyValueArg('f', 'filename.json', ':'))


# Generated at 2022-06-13 21:26:57.082685
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    arg = KeyValueArg(SEPARATOR_FILE_UPLOAD, 'key', './test_input/test.txt:text/plain')
    assert len(process_file_upload_arg(arg)) == 3
    arg = KeyValueArg(SEPARATOR_FILE_UPLOAD, 'key', './test_input/test.txt')
    assert len(process_file_upload_arg(arg)) == 3


if __name__ == "__main__":
    test_process_file_upload_arg()

# Generated at 2022-06-13 21:27:03.934275
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    arg = KeyValueArg(
        'a',
        'b',
        {
            "name": "a",
            "value": "b",
            "sep": "@"
        }
    )
    x = process_data_embed_raw_json_file_arg(arg)
    assert isinstance(x, dict)

# Generated at 2022-06-13 21:27:07.108085
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    data = str(process_data_embed_raw_json_file_arg(KeyValueArg(key='test', value='test')))
    assert data == '{\n    "test": "test"\n}'


# Generated at 2022-06-13 21:27:25.521032
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    #Test no error
    file_contents = '{"key": "value"}'
    arg = KeyValueArg('Content-Type', 'application/json', '+', '', '+', '', '+')
    value = process_data_embed_raw_json_file_arg(arg)
    assert value['key'] == 'value'
    #Test error
    file_contents = '{"key":       "value"}'
    arg = KeyValueArg('Content-Type', 'application/json', '+', '', '+', '', '+')
    try:
        value = process_data_embed_raw_json_file_arg(arg)
    except ParseError:
        print("Caught ParseError in function process_data_embed_raw_json_file_arg")
    #Test error
    file_contents

# Generated at 2022-06-13 21:27:32.582414
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    """The code to be tested"""
    # Arrange
    arg_stream = sys.argv[1]
    arg = KeyValueArg('Content-Type:text/plain')
    arg.value = arg_stream
    # Act
    value = process_file_upload_arg(arg)
    # Assert
    assert value == (os.path.basename(arg_stream),
                                 open(os.path.expanduser(arg_stream), 'rb'),
                                 get_content_type(arg_stream),)

# Generated at 2022-06-13 21:27:38.420736
# Unit test for function load_text_file
def test_load_text_file():
    f = open("test.txt", "w+")
    f.write("Hello World")
    f.close() 
    item = KeyValueArg(SEPARATOR_DATA_EMBED_FILE_CONTENTS, "test.txt", "Hello World")
    assert(load_text_file(item) == "Hello World") 


# Generated at 2022-06-13 21:27:41.866713
# Unit test for function load_text_file
def test_load_text_file():
    f = open(r'D:\Code\Python\httpie\test_file.txt','rb')
    text = f.read()
    text = f.read().decode()
    assert True

# Generated at 2022-06-13 21:27:55.378585
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    file = "myfile.txt"
    mime_type = "plain/txt"
    file_upload_string =  file + SEPARATOR_FILE_UPLOAD_TYPE + mime_type
    orig = "metrics" + SEPARATOR_FILE_UPLOAD + file_upload_string
    args = KeyValueArg.from_string(orig)
    file_name, f,mime_type2 = process_file_upload_arg(args)
    assert file_name == 'myfile.txt'
    assert mime_type2 == 'plain/txt'
    assert f != None

# Generated at 2022-06-13 21:27:57.503722
# Unit test for function load_text_file
def test_load_text_file():
    file = 'test_data.json'
    assert load_text_file(file) == ''


# Generated at 2022-06-13 21:28:01.247294
# Unit test for function load_text_file
def test_load_text_file():
    request_item_args = [
        KeyValueArg(
            'a',
            'x',
            value = 'a',
            sep = SEPARATOR_DATA_STRING
        )
    ]
    items = RequestItems.from_args(request_item_args)
    assert items.data['a'] == 'x'

# Generated at 2022-06-13 21:28:12.342078
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    filename = '../tests/data/unix-lines.txt'
    with open(filename, 'rb') as f:
        embedded_filename = os.path.basename(filename)
        data_item_arg = KeyValueArg('hi', embedded_filename, '@')
        actual = process_file_upload_arg(data_item_arg)
        expected = (embedded_filename, f, 'text/plain')
        assert expected == actual

        data_item_arg = KeyValueArg('hi', embedded_filename + ';filetype', '@')
        actual = process_file_upload_arg(data_item_arg)
        expected = (embedded_filename, f, 'filetype')
        assert expected == actual


# Generated at 2022-06-13 21:28:18.223074
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    arg = KeyValueArg(
            sep = SEPARATOR_DATA_EMBED_RAW_JSON_FILE,
            key = "name",
            value = "test.json"
            )

    ret = process_data_embed_raw_json_file_arg(arg)
    assert isinstance(ret, dict)
    assert ret["employees"][0]["firstName"] == "John"
    assert ret["employees"][0]["lastName"] == "Doe"



# Generated at 2022-06-13 21:28:24.400726
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    arg = KeyValueArg('file', '~/Documents/image.png', ':')
    test_value1 = process_file_upload_arg(arg)
    expected_result1 = ('image.png', open(os.path.expanduser('~/Documents/image.png'), 'rb'), 'image/png')
    print(test_value1 == expected_result1)
    arg = KeyValueArg('string', '~/Documents/string.json', ':')
    test_value2 = process_file_upload_arg(arg)
    expected_result2 = ('string.json', open(os.path.expanduser('~/Documents/string.json'), 'rb'), 'image/png')
    print(test_value2 == expected_result2)



# Generated at 2022-06-13 21:28:47.988373
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    test_path = r"C:\Users\John\PycharmProjects\httpie\tests\data\json_file\json_file_with_string_value_example.txt"
    test_item = KeyValueArg(
        raw_arg='@'+test_path,
        sep='@',
        orig=test_path,
        key=test_path,
        value=test_path
    )
    print(process_data_embed_raw_json_file_arg(test_item))


if __name__ == '__main__':
    test_process_data_embed_raw_json_file_arg()

# Generated at 2022-06-13 21:28:54.023479
# Unit test for function load_text_file
def test_load_text_file():
    print("等待键盘输入")
    _ = input()

    item = KeyValueArg("sz;/Users/sz/Documents/Work/python/automation_test/httpie_test/sample_files/baidu_home.html")
    print(load_text_file(item))


if __name__ == "__main__":
    test_load_text_file()

# Generated at 2022-06-13 21:29:00.931036
# Unit test for function process_file_upload_arg
def test_process_file_upload_arg():
    import tempfile
    import os
    f = tempfile.TemporaryFile(mode='w+')
    f.write("test")
    f.seek(0)
    fname = f.name
    mime_type = get_content_type(fname)
    file_arg = KeyValueArg("test.json", "test.json", "@@")
    file_name, file_object, file_mime_type = process_file_upload_arg(file_arg)
    assert file_name == "test.json"
    assert file_object is not None
    assert file_mime_type == mime_type
    f.close()

# Generated at 2022-06-13 21:29:08.046303
# Unit test for function load_text_file
def test_load_text_file():
    class KeyValueArgMock:
        def __init__(self, value):
            self.value = value

    value = "httpie"
    item = KeyValueArgMock(value)
    file = open(value+".txt",'w') 
    file.write(value) 
    file.close() 
    assert load_text_file(item) == value
    os.remove(value+".txt")

# Generated at 2022-06-13 21:29:11.696351
# Unit test for function process_data_embed_raw_json_file_arg
def test_process_data_embed_raw_json_file_arg():
    arg = KeyValueArg(
        sep=SEPARATOR_DATA_EMBED_RAW_JSON_FILE,
        key='test',
        value='test_json.json',
        orig='test@test_json.json'
    )
    assert process_data_embed_raw_json_file_arg(arg) == [1, 2, 3]


process_arg_func = Callable[[KeyValueArg], Union[str, Tuple[str, IO, str], JSONType]]