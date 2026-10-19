

# Generated at 2022-06-14 07:11:32.212628
# Unit test for function parse_forwarded

# Generated at 2022-06-14 07:11:45.007329
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {}
    headers["X-Forwarded-For"] = "127.0.0.1"
    config = {"PROXIES_COUNT": 0, "FORWARDED_FOR_HEADER": "X-Forwarded-For"}
    ret = parse_xforwarded(headers, config)
    assert ret == {}

    headers = {}
    headers["X-Forwarded-For"] = "127.0.0.1"
    config = {"PROXIES_COUNT": 1, "FORWARDED_FOR_HEADER": "X-Forwarded-For"}
    ret = parse_xforwarded(headers, config)
    assert ret == {}

    headers = {}
    headers["X-Forwarded-For"] = "127.0.0.1"

# Generated at 2022-06-14 07:11:55.978032
# Unit test for function fwd_normalize
def test_fwd_normalize():
    from pprint import pprint
    from .constants import REAL_IP_HEADER, FORWARDED_SECRET


# Generated at 2022-06-14 07:12:00.989708
# Unit test for function parse_content_header
def test_parse_content_header():
    assert parse_content_header('form-data; name=upload; filename="file.txt"') == ('form-data', {'name': 'upload', 'filename': 'file.txt'})


# Generated at 2022-06-14 07:12:11.624240
# Unit test for function fwd_normalize_address

# Generated at 2022-06-14 07:12:24.283328
# Unit test for function parse_forwarded
def test_parse_forwarded():
    headers = [
        "for=192.0.2.60;proto=http;host=example.com;by=203.0.113.43, for=192.0.2.43"
    ]
    config = {"FORWARDED_SECRET": "secret"}

    result = parse_forwarded(headers, config)
    assert result == {
        "for": "192.0.2.43",
        "proto": "http",
        "host": "example.com",
        "by": "203.0.113.43",
    }
    headers = [
        "for=192.0.2.43, for=198.51.100.17;proto=http;",
        "by=203.0.113.60, by=\"secret\""
    ]

# Generated at 2022-06-14 07:12:37.064432
# Unit test for function fwd_normalize
def test_fwd_normalize():
    pass
    # assert fwd_normalize([("host", "SITENAME.COM")]) == {'host': 'sitename.com'}
    # assert fwd_normalize([("for", "1.2.3.4")]) == {'for': '1.2.3.4'}
    # assert fwd_normalize([("FOR", "x.x.x.x")]) == {'for': 'x.x.x.x'}
    # assert fwd_normalize([("for", "::1")]) == {'for': '[::1]'}
    # assert fwd_normalize([("by", "x.x.x.x")]) == {'by': 'x.x.x.x'}
    # assert fwd_normalize([("by", "::1")]) == {'

# Generated at 2022-06-14 07:12:44.189137
# Unit test for function parse_content_header
def test_parse_content_header():
    # header_value param should be 'form-data; name=upload; filename=\"file.txt\"'
    header_value = "form-data; name=upload; filename=\"file.txt\""
    content_type, options = parse_content_header(header_value)
    assert content_type == "form-data"
    assert options["name"] == "upload"
    assert options["filename"] == "file.txt"

# Generated at 2022-06-14 07:12:47.876339
# Unit test for function parse_forwarded
def test_parse_forwarded():
    headers = {'forwarded':['for=198.51.100.17,for=192.0.2.60;proto=https;by=203.0.113.43']}
    config = {}
    config.SECRET = ''
    res = parse_forwarded(headers,config)
    assert res == {'for': '198.51.100.17', 'proto': 'https'}

# Generated at 2022-06-14 07:13:01.827499
# Unit test for function parse_forwarded

# Generated at 2022-06-14 07:13:12.722177
# Unit test for function fwd_normalize_address
def test_fwd_normalize_address():
    addr = '_1.2.3.4'
    normalize = fwd_normalize_address(addr)
    assert normalize == '_1.2.3.4'

# Generated at 2022-06-14 07:13:25.971310
# Unit test for function parse_forwarded
def test_parse_forwarded():
    assert parse_forwarded(None, {}) is None
    assert parse_forwarded({}, {}) is None
    assert parse_forwarded({}, {"FORWARDED_SECRET": None}) is None

    # Any forward won't pass without a valid secret
    assert parse_forwarded({"forwarded": "unknown,by=unknown"}, {}) is None
    assert parse_forwarded(
        {"forwarded": "secret=\"secret\";for=10.0.0.1"}, {}
    ) is None
    assert parse_forwarded(
        {"forwarded": "for=10.0.0.1,by=\"secret\""}, {}
    ) is None

    # Parse a forward with a valid secret

