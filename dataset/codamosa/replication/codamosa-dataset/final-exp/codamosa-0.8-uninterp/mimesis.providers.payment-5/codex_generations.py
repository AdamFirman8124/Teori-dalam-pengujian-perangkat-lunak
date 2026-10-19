

# Generated at 2022-06-14 00:36:13.263928
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    t = Payment()
    assert t.credit_card_number() != None
    assert t.credit_card_number() != t.credit_card_number()


# Generated at 2022-06-14 00:36:17.344181
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """
    This method is to test the method credit_card_number of class Payment
    """
    payment = Payment(seed=1)
    assert all(isinstance(payment.credit_card_number(), str) for _ in range(10))



# Generated at 2022-06-14 00:36:21.568871
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    x = Payment()
    x.credit_card_number()

# Generated at 2022-06-14 00:36:27.710836
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    from mimesis import Payment
    import re

    payment = Payment()
    assert str(re.findall('\d{16}', payment.credit_card_number(CardType.VISA))).find('[4000, 4999]') != -1
    assert str(re.findall('\d{16}', payment.credit_card_number(CardType.MASTER_CARD))).find('[2221, 2720] or [5100, 5599]') != -1
    assert str(re.findall('\d{15}', payment.credit_card_number(CardType.AMERICAN_EXPRESS))).find('[34, 37]') != -1

# Generated at 2022-06-14 00:36:41.925333
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment(seed=12345)
    # Visa tests
    visa_ccn_1 = payment.credit_card_number(CardType.VISA)
    assert visa_ccn_1 == '4545 8172 2933 6489'
    visa_ccn_2 = payment.credit_card_number(CardType.VISA)
    assert visa_ccn_2 == '4339 6200 8142 7583'

    # Mastercard tests
    mastercard_ccn_1 = payment.credit_card_number(CardType.MASTER_CARD)
    assert mastercard_ccn_1 == '5550 7166 5806 8683'
    mastercard_ccn_2 = payment.credit_card_number(CardType.MASTER_CARD)

# Generated at 2022-06-14 00:36:51.005155
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    ccn1 = payment.credit_card_number()
    assert type(ccn1) == str
    assert len(ccn1) == 19

    ccn2 = payment.credit_card_number(card_type=CardType.VISA)
    assert isinstance(ccn2, str)
    assert len(ccn2) == 19

    ccn3 = payment.credit_card_number(card_type=CardType.MASTER_CARD)
    assert isinstance(ccn3, str)
    assert len(ccn3) == 19

    ccn4 = payment.credit_card_number(card_type=CardType.AMERICAN_EXPRESS)
    assert isinstance(ccn4, str)
    assert len(ccn4) == 17

# Generated at 2022-06-14 00:37:02.153533
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment('en')
    type_card = p.random.choice([CardType.VISA, CardType.MASTER_CARD, CardType.AMERICAN_EXPRESS])
    assert p.credit_card_number(type_card).__contains__(str(type_card))
    assert p.credit_card_number(type_card).__contains__(p.credit_card_expiration_date())
    assert p.credit_card_number(type_card).__contains__(p.credit_card_network())


# Generated at 2022-06-14 00:37:10.149565
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():

    print("Test 1: Creating Payment Class Object")
    payment = Payment()

    print("Test 2: Calling Credit Card method of Payment class")
    creditCard = payment.credit_card_number()

    print("Test 3: Validating a credit card number returned")
    assert len(creditCard) == 19, "Incorrect Credit Card length"
    assert re.match("^[0-9]{4} ([0-9]{4} )[0-9]{4} [0-9]{4}$", creditCard), "Incorrect Credit Card number returned"



# Generated at 2022-06-14 00:37:19.965314
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Test for method credit_card_number of class Payment."""
    assert Payment().credit_card_number() == '4455 5299 1152 2450'
    assert Payment().credit_card_number() == '4455 5299 1152 2450'
    assert Payment().credit_card_number() == '4455 5299 1152 2450'
    assert Payment().credit_card_number(CardType.VISA) == '4455 5299 1152 2450'
    assert Payment().credit_card_number(CardType.MASTER_CARD) == '5472 6289 4454 7595'
    assert Payment().credit_card_number(CardType.AMERICAN_EXPRESS) == '3488 882855 50657'

# Generated at 2022-06-14 00:37:22.123901
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    print("Payment credit_card_number(): ", payment.credit_card_number())


# Generated at 2022-06-14 00:37:35.944547
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Test method credit_card_number of class Payment."""
    # Tests with Visa card type
    visa_cards = ['4008', '4837', '4525', '4929', '4929', '4837', '4285',
                  '4532']
    for i in range(0, 5):
        payment = Payment()
        payment.random.seed(i)
        assert payment.credit_card_number(card_type=CardType.VISA)\
            .startswith(visa_cards[i])

    # Tests with MasterCard card type
    master_cards = ['2221', '5479', '5100', '5599']
    for i in range(0, 5):
        payment = Payment()
        payment.random.seed(i)

