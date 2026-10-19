

# Generated at 2022-06-13 07:07:14.544870
# Unit test for function parse_address
def test_parse_address():
    assert parse_address('localhost') == ('localhost', None)
    assert parse_address('localhost:123') == ('localhost', 123)

    assert parse_address('127.0.0.1') == ('127.0.0.1', None)
    assert parse_address('127.0.0.1:123') == ('127.0.0.1', 123)
    assert parse_address('127.0.0.1:123:456') == ('127.0.0.1:123:456', None)

    assert parse_address('[::1]') == ('::1', None)
    assert parse_address('[::1]:123') == ('::1', 123)
    assert parse_address('[::1]:123:456') == ('::1', 123)


# Generated at 2022-06-13 07:07:25.413555
# Unit test for function parse_address
def test_parse_address():
    host, port = parse_address("[::1]:5900")
    assert host == "::1"
    assert port == 5900
    host, port = parse_address("192.0.2.3:5900")
    assert host == "192.0.2.3"
    assert port == 5900
    host, port = parse_address("example.com:5900")
    assert host == "example.com"
    assert port == 5900
    host, port = parse_address("example.com")
    assert host == "example.com"
    assert port is None
    host, port = parse_address("192.0.2.3")
    assert host == "192.0.2.3"
    assert port is None

# Generated at 2022-06-13 07:07:33.590343
# Unit test for function parse_address
def test_parse_address():
    assert parse_address('1.2.3.4') == ('1.2.3.4', None)
    assert parse_address('1.2.3.4:22') == ('1.2.3.4', 22)
    assert parse_address('1.2.3.4[2:4]') == ('1.2.3.4[2:4]', None)
    assert parse_address('1.2.3.4[2:4]:22') == ('1.2.3.4[2:4]', 22)
    assert parse_address('1.2.3.4[2:4]:22', allow_ranges=True) == ('1.2.3.4[2:4]', 22)

# Generated at 2022-06-13 07:07:41.744361
# Unit test for function parse_address
def test_parse_address():
    assert parse_address('[127.0.0.1]:123') == ('127.0.0.1', 123)
    assert parse_address('127.0.0.1') == ('127.0.0.1', None)
    assert parse_address('127.0.0.1:123') == ('127.0.0.1', 123)
    assert parse_address('something:5432') == ('something', 5432)
    assert parse_address('[some thing]') == ('some thing', None)
    assert parse_address('[some[thing]') == ('some[thing', None)
    assert parse_address('some[thing]') == ('some[thing]', None)
    assert parse_address('[some[thing]') == ('some[thing', None)

# Generated at 2022-06-13 07:07:51.377137
# Unit test for function parse_address
def test_parse_address():
    assert parse_address("localhost") == ("localhost", None)
    assert parse_address("localhost.localdomain") == ("localhost.localdomain", None)
    assert parse_address("localhost:5") == ("localhost", 5)
    assert parse_address("localhost.localdomain:5") == ("localhost.localdomain", 5)
    assert parse_address("localhost[1:2]") == ("localhost[1:2]", None)
    assert parse_address("localhost[1:2]:5") == ("localhost[1:2]", 5)
    assert parse_address("localhost[0:2]") == ("localhost[0:2]", None)
    assert parse_address("localhost[1:2]") == ("localhost[1:2]", None)

# Generated at 2022-06-13 07:08:00.606325
# Unit test for function parse_address
def test_parse_address():
    assert parse_address('foo:1') == ('foo', 1)
    assert parse_address('foo.example.com:22') == ('foo.example.com', 22)
    assert parse_address('[::1]:22') == ('::1', 22)
    assert parse_address('192.168.0.1:22') == ('192.168.0.1', 22)
    assert parse_address('192.168.0.1') == ('192.168.0.1', None)
    assert parse_address('192.168.0.1[0:10]:22') == ('192.168.0.1[0:10]', 22)
    assert parse_address('192.168.0.1[0:10]') == ('192.168.0.1[0:10]', None)

# Generated at 2022-06-13 07:08:06.279947
# Unit test for function parse_address

# Generated at 2022-06-13 07:08:13.704711
# Unit test for function parse_address
def test_parse_address():

    assert parse_address('192.0.2.1') == ('192.0.2.1', None)
    assert parse_address('192.0.2.1:80') == ('192.0.2.1', 80)
    assert parse_address('foo.example.com') == ('foo.example.com', None)
    assert parse_address('[fd00:dead:beef::1]') == ('fd00:dead:beef::1', None)
    assert parse_address('[fd00:dead:beef::1]:80') == ('fd00:dead:beef::1', 80)
    assert parse_address('[fd00:dead:beef::1%eth0]') == ('fd00:dead:beef::1%eth0', None)

# Generated at 2022-06-13 07:08:25.372403
# Unit test for function parse_address

# Generated at 2022-06-13 07:08:37.212847
# Unit test for function parse_address
def test_parse_address():
    from ansible.utils.network import parse_address

    # IPv4 address
    assert parse_address('127.0.0.1') == ('127.0.0.1', None)

    # IPv4 address with range
    assert parse_address('127.0.0.[1]') == ('127.0.0.[1]', None)

    # Bracketed IPv4 address with range
    assert parse_address('[127.0.0.[1]]') == ('127.0.0.[1]', None)

    # IPv6 address
    assert parse_address('::1') == ('::1', None)

    # IPv6 address with range
    assert parse_address('2001:db8::[1]') == ('2001:db8::[1]', None)

    # Bracketed IPv6 address with range
    assert parse_