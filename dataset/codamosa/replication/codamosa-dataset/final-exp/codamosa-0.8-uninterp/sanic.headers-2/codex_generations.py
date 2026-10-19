

# Generated at 2022-06-14 07:11:34.978702
# Unit test for function fwd_normalize
def test_fwd_normalize():
    fwd = fwd_normalize([("secret", "bhu2"), ("for", "192.168.1.1"),
                         ("proto", "http"), ("port", "8000"),
                         ("host", "localhost"), ("by", "foo"),
                         ("path", "/users"), ("unknown", "keys")])
    assert fwd["secret"] == "bhu2"
    assert fwd["for"] == "192.168.1.1"
    assert fwd["proto"] == "http"
    assert fwd["port"] == 8000
    assert fwd["host"] == "localhost"
    assert fwd["by"] == "foo"
    assert fwd["path"] == "/users"
    assert 'unknown' not in fwd

# Generated at 2022-06-14 07:11:38.579182
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {}
    headers["a"] = "test"
    headers["test"] = "test1"

    assert parse_xforwarded(headers, None) == None

# Generated at 2022-06-14 07:11:46.519246
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {"X-Forwarded-For": "192.168.1.1, 129.78.138.66, 127.0.0.1"}
    config = {"FORWARDED_FOR_HEADER": "X-Forwarded-For", "PROXIES_COUNT": 1}
    result = parse_xforwarded(headers, config)
    assert result == {"for": "127.0.0.1"}

# Generated at 2022-06-14 07:11:52.666168
# Unit test for function parse_content_header
def test_parse_content_header():
    content_type = 'multipart/form-data; name="upload"; filename="file.txt"'
    expected = ('multipart/form-data', {
                'name': 'upload',
                'filename': 'file.txt'
                })
    result = parse_content_header(content_type)
    assert result == expected

# Generated at 2022-06-14 07:12:06.147703
# Unit test for function fwd_normalize_address
def test_fwd_normalize_address():
    assert fwd_normalize_address("192.168.0.1") == "192.168.0.1"
    assert fwd_normalize_address("fe80::a00:27ff:fe48:e731") == "[fe80::a00:27ff:fe48:e731]"
    assert fwd_normalize_address("fe80::a00:27ff:fe48:e731") == "[fe80::a00:27ff:fe48:e731]"
    assert fwd_normalize_address("_AB:eC0:9D") == "_AB:eC0:9D"

if __name__ == "__main__":
    test_fwd_normalize_address()

# Generated at 2022-06-14 07:12:13.841795
# Unit test for function fwd_normalize
def test_fwd_normalize():
    assert fwd_normalize([("by", "192.0.2.1")]) == {"by": "192.0.2.1"}

    assert fwd_normalize([("by", "unknown")]) == {}

    assert fwd_normalize([("proto", "https")]) == {"proto": "https"}

    assert fwd_normalize([("proto", "UNKNOWN")]) == {"proto": "unknown"}

    assert fwd_normalize([("port", "8080")]) == {"port": 8080}

    assert fwd_normalize([("port", "foo")]) == {}

    assert fwd_normalize([("port", "65000")]) == {}

    assert fwd_normalize([("path", "")]) == {"path": ""}


# Generated at 2022-06-14 07:12:25.117756
# Unit test for function parse_forwarded
def test_parse_forwarded():
    # parsed output of parse_forwarded, strict IP address checking:
    assert parse_forwarded({"forwarded": "for=192.172.2.2;by=secret"}, type(
        "Config", (object,), {"FORWARDED_SECRET": "secret"})) == {
            "for": "192.172.2.2"
        }
    # No secret found, should return none:
    assert parse_forwarded({"forwarded": "for=192.172.2.2"}, type(
        "Config", (object,), {"FORWARDED_SECRET": "secret"})) is None
    # Wrong secret found, should return none:

