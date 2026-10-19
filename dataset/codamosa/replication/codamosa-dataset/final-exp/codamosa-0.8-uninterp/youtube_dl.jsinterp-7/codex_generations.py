

# Generated at 2022-06-14 17:49:23.168243
# Unit test for method interpret_statement of class JSInterpreter
def test_JSInterpreter_interpret_statement():
    interpreter = JSInterpreter("a='hello'; b=a+1; return a.split('').reverse().join('');")
    assert interpreter.interpret_statement("a='hello'; b=a+1; return a.split('').reverse().join('');", {}) == ('olleh', True)

# Generated at 2022-06-14 17:49:30.304643
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    # example from http://www.jslint.com/help.html
    interpreter = JSInterpreter('''
        var s = "frog";
        var t = s.substring(1);
    ''')
    assert interpreter.interpret_expression('s', {}) == 'frog'
    assert interpreter.interpret_expression('t', {}) == 'rog'



# Generated at 2022-06-14 17:49:43.024645
# Unit test for method interpret_expression of class JSInterpreter

# Generated at 2022-06-14 17:49:53.144748
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    js_interpreter = JSInterpreter("""
        a = "abcd";
        b = [a, "efgh"];
        c = [b[0], "ijkl"];
        d = c[1];
        function test(a, b, c) {
            var d;
            d = a + b;
            e = c + a[1];
            return d;
        }
        f = test("opqr", "stuv", "wxyz");
        g = f[2];
    """, {'a': 'abcd'})
    assert js_interpreter.interpret_expression("a.length") == 4
    assert js_interpreter.interpret_expression("b[0]") == "abcd"

# Generated at 2022-06-14 17:50:05.111246
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    js_interpreter = JSInterpreter(None, {"b": [1, 2, 3]})
    assert js_interpreter.interpret_expression('(1)', {}, 100) == 1
    assert js_interpreter.interpret_expression('(1 + 2)', {}, 100) == 3
    assert js_interpreter.interpret_expression('(1 + 2) * 3', {}, 100) == 9
    assert js_interpreter.interpret_expression('1', {'a': 2}, 100) == 2
    assert js_interpreter.interpret_expression('a', {'a': 2}, 100) == 2
    assert js_interpreter.interpret_expression('b[0]', {'a': 2}, 100) == 1

# Generated at 2022-06-14 17:50:14.825185
# Unit test for method build_function of class JSInterpreter

# Generated at 2022-06-14 17:50:25.311091
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():

    # test for a expression
    def test_interpret_expr(expr, expected):
        js = JSInterpreter("var p; var q;")
        js.interpret_expression(expr, {'true': True, 'false': False, 'p': 12, 'q': 20})

        assert js.interpret_expression(expr, {'true': True, 'false': False, 'p': 12, 'q': 20}) == expected

    test_interpret_expr("true", True)
    test_interpret_expr("false", False)
    test_interpret_expr("p", 12)
    test_interpret_expr("(p)", 12)
    test_interpret_expr("p+q", 32)
    test_interpret_expr("q-2", 18)
    test_interpret_expr("(p+q)+q", 52)
    test_interpret

# Generated at 2022-06-14 17:50:34.404783
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    js = '''var swfArgs = {"vkey":"9937","t":1435661088,"vid":"e0012q3x3q0&type=mp4","duration":154,"defn":"shd","fmt":"auto","p":0};
'''
    js_interpreter = JSInterpreter(js)
    obj = js_interpreter.extract_object('swfArgs')
    assert obj['t'] == 1435661088
    assert obj['fmt'] == 'auto'


# Generated at 2022-06-14 17:50:47.925241
# Unit test for method interpret_statement of class JSInterpreter
def test_JSInterpreter_interpret_statement():
    objects = {
        'return': 'a',
        'NaN': float('nan'),
        'false': False,
        'true': True,
    }
    js_interpreter = JSInterpreter('a=5;a', objects=objects)
    assert js_interpreter.interpret_statement('return a;', {'a': 5}) == ('a', True)
    assert js_interpreter.interpret_statement('a', {'a': 5}) == (5, False)
    assert js_interpreter.interpret_statement('var a=1;', {}) == (1, False)
    assert js_interpreter.interpret_statement('var b;b=2;b=a;', {'a': 3}) == (3, False)

# Generated at 2022-06-14 17:50:59.847042
# Unit test for method build_function of class JSInterpreter

# Generated at 2022-06-14 17:51:35.038754
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    js = JSInterpreter('''
        a = 2;
        b = 5;
        function foo(c, d){
            return a + b + c + d
        }
    ''')
    res = js.call_function('foo', 1, 2)
    print(res)
    assert res == 10

