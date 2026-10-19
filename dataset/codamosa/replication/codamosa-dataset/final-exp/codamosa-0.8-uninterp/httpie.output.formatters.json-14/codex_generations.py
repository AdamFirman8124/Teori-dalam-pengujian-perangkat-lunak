

# Generated at 2022-06-13 22:01:55.471965
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():

    fp = JSONFormatter()

    body = '{"a": "b", "c": "d"}'
    mime = 'json'
    assert fp.format_body(body, mime) == '{\n    "a": "b",\n    "c": "d"\n}'

    body = '{"a": "b", "c": "d"}'
    mime = 'javascript'
    assert fp.format_body(body, mime) == '{\n    "a": "b",\n    "c": "d"\n}'

    body = '{"a": "b", "c": "d"}'
    mime = 'text'

# Generated at 2022-06-13 22:02:07.428109
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # Define the request with the JSON format
    request = {
        "method": "GET",
        "url": "http://127.0.0.1:5000/api/v1.0/users/1",
        "headers": {
            "Accept": "application/json"
        },
    }
    # Define the response of the request
    response = {
        "status": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": {
            "id": 1,
            "username": "admin",
            "email": "admin@admin.com",
            "password": "123456"
        }
    }

    # Initialize the object JSONFormatter
    formatter = JSONFormatter(**{})

    # Perform the format of the body
    body

# Generated at 2022-06-13 22:02:16.710677
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    from httpie.plugins.builtin import FormatterPlugin
    from httpie import ExitStatus
    from utils import http, HTTP_OK
    import json

    json_input = json.dumps({"field1":"value1","field2":"value2"})
    # check when indent is set to None
    json_options = {'json': {'format': True, 'indent': None, 'sort_keys': False}}
    json_env = {'HTTPIE_JSON_INDENT': None}
    r = http('--json', 'POST', 'http://httpbin.org/post', 'field1=value1', 'field2==value2',
             env=json_env, debug=True,
             config_dir=os.path.dirname(__file__),
             config_dict=json_options)
    assert r.exit

# Generated at 2022-06-13 22:02:19.670363
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter=JSONFormatter()
    assert formatter.format_body("abcdef","application/json") == "abcdef"

# Generated at 2022-06-13 22:02:31.111884
# Unit test for method format_body of class JSONFormatter

# Generated at 2022-06-13 22:02:38.194114
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter_json = JSONFormatter(explicit_json=False, format_options={'json': {'format': True, 'sort_keys': True, 'indent': 2}})
    assert json.dumps(
        obj=[1, 'simple', 'list'],
        sort_keys=True,
        ensure_ascii=False,
        indent=2
    ) == formatter_json.format_body(json.dumps([1, 'simple', 'list']), 'json')



# Generated at 2022-06-13 22:02:48.484544
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    test_formatter = JSONFormatter(
        format_options={
            'json': {
                'format': True,
                'sort_keys': True,
                'indent': 2
            }
        }, kwargs={'explicit_json': False}
    )

    # Valid JSON
    assert test_formatter.format_body('{"key":"value"}', '') == '{\n  "key": "value"\n}'

    # Valid JSON
    assert test_formatter.format_body('{"key":"value"}', 'json') == '{\n  "key": "value"\n}'

    # Invalid JSON
    assert test_formatter.format_body('{"key":"value"', '') == '{"key":"value"'



# Generated at 2022-06-13 22:02:53.829289
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter()
    body = '''{"data": [[1, 2], [3, 4]]}'''
    actual = formatter.format_body(body=body, mime='application/json')
    expected = '''{
    "data": [
        [
            1,
            2
        ],
        [
            3,
            4
        ]
    ]
}'''
    assert actual == expected

# Generated at 2022-06-13 22:03:04.226091
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    json_formatter = JSONFormatter()

    # Test case:
    body = '{"id":123,"value":"test value"}'
    mime = 'json'
    formatted_body = '{\n    "id": 123,\n    "value": "test value"\n}'
    # Assertion:
    assert json_formatter.format_body(body, mime) == formatted_body

    # Test case:
    body = 'not_json'
    mime = 'json'
    # Assertion:
    assert json_formatter.format_body(body, mime) == body

# Generated at 2022-06-13 22:03:15.000969
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    import json

# Generated at 2022-06-13 22:03:19.704298
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    jf = JSONFormatter()
    assert jf.enabled == True

