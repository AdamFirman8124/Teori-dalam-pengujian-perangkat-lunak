

# Generated at 2022-06-14 05:38:47.909415
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    checker = __ISBNChecker('978-91-47-11341-1')
    assert checker.is_isbn_13() is True

    checker = __ISBNChecker('0-9752298-0-X')
    assert checker.is_isbn_13() is False

    checker = __ISBNChecker('978-1-5698-7486-3')
    assert checker.is_isbn_13() is False

    checker = __ISBNChecker('978-1-5698-7486-3')
    assert checker.is_isbn_13() is False

    checker = __ISBNChecker('978-1-5698-7486-3')
    assert checker.is_isbn_13() is False


# Generated at 2022-06-14 05:38:52.122248
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') == False
    assert is_json('[1, 2, 3]') == False
    assert is_json('{nope}') == False
    return True



# Generated at 2022-06-14 05:38:58.342616
# Unit test for function is_json
def test_is_json():
    # Test for valid json format
    assert is_json('{ "test_name": { "test_val": "Peter" } }') is True
    # Test for invalid json format
    assert is_json('{ "test_name": { "test_val": "Peter" }') is False



# Generated at 2022-06-14 05:39:03.727998
# Unit test for function is_email
def test_is_email():
    # true
    assert is_email('my.email@the-provider.com') == True
    # false
    assert is_email('@gmail.com') == False
    assert is_email('my.email@the-provider.com..') == False
    assert is_email('my.email@@the-provider.com') == False
    assert is_email('my.email@the-.com') == False
    assert is_email('my.email.the-provider.com') == False



# Generated at 2022-06-14 05:39:13.257457
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert True == is_ip_v4("127.0.0.1")
    assert False == is_ip_v4("128.0.0.1")
    assert False == is_ip_v4("0.0.0.0")
    assert False == is_ip_v4("255.255.255.255.255")
    assert False == is_ip_v4("255.255.256.255")
    assert False == is_ip_v4("255.255.255.256")
    assert True == is_ip_v4("127.0.0.255")


# Generated at 2022-06-14 05:39:24.680468
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4("127.0.0.1") == True
    assert is_ip_v4("127.0.0.0") == True
    assert is_ip_v4("127.0.0.255") == True
    assert is_ip_v4("255.255.255.255") == True
    assert is_ip_v4("255.255.255.254") == True
    assert is_ip_v4("0.0.0.0") == True
    assert is_ip_v4("1") == False
    assert is_ip_v4("127.0.0.") == False
    assert is_ip_v4("127.0.0.256") == False
    assert is_ip_v4("255.255.255.256") == False
    assert is_ip_v

# Generated at 2022-06-14 05:39:36.852201
# Unit test for function is_email
def test_is_email():
    print('Testing function is_email')
    assert is_email('my.email@the-provider.com')
    assert not is_email('@gmail.com')
    assert not is_email('@')
    assert is_email('"very.(),:;<>[]\".VERY.\"very@\\ \"very\".unusual"@strange.example.com')
    assert not is_email('"very.(),:;<>[]\"very@\\"very.very.unusual"@strange.example.com')
    assert not is_email('"very.(),:;<>[]\"very@\\"very.unusual"very.example.com')
    assert not is_email('"very.(),:;<>[]\\"very@very.unusual"@strange.example.com')

# Generated at 2022-06-14 05:39:49.903168
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker('978-5-93286-128-0').is_isbn_13() is True
    assert __ISBNChecker('978-0-306-40615-7').is_isbn_13() is True
    assert __ISBNChecker('978-0-9542246-0-4').is_isbn_13() is True
    assert __ISBNChecker('978-5-9910-0936-1').is_isbn_13() is True
    assert __ISBNChecker('978-5-4461-0492-7').is_isbn_13() is True
    assert __ISBNChecker('978-966-2460-02-4').is_isbn_13() is True

