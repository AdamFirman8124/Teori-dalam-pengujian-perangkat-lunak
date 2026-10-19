

# Generated at 2022-06-13 20:43:15.460960
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True



# Generated at 2022-06-13 20:43:21.871432
# Unit test for function has_callables
def test_has_callables():
    """test the has_callables function"""
    obj = dict(a=1, b=2)
    attrs = ['get', 'items', 'keys', 'values']
    assert has_callables(obj, *attrs) is True
    attrs = ['get', 'items', 'keys', 'foo']
    assert has_callables(obj, *attrs) is False


# Generated at 2022-06-13 20:43:29.076998
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = dict(
        a=1,
        b=2,
        c=3,
        d=4,
    )
    assert has_any_callables(obj, 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables(obj, 'foo', 'bar') is False



# Generated at 2022-06-13 20:43:31.896155
# Unit test for function has_any_callables
def test_has_any_callables():
    from flutils.objutils import (
        has_any_callables
    )

    assert has_any_callables(dict(a=1, b=2), 'get','keys','foo','bar') is True



# Generated at 2022-06-13 20:43:38.667825
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo')
    assert has_any_callables(dict(),'close','keys','items','values')
    assert has_any_callables(int(),'bit_length','conjugate','denominator')



# Generated at 2022-06-13 20:43:46.476829
# Unit test for function has_any_callables
def test_has_any_callables():
    class MyClass(object):
        def __init__(self):
            self.foo = 'bar'
            self.hello = 'world'

    mc = MyClass()
    assert has_any_callables(mc,'foo','hello') == False
    assert has_any_callables(mc,'foo') == False
    assert has_any_callables(mc,'hello') == False
    assert has_any_callables(mc,'wakka') == False

    assert has_any_callables(mc,'f') == False
    assert has_any_callables(mc,'he') == False
    assert has_any_callables(mc,'bar') == False
    assert has_any_callables(mc,'wak') == False

    class MyClass2(MyClass):
        def hello(self):
            return 'hello world'



# Generated at 2022-06-13 20:43:52.019386
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables('hello', 'foo', 'upper')
    assert has_any_callables(dict(),'get','items','bar')
    assert has_any_callables(dict, 'get', 'items', 'bar')
    assert not has_any_callables(dict().keys(), 'get', 'items', 'bar')


# Generated at 2022-06-13 20:43:53.540516
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(),'get','keys','items','values') is True


# Generated at 2022-06-13 20:44:00.866954
# Unit test for function has_any_callables
def test_has_any_callables():
    # Should be True since at least one method is callable
    _obj = dict(foo=1, bar=2)
    assert has_any_callables(_obj, 'get', 'keys', 'values', 'foo') is True

    # Should be False since no methods are callable
    _obj = dict(foo=1, bar=2)
    assert has_any_callables(_obj, 'get', 'keys', 'values', 'foo') is True



# Generated at 2022-06-13 20:44:04.193064
# Unit test for function has_any_callables
def test_has_any_callables():
    expected = True
    actual = has_any_callables(dict(),'get','keys','items','values','foo')
    assert actual == expected


# Generated at 2022-06-13 20:44:08.245825
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')

# Generated at 2022-06-13 20:44:16.778233
# Unit test for function has_any_callables
def test_has_any_callables():
    def function():
        pass
    class Class(object):
        def __init__(self):
            pass
        def method(self):
            pass
    class ChildClass(Class):
        pass
    not_callable = 2
    test_dict = {
        'function': function,
        'some_method': ChildClass.method,
        'class': ChildClass,
        'not_callable': not_callable,
        'nested': {
            'method': Class.method,
        }
    }
    assert has_any_callables(test_dict, 'function', 'some_method')
    assert not has_any_callables(test_dict, 'class', 'not_callable')
    assert not has_any_callables(test_dict, 'nested')

# Generated at 2022-06-13 20:44:22.168398
# Unit test for function has_any_callables
def test_has_any_callables():
    foo = dict(a=1, b=2)
    assert has_any_callables(foo, 'get', 'update', 'clear', 'items')

    foo = {'a':1, 'b':2}
    assert has_any_callables(foo, 'get', 'update', 'clear', 'items')



# Generated at 2022-06-13 20:44:23.441045
# Unit test for function has_any_callables
def test_has_any_callables():
    pass


# Generated at 2022-06-13 20:44:34.290248
# Unit test for function has_any_callables
def test_has_any_callables():
    # Given: an object with attributes
    obj = dict(a=1, b=2)
    # and: callable attributes
    attrs = ('get', 'keys', 'items', 'values', 'foo')
    # fully qualified names
    fq_attrs = tuple(
        f'{obj.__class__.__module__}.{obj.__class__.__name__}.' + attr
        for attr in attrs
    )
    # When: asking if it has callable attributes
    result = has_any_callables(obj, *attrs)
    # and: asking if it has callable attributes fully qualified
    result_fq = has_any_callables(obj, *fq_attrs)
    # Then: it should return True
    assert result is True
    # and: if the attributes are fully qualified

# Generated at 2022-06-13 20:44:41.767496
# Unit test for function has_any_callables
def test_has_any_callables():

    assert has_any_callables([], 'append', 'sorted')
    assert has_any_callables({}, 'get', 'keys')
    assert has_any_callables('test', 'upper', 'find', 'index')
    assert not has_any_callables(0, 'bit_length', 'from_bytes')
    assert not has_any_callables(False, 'numerator', 'from_bytes')



# Generated at 2022-06-13 20:44:53.010711
# Unit test for function has_any_callables
def test_has_any_callables():
    """Tests for method has_any_callables"""

