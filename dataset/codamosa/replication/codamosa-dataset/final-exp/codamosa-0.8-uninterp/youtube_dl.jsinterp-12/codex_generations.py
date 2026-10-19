

# Generated at 2022-06-14 17:48:48.028126
# Unit test for method extract_function of class JSInterpreter
def test_JSInterpreter_extract_function():
    code = '''
        function a(c, d) {
            return c + d;
        }
    '''
    jsi = JSInterpreter(code)
    assert jsi.call_function('a', 4, 5) == 9


# Generated at 2022-06-14 17:48:55.365929
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    import os
    import sys
    print(
        "%s: %s" % (
            'Universal_play_video',
            sys.version
        )
    )
    if sys.version > '3':
        input_string = "input('input_string')"
    else:
        input_string = "input()"
    interpreter = JSInterpreter(
        "function test_function(arguments_string) {"
        "    return arguments_string;"
        "}"
    )
    arg_str = 'arguments_string'
    if sys.version > '3':
        arg_str = arg_str.encode('utf-8')
    result = interpreter.build_function(
        ('arguments_string',),
        "return arguments_string;"
    )

# Generated at 2022-06-14 17:49:03.922616
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    print('Test for method extract_object of class JSInterpreter')
    # Input for unit test of method extract_object of class JSInterpreter
    code = '''
        var cfg = {
            getExpression: function (prop) {
                var _0x5f5d = ['$index'];
                return _0x5f5d[prop];
            }
        }
        '''
    # Expectation output for unit test of method extract_object of class JSInterpreter
    expected = {
        'getExpression': lambda args: ['$index'][args[0]]
    }

    interpreter = JSInterpreter(code)
    assert interpreter.extract_object('cfg') == expected
    print('Pass')



# Generated at 2022-06-14 17:49:15.235801
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    js_interpreter = JSInterpreter('''
        function func_test(arg1, arg2, arg3) {
            return arg1;
        }
        ''')

    func = js_interpreter.build_function(['arg1', 'arg2', 'arg3'], 'return arg1;')
    assert func.__name__ == 'resf'
    assert func((1, 2, 3)) == 1

    func = js_interpreter.build_function(['arg1', 'arg2', 'arg3'], 'return arg2;')
    assert func.__name__ == 'resf'
    assert func((1, 2, 3)) == 2

    func = js_interpreter.build_function(['arg1', 'arg2', 'arg3'], 'return arg3;')

# Generated at 2022-06-14 17:49:26.889500
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    assert JSInterpreter('').interpret_expression('1', {}, 10) == 1
    assert JSInterpreter('').interpret_expression('- 1', {}, 10) == -1
    assert JSInterpreter('').interpret_expression('-1', {}, 10) == -1
    assert JSInterpreter('').interpret_expression(
        '-a', {'a': 1}, 10) == -1
    assert JSInterpreter('').interpret_expression(
        '- 1 - 2', {}, 10) == -3
    assert JSInterpreter('').interpret_expression(
        '-a -  -b', {'a': 1, 'b': 2}, 10) == 3
    assert JSInterpreter('').interpret_expression(
        '1 - -2', {}, 10) == 3

# Generated at 2022-06-14 17:49:28.738406
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    js_interpreter = JSInterpreter('a = 1 + 2;', {})
    assert js_interpreter.call_function('', {}) == 3


# Generated at 2022-06-14 17:49:41.347799
# Unit test for method interpret_expression of class JSInterpreter

# Generated at 2022-06-14 17:49:51.415858
# Unit test for method build_function of class JSInterpreter

# Generated at 2022-06-14 17:49:58.204190
# Unit test for method interpret_expression of class JSInterpreter

# Generated at 2022-06-14 17:50:11.378906
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    code = '''
            function swf(a, c) {
              var b = c;
              if (true) {
                b = a[0];
                var d = a[1];
              }
              var e = [b, d];
              return e
            }
        '''
    func_m = re.search(
        r'''(?x)
            (?:function\s+swf)\s*
            \((?P<args>[^)]*)\)\s*
            \{(?P<code>[^}]+)\}''',
        code)
    argnames = func_m.group('args').split(',')

    inter = JSInterpreter(code)
    f = inter.build_function(argnames, func_m.group('code'))

# Generated at 2022-06-14 17:50:37.493765
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    code = '''
        A = {
            foo: function(bar) {
                return "foo " + bar;
            },
            baz: function(qux) {
                return qux.toUpperCase();
            }
        };
    '''
    obj = JSInterpreter(code).extract_object('A')
    assert len(obj) == 2
    assert obj['foo']('hello') == 'foo hello'
    assert obj['baz']('goodbye') == 'GOODBYE'