# Generated at 2022-06-14 05:40:02.577897
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75')
    assert not is_ip_v4('nope')
    assert not is_ip_v4('255.200.100.999')
    assert not is_ip_v4('255.200.100')
    assert not is_ip_v4('255.200.100.75.1')
    assert not is_ip_v4('255.200.100.255.1')
    assert not is_ip_v4('255 .200.100.255')
    assert is_ip_v4('255.0.0.0')
    assert is_ip_v4('0.0.0.0')
    assert is_ip_v4('0.255.0.0')

# Generated at 2022-06-14 05:40:15.188034
# Unit test for function is_email
def test_is_email():
    assert is_email('username@gmail.com') == True
    assert is_email('username.@gmail.com') == False
    assert is_email('username.gmail.com') == False
    assert is_email('jojo@jojo..jojo') == False
    assert is_email('jojo@jojo.jojo..') == False
    assert is_email('jojo..jojo@joj.com') == False
    assert is_email('jojo.@jojo.jojo') == False
    assert is_email('jojo@jojo.jojo.') == False
    assert is_email('jojo@jojo..jojo') == False
    assert is_email('jojo@.jojo.jojo') == False
    assert is_email('jojo@jojo.jojo') == True

# Generated at 2022-06-14 05:40:27.070867
# Unit test for function is_ip
def test_is_ip():
    assert is_ip('255.200.100.75') == True
    assert is_ip('2001:db8:85a3:0000:0000:8a2e:370:7334') == True
    assert is_ip('1.2.3') == False
test_is_ip()


# Generated at 2022-06-14 05:40:36.345392
# Unit test for function is_ip_v4
def test_is_ip_v4():
    # This function is already tested by pytest in tests/test_validators.py
    with pytest.raises(AssertionError):
        is_ip_v4(None)

    assert is_ip_v4('') is False
    assert is_ip_v4('192.168.1.1') is True
    assert is_ip_v4('192.168.1') is False
    assert is_ip_v4('192.168.1.') is False
    assert is_ip_v4('256.168.1.1') is False
    assert is_ip_v4('192.168.1.1.') is False



# Generated at 2022-06-14 05:40:49.349887
# Unit test for function is_credit_card
def test_is_credit_card():
    assert is_credit_card('4111111111111111') # VISA
    assert is_credit_card('378282246310005') # AMEX
    assert is_credit_card('378734493671000') # AMEX
    assert is_credit_card('30569309025904') # DINERS_CLUB
    assert is_credit_card('6011111111111117') # DISCOVER
    assert is_credit_card('5105105105105100') # MASTERCARD
    assert is_credit_card('3530111333300000') # JCB
    assert is_credit_card('3566002020360505') # JCB
    assert not is_credit_card('4111111111111112')
    assert not is_credit_card('371449635398431')
    assert not is_credit_card

# Generated at 2022-06-14 05:40:55.153142
# Unit test for function is_url
def test_is_url():
    assert(is_url("http://www.google.com"))
    assert(not(is_url("www.google.com")))
    assert(not(is_url("https://www.google.com")))
#test_is_url()


# Generated at 2022-06-14 05:41:03.992998
# Unit test for function is_credit_card
def test_is_credit_card():
    assert is_credit_card('4242424242424242', 'VISA') == True
    assert is_credit_card('4242424242424242', 'MASTERCARD') == False
    assert is_credit_card('4242424242424242', 'AMERICAN_EXPRESS') == False
    assert is_credit_card('4242424242424242', 'DINERS_CLUB') == False
    assert is_credit_card('4242424242424242', 'DISCOVER') == False
    assert is_credit_card('4242424242424242', 'JCB') == False
    assert is_credit_card('555444666', 'VISA') == False
    try:
        is_credit_card('4242424242424242', 'TEST')
    except:
        assert True

# Generated at 2022-06-14 05:41:07.578613
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@theprovider.com') == True
    assert is_email('@gmail.com') == False

test_is_email()


# Generated at 2022-06-14 05:41:20.177775
# Unit test for function is_credit_card
def test_is_credit_card():
    assert is_credit_card('4242424242424242')
    assert is_credit_card('5555555555554444')
    assert is_credit_card('378282246310005')
    assert is_credit_card('341111111111111')
    assert is_credit_card('6011000000000004')
    assert is_credit_card('3530111333300000')
    assert is_credit_card('3566002020140006')
    assert is_credit_card('30000000000004')
    assert is_credit_card('4111111111111111')
    assert is_credit_card('6011050000000004')
    assert is_credit_card('6011000400000000')
    assert is_credit_card('6011111111111117')

