

# Generated at 2022-06-14 05:39:02.104563
# Unit test for function is_url
def test_is_url():
    assert is_url('http://www.mysite.com') == True
    assert is_url('https://mysite.com') == True
    assert is_url('.mysite.com') == False


# Generated at 2022-06-14 05:39:15.492081
# Unit test for function is_url
def test_is_url():
    input_string = 'http://www.mysite.com'
    assert is_url(input_string) is True
    input_string = 'https://mysite.com'
    assert is_url(input_string) is True
    input_string = '.mysite.com'
    assert is_url(input_string) is False
    input_string = 'http://www.mysite.com'
    assert is_url(input_string, ['http']) is True
    input_string = 'http://www.mysite.com'
    assert is_url(input_string, ['https']) is False
    input_string = ''
    assert is_url(input_string) is False
    input_string = ' '
    assert is_url(input_string) is False

# Generated at 2022-06-14 05:39:20.578310
# Unit test for function is_url
def test_is_url():
    assert is_url('http://www.mysite.com') == True
    assert is_url('https://mysite.com') == True
    assert is_url('.mysite.com') == False
    assert is_url('mysite.com') == False



# Generated at 2022-06-14 05:39:23.282621
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') == True
    assert is_json('[1, 2, 3]') == True
    assert is_json('1, 2, 3') == False



# Generated at 2022-06-14 05:39:33.804015
# Unit test for function is_isbn
def test_is_isbn():
    assert is_isbn('9780312498580') == True
    assert is_isbn('1506715214') == True
    assert is_isbn('9780312498580', normalize = False) == True
    assert is_isbn('1506715214', normalize = False) == True
    assert is_isbn('978-0312498580', normalize = False) == False
    assert is_isbn('150-6715214', normalize = False) == False
    assert is_isbn('978-0312498580') == True
    assert is_isbn('150-6715214') == True

# Generated at 2022-06-14 05:39:37.760362
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_full_string('192.168.0.1')
    assert is_string('192.168.0.1')
    assert is_ip_v4('192.168.0.1')
    assert not is_ip_v4('192.168.0.256')
    return 'Unit test for is_ip_v4 passed'


# Generated at 2022-06-14 05:39:50.415920
# Unit test for function is_email
def test_is_email():
    assert is_email("my.email@the-provider.com") == True
    assert is_email("_@gmail.com") == True
    assert is_email("my-email@gmail.com") == True
    assert is_email("my.email..@gmail.com") == False
    assert is_email("-@gmail.com") == False
    assert is_email("my..email@gmail.com") == False
    assert is_email("my.email_@gmail.com") == False
    assert is_email("my.email@g.mail@gmail.com") == False
    assert is_email("my.email@gmail.com_") == False
    assert is_email("myemail@gmail.com,") == False
    assert is_email("myemail@gmailcom") == False

# Generated at 2022-06-14 05:39:54.149858
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75') == True
    assert is_ip_v4('nope') == False
    assert is_ip_v4('255.200.100.999') == False

# Generated at 2022-06-14 05:39:55.690450
# Unit test for function is_isbn
def test_is_isbn():
    assert is_isbn("978-0312498580")

# Generated at 2022-06-14 05:40:09.203360
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert not is_ip_v4(None)
    assert not is_ip_v4("")
    assert not is_ip_v4(" ")
    assert not is_ip_v4("i am not a number")
    assert not is_ip_v4("1.2.3")
    assert not is_ip_v4("1.2.3.4.5")
    assert not is_ip_v4("10.2.3.4.5")
    assert is_ip_v4("0.0.0.0")
    assert is_ip_v4("10.10.10.10")
    assert is_ip_v4("255.255.255.255")
    assert not is_ip_v4("256.0.0.0")

# Generated at 2022-06-14 05:40:16.632390
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}')
    assert is_json('[1, 2, 3]')
    assert not is_json('{nope}')


# Generated at 2022-06-14 05:40:19.286843
# Unit test for function is_ip
def test_is_ip():
    assert is_ip('255.200.100.75') == True
    assert is_ip('2001:db8:85a3:0000:0000:8a2e:370:7334') == True
    assert is_ip('1.2.3') == False