if __name__ == '__main__':
    test_JSInterpreter_extract_object()

# Generated at 2022-06-14 17:50:40.292384
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    js = """
        function fact(num) {
            if (num <= 1) { return 1; }
            return num * fact(num - 1);
        }
    """
    res = JSInterpreter(js)
    assert res.call_function("fact", 5) == 120


# Unit tests for method interpret_statement of class JSInterpreter

# Generated at 2022-06-14 17:50:47.092940
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    test_string_1 = (
        "var foobar=function(){return 'hello world';};"
    )

    jsinterpreter = JSInterpreter(test_string_1)

    assert jsinterpreter.call_function("foobar") == 'hello world'

# Generated at 2022-06-14 17:50:54.615115
# Unit test for method interpret_statement of class JSInterpreter
def test_JSInterpreter_interpret_statement():
    interp = JSInterpreter('var a = 2; return a * 3;')

    res, abort = interp.interpret_statement('var a = 2', {})
    assert res == 2
    assert abort == False

    res, abort = interp.interpret_statement('return a * 3', {"a": 2})
    assert res == 6
    assert abort == True

    res, abort = interp.interpret_statement('a * 3', {"a": 2})
    assert res == 6
    assert abort == False


# Generated at 2022-06-14 17:51:05.090954
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    # Test: simple
    assert JSInterpreter('').interpret_expression('5') == 5

    # Test: var
    assert JSInterpreter('').interpret_expression('var a = 5; a') == 5

    # Test: var with spaces
    assert JSInterpreter('').interpret_expression('var a = 5; a') == 5

    # Test: var without spaces
    assert JSInterpreter('').interpret_expression('var a=5;a') == 5

    # Test: var in parens
    assert JSInterpreter('').interpret_expression('(var a=5);a') == 5

    # Test: assignment
    assert JSInterpreter('').interpret_expression('var a = 5; a = 10; a') == 10

    # Test: assignment with spaces

# Generated at 2022-06-14 17:51:16.820478
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    objname = 'id_map'
    js = '''
    id_map = {
        "2108": function(n) {
            return 1;
        },
        "2208": function(n) {
            return 1;
        },
        "mcd": function(n) {
            return 1;
        }
    };
    '''
    Node_to_test, Member_to_test, Params_to_test = "2208", "mcd", "n"
    expected_value = 1 # expected value when calling obj[Member_to_test](Params_to_test)
    extracted_object = JSInterpreter(js, {}).extract_object(objname)
    assert(extracted_object[Node_to_test](Params_to_test) == expected_value)

# Generated at 2022-06-14 17:51:26.523634
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    def get_embed_webpage(url):
        import requests  
        return requests.get(url).text

    javascript_sample = get_embed_webpage('http://www.vim.org/scripts/script.php?script_id=2388')
    js_interpreter = JSInterpreter(javascript_sample)
        
    g_func_name = 'oyejJ'
    arglist = ['XZPQo', 'g(15)']
    expect_result = 'int(0)'
    assert js_interpreter.call_function(g_func_name, *arglist) == expect_result


# Generated at 2022-06-14 17:51:32.122215
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    jsi = JSInterpreter('''
        var arg = "00FFFFFF";
        var arg2 = "1";
        var foo = {
            bar: function(x, y) {
                return x + y;
            }
        };
        function signature_decipher(s) {
            return s.split('').reverse().join('');
        }
    ''')
    assert jsi.call_function('signature_decipher', 'abc') == 'cba'
    assert jsi.call_function('foo.bar', 1, 2) == 3


if __name__ == '__main__':
    test_JSInterpreter_call_function()

# Generated at 2022-06-14 17:51:37.366935
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    JSIP = JSInterpreter('function testFunc(a, b){return a+b;}')
    assert JSIP.call_function('testFunc', 1, 2) == 3

    JSIP = JSInterpreter('function testFunc(a, b){var c;c=a*b;return c;}')
    assert JSIP.call_function('testFunc', 2, 2) == 4

    JSIP = JSInterpreter('function testFunc(a, b){return a-b;}')
    assert JSIP.call_function('testFunc', 2, 1) == 1


if __name__ == '__main__':
    test_JSInterpreter_call_function()

# Generated at 2022-06-14 17:51:43.380063
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    code = '''
        function function_0() {
            this.object_0 = {
                member_0 : function(arg_0) {
                    return arg_0
                },
                field_0 : "value_0"
            };
        };
    '''
    obj = JSInterpreter(code).extract_object('object_0')
    obj['member_0']('test_arg') == 'test_arg'
    obj['field_0'] == 'value_0'

