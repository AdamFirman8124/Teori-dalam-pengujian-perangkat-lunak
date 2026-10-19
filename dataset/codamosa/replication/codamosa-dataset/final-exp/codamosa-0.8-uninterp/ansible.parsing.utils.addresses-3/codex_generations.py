

# Generated at 2022-06-13 07:07:14.077629
# Unit test for function parse_address
def test_parse_address():
    def test(func, expected):
        result = func()
        if expected != result:
            raise AssertionError("got %s, expected %s" % (repr(result), repr(expected)))

    test(lambda: parse_address('foo'), ('foo', None))
    test(lambda: parse_address('foo:22'), ('foo', 22))
    test(lambda: parse_address('[foo]:22'), ('foo', 22))
    test(lambda: parse_address('192.0.2.1:44'), ('192.0.2.1', 44))
    test(lambda: parse_address('[192.0.2.1]:55'), ('192.0.2.1', 55))
    test(lambda: parse_address('[2001:db8::1]:66'), ('2001:db8::1', 66))
   

# Generated at 2022-06-13 07:07:25.074904
# Unit test for function parse_address

# Generated at 2022-06-13 07:07:36.550336
# Unit test for function parse_address

# Generated at 2022-06-13 07:07:47.136697
# Unit test for function parse_address
def test_parse_address():
    assert parse_address('www.example.com:80') == ('www.example.com', 80)
    assert parse_address('example.com') == ('example.com', None)
    assert parse_address('example.com:443') == ('example.com', 443)
    assert parse_address('www.example.com') == ('www.example.com', None)
    assert parse_address('192.0.2.1') == ('192.0.2.1', None)
    assert parse_address('192.0.2.1:443') == ('192.0.2.1', 443)
    assert parse_address('[2001:db8::1]:80') == ('[2001:db8::1]', 80)

# Generated at 2022-06-13 07:07:57.605501
# Unit test for function parse_address

# Generated at 2022-06-13 07:08:02.163312
# Unit test for function parse_address
def test_parse_address():
    def test_address(address, *args, **kwargs):
        try:
            result = parse_address(address, *args, **kwargs)
            print(address, '=>', repr(result))
        except AnsibleError as e:
            print(address, '=>', e)

    test_address('foo')
    test_address('192.0.2.3')
    test_address('2001:db8::1')
    test_address('foo.example.com')

    test_address('foo:123')
    test_address('192.0.2.3:123')
    test_address('2001:db8::1:123')
    test_address('foo.example.com:123')

    test_address('[foo]:123')
    test_address('[192.0.2.3]:123')

# Generated at 2022-06-13 07:08:11.311674
# Unit test for function parse_address
def test_parse_address():

    # A hostname with no port
    assert parse_address('example.com') == ('example.com', None)

    # An IPv4 address with no port
    assert parse_address('192.0.2.3') == ('192.0.2.3', None)

    # An IPv6 address with no port - we can't specify a port here
    assert parse_address('[::1]') == ('::1', None)

    # A hostname with a port
    assert parse_address('example.com:80') == ('example.com', 80)

    # An IPv4 address with a port
    assert parse_address('192.0.2.3:80') == ('192.0.2.3', 80)

    # An IPv6 address with a port

# Generated at 2022-06-13 07:08:18.601790
# Unit test for function parse_address

# Generated at 2022-06-13 07:08:27.514008
# Unit test for function parse_address

# Generated at 2022-06-13 07:08:38.312527
# Unit test for function parse_address

# Generated at 2022-06-13 07:08:52.566665
# Unit test for function parse_address
def test_parse_address():
    assert parse_address('www.example.com') == ('www.example.com', None)
    assert parse_address('www.example.com:80') == ('www.example.com', 80)
    assert parse_address('[www.example.com]:80') == ('[www.example.com]', 80)
    assert parse_address('localhost') == ('localhost', None)
    assert parse_address('localhost:80') == ('localhost', 80)
    assert parse_address('[localhost]:80') == ('[localhost]', 80)
    assert parse_address('foo.example.com[0:2]') == ('foo.example.com[0:2]', None)
    assert parse_address('foo.example.com[0:2]:80') == ('foo.example.com[0:2]', 80)
    assert parse_

# Generated at 2022-06-13 07:09:03.934057
# Unit test for function parse_address
def test_parse_address():

    def test(address, expected_host, expected_port):
        # According to the spec, the host is always present, but the port is
        # not. We use None to indicate that a port was not present.
        (host, port) = parse_address(address)
        assert host == expected_host
        assert port == expected_port

    # This is an exhaustive list of valid inputs to parse_address(). For each
    # input we specify the expected host and port components that should be
    # returned by the function.

    # IPv4, hostname, IPv6 addresses with a port
    test("192.0.2.1:22", "192.0.2.1", 22)
    test("[192.0.2.1]:22", "192.0.2.1", 22)

