

# Generated at 2022-06-14 07:11:32.160160
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {
        'X-scheme': 'http',
        'X-Forwarded-Host': 'www.sanic.com',
        'X-Forwarded-Path': '',
        'X-Forwarded-Port': '80',
        'X-Forwarded-Proto': 'https',
        'X-Real-Ip': '192.168.0.1'
    }
    config = {
        'FORWARDED_FOR_HEADER': 'X-Forwarded-For',
        'PROXIES_COUNT': 0,
        'FORWARDED_SECRET': None,
        'REAL_IP_HEADER': 'X-Real-Ip'
    }
    result = parse_xforwarded(headers, config)

# Generated at 2022-06-14 07:11:45.007159
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from sanic.request import Request
    from sanic.config import Config
    config = Config()
    config.PROXIES_COUNT = 0
    config.FORWARDED_FOR_HEADER = 'X-Forwarded-For'
    headers = {
        "X-Forwarded-For": "192.168.0.1",
        "X-Scheme": "http",
        "X-Forwarded-Host": "example.com",
        "X-Forwarded-Port": "8080",
        "X-Forwarded-Path": "/123"
        }
    request = Request("GET", "/", headers, config=config)
    assert request.scheme == "http"
    assert request.remote_addr == "192.168.0.1"
    assert request.host == "example.com"
    assert request.port

# Generated at 2022-06-14 07:11:50.136934
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    import asyncio
    from sanic.config import Config
    from sanic.request import Request
    from sanic.helpers import parse_xforwarded

    headers  = {'X-Forwarded-For': '10.32.0.1, 10.32.0.2, 10.32.0.3',
                'X-Forwarded-Proto': 'https',
                'X-Forwarded-Host': 'www.example.com, example.com',
                'X-Forwarded-Port': '80, 8080',
                'X-Forwarded-Path': '/api/v1, /api/v2'}
    config = Config()
    config.FORWARDED_FOR_HEADER = 'X-Forwarded-For'
    config.FORWARDED_FOR_HEADER_COUNT = 1
    config.FORWARD

# Generated at 2022-06-14 07:12:02.506915
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    assert parse_xforwarded({"X-Forwarded-For": "1.2.3.4"}, {}) == {"for": "1.2.3.4"}
    assert parse_xforwarded(
        {
            "X-Forwarded-For": "1.2.3.4",
            "X-Forwarded-Proto": "https",
            "X-Forwarded-Host": "example.com",
            "X-Forwarded-Port": "443",
        },
        {},
    ) == {
        "for": "1.2.3.4",
        "proto": "https",
        "host": "example.com",
        "port": 443,
    }

# Generated at 2022-06-14 07:12:12.388789
# Unit test for function fwd_normalize_address
def test_fwd_normalize_address():
     assert fwd_normalize_address("1.1.1.1") == "1.1.1.1"
     assert fwd_normalize_address("1:1:1:1:1:1:1:1") == "[1:1:1:1:1:1:1:1]"
     assert fwd_normalize_address("1:1:1:1::1:1") == "[1:1:1:1::1:1]"
     assert fwd_normalize_address("1:1:1:1::1:" + "0"*1000) == "[1:1:1:1::1:0]"
     assert fwd_normalize_address("1:1:1:1::1:0") == "[1:1:1:1::1:0]"
     assert fwd_normalize_address

# Generated at 2022-06-14 07:12:15.587821
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    is_ok = True
    ret = parse_xforwarded()
    #print("test_parse_xforwarded ret = [%s]" % (ret))
    if ret is None:
        is_ok = False
    return is_ok


# Generated at 2022-06-14 07:12:25.761722
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    config = Namespace(PROXIES_COUNT=3, REAL_IP_HEADER="X-Real-IP", FORWARDED_FOR_HEADER="X-Forwarded-For")
    if False:
        headers = {
            "X-Forwarded-For": "1.2.3.4, 192.168.1.1, 192.168.1.2, 192.168.1.3, 192.168.1.4"
        }