# Generated at 2022-06-14 07:13:38.818907
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    sample_headers = {
        "X-Forwarded-For": "10.0.0.1,10.0.0.2,10.0.0.3",
        "X-Forwarded-Host": "test.example.com:443",
        "X-Forwarded-Port": "80",
        "X-Forwarded-Proto": "https",
        "X-Scheme": "http",
        "X-Forwarded-Path": "/path/",
    }
    config = {"REAL_IP_HEADER": None, "PROXIES_COUNT": 3}

# Generated at 2022-06-14 07:13:45.018272
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {
        'X-Forwarded-Host': 'localhost',
        'X-Forwarded-Proto': 'https',
        'X-Forwarded-Path': '/home'
    }
    class Config:
        REAL_IP_HEADER = ''
        PROXIES_COUNT = ''
        FORWARDED_FOR_HEADER = 'X-Forwarded-For'

    config = Config()

    assert parse_xforwarded(headers, config) == {
        'for': 'localhost',
        'proto': 'https',
        'path': '/home'
    }



# Generated at 2022-06-14 07:13:55.803773
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {
        "x-scheme": "https",
        "x-forwarded-host": "proxy.example.com",
        "x-forwarded-path": "/path/file1",
        "x-forwarded-port": "9000"
    }
    print(parse_xforwarded(headers))
    # {'proto': 'https', 'host': 'proxy.example.com', 'path': '/path/file1', 'port': '9000'}
    assert parse_xforwarded(headers) == {'proto': 'https', 'host': 'proxy.example.com', 'path': '/path/file1', 'port': '9000'}

# Generated at 2022-06-14 07:14:08.536385
# Unit test for function parse_forwarded
def test_parse_forwarded():
    assert parse_forwarded(["forwarded: by=secret1; secret=secret1; by=secret2"], {'FORWARDED_SECRET': 'secret1'}) == {"by": "secret2", "secret":  "secret1"}
    assert parse_forwarded(["forwarded: by=secret1; secret=secret1; by=secret2"], {'FORWARDED_SECRET': 'secret2'}) == {"by": "secret2", "secret":  "secret1"}
    assert parse_forwarded(["forwarded: by=secret1; secret=secret2; by=secret2"], {'FORWARDED_SECRET': 'secret2'}) is None
    assert parse_forwarded(["forwarded: by=secret1; secret=secret2; by=secret2"], {'FORWARDED_SECRET': 'secret1'}) is None

# Generated at 2022-06-14 07:14:21.778991
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {"X-Scheme": "http",
               "X-Forwarded-For": "192.168.0.1, 10.0.0.1, , , 192.168.0.1, 10.0.0.1",
               "X-Forwarded-Host": "www.example.com",
               "X-Forwarded-Port": "80",
               "X-Forwarded-Path": "/"
               }

    expected_result = {"for": "10.0.0.1",
                       "proto": "http",
                       "host": "www.example.com",
                       "port": 80,
                       "path": "/"
                       }
    proxies_count = 2
    result = parse_xforwarded(headers, proxies_count)
    assert expected_result == result


# Generated at 2022-06-14 07:14:31.612440
# Unit test for function fwd_normalize

# Generated at 2022-06-14 07:14:43.816285
# Unit test for function parse_forwarded
def test_parse_forwarded():
    import sys
    sys.path.append("/Users/mengwang/Coding/Python/Sanic")
    import sanic.config
    config = sanic.config.Config()
    config.FORWARDED_SECRET = ""
    headers_no_secrets = {"forwarded": "By=192.0.2.60;For=\"[2001:db8:cafe::17]:4711\";Proto=https"}
    headers_with_secrets = {"forwarded": "proto=https,by=192.0.2.43,for=\"[2001:db8:cafe::17]:4711\""}
    assert parse_forwarded(headers_no_secrets, config) == None

# Generated at 2022-06-14 07:14:53.673699
# Unit test for function parse_forwarded
def test_parse_forwarded():
    header = "for=192.0.2.60; proto=http; by=203.0.113.43, for=192.0.2.61; proto=http; by=203.0.113.42, for=192.0.2.43; proto=http; by=203.0.113.43"
    secret = "secret"
    test = parse_forwarded(header,secret)
    t = {'for': '192.0.2.43', 'proto': 'http', 'by': '203.0.113.43'}
    if(test != t):
        print("ERROR: test_parse_forwarded")

