

# Generated at 2022-06-14 07:11:29.721769
# Unit test for function parse_forwarded
def test_parse_forwarded():
    headers = {'Forwarded': 'by=192.0.2.43,for=[2001:db8::c001:9:12:22:33]:65535;proto=https;host=example.com;port=80,by=192.0.2.42'}
    config = {'FORWARDED_SECRET': '123456'}
    print(parse_forwarded(headers, config))
    #return parse_forwarded(headers, config)



# Generated at 2022-06-14 07:11:43.770388
# Unit test for function fwd_normalize
def test_fwd_normalize():
    # Valid values
    assert fwd_normalize([("by","1.2.3.4")]) == {
        "by": "1.2.3.4"
    }
    assert fwd_normalize([("by","[::1]")]) == {
        "by": "[::1]"
    }
    assert fwd_normalize([("for","1.2.3.4")]) == {
        "for": "1.2.3.4"
    }
    assert fwd_normalize([("proto","http")]) == {
        "proto": "http"
    }
    assert fwd_normalize([("host","test")]) == {
        "host": "test"
    }

# Generated at 2022-06-14 07:11:51.771136
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from sanic.request import Request

    headers = {"X-Forwarded-For": "192.168.0.10, 172.20.1.1"}
    for p in range(1, 4):
        req = Request(
            headers=headers,
            app={"config": {"PROXIES_COUNT": p, "FORWARDED_FOR_HEADER": "X-Forwarded-For"}},
        )
        print(req.forwarded)


# Generated at 2022-06-14 07:11:59.607982
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {
        "x-forwarded-for": "123.123.123.123",
        "x-scheme": "https",
        "x-forwarded-host": "example.com",
        "x-forwarded-port": "80",
        "x-forwarded-path": "/abc?123"
    }
    config = {
        "REAL_IP_HEADER": None,
        "FORWARDED_FOR_HEADER": "x-forwarded-for",
        "PROXIES_COUNT": None
    }
    ret = parse_xforwarded(headers, config)
    assert ret, "Parse Failed"
    assert ret["proto"] == "https", "Parse Error"
    assert ret["host"] == "example.com", "Parse Error"

# Generated at 2022-06-14 07:12:11.091619
# Unit test for function parse_host

# Generated at 2022-06-14 07:12:20.876323
# Unit test for function parse_forwarded
def test_parse_forwarded():
    headers: Dict[str, List[str]] = \
        {'forwarded': ['secret=secret1, for=172.12.0.1;by=172.12.0.1',
                        'secret=secret2, for=172.12.0.2;by=172.12.0.2']}
    config = type('', (), {'FORWARDED_SECRET': 'secret2'})()
    assert parse_forwarded(headers, config) == {'for': '172.12.0.2',
                                                'by': '172.12.0.2'}

# Generated at 2022-06-14 07:12:31.081704
# Unit test for function fwd_normalize
def test_fwd_normalize():
    assert fwd_normalize([
        ("by", "1.1.1.1"),
        ("proto", "http"),
        ("host", "google.com"),
        ("port", "80"),
    ]) == {
        "by": "1.1.1.1",
        "proto": "http",
        "host": "google.com",
        "port": 80,
    }

    assert fwd_normalize([
        ("for", "_token"),
        ("proto", "http"),
        ("port", "80"),
    ]) == {
        "for": "_token",
        "proto": "http",
        "port": 80,
    }

# Generated at 2022-06-14 07:12:44.577829
# Unit test for function parse_forwarded

# Generated at 2022-06-14 07:12:50.795320
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    num_proxies = 1
    #print("parse_xforwarded")
    #print("")
    #print("num_proxies = 1")
    #print("")
    
    # Single entry
    #print("single entry")
    #print("")
    print("TRACE: test_parse_xforwarded")
    headers = {"x-forwarded-for": "127.0.0.1"}
    ret = parse_xforwarded(headers, num_proxies)
    assert ret["for"] == "127.0.0.1"
    assert ret.get("by") is None
    #print("")
    
    # Multiple entries
    #print("multiple entries")
    #print("")
    print("TRACE: multiple entries")

# Generated at 2022-06-14 07:12:58.231959
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = Headers([('x-forwarded-for', '2001:0db8:85a3:0000:0000:8a2e:0370:7334')])
    ret = parse_xforwarded(headers, Config())
    assert ret is not None
    assert ret['for'] == '2001:0db8:85a3:0000:0000:8a2e:0370:7334'

