

# Generated at 2022-06-14 07:11:21.720500
# Unit test for function fwd_normalize
def test_fwd_normalize():
    s = fwd_normalize((('for', 'unknown'), ('proto', 'https'), ('host', 'test.com'), ('port', '8080'), ('path', '/login')))
    assert s == {'proto': 'https', 'host': 'test.com', 'port': 8080, 'path': '/login'}
    s = fwd_normalize((('for', 'google.com'),))
    assert s == {'for': 'google.com'}
    s = fwd_normalize((('for', '2001:0db8:85a3:0000:0000:8a2e:0370:1234'),))
    assert s == {'for': '[2001:0db8:85a3:0000:0000:8a2e:0370:1234]'}

# Generated at 2022-06-14 07:11:26.296581
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = read_headers("""
        content-length: 15
        x-forwarded-host: 1.1.1.1:1234,2.2.2.2:5678
        x-forwarded-for: 1.1.1.1,2.2.2.2,3.3.3.3
        x-forwarded-path: /path
        x-forwarded-proto: https
        user-agent: curl/7.54.0
        host: localhost:8081
        """)
    xf = parse_xforwarded(headers, None)

# Generated at 2022-06-14 07:11:40.399264
# Unit test for function fwd_normalize
def test_fwd_normalize():
    data = [
        ("127.0.0.1", "127.0.0.1"),
        ("zetan.in", "zetan.in"),
        ("[::1]", "[::1]"),
        ("\u261e", "\u261e"),
        ("-", "-"),
        ("_\u261e", "_\u261e"),
        ("_Zetan", "_Zetan"),
        ("unknown", None),
    ]
    for addr, exp in data:
        try:
            assert fwd_normalize_address(addr) == exp
        except AssertionError as e:
            print("fwd_normalize_address('%s') == %s, expected %s" % (addr, exp, e))
        except ValueError:
            assert exp is None
        except:
            print

# Generated at 2022-06-14 07:11:54.262146
# Unit test for function parse_forwarded
def test_parse_forwarded():
    from sanic.config import Config, ConfigAttribute
    from sanic.request import RequestParameters
    from sanic.response import HTTPResponse
    # Unit test for function parse_forwarded
    def mock_config(proxies_count=None, FORWARDED_SECRET="", REAL_IP_HEADER="", FORWARDED_FOR_HEADER=""):
        class MockConfig(Config):
            PROXIES_COUNT = ConfigAttribute(proxies_count)
            FORWARDED_SECRET = ConfigAttribute(FORWARDED_SECRET)
            REAL_IP_HEADER = ConfigAttribute(REAL_IP_HEADER)
            FORWARDED_FOR_HEADER = ConfigAttribute(FORWARDED_FOR_HEADER)

        return MockConfig()


# Generated at 2022-06-14 07:12:07.762775
# Unit test for function parse_forwarded
def test_parse_forwarded():
    # Example from RFC 7239, section 4
    s = 'for=192.0.2.60; proto=http; by=203.0.113.43'
    assert parse_forwarded({"Forwarded": s}, AttrDict(FORWARDED_SECRET="")) == {
        "for": "192.0.2.60",
        "proto": "http",
        "by": "203.0.113.43",
    }

    # Some other examples

# Generated at 2022-06-14 07:12:21.877235
# Unit test for function parse_forwarded
def test_parse_forwarded():
    import sanic.request
    from unittest.mock import Mock

    # Test defaults
    mock_headers = [Mock(spec=[], return_value=None), Mock(spec=[], return_value=[])]
    config = sanic.request.Request.app.config_dict['test'].copy()
    config['FORWARDED_SECRET'] = None
    assert parse_forwarded(mock_headers[0], config) is None
    assert parse_forwarded(mock_headers[1], config) is None

    # Test valid headers
    mock_headers = [
        Mock(spec=[], return_value=["by=sanic-forwarded-by"]),
        Mock(spec=[], return_value=["by=sanic-forwarded-by"]),
    ]

# Generated at 2022-06-14 07:12:35.109594
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from sanic import Sanic
    from sanic.request import Header
    app = Sanic()
    app.config.FORWARDED_FOR_HEADER = "Forwarded"
    app.config.PROXIES_COUNT = 1
    headers = Header({"Forwarded":"for=1.2.3.4; by=5.6.7.8"})
    assert app.config.PROXIES_COUNT == 1
    assert "for" in parse_xforwarded(headers, app.config)
    assert "by" not in parse_xforwarded(headers, app.config)
    app.config.PROXIES_COUNT = 2
    assert "by" in parse_xforwarded(headers, app.config)

