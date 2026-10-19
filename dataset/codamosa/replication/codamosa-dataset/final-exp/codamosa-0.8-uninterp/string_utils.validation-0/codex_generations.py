

# Generated at 2022-06-14 05:38:42.720951
# Unit test for function is_ip_v4
def test_is_ip_v4():
    if not is_ip_v4('255.200.100.75'):
        print('failed: is_ip_v4')

# Generated at 2022-06-14 05:38:54.106927
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker('a').is_isbn_13() == False
    assert __ISBNChecker('1234567890123').is_isbn_13() == True
    assert __ISBNChecker('978-1-56619-909-4').is_isbn_13() == True
    assert __ISBNChecker('1-56619-909-5').is_isbn_13() == False
    assert __ISBNChecker('1-56619-909-4', normalize=False).is_isbn_13() == False
    print('Method is_isbn_13 of class __ISBNChecker is passed.')


# Generated at 2022-06-14 05:38:59.943347
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75') == True
    assert is_ip_v4('nope') == False
    assert is_ip_v4('255.200.100.999') == False

test_is_ip_v4()



# Generated at 2022-06-14 05:39:11.717992
# Unit test for function is_credit_card
def test_is_credit_card():
    # Testing the base functionality of the is_credit_card() function
    assert is_credit_card("6011000990139424") == True
    assert is_credit_card("378734493671000") == True
    assert is_credit_card("348439315365973") == True
    assert is_credit_card("348006087288750") == True
    assert is_credit_card("35280088684645") == True
    assert is_credit_card("5555555555554444") == True
    assert is_credit_card("2223003122003222") == True
    assert is_credit_card("") == False
    assert is_credit_card("fhbwehfb") == False
    assert is_credit_card("348439315365973") == True

# Generated at 2022-06-14 05:39:22.722797
# Unit test for function is_credit_card
def test_is_credit_card():
    assert is_credit_card('4111111111111111') == True  # VISA
    assert is_credit_card('5500000000000004') == True  # MASTERCARD
    assert is_credit_card('378282246310005') == True  # AMERICAN_EXPRESS
    assert is_credit_card('30569309025904') == True  # DINERS_CLUB
    assert is_credit_card('6011111111111117') == True  # DISCOVER
    assert is_credit_card('3530111333300000') == True  # JCB
    assert is_credit_card('4111-1111-1111-1111') == False



# Generated at 2022-06-14 05:39:26.281866
# Unit test for function is_url
def test_is_url():
    assert is_url('http://www.mysite.com')
    assert is_url('https://mysite.com')
    assert not is_url('.mysite.com')

# Generated at 2022-06-14 05:39:27.107321
# Unit test for function is_ip
def test_is_ip():
    assert is_ip('255.200.100.75') == True
    

# Generated at 2022-06-14 05:39:30.823017
# Unit test for function is_isbn
def test_is_isbn():
    assert is_isbn('9780312498580')
    assert is_isbn('1506715214')
    assert not is_isbn('9780000000000')
    assert not is_isbn('150715214')
    assert not is_isbn('hello')
    assert not is_isbn('')
    assert not is_isbn(None)
    assert not is_isbn(True)
    assert not is_isbn([])
    assert not is_isbn({})



# Generated at 2022-06-14 05:39:33.315416
# Unit test for function is_credit_card
def test_is_credit_card():
    assert is_credit_card('4111111111111111') == True
    assert is_credit_card('5105105105105100') == True
    assert is_credit_card('5105105105105106') == False


# Generated at 2022-06-14 05:39:43.630081
# Unit test for function is_palindrome
def test_is_palindrome():
    test_string = 'Madam, I\'m Adam.'
    assert is_palindrome(test_string)
    assert is_palindrome(test_string,ignore_case=True)
    assert is_palindrome(test_string,ignore_spaces=True)
    assert is_palindrome(test_string,ignore_case=True,ignore_spaces=True)
    test_string = 'Madam, I\'m Adam.'
    assert not is_palindrome(test_string,ignore_case=False,ignore_spaces=False)
    test_string = 'Madamiamadam'
    assert not is_palindrome(test_string)
    test_string = 'Madamiamadam'
    assert not is_palindrome(test_string,ignore_case=True)
    test_string

