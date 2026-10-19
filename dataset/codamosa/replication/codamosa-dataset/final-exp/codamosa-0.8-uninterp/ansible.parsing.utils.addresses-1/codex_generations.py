

# Generated at 2022-06-13 07:07:14.073824
# Unit test for function parse_address
def test_parse_address():
    assert parse_address('example.org') == ('example.org', None)
    assert parse_address('example.org:9000') == ('example.org', 9000)
    assert parse_address('[localhost]:9000') == ('localhost', 9000)
    assert parse_address('[2222:3333:4444:5555:6666:7777:8888:9999]:9000') == ('2222:3333:4444:5555:6666:7777:8888:9999', 9000)
    assert parse_address('[2222:3333:4444:5555:6666:7777:192.168.1.1]:9000') == ('2222:3333:4444:5555:6666:7777:192.168.1.1', 9000)

# Generated at 2022-06-13 07:07:25.075280
# Unit test for function parse_address
def test_parse_address():
    assert parse_address('localhost') == ('localhost', None)
    assert parse_address('localhost:22') == ('localhost', 22)
    assert parse_address('localhost:') == ('localhost', None)
    assert parse_address('localhost:xyz') == ('localhost', None)
    assert parse_address('127.0.0.1') == ('127.0.0.1', None)
    assert parse_address('127.0.0.1:22') == ('127.0.0.1', 22)
    assert parse_address('[127.0.0.1]') == ('127.0.0.1', None)
    assert parse_address('[127.0.0.1]:22') == ('127.0.0.1', 22)
    assert parse_address('[::1]') == ('::1', None)

# Generated at 2022-06-13 07:07:36.596798
# Unit test for function parse_address
def test_parse_address():
    # 1) IP V4
    host, port = parse_address("127.0.0.1:22")
    assert host == "127.0.0.1"
    assert port == 22

    # 2) IP V6 addresses surrounded by []. The port is specified after the
    # closing ].
    host, port = parse_address("[::1]:2222")
    assert host == "::1"
    assert port == 2222

    # 3) hostname with port
    host, port = parse_address("hostname:22")
    assert host == "hostname"
    assert port == 22

    # 4) IPv4 address with range
    try:
        parse_address("127.0.0.1[1:10]")
        assert False, "should have raised an error"
    except AnsibleParserError:
        pass

# Generated at 2022-06-13 07:07:47.136827
# Unit test for function parse_address
def test_parse_address():
    # No port specified
    assert ('10.0.0.1', None) == parse_address('10.0.0.1')
    assert ('10.0.0.1', None) == parse_address('10.0.0.1:')

    # No port specified, but we do have ranges
    assert ('10.0.0.1', None) == parse_address('10.0.0.1[1:2]')
    assert ('10.0.0.1', None) == parse_address('10.0.0.1[01:02]')
    assert ('10.0.0.1', None) == parse_address('10.0.0.1[01:02:03]')
    assert ('a.b', None) == parse_address('a.b[c:d]')

# Generated at 2022-06-13 07:07:57.606554
# Unit test for function parse_address
def test_parse_address():
    # We don't do exceptions for this one, because that is naturally
    # handled when we call AnsibleError.
    def check(input, expected):
        if expected is False:
            ok = False
            try:
                parse_address(input)
            except AnsibleError:
                ok = True
            assert ok, "%s should not parse as a host:port string" % input
            return

        (host, port) = parse_address(input)

        # Check that we got the expected values.
        if host != expected[0]:
            assert False, 'parse_address(%s) fails to return correct hostname: expected %s, got %s' % (input, expected[0], host)

# Generated at 2022-06-13 07:08:02.284031
# Unit test for function parse_address
def test_parse_address():
    """Returns (test passed, error message) or (True, None) on success."""


# Generated at 2022-06-13 07:08:13.909489
# Unit test for function parse_address
def test_parse_address():
    assert parse_address('foo:25') == ('foo', 25)
    assert parse_address('foo') == ('foo', None)
    assert parse_address('foo[1:5]') == ('foo[1:5]', None)
    assert parse_address('foo[1:5]:25') == ('foo[1:5]', 25)
    assert parse_address('[::1]') == ('[::1]', None)
    assert parse_address('[::1]:25') == ('[::1]', 25)
    assert parse_address('[1::1]') == ('[1::1]', None)
    assert parse_address('[1::1]:25') == ('[1::1]', 25)
    assert parse_address('1.2.3.4') == ('1.2.3.4', None)

# Generated at 2022-06-13 07:08:25.413095
# Unit test for function parse_address
def test_parse_address():
    # host, port = parse_address("foo.example.com")
    assert parse_address("foo.example.com") == ('foo.example.com', None)
    assert parse_address("foo.example.com:22") == ('foo.example.com', 22)
    assert parse_address("foo[1:3].example.com:22") == ('foo[1:3].example.com', 22)
    assert parse_address("foo[00:05].example.com:22") == ('foo[00:05].example.com', 22)

    assert parse_address("192.0.2.1:22") == ('192.0.2.1', 22)
    assert parse_address("192.0.2.1") == ('192.0.2.1', None)

# Generated at 2022-06-13 07:08:37.268760
# Unit test for function parse_address
def test_parse_address():

    # Bracketed expressions

    (host, port) = parse_address('[127.0.0.1]')
    assert host == '127.0.0.1'
    assert port is None

    (host, port) = parse_address('[127.0.0.1]:22')
    assert host == '127.0.0.1'
    assert port == 22

    (host, port) = parse_address('[example.com]:52')
    assert host == 'example.com'
    assert port == 52

    (host, port) = parse_address('[example.com]')
    assert host == 'example.com'
    assert port is None

    (host, port) = parse_address('[foo[1:3].example.com]')

# Generated at 2022-06-13 07:08:51.036491
# Unit test for function parse_address
def test_parse_address():
    assert parse_address('foo') == ('foo', None)
    assert parse_address('192.0.2.1') == ('192.0.2.1', None)
    assert parse_address('192.0.2.1:22') == ('192.0.2.1', 22)
    assert parse_address('foo:22') == ('foo', 22)
    assert parse_address('[foo]:22') == ('foo', 22)
    assert parse_address('[192.0.2.1]:22') == ('192.0.2.1', 22)
    assert parse_address('[::1]:22') == ('::1', 22)
    assert parse_address('foo[1:3]') == ('foo[1:3]', None)