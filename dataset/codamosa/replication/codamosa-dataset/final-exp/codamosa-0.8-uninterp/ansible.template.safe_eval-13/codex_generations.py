

# Generated at 2022-06-13 15:28:07.357318
# Unit test for function safe_eval
def test_safe_eval():
    """
    Safely evaluates a python expression in a sandboxed environment.
    """
    assert safe_eval('a.b.c.d', {u'a': {u'b': {u'c': {u'd': 'foo'}}}}) == 'foo'
    assert safe_eval('a.b.c.d', {u'a': {u'b': {u'c': {u'd': 'foo'}}}}) == 'foo'
    assert safe_eval('a.b.c.d', {u'a': {u'b': {u'c': {u'd': u'foo'}}}}) == 'foo'
    assert safe_eval('(a=="foo")', {u'a': 'foo'}) is True

# Generated at 2022-06-13 15:28:16.656535
# Unit test for function safe_eval

# Generated at 2022-06-13 15:28:24.679639
# Unit test for function safe_eval
def test_safe_eval():
    expr = "a * b * c + d * e * f + (g + h)"
    # Test case: regular expression evaluation
    assert eval(expr, {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}) == 198
    assert safe_eval(expr, {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}) == 198
    # Test case: regex with underscores
    assert safe_eval('a_b_c', {"a_b_c": 'd'}) == 'd'
    # Test case: invalid identifier (syntax error)
    # Note: invalid identifiers are not error in Python
    # assert safe_eval

# Generated at 2022-06-13 15:28:34.618779
# Unit test for function safe_eval
def test_safe_eval():
    # This test is based on the code
    # https://stackoverflow.com/questions/12523516/using-ast-and-whitelists-to-make-pythons-eval-safe/12528004#12528004

    def test_expr(expr):
        print("Testing %s" % expr)
        ret = safe_eval(expr)
        print("Result is: %s" % ret)
        return ret

    assert test_expr('[1,2,3]') == [1, 2, 3]
    assert test_expr('{"foo": "bar"}') == {"foo": "bar"}

    assert test_expr('__import__("os").getcwd()') == '/'
    assert test_expr('__import__("os").getcwd()') == '/'


# Generated at 2022-06-13 15:28:44.131350
# Unit test for function safe_eval
def test_safe_eval():
    """
    Test for function safe_eval

    :return:
    """
    if sys.version_info >= (3, 0):
        import unittest
        import ansible.module_utils.common.json_utils as json_utils

        class TestSafeEval(unittest.TestCase):
            """
            Test case for function safe_eval
            """

            def test_eval_success(self):
                """
                Test function safe_eval in success case

                :return:
                """
                assert safe_eval('"string"') == 'string'
                assert safe_eval('"string"', include_exceptions=True)[1] is None
                assert safe_eval('["a","b"]') == ['a', 'b']

# Generated at 2022-06-13 15:28:50.632354
# Unit test for function safe_eval
def test_safe_eval():
    '''
    For every test, we will make sure we didn't cause an
    exception and will make sure that the result is correct.
    '''

    def is_correct(expr, expected):

        result, exc = safe_eval(expr, include_exceptions=True)

        # ensure we didn't cause an exception
        assert exc is None, "An exception occurred during test - this is not expected"
        assert result == expected, "Result of evaluation was not as expected"


# Generated at 2022-06-13 15:28:59.393168
# Unit test for function safe_eval
def test_safe_eval():
    if C.DEFAULT_DEBUG:
        import sys, os
        fd, fn = tempfile.mkstemp(prefix='ansible-test-safe_eval-')
        print()

# Generated at 2022-06-13 15:29:08.379932
# Unit test for function safe_eval

# Generated at 2022-06-13 15:29:14.108566
# Unit test for function safe_eval

# Generated at 2022-06-13 15:29:21.107167
# Unit test for function safe_eval
def test_safe_eval():
    ''' Helper function to run tests against safe_eval '''
    def _test_safe_eval(expr, expected, expected_type=type(None), expected_exception=None, expected_exception_type=None):
        if C.DEFAULT_DEBUG:
            print("Testing '%s'" % expr)
        result, exception = safe_eval(expr, include_exceptions=True)
        if (exception is None):
            if (expected_exception is not None):
                raise Exception("No exception raised when expecting exception '%s' for '%s'" % (expected_exception, expr))
            if (isinstance(result, expected_type)):
                if (result == expected):
                    if C.DEFAULT_DEBUG:
                        print("Success: %s == %s" % (result, expected))
                    return True


