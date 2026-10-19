

# Generated at 2022-06-13 22:01:56.547541
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    my_JSONFormatter = JSONFormatter(explicit_json=True)
    my_JSONFormatter.format_options = {
        'json': {
            'format': True,
            'sort_keys': True,
            'indent': 4
        }
    }
    assert my_JSONFormatter.format_body('{"a": 1}', 'json') == '{\n    "a": 1\n}'
    assert my_JSONFormatter.format_body('{"a": 1,"b": 2}', 'json') == '{\n    "a": 1,\n    "b": 2\n}'
    assert my_JSONFormatter.format_body('{"a": 1,"b": 2}', 'json') == '{\n    "a": 1,\n    "b": 2\n}'
    assert my

# Generated at 2022-06-13 22:02:02.741388
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    assert JSONFormatter().format_body("{}", 'application/json') == "{}"
    assert JSONFormatter(format_options={'json':{'indent':4, 'sort_keys':True}}).format_body("{}", 'application/json') == "{\n    \"sort_keys\": true\n}"

# Generated at 2022-06-13 22:02:18.886261
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    json_formatter = JSONFormatter()
    # Content-Type: application/json
    body_json = ('{"message": "{\'hello\':\'world\'}"}')
    assert json_formatter.format_body(body_json, "application/json") == '{\n    "message": "{\'hello\':\'world\'}"\n}' 
    # Content-Type: application/json_DOM
    body_json_DOM = ('{"message": "{\'hello\':\'world\'}"}')
    assert json_formatter.format_body(body_json_DOM, "application/json_DOM") == '{\n    "message": "{\'hello\':\'world\'}"\n}' 
    # Content-Type: application/json2

# Generated at 2022-06-13 22:02:27.009892
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # a test case for invalid JSON
    f = JSONFormatter({'json': {'format': True, 'indent': 4, 'sort_keys': True}})
    assert f.format_body('{"a": 1, ', 'application/json') == '{"a": 1, '
    # a test case for valid JSON
    assert f.format_body('{"a": 1, "b": 2}', 'application/json') == '{\n    "a": 1,\n    "b": 2\n}'

# Generated at 2022-06-13 22:02:30.916412
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    body = '{"a":1}'
    formatter = JSONFormatter()
    output = formatter.format_body(body,'json')
    assert output == body

# Generated at 2022-06-13 22:02:42.087703
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    obj = [
        {"a": "2", "b": 1, "c": "c"} 
    ]

    obj_string = [
        '{"a": "2", "b": 1, "c": "c"}'
    ]

    obj_keysorted_string = [
        '{"a": "2", "b": 1, "c": "c"}'
    ]
    

    f_plugin = JSONFormatter(
        format_options={
            'json': {
                'format': True,
                'sort_keys': True,
                'indent': 2
            }
        },
        explicit_json=False,
    )


# Generated at 2022-06-13 22:02:54.125451
# Unit test for method format_body of class JSONFormatter

# Generated at 2022-06-13 22:03:02.449353
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    # Create JSONFormatter instance.
    json_formatter = JSONFormatter(format_options={'json': {'sort_keys':True, 'indent':4, 'format':True}})
    assert json_formatter.format_options['json']['sort_keys'] == True
    assert json_formatter.format_options['json']['indent'] == 4
    assert json_formatter.format_options['json']['format'] == True


# Generated at 2022-06-13 22:03:10.347046
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    """Test for JSONFormatter class method format_body."""
    json_formatter = JSONFormatter()
    assert json_formatter.format_body(body=
    '{"name": "Python"}',
    mime='application/json') == '{\n' \
                                '    "name": "Python"\n' \
                                '}'
    assert json_formatter.format_body(body=
    '{"name": "Python", "version": 2.7}',
    mime='application/json') == '{\n' \
                                '    "name": "Python",\n' \
                                '    "version": 2.7\n' \
                                '}'

# Generated at 2022-06-13 22:03:14.843426
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    body = '{"a":1}'
    mime = 'application/json'
    expected = '{\n  "a": 1\n}'
    assert JSONFormatter().format_body(body, mime) == expected

# Generated at 2022-06-13 22:03:24.280721
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    json_f = JSONFormatter(formatting_options={}, color_scheme={}, **{})
    assert json_f.enabled == True

