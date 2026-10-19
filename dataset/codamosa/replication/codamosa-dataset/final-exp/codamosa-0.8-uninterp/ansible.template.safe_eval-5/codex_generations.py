

# Generated at 2022-06-13 15:28:09.033161
# Unit test for function safe_eval
def test_safe_eval():
    # Test all of the initial conditions, then loop over the tests
    # in the safe_eval_tests array.
    if sys.version_info[0] == 2:
        ast_node = 'ast.Add'
        ast_call_node = 'ast.Call'
    elif sys.version_info[0] == 3:
        ast_node = '<class \'_ast.Add\'>'
        ast_call_node = '<class \'_ast.Call\'>'
    else:
        raise Exception('Error tests are not defined for this version of Python')

    # Tests to evaluate.

# Generated at 2022-06-13 15:28:18.094621
# Unit test for function safe_eval
def test_safe_eval():

    # positive test cases
    assert safe_eval('1') == 1
    assert safe_eval('1 + 2') == 3
    assert safe_eval('[1, 2, 3]') == [1, 2, 3]
    assert safe_eval('{"a": 2, "b": 4}') == {"a": 2, "b": 4}
    assert safe_eval('null') is None
    assert safe_eval('false') is False
    assert safe_eval('true') is True

    # negative test cases
    try:
        safe_eval('1 + foo')
    except Exception:
        pass
    else:
        assert False, "should have raised exception"

    try:
        safe_eval('1 + __import__("os").system("echo hi")')
    except Exception:
        pass

# Generated at 2022-06-13 15:28:22.034573
# Unit test for function safe_eval
def test_safe_eval():
    # Make sure safe_eval allows expected safe expressions
    assert safe_eval("1") == 1
    assert safe_eval("len([1,2,3])") == 3
    # Make sure safe_eval does not allow unsafe expressions
    try:
        safe_eval("import os")
        assert False
    except:
        pass

# Return a JSON serializable version of param

# Generated at 2022-06-13 15:28:26.451243
# Unit test for function safe_eval
def test_safe_eval():
    import subprocess
    import six

    unittest = subprocess.check_output(['python', '-m', 'unittest', 'ansible.module_utils.common.text.eval_util.safe_eval'])

    if six.PY2:
        unittest = unittest.decode('utf8')

    print(unittest)


if __name__ == "__main__":
    import unittest

    class TestSafeEval(unittest.TestCase):
        def test_split(self):
            self.assertEqual(safe_eval("'a string'.split(' ')"), ['a', 'string'])
            self.assertEqual(safe_eval("a_list_variable.split('.')"), 'a_list_variable.split(\'.\')')
            self.assertE

# Generated at 2022-06-13 15:28:35.655587
# Unit test for function safe_eval
def test_safe_eval():
    # a variable is provided for Jinja2 templating
    hostvars = dict(foo='bar')

    def test_eval(expression, expected, hostvars=hostvars, fail=False):
        """
        Try to evaluate the expression and compare it with the expected result.
        """
        result, exception = safe_eval(expression, dict(hostvars=hostvars), include_exceptions=True)
        if fail:
            assert result == expression and exception is not None
        else:
            assert result == expected and exception is None

    def test_eval_fail(expression, hostvars=hostvars):
        test_eval(expression, expression, hostvars, fail=True)

    # basic structure tests
    test_eval('{}', {})
    test_eval('[]', [])

# Generated at 2022-06-13 15:28:44.827583
# Unit test for function safe_eval
def test_safe_eval():
    SAFE_NODES = set((ast.Add, ast.BinOp, ast.Compare, ast.Constant, ast.Dict,
                      ast.Div, ast.Expression, ast.List, ast.Load, ast.Mult,
                      ast.Num, ast.Name, ast.Set, ast.Str, ast.Sub, ast.USub, ast.Tuple, ast.UnaryOp,))

    expr = dict(wrong=1)

    print(safe_eval(expr, locals={'a': 1}, include_exceptions=True))
    print(safe_eval(expr, locals={'a': 1}))

    expr = 1234
    print(safe_eval(expr, locals={'a': 1}, include_exceptions=True))
    print(safe_eval(expr, locals={'a': 1}))

    expr

