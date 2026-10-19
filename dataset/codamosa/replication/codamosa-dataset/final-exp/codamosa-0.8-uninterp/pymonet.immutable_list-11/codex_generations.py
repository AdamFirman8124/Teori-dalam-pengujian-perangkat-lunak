

# Generated at 2022-06-14 03:16:50.808521
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList() == ImmutableList()

    assert not (ImmutableList() != ImmutableList())
    assert ImmutableList(2, ImmutableList(3)) != ImmutableList(3, ImmutableList(4))
    assert ImmutableList(2, ImmutableList(3)) != ImmutableList(2, ImmutableList())

    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))) == ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))) != ImmutableList(1, ImmutableList(3, ImmutableList(3)))
    assert ImmutableList(2, ImmutableList(3)) == ImmutableList(2, ImmutableList(3))

# Generated at 2022-06-14 03:16:51.547738
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    asse

# Generated at 2022-06-14 03:16:55.922469
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    data = list(range(10))
    filtered = ImmutableList.of(*data).filter(lambda x: x % 2 == 0)
    assert len(filtered) == 5
    assert filtered.to_list() == list(range(10))[::2]


# Generated at 2022-06-14 03:17:00.678980
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList(1).find(lambda i: i > 100) == None
    assert ImmutableList(1).find(lambda i: i < 100) == 1
    assert ImmutableList(9, ImmutableList(1)).find(lambda i: i > 5) == 9
    assert ImmutableList(9, ImmutableList(1)).find(lambda i: i < 5) == 1


# Generated at 2022-06-14 03:17:04.555061
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    list_ = ImmutableList.of(1, 2, 3, 4, 5, 6, 7, 8, 9)
    assert list_.find(lambda v: v > 7) == 8
    assert list_.find(lambda v: v == 3) == 3
    assert list_.find(lambda v: v > 10) is None



# Generated at 2022-06-14 03:17:16.729011
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    a = ImmutableList(1, ImmutableList(2, ImmutableList(3, ImmutableList(4))))
    b = ImmutableList(1, ImmutableList(2, ImmutableList(3, ImmutableList(4))))
    c = ImmutableList(1, ImmutableList(2, ImmutableList(3, ImmutableList(5))))
    d = ImmutableList(1, ImmutableList(2))

    assert (a == b)
    assert (not (a == c))
    assert (not (c == d))
    assert (a != c)
    assert (not (a != b))
    assert (not (a != d))

# Generated at 2022-06-14 03:17:25.364516
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.empty().filter(lambda x: x % 2 == 0) == ImmutableList()

    assert ImmutableList.of(
        1, 2, 3, 4
    ).filter(lambda x: x % 2 == 0) == ImmutableList(
            2, 4
    )

    assert ImmutableList.of(
        1, 2, 3, 4
    ).filter(lambda x: x % 2 == 1) == ImmutableList(
            1, 3
    )

    assert ImmutableList.of(
        1, 2, 3, 4
    ).filter(lambda x: x % 2 == 3) == ImmutableList(
            is_empty=True
    )



# Generated at 2022-06-14 03:17:33.543376
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList(4, ImmutableList(8, ImmutableList(15, ImmutableList(16, ImmutableList(23, ImmutableList(42, is_empty=True)))))).__eq__(
        ImmutableList(4, ImmutableList(8, ImmutableList(15, ImmutableList(16, ImmutableList(23, ImmutableList(42, is_empty=True)))))))

# Generated at 2022-06-14 03:17:38.686040
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList().filter(lambda i: i % 2 == 0) == ImmutableList(is_empty=True)

    assert ImmutableList().filter(lambda i: i % 2 != 0) == ImmutableList(is_empty=True)

    assert ImmutableList.empty().filter(lambda i: i % 2 == 0) == ImmutableList(is_empty=True)

    assert ImmutableList.empty().filter(lambda i: i % 2 != 0) == ImmutableList(is_empty=True)

    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))).filter(lambda i: i % 2 == 0) == ImmutableList(2)