# Generated at 2022-06-14 07:15:31.246007
# Unit test for function fwd_normalize
def test_fwd_normalize():
    assert fwd_normalize_address("ABcD") == "abcd"
    assert fwd_normalize_address("ABcD:1234:5678") == "[abcd:1234:5678]"
    assert fwd_normalize_address("_abcd:1234:5678") == "_abcd:1234:5678"
    assert fwd_normalize(("key", "value")) == {"key": "value"}
    assert fwd_normalize([("key", "value")]) == {"key": "value"}
    assert fwd_normalize(("KEY", "value")) == {"key": "value"}
    assert fwd_normalize(("key", "VALUE")) == {"key": "value"}

# Generated at 2022-06-14 07:15:39.276935
# Unit test for function parse_forwarded
def test_parse_forwarded():
    """Sanity check for the parse_forwarded function. Assertions do not
    guarantee the best
    possible parsing result, but provides some clues about how we expect
    the function to behave.
    """
    from sanic.request import Request

    request = Request({}, None)
    request.app = Mock()

    # Basic test
    request.app.config = {
        'FORWARDED_SECRET':'secret'
    }
    request.headers = {'forwarded':'By=1234; Host="example.org"; Secret=secret, By=1.2.3.4; For="10.0.0.2"; Host="new.example.org"; Secret=secret, For="[::1]"; Proto=https'}
    fwd = parse_forwarded(request.headers, request.app.config)
    assert fwd

# Generated at 2022-06-14 07:15:51.996557
# Unit test for function fwd_normalize_address
def test_fwd_normalize_address():
    assert fwd_normalize_address("unknown") == "_unknown"
    assert fwd_normalize_address("127.0.0.1") == "127.0.0.1"
    assert fwd_normalize_address("127.0.0.1%foo") == "127.0.0.1%foo"
    assert fwd_normalize_address("2001:cdba:0000:0000:0000:0000:0000:3257") ==\
        "2001:cdba:0000:0000:0000:0000:0000:3257"
    assert fwd_normalize_address("2001:cdba:0000:0000:0000:0000:0000:3257-foo") == \
        "2001:cdba:0000:0000:0000:0000:0000:3257-foo"

# Generated at 2022-06-14 07:16:06.002461
# Unit test for function parse_host
def test_parse_host():
    assert parse_host("localhost") == ('localhost', None)
    assert parse_host("127.0.0.1") == ('127.0.0.1', None)
    assert parse_host("[::1]") == ('[::1]', None)
    assert parse_host("test.test.test") == ('test.test.test', None)
    assert parse_host("localhost:80") == ('localhost', 80)
    assert parse_host("127.0.0.1:8080") == ('127.0.0.1', 8080)
    assert parse_host("[::1]:180") == ('[::1]', 180)
    assert parse_host("test.test.test:1337") == ('test.test.test', 1337)



# Generated at 2022-06-14 07:16:17.345860
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {"X-Forwarded-For": "1.2.3.4",
               "X-Forwarded-Ssl": "on",
               "X-Forwarded-Host": "other.example.com",
               "X-Forwarded-Port": "443",
               "X-Forwarded-Server": "webproxy",
               "X-Forwarded-Path": "/dir/page.html"}
    config = type("Config", (), {"PROXIES_COUNT": 1, "FORWARDED_FOR_HEADER": "X-Forwarded-For", "REAL_IP_HEADER": "X-Forwarded-For"})
    forward = parse_xforwarded(headers, config)
    assert forward["for"] == "1.2.3.4"
    assert forward["proto"] == "on"

# Generated at 2022-06-14 07:16:25.839443
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from sanic.request import Request
    from sanic import Sanic
    app = Sanic(__name__)

    @app.route("/")
    async def handler(request):
        return request.x_forwarded_for

    request, response = app.test_client.get(
        "/", headers={"X-Forwarded-For": "127.0.0.1"}
    )

    assert request.x_forwarded_for == "127.0.0.1"

# Generated at 2022-06-14 07:16:31.841592
# Unit test for function fwd_normalize
def test_fwd_normalize():
    options = [('key1', 'val1'), ('key2', 'val2'), ('key3', 'val3')]
    res = fwd_normalize(options)
    assert res['key1'] == 'val1'
    assert res['key2'] == 'val2'
    assert res['key3'] == 'val3'

