

# Generated at 2022-06-14 00:36:27.254049
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    # Create instance of class Payment
    payment_instance = Payment()
    # Create list of card type values
    card_type_values = [
        CardType.MASTER_CARD,
        CardType.VISA,
        CardType.AMERICAN_EXPRESS
    ]
    # Check for correctness of generated data in case when
    # generating card numbers for all card types values in list
    for card_type_value in card_type_values:
        card_number = payment_instance.credit_card_number(card_type_value)
        assert len(card_number) == len(card_number.replace(' ', ''))
        assert re.match(r'^(\d{4}\s){3}\d{4}$', card_number) is not None

# Generated at 2022-06-14 00:36:41.437211
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()

    # Test visa card type
    assert re.match(r'^\d{16}$', payment.credit_card_number())
    assert re.match(r'^\d{16}$', payment.credit_card_number(CardType.VISA))

    # Test master card type
    assert re.match(r'^\d{16}$', payment.credit_card_number(
        CardType.MASTER_CARD))

    # Test American express card type
    assert re.match(r'^\d{15}$', payment.credit_card_number(
        CardType.AMERICAN_EXPRESS))

    # Test invalid card type
    # TODO: Change AssertError to NonEnumerableError in new version
    # assert NonEnumerableError(CardType)

# Generated at 2022-06-14 00:36:49.643156
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Unit test for method credit_card_number of class Payment."""

    p = Payment(seed=12345)

    card_number = p.credit_card_number(card_type=CardType.VISA)
    assert card_number == '4163 3238 9084 5971'

    card_number = p.credit_card_number(card_type=CardType.MASTER_CARD)
    assert card_number == '5367 8697 4096 2575'

    card_number = p.credit_card_number(card_type=CardType.AMERICAN_EXPRESS)
    assert card_number == '3736 898576 51677'

# Generated at 2022-06-14 00:37:04.651293
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Test credit_card_number()."""
    from mimesis.enums import CardType
    import re

    payment = Payment()

    # Test card_type Visa
    result_1 = payment.credit_card_number(card_type=CardType.VISA)
    pattern_1 = re.compile(r'^\d{16}$')
    assert re.search(pattern=pattern_1, string=result_1) is not None

    # Test card_type MasterCard
    result_2 = payment.credit_card_number(card_type=CardType.MASTER_CARD)
    pattern_2 = re.compile(r'^\d{16}$')
    assert re.search(pattern=pattern_2, string=result_2) is not None

    # Test card_type AmericanExpress
    result

# Generated at 2022-06-14 00:37:13.191470
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    m = Payment(seed = 0)

    assert m.credit_card_number(CardType.VISA) == "4455 5299 1152 2450"
    assert m.credit_card_number(CardType.AMERICAN_EXPRESS) == "3720 688 9234 5"
    assert m.credit_card_number(CardType.MASTER_CARD) == "5169 2107 0090 1331"

    try:
        m.credit_card_number(CardType.DISCOVER)
        assert False
    except ValueError:
        assert True

    regex = re.compile(r'(\d{4})(\d{4})(\d{4})(\d{4})')
    valid_card_number = m.credit_card_number()
    assert regex.search(valid_card_number).groups

# Generated at 2022-06-14 00:37:23.148792
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    # Initialize Payment class
    payment = Payment()
    # Create list of credit card numbers
    list_card_number = []
    # Create list of card type
    list_card_type = []
    # Create list of valid card number
    list_valid_card = []
    for i in range(100):
        # Get list of credit card number
        list_card_number.append(payment.credit_card_number())
        # Get list of card type
        list_card_type.append(payment.credit_card_number(card_type=CardType.VISA))
        list_card_type.append(payment.credit_card_number(card_type=CardType.MASTERCARD))
        list_card_type.append(payment.credit_card_number(card_type=CardType.AMERICAN_EXPRESS))

# Generated at 2022-06-14 00:37:35.853181
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment_obj = Payment()

    # Test CardType.VISA
    card_type = CardType.VISA
    number = payment_obj.credit_card_number(card_type)
    assert number[0] == '4'
    assert len(number) == 19

    # Test CardType.AMERICAN_EXPRESS
    card_type = CardType.AMERICAN_EXPRESS
    number = payment_obj.credit_card_number(card_type)
    assert len(number) == 17
    assert number[0:2] in ['34', '37']

    # Test CardType.MASTER_CARD
    card_type = CardType.MASTER_CARD
    number = payment_obj.credit_card_number(card_type)
    assert len(number) == 19

# Generated at 2022-06-14 00:37:41.527175
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    for i in range(10):
        print(payment.credit_card_number())
    for i in range(10):
        print(payment.credit_card_number(CardType.VISA))
    for i in range(10):
        print(payment.credit_card_number(CardType.MASTER_CARD))

# Generated at 2022-06-14 00:37:50.178553
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    card_type = CardType.VISA
    card_num = payment.credit_card_number(card_type)
    card_dict = {
        'VISA': r'4\d\d\d',
        'MASTERCARD': r'(5[1-5]\d\d|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)',
        'AMERICANEXPRESS': r'(34|37)',
    }
    assert len(card_num) == 19
    assert re.match(card_dict[str(card_type)], card_num.replace(' ', ''))


# Generated at 2022-06-14 00:37:53.513022
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    x = Payment()
    cc_number = x.credit_card_number(CardType.MASTER_CARD)
    assert x.credit_card_network() in cc_number

