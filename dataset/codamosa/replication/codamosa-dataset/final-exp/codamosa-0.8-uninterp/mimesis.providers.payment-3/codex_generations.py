

# Generated at 2022-06-14 00:36:23.406524
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    assert payment.credit_card_number(card_type=CardType.VISA) == '4455 5299 1152 2450'
    assert payment.credit_card_number(card_type=CardType.MASTER_CARD) == '5455 9299 3452 2450'
    assert payment.credit_card_number(card_type=CardType.AMERICAN_EXPRESS) == '3424 0069 0705 154'

# Generated at 2022-06-14 00:36:24.965876
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment('en')
    for i in range(1,10):
        print(p.credit_card_number())

# Generated at 2022-06-14 00:36:40.227601
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    # Check networks
    payment = Payment()
    card_networks = list(CardType)
    for _ in range(10):
        cc = payment.credit_card_number()
        #print(cc)
        assert cc[0] == '4'
    for _ in range(10):
        cc = payment.credit_card_number(CardType.MASTER_CARD)
        #print(cc)
        assert cc[0] == '5'
    for _ in range(10):
        cc = payment.credit_card_number(CardType.AMERICAN_EXPRESS)
        #print(cc)
        assert cc[0] == '3'
        assert ' ' not in cc[1:5]

    # Check length
    for _ in range(10):
        cc = payment.credit_card_number()
       

# Generated at 2022-06-14 00:36:50.318790
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Test for method credit_card_number of class Payment."""
    from mimesis.enums import CardType
    from mimesis.exceptions import NonEnumerableError
    from mimesis.typing import Enum
    payment = Payment()
    assert payment.credit_card_number() is not None
    assert payment.credit_card_number(CardType.VISA) is not None
    assert payment.credit_card_number(CardType.MASTER_CARD) is not None
    assert payment.credit_card_number(CardType.AMERICAN_EXPRESS) is not None
    assert payment.credit_card_number(CardType.DISCOVER) is not None
    assert isinstance(payment.credit_card_number(CardType.VISA), str)

# Generated at 2022-06-14 00:36:56.308598
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    # Instantiate a Payment object with a seed
    payment = Payment(seed=500)
    # Generate a credit card number
    card_number = payment.credit_card_number(CardType.MASTER_CARD)
    assert card_number == "5241 1293 2610 7491"


# Generated at 2022-06-14 00:37:08.099151
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    if __name__ == '__main__':
        import pytest
        # First way to create payment object
        payment = Payment()
        # Second way to create payment object
        # from mimesis.providers import Payment
        # payment = Payment()

        # Generate Visa card number
        number = payment.credit_card_number(CardType.VISA)

        # Generate MasterCard number
        number = payment.credit_card_number(CardType.MASTER_CARD)

        # Generate American Express number
        number = payment.credit_card_number(CardType.AMERICAN_EXPRESS)

        with pytest.raises(NonEnumerableError):
            payment.credit_card_number(CardType.VISA)


# Generated at 2022-06-14 00:37:16.620516
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    assert payment.credit_card_number(CardType.VISA) == '4455 5299 1152 2450'
    assert payment.credit_card_number(CardType.MASTER_CARD) == '5281 5854 9097 9875'
    assert payment.credit_card_number(CardType.AMERICAN_EXPRESS) == '3410 6704 89027 0'


# Generated at 2022-06-14 00:37:23.139572
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    test_enum = CardType.VISA
    test_object = Payment()
    test_number = test_object.credit_card_number(test_enum)
    assert len(test_number.split()[1]) == 16
    assert len(test_number.split()) == 4
    assert test_number.split()[0][0] == '4'
    assert test_number.split()[0][1] == '4'
    assert test_number.split()[0][2] == '4'
    assert test_number.split()[0][3] != '4'


# Generated at 2022-06-14 00:37:28.110209
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment()
    assert len(p.credit_card_number().split(' ')) == 4
    

# Generated at 2022-06-14 00:37:36.878649
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    instance = Payment()
    assert re.match(r'(\d{4})(\d{4})(\d{4})(\d{4})',instance.credit_card_number(),re.DOTALL)!=None
    assert re.match(r'(\d{4})(\d{6})(\d{5})',instance.credit_card_number(CardType.AMERICAN_EXPRESS),re.DOTALL)!=None
    assert re.match(r'(\d{4})(\d{4})(\d{4})(\d{4})',instance.credit_card_number(CardType.MASTER_CARD),re.DOTALL)!=None

# Generated at 2022-06-14 00:38:00.162629
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
        from mimesis.__version__ import __version__
        from mimesis.providers.payment import Payment
        for i in range(1):
          print("Starting test Payment_credit_card_number")
          p = Payment('en')
          obj = p.credit_card_number(card_type = None)
          assert obj is not None
          print("Finishing test Payment_credit_card_number")
          assert isinstance(obj, str)
          assert len(obj) > 14
          assert len(obj) <= 19
          assert obj[0:1] in [str(1),str(2),str(3),str(4),str(5)]
          assert " " in obj
          assert obj[5:6] == " "
          assert obj[9:10] == " "
          assert obj[13:14] == " "

# Generated at 2022-06-14 00:38:03.422010
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment()
    assert p.credit_card_number(CardType.VISA)
    assert p.credit_card_number(CardType.MASTER_CARD)
    assert p.credit_card_number(CardType.AMERICAN_EXPRESS)
    assert p.credit_card_number()

# Generated at 2022-06-14 00:38:08.809530
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    from mimesis.enums import CardType
    from mimesis.providers.payment import Payment
    p = Payment()
    for _ in range(10):
        print(p.credit_card_number(CardType.AMERICAN_EXPRESS))


# Generated at 2022-06-14 00:38:17.397190
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    ''' Test the method credit_card_number in class Payment '''
    import random
    from mimesis.enums import CardType
    from mimesis.exceptions import NonEnumerableError
    # Test 1
    print("\nTest 1")
    random.seed(1)
    payment = Payment()
    print("Credit card number: ", payment.credit_card_number())
    print()
    # Test 2
    print("\nTest 2")
    random.seed(1)
    payment = Payment()
    print("Credit card number: ", payment.credit_card_number(CardType.AMERICAN_EXPRESS))
    print()
    # Test 3
    print("\nTest 3")

# Generated at 2022-06-14 00:38:20.387941
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    credit_card_number = Payment(random.Random()).credit_card_number()

    assert len(credit_card_number) == 19

    # Unit test for method credit_card_network of class Payment

# Generated at 2022-06-14 00:38:27.169261
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    print("\nMethod credit_card_number of class Payment")
    print("\nVISA")
    for i in range(5):
        print("{} -> {}".format(i + 1, Payment().credit_card_number(CardType.VISA)))

    print("\nMASTER_CARD")
    for i in range(5):
        print("{} -> {}".format(i + 1, Payment().credit_card_number(CardType.MASTER_CARD)))

    print("\nAMERICAN_EXPRESS")

# Generated at 2022-06-14 00:38:38.791226
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    from mimesis.providers.payment import Payment
    from mimesis.enums import CardType
    payment = Payment()
    card_type = CardType.AMERICAN_EXPRESS
    card = payment.credit_card_number(card_type)
    # Check that the number of digits is correct
    assert len(card) == 19
    # Check that the first two digits are correct
    assert card[0:2] in ['34', '37']
    # Check whether the number is valid according to the Luhn algorithm
    assert payment.validate_credit_card_number(card) is True


# Generated at 2022-06-14 00:38:44.385327
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Test method credit_card_number.
    """
    test_case = {
        CardType.VISA: '4455 5299 1152 2450',
        CardType.AMERICAN_EXPRESS: '3733 011470 7916',
        CardType.MASTER_CARD: '5546 3449 0882 2366',
    }
    payment = Payment('en', seed=12345)
    for k, v in test_case.items():
        assert payment.credit_card_number(card_type=k) == v

