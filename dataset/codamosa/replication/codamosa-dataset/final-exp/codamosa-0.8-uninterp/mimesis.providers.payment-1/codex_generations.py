

# Generated at 2022-06-14 00:36:17.676645
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    card_number = payment.credit_card_number()
    print(card_number)
    assert len(card_number) == 19
    assert card_number[4] == ' '
    assert card_number[9] == ' '
    assert card_number[14] == ' '

# Generated at 2022-06-14 00:36:27.787992
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    from mimesis import Person
    import unittest
    from decimal import Decimal
    from mimesis.enums import CardType
    import random

    x = Payment('en', seed=random.randint(1,999))

    # Test with CardType.VISA
    y = x.credit_card_number(CardType.VISA)
    assert type(y) is str
    assert len(y) == 19
    assert y[1] == '4'
    assert y[17] == y[18]

    # Test with CardType.MASTER_CARD
    y = x.credit_card_number(CardType.MASTER_CARD)
    assert type(y) is str
    assert len(y) == 19

# Generated at 2022-06-14 00:36:34.875279
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    assert Payment().credit_card_number(CardType.VISA) == "4011 0252 9674 5559"
    assert Payment().credit_card_number(CardType.MASTER_CARD) == "5491 8959 0231 7563"
    assert Payment().credit_card_number(CardType.AMERICAN_EXPRESS) == "3404 4244 0996 772"

# Generated at 2022-06-14 00:36:40.628217
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment(seed=42)
    result = payment.credit_card_number()
    assert result == '4332 8937 3466 0562'
    result = payment.credit_card_number(CardType.AMERICAN_EXPRESS)
    assert result == '3409 947672 89438'


# Generated at 2022-06-14 00:36:50.479743
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    # Set seed
    # __init__(self, *, seed: t.Optional[t.Union[int, str]] = None)
    cc = Payment(seed = 9)

    # 1. Make 40000 random payments with the same seed.
    #   Verify the prefix of all the card numbers are 4
    count = 40000
    prefix = '4'
    while count > 0:
        res = cc.credit_card_number()
        assert res[0] == prefix
        count -= 1
    # 2. Make 40000 random payments with the same seed.
    #   Verify the prefix of all the card numbers are 5
    cc = Payment(seed = 6)
    count = 40000
    prefix = '5'
    while count > 0:
        res = cc.credit_card_number()
        assert res[0] == prefix
       

# Generated at 2022-06-14 00:36:54.409755
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment(seed=42)
    payment.Credit_card_number(CardType.VISA)
    assert credit_card_number == '4443 3631 1546 1245'

# Generated at 2022-06-14 00:37:03.545181
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Unit test for the method credit_card_number of class Payment"""

    # Arrange
    seed = 1
    my_Payment = Payment(seed=seed)
    card_type = CardType.VISA
    
    # Act
    result = my_Payment.credit_card_number(card_type=card_type)

    # Assert
    expected = '4455 5299 1152 2450'
    assert result == expected

# Generated at 2022-06-14 00:37:12.596498
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Unit test for method credit_card_number of class Payment"""

    payment = Payment()

    for _ in range(10):
        card_number = payment.credit_card_number(card_type=CardType.MASTER_CARD)
        card_number = card_number.replace(' ', '')
        assert len(card_number) == 16
        assert luhn_checksum(card_number) == 0
        assert int(card_number[0:2]) > 22 and int(card_number[0:2]) < 28
        assert int(card_number[0:2]) == 51 or int(card_number[0:2]) == 55

    for _ in range(10):
        card_number = payment.credit_card_number(card_type=CardType.AMERICAN_EXPRESS)
        card_number = card

# Generated at 2022-06-14 00:37:20.607295
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    # Setup test data
    from mimesis.enums import CardType
    p = Payment(1)
    test_types = [CardType.AMERICAN_EXPRESS, CardType.VISA, CardType.MASTER_CARD]
    test_lengths = [15, 16, 16]
    test_patterns = [re.compile(r'(\d{4})(\d{6})(\d{5})'), re.compile(r'(\d{4})(\d{4})(\d{4})(\d{4})'), re.compile(r'(\d{4})(\d{4})(\d{4})(\d{4})')]

    # Perform test
    test_results = []
    for index, test_type in enumerate(test_types):
        test_

