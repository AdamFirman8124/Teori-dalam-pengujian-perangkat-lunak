

# Generated at 2022-06-13 22:44:06.357297
# Unit test for function compress_request
def test_compress_request():
    import pytest
    from collections import namedtuple
    MockRequest = namedtuple('PreparedRequest', ['body', 'headers'])
    request = MockRequest(body=b'test_data', headers={'Content-Type': 'application/x-www-form-urlencoded'})
    expected = {'Content-Type': 'application/x-www-form-urlencoded', 'Content-Encoding': 'deflate', 'Content-Length': '15'}
    compress_request(request, always=True)
    assert request.body == b'x\x9cK\xcaH\xcd\xc9\xc9W(\xcf/\xcaI\x01\x00\x1b\x00\x03'
    compress_request(request, always=False)
    assert request.headers == expected



# Generated at 2022-06-13 22:44:17.965750
# Unit test for method __iter__ of class ChunkedUploadStream
def test_ChunkedUploadStream___iter__():
    import httpie.cli.dicts
    import httpie.cli.formatter
    import httpie.cli.argtypes
    import httpie.cli.output.streams
    import httpie.cli.exceptions
    import httpie.cli.utils
    from httpie.cli.argtypes import KeyValueArgType
    _is_windows = httpie.cli.utils.is_windows
    import httpie.cli.transformers
    import httpie.plugins
    import httpie.plugins.manager
    import httpie.plugins.builtin
    import httpie.plugins.builtin
    import httpie.content
    import httpie.plugins
    import httpie.content
    import httpie.cli.utils
    import httpie.compat
    import httpie.downloads
    import httpie.__main__

# Generated at 2022-06-13 22:44:28.935919
# Unit test for function prepare_request_body
def test_prepare_request_body():
    def callback(body):
        callback.called += 1

    callback.called = 0
    body = 'content'
    r = prepare_request_body(
        body,
        body_read_callback=callback
    )
    assert r == body
    assert callback.called == 0

    r = prepare_request_body(
        body,
        body_read_callback=callback,
        chunked=True
    )
    assert isinstance(r, ChunkedUploadStream)
    assert callback.called == 1

    callback.called = 0
    body = io.StringIO(body)
    body_len = super_len(body)
    r = prepare_request_body(
        body,
        body_read_callback=callback
    )
    assert isinstance(r, io.StringIO)

# Generated at 2022-06-13 22:44:41.104637
# Unit test for function prepare_request_body
def test_prepare_request_body():
    from requests_toolbelt.multipart.encoder import MultipartEncoder
    from requests.utils import super_len
    body_read_callback = lambda chunk: chunk
    # 1.prepare_request_body(body, body_read_callback, content_length_header_value, chunked, offline)
    # 2.prepare_request_body(body, body_read_callback, None, True, False)
    # 3.prepare_request_body(body, body_read_callback, None, None, True)
    # 4.prepare_request_body(body, body_read_callback, None, None, None)
    # 5.prepare_request_body(body, body_read_callback, None, True, None)
    # 6.prepare_request_body('', body_read_callback, 100,

# Generated at 2022-06-13 22:44:47.693362
# Unit test for function compress_request
def test_compress_request():
    request = requests.PreparedRequest()
    data = 'a' * 100000
    request.headers['Content-Length'] = str(len(data))
    request.body = data
    compress_request(request, True)

    assert request.headers['Content-Length'] != str(len(data))

# Generated at 2022-06-13 22:44:55.288656
# Unit test for function compress_request
def test_compress_request():
    request = requests.PreparedRequest()
    request.body = 'some content'
    compress_request(request, True)
    assert request.body == zlib.compress('some content'.encode('utf-8'))
    assert b'Content-Encoding' in request.headers
    assert request.headers['Content-Encoding'] == 'deflate'
    assert b'Content-Length' in request.headers



# Generated at 2022-06-13 22:45:00.665175
# Unit test for function compress_request
def test_compress_request():
    request = requests.PreparedRequest()
    request.body = 'hello world'
    request.headers['Content-Length'] = str(len(request.body))
    compress_request(request, False)
    assert request.body == \
        b'\x78\x9c\xcb\x48\xcd\xc9\xc9\x57\x28\xcf\x2f\xca\x49\x01\x00\x28\x94\x04\x00'
    assert request.headers['Content-Encoding'] == 'deflate'



# Generated at 2022-06-13 22:45:04.823266
# Unit test for function compress_request
def test_compress_request():
    request = requests.PreparedRequest()
    request.body = 'HELLO'
    compress_request(request, True)
    assert request.body == b'x\x9c\xcbH,V\x00\x00\xa3\x04\x80\x10\x04\x00'