# Generated at 2022-06-14 07:12:47.308929
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from sanic.app import Sanic
    from sanic.request import RequestParameters

    app = Sanic('test_parse_xforwarded')
    app.config.REAL_IP_HEADER = None

    @app.middleware('request')
    async def real_ip(request):
        request['real_ip_address'] = request.ip
        request['proxy_address'] = request.proxy_ip

    @app.route('/')
    async def test(request):
        return text(f'{request["real_ip_address"]}:{request["proxy_address"]}')


# Generated at 2022-06-14 07:13:01.333115
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {
        'X-Forwarded-For': '10.0.0.2, 10.0.0.1',
        'X-Scheme': 'https',
        'X-Forwarded-Host': 'host.com:8080',
        'X-Forwarded-Port': '443',
        'X-Forwarded-Path': 'path/to/here'
    }

    config = {
        'REAL_IP_HEADER': 'nonexistent',
        'PROXIES_COUNT': '2',
        'FORWARDED_FOR_HEADER': 'x-forwarded-for',
        'FORWARDED_SECRET': 'nonexistent'
    }


# Generated at 2022-06-14 07:13:12.674824
# Unit test for function parse_forwarded
def test_parse_forwarded():
    headers = [
        "for=192.0.2.60;proto=http;by=203.0.113.43",
        "for=192.0.2.43,for=198.51.100.17,for=192.0.2.61",
        "for=192.0.2.43,for=198.51.100.17,for=192.0.2.61;secret=\"xyz\"",
    ]
    assert parse_forwarded(headers[0], {'FORWARDED_SECRET': "xyz"}) is None
    assert parse_forwarded(headers[1], {'FORWARDED_SECRET': "xyz"}) is None

# Generated at 2022-06-14 07:13:25.253739
# Unit test for function parse_forwarded
def test_parse_forwarded():
    import requests
    s = "for=10.1.2.3,by=toto,proto=hTTp,host=toto.com/tutu,Port=443,paTH=tutu/tata"
    r = requests.Request(
        "get", "https://localhost:443", headers={"forwarded": s})
    f = r.headers.getall("forwarded")
    assert f == ["for=10.1.2.3, by=toto, proto=hTTp, host=toto.com/tutu, Port=443, paTH=tutu/tata"]
    opt = parse_forwarded(r.headers, r.config)

# Generated at 2022-06-14 07:13:33.347879
# Unit test for function fwd_normalize_address
def test_fwd_normalize_address():
    assert fwd_normalize_address("192.168.1.1") == "192.168.1.1"
    assert fwd_normalize_address("_123") == "_123"
    assert fwd_normalize_address("[::1]") == "[::1]"
    assert fwd_normalize_address("UNKNOWN") == "UNKNOWN"
    assert fwd_normalize_address("unknown") == "unknown"

# Generated at 2022-06-14 07:13:47.392825
# Unit test for function parse_forwarded
def test_parse_forwarded():
    from typing import Dict, List
    from sanic.config import Config


# Generated at 2022-06-14 07:13:58.643478
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {
        "x-real-ip": "1.3.3.7",
        "x-forwarded-for": "1.2.3.4, 3.2.1.1, 1.2.3.4, 3.2.1.1, 1.2.3.4, 3.2.1.1",
        "x-forwarded-host": "host.com, host2.com, host3.com",
        "x-forwarded-port": "1234, 5678, 90",
        "x-forwarded-proto": "http, https, https",
        "x-scheme": "http, https, https"
    }

# Generated at 2022-06-14 07:14:07.013483
# Unit test for function parse_forwarded
def test_parse_forwarded():
    assert parse_forwarded(None, None) is None
    assert parse_forwarded({"forwarded": "for=192.0.2.60;proto=http;by=203.0.113.43"}, {}) == {"for":"192.0.2.60", "proto":"http", "by":"203.0.113.43"}
    assert parse_forwarded({"forwarded": "for=192.0.2.60, for=198.51.100.17;proto=http;by=203.0.113.43"}, {}) == {"for":"198.51.100.17", "proto":"http", "by":"203.0.113.43"}

