

# Generated at 2022-06-14 00:36:26.498094
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    visa_card_number = Payment().credit_card_number(CardType.VISA)
    assert(len(visa_card_number) == 19)
    assert(visa_card_number[0:4] == '4999')
    assert(visa_card_number[15:19] == '8652')

    master_card_number = Payment().credit_card_number(CardType.MASTER_CARD)
    assert(len(master_card_number) == 19)
    assert((master_card_number[0:4] == '2221') or (master_card_number[0:4] == '5999'))
    assert(master_card_number[15:19] == '8792')


# Generated at 2022-06-14 00:36:31.414163
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Unit test for method credit_card_number of class Payment."""
    p = Payment(seed=100)
    card_number = p.credit_card_number()
    assert card_number == '4327 2825 5833 7389'


# Generated at 2022-06-14 00:36:35.589367
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    card_number = payment.credit_card_number(card_type=CardType.VISA)
    assert card_number.startswith("4")
    assert len(card_number) == 19

# Generated at 2022-06-14 00:36:48.009987
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    # Initialize class Payment
    payment = Payment()
    creditCards = {}
    for card_type in CardType:
        creditCards[card_type] = set()

    # Check credit card number of length 16
    for i in range(100):
        card_type = get_random_item(CardType, rnd=payment.random)
        creditCards[card_type].add(payment.credit_card_number(card_type))
    for c in [CardType.VISA, CardType.MASTER_CARD]:
        assert len(creditCards[c]) == 100
    assert len(creditCards[CardType.AMERICAN_EXPRESS]) == 100
    try:
        payment.credit_card_number(CardType.DISCOVER)
        assert False
    except NonEnumerableError:
        assert True

# Generated at 2022-06-14 00:36:57.013991
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    payment.seed(0)
    card_num_not_visa = payment.credit_card_number(CardType.MASTER_CARD)
    card_num_visa = payment.credit_card_number(CardType.VISA)
    assert card_num_not_visa[:2] != '42'
    assert card_num_visa[:2] == '42'
    print(payment.credit_card_number())

# Generated at 2022-06-14 00:37:09.436450
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    # Create test case for method credit_card_number
    test = {
        'card_type': CardType.VISA,
        'credit_card_number': '4455 5299 1152 2450',
        'cvv': 224,
        'expiration_date': '03/19',
        'owner': 'Erin Mays'
    }
    payment = Payment()

    # Generate the credit card number
    card_number = payment.credit_card_number(test['card_type'])

    # Generate the cvv
    cvv = payment.cvv()

    # Generate the expiration_date
    expiration_date = payment.credit_card_expiration_date()

    # Generate the owner
    owner = payment.credit_card_owner()

    # Generate the owner name

# Generated at 2022-06-14 00:37:13.612166
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment('en')
    card_type = payment.random.choice(list(CardType))
    assert payment.credit_card_number(card_type)

# Generated at 2022-06-14 00:37:23.197949
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    from mimesis.typing import CardType
    p = Payment()
    assert re.match(r'\d{4}\s\d{4}\s\d{4}\s\d{4}',
                    p.credit_card_number(CardType.VISA))
    assert re.match(r'\d{4}\s\d{4}\s\d{4}\s\d{4}',
                    p.credit_card_number(CardType.MASTER_CARD))
    assert re.match(r'\d{4}\s\d{6}\s\d{5}',
                    p.credit_card_number(CardType.AMERICAN_EXPRESS))


# Generated at 2022-06-14 00:37:35.795244
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """
    Test for Payment.credit_card_number() function
    """
    # Numbers
    numbers = [
        Payment().credit_card_number(),
        Payment().credit_card_number(card_type=CardType.VISA),
        Payment().credit_card_number(card_type=CardType.MASTER_CARD),
        Payment().credit_card_number(card_type=CardType.AMERICAN_EXPRESS),
    ]
    # Check is numbers are correct
    assert len(numbers) == 4
    for number in numbers:
        assert len(number) == 19
        assert type(number) is str
    # Test for right prefixes of numbers

# Generated at 2022-06-14 00:37:39.319130
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    number = Payment('en', seed = 1).credit_card_number(CardType.VISA)
    assert number == '4455 5299 1152 2450', "Not 4455 5299 1152 2450"

# Generated at 2022-06-14 00:37:49.061547
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    obj = Payment()
    for i in range(100):
        res = obj.credit_card_number()

# Generated at 2022-06-14 00:37:58.018680
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    import pytest
    from mimesis.enums import CardType
    from mimesis.exceptions import NonEnumerableError

    payment = Payment()

    err_msg = 'CardType is not supported'

    with pytest.raises(NonEnumerableError) as ex:
        payment.credit_card_number(card_type='Not a CardType')

    assert err_msg == str(ex.value)

    for i in [CardType.VISA, CardType.MASTER_CARD, CardType.AMERICAN_EXPRESS]:
        assert payment.credit_card_number(card_type=i)

# Generated at 2022-06-14 00:38:06.452550
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment_test = Payment(seed=1345)
    number_1 = payment_test.credit_card_number()
    number_2 = payment_test.credit_card_number(CardType.VISA)
    number_3 = payment_test.credit_card_number(CardType.MASTER_CARD)
    assert number_1 == "5531 8658 4477 8563"
    assert number_2 == "4473 9330 3798 2270"
    assert number_3 == "5578 0990 1481 9720"

# Generated at 2022-06-14 00:38:10.298470
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    test_number1 = Payment().credit_card_number()
    test_number2 = Payment().credit_card_number()
    assert test_number1 != test_number2
    assert isinstance(test_number1, str)
    assert isinstance(test_number2, str)

# Generated at 2022-06-14 00:38:14.409865
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    gen = Payment(seed=0)
    assert gen.credit_card_number() == '3859 8153 3740 5607'
    assert gen.credit_card_number(card_type=CardType.VISA) == '4553 4138 3686 4342'

# Generated at 2022-06-14 00:38:22.623316
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    card_number = payment.credit_card_number()

    # Test is_valid_credit_card_number is True
    assert payment.is_valid_credit_card_number(card_number) is True

    # Test if card_number is correct format (d{4} d{4} d{4} d{4})
    # NOTE: we don't put this in the method because it would slow it down too much
    reg_exp = re.compile(r'^\d{4} \d{4} \d{4} \d{4}$')
    match = reg_exp.match(card_number)
    if match is None:
        raise ValueError(f'Generated credit card number "{card_number}" is in invalid format')



# Generated at 2022-06-14 00:38:24.285729
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment('en')
    res = payment.credit_card_number()
    assert len(res) == 18 and not ' ' in res

# Generated at 2022-06-14 00:38:33.462926
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()

    # Visa
    assert re.match(r'\d{4} \d{4} \d{4} \d{4}', payment.credit_card_number(CardType.VISA))
    assert payment.credit_card_number(CardType.VISA).startswith('4')

    # MasterCard
    assert re.match(r'\d{4} \d{4} \d{4} \d{4}', payment.credit_card_number(CardType.MASTER_CARD))
    assert payment.credit_card_number(CardType.MASTER_CARD).startswith(('2', '5'))

    # American Express

# Generated at 2022-06-14 00:38:39.648967
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Unit test for method credit_card_number of class Payment"""

    payment = Payment('en')
    payment.random.seed(0)
    card_number = payment.credit_card_number(CardType.MASTER_CARD)
    assert card_number == "5245 7046 8279 6848"


