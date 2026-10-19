

# Generated at 2024-06-03 01:32:43.666379
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():    list1 = ImmutableList.of(1, 2, 3)

# Generated at 2024-06-03 01:32:47.708639
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():    # Test case 1: Filter out even numbers from the list
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    result = lst.filter(lambda x: x % 2 != 0)
    expected = ImmutableList.of(1, 3, 5)
    assert result == expected, f"Expected {expected}, but got {result}"

    # Test case 2: Filter out numbers greater than 3
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    result = lst.filter(lambda x: x > 3)
    expected = ImmutableList.of(4, 5)
    assert result == expected, f"Expected {expected}, but got {result}"

    # Test case 3: Filter out all elements (none should pass the filter)

# Generated at 2024-06-03 01:32:50.077934
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():    list1 = ImmutableList.of(1, 2, 3)

# Generated at 2024-06-03 01:32:53.206640
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():    # Test case 1: Finding an element that exists
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    assert lst.find(lambda x: x == 3) == 3

    # Test case 2: Finding an element that does not exist
    assert lst.find(lambda x: x == 6) is None

    # Test case 3: Finding an element in an empty list
    empty_lst = ImmutableList.empty()
    assert empty_lst.find(lambda x: x == 1) is None

    # Test case 4: Finding the first element that matches the condition
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    assert lst.find(lambda x: x > 2) == 3

    # Test case 5: Finding with a complex condition

# Generated at 2024-06-03 01:32:55.704694
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():    list1 = ImmutableList.of(1, 2, 3)

# Generated at 2024-06-03 01:32:59.155538
# Unit test for method __len__ of class ImmutableList
def test_ImmutableList___len__():    # Test case 1: Empty list
    empty_list = ImmutableList.empty()
    assert len(empty_list) == 0

    # Test case 2: List with one element
    single_element_list = ImmutableList.of(1)
    assert len(single_element_list) == 1

    # Test case 3: List with multiple elements
    multiple_elements_list = ImmutableList.of(1, 2, 3, 4)
    assert len(multiple_elements_list) == 4

    # Test case 4: List with nested ImmutableLists
    nested_list = ImmutableList.of(1, ImmutableList.of(2, 3), 4)
    assert len(nested_list) == 3


# Generated at 2024-06-03 01:33:02.185892
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():    # Test case 1: Filtering an empty list
    empty_list = ImmutableList.empty()
    assert empty_list.filter(lambda x: x is not None) == ImmutableList.empty()

    # Test case 2: Filtering a list with no elements passing the filter
    list_with_elements = ImmutableList.of(1, 2, 3)
    assert list_with_elements.filter(lambda x: x > 3) == ImmutableList.empty()

    # Test case 3: Filtering a list with some elements passing the filter
    assert list_with_elements.filter(lambda x: x > 1) == ImmutableList.of(2, 3)

    # Test case 4: Filtering a list with all elements passing the filter
    assert list_with_elements.filter(lambda x: x > 0) == list_with_elements

    # Test case 5: Filtering a list with a complex condition

# Generated at 2024-06-03 01:33:04.708662
# Unit test for method __len__ of class ImmutableList
def test_ImmutableList___len__():    # Test case 1: Empty list
    empty_list = ImmutableList.empty()
    assert len(empty_list) == 0

    # Test case 2: List with one element
    single_element_list = ImmutableList.of(1)
    assert len(single_element_list) == 1

    # Test case 3: List with multiple elements
    multiple_elements_list = ImmutableList.of(1, 2, 3, 4, 5)
    assert len(multiple_elements_list) == 5

    # Test case 4: List with nested ImmutableLists
    nested_list = ImmutableList.of(1, ImmutableList.of(2, 3), 4)
    assert len(nested_list) == 3


# Generated at 2024-06-03 01:33:07.029304
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():    list1 = ImmutableList.of(1, 2, 3)

# Generated at 2024-06-03 01:33:10.211513
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():    # Test case 1: Filter out even numbers from the list
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    filtered_lst = lst.filter(lambda x: x % 2 != 0)
    assert filtered_lst == ImmutableList.of(1, 3, 5)

    # Test case 2: Filter out numbers greater than 3
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    filtered_lst = lst.filter(lambda x: x > 3)
    assert filtered_lst == ImmutableList.of(4, 5)

    # Test case 3: Filter out all elements (none should pass the filter)
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    filtered_lst = lst.filter(lambda x: x > 5)
    assert filtered_lst == ImmutableList.empty()

   

