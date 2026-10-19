

# Generated at 2022-06-14 07:11:43.392340
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from collections import namedtuple
    from sanic.config import Config
    from sanic.utils import sanic_endpoint_test
    # Create some fake headers
    class Headers:
        def __init__(self, headers: HeaderIterable):
            self.headers = headers
        def get(self, key: str, default: Any = None) -> Any:
            try:
                return next((h for k, h in self.headers if k.lower() == key.lower()))
            except StopIteration:
                return default
        def getall(self, key: str, default: Any = None) -> Any:
            return [h for k, h in self.headers if k.lower() == key.lower()]
    # Config object to use when parsing
    Config.REAL_IP_HEADER = None
    Config.FORWARD

# Generated at 2022-06-14 07:11:50.786868
# Unit test for function parse_forwarded
def test_parse_forwarded():
    headers = {'forwarded': ['by=some.host, secret="meme", for=192.168.0.1;proto=https, by=2="meme2"']}
    config = {'FORWARDED_SECRET': 'meme'}
    print(parse_forwarded(headers, config))
    #print(parse_forwarded(headers, config))



# Generated at 2022-06-14 07:11:58.349113
# Unit test for function fwd_normalize
def test_fwd_normalize():
    assert fwd_normalize([("host", "localhost:8000")]) == {"host": "localhost:8000"}
    assert fwd_normalize([("proto", "https")]) == {"proto": "https"}
    # Strip the quotes from the for header in the forwarded header

# Generated at 2022-06-14 07:12:10.639505
# Unit test for function fwd_normalize
def test_fwd_normalize():
    assert {} == fwd_normalize([])
    assert {"by": "1.2.3.4"} == fwd_normalize([("by", "1.2.3.4")])
    assert {"for": "1.2.3.4"} == fwd_normalize([("for", "1.2.3.4")])
    assert {"for": "1.2.3.4", "proto": "https"} == fwd_normalize(
        [("for", "1.2.3.4"), ("proto", "https")]
    )
    assert {"by": "1.2.3.4", "proto": "https"} == fwd_normalize(
        [("by", "1.2.3.4"), ("proto", "https")]
    )

# Generated at 2022-06-14 07:12:23.647354
# Unit test for function parse_forwarded
def test_parse_forwarded():
    forwarded_string = 'From=_z9hG4bK10.49.69.178.29.1588232574653.7;'
    'Host=example.com;Proto=https;By=_foobarbaz;'
    'For="_gazonk\" [F'
    'or=_secret;'
    'By=_secret]\\"\';For=_someip"'
    'By=_secret";For=_127.0.0.1'
    header = [forwarded_string]

# Generated at 2022-06-14 07:12:30.175834
# Unit test for function fwd_normalize_address
def test_fwd_normalize_address():
    assert fwd_normalize_address('foo') == 'foo'
    assert fwd_normalize_address('foo') == 'foo'
    assert fwd_normalize_address('_foo') == '_foo'
    assert fwd_normalize_address('fo_o') == 'fo_o'
    assert fwd_normalize_address('foo_') == 'foo_'

# Generated at 2022-06-14 07:12:32.501325
# Unit test for function fwd_normalize
def test_fwd_normalize():
    """Unit test for the function fwd_normalize"""
    assert fwd_normalize({('adress', 'c'):1}) == {'address': 'c'}

# Generated at 2022-06-14 07:12:46.121190
# Unit test for function parse_forwarded
def test_parse_forwarded():
    from sanic import Sanic
    from sanic.response import text
    from sanic.request import Request

    app = Sanic()

    @app.middleware('request')
    async def process_forwarded(request):
        request.forwarded = parse_forwarded(request.headers, app.config)
        return await response(request)

    async def response(request: Request):
        return text(
            ', '.join([f"{k}: {v}" for k, v in request.forwarded.items()])
        )

    app.config.FORWARDED_SECRET = 'secret'