# Generated at 2022-06-14 00:38:47.761712
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment1 = Payment('en')
    payment2 = Payment('en', seed=42)
    assert payment1.credit_card_number(card_type=CardType.VISA) == "4455 5299 1152 2450"
    assert payment2.credit_card_number(card_type=CardType.VISA) == "4455 5299 1152 2450"
    assert payment1.credit_card_number(card_type=CardType.MASTER_CARD) == "5100 6284 2563 4252"
    assert payment2.credit_card_number(card_type=CardType.MASTER_CARD) == "2228 1622 6157 1470"
    assert payment1.credit_card_number(card_type=CardType.AMERICAN_EXPRESS) == "3738 116002 61534"

# Generated at 2022-06-14 00:38:57.545854
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Test for method credit_card_number of class Payment"""
    test_Payment = Payment('en')
    assert test_Payment.credit_card_number(CardType.VISA)
    assert test_Payment.credit_card_number(CardType.MASTER_CARD)
    assert test_Payment.credit_card_number(CardType.AMERICAN_EXPRESS)



# Generated at 2022-06-14 00:39:00.197385
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """
    Test case to test the credit_card_number method of class Payment
    """
    payment = Payment()
    credit_card_number = payment.credit_card_number()
    print(credit_card_number)


# Generated at 2022-06-14 00:39:07.881559
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    seed_number = 22
    card_type = CardType.VISA
    card_number = Payment(seed = seed_number).credit_card_number(card_type = card_type)
    card_number = card_number.replace(' ', '')
    assert card_number == '4022190529282475'
# End of Unit test for method credit_card_number of class Payment

# Generated at 2022-06-14 00:39:15.170498
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    print(Payment('en').credit_card_number())
    print(Payment('en').credit_card_number(card_type=CardType.MASTER_CARD))
    print(Payment('en').credit_card_number(card_type=CardType.AMERICAN_EXPRESS))

if __name__ == '__main__':
    test_Payment_credit_card_number()

# Generated at 2022-06-14 00:39:19.977233
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
	op = Payment(seed=None)
	assert re.fullmatch(r'((\d{4}( |-)){3}\d{4})', op.credit_card_number()) is not None


# Generated at 2022-06-14 00:39:28.250878
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    # Create a Payment object
    payment = Payment()

    # Generate credit card number
    credit_card = payment.credit_card_number()

    # Return 16 digit string
    assert len(credit_card) == 19

    # Return 4 groups of digits
    assert len(credit_card.split()) == 4

    # Return a valid credit card number
    assert luhn_checksum(credit_card[0:15]) == credit_card[15]

# Generated at 2022-06-14 00:39:32.526212
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment()
    print(p.credit_card_number())
    print(p.credit_card_number(card_type=CardType.AMERICAN_EXPRESS))
    print(p.credit_card_number(card_type=CardType.MASTER_CARD))
    print(p.credit_card_number(card_type=CardType.VISA))

test_Payment_credit_card_number()

# Generated at 2022-06-14 00:39:37.810185
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    provider = Payment()
    assert isinstance(provider.credit_card_number('Visa'), str)
    assert isinstance(provider.credit_card_number('MasterCard'), str)
    assert isinstance(provider.credit_card_number('AmericanExpress'), str)
    assert provider.credit_card_number('Visa')
    assert provider.credit_card_number('MasterCard')
    assert provider.credit_card_number('AmericanExpress')

# Generated at 2022-06-14 00:39:40.916775
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    output = payment.credit_card_number(CardType.AMERICAN_EXPRESS)
    assert len(output) == 19
    assert output[:2] == '37'
    assert output[-1] == luhn_checksum(output[:-1])

# Generated at 2022-06-14 00:39:45.359509
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Unit test for method credit_card_number of class Payment."""
    payment = Payment()
    number = payment.credit_card_number()
    assert luhn_checksum(number[:-1]) == number[-1]