# Generated at 2024-06-03 01:33:26.274558
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():    # Test case 1: Finding an element that exists
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    assert lst.find(lambda x: x == 3) == 3

    # Test case 2: Finding an element that does not exist
    assert lst.find(lambda x: x == 6) is None

    # Test case 3: Finding an element in an empty list
    empty_lst = ImmutableList.empty()
    assert empty_lst.find(lambda x: x == 1) is None

    # Test case 4: Finding the first element
    assert lst.find(lambda x: x == 1) == 1

    # Test case 5: Finding the last element
    assert lst.find(lambda x: x == 5) == 5

    # Test case 6: Finding with a complex condition

# Generated at 2024-06-03 01:33:29.347491
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():    # Test case 1: Filter out even numbers from the list
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    filtered_lst = lst.filter(lambda x: x % 2 != 0)
    assert filtered_lst == ImmutableList.of(1, 3, 5)

    # Test case 2: Filter out numbers greater than 3
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    filtered_lst = lst.filter(lambda x: x > 3)
    assert filtered_lst == ImmutableList.of(4, 5)

    # Test case 3: Filter out all elements (none should pass the filter)
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    filtered_lst = lst.filter(lambda x: x > 5)
    assert filtered_lst == ImmutableList.empty()

   

# Generated at 2024-06-03 01:33:32.242165
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():    # Test case 1: Finding an element that exists
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    assert lst.find(lambda x: x == 3) == 3

    # Test case 2: Finding an element that does not exist
    assert lst.find(lambda x: x == 6) is None

    # Test case 3: Finding an element in an empty list
    empty_lst = ImmutableList.empty()
    assert empty_lst.find(lambda x: x == 1) is None

    # Test case 4: Finding the first element that matches the condition
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    assert lst.find(lambda x: x > 2) == 3

    # Test case 5: Finding an element in a single-element list

# Generated at 2024-06-03 01:33:35.824195
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():    list1 = ImmutableList.of(1, 2, 3)

# Generated at 2024-06-03 01:33:37.757603
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():    list1 = ImmutableList.of(1, 2, 3)

# Generated at 2024-06-03 01:33:40.088349
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():    list1 = ImmutableList.of(1, 2, 3)

# Generated at 2024-06-03 01:33:42.035862
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():    list1 = ImmutableList.of(1, 2, 3)

# Generated at 2024-06-03 01:33:44.420930
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():    list1 = ImmutableList.of(1, 2, 3)

# Generated at 2024-06-03 01:33:46.864336
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():    list1 = ImmutableList.of(1, 2, 3)

# Generated at 2024-06-03 01:33:49.954589
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():    # Test case 1: Filter out even numbers from the list
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    result = lst.filter(lambda x: x % 2 != 0)
    expected = ImmutableList.of(1, 3, 5)
    assert result == expected, f"Expected {expected}, but got {result}"

    # Test case 2: Filter out numbers greater than 3
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    result = lst.filter(lambda x: x > 3)
    expected = ImmutableList.of(4, 5)
    assert result == expected, f"Expected {expected}, but got {result}"

    # Test case 3: Filter out all elements (none should pass the filter)
    lst = ImmutableList.of(1, 2, 3)
    result

# Generated at 2024-06-03 01:34:12.146683
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():    # Test case 1: Finding an element that exists
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    assert lst.find(lambda x: x == 3) == 3

    # Test case 2: Finding an element that does not exist
    assert lst.find(lambda x: x == 6) is None

    # Test case 3: Finding an element in an empty list
    empty_lst = ImmutableList.empty()
    assert empty_lst.find(lambda x: x == 1) is None

    # Test case 4: Finding the first element that matches the condition
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    assert lst.find(lambda x: x > 2) == 3

    # Test case 5: Finding an element in a single-element list

# Generated at 2024-06-03 01:34:14.924415
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():    list1 = ImmutableList.of(1, 2, 3)

