

# Generated at 2022-06-14 05:38:55.645559
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') == True
    assert is_json('[1, 2, 3]') == True
    assert is_json('{nope}') == False


# Generated at 2022-06-14 05:39:05.371634
# Unit test for function is_ip_v4
def test_is_ip_v4():
    with pytest.raises(AssertionError):
        is_ip_v4(None)
    with pytest.raises(InvalidInputError):
        is_ip_v4('nope')
    assert is_ip_v4('8.8.8.8')
    assert is_ip_v4('0.0.0.0')
    assert is_ip_v4('255.255.255.255')
    assert is_ip_v4('0.0.0.255')
    assert not is_ip_v4('0.0.0.')
    assert not is_ip_v4('0.0.0.256')
    assert not is_ip_v4('0.0.0.1000')
    assert not is_ip_v4('0.0.0.9999')


# Generated at 2022-06-14 05:39:13.701565
# Unit test for function is_credit_card
def test_is_credit_card():
    assert is_credit_card('5105105105105100') == True
    assert is_credit_card('5105105105105106') == False
    assert is_credit_card('5105105105105106',card_type='MASTERCARD') == False
    assert is_credit_card('378282246310005') == True
    assert is_credit_card('6269990123456785') == True
    assert is_credit_card('6011000990139424') == True
    assert is_credit_card('30569309025904') == True
    assert is_credit_card('3530111333300000') == True
    assert is_credit_card('5555555555554444') == True
    assert is_credit_card('5555-5555-5555-4444') == True



# Generated at 2022-06-14 05:39:18.519345
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') # returns true
    assert is_json('[1, 2, 3]') # returns true
    assert not is_json('{nope}') # returns false
test_is_json()



# Generated at 2022-06-14 05:39:32.895114
# Unit test for function is_email
def test_is_email():
    assert is_email("Aleksandar@gmail.com")
    assert is_email(".Aleksandar@gmail.com") == False
    assert is_email("@bit.edu") == False
    assert is_email("A.A@bit.edu")
    assert is_email("Aleksandar.A@bit.edu")
    assert is_email("Aleksandar.A@bit.edu.rs")
    assert is_email("Aleksandar.A@bit.edu.rs.") == False
    assert is_email("\"Aleksandar.A@bit.edu.rs\"@gmail.com")
    assert is_email("\"Aleksandar. A@bit.edu.rs\"@gmail.com") == False

# Generated at 2022-06-14 05:39:41.776112
# Unit test for function is_json
def test_is_json():
    # Test JSON that should not raise error
    assert is_json('{"name": "Peter"}') is True, 'valid json'
    assert is_json('[1, 2, 3]') is True, 'valid json'
    assert is_json('["1", 2]') is True, 'valid json'

    # Test invalid JSON
    assert is_json('{"name": "Peter"') is False, 'invalid json'
    assert is_json('[1, 2, 3') is False, 'invalid json'
    assert is_json('["1", 2') is False, 'invalid json'
    assert is_json('"name"') is False, 'invalid json'
    assert is_json('{"name": "Peter"}}') is False, 'invalid json'
    assert is_json('[1, 2, 3]]')

# Generated at 2022-06-14 05:39:52.666898
# Unit test for function is_url
def test_is_url():
    assert is_url('https://www.youtube.com/') == True
    assert is_url('https://www.youtube.com') == False
    assert is_url('www.youtube.com') == False
    assert is_url('http://www.youtube.com/') == True
    assert is_url('http://www.youtube.com') == False
    assert is_url('http://ww.youtube.com/') == False
    assert is_url('https://www.youtube') == False
    assert is_url('https://www.youtube.com/watch?v=Zo7VuH6BbvM') == True
    assert is_url('https://www.youtube.com/watch?v=Zo7VuH6BbvM/b') == False



# Generated at 2022-06-14 05:39:57.186507
# Unit test for function is_ip
def test_is_ip():
    assert is_ip('255.200.100.75')
    assert not is_ip('1.2.3')


# Only a-z and A-Z are accepted