# Generated at 2022-06-14 07:12:38.178210
# Unit test for function parse_forwarded
def test_parse_forwarded():
    import asyncio
    from sanic import Sanic
    from sanic.response import json

    app = Sanic(__name__)

    @app.route('/')
    async def handler(request):
        return json({"get": request.headers.get('forwarded', None),
                     "all": request.headers.getall('forwarded', None),
                     "set": request.headers.set('forwarded', None),
                     "script_name": request.script_name,
                     "path": request.path})

    server = app.create_server(host="127.0.0.1", port=8000)
    asyncio.ensure_future(server)


# Generated at 2022-06-14 07:12:48.658368
# Unit test for function parse_content_header
def test_parse_content_header():
    if __name__ == "__main__":
        assert parse_content_header('form-data; name=upload; filename="file.txt"') == ('form-data', {'name': 'upload', 'filename': 'file.txt'})
        assert parse_content_header('form-data; name=upload; filename="file.txt"') == ('form-data', {'name': 'upload', 'filename': 'file.txt'})
        assert parse_content_header('form-data; name=upload; filename="file.txt"') == ('form-data', {'name': 'upload', 'filename': 'file.txt'})
        assert parse_content_header('form-data; name=upload; filename="file.txt"') == ('form-data', {'name': 'upload', 'filename': 'file.txt'})
        assert parse

# Generated at 2022-06-14 07:13:02.518564
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    dict = {
        'x-forwarded-for': '192.168.1.1, 192.168.1.2',
        'x-scheme': 'http',
        'x-forwarded-host': 'example.org',
        'x-forwarded-path': 'hello/world',
        'x-forwarded-port': '80',
    }
    config = {
        'PROXIES_COUNT': 2,
        'REAL_IP_HEADER': 'x-forwarded-for',
        'FORWARDED_FOR_HEADER': 'x-forwarded-for',
    }
    print(parse_xforwarded(dict, config))
    assert dict == parse_xforwarded(dict, config)

# Generated at 2022-06-14 07:13:19.183821
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {
        'x-scheme': 'https',
        'x-forwarded-port': '80',
        'x-forwarded-path': '',
        'x-forwarded-host': '127.0.0.1'
    }
    config = {
        'REAL_IP_HEADER': '',
        'PROXIES_COUNT': 1,
        'FORWARDED_FOR_HEADER': 'x-forwarded-for',
        'FORWARDED_SECRET': ''
    }
    result = parse_xforwarded(headers, config)
    assert result == {'for': '127.0.0.1', 'proto': 'https', 'port': 80}

# Generated at 2022-06-14 07:13:30.988552
# Unit test for function parse_forwarded
def test_parse_forwarded():
    import pytest
    headers = {
        'forwarded':
        [
            'For=192.0.2.43, '
            'For=198.51.100.17;proto=http;by=203.0.113.60, '
            'secret=secret'
        ]
    }

    config = SanicConfig(FORWARDED_SECRET='secret')

    assert parse_forwarded(headers, config) == {
        'for': '198.51.100.17',
        'proto': 'http',
        'by': '203.0.113.60'
    }

    config = SanicConfig(FORWARDED_SECRET='wrong secret')
    pytest.raises(AssertionError, parse_forwarded, headers, config)

# Generated at 2022-06-14 07:13:45.214226
# Unit test for function fwd_normalize
def test_fwd_normalize():
    def cmp(value):
        assert value == fwd_normalize(fwd_normalize(value))
    cmp([])
    cmp([("for", None)])
    cmp([("for", "example.com")])
    cmp([("proto", "http")])
    cmp([("proto", "http"), ("for", "example.com")])
    cmp([("proto", "http"), ("for", "127.0.0.1"), ("host", "foo")])
    cmp([("host", "foo")])
    cmp([("proto", "https"), ("host", "foo"), ("port", "443")])
    cmp([("proto", "https"), ("host", "foo"), ("port", 443)])

