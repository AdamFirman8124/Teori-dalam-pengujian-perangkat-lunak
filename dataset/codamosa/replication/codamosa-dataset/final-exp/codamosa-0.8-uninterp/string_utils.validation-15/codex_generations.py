

# Generated at 2022-06-14 05:38:49.289395
# Unit test for function is_ip
def test_is_ip():
    # Positive test
    assert is_ip('255.200.100.75')
    assert is_ip('2001:db8:85a3:0000:0000:8a2e:370:7334')
    # Negative test
    assert is_ip('1.2.3') == False



# Generated at 2022-06-14 05:38:53.473220
# Unit test for function is_isbn
def test_is_isbn():
    assert is_isbn("9780312498580") == True
    assert is_isbn("1506715214") == True


# Generated at 2022-06-14 05:38:56.252590
# Unit test for function is_isbn
def test_is_isbn():
    assert is_isbn('9780312498580')
    assert is_isbn('1506715214')
    assert not is_isbn('978031249858')
    assert not is_isbn('978-0312498580', normalize=False)


# Generated at 2022-06-14 05:39:05.468775
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    good_isbn_set = [
        '9780982477500',
        '978-979-099-210-1',
        '978-0-00-811679-3',
        '978-3-16-148410-0',
        '978-1-4028-9462-6',
        '978-3-16-148410-0',
    ]
    bad_isbn_set = [
        '978098247750',
        '978-979-099-210-',
        '978-0-00-811679-',
        '978-3-16-148410-1',
        '978-1-4028-9462-7',
        '978-3-16-148410-2',
    ]


# Generated at 2022-06-14 05:39:11.809962
# Unit test for function is_ip_v4
def test_is_ip_v4():
    """
    Tests the function is_ip_v4.

    :return: Nothing
    """
    assert is_ip_v4('') is False
    assert is_ip_v4('a') is False
    assert is_ip_v4('a.b') is False
    assert is_ip_v4('256.b') is False
    assert is_ip_v4('255.200.100.999') is False
    assert is_ip_v4('255.200.100.75') is True



# Generated at 2022-06-14 05:39:19.809779
# Unit test for function is_ip
def test_is_ip():
    assert not is_ip('2001:db8:85a3:0000:0000:8a2e:370:?#')
    assert is_ip('2001:db8:85a3:0000:0000:8a2e:370:7334')
    assert is_ip('255.200.100.75')
    assert not is_ip('1.2.3')
test_is_ip()

# Generated at 2022-06-14 05:39:25.102880
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker('0-306-40615-2').is_isbn_10()
    assert __ISBNChecker('1847192106').is_isbn_10()
    assert not __ISBNChecker('019282347214').is_isbn_10()



# Generated at 2022-06-14 05:39:37.154744
# Unit test for function is_email
def test_is_email():
    # Test the happy path
    assert(is_email("z@z.com"))
    assert(is_email("test@test.com"))
    assert(is_email("test@test.test.test.test.test.test.test.test.test.test.test.test.test.test.test.test.test.test.test"))
    assert(is_email("test@test.test.test.test.test.test.test.test.test.test.test.test.test.test.test.test.test.test.test.test"))
    assert(is_email("1@1.1"))
    assert(is_email("1@1.1.1"))
    assert(is_email("1@1.1.1.1"))

# Generated at 2022-06-14 05:39:50.214893
# Unit test for function is_email
def test_is_email():
    assert is_email('test@test.com')
    # assert is_email('test@test.com ')
    assert is_email('test+test@test.com')
    assert is_email('"test"@test.com')
    assert is_email('test.test@test.com')
    assert is_email('"test\.test"@test.com')
    assert is_email('test.test@test.com')
    assert is_email('te.st@test.com')
    assert is_email('test@te.st.com')
    assert is_email('test@test.com')
    assert is_email('test@test.co.uk')

    assert not is_email('test@')
    assert not is_email('@test.com')
    assert not is_email('test.test')


