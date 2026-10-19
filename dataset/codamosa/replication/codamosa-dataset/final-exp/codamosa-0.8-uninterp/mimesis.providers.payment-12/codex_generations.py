

# Generated at 2022-06-14 00:36:21.298162
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    visa = payment.credit_card_number(card_type=CardType.VISA)
    assert visa[0] == '4'
    assert len(visa) == 19
    master_card = payment.credit_card_number(card_type=CardType.MASTER_CARD)
    assert master_card[0] == '5'
    assert len(master_card) == 19
    amex = payment.credit_card_number(card_type=CardType.AMERICAN_EXPRESS)
    assert amex[0] == '3'
    assert len(amex) == 17

# Generated at 2022-06-14 00:36:22.502073
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    module = Payment()
    assert len(module.credit_card_number()) == 19

# Generated at 2022-06-14 00:36:26.528443
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    # Initializing the object
    payment = Payment()
    # Testing
    assert payment.credit_card_number(CardType.VISA)
    assert payment.credit_card_number(CardType.MASTER_CARD)
    assert payment.credit_card_number(CardType.AMERICAN_EXPRESS)

# Generated at 2022-06-14 00:36:30.225256
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Test method credit_card_number of class Payment."""

    payment = Payment('en')
    print(payment.credit_card_number())


# Generated at 2022-06-14 00:36:36.737347
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    global payment
    payment = Payment()

    print("\n" + "Unit test for method credit_card_number of class Payment")

    print(payment.credit_card_number(CardType.VISA))
    print(payment.credit_card_number(CardType.MASTER_CARD))
    print(payment.credit_card_number(CardType.AMERICAN_EXPRESS))


# Generated at 2022-06-14 00:36:38.608173
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment()
    p.credit_card_number(CardType.VISA)

# Generated at 2022-06-14 00:36:41.565376
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment()
    assert re.compile(r'\d{16}').match(p.credit_card_number())

# Generated at 2022-06-14 00:36:47.708724
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Test if the credit card number generates is valid"""
    payment = Payment()
    for _ in range(10):
        credit_card = payment.credit_card_number()
        card = []
        for char in credit_card:
            if not char.isspace():
                card.append(char)
        number = ''.join(card)
        assert luhn_checksum(number) == 0

# Generated at 2022-06-14 00:36:56.950347
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    card_type = CardType.MASTER_CARD
    pay = Payment()
    # Test we get the right size 16
    assert len(pay.credit_card_number(card_type))==16
    # Test we get the right format 4xxx xxxx xxxx xxxx
    assert re.search(r'\d{4} \d{4} \d{4} \d{4}',pay.credit_card_number(card_type))


# Generated at 2022-06-14 00:37:05.417224
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment()
    r = p.credit_card_number()
    assert len(r) == 19
    r = p.credit_card_number(CardType.VISA)
    assert len(r) == 19
    r = p.credit_card_number(CardType.MASTER_CARD)
    assert len(r) == 19
    r = p.credit_card_number(CardType.AMERICAN_EXPRESS)
    assert len(r) == 17


# Generated at 2022-06-14 00:37:16.824094
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment()
    # c = CardType.VISA
    c = 'VISA'
    print(c)
    credit_card_number = p.credit_card_number(card_type=c)
    print(credit_card_number)

# Generated at 2022-06-14 00:37:25.003953
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    cc = Payment()

    cc.credit_card_number(cc.CardType.VISA) # VISA Card
    cc.credit_card_number(cc.CardType.MASTER_CARD) # MasterCard
    cc.credit_card_number(cc.CardType.AMERICAN_EXPRESS) # American Express

    # Random
    cc.credit_card_number() # Any card type
    

# Generated at 2022-06-14 00:37:27.941814
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    assert len(payment.credit_card_number()) == 19

# Generated at 2022-06-14 00:37:31.801909
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Unit test for method credit_card_number of class Payment."""

    payment = Payment(seed=12345)
    credit_card_number = payment.credit_card_number()
    assert credit_card_number == '4455 5299 1152 2450'



# Generated at 2022-06-14 00:37:44.394862
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Unit test for method credit_card_number of class Payment"""
    # Define the class
    my_seed = 777
    my_payment = Payment(my_seed)
    # Define the dictionary
    my_dict = {}
    # Extract 10 random credit card numbers
    for _ in range(10):
        # Define the card_type
        card_type = get_random_item(CardType, rnd=my_payment.random)
        # Extract the credit card number
        credit_card_number = my_payment.credit_card_number(card_type=card_type)
        # Store the type and credit card number in the dictionary
        my_key = str(card_type)[-1]
        if my_key not in my_dict:
            my_dict[my_key] = credit_card_number
    #