# Generated at 2022-06-14 00:38:55.548457
# Unit test for method credit_card_number of class Payment

# Generated at 2022-06-14 00:39:02.713841
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment('ru')
    card_number_1 = p.credit_card_number()
    card_number_2 = p.credit_card_number(card_type=CardType.VISA)
    card_number_3 = p.credit_card_number(card_type=CardType.MASTER_CARD)
    card_number_4 = p.credit_card_number(card_type=CardType.AMERICAN_EXPRESS)
    assert len(card_number_1) == 19
    assert len(card_number_2) == 19
    assert len(card_number_3) == 19
    assert len(card_number_4) == 17

# Generated at 2022-06-14 00:39:29.675960
# Unit test for method credit_card_number of class Payment

# Generated at 2022-06-14 00:39:30.766549
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment()
    print(p.credit_card_number())

# Generated at 2022-06-14 00:39:33.730754
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment('en')
    credit_card_number = payment.credit_card_number(CardType.MASTER_CARD)
    assert len(credit_card_number) == 19


# Generated at 2022-06-14 00:39:38.181416
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment('en')
    t = payment.credit_card_number(CardType.MASTER_CARD)
    assert(type(t) is str)
    assert(len(t.replace(' ', '')) == 16)
    assert(t.split()[0][0] == '2' or t.split()[0] == '5')



# Generated at 2022-06-14 00:39:40.368150
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    number = payment.credit_card_number()
    assert number != payment.credit_card_number()
    assert int(number[0]) in range(4, 5)

# Generated at 2022-06-14 00:39:51.568913
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    # Unit test for method credit_card_number of class Payment
    class TestCreditCardNumber:
        def test_card_type_is_None(self):
            payment = Payment()
            card_number = payment.credit_card_number()
            assert len(card_number) == 19

    class TestCardType:
        def test_card_type_is_CardType_VISA(self):
            payment = Payment()
            card_number = payment.credit_card_number(CardType.VISA)
            assert card_number[0:4] == '4XXX'

        def test_card_type_is_CardType_MASTER_CARD(self):
            payment = Payment()
            card_number = payment.credit_card_number(CardType.MASTER_CARD)