# Generated at 2022-06-14 05:39:57.106845
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker("9780306406157").is_isbn_13()
    assert not __ISBNChecker("9780306406158").is_isbn_13()
    assert not __ISBNChecker("978030640615").is_isbn_13()
    assert not __ISBNChecker("97803064061577").is_isbn_13()



# Generated at 2022-06-14 05:40:10.827789
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('127.0.0.1') == True
    assert is_ip_v4('255.200.100.75') == True
    assert is_ip_v4('nope') == False
    assert is_ip_v4('255.200.100.999') == False
    assert is_ip_v4('255.200.100.75.80') == False

# Generated at 2022-06-14 05:40:16.207257
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') is True
    assert is_json('[1, 2, 3]') is True
    assert is_json('{nope}') is False


# Generated at 2022-06-14 05:40:17.932467
# Unit test for function is_url
def test_is_url():
    import doctest
    doctest.testmod()


# Generated at 2022-06-14 05:40:20.537477
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    isbn = __ISBNChecker('080442957X')
    isbn.is_isbn_10()


# PUBLIC API



# Generated at 2022-06-14 05:40:26.141317
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com') == True
    assert is_email('@gmail.com') == False
    assert is_email('@') == False
    assert is_email('a@a') == False
    assert is_email('a@a.a') == True
    assert is_email('a@a.com') == True
    assert is_email('ab@a.com') == True
    assert is_email('abc@a.com') == True
    assert is_email('a..b@a.com') == False
    assert is_email('a.b@a.com') == True
    assert is_email('a.b.c@a.com') == True
    assert is_email('a.bc@a.com') == True

# Generated at 2022-06-14 05:40:29.662494
# Unit test for function is_json
def test_is_json():
    assert is_json("{'x': 'y'}") == True
    assert is_json("[1, 2, 3]") == True
    assert is_json("this is not json") == False


# Generated at 2022-06-14 05:40:43.165547
# Unit test for function is_email

# Generated at 2022-06-14 05:40:53.089465
# Unit test for function is_email
def test_is_email():
    assert not is_email('')
    assert not is_email('test')
    assert not is_email('test@test')
    assert not is_email('test@test.')
    assert not is_email('test.@test.com')
    assert not is_email('test@test.com ')
    assert not is_email(' test@test.com')
    assert not is_email('te st@test.com')
    assert not is_email('test@te.st.com')
    assert is_email('test@test.com')
    assert is_email('test@test.co.uk')
    assert is_email('test@test.co.uk')
    assert is_email('t.e.s.t@test.com')

# Generated at 2022-06-14 05:40:56.720689
# Unit test for function is_url
def test_is_url():
    assert is_url('http://www.mysite.com') == True
    assert is_url('https://mysite.com') == True
    assert is_url('.mysite.com') == False



# Generated at 2022-06-14 05:41:01.471607
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name":"Peter","age":null}') == True
    assert is_json('[1, 2, 3]') == True
    assert is_json('{nope}') == False
#test_is_json()



# Generated at 2022-06-14 05:41:09.589001
# Unit test for function is_credit_card
def test_is_credit_card():
    assert is_credit_card("365844926830494", "AMERICAN_EXPRESS") == True


# Generated at 2022-06-14 05:41:11.455366
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
	isbn_checker = __ISBNChecker("0446310786")
	return isbn_checker.is_isbn_10()



# Generated at 2022-06-14 05:41:22.253936
# Unit test for function is_credit_card
def test_is_credit_card():
    assert is_credit_card('4111111111111111')
    assert is_credit_card('4111 1111 1111 1111')
    assert is_credit_card('4111-1111-1111-1111')
    assert not is_credit_card('4111-1111-1111-1112')
    assert not is_credit_card('4111-1111-1111-111')
    assert is_credit_card('4012888888881881')
    assert is_credit_card('5555555555554444')
    assert is_credit_card('5105105105105100')
    assert is_credit_card('5105 1051 0510 5100')
    assert is_credit_card('5105-1051-0510-5100')
    assert is_credit_card('6759649826438453')

