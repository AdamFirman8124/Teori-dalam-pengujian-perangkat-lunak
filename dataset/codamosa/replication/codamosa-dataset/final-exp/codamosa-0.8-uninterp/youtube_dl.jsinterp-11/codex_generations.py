

# Generated at 2022-06-14 17:49:01.818161
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    js_code = r'''
        function what_am_i_doing_here() {
            var a = "what";
            var b = "the";
            var c = "fuck";
            return a + b + c;
        }
        var A = {
            "what": function(a) {
                return a + "?"
            },
            "the": function(a, b) {
                return a + b;
            },
            "fuck": function(a, b, c) {
                return a + b + c;
            }
        }
        var B = {
            "what": function() {
                return "what";
            },
            "the": function() {
                return "the";
            },
            "fuck": function() {
                return "fuck";
            }
        }'''
   

# Generated at 2022-06-14 17:49:13.678120
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    interpreter = JSInterpreter('', {})
    test_variables = {'test1':{'test11':[1,2,3]}}
    assert interpreter.interpret_expression('test1.test11[0]', test_variables, 100) == 1
    assert interpreter.interpret_expression('test1.test11[1]', test_variables, 100) == 2
    assert interpreter.interpret_expression('test1.test11[2]', test_variables, 100) == 3
    assert interpreter.interpret_expression('test1.test11.length', test_variables, 100) == 3
    test_variables = {'test1':['a','b','c']}
    assert interpreter.interpret_expression('test1.length', test_variables, 100) == 3

# Generated at 2022-06-14 17:49:19.244751
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    js_code = '''
        var b = 3, c = 5;
        var a = b + c;
    '''

    js_interpreter = JSInterpreter(js_code)
    assert js_interpreter.interpret_expression('a', locals()) == 8

# Generated at 2022-06-14 17:49:28.966493
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    js_interpreter = JSInterpreter("""
        var x1 = 1 + 2 * 3;
        var x2 = 1 * 2 + 3;
        var x3 = 1 * (2 + 3);
        var x4 = 1 + (2 * 3);
        var x5 = 'a' + 1;
        var x6 = 1 + 'a';
        var x7 = (1 + 2) * 3;
        var x8 = 1 << 3
        var x9 = '1' + '2'"""
    )
    assert js_interpreter.interpret_expression('x1', {}) == 7
    assert js_interpreter.interpret_expression('x2', {}) == 5
    assert js_interpreter.interpret_expression('x3', {}) == 5

# Generated at 2022-06-14 17:49:41.600084
# Unit test for method extract_function of class JSInterpreter
def test_JSInterpreter_extract_function():
    code = '''
        function test(a) {
            return a;
        }

        function test2(a,b) {
            return a+b;
        }

        function test3(a,b) {
            return a*b;
        }
    '''
    interpreter = JSInterpreter(code)
    assert interpreter.call_function('test', [1]) == 1
    assert interpreter.call_function('test2', [2, 3]) == 5
    assert interpreter.call_function('test3', [2, 3]) == 6
    interpreter = JSInterpreter(code)
    assert interpreter.call_function('test', (1,)) == 1
    assert interpreter.call_function('test2', (2, 3)) == 5
    assert interpreter.call_function('test3', (2, 3)) == 6


# Generated at 2022-06-14 17:49:51.730413
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    code = '''
        var obj1 = {
            a: function(p) {
                var q = p + 1;
                var r = p + q;
                return p + q + r;
            },
            b: function(p) {
                return p + 1;
            }
        };
        var obj2 = {
            c: function() {
                return 3;
            }
        };
        obj2.c;
    '''
    js_interpreter = JSInterpreter(code)
    obj1 = js_interpreter.extract_object("obj1")
    assert obj1["a"](1) == 15 and obj1["b"](1) == 2
    obj2 = js_interpreter.extract_object("obj2")
    assert obj2["c"]() == 3



# Generated at 2022-06-14 17:49:56.785451
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    code = """
        function test(a,b){
            var k, c, d;
            k = a + b;
            c = c + 1;
            d = c << 3;
            a = d;
            return a;
        }
    """
    js_interpreter = JSInterpreter(code)
    result = js_interpreter.call_function('test',5, 3)
    assert result == 40