# Generated at 2022-06-14 00:39:55.893813
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment()
    assert p.credit_card_number(CardType.VISA).startswith('4')
    assert p.credit_card_number(CardType.MASTER_CARD).startswith('2')
    assert p.credit_card_number(CardType.AMERICAN_EXPRESS).startswith('3')
# End of unit test

# Generated at 2022-06-14 00:40:06.907153
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    seed = 100
    random.seed(seed)
    payment = Payment(seed)
    print(payment.credit_card_number())
    print(payment.credit_card_number())
    print(payment.credit_card_number())
    print(payment.credit_card_number())
    print(payment.credit_card_number())
    print(payment.credit_card_number())

test_Payment_credit_card_number()

# Generated at 2022-06-14 00:40:11.124268
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    card_type = CardType.VISA
    payment = Payment()
    credit_card_number = payment.credit_card_number(card_type)
    assert credit_card_number.startswith('4')

# Generated at 2022-06-14 00:40:14.962951
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment(seed=4)
    assert payment.credit_card_number()=='4099 3665 9660 6171'
    assert payment.credit_card_number(CardType.MASTER_CARD)=='5390 4849 6890 9093'
    assert payment.credit_card_number(CardType.AMERICAN_EXPRESS)=='3729 599335 9'
    

# Generated at 2022-06-14 00:40:52.002698
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    card_number = '4427 5512 3595 1234'
    assert payment.credit_card_number(card_type=CardType.VISA) == card_number
    card_number = '5299 1152 2450 8052'
    assert payment.credit_card_number(card_type=CardType.MASTER_CARD) == card_number
    card_number = '3722 6912 1453 730'
    assert payment.credit_card_number(card_type=CardType.AMERICAN_EXPRESS) == card_number

# Generated at 2022-06-14 00:41:00.144633
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    assert '1234 5678 1234 5678' == Payment().credit_card_number(
        CardType.VISA)
    assert '5123 4567 8901 2346' == Payment().credit_card_number(
        CardType.MASTER_CARD)
    assert '3791 2345 6789 145' == Payment().credit_card_number(
        CardType.AMERICAN_EXPRESS)

# Generated at 2022-06-14 00:41:10.227677
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    list_ = ['Visa', 'MasterCard', 'AmericanExpress']
    raw = Payment()
    for i in list_:
        card = raw.credit_card_number(i)
        num = card.replace(' ', '')
        check_sum = num[-1]
        assert str(int(check_sum)) == check_sum, "Нет контрольной суммы"
        assert len(num) == 16, "Неверная длина карточки"



# Generated at 2022-06-14 00:41:12.062749
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Unit test for method credit_card_number of class Payment."""
    payment = Payment()
    # Unit test for method credit_card_number of class Payment with
    # non-default argument
    card_number = payment.credit_card_number(CardType.AMERICAN_EXPRESS)
    print(card_number)


# Generated at 2022-06-14 00:41:16.473628
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment()
    assert len(p.credit_card_number()) == 19
test_Payment_credit_card_number()


# Generated at 2022-06-14 00:41:30.161716
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    # MASTER_CARD
    credit_card_number = Payment().credit_card_number(CardType.MASTER_CARD)
    assert re.search(r'\d{3}', credit_card_number) is not None
    assert re.search(r'\d{4}', credit_card_number) is not None
    # VISA
    credit_card_number = Payment().credit_card_number(CardType.VISA)
    assert re.search(r'\d{3}', credit_card_number) is not None
    assert re.search(r'\d{4}', credit_card_number) is not None
    # AMERICAN_EXPRESS
    credit_card_number = Payment().credit_card_number(CardType.AMERICAN_EXPRESS)

# Generated at 2022-06-14 00:41:37.753334
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    # create an instance of class Payment
    pay = Payment()
    type_ = CardType.MASTER_CARD
    # call method credit_card_number
    result = pay.credit_card_number(card_type=type_)
    # assert the result
    assert(len(result) == 19)
    card_type = result[0]
    assert(card_type == '5')

# Generated at 2022-06-14 00:41:40.409454
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    assert payment.credit_card_number()

# Generated at 2022-06-14 00:41:53.887673
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Unit test method Payment.credit_card_number

        Test the method Payment.credit_card_number five times,
        with and without parameter.

    :return:
    """
    import random

    random.seed(12345)

    for i in range(0, 5):
        seed = random.randint(1, 1000000)

        p = Payment(seed)

        n1 = p.credit_card_number()
        n2 = p.credit_card_number(CardType.MASTER_CARD)
        n3 = p.credit_card_number(CardType.AMERICAN_EXPRESS)

        print('Test number:', i + 1, 'Seed:', seed)
        print(n1)
        print(n2)
        print(n3)
        print()


# Generated at 2022-06-14 00:41:56.351654
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    Payment('ru').credit_card_number()
    Payment('ru', seed=1234).credit_card_number(CardType.MASTER_CARD)