# Generated at 2022-06-14 00:37:39.810776
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    card_type = CardType.VISA
    cn = Payment().credit_card_number(card_type=card_type)
    print("credit card number: "+cn)
    assert (cn[:1]=='4')


# Generated at 2022-06-14 00:37:50.071120
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():

    payment = Payment('en')

    assert len(payment.credit_card_number()) == 16
    card_type = CardType.VISA
    cc_number = payment.credit_card_number(card_type=card_type)
    assert len(cc_number) == 16
    assert CardType(s=cc_number[0]) == card_type
    card_type = CardType.MASTER_CARD
    cc_number = payment.credit_card_number(card_type=card_type)
    assert len(cc_number) == 16
    assert CardType(s=cc_number[0:2]) == card_type
    card_type = CardType.AMERICAN_EXPRESS
    cc_number = payment.credit_card_number(card_type=card_type)
    assert len(cc_number) == 15

# Generated at 2022-06-14 00:37:57.726680
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    global provider
    provider = Payment("en")
    for i in range(1, 10000):
        card_type = 'MASTER_CARD'
        card_number = provider.credit_card_number(card_type)
        print(card_number)
        if not isinstance(card_number, str):
            print("test_Payment_credit_card_number fail")
            sys.exit()
    # Test passed
    print("test_Payment_credit_card_number pass")
    sys.exit()

# Generated at 2022-06-14 00:38:07.962180
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    from random import Random
    from mimesis.providers.payment import Payment
    from mimesis.enums import CardType

    card_type_list = [CardType.VISA,
                      CardType.MASTER_CARD,
                      CardType.AMERICAN_EXPRESS]

    seed = 0
    rnd = Random()
    rnd.seed(seed)

    payment = Payment('en', seed=0)

    for card_type in card_type_list:
        card_number = payment.credit_card_number(card_type=card_type)
        assert len(card_number.replace(' ', '')) == 16
        if card_number[0] == 4:
            assert card_type == card_type_list[0]

# Generated at 2022-06-14 00:38:13.666840
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment(seed=125)
    assert payment.credit_card_number() == '4455 5299 1152 2450'
    assert payment.credit_card_number() == '4067 7844 2009 5201'
    assert payment.credit_card_number() == '4067 7844 2009 5201'
    assert payment.credit_card_number() == '4455 5299 1152 2450'


# Generated at 2022-06-14 00:38:21.469246
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    # First test for all types of credit cards
    for i in range(CardType.__len__()):
        p = Payment()
        card = p.credit_card_number(i)
        assert str(i) == ',' and len(card) == 16, 'Wrong card type or number'
    # Second test for random credit card
    for i in range(100):
        p = Payment()
        card = p.credit_card_number()
        assert len(card) == 16, 'Wrong card type or number'


# Generated at 2022-06-14 00:38:23.522084
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
#assert len(payment.credit_card_number()) == 16
    assert payment.credit_card_number()[0:2] == '41'

# Generated at 2022-06-14 00:38:27.052522
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    card_type = CardType.AMERICAN_EXPRESS
    print("test_Payment_credit_card_number")
    print("Network :", card_type.value)
    print("Card Info :", Payment().credit_card_number(card_type))



# Generated at 2022-06-14 00:38:36.731323
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    card = Payment(seed=123).credit_card_number()
    # Default is CardType.VISA
    assert card == '4444 5259 9127 6599'
    card = Payment(seed=123).credit_card_number(CardType.MASTER_CARD)
    assert card == '5266 4697 9382 2047'
    card = Payment(seed=123).credit_card_number(CardType.AMERICAN_EXPRESS)
    assert card == '3445 865821 86596'

# Generated at 2022-06-14 00:38:53.282960
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    from mimesis.enums import CardType
    from mimesis.enums import Gender
    payment = Payment('en')
    visa = payment.credit_card_number(CardType.VISA)
    master = payment.credit_card_number(CardType.MASTER_CARD)
    american = payment.credit_card_number(CardType.AMERICAN_EXPRESS)
    names = [payment.credit_card_owner(gender=gender)['owner'] for gender in Gender]
    assert isinstance(visa, str)
    assert isinstance(master, str)
    assert isinstance(american, str)
    assert isinstance(names[0], str)

# Generated at 2022-06-14 00:38:56.371625
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    assert payment.credit_card_number(CardType.VISA) in CREDIT_CARD_NETWORKS

# Generated at 2022-06-14 00:39:02.143008
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    card_number = payment.credit_card_number(CardType.VISA)
    print(card_number)
    #check if the generated card number is of 16 digits
    assert len(card_number) == 16
    #check if all the digits of the generated card number are integer
    assert card_number.isdigit()
    #check if the card number is valid
    assert payment.is_valid_credit_card_number(card_number)


# Generated at 2022-06-14 00:39:04.357174
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    str_card = Payment('en').credit_card_number()
    assert isinstance(str_card, str)
    assert re.match(r'(^\d{4}\s\d{4}\s\d{4}\s\d{4}$)', str_card)