# Generated at 2022-06-13 22:03:37.944398
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    f = JSONFormatter(format_options={'json': {'format': True, 'indent': 4, 'sort_keys': False}})
    assert f.format_body('{"a": "b"}', 'json') == '{\n    "a": "b"\n}'
    assert f.format_body(r'{"a": "b\u0021"}', 'json') == '{\n    "a": "b!"\n}'
    assert f.format_body(r'{"a": "b"}', 'javascript') == '{\n    "a": "b"\n}'
    assert f.format_body('{"a": "b"}', 'text') == '{\n    "a": "b"\n}'

# Generated at 2022-06-13 22:03:47.723124
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    from httpie.compat import is_py3
    import json

    test_cases = [
        ('{ "a": "b" }', 'application/json', '{"a": "b"}'),
        ('{ "a": "b" }', 'text/html', '{ "a": "b" }'),
        ('Nothing to format', 'text/html', 'Nothing to format'),
        ('<a>', 'text/html', '<a>'),
    ]
    if not is_py3:
        test_cases.append(
            (u'{ "привет": "мир" }', 'application/json',
             u'{"привет": "мир"}'))


# Generated at 2022-06-13 22:03:59.025635
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter(explicit_json = True, format_options = {'json': {'format': True}})
    # Testing with valid JSON
    body = '{"some": "test", "more": "test"}'
    mime = 'json'
    expected = '''{
    "more": "test",
    "some": "test"
}'''
    assert(formatter.format_body(body, mime) == expected)
    # Testing with valid JSON
    body = '{"some": "test", "more": "test"}'
    mime = 'application/json'
    expected = '''{
    "more": "test",
    "some": "test"
}'''
    assert(formatter.format_body(body, mime) == expected)
    # Testing with valid JSON but an

# Generated at 2022-06-13 22:04:04.064818
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    formatter = JSONFormatter(
        **{'json':
           {'format': True,
            'sort_keys': True,
            'indent': 2},
           'explicit_json': True})
    assert(formatter is not None)


# Generated at 2022-06-13 22:04:14.703596
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter(
        stdout=None,
        format_options={
            "json": {"format": True, "indent": 2, "sort_keys": True},
        },
        explicit_json=False,
        style=None,
        colors=None
    )
    body = '{"key": "value"}'
    mimes = [
        'application/json+something-else',
        'application/javascript',
        'application/something-else+json',
        'text/javascript',
        'something-else/json+something-else'
    ]
    for mime in mimes:
        assert formatter.format_body(body, mime) == (
            '{\n'
            '  "key": "value"\n'
            '}'
        )

# Generated at 2022-06-13 22:04:27.517241
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    import json
    from httpie.plugins import FormatterPlugin
    test_input = json.loads('{"hello":"world"}')
    test_input_string = json.dumps(test_input)
    test_output_string = json.dumps(
                obj=test_input,
                sort_keys=False,
                ensure_ascii=False,
                indent=4
            )

    # Test input and output as str objects
    test_class = JSONFormatter(stream=False, explicit_json=True, format_options={'json': {'format': True, 'sort_keys': False, 'indent': 4}})
    assert test_class.format_body(test_input_string, "application/json") == test_output_string, "Error in test_JSONFormatter_format_body_as_str"

   

# Generated at 2022-06-13 22:04:29.584620
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    assert isinstance(JSONFormatter(), JSONFormatter)


# Generated at 2022-06-13 22:04:32.100533
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    f = JSONFormatter()
    assert (f.format_options['json']['format'] == True)


# Generated at 2022-06-13 22:04:42.630376
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    jf = JSONFormatter(format_options=dict(json=dict(format=True, indent=4, sort_keys=True)),
                       explicit_json=False,
                       pretty=True)
    assert jf.format_body('{"12":14}', 'application/json') == '{\n    "12": 14\n}'
    assert jf.format_body('{"12":14}', 'invalid') == '{"12":14}'
    assert jf.format_body('{"12":14}', 'application/javascript') == '{\n    "12": 14\n}'
    jf = JSONFormatter(format_options={},
                       explicit_json=True,
                       pretty=True)

# Generated at 2022-06-13 22:05:04.807162
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # Test case 1:
    body = '{"a": "b"}'
    mime = 'application/json'
    assert JSONFormatter(
        format_options={
            'json': {
                'format': True,
                'indent': 2,
                'sort_keys': True
            }
        },
        explicit_json=False
    ).format_body(body, mime) == '{\n  "a": "b"\n}'

    # Test case 2:
    body = '{"a": "b"}'
    mime = 'application/javascript'
    assert JSONFormatter(
        format_options={
            'json': {
                'format': True,
                'indent': 2,
                'sort_keys': True
            }
        },
        explicit_json=False
    ).format_

