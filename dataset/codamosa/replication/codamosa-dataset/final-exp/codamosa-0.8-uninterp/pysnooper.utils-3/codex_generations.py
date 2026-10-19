

# Generated at 2022-06-12 19:58:43.850727
# Unit test for function get_repr_function
def test_get_repr_function():
    class A: pass
    class B(A): pass
    class C: pass

    assert get_repr_function(A(), []) is repr
    assert get_repr_function(B(), []) is repr

    assert get_repr_function(A(), [(A, str)]) is str
    assert get_repr_function(B(), [(A, str)]) is str

    assert get_repr_function(A(), [(A, str), (B, int)]) is str
    with pytest.raises(AssertionError):
        get_repr_function(B(), [(A, str), (B, int)]) # Incompatible with A

    assert get_repr_function(A(), [(lambda x: True, str)]) is str

# Generated at 2022-06-12 19:58:52.399629
# Unit test for function get_repr_function
def test_get_repr_function():
    from . import my_list

    class Foo(object):
        pass

    def foo_repr(x):
        return 'foo_repr: {}'.format(x)

    assert get_repr_function(5, [(int, lambda x: 'a number')]) == 'a number'
    # You can use a type instead of a lambda
    assert get_repr_function(5, [(int, 'a number')]) == 'a number'
    assert get_repr_function(Foo(), [(Foo, foo_repr)]) == 'foo_repr: <__main__.Foo object at 0x...>'
    # You can use a type instead of a lambda:

# Generated at 2022-06-12 19:59:02.304523
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    from collections import namedtuple
    SomeThing = namedtuple('SomeThing', 'x y')
    assert get_shortish_repr(SomeThing(1, 2)) == 'SomeThing(x=1, y=2)'
    assert get_shortish_repr(SomeThing(1, 2), max_length=3) == 'Som...2)'
    assert get_shortish_repr(SomeThing(1, 2), max_length=10) == 'SomeThing(x=1, y=2)'
    assert get_shortish_repr(1) == '1'
    assert get_shortish_repr(1, max_length=2) == '1'
    assert get_shortish_repr(1, max_length=0) == '1'
    assert get_shortish

# Generated at 2022-06-12 19:59:11.650944
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('test', max_length=6) == 'test'
    assert get_shortish_repr('a_string', max_length=6) == 'a_stri...'
    assert get_shortish_repr('a_string', max_length=3) == 'a_s...'
    assert get_shortish_repr('a_string', max_length=2) == 'a_...'
    assert get_shortish_repr('a_string', max_length=1) == 'a...'
    assert get_shortish_repr('a_string', max_length=0) == '...'
    assert get_shortish_repr('a_string', max_length=None) == 'a_string'



# Generated at 2022-06-12 19:59:23.557503
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert normalize_repr('hello world') == 'hello world'
    assert normalize_repr(
        '<list at 0x0352536A>'
    ) == '<list>'
    assert normalize_repr('hello world at 0x0352536A') == 'hello world'

    assert get_shortish_repr(123) == '123'
    assert get_shortish_repr(123, normalize=True) == '123'
    assert get_shortish_repr(type(lambda: 123)) == "<type 'function'>"
    assert get_shortish_repr(type(lambda: 123), normalize=True) == \
                                                         "<type 'function'>"

# Generated at 2022-06-12 19:59:29.009740
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(7, ((lambda x: x % 2 == 0, str.upper),
                                 (lambda x: True, str))) == str
    assert get_repr_function(6, ((lambda x: x % 2 == 0, str.upper),
                                 (lambda x: True, str))) == str.upper
    assert get_repr_function(5, ((float, str.upper),
                                 (lambda x: True, str))) == str



# Generated at 2022-06-12 19:59:38.502719
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(123) == '123'
    assert get_shortish_repr(123, max_length=2) == '12'
    assert get_shortish_repr(123, max_length=1) == '1'
    assert get_shortish_repr('foo') == 'foo'
    assert get_shortish_repr('foo', max_length=2) == 'fo'
    assert get_shortish_repr('foo', max_length=1) == 'f'
    assert get_shortish_repr(123, custom_repr=((int, lambda x: 'int'),)) == 'int'
    assert get_shortish_repr(123, max_length=2, custom_repr=((int, lambda x: 'int'),)) == 'in'
    assert get

# Generated at 2022-06-12 19:59:45.825949
# Unit test for function get_repr_function
def test_get_repr_function():
    from .compatibility import unittest
    from . import dummy_objects

    class Dummy(dummy_objects.Dummy):
        pass

    for custom_repr in (
        [],
        [(lambda o: o.__class__.__name__ == 'Dummy', lambda o: 'the dummy')],
        [
            (lambda o: o.__class__.__name__ == 'Dummy', lambda o: 'the dummy'),
            (lambda o: o.__class__.__name__ == 'SomeClass', lambda o: 'some class'),
        ],
        [(Dummy, lambda o: 'the dummy')],
        [(lambda o: o.__class__.__name__ == 'Dummy', lambda o: 'the dummy'),
         (Dummy, lambda o: 'the dummy2')],
    ):
        print()


