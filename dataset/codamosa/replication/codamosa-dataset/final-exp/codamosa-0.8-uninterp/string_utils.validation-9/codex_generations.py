

# Generated at 2022-06-14 05:38:59.190297
# Unit test for function is_url
def test_is_url():
    assert is_url('http://foo.com/blah_blah')
    assert is_url('http://foo.com/blah_blah/')
    assert is_url('http://foo.com/blah_blah_(wikipedia)')
    assert is_url('http://foo.com/blah_blah_(wikipedia)_(again)')
    assert is_url('http://www.example.com/wpstyle/?p=364')
    assert is_url('https://www.example.com/foo/?bar=baz&inga=42&quux')
    assert is_url('http://✪df.ws/123')
    assert is_url('http://userid:password@example.com:8080')
    assert is_url('http://userid:password@example.com:8080/')
   

# Generated at 2022-06-14 05:39:04.635210
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75') == True
    assert is_ip_v4('nope') == False
    assert is_ip_v4('255.200.100.999') == False

# Generated at 2022-06-14 05:39:13.413210
# Unit test for function is_email
def test_is_email():
    assert not is_email(None)
    assert is_email('my.email@the-provider.com')
    assert not is_email('@gmail.com')
    assert not is_email('aa.com')
    assert is_email('"My.Email"@the-provider.com')
    assert is_email('"My\\ Email"@the-provider.com')
    assert is_email('"My.Email\\"@the-provider.com')
    assert is_email('"\\ My.Email"@the-provider.com')
    assert is_email('"My.Email@the-provider.com')
    assert is_email('My.Email"@the-provider.com')
    assert not is_email('"My.Email""@the-provider.com')
    assert is_email

# Generated at 2022-06-14 05:39:18.225727
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75') == True
    assert is_ip_v4('nope') == False
    assert is_ip_v4('255.200.100.999') == False


# Generated at 2022-06-14 05:39:32.841473
# Unit test for function is_email

# Generated at 2022-06-14 05:39:35.754112
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com') is True
    assert is_email('@gmail.com') is False


# Generated at 2022-06-14 05:39:49.683479
# Unit test for function is_credit_card
def test_is_credit_card():
    # test for card type VISA
    assert is_credit_card('4111111111111111', card_type='VISA') == True
    assert is_credit_card('4222222222222', card_type='VISA') == True

    # test for card type MASTERCARD
    assert is_credit_card('5555555555554444', card_type='MASTERCARD') == True
    assert is_credit_card('5105105105105100', card_type='MASTERCARD') == True
    # test for card type AMERICAN_EXPRESS
    assert is_credit_card('378282246310005', card_type='AMERICAN_EXPRESS') == True
    assert is_credit_card('371449635398431', card_type='AMERICAN_EXPRESS') == True
    #

# Generated at 2022-06-14 05:39:53.467231
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker('978019952122').is_isbn_13() == True
    assert __ISBNChecker('1234567890').is_isbn_13() == False


# Generated at 2022-06-14 05:40:01.053816
# Unit test for function is_email
def test_is_email():
    m = 'a"b(c)d,e:f;g<h>i[j\k]l@example.com'
    m1 = 'just"not"right@example.com'
    m2 = 'this is"not\allowed@example.com'

    assert is_email(m) == True
    assert is_email(m1) == False
    assert is_email(m2) == False


# Generated at 2022-06-14 05:40:09.542738
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('0.0.0.0')
    assert not is_ip_v4('')
    assert not is_ip_v4('256.0.0.0')
    assert not is_ip_v4('255.200.100.999')
    assert not is_ip_v4('255.200.100')
    assert not is_ip_v4('255.200.100.999')



# Generated at 2022-06-14 05:40:27.583673
# Unit test for function is_integer
def test_is_integer():
    assert is_integer(input_string='123')
    assert is_integer(input_string='-123')
    assert is_integer(input_string='0')
    assert is_integer(input_string='-0')
    assert is_integer(input_string='+0')
    assert is_integer(input_string='+123')
    assert is_integer(input_string='1E3')
    assert is_integer(input_string='-1E3')