# Generated at 2022-06-14 05:40:05.026145
# Unit test for function is_email
def test_is_email():
    assert is_email("my.email@the-provider.com")
    assert not is_email("@gmail.com")
    assert is_email("my.email\\ @the-provider.com")
    assert is_email("my.\"email\"@the-provider.com")
    assert is_email("\"quoted\"@gmail.com")
    assert not is_email("\"quoted@gmail.com")
    assert is_email("my.email\\\\@the-provider.com")


# Generated at 2022-06-14 05:40:12.683915
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert(is_ip_v4('250.200.100.75'))
    assert(is_ip_v4('255.200.100.75'))
    result = is_ip_v4('nope') 
    assert(not result)
    result = is_ip_v4('255.200.100.999') 
    assert(not result)
    
test_is_ip_v4()



# Generated at 2022-06-14 05:40:20.817405
# Unit test for function is_ip
def test_is_ip():
    input_string = '255.200.100.75'
    assert is_ip(input_string)
    input_string = '2001:db8:85a3:0000:0000:8a2e:370:7334'
    assert is_ip(input_string)
    input_string = '1.2.3'
    assert not is_ip(input_string)
    
test_is_ip()

# Generated at 2022-06-14 05:40:23.561056
# Unit test for function is_ip
def test_is_ip():
    assert(is_ip('255.200.100.75')==True)
    assert(is_ip('2001:db8:85a3:0000:0000:8a2e:370:7334')==True)
    assert(is_ip('1.2.3') == False)
# Test it
test_is_ip()
print_passed()


# Generated at 2022-06-14 05:40:35.077435
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker('030640615X').is_isbn_10() == True
    assert __ISBNChecker('030640615X').is_isbn_13() == False
    assert __ISBNChecker('978 0 306 40615 9').is_isbn_13() == True
    assert __ISBNChecker('978 0 306 40615 9').is_isbn_10() == False
    assert __ISBNChecker('0-306-40615-X').is_isbn_10() == True
    assert __ISBNChecker('0-306-40615-X').is_isbn_13() == False
    assert __ISBNChecker('ISBN 978-0-306-40615-9').is_isbn_13() == True

# Generated at 2022-06-14 05:40:36.858927
# Unit test for function is_ip
def test_is_ip():
    assert is_ip('255.200.100.75')
    assert is_ip('2001:db8:85a3:0000:0000:8a2e:370:7334')
    assert not is_ip('1.2.3')

# Generated at 2022-06-14 05:40:43.821476
# Unit test for function is_ip
def test_is_ip():
    assert is_ip('255.200.100.75')
    assert is_ip('2001:db8:85a3:0000:0000:8a2e:370:7334')
    assert not is_ip('1.2.3.4.5')


# Generated at 2022-06-14 05:40:53.743747
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com') == True
    assert is_email('@gmail.com') == False
    assert is_email('josef.k@gm.com') == True
    assert is_email('josef.k+123@gm.com') == True
    assert is_email('josef.k+123@gmail.com') == True
    assert is_email('josef.k@gmail.com') == True
    assert is_email('josef.k.@gmail.com') == False
    assert is_email('josef.k+123@gmail.c') == False
    assert is_email('josef.k+123@gmail.com.c') == False
    assert is_email('josef.k+123@.com') == False
   

# Generated at 2022-06-14 05:40:56.420302
# Unit test for function is_ip
def test_is_ip():
    assert is_ip('255.200.100.75')
    assert is_ip('2001:db8:85a3:0000:0000:8a2e:370:7334')
    assert not is_ip('1.2.3')

# Generated at 2022-06-14 05:41:02.323178
# Unit test for function is_ip
def test_is_ip():
    assert is_ip('255.200.100.75') == True
    assert is_ip('2001:db8:85a3:0000:0000:8a2e:370:7334') == True
    assert is_ip('1.2.3') == False
    print('test_is_ip() passed')


# Generated at 2022-06-14 05:41:14.707538
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com') == True
    assert is_email('@gmail.com') == False
    assert is_email('test@test.test') == True
    assert is_email('test@test.t') == False
    assert is_email('test@test.') == False
    assert is_email('test@test') == False
    assert is_email('testtest.test') == False
    assert is_email('test@.test') == False
    assert is_email('test.@test.test') == False
    assert is_email('test@test..test') == False




