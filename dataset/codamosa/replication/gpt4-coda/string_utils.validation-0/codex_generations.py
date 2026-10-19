

# Generated at 2024-03-18 07:11:37.030661
# Unit test for function is_url
def test_is_url():    assert is_url('http://www.example.com')

# Generated at 2024-03-18 07:11:37.886296
# Unit test for function is_ip_v4

# Generated at 2024-03-18 07:11:39.069167
# Unit test for function is_ip_v4

# Generated at 2024-03-18 07:11:44.776984
# Unit test for function is_json
def test_is_json():    assert is_json('{"name": "John", "age": 30}') == True

# Generated at 2024-03-18 07:11:48.357069
# Unit test for function is_ip_v4

# Generated at 2024-03-18 07:11:55.147833
# Unit test for function is_ip
def test_is_ip():    assert is_ip('255.200.100.75') == True

# Generated at 2024-03-18 07:12:00.163650
# Unit test for function is_json
def test_is_json():    assert is_json('{"name": "John", "age": 30}') == True

# Generated at 2024-03-18 07:12:09.553585
# Unit test for function is_email
def test_is_email():    assert is_email('my.email@the-provider.com') == True

# Generated at 2024-03-18 07:12:15.520157
# Unit test for function is_email
def test_is_email():    assert is_email('my.email@the-provider.com') == True

# Generated at 2024-03-18 07:12:23.265221
# Unit test for function is_email
def test_is_email():    assert is_email('my.email@the-provider.com') == True

# Generated at 2024-03-18 07:12:39.468515
# Unit test for function is_ip
def test_is_ip():    assert is_ip('255.200.100.75') == True

# Generated at 2024-03-18 07:12:48.369101
# Unit test for function is_email
def test_is_email():    assert is_email('my.email@the-provider.com') == True

# Generated at 2024-03-18 07:12:54.764048
# Unit test for function is_credit_card
def test_is_credit_card():    assert is_credit_card('4111111111111111') == True

# Generated at 2024-03-18 07:13:02.347448
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():    # Valid ISBN-13
    valid_isbn_13 = "9780306406157"
    checker = __ISBNChecker(valid_isbn_13)
    assert checker.is_isbn_13(), f"{valid_isbn_13} should be a valid ISBN-13"

    # Invalid ISBN-13
    invalid_isbn_13 = "9780306406158"
    checker = __ISBNChecker(invalid_isbn_13)
    assert not checker.is_isbn_13(), f"{invalid_isbn_13} should not be a valid ISBN-13"

    # ISBN-13 with hyphens
    isbn_13_with_hyphens = "978-0-306-40615-7"
    checker = __ISBNChecker(isbn_13_with_hyphens)
    assert checker.is_isbn_13(), f"{isbn_13_with_hyphens} should be a valid ISBN-13"

    #

# Generated at 2024-03-18 07:13:09.038475
# Unit test for function is_ip
def test_is_ip():    assert is_ip('255.200.100.75') == True

# Generated at 2024-03-18 07:13:16.398472
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():    # Valid ISBN-13
    valid_isbn_13 = "9780306406157"
    checker = __ISBNChecker(valid_isbn_13)
    assert checker.is_isbn_13(), f"{valid_isbn_13} should be a valid ISBN-13"

    # Invalid ISBN-13
    invalid_isbn_13 = "9780306406158"
    checker = __ISBNChecker(invalid_isbn_13)
    assert not checker.is_isbn_13(), f"{invalid_isbn_13} should not be a valid ISBN-13"

    # ISBN-13 with hyphens
    isbn_13_with_hyphens = "978-0-306-40615-7"
    checker = __ISBNChecker(isbn_13_with_hyphens)
    assert checker.is_isbn_13(), f"{isbn_13_with_hyphens} should be a valid ISBN-13"

    #

# Generated at 2024-03-18 07:13:23.088809
# Unit test for function is_ip
def test_is_ip():    assert is_ip('255.200.100.75') == True

# Generated at 2024-03-18 07:13:29.896741
# Unit test for function is_json
def test_is_json():    assert is_json('{"name": "John", "age": 30}') == True