# Test negative cases
    assert not is_integer(input_string='1E-3')
    assert not is_integer(input_string='-1E-3')
    assert not is_integer(input_string='-1.2')
    assert not is_integer(input_string='-1.2E-3')

# Generated at 2022-06-14 05:40:31.393954
# Unit test for function is_ip
def test_is_ip():
    assert is_ip('255.200.100.75')
    assert is_ip('2001:db8:85a3:0000:0000:8a2e:370:7334')
    assert not is_ip('1.2.3')
test_is_ip()



# Generated at 2022-06-14 05:40:40.328715
# Unit test for function is_ip
def test_is_ip():
    # TODO: Add missing test cases
    assert is_ip('255.200.100.75')
    assert is_ip('176.16.50.1')
    assert is_ip('2001:db8:85a3:0000:0000:8a2e:370:7334')
    assert is_ip('1.2.3') == False
    assert is_ip('2001:db8:85a3:0000:0000:8a2e:370:?') == False


# Generated at 2022-06-14 05:40:51.542970
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker('0201485672').is_isbn_10() == True
    assert __ISBNChecker('1-5659-2795-1').is_isbn_10() == True
    assert __ISBNChecker('9971-5-0210-1').is_isbn_10() == True
    assert __ISBNChecker('9971-5-0210').is_isbn_10() == False
    assert __ISBNChecker('9971-5-0210-11').is_isbn_10() == False
    assert __ISBNChecker('1-5659-2795-15').is_isbn_10() == False
    assert __ISBNChecker('1-5659-2795-11').is_isbn_10() == False

# Generated at 2022-06-14 05:40:52.462871
# Unit test for function is_json
def test_is_json():
    pass



# Generated at 2022-06-14 05:41:02.803613
# Unit test for function is_email
def test_is_email():
    assert not is_email('@gmail.com')
    assert not is_email('.@gmail.com')
    assert not is_email('a..b@gmail.com')
    assert not is_email('john.smith@gmail.')
    assert not is_email('john.smith.@gmail.com')
    assert not is_email('john..smith@gmail.com')
    assert not is_email('john.smith@gmail.com..com')
    assert is_email('a@gmail.com')
    assert is_email('john.smith@gmail.com')
    assert is_email('john.smith@gmail.com.com')
    assert is_email('"john.smith"@gmail.com')
    assert is_email('john\\.smith@gmail.com')

# Generated at 2022-06-14 05:41:07.558493
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') == True
    assert is_json('[1, 2, 3]') == True
    assert is_json('{nope}') == False
    assert is_json('{"name": peter}') == False
#test_is_json()



# Generated at 2022-06-14 05:41:13.186579
# Unit test for function is_ip
def test_is_ip():
        assert is_ip('255.200.100.75') is True
        assert is_ip('2001:db8:85a3:0000:0000:8a2e:370:7334') is True
        assert is_ip('1.2.3') is False


# Generated at 2022-06-14 05:41:17.439988
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "hello"}')
    assert is_json('["hello", "world"]')
    assert not is_json('{')
    assert not is_json('[')

# test_is_json()



# Generated at 2022-06-14 05:41:24.466788
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "John"}') is True
    assert is_json('{"name": "John", "age": 35}') is True
    assert is_json('[{"name": "John"}, {"name": "Peter"}]') is True
    assert is_json('[1, 2, 3]') is True
    assert is_json('{nope}') is False
    assert is_json('{"name": "John", "age": 35') is False



# Generated at 2022-06-14 05:41:32.903261
# Unit test for function is_email
def test_is_email():
    print(is_email('my.email@the-provider.com'))
    print(is_email('@gmail.com'))

test_is_email()


# Generated at 2022-06-14 05:41:38.141070
# Unit test for function is_json
def test_is_json():
  assert is_json("{\"key\": \"value\"}") == True
  assert is_json("{'key2': 'value2'}") == False
  assert is_json("") == False
  assert is_json("[1, 2.0, \"3\"]") == True




# Generated at 2022-06-14 05:41:39.892694
# Unit test for function is_credit_card
def test_is_credit_card():
    assert is_credit_card("4444444444444448") == True


