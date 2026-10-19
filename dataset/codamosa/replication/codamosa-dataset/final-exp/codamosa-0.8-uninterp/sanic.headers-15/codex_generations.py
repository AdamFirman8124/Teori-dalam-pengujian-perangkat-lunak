

# Generated at 2022-06-14 07:11:45.262362
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from collections import namedtuple
    from copy import deepcopy
    from sanic import Sanic
    from sanic.config import Config

    REAL_IP_HEADER_UNSET = namedtuple("REAL_IP_HEADER_UNSET", ["get"])()
    REAL_IP_HEADER_SET = namedtuple("REAL_IP_HEADER_SET", ["get"])(
        lambda *_, **__: "unittest.example.com"
    )
    FORWARDED_FOR_HEADER_UNSET = namedtuple("FORWARDED_FOR_HEADER_UNSET", ["getall"])()

# Generated at 2022-06-14 07:11:50.066573
# Unit test for function parse_content_header
def test_parse_content_header():
    value = 'form-data; name=upload; filename=\"file.txt\"';
    print ("Checking the data:", value)
    result = parse_content_header(value)
    print ("Please check the result: ", result)


# Generated at 2022-06-14 07:12:02.453898
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {
        'x-forwarded-by': '192.168.0.1', 
        'x-scheme': 'http', 
        'x-forwarded-path': '/path', 
        'x-forwarded-proto': 'https', 
        'x-forwarded-port': '8080', 
        'x-forwarded-host': 'example.com'
    }
    config = {}
    config["FORWARDED_FOR_HEADER"]='x-forwarded-by'
    config["REAL_IP_HEADER"]='x-forwarded-by'
    config["PROXIES_COUNT"]=1
    options = parse_xforwarded(headers, config)
    assert options['for'] == '192.168.0.1'

# Generated at 2022-06-14 07:12:12.361108
# Unit test for function parse_forwarded
def test_parse_forwarded():
    import base64
    from .request import RequestParameters
    config = RequestParameters(dict(
        FORWARDED_SECRET=base64.b64encode(b"secret").decode()
    ))
    print(
        parse_forwarded(
            {
                "Forwarded": "by=_hidden,for=_hidden,proto=https;host=example.com;port=8080"
            },
            config
        )
    )
    # split test
    print(
        parse_forwarded(
            {
                "Forwarded": "by=_hidden,for=_hidden",
                "Forwarded": "proto=https;host=example.com;port=8080"
            },
            config
        )
    )

# Generated at 2022-06-14 07:12:21.089335
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    assert parse_xforwarded({
        'x-forwarded-for': '127.0.0.1'
    }, object) == {
        'for': '127.0.0.1'
    }
    assert parse_xforwarded({
        'x-forwarded-host': 'a.io'
    }, object) == {
        'host': 'a.io'
    }
    assert parse_xforwarded({
        'x-forwarded-port': '80'
    }, object) == {
        'port': 80
    }
    assert parse_xforwarded({
        'x-forwarded-path': '/a/b'
    }, object) == {
        'path': 'a/b'
    }

# Generated at 2022-06-14 07:12:25.109824
# Unit test for function parse_forwarded
def test_parse_forwarded():
    assert parse_forwarded({"forwarded": "secret=test,value=abc,value2=xyz"}, {"FORWARDED_SECRET": "test"}) == {'value': 'abc', 'value2': 'xyz'}



# Generated at 2022-06-14 07:12:34.589157
# Unit test for function parse_forwarded
def test_parse_forwarded():
    # Set environment variable HTTP_FORWARDED=By="secret";Host="example.org"
    os.environ["HTTP_FORWARDED"] = 'By="secret";Host="example.org"'
    # Instantiate Request class and get access to headers variable
    request = Request.get('/')
    # Call function parse_forwarded
    # Parse Forwarded headers in request.headers for secret
    result = parse_forwarded(request.headers, request.config)
    # Assert value of key "by"
    assert result["by"] == "secret"



