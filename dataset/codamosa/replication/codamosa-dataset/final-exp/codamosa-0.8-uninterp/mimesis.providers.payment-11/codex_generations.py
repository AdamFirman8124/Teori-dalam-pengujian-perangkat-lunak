

# Generated at 2022-06-14 00:36:25.130107
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    assert len(payment.credit_card_number()) == 16
    assert len(payment.credit_card_number(CardType.MASTER_CARD)) == 16
    assert len(payment.credit_card_number(CardType.AMERICAN_EXPRESS)) == 15
    # Unit test for method credit_card_network of class Payment

# Generated at 2022-06-14 00:36:34.673953
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    from mimesis.enums import CardType
    payment = Payment()
    card = payment.credit_card_number(card_type=CardType.AMERICAN_EXPRESS)
    import re
    assert not re.search('[^\d\s]', card)
    assert re.search('\s', card)
    assert len(card.replace(' ', '')) == 15
    assert card[:2] == '34' or card[:2] == '37'


# Generated at 2022-06-14 00:36:39.349386
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment()
    r = p.credit_card_number()
    assert r
    result = " ".join(r.split())
    assert result is not None
    assert len(result.split()) == 4


# Generated at 2022-06-14 00:36:40.119620
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    pass

# Generated at 2022-06-14 00:36:42.949252
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    mimesis.complement.Payment()

test_Payment_credit_card_number()

# Generated at 2022-06-14 00:36:51.252285
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """This function is a unit test for method credit_card_number of class Payment
    The expected result is:
        -a credit card number with 16 digits (consisting of the first four digits (IIN) and the last 12 digits (account number)
    The method uses the testing-framework python unittest to test the method
    :return: This function does not return anythin.
    """
    test_p = Payment()
    test_p.seed(0)
    pattern_Visa = re.compile(r'\d{4}\s\d{4}\s\d{4}\s\d{4}')
    expected_Visa = '4455 5299 1152 2450'
    actual_Visa = test_p.credit_card_number(CardType.VISA)

# Generated at 2022-06-14 00:36:54.991518
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():

    test = Payment(seed=1)

    assert test.credit_card_number(CardType.VISA) == "4455 5299 1152 2450"


# Generated at 2022-06-14 00:37:05.765942
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    visa = payment.credit_card_number(CardType.VISA)
    assert visa[:1] == '4'
    assert len(visa) == 19
    master = payment.credit_card_number(CardType.MASTER_CARD)
    assert master[:2] == '22' or master[:2] == '51'
    assert len(master) == 19
    amex = payment.credit_card_number(CardType.AMERICAN_EXPRESS)
    assert amex[:2] == '34' or amex[:2] == '37'
    assert len(amex) == 18

# Generated at 2022-06-14 00:37:10.499835
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment()
    for _ in range(500):
        cc = p.credit_card_number()
        if len(cc) != 19:
            raise ValueError(cc)
        if not re.search(r'^\d{4}\s\d{4}\s\d{4}\s\d{4}$', cc):
            raise ValueError(cc)

# Generated at 2022-06-14 00:37:20.100403
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment(seed = 'a')
    # Visa
    for i in range(10):
        assert re.match(r'4\d{3} \d{4} \d{4} \d{4}', p.credit_card_number())
    # Visa
    for i in range(10):
        assert re.match(r'4\d{3} \d{4} \d{4} \d{4}',
                        p.credit_card_number(CardType.VISA))
    # MasterCard
    for i in range(10):
        print(p.credit_card_number(CardType.MASTER_CARD))

# Generated at 2022-06-14 00:37:34.053414
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    a = Payment()
    print(a.credit_card_number())
    print(a.credit_card_number(CardType.MASTER_CARD))
    print(a.credit_card_number(CardType.AMERICAN_EXPRESS))
    # print(a.credit_card_number(CardType.UNION_PAY))
    # print(a.credit_card_number(CardType.DISCOVER))
    # print(a.credit_card_number(CardType.DINERS_CLUB))
    # print(a.credit_card_number(CardType.JCB))



# Generated at 2022-06-14 00:37:45.422284
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Test for method credit_card_number of class Payment."""
    # data for test
    visa_set_data = [{"card_type": "visa", "number": "4455 5299 1152 2450"}]
    master_card_set_data = [{"card_type": "master_card", "number": "2221 6667 5556 2520"}]
    american_express_set_data = [{"card_type": "american_express", "number": "3781 7681 474"}]

    # test for visa card type
    for data in visa_set_data:
        assert data["number"] == Payment().credit_card_number(data["card_type"])
    # test for master card
    for data in master_card_set_data:
        assert data["number"] == Payment().credit_card_

# Generated at 2022-06-14 00:37:49.680712
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    for item in CardType:
        credit_card_number = payment.credit_card_number(CardType[item])
        print(credit_card_number)

# Generated at 2022-06-14 00:37:53.655425
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment("en")
    result = payment.credit_card_number(CardType.VISA)
    assert isinstance(result, str) and len(result) == 19


# Generated at 2022-06-14 00:37:59.910530
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    print("\nStart test credit_card_number method\n")
    payment = Payment()
    cardType = [
        CardType.VISA,
        CardType.MASTER_CARD,
        CardType.AMERICAN_EXPRESS,
    ]
    for i in range(len(cardType)):
        print(payment.credit_card_number(card_type=cardType[i]))
    print("\nEnd test credit_card_number method\n")

# Generated at 2022-06-14 00:38:03.602557
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Unit test for method credit_card_number of class Payment"""
    num1 = Payment(seed=111).credit_card_number()
    num2 = Payment(seed=111).credit_card_number()
    assert num1 == num2
    num3 = Payment(seed=222).credit_card_number()
    assert num1 != num3