# Generated at 2022-06-13 22:45:12.685401
# Unit test for function prepare_request_body
def test_prepare_request_body():
    import requests
    import json
    import io
    import zlib
    response = requests.get("https://httpie.org/docs")
    data = json.loads(response.text)
    # Test for ChunkedUploadStream
    output1 = io.BytesIO()
    request_body = ChunkedUploadStream(
        stream = (chunk.encode() for chunk in [response.text]),
        callback = lambda x: output1.write(x)
    )
    assert output1.getvalue() == response.text.encode()
    # Test for ChunkedMultipartUploadStream
    output2 = io.BytesIO()
    request_body = ChunkedMultipartUploadStream(encoder = MultipartEncoder(data))
    request_body1 = request_body.__iter__()

# Generated at 2022-06-13 22:45:17.939807
# Unit test for function compress_request
def test_compress_request():
    request = requests.PreparedRequest()
    request_data = "bala" * 100 * 1024
    request.body = request_data
    request.headers['Content-Encoding'] = 'deflate'
    request.headers['Content-Length'] = '9'
    compress_request(request, True)

# Generated at 2022-06-13 22:45:25.719854
# Unit test for function prepare_request_body
def test_prepare_request_body():
    body = 'string body'
    assert prepare_request_body(body, lambda x: x) == body

# Generated at 2022-06-13 22:45:36.145347
# Unit test for function compress_request
def test_compress_request():
    data = {
        'name': 'John',
        'lastname': 'Smith'
    }
    r = requests.Request('GET', 'http://example.com/api/example', data=data)
    assert hasattr(r, 'data') is True
    assert hasattr(r, 'headers') is True
    prepared = r.prepare()
    assert hasattr(prepared, 'body') is True
    assert hasattr(prepared, 'headers') is True
    compress_request(prepared, True)
    assert hasattr(prepared, 'headers') is True
    assert prepared.headers['Content-Encoding'] == 'deflate'

# Generated at 2022-06-13 22:45:45.778169
# Unit test for function prepare_request_body
def test_prepare_request_body():
    from .testutils.streams import MockStream

    # Mock object for callback
    class MockCallback:
        def __init__(self):
            # Store all data passed to callback
            self.data = []

        def __call__(self, chunk):
            self.data += [chunk]

    # Prepare variables
    stream = MockStream(1)
    body = stream
    mock = MockCallback()
    callback = mock
    # Run function
    res = prepare_request_body(
        body=body,
        body_read_callback=callback,
        content_length_header_value=None,
        chunked=True,
        offline=False,
    )
    # Check result
    assert isinstance(res, ChunkedUploadStream)
    assert isinstance(res.stream, MockStream)

# Generated at 2022-06-13 22:45:54.631502
# Unit test for function prepare_request_body
def test_prepare_request_body():
    body_read_callback = lambda chunk: None
    content_length_header_value = 5
    chunked = False
    offline = False
    
    # without offline, without chunked
    body = 'hello'
    mybody = prepare_request_body(body, body_read_callback, content_length_header_value, chunked, offline)
    assert mybody == 'hello'

    # with offline
    body = 'hello'
    offline = True
    mybody = prepare_request_body(body, body_read_callback, content_length_header_value, chunked, offline)
    assert mybody == 'hello'

    # with chunked
    body = 'hello'
    chunked = True
    offline = False

# Generated at 2022-06-13 22:46:02.839773
# Unit test for method __iter__ of class ChunkedMultipartUploadStream
def test_ChunkedMultipartUploadStream___iter__():
    from httpie.cli.dicts import MultipartRequestDataDict
    from requests_toolbelt import MultipartEncoder
    data = MultipartRequestDataDict({"test": "haha"})
    encoder = MultipartEncoder(fields=data.items())
    stream = ChunkedMultipartUploadStream(encoder)
    chunks = stream.__iter__()
    total_chunks = 0
    for chunk in chunks:
        total_chunks += 1
    assert total_chunks == 1

# Generated at 2022-06-13 22:46:10.361256
# Unit test for function prepare_request_body
def test_prepare_request_body():
    body={"hello": "world"}
    body_read_callback = lambda x: None
    body = prepare_request_body(body, body_read_callback)
    assert body == "hello=world"
    body = {"a": ["1","2","3"]}
    body = prepare_request_body(body, body_read_callback)
    assert body == "a=1&a=2&a=3"


# Generated at 2022-06-13 22:46:22.068835
# Unit test for function compress_request
def test_compress_request():
    request = requests.PreparedRequest()

# Generated at 2022-06-13 22:46:32.012572
# Unit test for function prepare_request_body
def test_prepare_request_body():
    import io

    # Test ChunkedUploadStream on file-like body
    buf = io.StringIO()
    buf.write('abc')
    buf.seek(0)
    read_callback = lambda chunk: print(chunk)

    stream = prepare_request_body(body=buf, body_read_callback=read_callback, chunked=True, offline=False)

    print(type(stream))
    print(stream.stream)
    for ch in stream:
        print(ch)

    # Test ChunkedUploadStream on non file-like body
    stream = prepare_request_body(body='aaa', body_read_callback=read_callback, chunked=True, offline=False)

    print(type(stream))
    print(stream.stream)
    for ch in stream:
        print(ch)

    # Test

