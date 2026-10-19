

# Generated at 2022-06-14 17:49:04.307883
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    jsi = JSInterpreter('')
    assert jsi.interpret_expression('n + 1', {'n': 1}) == 2
    assert jsi.interpret_expression('arr[n]', {'n': 1, 'arr': [1, 2, 3]}) == 2
    assert jsi.interpret_expression(
        'arr[n + 1]', {'n': 1, 'arr': [1, 2, 3]}) == 3
    assert jsi.interpret_expression('"abc"', {}) == 'abc'
    assert jsi.interpret_expression('an_array.pop()', {'an_array': [1, 2, 3]}) == 3
    assert jsi.interpret_expression('line.split("-")', {'line': 'a-b-c'}) == ['a', 'b', 'c']


# Generated at 2022-06-14 17:49:15.542048
# Unit test for method extract_object of class JSInterpreter

# Generated at 2022-06-14 17:49:24.251001
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    js = r'''
        var ytplayer = {
                "config":{
                    "args":{
                        "foo":"bar",
                        "fizz":"buzz"
                    }
                }
            };
    '''

    jsi = JSInterpreter(js)
    assert jsi.extract_object('ytplayer') == {
        "config": {"args": {"foo": "bar", "fizz": "buzz"}}}


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 17:49:36.209086
# Unit test for method build_function of class JSInterpreter

# Generated at 2022-06-14 17:49:46.513655
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    code = '''
        var obj = {
            "a": 1,
            "b": "value",
            "c": function(a, b, c) {
                return a + b + c;
            }
        };
        var d = {
            "b": function(a, b) {
                return a * b;
            }
        };
    '''
    interp = JSInterpreter(code)
    obj = interp.extract_object('obj')
    assert isinstance(obj, dict)
    assert len(obj) == 3
    assert obj['a'] == 1
    assert obj['b'] == 'value'
    assert callable(obj['c'])
    assert obj['c'](1, 2, 3) == 6
    # test extraction from separate lines
    obj = interp.extract

# Generated at 2022-06-14 17:49:55.838202
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    js_code = ('function a(b,c){\n'
               'f={"a":a.toString(),b:b.toString(),c:c.toString()};\n'
               'return f};')

    #########################################################################
    # Test 1:
    # Test interpret_expression with an empty statement,
    # which should return None
    js_interpreter = JSInterpreter(js_code)
    assert not js_interpreter.interpret_expression("",js_interpreter._objects,1)


    #########################################################################
    # Test 2:
    # Test interpret_expression with a statement contains a variable name
    # which should return the variable's value
    js_interpreter = JSInterpreter(js_code)

# Generated at 2022-06-14 17:50:09.157938
# Unit test for method interpret_statement of class JSInterpreter
def test_JSInterpreter_interpret_statement():
    code = r'''
        function f(a, b) {
            var c = 1 * 3 * 5 * 7 * 9;
            return c;
        }
        var d = 9 * 7 * 5 * 3 * 1;
    '''
    jsi = JSInterpreter(code)
    assert jsi.interpret_statement('var a = 42 * 7 * 1 * 6 * 3;', {})[0] == 1008
    assert jsi.interpret_statement('return b', {'a': 'b'}) == ('b', True)
    assert jsi.interpret_statement('return a', {'a': 42}) == (42, True)
    assert jsi.interpret_statement('var f = g;', {})[0] == 'g'

# Generated at 2022-06-14 17:50:16.835162
# Unit test for method extract_function of class JSInterpreter

# Generated at 2022-06-14 17:50:25.476512
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    try:
        JSInterpreter("").extract_object("")
    except ExtractorError as e:
        print("Test failed: %s" % e)

    try:
        JSInterpreter("{}").extract_object("")
    except ExtractorError as e:
        print("Test failed: %s" % e)

    try:
        JSInterpreter("{x:function(){}, y:function(){}}").extract_object("")
    except ExtractorError as e:
        print("Test failed: %s" % e)

    try:
        JSInterpreter("x={x:function(){}, y:function(){}}").extract_object("")
    except ExtractorError as e:
        print("Test failed: %s" % e)


# Generated at 2022-06-14 17:50:27.938601
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    js_interpreter = JSInterpreter('')
    f = js_interpreter.build_function(['a', 'b', 'c'], 'a(b+c)')
    assert f((1, 2, 3)) == 6


