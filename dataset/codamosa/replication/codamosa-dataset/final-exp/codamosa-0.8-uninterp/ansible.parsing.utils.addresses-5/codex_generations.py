

# Generated at 2022-06-13 07:07:04.807552
# Unit test for function parse_address
def test_parse_address():

    import pytest

    host, port = parse_address('foo')
    assert host == 'foo'
    assert port is None

    host, port = parse_address('foo:23')
    assert host == 'foo'
    assert port == 23

    host, port = parse_address('[::1]')
    assert host == '[::1]'
    assert port is None

    host, port = parse_address('[::1]:23')
    assert host == '[::1]'
    assert port == 23

    host, port = parse_address('192.0.2.1')
    assert host == '192.0.2.1'
    assert port is None

    host, port = parse_address('192.0.2.1:23')
    assert host == '192.0.2.1'
    assert port == 23

   

# Generated at 2022-06-13 07:07:15.969376
# Unit test for function parse_address
def test_parse_address():
    assert parse_address('example.com') == ('example.com', None)
    assert parse_address('example.com:22') == ('example.com', 22)
    assert parse_address('[example.com]:22') == ('example.com', 22)
    assert parse_address('85.14.0.168') == ('85.14.0.168', None)
    assert parse_address('85.14.0.168:22') == ('85.14.0.168', 22)
    assert parse_address('85.14.0.168:22', allow_ranges=True) == ('85.14.0.168', 22)
    assert parse_address('85.14.0.168:22', allow_ranges=False) == ('85.14.0.168', 22)

# Generated at 2022-06-13 07:07:27.224928
# Unit test for function parse_address
def test_parse_address():
    assert parse_address('example.com') == ('example.com', None)
    assert parse_address('example.com:80') == ('example.com', 80)
    assert parse_address('192.0.2.1') == ('192.0.2.1', None)
    assert parse_address('192.0.2.1:80') == ('192.0.2.1', 80)
    assert parse_address('[2001:db8::1]') == ('2001:db8::1', None)
    assert parse_address('[2001:db8::1]:80') == ('2001:db8::1', 80)
    assert parse_address('[192.0.2.1]') == ('192.0.2.1', None)

# Generated at 2022-06-13 07:07:37.991876
# Unit test for function parse_address
def test_parse_address():
    import binascii
    from ansible.utils.unicode import to_bytes
    from ansible.utils.vars import combine_vars


# Generated at 2022-06-13 07:07:44.158821
# Unit test for function parse_address
def test_parse_address():

    # Only IPv6 can be used without the "[]", but the port spec is optional.
    assert parse_address('2001:db8::1') == ('2001:db8::1', None)
    assert parse_address('[2001:db8::1]:80') == ('2001:db8::1', 80)
    assert parse_address('[2001:db8::1]') == ('2001:db8::1', None)
    assert parse_address('[2001:db8::1]:80') == ('2001:db8::1', 80)
    assert parse_address('[2001:db8::1:a]:80b') == ('2001:db8::1:a', 80)

# Generated at 2022-06-13 07:07:54.549161
# Unit test for function parse_address

# Generated at 2022-06-13 07:08:02.524889
# Unit test for function parse_address

# Generated at 2022-06-13 07:08:14.277098
# Unit test for function parse_address
def test_parse_address():
    assert parse_address('foo[0:9].example.com') == \
        ('foo[0:9].example.com', None)
    assert parse_address('foo.example.com:23') == \
        ('foo.example.com', 23)
    assert parse_address('bar.example.com[0:9]:23') == \
        ('bar.example.com[0:9]', 23)
    assert parse_address('[::ffff:192.0.2.3]:23') == \
        ('[::ffff:192.0.2.3]', 23)
    assert parse_address('[0:0:0:0:0:0:0:1]:23') == \
        ('[0:0:0:0:0:0:0:1]', 23)

# Generated at 2022-06-13 07:08:25.451369
# Unit test for function parse_address

# Generated at 2022-06-13 07:08:37.302063
# Unit test for function parse_address