# Generated at 2022-06-13 22:46:42.080687
# Unit test for function prepare_request_body
def test_prepare_request_body():
    def body_read_callback(data):
        return data

    body_is_file_like = hasattr(open('test.py', 'r'), 'read')
    body = prepare_request_body(
        body=open('test.py', 'r'),
        body_read_callback=body_read_callback,
        content_length_header_value=None,
        chunked=False,
        offline=False,
    )

    assert isinstance(body, ChunkedUploadStream)
    assert isinstance(body.stream, object)
    assert isinstance(body.callback, object)

    body_is_file_like = hasattr('s', 'read')

# Generated at 2022-06-13 22:46:44.203553
# Unit test for function prepare_request_body
def test_prepare_request_body():
    assert prepare_request_body("", None, chunked=True) == "".encode()

if __name__ == '__main__':
    test_prepare_request_body()

# Generated at 2022-06-13 22:46:58.104697
# Unit test for function compress_request
def test_compress_request():
    request = requests.PreparedRequest()
    request.body = 'test'
    compress_request(request, False)
    assert request.headers['Content-Encoding'] == 'deflate'
    assert request.headers['Content-Length'] == '10'

test_compress_request()

# Generated at 2022-06-13 22:47:05.036439
# Unit test for function compress_request
def test_compress_request():
    def _test_compress_request_impl(data):
        req = requests.Request('post', 'http://httpbin.org/post', data=data)
        p = req.prepare()
        compress_request(p, always=False)
        assert p.headers['Content-Encoding'] == 'deflate'
        r = requests.post('http://httpbin.org/post', data=p.body, headers=p.headers)
        assert data == json.loads(r.content.decode())['data']
    
    _test_compress_request_impl('foo bar')
    _test_compress_request_impl('foo bar baz')
    _test_compress_request_impl('foo bar baz gez')


# Generated at 2022-06-13 22:47:17.917830
# Unit test for function get_multipart_data_and_content_type
def test_get_multipart_data_and_content_type():
    upload_data = {
        'file': (
            'httpie.ini', 
            'Hello world', 
            'text/plain'
        ),
        'json': (None, json.dumps({'hello': 'world'}), 'application/json')
    }
    file_content = 'Hello world'

    multipart_data, content_type = get_multipart_data_and_content_type(upload_data)
    multipart_file = multipart_data.fields['file']
    assert(multipart_file.data == file_content)
    assert(multipart_file.content_type == 'text/plain')
    assert('boundary=' in content_type)

# Generated at 2022-06-13 22:47:28.555762
# Unit test for function prepare_request_body
def test_prepare_request_body():
    def callback(input):
        return input

    body1 = 'hello world'
    body2 = RequestDataDict({'key':'value'})
    body3 = 'hello'
    body4 = MultipartEncoder({'key':'value'})

    assert body1 == prepare_request_body(
        body1,
        body_read_callback=callback,
        chunked=False,
        offline=False
    )

    assert body3 == prepare_request_body(
        body3,
        body_read_callback=callback,
        chunked=True,
        offline=False
    )

    assert body4 == prepare_request_body(
        body4,
        body_read_callback=callback,
        chunked=True,
        offline=False
    )

    assert body2 == prepare_request_body

# Generated at 2022-06-13 22:47:32.596938
# Unit test for function compress_request
def test_compress_request():
    headers = {'Content-Type': 'application/json'}
    body = '{"test": "abcde"}'
    request = requests.Request('GET', 'https://httpbin.org/', headers=headers, data=body)
    request = request.prepare()
    compress_request(request, True)
    assert request.headers['Content-Encoding'] == 'deflate'

# Generated at 2022-06-13 22:47:41.484348
# Unit test for function compress_request
def test_compress_request():
    request = requests.Request(
        'POST',
        'http://httpbin.org/post',
        data={'abc': 'xyz'},
        headers={'Content-Type': 'application/json'},
    )
    request = request.prepare()
    compress_request(request, True)
    assert request.headers['Content-Encoding'] == 'deflate'
    assert request.headers['Content-Length'] == '27'
    assert request.body == b'x\x9c\xeb\xcfO\xcd\xc9\xc9\xa7\x01\x00\x89\x04\x04\x00\x00\x00'

# Generated at 2022-06-13 22:47:45.942530
# Unit test for function prepare_request_body
def test_prepare_request_body():
    assert prepare_request_body(
        'abc',
        body_read_callback=lambda x: 'abc',
        chunked=False,
        offline=True,
    ) == 'abc'

