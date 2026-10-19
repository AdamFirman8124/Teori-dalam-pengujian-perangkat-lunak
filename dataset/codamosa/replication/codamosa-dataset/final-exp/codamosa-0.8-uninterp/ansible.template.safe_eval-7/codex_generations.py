

# Generated at 2022-06-13 15:28:06.647830
# Unit test for function safe_eval
def test_safe_eval():
    '''
    safe_eval unit tests
    '''
    assert safe_eval('1') == 1
    assert safe_eval('True') == True
    assert safe_eval('True and False') == False
    assert safe_eval('True or False') == True
    assert safe_eval('True or False and False') == True
    assert safe_eval('True or False and False or True') == True
    assert safe_eval('"foo"') == 'foo'
    assert safe_eval('"foo" + "bar"') == 'foobar'
    assert safe_eval('"foo" + "bar" + "baz"') == 'foobarbaz'
    assert safe_eval('[1, 2, 3]') == [1, 2, 3]

# Generated at 2022-06-13 15:28:15.987442
# Unit test for function safe_eval
def test_safe_eval():
    #
    # Test converting all json types to native types
    #
    res = safe_eval("{'sub': [{'subsub': {'value': 'test'}}, 'foo', 'bar']}")
    assert res['sub'][0]['subsub']['value'] == 'test'
    assert res['sub'][1] == 'foo'
    assert res['sub'][2] == 'bar'

    #
    # stuff that will test syntax errors, and invalid expressions
    #

    # this one is OK
    safe_eval('[1,2,3]')

    printable = True

# Generated at 2022-06-13 15:28:24.172466
# Unit test for function safe_eval
def test_safe_eval():
    cmd = '{{ foo + 5 }}'
    result, err = safe_eval(cmd, dict(foo=1), include_exceptions=True)
    assert not err
    assert result == 6

    result, err = safe_eval(cmd, dict(foo='1'), include_exceptions=True)
    assert not err
    assert result == '1'

    # Test safe_eval works with complex expressions
    cmd = '{{ foo + 1 < 5 - bar }}'
    result, err = safe_eval(cmd, dict(foo=2, bar=3), include_exceptions=True)
    assert not err
    assert result == True

    # Test safe_eval works with expression containing dict, list, str and int
    cmd = '{{ [1,2] + ["abc"] + foo + "bca" + bar }}'
    result, err

# Generated at 2022-06-13 15:28:34.034316
# Unit test for function safe_eval
def test_safe_eval():
    def assert_safe_eval(s, locals=None, expected=None):
        ans = safe_eval(s, locals=locals)
        assert expected is None or ans == expected, "input %s was %s and not %s" % (s, ans, expected)

    def assert_unsafe_eval(s, locals=None, expected=None):
        ans = safe_eval(s, locals=locals, include_exceptions=True)

# Generated at 2022-06-13 15:28:43.469860
# Unit test for function safe_eval
def test_safe_eval():

    def eval_and_assert_equal(expr, expected_value):
        result = safe_eval(expr)
        assert result == expected_value, 'safe_eval(%s) returned %s' % (expr, result)

    def eval_and_assert_exception(expr):
        result, exception = safe_eval(expr, include_exceptions=True)
        assert exception, 'safe_eval(%s) did not raise an exception' % expr

    # simple bin op tests
    eval_and_assert_equal('1 + 2', 3)
    eval_and_assert_equal('1 + 2 + 3', 6)
    eval_and_assert_equal('1 + (2 + 3)', 6)
    eval_and_assert_equal('(1 + 2) + 3', 6)


# Generated at 2022-06-13 15:28:50.060986
# Unit test for function safe_eval
def test_safe_eval():
    '''
    AnsibleModule om declares arguments and passes in locals()
    to the safe_eval function.
    So, locals() contains all the arguments that AnsibleModule.__init__
    takes.
    '''
    locals = dict(
        _ansible_module_name='module_name_for_testing',
        _ansible_module_name_for_testing='example',
        _ansible_version='0.0.0',
        _ansible_selinux_special_fs=C.DEFAULT_SELINUX_SPECIAL_FS,
    )
    # Valid expressions
    assert safe_eval('[]', locals) == []
    assert safe_eval('{}', locals) == {}
    assert safe_eval('[[x,y,z]]', locals) == [['x','y','z']]