# Generated at 2022-06-14 05:41:44.751487
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker('978-0-306-40615-7').is_isbn_13() is True
    assert __ISBNChecker('978-40615').is_isbn_13() is False



# Generated at 2022-06-14 05:41:49.028124
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75') == True
    assert is_ip_v4('nope') == False
    assert is_ip_v4('255.200.100.999') == False


# Generated at 2022-06-14 05:42:00.481443
# Unit test for function is_email
def test_is_email():
    assert is_email('test@test.it') is True
    assert is_email('test.test@test.it') is True
    assert is_email('test+test@test.it') is True
    assert is_email('test test@test.it') is True
    assert is_email('test.test@test.test.it') is True
    assert is_email('test+test@test.test.it') is True
    assert is_email('test test@test.test.it') is True
    assert is_email('test@test..test.it') is False
    assert is_email('test@testtest.test.it') is True
    assert is_email('test@test.testtest.it') is True
    assert is_email('test@test.test.testtest.it') is True
    assert is_email

# Generated at 2022-06-14 05:42:08.672041
# Unit test for function is_isbn
def test_is_isbn():
    assert is_isbn('9780312498580')
    assert is_isbn('978-0312498580')
    assert is_isbn('9780312498580', normalize=False)
    assert not is_isbn('978-0312498580', normalize=False)

    assert is_isbn('1506715214')
    assert is_isbn('150-6715214')
    assert is_isbn('1506715214', normalize=False)
    assert not is_isbn('150-6715214', normalize=False)


# Generated at 2022-06-14 05:42:10.767070
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com') is True
    assert is_email('@gmail.com') is False



# Generated at 2022-06-14 05:42:14.505959
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    isbnChecker = __ISBNChecker("0891908880", True)
    result = isbnChecker.is_isbn_10()
    assert result == True
    return True


# Generated at 2022-06-14 05:42:18.283603
# Unit test for function is_isbn
def test_is_isbn():
    assert is_isbn('9780312498580') == True
    assert is_isbn('1506715214') == True

# Generated at 2022-06-14 05:42:36.617264
# Unit test for function is_email
def test_is_email():
    assert is_email("\".test@test.com\"@example.com")
    assert is_email("!#$%&'*+-/=?^_`{}|~@example.org")
    assert is_email("\"()<>[]:,;@\\\"!#$%&'-/=?^_`{}| ~.a\"@example.org")
    assert is_email("\"Abc\\@def\"@example.com")
    assert is_email("\"Fred Bloggs\"@example.com")
    assert is_email("\"Joe\\\\Blow\"@example.com")
    assert is_email("\"Abc@def\"@example.com")
    assert is_email("\"Fred Bloggs\"@example.com")
    assert is_email("\"Joe\\Blow\"@example.com")


# Generated at 2022-06-14 05:42:48.145128
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker("0425071720").is_isbn_10() == True
    assert __ISBNChecker("0451457994").is_isbn_10() == True
    assert __ISBNChecker("0440508835").is_isbn_10() == True
    assert __ISBNChecker("0812550706").is_isbn_10() == True
    assert __ISBNChecker("0812533550").is_isbn_10() == True
    assert __ISBNChecker("0812515287").is_isbn_10() == True
    assert __ISBNChecker("0812550706").is_isbn_10() == True
    assert __ISBNChecker("0812503623").is_isbn_10() == True

# Generated at 2022-06-14 05:42:52.803521
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75') is True
    assert is_ip_v4('nope') is False
    assert is_ip_v4('255.200.100.999') is False


# Generated at 2022-06-14 05:43:03.798972
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker('979-10-95546-02-1').is_isbn_13()
    assert __ISBNChecker('978-1593275846').is_isbn_13()
    assert __ISBNChecker('9781590512090').is_isbn_13()
    assert __ISBNChecker('978-1590512090').is_isbn_13()
    assert __ISBNChecker('979-10-95546-02-1', False).is_isbn_13()
    assert not __ISBNChecker('9791095546021').is_isbn_13()
    assert not __ISBNChecker('978-1593275847').is_isbn_13()  # Not valid
    assert not __ISBNChecker('9784321123456').is_

