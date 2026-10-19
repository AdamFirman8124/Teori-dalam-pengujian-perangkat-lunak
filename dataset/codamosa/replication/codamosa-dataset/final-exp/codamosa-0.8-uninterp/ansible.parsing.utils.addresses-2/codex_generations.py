

# Generated at 2022-06-13 07:07:04.520024
# Unit test for function parse_address
def test_parse_address():
    """ Unit tests for the parse_address() function """

    # Test cases:
    # * address
    # * expected host, None tuple

# Generated at 2022-06-13 07:07:09.519694
# Unit test for function parse_address
def test_parse_address():
    import unittest
    import pytest

    class TestParseAddress(unittest.TestCase):
        def test_valid_hostnames_with_ports(self):
            for hostname in ('local.example.com', 'foo.bar.example.com'):
                self.assertEqual(parse_address(hostname), (hostname, None))
                self.assertEqual(parse_address('%s:22' % hostname), (hostname, 22))
                self.assertEqual(parse_address('[%s]:22' % hostname), (hostname, 22))

        def test_valid_ipv4_addresses_with_ports(self):
            for ip in ('192.0.2.1', '127.0.0.1', '10.1.2.3'):
                self.assertE

# Generated at 2022-06-13 07:07:18.351354
# Unit test for function parse_address

# Generated at 2022-06-13 07:07:29.596779
# Unit test for function parse_address
def test_parse_address():
    import pytest
    from ansible.errors import AnsibleError

    # This used to succeed (return '') but now raises an AnsibleError.
    with pytest.raises(AnsibleError):
        parse_address('')

    assert parse_address('example.com') == ('example.com', None)
    assert parse_address('example.com:22') == ('example.com', 22)
    assert parse_address('[127.0.0.1]') == ('127.0.0.1', None)
    assert parse_address('[127.0.0.1]:22') == ('127.0.0.1', 22)
    assert parse_address('[127.0.0.1:22]') == ('127.0.0.1:22', None)

# Generated at 2022-06-13 07:07:39.093176
# Unit test for function parse_address
def test_parse_address():
    """
    host is the host component of the address,
    port is the port component of the address,
    address is the string to be parsed,
    allow_ranges is whether ranges should be considered valid or invalid.
    """

# Generated at 2022-06-13 07:07:47.305408
# Unit test for function parse_address

# Generated at 2022-06-13 07:07:57.837073
# Unit test for function parse_address

# Generated at 2022-06-13 07:08:02.518118
# Unit test for function parse_address
def test_parse_address():
    """
    Unit test for function parse_address
    """
    def test_parse_address(address, allow_ranges, expected_host, expected_port):
        host, port = parse_address(address, allow_ranges=allow_ranges)
        assert host == expected_host
        assert port == expected_port

    # hostname or IPv4 with or without port should work
    test_parse_address('[::1]', allow_ranges=False, expected_host='[::1]', expected_port=None)
    test_parse_address('[::1]', allow_ranges=True, expected_host='[::1]', expected_port=None)
    test_parse_address('[::1]:22', allow_ranges=False, expected_host='[::1]', expected_port=22)
    test

# Generated at 2022-06-13 07:08:14.203807
# Unit test for function parse_address
def test_parse_address():
    # test valid cases
    parse_address('192.168.1.1')
    parse_address('192.168.1.1:123')
    parse_address('[2001:0db8:85a3:0000:0000:8a2e:0370:7334]')
    parse_address('[2001:0db8:85a3:0000:0000:8a2e:0370:7334]:123')
    parse_address('foo.example.com')
    parse_address('foo.example.com:123')
    parse_address('foo[1:3].example.com')
    parse_address('foo[1:3].example.com:123')
    parse_address('foo[1:3].example.com[1:3]')

# Generated at 2022-06-13 07:08:25.452018
# Unit test for function parse_address
def test_parse_address():
    assert parse_address('123.123.123.123') == ('123.123.123.123', None)
    assert parse_address('127.0.0.1') == ('127.0.0.1', None)
    assert parse_address('[::1]') == ('::1', None)
    assert parse_address('[dead:beef::1]') == ('dead:beef::1', None)
    assert parse_address('hostname.example.org') == ('hostname.example.org', None)
    assert parse_address('hostname.example.org:59999') == ('hostname.example.org', 59999)
    assert parse_address('1.2.3.4:59999') == ('1.2.3.4', 59999)