# Generated at 2022-06-13 15:29:33.799300
# Unit test for function safe_eval
def test_safe_eval():
    '''
    test_safe_eval
    '''

    # ToDO: test the try/except block.
    # Currently it passes the expression as string if it fails.

    # Test some simple arithmetic
    expression = "100*45+69"
    assert safe_eval(expression) == 4569

    expression = "100*(45+69)"
    assert safe_eval(expression) == 4600

    expression = "100*(45+69)-1"
    assert safe_eval(expression) == 4599

    expression = "100*(45+69)-1-4200"
    assert safe_eval(expression) == -1

    expression = "-1-4200"
    assert safe_eval(expression) == -4201

    expression = "[i for i in range(5)]"

# Generated at 2022-06-13 15:29:41.447353
# Unit test for function safe_eval
def test_safe_eval():
    # Test a dictionary.  There is no valid string representation
    # of a dictionary that can be used with eval(), so we won't
    # try to construct a string of a dictionary - we'll just
    # run safe_eval() on a dictionary.
    # Note: it is worth noting that dictionary keys without
    #       quotes are not interpreted as strings by ast.literal_eval,
    #       but they *will be* interpreted as strings by safe_eval
    a_dict = {
        "a": True,
        "b": False,
        "c": None,
        "d": {
            "e": True
        }
    }
    test = safe_eval(a_dict)
    assert test == a_dict, "safe_eval failed with a valid dictionary"

    # Test a list.  This is the same as the dictionary test


# Generated at 2022-06-13 15:29:52.468657
# Unit test for function safe_eval
def test_safe_eval():
    cleartext = "some_var.rsplit(',')[1]"
    assert safe_eval(cleartext, {'some_var': "a,b"}) == 'b'
    cleartext = "1 % 2"
    assert safe_eval(cleartext) == 1 % 2
    cleartext = "len([0,1,2,3])"
    assert safe_eval(cleartext) == 4
    cleartext = "True"
    assert safe_eval(cleartext) == True
    cleartext = "True and False"
    assert safe_eval(cleartext) == False
    cleartext = "[1,2,3].index(1)"
    assert safe_eval(cleartext) == 0
    cleartext = "[1,2,3][-1]"
    assert safe

# Generated at 2022-06-13 15:30:00.389320
# Unit test for function safe_eval
def test_safe_eval():
    # successful evals
    assert safe_eval('[1,2,3,4]') == [1,2,3,4]
    assert safe_eval('{"k": "v"}') == {'k': 'v'}
    assert safe_eval('1 + 2') == 3
    assert safe_eval('null') is None
    assert safe_eval('true') is True
    assert safe_eval('false') is False
    assert safe_eval('(1, 2)') == (1, 2)

    # unsuccessful evals
    assert safe_eval('__import__("os").listdir("/tmp")') == '__import__("os").listdir("/tmp")'

# Generated at 2022-06-13 15:30:08.258982
# Unit test for function safe_eval
def test_safe_eval():
    # make sure safe_eval with default options does not work
    assert safe_eval('1 + 1') == '1 + 1'
    assert safe_eval('[1, 2, 3]') == '[1, 2, 3]'
    assert safe_eval('foo') == 'foo'
    assert safe_eval('foo.bar') == 'foo.bar'
    assert safe_eval('foo()') == 'foo()'
    assert safe_eval('foo(1, 2, 3)') == 'foo(1, 2, 3)'
    assert safe_eval('foo[1, 2, 3]') == 'foo[1, 2, 3]'
    assert safe_eval('foo[0]') == 'foo[0]'

    # now with safe_eval to work

# Generated at 2022-06-13 15:30:18.670694
# Unit test for function safe_eval
def test_safe_eval():

    # Don't worry about any of these symbols being defined in the test script
    expr_symbols = set(['a', 'b', 'c', 'd'])

    def check_expression(expr, expected):
        expr_symbols_used = set(expr.replace(',', ' ').replace('[', ' ').replace(']', ' ').split())
        assert expr_symbols.issuperset(expr_symbols_used), 'The expression %s uses undefined symbols: %s' % (expr, ', '.join(expr_symbols_used-expr_symbols))
        result = safe_eval(expr)

