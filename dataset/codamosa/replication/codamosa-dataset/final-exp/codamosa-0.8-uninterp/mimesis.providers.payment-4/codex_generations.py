

# Generated at 2022-06-14 00:36:25.661118
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    import re
    import random
    from collections import defaultdict
    from mimesis.enums import CardType
    from mimesis.random import Mimesis

    r = random.Random()
    pm = Payment(seed=r)
    m = Mimesis(seed=r)
    test_cases = defaultdict(list)

    for _ in range(50):
        ct = CardType(r.choice(['VISA', 'MASTER_CARD', 'AMERICAN_EXPRESS']))
        ccn = pm.credit_card_number(ct)
        test_cases[ct].append(ccn)


# Generated at 2022-06-14 00:36:32.572638
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    card_type = CardType.VISA
    payment = Payment()
    credit_card_number = payment.credit_card_number(card_type)
    expected_length = 16
    expected_first_digit = 4

    assert len(credit_card_number) == expected_length
    assert int(credit_card_number[0]) == expected_first_digit

# Generated at 2022-06-14 00:36:35.660846
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment("en")
    assert len(payment.credit_card_number()) == 19 and payment.credit_card_number().isdigit()

# Generated at 2022-06-14 00:36:48.059619
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    assert payment.credit_card_number(card_type='visa') in ['4042 2459 3874 8409', '4509 4269 6408 6895', '4071 7584 8269 4253', '4617 5155 8392 3667', '4273 1138 8672 7163', '4728 1616 7285 5159', '4365 7349 5785 2933', '4116 2418 3216 1517', '4236 3846 5906 7176', '4830 7281 3813 2722']

# Generated at 2022-06-14 00:36:50.598521
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    from mimesis.enums import CardType
    from mimesis.providers.payment import Payment
    provider = Payment()
    assert len(provider.credit_card_number()) == 19
    assert len(provider.credit_card_number(card_type=CardType.AMERICAN_EXPRESS)) == 18

# Generated at 2022-06-14 00:36:56.502023
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment()
    print(p.credit_card_number(card_type=CardType.VISA))
    print(p.credit_card_number(card_type=CardType.MASTER_CARD))
    print(p.credit_card_number(card_type=CardType.AMERICAN_EXPRESS))

# Generated at 2022-06-14 00:37:03.476157
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    assert len(payment.credit_card_number()) == 19
    assert(len(payment.credit_card_number(CardType.VISA))) == 19
    assert(len(payment.credit_card_number(CardType.MASTER_CARD))) == 19
    assert(len(payment.credit_card_number(CardType.AMERICAN_EXPRESS))) == 17

# Generated at 2022-06-14 00:37:05.397811
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    provider  = Payment(seed = 456)
    assert provider.credit_card_number() == '4455 5299 1152 2450'

# Generated at 2022-06-14 00:37:07.765310
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
	p = Payment()
	assert p.credit_card_number(CardType.Visa) == "4455 5299 1152 2450"

# Generated at 2022-06-14 00:37:19.800104
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """
    Unit test for method credit_card_number of class Payment
    """
    Payment_object = Payment()
    print("\nCredit card number:")
    credit_card_number = Payment_object.credit_card_number()
    print(credit_card_number)
    assert len(credit_card_number) <= 19, "Test failed because expected credit_card_number length\
    is " + str(len(credit_card_number))
    assert credit_card_number[0] in ['4', '5'], "Test failed because expected credit_card_number first\
    character is " + credit_card_number[0]
    print("Length of credit card number : ", len(credit_card_number))
    print("First character of credit card number : ", credit_card_number[0])
    print("Test passed")


# Generated at 2022-06-14 00:37:35.882174
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    # Initialize a Payment object
    payment = Payment('en')
    # Save the credit card number
    n1 = payment.credit_card_number()
    # Save the credit card number with card type MasterCard
    n2 = payment.credit_card_number(CardType.MASTER_CARD)
    print(n1)
    print(n2)

    # The credit card number with card type Visa or MasterCard should be 16 digits
    assert len(n1) == 16
    # The credit card number with card type American Express should be 15 digits
    assert len(n2) == 15

    # Test the American Express card
    n3 = payment.credit_card_number(CardType.AMERICAN_EXPRESS)
    assert len(n3) == 15
    # Save the number without the first two digits

