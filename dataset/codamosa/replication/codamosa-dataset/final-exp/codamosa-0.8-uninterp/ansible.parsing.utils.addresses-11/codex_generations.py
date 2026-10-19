

# Generated at 2022-06-13 07:07:13.998894
# Unit test for function parse_address
def test_parse_address():
    address = 'foo[1:2].example.org:1234'
    (host, port) = parse_address(address, allow_ranges=False)
    assert host is None
    assert port is None

    address = 'foo[1:2].example.org:1234'
    (host, port) = parse_address(address, allow_ranges=True)
    assert host == 'foo[1:2].example.org'
    assert port == 1234

    address = '[2001:db8::1]:1234'
    (host, port) = parse_address(address, allow_ranges=False)
    assert host == '2001:db8::1'
    assert port == 1234

    address = '2001:db8::1:1234'

# Generated at 2022-06-13 07:07:24.999763
# Unit test for function parse_address
def test_parse_address():

    def fail(msg):
        raise AssertionError(msg)

    def check(addr, host, port):
        (h, p) = parse_address(addr)
        if h != host:
            fail("%s -> host '%s' (expected '%s')" % (addr, h, host))
        if p != port:
            fail("%s -> port '%s' (expected '%s')" % (addr, p, port))

    def check_range(addr, expect_error):
        try:
            parse_address(addr, allow_ranges=False)
        except AnsibleParserError:
            if not expect_error:
                fail("%s -> detected range (expected no error)" % addr)

# Generated at 2022-06-13 07:07:36.449940
# Unit test for function parse_address

# Generated at 2022-06-13 07:07:47.094109
# Unit test for function parse_address
def test_parse_address():
    assert parse_address("127.0.0.1") == ("127.0.0.1", None)
    assert parse_address("127.0.0.1:123") == ("127.0.0.1", 123)
    assert parse_address("[::1]:123") == ("::1", 123)
    assert parse_address("[::1]") == ("::1", None)
    assert parse_address("ssh.example.com") == ("ssh.example.com", None)
    assert parse_address("ssh.example.com:22") == ("ssh.example.com", 22)
    assert parse_address("ssh.example.com[foo]:22") == ("ssh.example.com[foo]", 22)

# Generated at 2022-06-13 07:07:59.323083
# Unit test for function parse_address

# Generated at 2022-06-13 07:08:05.512225
# Unit test for function parse_address
def test_parse_address():
    """Validate that parse_address() behaves as expected."""

    import pytest

    # hostname with no port, no ranges.
    (host, port) = parse_address('foo.example.com')
    assert host == 'foo.example.com'
    assert port is None

    # hostname with no port, with ranges.
    (host, port) = parse_address('foo[1:10].example.com')
    assert host == 'foo[1:10].example.com'
    assert port is None

    # IPv4 address with no port, no ranges.
    (host, port) = parse_address('192.0.2.1')
    assert host == '192.0.2.1'
    assert port is None

    # IPv4 address with port, no ranges.
    (host, port) = parse_address

# Generated at 2022-06-13 07:08:16.503704
# Unit test for function parse_address
def test_parse_address():
    print(repr(parse_address('127.0.0.1')))
    print(repr(parse_address('127.0.0.1:22')))
    print(repr(parse_address('foo.example.com')))
    print(repr(parse_address('[::1]')))
    print(repr(parse_address('[::1]:22')))
    print(repr(parse_address('[127.0.0.1]')))
    print(repr(parse_address('[127.0.0.1]:22')))
    print(repr(parse_address('foo[1:3].example.com')))
    print(repr(parse_address('foo[1:3].example.com:22')))

# Generated at 2022-06-13 07:08:26.668958
# Unit test for function parse_address
def test_parse_address():
    # We use this as a standard for comparison throughout these tests.
    ipv4_base = (
        '192.0.2.1', 22
    )

    # Test IPv4 with a port
    assert parse_address('192.0.2.1:22') == ipv4_base

    # Test IPv4 with no port
    assert parse_address('192.0.2.1') == ('192.0.2.1', None)

    # Test IPv4 with a range
    assert parse_address('192.0.2[1:3]:22', True) == (
        '192.0.2[1:3]', 22
    )

    # Test IPv4 with a range and no port

# Generated at 2022-06-13 07:08:37.813057
# Unit test for function parse_address

# Generated at 2022-06-13 07:08:48.430852
# Unit test for function parse_address
def test_parse_address():
    assert parse_address('foo') == ('foo', None)
    assert parse_address('foo:80') == ('foo', 80)
    assert parse_address('foo:80:90') == ('foo:80:90', None)
    assert parse_address('[foo]:80') == ('foo', 80)
    assert parse_address('192.0.2.3') == ('192.0.2.3', None)
    assert parse_address('192.0.2.3:80') == ('192.0.2.3', 80)
    assert parse_address('[192.0.2.3]:80') == ('192.0.2.3', 80)
    assert parse_address('2001:db8::1') == ('2001:db8::1', None)
    assert parse_address('[2001:db8::1]')

