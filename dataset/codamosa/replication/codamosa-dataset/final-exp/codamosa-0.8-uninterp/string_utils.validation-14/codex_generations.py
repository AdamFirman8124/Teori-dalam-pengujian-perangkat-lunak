

# Generated at 2022-06-14 05:38:41.857675
# Unit test for function is_json
def test_is_json():
    assert is_json('["foo", "bar", "baz"]')
    assert is_json('{"foo": "bar", "baz": "qux"}')
test_is_json()



# Generated at 2022-06-14 05:38:53.556914
# Unit test for function is_email
def test_is_email():
    assert is_email("john@gmail.com") == True
    assert is_email("john@gmail.come") == False
    assert is_email("john@gmail.") == False
    assert is_email("@gmail.com") == False
    assert is_email("john@.com") == False
    assert is_email("john@.com") == False
    assert is_email("john@gmail.co") == True
    assert is_email("john.doe123@gmail.co") == True
    assert is_email("John.Doe@gmail.com") == True
    assert is_email("john234.doe@gmail.com") == True
    assert is_email("john.doe.jr@gmail.com") == True
    assert is_email("john.doe.jr@gmail.com") == True
   

# Generated at 2022-06-14 05:38:56.550526
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75')
    assert not is_ip_v4('nope')
    assert not is_ip_v4('255.200.100.999')



# Generated at 2022-06-14 05:39:01.254223
# Unit test for function is_json
def test_is_json():
    assert is_json('1') is False
    assert is_json('"asd"') is False
    assert is_json('{}') is True
    assert is_json('[]') is True
    assert is_json('{"asd": "asd"}') is True
    assert is_json('[1, 2, 3]') is True


# Generated at 2022-06-14 05:39:05.627213
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert(is_ip_v4('255.200.100.75') == True)
    assert(is_ip_v4('nope') == False)
    assert(is_ip_v4('255.200.100.999') == False)


# Generated at 2022-06-14 05:39:16.622309
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    checker = __ISBNChecker('978-0-306-40615-7')
    assert checker.is_isbn_13()

    checker = __ISBNChecker('978-0-306-40615-5')
    assert not checker.is_isbn_13()

    checker = __ISBNChecker('978 0 306 40615 7')
    assert checker.is_isbn_13()

    checker = __ISBNChecker('978 0 306 40615 5')
    assert not checker.is_isbn_13()

    checker = __ISBNChecker('978-0-306-40615-7', normalize=False)
    assert not checker.is_isbn_13()

    checker = __ISBNChecker('978 0 306 40615 7', normalize=False)
   

# Generated at 2022-06-14 05:39:25.888169
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    # Case 1
    isbn_checker = __ISBNChecker('978-3-16-148410-0', True)
    assert isbn_checker.is_isbn_13()

    # Case 2
    isbn_checker = __ISBNChecker('9783161484100', True)
    assert isbn_checker.is_isbn_13()

    # Case 3
    isbn_checker = __ISBNChecker('978-3-16-148410-1', True)
    assert not isbn_checker.is_isbn_13()

    # Case 4
    isbn_checker = __ISBNChecker('9783161484151', True)
    assert not isbn_checker.is_isbn_13()



# Generated at 2022-06-14 05:39:33.006179
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75')
    assert not is_ip_v4('nope')
    assert not is_ip_v4('255.200.100.999')
    assert not is_ip_v4('255.200.100.75.102')
    assert not is_ip_v4('255')

#helper functions to split ip into two parts

# Generated at 2022-06-14 05:39:35.882532
# Unit test for function is_integer
def test_is_integer():
    assert is_integer('1.1') == False
    assert is_integer('-1.1') == False
    assert is_integer('1') == False
    assert is_integer('1e3') == False


