

# Generated at 2022-06-14 05:38:48.533213
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}')
    assert is_json('[1, 2, 3]')
    assert not is_json('{nope}')
test_is_json()


# Generated at 2022-06-14 05:38:59.291016
# Unit test for function is_isbn
def test_is_isbn():
    assert is_isbn('123456789x')
    assert is_isbn('123-456789x')
    assert is_isbn('123.456789x')
    assert is_isbn('123-456-789x')
    assert is_isbn('0-306-40615-2')
    assert is_isbn('1-930110-91-2')
    assert is_isbn('978-0312498580')
    assert is_isbn('978-0-312-498580')
    assert is_isbn('978-3-12-498580-5')
    assert is_isbn('978.3.12.498580.5')
    assert is_isbn('ISBN 978-4-06-206438-9')

# Generated at 2022-06-14 05:39:01.880823
# Unit test for function is_url
def test_is_url():
    assert is_url('http://www.mysite.com') == True
    assert is_url('https://mysite.com') == True
    assert is_url('mysite.com') == False


# Generated at 2022-06-14 05:39:15.589984
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert not is_ip_v4(None)
    assert not is_ip_v4('')
    assert not is_ip_v4('a.b.c.d')
    assert not is_ip_v4('10.0.a.0')
    assert not is_ip_v4('10.0.0.300')
    assert not is_ip_v4('10.0.0')
    assert not is_ip_v4('10.0.0.0.0')
    assert not is_ip_v4('1.0.0.a')
    assert is_ip_v4('10.0.0.0')
    assert is_ip_v4('127.0.0.1')
    assert is_ip_v4('255.255.255.255')
    assert is_ip

# Generated at 2022-06-14 05:39:24.174887
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.255.255.255')
    assert not is_ip_v4('999.999.999.999')
    assert not is_ip_v4('255.255.255.255.')
    assert not is_ip_v4('255.255.255')
    assert not is_ip_v4('255.255.255.256')
    assert not is_ip_v4('255.255.255.x')
    assert not is_ip_v4('255.255.255.2x5')
    assert not is_ip_v4(None)

# Generated at 2022-06-14 05:39:25.753621
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@gmail.com') == True


# Generated at 2022-06-14 05:39:35.464243
# Unit test for function is_json
def test_is_json():
    assert is_json(' {}') == True
    assert is_json(' { "name" : "Peter"}') == True
    assert is_json(' {"name" : "Peter"}') == True
    assert is_json('{ "name": "Peter" }') == True
    assert is_json(' {"name": "Peter"}') == True
    assert is_json('{"name": "Peter"}') == True
    assert is_json('{"Key": "Value"}') == True
    assert is_json('{"Key": 12.3}') == True
    assert is_json('{"Key": 12.3}') == True
    assert is_json('{"Key": [12, 15, 18]}') == True
    assert is_json('{"Key": [12, 15, 18]}') == True
    assert is_json('{name: "Peter"}')

# Generated at 2022-06-14 05:39:43.031055
# Unit test for function is_ip_v4
def test_is_ip_v4():
    for ip in ['0.0.0.0', '127.0.0.1', '255.255.255.255']:
        assert is_ip_v4(ip)
    assert is_ip_v4('172.16.0.0')
    assert not is_ip_v4('172.32.0.0')



# Generated at 2022-06-14 05:39:45.696565
# Unit test for function is_json
def test_is_json():
    result=is_json('[1,2,3]')
    assert result==True
test_is_json()



# Generated at 2022-06-14 05:39:48.084516
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') == True
    assert is_json('[1, 2, 3]') == True
    assert is_json('{nope}') == False

# Generated at 2022-06-14 05:40:01.710547
# Unit test for function is_ip
def test_is_ip():
    assert is_ip('255.200.100.75') 
    assert is_ip('2001:db8:85a3:0000:0000:8a2e:370:7334')
    assert is_ip('1.2.3')
test_is_ip()


# Generated at 2022-06-14 05:40:11.769033
# Unit test for function is_email
def test_is_email():
    assert is_email("a@a.com")==True
    assert is_email("a@a.com.cn")==True
    assert is_email("a.a@a.com.cn")==True
    assert is_email("a.a@a_a.com.cn")==True
    assert is_email("a+a@a_a.com.cn")==True
    assert is_email("a_a@a_a.com.cn")==True
    assert is_email("a-a@a_a.com.cn")==True


