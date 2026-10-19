

# Generated at 2022-06-14 17:49:21.775315
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    interpreter = JSInterpreter("var func = function(x,y){var t=0;var u='';u=u+y;return u;} func(1,2);")
    fct = interpreter.build_function(["x","y"], "var t=0;var u='';u=u+y;return u;")
    assert fct is not None
    assert fct((1,2)) == "2"


# Generated at 2022-06-14 17:49:30.254618
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    js_code = open('test_JSInterpreter_extract_object.js').read()
    test_object_name = 'test_object'
    _FUNC_NAME_RE = r'''(?:[a-zA-Z$0-9]+|"[a-zA-Z$0-9]+"|'[a-zA-Z$0-9]+')'''
    obj = {}

# Generated at 2022-06-14 17:49:40.729797
# Unit test for method interpret_expression of class JSInterpreter

# Generated at 2022-06-14 17:49:47.566763
# Unit test for method interpret_statement of class JSInterpreter
def test_JSInterpreter_interpret_statement():
    js = """
        var f = {
            a: function() {
                return 5;
            }
        };
        var g = function() {
            return f.a() + 2;
        };
    """
    i = JSInterpreter(js)
    f = i.extract_function('g')
    assert f() == 7


if __name__ == '__main__':
    import sys
    test_JSInterpreter_interpret_statement()
    print('Passed')
    sys.exit(0)

# Generated at 2022-06-14 17:49:56.377026
# Unit test for method extract_object of class JSInterpreter

# Generated at 2022-06-14 17:50:09.795530
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    import unittest
    # Test for function ab
    def f(code):
        interpreter = JSInterpreter('')
        f = interpreter.build_function(['a', 'b'], code)
        return f
    # Test case
    class TestJSInterpreterBuildFunction(unittest.TestCase):
        def test_ab(self):
            self.assertEqual(f('a + b')([1, 2]), 3)
            self.assertEqual(f('a - b')([1, 2]), -1)
            self.assertEqual(f('a * b')([1, 2]), 2)
            self.assertEqual(f('a / b')([1, 2]), 0.5)
            self.assertEqual(f('a % b')([1, 2]), 1)


# Generated at 2022-06-14 17:50:17.681674
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    # YouTubePlayer's functions are provided in an external JavaScript file
    # saved as ./m.js
    # Load function definitions from file './m.js' into JSInterpreter
    m_js = open('./m.js', 'r').read()
    m = JSInterpreter(m_js)
    # Call function 'AA' in YouTubePlayer with arguments (3, 4)
    #    m.call_function('AA', 3, 4)
    # It should return 32
    assert m.call_function('AA', 3, 4) == 32

# Generated at 2022-06-14 17:50:23.035712
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    extractor_code = r'''var a = {b: function(p){var a = p.split('');a.reverse();return a.join('')}};'''
    jsinterpreter = JSInterpreter(extractor_code)
    obj_result = jsinterpreter.extract_object(objname='a')
    assert obj_result == {'b': lambda x: ''.join(x[0][::-1])}

# Generated at 2022-06-14 17:50:35.396045
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    code = 'var a = { b: function(p) { return p } };'
    js_interpreter = JSInterpreter(code)
    actual = js_interpreter.extract_object('a')
    expected = {'b': lambda x: x}
    assert actual == expected

    code = 'var a = { b: function(p) { return p }, c: function(p, q) { return p + q } };'
    js_interpreter = JSInterpreter(code)
    actual = js_interpreter.extract_object('a')
    expected = {'b': lambda x: x, 'c': lambda x, y: x + y}
    assert actual == expected


# Generated at 2022-06-14 17:50:47.969623
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    jsi = JSInterpreter('')
    assert jsi.interpret_expression('[1,2]', {}, 100) == [1, 2]
    assert jsi.interpret_expression('1+1', {}, 100) == 2
    assert jsi.interpret_expression('1-1', {}, 100) == 0
    assert jsi.interpret_expression('1*1', {}, 100) == 1
    assert jsi.interpret_expression('1/1', {}, 100) == 1
    assert jsi.interpret_expression('1%1', {}, 100) == 0
    assert jsi.interpret_expression('1&1', {}, 100) == 1
    assert jsi.interpret_expression('1|1', {}, 100) == 1
    assert jsi.interpret_expression('1^1', {}, 100) == 0
   