# Generated at 2022-06-13 22:03:30.836591
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    j = JSONFormatter()
    assert j.format_body('{"key": "value"}','json') == '{\n    "key": "value"\n}'
    assert j.format_body('{"key": "value"}','text') == '{\n    "key": "value"\n}'
    assert j.format_body('{"key": "value"}','javascript') == '{\n    "key": "value"\n}'
    assert j.format_body('{"key": "value"}','image') == '{"key": "value"}'
    assert j.format_body('Not valid json','not valid') == 'Not valid json'

# Generated at 2022-06-13 22:03:35.914177
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    json_formatter = JSONFormatter()
    body = '{"key": "my_value"}'
    content_type = 'application/json'

    assert json_formatter.format_body(body=body, mime=content_type) == \
        '{\n    "key": "my_value"\n}'

# Generated at 2022-06-13 22:03:44.970648
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    from httpie.output.formatters.colors import get_lexer
    from jwt import encode
    from datetime import datetime, timedelta

    # Defining testing data
    test_data = {
        'sub': 'test@test.com',
        'iat': datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(seconds=60)
    }
    test_body = encode(test_data, 'secret', algorithm='HS256').decode('ascii')
    default_mime = 'json'
    lexer = get_lexer()

    # Define JSONFormatter instance with default values

# Generated at 2022-06-13 22:03:56.079950
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter_plugin_instance = JSONFormatter()
    body = formatter_plugin_instance.format_body(
        body=r'{"status": "OK", "code": 100}',
        mime='json'
    )
    assert body == '{\n  "code": 100, \n  "status": "OK"\n}'
    body = formatter_plugin_instance.format_body(
        body=r'{"status": "OK", "code": 100}',
        mime='text'  # This will also trigger the formatter.
    )
    assert body == '{\n  "code": 100, \n  "status": "OK"\n}'

# Generated at 2022-06-13 22:04:08.657308
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter(format_options = {'json':{'indent': 2, 'sort_keys': True}})

    assert formatter.format_body("""{ "key": "value" }""", 'json') == '{\n  "key": "value"\n}'
    assert formatter.format_body("""{ "key": "value" }""", 'text') == '{\n  "key": "value"\n}'
    assert formatter.format_body("""{ "key": "value" }""", 'javascript') == '{\n  "key": "value"\n}'
    assert formatter.format_body("""{ "key": "value" }""", 'text/html') == '{ "key": "value" }'


# Generated at 2022-06-13 22:04:09.895066
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    pass

# Generated at 2022-06-13 22:04:13.329647
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    result = JSONFormatter.format_body("{'a':1,'b':2}", "application/json")
    assert result == '{\n    "a": 1,\n    "b": 2\n}'



# Generated at 2022-06-13 22:04:26.769727
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # Preparation
    h = JSONFormatter()
    h.kwargs['explicit_json'] = False

    # Test
    body = b'{"key1":"value1","key2":3}'
    assert h.format_body(body, 'json') == body.decode('utf-8')

    body = b'{"key1":"value1","key2":3}'
    assert h.format_body(body, 'text') == body.decode('utf-8')

    body = '{"key1":"value1","key2":3}'
    assert h.format_body(body, 'json') == body

    body = '{"key1":"value1","key2":3}'
    assert h.format_body(body, 'text') == body


# Generated at 2022-06-13 22:04:39.450878
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter()
    body1 = '{"a": "b", "c": 123}'
    body2 = '{"a": "b"}'
    body3 = '{"a": "b", "c": 321}'
    body4 = '[1, 2, 3]'
    body5 = '[1, 2]'
    body6 = '[1, 2, 3, 4]'
    assert formatter.format_body(body1, 'json') == body1
    assert formatter.format_body(body2, 'json') == body2
    assert formatter.format_body(body3, 'json') == body3
    assert formatter.format_body(body4, 'application/json') == body4
    assert formatter.format_body(body5, 'application/json') == body5
    assert formatter.format

# Generated at 2022-06-13 22:05:01.371405
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    json_formatter = JSONFormatter(
        format_options={'json': {'format': True, 'indent': 4, 'sort_keys': True}},
        explicit_json=False,
    )
    # test 'json' in mime
    assert json_formatter.format_body('{"1": "2"}', 'json') == '{\n    "1": "2"\n}'
    # test 'javascript' in mime
    assert json_formatter.format_body('{"1": "2"}', 'javascript') == '{\n    "1": "2"\n}'
    # test 'text' in mime
    assert json_formatter.format_body('{"1": "2"}', 'text') == '{\n    "1": "2"\n}'
    # test invalid JSON
   