# Generated at 2024-06-03 01:34:17.343260
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():    list1 = ImmutableList.of(1, 2, 3)

# Generated at 2024-06-03 01:34:20.674565
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():    # Test case 1: Finding an element that exists
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    assert lst.find(lambda x: x == 3) == 3

    # Test case 2: Finding an element that does not exist
    assert lst.find(lambda x: x == 6) is None

    # Test case 3: Finding an element in an empty list
    empty_lst = ImmutableList.empty()
    assert empty_lst.find(lambda x: x == 1) is None

    # Test case 4: Finding the first element that matches the condition
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    assert lst.find(lambda x: x > 2) == 3

    # Test case 5: Finding an element with a complex condition

# Generated at 2024-06-03 01:34:23.792651
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():    # Test case 1: Filter out even numbers from the list
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    result = lst.filter(lambda x: x % 2 != 0)
    expected = ImmutableList.of(1, 3, 5)
    assert result == expected, f"Expected {expected}, but got {result}"

    # Test case 2: Filter out numbers greater than 3
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    result = lst.filter(lambda x: x > 3)
    expected = ImmutableList.of(4, 5)
    assert result == expected, f"Expected {expected}, but got {result}"

    # Test case 3: Filter out all elements (none should pass the filter)

# Generated at 2024-06-03 01:34:25.873903
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():    list1 = ImmutableList.of(1, 2, 3)

# Generated at 2024-06-03 01:34:28.882018
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():    # Test case 1: Finding an element that exists
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    assert lst.find(lambda x: x == 3) == 3

    # Test case 2: Finding an element that does not exist
    assert lst.find(lambda x: x == 6) is None

    # Test case 3: Finding an element in an empty list
    empty_lst = ImmutableList.empty()
    assert empty_lst.find(lambda x: x == 1) is None

    # Test case 4: Finding the first element
    assert lst.find(lambda x: x == 1) == 1

    # Test case 5: Finding the last element
    assert lst.find(lambda x: x == 5) == 5

    # Test case 6: Finding with a complex condition

# Generated at 2024-06-03 01:34:31.008200
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():    list1 = ImmutableList.of(1, 2, 3)

# Generated at 2024-06-03 01:34:35.304694
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():    # Test case 1: Filter out even numbers from the list
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    filtered_lst = lst.filter(lambda x: x % 2 != 0)
    assert filtered_lst == ImmutableList.of(1, 3, 5)

    # Test case 2: Filter out numbers greater than 3
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    filtered_lst = lst.filter(lambda x: x > 3)
    assert filtered_lst == ImmutableList.of(4, 5)

    # Test case 3: Filter out all elements (none should pass the filter)
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    filtered_lst = lst.filter(lambda x: x > 5)
    assert filtered_lst == ImmutableList.empty()

   

# Generated at 2024-06-03 01:34:38.503954
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():    # Test case 1: Filter out even numbers from the list
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    result = lst.filter(lambda x: x % 2 != 0)
    expected = ImmutableList.of(1, 3, 5)
    assert result == expected, f"Expected {expected}, but got {result}"

    # Test case 2: Filter out numbers greater than 3
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    result = lst.filter(lambda x: x > 3)
    expected = ImmutableList.of(4, 5)
    assert result == expected, f"Expected {expected}, but got {result}"

    # Test case 3: Filter out all elements (none should pass the filter)

# Generated at 2024-06-03 01:35:15.727313
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():    list1 = ImmutableList.of(1, 2, 3)

# Generated at 2024-06-03 01:35:18.910547
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():    # Test case 1: Finding an element that exists
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    assert lst.find(lambda x: x == 3) == 3

    # Test case 2: Finding an element that does not exist
    assert lst.find(lambda x: x == 6) is None

    # Test case 3: Finding an element in an empty list
    empty_lst = ImmutableList.empty()
    assert empty_lst.find(lambda x: x == 1) is None

    # Test case 4: Finding the first element that matches the condition
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    assert lst.find(lambda x: x > 2) == 3

    # Test case 5: Finding with a complex condition

# Generated at 2024-06-03 01:35:21.244568
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():    list1 = ImmutableList.of(1, 2, 3)

