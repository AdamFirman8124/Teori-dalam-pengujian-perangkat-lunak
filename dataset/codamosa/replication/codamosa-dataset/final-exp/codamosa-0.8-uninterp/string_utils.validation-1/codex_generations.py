

# Generated at 2022-06-14 05:38:58.942315
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') == True
    assert is_json('[1, 2, 3]') == True
    assert is_json('{nope}') == False



# Generated at 2022-06-14 05:39:01.616350
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') == True
    assert is_json('[1, 2, 3]') == True
    assert is_json('{nope}') == False



# Generated at 2022-06-14 05:39:13.417325
# Unit test for function is_json
def test_is_json():
    assert is_json('{}')
    assert is_json('{"a":5}')
    assert is_json('{"a":5, "b":6}')
    assert is_json('{"a":"a"}')
    assert is_json('[1, 2, 3]')
    assert is_json('{"a":1, "b":2}')
    assert is_json('{"a":1, "b":2, "c":{"c1":1, "c2":2}, "d":[1, 2, 3], "d2":{"d21":1, "d22":{"d221":1, "d222":2}}}')



# Generated at 2022-06-14 05:39:24.710405
# Unit test for function is_email
def test_is_email():
    assert is_email('test@test.com') == True
    assert is_email('test@test') == False
    assert is_email('test.test') == False
    assert is_email('') == False

    assert is_email('test+test@test.com') == True
    assert is_email('test.test@test.com') == True

    assert is_email('test@test.com.com') == True
    assert is_email('test@test.com.com.au') == True
    assert is_email('test@test.com.com.au.uk') == True

    assert is_email('test@test.test') == False
    assert is_email('test@.test') == False
    assert is_email('test@.test.test') == False

# Generated at 2022-06-14 05:39:33.978042
# Unit test for function is_json
def test_is_json():
    assert(is_json('{"name": "Peter"}') == True)
    assert(is_json('{\'name\': \'Peter\'}') == True)
    assert(is_json('[1, 2, 3]') == True)
    assert(is_json('{nope}') == False)
    assert(is_json('<html>') == False)
    assert(is_json('a') == False)
    assert(is_json('Peter') == False)
    assert(is_json('123') == False)
    assert(is_json('{"id":1,"name":"Peter","address":"1A Smith St"}') == True)
    assert(is_json('"Peter"') == False)
    assert(is_json('[1, 2, 3]') == True)

# Generated at 2022-06-14 05:39:37.118454
# Unit test for function is_isbn
def test_is_isbn():
    assert not is_isbn('hello world')
    assert is_isbn('9780312498580')
    assert is_isbn('1506715214')
    assert not is_isbn('1506715214', normalize=False)


# Generated at 2022-06-14 05:39:41.122756
# Unit test for function is_url
def test_is_url():
    assert is_url('http://www.mysite.com')
    assert is_url('https://mysite.com')
    assert not is_url('.mysite.com')



# Generated at 2022-06-14 05:39:44.867525
# Unit test for function is_url
def test_is_url():
    assert is_url('http://www.mysite.com') == True
    assert is_url('https://www.mysite.com') == True
    assert is_url('.mysite.com') == False

# Generated at 2022-06-14 05:39:49.738144
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com') == True
    assert is_email('@gmail.com') == False
    assert is_email('ahmed.al-sayed@ucalgary.ca') == True
    
test_is_email()

# Test for function is_email

# Generated at 2022-06-14 05:40:02.381373
# Unit test for function is_credit_card
def test_is_credit_card():
    assert is_credit_card('4111111111111111') == True
    assert is_credit_card('411111111111111') == False
    assert is_credit_card('4111111111111111111') == False
    assert is_credit_card('41111111111111115') == True
    assert is_credit_card('5500000000000004') == True
    assert is_credit_card('5500000000000014') == False
    assert is_credit_card('5500000000000004', 'MasterCard') == True
    assert is_credit_card('5500000000000004', 'MASTERCARD') == True
    assert is_credit_card('5500000000000004', 'mastercard') == True
    assert is_credit_card('5500000000000004', 'Visa') == False