# Generated at 2022-06-14 07:13:20.086446
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {
        'X-Forwarded-For': '1.1.1.1, 2.2.2.2',
        'X-Forwarded-Proto': 'https',
        'X-Forwarded-Host': '3.3.3.3',
        'X-Forwarded-Port': '4',
        'X-Forwarded-Path': '5'
    }
    result = parse_xforwarded(headers)
    assert result == {'for': '1.1.1.1', 'proto': 'https', 'host': '3.3.3.3', 'port': 4, 'path': '5'}

# Generated at 2022-06-14 07:13:28.958794
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from sanic.config import Config

    config = Config()
    config.REAL_IP_HEADER = ""
    config.FORWARDED_FOR_HEADER = "x-forwarded-for"
    config.PROXIES_COUNT = 1
    headers = {
        "x-forwarded-for": "192.168.0.1, 192.168.0.2",
    }

    result = parse_xforwarded(headers, config)
    expected = {"for": "192.168.0.2"}

    assert result == expected


# Generated at 2022-06-14 07:13:31.848230
# Unit test for function parse_content_header
def test_parse_content_header():
    assert parse_content_header('form-data; name=upload; filename=\"file.txt\"') == ('form-data', {'name': 'upload', 'filename': 'file.txt'})


# Generated at 2022-06-14 07:13:40.462050
# Unit test for function fwd_normalize_address
def test_fwd_normalize_address():
    address = "unknown"
    print(fwd_normalize_address(address))
    address = "_fake_"
    print(fwd_normalize_address(address))
    address = "127.0.0.1"
    print(fwd_normalize_address(address))
    address = "::1"
    print(fwd_normalize_address(address))
    address = "[::1]"
    print(fwd_normalize_address(address))



# Generated at 2022-06-14 07:13:51.019988
# Unit test for function fwd_normalize_address
def test_fwd_normalize_address():
    addr_normalized_expect_result = {
        "8.8.8.8": "8.8.8.8",
        "2001:0db8:85a3:0000:0000:8a2e:0370:7334": "[2001:0db8:85a3:0000:0000:8a2e:0370:7334]",
        "example.com": "example.com",
        "www.example.com": "www.example.com",
        "unknown": ValueError(),
        "_private_ip": "_private_ip",
        "_private_ipv6": "_private_ipv6",
        "_private_hostname": "_private_hostname",
        "0.0.0.0": "0.0.0.0",
        "::1": "[::1]",
    }

# Generated at 2022-06-14 07:14:04.950616
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {'X-Forwarded-For': '1.2.3.4, 5.6.7.8, 9.10.11.12, test, localhost'}
    def run_test(count, real_ip, expected):
        from sanic.config import Config
        config = Config()
        config.PROXIES_COUNT = count
        config.REAL_IP_HEADER = real_ip
        assert parse_xforwarded(headers, config) == expected

# Generated at 2022-06-14 07:14:19.295996
# Unit test for function parse_forwarded
def test_parse_forwarded():
    class Header:
        def __init__(self, d):
            self.d = d

        def getall(self, key, default=None):
            # key: string
            # default: string
            # return list of string
            return self.d.get(key, default) if type(self.d) == dict else []

    class Config:
        def __init__(self, secret):
            self.FORWARDED_SECRET = secret

    h = Header({"Forwarded": "for=192.0.2.60; Proto=Tcp; by=_secret"})
    c = Config("_secret")
    assert parse_forwarded(h, c) == {"for": "192.0.2.60", "proto": "tcp"}


# Generated at 2022-06-14 07:14:20.084487
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    pass

# Generated at 2022-06-14 07:14:30.736837
# Unit test for function parse_forwarded
def test_parse_forwarded():
    from sanic import Sanic
    from sanic.request import RequestParameters
    from sanic.response import HTTPResponse

    app = Sanic()
    app.config.FORWARDED_SECRET = "test"

    @app.route("/test", methods=["POST"])
    async def test(request):
        return HTTPResponse(json=request.forwarded)


# Generated at 2022-06-14 07:14:42.980365
# Unit test for function parse_forwarded
def test_parse_forwarded():
    from sanic.config import Config
    from sanic.server import HeaderResolver
    config = Config()
    h = HeaderResolver()

    # Single valid forwarded
    h.set("Forwarded", "for=10.0.0.1")
    f = parse_forwarded(h, config)
    assert f == {"for": "10.0.0.1"}

    # Multiple forwarded headers
    h.add("Forwarded", "by=10.0.0.1")
    h.add("Forwarded", "secret=secret1")
    h.add("Forwarded", "for=10.0.0.2;proto=https;host=example.com")
    h.add("Forwarded", "for=10.0.0.3;proto=https;host=example.com:443")
    h.add

