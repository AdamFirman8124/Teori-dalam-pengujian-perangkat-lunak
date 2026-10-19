

# Generated at 2022-06-13 22:44:21.716280
# Unit test for function compress_request
def test_compress_request():
    from requests import Request
    request = Request(
        "POST",
        url="http://httpbin.org/post",
        data={
            "key1": "value1",
            "key2": "value2"
        }
    )
    prepared = request.prepare()
    assert prepared.headers["Content-Length"] == "44"
    assert prepared.headers.get("Content-Encoding", "") == ""
    compress_request(prepared, False)
    assert prepared.headers["Content-Length"] == "26"
    assert prepared.headers["Content-Encoding"] == "deflate"

# Generated at 2022-06-13 22:44:26.734750
# Unit test for function compress_request
def test_compress_request():
    data = '{"key": "value"}'
    request = requests.Request('GET', 'http://httpbin.org/get')
    request = request.prepare()
    request.body = data
    request.headers['Content-Length'] = str(len(data))
    compress_request(request,True)
    print(request.body)

# Generated at 2022-06-13 22:44:28.166673
# Unit test for function compress_request
def test_compress_request():
    request=requests.PreparedRequest()
    compress_request(request,True)

# Generated at 2022-06-13 22:44:33.809098
# Unit test for function prepare_request_body
def test_prepare_request_body():
    body = b"Hello World"
    assert prepare_request_body(body, None, None, False, False) == body
    assert prepare_request_body(body, None, None, False, True) == body
    assert prepare_request_body(body, None, None, True, False) != body
    assert prepare_request_body(body, None, None, True, False) != body

# Generated at 2022-06-13 22:44:39.175453
# Unit test for function compress_request
def test_compress_request():
    from test_client import MockPreparedRequest

    request = MockPreparedRequest()
    request.body = 'hello'
    compress_request(request, True)
    assert request.body != 'hello'
    assert request.headers['Content-Encoding'] == 'deflate'
    assert len(request.body) < 5

# Generated at 2022-06-13 22:44:43.669881
# Unit test for function compress_request
def test_compress_request():
    request = requests.PreparedRequest()
    request.body = 'test'
    always = True
    compress_request(request, always)
    assert(request.body != 'test')
    assert(request.headers['Content-Encoding'] == 'deflate')
    assert(request.headers['Content-Length'] == '12')

# Generated at 2022-06-13 22:44:50.514240
# Unit test for method __iter__ of class ChunkedUploadStream
def test_ChunkedUploadStream___iter__():
    data = [1,2,3,4,5]
    def callback(d):
        print(f"callback: {d}")
    us = ChunkedUploadStream(data, callback)
    actual = [d for d in us]
    assert data == actual, f"test_ChunkedUploadStream___iter__() failed"
    print("test_ChunkedUploadStream___iter__() passed")
    return


# Generated at 2022-06-13 22:44:59.847296
# Unit test for function compress_request
def test_compress_request():
    def test(always):
        r = requests.Request('GET', 'localhost')
        r.prepare()
        r.headers['Content-Encoding'] = 'gzip'
        r.body = zlib.compress('hello'.encode())
        compress_request(r.prepare(), always)
        return r.headers['Content-Encoding'] == 'deflate', r.body

    assert test(True) == (True, zlib.compress('hello'.encode()))
    assert test(False) == (True, zlib.compress('hello'.encode()))
    assert test(False)[0] == False

# Generated at 2022-06-13 22:45:02.407479
# Unit test for function compress_request
def test_compress_request():
    assert compress_request("hello world") == "x\x9c\xcbH\xcd\xc9\xc9W(\xcf/\xcaI\x01\x00\x1e\x9b"

# Generated at 2022-06-13 22:45:11.174604
# Unit test for function compress_request
def test_compress_request():
    def create_request(body):
        return requests.Request('GET', 'https://www.google.com', body=body)
    
    request = create_request('abc')
    compress_request(request.prepare(), True)
    assert request.body != b'abc'
    assert request.body == b'x\x9c+,V\x02\xff'

    request = create_request('abc')
    compress_request(request.prepare(), False)
    assert request.body != b'abc'
    assert request.body == b'x\x9c+,V\x02\xff'

    request = create_request('abc')
    compress_request(request.prepare(), False)
    assert request.body != b'abc'