# Generated at 2022-06-14 05:39:53.466679
# Unit test for function is_ip
def test_is_ip():
    assert is_ip('255.200.100.75') == True
    assert is_ip('2001:db8:85a3:0000:0000:8a2e:370:7334') == True
    assert is_ip('1.2.3') == False
test_is_ip()

# Generated at 2022-06-14 05:40:06.071171
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com') is True
    assert is_email('.my.email@the-provider.com') is False
    assert is_email('my.email.@the-provider.com') is False
    assert is_email('my.email..something@the-provider.com') is False
    assert is_email('my.email\\ something@the-provider.com') is False
    assert is_email('my.email@the-provider.com\\ something') is True
    assert is_email('"\ has space"@the-provider.com') is True
    assert is_email('"\ has space"@the-provider.com\ has space') is False
    assert is_email('') is False



# Generated at 2022-06-14 05:40:14.056228
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') == True
    assert is_json('[1, 2, 3]') == True
    assert is_json('{"name": "Peter", "age": 40}') == True
    assert is_json('{"name": "Peter", "age": 40, "city": "New York"}') == True
    assert is_json('{nope}') == False
    assert is_json('') == False
test_is_json()



# Generated at 2022-06-14 05:40:26.764103
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker(input_string='978-0-306-40615-7').is_isbn_13() is True
    assert __ISBNChecker(input_string='978-0-306-40615-4').is_isbn_13() is False
    assert __ISBNChecker(input_string='978 0 306 40615 7').is_isbn_13() is True
    assert __ISBNChecker(input_string='9780306406157').is_isbn_13() is True
    assert __ISBNChecker(input_string='9780306406154').is_isbn_13() is False
    assert __ISBNChecker(input_string='A9780306406157').is_isbn_13() is False

# Generated at 2022-06-14 05:40:30.025294
# Unit test for function is_ip
def test_is_ip():
    assert is_ip('255.200.100.75') is True
    assert is_ip('2001:db8:85a3:0000:0000:8a2e:370:7334') is True
    assert is_ip('1.2.3') is False
test_is_ip()


# # Full (absolute) path example:
# # C:\folder\subfolder\file.txt
# # C:/folder/subfolder/file.txt
# # \folder\subfolder\file.txt
# # /folder/subfolder/file.txt

# Generated at 2022-06-14 05:40:34.732370
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com')
    assert is_email('my.email@the-provider.com')
    assert not is_email('@gmail.com')
    assert not is_email('hello@')
    assert not is_email('@')



# Generated at 2022-06-14 05:40:36.826925
# Unit test for function is_ip
def test_is_ip():
    assert is_ip('255.200.100.75') == True
    assert is_ip('2001:db8:85a3:0000:0000:8a2e:370:7334') == True
    assert is_ip('1.2.3') == False
    
test_is_ip()


# Generated at 2022-06-14 05:40:44.924695
# Unit test for function is_ip
def test_is_ip():
    assert is_ip('255.200.100.75') == True, "ip should be validated"
    assert is_ip('2001:db8:85a3:0000:0000:8a2e:370:7334') == True, "ip should be validated"
    assert is_ip('1.2.3') == False, "ip should not be validated"

# Generated at 2022-06-14 05:40:48.293469
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75') == True
    assert is_ip_v4('nope') == False
    assert is_ip_v4('255.200.100.999') == False


# Generated at 2022-06-14 05:41:01.805371
# Unit test for function is_email
def test_is_email():
    assert is_email('Dinh.Hieu.TK@gmail.com') == True
    assert is_email('Dinh.Hieu.TK@gmail.com') == True
    assert is_email('Dinh.Hieu.TK@gmail.com') == True
    assert is_email('Dinh.Hieu.TK@gmail.com') == True
    assert is_email('Dinh.Hieu.TK@gmail.com') == True
    assert is_email('Dinh.Hieu.TK@gmail.com') == True
    assert is_email('Dinh.Hieu.TK@gmail.com') == True
    assert is_email('Dinh.Hieu.TK@gmail.com') == True

# Generated at 2022-06-14 05:41:21.183732
# Unit test for method is_isbn_10 of class __ISBNChecker

