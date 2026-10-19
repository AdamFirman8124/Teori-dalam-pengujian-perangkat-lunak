

# Generated at 2022-06-13 15:28:13.939604
# Unit test for function safe_eval
def test_safe_eval():
    """
    Ansible module for testing function safe_eval
    """

    # load_resources

    # define specific test cases
    test_cases = dict()

    # this is an invalid expression and should raise an exception
    test_cases['invalid_expr'] = dict(
        expr='1 == 1 = 1',
        success=False,
        exception=True,
        exception_str='invalid expression (1 == 1 = 1)',
    )

    # this is an expression which may be evaluated to an empty string
    test_cases['empty_string'] = dict(
        expr='""',
        success=True,
        exception=False,
        result=u'',
        exception_str=None,
    )

    # this is a simple expression

# Generated at 2022-06-13 15:28:22.407223
# Unit test for function safe_eval
def test_safe_eval():
    # simple test to make sure the code works in both python 2 and 3
    assert safe_eval('True') is True
    assert safe_eval('False') is False
    assert safe_eval('None') is None
    assert safe_eval('true') is True
    assert safe_eval('false') is False
    assert safe_eval('null') is None

    assert safe_eval('-1') == -1
    assert safe_eval('1') == 1
    assert safe_eval('1 + 1') == 2
    assert safe_eval('1 + 2 - 1') == 2
    assert safe_eval('- 1') == -1
    assert safe_eval('1 - 2') == -1
    assert safe_eval('2 * 2') == 4
    assert safe_eval('4 // 2') == 2

# Generated at 2022-06-13 15:28:26.815245
# Unit test for function safe_eval
def test_safe_eval():
    # A number
    result, e = safe_eval("42", include_exceptions=True)
    assert result == 42
    assert e == None

    # A string
    result, e = safe_eval("'42'", include_exceptions=True)
    assert result == '42'
    assert e == None

    # A string with a double quote, note we escape it in our string
    result, e = safe_eval("'42\"'", include_exceptions=True)
    assert result == '42"'
    assert e == None

    # A single-element list
    result, e = safe_eval("[42]", include_exceptions=True)
    assert result == [42]
    assert e == None

    # A 1-tuple

# Generated at 2022-06-13 15:28:35.915627
# Unit test for function safe_eval
def test_safe_eval():
    # check known safe values
    assert safe_eval('a', dict(a='a')) == 'a'
    assert safe_eval('a', dict(a=1)) == 1
    assert safe_eval('a', dict(a=1.1)) == 1.1
    assert safe_eval('a', dict(a=True)) is True
    assert safe_eval('a', dict(a=False)) is False
    assert safe_eval('a', dict(a=None)) is None
    # True, False, None can be passed as strings or native types
    assert safe_eval('a', dict(a='True')) is True
    assert safe_eval('a', dict(a='False')) is False
    assert safe_eval('a', dict(a='None')) is None
    # test for safe operators

# Generated at 2022-06-13 15:28:45.026189
# Unit test for function safe_eval
def test_safe_eval():
    if sys.version_info[0] == 3:
        unicode_type = str

    assert safe_eval("ansible_foobar == 'red'")
    assert not safe_eval("ansible_foobar == 'blue'")

    safe_eval("1 + 1", include_exceptions=True)
    safe_eval("a + b", include_exceptions=True, locals=dict(a=1, b=1))

    assert safe_eval("1 + 1") == 2
    assert safe_eval("'ansible_' + 'foobar'") == 'ansible_foobar'

    assert safe_eval("a + b", locals=dict(a=1, b=1)) == 2

# Generated at 2022-06-13 15:28:53.076534
# Unit test for function safe_eval

# Generated at 2022-06-13 15:29:00.111079
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('5') == 5
    assert safe_eval('{"a":1}') == {"a":1}
    assert safe_eval('[5,6]') == [5,6]
    assert safe_eval("'five'") == 'five'
    assert safe_eval("'five' + 'six'") == 'fivesix'
    assert safe_eval("1 + 2") == 3
    assert safe_eval("'1' + '2'") == '12'
    assert safe_eval('[1,2] + [3,4]') == [1,2,3,4]
    assert safe_eval('{"a": 1} + {"b": 2}') == {"a":1, "b":2}