# Generated at 2022-06-13 22:47:49.385959
# Unit test for function prepare_request_body
def test_prepare_request_body():
    body = 'aaaaaaa'
    def callback(chunk):
        pass
    offline = True
    assert prepare_request_body(body=body, body_read_callback=callback, offline=offline) == body

# Generated at 2022-06-13 22:47:55.431192
# Unit test for function prepare_request_body
def test_prepare_request_body():
    body = 'test'

    response = prepare_request_body(
        body=body,
        body_read_callback=lambda x: x,
        content_length_header_value=None,
        chunked=False,
        offline=True
    )

    assert response == 'test'



# Generated at 2022-06-13 22:47:57.394763
# Unit test for method __iter__ of class ChunkedMultipartUploadStream
def test_ChunkedMultipartUploadStream___iter__():
    print(ChunkedMultipartUploadStream.__dict__)
    return None


if __name__ == '__main__':
    test_ChunkedMultipartUploadStream___iter__()

# Generated at 2022-06-13 22:48:04.843372
# Unit test for function prepare_request_body
def test_prepare_request_body():
        body = prepare_request_body('body',None,None,False,False)
        assert(body == 'body')


# Generated at 2022-06-13 22:48:06.375604
# Unit test for function prepare_request_body
def test_prepare_request_body():
    pass


# Generated at 2022-06-13 22:48:18.176931
# Unit test for method __iter__ of class ChunkedMultipartUploadStream
def test_ChunkedMultipartUploadStream___iter__():
    import pytest
    import requests_toolbelt.multipart
    import requests
    boundary = b'-----------------------------168072824752491622650073'
    # Create a sample multipart-encoded request body
    encoder = requests_toolbelt.multipart.encoder.MultipartEncoder(
        fields=[
            ('foo', 'a' * 100000),
            ('bar', 'b' * 100000),
        ],
        boundary=boundary,
    )
    # Get sample chunks to be sent
    chunks = []
    for chunk in encoder:
        chunks.append(chunk)
    # Create a requests.PreparedRequest instance for this sample request body

# Generated at 2022-06-13 22:48:25.234851
# Unit test for function compress_request
def test_compress_request():
    request = requests.PreparedRequest()
    request.body = b'1234567890'
    request.headers['Content-Length'] = '10'
    compress_request(request,True)
    assert request.body == b'x\x9c\xcbH,V\xcd\xc9\xc9W(F\xcaK\xcc\xcf/\x00\x82\x01'

# Generated at 2022-06-13 22:48:32.467699
# Unit test for function compress_request
def test_compress_request():
    data = {
        'first_name': 'Donald',
        'last_name': 'Trump',
        'age': 74,
        'president': True
    }
    req = requests.Request('POST', 'http://gordon.dev', json=data)
    prepared_req = req.prepare()

    data_size_before_compression = len(prepared_req.body)
    compress_request(prepared_req, always=True)
    data_size_after_compression = len(prepared_req.body)

    if data_size_before_compression < data_size_after_compression:
        exit(1)

# Generated at 2022-06-13 22:48:39.098483
# Unit test for function compress_request
def test_compress_request():
    data = "This is the request body"
    request = requests.Request('POST', 'http://www.example.com', data=data)
    prepared_request = request.prepare()
    print("Compressed Request:")
    compress_request(prepared_request, False)
    print(prepared_request)
    print("Body of Request:")
    print(prepared_request.body)


# Generated at 2022-06-13 22:48:47.470986
# Unit test for function prepare_request_body
def test_prepare_request_body():
    # test for non-file-like body
    body = '12345'
    expected = ChunkedUploadStream(
        stream=(chunk.encode() for chunk in [body]),
        callback=None,
    )
    assert prepare_request_body(body, chunked=True) == expected

    # test for file-like body
    body = io.BytesIO(b'12345')
    expected = ChunkedUploadStream(
        stream=body,
        callback=None,
    )
    assert prepare_request_body(body, chunked=True) == expected

    # test for urlencoded body
    body = RequestDataDict({'key': 'value'})
    expected = urlencode(body, doseq=True)
    assert prepare_request_body(body, chunked=True) == expected

    # test

# Generated at 2022-06-13 22:48:54.793768
# Unit test for function compress_request
def test_compress_request():
    request = requests.PreparedRequest()
    request.body = "Hello World"
    compress_request(request,False)

    assert len(request.body) < len("Hello World") == True
    assert "deflate" in request.headers['Content-Encoding'] == True
    assert "Hello World" not in str(request.body) == True
    assert len(request.body) == len(str(request.body)) == True

