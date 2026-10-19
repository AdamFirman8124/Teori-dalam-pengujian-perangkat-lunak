

# Generated at 2022-06-14 07:11:29.721746
# Unit test for function fwd_normalize
def test_fwd_normalize():
    assert fwd_normalize([]) == {}
    assert fwd_normalize([("by", "1.2.3.4")]) == {"by": "1.2.3.4"}
    assert fwd_normalize([("by", "1.2.3.4"), ("by", "5.6.7.8")]) == {
        "by": "5.6.7.8"
    }
    assert (
        fwd_normalize([("for", "1.2.3.4"), ("by", "5.6.7.8"), ("proto", "https")])
        == {"for": "1.2.3.4", "by": "5.6.7.8", "proto": "https"}
    )

# Generated at 2022-06-14 07:11:41.359164
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {
        "real_ip": "192.168.0.1",
        "x-forwarded-for": "192.168.0.1, 192.168.0.2",
        "x-scheme": "https",
        "x-forwarded-host": "hostname",
        "x-forwarded-port": "443",
        "x-forwarded-path": "/path",
    }
    config = {
        "REAL_IP_HEADER": "real_ip",
        "FORWARDED_FOR_HEADER": "x-forwarded-for",
        "PROXIES_COUNT": 2,
    }
    ret = parse_xforwarded(headers, config)

# Generated at 2022-06-14 07:11:53.302223
# Unit test for function fwd_normalize
def test_fwd_normalize():
    fwd_options = [('proto', 'http'), ('host', 'host.com'), ('port', '80'), ('path', 'some/path'), ('unknown', 'some_value')]
    print('fwd_options:')
    print(fwd_options)
    ret = fwd_normalize(fwd_options)
    print('fwd_normalize:')
    print(ret)
    assert(ret['proto'] == 'http')
    assert(ret['host'] == 'host.com')
    assert(ret['port'] == 80)
    assert(ret['path'] == 'some/path')
    assert('unknown' not in ret)


test_fwd_normalize()

# Generated at 2022-06-14 07:12:06.803091
# Unit test for function fwd_normalize
def test_fwd_normalize():
    options = fwd_normalize([
        ("for","1.2.3.4"),
        ("for", "127.0.0.1"),
        ("by","192.168.1.1"),
        ("secret","secret"),
        ("host","example.com"),
        ("host","www.example.com"),
        ("port","80"),
        ("port","443"),
        ("proto","http"),
        ("proto","HTTP"),
        ("path","example%20path"),
        ("path","example%20path%2Fpath2"),
        ("foo","bar"),
        ("foo","BAR"),
        ("foo","bar%2Fbaz")
    ])

    assert options["for"] == "1.2.3.4"
    assert options["by"] == "192.168.1.1"
    assert options

# Generated at 2022-06-14 07:12:13.926491
# Unit test for function parse_forwarded
def test_parse_forwarded():
    from sanic.testing import SanicTestClient, create_test_server
    app = create_test_server(app_func)
    client = SanicTestClient(app)
    res = client.get('/', headers=[
        ('Forwarded', 'for="[2001::1]:1234", by=2.3.4.5; protocol=https, host=example.com, path=/'),
        ('Forwarded', 'for=192.0.2.60, for=192.0.2.61; host="example.com:8000", for=192.0.2.62')
        ])
    for k, v in res.headers.items():
        print('{}: {}'.format(k, v))
    print(res.text)
    assert res.status == 200


# Generated at 2022-06-14 07:12:24.018734
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {
        'x-forwarded-host': 'host:port',
        'x-forwarded-proto': 'https',
        'x-forwarded-path': '/path',
        'x-forwarded-port': 'port',
        'x-scheme': 'http'
    }
    ret = parse_xforwarded(headers, None)
    assert ret['for'] == 'host:port'
    assert ret['proto'] == 'https'
    assert ret['path'] == '/path'
    assert ret['port'] == 'port'

if __name__ == "__main__":
    test_parse_xforwarded()

