

# Generated at 2024-03-18 05:32:48.654110
# Unit test for function has_callables
def test_has_callables():    assert has_callables(dict, 'get', 'keys', 'items', 'values')

# Generated at 2024-03-18 05:32:54.648350
# Unit test for function has_any_callables
def test_has_any_callables():    assert has_any_callables(dict, 'get', 'keys', 'items', 'values') is True

# Generated at 2024-03-18 05:32:58.537002
# Unit test for function has_callables
def test_has_callables():    assert has_callables(dict, 'get', 'keys', 'items', 'values')

# Generated at 2024-03-18 05:33:02.657109
# Unit test for function has_callables
def test_has_callables():    assert has_callables(dict, 'get', 'keys', 'items', 'values')

# Generated at 2024-03-18 05:33:07.974509
# Unit test for function has_callables
def test_has_callables():    assert has_callables(dict, 'get', 'keys', 'items', 'values')

# Generated at 2024-03-18 05:33:14.861086
# Unit test for function has_any_callables
def test_has_any_callables():    assert has_any_callables(dict, 'get', 'keys', 'items', 'values') is True

# Generated at 2024-03-18 05:33:20.000758
# Unit test for function has_any_callables
def test_has_any_callables():    assert has_any_callables(dict, 'get', 'keys', 'items', 'values') is True

# Generated at 2024-03-18 05:33:24.507060
# Unit test for function has_callables
def test_has_callables():    assert has_callables(dict, 'get', 'keys', 'items', 'values')

# Generated at 2024-03-18 05:33:34.429053
# Unit test for function has_any_attrs
def test_has_any_attrs():    assert has_any_attrs(dict(), 'get', 'keys', 'items', 'values', 'something') is True

# Generated at 2024-03-18 05:33:43.022735
# Unit test for function has_any_attrs
def test_has_any_attrs():    assert has_any_attrs(dict(), 'get', 'keys', 'items', 'values', 'something') is True

# Generated at 2024-03-18 05:33:53.277593
# Unit test for function has_attrs
def test_has_attrs():    assert has_attrs(dict(), 'get', 'keys', 'items', 'values') is True

# Generated at 2024-03-18 05:33:59.800149
# Unit test for function has_any_callables
def test_has_any_callables():    assert has_any_callables(dict, 'get', 'keys', 'items', 'values') is True

# Generated at 2024-03-18 05:34:09.473240
# Unit test for function has_any_callables
def test_has_any_callables():    assert has_any_callables(dict, 'get', 'keys', 'items', 'values') is True

# Generated at 2024-03-18 05:34:18.208392
# Unit test for function has_any_callables
def test_has_any_callables():    assert has_any_callables(dict, 'get', 'keys', 'items', 'values') is True

# Generated at 2024-03-18 05:34:23.724583
# Unit test for function has_callables
def test_has_callables():    assert has_callables(dict, 'get', 'keys', 'items', 'values')

# Generated at 2024-03-18 05:34:30.633411
# Unit test for function has_any_callables
def test_has_any_callables():    assert has_any_callables(dict, 'get', 'keys', 'items', 'values') is True

# Generated at 2024-03-18 05:34:35.067088
# Unit test for function has_any_callables
def test_has_any_callables():    assert has_any_callables(dict, 'get', 'keys', 'items', 'values') is True

# Generated at 2024-03-18 05:34:38.669848
# Unit test for function has_callables
def test_has_callables():    assert has_callables(dict, 'get', 'keys', 'items', 'values')

# Generated at 2024-03-18 05:34:42.745267
# Unit test for function has_callables
def test_has_callables():    assert has_callables(dict, 'get', 'keys', 'items', 'values')

# Generated at 2024-03-18 05:34:47.762581
# Unit test for function has_callables
def test_has_callables():    assert has_callables(dict, 'get', 'keys', 'items', 'values')

