

# Generated at 2022-06-14 05:38:42.778993
# Unit test for function is_json
def test_is_json():
    test = str(open('test.json', 'r').read())
    res = is_json(test)
    assert res is True

# Generated at 2022-06-14 05:38:55.979727
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('1.1.1.1') == True
    assert is_ip_v4('255.255.255.255') == True
    assert is_ip_v4('1.1.1') == False
    assert is_ip_v4('255.255.255.b') == False
    assert is_ip_v4('') == False
    assert is_ip_v4(' ') == False
    assert is_ip_v4('1.1.1.') == False
    assert is_ip_v4('1.1.1.b') == False
    assert is_ip_v4('1.1.1.1.1') == False
    assert is_ip_v4('01.01.01.01') == False

# Generated at 2022-06-14 05:39:05.440612
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker('978-1-891830-08-2').is_isbn_13() is True
    assert __ISBNChecker('1-891830-08-7').is_isbn_13() is False

    assert __ISBNChecker('1-4129-4166-2').is_isbn_13() is True
    assert __ISBNChecker('0-306-40615-2').is_isbn_13() is True
    assert __ISBNChecker('1-4129-4166-2').is_isbn_13() is True

    assert __ISBNChecker('978-1-4129-4166-2').is_isbn_13() is True
    assert __ISBNChecker('1-4129-4166-2').is_isbn_13() is True


# Generated at 2022-06-14 05:39:08.394446
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    checker = __ISBNChecker('3836221195')
    assert checker.is_isbn_10() == True


# Generated at 2022-06-14 05:39:13.521441
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('192.168.1.1')
    assert not is_ip_v4('999')
    assert not is_ip_v4('hello')
    assert not is_ip_v4('192.168.1.300')
    assert not is_ip_v4('192.168.500.1')


# Generated at 2022-06-14 05:39:24.784623
# Unit test for function is_ip_v4
def test_is_ip_v4():
    # check that valid entries are considered valid
    assert is_ip_v4('6.45.234.9') == True
    assert is_ip_v4('255.0.0.0') == True
    assert is_ip_v4('0.0.0.0') == True
    assert is_ip_v4('1.1.1.1') == True
    assert is_ip_v4('123.123.123.123') == True
    assert is_ip_v4('192.168.1.1') == True

    # check that other entries are not considered valid
    assert is_ip_v4('255.200.100.999') == False
    assert is_ip_v4('nope') == False
    assert is_ip_v4('192.168.1') == False
    assert is_ip

# Generated at 2022-06-14 05:39:26.304710
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}')
    assert is_json('[1, 2, 3]')
    assert not is_json('{nope}')


# Generated at 2022-06-14 05:39:33.621966
# Unit test for function is_email
def test_is_email():
    assert is_email("k@gmail.com") == True
    assert is_email("abc123@vmail.com") == True
    assert is_email("a.b@gmail.com") == True
    assert is_email("a.b@gmail.com") == True
    assert is_email("abcd ppp@gmail.com") == True
    assert is_email("abc@gmail.com") == True
    assert is_email("abcd123@gmail.com") == True
    assert is_email("abcde12345@gmail.com") == True
    assert is_email("abcde12345@gmail.com") == True
    assert is_email("w.y@gmail.com") == True
    assert is_email("w.y.z@gmail.com") == True

# Generated at 2022-06-14 05:39:38.637933
# Unit test for function is_isbn
def test_is_isbn():
    assert not is_isbn('978-323-53')
    assert is_isbn('1593275846')
    assert is_isbn('9781593275844')
    assert not is_isbn('978 1593275844')
    assert is_isbn('9781593275844', normalize=False)


# noinspection PyPep8Naming

# Generated at 2022-06-14 05:39:44.929204
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com') == True
    assert is_email('@gmail.com') == False
    assert is_email('"hello there"@gmail.com') == True
    assert is_email('"hello there"@gmail.com') == True

# Test the case that email has a double quotes at the beginning and end but is surrounded by spaces

# Generated at 2022-06-14 05:39:58.529609
# Unit test for function is_ip
def test_is_ip():
    assert is_ip('47.10.0.0') is True
    assert is_ip('nope') is False
    assert is_ip('255.200.100.999') is False
    assert is_ip('2001:db8:85a3:0000:0000:8a2e:370:7334') is True
    assert is_ip('2001:db8:85a3:0000:0000:8a2e:370:?') is False
    assert is_ip('1.2.3') is False