# Generated at 2022-06-14 05:41:28.474745
# Unit test for function is_ip
def test_is_ip():
    assert not is_ip('')
    assert not is_ip('a.b.c')
    assert not is_ip('2001:db8:85a3:0000:0000:8a2e:370:7334:')
    assert is_ip('2001:db8:85a3:0000:0000:8a2e:370:7334')
    assert is_ip('255.200.100.75')



# Generated at 2022-06-14 05:41:33.170847
# Unit test for function is_isbn
def test_is_isbn():
    assert is_isbn('1506715214')
    assert is_isbn('9780312498580')
    assert is_isbn('978-0312498580', False) == False


# Generated at 2022-06-14 05:41:36.480674
# Unit test for function is_ip
def test_is_ip():
    assert is_ip('255.200.100.75') == True
    assert is_ip('2001:db8:85a3:0000:0000:8a2e:370:7334') == True
    assert is_ip('1.2.3') == False

test_is_ip()

# Generated at 2022-06-14 05:41:54.130603
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com')
    assert is_email('my.email+sub.account@the-provider.com')
    assert is_email('my.email+sub.account@sub.the-provider.com')
    assert is_email('email@123.123.123.123')
    assert is_email('email@[123.123.123.123]')
    assert is_email('"email"@the-provider.com')
    assert is_email('"email@sub"@the-provider.com')
    assert is_email('"email@sub.account"@the-provider.com')
    assert is_email('"sub account"@the-provider.com')
    assert is_email('"sub@account"@the-provider.com')


# Generated at 2022-06-14 05:41:57.240316
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
        assert __ISBNChecker('9781118539072').is_isbn_13() is True
        assert __ISBNChecker('9781118539073').is_isbn_13() is False



# Generated at 2022-06-14 05:42:02.090534
# Unit test for function is_json
def test_is_json():
    assert is_json('{"key":"value","nested":{"key":"value"}}')
    assert is_json('{"key":"value","nested":{"key":{"key":"value"}}}')
    assert is_json('{"key":"value","nested":{"key":{"key":{"key":"value"}}}}')
    assert is_json('{"key":"value","nested":{"key":{"key":{"key":{"key":"value"}}}}}')
    return "unit test for is_json succeeded"



# Generated at 2022-06-14 05:42:07.841935
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker('978-88-8383-098-1').is_isbn_13() == True
    assert __ISBNChecker('978-88-8383-098-3').is_isbn_13() == False
    assert __ISBNChecker('978-88-8383-098').is_isbn_13() == False


# Generated at 2022-06-14 05:42:20.364155
# Unit test for function is_json

# Generated at 2022-06-14 05:42:32.515052
# Unit test for function is_url
def test_is_url():
    # ------------
    # is_url
    # ------------

    assert is_url('http://www.mysite.com') is True
    assert is_url('http://www.mysite-complex-123.com') is True
    assert is_url('https://mysite.com') is True
    assert is_url('https://mysite.com') is True
    assert is_url('http://www.mysite.com/subfolder') is True
    assert is_url('http://www.my-site.com/subfolder') is True
    assert is_url('http://www.mysite.com/subfolder/') is True
    assert is_url('http://www.mysite.com/sub-folder/') is True

# Generated at 2022-06-14 05:42:42.138464
# Unit test for function is_url
def test_is_url():
    assert is_url('http://www.mysite.com') is True
    assert is_url('https://mysite.com') is True
    assert is_url('ftp://mysite.com') is True
    assert is_url('file://mysite.com') is True
    assert is_url('mysite.com') is False
    assert is_url('.mysite.com') is False
    assert is_url('www.mysite.com') is False
    assert is_url('http://mysite.com') is True
    assert is_url('http://mysite.com', allowed_schemes=['http', 'ftp']) is True
    assert is_url('https://mysite.com', allowed_schemes=['http', 'ftp']) is False