# Generated at 2022-06-14 05:43:07.954012
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') == True
    assert is_json('[1, 2, 3]') == True
    assert is_json('{nope}') == False


# Generated at 2022-06-14 05:43:10.822458
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') == True
    assert is_json('[1, 2, 3]') == True
    assert is_json('{nope}') == False
    assert is_json('test') == True

test_is_json()


# Generated at 2022-06-14 05:43:13.552095
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75') # returns true
    assert not is_ip_v4('nope') # returns false (not an ip)
    assert not is_ip_v4('255.200.100.999') # returns false (999 is out of range)



# Generated at 2022-06-14 05:43:14.802162
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75')

# Generated at 2022-06-14 05:43:23.208929
# Unit test for function is_email
def test_is_email():
    assert is_email("test@gmail.com") == True
    assert is_email("test@gmailcom") == False
    assert is_email("test@") == False
    assert is_email("test@gmail.com.au") == True
    assert is_email("test@test.test@test.test") == False
    assert is_email("'test'@test.test") == False
    assert is_email("test@test.test'") == False

# Generated at 2022-06-14 05:43:32.526766
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    isbn_checker = __ISBNChecker('9780446310789')
    assert isbn_checker.is_isbn_13() == True

    isbn_checker = __ISBNChecker('9781853267338')
    assert isbn_checker.is_isbn_13() == True

    isbn_checker = __ISBNChecker('9781853267333')
    assert isbn_checker.is_isbn_13() == True

    isbn_checker = __ISBNChecker('978185326733')
    assert isbn_checker.is_isbn_13() == False

    isbn_checker = __ISBNChecker('978185326733a')
    assert isbn_checker.is_isbn_13() == False



# Generated at 2022-06-14 05:43:44.965146
# Unit test for function is_email
def test_is_email():
    assert is_email("email@address.com") == True
    assert is_email("email@address") == False
    assert is_email("email@address.co.uk") == True
    assert is_email("email@address.uk") == False
    assert is_email("email@address.nhs.uk") == True
    assert is_email("email@address.nhs") == False
    assert is_email("email@address.za") == True



# Generated at 2022-06-14 05:43:48.579772
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert not is_ip_v4(None)
    assert not is_ip_v4('192.168.0.256')
    assert is_ip_v4('192.168.0.255')


# Generated at 2022-06-14 05:43:59.339183
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker('9788885206736').is_isbn_13()
    assert __ISBNChecker('978888520673').is_isbn_13() is False
    assert __ISBNChecker('9788885206').is_isbn_13() is False
    assert __ISBNChecker('9788885206t').is_isbn_13() is False
    assert __ISBNChecker('9788885206t3').is_isbn_13() is False
    assert __ISBNChecker('9788885206t36').is_isbn_13() is False

# Generated at 2022-06-14 05:44:08.985829
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    checker = __ISBNChecker('978-3-16-148410-0')
    assert checker.is_isbn_13() == True

    checker = __ISBNChecker('9783161484100')
    assert checker.is_isbn_13() == True

    checker = __ISBNChecker('978316148410A')
    assert checker.is_isbn_13() == False

    checker = __ISBNChecker('9783161484104')
    assert checker.is_isbn_13() == False

    checker = __ISBNChecker('3-16-148410-0')
    assert checker.is_isbn_13() == False

    checker = __ISBNChecker('978-3-16-148410-01')

# Generated at 2022-06-14 05:44:13.748551
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker("978-1-569-87960-7", False).is_isbn_13()
    assert __ISBNChecker("979-1-569-87960-7", False).is_isbn_13()

    assert not __ISBNChecker("978-1-569-87960-7", False).is_isbn_13()
    assert not __ISBNChecker("978-1-569-87960-7", False).is_isbn_13()



# Generated at 2022-06-14 05:44:17.736429
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}')
    assert not is_json('{nope}')
    assert not is_json('[1, 2, 3]')
    assert not is_json('')