# Generated at 2022-06-14 17:51:30.777783
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    # Simple case
    js = "var a = 1;\nvar b = a;"
    i = JSInterpreter(js)
    assert i.interpret_expression('a', {}) == 1
    assert i.interpret_expression('b', {}) == 1
    # Containing object
    js = "var a = {'b':1};\nvar c = a.b;"
    i = JSInterpreter(js)
    assert i.interpret_expression('a.b', {}) == 1
    assert i.interpret_expression('c', {}) == 1
    # Object with function
    js = "var a = {'b':function() {return 1;}};\nvar c = a.b();"
    i = JSInterpreter(js)
    assert i.interpret_expression('a.b()', {}) == 1

# Generated at 2022-06-14 17:51:37.079611
# Unit test for method interpret_expression of class JSInterpreter

# Generated at 2022-06-14 17:51:48.566397
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    js_interpreter = JSInterpreter('''
        jwplayer.thumbs = function() {
            var encoded = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
            return {
                encode: function(number) {
                    if (number < 0) {
                        number = 0;
                    }
                    if (number > 1) {
                        number = 1;
                    }
                    var e = Math.floor(number * (encoded.length - 1));
                    return {
                        base64: encoded.charAt(e),
                        ascii: e
                    };
                }
            };
        }();
        ''')

# Generated at 2022-06-14 17:51:58.070684
# Unit test for method extract_function of class JSInterpreter
def test_JSInterpreter_extract_function():
	code_a = '''
		var a="a";
		var b="b";
		var c="c";
		'''
	code_b = '''
		var d="d";
		var e="e";
		var f="f";
		function b(a,c){
			var d=a+c;
			return d+"g";
		}
		'''
	code = code_a+code_b
	assert(JSInterpreter(code).extract_function("b")("2","3")=="5g")


# Generated at 2022-06-14 17:52:09.395286
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    html = '''
        <html>
        <head>
        <script>
            var A = {
                "B": function(p) {
                    return p;
                }
            }
        </script>
        </head>
        <body>
        </body>
        </html>
    '''
    js_code = JSInterpreter('', {'html': html})
    js_obj = js_code.extract_object('A')
    assert js_obj['B']('x') == 'x'

    # It should return an object with the same name
    js_code = JSInterpreter('', {'html': html})
    js_obj = js_code.extract_object('B')
    assert js_obj['B']('x') == 'x'


# Generated at 2022-06-14 17:52:16.227175
# Unit test for method interpret_expression of class JSInterpreter

# Generated at 2022-06-14 17:52:28.441082
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    code = """
        var a = { a: 'ok' };
        var b = function (arg1) {
            return arg1;
        };
        function c(arg1, arg2) {
            return arg1 + arg2;
        }"""
    interpreter = JSInterpreter(code)
    assert interpreter.call_function('b', 'ok') == 'ok'
    assert interpreter.call_function('c', 'ok', 'ok') == 'okok'
    assert interpreter.call_function('c', 'okok', 'ok') == 'okokok'
    assert interpreter.call_function('c', 1, 2) == 3
    assert interpreter.call_function('c', 1, -1) == 0
    assert interpreter.call_function('c', 1, -0.999) == 0

# Generated at 2022-06-14 17:52:37.521954
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    js = JSInterpreter('', {})
    f = js.build_function(['a', 'b'],
    '''
    c=a+b;
    return c;
    '''
    )
    assert f([1, 2]) == 3

    f = js.build_function(['a', 'b'],
    '''
    c=a+b;
    return c;
    '''
    )
    assert f([2, 2]) == 4


# Generated at 2022-06-14 17:52:47.641023
# Unit test for method extract_function of class JSInterpreter
def test_JSInterpreter_extract_function():
    # test data
    obj = (
        'var a={b:function(p){do{p+=d}while(p<e);return p}};'
        'var g={h:function(p){do{p+=d}while(p<e);return p}};'
    )
    # expect result
    exp_res = '{h: function (p){do{p+=d}while(p<e);return p}}'

    actual_res = JSInterpreter(obj).extract_function('g').__str__()
    assert actual_res == exp_res, 'result of method extract_function of class JSInterpreter is not correct'
    return


