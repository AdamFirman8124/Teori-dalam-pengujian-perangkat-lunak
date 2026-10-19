

# Generated at 2022-06-13 07:07:04.493024
# Unit test for function parse_address
def test_parse_address():
    import pytest

    # IPv4 addresses
    assert parse_address('192.0.2.3') == ('192.0.2.3', None)
    assert parse_address('192.0.2.3:55') == ('192.0.2.3', 55)

    # IPv4 address ranges
    assert parse_address('192.0.2.0[0:4]') == ('192.0.2.0[0:4]', None)
    assert parse_address('192.0.2.0[0:4]:55') == ('192.0.2.0[0:4]', 55)

    # IPv6 addresses
    assert parse_address('::1') == ('::1', None)
    assert parse_address('::1%2') == ('::1%2', None)

# Generated at 2022-06-13 07:07:15.846375
# Unit test for function parse_address
def test_parse_address():
    assert parse_address("192.0.2.1:22") == ("192.0.2.1", 22)
    assert parse_address("192.0.2.1:65535") == ("192.0.2.1", 65535)
    assert parse_address("192.0.2.1", True) == ("192.0.2.1", None)
    assert parse_address("host.example.org:65535") == ("host.example.org", 65535)
    assert parse_address("host.example.org", True) == ("host.example.org", None)
    assert parse_address("[2001:db8::1]:22") == ("2001:db8::1", 22)
    assert parse_address("[2001:db8::1]:65535") == ("2001:db8::1", 65535)



# Generated at 2022-06-13 07:07:27.187096
# Unit test for function parse_address
def test_parse_address():
    # IPv4 addresses
    assert parse_address('192.0.2.3') == ('192.0.2.3', None)
    assert parse_address('192.0.2.3:22') == ('192.0.2.3', 22)
    assert parse_address('192.0.2.3:22', allow_ranges=True) == ('192.0.2.3', 22)
    assert parse_address('[192.0.2.3]:22') == ('192.0.2.3', 22)
    assert parse_address('[192.0.2.3]:22', allow_ranges=True) == ('192.0.2.3', 22)
    assert parse_address('[1.2.3.4]:22') == ('1.2.3.4', 22)

    # IPv4

# Generated at 2022-06-13 07:07:37.952702
# Unit test for function parse_address
def test_parse_address():
    import random
    import string
    import socket


# Generated at 2022-06-13 07:07:47.204005
# Unit test for function parse_address

# Generated at 2022-06-13 07:07:59.370726
# Unit test for function parse_address
def test_parse_address():

    # Symbolic names for the tuple fields; makes the tests easier to read.
    HOST = 0
    PORT = 1

    def test(text, expected):
        try:
            result = parse_address(text)
            if result != expected:
                print ("FAIL: parse_address(%s) -> %s, expected %s" %
                       (text, result, expected))
        except AnsibleError as e:
            if not expected:
                print ("FAIL: parse_address(%s) -> %s" % (text, e))

    # Basic tests: host:port
    test('foo.example.com:80', ('foo.example.com', 80))
    test('192.0.2.1:80', ('192.0.2.1', 80))

# Generated at 2022-06-13 07:08:05.535051
# Unit test for function parse_address
def test_parse_address():
    record = dict(host='foo', port=None)
    assert record == parse_address('foo')
    assert record == parse_address('foo:')
    assert record == parse_address('foo[0:5]')
    assert record == parse_address('foo[0:5]:')
    assert record == parse_address('foo[0:5]:5555')

    record = dict(host='192.0.2.3', port=None)
    assert record == parse_address('192.0.2.3')
    assert record == parse_address('192.0.2.3:')
    assert record == parse_address('192.0.2.3:5555')
    assert record == parse_address('192.0.2[0:5].3')

# Generated at 2022-06-13 07:08:16.501502
# Unit test for function parse_address
def test_parse_address():
    assert parse_address("localhost") == ("localhost", None)
    assert parse_address("localhost:22") == ("localhost", 22)
    assert parse_address("localhost:2222") == ("localhost", 2222)
    assert parse_address("localhost:222") == ("localhost", 222)
    assert parse_address("foo") == ("foo", None)
    assert parse_address("foo.example.com") == ("foo.example.com", None)
    assert parse_address("192.168.1.1") == ("192.168.1.1", None)
    assert parse_address("192.168.1.1:22") == ("192.168.1.1", 22)
    assert parse_address("192.168.1.1:2222") == ("192.168.1.1", 2222)

# Generated at 2022-06-13 07:08:26.660026
# Unit test for function parse_address
def test_parse_address():
    # ensure that the IPs and hosts are handed off successfully
    assert parse_address("127.0.0.1") == ('127.0.0.1', None)
    assert parse_address("127.0.0.1:22") == ('127.0.0.1', 22)
    assert parse_address("127.0.0.1:20-22") == ('127.0.0.1', 20)
    assert parse_address("127.0.0.1:20-22") == ('127.0.0.1', 20)
    assert parse_address("127.0.0.1:20-22", True) == ('127.0.0.1:20-22', 20)

# Generated at 2022-06-13 07:08:37.779552
# Unit test for function parse_address
def test_parse_address():
    parse = parse_address
    assert parse("example.org") == ("example.org", None)
    assert parse("[example.org]") == ("example.org", None)
    assert parse("[example.org]:1000") == ("example.org", 1000)
    assert parse("example.org:1000") == ("example.org", 1000)
    assert parse("192.168.42.0") == ("192.168.42.0", None)
    assert parse("192.168.42.0:1000") == ("192.168.42.0", 1000)
    assert parse("2001:db8::1") == ("2001:db8::1", None)
    assert parse("[2001:db8::1]") == ("2001:db8::1", None)