# Generated at 2022-06-14 07:15:01.673585
# Unit test for function parse_forwarded
def test_parse_forwarded():
    from sanic.request import Request

    class DummyConnection:
        def __init__(self, headers):
            self.headers = headers

    class DummyRawStream:
        def __init__(self, headers):
            self.headers = headers

    class DummyProtocol:
        @property
        def version(self):
            return "HTTP/1.1"

        def parse_headers(self, headers):
            return headers

    headers = {'Host': '127.0.0.1:8000', 'Forwarded': 'for=192.0.2.60;proto=http;by=203.0.113.43'}
    # headers = {'Host': '127.0.0.1:8000', 'Forwarded': 'secret=secret1, for=192.0.2.60;proto=http;by

# Generated at 2022-06-14 07:15:15.728034
# Unit test for function parse_forwarded
def test_parse_forwarded():
    headers = {}
    config = None

    # No header line
    assert parse_forwarded(headers, config) == None

    # Header line without value
    headers = {"Forwarded": ['']}
    assert parse_forwarded(headers, config) == None

    # Even Multiple Header lines without value
    headers = {"Forwarded": ['']*3}
    assert parse_forwarded(headers, config) == None
    
    # Header line with value but without secret
    headers = {"Forwarded": ['for="_gazonk"']}
    assert parse_forwarded(headers, config) == None

    # Multiple Header lines without secret, only the 1st is processed
    headers = {"Forwarded": ['for="_gazonk"']*3}
    assert parse_forwarded(headers, config) == None

    # Header line with secret,

# Generated at 2022-06-14 07:15:25.678636
# Unit test for function parse_forwarded
def test_parse_forwarded():
    class MockConfig(object):
        FORWARDED_SECRET = 'mysecret'

    def assertParsed(header, expected):
        assert parse_forwarded(header, MockConfig()) == expected

    assertParsed(None, None)
    assertParsed({"forwarded": b""}, None)
    assertParsed({"forwarded": b"for=1.2.3.4"}, {"for": "1.2.3.4"})
    assertParsed({"forwarded": b"for=\"1.2.3.4\""}, {"for": "1.2.3.4"})
    assertParsed({"forwarded": b"for=1.2.3.4; pro=https"}, {"for": "1.2.3.4"})

# Generated at 2022-06-14 07:15:36.544180
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {
        "X-Forwarded-For": "192.168.0.3, 127.0.0.1",
        "X-Forwarded-Port": "80",
        "X-Forwarded-Proto": "https",
    }
    config = {"PROXIES_COUNT": 2, "FORWARDED_FOR_HEADER": "X-Forwarded-For"}
    result = parse_xforwarded(headers, config)
    assert result["for"] == "192.168.0.3"
    assert result["proto"] == "https"
    assert result["port"] == 80
    config["PROXIES_COUNT"] = 3
    result = parse_xforwarded(headers, config)
    assert result["for"] == "127.0.0.1"

# Generated at 2022-06-14 07:15:44.800720
# Unit test for function parse_host
def test_parse_host():
    assert parse_host("localhost") == ("localhost", None)
    assert parse_host("[::1]") == ("[::1]", None)
    assert parse_host("[::1]:8080") == ("[::1]", 8080)
    assert parse_host("[::1]:-1") == ("[::1]", -1)
    assert parse_host("[::1]:65536") == ("[::1]", None)
    assert parse_host("a.b.c.d") == ("a.b.c.d", None)
    assert parse_host("a.b.c.d:80") == ("a.b.c.d", 80)

    assert parse_host("localhost:") == (None, None)
    assert parse_host("localhost:80") == ("localhost", 80)
    assert parse

# Generated at 2022-06-14 07:15:51.443795
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {
        'x-forwarded-host': '0.0.0.0:5000',
        'x-forwarded-proto': 'http',
        'x-forwarded-path': '/static/arq/img/bg_art.jpg'
    }
    print(parse_xforwarded(headers, None))


if __name__ == '__main__':
    test_parse_xforwarded()

