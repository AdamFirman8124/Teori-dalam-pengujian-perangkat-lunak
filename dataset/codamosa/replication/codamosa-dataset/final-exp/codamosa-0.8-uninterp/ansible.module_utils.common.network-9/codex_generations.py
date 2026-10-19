

# Generated at 2022-06-12 23:17:16.724872
# Unit test for function to_subnet
def test_to_subnet():
    assert to_subnet('192.168.1.1', '255.255.255.0') == '192.168.1.0/24'
    assert to_subnet('192.168.1.1', '24') == '192.168.1.0/24'
    assert to_subnet('192.168.1.1', 24) == '192.168.1.0/24'
    assert to_subnet('10.10.10.1', 29) == '10.10.10.0/29'
    assert to_subnet('10.10.10.1', '255.255.255.248') == '10.10.10.0/29'

# Generated at 2022-06-12 23:17:24.765727
# Unit test for function to_masklen
def test_to_masklen():
    netmask_32 = "255.255.255.255"
    netmask_30 = "255.255.255.252"
    netmask_21 = "255.255.248.0"
    netmask_0 = "0.0.0.0"
    netmask_wrong = "255.255.255.256"

    assert to_masklen(netmask_32) == 32
    assert to_masklen(netmask_30) == 30
    assert to_masklen(netmask_21) == 21
    assert to_masklen(netmask_0) == 0
    assert to_masklen(netmask_wrong) == ValueError


# Generated at 2022-06-12 23:17:27.485230
# Unit test for function to_masklen
def test_to_masklen():
    assert to_masklen('255.0.0.0') == 8
    assert to_masklen('255.255.0.0') == 16
    assert to_masklen('255.255.255.0') == 24
    assert to_masklen('255.255.254.0') == 23



# Generated at 2022-06-12 23:17:32.523027
# Unit test for function to_subnet
def test_to_subnet():
    assert to_subnet('192.168.1.1', '24') == '192.168.1.0/24'
    assert to_subnet('192.168.1.1', '255.255.255.0') == '192.168.1.0/24'
    assert to_subnet('192.168.1.1', '255.255.255.0', dotted_notation=True) == '192.168.1.0 255.255.255.0'



# Generated at 2022-06-12 23:17:43.649209
# Unit test for function to_ipv6_network
def test_to_ipv6_network():
    # Generic test
    test_addr = '2001:0db8:85a3:0000:0000:8a2e:0370:7334/64'
    test_network = to_ipv6_network(test_addr)
    assert test_network == '2001:db8:85a3::', "Generic test of to_ipv6_network() failed."

    # Zero test
    test_addr = '::/64'
    test_network = to_ipv6_network(test_addr)
    assert test_network == '::', "Zero test of to_ipv6_network() failed."

    # Compressed test
    test_addr = '2001:0db8:85a3:0:0:8a2e:0370:7334/64'
    test_network = to_ipv6_network

# Generated at 2022-06-12 23:17:51.918331
# Unit test for function to_subnet
def test_to_subnet():
    assert to_subnet('1.2.3.4', '255.255.255.0') == '1.2.3.0/24'
    assert to_subnet('1.2.3.4', '255.255.0.0') == '1.2.0.0/16'
    assert to_subnet('1.2.3.4', '255.0.0.0') == '1.0.0.0/8'
    assert to_subnet('172.16.1.1', '255.255.0.0') == '172.16.0.0/16'
    assert to_subnet('172.16.1.1', '255.255.0.0', True) == '172.16.0.0 255.255.0.0'

# Generated at 2022-06-12 23:18:03.129892
# Unit test for function is_netmask
def test_is_netmask():

    # check invalid netmask
    assert not is_netmask('255.256.255.0')
    assert not is_netmask('255.255.999.0')
    assert not is_netmask('255.255.255.256')
    assert not is_netmask('255.999.255.255')
    assert not is_netmask('255.255.999')
    assert not is_netmask('255.255.255.255.255')
    assert not is_netmask('255.255.255.1000')
    assert not is_netmask('255.255.255.1-0')
    assert not is_netmask('255.255.255.1b')

    # check valid netmasks
    assert is_netmask('255.255.255.0')

# Generated at 2022-06-12 23:18:13.350109
# Unit test for function is_netmask
def test_is_netmask():
    assert is_netmask('255.255.255.0') is True
    assert is_netmask('255.255.255.128') is True
    assert is_netmask('255.255.255.192') is True
    assert is_netmask('255.255.255.224') is True
    assert is_netmask('255.255.255.240') is True
    assert is_netmask('255.255.255.248') is True
    assert is_netmask('255.255.255.252') is True
    assert is_netmask('255.255.255.254') is True
    assert is_netmask('255.255.255.255') is True

    assert is_netmask('255.255.255') is False
    assert is_netmask('255.255') is False