# Generated at 2022-06-14 03:17:45.881429
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3, 4, 5, 6, 7, 8, 9).filter(lambda x: x % 2 == 0) == ImmutableList.of(2, 4, 6, 8)
    assert ImmutableList.of(1, 2, 3, 4, 5, 6, 7, 8, 9).filter(lambda x: x < 4) == ImmutableList.of(1, 2, 3)
    assert ImmutableList.of(1, 2, 3, 4, 5, 6, 7, 8, 9).filter(lambda x: x % 5 == 0) == ImmutableList.of(5)

    assert ImmutableList.of("A", "B", "C", "D", "E").filter(lambda x: x == "A") == ImmutableList.of("A")

# Generated at 2022-06-14 03:17:52.797612
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3, is_empty=True))) \
           .filter(lambda x: x % 2 == 1) \
           == ImmutableList(1, ImmutableList(3))



# Generated at 2022-06-14 03:18:03.047810
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    def is_even(a: int) -> bool:
        return a % 2 == 0

    assert ImmutableList.of(2).filter(is_even) == ImmutableList.of(2)
    assert ImmutableList.of(1).filter(is_even) == ImmutableList.empty()
    assert ImmutableList.of(1, 2, 3, 4).filter(is_even) == ImmutableList.of(2, 4)
    assert ImmutableList.of(1, 3, 5, 7).filter(is_even) == ImmutableList.empty()

# Generated at 2022-06-14 03:18:13.633802
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 2, 3, 4).filter(lambda x: x > 3).to_list() == [4]
    assert ImmutableList.of(1, 2, 3, 4).filter(lambda x: x % 2 != 0).to_list() == [1, 3]
    assert ImmutableList.of(1, 2, 3, 3, 3).filter(lambda x: x == 3).to_list() == [3, 3, 3]
    assert ImmutableList.of(1).filter(lambda x: x > 3).to_list() == []


# Generated at 2022-06-14 03:18:19.970734
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():  # pragma: no cover
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))).find(lambda x: x == 2) == 2
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))).find(lambda x: x == 3) == 3
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))).find(lambda x: x == 4) is None
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))).find(lambda x: x == 1) == 1


# Generated at 2022-06-14 03:18:27.621688
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    container = ImmutableList.of(1, 2, 4, 5, 6)
    assert container.find(lambda x: x == 1) == 1
    assert container.find(lambda x: x == 2) == 2
    assert container.find(lambda x: x == 4) == 4
    assert container.find(lambda x: x == 5) == 5
    assert container.find(lambda x: x == 6) == 6
    assert container.find(lambda x: x == 3) == None


# Generated at 2022-06-14 03:18:30.594091
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    myList = ImmutableList.of(1, 2, 3, 4, 5)
    output = myList.filter(lambda x: x > 3)
    expected = ImmutableList.of(4, 5)

    assert expected == output


# Generated at 2022-06-14 03:18:42.194863
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3, 4, 5).filter(lambda x: x % 2 == 0).to_list() == [2, 4]
    assert ImmutableList.of(1, 2, 3, 4, 5).filter(lambda x: x > 3).to_list() == [4, 5]

    assert ImmutableList.of(1, 2, 3, 4, 5).filter(lambda x: x % 2 == 0)\
     .filter(lambda x: x > 3).to_list() == [4]
    
    assert ImmutableList.of(1, 2, 3, 4, 5).filter(lambda x: x % 2 == 0)\
     .filter(lambda x: x > 3).filter(lambda x: x > 5)\
     .to_list() == []


# Generated at 2022-06-14 03:18:47.835564
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    instance = ImmutableList.of(1, 2, 3, 4)
    filtered_instance = instance.filter(lambda value: value % 2 == 0)
    assert filtered_instance.to_list() == [2, 4]



# Generated at 2022-06-14 03:18:58.091142
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # given
    given_list = ImmutableList.of(1, 2, 3, 4, 5, 6)

    # when
    result = given_list.find(lambda x: x == 4)

    # then
    assert result == 4