# Generated at 2022-06-13 22:45:31.153824
# Unit test for function prepare_request_body
def test_prepare_request_body():
    # create a file like object
    txt=open('dir.txt','w')
    txt.write('test')
    txt.close()
    txt=open('dir.txt','r')
    body=txt.read()
    # test offline
    prepare_request_body(body,None,content_length_header_value=100,chunked=False,offline=True)
    # test chunked
    prepare_request_body(body,None,content_length_header_value=100,chunked=True,offline=False)
    # test without chunked
    prepare_request_body(body,None,content_length_header_value=100,chunked=False,offline=False)
    txt.close()
    # test multipart
    data={'test':'test'}


# Generated at 2022-06-13 22:45:39.900586
# Unit test for function compress_request
def test_compress_request():
    import io
    import requests
    import json

    body_dict = {"a":1}
    body_str = json.dumps(body_dict)
    body_content_length = len(body_str.encode())
    body_str_io = io.StringIO(body_str)
    request1 = requests.Request("POST", "http://baidu.com", data=body_str)
    request2 = requests.Request("POST", "http://baidu.com", data=body_dict)
    request3 = requests.Request("POST", "http://baidu.com", data=body_str_io)
    prepared_request1 = request1.prepare()
    prepared_request2 = request2.prepare()
    prepared_request3 = request3.prepare()

# Generated at 2022-06-13 22:45:46.167826
# Unit test for function compress_request
def test_compress_request():
    request = requests.PreparedRequest()
    request.body = b'Hello world!'
    request.headers = {}
    compress_request(request, False)
    assert request.body != b'Hello world!'
    assert request.headers['Content-Encoding'] == 'deflate'
    assert request.headers['Content-Length'] == str(len(request.body))

# Generated at 2022-06-13 22:45:56.991568
# Unit test for function prepare_request_body
def test_prepare_request_body():
    def body_read_callback(chunk: bytes) -> bytes:
        return chunk

    assert prepare_request_body('test', body_read_callback, offline=True) == b'test'

    assert prepare_request_body(
        RequestDataDict({'v': 'test'}), body_read_callback, offline=True) == b'v=test'

    assert isinstance(
        prepare_request_body(io.StringIO(u'test'), body_read_callback, offline=True), io.StringIO) is True
    assert isinstance(
        prepare_request_body(io.BytesIO(b'test'), body_read_callback, offline=True), io.BytesIO) is True

    assert isinstance(
        prepare_request_body('test', body_read_callback, offline=False), ChunkedUploadStream)

# Generated at 2022-06-13 22:46:00.780045
# Unit test for method __iter__ of class ChunkedUploadStream
def test_ChunkedUploadStream___iter__():
    stream = ["123", "456"]
    test_callback = lambda x: x
    test_class = ChunkedUploadStream(stream, test_callback)
    assert test_class.callback(b"hello") == b"hello"

    assert next(test_class.__iter__()) == b"123"
    assert next(test_class.__iter__()) == b"456"



# Generated at 2022-06-13 22:46:07.136136
# Unit test for function compress_request
def test_compress_request():
    # Set request body, header and expected body
    request = requests.PreparedRequest()
    request.headers = requests.structures.CaseInsensitiveDict()
    request.body = bytes('minimal content', 'utf-8')
    request.headers['Content-Encoding'] = 'identity'
    request.headers['Content-Length'] = str(len(request.body))
    compress_request(request, True)
    assert request.body == zlib.compress(bytes('minimal content', 'utf-8'))

# Generated at 2022-06-13 22:46:16.442582
# Unit test for method __iter__ of class ChunkedUploadStream
def test_ChunkedUploadStream___iter__():
    from responses import RequestsMock
    from .helpers import http
    from . import assertions

    # GET /test
    URL = 'http://example.com/test'

    # Mock the server response
    with RequestsMock() as rsps:
        rsps.add(rsps.GET, URL)

        # Mock the client upload stream
        def stream():
            yield '12345678'
            yield '9'
        upload_stream = ChunkedUploadStream(stream(), lambda chunk: None)
        r = http('GET', URL, body=upload_stream)

        # Assert the response
        assertions.assert_ok(r)



# Generated at 2022-06-13 22:46:21.966689
# Unit test for function compress_request
def test_compress_request():
    response = '{"test": 1}'
    request = requests.Request()
    request.body = response
    compress_request(request, True)
    assert request.body == zlib.compress(response.encode())
    assert request.headers['Content-Encoding'] == 'deflate'
    assert request.headers['Content-Length'] == '19'