# Generated at 2022-06-14 05:41:33.818554
# Unit test for function is_credit_card
def test_is_credit_card():
    assert not is_credit_card('1234')
    assert not is_credit_card('')
    assert is_credit_card('4532848765293')
    assert is_credit_card('4532848765293921')
    assert not is_credit_card(4532848765293921)
    assert is_credit_card('4929908534235910')
    assert is_credit_card('5556555555555557')
    assert is_credit_card('37195853177634')
    assert is_credit_card('3719585317763')
    assert not is_credit_card('37195853177')
    assert is_credit_card('30569309025904')
    assert not is_credit_card('305693090259045')
    assert not is_

# Generated at 2022-06-14 05:41:38.756767
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker('978-3-16-148410-0').is_isbn_13() == True
    assert __ISBNChecker('978-3-16-148410-x').is_isbn_13() == False
    assert __ISBNChecker('978-3-16-14841-x').is_isbn_13() == False
    assert __ISBNChecker('978-3-16-148411-0').is_isbn_13() == False
    assert __ISBNChecker('978-3-16-14841-00').is_isbn_13() == False


# Generated at 2022-06-14 05:41:47.014292
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker('9780140449300').is_isbn_10() == False
    assert __ISBNChecker('0140449304').is_isbn_10() == True
    assert __ISBNChecker('0140039907').is_isbn_10() == True
    assert __ISBNChecker('161729120X').is_isbn_10() == True
    assert __ISBNChecker('978-1-61729-120-6').is_isbn_10() == True
    assert __ISBNChecker('0140449305').is_isbn_10() == False
    assert __ISBNChecker('X61729120').is_isbn_10() == False  # Invalid letter in the end
    assert __ISBNChecker('X6172912').is_isbn_10() == False

# Generated at 2022-06-14 05:41:58.730377
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    checker = __ISBNChecker(input_string='978-1-4711-5839-4')
    assert checker.is_isbn_13()
    checker = __ISBNChecker(input_string='9780133957059')
    assert checker.is_isbn_13()
    checker = __ISBNChecker(input_string='978-1-4671-5839-4')
    assert not checker.is_isbn_13()
    checker = __ISBNChecker(input_string='97801339570')
    assert not checker.is_isbn_13()
    checker = __ISBNChecker(input_string='9780133957058')
    assert not checker.is_isbn_13()

# Generated at 2022-06-14 05:42:09.881169
# Unit test for function is_email
def test_is_email():
    assert is_email('foo@bar.com') == True
    assert is_email('foo@bar.co') == True
    assert is_email('foo.bar@baz.com') == True
    assert is_email('foo.bar@baz.co') == True
    assert is_email('foo.bar@baz.co.') == False
    assert is_email('foo.bar.@baz.co') == False
    assert is_email('@baz.co') == False
    assert is_email('foo@') == False
    assert is_email('foo@bar@baz.co') == False
    assert is_email('.foo@bar.co') == False
    assert is_email('foo..bar@baz.co') == False

# Generated at 2022-06-14 05:42:22.642566
# Unit test for function is_url
def test_is_url():
    assert is_url('http://www.google.com')
    assert is_url('https://www.google.com')
    assert is_url('file:///etc/hosts')
    assert is_url('ftp://ftp.redhat.com')
    assert is_url('elo://elo.elo.elo')
    assert is_url('www.google.com', [''])
    assert is_url('http://www.google.com', ['http', 'https'])
    assert is_url('https://www.google.com', ['http', 'https'])
    assert not is_url('ftp://ftp.redhat.com', ['http', 'https'])
    assert not is_url('file:///etc/hosts', ['http', 'https'])

# Generated at 2022-06-14 05:42:27.212711
# Unit test for function is_url
def test_is_url():
    assert is_url('http://www.mysite.com') is True
    assert is_url('https://mysite.com') is True
    assert is_url('mysite.com') is False


# Generated at 2022-06-14 05:42:31.622099
# Unit test for function is_credit_card
def test_is_credit_card():
    assert is_credit_card('4012888888881881','VISA') == True
    assert is_credit_card('4012888888881881','MASTERCARD') == False