# Generated at 2022-06-12 19:59:48.160941
# Unit test for function get_repr_function
def test_get_repr_function():

    assert get_repr_function(1, custom_repr=((int, lambda x: x),)) == 1

    assert get_repr_function(1, custom_repr=()) == repr

    assert get_repr_function('spam', custom_repr=((int, lambda x: x),)) == repr



# Generated at 2022-06-12 19:59:49.582432
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Foo(WritableStream):
        def write(self, s): pass
    assert issubclass(Foo, WritableStream)

    class Foo(WritableStream): pass
    assert not issubclass(Foo, WritableStream)



# Generated at 2022-06-12 19:59:59.251425
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MinimalWritableStream(WritableStream):
        def __init__(self):
            self.data = ''

        def write(self, s):
            self.data += s


    with MinimalWritableStream() as mws:
        mws.write('a')
        mws.write('b')
        mws.write('c')

    assert mws.data == 'abc'




# Generated at 2022-06-12 20:00:04.363138
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A:
        def write(self, s):
            pass
    class B(A):
        def write(self, s):
            pass
    assert issubclass(A, WritableStream)
    assert issubclass(B, WritableStream)
    assert A().write('meow') is None
    assert B().write('meow') is None



# Generated at 2022-06-12 20:00:12.760856
# Unit test for function get_repr_function
def test_get_repr_function():
    item = 5
    assert get_repr_function(item, custom_repr=()) is repr
    custom_repr = (
        (lambda item: isinstance(item, int), lambda item: 'int'),
        (lambda item: item is None, lambda item: 'None')
    )
    assert get_repr_function(item, custom_repr=custom_repr) is repr
    item = None
    assert get_repr_function(item, custom_repr=custom_repr) == repr
    item = lambda: None
    assert get_repr_function(item, custom_repr=custom_repr) == repr

# Generated at 2022-06-12 20:00:20.024873
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import sys

    assert isinstance(sys.stdout, WritableStream)

    class SomeStuff(WritableStream):
        pass

    with pytest.raises(TypeError):
        isinstance(SomeStuff(), WritableStream)

    class SomeOtherStuff(WritableStream):
        def write(self, s):
            pass

    assert isinstance(SomeOtherStuff(), WritableStream)

    class SomeOtherOtherStuff(WritableStream):
        def write(self, s):
            pass

        def nice_write(self, s):
            pass

    assert isinstance(SomeOtherOtherStuff(), WritableStream)

# Generated at 2022-06-12 20:00:27.654125
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(1, custom_repr=[]) == repr
    assert get_repr_function(2, custom_repr=[int]) == int.__repr__
    assert get_repr_function(2.0, custom_repr=[int, float]) == repr
    assert get_repr_function(1.0, custom_repr=[int, float]) == float.__repr__
    assert get_repr_function(3.0, custom_repr=[(float, float.__str__)]) == str



# Generated at 2022-06-12 20:00:36.618852
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('hello') == "'hello'"
    assert get_shortish_repr('hello world' * 100) == "'hello worldhello worldhello worldhello worldhello worldhello worldhello worldhello worldhello worldhello worldhello worldhello worldhello worldhello worldhello worldhello worldhello worldhello worldhello worldhello worldhello worldhello worldhello worldhello worldhello worldhello worldhello worldhello worldhello worldhello worldhello world'"
    assert get_shortish_repr('hello world' * 100, max_length=45) == "'hello worldhello worldhello worldhello world...orldhello worldhello worldhello world'"
    assert get_shortish_repr('hello world' * 100, max_length=46) == "'hello worldhello worldhello worldhello world...orldhello worldhello worldhello world'"

# Generated at 2022-06-12 20:00:48.202513
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    for item, expected in ((1, "1"), (1., "1.0"), ('hi', "'hi'"),
                           (str, "<class 'str'>")):
        assert get_shortish_repr(item) == expected


# Generated at 2022-06-12 20:00:52.431278
# Unit test for function shitcode
def test_shitcode():
    assert shitcode(u'Hello world!') == u'Hello world!'
    assert shitcode(u'abc') == u'abc'
    assert shitcode(u'Hi \U0001f638') == u'Hi ?'



# Generated at 2022-06-12 20:01:03.020573
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function('hello', []) is repr

    assert get_repr_function('hello', [
        (lambda x: True, 'hi')
    ])('hello') == 'hi'

    assert get_repr_function('hello', [
        (lambda x: False, 'hi')
    ])('hello') == 'hello'

    assert get_repr_function('hello', [
        (str, 'hi')
    ])('hello') == 'hi'

    assert get_repr_function('hello', [
        (str, 'hi')
    ])(5) == '5'

    assert get_repr_function(5, [
        (str, 'hi')
    ])('hello') == 'hi'


# Generated at 2022-06-12 20:01:04.499910
# Unit test for function shitcode
def test_shitcode():
    assert shitcode('hello') == 'hello'
    assert shitcode('héllo') == 'h?llo'