# Generated at 2022-06-14 05:39:49.688421
# Unit test for function is_email
def test_is_email():
    assert is_email('foobar@example.com')
    assert not is_email('foo@example..com')
    assert not is_email('foo@@bar.com')
    assert is_email('f@e.com')
    assert is_email('foobar@example.com')
    assert not is_email('foo@example.com.')
    assert is_email('example.com')
    assert is_email('foo@example_bar.com')
    assert not is_email('foobar@example..com')
    assert is_email('foo@ex.ample.com')
    assert is_email('foo@[127.0.0.1]')
    assert is_email('foo@[127.0.0.1]')
    assert not is_email('foo@example.com>')
    assert not is_email

# Generated at 2022-06-14 05:40:00.565720
# Unit test for function is_isbn
def test_is_isbn():
    assert(is_isbn('9780312498580')==True)
    assert(is_isbn('1506715214')==True)
    
test_is_isbn()


# Generated at 2022-06-14 05:40:07.020373
# Unit test for function is_ip
def test_is_ip():
    assert(is_ip('255.200.100.75') == True)
    assert(is_ip('2001:db8:85a3:0000:0000:8a2e:370:7334') == True)
    assert(is_ip('') == False)
    assert(is_ip('1.2.3') == False)
    
test_is_ip()


# Generated at 2022-06-14 05:40:12.118153
# Unit test for function is_ip
def test_is_ip():
    assert is_ip('255.200.100.75')
    assert is_ip('2001:db8:85a3:0000:0000:8a2e:370:7334')
    assert is_ip('1.2.3') == False
test_is_ip()



# Generated at 2022-06-14 05:40:15.067889
# Unit test for function is_url
def test_is_url():
    assert is_url('https://www.google.com') == True
# End unit test



# Generated at 2022-06-14 05:40:19.813599
# Unit test for function is_url
def test_is_url():
    assert is_url('http://www.mysite.com') is True
    assert is_url('https://mysite.com') is True
    assert is_url('mysite.com') is False
    assert is_url('.mysite.com') is False



# Generated at 2022-06-14 05:40:27.227437
# Unit test for function is_credit_card
def test_is_credit_card():
    # Visa
    assert is_credit_card('4532242899053534', 'VISA')
    assert is_credit_card('4532 2428 9905 3534', 'VISA')
    assert is_credit_card('4532495899053534', 'VISA')
    assert is_credit_card('4532495899053534', 'VISA')
    assert is_credit_card('4532 4958 9905 3534', 'VISA')
    assert is_credit_card('4024007188084288', 'VISA')
    assert is_credit_card('4024 0071 8808 4288', 'VISA')
    # Mastercard
    assert is_credit_card('5476380417997670', 'MASTERCARD')

# Generated at 2022-06-14 05:40:29.296571
# Unit test for function is_ip
def test_is_ip():
    assert is_ip('255.200.100.75')
    assert is_ip('2001:db8:85a3:0000:0000:8a2e:370:7334')
    assert not is_ip('1.2.3')
test_is_ip()



# Generated at 2022-06-14 05:40:43.112811
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker('0306406152').is_isbn_10()
    assert __ISBNChecker('0764567524').is_isbn_10()
    assert __ISBNChecker('0804001084').is_isbn_10()
    assert __ISBNChecker('0804001532').is_isbn_10()
    assert __ISBNChecker('0899661555').is_isbn_10()
    assert __ISBNChecker('1558604820').is_isbn_10()
    assert __ISBNChecker('1571690582').is_isbn_10()
    assert __ISBNChecker('1571690643').is_isbn_10()
    assert __ISBNChecker('1571690817').is_isbn_10()
    assert __ISBNChecker

# Generated at 2022-06-14 05:40:52.529866
# Unit test for function is_email
def test_is_email():
    assert is_email("john.smith@gmail.com")
    assert not is_email("john.smith@gmail.com.")
    assert is_email("john.smith@gmail.com")
    assert not is_email("@gmail.com")
    assert not is_email("www.mydomain.com")
    assert not is_email("mydomain.com")
    assert not is_email("")
    assert not is_email("test@test@test.com")
    assert is_email("john.smith@gmail.com")
    assert not is_email("john.smith@gmail.com")
    assert is_email("john.smith@mailserver1.com")
    assert not is_email("john.smith@gmail..com")
    assert is_email("john.smith+label@gmail.com")