# Generated at 2022-06-14 07:13:57.331326
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    import random
    import string
    import sanic.utils
    from sanic.request import Request
    from sanic.config import Config

    class MockConfig(Config):
        def __init__(self, *args, **kwargs):
            for k, v in kwargs.items():
                setattr(self, k, v)

    def rand_string(length=10):
        """Return a random string with the combination of lowercase and uppercase letters """
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(length))
    
    forwarded_secret = rand_string()
    num_proxies = random.randint(0,10000)

# Generated at 2022-06-14 07:14:05.872968
# Unit test for function parse_forwarded
def test_parse_forwarded():
    from sanic import Sanic
    from sanic.config import Config
    from sanic.response import text

    app = Sanic(__name__)

    @app.route("/")
    async def test(request):
        return text("OK")

    config = Config()
    config.FORWARDED_SECRET = "asdf"
    request, response = app.test_client.get("/", headers={
        "Forwarded": "by=_forwarded; secret=asdf; for=_forwarded; proto=https; host=example.com; port=443; path=/test?q=1"
    })
    request.app = app
    request.app.config = config

# Generated at 2022-06-14 07:14:19.714719
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    class MockHeaders:
        def get(self, key):
            return self.dict.get(key)

        def getall(self, key):
            return self.dict.getall(key)

    class MockConfig:
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)


# Generated at 2022-06-14 07:14:30.496279
# Unit test for function parse_forwarded
def test_parse_forwarded():
    headers = {'forwarded': 'for=127.0.0.1;proto=https;by=192.168.1.1;secret=123'}
    config = {'FORWARDED_SECRET': "123"}
    assert parse_forwarded(headers, config) == {'for': '127.0.0.1', 'proto': 'https', 'by': '192.168.1.1'}
    config = {'FORWARDED_SECRET': "1234"}
    assert parse_forwarded(headers, config) == None
    headers = {'forwarded': 'for=6.6.6.6;proto=https;by=192.168.1.1;secret=123'}
    assert parse_forwarded(headers, config) == None

# Generated at 2022-06-14 07:14:37.806922
# Unit test for function parse_host
def test_parse_host():
    testcases = [
        ("localhost", ("localhost", None)),
        ("localhost:8080", ("localhost", 8080)),
        ("[::1]", ("[::1]", None)),
        ("[::1]:8080", ("[::1]", 8080)),
        ("[::1]:8080", ("[::1]", 8080)),
    ]

    for host, expected in testcases:
        assert parse_host(host) == expected

# Generated at 2022-06-14 07:14:44.425703
# Unit test for function parse_forwarded
def test_parse_forwarded():
    from sanic.testing import HOST

    headers = {"forwarded": f"by=127.0.0.1; for={HOST}, for=_foo"}
    config = AppConfig.load(
        testing=True, DEBUG=True, FORWARDED_FOR_HEADER="x-forwarded-for"
    )
    assert fwd_normalize(parse_forwarded(headers, config)) == {
        "by": "127.0.0.1",
        "for": HOST,
    }

    headers = {"forwarded": f"by=127.0.0.1, by=_bar; for=::1, for=_baz"}
    config = AppConfig.load(testing=True, DEBUG=True, FORWARDED_SECRET=None)
    assert parse_forwarded(headers, config) is None



# Generated at 2022-06-14 07:14:56.377850
# Unit test for function parse_forwarded
def test_parse_forwarded():
    import io
    from sanic.request import Request
    from sanic.config import Config

    # Taken from https://tools.ietf.org/html/rfc7239#section-5.1
    # Forwarded and X-Forwarded-For headers
    http_forwarded = """
Forwarded: for=198.51.100.17;by=203.0.113.43;proto=https;host=example.com
X-Forwarded-For: 2001:db8::c001, 10.0.0.1, 2002:c0a8:101::1
    """

    cfg = Config()
    cfg.FORWARDED_SECRET = "123456789"