# Generated at 2022-06-14 07:12:57.396923
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from sanic import Sanic
    from sanic.config import Config
    from sanic.response import HTTPResponse
    from sanic.request import Request
    from sanic.server import HttpProtocol
    from sanic.websocket import WebSocketProtocol
    import aiohttp

    app = Sanic('test_parse_xforwarded')

    @app.route('/test')
    async def test(request):
        return HTTPResponse(body=str(request.remote))

    @app.websocket('/test')
    async def test_ws(request, ws):
        remote_addr = ws.remote_address
        ws.send(str(remote_addr))
        while True:
            msg = await ws.recv()
            if msg is None:
                break
        #

# Generated at 2022-06-14 07:13:00.608380
# Unit test for function fwd_normalize
def test_fwd_normalize():
    if not fwd_normalize((("by", "::1"),)) == {"by": "[::1]"}:
        raise Exception("Failed test")

# Generated at 2022-06-14 07:13:21.827556
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from sanic.request import Request
    from sanic.config import Config
    from sanic.constants import TEST_SERVER
    from sanic.server import HttpProtocol
    
    config = Config()
    config.REAL_IP_HEADER = 'x-real-ip'
    config.FORWARDED_FOR_HEADER = 'x-forwarded-for'
    config.PROXIES_COUNT = 1
    config.FORWARDED_FOR_HEADERS='x-forwarded-for'

    headers = {'x-forwarded-for': '10.10.10.10, 192.168.1.1'}


# Generated at 2022-06-14 07:13:32.786837
# Unit test for function parse_xforwarded

# Generated at 2022-06-14 07:13:40.401124
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = [('Host', '0.0.0.0:8000'), ('X-Forwarded-Host', 'localhost:8000'), 
		('X-Forwarded-Port', '8000'), ('X-Forwarded-For', '127.0.0.1'), 
		('X-Forwarded-Proto', 'http'), ('X-Scheme', 'http')]
    parse_xforwarded(headers, config)

# Generated at 2022-06-14 07:13:51.532028
# Unit test for function parse_forwarded
def test_parse_forwarded():
    from sanic.config import Config
    config = Config()
    config.FORWARDED_SECRET = "totally secret"
    line = 'for=192.0.2.60; proto=http; by=203.0.113.43,for=192.0.2.43;'
    headers = {'Forwarded': line}
    options = parse_forwarded(headers, config)
    print(options)
    assert options['for'] == '192.0.2.43'
    assert options['proto'] == 'http'
    assert options['by'] == '203.0.113.43'


# Generated at 2022-06-14 07:14:01.358254
# Unit test for function fwd_normalize_address
def test_fwd_normalize_address():
    """
    Testcase for fwd_normalize_address
    """
    assert fwd_normalize_address("192.168.1.1") == "192.168.1.1"
    assert fwd_normalize_address("_192.168.1.1") == "_192.168.1.1"
    assert fwd_normalize_address("_unknown") == "_unknown"
    assert fwd_normalize_address("_Unknown") == "_unknown"
    with pytest.raises(ValueError):
        fwd_normalize_address("unknown")
    with pytest.raises(ValueError):
        fwd_normalize_address("Unknown")
    assert fwd_normalize_address("[::1]") == "[::1]"

# Generated at 2022-06-14 07:14:13.800195
# Unit test for function parse_xforwarded
def test_parse_xforwarded():

    # Test a positive case as described in README.md
    headers = {
        #"X-Forwarded-Proto": "http",
        #"X-Forwarded-Host": "remote_host",
        #"X-Forwarded-Port": "80",
        #"X-Forwarded-Path": "/the/path",
        "X-Real-Ip": "127.0.0.1"
    }

    config = type('obj', (object,), {})()
    config.FORWARDED_SECRET = None
    config.REAL_IP_HEADER = "X-Real-Ip"
    config.FORWARDED_FOR_HEADER = "X-Forwarded-For"
    config.PROXIES_COUNT = 1

    forwarded = parse_xforwarded(headers, config)

    assert forwarded

