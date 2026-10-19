

# Generated at 2022-06-14 17:49:04.724950
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    import unittest


# Generated at 2022-06-14 17:49:15.823250
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    js_interpreter = JSInterpreter("""
    c = function(){
        var a = 1;
        var b = 2;
        var c = 3;
        var d = a * b * c / 2;
        return a + b + c + d;
    }""")


# Generated at 2022-06-14 17:49:23.411935
# Unit test for method extract_function of class JSInterpreter
def test_JSInterpreter_extract_function():
    js_code = """
    {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": function()
        {
            return this.a + this.b + this.c;
        }
    }
    """
    jsinterpreter = JSInterpreter(js_code)
    assert jsinterpreter.extract_function("d")() == 6



# Generated at 2022-06-14 17:49:36.168023
# Unit test for method extract_object of class JSInterpreter

# Generated at 2022-06-14 17:49:46.470857
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    test_code = r'''
    var obj = {
        a: function (b,c){
            return b + c;
        },
        b: function (b,c){
            return b - c;
        },
        c: "abcd"
    };
    var obj2 = {
        d: function (a,b){
            return a + b;
        }
    };'''
    obj = JSInterpreter(test_code).extract_object('obj')
    assert obj['a'](1, 4) == 5
    assert obj['b'](5, 1) == 4
    assert obj['c'] == "abcd"

    obj2 = JSInterpreter(test_code).extract_object('obj2')
    assert obj2['d'](1, 4) == 5
    return




# Generated at 2022-06-14 17:49:51.732286
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    TEST_CODE = '''d={b:function(a,b){return a+b},c:"hello"};'''
    obj = JSInterpreter(TEST_CODE).extract_object('d')
    assert obj['c'] == 'hello'
    assert callable(obj['b'])
    assert obj['b'](1, 2) == 3


# Generated at 2022-06-14 17:49:57.051755
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    js_interpreter = JSInterpreter('function foo(x){return x + 1}')
    assert js_interpreter.call_function('foo', 2) == 3
    assert js_interpreter.call_function('foo', 3) == 4

    js_interpreter = JSInterpreter('function foo(x, y){return x + y + 1}')
    assert js_interpreter.call_function('foo', 2, 3) == 6
    assert js_interpreter.call_function('foo', 3, 4) == 8


# Generated at 2022-06-14 17:50:10.572609
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    assert JSInterpreter('').build_function([], '1')() == 1
    assert JSInterpreter('function abc(){return 1;}').build_function([], 'return abc()')() == 1
    assert JSInterpreter('').build_function(['a'], 'return a')('b') == 'b'
    assert JSInterpreter('').build_function(['a'], 'return a')('b', 'c') == 'b'
    assert JSInterpreter('function abc(d){return d;}').build_function(['a', 'b'], 'return abc(a)')('c', 'd') == 'c'
    assert JSInterpreter('').build_function(['a', 'b'], 'a=a-b;return a')(5, 3) == 2
   

# Generated at 2022-06-14 17:50:20.642293
# Unit test for method build_function of class JSInterpreter

# Generated at 2022-06-14 17:50:27.941256
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    # build_function method returns a function
    js = JSInterpreter("""
        function test_1(arg1, arg2){
            var result = arg1 * arg2;
            return result;
        }
    """)
    res = js.build_function(['arg1', 'arg2'], "var result = arg1 * arg2;return result")
    assert callable(res)
    assert res((2,3)) == 6
    # build_function method returns a function
    js = JSInterpreter("""
        function test_1(arg1, arg2){
            var result = arg1 * arg2;
            return result;
        }
    """)
    res = js.build_function(['arg1', 'arg2'], "var result = arg1 * arg2;return result")
    assert callable

# Generated at 2022-06-14 17:50:51.220734
# Unit test for method interpret_expression of class JSInterpreter

# Generated at 2022-06-14 17:50:59.902844
# Unit test for method extract_function of class JSInterpreter
def test_JSInterpreter_extract_function():
    JSInterpreter('function test(arg1,arg2){stmt1;stmt2;}').extract_function('test')
    JSInterpreter('test=function(arg1,arg2){stmt1;stmt2;}').extract_function('test')
    JSInterpreter('var test=function(arg1,arg2){stmt1;stmt2;}').extract_function('test')
    JSInterpreter('var test=function(){stmt1;stmt2;}').extract_function('test')