# Generated at 2022-06-14 03:19:03.264037
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    list = ImmutableList.of(1, 2, 3, 4)
    filtered_list = list.filter(lambda element: element % 2 == 0)

    assert filtered_list == ImmutableList.of(2, 4)


# Generated at 2022-06-14 03:19:13.509791
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    values = ImmutableList.of(1, 2, 3, 4, 5)
    filtred_values = values.filter(lambda x: x % 2 == 0)
    expected = ImmutableList.of(2, 4)
    assert filtred_values == expected


# Generated at 2022-06-14 03:19:15.237221
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3)\
        .filter(lambda x: x == 2)\
        == ImmutableList.of(2)

# Generated at 2022-06-14 03:19:21.643403
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    first_array = [
        {'name': 'John', 'age': 20},
        {'name': 'Joe', 'age': 10},
        {'name': 'Sam', 'age': 15},
        {'name': 'Taylor', 'age': 30},
    ]

    expected_array = [
        {'name': 'John', 'age': 20},
        {'name': 'Taylor', 'age': 30},
    ]

    result = ImmutableList.of(*first_array)\
        .filter(lambda elem: elem['age'] > 15)

    assert result.to_list() == expected_array


# Generated at 2022-06-14 03:19:32.964481
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x == 3 ) == 3
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x > 3 ) == 4
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x < 3 ) == 1
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x == 0 ) is None
    assert ImmutableList.of(1).find(lambda x: x == 1 ) == 1
    assert ImmutableList.of(1).find(lambda x: x == 2 ) is None
    assert ImmutableList.of().find(lambda x: x == 1 ) is None

# Generated at 2022-06-14 03:19:38.704651
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3, 4, 5, 6, 7, 8).filter(lambda x: x % 2 == 0) == \
        ImmutableList.of(2, 4, 6, 8)

# Generated at 2022-06-14 03:19:48.878757
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    list1 = ImmutableList.empty()
    assert list1.filter(lambda x: x < 2) == ImmutableList()

    list2 = ImmutableList.of(1, 2, 3, 4)
    assert list2.filter(lambda x: x < 2) == ImmutableList(1)

    list3 = ImmutableList.of(1, 2, 3, 4)
    assert list3.filter(lambda x: x < 2 or x > 3) == ImmutableList(1, 4)

    list4 = ImmutableList.of(1, 2, 3, 4)
    assert list4.filter(lambda x: x > 4) == ImmutableList.empty()

# Generated at 2022-06-14 03:20:03.499039
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of('a', 'b', 'c').filter(lambda x: x != 'b') == ImmutableList.of('a', 'c')
    assert ImmutableList.of(1, 2, 3, 4).filter(lambda x: x > 3) == ImmutableList.of(4)
    assert ImmutableList.of(1, 2, 3, 4).filter(lambda x: x > 5) == ImmutableList.empty()
    assert ImmutableList.of().filter(lambda x: x != 'a') == ImmutableList.empty()
    assert ImmutableList.of('b', 'c').filter(lambda x: x != 'b') == ImmutableList.of('c')
    assert ImmutableList.empty().filter(lambda x: x != 'a') == ImmutableList.empty()
    assert ImmutableList.of

# Generated at 2022-06-14 03:20:05.463299
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    d = ImmutableList.of(1, 2, 3)
    assert d.find(lambda x: x == 2) == 2
test_ImmutableList_find()


# Generated at 2022-06-14 03:20:08.706747
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # given
    list = ImmutableList.of(1, 2, 3, 4, 5, 6)

    # when
    found_element = list.find(lambda x: x > 3)

    # then
    assert found_element == 4


# Generated at 2022-06-14 03:20:13.253999
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    test_list = ImmutableList.of(1, 2, 3, 4, 5)
    assert test_list.find(lambda x: x > 3) == 4

# Generated at 2022-06-14 03:20:35.239988
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    def _is_even(element: int) -> bool:
        return element % 2 == 0

    assert ImmutableList.of(1, 3, 7, 11).filter(_is_even).to_list() == []
    assert ImmutableList.of(2, 4, 6, 9).filter(_is_even).to_list() == [2, 4, 6]
    assert ImmutableList.of(1, 4, 7).filter(_is_even).to_list() == [4]
    assert ImmutableList.of(2, 4, 6).filter(_is_even).to_list() == [2, 4, 6]
    assert ImmutableList.of(2, 4, 6).filter(_is_even).to_list() == [2, 4, 6]