# Generated at 2022-06-14 07:15:14.873716
# Unit test for function fwd_normalize
def test_fwd_normalize():
    assert fwd_normalize(
        (
            ("for", "123.123.123.123"),
            ("port", "123"),
            ("host", "hostname"),
            ("proto", "proto"),
            ("path", "/path/to/file.jpg"),
        )
    ) == {
        "for": "123.123.123.123",
        "port": 123,
        "host": "hostname",
        "proto": "proto",
        "path": "/path/to/file.jpg",
    }
    assert fwd_normalize(
        (
            ("for", 'unknown'),
            ("port", "invalid"),
            ("host", "hostname"),
            ("proto", "proto"),
            ("path", "/path/to/file.jpg"),
        )
    )

# Generated at 2022-06-14 07:15:21.875581
# Unit test for function fwd_normalize
def test_fwd_normalize():
    from sanic.exceptions import NotFound

    from . import test_utils
    from . import exceptions
    from . import request
    from . import response
    from . import config

    from .constants import HTTP_METHODS
    from .exceptions import ReqeustTimeout

    def test_fwd_normalize():
        assert fwd_normalize([]) == {}
        assert fwd_normalize([("by", "unknown")]) == {}
        assert fwd_normalize([("by", "1.2.3.4")])["by"] == "1.2.3.4"
        assert fwd_normalize([("by", "[::1]")])["by"] == "[::1]"
        assert fwd_normalize([("by", "2001:db8:a0b:12f0::1")])["by"]

# Generated at 2022-06-14 07:15:32.952548
# Unit test for function fwd_normalize_address
def test_fwd_normalize_address():
    assert fwd_normalize_address("aa:bb:cc:dd:ee:ff:00:11") == "[aa:bb:cc:dd:ee:ff:00:11]"
    assert fwd_normalize_address("2001:0db8:85a3:0000:0000:8a2e:0370:7334") == "[2001:0db8:85a3:0000:0000:8a2e:0370:7334]"
    assert fwd_normalize_address("2001:db8:85a3:0:0:8a2e:370:7334") == "[2001:db8:85a3:0:0:8a2e:370:7334]"

# Generated at 2022-06-14 07:15:40.573699
# Unit test for function parse_forwarded
def test_parse_forwarded():
    f1 = 'secret="foobar", by=_hidden, for=192.0.2.60, for="[2001:db8:cafe::17]"'
    f2 = 'by=_hidden, for=192.0.2.60, for="[2001:db8:cafe::17]" secret="foobar"'
    f3 = 'for="[2001:db8:cafe::17]", secret="foobar", by=_hidden, for=192.0.2.60'
    f4 = 'for="[2001:db8:cafe::17]", secret="foobar", for=192.0.2.60, by=_hidden'
    f5 = 'for="[2001:db8:cafe::17]", for=192.0.2.60, secret="foobar", by=_hidden'


# Generated at 2022-06-14 07:15:46.443400
# Unit test for function parse_forwarded
def test_parse_forwarded():
    ret = parse_forwarded({'forwarded': 'secret="secret1",secret="secret2",by=127.0.0.1'},{'FORWARDED_SECRET': 'secret1'})
    assert ret['for'] == '127.0.0.1' and ret['secret'] == 'secret1'

# Generated at 2022-06-14 07:15:57.983978
# Unit test for function parse_forwarded
def test_parse_forwarded():
    from sanic import Sanic
    from sanic import request

    app = Sanic()

    @app.route('/')
    async def handler(req):
        # req.forwarded is the result of parse_forwarded
        return request.json(req.forwarded)

    request_uri = '/'
    request_headers = {'Forwarded': (
        'by=192.168.1.1;for=192.168.1.2;host=host.com;proto=https;port=8080;'
        'path=/test;test=test;abc="test"')}
    request_method = 'GET'

    app.config.FORWARDED_SECRET = ""  # not mandatory for test case

    request, response = app.test_client.get(request_uri, headers=request_headers)

