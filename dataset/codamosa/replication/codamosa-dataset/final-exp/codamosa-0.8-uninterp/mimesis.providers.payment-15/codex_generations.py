

# Generated at 2022-06-14 00:36:27.728609
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    # Test case 1
    Payment_test1 = Payment('en')
    print(Payment_test1.credit_card_number())
    print(Payment_test1.credit_card_number())

    # Test case 2
    Payment_test2 = Payment('en')
    print(Payment_test2.credit_card_number(CardType.VISA))

    # Test case 3
    Payment_test3 = Payment('en')
    print(Payment_test3.credit_card_number(CardType.MASTER_CARD))

    # Test case 4
    Payment_test4 = Payment('en')
    print(Payment_test4.credit_card_number(CardType.AMERICAN_EXPRESS))

    # Test case 5

# Generated at 2022-06-14 00:36:32.004478
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    creditCardNum = Payment().credit_card_number()

    assert len(creditCardNum) == 19

    newCreditCardNum = creditCardNum.replace(' ', '')

    assert len(newCreditCardNum) == 16

# Generated at 2022-06-14 00:36:41.100583
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Test method credit_card_number of class Payment."""
    payment = Payment()
    assert payment.credit_card_number().__len__() == 19
    assert payment.credit_card_number(
        CardType.VISA).__len__() == 19
    assert payment.credit_card_number(
        CardType.MASTER_CARD).__len__() == 19
    assert payment.credit_card_number(
        CardType.AMERICAN_EXPRESS).__len__() == 17

# Generated at 2022-06-14 00:36:50.677668
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    from mimesis.enums import CardType
    from mimesis.providers.payment import Payment
    p = Payment()
    visa = p.credit_card_number(CardType.VISA)
    print(visa)
    master_card = p.credit_card_number(CardType.MASTER_CARD)
    print(master_card)
    american_express = p.credit_card_number(CardType.AMERICAN_EXPRESS)
    print(american_express)
    try:
        p.credit_card_number("MasterCard")
    except NonEnumerableError as e:
        print("Expected failure")


# Generated at 2022-06-14 00:37:03.831147
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Test Payment class's method credit_card_number."""
    p = Payment()
    results_card_type = [CardType.VISA,
                         CardType.MASTER_CARD,
                         CardType.AMERICAN_EXPRESS]

    card_visa = p.credit_card_number(CardType.VISA)
    assert int(card_visa[0:1]) == 4
    assert int(card_visa[0:2]) >= 40
    assert int(card_visa[0:2]) <= 49
    assert int(card_visa[0:5]) >= 40000
    assert int(card_visa[0:5]) <= 49999

    card_master_card = p.credit_card_number(CardType.MASTER_CARD)

# Generated at 2022-06-14 00:37:07.997863
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Test the method credit_card_number of class Payment."""
    for _ in range(100):
        card_number = Payment().credit_card_number()
        assert Payment().luhn_checksum(card_number[:-1]) == card_number[-1]

# Generated at 2022-06-14 00:37:13.779006
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    assert payment.credit_card_number() in [
        '4123 5908 1805 4934',
        '4989 4956 1498 8126',
        '4716 0285 7588 8900',
    ]



# Generated at 2022-06-14 00:37:20.002838
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    'Test if credit card type follows the enum type specified'
    p = Payment('en')
    assert p.credit_card_number(CardType.VISA)[0] == '4'
    assert p.credit_card_number(CardType.MASTER_CARD)[0] == '5'
    assert p.credit_card_number(CardType.AMERICAN_EXPRESS)[0] == '3'

# Generated at 2022-06-14 00:37:24.825610
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    test_Payment = Payment(seed=123)
    print(test_Payment.credit_card_number(CardType.VISA))
    print(test_Payment.credit_card_number(CardType.MASTER_CARD))
    print(test_Payment.credit_card_number(CardType.AMERICAN_EXPRESS))

# Generated at 2022-06-14 00:37:35.605406
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    #test if the input is valid
    card_number = Payment().credit_card_number(CardType.VISA)
    print(type(card_number))
    print(card_number)
    # print(card_number[0])
    # print(luhn_checksum(card_number))
    # print(type(card_number))
    # print(type(luhn_checksum(card_number)))
    # print(card_number+luhn_checksum(card_number))
    # print(type(int(card_number+luhn_checksum(card_number))))
    #print(isinstance(int(card_number), int()))
    assert isinstance(card_number, str)
    print("\nPass")



# Generated at 2022-06-14 00:37:43.953557
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    assert isinstance(payment.credit_card_number(), str)
    assert len(payment.credit_card_number()) == 19


# Generated at 2022-06-14 00:37:54.589781
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():

    print("\nTest method \"credit_card_number\", class Payment")

    # CardType is Visa
    upper_credit_card_number = Payment()
    print(upper_credit_card_number.credit_card_number())

    # CardType is Visa
    upper_credit_card_number = Payment(CardType.VISA)
    print(upper_credit_card_number.credit_card_number())

    # CardType is MasterCard
    upper_credit_card_number = Payment(CardType.MASTER_CARD)
    print(upper_credit_card_number.credit_card_number())

    # CardType is AmericanExpress
    upper_credit_card_number = Payment(CardType.AMERICAN_EXPRESS)
    print(upper_credit_card_number.credit_card_number())



# Generated at 2022-06-14 00:37:56.539819
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
  print()
  payment = Payment()
  for i in range(2):
    print(payment.credit_card_number())

# Generated at 2022-06-14 00:37:59.866701
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():

    from random import seed, randint
    from mimesis.enums import CardType

    seed(randint(0, 100000))

    payment = Payment('en')
    print("Card Number: ", payment.credit_card_number())

# Generated at 2022-06-14 00:38:04.009806
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    pp = Payment()
    # Test that the method generates a card number in the correct format
    assert pp.credit_card_number() == '4514 6087 4690 7111'



# Generated at 2022-06-14 00:38:08.204129
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment(seed=0)
    card = payment.credit_card_number(CardType.VISA)
    assert card == "4018 8381 2066 8019"

# Generated at 2022-06-14 00:38:20.372187
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Test method credit_card_number of class Payment"""
    payment = Payment(seed=1234)
    print('Test credit_card_number: ', payment.credit_card_number())
    print('Test credit_card_number: ', payment.credit_card_number())
    print('Test credit_card_number: ', payment.credit_card_number())
    print('Test credit_card_number: ', payment.credit_card_number())
    print('Test credit_card_number: ', payment.credit_card_number())
    print('Test credit_card_number: ', payment.credit_card_number())
    print('Test credit_card_number: ', payment.credit_card_number())
    print('Test credit_card_number: ', payment.credit_card_number())