# Generated at 2022-06-14 05:40:16.492579
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    checker = __ISBNChecker('0306406152')
    print(checker.is_isbn_10())
    assert checker.is_isbn_10() == True

# Generated at 2022-06-14 05:40:22.970381
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com')
    assert is_email('"my email"@the-provider.com')
    assert not is_email('@gmail.com')
    assert not is_email('my.email@')
    assert not is_email('@')
    assert not is_email('')
    assert not is_email(None)

# Generated at 2022-06-14 05:40:34.695065
# Unit test for function is_email
def test_is_email():
    assert is_email('foo@bar.com')
    assert not is_email('foo@bar')
    assert not is_email('foo.bar.com')
    # we accept "explicit" email addresses, like <foo@bar.com>
    assert is_email('<foo@bar.com>')
    # escaped spaces are ok
    assert is_email('"foo bar"@bar.com')
    assert is_email('"foo@bar"@bar.com')
    # quoted texts are ok
    assert is_email('"foo bar"@bar.com')
    assert is_email('"foo\\@bar"@bar.com')
    # however the head cannot start with a dot
    assert not is_email('.foo@bar.com')
    # border line cases

# Generated at 2022-06-14 05:40:36.857001
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    checker = __ISBNChecker("")
    assert checker.is_isbn_10() is False


# Generated at 2022-06-14 05:40:39.958678
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    # input_string, expected output
    test_data = [
        ('0385514239', True),
        ('0385514236', False),
    ]

    for string, expected in test_data:
        checker = __ISBNChecker(string)
        output = checker.is_isbn_10()
        assert output == expected


# Generated at 2022-06-14 05:40:51.502346
# Unit test for function is_ip
def test_is_ip():
    assert is_ip('255.200.100.75') == True
    assert is_ip('2001:db8:85a3:0000:0000:8a2e:370:7334') == True
    assert is_ip('1.2.3.4') == True
    assert is_ip('2001:db8:85a3:0:0:8a2e:370:7334') == True
    assert is_ip('2001:db8:85a3::8a2e:370:7334') == True
    assert is_ip('2001:db8:85a3::8a2e:370:7334::') == False
    assert is_ip('2607:f8b0:400a:808::200e') == True

# Generated at 2022-06-14 05:41:02.363882
# Unit test for function is_credit_card
def test_is_credit_card():
    assert is_credit_card(input_string = '378282246310005') # American Express
    assert is_credit_card(input_string = '371449637543151') # American Express
    assert is_credit_card(input_string = '371449635398431') # American Express
    assert is_credit_card(input_string = '5555555555554444') # MasterCard
    assert is_credit_card(input_string = '5105105105105100') # MasterCard
    assert is_credit_card(input_string = '4111111111111111') # VISA
    assert is_credit_card(input_string = '4012888888881881') # VISA
    assert is_credit_card(input_string = '4222222222222') # VISA
    


# Generated at 2022-06-14 05:41:17.178224
# Unit test for function is_credit_card
def test_is_credit_card():
    assert is_credit_card('4929435258435678', 'VISA') == True
    assert is_credit_card('4929435258435678', 'MASTERCARD') == False
    assert is_credit_card('4929435258435678', 'AMERICAN_EXPRESS') == False
    assert is_credit_card('4929435258435678', 'DINERS_CLUB') == False
    assert is_credit_card('4929435258435678', 'DISCOVER') == False
    assert is_credit_card('4929435258435678', 'JCB') == False
    assert is_credit_card('4929435258435678', 'INVALID_CARD') == False
    
    assert is_credit_card('4929435258435678') == True

# Generated at 2022-06-14 05:41:26.579920
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    checker = __ISBNChecker(input_string='0306406152')

    assert checker.is_isbn_10() is True
    assert checker.is_isbn_13() is False


# Generated at 2022-06-14 05:41:31.547996
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    checker = __ISBNChecker('978-0-306-40615-7')
    assert checker.is_isbn_13() == True

    checker = __ISBNChecker('978-0-306-40615-8')
    assert checker.is_isbn_13() == False