# Generated at 2022-06-14 07:12:47.172624
# Unit test for function parse_forwarded
def test_parse_forwarded():
    """Unit test for function parse_forwarded"""

    class mock_headers():
        def __init__(self, forwarded):
            self.header = forwarded

        def getall(self, header):
            return self.header

    class mock_config():
        def __init__(self, forwarded_secret):
            self.forwarded_secret = forwarded_secret
            self.FORWARDED_SECRET = self.forwarded_secret

    print("Test parse_forwarded when secret is not specified")
    forwarded_secret = ""
    forwarded = ("attacker=\"evil.com\","
                 "for=\"foo\";by=\"bar\";host=\"example.com\";secret="
                 "\"my_secret\";proto=https")
    config = mock_config(forwarded_secret)
    headers = mock_headers(forwarded)

   

# Generated at 2022-06-14 07:13:01.110540
# Unit test for function parse_forwarded
def test_parse_forwarded():
    from sanic.config import Config

    headers = {
        "Forwarded": "for=192.0.2.60;proto=http;host=www.example.com;param=v,"
        + "for=192.0.2.60;proto=http;host=www.example.com;param=w",
        "forwarded": "host=localhost:8080;secret=foo,"
        + "host=localhost:8080;secret=foo",
    }
    config = Config()
    config.FORWARDED_SECRET= "foo"
    config.PROXIES_COUNT = 0
    config.PROXY_FORWARDED_COUNT = float("inf")

# Generated at 2022-06-14 07:13:10.859094
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    """Test parse_xforwarded() function."""
    # noinspection PyTypeChecker
    ctx: Context = None  # So we can use Mypy
    ctx.config.PROXIES_COUNT = 2
    ctx.config.REAL_IP_HEADER = "x-forwarded-for"
    ctx.config.FORWARDED_FOR_HEADER = "x-forwarded-for"
    ctx.config.enable_forwarded_for_parser = True
    ctx.config.FORWARDED_SECRET = "mysecret"
    headers = CIMultiDict()
    headers.add("forwarded", "for=_hidden;proto=https;foo=bar;secret=mysecret")

# Generated at 2022-06-14 07:13:20.606989
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    print(parse_xforwarded({'x-forwarded-path': 'https://www.baidu.com/index'}, config))



# Generated at 2022-06-14 07:13:22.725501
# Unit test for function parse_forwarded
def test_parse_forwarded():
    headers = {}
    config = {}
    print(parse_forwarded(headers, config))



# Generated at 2022-06-14 07:13:26.651122
# Unit test for function fwd_normalize
def test_fwd_normalize():
    assert fwd_normalize([('proto', 'https'), ('host', 'm.sanic.vn')]) == {
        'proto': 'https',
        'host': 'm.sanic.vn'
    }

# Generated at 2022-06-14 07:13:39.129050
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    config = {
        'REAL_IP_HEADER': "X-Real-IP",
        'PROXIES_COUNT':0,
        'FORWARDED_FOR_HEADER': "X-Forwarded-For",
        'FORWARDED_FOR_COUNT': 0,
        'FORWARDED_SECRET': None
    }

# Generated at 2022-06-14 07:13:49.252052
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from sanic.config import Config

    config = Config()
    config.REAL_IP_HEADER = "X-Real-IP"
    config.PROXIES_COUNT = 3
    config.FORWARDED_FOR_HEADER = "X-Forwarded-For"

    class Headers():
        def __init__(self, headers):
            self.headers = headers

        def get(self, hdr):
            return self.headers.get(hdr)

        def getall(self, hdr):
            return self.headers.getall(hdr)


# Generated at 2022-06-14 07:14:03.526311
# Unit test for function fwd_normalize
def test_fwd_normalize():
    assert fwd_normalize(
        (("host", "Real-host"), ("port", "443"), ("path", "/%C3%B6l"))
    ) == {"host": "real-host", "port": 443, "path": "/öl"}
    assert fwd_normalize((("host", "Real-host"), ("port", "443"))) == {
        "host": "real-host",
        "port": 443,
    }
    assert fwd_normalize((("host", "Real-host"), ("port", "port"))) == {
        "host": "real-host",
    }
    assert fwd_normalize((("host", "Real-host"), ("unknown", "port"))) == {
        "host": "real-host",
    }

