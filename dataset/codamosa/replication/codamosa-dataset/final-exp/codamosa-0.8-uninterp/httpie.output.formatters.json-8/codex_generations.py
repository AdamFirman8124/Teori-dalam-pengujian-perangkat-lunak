

# Generated at 2022-06-13 22:01:52.774358
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    json_formatter = JSONFormatter(explicit_json = False)
    assert json_formatter.format_body('{"test":true}', 'json') == \
        '{\n    "test": true\n}'
    assert json_formatter.format_body('{"test":true}', 'text') == \
        '{\n    "test": true\n}'
    assert json_formatter.format_body('{"test":true}', 'html') == \
        '{"test":true}'

# Generated at 2022-06-13 22:01:55.441721
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
	instance = JSONFormatter(default_options=None, quiet=None, format_options=None, colors=None, config_dir=None)

# Generated at 2022-06-13 22:01:56.149040
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    pass

# Generated at 2022-06-13 22:02:03.045171
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    body = "[{'username': 'Jane'}]"
    assert "[{u'username': u'Jane'}]" == JSONFormatter().format_body(body, 'json')
    assert "[{\"username\": \"Jane\"}]" == JSONFormatter().format_body(body, 'text')
    assert "[{'username': 'Jane'}]" == JSONFormatter().format_body('{"username": "Jane"}', 'javascript')

# Generated at 2022-06-13 22:02:09.800633
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    test_JSONFormatter=JSONFormatter(JSONFormatter,format_options={'json': {'format': True, 'indent': 4, 'sort_keys': True}})
    assert test_JSONFormatter
    assert test_JSONFormatter.enabled

# test the method format_body

# Generated at 2022-06-13 22:02:13.857795
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    s, mime = '{"foo": "bar", "baz": "qux"}', 'application/json'
    s_exp = '{\n    "baz": "qux",\n    "foo": "bar"\n}'
    j = JSONFormatter()
    assert j.format_body(body=s, mime=mime) == s_exp

# Generated at 2022-06-13 22:02:23.475265
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    json_formatter = JSONFormatter(
        format_options={'json': {'format': True, 'sort_keys': False, 'indent': 2}},
        explicit_json=False,
        pretty=False,
    )
    # Valid JSON
    body = '{"key": "value"}'
    mime = 'json'
    assert json_formatter.format_body(body, mime) == '{\n  "key": "value"\n}'
    mime = 'javascript'
    assert json_formatter.format_body(body, mime) == '{\n  "key": "value"\n}'
    # Invaild JSON
    body = '{"key": "value"'
    mime = 'json'

# Generated at 2022-06-13 22:02:33.377700
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    from httpie.context import Environment
    from httpie.compat import is_py26, is_windows
    env = Environment()
    jf = JSONFormatter(env=env)

    # Test output for positive case.
    response_json = {
        "code": 200,
        "result": [
            {
                "id": "1",
                "name": "test1"
            },
            {
                "id": "2",
                "name": "test2"
            }
        ]
    }
    response_json_str = json.dumps(response_json)
    parsed_body = jf.format_body(response_json_str, "application/json")
    assert parsed_body == response_json_str

    # Test output for negative case.
    response_text = "Hello, world!"


# Generated at 2022-06-13 22:02:37.130086
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    body = '{"abc": "def"}'
    mime = 'apllication/json'
    json_formatter = JSONFormatter()
    assert json_formatter.format_body(body, mime) == body

# Generated at 2022-06-13 22:02:50.347683
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    
    # i. default constructor
    try:
        formatter = JSONFormatter()
        assert formatter.format_options == dict() and \
               formatter.is_streaming == False and \
               formatter.should_pretty_print == False and \
               formatter.should_colors_be_disabled == False and \
               formatter.output_options == dict()
    except:
        assert False

    # ii. passing some parameters to constructor

# Generated at 2022-06-13 22:03:06.475555
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    from mock import Mock

    def set_format_options(req):
        req.format_options = {
            'json': {'format': True},
            'headers': {'format': None, 'sep': ': '},
            'regex': None,
            'colors': {
                'args': None,
                'bodies': None,
                'headers': None,
                'history': True,
                'json': None,
                'method': 'blue',
                'pretty': True,
                'status': None,
                'url': None,
            }
        }

    req = Mock()
    set_format_options(req)
    plugin = JSONFormatter(kwargs={'explicit_json': False}, options=req.format_options)

