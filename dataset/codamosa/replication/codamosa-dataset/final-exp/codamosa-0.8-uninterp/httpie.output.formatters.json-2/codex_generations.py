

# Generated at 2022-06-13 22:01:53.941870
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    import pytest
    formatter = JSONFormatter()
    data = {'test': 'data'}
    data_json = json.dumps(data)
    content_type_json = 'application/json'

    assert formatter.format_body(body=data_json, mime=content_type_json) == data_json
    assert formatter.format_body(body=data_json, mime='text/plain') == data_json
    with pytest.raises(ValueError):
        formatter.format_body(body='no_json', mime=content_type_json)

# Generated at 2022-06-13 22:02:06.048380
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # 1. Test with JSON data
    # 1.1 Test with explicit json param
    f = JSONFormatter(format_options={'json':{'format':True}},
                      explicit_json=True)
    body = '{"n":1}\n'
    mime = 'application/json'
    formatted_body = f.format_body(body, mime)

    assert formatted_body == '{\n    "n": 1\n}\n'

    # 1.2. Test with hint of JSON mime type
    f = JSONFormatter(format_options={'json':{'format':True}},
                      explicit_json=False)
    body = '{"n":1}\n'
    mime = 'application/json'
    formatted_body = f.format_body(body, mime)


# Generated at 2022-06-13 22:02:16.164524
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    import pprint
    from httpie.response import _format_json
    from httpie.plugins.json import JSONPlugin
    json_data = {'a': 1}
    # Create an instance of JSONPlugin
    json_plugin = JSONPlugin(format_options={
        'json': {
            'indent': None,
            'sort_keys': False,
        },
    })
    # Create an instance of JSONFormatter
    json_formatter = JSONFormatter(format_options={
        'json': {
            'indent': None,
            'sort_keys': False,
            'format': True,
        },
    }, kwargs={}, __response_options={})
    # The instance of JSONFormatter calls the method format_body of its parent JSONPlugin
    assert json.dumps(json_data) == json_form

# Generated at 2022-06-13 22:02:29.129264
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    from httpie.plugins import JSONFormatter

    string_json = """{
        "foo": "bar",
        "baz": "qux"
    }"""
    string_json_min = """{"foo":"bar","baz":"qux"}"""
    string_json_indent = '''{
    "baz": "qux",
    "foo": "bar"
}'''

    assert JSONFormatter(kwargs={}).format_body(string_json, '') == string_json
    assert JSONFormatter(kwargs={'explicit_json': True}).format_body(string_json_min, '') == string_json_min
    assert JSONFormatter(kwargs={'explicit_json': True, 'json.indent': 2}).format_body(string_json_min, '') == string

# Generated at 2022-06-13 22:02:32.192274
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter()
    assert formatter.format_body('{"name": "Bozo"}', 'application/json') == '{\n    "name": "Bozo"\n}'

# Generated at 2022-06-13 22:02:40.993372
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter()
    assert(formatter.format_body("{}", "application/json") == "{}")
    assert(formatter.format_body("{}", "application/javascript") == "{}")
    assert(formatter.format_body("{}", "text/json") == "{}")
    assert(formatter.format_body("{}", "text/javascript") == "{}")
    assert(formatter.format_body("{", "application/json") == "{}")
    assert(formatter.format_body("{", "text/json") == "{}")

# Generated at 2022-06-13 22:02:44.797602
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    formatOptions = {'json': {'format': True, 'indent': None, 'sort_keys': None}}
    formatter = JSONFormatter(formatOptions)
    assert formatter.enabled == True

# Generated at 2022-06-13 22:02:54.068915
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    test_class = JSONFormatter()
    assert json.dumps(
        obj="{0}",
        sort_keys=test_class.format_options['json']['sort_keys'],
        ensure_ascii=False,
        indent=test_class.format_options['json']['indent']
    ) == json.dumps(
        obj=test_class.format_body("{0}", 'json'),
        sort_keys=test_class.format_options['json']['sort_keys'],
        ensure_ascii=False,
        indent=test_class.format_options['json']['indent']
    )

# Generated at 2022-06-13 22:03:01.508069
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    class DummyRequest:
        headers = {'Content-Type': 'application/json'}

    class DummyResponse:
        status_code = 200
        request = DummyRequest()

    formatter = JSONFormatter({}, **{'explicit_json': False})
    assert formatter.format_body(body='{}', mime='text/plain') == '{}'