# Generated at 2022-06-14 05:40:24.803484
# Unit test for function is_ip
def test_is_ip():
    assert is_ip("127.0.0.1") == True
    assert is_ip("255.255.255.255") == True
    assert is_ip("0.0.0.0") == True
    assert is_ip("255.0.0.1") == True
    assert is_ip("192.168.1.0") == True
    assert is_ip("192.168.1.255") == True
    assert is_ip("10.10.1.1") == True
    assert is_ip("132.254.111.10") == True
    assert is_ip("26.10.2.10") == True
    assert is_ip("127.0.0.256") == False
    assert is_ip("127.0.0.0.1") == False

# Generated at 2022-06-14 05:40:29.413537
# Unit test for function is_email
def test_is_email():
    assert is_email('test@test.com') == True
    assert is_email('test@test.com.com.com') == True
    assert is_email('test@test.com ') == False
    assert is_email('test.com') == False


# Generated at 2022-06-14 05:40:43.165473
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    t1 = "1234567890"
    t2 = "123456789"
    t3 = "12345678"
    t4 = "1234567"
    t5 = "123456"
    t6 = "12345"
    t7 = "1234"
    t8 = "123"
    t9 = "12"
    t10 = "1"
    t11 = "123456789X"
    t12 = "1234567890X"
    t13 = "123456789Y"
    t14 = "123456789X0"
    t15 = "123456789X01"

    # test valid ones
    assert __ISBNChecker(t1).is_isbn_10() == True
    assert __ISBNChecker(t11).is_isbn_10

# Generated at 2022-06-14 05:40:50.543960
# Unit test for function is_credit_card
def test_is_credit_card():
    assert is_credit_card('4111111111111111') is True
    assert is_credit_card('12345678901234567') is False 
    assert is_credit_card('4111111111111111', card_type='VISA') is True
    assert is_credit_card('4111111111111111', card_type='MASTERCARD') is False
    assert is_credit_card('', card_type='VISA') is False
    assert is_credit_card(None, card_type='VISA') is False
# Unit test ends here:


# Generated at 2022-06-14 05:40:56.265558
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') is True
    assert is_json('[1, 2, 3]') is True
    assert is_json('{nope}') is False
    assert is_json(10) is False
    assert is_json(None) is False



# Generated at 2022-06-14 05:41:00.234797
# Unit test for function is_json
def test_is_json():
    assert(is_json('{"name": "Peter"}') == True)
    assert(is_json('[1, 2, 3]') == True)
    assert(is_json('{nope}') == False)
    assert(is_json('') == False)



# Generated at 2022-06-14 05:41:06.157785
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}')
    assert is_json('[1, 2, 3]')
    assert not is_json('{nope}')
    assert not is_json('[nope')
    assert not is_json('nope]')
    assert not is_json('{')
    assert not is_json(']')
    assert not is_json('')



# Generated at 2022-06-14 05:41:19.467502
# Unit test for function is_credit_card
def test_is_credit_card():
    assert is_credit_card("4111111111111111") is True
    assert is_credit_card("4111-1111-1111-1111") is True
    assert is_credit_card("4111 1111 1111 1111") is True
    assert is_credit_card("411111111111") is False
    assert is_credit_card("4111111111111112") is False
    assert is_credit_card("5105105105105100") is True
    assert is_credit_card("5105-1051-0510-5100") is True
    assert is_credit_card("5105 1051 0510 5100") is True
    assert is_credit_card("6011111111111117") is True
    assert is_credit_card("6011111111111118") is False

# Generated at 2022-06-14 05:41:35.891266
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('123.45.67.89') == True
    assert is_ip_v4('255.0.0.0') == True
    assert is_ip_v4('0.0.0.0') == True
    assert is_ip_v4('255.255.255.255') == True
    assert is_ip_v4('256.0.0.0') == False
    assert is_ip_v4('255.0.0') == False
    assert is_ip_v4('0.0.0') == False
    assert is_ip_v4('255.255.255') == False
    assert is_ip_v4('255.255.255.') == False
    assert is_ip_v4('255.255.255.256') == False
    assert is_ip_