# Generated at 2024-06-03 01:35:24.293138
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():    # Test case 1: Filter out even numbers from the list
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    result = lst.filter(lambda x: x % 2 != 0)
    expected = ImmutableList.of(1, 3, 5)
    assert result == expected, f"Expected {expected}, but got {result}"

    # Test case 2: Filter out numbers greater than 2
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    result = lst.filter(lambda x: x > 2)
    expected = ImmutableList.of(3, 4, 5)
    assert result == expected, f"Expected {expected}, but got {result}"

    # Test case 3: Filter out all elements (none should pass the filter)

# Generated at 2024-06-03 01:35:26.756869
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():    list1 = ImmutableList.of(1, 2, 3)

# Generated at 2024-06-03 01:35:30.541703
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():    # Test case 1: Filter out even numbers from the list
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    filtered_lst = lst.filter(lambda x: x % 2 != 0)
    assert filtered_lst == ImmutableList.of(1, 3, 5)

    # Test case 2: Filter out numbers greater than 3
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    filtered_lst = lst.filter(lambda x: x > 3)
    assert filtered_lst == ImmutableList.of(4, 5)

    # Test case 3: Filter out all elements (none should pass the filter)
    lst = ImmutableList.of(1, 2, 3)
    filtered_lst = lst.filter(lambda x: x > 5)
    assert filtered_lst == ImmutableList.empty()

    # Test case 4:

# Generated at 2024-06-03 01:35:34.351598
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():    # Test case 1: Filter out even numbers from the list
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    filtered_lst = lst.filter(lambda x: x % 2 != 0)
    assert filtered_lst == ImmutableList.of(1, 3, 5)

    # Test case 2: Filter out numbers greater than 3
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    filtered_lst = lst.filter(lambda x: x > 3)
    assert filtered_lst == ImmutableList.of(4, 5)

    # Test case 3: Filter out all elements (none should pass the filter)
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    filtered_lst = lst.filter(lambda x: x > 5)
    assert filtered_lst == ImmutableList.empty()

   

# Generated at 2024-06-03 01:35:37.163436
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():    # Test case 1: Filter out even numbers from the list
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    result = lst.filter(lambda x: x % 2 != 0)
    expected = ImmutableList.of(1, 3, 5)
    assert result == expected, f"Expected {expected}, but got {result}"

    # Test case 2: Filter out numbers greater than 2
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    result = lst.filter(lambda x: x > 2)
    expected = ImmutableList.of(3, 4, 5)
    assert result == expected, f"Expected {expected}, but got {result}"

    # Test case 3: Filter out all elements (none should pass the filter)

# Generated at 2024-06-03 01:35:40.162534
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():    # Test case 1: Filter out even numbers from the list
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    result = lst.filter(lambda x: x % 2 != 0)
    expected = ImmutableList.of(1, 3, 5)
    assert result == expected, f"Expected {expected}, but got {result}"

    # Test case 2: Filter out numbers greater than 3
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    result = lst.filter(lambda x: x > 3)
    expected = ImmutableList.of(4, 5)
    assert result == expected, f"Expected {expected}, but got {result}"

    # Test case 3: Filter out all elements (none should pass the filter)
    lst = ImmutableList.of(1, 2, 3)
    result

# Generated at 2024-06-03 01:35:46.300896
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():    # Test case 1: Filter out even numbers from the list
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    filtered_lst = lst.filter(lambda x: x % 2 != 0)
    assert filtered_lst == ImmutableList.of(1, 3, 5)

    # Test case 2: Filter out numbers greater than 3
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    filtered_lst = lst.filter(lambda x: x > 3)
    assert filtered_lst == ImmutableList.of(4, 5)

    # Test case 3: Filter out all elements (none should pass the filter)
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    filtered_lst = lst.filter(lambda x: x > 5)
    assert filtered_lst == ImmutableList.empty()

   

# Generated at 2024-06-03 01:36:59.776213
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():    list1 = ImmutableList.of(1, 2, 3)

# Generated at 2024-06-03 01:37:01.282209
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():    list1 = ImmutableList.of(1, 2, 3)