# Generated at 2022-06-14 07:12:34.644801
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    fake_headers = {
        'X-Forwarded-For': '192.0.2.0',
        'X-Forwarded-Host': 'fakehost',
        'X-Forwarded-Port': '8080',
        'X-Forwarded-Proto': 'http',
    }
    expected = {
        'for': '192.0.2.0',
        'proto': 'http',
        'host': 'fakehost',
        'port': 8080,
    }
    parsed = parse_xforwarded(fake_headers, None)
    assert parsed == expected

# Generated at 2022-06-14 07:12:43.002869
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {'content-type': 'text/plain; charset=utf-8', 'content-length': '16', 'x-forwarded-proto': 'http', 'host': '127.0.0.1:8000', 'x-forwarded-for': '127.0.0.1', 'connection': 'close'}
    config = {'REAL_IP_HEADER': 'x-real-ip', 'FORWARDED_FOR_HEADER': 'x-forwarded-for', 'PROXIES_COUNT': 0}
    print(parse_xforwarded(headers, config))
    print(parse_xforwarded(headers, config)['proto'])
    print(parse_xforwarded(headers, config)['for'])

if __name__ == "__main__":
    test_parse_xforward

# Generated at 2022-06-14 07:12:46.782408
# Unit test for function parse_content_header
def test_parse_content_header():
    assert parse_content_header('application/json; charset=utf-8') == ('application/json', {'charset': 'utf-8'})

# Generated at 2022-06-14 07:13:03.865396
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    """
    Test function parse_xforwarded
    """
    IPv4_and_IPv6 = [
        '::1',
        '127.0.0.1',
        '192.168.0.1',
        '8.8.8.8',
        '2001:0db8:85a3:0042:1000:8a2e:0370:7334',
        '2001:db8::1',
    ]


# Generated at 2022-06-14 07:13:11.239244
# Unit test for function parse_forwarded
def test_parse_forwarded():
    from sanic.config import SanicConfig
    from sanic.request import Headers
    config = SanicConfig()
    config.FORWARDED_SECRET = "secret"
    dummy_header = b"for=localhost; by=localhost; secret=secret, for=localhost"
    headers = Headers({"forwarded": [dummy_header]})
    assert parse_forwarded(headers, config) == {"for": "localhost"}

    dummy_header = b"for=localhost; by=localhost; secret=secret2, for=localhost, for=localhost"
    headers = Headers({"forwarded": [dummy_header]})
    assert parse_forwarded(headers, config) == {"for": "localhost"}


# Generated at 2022-06-14 07:13:22.320632
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    h = {'X-Forwarded-For': '192.168.0.1, 10.0.0.1'}
    assert parse_xforwarded(h, {'FORWARDED_FOR_HEADER':'X-Forwarded-For'}) == {'for': '192.168.0.1'}
    h = {'X-Forwarded-For': '192.168.0.1, 10.0.0.1', 'X-Scheme': 'https', 'X-Forwarded-Host': 'test_host', 'X-Forwarded-Port': '8443'}

# Generated at 2022-06-14 07:13:33.129318
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from sanic.config import Config
    from sanic.request import Request
    config = Config()
    config.REAL_IP_HEADER = 'x-real-ip'
    config.PROXIES_COUNT = 3
    config.FORWARDED_FOR_HEADER = 'x-forwarded-for'
    config.FORWARDED_PROTO_HEADER = 'x-forwarded-proto'
    config.FORWARDED_HOST_HEADER = 'x-forwarded-host'
    config.FORWARDED_PORT_HEADER = 'x-forwarded-port'
    config.FORWARDED_PATH_HEADER = 'x-forwarded-path'
    config.FORWARDED_SECRET = 'test'

# Generated at 2022-06-14 07:13:47.228549
# Unit test for function parse_forwarded

# Generated at 2022-06-14 07:14:01.239914
# Unit test for function parse_forwarded
def test_parse_forwarded():
    from pprint import pprint
    from sanic import Sanic
    from sanic.config import Config

    config = Config()
    config.FORWARDED_SECRET = "test"

    headers = {}
    s = Sanic("test_parse_forwarded", config=config)
    fwd = parse_forwarded(s.request_class(headers).headers, s.config)
    pprint(fwd)
    assert fwd is None

    headers = {
        "FORWARDED": "for=192.0.2.43,for=198.51.100.17;by=203.0.113.60;proto=http",
    }
    s = Sanic("test_parse_forwarded", config=config)
    fwd = parse_forwarded(s.request_class(headers).headers, s.config)