# Generated at 2024-03-18 05:35:15.898093
# Unit test for function has_callables
def test_has_callables():    assert has_callables(dict, 'get', 'keys', 'items', 'values')

# Generated at 2024-03-18 05:35:21.233411
# Unit test for function has_callables
def test_has_callables():    assert has_callables(dict, 'get', 'keys', 'items', 'values')

# Generated at 2024-03-18 05:35:26.616158
# Unit test for function has_any_callables
def test_has_any_callables():    # Test with an object that has some callable attributes
    assert has_any_callables(dict, 'get', 'keys', 'items', 'values', 'foo') is True, \
        "has_any_callables failed to identify callable attributes"

    # Test with an object that has no callable attributes
    class NonCallableAttrs:
        attr1 = 1
        attr2 = 'string'
        attr3 = [1, 2, 3]

    assert has_any_callables(NonCallableAttrs, 'attr1', 'attr2', 'attr3') is False, \
        "has_any_callables incorrectly identified non-callable attributes as callable"

    # Test with an object that has no attributes
    assert has_any_callables(object(), 'nonexistent_method') is False, \
        "has_any_callables incorrectly identified nonexistent attributes"

    # Test with an object that has all attributes but not all are callable

# Generated at 2024-03-18 05:35:31.972147
# Unit test for function has_any_callables
def test_has_any_callables():    # Test with an object that has some callable attributes
    class MyClass:
        def method_one(self):
            pass

        def method_two(self):
            pass

        non_callable = "I am not callable"

    obj = MyClass()

    assert has_any_callables(obj, 'method_one', 'non_callable') is True, "has_any_callables should return True when at least one attribute is callable"
    assert has_any_callables(obj, 'non_callable') is False, "has_any_callables should return False when no attributes are callable"
    assert has_any_callables(obj, 'method_one', 'method_two') is True, "has_any_callables should return True when multiple attributes are callable"
    assert has_any_callables(obj, 'non_existent_method') is False, "has_any_callables should return False when the attribute does not exist"

    # Test with built-in types

# Generated at 2024-03-18 05:35:39.219093
# Unit test for function has_callables

# Generated at 2024-03-18 05:35:46.836461
# Unit test for function has_any_callables
def test_has_any_callables():    assert has_any_callables(dict, 'get', 'keys', 'items', 'values') is True

# Generated at 2024-03-18 05:35:54.010915
# Unit test for function has_callables
def test_has_callables():    assert has_callables(dict, 'get', 'keys', 'items', 'values')

# Generated at 2024-03-18 05:36:00.048974
# Unit test for function has_any_callables
def test_has_any_callables():    assert has_any_callables(dict, 'get', 'keys', 'items', 'values') is True

# Generated at 2024-03-18 05:36:05.127173
# Unit test for function has_any_callables
def test_has_any_callables():    assert has_any_callables(dict, 'get', 'keys', 'items', 'values') is True

# Generated at 2024-03-18 05:36:11.096658
# Unit test for function has_any_callables
def test_has_any_callables():    assert has_any_callables(dict, 'get', 'keys', 'items', 'values') is True

# Generated at 2024-03-18 05:36:50.258569
# Unit test for function has_any_callables
def test_has_any_callables():    assert has_any_callables(dict, 'get', 'keys', 'items', 'values') is True

# Generated at 2024-03-18 05:36:57.230780
# Unit test for function has_any_callables
def test_has_any_callables():    assert has_any_callables(dict, 'get', 'keys', 'items', 'values') is True

# Generated at 2024-03-18 05:37:00.775863
# Unit test for function has_callables
def test_has_callables():    assert has_callables(dict, 'get', 'keys', 'items', 'values')

# Generated at 2024-03-18 05:37:04.977150
# Unit test for function has_callables
def test_has_callables():    assert has_callables(dict, 'get', 'keys', 'items', 'values')