# Generated at 2022-06-14 00:37:52.482694
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    import mimesis.enums
    for i in range(100):
        if Payment().credit_card_number(mimesis.enums.CardType.VISA) and Payment().credit_card_number(mimesis.enums.CardType.MASTER_CARD) and Payment().credit_card_number(mimesis.enums.CardType.AMERICAN_EXPRESS):
            return True
    return False


# Generated at 2022-06-14 00:37:53.890713
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    assert payment.credit_card_number().startswith('40')

# Generated at 2022-06-14 00:38:02.415389
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
  payment=Payment(seed=1234567890)
  assert(payment.credit_card_number(CardType.AMERICAN_EXPRESS) == '3706 451488 62357')
  assert(payment.credit_card_number() == '4308 1792 3533 2682')
  assert(payment.credit_card_number() == '3779 487110 17888')
  assert(payment.credit_card_number() == '4831 405430 37792')
  assert(payment.credit_card_number(CardType.VISA) == '4308 1792 3533 2682')
  assert(payment.credit_card_number(CardType.MASTER_CARD) == '5308 1792 3533 2682')

# Generated at 2022-06-14 00:38:08.508757
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    assert len(payment.credit_card_number()) == 19
    assert len(payment.credit_card_number(CardType.AMERICAN_EXPRESS)) == 17
    assert len(payment.credit_card_number(CardType.MASTER_CARD)) == 19

# Generated at 2022-06-14 00:38:11.474116
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    pay = Payment(seed=54321)
    card_type = pay.random.choice(CardType)
    assert pay.credit_card_number(card_type) == "4455 5299 1152 2450"

# Generated at 2022-06-14 00:38:20.433003
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    print(payment.credit_card_number())

# Generated at 2022-06-14 00:38:26.981466
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    import random
    from mimesis.enums import CardType
    for _ in range(20):
        _ = Payment('en', random.random()).credit_card_number(CardType.VISA)