# Generated at 2022-06-14 05:41:43.388878
# Unit test for function is_url
def test_is_url():
    assert is_url('http://www.mysite.com')
    assert is_url('https://mysite.com')
    assert is_url('.mysite.com') is False
    assert is_url('http://www.mysite.com/path/file.ext', allowed_schemes=['http'])
    assert is_url('http://www.mysite.com/path/file.ext', allowed_schemes=['https']) is False
    assert is_url('https://www.mysite.com/path/file.ext', allowed_schemes=['http', 'https'])
    assert is_url('https://www.mysite.com/path/file.ext', allowed_schemes=['ftp', 'ssh']) is False

# Generated at 2022-06-14 05:41:56.116134
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker('1887983593').is_isbn_10()
    assert not __ISBNChecker('1887983592').is_isbn_10()
    assert __ISBNChecker('978020083743').is_isbn_10()
    assert not __ISBNChecker('978020083744').is_isbn_10()
    assert __ISBNChecker('9791162240335').is_isbn_10()
    assert not __ISBNChecker('9791162240336').is_isbn_10()
    assert not __ISBNChecker('3453452083').is_isbn_10()  # not a valid array
    assert not __ISBNChecker('A345345208').is_isbn_10()  # not a valid array
    assert not __ISBNChecker

# Generated at 2022-06-14 05:41:58.887731
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    test = __ISBNChecker('978-0-306-40615-7')
    expected = test.is_isbn_13()
    actual = True
    assert_equals(expected, actual)



# Generated at 2022-06-14 05:42:00.841137
# Unit test for function is_url
def test_is_url():
    assert is_url('.mysite.com') == True


# Generated at 2022-06-14 05:42:10.980520
# Unit test for function is_url
def test_is_url():
    assert is_url('http://www.mysite.com')
    assert is_url('https://mysite.com')
    assert is_url('.mysite.com') == False
    assert is_url('http://www.mysite.com:80/foo?bar')
    assert is_url('http://www.my-site.com:80/foo?bar')
    assert is_url('http://12.34.56.78:80/foo?bar')
    assert is_url('http://12.34.56.foo/foo?bar') == False
    assert is_url('abc://www.mysite.com:80/foo?bar') == False
    assert is_url('mysite.com') == False
    assert is_url('http://mysite.com')

# Generated at 2022-06-14 05:42:16.129194
# Unit test for function is_url
def test_is_url():
    print(is_url('http://www.mysite.com')) # returns true
    print(is_url('https://mysite.com')) # returns true
    print(is_url('.mysite.com')) # returns false


# Generated at 2022-06-14 05:42:19.628455
# Unit test for function is_url
def test_is_url():
    assert is_url('http://www.mysite.com')
    assert is_url('https://mysite.com')
    assert not is_url('.mysite.com')
# test_is_url()



# Generated at 2022-06-14 05:42:22.877598
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75')
    assert not is_ip_v4('nope')
    assert not is_ip_v4('255.200.100.999')

# Generated at 2022-06-14 05:42:32.601300
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') == True
    assert is_json('[1, 2, 3]')             == True
    assert is_json('{nope}')                == False


# Generated at 2022-06-14 05:42:42.214163
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker("").is_isbn_10() == False
    assert __ISBNChecker("0").is_isbn_10() == False
    assert __ISBNChecker("0123456789").is_isbn_10() == True
    assert __ISBNChecker("01234567890").is_isbn_10() == False
    assert __ISBNChecker("012345678a").is_isbn_10() == False
    assert __ISBNChecker("012345678k").is_isbn_10() == False
    assert __ISBNChecker("0123456780").is_isbn_10() == True
    assert __ISBNChecker("01234567891").is_isbn_10() == False

# Generated at 2022-06-14 05:42:55.314165
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    test_cases = [
        {
            'input_string': '',
            'output': False,
        },
        {
            'input_string': '978-0-306-40615-7',
            'output': True,
        },
        {
            'input_string': '978-0-306-40615-8',
            'output': False,
        },
        {
            'input_string': '978-0-306-40615-3',
            'output': False,
        },
        {
            'input_string': '978-0-306-40615-1',
            'output': False,
        },
        {
            'input_string': '978-0-306-40615-9',
            'output': False,
        },
    ]


# Generated at 2022-06-14 05:43:00.868519
# Unit test for function is_json
def test_is_json():
    assert(is_json('{"name": "Peter"}') == True)
    assert(is_json('[1, 2, 3]') == True)
    assert(is_json('{nope}') == False)
    assert(is_json({"name": "Peter"}) == True)
    print("Passed test_is_json")