if __name__ == '__main__':
    test_JSInterpreter_extract_object()

# Generated at 2022-06-14 17:52:01.729102
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    code = '''
        var foo = {
            bar: function () {
                return 'bar'
            }
        }
    '''

    obj = JSInterpreter(code).extract_object('foo')
    assert isinstance(obj, dict)
    assert obj['bar']() == 'bar'


# Generated at 2022-06-14 17:52:11.883823
# Unit test for method interpret_expression of class JSInterpreter

# Generated at 2022-06-14 17:52:16.301707
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    # Testing interpreter of simple equations
    js_interpreter = JSInterpreter("")
    expr = "2924 + 2"
    expected_value = expr
    assert js_interpreter.interpret_expression(expr, {}) == eval(expected_value)
    expr = "100 - 20"
    expected_value = expr
    assert js_interpreter.interpret_expression(expr, {}) == eval(expected_value)
    expr = "100 * 20"
    expected_value = expr
    assert js_interpreter.interpret_expression(expr, {}) == eval(expected_value)
    expr = "1000 / 20"
    expected_value = expr
    assert js_interpreter.interpret_expression(expr, {}) == eval(expected_value)
    expr = "1000 % 20"
    expected_value = expr


# Generated at 2022-06-14 17:52:28.485375
# Unit test for method interpret_expression of class JSInterpreter

# Generated at 2022-06-14 17:52:36.781525
# Unit test for method interpret_statement of class JSInterpreter
def test_JSInterpreter_interpret_statement():
    import unittest
    class JSInterpreterTestCase(unittest.TestCase):
        def test_interpret_statement(self):
            # test case1
            JS_CODE = """
                var a = {'b':function(p){return p+1},'c':function(p){return p+2}};
            """
            js_interpreter = JSInterpreter(JS_CODE)
            local_vars = {}
            self.assertEqual(
                js_interpreter.interpret_statement("var d = ['a','b','c'];", local_vars)[0], ['a','b','c'])
            local_vars = {}

# Generated at 2022-06-14 17:52:46.894637
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    txt = """
    var abc = {
       "def": function (a) {
       return 7;
       },
       "ghi": function (a) {
       return 8;
       }
    };
    """
    jsinter = JSInterpreter(txt)
    obj = jsinter.extract_object('abc')
    assert isinstance(obj, dict)
    assert isinstance(obj["def"], type(lambda: None))
    assert isinstance(obj["ghi"], type(lambda: None))
    assert obj['def']() == 7
    assert obj['ghi']() == 8

test_JSInterpreter_extract_object()



# Generated at 2022-06-14 17:52:57.214762
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    code = '''
        function func(arg1, arg2) {
            var object = {
                member1: function(arg1) {
                    return arg1 * 5;
                },
                member2: function(arg2) {
                    return arg2 * 2;
                }
            };
            return object;
        };
    '''
    jsi = JSInterpreter(code)
    obj = jsi.extract_object('object')
    assert obj['member1'](3) == 15
    assert obj['member2'](5) == 10
    return True


# Generated at 2022-06-14 17:53:03.202313
# Unit test for method build_function of class JSInterpreter

# Generated at 2022-06-14 17:53:09.125818
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    code = '''
        a = {
            b: function(p) {
                return p * 2;
            }
        };
        '''
    interp = JSInterpreter(code)
    obj = interp.extract_object('a')
    assert obj['b'](3) == 6

    # Test more
    code = '''
        a = {
            "b": function(p) {
                return p * 2;
            },
            'num': 1,
        };
        '''
    interp = JSInterpreter(code)
    obj = interp.extract_object('a')
    assert obj['b'](3) == 6
    assert obj['num'] == 1



# Generated at 2022-06-14 17:53:22.459548
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    code = '''
        var a;
        a = [1,2,3]
        b = {
            foo: function (a, b) {
                return a+b;
            }
        }
        '''
    js = JSInterpreter(code)
    js.extract_object('b')
    assert js.call_function('b.foo', 32, 32) == 64
    code = '''
        function c(a) {
            return a+1;
        }
        '''
    js = JSInterpreter(code)
    assert js.call_function('c', 32) == 33
    code = '''
        d = function(a) {
            return a+1;
        }
        '''
    js = JSInterpreter(code)

# Generated at 2022-06-14 17:53:53.056703
# Unit test for method build_function of class JSInterpreter