# Generated at 2022-06-13 20:45:04.307025
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'values', 'items') is True
    assert has_any_callables(dict(), 'get', 'keys', 'values', 'some_method') is True
    assert has_any_callables(dict(), 'get', 'keys', 'values', 'some_method', 'something') is True
    assert has_any_callables(dict(), '__init__', 'keys', 'values', 'foo') is False
    assert has_any_callables(dict(), '__init__', 'keys', 'values', 'something') is False
    assert has_any_callables(dict(), '__init__', 'keys', 'values', 'something') is False

# Generated at 2022-06-13 20:45:07.516224
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True



# Generated at 2022-06-13 20:45:16.041327
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(a=4), 'get', 'keys', 'items', 'values') == True
    assert has_any_callables(dict(a=4), 'get', 'keys', 'items', 'values', 'foo') == True
    assert has_any_callables(dict(a=4), 'foo') == False
    assert has_any_callables(dict(a=4)) == False


# Generated at 2022-06-13 20:45:29.707748
# Unit test for function has_any_callables
def test_has_any_callables():
    from collections import ChainMap
    from typing import ChainMap as _ChainMap

    from flutils.objutils import has_any_callables

    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables(0, 'bit_length') is True

    assert has_any_callables(int(), 'bit_length') is True
    assert has_any_callables(int(), 'bit_length', '__sizeof__') is True
    assert has_any_callables(int(), 'bit_length', '__sizeof__', 'conjugate') is False

    assert has_any_callables(dict(), 'get', 'foo') is True
    assert has_any_callables(dict(), 'foo', '__sizeof__') is False

   

# Generated at 2022-06-13 20:45:37.620931
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo') ==  True
    assert has_any_callables(dict(),'foo') == False
    assert has_any_callables(set(),'discard', 'intersection', 'symmetric_difference') ==  True
    assert has_any_callables(set(),'foo') == False
    assert has_any_callables({}, 'create', 'foo') == False
    assert has_any_callables({}, 'copy', 'foo') == True
    assert has_any_callables({}, 'foo') == False
    assert has_any_callables(list(), 'append', 'foo') == True
    assert has_any_callables(list(), 'foo') == False

# Generated at 2022-06-13 20:45:41.066955
# Unit test for function has_any_callables
def test_has_any_callables():
    """Testing has_any_callables"""
    assert has_any_callables(dict(),'get','keys','items','values','foo') == True
    assert has_any_callables(dict(),'get','keys','items','values','foo')


# Generated at 2022-06-13 20:45:57.150392
# Unit test for function has_any_callables
def test_has_any_callables():
    import unittest

    class TestHasAnyCallables(unittest.TestCase):
        def test_has_any_callables(self):
            class Foo:
                def __init__(self):
                    pass

            foo = Foo()
            self.assertEqual(has_any_callables(foo, 'bar', 'baz'), False)

            foo.bar = ''
            self.assertEqual(has_any_callables(foo, 'bar', 'baz'), False)

            foo.bar = lambda: None
            self.assertEqual(has_any_callables(foo, 'bar', 'baz'), True)

            foo.baz = lambda: None
            self.assertEqual(has_any_callables(foo, 'bar', 'baz'), True)

            foo.bar = ''

# Generated at 2022-06-13 20:46:08.823169
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables('hello', 'upper')
    assert not has_any_callables(dict(), 'foo')
    assert has_any_callables(dict(), 'foo', 'keys')
    assert has_any_callables(dict(), 'foo', 'keys', 'get')
    assert has_any_callables(dict(), 'items', 'foo')
    assert has_any_callables(dict(), 'values', 'foo')
    assert not has_any_callables(list(), 'foo')
    assert has_any_callables(list(), 'foo', 'index')
    assert has_any_callables(list(), 'foo', 'index', 'append')
    assert has_any_callables(list(), 'index', 'foo')
    assert has_any_callables(list(), 'sort', 'foo')

# Generated at 2022-06-13 20:46:13.771174
# Unit test for function has_any_callables
def test_has_any_callables():
    print('Testing function has_any_callables...')
    obj = dict()
    assert has_any_callables(obj, 'get', 'keys', 'items', 'values', 'foo') is True


# Generated at 2022-06-13 20:46:23.537373
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'items') == True
    assert has_any_callables(dict(), 'get') == True
    assert has_any_callables(dict(), 'keys') == True
    assert has_any_callables(dict(), 'values') == True
    assert has_any_callables(dict(), 'foo') == False
    assert has_any_callables(dict(), 'items', 'keys', 'get') == True
    assert has_any_callables(dict(), 'items', 'keys', 'foo') == True
    assert has_any_callables(dict(), 'foo', 'foobar') == False
    assert has_any_callables(str(), 'join', 'find') == True
    assert has_any_callables(str(), 'join', 'find', 'upper', 'lower') == True
   

# Generated at 2022-06-13 20:46:27.180603
# Unit test for function has_any_callables
def test_has_any_callables():
    """Test for the function has_any_callables"""
    d = dict()
    assert has_any_callables(d, "get", "keys", "items", "values") is True



# Generated at 2022-06-13 20:46:34.223846
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = dict(a=1, b=2)
    attrs = ('values', 'keys')
    ans = has_any_callables(obj, *attrs)
    assert ans == True
    attrs = ('foo', 'bar', 'zip')
    ans = has_any_callables(obj, *attrs)
    assert ans == False


# Generated at 2022-06-13 20:46:39.329939
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = dict(a=1, b=2)
    assert has_any_callables(obj, '__getitem__', '__len__') is True
    assert has_any_callables(obj, 'foo', 'bar') is False