# Generated at 2022-06-13 22:05:14.900382
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # Given
    formatter = JSONFormatter()

# Generated at 2022-06-13 22:05:26.112867
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    f = JSONFormatter()
    assert f.format_body('{"foo":"bar"}', 'json') == '{\n    "foo": "bar"\n}'
    assert f.format_body('{"foo":"bar"}', 'text') == '{\n    "foo": "bar"\n}'
    assert f.format_body('{"foo":"bar"}', 'html') == '{"foo":"bar"}'
    assert f.format_body('invalid json', 'application/json') == 'invalid json'


__all__ = ('JSONFormatter',)

# Generated at 2022-06-13 22:05:31.843976
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    json_formatter = JSONFormatter()
    assert json_formatter.format_body('{"a": [1, 2, 3], "b": {"c": "d"}}', '') == '''{
    "a": [
        1,
        2,
        3
    ],
    "b": {
        "c": "d"
    }
}'''

# Generated at 2022-06-13 22:05:41.156192
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter()
    assert formatter.format_body(
            body = '{"some": "json"}',
            mime = 'application/json') == '{\n    "some": "json"\n}'
    assert formatter.format_body(
            body = '{"some": "json"}',
            mime = 'application/javascript') == '{\n    "some": "json"\n}'
    assert formatter.format_body(
            body = '{"some": "json"}',
            mime = 'application/text') == '{\n    "some": "json"\n}'
    assert formatter.format_body(
            body = '{"some": "json"}',
            mime = 'application/csv') == '{"some": "json"}'

# Generated at 2022-06-13 22:05:51.075048
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    parser_kwargs = {'explicit_json': False, 'json': {'indent': 4, 'sort_keys': False}}
    json_formatter = JSONFormatter(**parser_kwargs)
    # Test that body is formatted using json.dumps
    assert json_formatter.format_body("""{"a": ["b", "c"]}""", 'json') == """{
    "a": [
        "b",
        "c"
    ]
}"""
    # Test that body is not formatted using json.dumps
    assert json_formatter.format_body("""{"a": ["b", "c"]}""", 'html') == """{"a": ["b", "c"]}"""
    # Test that body is formatted using json.dumps if mime is "text"
    assert json_formatter.format

# Generated at 2022-06-13 22:05:59.322719
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    from httpie.output.formatters.utils import get_response
    from httpie.plugins import BuiltinPluginManager
    builtin_pm = BuiltinPluginManager()
    plugin_context = {
        'stdin_isatty': True,
        'output_options': {},
    }
    pm = builtin_pm.filter(plugin_context)
    response = get_response('https://httpbin.org/json', 'GET', pm)
    formatter = JSONFormatter(**plugin_context)
    assert formatter.format_body(response.raw, 'json') is not None

# Generated at 2022-06-13 22:06:05.771404
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # given
    formatter_plugin = JSONFormatter(format_options={
        'json': {
            'format': True,
            'indent': 4,
            'sort_keys': True,
        },
    })

    # when
    body = formatter_plugin.format_body(
        body='["foo", {"bar":["baz", null, 1.0, 2]}]',
        mime='application/json',
    )

    # then
    assert json.loads(body) == \
        [u"foo", {u"bar": [u"baz", None, 1.0, 2]}]

# Generated at 2022-06-13 22:06:15.202989
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    jsonformatter = JSONFormatter(format_options={'json': {'indent': 2, 'sort_keys': False, 'format': True}})

    # Normal JSON, should be parsed and indented
    body = '{"title": "Hello", "message": "This is a test"}'
    assert(jsonformatter.format_body(body, 'application/json') == '{\n  "title": "Hello",\n  "message": "This is a test"\n}')

    # Invalid JSON, should be ignored and unchanged
    body = '{"title": "Hello", "message": "This is a test"'
    assert(jsonformatter.format_body(body, 'application/json') == body)

    # This is not a JSON, should be ignored and unchanged

# Generated at 2022-06-13 22:06:26.146682
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter()
    assert not formatter.enabled, "default JSONFormatter should be disabled"
    # Testing format_body, with explicit_json set to False
    assert formatter.format_body(b"", 'application/json') == ""
    assert formatter.format_body(b"a", 'application/json') == "a"
    assert formatter.format_body(b"{}", 'application/json') == "{}"
    assert formatter.format_body(
        b'{"toto":{"titi":3}}', 'application/json') == '{"toto": {"titi": 3}}'
    # Testing format_body, with explicit_json set to True
    formatter.kwargs['explicit_json'] = True
    assert formatter.format_body(b"", 'application/json') == ""