# Generated at 2022-06-14 17:54:01.693933
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    js_interpreter = JSInterpreter('')
    assert js_interpreter.interpret_expression('0', {}) == 0
    assert js_interpreter.interpret_expression('1', {}) == 1
    assert js_interpreter.interpret_expression('"test"', {}) == "test"
    assert js_interpreter.interpret_expression('37+2*4', {}) == 45
    assert js_interpreter.interpret_expression('(3)', {}) == 3
    assert js_interpreter.interpret_expression('(3 + 4) * 7', {}) == 49
    assert js_interpreter.interpret_expression('(1+2) * 3', {}) == 9
    assert js_interpreter.interpret_expression('1 == 3', {}) == False

# Generated at 2022-06-14 17:54:12.126244
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    code = '''
        function f(a,b,c){
            a = 1;
            b /= 10;
            c = a + b;
            return c;
        }
        var x = 3.1;
        var y = f(x,x,x) + x;
        var z = f(y,y,y);
    '''
    js = JSInterpreter(code)
    z = js.call_function("f", 1, 2, 3)
    assert z == 0.9

# Generated at 2022-06-14 17:54:23.296394
# Unit test for method interpret_expression of class JSInterpreter

# Generated at 2022-06-14 17:54:36.000531
# Unit test for method interpret_statement of class JSInterpreter
def test_JSInterpreter_interpret_statement():
    js_interpreter = JSInterpreter()
    stmt = 'var my_var=23;'
    local_vars = {}
    should_abort = False
    returned_value, returned_abort = js_interpreter.interpret_statement(
        stmt, local_vars)
    assert returned_value == 23 and returned_abort == should_abort

    stmt = 'return abcd;'
    local_vars = {'abcd': 1234}
    returned_value, returned_abort = js_interpreter.interpret_statement(
        stmt, local_vars)
    assert returned_value == 1234 and returned_abort is True

    stmt = 'var test_1='
    stmt += '{'
    stmt += '"name": "justin",'
   

# Generated at 2022-06-14 17:54:44.368763
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    objects = {
        'spf': {
            'script': {
                'load': lambda args: ['spf', 'script', 'load', args]
            },
            'response': {
                'process': lambda args: ['spf', 'response', 'process', args]
            }
        },
        '_': {
            'info': {
                'load': {
                    'video': 'https://www.youtube.com/watch?v=iCdP-SD75FU'
                }
            }
        }
    }

    interpreter = JSInterpreter('', objects)

    assert interpreter.interpret_expression('1') == 1
    assert interpreter.interpret_expression('(2)') == 2
    assert interpreter.interpret_expression('1 + 2.3') == 3.3

# Generated at 2022-06-14 17:54:53.899867
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    js = r'''
        var a = {
            b: function() {
                return 4;
            },
            c: 7
        };
        var d = [3,4];
        if (d[1] != 4)
            throw "Expected d[1] == 4";
        if (a.c != 7)
            throw "Expected a.c == 7";
        if (a.b() != 4)
            throw "Expected a.b() == 4";
        ;'''
    JSInterpreter(js).interpret_expression(js, {})


# Generated at 2022-06-14 17:55:02.762397
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    assert JSInterpreter('').interpret_expression('1', {}) == 1
    assert JSInterpreter('').interpret_expression('2 + 3', {}) == 5
    assert JSInterpreter('').interpret_expression('a = 2 + 3', {'a': 0}) == 5
    assert JSInterpreter('').interpret_expression(
        'a = 2 + 3; b = a * a', {'a': 0, 'b': 0}) == 25
    assert JSInterpreter('').interpret_expression(
        'a = {x: 1, y: 2}', {}) == {'x': 1, 'y': 2}
    assert JSInterpreter('').interpret_expression(
        'a = {x: 1, y: 2};a.x', {}) == 1

# Generated at 2022-06-14 17:55:13.316102
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    def verify_interpret_result(source, value_dict, values):
        js_interpreter = JSInterpreter(source)
        for i in range(len(values)):
            value = values[i]
            variable = value_dict[i]
            assert value == js_interpreter.interpret_expression(source, variable)

    source = 'var swfHTML = swfHTML.split("\\n").slice(1).join("\\n");'

# Generated at 2022-06-14 17:55:23.782899
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    def build_function(arg_list, code):
        def res(args):
            local_vars = dict(zip(arg_list, args))
            for stmt in code.split(';'):
                res, abort = interpret_statement(stmt, local_vars)
                if abort:
                    break
            return res
        return res

    def interpret_statement(stmt, local_vars, allow_recursion=100):
        if allow_recursion < 0:
            raise ValueError('Recursion limit reached')

        should_abort = False
        stmt = stmt.lstrip()
        stmt_m = re.match(r'var\s', stmt)
        if stmt_m:
            expr = stmt[len(stmt_m.group(0)):]