# Generated at 2022-06-14 07:12:30.696391
# Unit test for function fwd_normalize
def test_fwd_normalize():
    options = [
        ("for", "::ffff:127.0.0.1"),
        ("proto", "http"),
        ("host", "example.com"),
        ("port", "80"),
        ("path", "/path/to/resource"),
    ]
    assert fwd_normalize(options) == {
        "for": "::ffff:127.0.0.1",
        "proto": "http",
        "host": "example.com",
        "port": 80,
        "path": "/path/to/resource",
    }

# Generated at 2022-06-14 07:12:38.438093
# Unit test for function fwd_normalize_address
def test_fwd_normalize_address():
    input_data = [
        ("::1", "::1"),
        ("_2adcdc68d5a9", "_2adcdc68d5a9"),
        ("_2adcdc68d5a9.ipv6.xyz", "_2adcdc68d5a9.ipv6.xyz"),
    ]
    for addr, expected in input_data:
        assert fwd_normalize_address(addr) == expected

# Generated at 2022-06-14 07:12:48.771823
# Unit test for function parse_forwarded
def test_parse_forwarded():
    import time
    from sanic.config import Config
    from sanic.request import Request


# Generated at 2022-06-14 07:13:02.507991
# Unit test for function parse_forwarded

# Generated at 2022-06-14 07:13:21.510259
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from sanic import Sanic

    app = Sanic("Test")
    app.config.PROPAGATE_EXCEPTIONS = False
    app.config.FORWARDED_FOR_HEADER = "X-Forwarded-For"
    app.config.FORWARDED_HOST_HEADER = "x-forwarded-host"

    @app.route("/")
    async def handler(request):
        return fwd_normalize(request.forwarded_options.items())

    request, response = app.test_client.get(
        "/",
        headers={
            "X-Forwarded-For": "140.90.15.20, 10.0.0.10"
        },
    )

    # print(response.json)
    assert response.json == {'for': '140.90.15.20'}

# Generated at 2022-06-14 07:13:27.430615
# Unit test for function parse_forwarded
def test_parse_forwarded():
    headers = {'forwarded': ['for="_gazonk"', 'For="[2001:db8:cafe::17]:4711"', 'for=192.0.2.60;proto=httpppp;by=203.0.113.43']}
    config = {'FORWARDED_SECRET': '_urlisnotsecret_'}
    print(parse_forwarded(headers, config))

# Generated at 2022-06-14 07:13:35.307621
# Unit test for function parse_forwarded
def test_parse_forwarded():
    headers = {'Forwarded': ['for=192.0.2.60; proto=http; by=203.0.113.43, for=192.0.2.61; proto=https']}

    secret = '123456'
    config = {"FORWARDED_SECRET": secret}
    result = parse_forwarded(headers, config)
    assert result == {'for': '192.0.2.60', 'proto': 'http', 'by': secret}

    secret = '123456'
    config = {"FORWARDED_SECRET": secret}
    result = parse_forwarded(headers, config)
    assert result == {'for': '192.0.2.60', 'proto': 'http', 'by': secret}

    secret = '123456'

# Generated at 2022-06-14 07:13:48.809487
# Unit test for function parse_forwarded
def test_parse_forwarded():
    headers = {'forwarded': 'For=203.0.113.195; Proto=https, for="[2001:DB8::C001]:80" ;Secret="v4^$4f4"; Host=www.example.com, for=192.0.2.43, for=198.51.100.17; proto=https; by=203.0.113.43, for=192.0.2.43; proto=https'}
    config = Options
    config['FORWARDED_SECRET'] = "v4^$4f4"
    config['PROXIES_COUNT'] = 5
    config['FORWARDED_FOR_HEADER'] = ""
    config['REAL_IP_HEADER'] = ""

# Generated at 2022-06-14 07:14:03.059846
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {}
    config = type('X', (object,), {})()

    config.FORWARDED_FOR_HEADER = 'x-forwarded-for'
    config.REAL_IP_HEADER = 'x-real-ip'
    config.PROXIES_COUNT = 2
    config.FORWARDED_SECRET = 'my-secret'

    headers['x-forwarded-for'] = '19.42.42.42'
    x = parse_xforwarded(headers, config)
    assert x['for'] == '19.42.42.42'

    headers['x-forwarded-for'] = '43.43.43.43, 19.42.42.42, 21.42.42.42'
    x = parse_xforwarded(headers, config)