# Generated at 2022-06-14 17:51:14.416547
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    js_code = '''
        var a = "Hello ";
        var c = "world";
        var e = function(b) {
            var d = "dlrow";
            return a + b + d + c;
        };
        var g = function() {
            return e("o");
        };
        var i = function() {
            var j = "o";
            return e(j);
        };
    '''
    js = JSInterpreter(js_code)
    # Basic expression with multiple variables
    assert js.call_function("e", "o") == "Hello odlrowworld"
    # Multiple operators
    assert js.call_function("i") == "Hello odlrowworld"
    # Function call with no parameters
    assert js.call_function("g") == "Hello odlrowworld"

# Generated at 2022-06-14 17:51:24.486840
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    code = '''var y = 1;
var z = y;
function obj(x, y) {
    this.x = x;
    this.y = function(z) {
        return [this.x, this.y, z];
    };
}
obj.prototype.test = function(test_arg) {
    var d = "5";
    var e = "6";
    var f = "7";
    var g = "8";
    return this.y(test_arg) + [d, e, f, g, arguments];
};'''

    jsi = JSInterpreter(code, {'x': 'abc', 'y': {'z': 3}, 'null': None})

    assert jsi.interpret_expression('x', {}) == 'abc'

# Generated at 2022-06-14 17:51:27.859444
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    js_interpreter = JSInterpreter("")
    local_vars = {"a": 0, "b": 0}
    code = "a = 1; b = 2;"
    js_interpreter.build_function([], code)([])
    assert local_vars == {"a": 1, "b": 2}


# Generated at 2022-06-14 17:51:36.474898
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    source = '''function() {
        var obj = {
            "a": "hello",
            "b": "world",
            "c": function(str) {
                return str + " " + this.b;
            }
        };
        var list = ["1", "2", obj.a, obj.a + " " + obj.b];
        var x = obj.c;
        var res = x("good");
        return list[2] + " " + list[3] + ", " + res;
    }'''
    interp = JSInterpreter(source)
    f = interp.build_function([], source)
    res = f()
    assert res == 'hello hello world, good world'

    # Now test deprecated method

# Generated at 2022-06-14 17:51:43.985467
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    #test case 1
    js_interpreter = JSInterpreter('')
    argnames = ['a', 'b']
    code = 'return a + b'
    func = js_interpreter.build_function(argnames, code)
    assert func(1, 2) == 3
    #test case 2
    code = 'return a + b; return a - b'
    func = js_interpreter.build_function(argnames, code)
    assert func(1, 2) == 3
    #test case 3
    code = '''
    var c = a + b;
    c = c*c;
    return a - b;
    '''
    func = js_interpreter.build_function(argnames, code)
    assert func(1, 2) == -1
    #test case 4

# Generated at 2022-06-14 17:51:49.825780
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    js = JSInterpreter(None)
    local_vars = {}
    def assert_expr(s, e):
        assert js.interpret_expression(s, local_vars) == e

    assert_expr('1', 1)
    assert_expr('1+1', 2)
    assert_expr('3-2', 1)
    assert_expr('(1+1)', 2)
    assert_expr('(1*2)', 2)
    assert_expr('(1*-1)', -1)
    assert_expr('"1+2"', '1+2')
    assert_expr('"1+2"+"3-4"', '1+23-4')
    assert_expr('"1+1"+1+1', '11')
    # The following case is not defined yet
    #

# Generated at 2022-06-14 17:52:01.926217
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    jsinterpreter = JSInterpreter('')
    assert jsinterpreter.build_function(
            [], 'return 42;')([]) == 42
    assert jsinterpreter.build_function(
            [], 'var x = 1; return x;')([]) == 1
    assert jsinterpreter.build_function(
            [], 'var x = 1; return x;')([]) == 1
    assert jsinterpreter.build_function(
            ['x'], 'return x;')([42]) == 42
    assert jsinterpreter.build_function(
            ['x'], 'return x + 1;')([41]) == 42
    assert jsinterpreter.build_function(
            ['x', 'y'], 'return x + y;')([20, 22]) == 42



