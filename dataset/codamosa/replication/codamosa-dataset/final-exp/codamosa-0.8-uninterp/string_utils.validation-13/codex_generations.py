

# Generated at 2022-06-14 05:38:56.349488
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') == True
    assert is_json('[1, 2, 3]') == True
    assert is_json('{nope}') == False


# Generated at 2022-06-14 05:39:05.244139
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker("3-598-21500-x").is_isbn_13()
    assert __ISBNChecker("978-3-662-48339-5").is_isbn_13()
    assert __ISBNChecker("978-3-662-48339-6").is_isbn_13() == False
    assert __ISBNChecker("978-3-662-48339").is_isbn_13() == False
    assert __ISBNChecker("978-3-662-483391").is_isbn_13() == False
    assert __ISBNChecker("978-3-662-48339 5").is_isbn_13() == False
    assert __ISBNChecker("").is_isbn_13() == False


# Generated at 2022-06-14 05:39:07.525087
# Unit test for function is_json
def test_is_json():
    assert(is_json("{\"name\": \"Peter\"}") == True)
    assert(is_json("{nope}") == False)
    assert(is_json("[1, 2, 3]") == True)


# Generated at 2022-06-14 05:39:14.800199
# Unit test for function is_email
def test_is_email():
    assert is_email("test@gmail.com")
    assert not is_email("test@gmail.com.")
    assert not is_email("test@gmail.com...")
    assert not is_email("test@gmail.com..")
    assert not is_email("test..@gmail.com")
    assert is_email("test.test@gmail.com")
    assert is_email("test.test@gmail..com")
    assert is_email("test@gmail.com.com")



# Generated at 2022-06-14 05:39:16.007888
# Unit test for function is_ip
def test_is_ip():
    #Your code here
    pass

# Generated at 2022-06-14 05:39:20.240178
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') == True
    assert is_json('[1, 2, 3]') == True
    assert is_json('{nope}') == False


# Generated at 2022-06-14 05:39:27.631996
# Unit test for function is_json
def test_is_json():
    assert is_json('{"message":"hello"}') == True
    assert is_json('{}') == True
    assert is_json('[]') == True
    assert is_json('{"name":"john","age":30,"city":"New York"}') == True
    assert is_json('{"name":"john","age":30}') == True
    assert is_json('{"name":["john","smith"],"age":30}') == True
    assert is_json('{"id":1,"name":["john","smith"],"age":30}') == True
    assert is_json('[{"name":"john","age":30},{"name":"smith","age":35}]') == True
    assert is_json('{"name":"john","age":30,"cars":["Ford","BMW","Fiat"]}') == True

# Generated at 2022-06-14 05:39:31.784052
# Unit test for function is_email
def test_is_email():
    assert is_email('luca@gmail.com')
    assert not is_email('luca@gmail')
    assert not is_email('luca.gmail.com')
    assert not is_email('luca..gmail.com')



# Generated at 2022-06-14 05:39:36.460437
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75')
    assert is_ip_v4('nope') == False
    assert is_ip_v4('255.200.100.999') == False

test_is_ip_v4()



# Generated at 2022-06-14 05:39:45.167185
# Unit test for function is_json
def test_is_json():
    assert(is_json('{"name":"Peter"}'))
    assert(is_json('[1,2,3]'))
    assert(is_json('{"name":"Peter","age":18}'))
    assert(not is_json(None))
    assert(not is_json('{nope}'))
    assert(not is_json(''))
    assert(not is_json('[]'))
    assert(not is_json('{}'))



# Generated at 2022-06-14 05:40:03.063332
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com') == True
    assert is_email('@gmail.com') == False
    assert is_email('""@gmail.com') == True
    assert is_email('\"@gmail.com') == False
    assert is_email('"\"@gmail.com') == False
    assert is_email('"my.address@gmail.com"@gmail.com') == True
    assert is_email('\"my.address@gmail.com\"@gmail.com') == True
    assert is_email('my.address@\"gmail.com') == False
    assert is_email('my.address@\"gmail.com\"') == True
    assert is_email('my.address@\"gmail.com\"/') == False

# Generated at 2022-06-14 05:40:09.081334
# Unit test for function is_url
def test_is_url():
    assert is_url('http://www.mysite.com', allowed_schemes=["http"])
    assert is_url('https://mysite.com', allowed_schemes=["https"])
    assert is_url('.mysite.com') is False



