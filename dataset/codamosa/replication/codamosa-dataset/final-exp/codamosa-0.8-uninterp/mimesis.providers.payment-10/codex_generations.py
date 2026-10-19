

# Generated at 2022-06-14 00:36:22.641417
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment()
    for card_type in CardType:
        assert re.match(r'^\d{4} \d{4} \d{4} \d{4}$', p.credit_card_number(card_type))
    assert re.match(r'^\d{4} \d{6} \d{5}$', p.credit_card_number(CardType.AMERICAN_EXPRESS))
    try:
        p.credit_card_number(CardType.VISA_ELECTRON)
        raise TypeError("Argument `card_type` has unknown value")
    except NonEnumerableError:
        pass

# Generated at 2022-06-14 00:36:29.133332
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    import mimesis
    import mimesis.enums as enums
    import mimesis.providers.payment as payment
    import pytest


# Generated at 2022-06-14 00:36:30.127488
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    assert payment.credit_card_number(CardType.VISA) == payment.credit_card_number()

# Generated at 2022-06-14 00:36:36.464176
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    # Setup
    p = Payment(seed=42).credit_card_number()

    # Exercise

    # Verify
    p_expected = "4783 0298 3162 4361"
    assert p == p_expected, "Expected: " + p_expected + " Actual: " + p

    # Cleanup - none necessary