# Generated at 2022-06-13 15:28:52.949638
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval("1+1", include_exceptions=True)[0] == 2
    assert safe_eval("True", include_exceptions=True)[0] is True
    assert safe_eval("{'foo': 'bar'}", include_exceptions=True)[0] == {'foo': 'bar'}
    assert safe_eval("list('foo')", include_exceptions=True)[0] == ['f', 'o', 'o']
    assert safe_eval("{'foo': 'bar'}['foo']", include_exceptions=True)[0] == 'bar'
    assert safe_eval("{'foo': 'bar'}['bar']", include_exceptions=True)[0] is None
    assert safe_eval("1+'foo'", include_exceptions=True)[0] == "1foo"
    assert safe

# Generated at 2022-06-13 15:29:00.087116
# Unit test for function safe_eval
def test_safe_eval():
    global CALL_ENABLED

    # Do full import here, it's needed for the side effect of calling safe_eval
    from ansible.playbook.conditional import Conditional

    CALL_ENABLED = ['lookup']

# Generated at 2022-06-13 15:29:08.924910
# Unit test for function safe_eval
def test_safe_eval():
    """
    False, None, True are allowed
    """
    assert safe_eval("False") == False
    assert safe_eval("True") == True
    assert safe_eval("None") == None

    """
    Valid lists and dicts are allowed
    """
    assert safe_eval("['a', 'b', 'c']") == ['a', 'b', 'c']
    assert safe_eval("{'a': 1, 'b': {'c': 2}}") == {'a': 1, 'b': {'c': 2}}

    """
    Valid literals are allowed
    """
    assert safe_eval("'a'") == 'a'
    assert safe_eval("1") == 1
    assert safe_eval("[1]") == [1]

# Generated at 2022-06-13 15:29:18.449738
# Unit test for function safe_eval
def test_safe_eval():
    """
    >>> test_safe_eval()
    Datastructures: OK
    ...
    SyntaxErrors: OK
    """
    expr = 'a_list_variable'
    locals = {}
    result, err = safe_eval(expr, locals, include_exceptions=True)
    assert result == expr
    assert isinstance(err, SyntaxError)
    print('SyntaxErrors: OK')


# Generated at 2022-06-13 15:29:31.978419
# Unit test for function safe_eval
def test_safe_eval():
    # What we really want to test is that CleansingNodeVisitor is actually
    # being called, but since the C implementation of ast calls visit_*
    # methods directly instead of using the generic_visit method, the only
    # way to test it is to try evaluating a non-constant.
    #
    # Note that in Python 3, a raw string is always a legal ast.Constant
    # value, so we have to use a non-raw string to test with.

    # Let's try defining a function and calling it
    try:
        safe_eval("def f(): pass; f()")
        raise AssertionError("f() should not be allowed!")
    except Exception as e:
        print("Got the expected exception for f():", e)

    # OK, now let's try calling an allowed function.
    # safe_eval happens

# Generated at 2022-06-13 15:29:39.946250
# Unit test for function safe_eval
def test_safe_eval():
    text = '''
    {% set facts = {
        'key1': 'value1',
        'key2': 'value2',
        '__key': 'value',
    } %}

    {{
    facts['key2']
    }}

    {{
    facts.key1
    }}

    {{
    facts.__key
    }}
    '''
    result = safe_eval(text)
    assert result == {'key2': 'value2'}, result

    assert safe_eval("foo.bar") == "foo.bar"
    assert safe_eval("foo['bar']") == "foo['bar']"
    assert safe_eval("foo[bar]") == "foo[bar]", safe_eval("foo[bar]")


# Generated at 2022-06-13 15:29:50.963687
# Unit test for function safe_eval
def test_safe_eval():
    ansible_base_dir = C.ANSIBLE_LIB_ROOT
    ansible_module_utils_dir = ansible_base_dir + '/module_utils/'
    sys.path.insert(0, ansible_module_utils_dir)
    import module_utils.basic
    assert safe_eval('True')
    assert safe_eval('False')
    assert safe_eval('null')
    assert safe_eval('null is None')
    assert safe_eval('false is False')
    assert safe_eval('true is True')
    assert safe_eval('1 is 1')
    assert safe_eval('1 is not 0')
    assert safe_eval('[1, 2, 3]')
    assert safe_eval('["a", "b", "c"]')

# Generated at 2022-06-13 15:29:59.244772
# Unit test for function safe_eval
def test_safe_eval():
    # Test that safe_eval works with just builtins
    result = safe_eval('2 + 2')
    assert result == 4
    result = safe_eval('7 * 9')
    assert result == 63
    # Test that safe_eval works with function calls
    CALL_ENABLED.append('max')
    result = safe_eval('max(4, 8)')
    assert result == 8
    CALL_ENABLED.append('min')
    result = safe_eval('min(4, 8)')
    assert result == 4
    CALL_ENABLED.append('round')
    result = safe_eval('round(3.5)')
    assert result == 4
    CALL_ENABLED.append('abs')
    result = safe_eval('abs(-4)')
    assert result == 4

    # Test that safe_eval raises

