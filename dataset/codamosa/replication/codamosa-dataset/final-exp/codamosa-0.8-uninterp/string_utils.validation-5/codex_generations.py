

# Generated at 2022-06-14 05:38:56.515776
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker('9176378699').is_isbn_10() == True
    assert __ISBNChecker('9176378699').is_isbn_10() == True
    assert __ISBNChecker('0195153448').is_isbn_10() == True
    assert __ISBNChecker('0374257064').is_isbn_10() == True
    assert __ISBNChecker('0345340777').is_isbn_10() == True
    assert __ISBNChecker('1590171312').is_isbn_10() == True


# Generated at 2022-06-14 05:39:02.049339
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}')  # returns true
    assert is_json('[1, 2, 3]')  # returns true
    assert not is_json('{nope}')  # returns false
    assert not is_json(None)
    assert not is_json(False)
    assert not is_json(True)


# Generated at 2022-06-14 05:39:08.544073
# Unit test for function is_ip
def test_is_ip():
    x = is_ip("192.168.100.1")
    y = is_ip("2001:db8:85a3:0000:0000:8a2e:370:7334")
    assert x == True
    assert y == True
test_is_ip()



# Generated at 2022-06-14 05:39:13.678492
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert(is_ip_v4('255.200.100.75') == True)
    assert(is_ip_v4('nope') == False)
    assert(is_ip_v4('255.200.100.999') == False)
    assert(is_ip_v4('255.200.100') == False)
    
    

# Generated at 2022-06-14 05:39:19.290997
# Unit test for function is_isbn
def test_is_isbn():
    assert is_isbn("9780312498580", normalize=True) == True
    assert is_isbn("1506715214", normalize=True) == True
    assert is_isbn("5-547-55012-5", normalize=True) == True


# Generated at 2022-06-14 05:39:24.336859
# Unit test for function is_decimal
def test_is_decimal():
    assert is_decimal('42.0')
    assert is_decimal('42') == False
    assert is_decimal('42,0') == False


# Generated at 2022-06-14 05:39:27.584831
# Unit test for function is_json
def test_is_json():
    assert is_json("[1, 2, 3, 4]") == True
    assert is_json("{'name': 'Peter'}") == True
    assert is_json("{1: 'Peter'}") == False
    assert is_json("hello") == False
    assert is_json("") == False
    assert is_json(" ") == False
    
test_is_json()


# Generated at 2022-06-14 05:39:32.176834
# Unit test for function is_url
def test_is_url():
    print(is_url('http://www.mysite.com')) # returns true
    print(is_url('https://mysite.com')) # returns true
    print(is_url('.mysite.com')) # returns false
test_is_url()


# Generated at 2022-06-14 05:39:36.630591
# Unit test for function is_json
def test_is_json():
    assert not is_json(b'{"name": "Peter"}')
    assert not is_json(123)
    assert not is_json('')
    assert not is_json('{nope}')
    assert not is_json('[1, 2, 3')
    assert not is_json('name": "Peter"}')

    assert is_json('{"name": "Peter"}')
    assert is_json('[1, 2, 3]')
    assert is_json('{"name": "Peter"')
    assert is_json('[1, 2, 3')

test_is_json()



# Generated at 2022-06-14 05:39:42.292763
# Unit test for function is_ip
def test_is_ip():
    assert is_ip('255.200.100.75') == True
    assert is_ip('2001:db8:85a3:0000:0000:8a2e:370:7334') == True
    assert is_ip('1.2.3') == False


# Generated at 2022-06-14 05:40:00.303888
# Unit test for function is_credit_card
def test_is_credit_card():
    assert is_credit_card("4062901840") # VISA: valid
    assert is_credit_card("5555555555554444") # MASTERCARD: valid
    assert is_credit_card("378282246310005") # AMERICAN_EXPRESS: valid
    assert is_credit_card("30569309025904") # DINERS_CLUB: valid
    assert is_credit_card("6011111111111117") # DISCOVER: valid
    assert is_credit_card("3530111333300000") # JCB: valid
    assert not is_credit_card("371449635398431") # AMEX: not valid
    assert not is_credit_card("123456789") # VISA: not not valid