# Generated at 2022-06-13 15:29:03.765053
# Unit test for function safe_eval
def test_safe_eval():
    import re
    # test a few basic types
    assert safe_eval('1') == 1
    assert safe_eval('None') == None
    assert safe_eval('true') == True
    assert safe_eval('string') == "string"
    assert safe_eval('["a", "b", "c", 1, 2, 3]') == ["a", "b", "c", 1, 2, 3]
    assert safe_eval("{'a':1, 'b':2, 'c': 3, null: 99}") == {'a':1, 'b':2, 'c': 3, 'null': 99}
    assert safe_eval("('a', 'b', 'c', 1, 2, 3)") == ('a', 'b', 'c', 1, 2, 3)
    # Test math operations

# Generated at 2022-06-13 15:29:11.008814
# Unit test for function safe_eval

# Generated at 2022-06-13 15:29:19.532151
# Unit test for function safe_eval
def test_safe_eval():
    assert 3 == safe_eval('1 + 2')
    assert 1 == safe_eval(' 0  and  1 or 2')
    assert "text" == safe_eval('"text"')

# Generated at 2022-06-13 15:29:32.635449
# Unit test for function safe_eval
def test_safe_eval():
    # Simple test
    assert safe_eval('2 + 3') == 5

    # Disallowed node type
    try:
        safe_eval('__import__("os").system("rm -rf /")')
    except Exception as e:
        assert 'invalid expression' in str(e)
    else:
        assert False, "unexpected success"

    # Convert original exception message
    try:
        safe_eval('a[0]')
    except Exception as e:
        assert "name 'a' is not defined" in str(e)
    else:
        assert False, "unexpected success"

    # Complex test
    try:
        safe_eval('all_hosts[:3]')
    except Exception as e:
        assert "name 'all_hosts' is not defined" in str(e)

# Generated at 2022-06-13 15:29:40.453218
# Unit test for function safe_eval
def test_safe_eval():

    if sys.version_info[0] == 2:
        from ansible.module_utils.six import b
    else:
        def b(unicode_object):
            return unicode_object.encode('utf-8')


# Generated at 2022-06-13 15:29:51.832007
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('"foo"') == 'foo'
    assert safe_eval('foo') == 'foo'
    assert safe_eval('foo + bar', dict(foo=1, bar=2)) == 3
    assert safe_eval('[1,2,3]') == [1, 2, 3]
    assert safe_eval('["a","b","c"]') == ['a', 'b', 'c']
    assert safe_eval('{"a":1,"b":2}') == {'a': 1, 'b': 2}
    assert safe_eval('1') == 1
    assert safe_eval('null') is None
    assert safe_eval('true') is True
    try:
        assert safe_eval('False and True') is True
    except:
        pass
    assert safe_eval('False or True') is True
   

# Generated at 2022-06-13 15:29:59.958050
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('[1,2,3]') == [1, 2, 3]
    assert safe_eval('{"foo": "bar"}') == {"foo": "bar"}
    assert safe_eval('42') == 42

    assert safe_eval('foo') == 'foo'
    assert safe_eval('foo.bar') == 'foo.bar'
    assert safe_eval('foo + bar') == 'foo + bar'

    assert safe_eval('foo + bar', dict(foo=42,
                                       bar=13)) == 55
    assert safe_eval('foot(bar)', dict(foo=True,
                                       bar=False),
                      include_exceptions=True) == ('foot(bar)', None)

    # set callable whitelist
    CALL_ENABLED.append('callable')

# Generated at 2022-06-13 15:30:06.292631
# Unit test for function safe_eval

# Generated at 2022-06-13 15:30:16.701196
# Unit test for function safe_eval
def test_safe_eval():
    # test for globs
    glob_result = safe_eval('foo', {'foo': 'bar'}, True)
    assert to_native(glob_result[0]) == 'bar'
    glob_result = safe_eval('foo', True)
    assert glob_result[0] == 'foo'

    # test for simple stuff
    result = safe_eval('1 + 1', True)
    assert result[0] == 2
    result = safe_eval('1 + 1', {'foo': 'bar'}, True)
    assert result[0] == 2

    # test for list
    result = safe_eval('[1, 2, 3] + [4, 5, 6]', True)
    assert result[0] == [1, 2, 3, 4, 5, 6]

    # test for dict
    result = safe_

# Generated at 2022-06-13 15:30:25.213127
# Unit test for function safe_eval
def test_safe_eval():
    """
    ref: https://docs.python.org/2/library/ast.html#abstract-grammar
    """
    # supported AST nodes
    assert safe_eval("1 + 2 + 3") == 6
    assert safe_eval("1 - 2 - 3") == -4
    assert safe_eval("3 * 4 * 5") == 60
    assert safe_eval("2 ** 3 ** 4") == 2 ** 81
    assert safe_eval("7 / 2 / 3") == 7 / 6.0
    assert safe_eval("-42") == -42
    assert safe_eval("42") == 42
    assert safe_eval("1 == 1")
    assert not safe_eval("1 != 1")
    assert not safe_eval("1 is None")

