

# Generated at 2022-06-14 17:48:49.463123
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    objects = {
        'a': [1, 2, 3],
        'b': 'foobar',
    }
    code = """
        var arkasha = {};
        arkasha.reverse = function() {
            a.reverse();
        };
        arkasha.length = function() {
            return b.length;
        };
        arkasha.splice = function(a) {
            return a.splice(1);
        };
    """
    assert JSInterpreter(code, objects).extract_object('arkasha') == {
        'splice': lambda x: x[1:],
        'reverse': lambda: objects['a'].reverse(),
        'length': lambda: len(objects['b']),
    }



# Generated at 2022-06-14 17:49:01.459033
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    js = JSInterpreter('var iabtk=function(){};')
    eq_(js.interpret_expression('iabtk', {}), None)
    eq_(js.interpret_expression('(iabtk)', {}), None)
    eq_(js.interpret_expression('iabtk()', {}), None)
    eq_(js.interpret_expression('(iabtk())', {}), None)

    js = JSInterpreter('var o={x: "a", y: function(){}};')
    eq_(js.interpret_expression('o.x', {}), 'a')
    eq_(js.interpret_expression('o.y', {}), None)
    eq_(js.interpret_expression('o.length', {}), 2)

    js = JSInterpreter('var v1=1;var v2="2";')

# Generated at 2022-06-14 17:49:10.458553
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    jsinterpreter = JSInterpreter('''
        a.control_function(function(i){
            if (i == 0)
                return "a";
            else if (i == 1)
                return "b";
            return "c"
        });
    ''')
    assert jsinterpreter.interpret_expression('1', {}) == 1
    assert jsinterpreter.interpret_expression('"xx"', {}) == 'xx'
    assert jsinterpreter.interpret_expression('(1)', {}) == 1
    assert jsinterpreter.interpret_expression('(1+2)', {}) == 3
    assert jsinterpreter.interpret_expression('1*2', {}) == 2
    assert jsinterpreter.interpret_expression('"a\"b"', {}) == 'a"b'

# Generated at 2022-06-14 17:49:14.204423
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    assert JSInterpreter('var b={"a":function(x){return x+a}};').extract_object('b') == {'a': lambda x: x + a}
    assert JSInterpreter('var b={"a":function(x,y){return x*y}};').extract_object('b') == {'a': lambda x, y: x * y}

# Generated at 2022-06-14 17:49:21.376012
# Unit test for method interpret_statement of class JSInterpreter
def test_JSInterpreter_interpret_statement():
    interpreter = JSInterpreter("if(a==3){return 1}else{return 2}")
    assert(interpreter.interpret_statement("if(a==3){return 1}else{return 2}",{"a":3})[0] == 1)
    assert(interpreter.interpret_statement("if(a==3){return 1}else{return 2}",{"a":4})[0] == 2)

# Generated at 2022-06-14 17:49:30.042184
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    code = 'function func1(arg1,arg2){var a=0;return arg1+arg2}'
    jsint_func1 = JSInterpreter(code)
    code_func1 = jsint_func1.build_function(['arg1','arg2'], 'var a=0;return arg1+arg2')
    assert code_func1(1,1) == 2

    code = 'var func2 = function(arg1,arg2){var a=0;return arg1+arg2}'
    jsint_func2 = JSInterpreter(code)
    code_func2 = jsint_func2.build_function(['arg1','arg2'], 'var a=0;return arg1+arg2')
    assert code_func2(1,1) == 2


# Generated at 2022-06-14 17:49:42.729931
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    js_code = """
          /*"asd".reverse()+"b"*/
          var xxx = "abcd"
          /*"asd".reverse()+"b"*/
          var yyy = xxx.split("")
          /*"asd".reverse()+"b"*/
          var zzz = yyy.reverse()
          /*"asd".reverse()+"b"*/
          var www = zzz.join("")
          /*"asd".reverse()+"b"*/
          var hhh = www + "b"
          """
    interpreter = JSInterpreter(js_code)
    result = interpreter.interpret_expression("123")
    assert result == 123
    result = interpreter.interpret_expression("'123'")
    assert result == '123'