# Generated at 2022-06-14 05:41:20.473931
# Unit test for function is_json
def test_is_json():
    """
    Test the function is_json
    """
    assert is_json('{"name": "Peter"}')
    assert is_json('[1, 2, 3]')
    assert not is_json('{nope}')
    assert not is_json(None)
    assert not is_json('')



# Generated at 2022-06-14 05:41:32.999179
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker('978-0-306-40615-7').is_isbn_13() is True
    assert __ISBNChecker('978-0-306-40615-5').is_isbn_13() is False
    assert __ISBNChecker('0-306-40615-6').is_isbn_13() is None
    assert __ISBNChecker('978-1-61304-2').is_isbn_13() is None



# Generated at 2022-06-14 05:41:43.979693
# Unit test for function is_isbn
def test_is_isbn():
    assert is_isbn('9780312498580')
    assert is_isbn('9780312498580', normalize=False)
    assert is_isbn('1506715214')
    assert is_isbn('1506715214', normalize=False)
    assert is_isbn('978-0312498580')
    assert not is_isbn('978-0312498580', normalize=False)
    assert is_isbn('150-6715214')
    assert not is_isbn('150-6715214', normalize=False)
    assert not is_isbn('150-6715214', normalize=False)

    assert is_isbn('150-6715214', normalize=False)
    assert is_isbn('150-6715214', normalize=False)

# Generated at 2022-06-14 05:41:54.600832
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com') == True
    assert is_email('@gmail.com') == False
    assert is_email('my.email@the-provider.com ') == False
    assert is_email('my.email @ the-provider.com') == False
    assert is_email('my.email@.com') == False
    assert is_email('my.email@ the-provider.com') == False
    assert is_email('my.email@the-provider..com') == False
    assert is_email('my.email@the-provider.com ') == False



# Generated at 2022-06-14 05:42:02.922731
# Unit test for function is_email
def test_is_email():
    assert not is_email(1)
    assert not is_email('')
    assert not is_email('.myemail@the-provider.com')
    assert not is_email('myemail@the-provider.com.')
    assert not is_email('myemail@the-provider.com.au')
    assert not is_email('@gmail.com')
    assert not is_email('m@y.email@gmail.com')
    assert not is_email('myemail@')
    assert not is_email('myemail@gmail..com')
    assert not is_email('myemail@gmail.com.')
    assert not is_email('myemail@gmail')
    assert not is_email('myemail@gmail.com..')
    assert not is_email('mail@domain.com.com')

# Generated at 2022-06-14 05:42:08.114546
# Unit test for function is_isbn
def test_is_isbn():
    assert is_isbn(9780312498580) == True
    assert is_isbn(1506715214) == True
    assert is_isbn(9780001806660) == False
    assert is_isbn('9780001806660') == True
    
    
test_is_isbn()    

# Generated at 2022-06-14 05:42:20.214424
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    checker = __ISBNChecker('0')
    assert checker.is_isbn_10() is False
    assert checker.is_isbn_13() is False

    checker = __ISBNChecker('012345678')
    assert checker.is_isbn_10() is False
    assert checker.is_isbn_13() is False

    checker = __ISBNChecker('0123456789')
    assert checker.is_isbn_10() is True
    assert checker.is_isbn_13() is False

    checker = __ISBNChecker('123456789x')
    assert checker.is_isbn_10() is True
    assert checker.is_isbn_13() is False

# Generated at 2022-06-14 05:42:32.385607
# Unit test for function is_email
def test_is_email():
    print("TESTING FUNCTION is_email")
    print("Correct emails")
    print("simple@simple.com" + ": " + str(is_email("simple@simple.com")))
    print("msa.bob@i.suf.er.fro.ma.lland.of.do.om.and.des.pai.r@gmail.com" + ": " + str(is_email("msa.bob@i.suf.er.fro.ma.lland.of.do.om.and.des.pai.r@gmail.com")))

# Generated at 2022-06-14 05:42:41.171777
# Unit test for function is_json
def test_is_json():
    # Check cases when input_string is empty
    assert is_json(None) == False
    assert is_json('') == False
    assert is_json('  ') == False
    assert is_json(1) == False
    
    # Check cases when input_string is not empty
    assert is_json('   {foo}  ') == False
    assert is_json('  [foo] ') == False
    assert is_json(' { "name": "Peter" } ') == True
    assert is_json('    [1, 2, 3]  ') == True
    assert is_json('{ "name": "Peter", "age": 36 }') == True
    
    