# Generated at 2022-06-14 00:36:41.898831
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Unit test for method credit_card_number of class Payment."""
    payment = Payment('en')
    card_type = CardType.VISA
    numbers = {}
    for i in range(100):
        numbers[payment.credit_card_number(card_type=card_type)] = 1
    assert len(numbers) == 100


# Generated at 2022-06-14 00:36:49.091067
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment('en')
    credit_card_number = payment.credit_card_number()
    credit_card_type = payment.credit_card_network()
    print("\nCredit card number: ", credit_card_number)
    print("Credit card type: ", credit_card_type)
    print("Test1: ", len(credit_card_number) <= 19)
    print("Test2: ", len(credit_card_number) >= 14)
    print("Test3: ", credit_card_type == 'Visa')


# Generated at 2022-06-14 00:36:53.245848
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment()
    assert re.match(r'^\d{4} \d{4} \d{4} \d{4}$', p.credit_card_number())


# Generated at 2022-06-14 00:36:58.206797
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment()
    x = p.credit_card_number()
    print("Test credit_card_number of class Payment: ")
    print("The random visa credit card number is: ", x)
    return True


# Generated at 2022-06-14 00:37:01.223315
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p1 = Payment()
    assert p1.credit_card_number()[0:3] == '560'


# Generated at 2022-06-14 00:37:03.741415
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment()

    assert re.search(r'\d+', p.credit_card_number()) != None

# Generated at 2022-06-14 00:37:15.639996
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment()
    l = []
    for i in range(100):
        l.append(p.credit_card_number())
    for item in l:
        assert len(item)==16 or len(item)==19
        assert item[0]=='4' or item[0]=='5' or item[0]=='3'


# Generated at 2022-06-14 00:37:18.651545
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment=Payment()
    output=payment.credit_card_number()
    print(output)


# Generated at 2022-06-14 00:37:26.993604
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment('en')
    credit_card_number = payment.credit_card_number()
    # credit_card_number = payment.credit_card_number(card_type = CardType.VISA)
    # credit_card_number = payment.credit_card_number(card_type = CardType.MASTER_CARD)
    # credit_card_number = payment.credit_card_number(card_type = CardType.AMERICAN_EXPRESS)
    print(credit_card_number)

if __name__ == "__main__":
    test_Payment_credit_card_number()

# Generated at 2022-06-14 00:37:28.233953
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    pl = Payment()
    print(pl.credit_card_number())


# Generated at 2022-06-14 00:37:36.963236
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
	p = Payment()
	is_visa_card=False
	is_master_card=False
	is_american_express=False
	for i in range(1000):
		card_type = p.credit_card_number()
		if card_type[:4]=="4556":
			is_master_card=True
		elif card_type[:4]=="4559":
			is_master_card=True
		elif card_type[:4]=="4571":
			is_master_card=True
		elif card_type[:4]=="4576":
			is_master_card=True
		elif card_type[:4]=="4213":
			is_master_card=True
	

# Generated at 2022-06-14 00:37:41.576154
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    # generate a random credit card number
    ccn = Payment.credit_card_number()
    assert len(ccn) == 19  # check the length of the ccn
    assert luhn_checksum(ccn[:16]) == ccn[16:]  # check the ccn is valid


# Generated at 2022-06-14 00:37:47.530115
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment()
    for i in range(100):
        assert len(p.credit_card_number(CardType.VISA)) == 19
        assert len(p.credit_card_number(CardType.MASTER_CARD)) == 19
        assert len(p.credit_card_number(CardType.AMERICAN_EXPRESS)) == 18
    try:
        p.credit_card_number(CardType.DISCOVER)
    except NonEnumerableError as e:
        assert str(e) == 'CardType: not enumerable type'



# Generated at 2022-06-14 00:37:53.267975
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment()
    r_num = p.credit_card_number()
    v = re.match(r'\d{4}\s\d{4}\s\d{4}\s\d{4}',r_num)
    assert v.group(0) == r_num


# Generated at 2022-06-14 00:37:56.007522
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
        payment = Payment()
        try:
            payment.credit_card_number('Visa')
        except Exception as e:
            print(e)


# Generated at 2022-06-14 00:38:04.244996
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    # Instantiate
    ps = Payment()

    # To store generated credit card number
    card_number = ""

    # Generate credit card number
    # Check whether it is Visa
    card_number = ps.credit_card_number()
    assert card_number[0] == "4"

    # Generate credit card number
    # Check whether it is MasterCard
    card_number = ps.credit_card_number(CardType.MASTER_CARD)
    assert_card_number = card_number[:2]
    assert_card_number = int(assert_card_number)
    assert assert_card_number in range(2221, 2720) or assert_card_number in range(5100, 5599)

    # Generate credit card number
    # Check whether it is American Express
    card_number = ps.credit_

# Generated at 2022-06-14 00:38:18.788500
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment()
    print("========== Start test case of method credit_card_number of class Payment ==========\n")

    # Test with default value
    print('Test with default value')
    print(p.credit_card_number())
    
    print('\n========== End test case of method credit_card_number of class Payment ==========\n')


# Generated at 2022-06-14 00:38:23.193884
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment(seed=1)
    assert p.credit_card_number() == '4455 5299 1152 2450'
    assert p.credit_card_number(CardType.MASTER_CARD) == '5565 4857 4134 2325'
    assert p.credit_card_number(CardType.AMERICAN_EXPRESS) == '3463 090682 28199'

# Generated at 2022-06-14 00:38:35.818096
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment(seed=1)
    for i in range(1000):
        assert(p.credit_card_number(CardType.VISA)=='4063 9043 5127 9819')
        assert(p.credit_card_number(CardType.MASTER_CARD)=='5202 9102 4060 9729')
        assert(p.credit_card_number(CardType.AMERICAN_EXPRESS)=='3735 368563 84558')
    assert(p.credit_card_number()=='4063 9043 5127 9819')
    try:
        p.credit_card_number(CardType.DISCOVER)
        assert(False)
    except NonEnumerableError:
        assert(True)
    p = Payment(seed=1)

# Generated at 2022-06-14 00:38:45.173363
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    # Test-Data
    tdcn_card_type = [
        CardType.VISA,
        CardType.MASTER_CARD,
        CardType.AMERICAN_EXPRESS,
    ]

    # Initialization
    test = Payment()

    # Test-Run
    for enum in tdcn_card_type:
        for i in range(0, 1000):
            assert test.credit_card_number(enum)

test_Payment_credit_card_number()


# Generated at 2022-06-14 00:38:56.237555
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    # Test Visa
    assert payment.credit_card_number(card_type=CardType.VISA) == '4455 5299 1152 2450'
    # Test MasterCard
    assert payment.credit_card_number(card_type=CardType.MASTER_CARD) == '5100 0349 5123 9100'
    # Test American Express
    assert payment.credit_card_number(card_type=CardType.AMERICAN_EXPRESS) == '3721 5813 686 077'
    # Test NonEnumerableError
    try:
        payment.credit_card_number(card_type=CardType.JCB)
    except NonEnumerableError:
        pass
    else:
        raise AssertionError('Expected NonEnumerableError')

# Generated at 2022-06-14 00:38:59.183981
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment()
    assert re.match(r'\d{4} \d{4} \d{4} \d{4}', p.credit_card_number())

# Generated at 2022-06-14 00:39:04.102234
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    card_type = CardType.AMERICAN_EXPRESS
    payment = Payment('en', seed=0)
    card_number = payment.credit_card_number(card_type)
    assert card_number == '3464 935303 60392'

# Generated at 2022-06-14 00:39:11.097197
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment("en")
    print(p.credit_card_number())
    p = Payment("en")
    print(p.credit_card_number(CardType.MASTER_CARD))
    # assert p.credit_card_number() == 4455 5299 1152 2450, "This is wrong"
    # assert p.credit_card_number(CardType.MASTER_CARD) == 2221 4997 9746 2632, "This is wrong"


# Generated at 2022-06-14 00:39:18.359360
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    # Visa
    assert re.match(r"(\d{4})(\d{4})(\d{4})(\d{4})",
                    Payment.credit_card_number(CardType.VISA))

    # MasterCard
    assert re.match(r"(\d{4})(\d{4})(\d{4})(\d{4})",
                    Payment.credit_card_number(CardType.MASTER_CARD))

    # American Express
    assert re.match(r"(\d{4})(\d{6})(\d{5})",
                    Payment.credit_card_number(CardType.AMERICAN_EXPRESS))

# Generated at 2022-06-14 00:39:24.295122
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment('en')
    for _ in range(100):
        card_number = payment.credit_card_number()
        assert len(card_number) <= 19
        assert len(card_number.replace(' ','')) == 16
        assert card_number[:4] == '4553'

# Generated at 2022-06-14 00:39:54.955254
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment(seed=0)
    enum = CardType.VISA
    assert p.credit_card_number(enum) == "4555 8019 3579 2937"
    assert p.credit_card_number(CardType.AMERICAN_EXPRESS) == "3766 663145 91353"
    assert p.credit_card_number(CardType.MASTER_CARD) == "5176 5324 6885 9704"


# Generated at 2022-06-14 00:40:06.913242
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():

    from mimesis.enums import CardType

    payment = Payment(seed=1234)
    payment.credit_card_number(CardType.VISA)

    assert payment.credit_card_number(CardType.VISA) == '4975 7369 5262 1903'
    assert payment.credit_card_number(CardType.MASTER_CARD) == '5263 1548 4328 3448'
    assert payment.credit_card_number(CardType.AMERICAN_EXPRESS) == '34690767652358'


# Generated at 2022-06-14 00:40:21.397867
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Unit test for method credit_card_number of class Payment."""
    payment = Payment()
    visa1 = payment.credit_card_number(card_type=CardType.VISA)
    visa2 = payment.credit_card_number(card_type=CardType.VISA)
    master1 = payment.credit_card_number(card_type=CardType.MASTER_CARD)
    master2 = payment.credit_card_number(card_type=CardType.MASTER_CARD)
    amex1 = payment.credit_card_number(card_type=CardType.AMERICAN_EXPRESS)
    amex2 = payment.credit_card_number(card_type=CardType.AMERICAN_EXPRESS)