# Generated at 2022-06-13 22:46:32.012577
# Unit test for function compress_request
def test_compress_request():
    # I wrote 6 tests:
    # 1) Empty body
    # 2) Empty body and always True
    # 3) Non empty body but not economical
    # 4) Non empty body but not economical and always True
    # 5) Non empty economical body
    # 6) Non empty economical body and always True
    empty_body = ''
    empty_body_true = ''
    non_empty_body_not_econ = 'aaaaaaaaaa'
    non_empty_body_not_econ_and_always_true = 'aaaaaaaaaa'
    non_empty_body_econ = 'aaaaaaaaa'
    non_empty_body_econ_and_always_true = 'aaaaaaaaa'
    request1 = requests.PreparedRequest()
    request1.body = empty_body
    request2 = requests.PreparedRequest()


# Generated at 2022-06-13 22:46:38.286354
# Unit test for function compress_request
def test_compress_request():
    request = requests.PreparedRequest()
    request.body = 'body'
    request.headers['Content-Type'] = 'text/html'
    request.headers['Content-Length'] = str(len(request.body))

    compress_request(request, False)

    assert request.body != 'body'
    assert request.headers['Content-Encoding'] == 'deflate'
    assert request.headers['Content-Length'] != str(len(request.body))

# Generated at 2022-06-13 22:46:48.725607
# Unit test for function compress_request
def test_compress_request():
    request = requests.PreparedRequest()
    request.body = 'hello world'
    request.headers = {'Content-Length': '11',
                       'Content-Type': 'text/plain'}
    compress_request(request, False)
    print(request.body)
    print(request.headers)
    print(bytes(request.body))

# Generated at 2022-06-13 22:46:53.704570
# Unit test for function compress_request
def test_compress_request():
    request = requests.PreparedRequest()
    request.body = b'This is a normal body'
    request.headers['Content-Encoding'] = 'null'
    request.headers['Content-Length'] = '19'
    compress_request(request, True)

    expect_body = zlib.compress(b'This is a normal body')
    expect_header = 'deflate'
    expect_length = '22'

    assert request.body == expect_body
    assert request.headers['Content-Encoding'] == expect_header
    assert request.headers['Content-Length'] == expect_length

# Generated at 2022-06-13 22:47:03.910429
# Unit test for function compress_request
def test_compress_request():
    request = requests.PreparedRequest()

# Generated at 2022-06-13 22:47:15.553659
# Unit test for function compress_request
def test_compress_request():
    class Request(object):
        def __init__(self):
            self.headers = dict()
            self.body = ""

    req = Request()
    req.headers['Content-Length'] = "1000"
    req.body = '{'
    compress_request(req, True)
    
    assert req.headers['Content-Length'] == '1'
    assert req.headers['Content-Encoding'] == 'deflate'
    assert req.body == b'x\x9cK\r\x00\x01\x05\x00\x00\x00\x00\x00\x00\x00'

# Generated at 2022-06-13 22:47:27.250624
# Unit test for function get_multipart_data_and_content_type
def test_get_multipart_data_and_content_type():
    data = {'key1': 'value1', 'key2': 'value2'}
    data, content_type = get_multipart_data_and_content_type(data)
    assert data.to_string() == '''\
--===============6330780887842465327==
Content-Disposition: form-data; name="key1"

value1
--===============6330780887842465327==
Content-Disposition: form-data; name="key2"

value2
--===============6330780887842465327==--
'''
    assert content_type == 'multipart/form-data; boundary================6330780887842465327=='

# Generated at 2022-06-13 22:47:31.489948
# Unit test for function compress_request
def test_compress_request():
    request = requests.Request('GET', 'http://127.0.0.1').prepare()
    request.body = 'dsfjdi'
    request.headers['Content-Length'] = '7'
    compress_request(request, False)
    assert request.headers['Content-Encoding'] == 'deflate'
    assert request.headers['Content-Length'] == '38'

# Generated at 2022-06-13 22:47:36.714704
# Unit test for function prepare_request_body
def test_prepare_request_body():
    from io import BytesIO
    from requests.structures import CaseInsensitiveDict

    # Send proper Content-Length header.
    content_length = '2'
    assert prepare_request_body(b'hi', lambda *a: None, content_length) == b'hi'

    request = requests.Request(
        url='',
        data=prepare_request_body(
            BytesIO(b'hi'),
            lambda *a: None,
            content_length,
            chunked=False,
            offline=False,
        ),
    )
    request.prepare()
    assert request.headers.get('Content-Length') == content_length

    # Use chunked encoding.