##test_is_json()



# Generated at 2022-06-14 05:42:47.963090
# Unit test for function is_email
def test_is_email():
    assert is_email("me@domain.com") == True
    assert is_email("me@domain") == False
    assert is_email("me@domain.org") == True
    assert is_email("me@<domain>.org") == False
    assert is_email("me@<domain>.org") == False
    assert is_email(".me@domain.com") == False



# Generated at 2022-06-14 05:42:52.243845
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') == True
    assert is_json('[1, 2, 3]') == True
    assert is_json('asd') == True
    assert is_json('{nope}') == False



# Generated at 2022-06-14 05:43:05.982392
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker('9814561626').is_isbn_13() == True
    assert __ISBNChecker('9789814561623').is_isbn_13() == True
    assert __ISBNChecker('9814561625').is_isbn_13() == False
    assert __ISBNChecker('97914561622').is_isbn_13() == False
    assert __ISBNChecker('9814561623').is_isbn_13() == False
    assert __ISBNChecker('981456162').is_isbn_13() == False
    assert __ISBNChecker('98145616270').is_isbn_13() == False
    assert __ISBNChecker(9814561625).is_isbn_13() == False
    assert __ISBNCheck

# Generated at 2022-06-14 05:43:13.834287
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    if not __ISBNChecker('0306406152').is_isbn_10():
        raise AssertionError('Expected __ISBNChecker(\'0306406152\').is_isbn_10() to return True')
    if __ISBNChecker('0306406153').is_isbn_10():
        raise AssertionError('Expected __ISBNChecker(\'0306406153\').is_isbn_10() to return False')
    if not __ISBNChecker('0306406154').is_isbn_10():
        raise AssertionError('Expected __ISBNChecker(\'0306406154\').is_isbn_10() to return True')

# Generated at 2022-06-14 05:43:27.419387
# Unit test for function is_email
def test_is_email():
    assert is_email('me@gmail.com') == True
    assert is_email('me@gmail.coma') == False
    assert is_email('me') == False
    assert is_email('me@gmail.com ') == False
    assert is_email('me@gmail.com.') == False
    assert is_email('me@.com') == False
    assert is_email('me@') == False
    assert is_email('') == False
    assert is_email(None) == False
    assert is_email('.me@gmail.com') == False
    assert is_email('().:;<>[]@gmail.com') == False
    assert is_email('me@gmail..com') == False
    assert is_email('me@gmail.com.') == False

# Generated at 2022-06-14 05:43:33.523595
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker('978-3-1614-5409-3').is_isbn_13()

    assert not __ISBNChecker('978-3-1614-5409-4').is_isbn_13()
    assert not __ISBNChecker('978-3-1614-5409').is_isbn_13()
    assert not __ISBNChecker('97831614 54093').is_isbn_13()
    assert not __ISBNChecker('3-1614-5409-3').is_isbn_13()
    assert not __ISBNChecker('978316145409').is_isbn_13()



# Generated at 2022-06-14 05:43:46.686727
# Unit test for function is_email
def test_is_email():
    assert is_email('m.c.@gmail.com') == True
    assert is_email('m@gmail.com') == True
    assert is_email('m.c@gmail.com') == True
    assert is_email('m.c.@gmail.com') == True
    assert is_email('m.c.a@gmail.com') == True
    assert is_email('m.c.a@gmail.co') == True
    assert is_email('m.c.a@gmail.com') == True
    assert is_email('m.c.a@gmail.com') == True
    assert is_email('m.c.a@gmail.mcom') == True
    assert is_email('m.c.a@gmail.mcom') == True

# Generated at 2022-06-14 05:43:57.357877
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

# Generated at 2022-06-14 05:44:08.928480
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker('978-1-56619-909-4').is_isbn_13() is True
    assert __ISBNChecker('1-56619-909-7').is_isbn_13() is True
    assert __ISBNChecker('1-56619-909-0').is_isbn_13() is True
    assert __ISBNChecker('0-306-40615-2').is_isbn_13() is False
    assert __ISBNChecker('1-56619-909-8').is_isbn_13() is False
    assert __ISBNChecker('979-1-56619-909-1').is_isbn_13() is False
    assert __ISBNChecker('979-1-56619-909-8').is_isbn_13