# Generated at 2022-06-13 22:07:02.269935
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter()
    assert (
        formatter.format_body('{"a": 1, "b": 2}', 'application/json') ==
        '{\n    "a": 1,\n    "b": 2\n}'
    )
    assert (
        formatter.format_body('{"a": 1, "b": 2}', 'application/javascript') ==
        '{\n    "a": 1,\n    "b": 2\n}'
    )
    assert (
        formatter.format_body('{"a": 1, "b": 2}', 'text/javascript') ==
        '{\n    "a": 1,\n    "b": 2\n}'
    )

# Generated at 2022-06-13 22:07:11.651530
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # Test with a valid JSON
    body = '''{"name": "httpie", "description": "HTTPie is a CLI, cURL-like tool for humans."}'''
    formatted_body = JSONFormatter().format_body(body, 'text/json')
    assert formatted_body == '''{
    "name": "httpie",
    "description": "HTTPie is a CLI, cURL-like tool for humans."
}'''
    formatted_body = JSONFormatter().format_body(body, 'text/javascript')
    assert formatted_body == '''{
    "name": "httpie",
    "description": "HTTPie is a CLI, cURL-like tool for humans."
}'''
    formatted_body = JSONFormatter().format_body(body, 'application/json')

# Generated at 2022-06-13 22:07:22.682918
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    class JSONFormatter1(JSONFormatter):
        def __init__(self):
            super().__init__()
            self.format_options['json'] = {
                'format': True,
                'sort_keys': False,
                'indent': 4
            }
    body1 = '{"name": "John", "age": 31}'
    mime1 = 'json'
    body1_expected = '{\n    "age": 31,\n    "name": "John"\n}'
    json_formatter1 = JSONFormatter1()
    assert body1_expected == json_formatter1.format_body(body1, mime1)
    body2 = '{"name": "John", "age": 31}'
    mime2 = 'text'
    json_formatter2 = JSONFormatter1

# Generated at 2022-06-13 22:07:34.105736
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter(format_options={'json': {'format': True, 'indent': None, 'sort_keys': False}})
    assert formatter.format_body('{"a":1}', 'json') == '{"a":1}'
    assert formatter.format_body('{"a":1}', 'javascript') == '{"a":1}'
    assert formatter.format_body('{"a":1}', 'text') == '{"a":1}'
    assert formatter.format_body('{"a":1}', '') == '{"a":1}'
    assert formatter.format_body('{"a":1}', 'unknown') != '{"a":1}'
    assert formatter.format_body('{"a":1}', 'unknown') == '{"a":1}'

# Generated at 2022-06-13 22:07:44.937096
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    json_formatter = JSONFormatter(None, None, None, None, None)
    json_formatter.format_options['json']['format'] = True
    json_formatter.format_options['json']['indent'] = 2
    json_formatter.format_options['json']['sort_keys'] = True
    json_formatter.kwargs['explicit_json'] = False

    json_string = '{"a": 1, "b": {"a": 3, "b": 4}}'
    formatted_json = json_formatter.format_body(json_string, 'json')
    assert formatted_json == '{\n  "a": 1,\n  "b": {\n    "a": 3,\n    "b": 4\n  }\n}'

# Generated at 2022-06-13 22:07:53.264309
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    class MockJSONFormatter:
        def __init__(self, **kwargs):
            self.kwargs = kwargs
            self.format_options = {
                'json': {
                    'format': True,
                    'sort_keys': True,
                    'indent': 2,
                }
            }

    body = '{"name": "Foo", "rank": 10}'

    formatter = MockJSONFormatter(explicit_json=False, json_indent=2)
    new_body = JSONFormatter.format_body(formatter, body, 'application/json')
    assert new_body == '{\n  "name": "Foo",\n  "rank": 10\n}'


    formatter = MockJSONFormatter(explicit_json=True, json_indent=2)
    new_

# Generated at 2022-06-13 22:08:02.502012
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    mock = {
        'format_options': {
            'json': {
                'sort_keys': True,
                'format': True,
                'indent': 2
            }
        }
    }
    formatter = JSONFormatter(**mock)

    mock_response = '{"response": "first response"}'
    expected_response = '{\n  "response": "first response"\n}'

    assert formatter.format_body(mock_response, '') == expected_response