# Generated at 2022-06-13 22:47:44.242143
# Unit test for function compress_request
def test_compress_request():
    import requests
    p = requests.PreparedRequest()
    # p.body cannot be empty
    p.body = "DUMMY"
    expected = "DUMMY"
    compress_request(p, False)
    if isinstance(p.body, str):
        actual = p.body
    else:
        actual = p.body.decode('utf-8')
    assert actual == expected

    import zlib
    deflater = zlib.compressobj()
    deflated_data = deflater.compress("dummy")
    deflated_data += deflater.flush()
    p.body = deflated_data
    expected = deflated_data
    compress_request(p, False)
    actual = p.body
    assert actual == expected

# Generated at 2022-06-13 22:47:45.026156
# Unit test for function compress_request
def test_compress_request():
    assert True

# Generated at 2022-06-13 22:47:55.644765
# Unit test for function compress_request
def test_compress_request():
    class FakeResponse:
        def __init__(self, content):
            self.content = content

    class FakeRequest:
        def __init__(self, body, headers):
            self.body = body
            self.headers = headers

    def send_request():
        self.response = response_class(
            content=response.content,
            status_code=response.status_code,
            headers=response.headers,
            request=self.request,
        )

    request = FakeRequest(body=b'aaaaa', headers={'Content-Length': 5, 'Content-Encoding': 'gzip'})
    compress_request(request, True)

# Generated at 2022-06-13 22:48:13.420640
# Unit test for function compress_request
def test_compress_request():
    req = requests.Request('GET', 'http://example.com', data="Hello World!")
    prepared_req = req.prepare()
    compress_request(prepared_req, True)
    assert prepared_req.headers['Content-Encoding'] == 'deflate'

# Generated at 2022-06-13 22:48:21.758410
# Unit test for function prepare_request_body
def test_prepare_request_body():
    import requests
    import json

    r = requests.get('http://httpbin.org/get')
    print(r.url)
    print(r.text)
    print(r.json())

    # prepare a dict
    payload = {"name": "John Doe", "age": 21, "address": "somewhere"}
    r = requests.post('http://httpbin.org/post', data=payload)
    print(r.json())

    # prepare files
    payload = {"file": open('test.txt', 'rb')}
    r = requests.post('http://httpbin.org/post', files=payload)
    print(r.json())

    # json
    payload = {'name': 'John Doe'}
    r = requests.post('http://httpbin.org/post', json=payload)

# Generated at 2022-06-13 22:48:32.009414
# Unit test for function compress_request
def test_compress_request():
    def test_case(
        request: requests.PreparedRequest,
        always: bool,
        expected_compressed: bool
    ):
        compress_request(request, always)
        is_compressed = request.headers.get('Content-Encoding') == 'deflate'
        assert is_compressed == expected_compressed, \
            "Compression of request was as expected"

    common_headers = {
        'Content-Type': 'application/json',
        'Content-Length': '0'
    }
    req = requests.PreparedRequest()

# Generated at 2022-06-13 22:48:43.191011
# Unit test for function prepare_request_body
def test_prepare_request_body():
    def body_read_callback(chunk):
        return chunk

    test_str = "abc"
    test = prepare_request_body(test_str, body_read_callback)
    assert test == "abc"

    test_dict = {"a": "b"}
    test = prepare_request_body(test_dict, body_read_callback)
    assert test == "a=b"

    test_dict = {"a": ["zz", "ll"]}
    test = prepare_request_body(test_dict, body_read_callback)
    assert test == "a=zz&a=ll"

    test_file_like = io.StringIO('abc')
    assert test_file_like.closed == False
    test = prepare_request_body(test_file_like, body_read_callback)

# Generated at 2022-06-13 22:48:54.347290
# Unit test for function compress_request
def test_compress_request():
    request = requests.PreparedRequest()
    request.body = b'lalala'
    request.headers = {}
    compress_request(request, always=True)
    assert(request.headers['Content-Encoding'] == 'deflate')
    assert(request.body == zlib.compress(b'lalala'))

    request = requests.PreparedRequest()
    request.body = b'lalala'
    request.headers = {}
    compress_request(request, always=False)
    assert('Content-Encoding' not in request.headers)
    assert(request.body == b'lalala')

