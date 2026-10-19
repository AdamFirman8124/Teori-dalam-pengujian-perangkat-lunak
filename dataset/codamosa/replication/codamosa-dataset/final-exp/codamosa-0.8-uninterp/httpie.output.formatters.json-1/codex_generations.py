

# Generated at 2022-06-13 22:01:48.292545
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    json_formatter = JSONFormatter()
    body = '{"name": "value"}'
    mime = 'json'
    assert json_formatter.format_body(body, mime) == '{\n    "name": "value"\n}'

# Generated at 2022-06-13 22:01:51.914230
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    formatter = JSONFormatter({'json': {'format': False, 'indent': 2, 'sort_keys': True}}, explicit_json=False)
    assert formatter.enabled == False


# Generated at 2022-06-13 22:02:02.462187
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    settings = {
        'json': {
            'format': False,
            'indent': 2,
            'sort_keys': True,
        }
    }
    JF = JSONFormatter(settings=settings)
    assert JF.kwargs['settings'] == settings
    assert JF.format_options['json']['format'] == settings['json']['format']
    assert JF.format_options['json']['indent'] == settings['json']['indent']
    assert JF.format_options['json']['sort_keys'] == settings['json']['sort_keys']


# Generated at 2022-06-13 22:02:04.157093
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    pass
    # TODO



# Generated at 2022-06-13 22:02:07.101074
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    body = '{"hello": "world"}'
    mime = 'application/json'
    assert JSONFormatter().format_body(body, mime) == body

# Generated at 2022-06-13 22:02:15.778127
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    json_formatter = JSONFormatter()
    # test: Invalid JSON
    input = '{"foo" : "bar", "abc" : "xyz"}'
    json_formatter.kwargs['explicit_json'] = False
    json_formatter.format_options['json']['format'] = True
    json_formatter.format_options['json']['indent'] = 1
    json_formatter.format_options['json']['sort_keys'] = True
    expected_output = '{\n    "abc": "xyz",\n    "foo": "bar"\n}'
    output = json_formatter.format_body(input, "text")
    assert output == expected_output

# Generated at 2022-06-13 22:02:16.758152
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    assert False

# Generated at 2022-06-13 22:02:24.639708
# Unit test for method format_body of class JSONFormatter

# Generated at 2022-06-13 22:02:37.218330
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # assert(False)

    json_formatter = JSONFormatter(format_options={'json':{
        'sort_keys': True,
        'indent': 4,
        'format': True
    }})

    assert json_formatter.format_body(body='{"a": "value", "b": "value"}', mime='json') == \
        '{\n    "a": "value",\n    "b": "value"\n}'

    json_formatter.format_options['json']['sort_keys'] = False
    assert json_formatter.format_body(body='{"a": "value", "b": "value"}', mime='json') == \
        '{\n    "a": "value",\n    "b": "value"\n}'

    json_formatter.format

# Generated at 2022-06-13 22:02:47.096169
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    body = """
["coucou", "hi", "yo", "hey"]"""
    formatter = JSONFormatter(explicit_json=True)
    formatter.format_options['json']['indent'] = 4
    formatter.format_options['json']['sort_keys'] = True
    body = formatter.format_body(body=body, mime='json')
    assert body == """
[
  "coucou",
  "hi",
  "yo",
  "hey"
]"""


# Generated at 2022-06-13 22:03:01.178714
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():

    formatter = JSONFormatter()

    result = formatter.format_body('{"foo":"bar"}', 'application/json')
    assert result == '{\n    "foo": "bar"\n}'

    result = formatter.format_body('{"foo":"bar"}', 'text/javascript')
    assert result == '{\n    "foo": "bar"\n}'

    result = formatter.format_body('{"foo":"bar"}', 'text/plain')
    assert result == '{\n    "foo": "bar"\n}'

    result = formatter.format_body('Not valid JSON', 'application/json')
    assert result == 'Not valid JSON'

    result = formatter.format_body('Not valid JSON', 'text/javascript')
    assert result == 'Not valid JSON'

    result = formatter.format

# Generated at 2022-06-13 22:03:02.763517
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    jf = JSONFormatter()
    assert jf.enabled == jf.format_options['json']['format']