# Generated at 2022-06-14 07:16:41.110908
# Unit test for function parse_host
def test_parse_host():
    assert parse_host("localhost:8080") == ('localhost', 8080)
    assert parse_host("localhost:8080") == ('localhost', 8080)
    assert parse_host("localhost") == ('localhost', None)
    assert parse_host("::1") == ('[::1]', None)
    assert parse_host("::1:8080") == ('[::1]', 8080)
    assert parse_host("[::1]") == ('[::1]', None)
    assert parse_host("[::1]:8080") == ('[::1]', 8080)
    assert parse_host("[[::1]]:8080") == (None, None)


if __name__ == "__main__":
    test_parse_host()

# Generated at 2022-06-14 07:16:46.813494
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from sanic.config import Config
    from sanic.request import Header
    config = Config()
    config.REAL_IP_HEADER = 'X-Real-IP'
    config.FORWARDED_FOR_HEADER = 'X-Forwarded-For'
    headers = Header()
    headers.add('X-Forwarded-For', '111.222.333.444')
    assert parse_xforwarded(headers, config) == {'for': '111.222.333.444'}

# Generated at 2022-06-14 07:16:57.809787
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from sanic.config import Config
    from sanic.request import Request, StreamBuffer
    from sanic.server import HttpProtocol
    from sanic.testing import HOST, PORT, create_server
    
    """
    Used to test parse_xforwarded code 
    """

    class TestConfig(Config):
        PROXIES_COUNT = 1
        REAL_IP_HEADER = 'x-forwarded-for'
        FORWARDED_FOR_HEADER = 'x-forwarded-for'

    async def handler(request):
        return text("OK")

    app = Sanic("test_parse_xforwarded")
    app.add_route(handler, "/")

    server, app, loop = create_server(TestConfig)

# Generated at 2022-06-14 07:17:25.347039
# Unit test for function parse_forwarded
def test_parse_forwarded():
    """Test for function parse_forwarded"""
    from .request import HttpHeaders

    fwd_header = {"forwarded": ["by=localhost;proto=https;for=192.168.64.1:8080"]}
    headers = HttpHeaders(fwd_header)
    options = parse_forwarded(headers, None)
    assert options["for"] == "[192.168.64.1]:8080"
    assert options["by"] == "localhost"
    assert options["proto"] == "https"

    fwd_header = {"forwarded": [
        "by=localhost;proto=https;for=192.168.64.1:",
        "by=localhost;proto=https;for=192.168.64.1"]}
    headers = HttpHeaders(fwd_header)
   

# Generated at 2022-06-14 07:17:38.657518
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from sanic.exceptions import InvalidUsage
    from sanic.request import Request
    from sanic.config import Config

    cookie_values = {
        "secret": "4c50d6ef-a6c0-4bc8-99c9-ca9d98838962",
        "max_age": "120",
        "version": "1",
        "payload": "eyJmb28iOiJiYXIifQ.",
        "signature": "v3qr3a75no"
    }

# Generated at 2022-06-14 07:17:47.441982
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    # Configure the function to parse X-Forwarded-For headers
    config = Dict()
    config.REAL_IP_HEADER = "X-Real-IP"
    config.FORWARDED_FOR_HEADER = "X-Forwarded-For"
    config.PROXIES_COUNT = 0
    
    # No headers
    headers = Dict()
    assert parse_xforwarded(headers, config) == None

    # Parse X-Forward-For: 1.1.1.1, 2.2.2.2, 3.3.3.3, 4.4.4.4
    headers = Dict()
    headers["X-Forwarded-For"] = "1.1.1.1, 2.2.2.2, 3.3.3.3, 4.4.4.4"
   

# Generated at 2022-06-14 07:17:53.925654
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from sanic import Sanic
    from sanic.config import Config
    from sanic.request import Request
    from io import BytesIO

    app = Sanic()
    c = Config()
    c.PROXIES_COUNT = 1
    # Add a dummy header to trigger X-Forwarded parsing
    c.REAL_IP_HEADER = "x-real-ip"
    c.FORWARDED_FOR_HEADER = "x-forwarded-for"

    @app.route("/")
    async def handler(request):
        return text("OK")

    class BytesIOWithLength(BytesIO):
        def __init__(self, value):
            BytesIO.__init__(self)
            self.value = value
            self.length = len(value)


# Generated at 2022-06-14 07:18:03.427126
# Unit test for function parse_forwarded