# Generated at 2022-06-14 07:14:26.906861
# Unit test for function parse_forwarded
def test_parse_forwarded():
    class Config:
        FORWARDED_SECRET = "a"
    # RFC 7239 example
    assert parse_forwarded(
        {
            "forwarded": [
                'for="[2001:db8:cafe::17]:4711";'
                'proto=http;'
                'by="[192.0.2.60]"'
            ]
        },
        Config(),
    ) == {"for": "[2001:db8:cafe::17]", "proto": "http", "by": "[192.0.2.60]"}
    assert parse_forwarded({}, Config()) is None
    assert parse_forwarded(
        {"forwarded": ["for=unknown"]}, Config()
    ) == {"for": "unknown"}

# Generated at 2022-06-14 07:14:38.515954
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {
        "x-scheme": "http",
        "x-forwarded-host": "www.eumlab.com",
        "x-forwarded-port": "80",
        "x-forwarded-path": "mypath",
    }
    print(parse_xforwarded(headers, None))
    headers1 = {
        "x-scheme": "https",
        "x-forwarded-host": "www.eumlab.com",
        "x-forwarded-port": "443",
        "x-forwarded-path": "mypath",
    }
    print(parse_xforwarded(headers1, None))

# Generated at 2022-06-14 07:14:46.467008
# Unit test for function fwd_normalize
def test_fwd_normalize():
    ret = fwd_normalize([("for", "198.51.100.1"), ("host", "example.com")])
    assert ret["for"] == "198.51.100.1"
    assert ret["host"] == "example.com"
    ret = fwd_normalize([("for", "198.51.100.1")])
    assert ret["for"] == "198.51.100.1"
    ret = fwd_normalize([("for", "198.51.100.1"), ("port", "443")])
    assert ret["for"] == "198.51.100.1"
    assert ret["port"] == 443


if __name__ == "__main__":
    test_fwd_normalize()

# Generated at 2022-06-14 07:14:59.619737
# Unit test for function parse_xforwarded
def test_parse_xforwarded():

    # Test we can parse x-forwarded headers with multiple values
    headers = MagicMock()

    # We should get the last value
    headers.getall.return_value = [
        "192.168.1.1",
        "192.168.0.1",
        "10.1.1.1",
    ]
    headers.get.return_value = "80"


    config = MagicMock()
    config.PROXIES_COUNT = 3
    # X-Forwarded-Port not set in headers
    config.FORWARDED_FOR_HEADER = 'X-Forwarded-For'
    config.FORWARDED_PROTO_HEADER = 'X-Forwarded-Proto'
    config.FORWARDED_HOST_HEADER = 'X-Forwarded-Host'
    config.FORWARDED

# Generated at 2022-06-14 07:15:14.227600
# Unit test for function parse_forwarded
def test_parse_forwarded():
    assert parse_forwarded({"forwarded":"for=\"_mdnx\";proto=https;by=192.168.0.1;host=example.org;path=/test/"},{'FORWARDED_SECRET': '_mdnx'}) == {'by': '_mdnx', 'for': '_mdnx', 'host': 'example.org', 'proto': 'https', 'path': '/test/'}
    assert parse_forwarded({"forwarded":"by=_mdnx;for=192.168.0.1;proto=https"},{'FORWARDED_SECRET': '_mdnx'}) == {'by': '_mdnx', 'for': '192.168.0.1', 'proto': 'https'}

# Generated at 2022-06-14 07:15:21.622813
# Unit test for function parse_forwarded
def test_parse_forwarded():
    assert parse_forwarded({}) == {}
    assert parse_forwarded({
        "Forwarded": "for=192.0.2.60; proto=http; host=www.example.com",
        "X-Forwarded-For": "192.0.2.43, 198.51.100.17"
    }) == {
        "for": "192.0.2.60",
        "proto": "http",
        "host": "www.example.com"
    }

# Generated at 2022-06-14 07:15:34.670122
# Unit test for function parse_forwarded
def test_parse_forwarded():
    # Test with valid and invalid secrets
    headers1 = {"Forwarded": ["for=\"_mdnx\", by=_mdoy; proto=http, for=\"_mdnx\", by=\"_mdoy\""]}
    parsed1 = parse_forwarded(headers1, Config())

    # Match
    assert parsed1 == {'for': '_mdnx', 'by': '_mdoy', 'proto': 'http'}

    # No match, no secret
    headers2 = {'Forwarded' : ['for=\"_mdnx\", by=_mdoy']}
    parsed2 = parse_forwarded(headers2, Config())
    assert parsed2 == None

    # No match, secret does not match value

