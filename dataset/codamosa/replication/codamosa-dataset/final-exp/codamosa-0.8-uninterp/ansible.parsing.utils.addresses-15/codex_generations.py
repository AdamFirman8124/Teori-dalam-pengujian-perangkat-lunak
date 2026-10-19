

# Generated at 2022-06-13 07:07:14.542684
# Unit test for function parse_address

# Generated at 2022-06-13 07:07:25.412574
# Unit test for function parse_address
def test_parse_address():
    if patterns['ipv4'].match('192.0.2.3') is not None:
        print('Unit test for function parse_address: failed')
    elif patterns['ipv4'].match('[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}') is not None:
        print('Unit test for function parse_address: failed')
    elif patterns['ipv6'].match('[0-9a-f]{1,4}:[0-9a-f]{1,4}') is not None:
        print('Unit test for function parse_address: failed')

# Generated at 2022-06-13 07:07:36.857906
# Unit test for function parse_address
def test_parse_address():
    import sys

    def test(address, expected):
        output = parse_address(address)
        if output != expected:
            print("{address}: {expected!r} expected, got {output!r}".format(
                address=address, expected=expected, output=output))
            sys.exit(1)

    test('[1:2:3]', ('[1:2:3]', None))
    test('[1:2:3:4:5:6:7:8]', ('[1:2:3:4:5:6:7:8]', None))
    test('[1:2:3:4:5:6:7:8]:443', ('[1:2:3:4:5:6:7:8]', 443))

# Generated at 2022-06-13 07:07:47.136605
# Unit test for function parse_address

# Generated at 2022-06-13 07:07:59.346852
# Unit test for function parse_address

# Generated at 2022-06-13 07:08:05.354677
# Unit test for function parse_address
def test_parse_address():
    def test(address, allow_ranges, expected_host, expected_port, fail=False):
        #print 'testing %r...' % address
        try:
            host, port = parse_address(address, allow_ranges)
        except AnsibleError:
            if fail:
                return
            raise
        assert host == expected_host, \
            'host %r != expected host %r' % (host, expected_host)
        assert port == expected_port, \
            'port %r != expected port %r' % (port, expected_port)

    # IPv4 with port
    test('192.0.2.3:22', False, '192.0.2.3', 22)
    test('192.0.2.3:22', False, '192.0.2.3', 22)

# Generated at 2022-06-13 07:08:16.499484
# Unit test for function parse_address

# Generated at 2022-06-13 07:08:26.626695
# Unit test for function parse_address
def test_parse_address():
    import unittest

    def addTest(host, port, allow_ranges=False):
        # note that port can be None
        if port is not None:
            port = str(port)
        else:
            port = ''
        if port:
            host = host + ':' + port
        if allow_ranges:
            host = host + ' (ranges allowed)'
        else:
            host = host + ' (ranges not allowed)'
        tc = TestCase(lambda: self.assertEqual( (host, port), parse_address(host, allow_ranges=allow_ranges) ))
        setattr(tc, 'test_' + host, lambda: None)
        TestParseAddress.addTest(tc)

# Generated at 2022-06-13 07:08:37.733832
# Unit test for function parse_address
def test_parse_address():

    def check(input_value, expected_output, expected_exception=None):
        if expected_exception:
            try:
                result = parse_address(input_value)
                assert False, 'should have raised'
            except AnsibleError as e:
                assert e.message == expected_exception
        else:
            result = parse_address(input_value)
            assert result == expected_output

    check('', (None, None))
    check('foo:bar', (None, None))
    check('[foo]:bar', (None, None))

    check('foo:1', ('foo', 1))
    check('[foo]:1', ('foo', 1))
    check('[foo]:01', ('foo', 1))
    check('[foo]:257', (None, None))

# Generated at 2022-06-13 07:08:51.294785
# Unit test for function parse_address