# Generated at 2022-06-14 07:14:11.536026
# Unit test for function parse_forwarded
def test_parse_forwarded():
    forwarded_str="for=192.0.2.60;proto=http;host=example.com;port=80;path=/foo;by=192.0.2.43,for=192.0.2.43;proto=http;host=example.com;port=80;path=/bar;by=192.0.2.60"
    result = parse_forwarded(forwarded_str, "192.0.2.43")
    assert result == {'by': '192.0.2.43', 'for': '192.0.2.60', 'host': 'example.com', 'port': 80, 'proto': 'http', 'path': '/foo'}

# Generated at 2022-06-14 07:14:18.959093
# Unit test for function parse_forwarded
def test_parse_forwarded():
    headers ={'Forwarded': 'for=192.0.2.60;proto=http;by=203.0.113.43, for="[2001:db8:cafe::17]:4711";by="[2001:db8:cafe::17]"  , for=192.0.2.43, for=198.51.100.17, for=198.51.100.17'}
    from sanic.config import Config
    config = Config()
    config.FORWARDED_SECRET = 'sanic'
    config.PROXIES_COUNT = 1
    config.REAL_IP_HEADER = 'X-Real-Ip'
    config.FORWARDED_FOR_HEADER = 'X-Forwarded-For'
    print(parse_forwarded(headers, config))

# Generated at 2022-06-14 07:14:30.104751
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from sanic import Sanic
    from sanic.request import Request
    from sanic.config import Config
    from sanic.response import HTTPResponse

    class MockApp(Sanic):
        def __init__(self, config=None, test_name=""):
            super().__init__(config=config)
            self.name = test_name

    # TODO: change these test cases

# Generated at 2022-06-14 07:14:35.525937
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from sanic.config import Config
    from multidict import CIMultiDict
    from collections import namedtuple
    from http.cookies import SimpleCookie
    from sanic.cookies import Cookie

    tuple_util = namedtuple("tuple_util", ["key", "value"])

    config = Config()
    config.PROXIES_COUNT = 1
    config.FORWARDED_FOR_HEADER = "X-FORWARDED-FOR"

    cookie = SimpleCookie()
    cookie["sessionid_test"] = "123456789"
    cookie["sessionid_test"]["httponly"] = True
    cookie["sessionid_test"]["path"] = "/"
    cookie["sessionid_test"]["expires"] = "Fri, 31 Dec 9999 23:59:59 GMT"

   

# Generated at 2022-06-14 07:14:53.989906
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    """
    function test_parse_xforwarded() will unit test function parse_xforwarded()
    """
    from collections import namedtuple
    from .config import Config
    from . import Sanic
    from .helpers import parse_xforwarded
    
    class FakeRequest:
        def __init__(self, headers):
            self.headers = headers

    class FakeConfig:
        def __init__(self):
            self.REAL_IP_HEADER = 'x-real-ip'
            self.PROXIES_COUNT = 2
            self.FORWARDED_FOR_HEADER = 'x-forwarded-for'

    sanic = Sanic('test_parse_xforwarded')
    sanic.config = FakeConfig()

    # test function parse_xforwarded() with a valid x-real-ip header

# Generated at 2022-06-14 07:15:03.157909
# Unit test for function parse_xforwarded
def test_parse_xforwarded():

    forwarded_headers = {
        'x-forwarded-for': '127.0.0.1',
        'x-forwarded-host': 'host',
        'x-forwarded-port': '80',
        'x-forwarded-proto': 'http',
        'x-forwarded-path': 'path'
    }

    config = {
        'FORWARDED_FOR_HEADER': 'x-forwarded-for',
        'FORWARDED_HOST_HEADER': 'x-forwarded-host',
        'FORWARDED_PORT_HEADER': 'x-forwarded-port',
        'FORWARDED_PROTO_HEADER': 'x-forwarded-proto',
        'FORWARDED_PATH_HEADER': 'x-forwarded-path'
    }

    forwarded = parse_x