# Generated at 2022-06-14 07:15:49.103845
# Unit test for function parse_forwarded
def test_parse_forwarded():
    # Set global config
    settings.FORWARDED_SECRET = 'secret-key'

    # Test empty string
    headers = {}
    assert parse_forwarded(headers, settings) is None

    # Test empty Forwarded header
    headers = {
        'forwarded': ''
    }
    assert parse_forwarded(headers, settings) is None

    # Test empty Forwarded header with secret
    headers = {
        'forwarded': 'secret="secret-key"'
    }
    assert parse_forwarded(headers, settings) is None

    # Test Forwarded header with invalid secret
    headers = {
        'forwarded': 'secret="invalid-key"'
    }
    assert parse_forwarded(headers, settings) is None

    # Test Forwarded header with secret only

# Generated at 2022-06-14 07:15:57.451905
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from sanic import Sanic
    from sanic.request import Request
    from sanic.config import Config

    class App(Sanic):
        def handle_request(self, request, *args, **kwargs):
            return request.headers.get("custom")

    app = App(__name__)
    config = Config()

    # test case 1
    req_headers = {"host": "example.com", "custom": "value"}
    request = Request("GET", "/", request={}, headers=req_headers)
    assert app.handle_request(request) == "value"

    # test case 2
    req_headers = {
        "host": "example.com", 
        "custom": "value",
        "X-Forwarded-Port": "443",
    }

# Generated at 2022-06-14 07:16:09.156540
# Unit test for function fwd_normalize_address
def test_fwd_normalize_address():
    assert fwd_normalize_address('192.168.1.1') == '192.168.1.1'
    assert fwd_normalize_address('0.0.0.0') == '0.0.0.0'
    assert fwd_normalize_address('255.255.255.255') == '255.255.255.255'
    assert fwd_normalize_address('::1') == '[::1]'
    assert fwd_normalize_address('::') != '[::]'
    assert fwd_normalize_address('0:0:0:0:0:0:0:0') == '[0:0:0:0:0:0:0:0]'

# Generated at 2022-06-14 07:16:18.192754
# Unit test for function fwd_normalize_address
def test_fwd_normalize_address():
    assert fwd_normalize_address("unknown") == "unknown"
    assert fwd_normalize_address("_x") == "_x"
    assert fwd_normalize_address("::1") == "[::1]"
    assert fwd_normalize_address("Example.COM") == "example.com"
    assert fwd_normalize_address("EXAMple.cOm") == "example.com"

# Generated at 2022-06-14 07:16:31.410958
# Unit test for function parse_forwarded
def test_parse_forwarded():
    from sanic.config import Config
    from sanic.response import HTTPResponse as Response
    from sanic.request import Request
    from sanic import Sanic
    from sanic import response
    import sys
    if sys.version_info >= (3, 7):
        headers={"Foo": "bar", "BAZ": "inga"}
        app = Sanic(__name__, log_config=None)
        req = Request("GET", "http://python_sanic_test/foo", headers=headers, version=1.1)
        app.config.FORWARDED_SECRET = "secret123"
        req.forwarded = parse_forwarded(req.headers, app.config)
        print(req.forwarded)

if __name__ == '__main__':
    test_parse_forwarded()

# Generated at 2022-06-14 07:16:41.529022
# Unit test for function fwd_normalize
def test_fwd_normalize():
    assert fwd_normalize_address("example.com") == "example.com"
    assert fwd_normalize_address("EXAMPLE.com") == "example.com"
    assert fwd_normalize_address("[::1]") == "[::1]"
    assert fwd_normalize_address("[2001:0db8:0a0b:12f0:0000:0000:0000:0001]") == "[2001:db8:a0b:12f0::1]"
    assert fwd_normalize_address("[1:2:3::4]") == "[1:2:3::4]"
    assert fwd_normalize_address("[::192.168.1.1]") == "[::192.168.1.1]"