# Generated at 2022-06-14 07:14:20.469734
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from sanic.response import raw

    # Test invalid (non-integer) PROXIES_COUNT
    config = object()
    config.PROXIES_COUNT = 1.5
    config.FORWARDED_FOR_HEADER = "X-Forwarded-For"
    config.REAL_IP_HEADER = None
    headers = {"X-Forwarded-For": "192.168.1.1, 127.0.0.1"}
    assert parse_xforwarded(headers, config) == {"for": "192.168.1.1"}

    # Test invalid (negative) PROXIES_COUNT
    config = object()
    config.PROXIES_COUNT = -1
    config.FORWARDED_FOR_HEADER = "X-Forwarded-For"

# Generated at 2022-06-14 07:14:30.970745
# Unit test for function parse_forwarded
def test_parse_forwarded():
    # RFC 7239, section 4
    assert parse_forwarded(Bunch({"forwarded": ["by=_foo; For=\"", "bar\""]}), Bunch({"FORWARDED_SECRET": "_foo"})) == {"by": "_foo", "for": "bar"}
    # Section 5, examples 1 and 2
    assert parse_forwarded(Bunch({"forwarded": ["by=_foo; For=\"bar\", ", "proto=https"]}), Bunch({"FORWARDED_SECRET": "_foo"})) == {"by": "_foo", "for": "bar", "proto": "https"}

# Generated at 2022-06-14 07:14:42.310485
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {
        "x-forwarded-for": "127.0.0.1",
        "x-scheme": "http",
        "x-forwarded-host": "host",
        "x-forwarded-port": "80",
        "x-forwarded-path": "abc",
        "x-forwarded-proto": "https"
    }
    result = parse_xforwarded(headers, 1)
    print(result)
    assert result["for"] == "127.0.0.1"
    assert result["proto"] == "https"
    assert result["host"] == "host"
    assert result["port"] == 80
    assert result["path"] == "abc"

# Generated at 2022-06-14 07:14:56.162637
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    import string
    import random
    import pytest
    headers = {
        'X-Forwarded-For':'192.168.77.77',
        'X-Forwarded-Proto':'https',
        'X-Forwarded-Host':'test.com',
        'X-Forwarded-Port':'443',
        'X-Forwarded-Path':'/test'
    }
    print('Test 1: KeyError')
    with pytest.raises(KeyError):
        res = parse_xforwarded(headers, {'REAL_IP_HEADER':'aaa', 'PROXIES_COUNT':1})
    print('Test 2: Bad String')

# Generated at 2022-06-14 07:15:06.515239
# Unit test for function fwd_normalize_address
def test_fwd_normalize_address():
    assert fwd_normalize_address("unknown") == "unknown"
    assert fwd_normalize_address("_fake_ipv4") == "_fake_ipv4"
    assert fwd_normalize_address("192.168.0.2") == "192.168.0.2"
    assert fwd_normalize_address("192.168.0.2") == "192.168.0.2"
    assert fwd_normalize_address("::1") == "[::1]"
    assert fwd_normalize_address("FC00::") == "[fc00::]"



# Generated at 2022-06-14 07:15:19.721047
# Unit test for function parse_host
def test_parse_host():
    for host, port in (
        ('localhost', None),
        ('localhost:80', 80),
        ('[127.0.0.1]', None),
        ('[127.0.0.1]:80', 80),
    ):
        assert parse_host(host) == (host, port)




# Generated at 2022-06-14 07:15:33.474133
# Unit test for function parse_xforwarded
def test_parse_xforwarded():

    class Mock(object):
        def __init__(self, d):
            self.__dict__ = d

    class MockHeaders(dict):
        def get(self, item):
            return self[item]

    headers = MockHeaders(
        {
            "x-scheme": "http",
            "x-forwarded-host": "127.0.0.1",
            "x-forwarded-port": "8888",
            "x-forwarded-proto": "http",
            "x-forwarded-path": "/path/",
        }
    )

    config = Mock(
        {
            "REAL_IP_HEADER": "x-real-ip",
            "FORWARDED_FOR_HEADER": "x-forwarded-for",
        }
    )

    config.PROX