# Generated at 2024-03-18 05:37:12.530177
# Unit test for function has_any_callables
def test_has_any_callables():    # Test with an object that has some callable attributes
    obj_with_callables = {'get': lambda x: x, 'pop': lambda x: x, 'non_callable': 123}
    assert has_any_callables(obj_with_callables, 'get', 'pop', 'non_callable') is True
    assert has_any_callables(obj_with_callables, 'get', 'pop') is True
    assert has_any_callables(obj_with_callables, 'non_callable') is False

    # Test with an object that has no callable attributes
    obj_without_callables = {'attr1': 1, 'attr2': 2}
    assert has_any_callables(obj_without_callables, 'attr1', 'attr2') is False

    # Test with an object that has all callable attributes
    obj_all_callables = {'method1': lambda: None, 'method2': lambda: None}
    assert has_any_callables

# Generated at 2024-03-18 05:37:19.652292
# Unit test for function has_any_callables
def test_has_any_callables():    assert has_any_callables(dict, 'get', 'keys', 'items', 'values') is True

# Generated at 2024-03-18 05:37:23.466494
# Unit test for function has_callables
def test_has_callables():    assert has_callables(dict, 'get', 'keys', 'items', 'values')

# Generated at 2024-03-18 05:37:28.238250
# Unit test for function has_callables
def test_has_callables():    assert has_callables(dict, 'get', 'keys', 'items', 'values')

# Generated at 2024-03-18 05:37:32.256809
# Unit test for function has_callables
def test_has_callables():    assert has_callables(dict, 'get', 'keys', 'items', 'values')

# Generated at 2024-03-18 05:37:37.743108
# Unit test for function has_any_callables
def test_has_any_callables():    assert has_any_callables(dict, 'get', 'keys', 'items', 'values') is True

# Generated at 2024-03-18 05:38:14.036934
# Unit test for function has_any_callables
def test_has_any_callables():    # Test with an object that has some callable attributes
    class MyClass:
        def method_one(self):
            pass

        def method_two(self):
            pass

        non_callable = "I am not callable"

    obj = MyClass()

    assert has_any_callables(obj, 'method_one', 'non_callable') is True
    assert has_any_callables(obj, 'method_two') is True
    assert has_any_callables(obj, 'non_callable') is False
    assert has_any_callables(obj, 'method_one', 'method_two') is True
    assert has_any_callables(obj, 'non_existent_method') is False

    # Test with built-in types
    assert has_any_callables(dict, 'get', 'pop', 'non_callable') is True
    assert has_any_callables(list, 'append', 'extend') is True
    assert has_any_callables(set, 'add', 'update') is True


# Generated at 2024-03-18 05:38:21.227548
# Unit test for function has_callables
def test_has_callables():    # Test with an object that has all callable attributes
    class MyClass:
        def method_one(self):
            pass

        def method_two(self):
            pass

    obj_with_callables = MyClass()
    assert has_callables(obj_with_callables, 'method_one', 'method_two') is True

    # Test with an object that has some non-callable attributes
    class MyOtherClass:
        method_one = 1
        method_two = lambda self: None

    obj_with_non_callables = MyOtherClass()
    assert has_callables(obj_with_non_callables, 'method_one', 'method_two') is False

    # Test with an object that has no attributes
    class EmptyClass:
        pass

    obj_empty = EmptyClass()
    assert has_callables(obj_empty, 'method_one', 'method_two') is False

    # Test with built-in types

# Generated at 2024-03-18 05:38:28.374680
# Unit test for function has_any_callables
def test_has_any_callables():    # Test with an object that has some callable attributes
    assert has_any_callables(dict, 'get', 'keys', 'items', 'values', 'foo') is True, \
        "has_any_callables should return True for dict with callable attributes"

    # Test with an object that has no callable attributes
    class NonCallableAttrs:
        attr1 = 1
        attr2 = 'string'
        attr3 = [1, 2, 3]

    assert has_any_callables(NonCallableAttrs, 'attr1', 'attr2', 'attr3') is False, \
        "has_any_callables should return False for object with no callable attributes"

    # Test with an object that has some non-callable and some callable attributes
    class MixedAttrs:
        def method1(self):
            pass

        attr2 = 'string'