# Generated at 2022-06-14 17:50:10.256448
# Unit test for method interpret_statement of class JSInterpreter
def test_JSInterpreter_interpret_statement():
    js = '''
        var f = {};
        var a = [100,200,300,400];
        var e = [500,600,700,800];
        var b = a[0]+a[1]+"_"+e[0]+e[1];
        var c = b.length;
        var d = b.slice(0);
        f.get = function (a) {
            var s = [a,b,c,d];
            if (a > 0) {
                return d[a-1];
            } else {
                return s;
            }
        };
    '''
    js_interpreter = JSInterpreter(js)
    f = js_interpreter.extract_function("get")

# Generated at 2022-06-14 17:50:20.424754
# Unit test for method interpret_expression of class JSInterpreter

# Generated at 2022-06-14 17:50:22.182447
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    # TODO: Add a dummy youtube video URL for testing
    #       (right now, we can not find a stable video)
    pass



# Generated at 2022-06-14 17:50:48.053043
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    # Parse a string into a JavaScript code
    js = JSInterpreter("""
        function func(pal) {
            str = "abcb"
            value1 = str.indexOf("c")
            value2 = str.indexOf("c", value1 + 1)
            return value1 + value2 + pal;
        }
    """)
    # The function func takes one argument and returns a value
    # The returned value is the sum of:
    # 1. The index of the first "c" in the string "abcb"
    # 2. The index of the second "c" in the string "abcb"
    # 3. The argument of the function
    assert js.call_function("func", 20) == 28


if __name__ == '__main__':
    test_JSInterpreter_call_function()

# Generated at 2022-06-14 17:50:56.196537
# Unit test for method build_function of class JSInterpreter

# Generated at 2022-06-14 17:51:06.941948
# Unit test for method interpret_expression of class JSInterpreter

# Generated at 2022-06-14 17:51:14.888741
# Unit test for method extract_function of class JSInterpreter
def test_JSInterpreter_extract_function():
    """
    test_JSInterpreter_extract_function
    """
    code = '''
    function hello(a, b) {
        return a * b;
    }
    '''
    js_interpreter = JSInterpreter(code)
    func = js_interpreter.extract_function('hello')
    assert func([1, 2]) == 2
    assert func([3, 4]) == 12


if __name__ == "__main__":
    test_JSInterpreter_extract_function()

# Generated at 2022-06-14 17:51:26.785788
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    code = ('var x = function(a){return a;},'
            'y = function(a,b){if(a==b){return a;}else{return b;}},'
            'z = function(a){return y(a,a);};')
    js = JSInterpreter(code)
    assert js.interpret_expression('z(1)', {}) == 1
    assert js.interpret_expression('z(1.0)', {}) == 1.0
    assert js.interpret_expression('z("1")', {}) == '1'
    assert js.interpret_expression('z(true)', {}) is True
    assert js.interpret_expression('z(false)', {}) is False
    assert js.interpret_expression('z([1,2,3])', {}) == [1, 2, 3]
    assert js

# Generated at 2022-06-14 17:51:28.990958
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    js = r'''var a = 'asdf'; var b = a[0] + 1;'''

    func = JSInterpreter(js)
    assert func.interpret_expression('a[0] + 1', {}) == 'a\x01'


# Generated at 2022-06-14 17:51:37.921115
# Unit test for method extract_function of class JSInterpreter

# Generated at 2022-06-14 17:51:46.750654
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    code = '''
    e=function(b){
        var a = 0;
        b = b.split("");
        while (a < b.length) {
            if (a % 2 == 0) {
                b[a] = 1;
            } else {
                b[a] = 0;
            }
            a++;
        }
        return b.join("");
    }
    '''
    js_interpreter = JSInterpreter(code)
    assert js_interpreter.interpret_expression('e("110010101")', {}) == "101010101"

# Generated at 2022-06-14 17:51:54.714624
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    js_code = """
    var a={b:1,c:2};
    var d="d";
    var f={e:d};
    """
    js_int = JSInterpreter(js_code)
    assert js_int.interpret_expression("a.b",{}) == 1
    assert js_int.interpret_expression("a['b']",{}) == 1
    assert js_int.interpret_expression("a.b + a.c",{}) == 3
    assert js_int.interpret_expression("a['b'] + a['c']",{}) == 3
    assert js_int.interpret_expression("f.e+'_str'",{}) == 'd_str'


if __name__ == '__main__':
    import nose
    nose.runmodule()

# Generated at 2022-06-14 17:52:07.875186
# Unit test for method interpret_statement of class JSInterpreter
def test_JSInterpreter_interpret_statement():
    js_code = '''
        +function(p, a, c, k, e, d) {
            e = function(c) {
                return c
            };
            if (!''[d] || !''[d](e)) {
                while (c--) {
                    if (k[c]) {
                        p = p[d](k[c])
                    }
                }
            }
            return p[d](e(a))
        }(
            "bok",
            "bok",
            bok,
            ["c", "e", "f", "g", "h", "i", "o", "s", "t"],
            0,
        )
    '''
    js_inter = JSInterpreter(js_code)