# Generated at 2022-06-14 05:40:18.237114
# Unit test for function is_url
def test_is_url():
    # validate url
    assert is_url('http://www.site.com')
    assert is_url('https://site.com')
    assert is_url('ftp://127.0.0.1/')
    assert is_url('http://site')
    assert is_url('http://127.0.0.1')
    assert is_url('http://site.com/my/path')
    assert is_url('http://site.com/my/path/image.png?with=params&and=options')
    assert is_url('http://username@site.com')
    assert is_url('http://username:password@site.com')
    assert is_url('http://username:password@site.com/')
    assert is_url('http://127.0.0.1:8000')
    assert is_

# Generated at 2022-06-14 05:40:30.582141
# Unit test for function is_url
def test_is_url():
    assert is_url('http://www.domain.com/path/to/file.html') == True
    assert is_url('.com') == False
    assert is_url('.com/path/to/file.html') == False
    assert is_url('com/path/to/file.html') == False
    assert is_url('google.fr') == False
    assert is_url('/path/to/file.html') == False
    assert is_url('/path/to/file.') == False
    assert is_url('/path/to/file') == False
    assert is_url('file.html') == False
    assert is_url('www.google.fr') == False
    assert is_url('www.fr') == False
    assert is_url('fr') == False



# Generated at 2022-06-14 05:40:43.307963
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker('12-345-678-9').is_isbn_10() == True
    assert __ISBNChecker('1234567891').is_isbn_10() == True
    assert __ISBNChecker('1234567891', normalize=False).is_isbn_10() == True
    assert __ISBNChecker('1234567890').is_isbn_10() == True
    assert __ISBNChecker('1234567890', normalize=False).is_isbn_10() == True
    assert __ISBNChecker('123456789X').is_isbn_10() == True
    assert __ISBNChecker('123456789X', normalize=False).is_isbn_10() == True
    assert __ISBNChecker('123456789x').is_

# Generated at 2022-06-14 05:40:52.620912
# Unit test for function is_url
def test_is_url():
    assert is_url('https://www.google.fr') is True
    assert is_url('http://www.google.fr') is True
    assert is_url('www.google.fr') is True
    assert is_url('google.fr') is True
    assert is_url('https://google.fr') is True
    assert is_url('ftp://ftp.google.fr') is True
    assert is_url('ftp://ftp.google') is True
    assert is_url('ftp://root:@ftp.google.fr') is True
    assert is_url('https://www.google.fr?q=value') is True
    assert is_url('https://www.google.fr?q=value#fragment') is True

# Generated at 2022-06-14 05:41:02.640060
# Unit test for function is_url
def test_is_url():
    assert is_url(None) == False
    assert is_url('') == False
    assert is_url('.mysite.com') == False
    assert is_url('http://www.mysite.com') == True
    assert is_url('https://mysite.com') == True
    assert is_url('http://mysite.com') == True
    assert is_url('ftp://mysite.com') == True
    assert is_url('ftp://mysite.com', ['ftp']) == True
    assert is_url('ftp://mysite.com', ['http']) == False
    assert is_url('http://mysite.com', ['https']) == False
    assert is_url('http://http.mysite.com') == False



# Generated at 2022-06-14 05:41:08.539063
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75') is True
    assert is_ip_v4('nope') is False
    assert is_ip_v4('255.200.100.999') is False


# Generated at 2022-06-14 05:41:17.751904
# Unit test for function is_isbn
def test_is_isbn():
    assert is_isbn("9780312498580")
    assert is_isbn("1506715214")
    assert not is_isbn("1234567890123")
    assert not is_isbn("123456789012345")
    assert is_isbn("9780312498580", normalize=False)
    assert is_isbn("1506715214", normalize=False)
    assert not is_isbn("978-0312498580", normalize=False)
    assert not is_isbn("150-6715214", normalize=False)
    assert not is_isbn("123-456789012-3", normalize=False)
    assert not is_isbn("123-456789012345", normalize=False)
test_is_isbn()

# Unit test

# Generated at 2022-06-14 05:41:22.396793
# Unit test for function is_ip
def test_is_ip():
    assert is_ip('255.200.100.75')
    assert is_ip('2001:db8:85a3:0000:0000:8a2e:370:7334')
    assert not is_ip('1.2.3')
    assert not is_ip('')
    assert not is_ip(1)
    assert not is_ip(None)