# Generated at 2022-06-13 22:03:08.150028
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    json_formatter = JSONFormatter(**{
        'format_options': {
            'json': {
                'format': True,
                'indent': 4,
                'sort_keys': False,
            },
            'colors': {
                'method': False,
                'status': False,
                'headers': False
            }
        }
    })
    assert (json_formatter.format_body('{"key": "value"}', 'javascript') ==
            '{\n    "key": "value"\n}')
    assert (json_formatter.format_body('{"key": "value"}', 'json') ==
            '{\n    "key": "value"\n}')

# Generated at 2022-06-13 22:03:18.501012
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter(kwargs={'explicit_json': True}, format_options={}, headers={})
    # test empty payload
    assert formatter.format_body(mime='json', body='') == ''
    # test invalid payload
    assert formatter.format_body(mime='json', body='{test}') == '{test}'
    # test valid payload
    assert formatter.format_body(mime='json', body='{"test":"test"}') == '{\n    "test": "test"\n}'


# Generated at 2022-06-13 22:03:29.004271
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    indent = True
    sort_keys = True
    explicit_json = True
    format_options = {'json': {'indent': indent, 'sort_keys': sort_keys}}
    args = ['http']
    kwargs = {'format_options': format_options, 'explicit_json': explicit_json}
    formatter = JSONFormatter(args=args, kwargs=kwargs)

    # Case 1: Ensure that the method returns the original input, if the input is not JSON
    obj = {'a': 1, 'b': '2', 'c': ['1', '2', '3']}
    body = 'key=value&key=value'
    mime = 'text/html'
    assert body == formatter.format_body(body=body, mime=mime)

    # Case 2: Ensure

# Generated at 2022-06-13 22:03:40.483588
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter_plugin = JSONFormatter()

    assert (formatter_plugin.format_body(
        '{"a": 1}', 'application/json') == '{\n    "a": 1\n}')

    assert (formatter_plugin.format_body(
        '{"a": 1}', 'application/json') == '{\n    "a": 1\n}')

    assert (formatter_plugin.format_body(
        '{"a": 1}', 'text/javascript') == '{\n    "a": 1\n}')

    assert (formatter_plugin.format_body(
        '{"a": 1}', 'application/javascript') == '{\n    "a": 1\n}')


# Generated at 2022-06-13 22:03:41.451417
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    pass

# Generated at 2022-06-13 22:03:53.270700
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter()

    for body in (None, '', 'text'):
        assert formatter.format_body(body, None) == body

    body = '{"a": "text"}'

    assert formatter.format_body(body, 'json') == body
    assert formatter.format_body(body, 'javascript') == body
    assert formatter.format_body(body, 'text') == body

    assert formatter.format_body(body, None) == body
    assert formatter.format_body(body, 'text/css') == body
    assert formatter.format_body(body, 'text/html') == body

    assert formatter.format_body(body, 'application/json') ==\
        '{\n    "a": "text"\n}'

    assert formatter.format_body

# Generated at 2022-06-13 22:03:57.746426
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    import json
    formatter = JSONFormatter()
    # Testing with a valid json
    valid = json.dumps({'a': 1, 'b': 2, 'c': 3})
    assert formatter.format_body(valid, 'javascript') == valid



# Generated at 2022-06-13 22:04:12.740947
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    from httpie.output.formatters.utils import GenericJSONAdapter
    from httpie.output.streams import StdoutStderrMixin

    std_streams = StdoutStderrMixin()
    formatter = JSONFormatter(std_streams=std_streams, format_options={})

    # Set all values to False
    formatter.format_options['json'] = {
        'format': False,
        'sort_keys': False,
        'indent': False
    }
    formatter._kwargs['explicit_json'] = False

    # No json (json=False, explicit_json=False, mime='html')
    body = formatter.format_body(body='{a: 1}', mime='html')
    assert body == '{a: 1}'

    # Enable json feature

# Generated at 2022-06-13 22:04:25.013756
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    body = '''
{
    "valid": "json",
    "invalid json": "json",
    "valid json": "invalid"
}
'''
    expected = '''
{
    "invalid json": "json",
    "valid": "json",
    "valid json": "invalid"
}
'''
    formatter = JSONFormatter(format_options={'json': {'format': True, 'indent': 4, 'sort_keys': True}})
    assert formatter.format_body(body, 'application/json') == expected