# Generated at 2022-06-14 07:14:15.495547
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    import pytest
    from sanic.config import Config
    from sanic.response import HTTPResponse
    from sanic.request import Request
    from sanic.server import Server
    from sanic.websocket import WebSocketProtocol

    server = Server(
        request_class=Request,
        response_class=HTTPResponse,
        websocket_class=WebSocketProtocol,
    )
    config = Config()
    config.REAL_IP_HEADER = "request-id"
    config.FORWARDED_FOR_HEADER = "forwarded-for"
    config.PROXIES_COUNT = 2


# Generated at 2022-06-14 07:14:27.986359
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from sanic.config import Config
    config = Config()
    config.REAL_IP_HEADER = "X-Real-IP"
    config.PROXIES_COUNT = 3
    config.FORWARDED_FOR_HEADER = "X-Forwarded-For"

    headers = {"X-Forwarded-For": "10.10.100.100, 192.168.100.100"}
    options = parse_xforwarded(headers, config)
    assert options == {"for": "192.168.100.100"}

    headers = {"X-Forwarded-For": "10.10.100.100, 192.168.100.100, 10.200.200.200"}
    options = parse_xforwarded(headers, config)
    assert options == {"for": "10.200.200.200"}


# Generated at 2022-06-14 07:14:41.192593
# Unit test for function parse_forwarded
def test_parse_forwarded():
    test_headers = {'Forwarded': ['for="_mdnx27._tcp.local"', 'by="::1"; proto=http',
                                  'for=192.0.2.60;proto=http;by=203.0.113.43']}
    config = type("Config", (object,), dict(for_host="localhost",
                                            for_port=80,
                                            forwarded_secret="test"))
    assert parse_forwarded(test_headers, config) == {
        "for": '192.0.2.60', "proto": "http", "by": "203.0.113.43"}

# Generated at 2022-06-14 07:14:52.196707
# Unit test for function fwd_normalize_address
def test_fwd_normalize_address():
    assert fwd_normalize_address("127.0.0.1") == "127.0.0.1"
    assert fwd_normalize_address("[::1]") == "[::1]"
    assert fwd_normalize_address("_abc") == "_abc"
    assert fwd_normalize_address("_") == "_"
    assert fwd_normalize_address("ABC") == "abc"
    assert fwd_normalize_address("ABCD") == "abcd"
    assert fwd_normalize_address("_ABC") == "_ABC"
    assert fwd_normalize_address("") == ""
    assert fwd_normalize_address("unknown") == ""

# Generated at 2022-06-14 07:15:00.093917
# Unit test for function parse_forwarded
def test_parse_forwarded():
    assert parse_forwarded({'forwarded': 'for=192.0.2.60;proto=http;by=203.0.113.43'}, None) == {'by': '203.0.113.43', 'for': '192.0.2.60', 'proto': 'http'}
    assert parse_forwarded({'forwarded': 'for=192.0.2.43, for=198.51.100.17'}, None) == {'for': '198.51.100.17'}

# Generated at 2022-06-14 07:15:11.783788
# Unit test for function parse_forwarded
def test_parse_forwarded():
    forwarded_value = 'by=_hidden, for=192.0.2.60, for=192.0.2.43, for="[2001:db8:cafe::17]:4711", for=_hidden, for=unknown, host=example.com, proto=https'
    forwarded_secret = '_hidden'
    output = parse_forwarded(forwarded_value, forwarded_secret)
    print(f"output is: {output}")

# Generated at 2022-06-14 07:15:20.837618
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    import os
    import re
    import csv
    import tempfile
    import pytest
    import aiosanic
    from sanic.config import Config

    # more examples
    # https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-request-tracing.html#record-example-header

    REGEX = re.compile(r'([a-zA-Z\-]+): ([^;,]+)(;|,|$)')    

    X_FORWARDED_FOR = os.environ["X-Forwarded-For"]
    X_FORWARDED_PROTO = os.environ["X-Forwarded-Proto"]
    X_FORWARDED_HOST = os.environ["X-Forwarded-Host"]
    X_FORWARDED_PORT = os

