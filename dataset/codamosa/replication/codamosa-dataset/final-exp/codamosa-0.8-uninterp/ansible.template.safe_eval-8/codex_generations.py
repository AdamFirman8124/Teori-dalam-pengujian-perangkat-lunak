

# Generated at 2022-06-13 15:28:15.042127
# Unit test for function safe_eval
def test_safe_eval():
    # String literals
    assert safe_eval("foo") == "foo"
    assert safe_eval("'foo'") == "foo"
    assert safe_eval("\"foo\"") == "foo"
    assert safe_eval("'''foo'\"\"\"") == "foo"
    assert safe_eval("'''foo'''") == "foo"
    assert safe_eval("''") == ""
    # simple addition
    assert safe_eval("foo + bar") == "foobar"
    assert safe_eval("foo + 1") == "foo1"
    assert safe_eval("foo + 'bar'") == "foobar"
    assert safe_eval("1 + 2") == 3
    assert safe_eval("'foo' + 'bar'") == "foobar"
    # simple multiplication
    assert safe_eval("foo * 2")

# Generated at 2022-06-13 15:28:23.424394
# Unit test for function safe_eval
def test_safe_eval():
    safe_eval("1 + 1")
    safe_eval("1 * 1")
    safe_eval("9.4 / 3")
    safe_eval("foo")
    safe_eval("(1, 2)")
    safe_eval("[1, 2]")
    safe_eval("{'foo': 'bar'}")
    safe_eval("{foo: 'bar'}")
    safe_eval("1 == 1")
    safe_eval("true")
    safe_eval("null")
    safe_eval("x + null")
    safe_eval("x + true")
    safe_eval("x + false")
    try:
        safe_eval("1 / 0")
        assert False, "dividing by zero should not work"
    except:
        pass

# Generated at 2022-06-13 15:28:33.428725
# Unit test for function safe_eval
def test_safe_eval():
    # This test is also an example of what safe_eval() can evaluate.

    # Setup
    locals = {'fact_a': 'some string', 'fact_b': True}

    # Test basic evaluation
    result = safe_eval('fact_a', locals)
    assert isinstance(result, string_types)
    assert result == 'some string'

    # Test a true boolean
    result = safe_eval('fact_b', locals)
    assert isinstance(result, bool)
    assert result is True

    # Test a false boolean
    result = safe_eval('not fact_b', locals)
    assert isinstance(result, bool)
    assert result is False

    # Test integer
    result = safe_eval('1', locals)
    assert isinstance(result, int)
    assert result == 1

    # Test string
    result

# Generated at 2022-06-13 15:28:43.219976
# Unit test for function safe_eval
def test_safe_eval():
    print('Testing safe_eval')
    # explicit list of errors to ignore, as not all test machines
    # will support all of them
    errors = [
        'invalid function: _',
        'invalid expression ({{ foo.bar }}',
        'invalid operation ({{ foo.bar + 42 }})',
        'invalid expression ({{ foo.bar 42 }})',
        'invalid expression ({{ foo.bar(42) }})',
        'invalid function: (',
        "invalid function: 'foo'",
        'invalid function: print',
        'invalid function: sys',
        'invalid function: max',
        'invalid function: min',
        'invalid function: __import__',
        'invalid function: eval',
    ]
    # this should pass

# Generated at 2022-06-13 15:28:49.884364
# Unit test for function safe_eval
def test_safe_eval():

    def _test_expr(e, locals=None, result="unknown", include_exceptions=False):
        if locals is None:
            locals = {}

        res, exc = safe_eval(e, locals=locals, include_exceptions=include_exceptions)

        if isinstance(result, Exception):
            if exc is not None and type(exc).__name__ == result.__name__:
                return None

            raise Exception("expected exception '%s' but got %s" % (result.__name__, exc))

        if include_exceptions:
            res = res[0]

        if res != result:
            raise Exception("invalid result for '%s', got %s but expected %s" % (e, res, result))

    # Test strings
    _test_expr("a string")

# Generated at 2022-06-13 15:28:55.167021
# Unit test for function safe_eval

# Generated at 2022-06-13 15:29:05.287923
# Unit test for function safe_eval

