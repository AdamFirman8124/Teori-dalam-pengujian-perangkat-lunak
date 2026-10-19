

# Generated at 2022-06-14 00:36:19.409243
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    Payment_test = Payment()
    for _ in range(4):
        assert Payment_test.credit_card_number() == Payment_test.credit_card_number(), 'Ошибка'


# Generated at 2022-06-14 00:36:25.783098
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Test for method credit_card_number of class Payment.
    """
    payment = Payment()
    assert payment.credit_card_network() == "Visa"
    assert payment.credit_card_expiration_date() == "04/23"
    assert payment.cvv() == 776
    assert payment.paypal() == "pawel@yahoo.com"
    assert payment.bitcoin_address() == "1NT2z2d8sxK9sxUmYgYGZUsbojKwJiHLA2"


# Generated at 2022-06-14 00:36:34.807339
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    card = payment.credit_card_number()
    assert len(card.split()) == 4
    card_AmericanExpress = payment.credit_card_number(CardType.AMERICAN_EXPRESS)
    assert len(card_AmericanExpress.split()) == 3
    assert card.replace(' ', '').isnumeric()
    assert len(card.replace(' ', '')) == 16 or len(card.replace(' ', '')) == 15


# Generated at 2022-06-14 00:36:40.028952
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    assert payment.credit_card_number(CardType.VISA) not in [
        payment.credit_card_number(CardType.MASTER_CARD),
        payment.credit_card_number(CardType.AMERICAN_EXPRESS),
    ]

# Generated at 2022-06-14 00:36:46.485652
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment('en')
    credit_card_number = payment.credit_card_number()
    assert credit_card_number is not None
    assert len(credit_card_number) == 19
    assert credit_card_number.split()[0] > '4000'
    assert credit_card_number.split()[0] < '4999'

# Generated at 2022-06-14 00:37:01.404417
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    test_obj = Payment()
    test_obj.seed(0)
    assert test_obj.credit_card_number() == '4159 8541 0566 7145'
    assert test_obj.credit_card_number(CardType.VISA) == '4348 3293 1429 4932'
    assert test_obj.credit_card_number(CardType.MASTER_CARD) == '5518 4330 1639 7924'
    assert test_obj.credit_card_number(CardType.AMERICAN_EXPRESS) == '3410 044738 92454'


# def test_Payment_credit_card_number_NotEnumerableError():
#     test_obj = Payment()
#     test_obj.seed(0)
#     with pytest.raises(NotImplementedError):
#         test_

# Generated at 2022-06-14 00:37:05.159780
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    print("Test passed!")
    payment = Payment(seed=123)
    p = payment.credit_card_number()
    assert p == '4554 3545 8110 5188'


# Generated at 2022-06-14 00:37:07.613684
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    v = Payment("en", seed=1)
    r = v.credit_card_number()
    assert r == '4017 7234 5612 7770'
    r = v.credit_card_number()
    assert r == '5627 1293 1182 9414'

# Generated at 2022-06-14 00:37:08.985094
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment(seed=42)
    print(p.credit_card_number())

# Generated at 2022-06-14 00:37:18.636391
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()

    # Test all the possible card types
    card_number = payment.credit_card_number(CardType.VISA)
    assert int(card_number[0]) == 4

    card_number = payment.credit_card_number(CardType.MASTER_CARD)
    assert int(card_number[0:2]) in range(22, 28) or int(card_number[0:2]) in range(51, 56)

    card_number = payment.credit_card_number(CardType.AMERICAN_EXPRESS)
    assert int(card_number[0:2]) in range(34, 38)

# Generated at 2022-06-14 00:37:30.751846
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    match = re.compile(r'\d{4}\s\d{4}\s\d{4}\s\d{4}')
    payment = Payment()
    cc_number = payment.credit_card_number()
    assert match.search(cc_number) is not None


# Generated at 2022-06-14 00:37:35.877129
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    print(payment.credit_card_number(CardType.MASTER_CARD))


# Generated at 2022-06-14 00:37:42.329341
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    card_type = CardType.VISA

    def test_visa_1():
        """
        Visa card number should match length '16'
        """
        assert len(payment.credit_card_number(card_type)) == 16

    def test_visa_2():
        """
        Visa card number should start with '4'
        """
        assert payment.credit_card_number(card_type)[0] == '4'

# Generated at 2022-06-14 00:37:47.978180
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    from mimesis.builtins import Payment
    
    card_type = ["MASTER_CARD"]
    for i in range(1000):
        card_type[0] = Payment.Meta.random.choice(["MASTER_CARD"])
        # card_type.append(get_random_item(CardType, rnd=Payment.Meta.random))
        result = Payment.credit_card_number(card_type[0])
        print(result)
        if (result.startswith("2")):
            print(result)


# Generated at 2022-06-14 00:37:59.447593
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Проверка класса Payment.

    Проверка метода credit_card_number.
    """
    from mimesis.enums import CardType
    from mimesis.random import Random
    from mimesis.exceptions import NonEnumerableError
    r = Random()
    p = Payment('en', r.getrandbits(16))
    card_type = CardType.VISA
    result = p.credit_card_number(card_type)
    print('result:', result)
    result = p.credit_card_number()
    print('result:', result)
    card_type = CardType.MASTER_CARD
    result = p.credit_card_number(card_type)