# Generated at 2022-06-13 15:30:31.492780
# Unit test for function safe_eval
def test_safe_eval():
    '''
    The safe_eval function may also call certain builtin functions such as
    len and str. Support for this is determined by the CALL_ENABLED option.
    Note: This is a global variable and hence changes will persist over calls.
    '''
    # save off the current value of CALL_ENABLED
    saved_call_enabled = safe_eval.__globals__['CALL_ENABLED']
    try:
        # perform test with no extra builtins enabled
        safe_eval.__globals__['CALL_ENABLED'] = []
        _test_safe_eval()

        # repeat test with len enabled
        safe_eval.__globals__['CALL_ENABLED'] = ['len']
        _test_safe_eval()
    finally:
        # restore the original value
        safe_

# Generated at 2022-06-13 15:30:40.724361
# Unit test for function safe_eval
def test_safe_eval():
    # Evaluate expressions that should work
    safe_eval('1')
    safe_eval('foo')
    safe_eval('True')
    safe_eval('False')
    safe_eval('None')
    safe_eval('foo + bar')
    safe_eval('foo.bar')
    safe_eval('foo[0]')
    safe_eval('foo["bar"]')
    safe_eval('foo["bar"][0]')
    safe_eval('[1, 2, 3]')
    safe_eval('[1, foo, 3]')
    safe_eval('{1: 2, 3: 4}')
    safe_eval('{1: 2, "foo": 4}')
    safe_eval('{1: 2, 3: foo}')
    safe_eval('{1: "foo", 3: foo}')



# Generated at 2022-06-13 15:30:51.951012
# Unit test for function safe_eval
def test_safe_eval():
    # Strings
    assert(safe_eval('hello') == 'hello')
    assert(safe_eval('"hello"') == 'hello')
    assert(safe_eval('u"hello"') == 'hello')
    # ints
    assert(safe_eval('1') == 1)
    assert(safe_eval('-1') == -1)
    assert(safe_eval('0xff') == 255)
    assert(safe_eval('0o10') == 8)
    assert(safe_eval('-0xff') == -255)
    assert(safe_eval('-0o10') == -8)
    # lists
    assert(safe_eval('[]') == [])
    assert(safe_eval('[1,-2,3]') == [1,-2,3])

# Generated at 2022-06-13 15:31:00.276807
# Unit test for function safe_eval
def test_safe_eval():
    # Test the safe evals
    assert safe_eval("[1, 2, 3]") == [1, 2, 3]
    assert safe_eval("2+2") == 4
    assert safe_eval("pow(2,5)") == 32
    assert safe_eval("3*3.14") == 9.42
    assert safe_eval("[1, pow(2,5), range(5)]") == [1, 32, [0, 1, 2, 3, 4]]
    assert safe_eval("{'a': 1, 'b': 2}", include_exceptions=True) == ({'a': 1, 'b': 2}, None)
    assert safe_eval("[pow(2,5), range(5)]") == [32, [0, 1, 2, 3, 4]]

# Generated at 2022-06-13 15:31:10.509422
# Unit test for function safe_eval
def test_safe_eval():

    # Test when CALL_ENABLED is empty
    assert safe_eval('1+1') == 2
    assert safe_eval('1+1') != 3

    assert safe_eval('a_list_variable | length') == 'a_list_variable | length'
    assert safe_eval('a_list_variable | length') != 'a_list_variable'

    assert safe_eval('a_list_variable.append("two")') == 'a_list_variable.append("two")'
    assert safe_eval('a_list_variable.append("two")') != 'a_list_variable.append'

    assert safe_eval('[ item for item in a_list_variable ]') == \
        '[ item for item in a_list_variable ]'

# Generated at 2022-06-13 15:31:17.373666
# Unit test for function safe_eval
def test_safe_eval():

    def test(expr, expected, locals=None):
        actual = safe_eval(expr, locals=locals)
        if actual != expected:
            print("%s != %s" % (to_native(actual), expected))
            return False
        return True

    assert test('"test"', 'test')
    assert test('true', True)
    assert test('false', False)
    assert test('null', None)
    assert test('1 + 1', 2)
    assert test('var2', 3, locals=dict(var2=3))
    assert test('[1,2,3]', [1, 2, 3])
    assert test('{"foo": "bar"}', {"foo": "bar"})
    assert test('{"foo": var2}', {"foo": 3}, locals=dict(var2=3))