# Generated at 2022-06-14 05:42:45.119457
# Unit test for function is_email
def test_is_email():
    assert is_email('a@b.com') == True
    assert is_email('a@b.c') == True
    assert is_email('ab.com') == False
    assert is_email('') == False
    assert is_email('@b.c') == False
    assert is_email('a@b') == False
    assert is_email('a@b.c.d.e') == True
    assert is_email('a.@b.c') == False
    assert is_email('-a@b.com') == True
    assert is_email('a.b@c.com') == True
    assert is_email('a-b@c.com') == True
    assert is_email('a.b-c@d.com') == True

# Generated at 2022-06-14 05:42:53.327418
# Unit test for function is_email
def test_is_email():
    email = "a@gmail.com"
    assert is_email(email) is True, "Assertion failed"
test_is_email()

# Generated at 2022-06-14 05:42:58.837290
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    cases = [
        (("978-3-16-148410-0", False), False),
        (("978-3-16-148410-0", True), True),
        (("9783161484100", True), True)
    ]

    for data in cases:
        assert __ISBNChecker(data[0][0], data[0][1]).is_isbn_13() is data[1]



# Generated at 2022-06-14 05:43:01.160520
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker(input_string="0764526413").is_isbn_10() == True



# Generated at 2022-06-14 05:43:04.660959
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75')
    assert not is_ip_v4('nope')
    assert not is_ip_v4('255.200.100.999')

if __name__ == "__main__":
    test_is_ip_v4()

# Generated at 2022-06-14 05:43:08.746282
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():  # check if method works correctly
    checker = __ISBNChecker("978-2-1234-5680-3")
    assert checker.is_isbn_13()



# Generated at 2022-06-14 05:43:19.377947
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker("0596102074").is_isbn_13() is True
    assert __ISBNChecker("978-0596102075").is_isbn_13() is True
    assert __ISBNChecker("0596102075").is_isbn_13() is False
    assert __ISBNChecker("059610207").is_isbn_13() is False
    assert __ISBNChecker("0596102074X").is_isbn_13() is False
    assert __ISBNChecker("05961020744").is_isbn_13() is False
    assert __ISBNChecker("0596102074AB").is_isbn_13() is False



# Generated at 2022-06-14 05:43:30.994544
# Unit test for function is_email
def test_is_email():
    assert is_email('') == False
    assert is_email('a@gmail.com') == True
    assert is_email('a@g_email.com') == True
    assert is_email('a@gmail..com') == False
    assert is_email('a@gmail.com1') == True
    assert is_email('a@gmail...com') == False
    assert is_email('a@gmail.com.') == False
    assert is_email('a@gmail.c_m') == True
    assert is_email('a@gmail.c2m') == True
    assert is_email('a@gmail.c/m') == False
    assert is_email('a@gmail.com ') == False
    assert is_email('a@gmail') == False
    assert is_email('a@gmail.c') == True

# Generated at 2022-06-14 05:43:44.965523
# Unit test for function is_email
def test_is_email():
    #--BEGIN-TEST--
    # Testing the is_email function
    #--END--

    assert is_email('name@company.com') == True
    assert is_email('name@company.com') == True
    assert is_email('name.surname@company.com') == True
    assert is_email('name.surname@company.com') == True
    assert is_email('name.surname+family@company.com') == True
    assert is_email('name.surname+family@company.com') == True
    assert is_email('name.surname+family+wife@company.com') == True
    assert is_email('name.surname+family+wife@company.com') == True

# Generated at 2022-06-14 05:43:49.926201
# Unit test for function is_email
def test_is_email():
    assert is_email('user@gmail.com') == True
    assert is_email('user@hotmail.com') == True
    assert is_email('user@yahoo.com.br') == True
    assert is_email('user@yahoocom') == False


# Generated at 2022-06-14 05:43:55.665114
# Unit test for function is_email
def test_is_email():
    assert is_email('foo@bar.com') == True, 'is_email returned False for "foo@bar.com"'
    assert is_email('foo@bar.com.') == False, 'is_email returned True for "foo@bar.com."'
    assert is_email('foo@bar.c') == False, 'is_email returned True for "foo@bar.c"'



# Generated at 2022-06-14 05:44:04.866030
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75') == True
    assert is_ip_v4('nope') == False
    assert is_ip_v4('255.200.100.999') == False

test_is_ip_v4()



# Generated at 2022-06-14 05:44:10.509459
# Unit test for function is_email
def test_is_email():
    assert not is_email('my.email@the-provider.com')
    assert is_email('my.email@the-provider.com')
    