# Generated at 2022-06-14 05:44:28.222987
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    checker = __ISBNChecker("1234567890123", normalize=False)
    assert checker.is_isbn_13() == True

    checker = __ISBNChecker("12345678901231", normalize=False)
    assert checker.is_isbn_13() == False

    checker = __ISBNChecker("1234567890124", normalize=False)
    assert checker.is_isbn_13() == False

    checker = __ISBNChecker("123456789012", normalize=False)
    assert checker.is_isbn_13() == False


# Generated at 2022-06-14 05:44:37.000197
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    cases = ['000147486852', '00101223976', '002000601980', '00214483643', '1-86046-382-4']
    for index, case in enumerate(cases):
        print('Testing case #' + str(index + 1))
        checker = __ISBNChecker(case)
        assert checker.is_isbn_10()

    cases = ['', '000', '@' * 10, '0' * 9, '1' * 10, '1' * 11, '1' * 12, '1' * 13, \
        '1' * 100, '0' * 9, '002000601980', '00214483643', '1-86046-382-4']

# Generated at 2022-06-14 05:44:46.592192
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    # Test positive cases
    positive_test_input_string = [
        '9780984782857',
        '978-0-9847828-5-7',
        '978 09847828 5 7',
        '978-1-56619-909-4',
        '978-0-940450-43-8',
    ]

    try:
        for input_string in positive_test_input_string:
            assert __ISBNChecker(input_string).is_isbn_13()
    except AssertionError as e:
        print(f'Failed test for __ISBNChecker.is_isbn_13()!')
        print(f'Error message: {e}')

    # Test negative cases

# Generated at 2022-06-14 05:44:57.066864
# Unit test for function is_email
def test_is_email():
    # positive cases
    assert is_email("email@domain.com")
    assert is_email("firstname.lastname@domain.com")
    assert is_email("email@subdomain.domain.com")
    assert is_email("firstname+lastname@domain.com")
    assert is_email("email@123.123.123.123")
    assert is_email("email@[123.123.123.123]")
    assert is_email("1234567890@domain.com")
    assert is_email("email@domain-one.com")
    assert is_email("_______@domain.com ")
    assert is_email("email@domain.name")
    assert is_email("email@domain.co.jp")
    assert is_email("firstname-lastname@domain.com")

    # negative cases


# Generated at 2022-06-14 05:45:11.996055
# Unit test for function is_email
def test_is_email():
    assert is_email('abc@abc.com') == True
    assert is_email('abc@abc.com.vn') == True
    assert is_email('123.abc@abc.com') == True
    assert is_email('abc@abc.edu.vn') == True
    assert is_email('abc@_123.com') == True
    assert is_email('@gmail.com') == False
    assert is_email('.@gmail.com') == False
    assert is_email('abc..123@gmail.com') == False
    assert is_email('abc.@gmail.com') == False
    assert is_email('abc@abc@abc.com') == False
    assert is_email('abc@.com') == False
    assert is_email('abc@.abc.com') == False

# Generated at 2022-06-14 05:45:26.602158
# Unit test for function is_email
def test_is_email():
    assert is_email('email@example.com') == True
    assert is_email('firstname.lastname@example.com') == True
    assert is_email('email@subdomain.example.com') == True
    assert is_email('firstname+lastname@example.com') == True
    assert is_email('email@123.123.123.123') == True
    assert is_email('email@[123.123.123.123]') == True
    assert is_email('"email"@example.com') == True
    assert is_email('1234567890@example.com') == True
    assert is_email('email@example-one.com') == True
    assert is_email('_______@example.com') == True
    assert is_email('email@example.name') == True

# Generated at 2022-06-14 05:45:31.059146
# Unit test for function is_json
def test_is_json():
    assert is_json('[1,2,3]') == True
    assert is_json('{"key":"value"}') == True
    assert is_json('{ "key" : "value" }') == True
    assert is_json('{"key":"value","key2":"value2"}') == True


# Generated at 2022-06-14 05:45:45.462510
# Unit test for function is_email
def test_is_email():

    assert is_email('my.email@the-provider.com') == True
    assert is_email('@gmail.com') == False
    assert is_email('me+@gmail.com') == True
    assert is_email('me+label@gmail.com') == True
    assert is_email('me+label@gmail.com') == True
    assert is_email('me@gmail.com') == True
    assert is_email('"me"@gmail.com') == True
    assert is_email('me\\@gmail.com') == True
    assert is_email('me@gmail.com') == True
    assert is_email('"me"@gmail.com') == True
    assert is_email('me\\@gmail.com') == True
    assert is_email('"me"@gmail.com') == True

