

# Generated at 2022-06-14 00:36:27.730825
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Test credit_card_number from Payment class."""
    from random_tests import RandomTestCase
    from random_tests.contrib.payment import Payment

    r = RandomTestCase()
    payment = Payment(seed=100)

    assert payment.credit_card_number() == '4464 2393 0413 9696'
    assert payment.credit_card_number(CardType.VISA) == '4464 2393 0413 9696'
    assert payment.credit_card_number(CardType.MASTER_CARD) == '5202 9098 1471 2674'
    assert payment.credit_card_number(CardType.AMERICAN_EXPRESS) == '3776 763106 35864'


# Generated at 2022-06-14 00:36:41.962783
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    tmp = Payment('en')
    res = tmp.credit_card_number(CardType.VISA)
    assert res is not None
    assert re.match(r'\d{4}\s\d{4}\s\d{4}\s\d{4}', res) is not None

    res = tmp.credit_card_number(CardType.MASTER_CARD)
    assert res is not None
    assert re.match(r'\d{4}\s\d{4}\s\d{4}\s\d{4}', res) is not None

    res = tmp.credit_card_number(CardType.AMERICAN_EXPRESS)
    assert res is not None
    assert re.match(r'\d{4}\s\d{6}\s\d{5}', res) is not None

# Generated at 2022-06-14 00:36:47.897348
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """
    Unit test for the method credit_card_number of class Payment
    """
    x = Payment()
    ccn = x.credit_card_number()
    ccn = ccn.split()
    ccn = "".join(ccn)
    assert int(ccn[0]) == 4 or int(ccn[0]) == 5, "Error with the credit card number"


# Generated at 2022-06-14 00:36:51.005247
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    from mimesis.enums import CardType

    payment = Payment()
    credit_card_number = payment.credit_card_number(card_type=CardType.VISA)

    print(credit_card_number)
    assert re.match(r'[4]{4} \d{4} \d{4} \d{4}', credit_card_number)


# Generated at 2022-06-14 00:36:59.808884
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Unit test for method credit_card_number of class Payment"""
    test_list = [
        #Correct output
        CardType.VISA,
        CardType.MASTER_CARD,
        CardType.AMERICAN_EXPRESS
    ]

    # Test funcitons:
    payment = Payment()
    
    count = 1
    for item in test_list:
        print("Test", count, ":", item)
        print(payment.credit_card_number(CardType[item]))
        count += 1

# Generated at 2022-06-14 00:37:10.109117
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    credit_card = Payment(seed=42)
    n1 = credit_card.credit_card_number(CardType.AMERICAN_EXPRESS)
    n2 = credit_card.credit_card_number(CardType.AMERICAN_EXPRESS)
    n3 = credit_card.credit_card_number(CardType.AMERICAN_EXPRESS)
    n4 = credit_card.credit_card_number(CardType.AMERICAN_EXPRESS)
    n5 = credit_card.credit_card_number(CardType.AMERICAN_EXPRESS)

    assert n1 == '3459 758231 46830'
    assert n2 == '3422 467995 15336'
    assert n3 == '3744 844396 49547'
    assert n4 == '3715 927511 41877'


# Generated at 2022-06-14 00:37:13.218326
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    #Test when card type is VISA
    assert payment.credit_card_number(CardType.VISA) == '4455 5299 1152 2450'
    #Test when card type is MASTER_CARD
    assert payment.credit_card_number(CardType.MASTER_CARD) == '2221 1800 2710 0090'
    #Test when card type is AMERICAN_EXPRESS
    assert payment.credit_card_number(CardType.AMERICAN_EXPRESS) == '3736 3578 3868 464'


# Generated at 2022-06-14 00:37:22.224275
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    #Expected output
    #TestCase #1: 4455 5299 1152 2450
    #TestCase #2: 5373 1048 7376 2621
    #TestCase #3: 3474 3311 9584 546

    payment = Payment()
    payment.seed(1234)
    assert payment.credit_card_number()=="4455 5299 1152 2450"
    payment.seed(1235)
    assert payment.credit_card_number(CardType.MASTER_CARD)=="5373 1048 7376 2621"
    payment.seed(1236)
    assert payment.credit_card_number(CardType.AMERICAN_EXPRESS)=="3474 3311 9584 54"