# Generated at 2022-06-14 07:16:01.008650
# Unit test for function parse_forwarded
def test_parse_forwarded():
    headers = {
        'Forwarded': ['By=kong;For=10.1.1.1:8443;Proto=https']
    }

    config = {
        'FORWARDED_SECRET': 'kong'
    }

    expected = {
        'for': '10.1.1.1:8443',
        'proto': 'https',
        'by': 'kong'
    }

    forwarded = parse_forwarded(headers, config)
    assert expected == forwarded

# Generated at 2022-06-14 07:16:15.099157
# Unit test for function parse_forwarded

# Generated at 2022-06-14 07:16:26.492046
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    # Check that it parses x-forwarded-for and x-forwarded-proto
    headers = {
        'X-Forwarded-For': '127.0.0.1, localhost',
        'X-Forwarded-Proto': 'https',
    }
    res = parse_xforwarded(headers, None)
    assert res == {'host': '127.0.0.1', 'proto': 'https'}
    # Check that we get None if the header is missing
    headers = {'X-Forwarded-Proto': 'https'}
    assert parse_xforwarded(headers, None) is None
    # Check that we ignore values after the first comma
    headers = {'X-Forwarded-For': '127.0.0.1, localhost'}

# Generated at 2022-06-14 07:16:36.170528
# Unit test for function parse_forwarded
def test_parse_forwarded():
    forwarded = " for=\"_mdnxca=1, _mdn=1234567890, _mdne=0987654321\"; by=192.168.0.1, for=10.0.0.1; secret=\"1234567890\"; proto=http, for=10.0.0.2; secret=\"0987654321\", for=10.0.0.3"
    options = parse_forwarded(forwarded, None)
    # verify options right to left
    assert options["proto"] == "http"
    assert options["for"] == "10.0.0.3"
    assert options["secret"] == "0987654321"

# Generated at 2022-06-14 07:16:56.213580
# Unit test for function parse_forwarded
def test_parse_forwarded():
    config = Config()
    config.FORWARDED_SECRET = "secret"
    assert (
        parse_forwarded({"Forwarded": ["by=child;secret=secret"]}, config)
        == {"by": "child", "secret": "secret"}
    )
    assert parse_forwarded({"Forwarded": ["secret=secret"]}, config) == {}
    assert parse_forwarded(
        {"Forwarded": ["secret=child;secret=secret"]}, config
    ) == {}
    config.FORWARDED_SECRET = "secret"
    assert (
        parse_forwarded(
            {"Forwarded": ["secret=child;by=child;secret=secret"]}, config
        )
        == {"by": "child", "secret": "secret"}
    )
    config.FORWARDED_SECRET = ""
    assert parse

# Generated at 2022-06-14 07:17:07.799097
# Unit test for function parse_forwarded
def test_parse_forwarded():
    from sanic.config import Config

    headers = "for=192.0.2.60; proto=http; by=203.0.113.43"
    config = Config()

    config.FORWARDED_SECRET = None
    result = parse_forwarded({'forwarded': [headers, 'for=192.0.2.60;'
                                            ' proto=http; by=203.0.113.43']}, config)
    assert result == {'for': '192.0.2.60', 'proto': 'http', 'by': '203.0.113.43'}

    config.FORWARDED_SECRET = 'secret'
    result = parse_forwarded({'forwarded': [headers + "; secret=secret"]}, config)

# Generated at 2022-06-14 07:17:15.827414
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from sanic.exceptions import InvalidUsage
    from sanic.response import text
    from sanic.request import Request
    from sanic.config import Config


# Generated at 2022-06-14 07:17:28.100064
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    import sanic, requests
    app = sanic.Sanic("test_parse_xforwarded")
    @app.route("/")
    def handler(request):
        return sanic.response.text("done")
    app.config.PROXIES_COUNT = 2
    app.config.FORWARDED_FOR_HEADER = "X-Forwarded-For"
    # No xforwarded headers provided
    client = app.test_client
    assert client.get("/").status == 200
    # Valid xforwarded
    client = requests.Session()

# Generated at 2022-06-14 07:17:31.826545
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {"X-Forwarded-For": "10.0.1.1"}
    options = parse_xforwarded(headers, Options)
    assert options['host'] == '10.0.1.1'

# Generated at 2022-06-14 07:17:43.548276
# Unit test for function parse_forwarded
def test_parse_forwarded():
    assert parse_forwarded({"forwarded": "for=192.0.2.60;proto=http,by=203.0.113.43;secret=\"v4v6;,:=?@!\""}, None) == {'for': '192.0.2.60', 'proto': 'http', 'by': '203.0.113.43', 'secret': 'v4v6;,:=?@!'}
    assert parse_forwarded({"forwarded": "for=192.0.2.43, for=198.51.100.17"}, None) == {'for': '198.51.100.17'}