test_is_ip()



# Generated at 2022-06-14 05:40:03.439445
# Unit test for function is_isbn
def test_is_isbn():
    assert is_isbn('978-84-376-0494-7') == True
    assert is_isbn('9780312498580') == True
    assert is_isbn('978-0312498580') == True
    assert is_isbn('1506715214') == True


# Generated at 2022-06-14 05:40:09.981006
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') # returns true
    assert is_json('[1, 2, 3]') # returns true
    assert not is_json('{nope}') # returns false
    
test_is_json()
# Function is_json passed test.



# Generated at 2022-06-14 05:40:23.033624
# Unit test for function is_palindrome
def test_is_palindrome():
    # return True if is a palindrome
    # return False if is not a palindrome
    assert is_palindrome('LOL') == True
    assert is_palindrome('Lol') == False
    assert is_palindrome('Lol', ignore_case=True) == True
    assert is_palindrome('ROTFL') == False

    # return True if is palindrome but with ignore_spaces
    # return False if is not a palindrome
    assert is_palindrome(' i topi non avevano nipoti', ignore_spaces=True) == True
    assert is_palindrome('i topi non avevano nipoti', ignore_spaces=True) == True
    assert is_palindrome('a man a plan a canal panama') == False
    assert is_pal

# Generated at 2022-06-14 05:40:28.403173
# Unit test for function is_credit_card
def test_is_credit_card():
    test_inputs = [
        # VISA
        '4111111111111111',
        '4012888888881881',
        '4222222222222',

        # MASTERCARD
        '5555555555554444',
        '5105105105105100',

        # AMERICAN EXPRESS
        '378282246310005',
        '371449635398431',

        # DINERS CLUB
        '30569309025904',
        '38520000023237',

        # DISCOVER
        '6011111111111117',
        '6011000990139424',

        # JCB
        '3530111333300000',
        '3566002020360505',
    ]

    for ti in test_inputs:
        assert is_credit_card(ti)

# Generated at 2022-06-14 05:40:38.030631
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker("0306406152").is_isbn_10() == True
    assert __ISBNChecker("0-306406-15-2").is_isbn_10() == True
    assert __ISBNChecker("0-306-40615-2").is_isbn_10() == True
    assert __ISBNChecker("0306406153").is_isbn_10() == False
    assert __ISBNChecker("0306406154").is_isbn_10() == False
    assert __ISBNChecker("0306406155").is_isbn_10() == False
    assert __ISBNChecker("0306406156").is_isbn_10() == False
    assert __ISBNChecker("0306406157").is_isbn_10() == False
    assert __ISBNChecker

# Generated at 2022-06-14 05:40:46.449061
# Unit test for function is_ip
def test_is_ip():
    assert is_ip('255.200.100.75') # returns true
    assert (is_ip('2001:db8:85a3:0000:0000:8a2e:370:7334')) # returns true
    assert (is_ip('1.2.3')) # returns false
test_is_ip()



# Generated at 2022-06-14 05:40:49.911190
# Unit test for function is_ip
def test_is_ip():
    assert is_ip('255.200.100.75') == True
    assert is_ip('2001:db8:85a3:0000:0000:8a2e:370:7334') == True
    assert is_ip('1.2.3') == False


# Generated at 2022-06-14 05:41:01.355341
# Unit test for function is_isbn
def test_is_isbn():
    assert is_isbn('9780312498580')
    assert is_isbn('978-0312498580')
    assert is_isbn('1506715214')
    assert is_isbn('150-6715214')

    assert not is_isbn('978-0312498580', normalize=False)
    assert not is_isbn('150-6715214', normalize=False)
    assert not is_isbn('Lorem !')
    assert not is_isbn('97803124985')
    assert not is_isbn('978-03124985')
    assert not is_isbn('150671521')
    assert not is_isbn('150-671521')