# Generated at 2022-06-14 17:51:08.329921
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    code = '''var ca={"8a":function(a){return a},"1f":function(a){return a},"3b":function(a){return(a<10?"0":"")+a}};
            '''
    jsinterp = JSInterpreter(code)
    obj = jsinterp.extract_object('ca')
    assert obj['8a']('a') == 'a'
    assert obj['1f']('a') == 'a'
    assert obj['3b'](0) == '00'
    assert obj['3b'](9) == '09'
    assert obj['3b'](10) == '10'


# Generated at 2022-06-14 17:51:19.594455
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    local_vars = {'a': [0, 1, 2, 3, 4, 5], 'b': 2, 'c': 3}

    js_interpreter = JSInterpreter('')
    assert js_interpreter.interpret_expression('a[b]', local_vars) == 2
    assert js_interpreter.interpret_expression('a[b + 1]', local_vars) == 3
    assert js_interpreter.interpret_expression('a[a[b]]', local_vars) == 2
    assert js_interpreter.interpret_expression('5 * c', local_vars) == 15

if __name__ == '__main__':
    test_JSInterpreter_interpret_expression()

# Generated at 2022-06-14 17:51:28.572513
# Unit test for method extract_function of class JSInterpreter

# Generated at 2022-06-14 17:51:39.298574
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    js_code = '''
var x = {};
x.split = function(arg) {
    return arg.split(arguments[1]);
};
x.slice = function(arg) {
    return arg.slice(arguments[1]);
};
x.charAt = function(arg) {
    return arg.charAt(arguments[1]);
};
x.charCodeAt = function(arg) {
    return arg.charCodeAt(arguments[1]);
};
x.reverse = function() {
    return this.slice(0).reverse();
};
'''
    js_interpreter = JSInterpreter(js_code)
    assert js_interpreter.interpret_expression('x.split("a,b,c", ",")', {}) == ['a', 'b', 'c']
    assert js

# Generated at 2022-06-14 17:51:49.753545
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    code = r'''
        var f = function(a, b) {
            var c = a + b;
            var d = g(c, b);
            return d;
        };
        var g = function(a, b) {
            var c = 1.5 * a * b;
            return c;
        };
        var h = {
            "key": "value"
        };
        var i = "abcdef";
    '''
    jsi = JSInterpreter(code)
    assert jsi.interpret_expression('1 + 2', {}) == 3
    assert jsi.interpret_expression('var', {'var': 'value'}) == 'value'
    assert jsi.interpret_expression('f(3, 5)', {}) == 52.5

# Generated at 2022-06-14 17:52:01.880834
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    js_interpreter = JSInterpreter('''
var faketitle = function (e){
    function b(i){
    return i.substr(i.length - 1)
    }
    var t = e.substr(e.length - 4),
    n = e.substr(e.length - 3);
    return "mp4" == t || "webm" == t || "ogg" == n ? "video" : "audio"
    }''')

# Generated at 2022-06-14 17:52:11.959304
# Unit test for method extract_object of class JSInterpreter

# Generated at 2022-06-14 17:52:21.235757
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    jsi = JSInterpreter('function dummy(){};')
    args = []
    dummy_function = jsi.build_function(args, '')
    args = [dummy_function, 'dummy', '1', 2, 3.0]
    assert jsi.interpret_expression('0', args) is 0
    assert jsi.interpret_expression('1', args) is 1
    assert jsi.interpret_expression('-1', args) is -1
    assert jsi.interpret_expression('1.2', args) is 1.2
    assert jsi.interpret_expression('1.0', args) is 1.0
    assert jsi.interpret_expression('+1', args) is 1
    assert jsi.interpret_expression('-1', args) is -1

# Generated at 2022-06-14 17:52:43.838411
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    f = JSInterpreter('', {}).build_function(["a", "b", "c", "d", "e"], "c = d + e; b = c + a; f = b + d;")
    assert 6 == f([1, 2, 3, 4, 5])
    assert 11 == f([10, 20, 20, 20, 20])
    assert 16 == f([10, 20, 20, 20, -20])
    assert 15 == f([20, 10, 20, -20, 20])
    assert 17 == f([20, 20, 10, 20, -20])
    assert 21 == f([20, 20, 20, 10, -20])
    assert 16 == f([10, 20, -20, 20, 20])
    assert 14 == f([20, 10, -20, 20, 20])

# Generated at 2022-06-14 17:52:54.048176
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    code = r'''
    var y = {"%":"m","b":[{"a":1},{"a":2},{"a":3}]};
    '''
    interpreter = JSInterpreter(code)
    result = interpreter.interpret_expression('y.b[1]', {})
    assert result == {'a': 2}
    result = interpreter.interpret_expression('y.b[0].a', {})
    assert result == 1
    # The following expression is not supported
    #result = interpreter.interpret_expression('y["%"][1]', {})
    #assert result == "m"