test_is_ip()

# Generated at 2022-06-14 05:41:31.141022
# Unit test for function is_json
def test_is_json():
    assert is_json( '{"name": "Peter"}')
    assert is_json( '[1, 2, 3]')
    assert is_json( '{nope}') == False


# Generated at 2022-06-14 05:41:35.121001
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}')
    assert is_json('[1, 2, 3]')
    assert not is_json('{nope}')


# Generated at 2022-06-14 05:41:46.148260
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker('9780470059029').is_isbn_10() == True
    assert __ISBNChecker('978-0471958697').is_isbn_10() == True
    assert __ISBNChecker('978 0 471 48648 0').is_isbn_10() == True
    assert __ISBNChecker('097522980X').is_isbn_10() == True
    assert __ISBNChecker('0-321-14653-0').is_isbn_10() == True
    assert __ISBNChecker('-0471958697').is_isbn_10() == False
    assert __ISBNChecker('0471958697').is_isbn_10() == True

# Generated at 2022-06-14 05:41:54.135109
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker("978-0-306-40615-7").is_isbn_13()
    assert not __ISBNChecker("978-0-306-40615-0").is_isbn_13()
    assert not __ISBNChecker("978-0-306-40615").is_isbn_13()
    assert not __ISBNChecker("book").is_isbn_13()


# Generated at 2022-06-14 05:42:02.669498
# Unit test for function is_email
def test_is_email():
    assert is_email('me@example.com') == True
    assert is_email('me+me@example.com') == True
    assert is_email('me-me@example.com') == True
    assert is_email('me.me@example.com') == True
    assert is_email('me=me@example.com') == True
    assert is_email('me(me)@example.com') == True
    assert is_email('me,me@example.com') == True
    assert is_email('me:me@example.com') == True

    assert is_email('me@example.com') == True
    assert is_email('ME@example.com') == True
    assert is_email('mE@example.com') == True
    assert is_email('@example.com') == False
    assert is_

# Generated at 2022-06-14 05:42:08.285815
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker('3836221195').is_isbn_10()  # Valid
    assert __ISBNChecker('3-8362-2119-5').is_isbn_10()  # Valid
    assert not __ISBNChecker('3836221196').is_isbn_10()  # Invalid


# PUBLIC API



# Generated at 2022-06-14 05:42:16.376171
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('') == False
    assert is_ip_v4(None) == False
    assert is_ip_v4('255.200.100.75') == True
    assert is_ip_v4('nope') == False
    assert is_ip_v4('255.200.100.999') == False
    assert is_ip_v4('255.200.100.75') == True
test_is_ip_v4()


# Generated at 2022-06-14 05:42:21.188573
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}')
    assert is_json('[1, 2, 3]')
    assert is_json('{name: "Peter"}')
    assert not is_json('{nope}')
    assert not is_json('[1, 2, 3')



# Generated at 2022-06-14 05:42:33.069136
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker('0321751043').is_isbn_10() is True
    assert __ISBNChecker('0374530850').is_isbn_10() is True
    assert __ISBNChecker('0345388677').is_isbn_10() is True
    assert __ISBNChecker('034538867X').is_isbn_10() is True
    assert __ISBNChecker('0978757412').is_isbn_10() is True
    assert __ISBNChecker('0-97-875741-2').is_isbn_10() is True
    assert __ISBNChecker('978-0-545-39023-3').is_isbn_10() is True
    assert __ISBNChecker('0-9752298-0-X').is_isbn_10

# Generated at 2022-06-14 05:42:38.181544
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('127.0.0.1') == True
    assert is_ip_v4('192.128.1.1') == True
    assert is_ip_v4('999.999.999.999') == False
    assert is_ip_v4('192.128.1') == False
    assert is_ip_v4('99.128.1.1') == True
    assert is_ip_v4('') == False

# is_ip_v4() 


# Generated at 2022-06-14 05:42:54.586472
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') == True, "Test 1 Failed"
    assert is_json('[1, 2, 3]') == True, "Test 2 Failed"
    assert is_json('{nope}') == False, "Test 3 Failed"
    assert is_json(34) == False, "Test 4 Failed"
    print('is_json Test Passed')

test_is_json()