# Generated at 2024-03-18 07:13:31.497283
# Unit test for function is_ip_v4

# Generated at 2024-03-18 07:13:39.342209
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():    # Valid ISBN-13
    valid_isbn_13 = "9780306406157"
    checker = __ISBNChecker(valid_isbn_13)
    assert checker.is_isbn_13(), f"{valid_isbn_13} should be a valid ISBN-13"

    # Invalid ISBN-13
    invalid_isbn_13 = "9780306406158"
    checker = __ISBNChecker(invalid_isbn_13)
    assert not checker.is_isbn_13(), f"{invalid_isbn_13} should be an invalid ISBN-13"

    # ISBN-13 with hyphens
    isbn_13_with_hyphens = "978-0-306-40615-7"
    checker = __ISBNChecker(isbn_13_with_hyphens)
    assert checker.is_isbn_13(), f"{isbn_13_with_hyphens} should be a valid ISBN-13"

    # Short

# Generated at 2024-03-18 07:13:56.876211
# Unit test for function is_ip_v4

# Generated at 2024-03-18 07:14:02.466880
# Unit test for function is_email
def test_is_email():    assert is_email('my.email@the-provider.com') == True

# Generated at 2024-03-18 07:14:03.653866
# Unit test for function is_isbn
def test_is_isbn():import unittest


# Generated at 2024-03-18 07:14:10.391439
# Unit test for function is_ip_v4
def test_is_ip_v4():    assert not is_ip_v4(None)

# Generated at 2024-03-18 07:14:18.443414
# Unit test for function is_ip
def test_is_ip():    assert is_ip('255.200.100.75') == True

# Generated at 2024-03-18 07:14:27.732450
# Unit test for function is_credit_card
def test_is_credit_card():    # Test valid VISA card
    assert is_credit_card('4111111111111111', 'VISA')
    assert is_credit_card('4012888888881881', 'VISA')

    # Test valid MasterCard
    assert is_credit_card('5555555555554444', 'MASTERCARD')
    assert is_credit_card('5105105105105100', 'MASTERCARD')

    # Test valid American Express
    assert is_credit_card('378282246310005', 'AMERICAN_EXPRESS')
    assert is_credit_card('371449635398431', 'AMERICAN_EXPRESS')

    # Test valid Diners Club
    assert is_credit_card('30569309025904', 'DINERS_CLUB')
    assert is_credit_card('38520000023237', 'DINERS_CLUB')

    # Test valid Discover

# Generated at 2024-03-18 07:14:33.008335
# Unit test for function is_ip
def test_is_ip():    assert is_ip('255.200.100.75') == True

# Generated at 2024-03-18 07:14:38.748479
# Unit test for function is_email
def test_is_email():    assert is_email('my.email@the-provider.com') == True

# Generated at 2024-03-18 07:14:39.518886
# Unit test for function is_ip_v4

# Generated at 2024-03-18 07:14:47.028884
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():    # Valid ISBN-13
    valid_isbn_13 = "9780306406157"
    checker = __ISBNChecker(valid_isbn_13)
    assert checker.is_isbn_13(), f"{valid_isbn_13} should be a valid ISBN-13"

    # Invalid ISBN-13
    invalid_isbn_13 = "9780306406158"
    checker = __ISBNChecker(invalid_isbn_13)
    assert not checker.is_isbn_13(), f"{invalid_isbn_13} should not be a valid ISBN-13"

    # ISBN-13 with hyphens
    isbn_13_with_hyphens = "978-0-306-40615-7"
    checker = __ISBNChecker(isbn_13_with_hyphens)
    assert checker.is_isbn_13(), f"{isbn_13_with_hyphens} should be a valid ISBN-13"

    #

# Generated at 2024-03-18 07:14:58.579384
# Unit test for function is_isbn
def test_is_isbn():import unittest


# Generated at 2024-03-18 07:15:05.410394
# Unit test for function is_json
def test_is_json():    assert is_json('{"name": "John", "age": 30}') == True