# Generated at 2022-06-14 00:38:30.942059
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Unit test for method credit_card_number of class Payment"""
    p = Payment()

    # generate a random number of 16 digits
    print(p.credit_card_number())

# Generated at 2022-06-14 00:38:34.074911
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment(random=Random())
    creditCardNumber = payment.credit_card_number()
    print(creditCardNumber)


# Generated at 2022-06-14 00:38:40.257589
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment('en')
    assert payment.credit_card_number() in ['4455 5299 1152 2450', '4444 5299 1152 2450', '4444 5299 1152 2450', '4444 5299 1152 2450', '4444 5299 1152 2450']


# Generated at 2022-06-14 00:38:45.612734
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()

    for i in range(0, 100):
        if payment.random.randint(0, 1):
            _ = payment.credit_card_number(CardType.VISA)
        else:
            _ = payment.credit_card_number(CardType.MASTER_CARD)

# Generated at 2022-06-14 00:38:57.068429
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """
    Unit test for method credit_card_number of class Payment
    """
    payment_object = Payment()
    # Test the method credit_card_number of class Payment with default parameter
    card_type = payment_object.credit_card_number()
    card_number_regex = '\d{4} \d{4} \d{4} \d{4}'
    assert re.match(card_number_regex, card_type)

    # Test the method credit_card_number of class Payment with CardType.VISA
    card_type = payment_object.credit_card_number(card_type = CardType.VISA)
    card_number_regex = '\d{4} \d{4} \d{4} \d{4}'

# Generated at 2022-06-14 00:39:01.131623
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """ Unit test for method credit_card_number of class Payment"""
    p = Payment()
    assert len(p.credit_card_number()) == 19
    assert p.credit_card_number(CardType.VISA)
    assert p.credit_card_number(CardType.MASTER_CARD)
    assert p.credit_card_number(CardType.AMERICAN_EXPRESS)


# Generated at 2022-06-14 00:39:04.376840
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment()
    print(p.credit_card_number())
    print(p.credit_card_number('visa'))

# Generated at 2022-06-14 00:39:15.237049
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    # test the default value of card_type
    credit_card_number = payment.credit_card_number()
    assert len(credit_card_number) == 19
    assert ' ' in credit_card_number
    # test the value of card_type is Visa
    credit_card_number = payment.credit_card_number(CardType.VISA)
    assert len(credit_card_number) == 19
    assert ' ' in credit_card_number
    assert credit_card_number[0] == '4'
    # test the value of card_type is MasterCard
    credit_card_number = payment.credit_card_number(CardType.MASTER_CARD)
    assert len(credit_card_number) == 19
    assert ' ' in credit_card_number
    assert credit_card_number

# Generated at 2022-06-14 00:39:36.684054
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    assert Payment().credit_card_number(CardType.AMERICAN_EXPRESS) == '3722 369660 90332'
    assert Payment().credit_card_number(CardType.VISA) == '4215 0646 0196 1278'
    assert Payment().credit_card_number(CardType.MASTER_CARD) == '5174 0395 6753 0723'

test_Payment_credit_card_number()

# Generated at 2022-06-14 00:39:38.320561
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    print(payment.credit_card_number(3))


# Generated at 2022-06-14 00:39:51.005561
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    
    """Unit test for method credit_card_number of class Payment."""

    print('\n')
    # for i in CREDIT_CARD_NETWORKS:
    #     card_type=i
    #     print(card_type)
    for i in CREDIT_CARD_NETWORKS:
        card_type=CardType(i)
        print('{}: {}'.format(i,card_type))
    print('\n')
    # print(CardType.VISA)
    # print(CardType.MASTER_CARD)
    # print(CardType.AMERICAN_EXPRESS)
    # print(CardType.DISCOVER)
    # print(CardType.DINER_CLUB)
    # print(CardType.JCB)
    # for i in range(3):
   

# Generated at 2022-06-14 00:39:59.122699
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    # Test for card type VISA
    card_number = Payment().credit_card_number(CardType.VISA)
    print(card_number)
    assert card_number[0] == '4'
    assert len(card_number) > 13
    # Test for card type MASTER_CARD
    card_number = Payment().credit_card_number(CardType.MASTER_CARD)
    print(card_number)
    assert card_number[:2] == '51' or card_number[:2] == '22'
    assert len(card_number) > 13
    # Test for card type AMERICAN_EXPRESS
    card_number = Payment().credit_card_number(CardType.AMERICAN_EXPRESS)
    print(card_number)

# Generated at 2022-06-14 00:40:06.907362
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment(seed=0)
    assert payment.credit_card_number(card_type=None) == '4964 8065 3653 6738'
    assert payment.credit_card_number(card_type=CardType.AMERICAN_EXPRESS) == '3792 062976 69731'
    assert payment.credit_card_number(card_type=CardType.MASTER_CARD) == '5537 6417 4272 8543'
    assert payment.credit_card_number(card_type=CardType.VISA) == '4964 8065 3653 6738'
    try:
        payment.credit_card_number('hello')
    except NonEnumerableError:
        pass


# Generated at 2022-06-14 00:40:16.121311
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    # This is a unit test for method credit_card_number of class Payment
    # Set the seed to make sure the random number is the same
    payment = Payment()
    assert payment.credit_card_number() == '4455 5299 1152 2450'
    payment = Payment(seed=101)
    assert payment.credit_card_number() == '4929 3537 5930 2443'



# Generated at 2022-06-14 00:40:19.327215
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    assert len(Payment().credit_card_number()) == 19
    assert len(Payment().credit_card_number(CardType.AMERICAN_EXPRESS)) == 18

# Generated at 2022-06-14 00:40:24.059199
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Test for method credit_card_number of class Payment"""
    payment = Payment()
    # Test credit_card_number without parameters
    credit_card_number = payment.credit_card_number()
    # Test credit_card_number with parameters
    credit_card_number_with_parameters = payment.credit_card_number(CardType.VISA)
    assert len(credit_card_number) == 19
    assert len(credit_card_number_with_parameters) == 19