# Generated at 2022-06-14 07:14:15.871730
# Unit test for function fwd_normalize
def test_fwd_normalize():
    assert fwd_normalize([('secret', 'obfuscated'), ('by', 'obfuscated')]) == {'secret': 'obfuscated', 'by': 'obfuscated'}
    assert fwd_normalize([('secret', 'obfuscated'), ('for', 'obfuscated')]) == {'secret': 'obfuscated', 'for': 'obfuscated'}
    assert fwd_normalize([('for', 'obfuscated'), ('secret', 'obfuscated')]) == {'for': 'obfuscated', 'secret': 'obfuscated'}
    # Check that the order of the parameters doesn't matter
    assert fwd_normalize([('by', 'obfuscated'), ('secret', 'obfuscated')]) == {'by': 'obfuscated', 'secret': 'obfuscated'}
    assert fwd_normal

# Generated at 2022-06-14 07:14:28.236127
# Unit test for function fwd_normalize
def test_fwd_normalize():
    # client_ip = "12.34.56.78"
    # fwd_options = {"for": client_ip, "proto": "https", "host": "www.example.com", "port": 443, "path": "/", "by": "127.0.0.1"}
    with app.app.config(FORWARDED_SECRET="secret"):
        assert fwd_normalize_address("unknown") == "unknown"
        assert fwd_normalize_address("1.2.3.4") == "1.2.3.4"
        assert fwd_normalize_address("1.2.3.4\t") == "1.2.3.4"

# Generated at 2022-06-14 07:14:32.889241
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {
        'X-Forwarded-For': '18.211.0.233, 10.2.2.3'
    }
    print(parse_xforwarded(headers, 1))

test_parse_xforwarded()

# Generated at 2022-06-14 07:14:44.544588
# Unit test for function parse_forwarded
def test_parse_forwarded():
    import unittest

    headers = [
        ['By=r2d2;for=127.0.0.1,x-forwarded-for=192.0.2.2,for=127.0.0.1;by=r2d2'],
        ['By="r2d2";for=127.0.0.1,x-forwarded-for=192.0.2.2,for=127.0.0.1;by=r2d2'],
        ['for=127.0.0.1;by=r2d2'],
    ]


# Generated at 2022-06-14 07:15:02.369818
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {"X-Forwarded-For": "ip_1, ip_2, ip_3"}
    xforwarded = parse_xforwarded(headers, {})
    assert xforwarded is None
    xforwarded = parse_xforwarded(headers, {'PROXIES_COUNT': 1})
    assert xforwarded == {"path": None, "proto": None, "port": None, "for": "ip_3", "host": None}
    xforwarded = parse_xforwarded(headers, {'PROXIES_COUNT': 2})
    assert xforwarded == {"path": None, "proto": None, "port": None, "for": "ip_2, ip_3", "host": None}


# Generated at 2022-06-14 07:15:16.137903
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {
        'x-scheme': 'https', 
        'x-forwarded-host': 'user.example.com', 
        'x-forwarded-port': '3000', 
        'x-forwarded-path': '/saved_search/show/14'
    }
    class Config:
        REAL_IP_HEADER = 'x-forwarded-for'
        PROXIES_COUNT = 1
        FORWARDED_FOR_HEADER = 'x-forwarded-for'
    config = Config()
    options = parse_xforwarded(headers, config)
    assert options['host'] == 'user.example.com'
    assert options['proto'] == 'https'
    assert options['port'] == 3000
    assert options['path'] == '/saved_search/show/14'
    


# Generated at 2022-06-14 07:15:30.011969
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    old_proxies_count = config.PROXIES_COUNT
    old_real_ip_header = config.REAL_IP_HEADER
    old_forwarded_for_header = config.FORWARDED_FOR_HEADER