# Generated at 2022-06-14 00:37:31.257692
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    import random

    # Create an instance of Payment
    pay = Payment()

    for i in range(0, 100):
        random_card_type = random.choice(list(CardType))
        # random_card_type = 'Visa'
        # print(random_card_type)
        card_number = pay.credit_card_number(random_card_type)
        # print(card_number)
        # regex = re.compile(r'(\d{4}).*(\d{4}).*(\d{4}).*(\d{4})')
        regex = re.compile(r'(\d{4}) (\d{4}) (\d{4}) (\d{4})')
        groups = regex.search(card_number).groups()
        card = ''.join(groups)
        #

# Generated at 2022-06-14 00:37:42.002769
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """
    Test if the credit card type is "VISA" and lenght is 16, return True
    Test if the credit card type is "MASTER_CARD" and lenght is 16, return True
    Test if the credit card type is "AMERICAN_EXPRESS", return False
    """
    payment = Payment()

    assert len(payment.credit_card_number(
        CardType.VISA)) == 16, "The credit card type is VISA and lenght is 16"
    assert len(payment.credit_card_number(
        CardType.MASTER_CARD)) == 16, \
        "The credit card type is MASTER_CARD and lenght is 16"

# Generated at 2022-06-14 00:37:53.655251
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment()
    p.credit_card_number()

# Generated at 2022-06-14 00:37:56.845891
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    print("\nUnit test for method credit_card_number of class Payment")
    p = Payment()
    print("Credit_card_number : "+str(p.credit_card_number()))


# Generated at 2022-06-14 00:38:03.732630
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment(seed=0)

    # Visa
    assert p.credit_card_number() == '4088 5982 1455 7697'

    # MasterCard
    assert p.credit_card_number() == '5465 0585 9199 5646'

    # American Express
    assert p.credit_card_number() == '3745 229975 34757'

# Generated at 2022-06-14 00:38:04.343028
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    pass

# Generated at 2022-06-14 00:38:13.942890
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment(seed=0)
    assert payment.credit_card_number() == '4148 4749 6515 9995'
    assert payment.credit_card_number() == '4555 5299 1152 2450'
    assert payment.credit_card_number(CardType.VISA) == '4372 9104 6193 3451'
    assert payment.credit_card_number(CardType.MASTER_CARD) == '5183 5688 7054 0657'
    assert payment.credit_card_number(CardType.AMERICAN_EXPRESS) == '3498 948696 66741'


# Generated at 2022-06-14 00:38:18.144467
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p_test = Payment()
    cc_test = p_test.credit_card_number()
    print(cc_test)

    assert len(cc_test.replace(" ", "")) == 16


# Generated at 2022-06-14 00:38:26.330241
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    res1 = Payment().credit_card_number()
    res2 = Payment().credit_card_number(card_type=CardType.VISA)
    res3 = Payment().credit_card_number(card_type=CardType.AMERICAN_EXPRESS)
    res4 = Payment().credit_card_number(card_type=CardType.MASTER_CARD)
    assert len(res1) == 16
    assert len(res2) == 16
    assert len(res3) == 15
    assert len(res4) == 16

# Generated at 2022-06-14 00:38:33.649325
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    assert payment.credit_card_number()
    assert payment.credit_card_number(card_type = CardType.VISA)
    assert payment.credit_card_number(card_type = CardType.MASTER_CARD)
    assert payment.credit_card_number(card_type = CardType.AMERICAN_EXPRESS)


# Generated at 2022-06-14 00:38:46.379091
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    import random
    import re
    from mimesis.enums import CardType

    # test_case 1
    card_type = CardType.VISA
    credit_card_number = Payment('en', random.randint(0,1000)).credit_card_number(card_type)
    credit_card_regex = re.compile('^4[\d]{3}(-| )[\d]{4}(-| )[\d]{4}(-| )[\d]{4}$')
    assert credit_card_regex.search(credit_card_number) is not None

    # test_case 2
    card_type = CardType.MASTER_CARD
    credit_card_number = Payment('en', random.randint(0,1000)).credit_card_number(card_type)
    credit