# Generated at 2022-06-14 07:15:14.593412
# Unit test for function parse_forwarded
def test_parse_forwarded():
    assert parse_forwarded({'Forwarded': ['host=192.0.2.60;by=203.0.113.43;for=192.0.2.43']}, 'host=192.0.2.60;by=203.0.113.43;for=192.0.2.43') == None
    assert parse_forwarded({'Forwarded': ['host=192.0.2.60;by=203.0.113.43;for=192.0.2.43']}, 'host=192.0.2.60;by=203.0.113.43;secret=a-secret-value') == 0

# Generated at 2022-06-14 07:15:21.766160
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    # Should be correct
    headers = {'X-Forwarded-Host': 'a.pizzamixer.org', 'X-Scheme': 'https'}
    res = parse_xforwarded(headers)
    assert res['host'] == 'a.pizzamixer.org'
    assert res['proto'] == 'https'

    # Should not be overwritten
    headers = {'X-Forwarded-Host': 'a.pizzamixer.org', 'X-Scheme': 'https', 'X-Forwarded-Proto': 'http'}
    res = parse_xforwarded(headers)
    assert res['host'] == 'a.pizzamixer.org'
    assert res['proto'] == 'https'

    # Should not crash

# Generated at 2022-06-14 07:15:34.745920
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    # Valid X-Forwarded-For value
    assert parse_xforwarded({
        'x-forwarded-for': '1.2.3.4'
        }, None) == {
        'for': '1.2.3.4'
    }
    # Valid X-Forwarded-For value with port
    assert parse_xforwarded({
        'x-forwarded-for': '1.2.3.4:8080'
        }, None) == {
        'for': '1.2.3.4'
    }
    # Invalid X-Forwarded-For value
    assert parse_xforwarded({
        'x-forwarded-for': '1.2.3.4:8080:8080'
        }, None) == None

    # More specific header will override more general header
    assert parse_x

# Generated at 2022-06-14 07:15:49.160412
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    parse_xforwarded_headers = {
        "REMOTE_ADDR": "127.0.0.1",
        "X-FORWARDED-FOR": "127.0.0.1",
        "X-FORWARDED-HOST": "localhost",
        "X-FORWARDED-PORT": "80",
        "X-FORWARDED-PROTO": "http"
    }

# Generated at 2022-06-14 07:15:57.788968
# Unit test for function parse_forwarded
def test_parse_forwarded():
    import requests
    r = requests.post("http://localhost:8000/")
    a = r.headers['Forwarded']
    print(a)
    b = parse_forwarded(a)
    print(b)
    # print(b.__dict__)
    # print(b.__dir__())
    # print(dir(b))
    print(repr(b))
    # print(f"{b}")
    # print(b.__str__())
    # print(b.__unicode__())
    # print(b.__bytes__())


if __name__ == '__main__':
    test_parse_forwarded()

# Generated at 2022-06-14 07:16:09.269443
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    h = {"x-forwarded-for": "127.0.0.1"}
    print(parse_xforwarded(h, {"REAL_IP_HEADER": None, "PROXIES_COUNT": 1}))
    print(parse_xforwarded(h, {"REAL_IP_HEADER": "x-forwarded-for", "PROXIES_COUNT": 1}))
    print(parse_xforwarded(h, {"REAL_IP_HEADER": "x-forwarded-for", "PROXIES_COUNT": 0}))
    h = {
        "x-forwarded-for": "127.0.0.1,127.0.0.2",
        "x-forwarded-host": "localhost",
        "x-forwarded-proto": "http",
    }
    print

# Generated at 2022-06-14 07:16:17.244772
# Unit test for function parse_forwarded
def test_parse_forwarded():
    s="""
    For=192.0.2.60; Proto=http; By=203.0.113.43
    By=203.0.113.43; For="[2001:db8:cafe::17]"; Proto=https,
    by=unknown;For=192.0.2.43, For=198.51.100.17;
    """
    print(parse_forwarded(s,))