# Generated at 2022-06-14 07:15:34.209139
# Unit test for function parse_forwarded
def test_parse_forwarded():
    config = None
    headers = None
    assert (parse_forwarded(headers,config) == None)
    config = type('', (), {})()
    config.FORWARDED_SECRET = None
    headers = {'Forwarded': 'For=127.0.0.1; By=test_secret'}
    assert (parse_forwarded(headers,config) == None)
    config.FORWARDED_SECRET = 'test_secret'
    assert (parse_forwarded(headers,config) == {'for': '127.0.0.1', 'by': 'test_secret'})
    headers = {'Forwarded': 'For=127.0.0.1, For=127.0.0.2; By=test_secret'}

# Generated at 2022-06-14 07:15:46.681442
# Unit test for function parse_forwarded
def test_parse_forwarded():
    # Construct a sample forwarded header
    class Headers:
        def __init__(self):
            self.header = {
                "Forwarded": "for=192.168.1.1; proto=http; by=_secret"
            }

        def getall(self, k):
            return self.header.get(k, "")

    class Config:
        FORWARDED_SECRET = "_secret"

    headers = Headers()
    config = Config()
    assert parse_forwarded(headers, config) == {
        "for": "192.168.1.1",
        "proto": "http",
        "by": "_secret",
    }



# Generated at 2022-06-14 07:15:58.022666
# Unit test for function parse_forwarded
def test_parse_forwarded():
    headers = [
    "secret={{ secret }}",
    "for=192.0.2.60;proto=http;by=203.0.113.43",
    "for=_hidden,for=example.com;by=203.0.113.43",
    "for=192.0.2.60;proto=http,by=203.0.113.43",
    "for=192.0.2.60;proto=http,by=203.0.113.43;by=203.0.113.44",
    "for=192.0.2.60; proto=http;by=203.0.113.43; secret=\"if you can see this, it is wrong\"",
    ]
    for h in headers:
        result = parse_forwarded(h, "{{ secret }}")
       

# Generated at 2022-06-14 07:16:03.610554
# Unit test for function fwd_normalize_address
def test_fwd_normalize_address():
    assert fwd_normalize_address("unknown") == ""
    assert fwd_normalize_address("localhost") == "localhost"
    assert fwd_normalize_address("_ip_address") == "_ip_address"
    assert fwd_normalize_address("127.0.0.1") == "127.0.0.1"
    assert fwd_normalize_address("0:0:0:0:0:ffff:7f00:1") == "[::ffff:7f00:1]"
    assert fwd_normalize_address("0:0:0:0:0:ffff:127.0.0.1") == "[::ffff:7f00:1]"

# Generated at 2022-06-14 07:16:08.341509
# Unit test for function parse_content_header
def test_parse_content_header():
    assert parse_content_header('form-data; name=upload; filename="file.txt"') == ('form-data', {'name': 'upload', 'filename': 'file.txt'})


# Generated at 2022-06-14 07:16:21.651692
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = dict()
    headers['X-Forwarded-For'] = '10.0.0.1, 10.0.0.2'
    headers['X-Forwarded-Host'] = 'host1.example.com'
    headers['X-Forwarded-Port'] = '8080'
    headers['X-Forwarded-Proto'] = 'http'
    headers['X-Forwarded-Path'] = '/foo/bar'
    headers['X-Scheme'] = 'http'
    headers['X-Real-Ip'] = '10.0.0.42'
    config={}
    config.REAL_IP_HEADER = 'X-Real-Ip'
    config.PROXIES_COUNT = 1
    config.FORWARDED_FOR_HEADER = 'X-Forwarded-For'

# Generated at 2022-06-14 07:16:29.607341
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from sanic.config import Config
    from sanic.request import AsyncRequest

    config = Config()
    headers = AsyncRequest({}, config)

    # Test 1: Forwarded header, no real ip header, don't care about proxies
    headers.headers = {"forwarded": "for=100.100.100.100"}
    assert parse_xforwarded(headers, config) == {"for": "100.100.100.100"}

    # Test 2: Forwarded header, no real ip header, care about proxies
    config.PROXIES_COUNT = 2
    headers.headers = {
        "forwarded": "for=100.100.100.100,for=101.101.101.101,for=102.102.102.102"
    }