# Generated at 2022-06-14 00:40:01.554952
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment()
    print(p.credit_card_number())
    print(p.credit_card_number(CardType.AMERICAN_EXPRESS))


# Generated at 2022-06-14 00:40:11.691920
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    # test for method credit_card_number of class Payment
    # when card_type is None
    p = Payment()
    card_number = p.credit_card_number()
    print(card_number)
    assert len(card_number)

    # test for method credit_card_number of class Payment
    # when card_type is VISA
    p = Payment()
    card_number = p.credit_card_number(card_type=CardType.VISA)
    print(card_number)
    assert len(card_number)

    # test for method credit_card_number of class Payment
    # when card_type is MASTER_CARD
    p = Payment()
    card_number = p.credit_card_number(card_type=CardType.MASTER_CARD)
    print(card_number)


# Generated at 2022-06-14 00:40:15.891709
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    ans = payment.credit_card_number()
    assert ans in map(lambda x: str(x), range(1000000000000000, 9999999999999999))
    assert ' ' not in ans



# Generated at 2022-06-14 00:40:21.753201
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    card_number = payment.credit_card_number(CardType.MASTER_CARD)
    assert card_number[0:2] == "52" or card_number[0:2] == "53" or card_number[0:2] == "54" or card_number[0:2] == "55"

# Generated at 2022-06-14 00:40:25.882967
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    assert re.match(r'\d{4} \d{4} \d{4} \d{4}$', Payment().credit_card_number())