# Generated at 2022-06-14 05:43:03.533685
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75') == True
    assert is_ip_v4('nope') == False
    assert is_ip_v4('255.200.100.999') == False



# Generated at 2022-06-14 05:43:12.899308
# Unit test for function is_email
def test_is_email():
    assert is_email('email@example.com') is True
    assert is_email('firstname.lastname@example.com') is True
    assert is_email('email@subdomain.example.com') is True
    assert is_email('firstname+lastname@example.com') is True
    assert is_email('email@123.123.123.123') is True
    assert is_email('email@[123.123.123.123]') is True
    assert is_email('"email"@example.com') is True
    assert is_email('1234567890@example.com') is True
    assert is_email('email@example-one.com') is True
    assert is_email('_______@example.com') is True
    assert is_email('email@example.name') is True

# Generated at 2022-06-14 05:43:20.513477
# Unit test for function is_email
def test_is_email():
    assert is_email('abc') == False
    assert is_email('123@mail.com') == True
    assert is_email('"Abc@def"@example.com') == True
    assert is_email('a\@b@c.com') == True
    assert is_email('a@b.c') == True
    assert is_email('a@b.c.') == True
    assert is_email('Abc.def@example.com.') == False
    assert is_email('a"b(c)d,e:f;g<h>i[j\\k]l@example.com') == True
    assert is_email('just"not"right@example.com') == False
    assert is_email('this is"not\\allowed@example.com') == False

# Generated at 2022-06-14 05:43:22.652465
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75') == True
    assert is_ip_v4('nope') == False
    assert is_ip_v4('255.200.100.999') == False


# Generated at 2022-06-14 05:43:26.276961
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com') == True
    assert is_email('@gmail.com') == False
    assert is_email('"lele"@gmail.com') == True
    
test_is_email()



# Generated at 2022-06-14 05:43:37.515981
# Unit test for function is_email
def test_is_email():
    assert not is_email('')
    assert not is_email(None)
    assert not is_email(' ')
    assert not is_email('hello')
    assert not is_email('hello@')
    assert not is_email('.hello@gmail.com')
    assert not is_email('hello@gmail')
    assert not is_email('hello@gmail...com')
    assert not is_email("hello@gmail.com\n")
    assert not is_email("hello@gmail.com\r")
    assert not is_email("hello@gmail.com\t")
    assert not is_email("hello@gmail.com\0")
    assert not is_email("hello@gmail.com ")
    assert not is_email("@gmail.com")
    assert not is_email("hello@gmail..com")
   

# Generated at 2022-06-14 05:43:49.631697
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    checker = __ISBNChecker('1234567890123')
    assert checker.is_isbn_13()

    checker = __ISBNChecker('1234567890124')
    assert not checker.is_isbn_13()



# Generated at 2022-06-14 05:43:54.246764
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75') == True
    assert is_ip_v4('nope') == False
    assert is_ip_v4('255.200.100.999') == False
    return True

# Generated at 2022-06-14 05:44:05.486376
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    test_values = {
        '0385353308': True,
        '0471958697': True,
        '0-7897-2240-2': True,
        '978-0-306-40615-7': False,
        '978-0-306-40615': False,
        '0-7897-2240--': False,
        '0-7897-2240-12': False,
        '0-7897-2240': False
    }

    for value, expected_result in test_values.items():
        assert __ISBNChecker(value).is_isbn_10() == expected_result

#Unit test for method is_isbn_13 of class __ISBNChecker

# Generated at 2022-06-14 05:44:19.289613
# Unit test for function is_email
def test_is_email():
    assert is_email('example.email@gmail.com') # should be true
    assert is_email('example.email+tag@gmail.com') # should be true
    assert is_email('example.email-tag@gmail.com') # should be true
    assert is_email('example.email_tag@gmail.com') # should be true
    assert is_email('example.email.tag@gmail.com') # should be true
    assert is_email('_example.email@gmail.com') # should be true
    assert is_email('example.email@gmail.web') # should be true
    assert is_email('example.email@gmail.info') # should be true
    assert is_email('example.email@gmail.name') # should be true
    assert is_email('example.email@gmail.io') # should be true