# Generated at 2022-06-14 05:43:04.954783
# Unit test for function is_credit_card
def test_is_credit_card():
    assert is_credit_card('4111 1111 1111 1111')
    assert is_credit_card('4111-1111-1111-1111')
    assert is_credit_card('4111111111111111')
    assert is_credit_card('4111-1111-1111-1111', 'VISA')
    assert not is_credit_card('5111-1111-1111-1111', 'VISA')
    assert is_credit_card('5111-1111-1111-1111')
    assert is_credit_card('5111 1111 1111 1111')
    assert is_credit_card('5111 11111 11111111')
    assert is_credit_card('5111-1111-1111-1111', 'MASTERCARD')
    assert not is_credit_card('5111-1111-1111-1111', 'VISA')

# Generated at 2022-06-14 05:43:11.453442
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    checker = __ISBNChecker('978-1-56924-979-9')
    assert checker.is_isbn_13() == True

    checker = __ISBNChecker('978-1-56924-979-5')
    assert checker.is_isbn_13() == False

    try:
        checker = __ISBNChecker(1234)
        assert checker.is_isbn_13() == True
    except InvalidInputError:
        pass


# Generated at 2022-06-14 05:43:17.690565
# Unit test for function is_credit_card
def test_is_credit_card():
    assert is_credit_card('1111222233334444', card_type='VISA') == True
    assert is_credit_card('1111222233334444') == True
    assert is_credit_card('5555555555554444') == True
    assert is_credit_card('5555555555554444', card_type='MASTERCARD') == True
    assert is_credit_card('6011000990139424') == True
    assert is_credit_card('6011000990139424', card_type='DISCOVER') == True
    assert is_credit_card('343434343434343') == True
    assert is_credit_card('343434343434343', card_type='AMERICAN_EXPRESS') == True

# Generated at 2022-06-14 05:43:21.438849
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') == True
    assert is_json('[1, 2, 3]') == True
    assert is_json('{nope}') == False




# Generated at 2022-06-14 05:43:25.860811
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75') == True
    assert is_ip_v4('nope') == False
    assert is_ip_v4('255.200.100.999') == False

test_is_ip_v4()


# Generated at 2022-06-14 05:43:30.938677
# Unit test for function is_json
def test_is_json():
    assert is_json("{}") is True
    assert is_json("[]") is True
    assert is_json("{\"name\": \"Peter\"}") is True
    assert is_json("{nope}") is False


# Generated at 2022-06-14 05:43:44.911385
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert not __ISBNChecker('978-0-306-40615-7').is_isbn_13()
    assert not __ISBNChecker('0-306-40615-2').is_isbn_13()
    assert __ISBNChecker('978-83-7579-288-6').is_isbn_13()
    assert __ISBNChecker('83-7579-288-3').is_isbn_13()
    assert not __ISBNChecker('978-83-38-05773-1').is_isbn_13()
    assert not __ISBNChecker('83-38-05773-5').is_isbn_13()
    assert __ISBNChecker('83-75-79-288-3').is_isbn_13()

# Generated at 2022-06-14 05:43:56.788811
# Unit test for function is_credit_card
def test_is_credit_card():

    # Test valid credit cards
    assert is_credit_card('4111111111111111') is True  # Visa
    assert is_credit_card('5105105105105100') is True  # Mastercard
    assert is_credit_card('6011111111111117') is True  # Discover
    assert is_credit_card('3530111333300000') is True  # JCB
    assert is_credit_card('341111111111111') is True  # American Express
    assert is_credit_card('5555555555554444') is True  # Mastercard
    assert is_credit_card('5555555555554444') is True  # Mastercard
    assert is_credit_card('5555555555554444') is True  # Mastercard

    # Test invalid credit cards

# Generated at 2022-06-14 05:43:58.657195
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    checker = __ISBNChecker("123456789X")
    assert checker.is_isbn_10() is True



# Generated at 2022-06-14 05:44:14.292973
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker('978-3-16-148410-0').is_isbn_13() == True
    assert __ISBNChecker('9783161484100').is_isbn_13() == True
    assert __ISBNChecker('978 3 16 148410 0').is_isbn_13() == True
    assert __ISBNChecker('9783161484100').is_isbn_13() == True
    assert __ISBNChecker('9783161484100', normalize=False).is_isbn_13() == True
    assert __ISBNChecker('978-3-16-148410-1').is_isbn_13() == False
    assert __ISBNChecker('978 316 148410 1').is_isbn_13() == False

