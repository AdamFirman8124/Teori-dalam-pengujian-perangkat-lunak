

# Generated at 2022-06-13 07:07:10.921734
# Unit test for function parse_address
def test_parse_address():
    assert parse_address("foo.example.com") == ("foo.example.com", None)
    assert parse_address("foo.example.com:22") == ("foo.example.com", 22)
    assert parse_address("foo[1:3].example.com:22") == ("foo[1:3].example.com", 22)
    assert parse_address("foo[1:3]:22") == ("foo[1:3]", 22)
    assert parse_address("[foo]:22") == ("foo", 22)
    assert parse_address("foo[1:3]") == ("foo[1:3]", None)
    assert parse_address("foo[1:3].example.com") == ("foo[1:3].example.com", None)

# Generated at 2022-06-13 07:07:19.192265
# Unit test for function parse_address
def test_parse_address():
    import sys
    import os
    my_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(my_dir)
    sys.path.append(parent_dir)
    from test.units.compat import unittest
    test_class = type('test_class', (unittest.TestCase,), {})

    def testmethod(self):
        self.assertEqual(parse_address('[1:2:3:4:5:6:7:8:9]:123'), ('[1:2:3:4:5:6:7:8:9]:123', None))

# Generated at 2022-06-13 07:07:30.662967
# Unit test for function parse_address
def test_parse_address():
    assert parse_address('') == (None, None)
    assert parse_address('example.com') == ('example.com', None)
    assert parse_address('example.com:80') == ('example.com', 80)
    assert parse_address('example.com:443') == ('example.com', 443)
    assert parse_address('example.com:443') == ('example.com', 443)
    assert parse_address('10.0.1.1') == ('10.0.1.1', None)
    assert parse_address('10.0.1.1') == ('10.0.1.1', None)
    assert parse_address('10.0.1.1:80') == ('10.0.1.1', 80)

# Generated at 2022-06-13 07:07:40.163583
# Unit test for function parse_address
def test_parse_address():
    assert parse_address('1.2.3.4') == ('1.2.3.4', None)
    assert parse_address('[1.2.3.4]') == ('1.2.3.4', None)
    assert parse_address('[1.2.3.4]:1234') == ('1.2.3.4', 1234)
    assert parse_address('foo[1:3].example.com') == ('foo[1:3].example.com', None)
    assert parse_address('foo[1:3].example.com:1234') == ('foo[1:3].example.com', 1234)
    assert parse_address('foo[1:3].example.com:1234', allow_ranges=True) == ('foo[1:3].example.com', 1234)
    assert parse

# Generated at 2022-06-13 07:07:54.795161
# Unit test for function parse_address
def test_parse_address():
    # Test handling of IP addresses.
    def ip(addr, expect):
        assert parse_address(addr) == expect, '%s should be %s but is %s' % (addr, expect, parse_address(addr))

    ip('192.0.2.3:30', ('192.0.2.3', 30))
    ip('192.0.2.3', ('192.0.2.3', None))
    ip('[2001:db8::1]:30', ('2001:db8::1', 30))
    ip('[1::2]:30', ('1::2', 30))
    ip('[2001:db8::]:30', ('2001:db8::', 30))
    ip('[::1]:30', ('::1', 30))
    ip('[::]:30', ('::', 30))

# Generated at 2022-06-13 07:07:55.622128
# Unit test for function parse_address
def test_parse_address():
    import nose2
    nose2.main()

# Generated at 2022-06-13 07:08:03.407364
# Unit test for function parse_address
def test_parse_address():
    assert parse_address("ansible.example.com") == ('ansible.example.com', None)
    assert parse_address("ansible:2049") == ('ansible', 2049)
    assert parse_address("ansible.example.com:2049") == ('ansible.example.com', 2049)
    assert parse_address("192.168.1.1") == ('192.168.1.1', None)
    assert parse_address("192.168.1.1:2049") == ('192.168.1.1', 2049)
    assert parse_address("[192.168.1.1]:2049") == ('[192.168.1.1]', 2049)
    assert parse_address("[fe80::1]:2049") == ('[fe80::1]', 2049)
    assert parse_

# Generated at 2022-06-13 07:08:11.877382
# Unit test for function parse_address
def test_parse_address():
    def check(addr, expected, allow_ranges=False):
        if expected is None:
            try:
                parse_address(addr, allow_ranges=allow_ranges)
            except (AnsibleError):
                pass
            else:
                assert(False)

        else:
            parsed = parse_address(addr, allow_ranges=allow_ranges)
            assert parsed == expected, \
                "parse_address('{}') failed, expected {} but got {}".format(addr, expected, parsed)

    # Examples taken from RFC 2396 and RFC 2732
    check('www.ansible.com', ('www.ansible.com', None))
    check('www.ansible.com:80', ('www.ansible.com', 80))

# Generated at 2022-06-13 07:08:24.387116
# Unit test for function parse_address
def test_parse_address():

    assert parse_address('192.0.2.1:22') == ('192.0.2.1', 22)
    assert parse_address('192.0.2.1:22', allow_ranges=True) == ('192.0.2.1', 22)
    assert parse_address('192.0.2.1:22,192.0.2.2:22') == ('192.0.2.1', 22)
    assert parse_address(u'192.0.2.1:22') == (u'192.0.2.1', 22)
    assert parse_address(u'192.0.2.1:22') == (u'192.0.2.1', 22)

    assert parse_address('[2001:db8::1]:22') == ('[2001:db8::1]', 22)

# Generated at 2022-06-13 07:08:35.787821
# Unit test for function parse_address
def test_parse_address():
    import unittest

    class TestParseAddress(unittest.TestCase):

        def test_hostname(self):
            self.assertEqual(parse_address('foo.example.net:12345'), ('foo.example.net', 12345))
            self.assertEqual(parse_address('foo.example.net:12345', allow_ranges=True), ('foo.example.net', 12345))
            self.assertEqual(parse_address('foo.example.net'), ('foo.example.net', None))
            self.assertEqual(parse_address('foo.example.net', allow_ranges=True), ('foo.example.net', None))
            self.assertEqual(parse_address('foo', allow_ranges=True), ('foo', None))