# Generated at 2022-06-14 05:40:58.021458
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    checker = __ISBNChecker('978-1-63345-649-7')
    assert checker.is_isbn_13() is True

    checker = __ISBNChecker('978-1-63345-649-3')
    assert checker.is_isbn_13() is False

# Generated at 2022-06-14 05:41:09.059961
# Unit test for function is_url
def test_is_url():
  print("Test is_url")
  assert(is_url('http://www.mysite.com') == True)
  assert(is_url('https://mysite.com') == True)
  assert(is_url('.mysite.com') == False)
test_is_url()




# Generated at 2022-06-14 05:41:20.631975
# Unit test for function is_email
def test_is_email():
    assert is_email('jack@gmail.com') == True
    assert is_email('test_email@test-test.test') == True
    assert is_email('test@test_test.test') == True
    assert is_email('test@test_test..test.test') == True
    assert is_email('test_name@test.test_test.test') == True
    assert is_email('my@my.example.com') == True
    assert is_email('jack@@gmail.com') == False
    assert is_email('test@test_test..test') == False
    assert is_email('@gmail.com') == False
    assert is_email('gmail.com') == False
    assert is_email('test_name@test.test_test.test.') == False

# Generated at 2022-06-14 05:41:29.624406
# Unit test for function is_url
def test_is_url():
    assert is_url('http://www.mysite.com') == True
    assert is_url('https://mysite.com') == True
    assert is_url('.mysite.com') == False
    assert is_url(None) == False
    assert is_url('http://www.mysite.com', allowed_schemes=['http', 'https']) == True
    assert is_url('https://www.mysite.com', allowed_schemes=['http', 'https']) == True
    assert is_url('ftp://www.mysite.com', allowed_schemes=['http', 'https']) == False
    assert is_url('http://www.mysite.com', allowed_schemes=[]) == False
    
test_is_url()



# Generated at 2022-06-14 05:41:42.811381
# Unit test for function is_email

# Generated at 2022-06-14 05:41:45.682686
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}')
    assert is_json('[1, 2, 3]')
    assert is_json('{nope}') is False


# Generated at 2022-06-14 05:41:58.113647
# Unit test for function is_email
def test_is_email():
    assert is_email("a@b.c") is True
    assert is_email("a@b.c.d.e.f.g.h.i.j") is True
    assert is_email("a.b.c") is True
    assert is_email("a.b.c0") is True
    assert is_email("a.b.c0@d.e") is True
    assert is_email("a.b.c0@d.e.f") is True
    assert is_email("a.b.c0@d.e.f.g.h.i.j") is True
    assert is_email("aa.b.c0@d.e.f.g.h.i.j") is True

# Generated at 2022-06-14 05:42:09.497198
# Unit test for function is_email
def test_is_email():
    assert is_email('testemail1@test.test')
    assert is_email('test_email@test.test')
    assert is_email('test.email@test.test')
    assert is_email('test.email1@test.test')
    assert is_email('testemail.1@test.test')
    assert is_email('testemail1@test.com')
    assert is_email('testemail1@test.it')
    assert is_email('testemail1@test.net')
    assert is_email('testemail1@test.org')
    assert is_email('testemail1@test.edu')
    assert is_email('testemail1@test.gov')
    assert is_email('testemail1@test.ca')
    assert is_email('testemail1@test.us')

# Generated at 2022-06-14 05:42:18.673247
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    num_passed = 0

    assert __ISBNChecker('0-306-40615-2').is_isbn_10() is True, 'Test failed'
    num_passed += 1
    assert __ISBNChecker('0306406152').is_isbn_10() is True, 'Test failed'
    num_passed += 1
    assert __ISBNChecker('0306406153').is_isbn_10() is False, 'Test failed'
    num_passed += 1

    return num_passed