# Generated at 2022-06-14 07:16:35.640721
# Unit test for function parse_forwarded
def test_parse_forwarded():
    print("Unit Test: parse_forwarded")
    class Config:
        def __init__(self, FORWARDED_SECRET=None, PROXIES_COUNT=0):
            self.FORWARDED_SECRET = FORWARDED_SECRET
            self.PROXIES_COUNT = PROXIES_COUNT
        @property
        def REAL_IP_HEADER(self):
            return None
        @property
        def FORWARDED_FOR_HEADER(self):
            return None

    cfg = Config(FORWARDED_SECRET=None)
    assert parse_forwarded({}, cfg) is None
    assert parse_forwarded({"Forwarded": "For=192.168.1.1"}, cfg) is None

# Generated at 2022-06-14 07:16:49.985998
# Unit test for function parse_forwarded
def test_parse_forwarded():
    config = FakeConfig()
    config.FORWARDED_SECRET = "IPv6.11"
    result = parse_forwarded({'Forwarded': ['token=2.2.1, '
                                            'by=IPv6.11, '
                                            'for="[::1]"; '
                                            'host="test.com"; '
                                            'proto="https"; '
                                            'port=8080']}, config)
    assert result == {'proto': 'https', 'for': '::1', 'port': 8080, 'host': 'test.com'}
    result = parse_forwarded({'Forwarded': ['by=IPv6.11', 'by="[::1]"']}, config)
    assert result == {'by': '::1'}
    result = parse_forward

# Generated at 2022-06-14 07:16:57.429905
# Unit test for function fwd_normalize
def test_fwd_normalize():
    assert fwd_normalize(fwd_normalize(parse_forwarded({"forwarded":""}, None)))
    assert fwd_normalize(fwd_normalize(parse_xforwarded({"x-real-ip":""}, None)))
    assert fwd_normalize(fwd_normalize(parse_xforwarded({"x-forwarded-for":""}, None)))

# Generated at 2022-06-14 07:17:08.356864
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from sanic.config import Config
    from collections import OrderedDict
    config = Config()
    config.PROXIES_COUNT = 1

    # Test x-forwarded-for used alone
    headers = OrderedDict([("x-forwarded-for", "127.0.0.1")])
    obj = parse_xforwarded(headers, config)
    assert obj == {"for": "127.0.0.1"}

    # Test x-forwarded-for used in combination with x-scheme
    headers = OrderedDict([("x-forwarded-for", "127.0.0.1"),
                           ("x-scheme", "https")])
    obj = parse_xforwarded(headers, config)

# Generated at 2022-06-14 07:17:12.685235
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {'x-scheme': 'https', 'x-forwarded-host': '127.0.0.1:8000'}
    assert parse_xforwarded(headers, "127.0.0.1") == {'host': '127.0.0.1:8000', 'proto': 'https'}

# Generated at 2022-06-14 07:17:25.609686
# Unit test for function fwd_normalize_address
def test_fwd_normalize_address():
    # uppercase
    assert fwd_normalize_address("1.2.3.4") == "1.2.3.4"
    assert fwd_normalize_address("1:2::3") == "1:2::3"
    assert fwd_normalize_address("[1:2::3]") == "[1:2::3]"
    # lowercase
    assert fwd_normalize_address("11.22.33.44") == "11.22.33.44"
    assert fwd_normalize_address("AA:BB::CC") == "aa:bb::cc"
    assert fwd_normalize_address("[AA:BB::CC]") == "[aa:bb::cc]"
    # IPv4 mapped IPv6

# Generated at 2022-06-14 07:17:38.881402
# Unit test for function parse_forwarded
def test_parse_forwarded():
    headers = []
    headers.append(("FORWARDED", "for=10.1.2.3;host=HOST"))
    headers.append(("FORWARDED", "for=10.1.2.4;by=BY"))
    headers.append(("FORWARDED", "for=10.1.2.5;proto=https;by=BY2"))
    headers.append(("FORWARDED", "for=10.1.2.6;host=HOST2;port=8080"))
    headers.append(("FORWARDED", "for=10.1.2.7;path=/path"))
    headers.append(("FORWARDED", "for=10.1.2.8;QUOTED=\"quoted\""))