# Generated at 2022-06-14 17:55:55.361569
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    JSInterpreter_test = JSInterpreter('', {})
    code = """
        var a = function(b){
            var c = 5;
            var d = b;
            while(c--){
                d--;
            }
            c = e;
            return d;
        }
    """
    argnames = ['e']
    func = JSInterpreter_test.build_function(argnames, re.search(r'\{([^}]+)\}', code).group(1))
    assert func([5]) == 0

# Generated at 2022-06-14 17:55:58.312950
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    # input
    funcname = 'test'
    argnames = ['x','y','z']
    code = 'x+y*z'
    # result
    result = JSInterpreter_build_function(funcname, argnames, code)
    assert result(1,2,3) == 7

# Generated at 2022-06-14 17:56:08.704532
# Unit test for method interpret_expression of class JSInterpreter

# Generated at 2022-06-14 17:56:17.798219
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    js_code = '''
    var k = "";
    var a = "thisisatest";
    var b = "test";
    var c = k + a + b;
    var d = c.split('').reverse().join('');
    function e(c) {
        return d.split('').slice(-c).reverse().join('');
    }
    e(5);
    '''
    interpreter = JSInterpreter(js_code)
    assert interpreter.interpret_expression('5', {}) == 5
    assert interpreter.interpret_expression('b', {}) == 'test'
    assert interpreter.interpret_expression('c', {}) is None
    assert interpreter.interpret_expression('c + b', {}) == 'thisisatesttest'

# Generated at 2022-06-14 17:56:27.005606
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    interpreter = JSInterpreter('')
    locals = {}

    # String
    assert interpreter.interpret_expression(
        "a + b + 'e'", locals) == 'abe'
    assert interpreter.interpret_expression(
        'a + "b"', locals) == 'ab'
    assert interpreter.interpret_expression(
        "'a' + 'b' + c", locals) == 'abc'

    # Numeric
    assert interpreter.interpret_expression(
        "a + 5 + b", locals) == 10
    assert interpreter.interpret_expression(
        'a + b', locals) == 3
    assert interpreter.interpret_expression(
        "a + b + c", locals) == 6
    assert interpreter.interpret_expression(
        "a + b - 5", locals) == -1

    # List

# Generated at 2022-06-14 17:56:39.102422
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    code = r'''function(a){var e={reqId:a,dur:0,earlyF:0,wait:0,serverF:0,play:0,pause:0,rebufs:0};return e}
'''
    inter = JSInterpreter(code)
    vars = {'a': 5}
    val = inter.interpret_expression('function(a){var e={reqId:a,dur:0,earlyF:0,wait:0,serverF:0,play:0,pause:0,rebufs:0};return e}', vars)
    assert(val == {'reqId':5, 'dur':0, 'earlyF':0, 'wait':0, 'serverF':0, 'play':0, 'pause':0, 'rebufs':0})


# Generated at 2022-06-14 17:56:44.294543
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    code = '''
        function func(a, b, c) {
            return a + b + c;
        }
    '''
    assert JSInterpreter(code).build_function(['a', 'b', 'c'], 'return a + b + c;')((1, 2, 3)) == 6


# Generated at 2022-06-14 17:56:54.069086
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    code = """
        var obj = {
            "a": function() {
                console.log("a");
            },
            "b": function() {
                console.log("b");
            },
            "c": function() {
                console.log("c");
            }
        }
        var obj2 = {
            "a": function() {
                console.log("a");
            },
            "b": function() {
                console.log("b");
            },
            "c": function() {
                console.log("c");
            }
        }
    """
    interpreter = JSInterpreter(code)
    interpreter._functions['console.log'] = lambda args: None
    extracted_obj = interpreter.extract_object('obj')
    extracted_obj2 = interpreter.extract_object('obj2')

# Generated at 2022-06-14 17:57:03.990151
# Unit test for method extract_object of class JSInterpreter

# Generated at 2022-06-14 17:57:10.841443
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    code = """
        function a(){};
        function b(){};
        var d = {
            e : function(){},
            f : function(){},
            'g' : function(){}
        };
    """
    jsi = JSInterpreter(code)
    obj = jsi.extract_object('d')
    assert len(obj) == 3
    assert 'e' in obj
    assert 'f' in obj
    assert 'g' in obj