# Generated at 2022-06-14 17:51:47.861252
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    objects = {
        'Object1': {
            'f1': lambda args: args[0],
            'f2': lambda args: args[1],
            'f3': lambda args: args[0]+args[1]
        }
    }
    js_interpreter = JSInterpreter("Object1['a']=1;Object1['b']=2;Object1['c']=3", objects)
    assert js_interpreter.extract_object('Object1') == {'a': 1, 'b': 2, 'c': 3}
    # Test method extract_object with function
    js_interpreter = JSInterpreter("Object1['f1']=function(a){return a;};", objects)

# Generated at 2022-06-14 17:51:55.535339
# Unit test for method extract_function of class JSInterpreter
def test_JSInterpreter_extract_function():
    code = '''
        function func1(arg1, arg2) {
            var a = 3*arg1;
            var b = 5+arg2;
            return a + b;
        }
        // func2 definition
        function func2(arg3, arg4) {
            var c = func1(arg3, arg4);
            return c;
        }
    '''
    js_interpreter = JSInterpreter(code)
    func_value1 = js_interpreter.extract_function('func1')
    assert func_value1((2, 3)) == 2*3+5+3
    func_value1 = js_interpreter.extract_function('func2')
    assert func_value1((2, 3)) == 2*3+5+3


# Generated at 2022-06-14 17:52:08.103864
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    js_interpreter = JSInterpreter('')
    # Test data:
    # expr, local_vars, expected_output

# Generated at 2022-06-14 17:52:14.824175
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    test_JSInterpreter = JSInterpreter(
        '''
        var a = {
            b: function(a){
                return a
            }
        }
        '''
    )
    test_extract_obj = test_JSInterpreter.extract_object('a')
    attr_name = 'b'
    func = test_extract_obj.get(attr_name)
    assert func is not None, 'Cannot extract function %s from object a' % attr_name
    assert func((1, )) == (1, ), 'Test for %s failed.' % attr_name

if __name__ == '__main__':
    test_JSInterpreter_extract_object()

# Generated at 2022-06-14 17:52:23.006757
# Unit test for method extract_function of class JSInterpreter
def test_JSInterpreter_extract_function():
    code = r'''
        function x(a, b) {
            var c = 25;
            var d = a * b * c;
            var e = d % c;
            return e;
        }
        '''
    interp = JSInterpreter(code)
    f = interp.extract_function('x')
    assert f((2, 3)) == 10
    f = interp.extract_function('x')
    assert f((1, 2)) == 5


# Generated at 2022-06-14 17:52:32.390157
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    jsi = JSInterpreter('''
        function myfunc(x, y, z) {
            a = x + y;
            b = a * z;
            return b;
        }
    ''')
    f = jsi.build_function(['x', 'y', 'z'], '''
        a = x + y;
        b = a * z;
        return b;
    ''')
    assert f((2, 3, 5)) == 25
    assert f((3, 4, 2)) == 14

if __name__ == '__main__':
    import sys
    import argparse
    argparser = argparse.ArgumentParser()

# Generated at 2022-06-14 17:52:43.071624
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    """
    Expression
        1
        -1
        1 + 1
        1 - 1
        1 * 1
        1 / 1
        1 % 1
        1 ^ 1
        1 << 1
        1 >> 1
        1 & 1
        1 | 1
        "1"
        '1'
        true
        false
        a
        b[c]
        d(e, f)
    """
    js = JSInterpreter("""
        var a = 1;
        var b = function(c) {
            return [1, 2, 3];
        };
        var d = function(e, f) {
            return e + f;
        };
    """)
    assert js.interpret_expression('1', {}) == 1
    assert js.interpret_expression('-1', {}) == -1

# Generated at 2022-06-14 17:52:53.918601
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    # Test 1: simple object initialisation
    code = '''
        var Test = {
            field1: 'a',
            field2: 'b',
            field3: 'c',
        };
    '''
    jsi = JSInterpreter(code)
    obj = jsi.extract_object('Test')
    assert obj == {'field1': 'a', 'field2': 'b', 'field3': 'c'}
    # Test 2: multiple object initialisation
    code = '''
        var Test = {
            field1: 'a',
            field2: 'b',
            field3: 'c',
        };
        var Test2 = {
            field1: 'a2',
            field2: 'b2',
            field3: 'c2',
        };
    '''
    j