# Generated at 2024-06-03 01:37:04.022588
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():    # Test case 1: Filter out even numbers from the list
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    result = lst.filter(lambda x: x % 2 != 0)
    expected = ImmutableList.of(1, 3, 5)
    assert result == expected, f"Expected {expected}, but got {result}"

    # Test case 2: Filter out numbers greater than 2
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    result = lst.filter(lambda x: x > 2)
    expected = ImmutableList.of(3, 4, 5)
    assert result == expected, f"Expected {expected}, but got {result}"

    # Test case 3: Filter out all elements (none should pass the filter)

# Generated at 2024-06-03 01:37:06.944905
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():    # Test case 1: Filter out even numbers from the list
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    filtered_lst = lst.filter(lambda x: x % 2 != 0)
    assert filtered_lst == ImmutableList.of(1, 3, 5)

    # Test case 2: Filter out numbers greater than 3
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    filtered_lst = lst.filter(lambda x: x > 3)
    assert filtered_lst == ImmutableList.of(4, 5)

    # Test case 3: Filter out all elements (none should pass the filter)
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    filtered_lst = lst.filter(lambda x: x > 5)
    assert filtered_lst == ImmutableList.empty()

   

# Generated at 2024-06-03 01:37:10.087255
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():    # Test case 1: Filter out even numbers from the list
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    filtered_lst = lst.filter(lambda x: x % 2 != 0)
    assert filtered_lst == ImmutableList.of(1, 3, 5)

    # Test case 2: Filter out numbers greater than 3
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    filtered_lst = lst.filter(lambda x: x > 3)
    assert filtered_lst == ImmutableList.of(4, 5)

    # Test case 3: Filter out all elements (none should pass the filter)
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    filtered_lst = lst.filter(lambda x: x > 5)
    assert filtered_lst == ImmutableList.empty()

   

# Generated at 2024-06-03 01:37:13.176779
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():    # Test case 1: Filtering an empty list
    empty_list = ImmutableList.empty()
    assert empty_list.filter(lambda x: x is not None) == ImmutableList.empty()

    # Test case 2: Filtering a list with no elements passing the filter
    list_with_elements = ImmutableList.of(1, 2, 3)
    assert list_with_elements.filter(lambda x: x > 3) == ImmutableList.empty()

    # Test case 3: Filtering a list with some elements passing the filter
    assert list_with_elements.filter(lambda x: x > 1) == ImmutableList.of(2, 3)

    # Test case 4: Filtering a list with all elements passing the filter
    assert list_with_elements.filter(lambda x: x > 0) == list_with_elements

    # Test case 5: Filtering a list with a complex condition

# Generated at 2024-06-03 01:37:15.997299
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():    # Test case 1: Filter out even numbers from the list
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    result = lst.filter(lambda x: x % 2 != 0)
    expected = ImmutableList.of(1, 3, 5)
    assert result == expected, f"Expected {expected}, but got {result}"

    # Test case 2: Filter out numbers greater than 3
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    result = lst.filter(lambda x: x > 3)
    expected = ImmutableList.of(4, 5)
    assert result == expected, f"Expected {expected}, but got {result}"

    # Test case 3: Filter out all elements (none should pass the filter)

# Generated at 2024-06-03 01:37:18.546902
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():    list1 = ImmutableList.of(1, 2, 3)

# Generated at 2024-06-03 01:37:21.216771
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():    # Test case 1: Filter out even numbers from the list
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    result = lst.filter(lambda x: x % 2 != 0)
    expected = ImmutableList.of(1, 3, 5)
    assert result == expected, f"Expected {expected}, but got {result}"

    # Test case 2: Filter out numbers greater than 3
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    result = lst.filter(lambda x: x > 3)
    expected = ImmutableList.of(4, 5)
    assert result == expected, f"Expected {expected}, but got {result}"

    # Test case 3: Filter out all elements (none should pass the filter)

# Generated at 2024-06-03 01:37:23.178037
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():    list1 = ImmutableList.of(1, 2, 3)

# Generated at 2024-06-03 01:39:48.958087
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():    # Test case 1: Filter out even numbers from the list
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    result = lst.filter(lambda x: x % 2 != 0)
    expected = ImmutableList.of(1, 3, 5)
    assert result == expected, f"Expected {expected}, but got {result}"

    # Test case 2: Filter out numbers greater than 3
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    result = lst.filter(lambda x: x > 3)
    expected = ImmutableList.of(4, 5)
    assert result == expected, f"Expected {expected}, but got {result}"

    # Test case 3: Filter out all elements (none should pass the filter)

