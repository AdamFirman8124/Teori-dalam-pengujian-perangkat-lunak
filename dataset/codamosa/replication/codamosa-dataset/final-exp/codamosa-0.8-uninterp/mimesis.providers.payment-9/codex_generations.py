

# Generated at 2022-06-14 00:36:21.468501
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    print(payment.credit_card_number())


# Generated at 2022-06-14 00:36:24.939443
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    import mimesis
    pay = mimesis.Payment()
    assert isinstance(pay.credit_card_number(), str)
    assert type(pay.credit_card_number(card_type = pay.CardType.VISA)) == str

# Generated at 2022-06-14 00:36:40.163179
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment('ru')

    # Test 1.1
    card_type = CardType.AMERICAN_EXPRESS
    output = payment.credit_card_number(card_type)
    print(output)
    # Test 2.1
    card_type = CardType.MASTER_CARD
    output = payment.credit_card_number(card_type)
    print(output)
    # Test 3.1
    card_type = CardType.VISA
    output = payment.credit_card_number(card_type)
    print(output)
    # Test 4.1
    card_type = CardType.VISA
    output = payment.credit_card_number(card_type)
    print(output)


if __name__ == "__main__":
    test_Payment_credit_card_number()

# Generated at 2022-06-14 00:36:46.569061
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    from mimesis.enums import CardType
    from mimesis.providers.payment import Payment
    payment = Payment()
    credit_card_number = payment.credit_card_number(CardType.VISA)
    assert credit_card_number[:4] == '4556'
    assert credit_card_number[-1] == '1'


# Generated at 2022-06-14 00:36:50.093724
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment()
    number = p.credit_card_number()
    assert number is not None


# Generated at 2022-06-14 00:37:04.908337
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """For now, this method will not test Visa number.
    Because, it will automatically generate a random number
    from Visa cards and it is almost impossible to test all possibilities."""
    card_number_visa = Payment().credit_card_number()

    assert len(card_number_visa) == 16
    assert card_number_visa[:1] == '4'

    card_number_master_card = Payment().credit_card_number(
        CardType.MASTER_CARD,
    )
    assert len(card_number_master_card) == 19
    assert card_number_master_card[:2] != '49'
    
    card_number_american_express = Payment().credit_card_number(
        CardType.AMERICAN_EXPRESS,
    )

# Generated at 2022-06-14 00:37:09.519538
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """ Testing the credit_card_number method of Payment class. """
    payment = Payment('ar')
    resultado = payment.credit_card_number(CardType.VISA)
    assert re.match('^(\d{4}\s){3}\d{4}$', resultado)
    assert len(resultado) == 19


# Generated at 2022-06-14 00:37:14.069031
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment(seed=0)
    a = p.credit_card_number(CardType.VISA)
    assert a == '4455 5299 1152 2450'


# Generated at 2022-06-14 00:37:23.995862
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    import random
    result = []
    for _ in range(1000):
        rnd = random.randint(1, 4)
        if rnd == 1 :
            result.append(Payment().credit_card_number(CardType.VISA))
        elif rnd == 2 :
            result.append(Payment().credit_card_number(CardType.MASTER_CARD))
        elif rnd == 3 :
            result.append(Payment().credit_card_number(CardType.AMERICAN_EXPRESS))
        else :
            result.append(Payment().credit_card_number(CardType.DISCOVER))
    assert len(result) == 1000, "The result is not 1000"
    assert isinstance(result[0], str), "The result's type is not string"

# Generated at 2022-06-14 00:37:30.578109
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    for credit_card_number in range(1,6):
        test_card_number = Payment.credit_card_number()
        card_type = re.search(r'^\d{4}',test_card_number)
        assert int(card_type.group()) >= 4000, "invalid visa card number"

# Generated at 2022-06-14 00:37:44.873555
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    pass
    # Test VISA number
    tester = Payment(seed=33)
    result = tester.credit_card_number(CardType.VISA)
    assert result == "4128 1292 8232 7458"

    # Test Master Card number
    tester = Payment(seed=33)
    result = tester.credit_card_number(CardType.MASTER_CARD)
    assert result == "5457 7512 0818 5270"

    # Test American Express number
    tester = Payment(seed=33)
    result = tester.credit_card_number(CardType.AMERICAN_EXPRESS)
    assert result == "34941912847823"