# Generated at 2022-06-13 07:09:01.225166
# Unit test for function parse_address
def test_parse_address():
    # Basic tests
    assert parse_address('example.com') == ('example.com', None)
    assert parse_address('example.com:42') == ('example.com', 42)
    assert parse_address('[::1]') == ('::1', None)
    assert parse_address('[::1]:42') == ('::1', 42)
    assert parse_address('192.0.2.1') == ('192.0.2.1', None)
    assert parse_address('192.0.2.1:42') == ('192.0.2.1', 42)
    assert parse_address('192.0.2.1/24') == ('192.0.2.1/24', None)

# Generated at 2022-06-13 07:09:11.363789
# Unit test for function parse_address

# Generated at 2022-06-13 07:09:19.537381
# Unit test for function parse_address

# Generated at 2022-06-13 07:09:34.470905
# Unit test for function parse_address
def test_parse_address():
    assert parse_address('[::1]:1234') == ('::1', 1234)
    assert parse_address(':1234') == (None, 1234)
    assert parse_address('[::1]') == ('::1', None)
    assert parse_address('::1') == (None, None)
    assert parse_address("[a::1]:1234") == ('a::1', 1234)
    assert parse_address("example.com:1234") == ('example.com', 1234)
    assert parse_address("user@[a::1]:1234") == (None, None)
    assert parse_address("[a::1]/32") == (None, None)
    assert parse_address("[::1]@example.com") == (None, None)


# Generated at 2022-06-13 07:09:40.300029
# Unit test for function parse_address
def test_parse_address():
    def test(input, expected_host, expected_port):
        (host, port) = parse_address(input)
        assert host == expected_host
        assert port == expected_port

    # Test IPv4
    test('192.0.2.1', '192.0.2.1', None)
    test('192.0.2.1:22', '192.0.2.1', 22)
    test('[192.0.2.1]:22', '192.0.2.1', 22)
    test('[192.0.2.1]', '192.0.2.1', None)

    # Test IPv6 addresses
    test('::1', '::1', None)
    test('[::]:22', '::', 22)
    test('[::1]', '::1', None)


# Generated at 2022-06-13 07:09:50.187312
# Unit test for function parse_address
def test_parse_address():
    # Just a simple hostname
    h, p = parse_address("foo[1:3].example.com")
    assert h == "foo[1:3].example.com"
    assert p is None
    # With a port
    h, p = parse_address("foo[1:3].example.com:1234")
    assert h == "foo[1:3].example.com"
    assert p == 1234
    # An IPv6 address with a port
    h, p = parse_address("[::1]:22")
    assert h == "::1"
    assert p == 22
    # IPv4 with a port. We don't allow or check for ranges in IPv4 addresses.
    h, p = parse_address("192.0.2.42:22")
    assert h == "192.0.2.42"


# Generated at 2022-06-13 07:10:01.856412
# Unit test for function parse_address
def test_parse_address():
    assert parse_address('[10.0.0.1]', True) == ('10.0.0.1', None)
    assert parse_address('server[1:2].example.com', True) == ('server[1:2].example.com', None)
    assert parse_address('server[1:2].example.com', False) == ('server[1:2].example.com', None)
    assert parse_address('server1.example.com', True) == ('server1.example.com', None)
    assert parse_address('server2.example.com', True) == ('server2.example.com', None)
    assert parse_address('server[1:3:2].example.com', True) == ('server[1:3:2].example.com', None)

# Generated at 2022-06-13 07:10:10.135728
# Unit test for function parse_address
def test_parse_address():
    # Valid inputs, IPv4, IPv6 and hostname with port
    assert (parse_address('192.168.1.1') == ('192.168.1.1', None))
    assert (parse_address('192.168.1.1:22') == ('192.168.1.1', 22))
    assert (parse_address('[1:2:3:4:5:6:7:8]') == ('1:2:3:4:5:6:7:8', None))
    assert (parse_address('[1:2:3:4:5:6:7:8]:22') == ('1:2:3:4:5:6:7:8', 22))
    assert (parse_address('host.example.com') == ('host.example.com', None))

# Generated at 2022-06-13 07:10:21.849928
# Unit test for function parse_address
def test_parse_address():
    assert parse_address("example.com") == (b"example.com", None)
    assert parse_address("example.com:50") == (b"example.com", 50)
    assert parse_address("[example.com]") == (b"example.com", None)
    assert parse_address("[example.com]:50") == (b"example.com", 50)
    assert parse_address("foo[1:3].example.com:50") == (b"foo[1:3].example.com", 50)
    assert parse_address("foo[1:3].example.com") == (b"foo[1:3].example.com", None)
    assert parse_address("192.168.1.2:50") == (b"192.168.1.2", 50)

# Generated at 2022-06-13 07:10:33.235014
# Unit test for function parse_address