# Generated at 2022-06-14 05:40:13.465814
# Unit test for function is_email
def test_is_email():
    assert(is_email('my.email@the-provider.com')==True)
    #assert(is_email('@gmail.com') == False)
    assert (is_email('xxx@yyy.zzz') == True)
    assert (is_email('xxx@yyy.zz') == False)
    assert (is_email('xxx@yyy.zzzz') == True)
    #assert (is_email('xxx@yyy.zzzzz') == False)
    assert (is_email('email@example.com') == True)
    assert (is_email('firstname.lastname@example.com') == True)
    assert (is_email('email@subdomain.example.com') == True)
    assert (is_email('email@123.123.123.123') == True)

# Generated at 2022-06-14 05:40:20.596711
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com')  # returns true
    assert is_email('@gmail.com')  # returns false
    assert is_email('my.email@the-provider.com')  # returns true
    assert is_email('john.doe@cool-provider.io')  # returns true
    assert is_email('john.doe@cool-provider.io')  # returns true
    assert not is_email('@gmail.com')  # returns false
    assert not is_email('john..doe@gmail.com')  # returns false
    assert not is_email('john.doe@gmail.com.')  # returns false
    assert not is_email('john.doe@gmail.com\ ')  # returns false

# Generated at 2022-06-14 05:40:24.117229
# Unit test for function is_url
def test_is_url():
    assert is_url('https://www.mysite.com') == True
    assert is_url('http://www.mysite.com') == True
    assert is_url('https://mysite.com') == True
    assert is_url('.mysite.com') == False

# Generated at 2022-06-14 05:40:29.662589
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com') == True
    assert is_email('.my.email@the-provider.com') == False
    assert is_email('my.email@the-provider.com.') == False
    assert is_email('my.email@the-provider.com..') == False

# Generated at 2022-06-14 05:40:43.165211
# Unit test for function is_email
def test_is_email():
    assert not is_email('example.com')
    assert not is_email('@example.com')
    assert is_email('\"Abc\@def\"@example.com')
    assert not is_email('\"A@b\@c\"@example.com')
    assert is_email('\"Abc@def\"@example.com')
    assert is_email('\Aabc\"def\@example.com')
    assert not is_email('abc\@def@example.com')
    assert not is_email('abc\@example.com')
    assert is_email('a"b(c)d,e:f;gi[j\\k]l@example.com')
    assert is_email('just"not"right@example.com')
    assert is_email('this is"not\\allowed@example.com')


# Generated at 2022-06-14 05:40:44.943257
# Unit test for function is_email
def test_is_email():
    return is_email('user@example.com')
# Unit test execution
test_is_email()


# Generated at 2022-06-14 05:40:55.013118
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com') == True
    assert is_email('my.email@the-provider.com,') == False
    assert is_email('my.email@the-provider.com\n') == False
    assert is_email('my.email@the-provider.com.') == False
    assert is_email('my.email@the-provider.com,') == False
    assert is_email('"my.email"@the-provider.com') == True
    assert is_email('') == False
    assert is_email(' ') == False
    assert is_email('.') == False
    assert is_email('.@gmail.com') == False
    assert is_email('1@gmail.com') == True

# Generated at 2022-06-14 05:41:03.952732
# Unit test for function is_email
def test_is_email():
    # it should pass if the email is not empty and contains an @ sign
    assert is_email('hello@gmail.com')
    assert is_email('hello.world.again@gmail.com')
    assert is_email('hello.world.again@gmail.com')
    assert is_email('"spaces are allowed if quoted"@gmail.com')

    # it should pass if we have escaped spaces (\ )
    assert is_email('hello.world\\ again@gmail.com')
    assert is_email('"escaped\\ spaces\\ are\\ allowed"@gmail.com')

    # it should pass if we have multiple @ signs, but only in the header (escaped)
    assert is_email('hello\\@world@gmail.com')
    assert is_email('"hello\\@world"@gmail.com')

    # it should pass if

# Generated at 2022-06-14 05:41:08.601951
# Unit test for function is_url
def test_is_url():
    assert is_url('http://www.mysite.com') # returns true
    assert is_url('https://mysite.com') # returns true
    assert not is_url('http://mysite') # returns false



# Generated at 2022-06-14 05:41:26.249655
# Unit test for function is_json
def test_is_json():
    assert is_json('{"a": "b"}')
    assert is_json('{"a": "b", "c": [1, 2, 3]}')
    assert is_json('{}')
    assert is_json('[]')
    assert is_json(r'{"a": "\b"}')
    assert is_json('{}')
    assert is_json('[{"a": "a"}, {"b": "b"}]')
    assert is_json('[{"a": "a"}, {"b": "b"}, {}]')
    assert not is_json('')
    assert not is_json('{"nope": "nope"')
    assert not is_json('{"nope: "nope"}')
    assert not is_json('{nope: "nope"}')