# Generated at 2022-06-14 05:41:16.181895
# Unit test for function is_palindrome
def test_is_palindrome():
    assert is_palindrome('abba') is True
    assert is_palindrome('abbA') is False
    assert is_palindrome('abba', ignore_case=True) is True
    assert is_palindrome('ab ba', ignore_spaces=True) is True
    assert is_palindrome('ab ba', ignore_case=True, ignore_spaces=True) is True
    assert is_palindrome('a', ignore_case=True, ignore_spaces=True) is True
    assert is_palindrome('abc') is False
    assert is_palindrome('aBba') is False
    assert is_palindrome('a BB a') is False
    assert is_palindrome('abba', True) is True
    assert is_palindrome('ab ba', ignore_case=True) is False
   

# Generated at 2022-06-14 05:41:36.067220
# Unit test for function is_email
def test_is_email():
    assert is_email('zhaogengliang@gmail.com')
    assert is_email('root@23.42.1.1')
    assert is_email('root@[23.42.1.1]')
    assert is_email('"this is"@gmail.com')
    assert is_email('foo.@gmail.com')
    assert is_email('foo@bar.baz')
    assert is_email('123@gmail.com')
    assert is_email('foo@gmail.com')
    assert is_email('zhaogengliang@googlemail.com')
    assert is_email('root@[127.0.0.1]')
    assert is_email('root@[127.0.0.1]')
    assert is_email('root@localhost')

# Generated at 2022-06-14 05:41:45.630021
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    def _test_isbn_13(expected: bool, input_string: str):
        assert bool(__ISBNChecker(input_string).is_isbn_13()) == expected

    _test_isbn_13(True, '978-3-16-148410-0')
    _test_isbn_13(True, '9783161484100')
    _test_isbn_13(True, '978-3-16-148410-0')
    _test_isbn_13(True, '9783161484100')
    _test_isbn_13(False, '978-3-16-148410-8')
    _test_isbn_13(False, '9783161484108')

# Generated at 2022-06-14 05:41:48.223353
# Unit test for function is_url
def test_is_url():
    url = 'http://www.mysite.com'
    assert is_url(url) is True


# Generated at 2022-06-14 05:41:59.493941
# Unit test for function is_credit_card
def test_is_credit_card():
    assert is_credit_card('4929379558465535') == True
    assert is_credit_card('4929379558465536') == False
    assert is_credit_card('4111111111111111') == True
    assert is_credit_card('4111111111111') == False
    assert is_credit_card('6011111111111117') == True
    assert is_credit_card('3530111333300000') == True
    assert is_credit_card('3566002020360505') == True
    assert is_credit_card('5555555555554444') == True
    assert is_credit_card('5105105105105100') == True
    assert is_credit_card('4111111111111111') == True
    assert is_credit_card('4012888888881881') == True

# Generated at 2022-06-14 05:42:02.025290
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75') == True
    assert is_ip_v4('nope') == False
    assert is_ip_v4('255.200.100.999') == False



# Generated at 2022-06-14 05:42:11.654085
# Unit test for function is_url
def test_is_url():
    assert is_url(None) == False
    assert is_url('') == False
    assert is_url(' ') == False
    assert is_url('www.mysite.com') == False
    assert is_url('http://mysite.com') == True
    assert is_url('https://mysite.com') == True
    assert is_url('hppts://mysite.com') == False
    assert is_url('http://www.mysite.com') == True
    assert is_url('https://www.mysite.com') == True
    assert is_url('hppts://www.mysite.com') == False
    assert is_url('http://www.mysite.com/') == True
    assert is_url('https://www.mysite.com/') == True

# Generated at 2022-06-14 05:42:20.364498
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') is True
    assert is_json('[1, 2, 3]') is True
    assert is_json('{"name":"Peter"}') is True
    assert is_json('[1,2,3]') is True
    assert is_json('{nope}') is False
    assert is_json('[1, 2, 3') is False
    assert is_json('{"name":"Peter"') is False


# Generated at 2022-06-14 05:42:24.077567
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75') == True
    assert is_ip_v4('nope') == False
    assert is_ip_v4('255.200.100.999') == False


# Generated at 2022-06-14 05:42:36.191033
# Unit test for function is_credit_card
def test_is_credit_card():
    assert is_credit_card('4242424242424242') == True
    assert is_credit_card('5555555555554444') == True
    assert is_credit_card('378282246310005') == True
    assert is_credit_card('371449635398431') == True
    assert is_credit_card('6011111111111117') == True
    assert is_credit_card('3530111333300000') == True
    assert is_credit_card('5105105105105100') == True
    assert is_credit_card('4111111111111111') == True
    assert is_credit_card('6011000990139424') == True
    assert is_credit_card('4263982640269299') == True