# Generated at 2022-06-13 15:28:55.402398
# Unit test for function safe_eval
def test_safe_eval():
    """
    Test to make sure the safe_eval actually works
    """
    # make sure these are valid
    assert safe_eval('a') == 'a'
    assert safe_eval('a or b') == 'a or b'
    assert safe_eval('a and b') == 'a and b'
    assert safe_eval('a + b') == 'a + b'
    assert safe_eval('a - b') == 'a - b'
    assert safe_eval('a in b') == 'a in b'
    assert safe_eval('a not in b') == 'a not in b'

    # truth statements
    assert safe_eval('not a', locals={'a': False}) is True
    assert safe_eval('a', locals={'a': True}) is True

# Generated at 2022-06-13 15:29:05.580554
# Unit test for function safe_eval
def test_safe_eval():
    """
    Test cases for function safe_eval.
    """
    from collections import namedtuple

    # Test cases for valid expressions and the expected result.

# Generated at 2022-06-13 15:29:11.395859
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval("[1,2,3]", include_exceptions=True)[0] == [1, 2, 3]
    assert safe_eval("1 + 1") == 2
    assert safe_eval("False") is False
    assert safe_eval("'hi'", include_exceptions=True)[0] == 'hi'
    assert safe_eval("{'a': 1, 'b': 2}", include_exceptions=True)[0] == {'a': 1, 'b': 2}
    assert safe_eval("container_to_text([1, 2, 3])", dict(container_to_text=container_to_text), include_exceptions=True)[0] == '1, 2, 3'

# Generated at 2022-06-13 15:29:19.746747
# Unit test for function safe_eval
def test_safe_eval():
    for (item, result) in (
            ("", ""),
            ("[]", []),
            ("[1]", [1]),
            ("[1, 2, 3]", [1, 2, 3]),
            ("{}", {}),
            ("{'a': 1}", {'a': 1}),
            ("{'a': 1, 'b': 2}", {'a': 1, 'b': 2})):
        output, exception = safe_eval(item, include_exceptions=True)
        assert output == result and exception is None, "safe_eval failed on %s, output: %s exception: %s" % (item, output, exception)
    # test that we return exception
    item = "import os"

# Generated at 2022-06-13 15:29:34.280559
# Unit test for function safe_eval
def test_safe_eval():
    # no exception should be raised for these
    assert safe_eval('[]') == []
    assert safe_eval('{}') == {}
    assert safe_eval('{"foo": "bar"}') == {'foo': 'bar'}
    assert safe_eval('True') is True
    assert safe_eval('False') is False
    assert safe_eval('None') is None
    assert safe_eval('true') is True
    assert safe_eval('false') is False
    assert safe_eval('null') is None
    assert safe_eval('none') is None
    assert safe_eval('1') == 1
    assert safe_eval('"foo"') == "foo"
    assert safe_eval('1 + 1') == 2
    assert safe_eval('1 + 1 == 2') is True
    assert safe_eval('1 + 1 == 3')

# Generated at 2022-06-13 15:29:40.045493
# Unit test for function safe_eval
def test_safe_eval():
    def _test_safe_eval(expr, expected, expected_error=None):
        rc, value = safe_eval(expr, include_exceptions=True)
        assert not expected_error, "test fails: '%s' should raise an exception" % expr
        assert rc == expected, "test fails: '%s' should have been evaluated to '%s' but instead got '%s'" % (expr, expected, rc)
        # The legacy invocation of ``safe_eval`` does not include exceptions
        assert safe_eval(expr) == expected, "test fails: '%s' should have been evaluated to '%s' but instead got '%s'" % (expr, expected, rc)

    def _test_safe_eval_error(expr, expected_error=Exception):
        rc, value = safe_eval(expr, include_exceptions=True)

# Generated at 2022-06-13 15:29:51.293131
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('[1,2,3]') == [1, 2, 3]

    bad_expr = 'import os'
    if sys.version_info < (3, 0):
        assert safe_eval(bad_expr) == bad_expr
    else:
        assert safe_eval(bad_expr) == 'import os'

    assert safe_eval('1 + 2') == 3

    # this is not OK
    bad_expr = '{{ asdf }}'
    assert safe_eval(bad_expr) == bad_expr

    # this should work
    assert safe_eval('"{{ asdf }}"') == '{{ asdf }}'

    # this is not OK
    bad_expr = '1 + {{asdf}}'
    assert safe_eval(bad_expr) == bad_expr

    # this is not OK