# Generated at 2022-06-14 05:40:14.760216
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker('9780262032933').is_isbn_13()
    assert not __ISBNChecker(9780262032933).is_isbn_13()
    assert not __ISBNChecker('97802-6203-293-3').is_isbn_13()
    assert not __ISBNChecker('9780262032932').is_isbn_13()



# Generated at 2022-06-14 05:40:18.554880
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    # setup
    isbn_checker = __ISBNChecker('9780132350884')

    # assert
    assert isbn_checker.is_isbn_13() is True


# Generated at 2022-06-14 05:40:25.104059
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75') # returns true
    #assert is_ip_v4('nope') # returns false (not an ip)
    assert is_ip_v4('255.200.100.999') # returns false (999 is out of range)
if __name__ == "__main__":
    test_is_ip_v4()


# Generated at 2022-06-14 05:40:29.961213
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker('9786138566827').is_isbn_13()
    assert not __ISBNChecker('9786138566821').is_isbn_13()
    assert not __ISBNChecker('9786138566822').is_isbn_13()


# PUBLIC API


# Generated at 2022-06-14 05:40:36.399203
# Unit test for function is_ip
def test_is_ip():
    assert is_ip('255.200.100.75') == True
    assert is_ip('2001:db8:85a3:0000:0000:8a2e:370:7334') == True
    assert is_ip('1.2.3') == False
test_is_ip()

# Generated at 2022-06-14 05:40:39.566240
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com') == True
    assert is_email('my.email@the-provider.com.com') == False


# Generated at 2022-06-14 05:40:47.792158
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('') == False
    assert is_ip_v4(None) == False
    assert is_ip_v4('11.22.33') == False
    assert is_ip_v4('11.22.33.44.55') == False
    assert is_ip_v4('255.200.100.75') == True
    assert is_ip_v4('255.200.100.999') == False



# Generated at 2022-06-14 05:40:51.395811
# Unit test for function is_ip
def test_is_ip():
    assert is_ip('2001:db8:85a3:0000:0000:8a2e:370:7334') == True
    assert is_ip('255.200.100.75') == True
    assert is_ip('1.2.3') == False
test_is_ip()


# Generated at 2022-06-14 05:40:55.542419
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75')
    assert is_ip_v4('192.0.0.1') is True
    assert is_ip_v4('nope') is False
    assert is_ip_v4('255.200.100.999') is False



# Generated at 2022-06-14 05:41:03.354599
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker('043942089X').is_isbn_10()
    assert __ISBNChecker('0780254783').is_isbn_10()
    assert __ISBNChecker('1568494444').is_isbn_10()
    assert __ISBNChecker('0972665404').is_isbn_10()
    assert __ISBNChecker('0756605799').is_isbn_10()
    assert not __ISBNChecker('0439420891').is_isbn_10()
    assert not __ISBNChecker('043942089A').is_isbn_10()


# Public API



# Generated at 2022-06-14 05:41:11.709012
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') == True
    assert is_json('[1, 2, 3]') == True
    assert is_json('{nope}') == False
    assert is_json('') == False
    assert is_json(None) == False


# Generated at 2022-06-14 05:41:22.373460
# Unit test for function is_url
def test_is_url():
    assert is_url('http://www.mysite.com')
    assert is_url('https://mysite.com')
    assert is_url('ftp://mysite.com')
    assert is_url('https://mysite.com')
    assert is_url('https://www.mysite.com')
    assert is_url('https://www.mysite.com:42')
    assert is_url('https://www.mysite.com/path/to/file')
    assert is_url('https://www.mysite.com/path/to/file.ext')
    assert is_url('https://username:password@www.mysite.com/path/to/file.ext')

# Generated at 2022-06-14 05:41:23.995279
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') == True
    
    

# Generated at 2022-06-14 05:41:31.430828
# Unit test for function is_url
def test_is_url():
    assert is_url('http://www.mysite.com')
    assert is_url('https://www.mysite.com')
    assert is_url('ftp://www.mysite.com')
    assert is_url('ws://www.mysite.com')
    assert is_url('wss://www.mysite.com')
    assert is_url('ftps://www.mysite.com')
    assert not is_url('www.mysite.com')