# Generated at 2022-06-14 05:44:18.019079
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('192.168.1.1') == True
    assert is_ip_v4('255.200.100.75') == True
    assert is_ip_v4('nope') == False
    assert is_ip_v4('255.200.100.999') == False


# Generated at 2022-06-14 05:44:20.939101
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com')
    assert not is_email('@gmail.com')
    assert is_email('"very.(),:;<>[]\".VERY.\"very@\\ \"very\".unusual"@gmail.com')



# Generated at 2022-06-14 05:44:33.329695
# Unit test for function is_json
def test_is_json():
    assert is_json('{"hello": "world"}') == True
    assert is_json('{hello: "world"}') == False
    assert is_json('[hello: "world"]') == False
    assert is_json('{"hello": "world"}') == True
    assert is_json('[{hello: "world"}]') == False
    assert is_json('[hello: "world"]') == False
    assert is_json('[hello: "world"]') == False
    assert is_json('{"a": "b"}') == True
    assert is_json('{"1": "2"}') == True
    assert is_json('{"$": "2"}') == True
    assert is_json('{"1": "a"}') == True
    assert is_json('{"a": "a"}') == True
    assert is_json

# Generated at 2022-06-14 05:44:38.044290
# Unit test for function is_json
def test_is_json():
    assert is_json('"test"') is False
    assert is_json('{"name": "Peter"}') is True
    assert is_json('[1, 2, 3]') is True


# Generated at 2022-06-14 05:44:43.599610
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75')
    assert not is_ip_v4('nope')
    assert not is_ip_v4('255.200.100.999')
test_is_ip_v4()



# Generated at 2022-06-14 05:44:55.781347
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker('1843560283').is_isbn_10() == True
    assert __ISBNChecker('0-9752298-0-X').is_isbn_10() == True
    assert __ISBNChecker('0 302 05694 1').is_isbn_10() == True
    assert __ISBNChecker('0-8044-2957-X').is_isbn_10() == True
    assert __ISBNChecker('0-9752298-0-x').is_isbn_10() == True
    assert __ISBNChecker('0-9752298-0-8').is_isbn_10() == False
    assert __ISBNChecker('978-1-84356-028-3').is_isbn_10() == False


# PUBLIC API


# type checks

# Generated at 2022-06-14 05:45:09.841126
# Unit test for function is_email
def test_is_email():
    assert not is_email('me!')
    assert not is_email('')
    assert not is_email('ab.cd@12.123.123.123')
    assert not is_email('my.email@')
    assert not is_email('my.email@the_provider.com')
    assert not is_email('@gmail.com')
    assert not is_email('.my.email@the-provider.com')
    assert not is_email('my.em.ail@the-provider.com')
    assert not is_email('my.email@the-provider.com.')
    assert not is_email('my.email@localhost')
    assert not is_email('my.email@.com.my')
    assert not is_email('my.email123@gmail.b')

# Generated at 2022-06-14 05:45:13.990784
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75') == True
    assert is_ip_v4('nope') == False
    assert is_ip_v4('255.200.100.999') == False

test_is_ip_v4()

# Generated at 2022-06-14 05:45:20.345877
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker('0-306-40615-2').is_isbn_10() is True
    assert __ISBNChecker('0306406152').is_isbn_10() is True
    assert __ISBNChecker('0-306-40615-3').is_isbn_10() is False

# Generated at 2022-06-14 05:45:30.088898
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') is True
    assert is_json('[1, 2, 3]') is True
    assert is_json('{nope}') is False
    assert is_json('{"a":"b"} {"b":"c"}') is False


# Generated at 2022-06-14 05:45:44.531258
# Unit test for function is_email
def test_is_email():
    assert is_email('"email"@gmail.com') == True
    assert is_email('simple@example.com') == True
    assert is_email('very.common@example.com') == True
    assert is_email('disposable.style.email.with+symbol@example.com') == True
    assert is_email('other.email-with-hyphen@example.com') == True
    assert is_email('x@example.com') == True
    assert is_email('example-indeed@strange-example.com') == True
    assert is_email('example@localhost') == True
    assert is_email('example@s.solutions') == True
    assert is_email('" "@example.org') == True
    assert is_email('example@localhost.') == True