# Generated at 2022-06-14 07:16:25.234010
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    x = {'x-forwarded-for': 'http://wild-wild-west.com',
        'x-scheme': 'https',
        'x-forwarded-path': '/sanic'
    }
    a = parse_xforwarded(x, None)
    assert a["for"] == "http://wild-wild-west.com"
    assert a["proto"] == "https"
    assert a["path"] == "/sanic"

# Generated at 2022-06-14 07:16:49.194671
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {
        "x-forwarded-for": "8.8.8.8",
        "x-scheme": "https",
        "x-forwarded-host": "example.com",
        "x-forwarded-port": "443",
        "x-forwarded-proto": "https",
        "x-forwarded-path": "/q=1",
    }
    ret1 = parse_xforwarded(headers, {"PROXIES_COUNT": 1})
    ret2 = parse_xforwarded(headers, {"PROXIES_COUNT": 2})
    ret3 = parse_xforwarded(headers, {"PROXIES_COUNT": 3})
    assert ret1 is not None
    assert ret2 is not None
    assert ret3 is None

# Generated at 2022-06-14 07:16:57.809742
# Unit test for function parse_forwarded
def test_parse_forwarded():
    from sanic.config import Config
    from sanic.request import Request
    from sanic.server import HOST, PORT
    headers = {"Forwarded": "by=%s;host=%s:%d;proto=https" % (HOST, HOST, PORT)}
    config = Config(FORWARDED_SECRET=HOST)
    request = Request("GET", "/", headers=headers, config=config)
    assert request.forwarded_protocol == "https"
    assert request.forwarded_path == "/"
    assert request.forwarded_port == PORT
    assert request.forwarded_host == HOST
    assert request.forwarded_scheme == "https"

# Generated at 2022-06-14 07:17:08.522348
# Unit test for function parse_forwarded
def test_parse_forwarded():
    headers = {
        "forwarded": "for=10.0.0.1;proto=http;host=localhost:80;secret=secret;by=10.0.0.2",
        "Forwarded": "by=10.0.0.3;secret=secret;for=10.0.0.2",
    }
    config = {"FORWARDED_SECRET": "secret"}

    assert parse_forwarded(headers, config) == {
        "for": "10.0.0.1",
        "proto": "http",
        "host": "localhost:80",
        "secret": "secret",
        "by": "10.0.0.2",
    }
    # Test parsing with an invalid config
    config = {"FORWARDED_SECRET": "secret_"}
    assert parse_forwarded

# Generated at 2022-06-14 07:17:16.344783
# Unit test for function parse_xforwarded
def test_parse_xforwarded():

    # Test CONF_FORWADED_HEADER
    CONF_FORWADED_HEADER = "x-forwarded-for"
    CONF_FORWADED_FOR_HEADER = "x-forwarded-for"
    CONF_FORWADED_HOST_HEADER = "x-forwarded_host"
    CONF_FORWADED_PORT_HEADER = "x-forwarded-port"
    CONF_FORWADED_PROTO_HEADER = "x-forwarded-proto"
    CONF_FORWADED_PATH_HEADER = "x-forwarded-path"
    # Test CONF_FORWADED_HEADER_VALUE
    CONF_FORWADED_HEADER_VALUE = "1.1.1.1"
    CONF_FORW

# Generated at 2022-06-14 07:17:28.734785
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    """
    Unit test for function parse_xforwarded.
    """
    assert parse_xforwarded(Headers({}), Config()) is None
    assert parse_xforwarded(Headers({"X-Forwarded-For": "10.0.0.1"}), Config()) is None
    assert parse_xforwarded(Headers({"X-Forwarded-For": "10.0.0.1"}), Config(PROXIES_COUNT=1)) == {"for": "10.0.0.1"}
    assert parse_xforwarded(Headers({"X-Forwarded-For": "10.0.0.1"}), Config(PROXIES_COUNT=0)) is None

