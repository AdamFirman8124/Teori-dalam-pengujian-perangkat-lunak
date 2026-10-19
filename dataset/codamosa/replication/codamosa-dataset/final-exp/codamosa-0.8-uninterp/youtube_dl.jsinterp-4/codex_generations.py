

# Generated at 2022-06-14 17:48:53.814948
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    interpreter = JSInterpreter('')
    assert interpreter.interpret_expression('1', {}) == 1
    assert interpreter.interpret_expression('+1', {}) == 1
    assert interpreter.interpret_expression('-1', {}) == -1
    assert interpreter.interpret_expression('-1 + 1', {}) == 0
    assert interpreter.interpret_expression('1 - 1', {}) == 0
    assert interpreter.interpret_expression('1 * 1', {}) == 1
    assert interpreter.interpret_expression('1 / 1', {}) == 1
    assert interpreter.interpret_expression('1 % 1', {}) == 0
    assert interpreter.interpret_expression('1 & 1', {}) == 1
    assert interpreter.interpret_expression('1 | 1', {}) == 1
    assert interpreter.interpret_expression('1 ^ 1', {}) == 0
    assert interpreter

# Generated at 2022-06-14 17:49:00.263341
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    jsi = JSInterpreter(
"""
                function test1 (a, b) {
                    return test2(a, b);
                }
                function test2 (a, b) {
                    return a + b;
              }""")
    assert jsi.extract_function('test2')((1, 2)) == 3
    assert jsi.call_function('test1', 1, 2) == 3


# Generated at 2022-06-14 17:49:10.253206
# Unit test for method interpret_statement of class JSInterpreter
def test_JSInterpreter_interpret_statement():
    jsint = JSInterpreter("""
        function function2(argument) {
            return argument;
        }
        function function1(argument) {
            return function2(argument);
        }
        function function3(argument) {
            return function2(2);
        }
        """)
    assert(jsint.call_function("function1", 1234) == 1234)
    assert(jsint.call_function("function3", 1234) == 2)

test_JSInterpreter_interpret_statement()

# Generated at 2022-06-14 17:49:17.111201
# Unit test for method interpret_statement of class JSInterpreter
def test_JSInterpreter_interpret_statement():
    code = js_to_json('''
        var b = a[0];
        var c = d + f[0];
        var l = k.length;
        var m = k[i];
        var g = h + d;
        f += 1;
        d[0] = d[1];
        var a = "test"
        return function(p,q) {}
        return "test";
    ''')
    interpreter = JSInterpreter(code)
    a = [2]
    f = [1]
    d = [3, 2]
    k = [1, 2, 3]
    local_vars = {'a': a, 'f': f, 'd': d, 'k': k, 'i': 0, 'h': 1}

# Generated at 2022-06-14 17:49:30.586027
# Unit test for method interpret_statement of class JSInterpreter

# Generated at 2022-06-14 17:49:42.345030
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    js = JSInterpreter(None)
    f = js.build_function(["a", "b", "c"], "return a+b+c;")
    assert f([1, 2, 3]) == 6
    assert f([1, 2, "foo"]) == "3foo"
    f = js.build_function(["a", "b", "c"], "a=b+c; return a+b+c;")
    assert f([1, 2, 3]) == 12
    f = js.build_function(["a", "b", "c"], "var d;d=b;a=b+c; return d;")
    assert f([1, 2, 3]) == 2


# Generated at 2022-06-14 17:49:52.492255
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    # Test Case 1
    code = """function f(a,b){a=a>>>0;var c=0;for(var d=0;d<b;d++){c+=(a&1)<<d;a>>=1}return c}"""
    assert JSInterpreter.build_function(['a', 'b'], code.split("{")[1].split("}")[0])([4, 5]) == 16

    # Test Case 2

# Generated at 2022-06-14 17:50:04.270858
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    js_interpreter = JSInterpreter('var a = 1;')
    assert js_interpreter.interpret_expression('a', {'a': 2}) == 2
    assert js_interpreter.interpret_expression('(a)', {'a': 3}) == 3
    assert js_interpreter.interpret_expression('(89)', {}) == 89
    assert js_interpreter.interpret_expression('1+1', {}) == 2
    assert js_interpreter.interpret_expression('1 + 1', {}) == 2
    assert js_interpreter.interpret_expression('1 +1', {}) == 2
    assert js_interpreter.interpret_expression('a + 1', {'a': 10}) == 11