# Generated at 2024-03-18 05:38:34.332968
# Unit test for function has_callables
def test_has_callables():    assert has_callables(dict, 'get', 'keys', 'items', 'values')

# Generated at 2024-03-18 05:38:39.080982
# Unit test for function has_callables
def test_has_callables():    assert has_callables(dict, 'get', 'keys', 'items', 'values')

# Generated at 2024-03-18 05:38:45.801691
# Unit test for function has_any_callables
def test_has_any_callables():    # Test with an object that has some callable attributes
    assert has_any_callables(dict, 'get', 'keys', 'items', 'values', 'foo') is True, \
        "has_any_callables should return True for dict with callable attributes"

    # Test with an object that has no callable attributes
    class NonCallableObject:
        attr1 = 1
        attr2 = 'string'

    assert has_any_callables(NonCallableObject, 'attr1', 'attr2') is False, \
        "has_any_callables should return False for object with no callable attributes"

    # Test with an object that has both callable and non-callable attributes
    class MixedObject:
        def method(self):
            pass
        attr = 42

    assert has_any_callables(MixedObject, 'method', 'attr') is True, \
        "has_any_callables should return True for object with mixed attributes"

    #

# Generated at 2024-03-18 05:38:53.286947
# Unit test for function has_callables
def test_has_callables():    assert has_callables(dict, 'get', 'keys', 'items', 'values')

# Generated at 2024-03-18 05:38:59.463795
# Unit test for function has_callables
def test_has_callables():    assert has_callables(dict, 'get', 'keys', 'items', 'values')

# Generated at 2024-03-18 05:39:03.537515
# Unit test for function has_callables
def test_has_callables():    assert has_callables(dict, 'get', 'keys', 'items', 'values')

# Generated at 2024-03-18 05:39:10.175375
# Unit test for function has_any_callables
def test_has_any_callables():    assert has_any_callables(dict, 'get', 'keys', 'items', 'values') is True

# Generated at 2024-03-18 05:40:19.047674
# Unit test for function has_any_callables
def test_has_any_callables():    assert has_any_callables(dict, 'get', 'keys', 'items', 'values') is True

# Generated at 2024-03-18 05:40:22.719518
# Unit test for function has_callables
def test_has_callables():    assert has_callables(dict, 'get', 'keys', 'items', 'values')

# Generated at 2024-03-18 05:40:29.670310
# Unit test for function has_callables
def test_has_callables():    assert has_callables(dict, 'get', 'keys', 'items', 'values')

# Generated at 2024-03-18 05:40:37.129182
# Unit test for function has_callables
def test_has_callables():    assert has_callables(dict, 'get', 'keys', 'items', 'values')

# Generated at 2024-03-18 05:40:40.350547
# Unit test for function has_callables
def test_has_callables():    assert has_callables(dict, 'get', 'keys', 'items', 'values')

# Generated at 2024-03-18 05:40:48.026249
# Unit test for function has_any_callables
def test_has_any_callables():    assert has_any_callables(dict, 'get', 'keys', 'items', 'values') is True

# Generated at 2024-03-18 05:40:55.482950
# Unit test for function has_any_callables
def test_has_any_callables():    assert has_any_callables(dict, 'get', 'keys', 'items', 'values') is True

# Generated at 2024-03-18 05:41:00.323167
# Unit test for function has_callables
def test_has_callables():    assert has_callables(dict, 'get', 'keys', 'items', 'values')

# Generated at 2024-03-18 05:41:06.468784
# Unit test for function has_any_callables
def test_has_any_callables():    assert has_any_callables(dict, 'get', 'keys', 'items', 'values') is True

# Generated at 2024-03-18 05:41:11.285224
# Unit test for function has_callables
def test_has_callables():    assert has_callables(dict, 'get', 'keys', 'items', 'values')