# Generated at 2022-06-13 15:31:29.104062
# Unit test for function safe_eval
def test_safe_eval():
    """ Unit test for function safe_eval.
    """
    assert safe_eval('1 + 1') == 2
    assert safe_eval('1 * 6') == 6
    assert safe_eval('a', dict(a=9)) == 9
    assert safe_eval('foo', dict(foo='bar')) == 'bar'

    # Test list
    assert safe_eval('[1,2,3]') == [1, 2, 3]
    assert safe_eval('[[1,2],[3,4]]') == [[1, 2], [3, 4]]

    # Test dict
    assert safe_eval('{"k1":"v1","k2":"v2"}') == {u'k1': u'v1', u'k2': u'v2'}

    # Test dict with unicode

# Generated at 2022-06-13 15:31:36.794223
# Unit test for function safe_eval
def test_safe_eval():
    # First, prove a regular eval works
    assert(eval("1 + 2") == 3)

    # Assert known valid expressions
    assert(safe_eval("1 + 2") == 3)
    assert(safe_eval("1 / True") == 1.0)
    assert(safe_eval("[1, 2, 3]") == [1, 2, 3])
    assert(safe_eval("[1, 2, 3] + [4, 5, 6]") == [1, 2, 3, 4, 5, 6])
    assert(safe_eval("(1, 2, 3)") == (1, 2, 3))
    assert(safe_eval("{1:'one', 2:'two', 3:'three'}") == {1: 'one', 2: 'two', 3: 'three'})

# Generated at 2022-06-13 15:31:44.694016
# Unit test for function safe_eval
def test_safe_eval():
    # assert that basic literals work
    assert safe_eval('1') == 1
    assert safe_eval('[1, 2, 3]') == [1, 2, 3]
    assert safe_eval('{"a": 1, "b": 2}') == {"a": 1, "b": 2}
    assert safe_eval('"string"') == 'string'

    # compare and operations
    assert safe_eval('1 < 2')
    assert safe_eval('3 > 2')
    assert safe_eval('[1, 2, 3] < [1, 2, 4]')
    assert safe_eval('"string" > "str"')

    # evaluate a combination of literals and operations
    assert safe_eval('1 in [1, 2, 3]')
    assert safe_eval('[2] < [1, 2, 3]')

# Generated at 2022-06-13 15:31:55.184460
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval("[1,2,'3']") == [1, 2, '3']
    assert safe_eval("{'k1': 'v1'}") == {'k1': 'v1'}
    assert safe_eval("{'k1': 'v1', 'k2': ['1', 2, '3']}") == {'k1': 'v1', 'k2': ['1', 2, '3']}
    assert safe_eval("16") == 16
    assert safe_eval("16.5") == 16.5
    assert safe_eval("'16.5'") == '16.5'
    assert safe_eval("'test'") == 'test'
    assert safe_eval("True") is True
    assert safe_eval("False") is False
    assert safe_eval("None") is None


# Generated at 2022-06-13 15:32:05.808330
# Unit test for function safe_eval
def test_safe_eval():
    success = 0
    failed = 0

# Generated at 2022-06-13 15:32:17.857495
# Unit test for function safe_eval
def test_safe_eval():
    print('ansible_safe_eval unit tests')
    assert safe_eval('blah') == 'blah'
    assert safe_eval('1 + 1') == 2
    assert safe_eval('[1, 2, 3]') == [1, 2, 3]
    assert safe_eval('{ "a": "b", "b": "c" }') == { "a": "b", "b": "c" }
    assert safe_eval('1 + 1') == 2
    assert safe_eval('-3') == -3
    assert safe_eval('None') is None
    assert safe_eval('true') is True
    assert safe_eval('false') is False

    # These should all fail and raise an exception
    try:
        safe_eval('import subprocess')
    except:
        pass
    else:
        assert False

# Generated at 2022-06-13 15:32:29.871815
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('1') == 1
    assert safe_eval('a') == 'a'
    assert safe_eval('a.b') == 'a.b'
    assert safe_eval('a["b"]') == 'a["b"]'
    assert safe_eval('a[1]') == 'a[1]'
    assert safe_eval('a[1].c') == 'a[1].c'

    assert safe_eval('[1,2]') == [1, 2]
    assert safe_eval('[1,2] | length') == [1, 2]
    assert safe_eval('[1,2] | length().txt') == [1, 2]
    assert safe_eval('[1,2] + [3,4]') == [1, 2, 3, 4]