# Generated at 2022-06-12 20:01:12.779245
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    test_me = lambda x: get_shortish_repr(x, max_length=None)
    assert test_me(0) == '0'
    assert test_me(1234) == '1234'
    assert test_me(2**100) == '1267650600228229401496703205376'
    assert test_me((1, 2, 3, 4)) == '(1, 2, 3, 4)'
    assert test_me('abc') == "'abc'"
    assert test_me('a'*100) == "'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"\
                              "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"\
                              "aaaaa'"
    assert test_me(set((1, 2, 3))) == 'set([1, 2, 3])'


# Generated at 2022-06-12 20:01:18.803156
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import io
    import sys
    import builtins
    import contextlib
    class StupidWritableStream(WritableStream):
        def write(self, s):
            pass
    assert isinstance(StupidWritableStream(), WritableStream)
    assert isinstance(sys.stdout, WritableStream)
    assert isinstance(sys.stderr, WritableStream)
    assert isinstance(io.StringIO(), WritableStream)
    assert isinstance(io.BytesIO(), WritableStream)
    assert isinstance(open('temp.txt', 'w'), WritableStream)
    assert isinstance(builtins.open('temp.txt', 'w'), WritableStream)
    assert isinstance(contextlib.closing(open('temp.txt', 'w')),
                      WritableStream)

# Generated at 2022-06-12 20:01:21.833961
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(1) in ('1', '...')




# Generated at 2022-06-12 20:01:26.031261
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A:
        def write(self, s):
            assert isinstance(s, string_types)
            return len(s)

    class B:
        pass

    assert WritableStream.__subclasshook__(A)
    assert not WritableStream.__subclasshook__(B)




# Generated at 2022-06-12 20:01:34.318869
# Unit test for function get_repr_function
def test_get_repr_function():
    class Foo(object): pass
    class Bar(Foo): pass
    class Baz(Foo): pass
    class Spam(Bar): pass

    foo = Foo()
    bar = Bar()
    baz = Baz()
    spam = Spam()

    def my_repr(x): return 'my_repr'
    def bar_repr(x): return 'bar_repr'
    def spam_repr(x): return 'spam_repr'


    assert get_repr_function(foo) is repr
    assert get_repr_function(bar) is repr
    assert get_repr_function(baz) is repr
    assert get_repr_function(spam) is repr


# Generated at 2022-06-12 20:01:42.040233
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    def my_custom_repr(item):
        return 'CUSTOM!'
    assert get_shortish_repr(1) == '1'
    assert get_shortish_repr(1, custom_repr=((lambda x: True, my_custom_repr),)) \
                                                                    == 'CUSTOM!'
    assert get_shortish_repr('12345', max_length=3) == '123...'
    assert get_shortish_repr('12345', max_length=None) == '12345'



# Generated at 2022-06-12 20:01:49.315045
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function([1, 2, 3], ((list, lambda l: ('[', ']')),)) == repr
    assert get_repr_function([1, 2, 3], ((list, lambda l: ('[', ']')),
                                         (int, lambda l: ('[', ']')))) == \
                                                                          repr

# Generated at 2022-06-12 20:01:57.132791
# Unit test for function shitcode
def test_shitcode():
    assert shitcode(u'the quick brown fox') == u'the quick brown fox'
    assert shitcode(u'the quick פאקש קשא') == u'the quick ?a??? a?'
    assert shitcode(u'the quick פאקש קשא'.encode('utf-8')) == \
                    u'the quick ?a??? a?'
    assert shitcode(u'שתקש') == u'?a??'
    assert shitcode(u'שתקש'.encode('latin')) == u'?a??'



# Generated at 2022-06-12 20:01:59.824278
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def write(self, s): pass
    assert issubclass(MyWritableStream, WritableStream)


# Generated at 2022-06-12 20:02:10.212768
# Unit test for function get_repr_function
def test_get_repr_function():
    import numpy
    numpy_int16 = numpy.int16
    int_representation = get_repr_function(5, custom_repr=[])
    int_with_custom_repr = get_repr_function(5, custom_repr=[(int, lambda x: 'int')])
    numpy_int16_with_custom_numpy_types = get_repr_function(
        numpy_int16(5),
        custom_repr=[(numpy_int16, lambda x: 'custom_numpy_int16_repr')]
    )
    numpy_int16_with_custom_int_types = get_repr_function(
        numpy_int16(5),
        custom_repr=[(int, lambda x: 'custom_int_repr')]
    )

# Generated at 2022-06-12 20:02:20.893320
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    # Let's do this without the `unittest` library, because we aren't
    # sure what will have been imported by the time we're at this point.

    class MyWritableStream(WritableStream):
        def write(self, s):
            self.wrote_this = s

    writable_stream = MyWritableStream()
    writable_stream.write('hello')
    assert writable_stream.wrote_this == 'hello'

    try:
        class NotImplementingWrite(WritableStream):
            pass
    except TypeError:
        pass
    else:
        raise AssertionError

    try:
        class DefiningWriteButNotImplementingIt(WritableStream):
            write = lambda *args: None
    except TypeError:
        pass
    else:
        raise AssertionError