# Generated at 2022-06-13 15:30:07.896958
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval("1+1") == 2
    assert safe_eval("foo", locals=dict(foo="bar")) == "bar"
    assert safe_eval("foo + 'bar'", locals=dict(foo="foo")) == "foobar"
    assert safe_eval("foo + 'bar'", locals=dict(foo="foo"), include_exceptions=True) == ("foobar", None)
    assert safe_eval("'foo' + bar", locals=dict(bar="bar")) == "foobar"
    assert safe_eval("item.key", locals=dict(item=dict(key="val"))) == "val"
    assert safe_eval("item[0]", locals=dict(item=["val"])) == "val"

    # Check if we can use certain keywords as variables

# Generated at 2022-06-13 15:30:18.363909
# Unit test for function safe_eval
def test_safe_eval():
    # These should pass
    returnval = None
    try:
        returnval = safe_eval("5")
    except:
        pass
    assert returnval == 5, "test_safe_eval failed while processing '5'"

    returnval = None
    try:
        returnval = safe_eval("5 + 7")
    except:
        pass
    assert returnval == 12, "test_safe_eval failed while processing '5 + 7'"

    returnval = None
    try:
        returnval = safe_eval("5 * 7")
    except:
        pass
    assert returnval == 35, "test_safe_eval failed while processing '5 * 7'"

    returnval = None
    try:
        returnval = safe_eval("5 - 7")
    except:
        pass

# Generated at 2022-06-13 15:30:26.555766
# Unit test for function safe_eval
def test_safe_eval():
    # Test valid expressions
    assert safe_eval('1 + 1') == 2
    assert safe_eval('1 + 1', include_exceptions=True) == (2, None)
    assert safe_eval('(1 + 1) in (False, None, 0, "", [], (), {})') == False
    assert safe_eval('(1 + 1) in (True, 1)') == True
    assert safe_eval('(1 + 1) in (True, 1)', include_exceptions=True) == (True, None)
    assert safe_eval('(1 + 1) in (True, 1, None)') == True
    assert safe_eval('(1 + 1) in (True, 1, None)', include_exceptions=True) == (True, None)

# Generated at 2022-06-13 15:30:32.299513
# Unit test for function safe_eval
def test_safe_eval():
    # define certain JSON types
    # eg. JSON booleans are unknown to python eval()
    OUR_GLOBALS = {
        '__builtins__': {},  # avoid global builtins as per eval docs
        'false': False,
        'null': None,
        'true': True,
        # also add back some builtins we do need
        'True': True,
        'False': False,
        'None': None
    }

    # this is the whitelist of AST nodes we are going to
    # allow in the evaluation. Any node type other than
    # those listed here will raise an exception in our custom
    # visitor class defined below.

# Generated at 2022-06-13 15:30:41.497616
# Unit test for function safe_eval
def test_safe_eval():

    class FakeVarsModule(object):
        def __init__(self, vars):
            self.ansible_vars = vars

    # safe_eval should return an empty string for any strings
    assert safe_eval('test') == 'test'

    # safe_eval should return a list literal string unchanged
    assert safe_eval('[foo, bar]') == '[foo, bar]'
    # but it should return a list of the parsed contents for a list literal
    assert safe_eval('["foo", "bar"]') == ['foo', 'bar']

    # safe_eval should return a dictionary literal unchanged
    assert safe_eval('{foo: bar}') == '{foo: bar}'
    # but it should return a dictionary of the parsed contents for a dict literal

# Generated at 2022-06-13 15:30:52.629097
# Unit test for function safe_eval
def test_safe_eval():
    # Testing for expression type
    expr = [1, 2, 'A string']
    result, error = safe_eval(expr, include_exceptions=True)
    assert result == expr
    assert error is None

    expr = 'not_a_list'
    result, error = safe_eval(expr, include_exceptions=True)
    assert result == expr
    assert error is None

    # Testing a list
    expr = "[1, 2, 3]"
    result, error = safe_eval(expr, include_exceptions=True)
    assert result == [1, 2, 3]
    assert error is None

    # Testing a list comprehension
    expr = "[i for i in range(10, 12)]"
    result, error = safe_eval(expr, include_exceptions=True)
    assert result == [10, 11]