# Generated at 2022-06-14 07:17:47.554747
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    import pytest
    from sanic.response import HTTPResponse

    # Example Forwarded header with a single entry, no port
    forwarded = "for=192.0.2.43, for=198.51.100.17; proto=https"
    response = HTTPResponse(headers={"Forwarded": forwarded})
    forward_real_ip = response.headers.get("X-Forwarded-For")
    forward_proto = response.headers.get("X-Forwarded-Proto")
    assert forward_real_ip == "192.0.2.43, 198.51.100.17"
    assert forward_proto == "https"

    # Example Forwarded header with multiple entries, with port

# Generated at 2022-06-14 07:17:54.050313
# Unit test for function fwd_normalize_address
def test_fwd_normalize_address():
    assert fwd_normalize_address("a[bc:de:f]g:1:2:3:4:5:6:7") == "[a[bc:de:f]g:1:2:3:4:5:6:7]"
    assert fwd_normalize_address("0:0:0:0:0:0:0:0::1") == "[::1]"
    assert fwd_normalize_address("_x1:2:3:4:5:6:7:8") == "_x1:2:3:4:5:6:7:8"
    assert fwd_normalize_address("_x0:0:0:0:0:0:0:0::1") == "_x0:0:0:0:0:0:0:0::1"

# Generated at 2022-06-14 07:17:59.064341
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {'X-Forwarded-Path': '%2Fapi%2Fv1%2Faccount%2Finfo', 'X-Forwarded-Proto': 'https', 'X-Forwarded-Host': '192.168.1.1:8080', 'X-Forwarded-For': '10.20.30.40', 'X-Scheme': 'http'}
    ret = parse_xforwarded(headers)
    print(ret)


if __name__ == '__main__':
    test_parse_xforwarded()

# Generated at 2022-06-14 07:18:09.043038
# Unit test for function parse_forwarded
def test_parse_forwarded():
    headers = {'forwarded': ['for=192.0.2.60;proto=http;host=example.com;port=8080;secret=secret1', 'proto=https,host=www.example.com;by=_secret2,for=192.0.2.62;secret=secret2', 'x-dns-prefetch-control: off', 'X-Forwarded-Port: 443', 'for=192.0.2.63;secret=secret3']}
    config = {'FORWARDED_SECRET': 'secret2'}
    print(parse_forwarded(headers, config))

# Generated at 2022-06-14 07:18:29.332469
# Unit test for function parse_forwarded
def test_parse_forwarded():
    headers = {'Forwarded':'for=192.0.2.43, for="[2001:db8:cafe::17]";proto=https;by=203.0.113.60;host="example.org";port="4321", for=203.0.113.60, for=unknown, for="[0:0:0:0:0:ffff:c0a8:0101]"', 'real-ip-header':'x-real-ip', 'FORWARDED_FOR_HEADER': 'X-Forwarded-For', 'x-forwarded-host': 'example.org', 'proxies-count':3, 'x-scheme': 'https', 'x-forwarded-port': '4321', 'x-forwarded-path': '/foo/(bar)', 'x-forwarded-proto': 'https'}

# Generated at 2022-06-14 07:18:36.260295
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    import logging
    import ujson
    from sanic.config import Config
    from sanic.request import Headers
    
    logging.basicConfig(level=logging.DEBUG)

    config = Config()
    config.REAL_IP_HEADER = 'X-Real-IP'
    config.PROXIES_COUNT = 1

    headers = Headers()
    headers.set('X-Real-IP', '60.155.123.249')
    headers.set('X-Forwarded-For', '171.221.223.178')

    result = parse_xforwarded(headers, config)

    print(ujson.dumps(result, indent=4))

# Generated at 2022-06-14 07:18:40.088970
# Unit test for function parse_forwarded
def test_parse_forwarded():
    type = 'application/json'
    options = {}
    headers = HeaderIterable([('Content-Type', type)])
    for h in headers:
        print(h)

