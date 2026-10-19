

# Generated at 2022-06-14 00:36:24.823945
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    print(payment.credit_card_number(card_type=CardType.MASTER_CARD))
    print(payment.credit_card_number(card_type=CardType.VISA))
    print(payment.credit_card_number(card_type=CardType.AMERICAN_EXPRESS))
    print(payment.credit_card_number())

# Generated at 2022-06-14 00:36:36.759073
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number(): # pragma: no cover
    payment = Payment()
    assert re.search(r'^\d{16}$', payment.credit_card_number())
    assert re.search(r'^\d{15}$', payment.credit_card_number(CardType.AMERICAN_EXPRESS))
    try:
        payment.credit_card_number(CardType.DINERS_CLUB)
        assert False
    except NonEnumerableError as e:
        assert str(e) == 'Value of CardType.DINERS_CLUB is not enumerable'



# Generated at 2022-06-14 00:36:41.283104
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    i=0
    while i<10000:
        a=Payment()
        print(a.credit_card_number())
        i=i+1
if __name__ == '__main__':
    test_Payment_credit_card_number()

# Generated at 2022-06-14 00:36:46.891671
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    instance = Payment()
    instance.random.seed(42)
    testing_result = instance.credit_card_number()
    expected_result = "4455 5299 1152 2450"
    assert testing_result == expected_result

if __name__ == '__main__':
    test_Payment_credit_card_number()

# Generated at 2022-06-14 00:37:01.853644
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    from mimesis.enums import CardType
    mm = Payment()
    # Test condition : card_type == None
    list_expect_a = ['Visa', 'MasterCard', 'AmericanExpress']
    # Test condition : card_type == CardType
    list_expect_b = ['Visa', 'MasterCard', 'AmericanExpress']
    # Test condition : card_type not in CardType
    invalid_card_type = 'invalid_card_type'

    # Unit test cases
    card_number_a = mm.credit_card_number()
    assert card_number_a.split(' ')[0] in list_expect_a
    

# Generated at 2022-06-14 00:37:11.941562
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    card_type = CardType.AMERICAN_EXPRESS

    payment.random.seed(12)
    number = payment.credit_card_number(card_type=card_type)
    assert len(number) == 17
    assert number == '3793 4564147 81464'

    payment.random.seed(12)
    number = payment.random.choice(['34', '37'])
    assert len(number) == 2

    payment.random.seed(12)
    number = str(payment.random.randint(100, 999))
    assert len(number) == 3
    assert number == '793'

    payment.random.seed(12)
    number = str(payment.random.choice(['4564', '4563']))
    assert len(number) == 4

# Generated at 2022-06-14 00:37:20.387090
# Unit test for method credit_card_number of class Payment

# Generated at 2022-06-14 00:37:22.421816
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    card = payment.credit_card_number()
    print(card)
    assert len(card) == 19


# Generated at 2022-06-14 00:37:31.391513
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    print('Testing Payment class - credit_card_number method')
    credit_card_number_visa = Payment.credit_card_number(CardType.VISA)
    print('\tVisa credit card number = \'' + credit_card_number_visa + '\'')
    assert credit_card_number_visa[:1] == '4'
    assert len(credit_card_number_visa) == 19
    credit_card_number_mastercard = Payment.credit_card_number(CardType.MASTER_CARD)
    print('\tMasterCard credit card number = \'' + credit_card_number_mastercard + '\'')
    assert len(credit_card_number_mastercard) == 19

# Generated at 2022-06-14 00:37:37.578441
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    for i in range(100):
        assert Payment().credit_card_number(
                card_type=Payment().credit_card_network()
            ) == Payment().credit_card_number(
                card_type=CardType.VISA
            )



# Generated at 2022-06-14 00:37:57.052692
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment('en')
    assert payment.credit_card_number(CardType.VISA)
    assert payment.credit_card_number(CardType.MASTER_CARD)
    assert payment.credit_card_number(CardType.AMERICAN_EXPRESS)
    try:
        payment.credit_card_number(CardType.UNION_PAY)
    except NonEnumerableError:
        pass

# Generated at 2022-06-14 00:38:05.783797
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    print("credit_card_number >>>", payment.credit_card_expiration_date())
    print("credit_card_number >>>", payment.credit_card_number())
    print("credit_card_number >>>", payment.credit_card_number(CardType.VISA))
    print("credit_card_number >>>", payment.credit_card_number(CardType.MASTER_CARD))
    print("credit_card_number >>>", payment.credit_card_number(CardType.AMERICAN_EXPRESS))


# Generated at 2022-06-14 00:38:09.672504
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    pym = Payment('en')
    assert pym.credit_card_number(CardType.VISA)

# Generated at 2022-06-14 00:38:12.633835
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    card=Payment()
    card_type=CardType.AMERICAN_EXPRESS
    print(card.credit_card_number(card_type))


# Generated at 2022-06-14 00:38:17.425353
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment(seed=42)
    assert payment.credit_card_number(card_type=CardType.VISA) == '4455 5299 1152 2450'


# Generated at 2022-06-14 00:38:22.183138
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    Payment.register(region='RU')
    p = Payment('RU')
    card_number = p.credit_card_number(CardType.VISA)
    assert len(card_number.replace(' ', '')) == 16
    assert card_number[0] == '4'
    print('test_Payment_credit_card_number ok!')