# Generated at 2022-06-13 15:30:59.739453
# Unit test for function safe_eval
def test_safe_eval():
    # Test that safe_eval correctly holds back unsafe constructs
    # This should raise an exception
    try:
        assert safe_eval("__import__('os').system('echo hello world')")
    except:
        pass
    else:
        assert False

    # This should not raise an exception
    safe_eval("1 + 2")

    # This should evaluate to the expected value
    assert safe_eval("1 + 2") == 3

    # A few test cases inspired by the simplejson test suite:
    assert safe_eval("0") == 0
    assert safe_eval("-123") == -123
    assert safe_eval("2 ** 31 - 1") == 2147483647
    assert safe_eval("2 ** 31") == 2147483648
    assert safe_eval("-2 ** 31") == -2147483648
    assert safe

# Generated at 2022-06-13 15:31:09.987236
# Unit test for function safe_eval
def test_safe_eval():
    module = AnsibleModule(argument_spec=dict(
        expr=dict(required=True, type='str'),
        locals=dict(type='dict', default={}),
        include_exceptions=dict(default=False, type='bool')
    ))
    expr = module.params['expr']
    locals = module.params['locals']
    include_exceptions = module.params['include_exceptions']
    result = safe_eval(expr, locals, include_exceptions)
    if include_exceptions:
        if result[1] is None:
            module.exit_json(result=result[0])
        else:
            module.fail_json(msg=to_native(result[1]))
    else:
        module.exit_json(result=result)


# Generated at 2022-06-13 15:31:16.999696
# Unit test for function safe_eval
def test_safe_eval():
    """
    Unit test for function safe_eval.
    :return:
    """
    python_version = (sys.version_info)[0]
    if python_version == 2:
        from nose.tools import assert_equal
    elif python_version == 3:
        from unittest.case import TestCase
        from unittest.util import safe_repr

        class AssertEqualsTestCase(TestCase):
            def assertEqual(self, first, second, msg=None):
                assert first == second, msg or "{} != {}".format(safe_repr(first), safe_repr(second))
    else:
        print("Unsupported python version: {}".format(python_version))
        return

    # build the test cases

# Generated at 2022-06-13 15:31:28.764391
# Unit test for function safe_eval
def test_safe_eval():
    '''
    This is not compatible with older python versions,
    this is just a simple and manual test.
    '''


# Generated at 2022-06-13 15:31:36.660629
# Unit test for function safe_eval
def test_safe_eval():
    v = dict(a=1, b=2, l=['a', 'b', 'c'], d=dict(a=1, b=2), s='foo')
    assert safe_eval('a', v) == 1
    assert safe_eval('l[1]', v) == 'b'
    assert safe_eval('d[l[1]]', v) == 2
    assert safe_eval('a * b', v) == 2
    assert safe_eval('a ** b', v) == 1
    assert safe_eval('(s + "bar")[2:]', v) == 'obar'
    assert safe_eval('s[1:] + "bar"', v) == 'oobar'
    assert safe_eval('s[1:]*2', v) == 'oofoo'

# Generated at 2022-06-13 15:31:44.629285
# Unit test for function safe_eval
def test_safe_eval():
    # check callability, needed for later
    assert callable(safe_eval)

    # check return value, needed for later
    assert safe_eval('True') == True
    assert safe_eval('False') == False
    assert safe_eval('None') == None
    assert safe_eval('true') == True
    assert safe_eval('false') == False
    assert safe_eval('null') == None
    assert safe_eval('[]') == []
    assert safe_eval('[1]') == [1]
    assert safe_eval('[1, 2]') == [1, 2]
    assert safe_eval('[1, [2]]') == [1, [2]]
    assert safe_eval('[1, [2, [3]]]') == [1, [2, [3]]]

# Generated at 2022-06-13 15:31:52.089781
# Unit test for function safe_eval
def test_safe_eval():
    # Check safe_eval() error handling
    # Legal expression
    assert safe_eval('1') == 1
    # Illegal expression
    assert safe_eval('__import__') == '__import__'
    # Check safe_eval() error handling when used with include_exceptions=True
    # Legal expression
    assert safe_eval('1', include_exceptions=True) == (1, None)
    # Illegal expression

# Generated at 2022-06-13 15:31:59.378368
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('var') == 'var'
    assert safe_eval('"test"') == 'test'
    assert safe_eval('1') == 1
    assert safe_eval('2') == 2
    assert safe_eval('2+2') == 4
    assert safe_eval('1 - 2') == -1
    assert safe_eval('2 * 3') == 6
    assert safe_eval('2 * 3 + 4') == 10
    assert safe_eval('2 * (3 + 4)') == 14
    assert safe_eval('2 * 3 + 4 * 5') == 26
    assert safe_eval('2 * (3 + 4) * 5') == 70
    assert safe_eval('[1, 2, 3]') == [1, 2, 3]