# Generated at 2022-06-13 15:29:11.136337
# Unit test for function safe_eval
def test_safe_eval():
    expr_success = ["True", "['localhost']", "['localhost', 'example.com']",
                    "a==1", "a==1 or b==1", "'a' in 'abc'", "a.split(',')",
                    "{'a': 'b'}", "('a', 'b')", "['a', 'b', 'c']"]
    expr_failure = ["BADVARIABLE", "a.split(' ')", "a in b", "a in b.split(',')",
                    "a in b.split(',') and c==1"]
    compare_failure = ["a==2"]
    for expr in expr_success:
        res, err = safe_eval(expr, include_exceptions=True)
        assert res is not None
        assert err is None

# Generated at 2022-06-13 15:29:19.604490
# Unit test for function safe_eval
def test_safe_eval():
    import pytest

    def test_expr(expr, expected, err=None):
        try:
            result = safe_eval(expr)
        except Exception as e:
            result = e
        if expected is not None:
            assert result == expected
        else:
            assert isinstance(result, err)

    # Test non-string input
    test_expr(["bogus"], ["bogus"])
    test_expr(("bogus", ), ("bogus", ))
    test_expr({'a': 1, 'b': 2}, {'a': 1, 'b': 2})
    test_expr(set('abcd'), set(['a', 'b', 'c', 'd']), err=Exception)

    # Test safe expressions
    test_expr("1", 1)
    test_expr("False", False)

# Generated at 2022-06-13 15:29:30.545791
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('1') == 1
    assert safe_eval('[1, 2]') == [1, 2]
    assert safe_eval('{"a": "b"}') == {"a": "b"}
    assert safe_eval('1 | string') == '1'
    assert safe_eval('2+2') == 4
    assert safe_eval('1+1', {}, True) == (2, None)

    # Test some blacklisted expressions

# Generated at 2022-06-13 15:29:41.319512
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('foo') == 'foo'
    assert safe_eval('foo.bar') == 'foo.bar'
    assert safe_eval('foo["bar"]') == 'foo["bar"]'
    assert safe_eval('foo.bar()') == 'foo.bar()'
    assert safe_eval('foo[bar]', dict(bar='baz')) == 'foo[bar]'
    assert safe_eval('foo[bar]()', dict(bar='baz')) == 'foo[bar]()'
    assert safe_eval('foo.bar()[baz]') == 'foo.bar()[baz]'
    assert safe_eval('foo.bar()[baz]()') == 'foo.bar()[baz]()'

# Generated at 2022-06-13 15:29:52.356439
# Unit test for function safe_eval
def test_safe_eval():
    # test list
    assert safe_eval("[1, 2, [3]]") == [1, 2, [3]]
    assert safe_eval("['a', 'b', ['c']]") == ['a', 'b', ['c']]
    assert safe_eval("['1', '2', ['3']]") == ['1', '2', ['3']]
    assert safe_eval("[1, '2', 3]") == [1, '2', 3]

    # test dict
    assert safe_eval("{'a': 1, 'b': 2}") == {'a': 1, 'b': 2}
    assert safe_eval("{1: 'a', 2: 'b'}") == {1: 'a', 2: 'b'}

# Generated at 2022-06-13 15:30:00.309167
# Unit test for function safe_eval
def test_safe_eval():
    # Make sure safe_eval doesn't evaluate this as Python code
    # - just returns the expression string as-is
    code_expr = "1 + 1"
    result = safe_eval(code_expr)
    assert result == code_expr, \
           'safe_eval incorrectly evaluated {0}'.format(container_to_text(expr))

    # Regular expressions are not allowed
    expr = 're.search("expression", "test expression")'
    result = safe_eval(expr)
    assert result == expr, \
           'safe_eval incorrectly evaluated {0}'.format(container_to_text(expr))

    # Evaluate a simple expression
    expr = '1 + 1'
    result = safe_eval(expr)

# Generated at 2022-06-13 15:30:08.204037
# Unit test for function safe_eval
def test_safe_eval():
    # See test/utils/test_safe_eval.py for a more complete set of tests
    # Negative tests
    expr = '__import__("os").mkdir("/tmp/test_safe_eval")'
    assert safe_eval(expr) == expr
    expr = '1+a'
    assert safe_eval(expr, {'a': 2}) == expr
    expr = '1+2+3()'
    assert safe_eval(expr) == expr
    expr = '"abc" in globals()'
    assert safe_eval(expr) == expr

    # Positive tests
    expr = 'True'
    assert safe_eval(expr)
    expr = 'false'
    assert not safe_eval(expr)
    expr = '1'
    assert safe_eval(expr) == 1
    expr = '1+2'