# Generated at 2022-06-14 07:16:09.343213
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    fail = False
    config = Object()
    config.REAL_IP_HEADER = "host"
    config.FORWARDED_FOR_HEADER = "x-forwarded-for"
    config.PROXIES_COUNT = 3
    headers = Object()
    headers.a = "b"
    headers.host = "a"
    headers.x_forwarded_for = "a, b, c, d, e"
    result = parse_xforwarded(headers, config)
    if result is None:
        fail = True
    else:
        if result.get("for") != "e":
            fail = True
    if fail:
        print("test_parse_xforwarded() Failed")
    else:
        print("test_parse_xforwarded() Passed")

test_parse_xforwarded()

# Generated at 2022-06-14 07:16:18.691322
# Unit test for function parse_forwarded
def test_parse_forwarded():
    """Test parsing of Forwarded header."""
    import pytest
    from sanic.server import Sanic
    s = Sanic("test_parse_forwarded")

    @s.route("/")
    async def test_forwarded(request):
        return text(str(request.forwarded))

    s.config.FORWARDED_SECRET = "mysecret"
    client = s.test_client
    forwarded = (
        "By=%3Cproxy%3E; for=%3Cuser%3E; host=%3Cexample.org%3E; "
        "proto=%3Chttp%3E"
    )
    res = client.get("/", headers={"Forwarded": forwarded})
    assert res.status == 200
    assert res.text == "None"

    # Check that we need the

# Generated at 2022-06-14 07:16:30.159087
# Unit test for function parse_forwarded
def test_parse_forwarded():
    options = parse_forwarded("""
        by=_secret;for=_for\",proto=_proto;host=_host;port=_port;path=_path,
        by=_for;for=_secret";host=_host2;port=_port2;path=_path2;
        by=_secret;for=_for";proto=_proto;host=_host;port=_port;path=_path
    """, ",")
    assert options == {"by": "_for", "for": "_secret",
                       "proto": "_proto", "host": "_host",
                       "port": "_port", "path": "_path"}


test_method = parse_forwarded

# Generated at 2022-06-14 07:16:40.527998
# Unit test for function parse_host
def test_parse_host():
    assert parse_host("localhost:8080") == ("localhost", 8080)
    assert parse_host("127.0.0.1:3000") == ("127.0.0.1", 3000)
    assert parse_host("[::1]:3000") == ("[::1]", 3000)
    assert parse_host("example.com:3000") == ("example.com", 3000)
    assert parse_host("localhost") == ("localhost", None)
    assert parse_host("example.com") == ("example.com", None)
    assert parse_host("[::1]") == ("[::1]", None)
    assert parse_host("[::1:5000") is (None, None)
    assert parse_host("[::1]:[5000]") is (None, None)
    assert parse_host("[::1]:p5000")

# Generated at 2022-06-14 07:16:58.681197
# Unit test for function parse_forwarded
def test_parse_forwarded():
    # Multiple elements
    assert parse_forwarded({"forwarded": ["a=b; secret=foo, c=d; secret=bar"]}, config) == {'a': 'b', 'c': 'd'}
    # Multiple headers
    assert parse_forwarded({"forwarded": ["a=b", " c=d; secret=bar"]}, config) == {'c': 'd'}
    # With secret value
    assert parse_forwarded({"forwarded": ["a=b; secret=foo, c=d; secret=bar"]}, config) == {'a': 'b', 'c': 'd'}
    # With secret key

# Generated at 2022-06-14 07:17:12.173014
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from sanic.constants import REAL_IP_HEADER, FORWARDED_FOR_HEADER, PROXIES_COUNT
    from sanic.request import Headers

    headers = Headers()
    headers.append(FORWARDED_FOR_HEADER, "10.0.0.1")
    headers.append(FORWARDED_FOR_HEADER, "10.0.0.10")
    headers.set(REAL_IP_HEADER, "10.0.0.100")
    headers.set("x-forwarded-port", "443")
    headers.set("x-forwarded-path", "/hello/world")
    headers.set("x-scheme", "https")
    headers.set("x-forwarded-host", "sanic.com")

    config = Config()
    config.PROXIES_