# Generated at 2022-06-13 22:03:16.042749
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    from httpie.context import Environment

    env = Environment(colors=256, stdin=True, stdout=True, v=True)
    json = JSONFormatter(env, format_options={'json': {}})
    json_pretty = JSONFormatter(env, format_options={'json': {'indent': 2, 'sort_keys': True}})

    # Content-Type: application/json
    # Content: {}
    body = '{}'
    assert json.format_body(body, 'application/json') == body
    assert json_pretty.format_body(body, 'application/json') == body

    # Content-Type: application/json
    # Content: {"id": 1, "text"="hello"}
    body = '{"id": 1, "text": "hello"}'

# Generated at 2022-06-13 22:03:17.702304
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    formatter = JSONFormatter()
    assert formatter.enabled == False

# Generated at 2022-06-13 22:03:28.812885
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    import json
    import pytest
    f = JSONFormatter(**{
        'pretty': {'colors': None},
        'format': {'format': True, 'json': {
            'indent': 2,
            'sort_keys': True
        }}
    })
    obj = {
        'foo': 'bar',
        'baz': {
            'one': 'two',
            'three': 'four five'
        }
    }
    body = json.dumps(obj=obj, indent=4)
    fmted = f.format_body(body, 'application/json')
    assert fmted == json.dumps(obj=obj, indent=2)
    assert f.format_body(body, 'text/html') == body

# Generated at 2022-06-13 22:03:40.424630
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # Initialize class object
    jsonformatter = JSONFormatter(**{'explicit_json':True, 'format_options':{'json':{'format':False,'indent':2,'sort_keys':False}}})
    # Case 1: mime='json' and body='{}'
    assert jsonformatter.format_body(body='{}',mime='json') == {}
    # Case 2: mime='javascript' and body='{}'
    assert jsonformatter.format_body(body='{}',mime='javascript') == {}
    # Case 3: mime='text' and body='{}'
    assert jsonformatter.format_body(body='{}',mime='text') == {}
    # Case 4: mime='invalid' and body='{}'
    assert jsonformatter.format

# Generated at 2022-06-13 22:03:47.910453
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    from httpie.input import ParseError
    from httpie.plugins.builtin import JSONFormatter

    formatter = JSONFormatter()

    # Parse JSON format
    body = '{"a": "b"}'
    assert formatter.format_body(body, 'application/json') == '{\n    "a": "b"\n}'
    assert formatter.format_body(body, 'text/javascript') == '{\n    "a": "b"\n}'

    # Parse JSON invalid
    body = '[{invalid}]'
    assert formatter.format_body(body, 'application/json') == '[{invalid}]'
    assert formatter.format_body(body, 'text/javascript') == '[{invalid}]'

    # JSON not parsed
    body = '<html></html>'


# Generated at 2022-06-13 22:03:59.036076
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    expected_result = '{"test": 1, "test2": 2, "test3": 3}'

    class TestJSONFormatter(JSONFormatter):
        pass

    formatter = TestJSONFormatter()
    formatter.format_options = {
        "json": {
            "format": False,
            "indent": 4,
            "sort_keys": True,
            "explicit_json": False
        }
    }
    formatter.kwargs = {}

    assert(formatter.format_body(
        "{\"test\": 1, \"test2\": 2, \"test3\": 3}",
        "json"
    ) == expected_result)

# Generated at 2022-06-13 22:04:11.397552
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter(format_options={"json": {"indent": 0}})
    assert formatter.format_body(body='{"name": "John"}', mime='application/json') == '{"name": "John"}'

    formatter = JSONFormatter(format_options={"json": {"indent": 4, "sort_keys": True}})
    assert (formatter.format_body(body='{"name": "John", "surname": "Doe"}', mime='application/json')) == \
           '{\n' \
           '    "name": "John",\n' \
           '    "surname": "Doe"\n' \
           '}'

    formatter = JSONFormatter(format_options={"json": {"indent": 0, "sort_keys": True}})

# Generated at 2022-06-13 22:04:16.889036
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
	assert JSONFormatter(None, None, None, None, None, None, None, None, None,
						 {'json': {'format': True, 'indent': 2, 'sort_keys': False}})

# Generated at 2022-06-13 22:04:18.756102
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    formatter = JSONFormatter()
    assert not formatter.enabled