# Generated at 2022-06-13 15:30:26.926461
# Unit test for function safe_eval
def test_safe_eval():

    # Make sure safe_eval is capable of evaluating simple expressions while
    # not allowing any kind of code execution

    assert safe_eval("1 + 1") == 2
    assert safe_eval("'hello ' + 'world'") == 'hello world'

    tests = ["__import__('os').system('touch foo')",
             "__import__('tempfile').mkstemp()",
             "[x for x in range(10)]",
             "{x: x for x in range(10)}",
             """
             def foo():
                pass
             """,
             """
             for i in range(10):
                pass
             """,
             """
             class Foo(object):
                pass
             """,
             "foo(1,2,3)",
             "{0: [1,2,3]}",
             ]

# Generated at 2022-06-13 15:30:33.304117
# Unit test for function safe_eval
def test_safe_eval():

    # Test if safe_eval is able to evaluate a simple expression
    result = safe_eval("{{ 1 + 1 }}")
    assert result == 2, 'safe_eval should be able to evaluate a simple expression'

    # Test if safe_eval is able to evaluate a dict
    result = safe_eval("{{ {'key': 'value', 'key2': 'value2'} }}")
    assert result == {'key': 'value', 'key2': 'value2'}, 'safe_eval should be able to evaluate a dict'

    # Test if safe_eval is able to evaluate a list
    result = safe_eval("{{ ['val1', 'val2', 123, 123.0, True] }}")
    assert result == ['val1', 'val2', 123, 123.0, True], 'safe_eval should be able to evaluate a dict'

    #

# Generated at 2022-06-13 15:30:42.417907
# Unit test for function safe_eval

# Generated at 2022-06-13 15:30:53.062038
# Unit test for function safe_eval
def test_safe_eval():

    # basic sanity
    assert safe_eval('[1,2,3,4]') == [1,2,3,4]
    assert safe_eval('{"a": "b", "c": "d"}') == {"a": "b", "c": "d"}
    assert safe_eval('{"a": "b", "c": "d"}.keys()') == ['a', 'c']

    # eval with an invalid expression
    assert safe_eval('{"a": "b", "c": "d"}.keys()[0]()') is None

    # call a builtin function
    assert safe_eval('len({"a": "b", "c": "d"})') == 2

    # call a disallowed builtin function
    assert safe_eval('__import__("os")') is None

    # try to access a builtin

# Generated at 2022-06-13 15:31:08.173949
# Unit test for function safe_eval
def test_safe_eval():
    """ tests to ensure the safe eval function works as expected """

    # empty expression
    assert safe_eval('') == ''

    # normal expression
    assert safe_eval('1 + 1') == 2

    # malformed expression
    try:
        safe_eval('1 +')
    except Exception:
        pass
    else:
        assert False, "failed to raise exception for unsafe expression"

    # malformed expression
    try:
        safe_eval('a + 1')
    except Exception:
        pass
    else:
        assert False, "failed to raise exception for unsafe expression"

    # dictionary expression
    assert safe_eval('{"a": 1}') == {"a": 1}

    # list expression
    assert safe_eval('[1, 2, 3]') == [1, 2, 3]

    # list expression as string
   

# Generated at 2022-06-13 15:31:15.686834
# Unit test for function safe_eval
def test_safe_eval():
    '''
    Test function safe_eval
    '''


# Generated at 2022-06-13 15:31:27.594076
# Unit test for function safe_eval
def test_safe_eval():
    # empty expression, should return empty string
    assert safe_eval('') == ''

    # simple expression, should return value of expression
    assert safe_eval('True')

    # valid expression, should return result of expression
    assert safe_eval('(1, 2, 3)') == (1, 2, 3)

    # expression with unsafe functions and attributes
    assert safe_eval('name.upper()') == 'name.upper()'
    assert safe_eval('[x for x in range(10)]') == '[x for x in range(10)]'

    # dict expressions
    assert safe_eval('{"a": 1, "b": 2}') == {'a': 1, 'b': 2}

    # tuple expressions
    assert safe_eval('(1, (2, 3))') == (1, (2, 3))

    # list

