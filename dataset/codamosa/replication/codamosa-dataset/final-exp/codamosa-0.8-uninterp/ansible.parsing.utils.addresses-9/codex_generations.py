

# Generated at 2022-06-13 07:07:13.775006
# Unit test for function parse_address
def test_parse_address():
    """
    >>> test_parse_address()
    True
    """
    def assert_equal(a, b):
        assert (a == b)

    assert_equal(parse_address("foo[1:3]"), ('foo[1:3]', None))
    assert_equal(parse_address("foo[0:5]-bar[x-z]"), ('foo[0:5]-bar[x-z]', None))
    assert_equal(parse_address("foo[1:3]", allow_ranges=True), ('foo[1:3]', None))
    assert_equal(parse_address("[1:3]", allow_ranges=True), ('[1:3]', None))
    assert_equal(parse_address("[::1]", allow_ranges=True), ('[::1]', None))


# Generated at 2022-06-13 07:07:24.613386
# Unit test for function parse_address
def test_parse_address():

    assert parse_address('ipv4[00:10]') == ('ipv4[00:10]', None)
    assert parse_address('ipv4[00:10]:33') == ('ipv4[00:10]', 33)
    assert parse_address('ipv6[2001:db8::ff00:42:8329]:80') == ('ipv6[2001:db8::ff00:42:8329]', 80)
    assert parse_address('ipv6[2001:db8::ff00:42:8329]') is None
    assert parse_address('foo[1:3].example.com') == ('foo[1:3].example.com', None)
    assert parse_address('foo[1:3].example.com:33') == ('foo[1:3].example.com', 33)
   

# Generated at 2022-06-13 07:07:36.009602
# Unit test for function parse_address
def test_parse_address():

    from ansible.utils.hashing import checksum_s

    def assert_parse(address, expected_host, expected_port=None, allow_ranges=False):
        (got_host, got_port) = parse_address(address, allow_ranges)
        assert got_host == expected_host and got_port == expected_port


# Generated at 2022-06-13 07:07:40.502548
# Unit test for function parse_address
def test_parse_address():
    assert parse_address('localhost') == ('localhost', None)
    assert parse_address('localhost:6379') == ('localhost', 6379)
    assert parse_address('127.0.0.1') == ('127.0.0.1', None)
    assert parse_address('127.0.0.1:6379') == ('127.0.0.1', 6379)
    assert parse_address('127.0.0.1[1:2]') == ('127.0.0.1[1:2]', None)
    assert parse_address('127.0.0.1[1:2]:6379') == ('127.0.0.1[1:2]', 6379)
    assert parse_address('[::]:6379') == ('[::]', 6379)

# Generated at 2022-06-13 07:07:54.936494
# Unit test for function parse_address
def test_parse_address():
    assert parse_address('127.0.0.1:1234') == ('127.0.0.1', 1234)
    assert parse_address('127.0.0.1') == ('127.0.0.1', None)
    assert parse_address('[::1]:1234') == ('::1', 1234)
    assert parse_address('[::1]') == ('::1', None)
    assert parse_address('[2001:db8::1]:1234') == ('2001:db8::1', 1234)
    assert parse_address('[2001:db8::1]') == ('2001:db8::1', None)
    assert parse_address('[2001:db8::1%lo0]:1234') == ('2001:db8::1%lo0', 1234)

# Generated at 2022-06-13 07:08:02.898899
# Unit test for function parse_address
def test_parse_address():
    assert parse_address('localhost') == ('localhost', None)
    assert parse_address('localhost:1234') == ('localhost', 1234)
    assert parse_address('127.0.0.1') == ('127.0.0.1', None)
    assert parse_address('127.0.0.1:1234') == ('127.0.0.1', 1234)
    assert parse_address('[127.0.0.1]:1234') == ('127.0.0.1', 1234)
    assert parse_address('[2001:db8::1]:1234') == ('2001:db8::1', 1234)
    assert parse_address('2001:db8::1:1234') == ('2001:db8::1', 1234)

# Generated at 2022-06-13 07:08:11.527008
# Unit test for function parse_address
def test_parse_address():
    # Verify that we recognize an IPv4 address.
    assert parse_address('192.0.2.0') == ('192.0.2.0', None)

    # Verify that we recognize an IPv4 address with a port number.
    assert parse_address('192.0.2.3:10054') == ('192.0.2.3', 10054)
    assert parse_address('[192.0.2.3]:10054') == ('192.0.2.3', 10054)

    # Verify that we recognize an IPv4 address with a range.
    # We use this to specify multiple hosts in a single line:
    # example.com[1:10].

# Generated at 2022-06-13 07:08:24.007431
# Unit test for function parse_address

# Generated at 2022-06-13 07:08:35.665860
# Unit test for function parse_address
def test_parse_address():
    import unittest

    class TestParseAddress(unittest.TestCase):
        def test_hostport(self):
            self.assertEqual(parse_address('example.com:22'), ('example.com', 22))
            self.assertEqual(parse_address('[example.com]:22'), ('example.com', 22))

        def test_ipv4(self):
            self.assertEqual(parse_address('192.0.2.1'), ('192.0.2.1', None))
            self.assertEqual(parse_address('192.0.2.1:22'), ('192.0.2.1', 22))
            self.assertEqual(parse_address('[192.0.2.1]'), ('192.0.2.1', None))

# Generated at 2022-06-13 07:08:49.072066
# Unit test for function parse_address