test_is_json()



# Generated at 2022-06-14 05:41:31.715307
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}')
    assert is_json('[1, 2, 3]')
    assert is_json('{nope}')
    assert not is_json('{nope')
    assert not is_json('nope}')
    assert not is_json('nope')


# Generated at 2022-06-14 05:41:34.660640
# Unit test for function is_url
def test_is_url():
    assert is_url('http://www.google.com')
    assert not is_url('google.com')


# Generated at 2022-06-14 05:41:37.676499
# Unit test for function is_json
def test_is_json():
    assert is_json('[1,2,3]')
    assert is_json('[1,2,3]')
    assert not is_json('[{}]')
    assert not is_json('[]')


# Generated at 2022-06-14 05:41:41.074668
# Unit test for function is_json
def test_is_json():
	assert is_json('{"name": "Peter"}') == True
	assert is_json('[1, 2, 3]') == True
	assert is_json('{nope}') == False


# Generated at 2022-06-14 05:41:53.973067
# Unit test for function is_url
def test_is_url():
    assert is_url('http://stackoverflow.com/questions/35727696/how-to-write-unittest-for-a-function-whose-return-value-is-a-boolean') == True
    assert is_url('https://stackoverflow.com/questions/35727696/how-to-write-unittest-for-a-function-whose-return-value-is-a-boolean') == True
    assert is_url('ftp://stackoverflow.com/questions/35727696/how-to-write-unittest-for-a-function-whose-return-value-is-a-boolean') == True

# Generated at 2022-06-14 05:42:02.582257
# Unit test for function is_url
def test_is_url():
    assert(is_url('http://www.mysite.com') == True)
    assert(is_url('https://mysite.com') == True)
    assert(is_url('ftp://www.mysite.com') == True)
    assert(is_url('.mysite.com') == False)
    assert(is_url('mysite.com/') == False)
    assert(is_url('mysite.com/faq') == False)
    assert(is_url('www.mysite.com') == False)
    assert(is_url('www.mysite.com:8080') == False)
    assert(is_url('www.mysite.com:8080/faq') == False)

# Generated at 2022-06-14 05:42:08.882173
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com')
    assert is_email('my-email@the-provider.com')
    assert is_email('my_email@the-provider.com')
    assert is_email('my-email@the_provider.com')
    assert not is_email('my_email@the_provider.com')
    assert not is_email('@gmail.com')

# '

# Generated at 2022-06-14 05:42:21.542803
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    # Test for empty input
    try:
        __ISBNChecker('').is_isbn_10()
    except InvalidInputError as e:
        assert isinstance(e, InvalidInputError)
    else:
        raise AssertionError("Not raise an InvalidInputError")
    # Test for invalid input
    try:
        __ISBNChecker('a').is_isbn_10()
    except InvalidInputError as e:
        assert isinstance(e, InvalidInputError)
    else:
        raise AssertionError("Not raise an InvalidInputError")
    # Test for correct input
    assert __ISBNChecker('0-306-40615-2').is_isbn_10()
    assert __ISBNChecker('0306406152').is_isbn_10()

# Generated at 2022-06-14 05:42:33.466089
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com')
    assert is_email('my.email@the-provider.com')
    assert is_email('my.email@the-provider.com')
    assert is_email('gil@example.com')
    assert is_email('gilma.rodriguez@example.com')
    assert is_email('gilma.rodriguez-f@example.com')
    assert is_email('gilma.rodriguez_f@example.com')
    assert is_email('gilma.rodriguez-f-j@example.com')
    assert is_email('gilma.rodriguez_f.j@example.com')
    assert is_email('gilma-rodriguez@example.com')

# Generated at 2022-06-14 05:42:42.386829
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    checker = __ISBNChecker('9788176298818')
    assert checker.is_isbn_13() is True


# Generated at 2022-06-14 05:42:55.429623
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com') == True
    assert is_email('@gmail.com') != True
    assert is_email('.@gmail.com') != True
    assert is_email('me@gmail.com') == True
    assert is_email('me.@gmail.com') != True
    assert is_email('me..mm@gmail.com') != True
    assert is_email('me@gmail..com') != True
    assert is_email('me@gmail.c.om') == True
    assert is_email('me@gmail.c.om.') != True
    assert is_email('me@gmail.c.om..') != True
    assert is_email('me@gmail.') != True
    assert is_email('.me@gmail.com') != True
    assert is_