# Generated at 2022-06-14 07:18:52.013171
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    request = {}
    request['headers'] = {}
    request['headers']['X-Forwarded-For'] = '192.168.3.3'
    request['headers']['X-Scheme'] = 'https'
    request['headers']['X-Forwarded-Host'] = 'x.x.x.x'
    request['headers']['X-Forwarded-Port'] = '80'
    request['headers']['X-Forwarded-Path'] = '/api/'

    req = parse_xforwarded(request['headers'], "")
    assert req['for'] == '192.168.3.3'
    assert req['proto'] == 'https'
    assert req['host'] == 'x.x.x.x'
    assert req['port'] == 80

# Generated at 2022-06-14 07:19:02.074073
# Unit test for function parse_forwarded
def test_parse_forwarded():
    # assert parse_forwarded(None, None) is None
    # assert parse_forwarded({}, None) is None
    # assert parse_forwarded({'fwd': 'for=1.2.3.4;proto=https'}, None) is None
    assert parse_forwarded({'fwd': 'for=1.2.3.4;proto=https;by=2.3.4.5'}, '2.3.4.5') == {'for': '1.2.3.4', 'proto': 'https'}
    assert parse_forwarded({'fwd': 'for=1.2.3.4;proto=https'}, None) == {'for': '1.2.3.4', 'proto': 'https'}

# Generated at 2022-06-14 07:19:09.359166
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from http import HTTPStatus
    from sanic.config import Config
    from sanic.request import Request
    from sanic.response import text

    config = Config()
    config.REAL_IP_HEADER = "X-Real-IP"
    config.FORWARDED_FOR_HEADER = "X-Forwarded-For"
    config.FORWARDED_PROTO_HEADER = "X-Forwarded-Proto"
    config.FORWARDED_PORT_HEADER = "X-Forwarded-Port"
    config.FORWARDED_HOST_HEADER = "X-Forwarded-Host"
    config.FORWARDED_PATH_HEADER = "X-Forwarded-Path"

    app = Sanic("test_parse_xforwarded")


# Generated at 2022-06-14 07:19:22.752640
# Unit test for function parse_host
def test_parse_host():
    assert parse_host('localhost:5000') == ('localhost', 5000)
    assert parse_host('localhost') == ('localhost', None)
    assert parse_host('localhost5') == ('localhost5', None)
    assert parse_host('localhost.com') == ('localhost.com', None)
    assert parse_host('::1') == ('[::1]', None)
    assert parse_host('[::1]') == ('[::1]', None)
    assert parse_host('[2002:4559:1fe2::4559:1fe2]:80') == ('[2002:4559:1fe2::4559:1fe2]', 80)

# Generated at 2022-06-14 07:19:33.693771
# Unit test for function parse_forwarded
def test_parse_forwarded():
    forward_header_string = 'By=_mdn_; For=_mdn_:192.168.1.1, host=example.com; Proto=https; Host=example.com; Path=/index'
    reverse_header_string = forward_header_string[::-1]

    m = _rparam.finditer(reverse_header_string)
    pos = None
    options: List[Tuple[str, str]] = []
    found = False
    for ma in m:
        print(ma.groups())
        # Start of new element? (on parser skips and non-semicolon right sep)
        if ma.start() != pos or sep != ";":
            # Was the previous element (from right) what we wanted?
            if found:
                break
            # Clear values and parse as new element
            del options

# Generated at 2022-06-14 07:19:40.085011
# Unit test for function parse_host
def test_parse_host():
    assert parse_host("localhost") == ("localhost", None)
    assert parse_host("localhost:80") == ("localhost", 80)
    assert parse_host("[::1]") == ("::1", None)
    assert parse_host("[::1]:443") == ("::1", 443)
    assert parse_host("::1") == ("::1", None)
    assert parse_host("::1:80") == ("::1", 80)
    assert any(parse_host(h) != (None, None) for h in ("", ":", ":80", ":443"))
    assert all(parse_host("_%s" % h) == (h, None) for h in ("localhost", "127.0.0.1", "::1"))