# Generated at 2022-06-13 15:31:35.970672
# Unit test for function safe_eval
def test_safe_eval():
    # some basic tests to make sure we do the right thing
    assert safe_eval("1 + 1") == 2
    assert safe_eval("1 + 1", None, include_exceptions=True)[0] == 2
    assert safe_eval("1 + 1", None, include_exceptions=True)[1] is None
    assert safe_eval("[1,2,3]") == [1, 2, 3]
    assert safe_eval("a", dict(a=1)) == 1
    assert safe_eval("a.b", dict(a={'b': 2})) == 2
    assert safe_eval("{'foo': 'bar'}") == {'foo': 'bar'}
    assert safe_eval("1 if True else 2") == 1
    assert safe_eval("1 if False else 2") == 2
    # test some negative examples

# Generated at 2022-06-13 15:31:44.317021
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('1') == 1
    assert safe_eval('1 + 1') == 2

    if sys.version_info[:2] == (2, 6):
        assert safe_eval('True') == True
        assert safe_eval('False') == False
    else:
        assert safe_eval('True') is True
        assert safe_eval('False') is False

    assert safe_eval('1 + True') == 2
    assert safe_eval('1 + False') == 1
    assert safe_eval('None') is None

    assert safe_eval('foo') == 'foo'
    assert safe_eval('foo.bar') == 'foo.bar'
    assert safe_eval('foo["bar"]') == 'foo["bar"]'
    assert safe_eval('foo[1]') == 'foo[1]'

    assert safe_eval

# Generated at 2022-06-13 15:31:55.145791
# Unit test for function safe_eval
def test_safe_eval():
    try:
        from ansible.utils import context_objects as co
    except ImportError:
        # prior to 2.8 context_objects was in __init__
        from ansible import context_objects as co

    # test for bad expressions

# Generated at 2022-06-13 15:32:05.775102
# Unit test for function safe_eval

# Generated at 2022-06-13 15:32:17.812179
# Unit test for function safe_eval
def test_safe_eval():
    # no calls allowed since CALL_ENABLED is empty
    assert safe_eval("foo") == "foo"
    assert safe_eval("foo.bar") == "foo.bar"
    assert safe_eval("'foo'.bar") == "'foo'.bar"
    assert safe_eval("foo.bar()") == "foo.bar()"
    assert safe_eval("range(4)") == "range(4)"
    assert safe_eval("'foo'") == "'foo'"
    assert safe_eval("foo['bar']['bam']") == "foo['bar']['bam']"
    assert safe_eval("foo['bar']") == "foo['bar']"
    assert safe_eval("foo[0]") == "foo[0]"

# Generated at 2022-06-13 15:32:29.833354
# Unit test for function safe_eval
def test_safe_eval():
    expr = u'''{"a": 1, "b": 2}'''
    assert safe_eval(expr) == {u'a': 1, u'b': 2}

    expr = u'''{% set a = 1 %}'''
    assert safe_eval(expr) == u'{% set a = 1 %}'

    expr = u'''{% set a = 1 + 2 %}'''
    assert safe_eval(expr) == u'{% set a = 1 + 2 %}'

    expr = u'''{% set a = 2 %}'''
    assert safe_eval(expr) == u'{% set a = 2 %}'

    expr = u'''[1, 2, 3, 4]'''
    assert safe_eval(expr) == [1, 2, 3, 4]

    expr

# Generated at 2022-06-13 15:32:39.995312
# Unit test for function safe_eval
def test_safe_eval():
    locals = {}
    # good expressions

# Generated at 2022-06-13 15:32:54.123177
# Unit test for function safe_eval
def test_safe_eval():
    '''
    Basic tests for safe_eval
    '''

    def ex(expr, exception=None):
        result, err = safe_eval(expr, include_exceptions=True)
        if exception is not None:
            assert err is not None
            assert isinstance(err, exception)
        else:
            assert err is None
        return result

    assert ex('4') == 4
    assert ex('4 + 4') == 8
    assert ex('a[1]', KeyError) == 'a[1]'
    assert ex('a.b', AttributeError) == 'a.b'
    assert ex('4 + a', NameError) == '4 + a'
    assert ex('4 - ', SyntaxError) == '4 - '
    assert ex('True and False') is False
    assert ex('True or False') is True

# Generated at 2022-06-13 15:33:04.210234
# Unit test for function safe_eval
def test_safe_eval():

    # Test with a valid datastructure
    good_list = "[1, 2, 3]"
    result = safe_eval(good_list)
    assert isinstance(result, list)

    # Test with a string that is not a valid datastructure
    bad_list = "[1, 2, 3"
    result = safe_eval(bad_list)
    assert not isinstance(result, list)
    assert isinstance(result, string_types)
    assert result == bad_list

    # Test an invalid function call
    bad_expr = "join(',', [1,2,3])"
    result = safe_eval(bad_expr)
    assert not isinstance(result, list)
    assert isinstance(result, string_types)
    assert result == bad_expr

    # Test a valid call to a builtin function
   