# Generated at 2022-06-14 05:45:47.525987
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    checker = __ISBNChecker('978-3-16-148410-0')
    assert checker.is_isbn_13() is True



# Generated at 2022-06-14 05:45:57.946769
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4("172.16.254.1") == True
    assert is_ip_v4("0.0.0.0") == True
    assert is_ip_v4("255.255.255.255") == True
    assert is_ip_v4("172.16.254.1.1") == False
    assert is_ip_v4("hello") == False
    assert is_ip_v4("") == False
    assert is_ip_v4("0") == False
    assert is_ip_v4("10.1.1.1.1") == False
    assert is_ip_v4("0..0.0.0") == False
    assert is_ip_v4("0.0.0") == False

# Generated at 2022-06-14 05:46:01.062347
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75') == True
    assert is_ip_v4('nope') == False
    assert is_ip_v4('255.200.100.999') == False
test_is_ip_v4()



# Generated at 2022-06-14 05:46:14.402513
# Unit test for function is_email
def test_is_email():
    assert is_email('info@example.com') == True
    assert is_email('info@example.com ') == False
    assert is_email('info @example.com ') == False
    assert is_email('info@example. com ') == False
    assert is_email('info@example.com. ') == False
    assert is_email('"info@example.com"@example.com') == True
    assert is_email('"info@example.com"@ example.com') == False
    assert is_email('"info@example.com" @example.com') == False
    assert is_email('"info@example.com"@example. com') == False
    assert is_email('"info@example.com"@example.com. ') == False

# Generated at 2022-06-14 05:46:18.351379
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') == True
    assert is_json('[1, 2, 3]') == True
    assert is_json('{nope}') == False


# Generated at 2022-06-14 05:46:23.786466
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') is True
    assert is_json('[1, 2, 3]') is True
    assert is_json('{nope}') is False


# Generated at 2022-06-14 05:46:32.178322
# Unit test for function is_email
def test_is_email():
    is_email('me@example.com')
    is_email('me@example.co.uk')
    is_email('Hi,me@example.com')
    is_email('me@example.museum')
    is_email('me_123@example.com')

    is_email('.me@example.com')
    is_email('me.@example.com')
    is_email('me@example..com')



# Generated at 2022-06-14 05:46:39.614636
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75') == True
    assert is_ip_v4('0.0.0.0') == True
    assert is_ip_v4('255.200.100.999') == False
    assert is_ip_v4('nope') == False
    assert is_ip_v4('255.200.100.999') == False


# Generated at 2022-06-14 05:46:48.806659
# Unit test for function is_json
def test_is_json():
    assert not is_json('')
    assert not is_json(12)
    assert not is_json('foo')
    assert not is_json('{"name"}')
    assert not is_json('{"name": "Peter"')
    assert is_json('{"name": "Peter"}')
    assert is_json('{"name": 12}')
    assert is_json('{"name": null}')
    assert is_json('[1, 2, 3]')



# Generated at 2022-06-14 05:46:53.877481
# Unit test for function is_json
def test_is_json():
    x = '{"name": "Peter"}'
    y = '{"name": "Peter"}'
    z = '{nope}'
    assert is_json(x) == is_json(y)
    assert is_json(z) == False



# Generated at 2022-06-14 05:46:56.177425
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}')
    assert not is_json('[1, 2, 3, "abc"]')


# Generated at 2022-06-14 05:46:58.113089
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker('1780572673').is_isbn_10() == True


# PUBLIC API



# Generated at 2022-06-14 05:47:03.132308
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75') == True
    assert is_ip_v4('nope') == False
    assert is_ip_v4('255.200.100.999') == False
    
test_is_ip_v4()