# Generated at 2022-06-14 05:42:39.243068
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com') == True
    assert is_email('@gmail.com') == False


# Generated at 2022-06-14 05:42:52.343213
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4("255.200.100.75")
    assert not is_ip_v4("nope")
    assert not is_ip_v4("255.200.100.999")
    print("is_ip_v4() function passed unit testing succesfully!")

test_is_ip_v4()


# Generated at 2022-06-14 05:43:03.513312
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com')
    assert is_email('my.email@big.provider.com')
    assert is_email('my.email+(something)@gmail.com')
    assert is_email('test@test.test')
    assert is_email("test\\s@test.test")
    assert is_email("\"test\"@test.test")
    assert not is_email('@gmail.com')
    assert not is_email('foo@')
    assert not is_email('foo')
    assert not is_email('.foo@gmail.com')
    assert not is_email('foo@.gmail.com')
    assert not is_email('foo@gmail..com')
    assert not is_email('foo+gmail.com')

# Generated at 2022-06-14 05:43:07.572843
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') # returns true
    assert is_json('[1, 2, 3]') # returns true
    assert is_json('{nope}') == False # returns false



# Generated at 2022-06-14 05:43:15.294651
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com') == True
    assert is_email('@gmail.com') == False
    assert is_email('my.email@') == False
    assert is_email('.my.email@the-provider.com') == False
    assert is_email('"my.email"@the-provider.com') == True
    assert is_email('my.email@the-provider.com ') == False
    assert is_email(' my.email@the-provider.com') == False
    assert is_email('my email@the-provider.com') == False
    assert is_email('my.email@the provider.com') == False
    assert is_email('my.email@the.provider.com') == True

# Generated at 2022-06-14 05:43:28.115335
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com')
    assert is_email('my_email@the-provider.com')
    assert is_email('myemail@the-provider.com')
    assert not is_email(' @gmail.com')
    assert not is_email('@gmail.com')
    assert not is_email('@.com')
    assert not is_email('@gmail')
    assert not is_email('@')
    assert not is_email('gmail.com')
    assert not is_email('my.email')
    assert not is_email('my.email@')
    assert not is_email('my.email@gmail')
    assert not is_email('my.email.gmail.com')
    assert not is_email('my.email@gmail.com.')

# Generated at 2022-06-14 05:43:32.508345
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') == True
    assert is_json('[1, 2, 3]') == True
    assert is_json('{nope}') == False
    assert is_json(123) == False
    assert is_json(None) == False
    assert is_json('') == False


# Generated at 2022-06-14 05:43:37.786262
# Unit test for function is_email
def test_is_email():
    assert is_email('a@a.com') == True
    assert is_email('a.a.com') == False
    assert is_email('a@a') == False


# Generated at 2022-06-14 05:43:49.912553
# Unit test for function is_email

# Generated at 2022-06-14 05:43:55.273916
# Unit test for function is_json
def test_is_json():
    print(is_json('{"name": "Peter"}'))
    print(is_json('[1, 2, 3]'))
    print(is_json('{nope}'))
    print(is_json(''))

test_is_json()



# Generated at 2022-06-14 05:44:06.811887
# Unit test for function is_json
def test_is_json():
    assert is_json(' {"name": "Peter"}') == False  
    assert is_json('') == False
    assert is_json('{"name": "Peter"') == False
    assert is_json('{"name": "Peter"}') == True
    assert is_json('{"name": "Peter", "age": 40}') == True
    assert is_json('[1, 2, 3]') == True
    assert is_json('[{"name": "Peter", "age": 40}, {"name": "John", "age":  36}]') == True
    assert is_json('{"name": "Peter", "age": "40"}') == True
    assert is_json('{"name": "Peter", "age": 40.0}') == True
    assert is_json('{"name": ["foo", "bar"], "age": 40}')

# Generated at 2022-06-14 05:44:15.826612
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    checker = __ISBNChecker('978-0-306-40615-7')

    assert checker.is_isbn_13() == True

    checker = __ISBNChecker('978-0-306-40615-8')

    assert checker.is_isbn_13() == False