# Generated at 2022-06-14 00:38:15.366286
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    assert payment.credit_card_number()[:2] == '45' or payment.credit_card_number()[:2] == '44'
    assert payment.credit_card_number(CardType.VISA)[:2] == '45' or payment.credit_card_number()[:2] == '44'
    assert payment.credit_card_number(CardType.MASTER_CARD)[:2] == '51' or payment.credit_card_number()[:2] == '52' or payment.credit_card_number()[:2] == '53' or payment.credit_card_number()[:2] == '54' or payment.credit_card_number()[:2] == '55'

# Generated at 2022-06-14 00:38:17.101991
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    assert payment.credit_card_number().startswith("4")


# Generated at 2022-06-14 00:38:25.219994
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment(seed=100)
    card_number = payment.credit_card_number(card_type=CardType.VISA)
    assert (card_number == '4455 5299 1152 2450')
    card_number = payment.credit_card_number(card_type=CardType.MASTER_CARD)
    assert (card_number == '5234 4365 2785 9582')
    card_number = payment.credit_card_number(card_type=CardType.AMERICAN_EXPRESS)
    assert (card_number == '3722 807816 13608')
    try:
        payment.credit_card_number(card_type=CardType.VISA_ELECTRON)
    except NonEnumerableError:
        pass


# Generated at 2022-06-14 00:38:32.251545
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    different_types = []
    for _ in range(0, 10):
        obj = Payment('en')
        different_types.append(obj.credit_card_number())
    
    credit_card_number1 = str(Payment('en').credit_card_number())
    credit_card_number2 = str(Payment('en').credit_card_number())
    credit_card_number3 = str(Payment('de').credit_card_number())

    assert credit_card_number1 != credit_card_number2
    assert credit_card_number1 != credit_card_number3
    assert type(credit_card_number1) is str


# Generated at 2022-06-14 00:38:46.331166
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    for i in range(10):
        print(payment.credit_card_number())


# Generated at 2022-06-14 00:38:50.410898
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    for i in range(0, 10):
        r = Payment()
        assert re.match(r"\d{4} \d{4} \d{4} \d{4}", r.credit_card_number())


# Generated at 2022-06-14 00:39:01.666231
# Unit test for method credit_card_number of class Payment

# Generated at 2022-06-14 00:39:09.710576
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    import collections
    # Test case 1
    p = Payment()
    p.seed(0)
    cn = p.credit_card_number()
    result = collections.Counter(cn).items()
    compare_result = [(' ', 5), ('4', 16)]
    assert(result == compare_result)
    # Test case 2
    p = Payment()
    p.seed(1)
    cn = p.credit_card_number()
    result = collections.Counter(cn).items()
    compare_result = [(' ', 4), ('3', 2), ('7', 14)]
    assert(result == compare_result)
    # Test case 3
    p = Payment()
    p.seed(2)
    cn = p.credit_card_number()
    result = collections.Counter(cn).items()
    compare_

# Generated at 2022-06-14 00:39:13.727711
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    # Unit test for method credit_card_number of class Payment
    assert (re.match('^(\d{4} ){3}\d{4}$', payment.credit_card_number()) is not None)

# Generated at 2022-06-14 00:39:20.608217
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment(seed=42)
    print(p.credit_card_number())
    print(p.credit_card_number(CardType.MASTER_CARD))
    print(p.credit_card_number(CardType.AMERICAN_EXPRESS))
    print(p.credit_card_number())


# Generated at 2022-06-14 00:39:34.032947
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    visa_number = Payment().credit_card_number(CardType.VISA)
    assert re.match(r'[0-9]{4}[ ]{1}[0-9]{4}[ ]{1}[0-9]{4}[ ]{1}[0-9]{4}', visa_number) is not None
    mastercard_number = Payment().credit_card_number(CardType.MASTER_CARD)
    assert re.match(r'[0-9]{4}[ ]{1}[0-9]{4}[ ]{1}[0-9]{4}[ ]{1}[0-9]{4}', mastercard_number) is not None
    american_express_number = Payment().credit_card_number(CardType.AMERICAN_EXPRESS)

# Generated at 2022-06-14 00:39:36.386769
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    assert payment.credit_card_number(
        CardType.AMERICAN_EXPRESS) == "3787 716275 82227"