# Generated at 2022-06-14 00:39:08.248525
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    result = payment.credit_card_number()
    print(result)
    assert isinstance(result, str)
    assert len(result) == 19


# Generated at 2022-06-14 00:39:11.154537
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    assert Payment('en').credit_card_number() == '4455 5299 1152 2450'


# Generated at 2022-06-14 00:39:14.449903
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment()
    assert re.fullmatch(r'[a-zA-Z0-9]{16,19}', p.credit_card_number())


# Generated at 2022-06-14 00:39:29.214544
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment('en')
    # Test with card_type Visa
    visa_ccn = payment.credit_card_number(card_type = CardType.VISA)
    visa_ccn_valid = re.match(r'^4\d{3} \d{4} \d{4} \d{4}$', visa_ccn)
    assert visa_ccn_valid, 'Visa Credit Card Number is not valid'

    # Test with card_type Master Card
    mc_ccn = payment.credit_card_number(card_type = CardType.MASTER_CARD)

# Generated at 2022-06-14 00:39:36.859900
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment()
    # Check with all CardType possible
    p.credit_card_number(CardType.VISA)
    p.credit_card_number(CardType.MASTER_CARD)
    p.credit_card_number(CardType.AMERICAN_EXPRESS)
    # Try to get with invalid CardType    
    try:
        p.credit_card_number(CardType.DINERS_CLUB)
    except NonEnumerableError:
        # Check if the not implemented card_type is Diners Club
        assert True

# Generated at 2022-06-14 00:39:47.244961
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    # Method credit_card_number of class Payment returns valid Visa card number
    payment = Payment(seed=20190903)
    card_number = payment.credit_card_number(CardType.VISA)
    assert re.match('4\d{15}', card_number)

    # Method credit_card_number of class Payment returns valid MasterCard card number
    payment = Payment(seed=20190903)
    card_number = payment.credit_card_number(CardType.MASTER_CARD)
    assert re.match('5[1-5]\d{14}', card_number)

    # Method credit_card_number of class Payment returns valid American Express card number
    payment = Payment(seed=20190903)
    card_number = payment.credit_card_number(CardType.AMERICAN_EXPRESS)

# Generated at 2022-06-14 00:40:15.058601
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Unit test for method credit_card_number of class Payment"""
    p = Payment()
    
    # Test the presence of spaces
    assert p.credit_card_number().find(' ') != -1
    
    # Test the presence of an expiration date
    assert p.credit_card_number().find('/') != -1

# Generated at 2022-06-14 00:40:20.086435
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    test_card_type = CardType.MASTER_CARD
    p = Payment(seed=324)
    # print(p.credit_card_number(test_card_type))
    assert p.credit_card_number(test_card_type) == '5105 5523 9692 5275'

# Generated at 2022-06-14 00:40:24.888188
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    card_number = Payment('en').credit_card_number(CardType.VISA)
    assert len(card_number) == 19
    assert card_number[0] == '4'
    assert card_number[4] == ' '


# Generated at 2022-06-14 00:40:28.867553
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment()
    print(p.credit_card_number(card_type=CardType.AMERICAN_EXPRESS))

# Generated at 2022-06-14 00:40:36.528057
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment()
    # testing visa numbers
    for i in range(0, 9):
        cc = p.credit_card_number(card_type=CardType.VISA)
        assert cc[0] == "4"
        assert len(cc) == 19
    # testing mastercard numbers
    for i in range(0, 9):
        cc = p.credit_card_number(card_type=CardType.MASTER_CARD)
        assert int(cc[0]) > 1
        assert int(cc[0]) < 5
        assert int(cc[1]) == 2 or int(cc[1]) == 5
        assert len(cc) == 19
    # testing american express numbers

# Generated at 2022-06-14 00:40:40.772872
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    number = payment.credit_card_number()
    print(number)
    assert len(number) == 19


if __name__ == "__main__":
    test_Payment_credit_card_number()

# Generated at 2022-06-14 00:40:45.743922
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment(random_state=1)
    assert payment.credit_card_number() == '4455 5299 1152 2450'


# Generated at 2022-06-14 00:40:51.829957
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    import random
    print("Test Payment_credit_card_number")
    random.seed(1)
    temp = Payment(random=random)
    for i in range(10):
        card_type = temp.random.choice(list(CardType))
        result = temp.credit_card_number(card_type=card_type)
        print(result)


# Generated at 2022-06-14 00:40:57.219869
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
	payment = Payment()
	credit_card_number = payment.credit_card_number(CardType.MASTER_CARD)
	assert isinstance(credit_card_number, str)
	assert len(credit_card_number) == 19
	assert re.match('^[\d ]+$', credit_card_number)


# Generated at 2022-06-14 00:41:02.340624
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment(seed=123)
    # print(payment.credit_card_number())
    assert payment.credit_card_number() == '4455 5299 1152 2450', "This method should return '4455 5299 1152 2450'"