# Generated at 2022-06-13 22:04:32.801931
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    example = {
        'a': '1',
        'b': 2,
        'c': [
            3,
            4
        ]
    }
    formatter = JSONFormatter()
    assert formatter.format_body(json.dumps(example), 'application/json') == '{\n    "a": "1",\n    "b": 2,\n    "c": [\n        3,\n        4\n    ]\n}', \
        'Should return the JSON prettified'

# Generated at 2022-06-13 22:04:42.951149
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # Test with json mime type
    body = b'{"test": "data"}'
    mime = "application/json"
    assert JSONFormatter().format_body(body.decode(), mime) == '{\n    "test": "data"\n}'

    # Test with text mime type
    body = b'test data'
    mime = "text/plain"
    assert JSONFormatter().format_body(body.decode(), mime) == 'test data'

    # Test with a non json mime type
    body = b'{"test": "data"}'
    mime = "application/octet-stream"
    assert JSONFormatter().format_body(body.decode(), mime) == '{"test": "data"}'

    # Test with invalid JSON

# Generated at 2022-06-13 22:04:54.023231
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    import pytest

    ej = (
        '{\n'
        '    "c": 3,\n'
        '    "a": 1,\n'
        '    "b": 2\n'
        '}'
    )


# Generated at 2022-06-13 22:04:59.006366
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter()
    body = '{"test_body": "test_formatter"}'
    assert formatter.format_body(body, 'json') == '{\n    "test_body": "test_formatter"\n}'
    # Should not be indented for text
    assert formatter.format_body(body, 'text/html') == body

# Generated at 2022-06-13 22:05:07.570448
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    #import pytest

    formatter = JSONFormatter()

    body = '{\n"id": 42,\n"name": "Athan"\n}'
    assert formatter.format_body(body, 'application/json') == body

    body = '{\n"name": "Athan"\n}'
    expected = '{\n    "name": "Athan"\n}'
    assert formatter.format_body(body, 'application/json') == expected

# Generated at 2022-06-13 22:05:15.004277
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body(): 
    from httpie.formatter import JSONFormatter
    jf = JSONFormatter()
    json_str = '{"a": 1, "b": 2}'
    body = jf.format_body(json_str, 'json')
    assert body == json_str



# Generated at 2022-06-13 22:05:20.465671
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    f = JSONFormatter(explicit_json=True)
    body = "{'status': 'ok'}"
    assert f.format_body(body=body, mime='json') == '{\n    "status": "ok"\n}'

# Generated at 2022-06-13 22:05:28.740977
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # Arrange
    formatter = JSONFormatter()
    body = """
{
    "a": {
        "b": 2,
        "c": 3
    },
    "d": 4
}
"""
    mime = 'json'

    # Act
    result = formatter.format_body(body, mime)

    # Assert
    assert result == """
{
    "a": {
        "b": 2, 
        "c": 3
    }, 
    "d": 4
}
"""

# Generated at 2022-06-13 22:05:34.054772
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    '''
    Test function format_body of class JSONFormatter

    '''

    mime = 'json'
    body = '{"key": "value"}'
    formatter = JSONFormatter()

    assert formatter.format_body(body, mime) == body


# Generated at 2022-06-13 22:05:39.592203
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    pass

# Generated at 2022-06-13 22:05:46.012776
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    json_formatter = JSONFormatter(format_options={
        'json': {
            'format': True,
            'indent': 2,
            'sort_keys': True
        }
    })
    assert json_formatter.format_body('{"a": 1, "b": 2}', 'application/json') == '{\n  "a": 1,\n  "b": 2\n}'

# Generated at 2022-06-13 22:05:54.375050
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # 1. Input: Valid JSON string with mime type 'json'
    json_string = '{"a": "apple", "b": "boy"}'
    mime = 'json'
    formatter = JSONFormatter(explicit_json=False)
    actual_result = formatter.format_body(json_string, mime)
    # Should return the same string, but with pretty print.
    expected_result = '{\n    "a": "apple",\n    "b": "boy"\n}'
    assert actual_result == expected_result

    # 2. Input: Invalid JSON string with mime type 'json'
    json_string = '{"a": "apple", "b": "boy"'
    mime = 'json'
    formatter = JSONFormatter(explicit_json=False)