# Generated at 2022-06-13 15:33:15.497611
# Unit test for function safe_eval
def test_safe_eval():
    def myfunc():
        pass

    # invalid AST node types
    assert safe_eval('__import__("os").getcwd()') is None
    assert safe_eval('__import__("os").getcwd()', include_exceptions=True)[0] is None
    assert safe_eval('__import__("shutil").rmtree("/tmp")') is None
    assert safe_eval('__import__("shutil").rmtree("/tmp")', include_exceptions=True)[0] is None
    assert safe_eval('__import__("time").sleep(1)') is None
    assert safe_eval('__import__("time").sleep(1)', include_exceptions=True)[0] is None

    # valid AST node types
    assert safe_eval('True') is True

# Generated at 2022-06-13 15:33:26.585914
# Unit test for function safe_eval
def test_safe_eval():
    # Test the most simple usage
    assert safe_eval('1') == 1
    assert safe_eval('a') == 'a'

    # Test some of the available operators
    assert safe_eval('(1, 2)') == (1, 2)
    assert safe_eval('1 + 2') == 3
    assert safe_eval('4 - 2') == 2
    assert safe_eval('4 * 5') == 20
    assert safe_eval('10 / 2') == 5
    assert safe_eval('-5') == -5

    assert safe_eval('True') is True
    assert safe_eval('False') is False
    assert safe_eval('None') is None

    assert safe_eval('true') is True
    assert safe_eval('false') is False
    assert safe_eval('null') is None


# Generated at 2022-06-13 15:33:33.407890
# Unit test for function safe_eval
def test_safe_eval():

    # Test for dict items
    dict_items = ["'{foo:bar}'", "'{1:1, 2:3}'", "'{foo:bar, 1:1, 2:3}'"]
    expected = [{'foo': 'bar'}, {1: 1, 2: 3}, {'foo': 'bar', 1: 1, 2: 3}]
    for index, result in enumerate(dict_items):
        assert safe_eval(result) == expected[index]

    # Test for list items
    list_items = ["'[foo, bar]'", "'[foo, bar, 1, 2]'", "'[1,2,3]'"]
    expected = [['foo', 'bar'], ['foo', 'bar', 1, 2], [1, 2, 3]]

# Generated at 2022-06-13 15:33:44.345404
# Unit test for function safe_eval
def test_safe_eval():
    # Test the case where an exception is thrown
    test_syntax_error = False
    try:
        safe_eval('a = 1 +')
    except Exception as e:
        test_syntax_error = True
    assert(test_syntax_error)

    # Test the case where a constant is returned
    assert safe_eval('1') == 1

    # Test the case where variables are used
    assert safe_eval('a', dict(a=1)) == 1

    # Test the use of booleans
    assert safe_eval('false') == False
    assert safe_eval('true') == True

    # Test the use of null
    assert safe_eval('null') is None

    # Test the use of expressions
    assert safe_eval('1 + 5') == 6

    # Test the use of dicts
    assert safe_eval

# Generated at 2022-06-13 15:33:50.030204
# Unit test for function safe_eval
def test_safe_eval():
    d = {'a': 'abc', 'b': 'bcd', 'c': ['a', 'b'], 'd': [1, 2, 3]}
    f = 'a + b'
    if sys.version_info[0] < 3:
        f2 = u"u'ab'+u'cd'"
        f3 = u'u"ab" + u"cd"'
    else:
        f2 = "u'ab'+u'cd'"
        f3 = '''u"ab" + u"cd"'''

    assert safe_eval('{{ a }}') == 'abc'
    assert safe_eval('{{ a }} + {{ b }}') == 'abcbcd'
    assert safe_eval('{{ c + c }}') == ['a', 'b', 'a', 'b']