test_is_email()



# Generated at 2022-06-14 05:44:22.596548
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    obj = __ISBNChecker('0747532699')
    assert obj.is_isbn_10() == True 
    obj = __ISBNChecker('0306406152')
    assert obj.is_isbn_10() == True 
    obj = __ISBNChecker('0345339681')
    assert obj.is_isbn_10() == True 
    obj = __ISBNChecker('1568496088')
    assert obj.is_isbn_10() == True 
    obj = __ISBNChecker('0521663565')
    assert obj.is_isbn_10() == True 
    obj = __ISBNChecker('0590353403')
    assert obj.is_isbn_10() == True 
    obj = __ISBNChecker('0394800580')
   

# Generated at 2022-06-14 05:44:25.081133
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    checker = __ISBNChecker("1512147790")
    assert checker.is_isbn_13() == True
	

# Generated at 2022-06-14 05:44:33.254878
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    checker_instance = __ISBNChecker('0891907300')
    assert checker_instance.is_isbn_10() == True
    # Unit test for method is_isbn_10 of class __ISBNChecker
    def test___ISBNChecker_is_isbn_10():
        checker_instance = __ISBNChecker('0891907300')
        assert checker_instance.is_isbn_10() == True
        assert checker_instance.is_isbn_13() == False

# PUBLIC API



# Generated at 2022-06-14 05:44:44.911785
# Unit test for function is_email
def test_is_email():
    assert not is_email(" ")
    assert not is_email("@")
    assert not is_email("@gmail.com")
    assert not is_email("myemailgmail.com")
    assert not is_email("my.email@abc")
    assert not is_email("my.email@gmail.com@")
    assert not is_email("my.email@gmail.com@gmail.com")
    assert is_email("my.email@gmail.com")
    assert is_email("myemail@gmail.com")
    assert is_email("my.email+1@gmail.com")
    assert is_email("my.email@the.example.com")
    assert is_email("myemail@the-example.com")
    assert is_email("my.e.m.a.i.l@gmail.com")

# Generated at 2022-06-14 05:44:53.120959
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker('978-0-306-40615-7').is_isbn_13()
    assert __ISBNChecker('978-0-306-40615-7', normalize=False).is_isbn_13()
    assert not __ISBNChecker('0-306-40615-8').is_isbn_13()
    assert not __ISBNChecker('0-306-40615-8', normalize=False).is_isbn_13()

# Generated at 2022-06-14 05:45:05.518637
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker('10-01-99-01-23-45').is_isbn_10() == False, "invalid isbn-10"
    assert __ISBNChecker('100000000').is_isbn_10() == False, "invalid isbn-10"
    assert __ISBNChecker('0990039824').is_isbn_10() == True, "valid isbn-10"
    assert __ISBNChecker('0990039824', normalize=False).is_isbn_10() == False, "isbn-10 with dashes"
    assert __ISBNChecker('0990039824', normalize=False).is_isbn_13() == False, "isbn-10 with dashes"

# Generated at 2022-06-14 05:45:09.445513
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    isbn_checker = __ISBNChecker("978-3-89722-147-6")
    assert isbn_checker.is_isbn_13() == True

# Generated at 2022-06-14 05:45:20.526042
# Unit test for function is_json
def test_is_json():
    assert not is_json({'a': 1, 'b': 2})
    assert not is_json(['a', 'b'])
    assert not is_json(1)
    assert is_json('[1, 2, 3]')
    assert is_json('[]')
    assert is_json('[{}, {}]')
    assert is_json('{"a": 1, "b": 2}')
    assert is_json('{"a": 1, "b": [1, 2, 3]}')
    assert not is_json('{"a": 1, b:}')
    assert not is_json('{a: "hello"}')
    assert not is_json('')
    assert not is_json(None)
    assert not is_json('&')
    assert not is_json('{,}')

# Generated at 2022-06-14 05:45:33.944735
# Unit test for function is_json
def test_is_json():
    assert is_json('[1, 2, 3]') is True
    assert is_json('{"name": "Peter"}') is True
    assert is_json('{nope}') is False
    assert is_json('{"foo": "bar", "baz": "blah"}') is True
    assert is_json('[{"foo": "bar", "baz": "blah"}]') is True
    assert is_json('{]') is False
    assert is_json('{"foo": "bar", "baz": "blah"}][[{"foo": "bar", "baz": "blah"}') is False
    
    