# Generated at 2024-03-18 07:15:10.893093
# Unit test for function is_json
def test_is_json():    assert is_json('{"name": "John", "age": 30}') == True

# Generated at 2024-03-18 07:15:16.900702
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():    # Valid ISBN-10 without dashes
    assert __ISBNChecker("0306406152").is_isbn_10() == True
    # Valid ISBN-10 with dashes
    assert __ISBNChecker("0-306-40615-2").is_isbn_10() == True
    # Invalid ISBN-10 with wrong check digit
    assert __ISBNChecker("0306406153").is_isbn_10() == False
    # Invalid ISBN-10 with characters
    assert __ISBNChecker("0-306-40615-X").is_isbn_10() == False
    # Invalid ISBN-10 with incorrect length
    assert __ISBNChecker("030640615").is_isbn_10() == False
    # Valid ISBN-10 with X as check digit
    assert __ISBNChecker("123456789X").is_isbn_10() == True


# Generated at 2024-03-18 07:15:22.854432
# Unit test for function is_ip
def test_is_ip():    assert is_ip('255.200.100.75') == True

# Generated at 2024-03-18 07:15:30.621306
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():    # Valid ISBN-13
    valid_isbn_13 = "9780306406157"
    checker = __ISBNChecker(valid_isbn_13)
    assert checker.is_isbn_13(), f"{valid_isbn_13} should be a valid ISBN-13"

    # Invalid ISBN-13
    invalid_isbn_13 = "9780306406158"
    checker = __ISBNChecker(invalid_isbn_13)
    assert not checker.is_isbn_13(), f"{invalid_isbn_13} should not be a valid ISBN-13"

    # ISBN-13 with hyphens
    isbn_13_with_hyphens = "978-0-306-40615-7"
    checker = __ISBNChecker(isbn_13_with_hyphens)
    assert checker.is_isbn_13(), f"{isbn_13_with_hyphens} should be a valid ISBN-13"

    #

# Generated at 2024-03-18 07:15:36.491027
# Unit test for function is_ip
def test_is_ip():    assert is_ip('255.200.100.75') == True

# Generated at 2024-03-18 07:15:42.772419
# Unit test for function is_email
def test_is_email():    assert is_email('my.email@the-provider.com') == True

# Generated at 2024-03-18 07:15:43.546609
# Unit test for function is_ip_v4

# Generated at 2024-03-18 07:15:52.339694
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():    # Valid ISBN-10 without dashes
    assert __ISBNChecker("0471958697").is_isbn_10() == True
    # Valid ISBN-10 with dashes
    assert __ISBNChecker("0-471-60695-2").is_isbn_10() == True
    # Invalid ISBN-10 with wrong length
    assert __ISBNChecker("123456789").is_isbn_10() == False
    # Invalid ISBN-10 with wrong check digit
    assert __ISBNChecker("0471958699").is_isbn_10() == False
    # Invalid ISBN-10 with non-numeric characters
    assert __ISBNChecker("0-471-XXXX-2").is_isbn_10() == False
    # Valid ISBN-10 with X as check digit
    assert __ISBNChecker("0306406152").is_isbn_10() == True
    # Valid ISBN-10 with X

# Generated at 2024-03-18 07:16:11.367413
# Unit test for function is_json
def test_is_json():    assert is_json('{"name": "John", "age": 30}') == True

# Generated at 2024-03-18 07:16:12.670209
# Unit test for function is_isbn
def test_is_isbn():import unittest


# Generated at 2024-03-18 07:16:21.777340
# Unit test for function is_json
def test_is_json():    assert is_json('{"name": "John", "age": 30}') == True

# Generated at 2024-03-18 07:16:28.168673
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():    # Valid ISBN-10 without hyphens
    assert __ISBNChecker("0306406152").is_isbn_10() == True
    # Valid ISBN-10 with hyphens
    assert __ISBNChecker("0-306-40615-2").is_isbn_10() == True
    # Invalid ISBN-10
    assert __ISBNChecker("1234567890").is_isbn_10() == False
    # Invalid input (not a string)
    try:
        __ISBNChecker(123).is_isbn_10()
        assert False, "Expected an InvalidInputError"
    except InvalidInputError:
        assert True
    # Invalid input (string with invalid characters)
    assert __ISBNChecker("0-306-40A15-2").is_isbn_10() == False
    # Invalid length (too short)
    assert __ISBNChecker("123456789").is_isbn_10