# Generated at 2022-06-14 05:41:30.561579
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker('0138001424').is_isbn_10() == True
    assert __ISBNChecker('0138001425').is_isbn_10() == False
    assert __ISBNChecker('01380014424').is_isbn_10() == False
    assert __ISBNChecker('01380014244').is_isbn_10() == False
    assert __ISBNChecker('013800142A').is_isbn_10() == False


# Generated at 2022-06-14 05:41:42.894306
# Unit test for function is_email
def test_is_email():
    assert not is_email(' ')
    assert not is_email('')
    assert not is_email(None)
    assert not is_email('email@')
    assert not is_email('@')
    assert is_email('email@domain.com')
    assert is_email('"first last"@domain.com')
    assert is_email('name+tag@domain.com')
    assert is_email('name+tag@domain.com')
    assert is_email('email@domain-one.com')
    assert is_email('email@domain.name')
    assert is_email('email@domain.co.jp')
    assert is_email('firstname-lastname@domain.com')
    assert is_email('email@domain.web')
    assert is_email('firstname+lastname@domain.com')

# Generated at 2022-06-14 05:41:55.647977
# Unit test for function is_url
def test_is_url():
    assert is_url('www.domain.com') == False
    assert is_url('domain.com') == False
    assert is_url('.com') == False
    assert is_url('.com/') == False
    assert is_url('.com/subfolder') == False
    assert is_url('.com/subfolder?param=value') == False
    assert is_url('subdomain.domain.com') == False

    assert is_url('com') == False
    assert is_url('subdomain.com') == False
    assert is_url('subdomain.com/') == False
    assert is_url('subdomain.com/subfolder') == False
    assert is_url('subdomain.com/subfolder?param=value') == False

    assert is_url('http://subdomain.com') == True

# Generated at 2022-06-14 05:42:03.471969
# Unit test for function is_email
def test_is_email():
    assert is_email('john.doe@the-provider.com') is True
    assert is_email('john.doe@the-provider.com') is True
    assert is_email('.john.doe@the-provider.com') is False
    assert is_email('john.doe.@the-provider.com') is False
    assert is_email('john..doe@the-provider.com') is False
    assert is_email('john.doe@the-provider..com') is False
    assert is_email('.john.doe@the-provider.com') is False
    assert is_email('john.doe@the-provider.com.') is False
    assert is_email('john.doe@the-provider..com') is False

# Generated at 2022-06-14 05:42:11.858278
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com') == True
    assert is_email('@gmail.com') == False
    assert is_email('my.email@the-provider,com') == False
    assert is_email('my.email@the-provider.c') == False
    assert is_email('my.email@the-provider.com.') == False
    assert is_email('my.email@the-provider.com?') == False
    assert is_email('.my.email@the-provider.com') == False
    assert is_email('my.email@the-provider.com ') == False
    assert is_email('my.email@the-provider.com\n') == False



# Generated at 2022-06-14 05:42:22.618086
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():

    assert __ISBNChecker('9788376119269').is_isbn_13() == True
    assert __ISBNChecker('9788376119268').is_isbn_13() == False
    assert __ISBNChecker('9788376192690').is_isbn_13() == False
    assert __ISBNChecker('9788376119260').is_isbn_13() == False
    assert __ISBNChecker('9788376192697').is_isbn_13() == False

    assert __ISBNChecker('9780201379624').is_isbn_13() == True
    assert __ISBNChecker('9780201379623').is_isbn_13() == False
    assert __ISBNChecker('9780201370624').is_isbn_13() == False


# Generated at 2022-06-14 05:42:24.914453
# Unit test for function is_url
def test_is_url():
    return 'unit test has not been created'

# Generated at 2022-06-14 05:42:34.368229
# Unit test for function is_ip_v4
def test_is_ip_v4():
    ip = '255.200.100.75'
    ip2 = '255.200.100.999'
    assert is_ip_v4(ip) == True
    assert is_ip_v4(ip2) == False