# Generated at 2022-06-14 05:42:30.832188
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com')
    assert not is_email('my.emailthe-provider.com')
    assert not is_email('my.email@the-providercom')
    assert not is_email('@gmail.com')
    assert not is_email('mail@')
    assert is_email('<your.email@provider.com>')
    assert not is_email('<your.email@providercom>')
    assert is_email('your.email@provider.com')
    assert not is_email('your.email@providercom')
    assert is_email('your.email@provider.co.uk')
    assert not is_email('your.email@providercouk')
    assert is_email('your.email@provider.solutions')
   

# Generated at 2022-06-14 05:42:43.912138
# Unit test for function is_email
def test_is_email():
    assert is_email('test@test.test')
    assert is_email('Test@test.test')
    assert is_email('test@test.test.test')
    assert is_email('Test@test.test.test')
    assert is_email('test@test.test.test.test')
    assert is_email('Test@test.test.test.test')
    assert is_email('test@test-test.test')
    assert is_email('test@test-test.test-test')
    assert is_email('test.test@test.test')
    assert is_email('test.test@test.test')
    assert is_email('test.test@test.test-test')
    assert is_email('test_test@test.test')

# Generated at 2022-06-14 05:43:00.825950
# Unit test for function is_email
def test_is_email():
    # the following tests are positive
    assert is_email('test@test.com')
    assert is_email('Test@test.com')
    assert is_email('test.test@test.com')
    assert is_email('test.test+spam@test.com')
    assert is_email('-test@test.com')
    assert is_email('!#$%&\'*+-/=?^_`{|}~@test.com')
    assert is_email('"test@test.com"@test.com')  # noqa
    assert is_email('"a.a"@test.com')
    assert is_email('"aaaa"@test.com')
    assert is_email('"a@a"@test.com')
    assert is_email('"test@test"@test.com')

# Generated at 2022-06-14 05:43:02.076223
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com') == True



# Generated at 2022-06-14 05:43:04.807535
# Unit test for function is_json
def test_is_json():
    assert is_json({"name": "Peter"}) == True
    assert is_json([1, 2, 3]) == True
    assert is_json('{nope}') == False


# Generated at 2022-06-14 05:43:08.321900
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    checker = __ISBNChecker("978-3-16-148410-0")
    assert checker.is_isbn_10() == True


# Generated at 2022-06-14 05:43:14.497671
# Unit test for function is_email
def test_is_email():
    assert is_email('lucio.fazio@gmail.com') == True
    assert is_email('lucio_fazio@gmail.com') == True
    assert is_email('lucio.fazio@cineca.it') == True
    assert is_email('lucio.fazio@cineca.daf.it') == True
    assert is_email('lucio.fazio@outlook.it') == True
    assert is_email('lucio.fazio@yahoo.com') == True
    assert is_email('lucio.fazio@hotmail.com') == True
    assert is_email('lucio.fazio@smt.it') == True
    assert is_email('lucio.fazio@infn.it') == True

# Generated at 2022-06-14 05:43:20.271989
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75') == True
    assert is_ip_v4('nope') == False # not an ip
    assert is_ip_v4('255.200.100.999') == False # 999 is out of range

# Generated at 2022-06-14 05:43:31.074253
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com') == True
    assert is_email('@gmail.com') == False
    assert is_email('me@localhost') == True
    assert is_email('me@[192.168.0.1]') == True
    assert is_email('me@[2001:0db8:85a3:08d3:1319:8a2e:0370:7344]') == True
    assert is_email('me@[www.example.com]') == True
    assert is_email('first.last@iana.org') == True
    assert is_email('1234567890123456789012345678901234567890123456789012345678901234@iana.org') == True

# Generated at 2022-06-14 05:43:35.202777
# Unit test for function is_email
def test_is_email():

    assert is_email('my.email@the-provider.com') == True
    assert is_email('@gmail.com') == False