# Generated at 2022-06-14 07:18:09.114541
# Unit test for function parse_forwarded
def test_parse_forwarded():
	from sanic.config import Config
	from sanic.request import Headers
	config = Config()
	config.FORWARDED_SECRET = 'secret'
	headers = Headers()
	headers.add('Forwarded', 'for=\'127.0.0.1\'; for=\'127.0.0.2\'; by=\'secret\', for=\'127.0.0.3\'')
	out = parse_forwarded(headers, config)
	assert out['for'] == '127.0.0.1'

# Generated at 2022-06-14 07:18:20.004657
# Unit test for function fwd_normalize
def test_fwd_normalize():
    options = [
        ('for', '[::1]'),
        ('proto', 'https'),
        ('host', 'test.com'),
        ('port', '8090'),
        ('path', '/path'),
    ]

    option = fwd_normalize(options)
    assert option['for'] == '[::1]'
    assert option['proto'] == 'https'
    assert option['host'] == 'test.com'
    assert option['port'] == 8090
    assert option['path'] == '/path'


# Generated at 2022-06-14 07:18:29.346678
# Unit test for function parse_forwarded
def test_parse_forwarded():
    import copy
    from collections import OrderedDict
    parameters = OrderedDict()
    parameters["secret"] = "secret"
    parameters["by"] = "192.0.2.60"
    parameters["host"] = "example.com"
    parameters["proto"] = "http"
    parameters["for"] = "192.0.2.43, 198.51.100.17"
    parameters["proto"] = "https"
    parameters["path"] = "/"
    parameters["query"] = "arguments"

    params = copy.copy(parameters)
    options = None
    forward_header = ";".join(
        [key + "=" + params[key] for key in params.keys()])
    forward_header = "Forwarded: " + forward_header + "\n"

# Generated at 2022-06-14 07:18:37.062727
# Unit test for function fwd_normalize
def test_fwd_normalize():
    print('testing fwd_normalize')
    from types import GeneratorType
    
    def test_fwd_normalize(x, y=0):
        print('\nfwd_normalize(%s)' % str(x))
        z = fwd_normalize(x)
        print(str(z))
        if y != 0:
            assert z == y, "expected %s, got %s" % (str(y), str(z))
    
    test_fwd_normalize((('host', 'www.example.org'),('proto', 'http')))
    test_fwd_normalize((('proto', 'http'),('host', 'www.example.org')), {'proto':'http', 'host': 'www.example.org'})

# Generated at 2022-06-14 07:18:48.123605
# Unit test for function parse_forwarded
def test_parse_forwarded():
    # start up a sanic app
    app = Sanic('test_parse_forwarded')

    # test if FORWARDED_SECRET key is not in the headers
    req, res = app.test_client.get("/")
    assert parse_forwarded(req.headers, app.config) is None

    # test that a missing key of FORWARDED_SECRET in the first forward
    # doesn't return anything
    req, res = app.test_client.get("/", headers={"Forwarded":"badsecret, by=_forwarded_secret_key, for=127.0.0.1"})
    assert parse_forwarded(req.headers, app.config) is None

    # test that a missing key of FORWARDED_SECRET in the second forward
    # doesn't return anything
    req, res = app.test_

# Generated at 2022-06-14 07:19:05.458531
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = dict()
    ret = parse_xforwarded(headers, None)
    assert ret == None


# Generated at 2022-06-14 07:19:15.800458
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    import unittest


# Generated at 2022-06-14 07:19:27.777480
# Unit test for function parse_forwarded
def test_parse_forwarded():
    options = parse_forwarded(
        [
            "for=192.168.2.88;proto=http;by=secret",
            "for=\"192.168.2.88, 127.0.0.1\";proto=http;by=secret",
            "for=\"192.168.2.88, 127.0.0.1\";proto=http;by=wrong",
            "for=\"192.168.2.88, 127.0.0.1\";by=secret",
            "by=secret;for=192.168.2.88;proto=http",
            "by=wrong;for=192.168.2.88;proto=http",
        ],
        b"secret"
    )

# Generated at 2022-06-14 07:19:36.201587
# Unit test for function parse_forwarded
def test_parse_forwarded():
    from asynctest import TestCase as AsyncTestCase, mock as async_mock
    from asynctest.mock import CoroutineMock, patch
    from sanic.response import json

    class TestParseForwarded(AsyncTestCase):
        def setUp(self):
            self.app = Sanic("test_parse_forwarded")
            sanic_config.REQUEST_TIMEOUT = 60

        async def test_parse_forwarded_headers(self):
            from sanic.request import Header

            FWD = "for=192.0.2.60; proto=https; by=203.0.113.43"
            req = mock.MagicMock()
            req.headers = Header()
            req.headers["forwarded"] = FWD


