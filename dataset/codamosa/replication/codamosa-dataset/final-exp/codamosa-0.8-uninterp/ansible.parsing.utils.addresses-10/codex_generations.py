

# Generated at 2022-06-13 07:07:12.152395
# Unit test for function parse_address
def test_parse_address():
    assert parse_address('[localhost]') == ('localhost', None)
    assert parse_address('localhost:22') == ('localhost', 22)
    assert parse_address('[localhost]:22') == ('localhost', 22)
    assert parse_address('[127.0.0.1]') == ('127.0.0.1', None)
    assert parse_address('127.0.0.1:22') == ('127.0.0.1', 22)
    assert parse_address('[127.0.0.1]:22') == ('127.0.0.1', 22)
    assert parse_address('[::1]') == ('::1', None)
    assert parse_address('::1:22') == ('::1', 22)
    assert parse_address('[::1]:22') == ('::1', 22)
   

# Generated at 2022-06-13 07:07:20.177567
# Unit test for function parse_address
def test_parse_address():
    def dotest(address, expected, allow_ranges=False):
        expected = (expected, None) if expected else (None, None)
        result = parse_address(address, allow_ranges)
        assert result == expected, "parse_address(%r, %r) returned %r instead of %r" % \
                                   (address, allow_ranges, result, expected)

    def dotest_with_port(address, expected, expected_port, allow_ranges=False):
        expected = (expected, expected_port) if expected else (None, None)
        result = parse_address(address, allow_ranges)
        assert result == expected, "parse_address(%r, %r) returned %r instead of %r" % \
                                   (address, allow_ranges, result, expected)

    # Test parsing of

# Generated at 2022-06-13 07:07:30.832942
# Unit test for function parse_address
def test_parse_address():
    # hostnames
    assert parse_address('foo') == ('foo', None)
    assert parse_address('foo.example.com') == ('foo.example.com', None)
    assert parse_address('foo.example.com:1234') == ('foo.example.com', 1234)
    assert parse_address('[foo.example.com]:1234') == ('foo.example.com', 1234)
    assert not parse_address('d[x]')
    assert not parse_address('-')
    assert not parse_address('foo:')
    assert not parse_address('[foo]')
    assert not parse_address('[foo]:1234:5678')

    # ipv4
    assert parse_address('192.0.2.3') == ('192.0.2.3', None)
    assert parse_address

# Generated at 2022-06-13 07:07:40.201127
# Unit test for function parse_address
def test_parse_address():
    assert ('localhost', None) == parse_address('localhost')
    assert ('localhost', 22) == parse_address('localhost:22')
    assert ('foo[1:2].example.org', None) == parse_address('foo[1:2].example.org')
    assert ('foo[1:2].example.org', 22) == parse_address('foo[1:2].example.org:22')
    assert ('foo[1:2].example.org', 22) == parse_address('foo[1:2].example.org[1:2]:22')
    assert ('192.0.2.3', None) == parse_address('192.0.2.3')
    assert ('192.0.2.3', 22) == parse_address('192.0.2[1:2].3:22')

# Generated at 2022-06-13 07:07:54.794661
# Unit test for function parse_address
def test_parse_address():
    from ansible.compat.tests import unittest

    class TestNetworkAddresses(unittest.TestCase):
        def test_port_only(self):
            self.assertRaises(AnsibleError, parse_address, ":22")

        def test_silly_ports(self):
            self.assertRaises(AnsibleError, parse_address, ":666666")
            self.assertRaises(AnsibleError, parse_address, ":0")

        def test_empty_address(self):
            self.assertRaises(AnsibleError, parse_address, "")

        def test_ipv4_address_only(self):
            self.assertEquals(parse_address("127.0.0.1"), ("127.0.0.1", None))


# Generated at 2022-06-13 07:08:02.814693
# Unit test for function parse_address

# Generated at 2022-06-13 07:08:11.459381
# Unit test for function parse_address
def test_parse_address():
    from nose.tools import assert_equal


# Generated at 2022-06-13 07:08:23.878588
# Unit test for function parse_address
def test_parse_address():
    import pytest

    # returns (host, port)

# Generated at 2022-06-13 07:08:35.666331
# Unit test for function parse_address
def test_parse_address():
    # Simple case, name
    assert ('host', None) == parse_address('host')
    # Simple case, IPv4, with port
    assert ('192.168.1.1', 1234) == parse_address('192.168.1.1:1234')
    assert ('192.168.1.1', None) == parse_address('192.168.1.1')
    # IPv4 with '[' in name
    assert ('192.168.1.1[1:3]', 1234) == parse_address('192.168.1.1[1:3]:1234')
    assert ('192.168.1.1[1:3]', None) == parse_address('192.168.1.1[1:3]')
    assert ('192.168.1.1[1-2]', None) == parse_

# Generated at 2022-06-13 07:08:46.956497
# Unit test for function parse_address
def test_parse_address():
    assert parse_address(":") == (None, None)
    assert parse_address("foo:") == ("foo", None)
    assert parse_address("foo:12") == ("foo", 12)
    assert parse_address("foo:012") == ("foo", 12)
    assert parse_address("[foo:12]") == ("foo:12", None)
    assert parse_address("[foo:12]:34") == ("foo:12", 34)
    assert parse_address("[foo:bar]:34") == ("foo:bar", 34)
    assert parse_address("[foo:bar]:034") == ("foo:bar", 34)
    assert parse_address("[foo]:bar:34") == (None, None)
    assert parse_address("foo.bar:1234") == ("foo.bar", 1234)
    assert parse_