# Generated at 2022-06-14 00:37:23.039176
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment("it")
    ccn = p.credit_card_number(CardType.MASTER_CARD)
    assert len(ccn.replace(" ", "")) == 16


# Generated at 2022-06-14 00:37:30.938359
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    assert Payment().credit_card_number(CardType.VISA) == "4539 8496 5292 9697"
    assert CardType.MASTER_CARD.value in Payment().credit_card_number(CardType.MASTER_CARD)
    assert CardType.AMERICAN_EXPRESS.value in Payment().credit_card_number(CardType.AMERICAN_EXPRESS)

# Generated at 2022-06-14 00:37:41.157733
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    from mimesis.enums import CardType
    from mimesis.exceptions import NonEnumerableError
    from mimesis.providers.payment import Payment
    payment = Payment()
    assert payment.credit_card_number(card_type=CardType.VISA)
    assert payment.credit_card_number(card_type=CardType.MASTER_CARD)
    assert payment.credit_card_number(card_type=CardType.AMERICAN_EXPRESS)
    try:
        payment.credit_card_number(card_type=CardType.UNION_PAY)
    except NonEnumerableError as e:
        assert e.code == "EP0014"
        assert e.default_message == "The name of enumerable is not supported."

# Generated at 2022-06-14 00:37:56.990009
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Test for credit_card_number method."""
    from mimesis import Payment
    from mimesis.enums import CardType

    payment = Payment('en')
    assert payment.credit_card_number(CardType.VISA).startswith(('4', '5'))
    assert payment.credit_card_number(CardType.AMERICAN_EXPRESS).startswith(
        ('3', '1'))
    assert payment.credit_card_number(CardType.DINERS_CLUB).startswith(
        ('3', '2'))
    assert payment.credit_card_number(CardType.DISCOVER).startswith(('6', '5'))
    assert payment.credit_card_number(CardType.JCB).startswith('3')

# Generated at 2022-06-14 00:38:01.321421
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    from mimesis.enums import CardType
    from mimesis.providers.payment import Payment

    provider = Payment('en')
    assert len(provider.credit_card_number()) == 16
    assert len(provider.credit_card_number(CardType.AMERICAN_EXPRESS)) == 15
    

# Generated at 2022-06-14 00:38:11.277965
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    # Checking exceptions
    payment = Payment()
    try:
        payment.credit_card_number(CardType.DISCOVER)
    except Exception as e:
        assert isinstance(e, NonEnumerableError)

    # Checking that method returns a valid card number
    payment = Payment("en", seed=42)
    cc_number = payment.credit_card_number()
    assert luhn_checksum(cc_number.replace(" ", "")) == 0
    payment.seed(42)
    cc_number2 = payment.credit_card_number()
    assert cc_number == cc_number2

# Generated at 2022-06-14 00:38:16.316880
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment('zh')
    cardnum = payment.credit_card_number(CardType.MASTER_CARD)
    assert cardnum == '5125 9316 6941 8852'

# Generated at 2022-06-14 00:38:21.780497
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    from mimesis.enums import CardType
    from mimesis.providers.payment import Payment
    provider = Payment()
    for i in range(100):
        card = provider.credit_card_number(CardType.AMERICAN_EXPRESS)
        numbers = ''.join(card.split(' '))
        assert len(card) == 19
        assert luhn_checksum(numbers.replace(' ', '')) == numbers[-1]

# Generated at 2022-06-14 00:38:25.883351
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    x = Payment(seed=42)
    card_number = x.credit_card_number()
    assert card_number == '4585 3071 7787 5919'
    

# Generated at 2022-06-14 00:38:41.008154
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    assert Payment().credit_card_number(card_type=CardType.VISA) in ['4455 5299 1152 2450', '4647 6478 3390 3261', '4929 5398 2871 0086', '4667 6084 4108 2428', '4179 3858 7552 2704']
    assert Payment().credit_card_number(card_type=CardType.MASTER_CARD) in ['2221 6155 1177 8495', '5570 5999 5045 4910', '5532 3591 4606 8586', '5532 8223 9303 5385', '5500 9610 5236 0114', '5587 5781 3292 6165', '5588 0590 4857 9766']

# Generated at 2022-06-14 00:38:45.668563
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    assert len(Payment.credit_card_number()) == 19
    assert len(Payment.credit_card_number(CardType.MASTER_CARD)) == 19
    assert len(Payment.credit_card_number(CardType.AMERICAN_EXPRESS)) == 17

# Generated at 2022-06-14 00:38:57.796606
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    assert len(Payment().credit_card_number()) == 19
    assert len(Payment().credit_card_number(CardType.VISA)) == 19
    assert len(Payment().credit_card_number(CardType.MASTER_CARD)) == 19
    assert len(Payment().credit_card_number(CardType.AMERICAN_EXPRESS)) == 17


# Generated at 2022-06-14 00:39:07.292473
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Unit test for method credit_card_number of class Payment
    """
    p_1 = Payment(seed=100)
    p_2 = Payment(seed=100)

    assert p_1.credit_card_number(CardType.VISA) == '4455 5299 1152 2450'
    assert p_2.credit_card_number(CardType.MASTER_CARD) == '5491 8056 4386 8017'
    assert p_1.credit_card_number(CardType.AMERICAN_EXPRESS) == '3775 039391 06811'