# Generated at 2022-06-13 22:49:05.372199
# Unit test for function compress_request
def test_compress_request():
    d = {'test_key': 'test_value'}
    url = 'http://httpbin.org/get'
    request = requests.Request('GET', url, data=d).prepare()
    compress_request(request, False)
    compressed_request = requests.Request('GET', url, data=d).prepare()
    compressed_request.body = b'x\x9c+\xcf,IJ\xce\xcf/\xcaI\xcc\xcf\xf8a\x04\x00\xc3\x1b\x8a\x85\x9a\x01\x00'

# Generated at 2022-06-13 22:49:14.407316
# Unit test for function compress_request
def test_compress_request():
    request = requests.PreparedRequest()
    request.body = "This is a test"
    request.headers = { 'Content-Length': str(len(request.body)) }
    compress_request(request, False)
    assert request.headers['Content-Length'] == '19'
    assert request.headers['Content-Encoding'] == 'deflate'
    assert request.body == (b'x\x9c\xcbH\xcd\xc9\xc9W(\xcf/\xcaI\x01\x00\x08\x02\xf3\x01')

# Generated at 2022-06-13 22:49:17.968949
# Unit test for function prepare_request_body
def test_prepare_request_body():
    body = {'request': 'hello_request'}
    body_read_callback = lambda x: x
    body = prepare_request_body(body, body_read_callback)
    assert body == 'request=hello_request'

# Generated at 2022-06-13 22:49:23.156265
# Unit test for function compress_request
def test_compress_request():
    request = requests.PreparedRequest()
    request.body = "test"
    compress_request(request, True)
    assert request.body == zlib.compress("test".encode())

test_compress_request()

# Generated at 2022-06-13 22:49:31.193955
# Unit test for function compress_request
def test_compress_request():
    from httpie.models import Request
    from httpie.client import prepare_body_and_headers
    from httpie.compression import decompress_response
    from httpie import ExitStatus
    from httpie._compat import urlopen
    from json import loads

    # init body and headers for request

# Generated at 2022-06-13 22:49:47.208521
# Unit test for function compress_request
def test_compress_request():
    test_request = requests.Request(method='GET', url='https://fake.com/')
    test_request.headers = {'foo': 'bar'}

    # 1. test request body is str
    test_request.body = "abracadabra"
    compress_request(test_request, False)
    assert test_request.body == b'x\x9c\xcbH\xcd\xc9\xc9W(\xcf/\xcaI\x01\x00?\x01\x00'
    assert test_request.headers == {'foo': 'bar', 'Content-Encoding': 'deflate', 'Content-Length': '18'}

    # 2. test request body is not str, no Content-Length in request headers
    test_request.body = b'abracadabra'
   

# Generated at 2022-06-13 22:49:55.284739
# Unit test for function prepare_request_body
def test_prepare_request_body():
    def test_body(body, expected_body, body_read_callback, expected_callback_count, content_length_header_value, chunked, offline):
        counter = 0
        def callback(chunk):
            nonlocal counter
            counter += 1
        body = prepare_request_body(body, callback, content_length_header_value, chunked, offline)
        assert body == expected_body
        assert counter == expected_callback_count

    def callback(chunk):
        return chunk

    class FakeFile:
        def __init__(self, data):
            self._data = data
            self._pos = 0

        def read(self, *args, **kwargs):
            result = self._data[self._pos:self._pos+1]
            if result:
                self._pos += 1
            return result


# Generated at 2022-06-13 22:50:00.687283
# Unit test for function prepare_request_body
def test_prepare_request_body():

    def body_read_callback(chunk):
        pass

    result = prepare_request_body(
        body={'username': 'test', 'password': 'test123'},
        body_read_callback=body_read_callback,
        content_length_header_value=None,
        chunked=False,
        offline=False,
    )
    assert result == "username=test&password=test123"

# Generated at 2022-06-13 22:50:08.207762
# Unit test for function prepare_request_body
def test_prepare_request_body():
    # Given
    class FileLike(object):
        def read(self):
            return b'foo'

    def mycallback(x):
        pass

    # When
    body = prepare_request_body(
        body='foo',
        body_read_callback=mycallback,
        content_length_header_value=None,
        chunked=False,
        offline=True,
    )
    # Then
    assert body == b'foo'
    # When
    body = prepare_request_body(
        body=FileLike(),
        body_read_callback=mycallback,
        content_length_header_value=None,
        chunked=False,
        offline=False,
    )
    # Then
    assert body.read() == b'foo'