# Generated at 2022-06-14 00:40:31.696529
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Unit test for method credit_card_number of class Payment"""
    provider = Payment()
    card_number = ''
    try:
        card_number = provider.credit_card_number('CARTE BLEUE')
    except Exception as e:
        print(e)
    assert len(card_number) > 0 and card_number == '4455 5299 1152 2450'


# Generated at 2022-06-14 00:40:43.037921
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    # test for CardType.VISA
    visa = Payment()
    assert visa.credit_card_number(CardType.VISA)
    # test for CardType.MASTERCARD
    master_card = Payment()
    assert master_card.credit_card_number(CardType.MASTER_CARD)
    # test for CardType.AMERICAN_EXPRESS
    american_express = Payment()
    assert american_express.credit_card_number(CardType.AMERICAN_EXPRESS)
    # test for unsupported card type
    test_type = Payment()
    try:
        assert test_type.credit_card_number('Some card type')
    except NonEnumerableError:
        assert True
    else:
        assert False

# Generated at 2022-06-14 00:40:54.319187
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    from random import seed
    from mimesis.enums import CardType

    seed(0)
    assert(Payment().credit_card_number(CardType.VISA) == "4611 8452 0743 9490")

    seed(1)
    assert(Payment().credit_card_number(CardType.MASTER_CARD) == "5174 8006 7553 8387")

    seed(2)
    assert(Payment().credit_card_number(CardType.AMERICAN_EXPRESS) == "3775 0361 70916")

    seed(2)
    assert(Payment().credit_card_number() == "4611 8452 0743 9490")

    seed(2)

# Generated at 2022-06-14 00:41:08.528542
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    # Test case 1, 2, 3

    # Test case 1
    _card_type = CardType.VISA
    _card_number = Payment.credit_card_number(_card_type)
    _card_number_1st_4_digit = int(_card_number[:4])
    _card_number_2nd_4_digit = int(_card_number[5:9])
    _card_number_3rd_4_digit = int(_card_number[10:14])
    _card_number_4th_4_digit = int(_card_number[15:19])

    assert 0 <= _card_number_4th_4_digit < 10
    assert 0 <= _card_number_3rd_4_digit < 10
    assert 0 <= _card_number_2nd_4_digit < 10
    assert 0

# Generated at 2022-06-14 00:41:14.018881
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment('zh')
    assert p.credit_card_number() == ('4455 5299 1152 2450')


# Generated at 2022-06-14 00:41:44.274494
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    # Test 1
    caller = Payment("en")
    result = caller.credit_card_number(CardType.AMERICAN_EXPRESS)
    assert len(result) == 17

# Generated at 2022-06-14 00:41:53.240849
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    from mimesis.enums import CardType
    payment = Payment()
    # print(payment.credit_card_number())
    assert payment.credit_card_number(CardType.VISA)
    assert payment.credit_card_number(CardType.MASTER_CARD)
    assert payment.credit_card_number(CardType.AMERICAN_EXPRESS)
    # assert payment.credit_card_number(CardType.DINERS_CLUB)
    # assert payment.credit_card_number(CardType.JCB)



# Generated at 2022-06-14 00:41:57.213742
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():

    # instantiate class Payment
    payment = Payment('en')

    # test for default value
    assert payment.credit_card_number()

    # test for card type from enum object
    assert payment.credit_card_number(CardType.MASTER_CARD)

    # test for card type from string
    assert payment.credit_card_number('MasterCard')


# Generated at 2022-06-14 00:41:58.901202
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    import doctest
    doctest.testmod(extraglobs={'payment':Payment('en')})

# Generated at 2022-06-14 00:42:00.918084
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    myPayment = Payment(random=True)

    for num in range(100):
        print(myPayment.credit_card_number())

# Generated at 2022-06-14 00:42:10.694528
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    generator = Payment('en')
    card_number = generator.credit_card_number()
    print('Random card number: ', card_number)
    # Test case: check valid card number
    assert len(card_number) == 19 and bool(re.search(r'\d', card_number)) == True
    # Test case: check card number with CardType Visa
    card_number_Visa = generator.credit_card_number(CardType.VISA)
    assert card_number_Visa[0] == '4' and len(card_number_Visa) == 19 and bool(re.search(r'\d', card_number_Visa)) == True
    # Test case: check card number with CardType MasterCard
    card_number_MasterCard = generator.credit_card_number(CardType.MASTER_CARD)


# Generated at 2022-06-14 00:42:21.855073
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    for i in range(0,100):
        pc = Payment("en")
        cc_number = pc.credit_card_number()
        cc_number_list = cc_number.split()
        cc_number_str = ''.join(cc_number_list)
        cc_number_str_list = [int(num) for num in cc_number_str]
        luhn_list = [num * 2 for num in cc_number_str_list]
        for j in range(0,15):
            if j%2 == 0:
                luhn_list[j] = luhn_list[j] - 9 if luhn_list[j] > 9 else luhn_list[j]
        sum_luhn_list = sum(luhn_list)
        check_digit = 10 - sum_lu

# Generated at 2022-06-14 00:42:33.004941
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment(seed=123456789)
    result_1 = p.credit_card_number(CardType.VISA)
    expected_result_1 = '4588 3231 2347 6403'
    result_2 = p.credit_card_number(CardType.MASTER_CARD)
    expected_result_2 = '5694 4142 5187 9267'
    result_3 = p.credit_card_number(CardType.AMERICAN_EXPRESS)
    expected_result_3 = '3478 983581 89729'

    assert(result_1 == expected_result_1)
    assert(result_2 == expected_result_2)
    assert(result_3 == expected_result_3)

    payment = Payment()
    result_4 = payment.credit_card_number()

# Generated at 2022-06-14 00:42:34.681657
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    pt = Payment()
    assert isinstance(pt.credit_card_number(), str)


# Generated at 2022-06-14 00:42:39.036019
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment("en")

    assert p.credit_card_number(CardType.VISA) == "4543 0747 4291 7170"
    assert p.credit_card_number(CardType.MASTER_CARD) == "5510 0166 3965 5837"
    assert p.credit_card_number(CardType.AMERICAN_EXPRESS) == "3745 609584 03204"

# Generated at 2022-06-14 00:43:37.203161
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment()

    # Test for card type "Visa"
    ccn_visa = p.credit_card_number(card_type='visa')
    assert len(ccn_visa) == 18
    assert luhn_checksum(ccn_visa[:-3].replace(' ', '')) == int(ccn_visa[-3:].replace(' ', ''))

    # Test for card type "Master Card"
    ccn_mc = p.credit_card_number(card_type='mastercard')
    assert len(ccn_mc) == 18
    assert luhn_checksum(ccn_mc[:-3].replace(' ', '')) == int(ccn_mc[-3:].replace(' ', ''))

    # Test for card type "American Express"

# Generated at 2022-06-14 00:43:46.228268
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Test credit_card_number method of class Payment."""
    payment = Payment()
    assert payment.credit_card_number(CardType.VISA) == "4829 0368 2905 2361"
    assert payment.credit_card_number(CardType.MASTER_CARD) == "2224 9269 5688 4514"
    assert payment.credit_card_number(CardType.AMERICAN_EXPRESS) == "3496 276087 88712"
    assert payment.credit_card_number(CardType.DANKORT) == "5019 0871 6732 0798"
    assert payment.credit_card_number(CardType.DINERS_CLUB) == "3676 0206 5401 7965"