# Generated at 2022-06-13 22:05:04.092267
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    from .json_formatter_unit_test import test_JSONFormatter_format_body as test
    test()

# Generated at 2022-06-13 22:05:14.689770
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    """
    Create a testing instance of the class JSONFormatter in order to
    test the method format_body.
    """
    jsonFormatter = JSONFormatter()
    body = '{"name": "Jonas", "species": "human"}'
    mime = 'json'
    print(jsonFormatter.format_body(body, mime))
    body = "{'name': 'Jonas', 'species': 'human'}"
    mime = 'json'
    print(jsonFormatter.format_body(body, mime))
    body = '""'
    mime = 'json'
    print(jsonFormatter.format_body(body, mime))
    body = ''
    mime = 'json'
    print(jsonFormatter.format_body(body, mime))

# Generated at 2022-06-13 22:05:27.707525
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # Create one instance of class JSONFormatter with default value
    json_formatter_instance = JSONFormatter(**{
        'format_options': {
            'json': {
                'format': True,
                'indent': 2,
                'sort_keys': False,
            }
        },
        'explicit_json': False,
    })

    # Test the method format_body with body = '{"key": "value"}', mime = 'json'
    # The returned body is expected to be:
    # {
    #   "key": "value"
    # }
    body = '{"key": "value"}'
    mime = 'json'
    expected_body = '{\n  "key": "value"\n}'
    assert json_formatter_instance.format_body(body, mime)

# Generated at 2022-06-13 22:05:39.243357
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # without any options, format_body() function should return the same result with default JSON formatter
    json_test_temp = JSONFormatter()
    assert json_test_temp.format_body('{"test_key":"test_value"}', '') == json.dumps({"test_key": "test_value"}, ensure_ascii=False)

    # if the mime type is json/javascript/text, default formatter should return the same result as before
    assert json_test_temp.format_body('{"test_key":"test_value"}', 'json;utf-8') == json.dumps({"test_key": "test_value"}, ensure_ascii=False)

# Generated at 2022-06-13 22:05:50.035499
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    f = JSONFormatter()

    ###
    # Test case 1: body is JSON and should be pretty printed
    ###
    body = '{"a": 1, "b": "string", "c": true, "d": [1, 2, 3], "e": {"f": 4}}'
    expected_result = ('{\n'
                       '    "a": 1,\n'
                       '    "b": "string",\n'
                       '    "c": true,\n'
                       '    "d": [\n'
                       '        1,\n'
                       '        2,\n'
                       '        3\n'
                       '    ],\n'
                       '    "e": {\n'
                       '        "f": 4\n'
                       '    }\n'
                       '}')

# Generated at 2022-06-13 22:05:59.190806
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # Given
    body = '{"a": 1, "c": 2, "b": 3}'
    format_options = {'json': {'format': True, 'indent': 2, 'sort_keys': True}}
    kwargs = {'explicit_json': True}
    formatter = JSONFormatter(format_options=format_options, **kwargs)
    # When
    body = formatter.format_body(body, 'application/json')
    # Then
    assert body == '{\n  "a": 1,\n  "b": 3,\n  "c": 2\n}'

# Generated at 2022-06-13 22:06:05.849280
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    from httpie.output.streams import BytesIO
    formatter = JSONFormatter(kwargs={'explicit_json': True},
                              format_options={'json': {'format': True,
                                                       'indent': 4,
                                                       'sort_keys': True}})
    input_data = (b'{"a": 2, "b": [1, 2]}', 'application/json')
    expected_output = b'{\n    "a": 2,\n    "b": [\n        1,\n        2\n    ]\n}'
    actual_output = formatter.format_body(*input_data)
    assert actual_output == expected_output
    input_data = (b'{"a": 1, "b": [1, 2]}', 'application/javascript')
    expected_output

# Generated at 2022-06-13 22:06:15.249337
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    class kwargs():
        explicit_json = False

    class format_options():
        json = {
            'format': False,
            'indent': 4,
            'sort_keys': True,
        }


# Generated at 2022-06-13 22:06:26.172201
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # MIME type is not json and the option explicit_json is not set.
    assert JSONFormatter(format_options={'json': {'format': True, 'indent': None, 'sort_keys': False}},
                         explicit_json=False).format_body(
        '{"foo": "bar", "key": "value"}',
        'text/plain') == '{"foo": "bar", "key": "value"}'

    # MIME type is json and the option explicit_json is set.