# Generated at 2022-06-14 17:53:04.019622
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    # Case 1: Simple expression 'abc'
    interpreter = JSInterpreter(code = None, objects = None)
    assert interpreter.interpret_expression(expr = 'abc', local_vars = {'abc':'abc'}, allow_recursion = 100) == 'abc'

    # Case 2: Simple expression '123'
    assert interpreter.interpret_expression(expr = '123', local_vars = {'abc':'abc'}, allow_recursion = 100) == 123

    # Case 3: Simple expression 'true'
    assert interpreter.interpret_expression(expr = 'true', local_vars = {'abc':'abc'}, allow_recursion = 100) == True

    # Case 4: Simple expression 'false'

# Generated at 2022-06-14 17:53:10.234208
# Unit test for method interpret_expression of class JSInterpreter

# Generated at 2022-06-14 17:53:18.463834
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    js = r'''var x = 5;
                var y = 3;
                var z = function(a,b){
                    return a+b;
                }
            '''
    interpreter = JSInterpreter(js)
    func = interpreter.build_function(["a", "b"], "var x = a; var y = b; return x + y;")
    assert func([2, 3]) == 5



# Generated at 2022-06-14 17:53:29.026589
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    def test_function(js_code, *args):
        js_interpreter = JSInterpreter(js_code)
        return js_interpreter.build_function(["a", "b", "c"], js_code)(args)

    assert test_function("a", 1, 2, 3) == 1
    assert test_function("return a - b - c;", 1, 2, 3) == -4
    assert test_function("return a + b * c;", 1, 2, 3) == 7
    assert test_function("return (a + b) / c;", 1, 2, 3) == 1
    assert test_function("return a - (b - c);", 1, 2, 3) == 2
    assert test_function("return a == b ? a : c;", 1, 2, 3) == 3

# Generated at 2022-06-14 17:53:38.269688
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    code = '''
        function Myfunc(start, end) {
            if (end - start == 1) {
                return [start];
            } else {
                var m = Math.floor((start + end) / 2);
                return Myfunc(start, m).concat(Myfunc(m, end));
            }
        }
        '''

    js_interpreter = JSInterpreter(code)
    func = js_interpreter.build_function(['start', 'end'], code)

    result = list(func((0, 5)))
    assert result == [0, 1, 2, 3, 4]

# Generated at 2022-06-14 17:53:49.452009
# Unit test for method interpret_expression of class JSInterpreter

# Generated at 2022-06-14 17:53:59.090272
# Unit test for method interpret_expression of class JSInterpreter

# Generated at 2022-06-14 17:54:09.382504
# Unit test for method interpret_statement of class JSInterpreter
def test_JSInterpreter_interpret_statement():
    code = r'''
        function test(arg1, arg2) {
            var a = arg1 + arg2;
            return a;
        }
    '''
    js = JSInterpreter(code)
    assert js.interpret_statement("a = 1; return a;", {}) == (1, True)
    assert js.interpret_statement("a = arg2; return a;", {'arg2': 2}) == (2, True)
    assert js.interpret_statement("a = arg1 + arg2; return a;", {'arg1': 2, 'arg2': 3}) == (5, True)
    assert js.interpret_statement("a = test(1, 2); return a;", {}) == (3, True)

# Generated at 2022-06-14 17:54:31.938893
# Unit test for method interpret_statement of class JSInterpreter
def test_JSInterpreter_interpret_statement():
    assert JSInterpreter('').interpret_statement(
        '0', {})[0] is 0
    assert JSInterpreter('').interpret_statement(
        '1', {})[0] is 1
    assert JSInterpreter('').interpret_statement(
        '1.1', {})[0] is 1.1
    assert JSInterpreter('').interpret_statement(
        '"1.1"', {})[0] == '1.1'
    assert JSInterpreter('').interpret_statement(
        '"1.2a"', {})[0] == '1.2a'
    assert JSInterpreter('').interpret_statement(
        'true', {})[0] is True
    assert JSInterpreter('').interpret_statement(
        'false', {})[0] is False

# Generated at 2022-06-14 17:54:41.080044
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    js = '''
        var a=1;
        var b=2;
        var f = function(a,b,c){
            a=a+b;
            b=c;
            return a;
        };
    '''
    interpreter = JSInterpreter(js)
    f = interpreter.build_function(argnames=('a','b','c'), code=interpreter.code.split(';')[5:-1])
    assert f((4,5,6)) == 9
    assert f((4,5)) == 9