# Generated at 2022-06-13 15:33:58.606996
# Unit test for function safe_eval
def test_safe_eval():
    # invalid expression
    invalid_expr = 'a_dict["a_key"]'
    (result, exception) = safe_eval(invalid_expr, include_exceptions=True)
    assert result == invalid_expr
    assert exception is not None
    assert type(exception) == Exception

    # valid expression
    valid_expr = 'a_dict["a_key"]'
    (result, exception) = safe_eval('{"a_key": "value"}["a_key"]', include_exceptions=True)
    assert result == "value"
    assert exception is None
    assert type(result) == str

    # invalid json
    exception = safe_eval('{"a_key": }')
    assert type(exception) == SyntaxError



# Generated at 2022-06-13 15:34:06.944623
# Unit test for function safe_eval
def test_safe_eval():
    # No variables are allowed in the expression,
    # as no locals were passed to safe_eval
    assert safe_eval("1 + 1") == 2
    assert safe_eval("foo", {}, include_exceptions=True) == ('foo', None)
    assert safe_eval("1 + 1", {}, include_exceptions=True) == (2, None)
    assert safe_eval("1 + 1", {'foo':'bar'}, include_exceptions=True) == (2, None)
    assert safe_eval("1 + 1", {'foo':'bar'}) == 2
    assert safe_eval("1 + 1", {'foo':'bar'}, include_exceptions=True) == (2, None)
    assert safe_eval("1 + 1", include_exceptions=True) == (2, None)
    assert safe_

# Generated at 2022-06-13 15:34:15.218991
# Unit test for function safe_eval
def test_safe_eval():
    # tests for with_items as string
    assert safe_eval('[1]') == [1]
    assert safe_eval('[1, 2]') == [1, 2]
    assert safe_eval('[]') == []
    assert safe_eval('{"a": 1, "b": 2}') == {"a": 1, "b": 2}
    assert safe_eval('"string"') == "string"
    assert safe_eval('42') == 42
    assert safe_eval('42.42') == 42.42
    assert safe_eval('42.42 * 42') == 42.42 * 42
    assert safe_eval('42.42 * 42 - 42') == 42.42 * 42 - 42
    assert safe_eval('42 / 3') == 42 / 3
    assert safe_eval('42 // 3') == 42 // 3

# Generated at 2022-06-13 15:34:30.954333
# Unit test for function safe_eval
def test_safe_eval():

    if C.DEFAULT_DEBUG:
        sys.stderr.write("Testing function safe_eval\n")

    mylist = [1,2,3]
    mydict = {'a':1, 'b':2}

    # simple tests of valid calls
    assert safe_eval("2+3") == 5
    assert safe_eval("(1,2)+('a','b')") == (1,2,'a','b')
    assert safe_eval('{"a":1, "b":2}') == mydict
    assert safe_eval('["a", "b", "c"]') == ['a', 'b', 'c']
    assert safe_eval('mydict', dict(mydict=mydict)) == mydict
    assert safe_eval('2*3', dict(), ['__builtins__']) == 6

    # now

# Generated at 2022-06-13 15:34:40.860682
# Unit test for function safe_eval

# Generated at 2022-06-13 15:34:47.895820
# Unit test for function safe_eval
def test_safe_eval():

    def assertEvalRaisesException(expr, expected_exception):
        evaluated = safe_eval(expr, include_exceptions=True)
        assert evaluated[0] == expr
        assert isinstance(evaluated[1], expected_exception)

    def assertEvalReturns(expr, expected_value):
        assert safe_eval(expr) == expected_value

    assertEvalRaisesException('__builtins__.open("/etc/passwd")', Exception)
    assertEvalRaisesException('eval("__import__(\'os\').system(\'id\')")', Exception)
    assertEvalRaisesException('__import__(\'os\').system(\'id\')', Exception)
    assertEvalRaisesException('__import__(\'os\').system(\'id\')', Exception)
    assertEvalRaisesException

# Generated at 2022-06-13 15:34:56.301670
# Unit test for function safe_eval
def test_safe_eval():

    # Given
    C.CALL_ENABLED = ['methodcall']

    def methodcall():
        return "hello"

    expr = 'methodcall()'
    locals = {}
    locals['methodcall'] = methodcall

    # When
    result = safe_eval(expr, locals)

    # Then
    assert result == 'hello'

    # Given
    C.CALL_ENABLED = []

    # When
    result = safe_eval(expr, locals)

    # Then
    assert result == expr