# Generated at 2022-06-14 05:44:14.563762
# Unit test for function is_email
def test_is_email():
    assert is_email('abc@abc.abc') is True
    assert is_email('abc@abc.abc ') is False
    assert is_email('abc@abc') is False
    assert is_email(' abc@abc.abc') is False
    assert is_email('abc@abc.ab c') is False
    assert is_email('a bc@abc.abc') is False



# Generated at 2022-06-14 05:44:18.838432
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker('0747532699').is_isbn_10()
    assert not __ISBNChecker('123456789').is_isbn_10()
    assert __ISBNChecker('007-31-0467').is_isbn_10()
    assert __ISBNChecker('978-1566199094', normalize=False).is_isbn_10() is False


# Generated at 2022-06-14 05:44:20.509439
# Unit test for function is_json
def test_is_json():   
    # This is a test
    s = "{'test': 'is_json'}"
    assert is_json(s)


# Generated at 2022-06-14 05:44:30.250970
# Unit test for function is_json
def test_is_json():
    assert( is_json('{"name": "Peter"}') )
    assert( not is_json('{"name": "Peter"') )
    assert( is_json('[1, 2, 3]') )
    assert( not is_json('{nope}') )



# Generated at 2022-06-14 05:44:40.676072
# Unit test for function is_email
def test_is_email():
    assert not is_email('')
    assert not is_email('jason@') # should be jason@gmail.com
    assert not is_email('lalala.com')

    # email with dot before @
    assert not is_email('.jason@gmail.com') # another dot is ok (see below)
    assert not is_email('jason@gmail.com.')

    # email with multiple .
    assert is_email('jason.jason@gmail.com') # a dot before @ is ok
    assert is_email('jason..jason@gmail.com')
    assert is_email('jason..jason..jason@gmail.com') # multiple dot, either before or after @ are ok
    assert is_email('jason..jason..jason@gmail.com.')

    # email with escaped

# Generated at 2022-06-14 05:44:53.699918
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker('0201485672').is_isbn_10() == True
    assert __ISBNChecker('-0201485672').is_isbn_10() == False
    assert __ISBNChecker('02014856721').is_isbn_10() == False
    assert __ISBNChecker('020148567').is_isbn_10() == False
    assert __ISBNChecker('020148567x').is_isbn_10() == False
    assert __ISBNChecker('O2O1485672').is_isbn_10() == False
    assert __ISBNChecker('0201485670').is_isbn_10() == True


# Generated at 2022-06-14 05:44:57.296067
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('127.0.0.1') == True
    assert is_ip_v4('255.200.100.75') == True
    assert is_ip_v4('nope') == False
    assert is_ip_v4('255.200.100.999') == False

print(test_is_ip_v4())


# Generated at 2022-06-14 05:45:04.019573
# Unit test for function is_json
def test_is_json():
    result = is_json('{"name": "Peter"}')
    expected = True
    assert expected == result

    result = is_json('[1, 2, 3]')
    expected = True
    assert expected == result

    result = is_json('{nope}')
    expected = False
    assert expected == result
# Test run
# test_is_json()


# Generated at 2022-06-14 05:45:08.037002
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert(is_ip_v4('255.200.100.75') == True)
    assert(is_ip_v4('nope') == False)
    assert(is_ip_v4('255.200.100.999') == False)



# Generated at 2022-06-14 05:45:19.951985
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    def case(expected_result, input_string):
        if not is_string(input_string):
            raise InvalidInputError(input_string)

        result = __ISBNChecker(input_string, normalize=True).is_isbn_10()
        assert result == expected_result, \
            'is_isbn_10({0}) expected {1}, but returned {2}'.format(input_string, expected_result, result)

# Generated at 2022-06-14 05:45:24.077553
# Unit test for function is_json
def test_is_json():
    assert len(is_json('{"name": "Peter"}')) == 2
    assert is_json('{nope}') == False
    assert is_json('[1, 2, 3]') == True

test_is_json()