# Generated at 2022-06-14 17:54:48.932529
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    interpreter = JSInterpreter("""
            var test = {
                'split': function(a, b){
                    return b.split(a);
                }
            };
            """)
    f = interpreter.build_function(['a', 'b'], """
            var split = test["split"];
            return split(a, b);
            """)
    assert f("abc".split("")) == 'abc'
    assert f("a".split("a")) == ''



# Generated at 2022-06-14 17:54:53.483796
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    c = """
    x = 'foo';
    return "hello " + x + "!";
    """
    f = JSInterpreter('').build_function(['x'], c)
    assert f(['bar']) == 'hello bar!'

# Generated at 2022-06-14 17:55:02.512479
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    js_interpreter = JSInterpreter('')
    print(js_interpreter.interpret_expression('[]', {}, 5)) # => []
    print(js_interpreter.interpret_expression('{}', {}, 5)) # => {}
    print(js_interpreter.interpret_expression('1', {}, 5)) # => 1
    print(js_interpreter.interpret_expression('"b"', {}, 5)) # => "b"
    print(js_interpreter.interpret_expression('true', {}, 5)) # => true
    print(js_interpreter.interpret_expression('false', {}, 5)) # => false
    print(js_interpreter.interpret_expression('undefined', {}, 5)) # => undefined

# Generated at 2022-06-14 17:55:13.170001
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    jsi = JSInterpreter('''function func1(arg1, arg2) {
            var result = 0;
            for(var i = 0; i < arg1; i++) {
                result += arg2;
            }
            return result;
        }''')
    res = jsi.call_function('func1', 10, 3)
    assert res == 30

    jsi = JSInterpreter('''function func2(arg1, arg2) {
            var result = arg1;
            for(var i = 0; i < arg2.length; i++) {
                result += arg2[i];
            }
            return result;
        }''')
    res = jsi.call_function('func2', 10, [1, 2, 1])
    assert res == 14

    jsi = JSInterpre

# Generated at 2022-06-14 17:55:19.870659
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    with open('js_test.text', 'r') as f:
        source = f.read()

    variables = {}
    f = JSInterpreter(source).build_function(['a', 'b', 'c'], 'a = a * 2 ; b = b * 4 ; c = c * 6')
    f(variables)
    assert variables == {'a': 8, 'b': 24, 'c': 36}



# Generated at 2022-06-14 17:55:31.519266
# Unit test for method call_function of class JSInterpreter

# Generated at 2022-06-14 17:55:41.587083
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():

    code = """
    var f = function(a,b){
        return a+b;
    }
    var g;
    var h = function(a,b){
        return a-b;
    }

    var obj = {
        length: 100,
        join: function(x){return x+a;},
        split: function(x){return x;},
        reverse: function(x){return x;},
        slice: function(x){return x;},
        splice: function(x){return x;}
    }
    """
    js_interpreter = JSInterpreter(code)
    assert js_interpreter.interpret_expression(
        '1 + 2', {'a': 100, 'b': 101}) == 3

# Generated at 2022-06-14 17:55:53.575335
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    js_interpreter = JSInterpreter('')
    def interpret_expression(expr):
        return js_interpreter.interpret_expression(expr, {'a': 0, 'b': 1})

    assert interpret_expression('true') is True
    assert interpret_expression('false') is False
    assert interpret_expression('null') is None
    assert interpret_expression('1') == 1
    assert interpret_expression('1 + 1') == 2
    assert interpret_expression('(1)') == 1
    assert interpret_expression('"foo"') == 'foo'
    assert interpret_expression('"foo" + "bar"') == 'foobar'
    assert interpret_expression('a') == 0
    assert interpret_expression('1 + a') == 1
    assert interpret_expression('a + 1') == 1

# Generated at 2022-06-14 17:56:22.495540
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    script = ("var x = '1' * '1';")
    interpreter = JSInterpreter(script)
    local_vars = {}
    val = interpreter.interpret_expression('x', local_vars, 100)
    assert val == 1

if __name__ == '__main__':
    test_JSInterpreter_interpret_expression()

# Generated at 2022-06-14 17:56:27.057941
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    jsi = JSInterpreter('''
    function a(b, c) {
        return (b+c);
    }
    ''')
    f = jsi.extract_function('a')
    print(f((1,2)))