# Generated at 2022-06-14 07:15:47.696307
# Unit test for function parse_forwarded
def test_parse_forwarded():
    assert parse_forwarded(
        {'forwarded': 'For="_gazonk" , FOR="[127.0.0.1]" , By=_foo;'},
        {'FORWARDED_SECRET': '_foo'}
    ) == {'by': '_foo', 'for': '_gazonk'}
    assert parse_forwarded(
        {'forwarded': 'By=_foo;For="[127.0.0.1]" ;  FOR="[127.0.0.1]"'},
        {'FORWARDED_SECRET': '_foo'}
    ) == {'by': '_foo', 'for': '_ipv6'}

# Generated at 2022-06-14 07:15:55.609974
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    assert parse_xforwarded({'X-FORWARDED-PROTO': 'http,https'}, {}) == {'proto': 'http'}
    assert parse_xforwarded({'X-FORWARDED-FOR': 'http,https'}, {}) == {'for': 'http'}
    assert parse_xforwarded({'X-FORWARDED-PATH': 'http,https'}, {}) == {'path': 'http'}
    assert parse_xforwarded({'X-FORWARDED-HOST': 'http,https'}, {}) == {'host': 'http'}
    assert parse_xforwarded({'X-FORWARDED-PORT': 'http,https'}, {}) == {'port': 'http'}

# Generated at 2022-06-14 07:15:59.284545
# Unit test for function parse_forwarded
def test_parse_forwarded():
    result = parse_forwarded("for=127.0.0.1;host=example.com;proto=http", "test_secret")
    assert isinstance(result, dict) is True

# Generated at 2022-06-14 07:16:08.288079
# Unit test for function parse_forwarded
def test_parse_forwarded():
    raw_forwarded = 'for="[2001:db8:cafe::17]:4711",by="[2001:db8:cafe::1]";secret="abc123",for="[2001:db8:cafe::1]:80"'
    secret = 'abc123'
    parsed = parse_forwarded(raw_forwarded, secret)

    assert parsed['by'] == '[2001:db8:cafe::1]'
    assert parsed['for'] == '[2001:db8:cafe::1]:80'
    assert parsed['secret'] == 'abc123'


# Generated at 2022-06-14 07:16:21.595848
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from sanic.compat import PY_35
    from io import BytesIO
    from tempfile import TemporaryFile, SpooledTemporaryFile
    from wsgiref.validate import validator
    from wsgiref.handlers import format_date_time

    from sanic.response import HTTPResponse
    from sanic.request import Request
    from sanic import Sanic
    from sanic.exceptions import InvalidUsage
    from sanic.websocket import WebSocketProtocol
    from sanic.log import logger

    app = Sanic()
    app.config.PROXIES_COUNT = 1

    async def get_ws(request, ws):
        pass

    async def get_http(request):
        return HTTPResponse("success")


# Generated at 2022-06-14 07:16:29.582900
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers={'x-forwarded-for': '192.168.1.1', 'x-forwarded-port': '443', 'x-forwarded-proto': 'https', 'x-forwarded-host': '127.0.0.1', 'x-forwarded-path': '', 'host': '127.0.0.1'}
    class ConfigClass:
        def __init__(self):
            self.REAL_IP_HEADER='x-real-ip'
            self.PROXIES_COUNT=3
            self.FORWARDED_FOR_HEADER='x-forwarded-for'
    config=ConfigClass()
    print(parse_xforwarded(headers,config))

if __name__ == '__main__':
    test_parse_xforwarded()

# Generated at 2022-06-14 07:16:39.602762
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {
        'x-scheme': 'https',
        'x-forwarded-for': '1.1.1.1',
        'x-forwarded-host': 'localhost',
        'x-forwarded-port': '80',
        'x-forwarded-path': '/'
    }
    config = {
        'PROXIES_COUNT': 1,
        'REAL_IP_HEADER': None,
        'FORWARDED_FOR_HEADER': 'XX-Forwarded-For',
        'FORWARDED_SECRET': None
    }

# Generated at 2022-06-14 07:16:48.470219
# Unit test for function parse_xforwarded