# Generated at 2022-06-14 05:43:42.045533
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker('1321354352').is_isbn_10() is True
    assert __ISBNChecker('1321354351').is_isbn_10() is False
    assert __ISBNChecker('13213543').is_isbn_10() is False
    assert __ISBNChecker('a321354353').is_isbn_10() is False

# Generated at 2022-06-14 05:43:48.854138
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    checker = __ISBNChecker('978-3-16-148410-0')
    assert checker.is_isbn_13() is True
    checker = __ISBNChecker('9783161484100')
    assert checker.is_isbn_13() is True
    checker = __ISBNChecker('9783161484106')
    assert checker.is_isbn_13() is False



# Generated at 2022-06-14 05:44:07.256035
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com') == True
    assert is_email('my.email@the-provider') == False
    assert is_email('@gmail.com') == False
    assert is_email('"my email"@gmail.com') == True
    assert is_email('"my.email"@gmail.com') == True
    assert is_email('"my.email"@gmail') == False
    assert is_email('my\\ email@gmail.com') == True
    assert is_email('.email@gmail.com') == False
    assert is_email('my.email@.gmail.com') == False
    assert is_email('my.email@gmail..com') == False
    assert is_email('my.email@gmail.com.') == False

# Generated at 2022-06-14 05:44:18.674062
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker('0-201-30338-1').is_isbn_10() == True
    assert __ISBNChecker('0-201-30338-9').is_isbn_10() == False
    assert __ISBNChecker('0-201-303381').is_isbn_10() == False
    assert __ISBNChecker('0-201-303381-1').is_isbn_10() == False
    assert __ISBNChecker('0201303381').is_isbn_10() == True
    assert __ISBNChecker('020130338-1').is_isbn_10() == True
    assert __ISBNChecker('0201303381-1').is_isbn_10() == False

# Generated at 2022-06-14 05:44:21.623044
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') == True # True
    assert is_json('[1, 2, 3]') == True # True
    assert is_json('{nope}') == False # False

    print('Successful - test_is_json')
test_is_json()



# Generated at 2022-06-14 05:44:29.978319
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker('359821416X').is_isbn_10() is True
    assert __ISBNChecker('0201558025').is_isbn_10() is True
    assert __ISBNChecker('0201558025').is_isbn_13() is False
    assert __ISBNChecker('1484201721').is_isbn_10() is True
    assert __ISBNChecker('1484201721').is_isbn_13() is True



# Generated at 2022-06-14 05:44:33.631067
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75') 
    assert not is_ip_v4('nope') 
    assert not is_ip_v4('255.200.100.999')

# Generated at 2022-06-14 05:44:40.949400
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker('0-306-40615-2').is_isbn_10() == True
    assert __ISBNChecker('0306406152').is_isbn_10() == True
    assert __ISBNChecker('0-306-406152').is_isbn_10() == False
    assert __ISBNChecker('030640615').is_isbn_10() == False
    assert __ISBNChecker('0-306-40615-3').is_isbn_10() == False
    assert __ISBNChecker('0306406153').is_isbn_10() == False


# PUBLIC API



# Generated at 2022-06-14 05:44:44.650649
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker('0747532699').is_isbn_10() == True



# Generated at 2022-06-14 05:44:47.622530
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    obj = __ISBNChecker('1234567890123')
    assert obj.is_isbn_13() is True


# Generated at 2022-06-14 05:44:52.451554
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75') == True
    assert is_ip_v4('nope') == False
    assert is_ip_v4('255.200.100.999') == False
test_is_ip_v4()



# Generated at 2022-06-14 05:44:55.790738
# Unit test for function is_json
def test_is_json():
    assert is_json("{\"name\": \"Peter\"}") # returns true
    assert is_json("[1, 2, 3]") # returns true
    assert is_json("{nope}") # returns false