# Generated at 2022-06-14 17:52:53.058087
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    JSInterpreter("""
        var foo = { bar: 'baz' };
        var sayHi = function(message) {
            console.log(message + ', ' + foo.bar);
        }
    """).call_function('sayHi', 'Hello')

# Generated at 2022-06-14 17:53:23.652521
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    # Test
    js_interpreter = JSInterpreter('function test_function(var1){ return var1 + 1 };')
    assert js_interpreter.call_function("test_function", 1) == 2
    assert js_interpreter.call_function("test_function", "a") == "a1"



# Generated at 2022-06-14 17:53:28.836959
# Unit test for method interpret_statement of class JSInterpreter
def test_JSInterpreter_interpret_statement():
    code = """
        function test(arg1, arg2, arg3) {
            var a = arg1;
            return a;
        }
    """
    interpreter = JSInterpreter(code)
    assert interpreter.call_function('test', 'abc', 'def', 'ghi') == 'abc'


# Generated at 2022-06-14 17:53:40.565777
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    # Test case 1: functions with predefined variables
    def test_case_1(argname, code, args, expected):
        i = JSInterpreter('')
        f = i.build_function([argname], code)
        assert f(args) == expected

    test_case_1(
        'x',
        'return x',
        (5,),
        5)
    test_case_1(
        'x',
        'return x + 1',
        (5,),
        6)
    test_case_1(
        'x',
        'return x.join("")',
        (list('hi there'),),
        'hi there')
    test_case_1(
        'x',
        'return x.reverse();',
        (list('hi there'),),
        None)
   

# Generated at 2022-06-14 17:53:42.105125
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    JSInterpreter.test_build_function()


# Generated at 2022-06-14 17:53:53.347947
# Unit test for method interpret_statement of class JSInterpreter
def test_JSInterpreter_interpret_statement():
    class JSInterpreter(object):
        def interpret_expression(self, expr, local_vars, allow_recursion):
            if expr.isdigit():
                return int(expr)
            if expr == 'a':
                return 10
            if expr == 'b':
                return 2
            raise ExtractorError('unsupported expression')
        def interpret_statement(self, stmt, local_vars, allow_recursion):
            if stmt.startswith('return '):
                return self.interpret_expression(stmt[7:], local_vars, allow_recursion), True

    stmt = 'var a = 10; return a;'
    local_vars = {}
    allow_recursion = 100
    # convert stmt to a list

# Generated at 2022-06-14 17:54:01.872354
# Unit test for method interpret_statement of class JSInterpreter
def test_JSInterpreter_interpret_statement():
    js_code = r'''
    var obj = {};
    obj.a = 0x1;
    obj.b = 0x3;
    obj.c = function(a, b) {
        var c = a + b;
        var d = a * b;
        return d | c;
    }
    '''

    js_interpreter = JSInterpreter(js_code)
    assert js_interpreter.interpret_statement('var a = 1', {})[0] == 1

    # Test function call
    local_vars = {
        'a': 2,
        'b': 6,
    }
    assert js_interpreter.interpret_statement('var a = obj.c(a, b)', local_vars)[0] == 14



# Generated at 2022-06-14 17:54:15.471569
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    js = JSInterpreter("""
        function func_1(a,b,c){
            a = [0,0,0,0,0,0];
            a[0] = b;
            a[1] = c;
            return a;
        }
        function func_2(a,b,c){
            function func_2_1(a){
                return a + 2;
            }
            a = [0,0,0,0,0,0];
            a[0] = func_2_1(b);
            a[1] = c;
            return a;
        }

    """)
    argnames = ['a', 'b', 'c']

# Generated at 2022-06-14 17:54:24.242543
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    instance = JSInterpreter('')
    assert instance.call_function('foo') == None
    assert instance.call_function('return foo') == 'foo'
    assert instance.call_function('(function(x){ return x; })', 'hello') == 'hello'
    assert instance.call_function('(function(x){ return x + 1; })', 3) == 4
    assert instance.call_function('(function(x, y){ return x + y; })', 1, 2) == 3
    assert instance.call_function('(function(x){ return x[0] + x[1]; })', [1, 2]) == 3
    assert instance.call_function('(function(x){ return x[0] + x[1]; })', (1, 2)) == 3