# Generated at 2022-06-14 05:43:05.441004
# Unit test for function is_email
def test_is_email():
    assert not is_email('')
    assert not is_email(' ')
    assert not is_email(':')
    assert is_email('my.email@the-provider.com')
    assert is_email('email@gmail.com')
    assert is_email('a.little.lengthy.but.fine@dept.example.com')
    assert is_email('niceandsimple@example.com')
    assert is_email('disposable.style.email.with+symbol@example.com')
    assert is_email('!#$%&*+-/=?^_`{}|~@example.org')
    assert is_email('!#$%&*+-/=?^_`{}|~@gmail.com')

# Generated at 2022-06-14 05:43:09.794828
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert True == __ISBNChecker('9783161484100').is_isbn_13()
    assert False == __ISBNChecker('978316148410').is_isbn_13()
    assert False == __ISBNChecker('978316148410x').is_isbn_13()


# Generated at 2022-06-14 05:43:16.308908
# Unit test for function is_credit_card
def test_is_credit_card():
    assert not is_credit_card("")
    assert not is_credit_card("1")
    assert not is_credit_card("13")
    assert not is_credit_card("111")
    assert is_credit_card("4111-1111-1111-1111")
    assert is_credit_card("4111 1111 1111 1111")
    assert not is_credit_card("4111111111111111")
    assert not is_credit_card("4111-1111-1111-1111a")
    assert not is_credit_card("4111-1111-1111-a111")
    assert is_credit_card("5500 0000 0000 0004")
    assert is_credit_card("5500 0000 0000 0004")
    assert is_credit_card("6011 0000 0000 0004")
    assert is_credit_card("6011 0000 0000 0004")


# Generated at 2022-06-14 05:43:21.640789
# Unit test for function is_email
def test_is_email():
    assert is_email('bob@example.com')
    assert is_email('bob@example.com')
    assert is_email('Bob O\'brien <bob@example.com>')
    assert is_email('bob.o\'brien+tag@example.com')
    assert is_email('bob.o\'brien+tag@example.com')
    assert is_email('"bob"+tag@example.com')
    assert is_email('"bob o\'brien"@example.com')
    assert is_email('bob+"."+o\'brien@example.com')
    assert is_email('bob@example.co.uk')
    assert is_email('bob@example.com')
    assert is_email('bob@example.museum')

# Generated at 2022-06-14 05:43:26.402506
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com') == True
    assert is_email('my.emailthe-provider.com') == False
    assert is_email('@gmail.com') == False
    assert is_email('my.email@gmail.com') == True
    assert is_email('"my.email"@gmail.com') == True


# Generated at 2022-06-14 05:43:30.805705
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker('9784873117584').is_isbn_13()
    assert not __ISBNChecker('9784873117585').is_isbn_13()



# Generated at 2022-06-14 05:43:33.228913
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker('123456789X').is_isbn_10()

# Generated at 2022-06-14 05:43:46.580666
# Unit test for function is_credit_card
def test_is_credit_card():
    assert is_credit_card("6011111111111117")
    assert is_credit_card("341111111111111")
    assert is_credit_card("340000000000009")
    assert is_credit_card("5500000000000004")
    assert is_credit_card("6011000000000004")
    assert is_credit_card("3096000000000009")
    assert is_credit_card("6011000000000004")
    assert is_credit_card("3566002020360505")
    assert is_credit_card("3530111333300000")
    assert is_credit_card("4111111111111111")
    assert is_credit_card("4917485729304")
    assert is_credit_card("4111111111111111")
    assert is_credit_card("4917485729304")

# Generated at 2022-06-14 05:44:02.981745
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker('9780451498230').is_isbn_13() is True
    assert __ISBNChecker('978045149823').is_isbn_13() is False
    assert __ISBNChecker('978045149823x').is_isbn_13() is False
    assert __ISBNChecker('9780451498231').is_isbn_13() is False
    assert __ISBNChecker('4780451498230').is_isbn_13() is False
    assert __ISBNChecker('97804514982300').is_isbn_13() is False
    assert __ISBNChecker('9780451498230000').is_isbn_13() is False