# Generated at 2022-06-14 00:37:53.548741
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Unit test for method credit_card_number of class Payment"""
    print("Testing method credit_card_number() of class Payment")

    objPayment = Payment()  # create an object of Payment class
    cc_number = objPayment.credit_card_number()  # get credit card number from method credit_card_number

    print("\tExpected value of length of credit card number is 16")
    print("\tActual value of length of credit card number is {}".format(len(cc_number)))

    assert len(cc_number) == 16  # check actual value is equal to expected value


# Generated at 2022-06-14 00:37:57.494857
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment(seed=1)
    p.random.seed(1000)
    assert p.credit_card_number() == '4237 7419 3889 7411'
    assert p.credit_card_number() != '1234 5678 9012 3456'



# Generated at 2022-06-14 00:38:06.637444
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Unit test for the method credit_card_number of class Payment."""
    payment = Payment('en')
    card_number = payment.credit_card_number()
    assert len(card_number) == 19
    assert card_number.count(' ') == 3
    assert card_number[4] == ' '
    assert card_number[9] == ' '
    assert card_number[14] == ' '
    assert card_number[0:4] not in ['2221', '2720']
    assert int(card_number[0:4]) not in range(5100, 5599)

# Generated at 2022-06-14 00:38:16.926745
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    # Cases
    # case 1: card_type None -> visa
    result = payment.credit_card_number()
    assert len(result) == 19
    assert result[0] == '4'
    # case 2: card_type CardType.VISA -> visa network
    result = payment.credit_card_number(CardType.VISA)
    assert len(result) == 19
    assert result[0] == '4'
    # case 3: card_type CardType.MASTER_CARD -> mastercard network
    result = payment.credit_card_number(CardType.MASTER_CARD)
    assert len(result) == 19
    # case 4: card_type CardType.AMERICAN_EXPRESS -> american express network

# Generated at 2022-06-14 00:38:20.624860
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment()
    # Test if the generated credit card number is matched with the pattern
    assert re.match(r'(\d{4})(\d{4})(\d{4})(\d{4})', p.credit_card_number()) is not None



# Generated at 2022-06-14 00:38:23.449704
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    t = Payment()
    card_type = CardType.VISA
    t.seed(5)
    card_number = t.credit_card_number(card_type)
    assert card_number == '4040 7665 3113 2067'

# Generated at 2022-06-14 00:38:36.374177
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    # 1st try
    print("\n*** Try 1:")
    card_type = CardType.MASTER_CARD
    x = Payment().credit_card_number(card_type)
    print(x)
    assert type(x) is str
    assert len(x) is 19
    assert x[4] is ' '
    assert x[9] is ' '
    assert x[14] is ' '
    if x[0:1] is '4':
        assert card_type is CardType.VISA
    elif x[0:2] in ['22', '51']:
        assert card_type is CardType.MASTER_CARD
    elif x[0:2] in ['34', '37']:
        assert card_type is CardType.AMERICAN_EXPRESS

# Generated at 2022-06-14 00:38:45.461498
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    # Create object
    payment = Payment('en')
    # Generate credit card number with all CardType
    for card_type in [CardType.VISA, CardType.MASTER_CARD, CardType.AMERICAN_EXPRESS]:
        card_number = payment.credit_card_number(card_type=card_type)
        assert card_number.count(" ") == 3
        assert (card_number.split(" ")[0] in CREDIT_CARD_NETWORKS[card_type])

# Generated at 2022-06-14 00:38:50.672759
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    result_list = []
    for _ in range(1000):
        result_list.append(Payment().credit_card_number())
    card_number_list = [i[0:4] for i in result_list]
    assert all(i in ['4000', '4999', '222', '270'] for i in card_number_list)