# Generated at 2022-06-13 22:49:01.098572
# Unit test for function get_multipart_data_and_content_type
def test_get_multipart_data_and_content_type():
    test_data = {'test': 'test_data'}
    test_content_type = 'multipart/form-data'
    test_boundary = '123456'
    result = get_multipart_data_and_content_type(test_data, test_boundary, test_content_type)
    assert result[1] == f'{test_content_type}; boundary={test_boundary}'

# Generated at 2022-06-13 22:49:08.746967
# Unit test for method __iter__ of class ChunkedMultipartUploadStream
def test_ChunkedMultipartUploadStream___iter__():
    """
    Unit test for method __iter__ of class ChunkedMultipartUploadStream
    """
    import json
    import tempfile

    temp = tempfile.TemporaryFile('w+')
    temp.write('test')
    temp.seek(0)

    data = {'test': 'true'}
    data['testdata'] = 'testfile'
    data['testfile'] = (temp.name, temp)
    headers={'Accept': 'application/json'}
    encoder = MultipartEncoder(fields=data.items())

    chunkedmultipartuploadstream = ChunkedMultipartUploadStream(encoder=encoder)
    for chunk in chunkedmultipartuploadstream:
        print(chunk.decode())


# Generated at 2022-06-13 22:49:21.519017
# Unit test for function prepare_request_body
def test_prepare_request_body():
    def on_body_read(chunk):
        print(chunk)

    encoder = MultipartEncoder(
        fields={"field1": "value1", "field2": "value2"},
        boundary='bWl0aG9k',
    )
    body = encoder

    rb = prepare_request_body(
        body,
        on_body_read,
        chunked=False,
    )
    print(rb)

    # stdout
    # b'--bWl0aG9k\r\nContent-Disposition: form-data; name="field1"\r\n\r\nvalue1\r\n--bWl0aG9k\r\nContent-Disposition: form-data; name="field2"\r\n\r\nvalue2\

# Generated at 2022-06-13 22:49:29.344162
# Unit test for method __iter__ of class ChunkedMultipartUploadStream
def test_ChunkedMultipartUploadStream___iter__():
    def check_iter(cb):
        target = ChunkedMultipartUploadStream(encoder)
        iterator = target.__iter__()
        cb(iterator)

    encoder = MultipartEncoder()
    check_iter(lambda iterator: assert_equal(False, iterator.__next__()))
    encoder = MultipartEncoder(fields={})
    check_iter(lambda iterator: assert_equal(False, iterator.__next__()))
    encoder = MultipartEncoder(fields={'k': 'v'})
    check_iter(lambda iterator: assert_equal(b'', iterator.__next__()))

# Generated at 2022-06-13 22:49:38.212552
# Unit test for function get_multipart_data_and_content_type
def test_get_multipart_data_and_content_type():
    data = {
        'a': 'b',
        'c': 'd',
    }

    _, content_type = get_multipart_data_and_content_type(data)
    assert content_type in (
        'multipart/form-data; boundary=------------------------f79d947b12f1457f',
        'multipart/form-data; boundary=------------------------647b6c5f6a09aa6e',
    )

    _, content_type = get_multipart_data_and_content_type(
        data, boundary='foo', content_type='',
    )
    assert content_type == 'multipart/form-data; boundary=foo'


# Generated at 2022-06-13 22:49:47.213777
# Unit test for function compress_request
def test_compress_request():
    simple_request = {
        'method': 'POST',
        'url': 'http://temp.com',
        'headers': {
            'Accept': '*/*',
            'User-Agent': 'Fake'
        },
        'body': 'test'
    }
    test_request = requests.Request(**simple_request).prepare()
    compress_request(test_request, True)
    actual_result = {
        'method': test_request.method,
        'url': test_request.url,
        'headers': test_request.headers,
        'body': test_request.body
    }

# Generated at 2022-06-13 22:49:51.394579
# Unit test for function compress_request
def test_compress_request():
    # test_compress_request()
    request = requests.PreparedRequest()
    request.body = "Simple body"
    request.headers['Content-Length'] = len(request.body)

    # check deflate works as expected
    compress_request(request, True)
    deflated_data = zlib.compress(request.body.encode())
    assert request.body == deflated_data

    # check that if no compression is needed (original data size is smaller)
    # we do not compress it
    compress_request(request, False)
    deflated_data = zlib.compress(request.body.encode())
    assert request.body != deflated_data

    # check that if no compression is needed (original data size is smaller)
    # but always == True we still compress it

# Generated at 2022-06-13 22:50:01.254518
# Unit test for function compress_request
def test_compress_request():
    post_data = 'Num=12&Name=Alice'
    post_url = 'http://httpbin.org/post'
    r = requests.Request('POST', post_url, data=post_data)
    prepped = r.prepare()
    compress_request(request=prepped, always=False)
    is_economical = (len(prepped.body) < len(post_data))
    assert prepped.body != post_data
    assert is_economical
    assert prepped.headers['Content-Encoding'] == 'deflate'
    assert int(prepped.headers['Content-Length']) == len(prepped.body)
    s = requests.Session()
    s.send(prepped)