# Generated at 2022-06-14 05:44:28.721701
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com')
    assert not is_email('@gmail.com')
    assert is_email('email.with.long.name@the-provider.com')
    assert is_email('email.with.long.name.agg@the-provider.com')
    assert is_email('my.email.with.long.name@the-provider.com')
    assert is_email('my.email.with.long.name.agg@the-provider.com')
    assert is_email('my.email.with.long.name.agg@the-provider.com')
    assert not is_email('my.email.with.long.name.agg@the-provider.com.')


# Generated at 2022-06-14 05:44:31.127576
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('192.168.1.1') == True
    assert is_ip_v4('255.200.100.75') == True
    assert is_ip_v4('255.200.100.999') == False
    assert is_ip_v4('nope') == False
    return "Unit test for function is_ip_v4 PASSED"
# Test it
test_is_ip_v4()


# Generated at 2022-06-14 05:44:37.202518
# Unit test for function is_email
def test_is_email():
    assert is_email('test@test.com') == True
    assert is_email('te.s.t@test.com') == True
    assert is_email('tes.t@test.c.om') == True
    assert is_email('tes.t@test.com') == True
    assert is_email('tes.t@test..com') == False
    assert is_email('tes.t@.test.com') == False
    assert is_email('tes.t@test.com.') == False
    assert is_email('tes.t@test..com') == False
    assert is_email('test@test.com') == True



# Generated at 2022-06-14 05:44:41.436903
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') == True, 'The value is not json'
    assert is_json('[1, 2, 3]') == True, 'The value is not json'
    assert is_json('{nope}') == False, 'The value is not json'
    
    
    


# Generated at 2022-06-14 05:44:47.556812
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
        assert __ISBNChecker('078-0-470-84328-0').is_isbn_10() == True
        assert __ISBNChecker('078-0-470-84328-1').is_isbn_10() == False


# Generated at 2022-06-14 05:44:56.819346
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker('1234567892').is_isbn_10() == True
    assert __ISBNChecker('1234567893').is_isbn_10() == False
    assert __ISBNChecker('123456789X').is_isbn_10() == True
    assert __ISBNChecker('123456789x').is_isbn_10() == True
    assert __ISBNChecker('123456-7892').is_isbn_10() == True
    assert __ISBNChecker('1234567-892').is_isbn_10() == True

test___ISBNChecker_is_isbn_10()


# PUBLIC API



# Generated at 2022-06-14 05:45:00.917719
# Unit test for function is_credit_card
def test_is_credit_card():
    assert(is_credit_card('4007000000027') == True)
    assert(is_credit_card('5412345678901234') == True)



# Generated at 2022-06-14 05:45:12.416927
# Unit test for function is_email
def test_is_email():
    assert is_email('jason@lobsterink.com') == True
    assert is_email('jason.li@lobsterink.com') == True
    assert is_email('jason@lobster-ink.com') == True
    assert is_email('jason@lobster_ink.com') == True
    assert is_email('j@s.s') == True
    assert is_email('abc@abc.abc') == True

    assert is_email('.jason@lobsterink.com') == False
    assert is_email('jason@') == False
    assert is_email('jason@lobster-ink') == False
    assert is_email('jason@lobsterink') == False
    assert is_email('jason @lobsterink.com') == False

# Generated at 2022-06-14 05:45:26.767117
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com') == True
    assert is_email('@gmail.com') == False
    assert is_email('     ') == False
    assert is_email('') == False
    assert is_email('1') == False
    assert is_email('abcdefghijklmnopqrstuvwxyz') == False
    assert is_email('abcdefghijklmnopqrstuvwxyz@gmail.com') == True
    assert is_email('abcdefghijklmnopqrstuvwxyz0@gmail.com') == True
    assert is_email('0123456789@gmail.com') == True
    assert is_email('01234567890@gmail.com') == True

# Generated at 2022-06-14 05:45:45.786825
# Unit test for function is_email
def test_is_email():
    # assert is_email('my.email@the-provider.com') is True
    assert is_email('myemail@the-provider.com') is True
    assert is_email('my.email+foo@the-provider.com') is True
    assert is_email('myemail@abc.example.com') is True
    assert is_email('myemail@example.com') is True
    assert is_email('help@example.co.in') is True
    assert is_email('help@example.cloud') is True
    assert is_email('myemail+foo@gmail.com') is True
    assert is_email('hello@.com') is False
    assert is_email('.hello@gmail.com') is False
    assert is_email('my..email@gmail.com') is False