# Generated at 2022-06-14 00:39:00.052220
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    print('Payment.credit_card_number()')

    result = Payment(seed=0).credit_card_number()
    print(result)

    assert result == '3591 8969 5733 5466'


# Generated at 2022-06-14 00:39:05.428839
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    payment.credit_card_number(CardType.VISA)
    payment.credit_card_number(CardType.MASTER_CARD)
    payment.credit_card_number(CardType.AMERICAN_EXPRESS)

# Generated at 2022-06-14 00:39:13.731662
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():

    p = Payment()

    # test card type
    assert p.credit_card_number(CardType.VISA)[0] == '4'
    assert p.credit_card_number(CardType.MASTER_CARD)[0] == '5'
    assert p.credit_card_number(CardType.AMERICAN_EXPRESS)[0] == '3'

    # test card number length
    assert len(p.credit_card_number(CardType.VISA)) == 16
    assert len(p.credit_card_number(CardType.MASTER_CARD)) == 16
    assert len(p.credit_card_number(CardType.AMERICAN_EXPRESS)) == 15

    # test with no card type specified
    # assert that it is visa or master

# Generated at 2022-06-14 00:39:16.823474
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    # Create new Payment object
    payment = Payment()

    # Call the tested method
    number = payment.credit_card_number()

    # Check the assertion
    assert re.match(r'\d{4}\s\d{4}\s\d{4}\s\d{4}', number)

# Generated at 2022-06-14 00:39:19.978319
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    card_data = Payment().credit_card_number(CardType.VISA)
    print(card_data)


# Generated at 2022-06-14 00:39:26.596522
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    assert Payment().credit_card_number(CardType.AMERICAN_EXPRESS) == "3716 411273 06492"
    assert Payment().credit_card_number(CardType.MASTER_CARD) == "5404 8444 2523 5105"
    assert Payment().credit_card_number(CardType.VISA) == "4015 4751 8293 8384"

# Generated at 2022-06-14 00:39:39.879280
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    from mimesis.enums import CardType
    # Test for Visa
    visa_card_number = Payment().credit_card_number(CardType.VISA)
    assert len(visa_card_number) == 19
    assert isinstance(visa_card_number, str)
    assert type(visa_card_number) == str

    # Test for Mastercard
    mastercard_number = Payment().credit_card_number(CardType.MASTER_CARD)
    assert len(mastercard_number) == 19
    assert isinstance(mastercard_number, str)
    assert type(mastercard_number) == str

    # Test for American Express
    amex_number = Payment().credit_card_number(CardType.AMERICAN_EXPRESS)
    assert len(amex_number) == 18
    assert isinstance

# Generated at 2022-06-14 00:39:51.483401
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    import time
    import random
    import numpy as np
    random.seed(time.time())
    seed = random.randint(0, 1000)
    print(seed)
    test_data = []
    label_data = []
    
    num_test_cases = 1000
    cc = Payment(seed=seed)
    test_data = np.zeros((num_test_cases, 16))
    for i in range(0, num_test_cases):
        card = cc.credit_card_number(CardType.VISA)
        card = str(card.replace(" ", ""))
        for digit in range(0,16):
            test_data[i][digit] = int(card[digit])
        label_data.append(0)
    for i in range(0, num_test_cases):
        card

# Generated at 2022-06-14 00:39:55.891162
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    card_type = 'AmericanExpress'
    credit_card_number = Payment().credit_card_number(card_type)
    assert credit_card_number.startswith('34') or credit_card_number.startswith('37')

# Generated at 2022-06-14 00:40:00.840250
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    new_Payment = Payment()
    card_number = new_Payment.credit_card_number(CardType.VISA)
    assert len(card_number) == 19
    assert card_number[0] == '4'

# Generated at 2022-06-14 00:40:24.546519
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    # Call the function with CardType.Visa
    result = Payment(seed=100).credit_card_number(CardType.VISA)
    assert result == "4077 7916 5978 4448"

    # Call the function with CardType.MasterCard
    result = Payment(seed=100).credit_card_number(CardType.MASTER_CARD)
    assert result == "5287 2674 2106 1543"

    # Call the function with CardType.AmericanExpress
    result = Payment(seed=100).credit_card_number(CardType.AMERICAN_EXPRESS)
    assert result == "3711 744299 25104"