# Generated at 2022-06-14 17:52:31.598457
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    code = '''
        a = [];
        a[3] = 15;
        a[0] = a[3] + 5;
        a[1] = a[0] + a[3];
        a[2] = a[1] + a[3];
        var b = a.join('+');
        var c = b.split('+');
    '''
    interp = JSInterpreter(code)
    assert interp.call_function('', '') == None
    assert interp.call_function('', '20') == None
    assert interp.call_function('', '20,15') == None

if __name__ == '__main__':
    test_JSInterpreter_interpret_expression()
    print('all tests passed')

# Generated at 2022-06-14 17:52:37.110679
# Unit test for method interpret_statement of class JSInterpreter
def test_JSInterpreter_interpret_statement():
    js = """var x = 1;"""
    js_1 = js
    js_2 = """var x = 1;
var y = x + 1;"""
    js_3 = """var x = [1, 2, 3];
var y = x[0];"""
    js_4 = """var x = 1;
var y = x + 3;
var z = y + 5;"""
    js_5 = """var x = [1, 2, 3];
var y = x[0] + 1;
var z = y + x[1] + x[2];"""
    js_6 = """var a = 'hello';
var x = [1, 2, 3];
var y = x[0] + 1;
var b = a + y;
var z = b + x[1] + x[2];"""
    js