# Generated at 2022-06-14 17:49:52.863659
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    interpreter = JSInterpreter('',{})
    assert interpreter.build_function([], "null")() == None
    # Test for operator +
    assert interpreter.build_function([], "1+1")() == 2
    assert interpreter.build_function(["x"], "x+1")(1) == 2
    # Test for operator -
    assert interpreter.build_function([], "1-1")() == 0
    assert interpreter.build_function(["x"], "x-1")(1) == 0
    # Test for operator >>
    assert interpreter.build_function([], "2>>1")() == 1
    assert interpreter.build_function(["x"], "x>>1")(2) == 1
    # Test for operator <<
    assert interpreter.build_function([], "2<<1")() == 4
    assert interpreter.build

# Generated at 2022-06-14 17:50:04.211016
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    print('unit test for method extract_object of class JSInterpreter')

    code = """
    var a = {
        b: function (c,d) {
            if (c) {
                d += e;
            }
        },
        c: function (d,e) {
            var a = [1, 2, 3];
            e += d;
            return a[0];
        }
    }
    """
    JSI = JSInterpreter(code)
    a = JSI.extract_object('a')
    print(a)
    assert a['b']('hello', 'world') == None
    assert a['b'](False, 1) == None
    assert a['c'](2, 3) == 1


# Generated at 2022-06-14 17:50:09.650709
# Unit test for method extract_function of class JSInterpreter
def test_JSInterpreter_extract_function():
    JSInterpreter_extract_function = JSInterpreter('''
    var f = function(x,y) {  
        return x;
    }
    ''').extract_function('f')
    assert JSInterpreter_extract_function([2,3]) == 2
test_JSInterpreter_extract_function()

# Generated at 2022-06-14 17:50:37.115831
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():

    js = JSInterpreter(code='', objects={})

# Generated at 2022-06-14 17:50:48.432567
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    JSI = JSInterpreter('')
    print('Running unit test for method build_function of class JSInterpreter')
    def test_func(argnames, code, expected_args, expected_result):
        print('Testing function %s with args %s and code %s' % (argnames, code, expected_args))

# Generated at 2022-06-14 17:51:00.427092
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    from .common import *
    from .extractor import *
    from collections import defaultdict

    for extractor_class in [YoutubeIE, YoutubePlaylistIE]:
        _RESOURCE_MAP = defaultdict(list)
        if extractor_class.ie_key() == 'YoutubePlaylist':
            p = extractor_class('PLwP_SiAcdui0KVebT0mU9Apz359a4ubsC')
            p.extract()
            assert 'tDvBwPzJ7dY' in _RESOURCE_MAP[extractor_class.ie_key()]
        else:
            p = extractor_class('https://www.youtube.com/watch?v=BaW_jenozKc')
            p.extract()
            assert 'BaW_jenozKc' in _

# Generated at 2022-06-14 17:51:08.698964
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    js = '''
        function someFunc(a, b) {
            return a + b;
        }
    '''
    js_interpreter = JSInterpreter(js)
    result = js_interpreter.call_function('someFunc', 1, 2)
    assert result == 3

if __name__ == '__main__':
    test_JSInterpreter_call_function()

# Generated at 2022-06-14 17:51:15.740447
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    code = """function test1(arg1,arg2,arg3) {
        var field2 = arg1;
        var field1 = arg1;
        var field3 = arg3;
        var field4 = arg3
    }"""
    inter = JSInterpreter(code)
    result = inter.call_function('test1', 10, 20, 30)
    assert result is None
# END Unit test for method call_function of class JSInterpreter