# Generated at 2022-06-12 20:02:30.153722
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def write(self, s):
            self.s = s
            self.s_type = type(s)

    x = MyWritableStream()
    assert isinstance(x, WritableStream)
    x.write('meow')
    assert x.s == 'meow'
    assert x.s_type is type('meow')

    class MyWritableStream2(WritableStream):
        def write(self, s):
            self.s = s
            self.s_type = type(s)

    y = MyWritableStream2()
    assert isinstance(y, WritableStream)
    y.write(u'meow')
    assert y.s == u'meow'
    assert y.s_type is type(u'meow')






# Generated at 2022-06-12 20:02:39.562917
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Foo:
        pass

    assert WritableStream.__subclasshook__(Foo) is NotImplemented

    class Foo:
        def write(self, x):
            pass
    assert WritableStream.__subclasshook__(Foo) is NotImplemented

    class Foo:
        def write(self, x):
            pass
        def write_again(self, x):
            pass
    assert WritableStream.__subclasshook__(Foo) is NotImplemented

    class Foo:
        def write(self, x):
            pass
    assert WritableStream.__subclasshook__(Foo)
    assert isinstance(Foo(), WritableStream)



# Generated at 2022-06-12 20:02:42.637118
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A(WritableStream):
        def write(self, s):
            print(s)

    assert issubclass(A, WritableStream)

    class B:
        def write(self, s):
            print(s)

    assert not issubclass(B, WritableStream)



# Generated at 2022-06-12 20:02:50.399086
# Unit test for function get_repr_function
def test_get_repr_function():
    class Foo(object):
        def __init__(self, s):
            self.s = s
        def __repr__(self):
            return self.s
    custom_repr = [
        (lambda x: x.s == 'xyzzy', lambda x: 'xyzzy'),
        ((str, int), lambda x: 'str or int'),
        (str, lambda x: 'str'),
    ]
    assert get_repr_function(Foo('nothing'), custom_repr) is repr
    assert get_repr_function(Foo('xyzzy'), custom_repr) is xyzzy
    assert get_repr_function(Foo('str or int'), custom_repr) is xyzzy
    assert get_repr_function(Foo('str'), custom_repr) is xyzzy


# Generated at 2022-06-12 20:02:56.107796
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class X(WritableStream):
        def write(self, s):
            pass

    assert issubclass(X, WritableStream)
    x = X()
    x.write('hi')
    assert issubclass(X, WritableStream)

    class Y(X):
        pass

    assert issubclass(Y, WritableStream)
    y = Y()
    y.write('hi')
    assert issubclass(Y, WritableStream)

# Generated at 2022-06-12 20:02:57.932605
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class C(WritableStream):
        def write(self): pass

    assert isinstance(C(), WritableStream)




# Generated at 2022-06-12 20:03:03.341443
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A(object): pass
    class B(A): pass

    class _Test(object):
        def write(self, s):
            pass

    assert WritableStream.__subclasshook__(A) is NotImplemented
    assert WritableStream.__subclasshook__(B) is NotImplemented
    assert WritableStream.__subclasshook__(_Test) is True

# Generated at 2022-06-12 20:03:05.044228
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import io
    s = io.StringIO()
    WriteableStream.write(s, 'hello')
    assert s.getvalue() == 'hello'

# Generated at 2022-06-12 20:03:07.585803
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class GoodWritableStream(WritableStream):
        def write(self, s):
            pass

    assert issubclass(GoodWritableStream, WritableStream)

    class BadWritableStream(WritableStream):
        pass

    assert not issubclass(BadWritableStream, WritableStream)

# Generated at 2022-06-12 20:03:13.413914
# Unit test for function get_repr_function
def test_get_repr_function():
    x = []
    assert get_repr_function(x, (
        (lambda x: isinstance(x, list), lambda x: 'list!'),
    )) is repr

# Generated at 2022-06-12 20:03:17.267491
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Foo(WritableStream):

        def write(self, *args):
            self.args = args
    foo = Foo()
    foo.write('meow')
    assert foo.args == ('meow',)
    foo.write('woof', 'ribbit')
    assert foo.args == ('woof', 'ribbit')



# Generated at 2022-06-12 20:03:18.627613
# Unit test for method write of class WritableStream
def test_WritableStream_write():

    class Quack(WritableStream):
        def write(self, s):
            pass

    Quack()



# Generated at 2022-06-12 20:03:25.489910
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('hello') == "'hello'"
    assert get_shortish_repr(['a', 'b']) == "['a', 'b']"
    assert get_shortish_repr(['a', 'b'], max_length=6) == "['a', 'b']"
    assert get_shortish_repr(['a', 'b'], max_length=5) == "['a', 'b']"
    assert get_shortish_repr(['a', 'b'], max_length=4) == "['a']"
    assert get_shortish_repr(['a', 'b'], max_length=3) == "['a']"
    assert get_shortish_repr(['a', 'b'], max_length=2) == "[]"

# Generated at 2022-06-12 20:03:32.780885
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(1, [(int, str)]) == str
    assert get_repr_function(1, [(False, str)]) == repr
    assert get_repr_function(1, [(lambda x: x == 1, str)]) == str
    assert get_repr_function(1, [(lambda x: x == 2, str)]) == repr
    assert get_repr_function(1, [(lambda x, y=1: x == y, str)]) == str
    assert get_repr_function(1, [(lambda x, y=2: x == y, str)]) == repr