# Generated at 2022-06-14 17:52:43.401494
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    # Given
    arguments_array = ['a','b','c','d','e','f','g','h']
    code_string = 'new a[b](c,d)'

    # When
    resf = JSInterpreter.build_function(arguments_array, code_string)

    # Then
    assert resf(1,2,3,4) == {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Generated at 2022-06-14 17:52:54.184132
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    code = """var $=function(a){var b=function(a,b){if(a<b)var c=a;else var c=b;for(var d=c;d>=2;d--){if(a%d==0&&b%d==0)return d}return 1};var c=function(a,b){return a*b/b(a,b)};var d=function(a,b){return a(b)};return d(c,a)};"""
    interpreter = JSInterpreter(code)
    assert interpreter.interpret_expression("2", {}) == 2
    assert interpreter.interpret_expression("(2,3)", {}) == 3
    assert interpreter.interpret_expression("1>2?1:2", {}) == 2

# Generated at 2022-06-14 17:53:04.078796
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    # Scenario 1: input with only variables
    # Expected result: {"var1": "value1", "var2": "value2"}
    js_code = 'var var1 = "value1"; var var2 = "value2";'
    js_interpreter = JSInterpreter(js_code)
    local_vars = {}
    js_interpreter.interpret_expression(js_code, local_vars)
    assert local_vars == {"var1": "value1", "var2": "value2"}

    # Scenario 2: input with only primitive values
    # Expected result: {"var1": 1, "var2": 2}
    js_code = 'var var1 = 1; var var2 = 2;'
    js_interpreter = JSInterpreter(js_code)
    local_

# Generated at 2022-06-14 17:53:12.444838
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    js = '''
    var x = "bla";
    var y = 1;
    var z = [9, 8, 7];
    function f(a, b) {
        var d = 2;
        var e = a + y;
        var f = [3, 4, 5];
        return x.split('').reverse().join(b);
    }
    '''
    jsinterpreter = JSInterpreter(js)
    assert jsinterpreter.call_function('f', '', ',').strip() == 'alb'


# Generated at 2022-06-14 17:53:18.875051
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    interpreter = JSInterpreter("""
    function a(a, b){
        var c;
        c = a + b;
        return c;
    }
    """)
    assert interpreter.build_function(["a", "b"], "var c; c = a + b; return c;")(["a", "b"]) == "ab"


# Generated at 2022-06-14 17:53:29.416809
# Unit test for method interpret_statement of class JSInterpreter
def test_JSInterpreter_interpret_statement():
    js_code = '''
        var abc = 4;
        var cde = "abcd";
        var efg = "abcd".split("");
        function xyz(pqr){
            var def = pqr + abc;
            return def;
        }
    '''
    jsi = JSInterpreter(js_code)

    assert jsi.interpret_statement('abc = 2', {})[0] == 2
    assert jsi.interpret_statement('abc', {})[0] == 2
    assert jsi.interpret_statement('abc + 4', {})[0] == 2 + 4
    assert jsi.interpret_statement(
        'var ghi = abc', {})[0] == 2

# Generated at 2022-06-14 17:53:38.267458
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    jsinterpreter = JSInterpreter(
        code='''function foobar(a,b,c) { e = a+b-c; var d = a*b/c; return d; }''')
    func = jsinterpreter.build_function(
        argnames=['a','b','c'],
        code='''e = a+b-c; var d = a*b/c; return d;''')
    assert func([1,2,3]) == -2
    assert func([5,5,5]) == 2


# Generated at 2022-06-14 17:53:45.644297
# Unit test for method interpret_statement of class JSInterpreter
def test_JSInterpreter_interpret_statement():
    code = '''
    function test() {
        for (var f = 0; f < 10; f++)
            var b = f < 5 ? f * 5 : 20;
        return b + 5;
    }
    '''
    res = JSInterpreter(code).extract_function('test')(tuple([]))

    assert res == 30

if __name__ == '__main__':
    test_JSInterpreter_interpret_statement()

# Generated at 2022-06-14 17:54:28.117076
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    test_str = '''
        function sampleFunc(a, b){
            c = a + b;
            return c;
        }
    '''

    interp = JSInterpreter(test_str)
    assert interp.call_function('sampleFunc', 1, 2) == 3



# Generated at 2022-06-14 17:54:39.235295
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():

    # test translate_unicode_escape function
    js_code = u'''
        function _translate_unicode_escape(a){
            return String.fromCharCode(parseInt(a.slice(2), 16))
        }

        var a = '\\u8c46'

        _translate_unicode_escape(a)
    '''
    interpreter = JSInterpreter(js_code)
    assert interpreter.call_function('_translate_unicode_escape', u'\\u8c46') == '豆'

    # test slice_js_code function

# Generated at 2022-06-14 17:54:51.462237
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    code = """
            var a = 0;
            var b = 1;
            var c = 12;
            var d = [1, 2, 3]
            var r = a | b;
            var e = r + c
            var f = d.length;
            var g = d[0];
            var h = [e, r, f, g].join(' ');
            var i = h.split(' ');
            var j = i.reverse();
            var k = j.slice(1);
            var l = k[0];
            """
    interpreter = JSInterpreter(code)
    result = interpreter.interpret_expression("0 | 1", {})
    assert result == 1

    result = interpreter.interpret_expression("a | b", {})
    assert result == 1


# Generated at 2022-06-14 17:55:01.402644
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    code = (
        'var b;'
        'var d = function() {};'
        'var a = {'
        '    c: function() {},'
        '    e: function() {}'
        '};'
        'var f = {'
        '    g: function() {},'
        '    h: function() {}'
        '};'
        'var i = {'
        '    j: function() {},'
        '    k: function() {}'
        '};'
        'var k = function() {};'
        'var x = function() {};'
        'var y = {'
        '    u: function() {},'
        '    v: function() {}'
        '};'
    )
    js_interpreter = JSInterpreter(code)
    assert js_

# Generated at 2022-06-14 17:55:05.760222
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    JSInterpreter.build_function(['a','b','c'], '(function(){return a+b+c})();')

if __name__ == '__main__':
    test_JSInterpreter_build_function()

# Generated at 2022-06-14 17:55:13.277370
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    code = """
        my_func1 = function(a, b) {
            return a + b;
        }
        my_func2 = function(obj) {
            return obj.member;
        }
        """
    js_interpreter = JSInterpreter(code)
    assert js_interpreter.call_function("my_func1", 1, 2) == 3
    obj = {'member': 7}
    assert js_interpreter.call_function("my_func2", obj) == 7


if __name__ == '__main__':
    test_JSInterpreter_call_function()

# Generated at 2022-06-14 17:55:23.783026
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    jsi = JSInterpreter(None)
    local_vars = {
        'a': [1, 2, 3],
        'b': 4,
        'c': 5,
        'd': 6,
        'e': [],
        'f': {'g': None, 'k': {}},
    }

# Generated at 2022-06-14 17:55:33.005086
# Unit test for method call_function of class JSInterpreter

# Generated at 2022-06-14 17:55:42.546107
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    code = """
    function _v(n){
        var v='';
        for(var i=0;i<n.length;i++){
            v+=String.fromCharCode(n.charCodeAt(i)-1);
        }
        return v;
    }
    """
    jsi = JSInterpreter(code)
    assert jsi.call_function("_v", "qjmpq") == "pilop"

    code = """
    function _b(n){
        var v='';
        for(var i=0;i<n.length;i++){
            v+=String.fromCharCode(n.charCodeAt(i)+1);
        }
        return v;
    }
    """
    jsi = JSInterpreter(code)
    assert jsi.call_function

# Generated at 2022-06-14 17:55:51.180675
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    JSInterpreter = JSInterpreter

    def a(i):
        return i + 1
    def b(f):
        return lambda i: f(i) + 2
    def c(i, j):
        return i + j
    def d():
        return 42

    b_func = JSInterpreter.build_function(['f'], 'return f(a) + 2;')
    b_func_autocall = JSInterpreter.build_function(['f'], 'return f(a());')
    assert b_func(a) == 5
    assert b_func_autocall(a) == 4

    c_func = JSInterpreter.build_function(['i', 'j'], 'return i + j;')

# Generated at 2022-06-14 17:56:51.603810
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    code = '''\
    var obj1 = {
        a : function() {
            return;
        },
        b : function() {
            return;
        }
    }
    '''
    interpreter = JSInterpreter(code)
    obj1 = interpreter.extract_object('obj1')
    assert obj1['a']
    assert callable(obj1['a'])
    assert obj1['b']
    assert callable(obj1['b'])


# Generated at 2022-06-14 17:57:03.733006
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    js_interpreter = JSInterpreter('')
    f = js_interpreter.build_function([], '')
    assert f(()) == None

    f = js_interpreter.build_function([], 'a=10')
    assert f(()) == 10
    f = js_interpreter.build_function([], 'a=10; a=20')
    assert f(()) == 20

    f = js_interpreter.build_function([], 'a=10; return a;')
    assert f(()) == 10

    f = js_interpreter.build_function([], 'x=5; y=6; return x+y;')
    assert f(()) == 11

    f = js_interpreter.build_function([], 'return 1; return 2;')

# Generated at 2022-06-14 17:57:10.171129
# Unit test for method interpret_expression of class JSInterpreter

# Generated at 2022-06-14 17:57:19.315340
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    code = '''
        function func1() {}
        var func2 = function() {};
        var func3 = function func4() {};
        var func5 = function func6(a) { return a; };
        {
            function func7(a) { return a; };
        };
        var obj1 = {
            func8: function(a) { return a; },
            func9: function func10(a) { return a; },
        };
    '''
    jsi = JSInterpreter(code)
    func1 = jsi.build_function([], '')
    assert func1() is None
    func2 = jsi.build_function([], '')
    assert func2() is None
    func3 = jsi.build_function([], '')
    assert func3() is None
    func4

# Generated at 2022-06-14 17:57:26.507370
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    interpreter = JSInterpreter(r'''
        a = {
            a0: function(b){return b},
            a1: function(c){return c+"a"},
            a2: function(d){return d+1},
        }
    ''')
    a = interpreter.extract_object('a')
    assert a['a0']('test') == 'test'
    assert a['a1']('test') == 'testa'
    assert a['a2'](1) == 2

if __name__ == '__main__':
    test_JSInterpreter_extract_object()

# Generated at 2022-06-14 17:57:37.808504
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    code = """
		var a = function() {};
		a.b = function (c) {return c;};
	"""
    interpreter = JSInterpreter(code)
    assert interpreter.interpret_expression("a.b('d')", {}) == 'd'
    assert interpreter.interpret_expression("a.b(4)", {}) == 4

    code = """
		var a = ['d'];
	"""
    interpreter = JSInterpreter(code)
    assert interpreter.interpret_expression("a[0]", {}) == 'd'
    assert interpreter.interpret_expression("a.length", {}) == 1
    assert interpreter.interpret_expression("a.reverse()[0]", {}) == 'd'

    code = """
		var a = ['d', 'd2'];
	"""
    interpreter

# Generated at 2022-06-14 17:57:47.983464
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    interpreter = JSInterpreter('', {})

    def interpret_expression(expr, local_vars):
        return interpreter.interpret_expression(expr, local_vars, 100)

    assert interpret_expression('1', {}) == 1
    assert interpret_expression('true', {})

    local_vars = {'a': [1, 2], 'b': 3}
    assert interpret_expression('a[0]', local_vars) == 1
    assert interpret_expression('a[1]', local_vars) == 2
    assert interpret_expression('a.length', local_vars) == 2
    assert interpret_expression('a.join("")', local_vars) == '12'
    assert interpret_expression('a.join("0")', local_vars) == '1020'

# Generated at 2022-06-14 17:57:58.969407
# Unit test for method extract_object of class JSInterpreter