# Generated at 2022-06-14 07:17:36.884854
# Unit test for function parse_forwarded
def test_parse_forwarded():
    headers = {
        "Forwarded": "for=192.0.2.60;host=example.com;proto=https"
    }
    config = {
        "FORWARDED_SECRET": "test"
    }
    options = parse_forwarded(headers, config)
    assert options["proto"] == "https"
    assert options["host"] == "example.com"
    assert options["for"] == "192.0.2.60"

# Generated at 2022-06-14 07:17:47.936061
# Unit test for function parse_forwarded
def test_parse_forwarded():
    from sanic.response import text
    from sanic.server import HttpProtocol
    import h11
    from h11 import Connection, Request

    class Server(HttpProtocol):
        def __init__(self):
            self.server_buffer = b""

        async def write_response(self, response):
            # pylint: disable=arguments-differ
            status_text = STATUS_CODES.get(response.status)
            status = f"HTTP/1.1 {response.status} {status_text}".encode(
                "utf-8"
            ) + b"\r\n"
            headers = []
            for k, v in response.headers.items():
                if k == "CONTENT-LENGTH":
                    v = str(len(response.body)).encode("utf-8")

# Generated at 2022-06-14 07:17:56.836510
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    header = {"x-forwarded-for": "1.1.1.1",
              "x-forwarded-proto": "https"}
    config = {"PROXIES_COUNT": 5,
              "REAL_IP_HEADER": "x-forwarded-for",
              "FORWARDED_FOR_HEADER": "x-forwarded-for"}
    assert parse_xforwarded(header, config) == {"for": "1.1.1.1", "proto": "https"}

# Generated at 2022-06-14 07:18:07.835145
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {
        "x-real-ip": "192.0.2.42",
        "x-forwarded-for": "192.0.2.43, 192.0.2.44"
    }
    assert parse_xforwarded(headers, 2) == {
        "for": "192.0.2.44"
    }
    headers = {
        "x-real-ip": "192.0.2.42",
        "x-forwarded-for": "192.0.2.43, _192.0.2.44"
    }
    assert parse_xforwarded(headers, 2) == {
        "for": "_192.0.2.44"
    }

# Generated at 2022-06-14 07:18:19.579152
# Unit test for function parse_forwarded
def test_parse_forwarded():
    from sanic.config import Config
    from sanic.server import HttpProtocol

    config = Config()
    config.FORWARDED_SECRET = "secret"
    protocol = HttpProtocol(config)

    headers = [
        "forwarded: by=_hidden; secret=secret; host=localhost; proto=http",
        "forwarded: by=_hidden; secret=secret; host=localhost; proto=http",
    ]
    parsed_headers = protocol.parse_forwarded(headers)

    assert parsed_headers == {'by': '_hidden', 'secret': 'secret', 'host': 'localhost', 'proto': 'http'}


# Generated at 2022-06-14 07:18:52.941007
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from sanic.config import Config
    from sanic.exceptions import SanicException
    from sanic.request import RequestParameters

    assert parse_xforwarded({}, Config()) == None

    config = Config()
    config.PROXIES_COUNT = 5
    config.REAL_IP_HEADER = "X-Real-Ip"
    config.FORWARDED_FOR_HEADER = "X-Forwarded-For"

    # Test when there is no information in X-Forwarded-For and
    # X-Real-Ip doesn't provide any information
    config.REAL_IP_HEADER = "X-Real-Ip"
    headers = {'X-Forwarded-For': "198.51.100.0, 203.0.113.195"}
    assert parse_xforwarded(headers, config) == None

# Generated at 2022-06-14 07:19:02.433364
# Unit test for function parse_forwarded
def test_parse_forwarded():
    headers = {'X-Forwarded-Host': 'www.example.com',
                'X-Forwarded-Port': '80',
                'X-Forwarded-Proto': 'http',
                'X-Forwarded-For': '8.8.8.8',
                'X-Forwarded-Path': 'example',
                'Forwarded': 'secret=1234; by=www.example.com',
                'X-Forwarded-Secret': '1234',
                'X-Scheme': 'http'
                }

# Generated at 2022-06-14 07:19:09.566510
# Unit test for function parse_xforwarded