# Generated at 2024-03-18 07:16:35.312248
# Unit test for function is_email
def test_is_email():    assert is_email('my.email@the-provider.com') == True

# Generated at 2024-03-18 07:16:41.830535
# Unit test for function is_ip
def test_is_ip():    assert is_ip('255.200.100.75') == True

# Generated at 2024-03-18 07:16:48.268849
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():    # Valid ISBN-13
    valid_isbn_13 = "9780306406157"
    checker = __ISBNChecker(valid_isbn_13)
    assert checker.is_isbn_13(), f"{valid_isbn_13} should be a valid ISBN-13"

    # Invalid ISBN-13
    invalid_isbn_13 = "9780306406158"
    checker = __ISBNChecker(invalid_isbn_13)
    assert not checker.is_isbn_13(), f"{invalid_isbn_13} should not be a valid ISBN-13"

    # ISBN-13 with hyphens
    isbn_13_with_hyphens = "978-0-306-40615-7"
    checker = __ISBNChecker(isbn_13_with_hyphens)
    assert checker.is_isbn_13(), f"{isbn_13_with_hyphens} should be a valid ISBN-13"

    #

# Generated at 2024-03-18 07:16:49.366245
# Unit test for function is_ip_v4

# Generated at 2024-03-18 07:16:56.915934
# Unit test for function is_email
def test_is_email():    assert is_email('my.email@the-provider.com') == True

# Generated at 2024-03-18 07:17:06.431883
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():    checker = __ISBNChecker("978-3-16-148410-0")

# Generated at 2024-03-18 07:17:25.833506
# Unit test for function is_ip
def test_is_ip():    assert is_ip('255.200.100.75') == True

# Generated at 2024-03-18 07:17:31.929306
# Unit test for function is_json
def test_is_json():    assert is_json('{"name": "John", "age": 30}') == True

# Generated at 2024-03-18 07:17:39.163890
# Unit test for function is_ip
def test_is_ip():    assert is_ip('255.200.100.75') == True

# Generated at 2024-03-18 07:17:48.324339
# Unit test for function is_json
def test_is_json():    assert is_json('{"name": "John", "age": 30}') == True

# Generated at 2024-03-18 07:17:49.432145
# Unit test for function is_isbn
def test_is_isbn():import unittest


# Generated at 2024-03-18 07:17:50.963111
# Unit test for function is_isbn
def test_is_isbn():import unittest


# Generated at 2024-03-18 07:17:51.807474
# Unit test for function is_isbn
def test_is_isbn():import unittest


# Generated at 2024-03-18 07:18:01.819257
# Unit test for function is_json
def test_is_json():    assert is_json('{"name": "John", "age": 30}') == True

# Generated at 2024-03-18 07:18:03.041630
# Unit test for function is_ip_v4

# Generated at 2024-03-18 07:18:11.689554
# Unit test for function is_ip
def test_is_ip():    assert is_ip('255.200.100.75') == True

# Generated at 2024-03-18 07:18:29.928846
# Unit test for function is_email
def test_is_email():    assert is_email('my.email@the-provider.com') == True

# Generated at 2024-03-18 07:18:35.456230
# Unit test for function is_ip
def test_is_ip():    assert is_ip('255.200.100.75') == True

# Generated at 2024-03-18 07:18:42.918408
# Unit test for function is_json
def test_is_json():    assert is_json('{"name": "John", "age": 30}') == True

# Generated at 2024-03-18 07:18:50.544697
# Unit test for function is_email
def test_is_email():    assert is_email('my.email@the-provider.com') == True

# Generated at 2024-03-18 07:18:57.197400
# Unit test for function is_email
def test_is_email():    assert is_email('my.email@the-provider.com') == True

# Generated at 2024-03-18 07:19:05.582061
# Unit test for function is_ip
def test_is_ip():    assert is_ip('255.200.100.75') == True