# Generated at 2022-06-13 22:08:09.864073
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter(format_options={'json': {'format': True, 'indent': 2, 'sort_keys': True}})
    body = '{"c": 3, "b": [2, 4], "a": 1}'
    mime = 'json'
    expected_body = '{\n  "a": 1, \n  "b": [\n    2, \n    4\n  ], \n  "c": 3\n}'
    assert formatter.format_body(body, mime) == expected_body

# Generated at 2022-06-13 22:08:20.447186
# Unit test for method format_body of class JSONFormatter

# Generated at 2022-06-13 22:08:31.353993
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # Test cases:
    # (1) Body is a string that is valid JSON
    #       - Indent keys by 4 space
    #       - Sort keys
    #       - Avoid unicode escapes
    # (2) Body is invalid JSON
    #       - Ignore

    formatter = JSONFormatter(format_options={'json': {'format': True,
                                                        'indent': 4,
                                                        'sort_keys': True}},
                              explicit_json=True,
                              colors=False,
                              styles=None)

    # Test case (1)
    body = '{"key_1": "value_1", "key_2": "value_2"}'
    mime = 'json'

# Generated at 2022-06-13 22:09:03.894872
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    """
    Test that the function JSONFormatter.format_body works as expected
    """
    import json
    import os
    import sys
    import unittest

    # Search path for tests.json file
    # Set of directories to look in when searching for `tests.json`
    TEST_DIRECTORIES = [
        os.curdir,
        os.path.join(os.curdir, 'tests', 'data'),
        os.path.join(os.curdir, 'httpie', 'tests', 'data'),
    ]

    # Look for the `tests.json` file.
    for test_directory in TEST_DIRECTORIES:
        test_file = os.path.join(test_directory, 'tests.json')
        if os.path.exists(test_file):
            TESTS_

# Generated at 2022-06-13 22:09:14.858703
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    json_formatter = JSONFormatter(format_options={
        'json': {
            'format': True,
            'indent': 4,
            'sort_keys': True,
        }
    }, explicit_json=False,
        stdin=None,
        stdin_isatty=False,
        stdout=None,
        stderr=None)

# Generated at 2022-06-13 22:09:23.944101
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter()
    assert not formatter.enabled
    assert formatter.format_body('abc', 'abc') == 'abc'
    assert formatter.format_body('abc', 'json') == 'abc'
    formatter.enabled = True
    assert formatter.format_body('abc', 'json') == '"abc"'
    assert formatter.format_body('{"abc": 1}', 'json') == '{"abc": 1}'

    formatter.enabled = False
    assert formatter.active
    formatter.enabled = True
    formatter.format_options['json']['format'] = False
    assert not formatter.active
    formatter.format_options['json']['format'] = True
    assert formatter.active
    formatter.format_options['json']['indent'] = 2

# Generated at 2022-06-13 22:09:32.691483
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    class FakeRequest():
        def __init__(self, kwargs):
            self.kwargs = kwargs

    class FakeResponse():
        def __init__(self, status_code, headers):
            self.status_code = status_code
            self.headers = headers

    # Case 1
    request = FakeRequest({})
    response = FakeResponse(200, {})
    fake_body_1 = '{"a": 1}'
    formatter_plugin = JSONFormatter(
        request=request, response=response, format_options={},
    )
    formatter_plugin.enabled = False
    assert formatter_plugin.format_body(
        body=fake_body_1, mime='json',
    ) == fake_body_1

    # Case 2
    request = FakeRequest({})
    response = Fake

# Generated at 2022-06-13 22:09:41.242745
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    from httpie.core import main
    from httpie.plugins import JSONFormatter

    response = main._sessions.get("https://cloud.google.com/storage/docs/json_api/v1/objects/bucket/object/").response
    assert response.request.headers['Content-Type'] == "text/html; charset=utf-8"
    response.request.headers['Content-Type'] = "application/json"
    assert JSONFormatter().format_body(response.text, response.request.headers['Content-Type'])

    #assert JSONFormatter().format_body("""{"id": 1}""", response.request.headers['Content-Type']) == '{\n    "id": 1\n}'

# Generated at 2022-06-13 22:09:48.752131
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # Given
    line = '{"password": "12345678", "email": "admin@admin.com"}'
    mime = 'json'
    body = line

    # When
    json_formatter = JSONFormatter(format_options={'json': {'format': 'True'}})
    result = json_formatter.format_body(body, mime)

    # Then
    expected = '{\n    "email": "admin@admin.com",\n    "password": "12345678"\n}'
    assert result == expected