# Generated at 2022-06-14 05:45:34.886469
# Unit test for function is_json
def test_is_json():
    assert not is_json('')
    assert not is_json('foo')
    assert not is_json('{nope}')
    assert is_json('{"name": "Peter"}')
    assert is_json('[1, 2, 3]')
    assert is_json('[]')
    assert is_json('{}')
    assert is_json('{"name": "Peter", "age": 21, "height": 1.85}')
    assert not is_json('{"name": Peter", "age": 21, "height": 1.85}')
    assert not is_json('["name": "Peter", "age": 21, "height": 1.85}')
    assert not is_json('{name": "Peter", "age": 21, "height": 1.85}')



# Generated at 2022-06-14 05:45:46.987687
# Unit test for function is_email
def test_is_email():
    assert is_email('hello@gmail.com') is True
    assert is_email('hello@gmail') is False
    assert is_email('hello\\@gmail\\@abc@gmail.com') is True
    assert is_email('hello@gmail..com') is False
    assert is_email('hello.@gmail.com') is True
    assert is_email('hello\\ world@gmail\\ .com') is True
    assert is_email('hello. world@gmail. com') is False
    assert is_email('hello. world@gmail. com') is False
    assert is_email('hello.....world@gmail.com') is True
    assert is_email('hello..world@gmail.com') is True
    assert is_email('hello world@gmail.com') is True
    assert is_email('hello.world@gmail.com') is True


# Generated at 2022-06-14 05:46:01.927965
# Unit test for function is_email
def test_is_email():
    assert is_email("my.email@the-provider.com")
    assert is_email("my.email@the-provider.com.uk")
    assert is_email("my.email+filter@the-provider.com")
    assert is_email("my.email@the-provider.co.uk")
    assert is_email("me@example.com")
    assert not is_email("@gmail.com")
    assert not is_email("me@example")
    assert not is_email("me.@example.com")
    assert not is_email("me.example.com")
    assert not is_email("me..example@example.com")
    assert not is_email("me\\ @example.com")
    assert is_email("\"me\\\"@example.com")

# Generated at 2022-06-14 05:46:07.629099
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}')
    assert is_json('[1, 2, 3]')
    assert not is_json('{nope}')
    assert not is_json(None)
    assert not is_json('')
    assert not is_json(' ')


# Generated at 2022-06-14 05:46:12.054132
# Unit test for function is_json
def test_is_json():
    assert (is_json('{"name": "Peter"}')) == True
    assert (is_json('[1, 2, 3]')) == True
    assert (is_json('{nope}')) == False



# Generated at 2022-06-14 05:46:18.226330
# Unit test for function is_email
def test_is_email():
    assert is_email('"very.(),:;<>[]\\".VERY.\\"very@\\ \\"very\\".unusual"@strange.example.com')
    assert not is_email('joe@example.com')
    assert not is_email('joe')
    assert is_email(100)


# Generated at 2022-06-14 05:46:27.694204
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('0.0.0.0') == True
    assert is_ip_v4('100.100.100.100') == True
    assert is_ip_v4('255.255.255.255') == True
    assert is_ip_v4('256.0.0.0') == False
    assert is_ip_v4('255.255.255') == False
    assert is_ip_v4('0') == False

# Generated at 2022-06-14 05:46:30.777242
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') == True
    assert is_json('[1, 2, 3]') == True
    assert is_json('{nope}') == False
    assert is_json('abc') == False



# Generated at 2022-06-14 05:46:43.259574
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker('978-386490-61-9').is_isbn_13()
    assert __ISBNChecker('97838649066-6').is_isbn_13()
    assert not __ISBNChecker('978-386490-61-3').is_isbn_13()
    assert not __ISBNChecker('978-386490-61-88').is_isbn_13()
    assert not __ISBNChecker('978-386490-61--9').is_isbn_13()
    assert not __ISBNChecker('978-386490-619').is_isbn_13()
    assert not __ISBNChecker('978-386490-61').is_isbn_13()

# Generated at 2022-06-14 05:46:52.213461
# Unit test for function is_email
def test_is_email():
    email = "my.email@the-provider.com"
    assert is_email(email) is True
    email = "@gmail.com"
    assert is_email(email) is False
    email = "my.email@gmail.com"
    assert is_email(email) is True
    email = 'my.email@gmai\\ l.com'
    assert is_email(email) is True