# Generated at 2022-06-13 15:32:07.177800
# Unit test for function safe_eval
def test_safe_eval():
    expr = "a_list_variable"
    assert expr == safe_eval(expr)
    assert '__builtins__' == safe_eval('__builtins__')
    assert None == safe_eval('None')
    assert 1 == safe_eval('1+0')
    assert 0 == safe_eval('1-1')
    assert 2 == safe_eval('6/3')
    assert 3 == safe_eval('1+2')
    assert 3 == safe_eval('(3)')
    assert 6 == safe_eval('1+2+3')
    assert 2 == safe_eval('6//3')
    assert 3 == safe_eval('1+2')


# Generated at 2022-06-13 15:32:18.432779
# Unit test for function safe_eval
def test_safe_eval():
    """
    This test uses information from ast.dump(ast.parse('1'))
    to validate the safe_eval filter.
    """

    # checks that a valid string returns the evaluated result
    assert safe_eval('[1,2,3]') == [1, 2, 3]

    # checks that modified builtins are not allowed
    assert safe_eval('__import__("os")') == '__import__("os")'

    # checks that modules are not allowed
    assert safe_eval('os.getcwd()') == 'os.getcwd()'

    # checks that 'null' is not allowed
    assert safe_eval('null') is 'null'

    # checks that literals are allowed
    assert safe_eval('1') == 1
    assert safe_eval('"foo"') == 'foo'
    assert safe_eval

# Generated at 2022-06-13 15:32:33.410874
# Unit test for function safe_eval
def test_safe_eval():
    env = {'foo': 'bar', 'spam': 'eggs'}
    constant_tests = [
        ('123', 123),
        ('True', True),
        ('False', False),
        ('None', None),
        ('"hello world"', 'hello world')
    ]

    variable_tests = [
        ('foo', 'bar'),
        ('spam', 'eggs')
    ]

    other_tests = [
        ('[1,2,3,4]', [1, 2, 3, 4]),
        ('["foo","bar","baz"]', ['foo', 'bar', 'baz']),
        ('[]', []),
        ('{}', {}),
        ('["foo"]', ['foo']),
        ('"foo"', 'foo'),
    ]


# Generated at 2022-06-13 15:32:42.861259
# Unit test for function safe_eval
def test_safe_eval():

    def handle_eval_output(x, y):
        (result, error) = x
        if error:
            print('Looks like there was an exception: %s' % y)
        else:
            if isinstance(result, str):
                print('Evaluated value is a string [%s]' % result)
            else:
                print('Evaluated value is not a string [%s]' % result)
        sys.exit(error is None)

    # Lets check a string
    handle_eval_output(safe_eval('"hello"', include_exceptions=True),
                       '"hello"')
    handle_eval_output(safe_eval('True', include_exceptions=True),
                       'True')
    handle_eval_output(safe_eval('False', include_exceptions=True),
                       'False')
   

# Generated at 2022-06-13 15:32:53.194181
# Unit test for function safe_eval
def test_safe_eval():
    # Test safe_eval without exceptions
    assert safe_eval("2 + 3") == 2 + 3
    assert safe_eval("tiny_dict_variable.items()") == {'a': 1, 'b': 2}.items()
    # Test safe_eval with exceptions
    assert safe_eval("2 + 3", include_exceptions=True) == (2 + 3, None)
    assert safe_eval("tiny_dict_variable.foo()", include_exceptions=True) == ('tiny_dict_variable.foo()', None)
    # Test safe_eval with invalid expressions and exceptions
    # This is necessary to use with_items with a variable
    assert safe_eval("invalid_expression_for_jinja", include_exceptions=True) == ('invalid_expression_for_jinja', None)

# Generated at 2022-06-13 15:33:03.437698
# Unit test for function safe_eval
def test_safe_eval():
    try:
        import unittest2 as unittest
    except ImportError:
        import unittest

    class TestSafeEval(unittest.TestCase):
        def test_native(self):
            self.assertEqual(1, safe_eval("1"))

        def test_native_basic_ops(self):
            self.assertEqual(3, safe_eval("1 + 2"))

        def test_native_basic_ops2(self):
            self.assertEqual(4, safe_eval("2 * 2"))

        def test_native_basic_ops3(self):
            self.assertEqual(6, safe_eval("1 + 2 * 3"))

        def test_native_basic_ops4(self):
            self.assertEqual(10, safe_eval("(1 + 2) * 3"))