# Generated at 2022-06-14 05:41:46.568180
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('192.168.10.15') == True
    assert is_ip_v4('0.0.0.0') == True
    assert is_ip_v4('255.0.0.0') == True
    assert is_ip_v4('255.255.255.255') == True
    assert is_ip_v4('256.255.255.255') == False
    assert is_ip_v4('255.256.255.255') == False
    assert is_ip_v4('255.255.256.255') == False
    assert is_ip_v4('255.255.255.256') == False
    assert is_ip_v4('000.000.000.000') == False
    assert is_ip_v4('255.0.1') == False
   

# Generated at 2022-06-14 05:41:58.692725
# Unit test for function is_email
def test_is_email():
    result = is_email('my.email@the-provider.com')
    assert result == True
    result = is_email('@gmail.com')
    assert result == False
    result = is_email('email@domain.net')
    assert result == True
    result = is_email('firstname.lastname@domain.com')
    assert result == True
    result = is_email('email@subdomain.domain.com')
    assert result == True
    result = is_email('firstname+lastname@domain.com')
    assert result == True
    result = is_email('email@123.123.123.123')
    assert result == True
    result = is_email('email@[123.123.123.123]')
    assert result == True

# Generated at 2022-06-14 05:42:09.884906
# Unit test for function is_email
def test_is_email():
    assert(is_email("foo@example.com") is True)
    assert(is_email("foo.bar@example.com") is True)
    assert(is_email("f.o.o.b.a.r@example.com") is True)
    assert(is_email("foo.@example.com") is False)
    assert(is_email("foo..bar@example.com") is False)
    assert(is_email("foo.bar@.example.com") is False)
    assert(is_email("foo.bar@example..com") is False)
    assert(is_email("foo.bar@example.com.") is False)
    assert(is_email("foo bar@example.com") is False)
    assert(is_email("foobar@example. com") is False)

# Generated at 2022-06-14 05:42:21.976908
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com')
    assert not is_email('.@')
    assert not is_email('my.email@')
    assert not is_email('my.email')
    assert not is_email('')
    assert not is_email(' ')
    assert is_email(r'first\@token@the-provider.com')
    assert is_email(r'my"\\"email@the-provider.com')
    assert not is_email(r'my\"email@the-provider.com')
    assert is_email(r'my\ email@the-provider.com')
    assert is_email(r'my.email@the-provider.co.uk')

# Generated at 2022-06-14 05:42:36.259739
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com') is True
    assert is_email('my.email@the-provider.com') is True
    assert is_email('my.email@the-provider.com') is True
    assert is_email('my.email@the-provider.com') is True
    assert is_email('my.email@the-provider.com') is True
    assert is_email('my.email@the-provider.com') is True
    assert is_email('my.email@the-provider.com') is True
    assert is_email('my.email@the-provider.com') is True
    assert is_email('my.email@the-provider.com') is True
    assert is_email('my.email@the-provider.com') is True

# Generated at 2022-06-14 05:42:43.949403
# Unit test for function is_json
def test_is_json():
    assert(is_json('{"name": "Peter"}'))
    assert(is_json('[1, 2, 3]'))
    assert(not is_json('{nope}'))
    assert(is_json('{"name": "peter", "age": "20"}'))
    assert(not is_json('{"name": "peter", age: "20"}'))
    assert(is_json('{"name": "peter"}'))
    return True


# Generated at 2022-06-14 05:42:46.760092
# Unit test for function is_email
def test_is_email():
    if is_email('a@a.a') != True:
        raise Exception("is_email Fail")
    else:
        print("is_email OK")

test_is_email()


# UUID format:
# xxxxxxxx-xxxx-Mxxx-Nxxx-xxxxxxxxxxxx
# where M is the version and N is the variant

# Generated at 2022-06-14 05:42:58.108059
# Unit test for function is_email
def test_is_email():
    assert is_email("test@test.com") == True
    assert is_email("test1@test.com") == True
    assert is_email("test.1@test.com") == True
    assert is_email("test_1@test.com") == True
    assert is_email("test_1@test.co.uk") == True
    assert is_email("test@test.c") == False
    assert is_email("@test.com") == False
    assert is_email("what?") == False
    assert is_email("?what") == False
    assert is_email("what") == False
    assert is_email("test.com") == False
    assert is_email("test@.com") == False
    assert is_email("@test") == False
    assert is_email("t@est.com")