# Generated at 2022-06-14 00:38:32.512469
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment(random_provider=None)
    card_type = CardType.VISA
    res = payment.credit_card_number(card_type)
    res_list = res.split(' ')

# Generated at 2022-06-14 00:38:40.398462
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    b = Payment('en')
    assert re.match(r'(\d{4})(\d{4})(\d{4})(\d{4})', b.credit_card_number())
    assert re.match(r'(\d{4})(\d{6})(\d{5})', b.credit_card_number(CardType.AMERICAN_EXPRESS))


# Generated at 2022-06-14 00:38:44.039179
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    # Set seed for the generator
    payment = Payment()
    payment.seed(1)
    # Generate a random credit card number
    card_number = payment.credit_card_number(card_type=CardType.VISA)
    # Check card_number is initialized correctly
    assert card_number == '4050 4817 0030 7842'

# Generated at 2022-06-14 00:39:00.538849
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment('en')
    card_number = p.credit_card_number()
    assert(len(card_number)==19)

# Generated at 2022-06-14 00:39:09.709326
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    # Case 1
    from mimesis.enums import CardType
    payment = Payment('en')
    result = payment.credit_card_number(CardType.AMERICAN_EXPRESS)
    assert(len(result)) == (19)

    # Case 2
    payment = Payment('en')
    result = payment.credit_card_number(CardType.MASTER_CARD)
    assert(len(result)) == (19)

    assert(len(payment.credit_card_number())) == (19)

# Generated at 2022-06-14 00:39:16.891735
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Test method credit_card_number of class Payment."""
    payment = Payment()
    # Testing card type VISA.
    visa_card_number = payment.credit_card_number(CardType.VISA)
    assert visa_card_number[0] == '4'
    assert luhn_checksum(visa_card_number[:-1]) == visa_card_number[-1]
    # Testing card type MASTER_CARD.
    master_card_number = payment.credit_card_number(CardType.MASTER_CARD)
    assert master_card_number[0] in ('2', '5')
    assert luhn_checksum(master_card_number[:-1]) == master_card_number[-1]
    # Testing card type AMERICAN_EXPRESS.
    american_express_

# Generated at 2022-06-14 00:39:24.018583
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    # Ensure that all card_type works correctly
    card_type_set = set()
    for i in range(0, 100):
        card = Payment().credit_card_number()
        card_type = CardType(card[0])
        card_type_set.add(card_type)
    assert card_type_set == set(CardType)
    

# Generated at 2022-06-14 00:39:29.340553
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()

    card = 0
    for _ in range(10000):
        card = payment.credit_card_number()
        if card != "": # check card not null
            break

    assert card != "", "card can not be null"


# Generated at 2022-06-14 00:39:39.879998
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    P = Payment(seed=777)
    print("The unit test for method credit_card_number of class Payment")
    '''
    l_CardType = [CardType.VISA, CardType.MASTER_CARD, CardType.AMERICAN_EXPRESS]
    n = random.randint(0, len(l_CardType))
    card_type = l_CardType[n]
    '''
    # pass
    card_type = CardType.VISA
    print("CardType : ", card_type)
    print("CardNumber : ", P.credit_card_number(card_type=card_type))
    print("-"*20)

    # fail
    card_type = CardType.MAESTRO
    print("CardType : ", card_type)

# Generated at 2022-06-14 00:39:51.482610
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    from mimesis.enums import CardType
    import random
    import string
    random.seed(0)

# Generated at 2022-06-14 00:39:54.778979
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    card_type = CardType.MASTER_CARD
    pay = Payment()
    res = pay.credit_card_number(card_type)
    print(res)

# Generated at 2022-06-14 00:40:02.051143
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """
    Test method credit_card_number of class Payment

    """
    card_types = [CardType.VISA, CardType.MASTER_CARD, CardType.AMERICAN_EXPRESS]
    for card_type in card_types:
        card = Payment().credit_card_number(card_type)
        assert (card is not None) or (card is not "")

# Generated at 2022-06-14 00:40:09.701962
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment(seed=3)
    assert payment.credit_card_number(CardType.VISA) == '4927 3998 7076 6664'
    assert payment.credit_card_number(CardType.MASTER_CARD) == '5274 3125 1768 3064'
    assert payment.credit_card_number(CardType.AMERICAN_EXPRESS) == '3456 760951 06904'

# Generated at 2022-06-14 00:40:45.411394
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    credit_card_number = payment.credit_card_number(CardType.VISA)
    regex = re.compile(r'(\d{4})(\d{4})(\d{4})(\d{4})')
    assert regex.search(credit_card_number[0]).groups() != None
    assert int(credit_card_number[0][0]) == 4