# Generated at 2022-06-14 05:42:44.752307
# Unit test for function is_url
def test_is_url():
    assert is_url('http://www.mysite.com') == True
    assert is_url('www.mysite.com') == False
#


# Generated at 2022-06-14 05:42:58.355048
# Unit test for function is_email
def test_is_email():
    """
    Test function is_email.
    """
    from . import utils

    assert(utils.is_email('foo.bar@baz.com') == True)
    assert(utils.is_email('foo.bar@baz.co.uk') == True)
    assert(utils.is_email('foo.bar.@baz.co.uk') == False)
    assert(utils.is_email('foobar@baz.co.uk') == True)

    assert(utils.is_email('foo.ba.r@baz.com') == True)
    assert(utils.is_email('foo_bar@baz.co.uk') == True)
    assert(utils.is_email('foo_bar_@baz.co.uk') == False)

# Generated at 2022-06-14 05:43:11.519403
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    isbn_checker = __ISBNChecker("0140444601")
    assert isbn_checker.is_isbn_10()

    isbn_checker = __ISBNChecker("1234567890")
    assert isbn_checker.is_isbn_10()

    isbn_checker = __ISBNChecker("978-0-306-40615-7")
    assert isbn_checker.is_isbn_10()

    isbn_checker = __ISBNChecker("0-306-40615-2")
    assert isbn_checker.is_isbn_10()

    isbn_checker = __ISBNChecker("9789571121759")
    assert isbn_checker.is_isbn_10() == False
    

# Generated at 2022-06-14 05:43:23.084642
# Unit test for function is_email
def test_is_email():
    assert not is_email('some text')
    assert is_email('email@domain.com')
    assert is_email('firstname.lastname@domain.com')
    assert is_email('email@subdomain.domain.com')
    assert is_email('firstname+lastname@domain.com')
    assert is_email('1234567890@domain.com')
    assert is_email('email@domain-one.com')
    assert not is_email('email@domain.web')
    assert not is_email('email@domain..com')
    assert is_email('email@-domain.com')
    assert is_email('email@domain.name')
    assert is_email('email@domain.co.jp')
    assert is_email('firstname-lastname@domain.com')

# Generated at 2022-06-14 05:43:32.502993
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    print('test___ISBNChecker_is_isbn_10()')

    isbn = __ISBNChecker('0-306-40615-2')
    print('isbn.is_isbn_10()', isbn.is_isbn_10())

    isbn = __ISBNChecker('0306406152')
    print('isbn.is_isbn_10()', isbn.is_isbn_10())

    isbn = __ISBNChecker('18-4842-2978')
    print('isbn.is_isbn_10()', isbn.is_isbn_10())

    isbn = __ISBNChecker('1848422978')
    print('isbn.is_isbn_10()', isbn.is_isbn_10())


# Generated at 2022-06-14 05:43:45.461008
# Unit test for function is_email
def test_is_email():
    assert is_email("person@domain.com")
    assert is_email("person@domain.net")
    assert is_email("person@domain.co.uk")
    assert is_email("person@domain.info")
    assert is_email("person@domain.ca")
    assert is_email("person@domain.be")
    assert is_email("person@domain.fr")
    assert is_email("person@domain.us")
    assert not is_email("person@domain")
    assert not is_email("person@domain.c")
    assert not is_email("person@domain.con")
    assert not is_email("person@domain.co.u")
    assert not is_email("person.domain.com")



# Generated at 2022-06-14 05:43:50.942069
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker('0306406152').is_isbn_10() == True
    assert __ISBNChecker('1-56619-909-3').is_isbn_10() == False
    assert __ISBNChecker('978-5-16-006307-9').is_isbn_10() == False


# Generated at 2022-06-14 05:43:59.823272
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') == True
    assert is_json('[1, 2, 3]') == True
    assert is_json('{"name": "Peter"}') == True
    assert is_json('"name"') == False
    assert is_json('') == False
    assert is_json('{nope}') == False
    assert is_json('"{nope}"') == False
    assert is_json('Jackson') == False