# Generated at 2022-06-14 17:51:27.340042
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    def assert_interpret(expr, expected_result, objects = None):
        interpreter = JSInterpreter('', objects)
        result = interpreter.interpret_expression(expr, {})
        assert result == expected_result, '%r != %r (from %r)' % (result, expected_result, expr)

    assert_interpret('2 + 3', 5)
    assert_interpret('2 + 3; 4 + 5; 8', 8)
    assert_interpret('x = 1 + 3; x', 4)
    assert_interpret('"as" + "df"', 'asdf')
    assert_interpret('-2', -2)
    assert_interpret('-2 + 3', 1)
    assert_interpret('3 + -2', 1)
    assert_interpret('3 - -2', 5)
    assert_interpret('[]', [])
   

# Generated at 2022-06-14 17:51:34.156891
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    code = '''
        function test1(arg1, arg2)
        {
            var testVal = arg1 + " - " + arg2;
            if (testVal == "some value - 123")
                return arg1 + arg2;
            else
                throw new Error("Wrong value for testVal");
        }
        '''
    js = JSInterpreter(code)
    f = js.build_function(['arg1', 'arg2'], '''
        var testVal = arg1 + " - " + arg2;
        if (testVal == "some value - 123")
            return arg1 + arg2;
        else
            throw new Error("Wrong value for testVal");
        ''')
    assert f(['some value', 123]) == 'some value123'

# Generated at 2022-06-14 17:51:43.790293
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    jsinterpreter = JSInterpreter('''var a=1; var b=1; var c=a+b; return c;''')
    assert jsinterpreter.interpret_expression('a+b', jsinterpreter.extract_object('[a, b, c]')) == 2
    assert jsinterpreter.interpret_expression('c', jsinterpreter.extract_object('[a, b, c]')) == 2


if __name__ == '__main__':
    test_JSInterpreter_interpret_expression()

# Generated at 2022-06-14 17:51:49.643107
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    code = """
    var obj = {
        a:1,
        b:function() { return this.a; },
        c:function(a,b) { if (a) { return b; } else { return ''; } },
        d:function() { return 'a' in this; },
        e:function() { return 'f' in this; },
        f:function(a) { return a; }
    };
    var func = function(a, b, c) {
        var abc = a - b + c;
        return abc;
    };
    """
    interpreter = JSInterpreter(code)
    assert interpreter.call_function('obj.b', {'a': 'some string'}) == 'some string'

# Generated at 2022-06-14 17:52:01.843677
# Unit test for method interpret_expression of class JSInterpreter

# Generated at 2022-06-14 17:52:31.693269
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    code = """
        x = new Object();
        x.foo = function() { return 'bar'; };
        x.alpha = [0x100, 0x200, 0x300];
        x.num = 42;
        x.sub = function(a, b) { return a - b; }
        var x.message = "hello world";
    """
    jsi = JSInterpreter(code)
    assert jsi.interpret_expression('x.foo()', {}) == 'bar'
    assert jsi.interpret_expression('x.sub(3,2)', {}) == 1
    assert jsi.interpret_expression('x.alpha[2]', {}) == 0x300
    assert jsi.interpret_expression('x.alpha[0]', {}) == 0x100

# Generated at 2022-06-14 17:52:35.337348
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    code = '''(function(a,b,c){var d,e,f;d=d||0;e=0===d?a[0]:a.b<c.length?a.slice(1,2):a.slice(3,4);f=f||0;return e.join(f)})("abcdef",10,2);'''
    interpreter = JSInterpreter(code)
    out = interpreter.interpret_expression(code, {})
    assert out == 'ab'

# Generated at 2022-06-14 17:52:46.842953
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    jsinterpreter = JSInterpreter('')
    assert jsinterpreter.interpret_expression('1') == 1
    assert jsinterpreter.interpret_expression('"1"') == '1'
    assert jsinterpreter.interpret_expression('true') == True
    assert jsinterpreter.interpret_expression('false') == False
    assert jsinterpreter.interpret_expression('var') is None
    assert jsinterpreter.interpret_expression('return') is None
    assert jsinterpreter.interpret_expression('1 + 1') == 2
    assert jsinterpreter.interpret_expression('2 - 1') == 1
    assert jsinterpreter.interpret_expression('2 * 3') == 6
    assert jsinterpreter.interpret_expression('8 / 4') == 2