#We test the function with the 2 examples from the documentation
test_is_ip_v4()



# Generated at 2022-06-14 05:42:36.616583
# Unit test for function is_json
def test_is_json():
    assert is_json('{}')
    assert is_json('[]')


# Generated at 2022-06-14 05:42:43.260223
# Unit test for function is_ip_v4
def test_is_ip_v4():
    correct_ip_v4 = "216.3.128.12"
    not_correct_ip_v4 = "999.3.128.12"
    assert is_ip_v4(correct_ip_v4) == True
    assert is_ip_v4(not_correct_ip_v4) == False
test_is_ip_v4()


# Generated at 2022-06-14 05:42:48.831597
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75') == True
    assert is_ip_v4('nope') == False
    assert is_ip_v4('255.200.100.999') == False
    assert is_ip_v4('255.200') == False


# Generated at 2022-06-14 05:42:56.118743
# Unit test for function is_url
def test_is_url():
    assert is_url('http://www.mysite.com')
    assert is_url('http://www.mysite.com', ['http','ftp'])
    assert not is_url('http://www.mysite.com', ['https','ftp'])
    assert is_url('http://192.168.0.1')
    assert not is_url('http://192.168.0.1/page.html#test')
    
    

# Generated at 2022-06-14 05:42:59.811503
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') == True
    assert is_json('[1, 2, 3]') == True
    assert is_json('{nope}') == False


# Generated at 2022-06-14 05:43:07.488676
# Unit test for function is_email
def test_is_email():
    print(is_email(input_string='galilio.tang@gmail.com'))
    print(is_email(input_string='galilio.tang.xiaojun@gmail.com'))
    print(is_email(input_string='galilio.tang.xiaojun@gmail.com'))
    print(is_email(input_string='galilio.tang.xiaojun@gmai.com'))
    print(is_email(input_string='galilio.tang.xiaojun@gmail.com.cn'))
    print(is_email(input_string='galilio.tang.xiaojun@gmail.cn'))
    print(is_email(input_string='galilio.tang.xiaojun@gmail.net'))

# Generated at 2022-06-14 05:43:09.970973
# Unit test for function is_url
def test_is_url():
    assert is_url('http://www.mysite.com') == True
    assert is_url('https://mysite.com') == True
    assert is_url('.mysite.com') == False


# Generated at 2022-06-14 05:43:14.413766
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75')
    assert not is_ip_v4('nope')
    assert not is_ip_v4('255.200.100.999')
    assert is_ip_v4('0.0.0.1')
    assert is_ip_v4('1.1.1.1')
    assert not is_ip_v4('0.0.0.256')
    assert not is_ip_v4('')


# Generated at 2022-06-14 05:43:18.299081
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com') == True
    assert is_email('@gmail.com') == False



# Generated at 2022-06-14 05:43:25.439022
# Unit test for function is_email
def test_is_email():
    print('test_is_email')
    assert(is_email('fjabou@gmail.com'))
    assert(not is_email('fjabou.com'))
    assert(not is_email('hello.world@gmail.com'))
    
    


# Generated at 2022-06-14 05:43:30.850431
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com')
    assert not is_email('@gmail.com')

# Credit Card Numbers:
# https://gist.github.com/webbdev/6120876

# Generated at 2022-06-14 05:43:35.393860
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}')
    assert is_json('[1, 2, 3]')
    assert not is_json('{nope}')



# Generated at 2022-06-14 05:43:44.569470
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75')
    assert is_ip_v4('255.200.100.77')
    assert is_ip_v4('192.168.1.1')
    assert not is_ip_v4('')
    assert not is_ip_v4('nope')
    assert not is_ip_v4('255.200.100.999')
    assert not is_ip_v4('192.168.1.')
    assert not is_ip_v4('hello.200.100.75')