# Generated at 2022-06-13 15:32:43.334237
# Unit test for function safe_eval
def test_safe_eval():
    # test some simple valid expressions
    expr = "1 + 2"
    result = safe_eval(expr)
    assert result == 3

    expr = "1 + 2 + 3"
    result = safe_eval(expr)
    assert result == 6

    expr = "11 - 2"
    result = safe_eval(expr)
    assert result == 9

    expr = "1 - 2"
    result = safe_eval(expr)
    assert result == -1

    # test some simple invalid expressions
    expr = "1 + "
    try:
        result = safe_eval(expr)
    except Exception:
        pass

    expr = "1 + + 2"
    try:
        result = safe_eval(expr)
    except Exception:
        pass

    expr = "1 & 2"

# Generated at 2022-06-13 15:32:53.423389
# Unit test for function safe_eval
def test_safe_eval():
    class TestClass:
        def __init__(self, x):
            self.x = x

    testclass = TestClass(sys)
    env = {'foo': testclass}

    from ansible.playbook import Play
    from ansible.playbook.play_context import PlayContext

    play = Play().load({'name': "foo",
                        'hosts': 'all',
                        'vars': {'var1': {'a': 12},
                                 'foo': "bar",
                                 'baz': True,
                                 'some_attr': {'nested': "attr"}}},
                       variable_manager=None, loader=None)
    play.set_variable_manager(None)
    play_context = PlayContext(play=play)

# Generated at 2022-06-13 15:33:03.678399
# Unit test for function safe_eval
def test_safe_eval():

    # success cases
    assert safe_eval('1 + 1') == 2
    assert safe_eval('"a"') == 'a'
    assert safe_eval('1.2') == 1.2
    assert safe_eval('(1 + 5)/2') == 3
    assert safe_eval('a or b', locals={'a': 'a'}) == 'a'
    assert safe_eval('a or b', locals={'b': 'b'}) == 'b'
    assert safe_eval('a and b', locals={'a': 'a'}) == 'b'
    assert safe_eval('a and b', locals={'b': 'b'}) == 'b'
    assert safe_eval('not a', locals={'a': False})
    assert safe_eval('a == b', locals={'a': 'a'}) == False


# Generated at 2022-06-13 15:33:15.126497
# Unit test for function safe_eval
def test_safe_eval():
    mystring = "'a string'"
    myint = "44"
    mylist = "['a','b','c']"
    mydict = "{'a':'b','c':'d'}"
    myliteral = '{"a":"b","c":"d"}'

    def _safe_eval(expr, expect, **kwargs):
        result, exception = safe_eval(expr, **kwargs)
        result = '%s' % result
        if exception is not None:
            result = '<exception>%s' % exception

        assert result == expect, "%s returned %s, expected %s" % (expr, result, expect)

    _safe_eval(mystring, "'a string'")
    _safe_eval(myint, "44")

# Generated at 2022-06-13 15:33:26.293659
# Unit test for function safe_eval
def test_safe_eval():
    """
    Test safe_eval function
    """
    # Validate that a list returns as a list
    assert isinstance(safe_eval('["test", "test2"]'), list)

    # Validate that the eval safely allows known variables to evaluate
    local_vars = {'var1': 'test', 'var2': 'test2'}
    assert safe_eval('var1', local_vars) == 'test'
    assert safe_eval('var2', local_vars) == 'test2'

    # Validate that a variable name starting with a number cannot be evaluated
    with pytest.raises(Exception):
        # string should not be eval'd, it is not quoted, so it should raise
        safe_eval('1var1')

    # Validate that a variable name starting with a number can be allowed if escaped
    assert safe

# Generated at 2022-06-13 15:33:32.534972
# Unit test for function safe_eval

# Generated at 2022-06-13 15:33:43.496191
# Unit test for function safe_eval
def test_safe_eval():
    '''safe_eval should allow the following to run without raising an exception:'''

    # (a + b)
    safe_eval('(a + b)')
    # (a - b)
    safe_eval('(a - b)')
    # (a / b)
    safe_eval('(a / b)')
    # (a // b)
    safe_eval('(a // b)')
    # (a ** b)
    safe_eval('(a ** b)')
    # (a % b)
    safe_eval('(a % b)')
    # (a * b)
    safe_eval('(a * b)')
    # [1, 2, 3]
    safe_eval('[1, 2, 3]')
    # {foo: bar}

# Generated at 2022-06-13 15:33:54.680181
# Unit test for function safe_eval
def test_safe_eval():
    result, exception = safe_eval("0 * 4 * [1, 2, 3]", None, True)
    assert result == [0, 0, 0]
    result, exception = safe_eval("0 * 4 * (1, 2, 3)", None, True)
    assert result == (0, 0, 0)
    result, exception = safe_eval("0 * 4 * {'a': 1, 'b': 2, 'c': 3}", None, True)
    assert result == {'a': 0, 'b': 0, 'c': 0}
    result, exception = safe_eval("0 * 4 * {'a': 1, 'b': 2, 'c': [1, 2, 3]}", None, True)
    assert result == {'a': 0, 'b': 0, 'c': [0, 0, 0]}
    result