# Generated at 2022-06-13 07:09:04.071802
# Unit test for function parse_address
def test_parse_address():
    import unittest

    class TestParseAddress(unittest.TestCase):

        def test_failure(self):
            self.assertRaises(AnsibleError, parse_address, '')
            self.assertRaises(AnsibleError, parse_address, ':')
            self.assertRaises(AnsibleError, parse_address, ':::')
            self.assertRaises(AnsibleError, parse_address, 'foo:bar')
            self.assertRaises(AnsibleError, parse_address, '[foo]')
            self.assertRaises(AnsibleError, parse_address, '-foo')
            self.assertRaises(AnsibleError, parse_address, 'foo-')
            self.assertRaises(AnsibleError, parse_address, 'foo_-')
            self

# Generated at 2022-06-13 07:09:13.304038
# Unit test for function parse_address
def test_parse_address():
  assert parse_address('hostname:80') == ('hostname', 80)
  assert parse_address('hostname') == ('hostname', None)
  assert parse_address('[ff:ff::]:80') == ('ff:ff::', 80)
  assert parse_address('192.0.2.3:80') == ('192.0.2.3', 80)
  assert parse_address('192.0.2.3') == ('192.0.2.3', None)
  assert parse_address('[192.0.2.3]') == ('192.0.2.3', None)
  assert parse_address('[192.0.2.3]:80') == ('192.0.2.3', 80)

# Generated at 2022-06-13 07:09:20.687213
# Unit test for function parse_address
def test_parse_address():
    #
    # Test that the parsing of IPv4 addresses works.
    #

    # Test basic IPv4 address(es)
    assert parse_address('192.0.2.1') == ('192.0.2.1', None)
    assert parse_address('192.0.2.1:80') == ('192.0.2.1', 80)
    assert parse_address('[192.0.2.1]:80') == ('192.0.2.1', 80)

    # Test that IPv4 addresses with ranges work (1)
    assert parse_address('192.0.2.[1:5]') == ('192.0.2.[1:5]', None)
    assert parse_address('192.0.2.[1:5]:80') == ('192.0.2.[1:5]', 80)

# Generated at 2022-06-13 07:09:35.684786
# Unit test for function parse_address
def test_parse_address():
    import pytest
    # Test cases and expected result

# Generated at 2022-06-13 07:09:47.950784
# Unit test for function parse_address
def test_parse_address():
    assert parse_address("foo") == ("foo", None)
    assert parse_address("foo:1234") == ("foo", 1234)
    assert parse_address("foo[bar]") == ("foo[bar]", None)
    assert parse_address("foo[bar]:1234") == ("foo[bar]", 1234)
    assert parse_address("[foo]:1234") == ("foo", 1234)
    assert parse_address("[foo]") == ("foo", None)
    assert parse_address("[foo][bar]") == ("foo[bar]", None)
    assert parse_address("[foo][bar]:1234") == ("foo[bar]", 1234)
    assert parse_address("[foo[bar]]:1234") == ("foo[bar]", 1234)

# Generated at 2022-06-13 07:09:57.644670
# Unit test for function parse_address

# Generated at 2022-06-13 07:10:06.111854
# Unit test for function parse_address
def test_parse_address():
    import unittest


# Generated at 2022-06-13 07:10:11.929914
# Unit test for function parse_address

# Generated at 2022-06-13 07:10:22.860039
# Unit test for function parse_address
def test_parse_address():
    import unittest


# Generated at 2022-06-13 07:10:34.502781
# Unit test for function parse_address
def test_parse_address():

    # No port
    assert (None, None) == parse_address('example.com')
    assert (None, None) == parse_address('192.0.2.1')
    assert (None, None) == parse_address('[2001:db8::1]')

    # With port
    assert (None, None) == parse_address('example.com:')
    assert (None, None) == parse_address('192.0.2.1:')
    assert (None, None) == parse_address('[2001:db8::1]:')

    # No port, IPv4
    assert (None, None) == parse_address('[192.0.2.1]')
    assert (None, None) == parse_address('[192.0.2.[1]]')