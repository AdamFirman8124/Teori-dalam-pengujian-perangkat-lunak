

# Generated at 2022-06-13 22:01:53.745461
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    plugin = JSONFormatter(explicit_json=True, format_options={
        'json': {
            'format': True,
            'sort_keys': True,
            'indent': 4
        }
    })
    assert(plugin.format_body('{"key": "value"}', 'application/json') == '{\n    "key": "value"\n}')
    assert(plugin.format_body('not_json', 'application/json') == 'not_json')

# Generated at 2022-06-13 22:02:02.985339
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    new_json_formatter = JSONFormatter(format_options={'json': {'format': True, 'indent': 1, 'sort_keys': False}})
    expected_enabled = True
    actual_enabled = new_json_formatter.enabled
    assert expected_enabled == actual_enabled
    expected_format_options = {'json': {'format': True, 'indent': 1, 'sort_keys': False}}
    actual_format_options = new_json_formatter.format_options
    assert expected_format_options == actual_format_options


# Generated at 2022-06-13 22:02:07.165525
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    assert JSONFormatter(**{'explicit_json': False, 'format_options': {'json': {'format': False, 'sort_keys': False, 'indent': 4}}})

# Generated at 2022-06-13 22:02:16.571294
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    from httpie.formatters import JSONFormatter
    from httpie.plugins import FormatterPlugin
    instance = JSONFormatter()
    assert isinstance(instance, FormatterPlugin)
    assert 'json' in instance.format_options
    assert instance.kwargs == {
        'format': 'colors',
        'format_options': {
            'json': {
                'format': True,
                'indent': 2,
                'sort_keys': False
            },
            'colors': True,
            'stream': False,
            'verbose': False,
            'default_options': {
                'verify': True,
                'headers': {},
                'timeout': None
            }
        },
        'style': 'default'
    }
    assert instance.enabled == True

# Generated at 2022-06-13 22:02:27.706305
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    import json
    json_object = json.dumps(obj={"a": 1, "b": 2}, sort_keys=True, ensure_ascii=False, indent=4)
    formatter = JSONFormatter(format_options={'json': {'format': True, 'indent': 4, 'sort_keys': True}})
    assert formatter.format_body("{}", "application/json") == json_object
    assert formatter.format_body("{\"a\": 1, \"b\": 2}", "text/javascript") == json_object
    assert formatter.format_body("{\"a\": 1, \"b\": 2}", "text/html") == json_object

# Generated at 2022-06-13 22:02:31.512966
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter()
    assert formatter.format_body('{ "key": "value" }', "application/json") == '{\n    "key": "value"\n}'



# Generated at 2022-06-13 22:02:41.694260
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():

    class MockJSONFormatter(JSONFormatter):

        def __init__(self, **kwargs):
            super().__init__(**kwargs)

        def get_json_kwargs(self):
            return {'indent': 4, 'sort_keys': 0}

    mock_json_formatter = MockJSONFormatter()
    body = mock_json_formatter.format_body(body='{"hello": "world"}', mime='application/json')
    assert body == '{\n    "hello": "world"\n}'

    body = mock_json_formatter.format_body(body='{"foo": "bar"}', mime='application/xml')
    assert body == '{"foo": "bar"}'

# Generated at 2022-06-13 22:02:53.786761
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    s = JSONFormatter(**{'json': {'indent': 2, 'sort_keys': True, 'format': True}, 'explicit_json': False})
    assert s.format_body('{ "a": 3, "b": 2 }', 'json') == '{\n  "a": 3,\n  "b": 2\n}'
    assert s.format_body('{ "1": 1, "2": 2 }', 'json') == '{\n  "1": 1,\n  "2": 2\n}'
    assert s.format_body('{ "b": 2, "a": 1 }', 'json') == '{\n  "a": 1,\n  "b": 2\n}'

# Generated at 2022-06-13 22:03:06.477907
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    BODY_JSON = '{"a":[1,2,3],"b":{"c":true}}'
    BODY_PLAIN = 'No JSON.'

    jf = JSONFormatter()

    # test_case_1
    # test JSONformatting
    mime = 'application/json'
    formatted = jf.format_body(BODY_JSON, mime)
    assert formatted == '{\n    "a": [\n        1,\n        2,\n        3\n    ],\n    "b": {\n        "c": true\n    }\n}'

    # test_case_2
    # test JSON formatting
    mime = 'text/json'
    formatted = jf.format_body(BODY_JSON, mime)

# Generated at 2022-06-13 22:03:16.042873
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    json_formatter = JSONFormatter(
        format_options={
            'json': {
                'format': True,
                'indent': 4,
                'sort_keys': True
            }
        },
        explicit_json=False
    )
    body = '[{"a": "b", "c": "d", "e": "f"}]'
    actual = json_formatter.format_body(body, "json")
    expected = (
        "[\n"
        "    {\n"
        "        \"a\": \"b\",\n"
        "        \"c\": \"d\",\n"
        "        \"e\": \"f\"\n"
        "    }\n"
        "]"
    )
    assert actual == expected