# Generated at 2022-06-14 07:19:49.137613
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from .config import Config
    from .headers import HttpHeaders
    config = Config()
    config.FORWARDED_FOR_HEADER = 'X-Forwarded-For'
    config.REAL_IP_HEADER = 'X-Real-IP'
    config.PROXIES_COUNT = 3
    headers = HttpHeaders()
    headers['X-Real-IP'] = '192.0.2.10'
    headers['X-Forwarded-For'] = ['192.0.2.10', '198.51.100.70, 203.0.113.1', '127.0.0.1']
    assert parse_xforwarded(headers, config) == {'for': '127.0.0.1'}

if __name__ == "__main__":
    test_parse_xforwarded

# Generated at 2022-06-14 07:19:55.751239
# Unit test for function parse_forwarded
def test_parse_forwarded():
    hdr = " for=123.123.123.123, for=203.0.113.195, by=\"[::1]:5555\"; secret=foobar"
    fwd = parse_forwarded(hdr)
    assert fwd == {"for": '123.123.123.123', "by": "[::1]:5555"}

# Generated at 2022-06-14 07:20:09.524630
# Unit test for function parse_forwarded
def test_parse_forwarded():
    import requests
    import json

    data = json.loads(open('test_data.txt', 'r').read())
    data = data['parse_forwarded']

    def run_parse(header, result):
        config = requests.__config
        config.FORWARDED_SECRET = None
        assert requests.parse_forwarded({'forwarded': header}, config) is None

        config.FORWARDED_SECRET = result.pop('secret')
        assert requests.parse_forwarded({'forwarded': header}, config) == result

    for datum in data:
        if isinstance(datum, list):
            for d in datum:
                run_parse(d['header'], d['result'])
        else:
            run_parse(datum['header'], datum['result'])
    
    
# Unit

# Generated at 2022-06-14 07:20:21.710058
# Unit test for function parse_forwarded
def test_parse_forwarded():
    """ Test the function parse_forwarded in sanic.request """
    assert parse_forwarded({"forwarded": "by=yiyi"}, config=None) == {
        "by": "yiyi"
    }
    assert parse_forwarded(
        {"forwarded": "for=abc;proto=http;by=yiyi"}, config=None
    ) == {"by": "yiyi", "for": "abc", "proto": "http"}
    assert parse_forwarded({"forwarded": "by=yiyi;for=abc"}, config=None) is None
    assert parse_forwarded(
        {"forwarded": "by=yiyi;secret=abc;for=abc"}, config={"FORWARDED_SECRET":"abc"}
    ) == {"by": "yiyi", "for": "abc"}

# Generated at 2022-06-14 07:20:30.916205
# Unit test for function parse_forwarded
def test_parse_forwarded():
    assert parse_forwarded({"forwarded":"for=192.0.2.60;proto=http;by=http://example.com/forward, for=203.0.113.43, for=198.51.100.17;proto=https"}, config={'FORWARDED_SECRET':'http://example.com/forward'}) == {'proto': 'http', 'secret': 'http://example.com/forward', 'by': 'http://example.com/forward', 'for': '192.0.2.60'}

# Generated at 2022-06-14 07:20:43.128661
# Unit test for function parse_forwarded
def test_parse_forwarded():
    # Some secure tests on Forwarded parsing
    forwarded_true = [
        "for=192.0.2.60;proto=http;by=203.0.113.43;host=example.com",
        "for=192.0.2.43, for=198.51.100.17;host=example.net;secret=17Lj5F5f",
    ]
    forwarded_false = [
        "for=255.0.0.17;proto=http;by=203.0.113.43, for=192.0.2.43",
        "for=192.0.2.43, for=198.51.100.17;host=example.net;secret=",
    ]
    secret = "17Lj5F5f"

# Generated at 2022-06-14 07:21:15.795873
# Unit test for function parse_forwarded
def test_parse_forwarded():
    options = parse_forwarded(
        "for=192.0.2.60;proto=http;by=203.0.113.43",
        config.FORWARDED_SECRET,
    )
    assert options["for"] == "192.0.2.60"
    assert options["by"] == "203.0.113.43"
    assert options["proto"] == "http"

    options = parse_forwarded(
        "for=192.0.2.43, for=198.51.100.17",
        config.FORWARDED_SECRET,
    )
    assert options["for"] == "198.51.100.17"
    assert options["by"] == "192.0.2.43"