# Generated at 2022-06-14 05:44:32.063754
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    # test a valid isbn-10
    assert __ISBNChecker('0306406152').is_isbn_10() == True

    # test an invalid isbn-10
    assert __ISBNChecker('0306406154').is_isbn_10() == False

    # test with a string representing a valid isbn-10
    assert __ISBNChecker('ISBN 0306406152').is_isbn_10() == True

    # test with an empty string
    assert __ISBNChecker('').is_isbn_10() == False

    # test with a non-string value
    # assert __ISBNChecker(0).is_isbn_10() == False
    try:
        __ISBNChecker(0)
    except InvalidInputError:
        pass


# Generated at 2022-06-14 05:44:37.353693
# Unit test for function is_json
def test_is_json():
    assert not is_json('42')
    assert not is_json(42)
    assert is_json(' "42" ')
    assert is_json('{"a": "b"}')
    assert is_json('[] ')
    assert is_json('[42]')
    assert not is_json('["foo":["bar"]')


# Generated at 2022-06-14 05:44:46.766845
# Unit test for function is_email
def test_is_email():
    assert is_email('foo@bar.com')
    assert is_email('x@x.au')
    assert is_email('foo+bar@bar.com')
    assert is_email('hans.m端ller@test.com')
    assert is_email('hans@m端ller.com')
    assert is_email('test|123@m端ller.com')
    assert is_email('"foo\\@bar"@example.com')
    assert is_email('"foo@bar"@example.com')
    assert is_email('foo.bar@example.com')
    assert is_email('foo-bar@example.com')
    assert is_email('foo_bar@example.com')
    assert is_email('foor@example.com')

# Generated at 2022-06-14 05:44:58.401265
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker("9123456789010").is_isbn_13()
    assert __ISBNChecker("0000000000000").is_isbn_13()
    assert __ISBNChecker("9789898989898").is_isbn_13()
    assert not __ISBNChecker("9123456789000").is_isbn_13()
    assert not __ISBNChecker("9789898989899").is_isbn_13()
    assert not __ISBNChecker("978989898989").is_isbn_13()
    assert not __ISBNChecker("97898989898981").is_isbn_13()
    assert not __ISBNChecker("912345678901").is_isbn_13()
    assert not __ISBNChecker("00000000000000").is_

# Generated at 2022-06-14 05:45:03.367739
# Unit test for function is_ip_v4
def test_is_ip_v4():
  assert is_ip_v4('255.200.100.75') == True
  assert is_ip_v4('nope') == False
  assert is_ip_v4('255.200.100.999') == False

test_is_ip_v4()


# Generated at 2022-06-14 05:45:07.116221
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') == True
    assert is_json('[1, 2, 3]') == True
    assert is_json('{nope}') == False



# Generated at 2022-06-14 05:45:15.412807
# Unit test for function is_email
def test_is_email():
    assert is_email('hello@gmail.com') == True



# Generated at 2022-06-14 05:45:28.293121
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75')
    assert is_ip_v4('127.0.0.1')
    assert is_ip_v4('192.168.0.3')
    assert is_ip_v4('0.1.1.1')
    assert is_ip_v4('0.0.0.0')
    assert not is_ip_v4('nope')
    assert not is_ip_v4('255.200.100.999')
    assert not is_ip_v4('0.0.0.256')
    assert not is_ip_v4('256.0.0.0')
    assert not is_ip_v4('0.256.0.0')
    assert not is_ip_v4('0.0.256.0')


# Generated at 2022-06-14 05:45:31.350265
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com') == True
    assert is_email('@gmail.com') == False
    assert is_email('my.email@the-provider.com.') == False


# Generated at 2022-06-14 05:45:42.018149
# Unit test for function is_json
def test_is_json():
    # Test case 1
    input_string = '{"name": "Peter"}'
    expected = True
    actual = is_json(input_string)
    assert actual == expected

    # Test case 2
    input_string = '[1, 2, 3]'
    expected = True
    actual = is_json(input_string)
    assert actual == expected

    # Test case 3
    input_string = '{nope}'
    expected = False
    actual = is_json(input_string)
    assert actual == expected