# Generated at 2022-06-13 22:03:32.574426
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    fp = JSONFormatter()
    assert fp.format_body('{"a":1, "b":2}', 'json') == '{"a": 1, "b": 2}'
    assert fp.format_body('{"a":1, "b":2}', 'javascript') == '{"a": 1, "b": 2}'
    assert fp.format_body('{"a":1, "b":2}', 'text') == '{"a": 1, "b": 2}'
    assert fp.format_body('{"a":1, "b":2}', 'html') == '{"a": 1, "b": 2}'
    assert fp.format_body('{"a":1, "b":2}', 'jason') == '{"a": 1, "b": 2}'
    assert fp

# Generated at 2022-06-13 22:03:37.681320
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter()
    body = "{\"name\": \"foo\", \"age\": 20}"
    result = formatter.format_body(body, "application/json")
    assert result == '{\n    "age": 20,\n    "name": "foo"\n}'

# Generated at 2022-06-13 22:03:45.580059
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # Valid JSON
    body = '{"hi":"hello"}'
    mime = 'json'
    expected = '{\n    "hi": "hello"\n}'
    actual = JSONFormatter(format_options={
        'json': {
            'format': True,
            'indent': 4,
            'sort_keys': True,
        }
    }).format_body(body, mime)
    assert actual == expected

    # Invalid JSON
    body = '{"hi":"hello"'
    mime = 'json'
    expected = '{"hi":"hello"'
    actual = JSONFormatter(format_options={
        'json': {
            'format': True,
            'indent': 4,
            'sort_keys': True,
        }
    }).format_body(body, mime)

# Generated at 2022-06-13 22:03:56.404186
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # Create a JSONFormatter object with keyword arguments
    # explicit_json = True and format_options = {'format': True, 'sort_keys': True, 'indent': 2}
    dummy_kwargs = {'format': True, 'sort_keys': True, 'indent': 2}
    b1 = JSONFormatter(explicit_json=True, format_options=dummy_kwargs)
    assert b1.format_body(body='[1,2,3]', mime='json') == '[1, 2, 3]'
    assert b1.format_body(body='{"a":1}', mime='json') == '{\n  "a": 1\n}'

    # Create a JSONFormatter object with keyword arguments
    # explicit_json = False and format_options = {'format': True, 'sort_keys

# Generated at 2022-06-13 22:04:09.071142
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter()

    initial_str = (
        r'{"asset": {"id": "00006877", "name": "Asset-001-test"}, "customAttributes": {}, "installationStatus": {'
        '"installationTime": "2020-04-27T10:03:13Z", "installationTimestamp": 1587984993000, '
        '"lastServiceTime": "2020-04-27T10:03:13Z", "lastServiceTimestamp": 1587984993000, '
        '"lruSerialNumbers": ["60-00123-000"], "lruType": "Printer", "serviceState": "Installed"}}')

# Generated at 2022-06-13 22:04:19.029109
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter_json = JSONFormatter(
        format_options={'json': {
            'format': True,
            'indent': 2,
            'sort_keys': True,
        }}
    )

# Generated at 2022-06-13 22:04:26.104665
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    from httpie.plugins import builtin
    json_formatter = JSONFormatter(explicit_json=False, format_options={'json': {'format': 'on', 'sort_keys': True, 'indent': 2}})
    print(json_formatter.format_body('{"test": "test"}', 'json'))


# Generated at 2022-06-13 22:04:36.676150
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    json_formatter_plugin = JSONFormatter(**{'format_options': {'json': {'format': True, 'indent': 4, 'sort_keys': True}}, 'explicit_json': False})
    obj = {
        'name': 'John Doe',
        'age': 34,
        'is_teacher': False,
        'address': '123 Main St.\nAnytown, USA'
    }
    assert json_formatter_plugin.format_body(
        json.dumps(obj), 'application/json') == json.dumps(obj,indent=4,sort_keys=True)

# Example test for code coverage

# Generated at 2022-06-13 22:04:43.164956
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    json_formatter = JSONFormatter({})
    data = b'{"my": "value"}'
    expected = '{\n    "my": "value"\n}'
    assert json_formatter.format_body(data, 'json') == expected

# Generated at 2022-06-13 22:04:54.134700
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    jsonFormatter = JSONFormatter(
        format_options={
            "json": {
                "format": True,
                "sort_keys": False,
                "indent": None
            },
            "colors": {
                "method": "1;34",
                "body": "31",
                "status": "1;32",
                "hdr_name": "1;34",
                "hdr_value": "",
                "url": "",
                "line_number": "1;30",
                "error_name": "1;31",
                "error_msg": "1;31",
                "redirection": "1;33"
            }
        },
        color=True,
        explicit_json=False
    )

    # 'format' = False
    jsonFormatter.enabled = False