# Generated at 2022-06-14 07:17:21.720306
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {
        'X-Scheme': 'http',
        'X-Real-IP': '127.0.0.1',
        'FORWARDED_FOR': '127.0.0.1',
        'X-Forwarded-Proto': 'http',
        'X-Forwarded-Host': '127.0.0.1',
        'X-Forwarded-Path': '/',
    }
    result = parse_xforwarded(headers,2)
    print(result)


# Generated at 2022-06-14 07:17:31.311534
# Unit test for function parse_forwarded
def test_parse_forwarded():
    config = {"FORWARDED_SECRET": "changeme"}
    # This source code example is from the book "Internet programming with
    # Python" by Amjith Ramanujam, published by Packt Publishing
    headers = {
        "Forwarded": "By=<http://localhost:8080>; For=<self>, "
                     "For=<\"127.0.0.1\">; Host=localhost:8080, "
                     "Host=changed; Port=42, Port=8080; "
                     "proto=http, proto=https"}
    result = parse_forwarded(headers, config)

# Generated at 2022-06-14 07:17:43.521498
# Unit test for function parse_forwarded
def test_parse_forwarded():
    from sanic.config import Config, ConfigAttribute
    from sanic.request import BaseRequest, Header
    config = Config()
    config.FORWARDED_SECRET = 'i-am-secret'
    req = BaseRequest()
    req.headers = Header()
    req.headers = None
    # Test case 1: Forwarded: secret="i-am-secret"; for=192.0.2.60; proto=https; host="example.com"
    req.headers["Forwarded"] = 'secret="i-am-secret";for=192.0.2.60;proto=https;host="example.com"'
    assert parse_forwarded(req.headers, config) == {'for': '192.0.2.60', 'proto': 'https', 'host': 'example.com'}
    # Test case 2: Forward

# Generated at 2022-06-14 07:17:46.649183
# Unit test for function parse_forwarded
def test_parse_forwarded():
    headers = {'line': ['by=localhost; for=localhost', 'secret']}

    assert parse_forwarded(headers, "secret") == {'for': 'localhost', 'by': 'localhost'}

# Generated at 2022-06-14 07:18:00.448312
# Unit test for function parse_forwarded
def test_parse_forwarded():
    assert parse_forwarded({}, type("", (), {"FORWARDED_SECRET": None})) is None

    headers = {"Forwarded": "for=127.0.0.1"}
    config = {"FORWARDED_SECRET": None}
    assert parse_forwarded(headers, config) == {"for": "127.0.0.1"}

    headers = {"Forwarded": "secret=abcd; for=192.168.0.1"}
    config = {"FORWARDED_SECRET": "abcd"}
    assert parse_forwarded(headers, config) == {"for": "192.168.0.1"}

    # Test errors
    headers = {"Forwarded": "for=127.0.0.1; for=127.0.0.2"}
    config = {"FORWARDED_SECRET": None}

# Generated at 2022-06-14 07:18:12.394333
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from sanic.config import Config
    config = Config(None)
    config.REAL_IP_HEADER = None
    config.FORWARDED_FOR_HEADER = 'x-forwarded-for'
    config.PROXIES_COUNT = 1

    # input: ['192.168.1.1']
    # output: {'for': '192.168.1.1'}
    assert {'for': '192.168.1.1'} == parse_xforwarded({'x-forwarded-for': '192.168.1.1'}, config)

    # input: ['_obfuscate_ip1', '192.168.1.1']
    # output: {'for': '_obfuscate_ip1'}