# Generated at 2022-06-13 15:35:05.294253
# Unit test for function safe_eval
def test_safe_eval():
    # If we just told the user it's a syntax error and didn't even try
    # to run it, that's a big problem.  Let's verify that.
    assert safe_eval("[1,2,3]") == [1,2,3]
    assert safe_eval("{'foo': 'bar'}") == {'foo': 'bar'}
    assert safe_eval("True") is True
    assert safe_eval("'foobar'") == 'foobar'
    assert safe_eval("1+2") == 3
    assert safe_eval("(1,2)") == (1,2)
    assert safe_eval("[1,2]") == [1,2]
    assert safe_eval("[1, 2]", include_exceptions=True)[0] == [1, 2]

# Generated at 2022-06-13 15:35:13.273395
# Unit test for function safe_eval
def test_safe_eval():
    # string literals
    for expr in ['"foobar"', "'foobar'"]:
        assert safe_eval(expr) == "foobar"

    # list of literals
    for expr in ['["foo", "bar"]']:
        assert safe_eval(expr) == ["foo", "bar"]

    # dict of literals
    for expr in ['{"foo": "bar"}']:
        assert safe_eval(expr) == {"foo": "bar"}

    # we don't care about the type of the returned literal
    # so long as it's consistent
    assert safe_eval('1') == 1
    assert safe_eval('1.0') == 1.0

    # simple operations
    assert safe_eval('1+1') == 2
    assert safe_eval('1*1') == 1

    # nested dicts and lists
   

# Generated at 2022-06-13 15:35:21.863560
# Unit test for function safe_eval
def test_safe_eval():
    # a syntax error in the expression
    # should return the string back
    expr = "{{ foo +"
    result = safe_eval(expr)
    assert result == expr
    result, exception = safe_eval(expr, include_exceptions=True)
    assert result == expr
    assert isinstance(exception, SyntaxError)

    # an invalid expression that has unsafe AST elements
    # should also return the string back
    expr = "{{ foo().bar }}"
    result = safe_eval(expr)
    assert result == expr
    result, exception = safe_eval(expr, include_exceptions=True)
    assert result == expr
    assert type(exception) == Exception

    # a valid expression that is a template variable that
    # gets evaluated as a string (i.e. not yet templated)

# Generated at 2022-06-13 15:35:31.942474
# Unit test for function safe_eval
def test_safe_eval():
    class TestModule(object):
        def __getitem__(self, key):
            return key

        def get(self, key):
            return key

        def __call__(self, key):
            return key

        def __contains__(self, key):
            return True

    from ansible.constants import MK_BOOL, MK_NUMERIC

    # Test different types of objects that are passed
    assert safe_eval(1) == 1
    assert safe_eval(1.1) == 1.1
    assert safe_eval(True) is True
    assert safe_eval(False) is False
    assert safe_eval('1') == '1'
    assert safe_eval('true') == 'true'
    assert safe_eval([]) == []
    assert safe_eval({}) == {}

# Generated at 2022-06-13 15:35:39.509723
# Unit test for function safe_eval
def test_safe_eval():
    failures = 0

# Generated at 2022-06-13 15:35:39.963613
# Unit test for function safe_eval
def test_safe_eval():
    pass



# Generated at 2022-06-13 15:36:05.045892
# Unit test for function safe_eval
def test_safe_eval():

    class MyTest(object):
        def __init__(self, value):
            self.value = value
        def __str__(self):
            return str(self.value)

    # define a list of expressions that should succeed
    # and a list of expressions that should fail

# Generated at 2022-06-13 15:36:12.445405
# Unit test for function safe_eval
def test_safe_eval():
    def check_safe_eval(expr, value):
        ''' helper method for unit tests '''

        result, exception = safe_eval(expr, include_exceptions=True)
        if exception is not None:
            raise Exception("Expression '%s' failed: '%s'" % (expr, exception))
        if result != value:
            raise Exception("Expression '%s' failed: '%s' != '%s'" % (expr, result, value))

    def check_safe_eval_exc(expr, exc_str):
        ''' helper method for unit tests '''

        result, exception = safe_eval(expr, include_exceptions=True)
        if exception is None:
            raise Exception("Expression '%s' should have failed." % (expr))
        if str(exception) != exc_str:
            raise