# Generated at 2022-06-14 05:45:54.748964
# Unit test for function is_json
def test_is_json():
    assert(is_json('true') == False)
    assert(is_json('null') == False)
    assert(is_json('"null"') == False)
    assert(is_json('42') == False)
    assert(is_json('3.14') == False)
    assert(is_json('"hello"') == False)
    assert(is_json('[]') == True)
    assert(is_json('{}') == True)
    assert(is_json('{"name": "Peter"}') == True)
    assert(is_json('[1, 2, 3]') == True)
    assert(is_json('[1, "two", 3.0]') == True)
    assert(is_json('{"name": "Peter", "age": 23}') == True)

# Generated at 2022-06-14 05:45:57.208755
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') is True
    assert is_json('[1, 2, 3]') is True
    assert is_json('{nope}') is False
#test end



# Generated at 2022-06-14 05:46:00.929453
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') is True
    assert is_json('[1, 2, 3]') is True
    assert is_json('{nope}') is False
    assert is_json('') is False
    assert is_json(None) is False


# Generated at 2022-06-14 05:46:02.801561
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}')
    assert is_json('[1, 2, 3]')
    assert not is_json('{nope}')

# Generated at 2022-06-14 05:46:12.393840
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker('0446580791').is_isbn_10()
    assert __ISBNChecker('048665088X').is_isbn_10()
    assert __ISBNChecker('0307887448').is_isbn_10()

    assert __ISBNChecker('0446580792').is_isbn_10() is False
    assert __ISBNChecker('0486650881').is_isbn_10() is False
    assert __ISBNChecker('0307887449').is_isbn_10() is False

# Generated at 2022-06-14 05:46:23.105140
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    checker = __ISBNChecker(input_string='159017860X')
    assert checker.is_isbn_10()

    checker = __ISBNChecker(input_string='013454323X')
    assert checker.is_isbn_10()

    checker = __ISBNChecker(input_string='0262510871')
    assert checker.is_isbn_10()

    checker = __ISBNChecker(input_string='0312510871')
    assert checker.is_isbn_10()

    checker = __ISBNChecker(input_string='0312510871')
    assert checker.is_isbn_10()

    checker = __ISBNChecker(input_string='1590178609')
    assert not checker.is_isbn_10

# Generated at 2022-06-14 05:46:41.677769
# Unit test for function is_email
def test_is_email():
    assert is_email('test@test.com') is True
    assert is_email('test@test.co.uk') is True
    assert is_email('test.test@test.co.uk') is True
    assert is_email('test@test.com.') is True
    assert is_email('test@test.c') is True
    assert is_email('test@test.c') is True
    assert is_email('test+test@test.c') is True
    assert is_email('test+test@test.com') is True
    assert is_email('test@test.apple') is True
    assert is_email('test@test.co.uk.id') is True
    assert is_email('test@test.co.uk.id.test') is True

# Generated at 2022-06-14 05:46:49.109685
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}')
    assert is_json('[1, 2, 3]')
    assert is_json('{"name": "Peter", "age": "12"}')
    assert is_json('[]')
    assert not is_json('{nope}')
    assert not is_json('nope')



# Generated at 2022-06-14 05:46:57.982549
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():

    valid_inputs = [
        '9788376428591',
        '9788371857126',
        '9781910620389'
    ]

    invalid_inputs = [
        '978837642859',  # length too short
        '9788376428591111',  # length too long
        '978837642859a',  # non-digit character
        '9788376428593',  # invalid check digit
        '978837642859211',  # invalid check digit
        '9788376428592a'  # non-digit character
    ]

    for input_string in valid_inputs:
        checker = __ISBNChecker(input_string)

# Generated at 2022-06-14 05:47:07.998178
# Unit test for function is_json
def test_is_json():
    with pytest.raises(InvalidInputError):
        is_json(None)
    assert not is_json('')
    assert not is_json('hello')
    assert not is_json('[1, 2, 3')
    assert is_json('{}')
    assert is_json('[]')
    assert is_json('{"name": "Peter"}')
    assert is_json('[1, 2, 3]')
    assert is_json('{"name": "Peter", "foo": [1, 2, 3]}')
    assert not is_json('{nope}')



# Generated at 2022-06-14 05:47:11.014344
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com')==1
    assert is_email('@gmail.com')==0
test_is_email()