# Generated at 2022-06-14 05:44:06.623993
# Unit test for function is_credit_card
def test_is_credit_card():
    input_string = '4111111111111111'
    card_type = 'VISA'
    output = is_credit_card(input_string, card_type)
    expected =  True
    assert output == expected
test_is_credit_card()

# Generated at 2022-06-14 05:44:18.079989
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker('978-3-16-148410-0').is_isbn_13() is True
    assert __ISBNChecker('9783161484100').is_isbn_13() is True
    assert __ISBNChecker('9783161484100', normalize=False).is_isbn_13() is True
    assert __ISBNChecker('979-316-148-410-0').is_isbn_13() is True
    assert __ISBNChecker('97931614841000').is_isbn_13() is True
    assert __ISBNChecker('97931614841000', normalize=False).is_isbn_13() is True
    assert __ISBNChecker('978-3-16-148410-1').is_isbn_13() is False

# Generated at 2022-06-14 05:44:21.200791
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}')
    assert is_json('[1, 2, 3]')
    assert not is_json('{nope}')



# Generated at 2022-06-14 05:44:23.482015
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    checker = __ISBNChecker('123456789')
    assert checker.is_isbn_10() is True



# Generated at 2022-06-14 05:44:27.716806
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4("255.200.100.75") == True
    assert is_ip_v4("nope") == False
    assert is_ip_v4("255.200.100.999") == False

test_is_ip_v4()


# Generated at 2022-06-14 05:44:31.952303
# Unit test for function is_email
def test_is_email():
    assert is_email('example@email.com')
    assert not is_email('example@email.com')
    assert is_email('example@email.com')
    assert not is_email('example@email.com')

# Generated at 2022-06-14 05:44:38.221508
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker('0-321-14653-0').is_isbn_13()
    assert __ISBNChecker('9669469324548').is_isbn_13()
    assert __ISBNChecker('1234567890123').is_isbn_13() is False
    assert __ISBNChecker('0-321-14653-*').is_isbn_13() is False


# Generated at 2022-06-14 05:44:49.256580
# Unit test for function is_credit_card
def test_is_credit_card():
    assert is_credit_card("4111111111111111")
    assert is_credit_card("4012888888881881")
    assert is_credit_card("5555555555554444")
    assert is_credit_card("5105105105105100")
    assert is_credit_card("378282246310005")
    assert is_credit_card("371449635398431")
    assert is_credit_card("6011111111111117")
    assert is_credit_card("6011000000000012")
    assert is_credit_card("3530")

# Generated at 2022-06-14 05:44:59.435830
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    try:
        __ISBNChecker('1234567890123')
    except InvalidInputError:
        pass
    else:
        raise Exception('test___ISBNChecker_is_isbn_13 failed: '
                        '__ISBNChecker should fail with a string that '
                        'contains a non-digit character.')

    try:
        __ISBNChecker('12345678901235')
    except InvalidInputError:
        pass
    else:
        raise Exception('test___ISBNChecker_is_isbn_13 failed: '
                        '__ISBNChecker should fail with a string that '
                        'contains more than 13 digits.')

    try:
        __ISBNChecker('123456789012')
    except InvalidInputError:
        pass

# Generated at 2022-06-14 05:45:05.518662
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    # create object
    checker = __ISBNChecker('0439708184')

    # assert
    assert checker.is_isbn_10() is True

# Generated at 2022-06-14 05:45:14.014781
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert not __ISBNChecker('97891-1-938-219-2').is_isbn_13()
    assert __ISBNChecker('9789113193820').is_isbn_13()
    assert not __ISBNChecker('9789113193821').is_isbn_13()
    assert not __ISBNChecker('9789113193822').is_isbn_13()
    assert not __ISBNChecker('9789113193823').is_isbn_13()
    assert not __ISBNChecker('9789113193824').is_isbn_13()
    assert __ISBNChecker('9789113193825').is_isbn_13()
    assert not __ISBNChecker('9789113193826').is_isbn_13()
    assert not __

# Generated at 2022-06-14 05:45:27.195487
# Unit test for function is_email
def test_is_email():
    assert is_email('myemail@gmail.com') == True
    assert is_email('my.email@the-provider.com') == True
    assert is_email('@gmail.com') == False
    assert is_email('myemail@gmail') == False
    assert is_email('@') == False
    assert is_email('my.email@theprovider') == False
    assert is_email('myemail@gmail.c') == False
    assert is_email('myemail@.com') == False
    assert is_email('myemail.com') == False
    assert is_email('myemail') == False
    assert is_email('my..email@gmail.com') == False
    assert is_email('my.email.@gmail.com') == False
    assert is_email('my.email..@gmail.com')