# Generated at 2022-06-13 15:29:59.467494
# Unit test for function safe_eval

# Generated at 2022-06-13 15:30:07.961630
# Unit test for function safe_eval
def test_safe_eval():
    '''
    Test safe_eval function
    '''

    # Make sure safe_eval does not allow executing actual code
    # This catches both Python2 and Python3
    # A Python2 SyntaxError becomes a NameError in Python3

# Generated at 2022-06-13 15:30:18.363201
# Unit test for function safe_eval
def test_safe_eval():
    # test for type conversion for JSON types
    assert safe_eval('true') is True
    assert safe_eval('false') is False
    assert safe_eval('null') is None
    assert safe_eval('false') is False

    # test for binary operators
    assert safe_eval('1 + 2') == 3
    assert safe_eval('1 - 2') == -1
    assert safe_eval('1 * 2') == 2
    assert safe_eval('7 // 2') == 3
    # TODO: fix this flake8 E711 comparison with None should be 'if cond is not None:'
    # changing this breaks some of the test_safe_eval() tests
    assert safe_eval('7 / 2') == 3.5
    assert safe_eval('8 % 2') == 0
    assert safe_eval('1 + 2 * 3') == 7



# Generated at 2022-06-13 15:30:23.469188
# Unit test for function safe_eval
def test_safe_eval():
    # success cases
    assert safe_eval("{{ 'foo' }}", dict(a_list_variable=['foo', 'bar'])) == 'foo'
    assert safe_eval("{{ '{0}' }}", dict(a_list_variable=['foo', 'bar'])) == '{0}'
    assert safe_eval("{{ 1 + 1 }}", dict(a_list_variable=['foo', 'bar'])) == 2

    # fail cases
    assert safe_eval("{{ a_list_variable.append('baz') }}", dict(a_list_variable=['foo', 'bar'])) == "{{ a_list_variable.append('baz') }}"
    assert safe_eval("{{ None.foo }}", dict(a_list_variable=['foo', 'bar'])) == "{{ None.foo }}"
    assert safe

# Generated at 2022-06-13 15:30:30.373441
# Unit test for function safe_eval

# Generated at 2022-06-13 15:30:39.442301
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('foo') == 'foo'
    assert safe_eval('foo < bar') == 'foo < bar'
    assert safe_eval(123) == 123

    # built-in name should fail
    try:
        safe_eval('vars')
    except Exception:
        pass
    else:
        assert False, "vars() built-in should not be allowed"

    # a couple of the builtins are allowed
    assert safe_eval('True') == True

    # booleans
    assert safe_eval('true') == True
    assert safe_eval('false') == False
    # null
    assert safe_eval('null') == None

    # math
    assert safe_eval('(1 + 1)') == 2
    assert safe_eval('(1 + 1) * 2') == 4

# Generated at 2022-06-13 15:30:46.467744
# Unit test for function safe_eval
def test_safe_eval():
    # put all unit tests in one function

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

    def _test(expr, locals=None, result=None):
        if locals is None:
            locals = {}
        eval_result = safe_eval(expr, locals)
        print(eval_result)
        print(result)
        if isinstance(result, Exception):
            assert isinstance(eval_result, tuple)
            assert eval_

# Generated at 2022-06-13 15:30:56.826423
# Unit test for function safe_eval

# Generated at 2022-06-13 15:31:07.717702
# Unit test for function safe_eval
def test_safe_eval():

    def _test_eval(expr, expected, locals=None):
        ''' Helper function to test safe_eval. '''
        result, err = safe_eval(expr, locals=locals, include_exceptions=True)
        assert result == expected
        if err:
            raise err

    # simple numbers, strings and sequences
    _test_eval('42', 42)
    _test_eval('str', 'str')
    _test_eval('[1, 2]', [1, 2])

    # those are allowed in Python but raise an exception in safe_eval
    _test_eval('__import__("os").system("echo hello")', '__import__("os").system("echo hello")', locals={})
    _test_eval('__buildin__', '__buildin__', locals={})