# Generated at 2022-06-13 22:50:08.639515
# Unit test for function prepare_request_body
def test_prepare_request_body():
    import filecmp
    from requests_toolbelt import MultipartEncoder
    from os import remove, path
    from httpie.cli import parser
    from httpie.cli.dicts import RequestDataDict

    data = RequestDataDict([('1', 1), ('2', 2)])
    stream = open('test/test.jpg', 'rb')
    data_dict = {'a': 1, 'b': 2}
    request_data_dict = data
    multipart_data_dict = {'a': 1, 'b': open('test/test.jpg', 'rb')}
    multipart_data = MultipartEncoder(multipart_data_dict)

    body = prepare_request_body(data, parser.test_data_read_cb, False, False)

# Generated at 2022-06-13 22:50:20.979962
# Unit test for function prepare_request_body
def test_prepare_request_body():
    body = prepare_request_body(body="This is body", body_read_callback=None, content_length_header_value=None, chunked=False, offline=False)
    assert body == "This is body"

    body = prepare_request_body(body="This is body", body_read_callback=None, content_length_header_value=None, chunked=True, offline=False)
    assert body != "This is body"

    body = prepare_request_body(body="This is body", body_read_callback=None, content_length_header_value=None, chunked=False, offline=True)
    assert body == "This is body"


# Generated at 2022-06-13 22:50:26.304803
# Unit test for method __iter__ of class ChunkedMultipartUploadStream
def test_ChunkedMultipartUploadStream___iter__():
    import StringIO

    body = StringIO.StringIO()
    body.write('I am a test message')

    multipart = ChunkedMultipartUploadStream(content_type="application/octet-stream", body=body)
    for i in multipart:
        print(i)
    
    

# Generated at 2022-06-13 22:50:26.818914
# Unit test for function prepare_request_body
def test_prepare_request_body():
    pass

# Generated at 2022-06-13 22:50:43.398047
# Unit test for function compress_request
def test_compress_request():
    request = requests.PreparedRequest()
    val = "Test string"
    request.body = val
    request.headers = {}
    compress_request(request, True)
    assert request.headers['Content-Encoding'] == 'deflate'
    assert request.headers['Content-Length'] == '27'
    assert request.body != val

# Generated at 2022-06-13 22:50:48.270205
# Unit test for method __iter__ of class ChunkedUploadStream
def test_ChunkedUploadStream___iter__():
    stream = ['a', 'b', 'c', 'd']
    callback_list = []
    result_list = []

    def callback(chunk):
        callback_list.append(chunk)

    chunked_upload_stream = ChunkedUploadStream(stream, callback)
    for item in chunked_upload_stream:
        result_list.append(item)

    assert callback_list == result_list
    assert callback_list == stream



# Generated at 2022-06-13 22:50:54.245404
# Unit test for function compress_request
def test_compress_request():
    # Request with body
    r = requests.Request(method='POST', url='http://example.org', headers={}, data='Hello World!')
    p = r.prepare()
    compress_request(p, False)
    print(p.body)
    print(p.headers['Content-Length'])


# Generated at 2022-06-13 22:50:57.473380
# Unit test for method __iter__ of class ChunkedMultipartUploadStream
def test_ChunkedMultipartUploadStream___iter__():
    a = MultipartEncoder(fields={'a':'b'})
    b = ChunkedMultipartUploadStream(a)
    assert len(b) == 32

# Generated at 2022-06-13 22:51:04.618060
# Unit test for function compress_request
def test_compress_request():
    raw_request = requests.PreparedRequest()
    raw_request.body = '{"name":"foo","age":3}'
    raw_request.headers = {'Content-Type':'application/json'}
    expected_request = requests.PreparedRequest()
    expected_request.body = zlib.compress(raw_request.body.encode())
    expected_request.headers = {'Content-Type':'application/json',
                                'Content-Encoding': 'deflate',
                                'Content-Length': str(len(expected_request.body))}
    compress_request(raw_request, True)
    assert raw_request.body == expected_request.body, 'not match'
    assert raw_request.headers == expected_request.headers, 'not match'

# Generated at 2022-06-13 22:51:15.585527
# Unit test for method __iter__ of class ChunkedMultipartUploadStream
def test_ChunkedMultipartUploadStream___iter__():
    # create MultipartEncoder
    fields = [('field1', 'value1'), ('field2', 'value2')]
    en = MultipartEncoder(fields)
    # create ChunkedMultipartUploadStream
    chunked_upload_stream = ChunkedMultipartUploadStream(en)
    # test whether the result of ChunkedMultipartUploadStream.__iter__ can
    # be used to generate a string for the request body
    body = ''.join([chunk.decode() for chunk in chunked_upload_stream])
    assert body == en.to_string()
    # test whether the result of ChunkedMultipartUploadStream.__iter__ is
    # equal to the content of MultipartEncoder