# Generated at 2022-06-14 05:47:01.732048
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('192.168.0.1') == True
    assert is_ip_v4('192.168.0.1.') == False
    assert is_ip_v4('192.168.0.1.1') == False
    assert is_ip_v4('192.168.0..1') == False
    assert is_ip_v4('192.168.0.01') == False
    assert is_ip_v4('192.168.0.1a') == False
    assert is_ip_v4('192.168.0.0') == True
    assert is_ip_v4('192.168.0.255') == True
    assert is_ip_v4('192.168.00.000') == False
    assert is_ip_v4('') == False
   

# Generated at 2022-06-14 05:47:06.513486
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75') == True
    assert is_ip_v4('nope') == False
    assert is_ip_v4('255.200.100.999') == False

test_is_ip_v4()



# Generated at 2022-06-14 05:47:12.918838
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com')
    
test_is_email()

# Generated at 2022-06-14 05:47:17.745021
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') == True
    assert is_json('[1, 2, 3]') == True
    assert is_json('{nope}') == False


# Generated at 2022-06-14 05:47:29.349610
# Unit test for function is_email
def test_is_email():
    assert is_email('somebody@gmail.com') is True
    assert is_email('some.body+with.dots@gmail.com') is True
    assert is_email('someone.with.subdomain@sub.somedomain.com') is True
    assert is_email('somebody@gmail.com') is True
    assert is_email('somebody+with+dots@gmail.com') is True
    assert is_email('somebody_with-dashes@gmail.com') is True
    assert is_email('somebody.with+dots@gmail.com') is True
    assert is_email('someone.with.subdomain@sub.somedomain.com') is True
    assert is_email('somebody@gmail.com') is True

# Generated at 2022-06-14 05:47:43.020526
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker('9789814180838').is_isbn_13() == True
    assert __ISBNChecker('978981418083').is_isbn_13() == False
    assert __ISBNChecker('97898141808D8').is_isbn_13() == False
    assert __ISBNChecker('9789-81418-083-8').is_isbn_13() == True
    assert __ISBNChecker('97-89-8141808-38').is_isbn_13() == True
    assert __ISBNChecker('97-89-8141808-34').is_isbn_13() == False
    assert __ISBNChecker('97-89-8141808-3X').is_isbn_13() == False
    assert __ISBNChecker

# Generated at 2022-06-14 05:47:52.447703
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}')
    assert is_json('[1, 2, 3]')
    assert not is_json('{nope}')
    assert not is_json('{1: 2, 3}')
    assert not is_json('{1: 2, "name": "Peter"}')
    assert not is_json('{1, 2, 3}')
    assert not is_json('[{"name": "Peter"}]')
    assert not is_json('{"name": "Peter", "surname": "Pan"}')
    assert not is_json('[1, 2, 3, {"name": "Peter"}]')
test_is_json()



# Generated at 2022-06-14 05:47:56.786323
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('100.100.100.100') == True
    assert is_ip_v4('100.100.100.1000') == False
    assert is_ip_v4('100.100.100') == False


# Generated at 2022-06-14 05:48:01.897305
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}')
    assert is_json('[1, 2, 3]')
    assert not is_json('{nope}')
    assert not is_json('{}')

test_is_json()



# Generated at 2022-06-14 05:48:09.047806
# Unit test for function is_ip_v4
def test_is_ip_v4():
    """
    Test function is_ip_v4().
    :return:
    """
    assert(is_ip_v4('255.200.100.75') == True)
    assert(is_ip_v4('nope') == False)
    assert(is_ip_v4('255.200.100.999') == False)
    print("Test is_ip_v4 success!")



# Generated at 2022-06-14 05:48:12.397237
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75')
    assert not is_ip_v4('nope')
    assert not is_ip_v4('255.200.100.999')



# Generated at 2022-06-14 05:48:20.380895
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    checker = __ISBNChecker("0-684-85759-1", False)
    assert checker.is_isbn_10() is True

    checker = __ISBNChecker("0684857591", False)
    assert checker.is_isbn_10() is True

    checker = __ISBNChecker("0-684-85759-0", False)
    assert checker.is_isbn_10() is False

    checker = __ISBNChecker("0684857590", False)
    assert checker.is_isbn_10() is False