# Generated at 2022-06-14 07:17:56.512233
# Unit test for function fwd_normalize
def test_fwd_normalize():
    from sanic import Sanic
    from sanic.request import RequestParameters
    from sanic.server import HttpProtocol


    def parse(app, hdrs, *args, **kwargs):
        return HttpProtocol.parse_request_async(
            app, RequestParameters(hdrs), *args, **kwargs
        )[0]


    app = Sanic()
    app.config.from_object({"FORWARDED_SECRET": "secret"})

    # Empty
    assert not parse(app, {}).forwarded

    # Single forward
    app.config["FORWARDED_FOR_HEADER"] = "X-Forwarded-For"

# Generated at 2022-06-14 07:18:07.652381
# Unit test for function parse_forwarded
def test_parse_forwarded():
    from sanic.config import Config
    from sanic import Sanic
    from sanic.response import json
    from sanic.request import Request

    app = Sanic("test_parse_forwarded")

    @app.route("/", methods=["GET"])
    async def handler(request: Request):
        return json(
            {"path": request.path, "forwarded": request.app.config.FORWARDED_SECRET}
        )

    cli = app.test_client
    app.config.FORWARDED_SECRET = "secret"
    assert cli.get("/?hello=world").status == 200
    assert cli.get("/?hello=world", headers={"forwarded": "by=_; for=localhost"}).status == 200

# Generated at 2022-06-14 07:18:19.468443
# Unit test for function parse_forwarded
def test_parse_forwarded():
    # Parse forwarded for for different secret strings
    assert parse_forwarded(
        {"Forwarded": ["for=192.0.2.60;proto=https, by=1.2.3.4;secret=xyz"]},
        MagicMock(FORWARDED_SECRET="xyz"),
    ) == {"for": "192.0.2.60", "proto": "https"}
    assert parse_forwarded(
        {"Forwarded": ["for=192.0.2.60;proto=https, by=1.2.3.4;secret=\"xyz\""]},
        MagicMock(FORWARDED_SECRET="xyz"),
    ) == {"for": "192.0.2.60", "proto": "https"}

# Generated at 2022-06-14 07:18:32.381058
# Unit test for function fwd_normalize
def test_fwd_normalize():
    assert fwd_normalize([]) == {}

    assert fwd_normalize([("for", "1.2.3.4")]) == {
        "for": "1.2.3.4"
    }

    assert fwd_normalize([("for", "1.2.3.4"), ("host", "example.com")]) == {
        "for": "1.2.3.4",
        "host": "example.com",
    }

    assert fwd_normalize([("proto", "https"), ("for", "1.2.3.4")]) == {
        "proto": "https",
        "for": "1.2.3.4",
    }


# Generated at 2022-06-14 07:18:54.169710
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {"x-scheme": "https"}
    opts = parse_xforwarded(headers)
    assert opts == {"proto": "https"}
    headers = {"x-forwarded-for": "1.2.3.4"}
    opts = parse_xforwarded(headers)
    assert opts == {"for": "1.2.3.4"}
    headers = {"x-scheme": "https", "x-forwarded-for": "1.2.3.4"}
    opts = parse_xforwarded(headers)
    assert opts == {"proto": "https", "for": "1.2.3.4",}
    headers = {"x-forwarded-for": "1.2.3.4, 2.3.4.5, 3.4.5.6"}
    opt

# Generated at 2022-06-14 07:19:03.314805
# Unit test for function parse_forwarded
def test_parse_forwarded():
    headers = {'forwarded': ['For="_mdnx654321"; proto=https, for=192.0.2.60; Host="example.com"; Port=443, for=198.51.100.17']}
    config = {'FORWARDED_SECRET': ['_mdnx654321']}
    result = parse_forwarded(headers, config)
    assert result == {'for': '198.51.100.17', 'proto': 'https', 'host': 'example.com', 'port': 443}

# Generated at 2022-06-14 07:19:14.567063
# Unit test for function parse_xforwarded

# Generated at 2022-06-14 07:19:19.087693
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    options = parse_xforwarded({"X-Forwarded-For": "10.0.0.1"}, Config())
    rt.eq(options, {
        'for': '10.0.0.1'
    })