# Generated at 2022-06-14 05:45:33.902718
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    checker = __ISBNChecker('097522980X')
    assert checker.is_isbn_10() == True
    checker = __ISBNChecker('097522980x')
    assert checker.is_isbn_10() == True
    checker = __ISBNChecker('097522980Y')
    assert checker.is_isbn_10() == False
    checker = __ISBNChecker('123456789')
    assert checker.is_isbn_10() == False


# Generated at 2022-06-14 05:45:38.416967
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com') # returns true
    assert not is_email('@gmail.com') # returns false
# Test the is_email function
test_is_email()

# Generated at 2022-06-14 05:45:42.700529
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') == True # returns true
    assert is_json('[1, 2, 3]') == True # returns true
    assert is_json('{nope}') == False # returns false



# Generated at 2022-06-14 05:45:54.711511
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    isbn_checker = __ISBNChecker('9780596158064')
    assert isbn_checker.is_isbn_10() == True, 'trying to check a valid isbn10 code'
    isbn_checker = __ISBNChecker('0136091801')
    assert isbn_checker.is_isbn_10() == True, 'trying to check a valid isbn10 code'
    isbn_checker = __ISBNChecker('0-7356-1969-4')
    assert isbn_checker.is_isbn_10() == True, 'trying to check a valid isbn10 code'
    isbn_checker = __ISBNChecker('9780596158064')

# Generated at 2022-06-14 05:46:03.409821
# Unit test for method is_isbn_13 of class __ISBNChecker

# Generated at 2022-06-14 05:46:07.290845
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    checker = __ISBNChecker('9781486802494')

    assert checker.is_isbn_13() == True
    assert checker.is_isbn_10() == False



# Generated at 2022-06-14 05:46:15.211831
# Unit test for function is_json
def test_is_json():
    assert is_json('{ "key": "value" }') is True
    assert is_json('{"key": "value"}') is True
    assert is_json('["value", "value"]') is True

    # invalid json: missing closing curly brace
    assert is_json('[ "value", "value"') is False
    assert is_json('') is False

    # json with extra spaces
    assert is_json(' {"key": "value" } ') is False



# Generated at 2022-06-14 05:46:26.178602
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    # Normal case
    assert __ISBNChecker(input_string="8172234979").is_isbn_10() is True

    # Issue #102
    assert __ISBNChecker(input_string="0285637124").is_isbn_10() is True


# PUBLIC API



# Generated at 2022-06-14 05:46:29.764055
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "John"}') == True
    assert is_json('{"name": "John", "age": 30, "city": "New York"}') == True



# Generated at 2022-06-14 05:46:37.041539
# Unit test for function is_json
def test_is_json():
    data = [
        ('{"name": "Peter"}', True),
        ('[1, 2, 3]', True),
        ('{nope}', False),
        ('', False),
        ('abc', False),
        ('[{', False),
        ('[1,2,3', False)
    ]

    for s, expected in data:
        assert is_json(s) == expected



# Generated at 2022-06-14 05:46:47.885499
# Unit test for function is_email
def test_is_email():
    assert(is_email('a@a.a') == True)
    assert(is_email('a@a') == False)
    assert(is_email('') == False)
    assert(is_email('.a@a.a') == False)
    assert(is_email('a.@a.a') == False)
    assert(is_email('a..a@a.a') == False)
    assert(is_email('a..a.a@a.a') == False)
    assert(is_email('a.a@a.a.') == False)


# Generated at 2022-06-14 05:46:54.789856
# Unit test for function is_email
def test_is_email():
    assert not is_email(None)
    assert not is_email('')
    assert not is_email('my.email')
    assert is_email('my.email@the-provider.com')
    assert is_email('my.email@the-provider.com')
    assert is_email('my_email@the-provider.com')
    assert is_email('my+email@the-provider.com')
    assert is_email('my%email@the-provider.com')
    assert is_email('"my email"@the-provider.com')
    assert is_email('my\\ email@the-provider.com')
    assert not is_email('my\\.email@the-provider.com')
    assert is_email(' "my email" @the-provider.com')
   

# Generated at 2022-06-14 05:47:00.251763
# Unit test for function is_email
def test_is_email():
    print("Testing is_email")
    assert is_email('my.email@the-provider.com') == True # returns true
    assert is_email('@gmail.com') == False # returns false
    print("Testing is_email finished")



