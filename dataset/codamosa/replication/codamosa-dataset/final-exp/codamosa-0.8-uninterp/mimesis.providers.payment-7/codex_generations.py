

# Generated at 2022-06-14 00:36:27.406876
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    c = Payment(seed=12345678)
    assert c.credit_card_number() == '4455 5299 1152 2450'
    assert c.credit_card_number(CardType.VISA) == '4455 5299 1152 2450'
    assert c.credit_card_number(CardType.VISA) == '4024 0071 0200 5771'
    assert c.credit_card_number(CardType.MASTER_CARD) == '2221 0445 4520 0243'
    assert c.credit_card_number(CardType.MASTER_CARD) == '5179 9644 1585 8126'
    assert c.credit_card_number(CardType.AMERICAN_EXPRESS) == '3785 9224 2835 093'

# Generated at 2022-06-14 00:36:36.709842
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment(seed=0)
    assert payment.credit_card_number() == '4349 7795 2562 8974'
    assert payment.credit_card_number(CardType.VISA) == '4349 7795 2562 8974'
    assert payment.credit_card_number(CardType.MASTER_CARD) == '5298 4187 0745 4608'
    assert payment.credit_card_number(CardType.AMERICAN_EXPRESS) == '3732 011492 05359'

# Generated at 2022-06-14 00:36:42.799128
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    import mimesis
    payment = mimesis.Payment()
    number = payment.credit_card_number(card_type=mimesis.CardType.VISA)
    print(number)
    print(payment.credit_card_expiration_date(minimum=16, maximum=25))
    print(payment.cvv())
    owner = payment.credit_card_owner(gender=mimesis.Gender.MALE)
    print(owner)

# Generated at 2022-06-14 00:36:46.608597
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    assert Payment().credit_card_number(CardType.MASTER_CARD) == '5591 5165 3572 4255'
    assert Payment().credit_card_number(CardType.AMERICAN_EXPRESS) == '3721 545696 71490'

# Generated at 2022-06-14 00:37:01.529815
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    test_data = "4242424242424242"
    provider = Payment()
    assert provider.credit_card_number() is not None
    assert provider.credit_card_number().isnumeric() == 1
    assert provider.credit_card_number(CardType.MASTER_CARD) is not None
    assert provider.credit_card_number(CardType.MASTER_CARD).isnumeric() == 1
    assert provider.credit_card_number(CardType.AMERICAN_EXPRESS) is not None
    assert provider.credit_card_number(CardType.AMERICAN_EXPRESS).isnumeric() == 1

    # Test for Visa card type
    assert provider.credit_card_number(CardType.VISA) is not None
    assert provider.credit_card_number(CardType.VISA).isnumeric

# Generated at 2022-06-14 00:37:06.111492
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    print("Test Payment.credit_card_number")
    payment = Payment(seed=123)
    print(payment.credit_card_number())
    print(payment.credit_card_number())
    print(payment.credit_card_number())


# Generated at 2022-06-14 00:37:08.051464
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment()
    print(p.credit_card_number(p.random.choice(list(CardType))))

# Generated at 2022-06-14 00:37:19.799735
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    # Test 1: Visa Card
    assert re.match(r'\d{4} \d{4} \d{4} \d{4}', payment.credit_card_number())
    assert re.match(r'\d{4} \d{4} \d{4} \d{4}', payment.credit_card_number(CardType('visa')))

    # Test 2: Master Card
    assert re.match(r'\d{4} \d{4} \d{4} \d{4}', payment.credit_card_number(CardType('mastercard')))

    # Test 3: American Express
    assert re.match(r'\d{4} \d{6} \d{5}', payment.credit_card_number(CardType('american express')))



# Generated at 2022-06-14 00:37:21.609904
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    Payment(seed=1).credit_card_number() == '4455 5299 1152 2450'


# Generated at 2022-06-14 00:37:27.982225
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    print("Testing method credit_card_number of class Payment")
    payment = Payment()
    card = payment.credit_card_number()
    groups = re.search(r'(\d{4})(\d{4})(\d{4})(\d{4})', card).groups()
    assert len(groups) == 4
    assert groups[0] and groups[1] and groups[2] and groups[3]
    print("  Successful\n")


# Generated at 2022-06-14 00:37:47.647808
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    INSTANCES = [
        Payment(randomize=True), 
        Payment(randomize=False)
    ]
    for instance in INSTANCES:
        assert len(instance.credit_card_number()) == 19
        assert len(instance.credit_card_number(CardType.AMERICAN_EXPRESS)) == 17 
        assert instance.credit_card_number(CardType.MASTER_CARD) != instance.credit_card_number(CardType.MASTER_CARD)
        assert instance.credit_card_number(CardType.VISA) != instance.credit_card_number(CardType.VISA)


# Generated at 2022-06-14 00:37:53.704419
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    number = payment.credit_card_number(CardType.VISA)
    # String start with 4
    assert number[0] == '4'
    # String is 16 characters long and the last digit is even
    assert len(number) == 16
    assert int(number[-1]) % 2 == 0


# Generated at 2022-06-14 00:38:03.156128
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
   # test the case card_type is None
    CardType.MASTER_CARD == CardType.MASTER_CARD
    CardType.VISA == CardType.VISA
    CardType.AMERICAN_EXPRESS == CardType.AMERICAN_EXPRESS
    global count
    count = 0
    global count2
    count2 = 0
    global count3
    count3 = 0
    Payment._Payment__data = None
    Payment(seed=1).__rand = None
    Payment(seed=1)
    Payment(seed=1)
    Payment(seed=1).__seed = 1
    global i
    for i in range(10):
        Payment(seed=1).credit_card_number(card_type=None)