# Generated at 2022-06-14 07:17:12.371007
# Unit test for function parse_forwarded
def test_parse_forwarded():
    from .websocket import WebSocketProtocol

    class config:
        FORWARDED_SECRET = "secret"
        REAL_IP_HEADER = ""
        PROXIES_COUNT = 0
        FORWARDED_FOR_HEADER = "X-Forwarded-For"

    def assert_parse_forwarded(
        header, expected, reverse=False
    ):  # pragma: no cover
        headers = {
            "forwarded": header.split(",") if header else None
        }
        assert parse_forwarded(headers, config) == expected

    assert_parse_forwarded("123", None)
    assert_parse_forwarded("secret=1234; x=y; props=123", None)
    assert_parse_forwarded("secret=1234,x=y", None)
    assert_parse_forwarded

# Generated at 2022-06-14 07:17:24.515627
# Unit test for function parse_forwarded
def test_parse_forwarded():
    """Test the minimal parsing of the Forwarded header"""
    import os
    os.environ["FORWARDED_SECRET"] = "secret"
    from sanic import Sanic
    app = Sanic("sanic-test", strict_slashes=False)
    # Test the minimal parsing

# Generated at 2022-06-14 07:17:37.779800
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    # Test the function by checking the output is correct for each value
    assert parse_xforwarded({}, {'FORWARDED_FOR_HEADER': 'X-Forwarded-For'}) is None
    assert parse_xforwarded({'X-Forwarded-For': '127.0.0.1'}, {'FORWARDED_FOR_HEADER': 'X-Forwarded-For'}) == {'for': '127.0.0.1'}
    assert parse_xforwarded({'X-Forwarded-For': '127.0.0.1,127.0.0.1'}, {'FORWARDED_FOR_HEADER': 'X-Forwarded-For'}) == {'for': '127.0.0.1'}

# Generated at 2022-06-14 07:17:43.140021
# Unit test for function parse_host
def test_parse_host():
    f = parse_host('abc.com:80')
    assert f == ('abc.com', 80)

    f = parse_host('[::1]:80')
    assert f == ('[::1]', 80)

    f = parse_host('[::1]')
    assert f == ('[::1]', None)


if __name__ == "__main__":
    test_parse_host()

# Generated at 2022-06-14 07:17:49.605587
# Unit test for function parse_forwarded
def test_parse_forwarded():
    headers = HeaderIterable({
        "Host": "example.com",
        "Forwarded": [
            "by=8.8.8.8; proto=https; host=foo.com; for=192.0.2.60; f=bar",
            "By=_secret; for=1.1.1.1, by=2.2.2.2; f=baz; host=_myhost",
        ],
    })
    config = Options({
        "FORWARDED_SECRET": "_secret",
        "PROXIES_COUNT": 2,
        "REAL_IP_HEADER": None,
        "FORWARDED_FOR_HEADER": None,
    })

# Generated at 2022-06-14 07:18:03.321247
# Unit test for function parse_forwarded
def test_parse_forwarded():
    headers = [
        "for=192.0.2.60; proto=http; host=example.com",
        "for=198.51.100.17,for=203.0.113.90;by=203.0.113.43",
        "for=192.0.2.43,for=198.51.100.17;by=203.0.113.43",
    ]
    options = [
        {"for":"192.0.2.60","proto":"http","host":"example.com"},
        {"for":"198.51.100.17","by":"203.0.113.43"},
        {"for":"202.0.113.90","by":"203.0.113.43"},
    ]

# Generated at 2022-06-14 07:18:14.319594
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    # Basic test
    headers = {
        "X-Forwarded-For": "127.0.0.1",
        "X-Forwarded-Proto": "http",
        "X-Forwarded-Host": "",
        "X-Forwarded-Port": "8000",
        "X-Forwarded-Path": "",
    }
    fwd = {
        "for": "127.0.0.1",
        "proto": "http",
        "host": "",
        "port": 8000,
        "path": "",
    }
    assert parse_xforwarded(headers, True) == fwd

    # Test different order of headers
    headers["X-Forwarded-Host"] = "example.com"
    fwd["host"] = "example.com"

# Generated at 2022-06-14 07:18:28.583196
# Unit test for function parse_forwarded
def test_parse_forwarded():
    from .request import Request
    from . import config
    from . import sanic
    from .test_utils import sanic_request

    app = sanic.Sanic(__name__)

    @app.route("/")
    def handler(request):
        return "hello"

    @app.middleware("request")
    async def update_fwd_env(request):
        fwd = parse_forwarded(request.headers, app.config)
        if not fwd:
            return
        for key, val in fwd.items():
            request.env[f"HTTP_X_FORWARDED_" + key.upper()] = val

    csrf_token = "0123456789abcdef"