# Generated at 2022-06-14 07:18:21.731698
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    """ Unit test for function parse_xforwarded """
    class Headers():
        def __getitem__(self, key):
            return self.get(key)

        def get(self, key, default=None):
            if key == "X-Forwarded-For":
                return "1.2.3.4"
            if key == "X-Forwarded-Host":
                return "testing.com"
            return default

    class Config():
        REAL_IP_HEADER = "X-Forwarded-For"
        FORWARDED_FOR_HEADER = "X-Forwarded-For"
        PROXIES_COUNT = 1

    headers = Headers()
    config = Config()
    options = parse_xforwarded(headers, config)
    assert options["for"] == "1.2.3.4"
   

# Generated at 2022-06-14 07:18:33.616411
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = Headers()
    headers['X-Forwarded-For'] = "10.0.0.1"
    headers['X-Forwarded-Port'] = "8000"
    headers['X-Forwarded-Host'] = "example.com"
    headers['X-Forwarded-Proto'] = "http"
    headers['X-Forwarded-Path'] = "/"
    config = Config()
    config.REAL_IP_HEADER = "X-Forwarded-For"
    config.FORWARDED_FOR_HEADER = "X-Forwarded-For"
    config.FORWARDED_HOST_HEADER = "X-Forwarded-Host"
    config.FORWARDED_PROTO_HEADER = "X-Forwarded-Proto"

# Generated at 2022-06-14 07:19:00.139919
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from sanic import Sanic
    from sanic.config import LOGGING
    from sanic.request import RequestParameters
    from sanic.response import HTTPResponse as Response

    app = Sanic(__name__)
    request = RequestParameters()
    request.path = '/test/'
    request.headers = {"x-scheme":"https","x-forwarded-host":"0:0:0:0:0:0:0:1","x-forwarded-path":"/test/"}
    response = Response(body="test")
    app.add_route(test_parse_xforwarded, '/test/')
    resp = response.prepare(request)
    headers = resp.headers
    params = parse_xforwarded(headers,LOGGING)

# Generated at 2022-06-14 07:19:05.217100
# Unit test for function parse_forwarded
def test_parse_forwarded():
    headers = 'by=_secret;for="_hidden", for=8.8.8.8;host=example.com, secret=_secret2;for=9.9.9.9;host=example.com;proto=https'
    print('before')
    print(headers)
    print('after')
    print(parse_forwarded(headers, '_secret'))

# Generated at 2022-06-14 07:19:15.634345
# Unit test for function parse_forwarded

# Generated at 2022-06-14 07:19:27.671470
# Unit test for function parse_forwarded
def test_parse_forwarded():
    # Taken from real HTTP request
    assert parse_forwarded(
        {
            "x-forwarded-for": "175.135.135.135",
            "x-forwarded-proto": "https",
            "x-forwarded-host": "www.example.com",
            "x-scheme": "http",
            "x-forwarded-port": "80",
            "forwarded": "secret=testby=10;11",
        },
        config={"FORWARDED_SECRET": "test"},
    ) == {
        "host": "www.example.com",
        "proto": "https",
        "port": 80,
        "by": "11",
        "for": "175.135.135.135",
    }

    # Broken headers

# Generated at 2022-06-14 07:19:32.214064
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    http_headers = {'x-forwarded-for': '127.0.0.1', 'x-forwarded-host': 'localhost'}
    options = parse_xforwarded(http_headers, config=DefaultConfig())
    assert options == {"for": "127.0.0.1", "host": "localhost"}

# Generated at 2022-06-14 07:19:39.662726
# Unit test for function parse_forwarded
def test_parse_forwarded():
    headers = {'Forwarded': 'for=192.0.2.60;proto=https;by=203.0.113.43'}
    assert parse_forwarded(headers, None) == {'for': '192.0.2.60', 'proto': 'https', 'by': '203.0.113.43'}


# Generated at 2022-06-14 07:19:49.732449
# Unit test for function parse_xforwarded
def test_parse_xforwarded():

    from sanic.config import Config
    from sanic.request import RequestParameters

    config = Config()
    r = RequestParameters({}, {}, [], [])

    r.headers = {
        "X-Forwarded-For": ["1.2.3.4"],
        "X-Forwarded-Proto": ["https"],
        "X-Forwarded-Host": ["www.example.com:8000"],
        "X-Forwarded-Port": ["8000"],
        "X-Forwarded-Path": ["/my/path"],
        "X-Forwarded-Something": ["wrong"],
    }
    forward_data = parse_xforwarded(r.headers, config)
    assert forward_data is not None
    assert forward_data["for"] == "1.2.3.4"