# Generated at 2022-06-14 05:44:09.428843
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker('0-321-14653-0').is_isbn_10()
    assert __ISBNChecker('0-306-40615-2').is_isbn_10()
    assert __ISBNChecker('0-306-40615-2').is_isbn_10()
    assert __ISBNChecker('0306406152').is_isbn_10()
    assert __ISBNChecker('0306406152').is_isbn_10()
    assert __ISBNChecker('0306406152').is_isbn_10()
    assert __ISBNChecker('0306406152').is_isbn_10()
    assert not __ISBNChecker('0-306-40615-8').is_isbn_10()

# Generated at 2022-06-14 05:44:14.457279
# Unit test for function is_email
def test_is_email():
    assert is_email('email@emai.com') == True
    assert is_email('www.test@test.com') == True
    assert is_email('.test@test.com') == False
    assert is_email('@test.com') == False
    assert is_email('test@.com') == False
    assert is_email('test@test.') == False
    assert is_email('test@test..com') == False



# Generated at 2022-06-14 05:44:18.431629
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    isbn = __ISBNChecker('0732352964')
    assert isbn.is_isbn_10() == True, "Errore isbn 10"

    isbn = __ISBNChecker('0732352965')
    assert isbn.is_isbn_10() == False, "Errore isbn 10"


# PUBLIC API



# Generated at 2022-06-14 05:44:31.408357
# Unit test for function is_email
def test_is_email():
    assert is_email('normal@example.com') == True
    assert is_email('$mail@example.com') == True
    assert is_email('!mail@example.com') == True
    assert is_email('*mail@example.com') == True
    assert is_email('+mail@example.com') == True
    assert is_email('/mail@example.com') == True
    assert is_email('=mail@example.com') == True
    assert is_email('.mail@example.com') == True
    assert is_email('?mail@example.com') == True
    assert is_email('^mail@example.com') == True
    assert is_email('_mail@example.com') == True
    assert is_email('`mail@example.com') == True

# Generated at 2022-06-14 05:44:36.819941
# Unit test for function is_json
def test_is_json():
    assert is_json("{'a': 'b'}") == True
    assert is_json("{'a': 'b'}") == True
    assert is_json("{'a': 'b'}") == True
    assert is_json("{'a': 'b'}") == True
    assert is_json("{'a': 'b'}") == True



# Generated at 2022-06-14 05:44:44.875119
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') == True
    assert is_json('[1, 2, 3]') == True
    assert is_json('{nope}') == False



# Generated at 2022-06-14 05:44:56.352677
# Unit test for function is_email
def test_is_email():
    assert is_email("codewithrohan@gmail.com") == True
    assert is_email("codewithrohan@gmail") == False
    assert is_email("rohan@gmail.com") == True
    assert is_email("@") == False
    assert is_email("codewithrohan@.") == False
    assert is_email("codewithrohan@.com") == False
    assert is_email("codewithrohan@.com") == False
    assert is_email("a@ab.com") == True
    assert is_email("a b@ab.com") == True
    assert is_email("a b@ab.com") == True
    assert is_email("a b@ab.com") == True
    assert is_email("code@gmail.com") == True

# Generated at 2022-06-14 05:45:04.020121
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker('9788375385908').is_isbn_13()
    assert __ISBNChecker('978-0-306-40615-7').is_isbn_13()
    assert __ISBNChecker('9780306406157').is_isbn_13()
    assert __ISBNChecker('97803064061571').is_isbn_13() is False



# Generated at 2022-06-14 05:45:09.387481
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com')
    assert is_email('my.email+1@the-provider.com')
    assert not is_email(' @gmail.com')
    assert not is_email('my.email@gmail.com')


# Generated at 2022-06-14 05:45:11.655144
# Unit test for function is_json
def test_is_json():
    assert is_json('{}') == True, "Error in is_json()"
test_is_json()


# Generated at 2022-06-14 05:45:14.467520
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') == True
    assert is_json('[1,2,3]') == True
    assert is_json('{nope}') == False