# Generated at 2022-06-14 05:43:04.105815
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75')
    assert not is_ip_v4('nope')
    assert not is_ip_v4('255.200.100.999')


# Generated at 2022-06-14 05:43:17.312664
# Unit test for function is_email
def test_is_email():
    assert is_email('me.e@me.e')
    assert not is_email('me.e.me.e')
    assert not is_email('me.e@.me.e')
    assert not is_email('me.e@me.e.')
    assert not is_email('me.e@me.e.')
    assert not is_email('me.e@me..e')
    assert is_email('me\\ e@me.e')
    assert is_email('\\"me.e\\"@me.e')
    assert is_email('me&l=2@me.e')
    assert is_email('"me. e"@me.e')
    assert is_email('"me.e"@me.e')


# Generated at 2022-06-14 05:43:19.802437
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') is True  # json object
    assert is_json('[1, 2, 3]') is True  # json array
    assert is_json('{nope}') is False  # not a json
    assert is_json('') is False  # empty string always return false


# Generated at 2022-06-14 05:43:30.900657
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    """Unit test for is_isbn_10"""
    assert __ISBNChecker('0306406152').is_isbn_10()
    assert __ISBNChecker('999996319X').is_isbn_10()
    assert __ISBNChecker('9992158107').is_isbn_10()
    # check false
    assert not __ISBNChecker('03064061529').is_isbn_10()
    assert not __ISBNChecker('030640615').is_isbn_10()
    assert not __ISBNChecker('999996319').is_isbn_10()
    assert not __ISBNChecker('999215810').is_isbn_10()
    # check case insensitive
    assert __ISBNChecker('0312345678').is_isbn_10()

# Generated at 2022-06-14 05:43:35.452250
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('127.0.0.1')
    assert not is_ip_v4('127.0.0.')
  

# Generated at 2022-06-14 05:43:39.329770
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') == True
    assert is_json('[1, 2, 3]') == True
    assert is_json('{nope}') == False


# Generated at 2022-06-14 05:43:46.328643
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4(None) == False
    assert is_ip_v4('') == False
    assert is_ip_v4(' ') == False
    assert is_ip_v4('hello') == False
    assert is_ip_v4('1234') == False
    assert is_ip_v4('255.255.255.0') == True
    assert is_ip_v4('255.255.255.256') == False
    assert is_ip_v4('255.255.255.0.1') == False


# Generated at 2022-06-14 05:43:57.078382
# Unit test for function is_email
def test_is_email():
    assert is_email('me@here.com')
    assert is_email('my.email@the-provider.com')
    assert is_email('my.email@the-provider.name')
    assert is_email('my.email@the-provider.co.uk')
    assert is_email('my.email+spam@the-provider.com')
    assert is_email('my.email-spam@the-provider.com')
    assert is_email('myemail@theprovider.com')
    assert is_email('myemail@theprovider-name.com')
    assert is_email('myemail@theprovider-name.co.uk')
    assert is_email('myemail@the-provider.name')
    assert is_email('me+spam@here.com')
   

# Generated at 2022-06-14 05:44:00.695379
# Unit test for function is_email
def test_is_email():
    assert is_email('andrea_brambilla@gmail.com') == True
    assert is_email('andrea@andrea.andre') == True
    assert is_email('andrea') == False



# Generated at 2022-06-14 05:44:07.748245
# Unit test for function is_email
def test_is_email():
    assert is_email("test@test.com")
    assert not is_email("test.com")
    assert is_email("test()[]\\;:,<>@test.com")
    assert is_email("\"test.test@test.com\"@test.com")
    assert not is_email("test.test\"@test.com\"@test.com")
    assert is_email("\"test.test@test.com\"@test.com")

test_is_email()