# Generated at 2022-06-13 15:34:05.397518
# Unit test for function safe_eval

# Generated at 2022-06-13 15:34:13.851519
# Unit test for function safe_eval
def test_safe_eval():
    '''
    Example AST of an expression
    >>> import ast
    >>> expr = "1 + (2 * 3)"
    >>> tree = ast.parse(expr, mode='eval')
    >>> print(ast.dump(tree))
    "Expression(body=BinOp(left=Num(n=1), op=Add(), right=BinOp(left=Num(n=2), op=Mult(), right=Num(n=3))))"
    '''

    # Simple expressions
    print("Simple expressions")
    assert safe_eval("1 + 2") == 3
    assert safe_eval("1 + (2 * 3)") == 7
    assert safe_eval("1 + (4 / 2)") == 3

    # Dicts
    print("Dicts")
    assert safe_eval("{'a': 1, 'b': 2}")

# Generated at 2022-06-13 15:34:30.354071
# Unit test for function safe_eval
def test_safe_eval():
    ''' test safe_eval '''

    ############################
    #### Safe eval examples ####

    # Basic arithmetic
    assert isinstance(safe_eval('1 + 2'), int)
    assert isinstance(safe_eval('1 + 2'), int)
    assert isinstance(safe_eval('1 + 2 * 3'), int)
    assert isinstance(safe_eval('(1 + 2) * 3'), int)

    # Boolean logic
    assert isinstance(safe_eval('3 == 3'), bool)
    assert isinstance(safe_eval('a == 3', dict(a=3)), bool)
    assert isinstance(safe_eval('1 < 2'), bool)
    assert isinstance(safe_eval('1 < 2 and 2 < 3'), bool)

    # Lists

# Generated at 2022-06-13 15:34:40.151997
# Unit test for function safe_eval
def test_safe_eval():
    """
    Test cases for function safe_eval
    """
    # empty
    assert safe_eval('') == ''
    # string
    assert safe_eval('"foo"') == 'foo'
    # integer
    assert safe_eval('1234') == 1234
    # float
    assert safe_eval('1234.5678') == 1234.5678
    # negative float
    assert safe_eval('-1234.5678') == -1234.5678
    # negative float 2
    assert safe_eval('-1234.5678') == -1234.5678
    # negative float 3
    assert safe_eval('-0.5678') == -0.5678
    # negative float 4
    assert safe_eval('-0.0') == -0.0
    # negative integer
    assert safe_

# Generated at 2022-06-13 15:34:47.337722
# Unit test for function safe_eval

# Generated at 2022-06-13 15:34:58.837205
# Unit test for function safe_eval
def test_safe_eval():
    # check number
    assert safe_eval('3') == 3
    assert safe_eval(3) == 3

    # check string
    assert safe_eval('"hello world"') == "hello world"
    assert safe_eval('u"hello world"') == "hello world"

    # check boolean
    assert safe_eval('True') is True
    assert safe_eval('true') is True
    assert safe_eval('False') is False
    assert safe_eval('false') is False

    # check json null
    assert safe_eval('null') is None

    # check list
    assert safe_eval('[]') == []
    assert safe_eval('[1,2,3]') == [1,2,3]

    # check dict
    assert safe_eval('{}') == {}

# Generated at 2022-06-13 15:35:07.766754
# Unit test for function safe_eval
def test_safe_eval():
    val = safe_eval("'string'")
    assert val == 'string'

    val = safe_eval('{"a":"list","b":3}')
    assert val == {'a': 'list', 'b': 3}

    val = safe_eval('True')
    assert val is True

    val = safe_eval('False')
    assert val is False

    val = safe_eval('null')
    assert val is None

    val = safe_eval('1 and 0')
    assert val is False

    val = safe_eval('1 or 0')
    assert val is True

    val = safe_eval('"string" or "other"')
    assert val == 'string'

    val = safe_eval('"" or "other"')
    assert val == 'other'

    val = safe_eval('1 and 3 or 0')