# Generated at 2022-06-14 05:45:11.359226
# Unit test for function is_email
def test_is_email():
    assert is_email('') == False
    assert is_email(' '*29) == False
    assert is_email(' '*30) == True
    assert is_email(' '*320) == True
    assert is_email(' '*321) == False
    assert is_email('.foo.com') == False
    assert is_email('foo.com') == False
    assert is_email('lalala@foo.com') == True
    assert is_email('"lala la"@foo.com') == True
    assert is_email('"lala@la"@foo.com') == True
    assert is_email('"lala la"@foo.com') == True
    assert is_email('"lala la"@foo.com') == True

# Generated at 2022-06-14 05:45:14.593162
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker('0-306-40615-2').is_isbn_10() is True
    assert __ISBNChecker('161729134X').is_isbn_10() is True


# Generated at 2022-06-14 05:45:27.662579
# Unit test for function is_email
def test_is_email():
    assert not is_email(None)
    assert not is_email('')
    assert not is_email(' ')
    assert not is_email('Abc.example.com')
    assert not is_email('A@b@c@example.com')
    assert not is_email('a"b(c)d,e:f;g<h>i[j\k]l@example.com')
    assert not is_email('just"not"right@example.com')
    assert not is_email('this is"not\allowed@example.com')
    assert not is_email('this\ still\"not\\allowed@example.com')
    assert not is_email('john..doe@example.com')
    assert not is_email('john.doe@example..com')
    assert not is_email(' ')

# Generated at 2022-06-14 05:45:33.747757
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}')==True
    assert is_json('[1, 2, 3]')==True
    assert is_json('{nope}')==False
    assert is_json('{"name": "Peter", "age": 28}')==True
    assert is_json('[1, 2, 3]')==True
    assert is_json('{nope}')==False
    assert is_json("")==False
    assert is_json(" ")==False


# Generated at 2022-06-14 05:45:39.877645
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    isbn = __ISBNChecker('978-3-16-148410-0')
    assert isbn.is_isbn_13() == True
    assert isbn.is_isbn_10() == False
    isbn = __ISBNChecker('978-3-16-148410-1')
    assert isbn.is_isbn_13() == False
    assert isbn.is_isbn_10() == False
    isbn = __ISBNChecker('1234567890')
    assert isbn.is_isbn_13() == False
    assert isbn.is_isbn_10() == False


# Generated at 2022-06-14 05:45:44.908326
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75') == True
    assert is_ip_v4('nope') == False
    assert is_ip_v4('255.200.100.999') == False
# Test
test_is_ip_v4()



# Generated at 2022-06-14 05:45:54.901641
# Unit test for function is_email
def test_is_email():
    assert is_email('foo@bar.com') == True
    assert is_email('foo.bar@bar.com') == True
    assert is_email('foo@bar') == True
    assert is_email('foo.bar@bar') == True
    assert is_email('foo@bar.com.br') == True
    assert is_email('foo.bar@bar.com.br') == True
    assert is_email('foo-bar@bar.com') == True
    assert is_email('foo-bar@bar.com.br') == True
    assert is_email('foo_bar@bar.com') == True
    assert is_email('foo_bar@bar.com.br') == True
    assert is_email('foo-bar@123.com') == True

# Generated at 2022-06-14 05:45:58.151231
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    isbn_checker = __ISBNChecker("978-1-56619-909-4")
    check = isbn_checker.is_isbn_10()
    assert check == False

# Generated at 2022-06-14 05:45:59.413402
# Unit test for function is_json
def test_is_json():
    import doctest
    doctest.testmod(verbose=True)



# Generated at 2022-06-14 05:46:09.772347
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker('978-3-16-148410-0').is_isbn_13()
    assert __ISBNChecker('978-3-16-148410-0', normalize=False).is_isbn_13()
    assert not __ISBNChecker('978-3-16-148410-0').is_isbn_10()
    assert __ISBNChecker('978-3-16-148410-0', normalize=False).is_isbn_10()