# Generated at 2022-06-13 22:50:15.182703
# Unit test for function compress_request
def test_compress_request():
    url = 'https://httpbin.org/post'
    data = 'hello world'
    request = requests.Request('POST', url, data=data).prepare()
    compress_request(request, True)
    assert request.body == zlib.compress(data.encode())
    assert request.headers['Content-Encoding'] == 'deflate'

# Generated at 2022-06-13 22:50:20.643456
# Unit test for function get_multipart_data_and_content_type
def test_get_multipart_data_and_content_type():
    data = {'key1': 'val1', 'key2': 'val2'}
    result = get_multipart_data_and_content_type(data)
    assert(b'Content-Type: multipart/form-data; boundary="' in result[0].to_string())
    assert('Content-Type: multipart/form-data; boundary="' in result[1])



# Generated at 2022-06-13 22:50:25.131013
# Unit test for function compress_request
def test_compress_request():
    request = requests.PreparedRequest()
    request.headers = {}
    request.body = 'hello'
    compress_request(request, False)
    assert request.body == b'x\x9c\xcbH\xcd\xc9\xc9W(\xcf/\xcaI\x01\x00?\xdb\x05\x01'
    assert request.headers == {
        'Content-Encoding': 'deflate',
        'Content-Length': '22'
    }

# Generated at 2022-06-13 22:50:31.313780
# Unit test for function compress_request
def test_compress_request():
    TEST_URL = "http://httpbin.org/post"
    data = {
        'name': 'foo',
        'file': 'blah'
    }
    request = requests.Request('POST', TEST_URL, data=data).prepare()
    assert len(request.headers) == 4
    assert request.headers['Content-Type'] == 'application/x-www-form-urlencoded'
    assert request.headers['Content-Length'] == '17'
    assert 'Content-Encoding' not in request.headers
    compress_request(request, True)
    assert len(request.headers) == 4
    assert request.headers['Content-Type'] == 'application/x-www-form-urlencoded'
    assert request.headers['Content-Length'] == '16'
    assert request.headers['Content-Encoding']

# Generated at 2022-06-13 22:50:34.091738
# Unit test for function compress_request
def test_compress_request():
    r = requests.PreparedRequest()
    r.body = "{\"key\": \"value\"}"
    compress_request(r, True)
    assert(r.headers['Content-Encoding'] == 'deflate')

# Generated at 2022-06-13 22:50:41.710265
# Unit test for function get_multipart_data_and_content_type
def test_get_multipart_data_and_content_type():
    data = {'a': 'b', 'c': 'd'}
    data, content_type = get_multipart_data_and_content_type(data, boundary=None, content_type=None)
    assert content_type.startswith('multipart/form-data;')

    data = {'a': 'b', 'c': 'd'}
    data, content_type = get_multipart_data_and_content_type(data, boundary='wtf', content_type=None)
    assert content_type.startswith('multipart/form-data;')
    assert 'boundary=wtf' in content_type

    data = {'a': 'b', 'c': 'd'}

# Generated at 2022-06-13 22:50:57.881969
# Unit test for function compress_request
def test_compress_request():
    req = requests.PreparedRequest()
    req.body = '123456789'
    compress_request(req, False)
    assert req.headers['Content-Length'] == str(9)
    assert req.headers['Content-Encoding'] == 'deflate'
    assert req.body == b'x\x9cW\xcb\xcf\x07\x00\x02\xf2\x01\x04\x00\x00\xff\xff=\xd4\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00'

# Generated at 2022-06-13 22:51:02.215023
# Unit test for function compress_request
def test_compress_request():
    request = requests.PreparedRequest()
    request.body = "hello"
    request.headers['Content-Length'] = 5
    compress_request(request, False)
    assert request.body == b'x\x9c+\xcbH\xcd\xc9\xc9\x07\x00\x06,H\x04\x00'



# Generated at 2022-06-13 22:51:13.499748
# Unit test for function compress_request
def test_compress_request():
    req = request_module.Request()
    req.method = 'POST'
    req.url = "https://httpbin.org/post"
    req.data = 'abcdefgh'
    req.data_type = ''
    req.headers = {'Content-Length': 8}
    req.content_type = ''

    req = request_module.prepare_request(req)
    req.body = bytes(req.body, 'utf-8')
    compress_request(req, True)

    # print(req.body)
    assert req.body == b'x\x9c\xcbH\xcd\xc9\xc9W(\xcf/\xcaI\x01\x00'
    assert req.headers["Content-Encoding"] == 'deflate'
    assert req.headers["Content-Length"]