# Generated at 2022-06-13 22:03:04.899505
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    f = JSONFormatter()
    assert f.format_body(
        '{"key":"value"}',
        'application/json'
    ) == '{\n    "key": "value"\n}'

# Generated at 2022-06-13 22:03:21.313907
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():

    # Create a JSONFormatter
    myJSONFormatter = JSONFormatter()

    # Test the function format_body
    assert myJSONFormatter.format_body('{"name" : "test"}', 'json') == '{\n    "name": "test"\n}'
    assert myJSONFormatter.format_body('{"name" : "test"}', 'javascript') == '{\n    "name": "test"\n}'
    assert myJSONFormatter.format_body('{"name" : "test"}', 'text') == '{\n    "name": "test"\n}'
    assert myJSONFormatter.format_body('{"name" : "test"}', 'xml') == '{"name" : "test"}'

# Generated at 2022-06-13 22:03:34.813222
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    body = '{"foo": 1, "bar": "alpha"}'
    mime = 'json'
    kwargs = {'explicit_json': False}
    json_plugin = JSONFormatter(**kwargs)
    result = json_plugin.format_body(body=body, mime=mime)
    assert result == '{\n    "bar": "alpha",\n    "foo": 1\n}'

    kwargs = {'explicit_json': False}
    json_plugin = JSONFormatter(**kwargs)
    result = json_plugin.format_body(body=body, mime='javascript')
    assert result == '{\n    "bar": "alpha",\n    "foo": 1\n}'

    kwargs = {'explicit_json': False}
    json_plugin = JSON

# Generated at 2022-06-13 22:03:43.016140
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter({'json':{'format':True,'indent':4,'sort_keys':True}})
    assert formatter.format_body('{"foo":"bar"}', 'json') == '{\n    "foo": "bar"\n}'
    assert formatter.format_body('{"foo":"bar"}', 'text') == '{\n    "foo": "bar"\n}'
    assert formatter.format_body('{"foo":"bar"}', 'javascript') == '{\n    "foo": "bar"\n}'
    assert formatter.format_body('{"foo":"bar"}', 'xml') == '{"foo":"bar"}'

# Generated at 2022-06-13 22:03:50.986276
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    import pytest
    plugin = JSONFormatter(**{'explicit_json': True})
    assert plugin.format_body(body="{}", mime="JSON") == "{}"
    assert plugin.format_body(body="{}", mime="Text") == "{}"
    assert plugin.format_body(body="0", mime="JSON") == "0"
    with pytest.raises(ValueError):
        plugin.format_body(body="{", mime="JSON")



# Generated at 2022-06-13 22:03:52.457593
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    obj = JSONFormatter()
    assert isinstance(obj, FormatterPlugin)

# Generated at 2022-06-13 22:03:56.308146
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    JSONFormatter({}, {
        'json': {
            'format': True,
            'indent': 4,
            'sort_keys': True,
        },
        'colors': {
            'value': 'on',
        },
        'style': {
            'value': 'default',
        },
    })

# Generated at 2022-06-13 22:04:05.462980
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    format_options = json.loads('''{
        "json": {
            "format": true,
            "sort_keys": true,
            "indent": 1
        }
    }''')
    dic = {'format_options': format_options, 'explicit_json': False,
           'output_options': {'format': 'test'}, 'kwargs': {'explicit_json': False}}
    a = JSONFormatter(**dic)
    assert a.enabled is True
    assert a.kwargs == {'explicit_json': False}


# Generated at 2022-06-13 22:04:06.243539
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    pass

# Generated at 2022-06-13 22:04:16.793724
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter(
        **{'explicit_json': True,
        'format_options': {
            'json': {
                'format': True,
                'indent': 4,
                'sort_keys': True
            }
        }})


# Generated at 2022-06-13 22:04:23.173048
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    """
    Test method format_body of class JSONFormatter
    """
    json_formatter = JSONFormatter(
        format_options={'json': {
            'format': True,
            'indent': 2,
            'sor_keys': False,
        }},
        explicit_json=False,
    )
    json_formatter.kwargs = {
        'explicit_json': False,
    }

    body = json_formatter.format_body('{"foo": "bar"}', 'application/json')
    assert body == '{\n  "foo": "bar"\n}'

    body = json_formatter.format_body('{"foo": "bar"}', 'text/html')
    assert body == '{\n  "foo": "bar"\n}'