# Generated at 2022-06-14 05:45:46.470035
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com') == True
    assert is_email('.@gmail.com') == False
    assert is_email('my..email@the-provider.com') == False
    assert is_email('myemail@gmail..com') == False
    assert is_email('my.email@the-provider.com.com') == True
    assert is_email('my.email@gmail.example.com') == True
    assert is_email('my.email@gmail.example.c') == True
    assert is_email('my.email@gmail.example.co') == True
    assert is_email('my.email@gmail.example.comb') == False
    assert is_email('my.email@gmail.example.comb.') == False

# Generated at 2022-06-14 05:45:49.255140
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():

    checker = __ISBNChecker('9165356813', normalize=False)

    assert checker.is_isbn_10()



# Generated at 2022-06-14 05:45:56.770949
# Unit test for function is_email
def test_is_email():
    assert is_email('myemail@gmail.com') == True
    assert is_email('myemail@gamil.com') == False
    assert is_email('myemail@') == False
    assert is_email('myemail@gamil.com.') == False
    assert is_email('myemail.@gamil.com') == False
    assert is_email('.myemail@gamil.com') == False
    assert is_email('myemail@@gamil.com') == False
    assert is_email('myemail@gamil..com') == False

# Generated at 2022-06-14 05:46:04.458451
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker('8870080233').is_isbn_10()
    assert __ISBNChecker('1932394699').is_isbn_10()
    assert __ISBNChecker('0679729599').is_isbn_10()
    assert __ISBNChecker('0201633612').is_isbn_10()
    assert __ISBNChecker('880874012X').is_isbn_10()
    assert __ISBNChecker('978-88-8074-012-X').is_isbn_10()
    assert __ISBNChecker('0').is_isbn_10() is False
    assert __ISBNChecker('-8870080233').is_isbn_10() is False

# Generated at 2022-06-14 05:46:08.836693
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com')
    assert is_email('my.email@the-provider.com.')
    assert not is_email('my.emailthe-provider.com')

# Generated at 2022-06-14 05:46:20.637880
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker('978-3-16-148410-0').is_isbn_13() == True
    assert __ISBNChecker('978-3-16-148410-1').is_isbn_13() == True
    assert __ISBNChecker('978-3-16-148410-2').is_isbn_13() == False
    assert __ISBNChecker('978-3-16-148410-3').is_isbn_13() == False
    assert __ISBNChecker('978-3-16-148410-4').is_isbn_13() == False
    assert __ISBNChecker('978-3-16-148410-5').is_isbn_13() == False

# Generated at 2022-06-14 05:46:34.107734
# Unit test for function is_email
def test_is_email():
    assert not is_email(None)
    assert not is_email('')
    assert not is_email(' ')
    assert not is_email('a@')
    assert not is_email('@a')
    assert not is_email('@@a')
    assert not is_email('@a.com')
    assert not is_email('a.@com')
    assert not is_email('foo.bar@a.com@b.com')
    assert is_email('foo@bar.com')
    assert is_email('foo+bar@baz.com')
    assert is_email('"foo.bar@baz.com"')
    assert is_email('foo.bar@baz.com')
    assert is_email('foo.bar@baz.com')

# Generated at 2022-06-14 05:46:37.996825
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') == True
    assert is_json('[1, 2, 3]') == True
    assert is_json('{nope}') == False


# Generated at 2022-06-14 05:46:41.717534
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com') == True
    assert is_email('@gmail.com') == False
    assert is_email('joe.doe@the-provider.com') == True



# Generated at 2022-06-14 05:46:50.769359
# Unit test for function is_json
def test_is_json():
    assert is_json('{}') is True
    assert is_json('[]') is True
    assert is_json('["test"]') is True
    assert is_json('test') is False
    is_json(None) is False



# Generated at 2022-06-14 05:47:01.290385
# Unit test for function is_ip_v4
def test_is_ip_v4():
    print("Test is_ip_v4: ", end="")
    assert not is_ip_v4("nope") # non string
    assert not is_ip_v4("") # empty
    assert not is_ip_v4("255.200.100.nope")
    assert not is_ip_v4("255.200.100.999")
    assert not is_ip_v4("255.200.100")
    assert is_ip_v4("255.200.100.75")
    assert is_ip_v4("127.0.0.1")
    assert is_ip_v4("0.0.0.0")
    assert is_ip_v4("255.255.255.255")
    assert not is_ip_v4("-123.123.123.123")