# Generated at 2022-06-14 17:52:58.966972
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    code = '''
    var b=function(){}
    var a={
        split:function(b){return b.split("")},
        reverse:function(){},
        slice:function(b){return b.slice(0)},
        splice:function(a,b){this.length-=b},
        join:function(c){return this.join(c)}
    }
    '''
    js_interpreter = JSInterpreter(code)

    func = js_interpreter.build_function(['a'], '; return a;')
    assert func([5]) == 5

    func = js_interpreter.build_function(['b'], '; return b;')
    assert func([7]) == 7


# Generated at 2022-06-14 17:53:04.973622
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    js_interpreter = JSInterpreter('')
    local_var = {}
    assert js_interpreter.interpret_expression(
        r'(function(w,d,c){', local_var, 100) == None
    assert js_interpreter.interpret_expression(
        r'w.swfobject_embedSWF(c.SWF_NAME,"player_uid_95830553_1","669","377","9.0.115",{},{allowscriptaccess:"always",allowfullscreen:"true",wmode:"opaque"},{id:"player_uid_95830553_1",name:"player_uid_95830553_1"},{},"http://static.hdslb.com/play.swf",false)})(window,document,conf);', local_var, 100) == None
    assert js_

# Generated at 2022-06-14 17:53:15.126543
# Unit test for method interpret_expression of class JSInterpreter

# Generated at 2022-06-14 17:53:20.643310
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
	import sys

# Generated at 2022-06-14 17:53:24.286082
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    jsi = JSInterpreter('var url = function(a,b){return "youtube.com/"};')
    url = jsi.build_function(['a', 'b'], 'return "youtube.com/"')
    assert url(['a', 'b']) == "youtube.com/"

# Generated at 2022-06-14 17:53:35.366541
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    p = JSInterpreter('')
    assert p.interpret_expression('12', {}) == 12
    assert p.interpret_expression('1+3', {}) == 4
    assert p.interpret_expression('(1+3)', {}) == 4
    assert p.interpret_expression('(6-1)', {}) == 5
    assert p.interpret_expression('(1+3)*2', {}) == 8
    assert p.interpret_expression('6-1*2', {}) == 4
    assert p.interpret_expression('a=1', {'a': 10}) == 1
    assert p.interpret_expression('a', {'a': 10}) == 10
    assert p.interpret_expression('a', {'a': [10, 20]}) == [10, 20]

# Generated at 2022-06-14 17:53:47.563354
# Unit test for method interpret_expression of class JSInterpreter

# Generated at 2022-06-14 17:54:46.577525
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    interp = JSInterpreter("", {})
    assert interp.interpret_expression('6*7', {}, 100) == 42
    assert interp.interpret_expression('var abc = 6', {}, 100) == 6
    assert interp.interpret_expression('(function(){return 3}())', {}, 100) == 3
    assert interp.interpret_expression('abc*7', {'abc': 6}, 100) == 42


# Generated at 2022-06-14 17:54:55.391534
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    is_ok = True
    js_interpreter = JSInterpreter(None)
    # This is the test-cases for method interpret_expression of class JSInterpreter
    # return type of method is value
    code = '''var $b = "test"; $b;'''
    try:
        result = js_interpreter.interpret_expression(code, {'$b': "test"})
        if result != 'test':
            raise AssertionError('1')
    except AssertionError as e:
        print('test-case 1 failed')
        is_ok = False
        print(e)
    # $a = {'get': 1}
    code = '''$a.get;'''