# Generated at 2022-06-14 17:52:11.995798
# Unit test for method interpret_expression of class JSInterpreter

# Generated at 2022-06-14 17:52:17.727729
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    test_code = """
        var test = {
          'a': 'b',
          'a.b': 'c',
          'a1': [
            'b',
            'c'
          ],
          'a2': {
            'b': 'c'
          },
          'abc': function(arg1, arg2, arg3) {
            var test1 = arg1;
            var test2 = arg2;
            var test3 = arg3;
          },
          'def': function() {
            return 'def';
          }
        };
    """
    js_interpreter = JSInterpreter(test_code)
    assert 'b' == js_interpreter.interpret_expression("test['a']", {'test': {'a': 'b'}})
    assert 'c' == js_

# Generated at 2022-06-14 17:52:29.709724
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    js_interpreter = JSInterpreter('')
    test_function_names = [
        'test_function_1',
        'test_function_2',
        'test_function_3'
    ]
    test_function_codes = [
        'a + b',
        'a, b',
        'a; b; return a + b'
    ]

    def test_function(fname, fcode):
        argnames = [
            'a',
            'b'
        ]
        f = js_interpreter.build_function(argnames, fcode)
        assert f([4, 2]) == eval(fcode)

    for test_function_name, test_function_code in zip(
            test_function_names, test_function_codes):
        yield test_function, test_function

# Generated at 2022-06-14 17:52:59.239518
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    code = 'var f = function(a, b) {return a + b;}'
    v = JSInterpreter(code).interpret_expression('f(1, 2)', {})
    assert v == 3

    code = 'var f = function(a, b) {return a + b;}'
    v = JSInterpreter(code).interpret_expression('f(1, b)', {'b': 2})
    assert v == 3

    code = 'var f = function(a, b) {return a + b;}'
    v = JSInterpreter(code).interpret_expression('f()', {})
    assert v == None

    code = 'var f = function(a, b) {return a + b;}'
    v = JSInterpreter(code).interpret_expression('func()', {})
    assert v == None

# Generated at 2022-06-14 17:53:13.160790
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    def check_JS_Inpreter(js_expression, expected_result, local_variable={}, objects={}):
        js_interpreter = JSInterpreter("", objects)
        assert isinstance(js_interpreter, JSInterpreter)
        result = js_interpreter.interpret_expression(js_expression, local_variable)
        assert expected_result == result

    check_JS_Inpreter("a + b", 2, {'a': 1, 'b': 1})
    check_JS_Inpreter("a - b  ", 2, {'a': 3, 'b': 1})
    check_JS_Inpreter("a * b", 2, {'a': 2, 'b': 1})
    check_JS_Inpreter("a / b", 2, {'a': 4, 'b': 2})

# Generated at 2022-06-14 17:53:25.095320
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    # Test object instantiating
    js_code = """
        var obj = {
            'test': function(test1, test2) {
                return test1 + test2;
            }
        };
        """
    interpreter = JSInterpreter(js_code)
    res = interpreter.interpret_expression("obj.test(1, 2)", {})
    assert res == 3

    # Test function extracting
    js_code = """
        function test(test1, test2) {
            test3 = test1 + test2;
            return test3;
        }
        """
    interpreter = JSInterpreter(js_code)
    res = interpreter.interpret_expression("test(2, 3)", {})
    assert res == 5

    # Test function extracting

# Generated at 2022-06-14 17:53:36.284710
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    objects = {
        'foo': {
            'bar': 123
        },
        'qaz': {
            'pop': [1, 2, 3].pop,
            'join': '*'.join
        }
    }
    js_interpreter = JSInterpreter('', objects=objects)
    assert js_interpreter.interpret_expression('foo["bar"]', {}) == 123
    assert js_interpreter.interpret_expression('foo[\'bar\']', {}) == 123
    assert js_interpreter.interpret_expression('foo[bar]', {'bar': 'bar'}) == 123
    assert js_interpreter.interpret_expression(
        'qaz.pop()', {}) == 3