# Generated at 2022-06-14 00:39:41.394139
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    card_types = [
        CardType.VISA,
        CardType.AMERICAN_EXPRESS,
        CardType.MASTER_CARD
    ]
    for card_type in card_types:
        assert re.search(r'^\d{4}\s\d{4}\s\d{4}\s\d{4}$', Payment().credit_card_number(card_type)) is not None
    print('test_Payment_credit_card_number is finished')

# Generated at 2022-06-14 00:39:49.702543
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Testing correct form of credit card number generation."""
    payment = Payment()
    regex = re.compile(r'^\d{16}$')
    assert regex.search(payment.credit_card_number(card_type=CardType.VISA))
    assert regex.search(payment.credit_card_number(card_type=CardType.MASTER_CARD))
    assert regex.search(payment.credit_card_number(card_type=CardType.AMERICAN_EXPRESS))
    assert regex.search(payment.credit_card_number())


# Generated at 2022-06-14 00:40:25.373959
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    card = payment.credit_card_number()
    assert isinstance(card, str)


# Generated at 2022-06-14 00:40:26.453951
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    generator = Payment()
    assert generator.credit_card_number()

# Generated at 2022-06-14 00:40:35.200096
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    assert payment.credit_card_number() in {
        '4455 5299 1152 2450',
        '2221 0772 1326 6959',
        '5100 2040 0140 8060',
        '3734 9951 3524 086',
    }
    assert payment.credit_card_number(
        card_type=CardType.VISA) == '4455 5299 1152 2450'
    assert payment.credit_card_number(
        card_type=CardType.MASTER_CARD) in {
            '2221 0772 1326 6959',
            '5100 2040 0140 8060',
        }
    assert payment.credit_card_number(
        card_type=CardType.AMERICAN_EXPRESS) == '3734 9951 3524 086'

# Generated at 2022-06-14 00:40:45.221750
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment()
    n = p.credit_card_number(CardType.AMERICAN_EXPRESS)
    assert isinstance(n, str)
    assert ' ' in n
    assert len(n.replace(' ', '')) == 15
    assert n[0] == '3'
    assert (n[1] == '4' or n[1] == '7')

    n = p.credit_card_number(CardType.MASTER_CARD)
    assert isinstance(n, str)
    assert ' ' in n
    assert len(n.replace(' ', '')) == 16
    assert n[0] == '5'

    n = p.credit_card_number(CardType.VISA)
    assert isinstance(n, str)
    assert ' ' in n

# Generated at 2022-06-14 00:40:52.664523
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    for _ in range(10):
        card_type = get_random_item(CardType, rnd=random)
        card_num = Payment(random.randint(0, 100)).credit_card_number(card_type)
        card_num_int = int(''.join(card_num.split()))
        assert card_num_int % 10 == 0 and len(card_num) == 19 \
            if card_type == CardType.AMERICAN_EXPRESS else True

# Generated at 2022-06-14 00:41:07.218026
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment_inst = Payment()
    # Test with VISA
    random_16_digit_number = payment_inst.credit_card_number(
        CardType.VISA)
    assert(random_16_digit_number[:1] == '4')
    assert(len(random_16_digit_number) == 19)
    # Test with MasterCard
    random_16_digit_number = payment_inst.credit_card_number(
        CardType.MASTER_CARD)
    assert(random_16_digit_number[:1] == '5')
    assert(len(random_16_digit_number) == 19)
    # Test with American Express
    random_15_digit_number = payment_inst.credit_card_number(
        CardType.AMERICAN_EXPRESS)

# Generated at 2022-06-14 00:41:12.419508
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    assert re.match(r'\d{4} \d{4} \d{4} \d{4}', Payment().credit_card_number())
    assert re.match(r'34\d{13}', Payment().credit_card_number(CardType.AMERICAN_EXPRESS))


# Generated at 2022-06-14 00:41:25.495587
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment('ru')
    card_type = CardType.MASTER_CARD
    cc = p.credit_card_number(card_type)
    assert len(cc) == 19
    assert int(cc[:2]) in range(51,56)
    card_type = CardType.VISA
    cc = p.credit_card_number(card_type)
    assert len(cc) == 19
    assert int(cc[:2]) in range(40,50)
    card_type = CardType.AMERICAN_EXPRESS
    cc = p.credit_card_number(card_type)
    assert len(cc) == 17
    assert int(cc[:2]) in [34, 37]
    


# Generated at 2022-06-14 00:41:32.975766
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    print("Test credit_card_number()")
    # Arrange
    payment = Payment()
    card_no = payment.credit_card_number()

    # Assert
    assert len(card_no) == 16
    assert card_no.isdigit()

# Test method credit_card_network of class Payment

# Generated at 2022-06-14 00:41:35.822354
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment('en')
    assert re.match(r'^[0-9][0-9][0-9][0-9] [0-9][0-9][0-9][0-9] [0-9][0-9][0-9][0-9] [0-9][0-9][0-9][0-9]$',
                     payment.credit_card_number())