# Generated at 2022-06-14 17:55:00.418527
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    code = '''
         function test(c){
         return function(t){
         return c(t)}
         };
         function test2(c,d){
         return c(d);
         };
         '''
    js = JSInterpreter(code)
    func = js.build_function(['c'],"var x=c(6); return x+7")
    assert func(6) == 13

# Generated at 2022-06-14 17:55:12.008638
# Unit test for method interpret_statement of class JSInterpreter
def test_JSInterpreter_interpret_statement():
    local_vars = {'a': 5, 'b': 6, 'c': 7}

# Generated at 2022-06-14 17:55:23.096006
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    js_code = '''
         var b = "";
         var a = {"x": "X", "y": "Y", "z": "Z"};
         var c = {"4": "4", "5": "5", "6": "6"};
         b += a.x;
         b += a["y"];
         b += a.z;
         b += c[4];
         b += c[5];
         b += c[6];
         b += "!";
    '''
    js_interpreter = JSInterpreter(js_code)
    assert js_interpreter.interpret_expression('b', {'b': ''}) == 'XYZ456!'

# Generated at 2022-06-14 17:55:32.779183
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    # Create a JSInterpreter Object
    js = JSInterpreter("""
        function b(c, a) {
            var d = a;
            var e = 0;
            while (e < c.length) {
                d = d[c[e]] || (a[c[e]] = []);
                e++
            }
            return d
        };
    """)

    # Call build_function method
    f = js.build_function(['c', 'a'], """
        var d = a;
        var e = 0;
        while (e < c.length) {
            d = d[c[e]] || (a[c[e]] = []);
            e++
        }
        return d
    """)

    # Assign the expected output
    expected = ["b", "c"]



# Generated at 2022-06-14 17:55:40.068732
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    test = """var f = function(a, b, c) {
        if (a == 0) {
            b = b + 10;
        } else {
            c = c + 15;
        }
        return c;
    }"""

    js_interp = JSInterpreter(test)
    f = js_interp.build_function(['a', 'b', 'c'], test[test.index('{'):])
    assert f((0, 10, 20)) == 35
    assert f((1, 10, 20)) == 20

# Generated at 2022-06-14 17:55:46.327517
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    interpreter = JSInterpreter(
        'function test(arg1, arg2){return arg1 + arg2;}')
    f = interpreter.build_function(['arg1', 'arg2'], 'return arg1 + arg2;')
    assert f([1, 2]) == 3

if __name__ == '__main__':
    import sys
    test_JSInterpreter_build_function()
    print('Tests passed')
    sys.exit(0)

# Generated at 2022-06-14 17:55:57.012478
# Unit test for method interpret_expression of class JSInterpreter

# Generated at 2022-06-14 17:56:07.933516
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    # First example
    js_code = """
    var s = "abcdef"
    function reverse(a, b) {
        var c;
        if (b) {
            c = a
            a = b
            b = c
        }
        return a.split('').reverse().join('')
    }
    var t = reverse(s, null)
    """
    js_interpreter = JSInterpreter(js_code)
    f = js_interpreter.build_function(["a", "b"], "return a.split('').reverse().join('');")
    assert f(["abcdef", None]) == "fedcba"

    # Second example

# Generated at 2022-06-14 17:56:32.726638
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    interpreter = JSInterpreter(None)
    # Test case 1
    expr = "i < e.length ? e.charCodeAt(i) : 0"
    local_vars = {
        "i": 0,
        "e": "Hello"
    }
    try:
        res = interpreter.interpret_expression(expr, local_vars, 100)
        assert res == ord('H')
    except Exception as err:
        raise Exception("Failed to interpret expression: %r" % expr)

    # Test case 2

# Generated at 2022-06-14 17:56:37.987434
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    print('Testing JSInterpreter.build_function...')
    jsint = JSInterpreter('');
    assert ('' == jsint.call_function('return_identity', ''));
    assert ('abc' == jsint.call_function('return_identity', 'abc'));