# Generated at 2022-06-14 00:38:07.096946
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    card = payment.credit_card_number(CardType.MASTER_CARD)
    assert len(card) == 19, 'Credit card number should be 19 chars long'
    card = payment.credit_card_number(CardType.AMERICAN_EXPRESS)
    assert len(card) == 17, 'Credit card number should be 17 chars long'
    card = payment.credit_card_number(CardType.VISA)
    assert len(card) == 19, 'Credit card number should be 19 chars long'
    card = payment.credit_card_number()
    assert len(card) == 19, 'Credit card number should be 19 chars long'


# Generated at 2022-06-14 00:38:10.552888
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Test for Payment_credit_card_number."""
    a = Payment(seed=12345)
    card_number = a.credit_card_number()
    assert card_number == "4455 5299 1152 2450"

# Generated at 2022-06-14 00:38:15.979292
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    assert payment.credit_card_number(CardType.VISA) == "4147 1671 4974 0660"
    assert payment.credit_card_number(CardType.MASTER_CARD) == "5288 2794 0241 1778"
    assert payment.credit_card_number(CardType.AMERICAN_EXPRESS) == "3764 499395 17589"


# Generated at 2022-06-14 00:38:18.591332
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    t = Payment()
    result = t.credit_card_number(card_type='Visa')
    print(result)
    # return result


# Generated at 2022-06-14 00:38:21.017717
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    credit_card_network = Payment.credit_card_number(CardType.MASTER_CARD)
    assert isinstance(credit_card_network, str)



# Generated at 2022-06-14 00:38:46.454478
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    VISA = "4039 1779 7085 7635"
    MASTER_CARD = "2221 0297 2452 3139"
    AMERICAN_EXPRESS = "3736 0059 84922"
    payment = Payment()  
    payment.seed(7)  # Always genrate the same random numbers
    #In order to garantee that the test pass everytime, we set a fixed seed for the random number generator
    assert payment.credit_card_number(CardType.VISA) == VISA
    assert payment.credit_card_number(CardType.MASTER_CARD) == MASTER_CARD
    assert payment.credit_card_number(CardType.AMERICAN_EXPRESS) == AMERICAN_EXPRESS
    #The different cards should be the same everytime this test is done

# Generated at 2022-06-14 00:38:51.850563
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment()
    unit_test_result = p.credit_card_number(CardType.VISA)

    assert isinstance(unit_test_result, str)
    assert len(unit_test_result.split(" ")) == 4


# Generated at 2022-06-14 00:38:56.237463
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment()
    CardType = p.CardType
    card_number = p.credit_card_number()
    assert len(card_number.replace(" ", "")) == 16
    card_number = p.credit_card_number(CardType.MASTER_CARD)
    assert len(card_number.replace(" ", "")) == 16
    card_number = p.credit_card_number(CardType.AMERICAN_EXPRESS)
    assert len(card_number.replace(" ", "")) == 15

# Generated at 2022-06-14 00:39:02.886038
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    for i in range(10):
        assert len(Payment().credit_card_number()) == 19 # Should be 16 digits, with 3 spaces
        assert Payment().credit_card_number(CardType.VISA)[0] == '4'
        assert Payment().credit_card_number(CardType.MASTER_CARD)[0] == '2'
        assert Payment().credit_card_number(CardType.AMERICAN_EXPRESS)[0] == '3'
        assert Payment().credit_card_number(CardType.AMERICAN_EXPRESS)[1] in ['3','7']

# Generated at 2022-06-14 00:39:14.591757
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment()
    number_of_test = 10

    # Test Visa card
    card_type = CardType.VISA
    for _ in range(number_of_test):
        card_number = p.credit_card_number(card_type)
        assert card_number[:1] == '4'

    # Test Master
    card_type = CardType.MASTER_CARD
    for _ in range(number_of_test):
        card_number = p.credit_card_number(card_type)
        assert card_number[:2] == '22' or card_number[:4] == '5100'

    # Test American Express
    card_type = CardType.AMERICAN_EXPRESS
    for _ in range(number_of_test):
        card_number = p.credit_card_

# Generated at 2022-06-14 00:39:20.400761
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment()
    assert p.credit_card_number(CardType.VISA)
    assert p.credit_card_number(CardType.MASTER_CARD)
    assert p.credit_card_number(CardType.AMERICAN_EXPRESS)

# Generated at 2022-06-14 00:39:27.776143
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Unit test for method credit_card_number of class Payment."""
    payment = Payment()
    credit_card_number = payment.credit_card_number()
    assert len(credit_card_number) == 19
    assert re.match(r'^[0-9]{4} [0-9]{4} [0-9]{4} [0-9]{4}$', credit_card_number)

# Generated at 2022-06-14 00:39:32.467677
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    card_type_list = ['VISA','MASTER_CARD','AMERICAN_EXPRESS']
    card_type = card_type_list[randint(0,2)]
    res = Payment(seed=1).credit_card_number(card_type=card_type)
    print('\n================\n')
    print(card_type)
    print('\n================\n')
    print(res)
    print('\n================\n')

# Generated at 2022-06-14 00:39:35.692489
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment()
    print(p.credit_card_number())
    print(p.credit_card_number(CardType.MASTER_CARD))
    print(p.credit_card_number(CardType.AMERICAN_EXPRESS))

# Generated at 2022-06-14 00:39:40.359987
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    test = Payment()
    assert(len(test.credit_card_number()) == 19)
    assert(len(test.credit_card_number(CardType.VISA)) == 19)
    assert(len(test.credit_card_number(CardType.MASTER_CARD)) == 19)
    assert(len(test.credit_card_number(CardType.AMERICAN_EXPRESS)) == 17)