# Generated at 2022-06-14 00:43:52.219453
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    provider = Payment()
    assert re.match(r'\d{4} \d{4} \d{4} \d{4}', provider.credit_card_number())
    print("Test method credit_card_number of class Payment: OK")


# Generated at 2022-06-14 00:43:53.181407
# Unit test for method credit_card_number of class Payment

# Generated at 2022-06-14 00:43:57.870991
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment(locale="en")
    card_number = payment.credit_card_number(CardType.MASTER_CARD)
    print(card_number)


# Generated at 2022-06-14 00:44:08.780510
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Unit test for the method credit_card_number of class Payment"""
    payment = Payment()
    card_number = payment.credit_card_number()
    # check that the length of the generated card is 16
    assert len(card_number) == 16
    # check that the generated card number is a natural number
    assert card_number.isdigit() == True
    # check that the generated card number is a product of luhn checksum
    assert luhn_checksum(card_number) == 0

# Generated at 2022-06-14 00:44:12.070135
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment(seed=12)
    assert p.credit_card_number() == '4455 5299 1152 2450'

# Generated at 2022-06-14 00:44:15.142412
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment()
    p.credit_card_number()
    p.credit_card_number()
    p.credit_card_number()

# Generated at 2022-06-14 00:44:18.389561
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment()
    assert len(p.credit_card_number()) == 19

# Generated at 2022-06-14 00:44:21.911864
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment: Payment = Payment(seed=123456)
    result: str = payment.credit_card_number(card_type=CardType.MASTER_CARD)
    assert result == '5338 4659 0512 0961'

# Generated at 2022-06-14 00:45:55.330952
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment()
    assert len(p.credit_card_number()) == 19


# Generated at 2022-06-14 00:46:06.161499
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    from enum import Enum
    from random import randint
    payment = Payment()
    regex = re.compile(r'(\d{4})(\d{4})(\d{4})(\d{4})')

    for _ in range(10):
        cardType = randint(0, 3)
        if cardType == 0:
            cardType = Enum('CardType', 'VISA')
        elif cardType == 1:
            cardType = Enum('CardType', 'MASTER_CARD')
        elif cardType == 2:
            cardType = Enum('CardType', 'AMERICAN_EXPRESS')
        else:
            raise NonEnumerableError('CardType')

        card = payment.credit_card_number(card_type=cardType)

# Generated at 2022-06-14 00:46:14.865259
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Unit test for method credit_card_number of class Payment."""
    payment = Payment()
    print(payment.credit_card_number(CardType.VISA))
    print()
    try:
        print(payment.credit_card_number(CardType.UNKNOWN))
    except NonEnumerableError as e:
        print(e)
    print()
    print(payment.credit_card_number(CardType.MASTER_CARD))
    print()
    print(payment.credit_card_number(CardType.AMERICAN_EXPRESS))
    print()