# Generated at 2022-06-13 15:33:14.887351
# Unit test for function safe_eval

# Generated at 2022-06-13 15:33:25.961224
# Unit test for function safe_eval
def test_safe_eval():
    # Test call with a simple expression, ensure the eval is correct
    expr = '2 + 2'
    assert safe_eval(expr) == 4, "test_safe_eval 1 failed"

    # Test call with an expression that raises a SyntaxError.
    # Ensure the expression is returned.
    expr = '{{2 + 2}}'
    assert safe_eval(expr) == expr, "test_safe_eval 2 failed"

    # Test call with an expression that is not valid. Ensure the
    # expression is returned.
    expr = '2 + 2 = 5'
    assert safe_eval(expr) == expr, "test_safe_eval 3 failed"

    # Test call with a complex dictionary that is valid.
    # Ensure the dictionary returned is equal to the original.

# Generated at 2022-06-13 15:33:32.265949
# Unit test for function safe_eval

# Generated at 2022-06-13 15:33:43.126155
# Unit test for function safe_eval

# Generated at 2022-06-13 15:33:54.287589
# Unit test for function safe_eval
def test_safe_eval():
    from ansible.module_utils import basic

    _json_data = basic.json_dict_unicode_to_bytes({
        'a_list': [1, 2, 3],
        'a_dict': {'b': 'c', 'd': 'e'},
    })
    assert safe_eval("[1, 2, 3]", _json_data) == ([1, 2, 3], None)
    assert safe_eval("{'b': 'c', 'd': 'e'}", _json_data) == ({'b': 'c', 'd': 'e'}, None)
    assert safe_eval("'b' in {'b': 'c', 'd': 'e'}", _json_data) == (True, None)

# Generated at 2022-06-13 15:34:04.883410
# Unit test for function safe_eval
def test_safe_eval():
    # empty string
    assert safe_eval("") == ""
    # string
    assert safe_eval("'hello world'") == "hello world"
    # unicode string
    assert safe_eval("u'\u00e5\u00e4\u00f6'") == "\xe5\xe4\xf6"
    # integer
    assert safe_eval("42") == 42
    # negative integer
    assert safe_eval("-42") == -42
    assert safe_eval("-42 - 1") == -43
    # list
    assert safe_eval("[1, 1, 2, 3, 5, 8]") == [1, 1, 2, 3, 5, 8]
    assert safe_eval("[1, 1, 2, 3, 5, 8][3]") == 3
    # dictionary
    assert safe_

# Generated at 2022-06-13 15:34:18.883157
# Unit test for function safe_eval
def test_safe_eval():
    # test some simple cases
    assert safe_eval("nested['foo'][1]") == "nested['foo'][1]"
    assert safe_eval("foo=='bar'") == "foo=='bar'"

    # Test that some basic data structures are accepted
    assert safe_eval("[1,2]") == [1,2]
    assert safe_eval("{'foo': 'bar'}") == {'foo': 'bar'}

    # Test that we are doing some validation
    assert safe_eval("nested['foo'][1]") == "nested['foo'][1]"
    assert safe_eval("__import__('os').path") == "__import__('os').path"
    assert safe_eval("bytes") == "bytes"

    # Test that we can evaluate simple expressions

# Generated at 2022-06-13 15:34:28.063179
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval("'test_string'") == 'test_string'
    assert safe_eval("test_string") == 'test_string'
    assert safe_eval("True") is True
    assert safe_eval("False") is False
    assert safe_eval("None") is None
    assert safe_eval("true") is True
    assert safe_eval("false") is False
    assert safe_eval("null") is None
    assert safe_eval("'test' + '_' + 'string'") == 'test_string'
    assert safe_eval("1 + 2 * 3") == 7
    assert safe_eval("[1, 2, 3, 4]") == [1, 2, 3, 4]
    assert safe_eval("(1, 2, 3, 4)") == (1, 2, 3, 4)
    assert safe

# Generated at 2022-06-13 15:34:36.759297
# Unit test for function safe_eval

# Generated at 2022-06-13 15:34:44.930510
# Unit test for function safe_eval