# Generated at 2022-06-14 07:15:38.487951
# Unit test for function parse_forwarded
def test_parse_forwarded():
    addr = "127.0.0.1"
    assert parse_forwarded({"forwarded": f"For={addr}"}) == {"for": addr}
    assert parse_forwarded({"forwarded": f'For="{addr}"'}) == {"for": addr}
    assert parse_forwarded({"forwarded": f"for={addr}"}) is None
    assert parse_forwarded(
        {"forwarded": f"for=127.0.0.1; for=\"127.0.0.1\"; for=127.0.0.2"}
    ) == {"for": "127.0.0.2"}
    assert parse_forwarded({"forwarded": f"for=127.0.0.1;by=;for=127.0.0.2"}) is None

# Generated at 2022-06-14 07:15:51.633249
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {'X-Real-Ip': '8.8.8.8', 'X-Scheme': 'http',
               'X-Forwarded-For': '1.1.1.1, 2.2.2.2, 3.3.3.3',
               'X-Forwarded-Port': '8000', 'X-Forwarded-Path': 'jupyter'}
    config = {'PROXIES_COUNT': 2, 'FORWARDED_FOR_HEADER': 'X-Forwarded-For',
              'REAL_IP_HEADER': 'X-Real-Ip'}

# Generated at 2022-06-14 07:16:06.057103
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    h = {
        'x-forwarded-for': '1.2.3.4',
        'x-forwarded-proto': 'https',
        'x-forwarded-host': 'localhost',
        'x-forwarded-port': '443',
        'x-forwarded-path': '/test'
    }
    r = parse_xforwarded(h, {
        "REAL_IP_HEADER": None,
        "FORWARDED_FOR_HEADER": 'x-forwarded-for',
        "PROXIES_COUNT": 2
    })
    assert r == {
        'for': '1.2.3.4',
        'proto': 'https',
        'host': 'localhost',
        'port': 443,
        'path': '/test'
    }


# Generated at 2022-06-14 07:16:18.192764
# Unit test for function parse_forwarded
def test_parse_forwarded():
    import logging
    import ipaddress
    headers = {'forwarded': 'for="_gazonk" , for=192.0.2.60 ;proto=http;by=203.0.113.43, for=2001:db8:cafe::17;by=unknown'}

    logging.info(headers)
    fwd = parse_forwarded(headers, config)

    # generate a list of all the ip's in the header
    ipv6 = fwd['for']
    ipv6 = ipv6[1:-1].lower()
    ipv6 = ipv6.split(',')
    for ip in ipv6:
        ip = ip.strip()
        logging.info(ip)

# Generated at 2022-06-14 07:16:24.705263
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from test_cases import xforwarded_headers, xforwarded_expected
    for i in range(len(xforwarded_headers)):
        assert (
            parse_xforwarded(xforwarded_headers[i], config)
            == xforwarded_expected[i]
        )

test_parse_xforwarded()

# Generated at 2022-06-14 07:16:36.791936
# Unit test for function parse_forwarded
def test_parse_forwarded():
    # Generated with:
    #   $ curl -vsSko/dev/null -H "Forwarded: for=10.1.2.3; by=_ME_; \
    #   proto=https; host=myhost; port=80; path=/the/path" https://test.server
    # Example with two secret and quotes
    forwarded_str = "for=10.1.2.3; by=_ME_; proto=https; host=myhost; \
        port=80; path=/the/path"

    result = parse_forwarded(forwarded_str, secret="_ME_")
    assert "for" in result
    assert result["for"] == "10.1.2.3"
    assert "by" in result
    assert result["by"] == "_ME_"
    assert "host" in result