# Generated at 2022-06-12 23:18:17.542226
# Unit test for function to_masklen
def test_to_masklen():
    assert to_masklen('255.0.255.0') == 16
    assert to_masklen('255.255.255.0') == 24
    assert to_masklen('255.255.252.0') == 22
    assert to_masklen('255.255.255.254') == 31
    assert to_masklen('255.255.255.255') == 32

# Generated at 2022-06-12 23:18:19.438285
# Unit test for function to_bits
def test_to_bits():
    assert to_bits('0.0.0.0') == '00000000000000000000000000000000'
    assert to_bits('255.255.255.255') == '11111111111111111111111111111111'

# Generated at 2022-06-12 23:18:29.632746
# Unit test for function is_netmask
def test_is_netmask():
    assert is_netmask('255.255.255.0')
    assert is_netmask('255.255.0.0')
    assert not is_netmask('255.255.255.0.1')
    assert not is_netmask('255.256.255.0')
    assert not is_netmask('255.255.0')
    assert not is_netmask('255.255.0.')
    assert not is_netmask('256.255.0.0')
    assert not is_netmask('255.255.0.x')
    assert not is_netmask('255.255.0.1')


# Generated at 2022-06-12 23:18:37.430368
# Unit test for function is_netmask
def test_is_netmask():
    assert is_netmask('1.1.1.1')
    assert is_netmask('255.0.255.0')
    assert is_netmask('255.128.0.0')
    assert not is_netmask('0')
    assert not is_netmask('256.0.0.0')
    assert not is_netmask('0.0.0')
    assert not is_netmask('0.0.0.0.0')
    assert not is_netmask('1.1.1.1.1')
    assert not is_netmask('1.256.1.1')
    assert not is_netmask('1.1.1')


# Generated at 2022-06-12 23:18:40.607849
# Unit test for function to_ipv6_subnet
def test_to_ipv6_subnet():

    ip = 'dead:beef::1/64'
    subnet = 'dead:beef::'

    assert to_ipv6_subnet(ip) == subnet
    assert to_ipv6_subnet(subnet) == subnet


# Generated at 2022-06-12 23:18:45.044668
# Unit test for function is_netmask
def test_is_netmask():
    assert not is_netmask(None)
    assert not is_netmask('')
    assert not is_netmask('a.b.c.d')
    assert not is_netmask('255.255.0.255')
    assert is_netmask('255.255.0.0')



# Generated at 2022-06-12 23:18:50.571982
# Unit test for function to_ipv6_subnet

# Generated at 2022-06-12 23:18:57.958069
# Unit test for function to_ipv6_subnet
def test_to_ipv6_subnet():
    assert to_ipv6_subnet("2001:0DB8:BD05:01D2:288A:1FC0:0001:10EE") == "2001:0DB8:BD05:01D2::"
    assert to_ipv6_subnet("2001:0DB8::0001:10EE") == "2001:0DB8::"
    assert to_ipv6_subnet("::") == "::"
    assert to_ipv6_subnet("2001::") == "2001::"


# Generated at 2022-06-12 23:19:06.077265
# Unit test for function to_ipv6_subnet
def test_to_ipv6_subnet():
    assert(to_ipv6_subnet("2001:0db8:85a3:0000:0000:8a2e:0370:7334") == "2001:db8:85a3::")
    assert(to_ipv6_subnet("2001:0db8:85a3:0000:0000:8a2e:0370:7334/64") == "2001:db8:85a3::")
    assert(to_ipv6_subnet("2001:0db8:85a3::8a2e:0370:7334") == "2001:db8:85a3::")
    assert(to_ipv6_subnet("2001:0db8:85a3::8a2e:0370:7334/64") == "2001:db8:85a3::")

# Generated at 2022-06-12 23:19:15.759490
# Unit test for function to_ipv6_subnet
def test_to_ipv6_subnet():
    assert to_ipv6_subnet('2001:db8:85a3::8a2e:370:7334') == '2001:db8:85a3::'
    assert to_ipv6_subnet('fe80::') == 'fe80::'
    assert to_ipv6_subnet('fe80::7334') == 'fe80::'
    assert to_ipv6_subnet('fe80::7334%eth0') == 'fe80::'
    assert to_ipv6_subnet('fc00:db8::3') == 'fc00:db8::'
    assert to_ipv6_subnet('fc00:db8::3:4') == 'fc00:db8::'
    assert to_ipv6_subnet('fc00:db8::3:4:5')

# Generated at 2022-06-12 23:19:27.714532
# Unit test for function to_ipv6_subnet
def test_to_ipv6_subnet():
    assert '2001::' == to_ipv6_subnet('2001::')
    assert '2001::' == to_ipv6_subnet('2001::1')
    assert '2001:db8::' == to_ipv6_subnet('2001:db8::1')
    assert '2001:0db8:0000:000:0000:0000:0000:0000' == to_ipv6_subnet('2001:0db8:0000:000:0000:0000:0000:0001')
    assert '2001::' == to_ipv6_subnet('2001:0db8::1')
    assert '2001:dba::' == to_ipv6_subnet('2001:dba::1')