# Generated at 2022-06-13 15:30:18.623924
# Unit test for function safe_eval
def test_safe_eval():
    # No exception raised
    assert safe_eval("2+2") == 4
    assert safe_eval("'abcd'") == "abcd"
    assert safe_eval("'abcd'+'efgh'") == "abcdefgh"
    assert safe_eval("len(['a', 'b', 'c'])") == 3
    assert safe_eval("['a', 'b', 'c'][0]") == "a"
    assert safe_eval("['a', 'b', 'c'][-1]") == "c"
    assert safe_eval("'foo' in ['a', 'b', 'c']") is False
    assert safe_eval("'a' in ['a', 'b', 'c']") is True
    assert safe_eval("'abcd' in 'abcde'") is True
    assert safe_

# Generated at 2022-06-13 15:30:26.902213
# Unit test for function safe_eval
def test_safe_eval():
    expr = "True and True"

    (result, exception) = safe_eval(expr, {}, True)
    assert(isinstance(result, bool))
    assert(result is True)
    assert(exception is None)

    expr = "[1, 2, 3, 4]"

    (result, exception) = safe_eval(expr, {}, True)
    assert(isinstance(result, list))
    assert(exception is None)

    expr = "{'a': 1, 'b': 2}"

    (result, exception) = safe_eval(expr, {}, True)
    assert(isinstance(result, dict))
    assert(exception is None)

    expr = "my_bad_var"

    (result, exception) = safe_eval(expr, {}, True)

# Generated at 2022-06-13 15:30:33.255731
# Unit test for function safe_eval
def test_safe_eval():
    # These tests should pass
    assert safe_eval("[1, [2, 3]]") == [1, [2, 3]]
    assert safe_eval("{'foo': 'bar'}") == {'foo': 'bar'}
    assert safe_eval("True") is True
    assert safe_eval("True and False") is False
    assert safe_eval("'foo' not in ['bar', 'baz']") is True

    if C.DEFAULT_TRANSFORM_REQUIRED is False:
        assert safe_eval("ansible_default_ipv4.address")
        assert safe_eval("ansible_default_ipv4['address']")
    else:
        msg = "Vault transformations require DEFAULT_TRANSFORM_REQUIRED to be set to True."

# Generated at 2022-06-13 15:30:42.385705
# Unit test for function safe_eval
def test_safe_eval():
    # pylint: disable=unused-variable

    # test 1: null value
    try:
        null_result, null_exc = safe_eval("null", {}, True)
        if null_result is not None:
            return False
    except Exception as e:
        return False

    # test 2: truth values
    try:
        truth_result, truth_exc = safe_eval("true or false", {}, True)
        if not truth_result:
            return False
    except Exception as e:
        return False

    # test 3: bool ops
    try:
        bool_true = safe_eval("1 == 1")
        bool_false = safe_eval("2 == 3")
        if not bool_true or bool_false:
            return False
    except Exception as e:
        return False

    # test 4:

# Generated at 2022-06-13 15:30:53.066639
# Unit test for function safe_eval
def test_safe_eval():
    # Create a dictionary containing builtin functions
    # which will represent our module's builtins
    import_module = __import__


# Generated at 2022-06-13 15:30:56.927563
# Unit test for function safe_eval
def test_safe_eval():
    data = [
        "{{ test_var }}",
        "['foo', 'bar', 'baz']",
        "('foo', 'bar', 'baz')",
        "{'foo': 'bar', 'bar': 'baz'}",
        "True",
        "False",
        "None",
        "1+2*3",
        "(1+2)*3",
        "2-1",
        "2**10",
        "round(1.23, 1)",
        "false",
        "true",
        "null"
    ]

    for d in data:
        try:
            print(d, '=>', safe_eval(d))
        except Exception as e:
            print(d, '=>', str(e))

if __name__ == '__main__':
    test_safe_

# Generated at 2022-06-13 15:31:13.309140
# Unit test for function safe_eval
def test_safe_eval():
    my_dict = dict(
        one=1,
        two=dict(
            list=[1, 2, 3],
            string='foo',
            bool=True,
            none=None,
        )
    )

    # no errors raised
    safe_eval("{{ one }}")
    safe_eval("{{ one }}", dict(one=1))
    safe_eval("{{ one }}", dict(one='foo'))

    safe_eval("{{ one }}", dict(one=1))
    safe_eval("{{ one }}", dict(one='foo'))

    safe_eval("{{ one }}", dict(one=1))
    safe_eval("{{ two.list.0 }}", dict(two=dict(list=[1, 2, 3])))