# Generated at 2022-06-14 17:53:48.280600
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    js_code = '''
        function func(a, b) {
            var result;
            var c = a + 1;
            if (c > 2) {
                if (b === 'hello') {
                    result = a + b + c;
                } else {
                    result = a + b + c - 1;
                }
            } else {
                result = a + b + c + 1;
            }
            return result;
        }
        '''
    js_interpreter = JSInterpreter(js_code)
    assert js_interpreter.call_function('func', 1, 'hello') == '1hellod'
    assert js_interpreter.call_function('func', 1, 'hello2') == '1hello2d'

# Generated at 2022-06-14 17:53:58.113256
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    js_obj_1 = {
        "substr": lambda args: args[0][args[1]:args[2]],
        "substring": lambda args: args[0][args[1]:args[2]],
        "split": lambda args: list(args[0]),
        "join": lambda args: args[0].join(args[1]),
        "length": lambda args: len(args[0]),
        "reverse": lambda args: args[0][::-1],
        "slice": lambda args: args[0][args[1]:]
    }

# Generated at 2022-06-14 17:54:08.214479
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    jsinterp = JSInterpreter("var b = \"this_is_a_string\";")
    assert jsinterp.interpret_expression("b", {}) == "this_is_a_string"

    jsinterp = JSInterpreter("")
    assert jsinterp.interpret_expression("1+2", {}) == 3

    jsinterp = JSInterpreter("")
    assert jsinterp.interpret_expression("1+2*3", {}) == 7

    jsinterp = JSInterpreter("")
    assert jsinterp.interpret_expression("[1,2,3]", {}) == [1,2,3]

    jsinterp = JSInterpreter("")
    assert jsinterp.interpret_expression("1, [1, 2, 3][1]", {}) == 2


# Generated at 2022-06-14 17:54:17.718270
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    def test_func(interpreter, funcname, expected_argnames, expected_code,
                  expected_func):
        func = interpreter.build_function(expected_argnames, expected_code)
        assert func is not None
        assert func == expected_func
        return func

    # test function f1 with one argument
    interpreter = JSInterpreter('function f1(arg1) { return arg1; }', {})
    func = test_func(interpreter, 'f1', ['arg1'], 'return arg1',
                     lambda arg1: arg1)
    assert func('x') == 'x'

    # test function f2 with three arguments
    interpreter = JSInterpreter('function f2(arg1, arg2, arg3) { return arg1 + arg2 + arg3; }', {})
    func = test

# Generated at 2022-06-14 17:54:30.516684
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    js_interpreter = JSInterpreter("foo = 'bar'")
    assert js_interpreter.interpret_expression("foo", dict()) == "bar"
    assert js_interpreter.interpret_expression("'ba'+'r'", dict()) == "bar"
    assert js_interpreter.interpret_expression("'ba'+'r'+foo", dict()) == "barbar"
    assert js_interpreter.interpret_expression("foo+'bar'", dict()) == "barbar"


# Generated at 2022-06-14 17:54:42.523347
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    from .compat import compat_str
    from .extractor import gen_extractors
    extractors = gen_extractors()
    for ie in extractors:
        if compat_str(type(ie)) == 'youtube_dl.extractor.youtube.YoutubeIE':
            break

    t = JSInterpreter(code = ie._parse_config)
    test_func_name = 'reverse'
    argnames = ('a',)
    code = '{a.reverse();return a}'
    resf = t.build_function(argnames, code)

    assert(resf(('abc',)) == 'cba')

if __name__ == '__main__':
    test_JSInterpreter_build_function()

# Generated at 2022-06-14 17:55:22.344535
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    code = 'function test(a, b, c){return a*b+c+d}'
    func = JSInterpreter(code).extract_function('test')
    assert func((1, 2, 3)) == 13

if __name__ == '__main__':
    test_JSInterpreter_interpret_expression()