# Generated at 2022-06-14 05:44:18.978441
# Unit test for function is_email
def test_is_email():
    assert is_email('a@b.c') is True
    assert is_email('postbox@com') is True
    assert is_email('a"b@c') is False
    assert is_email('a@b"c.c') is False
    assert is_email('"a@b"@c.c') is True
    assert is_email('"a@b"@c.com') is True
    assert is_email('a..b@gmail.com') is False
    assert is_email('a\ @b@c.com') is True
    assert is_email('a\\@b@c.com') is False
    assert is_email('a\\\@b@c.com') is False
    assert is_email('a"\\\\@b"@c.com') is True

# Generated at 2022-06-14 05:44:33.059504
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    # case 1
    checker = __ISBNChecker('0306406152')
    assert checker.is_isbn_10() == True

    # case 2
    checker = __ISBNChecker('1848000707')
    assert checker.is_isbn_10() == False

    # case 3
    checker = __ISBNChecker('1848000707z')
    assert checker.is_isbn_10() == False


# Generated at 2022-06-14 05:44:39.519803
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com') == True
    assert is_email('@gmail.com') == False
    assert is_email('hello..world@gmail.com') == False
    assert is_email('hello.world@gmail.com.') == False
    
# Test for example
test_is_email()


# Generated at 2022-06-14 05:44:45.793309
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') is True
    assert is_json('[1, 2, 3]') is True
    assert is_json('{nope}') is False
    assert is_json('[[[[[[[') is False



# Generated at 2022-06-14 05:44:56.733425
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    checker = __ISBNChecker('9780470059029')
    assert checker.is_isbn_13()
    checker = __ISBNChecker('978-0470059029')
    assert checker.is_isbn_13()
    checker = __ISBNChecker('978-0-470-059029')
    assert checker.is_isbn_13()

    checker = __ISBNChecker('9780470059029', False)
    assert not checker.is_isbn_13()
    checker = __ISBNChecker('978-0470059029', False)
    assert not checker.is_isbn_13()
    checker = __ISBNChecker('978-0-470-059029', False)
    assert not checker.is_isbn_13

# Generated at 2022-06-14 05:45:10.279544
# Unit test for function is_json
def test_is_json():
    # Test empty string
    expected = False
    actual = is_json("")
    assert actual == expected, "Test failed"

    # Test invalid JSON
    expected = False
    actual = is_json("{")
    assert actual == expected, "Test failed"

    expected = False
    actual = is_json("{}")
    assert actual == expected, "Test failed"

    # Test valid JSON
    expected = True
    actual = is_json("{\"test\": \"test\"}")
    assert actual == expected, "Test failed"

    expected = True
    actual = is_json("{\"test\":[\"test\"]}")
    assert actual == expected, "Test failed"

    expected = True
    actual = is_json("[1, 2, 3]")
    assert actual == expected, "Test failed"



# Generated at 2022-06-14 05:45:14.036868
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker('978-0-306-40615-7').is_isbn_13() == True
    assert __ISBNChecker('978-0-306-40615-6').is_isbn_13() == False

# Generated at 2022-06-14 05:45:27.134274
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    test_cases = [
        (None, False),
        ([], False),
        ({}, False),
        (False, False),
        (5, False),
        (5.6, False),
        ('', False),
        ('dfgdf', False),
        ('9783161484100', True),
        ('97831614841003', False),
        ('9783161484', False),
        ('978316148410', False),
        ('978316148410A', False),
        ('978316148410A0', False)
    ]

    for test_case in test_cases:
        try:
            assert __ISBNChecker(str(test_case[0])).is_isbn_13() == test_case[1]
        except InvalidInputError:
            assert not test_case[1]

# Generated at 2022-06-14 05:45:36.326536
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    # case 1: valid isbn-13 string
    expected = True
    actual = __ISBNChecker('9789887739526').is_isbn_13()
    assert actual == expected

    # case 2: invalid isbn-13 string
    expected = False
    actual = __ISBNChecker('9789887739527').is_isbn_13()
    assert actual == expected

    # case 3: too long isbn-13 string
    expected = False
    actual = __ISBNChecker('97898877395269').is_isbn_13()
    assert actual == expected

    # case 4: too short isbn-13 string
    expected = False
    actual = __ISBNChecker('97898877395').is_isbn_13()
    assert actual == expected