# Generated at 2022-06-13 15:31:24.201427
# Unit test for function safe_eval

# Generated at 2022-06-13 15:31:33.110050
# Unit test for function safe_eval
def test_safe_eval():
    # json data types
    assert safe_eval('"string"')    == "string"
    assert safe_eval('u"string"')   == "string"
    assert safe_eval('1')           == 1
    assert safe_eval('1.1')         == 1.1
    assert safe_eval('1.1e-1')      == 0.11
    assert safe_eval('1000000000')  == 1000000000
    assert safe_eval('false')       == False
    assert safe_eval('false')       == False
    assert safe_eval('-123')        == -123
    assert safe_eval('-123.456')    == -123.456
    assert safe_eval('-123.456e-2') == -1.23456

    # json built-in constants
    assert safe_eval('True')      == True
   

# Generated at 2022-06-13 15:31:38.908816
# Unit test for function safe_eval
def test_safe_eval():
    pass_expr = [
        "None",
        "True",
        "False",
        "false",
        "true",
        "null",
        "a == '1'",
        "a == 'a'",
        "a != 'a'",
        "1 + 2 + 3 - 3 - 2 - 1",
        "1 + 2 * 3 - 3 / 2 - 1",
        "1 + 2 * (3 - 3) / 2 - 1",
        "1 + a * 3 - 3 / 2 - 1",
        "1 + b[0] * 3 - 3 / 2 - 1",
        "''.join(['1'])",
        "','.join(['1'])",
        "','.join([str(x) for x in [1]])",
    ]

    for expr in pass_expr:
        res

# Generated at 2022-06-13 15:31:46.222520
# Unit test for function safe_eval
def test_safe_eval():
    '''
    unit test for function safe_eval
    '''
    LOCALS = {}

    # exception test cases

# Generated at 2022-06-13 15:31:56.144790
# Unit test for function safe_eval
def test_safe_eval():
    # Basic booleans
    assert safe_eval('true') is True
    assert safe_eval('True') is True
    assert safe_eval('false') is False
    assert safe_eval('False') is False

    # Basic numbers
    assert safe_eval('1') == 1
    assert safe_eval('1 + 1') == 2

    # String literals
    assert safe_eval('"foo"') == 'foo'

    # String literals with quotes in them
    assert safe_eval('"foo \' bar"') == 'foo \' bar'
    assert safe_eval('"foo \" bar"') == 'foo " bar'
    assert safe_eval('"foo \' \" bar"') == 'foo \' " bar'
    assert safe_eval('"foo \" \' bar"') == 'foo " \' bar'

    # Unicode strings
    assert safe

# Generated at 2022-06-13 15:32:06.229654
# Unit test for function safe_eval
def test_safe_eval():
    try:
        from ast import literal_eval
        from ansible.module_utils.six import string_types
    except Exception:
        print("SKIP: no safe_eval unit tests because the Python ast module is not available")
        sys.exit(0)

    # Test safe evals
    assert safe_eval("1 == 1")

    assert safe_eval("1 + 1") == 2
    assert safe_eval("1 + 1") == literal_eval("1 + 1")

    assert safe_eval("'1 + 1'") == '1 + 1'
    assert safe_eval("'1 + 1'") == literal_eval("'1 + 1'")

    assert safe_eval("1 + 1", include_exceptions=True) == (2, None)
    assert safe_eval("'1 + 1'", include_exceptions=True)

# Generated at 2022-06-13 15:32:18.180473
# Unit test for function safe_eval
def test_safe_eval():
    # These tests should not raise an exception, while using with_items
    assert safe_eval('item.0') is None
    assert safe_eval('ansible_eth0.device') is None

    # These tests should raise an exception, while using with_items
    try:
        safe_eval('item.0.ansible_eth0')
    except Exception as e:
        assert isinstance(e, Exception)
    try:
        safe_eval('ansible_eth0')
    except Exception as e:
        assert isinstance(e, Exception)

    # Tests for public API (since 2.6)
    # These tests should not raise an exception, and instead return
    # the same value back
    assert safe_eval('1') == 1
    assert safe_eval('1.0') == 1.0