# Generated at 2022-06-14 07:19:58.757863
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    a = parse_xforwarded( { 'x-forwarded-for': '192.168.1.1, 192.168.1.100', 'x-scheme': 'https', 'x-forwarded-host': 'localhost', 'x-forwarded-port': '80' }, None)
    if a['proto'] == 'https' and a['host'] == 'localhost' and a['port'] == 80 and a['for'] == '192.168.1.1':
        print("test_parse_xforwarded OK")
        return True
    else:
        print("test_parse_xforwarded NG")
        return False


# Generated at 2022-06-14 07:20:11.341413
# Unit test for function parse_forwarded
def test_parse_forwarded():
    headers = {
        "Forwarded": "secret=a;key=value;by=127.0.0.1,secret=b;by=127.0.0.2"
    }
    assert parse_forwarded(headers, {"FORWARDED_SECRET":"a"}) == {
        "secret": "a",
        "by": "127.0.0.1",
        "key": "value",
    }
    assert parse_forwarded(headers, {"FORWARDED_SECRET":"b"}) == {
        "secret": "b",
        "by": "127.0.0.2",
    }
    assert parse_forwarded(headers, {"FORWARDED_SECRET":"c"}) == None

# Generated at 2022-06-14 07:20:15.553584
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {"x-forwarded-for": "10.0.0.0"}
    if headers is not None and "real_ip_header" in headers:
        assert parse_xforwarded(headers, "x-forwarded-for") == {"for": "10.0.0.0"}

# Generated at 2022-06-14 07:20:59.006286
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    import sanic
    class Request(sanic.request.Request):
       def __init__(self, headers = None, ip = None, proxy_count = 0, **kwargs):
           self.ip = ip
           self.headers = headers
           self.app = self
           self.app.FORWARDED_FOR_HEADER = "X-Forwarded-For"
           self.app.FORWARDED_PROTO_HEADER = "X-Forwarded-Proto"
           self.app.FORWARDED_HOST_HEADER = "X-Forwarded-Host"
           self.app.FORWARDED_PORT_HEADER = "X-Forwarded-Port"
           self.app.FORWARDED_PATH_HEADER = "X-Forwarded-Path"
           self.app.PROXIES_COUNT = proxy_count


# Generated at 2022-06-14 07:21:08.006487
# Unit test for function parse_forwarded
def test_parse_forwarded():
    import os
    import sys
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from sanic.config import Config
    config = Config()
    config.FORWARDED_SECRET = ["secret"]
    config.PROXIES_COUNT = 2

    from sanic.server import HttpProtocol
    from sanic.response import HTTPResponse
    from sanic.request import Request
    from sanic.websocket import WebSocketProtocol, WebSocketCommonProtocol
    from sanic.websocket import WebSocketState

    from .fixtures import Fixtures

    from sanic.exceptions import UnsupportedWebsocketProtocol
    from sanic.exceptions import InvalidUsage
    from sanic.exceptions import ServerError


# Generated at 2022-06-14 07:21:20.536255
# Unit test for function parse_forwarded
def test_parse_forwarded():
    from sanic import Sanic
    from sanic.config import Config

    app = Sanic('test_parse_forwarded')
    config = Config(FORWARDED_SECRET='fO0-Bar$')

    # Parse a key-value option
    assert parse_forwarded({'Forwarded': 'for=192.0.2.60;proto=http;by=192.0.2.43'}, config) == \
        {'for': '192.0.2.60', 'proto': 'http'}

    # Parse with multiple headers
    assert parse_forwarded({'Forwarded': 'for=192.0.2.60'}, config) == \
        {'for': '192.0.2.60'}