# Generated at 2022-06-14 05:45:46.358936
# Unit test for function is_email
def test_is_email():
    assert is_email("test@test.org") == True
    assert is_email("testtest.org") == False
    assert is_email("test@test") == False



# Generated at 2022-06-14 05:45:49.487564
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com') is True
    assert is_email('@gmail.com') is False
#is_email('my.email@the-provider.com')



# Generated at 2022-06-14 05:45:59.209351
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    checker = __ISBNChecker(input_string="0789751984")
    assert checker.is_isbn_10() == True
    assert checker.is_isbn_13() == False

    checker = __ISBNChecker(input_string="0789751985")
    assert checker.is_isbn_10() == False
    assert checker.is_isbn_13() == False

    checker = __ISBNChecker(input_string="0-7897-5198-4")
    assert checker.is_isbn_10() == True
    assert checker.is_isbn_13() == False

# Generated at 2022-06-14 05:46:13.948172
# Unit test for function is_ip_v4
def test_is_ip_v4():
    cases = [
        ('127.0.0.1', True),
        ('0.0.0.0',   True),
        ('255.255.255.255', True),
        ('192.168.1.1', True),
        ('1.2.3.4',   True),
        ('256.255.255.255', False),
        ('1.2.3',     False),
        ('1.2.3.4.5', False),
        ('1.2.3.4.',  False),
        ('myhost',    False),
        ('127.0.0.1:8000', False) # not a valid ip v4
    ]


# Generated at 2022-06-14 05:46:19.351913
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert not is_ip_v4('nope'), "Should not be a valid IP"
    assert not is_ip_v4('255.200.100.999'), "Should not be a valid IP (out of range)"
    assert is_ip_v4('255.200.100.75'), "Should be a valid IP"


# Generated at 2022-06-14 05:46:27.395345
# Unit test for function is_json
def test_is_json():
    if(is_json('') == False):
        print("empty string - success")
    else:
        print("empty string - fail")
    if(is_json('{"name": "Peter"}') == True):
        print('{"name": "Peter"} - success')
    else:
        print('{"name": "Peter"} - fail')
    if(is_json('[1, 2, 3]') == True):
        print('[1, 2, 3] - success')
    else:
        print('[1, 2, 3] - fail')
    if(is_json('{nope}') == False):
        print('{nope} - success')
    else:
        print('{nope} - fail')

# Generated at 2022-06-14 05:46:29.450599
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker('0316666343').is_isbn_10() is True
    assert __ISBNChecker('0345391802').is_isbn_10() is False


# PUBLIC API


# Generated at 2022-06-14 05:46:33.512777
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker("9780321534965").is_isbn_13()
    assert not __ISBNChecker("9780321534964").is_isbn_13()


# Generated at 2022-06-14 05:46:46.708336
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker('ABCDE12345').is_isbn_10() == False
    assert __ISBNChecker('1234567890').is_isbn_10() == True
    assert __ISBNChecker('123456789').is_isbn_10() == False
    assert __ISBNChecker('12345678901').is_isbn_10() == False
    assert __ISBNChecker('0867209476').is_isbn_10() == True
    assert __ISBNChecker('0867209472').is_isbn_10() == True
    assert __ISBNChecker('1568811465').is_isbn_10() == True
    assert __ISBNChecker('0393049489').is_isbn_10() == True

# Generated at 2022-06-14 05:46:50.890788
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75') is True
    assert is_ip_v4('nope') is False
    assert is_ip_v4('255.200.100.999') is False


# Generated at 2022-06-14 05:47:01.350936
# Unit test for function is_email
def test_is_email():
    assert is_email("my.email@the-provider.com") == True
    assert is_email("@gmail.com") == False
    assert is_email("my.email@gmail.com") == True
    assert is_email("my.email@gmail") == False
    assert is_email("my.email@gmail.") == False
    assert is_email("my.email@gmail.com.") == False
    assert is_email("my.email@gmail.com.es") == True
    assert is_email("my.email@gmail.com.es.uk.co.fr") == True
    assert is_email("myemail@gmail.com.es.uk.co.fr.org") == True
    assert is_email("a" * (320 + 1) + "@gmail.com.es") == False

