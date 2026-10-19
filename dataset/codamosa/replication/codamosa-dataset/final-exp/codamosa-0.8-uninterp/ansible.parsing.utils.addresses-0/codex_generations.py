

# Generated at 2022-06-13 07:07:09.677418
# Unit test for function parse_address

# Generated at 2022-06-13 07:07:18.498493
# Unit test for function parse_address
def test_parse_address():
    # throw a bunch of valid and invalid hosts at it and make sure it does the
    # right thing in each case
    assert parse_address('foo') == ('foo', None)
    assert parse_address('foo:22') == ('foo', 22)
    assert parse_address('foo:bar') == None
    assert parse_address('192.0.2.1') == ('192.0.2.1', None)
    assert parse_address('192.0.2.1:22') == ('192.0.2.1', 22)
    assert parse_address('[::1]') == ('::1', None)
    assert parse_address('[::1]:22') == ('::1', 22)
    assert parse_address('[192.0.2.1]') == ('192.0.2.1', None)
    assert parse

# Generated at 2022-06-13 07:07:29.717887
# Unit test for function parse_address

# Generated at 2022-06-13 07:07:39.209233
# Unit test for function parse_address
def test_parse_address():
    '''
       Test parse_address()
    '''

    import pytest


# Generated at 2022-06-13 07:07:47.403898
# Unit test for function parse_address
def test_parse_address():

    assert parse_address('192.0.2.1:1234') == ('192.0.2.1', 1234)
    assert parse_address('[2001:db8::1]:1234') == ('[2001:db8::1]', 1234)
    assert parse_address('2001:db8::1:1234') == ('2001:db8::1:1234', None)

    # square braces
    assert parse_address('[foo]') == ('foo', None)
    assert parse_address('[foo]:1234') == ('foo', 1234)

    assert parse_address('foo') == ('foo', None)
    assert parse_address('foo:1234') == ('foo', 1234)

    # square braces with port in address

# Generated at 2022-06-13 07:07:57.956045
# Unit test for function parse_address

# Generated at 2022-06-13 07:08:02.686472
# Unit test for function parse_address
def test_parse_address():
    assert parse_address('foo') == ('foo', None)
    assert parse_address('foo.example.com') == ('foo.example.com', None)
    assert parse_address('[2001:db8::1]:22') == ('2001:db8::1', 22)
    assert parse_address('192.0.2.3:22') == ('192.0.2.3', 22)
    assert parse_address('foo[0:2].example.com') == ('foo[0:2].example.com', None)
    assert parse_address('foo[a:c].example.com') == ('foo[a:c].example.com', None)

    assert parse_address('foo{2,4}.example.com') == ('foo[2:4].example.com', None)

# Generated at 2022-06-13 07:08:11.387801
# Unit test for function parse_address

# Generated at 2022-06-13 07:08:23.705929
# Unit test for function parse_address
def test_parse_address():
    test_hostname = 'foo.example.com'
    (host, port) = parse_address(test_hostname)
    assert host == test_hostname
    assert port == None

    test_ipv4 = '192.0.2.1'
    (host, port) = parse_address(test_ipv4)
    assert host == test_ipv4
    assert port == None

    test_ipv6 = '2001:db8:85a3::8a2e:370:7334'
    (host, port) = parse_address(test_ipv6)
    assert host == test_ipv6
    assert port == None

    (host, port) = parse_address('[%s]' % test_ipv6)
    assert host == test_ipv6
    assert port == None

   

# Generated at 2022-06-13 07:08:35.622409
# Unit test for function parse_address
def test_parse_address():
    # Valid addresses
    host, port = parse_address('127.0.0.1')
    assert (port is None)
    assert (host == '127.0.0.1')

    host, port = parse_address('127.0.0.1:22')
    assert (port == 22)
    assert (host == '127.0.0.1')

    host, port = parse_address('[127.0.0.1]')
    assert (port is None)
    assert (host == '127.0.0.1')

    host, port = parse_address('[127.0.0.1]:22')
    assert (port == 22)
    assert (host == '127.0.0.1')

    host, port = parse_address('[::1]')
    assert (port is None)