# Generated at 2022-06-14 00:38:54.271191
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    card_numbers = [payment.credit_card_number(CardType.AMERICAN_EXPRESS) for _ in range(100)]
    card_numbers.extend([payment.credit_card_number(CardType.VISA) for _ in range(100)])
    card_numbers.extend([payment.credit_card_number(CardType.MASTER_CARD) for _ in range(100)])
    for card_number in card_numbers:
        assert all(card_number[i] != card_number[i+1] for i in range(3))

# Generated at 2022-06-14 00:39:22.336905
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    print("Method credit_card_number of class Payment")
    p = Payment(seed = 1)
    card_number = p.credit_card_number(CardType.VISA)
    print("Credit card number is : "+ card_number)
    print("---------------------------")


# Generated at 2022-06-14 00:39:29.793247
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    pm = Payment('zh')
    # Visa
    print(pm.credit_card_number(CardType.VISA))
    # MasterCard
    print(pm.credit_card_number(CardType.MASTER_CARD))
    # AmericanExpress
    print(pm.credit_card_number(CardType.AMERICAN_EXPRESS))
    # Default: Visa
    print(pm.credit_card_number())



# Generated at 2022-06-14 00:39:39.879626
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    provider = Payment(seed=0)
    credit_card_number = provider.credit_card_number()
    assert credit_card_number == '4040 5682 4113 7548'

    print(credit_card_number)
    credit_card_number = provider.credit_card_number(CardType.VISA)
    assert credit_card_number == '4455 5299 1152 2450'

    print(credit_card_number)
    credit_card_number = provider.credit_card_number(CardType.MASTER_CARD)
    assert credit_card_number == '5178 6700 9827 9851'

    print(credit_card_number)
    credit_card_number = provider.credit_card_number(CardType.AMERICAN_EXPRESS)

# Generated at 2022-06-14 00:39:44.417676
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    #TODO
    #def credit_card_number(self, card_type: Optional[CardType] = None) -> str:
    return 0;

# Generated at 2022-06-14 00:39:50.276722
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment("en")
    value = payment.credit_card_number()
    assert value.count(" ") == 3
    value = payment.credit_card_number(CardType.AMERICAN_EXPRESS)
    assert value.count(" ") == 2
    assert value.count("-") == 0
    assert value.count("-") == 0
    assert int(value[:2]) in [34, 37] & value[0] == '3'

# Generated at 2022-06-14 00:39:53.934421
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    assert len(Payment().credit_card_number()) == 16


# Generated at 2022-06-14 00:40:06.912880
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    # Test CardType.MASTER_CARD
    card_number = payment.credit_card_number(CardType.MASTER_CARD)
    credit_card_network = payment.credit_card_network()
    assert credit_card_network == 'MasterCard'
    prefix = card_number[:2]
    assert prefix == '51' or prefix == '52' or prefix == '53' or prefix == '54' or prefix == '55'
    # Test CardType.VISA
    card_number = payment.credit_card_number(CardType.VISA)
    credit_card_network = payment.credit_card_network()
    assert credit_card_network == 'Visa'
    prefix = card_number[:1]
    assert prefix == '4'
    # Test CardType.AMERICAN

# Generated at 2022-06-14 00:40:19.939342
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
   provider = Payment(seed=0)
   list_visa = [
       provider.credit_card_number(CardType.VISA) for x in range(0,10)]
   list_master = [
       provider.credit_card_number(CardType.MASTER_CARD) for x in range(0,10)]
   list_amex = [
       provider.credit_card_number(CardType.AMERICAN_EXPRESS) for x in range(0,10)]


# Generated at 2022-06-14 00:40:25.924319
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    P = Payment()
    assert P.credit_card_number() != None
    assert P.credit_card_number(CardType.VISA) != None
    assert P.credit_card_number(CardType.MASTER_CARD) != None
    assert P.credit_card_number(CardType.AMERICAN_EXPRESS) != None

# Generated at 2022-06-14 00:40:30.837106
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Test a Payment's method credit_card_number."""
    payment = Payment()
    result = payment.credit_card_number(CardType.AMERICAN_EXPRESS)
    assert result[0] == '3'
    assert result[1] == '4' or result[1] == '7'
    assert len(result.replace(' ', '')) == 15
