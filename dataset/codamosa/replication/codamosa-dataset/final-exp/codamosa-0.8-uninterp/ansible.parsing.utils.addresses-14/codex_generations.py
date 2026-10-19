

# Generated at 2022-06-13 07:07:09.703433
# Unit test for function parse_address
def test_parse_address():
    (host, port) = parse_address("example.com")
    assert host == "example.com"
    assert port == None

    (host, port) = parse_address("example.com:22")
    assert host == "example.com"
    assert port == 22

    (host, port) = parse_address("example.com[1:3]")
    assert host == "example.com[1:3]"
    assert port == None

    (host, port) = parse_address("example.com[1:3].example.org:22")
    assert host == "example.com[1:3].example.org"
    assert port == 22

    (host, port) = parse_address("192.168.0.1")
    assert host == "192.168.0.1"
    assert port == None


# Generated at 2022-06-13 07:07:18.529899
# Unit test for function parse_address

# Generated at 2022-06-13 07:07:29.979597
# Unit test for function parse_address
def test_parse_address():
    try:
        parse_address("")
        assert False
    except AnsibleError:
        pass

    try:
        parse_address("192.168.0.1:65536")
        assert False
    except AnsibleError:
        pass

    try:
        parse_address("192.168.0.1:99999")
        assert False
    except AnsibleError:
        pass

    try:
        parse_address("192.168.0.1[1:99999]")
        assert False
    except AnsibleParserError:
        pass

    try:
        parse_address("192.168.999.999")
        assert False
    except AnsibleError:
        pass

    try:
        parse_address("192.168.999.999")
        assert False
    except AnsibleError:
        pass

   

# Generated at 2022-06-13 07:07:39.472402
# Unit test for function parse_address
def test_parse_address():
    x = parse_address('localhost.localdomain')
    assert x[0] == 'localhost.localdomain'
    assert x[1] is None

    x = parse_address('localhost.localdomain:7777')
    assert x[0] == 'localhost.localdomain'
    assert x[1] == 7777

    x = parse_address('[localhost.localdomain]:7777')
    assert x[0] == 'localhost.localdomain'
    assert x[1] == 7777

    x = parse_address('[192.0.2.1]:7777')
    assert x[0] == '192.0.2.1'
    assert x[1] == 7777

    x = parse_address('192.0.2.1:7777')

# Generated at 2022-06-13 07:07:44.024127
# Unit test for function parse_address
def test_parse_address():
    parse_address('[::1]:22')
    parse_address('[::1]')  # port implied by brackets
    parse_address('[2001:db8::1]:22')
    parse_address('[0:0:0:0:0:0:0:1]:22')
    parse_address('[0:0:0:0:0:0:0:1]')
    parse_address('[::ffff:127.0.0.1]:22')
    parse_address('[::ffff:127.0.0.1]')
    parse_address('127.0.0.1:22')
    parse_address('192.0.2.1:22', allow_ranges=True)
    parse_address('foo[0:4].example.com:22', allow_ranges=True)
    parse

# Generated at 2022-06-13 07:07:54.395276
# Unit test for function parse_address
def test_parse_address():
    """
    Tests the function parse_address() to make sure it returns
    the expected results when it is given various inputs.
    """
    # test that a basic hostname with a port works
    (test_host, test_port) = parse_address('test.example.com:1234')
    assert test_host == 'test.example.com'
    assert test_port == 1234

    # test that hostname with a port in brackets works
    (test_host, test_port) = parse_address('[test.example.com]:1234')
    assert test_host == 'test.example.com'
    assert test_port == 1234

    # test that a hostname with a port in brackets works
    (test_host, test_port) = parse_address('[example.com]:1234')

# Generated at 2022-06-13 07:08:02.390975
# Unit test for function parse_address
def test_parse_address():

    assert(parse_address("192.0.2.1") == ("192.0.2.1", None))
    assert(parse_address("192.0.2.1:22") == ("192.0.2.1", 22))
    assert(parse_address("192.0.2.1:22") == ("192.0.2.1", 22))
    assert(parse_address("192.0.2.1:22") == ("192.0.2.1", 22))
    assert(parse_address("[2001:db8:a0b:12f0::1]") == ("2001:db8:a0b:12f0::1", None))

# Generated at 2022-06-13 07:08:14.020329
# Unit test for function parse_address
def test_parse_address():
    """
    This can't be a nose test because it depends on the use of actual
    exceptions.
    """
    # Bracketed addresses
    assert parse_address('[127.0.0.1]:22')        == ('127.0.0.1', 22)
    assert parse_address('[127.0.0.1]')           == ('127.0.0.1', None)
    assert parse_address('[[::1]]:5432')          == ('[::1]', 5432)
    assert parse_address('[[::1]]')               == ('[::1]', None)
    assert parse_address('[server.example.com]')  == ('server.example.com', None)

    # Bracketed addresses with ranges
    assert parse_address('[127.0.0.[1:3]]:22')   

# Generated at 2022-06-13 07:08:25.420872
# Unit test for function parse_address