# Generated at 2022-06-13 15:32:29.989625
# Unit test for function safe_eval
def test_safe_eval():
    # Make sure things which should work, do
    assert safe_eval('1 + 1', {}) == 2
    assert safe_eval('"foo %s" % "bar"', {}) == 'foo bar'
    assert safe_eval('"foo" == "foo"', {}) is True
    assert safe_eval('"foo" != "foo"', {}) is False
    assert safe_eval('"foo" in "foobar"', {}) is True
    assert safe_eval('[1, 2, 3]', {}) == [1, 2, 3]
    assert safe_eval('{"k1": "v1", "k2": "v2"}', {}) == {u'k2': u'v2', u'k1': u'v1'}
    assert safe_eval('True', {}) is True
    assert safe_

# Generated at 2022-06-13 15:32:40.187775
# Unit test for function safe_eval
def test_safe_eval():

    assert safe_eval("1 + 1") == 2
    assert safe_eval("'a' + 'b'") == 'ab'
    assert safe_eval("'a' + 'b' + \"c\"") == 'abc'
    assert safe_eval("('a' + 'b' + \"c\") * 2") == 'abcc'

    assert safe_eval("1.0 + 1") == 2.0
    assert safe_eval("1.0 + 1.0") == 2.0
    assert safe_eval("1.0 + 1.1") == 2.1

    assert safe_eval("2 / 6") == 0
    assert safe_eval("1.0 / 6") == 0.16666666666666666
    assert safe_eval("2.0 / 6.0") == 0.3333333333333333


# Generated at 2022-06-13 15:33:05.186932
# Unit test for function safe_eval

# Generated at 2022-06-13 15:33:16.096727
# Unit test for function safe_eval

# Generated at 2022-06-13 15:33:27.031484
# Unit test for function safe_eval
def test_safe_eval():
    """
    Test safe_eval function.
    """

    # Assert that safe_eval is working given a valid expression.
    assert safe_eval('5*5') == 25

    # Assert that safe_eval is working given a valid expression
    assert safe_eval('"hello world"') == "hello world"

    # Assert that safe_eval is working given a valid expression (numbers)
    # Passing in the number 5 should return an integer
    assert safe_eval('5') == 5
    # Passing in the number 5.0 should return an float
    assert isinstance(safe_eval('5.0'), float)
    # Passing in the number 5j should return an complex
    assert isinstance(safe_eval('5j'), complex)

    # Assert that safe_eval is working given a valid expression
    # Passing in the string '5'

# Generated at 2022-06-13 15:33:38.048678
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('1 + 2') == 3
    assert safe_eval('True')
    assert safe_eval('false') is False
    assert safe_eval('null') is None
    assert safe_eval('"foo"') == 'foo'
    assert safe_eval('foo') == 'foo'
    assert safe_eval('[1, 2, 3]') == [1, 2, 3]
    assert safe_eval('(1, 2, 3)') == (1, 2, 3)
    assert safe_eval('{"a": 1, "b": 2}') == {'a': 1, 'b': 2}
    assert safe_eval('1 + 2', include_exceptions=True)[0] == 3
    assert safe_eval('foo', {'foo': 'bar'}) == 'bar'

# Generated at 2022-06-13 15:33:48.765437
# Unit test for function safe_eval
def test_safe_eval():
    '''
    Basic unit test for function safe_eval
    '''
    assert safe_eval('1 + 1') == 2
    assert safe_eval('"foo".strip()') == 'foo'
    assert safe_eval('dict(a=1, b=2)') == {'a': 1, 'b': 2}
    assert safe_eval('["foo", 3, None]') == ['foo', 3, None]
    assert safe_eval('dict(a=1, b=2)') == {'a': 1, 'b': 2}
    assert safe_eval('dict(a=1, b=2)') == {'a': 1, 'b': 2}

    assert safe_eval('__import__("os")', include_exceptions=True)[0] == None

# Generated at 2022-06-13 15:33:58.431257
# Unit test for function safe_eval
def test_safe_eval():
    # Test Python 3
    sys.version_info[0] = 3
    assert safe_eval("1 + 1") == 2
    assert safe_eval("1 + 1", include_exceptions=True) == (2, None)
    assert safe_eval("a_list", {"a_list": [1, 2, 3]}) == [1, 2, 3]
    assert safe_eval("a_list", {"a_list": [1, 2, 3]}, include_exceptions=True) == ([1, 2, 3], None)
    assert safe_eval("a_list", include_exceptions=True) == ("a_list", None)
    assert safe_eval("not there", include_exceptions=True) == ("not there", None)