# Generated at 2022-06-14 17:56:33.744353
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    js_i = JSInterpreter("""function someFunc(foo, bar) {
        var left = foo;
        var right = bar;
        var result = left + right;
        return result;}""")
    assert js_i.build_function(['foo', 'bar'], """var left = foo;
        var right = bar;
        var result = left + right;
        return result;""")([2, 3]) == 5


# Generated at 2022-06-14 17:56:38.527256
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    code = '''
        function add1(arg0, arg1) {
            return arg0 + arg1;
        }
    '''
    interpreter = JSInterpreter(code)
    f = interpreter.extract_function('add1')
    assert f((3, 5)) == 8

# Generated at 2022-06-14 17:56:50.592020
# Unit test for method interpret_statement of class JSInterpreter
def test_JSInterpreter_interpret_statement():
    code = """
        a = 1;
        b = (function () {
            return [
                "a",
                "b",
                "c"
            ];
        }());
    """
    interpreter = JSInterpreter(code)
    local_vars = {}
    interpreter.interpret_statement('a = 1', local_vars)
    assert local_vars['a'] == 1
    interpreter.interpret_statement('var b = a', local_vars)
    assert local_vars['b'] == local_vars['a'] == 1
    interpreter.interpret_statement('var c = b + 1', local_vars)
    assert local_vars['c'] == 2
    interpreter.interpret_statement('var d = a + b', local_vars)
    assert local_vars['d'] == 2
   

# Generated at 2022-06-14 17:57:03.189166
# Unit test for method interpret_statement of class JSInterpreter
def test_JSInterpreter_interpret_statement():
    s = JSInterpreter('')
    # Evaluate numeric expression
    assert s.interpret_statement('2 + 3 + 5 - 8', {})[0] == 2
    # Evaluate assignment
    assert s.interpret_statement('var a = 2', {})[0] == 2
    assert s.interpret_statement('var a = 2 + 3', {})[0] == 5
    assert s.interpret_statement('var a = 2 + 3; a;', {})[0] == 5
    assert s.interpret_statement('var a = 2 + 3; a + 2;', {})[0] == 7
    assert s.interpret_statement('var a = 2 + 3; var a = a + 2; a;', {})[0] == 7
    # Evaluate return
    assert s.interpret_statement('return 2', {})[0] == 2

# Generated at 2022-06-14 17:57:09.788825
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    intepreter = JSInterpreter("", {"objectA": {"foo": "bar"},
                                     "list": ["a", "b"]})

    assert intepreter.interpret_expression("1 + 2 + 3 - 4", {}, 100) == 2
    assert intepreter.interpret_expression("1 + 2 * 3 - 4", {}, 100) == 3
    assert intepreter.interpret_expression("5 / 3", {}, 100) == 1
    assert intepreter.interpret_expression("5 % 3", {}, 100) == 2
    assert intepreter.interpret_expression("(1 + 2) * 3 - 4", {}, 100) == 5
    assert intepreter.interpret_expression("(1 + 2) * 3 - 4", {}, 100) == 5

# Generated at 2022-06-14 17:57:14.443464
# Unit test for method interpret_statement of class JSInterpreter
def test_JSInterpreter_interpret_statement():
    code = "var a = '1'; var b = '2'; c = a + b;"
    js_interpreter = JSInterpreter(code)

    local_vars = {
        'a': 1,
        'b': 2,
        'c': 0
    }

    js_interpreter.interpret_statement("a=a+1", local_vars)
    assert local_vars['a'] == 2


# Generated at 2022-06-14 17:57:22.226894
# Unit test for method interpret_statement of class JSInterpreter
def test_JSInterpreter_interpret_statement():
    js = JSInterpreter('')
    lv = {'a': 1, 'b': [3, 4]}
    assert js.interpret_statement('return a', lv)[0] == 1
    assert js.interpret_statement('return b', lv)[0] == [3, 4]
    assert js.interpret_statement('b[0] = b[0] + 1', lv)[0] == 4
    assert js.interpret_statement('return b[1]', lv)[0] == 4


# Generated at 2022-06-14 17:57:26.721341
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():

    js_code = """
        function f(a, b, c) {
            var d = function(e) {
                return e * 2 + a
            };
            var f = function(g) {
                return g + b
            };

            return d(c) + f(c) + d(c) + f(c)
        }
    """

    js_interpreter = JSInterpreter(js_code)
    assert js_interpreter.call_function('f', 1, 2, 3) == 23


if __name__ == '__main__':
    test_JSInterpreter_call_function()