# Generated at 2022-06-14 07:19:22.897783
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from datapunt_api.config import Config

    config = Config(PROXIES_COUNT=5)

    # no real_ip_header
    request = {'X-Forwarded-For': '33.44.55.66, 1.2.3.4'}
    result = parse_xforwarded(request, config)
    assert result['for'] == '1.2.3.4'

    # with real_ip_header
    config.REAL_IP_HEADER = 'X-Real-Ip'

    request = {'X-Forwarded-For': '33.44.55.66, 1.2.3.4', 'X-Real-Ip': '1.1.1.1'}
    #print(parse_xforwarded(request, config))

# Generated at 2022-06-14 07:19:33.840140
# Unit test for function parse_forwarded
def test_parse_forwarded():
    from .helpers import HttpProtocol

    class FakeConfig():
        FORWARDED_SECRET = "testme"

    headers = HttpProtocol({
        "Forwarded": "for=1.1.1.1, proto=https, by=2.2.2.2; secret=testme, for=4.4.4.4; for=3.3.3.3",
        "forwarded": "secret=testme, for= 4.4.4.4 ; by=3.3.3.3; other= a; other = b; other = x; other = y"
    })

    expected = {
        "for": "1.1.1.1",
        "proto": "https",
        "by": "2.2.2.2"
    }

# Generated at 2022-06-14 07:19:45.538400
# Unit test for function parse_forwarded
def test_parse_forwarded():
    # "by" check
    assert parse_forwarded({"forwarded": ["for=127.0.0.1; secret=foo; by=127.0.0.1"]}, config={
        "FORWARDED_SECRET": "foo"
    }) is not None
    assert parse_forwarded({"forwarded": ["for=127.0.0.1; secret=bar; by=127.0.0.1"]}, config={
        "FORWARDED_SECRET": "foo"
    }) is None

    # "secret" check
    assert parse_forwarded({"forwarded": ["for=127.0.0.1; secret=foo; by=127.0.0.1"]}, config={
        "FORWARDED_SECRET": "foo"
    }) is not None

# Generated at 2022-06-14 07:19:57.985013
# Unit test for function parse_forwarded
def test_parse_forwarded():
    d = parse_forwarded('by="[\\\\\\"\\"\\"192.168.0.1\\\\\\"\\"\\"]:123"; for="[\\\\\\"\\"\\"192.168.0.2\\\\\\"\\"\\"]:456";proto=https, by="[\\\\\\"\\"\\"192.168.0.3\\\\\\"\\"\\"]:789";for="[\\\\\\"\\"\\"192.168.0.4\\\\\\"\\"\\"]:101112"', '')
    print(d)

# Generated at 2022-06-14 07:20:07.961095
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {'x-forwarded-for': ['10.0.121.72, 10.0.0.1, 10.0.0.2'], 'x-forwarded-proto': ['https']}
    secret = 'secret'
    assert parse_forwarded(headers, secret) == None
    assert 'sanic.config.FORWARDED_FOR_HEADER' in 'FORWARDED_FOR_HEADER'
    assert 'sanic.config.REAL_IP_HEADER' in 'REAL_IP_HEADER'

if __name__ == '__main__':
    test_parse_xforwarded()

# Generated at 2022-06-14 07:20:17.809630
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from sanic import Sanic
    app = Sanic("test")

    @app.route("/")
    async def handler(request):
        app.logger.info(repr(parse_xforwarded(request.headers, app.config)))
        return text("OK")

    from sanic.testing import HOST, PORT
    from sanic.websocket import WebSocketConnection
    from sanic.websocket import ConnectionClosed

    import socket
    import tempfile
    import time

    with tempfile.TemporaryFile("w+") as logfile:
        app.config.set("LOGO", False)
        app.config.set("LOG_FILE", logfile)
        app.config.set("LOG_LEVEL", "INFO")

# Generated at 2022-06-14 07:20:20.800895
# Unit test for function parse_forwarded
def test_parse_forwarded():
    print(parse_forwarded(headers={"Forwarded":"secret=\"foo\";by=bar"}, config={}))
    assert False