# Generated at 2022-06-14 05:47:19.723002
# Unit test for function is_email
def test_is_email():
    assert not is_email(None)
    assert not is_email('')
    assert not is_email('@')
    assert not is_email('@gmail.com')
    assert not is_email('name@')
    assert not is_email('.name@gmail.com')
    assert not is_email('name.@gmail.com')
    assert not is_email('name..surname@gmail.com')
    assert not is_email('name.surname@gmail.')
    assert not is_email('name+surname@gmail.com')
    assert not is_email('name_surname@gmail.com')
    assert not is_email('name$surname@gmail.com')
    assert not is_email('name#surname@gmail.com')

# Generated at 2022-06-14 05:47:31.012054
# Unit test for function is_email
def test_is_email():
	assert is_email('toto@gmail.com') == True
	assert is_email('toto.titi@gmail.com') == True
	assert is_email('toto.titi.tata@gmail.com') ==  True
	assert is_email(' toto.titi@gmail.com') == False
	assert is_email('toto.titi@gmail.com ') == False
	assert is_email('tototiti@gmail.com') == False
	assert is_email('toto.titi.tata.tutu@gmail.com') == False
	assert is_email('toto@titi@gmail.com') == False


# Generated at 2022-06-14 05:47:36.057910
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4("255.200.100.75")
    assert not is_ip_v4("nope")
    assert not is_ip_v4("255.200.100.999")
test_is_ip_v4()



# Generated at 2022-06-14 05:47:48.567687
# Unit test for function is_email
def test_is_email():
    assert is_email('xxxx@gmail.com') == True
    assert is_email('xxxx.xxxx@domain.com') == True
    assert is_email('xxxx.xxxx@subdomain.domain.com') == True
    assert is_email('device.xxxx@subdomain.domain.com') == True
    assert is_email('device.xxxx@subdomain.domain.com') == True
    assert is_email('xxxx.xxxx.xxxx@domain.com') == True
    assert is_email('xxxx-xxxx@domain.com') == True
    assert is_email('xxxx-xxxx.xxxx@domain.com') == True
    assert is_email('xxxx-xx--xx@domain.com') == False
    assert is_email('xxxxx.xxxx@domain.com') == False
    assert is_email('xxxx.xxxxxxx@domain.com')

# Generated at 2022-06-14 05:47:54.807830
# Unit test for function is_email
def test_is_email():
    assert is_email("my@email.com") == True
    assert is_email("my.email@gmail.com") == True
    assert is_email("my.email@the-provider.com") == True
    assert is_email("my.email@the-provider.com") == True
    assert is_email("my.email.@the-provider.com") == False
    assert is_email("my.email.@.the-provider.com") == False
    assert is_email("my.email") == False
    assert is_email("@gmail.com") == False

test_is_email()



# Generated at 2022-06-14 05:48:06.086277
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    checker = __ISBNChecker('9570254389')
    assert checker.is_isbn_10() == True
    assert checker.is_isbn_13() == False
    print('Test for method is_isbn_10 of class __ISBNChecker passed')


# Generated at 2022-06-14 05:48:17.787340
# Unit test for function is_email
def test_is_email():
    assert is_email('abc@abc.com') == True
    assert is_email("abc@abc.com") == True
    assert is_email("abc@abc.com ") == False
    assert is_email('abc@abc..com') == False
    assert is_email('abc@') == False
    assert is_email("abc@abc..com") == False
    assert is_email("abc@abc.com ") == False
    assert is_email(" abc@abc.com") == False
    assert is_email("abc@abc.com") == True
    assert is_email("abc.abc@abc.com") == True
    assert is_email("abc.abc@abc.com ") == False
    assert is_email(".abc@abc.com") == False
    assert is_email("abc@abc.com/")

# Generated at 2022-06-14 05:48:29.019069
# Unit test for function is_email
def test_is_email():

    # 1. non-empty string
    assert is_email("some_email@gmail.com") == True
    assert is_email("some_email@yahoo.co.in") == True

    # 2. Empty string
    assert is_email("") == False

    # 3. At missing
    assert is_email("some_emailgmail.com") == False
    assert is_email("some_emailyahoo.co.in") == False

    # 4. Second component missing
    assert is_email("some_email@") == False

    # 5. First component empty
    assert is_email("@gmail.com") == False

    # 6. End component has dot
    assert is_email("some_email@gmail.com.") == False

    # 7. Start component has dot