# Generated at 2022-06-13 22:10:01.348185
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter()
    non_json = (
        b'{"test_key": "\xc3\xb6\xc3\xa4"}',
        '{"test_key": "ÖÄ"}',
        '{"test_key": "\xc3\xb6\xc3\xa4"}'
    )
    # JSON, indented
    assert(
        formatter.format_body(
            body=non_json[0], 
            mime='application/json',
        ) == '{\n    "test_key": "\\u00f6\\u00e4"\n}'
    )
    # JSON, not indented
    formatter.format_options['json']['indent'] = None

# Generated at 2022-06-13 22:10:10.936945
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    import httpie.cli.formatters
    httpie.cli.formatters.JSONFormatter.kwargs['explicit_json'] = False
    JSONFormatter.kwargs['explicit_json'] = True
    # An URL with a body that is not JSON should not be reformatted
    assert JSONFormatter.format_body("hello world", 'text/plain') == "hello world"
    # An URL with a body that is JSON should be reformatted
    assert JSONFormatter.format_body('{"hello":"world"}', 'application/json') == '{\n\t"hello": "world"\n}'
    # An URL with a body that is not JSON but has a mimetype with the token 'json' should be reformatted

# Generated at 2022-06-13 22:10:14.540306
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    jf = JSONFormatter()
    obj = {
        "name": "Joe",
        "surname": "Doe",
        "age": 42,
        "friends": ["Mary", "John"],
        "skills": [
            {"name": "Python", "level": 5},
            {"name": "Java", "level": 3},
        ],
    }
    obj_str = json.dumps(obj=obj, sort_keys=True)

    assert jf.format_body(obj_str, 'json') == obj_str
    assert jf.format_body(obj_str, 'json; charset=utf-8') == obj_str
    assert jf.format_body(obj_str, 'application/json') == obj_str

# Generated at 2022-06-13 22:10:24.049751
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter()

    body = '{"json":"my_json_value"}'
    assert formatter.format_body(body=body, mime='application/json') == body

    body = '{"json":"my_json_value"}'
    assert formatter.format_body(body=body, mime='text/javascript') == body

    body = '{"json":"my_json_value"}'
    assert formatter.format_body(body=body, mime='text/plain') == body

    body = '{"json":"my_json_value"}'
    assert formatter.format_body(body=body, mime='text/html') == body

    body = '{"json":"my_json_value"}'
    assert formatter.format_body(body=body, mime='application/xml') == body



# Generated at 2022-06-13 22:11:12.525488
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # Test whether a json object is correctly formatted as string
    my_obj = {'a': 1, 'b': 2, 'c': 3}
    my_string = json.dumps(obj=my_obj, sort_keys=True, ensure_ascii=False, indent=2)
    assert JSONFormatter.format_body(my_string, 'json') == my_string

# Generated at 2022-06-13 22:11:18.945959
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter()
    body = "{\"foo\": 1, \"bar\": 2}"
    assert body == formatter.format_body(body, mime="json")
    assert body == formatter.format_body(body, mime="text")
    assert body

# Generated at 2022-06-13 22:11:29.654595
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter({}, {
        'json': {
            'format': True,
            'ensure_ascii': False,
            'indent': 4,
            'sort_keys': True,
        }
    })
    body = '{"key": "value"}'
    expected_body = json.dumps(json.loads(body), ensure_ascii=False, indent=4, sort_keys=True)
    formatted = formatter.format_body(body, 'application/json')
    assert formatted == expected_body, 'JSON body failed to be formatted'
    body = '{"key": "value"}'
    assert formatter.format_body(body, 'text/plain') == body, 'Text body was formatted'

# Generated at 2022-06-13 22:11:34.633289
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    from httpie.formatting import JSONFormatter
    json_formatter = JSONFormatter()
    print(json_formatter.format_body('{"fnord": 42}', 'json'))


# Generated at 2022-06-13 22:11:45.303874
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    from .utils import http
    expected = (
        '{\n'
        '    "args": {\n'
        '        "foo": "bar"\n'
        '    },\n'
        '    "headers": {\n'
        '        "Accept": "*/*",\n'
        '        "Accept-Encoding": "gzip, deflate",\n'
        '        "Host": "httpbin.org",\n'
        '        "User-Agent": "HTTPie/1.0.0"\n'
        '    },\n'
        '    "origin": "1.2.3.4",\n'
        '    "url": "http://httpbin.org/get?foo=bar"\n'
        '}'
    )