# Generated at 2022-06-13 15:35:15.852651
# Unit test for function safe_eval
def test_safe_eval():
    if sys.version_info < (2, 7):
        pytest.skip("Test requires Python 2.7+")

    # No exceptions expected
    assert safe_eval('1') == 1
    assert safe_eval('a_list_variable') == 'a_list_variable'
    assert safe_eval('1.1 + 1.0') == 2.1
    assert safe_eval('"ansible"') == "ansible"
    assert safe_eval('"ansible is great"') == "ansible is great"
    assert safe_eval('"{{ ansible is great }}"') == "{{ ansible is great }}"
    assert safe_eval('a_list_variable_with_list') == 'a_list_variable_with_list'

# Generated at 2022-06-13 15:35:25.773093
# Unit test for function safe_eval
def test_safe_eval():
    tests = (
        (1, 1),
        ('foo', 'foo'),
        ('some_list', 'some_list'),
     # this will fail because the expression contains a call
     # to python's builtin function map(), which we've not
     # whitelisted in this example
     #('some_list | map(attribute=foo) | list', 'some_list | map(attribute=foo) | list'),
        ('some_var.split(".")', 'some_var.split(".")'),
        ('isinstance(1, int)', True),
        ('[[1, 2], [3, 4]]', [[1, 2], [3, 4]]),
    )
    for expr, expected in tests:
        yield check_safe_eval, expr, expected
    # Test additional builtins

# Generated at 2022-06-13 15:35:34.908840
# Unit test for function safe_eval
def test_safe_eval():
    '''Unit test for function safe_eval'''
    # Test all valid syntax that you want to allow.

# Generated at 2022-06-13 15:35:40.459446
# Unit test for function safe_eval
def test_safe_eval():
    # boolean
    assert safe_eval("true") is True
    assert safe_eval("false") is False
    # arithmetic operators
    assert safe_eval("3 + 7") == 10
    assert safe_eval("2 - 4") == -2
    # comparisons
    assert safe_eval("3 > 7") is False
    assert safe_eval("2 < 4") is True
    assert safe_eval("6 <= 6") is True
    assert safe_eval("6 >= 6") is True
    assert safe_eval("1 == 1") is True
    assert safe_eval("1 == 2") is False
    assert safe_eval("1 != 2") is True
    assert safe_eval("1 != 1") is False
    # logical operators
    assert safe_eval("true and false") is False
    assert safe_eval("true and true") is True

# Generated at 2022-06-13 15:35:50.617772
# Unit test for function safe_eval
def test_safe_eval():
    '''
    Basic idea of this test is to build up a data structure
    with a number of sub-elements which can be used to test
    the safe_eval function
    '''

    # Example data structure

# Generated at 2022-06-13 15:36:07.613196
# Unit test for function safe_eval

# Generated at 2022-06-13 15:36:15.876193
# Unit test for function safe_eval
def test_safe_eval():
    # test simple expression
    test_expr = '1 + 1'
    result = safe_eval(test_expr)
    if not result == 2:
        raise Exception("failed to evaluate %s" % test_expr)

    # test expression with list and dict
    test_expr = '1 + 1 == 2 and [1, 2] == [1, 2] and {1: 2} == {1: 2}'
    result = safe_eval(test_expr)
    if not result == True:
        raise Exception("failed to evaluate %s" % test_expr)

    # test expression with local variable
    test_expr = 'a_dict["a"]'
    a_dict = { "a": 1 }
    result = safe_eval(test_expr, locals=locals())

# Generated at 2022-06-13 15:36:24.951321
# Unit test for function safe_eval
def test_safe_eval():

    def _test_safe_eval(expr, locals_vars, expected_result):
        '''
        Test safe_eval function with different input expression,
        locals_vars and expected_results.
        '''
        actual_result = safe_eval(expr, locals_vars)
        assert expected_result == actual_result, \
            ("Eval for expression '%s' "
             "with locals_vars %s failed.\n"
             "Got result: %s\n"
             "Expected result: %s\n"
             % (expr, locals_vars, actual_result, expected_result))

    # test various inputs
    _test_safe_eval('1', {}, 1)
    _test_safe_eval('a', {'a': 1}, 1)

# Generated at 2022-06-13 15:36:31.567050
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval("foo") == 'foo'
    assert safe_eval("foo.bar") == 'foo.bar'
    assert safe_eval("(1 + 2)") == 3
    assert safe_eval("{'foo.bar': 'baz'}") == {"foo.bar": "baz"}
    assert safe_eval("['foo.bar', 'baz']") == ['foo.bar', 'baz']
    assert safe_eval("1 and 0") == 0
    assert safe_eval("(1, 2)") == (1, 2)
    assert safe_eval("[1, 2]") == [1, 2]
    assert safe_eval("{1:2}") == {1: 2}
    assert safe_eval("True") is True
    assert safe_eval("False") is False