# Generated at 2022-06-13 22:04:37.616661
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    plugin = JSONFormatter()
    body = '{"message": "Hello"}'
    mime = 'application/json'
    assert plugin.format_body(body, mime) == body
    body = 'Hello, World'
    mime = 'text/a-fake-mime-type'
    assert plugin.format_body(body, mime) == body
    mime = 'application/javascript'
    assert plugin.format_body(body, mime) == body
    body = '{"message": "Hello World"}'
    assert plugin.format_body(body, mime) == body

# Generated at 2022-06-13 22:04:46.091999
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    import httpie

    json_format = JSONFormatter(
        format_options=httpie.prefs.get_prefs(),
        explicit_json=True
    )

    # Test #1
    arg1 = "[1, 2, 3]"
    arg2 = "application/json"
    exp1 = "[\n    1,\n    2,\n    3\n]"
    obs1 = json_format.format_body(arg1, arg2)
    assert (exp1 == obs1)

# Generated at 2022-06-13 22:04:55.363188
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    import json
    import httpie.plugins
    # Test JSONFormatter.format_body()
    # Create an instance of JSONFormatter class
    json_instance = httpie.plugins.JSONFormatter(explicit_json=False, format_options={'json': {'format': True, 'indent': 4, 'sort_keys': False}})
    # Test with valid json string
    valid_json = '{"name": "Hello World", "number": 1}'
    assert json_instance.format_body(valid_json, 'json') == "{\"name\": \"Hello World\", \"number\": 1}"
    # Test with invalid json string
    invalid_json = '{"name": "Hello World", "number": 1}-123'
    assert json_instance.format_body(invalid_json, 'json') == invalid_json


__version

# Generated at 2022-06-13 22:04:56.054002
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    pass

# Generated at 2022-06-13 22:05:06.314130
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    valid_json = json.dumps(
        {
            'foo': 'bar',
            'arr': [1, 2, 3],
        }
    )


# Generated at 2022-06-13 22:05:13.658641
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    jf = JSONFormatter(format_options={'json': {'format': True,
                                           'sort_keys': True,
                                           'indent': 2}},
                                    explicit_json=True)
    body = jf.format_body('{"user_id": 123}', 'json')
    assert body == '{\n  "user_id": 123\n}'


# Generated at 2022-06-13 22:05:27.160020
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    class_ = JSONFormatter(format_options = {'json': {'format': True}},
        explicit_json = True)
    assert class_.format_body("{}", "json") == "{}"
    assert class_.format_body("", "json") == ""
    assert class_.format_body("text", "text") == "text"
    class_.format_options = {'json': {'format': False}}
    assert class_.format_body("text", "text") == "text"
    class_.format_options = {'json': {'format': True}}
    assert class_.format_body("text", "text") == ""
    class_.format_options = {'json': {'format': True}}
    assert class_.format_body("{", "text") == "{}"

# Generated at 2022-06-13 22:05:34.412721
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # Given a valid json (dict)
    unformatted_json = '{"foo": "bar"}'

    # When I use a JSONFormatter instance to format it
    formatted_json = JSONFormatter(**{'explicit_json': True}
                                   ).format_body(unformatted_json, '')

    # Then I expect that it would be indented
    assert formatted_json == '{\n    "foo": "bar"\n}'



# Generated at 2022-06-13 22:05:42.351619
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    jsonFormatter = JSONFormatter()

    # test JSON formatter with JSON body
    body = '{"foo":42,"bar":"baz"}'
    result_body = jsonFormatter.format_body(body, "json")
    assert result_body == '{\n    "bar": "baz",\n    "foo": 42\n}'

    # test JSON formatter with text/plain body
    body = 'Hello, world!'
    result_body = jsonFormatter.format_body(body, "text/plain")
    assert result_body == body

    # test JSON formatter with invalid JSON body
    body = '{"foo":42,"baz"}'
    result_body = jsonFormatter.format_body(body, "json")
    assert result_body == body

# Generated at 2022-06-13 22:05:51.656408
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    from httpie import ExitStatus
    from utils import http, HTTP_OK

    json_input = json.dumps({'a': 5, 'b': 10})

    # No format_options, nothing should be returned
    args = http('--verbose', 'POST', '--form', 'field=@-' << json_input)
    assert HTTP_OK in args
    assert 'json:' not in args
    assert '"field":' not in args

    # JSON output, nothing should be returned
    args = http('--verbose', 'POST', '--form', 'field=@-' << json_input, '--json')
    assert HTTP_OK in args
    assert 'json:' not in args
    assert '"field":' not in args

    # JSON formatter should be enabled, output for form should not be returned