# Generated at 2022-06-14 17:56:43.368296
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    js_interp = JSInterpreter('function test(a, b, c, d) { return a + b * c + d; }')
    f = js_interp.build_function(['a', 'b', 'c', 'd'], 'return a + b * c + d;')
    assert f((0, 1, 2, 3)) == 5

# Generated at 2022-06-14 17:56:46.984353
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    interpreter = JSInterpreter(None)
    assert interpreter.interpret_expression(
        ' Math.round(3.5)  ', {}) == 4
    assert interpreter.interpret_expression(
        ' "3.5" + 2 ', {}) == '3.52'


# Generated at 2022-06-14 17:56:56.160320
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    interp = JSInterpreter(
        "a = function(p, a, c, k, e, d) { e = function(c) { return c; };"
        "if (!''.replace(/^/, String)) { while (c--) { d[c] = k[c] || c; } k = "
        "[function(e) { return d[e]; }]; e = function() { return '\\\\w+'; }; c = 1; }"
        ";while (c--) { if (k[c]) { p = p.replace(new RegExp('\\\\b' + e(c) + '\\\\b', 'g'), k[c]); } }"
        "return p; };")

# Generated at 2022-06-14 17:57:05.479093
# Unit test for method interpret_statement of class JSInterpreter
def test_JSInterpreter_interpret_statement():
    s = JSInterpreter('return [1,2,3];')
    assert (s.interpret_statement('[1,2,3];', {})[0] == [1,2,3])
    assert (s.interpret_statement('var obj={"a":"b"};', {})[0] == {"a":"b"})
    assert (s.interpret_statement('var x = {a: b};', {"b":2})[0] == {"a":2})
    assert (s.interpret_statement('var a=1;a+1;', {})[0] == 2)
    assert (s.interpret_statement('var x = 1;return x;', {})[0] == 1)
    assert (s.interpret_statement('return x;', {"x":1})[0] == 1)

# Generated at 2022-06-14 17:57:14.642308
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    jsi = JSInterpreter('')
    assert jsi.interpret_expression('1 + 1', {}) == 2
    assert jsi.interpret_expression('1 + 1 + 1 + 1', {}) == 4
    assert jsi.interpret_expression('1 + 1 + 1 + 1 - 1', {}) == 3
    assert jsi.interpret_expression('1 + 1 + 1 + 1 - 1 - 1', {}) == 2
    assert jsi.interpret_expression('1 + 1 + 1 + 1 - 1 - 1 - 1', {}) == 1
    assert jsi.interpret_expression('1 + 1 + 1 + 1 - 1 - 1 - 1 < 2', {}) == True
    assert jsi.interpret_expression('1 + 1 + 1 + 1 - 1 - 1 - 1 >= 2', {}) == False

# Generated at 2022-06-14 17:57:23.204509
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    jsInte = JSInterpreter('', {'b': 8})
    assert jsInte.interpret_expression('a', {'a': 1}) == 1
    assert jsInte.interpret_expression('a + 1', {'a': 1}) == 2
    assert jsInte.interpret_expression('a - 1', {'a': 1}) == 0
    assert jsInte.interpret_expression('a | 1', {'a': 1}) == 1
    assert jsInte.interpret_expression('a ^ 1', {'a': 1}) == 0
    assert jsInte.interpret_expression('a & 1', {'a': 1}) == 1
    assert jsInte.interpret_expression('a + 1 - 1', {'a': 1}) == 1

# Generated at 2022-06-14 17:57:30.478071
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():

    def test_run(code, function_name, function_arguments, assert_val):
        js_interpreter = JSInterpreter(code)
        res = js_interpreter.call_function(function_name, *function_arguments)
        assert res == assert_val

    # Aggregate test run

# Generated at 2022-06-14 17:57:33.018218
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    JSInterpreter.build_function(JSInterpreter, argnames = ["abc", "def"], code = "abc = 1; return abc")

_LOG = {}