# Generated at 2022-06-14 17:53:03.957594
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    code = '''
        ytplayer.config = {'args': {
            'no_get_video_log': '',
            'video_id': 'WDZajpI1gD0',
            't': 'vjVQa1PpcFNbXhYJakl0R1c1ajl5dDRzd0tEa3lzV3BqNXdXZVMyN3Nk'
        }};
    '''
    interpreter = JSInterpreter(code)
    function = interpreter.build_function(['args'], '''
        var b = f(args.video_id, args.t);
        var d = a(b);
        var e = d.split("");
        c = g(e, b);
        return c;
    ''')
   

# Generated at 2022-06-14 17:53:27.413806
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    # Simple object
    code = """
        var obj = {"id": "abc", "func": function(b) { return b + "def" }};
    """
    obj = JSInterpreter(code).extract_object('obj')
    assert obj == {'id': 'abc', 'func': lambda b: b + 'def'}

    # Obj. with nested object
    code = """
        var obj = {"id": "abc", "func": function(b) { return b + "def" },
                   "nested": { "key": "qqwerty" }};
    """
    obj = JSInterpreter(code).extract_object('obj')
    assert obj == {'id': 'abc',
                   'func': lambda b: b + 'def',
                   'nested': {'key': 'qqwerty'}}

# Generated at 2022-06-14 17:53:39.367610
# Unit test for method call_function of class JSInterpreter

# Generated at 2022-06-14 17:53:50.296559
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    code = r'''
    var d = function() {
        var a = '';
        var b = {};
        b.length = 0x400;
        b[0] = '\\u0068\\u0065\\u006c\\u006c\\u006f';
        b[129] = '\\u0077\\u006f\\u0072\\u006c\\u0064';
        for (var c = 0; c < b.length; c++) {
            if (b[c]) {
                a += b[c];
            }
        }
        return a;
    }();
    '''
    js_in = JSInterpreter(code)
    assert js_in.call_function('d') == 'hello world'


# Generated at 2022-06-14 17:53:55.076743
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    js_code_str='''
        var a = 'ytd-thumbnail'.slice(2);
    '''
    js_interpreter = JSInterpreter(js_code_str)
    a=js_interpreter.call_function('slice', 'ytd-thumbnail', 2)
    assert a=='thumbnail'

# Generated at 2022-06-14 17:54:07.125776
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    obj = []
    js_interp = JSInterpreter("""
        ytplayer.config = {'assets': {
            'js': '//s.ytimg.com/yts/jsbin/player-fr_FR-vflW7RvQc/base.js'},
            'args':{
                't': '1,00:00:00.00',
                'vmap': '4'
            }
        };
    """)
    js_interp.build_function(['arg1', 'arg2'], """
        tst = arg1 + " " + arg2;
        ;
        obj.append(tst);
    """)(['hello', 'world'])
    assert obj == ['hello world']



# Generated at 2022-06-14 17:54:17.016726
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    code = """
    var a = 123;
    var b = 456;
    function x(c,d){
        return a + b + c + d;
    }"""
    JSInt=JSInterpreter(code)
    func_m = re.search(
            r'''(?x)
                (?:function\s+x|[{;,]\s*x\s*=\s*function|var\s+x\s*=\s*function)\s*
                \((?P<args>[^)]*)\)\s*
                \{(?P<code>[^}]+)\}''' ,
            code)
    argnames=func_m.group('args').split(',')
    f=JSInt.build_function(argnames, func_m.group('code'))

# Generated at 2022-06-14 17:54:23.240344
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    jsi = JSInterpreter("")
    assert(jsi.interpret_expression("3", {})) is 3
    assert(jsi.interpret_expression("3.14", {})) == 3.14
    assert(jsi.interpret_expression("true", {})) is True
    assert(jsi.interpret_expression("false", {})) is False
    assert(jsi.interpret_expression("'abc'", {})) == 'abc'

if __name__ == "__main__":
    test_JSInterpreter_interpret_expression()

# Generated at 2022-06-14 17:54:35.863106
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    jsi = JSInterpreter('', {
        'a': 100,
        'b': [0, 1, 2, 3],
        'c': [[1, 2], [3, 4]],
    })
    assert jsi.interpret_expression('a', {}) == 100
    assert jsi.interpret_expression('b[2]', {}) == 2
    assert jsi.interpret_expression('c[1][1]', {}) == 4
    assert jsi.interpret_expression('b[1 + 1]', {}) == 2
    assert jsi.interpret_expression('b[1 + 1] + 10', {}) == 12
    assert jsi.interpret_expression('2 + 3 * 5', {}) == 17
    assert jsi.interpret_expression('6 * 7 + 8', {}) == 50
    assert jsi.interpret_