# Generated at 2022-06-14 07:16:50.052825
# Unit test for function fwd_normalize
def test_fwd_normalize():
    from unittest import TestCase, main

    class FwdNormalizeTestCase(TestCase):
        def test_fwd_normalize(self):
            self.assertEqual(
                fwd_normalize(
                    [
                        ("By", "12.34.56.78"),
                        ("proto", "http"),
                        ("host", "example.com"),
                        ("port", "80"),
                        ("path", "/foo bar"),
                    ]
                ),
                {"by": "12.34.56.78", "host": "example.com", "port": 80, "path": "/foo bar"},
            )

    main()

# Generated at 2022-06-14 07:17:00.001112
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    pass

# Generated at 2022-06-14 07:17:13.119911
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    """Sanity check for function parse_xforwarded."""
    from sanic.config import Config
    from sanic.request import Request
    from sanic.websocket import WebSocketProtocol
    from sanic.constants import HTTP_METHODS, SCHEMES

    # Test all possible HTTP and websocket methods, and their schemes
    for method, scheme in itertools.product(HTTP_METHODS + ["WS"], SCHEMES):
        config = Config(SERVER_NAME="", FORWARDED_FOR_HEADER="X-Forwarded-For")

# Generated at 2022-06-14 07:17:25.671059
# Unit test for function parse_forwarded
def test_parse_forwarded():
    class config:
        FORWARDED_SECRET = None
        FORWARDED_FOR_HEADER = "X-Forwarded-For"
        REAL_IP_HEADER = "X-Real-IP"
        PROXIES_COUNT = 1

    class headers:
        def getall(header, default):
            if header == "forwarded":
                return [
                    "for=192.0.2.60;proto=http,by=192.0.2.43;secret=hello",
                    "for=192.0.2.61;proto=http,by=192.0.2.43;secret=hello",
                ]

# Generated at 2022-06-14 07:17:38.948991
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = dict()
    config = Config()
    config.REAL_IP_HEADER = "remote_addr"
    config.PROXIES_COUNT = 2
    config.FORWARDED_FOR_HEADER = "x-forwarded-for"

    headers["remote_addr"] = "1.0.0.0"
    headers["x-forwarded-for"] = ["1.1.1.1,2.2.2.2"]
    ret = parse_xforwarded(headers=headers, config=config)
    assert("for" in ret)
    assert(ret["for"] == "1.1.1.1")
    assert("remote_addr" in headers)
    assert(headers["remote_addr"] == "1.0.0.0")

    del headers["remote_addr"]

# Generated at 2022-06-14 07:17:47.584796
# Unit test for function parse_forwarded

# Generated at 2022-06-14 07:18:00.604598
# Unit test for function parse_forwarded

# Generated at 2022-06-14 07:18:09.098603
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    import tempfile
    sock = tempfile.TemporaryFile()
    sock.write(b'GET / HTTP/1.1\r\nx-forwarded-for: 127.0.0.1\r\n\r\n')
    sock.seek(0)
    from .request import Request
    from .settings import Config
    config = Config()
    request = Request(config, sock, "GET", "HTTP/1.1", "/", headers={})
    assert parse_xforwarded(request.headers, config) is not None

# Generated at 2022-06-14 07:18:20.002727
# Unit test for function parse_forwarded
def test_parse_forwarded():
    class FakeHeaders(dict):
        def __init__(self, names):
            self.names = names

        def getall(self, name):
            return self.names.get(name)

    class Config:
        def __init__(self, secret, proxies_count):
            self.FORWARDED_SECRET = secret
            self.PROXIES_COUNT = proxies_count

    h = FakeHeaders(names={"forwarded":["a"]})
    cfg = Config(secret="b", proxies_count=0)
    assert None == parse_forwarded(h, cfg)

    h = FakeHeaders(names={"forwarded":["a"]})
    cfg = Config(secret="a", proxies_count=0)
    assert None == parse_forwarded(h, cfg)