# Generated at 2024-06-03 01:39:51.814690
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():    # Test case 1: Finding an element that exists
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    assert lst.find(lambda x: x == 3) == 3

    # Test case 2: Finding an element that does not exist
    assert lst.find(lambda x: x == 6) is None

    # Test case 3: Finding an element in an empty list
    empty_lst = ImmutableList.empty()
    assert empty_lst.find(lambda x: x == 1) is None

    # Test case 4: Finding the first element that matches the condition
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    assert lst.find(lambda x: x > 2) == 3

    # Test case 5: Finding with a complex condition

# Generated at 2024-06-03 01:39:55.220527
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():    # Test case 1: Finding an element that exists
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    assert lst.find(lambda x: x == 3) == 3

    # Test case 2: Finding an element that does not exist
    assert lst.find(lambda x: x == 6) is None

    # Test case 3: Finding an element in an empty list
    empty_lst = ImmutableList.empty()
    assert empty_lst.find(lambda x: x == 1) is None

    # Test case 4: Finding the first element
    assert lst.find(lambda x: x == 1) == 1

    # Test case 5: Finding the last element
    assert lst.find(lambda x: x == 5) == 5

    # Test case 6: Finding with a complex condition

# Generated at 2024-06-03 01:39:57.996503
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():    # Test case 1: Filter out even numbers from the list
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    result = lst.filter(lambda x: x % 2 != 0)
    expected = ImmutableList.of(1, 3, 5)
    assert result == expected, f"Expected {expected}, but got {result}"

    # Test case 2: Filter out numbers greater than 3
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    result = lst.filter(lambda x: x > 3)
    expected = ImmutableList.of(4, 5)
    assert result == expected, f"Expected {expected}, but got {result}"

    # Test case 3: Filter out all elements (none should pass the filter)

# Generated at 2024-06-03 01:40:01.005663
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():    # Test case 1: Filter out even numbers from the list
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    result = lst.filter(lambda x: x % 2 != 0)
    expected = ImmutableList.of(1, 3, 5)
    assert result == expected, f"Expected {expected}, but got {result}"

    # Test case 2: Filter out numbers greater than 3
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    result = lst.filter(lambda x: x > 3)
    expected = ImmutableList.of(4, 5)
    assert result == expected, f"Expected {expected}, but got {result}"

    # Test case 3: Filter out all elements (none should pass the filter)

# Generated at 2024-06-03 01:40:03.996829
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():    # Test case 1: Finding an element that exists
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    assert lst.find(lambda x: x == 3) == 3

    # Test case 2: Finding an element that does not exist
    assert lst.find(lambda x: x == 6) is None

    # Test case 3: Finding an element in an empty list
    empty_lst = ImmutableList.empty()
    assert empty_lst.find(lambda x: x == 1) is None

    # Test case 4: Finding the first element
    assert lst.find(lambda x: x == 1) == 1

    # Test case 5: Finding the last element
    assert lst.find(lambda x: x == 5) == 5

    # Test case 6: Finding with a complex condition

# Generated at 2024-06-03 01:40:06.089411
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():    list1 = ImmutableList.of(1, 2, 3)

# Generated at 2024-06-03 01:40:08.117736
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():    list1 = ImmutableList.of(1, 2, 3)

# Generated at 2024-06-03 01:40:09.878478
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():    list1 = ImmutableList.of(1, 2, 3)

# Generated at 2024-06-03 01:40:12.913867
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():    # Test case 1: Filter out even numbers from the list
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    result = lst.filter(lambda x: x % 2 != 0)
    expected = ImmutableList.of(1, 3, 5)
    assert result == expected, f"Expected {expected}, but got {result}"

    # Test case 2: Filter out numbers greater than 2
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    result = lst.filter(lambda x: x > 2)
    expected = ImmutableList.of(3, 4, 5)
    assert result == expected, f"Expected {expected}, but got {result}"

    # Test case 3: Filter out all elements (none should pass the filter)