# Generated at 2022-06-13 15:36:22.076215
# Unit test for function safe_eval
def test_safe_eval():

    # trailing newline is required for eval
    # to catch syntax errors
    # http://stackoverflow.com/questions/30492623/
    # how-can-i-check-whether-code-is-a-valid-python-expression

    # invalid syntax, but safe to print user expression back
    assert safe_eval("a**2 + b**2 \n") == "a**2 + b**2"
    assert safe_eval("a**2 + b**2") == "a**2 + b**2"
    assert safe_eval("a**2 + b**2 \n", include_exceptions=True)[0] == "a**2 + b**2"

    # invalid syntax, but safe to print user expression back
    assert safe_eval("a**2 + b**2") == "a**2 + b**2"


# Generated at 2022-06-13 15:36:29.849487
# Unit test for function safe_eval
def test_safe_eval():

    from ansible.module_utils._text import to_bytes, to_text


# Generated at 2022-06-13 15:36:35.749054
# Unit test for function safe_eval
def test_safe_eval():
    '''
    Some simple tests for safe_eval
    '''
    # safe_eval should return the value unchanged in the case of Jinja2 template
    # types that are not strings.  It should return the string value for
    # Jinja2 template types that are strings.
    assert safe_eval("foo", include_exceptions=True) == ("foo", None)
    assert safe_eval("foo", locals={"foo": 4}, include_exceptions=True) == (4, None)
    assert safe_eval("foo", locals={"foo": 4.0}, include_exceptions=True) == (4.0, None)
    assert safe_eval("foo", locals={"foo": [4]}, include_exceptions=True) == ([4], None)

# Generated at 2022-06-13 15:36:44.175970
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('a', dict(a=1)) == 1
    assert safe_eval('a', dict(a=1.1)) == 1.1
    assert safe_eval('a', dict(a='string')) == 'string'
    assert safe_eval('a', dict(a=False)) is False
    assert safe_eval('a', dict(a=True)) is True
    assert safe_eval('a', dict(a='True')) == 'True'
    assert safe_eval('a', dict(a='False')) == 'False'
    assert safe_eval('a', dict(a='None')) == 'None'
    assert safe_eval('a', dict(a=None)) is None
    assert safe_eval('[1,2,3]', dict()) == [1,2,3]
    assert safe_eval

# Generated at 2022-06-13 15:36:55.687832
# Unit test for function safe_eval
def test_safe_eval():
    """
    This function tests the safe_eval function from the lookups module.
    """
    # simple
    assert safe_eval('1') == 1
    assert safe_eval('"string"') == "string"
    assert safe_eval('1 + 1') == 2
    assert safe_eval('"string" * 2') == "stringstring"
    assert safe_eval('"string" * 2 + "string" * 2') == "stringstringstringstring"
    assert safe_eval('1.0') == 1.0
    assert safe_eval('[1]') == [1]
    assert safe_eval('[[1]]') == [[1]]
    assert safe_eval('{"key": 1}') == {"key": 1}
    assert safe_eval('{"key": [1]}') == {"key": [1]}
    assert safe_eval

# Generated at 2022-06-13 15:37:02.243510
# Unit test for function safe_eval
def test_safe_eval():
    # trivial tests
    assert(safe_eval("1") == 1)
    assert(safe_eval("1+2") == 3)
    assert(safe_eval("3*3") == 9)
    assert(safe_eval("['a','b','c']") == ['a', 'b', 'c'])
    assert(safe_eval("{'a':'b','c':'d'}") == {'a':'b','c':'d'})
    assert(safe_eval("True") == True)
    assert(safe_eval("False") == False)
    assert(safe_eval("None") == None)
    assert(safe_eval("a") == "a")
    # Verify we get back same string for non-str types
    assert(safe_eval(1) == "1")

# Generated at 2022-06-13 15:37:11.587455
# Unit test for function safe_eval
def test_safe_eval():
    tests = dict(
        simple_numbers=42,
        simple_strings="foo",
        simple_dict=dict(a="foo", b="bar"),
        nested_dict=dict(a="foo", b=dict(c="bar")),
        string_list=list("foo"),
        dict_list=["foo", dict(b="bar")],
        dict_list2=dict(a="foo", b=[1, 2, 3]),
        dict_list3=dict(a="foo", b=[dict(c="bar"), dict(d="baz")]),
        dict_with_json=dict(a="foo", b=dict(c="bar", d=True, e=False)),
        unicode_strings=u"\u99ac\u9a5a",
    )


# Generated at 2022-06-13 15:37:21.134905
# Unit test for function safe_eval

# Generated at 2022-06-13 15:38:01.289785
# Unit test for function safe_eval