# Generated at 2022-06-14 05:41:43.265377
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker('978-0-306-40615-7').is_isbn_13() == True
    assert __ISBNChecker('978 0 306 40615 7').is_isbn_13() == True
    assert __ISBNChecker('978 0 306 40615 8').is_isbn_13() == True
    assert __ISBNChecker('978-0-306-40615-0').is_isbn_13() == True
    assert __ISBNChecker('978 0 306 40615 0').is_isbn_13() == True
    assert __ISBNChecker('978 0 306 40615 1').is_isbn_13() == True
    assert __ISBNChecker('978 0 306406150').is_isbn_13() == True


# Generated at 2022-06-14 05:41:46.568134
# Unit test for function is_email
def test_is_email():
    assert is_email('"John Doe" <john.doe@example.com>') == True

# Credit card regex from https://github.com/jamesday0/credit-card-validator

# Generated at 2022-06-14 05:41:57.334220
# Unit test for function is_email
def test_is_email():
  assert is_email("test@test.com")
  assert is_email("test@test.google.com")
  assert is_email("test@test.co.uk")
  assert is_email("test+1@test.com")
  assert is_email("test+test@test.test.test.test.test.test")
  assert is_email("test@test..test") == False
  assert is_email("test@test.test.") == False
  assert is_email("test@@test.com") == False
  assert is_email("test@test.com.") == False
  assert is_email(".test@test.com") == False



# Generated at 2022-06-14 05:42:09.458441
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker('0201896834').is_isbn_10(), 'is_isbn_10 failed'
    assert __ISBNChecker('0-201-89683-4').is_isbn_10(), 'is_isbn_10 failed'
    assert not __ISBNChecker('0-201-89683-5').is_isbn_10(), 'is_isbn_10 failed'
    assert not __ISBNChecker('123456789').is_isbn_10(), 'is_isbn_10 failed'
    assert not __ISBNChecker('%20123456789').is_isbn_10(), 'is_isbn_10 failed'
    assert not __ISBNChecker('').is_isbn_10(), 'is_isbn_10 failed'
    assert not __ISBNCheck

# Generated at 2022-06-14 05:42:21.857570
# Unit test for function is_email
def test_is_email():
    assert is_email('maurice.hentschel@fake-email.com') == True
    assert is_email('marco.hentschel@fake-email.com') == True
    assert is_email('mariano.hentschel@fake-email.com') == True
    assert is_email('mario.hentschel@fake-email.com') == True
    assert is_email('matthew.hentschel@fake-email.com') == True
    assert is_email('maurice.hentschel@fake-email.com') == True
    assert is_email('mike.hentschel@fake-email.com') == True
    assert is_email('monica.hentschel@fake-email.com') == True
    assert is_email('natalie.hentschel@fake-email.com')

# Generated at 2022-06-14 05:42:36.253545
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    print('- Test method __ISBNChecker.is_isbn_13')

    try:
        __ISBNChecker('').is_isbn_13()
    except InvalidInputError:
        print('InvalidInputError: empty string')

    try:
        __ISBNChecker('123').is_isbn_13()
    except InvalidInputError:
        print('InvalidInputError: short string')

    try:
        __ISBNChecker('12345678901234').is_isbn_13()
    except InvalidInputError:
        print('InvalidInputError: long string')

    assert __ISBNChecker('9780143008207').is_isbn_13() == True
    assert __ISBNChecker('9791156475313').is_isbn_13() == True

# Generated at 2022-06-14 05:42:52.911196
# Unit test for function is_email
def test_is_email():
    assert is_email('"Abc\\@def"@example.com') is True
    assert is_email('"Fred Bloggs"@example.com') is True
    assert is_email('"Joe\\\\Blow"@example.com') is True
    assert is_email('"Abc@def"@example.com') is True
    assert is_email('customer/department=shipping@example.com') is True
    assert is_email('$A12345@example.com') is True
    assert is_email('!def!xyz%abc@example.com') is True
    assert is_email('_somename@example.com') is True
    assert is_email('dclo@us.ibm.com') is True



# Generated at 2022-06-14 05:43:01.326626
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker('9780141015045').is_isbn_13()
    assert __ISBNChecker('9780141015045', normalize=False).is_isbn_13()
    assert __ISBNChecker('978-0141015045').is_isbn_13()
    assert not __ISBNChecker('9780141015046').is_isbn_13()
    assert __ISBNChecker('9780141015046', normalize=False).is_isbn_13()
    assert not __ISBNChecker('9780141015047').is_isbn_13()
    assert not __ISBNChecker('9780141015047', normalize=False).is_isbn_13()
    assert not __ISBNChecker('9780141015048').is_is