# Generated at 2022-06-13 22:05:55.981487
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    JSONFormatter().format_body(body='{ "hello": "world" }', mime='json')

# Generated at 2022-06-13 22:06:06.304454
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    from httpie.core import main
    from httpie.plugins import FormatterPluginManager

    manager = FormatterPluginManager(['json'])
    # manager.format_options['json']['format'] = True
    manager.add_formatter(JSONFormatter)
    args = main.parser.parse_args([
        'http', 'httpbin.org/get',
        '-f',
        '--json',
        '--json-indent', '2',
        '--json-sort-keys'
    ])
    args.formatter = manager.get_formatter(args)
    output_options = main.get_output_options(args)
    output = manager.get_output(args)
    assert isinstance(args.formatter, JSONFormatter)
    assert output_options['format'] == 'json'
   

# Generated at 2022-06-13 22:06:11.613148
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # Given
    json_string = '{ "string" : "test" }'
    mime = 'json'
    # When
    json_formatter = JSONFormatter()
    formatted_json = json_formatter.format_body(json_string, mime)
    # Then
    assert formatted_json == '{\n    "string": "test"\n}'

# Generated at 2022-06-13 22:06:17.857780
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # Test of format_body when the body is valid JSON but the mime isn't
    # json, javascript, or text
    jf = JSONFormatter(explicit_json=False)
    body = jf.format_body("{\"callerId\": 12, \"status\": \"FAILED\"}", "svg")
    assert body == "{\"callerId\": 12, \"status\": \"FAILED\"}"
    # Test of format_body when the body is valid JSON but the explicit_json
    # is False
    jf = JSONFormatter(explicit_json=False)
    body = jf.format_body("{\"callerId\": 12, \"status\": \"FAILED\"}", "json")
    assert body == "{\"callerId\": 12, \"status\": \"FAILED\"}"
    # Test of format

# Generated at 2022-06-13 22:06:26.899535
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():

    import json
    import pytest

    from httpie.plugins import JSONFormatter

    # Test a basic example
    j = JSONFormatter()
    body = '{"time":"2018-09-01T13:09:34.058354","results":[{"x":0,"y":6},{"x":1,"y":7},{"x":2,"y":8},{"x":3,"y":9},{"x":4,"y":10}]}'
    expected = json.loads(body)
    result = json.loads(j.format_body(body, 'json'))
    assert(result == expected)

    # Test with malformed json
    j = JSONFormatter()
    body = '{"time":"2018-09-01T13:09:34.058354","results":{}}'
    expected = body

# Generated at 2022-06-13 22:06:37.810694
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    from httpie.formatter import JSON_FORMAT_OPTIONS_MAP
    json_formatter = JSONFormatter({})
    # Test invalid JSON
    assert json_formatter.format_body('some json {', 'json') == 'some json {'
    # Test application/json type
    assert json.loads(json_formatter.format_body('{"foo":"bar"}', 'application/json')) == {'foo': 'bar'}
    # Test text/json type
    assert json.loads(json_formatter.format_body('{"foo":"bar"}', 'text/json')) == {'foo': 'bar'}
    # Test application/javascript type
    assert json.loads(json_formatter.format_body('{"foo":"bar"}', 'application/javascript')) == {'foo': 'bar'}
    #

# Generated at 2022-06-13 22:06:46.873850
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    from httpie.input import ParseResult
    kwargs = {'explicit_json': False}
    fp = JSONFormatter(**kwargs)
    source = "abc"
    assert source == fp.format_body(source, "application/json")
    source = '"abc"'
    assert source == fp.format_body(source, "application/json")
    source = '"a\\"b\\"c"'
    assert source == fp.format_body(source, "application/json")
    source = """[{"body": "OK"}]"""
    assert source == fp.format_body(source, "application/json")
    # Testing explicit_json without valid JSON should return raw input data
    kwargs['explicit_json'] = True
    fp = JSONFormatter(**kwargs)