# Generated at 2022-06-14 17:50:14.276422
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    def assert_interpret_expression(js, var_dict, expected_value):
        interp = JSInterpreter(code=js, objects=var_dict)
        value = interp.interpret_expression(js, var_dict)
        assert value == expected_value

    var_dict = {'e': '%71%7A%68%61%63%6B%65%64%62%79%77%72%6C%64%3D%3D',
                'a': 'poiuytre1234!@#$',
                'd': '1,2,3,4',
                'b': 123,
                'c': 'qwerty',
                }

    assert_interpret_expression('1+1', var_dict, 2)
    assert_interpret_expression('a+1', var_dict, 124)


# Generated at 2022-06-14 17:50:25.212905
# Unit test for method interpret_expression of class JSInterpreter

# Generated at 2022-06-14 17:50:56.860314
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    def test(func_name, args, code, expected_result, expected_local_vars):
        actual_result = JSInterpreter('function {}() {{ {}; }}'.format(func_name, code)).build_function(args, code)(args)
        assert actual_result == expected_result
    test('d', ['a', 'b', 'c'], 'a = b + c; e = a/d; return e;', None, {'a': None, 'b': None, 'c': None, 'd': ['a', 'b', 'c'], 'e': None})

# Generated at 2022-06-14 17:51:07.425884
# Unit test for method extract_object of class JSInterpreter

# Generated at 2022-06-14 17:51:13.801831
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    J = JSInterpreter('''
        var a = {
            b: 12,
            c: function() { return 3; },
            e: function(a){ return a-1; }
        }
    ''')
    expected = {'b': 12, 'c' : lambda: 3, 'e' : lambda a: a-1}
    assert J.extract_object('a') == expected


# Generated at 2022-06-14 17:51:26.046477
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    import pytest

    # Test for 'var' statement
    assert JSInterpreter('var a = 4').interpret_expression('a', {}) == 4

    # Test for 'return' statement
    assert JSInterpreter('return 4').interpret_expression('', {}) is None

    # Test for expression
    assert JSInterpreter('x = 3').interpret_expression('3', {}) == 3
    assert JSInterpreter('x = 3').interpret_expression('x', {}) == 3

    # Test for expression with '+', '-' and '*'
    assert JSInterpreter('x = "5"').interpret_expression('x+2', {}) == 7
    assert JSInterpreter('x = "5"').interpret_expression('x*2', {}) == 10
    assert JSInterpreter('x = "5"').interpret_

# Generated at 2022-06-14 17:51:29.917066
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    test_code = """
    var test_JSInterpreter_call_function = function (a, b) {
        var c = a + "Hi " + b;
        return c;
    }
    """
    jsi = JSInterpreter(test_code)
    assert jsi.call_function('test_JSInterpreter_call_function', 'hello ', 'world') == 'hello Hi world'


# Generated at 2022-06-14 17:51:36.357988
# Unit test for method extract_object of class JSInterpreter

# Generated at 2022-06-14 17:51:48.567290
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    def _test(code, argnames, args, expected):
        f = JSInterpreter(code).build_function(argnames, code)
        return f(args) == expected
    assert _test(
        'var a = {};a.b = function() {};',
        [],
        [],
        None)
    assert _test(
        'function xxx(a,b){return a+b;}',
        ['a', 'b'],
        [1, 2],
        3)
    assert _test(
        'function xxx(a,b){return a+b;};',
        ['a', 'b'],
        [1, 2],
        3)

# Generated at 2022-06-14 17:51:56.009984
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    func_call = JSInterpreter('''
    function f(x, y) {
        return x+y;
    }
    ''')
    result = func_call.interpret_expression('f(1, 2)')
    assert result == 3

    func_call = JSInterpreter('''
    function g(x, y, z) {
        return x+y+z;
    }

    function f(x, y) {
        return g(x, y, 1);
    }
    ''')
    result = func_call.interpret_expression('f(1, 2)')
    assert result == 4

    func_call = JSInterpreter('''
    function f(x, y) {
        var a = x+y;
        return a;
    }
    ''')


# Generated at 2022-06-14 17:52:07.377974
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    test_code = """\
    test_func = function() {
        return true;
    };
    test_obj = {
        a: function() {
            return 'a';
        },
        b: function() {
            return 'b';
        }
    };
    """
    test_obj = JSInterpreter(test_code)
    result = test_obj.extract_object('test_obj')
    assert sorted(result) == sorted(['a', 'b'])
    assert result['a']() == 'a'
    assert result['b']() == 'b'

if __name__ == '__main__':
    test_JSInterpreter_extract_object()