# Generated at 2024-03-18 07:19:06.331227
# Unit test for function is_ip_v4

# Generated at 2024-03-18 07:19:14.071340
# Unit test for function is_email
def test_is_email():    assert is_email('my.email@the-provider.com') == True

# Generated at 2024-03-18 07:19:20.824223
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():    # Valid ISBN-13
    valid_isbn_13 = "9780306406157"
    checker = __ISBNChecker(valid_isbn_13)
    assert checker.is_isbn_13(), f"{valid_isbn_13} should be a valid ISBN-13"

    # Invalid ISBN-13
    invalid_isbn_13 = "9780306406158"
    checker = __ISBNChecker(invalid_isbn_13)
    assert not checker.is_isbn_13(), f"{invalid_isbn_13} should not be a valid ISBN-13"

    # ISBN-13 with hyphens
    isbn_13_with_hyphens = "978-0-306-40615-7"
    checker = __ISBNChecker(isbn_13_with_hyphens)
    assert checker.is_isbn_13(), f"{isbn_13_with_hyphens} should be a valid ISBN-13"

    #

# Generated at 2024-03-18 07:19:21.677942
# Unit test for function is_ip_v4

# Generated at 2024-03-18 07:19:48.151586
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10():    # Valid ISBN-10 without hyphens
    assert __ISBNChecker("0306406152").is_isbn_10() == True
    # Valid ISBN-10 with hyphens
    assert __ISBNChecker("0-306-40615-2").is_isbn_10() == True
    # Invalid ISBN-10
    assert __ISBNChecker("1234567890").is_isbn_10() == False
    # Invalid input (not a string)
    try:
        __ISBNChecker(123).is_isbn_10()
        assert False, "Expected an InvalidInputError"
    except InvalidInputError:
        assert True
    # Invalid input (string with invalid characters)
    assert __ISBNChecker("030640615X").is_isbn_10() == False
    # Invalid length (too short)
    assert __ISBNChecker("306406152").is_isbn_10() == False
   

# Generated at 2024-03-18 07:19:55.551256
# Unit test for function is_email
def test_is_email():    assert is_email('my.email@the-provider.com') == True

# Generated at 2024-03-18 07:20:02.438337
# Unit test for function is_email
def test_is_email():    assert is_email('my.email@the-provider.com') == True

# Generated at 2024-03-18 07:20:08.391517
# Unit test for function is_email
def test_is_email():    assert is_email('my.email@the-provider.com') == True

# Generated at 2024-03-18 07:20:13.051227
# Unit test for function is_json
def test_is_json():    assert is_json('{"name": "John", "age": 30}') == True

# Generated at 2024-03-18 07:20:24.120595
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13():    # Valid ISBN-13
    checker = __ISBNChecker("978-3-16-148410-0")
    assert checker.is_isbn_13() is True, "Should be a valid ISBN-13"

    # Invalid ISBN-13
    checker = __ISBNChecker("978-3-16-148410-1")
    assert checker.is_isbn_13() is False, "Should be an invalid ISBN-13"

    # Valid ISBN-13 without hyphens
    checker = __ISBNChecker("9783161484100", normalize=False)
    assert checker.is_isbn_13() is True, "Should be a valid ISBN-13 without normalization"

    # Invalid length
    checker = __ISBNChecker("978-3-16-14841")
    assert checker.is_isbn_13() is False, "Should be invalid due to incorrect length"

    # Invalid characters

# Generated at 2024-03-18 07:20:31.135046
# Unit test for function is_ip
def test_is_ip():    assert is_ip('255.200.100.75') == True

# Generated at 2024-03-18 07:20:41.620058
# Unit test for function is_email
def test_is_email():    assert is_email('my.email@the-provider.com') == True

# Generated at 2024-03-18 07:20:49.903165
# Unit test for function is_ip
def test_is_ip():    assert is_ip('255.200.100.75') == True

# Generated at 2024-03-18 07:20:57.092846
# Unit test for function is_email
def test_is_email():    assert is_email('my.email@the-provider.com') == True