# Generated at 2022-06-14 05:47:12.558085
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com') is True
    assert is_email('@gmail.com') is False
    assert is_email('me@gmail') is False
    assert is_email('me@gmail.com.c') is False
    assert is_email('me.gmail.com') is False
    assert is_email('my.email@the-provider-222.com') is True
    assert is_email('another@email.com') is True
    assert is_email('"my email"@the-provider.com') is True
    assert is_email('=?ISO-8859-1?Q?Andr=E9?= <email@example.com>') is True
    assert is_email('another@email..com') is False
    assert is_email('another@email.c')

# Generated at 2022-06-14 05:47:17.493257
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') == True
    assert is_json('[1, 2, 3]') == True
    assert is_json('{nope}') == False


# Generated at 2022-06-14 05:47:21.884319
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75') == True
    assert is_ip_v4('nope') == False
    assert is_ip_v4('255.200.100.999') == False

# Generated at 2022-06-14 05:47:33.972828
# Unit test for function is_email
def test_is_email():
    assert is_email("bob@example.com") == True
    assert is_email("bob.smith@example.com") == True
    assert is_email("bob.smith@example.support") == True
    assert is_email("bob.smith@example.support.") == False
    assert is_email("bobsmith123@example.com") == True
    assert is_email("bobsmith123@example.support") == True
    assert is_email("bob_smith_1@example.com") == True
    assert is_email("bob_smith_1@example.support") == True
    assert is_email("bobsmith123@example_1.com") == True
    assert is_email("bobsmith123@example_1.support") == True

# Generated at 2022-06-14 05:47:46.868633
# Unit test for function is_email
def test_is_email():
    assert not is_email(None)
    assert not is_email('')
    assert not is_email(' ')
    assert not is_email('e@')
    assert not is_email('.@')
    assert not is_email('x@y..com')
    assert not is_email('.x@y.com')
    assert not is_email('\" x@y.com')
    assert not is_email('\"\"x@y.com')
    assert not is_email('x\"@y.com')
    assert not is_email('x\"y.com')
    assert is_email('x.y.com')
    assert is_email('abc.def@foo.com')
    assert is_email('abc*def@foo.com')
    assert is_email('abc_def@foo.com')


# Generated at 2022-06-14 05:47:52.552807
# Unit test for function is_json
def test_is_json():
    input_string = '[1, 2, 3]'
    assert is_json(input_string) is True
    input_string = '{nope}'
    assert is_json(input_string) is False
test_is_json()



# Generated at 2022-06-14 05:48:06.085844
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker('9788374034172').is_isbn_13() is True
    assert __ISBNChecker('978-837-403-417-2').is_isbn_13() is True
    assert __ISBNChecker('9788374034170').is_isbn_13() is False
    assert __ISBNChecker('9788374034171').is_isbn_13() is False
    assert __ISBNChecker('9788374034').is_isbn_13() is False
    assert __ISBNChecker('1').is_isbn_13() is False
    assert __ISBNChecker('abc').is_isbn_13() is False
    assert __ISBNChecker(8374034172).is_isbn_13() is False


# Generated at 2022-06-14 05:48:11.103173
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') == True
    assert is_json('[1, 2, 3]') == True
    assert is_json('{nope}') == False
    assert is_json(None) == False
    assert is_json('') == False
    assert is_json(' ') == False


# Generated at 2022-06-14 05:48:26.077015
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert not __ISBNChecker('1234567891011').is_isbn_13()
    assert not __ISBNChecker('1234567891011-1').is_isbn_13()
    assert __ISBNChecker('1234567891011').is_isbn_13()
    assert __ISBNChecker('9780143127796').is_isbn_13()
    assert __ISBNChecker('9780375869020').is_isbn_13()
    assert not __ISBNChecker('9780375869021').is_isbn_13()
    assert not __ISBNChecker('9780375869010').is_isbn_13()
    assert not __ISBNChecker('978037586-9020').is_isbn_13()
    assert not __ISBNCheck