# Generated at 2022-06-13 15:31:10.859582
# Unit test for function safe_eval
def test_safe_eval():
    locals_ = {'my_list': [1, 2, 3]}
    # Test basic eval-like functionality
    assert safe_eval('1 + 1', locals_) == 2
    assert safe_eval('"string"') == 'string'
    assert safe_eval('my_list[0]', locals_) == 1
    assert safe_eval('my_list[1]', locals_) == 2

    # Test that we can call functions in locals
    def my_func(val):
        return val * 2

 

# Generated at 2022-06-13 15:31:17.843430
# Unit test for function safe_eval
def test_safe_eval():
    """ Unit tests for function safe_eval """
    # Test scalars
    assert safe_eval('1 + 1') == 2
    # Test dict
    assert safe_eval('{"a": "b", "c": "d"}') == {"a": "b", "c": "d"}
    # Test list
    assert safe_eval('[1, 2, 3]') == [1, 2, 3]
    # Test list of dicts
    assert safe_eval('[{"a": "b"}, {"c": "d"}]') == [{"a": "b"}, {"c": "d"}]
    # Test set
    assert safe_eval('{1, 2, 3}') == {1, 2, 3}
    # Test set of dicts

# Generated at 2022-06-13 15:31:29.286001
# Unit test for function safe_eval
def test_safe_eval():
    expr = "[1, 2, 'a', 'b', 'c']"
    result = safe_eval(expr)
    assert result == [1, 2, 'a', 'b', 'c']

    expr = "[1, 2, 'a', 'b', 'c'] | count"
    result = safe_eval(expr)
    assert result == expr

    expr = "{ 'a': 1, 'b': 2, 'c': 3 }"
    result = safe_eval(expr)
    assert result == {'a': 1, 'b': 2, 'c': 3}

    expr = "{ 'a': 1, 'b': 2, 'c': 3 } | count"
    result = safe_eval(expr)
    assert result == expr

    expr = "{ 'a': 1, 'b': 2, 'c': 3 } | random"


# Generated at 2022-06-13 15:31:36.916279
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('[1, 2, 3]') == [1, 2, 3]
    assert safe_eval('a or b') == 'a or b'
    assert safe_eval('[1, 2, 3]', {'a':1}) == [1, 2, 3]
    assert safe_eval('[1, 2, a]', {'a':3}) == [1, 2, 3]
    assert safe_eval('[1, 2, 3 + a]', {'a':3}) == [1, 2, 6]
    assert safe_eval('a or b', {'a':'hello', 'b':'goodbye'}) == 'hello'
    assert safe_eval('a and b', {'a':'hello', 'b':'goodbye'}) == 'goodbye'

# Generated at 2022-06-13 15:31:44.784822
# Unit test for function safe_eval
def test_safe_eval():
    import sys
    import ast

    # Test safe_eval()
    assert safe_eval("a + b", {"a": 1, "b": 2}) == 3
    assert safe_eval("c['d']", {"c": {"d": 0}}) == 0
    assert safe_eval("len(a)", {"a": [1, 2, 3]}) == 3
    assert safe_eval("non_existant", {"a": None}) is None
    assert safe_eval("a[0]", {"a": [1, 2, 3]}) == 1
    # should fail:
    if sys.version_info[0] == 2:
        with open("/dev/null") as f:
            assert safe_eval("f", {"f": f}) == "f"

# Generated at 2022-06-13 15:31:55.184868
# Unit test for function safe_eval

# Generated at 2022-06-13 15:32:05.810225
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval("foo", dict(foo="bar")) == "bar"
    assert safe_eval("foo", dict(foo=["bar", "baz"])) == ["bar", "baz"]
    assert safe_eval("foo", dict(foo=["bar", "baz", "{{foo.bar}}"])) == ["bar", "baz", "{{foo.bar}}"]
    assert safe_eval("foo", dict(foo={"bar": "baz"})) == {"bar": "baz"}
    assert safe_eval("foo", dict(foo={"bar": "baz", "ban": "{{foo.bar}}"})) == {"bar": "baz", "ban": "{{foo.bar}}"}