# Generated at 2022-06-12 23:19:39.230562
# Unit test for function to_ipv6_subnet
def test_to_ipv6_subnet():

    assert to_ipv6_subnet('::1') == '::'
    assert to_ipv6_subnet('2001::1') == '2001::'
    assert to_ipv6_subnet('2001:1::1') == '2001:1::'
    assert to_ipv6_subnet('2001:1:1::1') == '2001:1:1::'

    # Used in tests/unit/network/net_facts/test_net_facts.py
    assert to_ipv6_subnet('2001::') == '2001::'
    assert to_ipv6_subnet('2001:1::') == '2001:1::'
    assert to_ipv6_subnet('2001:1:1::') == '2001:1:1::'

# Generated at 2022-06-12 23:19:41.992569
# Unit test for function is_netmask
def test_is_netmask():
    assert is_netmask('255.255.255.0')



# Generated at 2022-06-12 23:19:49.782937
# Unit test for function is_netmask
def test_is_netmask():
    '''
    Validate that valid netmask is detected
    '''
    assert is_netmask("255.255.255.0") is True
    assert is_netmask("255.255.0.0") is True
    assert is_netmask("255.0.0.0") is True
    assert is_netmask("128.0.0.0") is False  # First bit must be 1
    assert is_netmask("255.255.255.255") is True
    assert is_netmask("255.255.255.254") is True
    assert is_netmask("255.255.255.253") is True
    assert is_netmask("255.255.255.252") is False  # First bit outside the mask must be 0
    assert is_netmask("255.255.255.251") is False  # First

# Generated at 2022-06-12 23:19:54.019502
# Unit test for function is_netmask
def test_is_netmask():
    assert is_netmask('255.255.255.255')
    assert is_netmask('255.255.255.254')
    assert not is_netmask('255.255.255.256')
    assert not is_netmask('255.255.255.255.255')
    raise Exception('Test is_netmask failed')


# Generated at 2022-06-12 23:19:59.841569
# Unit test for function is_netmask
def test_is_netmask():
    assert is_netmask('255.255.255.255')
    assert is_netmask('0.0.0.0')
    assert not is_netmask('256.0.0.0')
    assert not is_netmask('255.256.0.0')
    assert not is_netmask('255.0.256.0')
    assert not is_netmask('255.0.0.256')
    assert not is_netmask('255.255.255.0.0')
    assert not is_netmask('255.255.255')
    assert not is_netmask(0)


# Generated at 2022-06-12 23:20:07.796309
# Unit test for function is_netmask
def test_is_netmask():
    assert(is_netmask('255.255.255.0'))
    assert(is_netmask('255.0.255.0'))
    assert(is_netmask('0.0.255.0'))
    assert(not is_netmask('255.255.256.0'))
    assert(not is_netmask('255.0.256.0'))
    assert(not is_netmask('0.0.256.0'))
    assert(not is_netmask('0.0.0.0.0.0'))


# Generated at 2022-06-12 23:20:08.512732
# Unit test for function is_netmask
def test_is_netmask():
    assert is_netmask('255.255.255.0') == True


# Generated at 2022-06-12 23:20:15.343656
# Unit test for function is_netmask
def test_is_netmask():
    assert is_netmask('255.255.255.0')
    assert is_netmask('255.255.255.25')
    assert is_netmask('192.168.0.0')
    assert not is_netmask('255.255.255')
    assert not is_netmask('255.255.256.0')
    assert not is_netmask('192.168.0')
    assert not is_netmask('192.168.0.1.1')
    assert not is_netmask('192.168.0.a')


# Generated at 2022-06-12 23:20:23.828181
# Unit test for function is_netmask
def test_is_netmask():
    assert is_netmask('255.255.255.0')
    assert is_netmask('255.255.0.0')
    assert is_netmask('255.0.0.0')
    assert is_netmask('255.255.255.255')
    assert not is_netmask('255.255.255.256')
    assert not is_netmask('255.255.256.0')
    assert not is_netmask('255.256.0.0')
    assert not is_netmask('266.0.0.0')



# Generated at 2022-06-12 23:20:29.770389
# Unit test for function is_netmask
def test_is_netmask():
    assert is_netmask('255.255.255.0')
    assert is_netmask('255.255.255.128')
    assert not is_netmask('255.255.255.000')
    assert not is_netmask('255.255.255.256')
    assert not is_netmask('255.255.255.255.255')


# Generated at 2022-06-12 23:20:33.401384
# Unit test for function is_netmask
def test_is_netmask():
    assert is_netmask('255.255.255.255') is True
    assert is_netmask('255.255.255.0') is True
    assert is_netmask('255.0.0.0') is True
    assert is_netmask('0.0.0.0') is True
    assert is_netmask('0.0.255.0') is True
    assert is_netmask('255.255.0.0') is True
    assert is_netmask('255.255.255.255.') is False
    assert is_netmask('.255.255.255.255') is False
    assert is_netmask('300.255.255.255') is False
    assert is_netmask('300.500.255.255') is False
    assert is_netmask('255.255.255.300') is False