# Generated at 2022-06-14 00:37:38.984442
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Unit test for method credit_card_number of class Payment."""

    obj = Payment()
    assert len(obj.credit_card_number()) == 19


# Generated at 2022-06-14 00:37:48.902138
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    #case 1
    payment = Payment()
    result = payment.credit_card_number(CardType.VISA)
    assert result != None
    #case 2
    payment = Payment()
    result = payment.credit_card_number(CardType.MASTER_CARD)
    assert result != None
    #case 3
    payment = Payment()
    result = payment.credit_card_number(CardType.AMERICAN_EXPRESS)
    assert result != None
    #case 4
    payment = Payment()
    result = payment.credit_card_number(CardType.UNIONPAY)
    assert result == None

# Generated at 2022-06-14 00:38:00.163509
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    from mimesis.enums import CardType
    from mimesis.providers.payment import Payment
    payment = Payment()
    for _ in range(20):
        card_type = get_random_item(CardType, rnd=payment.random)
        card_number = payment.credit_card_number(card_type=card_type)
        if card_type == CardType.VISA:
            assert card_number.startswith("4")
        elif card_type == CardType.MASTER_CARD:
            assert card_number.startswith("2") or card_number.startswith("5")
        elif card_type == CardType.AMERICAN_EXPRESS:
            assert card_number.startswith("34") or card_number.startswith("37")

# Generated at 2022-06-14 00:38:03.155761
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    for i in range(500):
        card_type = get_random_item(CardType, rnd=get_random_item())
        number = Payment().credit_card_number(card_type)
        assert luhn_checksum(number.replace(' ', ''))



# Generated at 2022-06-14 00:38:09.005597
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    test_data = {
        "card_type": CardType.VISA,
        "card_number": "4253 9056 6348 0864"
    }
    payment = Payment()
    assert payment.credit_card_number(test_data['card_type']) == test_data['card_number']

# Generated at 2022-06-14 00:38:19.108781
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():

    import numpy as np
    import pandas as pd

    payment = Payment()
    data_card_type = []
    data_credit_card_number = []

    for i in range(10000):
        card_type = payment.credit_card_network()
        data_card_type.append(card_type)
        data_credit_card_number.append(payment.credit_card_number())

    c = pd.DataFrame({'card_type':data_card_type, 'credit_card_number':data_credit_card_number})
    card_type = ['VISA', 'MasterCard', 'American Express']

# Generated at 2022-06-14 00:38:24.031819
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    card_number_list = []
    for i in range(2):
        for j in range(2):
            for n in range(100):
                card_number_list.append(Payment(seed=n).credit_card_number(card_type=j))
    for i in range(4):
        for n in range(100):
            card_number_list.append(Payment(seed=n).credit_card_number(card_type=i))
    return card_number_list

# Generated at 2022-06-14 00:38:27.512469
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    mp = Payment()
    ccn = mp.credit_card_number()
    assert len(ccn) != 0
    assert ccn[0] == '4' or ccn[0] == '5' or ccn[0] == '3'

# Generated at 2022-06-14 00:38:42.700340
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    Payment = Payment()
    
    card_type_list = [CardType.VISA, CardType.MASTER_CARD, CardType.AMERICAN_EXPRESS]
    
    for _ in range(0, 50):
        card_type = Payment.random.choice(card_type_list)
        number = Payment.credit_card_number(card_type)
        number_int = int(number.replace(" ", ""))
        assert number_int % 10 == 0
        
        if card_type == CardType.VISA:
            assert number_int > 3999 and number_int < 5000
        elif card_type == CardType.MASTER_CARD:
            assert number_int > 2299 and number_int < 2800 or number_int > 5099 and number_int < 5600
        else:
            assert number_

# Generated at 2022-06-14 00:38:56.237541
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    # Initialize a class Payment()
    Payment_obj = Payment()

    # Call the method credit_card_number() of the class Payment()
    # and pass a parameter MasterCard
    Payment_obj.credit_card_number(CardType.MASTER_CARD)

# Generated at 2022-06-14 00:39:00.500942
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment('en')
    # Visa
    payment.credit_card_number(CardType.VISA)

    # American Express
    payment.credit_card_number(CardType.AMERICAN_EXPRESS)

    # Master Card
    payment.credit_card_number(CardType.MASTER_CARD)

# Generated at 2022-06-14 00:39:07.014488
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """
    Test method credit_card_number of class Payment
    :return:
    """
    payment = Payment("en")
    card_type = CardType.VISA
    print("Credit card number: {}".format(payment.credit_card_number(card_type)))



# Generated at 2022-06-14 00:39:15.614276
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    card_generator = Payment()
    card_number = card_generator.credit_card_number()
    last_digit = card_number[-1]
    card_number = card_number[:-1]
    checksum = luhn_checksum(card_number)
    if last_digit == checksum:
        print(card_number)
    else:
        print("There is somthing wrong with credit_card_number()")


# Generated at 2022-06-14 00:39:18.445652
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    number = payment.credit_card_number()
    print(number)


# Generated at 2022-06-14 00:39:23.881169
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    # Initialize a Payment instance
    payment = Payment()
    # Execute
    result = payment.credit_card_number()
    # Assert the result
    assert re.match("^[4-6]{1}[0-9]{15}$", result) is not None

# Generated at 2022-06-14 00:39:28.182547
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment()
    number = p.credit_card_number(CardType.VISA)
    assert re.match(r'^[0-9]{16}$', number)



# Generated at 2022-06-14 00:39:31.661885
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    provider = Payment()
    assert provider.credit_card_number()


# Generated at 2022-06-14 00:39:33.437549
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    provider = Payment()
    assert (provider.credit_card_number() == '4455 5299 1152 2450')

# Generated at 2022-06-14 00:39:41.781772
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    import random
    random.seed(0)

    payment = Payment(seed=0)
    print(payment.credit_card_number())
    print(payment.credit_card_number())
    print(payment.credit_card_number())
    print(payment.credit_card_number())
    print(payment.credit_card_number())
    print(payment.credit_card_number())
    print(payment.credit_card_number())
    print(payment.credit_card_number())
    print(payment.credit_card_number())
    print(payment.credit_card_number())
    print(payment.credit_card_number())
    print(payment.credit_card_number())
    print(payment.credit_card_number())
    print(payment.credit_card_number())

# Generated at 2022-06-14 00:40:09.368761
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    assert Payment().credit_card_number().startswith('4')

# Generated at 2022-06-14 00:40:18.844727
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    def test_Payment_credit_card_number():
       mimesis.providers.payment.Payment.credit_card_number(card_type=None)
    def test_Payment_credit_card_number():
       mimesis.providers.payment.Payment.credit_card_number(card_type=CardType.VISA)
    def test_Payment_credit_card_number():
       mimesis.providers.payment.Payment.credit_card_number(card_type=CardType.MASTER_CARD)
    def test_Payment_credit_card_number():
       mimesis.providers.payment.Payment.credit_card_number(card_type=CardType.AMERICAN_EXPRESS)


# Generated at 2022-06-14 00:40:26.425802
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Unit test for method credit_card_number of class Payment."""
    payment = Payment(seed=42)

    assert payment.credit_card_number(CardType.VISA) == '4455 5299 1152 2450'
    assert payment.credit_card_number(CardType.MASTER_CARD) == '5441 0377 4300 9793'
    assert payment.credit_card_number(CardType.AMERICAN_EXPRESS) == '3764 094007 72936'