# Generated at 2022-06-13 15:34:06.691561
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('[]') == []
    assert safe_eval('[1, 2, 3]') == [1, 2, 3]
    assert safe_eval('{"foo": "bar"}') == {"foo": "bar"}
    assert safe_eval('{"foo": "{{bar}}"}', dict(bar='baz')) == {"foo": "baz"}
    # complex python expressions
    assert safe_eval('(x for x in range(10))', dict(x='a')) == ('a',)
    assert safe_eval('key{{1}}', dict(key1='foo', key2='bar')) == 'foo'
    # None should still be none
    assert safe_eval('None') is None

# Unit tests for function container_to_text

# Generated at 2022-06-13 15:34:14.943209
# Unit test for function safe_eval
def test_safe_eval():

    # Functionality

    # strings and numbers
    assert safe_eval("1") == 1
    assert safe_eval("'foobar'") == "foobar"
    assert safe_eval("'$foo'") == "$foo"

    # list and dict literals
    assert safe_eval("[]") == []
    assert safe_eval("{}") == {}
    assert safe_eval("[1, 2]") == [1, 2]
    assert safe_eval("{'foo': 1, 'bar': 2}") == {'foo': 1, 'bar': 2}

    # literals combined with operators
    assert safe_eval("1 + 1") == 2
    assert safe_eval("[1, 2] * 2") == [1, 2, 1, 2]

    # arbitrary expressions no longer allowed
    exc = None

# Generated at 2022-06-13 15:34:25.255631
# Unit test for function safe_eval
def test_safe_eval():
    # Test for invalid expressions
    for expr in [
        'not_allowed_function()',
        'ansible_test_func("test")',
        'len("test")',
        'close("test")',
        'open("test")',
    ]:
        (eval_result, eval_exc) = safe_eval(expr, include_exceptions=True)
        assert eval_result == expr
        assert isinstance(eval_exc, Exception) is True

    # Test for valid expressions

# Generated at 2022-06-13 15:34:32.536638
# Unit test for function safe_eval

# Generated at 2022-06-13 15:35:00.309857
# Unit test for function safe_eval
def test_safe_eval():
    # Test simple cases
    assert safe_eval("2+2") == 4
    assert safe_eval("4-2") == 2
    assert safe_eval("4*2") == 8
    assert safe_eval("4/2") == 2

    # Test boolean literals
    assert safe_eval("1 == 1") is True
    assert safe_eval("1 != 0") is True
    assert safe_eval("True and True") is True
    assert safe_eval("True or False") is True

    # Test list literals
    assert safe_eval("['hello','world']") == ['hello','world']

    # Test invalid expressions
    assert safe_eval("1/0") == "1/0"

# Generated at 2022-06-13 15:35:05.302725
# Unit test for function safe_eval
def test_safe_eval():
    '''
    This is here to help with development and testing.
    '''
    print("Testing functions in module: %s" % __file__)
    print("safe_eval(...):")

    # Error handling
    # eval should raise an exception
    if True:
        # This expression is built via ast.dump(parse("1(")) from pythons ast module
        expr = "Expression(body=Call(func=Name(id='1', ctx=Load()), args=[], keywords=[], starargs=None, kwargs=None))"
        (result, exception) = safe_eval(expr, include_exceptions=True)
        assert isinstance(exception, Exception)

    # safe_eval should return the expression if an exception occurs

# Generated at 2022-06-13 15:35:13.736229
# Unit test for function safe_eval

# Generated at 2022-06-13 15:35:22.249757
# Unit test for function safe_eval
def test_safe_eval():

    def raises(func, exception, *args, **kwargs):
        # Python 2.6 does not have assertRaisesRegexp
        try:
            func(*args, **kwargs)
            raise Exception('Expected exception %s' % exception)
        except exception:
            pass

    # Use boolean expressions
    # FIXME: Add more tests
    assert safe_eval('true') is True
    assert safe_eval('True') is True
    assert safe_eval('false') is False
    assert safe_eval('False') is False

    # Use built-in functions
    assert safe_eval('len([1, 2, 3])') == 3
    raises(lambda: safe_eval('open("/tmp/file")'), NameError)

    # Use variables

# Generated at 2022-06-13 15:35:32.134712
# Unit test for function safe_eval
def test_safe_eval():
    '''
    Unit tests for function safe_eval
    '''
    if sys.version_info >= (3,):
        long = int