# Generated at 2022-06-14 05:43:56.708344
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker("9780247154343").is_isbn_10() == False
    assert __ISBNChecker("97802475154343").is_isbn_10() == False
    assert __ISBNChecker("97802475154341").is_isbn_10() == False
    assert __ISBNChecker("0247515434").is_isbn_10() == True
    assert __ISBNChecker("0-2475-15434").is_isbn_10() == True
    assert __ISBNChecker("0-2475-15434").is_isbn_10() == True
    assert __ISBNChecker("0-2471-5716-3").is_isbn_10() == True
    assert __ISBNChecker("0-2471-5716-2").is_isbn

# Generated at 2022-06-14 05:43:59.296052
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker('9781234567897').is_isbn_13() == True
    assert __ISBNChecker('9781234567890').is_isbn_13() == False



# Generated at 2022-06-14 05:44:08.943775
# Unit test for method is_isbn_10 of class __ISBNChecker

# Generated at 2022-06-14 05:44:19.676732
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():

    assert __ISBNChecker('978-1-56619-909-4').is_isbn_13()
    assert __ISBNChecker('978-1-56619-909-4', normalize=False).is_isbn_13()
    assert __ISBNChecker('9781566199094').is_isbn_13()
    assert not __ISBNChecker('9781-56619-909-4', normalize=False).is_isbn_13()
    assert not __ISBNChecker('9781-56619-909-4', normalize=False).is_isbn_13()
    assert not __ISBNChecker('978-1-56619-909-5').is_isbn_13()

# Generated at 2022-06-14 05:44:32.338298
# Unit test for function is_email
def test_is_email():
    assert is_email('"Abc\@def"@example.com')
    assert not is_email('"Fred\ Bloggs"@example.com')
    assert not is_email('"Joe.\\Blow"@example.com')
    assert is_email('"Abc@def"@example.com')
    assert is_email('customer/department=shipping@example.com')
    assert not is_email('$A12345@example.com')
    assert is_email('!def!xyz%abc@example.com')
    assert is_email('_somename@example.com')
    assert not is_email('/@example.com')
    assert not is_email('\"Abc@def\"@example.com')

# Generated at 2022-06-14 05:44:37.178994
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    checker = __ISBNChecker('978-3-16-148410-0')
    assert checker.is_isbn_13() is True

    checker = __ISBNChecker('978-1-61145-0')
    assert checker.is_isbn_13() is False

# Generated at 2022-06-14 05:44:54.864128
# Unit test for function is_email
def test_is_email():
    assert is_email('foo@gmail.com')
    assert is_email('foo@example.com')
    assert is_email('foo.bar@example.com')
    assert is_email('foo.bar@sub.example.com')
    assert not is_email('foo.bar@sub..example.com')
    assert not is_email('foo.@sub.example.com')
    assert not is_email('foo.bar@sub.example')
    assert is_email('"foo+bar@sub.example.com"') # with escaped special characters
    assert is_email('"foo\\@bar"@sub.example.com')
    assert not is_email('"foo\\@bar"@sub.example.com@gmail.com')
    assert is_email('foo.bar@sub..example.com') # but this is a

# Generated at 2022-06-14 05:45:02.157563
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') == True, 'The string is json'
    assert is_json('[1,2,3]') == True, 'The string is json'
    assert is_json('{nope}') == False, 'The string is not json'

test_is_json()



# Generated at 2022-06-14 05:45:12.319024
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker('123456789X').is_isbn_10() == True
    assert __ISBNChecker('1234567890').is_isbn_10() == True
    assert __ISBNChecker('1234567899').is_isbn_10() == True
    assert __ISBNChecker('1234567897').is_isbn_10() == False
    assert __ISBNChecker('123456789V').is_isbn_10() == False
    assert __ISBNChecker('123456789').is_isbn_10() == False
    assert __ISBNChecker('1234567890X').is_isbn_10() == False


# PUBLIC API