# Generated at 2022-06-14 03:20:41.263982
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    list1 = ImmutableList.of(1, 32, 23, 45, 41, 54)
    result1 = list1.filter(lambda e: e % 2 == 0)
    assert ImmutableList.of(32, 54) == result1

    list2 = ImmutableList.of(21, 23, 54, 12, 10, 543)
    result2 = list2.filter(lambda e: e % 2 == 0)
    assert ImmutableList.of(54, 12, 10) == result2



# Generated at 2022-06-14 03:20:50.581499
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3, 4, 5).filter(lambda v: v <= 4) == ImmutableList.of(1, 2, 3, 4)
    assert ImmutableList.of(1, 2, 3, 4, 5).filter(lambda v: v <= 0) == ImmutableList.empty()
    assert ImmutableList.of(1, 2, 3, 4, 5).filter(lambda v: v <= 5) == ImmutableList.of(1, 2, 3, 4, 5)
    assert ImmutableList.of(1, 2, 3, 4, 5).filter(lambda v: v <= 6) == ImmutableList.of(1, 2, 3, 4, 5)
    assert ImmutableList.empty().filter(lambda v: v <= 4) == ImmutableList.empty()

# Generated at 2022-06-14 03:20:53.587144
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    list1 = ImmutableList.of(4, 5, 9)
    assert list1.find(lambda x: x % 2 == 0) == 4
    assert list1.find(lambda x: x % 5 == 0) == 5
    assert list1.find(lambda x: x % 10 == 0) == None


# Generated at 2022-06-14 03:20:56.664717
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    first_test = ImmutableList.of(1, 2, 3)

    second_test = first_test.find(lambda x: x == 3)

    assert second_test == 3


# Generated at 2022-06-14 03:21:00.410189
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # Setup
    input_list = ImmutableList.of(1, 2, 3, 4, 5)

    # Exercise
    output = input_list.find(lambda x: x == 3)

    # Verify
    assert output == 3



# Generated at 2022-06-14 03:21:03.326761
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3, 4).filter(lambda x: x % 2 == 0) == ImmutableList.of(2, 4)
    assert ImmutableList.of(1, 2, 3, 4).filter(lambda x: x % 2 == 1) == ImmutableList.of(1, 3)


# Generated at 2022-06-14 03:21:06.513049
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    array = [0, 1, 2, 3, 4, 4, 5, 10]
    example = ImmutableList.of(*array)
    assert example.filter(lambda x: x > 3).to_list() == [4, 4, 5, 10]

# Generated at 2022-06-14 03:21:10.642892
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    def is_even(number):
        return number % 2 == 0

    list_of_numbers = ImmutableList.of(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    even_numbers = ImmutableList.of(2, 4, 6, 8, 10)

    assert list_of_numbers.filter(is_even) == even_numbers



# Generated at 2022-06-14 03:21:14.647207
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1).find(lambda x: x == 1) == 1
    assert ImmutableList.of(2, 3, 4).find(lambda x: x == 3) == 3
    assert ImmutableList.of(2, 3, 4).find(lambda x: x == 5) is None

# Generated at 2022-06-14 03:21:45.046320
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1,2).find(lambda x: x == 2) == 2
    assert ImmutableList.empty().find(lambda x: x == 2) is None
    assert ImmutableList.of(1,2,3,4,5).find(lambda x: x % 2 == 0) == 2



# Generated at 2022-06-14 03:21:57.929923
# Unit test for method filter of class ImmutableList

# Generated at 2022-06-14 03:22:03.942150
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert type(ImmutableList()) is ImmutableList

    my_list = ImmutableList(1, ImmutableList(2, ImmutableList(3, ImmutableList(4))))
    assert my_list.find(lambda x: x == 3) == 3
    assert my_list.find(lambda x: x < 3) == 1
    assert my_list.find(lambda x: x > 10) is None