# Generated at 2022-06-14 00:40:32.554329
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    '''
    Function to test method credit_card_number of class Payment
    '''
    payment = Payment()
    card_type = CardType.VISA
    card_number = payment.credit_card_number(card_type)
    assert len(card_number) == 19
    assert card_number[:1] == '4'
    card_type = CardType.MASTER_CARD
    card_number = payment.credit_card_number(card_type)
    assert len(card_number) == 19
    assert card_number[:2] == '51' or card_number[:2] == '55'
    card_type = CardType.AMERICAN_EXPRESS
    card_number = payment.credit_card_number(card_type)
    assert len(card_number) == 17
    assert card_

# Generated at 2022-06-14 00:40:39.400822
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    print(payment.credit_card_number(CardType.VISA))
    print(payment.credit_card_number(CardType.MASTER_CARD))
    print(payment.credit_card_number(CardType.AMERICAN_EXPRESS))


# Generated at 2022-06-14 00:40:44.994983
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment.Meta.name
    m = Payment(seed=123)
    card_type = CardType.VISA
    res = m.credit_card_number(card_type)
    network = CREDIT_CARD_NETWORKS[card_type.value]
    print(f"source.{p}.Payment.credit_card_number(card_type={card_type}) = {res} ({network})")


# Generated at 2022-06-14 00:40:53.374071
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment()
    assert re.fullmatch(r'\d{4} \d{4} \d{4} \d{4}', p.credit_card_number()) == None
    assert re.fullmatch(r'\d{4} \d{4} \d{4} \d{4}', p.credit_card_number(CardType.MASTER_CARD)) == None
    assert re.fullmatch(r'\d{4} \d{6} \d{5}', p.credit_card_number(CardType.AMERICAN_EXPRESS)) == None

# Generated at 2022-06-14 00:40:59.495443
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    # Set data
    card_type = CardType.MASTERCARD

    # Init
    Payment = Payment(seed=568)

    # Execute
    res = Payment.credit_card_number(card_type)

    # Verification
    assert res == '5266 8228 7537 1198'

# Generated at 2022-06-14 00:41:11.131748
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
  # call method credit_card_number
  # parameter card_type = CardType.VISA
  payment = Payment()
  card_type = payment.CardType.VISA.value
  payment.credit_card_number(card_type)
  
  # parameter card_type = CardType.MASTER_CARD
  payment = Payment()
  card_type = payment.CardType.MASTER_CARD.value
  payment.credit_card_number(card_type)
  
  # parameter card_type = CardType.AMERICAN_EXPRESS
  payment = Payment()
  card_type = payment.CardType.AMERICAN_EXPRESS.value
  payment.credit_card_number(card_type)
  
  # parameter card_type = type Int
  payment = Payment()

# Generated at 2022-06-14 00:41:26.418479
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    from mimesis.exceptions import NonEnumerableError
    from mimesis.enums import CardType
    from mimesis.providers.payment import Payment

    p = Payment()
    for i in range(1000):
        assert re.match(r'^\d{4}\s\d{4}\s\d{4}\s\d{4}$', p.credit_card_number())
    assert re.match(r'^\d{4}\s\d{6}\s\d{5}$',
                    p.credit_card_number(card_type=CardType.AMERICAN_EXPRESS))

    p = Payment()