# Generated at 2022-06-14 05:43:03.719106
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') == True
    assert is_json('[1, 2, 3]') == True
    assert is_json('{nope}') == False



# Generated at 2022-06-14 05:43:07.818847
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') == True
    assert is_json('[1, 2, 3]') == True
    assert is_json('{nope}') == False



# Generated at 2022-06-14 05:43:10.211697
# Unit test for function is_url
def test_is_url():
    assert is_url('http://www.mysite.com') is True
    assert is_url('https://mysite.com') is True
    assert is_url('.mysite.com') is False


# Generated at 2022-06-14 05:43:14.257750
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') is True
    assert is_json('[1, 2, 3]') is True
    assert is_json('{"name": "Peter", "age": 20}') is True
    assert is_json('{"name": "Peter", "hobbies": ["Fishing", "Sailing"]}') is True
    assert is_json('{nope}') is False

# End of is_json()



# Generated at 2022-06-14 05:43:21.613302
# Unit test for function is_url
def test_is_url():
    assert is_url(None) == False
    assert is_url('www.url.fr') == False
    assert is_url('url.fr') == False
    assert is_url('https://www.url.fr') == True
    assert is_url('http://www.url.fr') == True
    assert is_url('ftp://www.url.fr') == False



# Generated at 2022-06-14 05:43:31.789773
# Unit test for function is_email
def test_is_email():
    assert is_email('my.email@the-provider.com')
    assert is_email('my.email@the-provider.com ')
    assert not is_email('@gmail.com')
    assert not is_email('my.email@the-providercom')
    assert not is_email('my email@the-provider.com')
    assert not is_email('my . email@the-provider.com')
    assert not is_email('my. email@the-provider.com')
    assert not is_email('my..email@the-provider.com')
    assert not is_email('my.email@the-provider.com.')

    assert is_email('my.email@gmail.com')
    assert is_email('my.email@gmail.com ')
    assert is_email

# Generated at 2022-06-14 05:43:39.145937
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker('978-83-926174-4-3').is_isbn_13() is True
    assert __ISBNChecker('978-83-926174-4-4').is_isbn_13() is False
    assert __ISBNChecker('1').is_isbn_13() is False

# Generated at 2022-06-14 05:43:51.271122
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    # python -m unittest test_validators.py -v
    assert __ISBNChecker('978-0-306-40615-7').is_isbn_13() is True
    assert __ISBNChecker('9780306406157').is_isbn_13() is True
    assert __ISBNChecker('978-0306406157').is_isbn_13() is True
    assert __ISBNChecker('978030640615').is_isbn_13() is False
    assert __ISBNChecker('978-030640615').is_isbn_13() is False
    assert __ISBNChecker('97803064061574').is_isbn_13() is False
    assert __ISBNChecker('978-03064061574').is_isbn_13() is False
    assert __IS

# Generated at 2022-06-14 05:44:00.872404
# Unit test for function is_email
def test_is_email():
    assert is_email('test#test@test.test.test') == True
    assert is_email('my.email@the-provider.com') == True
    assert is_email('my.email@the-provider.con') == False
    assert is_email('@gmail.com') == False


# Generated at 2022-06-14 05:44:10.226601
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker('978-7-115-26332-8').is_isbn_13()
    assert __ISBNChecker('9787115263325').is_isbn_13()
    assert not __ISBNChecker('978-7-115-26332-2').is_isbn_13()
    assert not __ISBNChecker('978-7-115-26332-6').is_isbn_13()

    # normalize test
    assert __ISBNChecker('978-7-115-26332-8', normalize=False).is_isbn_13()
    assert not __ISBNChecker('978-7-115-26332-6', normalize=False).is_isbn_13()

    # should raise InvalidInputError

# Generated at 2022-06-14 05:44:12.647201
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}')
    assert is_json('[1, 2, 3]')
    assert not is_json('{nope}')