# Generated at 2022-06-13 07:08:37.258959
# Unit test for function parse_address
def test_parse_address():
    def test(address, host, port):
        assert parse_address(address) == (host, port)

    # Test IPv4 addresses and host names
    test('[127.0.0.1]:8000', '127.0.0.1', 8000)
    test('foo[1]:8000', 'foo[1]', 8000)
    test('foo[0]:8000', 'foo[0]', 8000)
    test('foo:8000', 'foo', 8000)
    test('foo[1:3]:8000', 'foo[1:3]', 8000)
    test('foo:8000', 'foo', 8000)
    test('localhost', 'localhost', None)
    test('127.0.0.1', '127.0.0.1', None)

# Generated at 2022-06-13 07:08:51.927406
# Unit test for function parse_address
def test_parse_address():
    """
    This test exists primarily as a way to avoid accidental breakage during
    refactoring, and to support future development.

    TODO: test the range patterns.
    """


# Generated at 2022-06-13 07:09:03.239416
# Unit test for function parse_address
def test_parse_address():
    """
    Test the parse_address function.
    """

    import json
    import pytest
    from ansible.module_utils import six


# Generated at 2022-06-13 07:09:07.210001
# Unit test for function parse_address

# Generated at 2022-06-13 07:09:15.443620
# Unit test for function parse_address
def test_parse_address():
    parse_func = parse_address

# Generated at 2022-06-13 07:09:23.231755
# Unit test for function parse_address
def test_parse_address():
    # TODO: put this into a test suite
    assert parse_address('example.com') == ('example.com', None)
    assert parse_address('[::1]') == ('::1', None)
    assert parse_address('[::1]', True) == ('::1', None)
    assert parse_address('foo[0:2].example.com') == ('foo[0:2].example.com', None)
    assert parse_address('foo[0:2].example.com', True) == ('foo[0:2].example.com', None)

    assert parse_address('foo[x-z].example.com') == ('foo[x-z].example.com', None)
    assert parse_address('foo[x-z].example.com', True) == ('foo[x-z].example.com', None)


# Generated at 2022-06-13 07:09:32.817349
# Unit test for function parse_address
def test_parse_address():
    import json

    with open('parse_address_test.json', 'r') as f:
        data = json.load(f)

    for row in data['rows']:
        expected = row['expected']
        address = row['address']

        message = "parse_address('%s') should return %s" % (address, expected)
        try:
            result = parse_address(address)
        except Exception as e:
            result = e
            if expected == 'error':
                continue
        assert result == expected, message

# Generated at 2022-06-13 07:09:39.813956
# Unit test for function parse_address
def test_parse_address():
    print("testing parse_address()")

    def check(host, port, allow_ranges=False):
        expected = (host, port)
        try:
            actual = parse_address(host, allow_ranges=allow_ranges)
            assert actual == expected, "address was '%s', expected %s but got %s" % (host, expected, actual)
        except Exception as e:
            assert False, "while trying to parse_address of '%s', got %s (%s)" % (host, e, e.__doc__)

    def check_invalid(host):
        try:
            actual = parse_address(host)
            assert False, "expected parse_address of '%s' to fail, but got %s" % (host, actual)
        except Exception as e:
            pass


# Generated at 2022-06-13 07:09:48.985471
# Unit test for function parse_address
def test_parse_address():
    # Test cases for parse_address() function
    cases = [['[2001:db8::7]', ('2001:db8::7', None)],
             ['[2001:db8::7]:22', ('2001:db8::7', 22)],
             ['[2001:db8::7]:0', ('2001:db8::7', 0)]]
    for case in cases:
        try:
            assert case[1] == parse_address(case[0])
            print("Success: %s" % case[0])
        except AssertionError as e:
            print("Test case '%s' failed: %s" % (case[0], e))

# Generated at 2022-06-13 07:09:58.329193
# Unit test for function parse_address
def test_parse_address():
    # valid IPv4 addresses in various forms
    assert(parse_address("192.0.2.3"))
    assert(parse_address("192.0.2.3:22"))
    assert(parse_address("192.0.2.3:[22, 23]"))
    assert(parse_address("192.0.2.3[22:23]:22"))
    assert(parse_address("192.0.2.3[22:23:2]:22"))
    assert(parse_address("192.0.2.3[22:24:2]:22"))
    assert(parse_address("192.0.2.3[22:24:2]:[22:23]"))
    assert(parse_address("192.0.2.3[22:24:2]:[22:23:2]"))

# Generated at 2022-06-13 07:10:08.136784
# Unit test for function parse_address
def test_parse_address():
    # Individual failures should raise an exception
    test_cases = [
        ('[not_an_ipv6_address', 'incomplete bracketed expression'),
        ('[not_an_ipv6_address]', 'invalid IP address or hostname inside brackets'),
        ('[not_an_ipv6_address]:99', 'invalid IP address or hostname inside brackets'),
        ('not_a_hostname:99', 'missing port number'),
        ('not_a_hostname.com', 'not a valid network hostname'),
        ('192.168.1.1[1]', 'has a range, but we were told to ignore ranges'),
    ]