# Generated at 2022-06-14 07:16:49.436515
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {
        "x-real-ip": "127.0.0.1",
        "x-forwarded-for": "127.0.0.1, 127.0.0.2",
        "x-scheme": "https",
        "x-forwarded-proto": "http",
        "x-forwarded-host": "example.com",
        "x-forwarded-port": "443",
        "x-forwarded-path": "%2Fusers%2F1",
    }
    config = {
        "REAL_IP_HEADER": "x-real-ip",
        "FORWARDED_FOR_HEADER": "x-forwarded-for",
        "FORWARDED_SECRET": "",
        "PROXIES_COUNT": 1,
    }

# Generated at 2022-06-14 07:17:07.690758
# Unit test for function parse_forwarded
def test_parse_forwarded():
    print(parse_forwarded({
        "forwarded": "for=192.0.2.60;proto=http;by=203.0.113.43"
    }, {"forwarded_secret": "secret"}))

# Generated at 2022-06-14 07:17:17.691634
# Unit test for function parse_forwarded
def test_parse_forwarded():
    assert parse_forwarded(['by=foo;for="192.0.2.1";proto=http;host=example.com', 'for="[2001:db8::1]"', 'for="192.0.2.2";host=foo.com;'], None) == {'for': '192.0.2.1', 'proto': 'http', 'host': 'example.com'}
    assert parse_forwarded(['by=foo;for="192.0.2.1";proto=http;host=example.com', 'for="[2001:db8::1]"', 'for="192.0.2.2";host=foo.com;'], 'foo') == {'for': '192.0.2.1', 'proto': 'http', 'host': 'example.com'}
    assert parse_

# Generated at 2022-06-14 07:17:30.230942
# Unit test for function parse_forwarded
def test_parse_forwarded():
    forwarded = parse_forwarded(["by=EXAMPLE;for=EXAMPLE;proto=http",
                                 "for=127.0.0.1;proto=https;by=EXAMPLE",
                                 "for=127.0.0.1;by=EXAMPLE"])
    assert forwarded is None

    forwarded = parse_forwarded(["for=127.0.0.1;by=EXAMPLE"], None)
    assert forwarded is not None

    forwarded = parse_forwarded(["by=EXAMPLE;for=EXAMPLE;proto=http",
                                 "for=127.0.0.1;proto=https;by=EXAMPLE",
                                 "for=127.0.0.1;by=EXAMPLE"], None)
    assert forwarded is None

    forwarded = parse_

# Generated at 2022-06-14 07:17:42.277024
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {
        'X-Forwarded-For': '127.0.0.1,192.168.0.1,192.168.0.2',
        'X-Forwarded-Proto': 'http',
        'X-Forwarded-Host': 'test.com',
        'X-Forwarded-Port': '1234',
        'X-Forwarded-Path': '/v1'
    }
    config = type('Config', (object,), {'PROXIES_COUNT': 2, 'FORWARDED_FOR_HEADER': 'X-Forwarded-For'})()
    result = parse_xforwarded(headers, config)
    print(result)



# Generated at 2022-06-14 07:17:45.914142
# Unit test for function parse_forwarded
def test_parse_forwarded():
    opts = parse_forwarded({'forwarded': ['for=127.0.0.1;by=127.0.0.1;']}, None)
    assert(opts == {'for': '127.0.0.1', 'by': '127.0.0.1'})

# Generated at 2022-06-14 07:17:54.133874
# Unit test for function parse_forwarded
def test_parse_forwarded():
    options = {}
    option = parse_forwarded(options)
    assert option is None

    options = {'forwarded': 'for=192.0.2.60;proto=http;by=203.0.113.43, for=127.0.0.1, for=localhost'}
    option = parse_forwarded(options)
    assert option is not None
    assert option['for'] == '127.0.0.1'
    assert option['proto'] == 'http'

# Generated at 2022-06-14 07:17:58.493305
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {
        "x-real-ip": "fake_ip",
        "x-forwarded-for": "fake_for",
    }
    config = {
        "FORWARDED_FOR_HEADER": "x-forwarded-for",
        "REAL_IP_HEADER": "x-real-ip",
        "PROXIES_COUNT": 1,
    }
    assert parse_xforwarded(headers, config) == {"for": "fake_for"}