# Generated at 2022-06-14 05:44:15.109085
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker('9780302911870').is_isbn_13(), 'invalid isbn13'
test___ISBNChecker_is_isbn_13()


# Generated at 2022-06-14 05:44:18.480355
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') == True
    assert is_json('[1, 2, 3]') == True
    assert is_json('{nope}') == False



# Generated at 2022-06-14 05:44:27.536487
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75')
    assert is_ip_v4('255.200.100.0')
    assert is_ip_v4('0.0.0.0')
    assert is_ip_v4('255.255.255.255')
    assert not is_ip_v4('nope')
    assert not is_ip_v4('255.200.100.999')

if __name__ == '__main__':
    test_is_ip_v4()


# Generated at 2022-06-14 05:44:38.860639
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker('080442957X').is_isbn_10() is True
    assert __ISBNChecker('0-306-40615-2').is_isbn_10() is True
    assert __ISBNChecker('0306406152').is_isbn_10() is True
    assert __ISBNChecker('9780306406157').is_isbn_10() is False
    assert __ISBNChecker('0-306-40615-2').is_isbn_10() is True
    assert __ISBNChecker('0-3-06-40615-2').is_isbn_10() is True
    assert __ISBNChecker('0-306-40615-2').is_isbn_10() is True
    assert __ISBNChecker('0-306406152').is_isbn

# Generated at 2022-06-14 05:44:53.110096
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker("jfhqrTsT").is_isbn_10() == False
    assert __ISBNChecker("").is_isbn_10() == False
    assert __ISBNChecker("123456789").is_isbn_10() == True
    assert __ISBNChecker("1234567890").is_isbn_10() == False
    assert __ISBNChecker("7421394761").is_isbn_10() == False
    assert __ISBNChecker("7421394762").is_isbn_10() == True
    assert __ISBNChecker("817654237X").is_isbn_10() == True
    assert __ISBNChecker("1-4302-1949-8").is_isbn_10() == False

# Generated at 2022-06-14 05:44:59.539382
# Unit test for function is_url

# Generated at 2022-06-14 05:45:03.243699
# Unit test for function is_url
def test_is_url():
    assert is_url('http://www.mysite.com') == True
    assert is_url('https://mysite.com') == True
    assert is_url('.mysite.com') == False



# Generated at 2022-06-14 05:45:10.546624
# Unit test for function is_url
def test_is_url():
    assert is_url('http://www.mysite.com') == True
    assert is_url('https://mysite.com') == True
    assert is_url('.mysite.com') == False


# Generated at 2022-06-14 05:45:14.834703
# Unit test for function is_url
def test_is_url():
    assert is_url("http://www.mysite.com") == True
    assert is_url("http://www.mysite2.com") == True
    assert is_url("https://mysite.com") == True
    assert is_url("ftp://mysite.com") == False



# Generated at 2022-06-14 05:45:17.686819
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker("978-0596804848").is_isbn_13() == True


# Generated at 2022-06-14 05:45:24.643399
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker('0-8436-1738-0').is_isbn_10() is True
    assert __ISBNChecker('080442957X').is_isbn_10() is True
    assert __ISBNChecker('0-306-40615-2').is_isbn_10() is True
    assert __ISBNChecker('0-684-84328-5').is_isbn_10() is True
    assert __ISBNChecker('0-684-84328-6').is_isbn_10() is False
    assert __ISBNChecker('0-684-84328').is_isbn_10() is False
    assert __ISBNChecker('').is_isbn_10() is False

# PUBLIC API



# Generated at 2022-06-14 05:45:30.883798
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4('255.200.100.75') == True
    assert is_ip_v4('nope') == False
    assert is_ip_v4('255.200.100.999') == False

# Test is_ip_v4
test_is_ip_v4()

# End of function is_ip_v4


# Generated at 2022-06-14 05:45:42.134590
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():
    assert __ISBNChecker('0001234567').is_isbn_10()
    assert not __ISBNChecker('0001234568').is_isbn_10()
    assert not __ISBNChecker('000123456').is_isbn_10()
    assert not __ISBNChecker('000123456789').is_isbn_10()
    assert not __ISBNChecker('00012345678').is_isbn_10()
    assert not __ISBNChecker('00012345678.').is_isbn_10()


# PUBLIC API