# Generated at 2022-06-14 05:47:11.996559
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker('0000000000').is_isbn_10() == True
    assert __ISBNChecker('1111222333').is_isbn_10() == True
    assert __ISBNChecker('2223334444').is_isbn_10() == True
    assert __ISBNChecker('3334445555').is_isbn_10() == True
    assert __ISBNChecker('4445556666').is_isbn_10() == True
    assert __ISBNChecker('5566666666').is_isbn_10() == True

    assert __ISBNChecker('abcdefghij').is_isbn_10() == False
    assert __ISBNChecker('abc-def-ghi').is_isbn_10() == False
    assert __ISBNChecker('abcdefg-hi').is_

# Generated at 2022-06-14 05:47:16.777387
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name":"Peter"}') == True
    assert is_json('[1, 2, 3]') == True
    assert is_json('{nope}') == False


# Generated at 2022-06-14 05:47:28.862466
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    checker = __ISBNChecker('0061120081')
    assert checker.is_isbn_10()

    checker = __ISBNChecker('0061120080')
    assert not checker.is_isbn_10()

    checker = __ISBNChecker('0061120082')
    assert not checker.is_isbn_10()

    checker = __ISBNChecker('1680502395')
    assert checker.is_isbn_10()

    checker = __ISBNChecker('1680502396')
    assert not checker.is_isbn_10()

    checker = __ISBNChecker('1680502394')
    assert not checker.is_isbn_10()

    checker = __ISBNChecker('abc')
    assert not checker

# Generated at 2022-06-14 05:47:40.604882
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker('111-1-111-11111-1').is_isbn_10() == True
    assert __ISBNChecker('111-1-111-11111-1', False).is_isbn_10() == False
    assert __ISBNChecker('1234567890').is_isbn_10() == False
    assert __ISBNChecker('156881111X', False).is_isbn_10() == True
    assert __ISBNChecker('156881111X').is_isbn_10() == False
    assert __ISBNChecker('1568811115', False).is_isbn_10() == False



# Generated at 2022-06-14 05:48:01.898082
# Unit test for function is_email
def test_is_email():
    assert is_email("") == False
    assert is_email(" ") == False
    assert is_email("@") == False
    assert is_email("1@2") == False
    assert is_email("12@") == False
    assert is_email("@2") == False
    assert is_email("abc@abc.abc") == True
    assert is_email("abc.abc@abc.abc") == True
    assert is_email("abc.@abc.abc") == False
    assert is_email("abc@abc..abc") == False
    assert is_email("abc@abc.") == False
    assert is_email("abc@.abc") == False
    assert is_email("abc@.abc.abc") == False
    assert is_email("abc@abc..abc.abc") == False

# Generated at 2022-06-14 05:48:13.002297
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    # Invalid input
    assert not __ISBNChecker('').is_isbn_10()
    assert not __ISBNChecker('1').is_isbn_10()
    assert not __ISBNChecker('12345678910').is_isbn_10()
    assert __ISBNChecker('1234567891').is_isbn_10()
    assert not __ISBNChecker('123456789w').is_isbn_10()

    # Good cases
    assert __ISBNChecker('038549081X').is_isbn_10()
    assert not __ISBNChecker('1439594635').is_isbn_10()
    assert __ISBNChecker('0471651468').is_isbn_10()
    assert __ISBNChecker('0765347381').is_is

# Generated at 2022-06-14 05:48:15.395025
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker('9780321751041').is_isbn_13()



# Generated at 2022-06-14 05:48:18.274600
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker('978-0-306-40615-7').is_isbn_13()
    assert __ISBNChecker('9780306406157').is_isbn_13()

# Generated at 2022-06-14 05:48:29.198804
# Unit test for function is_json
def test_is_json():
    a_list = [1, 2, 3, "4", "5"]
    a_dict = {'a': '1', 'b': 2, 'c': 3, 'd': '4', 'e': 5}
    a_str = '{"a": "1", "b": 2, "c": 3, "d": "4", "e": 5}'
    a_str2 = '{"a": "1", "b": 2, "c": 3, "d": "4", "e": 5, "f": {}}'
    a_str3 = '{"a": "1", "b": 2, "c": 3, "d": "4", "e": 5, "f": [1, 2, 3, "4", "5"], "g": {}}'