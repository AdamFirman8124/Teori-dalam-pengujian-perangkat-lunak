

# Generated at 2022-06-13 07:07:15.634390
# Unit test for function parse_address
def test_parse_address():
    import json

    results = { }
    error = None
    data = None

    try:
        with open('./test/units/library/parse_address.json', 'r') as f:
            data = json.load(f)
        for specifier in data:
            host, port = parse_address(specifier, allow_ranges=True)
            results[specifier] = [ host, port ]
    except (OSError, IOError):
        error = "Failed to open or read from ./test/units/library/parse_address.json"

# Generated at 2022-06-13 07:07:27.144197
# Unit test for function parse_address
def test_parse_address():
    assert parse_address('foo.bar.com') == ('foo.bar.com', None)
    assert parse_address('foo.bar.com:22') == ('foo.bar.com', 22)
    assert parse_address('foo.bar.com:22-j', allow_ranges=True) == ('foo.bar.com:22-j', None)
    assert parse_address('foo.bar.com:22-j') == ('foo.bar.com', None)
    assert parse_address('192.0.2.1', allow_ranges=True) == ('192.0.2.1', None)
    assert parse_address('192.0.2.1') == ('192.0.2.1', None)

# Generated at 2022-06-13 07:07:37.911442
# Unit test for function parse_address
def test_parse_address():
    assert ('foo', None) == parse_address('foo')
    assert ('foo', None) == parse_address('foo.example.com')
    assert ('foo.example.com', None) == parse_address('foo.example.com.')
    assert ('bar', None) == parse_address('foo.example.com.bar')
    assert ('foo.example.com', None) == parse_address('foo.example.com.bar.')
    assert ('192.0.2.3', None) == parse_address('192.0.2.3')
    assert ('192.0.2.3', None) == parse_address('192.0.2.3.example.com')
    assert ('192.0.2.3', None) == parse_address('192.0.2.3.example.com.')

# Generated at 2022-06-13 07:07:47.203255
# Unit test for function parse_address
def test_parse_address():
    assert parse_address('foo:22') == ('foo', 22)
    assert parse_address('foo') == ('foo', None)
    assert parse_address('foo.example.com') == ('foo.example.com', None)
    assert parse_address('[::1]:22') == ('::1', 22)
    assert parse_address('::1') == ('::1', None)
    assert parse_address('192.0.2.1:22') == ('192.0.2.1', 22)
    assert parse_address('192.0.2.1') == ('192.0.2.1', None)

    assert parse_address('foo[1:3]') == ('foo[1:3]', None)
    assert parse_address('foo[1:3]:22') == ('foo[1:3]', 22)


# Generated at 2022-06-13 07:07:57.682800
# Unit test for function parse_address
def test_parse_address():
    assert parse_address('[foo.example.com]:443') == (u'foo.example.com', 443)
    assert parse_address('foo.example.com:443') == (u'foo.example.com', 443)
    assert parse_address('foo.example.com') == (u'foo.example.com', None)
    assert parse_address('foo[1:3].example.com') == (u'foo[1:3].example.com', None)
    assert parse_address('foo[1:3].example.com:443') == (u'foo[1:3].example.com', 443)
    assert parse_address('[foo[1:3].example.com]:443') == (u'foo[1:3].example.com', 443)

# Generated at 2022-06-13 07:08:02.245708
# Unit test for function parse_address
def test_parse_address():
    host = None
    port = None

    result = parse_address('foo.example.com')
    assert result[0] == 'foo.example.com'
    assert result[1] is None

    result = parse_address('foo.example.com:22')
    assert result[0] == 'foo.example.com'
    assert result[1] == 22

    result = parse_address('foo[1:3].example.com')
    assert result[0] == 'foo[1:3].example.com'
    assert result[1] is None

    result = parse_address('foo[1:3].example.com:22')
    assert result[0] == 'foo[1:3].example.com'
    assert result[1] == 22


# Generated at 2022-06-13 07:08:11.351617
# Unit test for function parse_address
def test_parse_address():
    import itertools
    import pytest

    def assert_parse(address, want_host, want_port=None):
        actual_host, actual_port = parse_address(address, allow_ranges=True)
        assert actual_host == want_host
        assert actual_port == want_port

    # Hostnames
    # Some are legal
    assert_parse('example.com', 'example.com')
    assert_parse('a_b-c.d-e.f-0.g_h', 'a_b-c.d-e.f-0.g_h')
    assert_parse('foo[1:3]', 'foo[1:3]')
    assert_parse('foo[x-z]', 'foo[x-z]')

# Generated at 2022-06-13 07:08:16.443117
# Unit test for function parse_address
def test_parse_address():
    # Valid functions
    assert parse_address('foo.bar') == ('foo.bar', None)
    assert parse_address('[foo.bar]') == ('foo.bar', None)
    assert parse_address('foo.bar:1234') == ('foo.bar', 1234)
    assert parse_address('[foo.bar]:1234') == ('foo.bar', 1234)
    assert parse_address('192.0.2.123') == ('192.0.2.123', None)
    assert parse_address('[192.0.2.123]') == ('192.0.2.123', None)
    assert parse_address('[192.0.2.123]:1234') == ('192.0.2.123', 1234)
    assert parse_address('[::ffff:192.0.2.123]')

# Generated at 2022-06-13 07:08:26.592447
# Unit test for function parse_address

# Generated at 2022-06-13 07:08:37.691520
# Unit test for function parse_address
def test_parse_address():
    assert parse_address('localhost') == ('localhost', None)
    assert parse_address('hetzner[1:50]') == ('hetzner[1:50]', None)
    assert parse_address('hetzner[1:50]:22') == ('hetzner[1:50]', 22)
    assert parse_address('[192.168.1.42]:22') == ('192.168.1.42', 22)
    assert parse_address('[2001:db8:85a3::8a2e:370:7334]:22') == ('2001:db8:85a3::8a2e:370:7334', 22)