# Generated at 2022-06-14 17:52:16.562955
# Unit test for method interpret_statement of class JSInterpreter
def test_JSInterpreter_interpret_statement():
    jsi = JSInterpreter('a = 1; b = 2')
    res, abort = jsi.interpret_statement('a = 1', {}, 100)
    assert res == 1
    assert not abort
    res, abort = jsi.interpret_statement('b = 2', {}, 100)
    assert res == 2
    assert not abort
    res, abort = jsi.interpret_statement('a = b', {'a': 3}, 100)
    assert res == 2
    assert not abort
    res, abort = jsi.interpret_statement('return 1 + 2', {}, 100)
    assert res == 3
    assert abort



# Generated at 2022-06-14 17:53:27.849914
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    interpreter = JSInterpreter('')
    local_vars = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Generated at 2022-06-14 17:53:34.387759
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    js_code = """
        var obj = {a: function() {}, b: function() {}};
    """
    interpreter = JSInterpreter(js_code)
    assert 'a' in interpreter.extract_object('obj')
    assert 'b' in interpreter.extract_object('obj')
    assert 'c' not in interpreter.extract_object('obj')


# Generated at 2022-06-14 17:53:46.123198
# Unit test for method interpret_statement of class JSInterpreter
def test_JSInterpreter_interpret_statement():
    x, y, z = "x", "y", "z"
    objects = {"w": [x, y, z]}
    code = "var paella_IS_PLAYING_PROGRESS = true;"
    jsinterpreter = JSInterpreter(code, objects)
    jsinterpreter.interpret_statement(code, {})
    assert jsinterpreter._objects["paella_IS_PLAYING_PROGRESS"] == True
    code = "var w = true"
    jsinterpreter.interpret_statement(code, {})
    assert jsinterpreter._objects["w"] == True
    code = "denc=String.fromCharCode(c^this._keyStr.charCodeAt(k++))"
    jsinterpreter._objects["String"] = {"fromCharCode": lambda c: unichr(c)}

# Generated at 2022-06-14 17:53:57.092607
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    the_js_code = '''
        var player = {
            onReady: function() {
                // do something
            },
            get: function() {
                // do something else
            },
        };
    '''
    js_interpreter = JSInterpreter(the_js_code)
    assert len(js_interpreter._objects) == 0
    obj_player = js_interpreter.extract_object('player')
    assert obj_player['onReady'] is not None
    assert obj_player['get'] is not None
    assert len(obj_player['onReady'].__code__.co_varnames) == 0
    assert len(obj_player['get'].__code__.co_varnames) == 0
    assert type(obj_player) == dict

# Generated at 2022-06-14 17:54:07.685661
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():

    js_interpreter = JSInterpreter('''
        var a = 10;
        var b = 24;
        var c = "abcd";
        var d = [1,2,3,4];
        var e = {a: 1, b: 2};
        var f = function hello(arg1){
            if ( arg1 > 90 ) {
                return "Likely to be spam";
            }
            return "Likely to be ham";
        };
        var g = {"a": "A", "b": "B"};
    ''')

    # Test: A basic expression
    assert js_interpreter.interpret_expression('a', {}) == 10
    assert js_interpreter.interpret_expression('a+b', {}) == 34

    # Test: Support for string comparisons and operators
    assert js_

# Generated at 2022-06-14 17:54:19.278304
# Unit test for method interpret_statement of class JSInterpreter
def test_JSInterpreter_interpret_statement():
    js_interpreter = JSInterpreter('')
    local_vars = {}
    # Test assign statement
    v, should_abort = js_interpreter.interpret_statement('var a = b', local_vars)
    assert v is None
    assert not should_abort
    v, should_abort = js_interpreter.interpret_statement('b = 1', local_vars)
    assert local_vars['a'] == 1
    assert not should_abort
    local_vars['c'] = 1
    v, should_abort = js_interpreter.interpret_statement('a += c', local_vars)
    assert local_vars['a'] == 2
    assert not should_abort
    # Test return statement

# Generated at 2022-06-14 17:54:24.545682
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    interpreter = JSInterpreter('')
    f = interpreter.build_function(('a', 'b', 'c', 'd', 'e'), 'a=b+1;c=d+4;return a+c')
    assert f((1, 2, 3, 4, 5)) == 7

# Generated at 2022-06-14 17:54:36.783509
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    js = JSInterpreter("")
    assert js.interpret_expression("1+1", {}) == 2
    assert js.interpret_expression("2-1", {}) == 1
    assert js.interpret_expression("'a'+'b'", {}) == "ab"
    assert js.interpret_expression("'a'+3", {}) == "a3"
    assert js.interpret_expression("2-1", {}) == 1
    assert js.interpret_expression("'a'.toUpperCase()", {}) == "A"
    assert js.interpret_expression("'a'.charCodeAt(0)", {}) == 97
    assert js.interpret_expression("String.fromCharCode(65)", {}) == "A"