# Generated at 2022-06-14 00:39:17.709215
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment('en')
    expected_value = ({"VISA": "4455 5299 1152 2450",
                       "AMERICAN_EXPRESS": "3737 7019 176 5190",
                       "MASTER_CARD": "2221 0571 3348 6072"})
    assert isinstance(payment.credit_card_number(CardType.VISA),
                      str) == True
    assert isinstance(payment.credit_card_number(CardType.AMERICAN_EXPRESS),
                      str) == True
    assert isinstance(payment.credit_card_number(CardType.MASTER_CARD),
                      str) == True
    assert payment.credit_card_number(
    ) in expected_value.values() == True

# Generated at 2022-06-14 00:39:24.296932
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment()
    card_type = CardType.VISA
    credit_card_number = p.credit_card_number(card_type)
    assert len(credit_card_number) >= 16 and len(credit_card_number) <= 19
    assert int(credit_card_number[0:1]) == 4


# Generated at 2022-06-14 00:39:35.533514
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment('en')
    res = payment.credit_card_number(CardType.AMERICAN_EXPRESS)
    assert len(res) == 19
    assert res[0:2] == '37'
    assert res[4:6] == '15'
    try:
        payment.credit_card_number('BANANA')
        assert True == False
    except NonEnumerableError:
        assert True == True
    res = payment.credit_card_number(CardType.MASTER_CARD)
    assert len(res) == 19
    assert int(res[0:4]) > 2221
    assert int(res[0:4]) < 2720 or int(res[0:4]) > 5100
    assert int(res[0:4]) < 5599

# Generated at 2022-06-14 00:39:36.773397
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    assert len(Payment('en').credit_card_number()) == 16

# Generated at 2022-06-14 00:39:37.684585
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    assert Payment().credit_card_number()

# Generated at 2022-06-14 00:39:41.577655
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    # print(payment.credit_card_number(CardType.VISA))
    # print(payment.credit_card_number(CardType.MASTER_CARD))
    # print(payment.credit_card_number(CardType.AMERICAN_EXPRESS))
    # print(payment.credit_card_number(CardType.DISCOVER))


# Generated at 2022-06-14 00:39:51.731030
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """ Unit test for method credit_card_number of class Payment """
    # It creates a Payment object
    provider = Payment()
    # It generates a random credit card number
    number = provider.credit_card_number(CardType.VISA)
    assert len(number) == 19
    # It generates a random credit card number
    number = provider.credit_card_number(CardType.MASTER_CARD)
    assert len(number) == 19
    # It generates a random credit card number
    number = provider.credit_card_number(CardType.AMERICAN_EXPRESS)
    assert len(number) == 17
    # It generates a random credit card number
    number = provider.credit_card_number()
    # It checks that the credit card number is valid