# Generated at 2022-06-12 20:03:36.207684
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(object, ()) is repr
    assert get_repr_function(None, ((lambda x: isinstance(x, object), str))) is str
    assert get_repr_function(None, ((lambda x: True, str), (object, repr))) is str

# Generated at 2022-06-12 20:03:46.784820
# Unit test for function get_repr_function
def test_get_repr_function():
    import types

    assert get_repr_function(1, ()) is repr
    assert get_repr_function('a', ()) is repr

    assert get_repr_function(1, [(lambda x: True, 'x')]) == 'x'
    assert get_repr_function(1, [(lambda x: False, 'x')]) is repr

    assert get_repr_function('a', [(str, 'b')]) == 'b'
    assert get_repr_function('a', [(str, 'b'), (int, 'c')]) == 'b'

    assert get_repr_function('a', [((lambda x: True), 'b')]) == 'b'
    assert get_repr_function('a', [(str, 'b'), ((lambda x: True), 'c')]) == 'b'

    assert get_

# Generated at 2022-06-12 20:03:52.857629
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('123456789', max_length=5) == '12345...'
    assert get_shortish_repr('123459', max_length=5) == '12345...'
    assert get_shortish_repr('1234', max_length=5) == '1234'
    assert get_shortish_repr('123', max_length=5) == '123'

# Generated at 2022-06-12 20:04:00.390503
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    class Class(object):
        def __repr__(self):
            return 'this is a repr'
        def __str__(self):
            return 'this is a str'
    class Class2(object):
        def __repr__(self):
            return 'this is also a repr'
        def __str__(self):
            return 'this is also a str'

    assert get_shortish_repr('this is a string') == 'this is a string'
    assert get_shortish_repr('this is a string', max_length=4) == 'thi...'
    assert get_shortish_repr('this is a string', max_length=2) == 'th...'
    assert get_shortish_repr('this is a string', max_length=3) == 'thi...'

# Generated at 2022-06-12 20:04:03.666608
# Unit test for function get_repr_function
def test_get_repr_function():
    from . import testutils
    
    assert isinstance(get_repr_function(testutils, ((testutils, len),)),
                      collections_abc.Callable)
    assert get_repr_function(testutils, ((testutils, len),)) is len

# Generated at 2022-06-12 20:04:14.339069
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class X:
        pass

    assert not isinstance(X(), WritableStream)

    class X:
        pass

    assert not isinstance(X(), WritableStream)
    from .writable_stream_mixin import WritableStreamMixin
    X = type('X', (), {})
    assert not isinstance(X(), WritableStream)

# Generated at 2022-06-12 20:04:21.254720
# Unit test for function shitcode
def test_shitcode():
    assert shitcode(u'abc') == u'abc'
    assert shitcode(u'abc\nabc') == u'abc?abc'
    assert shitcode(u'\n') == u'?'
    assert shitcode(u'\xfe') == u'?'
    assert shitcode(u'\xff') == u'?'
    assert shitcode(u'\x00') == u'?'
    assert shitcode(u'\u20ac') == u'?'
    assert shitcode(u'') == u''

# Generated at 2022-06-12 20:04:27.482171
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class ExtensibleString(str):
        def __init__(self):
            self.data = []

        def write(self, s):
            self.data.append(s)

    assert isinstance(ExtensibleString(), WritableStream)

    es = ExtensibleString()
    es.write('hi')
    assert es.data == ['hi']
    es.write('hello')
    es.write(('world',))
    assert es.data == ['hi', 'hello', ('world',)]



# Generated at 2022-06-12 20:04:30.101423
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class TestWritableStream(WritableStream):
        def write(self, s):
            pass

    test_writable_stream = TestWritableStream()
    assert isinstance(test_writable_stream, WritableStream)




# Generated at 2022-06-12 20:04:35.732203
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(1) == '1'
    assert get_shortish_repr('hi') == 'hi'
    assert get_shortish_repr('hello, world!') == 'hello, world!'
    assert get_shortish_repr('hello,') == 'hello,'
    assert get_shortish_repr('hello, world!', max_length=7) == 'hel...!'
    assert get_shortish_repr('hello, world!', max_length=8) == 'hello...!'
    assert get_shortish_repr('hello, world!', max_length=9) == 'hello,...!'
    assert get_shortish_repr('hello, world!', max_length=10) == 'hello, w...'

# Generated at 2022-06-12 20:04:46.228765
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    from .test_tools import assert_equal


    assert_equal(get_shortish_repr(b'Hello', normalize=True), "'Hello'")
    assert_equal(get_shortish_repr(b'Hello', max_length=10, normalize=True),
                 "'Hello'")
    assert_equal(get_shortish_repr(b'Hello', max_length=1, normalize=True),
                 "'H'")
    assert_equal(get_shortish_repr(b'Hello', max_length=2, normalize=True),
                 "'H'")
    assert_equal(get_shortish_repr(b'Hello', max_length=3, normalize=True),
                 "'H'")