# Generated at 2022-06-14 17:54:50.906753
# Unit test for method interpret_expression of class JSInterpreter

# Generated at 2022-06-14 17:54:58.552263
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    objects = JSInterpreter(code='''
var obj = {
    a: function (a){
        return a;
    },
    b: function (b){
        return b;
    },
    c: function (c){
        return c;
    }
}
    ''')._objects
    obj = objects['obj']
    assert obj['a']('a') == 'a'
    assert obj['b']('b') == 'b'
    assert obj['c']('c') == 'c'


# Generated at 2022-06-14 17:55:47.651940
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    codec = """
        function foo(a, b, c) {
            var d = 1;
            d = a / c;
            return a * b * d;
        }
        """
    def test_foo(args):
        assert len(args) == 3
        return args[0] * args[1] * (args[0] / args[2])
    resf = JSInterpreter(codec).build_function(['a', 'b', 'c'], 'var d = 1; d = a / c; return a * b * d;')
    assert resf(args=(7, 8, 2)) == test_foo(args=(7, 8, 2))
    assert resf(args=(1, 2, 3)) == test_foo(args=(1, 2, 3))

# Generated at 2022-06-14 17:55:49.799754
# Unit test for method interpret_statement of class JSInterpreter
def test_JSInterpreter_interpret_statement():
    interp = JSInterpreter(None)
    res, abort = interp.interpret_statement(
        'var f = function(){}; return f();', {})
    assert res == {} and abort == True



# Generated at 2022-06-14 17:55:56.287740
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    assert JSInterpreter('{}').interpret_expression('1+1', {}, 0) == 2
    assert JSInterpreter('{}').interpret_expression(
        '"hello " + "world"', {}, 0) == 'hello world'
    assert JSInterpreter('{}').interpret_expression(
        ' "  " .charCodeAt(0) .toString(16)', {}, 0) == '20'
    assert JSInterpreter('{}').interpret_expression(
        '"abc".slice(2)', {}, 0) == 'c'
    assert JSInterpreter('{}').interpret_expression('[1,2,3].length', {}, 0) == 3

# Generated at 2022-06-14 17:56:07.505685
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():

    # Test with simple arithmetic expressions
    jsi = JSInterpreter('')
    jsvals = [("1 + 1", 2), ("3 * 1", 3), ("2 - 3", -1), ("2.0 / 3", 2.0/3), ("5 % 9", 5), ("1 ^ 1", 0), ("1 | 1", 1), ("4 >> 1", 2), ("4 << 1", 8), ("1 | 2 & 3 ^ 4 + 5 - 6", 3)]
    for expr, val in jsvals:
        print("Test expression %s" % expr)
        assert jsi.interpret_expression(expr, dict()) == val

    # Test with expressions that use variables
    jsvals = [("a + b", 4), ("c ^ d", 0), ("c & d", 16), ("e << b", 8192), ("f >> b", 2)]

# Generated at 2022-06-14 17:56:14.020371
# Unit test for method interpret_statement of class JSInterpreter
def test_JSInterpreter_interpret_statement():
    # case 1: basic expression
    code = 'var a = 1 + 2 * 3;'
    interpreter = JSInterpreter(code)
    local_vars = {'a': 0}
    v, should_abort = interpreter.interpret_statement(code, local_vars)
    print(v)
    assert v == 7

    # case 2: statement with function call
    code = 'var a = __D(1);'
    interpreter = JSInterpreter(code)
    def __D(args):
        assert args == (1,)
        return 2
    interpreter._functions['__D'] = __D
    local_vars = {'a': 0}
    v, should_abort = interpreter.interpret_statement(code, local_vars)
    print(v)
    assert v == 2
    assert local

# Generated at 2022-06-14 17:56:25.925447
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    js_code = '''\
        var test = a + b;
        test -= c;
        var d = test * e;
        var f = "test " + d;
        var g = d + ' testing';
        var h = d.toString();
        var i = d.testing('test');
        var j = d[i];
        var k = d[i + 1];
        var l = d.length;
        d.reverse();
        return d.join(',');
    '''
    interpreter = JSInterpreter(js_code)
    result = interpreter.interpret_expression(
        js_code, {'a': 1, 'b': 3, 'c': 2, 'e': 5})
    assert result == '3,2,1,0'