# Generated at 2022-06-14 05:45:50.058170
# Unit test for function is_ip_v4
def test_is_ip_v4():
    
    # Unit test for function is_ip_v4
    assert is_ip_v4('255.200.100.75')
    assert not (is_ip_v4('nope'))
    assert not (is_ip_v4('255.200.100.999'))


# Generated at 2022-06-14 05:46:00.821628
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker('0316543187').is_isbn_10() is True # 0+3+1+6+5+4+3+1+8+7=37
    assert __ISBNChecker('0316543188').is_isbn_10() is False # 0+3+1+6+5+4+3+1+8+8=38
    assert __ISBNChecker('1-56619-909-3').is_isbn_10() is True # 1+5+6+6+1+9+9+0+9+3=54
    assert __ISBNChecker('1-56619-909-4').is_isbn_10() is False # 1+5+6+6+1+9+9+0+9+4=55


# Generated at 2022-06-14 05:46:05.004575
# Unit test for function is_json
def test_is_json():
    assert is_json("{\"name\": \"Peter\"}") == True
    assert is_json("[1, 2, 3]") == True
    assert is_json("{nope}") == False



# Generated at 2022-06-14 05:46:17.320324
# Unit test for function is_credit_card
def test_is_credit_card():
    """
    test if function is_credit_card.
    """
    assert is_credit_card('378282246310005', card_type='AMERICAN_EXPRESS') == True
    assert is_credit_card('378282246310005', card_type='MASTERCARD') == False
    assert is_credit_card('378282246310005') == True
    assert is_credit_card('371449635398431', card_type='AMERICAN_EXPRESS') == True
    assert is_credit_card('371449635398431', card_type='MASTERCARD') == False
    assert is_credit_card('371449635398431') == True
    assert is_credit_card('378734493671000', card_type='AMERICAN_EXPRESS') == False

# Generated at 2022-06-14 05:46:24.192751
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker('1234567890123').is_isbn_13()
    assert __ISBNChecker('978-150325034').is_isbn_13()

    assert not __ISBNChecker('123456789012').is_isbn_13()
    assert not __ISBNChecker('978-150325033').is_isbn_13()

    assert not __ISBNChecker('A234567890123').is_isbn_13()
    assert not __ISBNChecker('978-15032503A').is_isbn_13()

# Generated at 2022-06-14 05:46:34.582780
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com') == True
    assert is_email('@gmail.com') == False
    assert is_email('my.email.@the-provider.com') == False
    assert is_email('my.email@the-provider.com:') == False
    assert is_email('my.email@the-provider.com:8080') == False
    assert is_email('my.email@the-provider.com?hi=hi') == False
    assert is_email('my.email@the-provider.com.com') == True

# Generated at 2022-06-14 05:46:40.044579
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('1.1.1.1') == True
    assert is_ip_v4('255.200.100.75') == True
    assert is_ip_v4('nope') == False
    assert is_ip_v4('255.200.100.999') == False



# Generated at 2022-06-14 05:46:44.433864
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75')
    assert not is_ip_v4('nope')
    assert not is_ip_v4('255.200.100.999')
    print('Tested function is_ip_v4 !')


# Generated at 2022-06-14 05:46:57.440486
# Unit test for function is_ip_v4
def test_is_ip_v4(): 
    assert is_ip_v4('127.1.1.1') == True
    assert is_ip_v4('111111') == False
    assert is_ip_v4('192.168.1.1') == True
    assert is_ip_v4('192.168.1.1.') == False
    assert is_ip_v4('333.333.333.333') == False
    assert is_ip_v4('192.168.1') == False
    assert is_ip_v4('192.168.1.1.1.1') == False
    assert is_ip_v4('65535') == False
    assert is_ip_v4('40.1.1.1') == True
    
    
    


# Generated at 2022-06-14 05:47:13.866143
# Unit test for function is_email
def test_is_email():
    assert is_email('joe@example.com') == True
    assert is_email('JOE@example.com') == True
    assert is_email('joe@EXAMPLE.COM') == True
    assert is_email('joe123@example.com') == True
    assert is_email('joe.123@example.com') == True
    assert is_email('joe.123@example.sub.com') == True
    assert is_email('123@example.com') == True
    assert is_email('joe+123@example.com') == True
    assert is_email('joe-123@example.com') == True
    assert is_email('joe_123@example.com') == True
    assert is_email('joe!123@example.com') == True