# Generated at 2022-06-12 20:04:55.252796
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(1) == '1'

    assert get_shortish_repr(1, [], max_length=0) == ''

    assert get_shortish_repr(1, [], max_length=3) == '1'

    assert get_shortish_repr(1, [], max_length=4) == '1'

    assert get_shortish_repr(1, [], max_length=5) == '1'

    assert get_shortish_repr(1234567890, [], max_length=5) == '1...0'

    assert get_shortish_repr(1234567890, [], max_length=6) == '1...0'


# Generated at 2022-06-12 20:05:06.230186
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(1) == '1'
    assert get_shortish_repr(1, max_length=1) == '1'
    assert get_shortish_repr(1, max_length=2) == '1'
    assert get_shortish_repr('abcdef') == 'abcdef'
    assert get_shortish_repr('abcdef', max_length=5) == 'ab...f'
    assert get_shortish_repr('abcdef', max_length=4) == 'ab...'
    assert get_shortish_repr('abcdef', max_length=3) == 'a...'
    assert get_shortish_repr('abcdef', max_length=2) == '...'

# Generated at 2022-06-12 20:05:10.340374
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyFile(object):
        def write(self, s):
            self.contents += s

    try:
        f = MyFile()
    except TypeError:
        return
    assert issubclass(MyFile, WritableStream)



# Generated at 2022-06-12 20:05:18.268931
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(1, ((int, lambda x: str(x)),)) == str
    assert get_repr_function(1.0, ((int, lambda x: str(x)),)) == repr

    assert get_repr_function(1.0, ((float, lambda x: str(x)),)) == str
    assert get_repr_function(1, ((float, lambda x: str(x)),)) == repr

    assert get_repr_function(1, (((int, float), lambda x: str(x)),)) == str
    assert get_repr_function((1,), (((int, float), lambda x: str(x)),)) == repr



# Generated at 2022-06-12 20:05:32.313340
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('') == "''"
    assert get_shortish_repr('abc') == "'abc'"
    assert get_shortish_repr(1) == '1'
    assert get_shortish_repr(True) == 'True'
    assert get_shortish_repr(False) == 'False'
    assert get_shortish_repr(re.compile('a')) == "re.compile('a')"

    assert get_shortish_repr([1, 2, 3]) == '[1, 2, 3]'
    assert get_shortish_repr([1, 2, 3], max_length=10) == '[1, 2, 3]'

# Generated at 2022-06-12 20:05:39.219964
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(u'hello', max_length=10) == u'hello'
    assert get_shortish_repr(u'hello', max_length=3) == u'...'
    assert get_shortish_repr(u'hello', max_length=None) == u'hello'
    assert get_shortish_repr(u'hello', max_length=0) == u''



# Generated at 2022-06-12 20:05:42.531031
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def write(self, s):
            self.s = s

    writable_stream = MyWritableStream()
    writable_stream.write(u'my string')
    assert writable_stream.s == u'my string'

# Generated at 2022-06-12 20:05:48.266272
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function([], [(None, None)]) is repr
    assert get_repr_function([], [(list, None)]) is repr
    assert get_repr_function([], [(list, lambda x: 42)]) == 42
    assert get_repr_function([], [(list, lambda x: x + 2)]) == 2
    assert get_repr_function([], [(list, lambda x: x + 2), (tuple, None)]) == 2
    assert get_repr_function(None, [(list, lambda x: x + 2), (tuple, None)]) is repr
    assert get_repr_function(None, [(list, lambda x: x + 2), (tuple, lambda x: x + 3)]) == 3

# Generated at 2022-06-12 20:05:52.375305
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('abcde', max_length=10) == 'abcde'
    assert get_shortish_repr(42, max_length=10) == '42'
    assert get_shortish_repr(list(range(20)),
                                 max_length=10) == '[0, 1, 2, ..., 17, 18, 19]'

# Generated at 2022-06-12 20:05:59.632476
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Foo:
        def write(self, s):
            assert s is not None
            pass

    class Bar(Foo):
        pass

    class Baz(Bar):
        pass

    assert issubclass(Bar, WritableStream)
    assert not issubclass(Bar, ABC)

    assert issubclass(Baz, WritableStream)
    assert not issubclass(Baz, ABC)

    bar = Bar()
    assert isinstance(bar, WritableStream)
    assert not isinstance(bar, ABC)

    baz = Baz()
    assert isinstance(baz, WritableStream)
    assert not isinstance(baz, ABC)



# Generated at 2022-06-12 20:06:09.250360
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    class A:
        pass

    assert get_shortish_repr(A()) == 'REPR FAILED'

    def custom_repr_a(a):
        assert a is a_
        return 'a'

    a_ = A()
    assert get_shortish_repr(a_, custom_repr=((type(a_), custom_repr_a),)) == 'a'

    assert get_shortish_repr(a_, custom_repr=((True, custom_repr_a),)) == 'a'

    assert get_shortish_repr(a_, custom_repr=((lambda x, y=type(a_):
                                                    isinstance(x, y),
                                               custom_repr_a),)) == 'a'