# Generated at 2022-06-14 00:38:14.745208
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment()
    assert re.match(r'^4\d{3} \d{4} \d{4} \d{4}$',
                    p.credit_card_number(CardType.VISA))
    assert re.match(r'^5\d{3} \d{4} \d{4} \d{4}$',
                    p.credit_card_number(CardType.MASTER_CARD))
    assert re.match(r'^3[47]\d{2} \d{6} \d{5}$',
                    p.credit_card_number(CardType.AMERICAN_EXPRESS))

# Generated at 2022-06-14 00:38:17.144693
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment("en")
    card_number = payment.credit_card_number(CardType.VISA)
    print("credit card number: " + card_number)


# Generated at 2022-06-14 00:38:19.730340
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    card_type = CardType.AMERICAN_EXPRESS
    assert len(payment.credit_card_number(card_type)) == 17

# Generated at 2022-06-14 00:38:25.885241
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment(seed=4)

    # Test for Visa
    assert p.credit_card_number(card_type=CardType.VISA) == "4091 0599 3586 6821"
    assert p.credit_card_number() == "4091 0599 3586 6821"
    # Test for Mastercard
    assert p.credit_card_number(card_type=CardType.MASTER_CARD) == "2223 5107 5552 0485"

    # Test for American Express
    assert p.credit_card_number(card_type=CardType.AMERICAN_EXPRESS) == "3424 271738 90128"

# Generated at 2022-06-14 00:38:31.718480
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment('en')
    value = p.credit_card_number(CardType.VISA)
    assert re.match("([0-9]{4} [0-9]{4} [0-9]{4} [0-9]{4})", value)

# Generated at 2022-06-14 00:38:35.957786
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment()
    for _ in range(20):
        ctn = p.credit_card_number()
        print(ctn)
        assert len(ctn) == 19


# Generated at 2022-06-14 00:38:44.466954
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Test for method credit_card_number of class Payment"""

    # Initialaizing object
    p = Payment()

    # It is necesary to add seed for this test, because random is
    # needed in the method to be tested
    p.seed(1234567890)

    # By default credit card type is Visa, but we want to test only
    # with this type, because we don't want to enforce the user
    # that wants to use the method to pass CardType's enum object
    result = p.credit_card_number()
    desiredResult = '4419 5037 7333 6306'
    assert result == desiredResult


# Generated at 2022-06-14 00:38:46.374963
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    for i in range(10):
        assert len(Payment().credit_card_number()) == 19

# Generated at 2022-06-14 00:38:51.543837
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    card_number = payment.credit_card_number()
    print(card_number)
    print(payment.credit_card_number(card_type=CardType.AMERICAN_EXPRESS))


# Generated at 2022-06-14 00:38:56.281953
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Provide data for tests of method credit_card_number of class Payment."""
    data = [
        (CardType.VISA,),
        (CardType.MASTER_CARD,),
        (CardType.AMERICAN_EXPRESS,)
    ]
    return data



# Generated at 2022-06-14 00:39:27.982729
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    data = payment.credit_card_number()
    assert 4 <= len(data.split()) <= 5


# Generated at 2022-06-14 00:39:30.914322
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Unit test with VISA."""
    assert re.match(r'^\d{4} \d{4} \d{4} \d{4}$', Payment().credit_card_number(CardType.VISA))


# Generated at 2022-06-14 00:39:34.658642
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment(seed=1234)
    for _ in range(10):
        try:
            payment.credit_card_number(CardType.AMERICAN_EXPRESS)
        except NonEnumerableError as e:
            print(e)



# Generated at 2022-06-14 00:39:40.403385
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    test_instance = Payment()
    test_instance.seed(0)
    assert test_instance.credit_card_number(card_type=CardType.MASTER_CARD)== "2221 5411 7167 5427"
    assert test_instance.credit_card_number(card_type=CardType.AMERICAN_EXPRESS) == "3610 8182 81"
    assert test_instance.credit_card_number(card_type=CardType.VISA) == "4231 2673 8019 2775"

# Generated at 2022-06-14 00:39:43.448945
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    assert Payment().credit_card_number()


# Generated at 2022-06-14 00:39:44.063867
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    pass

# Generated at 2022-06-14 00:39:47.270335
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment(seed=123456789)
    
    result = payment.credit_card_number(CardType.VISA)
    
    # result == "4455 5299 1152 2450"
    print(result)


# Generated at 2022-06-14 00:39:49.172848
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    tester = Payment()
    tester.credit_card_number() == '4551 5299 1315 2402'

# Generated at 2022-06-14 00:39:59.072059
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    card = payment.credit_card_number(CardType.VISA)
    assert card.startswith('4')
    assert re.match(r'\b[0-9]{16}\b', card.replace(' ', '')) is not None
    assert luhn_checksum(card.replace(' ', '')) == '0'
    card = payment.credit_card_number(CardType.MASTER_CARD)
    assert card.startswith('5')
    assert re.match(r'\b[0-9]{16}\b', card.replace(' ', '')) is not None
    assert luhn_checksum(card.replace(' ', '')) == '0'
    card = payment.credit_card_number(CardType.AMERICAN_EXPRESS)
    assert card.startsw

# Generated at 2022-06-14 00:40:06.908641
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    import unittest
    import string
    import re
    from mimesis.enums import CardType
    from mimesis.providers.payment import Payment
    import mimesis.enums

    class PaymentTestCase(unittest.TestCase):

        def setUp(self):
            self.payment = Payment()

        def test_return_type(self):
            assert isinstance(self.payment.credit_card_number(), str)

        def test_return_value(self):
            for _ in range(100):
                card = self.payment.credit_card_number()
                assert not any(i not in string.digits for i in card)
            