# Generated at 2022-06-14 05:47:13.277694
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com')
    assert not is_email('@gmail.com')
    assert is_email('\"\\\"very.unusual.@.unusual.com\\\"\"@example.com')
    assert is_email('\"very.(),:;<>[]\\\".VERY.\\\"very@\\\\ \\\"very\\\".unusual\"@strange.example.com')
    assert is_email('example-indeed@strange-example.com')
    assert is_email('admin@mailserver1')
    assert is_email('#!$%&\'*+-/=?^_`{}|~@example.org')

# Generated at 2022-06-14 05:47:17.614879
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    checker = __ISBNChecker('9780132124737')
    assert(checker.is_isbn_10() == False)


# Generated at 2022-06-14 05:47:21.440208
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    checker = __ISBNChecker('3-861-01997-9')
    assert checker.is_isbn_10(), 'checker.is_isbn_10 should return True'

# Generated at 2022-06-14 05:47:36.194027
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    # input_string is not string
    try:
        __ISBNChecker(input_string=object)
        assert False, 'Not catch exception: InvalidInputError'
    except InvalidInputError:
        pass
    # input_string is string but not numeric
    try:
        __ISBNChecker(input_string='a')
        assert False, 'Not catch exception: InvalidInputError'
    except InvalidInputError:
        pass
    # input_string length is not equal 10
    try:
        __ISBNChecker(input_string='123')
        assert False, 'Not catch exception: InvalidInputError'
    except InvalidInputError:
        pass
    # input_string length is 10 but not ISBN-10
    assert False == __ISBNChecker(input_string='1234567890').is_isbn_10()
   

# Generated at 2022-06-14 05:47:38.982876
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com') == True
    assert is_email('@gmail.com') == False


# Generated at 2022-06-14 05:47:47.254682
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert(    __ISBNChecker('978-3-16-148410-0').is_isbn_13() == True)
    assert(    __ISBNChecker('9783161484100').is_isbn_13() == True)

    assert(not __ISBNChecker('').is_isbn_13() == True)
    assert(not __ISBNChecker('978-3-16-148410-1').is_isbn_13() == True)
    assert(not __ISBNChecker('978-3-16-148410-**').is_isbn_13() == True)
    assert(not __ISBNChecker('978-3-16-14-810-**').is_isbn_13() == True)

# Generated at 2022-06-14 05:47:53.971360
# Unit test for function is_json
def test_is_json():
    """
    Test case for function is_json
    """
    assert is_json(None) == False
    assert is_json('{"name": "Peter"}') == True
    assert is_json('[1, 2, 3]') == True
    assert is_json('{nope}') == False



# Generated at 2022-06-14 05:48:01.704816
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4("0.0.0.0") == True
    assert is_ip_v4("255.255.255.255") == True
    assert is_ip_v4("255.255.255.256") == False
    assert is_ip_v4("255.255.255.2551") == False
    assert is_ip_v4("") == False
    assert is_ip_v4(" ") == False
    assert is_ip_v4("255.255.2551.255") == False
    assert is_ip_v4("255.255.2551") == False
    assert is_ip_v4("255.255.255") == False
    assert is_ip_v4("255.255.255.") == False

# Generated at 2022-06-14 05:48:06.212455
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') == True
    assert is_json('[1, 2, 3]') == True
    assert is_json('{nope}') == False
    
test_is_json()



# Generated at 2022-06-14 05:48:09.907454
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') == True
    assert is_json('[1, 2, 3]') == True
    assert is_json('[1, 2, 3') == False


# Generated at 2022-06-14 05:48:20.328164
# Unit test for method is_isbn_13 of class __ISBNChecker

# Generated at 2022-06-14 05:48:31.518669
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker('9780306406157').is_isbn_13() == True
    assert __ISBNChecker('978-0-306-40615-7').is_isbn_13() == True
    assert __ISBNChecker('9783-413-24186-3').is_isbn_13() == True
    assert __ISBNChecker('978-0-306-40615-0').is_isbn_13() == False
    assert __ISBNChecker('978-0-306-40615-*').is_isbn_13() == False
    assert __ISBNChecker('978-0-306-40615-8').is_isbn_13() == False
    assert __ISBNChecker('978-0-306-40615-5').is_isbn_13() == False