# Generated at 2022-06-14 03:22:15.921800
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.empty().find(lambda el: True) is None
    assert ImmutableList.of(4, 5, 6).find(lambda el: True) == 4
    assert ImmutableList.of(4, 5, 6).find(lambda el: el == 5) == 5
    assert ImmutableList.of(4, 5, 6).find(lambda el: el % 2 == 0) == 4
    assert ImmutableList.of(4, 7, 6).find(lambda el: el % 2 == 0) == 4
    assert ImmutableList.of(4, 7, 6).find(lambda el: el % 2 == 0) == 4
    assert ImmutableList.of(4, 7, 6).find(lambda el: el % 2 == 0) == 4


# Generated at 2022-06-14 03:22:27.498178
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(5, 4, 3, 2, 1).filter(lambda x: x > 2) == ImmutableList.of(5, 4, 3)
    assert ImmutableList.of(
        ImmutableList.of(1, 2, 3),
        ImmutableList.of(4, 5, 6)
    ).filter(lambda x: True) == ImmutableList.of(
        ImmutableList.of(1, 2, 3),
        ImmutableList.of(4, 5, 6)
    )

# Generated at 2022-06-14 03:22:38.148024
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.empty().find(lambda _: True) is None

    assert ImmutableList.of(1, 2, 3).find(lambda _: True) == 1

    assert ImmutableList.of(1, 2, 3).find(lambda _: False) == None

    assert ImmutableList.of(1, 2, 3).find(lambda i: i == 2) == 2

    assert ImmutableList.of(1, 2, 3).find(lambda i: i > 2) == 3

    assert ImmutableList.of(1, 2, 3).find(lambda i: i < 1) == None

    assert ImmutableList.of(1, 2, 3, 4).find(lambda i: i < 3) == 1



# Generated at 2022-06-14 03:22:41.232508
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    il1 = ImmutableList.of(1, 2, 3)
    il2 = il1.filter(lambda x: x % 2 == 0)
    assert il2 == ImmutableList.of(2)


# Generated at 2022-06-14 03:22:47.441871
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    list_to_filter = ImmutableList(
        'a',
        ImmutableList('b', ImmutableList('c', ImmutableList('d')))
    )

    assert list_to_filter.filter(
        lambda el: el != 'c'
    ) == ImmutableList(
        'a',
        ImmutableList('b', ImmutableList('d'))
    )


# Generated at 2022-06-14 03:22:54.140757
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    list_ = ImmutableList.of(1, 2, 3, 4).filter(lambda v: v == 2)
    assert list_ == ImmutableList.of(2) 

    list_ = ImmutableList.empty().filter(lambda v: v == 2)
    assert list_ == ImmutableList.of(is_empty=True) 

    list_ = ImmutableList.of(1, 2, 3, 4).filter(lambda v: v == 9)
    assert list_ == ImmutableList.of(is_empty=True) 




# Generated at 2022-06-14 03:23:02.593230
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    list_without_elements = ImmutableList(is_empty=True)
    assert list_without_elements.find(lambda x: True) is None

    list_with_one_element = ImmutableList.of(1)
    assert list_with_one_element.find(lambda x: True) == 1

    list_with_two_elements = ImmutableList.of(1, 2)
    assert list_with_two_elements.find(lambda x: x == 2) == 2

    list_with_three_elements = ImmutableList.of(1, 2, 3)
    assert list_with_three_elements.find(lambda x: x == 7) is None



# Generated at 2022-06-14 03:24:08.557455
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1).find(lambda x: x == 1) == 1
    assert ImmutableList.of(1).find(lambda x: x == 2) is None
    assert ImmutableList.of(2, 3).find(lambda x: x == 2) == 2
    assert ImmutableList.of(2, 3).find(lambda x: x == 3) == 3
    assert ImmutableList.of(2, 3).find(lambda x: x == 4) is None
    assert ImmutableList.of(2, 3, 4).find(lambda x: x == 4) == 4
    assert ImmutableList.of(2, 3, 4).find(lambda x: x <= 3) == 2
    assert ImmutableList.of(2, 3, 4).find(lambda x: x <= 5) == 2
    assert ImmutableList