# Generated at 2022-06-13 15:32:17.853415
# Unit test for function safe_eval
def test_safe_eval():
    def assert_safe_eval(expr, result):
        actual = safe_eval(expr)
        assert actual == result, "%r != %r (actual)" % (result, actual)

    def assert_safe_eval_error(expr):
        try:
            actual = safe_eval(expr)
        except Exception:
            return
        assert False, "Expected safe_eval to raise an exception for %s" % expr

    assert_safe_eval('true', True)
    assert_safe_eval_error('function()')
    assert_safe_eval('true and false', False)
    assert_safe_eval('[1, 2, 3]', [1, 2, 3])

# Generated at 2022-06-13 15:32:34.735211
# Unit test for function safe_eval
def test_safe_eval():
    # Addition:
    # The following should pass
    assert safe_eval('[1, 2, 3] + [4, 5, 6]') == [1, 2, 3, 4, 5, 6]
    assert safe_eval('[1, 2, 3] + 4') == [1, 2, 3, 4]
    assert safe_eval('1 + 4') == 5
    assert safe_eval('"test" + "test"') == "testtest"
    # The following should fail
    assert safe_eval('"test" + [1, 2, 3]') == "test[1, 2, 3]"

    # Subtraction:
    # The following should pass
    assert safe_eval('1 - 1') == 0
    assert safe_eval('[1, 2, 3] - [2, 3]') == [1]
   

# Generated at 2022-06-13 15:32:43.158154
# Unit test for function safe_eval
def test_safe_eval():
    # set to True for debugging
    DEBUG = False
    failed = False
    if DEBUG:
        print("Testing safe_eval")
    for index, val in enumerate(C.SAFE_EVAL_LOCALS):
        try:
            result = safe_eval(val)
            if DEBUG:
                print("safe_eval('%s') test %s" % (val, result))
        except:
            failed = True
            print("safe_eval('%s') test %s" % (val, "failed"))
    if index+1 != len(C.SAFE_EVAL_LOCALS):
        failed = True
        print('Wrong number of lines in constants, should have %d lines' % (index+1))
    return failed



# Generated at 2022-06-13 15:32:53.309674
# Unit test for function safe_eval
def test_safe_eval():
    test_vals = [
        ("a + b", {"a": 1, "b": 2}),
        ("a + b", {"a": 'fooo', "b": 'baaaaa'}),
        ("a + b", {"a": [], "b": []}),
        ("a + b", {"a": {}, "b": {}}),
        ("{a:1}", {"a": "foo"}),
        ("{a:1}", {"a": "foo", "b": [1]}),
        ("[1, 2, 3]", {"a": "foo"}),
        ("'a' in x", {"x": "foobar"}),
        ("'a' in x", {"x": ["a", "b", "c"]}),
    ]

# Generated at 2022-06-13 15:33:03.582705
# Unit test for function safe_eval
def test_safe_eval():
    # Test success cases
    if 0:
        # in the future, use assertRaises to make sure this fails
        safe_eval('1+1')
        safe_eval('2 + 3')
        safe_eval('x + y', {'x': 1, 'y': 2})
        safe_eval('x + y', {'x': [1], 'y': ['foo']})
        safe_eval('x + y + z', {'x': 1, 'y': 2, 'z': 3})
        safe_eval('a and b or c', {'a': True, 'b': 'foo', 'c': None})
        safe_eval('null')
        safe_eval('null is None')
        safe_eval('true')
        safe_eval('true is True')
        safe_eval('false')

# Generated at 2022-06-13 15:33:15.045281
# Unit test for function safe_eval
def test_safe_eval():
    def assert_raises_invalid_expression(test_input, with_call_enabled=False):
        if with_call_enabled:
            CALL_ENABLED.append('int')
        try:
            result, error = safe_eval(test_input, include_exceptions=True)
            assert error != None, "Expected an error for test_input '%s'" % test_input
            assert result == test_input, "Expected '%s', received '%s'" % (test_input, result)
        finally:
            if with_call_enabled:
                CALL_ENABLED.remove('int')