# Generated at 2022-06-14 00:40:31.804417
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Test for credit card number method."""
    payment = Payment()
    payment.credit_card_number(CardType.VISA)
    payment.credit_card_number(CardType.MASTER_CARD)
    payment.credit_card_number(CardType.AMERICAN_EXPRESS)
    # payment.credit_card_number(CardType.DINERS_CLUB)
    # payment.credit_card_number(CardType.DISCOVER)

# Generated at 2022-06-14 00:40:43.778663
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    # default test
    credit_card_number = payment.credit_card_number()
    assert len(credit_card_number) == 19 # 16 + 3 spaces
    assert credit_card_number[:1] == "4"
    # test with CardType = CardType.MASTER_CARD
    credit_card_number = payment.credit_card_number(CardType.MASTER_CARD)
    assert len(credit_card_number) == 19 # 16 + 3 spaces
    assert credit_card_number[:1] == "5"
    # test with CardType = CardType.AMERICAN_EXPRESS
    credit_card_number = payment.credit_card_number(CardType.AMERICAN_EXPRESS)
    assert len(credit_card_number) == 17 # 15 + 2 spaces

# Generated at 2022-06-14 00:41:24.898957
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
	# Test CardType.VISA
    print("\nTest CardType.VISA")
    pay = Payment()
    print(pay.credit_card_number())

    # Test CardType.MASTER_CARD
    print("\nTest CardType.MASTER_CARD")
    pay = Payment()
    print(pay.credit_card_number())

    # Test CardType.AMERICAN_EXPRESS
    print("\nTest CardType.AMERICAN_EXPRESS")
    pay = Payment()
    print(pay.credit_card_number())

# Generated at 2022-06-14 00:41:32.976368
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    from mimesis.enums import CardType
    from mimesis.exceptions import NonEnumerableError
    from mimesis.providers.payment import Payment
    payment = Payment()
    try:
        payment.credit_card_number(card_type=CardType.DISCOVER)
        assert False
    except NonEnumerableError:
        assert True
    assert payment.credit_card_number(card_type=CardType.VISA)
    assert payment.credit_card_number(card_type=CardType.MASTER_CARD)
    assert payment.credit_card_number(card_type=CardType.AMERICAN_EXPRESS)

# Generated at 2022-06-14 00:41:36.062650
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    print("\nTest for method credit_card_number of class Payment")
    payment = Payment()
    print(str(payment.credit_card_number()))
    print(str(payment.credit_card_number(card_type=CardType.MASTER_CARD)))
    print(str(payment.credit_card_number(card_type=CardType.AMERICAN_EXPRESS)))
    print(str(payment.credit_card_number(card_type=CardType.VISA)))


# Generated at 2022-06-14 00:41:39.433474
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    # Unit test for method credit_card_number of class Payment
    payment = Payment(seed=0)
    print(payment.credit_card_number())

# Generated at 2022-06-14 00:41:50.037517
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment()
    num_visa = p.credit_card_number()
    num_mc = p.credit_card_number(CardType.MASTER_CARD)
    num_amex = p.credit_card_number(CardType.AMERICAN_EXPRESS)
    print(num_visa)
    print(num_mc)
    print(num_amex)



# Generated at 2022-06-14 00:41:51.307274
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment()
    assert len(p.credit_card_number()) == 19

# Generated at 2022-06-14 00:41:52.961527
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    print(Payment('en').credit_card_number())

# Generated at 2022-06-14 00:41:57.872815
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    provider = Payment('en')
    cc_number = provider.credit_card_number()
    assert re.match(r'\d{4} \d{4} \d{4} \d{4}$', cc_number)
    cc_number = provider.credit_card_number(card_type=CardType.AMERICAN_EXPRESS)
    assert re.match(r'\d{4} \d{6} \d{5}$', cc_number)


# Generated at 2022-06-14 00:42:07.518302
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment('en')
    credit = payment.credit_card_number()
    assert len(credit) == 19
    assert re.match(r'^\d{4} \d{4} \d{4} \d{4}$', credit)
    master = payment.credit_card_number(CardType.MASTER_CARD)
    assert len(master) == 19
    assert re.match(r'^\d{4} \d{4} \d{4} \d{4}$', master)
    amex = payment.credit_card_number(CardType.AMERICAN_EXPRESS)
    assert len(amex) == 17
    assert re.match(r'^\d{4} \d{6} \d{5}$', amex)

    # Test for not implemented

# Generated at 2022-06-14 00:42:19.515179
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    temp_payment = Payment("en")
    CardTypeList = [CardType.AMERICAN_EXPRESS, CardType.MASTER_CARD, CardType.VISA]
    for index in range (1, 100):
        card_type = CardTypeList[index % 3]
        test_card_number = temp_payment.credit_card_number(card_type)
        assert len(test_card_number) in [16, 17, 18, 19]
        if card_type == CardType.AMERICAN_EXPRESS:
            assert test_card_number[:2] == '34' or test_card_number[:2] == '37'