# Generated at 2022-06-14 05:45:48.239728
# Unit test for function is_email
def test_is_email():
    assert is_email("my.email@the-provider.com") == True
    assert is_email("@gmail.com") == False
    assert is_email("my email@gmail.com") == True
    assert is_email("234.567@gmail.com") == False
    assert is_email("email234@gmail.com") == True
    assert is_email("") == False
    assert is_email("   ") == False
    assert is_email("@") == False
    assert is_email("ciao@.it") == False
    assert is_email("ciao@it.") == False
    assert is_email("ciao@it.it.") == False
    assert is_email("ciao@it.it") == True
    assert is_email(".....") == False

# Generated at 2022-06-14 05:45:52.242837
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75') == True
    assert is_ip_v4('nope') == False
    assert is_ip_v4('255.200.100.999') == False
    
test_is_ip_v4()

# Generated at 2022-06-14 05:46:05.025544
# Unit test for function is_email
def test_is_email():
    assert is_email('tom@gmail.com') == True
    assert is_email('thisisatest@sc.edu') == True
    assert is_email('thisisatest@.com') == False
    assert is_email('thisisatest@') == False
    assert is_email('thisisatest') == False
    assert is_email('tom@sc..edu') == False
    assert is_email('tom@sc.edu.') == False
    assert is_email('tom@sc.edu.x') == False
    assert is_email('tom@sc.edu.') == False
    assert is_email('tom@sc..x') == False
    assert is_email('tom@sc..') == False
    assert is_email('tom@sc..x') == False



# Generated at 2022-06-14 05:46:08.635877
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com')
    assert not is_email('@gmail.com')
    assert not is_email('')
    assert not is_email('test@test')



# Generated at 2022-06-14 05:46:15.645800
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker('9780340831158').is_isbn_13()
    assert __ISBNChecker('9789768182258').is_isbn_13()
    assert not __ISBNChecker('9780340831159').is_isbn_13()
    assert not __ISBNChecker('9789768182250').is_isbn_13()

# Generated at 2022-06-14 05:46:24.991892
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker('0-7356-1967-0').is_isbn_10() == True
    assert __ISBNChecker('0-87930-832-1').is_isbn_10() == True
    assert __ISBNChecker('0-7356-1967-4').is_isbn_10() == False
    # failed when there are extra characters
    assert __ISBNChecker('0-7356-1967-0ab').is_isbn_10() == False
    # failed when there is missing character
    assert __ISBNChecker('0-7356-1967-0 ').is_isbn_10() == False
    assert __ISBNChecker('0-7356-1967-04').is_isbn_10() == False

# Generated at 2022-06-14 05:46:29.579422
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75') == True
    assert is_ip_v4('nope') == False
    assert is_ip_v4('255.200.100.999') == False


# Generated at 2022-06-14 05:46:38.207628
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com') == True
    assert is_email('@gmail.com') == False
    assert is_email('"my.dude\\ "email\\"@the-provider.com') == True
    assert is_email('my.email@the-provider.com.') == False
    assert is_email('this\ is\ not\ a\ valid\ email') == False
    assert is_email('dude@gmail.com@gmail.com') == False



# Generated at 2022-06-14 05:46:41.949560
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75')
    assert is_ip_v4('nope')
    assert is_ip_v4('255.200.100.999')

test_is_ip_v4()


# Generated at 2022-06-14 05:46:48.930037
# Unit test for function is_ip_v4
def test_is_ip_v4():
    ip = "255.200.100.75"
    assert is_ip_v4(ip) == True
    ip = "nope"
    assert is_ip_v4(ip) == False
    ip = "255.200.100.999"
    assert is_ip_v4(ip) == False


# Generated at 2022-06-14 05:46:51.927212
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker('9780751563515').is_isbn_10() is False
    assert __ISBNChecker('0751563515').is_isbn_10() is True
    assert __ISBNChecker('0751563516').is_isbn_10() is False



# Generated at 2022-06-14 05:46:55.457289
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker('0306406151').is_isbn_10() is True
    assert __ISBNChecker('0306406152').is_isbn_10() is False

# Generated at 2022-06-14 05:47:04.036064
# Unit test for function is_ip_v4
def test_is_ip_v4():
    for test_str in ['255.200.100.75', 'nope', '255.200.100.999']:
        assert is_ip_v4(test_str) == True
        