# Generated at 2022-06-14 00:40:06.912301
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    import random
    import datetime
    from mimesis.enums import CardType
    from mimesis.providers.payment import Payment

    gen = Payment(random.seed(123))

    # ------- Card Type -------
    assert gen.credit_card_number(CardType.VISA) == "4555 5299 1152 2450"
    assert gen.credit_card_number(CardType.MASTER_CARD) == "5205 4273 4761 9502"
    assert gen.credit_card_number(CardType.AMERICAN_EXPRESS) == "3766 803875 08311"

    # ------- Credit card number length -------
    assert len(gen.credit_card_number(CardType.VISA)) == 19
    assert len(gen.credit_card_number(CardType.MASTER_CARD)) == 19


# Generated at 2022-06-14 00:40:30.773261
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    credit_card_number = payment.credit_card_number(card_type=CardType.VISA)
    assert credit_card_number[0] == '4'
    assert len(credit_card_number) == 19


# Generated at 2022-06-14 00:40:41.154784
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Test for credit_card_number."""
    payment = Payment()
    
    # Test case 1: Default card type
    card_number = payment.credit_card_number()
    assert re.search(r'\d{16}', card_number)

    # Test case 2: American Express
    card_number = payment.credit_card_number(CardType.AMERICAN_EXPRESS)
    assert re.search(r'\d{15}', card_number)

    # Test case 3: Unsupported card type
    with pytest.raises(NonEnumerableError):
        payment.credit_card_number(CardType.CHINA_UNION_PAY)

# Generated at 2022-06-14 00:40:44.794270
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    payment.credit_card_number(CardType.MASTER_CARD)
    payment.credit_card_number(CardType.VISA)
    payment.credit_card_number(CardType.AMERICAN_EXPRESS)

test_Payment_credit_card_number()


# Generated at 2022-06-14 00:40:54.345411
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Test for method ``credit_card_number`` of class ``Payment``."""
    payment = Payment()
    # type: str
    visa = payment.credit_card_number(CardType.VISA)
    master_card = payment.credit_card_number(CardType.MASTER_CARD)
    amex = payment.credit_card_number(CardType.AMERICAN_EXPRESS)
    # type: str
    regex = re.compile(r'^\d{4} \d{4} \d{4} \d{4}$')
    assert regex.match(visa)
    assert regex.match(master_card)
    assert len(amex) == 15



# Generated at 2022-06-14 00:40:57.110550
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    assert Payment().credit_card_number(CardType.MASTER_CARD) == '5500 0098 8210 8661'


# Generated at 2022-06-14 00:41:10.560465
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    # Test when card_type is not in [VISA, MASTER_CARD, AMERICAN_EXPRESS]
    payment = Payment(seed=42)
    card_type = 'TEST'
    try:
        payment.credit_card_number(card_type)
        assert False  # If Error is not NonEnumerableError
    except NonEnumerableError as e:
        assert str(e) == 'TEST is not included in the enumerable CardType'
    # Test when card_type is in [VISA, MASTER_CARD, AMERICAN_EXPRESS]
    card_type = CardType.VISA

# Generated at 2022-06-14 00:41:15.768709
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    card = Payment()
    assert len(card.credit_card_number()) == 20
    assert len(card.credit_card_number(card_type=CardType.AMERICAN_EXPRESS)) == 19


# Generated at 2022-06-14 00:41:23.546001
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    import mimesis
    card_type = mimesis.CardType.VISA
    cc_provider = mimesis.Payment()
    cc_number = cc_provider.credit_card_number(card_type=card_type)
    print(cc_number)
    ccn = cc_number.replace(' ', '')
    print(ccn)
    luhn_check_remainder = int(ccn) % 10
    print(luhn_check_remainder)
    mod10_checksum = cc_provider.luhn_checksum(ccn)
    print(mod10_checksum)
    print(luhn_check_remainder == mod10_checksum)

# Generated at 2022-06-14 00:41:30.747198
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    x = Payment()
    for _ in range(100):
        # Check if the card num has the right length
        if len(x.credit_card_number()) != 16:
            raise Exception("Credit card number should have length 16")

        # Check if the card num has the right length
        if len(x.credit_card_number(CardType.AMERICAN_EXPRESS)) != 15:
            raise Exception("Credit card number should have length 15")

# Generated at 2022-06-14 00:41:36.604639
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    # Case 1: Default
    result = Payment().credit_card_number()
    is_valid = False
    if (result[0] == '4'):
        is_valid = True
    assert result[0] == '4'
    assert is_valid == True