# Generated at 2022-06-14 07:18:02.522572
# Unit test for function parse_forwarded
def test_parse_forwarded():
    test_forwarded = "80, for=192.0.2.60; proto=http; host=foo"
    test_dict = {'for': '192.0.2.60', 'proto': 'http', 'host': 'foo'}
    test = parse_forwarded(test_forwarded)
    assert test == test_dict

test_parse_forwarded()
test_parse_forwarded()

# Generated at 2022-06-14 07:18:10.410888
# Unit test for function parse_forwarded
def test_parse_forwarded():
    """
    Considered the forwarded headers:

    Forwarded: for=192.0.2.60; proto=http; by=203.0.113.43
    Forwarded: for=192.0.2.60; proto=http; by=203.0.113.43
    Forwarded: for=192.0.2.61; proto=http; by=203.0.113.43
    """
    from sanic.config import Config
    from sanic.request import Headers

    class HeaderConfig(Config):
        FORWARDED_SECRET = "secret"
        FORWARDED_FOR_HEADER = "x-forwarded-for"
        REAL_IP_HEADER = "x-real-ip"
        PROXIES_COUNT = 0

    # Headers Inputs

# Generated at 2022-06-14 07:18:20.828510
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    import json
    import urllib

    headers = {
        'X-Forwarded-By': 'proxy_forwarded_by', 'X-Forwarded-Proto': 'proxy_forwarded_proto',
        'X-Forwarded-Host': 'proxy_forwarded_host', 'X-Forwarded-Port': 'proxy_forwarded_port',
        'X-Forwarded-Path': 'proxy_forwarded_path', 'X-Forwarded-For': 'proxy_forwarded_for'
    }

    # test for option with PROXIES_COUNT and FORWARDED_FOR_HEADER
    config = {'PROXIES_COUNT': 2, 'FORWARDED_FOR_HEADER': 'X-Forwarded-For'}
    res = parse_xforwarded(headers, config)

# Generated at 2022-06-14 07:18:59.599207
# Unit test for function parse_forwarded
def test_parse_forwarded():

    headers = [
        "for=\"_gazonk\"; proto=https, for=129.78.138.66",
        "by=\"[2001:db8:cafe::17]\"; proto=http; host=example.com; fo=bar",
        "for=192.0.2.60; proto=http; by=203.0.113.43",
        "for=192.0.2.43, for=198.51.100.17",
    ]

    config = {
        "REAL_IP_HEADER": "",
        "FORWARDED_FOR_HEADER": "",
        "FORWARDED_SECRET": "secret",
        "PROXIES_COUNT": 0
    }


# Generated at 2022-06-14 07:19:08.622868
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    f = open("test_parse_xforwarded.txt", "r")
    f_lines = f.read().strip().split("\n")
    f.close()
    f_res = open("test_parse_xforwarded_res.txt", "w")

    from sanic import Sanic
    app = Sanic(__name__)

    for line in f_lines:
        line = line.split("||")
        headers = {
                    "X-Forwarded-For":line[0],
                    "X-Forwarded-Proto":line[1],
                    "X-Forwarded-Host":line[2],
                    "X-Forwarded-Port":line[3],
                    "X-Forwarded-Path":line[4]
                    }
        res = parse_xforwarded(headers, app.config)
       

# Generated at 2022-06-14 07:19:12.399981
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {
        'X-Scheme': 'https'
    }
    parsed = parse_xforwarded(headers, None)
    assert parsed == {'proto': 'https'}

# Generated at 2022-06-14 07:19:24.705324
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    import io
    import tempfile

    mock = io.StringIO("""
    {
        "headers": {
            "x-forwarded-for": "some ip",
            "x-scheme": "some protocol",
            "x-forwarded-port": "some port",
            "x-forwarded-path": "some path"
        }
    }
    """)

    with tempfile.NamedTemporaryFile("w+") as f:
        f.write(mock.read())
        f.seek(0)

        class FakeConfig:
            def __init__(self, config_path: str):
                self.PROXIES_COUNT = 5
                self.FORWARDED_FOR_HEADER = "X-Forwarded-For"