# Generated at 2022-06-14 17:55:32.444881
# Unit test for method build_function of class JSInterpreter

# Generated at 2022-06-14 17:55:36.167517
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    js_interpreter = JSInterpreter('')
    js_function = js_interpreter.build_function(['a', 'b'], 'return a * b;')
    assert js_function([3, 4]) == 12


# Generated at 2022-06-14 17:55:47.645083
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    # Test for local variables
    for stmt in ['x', 'y', 'a', 'b', 'c']:
        assert JSInterpreter.interpret_expression(stmt, {'x': 1, 'y': 2, 'a': 3, 'b': 4, 'c': 5}) == eval(stmt)
    # Test for numbers (decimal, hexadecimal, octal, binary)
    for stmt in ['1', '123', '0x123', '017', '0b111']:
        assert JSInterpreter.interpret_expression(stmt, {}) == eval(stmt)
    # Test for strings
    for stmt in ['"hello"', "'world'"]:
        assert JSInterpreter.interpret_expression(stmt, {}) == eval(stmt)
    # Test for arrays

# Generated at 2022-06-14 17:55:57.280507
# Unit test for method build_function of class JSInterpreter

# Generated at 2022-06-14 17:56:02.256467
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    js_interpreter = JSInterpreter("function add(a,b) { return a+b; }")
    f = js_interpreter.build_function(['a', 'b'], 'return a+b;')
    assert f([40, 2]) == 42

# Generated at 2022-06-14 17:56:10.660105
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    local_vars = {'a': [1, 2, 3, 4], 'b': 4, 'c': 5, 'f': 4, 'g':5, 'd': 0.1, 'i': 'bob'}
    js = JSInterpreter('', local_vars)


# Generated at 2022-06-14 17:56:18.785604
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    code_1 = """function funcName(arg1, arg2, arg3) {
  var e = parseInt(arg1, 0);
  var g = arg2 % 10;
  var b;
  arg3 = arg3;
  b = 8 === g ? arg2 : arg2 ^ e;
return g != 8 ? b ^ e : b;}"""
    js = JSInterpreter(code_1)
    f = js.build_function(['arg1', 'arg2', 'arg3'], "var e = parseInt(arg1, 0); var g = arg2 % 10; var b; arg3 = arg3; b = 8 === g ? arg2 : arg2 ^ e; return g != 8 ? b ^ e : b;")
    assert f([4, 15, "a"]) == 11

# Generated at 2022-06-14 17:56:24.646524
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    ja = JSInterpreter('f1=function(a,b){a+b}')
    f1 = ja.build_function(['a','b'], 'a+b')
    assert(f1([1, 2]) == 3)


# Generated at 2022-06-14 17:56:33.966903
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    interpreter = JSInterpreter('')
    local_var = {}

    # Test for basic operation
    assert interpreter.interpret_expression('12', local_var, 1000) == 12
    assert interpreter.interpret_expression('2 + 3', local_var, 1000) == 5
    assert interpreter.interpret_expression('4 - 2', local_var, 1000) == 2
    assert interpreter.interpret_expression('3 * 2', local_var, 1000) == 6
    assert interpreter.interpret_expression('2 / 3', local_var, 1000) == 2 / 3
    assert interpreter.interpret_expression('2 % 3', local_var, 1000) == 2 % 3
    assert interpreter.interpret_expression('2 << 3', local_var, 1000) == 16
    assert interpreter.interpret_expression('2 >> 3', local_var, 1000) == 0

# Generated at 2022-06-14 17:57:58.932271
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    js_code = """
        var a = {
            'splitCode': function (code) {
                return code.split("_");
            },
            'reverse': function (arr) {
                arr.reverse();
            }
        }
        var array = "abcd_efgh".split("_")
        a.reverse(array)
    """
    js = JSInterpreter(js_code)
    res = js.interpret_expression("a.splitCode('abcd_efgh')", {})
    assert(res == ['abcd', 'efgh'])
    res = js.interpret_expression("a.reverse(array)", {})
    assert(res == ['efgh', 'abcd'])


if __name__ == '__main__':
    test_JSInterpreter_interpret_expression()