# Generated at 2022-06-12 23:20:45.980940
# Unit test for function is_netmask
def test_is_netmask():
    assert is_netmask('1.1.1.1') is False
    assert is_netmask('1.1.1.255') is True
    assert is_netmask('255.255.255.255') is True
    assert is_netmask('255.255.255.254') is False
    assert is_netmask('255.255.255.0') is True
    assert is_netmask('255.255.0.0') is True
    assert is_netmask('255.0.0.0') is True
    assert is_netmask('128.0.0.0') is True
    assert is_netmask('0.0.0.0') is True



# Generated at 2022-06-12 23:20:50.801554
# Unit test for function is_netmask
def test_is_netmask():
    assert is_netmask("255.0.0.0")
    assert is_netmask("0.0.0.0")
    assert is_netmask("255.255.255.255")
    assert not is_netmask("255.255.255.256")
    assert not is_netmask("255.255.255.0.0")


# Generated at 2022-06-12 23:20:56.492545
# Unit test for function is_netmask
def test_is_netmask():
    assert is_netmask('255.255.255.0')
    assert not is_netmask('255.255.255.0.0')
    assert not is_netmask('255.255.255.0/24')
    assert not is_netmask('255.255.0')
    assert not is_netmask('255.0')
    assert not is_netmask('255.256.255.0')
    assert not is_netmask('255.255.255.254')
    assert not is_netmask('abc.abc.abc.abc')



# Generated at 2022-06-12 23:21:05.411361
# Unit test for function is_netmask
def test_is_netmask():
    assert is_netmask('255.255.255.0')
    assert not is_netmask('255.255.0')
    assert not is_netmask('256.255.255.255')
    assert not is_netmask('255.255.255.256')
    assert not is_netmask('255.255.255.255.0')
    assert not is_netmask('255.255.255.0.0')
    assert is_netmask('255.128.0.0')
    assert not is_netmask('255.128.0')
    assert not is_netmask('255.128')



# Generated at 2022-06-12 23:21:12.151724
# Unit test for function is_netmask
def test_is_netmask():
    assert is_netmask('255.255.255.252') == True
    assert is_netmask('255.255.255.255') == True
    assert is_netmask('255.255.255.0') == True
    assert is_netmask('255.255.255.255.0') == False
    assert is_netmask('255.255.255.256') == False
    assert is_netmask('255.255.255.abc') == False
    assert is_netmask('255.255.255.300') == False



# Generated at 2022-06-12 23:21:17.166046
# Unit test for function is_netmask
def test_is_netmask():
    assert is_netmask('255.255.255.0')
    assert is_netmask('255.255.0.0')
    assert is_netmask('255.0.0.0')
    assert is_netmask('0.0.0.0')
    assert not is_netmask('255.255.0')
    assert not is_netmask('255.255.0.0.0')
    assert not is_netmask('0.0.0.0.0')


# Generated at 2022-06-12 23:21:26.476045
# Unit test for function is_netmask
def test_is_netmask():
    assert is_netmask(u'255.255.255.0')
    assert is_netmask(u'255.255.0.0')
    assert is_netmask(u'255.0.0.0')
    assert not is_netmask(u'255.255.255.0.')
    assert not is_netmask(u'255.255.255')
    assert not is_netmask(u'255.255.255.0.0.0.0')
    assert not is_netmask(u'255.255.256.0')
    assert not is_netmask(u'255.255.255.0/24')



# Generated at 2022-06-12 23:21:37.177873
# Unit test for function is_netmask
def test_is_netmask():
    assert(is_netmask('255.255.255.0'))
    assert(is_netmask('255.255.255.128'))
    assert(is_netmask('255.255.255.252'))
    assert(not is_netmask('255.255.255.254'))
    assert(not is_netmask('255.255.255.253'))
    assert(not is_netmask('255.255.255.255'))
    assert(not is_netmask('255.255.255.256'))
    assert(not is_netmask('255.255.255'))
    assert(not is_netmask('255.255.255.0.0'))
    assert(not is_netmask('255.255.255.00'))


# Generated at 2022-06-12 23:21:48.367714
# Unit test for function is_netmask
def test_is_netmask():
    assert is_netmask('255.255.255.0')
    assert is_netmask('255.255.0.0')
    assert is_netmask('255.0.0.0')
    assert is_netmask('255.255.255.128')
    assert is_netmask('255.255.255.192')
    assert is_netmask('255.255.255.224')
    assert is_netmask('255.255.255.240')
    assert is_netmask('255.255.255.248')
    assert is_netmask('255.255.255.252')
    assert is_netmask('255.255.255.254')
    assert is_netmask('128.0.0.0')
    assert is_netmask('192.0.0.0')