# Generated at 2022-06-13 15:34:52.565741
# Unit test for function safe_eval
def test_safe_eval():
    import ast
    from ansible.module_utils._text import to_text, to_bytes

    if sys.version_info < (2, 7, 0):
        raise SkipTest("Skipped: Python 2.6 fails to convert unicode to bytes")

    # Test ast.literal_eval, custom safe_eval, and function safe_eval
    test_str = u'''
        key1: "value1"
        key2: 2
        key3: True
        key4: false
        key5: null
        key6: "{{a_list_variable}}"
        key7: "{{ somestring }}"
        key8: "{{ lookup('env', 'HOME') }}"
        key9: "{{ item }}"
        key10: '{{ item }}'
    '''

    # Python 3 returns a str and Python 2

# Generated at 2022-06-13 15:35:02.510250
# Unit test for function safe_eval

# Generated at 2022-06-13 15:35:10.172919
# Unit test for function safe_eval
def test_safe_eval():

    # Should pass
    assert safe_eval("[1,2,3] + [4,5]") == [1, 2, 3, 4, 5]
    assert safe_eval("{'a': 1, 'b': 2}", {'a': 10}) == {'a': 1, 'b': 2}
    assert safe_eval("-5+4", {}, include_exceptions=True)[0] == -1
    assert safe_eval("-5+4", {}, include_exceptions=True)[1] is None
    assert safe_eval("[x for x in range(1, 10)]", {}, include_exceptions=True)[1] is not None
    assert safe_eval("{x:x for x in range(1, 10)}", {}, include_exceptions=True)[1] is not None
    assert safe_eval

# Generated at 2022-06-13 15:35:19.650763
# Unit test for function safe_eval
def test_safe_eval():
    class TestError(Exception):
        pass

    # use cases for safe expressions

# Generated at 2022-06-13 15:35:29.320481
# Unit test for function safe_eval
def test_safe_eval():
    """
    >>> test_safe_eval()
    True
    """

# Generated at 2022-06-13 15:35:38.179302
# Unit test for function safe_eval
def test_safe_eval():
    # Define our own builtins that are not safe so they can be tested
    class CheckedStr:
        def __init__(self, arg):
            if isinstance(arg, str):
                self.value = arg
            else:
                raise Exception("Expecting str, got {}".format(type(arg)))

        def __eq__(self, other):
            return self.value == other.value

    class DodgyDict(dict):
        def __init__(self, *args, **kwargs):
            super(DodgyDict, self).__init__(*args, **kwargs)
            raise Exception("DodgyDict")

        def items(self):
            return super(DodgyDict, self).items()


# Generated at 2022-06-13 15:35:52.813697
# Unit test for function safe_eval
def test_safe_eval():
    tests = [
        ("'10' + 10", 20),
        ("('10' + '10') * 2", 40),
        ("10 + '10'", '10+10'),
        ("10 + [10, 1]", '10+[10, 1]'),
        ("10 + {'a': 10, 'b': 20}", '10+{\'a\': 10, \'b\': 20}'),
        ("set(0)", set([0])),
        ("set(0, 1)", 'set(0, 1)'),
        ("set()", set()),
        ("set()", set()),
        ('{{ 1 | bool + 10 }}', '{{ 1 | bool + 10 }}'),
        ("{'a':10, 'b':20}", {'a': 10, 'b': 20}),
    ]


# Generated at 2022-06-13 15:36:03.696422
# Unit test for function safe_eval
def test_safe_eval():
    '''
    Validate that safe_eval works as expected.
    '''

    # check ok expression
    expr = 'foo'
    assert safe_eval(expr) == expr

    # check invalid expression
    expr = 'import sys'
    assert safe_eval(expr) == expr

    # check syntax error as expression
    expr = '-'
    assert safe_eval(expr) == expr

    # check safe expression
    expr = '1 + 1'
    assert safe_eval(expr) == 2

    # check dict expression
    expr = '{"foo": "bar"}'
    assert safe_eval(expr) == {"foo": "bar"}

    # check list expression
    expr = '["foo", "bar"]'
    assert safe_eval(expr) == ['foo', 'bar']

    # check tuple expression

# Generated at 2022-06-13 15:36:11.791236
# Unit test for function safe_eval
def test_safe_eval():

    assert safe_eval("['a', 'b']") == ['a', 'b']
    assert safe_eval("{'a': 'b'}") == {'a': 'b'}
    assert safe_eval("'foo'") == 'foo'
    assert safe_eval("1+1") == 2
    assert safe_eval("(1, 2, 3)") == (1, 2, 3)

    # test some bad inputs to make sure we don't catch them
    try:
        safe_eval("__import__('os').system('ls')")
        assert False
    except Exception:
        pass

    try:
        safe_eval("myvar")
        assert False
    except Exception:
        pass