# Generated at 2022-06-13 22:51:22.262795
# Unit test for method __iter__ of class ChunkedUploadStream
def test_ChunkedUploadStream___iter__():
    # Stream that returns each byte of a string following by EOF
    stream = (b'\x01\x02\x03\x04\x05',)

    # Callback that add 1 to each byte read, but that doesn't change the chunk
    callback = lambda x: x

    # Array to hold chunks read
    chunks = []

    # This is the stream, that returns each byte until EOF
    chunked_stream = ChunkedUploadStream(stream, callback)

    # Test that a chunk is received and add it to the chunks array
    assert next(chunked_stream) not in chunks
    chunks.append(next(chunked_stream))
    assert chunks[0] == b'\x01\x02\x03\x04\x05'

    # Test that EOF is returned

# Generated at 2022-06-13 22:51:29.745380
# Unit test for method __iter__ of class ChunkedMultipartUploadStream
def test_ChunkedMultipartUploadStream___iter__():
    import requests_toolbelt
    from requests_toolbelt.multipart.encoder import MultipartEncoderMonitor

    data = MultipartRequestDataDict(
        {'abc': 'abc'}
    )
    encoder = MultipartEncoder(
        fields=data.items(),
        boundary=requests_toolbelt.multipart.encoder.MultipartEncoder.ENCODE_TEMPLATE.format(int(time.time())).encode()
    )
    monitor = MultipartEncoderMonitor(encoder)
    iterator = ChunkedMultipartUploadStream(monitor)
    assert next(iterator) == monitor.read(ChunkedMultipartUploadStream.chunk_size)
    assert isinstance(iterator, ChunkedMultipartUploadStream)

# Generated at 2022-06-13 22:51:36.393269
# Unit test for function compress_request
def test_compress_request():
    class MockPreparedRequest(object):
        def __init__(self):
            self.body = b'hello'
        def headers(self):
            return {'Content-Length': 5,
                    'Content-Encoding': 'identity'}
    request = MockPreparedRequest()
    compress_request(request, always=True)
    assert request.headers['Content-Length'] == '3'
    assert request.headers['Content-Encoding'] == 'deflate'

# Generated at 2022-06-13 22:51:44.197337
# Unit test for function compress_request
def test_compress_request():
    class MockResponse:
        def __init__(self, status_code):
            self.status_code = status_code

    class MockRequest:
        def __init__(self, body):
            self.body = body
            self.headers = {}

        def prepare(self):
            return MockResponse(200)

    # http://blog.doughellmann.com/2013/06/pymotw-unittest-mock-patch-decorator.html
    def test_compress_request_should_call_compresses_request_body(self):
        with patch('httpie.client.utils.zlib.compressobj') as mock_compressobj:
            compress_request(MockRequest(body='test'), True)
            self.assertTrue(mock_compressobj.called)
            self.assertE

# Generated at 2022-06-13 22:52:07.996293
# Unit test for function get_multipart_data_and_content_type
def test_get_multipart_data_and_content_type():
    from httpie.cli.dicts import MultipartRequestDataDict
    data = MultipartRequestDataDict([
        ("key1", "value1"),
        ("key2", None),
        ("key3", ["value3a", "value3b"])
    ])
    content_type = None
    data, content_type = get_multipart_data_and_content_type(data, content_type)
    assert content_type == data.content_type
    # content_type = 'text'
    # data, content_type = get_multipart_data_and_content_type(data, content_type)
    # assert content_type == data.content_type

# Generated at 2022-06-13 22:52:13.978485
# Unit test for function prepare_request_body
def test_prepare_request_body():
    body = "test_body"
    body_read_callback = lambda bytes: print(bytes)
    content_length_header_value = 10
    chunked=False
    offline=False

    ret = prepare_request_body(
        body,
        body_read_callback,
        content_length_header_value,
        chunked,
        offline
    )
    assert ret == body

    body = "abcd"
    body_read_callback = lambda bytes: print(bytes)
    content_length_header_value = 10
    chunked = True
    offline = False

    ret = prepare_request_body(
        body,
        body_read_callback,
        content_length_header_value,
        chunked,
        offline
    )
    assert not hasattr(ret, "read")
    assert isinstance

# Generated at 2022-06-13 22:52:20.444302
# Unit test for function compress_request
def test_compress_request():
    data = {'json': '{"a": "b"}'}
    request = requests.Request('POST', 'http://kennethreitz.com', data=data).prepare()
    # Test zipping of request body with Content-Type: 'application/json'
    compress_request(request, False)
    assert request.headers['Content-Encoding'] == 'deflate'
    assert request.headers['Content-Length'] != str(len(data))