# Generated at 2022-06-12 23:21:58.933953
# Unit test for function is_netmask
def test_is_netmask():
    assert is_netmask('255.255.255.0') is True
    assert is_netmask('255.255.0.0') is True
    assert is_netmask('255.0.0.0') is True
    assert is_netmask('255.255.255.192') is True
    assert is_netmask('255.255.255.255') is True
    assert is_netmask('255.255.255.256') is False
    assert is_netmask('255.255.255.511') is False
    assert is_netmask('255.255.255.512') is False
    assert is_netmask('255.255.255.00') is False
    assert is_netmask('255.255.255.001') is False
    assert is_netmask('255.255.255.002') is False
   

# Generated at 2022-06-12 23:22:12.240755
# Unit test for function is_netmask
def test_is_netmask():
    if not is_netmask('255.255.255.0'):
        raise ValueError('is_netmask failed for 255.255.255.0')
    try:
        is_netmask('255.255.255.0.0')
        raise ValueError('is_netmask failed for 255.255.255.0.0')
    except ValueError:
        pass
    try:
        is_netmask('255.255.255')
        raise ValueError('is_netmask failed for 255.255.255')
    except ValueError:
        pass
    try:
        is_netmask('255.255.255.0/24')
        raise ValueError('is_netmask failed for 255.255.255.0/24')
    except ValueError:
        pass

# Generated at 2022-06-12 23:22:21.702073
# Unit test for function is_netmask

# Generated at 2022-06-12 23:22:22.965148
# Unit test for function is_netmask
def test_is_netmask():
    assert is_netmask('255.255.255.0')



# Generated at 2022-06-12 23:22:27.128120
# Unit test for function is_netmask
def test_is_netmask():
    assert is_netmask('255.255.255.0')
    assert is_netmask('255.255.255.128')
    assert not is_netmask('255.255.256.0')
    assert not is_netmask('255.255.255.0.0')
    assert not is_netmask('255.255.255.0.01')
    assert not is_netmask('')


# Generated at 2022-06-12 23:22:35.341364
# Unit test for function is_netmask
def test_is_netmask():
    assert is_netmask('255.255.255.0')
    assert is_netmask('255.255.255.128')
    assert is_netmask('255.255.255.192')
    assert is_netmask('255.255.255.224')
    assert is_netmask('255.255.255.240')
    assert is_netmask('255.255.255.248')
    assert is_netmask('255.255.255.252')
    assert is_netmask('255.255.255.254')
    assert is_netmask('255.255.255.255')

    assert not is_netmask('255.255.256.255')
    assert not is_netmask('255.255.255')
    assert not is_netmask('1234')
    assert not is_netmask('')


# Generated at 2022-06-12 23:22:45.024746
# Unit test for function is_netmask
def test_is_netmask():
    assert is_netmask('255.255.255.255')
    assert is_netmask('255.255.255.0')
    assert is_netmask('255.255.255.1')
    assert is_netmask('255.255.0.0')
    assert is_netmask('255.255.128.0')
    assert is_netmask('255.255.192.0')
    assert is_netmask('255.0.0.0')
    assert is_netmask('255.128.0.0')
    assert is_netmask('255.192.0.0')
    assert is_netmask('255.224.0.0')
    assert is_netmask('255.240.0.0')
    assert is_netmask('255.248.0.0')

# Generated at 2022-06-12 23:22:53.497893
# Unit test for function is_netmask
def test_is_netmask():
    """ Unit test for function is_netmask """
    valid_netmasks = ['255.255.255.0', '255.255.0.0', '255.0.0.0', '128.0.0.0', '0.0.0.0']
    invalid_netmasks = ['0.0.0', '0.0.0.0.0', '255.256.255.0', '255.0.0.255']

    for netmask in valid_netmasks:
        assert is_netmask(netmask)

    for netmask in invalid_netmasks:
        assert not is_netmask(netmask)



# Generated at 2022-06-12 23:23:01.106190
# Unit test for function is_netmask
def test_is_netmask():
    """
    Test is_netmask function
    """
    assert(is_netmask('1.1.1.1'))
    assert(not is_netmask('1.1.1.1.1'))
    assert(not is_netmask('1.1.1.1/24'))
    assert(not is_netmask('255.255.255.0/24'))
    assert(is_netmask('255.255.255.0'))
    assert(is_netmask('255.255.254.0'))
    assert(not is_netmask('255.255.254.1'))
    assert(not is_netmask('255.255.255.1'))
    assert(not is_netmask('255.255.254.256'))