# Generated at 2022-06-13 15:36:19.263165
# Unit test for function safe_eval

# Generated at 2022-06-13 15:36:27.352521
# Unit test for function safe_eval

# Generated at 2022-06-13 15:36:33.999982
# Unit test for function safe_eval

# Generated at 2022-06-13 15:36:39.263941
# Unit test for function safe_eval
def test_safe_eval():
    safe_eval_cases = (
        ("['child_var']", ['child_var'])
    )
    for (template, expected) in safe_eval_cases:
        result = safe_eval(template)
        assert result == expected, "'%s' did not evaluate to expected output of '%s', got '%s' instead." % (template, expected, result)


# Generated at 2022-06-13 15:36:46.188195
# Unit test for function safe_eval
def test_safe_eval():
    # Fail with non-string expression
    assert safe_eval(123) == 123
    # Test with non-executable string
    assert safe_eval('some_string_value') == 'some_string_value'
    # Test invalid expression
    try:
        safe_eval('[][1]')
        assert False
    except Exception:
        pass
    # Test valid expression
    assert safe_eval('{"a":1,"b":2}') == {"a": 1, "b": 2}
    # Test syntax errors
    if sys.version_info >= (3, 5):
        try:
            safe_eval('[][1]')
            assert False
        except SytnaxError:
            pass
    else:
        assert safe_eval('[][1]') == '[][1]'


# Generated at 2022-06-13 15:36:58.553577
# Unit test for function safe_eval
def test_safe_eval():
    # simple expression
    assert safe_eval('2 + 2') == 4

    # a dict inside a dict
    assert safe_eval('{"k1": {"k2": "v2"}}') == {"k1": {"k2": "v2"}}

    # a list inside a dict
    assert safe_eval('{"k1": ["v1", "v2"]}') == {"k1": ["v1", "v2"]}

    # a list of dicts
    assert safe_eval('[{"k1": "v1"}, {"k2": "v2"}]') == [{"k1": "v1"}, {"k2": "v2"}]

    # dicts inside lists inside dicts

# Generated at 2022-06-13 15:37:05.112218
# Unit test for function safe_eval

# Generated at 2022-06-13 15:37:22.016697
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('5') == 5
    assert safe_eval('a') == 'a'
    assert safe_eval('5 + 5') == 10
    assert safe_eval('"hello " + "world"') == 'hello world'
    assert safe_eval('a.b[1] + c.d[3]', locals={'a': {'b': [1,2,3]}, 'c': {'d': [1,2,3,4]}}) == 6
    assert safe_eval('a.b[1] + c.d[3]', locals={'a': {'b': [1,2,3]}, 'c': {'d': ['a',2,3,4]}}) == '2a'

# Generated at 2022-06-13 15:37:28.089186
# Unit test for function safe_eval

# Generated at 2022-06-13 15:37:36.039866
# Unit test for function safe_eval
def test_safe_eval():
    from ansible.module_utils.common.text.converters import to_bytes

# Generated at 2022-06-13 15:37:44.968729
# Unit test for function safe_eval
def test_safe_eval():
    from ansible.module_utils._text import to_text

    class FakeDisplay:
        def display(self, msg, color=None, stderr=False, screen_only=False, log_only=False):
            print(msg)

    display = FakeDisplay()

    # Base class for the exceptions in this module.
    class AnsibleModuleError(Exception):
        pass

    class AnsibleUndefinedVariable(AnsibleModuleError):
        pass

    raise_exception = True
    verbosity = 3

    def fail_json(*args, **kwargs):
        msg = args[0]
        obj = args[1]
        sys.stderr.write(msg)
        sys.stderr.write(to_text(obj))
        raise AnsibleUndefinedVariable()


# Generated at 2022-06-13 15:37:54.774118
# Unit test for function safe_eval

# Generated at 2022-06-13 15:38:03.092072
# Unit test for function safe_eval
def test_safe_eval():
    # the following are tests based on the examples in the docstring!
    assert safe_eval('foo') == 'foo'
    assert safe_eval('[]') == []
    assert safe_eval('[1, 2]') == [1, 2]
    assert safe_eval('[1, 2] + [3, 4]') == [1, 2, 3, 4]
    assert safe_eval('{"a": "b"}') == {'a': 'b'}
    assert safe_eval('False') is False
    try:
        safe_eval('__import__("os").system("touch /tmp/pwned")')
        sys.exit(1)
    except:
        pass
    try:
        safe_eval('[x for x in range(10)]')
        sys.exit(1)
    except:
        pass