# Generated at 2022-06-13 22:51:19.847815
# Unit test for function compress_request
def test_compress_request():
    headers = {"Content-Type": "application/json", "Content-Length": "43"}
    request = requests.PreparedRequest()
    request.method = "GET"
    request.url = None
    request.body = b'{"user_name":"test","password":"test","image_code":"test"}'
    request.prepare_headers(headers)
    compress_request(request, always=True)
    print(request.body)


test_compress_request()

# Generated at 2022-06-13 22:51:22.914351
# Unit test for function compress_request
def test_compress_request():
    request = requests.PreparedRequest()
    request.body = ['a', ' b', ' c']
    compress_request(request, True)
    assert request.headers['Content-Length'] == str(len(request.body))

# Generated at 2022-06-13 22:51:30.395070
# Unit test for function prepare_request_body
def test_prepare_request_body():
    test_string = '1234567890abcdefghijk'
    test_list = ['key1=value1', 'key2=value2', 'key3=value3']
    test_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
    test_string_reader = io.StringIO(test_string)
    test_bytes_reader = io.BytesIO(b'1234567890')
    test_file = open('/dev/zero', 'rb')
    test_bytes_reader2 = io.BytesIO(b'1234567890')

    def mycallback(chunk):
        print(chunk)

    def mycallback2(chunk):
        print(chunk)



# Generated at 2022-06-13 22:51:37.762895
# Unit test for function prepare_request_body
def test_prepare_request_body():
    body = "This is a test string"
    assert prepare_request_body(body, None) == "This is a test string"
    data = {'key': 'value'}
    assert prepare_request_body(data, None) == "key=value"
    assert prepare_request_body(data, None, None, True) == "key=value"
    data = MultipartRequestDataDict({'key': 'value'})
    body, content_type = get_multipart_data_and_content_type(data)
    assert isinstance(body, MultipartEncoder)

# Generated at 2022-06-13 22:51:47.960679
# Unit test for function get_multipart_data_and_content_type
def test_get_multipart_data_and_content_type():
    data = {'name': 'httpie', 'language': 'python'}
    boundary = '---ABC'
    content_type = 'multipart/form-data; boundary=---ABC'
    multipart_object = MultipartEncoder(fields=data.items(), boundary=boundary)
    multipart_encoder, content_type_none = get_multipart_data_and_content_type(data)
    assert multipart_object.to_string() == multipart_encoder.to_string() and content_type_none == content_type

# Generated at 2022-06-13 22:51:48.773506
# Unit test for function compress_request
def test_compress_request():
    assert compress_request


# Generated at 2022-06-13 22:51:59.831952
# Unit test for function compress_request
def test_compress_request():
    request1 = requests.PreparedRequest()
    request1.body = 'Hello world'
    compress_request(request1, False)
    assert request1.body == b'x\x9cK\xca\x00\x0f\x86\x00\x01\xaa(N\x84\x03'

    request2 = requests.PreparedRequest()
    request2.body = 'Hello world'
    compress_request(request2, True)
    assert request2.body == b'x\x9cK\xca\x00\x0f\x86\x00\x01\xaa(N\x84\x03'

# Generated at 2022-06-13 22:52:15.428433
# Unit test for function compress_request
def test_compress_request():
    test_data = "Hello World"
    test_header = {'Content-Length': str(len(test_data)), 'Content-Type': 'nonsense/none'}
    class test_req(object):
        def __init__(self, body, headers):
            self.body = body
            self.headers = headers
            
    req = test_req(test_data, test_header)
    compress_request(req, False)
    deflater = zlib.compressobj()
    deflated_data = deflater.compress(req.body.encode())
    deflated_data += deflater.flush()
    print(type(deflated_data))
    print(type(req.body))
    assert isinstance(req.body, bytes)
    
test_compress_request()

# Generated at 2022-06-13 22:52:24.665921
# Unit test for function prepare_request_body
def test_prepare_request_body():
    body = b"TXT"
    body_read_callback = lambda txt: bytes(txt)
    result = prepare_request_body(body, body_read_callback, offline = True)
    assert result == body

    body = RequestDataDict({'a': 'b'})
    body_read_callback = lambda txt: bytes(txt)
    result = prepare_request_body(body, body_read_callback, offline=True)
    assert result == b"a=b"