# Generated at 2022-06-13 07:09:13.234641
# Unit test for function parse_address
def test_parse_address():
    assert parse_address("hostname.example.com") == ("hostname.example.com", None)
    assert parse_address("hostname.example.com:49154") == ("hostname.example.com", 49154)
    assert parse_address("[192.0.2.3]:49154") == ("192.0.2.3", 49154)
    assert parse_address("[2001:db8::]:9000") == ("2001:db8::", 9000)
    assert parse_address("2001:db8::") == ("2001:db8::", None)
    assert parse_address("[2001:db8::]") == ("2001:db8::", None)
    assert parse_address("hostname.example.com", allow_ranges=True) == ("hostname.example.com", None)

# Generated at 2022-06-13 07:09:20.645673
# Unit test for function parse_address
def test_parse_address():
    """
    Unit test for function parse_address.
    """

    def assert_address(addr, default_port, host=None, port=default_port):
        """
        Assert that the given address string is parsed correctly and, if a host or
        port is supplied, that it matches the arguments.
        """
        r = parse_address(addr, allow_ranges=False)
        assert r is not None, "unable to parse %s" % addr
        if host is not None:
            assert host in r, "host mismatch: '%s' not in %r" % (host, r)
        if port is not None:
            assert port in r, "port mismatch: '%s' not in %r" % (port, r)

# Generated at 2022-06-13 07:09:35.683407
# Unit test for function parse_address

# Generated at 2022-06-13 07:09:47.949829
# Unit test for function parse_address
def test_parse_address():
    assert parse_address('[127.0.0.1]:1234') == ('[127.0.0.1]', 1234)
    assert parse_address('127.0.0.1:1234') == ('127.0.0.1', 1234)
    assert parse_address('example.com:1234') == ('example.com', 1234)
    assert parse_address('127.0.0.1') == ('127.0.0.1', None)
    assert parse_address('example.com') == ('example.com', None)
    assert parse_address('[::1]') == ('[::1]', None)
    assert parse_address('[::1]:1234') == ('[::1]', 1234)

# Generated at 2022-06-13 07:09:57.644857
# Unit test for function parse_address
def test_parse_address():
    # The test for invalid addresses is not very thorough, but that is not the
    # point of this function, and it's not easy to do.

    def try_address(a, expected_host, expected_port=None):
        (host, port) = parse_address(a)
        if host != expected_host or port != expected_port:
            raise AssertionError("'%s' returned %s:%s, expected %s:%s" %
                                 (a, host, port, expected_host, expected_port))

    # Correct host names
    try_address('foo', 'foo')
    try_address('foo.example.com', 'foo.example.com')
    try_address('f[o]o.example.com', 'f[o]o.example.com')

# Generated at 2022-06-13 07:10:06.112947
# Unit test for function parse_address

# Generated at 2022-06-13 07:10:10.938628
# Unit test for function parse_address
def test_parse_address():
    assert parse_address('foo') == ('foo', None)
    assert parse_address('foo:22') == ('foo', 22)
    assert parse_address('foo:22', True) == ('foo', 22)
    assert parse_address('foo:22', False) == ('foo', 22)
    assert parse_address('foo[1]') == ('foo[1]', None)
    assert parse_address('foo[1]', True) == ('foo[1]', None)
    assert parse_address('foo[1]', False) == ('foo[1]', None)
    assert parse_address('foo[1]:22') == ('foo[1]', 22)
    assert parse_address('foo[1]:22', True) == ('foo[1]', 22)

# Generated at 2022-06-13 07:10:22.378985
# Unit test for function parse_address
def test_parse_address():
    assert parse_address('127.0.0.1') == ('127.0.0.1', None), "Should parse host with no port"
    assert parse_address('127.0.0.1', True) == ('127.0.0.1', None), "Should parse host with no port"
    assert parse_address('127.0.0.1:22') == ('127.0.0.1', 22), "Should parse host with port"
    assert parse_address('127.0.0.1:22', True) == ('127.0.0.1', 22), "Should parse host with port"
    assert parse_address('localhost') == ('localhost', None), "Should parse hostname with no port"
    assert parse_address('localhost', True) == ('localhost', None), "Should parse hostname with no port"
    assert parse