# Generated at 2022-06-14 05:45:26.768216
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    checker = __ISBNChecker(input_string='')
    assert checker.is_isbn_10() is False

    checker = __ISBNChecker(input_string='978-3-16-148410-0')
    assert checker.is_isbn_10() is True

    checker = __ISBNChecker(input_string='9783161484100')
    assert checker.is_isbn_10() is True

    checker = __ISBNChecker(input_string='978-3-16-148410-1')
    assert checker.is_isbn_10() is True

    checker = __ISBNChecker(input_string='978-3-16-148410-9')
    assert checker.is_isbn_10() is True

    checker = __

# Generated at 2022-06-14 05:45:30.115054
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75') == True
    assert is_ip_v4('nope') == False
    assert is_ip_v4('255.200.100.999') == False


# Generated at 2022-06-14 05:45:33.980136
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker('0789751984').is_isbn_10()


# Generated at 2022-06-14 05:45:38.028936
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    input_string = "156881111X"
    isbn = __ISBNChecker(input_string, False)
    assert isbn.is_isbn_10() == True

# Generated at 2022-06-14 05:45:49.646232
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com') == True
    assert is_email('email@e.mail') == True
    assert is_email('email@e.m.a.i.l') == True
    assert is_email('email@e.m.a.i.l.') == False
    assert is_email('email@e..mail') == False
    assert is_email('email@e..m.a.i.l') == False
    assert is_email('email@e.m.a.i..l') == False
    assert is_email('email@e.m.a..i.l') == False
    assert is_email('email@e.m..a.i.l') == False
    assert is_email('email@e..m.a.i.l') == False

   

# Generated at 2022-06-14 05:45:55.809732
# Unit test for function is_ip_v4
def test_is_ip_v4():
        assert(is_ip_v4('255.200.100.75') == True)
        assert(is_ip_v4('nope') == False)
        assert(is_ip_v4('255.200.100.999') == False)
        print("test_is_ip_v4() passed")

test_is_ip_v4()



# Generated at 2022-06-14 05:45:59.372167
# Unit test for function is_json
def test_is_json():
    assert not is_json('{"id": 1}')
    assert not is_json('[1, 2, 3]')
    assert not is_json('{"name": "Peter"}')
    assert not is_json('{"nope"}')


# Generated at 2022-06-14 05:46:08.674843
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker("8362211102").is_isbn_10() == True
    assert __ISBNChecker("8362211103").is_isbn_10() == False


# PUBLIC API


# STRING

# Generated at 2022-06-14 05:46:13.560958
# Unit test for function is_json
def test_is_json():
    assert(is_json('{"name": "Peter"}') == True)
    assert(is_json('[1, 2, 3]') == True)
    assert(is_json('{nope}') == False)
test_is_json()



# Generated at 2022-06-14 05:46:23.819903
# Unit test for function is_email

# Generated at 2022-06-14 05:46:27.629786
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') == True
    assert is_json('[1, 2, 3]') == True
    assert is_json('{nope}') == False

# Generated at 2022-06-14 05:46:40.695381
# Unit test for function is_email
def test_is_email():
    assert is_email('john.doe@domain.com') == True
    assert is_email('john.doe@domain') == False
    assert is_email('john.doe@domain.co') == True
    assert is_email('john.doe@domain.comasd') == False
    assert is_email('john.doe@domain.c') == False
    assert is_email('john.doe@domain.coasd') == False
    assert is_email('john.doe@domain.asdasd') == False
    assert is_email('john.doe@domain.u') == False
    assert is_email('john.doe@domain.t') == False
    assert is_email('john.doe@domain.cou') == False

# Generated at 2022-06-14 05:46:50.945517
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75')
    assert is_ip_v4('0.0.0.0')
    assert is_ip_v4('255.255.255.255')
    assert not is_ip_v4('nope')
    assert not is_ip_v4('255.200.100.999')
    assert not is_ip_v4(None)
    assert not is_ip_v4('')
    assert not is_ip_v4(' ')



# Generated at 2022-06-14 05:46:55.821162
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75')
    assert not is_ip_v4('nope')
    assert not is_ip_v4('255.200.100.999')
test_is_ip_v4()