# Generated at 2022-06-14 07:18:36.734406
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    # Simple test
    assert parse_xforwarded({"X-Scheme": "http"}) == {"proto": "http"}
    # Test with multiple headers
    assert parse_xforwarded({"X-Scheme": "http", "X-Forwarded-Proto": "https"}) == {"proto": "https"}
    assert parse_xforwarded({"X-Scheme": "http", "X-Forwarded-Proto": "https", "X-Forwarded-Host": "example.com"}) == {"proto": "https", "host": "example.com"}

# Generated at 2022-06-14 07:18:47.873520
# Unit test for function parse_forwarded
def test_parse_forwarded():
    headers: Dict[str,Union[str,List[str]]] = {'forwarded': [' by = [2001:0db8:85a3:0000:0000:8a2e:0370:7334]; For = "[2001:0db8:85a3:0000:0000:8a2e:0370:7334]"; Proto=https, For="[2001:0db8:85a3:0000:0000:8a2e:0370:7334]";pRoTo="https"   ']}
    config: Dict[str,str] = {'FORWARDED_SECRET': ''}
    ret = parse_forwarded(headers,config)

# Generated at 2022-06-14 07:19:08.593591
# Unit test for function parse_forwarded
def test_parse_forwarded():
    assert None == parse_forwarded({"forwarded": ["By=_proxy_;X-Forwarded-for=x"]}, None)
    assert {'for': 'x', 'by': '_proxy_'} == parse_forwarded({"forwarded": ["By=_proxy_;X-Forwarded-for=x",
                                                                             "By=_proxy_;X-Forwarded-for=y,X-Forwarded-for=z"]}, None)
    assert {'for': 'x', 'by': '_proxy_'} == parse_forwarded({"forwarded": ["By=_proxy_;X-Forwarded-for=x",
                                                                             "By=_other_;X-Forwarded-for=y,X-Forwarded-for=z"]}, "_other_")

# Generated at 2022-06-14 07:19:22.028673
# Unit test for function parse_forwarded
def test_parse_forwarded():
    """
    Simple unit tests for parse_forwarded()
    """
    # Parse `Forwarded` and `X-Forwarded-*` headers
    headers = Headers()
    assert parse_forwarded(headers, Config()) is None
    headers['Forwarded'] = 'secret=from_me, proto="this is broken, but works", ' \
                           'by="_test.server:123"; secret=should_be_ignored'
    assert parse_forwarded(headers, Config(FORWARDED_SECRET="from_me")) == \
           {'by': '_test.server:123', 'proto': '"this is broken, but works"'}
    assert parse_forwarded(headers, Config(FORWARDED_SECRET="should_be_ignored")) is None
    assert parse_forwarded(headers, Config()) is None

# Generated at 2022-06-14 07:19:33.374189
# Unit test for function parse_forwarded
def test_parse_forwarded():
    assert parse_forwarded([""], "") == None
    assert parse_forwarded(None, "") == None
    assert parse_forwarded(["123"], "123") == None
    assert parse_forwarded(["123abc"], "abc") == None
    assert parse_forwarded(["abc123"], "abc") == None

    # Test: with good secret
    headers = [
        "for=192.0.2.60; proto=https; by=203.0.113.43",
        "for=192.0.2.61; by=203.0.113.43",
        "for=192.0.2.62; by=203.0.113.44",
        "for=192.0.2.63; by=203.0.113.45",
    ]

# Generated at 2022-06-14 07:19:37.888938
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = DictHeader({"x-forwarded-for": "6.5.4.3, 1.2.3.4, 9.8.7.6",
                          "x-forwarded-host": "foo.bar",
                          "x-forwarded-port": "12345"})
    config = SimpleNamespace(REAL_IP_HEADER="", PROXIES_COUNT=3, FORWARDED_FOR_HEADER="x-forwarded-for")
    forwarded = parse_xforwarded(headers, config)
    assert forwarded == {"for": "1.2.3.4", "host": "foo.bar", "port": 12345}


# Generated at 2022-06-14 07:19:41.384424
# Unit test for function parse_content_header
def test_parse_content_header():
    assert parse_content_header("form-data; name=upload; filename=\"file.txt\"") == ('form-data', {"name":"upload", "filename":"file.txt"})