# Generated at 2022-06-14 05:45:26.276709
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}')
    assert is_json('[1, 2, 3]')
    assert is_json('{nope}')  == False
    assert is_json(None)  == False
    assert is_json('')  == False
    assert is_json('123')  == False
    assert is_json(123)  == False
    assert is_json(True)  == False
    assert is_json(1.9)  == False
    assert is_json('{"name":')  == False
    assert is_json('name": "Peter"}')  == False
    assert is_json('{"name": "Peter"')  == False



# Generated at 2022-06-14 05:45:35.882013
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@my_provider.com')
    assert is_email('my.email@my-provider.com')
    assert is_email('my.email@myadeer.com')
    assert is_email('my.email@mya_deer.com')
    assert is_email('my.email@mya-deer.com')
    assert is_email('my_email@myprovider.com')
    assert is_email('my-email@myprovider.com')
    assert is_email('my_email@my_provider.com')
    assert is_email('my-email@my-provider.com')
    assert is_email('my_email@my_provider.com.uk')

# Generated at 2022-06-14 05:45:39.629669
# Unit test for function is_email
def test_is_email():
   assert is_email("my.email@the-provider.com") == True
   assert is_email("my.email@the-provider.com") == False
test_is_email()



# Generated at 2022-06-14 05:45:50.953642
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker('978-1-5663-9273-3').is_isbn_13() == True
    assert __ISBNChecker('978-1-5663-92734').is_isbn_13() == False
    assert __ISBNChecker('978-156639-273-3').is_isbn_13() == False
    assert __ISBNChecker('978-156639273-3').is_isbn_13() == False
    assert __ISBNChecker('9781566392733').is_isbn_13() == True
    assert __ISBNChecker('9781566392734').is_isbn_13() == False
    assert __ISBNChecker('978-1-56639-273-3').is_isbn_13() == True
    assert __ISBN

# Generated at 2022-06-14 05:46:04.485049
# Unit test for function is_email
def test_is_email():
    # test full email
    assert is_email('john.smith@mysite.com')
    assert is_email('john.smith+123@mysite.com')

    # test email with funny chars
    assert is_email('foo"bar"baz@example.com')
    assert is_email('foo\\ bar@example.com')
    assert is_email('foo[at]bar@example.com')

    # test international email
    assert is_email('θσè∂@θσè.com')
    assert is_email('иван@пример.рф')

    # test invalid email
    assert not is_email('john.smith@')
    assert not is_email('@mysite.com')
    assert not is_email('@#@')



# Generated at 2022-06-14 05:46:15.673951
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    checks = [
        ('1234567890', True),
        ('8193386532', True),
        ('1234567899', False),
        ('8039367912', False),
        ('8193386533', False),
        ('819338653', False),
        ('81933865321', False),
        ('8193386530A', False),
        ('8193386530', True),
        ('8039367913', False)
    ]

    for i, check in enumerate(checks):
        assert check[1] == __ISBNChecker(check[0]).is_isbn_10(), f'Failed test number: {i}'

# Generated at 2022-06-14 05:46:20.994741
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    try:
        __ISBNChecker('', False)
    except InvalidInputError:
        pass
    else:
        raise ValueError('The exception was not thrown')
    try:
        __ISBNChecker('0-306-40615-', False)
    except InvalidInputError:
        pass
    else:
        raise ValueError('The exception was not thrown')
    assert not __ISBNChecker('0-306-40615-X', False).is_isbn_13()
    assert __ISBNChecker('978-0-306-40615-7', False).is_isbn_13()



# Generated at 2022-06-14 05:46:24.687271
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') is True
    assert is_json('[1, 2, 3]') is True
    assert is_json('{nope}') is False
    assert is_json('null') is True
    assert is_json(None) is False



# Generated at 2022-06-14 05:46:28.422030
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker('1400079179').is_isbn_10()
    assert not __ISBNChecker('1-400079-17-9').is_isbn_10()


# Generated at 2022-06-14 05:46:33.811015
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75')
    assert not is_ip_v4('nope')
    assert not is_ip_v4('255.200.100.999')