# Generated at 2022-06-13 15:36:42.513850
# Unit test for function safe_eval
def test_safe_eval():
    # Test CALL_ENABLED
    safe_eval('builtins.len([1,2,3,4])', include_exceptions=True)
    CALL_ENABLED.append('len')
    (rc, err) = safe_eval('builtins.len([1,2,3,4])', include_exceptions=True)
    assert rc == 4
    assert err == None

    # Test simple expressions
    result = safe_eval('1 + 2')
    assert result == 3

    result = safe_eval('3 * 3')
    assert result == 9

    result = safe_eval('((2 + 5) * (3 + 7)) / 2')
    assert result == 30

    result = safe_eval('5 - 1')
    assert result == 4

    result = safe_eval('5 - (1 - 1)')

# Generated at 2022-06-13 15:36:54.208653
# Unit test for function safe_eval
def test_safe_eval():
    """
    The following tests were generated using the following Python script,
    which provides a simple way to generate a test suite for Python AST
    rules.

    The script is available on the following URL:
    https://gist.github.com/veksman/1a3d6f5691f63c7dfdd5

    <begin script>
    from __future__ import print_function
    import ast
    import itertools
    import logging
    import sys
    import optparse

    class AstTestGenerator(object):
        """

# Generated at 2022-06-13 15:37:03.186588
# Unit test for function safe_eval
def test_safe_eval():
    """most of the hard work is done in the CleansingNodeVisitor"""
    assert safe_eval('{foo: 1}') == {'foo': 1}
    assert safe_eval('{"foo": 1}') == {'foo': 1}
    assert safe_eval('[1, 2, 3]') == [1, 2, 3]
    assert safe_eval('(1, 2, 3)') == (1, 2, 3)
    assert safe_eval('a + 1 < 5', dict(a=2))
    assert safe_eval('True')
    assert safe_eval('None')
    assert not safe_eval('__import__("os").system("ls")')
    assert safe_eval("ansible_facts['os_family']")

# Generated at 2022-06-13 15:37:11.979231
# Unit test for function safe_eval
def test_safe_eval():

    # test all valid expressions
    # with_items: a_list_variable
    # with_items:
    #   - item1
    #   - item2
    expr = ("with_items: a_list_variable\n"
            "with_items:\n"
            "  - item1\n"
            "  - item2\n"
            "with_items: {{ a_list_variable }}\n"
            "with_items:\n"
            "  - {{ item1 }}\n"
            "  - {{ item2 }}\n")
    data = safe_eval(expr, dict(a_list_variable=['item1', 'item2']), include_exceptions=True)
    assert data[0] == ['item1', 'item2']
    assert data[1] is None

    # test all

# Generated at 2022-06-13 15:37:21.233843
# Unit test for function safe_eval
def test_safe_eval():
    # test 1: valid input
    expr = 'True and 10'
    result = safe_eval(expr)
    assert result is not None
    assert result is not False
    assert result is not True
    assert isinstance(result, int)
    assert result == 10

    # test 2: invalid syntax
    expr = 'True and 10 and'
    result = safe_eval(expr)
    assert result is not None
    assert result is not False
    assert result is not True
    assert isinstance(result, string_types)
    assert expr == result

    # test 3: invalid syntax
    expr = 'True and 10 and'
    result = safe_eval(expr, include_exceptions=True)
    assert result is not None
    assert result is not False
    assert result is not True
    assert isinstance(result, tuple)

# Generated at 2022-06-13 15:37:32.880247
# Unit test for function safe_eval
def test_safe_eval():
    '''
    Unit test for function safe_eval

    Example use:
    import sys
    sys.path.insert(0,'/path/to/lib/ansible')

    from ansible.utils import test_safe_eval
    test_safe_eval.run()
    '''
    def _run_tests(tests):
        ''' Generic testrunner for safe_eval tests '''
        test_errors = {}
        for test in tests:
            if isinstance(test['res'], type):
                result = safe_eval(test['inp'], include_exceptions=True)

# Generated at 2022-06-13 15:37:58.729376
# Unit test for function safe_eval
def test_safe_eval():
    expr = "a_list_variable"
    locals = {'a_list_variable': [1, 2, 3]}

    try:
        result = safe_eval(expr, locals=locals)
        if result != [1, 2, 3]:
            print("ERROR: got result %s from expr %s" % (result, expr))
    except Exception as e:
        print("ERROR: failed to parse expression %s: %s" % (expr, e))

    expr = "[item for item in a_list_variable]"

# Generated at 2022-06-13 15:38:06.371853
# Unit test for function safe_eval