# Generated at 2022-06-14 17:56:34.613249
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    code = r"""
        var a = "abcdefghijklmnopqrstuvwxyz";
        var b = function(x) {
            return x - 4;
        };
        var c = function(x) {
            return function(y) {
                return x + y;
            }
        };
        var d = {
            'a': 'b',
            'c': 'd'
        };
    """

    js = JSInterpreter(code)

    assert js.interpret_expression('5', {}) == 5
    assert js.interpret_expression('a', {}) == 'abcdefghijklmnopqrstuvwxyz'
    assert js.interpret_expression('b(8)', {}) == 4
    assert js.interpret_expression('c(9)(32)', {}) == 41

# Generated at 2022-06-14 17:56:43.942052
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    class TestObject(object):
        def __init__(self):
            self.a = 1
            self.b = 2

        def test_method(self):
            return self.a + self.b

    code = '''
    function test_method(){
        return a + b;
    }
    test_obj = {
        'test_method': test_method
    };
    '''
    interpreter = JSInterpreter(code)
    res = interpreter.call_function('test_method')
    assert res == 3

    code = '''
    function test_method(){
        return a + b;
    }

    function test_method2(){
        return a + test_method();
    }

    function test_method3(){
        return test_method() + b;
    }
    '''

# Generated at 2022-06-14 17:56:54.265814
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    js_interpreter = JSInterpreter("")
    f = js_interpreter.build_function(
        ['letters', 's'],
        'var out = ""; var i; for (i = 0; i < s.length; i = i + 2) {\
            out = out + letters.charAt(s.charCodeAt(i) - 97); } return out;'
    )
    assert f([
        'abcdefghijklmnopqrstuvwxyz',
        '0079ff2e2820293679ff2e2820293679ff2e2820293679ff2e2820293679ff2e28202'
    ]) == 'ybybybybybybybybybybybybybybybybybybybybybybybybyb'

# Generated at 2022-06-14 17:57:00.148649
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():

    interpreter = JSInterpreter("""
        var col = function (num, shift) {
            return (num >>> shift) & 0x3f;
        }
    """)

    assert interpreter.build_function(["num", "shift"], """
        return (num >>> shift) & 0x3f;
    """)([0x6A, 4]) == 0x6

# Generated at 2022-06-14 17:57:29.034534
# Unit test for method extract_object of class JSInterpreter

# Generated at 2022-06-14 17:57:39.029811
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    jsi = JSInterpreter('var a = 5;')
    assert jsi.interpret_expression('a', {}) == 5
    assert jsi.interpret_expression('a+1', {}) == 6
    assert jsi.interpret_expression('a + 1', {}) == 6
    assert jsi.interpret_expression('a - 1', {}) == 4
    assert jsi.interpret_expression('a * 1', {}) == 5
    assert jsi.interpret_expression('a / 1', {}) == 5
    assert jsi.interpret_expression('a % 1', {}) == 0
    assert jsi.interpret_expression('a ** 1', {}) == 5
    assert jsi.interpret_expression('a << 1', {}) == 10
    assert jsi.interpret_expression('a >> 1', {}) == 2

# Generated at 2022-06-14 17:57:43.213197
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    js_interpreter = JSInterpreter('')
    assert js_interpreter.interpret_expression('\'abc\'') == 'abc'
    assert js_interpreter.interpret_expression('1 + 2 + 3') == 6

# Generated at 2022-06-14 17:57:53.165308
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    def test(funcname, code, args, expected):
        interpreter = JSInterpreter('')
        f = interpreter.build_function(['a', 'b', 'c'], code)
        assert f(args) == expected
    test(funcname = 'f', code = 'a + b', args = ['a', 'b', 'c'], expected = 'ab')
    test(funcname = 'f', code = 'a + b + c', args = ['a', 'b', 'c'], expected = 'abc')
    test(funcname = 'f', code = 'a + b + c', args = ['', '1', '2'], expected = '12')
    test(funcname = 'f', code = 'a + b + c', args = ['1', '1', '2'], expected = '12')
    test

# Generated at 2022-06-14 17:58:01.102944
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    interpreter = JSInterpreter("")
    assert interpreter.interpret_expression("1+1", {}, 100) == 2
    assert interpreter.interpret_expression("2+2", {}, 100) == 4
    assert interpreter.interpret_expression("2+2;", {}, 100) == 4
    assert interpreter.interpret_expression("1+1;", {}, 100) == 2
    assert interpreter.interpret_expression("(1+1)", {}, 100) == 2
    assert interpreter.interpret_expression("(1+1);", {}, 100) == 2
    assert interpreter.interpret_expression("(1+1);(2+2);", {}, 100) == 4
    assert interpreter.interpret_expression("return 2+2;(2+2);", {}, 100) == 4