# Generated at 2022-06-14 05:47:09.037594
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    input_string = '0131103628'
    checker = __ISBNChecker(input_string)
    assert checker.is_isbn_10()
    input_string = '978-0131103628'
    checker = __ISBNChecker(input_string)
    assert checker.is_isbn_10()
    input_string = '9780131103628'
    checker = __ISBNChecker(input_string)
    assert checker.is_isbn_10()
    input_string = '978-013110362'
    checker = __ISBNChecker(input_string)
    assert not checker.is_isbn_10()
    input_string = '978-01311036296'
    checker = __ISBNChecker(input_string)


# Generated at 2022-06-14 05:47:18.309931
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com') == True
    assert is_email('my-email@the-provider.com') == True
    assert is_email('"my email"@the-provider.com') == True
    assert is_email('"my.email"@the-provider.com') == True
    assert is_email('my.email@the-provider.com') == True
    assert is_email('my.email@the-provider.com') == True
    assert is_email('my.email@the-provider.com') == True
    assert is_email('my.email@the-provider.com') == True
    assert is_email('my.email@the-provider.com') == True

# Generated at 2022-06-14 05:47:30.484888
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    checker = __ISBNChecker('0471958697')
    assert checker.is_isbn_10() == True

    checker = __ISBNChecker('0-321-14653-0')
    assert checker.is_isbn_10() == True

    checker = __ISBNChecker('877 1 95 869x')
    assert checker.is_isbn_10() == True

    checker = __ISBNChecker('877 1 95 869x', normalize=False)
    assert checker.is_isbn_10() == False

    checker = __ISBNChecker('000-0')
    assert checker.is_isbn_10() == False

    checker = __ISBNChecker('0-321@14653-0')
    assert checker.is_isbn_10()

# Generated at 2022-06-14 05:47:41.189472
# Unit test for function is_json
def test_is_json():
    assert(is_json('{"name": "Peter"}'))
    assert(is_json('[1, 2, 3]'))
    assert(not is_json('{nope}'))



# Generated at 2022-06-14 05:47:45.339436
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert not __ISBNChecker('1234567890123').is_isbn_13()
    assert __ISBNChecker('277862193X').is_isbn_13()
    assert __ISBNChecker('9782778621938').is_isbn_13()



# Generated at 2022-06-14 05:47:47.571403
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker.is_isbn_13(None, None) is None


# Generated at 2022-06-14 05:47:53.970409
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75')
    assert not is_ip_v4('nope')
    assert not is_ip_v4('255.200.100.999')
    assert not is_ip_v4('0.0.0.0.0')



# Generated at 2022-06-14 05:48:01.161986
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker(
        '9780201483416'
    ).is_isbn_13() == True, 'Should be True'

    assert __ISBNChecker(
        '1234567890123'
    ).is_isbn_13() == False, 'Should be False'
## end of test___ISBNChecker_is_isbn_13


# Generated at 2022-06-14 05:48:10.988282
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker('B007E8HXNW').is_isbn_10() is False
    assert __ISBNChecker('3864903572').is_isbn_10() is True
    assert __ISBNChecker('9783864903571').is_isbn_10() is False

    assert __ISBNChecker('1A2B3C4D5E6').is_isbn_10() is False
    assert __ISBNChecker('1234567890').is_isbn_10() is True
    assert __ISBNChecker('12345678901').is_isbn_10() is False


# Generated at 2022-06-14 05:48:21.586454
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com') == True
    assert is_email('@gmail.com') == False

# Generated at 2022-06-14 05:48:30.970127
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker('978-0470421352').is_isbn_13() is True
    assert __ISBNChecker('978-1449365035').is_isbn_13() is True
    assert __ISBNChecker('978-1491901632').is_isbn_13() is True
    assert __ISBNChecker('978-1491918954').is_isbn_13() is True
    assert __ISBNChecker('978-1491918954').is_isbn_13() is True
    assert __ISBNChecker('978-1491905012').is_isbn_13() is True
    assert __ISBNChecker('978-1491905013').is_isbn_13() is True