# Generated at 2022-06-14 07:19:55.323678
# Unit test for function parse_forwarded
def test_parse_forwarded():
    import urllib.parse
    import collections
    forward_header = "for=192.0.2.60; proto=http; by=203.0.113.43"
    reverse_forward_header = "for=192.0.2.60; proto=http; by=203.0.113.43"
    result = urllib.parse.parse_qs(forward_header)
    reverse_result = urllib.parse.parse_qs(reverse_forward_header)
    print(result)
    print(reverse_result)
    print(type(result))
    print(type(reverse_result))
    result = collections.OrderedDict(result)
    print(result)
    print(type(result))
    #result = collections.OrderedDict(result)
    #reverse_result = collections.Ordered

# Generated at 2022-06-14 07:20:09.187340
# Unit test for function parse_forwarded
def test_parse_forwarded():
    import unittest
    import urllib.parse

    class parse_forwarded_TestCase(unittest.TestCase):
        """Parse the Forwarded header."""

        def test_forwarded_parser(self):
            """Forwarded parser test."""
            import asyncio
            from sanic import Sanic
            from sanic.testing import HOST, PORT, SanicTestClient

            app = Sanic("test_forwarded")

            @app.route("/")
            async def handler(request):
                return text(request.forwarded)

            @app.listener("before_server_start")
            def fix_forwarded_port(app, loop):
                # Temporary fix for the port, because
                # the default port is not a standard one
                app.config.REVERSE_PROXY_PORT = PORT

# Generated at 2022-06-14 07:20:21.359996
# Unit test for function parse_forwarded
def test_parse_forwarded():
    from sanic.config import Config
    from sanic.request import Request
    from sanic.response import text
    from sanic.views import CompositionView

    class ForwardedView(CompositionView):

        @staticmethod
        def get(request: Request) -> str:
            fwd = parse_forwarded(request.headers, Config())
            assert fwd is None
            return text("test")

    assert ForwardedView.as_view()(None).body == b"test"
    assert ForwardedView.as_view()(None).status == 200

    class ForwardedView(CompositionView):

        @staticmethod
        def get(request: Request) -> str:
            fwd = parse_forwarded(request.headers, Config(FORWARDED_SECRET=None))
            assert fwd is None
            return text("test")

# Generated at 2022-06-14 07:20:30.727446
# Unit test for function parse_forwarded
def test_parse_forwarded():
    headers = {"forwarded": "By=<https://www.example.com>; Secret=123"}
    config = {"FORWARDED_SECRET": "123"}
    assert parse_forwarded(headers, config) == {
        "by": "https://www.example.com"
    }
    headers = {"forwarded": "By=<https://www.example.com>; Secret=124"}
    config = {"FORWARDED_SECRET": "123"}
    assert parse_forwarded(headers, config) is None
    headers = {"forwarded": "Secret=123; By=<https://www.example.com>"}
    config = {"FORWARDED_SECRET": "123"}
    assert parse_forwarded(headers, config) is None

# Generated at 2022-06-14 07:20:43.072709
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {
        'x-forwarded-for': '192.168.2.2',
        'x-forwarded-proto': 'https',
        'x-forwarded-port': '443',
        'x-forwarded-host': 'example.com',
        'x-forwarded-path': '/path/to/resource',
    }
    config = {
        'PROXIES_COUNT': 0,
        'REAL_IP_HEADER': '',
        'FORWARDED_SECRET': '',
        'FORWARDED_FOR_HEADER': 'x-forwarded-for',
    }
    res = parse_xforwarded(headers, config)
    print(res)


if __name__ == '__main__':
    test_parse_xforwarded()

# Generated at 2022-06-14 07:21:07.238071
# Unit test for function parse_forwarded
def test_parse_forwarded():
    from sanic.config import Config
    from multidict import CIMultiDict

    config = Config()
    config.PROXIES_COUNT = 0
    config.FORWARDED_SECRET = "test"

    # test static value
    headers = CIMultiDict({'Forwarded': 'secret=test'})
    ret = parse_forwarded(headers, config)
    assert ret == {}

    headers = CIMultiDict({'Forwarded': 'for=127.0.0.1;secret=test'})
    ret = parse_forwarded(headers, config)
    assert ret == {'for': '127.0.0.1'}

    headers = CIMultiDict({'Forwarded': 'for=127.0.0.1, for=127.0.0.2'})