# Generated at 2022-06-13 22:07:02.714375
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # Test 1: Output is normal
    input_body_1 = '{"foo": "bar"}'
    input_mime_1 = 'application/json'
    output_1 = json.dumps(
            obj = json.loads(input_body_1),
            sort_keys = False,
            ensure_ascii = False,
            indent = None
    )
    formatter_test_1 = JSONFormatter(
            format_options = {'json': {'format': True, 'indent': None, 'sort_keys': False}},
            explicit_json = False,
    )
    assert formatter_test_1.format_body(input_body_1, input_mime_1) == output_1

    # Test 2: Output is normal
    input_body_2 = '{"foo": "bar"}'

# Generated at 2022-06-13 22:07:11.819214
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # Test case 1 
    json_formatter = JSONFormatter(kwargs={'explicit_json':False},format_options={'json':{'format':True,'sort_keys':True,'indent':4}})
    body = '{ "firstName": "John", "lastName": "Smith", "age": 23 }'
    mime = 'json'
    assert(json_formatter.format_body(body=body,mime=mime)=='{\n    "age": 23,\n    "firstName": "John",\n    "lastName": "Smith"\n}'),'test_JSONFormatter_format_body() fails'

    # Test case 2

# Generated at 2022-06-13 22:07:22.124144
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    import mock
    import pytest

    # Create (mock) object with mock attribute format_options
    json_formatter = mock.MagicMock()
    json_formatter.format_options = {'json': {'format': True, 'sort_keys': False, 'indent': 4}}
    json_formatter.kwargs = {'explicit_json': False}

    # Check if formatting works
    body = '{"key": 1}'
    mime = 'javascript'
    expected_body = '{\n    "key": 1\n}'
    assert json_formatter.format_body(body, mime) == expected_body

    # Check if non-JSON is unchanged
    body = '<html><body>My webpage</body></html>'
    mime = 'html'
    assert json_formatter.format

# Generated at 2022-06-13 22:07:27.058024
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    json_formatter = JSONFormatter()
    assert json_formatter.format_body('{"foo": "bar"}', 'json') == '{\n    "foo": "bar"\n}'

# Generated at 2022-06-13 22:07:35.790098
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    import httpie.plugins
    httpie.plugins.JSONFormatter.register_JSONFormatter()
    JsonFormatter = httpie.plugins.JSONFormatter()

    body = r'{"foo":1,"bar":2}'
    mime = r'application/json'
    assert JsonFormatter.format_body(body, mime) == body
    
    body = r'{"foo":1,"bar":2}'
    mime = r'application/json'
    assert JsonFormatter.format_body(body, mime) == body
    
    body = r'{"foo":1,"bar":2}'
    mime = r'application/javascript'
    assert JsonFormatter.format_body(body, mime) == body
    
    body = r'{"foo":1,"bar":2}'

# Generated at 2022-06-13 22:07:45.739221
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():

    # Create a JSONFormatter object and call method format_body
    json_formatter = JSONFormatter()
    assert json_formatter.format_body('{"foo": "bar"}', 'json') == \
        '{\n    "foo": "bar"\n}'
    assert json_formatter.format_body('{"foo": "bar"}', 'javascript') == \
        '{\n    "foo": "bar"\n}'
    assert json_formatter.format_body('{"foo": "bar"}', 'text') == \
        '{\n    "foo": "bar"\n}'
    assert json_formatter.format_body('{"foo": "bar"}', 'foo') == \
        '{"foo": "bar"}'


# Generated at 2022-06-13 22:07:57.918570
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # Test JSON formatting is active
    body = '{"key":"value"}'
    formatter = JSONFormatter(explicit_json=False, format_options={
        'json': {
            'format': True,
            'sort_keys': True,
            'indent': 4,
            'align_keys': True,
        }
    })
    assert formatter.format_body(body, 'application/json') == """{
    "key": "value"
}"""

    # Test JSON formatting is inactive
    formatter = JSONFormatter(explicit_json=False, format_options={
        'json': {
            'format': False,
            'sort_keys': True,
            'indent': 4,
            'align_keys': True,
        }
    })