# Generated at 2022-06-14 00:40:33.193966
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Test for method credit_card_number of class Payment."""
    provider = Payment()
    number = provider.credit_card_number(card_type=CardType.VISA)
    assert re.match(r'\d{16}', number)
    number = provider.credit_card_number(card_type=CardType.MASTER_CARD)
    print(number)
    assert re.match(r'\d{16}', number)
    number = provider.credit_card_number(card_type=CardType.AMERICAN_EXPRESS)
    assert re.match(r'\d{15}', number)

# Generated at 2022-06-14 00:40:38.623837
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    assert payment.credit_card_number(CardType.VISA) == '4554 5299 1152 2450'
    assert payment.credit_card_number(CardType.MASTER_CARD) == '2221 6299 1152 2450'
    assert payment.credit_card_number(CardType.AMERICAN_EXPRESS) == '3445 6299 11524'

# Generated at 2022-06-14 00:40:40.416809
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    pp = Payment()
    print(pp.credit_card_number())

# Generated at 2022-06-14 00:40:45.541962
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    tester = Payment()
    assert(tester.credit_card_number(CardType.VISA))
    assert(tester.credit_card_number(CardType.MASTER_CARD))
    assert(tester.credit_card_number(CardType.AMERICAN_EXPRESS))


# Generated at 2022-06-14 00:40:52.459809
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment(seed=42)
    assert payment.credit_card_number(CardType.VISA) == '4984 1361 1402 7202'
    assert payment.credit_card_number(CardType.MASTER_CARD) == '2377 4249 8157 8076'
    assert payment.credit_card_number(CardType.AMERICAN_EXPRESS) == '3495 438708 43912'


# Generated at 2022-06-14 00:41:03.657866
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    assert payment.credit_card_number(card_type='Visa')
    assert payment.credit_card_number(card_type='AMEX')
    assert payment.credit_card_number(card_type='MasterCard')
    assert payment.credit_card_number()
    assert payment.credit_card_number(card_type='Visa').startswith('4')
    assert payment.credit_card_number(card_type='MasterCard').startswith('5')
    assert payment.credit_card_number(card_type='AMEX').startswith('3')

# Generated at 2022-06-14 00:41:11.016490
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    cc_provider = Payment()
    cc_provider.card_type = 'Visa'
    cc_number = cc_provider.credit_card_number()
    cc_number_prefix = cc_number.split(' ')[0]
    # Check if the first digit of the credit card number is a 4
    assert cc_number_prefix[0] == '4'
    assert len(cc_number) == 19

# Generated at 2022-06-14 00:41:22.926699
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    import random
    import string
    from mimesis.enums import CardType
    from mimesis.providers.payment import Payment

    p = Payment()
    # Arguments
    x = {
        'card_type': CardType.AMERICAN_EXPRESS,
    }
    # Expected output
    o = {
        'card_type': CardType.AMERICAN_EXPRESS,
        'number': 'xxxx xxxx xxxx xxx',
    }
    assert p.credit_card_number(**x) in set(['34', '37'])
    return None

# Generated at 2022-06-14 00:41:28.996927
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    card_type_list = ["VISA", "MASTER_CARD", "AMERICAN_EXPRESS"]
    for card_type in card_type_list:
        prefix = payment.credit_card_number(card_type=card_type)
        print(prefix)


# Generated at 2022-06-14 00:41:57.375202
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    assert re.match(r'^\d{16}$', payment.credit_card_number())
    assert re.match(r'^\d{15}$', payment.credit_card_number(CardType.AMERICAN_EXPRESS))

# Generated at 2022-06-14 00:42:07.218571
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    # Arrange
    Payment = Payment('en')

    # Act
    visa = Payment.credit_card_number()
    mastercard = Payment.credit_card_number(card_type=CardType.MASTER_CARD)
    american_express = Payment.credit_card_number(card_type=CardType.AMERICAN_EXPRESS)

    # Assert
    assert int(visa[0:4]) in range(4000, 5000), 'credit_card_number first 4 digits incorrect.'
    assert int(mastercard[0:4]) in range(2221, 2721) or int(mastercard[0:4]) in range(5100, 5600), 'credit_card_number first 4 digits incorrect.'

# Generated at 2022-06-14 00:42:19.308667
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()

    # Card = 4000....
    assert payment.credit_card_number(CardType.VISA).startswith('4')
    assert payment.credit_card_number(CardType.VISA).startswith('4455')
    
    # Card = 2221.... || 5100....
    assert payment.credit_card_number(CardType.MASTER_CARD).startswith('2')
    assert payment.credit_card_number(CardType.MASTER_CARD).startswith('5')
    
    # Card = 37....
    assert payment.credit_card_number(CardType.AMERICAN_EXPRESS).startswith('37')
    assert payment.credit_card_number(CardType.AMERICAN_EXPRESS).startswith('3444')

    # Check the length of credit card number

# Generated at 2022-06-14 00:42:20.400735
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    print(Payment().credit_card_number(CardType.VISA))

# Generated at 2022-06-14 00:42:31.608572
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Unit test for method credit_card_number of class Payment"""
    
    payment = Payment()
    card = payment.credit_card_number()
    new_card = card.split()
    assert len(new_card[0]) == 4, "The card_number method of Payment class is not behaving as expected"
    assert len(new_card[1]) == 4, "The card_number method of Payment class is not behaving as expected"
    assert len(new_card[2]) == 4, "The card_number method of Payment class is not behaving as expected"
    assert len(new_card[3]) == 4, "The card_number method of Payment class is not behaving as expected"
    
