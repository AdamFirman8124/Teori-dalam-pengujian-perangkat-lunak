

# Generated at 2022-06-14 00:36:21.774428
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    for i in range(1):
        print(Payment().credit_card_number())

# Generated at 2022-06-14 00:36:25.233123
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    card_number = payment.credit_card_number()
    print(card_number)

if __name__ == "__main__":
    test_Payment_credit_card_number()

# Generated at 2022-06-14 00:36:28.472790
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    v=payment.credit_card_number()
    print(v)


# Generated at 2022-06-14 00:36:43.087120
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment(seed=2)
    assert p.credit_card_number(CardType.VISA) == '4554 5299 1152 2450'
    assert p.credit_card_number(CardType.MASTER_CARD) == '2669 7143 6893 5079'
    assert p.credit_card_number(CardType.AMERICAN_EXPRESS) == '3748 757906 86588'
    try:
        p.credit_card_number(CardType.DISCOVER)
        assert 'NonEnumerableError should be raised'
    except NonEnumerableError:
        pass
    assert p.credit_card_number() in ['4554 5299 1152 2450', '2669 7143 6893 5079', '3748 757906 86588']


# Generated at 2022-06-14 00:36:48.948115
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    assert Payment().credit_card_number(CardType.AMERICAN_EXPRESS) == '3741 812099 39293', 'Não está funcionando'
    assert Payment().credit_card_number(CardType.MASTER_CARD) == '5115 3401 0432 4556', 'Não está funcionando'
    assert Payment().credit_card_number(CardType.VISA) == '4347 7414 5204 1527', 'Não está funcionando'

# Generated at 2022-06-14 00:36:54.130947
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    from mimesis.providers.payment import Payment
    from mimesis.enums import CardType
    p = Payment('zh')
    cn = p.credit_card_number(card_type = CardType.MASTER_CARD)
    assert cn[0] == '2'

# Generated at 2022-06-14 00:36:57.306761
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    cc_number = payment.credit_card_number()
    print(cc_number)


# Generated at 2022-06-14 00:37:03.515982
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    seed = 123456
    card_type = 2
    pp = Payment('ru', seed=seed)
    assert pp.credit_card_number(card_type).split(' ') == ['4405', '8498', '5414', '4981']

test_Payment_credit_card_number()

# Generated at 2022-06-14 00:37:05.158446
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    pay = Payment()
    card_number = pay.credit_card_number()
    assert True is pay.verify_credit_card_number(card_number)

# Generated at 2022-06-14 00:37:07.897213
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment(seed=42)
    number = payment.credit_card_number()

    assert number == "4455 5299 1152 2450"


# Generated at 2022-06-14 00:37:16.674508
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Test method credit_card_number(TestCase)."""
    ccn = Payment('en', seed=12345)
    assert ccn.credit_card_number() == '4455 5299 1152 2450'

# Generated at 2022-06-14 00:37:28.310257
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    from random import seed
    from mimesis.enums import CardType
    from mimesis.exceptions import NonEnumerableError
    from mimesis.providers.payment import Payment

    seed(42)
    p = Payment('en')

    # Test for CardType.VISA
    for _ in range(20):
        assert re.match(r'4\d{3}(\s\d{4}){3}', p.credit_card_number(CardType.VISA))

    # Test for CardType.MASTER_CARD
    for _ in range(20):
        num = p.credit_card_number(CardType.MASTER_CARD)

# Generated at 2022-06-14 00:37:37.019100
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    from mimesis.enums import CardType

    # Initialize and set seed to be 0
    payment = Payment(seed=0)

    # Test the case using card type VISA
    # if card_type is CardType.VISA:
    payment.credit_card_number(card_type=CardType.VISA)
    
    # Test the case using card type Master_Card
    # if card_type == CardType.MASTER_CARD:
    payment.credit_card_number(card_type=CardType.MASTER_CARD)

    # Test the case using card type AMERICAN_EXPRESS
    # elif card_type == CardType.AMERICAN_EXPRESS:
    payment.credit_card_number(card_type=CardType.AMERICAN_EXPRESS)

    # Test the case using card type DISCO

# Generated at 2022-06-14 00:37:41.468487
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Test method credit_card_number of Payment."""
    
    # test credit_card_number with card type equal to Visa
    p = Payment(seed=0)
    result = p.credit_card_number(CardType.VISA)
    assert result == "4418 0947 6356 0685"
    
    # test credit_card_number with card type equal to MasterCard
    p = Payment(seed=0)
    result = p.credit_card_number(CardType.MASTER_CARD)
    assert result == "2240 3249 1640 1283"
    
    # test credit_card_number with card type equal to AmericanExpress
    p = Payment(seed=0)
    result = p.credit_card_number(CardType.AMERICAN_EXPRESS)

# Generated at 2022-06-14 00:37:47.929555
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment('en')

    for _ in range(100):
        # Visa
        number = payment.credit_card_number(CardType.VISA)
        assert number[0] == '4'

        # MasterCard
        number = payment.credit_card_number(CardType.MASTER_CARD)
        assert int(number[0:2]) >= 22 and int(number[0:2]) <= 55

        # American Express
        number = payment.credit_card_number(CardType.AMERICAN_EXPRESS)
        assert (number[0:2] == '34' or number[0:2] == '37')