# Generated at 2022-06-12 23:23:05.892475
# Unit test for function is_netmask
def test_is_netmask():
    assert is_netmask('255.255.255.0') == True
    assert is_netmask('255.255.0.0') == True
    assert is_netmask('255.0.0.0') == True
    assert is_netmask('0.0.0.0') == True
    assert is_netmask('255.255.255.254') == True
    assert is_netmask('255.255.255.255') == True
    assert is_netmask('255.255.255.256') == False
    assert is_netmask('255.255.255.259') == False
    assert is_netmask('255.0.0.1') == False
    assert is_netmask('255.255.0') == False
    assert is_netmask('255.255.0.0/24') == False



# Generated at 2022-06-12 23:23:15.391052
# Unit test for function is_netmask
def test_is_netmask():
    assert is_netmask('255.255.255.0') is True
    assert is_netmask('255.255.0.0') is True
    assert is_netmask('255.240.0.0') is True
    assert is_netmask('255.252.0.0') is True
    assert is_netmask('255.248.0.0') is True
    assert is_netmask('255.255.255.128') is True
    assert is_netmask('255.255.255.192') is True
    assert is_netmask('255.255.255.224') is True
    assert is_netmask('255.255.255.240') is True
    assert is_netmask('255.255.255.248') is True
    assert is_netmask('255.255.255.252') is True
   

# Generated at 2022-06-12 23:23:28.470050
# Unit test for function is_netmask
def test_is_netmask():
    assert is_netmask('255.255.255.0')
    assert not is_netmask('255.255.255.0123')
    assert not is_netmask('255.255.255')


# Generated at 2022-06-12 23:23:36.065228
# Unit test for function is_netmask
def test_is_netmask():
    assert is_netmask('255.255.255.0')
    assert is_netmask('255.255.0.0')
    assert is_netmask('255.0.0.0')
    assert not is_netmask('255.255.255.255')
    assert not is_netmask('255.255.255.256')
    assert not is_netmask('255.255.255.256')
    assert not is_netmask('255.255.0')
    assert not is_netmask('255.255.0.0.0')
    assert not is_netmask('255.255.0.0.255')



# Generated at 2022-06-12 23:23:39.530671
# Unit test for function is_netmask
def test_is_netmask():
    assert is_netmask('255.255.255.0')
    assert is_netmask('0.0.0.255')
    assert not is_netmask('255.255.255.255.0')
    assert not is_netmask('255.255.255.300')
    assert not is_netmask('255.255.255.3x')



# Generated at 2022-06-12 23:23:44.995168
# Unit test for function is_netmask
def test_is_netmask():
    assert(is_netmask('0.0.0.0') == True)
    assert(is_netmask('255.255.255.255') == True)
    assert(is_netmask('255.255.255.256') == False)
    assert(is_netmask('255.255.255') == False)
    assert(is_netmask('255.256.255.255') == False)
    assert(is_netmask('255.255.255255') == False)


# Generated at 2022-06-12 23:23:50.525817
# Unit test for function is_netmask
def test_is_netmask():
    assert is_netmask('255.255.255.0')
    assert is_netmask('255.0.0.0')
    assert not is_netmask('255.0.0.255')
    assert not is_netmask('255.255.255.0.1')



# Generated at 2022-06-12 23:23:52.283704
# Unit test for function is_netmask
def test_is_netmask():
    netmask = "255.255.255.0"
    assert is_netmask(netmask)


# Generated at 2022-06-12 23:24:02.636778
# Unit test for function is_netmask
def test_is_netmask():
    assert is_netmask('255.255.255.0')
    assert not is_netmask('255.255.255.128')
    assert not is_netmask('255.255.255.256')
    assert is_netmask('255.255.255.252')
    assert not is_netmask('255.255.255.0.0')
    assert not is_netmask('255.255.255')
    assert not is_netmask('255.255.255.256.255')
    assert not is_netmask('255.255.255.567')
    assert not is_netmask('255.255.255.567.456')
    assert not is_netmask('255.255.255. 567')
    assert not is_netmask('255.255.255. 567.456')

# Generated at 2022-06-12 23:24:09.940517
# Unit test for function is_netmask
def test_is_netmask():
    assert is_netmask('255.255.255.0')
    assert is_netmask('255.255.255.254')
    assert is_netmask('255.255.0.0')
    assert is_netmask('255.0.0.0')
    assert not is_netmask('256.255.255.0')
    assert not is_netmask('255.256.255.0')
    assert not is_netmask('255.255.256.0')
    assert not is_netmask('255.255.255.256')
    assert not is_netmask('255.255.255.0.0')
    assert not is_netmask('255.255.255.0/24')
    assert not is_netmask('255.255.255')



# Generated at 2022-06-12 23:24:14.088177
# Unit test for function is_netmask
def test_is_netmask():
    assert is_netmask('255.0.0.0')
    assert is_netmask('255.255.0.0')
    assert not is_netmask('256.255.0.0')
    assert not is_netmask('255.255.0.0.0')