test_Payment_credit_card_number()

# Generated at 2022-06-14 00:42:38.185972
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    tempCard = payment.credit_card_number(CardType.MASTER_CARD)
    ccard = tempCard.split()
    if (ccard[0] != '5555'):
        print("check ccard[0]")
    if (ccard[1] != '5555'):
        print("check ccard[1]")
    if (ccard[2] != '5555'):
        print("check ccard[2]")
    if (ccard[3] != '5555'):
        print("check ccard[3]")
    if (ccard[4] != '5555'):
        print("check ccard[4]")

# Generated at 2022-06-14 00:42:41.417156
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    assert re.match(r'\d{13,16}', '2354674758592584')

# Generated at 2022-06-14 00:42:49.463252
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():

    testUUID = "86afd58f-bcc0-5279-89ac-defb9eb9d1eb"
    testCardType = CardType.VISA
    testCardNumber = "4005 5172 0134 9593"

    # Create a payment object and set its seed number to the testUUID.
    payment = Payment(seed=testUUID)
    assert payment.credit_card_number(testCardType) == testCardNumber

# Generated at 2022-06-14 00:42:52.245709
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment('en')
    for i in [CardType.VISA, CardType.MASTER_CARD, CardType.AMERICAN_EXPRESS]:
        print(payment.credit_card_number(i))

# Generated at 2022-06-14 00:42:56.113575
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    card_number = Payment().credit_card_number()
    assert len(card_number.replace(' ', '')) == 16