# Generated at 2022-06-14 00:37:56.795994
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    from mimesis.enums import CardType
    from mimesis.providers.payment import Payment

    test_cases = [
        (CardType.MASTER_CARD),
        (CardType.VISA),
        (CardType.AMERICAN_EXPRESS)
    ]
    payment_obj = Payment('en')
    init_p = payment_obj.credit_card_number
    for test_case in test_cases:
        print(test_case)
        assert type(init_p(card_type=test_case)) is str
        

# Generated at 2022-06-14 00:38:02.945201
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    assert re.match(r'^\d{16}$', Payment().credit_card_number(CardType.VISA))
    assert re.match(r'^\d{15}$', Payment().credit_card_number(CardType.AMERICAN_EXPRESS))
    assert re.match(r'^\d{16}$', Payment().credit_card_number(CardType.MASTER_CARD))
    assert re.match(r'^\d{16}$', Payment().credit_card_number())


# Generated at 2022-06-14 00:38:09.004515
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Unit test for method credit_card_number of class Payment."""
    payment = Payment("en")
    payment.credit_card_number()
    payment.credit_card_number(CardType.MASTER_CARD)
    payment.credit_card_number(CardType.AMERICAN_EXPRESS)


# Generated at 2022-06-14 00:38:16.810989
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    from mimesis.enums import CardType

    my_card_network = CardType.AMERICAN_EXPRESS
    # generate an American Express card
    card_obj = Payment()
    card_number = card_obj.credit_card_number(my_card_network)
    # re object matches 4 digits followed by 6 digits followed by 5 digits 
    re_object = re.compile(r'(\d{4})(\d{6})(\d{5})')
    # check if card number follows this pattern
    assert re_object.search(card_number) is not None

# Generated at 2022-06-14 00:38:19.344574
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
	credit_card_number = Payment().credit_card_number()
	print("credit_card_number:", credit_card_number)
	return credit_card_number


# Generated at 2022-06-14 00:38:39.236427
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """
    Test for method credit_card_number of class Payment
    """
    print("\nClass Payment, method credit_card_number:\n")
    payment_object = Payment()
    for card_type in CardType:
        number = payment_object.credit_card_number(card_type)
        print("credit_card_number(card_type=CardType." + str(card_type) + "):\t" + str(number))



# Generated at 2022-06-14 00:38:44.664060
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    payment.seed(0)
    card_number = payment.credit_card_number(card_type=CardType.VISA)
    card_number_expected = "4040 6096 9162 5176"
    if card_number == card_number_expected:
        print('[Unit Test for Payment Class] test_Payment_credit_card_number method PASS')
    else:
        print('[Unit Test for Payment Class] test_Payment_credit_card_number method FAIL')



# Generated at 2022-06-14 00:38:47.952804
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    credit_card_number = payment.credit_card_number(CardType.VISA)
    assert(credit_card_number != None)

# Generated at 2022-06-14 00:38:58.574804
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    card = payment.credit_card_number(CardType.AMERICAN_EXPRESS)
    assert len(card) == 18
    assert card[0:2] == '37' or card[0:2] == '34'
    
    card = payment.credit_card_number(CardType.MASTER_CARD)
    assert len(card) == 16
    #assert card[0:4] in ['2221','2222','2223','2224','2225','2226','2227','2228','2229',
    #                     '2230','2231','2232','2233','2234','2235','2236','2237','2238','2239',
    #                     '2240','2241','2242','2243','2244','2245','2246','2247','2248','2

# Generated at 2022-06-14 00:39:11.097246
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment('en')
    number_type = {
        1: CardType.VISA,
        2: CardType.MASTER_CARD,
        3: CardType.AMERICAN_EXPRESS,
    }
    result = payment.credit_card_number()
    print(result)
    assert result in CREDIT_CARD_NETWORKS
    assert len(result) == 16
    result = payment.credit_card_number(number_type[1])
    assert result in CREDIT_CARD_NETWORKS
    assert len(result) == 16
    result = payment.credit_card_number(number_type[2])
    assert result in CREDIT_CARD_NETWORKS
    assert len(result) == 16
    result = payment.credit_card_number(number_type[3])
    assert result

# Generated at 2022-06-14 00:39:19.327487
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()

    for _ in range(0, 100):
        result = payment.credit_card_number()
        assert re.search(r'\d{4} \d{4} \d{4} \d{4}', result) is not None
        assert len(result.replace(' ', '')) == 16

    for _ in range(0, 100):
        result = payment.credit_card_number(CardType.AMERICAN_EXPRESS)
        assert re.search(r'\d{4} \d{6} \d{5}', result) is not None
        assert len(result.replace(' ', '')) == 15

    for _ in range(0, 100):
        result = payment.credit_card_number(CardType.VISA)

# Generated at 2022-06-14 00:39:24.089182
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    card_type = CardType.VISA
    credit_card_number = payment.credit_card_number(card_type)
    assert (credit_card_number[0] == '4')

# Generated at 2022-06-14 00:39:30.373184
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    x = Payment()
    # my_regex = re.compile(r'(\d{4})(\d{4})(\d{4})(\d{4})')
    # print(my_regex.search(x.credit_card_number()).groups())
    assert x.credit_card_number() is not None


# Generated at 2022-06-14 00:39:35.691982
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    x = Payment()
    card1 = x.credit_card_number(CardType.VISA)
    card2 = x.credit_card_number(CardType.MASTER_CARD)
    card3 = x.credit_card_number(CardType.AMERICAN_EXPRESS)
    print(card1)
    print(card2)
    print(card3)


# Generated at 2022-06-14 00:39:37.410977
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment(seed=4)
    assert payment.credit_card_number() != payment.credit_card_number()

# Generated at 2022-06-14 00:40:10.547379
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    import mimesis
    data = mimesis.Payment()
    assert len(data.credit_card_number())==19


# Generated at 2022-06-14 00:40:15.449474
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    PAYMENT = Payment()
    CARD_TYPE = CardType.VISA
    CREDIT = PAYMENT.credit_card_number(CARD_TYPE)
    print("credit_card_number:", CREDIT)

#test_Payment_credit_card_number()

# Generated at 2022-06-14 00:40:22.774247
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    obj = Payment('en')
    pattern = re.compile(r'^\b((4\d{3})|(5[1-5]\d{2})|(6011))(-?|\040?)(\d{4})(-?|\040?)(\d{4})(-?|\040?)(\d{4})\b$')
    assert pattern.match(obj.credit_card_number())

# Generated at 2022-06-14 00:40:34.082695
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    # print (50 * '-')
    payment = Payment()
    assert payment.credit_card_number(CardType.VISA)
    assert payment.credit_card_number(CardType.MASTER_CARD)
    assert payment.credit_card_number(CardType.AMERICAN_EXPRESS)

    # print (50 * '-')
    print ('Unit test for method credit_card_number of class Payment')
    print ('Generate a random Visa card number: ', payment.credit_card_number(CardType.VISA))
    print ('Generate a random Master card number: ', payment.credit_card_number(CardType.MASTER_CARD))
    print ('Generate a random American Express card number: ', payment.credit_card_number(CardType.AMERICAN_EXPRESS))


# Generated at 2022-06-14 00:40:37.026030
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment()
    print(p.credit_card_number(card_type=CardType.MASTER_CARD))  # pass
    # print(p.credit_card_number(card_type=CardType.Unknown))  # raise exception

# Generated at 2022-06-14 00:40:46.619266
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Test method credit_card_number of class Payment."""
    payment = Payment()
    visa_card_number = payment.credit_card_number()
    assert len(visa_card_number) == 16
    assert luhn_checksum(visa_card_number[:-1]) == visa_card_number[-1]
    master_card_number = payment.credit_card_number(card_type=CardType.MASTER_CARD)
    assert len(master_card_number) == 16
    assert luhn_checksum(master_card_number[:-1]) == master_card_number[-1]
    amex_card_number = payment.credit_card_number(card_type=CardType.AMERICAN_EXPRESS)
    assert len(amex_card_number) == 15