# Generated at 2022-06-14 05:45:43.699847
# Unit test for function is_url
def test_is_url():
    assert is_url('http://www.mysite.com') == True



# Generated at 2022-06-14 05:45:46.559911
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4("1.1.1.1") == True

# Generated at 2022-06-14 05:45:56.314110
# Unit test for function is_email
def test_is_email():
    return_bool = is_email('my.email@the-provider.com')
    return_bool2 = is_email('@gmail.com')
    return_bool3 = is_email('.gmail.com')
    return_bool4 = is_email('gomail.com')
    return_bool5 = is_email('go mail.com')
    return_bool6 = is_email('my.email@the-provider.com@gmail.com')
    return_bool7 = is_email('my.email@the-provider.com@@gmail.com')
    return_bool8 = is_email('my.email@the-provider.com@gmail.com ')
    return_bool9 = is_email('a@a.com')
    return_bool10 = is_email('gmail.com')
    return_

# Generated at 2022-06-14 05:46:00.356035
# Unit test for function is_ip_v4
def test_is_ip_v4():
    assert is_ip_v4("255.200.100.75")
    assert is_ip_v4("0.0.0.0")
    assert not is_ip_v4("nope")
    assert not is_ip_v4("255.200.100.999")


# Generated at 2022-06-14 05:46:16.966170
# Unit test for function is_email
def test_is_email():
    assert is_email('example@example.com') == True
    assert is_email('example@exmple.com') == False
    assert is_email('email@example.co') == True
    assert is_email('email@example.co.uk') == True
    assert is_email('e.xample@example.co.uk') == True
    assert is_email('e.xample.2@example.co.uk') == True
    assert is_email('-email@example.com') == True
    assert is_email('_email@example.com') == True
    assert is_email('email@example-example.com') == True
    assert is_email('email@example_example.com') == True
    assert is_email('email@example.com') == True
    assert is_email('email@example.example')

# Generated at 2022-06-14 05:46:19.969983
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}')
    assert not is_json('{"name": "Peter"}{"animal": "dog"}')
    assert not is_json('')



# Generated at 2022-06-14 05:46:33.752672
# Unit test for function is_email
def test_is_email():
    assert is_email("test@test.com") == True
    assert is_email("test123@test123.com") == True
    assert is_email("test_test@test.com") == True
    assert is_email("test.test@test.com") == True
    assert is_email("test_test@test123.com") == True
    assert is_email("test@test.bar") == True
    assert is_email("test.test@test.bar") == True
    assert is_email("test!test@test.com") == False
    assert is_email("test@com") == False
    assert is_email("test@com.b") == False
    assert is_email("test@com.bar.b") == False
    assert is_email("test@.com") == False

# Generated at 2022-06-14 05:46:38.943909
# Unit test for function is_url
def test_is_url():
    for correct in ['http://www.mysite.com', 'https://mysite.com', 'ftp://ftp.mysite.com']:
        assert is_url(correct)

    for incorrect in ['www.mysite.com', '', 123]:
        assert not is_url(incorrect)



# Generated at 2022-06-14 05:46:42.289020
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') == True
    assert is_json('[1, 2, 3]') == True
    assert is_json('{nope') == False


# Generated at 2022-06-14 05:46:48.319175
# Unit test for function is_url
def test_is_url():
    assert is_url('http://www.mysite.com') # returns true
    assert is_url('https://mysite.com') # returns true
    assert not is_url('.mysite.com') # returns false






# Generated at 2022-06-14 05:46:59.291871
# Unit test for function is_email
def test_is_email():
    assert is_email('') == False
    assert is_email('.') == False
    assert is_email('abc') == False
    assert is_email('abc.com') == False
    assert is_email('abc@com') == False
    assert is_email('abc123@gmail.com') == True
    assert is_email('a.b.c@hotmail.com') == True
    assert is_email('postmaster@gmail.com') == True
    assert is_email('@gmail.com') == False
    assert is_email('a..b@gmail.com') == False
    assert is_email('abc de@gmail.com') == False
    assert is_email('abc\\ de@gmail.com') == True  # We cannot verify this case because we are using python3