# Generated at 2022-06-14 00:44:04.908567
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Unit test for method credit_card_number of class Payment.

    This test will generate 100 different card numbers, and assert the card type.
    """
    payment = Payment()
    
    for _ in range(100):
        number = payment.credit_card_number()
        first_digit = int(number[0])
        if (first_digit == 4):
            assert CardType.VISA
        elif (first_digit == 3):
            assert CardType.AMERICAN_EXPRESS
        elif ((first_digit == 2) or (first_digit == 5)):
            assert CardType.MASTER_CARD
        else:
            return False
    
    return True
    

if __name__ == '__main__':
    print(test_Payment_credit_card_number())

# Generated at 2022-06-14 00:44:13.389425
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():

    def test_visa():
        p = Payment()
        for i in range(1, 100):
            assert p.credit_card_number(CardType.VISA)[0:1] == '4'

    def test_mastercard():
        p = Payment()
        for i in range(1, 100):
            assert p.credit_card_number(CardType.MASTER_CARD)[0:2] == '52' or \
                   p.credit_card_number(CardType.MASTER_CARD)[0:2] == '51'

    def test_amex():
        p = Payment()

# Generated at 2022-06-14 00:44:15.565370
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    ccnum = payment.credit_card_number()
    print(ccnum)

# Generated at 2022-06-14 00:44:25.823061
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """
    Test method credit_card_number of class Payment
    :return: bool (test success)
    """
    card_types = [CardType.VISA, CardType.MASTER_CARD, CardType.AMERICAN_EXPRESS]
    for card_type in card_types:
        payment = Payment(seed=0)
        card_number = payment.credit_card_number(card_type)
        if card_type == CardType.VISA and card_number != '4455 5299 1152 2450':
            return False
        elif card_type == CardType.MASTER_CARD and card_number != '5423 9574 1446 4840':
            return False
        elif card_type == CardType.AMERICAN_EXPRESS and card_number != '3427 994319 65948':
            return

# Generated at 2022-06-14 00:44:36.916195
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """ Unit test for method credit_card_number of class Payment """
    payment = Payment(seed=123456789)
    print('Unit test for method credit_card_number of class Payment')
    print('2. credit card type')
    credit_card_type = "Visa"
    credit_card_number = payment.credit_card_number(card_type=credit_card_type)
    print('credit_card_type =', credit_card_type)
    print('credit_card_number =', credit_card_number)
    print('3. credit card number')
    credit_card_number = payment.credit_card_number(card_type="MasterCard")
    print('credit_card_number =', credit_card_number)
    print('4. credit card number')
    credit_card_number = payment.credit_

# Generated at 2022-06-14 00:44:40.489667
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    print("Testing Payment.credit_card_number()")
    payment = Payment()
    assert payment.credit_card_number() == '4455 5299 1152 2450'
    assert payment.credit_card_number(CardType.MASTER_CARD) == '2221 8784 1255 0705'
    assert payment.credit_card_number(CardType.AMERICAN_EXPRESS) == '3785 706568 99610'

# Generated at 2022-06-14 00:44:51.289237
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    '''
    This function is used to test the method credit_card_number of class Payment
    :return: None
    '''
    from mimesis.enums import CardType
    from mimesis.data import CREDIT_CARD_NETWORKS

    payment = Payment('zh')

    card_network = payment.credit_card_network()
    print(card_network)

    card_type = CardType.VISA
    card_number = payment.credit_card_number(card_type)
    print(card_type, card_number)

    card_type = CardType.MASTER_CARD
    card_number = payment.credit_card_number(card_type)
    print(card_type, card_number)

    card_type = CardType.AMERICAN_EXPRESS

# Generated at 2022-06-14 00:44:54.308067
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():

    from mimesis.enums import CardType

    card_type = get_random_item(CardType, rnd=random)
    print(card_type)

    payment = Payment(seed=101)
    print(payment.credit_card_number(card_type))



# Generated at 2022-06-14 00:45:00.654484
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Test whether method credit_card_number returns valid credit card number."""
    seed = 0
    payment = Payment('en', seed=seed)
    card_type = CardType.MASTER_CARD
    master_card_number = payment.credit_card_number(card_type)
    assert master_card_number in payment.providers

# Generated at 2022-06-14 00:45:13.565204
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    import random  # doctest: +SKIP
    from mimesis.enums import CardType  # doctest: +SKIP

    r = random.Random()  # doctest: +SKIP
    r.seed(42)  # doctest: +SKIP

    p = Payment(seed=r.getrandbits(32))  # doctest: +SKIP
    i = 0
    err = 0
    for _ in range(0, 100):    # doctest: +SKIP
        c = p.credit_card_number(card_type=CardType.VISA)  # doctest: +SKIP
        if not c[0] == '4':  # doctest: +SKIP
            err += 1
        if not len(c) == 19:  # doctest: +SKIP
            err += 1