# Generated at 2022-06-14 07:19:33.946840
# Unit test for function parse_forwarded
def test_parse_forwarded():
    """
    Testing parse_forwarded function using real
    header and knowing result
    """
    header = 'For="[2001:db8:cafe::17]:4711"; ' + \
        'Proto="https"; ' + \
            'By=_secret; ' + \
                'Host="sanic.org:443" ' + \
                    'For=111.222.133.144'
    config = Config()
    config.FORWARDED_SECRET = "_secret"
    result = parse_forwarded(header, config)
    assert result == {"for": "111.222.133.144", "proto": "https",
                      "host": "sanic.org:443"}

# Generated at 2022-06-14 07:19:46.900692
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {
        'x-scheme': 'https',
        'x-forwarded-host': 'host',
        'x-forwarded-port': '8080',
        'x-forwarded-path': 'path',
        'x-forwarded-for': '66.249.66.1, 127.0.0.1'
    }
    config = {'PROXIES_COUNT': 1, 'FORWARDED_FOR_HEADER': 'x-forwarded-for'}
    expected = {
        'for': '66.249.66.1',
        'proto': 'https',
        'host': 'host',
        'port': 8080,
        'path': 'path',
    }
    assert expected == parse_xforwarded(headers, config)


# Generated at 2022-06-14 07:19:57.172088
# Unit test for function parse_forwarded
def test_parse_forwarded():
    headers = {
        'forwarded': ['for=192.0.2.60;proto=http;by=203.0.113.43', 'for=192.0.2.43,for=198.51.100.17;by=192.0.2.61']}
    config = {'FORWARDED_SECRET': 'foo', 'PROXIES_COUNT': 2}
    res = parse_forwarded(headers, config)
    assert res['for'] == '198.51.100.17'
    assert res['proto'] == 'http'
    assert res['by'] == '192.0.2.61'

# Generated at 2022-06-14 07:20:04.333861
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {
        'x-real-ip': '192.168.0.1',
        'x-forwarded-for': '127.0.0.1, 192.168.0.1',
        'x-forwarded-host': 'example.com',
        #'x-forwarded-path': '?',
        'x-scheme': 'tcp',
        'x-forwarded-proto': 'https',
        'x-forwarded-port': '443'
    }
    config = lambda: None
    config.REAL_IP_HEADER = 'x-real-ip'
    config.FORWARDED_FOR_HEADER = 'x-forwarded-for'
    config.PROXIES_COUNT = 1
    print(parse_xforwarded(headers, config))



# Generated at 2022-06-14 07:20:13.847791
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers={"X-FORWARDED-FOR": "192.168.1.1","X-Forwarded-For": "127.0.0.1",
             "x-FORWARDED-FOr": "192.168.1.2","X-FORWARDED-FOR": "192.168.1.3",
             "HOST":"example.com"}
    config = type('',(),{"PROXIES_COUNT": 4, "REAL_IP_HEADER":"", "FORWARDED_FOR_HEADER": "X-FORWARDED-FOR"})
    config.__dict__.update(config.__dict__)
    headers_list=[list(headers.items())]
    options = parse_xforwarded(headers_list, config)
    assert options["for"] == "192.168.1.3"


# Generated at 2022-06-14 07:20:25.434751
# Unit test for function parse_forwarded
def test_parse_forwarded():
    headers = Headers()

    fw = r'By=192.0.2.60; Forwarded=for="_gazonk"'; secret = 'test'
    options = parse_forwarded(headers, { 'FORWARDED_SECRET' : secret })
    assert options == None
    headers["forwarded"] = fw
    options = parse_forwarded(headers, { 'FORWARDED_SECRET' : secret })
    assert {'by': '_gazonk', 'for': '192.0.2.60'} == options

    headers["forwarded"] = r'By=192.0.2.60; Forwarded=for="_gazonk", for="[2001:db8:cafe::17]"; secret="test"'