# Generated at 2022-06-12 23:24:17.293787
# Unit test for function is_netmask
def test_is_netmask():
    assert is_netmask("255.255.255.0")
    assert is_netmask("255.255.255.255")
    assert is_netmask("128.128.128.128")

    assert not is_netmask("255.255.255.0.0")
    assert not is_netmask("255.255.256.0")
    assert not is_netmask("255.255.255.0/24")
    assert not is_netmask("255.255.255")
    assert not is_netmask("128.128.128.128.128")


# Generated at 2022-06-12 23:24:32.131173
# Unit test for function is_netmask
def test_is_netmask():
    assert is_netmask('255.255.255.0') == True
    assert is_netmask('255.0.255.0') == True
    assert is_netmask('255.255.255.256') == False
    assert is_netmask('255.255.256.0') == False
    assert is_netmask('255.0.0') == False
    assert is_netmask('255.0.0.0.0') == False
    assert is_netmask('255.0.0.0.0.0') == False


# Generated at 2022-06-12 23:24:36.981403
# Unit test for function is_netmask
def test_is_netmask():
    assert is_netmask('255.255.255.0')
    assert not is_netmask('255.255.255.0.1')
    assert is_netmask('255.254.253.0')
    assert not is_netmask('255.254.253.257')



# Generated at 2022-06-12 23:24:46.324751
# Unit test for function is_netmask
def test_is_netmask():
    assert(is_netmask('255.255.254.0') == True)
    assert(is_netmask('255.255.255.0') == True)
    assert(is_netmask('255.255.255.255') == True)
    assert(is_netmask('255.255.254.255') == True)
    assert(is_netmask('255.255.255.254') == False)
    assert(is_netmask('255.255.255.256') == False)
    assert(is_netmask('255.255.255') == False)
    assert(is_netmask('255.255.255.255.255') == False)
    assert(is_netmask('') == False)
    assert(is_netmask(256) == False)

# Generated at 2022-06-12 23:24:58.269938
# Unit test for function is_netmask
def test_is_netmask():
    netmasks = ['255.0.0.0', '255.128.0.0', '255.255.0.0', '255.255.128.0',
                '255.255.255.0', '255.255.255.128', '255.255.255.192',
                '255.255.255.224', '255.255.255.240', '255.255.255.248',
                '255.255.255.252', '255.255.255.254', '255.255.255.255']

# Generated at 2022-06-12 23:25:02.815929
# Unit test for function is_netmask
def test_is_netmask():
    for i in range(0,256):
        if i not in [128,192,224,240,248,252,254,255]:
            print('%3d : %r' % (i, i in VALID_MASKS))


# Generated at 2022-06-12 23:25:10.290836
# Unit test for function is_netmask
def test_is_netmask():
    assert is_netmask('255.255.255.0') is True
    assert is_netmask('255.255.255.255') is True
    assert is_netmask('255.255.255.256') is False
    assert is_netmask('255.255.255.') is False
    assert is_netmask('255.255.255.0.0') is False
    assert is_netmask('255.0.255.0') is True
    assert is_netmask('0.0.0.0') is True



# Generated at 2022-06-12 23:25:21.420333
# Unit test for function is_netmask
def test_is_netmask():
    assert not is_netmask('255.0')
    assert not is_netmask('255.0.0.0.0')
    assert not is_netmask('255.0.0.0.0.0')
    assert not is_netmask('255.0.0.0.')
    assert not is_netmask('255.0.0.0.0.')
    assert not is_netmask('.255.0.0.0')
    assert not is_netmask('.255.0.0.0.0')
    assert not is_netmask('255.255.255.0.0')
    assert not is_netmask('255.255.255.255.0')
    assert not is_netmask('255.255.255.255.255')

# Generated at 2022-06-12 23:25:32.447856
# Unit test for function is_netmask
def test_is_netmask():
    assert is_netmask('255.255.255.252')
    assert is_netmask('255.255.255.0')
    assert is_netmask('255.255.255.128')
    assert is_netmask('255.255.255.255')
    assert not is_netmask('255.255.255.254')
    assert not is_netmask('255.255.255.256')
    assert not is_netmask('255.255.256.255')
    assert not is_netmask('255.256.255.255')
    assert not is_netmask('256.255.255.255')
    assert not is_netmask('123.123.123')
    assert not is_netmask('123.123.123.123.123')
    assert not is_netmask('foo')



# Generated at 2022-06-12 23:25:40.836605
# Unit test for function is_netmask
def test_is_netmask():
    assert is_netmask('255.255.255.0') == True
    assert is_netmask('255.240.255.0') == True
    assert is_netmask('255.255.255.255') == True
    assert is_netmask('255.255.255.254') == True
    assert is_netmask('255.255.255.253') == True
    assert is_netmask('255.255.255.252') == True
    assert is_netmask('255.255.255.251') == True
    assert is_netmask('255.255.255.250') == True
    assert is_netmask('255.255.255.249') == True
    assert is_netmask('255.255.255.248') == True
    assert is_netmask('255.255.255.240') == True
   