# Generated at 2022-06-14 17:54:44.081594
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    js = '''
        function func(a,b,c){
            if (a === b && b === 0)
                return 0;
            if (a === b && b === 1)
                return 1;
            return c;
        }
    '''
    js_interpreter = JSInterpreter(js)
    func = js_interpreter.build_function(['a', 'b', 'c'], 'if (a === b && b === 0)return 0;if (a === b && b === 1)return 1;return c;')
    assert func([1, 2, 3]) == 3
    assert func([0, 0, 3]) == 0
    assert func([0, 1, 3]) == 3
    assert func([1, 1, 3]) == 1


# Generated at 2022-06-14 17:54:54.522378
# Unit test for method extract_object of class JSInterpreter

# Generated at 2022-06-14 17:55:13.920608
# Unit test for method extract_object of class JSInterpreter

# Generated at 2022-06-14 17:55:24.154601
# Unit test for method extract_object of class JSInterpreter

# Generated at 2022-06-14 17:55:33.032361
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    interpreter = JSInterpreter('function a(b) {return b;}')
    assert interpreter.interpret_expression('a(b)', {'b': 1}) == 1

    interpreter = JSInterpreter('function a(b) {return b.c;}')
    assert interpreter.interpret_expression('a(b)', {'b': {'c': 1}}) == 1

    interpreter = JSInterpreter('function a(b) {return b[0];}')
    assert interpreter.interpret_expression('a(b)', {'b': [1, 2]}) == 1

    interpreter = JSInterpreter('function a(b) {return b[0][1][2];}')
    assert interpreter.interpret_expression('a(b)', {'b': [1, [2, [3]]]}) == 3

    interpreter = JSInter

# Generated at 2022-06-14 17:55:44.196357
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    js = JSInterpreter("""{}; a = {}; a.b = function (x) {};""")
    # Empty expression
    assert js.interpret_expression(""" "" """, {}) is None
    # Just a variable
    assert js.interpret_expression("a", {'a': 42}) == 42
    # Accessing a member
    assert js.interpret_expression("a.b", {'a': {'b': 42}}) == 42
    # Calling a function with no argument
    assert js.interpret_expression("a.b()", {'a': {'b': lambda: 42}}) == 42
    # Calling a function with one argument
    assert js.interpret_expression("a.b(42)", {'a': {'b': lambda x: x * 2}}) == 84


# Generated at 2022-06-14 17:55:52.038377
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    # Test 1
    code = """
        var c = function(a,b){
            return a-b;
        }
        var d = c(e,f);
        """
    objects={}
    jsi = JSInterpreter(code,objects)
    local_vars={'e':6,'f':2}
    assert(jsi.interpret_expression('c(e,f)',local_vars,5)==4)
    # Test 2
    code = """
        var c = function(a,b){
            return a-b;
        }
        var d = c(e,f);
        """
    objects={}
    jsi = JSInterpreter(code,objects)
    local_vars={'e':6,'f':2}

# Generated at 2022-06-14 17:56:03.306226
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    print("Testing method JSInterpreter.extract_object")
    code = '''s = {
    e: function(arr, x, y){
        return x + y
    },
    a: function(){
        return 1
    },
    b: function(e, arr){
        return arr
    }
}'''
    interpreter = JSInterpreter(code)
    obj = interpreter.extract_object("s")
    assert obj['e']((None, 1, 2)) == 3
    assert obj['a'](None) == 1
    assert obj['b']((None, [1, 2, 3])) == [1, 2, 3]



# Generated at 2022-06-14 17:56:11.276900
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    code = r'''
    hq = {
       "xk": function(p) {
        return p;
       },
       "jy": function(p) {
        return p + 1;
       },
    };
    '''
    interpreter = JSInterpreter(code)
    obj = interpreter.extract_object("hq")
    assert obj["xk"](42) == 42
    assert obj["jy"](42) == 43

    code = r'''
    aw = {
            "gq": function(p) {
                var b = 0;
                if (p) {
                    b = 1;
                }
                return b;
            },
        };
    '''
    interpreter = JSInterpreter(code)
    obj = interpreter.extract_object("aw")
    assert obj

# Generated at 2022-06-14 17:56:17.855763
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    # Expected result
    expected_result = 'Hello World'
    # Code to test
    code = '''
        function test(a, b) {
            return a + b;
        }
    '''
    # Arguments to test on
    args = ['Hello ', 'World']
    # Initialize JSInterpreter
    interpreter = JSInterpreter(code)
    # Get the result of the tested code
    result = interpreter.build_function(('a', 'b'), code)(args)
    # Assert the result is the one expected
    assert result == expected_result



# Generated at 2022-06-14 17:56:27.035380
# Unit test for method build_function of class JSInterpreter