# Generated at 2022-06-13 22:08:08.334508
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formmater = JSONFormatter()

    # Valid JSON -> no change
    assert formmater.format_body('{"key": "value"}', 'application/json') == '{"key": "value"}'

    # Invalid JSON -> no change
    assert formmater.format_body('{"key: "value"}', 'application/javascript') == '{"key: "value"}'

    # Valid JSON -> indented
    assert formmater.format_body('{"key": "value"}', 'text/plain') == '{\n    "key": "value"\n}'

# Generated at 2022-06-13 22:08:19.738289
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():

        mime = 'application/json'
        body = '''{
            "array": [
                1,
                2,
                3
            ],
            "boolean": true,
            "null": null,
            "number": 123,
            "object": {
                "a": "b",
                "c": "d",
                "e": "f"
            },
            "string": "Hello World"
        }'''


# Generated at 2022-06-13 22:08:30.898189
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    class MockJSONFormatter:
        @staticmethod
        def format_body(body: str, mime: str):
            if body == 'response-body':
                return json.dumps(obj=json.loads(body), sort_keys=True, ensure_ascii=False, indent=4)
            elif body == 'invalid-json':
                return body
            else:
                return None

    mock_JSONFormatter = MockJSONFormatter()
    assert(mock_JSONFormatter.format_body('response-body', 'json') == '{\n    "response-body": "response-body"\n}')
    assert(mock_JSONFormatter.format_body('invalid-json', 'json') == 'invalid-json')

# Generated at 2022-06-13 22:09:00.453199
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    from httpie.plugins import FormatterPluginManager
    my_kwargs = {u'explicit_json': False, u'print_body_only': False}
    JSONFormatter_instance = JSONFormatter(**my_kwargs)
    FormatterPluginManager.__init__(JSONFormatter_instance, [], [])
    my_kwargs = {u'format_options': {u'json': {u'format': True, u'indent': 4, u'sort_keys': True}}}
    JSONFormatter_instance.__init__(**my_kwargs)
    # Test with JSON body
    my_body = u'{   \n   "key1" : "value1",\n "$key2" : "value2"\n}\n'
    my_mime = u'json'

# Generated at 2022-06-13 22:09:13.920081
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():

    # Test for normal JSON body
    body = '{"id":1,"name":"John","email":"john@example.com"}'
    mime = "application/json"
    assert JSONFormatter(explicit_json=True, format_options={'json': {'format': True, 'indent': 4, 'sort_keys': True}}).format_body(body, mime) == '{\n    "email": "john@example.com",\n    "id": 1,\n    "name": "John"\n}'

    # Test for normal JSON body
    body = '{"id":1,"name":"John","email":"john@example.com"}'
    mime = "text/plain"

# Generated at 2022-06-13 22:09:23.515265
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter(
        format_options={
            'json': {
                'format': True,
                'sort_keys': True,
                'indent': 4
            }
        },
        explicit_json=True
    )

# Generated at 2022-06-13 22:09:32.582051
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    json_formatter = JSONFormatter(explicit_json=False, format_options={'json': {'format': True, 'sort_keys': True, 'indent': 2}})

    # Valid JSON
    body = '{"a": 1, "b": 2, "c": 3}'
    assert json_formatter.format_body(body, "application/json") == \
           '{\n  "a": 1,\n  "b": 2,\n  "c": 3\n}'

    # Invalid JSON => no change
    body = '{"invalid": json'
    assert json_formatter.format_body(body, "application/json") == body

    # JSON in a mime that doesn't include "json" token => no change

# Generated at 2022-06-13 22:09:39.387404
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    assert JSONFormatter().format_body('{"foo": 42}', 'json') == '{\n    "foo": 42\n}'
    assert JSONFormatter(explicit_json=True).format_body('{"foo": 42}', 'json') == '{\n    "foo": 42\n}'
    assert JSONFormatter(explicit_json=True).format_body('<xml>foo</xml>', 'html') == '<xml>foo</xml>'

# Generated at 2022-06-13 22:09:50.575945
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    json_formatter = JSONFormatter(format_options={'json': {'format': True, 'sort_keys': False, 'indent': False}})

# Generated at 2022-06-13 22:09:52.681218
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter_plugin = JSONFormatter(explicit_json=False)