# Generated at 2022-06-12 20:06:12.429847
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    # pylint: disable=too-few-public-methods
    class MyWritableStream(WritableStream):
        def write(self, s):
            pass
    writable_stream = MyWritableStream()
    assert isinstance(writable_stream, WritableStream)



# Generated at 2022-06-12 20:06:19.737136
# Unit test for function get_repr_function
def test_get_repr_function():
    class A(object):
        pass
    class B(object):
        pass
    class C(B):
        pass
    assert get_repr_function(A(), custom_repr=[]) == repr
    assert get_repr_function(A(), custom_repr=[(A, str)]) == str
    assert get_repr_function(A(), custom_repr=[(B, str)]) == repr
    assert get_repr_function(B(), custom_repr=[(A, str)]) == repr
    assert get_repr_function(B(), custom_repr=[(B, str)]) == str
    assert get_repr_function(B(), custom_repr=[(B, str)]) == str
    assert get_repr_function(C(), custom_repr=[(B, str)]) == str

# Generated at 2022-06-12 20:06:27.263095
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(None) == 'None'
    assert get_shortish_repr(False) == 'False'
    assert get_shortish_repr(5) == '5'
    assert get_shortish_repr(5.0) == '5.0'
    assert get_shortish_repr('hello') == 'hello'
    assert get_shortish_repr('hello', max_length=3) == 'hel...'
    assert get_shortish_repr('hello', max_length=4) == 'hell...'
    assert get_shortish_repr('hello', max_length=5) == 'hello'
    assert get_shortish_repr('hello', max_length=6) == 'hello'

# Generated at 2022-06-12 20:06:37.592481
# Unit test for function get_repr_function
def test_get_repr_function():
    def a(x):
        raise NotImplementedError()
    def b(x):
        return 'b: %s' % x
    def c(x):
        return 'c: %s' % x
    def d(x):
        return 'd: %s' % x
    def e(x):
        return 'e: %s' % x

    class A: pass
    class B: pass
    class C(A): pass
    class D(A): pass
    class E(B): pass

    custom_repr = (
        (str, a),
        (B, b),
        ((A, str), c),
        (E, d),
    )
    assert get_repr_function('hello', custom_repr) is a

# Generated at 2022-06-12 20:06:42.469037
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class DumbStringIO(WritableStream):
        def __init__(self):
            self.text = ''
        def write(self, s):
            self.text += s
        def flush(self):
            pass
    dumb_string_io = DumbStringIO()
    dumb_string_io.write('hi')
    assert dumb_string_io.text == 'hi'



# Generated at 2022-06-12 20:06:50.107741
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class DummyFile:
        def write(self, s):
            self.contents = s

    dummy_file = DummyFile()

    class WritableStreamImplementingClass(WritableStream):
        def write(self, s):
            dummy_file.write(s)

    assert isinstance(WritableStreamImplementingClass(), WritableStream)
    WritableStreamImplementingClass().write('meow')
    assert dummy_file.contents == 'meow'

    class WritableStreamNotImplementingClass:
        pass

    assert not isinstance(WritableStreamNotImplementingClass(), WritableStream)



# Generated at 2022-06-12 20:06:52.760841
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A:
        def write(self, s):
            pass
    assert issubclass(A, WritableStream)

    class B:
        pass
    assert not issubclass(B, WritableStream)

    class C:
        def write(self, s):
            pass
        def read(self):
            pass
    assert not issubclass(C, WritableStream)

# Generated at 2022-06-12 20:06:58.068354
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(None) is repr

    assert get_repr_function(None, custom_repr=((lambda x: x is None, str),)) is str

    class Old:
        pass
    class New:
        pass

    assert get_repr_function(Old(), ((Old, str),)) is str
    assert get_repr_function(Old(), ((New, str),)) is repr



# Generated at 2022-06-12 20:07:00.659036
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class WritableStreamDummy(WritableStream):
        def write(self, s):
            pass

    class NotWritableStreamDummy(WritableStream):
        def not_write(self, s):
            pass

    assert issubclass(WritableStreamDummy, WritableStream)

# Generated at 2022-06-12 20:07:05.347848
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class DummyWritableStream(WritableStream):
        def write(self, s):
            'an implementation'

    assert issubclass(DummyWritableStream, WritableStream)
    assert not issubclass(DummyWritableStream, ReadableStream)



# Generated at 2022-06-12 20:07:14.780009
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert '1' == get_shortish_repr(1)
    assert '1' == get_shortish_repr(1, max_length=5)
    assert '1...2' == get_shortish_repr(slice(1, 3), max_length=7)
    assert '1...2' == get_shortish_repr(slice(1, 3), max_length=11)
    assert '1' == get_shortish_repr(slice(1, 3), max_length=9)
    assert '1' == get_shortish_repr(slice(1, 3), max_length=5)
    assert '1...2' == get_shortish_repr(slice(1, 3), max_length=6)

# Generated at 2022-06-12 20:07:19.120561
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    class Foo:
        def __repr__(self):
            return 'Foooooo!'
    class Bar:
        def __repr__(self):
            return 'Ba' * 20
    class Qux:
        def __repr__(self):
            raise Exception
    custom_repr = (
        (str, lambda s: s + '***'),
        (Foo, lambda o: o.__repr__() + '?'),
        (int, lambda i: '0x{:x}'.format(i))
    )
    assert get_shortish_repr('abc', custom_repr) == 'abc***'
    assert get_shortish_repr(Foo(), custom_repr) == 'Foooooo!?'