# Generated at 2022-06-14 00:38:10.552711
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    assert (payment.credit_card_number(CardType.VISA)).strip() == '4455 5299 1152 2450'
    assert (payment.credit_card_number(CardType.MASTER_CARD)).strip() == '5527 8697 9738 6776'
    assert (payment.credit_card_number(CardType.AMERICAN_EXPRESS)).strip() == '3768 682033 74946'

# Generated at 2022-06-14 00:38:14.264314
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    idx = 0
    while idx < 10:
        payment = Payment()
        card_number = payment.credit_card_number()
        print('card_number: ', card_number)
        idx += 1


# Generated at 2022-06-14 00:38:17.878688
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    print('TEST: method credit_card_number of class Payment')

    from mimesis.enums import CardType

    c = Payment('en')
    cenn = c.credit_card_number()

    print(cenn)

    if not re.match(r'\d{4} \d{4} \d{4} \d{4}', cenn):
        print('FAIL: credit_card_number did not match the pattern')
        print(cenn)
        print('-'*20)

    cenn = c.credit_card_number(CardType.AMERICAN_EXPRESS)
    print(cenn)


# Generated at 2022-06-14 00:38:22.893049
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Test Function of credit card number creation."""
    # Create a Payment class
    payment = Payment()
    # Generate credit card number
    card = payment.credit_card_number()
    # Check if credit card number is valid
    if not luhn_checksum(card.replace(' ', '')):
        # If not valid stop execution and print error message
        exit('Error generating credit card number')

# Generated at 2022-06-14 00:38:24.297023
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    for i in range(0, 100):
        print(Payment().credit_card_number())


# Generated at 2022-06-14 00:38:25.490160
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    assert len(payment.credit_card_number()) == 19

# Generated at 2022-06-14 00:38:27.003394
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    card_number = Payment.credit_card_number()
    print(card_number)


if __name__ == '__main__':
    test_Payment_credit_card_number()

# Generated at 2022-06-14 00:38:59.330486
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    print(payment.credit_card_number(CardType.VISA))
    print(payment.credit_card_number(CardType.MASTER_CARD))
    print(payment.credit_card_number(CardType.AMERICAN_EXPRESS))


# Generated at 2022-06-14 00:39:04.266171
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    credit_card_number = payment.credit_card_number()
    assert credit_card_number == "4979 8489 3349 6788"
    # Unit test for method credit_card_owner of class Payment


# Generated at 2022-06-14 00:39:09.050621
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Unit test for the function credit_card_number of class Payment"""
    card_type = 'VISA'
    provider_payment = Payment()
    provider_payment.random.seed(66)
    print(provider_payment.credit_card_number(CardType.VISA))


# Generated at 2022-06-14 00:39:11.097030
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    assert len(Payment().credit_card_number()) == 19
    assert len(Payment().credit_card_number(CardType.AMERICAN_EXPRESS)) == 17

# Generated at 2022-06-14 00:39:19.354978
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Unit test for method credit_card_number of class Payment"""
    payment = Payment()

    # Test for method credit_card_number
    credit_card = payment.credit_card_number()
    assert len(credit_card.replace(" ", "")) == 16

    # Test for method credit_card_number with parameter
    credit_card = payment.credit_card_number(CardType.VISA)
    assert len(credit_card.replace(" ", "")) == 16
    credit_card = payment.credit_card_number(CardType.MASTER_CARD)
    assert len(credit_card.replace(" ", "")) == 16
    credit_card = payment.credit_card_number(CardType.AMERICAN_EXPRESS)
    assert len(credit_card.replace(" ", "")) == 15


# Generated at 2022-06-14 00:39:33.212338
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    assert payment.credit_card_number() == '4455 5299 1152 2450'
    assert payment.credit_card_number(CardType.AMERICAN_EXPRESS) == '3743 641055 75535'
    assert payment.credit_card_number(CardType.MASTER_CARD) == '5556 9623 7047 8278'
    assert payment.credit_card_number(CardType.VISA) == '4929 9358 5756 4270'
    #assert payment.credit_card_number(CardType.JCB) == '3569 1732 6202 5585'
    #assert payment.credit_card_number(CardType.DISCOVER) == '6011 5547 8772 0840'
    #assert payment.credit_card_number(CardType.DINERS_CLUB)

# Generated at 2022-06-14 00:39:36.642184
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    cc_number = payment.credit_card_number(CardType.VISA)
    assert re.match('^4\d{3} \d{4} \d{4} \d{4}$', cc_number) is not None


# Generated at 2022-06-14 00:39:40.257400
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    provider = Payment()
    credit_card = provider.credit_card_number(CardType.MASTER_CARD)
    credit_card_type = credit_card[0]
    assert credit_card_type in [str(i) for i in [2, 5]]
    assert len(credit_card) == 19

# Generated at 2022-06-14 00:39:51.513580
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    Payment1 = Payment()
    Payment2 = Payment()
    Payment3 = Payment()
    Payment4 = Payment()
    Payment5 = Payment()
    Payment6 = Payment()
    Payment7 = Payment()
    Payment8 = Payment()

    # test 1
    assert isinstance(Payment1.credit_card_number(),str)
    # test 2
    
    assert re.search(r"(\d{4} )(\d{4} )(\d{4} )(\d{4})",Payment2.credit_card_number())
    # test 3
    assert re.search(r"(\d{4} )(\d{4} )(\d{4} )(\d{4})",Payment3.credit_card_number())
    # test 4

# Generated at 2022-06-14 00:39:55.890721
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    pay = Payment()
    for _ in range(10):
        print(pay.credit_card_number(CardType.MASTER_CARD))
        print(pay.credit_card_number(CardType.AMERICAN_EXPRESS))