# Generated at 2022-06-14 05:47:12.515617
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker('9780306406157').is_isbn_13() == True
    assert __ISBNChecker('9780306406158').is_isbn_13() == False
    assert __ISBNChecker('9780306406159').is_isbn_13() == True
    assert __ISBNChecker('9780306406100').is_isbn_13() == False
    assert __ISBNChecker('9780306406146').is_isbn_13() == False
    assert __ISBNChecker('9780306406156').is_isbn_13() == True
    assert __ISBNChecker('1234567890').is_isbn_13() == False
    assert __ISBNChecker('1234567893').is_isbn_13() == True

# Generated at 2022-06-14 05:47:26.358818
# Unit test for function is_json
def test_is_json():
    assert is_json("""
{
  "name": "Peter",
  "age": 23,
  "address": {
    "street": "2 main st.",
    "zip": "90210"
  },
  "references": [
    {"name": "Annie", "phone": "212-555-1212"},
    {"name": "Petey", "phone": "212-555-1212"}
  ]
}
    """) is True


# Generated at 2022-06-14 05:47:27.777126
# Unit test for function is_ip_v4
def test_is_ip_v4():

    assert is_ip_v4('255.200.100.75') == True
    assert is_ip_v4('nope') == False
    assert is_ip_v4('255.200.100.999') == False



# Generated at 2022-06-14 05:47:37.352887
# Unit test for function is_email
def test_is_email():
    assert not is_email('.test@gmail.com')
    assert is_email('test@gmail.com')
    assert is_email('test@test.test.test')
    assert is_email(' test@test')
    assert not is_email('test@test.test..test')
    assert is_email('test@test.a.test')
    assert is_email('test@test.test.test')
    assert is_email('test@test.test.test.test')
    assert not is_email('test@@test.test.test')
    assert is_email('test+test@test.test')
    assert is_email('1test@test.test')
    assert is_email('test@a.longdomain.org')
    assert not is_email('test@test.a')

# Generated at 2022-06-14 05:47:45.281390
# Unit test for function is_email
def test_is_email():
    assert is_email('hello@gmail.com'), 'gmail'
    assert not is_email('hello@.com'), 'start with dot'
    assert not is_email('@gmail.com'), 'start with @'
    assert not is_email('hellogmail.com'), 'no @'
    assert not is_email('hello@gmailcom'), 'no .'
    assert not is_email('hello@gmail..com'), 'no consecutive dot'
    assert not is_email('hello@gmail.#com'), 'invalid tail'
    assert not is_email('hello@@gmail.com'), 'multiple @'
    assert is_email('hello@gmail.com.'), 'end dot'
    assert is_email('hello@g(mail.com'), 'invalid char in tail'

# Generated at 2022-06-14 05:47:50.797379
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert not __ISBNChecker('978-000147-00-0').is_isbn_10()
    assert __ISBNChecker('4242343946').is_isbn_10()
    assert __ISBNChecker('0123456789').is_isbn_10()
    assert not __ISBNChecker('1234567890').is_isbn_10()


# PUBLIC API



# Generated at 2022-06-14 05:47:53.568659
# Unit test for function is_email
def test_is_email():
    assert is_email("hsheikh62@gmail.com") == True
    assert is_email("hsheikh62gmail.com") == False


# Generated at 2022-06-14 05:48:08.320161
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker('123123123X').is_isbn_10() == True
    assert __ISBNChecker('123123123x').is_isbn_10() == True
    assert __ISBNChecker('123-123-12-3X').is_isbn_10() == True
    assert __ISBNChecker('123-123-12-3x').is_isbn_10() == True
    assert __ISBNChecker('1231231234').is_isbn_10() == False


# Generated at 2022-06-14 05:48:18.669800
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker('978919001855').is_isbn_13() == True
    assert __ISBNChecker('978-91-001855-3').is_isbn_13() == True
    assert __ISBNChecker('978-91-001855').is_isbn_13() == False
    assert __ISBNChecker('978-91-001855-').is_isbn_13() == False
    assert __ISBNChecker('978-91-00185-').is_isbn_13() == False
    assert __ISBNChecker('978-91-001s-s').is_isbn_13() == False
    assert __ISBNChecker('978-91-001s-1').is_isbn_13() == False


# Generated at 2022-06-14 05:48:20.991422
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    checker = __ISBNChecker('156881111X')
    assert checker.is_isbn_10() == True