# Generated at 2022-06-14 07:18:32.626351
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {}
    config = {}
    assert parse_xforwarded(headers, config) == None

    headers['X-Forwarded-For'] = '1.1.1.1'
    config['REAL_IP_HEADER'] = 'X-Forwarded-For'
    config['PROXIES_COUNT'] = 1
    assert parse_xforwarded(headers, config) == {'for': '1.1.1.1'}

    headers['X-Forwarded-For'] = '1.1.1.1'
    config['REAL_IP_HEADER'] = None
    config['PROXIES_COUNT'] = 1
    assert parse_xforwarded(headers, config) == {'for': '1.1.1.1'}


# Generated at 2022-06-14 07:18:47.290788
# Unit test for function parse_forwarded
def test_parse_forwarded():
    import urllib


# Generated at 2022-06-14 07:19:02.499822
# Unit test for function parse_forwarded
def test_parse_forwarded():
    headers = {
        'Forwarded': 'for=192.0.2.43, for="[2001:db8:cafe::17]", for=unknown, for=192.0.2.61; proto=https;by=203.0.113.43, for=203.0.113.43, for="[2001:db8:cafe::17]:4711", for=192.0.2.43; proto=http; by=203.0.113.43'
    }
    assert parse_forwarded(headers, config=None) is not None
    assert parse_forwarded(headers, config={'FORWARDED_SECRET': '203.0.113.43'}) is not None
    assert parse_forwarded(headers, config={'FORWARDED_SECRET': 'abc'}) is None


# Generated at 2022-06-14 07:19:09.558406
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from sanic import Sanic
    app = Sanic('test_parse_xforwarded')
    x_real_ip = '111.113.115.117'
    x_forwarded_for = "222.223.224.225,1.1.1.1,1.1.1.1"
    x_forwarded_host = 'example.com:8080'
    x_forwarded_proto = 'https'
    x_forwarded_port = '80'
    x_forwarded_path = '/v1/hello/world'

# Generated at 2022-06-14 07:19:22.897847
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {}
    assert parse_xforwarded(headers, None) is None
    headers = {
        "x-forwarded-for": "1.1.1.1",
    }
    assert parse_xforwarded(headers, None) == {"for": "1.1.1.1"}
    headers = {
        "x-forwarded-for": "1.1.1.1",
        "x-forwarded-port": "80",
    }
    assert parse_xforwarded(headers, None) == {"for": "1.1.1.1", "port": 80}

# Generated at 2022-06-14 07:19:33.839734
# Unit test for function parse_forwarded
def test_parse_forwarded():
    headers = {
        "Forwarded": ["for=192.0.2.43, for=\"[2001:db8:cafe::17]\""]
    }
    config = object()
    config.FORWARDED_SECRET = None
    assert parse_forwarded(headers, config) == {
        "for": ["192.0.2.43", "[2001:db8:cafe::17]"]
    }

    headers = {
        "Forwarded": ["for=192.0.2.60;proto=http;by=203.0.113.43"]
    }
    config.FORWARDED_SECRET = None

# Generated at 2022-06-14 07:19:37.229145
# Unit test for function parse_forwarded
def test_parse_forwarded():
    headers = {
        "Forwarded": ["for=\"_mdnx\"; proto=https; host=example.org; secret=value"]
    }
    sanic_app = Sanic("test_app")
    config = sanic_app.config
    config.FORWARDED_SECRET = "value"
    res = parse_forwarded(headers, config)
    assert(res == {"for": "_mdnx", "proto": "https", "host": "example.org"})

# Generated at 2022-06-14 07:19:44.100189
# Unit test for function parse_forwarded
def test_parse_forwarded():
    assert parse_forwarded({}, {"FORWARDED_SECRET": "test"}) == None
    assert parse_forwarded({"forwarded": "by=secret, by=localhost, by=test"}, {"FORWARDED_SECRET": "test"}) \
            == {'by': 'secret', 'proto': 'http', 'for': 'localhost', 'host': 'localhost', 'port': 80}