test_is_ip_v4()    


# Generated at 2022-06-14 05:46:37.721501
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') == True
    assert is_json('[1, 2, 3]') == True
    assert is_json('[1, 2, 3]}') == False


# Generated at 2022-06-14 05:46:42.514054
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75')  # returns true
    assert is_ip_v4('nope') is False  # returns false (not an ip)
    assert is_ip_v4('255.200.100.999') is False  # returns false (999 is out of range)

# Generated at 2022-06-14 05:46:49.051156
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75') == True
    assert is_ip_v4('nope') == False
    assert is_ip_v4('255.200.100.999') == False
    
test_is_ip_v4()

# Generated at 2022-06-14 05:46:56.176374
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker('0-306-40615-2').is_isbn_10()
    assert __ISBNChecker('0-306-40615-X').is_isbn_10()
    assert __ISBNChecker('0-306-40615-5').is_isbn_10() == False
    assert __ISBNChecker('0-306-40615-11').is_isbn_10() == False

# Generated at 2022-06-14 05:47:06.683568
# Unit test for function is_email

# Generated at 2022-06-14 05:47:09.256839
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com') == True
    assert is_email('@gmail.com') == False


# Generated at 2022-06-14 05:47:13.085294
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') == True, 'is_json failed'
    assert is_json('[1, 2, 3]') == True, 'is_json failed'
    assert is_json('{nope}') == False, 'is_json failed'
    
    


# Generated at 2022-06-14 05:47:26.750402
# Unit test for function is_email

# Generated at 2022-06-14 05:47:28.672829
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker('0747532699').is_isbn_10() is True

# Generated at 2022-06-14 05:47:42.685671
# Unit test for function is_email
def test_is_email():
    assert not is_email(None)
    assert not is_email('')
    assert not is_email(' ')
    assert not is_email('@gmail.com')
    assert not is_email('my.email.@the-provider.com')
    assert not is_email('my..email@the-provider.com')
    assert not is_email('my.email@the-.provider.com')
    assert not is_email('my.email@the-.provider..com')
    assert not is_email('my.email@the-provider.com.')
    assert not is_email('my.email@the-provider..com.')
    assert not is_email('my.email@the-provider.com.uk.')

# Generated at 2022-06-14 05:47:46.064981
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    obj = __ISBNChecker('0-306-40615-2')
    assert obj.is_isbn_10()

# Generated at 2022-06-14 05:47:48.436343
# Unit test for function is_json
def test_is_json():
    if is_json('{"name": "Peter"}')==True:
        assert True
    else:
        assert False
        


# Generated at 2022-06-14 05:47:53.050119
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4("255.200.100.75") == True
    assert is_ip_v4("nope") == False
    assert is_ip_v4("255.200.100.999")== False



# Generated at 2022-06-14 05:47:58.138832
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75')
    assert not is_ip_v4('nope')
    assert not is_ip_v4('255.200.100.999')
test_is_ip_v4()



# Generated at 2022-06-14 05:48:11.179312
# Unit test for function is_json
def test_is_json():
    assert is_json(42) == False
    assert is_json('{"name": "Peter"}') == True
    assert is_json('[1, 2, 3]') == True
    assert is_json('{nope}') == False
    assert is_json('{"name": "Peter"') == False # missing parenthesis
    assert is_json('}{"name": "Peter"}') == False # extra parenthesis
    assert is_json('{"name": "Peter"}{"name": "Peter"}') == False # extra parenthesis


# Generated at 2022-06-14 05:48:15.760030
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75')
    assert is_ip_v4('nope') == False
    assert is_ip_v4('255.200.100.999') == False

# Generated at 2022-06-14 05:48:22.029502
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    isbn_inputs = [
        ('9780470059029', True),
        ('0-321-14653-0', True),
        ('877 1 95 869x', False),
        ('877195x869', False),
        ('877195869x', False),
    ]
    for isbn_input, isbn_expected in isbn_inputs:
        isbn_checker = __ISBNChecker(isbn_input)
        assert isbn_checker.is_isbn_10() == isbn_expected