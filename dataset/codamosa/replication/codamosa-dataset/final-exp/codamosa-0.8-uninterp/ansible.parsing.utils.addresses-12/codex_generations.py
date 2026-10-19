

# Generated at 2022-06-13 07:07:04.741077
# Unit test for function parse_address
def test_parse_address():
    import sys

    if sys.version_info[0] < 3:
        # IP addresses
        assert parse_address('192.168.0.1') == ('192.168.0.1', None)
        assert parse_address('192.168.0.1:123') == ('192.168.0.1', 123)
        assert parse_address('192.168.0.1[1:3]') == ('192.168.0.1[1:3]', None)
        assert parse_address('192.168.0.1[1:3]:123') == ('192.168.0.1[1:3]', 123)
        assert parse_address('192.168.0.1[1:3:1]') == ('192.168.0.1[1:3:1]', None)
        assert parse_

# Generated at 2022-06-13 07:07:15.938051
# Unit test for function parse_address
def test_parse_address():
    print("Testing parse_address")

    # Basic cases: IPv4, IPv6, hostname, with and without port.
    assert parse_address('192.0.2.1') == ('192.0.2.1', None)
    assert parse_address('192.0.2.1:53') == ('192.0.2.1', 53)
    assert parse_address('[::1]') == ('::1', None)
    assert parse_address('[::1]:53') == ('::1', 53)
    assert parse_address('foo.example.com') == ('foo.example.com', None)
    assert parse_address('foo.example.com:53') == ('foo.example.com', 53)

    # The IPv6 address may not be contained in square brackets. The port must
    # be specified inside square brackets.


# Generated at 2022-06-13 07:07:27.226596
# Unit test for function parse_address
def test_parse_address():

    assert parse_address('[192.0.2.0]') == ('192.0.2.0', None)
    assert parse_address('[192.0.2.0]:80') == ('192.0.2.0', 80)
    assert parse_address('foo') == ('foo', None)
    assert parse_address('foo:80') == ('foo', 80)
    assert parse_address('foo.example.com') == ('foo.example.com', None)
    assert parse_address('foo.example.com:80') == ('foo.example.com', 80)
    assert parse_address('foo[1:2].example.com[6:7]:8080') == ('foo[1:2].example.com[6:7]', 8080)

# Generated at 2022-06-13 07:07:37.991920
# Unit test for function parse_address
def test_parse_address():

    assert parse_address('example.com') == ('example.com', None)
    assert parse_address('example.com:80') == ('example.com', 80)
    assert parse_address('example.com:443') == ('example.com', 443)

    assert parse_address('127.0.0.1') == ('127.0.0.1', None)
    assert parse_address('127.0.0.1:80') == ('127.0.0.1', 80)
    assert parse_address('127.0.0.1:443') == ('127.0.0.1', 443)

    assert parse_address('[::1]') == ('::1', None)
    assert parse_address('[::1]:80') == ('::1', 80)

# Generated at 2022-06-13 07:07:42.660401
# Unit test for function parse_address
def test_parse_address():

    def test(data, host=None, port=None):
        result = parse_address(data)
        assert (result == (host, port))

    test("[::1]", host="::1", port=None)
    test("[::1]:22", host="::1", port=22)
    test("[2001:db8::1]", host="2001:db8::1", port=None)
    test("[2001:db8::1]:22", host="2001:db8::1", port=22)
    test("[192.0.2.1]", host="192.0.2.1", port=None)
    test("[::ffff:192.0.2.1]", host="::ffff:192.0.2.1", port=None)

# Generated at 2022-06-13 07:07:56.900781
# Unit test for function parse_address
def test_parse_address():
    # network address with port specification
    assert parse_address("192.0.2.5:50") == ("192.0.2.5", 50)
    assert parse_address("198.51.100.0:34267") == ("198.51.100.0", 34267)
    assert parse_address("[2001:db8::4]:50") == ("2001:db8::4", 50)
    assert parse_address("[2001:db8::4]:65535") == ("2001:db8::4", 65535)
    assert parse_address("[192.0.2.1]:50") == ("192.0.2.1", 50)
    assert parse_address("[example.com]:50") == ("example.com", 50)

    # bare network address

# Generated at 2022-06-13 07:08:03.977937
# Unit test for function parse_address

# Generated at 2022-06-13 07:08:12.373755
# Unit test for function parse_address
def test_parse_address():
    assert parse_address('www.example.com') == ('www.example.com', None)
    assert parse_address('www.example.com:23') == ('www.example.com', 23)
    assert parse_address('[www.example.com]') == ('www.example.com', None)
    assert parse_address('[www.example.com]:23') == ('www.example.com', 23)
    assert parse_address('192.168.100.100') == ('192.168.100.100', None)
    assert parse_address('192.168.100.100:23') == ('192.168.100.100', 23)
    assert parse_address('[192.168.100.100]') == ('192.168.100.100', None)

# Generated at 2022-06-13 07:08:19.221792
# Unit test for function parse_address
def test_parse_address():
    assert parse_address('foo.example.com') == ('foo.example.com', None)
    assert parse_address('foo.example.com:23') == ('foo.example.com', 23)
    assert parse_address('foo.example.com:666') == ('foo.example.com', 666)
    assert parse_address('10.0.0.1:23') == ('10.0.0.1', 23)
    assert parse_address('10.0.0.1:666') == ('10.0.0.1', 666)
    assert parse_address('192.0.2.3:23') == ('192.0.2.3', 23)
    assert parse_address('192.0.2.3:666') == ('192.0.2.3', 666)

# Generated at 2022-06-13 07:08:27.455581
# Unit test for function parse_address
def test_parse_address():
    from ansible.playbook.play_context import PlayContext

    # Helper function to compare expected results with actual results.
    # Outputs PASS/FAIL and expected/actual results on failure.
    def test(i, e, a):
        if e == a:
            print("PASS[%d]: %s" % (i, e))
        else:
            print("FAIL[%d]: expected %s but got %s" % (i, e, a))

    # Test cases:
    #    Input string to parse,  # of elements in expected result,
    #    expected result