# Generated at 2022-06-13 15:33:26.166277
# Unit test for function safe_eval
def test_safe_eval():
    safe_eval("{'msg': 'ok'}")
    safe_eval("{'msg': 'ok'}")
    safe_eval("[]")
    safe_eval("{}")
    safe_eval("1.0")
    safe_eval("-1.0")
    safe_eval("'1.0'")
    safe_eval("0")
    safe_eval("-1")
    safe_eval("1")
    safe_eval("True")
    safe_eval("False")
    safe_eval("None")
    safe_eval("namespace")
    safe_eval("task_vars.get('namespace')")
    safe_eval("task_vars.get('namespace', 'global')")
    safe_eval("True if task_vars.get('namespace', 'global') else False")


# Generated at 2022-06-13 15:33:33.143821
# Unit test for function safe_eval
def test_safe_eval():
    from ansible.module_utils.six import PY3

    # First check that safe_eval does not accept calls
    # to python functions, unless we specify it in our CALL_ENABLED list.
    # By default, we enable list(), but not open()
    #
    # Note: for python2, CALL_ENABLED will be a list.  for python3,
    # it will be a mutable set.
    safe_eval("list()")
    if PY3:
        assert safe_eval("list()") == []
    else:
        assert safe_eval("list()") is None
    safe_eval("list")
    # Uncomment and run to see how safe_eval handles expressions that
    # raise a SyntaxError.
    # safe_eval("a b")
    # safe_eval("[1, 2, 3

# Generated at 2022-06-13 15:33:44.099623
# Unit test for function safe_eval
def test_safe_eval():

    # for python 2.6, 2.7 and 3.4 we can use the built-in unittest module
    if sys.version_info[:3] in [(2,6,0),(2,7,0),(3,4,0)]:
        import unittest
        from ansible.module_utils.common.text.converters import to_bytes


# Generated at 2022-06-13 15:33:55.245429
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('2 + 2') == 4
    assert safe_eval('2 + 2', include_exceptions=True) == (4, None)

    # No valid expression, so we should get the original string back
    assert safe_eval('a + b') == 'a + b'
    # Test behavior with invalid string
    assert safe_eval('a + b', include_exceptions=True) == ('a + b', Exception('invalid expression (a + b)'))

    # Test invalid function name
    assert safe_eval('foo()', include_exceptions=True) == ('foo()', Exception('invalid function: foo'))
    # Test for invalid builtin

# Generated at 2022-06-13 15:34:05.866728
# Unit test for function safe_eval
def test_safe_eval():
    expr1 = 'foo == "bar"'
    (result1, execution_error) = safe_eval(expr1, include_exceptions=True)

    assert result1 == expr1
    assert isinstance(execution_error, Exception)

    expr2 = '2 + 2 == 4'
    (result2, execution_error) = safe_eval(expr2, include_exceptions=True)

    assert isinstance(result2, bool)
    assert result2
    assert execution_error is None

    expr3 = '2 + 2 == 5'
    (result3, execution_error) = safe_eval(expr3, include_exceptions=True)

    assert isinstance(result3, bool)
    assert not result3
    assert execution_error is None

    expr4 = 'bar in foo'
    (result4, execution_error)

# Generated at 2022-06-13 15:34:25.532693
# Unit test for function safe_eval
def test_safe_eval():
    try:
        import astor
        has_astor = True
    except ImportError:
        has_astor = False

    try:
        import yaml
        has_yaml = True
    except ImportError:
        has_yaml = False

    # to_text test cases

# Generated at 2022-06-13 15:34:29.981684
# Unit test for function safe_eval
def test_safe_eval():
    module = AnsibleModule(argument_spec=dict(expr=dict(required=True, type='str')))
    expr = module.params.get('expr')
    result, exception = safe_eval(expr, {}, True)

    if exception:
        module.fail_json(msg=exception, expr=expr)

    module.exit_json(changed=True, result=result, expr=expr)



# Generated at 2022-06-13 15:34:39.622208
# Unit test for function safe_eval
def test_safe_eval():
    # Testing evaluation of basic expressions
    test_eval = safe_eval
    assert test_eval('1 + 1') == 2
    assert test_eval('foo') == 'foo'
    assert test_eval('foo.bar') == 'foo.bar'
    assert test_eval('foo["bar"]') == 'foo["bar"]'
    assert test_eval('foo.bar["1"]') == 'foo.bar["1"]'
    assert test_eval('"foo" + "bar"') == 'foobar'
    assert test_eval('1.0 + 1.0') == 2.0

    # Testing evaluation of dictionary
    assert test_eval('{"a": "b"}', {'a': 'b'}) == {u'a': u'b'}

    # Testing evaluation of list