# Generated at 2022-06-13 22:05:05.875792
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():

    from httpie.plugins.core import JSONStream
    from httpie.core import main

    json_formatter = JSONFormatter(
        format_options={'json': {'format': True, 'indent': 4, 'sort_keys': True}})
    json_stream = JSONStream()

    result = json_stream.transform(
        json_formatter.format_body(
            body='{"kevin": "kowalczyk", "green": "dev"}', mime='json'),
        {}
    )

    assert main.json_zoom(result, '$.headers.content-type') == "application/json"
    assert main.json_zoom(result, '$.headers.content-length') == "40"

# Generated at 2022-06-13 22:05:15.062500
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    import httpie.plugins
    class sample_JSONFormatter(httpie.plugins.JSONFormatter):
        def __init__(self):
            self.format_options = {}
            self.format_options['json'] = {}
            self.format_options['json']['format'] = True
            self.format_options['json']['sort_keys'] = True
            self.format_options['json']['indent'] = 2

    body = '{"foo":42}'
    mime = 'json'
    jsonformatter = sample_JSONFormatter()
    response = jsonformatter.format_body(body, mime)
    assert response.split('\n') == ['{',
                                    '  "foo": 42',
                                    '}']

# Generated at 2022-06-13 22:05:26.011905
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # Parameters.
    body = '[{"username":"admin","password":"admin"}]'
    mime = 'json'
    explicit_json = False
    indent = None
    sort_keys = False
    kwargs = {
        'explicit_json': explicit_json,
        'format_options': {
            'json': {
                'format': True,
                'indent': indent,
                'sort_keys': sort_keys
            }
        }
    }
    # Execute.
    formatter = JSONFormatter(**kwargs)
    result = formatter.format_body(body, mime)
    # Test.
    assert result == body

# Generated at 2022-06-13 22:05:34.746962
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter()
    assert formatter.format_body("{}", "json") == "{}"
    assert formatter.format_body('{"a": "b"}', "json") == '{\n    "a": "b"\n}'
    assert formatter.format_body("{}", "text") == "{}"
    assert formatter.format_body('{"a": "b"}', "text") == '{\n    "a": "b"\n}'
    assert formatter.format_body("{}", "javascript") == "{}"
    assert formatter.format_body('{"a": "b"}', "javascript") == '{\n    "a": "b"\n}'

# Generated at 2022-06-13 22:05:42.667915
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # Test 1: Return None when content-type is not JSON
    f = JSONFormatter(indent=4, sort_keys=False)
    response_string = '{\n"key" : "value"\n}'
    body = f.format_body(response_string, 'plain')
    assert body == response_string

    # Test 2: Return None when content-type is JSON
    f = JSONFormatter(indent=4, sort_keys=False)
    response_string = '{\n"key" : "value"\n}'
    body = f.format_body(response_string, 'json')
    assert body == '{\n    "key": "value"\n}' or body == '{\n    "key": "value"\n}\n'

    # Test 3: Return None when content-type is plain

# Generated at 2022-06-13 22:05:51.883126
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    obj = {
        'g': 7,
        'c': 6,
        'f': 5,
        'e': 4,
        'b': 3,
        'd': 2,
        'a': 1,
        'h': 0
    }
    j_format = {
        'sort_keys': True,
        'indent': 2
    }
    json_text = b'{"a": 1, "b": 3, "c": 6, "d": 2, "e": 4, "f": 5, "g": 7, "h": 0}'

# Generated at 2022-06-13 22:06:01.849623
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter()
    assert formatter.format_body('{"a": "b"}', 'application/json') == '{\n    "a": "b"\n}'
    assert formatter.format_body('{"a": "b"}', 'application/javascript') == '{\n    "a": "b"\n}'
    assert formatter.format_body('{"a": "b"}', 'text/javascript') == '{\n    "a": "b"\n}'
    assert formatter.format_body('{"a": "b"}', 'text') == '{\n    "a": "b"\n}'

# Generated at 2022-06-13 22:06:03.135267
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    pass

# Generated at 2022-06-13 22:06:12.082711
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter(kwargs={})
    body = '{"foo": "bar"}'
    mime = 'text/json'
    assert formatter.format_body(body, mime) == '{\n    "foo": "bar"\n}'
    mime = 'application/json'
    assert formatter.format_body(body, mime) == '{\n    "foo": "bar"\n}'
    mime = 'text/html'
    assert formatter.format_body(body, mime) == body

# Generated at 2022-06-13 22:06:23.598201
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter()
    # Valid JSON format
    body = '{"key": "value"}'
    mime = 'application/json'
    assert formatter.format_body(body, mime) == body
    # Valid JSON format, but mime is javascript
    body = '{"key": "value"}'
    mime = 'text/javascript'
    assert formatter.format_body(body, mime) == body
    # Valid JSON format, but mime is text
    body = '{"key": "value"}'
    mime = 'text/plain'
    assert formatter.format_body(body, mime) == body
    # Invalid JSON format
    body = '{"key: "value"}'
    mime = 'application/json'