# Generated at 2022-06-14 07:19:49.284415
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {
        'X-Forwarded-Proto': 'https',
        'X-Forwarded-Host': 'sanic.com',
        'X-Forwarded-Port': '80',
        'X-Forwarded-Path': '',
    }
    config = {
        'REAL_IP_HEADER': None,
        'FORWARDED_FOR_HEADER': None,
        'PROXIES_COUNT': 0
    }
    result = parse_xforwarded(headers, config)
    assert result == {
        'proto': 'https',
        'host': 'sanic.com',
        'port': 80,
        'path': ''
    }



# Generated at 2022-06-14 07:20:09.753120
# Unit test for function parse_forwarded
def test_parse_forwarded():
    from sanic.exceptions import InvalidUsage

    from sanic.request import RequestParameters, Request

    config = {
        "FORWARDED_SECRET": "abc"
    }


# Generated at 2022-06-14 07:20:18.963892
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from sanic import Sanic
    from sanic.request import Request
    app = Sanic(__name__)

    @app.route('/')
    async def test(request):
        x_forwarded_for = request.headers.get('X-Forwarded-For')
        return text(x_forwarded_for)

    request = Request('GET', '/', headers={"X-Forwarded-For": "test"}, version=1)
    app.config.PROXIES_COUNT = 1
    app.config.FORWARDED_FOR_HEADER = "x-forwarded-for"
    assert request.ip == 'test'

# Generated at 2022-06-14 07:20:29.886692
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    assert parse_xforwarded({"X-Forwarded-Proto": "https", "X-Forwarded-For": "127.0.0.1:8000"}, {}) == {
        "proto": "https",
        "for": "127.0.0.1:8000",
    }
    
    assert parse_xforwarded({"X-Forwarded-Proto": "http", "X-Forwarded-For": "127.0.0.1"}, {}) == {
        "proto": "http",
        "for": "127.0.0.1",
    }

    assert parse_xforwarded({"X-Forwarded-Proto": "https", "X-Forwarded-For": "127.0.0.1:8000"}, {"REAL_IP_HEADER": "X-Forwarded-For"})

# Generated at 2022-06-14 07:20:39.851447
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {"X-Forwarded-For": "test_host", "X-Forwarded-Port": "3030", "X-Forwarded-Proto": "http"}
    config = {}
    config['PROXIES_COUNT'] = 1
    config['FORWARDED_FOR_HEADER'] = 'X-Forwarded-For'

    fwd = parse_xforwarded(headers, config)

    assert(fwd['for'] == 'test_host')
    assert(fwd['proto'] == 'http')
    assert(fwd['port'] == 3030)



# Generated at 2022-06-14 07:20:48.211316
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {'x-forwarded-for': '123.123.123.123, 234.234.234.234', 'x-forwarded-proto': 'http'}
    config = {'PROXIES_COUNT': 2, 'FORWARDED_FOR_HEADER': 'x-forwarded-for', 'REAL_IP_HEADER': 'x-forwarded-for', 'FORWARDED_PROTO_HEADER': 'x-forwarded-proto'}
    assert parse_xforwarded(headers, config) == {'for': '234.234.234.234', 'proto': 'http'}

# Generated at 2022-06-14 07:21:00.547117
# Unit test for function parse_forwarded
def test_parse_forwarded():
    from .config import Config
    from .multidict import CIMultiDict

    config = Config()
    config.FORWARDED_SECRET = "example.org"
    headers = CIMultiDict()


# Generated at 2022-06-14 07:21:14.374243
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from sanic.request import Request
    from sanic_motor import BaseModel
    from sanic import Sanic
    from sanic.response import text

    app = Sanic(__name__)
    BaseModel.init_app(app)

    class User(BaseModel):
        __coll__ = "user"
        id = StringField(primary_key=True)
        name = StringField()

    async def test(request):
        ip = request.ip
        d = User(dict(id=request.headers["X-Forwarded-For"], name="user")).save()
        return text("Hello! " + ip)

    app.add_route(test, "/test")

    request, response = app.test_client.post(
        "/test", headers={"X-Forwarded-For": "localhost"}
    )
   