# Generated at 2022-06-13 15:35:39.674051
# Unit test for function safe_eval
def test_safe_eval():
    # basic tests
    assert safe_eval("2+2") == 4
    assert safe_eval("2+2", include_exceptions=True) == (4, None)
    assert safe_eval("[1,2,3]") == [1,2,3]
    assert safe_eval("[1,2,3]", include_exceptions=True) == ([1,2,3], None)
    assert safe_eval("{'okey':'dokey'}") == {'okey':'dokey'}
    assert safe_eval("{'okey':'dokey'}", include_exceptions=True) == ({'okey':'dokey'}, None)

    # nested data structures

# Generated at 2022-06-13 15:35:43.585475
# Unit test for function safe_eval
def test_safe_eval():
    # check simple literals
    assert safe_eval(123) == 123
    assert safe_eval('"abc"') == "abc"
    assert safe_eval("None") is None
    assert safe_eval("true") is True
    assert safe_eval("false") is False

    # Ensure dicts and lists can be constructed with int and string literals
    assert safe_eval('{"a":1, "b":2}') == {"a":1, "b":2}
    assert safe_eval('[1,2,3]') == [1,2,3]

    # check basic math
    assert safe_eval('1 + 1') == 2
    assert safe_eval('1 - 1') == 0
    assert safe_eval('2 * 2') == 4
    assert safe_eval('4 / 2') == 2

    # check precedence
   

# Generated at 2022-06-13 15:35:53.618593
# Unit test for function safe_eval

# Generated at 2022-06-13 15:36:04.162838
# Unit test for function safe_eval
def test_safe_eval():
    # Successful evals
    assert safe_eval('[]') == []
    assert safe_eval('{}') == {}
    assert safe_eval('[1,2,3]') == [1,2,3]
    assert safe_eval('{"a":1,"b":2,"c":3}') == {"a":1,"b":2,"c":3}
    assert safe_eval('1') == 1
    assert safe_eval('"a string"') == "a string"
    assert safe_eval('1+1') == 2
    assert safe_eval('1+1>2') == False
    assert safe_eval('1+1>2 and False') == False
    assert safe_eval('(1,2)') == (1,2)

# Generated at 2022-06-13 15:36:12.101573
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval("1 + 1") == 2
    assert safe_eval("foo") == 'foo'
    assert safe_eval("foo.bar") == 'foo.bar'
    assert safe_eval("foo['bar']") == "foo['bar']"
    assert safe_eval("foo['bar']", dict(foo=dict(bar=True)))

    try:
        safe_eval("__import__('os').remove('/etc/passwd')")
        assert False  # Execution should never reach here
    except Exception:
        pass

    try:
        safe_eval("__builtins__.__import__('os').remove('/etc/passwd')")
        assert False  # Execution should never reach here
    except Exception:
        pass


# Generated at 2022-06-13 15:36:35.399269
# Unit test for function safe_eval
def test_safe_eval():
    # Verify that safe_eval works as expected

    # Test safe_eval works when EXPECTED_EXCEPTION is set
    EXPECTED_EXCEPTION = Exception
    try:
        safe_eval('1 + 1', include_exceptions=True)
    except Exception as e:
        assert type(e) == EXPECTED_EXCEPTION
        return
    assert False, "Safe_eval did not fail with exception as expected"

    EXPECTED_EXCEPTION = None
    # Test safe_eval works as expected when a valid expression is passed
    assert safe_eval('1 + 1', include_exceptions=True) == (2, EXPECTED_EXCEPTION)

    # Test safe_eval fails as expected when an invalid expression is passed

# Generated at 2022-06-13 15:36:43.917746
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval("a") == "a"
    assert safe_eval("a.b") == "a.b"
    assert safe_eval("['a', 'b']") == ['a', 'b']
    assert safe_eval("{'a': 1}") == {'a': 1}
    assert safe_eval("foo(a, b)") == 'foo(a, b)'
    assert safe_eval("a + 'b'") == "a + 'b'"
    assert safe_eval("1 + 1") == 2
    assert safe_eval("a_list_variable") == 'a_list_variable'
    assert safe_eval("a_dict_variable") == 'a_dict_variable'

    # Evaluating a call to a builtin function should fail.