# Generated at 2022-06-14 00:40:30.247373
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment(seed=42)
    i=1
    while i<5:
        print(p.credit_card_number())
        i=i+1

if __name__ == '__main__':
    print("This is a module with data related to payment.")

# Generated at 2022-06-14 00:40:31.909039
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment('en')
    assert p.credit_card_number() == '4455 5299 1152 2450'


# Generated at 2022-06-14 00:40:36.661642
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    cardnum = payment.credit_card_number(CardType.VISA)
    if cardnum[0] != '4' or cardnum[1] == '0':
        print("Test failed")
    else:
        print('Test passed')

# Generated at 2022-06-14 00:40:40.220670
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    random = get_random_item(CardType, rnd=Payment.random)
    Pay = Payment()
    print(Pay.credit_card_number(card_type=random))

# Generated at 2022-06-14 00:40:46.617411
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment()
    # when
    actual = payment.credit_card_number(CardType.VISA)
    # then
    assert len(actual) == 19
    assert actual[:2] in ['40', '41', '42', '43', '44', '45', '46', '47', '48', '49']


# Generated at 2022-06-14 00:40:49.430570
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    a = Payment('en')
    print(a.credit_card_number(CardType.AMERICAN_EXPRESS))


# Generated at 2022-06-14 00:40:52.664741
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment('en')
    number = payment.credit_card_number()
    i = 0
    for letter in number:
        if letter in '1234567890':
            i += 1
    assert (i == 16)