# Generated at 2022-06-13 22:52:32.631472
# Unit test for function compress_request
def test_compress_request():
    always = True
    request = requests.PreparedRequest()
    request.url = 'https://httpbin.org/post'
    request.body = "testing"
    compress_request(request, always)
    assert request.headers['Content-Encoding'] == 'deflate'
    assert request.body == zlib.compress(b"testing")
    assert request.headers['Content-Length'] == str(len(request.body))
    request.body = "testing"
    request.headers['Content-Encoding'] = 'deflate'
    always = False
    compress_request(request, always)
    assert request.body == b"testing"

# Generated at 2022-06-13 22:52:38.966801
# Unit test for function compress_request
def test_compress_request():
    request = requests.PreparedRequest()
    request.body = "abc" * 1024 * 1024
    compress_request(request, False)
    assert len(request.body) < len("abc" * 1024 * 1024)
    assert request.headers['Content-Encoding'] == "deflate"
    assert int(request.headers['Content-Length']) == len(request.body)

# Generated at 2022-06-13 22:52:50.004613
# Unit test for function prepare_request_body
def test_prepare_request_body():
    # Request body text
    body = "this is a request body"
    prepared_body = prepare_request_body(body)
    assert prepared_body == body

    # Request body bytes
    body = b"this is a request body"
    prepared_body = prepare_request_body(body)
    assert prepared_body == body

    # Request body file
    body = open("test.jpg", "rb")
    prepared_body = prepare_request_body(body)
    assert prepared_body == body

    # Offline mode
    body = "this is a request body"
    prepared_body = prepare_request_body(body, offline=True)
    assert prepared_body == body.encode()

    body = b"this is a request body"
    prepared_body = prepare_request_body(body, offline=True)
    assert prepared

# Generated at 2022-06-13 22:52:59.308652
# Unit test for function compress_request
def test_compress_request():
    request1 = requests.PreparedRequest()
    request1.body = 'string body'
    compress_request(request=request1, always=False)
    assert request1.body == zlib.compress(b'string body')
    assert 'Content-Encoding' in request1.headers
    assert 'Content-Length' in request1.headers

    request2 = requests.PreparedRequest()
    request2.body = 'string'
    compress_request(request=request2, always=True)
    assert request2.body == zlib.compress(b'string')
    assert 'Content-Encoding' in request2.headers
    assert 'Content-Length' in request2.headers

# Generated at 2022-06-13 22:53:08.801196
# Unit test for function prepare_request_body
def test_prepare_request_body():
    data = {'foo': 'bar'}
    # Test not a file like object
    body = prepare_request_body(data, lambda: None)
    assert body == 'foo=bar'
    # Test file like object
    file = StringIO()
    file.write('test')
    file.seek(0)
    body = prepare_request_body(file, lambda x: None)
    assert body.read() == 'test'

    # Test chunked upload stream
    body = prepare_request_body(data, lambda: None, chunked=True)
    assert isinstance(body, ChunkedUploadStream)

    # Test ChunkedMultipartUploadStream
    data = {'foo': 'bar'}
    data = MultipartEncoder(fields=data.items())

# Generated at 2022-06-13 22:53:14.278837
# Unit test for function compress_request
def test_compress_request():
    request = requests.PreparedRequest()
    request.body = '{hello: world}'
    request.headers = {'Content-Type': 'application/json'}
    compress_request(request, always=False)
    assert request.body != '{hello: world}'
    assert request.headers['Content-Encoding'] == 'deflate'
    assert request.headers['Content-Length'] != 12

# Generated at 2022-06-13 22:53:19.557293
# Unit test for function prepare_request_body
def test_prepare_request_body():
    body = {'a': 'b'}
    encoded = urlencode(body, doseq=True)
    assert prepare_request_body(body, body_read_callback=None) == encoded

# Generated at 2022-06-13 22:53:30.793022
# Unit test for function prepare_request_body
def test_prepare_request_body():
    def callback(chunk):
        pass
    # offline
    body='foo'
    assert prepare_request_body(body, callback, offline=True) == body
    body=b'foo'
    assert prepare_request_body(body, callback, offline=True) == body
    body=io.BytesIO(body)
    result = prepare_request_body(body, callback, offline=True)
    assert result == body.getvalue()
    body = None
    assert prepare_request_body(body, callback, offline=True) == body
    # not offline
    body='foo'
    assert prepare_request_body(body, callback, offline=False) == body
    body=b'foo'
    assert prepare_request_body(body, callback, offline=False) == body