# Generated at 2022-06-13 15:36:55.388895
# Unit test for function safe_eval
def test_safe_eval():
    # Types
    assert safe_eval('1') == 1
    assert safe_eval('100') == 100
    assert safe_eval('1.1') == 1.1
    assert safe_eval('"a"') == "a"
    assert safe_eval("'a'") == "a"
    assert safe_eval('"a" * 2') == "aa"
    assert safe_eval("'a' * 2") == "aa"
    assert safe_eval('1 == 2') is False
    assert safe_eval('1 != 2') is True
    assert safe_eval('1 < 2') is True
    assert safe_eval('1 <= 2') is True
    assert safe_eval('1 > 2') is False
    assert safe_eval('1 >= 2') is False
    assert safe_eval('[]') == []
    assert safe_eval

# Generated at 2022-06-13 15:37:03.833496
# Unit test for function safe_eval
def test_safe_eval():
    def test_eval(expr, expected_result):
        if isinstance(expected_result, Exception):
            evaled, failure = safe_eval(expr, include_exceptions=True)
            assert failure
            assert isinstance(failure, expected_result)
            assert evaled == expr
        else:
            evaled, failure = safe_eval(expr, include_exceptions=True)
            assert not failure
            assert evaled == expected_result

    def test(expr, result):
        test_eval(expr, result)
        # test_eval(expr, result)

    # Basic testing
    yield test, "1", 1
    yield test, "a", 'a'
    yield test, "a.b", 'a.b'
    yield test, "1 + 2", 3

# Generated at 2022-06-13 15:37:12.429670
# Unit test for function safe_eval
def test_safe_eval():
    def _test_safe_eval(eval_string, expected_result, test_name, error_expected=False, msg=None):
        result, exception = safe_eval(eval_string, include_exceptions=True)
        if error_expected:
            if exception is None:
                sys.stdout.write("failed: " + test_name + " (should have raised exception)\n")
                return False
            else:
                sys.stdout.write("passed: " + test_name + "\n")
                return True
        elif exception:
            sys.stdout.write("failed: " + test_name + " (" + to_native(exception) + ")\n")
            return False

# Generated at 2022-06-13 15:37:14.105569
# Unit test for function safe_eval
def test_safe_eval():
    expr = '{{ num1|random }}'
    try:
        eval(expr)
    except:
        safe_eval(expr)
        assert True

if __name__ == '__main__':
    test_safe_eval()

# Generated at 2022-06-13 15:37:22.695630
# Unit test for function safe_eval
def test_safe_eval():
    def assert_safe_eval(expr, expected):
        actual = safe_eval(expr)
        assert expected == actual

    assert_safe_eval("a_list_variable", "a_list_variable")
    assert_safe_eval("a_list_variable[0]", "a_list_variable[0]")
    assert_safe_eval("a_list_variable[0].whatever", "a_list_variable[0].whatever")
    assert_safe_eval("a_list_variable.0.whatever", "a_list_variable.0.whatever")
    assert_safe_eval("foobar == 'monkey'", "foobar == 'monkey'")
    assert_safe_eval("(foobar == 'monkey') and (banana == 'split')", "(foobar == 'monkey') and (banana == 'split')")
   

# Generated at 2022-06-13 15:37:34.076727
# Unit test for function safe_eval

# Generated at 2022-06-13 15:37:44.205736
# Unit test for function safe_eval
def test_safe_eval():
    """Unit test for safe_eval"""

    # Simple literals
    literal_tests = [
        ("'A string'", "A string"),
        ("1", 1),
        ("1.0", 1.0),
        ("True", True),
        ("False", False),
    ]
    for expr, expected in literal_tests:
        result = safe_eval(expr)
        assert result == expected, "%r: expected %r, got %r" % (expr, expected, result)

    # String concatenation (only allowed if no builtins called)

# Generated at 2022-06-13 15:37:54.524089
# Unit test for function safe_eval
def test_safe_eval():

    _test_safe_eval_ok('42')
    _test_safe_eval_ok('4.2')
    _test_safe_eval_ok('42j')

    _test_safe_eval_ok('42 + 3')
    _test_safe_eval_ok('42 - 3')
    _test_safe_eval_ok('42 * 3')
    _test_safe_eval_ok('42 / 3')

    _test_safe_eval_ok('42 + 3 * 5')
    _test_safe_eval_ok('42 + (3 * 5)')

    _test_safe_eval_ok('[42]')
    _test_safe_eval_ok('[42, 3, 5]')

    _test_safe_eval_ok('(42,)')