# Generated at 2022-06-14 17:56:39.146100
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    with open('tests/resources/interpreter/js.html') as f:
        js = f.read()

    test = JSInterpreter(js)
    code = '''
        for (var s = "", i = 0; i < 3e3; i++) {
            s = s.concat(i);
        }
        return s;
    '''
    f = test.build_function([], code)
    assert isinstance(f, type(lambda x:x))

# Generated at 2022-06-14 17:56:58.470752
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    obj_def = "var obj = { a: function(b){ return b + 1; } };"
    js_interpreter = JSInterpreter(obj_def)
    obj = js_interpreter.extract_object('obj')
    assert obj['a'](10) == 11


# Generated at 2022-06-14 17:57:05.303940
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    tests = [
        ('if(foo){bar=1}', {'foo': True}, True),
        ('if(foo){bar=1}else{bar=2}', {'foo': False}, False),
        ('bar=foo?1:2', {'foo': True}, True),
        ('bar=foo?1:2', {'foo': False}, False),
        ('bar=1+2', {}, True),
    ]

    for expr, globals, expect_result in tests:
        js = JSInterpreter('', globals)
        assert js.interpret_expression(expr, globals) == expect_result

# Generated at 2022-06-14 17:57:14.543935
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    jsi = JSInterpreter('')

    assert jsi.interpret_expression('1+1') == 2
    assert jsi.interpret_expression('(1)') == 1
    assert jsi.interpret_expression('(1+1)') == 2
    assert jsi.interpret_expression('(1+1)==3') == False
    assert jsi.interpret_expression('(1+2*3)>5') == True
    assert jsi.interpret_expression('(1+2*3)>5&&1+1==2') == True
    assert jsi.interpret_expression('1+1==2') == True
    assert jsi.interpret_expression('1+1 == 2') == True
    assert jsi.interpret_expression('1 + 1 == 2') == True

# Generated at 2022-06-14 17:57:23.098215
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    js_interpreter = JSInterpreter(code='')

    assert js_interpreter.interpret_expression('1+1', {}) == 2
    assert js_interpreter.interpret_expression('2-1', {}) == 1
    assert js_interpreter.interpret_expression('2*2', {}) == 4
    assert js_interpreter.interpret_expression('4/2', {}) == 2
    assert js_interpreter.interpret_expression('1%2', {}) == 1
    assert js_interpreter.interpret_expression('2<<2', {}) == 8
    assert js_interpreter.interpret_expression('8>>2', {}) == 2
    assert js_interpreter.interpret_expression('1&1', {}) == 1

# Generated at 2022-06-14 17:57:24.648961
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    # Sample 1
    # assert build_function('parseInt(p,10)', 'function x(p){return parseInt(p,10);}', 2) == 2
    pass

# Generated at 2022-06-14 17:57:36.864119
# Unit test for method interpret_expression of class JSInterpreter

# Generated at 2022-06-14 17:57:47.833577
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    js_code = '''
        var o1 = {
            a: function(a, b){
                return a + b;
            },
            "b": function(a, b){
                return a - b;
            },
            'c': function(a, b){
                return a * b;
            },
            d: function(a, b){
                return a / b;
            }
        };
        var o2 = {
            a: function(a, b){
                return a + b;
            },
            "b": function(a, b){
                return a - b;
            },
            'c': function(a, b){
                return a * b;
            },
            d: function(a, b){
                return a / b;
            }
        };
    '''
    extracted_

# Generated at 2022-06-14 17:57:57.006883
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    # Tests for var assignments
    js = JSInterpreter("", {})
    local_vars = {}
    js.interpret_expression("var a = 3", local_vars, 100)
    print(local_vars)
    assert local_vars['a'] == 3
    js.interpret_expression("a=4", local_vars, 100)
    print(local_vars)
    assert local_vars['a'] == 4
    # Test for lists
    local_vars = {'a': ['v']}
    js.interpret_expression("a[0] = 5", local_vars, 100)
    print(local_vars)
    assert local_vars['a'] == [5]
    # Test for numbers
    js.interpret_expression("a=3", local_vars, 100)


# Generated at 2022-06-14 17:58:09.175910
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    assert JSInterpreter("").interpret_expression("1", {}) == 1
    assert JSInterpreter("").interpret_expression("'a'", {}) == 'a'
    assert JSInterpreter("").interpret_expression("f('a')", {'f': lambda x: x}) == 'a'
    assert JSInterpreter("").interpret_expression("a", {'a': 1}) == 1
    assert JSInterpreter("").interpret_expression("a.b", {'a': {'b': 1}}) == 1
    assert JSInterpreter("").interpret_expression("f(a)", {'f': lambda x: x, 'a': 1}) == 1