# Generated at 2022-06-14 00:41:44.274492
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    # Create an object of Payment class
    number = Payment().credit_card_number()
    # Check that the last digit of number is valid
    # by calculating the Luhn checksum of the first 15 digits
    # and comparing it with the 16th digit
    check = int(number[-1])
    number = number[:-1]
    number = [int(n) for n in number]  # type: ignore
    number = [n * 2 if i % 2 else n for i, n in enumerate(number)]
    number = sum(n - 9 if n > 9 else n for n in number)
    check = (10 - number % 10) % 10
    assert check == int(number[-1]), "using wrong algorithm"



# Generated at 2022-06-14 00:41:48.465479
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    pm = Payment(random_state=1)
    expected_number = "4455 5299 1152 2450"
    assert pm.credit_card_number() == expected_number


# Generated at 2022-06-14 00:41:57.103604
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    """Test method credit_card_number of class Payment."""
    import random
    import pytest

    seed = random.randrange(99999, 999999999)
    cc = Payment(seed=seed)

    assert cc.credit_card_number() in [
        '4455 5299 1152 2450', '5445 4342 6755 1040',
        '5890 4480 4453 6610', '5244 4483 0964 4460',
        '4539 5883 5676 2690', '5543 5146 9584 3200',
    ]

# Generated at 2022-06-14 00:41:59.197271
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    # Initialize the class
    payment = Payment()
    for x in range(10):
        print(payment.credit_card_number())


# Generated at 2022-06-14 00:42:03.373837
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
        payment = Payment(region='uk')
        card_number = payment.credit_card_number()
        # print(card_number)
        assert card_number != '4929341905633167'


# Generated at 2022-06-14 00:42:07.544905
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment()
    for i in range(50):
        card_type = p.random.choice(CardType)
        assert len(p.credit_card_number(card_type)) == 16

# Generated at 2022-06-14 00:42:19.572513
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    payment = Payment('en')
    a = payment.credit_card_number()
    b = payment.credit_card_number(CardType.AMERICAN_EXPRESS)
    c = payment.credit_card_number(CardType.MASTER_CARD)
    d = payment.credit_card_number(CardType.VISA)
    # Verify that each of the card numbers generated are in the correct format
    assert (len(a) == 19 and len(b) == 18 and len(c) == 19 and len(d) == 19)
    assert (a[0:4].isdigit() and c[0:4].isdigit() and d[0:4].isdigit())
    assert (b[0:2].isdigit() and b[2].isspace() and b[3:5].isdigit())
   

# Generated at 2022-06-14 00:42:21.330578
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    p = Payment()
    print(p.credit_card_number())


# Generated at 2022-06-14 00:42:25.212239
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    Payment = Payment('en', seed=0)
    Payment.credit_card_number()

# Generated at 2022-06-14 00:42:32.832079
# Unit test for method credit_card_number of class Payment
def test_Payment_credit_card_number():
    import random
    import mimesis
    provider = mimesis.Generic('en')
    provider.seed(0)
    random.seed(0)
    my_test_dict = {"VISA": 4000, "MASTERCARD": 5100, "AMERICAN EXPRESS": 37}
    for key in my_test_dict:
        card_type = mimesis.enums.CreditCardType[key]
        my_test_dict[key] = provider.payment.credit_card_number(card_type)
    assert my_test_dict == {
            "VISA": "4986 9384 5289 0188",
            "MASTERCARD": "5239 5959 5309 9129",
            "AMERICAN EXPRESS": "3761 7753 96351",
        }