# Generated at 2022-06-13 22:06:14.534526
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter(format_options={'json':{'format':True, 'indent':2, 'sort_keys':True}})

    test_body_1 = '{"key_1": "value_1", "key_2": "value_2", "key_3": "value_3"}'

    result_1 = formatter.format_body(test_body_1, 'application/json')

    assert result_1 == '{' \
                       '\n  "key_1": "value_1",' \
                       '\n  "key_2": "value_2",' \
                       '\n  "key_3": "value_3"' \
                       '\n}'

    formatter.format_options['json']['sort_keys'] = False

    result_2 = formatter.format

# Generated at 2022-06-13 22:06:18.017478
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    json_formatter = JSONFormatter()
    assert json_formatter.format_body('{"a":1}', 'json') == '{\n    "a": 1\n}'

# Generated at 2022-06-13 22:06:25.969437
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter_plugin = JSONFormatter(
        format_options={
            'json': {
                'format': True,
                'sort_keys': False,
                'indent': 4
            }
        },
        explicit_json=False,
        output_options={},
        parser_options={},
        env_options={},
        stdout=None,
        stderr=None
    )
    body = '{"key1": "value1", "key2": "value2"}'
    mime = 'application/json'
    assert formatter_plugin.format_body(body=body, mime=mime) == body

# Generated at 2022-06-13 22:06:37.158542
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # Build formatter object
    f = JSONFormatter(format_options={
            'json':
                {'format': True, 'indent': 4, 'sort_keys': True}
        },
        explicit_json=False)
    # Run tests
    assert f.format_body('example', 'application/json') == '"example"'

# Generated at 2022-06-13 22:06:40.684568
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    from httpie.plugins import JSONFormatter
    sender = JSONFormatter()
    result = sender.format_body(body='{"a":3, "b":1}', mime='text')
    assert result == '{\n    "a": 3,\n    "b": 1\n}'

# Generated at 2022-06-13 22:06:54.131235
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():

    test_cases = [
        (b'{"foo": "bar"}', 'application/json', b'{\n    "foo": "bar"\n}'),
        (b'{"foo": "bar"}', 'text/plain', b'{"foo": "bar"}'),
        (b'"foo"', 'text/plain', b'"foo"'),
        (b'"foo"', 'application/json', b'"foo"'),
    ]

    indent = 4
    sort_keys = True
    json_options = {'indent': indent, 'sort_keys': sort_keys}

    formatter = JSONFormatter(format_options={'json': json_options})

    for body, mime, expect in test_cases:
        actual = formatter.format_body(body, mime)
        assert actual == expect

# Generated at 2022-06-13 22:07:00.978499
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter(kwargs={
        'json':      False,
        'explicit_json': True,
        'format_options': {
            'json': {
                'format': True,
                'indent': 2,
                'sort_keys': False
            }
        }
    })
    body = formatter.format_body("""
{
    "a": [
        1,
        2
    ],
    "b": 3.14
}
    """, "application/json")
    assert body == """{
  "a": [1, 2],
  "b": 3.14
}
"""


# Generated at 2022-06-13 22:07:11.201331
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    f = JSONFormatter()

    # Should indent, sort keys and avoid unicode escapes when formatting.
    actual_body = f.format_body(
        '{"name":"apple","price":1.54,"id":1}',
        'application/json'
    )
    expected_body = '''{
    "id": 1,
    "name": "apple",
    "price": 1.54
}'''
    assert (actual_body == expected_body), \
        "actual_body: {}, expected_body: {}".format(actual_body, expected_body)

    # Should leave the original body when formatting failure.
    actual_body = f.format_body(
        'Not a JSON content',
        'application/json'
    )
    expected_body = 'Not a JSON content'

# Generated at 2022-06-13 22:07:21.591048
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    jsonformatter = JSONFormatter()
    jsonformatter.kwargs = {'explicit_json': True}
    jsonformatter.format_options = {
        'json': {
            'indent': 4,
            'sort_keys': True,
            'format': True
        }
    }
    body = jsonformatter.format_body('{"a": ["b"]}', 'json')
    assert json.loads(body) == {'a': ['b']}
    assert body == '{\n    "a": [\n        "b"\n    ]\n}'

# Generated at 2022-06-13 22:07:33.724898
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    jsonFormatter = JSONFormatter(
        format_options={
            'json': {
                'format': True,
                'sort_keys': True,
                'indent': 2
            }
        }
    )
    # Valid JSON case
    body = '{"employees":[{"firstName":"John","lastName":"Doe"},{"firstName":"Anna","lastName":"Smith"},{"firstName":"Peter","lastName":"Jones"}]}'
    mime = 'json'