# Generated at 2022-06-14 07:19:57.172744
# Unit test for function parse_forwarded
def test_parse_forwarded():
    assert parse_forwarded(["for=192.0.2.60;proto=http;by=203.0.113.43"], None) == {'for': '192.0.2.60', 'proto': 'http', 'by': '203.0.113.43'}
    assert parse_forwarded(["for=192.0.2.60, for=198.51.100.17;proto=http"], None) == None

# Generated at 2022-06-14 07:20:09.969715
# Unit test for function parse_forwarded
def test_parse_forwarded():
    fwd = 'By="[xx:xx:xx:xx:xx:xx:xx:xx]";for=127.0.0.1;proto=http;host=abc.com;port=8080;'
    headers = {'Forwarded': fwd}
    config = {'FORWARDED_SECRET': '59d66cb1'}
    fwd_result = parse_forwarded(headers, config)
    assert fwd_result == {'by': '[xx:xx:xx:xx:xx:xx:xx:xx]', 'for': '127.0.0.1', 'proto': 'http', 'host': 'abc.com', 'port': 8080}


# Generated at 2022-06-14 07:20:22.090503
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {"X-Real-Ip": "5.5.5.5", "X-Forwarded-Host": "test.com", "X-Forwarded-Port": 1000}
    config = {"REAL_IP_HEADER": "X-Real-Ip", "FORWARDED_FOR_HEADER": "X-Forwarded-Host", "PROXIES_COUNT": 2, "FORWARDED_SECRET": None}
    options = parse_xforwarded(headers, config)
    assert options == {'for': '5.5.5.5', 'host': 'test.com', 'port': 1000}

    headers = {"X-Forwarded-Host": "test.com", "X-Forwarded-Port": 1000}
    options = parse_xforwarded(headers, config)

# Generated at 2022-06-14 07:20:29.473654
# Unit test for function parse_forwarded
def test_parse_forwarded():
    headers = {"forwarded": "Secret=supersecret; By=0.0.0.0, Secret=supersecret; By=0.0.0.1, By=0.0.0.2"}
    assert parse_forwarded(headers, "supersecret") == {'by': '0.0.0.1'}
    headers = {"forwarded": "Secret=supersecret; By=0.0.0.0, Secret=no; By=0.0.0.1, By=0.0.0.2"}
    assert parse_forwarded(headers, "supersecret") == None

# Generated at 2022-06-14 07:20:50.848995
# Unit test for function parse_forwarded
def test_parse_forwarded():
    # success case
    forwarded_str = "proto=https,for=10.10.10.10:123,by=10.10.10.11:321,host=myhost.sanic.com,port=9090,proto=http,path=/hello"
    result = parse_forwarded(forwarded_str)

# Generated at 2022-06-14 07:21:04.543759
# Unit test for function parse_forwarded
def test_parse_forwarded():
    headers = [
        "for=192.0.2.60; proto=http; by=203.0.113.60; secret=123",
        "for=192.0.2.30; by=203.0.113.30; secret=123",
    ]
    fwd = parse_forwarded(headers, secret="123")
    assert fwd["proto"] == "http"
    assert fwd["for"] == "192.0.2.60"
    assert fwd["by"] == "203.0.113.60"
    assert fwd["secret"] == "123"
    assert list(fwd) == ["for", "proto", "by", "secret"]
    fwd = parse_forwarded(headers[::-1], secret="123")
    assert fwd["proto"] == "http"
   

# Generated at 2022-06-14 07:21:17.227718
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    config = type('', (), {})()
    config.REAL_IP_HEADER = 'X-Real-IP'
    config.FORWARDED_FOR_HEADER = 'X-Forwarded-For'
    config.PROXIES_COUNT = 3
    headers = type('', (), {})()
    # no Real IP
    headers.X_Real_IP = None
    assert parse_xforwarded(headers, config) == None
    # Real IP
    headers.X_Real_IP = '127.0.0.1'
    assert parse_xforwarded(headers, config) == {'for': '127.0.0.1'}
    # multiple proxies, invalid entries