# Generated at 2022-06-14 00:38:30.813423
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """test_Payment_credit_card_number(card_type: Optional[CardType] = None) -> str."""
    payment = Payment()
    # test VISA
    assert payment.credit_card_number(card_type=CardType.VISA).startswith('4')
    # test MASTER_CARD
    assert payment.credit_card_number(card_type=CardType.MASTER_CARD).startswith('5')
    # test AMERICAN_EXPRESS
    assert payment.credit_card_number(card_type=CardType.AMERICAN_EXPRESS).startswith('3')

# Generated at 2022-06-14 00:38:42.281495
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """
    Unit test for method credit_card_number of class Payment.
    :return: None
    """
    p = Payment()
    p.credit_card_number()
    p.credit_card_number(CardType.AMERICAN_EXPRESS)
    p.credit_card_number(CardType.MASTER_CARD)
    p.credit_card_number(CardType.VISA)
    try:
        p.credit_card_number('unknown_card')
    except NonEnumerableError:
        print('Unit test for method credit_card_number of class Payment is Passed!')



# Generated at 2022-06-14 00:38:52.260739
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    # Initialize test object
    provider = Payment(seed=1223)

    # Visa
    card_type = CardType.VISA
    assert provider.credit_card_number(card_type) == '4930 8269 5293 1522'

    # MasterCard
    card_type = CardType.MASTER_CARD
    assert provider.credit_card_number(card_type) == '5496 7657 6261 8518'

    # American Express
    card_type = CardType.AMERICAN_EXPRESS
    assert provider.credit_card_number(card_type) == '3790 01610 01516 2'


# Generated at 2022-06-14 00:38:56.934232
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    card_types = {
        # mimesis.enums.CardType.VISA:
        'visa':'4066 5386 3539 4889',
        # mimesis.enums.CardType.MASTER_CARD:
        'mastercard':'2245 8607 7047 8636',
        # mimesis.enums.CardType.AMERICAN_EXPRESS:
        'american_express':'3497 846584 91474',
    }
    p = Payment()
    for card_type, value in card_types.items():
        assert p.credit_card_number(card_type=getattr(CardType,card_type)) == value


# Generated at 2022-06-14 00:39:37.374770
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Test method credit_card_number of class Payment"""
    payment = Payment('en')
    assert payment.credit_card_number(CardType.VISA) == '4349 7706 5663 6452'
    assert payment.credit_card_number(CardType.MASTER_CARD) == '5100 1025 6419 6884'
    assert payment.credit_card_number(CardType.AMERICAN_EXPRESS) == '3736 939726 60934'

    try:
        payment.credit_card_number(CardType.DISCOVER)
    except Exception as e:
        assert str(e) == 'CardType.DISCOVER is not a valid CardType'
    except:
        assert 1 == 2
    else:
        assert 2 == 1

# Generated at 2022-06-14 00:39:40.579980
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    cardType = 'Visa'
    creditCardNumber = Payment(seed=23).credit_card_number(CardType.VISA)
    print(cardType, 'Card Number : ', creditCardNumber)
    assert creditCardNumber == '4951 1792 8175 7865'



# Generated at 2022-06-14 00:39:46.256133
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    print(payment.credit_card_number(CardType.VISA))
    print(payment.credit_card_number(CardType.MASTER_CARD))
    print(payment.credit_card_number(CardType.AMERICAN_EXPRESS))



# Generated at 2022-06-14 00:39:51.039066
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():  # noqa
    payment = Payment(seed=12345678)
    for _ in range(10):
        number = payment.credit_card_number()
        assert re.match(r'\d{4}\s\d{4}\s\d{4}\s\d{4}', number) is not None
        assert luhn_checksum(number.replace(' ', '')) == 0

# Generated at 2022-06-14 00:39:57.520992
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    from mimesis.enums import CardType
    payment = Payment()
    for card_type in CardType:
        credit_card_number = payment.credit_card_number(card_type)
        assert credit_card_number.replace(' ', '').isnumeric()
    try:
        payment.credit_card_number('test')
    except:
        pass


# Generated at 2022-06-14 00:39:59.655572
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    pay = Payment()
    card = pay.credit_card_number()
    print(card)


# Generated at 2022-06-14 00:40:06.912812
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    result = Payment().credit_card_number(CardType.VISA)
    if result[4:5] == ' ':
        print("Unit test for method credit_card_number of class Payment - Success")
    else:
        print("Unit test for method credit_card_number of class Payment - Failed")
    return


# Generated at 2022-06-14 00:40:11.551612
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment()
    # print(p.credit_card_number())
    assert re.match(r"\d{4} \d{4} \d{4} \d{4}", p.credit_card_number())

# Generated at 2022-06-14 00:40:17.733596
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    credit_card_number = payment.credit_card_number()
    if (len(credit_card_number) > 16):
        print("error: credit_card_number is too long!")
    if (credit_card_number[0] != '4'):
        print("error: credit_card_number doesn't start with 4!")

# Generated at 2022-06-14 00:40:22.788424
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment()
    assert len(p.credit_card_number()) == 19
    assert p.credit_card_number()[4] == ' '
    assert p.credit_card_number()[9] == ' '
    assert p.credit_card_number()[14] == ' '
    assert not p.credit_card_number(CardType.AMERICAN_EXPRESS)[16].isalpha()
    assert len(p.credit_card_number(CardType.AMERICAN_EXPRESS)) == 17