# Generated at 2022-06-13 15:34:46.935571
# Unit test for function safe_eval
def test_safe_eval():
    # any expressions that evaluate to a non-string
    # should be considered unsafe
    assert safe_eval("'a string'") == 'a string'
    assert safe_eval("'{{STRING}}'") == '{{STRING}}'
    assert safe_eval("[1,2,3,4]") == [1,2,3,4]
    assert safe_eval("{'a': 'b'}") == {'a': 'b'}
    assert safe_eval("1+2*3") == 7
    assert safe_eval("1+2*45") == 91
    assert safe_eval("(1,2,3)") == (1,2,3)
    assert safe_eval("'a string' + 'concatenated'") == 'a stringconcatenated'

# Generated at 2022-06-13 15:34:53.519776
# Unit test for function safe_eval
def test_safe_eval():
    # some simple test cases
    assert safe_eval("2 + 3") == 5
    assert safe_eval("[1, 2, 3]") == [1, 2, 3]
    assert safe_eval('{"a": "b", "c": "d"}') == {"a": "b", "c": "d"}
    # invalid syntax
    assert safe_eval("a + ") == "a + "
    assert safe_eval("a + [") == "a + ["
    # invalid expression
    assert safe_eval("2 + 3 +") == "2 + 3 +"
    # invalid expressions
    assert safe_eval("7 / 0") == "7 / 0"
    assert safe_eval("None.nonesuch") == "None.nonesuch"
    assert safe_eval("x = 5") == "x = 5"
    #

# Generated at 2022-06-13 15:35:02.998341
# Unit test for function safe_eval

# Generated at 2022-06-13 15:35:11.909714
# Unit test for function safe_eval
def test_safe_eval():
    def test_single(test_input, test_output):
        if isinstance(test_output, Exception):
            # test for exception
            result, exception = safe_eval(test_input, include_exceptions=True)
            if exception is None:
                raise Exception("Test failed, expected exception, got '%s'" % result)
        else:
            result = safe_eval(test_input)
            assert result == test_output, "actual value: %s, expected value: %s" % (result, test_output)

    dict_input = {
        'foo': ['bar'],
        'bar': 123
    }
    list_input = ['fizz', 'buzz']


# Generated at 2022-06-13 15:35:20.746428
# Unit test for function safe_eval

# Generated at 2022-06-13 15:35:27.352704
# Unit test for function safe_eval
def test_safe_eval():
    """ Test cases for the safe_eval() function.

    Each test case is a dictionary containing the following entries:
    name: a descriptive string for the test case
    expr: a valid or invalid python expression to evaluate
    is_valid: True if the expression is a valid python expression
    result_type: The result type of the evaluated expression
    result_val: The result value of the evaluated expression
    """

# Generated at 2022-06-13 15:35:36.488419
# Unit test for function safe_eval
def test_safe_eval():
    """
    # Confirm that the function operates as expected
    #   1. Confirm that we can perform safe operations
    #   2. Confirm that we can't perform unsafe operations
    #   3. Confirm that we don't allow calls to builtin functions or builtin modules
    #   4. Confirm that we can call some builtin functions
    #   5. Confirm that we can call user defined functions
    #   6. Confirm that we can call user defined classes

    """
    import ast

    def safe(expr):
        assert expr == safe_eval(expr)
        assert expr == safe_eval(expr, {})

    def unsafe(expr):
        try:
            safe_eval(expr)
        except Exception as e:
            assert "invalid expression" in to_native(e)

# Generated at 2022-06-13 15:36:03.773973
# Unit test for function safe_eval
def test_safe_eval():
    print("Testing safe_eval")

# Generated at 2022-06-13 15:36:11.846583
# Unit test for function safe_eval