# Generated at 2022-06-13 22:10:05.577186
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    f = JSONFormatter()
    assert f.format_body('[1,2,3]', 'text/html') == '[1,2,3]'
    assert f.kwargs['explicit_json'] == False
    assert f.format_options['json']['sort_keys'] == False
    assert f.format_options['json']['indent'] == None

    f.kwargs['explicit_json'] = True
    assert f.format_body('[1,2,3]', 'text/html') == '[\n  1,\n  2,\n  3\n]'
    assert f.format_body('{"a":1}', 'application/json') == '{\n  "a": 1\n}'

    f.format_options['json']['sort_keys'] = True
    assert f

# Generated at 2022-06-13 22:10:15.181052
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    from httpie.core import main
    from httpie import ExitStatus

    # Invalid JSON
    json_string = '{"asd":234}'
    env = TestEnvironment(stdin=json_string,
                          stdin_isatty=False,
                          stdout_isatty=False)
    rv = main(env=env)
    assert rv == ExitStatus.OK
    assert env.stdout == json_string + '\n'
    assert env.stderr == ''

    # Not JSON
    json_string = 'sometext'
    env = TestEnvironment(stdin=json_string,
                          stdin_isatty=False,
                          stdout_isatty=False)
    rv = main(env=env)
    assert rv == ExitStatus.OK
    assert env

# Generated at 2022-06-13 22:10:20.733878
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    json_plugin = JSONFormatter(
        format_options={'json': {'format': True, 'sort_keys': True, 'indent': 4}},
        explicit_json=False, kwargs=None
    )
    formatted = json_plugin.format_body(
        '{"name": "Johnny", "age": 20}',
        'application/json'
    )
    assert formatted == '{\n    "age": 20,\n    "name": "Johnny"\n}'



# Generated at 2022-06-13 22:11:06.159173
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # Given
    json_data = '{"key1":"value1","key2":"value2"}'

    # When
    formatter = JSONFormatter(json={"format": True, "sort_keys": True, "indent": 4})
    result = formatter.format_body(json_data, 'json')

    # Then
    assert result == '''\
{\n    "key1": "value1",\n    "key2": "value2"\n}'''

# Generated at 2022-06-13 22:11:10.368637
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    f = JSONFormatter({"json": {"format": True}})
    # body = '{"message": "Hello world!"}'
    assert f.format_body('{"message": "Hello world!"}', 'application/json') == '{\n    "message": "Hello world!"\n}'

# Generated at 2022-06-13 22:11:18.662063
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    p = JSONFormatter(
        format_options={'json': {
            'format': True,
            'indent': 2,
            'sort_keys': True,
        }},
        explicit_json=False
    )
    assert p.format_body('{"a": 1, "b": ["2", 3]}', 'application/json') == '{\n  "a": 1,\n  "b": [\n    "2",\n    3\n  ]\n}'
    assert p.format_body('{"a": 1, "b": ["2", 3]}', 'text/plain') == '{\n  "a": 1,\n  "b": [\n    "2",\n    3\n  ]\n}'

# Generated at 2022-06-13 22:11:29.626002
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    import httpie.input
    import httpie.cli

    class TestJSONFormatter(JSONFormatter):

        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.kwargs = kwargs
            self.json_options = self.kwargs['json']

    # Set "pretty" mode
    json_options = httpie.cli.JSONOptions(
        sort_keys=True,
        indent=4,
        explicit=False,
    )

    # Create a formatter with "pretty" mode
    formatter = TestJSONFormatter(json=json_options)

    # Create a JSON object to format in memory
    json_object = b'{"key": "value", "int": 1, "longint": 12345678901234567890}'

    # Format the JSON

# Generated at 2022-06-13 22:11:40.400571
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    json_str = '{"a": "1", "b": "2", "c": {"d": "3"}, "e": ["4", "5"]}'
    body_test_data = [
        {'body': json_str, 'mime': 'application/json', 'expected': json_str},
        {'body': json_str, 'mime': 'text/json', 'expected': json_str},
        {'body': json_str, 'mime': 'text/javascript', 'expected': json_str},
        {'body': 'foo', 'mime': 'text/json', 'expected': 'foo'},
        {'body': '', 'mime': 'text/json', 'expected': ''},
        ]