# Generated at 2022-06-14 17:54:36.736541
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    def _test_statement(js, expected_res):
        res, abort = JSInterpreter(js).interpret_statement(js, locals())
        assert res == expected_res, 'Expecting %r as result for %r, got %r' % (
            expected_res, js, res)
    _test_statement('0', 0)
    _test_statement('var s = "abcd";', None)
    _test_statement('s', 'abcd')
    _test_statement('s.length', 4)
    _test_statement('s.split("")', ['a', 'b', 'c', 'd'])
    _test_statement('s.split("").join("")', 'abcd')
    _test_statement('s.reverse()', ['d', 'c', 'b', 'a'])
    _test

# Generated at 2022-06-14 17:54:43.837671
# Unit test for method interpret_statement of class JSInterpreter

# Generated at 2022-06-14 17:56:05.990700
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    code = """
        function test() {
          let a = 'test';
          return a;
        }
    """
    js_int = JSInterpreter(code)
    assert js_int.call_function('test') == 'test'


if __name__ == '__main__':
    import doctest
    doctest.main()

# Generated at 2022-06-14 17:56:09.543787
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    code = """
        function b(x) {
        return x;
        }
        """
    x = JSInterpreter(code)
    b = x.call_function("b", "hello world")
    assert b == "hello world"

if __name__ == '__main__':
    test_JSInterpreter_call_function()

# Generated at 2022-06-14 17:56:18.228409
# Unit test for method interpret_expression of class JSInterpreter

# Generated at 2022-06-14 17:56:30.036690
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    code = r'''
        function test1(str1,str2)
        {
            var out = str1.slice(str2)
            return out
        }
        '''
    from .test_util import assertEquals
    js_interpreter = JSInterpreter(code)
    # test slice method
    str1 = 'ZTjT0T'
    str2 = 'j'
    assertEquals(js_interpreter.call_function('test1', str1, str2), 'T0T')
    # test split method
    code = r'''function test1(str1,str2)
        {
            var out = str1.split(str2)
            return out
        }'''
    js_interpreter = JSInterpreter(code)

# Generated at 2022-06-14 17:56:41.467710
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    test_js_code = '''
        var g_smooth_rates = {"r":0,"smf":10,"segs":1,"ts":1414211225};
        var g_idle_timer = {id: null, callbacks: []};
        var a = {"version":"8.8.8", "query":function(a,b,c){}};
        var b = {"c":function(a,b){}};
        function c(a, b){b.push(a)}
        function d(a){
            for (i = 0; i < a.length; i++) {
                a[i] = a[i] + 1;
            }
        }
    '''

# Generated at 2022-06-14 17:56:52.860089
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    text1 = '''
        var obj0 = {
            func0: function (arg0, arg1) {
                var loc0 = arg0;
                var loc1 = arg1;
                return loc0 + loc1;
            }
        };
        '''
    JMSt = JSInterpreter(text1)
    JMSt.build_function(['arg0', 'arg1'], 'var loc0 = arg0;var loc1 = arg1;return loc0 + loc1;')
    assert JMSt.call_function('func0', 2, 3) == 5


# Generated at 2022-06-14 17:56:59.706440
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    js = '''
        var a={
            b:function(){return 1},
            c:function(){return 2}
        }
        for(var i in a){
            console.log(i,a[i]())
        }
    '''
    ji = JSInterpreter(js)
    res = ji.extract_object('a')
    assert res['b']('b') == 1
    assert res['c']('c') == 2



# Generated at 2022-06-14 17:57:07.592288
# Unit test for method call_function of class JSInterpreter

# Generated at 2022-06-14 17:57:11.216658
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    js1 = r'''
        function v(name, value) {
            return name + '=' + value;
        }
        function x(a, b) {
            return a + b;
        }
    '''
    interpreter = JSInterpreter(js1)
    assert('name=value' == interpreter.call_function('v', 'name', 'value'))
    assert(10 == interpreter.call_function('x', 2, 8))


# Generated at 2022-06-14 17:57:22.951939
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    js_interpreter = JSInterpreter('a = 2; b = a; var c = 12; b[c] = 13;')
    assert js_interpreter.interpret_expression('a', {}) == 2
    assert js_interpreter.interpret_expression('b', {}) == [None, None, None, None, None, None, None, None, None, None, None, None, 13]
    assert js_interpreter.interpret_expression('2', {}) == 2
    assert js_interpreter.interpret_expression('2.0', {}) == 2.0
    assert js_interpreter.interpret_expression('b[c]', {}) == 13