# Generated at 2022-06-12 23:25:44.365116
# Unit test for function is_netmask
def test_is_netmask():
    assert not is_netmask(0)
    assert not is_netmask(1)
    assert not is_netmask(4)
    assert not is_netmask(8)
    assert is_netmask(16)
    assert is_netmask(17)
    assert is_netmask(32)
    assert not is_netmask(33)



# Generated at 2022-06-12 23:26:12.007390
# Unit test for function is_netmask
def test_is_netmask():
    assert is_netmask('255.255.255.0') == True
    assert is_netmask('128.0.0.0') == True
    assert is_netmask('255.224.0.0') == True
    assert is_netmask('0.0.0.0') == True
    assert is_netmask('0.255.255.255') == True
    assert is_netmask('255.255.255.255') == True
    assert is_netmask('255.255.224.255') == False
    assert is_netmask('256.255.255.255') == False
    assert is_netmask('255..255.255') == False
    assert is_netmask('255.255.255') == False
    assert is_netmask('255.255.255.255.255') == False

# Unit

# Generated at 2022-06-12 23:26:15.280159
# Unit test for function is_netmask
def test_is_netmask():
    assert is_netmask('255.255.255.192')
    assert not is_netmask('255.255.255.aa')
    assert not is_netmask('255.255.255')



# Generated at 2022-06-12 23:26:20.403734
# Unit test for function is_netmask
def test_is_netmask():
    try:
        assert is_netmask('255.255.255.0')
        assert is_netmask('255.255.255.240')
        assert not is_netmask('255.255.255.255.255')
        assert not is_netmask('255.255.255.255')
        assert not is_netmask('255.255.255.265')
    except AssertionError as e:
        raise AssertionError(e)



# Generated at 2022-06-12 23:26:25.399995
# Unit test for function is_netmask
def test_is_netmask():
    assert is_netmask('255.255.255.0')
    assert is_netmask('255.255.255.128')
    assert is_netmask('255.255.255.255')
    assert not is_netmask('0.0.0.0')
    assert not is_netmask('255.255.256.0')



# Generated at 2022-06-12 23:26:36.290814
# Unit test for function is_netmask
def test_is_netmask():
    assert is_netmask("0.0.0.0")
    assert is_netmask("255.255.255.255")
    assert is_netmask("255.255.0.0")
    assert is_netmask("255.0.0.0")
    assert is_netmask("255.255.255.0")
    assert is_netmask("128.0.0.0")
    assert is_netmask("254.0.0.0")
    assert not is_netmask("0.0.0.1")
    assert not is_netmask("255.255.255.128")
    assert not is_netmask("1.1.255.255")
    assert not is_netmask("192.168.0.1")
    assert not is_netmask("255.0.0.01")

# Generated at 2022-06-12 23:26:40.599883
# Unit test for function is_netmask
def test_is_netmask():
    assert is_netmask('255.255.255.0')
    assert is_netmask('255.255.255.128')
    assert not is_netmask('255.255.255')
    assert not is_netmask('255.255.255.256')
    assert not is_netmask('255.255.255.1.1')
    assert not is_netmask('255.255.255.1a')



# Generated at 2022-06-12 23:26:45.310784
# Unit test for function is_netmask
def test_is_netmask():
    assert is_netmask('255.255.255.255')
    assert is_netmask('255.255.255.128')
    assert is_netmask('255.255.255.0')
    assert is_netmask('255.255.0.0')
    assert is_netmask('255.0.0.0')
    assert is_netmask('128.0.0.0')
    assert is_netmask('0.0.0.0')
    assert not is_netmask('255.255.256.0')
    assert not is_netmask('255.255.255.0.0')
    assert not is_netmask('255.255')


# Generated at 2022-06-12 23:26:50.786340
# Unit test for function is_netmask
def test_is_netmask():

    assert is_netmask('255.255.255.0')
    assert is_netmask('255.255.0.0')
    assert is_netmask('255.0.0.0')
    assert is_netmask('0.0.0.0')

    assert not is_netmask('255.0.0.255')
    assert not is_netmask('255.255.0')
    assert not is_netmask('')
    assert not is_netmask('something invalid')



# Generated at 2022-06-12 23:26:51.958616
# Unit test for function is_netmask
def test_is_netmask():
    assert(is_netmask('255.255.255.0') is True)


# Generated at 2022-06-12 23:27:00.667951
# Unit test for function is_netmask
def test_is_netmask():
    assert is_netmask('255.255.255.0') is True
    assert is_netmask('255.255.255.255') is True
    assert is_netmask('255.255.255.254') is True
    assert is_netmask('255.255.255.1') is True
    assert is_netmask('255.255.255.128') is True
    assert is_netmask('255.255.255.2') is True
    assert is_netmask('255.255.255.10') is True
    assert is_netmask('255.255.255.200') is False
    assert is_netmask('255.255.255.256') is False
    assert is_netmask('255.255') is False
    assert is_netmask('255.255.255.0.0') is False


# Unit