# Generated at 2022-06-13 22:52:30.592887
# Unit test for function compress_request
def test_compress_request():
    data = b'blahblahblahblahblah'
    deflater = zlib.compressobj()
    deflated_data = deflater.compress(data)
    deflated_data += deflater.flush()
    m = MultipartEncoder(
        fields = [
            ('field1', 'value'),
            ('field2', 'value'),
            ('field3', 'value'),
        ],
        boundary='boundary'
        )
    m2 = MultipartEncoder(
        fields = [
            ('field1', 'value'),
            ('field2', 'value'),
            ('field3', 'value'),
        ],
        boundary='boundary'
    )
    req = requests.PreparedRequest()
    req.body = data

# Generated at 2022-06-13 22:52:38.178677
# Unit test for method __iter__ of class ChunkedUploadStream
def test_ChunkedUploadStream___iter__():
    # create a stream of 10 chunks
    stream=[i for i in range(10)]
    # create a function which returns the product of two arguments
    def func(chunk):
        return chunk*2
    # create a ChunkedUploadStream instance
    result = ChunkedUploadStream(stream, func)
    # __iter__ method of class ChunkedUploadStream return an iterable object
    assert hasattr(result.__iter__(), '__iter__')


# Generated at 2022-06-13 22:52:42.889135
# Unit test for function compress_request
def test_compress_request():
    data = 'Hello World!\n'
    deflater = zlib.compressobj()
    deflated_data = deflater.compress(data.encode())
    deflated_data += deflater.flush()

    request = requests.PreparedRequest()
    request.body = data
    compress_request(request, True)
    assert request.body == deflated_data


# Generated at 2022-06-13 22:52:47.380053
# Unit test for function compress_request
def test_compress_request():
    request_1 = {'aa': 'bb', 'cc': 'd d'}
    request_2 = {'aa': 'bb', 'cc': 'd d'}
    print(compress_request(request_1, request_2, True))

# Generated at 2022-06-13 22:52:49.363498
# Unit test for method __iter__ of class ChunkedUploadStream
def test_ChunkedUploadStream___iter__():
    chunked = ChunkedUploadStream(['hello', 'world!'], lambda x: print(x))
    assert list(chunked) == ['hello', 'world!']



# Generated at 2022-06-13 22:52:58.137793
# Unit test for function compress_request
def test_compress_request():
    headers = {
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
    }
    request = requests.Request(url="http://localhost:9999/",
                           headers=headers,
                           method="GET",
                           body='Hello').prepare()
    compress_request(request, True)
    print(request.headers)

# Generated at 2022-06-13 22:53:08.070913
# Unit test for function prepare_request_body
def test_prepare_request_body():
    data = [
        ('user', 'john'),
        ('passwd', 'pass'),
    ]

    original_data = urlencode(data, doseq=True)
    class FakeFile:
        def __init__(self):
            self.data = original_data
        def read(self):
            return self.data
    data_file = FakeFile()
    chunked_data_file = FakeFile()
    chunked_data_file.data = original_data

    read = 'to be or not to be'
    size = len(read)

    body_read_callback = (lambda data: None)

    # Test string
    body = urlencode(data, doseq=True)
    res = prepare_request_body(body, body_read_callback)
    assert res == body

    # Test string chunked


# Generated at 2022-06-13 22:53:31.325306
# Unit test for function compress_request
def test_compress_request():
    request = requests.Request('', 'http://httpbin.org/post')
    request = request.prepare()
    request.body = "hello httpie"
    compress_request(request, False)
    assert request.body == b'x\x9c\x03\x00\x00\x00\x00\x01\x04\x00\xbf\xff}\x04\x00\x00\x00'
    request = requests.Request('', 'http://httpbin.org/post')
    request = request.prepare()
    request.body = "hello httpie"
    compress_request(request, True)

# Generated at 2022-06-13 22:53:40.525738
# Unit test for function compress_request
def test_compress_request():
    url = 'http://httpbin.org/post'
    data = {'foo': 'bar'}
    request = requests.Request('POST', url=url, data=data).prepare()
    compress_request(request, always=True)

    print(request.headers)
    body = request.body
    inflated_data = zlib.decompress(body)
    print(inflated_data)

# Generated at 2022-06-13 22:53:53.599518
# Unit test for function prepare_request_body
def test_prepare_request_body():
    class FakeStream:
        def __init__(self):
            self.iter_count = 0

        def read(self):
            self.iter_count += 1
            if self.iter_count == 1:
                return "aaa"
            if self.iter_count == 2:
                return "bb"
            if self.iter_count == 3:
                return ""

    fake_stream = FakeStream()
    body = prepare_request_body(
        body=fake_stream,
        body_read_callback=lambda x: None,
        content_length_header_value=None,
        chunked=False,
        offline=False,
    )
    assert isinstance(body, FakeStream)