# Generated at 2022-06-12 20:07:28.807531
# Unit test for function get_repr_function
def test_get_repr_function():
    # Trivial tests
    assert get_repr_function(1, custom_repr=((int, lambda x: 'int: {}'.format(x)),)) == (lambda x: 'int: {}'.format(x))
    assert get_repr_function(1, custom_repr=((int, lambda x: 'int: {}'.format(x)),
                                             (None, lambda x: 'default'))) == (lambda x: 'int: {}'.format(x))

    # Tests with all-true predicate
    custom_repr = (
        (None, lambda x: 'all-true' if x else 'all-false'),
    )
    assert get_repr_function(1, custom_repr) == (lambda x: 'all-true' if x else 'all-false')

# Generated at 2022-06-12 20:07:34.849410
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    assert WritableStream.write(None, 'abc')



# Generated at 2022-06-12 20:07:39.347018
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(12345) == '12345'

    assert get_shortish_repr(12345, max_length=5) == '12...'

    assert get_shortish_repr(12345, max_length=2) == '12'

    assert get_shortish_repr(12345, max_length=None) == '12345'



# Generated at 2022-06-12 20:07:46.918900
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyStream(WritableStream):
        pass
    assert not issubclass(MyStream, WritableStream)
    class MyStream(WritableStream):
        def write(self, s): pass
    assert issubclass(MyStream, WritableStream)
    class MyStream(WritableStream):
        def write(self): pass
    assert not issubclass(MyStream, WritableStream)
    class MyStream(WritableStream):
        def write(self, s, t): pass
    assert not issubclass(MyStream, WritableStream)
    class MyStream(WritableStream):
        def write(self, s='a'): pass
    assert not issubclass(MyStream, WritableStream)
    class MyStream(WritableStream):
        def write(self, s=None): pass

# Generated at 2022-06-12 20:07:52.847415
# Unit test for function get_repr_function
def test_get_repr_function():
    class A(object): pass
    class B(A): pass
    a = A()
    b = B()

    assert get_repr_function(a, ((A, str),)) == str
    assert get_repr_function(b, ((A, str),)) == str
    assert get_repr_function(b, ((A, str), (B, lambda x: 'B!'))) == 'B!'



# Generated at 2022-06-12 20:08:01.702990
# Unit test for method write of class WritableStream
def test_WritableStream_write():

    class MyWritableStream(WritableStream):

        def write(self, s):
            self.s = s

    stream = MyWritableStream()

    try:
        stream.write(5)
    except (TypeError, AttributeError):
        pass
    else:
        raise Exception("write didn't raise `TypeError` on input which is not"
                        " a string")

    stream.write('')
    assert stream.s == ''

    stream.write('a')
    assert stream.s == 'a'

    stream.write('b')
    assert stream.s == 'b'

    stream.write(None)
    assert stream.s is None



# Generated at 2022-06-12 20:08:06.795069
# Unit test for function get_repr_function
def test_get_repr_function():
    def repr_1(x):
        return 'repr_1 was here'
    def repr_2(x):
        return 'repr_2 was here'
    custom_repr = (
        (lambda x: True, repr_1),
        (lambda x: False, repr_2),
    )
    assert get_repr_function(None, custom_repr) is repr_1
    assert get_repr_function(None) is repr



# Generated at 2022-06-12 20:08:09.062634
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A(WritableStream): pass
    class B(A):
        def write(self, s): pass
    assert issubclass(B, WritableStream)

# Generated at 2022-06-12 20:08:13.249324
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    import pytest

    class A(object):
        def __repr__(self):
            return 'I am some long string so that we can see that the truncate' \
                   ' function works'

    assert get_shortish_repr(A()) == 'I am some long string so that we can s' \
                                     'ee that the truncate function works'

    assert get_shortish_repr(A(), max_length=39) == 'I am some long stri...tion works'



# Generated at 2022-06-12 20:08:18.936000
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    from .pycompat import StringIO

    class MyWritableStream(WritableStream):
        def __init__(self, string_io):
            self.string_io = string_io

        def write(self, s):
            self.string_io.write(s)

    string_io = StringIO()
    my_writable_stream = MyWritableStream(string_io)
    my_writable_stream.write('Hello, world!')
    assert string_io.getvalue() == 'Hello, world!'



# Generated at 2022-06-12 20:08:25.537613
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(42, max_length=10) == '42'
    assert get_shortish_repr(42, max_length=9) == '42'
    assert get_shortish_repr(42, max_length=8) == '42'

    assert get_shortish_repr(1234, max_length=7) == '1234'
    assert get_shortish_repr(1234, max_length=6) == '1...4'
    assert get_shortish_repr(1234, max_length=5) == '1...4'
    assert get_shortish_repr(1234, max_length=4) == '1...4'
    assert get_shortish_repr(1234, max_length=3) == '1...4'
   