# PUBLIC API


# Generated at 2022-06-14 05:46:16.168128
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker('0306406152').is_isbn_10()


# PUBLIC API



# Generated at 2022-06-14 05:46:22.148525
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4("192.168.0.1") == True
    assert is_ip_v4("255.255.255.0") == True
    assert is_ip_v4("255.200.100.75") == True
    assert is_ip_v4("nope") == False
    assert is_ip_v4("255.200.100.999") == False
# is_ip_v4


# Generated at 2022-06-14 05:46:28.474285
# Unit test for function is_email
def test_is_email():
    assert is_email('@gmail.com') == False
    assert is_email('f@g.a') == False
    assert is_email("my.email@the-provider.com") == True
    assert is_email("laura@gmai..l.com") == False
    assert is_email("s_s@s.s") == True
# end of test



# Generated at 2022-06-14 05:46:38.838980
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    c = __ISBNChecker('1234567890')
    assert c.is_isbn_10() is True

    c.input_string = '3216549870'
    assert c.is_isbn_10() is True

    c.input_string = '321654987007'
    assert c.is_isbn_10() is False

    c.input_string = '321654987011'
    assert c.is_isbn_10() is False

    c.input_string = '32165498701'
    assert c.is_isbn_10() is True

# Generated at 2022-06-14 05:46:50.843250
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') == True
    assert is_json('[1, 2, 3]') == True
    assert is_json('"foo"') == True
    assert is_json('"foo": {}') == False
    assert is_json('{nope}') == False
    assert is_json('') == False
    assert is_json('[]invalid') == False
    assert is_json('[{"foo": "bar"}invalid]') == False
    assert is_json('{invalid}') == False
    assert is_json('{"foo": "bar"invalid}') == False
    assert is_json('"invalid') == False



# Generated at 2022-06-14 05:46:57.484362
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75') is True
    assert is_ip_v4('nope') is False
    assert is_ip_v4('255.200.100.999') is False
    assert is_ip_v4('255.200.100.774') is False
    assert is_ip_v4('') is False
    assert is_ip_v4(None) is False


# Generated at 2022-06-14 05:47:10.234825
# Unit test for function is_email
def test_is_email():
    print("is_email function test 1 passed" if is_email('my.email@the-provider.com') == True else "is_email function test 1 Failed")
    print("is_email function test 2 passed" if is_email('@gmail.com') == False else "is_email function test 2 Failed")
    print("is_email function test 3 passed" if is_email('.@gmail.com') == False else "is_email function test 3 Failed")
    print("is_email function test 4 passed" if is_email('my.email@the-provider.com') == True else "is_email function test 4 Failed")
    print("is_email function test 5 passed" if is_email('helloworld@gmail.com') == True else "is_email function test 5 Failed")

# Generated at 2022-06-14 05:47:18.275584
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker("9789571325554").is_isbn_13() is True
    assert __ISBNChecker("9789571325555").is_isbn_13() is False
    assert __ISBNChecker("B9789571325554").is_isbn_13() is False
    assert __ISBNChecker("978-957-1325-555-4").is_isbn_13() is True
    assert __ISBNChecker("978-957-1325-555-4", normalize=False).is_isbn_13() is False
    assert __ISBNChecker("97895713255548").is_isbn_13() is False



# Generated at 2022-06-14 05:47:21.376272
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('0.0.0.0') == True
    assert is_ip_v4('255.255.255.255') == True
    assert is_ip_v4('192.168.1.1') == True
    assert is_ip_v4('255.200.100.75') == True
    assert is_ip_v4('255.200.100.999') == False
    assert is_ip_v4('nope') == False
    assert is_ip_v4(None) == False

# Generated at 2022-06-14 05:47:33.784918
# Unit test for function is_email