# Generated at 2022-06-13 15:36:19.329036
# Unit test for function safe_eval
def test_safe_eval():
    # Inclusion of exception in function output is controlled by the
    # include_exceptions parameter.
    include_exceptions = False
    include_exceptions = True

    # happy path
    expr = "'hello'"
    result, exception = safe_eval(expr, include_exceptions=include_exceptions)
    print("got result %s" % result)
    assert str(result) == 'hello'

    # invalid expression
    expr = "a123"
    result, exception = safe_eval(expr, include_exceptions=include_exceptions)
    if include_exceptions:
        assert exception is not None
    else:
        assert result == expr

    # invalid expression
    expr = "a123"
    result, exception = safe_eval(expr, include_exceptions=include_exceptions)

# Generated at 2022-06-13 15:36:27.421171
# Unit test for function safe_eval
def test_safe_eval():
    # A function that takes a string and return the string unmodified.
    # Used to test if safe_eval() rejects calling functions
    def disabled_function(string):
        return string

    # A function that takes a string and return the string unmodified.
    # Used to test if safe_eval() accepts calling functions
    CALL_ENABLED.append(disabled_function.__name__)

    # Test the safe_eval function
    assert safe_eval('1') == 1
    assert safe_eval('1 + 2') == 3
    assert safe_eval('1 + 2 + 3') == 6
    assert safe_eval('-1') == -1
    assert safe_eval('1 + -2') == -1
    assert safe_eval('1 + -2 + 3') == 2
    assert safe_eval('-1 + -2') == -3


# Generated at 2022-06-13 15:36:34.057962
# Unit test for function safe_eval

# Generated at 2022-06-13 15:36:43.589754
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('1 + 3') == 4
    assert safe_eval('1 + 3') == 4
    assert safe_eval('1 + 3', dict(a=False, b=True)) == 4
    assert safe_eval('1 + 3', dict(a=False, b=True)) == 4
    assert safe_eval('1 + 3') == 4
    assert safe_eval('1 + 3') == 4
    assert safe_eval('a and b', dict(a=False, b=True)) == False
    assert safe_eval('a or b', dict(a=False, b=True)) == True
    assert safe_eval('a and not b', dict(a=False, b=True)) == False
    assert safe_eval('a or not b', dict(a=False, b=True)) == False

# Generated at 2022-06-13 15:36:55.185056
# Unit test for function safe_eval

# Generated at 2022-06-13 15:37:03.709522
# Unit test for function safe_eval
def test_safe_eval():
    """Unit test for function safe_eval"""
    import ast

    from ansible.module_utils.common.text.converters import container_to_text

    CALL_ENABLED = set(
        (
            'max',
            'min',
            'zip',
        )
    )

    safemode = {'expr': None, 'success': None, 'exception': None}

    def test_expr(expr, success=None, exception=None):
        safemode['expr'] = expr
        safemode['exception'] = exception
        safemode['success'] = success

    import sys

# Generated at 2022-06-13 15:37:12.357659
# Unit test for function safe_eval
def test_safe_eval():
    # test safe_eval with an empty string
    res = safe_eval('')
    assert res == ''

    # test safe_eval with an integer
    res = safe_eval('42')
    assert res == 42

    # test safe_eval with a float
    res = safe_eval('3.14')
    assert res == 3.14

    # test safe_eval with a string
    res = safe_eval('"foo"')
    assert res == 'foo'

    # test safe_eval with a boolean
    res = safe_eval('True')
    assert res is True

    res = safe_eval('False')
    assert res is False

    # test safe_eval with a list
    res = safe_eval('[1, 2, 3]')
    assert res == [1, 2, 3]

    # test safe_eval

# Generated at 2022-06-13 15:37:21.531467
# Unit test for function safe_eval
def test_safe_eval():
    our_eval = safe_eval

    #CHECK FOR EXCEPTION
    try:
        # Evaluate a "safe" expression
        our_eval("1+1")
    except Exception:
        assert False

    #CHECK FOR EXCEPTION
    try:
        # Evaluate a "unsafe" expression
        our_eval("open('/tmp/foo')")
    except Exception:
        assert True

    #CHECK FOR EXCEPTION
    try:
        # Evaluate a "unsafe" expression
        our_eval("__import__('sys')")
    except Exception:
        assert True

    #CHECK FOR EXCEPTION
    try:
        # Evaluate a "unsafe" expression
        our_eval("execfile('/tmp/foo')")
    except Exception:
        assert True

    #CHECK FOR EXCEPTION

# Generated at 2022-06-13 15:38:01.659358
# Unit test for function safe_eval