test_is_ip_v4()



# Generated at 2022-06-14 05:47:13.619699
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker('978-84-9163-111-6').is_isbn_13() == True
    assert __ISBNChecker('9788491631116').is_isbn_13() == True
    assert __ISBNChecker('8376421599').is_isbn_13() == False
    assert __ISBNChecker('9788491631111').is_isbn_13() == False
    assert __ISBNChecker(8376421599).is_isbn_13() == False
    assert __ISBNChecker(9788491631116).is_isbn_13() == False
    assert __ISBNChecker(8376421599).is_isbn_13() == False
test___ISBNChecker_is_isbn_13()

# Generated at 2022-06-14 05:47:16.999870
# Unit test for function is_json
def test_is_json():
    assert is_json("{test:test\"test\":test}") == False


# Generated at 2022-06-14 05:47:28.987828
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker('0-612-02870-X').is_isbn_10() is True
    assert __ISBNChecker('0596004427').is_isbn_10() is True
    assert __ISBNChecker('0-596-00442-7').is_isbn_10() is True
    assert __ISBNChecker('0596-004427').is_isbn_10() is True
    assert __ISBNChecker('0-596-004427').is_isbn_10() is True
    assert __ISBNChecker('0-596-0-04427').is_isbn_10() is True
    assert __ISBNChecker('0-596-004-4-2-7').is_isbn_10() is True

# Generated at 2022-06-14 05:47:42.851880
# Unit test for function is_json
def test_is_json():
    input_string = '[1,2,3]'
    assert is_json(input_string) == True
    input_string = '{"name": "asdf"}'
    assert is_json(input_string) == True
    input_string = '{}'
    assert is_json(input_string) == True
    input_string = '{"name": "asdf", "age": 32}'
    assert is_json(input_string) == True
    input_string = '{nope}'
    assert is_json(input_string) == False
    input_string = "{"
    assert is_json(input_string) == False
    input_string = "}"
    assert is_json(input_string) == False
    input_string = "["
    assert is_json(input_string) == False
   

# Generated at 2022-06-14 05:47:46.253012
# Unit test for function is_email
def test_is_email():
    assert is_email('test@test.test')
    assert is_email('test@test.test')

# Test to check if email is valid

# Generated at 2022-06-14 05:47:49.770502
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') == True
    assert is_json('[1, 2, 3]') == True
    assert is_json('{nope}') == False
# Run unit test
test_is_json()



# Generated at 2022-06-14 05:47:59.537838
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    checker_obj = __ISBNChecker('1-933988-03-7', normalize=False)
    assert checker_obj.is_isbn_10() == True
    checker_obj = __ISBNChecker('0-19-852663-6', normalize=False)
    assert checker_obj.is_isbn_10() == True
    checker_obj = __ISBNChecker('1-933988-03-9', normalize=False)
    assert checker_obj.is_isbn_10() == False

# Generated at 2022-06-14 05:48:01.773669
# Unit test for function is_email
def test_is_email():
    assert is_email("\"Abc\\@def\"@example.com") == True
test_is_email()



# Generated at 2022-06-14 05:48:04.427858
# Unit test for function is_json
def test_is_json():
    assert is_json('[1, 2, 3]')
test_is_json()



# Generated at 2022-06-14 05:48:17.621496
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}')
    assert not is_json('{"name": "Peter"}"')
    assert is_json('[1, 2, 3]')
    assert not is_json('[1, 2, 3')
    assert not is_json('{nope}')
    assert not is_json('{"name":}')



# Generated at 2022-06-14 05:48:20.866374
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com') == True
    assert is_email('@gmail.com') == False
# -----------------------------------------------------------------------------    


# Generated at 2022-06-14 05:48:29.053619
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker('9780767902870').is_isbn_13()
    assert __ISBNChecker('978-0-7679-0287-0').is_isbn_13()
    assert __ISBNChecker('978 0 7679 0287 0').is_isbn_13()
    assert __ISBNChecker('0277730027').is_isbn_13()
    assert __ISBNChecker('0277730027').is_isbn_13()
    assert __ISBNChecker('9791162190791').is_isbn_13()