# Generated at 2022-06-14 05:47:45.400656
# Unit test for function is_email
def test_is_email():

    assert(is_email("richard.gabriel@gmail.com") == True)
    assert(is_email("Richard.Gabriel@gmail.com") == True)
    assert(is_email("Richard..Gabriel@gmail.com") == False)
    assert(is_email("Richard...Gabriel@gmail.com") == False)

    # test no #1: as per RFC 1034, local-part of an email address is case-sensitive
    assert(is_email("richard.gabriel@gmail.com") == True)
    assert(is_email("Richard.Gabriel@gmail.com") == True)

    # test no #2: all that is before the @ symbol is the local-part and can be quoted
    assert(is_email('"Richard Gabriel"@gmail.com') == True)

    # test no #3

# Generated at 2022-06-14 05:47:54.322704
# Unit test for function is_email
def test_is_email():
    assert is_email('foo@bar.com') is True
    assert is_email('foo@bar.com.au') is True
    assert is_email('foo+bar@bar.com') is True
    assert is_email('foo-bar.com') is False
    assert is_email('foo@bar') is False
    assert is_email('foo@bar..com') is False
    assert is_email('foo@') is False
    assert is_email('@bar.com') is False
    assert is_email('a@a.a.a.a.a.com') is False
    assert is_email('foo@bar.com.') is False
    assert is_email(
        'this\\\ is\\\ a\\\ lot\\\ of\\\ escaped\\\ spaces\\ @bar.com'
    ) is True

# Generated at 2022-06-14 05:47:58.383958
# Unit test for function is_email
def test_is_email():
    assert is_email('foo@bar.com')
    assert is_email('foo@bar.com.br')
    assert is_email('foo.bar@bar.com')
    assert is_email('foo.bar@bar.co.uk')
    assert is_email('foo+bar@bar.com')
    assert is_email('foo-bar@bar.com')
    assert is_email('foo_bar@bar.com')
    assert is_email('foobar@bar.com')
    assert is_email('_foobar@bar.com')
    assert is_email('foo@bar.com.br')
    assert is_email('"foo"@bar.com')
    assert is_email('"foo bar"@bar.com')
    assert is_email('"foo.bar"@bar.com')

# Generated at 2022-06-14 05:48:00.623013
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert not __ISBNChecker('12345678901').is_isbn_13()
    assert __ISBNChecker('978000194841').is_isbn_13()


# Generated at 2022-06-14 05:48:09.600985
# Unit test for function is_json
def test_is_json():
    assert is_json('{ "foo": "bar" }') == True
    assert is_json('[1, 2, 3]') == True
    assert is_json('{nope}') == False
    assert is_json('{"foo": "bar"') == False
    assert is_json('["foo", "bar"]') == True
    assert is_json('true') == True
    assert is_json('false') == True
    assert is_json('') == False
    assert is_json(None) == False


# Generated at 2022-06-14 05:48:20.054808
# Unit test for function is_email
def test_is_email():
    assert not is_email('@gmail.com')
    assert not is_email('@')
    assert not is_email(' . ')
    assert not is_email('me@otheremail@googlemail.com')
    assert not is_email('')
    assert not is_email('@googlemail.com')
    assert not is_email('my.email@the-provider.com')
    assert not is_email('$%/^&@googlemail.com')
    assert not is_email('date@gmail.com')
    assert not is_email('date@gmailcom')
    assert not is_email('@gmail.com')
    assert not is_email('me@gmail.com')
    assert not is_email('.me@gmail.com')
    assert not is_email('.@gmail.com')
   

# Generated at 2022-06-14 05:48:27.184743
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker('0-321-14653-0').is_isbn_10() == True # ISBN 10 valid
    assert __ISBNChecker('0-321-14653-1').is_isbn_10() == False # ISBN 10 invalid
    assert __ISBNChecker('0-3211-4653-0').is_isbn_10() == False # ISBN 10 invalid
    assert __ISBNChecker('-0-3211-4653-0').is_isbn_10() == False # ISBN 10 invalid