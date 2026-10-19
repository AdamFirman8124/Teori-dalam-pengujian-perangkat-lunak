

# Generated at 2022-06-13 07:07:09.720743
# Unit test for function parse_address
def test_parse_address():
    assert ('foo', None) == parse_address('foo')
    assert ('foo', None) == parse_address('FOO')
    assert ('foo', 123) == parse_address('foo:123')
    assert ('foo', None) == parse_address('foo:')
    assert ('foo', None) == parse_address('foo[1:2]')

    assert ('192.0.2.3', None) == parse_address('192.0.2.3')
    assert ('192.0.2.3', None) == parse_address('192.0.2.3[0:255]')
    assert ('192.0.2.3', None) == parse_address('192.0.2.3[0:255][0:255]')

# Generated at 2022-06-13 07:07:18.531030
# Unit test for function parse_address
def test_parse_address():
    for (host, port, address) in [
        ('localhost', 22, 'localhost:22'),
        ('localhost', None, 'localhost'),
        ('127.0.0.1', 22, '127.0.0.1:22'),
        ('127.0.0.1', None, '127.0.0.1'),
        ('[::1]', 22, '[::1]:22'),
        ('[::1]', None, '[::1]'),
        ('[::ffff:192.0.2.3]', 22, '[::ffff:192.0.2.3]:22'),
        ('[::ffff:192.0.2.3]', None, '[::ffff:192.0.2.3]'),
    ]:
        parsed = parse_address(address)

# Generated at 2022-06-13 07:07:29.980032
# Unit test for function parse_address

# Generated at 2022-06-13 07:07:39.473422
# Unit test for function parse_address
def test_parse_address():
    import re
    assert parse_address('foo.example.com') == ('foo.example.com', None)
    assert parse_address('foo.example.com:123') == ('foo.example.com', 123)
    assert parse_address('[foo.example.com]:123') == ('foo.example.com', 123)
    assert parse_address('[::1]:123') == ('::1', 123)
    assert parse_address('[::1]') == ('::1', None)
    assert parse_address('[::1', allow_ranges=True) == ('[::1', None)
    assert parse_address('[::1:2:3:4:5:6:7:8:9]:123') == ('::1:2:3:4:5:6:7:8:9', 123)
    assert parse_

# Generated at 2022-06-13 07:07:47.571138
# Unit test for function parse_address

# Generated at 2022-06-13 07:07:58.156219
# Unit test for function parse_address
def test_parse_address():
    # a hostname is fine:
    assert parse_address('foo') == ('foo', None)
    assert parse_address('foo.example.com') == ('foo.example.com', None)
    assert parse_address('www.example.com:42') == ('www.example.com', 42)
    assert parse_address('[foo]') == ('foo', None)
    assert parse_address('[foo.example.com]') == ('foo.example.com', None)
    assert parse_address('[www.example.com]:42') == ('www.example.com', 42)
    # an IPv4 address is fine:
    assert parse_address('192.0.2.1') == ('192.0.2.1', None)

# Generated at 2022-06-13 07:08:02.911422
# Unit test for function parse_address

# Generated at 2022-06-13 07:08:11.561407
# Unit test for function parse_address

# Generated at 2022-06-13 07:08:24.092724
# Unit test for function parse_address
def test_parse_address():
    import sys
    if sys.version_info[0] == 2:
        import ipaddr
        # ipaddr.IPAddress("::1") is broken in ipaddr 2.1.11.
        obj = ipaddr.IPv6Address
    else:
        import ipaddress
        obj = ipaddress.IPv6Address

    # Tests for IPv4 addresses
    assert parse_address('192.0.2.1') == ('192.0.2.1', None)
    assert parse_address('192.0.2.1:80') == ('192.0.2.1', 80)
    assert parse_address('192.0.2.1:8080') == ('192.0.2.1', 8080)

# Generated at 2022-06-13 07:08:35.664799
# Unit test for function parse_address
def test_parse_address():
    # basic hostnames, IPv4 addresses and IPv6 addresses
    assert parse_address('foo') == ('foo', None)
    assert parse_address('foo.example.com') == ('foo.example.com', None)
    assert parse_address('192.0.2.3') == ('192.0.2.3', None)
    assert parse_address('[2001:db8::1]') == ('[2001:db8::1]', None)

    # IPv4 addresses with a port specification
    assert parse_address('192.0.2.3:22') == ('192.0.2.3', 22)
    assert parse_address('foo:22') == ('foo', 22)
    assert parse_address('[2001:db8::1]:22') == ('[2001:db8::1]:22', 22) # required

    #