# Generated at 2022-06-14 03:24:12.360806
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # Given
    list = ImmutableList.of(1, 2, 3, 4, 5, 6)

    # When
    res = list.find(lambda x: x == 3)

    # Then
    assert res == 3

# Generated at 2022-06-14 03:24:19.148862
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.empty().filter(bool) == ImmutableList.empty()
    assert ImmutableList(0).filter(bool) == ImmutableList.empty()
    assert ImmutableList(1).filter(bool) == ImmutableList(1)
    assert ImmutableList(0, 1, 2, 3).filter(bool) == ImmutableList(1, 2, 3)
    assert ImmutableList(0, 0, 2, 3).filter(bool) == ImmutableList(2, 3)



# Generated at 2022-06-14 03:24:22.926972
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    test_list = ImmutableList.of(1, 2, 3, 4)
    assert test_list.filter(lambda x: x % 2 == 0) == ImmutableList.of(2, 4)

# Generated at 2022-06-14 03:24:29.581570
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3, 4, 5, 6, 7, 8, 9).find(lambda x: x % 2 == 0) == 2
    assert ImmutableList.of(1, 2, 3, 4, 5, 6, 7, 8, 9).find(lambda x: x % 3 == 0) == 3
    assert ImmutableList.of(1, 2, 3, 4, 5, 6, 7, 8, 9).find(lambda x: x == 10) is None

# Generated at 2022-06-14 03:24:35.241919
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(2, 3, 4, 6, 8, 9) == ImmutableList(2, ImmutableList(3, ImmutableList(4, ImmutableList(6, ImmutableList(8, ImmutableList(9))))))
    assert ImmutableList.of(3, 6, 9) == ImmutableList(2, ImmutableList(3, ImmutableList(4, ImmutableList(6, ImmutableList(8, ImmutableList(9))))))\
        .filter(lambda x: x % 3 == 0)


if __name__ == "__main__":
    test_ImmutableList_filter()

# Generated at 2022-06-14 03:24:38.241238
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    """
    This test should pass if you correctly implemented ImmutableList filter method

    :returns: None
    :raises: AssertionError
    """
    assert ImmutableList.of(1, 2).filter(lambda x: x == 1) == ImmutableList.of(1) == ImmutableList(1, ImmutableList.empty())



# Generated at 2022-06-14 03:24:42.592980
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    list_ = ImmutableList.of(1, 2, 3, 4, 5)
    filtered_list = list_.filter(lambda x: x % 2 == 0)

    assert filtered_list == ImmutableList.of(2, 4)


# Generated at 2022-06-14 03:24:53.960434
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList().filter(lambda x: x != 10) == ImmutableList(is_empty=True)
    assert ImmutableList(10).filter(lambda x: x != 10) == ImmutableList(is_empty=True)
    assert ImmutableList(10).filter(lambda x: x == 10) == ImmutableList(10)
    assert ImmutableList(10, ImmutableList(20, ImmutableList(30, ImmutableList(10)))).filter(lambda x: x % 10 == 0) == ImmutableList(10, ImmutableList(30, ImmutableList(10)))
    assert ImmutableList(10, ImmutableList(20, ImmutableList(30, ImmutableList(10)))).filter(lambda x: x % 10 != 0) == ImmutableList(20)


# Generated at 2022-06-14 03:25:01.472379
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    list_even = ImmutableList.of(2, 4, 6, 8)
    list_odd = ImmutableList.of(1, 3, 5, 7, 9)

    assert list_even.find(lambda v: v % 2 == 0) == 2
    assert list_even.find(lambda v: v % 2 == 1) == None
    assert list_even.find(lambda v: v > 10) == None
    
    assert list_odd.find(lambda v: v % 2 == 1) == 1
    assert list_odd.find(lambda v: v % 2 == 0) == None
    assert list_odd.find(lambda v: v > 10) == None