# Generated at 2022-06-14 05:47:11.502791
# Unit test for function is_email
def test_is_email():
    assert EMAIL_RE.match('simple@example.com')
    assert EMAIL_RE.match('very.common@example.com')
    assert EMAIL_RE.match('disposable.style.email.with+symbol@example.com')
    assert EMAIL_RE.match('other.email-with-dash@example.com')
    assert EMAIL_RE.match('x@example.com')
    assert EMAIL_RE.match('email@123.123.123.123')
    assert EMAIL_RE.match('"much.more unusual"@example.com')
    assert EMAIL_RE.match('"very.unusual.@.unusual.com"@example.com')

# Generated at 2022-06-14 05:47:20.087603
# Unit test for function is_url
def test_is_url():
    assert is_url("http://www.mysite.com"), "Should assert success"
    assert is_url("https://mysite.com"), "Should assert success"
    assert is_url("https://www.mysite.com"), "Should assert success"
    assert is_url("ftp://www.mysite.com"), "Should assert success"
    assert not is_url(".mysite.com") , "Should assert fail"



# Generated at 2022-06-14 05:47:26.695203
# Unit test for function is_url
def test_is_url():
    assert not is_url('.mysite.com')
    assert not is_url('https://www.my.site.com')
    assert is_url('http://www.mysite.com')
    assert is_url('https://mysite.com')

is_email = lambda input_string: is_full_string(input_string) and EMAIL_RE.match(input_string) is not None

# Generated at 2022-06-14 05:47:44.290847
# Unit test for function is_json

# Generated at 2022-06-14 05:47:47.803375
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker('9780131101626').is_isbn_13() is True
    # Unit test for method is_isbn_10 of class __ISBNChecker

# Generated at 2022-06-14 05:47:53.358613
# Unit test for function is_json
def test_is_json():
    asserts = ['{"name": "Peter"}',
               '[1, 2, 3]',
               '{nope}']
    results = [True, True, False]
    passed = 0
    for i in range(3):
        if is_json(asserts[i]) == results[i]:
            passed += 1
        else:
            print(f'Test {i} failed')
    print(f'is_json test passed {passed} out of 3')

test_is_json()


# Generated at 2022-06-14 05:47:55.718273
# Unit test for function is_json
def test_is_json():
    assert not is_json(None)
    assert not is_json('')
    assert not is_json('  ')
    assert is_json('{}')
    assert is_json('{"name": "Peter"}')
    assert is_json('[1, 2, 3]')
    assert not is_json('{nope}')



# Generated at 2022-06-14 05:48:04.094792
# Unit test for function is_email
def test_is_email():
    # Valid emails
    assert is_email("john.smith@gmail.com")
    assert is_email("jsmith@gmail.com")
    assert is_email("john.smith@my.university.edu")
    assert is_email("john+smith@gmail.com")
    assert is_email("john+smith@my.university.edu")
    assert is_email("john.smith@gmail.co.uk")
    assert is_email("john.smith@gmail.travel")
    assert is_email("john.smith@gmail.aaa")
    assert is_email("john.smith@gmail.museum")
    assert is_email("john.smith@gmail.int")
    assert is_email("john.smith@gmail.coop")
    assert is_email("john.smith@gmail.gov")
    assert is_email

# Generated at 2022-06-14 05:48:05.854764
# Unit test for function is_json
def test_is_json():
    assert is_json('{"name": "Peter"}') # returns true


# Generated at 2022-06-14 05:48:17.475475
# Unit test for function is_email

# Generated at 2022-06-14 05:48:20.432338
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert (__ISBNChecker('978-3-16-148410-0').is_isbn_13() == True)

# Generated at 2022-06-14 05:48:31.615846
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():
    assert __ISBNChecker('978-1-56619-909-4').is_isbn_13(), 'ISBN-13 checksum failed'
    assert __ISBNChecker('978-1-56619-909-3', normalize=False).is_isbn_13(), 'ISBN-13 checksum failed'
    assert not __ISBNChecker('978-1-56619-909-5').is_isbn_13(), 'Invalid ISBN-13 passed'
    assert not __ISBNChecker('978-1-56619-909-5', normalize=False).is_isbn_13(), 'Invalid ISBN-13 passed'
    assert not __ISBNChecker('156619-909-4').is_isbn_13(), 'Invalid ISBN-13 passed'