# Generated at 2022-06-14 07:19:31.811723
# Unit test for function parse_forwarded

# Generated at 2022-06-14 07:19:44.839816
# Unit test for function parse_forwarded
def test_parse_forwarded():
    # parse_forwarded should return the correct values for valid inputs
    assert(parse_forwarded({"forwarded":"Secret=abc, By=bcd, For=cde, Proto=http, Host=localhost, Port=8080, Path=/test, Path=/test2, Path=/test3"},
        {"FORWARDED_SECRET": "abc"}) == {
        "secret": "abc",
        "by": "bcd",
        "for": "cde",
        "proto": "http",
        "host": "localhost",
        "port": 8080,
        "path": "/test"
    })
    # parse_forwarded should return None for invalid inputs

# Generated at 2022-06-14 07:19:57.576483
# Unit test for function fwd_normalize
def test_fwd_normalize():
    assert fwd_normalize((("for", "192.168.1.1"), ("by", "192.168.1.2"))) == {
        "for": "192.168.1.1",
        "by": "192.168.1.2",
    }
    assert fwd_normalize((("for", "192.168.1.1"), ("host", "host.com"))) == {
        "for": "192.168.1.1",
        "host": "host.com",
    }

# Generated at 2022-06-14 07:20:10.305865
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from requests import Request
    from sanic.utils import sanic_endpoint_test
    from sanic import Sanic
    
    app = Sanic('test_parse_xforwarded')
    
    request = Request(
    'GET',
    'http://sanic.herokuapp.com/test',
    # 'http://127.0.0.1:5000/test',
    headers={
        # "X-Forwarded-For": "192.0.2.43, 2001:db8:cafe::17",
        "X-Forwarded-For": "2001:db8:cafe::17",
        "X-Forwarded-Port": "443",
        # "X-Forwarded-Port": "80",
        "X-Forwarded-Proto": "https"}
    )

# Generated at 2022-06-14 07:20:16.945569
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {
        "x-forwarded-host": "fake-host",
        "x-forwarded-proto": "https",
        "x-forwarded-path": "my-path"
    }
    options = parse_xforwarded(headers)
    assert options.get("proto") == "https"
    assert options.get("host") == "fake-host"
    assert options.get("path") == "my-path"

# Generated at 2022-06-14 07:20:23.485980
# Unit test for function parse_forwarded
def test_parse_forwarded():
    test_str = 'for=192.0.2.60;proto=https, for=192.0.2.43;proto=http, for=192.0.2.61;proto=http, for=192.0.2.43;proto=http'
    assert parse_forwarded(test_str, None) == {'for': '192.0.2.61', 'proto': 'http'}

# Generated at 2022-06-14 07:20:54.229322
# Unit test for function parse_forwarded
def test_parse_forwarded():
    headers = {
        "forwarded": "For=1.2.3.4;By=me;Secret=\"my_secret\", For=1.2.3.5;By=You"
    }
    assert parse_forwarded(headers, "my_secret") == {
        "for": "1.2.3.4",
        "by": "me",
        "secret": "my_secret",
    }



# Generated at 2022-06-14 07:21:06.156554
# Unit test for function parse_forwarded
def test_parse_forwarded():
    from sanic.config import Config

    header = "By=192.0.2.43, For=\"[2001:db8:cafe::17]:4711\", For=192.0.2.43"
    options = parse_forwarded({"forwarded": header}, Config(FORWARDED_SECRET="x"))
    assert options == {'by': '192.0.2.43', 'for': '192.0.2.43'}
    options = parse_forwarded({"forwarded": header}, Config(FORWARDED_SECRET="y"))
    assert options is None
    header = (
        "By=192.0.2.43, For=\"[2001:db8:cafe::17]:4711\", "
        "For=192.0.2.43, For=unknown"
    )
    options = parse_

# Generated at 2022-06-14 07:21:17.706163
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from sanic.config import Config
    from types import SimpleNamespace
    config=Config()
    config.PROXIES_COUNT=2
    config.FORWARDED_FOR_HEADER="X_FORWARDED_FOR"
    config.REAL_IP_HEADER = "X_REAL_IP"
    headers=SimpleNamespace()
    def setheader(key,value):
        if hasattr(headers,key):
            return
        else:
            setattr(headers,key,value)
    setheader("X_REAL_IP","10.0.0.1")
    setheader("X_FORWARDED_FOR","10.0.0.2, 10.0.0.3, 10.0.0.4")  # More entries than proxies