# Generated at 2022-06-14 00:40:55.535727
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment("es")
    p1 = payment.credit_card_number("Visa")
    assert len(p1) == 19
    assert p1[0] == "4"
    assert p1[4] == " " 
    assert p1[9] == " " 
    assert p1[14] == " " 
    p2 = payment.credit_card_number("MasterCard")
    assert len(p2) == 19
    assert p2[0] == "5"
    assert p2[4] == " " 
    assert p2[9] == " " 
    assert p2[14] == " " 
    p3 = payment.credit_card_number("American Express")
    assert len(p2) == 19
    assert p2[0] == "5"

# Generated at 2022-06-14 00:41:09.508168
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():

    test_pool = [
        ('1', 0, None),
        ('2', 1, CardType.MASTER_CARD),
        ('3', 2, CardType.AMERICAN_EXPRESS)
    ]

    for item in test_pool:
        card_type = item[2]
        if card_type == CardType.AMERICAN_EXPRESS:
            regex = re.compile(r'(\d{4})\s{1}(\d{6})\s{1}(\d{5})')
        else:
            regex = re.compile(r'(\d{4})\s{1}(\d{4})\s{1}(\d{4})\s{1}(\d{4})')


# Generated at 2022-06-14 00:41:12.519430
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    assert payment.credit_card_number(CardType.VISA)
    assert payment.credit_card_number(CardType.MASTER_CARD)
    assert payment.credit_card_number(CardType.AMERICAN_EXPRESS)


# Generated at 2022-06-14 00:41:23.853046
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    provider = Payment()
    credit_card_number = provider.credit_card_number()
    assert len(credit_card_number) == 19
    assert len(re.search("^\d{4} \d{4} \d{4} \d{4}$", credit_card_number).group()) == 19
    provider = Payment(seed=0)
    credit_card_number_with_seed0 = provider.credit_card_number()
    assert credit_card_number_with_seed0 == '4871 4712 4463 6972'
    assert credit_card_number_with_seed0 != credit_card_number