# Generated at 2022-06-14 05:47:25.125665
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com')
    assert not is_email('@gmail.com')
    assert is_email('user@domain.tld')
    assert is_email('user@domain.tld')
    assert is_email('user@domain.tld')
    assert is_email('user@domain.tld')
    assert is_email('user@domain.tld')
    assert is_email('user@domain.tld')
    assert is_email('user@domain.tld')
    assert is_email('user@domain.tld')
    assert is_email('user@domain.tld')
    assert is_email('user@domain.tld')
    assert is_email('user@domain.tld')
    assert is_email('user@domain.tld')


# Generated at 2022-06-14 05:47:35.487960
# Unit test for function is_email
def test_is_email():
    # some valid emails
    assert is_email('info@example.com')
    assert is_email('my.example@gmail.com')
    assert is_email('me@example.com')
    assert is_email('"me@example.com"')
    # some invalid emails
    assert not is_email(None)
    assert not is_email('example@gmail')
    assert not is_email('')
    assert not is_email(' ')
    assert not is_email('info@example.com ')
    assert not is_email('info@example .com')
    assert not is_email('info @example.com')
    assert not is_email('info@example .com')
    # borderline cases
    assert not is_email('."me@example.com"')

# Generated at 2022-06-14 05:47:41.002818
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75')
    assert not is_ip_v4('nope')
    assert not is_ip_v4('255.200.100.999')

# Dataframe
df['ip_v4'] = df['ip_address'].apply(is_ip_v4)


# Generated at 2022-06-14 05:47:45.577157
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    checker = __ISBNChecker('978-1-84354-451-8')
    assert checker.is_isbn_10() is False

    checker = __ISBNChecker('1-843-54451-8')
    assert checker.is_isbn_10() is True


# PUBLIC API



# Generated at 2022-06-14 05:47:54.349792
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker('0-306-40615-2').is_isbn_10()
    assert __ISBNChecker('0-7434-7696-3').is_isbn_10()
    assert __ISBNChecker('0-393-04002-6').is_isbn_10()
    assert __ISBNChecker('0-375-70386-1').is_isbn_10()
    assert __ISBNChecker('0-385-47897-8').is_isbn_10()
    assert __ISBNChecker('0-385-35626-2').is_isbn_10()
    assert __ISBNChecker('0-385-49209-6').is_isbn_10()
    assert __ISBNChecker('0-449-00194-2').is_isbn_

# Generated at 2022-06-14 05:47:57.957575
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75')
    assert is_ip_v4('255.0.0.0')
    assert not is_ip_v4('nope')
    assert not is_ip_v4('255.200.100.999')



# Generated at 2022-06-14 05:47:58.858751
# Unit test for function is_email
def test_is_email():
    pass



# Generated at 2022-06-14 05:48:11.103528
# Unit test for function is_email
def test_is_email():
    assert is_email('w@w.com') == True
    assert is_email('"\\ w"@w.com') == True
    assert is_email('w\\ w@w.com') == True
    assert is_email('w\\@w@w.com') == True
    assert is_email('w@w.com') == True
    assert is_email('w@w..com') == False
    assert is_email('w@w.com.') == False
    assert is_email('w@w.com\\') == False
    assert is_email('.w@w.com') == False
    assert is_email('w@w.comcom') == False
    assert is_email('w@w..com') == False
    assert is_email('w@w.com...') == False

# Generated at 2022-06-14 05:48:21.735123
# Unit test for function is_email
def test_is_email():
    assert is_email("testMailId@gmail.com") == True
    assert is_email("testmailid@gmail.com") == True
    assert is_email("testmailid@gmail.co.uk") == True
    assert is_email("testmailid@gmail.co.in") == True
    assert is_email("testmailid@rediffmail.com") == True
    assert is_email("testmailid@yahoo.com") == True
    assert is_email("testmailid@yahoo.co.in") == True
    assert is_email("testmailid@yahoo.co.uk") == True
    assert is_email("testmailid@hotmail.com") == True
    assert is_email("testmailid@hotmail.co.in") == True