# Generated at 2022-06-14 00:42:18.601359
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    a = Payment().credit_card_number(CardType.VISA)
    b = Payment().credit_card_number(CardType.MASTER_CARD)
    c = Payment().credit_card_number(CardType.AMERICAN_EXPRESS)

    print(a)
    print(b)
    print(c)

test_Payment_credit_card_number()

# Generated at 2022-06-14 00:42:22.228773
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    gen = Payment()
    assert gen.credit_card_number().split()[0][0] == '4'
    assert gen.credit_card_number(CardType.MASTER_CARD).split()[0][0] == '5'
    assert gen.credit_card_number(CardType.AMERICAN_EXPRESS).split()[0][0] in ('3', '4')

# Generated at 2022-06-14 00:42:33.027334
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    from mimesis.enums import CardType
    from mimesis.exceptions import NonEnumerableError
    from mimesis.random import Random

    random = Random()
    payment = Payment(random=random)
    print("Test credit_card_number method of class Payment :\n")
    for i in range(5):
        print("\t" + "card number : " + payment.credit_card_number() + "\n")
    for i in range(5):
        print("\t" + "card number : " + payment.credit_card_number(CardType.VISA) + "\n")
    for i in range(5):
        print("\t" + "card number : " + payment.credit_card_number(CardType.MASTER_CARD) + "\n")

# Generated at 2022-06-14 00:42:34.889617
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    card_type = CardType.VISA

    for _ in range(10):
        print(payment.credit_card_number(card_type))

# Generated at 2022-06-14 00:42:41.811446
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    # test1 未指定卡类型test
    p = Payment(seed=2333)
    card_type = p.credit_card_type(CardType.VISA)
    print("test1: ")
    print(card_type)

    # test2 指定卡类型test
    p = Payment(seed=2333)
    card_type = p.credit_card_type(CardType.MASTER_CARD)
    print("test2: ")
    print(card_type)

    # test3 指定卡类型test
    p = Payment(seed=2333)
    card_type = p.credit_card_type(CardType.AMERICAN_EXPRESS)

# Generated at 2022-06-14 00:42:47.841845
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    print(payment.credit_card_number(CardType.VISA))
    print(payment.credit_card_number(CardType.MASTER_CARD))
    print(payment.credit_card_number(CardType.AMERICAN_EXPRESS))


# Generated at 2022-06-14 00:43:00.210256
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    from mimesis.enums import CardType
    from mimesis.providers.payment import Payment

    p = Payment()
    for _ in range(100):
        # Test for visa format
        card_number = p.credit_card_number(card_type=CardType.VISA)
        assert re.match(r'^4\d{15}$', card_number.replace(' ', ''))

        # Test for master card format
        card_number = p.credit_card_number(card_type=CardType.MASTER_CARD)
        assert re.match(r'^5[1-5]\d{14}$', card_number.replace(' ', ''))

        # Test for American express card format

# Generated at 2022-06-14 00:43:07.332808
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    # Create a random object
    p = Payment()

    #Create a list for the different random credit card number
    list = []
    for num in range(0, 100):
        list.append(p.credit_card_number())


    # Compare two numbers from the list
    # If they are equal then the method is OK
    flag = False
    for num in range(1, 100):
        flag = (list[0] == list[num])

    assert flag == False


# Generated at 2022-06-14 00:43:16.095408
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    assert Payment().credit_card_number() == '5732 0552 3176 5285'

    assert Payment().credit_card_number(CardType.VISA) == '2970 5481 0481 0117'

    assert Payment().credit_card_number(CardType.MASTER_CARD) == '2572 1744 4661 2380'

    assert Payment().credit_card_number(CardType.AMERICAN_EXPRESS) == '3751 83336 95856'



# Generated at 2022-06-14 00:43:22.208850
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    visa = payment.credit_card_number(card_type = CardType.VISA)
    master = payment.credit_card_number(card_type = CardType.MASTER_CARD)
    assert visa.find("VISA") != -1
    assert master.find("MASTERCARD") != -1

# Generated at 2022-06-14 00:44:37.358299
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    test_string = '4455 5299 1152 2450'
    test = Payment()
    assert test.credit_card_number() == test_string


# Generated at 2022-06-14 00:44:38.444364
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    cardNumber = Payment()
    assert len(cardNumber.credit_card_number()) == 19